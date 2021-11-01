#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : importlib_resources
Version  : 5.4.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/b5/d8/51ace1c1ea6609c01c7f46ca2978e11821aa0efaaa7516002ef6df000731/importlib_resources-5.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/d8/51ace1c1ea6609c01c7f46ca2978e11821aa0efaaa7516002ef6df000731/importlib_resources-5.4.0.tar.gz
Summary  : Read resources from Python packages
Group    : Development/Tools
License  : Apache-2.0
Requires: importlib_resources-license = %{version}-%{release}
Requires: importlib_resources-python = %{version}-%{release}
Requires: importlib_resources-python3 = %{version}-%{release}
Requires: zipp
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zipp

%description
.. image:: https://img.shields.io/pypi/v/importlib_resources.svg
:target: `PyPI link`_

%package license
Summary: license components for the importlib_resources package.
Group: Default

%description license
license components for the importlib_resources package.


%package python
Summary: python components for the importlib_resources package.
Group: Default
Requires: importlib_resources-python3 = %{version}-%{release}

%description python
python components for the importlib_resources package.


%package python3
Summary: python3 components for the importlib_resources package.
Group: Default
Requires: python3-core
Provides: pypi(importlib_resources)
Requires: pypi(zipp)

%description python3
python3 components for the importlib_resources package.


%prep
%setup -q -n importlib_resources-5.4.0
cd %{_builddir}/importlib_resources-5.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635741544
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/importlib_resources
cp %{_builddir}/importlib_resources-5.4.0/LICENSE %{buildroot}/usr/share/package-licenses/importlib_resources/3cd2faf9a752b7838f4b6a634116c24cc3053415
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/importlib_resources/3cd2faf9a752b7838f4b6a634116c24cc3053415

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
