#!/usr/bin/env python

import sys
import os

from wagtail.utils.setup import assets, sdist, check_bdist_egg

version = 1.7

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, "README.md"), encoding="utf-8").read()
except IOError:
    README = ""

# Hack to prevent "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when setup.py exits
# (see http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name="wagtailblock-register",
    version=version,
    description="Register wagtailblocks with a simple decorator",
    author="Thomas Bisseling",
    author_email="thomasbisselinghall@gmail.com",  # For support queries, please see https://docs.wagtail.io/en/stable/support.html
    packages=find_packages(),
    url="https://github.com/thomasBisseling/wagtailblock-register",
    long_description="\n\n".join([README]),
    long_description_content_type="text/markdown",
    include_package_data=True,
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Wagtail",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
    install_requires=["wagtail"],
)
