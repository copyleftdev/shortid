#!/usr/bin/env python

from distutils.core import setup

__version__ = "0.1.2"

setup(
    name="shortid",
    version=__version__,
    description="Short id generator",
    author="Dmitry Moskowski",
    author_email="me@corpix.ru",
    url="https://github.com/corpix/shortid",
    download_url="https://github.com/corpix/shortid/archive/{0}.tar.gz".format(__version__),
    keywords = ["short", "id", "uuid", "shortid", "tinyid"],
    packages=["shortid"],
    license="MIT",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
