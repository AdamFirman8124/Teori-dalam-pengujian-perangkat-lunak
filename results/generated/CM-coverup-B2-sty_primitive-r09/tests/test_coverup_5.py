# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

from sty.primitive import Register


def test_as_dict_exports_public_string_attributes():
    register = Register()
    register.visible = "value"

    assert register.as_dict() == {"visible": "value"}


def test_as_dict_excludes_private_and_non_string_attributes():
    register = Register()
    register._private = "hidden"
    register.number = 42
    register.data = {"key": "value"}

    result = register.as_dict()

    assert result == {}
    assert "_private" not in result
    assert "number" not in result
    assert "data" not in result
