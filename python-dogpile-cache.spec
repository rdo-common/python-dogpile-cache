%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_python3 1
%endif

%global modname dogpile.cache
%global sum A caching front-end based on the Dogpile lock
%global desc Dogpile consists of two subsystems, one building on top of the other.\
\
dogpile provides the concept of a "dogpile lock", a control structure\
which allows a single thread of execution to be selected as the\
"creator" of some resource, while allowing other threads of execution to\
refer to the previous version of this resource as the creation proceeds;\
if there is no previous version, then those threads block until the\
object is available.\
\
dogpile.cache is a caching API which provides a generic interface to\
caching backends of any variety, and additionally provides API hooks\
which integrate these cache backends with the locking mechanism of\
dogpile.\
\
Overall, dogpile.cache is intended as a replacement to the Beaker\
caching system, the internals of which are written by the same author.\
All the ideas of Beaker which "work" are re- implemented in\
dogpile.cache in a more efficient and succinct manner, and all the cruft\
(Beaker\'s internals were first written in 2005) relegated to the trash\
heap.

Name:               python-dogpile-cache
Version:            0.6.8
Release:            2%{?dist}
Summary:            %{sum}

License:            BSD
URL:                https://pypi.io/project/dogpile.cache
Source0:            https://pypi.io/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-mako
BuildRequires:      python2-pytest-cov
BuildRequires:      python2-devel
BuildRequires:      python2-mock
BuildRequires:      python2-setuptools

%if 0%{?with_python3}
BuildRequires:      python3-devel
BuildRequires:      python3-mako
BuildRequires:      python3-mock
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-setuptools
%endif


%description
%{desc}


%package -n python2-dogpile-cache
Summary:  %{sum}

Requires:           python2-mako

%{?python_provide:%python_provide python2-dogpile-cache}

Provides: python-dogpile-core = %{version}-%{release}
Obsoletes: python-dogpile-core < 0.4.1-12


%description -n python2-dogpile-cache
%{desc}


%if 0%{?with_python3}
%package -n python3-dogpile-cache
Summary:  %{sum}

Requires:           python3-mako

%{?python_provide:%python_provide python3-dogpile-cache}

Provides: python3-dogpile-core = %{version}-%{release}
Obsoletes: python3-dogpile-core < 0.4.1-12


%description -n python3-dogpile-cache
%{desc}
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
%{__python2} setup.py build
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
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}


%check
%{__python2} -m pytest

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} -m pytest
popd
%endif


%files -n python2-dogpile-cache
%license LICENSE
%doc README.rst
%{python2_sitelib}/dogpile
%{python2_sitelib}/%{modname}-%{version}*

%if 0%{?with_python3}
%files -n python3-dogpile-cache
%license LICENSE
%doc README.rst
%{python3_sitelib}/dogpile
%{python3_sitelib}/%{modname}-%{version}-*
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Alfredo Moralejo <amoralej@redhat.com> - 0.6.8-1
- Update to 0.6.8.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.7-1
- Update to 0.6.7 (#1609253).
- https://dogpilecache.readthedocs.io/en/latest/changelog.html#change-0.6.7

* Mon Jul 23 2018 Kevin Fenzi <kevin@scrye.com> - 0.6.6-1
- Fix FTBFS bug #1605662
- Update to 0.6.6.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.5-2
- Rebuilt for Python 3.7

* Thu Apr 12 2018 Ralph Bean <rbean@redhat.com> - 0.6.5-1
- new version

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.4-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.4-2
- Require python-mako.
- Use python2- versions of a few BuildRequires.

* Sat Jul 01 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4 (#1465192).
- http://dogpilecache.readthedocs.io/en/latest/changelog.html#change-0.6.4
- Sort the BuildRequires alphabetically.
- Run the tests.

* Thu Jun 01 2017 Ralph Bean <rbean@redhat.com> - 0.6.3-1
- new version

* Thu Feb 16 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.2-4
- Drop Require on python-dogpile-core (#1422716).
- Provide and obsolete python-dogpile-core.
- Replace the description with upstream's new description, and make it a global.
- Make the summary a global.
- Rename python-dogpile-cache to python2-dogpile-cache.
- Use the license macro.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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
