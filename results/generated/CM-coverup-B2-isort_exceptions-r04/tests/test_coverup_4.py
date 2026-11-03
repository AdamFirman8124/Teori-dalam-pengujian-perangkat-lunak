# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

import pytest

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_error_message_and_attributes():
    file_path = "/path/to/file_with_syntax_errors.py"
    error = ExistingSyntaxErrors(file_path)

    # The exception should be an instance of the base isort error and Exception.
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # The message passed to super().__init__ should be formatted correctly.
    expected_message = (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
    assert str(error) == expected_message

    # The file_path attribute should be stored on the instance.
    assert error.file_path == file_path
