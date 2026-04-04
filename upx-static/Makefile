
# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) kenzok8 <https://github.com/kenzok8>

include $(TOPDIR)/rules.mk

PKG_NAME:=upx-static
PKG_VERSION:=5.1.1
PKG_RELEASE:=1
PKG_SOURCE_VERSION:=v5.1.1

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
  PKG_HASH:=1ff660454227861e00772f743f66b900072116b9dc24f6ee28b97cce88a7828a
else ifeq ($(UPX_ARCH),i386)
  PKG_HASH:=54242a7f1fa05ecc254c83fac89437987af19492f0b27a3def1cdcf4746f8053
else ifeq ($(UPX_ARCH),arm64)
  PKG_HASH:=a307c2c821eeab47607ba5c232408b22ab884cca13884682508b98f7308b8443
else ifeq ($(UPX_ARCH),arm)
  PKG_HASH:=0d0ac4c2fd367ccf595522487db118a7ef07e31146ff3cebefe4b34381a00a78
else ifeq ($(UPX_ARCH),armeb)
  PKG_HASH:=46bcea55c16eb420df8567025b75bda6516ef1cb4b0b4e232a4a28f55f0add6c
else ifeq ($(UPX_ARCH),mipsel)
  PKG_HASH:=6e2c901c927be893141fa680ff4b86c3ac48d8390e6505db2fcf3a7ccd0c599b
else ifeq ($(UPX_ARCH),mips)
  PKG_HASH:=15d3949dd620a86ebff7622201c1b81b00677face68ab7d179b9e72b003759c9
else ifeq ($(UPX_ARCH),powerpc)
  PKG_HASH:=81bb6703ee02bd8b0664a8265fd607dccac606976c958d09333c4ed038aea2bf
else ifeq ($(UPX_ARCH),powerpc64le)
  PKG_HASH:=d8789d959f0a2fdd07890ebb332173a9b076cb6db2cb1fb22a2699ffd9f884c6
else ifeq ($(UPX_ARCH),riscv64)
  PKG_HASH:=8dec678ddcafb61837ecd59810f6ad89dfd30edd84333441aff44e088d4b7898
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
