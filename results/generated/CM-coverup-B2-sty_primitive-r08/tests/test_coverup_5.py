# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

from sty.primitive import Register


def test_as_dict_empty_register_returns_dict():
    reg = Register()
    result = reg.as_dict()
    assert isinstance(result, dict)
    assert result == {}
    # methods / non-string attrs must not leak into dict
    assert "as_dict" not in result
    assert "renderfuncs" not in result
    assert "is_muted" not in result


def test_as_dict_includes_plain_string_attribute():
    reg = Register()
    reg.my_color = "hello-value"
    result = reg.as_dict()
    assert result["my_color"] == "hello-value"
    assert result.get("my_color") == str(getattr(reg, "my_color"))
    assert isinstance(result, dict)


def test_as_dict_excludes_private_and_non_string_attributes():
    reg = Register()
    reg.visible = "shown"
    reg._hidden = "should-be-hidden"
    reg.count = 123
    reg.flag = True
    result = reg.as_dict()
    # true-branch of isinstance check
    assert result["visible"] == "shown"
    # False-branch: name.startswith("_") is True
    assert "_hidden" not in result
    assert not any(k.startswith("_") for k in result)
    # False-branch: not isinstance(value, str)
    assert "count" not in result
    assert "flag" not in result
    assert "renderfuncs" not in result
    assert "is_muted" not in result
    assert "eightbit_call" not in result
    assert "rgb_call" not in result
    # all values in dict are strings
    assert all(isinstance(v, str) for v in result.values())
