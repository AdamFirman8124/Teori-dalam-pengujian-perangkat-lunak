# file: project/isort/exceptions.py:63-71
# asked: {"lines": [67, 68, 70], "branches": []}
# gained: {"lines": [67, 68, 70], "branches": []}

from isort.exceptions import FileSkipped, FileSkipSetting, ISortError


def test_file_skip_setting_init_sets_message_and_file_path():
    file_path = "example.py"
    exc = FileSkipSetting(file_path)
    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert exc.file_path == file_path
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message
    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_file_skip_setting_can_be_raised_and_caught_as_file_skipped():
    file_path = "some/dir/skipped_file.py"
    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    try:
        raise FileSkipSetting(file_path)
    except FileSkipped as caught:
        assert caught.file_path == file_path
        assert str(caught) == expected_message
        assert caught.args[0] == expected_message
    else:
        raise AssertionError("FileSkipSetting was not raised")
