# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=124.0.6367.54-2
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
  PKG_HASH:=222c98c471ca1212cd12f41e191e815d6b2df6175025bfa119142f9d7a8c8758
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=38ba89a7fbd954bf47634f96c2942c398cb56d595a4621d1f441fe031914685e
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=2419743b3fc54e87d16483d2d0627273a309d576b8db1b9b5133665ddc47e4ff
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=a9ae3d38d1c2d05c3413860fe0faebee2310410d42c015bb12c55eab119a0a23
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=a76b19b4c977ce6595eaeb4c373fac680e9f3d66a084031752ab26808a369131
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=5166ec17e83a8d9d009c1ba07ac0d9b8669a34deb7c8fc7822d40610be0300f6
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=f7e3540a3e5beeef4eb9e9ce8ad26f538e648f2dda657babb24ae05b1cce9dee
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=7c34045a89465650a3127e99e6ccaaea126ea1c3c4680600cc9808c5a0dae56b
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=639301cd6a5cbe98561d04323011d8fa41a9cfe5f8611ac0394b9856d8756865
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=bd724596f967397da26c93b1f1c3c489cb6bccb536f10c3c62c38697508f5f3c
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=77d84fa6595f64d627849bd10285cebddc5785902242c9f76880f134c454b7ff
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=1b943d5643e6c382cae896277f674a681443d4dc35a593955374f965794b02f3
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=68c41de6be5be53c148880c07cc6c8a217ddf18ec77a7e0dc0af33f3e29ce3ff
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=ba7f3e7267ed73b23c6829b4c9368d181d81e336edcf4a61a1dae3dc6d79bc9b
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=abdb74c84b77a47d7d592faa95ae8c2cbfa828f551e58295d0b41dbf549779d3
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=828173fae3668936cd3c021e588c480ac78d5820e2ac516d3b968b526ea94615
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=bff1b5f1e55a79e440964c1c2c0f0251fa52265025183f0428f5ddd4af6eefef
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=2484dadf239727cd46101b56a0f920941e50ca06bee4dd557e88499f22de461e
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=120beca52a8738c2da5e38f9586e607f59c590602e51380c75d142630a7f6a40
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=1ea3bbe494ff50e51a8d8829686df1dbf8c97c5a52abff5247c9159ce6c75b4a
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=035ad181785673ad2f4e720922125b08a244a253dfc343272f5fbe5b9a3dd8e0
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
