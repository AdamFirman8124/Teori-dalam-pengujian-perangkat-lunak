# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

import pytest

from isort.exceptions import IntroducedSyntaxErrors


def test_introduced_syntax_errors_message_and_attributes():
    file_path = "/tmp/some_file.py"
    error = IntroducedSyntaxErrors(file_path)

    # The exception message must mention the file path.
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        f"contained within {file_path}."
    )
    # The file_path attribute must be stored on the instance.
    assert error.file_path == file_path
    # It must be an instance of the base isort exception and Exception.
    assert isinstance(error, Exception)
