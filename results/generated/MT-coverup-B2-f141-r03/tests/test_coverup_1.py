# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

from f141 import file_name_check


def test_file_name_check_rejects_invalid_names():
    assert file_name_check("filename") == "No"
    assert file_name_check("archive.tar.txt") == "No"
    assert file_name_check("filename.pdf") == "No"
    assert file_name_check(".txt") == "No"
    assert file_name_check("1file.txt") == "No"
    assert file_name_check("file1234.exe") == "No"


def test_file_name_check_accepts_valid_names():
    assert file_name_check("file.txt") == "Yes"
    assert file_name_check("file123.exe") == "Yes"
    assert file_name_check("Library.dll") == "Yes"
