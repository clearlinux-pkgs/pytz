#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x01FA998FBAC6374A (stub@ubuntu.com)
#
Name     : pytz
Version  : 2018.5
Release  : 54
URL      : https://pypi.debian.net/pytz/pytz-2018.5.tar.gz
Source0  : https://pypi.debian.net/pytz/pytz-2018.5.tar.gz
Source99 : https://pypi.debian.net/pytz/pytz-2018.5.tar.gz.asc
Summary  : World timezone definitions, modern and historical
Group    : Development/Tools
License  : MIT
Requires: pytz-python3
Requires: pytz-license
Requires: pytz-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
============================================

%package legacypython
Summary: legacypython components for the pytz package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pytz package.


%package license
Summary: license components for the pytz package.
Group: Default

%description license
license components for the pytz package.


%package python
Summary: python components for the pytz package.
Group: Default
Requires: pytz-python3

%description python
python components for the pytz package.


%package python3
Summary: python3 components for the pytz package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytz package.


%prep
%setup -q -n pytz-2018.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530383419
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1530383419
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pytz
cp LICENSE.txt %{buildroot}/usr/share/doc/pytz/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/pytz/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
