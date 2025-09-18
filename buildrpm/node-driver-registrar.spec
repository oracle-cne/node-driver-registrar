

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                node-driver-registrar
%global app_name_release        csi-node-driver-registrar
%global app_version             2.14.0
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Sidecar container that registers the CSI driver with Kubelet using the kubelet plugin registration mechanism.
License:        Apache 2.0
Group:          Development/Tools
Url:            https://github.com/oracle-cne/node-driver-registrar.git
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang
BuildRequires:	make

%description
Sidecar container that registers the CSI driver with Kubelet using the kubelet plugin registration mechanism.

%prep
%setup -q

%build
make build

%install
install -m 755 bin/%{app_name_release} %{buildroot}/%{app_name_release}

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
/%{app_name_release}

%changelog
* Thu Sep 18 2025 Olcne-Builder Jenkins <olcne-builder_us@oracle.com> - 2.14.0-1
- Added Oracle specific build files for CSI node-driver-registrar.

