%define major 1
%define libname %mklibname giigic %{major}
%define develname %mklibname giigic -d
%define staticname %mklibname giigic -d -s

Summary:	Extension to libgii for action/event binding
Name:		libgiigic
Version:	1.1.2
Release:	12
License:	BSD
Group:		System/Libraries
Url:		http://www.ggi-project.org
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
BuildRequires:	libgii-devel	>= 1.0.2
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}

%description
The goal of LibGIIGIC is to provide a single easy to use, 
but yet powerful API for (re)binding any kind of action 
to all possible input devices through LibGII at runtime.
You likely know this feature from modern computer games, 
where you can say which key (= input source) is used to 
shoot (= action) with your shotgun.

%package -n %{libname}
Summary:	Main library for libgiigic
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Main library for libgiigic.

%package -n %{develname}
Summary:	Header files for libgiigic library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%mklibname giigic 1 -d

%description -n %{develname}
Header files for libgiigic library

%package -n %{staticname}
Summary:	Static files for libgiigic library
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%mklibname giigic 1 -d -s

%description -n %{staticname}
Static files for libgiigic library.

%prep
%setup -q

%build
export echo=echo

%configure2_5x

%make

%install
export echo=echo

%makeinstall_std
%ifarch x86_64
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/cheat.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/keys.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/mousebutton.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/relmouse.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/valuator.so
%endif

%files
%doc ChangeLog
%dir %{_libdir}/ggi/gic
%dir %{_libdir}/ggi/gic/recognizer
%config(noreplace) %{_sysconfdir}/ggi/%{name}.conf
%{_bindir}/gic2c
%{_libdir}/ggi/gic/recognizer/*.so
%{_mandir}/man3/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/libgicaction.so.0*

%files -n %{develname}
%doc doc/*.txt
%{_includedir}/ggi/*.h
%{_libdir}/*.so
%{_mandir}/man7/*

%files -n %{staticname}
%{_libdir}/*.a


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-11mdv2011.0
+ Revision: 620125
- the mass rebuild of 2010.0 packages

* Sun Aug 02 2009 Funda Wang <fwang@mandriva.org> 1.1.2-10mdv2010.0
+ Revision: 407504
- fix requires

* Thu Mar 26 2009 Frederic Crozat <fcrozat@mandriva.com> 1.1.2-9mdv2009.1
+ Revision: 361372
- Rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-6mdv2008.1
+ Revision: 175957
- obsolete older devel library

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-5mdv2008.1
+ Revision: 174895
- new devel library policy
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Feb 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-4mdv2007.0
+ Revision: 125250
- correct a typo

* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-3mdv2007.1
+ Revision: 125204
- fix dependencies
- fix dependencies

* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-2mdv2007.1
+ Revision: 125110
- remove rpath

* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-1mdv2007.1
+ Revision: 125094
- make it work
- Import libgiigic

