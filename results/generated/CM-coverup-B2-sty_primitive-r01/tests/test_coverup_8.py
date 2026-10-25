# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

from sty.primitive import Register


def test_as_namedtuple_returns_style_register(monkeypatch):
    expected = {"red": "R-VAL", "green": "G-VAL"}
    monkeypatch.setattr(Register, "as_dict", lambda self: dict(expected))

    reg = Register.__new__(Register)
    result = reg.as_namedtuple()

    assert type(result).__name__ == "StyleRegister"
    assert tuple(result._fields) == tuple(expected.keys())
    assert tuple(result) == tuple(expected.values())
    assert result.red == "R-VAL"
    assert result.green == "G-VAL"
    assert dict(result._asdict()) == expected


def test_as_namedtuple_empty_dict(monkeypatch):
    monkeypatch.setattr(Register, "as_dict", lambda self: {})

    reg = Register.__new__(Register)
    result = reg.as_namedtuple()

    assert type(result).__name__ == "StyleRegister"
    assert tuple(result._fields) == ()
    assert tuple(result) == ()
    assert dict(result._asdict()) == {}
