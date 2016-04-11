#
# spec file for package ceph-deploy
#
%global dist_eayunobs .eayunobs.1.0

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

#################################################################################
# common
#################################################################################
Name:           ceph-deploy
Version:       1.5.28
Release:        2%{?dist_eayunobs}
Summary:        Admin and deploy tool for Ceph
License:        MIT
Group:          System/Filesystems
URL:            http://ceph.com/
Source0:        %{name}-%{version}.tar.bz2

Patch0001:      0001-eayunrgw-add-eayunrgw-deploy-architect.patch
Patch0002:      0002-the-implement-of-eayunrgw.patch
Patch0003:      0003-update-command-parameter-required-True.patch
Patch0004:      0004-Create-region-root-pools-Otherwise-fail-to-update-re.patch
Patch0005:      0005-Determine-the-installation-of-httpd.patch
Patch0006:      0006-a-little-problem-about-syntax-var.patch
Patch0007:      0007-Don-t-recursion-when-creating-a-user.patch
Patch0008:      0008-Add-pools.patch
Patch0009:      0009-mkdir-log-path.patch
Patch0010:      0010-Modify-rgw-start-method-and-enable-httpd.patch
Patch0011:      0011-Add-multi-domain-name-when-deploy.patch
Patch0012:      0012-Missing-.-in-pool-name.patch
Patch0013:      0013-Modify-http-start-command.patch
Patch0014:      0014-Modify-region-infile.patch
Patch0015:      0015-eayunrgw-implement-EayunOBS-HA-and-LB-setup-function.patch
Patch0016:      0016-eayunrgw-change-rgw-backend-listening-port-to-8080.patch
Patch0017:      0017-eayunrgw-haproxy-stick-table-size-should-equal-to-2-.patch
Patch0018:      0018-eayunrgw-clean-load-balance-init-procejure.patch
Patch0019:      0019-eayunrgw-comment-stick-table.patch
Patch0020:      0020-eayunrgw-change-rgw-backend-listening-port-to-9090.patch
Patch0021:      0021-eayunrgw-check-new-host-in-ceph.conf-before-extend-l.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  python-distribute
BuildRequires:  python-setuptools
BuildRequires:  python-virtualenv
BuildRequires:  python-mock
BuildRequires:  python-tox
%if 0%{?suse_version}
BuildRequires:  python-pytest
%else
BuildRequires:  pytest
%endif
BuildRequires:  git
Requires:       python-argparse
Requires:       python-distribute
#Requires:      lsb-release
#Requires:      ceph
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

#################################################################################
# specific
#################################################################################
%if 0%{defined suse_version}
%py_requires
%endif

%description
An easy to use admin tool for deploy ceph storage clusters.

%prep
#%%setup -q -n %%{name}
%setup -q
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1

%build
#python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -m 0755 -D scripts/ceph-deploy $RPM_BUILD_ROOT/usr/bin

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%{_bindir}/ceph-deploy
%{python_sitelib}/*

%changelog
* Mon Apr 11 2016 Zhao Chao <chao.zhao@eayun.com> - 1.5.28-2.eayunobs.1.0
- add 0015-eayunrgw-implement-EayunOBS-HA-and-LB-setup-function.patch
- add 0016-eayunrgw-change-rgw-backend-listening-port-to-8080.patch
- add 0017-eayunrgw-haproxy-stick-table-size-should-equal-to-2-.patch
- add 0018-eayunrgw-clean-load-balance-init-procejure.patch
- add 0019-eayunrgw-comment-stick-table.patch
- add 0020-eayunrgw-change-rgw-backend-listening-port-to-9090.patch
- add 0021-eayunrgw-check-new-host-in-ceph.conf-before-extend-l.patch

* Fri Mar 18 2016 Zhao Chao <chao.zhao@eayun.com> - 1.5.28-1.eayunobs.1.0
- add 0001-eayunrgw-add-eayunrgw-deploy-architect.patch
- add 0002-the-implement-of-eayunrgw.patch
- add 0003-update-command-parameter-required-True.patch
- add 0004-Create-region-root-pools-Otherwise-fail-to-update-re.patch
- add 0005-Determine-the-installation-of-httpd.patch
- add 0006-a-little-problem-about-syntax-var.patch
- add 0007-Don-t-recursion-when-creating-a-user.patch
- add 0008-Add-pools.patch
- add 0009-mkdir-log-path.patch
- add 0010-Modify-rgw-start-method-and-enable-httpd.patch
- add 0011-Add-multi-domain-name-when-deploy.patch
- add 0012-Missing-.-in-pool-name.patch
- add 0013-Modify-http-start-command.patch
- add 0014-Modify-region-infile.patch
