#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	A utility for patching ELF binaries
Name:		patchelf
Version:	0.3
Release:	1
License:	GPL
Group:		Development/Tools
URL:		http://nix.cs.uu.nl/patchelf.html
Source0:	http://nix.cs.uu.nl/dist/nix/patchelf-0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	20d77052ae559c60e6c5efb6ea95af9b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PatchELF is simple utility for modifing existing ELF executables and
libraries. It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%setup -q

%build
%configure
%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/patchelf
