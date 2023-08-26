%define libselinuxver 2.5
%define libsepolver 2.5
Summary: 	SELinux policy compiler
Name: 		checkpolicy
Version: 	3.5
Release: 	1
License: 	GPLv2
Group: 		Development/Other
URL:	 	http://www.selinuxproject.org
Source0:	https://github.com/SELinuxProject/selinux/releases/download/%{name}-%{version}.tar.gz
BuildRequires: 	byacc 
BuildRequires: 	bison 
BuildRequires: 	flex 
BuildRequires: 	sepol-static-devel >= %{libsepolver} 
BuildRequires: 	pkgconfig(libselinux)  >= %{libselinuxver} 

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
make clean
make CC=%{__cc} LIBDIR="%{_libdir}" CFLAGS="%{optflags}" 
cd test
make CC=%{__cc} LIBDIR="%{_libdir}" CFLAGS="%{optflags}" 

%install
mkdir -p %{buildroot}%{_bindir}
make LIBDIR="%{_libdir}" DESTDIR="%{buildroot}" install
install test/dismod %{buildroot}%{_bindir}/sedismod
install test/dispol %{buildroot}%{_bindir}/sedispol


%files
%{_bindir}/checkpolicy
%{_bindir}/checkmodule
%{_mandir}/man8/checkpolicy.8.xz
%{_mandir}/man8/checkmodule.8.xz
%{_mandir}/ru/man8/check*.8.*
%{_bindir}/sedismod
%{_bindir}/sedispol
