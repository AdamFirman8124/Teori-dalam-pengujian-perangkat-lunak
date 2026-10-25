# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

import pytest

from isort.exceptions import FileSkipComment, FileSkipped, ISortError


def test_file_skip_comment_message_and_file_path():
    file_path = "example.py"
    exc = FileSkipComment(file_path)
    expected_message = f"{file_path} contains an file skip comment and was skipped."
    assert exc.file_path == file_path
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message


def test_file_skip_comment_inheritance_and_raise():
    file_path = "/path/to/file.py"
    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipComment(file_path)
    exc = exc_info.value
    assert isinstance(exc, FileSkipComment)
    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.file_path == file_path
    assert file_path in str(exc)
    assert "file skip comment" in str(exc)
