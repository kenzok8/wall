# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=130.0.6723.40-5
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
  PKG_HASH:=caf705c6ef3ee9a3d0bf5500b7090f31b0a6bc277ac0cd9026374dd6214a8fea
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=742b746adf949f5b2b283cb1590d1f5cad965c136165428bccfd3ab4fa502f6c
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=9fd80e26f236ad290ef994b9d75a900861f23e8ad956dca0d2152df97f25cd75
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=02cf41769a7be2544460f1ac7ccd19b330efd3bc12fb39b97bdcb03f7c13f267
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=cbc2f655736bc7fd53132bc7219894567b24369c9ed31a040152962cd7e53850
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=a77396d9a8372a6f5dcb07d625e099841fca28a3a0ae295959813d548fc953e9
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=e528f983a13fd54b8ee8894f5ea325e185959b080648859deeeb358a289dafad
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=1c7aa990f95d403c53a8f40db2d1e4810edc4c1a89b9ddbb641417c3cae01578
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=cf81122cf6c8784facc611edf811b17eb2a4c44ac289868dcac3536e55d4f979
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=07b8de01bf42fa58f3a1a8e1c103914d7ab75361b3369b0d13abab88b47ac5d4
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=66e78250179d918322d77219b1e8ca96ab6ab5ac7c043e6486e2da9765444cf8
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=d8c7f6b658e2539c1cba83d275947ade2eace8ecb71dcf9dd04f26b6700ac28a
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=7704e250a56d313c12059fca5a036cee120860a2b3c290c616ea2e340a14d466
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=4462b1b2d95c516fdc4bd24535db32e4655a551b8b86a3036956d72d42ff7a4a
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=c106d135b23139c6a7b1b43008d30ced6687b4eb0746185c04baa0d1baa2d5f3
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=349e2c60e5c3344c317b699fa06dbcb377776bf4949c34d6e7b19808f5478b57
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=4a790122e8adb1957e756d84a34b39575818038b1e7d836fdc2678b1e288d45e
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=9c45bd94d0efb70c112453b911a6e24fe6fc998d8048e916726adbb9396d54d2
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=bab3c9252c3fd4ce4ce14ae32fe317ff3cbe4d00deaad00353517b9c25158d7f
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=c513fe77d6eabfb3346ab068db98e70f271590f54fbb0a798e2275a41a0e1bde
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=9e31fa0e55ebaea58b715469ac2ca069ac6d20ed553a6b66af80027d98ca63c9
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
