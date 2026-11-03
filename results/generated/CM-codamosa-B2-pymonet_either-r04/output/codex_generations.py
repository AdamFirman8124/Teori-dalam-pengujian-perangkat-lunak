

# Generated at 2026-11-03 00:23:08.681920
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    from pymonet.validation import Validation

    left = Left(42)
    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.value is None
    assert validation.errors == [42]

# Generated at 2026-11-03 00:25:04.599692
# Unit test for method map of class Right
def test_Right_map():
    """Unit test for method map of class Right."""
    right = Right(10)

    mapped = right.map(lambda value: value + 5)

    assert isinstance(mapped, Right)
    assert mapped.value == 15
    assert mapped.is_right() is True
    assert mapped.is_left() is False

# Generated at 2026-11-03 00:26:13.433260
# Unit test for constructor of class Right
def test_Right():
    right = Right(42)
    assert right.value == 42
    assert right.is_right() is True
    assert right.is_left() is False

    right_str = Right('test')
    assert right_str.value == 'test'
    assert right_str.is_right() is True
    assert right_str.is_left() is False

    assert right == Right(42)
    assert right != right_str

# Generated at 2026-11-03 00:27:13.521782
# Unit test for method ap of class Either
def test_Either_ap():
    # Right.ap applies the function inside the applicative to its value
    right = Right(21)
    applicative = Right(lambda value: value + 1)
    assert right.ap(applicative) == Right(22)

    # Right.ap with a Left applicative delegates to Left.map, which ignores the mapper
    assert right.ap(Left(0)) == Left(0)

    # Left.ap ignores the monad and returns a copy of self
    left = Left(42)
    result = left.ap(Right(lambda value: value + 1))
    assert result == Left(42)
    assert result is not left
    assert result.value == left.value

# Generated at 2026-11-03 00:28:28.577871
# Unit test for constructor of class Right
def test_Right():
    """Unit test for constructor of class Right."""
    right = Right(42)

    assert isinstance(right, Either)
    assert isinstance(right, Right)
    assert right.value == 42
    assert right.is_right() is True
    assert right.is_left() is False

    # Equality with another Right holding the same value
    assert right == Right(42)
    assert right != Right(43)
    assert right != Left(42)

# Generated at 2026-11-03 00:29:31.147067
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Left instances with the same value are equal
    assert Left(1) == Left(1)
    assert Left('value') == Left('value')
    assert Left(None) == Left(None)

    # Right instances with the same value are equal
    assert Right(1) == Right(1)
    assert Right('value') == Right('value')
    assert Right(None) == Right(None)

    # Left and Right with the same value are not equal (is_right differs)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # Instances with different values are not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)
    assert Left(1) != Right(2)
    assert Right(1) != Left(2)

    # Comparison against non-Either objects returns False
    assert (Left(1) == 1) is False
    assert (Right(1) == 1) is False
    assert (Left(1) == None) is False
    assert (Right(1) == None) is False
    assert (Left(1) == '1') is False

    # Comparison is symmetric
    left = Left(42)
    right = Right(42)
    assert (left == right) == (right == left)
    assert (left == Left(42)) == (Left(42) == left)
    assert (right == Right(42)) == (Right(42) == right)

# Generated at 2026-11-03 00:30:42.826997
# Unit test for method is_right of class Left
def test_Left_is_right():
    """Unit test for method is_right of class Left"""
    from pymonet.either import Left

    assert Left(42).is_right() is False
    assert Left(None).is_right() is False
    assert Left('error').is_right() is False