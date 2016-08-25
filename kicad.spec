Name:           kicad
Version:        4.0.3
Release:        1%{?dist}
Epoch:          1
Summary:        EDA software suite for creation of schematic diagrams and PCBs

Group:          Applications/Engineering
License:        GPLv2+
URL:            http://www.kicad-pcb.org

Source:         https://launchpad.net/kicad/4.0/%{version}/+download/kicad-%{version}.tar.xz
Source1:        https://github.com/KiCad/kicad-doc/archive/%{version}.tar.gz#/kicad-doc-%{version}.tar.gz
Source2:        https://github.com/KiCad/kicad-library/archive/%{version}.tar.gz#/kicad-library-%{version}.tar.gz
Source3:        https://github.com/KiCad/kicad-i18n/archive/%{version}.tar.gz#/kicad-i18n-%{version}.tar.gz

# This needs to be aligned with kicad-library-*/template/fp-lib-table.for-pretty
Source4:        https://github.com/KiCad/Air_Coils_SML_NEOSID.pretty/archive/%{version}.tar.gz#/Air_Coils_SML_NEOSID.pretty-%{version}.tar.gz
Source5:        https://github.com/KiCad/Buttons_Switches_SMD.pretty/archive/%{version}.tar.gz#/Buttons_Switches_SMD.pretty-%{version}.tar.gz
Source6:        https://github.com/KiCad/Buttons_Switches_ThroughHole.pretty/archive/%{version}.tar.gz#/Buttons_Switches_ThroughHole.pretty-%{version}.tar.gz
Source7:        https://github.com/KiCad/Buzzers_Beepers.pretty/archive/%{version}.tar.gz#/Buzzers_Beepers.pretty-%{version}.tar.gz
Source8:        https://github.com/KiCad/Capacitors_SMD.pretty/archive/%{version}.tar.gz#/Capacitors_SMD.pretty-%{version}.tar.gz
Source9:        https://github.com/KiCad/Capacitors_Tantalum_SMD.pretty/archive/%{version}.tar.gz#/Capacitors_Tantalum_SMD.pretty-%{version}.tar.gz
Source10:       https://github.com/KiCad/Capacitors_ThroughHole.pretty/archive/%{version}.tar.gz#/Capacitors_ThroughHole.pretty-%{version}.tar.gz
Source11:       https://github.com/KiCad/Choke_Axial_ThroughHole.pretty/archive/%{version}.tar.gz#/Choke_Axial_ThroughHole.pretty-%{version}.tar.gz
Source12:       https://github.com/KiCad/Choke_Common-Mode_Wurth.pretty/archive/%{version}.tar.gz#/Choke_Common-Mode_Wurth.pretty-%{version}.tar.gz
Source13:       https://github.com/KiCad/Choke_Radial_ThroughHole.pretty/archive/%{version}.tar.gz#/Choke_Radial_ThroughHole.pretty-%{version}.tar.gz
Source14:       https://github.com/KiCad/Choke_SMD.pretty/archive/%{version}.tar.gz#/Choke_SMD.pretty-%{version}.tar.gz
Source15:       https://github.com/KiCad/Choke_Toroid_ThroughHole.pretty/archive/%{version}.tar.gz#/Choke_Toroid_ThroughHole.pretty-%{version}.tar.gz
Source16:       https://github.com/KiCad/Connectors_Molex.pretty/archive/%{version}.tar.gz#/Connectors_Molex.pretty-%{version}.tar.gz
Source17:       https://github.com/KiCad/Connect.pretty/archive/%{version}.tar.gz#/Connect.pretty-%{version}.tar.gz
Source18:       https://github.com/KiCad/Converters_DCDC_ACDC.pretty/archive/%{version}.tar.gz#/Converters_DCDC_ACDC.pretty-%{version}.tar.gz
Source19:       https://github.com/KiCad/Crystals.pretty/archive/%{version}.tar.gz#/Crystals.pretty-%{version}.tar.gz
Source20:       https://github.com/KiCad/Diodes_SMD.pretty/archive/%{version}.tar.gz#/Diodes_SMD.pretty-%{version}.tar.gz
Source21:       https://github.com/KiCad/Diodes_ThroughHole.pretty/archive/%{version}.tar.gz#/Diodes_ThroughHole.pretty-%{version}.tar.gz
Source22:       https://github.com/KiCad/Discret.pretty/archive/%{version}.tar.gz#/Discret.pretty-%{version}.tar.gz
Source23:       https://github.com/KiCad/Display.pretty/archive/%{version}.tar.gz#/Display.pretty-%{version}.tar.gz
Source24:       https://github.com/KiCad/Displays_7-Segment.pretty/archive/%{version}.tar.gz#/Displays_7-Segment.pretty-%{version}.tar.gz
Source25:       https://github.com/KiCad/Divers.pretty/archive/%{version}.tar.gz#/Divers.pretty-%{version}.tar.gz
Source26:       https://github.com/KiCad/EuroBoard_Outline.pretty/archive/%{version}.tar.gz#/EuroBoard_Outline.pretty-%{version}.tar.gz
Source27:       https://github.com/KiCad/Fiducials.pretty/archive/%{version}.tar.gz#/Fiducials.pretty-%{version}.tar.gz
Source28:       https://github.com/KiCad/Filters_HF_Coils_NEOSID.pretty/archive/%{version}.tar.gz#/Filters_HF_Coils_NEOSID.pretty-%{version}.tar.gz
Source29:       https://github.com/KiCad/Fuse_Holders_and_Fuses.pretty/archive/%{version}.tar.gz#/Fuse_Holders_and_Fuses.pretty-%{version}.tar.gz
Source30:       https://github.com/KiCad/Hall-Effect_Transducers_LEM.pretty/archive/%{version}.tar.gz#/Hall-Effect_Transducers_LEM.pretty-%{version}.tar.gz
Source31:       https://github.com/KiCad/Heatsinks.pretty/archive/%{version}.tar.gz#/Heatsinks.pretty-%{version}.tar.gz
Source32:       https://github.com/KiCad/Housings_DFN_QFN.pretty/archive/%{version}.tar.gz#/Housings_DFN_QFN.pretty-%{version}.tar.gz
Source33:       https://github.com/KiCad/Housings_DIP.pretty/archive/%{version}.tar.gz#/Housings_DIP.pretty-%{version}.tar.gz
Source34:       https://github.com/KiCad/Housings_QFP.pretty/archive/%{version}.tar.gz#/Housings_QFP.pretty-%{version}.tar.gz
Source35:       https://github.com/KiCad/Housings_SIP.pretty/archive/%{version}.tar.gz#/Housings_SIP.pretty-%{version}.tar.gz
Source36:       https://github.com/KiCad/Housings_SOIC.pretty/archive/%{version}.tar.gz#/Housings_SOIC.pretty-%{version}.tar.gz
Source37:       https://github.com/KiCad/Housings_SSOP.pretty/archive/%{version}.tar.gz#/Housings_SSOP.pretty-%{version}.tar.gz
Source38:       https://github.com/KiCad/Inductors_NEOSID.pretty/archive/%{version}.tar.gz#/Inductors_NEOSID.pretty-%{version}.tar.gz
Source39:       https://github.com/KiCad/Inductors.pretty/archive/%{version}.tar.gz#/Inductors.pretty-%{version}.tar.gz
Source40:       https://github.com/KiCad/IR-DirectFETs.pretty/archive/%{version}.tar.gz#/IR-DirectFETs.pretty-%{version}.tar.gz
Source41:       https://github.com/KiCad/Labels.pretty/archive/%{version}.tar.gz#/Labels.pretty-%{version}.tar.gz
Source42:       https://github.com/KiCad/LEDs.pretty/archive/%{version}.tar.gz#/LEDs.pretty-%{version}.tar.gz
Source43:       https://github.com/KiCad/Measurement_Points.pretty/archive/%{version}.tar.gz#/Measurement_Points.pretty-%{version}.tar.gz
Source44:       https://github.com/KiCad/Measurement_Scales.pretty/archive/%{version}.tar.gz#/Measurement_Scales.pretty-%{version}.tar.gz
Source45:       https://github.com/KiCad/Mechanical_Sockets.pretty/archive/%{version}.tar.gz#/Mechanical_Sockets.pretty-%{version}.tar.gz
Source46:       https://github.com/KiCad/Microwave.pretty/archive/%{version}.tar.gz#/Microwave.pretty-%{version}.tar.gz
Source47:       https://github.com/KiCad/Mounting_Holes.pretty/archive/%{version}.tar.gz#/Mounting_Holes.pretty-%{version}.tar.gz
Source48:       https://github.com/KiCad/NF-Transformers_ETAL.pretty/archive/%{version}.tar.gz#/NF-Transformers_ETAL.pretty-%{version}.tar.gz
Source49:       https://github.com/KiCad/Oddities.pretty/archive/%{version}.tar.gz#/Oddities.pretty-%{version}.tar.gz
Source50:       https://github.com/KiCad/Opto-Devices.pretty/archive/%{version}.tar.gz#/Opto-Devices.pretty-%{version}.tar.gz
Source51:       https://github.com/KiCad/Oscillators.pretty/archive/%{version}.tar.gz#/Oscillators.pretty-%{version}.tar.gz
Source52:       https://github.com/KiCad/PFF_PSF_PSS_Leadforms.pretty/archive/%{version}.tar.gz#/PFF_PSF_PSS_Leadforms.pretty-%{version}.tar.gz
Source53:       https://github.com/KiCad/Pin_Headers.pretty/archive/%{version}.tar.gz#/Pin_Headers.pretty-%{version}.tar.gz
Source54:       https://github.com/KiCad/Potentiometers.pretty/archive/%{version}.tar.gz#/Potentiometers.pretty-%{version}.tar.gz
Source55:       https://github.com/KiCad/Power_Integrations.pretty/archive/%{version}.tar.gz#/Power_Integrations.pretty-%{version}.tar.gz
Source56:       https://github.com/KiCad/Relays_ThroughHole.pretty/archive/%{version}.tar.gz#/Relays_ThroughHole.pretty-%{version}.tar.gz
Source57:       https://github.com/KiCad/Resistors_SMD.pretty/archive/%{version}.tar.gz#/Resistors_SMD.pretty-%{version}.tar.gz
Source58:       https://github.com/KiCad/Resistors_ThroughHole.pretty/archive/%{version}.tar.gz#/Resistors_ThroughHole.pretty-%{version}.tar.gz
Source59:       https://github.com/KiCad/Resistors_Universal.pretty/archive/%{version}.tar.gz#/Resistors_Universal.pretty-%{version}.tar.gz
Source60:       https://github.com/KiCad/SMD_Packages.pretty/archive/%{version}.tar.gz#/SMD_Packages.pretty-%{version}.tar.gz
Source61:       https://github.com/KiCad/Sockets_BNC.pretty/archive/%{version}.tar.gz#/Sockets_BNC.pretty-%{version}.tar.gz
Source62:       https://github.com/KiCad/Sockets_Mini-Universal.pretty/archive/%{version}.tar.gz#/Sockets_Mini-Universal.pretty-%{version}.tar.gz
Source63:       https://github.com/KiCad/Sockets_MOLEX_KK-System.pretty/archive/%{version}.tar.gz#/Sockets_MOLEX_KK-System.pretty-%{version}.tar.gz
Source64:       https://github.com/KiCad/Sockets.pretty/archive/%{version}.tar.gz#/Sockets.pretty-%{version}.tar.gz
Source65:       https://github.com/KiCad/Socket_Strips.pretty/archive/%{version}.tar.gz#/Socket_Strips.pretty-%{version}.tar.gz
Source66:       https://github.com/KiCad/Sockets_WAGO734.pretty/archive/%{version}.tar.gz#/Sockets_WAGO734.pretty-%{version}.tar.gz
Source67:       https://github.com/KiCad/Symbols.pretty/archive/%{version}.tar.gz#/Symbols.pretty-%{version}.tar.gz
Source68:       https://github.com/KiCad/Terminal_Blocks.pretty/archive/%{version}.tar.gz#/Terminal_Blocks.pretty-%{version}.tar.gz
Source69:       https://github.com/KiCad/TO_SOT_Packages_SMD.pretty/archive/%{version}.tar.gz#/TO_SOT_Packages_SMD.pretty-%{version}.tar.gz
Source70:       https://github.com/KiCad/TO_SOT_Packages_THT.pretty/archive/%{version}.tar.gz#/TO_SOT_Packages_THT.pretty-%{version}.tar.gz
Source71:       https://github.com/KiCad/Transformers_CHK.pretty/archive/%{version}.tar.gz#/Transformers_CHK.pretty-%{version}.tar.gz
Source72:       https://github.com/KiCad/Transformers_SMPS_ThroughHole.pretty/archive/%{version}.tar.gz#/Transformers_SMPS_ThroughHole.pretty-%{version}.tar.gz
Source73:       https://github.com/KiCad/Transistors_OldSowjetAera.pretty/archive/%{version}.tar.gz#/Transistors_OldSowjetAera.pretty-%{version}.tar.gz
Source74:       https://github.com/KiCad/Valves.pretty/archive/%{version}.tar.gz#/Valves.pretty-%{version}.tar.gz
Source75:       https://github.com/KiCad/Varistors.pretty/archive/%{version}.tar.gz#/Varistors.pretty-%{version}.tar.gz
Source76:       https://github.com/KiCad/Wire_Connections_Bridges.pretty/archive/%{version}.tar.gz#/Wire_Connections_Bridges.pretty-%{version}.tar.gz
Source77:       https://github.com/KiCad/Wire_Pads.pretty/archive/%{version}.tar.gz#/Wire_Pads.pretty-%{version}.tar.gz

Patch1:         kicad-4.0.0-nostrip.patch
Patch2:         kicad-4.0.0-freerouting.patch
# https://code.launchpad.net/~lkundrak/kicad/appstream-data/+merge/293391
Patch3:         kicad-4.0.2-appstream.patch

BuildRequires:  desktop-file-utils
BuildRequires:  compat-wxGTK3-gtk2-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  glew-devel
BuildRequires:  openssl-devel
BuildRequires:  libappstream-glib

# Documentation
BuildRequires:  asciidoc
BuildRequires:  dblatex
BuildRequires:  po4a
BuildRequires:  perl(Unicode::GCString)

Requires:       electronics-menu
Requires:       freerouting

%description
KiCad is an EDA software to design electronic schematic
diagrams and printed circuit board artwork up to 16 layers.
KiCad is a set of four softwares and a project manager:
- KiCad: project manager
- Eeschema: schematic entry
- Pcbnew: board editor
- Cvpcb: footprint selector for components used in the circuit design
- Gerbview: GERBER viewer (photoplotter documents)

%package        doc
Summary:        Documentation for KiCad
Group:          Documentation
License:        GPLv2+
BuildArch:      noarch

Provides:       %{name}-doc-de = %{version}-%{release}
Provides:       %{name}-doc-es = %{version}-%{release}
Provides:       %{name}-doc-fr = %{version}-%{release}
Provides:       %{name}-doc-hu = %{version}-%{release}
Provides:       %{name}-doc-it = %{version}-%{release}
Provides:       %{name}-doc-ja = %{version}-%{release}
Provides:       %{name}-doc-pl = %{version}-%{release}
Provides:       %{name}-doc-pt = %{version}-%{release}
Provides:       %{name}-doc-ru = %{version}-%{release}
Provides:       %{name}-doc-zh_CN = %{version}-%{release}

Obsoletes:      %{name}-doc-de < %{version}-%{release}
Obsoletes:      %{name}-doc-es < %{version}-%{release}
Obsoletes:      %{name}-doc-fr < %{version}-%{release}
Obsoletes:      %{name}-doc-hu < %{version}-%{release}
Obsoletes:      %{name}-doc-it < %{version}-%{release}
Obsoletes:      %{name}-doc-ja < %{version}-%{release}
Obsoletes:      %{name}-doc-pl < %{version}-%{release}
Obsoletes:      %{name}-doc-pt < %{version}-%{release}
Obsoletes:      %{name}-doc-ru < %{version}-%{release}
Obsoletes:      %{name}-doc-zh_CN < %{version}-%{release}

%description    doc
Documentation for KiCad.


%prep
%setup -q -a 1 -a 2 -a 3

%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i "s|KICAD_PLUGINS lib/kicad/plugins|KICAD_PLUGINS %{_lib}/kicad/plugins|" CMakeLists.txt


%build

# Symbols libraries
pushd %{name}-library-%{version}/
%cmake -DKICAD_STABLE_VERSION=OFF
make -j1 VERBOSE=1
popd

# Documentation
pushd %{name}-doc-%{version}/
%cmake -DBUILD_FORMATS=html
make -j1 VERBOSE=1
popd

# Translations
mkdir %{name}-i18n-%{version}/build
pushd %{name}-i18n-%{version}/build
%cmake -DKICAD_I18N_UNIX_STRICT_PATH=ON ..
make -j1 VERBOSE=1
popd

# Core components
%if 0%{?fedora} == 23
CXXFLAGS="-fabi-version=8 %{optflags}" \
%endif
%cmake -DKICAD_STABLE_VERSION=OFF -DKICAD_SKIP_BOOST=ON \
  -DKICAD_BUILD_VERSION="%{version}-%{release}" \
  -DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config-3.0-gtk2
make %{_smp_mflags} VERBOSE=1


%install
# KiCAD itself
make INSTALL="install -p" DESTDIR=%{buildroot} install

# install desktop
for desktopfile in %{buildroot}%{_datadir}/applications/*.desktop ; do
  desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --remove-category Development              \
  --delete-original                          \
  ${desktopfile}
done

# Symbols libraries
pushd %{name}-library-%{version}/
make INSTALL="install -p" DESTDIR=%{buildroot} install
popd

# install template
install -d %{buildroot}%{_datadir}/%{name}/template
install -m 644 template/%{name}.pro %{buildroot}%{_datadir}/%{name}/template

# Footprints
mkdir -p %{buildroot}%{_datadir}/%{name}/modules
for S in %{sources}; do
  P=$(basename $S |sed -n 's/\.pretty-.*/.pretty/p')
  [ "$P" ] || continue
  mkdir -p %{buildroot}%{_datadir}/%{name}/modules/$P
  tar xzf $S --strip-components=1 -C %{buildroot}%{_datadir}/%{name}/modules/$P
done
ln -f %{buildroot}%{_datadir}/%{name}/template/fp-lib-table{.for-pretty,}

# Documentation
pushd %{name}-doc-%{version}/
make INSTALL="install -p" DESTDIR=%{buildroot} install
popd

# Translations
pushd %{name}-i18n-%{version}/build
make -j1 VERBOSE=1
make INSTALL="install -p" DESTDIR=%{buildroot} install
popd
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%post
touch --no-create %{_datadir}/icons/hicolor || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-desktop-database &> /dev/null || :


%postun
if [ $1 -eq 0 ]
then
  touch --no-create %{_datadir}/icons/hicolor || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
  touch --no-create %{_datadir}/mime/packages &> /dev/null || :
  update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
fi
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files -f %{name}.lang
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*.*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-%{name}-*.desktop
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*.txt

%files doc
%dir %{_pkgdocdir}
%lang(ca) %{_pkgdocdir}/help/ca
%lang(de) %{_pkgdocdir}/help/de
%lang(en) %{_pkgdocdir}/help/en
%lang(es) %{_pkgdocdir}/help/es
%lang(fr) %{_pkgdocdir}/help/fr
%lang(it) %{_pkgdocdir}/help/it
%lang(ja) %{_pkgdocdir}/help/ja
%lang(nl) %{_pkgdocdir}/help/nl
%lang(pl) %{_pkgdocdir}/help/pl
%lang(ru) %{_pkgdocdir}/help/ru
%{_pkgdocdir}/scripts


%changelog
* Thu Aug 25 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.3-1
- Update to 4.0.3

* Wed Apr 20 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.2-2
- Add AppStream metadata

* Tue Mar 01 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.2-1
- Update to 4.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1:4.0.1-4
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1:4.0.1-3
- Rebuild for glew 1.13

* Thu Dec 17 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.1-2
- Hardcode the C++ ABI version to make wxGTK happy

* Tue Dec 15 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.1-1
- Update to 4.0.1

* Thu Dec 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.0-1
- Update to the release
- SPEC file cleanup:
- Use tarballs, drop the 3rd party libraries we bundled

* Sat Oct 24 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.10.24-1.rev6276
- Update to a later snapshot
- Updated library, new documentation, translations

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2015.08.03-4.rev6041
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 2015.08.03-3.rev6041
- Rebuilt for Boost 1.58

* Mon Aug 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.08.03-2.rev6041
- Set KICAD_BUILD_VERSION
- Ship the maintainer tools with the source package

* Mon Aug 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.08.03-1.rev6041
- Update to a later snapshot

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.21-5.rev5528
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2015.03.21-4.rev5528
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.21-3.rev5528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2015.03.21-2.rev5528
- Handle all 64-bit architectures

* Sun Mar 22 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.03.21-1.rev5528
- Update to a later snapshot
- Fix the freerouter patch
- Enable parallel build

* Thu Mar 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.02.05-1.rev5404
- Update to a later snapshot

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2014.03.13-11.rev4744
- Rebuild for boost 1.57.0
- Add upstream patch to support new Boost.Context API
  (kicad-2014.03.13-boost-context.patch)

* Fri Jan 02 2015 Lubomir Rintel <lkundrak@v3.sk> - 2014.03.13-10.rev4744
- Use local autorouter

* Sun Nov 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 2014.03.13-9.rev4744
- Install library footprints

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 2014.03.13-8.rev4744
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03.13-7.rev4744
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03.13-6.rev4744
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2014.03.13-5.rev4744
- Rebuild for boost 1.55.0

* Tue Mar 18 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-4.rev4744
- Removing ExcludeArch as boost-context has been built for arm

* Mon Mar 17 2014 Ville Skyttä <ville.skytta@iki.fi> - 2014.03.13-3.rev4744
- Don't strip binaries too early (#1076929)

* Mon Mar 17 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-2.rev4744
- Fixing the pcb_calculator desktop file (missing underscore)

* Thu Mar 13 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-1.rev4744
- Update to the latest available revisions
- Building with -j1 instead of _smp_mflags (probably causing build failures)
- Creating scripts for source downloading & postprocessing
- Fixing bogus dates in the changelog

* Mon Dec 23 2013 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2013.06.11-2.rev4021
- Removed kicad.pdf from kicad (Fix #1001243)
- Clean up spec file as suggested by Michael Schwendt
- ldconfig no more needed in this release
- Fix kicad-doc Group
- kicad-doc no more requires kicad
 
* Sat Jun 22 2013 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2013.06.11-1.rev4021
- New upstream release
- Added symbols and modules (with 3d view) from Walter Lain
 
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.01.19-3.rev3256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.01.19-2.rev3256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2012.01.19-1.rev3256
- New upstream release
- Add doxygen as build requirement
- Add bulgarian language
- Add it and pl tutorials
- Update versioning patch
- Add patch to fix python syntax in bom-in-python (Gerd v. Egidy <gerd@egidy.de>)
- Add a new patch to fix a new link time error
- Fix a PS plotting scale bug
- Move junction button close to no connexion button
- Fix thermal relief gap calculation for circular pads in pcbnew
- Add undo/redo support for Pcbnew auto place, auto move, and auto route features.
- Make CvPcb correctly preview the selected component footprint if one has already been assigned.
- Fix a bug in pcb calculation
- Width tuning (width correction) for PS plotting of tracks, pads and vias

* Wed Jan 25 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-4.rev3047
- Fix gcc-4.7 issue by Scott Tsai <scottt.tw@gmail.com> 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.07.12-3.rev3047
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-2.rev3047
- Fix patch command 

* Tue Jul 12 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-1.rev3047
- New upstream version
- Update versioning patch
- Add Polish documentation
- Add Epcos MKT capacitors library
- Fix localisation installation path

* Mon Apr  4 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-3.rev2765
- Fix 3D viewer crash (BZ #693008)

* Wed Mar 23 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-2.rev2765
- Add missing library

* Tue Mar 22 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-1.rev2765
- New upstream version
- Update versioning patch, all others patches no more needed
- Patch to fix a link time error (with help from Kevin Kofler and Nikola Pajkovsky)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.05.27-10.rev2363
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Dan Horák <dan@danny.cz> - 2010.05.27-9.rev2363
- Add s390x as 64-bit arch

* Sat Jan 29 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-8.rev2363
- Fix 3D view crash with some graphics cards (BZ #664143).

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 2010.05.27-7.rev2363
- rebuilt against wxGTK-2.8.11-2

* Tue Jun 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-6
- Fix some module edition issues (https://bugs.launchpad.net/kicad/+bug/593546,
  https://bugs.launchpad.net/kicad/+bug/593547)

* Fri Jun 11 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-5
- Fix a crash in searching string (https://bugs.launchpad.net/kicad/+bug/592566)

* Tue Jun  8 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-4
- Fix a focus issue (https://bugs.launchpad.net/kicad/+bug/587970)
- Fix an unwanted mouse cursor move when using the t hotkey in pcbnew
- Fix an issue on arcs draw in 3D viewer (https://bugs.launchpad.net/kicad/+bug/588882)

* Mon May 31 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-3
- Fix an undo-redo issue (https://bugs.launchpad.net/kicad/+bug/586032)

* Sun May 30 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-2
- Don't forget icons

* Sat May 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-1
- New packager version
- Update kicad version number patch
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587175
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587176

* Fri May 21 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-3
- Fix the kicad version number
- Fix a problem when trying to modify a footprint value in eeschema
  https://bugs.launchpad.net/kicad/+bug/583939

* Tue May 18 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-2
- No backup of patched files to delete
- Add noreplace flag to config macro

* Mon May 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-1
- New upstream version
- All previous patches no more needed
- Backward to cmake 2.6 requirement

* Sun May  9 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.05-1
- New upstream version
- All previous patches no more needed
- Fix url: KiCad move from SourceForge.net to LaunchPad.net
- Remove vendor tag from desktop-file-install
- Add x-kicad-pcbnew mimetype
- Add new icons for mimetype

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-9.rev2515
- Fix a minor bug that occurs when changing module orientation or side

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-8.rev2515
- Auto update 3D viewer: fix https://bugs.launchpad.net/kicad/+bug/571089
- Create png from screen (libedit): fix https://bugs.launchpad.net/kicad/+bug/573833

* Sun May  2 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-7.rev2515
- Rename COTATION class (french word) in DIMENSION and fix
  https://bugs.launchpad.net/kicad/+bug/568356 and https://bugs.launchpad.net/kicad/+bug/568357
- Some code cleaning ans enhancements + fix a bug about last netlist file used (LP #567902)

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-6.rev2515
- Make cleanup feature undoable, fix https://bugs.launchpad.net/kicad/+bug/564619
- Fix issues in SVG export, fix https://bugs.launchpad.net/kicad/+bug/565388
- Minor pcbnew enhancements
- Fix minor gerber problems, fix https://bugs.launchpad.net/kicad/+bug/567881

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-5.rev2515
- DRC have to use the local parameters clearance if specified,
  and NETCLASS value only if no local value specified. 

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-4.rev2514
- Fix https://bugs.launchpad.net/bugs/568896 and https://bugs.launchpad.net/bugs/569312

* Thu Apr 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-3.rev2514
- Fix a crash that happens sometimes when opening the design rule dialog

* Mon Apr 26 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-2.rev2514
- Fix https://bugs.launchpad.net/bugs/570074

* Mon Apr 12 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-1.rev2514
- New upstream version
- Patches no more needed

* Mon Apr  5 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-5.rev2463
- Add patch to fix SF #2981759

* Sat Apr  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-4.rev2463
- Apply upstream patch to fix inch/mm ratio
- Provide a source download URL

* Wed Mar 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-3.rev2463
- Patch with svn revision 2463 which fix 2 bugs
- Harmonize identation in %%changelog

* Tue Mar 16 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2010.03.14-2.rev2462
- Link fixes. Really, these libraries should be linked properly so they don't need
  the executable linking calls to be explicitly correct, but cmake gives me a headache.
- Fix demo installation

* Mon Mar 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-1.rev2462
- New upstream version

* Mon Aug 24 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-4.rev1863
- Multilib path correction, BZ 518916.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.07.07-3.rev1863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-2.rev1863
- Dropped eeschema desktop file.
- Moved English kicad.pdf to main rpm.
- Added ls.so.conf file and ldconfig to post, postun to fix libs issue.
- Dropped category Development from desktop file.

* Tue Jul 7 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2009.07.07-1.rev1863
- svn rev 1863
- documentation splitted into multiple packages
- libraries are now taken directly from SVN rather than from older releases
- build changed to cmake based

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007.07.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2007.07.09-4
- First patch is Patch0 - should fix build in Rawhide.
- Include %%_libdir/kicad directory.
- Drop explicit Requires wxGTK in favour of automatic SONAME dependencies.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2007.07.09-3
- Autorebuild for GCC 4.3

* Mon Oct 15 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-2
- Update desktop file

* Thu Oct 04 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-1
- New upstream version
- Merge previous patches
- Remove X-Fedora, Electronics and Engineering categories
- Update desktop file

* Mon Aug 27 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-4
- License tag clarification

* Thu Aug 23 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-3
- Rebuild

* Wed Feb 14 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-2
- Fix desktop entry. Fix #228598

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-1
- New upstream version

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-4
- Add patch to build with RPM_OPT_FLAGS and remove -s from LDFLAGS
  Contribution of Ville Skyttä <ville[DOT]skytta[AT]iki[DOT]fi>
  Fix #227757
- Fix typo in french summary

* Thu Dec 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> 2006.08.28-3
- Rebuild with wxGTK 2.8.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2006.08.28-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-1
- New upstream version
- Use macro style instead of variable style
- Install missing modules. Fix #206602

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-6
- FE6 rebuild

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-5
- Removing backup files is no more needed.

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-4
- Remove BR libGLU-devel that is no more needed (bug #197501 is closed)
- Fix files permissions.

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-3
- s/mesa-libGLU-devel/libGLU-devel/

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-2
- BR mesa-libGLU-devel

* Wed Jun 28 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-1
- New upstream version

* Tue Jun 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.04.24-5
- Change name
- Use %%{_docdir} instead of %%{_datadir}/doc
- Use %%find_lang
- Update desktop database
- Convert MSDOS EOL to Unix EOL
- Remove BR utrac

* Mon Jun 12 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-4
- Patch to suppress extra qualification compile time error on FC5
- BR utrac to convert MSDOS files before applying patch
  This will be remove for the next upstream version.

* Tue May 23 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-3
- Install help in /usr/share/doc/kicad/ as the path is hardcoded in gestfich.cpp
- Add desktop file

* Mon May 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-2
- Add a second tarball that contains many things that are not included in
  the upstream source tarball such components and footprints librairies,
  help, localisation, etc.

* Sun May 21 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-1
- Initial Fedora RPM
