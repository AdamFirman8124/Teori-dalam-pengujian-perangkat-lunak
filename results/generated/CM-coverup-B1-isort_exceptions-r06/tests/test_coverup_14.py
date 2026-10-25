# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

import pytest

from isort.exceptions import ISortError, MissingSection


def test_missing_section_error_message() -> None:
    expected_message = (
        "Found example_module import while parsing, but CUSTOM was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection("example_module", "CUSTOM")

    assert isinstance(exc_info.value, ISortError)
    assert str(exc_info.value) == expected_message
    assert exc_info.value.args == (expected_message,)
