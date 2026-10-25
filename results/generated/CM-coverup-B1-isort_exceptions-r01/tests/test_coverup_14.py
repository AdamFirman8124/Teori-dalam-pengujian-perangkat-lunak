# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

import pytest

from isort.exceptions import ISortError, MissingSection


def test_missing_section_message_and_args():
    exc = MissingSection("django", "DJANGO")

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.args == (
        "Found django import while parsing, but DJANGO was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info.",
    )
    assert str(exc) == exc.args[0]
    assert "django" in str(exc)
    assert "DJANGO" in str(exc)
    assert "`sections`" in str(exc)
    assert str(exc).endswith("for more info.")


def test_missing_section_can_be_raised_and_caught_as_isort_error():
    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection("numpy", "THIRDPARTY")

    caught = exc_info.value
    assert isinstance(caught, ISortError)
    assert caught.args[0].startswith("Found numpy import while parsing, but THIRDPARTY")
    assert "was not included in the `sections` setting" in caught.args[0]
