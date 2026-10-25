# file: project/sty/primitive.py:195-200
# asked: {"lines": [199, 200], "branches": []}
# gained: {"lines": [199, 200], "branches": []}

from sty.primitive import Register


def test_register_as_namedtuple_exports_string_attributes():
    register = Register()
    register.alpha = "first"
    register.beta = "second"

    result = register.as_namedtuple()

    assert type(result).__name__ == "StyleRegister"
    assert result._fields == ("alpha", "beta")
    assert result.alpha == "first"
    assert result.beta == "second"
    assert result._asdict() == {"alpha": "first", "beta": "second"}
