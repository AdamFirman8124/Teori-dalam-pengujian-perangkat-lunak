# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

import pytest

from isort.exceptions import IntroducedSyntaxErrors, ISortError


def test_introduced_syntax_errors_message_and_attributes():
    file_path = "some/path/to/file.py"
    error = IntroducedSyntaxErrors(file_path)

    # Lines 39-43: __init__ calls super().__init__ and sets file_path
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        f"contained within {file_path}."
    )
