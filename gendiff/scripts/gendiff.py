#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', dest='FORMAT',
                    help='set format of output')


def find_diff(file1_dict, file2_dict):
    diff = {}

    for key in file1_dict:
        if key not in file2_dict:
            diff.setdefault(key, (file1_dict.get(key), ''))
        else:
            diff.setdefault(key, (file1_dict.get(key), file2_dict.get(key)))

    for k in file2_dict:
        if k not in file1_dict:
            diff.setdefault(k, ('', file2_dict.get(k)))

    return diff


def main():
    file1_dict = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": 'false'
    }

    file2_dict = {
        "timeout": 20,
        "verbose": 'true',
        "host": "hexlet.io"
    }

    print(find_diff(file1_dict, file2_dict))


if __name__ == '__main__':
    main()
