# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

from isort.exceptions import IntroducedSyntaxErrors


def test_introduced_syntax_errors() -> None:
    file_path = "path/to/example.py"

    error = IntroducedSyntaxErrors(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        f"contained within {file_path}."
    )
    assert error.args == (str(error),)
