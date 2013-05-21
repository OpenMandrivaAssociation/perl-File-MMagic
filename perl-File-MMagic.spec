%define	upstream_name	 File-MMagic
%define	upstream_version 1.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Guess file type from filename and/or filehandle
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This perl library uses perl5 objects to guess file type from filename and/or
filehandle.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.0
+ Revision: 403173
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.27-4mdv2009.0
+ Revision: 256981
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.27-2mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-2mdv2008.0
+ Revision: 86400
- rebuild


* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2007.0
- New release 1.27
- better source URL
- %%mkrel

* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdk
- New release 1.26

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- fix summary
- fix directory ownership
- enable tests
- better url

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.22-1mdk
- 1.22
- cosmetics

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 1.20-1mdk
- 1.20.

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.17-3mdk
- rebuild for new perl
- rm -rf /home/guillomovitch/rpm/tmp/perl-File-MMagic-1.27 in %%install, not %%prep
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

