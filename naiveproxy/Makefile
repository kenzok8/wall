# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=148.0.7778.96-1
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
  PKG_HASH:=61badb74574ce1a1cdce6351d6d43878689a7bc864f53bdeabfc1eba72dec930
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=4f1ec2434a19b883daa6bab2313498cb63f9dfa97f546b6910470bc3070a33c1
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=cbb8e4480231391db22c545f99ce921315defd86eaa0f8f9a4d8a89482f71224
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=66736fcff43dcb70bd0249473ffe5c7a9b842da8a02c5ee9918924983a2c203a
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=ef2e91938c0c1e37ba3d1ecb37adf76a9ad3ea7a39d037312d80f3b6df224aa7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=728800a85bcfcae786dbdbdbf55be40dfa5ce250ab47733358ac798a8d107ebb
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=1ebb1e877cd46818eaed8c88c87214694c1b7819525d8520079bb09a1d04ab34
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=ca9db61451c53fac7ebf41518e08a4f9b91ced6059a61d2618a2c9ad8e646e54
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=e8b7b57f59a2daa3a2990c6314f8431dbf8a2b0278cf77123200775ec15eedbe
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=3cb33126f0a66ab880f8842d038b6ce3e8d9b3ced5416210a18da90eccee9037
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=df017da67c38f4181f43e69aeae65f2aa780ebe50bf8097fc4d05bb879cbe9ff
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=596ccf7d1ed9cec0e6b42034af8d82e1623d2c7556948cb266a077dfe21b7aa4
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=916111591d5ad5868fd211b5a062f2c4af6bb7a0c1642a7e343ef076cb1e6e81
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=ef92983a8c59619392ea0161eae464b914ec97ad9ddcb7ad5c5e8b5beb78825a
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=4505de327c005844dec3c36d63ab5bb8aa14bc2b39c19270a87a540d47a12597
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=89f191971a784701932eda71453a14ffbdb6e22e80283e2ce5810c854fac520a
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=4e65f8336da060cb5894a0c7aebffd742b2d088c7025c4541146b7c1f6c9a8f0
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=952327ed425f2baf9849f2bf4866c487ef59613d663d6710c2b6da91c3fa2e59
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=4ad6558bf7a7b542dd1ad6a3a1304c07985f8e7d3cf6a56a6cb77d21ffdf72fd
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=decda101a78f683cd7ebbaee6dfc27ac9727207f7b710ac1f9fb37d6794a0548
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=8cb3217cf15a537798c4d163755205ff458c31310ab909edd5899cdaf961856b
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
