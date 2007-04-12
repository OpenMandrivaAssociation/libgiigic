%define major 1
%define libname %mklibname giigic %{major}

Summary:	Extension to libgii for action/event binding
Name:		libgiigic
Version:	1.1.2
Release:	%mkrel 4
License:	BSD
Group:		System/Libraries
Url:		http://www.ggi-project.org
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
BuildRequires:	libgii-devel	>= 1.0.2
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%package -n %{libname}-devel
Summary:	Header files for libgiigic library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Header files for libgiigic library

%package -n %{libname}-static-devel
Summary:	Static files for libgiigic library
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}

%description -n %{libname}-static-devel
Static files for libgiigic library.

%prep
%setup -q
./autogen.sh

%build
export echo=echo

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
export echo=echo

%makeinstall_std
%ifarch x86_64
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/cheat.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/keys.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/mousebutton.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/relmouse.so
chrpath -d %{buildroot}%{_libdir}/ggi/gic/recognizer/valuator.so
%endif

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{_libdir}/ggi/gic
%dir %{_libdir}/ggi/gic/recognizer
%config(noreplace) %{_sysconfdir}/ggi/%{name}.conf
%attr(755,root,root) %{_bindir}/gic2c
%attr(755,root,root) %{_libdir}/ggi/gic/recognizer/*.so
%attr(755,root,root) %{_libdir}/ggi/gic/recognizer/*.la
%{_mandir}/man3/*

%files -n %{libname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.%{major}*
%attr(755,root,root) %{_libdir}/libgicaction.so.0*

%files -n %{libname}-devel
%defattr(644,root,root,755)
%doc doc/*.txt
%{_includedir}/ggi/*.h
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_mandir}/man7/*

%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/ggi/gic/recognizer/*.a


