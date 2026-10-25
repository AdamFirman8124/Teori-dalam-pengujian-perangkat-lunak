# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

from isort.exceptions import FileSkipped, ISortError


def test_fileskipped_init_sets_message_and_file_path():
    message = "file was skipped"
    file_path = "/some/path/to/file.py"
    exc = FileSkipped(message, file_path)
    assert str(exc) == message
    assert exc.args == (message,)
    assert exc.file_path == file_path
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_fileskipped_raise_and_catch_preserves_attributes():
    message = "skip reason"
    file_path = "example.py"
    try:
        raise FileSkipped(message, file_path)
    except FileSkipped as exc:
        assert str(exc) == message
        assert exc.file_path == file_path
    else:
        assert False, "FileSkipped was not raised"
