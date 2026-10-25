

# Generated at 2026-10-25 00:07:31.154018
# Unit test for method bind of class Left

# Generated at 2026-10-25 00:07:33.585771
# Unit test for method bind of class Left

# Generated at 2026-10-25 00:07:36.010382
# Unit test for method bind of class Left

# Generated at 2026-10-25 00:07:38.428987
# Unit test for method ap of class Left

# Generated at 2026-10-25 00:07:40.846936
# Unit test for method ap of class Left

# Generated at 2026-10-25 00:07:43.263223
# Unit test for method ap of class Left

# Generated at 2026-10-25 00:07:45.680506
# Unit test for method map of class Right

# Generated at 2026-10-25 00:07:48.100470
# Unit test for method map of class Right

# Generated at 2026-10-25 00:07:50.526203
# Unit test for method map of class Right

# Generated at 2026-10-25 00:08:03.145512
# Unit test for method to_validation of class Left
def test_Left_to_validation():from pymonet.validation import Validation


# Generated at 2026-10-25 00:08:07.638397
# Unit test for method is_left of class Right
def test_Right_is_left():
    assert Right(42).is_left() is False

# Generated at 2026-10-25 00:08:48.558613
# Unit test for method ap of class Either
def test_Either_ap():
    # Right(function) applied to Right(value) -> Right(function(value))
    assert Right(lambda x: x + 1).ap(Right(1)) == Right(2)
    assert Right(lambda x: x.upper()).ap(Right("hello")) == Right("HELLO")

    # Right(function) applied to Left(value) -> Left(value)
    assert Right(lambda x: x + 1).ap(Left("error")) == Left("error")

    # Left(error) applied to Right(value) -> Left(error), function ignored
    assert Left("error").ap(Right(1)) == Left("error")

    # Left(error) applied to Left(value) -> Left(error), second ignored
    assert Left("error").ap(Left("other")) == Left("error")

# Generated at 2026-10-25 00:08:50.981829
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 00:08:53.396065
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 00:08:55.814457
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 00:09:07.755752
# Unit test for method is_right of class Left
def test_Left_is_right():assert Left("error").is_right() is False

# Generated at 2026-10-25 00:09:12.224825
# Unit test for method is_right of class Left
def test_Left_is_right():
    left = Left("error")

    assert left.is_right() is False

# Generated at 2026-10-25 00:09:25.073258
# Unit test for method ap of class Either
def test_Either_ap():
    # Right containing a function applies it to the value in another Right
    assert Right(lambda value: value * 2).ap(Right(3)) == Right(6)

    # A Left short-circuits the computation
    assert Left("function error").ap(Right(3)) == Left("function error")
    assert Right(lambda value: value * 2).ap(Left("value error")) == Left("value error")

# Generated at 2026-10-25 00:09:33.355910
# Unit test for method is_right of class Right
def test_Right_is_right():
    right = Right("value")

    assert right.is_right() is True

# Generated at 2026-10-25 00:09:37.446367
# Unit test for method is_right of class Left
def test_Left_is_right():
    left = Left("error")

    assert left.is_right() is False

# Generated at 2026-10-25 00:09:40.812559
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    """Transform Either to Maybe: Left -> Maybe.nothing"""
    from pymonet.either import Left

    left = Left(42)
    maybe = left.to_maybe()

    assert maybe.is_nothing
    assert maybe.value is None

# Generated at 2026-10-25 00:09:43.334894
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:09:45.756435
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:09:48.172240
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:09:50.587698
# Unit test for method case of class Either

# Generated at 2026-10-25 00:09:53.002230
# Unit test for method case of class Either

# Generated at 2026-10-25 00:09:55.418811
# Unit test for method case of class Either

# Generated at 2026-10-25 00:09:57.834665
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:10:00.250817
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:10:02.665968
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:10:05.080610
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:10:07.496581
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:10:09.910991
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 00:10:16.668534
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    lazy_right = right.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.get() == 42

    left = Left('error')
    lazy_left = left.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.get() == 'error'

# Generated at 2026-10-25 00:10:38.011603
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(42) == Left(42)
    assert Right(42) == Right(42)

    assert Left(42) != Left(7)
    assert Right(42) != Right(7)

    # Equal values on different branches must not be equal.
    assert Left(42) != Right(42)
    assert Right(42) != Left(42)

    # An Either must not equal an unrelated object.
    assert Left(42) != 42
    assert Right(42) != 42

# Generated at 2026-10-25 00:10:54.379398
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.either import Left, Right

    # Right == Right with the same value
    assert Right(42) == Right(42)

    # Left == Left with the same value
    assert Left(42) == Left(42)

    # Left is NOT equal to Right, even with the same value
    assert Left(42) != Right(42)
    assert Right(42) != Left(42)

    # Different values are not equal, within the same side
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)

    # Comparison with non-Either object returns False (no crash)
    assert Right(42) != 42
    assert Left(42) != "Left"
    assert Right(42) != None

    # Equality is symmetric
    assert (Right(1) == Right(1)) == (Right(1) == Right(1))
    assert (Left(1) == Right(1)) == (Right(1) == Left(1))

# Generated at 2026-10-25 00:11:15.522942
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Equal instances: same variant and value
    assert Left("error") == Left("error")
    assert Right(42) == Right(42)

    # Different values
    assert Left("error") != Left("other error")
    assert Right(42) != Right(43)

    # Same value but different variants
    assert Left(42) != Right(42)
    assert Right(42) != Left(42)

    # Non-Either objects
    assert Left("error") != "error"
    assert Right(42) != 42
    assert Right(None) != None  # noqa: E711

# Generated at 2026-10-25 00:11:36.196641
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Same variant and value are equal.
    assert Right(42) == Right(42)
    assert Left("error") == Left("error")

    # Different values are not equal.
    assert Right(42) != Right(43)
    assert Left("error") != Left("other error")

    # Equal values in different variants are not equal.
    assert Right(42) != Left(42)
    assert Left(42) != Right(42)

    # Either instances are not equal to unrelated objects.
    assert Right(42) != 42
    assert Left("error") != "error"

# Generated at 2026-10-25 00:11:52.924751
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.either import Left, Right

    # Right == Right with the same value
    assert Right(42) == Right(42)

    # Left == Left with the same value
    assert Left(42) == Left(42)

    # Left is NOT equal to Right, even with the same value
    assert Left(42) != Right(42)
    assert Right(42) != Left(42)

    # Different values are not equal, within the same side
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)

    # Comparison with non-Either object returns False (no crash)
    assert Right(42) != 42
    assert Left(42) != "Left"
    assert Right(42) != None

    # Equality is symmetric
    assert (Right(1) == Right(1)) == (Right(1) == Right(1))
    assert (Left(1) == Right(1)) == (Right(1) == Left(1))

# Generated at 2026-10-25 00:12:02.098632
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right("success")):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:12:03.425570
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:12:04.755172
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Right: success handler is called with the value
    assert Right(42).case(error_handler, success_handler) == 'success: 42'

    # Left: error handler is called with the value
    assert Left('oops').case(error_handler, success_handler) == 'error: oops'

# Generated at 2026-10-25 00:12:13.818027
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:12:15.150622
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:12:22.519539
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:12:31.734843
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 00:12:33.066051
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:12:41.229354
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:12:48.426583
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:12:55.800189
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:13:02.558516
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 00:13:03.928666
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:13:11.364390
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right("success")):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:13:12.695801
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:13:20.478877
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("value"), Right("value")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == "value"

# Generated at 2026-10-25 00:13:21.808182
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:13:29.731003
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:13:39.012320
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:13:47.206756
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right("success").to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == "success"

# Generated at 2026-10-25 00:13:55.811687
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:13:57.444735
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:14:04.101433
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:14:11.575859
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:14:12.904658
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:14:20.701545
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:14:22.122211
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:14:29.497025
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right("success")):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:14:30.823746
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:14:39.329210
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:14:46.699346
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:14:54.689127
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:15:04.727366
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:15:06.258452
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:15:13.032163
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:15:22.027456
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:15:29.195957
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:15:35.034128
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:15:45.275323
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:15:51.761226
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 00:15:53.085356
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:16:01.144116
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:16:08.312185
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 00:16:21.830039
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 00:16:23.148488
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:16:30.021533
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 00:16:31.335012
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:16:53.172741
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 00:16:54.598528
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:17:01.982322
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left("error").to_lazy().get() == "error"
    assert Right(42).to_lazy().get() == 42

# Generated at 2026-10-25 00:17:10.147180
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:17:11.472881
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'

# Generated at 2026-10-25 00:17:22.040948
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 00:17:29.824981
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 00:17:31.150348
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.either import Either, Left, Right
    from pymonet.lazy import Lazy

    lazy_right = Right(42).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.compute() == 42

    lazy_left = Left('error').to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.compute() == 'error'

    # value is not evaluated eagerly: a callable is stored, not the result
    lazy_fn = Left('x').to_lazy()
    assert lazy_fn.compute() == 'x'
    assert lazy_fn.compute() == 'x'