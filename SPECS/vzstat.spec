%define debug_package %{nil}

Summary:	vzlist enhancer
Name:		vzstat
Version:	1.0
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
BuildArch:	noarch
License:	MIT
Group:		Applications/System
URL:		https://github.com/thesharp/vzstat
Source0:	https://github.com/downloads/thesharp/%{name}/%{name}-%{version}.tar.gz
Requires:	vzctl >= 4.0
Requires:	vzkernel >= 2.6.32
Requires:	python >= 2.6
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
vzstat is a little vzlist enhancer for vSwap-enabled OpenVZ kernels.
It shows the RAM usage in a human-readable way and makes a summary
on your RAM/CPU overcommitment.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
%{__install} -D -p -m 0755 vzstat %{buildroot}/%{_sbindir}/vzstat

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/vzstat
%doc LICENSE README.md

%changelog
* Sun May 11 2014 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.0-1.vortex
- Update to 1.0.

* Fri Aug 10 2012 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.4-1
- Update to 0.4.

* Wed Mar 11 2012 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.3-1
- Update to 0.3.

* Wed Mar 07 2012 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.2-1
- Update to 0.2.

* Wed Mar 07 2012 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.1-1
- Initial packaging for Enterprise Linux.

