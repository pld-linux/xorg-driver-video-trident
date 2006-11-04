Summary:	X.org video driver for Trident video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Trident
Name:		xorg-driver-video-trident
Version:	1.2.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-trident-%{version}.tar.bz2
# Source0-md5:	c0e8b2f54942b6902b7dd4f30defe800
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
Requires:	xorg-xserver-server >= 1.0.99.901
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

%description -l pl
Sterownik obrazu X.org dla kart graficznych Trident. Obs³uguje karty
PCI, AGP i ISA oparte na nastêpuj±cych uk³adach: Blade (Blade3D,
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
