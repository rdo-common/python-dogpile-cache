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
Version:            1.1.2
Release:            1%{?dist}
Summary:            %{sum}

License:            MIT
URL:                https://pypi.io/project/dogpile.cache
Source0:            https://pypi.io/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

#
# It is unclear why this is pinned at 3.0.0 upstream
# So remove the constraint for now until the fedora stevedore package
# is updated
Patch1:             dogpile.cache-1.0.2-older-stevedore.patch

BuildArch:          noarch

BuildRequires:      python3-decorator >= 4.0.0
BuildRequires:      python3-devel
BuildRequires:      python3-mako
BuildRequires:      python3-mock
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-setuptools
BuildRequires:      python3-stevedore


%description
%{desc}


%package -n python3-dogpile-cache
Summary:  %{sum}

Requires:           python3-mako

%{?python_provide:%python_provide python3-dogpile-cache}

Provides: python3-dogpile-core = %{version}-%{release}
Obsoletes: python3-dogpile-core < 0.4.1-12


%description -n python3-dogpile-cache
%{desc}

%prep
%setup -q -n %{modname}-%{version}
%patch1 -p1

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}


%check
%{__python3} -m pytest


%files -n python3-dogpile-cache
%license LICENSE
%doc README.rst
%{python3_sitelib}/dogpile
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Thu Jan 28 2021 Kevin Fenzi <kevin@scrye.com> - 1.1.2-1
- Update to 1.1.2. Fixes rhbz#1920627

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Kevin Fenzi <kevin@scrye.com> - 1.1.1-1
- Upgrade to 1.1.1. Fixes rhbz#1897941

* Sat Oct 10 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.2-1
- Update to 1.0.2.
- Add patch to use older python-stevedore package in fedora for now for tests.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0 (#1766238).
- https://dogpilecache.sqlalchemy.org/en/latest/changelog.html#change-0.9.0

* Fri Sep 27 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0 (#1754092).
- https://dogpilecache.sqlalchemy.org/en/latest/changelog.html

* Mon Sep 09 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.8-3
- Drop python2-dogpile-cache (#1748419).

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-3
- Rebuilt for Python 3.8

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
