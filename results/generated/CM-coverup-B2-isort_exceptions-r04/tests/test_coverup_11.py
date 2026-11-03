# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

import pytest

from isort.exceptions import FileSkipComment, FileSkipped, ISortError


def test_file_skip_comment_message_and_attributes():
    """Instantiating FileSkipComment must exercise the super().__init__ call
    (lines 58-59) and produce the expected message and file_path attribute."""
    file_path = "some/module.py"

    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment(file_path)

    exc = exc_info.value

    # The exception was raised and is part of the expected hierarchy.
    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)

    # Postcondition of FileSkipped.__init__: message stored via Exception
    # and file_path attribute set.
    assert exc.file_path == file_path
    assert str(exc) == f"{file_path} contains an file skip comment and was skipped."
    assert exc.args == (f"{file_path} contains an file skip comment and was skipped.",)
