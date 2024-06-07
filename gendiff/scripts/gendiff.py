#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', dest='FORMAT',
                    help='set format of output')


def main():
    print(parser.parse_args())


if __name__ == '__main__':
    main()