# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest

from isort.exceptions import FileSkipped, ISortError


def test_file_skipped_sets_message_and_file_path():
    exc = FileSkipped("Skipping file", "/tmp/example.py")

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.file_path == "/tmp/example.py"
    assert exc.args == ("Skipping file",)
    assert str(exc) == "Skipping file"


def test_file_skipped_can_be_raised_and_caught():
    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipped("Skipped: unsupported", "pkg/module.py")

    caught = exc_info.value
    assert caught.file_path == "pkg/module.py"
    assert str(caught) == "Skipped: unsupported"
    assert caught.args == ("Skipped: unsupported",)


def test_file_skipped_caught_as_isort_error():
    with pytest.raises(ISortError) as exc_info:
        raise FileSkipped("Skipped: excluded", "a/b/c.py")

    assert exc_info.value.file_path == "a/b/c.py"


def test_file_skipped_attributes_are_independent_per_instance():
    first = FileSkipped("first", "one.py")
    second = FileSkipped("second", "two.py")

    assert first.file_path == "one.py"
    assert second.file_path == "two.py"
    assert first.args == ("first",)
    assert second.args == ("second",)
