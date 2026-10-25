# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


@pytest.mark.parametrize(
    ("file_name", "expected"),
    [
        ("filename", "No"),
        ("archive.tar.txt", "No"),
        ("report.pdf", "No"),
        (".txt", "No"),
        ("1report.txt", "No"),
        ("report1234.txt", "No"),
    ],
)
def test_file_name_check_rejects_invalid_names(file_name, expected):
    assert file_name_check(file_name) == expected


@pytest.mark.parametrize(
    "file_name",
    [
        ("report.txt"),
        ("app.exe"),
        ("library.dll"),
        ("report123.txt"),
    ],
)
def test_file_name_check_accepts_valid_names(file_name):
    assert file_name_check(file_name) == "Yes"
