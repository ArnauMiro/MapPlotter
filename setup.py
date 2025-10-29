#!/usr/bin/env python
#
# MapPlotter tool
#
# Last rev: 2021
from __future__ import print_function, division

from setuptools import setup, find_packages

with open('MapPlotter/__init__.py') as f:
	for l in f.readlines():
		if '__version__' in l:
			__version__ = eval(l.split('=')[1].strip())

with open('README.md') as f:
	readme = f.read()

# Main setup
setup(
	name               = "MapPlotter",
	version            = __version__,
	author             = 'Arnau Miro, Elena Terzić',
	author_email       = 'arnau.miro@upc.edu, elena.terzic@proton.me',
	maintainer         = 'Arnau Miro',
	maintainer_email   = 'arnau.miro@upc.edu',
    long_description   = readme,
    url                = 'https://github.com/ArnauMiro/MapPlotter',
    packages           = find_packages(exclude=('bin','Examples','doc')),
	install_requires   = ['numpy','matplotlib','cartopy','cmocean','datetime','netCDF4','requests'],
	scripts            = ['bin/map_plotter']
)