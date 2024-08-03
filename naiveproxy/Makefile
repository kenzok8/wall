# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=127.0.6533.64-2
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
  PKG_HASH:=76d6bf0891d72f2083f497aba44e9e7eb86ad420b5556a5c01857cfafb567b18
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=5e1ec15ec4fb1145a64f5befb18c49b9b970438bba57dd8d5c6a9043803bcf8d
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=a228558aa327c450e8631a8f855669f18801ea17f5efb1c32eced495e5b84597
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=7f90787828eb2bb2a957e70da4f9e500b4abd1bf7a9ff6ef2636a004e5314a2f
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=d9fb0c29f7c6b79afc0375751859b0db673d3355c0a5a69762f763de5d54b38e
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=0d378b74c59025973c2f9e8577bc514be6601fc191c3cbbbabad427793fc4df9
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=72433296d6417ee0edce2246e4c107f71253b1b2dd6cd6cf89da8e462a381a05
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=868ac8c97f6e8a7b4097e1a20b46c723a1caa31508e3844d470b38f820ef5976
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=ddb14e435dc396c5228647bc15fb2e3cbd49a15a5fc2c280a11417b0ad0d37c9
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=fc7a83ab309dcdf7f3ea2ed44ad9a37b3efedfb850372042bb8853e3b3bb784d
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=5eb32a09c30a7932bfe20bca6226d459eef7517796ea38065446b2bbaee8e0cc
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=aba4212b3e2af6e248ebbda90b43d55ea9a9448c3f578b6c9545027a1c54c111
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=a5f8461fa6b11fa9a53f8c41b450aed7cec8bcd0e690bc2316ec868cbf8b565a
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=e8d5501614d880c490cb6c0ad6d831c248de2668e07b7c98ee79c2f2f719fe19
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=a132692b8ac678ff6d40cb22767da80ef83b7f6c4f81242d8f033721d33ecc83
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=e0f10115b225bdffbdcbc550bc2baeeb1ea9e174926430ef848c5b767cefdc78
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=ccd2421d48ddcfc29633fe2059e0bb62a8dc7550de4d70892c50b898bab4dcc4
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=606b82c1bdaa84ec80be074b0551f12b79f36cf13be90e481da947397096632b
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=2cb07b68527032329ded3ab3ccbe66930cd6b7bd523787e90305a5476594a41f
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=afc71f4e0a45e5103e54ecc18a8c43e3d2b016c9a1d3113b3e483573e556171b
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=315a2321655f2d3dd8a54f5538e52b3d21d15df0d09e66c2b1f6afb83f427eb8
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
