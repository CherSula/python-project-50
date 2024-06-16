#!/usr/bin/env python3
import argparse
import json

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
            diff.setdefault(key, (file1_dict.get(key), None))
        else:
            diff.setdefault(key, (file1_dict.get(key), file2_dict.get(key)))

    for k in file2_dict:
        if k not in file1_dict:
            diff.setdefault(k, (None, file2_dict.get(k)))

    return diff


def convert_to_text(diff):
    generated_diff_str = ''
    sorted_items = sorted(diff.items(), key=lambda x: x[0])
    for key, (value_1, value_2) in sorted_items:
        if value_1 == value_2:
            generated_diff_str += f'\t  {key}: {value_1}\n'
        elif value_1 is None:
            generated_diff_str += f'\t+ {key}: {value_2}\n'
        elif value_2 is None:
            generated_diff_str += f'\t- {key}: {value_1}\n'
        elif value_1 != value_2:
            generated_diff_str += f'\t- {key}: {value_1}\n'
            generated_diff_str += f'\t+ {key}: {value_2}\n'
    return f'{{\n{generated_diff_str}}}'


def get_dict_from(path_to_file):
    with open(path_to_file, 'r') as file_obj:
        file_dict = json.loads(file_obj.read())
    return file_dict


def main():
    file1_dict = get_dict_from('gendiff/file1.json')
    file2_dict = get_dict_from('gendiff/file2.json')
    diff = find_diff(file1_dict, file2_dict)
    result = convert_to_text(diff)
    print(result)


if __name__ == '__main__':
    main()
