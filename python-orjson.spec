Name:           python-orjson
Version:        3.7.12
Release:        1
Summary:        Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:        Apache-2.0, MIT 
Group:          Development/Languages/Python
URL:            https://github.com/ijl/orjson/
Source0:         https://pypi.io/packages/source/o/orjson/orjson-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python-flit-core
BuildRequires:  python-pip
BuildRequires:  python-wheel
BuildRequires:  python-maturin

Requires: python-maturin

BuildArch:      noarch

%description
orjson is a fast, correct JSON library for Python. 
It benchmarks as the fastest Python library for JSON and is more correct than the standard json library or other third-party libraries. 
It serializes dataclass, datetime, numpy, and UUID instances natively.

%prep
%autosetup -a1 -n orjson-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
