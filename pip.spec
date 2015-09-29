#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pip
Version  : 7.1.2
Release  : 22
URL      : https://pypi.python.org/packages/source/p/pip/pip-7.1.2.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pip/pip-7.1.2.tar.gz
Summary  : The PyPA recommended tool for installing Python packages.
Group    : Development/Tools
License  : MIT
Requires: pip-bin
Requires: pip-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : virtualenv

%description
pip
===
The `PyPA recommended
<https://python-packaging-user-guide.readthedocs.org/en/latest/current.html>`_
tool for installing Python packages.

%package bin
Summary: bin components for the pip package.
Group: Binaries

%description bin
bin components for the pip package.


%package python
Summary: python components for the pip package.
Group: Default

%description python
python components for the pip package.


%prep
%setup -q -n pip-7.1.2

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pip
/usr/bin/pip2
/usr/bin/pip2.7

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
