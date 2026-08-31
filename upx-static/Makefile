
# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) kenzok8 <https://github.com/kenzok8>

include $(TOPDIR)/rules.mk

PKG_NAME:=upx-static
PKG_VERSION:=5.2.1
PKG_RELEASE:=1
PKG_SOURCE_VERSION:=v5.2.1

# Map OpenWrt $(ARCH) to UPX pre-built binary arch name.
# NOTE: OpenWrt uses "aarch64", UPX tarball uses "arm64".
UPX_ARCH:=$(ARCH)
ifeq ($(findstring x86_64,$(ARCH)),x86_64)
  UPX_ARCH:=amd64
else ifeq ($(findstring i386,$(ARCH)),i386)
  UPX_ARCH:=i386
else ifeq ($(findstring aarch64,$(ARCH)),aarch64)
  UPX_ARCH:=arm64
else ifeq ($(findstring arm,$(ARCH)),arm)
  UPX_ARCH:=arm
else ifeq ($(findstring armeb,$(ARCH)),armeb)
  UPX_ARCH:=armeb
else ifeq ($(findstring mipsel,$(ARCH)),mipsel)
  UPX_ARCH:=mipsel
else ifeq ($(findstring mips,$(ARCH)),mips)
  UPX_ARCH:=mips
else ifeq ($(findstring powerpc,$(ARCH)),powerpc)
  UPX_ARCH:=powerpc
else ifeq ($(findstring powerpc64,$(ARCH)),powerpc64)
  UPX_ARCH:=powerpc64le
else ifeq ($(findstring riscv64,$(ARCH)),riscv64)
  UPX_ARCH:=riscv64
endif

PKG_SOURCE:=upx-$(PKG_VERSION)-$(UPX_ARCH)_linux.tar.xz
PKG_SOURCE_URL:=https://github.com/upx/upx/releases/download/$(PKG_SOURCE_VERSION)

# AUTO-GENERATED HASHES BEGIN
ifeq ($(UPX_ARCH),amd64)
  PKG_HASH:=402162aad30af47e60dbd767fb2e64ca394ace9727ba1f40283641f1d1b91657
else ifeq ($(UPX_ARCH),i386)
  PKG_HASH:=44b505d881337ef17ad03f03fd80f2ecdebc3a36077e1dd260ae1b359c713ba5
else ifeq ($(UPX_ARCH),arm64)
  PKG_HASH:=a72d112c5970a904a31da0b9c84f919bc16b9a311787c12245508544a78c7d36
else ifeq ($(UPX_ARCH),arm)
  PKG_HASH:=d74c0d8bfdd7aad9114470efaa14fa889158f3dbfbc7128ba76c403aee545ef8
else ifeq ($(UPX_ARCH),armeb)
  PKG_HASH:=31ac41b612c4c1166dc7a7c194e2ad8fadcf9fdf25aa4bd3c14799823b9e5f9e
else ifeq ($(UPX_ARCH),mipsel)
  PKG_HASH:=84fc6c0c33ed668c099d4f82d72ac7fd4070b19797ebb990f999278267b94e0d
else ifeq ($(UPX_ARCH),mips)
  PKG_HASH:=d2cd981ff725a31f9f596f80fcc5c1682e648a59231e220a3967c661c6d1fafb
else ifeq ($(UPX_ARCH),powerpc)
  PKG_HASH:=5f89a57f6e76c5b16016330ee5a2ca87f9bfbdcca5420bc042a1fde1798818ed
else ifeq ($(UPX_ARCH),powerpc64le)
  PKG_HASH:=e914046633567c3255a6440bae4d6c13d9f90d458445b47b8474b048ca4072b7
else ifeq ($(UPX_ARCH),riscv64)
  PKG_HASH:=a8663b4cb6523104a8a807362d0da6f5d6d55f6083152f78fa27fa9c05443c17
else
  $(error Unsupported UPX_ARCH '$(UPX_ARCH)' for upx-static)
endif
# AUTO-GENERATED HASHES END

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SUBMENU:=Compression
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=UPX - The Ultimate Packer for eXecutables
  URL:=https://upx.github.io
endef

define Package/$(PKG_NAME)/description
  UPX is a free, portable, extendable, high-performance executable
  packer for several executable formats. This package installs the
  statically-linked pre-built binary from the official upstream release.
endef

define Build/Prepare
	rm -rf $(PKG_BUILD_DIR)
	mkdir -p $(PKG_BUILD_DIR)
	tar -xJf $(DL_DIR)/$(PKG_SOURCE) -C $(PKG_BUILD_DIR) --strip-components=1
endef

define Build/Compile
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/upx $(1)/bin/upx
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
