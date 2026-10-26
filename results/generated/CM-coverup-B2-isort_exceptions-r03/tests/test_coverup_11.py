# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

import pytest

from isort.exceptions import FileSkipComment


def test_file_skip_comment_message_and_attributes():
    file_path = "some/path/to/file.py"
    expected_message = f"{file_path} contains an file skip comment and was skipped."

    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment(file_path)

    assert str(exc_info.value) == expected_message
    assert exc_info.value.file_path == file_path
