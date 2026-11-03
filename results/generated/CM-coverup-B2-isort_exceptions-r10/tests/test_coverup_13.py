# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

from isort.exceptions import UnsupportedEncoding


def test_unsupported_encoding_with_str_filename():
    """UnsupportedEncoding should store the filename and build a message (str input)."""
    filename = "some_file.py"
    error = UnsupportedEncoding(filename)
    assert error.filename == filename
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(error, Exception)


def test_unsupported_encoding_with_path_filename():
    """UnsupportedEncoding should store the filename and build a message (Path input)."""
    filename = Path("some_file.py")
    error = UnsupportedEncoding(filename)
    assert error.filename == filename
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(error, Exception)
