%define		subver ae73e074
Summary:	Plex Desktop/Embedded Client
Name:		plex-media-player
Version:	2.58.1
Release:	0.1
License:	GPL-2.0
Group:		Applications/Multimedia
Source0:	https://github.com/plexinc/plex-media-player/archive/refs/tags/v%{version}-%{subver}.tar.gz
# Source0-md5:	-
URL:		https://github.com/plexinc/plex-media-player
BuildRequires:	cmake >= 3.1
BuildRequires:	ffmpeg-devel >= 3
BuildRequires:	mpv-client-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= 5.9.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plex Media Player.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
install -d build
cd build
%cmake -GNinja ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
