# file: project/pymonet/either.py:14-15
# asked: {"lines": [15], "branches": []}
# gained: {"lines": [15], "branches": []}

from pymonet.either import Either, Left, Right


def test_either_init_sets_value():
    either = Either(42)
    assert either.value == 42


def test_either_init_stores_none_value():
    either = Either(None)
    assert either.value is None


def test_either_init_stores_mutable_value_by_reference():
    payload = {'a': 1}
    either = Either(payload)
    assert either.value is payload
    payload['b'] = 2
    assert either.value == {'a': 1, 'b': 2}


def test_either_init_value_used_by_case():
    either = Either('boom')
    assert either.case(lambda v: 'error:' + v, lambda v: 'success:' + v) == 'error:boom'


def test_left_inherits_value_from_either_init():
    left = Left('err')
    assert left.value == 'err'
    assert left.is_left() is True
    assert left.is_right() is False


def test_right_inherits_value_from_either_init():
    right = Right(7)
    assert right.value == 7
    assert right.is_right() is True
    assert right.is_left() is False


def test_subclass_super_init_sets_value():
    class Custom(Either):
        def __init__(self, value):
            super().__init__(value)

    custom = Custom('x')
    assert custom.value == 'x'
    assert isinstance(custom, Either)
