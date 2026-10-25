# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_register_copy_returns_independent_deepcopy():
    register = Register()
    register.renderfuncs["test"] = ["original"]

    copied_register = register.copy()

    assert copied_register is not register
    assert copied_register.renderfuncs == register.renderfuncs
    assert copied_register.renderfuncs is not register.renderfuncs
    assert copied_register.renderfuncs["test"] is not register.renderfuncs["test"]

    copied_register.renderfuncs["test"].append("copied")

    assert register.renderfuncs["test"] == ["original"]
    assert copied_register.renderfuncs["test"] == ["original", "copied"]
