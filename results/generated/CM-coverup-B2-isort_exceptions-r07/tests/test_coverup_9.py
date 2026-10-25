# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

from isort.exceptions import FileSkipped, FileSkipSetting


def test_file_skip_setting_initializes_message_and_file_path():
    file_path = "project/generated.py"
    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting "
        "or matches a glob in 'skip_glob' setting"
    )

    exception = FileSkipSetting(file_path)

    assert isinstance(exception, FileSkipped)
    assert exception.file_path == file_path
    assert str(exception) == expected_message
    assert exception.args == (expected_message,)
