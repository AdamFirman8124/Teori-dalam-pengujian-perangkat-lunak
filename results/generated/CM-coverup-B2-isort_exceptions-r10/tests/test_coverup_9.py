# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

"""Tests for isort.exceptions.FileSkipSetting (covers lines 67-70)."""

import pytest

from isort.exceptions import FileSkipSetting, FileSkipped, ISortError


def test_file_skip_setting_initialization_covers_init_lines():
    """Instantiating FileSkipSetting executes FileSkipSetting.__init__ (lines 67-70)."""
    file_path = "/tmp/skipped_module.py"

    exception = FileSkipSetting(file_path)

    # Postconditions: exception type hierarchy is intact.
    assert isinstance(exception, FileSkipSetting)
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # The message passed to super().__init__ is stored and formatted correctly.
    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert str(exception) == expected_message

    # The file_path keyword argument forwarded to FileSkipped.__init__ is stored.
    assert exception.file_path == file_path


def test_file_skip_setting_when_raised():
    """Raising FileSkipSetting propagates the message and file_path attributes."""
    file_path = "another/skipped_file.py"

    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(file_path)

    assert exc_info.value.file_path == file_path
    assert str(exc_info.value) == (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    # The exception is also catchable via its base classes.
    with pytest.raises(FileSkipped):
        raise FileSkipSetting(file_path)
