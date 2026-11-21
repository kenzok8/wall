#!/usr/bin/env python3

import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path


API_URL = "https://api.github.com/repos/upx/upx/releases/latest"
MAKEFILE = Path("upx-static/Makefile")
UPX_MAKEFILE = Path("upx/Makefile")

ARCHES = {
    "amd64": "x86_64",
    "i386": "i386",
    "arm64": "aarch64",
    "arm": "arm",
    "armeb": "armeb",
    "mipsel": "mipsel",
    "mips": "mips",
    "powerpc": "powerpc",
    "powerpc64le": "powerpc64",
    "riscv64": "riscv64",
}


def fetch_json(url: str):
    headers = {"Accept": "application/vnd.github+json"}
    # Unauthenticated API calls share 60 req/hour per runner egress IP and
    # fail with 403 "rate limit exceeded"; the workflow passes GITHUB_TOKEN.
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def sha256_url(url: str) -> str:
    req = urllib.request.Request(url, headers={"Accept": "application/octet-stream"})
    h = hashlib.sha256()
    with urllib.request.urlopen(req) as resp:
        while True:
            chunk = resp.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def render_hash_block(hashes):
    lines = ["# AUTO-GENERATED HASHES BEGIN"]
    ordered = list(ARCHES.keys())
    for i, upx_arch in enumerate(ordered):
        prefix = "ifeq" if i == 0 else "else ifeq"
        lines.append(f"{prefix} ($(UPX_ARCH),{upx_arch})")
        lines.append(f"  PKG_HASH:={hashes[upx_arch]}")
    lines.append("else")
    lines.append("  $(error Unsupported UPX_ARCH '$(UPX_ARCH)' for upx-static)")
    lines.append("endif")
    lines.append("# AUTO-GENERATED HASHES END")
    return "\n".join(lines)


def main() -> int:
    if not MAKEFILE.exists():
        raise SystemExit(f"missing makefile: {MAKEFILE}")
    if not UPX_MAKEFILE.exists():
        raise SystemExit(f"missing makefile: {UPX_MAKEFILE}")

    release = fetch_json(API_URL)
    tag = release["tag_name"]
    version = tag.removeprefix("v")

    assets = {asset["name"]: asset for asset in release.get("assets", [])}
    hashes = {}
    for upx_arch in ARCHES:
        name = f"upx-{version}-{upx_arch}_linux.tar.xz"
        asset = assets.get(name)
        if not asset:
            raise SystemExit(f"missing release asset: {name}")
        # Prefer the sha256 the API already provides; avoids downloading every
        # tarball (slow and prone to download-CDN 504s). Fall back to download
        # only when an older release has no digest field.
        digest = asset.get("digest") or ""
        if digest.startswith("sha256:"):
            hashes[upx_arch] = digest.split(":", 1)[1]
        else:
            print(f"hashing {name} (no API digest)", file=sys.stderr)
            hashes[upx_arch] = sha256_url(asset["browser_download_url"])

    # Source package (upx): single hash for the source tarball.
    src_name = f"upx-{version}-src.tar.xz"
    src_asset = assets.get(src_name)
    if not src_asset:
        raise SystemExit(f"missing release asset: {src_name}")
    src_digest = src_asset.get("digest") or ""
    if src_digest.startswith("sha256:"):
        src_hash = src_digest.split(":", 1)[1]
    else:
        print(f"hashing {src_name} (no API digest)", file=sys.stderr)
        src_hash = sha256_url(src_asset["browser_download_url"])

    text = MAKEFILE.read_text()
    text = re.sub(r"^PKG_VERSION:=.*$", f"PKG_VERSION:={version}", text, count=1, flags=re.M)
    text = re.sub(r"^PKG_RELEASE:=.*$", "PKG_RELEASE:=1", text, count=1, flags=re.M)
    text = re.sub(r"^PKG_SOURCE_VERSION:=.*$", f"PKG_SOURCE_VERSION:=v{version}", text, count=1, flags=re.M)
    text = re.sub(
        r"# AUTO-GENERATED HASHES BEGIN\n.*?# AUTO-GENERATED HASHES END",
        render_hash_block(hashes),
        text,
        count=1,
        flags=re.S,
    )
    MAKEFILE.write_text(text)
    print(f"updated {MAKEFILE} to {version}")

    upx_text = UPX_MAKEFILE.read_text()
    upx_text = re.sub(r"^PKG_VERSION:=.*$", f"PKG_VERSION:={version}", upx_text, count=1, flags=re.M)
    upx_text = re.sub(r"^PKG_RELEASE:=.*$", "PKG_RELEASE:=1", upx_text, count=1, flags=re.M)
    upx_text = re.sub(r"^PKG_HASH:=.*$", f"PKG_HASH:={src_hash}", upx_text, count=1, flags=re.M)
    UPX_MAKEFILE.write_text(upx_text)
    print(f"updated {UPX_MAKEFILE} to {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
