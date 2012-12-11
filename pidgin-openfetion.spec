Summary: libpurple plugin powered by libofetion
Name: pidgin-openfetion
Version: 0.2
Release: 1
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/pidgin-ofetion-%{version}.tar.gz
Patch0: pidgin-openfetion-0.1-pidgin-prefix.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: pidgin-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: cmake

%description
libpurple plugin powered by libofetion.


%prep
%setup -qn pidgin-ofetion-%version
%patch0 -p0 -b .prefix

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang pidgin-ofetion

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pidgin-ofetion.lang
%defattr(-,root,root)
%{_libdir}/purple-2/libopenfetion.so
%{_datadir}/pixmaps/pidgin/protocols/16/openfetion.png
%{_datadir}/purple/openfetion


%changelog
* Wed Jun 08 2011 Funda Wang <fwang@mandriva.org> 0.2-1
+ Revision: 683142
- new version 0.2

* Sun Mar 13 2011 Funda Wang <fwang@mandriva.org> 0.1-2
+ Revision: 644364
- fix typo of xml libs
- import pidgin-openfetion

