#!/usr/bin/env python3

import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path


API_URL = "https://api.github.com/repos/upx/upx/releases/latest"
MAKEFILE = Path("upx-static/Makefile")

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
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
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

    release = fetch_json(API_URL)
    tag = release["tag_name"]
    version = tag.removeprefix("v")

    assets = {asset["name"]: asset["browser_download_url"] for asset in release.get("assets", [])}
    hashes = {}
    for upx_arch in ARCHES:
        name = f"upx-{version}-{upx_arch}_linux.tar.xz"
        url = assets.get(name)
        if not url:
            raise SystemExit(f"missing release asset: {name}")
        print(f"hashing {name}", file=sys.stderr)
        hashes[upx_arch] = sha256_url(url)

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
