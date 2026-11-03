# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

import pytest

from isort.exceptions import ISortError, IntroducedSyntaxErrors


def test_introduced_syntax_errors_message_and_attributes():
    file_path = "/path/to/some/file.py"
    error = IntroducedSyntaxErrors(file_path)

    # The exception should be an ISortError (and thus an Exception)
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # The message should mention the file path
    assert file_path in str(error)
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        f"contained within {file_path}."
    )

    # The file_path attribute should be stored
    assert error.file_path == file_path
