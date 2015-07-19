%define	modname	File-MMagic
%define modver 1.30

Summary:	Guess file type from filename and/or filehandle
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/File/File-MMagic-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This perl library uses perl5 objects to guess file type from filename and/or
filehandle.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README.en 
%{perl_vendorlib}/File
%{_mandir}/man3/*



