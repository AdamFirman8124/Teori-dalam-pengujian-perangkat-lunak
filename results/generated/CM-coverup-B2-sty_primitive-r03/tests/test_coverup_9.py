# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_register_copy_returns_independent_deepcopy():
    register = Register()
    register.custom_data = {"colors": ["red", "green"]}

    copied_register = register.copy()

    assert copied_register is not register
    assert isinstance(copied_register, Register)
    assert copied_register.custom_data == register.custom_data
    assert copied_register.custom_data is not register.custom_data
    assert copied_register.custom_data["colors"] is not register.custom_data["colors"]

    copied_register.custom_data["colors"].append("blue")

    assert copied_register.custom_data["colors"] == ["red", "green", "blue"]
    assert register.custom_data["colors"] == ["red", "green"]
