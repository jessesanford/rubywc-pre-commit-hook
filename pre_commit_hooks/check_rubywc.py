from __future__ import print_function

import argparse
import subprocess
import sys


def check_rubywc(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check.')
    args = parser.parse_args(argv)

    retval = 0

    for source_file in args.filenames:
        command = ["ruby", "-wc", source_file]

        try:
            retval = subprocess.check_call(command, shell=False)
        except subprocess.CalledProcessError as err:
            print('{0}: ruby -wc failed ({1})'.format(source_file, err))
            retval = 1

    return retval


if __name__ == '__main__':
    sys.exit(check_rubywc())
