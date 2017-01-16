#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import setuptools

def main():

    setuptools.setup(
        name             = "distributed_wellbeing",
        version          = "2017.01.16.1617",
        description      = "prototype decentralised wellbeing analysis and distribution system",
        long_description = long_description(),
        url              = "https://github.com/wdbm/distributed_wellbeing",
        author           = "Will Breaden Madden",
        author_email     = "wbm@protonmail.ch",
        license          = "GPLv3",
        py_modules       = [
                           ],
        install_requires = [
                           "abstraction",
                           "propyte",
                           "pyprel",
                           "shijian"
                           ],
        scripts          = [
                           "distributed_wellbeing",
                           "peers.txt",
                           "sentiment_tweets.py"
                           ],
        entry_points     = """
            [console_scripts]
            distributed_wellbeing = distributed_wellbeing:distributed_wellbeing
        """
    )

def long_description(
    filename = "README.md"
    ):

    if os.path.isfile(os.path.expandvars(filename)):
        try:
            import pypandoc
            long_description = pypandoc.convert_file(filename, "rst")
        except ImportError:
            long_description = open(filename).read()
    else:
        long_description = ""
    return long_description

if __name__ == "__main__":
    main()
