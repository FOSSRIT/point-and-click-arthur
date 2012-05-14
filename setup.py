#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

setup(
    name='point-and-click-arthur',
    version='0.0.1',
    description="Point and click Arthurian adventure!",
    long_description=long_description,
    url='http://github.com/FOSSRIT/point-and-click-arthur',
    license='OSL',
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=[
        ## This actually requires pygame, but it installs very
        ## weirdly when you try it in a virtualenv on Linux.
        #'pygame',
    ],
    #tests_require=['nose'],
    #test_suite='nose.collector',
    packages=['arthur'],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    play-arthur = arthur.main:main
    """
)
