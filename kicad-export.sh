#!/bin/sh
set -e

TIMESTAMP="2015.10.24"
MAIN_REV=6276
LIB_REV=bd0ec6a
DOC_REV=5787c29
I18N_REV=72e7da0

cd kicad.bzr
rm -rf kicad-$TIMESTAMP
bzr export -r $MAIN_REV kicad-$TIMESTAMP
echo "Creating kicad-$TIMESTAMP.tar.xz ..."
tar cJf kicad-$TIMESTAMP.tar.xz kicad-$TIMESTAMP
cd ../kicad-library
echo "Creating kicad-library-$TIMESTAMP.tar.xz ..."
git reset --hard $LIB_REV
git archive --prefix=kicad-library-$TIMESTAMP/ HEAD |xz -9 >kicad-library-$TIMESTAMP.tar.xz
cd ../kicad-doc
echo "Creating kicad-doc-$TIMESTAMP.tar.xz ..."
git reset --hard $DOC_REV
git archive --prefix=kicad-doc-$TIMESTAMP/ HEAD |xz -9 >kicad-doc-$TIMESTAMP.tar.xz
cd ../kicad-i18n
echo "Creating kicad-i18n-$TIMESTAMP.tar.xz ..."
git reset --hard $I18N_REV
git archive --prefix=kicad-i18n-$TIMESTAMP/ HEAD |xz -9 >kicad-i18n-$TIMESTAMP.tar.xz
cd ../footprints
echo "Creating kicad-footprints-$TIMESTAMP.tar.xz ..."
rm -rf kicad-footprints-$TIMESTAMP
mkdir -p kicad-footprints-$TIMESTAMP
>kicad-footprints-$TIMESTAMP/VERSIONS.footprints
sed -n 's|.*\${KIGITHUB}/\([^)]*\)).*|\1|p' \
	../kicad-library/template/fp-lib-table.for-github |
	while read FP
	do
		if [ -d $FP ]
		then
			cd $FP
			REV=$(git rev-list -n 1 --before="$TIMESTAMP" master)
			if [ -z $REV ]
			then
				echo "$FP did not exist at $TIMESTAMP!"
				REV=$(git rev-list -n 1 master)
			fi
			git archive --prefix=$FP/ $REV |tar xf - -C ../kicad-footprints-$TIMESTAMP
			echo $FP $REV >>../kicad-footprints-$TIMESTAMP/VERSIONS.footprints
			cd ..
		else
			echo "$FP missing now. Update libraries snapshot or patch it away from fp-lib-table!"
		fi
	done
tar -cJf kicad-footprints-$TIMESTAMP.tar.xz kicad-footprints-$TIMESTAMP
cd ..
