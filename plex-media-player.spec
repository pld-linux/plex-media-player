# TODO
# - handle build process downloads:
#-- Downloading https://artifacts.plex.tv/web-client-pmp/183-045db5be50e175/buildid.cmake to buildid-183-045db5be50e175.cmake...
#-- Downloading https://artifacts.plex.tv/web-client-pmp/183-045db5be50e175/web-client-desktop-4.29.2-e50e175.tar.xz.sha1 to web-client-desktop-4.29.2-e50e175.tar.xz.sha1...
#-- Downloading https://artifacts.plex.tv/web-client-pmp/183-045db5be50e175/web-client-tv-4.29.6-045db5b.tar.xz.sha1 to web-client-tv-4.29.6-045db5b.tar.xz.sha1...
#-- Downloading https://nightlies.plex.tv/directdl/plex-dependencies/plexmediaplayer-qt/206/hash.txt to plexmediaplayer-qt-206-hash.txt...
#-- Downloading web-client-desktop-4.29.2-e50e175.tar.xz...
#-- Downloading web-client-tv-4.29.6-045db5b.tar.xz...

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
