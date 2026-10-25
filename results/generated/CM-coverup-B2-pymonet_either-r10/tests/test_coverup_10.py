# file: project/pymonet/either.py:14-15
# asked: {"lines": [15], "branches": []}
# gained: {"lines": [15], "branches": []}

from pymonet.either import Either


def test_either_init_stores_int_value():
    instance = Either(42)
    assert instance.value == 42


def test_either_init_stores_various_values():
    assert Either(None).value is None
    assert Either("hello").value == "hello"
    obj = object()
    assert Either(obj).value is obj


def test_either_init_assigns_instance_attribute():
    instance = Either([1, 2, 3])
    assert "value" in instance.__dict__
    assert instance.__dict__["value"] == [1, 2, 3]
