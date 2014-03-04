# -*- coding: utf-8 -*-
"""Installer for the test.template package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='test.template',
    version='0.1',
    description="testing bobtemplate",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Travis-CI',
    author='Torkel Lyng',
    author_email='torkel.lyng@gmail.com',
    url='http://pypi.python.org/pypi/test.template',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['test'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'plone.app.registry',
        'plone.directives.form',
        'plone.i18n',
        'plone.registry',
        'Products.CMFPlone >=4.1',
        'Products.GenericSetup',
        'setuptools',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'plone.app.robotframework [reload,debug]',
            'unittest2',
        ],
        'develop': [
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'sphinx-rtd-theme',
            'sphinxcontrib-robotframework [docs]',
            'plone.app.robotframework [reload,debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
