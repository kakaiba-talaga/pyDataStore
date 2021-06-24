import os
from setuptools import find_packages, setup


def read(fileName):
    with open(os.path.join(os.path.dirname(__file__), fileName), encoding="utf-8") as fileIn:
        fileContents = fileIn.read()

    return fileContents

setup(
    name="pyDataStore",
    version="1.0.1",
    description="Persistent and portable serialized data store.",
    url="https://github.com/kakaiba-talaga/pyDataStore",
    author="kakaiba-talaga",
    author_email='kakaiba+github@gmail.com',
    license="GPL-3.0-or-later",
    keywords="datastore, data, store, portable, storage",
    packages=find_packages(),
    long_description=read("readme.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.5, <3.10",
    install_requires=[
        'pycryptodome >= 3.10.1',
    ],
    zip_safe=False,
)
