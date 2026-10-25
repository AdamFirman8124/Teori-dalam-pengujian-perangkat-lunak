# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

from isort.exceptions import ISortError, UnsupportedEncoding


def test_unsupported_encoding_with_str_filename():
    filename = "bad_encoding.py"
    exc = UnsupportedEncoding(filename)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.filename == filename
    assert str(exc) == f"Unknown or unsupported encoding in {filename}"
    assert exc.args == (f"Unknown or unsupported encoding in {filename}",)


def test_unsupported_encoding_with_path_filename():
    filename = Path("some_dir/bad_encoding.py")
    exc = UnsupportedEncoding(filename)
    assert isinstance(exc, ISortError)
    assert exc.filename == filename
    assert exc.filename is filename
    assert str(exc) == f"Unknown or unsupported encoding in {filename}"


def test_unsupported_encoding_can_be_raised_and_caught():
    filename = "unreadable.py"
    try:
        raise UnsupportedEncoding(filename)
    except UnsupportedEncoding as exc:
        assert exc.filename == filename
        assert str(exc) == f"Unknown or unsupported encoding in {filename}"
    else:
        raise AssertionError("UnsupportedEncoding was not raised")
