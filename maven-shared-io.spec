%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-shared-io
Version:        1.1
Release:        7.1%{?dist}
# Maven-shared defines maven-shared-io version as 1.2
Epoch:          1
Summary:        API for I/O support like logging, download or file scanning
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-shared-io
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-shared-io-1.1 maven-shared-io-1.1
# tar caf maven-shared-io-1.1.tar.xz maven-shared-io-1.1/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch1:         0001-Update-to-easymock-3.2.patch
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  easymock3

Obsoletes:      maven-shared-io < %{epoch}:%{version}-%{release}
Provides:       maven-shared-io = %{epoch}:%{version}-%{release}

%description
API for I/O support like logging, download or file scanning.

This is a replacement package for maven-shared-io

%package javadoc
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch1 -p1

%pom_add_dep org.apache.maven:maven-compat

# Failing tests
rm src/test/java/org/apache/maven/shared/io/location/ArtifactLocatorStrategyTest.java
rm src/test/java/org/apache/maven/shared/io/download/DefaultDownloadManagerTest.java

cp %{SOURCE1} LICENSE.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Aug 30 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7
- Bump release

* Fri Aug 30 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-6
- Migrate from easymock 1 to easymock 3
- Resolves: rhbz#1002479

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-5
- Build with xmvn

* Mon Feb 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-4
- Drop dependency on plexus-container-default

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:1.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Tomas Radej <tradej@redhat.com> - 1:1.1-1
- Initial version

