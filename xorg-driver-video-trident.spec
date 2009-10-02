Summary:	X.org video driver for Trident video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych Trident
Name:		xorg-driver-video-trident
Version:	1.3.3
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-trident-%{version}.tar.bz2
# Source0-md5:	47f3c5da1942017218355f178f02ef84
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-trident < 1:7.0.0
Obsoletes:	XFree86-Trident
Obsoletes:	XFree86-driver-trident < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Trident video adapters. It supports PCI, AGP
and ISA video cards based on the following chips: Blade (Blade3D,
CyberBlade series i1, i7 (DSTN), i1, i1 (DSTN), Ai1, Ai1 (DSTN),
CyberBlade/e4, CyberBladeXP, CyberBladeAi1/XP, BladeXP), Image
(3DImage975, 3DImage985, Cyber9520, Cyber9525, Cyber9397,
Cyber9397DVD), ProVidia (9682, 9685, Cyber9382, Cyber9385, Cyber9388),
TGUI (9440AGi, 9660, 9680), ISA/VLBus (8900C, 8900D, 9000, 9200CXr,
Cyber9320, 9400CXi, 9440AGi).

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych Trident. Obsługuje karty
PCI, AGP i ISA oparte na następujących układach: Blade (Blade3D,
CyberBlade z serii i1, i7 (DSTN), i1, i1 (DSTN), Ai1, Ai1 (DSTN),
CyberBlade/e4, CyberBladeXP, CyberBladeAi1/XP, BladeXP), Image
(3DImage975, 3DImage985, Cyber9520, Cyber9525, Cyber9397,
Cyber9397DVD), ProVidia (9682, 9685, Cyber9382, Cyber9385, Cyber9388),
TGUI (9440AGi, 9660, 9680), ISA/VLBus (8900C, 8900D, 9000, 9200CXr,
Cyber9320, 9400CXi, 9440AGi).

%prep
%setup -q -n xf86-video-trident-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/trident_drv.so
%{_mandir}/man4/trident.4*
