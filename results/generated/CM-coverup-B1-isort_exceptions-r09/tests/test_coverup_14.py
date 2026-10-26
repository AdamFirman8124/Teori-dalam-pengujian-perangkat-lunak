# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

from isort.exceptions import ISortError, MissingSection


def test_missing_section_initializes_with_expected_message():
    error = MissingSection("example_module", "custom")

    expected_message = (
        "Found example_module import while parsing, but custom was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

    assert isinstance(error, ISortError)
    assert str(error) == expected_message
    assert error.args == (expected_message,)
