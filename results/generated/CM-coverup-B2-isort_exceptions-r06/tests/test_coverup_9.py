# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

import pytest

from isort.exceptions import FileSkipSetting


def test_file_skip_setting_message_and_file_path():
    file_path = "some/dir/skipped_file.py"
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(file_path)

    assert exc_info.value.file_path == file_path
    assert str(exc_info.value) == (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
