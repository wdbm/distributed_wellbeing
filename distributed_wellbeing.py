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
version = "2016-06-27T1807Z"
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

import collections
import docopt
import logging
import os
import socket
import sys
import time

import propyte
import shijian

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

    host = "127.0.0.1" # 10.0.0.41
    port_number = 2718

    filename_peers = options["--peersfile"]

    log.info("")

    # Read the local peers list.
    if not os.path.exists(filename_peers):
        log.error("file {filename} not found".format(
            filename = filename_peers
        ))
        program.terminate()
    peers_list_local = [line.rstrip("\n") for line in open(filename_peers)]
    peers_consensus = shijian.List_Consensus()
    peers_consensus.append(tuple(peers_list_local))
    log.debug("peers list local: {peers}".format(
        peers = peers_list_local
    ))
    log.debug("peers list consensus: {peers}".format(
        peers = peers_consensus.consensus()
    ))

    port           = int(str(port_number), 10)
    address_remote = (host, port)

    # Create a datagram socket for UDP.
    socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set the socket to be reusable.
    socket_UDP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Set the socket to accept incoming broadcasts.
    socket_UDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Disengage socket blocking.
    socket_UDP.setblocking(False)
    # Set the socket to accept connections on the port.
    socket_UDP.bind(("", port))

    # Communicate data in a loop.
    log.info("Ctrl c to exit")
    while True:
        # receive
        try:
            # buffer size: 8192
            message, address = socket_UDP.recvfrom(8192)
            message = message.rstrip("\n")
            if message:
                log.debug("{address}:{port_number}> {message}".format(
                    address     = address[0],
                    port_number = port_number,
                    message     = message
                ))

                # upcoming: message accept/reject procedure
                # Record the sender ID in order to limit the number of senders
                # such that scalability problems do not manifest.
                # Record the message ID in order to avoid parsing it again.

                # If a peers list is detected, parse it and add it to the
                # consensus.
                if "peers =" in message:
                    peers_list_remote = eval(message.lstrip("peers =").rstrip(";"))
                    peers_consensus.append(tuple(peers_list_remote))
                    if len(peers_consensus) >= 3:
                        peers_consensus_list = list(peers_consensus.consensus())
                        log.debug("consensus peers list: {peers_consensus_list}".format(
                            peers_consensus_list = peers_consensus_list
                        ))
                        log.debug("update local peers list with consensus peers list")
                        peers_list_local = peers_consensus_list
                # upcoming functionality
                # If a heartbeat is detected, send the local peers list.
                if "heartbeat" in message:
                    message_send = "peers = {peers_list_local};".format(
                        peers_list_local = peers_list_local
                    )
                    socket_UDP.sendto(message_send, address)

        except:
            pass
        # send
        message_send =\
        "message_text = heartbeat; message_ID = {message_ID};".format(
            message_ID = shijian.UID()
        )
        socket_UDP.sendto(message_send, address_remote)
        time.sleep(1)

    log.info("")

    program.terminate()

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
