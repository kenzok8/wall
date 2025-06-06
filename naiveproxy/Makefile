# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=137.0.7151.44-2
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
  PKG_HASH:=db0527adea0cde274873c28c0562c00f9aff7488ce02bf582ebbb3bf22f198fd
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=81be558b8f478c20ebad5130d06766e2b2b662ff50cfcb284f8793111296392a
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=b89ed151af96a3ae96b12bc5afc6d875d42bf675c20357c6ae949e347171e849
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=29d3585aa2cb790d15803a25d3fd4a831296bdb4ae3eaa2f0ac52b5bc09abba4
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=beccdfae464ef7e8cd5575cc1e9f9c6e2512a78b441c3f0249402548b10557e7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=76dcb85944194bf5cb7caa971696cb74dd134167afa37b4a5476562932a9aac1
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=3f62e2f52423b2983a6ef569e99c797ac1322a34afbd0a6288514a7e936ec124
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=fa1c3cb597f41b6773079e83e42759347c300e90cc3f5c785352d265ca0e902c
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=25123b03d30add7b91bb265b26ec9533749b50f1e42c12dec709e593e8a5dc11
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=0f7f19b24ca5c60dbfb2b9979fe1e814843909803557e04a9c06e921b8e2b6dd
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=36ca82512e740e3967f556b45a58d0eb2e0df0cb189f1d7a354589c78a467c1e
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=1895d5d943abdab61f4d518700dcf21167f6e633213ee2fe438e5782e3a8c39a
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=13478da67df395e4e2cc37ffab22b2875d9a88cd0ec14b7af7f9936f0364b471
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=efd1a5a5f19c5a14991f8f607a9e636be7e205fdac5afbaeb811c26762583f28
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=f4999013284a30f7d0b092b16282c4e191989e3bbfa85e6b1083b2d35551119b
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=f2d12e524f0efe69435babdffeee9b49a9d68549326ad4c9374c2dd39acb0998
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=985844a518da495279d3b5d3eb46b3e17fccb0795bfdf909aef934a07e5834df
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=4e677e87a15b5a99eb365b0d26afd9157fa4f8df63240c8800d6ceb7c0d769a3
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=deceede3b36871a785ece5f1465517b7cfa42d014f5c21eb23a4ea9b6821d4a8
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=41b13c2a568b55b96122edc298f584a697238a80a5a240e74cd52ca578a57d29
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=11aa1d023d87075f102cadeb07780bdf3543cc47fd027e512ce7a292c582bd35
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
