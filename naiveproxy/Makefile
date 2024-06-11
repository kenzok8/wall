# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=126.0.6478.40-1
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
  PKG_HASH:=829e033c930645730e39529a7be54bde571d43d3ca01ad5f8a6c58749db34308
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=f32ce43b362aa6ceb2f24a5a8ec5c6190722b06b5a2c97ca6fddc6cfa76202cd
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=702dc4bb621d7a8189482f49d12d8d4943dbdfffe2c7c197bbe32f8f9c0f4ee0
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=d14931ec0a312f8fd996c14ae1ec012a5f9e03d92139509f5edd3f19feba40d4
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=bd8f45efa94ab89a8af08b48523a9a4a21cf954261123d5c73ea57246c29d611
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=790e264c4798031781eea07360906e86494a95f4bf7466e5d34735adc5b3842a
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=0a9d2f15e85b6a93580173b8a5a2527d40926fce70272570e2101f82c5bb96df
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=dc40da97ca7d7a24aa45e8520611c6f0dcb324b4326bc03051db12d50dcb4c35
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=282ca2cd3dc567a99da67bca9927180ef7147cc89249f43f0359c030fbcdcc55
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=c0987d38af34aae4687868625591a71d59b36906f2e453e7db458addebc594f1
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=ce7a23164af8720d71fff998ead2f0279792ede5fdb9b0cc54af05d77215af43
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=016895a8fa4a6ec36efa4a4890566bf33ea888526a8902da1b915573006d8dab
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=9875ca3884cbcf1704ea44900fc5c89f62502ed76a7c79137d1ff3c32e912988
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=0687360a7488b534818df5db071ff0feae8a0a8e6c0464fe0f64533d63682841
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=13cdb19c23add28f8cc02b9d0234db5836e851ef3ff4968363da27f6045b94ae
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=a9d4e1825a391ef9294b58d765cc6425322848a70b29f64955c5933121990288
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=7b358d7306f77f87bcee33beb6be1d8c1d70c2128172475616bb1531bb3aa908
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=1bc0af17f48b83e2439534f91d462b286d8c35888bfee87785f70337088a5d32
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=8cae7646c9cc4e99b33b2f4de65795ebeb6eb7744e9babc39e6357180eb3bfb0
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=c403e1bd29d19dcf811e034bf6cc6940c6ef9425b80d87a1643000e7361016aa
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=d88b2cc80fb3b79f13f0f1d426d2b2dda9127b0b24f477c008b4c8cfa86d99ce
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
