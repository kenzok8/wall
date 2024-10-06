# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=129.0.6668.81-1
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
  PKG_HASH:=feaefc5e55d50c4ca9b76ea322dd55c68759708f10f026ea446d30ba370c39fd
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=aa7f5b0297d1f66210752457eee5bdb564872fe532b5c62309309f8d77abe3b8
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=4bbed0271b7d3ff127af473dc31081b33c976b891e3fd725363f18a1ef360c18
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=e2fc9ab7871f41dc55b60ddafff28cc3845c9af5293f8d6c4a419b91ce03d29a
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=6b4d03bd232a13a0720dfba077bd1847617a1fb699bcf20ffee182c49643ccfb
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=63e71fd1f729e03f1edadda8435bf772b0bbad1a48e4e25b61d0df985e6202f7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=bdae0724f844da0224a94318193238f59e9766c86b05d6dd7bbdcd3b14773fa5
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=c6ca6644df5d57b241a212bea3d11427bb369a67d58d3352e7aa488ef56f34e2
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=ded055c58d29849532975d203e03f0347c41b88047cd0651638a0555acbaa1a3
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=4d24288c0003585ce57320dc1173c9dfe259675fbb0f6af83e94e4c5c104a759
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=a46a24ba320e1ad4e759d0f294801996acf919644cd4706bf2729c73e905cb78
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=9817e1cb42838829291bc1b72080d3c2219e3e1a6616cfcff39fc762eeb68d84
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=0ba19c0da0ebec667571af0750bd5c184d61702c3041291d517749e462a626e5
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=068bfebe298f92169aed86b5d2dbf13f595acbd04349f12823df5bfccb910f7e
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=2c2be2c624b0ba6462f71e14e592ec3abc77b4387a3c5786587372ff735d4fef
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=be397c5af50b9eb3f81408d9d5f2dbd75a71d6c2c0103054f1328b1c3ab8daba
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=2ac11b97037a5b5628bf8b858ee59db53f79ab15fc589533a0b1a61f68876fcf
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=f5f2eb49637d7541d21970cfb9d68c8399f0e93dfcd09c1b3b8db1a3ba2c4a64
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=cb2f0c970563915e53b8a90f3f19bd839d99a96186cab25f3428370c8813b779
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=fbdc2ba15f59f6be23eacc3e7de94eae04d47c353dd547c1cf9419ed928a4501
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=858d18d759de3db84e3431e39197a0cdd319681bbfb2861d9c866eb1bc28adad
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
