# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


#with open('README.rst') as f:
#    readme = f.read()
#
#with open('LICENSE') as f:
#    license = f.read()

setup(
    name='ChErrReporting',
    version='0.1.0',
    description='Utility to track PostAdj/Accum/EOB errors in CH',
    long_description='Utility to track PostAdj/Accum/EOB errors in CH',
    author='Ankit Gupta',
    author_email='gupta.ankit@optum.com',
    #url='https://github.com/kennethreitz/samplemod',
    #license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)