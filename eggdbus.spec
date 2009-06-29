Summary:	Experimental D-Bus bindings for GObject
Name:		eggdbus
Version:	0.4
Release:	1
License:	LGPLv2
Group:		Development/Libraries
Source0:	http://people.freedesktop.org/~david/%{name}-%{version}.tar.gz
# Source0-md5:	db135ef3072e102c319838e34f7eaa27
URL:		http://cgit.freedesktop.org/~david/eggdbus
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Experimental D-Bus bindings for GObject.

%package devel
Summary:	Development files for EggDBus
Group:		Development/Libraries
Requires:	%name = %{version}-%{release}
Requires:	glib2-devel
Requires:	gtk-doc
Requires:	pkgconfig

%description devel
Development files for EggDBus.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--disable-static

%{__make}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/tests

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_libdir}/libeggdbus-1.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libeggdbus-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libeggdbus-1.so
%{_pkgconfigdir}/eggdbus-1.pc
%{_includedir}/eggdbus-1
%{_datadir}/gtk-doc/html/eggdbus
%{_mandir}/man1/*.1*
