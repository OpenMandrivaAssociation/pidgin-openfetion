Summary: libpurple plugin powered by libofetion
Name: pidgin-openfetion
Version: 0.1
Release: %mkrel 2
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0: pidgin-openfetion-0.1-pidgin-prefix.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: pidgin-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: cmake

%description
libpurple plugin powered by libofetion.


%prep
%setup -qn %name-%version
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
