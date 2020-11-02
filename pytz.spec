#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x01FA998FBAC6374A (stub@ubuntu.com)
#
Name     : pytz
Version  : 2020.4
Release  : 76
URL      : https://files.pythonhosted.org/packages/09/07/448a8887c7195450604dfc0305d80d74324c36ee18ed997664051d4bffe3/pytz-2020.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/09/07/448a8887c7195450604dfc0305d80d74324c36ee18ed997664051d4bffe3/pytz-2020.4.tar.gz
Source1  : https://files.pythonhosted.org/packages/09/07/448a8887c7195450604dfc0305d80d74324c36ee18ed997664051d4bffe3/pytz-2020.4.tar.gz.asc
Summary  : World timezone definitions, modern and historical
Group    : Development/Tools
License  : MIT
Requires: pytz-license = %{version}-%{release}
Requires: pytz-python = %{version}-%{release}
Requires: pytz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
============================================

%package license
Summary: license components for the pytz package.
Group: Default

%description license
license components for the pytz package.


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
%setup -q -n pytz-2020.4
cd %{_builddir}/pytz-2020.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604339626
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pytz
cp %{_builddir}/pytz-2020.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pytz/a2641684130f5e32505fdc2a92ad836f0a13200a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytz/a2641684130f5e32505fdc2a92ad836f0a13200a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
