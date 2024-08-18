# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=128.0.6613.40-1
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
  PKG_HASH:=56c8157d88075a8ee2206420ab640a1f07ad88cb23ee2f2e9ddc57c2bb9ba195
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=aa7f5b0297d1f66210752457eee5bdb564872fe532b5c62309309f8d77abe3b8
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=6f5a57edec4439725df011909319002748f2b2cfbf5a0386c42a97eb2cdf864f
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=1611f9d1259089364ccc541a080b223d3de5d198a85dabee65bd03762b535bcf
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=526cb5f271ed82c1251548d26d5265449853105ea91af6731be9df93810d7dcc
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=565d6431547bdcfcbaddeb2aa5029e7fa975b19846824820a5f515e59575d573
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=23b3dd33b0742ff7aa50f8b7191d8426d7e360805dd9583e6d7a149bfc3169fa
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=e17edc19cb1890e202b036ec8522c42ef4d3ab3253028e0e88d17559e3ce2630
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=1d93b157f7332e8ff13dca658e36b5173a1f482e07d2e0840c6f4b316ef287c7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=78b0a8c969ba2f577c3ab2c6dd103f720a63d768080017263813e5f53d1d0987
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=883768f3c0e8ead66bda75dc79e6d49e16581ef8b1c1cde0c7629073b5ac92e0
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=df87743c510247e3025a3e5ec56370e4fd989448c52d5065fb92a374f3869f68
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=7aa2743d5ae233b0fe3c56bee89fb289cb5291c8f5c2d54b14c372c16098454b
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=601aec7c6b7382a4f778c73c81be5ac243695789636bab42d5171cbdb46728d7
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=c077e2387a9a49883e23e4fffe35622932ea8068fae4a45f491cd6490183e5f6
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=e4e256500a8c312ebff4b6ada2e1a3a997bed61b0c6c399d2ee6493d9b0a1fba
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=2074e25c712619ea182ba8ed548b82accc14d2533ddb63de210b18c57c120ea5
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=98963a397406082cd2b236f701b7e696b0814677485eccbf60332d47ed54cc28
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=ca347b75ba47a80105fb915f1b85b4f1654a05a6b437244715ee6bd4310bf771
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=6594a79adae775045168ca4609a9bde9204f46af76b56a20f4bf524c65824ac4
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=9ec9f71c8817c89372e47465547276d941b9668fcc6f4bc2e2159e13d7db9291
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
