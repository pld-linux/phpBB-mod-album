# TODO
# -  post/preun broken (think: upgrades), doesn't it break rpm -V phpBB?
Summary:	Photo Album for phpBB2
Summary(pl.UTF-8):	Album zdjęć dla phpBB2
Name:		phpBB-mod-album
Version:	2.0.53
Release:	0.1
License:	GPL 2
Group:		Applications/WWW
Source0:	http://smartor.is-root.com/downloads/album_v2053.zip
# Source0-md5:	335775e0d40697bb29e9325c9ca695f5
Source1:	%{name}-install.patch
Source2:	%{name}-uninstall.patch
Source3:	%{name}-locale.tar.gz
# patch for modified phpBB,lang_polish
URL:		http://smartor.is-root.com
BuildRequires:	unzip
Requires(post):	patch
Requires:	gd
Requires:	phpBB >= 2.0.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _appdir         %{_datadir}/phpBB
%define         _uploaddir      /var/lib/phpBB/album_mod

%description
This is a phpBB-based photo album/gallery management system. It is
really powerful, stable, efficient, rich features and highly
customizable. The version 2 was written from the scratch for more
security, performance, etc. It is not really a MOD/hack, it is rather
a phpBB-based system.

Features:
 - Fully integrated with phpBB2 backend (DB, session, template, multi
   languages, etc.)
 - Powerful and handy AdminCP
 - Auto-generated thumbnail
 - Manual-uploaded thumbnail
 - Thumbnail cache (for better performance)
 - Multi-categories
 - Powerful and phpBB-like permissions system
 - ModeratorCP
 - Upload Quota
 - Pic Description
 - Recent pics
 - Personal galleries (for member-oriented boards)
 - Rate system
 - Comment system

%description -l pl.UTF-8
To jest oparty na phpBB system zarządzania albumem zdjęć/galerią. Jest
naprawdę potężny, stabilny, wydajny, bogaty w możliwości i wysoko
konfigurowalny. Wersja 2 została przepisana od zera z większą
dbałością o bezpieczeństwo, wydajność itp. To naprawdę nie jest
MOD/hack, ale system oparty na phpBB.

Możliwości:
 - w pełni zintegrowany z backendem phpBB2 (baza danych, sesje,
   szablony, wielojęzyzcność itd.)
 - potężny i poręczny AdminCP
 - automatycznie generowane miniaturki
 - ręcznie wrzucane miniaturki
 - pamięć podręczna dla miniaturek (dla lepszej wydajności)
 - obsługa wielu kategorii
 - Potężny, podobny do phpBB system uprawnień
 - ModeratorCP
 - quota dla wrzucanych zdjęć
 - opisy zdjęć
 - pokazywanie najnowszych zdjęć
 - galerie osobiste (dla witryn zorientowanych na członków)
 - system oceniania
 - system komentarzy

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_uploaddir}/{upload,upload/cache} \
	$RPM_BUILD_ROOT%{_appdir}/{admin,album_mod,language,templates,language/lang_polish}

cp -pR	phpbb_root/*.php			$RPM_BUILD_ROOT%{_appdir}

cp -pR  phpbb_root/admin/*			$RPM_BUILD_ROOT%{_appdir}/admin
cp -pR  phpbb_root/album_mod/*.{php,html}	$RPM_BUILD_ROOT%{_appdir}/album_mod
cp -pR  phpbb_root/language/*			$RPM_BUILD_ROOT%{_appdir}/language
cp -pR  phpbb_root/templates/*			$RPM_BUILD_ROOT%{_appdir}/templates

cp -pR  phpbb_root/album_mod/upload/*		$RPM_BUILD_ROOT%{_uploaddir}/upload
cp -pR  phpbb_root/album_mod/upload/cache/*	$RPM_BUILD_ROOT%{_uploaddir}/upload/cache

ln -s %{_uploaddir}/upload			$RPM_BUILD_ROOT%{_appdir}/album_mod/upload

install %{SOURCE1}				$RPM_BUILD_ROOT%{_appdir}/album_mod/install.patch
install %{SOURCE2}				$RPM_BUILD_ROOT%{_appdir}/album_mod/uninstall.patch
tar zxf %{SOURCE3} -C				$RPM_BUILD_ROOT%{_appdir}/language/lang_polish/
%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_datadir}
patch -p0 < phpBB/album_mod/install.patch
chown root:http %{_datadir}/phpBB/ -R

%preun
cd /usr/share
patch -p0 < phpBB/album_mod/uninstall.patch

%files
%defattr(644,root,root,755)
%doc docs/* scripts/*
%attr(770,root,http) %{_uploaddir}/upload
%attr(770,root,http) %{_uploaddir}/upload/cache

%dir %{_uploaddir}
%dir %{_appdir}
%{_appdir}/*.php
%{_appdir}/admin
%{_appdir}/album_mod
%{_appdir}/language
%{_appdir}/templates
