# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

from sty.primitive import Register


def test_as_dict_returns_only_public_string_attributes(monkeypatch):
    reg = Register()
    monkeypatch.setattr(reg, "red", "38;5;9", raising=False)
    monkeypatch.setattr(reg, "bold", "1", raising=False)
    monkeypatch.setattr(reg, "_private", "hidden", raising=False)
    monkeypatch.setattr(reg, "count", 42, raising=False)
    monkeypatch.setattr(reg, "some_list", ["a", "b"], raising=False)
    monkeypatch.setattr(reg, "nothing", None, raising=False)

    result = reg.as_dict()

    assert isinstance(result, dict)
    assert result == {"red": "38;5;9", "bold": "1"}
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in result.items())
    assert "_private" not in result
    assert "count" not in result
    assert "some_list" not in result
    assert "nothing" not in result
    # dir() is sorted, so exported keys come out sorted
    assert list(result) == sorted(result)
    # values are str()-coerced copies of the attributes
    assert result["red"] == str(reg.red)
    assert result["bold"] == str(reg.bold)


def test_as_dict_empty_when_no_public_string_attributes():
    reg = Register()

    result = reg.as_dict()

    assert result == {}
    assert isinstance(result, dict)


def test_as_dict_returns_independent_dict(monkeypatch):
    reg = Register()
    monkeypatch.setattr(reg, "blue", "34", raising=False)

    first = reg.as_dict()
    first["blue"] = "changed"
    first["injected"] = "x"

    assert reg.blue == "34"
    assert reg.as_dict() == {"blue": "34"}
    assert first is not reg.as_dict()
