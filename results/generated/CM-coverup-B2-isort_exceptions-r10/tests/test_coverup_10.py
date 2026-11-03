# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest

from isort.exceptions import FileSkipped


def test_file_skipped_stores_message_and_file_path():
    """FileSkipped should pass the message to the base exception and store file_path."""
    message = "File was skipped due to settings"
    file_path = "/path/to/skipped_file.py"

    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipped(message, file_path)

    exception = exc_info.value
    # Verifies line 50: super().__init__(message) was called
    assert str(exception) == message
    # Verifies line 51: file_path attribute was set
    assert exception.file_path == file_path
