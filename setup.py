#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools
import pypandoc

def main():

    setuptools.setup(
        name             = "distributed_wellbeing",
        version          = "2016.06.27.1807",
        description      = "prototype decentralised wellbeing analysis and distribution system",
        long_description = pypandoc.convert("README.md", "rst"),
        url              = "https://github.com/wdbm/distributed_wellbeing",
        author           = "Will Breaden Madden",
        author_email     = "w.bm@cern.ch",
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

def read(*paths):
    with open(os.path.join(*paths), "r") as filename:
        return filename.read()

if __name__ == "__main__":
    main()
