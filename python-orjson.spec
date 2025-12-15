# Rust sucks
%undefine _debugsource_packages

Name:           python-orjson
Version:        3.11.5
Release:        1
Summary:        Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:        Apache-2.0, MIT 
Group:          Development/Languages/Python
URL:            https://github.com/ijl/orjson/
Source0:        https://pypi.io/packages/source/o/orjson/orjson-%{version}.tar.gz
# To update vendor. Cd to source dir, run in terminal as user "cargo vendor" (rust and cargo must be installed). Then compress vendor dir as .tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-rust)
BuildRequires:  python%{pyver}dist(flit-core)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(maturin)

Requires: python%{pyver}dist(maturin)

%description
orjson is a fast, correct JSON library for Python. 
It benchmarks as the fastest Python library for JSON and is more correct than the standard json library or other third-party libraries. 
It serializes dataclass, datetime, numpy, and UUID instances natively.

%files
%{python_sitearch}/orjson-%{version}.dist-info
%{python_sitearch}/orjson/
