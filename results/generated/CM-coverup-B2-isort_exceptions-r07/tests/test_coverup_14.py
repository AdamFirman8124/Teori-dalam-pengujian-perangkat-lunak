# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

import pytest

from isort.exceptions import ISortError, MissingSection


def test_missing_section_initializes_message():
    """Executing MissingSection.__init__ (lines 175-176) builds the full error message."""
    import_module = "os"
    section = "MY_CUSTOM_SECTION"

    error = MissingSection(import_module, section)

    # Postcondition: it is an ISortError (and therefore an Exception).
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Postcondition: the message produced on lines 175-176 contains the
    # interpolated module name, section name, guidance text, and doc link.
    message = str(error)
    assert f"Found {import_module} import while parsing" in message
    assert f"{section} was not included" in message
    assert "in the `sections` setting of your config" in message
    assert "Please add it before continuing" in message
    assert "https://pycqa.github.io/isort/#custom-sections-and-ordering" in message
    assert "for more info." in message


def test_missing_section_raises_when_raised():
    """Raising the exception also exercises __init__ and preserves the message."""
    import_module = "my_module"
    section = "FIRSTPARTY"

    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection(import_module, section)

    message = str(exc_info.value)
    assert import_module in message
    assert section in message
    assert isinstance(exc_info.value, ISortError)
