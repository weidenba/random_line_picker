#! /usr/bin/env python3
'''
Returns a random line of a text file
'''

import sys
import argparse
import random


PROGRAM_NAME = "Random Line Picker"
PROGRAM_VERSION = "0.1"
PROGRAM_DESCRIPTION = "Returns a random line of a text file"


def _setup_argparser():
    parser = argparse.ArgumentParser(description="{} - {}".format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version="{} {}".format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('input_file', help="text file with several lines")
    return parser.parse_args()


def remove_duplicates(input_list):
    return list(set(input_list))


def get_string_list_from_file(file_path):
    try:
        with open(file_path) as f:
            lines = f.readlines()
    except Exception as e:
        sys.exit("could not extract lines from file: {} {}".format(sys.exc_info()[0].__name__, e))
    return lines


if __name__ == '__main__':

    args = _setup_argparser()

    lines = get_string_list_from_file(args.input_file)
    lines = remove_duplicates(lines)
    print(random.choice(lines))

    sys.exit()
