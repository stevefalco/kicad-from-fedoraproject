#!/bin/sh
set -e

cd kicad.bzr
bzr update
cd ../kicad-library
git pull
cd ../kicad-doc
git pull
cd ../kicad-i18n
git pull
cd ..

fps () { sed -n 's|.*\${KIGITHUB}/\([^)]*\)).*|\1|p' kicad-library/template/fp-lib-table.for-github; }

# Deleted footprints
(fps; fps; ls footprints) |sort |uniq -u |while read FP
do
	echo rm -r footprints/$FP
done

# Update existing ones
fps |while read FP
do
	if [ -d footprints/$FP ]
	then
		cd footprints/$FP
		git pull
		cd ../..
	else
		git clone https://github.com/KiCad/$FP footprints/$FP ||
			print "$FP missing, possibly gone from GitHub now"
	fi
done
