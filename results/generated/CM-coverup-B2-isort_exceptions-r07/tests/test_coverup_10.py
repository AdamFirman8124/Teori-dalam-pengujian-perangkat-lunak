# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest

from isort.exceptions import FileSkipped, ISortError


def test_file_skipped_initialization():
    """Test that FileSkipped stores both the message and the file_path.

    This covers lines 50-51 in isort/exceptions.py:
        super().__init__(message)
        self.file_path = file_path
    """
    message = "File was skipped for testing reasons"
    file_path = "/some/path/to/file.py"

    exception = FileSkipped(message, file_path)

    # Line 51: file_path must be stored as an attribute.
    assert exception.file_path == file_path

    # Line 50: the message must be passed to the base exception,
    # so it shows up in args/str representation.
    assert exception.args == (message,)
    assert message in str(exception)

    # Inheritance postconditions.
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)
