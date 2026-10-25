# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

import pytest

from isort.exceptions import ISortError, MissingSection


def test_missing_section_init_message():
    import_module = "mymodule"
    section = "CUSTOM"
    exc = MissingSection(import_module, section)
    expected = (
        f"Found {import_module} import while parsing, but {section} was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert str(exc) == expected
    assert exc.args[0] == expected
    assert f"Found {import_module} import while parsing" in str(exc)
    assert f"but {section} was not included" in str(exc)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_missing_section_can_be_raised_and_caught():
    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection("os", "MYSECTION")
    assert "Found os import while parsing" in str(exc_info.value)
    assert "MYSECTION was not included" in str(exc_info.value)
    assert "in the `sections` setting of your config" in str(exc_info.value)
    assert "https://pycqa.github.io/isort/#custom-sections-and-ordering" in str(exc_info.value)


def test_missing_section_caught_as_isort_error():
    with pytest.raises(ISortError):
        raise MissingSection("requests", "THIRDPARTY_CUSTOM")
