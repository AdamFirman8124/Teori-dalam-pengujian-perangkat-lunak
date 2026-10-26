# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

import pytest

from isort.exceptions import FileSkipped, FileSkipComment, ISortError


def test_file_skip_comment_init_sets_message_and_file_path():
    file_path = "example.py"
    exc = FileSkipComment(file_path)
    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.file_path == file_path
    assert str(exc) == f"{file_path} contains an file skip comment and was skipped."
    assert exc.args[0] == f"{file_path} contains an file skip comment and was skipped."


def test_file_skip_comment_can_be_raised_and_caught():
    file_path = "/path/to/skipped.py"
    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipComment(file_path)
    assert exc_info.value.file_path == file_path
    assert str(exc_info.value) == f"{file_path} contains an file skip comment and was skipped."
