# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

from isort.exceptions import ISortError, MissingSection


def test_missing_section_error_message() -> None:
    error = MissingSection("example.module", "CUSTOM_SECTION")

    assert isinstance(error, ISortError)
    assert str(error) == (
        "Found example.module import while parsing, but CUSTOM_SECTION was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."
    )
    assert error.args == (str(error),)
