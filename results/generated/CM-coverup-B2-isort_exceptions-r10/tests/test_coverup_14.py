# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

import pytest

from isort.exceptions import ISortError, MissingSection


def test_missing_section_message_and_inheritance():
    """Executing MissingSection.__init__ (lines 175-176) builds the full error message."""
    import_module = "foo.bar"
    section = "MY_CUSTOM_SECTION"

    error = MissingSection(import_module, section)

    # Postcondition: it is an isort error (and therefore an Exception).
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Postcondition: the message produced by super().__init__ matches exactly.
    expected_message = (
        f"Found {import_module} import while parsing, but {section} was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert str(error) == expected_message
    assert import_module in str(error)
    assert section in str(error)


def test_missing_section_raised_message():
    """Raising MissingSection exercises the same __init__ lines and preserves the message."""
    import_module = "os.path"
    section = "FIRSTPARTY"

    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection(import_module, section)

    assert str(exc_info.value) == (
        f"Found {import_module} import while parsing, but {section} was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
