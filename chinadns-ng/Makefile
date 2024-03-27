# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2023 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=chinadns-ng
PKG_VERSION:=2024.03.27
PKG_RELEASE:=1

PKG_SOURCE_URL:=https://github.com/zfl9/chinadns-ng/releases/download/$(PKG_VERSION)
UNPACK_CMD=$(CP) $(DL_DIR)/$(PKG_SOURCE) $(PKG_BUILD_DIR)/chinadns-ng

ifeq ($(ARCH),aarch64)
  PKG_SOURCE:=chinadns-ng@aarch64-linux-musl@generic+v8a@fast+lto
  PKG_HASH:=cd53686626f678fff3122b61aabee6c3bf9dad7e7577a8efc5f432fdeaf8d975
else ifeq ($(ARCH),arm)
  ARM_CPU_FEATURES:=$(word 2,$(subst +,$(space),$(call qstrip,$(CONFIG_CPU_TYPE))))
  ifeq ($(ARM_CPU_FEATURES),)
    PKG_SOURCE:=chinadns-ng@arm-linux-musleabi@generic+v7a@fast+lto
    PKG_HASH:=c2e0378e20f5fda376d4f52bfbe1a3dbc7dfe23879e8edc8ef7ab55694cfd676
  else
    PKG_SOURCE:=chinadns-ng@arm-linux-musleabihf@generic+v7a@fast+lto
    PKG_HASH:=d065c7d55b6c43b20dbb668d7bdafabe371c3360cc75bd0279cc2d7a83e342e9
  endif
else ifeq ($(ARCH),mips)
  PKG_SOURCE:=chinadns-ng@mips-linux-musl@mips32+soft_float@fast+lto
  PKG_HASH:=2170011ecf8ee29057d805eb8054bcc4366b759f454c063f0a258c84403e416e
else ifeq ($(ARCH),mipsel)
  PKG_SOURCE:=chinadns-ng@mipsel-linux-musl@mips32+soft_float@fast+lto
  PKG_HASH:=26aa029b141a3d25e078c4b92c06c93a87c06b0516e86c13d32a9ee865dd2ca2
else ifeq ($(ARCH),i386)
  PKG_SOURCE:=chinadns-ng@i386-linux-musl@i686@fast+lto
  PKG_HASH:=bf22fb35fba5e9b1174b0334a5473d4db8b3f85e489cec5af94f9a92f7c9787b
else ifeq ($(ARCH),x86_64)
  PKG_SOURCE:=chinadns-ng@x86_64-linux-musl@x86_64@fast+lto
  PKG_HASH:=8adf68d15068a3a27588772deb19be0a9804077a075aa8dad9dafa12a154c529
else
  PKG_SOURCE:=dummy
  PKG_HASH:=dummy
endif

PKG_LICENSE:=AGPL-3.0-only
PKG_LICENSE_FILES:=LICENSE
PKG_MAINTAINER:=sbwml <admin@cooluc.com>

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
