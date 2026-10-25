# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_register_copy_creates_independent_deepcopy():
    register = Register()
    object.__setattr__(register, "payload", {"values": [1, 2, 3]})

    copied = register.copy()

    assert isinstance(copied, Register)
    assert copied is not register
    assert copied.payload == register.payload
    assert copied.payload is not register.payload
    assert copied.payload["values"] is not register.payload["values"]

    copied.payload["values"].append(4)

    assert copied.payload["values"] == [1, 2, 3, 4]
    assert register.payload["values"] == [1, 2, 3]
