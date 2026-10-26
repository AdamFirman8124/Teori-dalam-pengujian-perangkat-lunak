# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

from isort.exceptions import UnsupportedEncoding


def test_unsupported_encoding_with_string_filename():
    filename = "example.py"

    error = UnsupportedEncoding(filename)

    assert str(error) == "Unknown or unsupported encoding in example.py"
    assert error.filename == filename


def test_unsupported_encoding_with_path_filename():
    filename = Path("example.py")

    error = UnsupportedEncoding(filename)

    assert str(error) == "Unknown or unsupported encoding in example.py"
    assert error.filename == filename
