# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=134.0.6998.39-1
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
  PKG_HASH:=070ea4fec533a8ce32f55b6daf8c0431a9b532aba0a0a065583005c6baea77bc
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=c98c1867f58d24757d2fab09ee28bf921d9805f0d836bb11d25c4acf8306abec
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=110c0174bc9aeca41c03d207b1aa714c71528c03a8e148699b094473f8ef53f4
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=2442a34a532e7bfbc0926fd1fbabc94a19779a4ea6edcc50bfe8c2281d524b8d
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=04f237181162ff3e8d83f9f864efead8dcec60a5d75c69b7b112aa0d3107c7a7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=ec5bd89729eef1995b58f11f9e52f6495144001fdd3990116da598a9102d5454
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=30d429df58bd50d6a527500e1e279e5ae31440383afec5756b0373c68b971dcb
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=2a5456cc82a92a69407ddc61b1cfc7d44290e6167d96d4c4fd2dfae53df7f4c5
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=bf85b73a85a198f73b5d0bd5f538a04be9d126d54b35d56ef1fbf366a758b168
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=26481b7801cf55b46b0e0363de4f4520bf4e839586652ed820a3a21413cc3351
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=535c30dedf4a95b9d3e79e4b6c36e8ee256c6f439ebbdaa673163b32eef63f0e
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=afa8050347a759b1030939339a7e3e46bab4a8ba42d00b5db3dc7d9bddf5b996
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=52bd52c123e3b0c23eda946056bcdca805977ac81d97dba3bd8f07ecb04e2add
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=707ff36bf95a4e71ff98dcc43182890cc1ac15b6d427c28e443134ca00295374
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=a3cb60d42ae13253983728767cd41b7ded11bb699ea4239fafeb03e93477c0fc
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=4f7f88885c4318259cfba73ff846eea1c5a94632f5c9d969d664eb1d7795380a
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=64f6f77e87cb8c06d880b3d4ecafc9baab117452e70dddcdb8c69aae41b6a6ca
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=9be977a06b701dfadae4f6c5e56fde7adbda0f7cc8b11921fae01b5ef2315cc7
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=91969c969010f7bb1bde3871b7004a37257a8bc7dcf1d3d2a393b38213e236ff
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=50729ddb13d31caacc1cd2f6e96d7813478c7e693ae006e3a78e71fea82a2f23
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=49e051113d6bf1a9376f26e40ade0672e38b75bc978cabc7622e3a2d0c424d3a
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
