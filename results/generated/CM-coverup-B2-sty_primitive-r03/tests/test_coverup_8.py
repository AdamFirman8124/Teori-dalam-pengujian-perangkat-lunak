# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

from sty.primitive import Register


def test_register_as_namedtuple(monkeypatch):
    expected = {"red": "31", "green": "32"}
    monkeypatch.setattr(Register, "as_dict", lambda self: expected.copy())

    result = Register().as_namedtuple()

    assert result._fields == ("red", "green")
    assert result.red == "31"
    assert result.green == "32"
    assert dict(result._asdict()) == expected
