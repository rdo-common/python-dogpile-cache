%if 0%{?fedora} > 12
%global with_python3 1
%endif

%global modname dogpile.cache

Name:               python-dogpile-cache
Version:            0.6.2
Release:            2%{?dist}
Summary:            A caching front-end based on the Dogpile lock

Group:              Development/Libraries
License:            BSD
URL:                http://pypi.python.org/pypi/dogpile.cache
Source0:            http://pypi.python.org/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python-setuptools
BuildRequires:      python-nose
BuildRequires:      python-mock
BuildRequires:      python-dogpile-core >= 0.4.1

%if 0%{?with_python3}
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-nose
BuildRequires:      python3-mock
BuildRequires:      python3-dogpile-core >= 0.4.1
%endif

Requires:      python-dogpile-core >= 0.4.1

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

Requires:      python3-dogpile-core >= 0.4.1

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

%files
%doc README.rst LICENSE
%{python_sitelib}/dogpile
%{python_sitelib}/%{modname}-%{version}*

%if 0%{?with_python3}
%files -n python3-dogpile-cache
%doc README.rst LICENSE
%{python3_sitelib}/dogpile
%{python3_sitelib}/%{modname}-%{version}-*
%endif

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-2
- Rebuild for Python 3.6

* Sat Aug 27 2016 Kevin Fenzi <kevin@scrye.com> - 0.6.2-1
- Update to 0.6.2. Fixes bug #1370712

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 07 2016 Kevin Fenzi <kevin@scrye.com> - 0.6.1-1
- Update to 0.6.1. Fixes bug #1343255

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 Ralph Bean <rbean@redhat.com> - 0.5.7-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 Ralph Bean <rbean@redhat.com> - 0.5.5-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 0.5.4-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 0.5.3-1
- Latest upstream.
- Modernize python3 conditional.

* Mon Sep 9 2013 Pádraig Brady <pbrady@redhat.com> - 0.5.0-1
- Update to 0.5.0 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- Upstream accepted async patches.
- Added BuildRequires on python-mock
- Restrict python-dogpile-core to newer version.
- Remove tests since they're kind of stochastic.

* Fri Jan 11 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-2.20130111hg111
- Updated experimental async work.
- Actually require python-dogpile-core for install.

* Thu Jan 03 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-1.20130103hg108
- Move to a post-release hg checkout.
- Experimenting with background value creation.
- Temporarily removed the CHANGES doc

* Tue Dec 18 2012 Ralph Bean <rbean@redhat.com> - 0.4.0-3
- Remove period from end of summary.

* Fri Dec 14 2012 Ralph Bean <rbean@redhat.com> - 0.4.0-2
- Disable tests on epel6.

* Tue Dec 11 2012 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Initial packaging for Fedora
