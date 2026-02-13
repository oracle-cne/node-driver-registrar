

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                node-driver-registrar
%global app_version             2.16.0
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com
%global image_name	            csi-node-driver-registrar

Name:           %{app_name}-container-image
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Sidecar container that registers the CSI driver with Kubelet using the kubelet plugin registration mechanism.
License:        Apache 2.0
Group:          Development/Tools
Url:            https://github.com/oracle-cne/node-driver-registrar.git
Source:         %{name}-%{version}.tar.bz2

%description
Sidecar container that registers the CSI driver with Kubelet using the kubelet plugin registration mechanism.

%prep
%setup -q

%build
%global rpm_name %{app_name}-%{version}-%{release}.%{_build_arch}
%global docker_image container-registry.oracle.com/olcne/%{image_name}:v%{version}

yum clean all
yumdownloader --destdir=${PWD}/rpms %{rpm_name}
podman build --pull \
    --build-arg https_proxy=${https_proxy} \
    -t %{docker_image} -f ./olm/builds/Dockerfile .
podman save -o %{app_name}.tar %{docker_image}

%install
%__install -D -m 644 %{app_name}.tar %{buildroot}/usr/local/share/olcne/%{app_name}.tar

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
/usr/local/share/olcne/%{app_name}.tar

%changelog
* Fri Feb 13 2026 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 2.16.0-1
- Added Oracle specific build files for CSI node-driver-registrar.
