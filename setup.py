# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


VERSION = "?"
execfile(os.path.join(os.path.dirname(__file__), 'src/seilriss/__init__.py'))


requires = [
]

setup(
    name='seilriss',
    version=VERSION,
    author=u'Jürgen Kartnaller',
    author_email='juergen@kartnaller.at',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    extras_require=dict(
        test=[
            'collective.xmltestreport',
            'webtest',
        ],
    ),
    zip_safe=False,
    install_requires=requires,
    test_suite="seilriss",
    entry_points={
        'console_scripts': [
            'seilriss=seilriss.ui:run',
        ],
    },
)
