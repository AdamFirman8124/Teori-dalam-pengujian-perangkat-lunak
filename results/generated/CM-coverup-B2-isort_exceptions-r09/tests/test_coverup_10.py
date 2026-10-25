# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest

from isort.exceptions import FileSkipped


def test_file_skipped_initializes_message_and_file_path() -> None:
    message = "File was skipped"
    file_path = "package/module.py"

    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipped(message, file_path)

    assert str(exc_info.value) == message
    assert exc_info.value.args == (message,)
    assert exc_info.value.file_path == file_path
