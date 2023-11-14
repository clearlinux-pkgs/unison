#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : unison
Version  : 2.53.3
Release  : 8
URL      : https://github.com/bcpierce00/unison/archive/v2.53.3/unison-2.53.3.tar.gz
Source0  : https://github.com/bcpierce00/unison/archive/v2.53.3/unison-2.53.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: unison-bin = %{version}-%{release}
Requires: unison-license = %{version}-%{release}
Requires: unison-man = %{version}-%{release}
BuildRequires : ocaml
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains the code for building the tables in
src/unison_tables.ml.

%package bin
Summary: bin components for the unison package.
Group: Binaries
Requires: unison-license = %{version}-%{release}

%description bin
bin components for the unison package.


%package doc
Summary: doc components for the unison package.
Group: Documentation
Requires: unison-man = %{version}-%{release}

%description doc
doc components for the unison package.


%package license
Summary: license components for the unison package.
Group: Default

%description license
license components for the unison package.


%package man
Summary: man components for the unison package.
Group: Default

%description man
man components for the unison package.


%prep
%setup -q -n unison-2.53.3
cd %{_builddir}/unison-2.53.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1700000114
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1700000114
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unison
cp %{_builddir}/unison-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/unison/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/unison-%{version}/src/COPYING %{buildroot}/usr/share/package-licenses/unison/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
echo "Installing manually via install_append"
## install_append content
mkdir -p %{buildroot}/usr/bin
install -m0755 -t %{buildroot}/usr/bin src/unison src/unison-fsmonitor
mkdir -p %{buildroot}/usr/share/man/man1
install -m0755 -t %{buildroot}/usr/share/man/man1 man/unison.1
mkdir -p %{buildroot}/usr/share/doc/unison
install -m0755 -t %{buildroot}/usr/share/doc/unison doc/unison-manual.*
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unison
/usr/bin/unison-fsmonitor

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/unison/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/unison/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/unison.1
