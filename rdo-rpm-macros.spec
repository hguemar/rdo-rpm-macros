Name:           rdo-rpm-macros
Version:        1
Release:        1%{?dist}
Summary:        Compat RPM macros for RDO Packages

License:        GPLv2

URL:            http://github.com/hguemar/rdo-rpm-macros
Source0:        macros.rdo-rpm-macros
Source1:        GPL

BuildArch:      noarch


%description
This package contains compat RPM macros for building RDO packages.

%prep
install -pm 644 %{SOURCE1} .

%install
#GPG Key
install -Dpm 644 %{SOURCE0} \
    %{buildroot}/usr/lib/rpm/macros.d/macros.rdo-rpm-macros

%files
%license GPL
/usr/lib/rpm/macros.d/macros.rdo-rpm-macros


%changelog
* Fri Sep  4 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1-1
- Based on epel-rpm-macros

