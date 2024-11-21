# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=131.0.6778.86-1
PKG_RELEASE:=1

# intel 80386 & riscv64 & cortex-a76
ifeq ($(ARCH_PREBUILT),aarch64_cortex-a76)
  ARCH_PREBUILT:=aarch64_generic
else ifeq ($(ARCH_PREBUILT),i386_pentium-mmx)
  ARCH_PREBUILT:=x86
else ifeq ($(ARCH_PREBUILT),i386_pentium4)
  ARCH_PREBUILT:=x86
else ifeq ($(ARCH_PREBUILT),riscv64_riscv64)
  ARCH_PREBUILT:=riscv64
endif

ifeq ($(ARCH_PACKAGES),aarch64_cortex-a53)
  PKG_HASH:=e3ce0121aaf350fc146e06a80b4630050edf04d993436749100f119a1b6976e5
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=f7f3077c19ea485feb85aa5a82490901deb5433870e3d28ffaa4b16f32b2526c
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=9fd80e26f236ad290ef994b9d75a900861f23e8ad956dca0d2152df97f25cd75
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=dc31a9ba7e6c7b6c12fc7e46d75a99768d8cb5158c35aa32bd00a89a78799185
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=a7d6e53cc0e1ab87e0ced01ff01ab32bcfccbbd3db91c618c13161d74a675844
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=a77396d9a8372a6f5dcb07d625e099841fca28a3a0ae295959813d548fc953e9
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=2b9306942a692f606e4d169a5acff4e8b7e6c7fc4df445d0372eecfdbba4b0c7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=1c7aa990f95d403c53a8f40db2d1e4810edc4c1a89b9ddbb641417c3cae01578
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=e4335b98232fbce1920d3daf238da42f0e4b04ec1f13f53e53e443e086025c14
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=07b8de01bf42fa58f3a1a8e1c103914d7ab75361b3369b0d13abab88b47ac5d4
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=aefc8267919f638ea07ebd8a1fc07d2e08c223d9f997a0fdf7cbe9cdb464b9cc
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=8529aa579235dbf4cef39d639ec86b7fe7965244cf5eb4bbb474442da218e474
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=ae62a55da1b9bae187037337a5e123fd1af374ed4ed45dbf098336091f1361ef
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=760e2ee225a051defde873686a779f4605cb2a41c842d57ce2c24ff5037267e2
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=453e5c475fa361d2d5705ea902dc95690145c1008735c4b4a8c64238f700e244
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=080cf9016228ce231acda3969155d62da15085c0617f880a9efe497a8016f25d
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=6085a39eb46ace69fb9eacb6f1d9b00c167dee4e85b205ed277a42223a6fc07f
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=9c45bd94d0efb70c112453b911a6e24fe6fc998d8048e916726adbb9396d54d2
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=4ce2d5d65a4296c356b285346e8b423202c4a527f68d69da993287fe60c8e4fd
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=b981dd9e5eed9bea14edd5f21f3cf03fd6dd0ae81f43471c9cc7ec1682c22662
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=a628a7cf69110facbeb8b657785683a12db45f982f14534d67401197a867b28f
else
  PKG_HASH:=dummy
endif

PKG_SOURCE:=naiveproxy-v$(PKG_VERSION)-openwrt-$(ARCH_PACKAGES).tar.xz
PKG_SOURCE_URL:=https://github.com/klzgrad/naiveproxy/releases/download/v$(PKG_VERSION)/
PKG_BUILD_DIR:=$(BUILD_DIR)/naiveproxy-v$(PKG_VERSION)-openwrt-$(ARCH_PACKAGES)

PKG_LICENSE:=BSD 3-Clause
PKG_LICENSE_FILES:=LICENSE
PKG_MAINTAINER:=sbwml <admin@cooluc.com>

include $(INCLUDE_DIR)/package.mk

define Package/naiveproxy
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=Web Servers/Proxies
  TITLE:=Make a fortune quietly
  URL:=https://github.com/klzgrad/naiveproxy
  DEPENDS:=@(aarch64||arm||i386||mipsel||riscv64||x86_64) +libatomic
endef

define Package/naiveproxy/description
  NaïveProxy uses Chrome's network stack to camouflage traffic with strong
  censorship resistance and low detectability. Reusing Chrome's stack also
  ensures best practices in performance and security.
endef

define Package/naiveproxy/conffiles
/etc/config/naiveproxy
endef

define Build/Compile
endef

define Package/naiveproxy/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/naive $(1)/usr/bin/naive
	$(INSTALL_DIR) $(1)/etc/config $(1)/etc/init.d
	$(INSTALL_CONF) $(CURDIR)/files/naiveproxy.config $(1)/etc/config/naiveproxy
	$(INSTALL_BIN) $(CURDIR)/files/naiveproxy.init $(1)/etc/init.d/naiveproxy
endef

$(eval $(call BuildPackage,naiveproxy))
