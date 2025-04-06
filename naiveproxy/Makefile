# SPDX-License-Identifier: GPL-3.0-only
#
# Copyright (C) 2021 ImmortalWrt.org

include $(TOPDIR)/rules.mk

PKG_NAME:=naiveproxy
PKG_VERSION:=135.0.7049.38-2
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
  PKG_HASH:=7711d714d9cec37eac9048a59fc0d1fa7c7bc0a637018c9b2e419c43368e3c53
else ifeq ($(ARCH_PACKAGES),aarch64_cortex-a72)
  PKG_HASH:=44253ecd8cb7c62ffd948901a1191ca2c1b65430ec19253322c5935551e13b7c
else ifeq ($(ARCH_PACKAGES),aarch64_generic)
  PKG_HASH:=77ffe91387a29aaac22433b71c06bac3dcd28aad31ef3697e443a89bc8714c16
else ifeq ($(ARCH_PACKAGES),arm_arm1176jzf-s_vfp)
  PKG_HASH:=15e33c0368cf8adca8dade760e1d65307f93ea3a7f9e83aa6fe8ab6410578c0e
else ifeq ($(ARCH_PACKAGES),arm_arm926ej-s)
  PKG_HASH:=c7cca2201b9a582fb674984cf9521c237fa9ff8f5e8fbe6323d4be34b684c85e
else ifeq ($(ARCH_PACKAGES),arm_cortex-a15_neon-vfpv4)
  PKG_HASH:=474e3227c6bb0271e4d9e9a11f02bbf3a96171abbfad710b764a4cbf01276c39
else ifeq ($(ARCH_PACKAGES),arm_cortex-a5_vfpv4)
  PKG_HASH:=d8267795f9221e3c9ef1194f67b5c132e61236135ba9f5130666782e6cb3b00e
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7)
  PKG_HASH:=519d116bea3d19ef3f9da782d2066c09cb4b9fcc1494f9bc2450f65e5d5895b7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_neon-vfpv4)
  PKG_HASH:=e2d8748b13867f9c0f9007b4570bdf2466d4717ed5fe112cdd5c5745dd9cda88
else ifeq ($(ARCH_PACKAGES),arm_cortex-a7_vfpv4)
  PKG_HASH:=8675b1b6faef33386a074dcb37321ad85b465e596afcd3a9a8e56933b9490d82
else ifeq ($(ARCH_PACKAGES),arm_cortex-a8_vfpv3)
  PKG_HASH:=415aa150b519949cd89b0c8c22ba10681de2bfcd78894830e270c83412f247a7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9)
  PKG_HASH:=62c9b107c4cef346de3d7f81fc39e37356b7635b7c86c2e5628a7c79d852f6e7
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_neon)
  PKG_HASH:=8e7b251f880f7249138c93b623c82037ea03a4e91cfad0a127d2f0860363ade6
else ifeq ($(ARCH_PACKAGES),arm_cortex-a9_vfpv3-d16)
  PKG_HASH:=83a8f4333c8a0ce14348d461a6f1b2e55078a2afb5cfa937b5141dd58f700c1c
else ifeq ($(ARCH_PACKAGES),arm_mpcore)
  PKG_HASH:=7cb546a80eb7466e14ebd10f7172c25088a7242bd6b0c428e860f9d228f3a0ce
else ifeq ($(ARCH_PACKAGES),arm_xscale)
  PKG_HASH:=d27f2d18fd5ce59c78af7f879d300e0700de05672cfb6265d252a4a7197a4df1
else ifeq ($(ARCH_PACKAGES),mipsel_24kc)
  PKG_HASH:=054b2e9989ae30fbfc2ca4f69e1df686433a604d0c55827e6eb478b902d02cd1
else ifeq ($(ARCH_PACKAGES),mipsel_mips32)
  PKG_HASH:=c6e7015b2e900e94244e66118b2b3c7c9f5ff5e0257311625497e7dc133a1071
else ifeq ($(ARCH_PACKAGES),riscv64)
  PKG_HASH:=973930d0abda895d1414a611f9bea70a1a35c1b9965fc9062f2bb0900cbcd617
else ifeq ($(ARCH_PACKAGES),x86)
  PKG_HASH:=574dfa733c671d7d3125f53cf01f3f52d758a49cafc8df0e216e5ad5b501a149
else ifeq ($(ARCH_PACKAGES),x86_64)
  PKG_HASH:=8fabab9496f947f90d2a4b72379069d53c132cdb14a092898c628ed0e7879d4a
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
