# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

import pytest

from isort.exceptions import ISortError, MissingSection


@pytest.mark.parametrize(
    ("import_module", "section"),
    [
        ("os", "THIRDPARTY"),
        ("my_custom_module", "MY_CUSTOM_SECTION"),
    ],
)
def test_missing_section_message(import_module: str, section: str) -> None:
    """Instantiating MissingSection must execute the super().__init__ call (lines 175-176)
    and produce the fully formatted error message."""
    exception = MissingSection(import_module, section)

    # Postcondition: it is both a plain Exception and the isort base error type.
    assert isinstance(exception, Exception)
    assert isinstance(exception, ISortError)

    expected_message = (
        f"Found {import_module} import while parsing, but {section} was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert str(exception) == expected_message


def test_missing_section_can_be_raised_and_caught() -> None:
    """MissingSection must be raisable and catchable as an ISortError, with the
    formatted message (built on lines 175-176) available on the caught exception."""
    with pytest.raises(ISortError) as exc_info:
        raise MissingSection("some_module", "SOME_SECTION")

    message = str(exc_info.value)
    assert message == (
        "Found some_module import while parsing, but SOME_SECTION was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
