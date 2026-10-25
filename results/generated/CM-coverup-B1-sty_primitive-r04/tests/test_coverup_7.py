# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

from collections import namedtuple

from sty.primitive import Register


class _DummyRegister(Register):
    """Minimal concrete Register for testing as_namedtuple in isolation."""

    def __init__(self):
        super().__init__()
        self.red = "1"
        self.green = "2"
        self.blue = "3"

    def as_dict(self):
        return {"red": self.red, "green": self.green, "blue": self.blue}


def test_as_namedtuple_returns_namedtuple_with_dict_fields_and_values():
    reg = _DummyRegister()
    result = reg.as_namedtuple()

    # Postcondition: it is a namedtuple named "StyleRegister"
    assert isinstance(result, tuple)
    assert type(result).__name__ == "StyleRegister"
    assert hasattr(result, "_fields")
    assert hasattr(result, "_asdict")

    # Postcondition: fields and values match as_dict()
    d = reg.as_dict()
    assert result._fields == tuple(d.keys())
    assert tuple(result) == tuple(d.values())
    assert result._asdict() == d

    # Postcondition: attribute access works
    assert result.red == "1"
    assert result.green == "2"
    assert result.blue == "3"
    assert result.red == d["red"]
    assert result.green == d["green"]
    assert result.blue == d["blue"]


def test_as_namedtuple_does_not_pollute_global_state():
    # The namedtuple factory creates a new class each call; ensure calling
    # it repeatedly works and does not mutate the register instance.
    reg = _DummyRegister()
    first = reg.as_namedtuple()
    second = reg.as_namedtuple()

    assert first == second
    assert first._fields == second._fields
    assert reg.red == "1"
    assert reg.green == "2"
    assert reg.blue == "3"
    assert reg.is_muted is False
    assert reg.renderfuncs == {}
