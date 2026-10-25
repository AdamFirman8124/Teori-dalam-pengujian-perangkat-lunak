# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

import pytest

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_errors_message_and_file_path():
    file_path = "/tmp/example_module.py"
    error = ExistingSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
    assert error.args == (str(error),)


def test_existing_syntax_errors_is_raisable_and_catchable():
    file_path = "pkg/broken.py"

    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)

    caught = exc_info.value
    assert caught.file_path == file_path
    assert "pkg/broken.py." in str(caught)

    # Also catchable via the base class, as isort relies on.
    with pytest.raises(ISortError):
        raise ExistingSyntaxErrors(file_path)


def test_existing_syntax_errors_instances_are_independent():
    first = ExistingSyntaxErrors("a.py")
    second = ExistingSyntaxErrors("b.py")

    assert first.file_path == "a.py"
    assert second.file_path == "b.py"
    assert str(first) != str(second)
    assert first.args != second.args
