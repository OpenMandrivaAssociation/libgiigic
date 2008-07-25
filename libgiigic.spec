%define major 1
%define libname %mklibname giigic %{major}
%define develname %mklibname giigic -d
%define staticname %mklibname giigic -d -s

Summary:	Extension to libgii for action/event binding
Name:		libgiigic
Version:	1.1.2
Release:	%mkrel 8
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

%package -n %{develname}
Summary:	Header files for libgiigic library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname giigic 1 -d

%description -n %{develname}
Header files for libgiigic library

%package -n %{staticname}
Summary:	Static files for libgiigic library
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}
Obsoletes:	%mklibname giigic 1 -d -s

%description -n %{staticname}
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%dir %{_libdir}/ggi/gic
%dir %{_libdir}/ggi/gic/recognizer
%config(noreplace) %{_sysconfdir}/ggi/%{name}.conf
%{_bindir}/gic2c
%{_libdir}/ggi/gic/recognizer/*.so
%{_libdir}/ggi/gic/recognizer/*.la
%{_mandir}/man3/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%{_libdir}/libgicaction.so.0*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/*.txt
%{_includedir}/ggi/*.h
%{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man7/*

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/*.a
