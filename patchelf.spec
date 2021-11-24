#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	A utility for patching ELF binaries
Name:		patchelf
Version:	0.13
Release:	1
License:	GPL
Group:		Development/Tools
URL:		https://github.com/NixOS/patchelf
Source0:	https://github.com/NixOS/patchelf/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	d387eee9325414be0b1a80c8fbd2745f
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PatchELF is simple utility for modifing existing ELF executables and
libraries. It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%setup -q -n %{name}-%{version}.20210805.a949ff2

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
%doc README.md
%attr(755,root,root) %{_bindir}/patchelf
%{_mandir}/man1/patchelf.1*
