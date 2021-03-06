%define name		clog
%define version		0.6.4
%define release		1

Name: 		%{name}
Summary: 	Library that provides various logging services
Version: 	%{version}
Release: 	%{release}
License: 	ISC
Group: 		System Environment/Libraries
URL:		http://opensource.conformal.com/wiki/clog
Source: 	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Prefix: 	/usr

%description
clog (Copious Logger) is a library that provides various logging services.
It can be used to log information to syslog or stderr at various levels of
verboseness. The user can define his/her own debug/verbosity flags to,
at run-time, determine how verbose an application or daemon is.

%prep
%setup -q

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT LOCALBASE=/usr

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/lib/libclog.so.*


%package devel
Summary: Libraries and header files to develop applications using clog
Group: Development/Libraries
Requires: clens-devel >= 0.0.5

%description devel
This package contains the libraries, include files, and documentation to
develop applications with clog.

%files devel
%defattr(-,root,root)
%doc /usr/share/man/man?/*
/usr/include/clog.h
/usr/lib/libclog.so
/usr/lib/libclog.a

%changelog
* Fri May 31 2013 - davec 0.6.4-1
- Fix OpenBSD port Makefile for modern OpenBSD ports
* Fri Jan 04 2013 - davec 0.6.3-1
- Add support for Bitrig
- Add support for cygwin
- Remove the 'version: ' prefix from clog_verstring
* Tue Jul 17 2012 - davec 0.6.2-1
- Support clang builds
- Fix non-release build versioning
* Tue May 08 2012 - drahn 0.6.1-1
- Unbreak package build
* Tue May 08 2012 - drahn 0.6.0-1
- Add functions to get the current mask logfile and flags
- Add function to all caller to set the logging callback function
- Other minor cleanup and bug fixes
* Tue Apr 24 2012 - drahn 0.5.0-1
- add clog_end() to remove all resources clog has allocated
- fix CN* (masked) function entries on man page
- Other minor cleanup and bug fixes
* Thu Oct 27 2011 - davec 0.4.0-1
- Make clog.h self-contained
- Add addition C<LEVEL> functions to mirror syslog priority levels
- Modify time output for CLOG_F_DATE to include seconds
- Several man page updates and corrections
- Add build versioning
- Other minor cleanup and bug fixes
* Tue Jul 26 2011 - davec 0.3.5-1
- Add logic to install man pages
- Don't link against clens directly from library
* Tue Jun 21 2011 - davec 0.3.4-1
- Create
