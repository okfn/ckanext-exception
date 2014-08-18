from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name='ckanext-exception',
    version=version,
    description="Raise an exception at /exception",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Nigel Babu',
    author_email='nigel.babu@okfn.org',
    url='',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.exception'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        awesome=ckanext.exception.plugin:ExceptionPlugin
    ''',
)
