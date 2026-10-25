# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

import pytest

from isort.exceptions import FileSkipSetting


def test_file_skip_setting_message_and_file_path():
    file_path = "package/skipped.py"
    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(file_path)

    assert str(exc_info.value) == expected_message
    assert exc_info.value.args == (expected_message,)
    assert exc_info.value.file_path == file_path
