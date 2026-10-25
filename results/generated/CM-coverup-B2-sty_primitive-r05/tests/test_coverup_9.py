# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_register_copy_creates_independent_deepcopy():
    register = Register()
    register.renderfuncs["custom"] = {"values": [1, 2, 3]}

    copied = register.copy()

    assert isinstance(copied, Register)
    assert copied is not register
    assert copied.renderfuncs == register.renderfuncs
    assert copied.renderfuncs is not register.renderfuncs
    assert copied.renderfuncs["custom"] is not register.renderfuncs["custom"]
    assert (
        copied.renderfuncs["custom"]["values"]
        is not register.renderfuncs["custom"]["values"]
    )

    copied.renderfuncs["custom"]["values"].append(4)

    assert register.renderfuncs["custom"]["values"] == [1, 2, 3]
    assert copied.renderfuncs["custom"]["values"] == [1, 2, 3, 4]
