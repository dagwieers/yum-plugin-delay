prefix=/usr
libdir=$(prefix)/lib
sysconfdir=/etc
plugindir=$(libdir)/yum-plugins
pluginconfdir=$(sysconfdir)/yum/pluginconf.d
DESTDIR=

all:
	@echo "Nothing to do."

install:
	-[[ ! -f $(DESTDIR)$(pluginconfdir)/delay.conf ]] && install -Dp -m0644 delay.conf $(DESTDIR)$(pluginconfdir)/delay.conf
	install -Dp -m0644 delay.py $(DESTDIR)$(plugindir)/delay.py
