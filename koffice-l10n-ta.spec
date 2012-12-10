Name: koffice-l10n-ta
Version: 1.9.98.5
Release: %mkrel 2
Summary: Language files for KOffice Tamil
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: http://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/unstable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-ta
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Tamil translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.98.5-2mdv2011.0
+ Revision: 612655
- the mass rebuild of 2010.1 packages

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330507
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312760
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305063
- add source and spec
- Created package structure for koffice-l10n-ta.


* Sat Jul 15 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.2-1
- 1.5.2

* Wed Jul 12 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-3
- Requires koffice-apps

* Sat May 27 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-2
- Use %%mkrel

* Wed May 24 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-1mdk
- 1.5.1

* Tue May 02 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.0-1mdk
- 1.5.0

* Thu Jul 28 2005 Laurent MONTEL <lmontel@mandriva.com> 10mdk
- Fix provides koffice-l10n

* Sat Apr 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2-0.rc1.5mdk
- fix buildrequires
- spec cosmetics

* Wed Jul 16 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2-0.rc1.4mdk
- buildrequires
- macroize

