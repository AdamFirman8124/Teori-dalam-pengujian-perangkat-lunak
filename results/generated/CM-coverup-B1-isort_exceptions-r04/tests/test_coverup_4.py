# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_errors_initialization() -> None:
    file_path = "src/example.py"

    error = ExistingSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        "src/example.py."
    )
    assert error.args == (
        "isort was told to sort imports within code that contains syntax errors: "
        "src/example.py.",
    )
