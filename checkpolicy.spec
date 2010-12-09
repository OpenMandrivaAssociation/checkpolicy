%define libsepolver 2.0.10-1
Summary: SELinux policy compiler
Name: checkpolicy
Version: 2.0.16
Release: %mkrel 3
License: GPL
Group: Development/Other
Source: http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz

BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: byacc flex sepol-static-devel >= %{libsepolver} selinux-devel bison

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler.  
Only required for building policies. 

%prep
%setup -q

%build
%make clean
%make LIBDIR="%{_libdir}" CFLAGS="%{optflags}" CC=gcc

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%makeinstall_std LIBDIR="%{_libdir}"

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/checkpolicy
%{_bindir}/checkmodule
%{_mandir}/man8/checkpolicy.8*
%{_mandir}/man8/checkmodule.8*

