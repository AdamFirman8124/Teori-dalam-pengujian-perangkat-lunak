# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

from isort.exceptions import ISortError, IntroducedSyntaxErrors


def test_introduced_syntax_errors_initialization() -> None:
    file_path = "src/example.py"

    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        "contained within src/example.py."
    )
