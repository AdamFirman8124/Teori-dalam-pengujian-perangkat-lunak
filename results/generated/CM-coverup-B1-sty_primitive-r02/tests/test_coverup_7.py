# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

from sty.primitive import Register


def test_register_as_namedtuple_exports_string_attributes():
    register = Register()
    register.primary = "red"
    register.secondary = "blue"

    result = register.as_namedtuple()

    assert type(result).__name__ == "StyleRegister"
    assert result._fields == ("primary", "secondary")
    assert result.primary == "red"
    assert result.secondary == "blue"
    assert result._asdict() == {
        "primary": "red",
        "secondary": "blue",
    }
