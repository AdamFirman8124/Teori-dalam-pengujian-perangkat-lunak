# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

from sty.primitive import Register


def test_as_dict_returns_only_public_string_attributes():
    register = Register()
    register.visible = "visible value"
    register.empty = ""
    register.number = 42
    register._hidden = "hidden value"

    result = register.as_dict()

    assert result == {
        "visible": "visible value",
        "empty": "",
    }
    assert "_hidden" not in result
    assert "number" not in result
