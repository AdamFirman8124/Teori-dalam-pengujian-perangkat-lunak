

# Generated at 2026-11-02 15:37:52.735137
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    from pymonet.validation import Validation

    # to_validation should transform Left into a failed Validation
    assert Left(42).to_validation() == Validation.fail([42])
    assert Left('error').to_validation() == Validation.fail(['error'])

    # resulting Validation should hold value as a list of errors and no value
    validation = Left(42).to_validation()
    assert isinstance(validation, Validation)
    assert validation.value is None
    assert validation.errors == [42]
    assert validation.is_success() is False

    # falsy values should still be preserved in errors
    validation_falsy = Left(0).to_validation()
    assert validation_falsy.errors == [0]
    assert validation_falsy.value is None
    assert validation_falsy.is_success() is False

    # original Left instance should remain unchanged
    left = Left(42)
    left.to_validation()
    assert left.value == 42
    assert left.is_left() is True
    assert left.is_right() is False

# Generated at 2026-11-02 15:39:45.908804
# Unit test for method map of class Left
def test_Left_map():
    left = Left(42)

    result = left.map(lambda value: value + 1)

    # map on Left ignores the mapper and returns a new Left with the same value
    assert isinstance(result, Left)
    assert result.value == 42
    assert result == left
    assert result is not left
    assert result.is_left() is True
    assert result.is_right() is False

# Generated at 2026-11-02 15:42:39.348010
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    # Right.to_lazy returns Lazy monad wrapping the value
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # Left.to_lazy returns Lazy monad wrapping the value
    left_lazy = Left(42).to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 42

    # Lazy is not evaluated until get is called
    lazy = Right('value').to_lazy()
    assert lazy.is_evaluated is False
    assert lazy.get() == 'value'
    assert lazy.is_evaluated is True

    # Works with None and other falsy values
    assert Right(None).to_lazy().get() is None
    assert Left(0).to_lazy().get() == 0

# Generated at 2026-11-02 15:44:57.400797
# Unit test for method bind of class Right
def test_Right_bind():
    from unittest.mock import Mock

    from pymonet.either import Right

    right = Right(42)
    mapper = Mock()
    mapper.return_value = 43

    assert right.bind(mapper) == 43
    mapper.assert_called_once_with(42)

    # bind should return the mapper result directly, unwrapped
    assert right.bind(lambda value: value + 1) == 43
    assert right.bind(lambda value: Right(value + 1)) == Right(43)