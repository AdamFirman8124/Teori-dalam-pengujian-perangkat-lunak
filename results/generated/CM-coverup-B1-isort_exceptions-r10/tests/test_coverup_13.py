# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

from isort.exceptions import ISortError, UnsupportedEncoding


def test_unsupported_encoding_with_str_filename():
    filename = "example.py"
    exc = UnsupportedEncoding(filename)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.filename == filename
    assert str(exc) == f"Unknown or unsupported encoding in {filename}"
    assert exc.args[0] == f"Unknown or unsupported encoding in {filename}"


def test_unsupported_encoding_with_path_filename():
    filename = Path("some/file.py")
    exc = UnsupportedEncoding(filename)
    assert isinstance(exc, ISortError)
    assert exc.filename == filename
    assert exc.filename is filename
    assert str(exc) == f"Unknown or unsupported encoding in {filename}"


def test_unsupported_encoding_can_be_raised_and_caught():
    filename = "bad_encoding.py"
    try:
        raise UnsupportedEncoding(filename)
    except UnsupportedEncoding as exc:
        assert exc.filename == filename
        assert str(exc) == f"Unknown or unsupported encoding in {filename}"
    except ISortError:
        raise AssertionError("Should have been caught as UnsupportedEncoding")
    else:
        raise AssertionError("UnsupportedEncoding was not raised")
