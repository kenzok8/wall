# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2023 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=chinadns-ng
PKG_VERSION:=2023.10.28
PKG_RELEASE:=1

PKG_SOURCE_URL:=https://github.com/zfl9/chinadns-ng/releases/download/$(PKG_VERSION)
UNPACK_CMD=$(CP) $(DL_DIR)/$(PKG_SOURCE) $(PKG_BUILD_DIR)/chinadns-ng

ifeq ($(ARCH),aarch64)
  PKG_SOURCE:=chinadns-ng@aarch64-linux-musl@generic+v8a@fast+lto
  PKG_HASH:=skip
else ifeq ($(ARCH),arm)
  ARM_CPU_FEATURES:=$(word 2,$(subst +,$(space),$(call qstrip,$(CONFIG_CPU_TYPE))))
  ifeq ($(ARM_CPU_FEATURES),)
    PKG_SOURCE:=chinadns-ng@arm-linux-musleabi@generic+v7a@fast+lto
    PKG_HASH:=0c77f8d7631cca22d1816a90655b407b9f82bbb349ac221d12a9a26da6c72dcb
  else
    PKG_SOURCE:=chinadns-ng@arm-linux-musleabihf@generic+v7a@fast+lto
    PKG_HASH:=skip
  endif
else ifeq ($(ARCH),mips)
  PKG_SOURCE:=chinadns-ng@mips-linux-musl@mips32@fast+lto
  PKG_HASH:=skip
else ifeq ($(ARCH),mipsel)
  PKG_SOURCE:=chinadns-ng@mipsel-linux-musl@mips32@fast+lto
  PKG_HASH:=skip
else ifeq ($(ARCH),i386)
  PKG_SOURCE:=chinadns-ng@i386-linux-musl@i686@fast+lto
  PKG_HASH:=skip
else ifeq ($(ARCH),x86_64)
  PKG_SOURCE:=chinadns-ng@x86_64-linux-musl@x86_64@fast+lto
  PKG_HASH:=skip
else
  PKG_SOURCE:=dummy
  PKG_HASH:=dummy
endif

PKG_LICENSE:=AGPL-3.0-only
PKG_LICENSE_FILES:=LICENSE
PKG_MAINTAINER:=pexcn <i@pexcn.me>

include $(INCLUDE_DIR)/package.mk

define Package/chinadns-ng
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=IP Addresses and Names
  TITLE:=ChinaDNS next generation, refactoring with epoll and ipset.
  URL:=https://github.com/zfl9/chinadns-ng
  DEPENDS:=@(aarch64||arm||i386||mips||mipsel||x86_64) @!(TARGET_x86_geode||TARGET_x86_legacy) +ipset
endef

define Build/Compile
endef

define Package/chinadns-ng/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/chinadns-ng $(1)/usr/bin
endef

$(eval $(call BuildPackage,chinadns-ng))
