#!/usr/bin/env python

version = "0.1.0"

import os
from sys import prefix
from setuptools import setup

setup(
    name = "Tinybat",
    version = version,
    license = "GPL",
    description = "A standalone battery monitor for the rest of us.",
    author = "Aaron Mavrinac",
    author_email = "mavrinac@gmail.com",
    url = "http://code.google.com/p/tinybat",
    download_url = "http://tinybat.googlecode.com/files/tinybat-%s.tar.bz2" % version,
    keywords = "battery acpi",
    packages = [ "tinybat" ],
    scripts = [ "tinybat/tinybat" ],
    data_files = [ ( os.path.join( prefix, "share/tinybat/icons" ), [ os.path.join( "data/icons", f ) for f in os.listdir( "data/icons" ) ] ) ],
)
