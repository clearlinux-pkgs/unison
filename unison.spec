#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unison
Version  : 2.52.1
Release  : 7
URL      : https://github.com/bcpierce00/unison/archive/v2.52.1/unison-2.52.1.tar.gz
Source0  : https://github.com/bcpierce00/unison/archive/v2.52.1/unison-2.52.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: unison-bin = %{version}-%{release}
Requires: unison-license = %{version}-%{release}
BuildRequires : ocaml
Patch1: 0001-Fixup-makefiles.patch

%description
This directory contains the code for building the tables in
src/unison_tables.ml.

%package bin
Summary: bin components for the unison package.
Group: Binaries
Requires: unison-license = %{version}-%{release}

%description bin
bin components for the unison package.


%package license
Summary: license components for the unison package.
Group: Default

%description license
license components for the unison package.


%prep
%setup -q -n unison-2.52.1
cd %{_builddir}/unison-2.52.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652381353
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1652381353
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unison
cp %{_builddir}/unison-2.52.1/LICENSE %{buildroot}/usr/share/package-licenses/unison/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/unison-2.52.1/src/COPYING %{buildroot}/usr/share/package-licenses/unison/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unison
/usr/bin/unison-fsmonitor

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/unison/8624bcdae55baeef00cd11d5dfcfa60f68710a02
