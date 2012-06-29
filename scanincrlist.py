#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Hydriz
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
import urllib

# Global configuration
# Full URL to the directory that hosts the incremental dumps list
url = "http://ftpmirror.your.org/pub/wikimedia/imagedumps/tarballs/incrs/lists/"
incrdate = "20120627"

# Nothing to change below...
host = url + incrdate + "/"
def welcome():
	print "Scans the listing directory for wikis that have incremental dumps generated for them"

def bye():
	print "Done scanning. Output file is in result.txt of the same directory. Bye!"

def scanDir():
	directory = urllib.urlopen(host)
	raw = directory.read()
	directory.close()
	wikis = re.compile(r'<a href="(?P<wiki>[^>]+)-' + incrdate + '-local-media-incr.gz">[^<]+</a>').finditer(raw)
	wikilisting = []
	for wiki in wikis:
		wikilisting.append([wiki.group('wiki')])
	wikilist = wikilisting
	for something in wikilist:
		somethingelse = '\n'.join(something)
		os.system("echo " + somethingelse + ">> result.txt")

def process():
	welcome()
	scanDir()
	bye()

process()
