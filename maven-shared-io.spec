%bcond_with javadoc
Name:           maven-shared-io
Version:        3.1.0
Release:        1
# Maven-shared defines maven-shared-io version as 1.2
Epoch:          1
Summary:        API for I/O support like logging, download or file scanning
Group:          Development/Java
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-shared-io
Source0:        https://github.com/apache/maven-shared-io/archive/refs/tags/maven-shared-io-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

BuildRequires:  maven-shared
BuildRequires:  maven-components
BuildRequires:  maven-wagon

Obsoletes:      maven-shared-io < %{epoch}:%{version}-%{release}
Provides:       maven-shared-io = %{epoch}:%{version}-%{release}

%description
API for I/O support like logging, download or file scanning.

This is a replacement package for maven-shared-io

%if %{with javadoc}
%package javadoc
Summary:        Javadoc for %{name}
    
%endif
%if %{with javadoc}
%description javadoc
API documentation for %{name}.

%endif
%prep
%setup -q -n maven-shared-io-maven-shared-io-%{version}
cp %{SOURCE1} LICENSE.txt

%files -f .mfiles
%doc README.md LICENSE.txt

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc README.md LICENSE.txt

%endif
