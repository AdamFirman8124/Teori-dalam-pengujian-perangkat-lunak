# file: project/pymonet/either.py:14-15
# asked: {"lines": [15], "branches": []}
# gained: {"lines": [15], "branches": []}

from pymonet.either import Either


def test_either_stores_constructor_value():
    value = object()

    either = Either(value)

    assert either.value is value
