%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           alacarte
Version:        0.12.4
Release:        1%{?dist}
Summary:        Menu editor for the GNOME desktop

Group:          Applications/System
License:        LGPLv2+
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/alacarte/0.12/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python, python-devel, gettext
BuildRequires:  pygtk2-devel
BuildRequires:  pkgconfig
BuildRequires:  gnome-menus-devel >= 2.27.92
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
Requires:       pygtk2, gnome-python2-gconf
Requires:       gnome-menus >= 2.27.92

Patch0:		undo-delete.patch

%description
Alacarte is a graphical menu editor that lets you edit, add, and delete
menu entries. It follows the freedesktop.org menu specification and
should work with any desktop environment that uses this specification.

%prep
%setup -q
%patch0 -p1 -b .undo-delete

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# desktop-file-install can't manipulate NotShowIn
sed -i -e 's/NotShowIn=KDE;/OnlyShowIn=GNOME;/' \
  $RPM_BUILD_ROOT%{_datadir}/applications/alacarte.desktop
desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/alacarte.desktop


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS COPYING
%{python_sitelib}/Alacarte
%{_bindir}/alacarte
%{_datadir}/applications/alacarte.desktop
%{_datadir}/alacarte
%{_datadir}/icons/hicolor/16x16/apps/alacarte.png
%{_datadir}/icons/hicolor/22x22/apps/alacarte.png
%{_datadir}/icons/hicolor/24x24/apps/alacarte.png
%{_datadir}/icons/hicolor/32x32/apps/alacarte.png
%{_datadir}/icons/hicolor/48x48/apps/alacarte.png
%{_datadir}/icons/hicolor/256x256/apps/alacarte.png

%changelog
* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.4-1
- Update to 0.12.4

* Sat Sep 12 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.3-2
- Bump the gnome-menus requires

* Tue Sep  8 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.3-1
- Update to 0.12.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 16 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.10-1
- Update to 0.11.10

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.9-2
- Only show in GNOME (#486887)

* Tue Feb 17 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.9-1
- Update to 0.11.9

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.8-1
- Update to 0.11.8

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.7-1
- Update to 0.11.7

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.11.6-6
- Rebuild for Python 2.6

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.6-5
- Tweak %%summary and %%description

* Fri Oct 17 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.6-4
- Make undoing of deletion work

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.6-3
- Update to 0.11.6

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.5-1
- Update to 0.11.5

* Thu Feb 21 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.4-1
- Update to 0.11.4

* Sun Dec 02 2007 Todd Zullinger <tmz@pobox.com> - 0.11.3-5
- put the python scripts in sitelib, not sitearch
- remove autoconf, automake, and intltool BRs
- don't run autoconf/automake in %%build
- BR perl(XML::Parser)
- remove smeg Obsoletes and Provides
- minor rpmlint cleanups

* Sat Aug 11 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.3-4
- Fix the build with intltool 0.36
- Update the license field

* Fri Mar 23 2007 Ray Strode <rstrode@redhat.com> - 0.11.3-3
- change url to gnome.org (bug 233237)

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.3-2
- Update to 0.11.3

* Mon Feb 12 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.2-1.svn20070212
- Bring back editing of the System menu

* Fri Jan 26 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.1.1-2
- Fix the Provides: line

* Thu Jan 11 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.1.1-1
- Update to 0.11.1.1

* Wed Dec 20 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.2-2
- Update to 0.10.2

* Sat Dec  9 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.1-4
- try again 

* Wed Dec  6 2006 Jeremy Katz <katzj@redhat.com> - 0.10.1-2
- build against python 2.5 

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.1-1
- Update to 0.10.1
* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.0-1.fc6
- Update to 0.10.0

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.90-7.fc6
- Fix more build requires

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.90-3.fc6
- Add BR for pkgconfig

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.90-1.fc6
- Update to 0.9.90

* Thu Aug 17 2006 Ray Strode <rstrode@redhat.com> - 0.8-8
- initial build for Fedora Core

* Wed Feb 15 2006 John Mahowald <jpmahowald@gmail.com> - 0.8-7
- Rebuild for Fedora Extras 5

* Fri Feb 3 2006  John Mahowald <jpmahowald@gmail.com> - 0.8-3
- Fix stray reference to smeg
- Use python sitearch macro from template

* Sat Oct 29 2005  John Mahowald <jpmahowald@gmail.com> - 0.8-2
- Rebuild

* Thu Oct 27 2005  John Mahowald <jpmahowald@gmail.com> - 0.8-1
- rename to alacarte
- Update to 0.8

* Thu Oct 20 2005  John Mahowald <jpmahowald@gmail.com> - 0.7.5-4
- remove requires gnome-menus

* Tue Aug 30 2005 John Mahowald <jpmahowald@gmail.com> - 0.7.5-3
- Move to /usr/share

* Tue Jun 28 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.5-2
- Desktop-file-utils for kde desktop entry as well as default one.

* Wed Jun 08 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.5-1
- Rebuilt for 0.7.5

* Sun Jun 06 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.4-1
- Rebuilt for 0.7.4

* Wed Jun 01 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.1-1
- Rebuilt for 0.7.1
- Smeg now use the stock gnome menu icon, removed pixmaps from %%files

* Wed Jun 01 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7-2
- Added missing dependency gnome-python2-gconf

* Tue May 31 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7-1
- Rebuilt for 0.7

* Mon May 30 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.6.2-2
- Added desktop-file-utils to Buildrequires
- Addded desktop-file-utils %%post and %%postun

* Sat May 29 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.6.2-1
- Rebuilt for 0.6.2

* Mon May 23 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.5-1
- Initial build
