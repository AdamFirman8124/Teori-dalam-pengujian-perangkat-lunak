# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


@pytest.mark.parametrize(
    ("file_name", "expected"),
    [
        ("README", "No"),
        ("README.pdf", "No"),
        (".txt", "No"),
        ("1README.txt", "No"),
        ("file1234.dll", "No"),
    ],
)
def test_file_name_check_rejects_invalid_names(file_name, expected):
    assert file_name_check(file_name) == expected


@pytest.mark.parametrize("file_name", ["file.txt", "app123.exe", "library.dll"])
def test_file_name_check_accepts_valid_names(file_name):
    assert file_name_check(file_name) == "Yes"
