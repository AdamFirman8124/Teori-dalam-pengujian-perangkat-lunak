# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

import pytest

from isort.exceptions import FileSkipped, FileSkipSetting, ISortError


def test_file_skip_setting_message_and_file_path():
    file_path = "my_module.py"
    exc = FileSkipSetting(file_path)
    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert exc.file_path == file_path
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message


def test_file_skip_setting_inheritance():
    file_path = "some/dir/skipped.py"
    exc = FileSkipSetting(file_path)
    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_file_skip_setting_raised_and_caught_as_file_skipped():
    file_path = "skipped_file.py"
    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipSetting(file_path)
    assert exc_info.value.file_path == file_path
    assert str(exc_info.value) == expected_message
