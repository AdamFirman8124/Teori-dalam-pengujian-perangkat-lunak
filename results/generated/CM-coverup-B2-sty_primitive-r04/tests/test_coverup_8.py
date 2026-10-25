# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_register_copy_returns_independent_deepcopy():
    register = Register()
    register.metadata = {"colors": ["red", "green"]}

    copied_register = register.copy()

    assert isinstance(copied_register, Register)
    assert copied_register is not register
    assert copied_register.metadata == register.metadata
    assert copied_register.metadata is not register.metadata
    assert copied_register.metadata["colors"] is not register.metadata["colors"]

    copied_register.metadata["colors"].append("blue")
    copied_register.mute()

    assert register.metadata == {"colors": ["red", "green"]}
    assert register.is_muted is False
    assert copied_register.metadata == {"colors": ["red", "green", "blue"]}
    assert copied_register.is_muted is True
