import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, formatter, file_result",
    [
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            'stylish',
            './tests/fixtures/result_stylish.txt',
        ),
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            'plain',
            './tests/fixtures/result_plain.txt',
        ),
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            'json',
            './tests/fixtures/result_json.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            'stylish',
            './tests/fixtures/result_stylish.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            'plain',
            './tests/fixtures/result_plain.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            'json',
            './tests/fixtures/result_json.txt',
        ),
    ]
)
def test_gendiff(file1, file2, formatter, file_result):
    with open(file_result, "r", encoding="utf-8") as f_f:
        data_sample = f_f.read()

    assert generate_diff(file1, file2, formatter) == data_sample
