%define debug_package %{nil}

Summary:	vzlist enhancer
Name:		vzstat
Version:	0.1
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
BuildArch:	noarch
License:	GPLv3
Group:		Applications/System
URL:		https://github.com/thesharp/vzstat
Source0:	https://github.com/downloads/thesharp/%{name}/%{name}-%{version}.tar.gz
Requires:	vzctl >= 3.0.30
Requires:	vzkernel >= 2.6.32
Requires:	python >= 2.6
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
vzstat is a little vzlist enhancer for vSwap-enabled OpenVZ kernels. It
shows the RAM usage in a human-readable way and makes a summary on your
RAM/CPU overcommitment. And it's just so damn easy to type "vzstat" instead
of "vzlist -o ctid,hostname,physpages.l,physpages,laverage,cpus,cpuunits \
,status". :)

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
%doc LICENSE README.rst

%changelog
* Wed Mar 07 2012 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.1-1
- Initial packaging for Enterprise Linux.

