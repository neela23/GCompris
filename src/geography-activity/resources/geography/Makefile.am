SUBDIRS = africa afrique continents europe northamerica southamerica

xmldir = $(pkgdatadir)/@PACKAGE_DATA_DIR@/geography

xml_in_files = \
	board1_0.xml.in \
	board2_0.xml.in \
	board2_1.xml.in \
	board3_0.xml.in \
	board3_1.xml.in \
	board4_0.xml.in \
	board4_1.xml.in \
	board4_2.xml.in

xml_DATA = $(xml_in_files:.xml.in=.xml)

#
# Do not use the INTLTOOL_XML_RULE, we don't need to embed the translations
# in the file themselves. GCompris pick the translations from the po file at
# runtime.
#
$(xml_DATA): %.xml: %.xml.in
	sed -e "s/\(<\{1\}\/*\)_/\1/g" $< > $@

EXTRA_DIST = ${xml_in_files}
