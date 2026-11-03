# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

from isort.exceptions import ISortError, UnsupportedEncoding


def test_unsupported_encoding_with_str_filename():
    filename = "some_file.py"
    error = UnsupportedEncoding(filename)
    assert error.filename == filename
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(error, ISortError)


def test_unsupported_encoding_with_path_filename():
    filename = Path("some_file.py")
    error = UnsupportedEncoding(filename)
    assert error.filename == filename
    assert error.filename == Path("some_file.py")
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(error, ISortError)
