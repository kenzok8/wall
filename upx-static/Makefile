
# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) kenzok8 <https://github.com/kenzok8>

include $(TOPDIR)/rules.mk

PKG_NAME:=upx-static
PKG_VERSION:=5.3.0
PKG_RELEASE:=1
PKG_SOURCE_VERSION:=v5.3.0

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
  PKG_HASH:=79cea8a50b6fa102d10c7b79a419cd77dead3cc2d78661de2dc5e5815dc505c1
else ifeq ($(UPX_ARCH),i386)
  PKG_HASH:=d5ff15dfd7649d08970ffa86c9bae656b9fe3831285dd62db0ba7eabc6a3eae9
else ifeq ($(UPX_ARCH),arm64)
  PKG_HASH:=2a4afa860ac7aa6968f88df7841823746e5d00ba56affdf9342c2f5254fb776f
else ifeq ($(UPX_ARCH),arm)
  PKG_HASH:=541c8fc5e0ab43ae57273374215e6efe023aa43c2d5cf1e52a316a94a367bee5
else ifeq ($(UPX_ARCH),armeb)
  PKG_HASH:=770e62b1a60b7fd281c34556e321566827f57a5eb77cd4976280b92df565b6f0
else ifeq ($(UPX_ARCH),mipsel)
  PKG_HASH:=a4e6dc515aede12aeec7e8169a5f4c96da41cc58b5c834d8b6b7bddd015bb59d
else ifeq ($(UPX_ARCH),mips)
  PKG_HASH:=84c3203cf70d17ced90b777bf843e412ebc7a586cb4ee1e4c9a4801227131bc6
else ifeq ($(UPX_ARCH),powerpc)
  PKG_HASH:=2996e46af638fc20aa019f6c950ac91a829af0dae33fbfeca62012a310b995bb
else ifeq ($(UPX_ARCH),powerpc64le)
  PKG_HASH:=2102aa6c2e9fcdb147b27404bf87fc8f545327982ec9685efa5418be55be3480
else ifeq ($(UPX_ARCH),riscv64)
  PKG_HASH:=5a0663f369078cb069ac50252c9c8ca65a146307b7e6078c6f54f3bd146441ca
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
