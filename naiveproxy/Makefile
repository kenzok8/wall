# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=132.0.6834.79-2
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
  PKG_HASH:=4264588ab16565425a62436d5946a0630759acc3a71e2a673e2d5383caed8320
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=f4272d75cdcf4e5f9328886e50e49115ea40b75c373dcd7bbce1045a791beed8
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=b50ef4064c8e609730233fc358b4e992f174323eb11153f63ecbb152cbe4b92e
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=7ce0ba453c09f9978e421575aca96b34d381ec1731f19d29d8e16e7968fb1888
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=bd050616edb6d6538001db64dc7dcfc13941855890ec5741beff1144a897530c
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=94f22ed0e270d47b035ec6380ce6b26db93ff01382641c222f2db11929cc0856
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=2d12bb48e50fb88c3ab1375fc9f0df56d45aeaa3fc6c82b78555c1c4b7855266
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=e27d13fc44deecd5083d0e5cdf9f0df83a642df714f4a13a69b706bb5198a61e
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=e144fafb14c8bad7e7d96d01f3d3d799fddfcd1f620e8f045376a19c497c0f54
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=5f65427412398053e9cecc3139c91fb8b09147ddfd42b91df742b9909b141bc8
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=f9bdb669b6440d088336d17daaea24c6ecef85de4b8bac756a2d1fbd487fa1b1
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=8a4fbba18e8157dafddb7e684cf3c06bef2f10d3f9796bf0ea2496f9c788389c
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=b1371c204a9f4fa7cf98be0df0fbb257fd6708e7a096a57d9d31740b3ee74360
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=fb3dde55b6642a0527b0ea9110fcad8081255248a4bc59bf530768eaaee1e5b8
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=008d2231c867614dc3e40c966261d9dc5c9931b3c68beb33549ad3d4f7bed2f1
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=d8160e3b0963d124eb91762c6df9d96207510dc1a5f28f32f3ad6f6133f49d75
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=f9c0a4049388058aaa881aa13385470497beaeeca6473baf6539905a75d098bf
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=fd2520202c1cbe82498c90594a71cd1ed6aa4d8a6d470cf84871fd1d8f646380
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=557f8054e7643d6cdbbd1f70922ddf131f60ad03fb2cadf994ac15c9303d84ed
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=eab01156720906345230f6fb9cde7580b88e66799a4bdcef58636addbcab9a6c
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=95fd43646b86512ea46d87ccd0b5adda50aefe5c53dbcfd4b47930a146bec8b9
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
