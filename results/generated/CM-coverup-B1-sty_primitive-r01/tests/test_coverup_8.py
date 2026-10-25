# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

from sty.primitive import Register


def test_register_as_namedtuple(monkeypatch):
    expected = {"red": "\x1b[31m", "bold": "\x1b[1m"}
    monkeypatch.setattr(Register, "as_dict", lambda self: expected.copy())

    result = Register().as_namedtuple()

    assert type(result).__name__ == "StyleRegister"
    assert result._fields == ("red", "bold")
    assert result.red == "\x1b[31m"
    assert result.bold == "\x1b[1m"
    assert result._asdict() == expected
