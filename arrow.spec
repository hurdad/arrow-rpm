%define debug_package %{nil}
Name:           apache-arrow
Version:        %{VERSION}
Release:        1%{?dist}
Summary:        Apache Arrow is a columnar in-memory analytics layer designed to accelerate big data.
Group:          System Environment/Libraries
License:        Apache 2.0
URL:            https://arrow.apache.org/
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  boost-static
BuildRequires:  boost-devel
BuildRequires:  gcc-c++ 
BuildRequires:  cmake
Requires:       boost-filesystem
Requires:	boost-system
AutoReqProv:    no

%description
Apache Arrow is a columnar in-memory analytics layer designed to accelerate big data.

%package cpp
Summary:	%{name} c++ development package
Group:		Development/Libraries

%description cpp
C++ Shared Object files for %{name}.

%package cpp-gpu
Summary:	%{name} c++ gpu development package
Group:		Development/Libraries

%description cpp-gpu
GPU C++ Shared Object files for %{name}.

%package cpp-devel
Summary:	%{name} c++ development package
Group:		Development/Libraries
Requires:	%{name}-cpp = %{version}

%description cpp-devel
C++ Development files for %{name}.

%prep
%setup -n arrow-%{name}-%{version}

%build
cd %{_builddir}/arrow-%{name}-%{version}/cpp && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DARROW_GPU=ON && make %{?_smp_mflags}

%check
cd cpp && make unittest

%install
rm -rf $RPM_BUILD_ROOT
cd cpp && make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post cpp
ldconfig

%postun cpp
ldconfig

%files cpp
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/libarrow.so*

%files cpp-gpu
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/libarrow_gpu.so*

%files cpp-devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/libarrow.a
%{_libdir}/libarrow_gpu.a
%{_libdir}/pkgconfig/*

%changelog
