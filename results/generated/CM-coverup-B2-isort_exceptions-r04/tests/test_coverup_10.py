# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest

from isort.exceptions import FileSkipped, ISortError


def test_file_skipped_initialization():
    """Ensure FileSkipped.__init__ runs (lines 50-51) and stores its arguments."""
    message = "Skipped file due to configuration"
    file_path = "/path/to/skipped_file.py"

    exception = FileSkipped(message, file_path)

    # Line 50: super().__init__(message) -> Exception message is set
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)
    assert str(exception) == message
    assert exception.args == (message,)

    # Line 51: self.file_path = file_path -> attribute is stored
    assert exception.file_path == file_path
