# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

from isort.exceptions import ISortError, MissingSection


def test_missing_section_initializes_with_descriptive_error_message():
    import_module = "requests"
    section = "third_party"
    expected_message = (
        "Found requests import while parsing, but third_party was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

    error = MissingSection(import_module, section)

    assert isinstance(error, ISortError)
    assert error.args == (expected_message,)
    assert str(error) == expected_message
