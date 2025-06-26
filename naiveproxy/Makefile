# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=138.0.7204.35-1
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
  PKG_HASH:=ce0fbd501e11f515e0dac203157346201727ffec62ebc9f25c37db959e3b5b00
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=7e3778ded1fe210c180127c7fac4913e1b0fa624f27d4f9a581ca56315cac72d
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=29d3585aa2cb790d15803a25d3fd4a831296bdb4ae3eaa2f0ac52b5bc09abba4
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=c5838f4149efbc7b2e01d6f2c94f7585edc3b51ebc072e88f4e8d6e709125b02
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=a514d92010d2999ddbfe073e61dc9ea7f58414845077114979950ff5078a72ee
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=1e2677d68d9c81b7505ada6ed146177e53dca708fa878c5105b87812df20c797
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=e9047f458ecba7cfc4c722d0180c1a4d823d9edbde41e4abce0f293c52712b0f
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=954cea8e06240e6391d7057765335c6ac20fdbc42dcde9d20c2e4aa55a75a9e1
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=6d739e11f4df930139744d982ee9e98050cf6778ff0af90bf5e128f789f26b61
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=8f3de0015d28c341d8dd303bd770ffaf4cf05767a4af3612218da78a54d01c6e
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=bf15aaaf307ac86cbd3fc9c9a8a107103d2682ba227f54fd2d2a2def252b8fca
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=c5788e9ce8eef9d526390ef04966668ffd9e9f40af194257fb9600362585032f
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=5c93593112ad72c75d35fc41b6d6ed3c1115dcf8aa30f9bc61303696f31fa551
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=d23f160bf4e1a22e7997d589bedbde8368e4b842ee6f4e0c1dba3c6825d42ef6
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=b82aaaada7cf3261a58a8f30bdd2710dcc021435cf310a1cec25f6fed6788428
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=277405ce386c56172e8e0ca2d98beec5bf5034f77a1224de201119abc5cd92b5
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=4e31ac05f877cc36cf9296377bb4edbfc0b91657c39e5c9dfe36ea63500cf5a0
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=deceede3b36871a785ece5f1465517b7cfa42d014f5c21eb23a4ea9b6821d4a8
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=0181e0b33b961a50d3d17a25513d28d8e0286fb1db417da5875cbec9341dd073
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=0c633a5dfe7d929cac0b3f389522c47ac46db9a9491724c7e1e7ef7380b2299e
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
