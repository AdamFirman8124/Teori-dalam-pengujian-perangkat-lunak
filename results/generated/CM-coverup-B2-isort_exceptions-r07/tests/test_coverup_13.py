# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

from isort.exceptions import UnsupportedEncoding


def test_unsupported_encoding_stores_string_filename_and_message():
    filename = "example.py"

    error = UnsupportedEncoding(filename)

    assert error.filename == filename
    assert error.args == (f"Unknown or unsupported encoding in {filename}",)
    assert str(error) == f"Unknown or unsupported encoding in {filename}"


def test_unsupported_encoding_stores_path_filename_and_message():
    filename = Path("example.py")

    error = UnsupportedEncoding(filename)

    assert error.filename == filename
    assert error.args == (f"Unknown or unsupported encoding in {filename}",)
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
