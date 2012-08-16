Name:           mod_ranged
Version:        1.0.0
Release:        1%{?dist}
Group:          System/Base
License:        BSD
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Url:            https://github.com/imeyer/mod_ranged
Source:         %{name}-%{version}.tar.gz

Obsoletes: mod_ranged <= %{version}-%{release}
Provides: mod_ranged = %{version}-%{release}

Requires: httpd libcrange
BuildRequires: libcrange httpd-devel

Summary:        Something.

%description
Hi.

%prep

%build
apxs -c $RPM_BUILD_ROOT/mod_ranged.c -lcrange

%install
apxs -i $RPM_BUILD_ROOT/mod_ranged.so

%clean
%{__rm} -rf %{buildroot}

%post

%preun

%postun

%files

%changelog
* Mon Aug 6 2012 ianmmeyer@gmail.com
- First pass at mod_ranged.spec
