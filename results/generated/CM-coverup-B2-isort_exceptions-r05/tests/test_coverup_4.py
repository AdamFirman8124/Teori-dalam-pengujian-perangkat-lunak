# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

import pytest

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_error_message_and_attributes():
    file_path = "/path/to/file_with_syntax_errors.py"
    error = ExistingSyntaxErrors(file_path)

    # Verify the exception is an instance of the base isort error class
    assert isinstance(error, ISortError)

    # Verify the file_path attribute is set correctly (line 32)
    assert error.file_path == file_path

    # Verify the exception message includes the file path (lines 28-31)
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
    assert file_path in str(error)


def test_existing_syntax_error_is_raisable_and_catchable():
    file_path = "another_file.py"

    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)

    assert exc_info.value.file_path == file_path
    assert file_path in str(exc_info.value)
