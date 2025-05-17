#
# Conditional build:
%bcond_without	tests	# functional tests
#
Summary:	A utility for patching ELF binaries
Summary(pl.UTF-8):	Narzędzie do łatania binariów ELF
Name:		patchelf
Version:	0.18.0
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://github.com/NixOS/patchelf/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	9b091a689583fdc7c3206679586322d5
URL:		https://github.com/NixOS/patchelf
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpmbuild(macros) >= 1.719
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PatchELF is simple utility for modifing existing ELF executables and
libraries. It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%description -l pl.UTF-8
PatchELF to proste narzędzie do łatania istniejących programów
wykonywalnych i bibliotek ELF. Potrafi zmienić loader dynamiczny
("interpreter ELF") programów wykonywalnych oraz zmienić RPATH
programów oraz bibliotek.

%prep
%setup -q

%build
%configure
%{__make}

%if %{with tests}
%{__make} check
%endif

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
%{zsh_compdir}/_patchelf
