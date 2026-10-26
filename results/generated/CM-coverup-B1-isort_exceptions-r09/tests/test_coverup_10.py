# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

from isort.exceptions import FileSkipped, ISortError


def test_fileskipped_init_sets_message_and_file_path():
    message = "file was skipped"
    file_path = "/tmp/example.py"
    exc = FileSkipped(message, file_path)
    assert str(exc) == message
    assert exc.args == (message,)
    assert exc.file_path == file_path
    assert isinstance(exc, ISortError)


def test_fileskipped_can_be_raised_and_caught():
    message = "skip me"
    file_path = "some/file.py"
    try:
        raise FileSkipped(message, file_path)
    except FileSkipped as caught:
        assert caught.file_path == file_path
        assert str(caught) == message
        assert isinstance(caught, ISortError)
    else:
        raise AssertionError("FileSkipped was not raised")
