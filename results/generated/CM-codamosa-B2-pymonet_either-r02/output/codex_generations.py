

# Generated at 2026-11-02 12:08:14.130527
# Unit test for method is_right of class Right
def test_Right_is_right():
    from pymonet.either import Right, Left

    # is_right returns True for Right instances
    assert Right(42).is_right() is True
    assert Right(None).is_right() is True
    assert Right('value').is_right() is True
    assert Right([]).is_right() is True

    # is_right returns False for Left instances
    assert Left(42).is_right() is False
    assert Left('error').is_right() is False

# Generated at 2026-11-02 12:09:57.354303
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Equal Left instances with same value
    assert Left(1) == Left(1)
    assert Left('a') == Left('a')

    # Equal Right instances with same value
    assert Right(1) == Right(1)
    assert Right('a') == Right('a')

    # Not equal: different values
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # Not equal: same value but different sides
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # Not equal: comparing with non-Either object
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None
    assert Right(1) != None
    assert Left(1) != '1'

    # Explicit __eq__ method calls
    assert Left(1).__eq__(Left(1)) is True
    assert Right(1).__eq__(Right(1)) is True
    assert Left(1).__eq__(Right(1)) is False
    assert Right(1).__eq__(Left(1)) is False
    assert Left(1).__eq__(1) is False

# Generated at 2026-11-02 12:11:13.173204
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    from pymonet.maybe import Maybe

    left = Left('error')
    maybe = left.to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe == Maybe.nothing()
    assert maybe.is_nothing is True
    assert maybe.is_just is False

# Generated at 2026-11-02 12:13:07.478496
# Unit test for method map of class Left
def test_Left_map():
    left = Left(42)
    mapper = lambda x: x + 1
    result = left.map(mapper)
    assert isinstance(result, Left)
    assert result.value == 42
    assert result == Left(42)
    assert result.is_left() is True
    assert result.is_right() is False
    # mapper should not be applied to Left value
    called = []
    result2 = Left('error').map(lambda x: called.append(x))
    assert result2.value == 'error'
    assert called == []
    assert result2 == Left('error')

# Generated at 2026-11-02 12:16:42.436175
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right case
    right_either = Right(42)
    lazy = right_either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42

    # Left case
    left_either = Left('error')
    lazy = left_either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 'error'