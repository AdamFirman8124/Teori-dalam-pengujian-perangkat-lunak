# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

import pytest

from sty.primitive import Register


def test_as_namedtuple_returns_namedtuple_with_dict_fields_and_values():
    reg = Register()
    reg.red = "1"
    reg.green = "2"
    reg.blue = "3"

    result = reg.as_namedtuple()

    # Postcondition: it is a tuple (namedtuple) named "StyleRegister"
    assert isinstance(result, tuple)
    assert type(result).__name__ == "StyleRegister"
    assert hasattr(result, "_fields")
    assert hasattr(result, "_asdict")

    # Postcondition: fields and values match as_dict()
    d = reg.as_dict()
    assert d == {"blue": "3", "green": "2", "red": "1"}
    assert result._fields == tuple(d.keys())
    assert tuple(result) == tuple(d.values())
    assert result._asdict() == d

    # Postcondition: attribute access works for each field
    for key, value in d.items():
        assert getattr(result, key) == value
    assert result.red == "1"
    assert result.green == "2"
    assert result.blue == "3"


def test_as_namedtuple_empty_register():
    reg = Register()

    result = reg.as_namedtuple()

    assert isinstance(result, tuple)
    assert type(result).__name__ == "StyleRegister"
    assert result._fields == ()
    assert tuple(result) == ()
    assert result._asdict() == {}
    assert reg.as_dict() == {}


def test_as_namedtuple_does_not_mutate_register():
    reg = Register()
    reg.red = "1"
    reg.green = "2"

    first = reg.as_namedtuple()
    second = reg.as_namedtuple()

    assert first == second
    assert first._fields == second._fields
    assert reg.red == "1"
    assert reg.green == "2"
    assert reg.is_muted is False
    assert reg.renderfuncs == {}
