#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# distributed_wellbeing                                                        #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program distributes wellbeing.                                          #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

usage:
    program [options]

options:
    -h, --help               display help message
    --version                display version and exit
    -v, --verbose            verbose logging
    -s, --silent             silent
    -u, --username=USERNAME  username
    --peersfile=FILENAME     peers list file [default: peers.txt]
"""

name    = "distributed_wellbeing"
version = "2016-06-22T1725Z"
logo    = (
"       ___      __       _ __          __           __\n"
"  ____/ (_)____/ /______(_) /_  __  __/ /____  ____/ /\n"
" / __  / / ___/ __/ ___/ / __ \/ / / / __/ _ \/ __  / \n"
"/ /_/ / (__  ) /_/ /  / / /_/ / /_/ / /_/  __/ /_/ /  \n"
"\__,_/_/____/\__/_/  /_/_.___/\__,_/\__/\___/\__,_/   \n"
"                    ______         _                  \n"
"     _      _____  / / / /_  ___  (_)___  ____ _      \n"
"    | | /| / / _ \/ / / __ \/ _ \/ / __ \/ __ `/      \n"
"    | |/ |/ /  __/ / / /_/ /  __/ / / / / /_/ /       \n"
"    |__/|__/\___/_/_/_.___/\___/_/_/ /_/\__, /        \n"
"                                       /____/         "
)

import docopt
import logging
import os
import sys
import time

import propyte

def main(options):

    global program
    program = propyte.Program(
        options = options,
        name    = name,
        version = version,
        logo    = logo
    )
    global log
    from propyte import log

    filename_peers = options["--peersfile"]

    log.info("")

    # Read the local peers list.
    if not os.path.exists(filename_peers):
        log.error("file {filename} not found".format(
            filename = filename_peers
        ))
        program.terminate()
    peers_list_local = [line.rstrip("\n") for line in open(filename_peers)]
    log.debug("peers list local: {peers}".format(
        peers = peers_list_local
    ))

    # upcoming functionality

    log.info("")

    program.terminate()

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
