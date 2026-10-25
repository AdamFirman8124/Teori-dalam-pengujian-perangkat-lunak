# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

from sty.primitive import Register


def test_as_dict_includes_public_str_attr(monkeypatch):
    reg = Register()
    monkeypatch.setitem(reg.__dict__, "mycolor", "some-value")
    result = reg.as_dict()
    assert isinstance(result, dict)
    assert result["mycolor"] == "some-value"


def test_as_dict_excludes_private_and_non_str(monkeypatch):
    reg = Register()
    monkeypatch.setitem(reg.__dict__, "good", "yes")
    monkeypatch.setitem(reg.__dict__, "_hidden", "should-be-ignored")
    monkeypatch.setitem(reg.__dict__, "__dunder_like", "should-be-ignored")
    monkeypatch.setitem(reg.__dict__, "mynumber", 123)
    monkeypatch.setitem(reg.__dict__, "mynone", None)
    monkeypatch.setitem(reg.__dict__, "mydict", {"a": 1})

    result = reg.as_dict()

    assert result["good"] == "yes"
    assert "_hidden" not in result
    assert "__dunder_like" not in result
    assert "mynumber" not in result
    assert "mynone" not in result
    assert "mydict" not in result
    # default non-str / callable members must also be excluded
    assert "renderfuncs" not in result
    assert "is_muted" not in result
    assert "eightbit_call" not in result
    assert "rgb_call" not in result
    assert "mute" not in result
    assert "as_dict" not in result


def test_as_dict_empty_when_no_public_str(monkeypatch):
    reg = Register()
    # ensure no public str attrs remain (remove if any were added by other setup)
    for key in list(reg.__dict__.keys()):
        if not key.startswith("_") and isinstance(reg.__dict__[key], str):
            monkeypatch.delitem(reg.__dict__, key, raising=False)
    result = reg.as_dict()
    assert result == {}


def test_as_dict_converts_str_subclass_to_plain_str(monkeypatch):
    class MyStr(str):
        pass

    reg = Register()
    monkeypatch.setitem(reg.__dict__, "sub", MyStr("hi"))
    result = reg.as_dict()
    assert result["sub"] == "hi"
    assert type(result["sub"]) is str
