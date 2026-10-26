# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_errors_initializes_message_and_file_path():
    file_path = "src/example.py"

    error = ExistingSyntaxErrors(file_path)

    expected_message = (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert error.args == (expected_message,)
    assert str(error) == expected_message
