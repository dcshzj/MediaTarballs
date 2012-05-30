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

# Configuration (TODO: Move to .conf file)
# S3-like API keys (Get one at http://archive.org/account/s3.php)
accesskey = ""
secretkey = ""
# Archive.org matters
collection = ""
mediatype = ""
# Downloading information
dldhost = "" # Wikimedia or Your.org
method = "" # Wget or rsync

# Nothing to change below...
# Import required packages
import os
import re
import sys
import urllib

# Important global configuration
# %{wiki}-${date}-filename-%{num}.tar where filename is one of the following
filelist = {
	'remote-media',
	'local-media',
}

def welcome():
	print "Welcome to the Media Tarballs uploading script"

def bye():
	print "Done uploading!"
