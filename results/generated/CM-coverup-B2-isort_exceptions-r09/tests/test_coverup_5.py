# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

from isort.exceptions import IntroducedSyntaxErrors


def test_introduced_syntax_errors_message_and_attribute():
    file_path = "/tmp/some_file.py"
    exc = IntroducedSyntaxErrors(file_path)

    assert exc.file_path == file_path
    assert str(exc) == (
        "isort introduced syntax errors when attempting to sort the imports "
        "contained within /tmp/some_file.py."
    )
    assert isinstance(exc, Exception)
