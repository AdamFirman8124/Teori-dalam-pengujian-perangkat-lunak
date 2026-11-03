# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

import pytest

from isort.exceptions import FileSkipComment, FileSkipped, ISortError


def test_file_skip_comment_message_and_attributes():
    """Instantiating FileSkipComment must execute the super().__init__ call
    (lines 58-59) and set up the exception correctly."""
    file_path = "/some/path/to/skipped_file.py"
    exc = FileSkipComment(file_path)

    # The formatted message passed to the parent constructor is preserved.
    assert str(exc) == f"{file_path} contains an file skip comment and was skipped."

    # FileSkipped.__init__ must have stored the file_path attribute.
    assert exc.file_path == file_path

    # Inheritance chain postconditions.
    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_file_skip_comment_can_be_raised_and_caught():
    """The exception should behave like a normal exception when raised."""
    file_path = "another_skipped.py"
    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment(file_path)

    assert exc_info.value.file_path == file_path
    assert str(exc_info.value) == (
        f"{file_path} contains an file skip comment and was skipped."
    )
