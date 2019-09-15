"""
Setup script for PyPi
"""

from distutils.core import setup

setup(
    name='process_data_vicaaya',
    version='0.0.4',
    packages=['process_data_vicaaya', 'process_data_vicaaya.Stream'],
    license='Apache License, Version 2.0',
    description='Post processing for one of my project',
    author='Pramish Paudel',
    author_email='pramish.paudel123@gmail.com',
    url='https://pramishp.github.io/',
    keywords="",
    platforms=['Any'],
    install_requires=[
        'anitopy >= 2.0.0',
        'parse-torrent-name >= 1.1.1'
    ],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
