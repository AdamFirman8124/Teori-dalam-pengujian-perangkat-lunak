# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

from f141 import file_name_check


def test_file_name_check_rejects_missing_or_extra_dots():
    assert file_name_check("document") == "No"
    assert file_name_check("archive.tar.txt") == "No"


def test_file_name_check_rejects_unsupported_suffix():
    assert file_name_check("document.pdf") == "No"


def test_file_name_check_rejects_empty_stem():
    assert file_name_check(".txt") == "No"


def test_file_name_check_rejects_stem_not_starting_with_letter():
    assert file_name_check("1document.txt") == "No"


def test_file_name_check_rejects_more_than_three_digits():
    assert file_name_check("file1234.exe") == "No"


def test_file_name_check_accepts_valid_file_names():
    assert file_name_check("file123.dll") == "Yes"
    assert file_name_check("document.txt") == "Yes"
