#! /usr/bin/env python3

# Packages
from setuptools import setup

setup(
    name="tweetsplitter",
    version="0.1.0",
    author="Robin Winslow",
    author_email="robin@robinwinslow.co.uk",
    url="https://github.com/nottrobin/tweetsplitter",
    description=(
        "Split a chunk of text into 280-character blocks"
        "Attempting to split at the end of sentences etc."
    ),
    package=["tweetsplitter"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[]
)
