%define _topdir    /home/username/builds
%define _sourcedir %{_topdir}/SOURCES
%define _builddir  %{_topdir}/BUILD

%define logmsg logger -t %{name}/rpm

Name:          obs_autobuild_test
Version:       1.0
Release:       0.1%{?dist}
Summary:       A test to see how autobuilding works with open build services
Group:         Group/goes/here
License:       Apache2.0
URL:           https://github.com/seccubus/obs_autobuild_test
Vendor:        Frank Breedijk
Distribution:  Group for specific distribution

Source:        %{name}-%{version}.tgz
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
#Requires:      /bin/bash, /bin/date
BuildArch:     noarch

%description
A test to see how autobuilding works with open build services

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 file-in-source %{buildroot}/path/to/target/server/file-in-source

%pre
# Pre-install steps go here.

%post
# Post-install steps go here.

%preun
# Steps prior to uninstall go here.

%postun
# Steps after uninstall go here.

%clean
%{__rm} -rf %{buildroot}

%files
%doc README.md
%defattr(-,root,root,0755)
#/list/files/here

%changelog

* Wed Feb 24 2016 Frank Breedijk 
- Initial version. Date format is `date +"%a %b %d %Y`. Comments go here.