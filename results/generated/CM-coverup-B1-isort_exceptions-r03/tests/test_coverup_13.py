# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

import pytest

from isort.exceptions import ISortError, UnsupportedEncoding


def test_unsupported_encoding_with_str():
    filename = "example.py"
    exc = UnsupportedEncoding(filename)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.filename == filename
    assert str(exc) == f"Unknown or unsupported encoding in {filename}"
    assert exc.args == (f"Unknown or unsupported encoding in {filename}",)


def test_unsupported_encoding_with_path():
    filename = Path("some_dir/example.py")
    exc = UnsupportedEncoding(filename)
    assert exc.filename == filename
    assert exc.filename is filename
    assert str(exc) == f"Unknown or unsupported encoding in {filename}"


def test_unsupported_encoding_can_be_raised_and_caught():
    filename = Path("bad_encoding.py")
    with pytest.raises(UnsupportedEncoding) as exc_info:
        raise UnsupportedEncoding(filename)
    assert exc_info.value.filename == filename
    assert str(exc_info.value) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(exc_info.value, ISortError)
