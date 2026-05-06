# Rust sucks
%undefine _debugsource_template
%define module orjson

Name:		python-orjson
Version:	3.11.9
Release:	1
Summary:	Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:	MPL-2.0 AND (Apache-2.0 OR MIT)
Group:		Development/Languages/Python
URL:		https://github.com/ijl/orjson
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz
# To update vendor. Cd to source dir, run in terminal as user "cargo vendor" (rust and cargo must be installed). Then compress vendor dir as .tar.xz

BuildSystem:	python
BuildRequires:	cargo
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-rust)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	rust-packaging

Requires: python%{pyver}dist(maturin)

%description
orjson is a fast, correct JSON library for Python.

It benchmarks as the fastest Python library for JSON and is more correct than
the standard json library or other third-party libraries.

It serializes dataclass, datetime, numpy, and UUID instances natively.

%prep -a
tar xf %{SOURCE1}

# prep vendorered crates
%cargo_prep -v vendor/

# create .cargo/config file from vendoring output
cat >> .cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build -p
export CARGO_HOME=$PWD/.cargo

%build -a
# sort out crate licenses
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT LICENSE-MPL-2.0 LICENSES.dependencies
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
