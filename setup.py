#!/usr/bin/env python
""" Distutils setup file """
import setuptools
import os
from subprocess import check_output

command = "git describe --tags --dirty"
version_format = ("{tag}.dev{commitcount}+{gitsha}",)

def format_version(version, fmt):
    parts = version.split("-")
    assert len(parts) in (3, 4)
    dirty = len(parts) == 4
    tag, count, sha = parts[:3]
    if count == "0" and not dirty:
        return tag
    return fmt.format(tag=tag, commitcount=count, gitsha=sha.lstrip("g"))


version = check_output(command.split()).decode("utf-8").strip()


with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().split("\n")

setuptools.setup(
    name='sphinx_pcap',
    version=version,
    platforms=['any'],
    packages=['sphinx_pcap'],
    url='https://github.com/jinjamator/sphinx-pcap',
    license='',
    author='Wilhelm Putz',
    author_email='jinjamator@aci.guru',
    description='Sphinx support for displaying pcap files',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=['docutils', 'sphinx'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Framework :: Sphinx :: Extension',
        'Natural Language :: English',
    ],
    keywords='sphinx extension pcap tshark tcpdump',
)
