# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

from isort.exceptions import IntroducedSyntaxErrors, ISortError


def test_introduced_syntax_errors_init_sets_message_and_file_path():
    file_path = "/path/to/example.py"
    exc = IntroducedSyntaxErrors(file_path)
    expected_message = (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )
    assert exc.file_path == file_path
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_introduced_syntax_errors_can_be_raised_and_caught():
    file_path = "my_module.py"
    expected_message = (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )
    with __import__("pytest").raises(IntroducedSyntaxErrors) as exc_info:
        raise IntroducedSyntaxErrors(file_path)
    assert exc_info.value.file_path == file_path
    assert str(exc_info.value) == expected_message
