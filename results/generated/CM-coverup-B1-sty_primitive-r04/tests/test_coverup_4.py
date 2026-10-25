# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

from sty.primitive import Register


def test_as_dict_empty_register_returns_empty_dict():
    reg = Register()
    result = reg.as_dict()
    assert isinstance(result, dict)
    assert result == {}


def test_as_dict_includes_public_string_attributes():
    reg = Register()
    reg.custom_red = "custom-red-value"
    reg.custom_blue = "custom-blue-value"

    result = reg.as_dict()

    assert isinstance(result, dict)
    assert result["custom_red"] == "custom-red-value"
    assert result["custom_blue"] == "custom-blue-value"
    assert result == {"custom_red": "custom-red-value", "custom_blue": "custom-blue-value"}


def test_as_dict_excludes_private_and_non_string_attributes():
    reg = Register()
    reg.visible = "visible-value"
    reg._hidden = "secret-value"
    reg.count = 123
    reg.nothing = None
    reg.mapping = {"a": 1}

    result = reg.as_dict()

    assert isinstance(result, dict)
    assert result == {"visible": "visible-value"}
    assert "visible" in result
    assert "_hidden" not in result
    assert "count" not in result
    assert "nothing" not in result
    assert "mapping" not in result
    # dunder / private names are never leaked
    assert all(not k.startswith("_") for k in result)
    # all exported values are strings
    assert all(isinstance(v, str) for v in result.values())
