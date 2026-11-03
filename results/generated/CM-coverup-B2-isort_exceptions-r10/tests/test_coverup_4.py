# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

import pytest

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_error_message_and_attributes():
    file_path = "/path/to/file_with_syntax_errors.py"
    error = ExistingSyntaxErrors(file_path)

    # Verify the exception is properly initialized (covers lines 28-32)
    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_existing_syntax_error_raised():
    file_path = "another_file.py"
    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)

    assert exc_info.value.file_path == file_path
    assert file_path in str(exc_info.value)
