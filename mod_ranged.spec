Name:           mod_ranged
Version:        1.0.0
Release:        1%{?dist}
Group:          System/Base
License:        BSD
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Url:            https://github.com/ytoolshed/mod_ranged
Source:         %{name}-%{version}.tar.gz

Obsoletes: mod_ranged <= %{version}-%{release}
Provides: mod_ranged = %{version}-%{release}

Requires: httpd libcrange perl
BuildRequires: libcrange httpd-devel perl

Summary: Apache module interface to libcrange

%description
Apache module interface to libcrange

%prep
%setup -q

%build
apxs -c mod_ranged.c -lcrange $(perl -MExtUtils::Embed -e ldopts)

%install
install -Dp mod_ranged.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_ranged.conf
install -Dp .libs/mod_ranged.so %{buildroot}%{_libdir}/httpd/modules/mod_ranged.so

%clean
%{__rm} -rf %{buildroot}

%post

%preun

%postun

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_ranged.conf
%{_libdir}/httpd/modules/mod_ranged.so

%changelog
* Mon Aug 6 2012 ianmmeyer@gmail.com
- First pass at mod_ranged.spec
