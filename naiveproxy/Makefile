# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=123.0.6312.40-1
PKG_RELEASE:=1

# intel 80386 & riscv64
ifeq ($(ARCH_PACKAGES),i386_pentium-mmx)
  ARCH_PACKAGES:=x86
else ifeq ($(ARCH_PACKAGES),i386_pentium4)
  ARCH_PACKAGES:=x86
else ifeq ($(ARCH_PACKAGES),riscv64_riscv64)
  ARCH_PACKAGES:=riscv64
endif

ifeq ($(ARCH_PACKAGES),aarch64_cortex-a53)
  PKG_HASH:=3f7ba5f4660f801e675aac8124bd7da714ff9b5a11c72955086ed4914fdd0600
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=4027ff6b5d14ea0b4921f1048c2fa639c368b360bd34dd35bc5827c7377ba7ac
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=eb500d7baf5b05e1a4dbdd3554168a21ae60bb72efcb58f14357ca2f089e04c4
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=5403ef027fe947747397c961c08c73f8cf362023a94fb471b3e27e6150b0cd70
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=c115af1a2543028e4ce639aefb89ab74d98de30c9cdd34f50831c1636e19a406
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=67a17ce9b4c03915a552004b93b8245b2572b1f783d760c53fb683b46f112ce7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=86bd10f78e3ba1965021d1d2e09f7cd0857757e41409eca7059f9c455e23e4c2
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=fc1ce37ae04f8891fe987ecef2d3d0e3a738cc2c4063392593446f511c0d98e5
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=22434167977afcaf058c2723c6040d160680a73dcab150f2503be19a6dff584d
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=5a1dd8a0b8dc3f7e321de879268ebcb01f2da29d631d58db2383af0fd620fe48
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=a4d69095ff5e2d9c648c80d8ab71e9f238ff99dfde2ca9e29a70c0368342be1c
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=e06be005325bf520fc7eaa4a09c0bdcc4d3adc279d91557861e7712fa721d548
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=2bd65dbe753941086dd460e94052841664a16e85aaffe318542023f5fd054460
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=0f4278d97f748087844059361c926b073d1aa2173b0c643daa83f459e5eb85a2
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=45d085c0d8a71394484a002cf27a578750d48a2079c6f7370d161ef29feb54bf
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=80320bd47ee05d77b327b570e469cec601d18d1d0a1223f04528497296267049
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=335c8c8574adc591a6d6456b7e8e46557dee40dce05fef62bcd2a806bc59bfd5
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=f07a072843ce5c31aec640a3271a765bd26612c0bdefc167c54a639b657619ad
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=1dc9570f0f95976f3ea0a4d99c0a0340f98f7cb9488eefd86b87bb346f6d6d39
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=ddeba2d8b635d4c0f6583b986ed04700262f1c24817ce76a0aca9a9bacb0ade7
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=9438d78159f236bccc1f3491222e58af08c6864600ef5a989542f143eb3c0972
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
