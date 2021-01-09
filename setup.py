#!/usr/bin/env python
"""
Installer script for the wavebender module.
"""

from distutils.core import setup

setup(
    name="wavebender",
    description="An audio synthesis library for Python.",
    author='Zach Denton',
    author_email='zacharydenton@gmail.com',
    version="0.4",
    url='http://github.com/zacharydenton/wavebender',
    long_description='An audio synthesis library for Python.',
    classifiers=['Topic :: Multimedia :: Sound/Audio :: Sound Synthesis'],
    packages=['wavebender', ],
    install_requires=[]
)
