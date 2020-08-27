%global vertag Final

Name:                os-maven-plugin
Version:             1.2.3
Release:             1
Summary:             Maven plugin for generating platform-dependent properties
License:             ASL 2.0
URL:                 https://github.com/trustin/os-maven-plugin/
BuildArch:           noarch
Source0:             https://github.com/trustin/%{name}/archive/%{name}-%{version}.Final.tar.gz

Patch0:              0001-Port-to-current-plexus-utils.patch

BuildRequires:       maven-local mvn(junit:junit) mvn(org.apache.maven:maven-core)
BuildRequires:       mvn(org.apache.maven:maven-plugin-api)
BuildRequires:       mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:       mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:       mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:       mvn(org.codehaus.plexus:plexus-utils) mvn(org.sonatype.oss:oss-parent:pom:)

%description
os-maven-plugin is a Maven extension/plugin that generates various
useful platform-dependent project properties normalized from
${os.name} and ${os.arch}.

${os.name} and ${os.arch} are often subtly different between JVM and
operating system versions or they sometimes contain machine-unfriendly
characters such as whitespaces. This plugin tries to remove such
fragmentation so that you can determine the current operating system
and architecture reliably.

%package javadoc
Summary:             API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%autosetup -n %{name}-%{name}-%{version}.%{vertag} -p1

# Remove Eclipse plugin (not needed in Fedora)
%pom_remove_dep org.eclipse:ui
%pom_remove_plugin :maven-jar-plugin
find -name EclipseStartup.java -delete
find -name plugin.xml -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Jul 29 2020 wangxiao <wangxiao65@huawei.com> - 1.2.3-1
- package init
