# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

import pytest
from collections import namedtuple

from sty import Register


class _TestRegister(Register):
    red = "\x1b[31m"
    green = "\x1b[32m"


def test_as_namedtuple() -> None:
    reg = _TestRegister()

    result = reg.as_namedtuple()

    # Postcondition: result is a tuple (namedtuples are tuple subclasses)
    assert isinstance(result, tuple)

    # Postcondition: it is an instance of a namedtuple type named "StyleRegister"
    assert type(result).__name__ == "StyleRegister"
    assert hasattr(type(result), "_fields")

    # Postcondition: fields match the public string attributes of the register
    # (as_dict iterates dir(self), which yields names in alphabetical order)
    assert result._fields == ("green", "red")

    # Postcondition: values match the register's attribute values
    assert result.red == "\x1b[31m"
    assert result.green == "\x1b[32m"

    # Postcondition: consistent with as_dict()
    d = reg.as_dict()
    assert result._asdict() == d
