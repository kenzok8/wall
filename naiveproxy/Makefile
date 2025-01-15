# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=132.0.6834.79-1
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
  PKG_HASH:=5cdb9ca045995bfb41d76b5321090255fb8ea7ec22aedd8a72f4aa1cbca1c456
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=c4151ced17629b9267b07cc13bb5ca3cc0931a4205630a407e88611bb605aa85
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=c2587d13ef960d4efd0e2b5debb1b7a952b368838f7baac047183925fd7c896c
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=dc31a9ba7e6c7b6c12fc7e46d75a99768d8cb5158c35aa32bd00a89a78799185
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=979b513f5f246f856379016abf43c630ae1085f05cdb9d20ef29635c554a35f0
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=af2510de66dac0cde22b090864cfae314405969665a4abfc95bed51a77500e82
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=2b9306942a692f606e4d169a5acff4e8b7e6c7fc4df445d0372eecfdbba4b0c7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=308e22352b0bf042341cd96b0c3b54a6fdc7aa6d62b98fa1d298b081b62cf699
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=d925050e6ab276d3cff72c5e3ff4d348a9f49056a9cc60d9608ef272880cffc1
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
  PKG_HASH:=29293985c3d4af1bb0699a9907852555db6a3d8f1a01cc2a58651f9d20776e6f
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=26909683e0586696f2b3c914be6fd1132c93c8eb4dec99bea93d70accddb66d6
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=7ea7084fbcf22259a1ee7d785f886986f0f16e6dda86838991af50fb2b24cb72
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=cea3005186f9010cb5270bc5fd99d68c5d7f77c8267129ab4f114c37699c2aa3
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=515d14ae15009abaad4016ba36848a71ba52bca9b4aa8f207eec2343d31ed608
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=f53aba8d13f8ba11af0ba26e27c8fc616b7a28a0e1d81814e0128c10cc92d3be
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=2369644fb5ccb41cf511ddca67d30cc7f04e64068f4d1d28c42155b86dfd4a06
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
