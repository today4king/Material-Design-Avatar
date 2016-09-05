#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='avatars',
    version='0.1.0',
    description='Material Design Avatar',
    author='Zhao Jin',
    author_email='kerry@gewu3d.com',
    py_modules=['avatars', ],
    packages=['avatars'],
    url='',
    license="",
    long_description=open('README.md',encoding="utf8").read(),
    install_requires=[
    ],
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ])