# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_register_copy_returns_independent_deepcopy():
    register = Register()
    register.metadata = {"colors": ["red", "green"]}

    copied = register.copy()

    assert isinstance(copied, Register)
    assert copied is not register
    assert copied.renderfuncs == register.renderfuncs
    assert copied.renderfuncs is not register.renderfuncs
    assert copied.metadata == register.metadata
    assert copied.metadata is not register.metadata
    assert copied.metadata["colors"] is not register.metadata["colors"]

    copied.metadata["colors"].append("blue")

    assert copied.metadata["colors"] == ["red", "green", "blue"]
    assert register.metadata["colors"] == ["red", "green"]
