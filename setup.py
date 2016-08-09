#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

CONTAINING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

setup(
    name='qidata_widgets',
    version=open(os.path.join(CONTAINING_DIRECTORY,"qidata_widgets/VERSION")).read().split()[0],
    author='Surya Ambrose',
    author_email='sambrose@aldebaran.com',
    packages=find_packages("."),
    package_data={"qidata_widgets":["VERSION"]},
    url='.',
    license='LICENSE.txt',
    description='Contains different Qt Widget to display data_objects and interact with it.',
    scripts=['bin/annotator'],
    long_description=open(os.path.join(CONTAINING_DIRECTORY,'README.md')).read(),
    install_requires=[
        "PySide >= 1.2.2",
        "qidata_objects >= 0.1"
        "qidata_file >= 0.1",
        "argcomplete >= 1.1.0"
    ]
)

