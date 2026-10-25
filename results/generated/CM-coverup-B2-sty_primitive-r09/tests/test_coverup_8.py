# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

from sty.primitive import Register


def test_as_namedtuple_exports_register_data(monkeypatch):
    register = Register()
    expected = {"red": "\x1b[31m", "bold": "\x1b[1m"}
    calls = []

    def fake_as_dict(self):
        calls.append(self)
        return expected

    monkeypatch.setattr(Register, "as_dict", fake_as_dict)

    result = register.as_namedtuple()

    assert calls == [register]
    assert type(result).__name__ == "StyleRegister"
    assert result._fields == ("red", "bold")
    assert result.red == expected["red"]
    assert result.bold == expected["bold"]
    assert result._asdict() == expected
