

# Generated at 2026-11-01 22:45:51.687190
# Unit test for method is_right of class Right
def test_Right_is_right():
    """Test that Right.is_right() returns True."""
    right = Right(42)
    assert right.is_right() is True

    right_empty = Right(None)
    assert right_empty.is_right() is True

    right_string = Right("value")
    assert right_string.is_right() is True

# Generated at 2026-11-01 22:46:02.133786
# Unit test for method is_right of class Either
def test_Either_is_right():
    from pymonet.either import Left, Right

    assert Right(42).is_right() is True
    assert Left('error').is_right() is False

# Generated at 2026-11-01 22:46:13.191313
# Unit test for method map of class Left
def test_Left_map():
    from pymonet.either import Left, Right

    # map on Left should ignore the mapper and return a new Left with the same value
    left = Left(42)
    result = left.map(lambda value: value + 1)

    assert isinstance(result, Left)
    assert not isinstance(result, Right)
    assert result.value == 42
    assert result.is_left() is True
    assert result.is_right() is False
    assert result == left
    assert result is not left  # a new instance, not the same object

    # the mapper function should never be invoked
    side_effects = []

    def mapper(value):
        side_effects.append(value)
        return value * 2

    result2 = Left('error').map(mapper)
    assert side_effects == []
    assert result2 == Left('error')
    assert result2.value == 'error'

# Generated at 2026-11-01 22:46:23.693982
# Unit test for method is_left of class Left
def test_Left_is_left():
    """Unit test for method is_left of class Left."""
    left = Left(42)

    assert left.is_left() is True
    assert left.is_left() == True
    assert not left.is_right()

# Generated at 2026-11-01 22:46:34.392015
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    from pymonet.maybe import Maybe

    left = Left(42)
    maybe = left.to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe.is_nothing is True
    assert maybe.value is None
    assert maybe == Maybe.nothing()

# Generated at 2026-11-01 22:46:46.883587
# Unit test for method to_maybe of class Right

# Generated at 2026-11-01 22:47:10.157097
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():from pymonet.maybe import Maybe


# Generated at 2026-11-01 22:47:19.752052
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.maybe import Maybe

    # to_maybe should return a Maybe in the "just" state holding the same value
    right = Right(42)
    maybe = right.to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe.is_just is True
    assert maybe.is_nothing() is False
    assert maybe.value == 42
    assert maybe == Maybe.just(42)

    # Works with different value types as well
    right_str = Right("hello")
    maybe_str = right_str.to_maybe()

    assert isinstance(maybe_str, Maybe)
    assert maybe_str.is_just is True
    assert maybe_str.value == "hello"
    assert maybe_str == Maybe.just("hello")

# Generated at 2026-11-01 22:47:31.232513
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Rights with equal values are equal
    assert Right(42) == Right(42)
    assert Right('value') == Right('value')

    # Lefts with equal values are equal
    assert Left(42) == Left(42)
    assert Left('error') == Left('error')

    # Different values are not equal
    assert Right(42) != Right(43)
    assert Left(42) != Left(43)

    # Same value but different side is not equal
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Comparison with non-Either objects is not equal
    assert Right(42) != 42
    assert Left(42) != 42
    assert Right(None) != None
    assert Left(None) != None

    # Base Either instances (neither Left nor Right)
    assert Either(42) == Either(42)
    assert Either(42) != Right(42)
    assert Either(42) != Left(42)
    assert Right(42) != Either(42)

# Generated at 2026-11-01 22:47:56.309253
# Unit test for method case of class Either
def test_Either_case():
    # case on Right should call the success handler with the value
    assert Right(42).case(lambda x: 'error', lambda x: 'success {}'.format(x)) == 'success 42'

    # case on Left should call the error handler with the value
    assert Left(42).case(lambda x: 'error {}'.format(x), lambda x: 'success') == 'error 42'

    # case should return the result of the called handler
    assert Right(0).case(lambda x: x + 1, lambda x: x + 2) == 2
    assert Left(0).case(lambda x: x + 1, lambda x: x + 2) == 1

    # only the matching handler should be invoked
    called = []

    def error_handler(value):
        called.append('error')
        return 'from_error'

    def success_handler(value):
        called.append('success')
        return 'from_success'

    assert Right(1).case(error_handler, success_handler) == 'from_success'
    assert called == ['success']

    called.clear()
    assert Left(1).case(error_handler, success_handler) == 'from_error'
    assert called == ['error']

# Generated at 2026-11-01 22:48:08.802329
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.maybe import Maybe
    from pymonet.either import Right

    right = Right(42)
    maybe = right.to_maybe()

    assert maybe == Maybe.just(42)
    assert maybe.is_just
    assert not maybe.is_nothing
    assert maybe.get_or_else(0) == 42

    # empty value case
    right_empty = Right(None)
    maybe_empty = right_empty.to_maybe()
    assert maybe_empty == Maybe.just(None)
    assert maybe_empty.is_just

# Generated at 2026-11-01 22:48:24.984231
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right transforms into a Lazy wrapping its value
    lazy_from_right = Right(42).to_lazy()
    assert isinstance(lazy_from_right, Lazy)
    assert lazy_from_right.get_value() == 42
    assert lazy_from_right.is_evaluated() is True

    # Left transforms into a Lazy wrapping its value too
    lazy_from_left = Left('error').to_lazy()
    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.get_value() == 'error'

    # Equality against equivalent Lazy instance
    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left(20).to_lazy() == Lazy(lambda: 20)

# Generated at 2026-11-01 22:48:47.406943
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.maybe import Maybe

    either = Right(42)
    maybe = either.to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe == Maybe.just(42)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Generated at 2026-11-01 22:48:59.694169
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    '''Unit test for method to_maybe of class Right'''
    from pymonet.maybe import Maybe

    # Right should be transformed into a Maybe.just with the same value
    maybe = Right(42).to_maybe()

    assert isinstance(maybe, Maybe)
    assert maybe.is_nothing() is False
    assert maybe.value == 42
    assert maybe == Maybe.just(42)

    # Works with different value types as well
    assert Right('test').to_maybe() == Maybe.just('test')

# Generated at 2026-11-01 22:49:08.295445
# Unit test for method case of class Either
def test_Either_case():
    error_handler = lambda value: value + 1
    success_handler = lambda value: value + 2

    assert Left(42).case(error_handler, success_handler) == 43
    assert Right(42).case(error_handler, success_handler) == 44

# Generated at 2026-11-01 22:49:45.264093
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
# nonce:8be9ecd2
    from pymonet.lazy import Lazy

    # Right case: to_lazy should return unevaluated Lazy holding the value
    right = Right(42)
    lazy = right.to_lazy()

    assert isinstance(lazy, Lazy)
    assert not lazy.is_evaluated()
    assert lazy.get() == 42
    assert lazy.is_evaluated()

    # Left case: to_lazy should behave the same way
    left = Left('error')
    lazy_from_left = left.to_lazy()

    assert isinstance(lazy_from_left, Lazy)
    assert not lazy_from_left.is_evaluated()
    assert lazy_from_left.get() == 'error'
    assert lazy_from_left.is_evaluated()

# Generated at 2026-11-01 22:49:56.322364
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.either import Left, Right

    # Left instances with the same value should be equal
    assert Left(1) == Left(1)
    assert Left('test') == Left('test')

    # Right instances with the same value should be equal
    assert Right(1) == Right(1)
    assert Right('test') == Right('test')

    # Left and Right with the same value should not be equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # Instances with different values should not be equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)
    assert Left(1) != Right(2)

    # Either compared with non-Either object should not be equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != 'Left'
    assert Right(1) != 'Right'
    assert Left(1) != None
    assert Right(1) != None

    # Equality should be symmetric
    assert (Left(1) == Left(1)) == (Left(1) == Left(1))
    assert (Right(1) == Right(1)) == (Right(1) == Right(1))

    # Nested values should be compared
    assert Left([1, 2, 3]) == Left([1, 2, 3])
    assert Right([1, 2, 3]) == Right([1, 2, 3])
    assert Left([1, 2, 3]) != Left([1, 2])

# Generated at 2026-11-01 22:50:06.562387
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """Unit test for method __eq__ of class Either"""
    from pymonet.either import Left, Right

    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert not Left(1) == Left(2)
    assert not Right(1) == Right(2)
    assert not Left(1) == Right(1)
    assert not Right(1) == Left(1)
    assert not Left(1) == 1
    assert not Right(1) == 1
    assert not Left(1) == None

# Generated at 2026-11-01 22:50:11.581392
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """Test __eq__ method of Either class."""

    # Left equals Left with the same value
    assert Left(42) == Left(42)

    # Left does not equal Left with different value
    assert Left(42) != Left(43)

    # Right equals Right with the same value
    assert Right(42) == Right(42)

    # Right does not equal Right with different value
    assert Right(42) != Right(43)

    # Left does not equal Right even with the same value
    assert Left(42) != Right(42)

    # Right does not equal Left even with the same value
    assert Right(42) != Left(42)

    # Either does not equal object of other type
    assert Left(42) != 42
    assert Right(42) != '42'
    assert Left(None) != None
    assert Right([1, 2, 3]) != [1, 2, 3]

    # Equality is reflexive
    left = Left(10)
    right = Right(10)
    assert left == left
    assert right == right

# Generated at 2026-11-01 22:50:16.999498
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """Unit test for method __eq__ of class Either"""

    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right('value') == Right('value')
    assert Left('error') == Left('error')

    assert Right(1) != Right(2)
    assert Left(1) != Left(2)

    # Right and Left are not equal even with the same value
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)

    # Comparison with non-Either objects returns False
    assert Right(1) != 1
    assert Left(1) != 1
    assert Right(1) != 'Right(1)'
    assert Left(1) != None

    # Base Either instances with same values are equal
    assert Either(42) == Either(42)
    assert Either(42) != Either(43)

# Generated at 2026-11-01 22:50:21.409126
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Same side and same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left('value') == Left('value')
    assert Right('value') == Right('value')

    # Same value but different sides -> not equal
    assert not Left(1) == Right(1)
    assert not Right(1) == Left(1)

    # Different values -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)
    assert Left(1) != Right(2)

    # Comparing against non-Either objects -> not equal
    assert not Left(1) == 1
    assert not Right(1) == 1
    assert not Left(1) == 'Left'
    assert not Right(None) == None

# Generated at 2026-11-01 22:50:34.916543
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Equality between same side and same value
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left(None) == Left(None)
    assert Right('test') == Right('test')

    # Inequality between different sides with same value
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # Inequality between same side with different values
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # Inequality with non-Either objects
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None
    assert Right(1) != 'Left'

    # Base Either instances compare by value and is_right (both None)
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)

    # Cross comparison between base Either and Left/Right
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-11-01 22:50:43.722924
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    '''Unit test for method to_lazy of class Either'''
    from pymonet.lazy import Lazy

    # to_lazy on Right should return a Lazy monad wrapping the value
    right = Right(42)
    lazy_from_right = right.to_lazy()
    assert isinstance(lazy_from_right, Lazy)
    assert lazy_from_right.get() == 42

    # to_lazy on Left should return a Lazy monad wrapping the value
    left = Left('error')
    lazy_from_left = left.to_lazy()
    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.get() == 'error'

# Generated at 2026-11-01 22:50:51.916315
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """Should return True only when both sides are Either instances
    with equal values and the same rightness."""

    # Right == Right with the same value
    assert Right(42) == Right(42)
    assert Right('value') == Right('value')
    assert Right(None) == Right(None)
    assert Right([1, 2, 3]) == Right([1, 2, 3])

    # Left == Left with the same value
    assert Left(42) == Left(42)
    assert Left('error') == Left('error')
    assert Left(None) == Left(None)

    # Left and Right with the same value are not equal
    assert Left(42) != Right(42)
    assert Right(42) != Left(42)

    # Different values are not equal
    assert Right(42) != Right(43)
    assert Left(42) != Left(43)
    assert Right(42) != Right('42')

    # Comparing with non-Either objects returns False
    assert Right(42) != 42
    assert Left(42) != 42
    assert Right(42) != None
    assert Right(42) != 'Right(42)'
    assert Left('error') != 'error'

    # Equality is symmetric
    assert (Right(1) == Right(1)) == (Right(1) == Right(1))
    assert (Left(1) == Right(1)) == (Right(1) == Left(1))

# Generated at 2026-11-01 22:50:58.274165
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert not Left(1) == Left(2)
    assert not Right(1) == Right(2)
    assert not Left(1) == Right(1)
    assert not Right(1) == Left(1)
    assert not Left(1) == 1
    assert not Right(1) == None
    assert not Left('a') == Right('a')
    assert Left('a') == Left('a')
    assert Right('a') == Right('a')

# Generated at 2026-11-01 22:51:03.701334
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Either(1) == Either(1)

    assert Left(1) != Right(1)
    assert Right(1) != Left(1)
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)
    assert Left(1) != Either(1)
    assert Right(1) != Either(1)

    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) is not None
    assert Right(1) is not None

# Generated at 2026-11-01 22:51:13.942624
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    either = Either(42)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42
    assert lazy.is_evaluated is True
    assert lazy.value == 42

    # to_lazy works for Right as well
    right_lazy = Right('success').to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 'success'

    # to_lazy works for Left as well
    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

# Generated at 2026-11-01 22:51:24.824929
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_from_right = right.to_lazy()

    assert isinstance(lazy_from_right, Lazy)
    assert lazy_from_right.is_evaluated is False
    assert lazy_from_right.get() == 42
    assert lazy_from_right.is_evaluated is True

    left = Left('error')
    lazy_from_left = left.to_lazy()

    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.is_evaluated is False
    assert lazy_from_left.get() == 'error'
    assert lazy_from_left.is_evaluated is True

# Generated at 2026-11-01 22:51:34.535875
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    either = Right(42)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert lazy.get() == 42
    assert lazy.is_evaluated is True
    # value should be memoized after first evaluation
    assert lazy.get() == 42

    left = Left(21)
    lazy_left = left.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert lazy_left.is_evaluated is False
    assert lazy_left.get() == 21
    assert lazy_left.is_evaluated is True
    assert lazy_left.get() == 21

# Generated at 2026-11-01 22:51:42.819729
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # to_lazy on Right should wrap the value in a Lazy monad
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    # to_lazy on Left should also wrap its value in a Lazy monad
    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # underlying lambda should not be evaluated before get() is called
    counter = {'calls': 0}

    def increment_counter():
        counter['calls'] += 1
        return 100

    either_with_side_effect = Right(increment_counter)
    lazy_monad = either_with_side_effect.map(lambda fn: fn()).to_lazy()
    assert counter['calls'] == 0
    assert lazy_monad.get() == 100
    assert counter['calls'] == 1

# Generated at 2026-11-01 22:52:12.310040
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # to_lazy should return a Lazy monad wrapping the stored value
    right = Right(100)
    lazy_from_right = right.to_lazy()

    assert isinstance(lazy_from_right, Lazy)
    assert lazy_from_right.is_evaluated is False
    assert lazy_from_right.get_value() == 100
    assert lazy_from_right.is_evaluated is True

    # Works for Left as well - value is kept unchanged
    left = Left('error')
    lazy_from_left = left.to_lazy()

    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.get_value() == 'error'

    # Result is equivalent to manually created Lazy holding the same value
    assert Right(200).to_lazy() == Lazy(lambda: 200)
    assert Left(None).to_lazy() == Lazy(lambda: None)

# Generated at 2026-11-01 22:52:23.883620
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right wraps its value inside a Lazy monad
    right = Right(42)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42

    # Left also wraps its value inside a Lazy monad
    left = Left('error')
    lazy_from_left = left.to_lazy()
    assert isinstance(lazy_from_left, Lazy)
    assert lazy_from_left.get() == 'error'

    # Base Either wraps its value inside a Lazy monad
    base_lazy = Either('value').to_lazy()
    assert isinstance(base_lazy, Lazy)
    assert base_lazy.get() == 'value'

# Generated at 2026-11-01 22:52:31.053008
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    either = Right(42)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 42


def test_Either_to_lazy_should_return_lazy_wrapping_value():
    from pymonet.lazy import Lazy

    value = object()
    either = Right(value)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() is value


def test_Either_to_lazy_should_work_for_left():
    from pymonet.lazy import Lazy

    either = Left('error')
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 'error'

# Generated at 2026-11-01 22:53:21.228553
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # to_lazy wraps the Either value into a Lazy monad
    lazy = Either(42).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda value: value) == 42

    # Works identically for Right subclass
    right_lazy = Right('success').to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.fold(lambda value: value) == 'success'

    # Works identically for Left subclass
    left_lazy = Left('failure').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.fold(lambda value: value) == 'failure'

    # Original Either remains unchanged after transformation
    either = Either(42)
    either.to_lazy()
    assert either.value == 42

# Generated at 2026-11-01 22:53:46.316136
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either
    Should transform Either into Lazy monad with function returning previous value.
    """
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy

    # Right instance should be transformed into Lazy returning its value
    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get_value() == 42

    # Left instance should be transformed into Lazy returning its value
    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get_value() == 'error'

    # Result should be equal to an equivalent Lazy monad
    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left('error').to_lazy() == Lazy(lambda: 'error')

# Generated at 2026-11-01 22:54:25.035790
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    '''Unit test for method to_lazy of class Either.'''
    from pymonet.lazy import Lazy

    # to_lazy on Right should return a Lazy wrapping the value
    right_either = Right(42)
    lazy = right_either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.evaluate().get() == 42

    # to_lazy on Left should return a Lazy wrapping the value as well
    left_either = Left('error')
    lazy = left_either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.evaluate().get() == 'error'

    # lazy should be able to fold over the wrapped value
    assert right_either.to_lazy().fold(lambda v: v * 2) == 84

# Generated at 2026-11-01 22:55:11.722503
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Right case
    right = Right(42)
    lazy = right.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 42
    assert lazy.is_evaluated is True

    # Left case
    left = Left('error')
    lazy_left = left.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'
    assert lazy_left.is_evaluated is True

    # Lazy should only evaluate the wrapped function once
    lazy_again = Right(100).to_lazy()
    assert lazy_again.get() == 100
    assert lazy_again.get() == 100
    assert lazy_again.value == 100

    # Folding the Lazy should pass the stored value to the function
    assert lazy_again.fold(lambda value: value * 2) == 200