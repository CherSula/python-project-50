import pytest
from gendiff.scripts.gendiff import find_diff


@pytest.mark.parametrize(
    "file1, file2, file_result",
    [
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            './tests/fixtures/result_json.txt',
        ),
    ]
)
def test_gendiff(file1, file2, file_result):
    with open(file_result, "r", encoding="utf-8") as f_f:
        data_sample = f_f.read()

    assert find_diff(file1, file2) == data_sample
