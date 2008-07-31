%define	module	File-MMagic
%define	name	perl-%{module}
%define	version	1.27
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Guess file type from filename and/or filehandle
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This perl library uses perl5 objects to guess file type from filename and/or
filehandle.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README.en 
%{perl_vendorlib}/File
%{_mandir}/*/*

