# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

from sty.primitive import Register


def test_as_dict_includes_only_public_string_attributes():
    register = Register()
    object.__setattr__(register, "visible", "shown")
    object.__setattr__(register, "_hidden", "secret")
    object.__setattr__(register, "non_string", 42)

    state_before = vars(register).copy()

    result = register.as_dict()

    assert result == {"visible": "shown"}
    assert vars(register) == state_before
