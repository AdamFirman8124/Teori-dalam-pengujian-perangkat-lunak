# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

import pytest

from isort.exceptions import ExistingSyntaxErrors


def test_existing_syntax_error_message_and_attribute():
    file_path = "example.py"
    with pytest.raises(ExistingSyntaxErrors) as excinfo:
        raise ExistingSyntaxErrors(file_path)

    exception = excinfo.value
    assert exception.file_path == file_path
    assert str(exception) == (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
