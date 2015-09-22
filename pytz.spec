#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytz
Version  : 2015.6
Release  : 11
URL      : https://pypi.python.org/packages/source/p/pytz/pytz-2015.6.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pytz/pytz-2015.6.tar.gz
Summary  : World timezone definitions, modern and historical
Group    : Development/Tools
License  : MIT
Requires: pytz-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools

%description
pytz - World Timezone Definitions for Python
============================================

%package python
Summary: python components for the pytz package.
Group: Default

%description python
python components for the pytz package.


%prep
%setup -q -n pytz-2015.6

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
