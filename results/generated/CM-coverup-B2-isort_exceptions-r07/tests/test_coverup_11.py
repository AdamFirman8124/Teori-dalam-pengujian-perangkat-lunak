# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

import pytest

from isort.exceptions import FileSkipComment, FileSkipped, ISortError


def test_file_skip_comment_initialization():
    """Test that FileSkipComment correctly initializes its message and file_path.

    This covers lines 58-59 in isort/exceptions.py, where the super().__init__
    call formats the message and passes file_path to FileSkipped.
    """
    file_path = "/tmp/some_skipped_file.py"

    exception = FileSkipComment(file_path)

    # Verify inheritance chain
    assert isinstance(exception, FileSkipComment)
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)

    # Verify the file_path attribute was set via FileSkipped.__init__
    assert exception.file_path == file_path

    # Verify the message was formatted correctly and passed to the base exception
    assert str(exception) == (
        f"{file_path} contains an file skip comment and was skipped."
    )
