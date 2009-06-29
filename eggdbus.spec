Summary:	Experimental D-Bus bindings for GObject
Summary(pl.UTF-8):	Eksperymentalne wiązania D-Busa do GObject
Name:		eggdbus
Version:	0.5
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	44f1f6387c49e8198d7aa755aeee46c6
URL:		http://cgit.freedesktop.org/~david/eggdbus
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Experimental D-Bus bindings for GObject.

%description -l pl.UTF-8
Eksperymentalne wiązania D-Busa do GObject.

%package devel
Summary:	Development files for EggDBus
Summary(pl.UTF-8):	Pliki programistyczne dla EggDBus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.20.0

%description devel
Development files for EggDBus.

%description devel -l pl.UTF-8
Pliki programistyczne dla EggDBus.

%package static
Summary:	Static EggDBus library
Summary(pl.UTF-8):	Statyczna biblioteka EggDBus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EggDBus library.

%description static -l pl.UTF-8
Statyczna biblioteka EggDBus.

%package apidocs
Summary:	EggDBus API documentation
Summary(pl.UTF-8):	Dokumentacja API EggDBus
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
EggDBus API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API EggDBus.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libeggdbus-1.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libeggdbus-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libeggdbus-1.so
%{_libdir}/libeggdbus-1.la
%{_pkgconfigdir}/eggdbus-1.pc
%{_includedir}/eggdbus-1
%{_mandir}/man1/*.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libeggdbus-1.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/eggdbus
