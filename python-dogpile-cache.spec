
%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%endif

%global modname dogpile.cache

Name:               python-dogpile-cache
Version:            0.4.0
Release:            3%{?dist}
Summary:            A caching front-end based on the Dogpile lock

Group:              Development/Libraries
License:            BSD
URL:                http://pypi.python.org/pypi/dogpile.cache
Source0:            http://pypi.python.org/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch


BuildRequires:      python2-devel
BuildRequires:      python-setuptools
BuildRequires:      python-nose
BuildRequires:      python-dogpile-core

%if 0%{?with_python3}
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-nose
BuildRequires:      python3-dogpile-core
%endif

%description
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread generates
a new value.

dogpile.cache builds on the `dogpile.core
<http://pypi.python.org/pypi/dogpile.core>`_ locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract.   Overall, dogpile.cache is intended as a replacement to the
`Beaker <http://beaker.groovie.org>`_ caching system, the internals of
which are written by the same author.   All the ideas of Beaker which
"work" are re-implemented in dogpile.cache in a more efficient and succinct
manner, and all the cruft (Beaker's internals were first written in 2005)
relegated to the trash heap.

%if 0%{?with_python3}
%package -n python3-dogpile-cache
Summary:            A caching front-end based on the Dogpile lock.
Group:              Development/Libraries

%description -n python3-dogpile-cache
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread generates
a new value.

dogpile.cache builds on the `dogpile.core
<http://pypi.python.org/pypi/dogpile.core>`_ locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract.   Overall, dogpile.cache is intended as a replacement to the
`Beaker <http://beaker.groovie.org>`_ caching system, the internals of
which are written by the same author.   All the ideas of Beaker which
"work" are re-implemented in dogpile.cache in a more efficient and succinct
manner, and all the cruft (Beaker's internals were first written in 2005)
relegated to the trash heap.
%endif

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
%endif
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%check
# Disable tests on epel6
%if 0%{?fedora}
%{__python} setup.py test
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test
popd
%endif
%endif

%files
%doc README.rst LICENSE CHANGES
%{python_sitelib}/dogpile/cache/
%{python_sitelib}/%{modname}-%{version}*

%if 0%{?with_python3}
%files -n python3-dogpile-cache
%doc README.rst LICENSE CHANGES
%{python3_sitelib}/dogpile/cache/
%{python3_sitelib}/%{modname}-%{version}-*
%endif

%changelog
* Tue Dec 18 2012 Ralph Bean <rbean@redhat.com> - 0.4.0-3
- Remove period from end of summary.

* Fri Dec 14 2012 Ralph Bean <rbean@redhat.com> - 0.4.0-2
- Disable tests on epel6.

* Tue Dec 11 2012 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Initial packaging for Fedora
