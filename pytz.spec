#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x01FA998FBAC6374A (stub@ubuntu.com)
#
Name     : pytz
Version  : 2017.2
Release  : 32
URL      : https://pypi.debian.net/pytz/pytz-2017.2.zip
Source0  : https://pypi.debian.net/pytz/pytz-2017.2.zip
Source99 : https://pypi.debian.net/pytz/pytz-2017.2.zip.asc
Summary  : World timezone definitions, modern and historical
Group    : Development/Tools
License  : MIT
Requires: pytz-legacypython
Requires: pytz-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
============================================

%package legacypython
Summary: legacypython components for the pytz package.
Group: Default

%description legacypython
legacypython components for the pytz package.


%package python
Summary: python components for the pytz package.
Group: Default
Requires: pytz-legacypython

%description python
python components for the pytz package.


%prep
%setup -q -n pytz-2017.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505058833
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1505058833
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
