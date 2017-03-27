Name:           apache-arrow
Version:    	%{VERSION}
Release:        1%{?dist}
Summary:        Apache Arrow is a columnar in-memory analytics layer designed to accelerate big data.
Group:      	System Environment/Libraries
License:    	Apache 2.0
URL:            https://arrow.apache.org/
Source:     	%{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  boost-static
BuildRequires:  boost-devel
BuildRequires:  gcc-c++ 
BuildRequires:  cmake 
AutoReqProv: 	no

%description
Apache Arrow is a columnar in-memory analytics layer designed to accelerate big data.

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n arrow-%{name}-%{version}/cpp/

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
rm -rf $RPM_BUILD_ROOT/home

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/libarrow_*.so
%{_libdir}/libarrow.so

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/libarrow_*.a
%{_libdir}/libarrow.a
%{_libdir}/pkgconfig

%changelog