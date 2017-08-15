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
AutoReqProv:    no

%description
Apache Arrow is a columnar in-memory analytics layer designed to accelerate big data.

%package java
Summary:	%{name} java development package
Group:		Development/Libraries

%description java
Java Development files for %{name}.

%package cpp
Summary:	%{name} c++ development package
Group:		Development/Libraries

%description cpp
C++ Shared Object files for %{name}.

%package cpp-devel
Summary:	%{name} c++ development package
Group:		Development/Libraries
Requires:	%{name}-cpp = %{version}

%description cpp-devel
C++ Development files for %{name}.

%prep
%setup -n arrow-%{name}-%{version}

%build
cd %{_builddir}/arrow-%{name}-%{version}/java && mvn install
cd %{_builddir}/arrow-%{name}-%{version}/cpp && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr && make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd cpp && make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/share/java/arrow/
cp %{_builddir}/arrow-%{name}-%{version}/java/format/target/arrow-format-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/arrow/
cp %{_builddir}/arrow-%{name}-%{version}/java/memory/target/arrow-memory-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/arrow/
cp %{_builddir}/arrow-%{name}-%{version}/java/tools/target/arrow-tools-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/arrow/
cp %{_builddir}/arrow-%{name}-%{version}/java/vector/target/arrow-vector-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/arrow/

%clean
rm -rf $RPM_BUILD_ROOT

%post cpp
ldconfig

%postun cpp
ldconfig

%files java
%defattr(-,root,root,-)
/usr/share/java/arrow/

%files cpp
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/libarrow.so.*
%{_libdir}/libarrow.so

%files cpp-devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/libarrow.a
%{_libdir}/pkgconfig

%changelog
