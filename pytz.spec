#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x01FA998FBAC6374A (stub@ubuntu.com)
#
Name     : pytz
Version  : 2020.1
Release  : 74
URL      : https://files.pythonhosted.org/packages/f4/f6/94fee50f4d54f58637d4b9987a1b862aeb6cd969e73623e02c5c00755577/pytz-2020.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f4/f6/94fee50f4d54f58637d4b9987a1b862aeb6cd969e73623e02c5c00755577/pytz-2020.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/f4/f6/94fee50f4d54f58637d4b9987a1b862aeb6cd969e73623e02c5c00755577/pytz-2020.1.tar.gz.asc
Summary  : World timezone definitions, modern and historical
Group    : Development/Tools
License  : MIT
Requires: pytz-python = %{version}-%{release}
Requires: pytz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
pytz - World Timezone Definitions for Python
============================================

%package python
Summary: python components for the pytz package.
Group: Default
Requires: pytz-python3 = %{version}-%{release}

%description python
python components for the pytz package.


%package python3
Summary: python3 components for the pytz package.
Group: Default
Requires: python3-core
Provides: pypi(pytz)

%description python3
python3 components for the pytz package.


%prep
%setup -q -n pytz-2020.1
cd %{_builddir}/pytz-2020.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588085755
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
