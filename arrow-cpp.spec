Name:           apache-arrow-cpp
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Apache Arrow is a columnar in-memory analytics layer designed to accelerate big data.
Group:          System Environment/Libraries
License:        Apache 2.0
URL:            https://arrow.apache.org/
Source:         apache-arrow-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/apache-arrow-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  cmake3

%description
Apache Arrow is a columnar in-memory analytics layer designed to accelerate big data.

%package cuda
Summary:	%{name} c++ gpu development package
Group:		Development/Libraries

%description cuda
GPU C++ Shared Object files for %{name}.

%package parquet
Summary:	%{name} c++ parquet development package
Group:		Development/Libraries

%description parquet
Parquet C++ Shared Object files for %{name}.

%package devel
Summary:	%{name} c++ development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
C++ Development files for %{name}.

%prep
%setup -n arrow-apache-arrow-%{version}

%build
cd cpp && cmake3 -DCMAKE_BUILD_TYPE=Release -DARROW_BUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX=/usr -DARROW_CUDA=ON -DARROW_PARQUET=ON && make %{?_smp_mflags}

%check
#cd cpp && make unittest

%install
rm -rf $RPM_BUILD_ROOT
cd cpp && make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%post cuda
ldconfig

%postun cuda
ldconfig

%post parquet
ldconfig

%postun parquet
ldconfig

%files
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/libarrow.so.*
%{_libdir}/libarrow_dataset.so.*

%files cuda
%defattr(-,root,root,-)
%{_libdir}/libarrow_cuda.so.*

%files parquet
%defattr(-,root,root,-)
%{_libdir}/libparquet.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/arrow/*

%changelog
