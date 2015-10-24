#!/bin/sh
set -e

bzr checkout lp:kicad kicad.bzr
git clone https://github.com/KiCad/kicad-library
git clone https://github.com/KiCad/kicad-doc
git clone https://github.com/KiCad/kicad-i18n

fps () { sed -n 's|.*\${KIGITHUB}/\([^)]*\)).*|\1|p'  kicad-library/template/fp-lib-table.for-github; }

mkdir -p footprints
fps |while read FP
	do
		git clone https://github.com/KiCad/$FP footprints/$FP ||
			print "$FP missing, possibly gone from GitHub now"
	done
