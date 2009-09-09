%define gamename vdrift
%define name %{gamename}-data
%define version 0.2
%define fulldate 2008-03-11
%define date %(echo %{fulldate} | sed -e 's/-//g')
%define release %mkrel 2.%{date}.2

Summary: Data files for the VDrift driving simulation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{gamename}-%{fulldate}-src.tar.bz2
License: GPL
Group: Games/Arcade
Url: http://vdrift.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: %{gamename}

%description
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind.
This package contains data files for VDrift.

%prep
%setup -q -n %{gamename}-%{fulldate}-src
find -type f -name SConscript -exec rm {} \;

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}/%{gamename}
cp -a data %{buildroot}%{_gamesdatadir}/%{gamename}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{gamename}/data/*
