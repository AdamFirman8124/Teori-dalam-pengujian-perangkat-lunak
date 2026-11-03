# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

import pytest

from isort.exceptions import FileSkipped, FileSkipSetting, ISortError


def test_file_skip_setting_message_and_attributes():
    file_path = "test_file.py"
    exception = FileSkipSetting(file_path=file_path)

    # Lines 67-70: super().__init__ call is executed on instantiation.
    assert isinstance(exception, FileSkipSetting)
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)

    # Verify postconditions: message and file_path are set correctly.
    assert exception.file_path == file_path
    assert str(exception) == (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

    # The exception should be raisable and catchable as expected.
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(file_path)
    assert exc_info.value.file_path == file_path
    assert file_path in str(exc_info.value)
