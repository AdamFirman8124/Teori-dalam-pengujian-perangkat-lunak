# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

import pytest

from isort.exceptions import FileSkipSetting, FileSkipped


def test_file_skip_setting_message_and_file_path():
    """Constructing FileSkipSetting should execute its __init__ (lines 67-70),
    producing the expected message and file_path attribute."""
    file_path = "some/module.py"
    exception = FileSkipSetting(file_path)

    # The exception is a FileSkipped (and thus an ISortError / Exception).
    assert isinstance(exception, FileSkipped)

    # Verify the message built in __init__ (lines 67-68).
    assert str(exception) == (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

    # Verify the file_path keyword argument passed on line 70.
    assert exception.file_path == file_path


def test_file_skip_setting_is_subclass_of_file_skipped():
    """FileSkipSetting should inherit from FileSkipped and propagate attributes."""
    assert issubclass(FileSkipSetting, FileSkipped)

    file_path = "another/file.py"
    exception = FileSkipSetting(file_path)

    assert exception.file_path == file_path
    assert file_path in str(exception)
    assert "skip" in str(exception)
    assert "skip_glob" in str(exception)
