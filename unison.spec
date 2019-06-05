#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unison
Version  : 2.51.2
Release  : 3
URL      : https://github.com/bcpierce00/unison/archive/v2.51.2.tar.gz
Source0  : https://github.com/bcpierce00/unison/archive/v2.51.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: unison-bin
BuildRequires : ocaml
Patch1: 0001-Fixup-makefiles.patch

%description
This directory contains the code for building the tables in
src/unison_tables.ml.

%package bin
Summary: bin components for the unison package.
Group: Binaries

%description bin
bin components for the unison package.


%prep
%setup -q -n unison-2.51.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527192082
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1527192082
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unison
/usr/bin/unison-fsmonitor
