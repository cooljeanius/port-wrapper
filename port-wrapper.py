#!/usr/bin/env python3.3
import sys
import os
import subprocess
import configparser



def call_port(command, arguments):
    """
    This function calls the port executable with the specified parameters,
    printing the output to stdout.
    """
    command = ["port", command] + arguments
    if (os.getuid != 0):
        print("Using sudo to execute port.")
        return subprocess.call(["sudo"] + command)
    else:
        return subprocess.call(command)


def parse_alias(command, config):
    if command in config.options("Aliases"):
        command = config.get("Aliases", command)
    return command


if __name__ == '__main__':
    conf = configparser.RawConfigParser()
    conf.read(os.path.expanduser('~/.config/port-wrapper'))
    if len(sys.argv) > 1:
        cmd = parse_alias(sys.argv[1], conf)
        params = sys.argv[2:]
    else:
        print("No need for wrapper when using interactive mode! Exiting...")
        sys.exit(0)
    call_port(cmd, params)
