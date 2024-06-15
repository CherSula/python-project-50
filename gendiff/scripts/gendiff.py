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


def convert_to_text(diff):
    generated_diff_str = ''
    sorted_items = sorted(diff.items(), key=lambda x: x[0])
    for key, (value_1, value_2) in sorted_items:
        if value_1 == value_2:
            generated_diff_str += f'\t  {key}: {value_1}\n'
        elif not value_1:
            generated_diff_str += f'\t+ {key}: {value_2}\n'
        elif not value_2:
            generated_diff_str += f'\t- {key}: {value_1}\n'
        elif value_1 != value_2:
            generated_diff_str += f'\t- {key}: {value_1}\n'
            generated_diff_str += f'\t+ {key}: {value_2}\n'
    return f'{{\n{generated_diff_str}}}'


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

    diff = find_diff(file1_dict, file2_dict)
    result = convert_to_text(diff)
    print(result)


if __name__ == '__main__':
    main()
