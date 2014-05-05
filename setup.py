#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Feb 24, 2013
@author: nickmilon
see: https://docs.python.org/2/distutils/setupscript.html
'''
from setuptools  import setup, find_packages
from mongo_vs_es import __version__ 
setup(
    packages=find_packages(),
    #package_data={'pymongo_ext': ['js/*.js']},
    name="mongo_vs_es",
    version=__version__,
    author="nickmilon",
    #author_email="nickmilon@gmail.com",
    maintainer="nickmilon",
    #maintainer_email="nickmilon@gmail.com",
    url="https://github.com/nickmilon/mongo_vs_es",
    description="test/benchmarsks of Text Search between Elastic Search and Mongo",
    long_description="see: readme",
    download_url="https://github.com/nickmilon/mongo_vs_es.git",
    classifiers=[
    "Development Status :: ",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Programming Language :: Python :: 2.7",
    "Topic :: Database"],
    #platforms =
    license="MIT or Apache License, Version 2.0",
    keywords=["mongo", "mongodb", "pymongo", "Elastic Search", "ES", "Text Search"],
    # requirements and specs
    zip_safe=False,
    tests_require=["nose"],
    #install_requires = [],
    install_requires=[
        'pymongo>=2.7',
        'elasticsearch',
        'gevent',
        "git+https://github.com/nickmilon/pymongo_ext.git@master",
    ],
)
