%define	modname	File-MMagic
%define modver 1.30

Summary:	Guess file type from filename and/or filehandle
Name:		perl-%{modname}
Version:	%{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/File-MMagic
Source0:	https://cpan.metacpan.org/authors/id/K/KN/KNOK/File-MMagic-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
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



