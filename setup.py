#!/usr/bin/env python
from setuptools import setup

VERSION = '1.0.0'
DESCRIPTION = "Dict2obj: transform dict to simpler object"
LONG_DESCRIPTION = """
Dict2obj is a Python implementation to transform python dict to object,thus you 
can access json with easier way "dot",I'm sure this little tool can save your life
"""

CLASSIFIERS = filter(None, map(str.strip,
                               """
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3",
Operating System :: OS Independent
Topic :: Utilities
Topic :: Database :: Database Engines/Servers
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

setup(
    name="dict2obj",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=('data structures', 'bloom filter', 'bloom', 'filter',
              'probabilistic', 'set'),
    author="Ryan Luo",
    author_email="luo_senmu@163.com",
    url="http://github.com/jaybaird/python-bloomfilter/",
    license="MIT License",
    platforms=['any'],
    test_suite="pybloom.tests",
    zip_safe=True,
    install_requires=['bitarray>=0.3.4'],
    packages=['pybloom']
)
