# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

import pytest
from isort.exceptions import IntroducedSyntaxErrors


def test_introduced_syntax_errors_message_and_file_path():
    file_path = "my_module.py"
    err = IntroducedSyntaxErrors(file_path)
    assert err.file_path == file_path
    assert str(err) == (
        "isort introduced syntax errors when attempting to sort the imports "
        f"contained within {file_path}."
    )
    assert err.args[0] == str(err)
    assert isinstance(err, Exception)


def test_introduced_syntax_errors_can_be_raised_and_caught():
    file_path = "/path/to/file.py"
    with pytest.raises(IntroducedSyntaxErrors) as exc_info:
        raise IntroducedSyntaxErrors(file_path)
    assert exc_info.value.file_path == file_path
    assert file_path in str(exc_info.value)
    assert exc_info.value.args[0] == (
        "isort introduced syntax errors when attempting to sort the imports "
        f"contained within {file_path}."
    )
