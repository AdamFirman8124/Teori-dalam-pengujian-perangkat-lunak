

# Generated at 2026-10-25 03:37:44.267330
# Unit test for method ap of class Either
def test_Either_ap():
    inc = lambda x: x + 1

    # Right holding the function, applied to a Right value -> Right(result)
    assert Right(inc).ap(Right(1)) == Right(2)

    # Function in Right, applicative is Left -> Left copy of the Left value
    result = Right(inc).ap(Left('error'))
    assert result.is_left() is True
    assert result.value == 'error'

    # Function inside Left -> Left.ap ignores the applicative,
    # returns a Left copy holding the same function
    result = Left(inc).ap(Right(1))
    assert result.is_left() is True
    assert result.value is inc

# Generated at 2026-10-25 03:37:55.735473
# Unit test for method to_box of class Either
def test_Either_to_box():
    from pymonet.box import Box

    left_box = Left("error").to_box()
    assert isinstance(left_box, Box)
    assert left_box.value == "error"

    right_box = Right(42).to_box()
    assert isinstance(right_box, Box)
    assert right_box.value == 42

# Generated at 2026-10-25 03:38:02.207457
# Unit test for method ap of class Left
def test_Left_ap():
    left = Left(1)
    mapper = lambda value: value + 1

    # Left.ap ignores the function inside the Right applicative
    assert left.ap(Right(mapper)) == Left(1)
    assert left.ap(Right(mapper)).value == 1

    # The mapper function must never be called
    called = []
    def tracking_mapper(value):
        called.append(value)
        return value + 1

    result = left.ap(Right(tracking_mapper))
    assert called == []
    assert result == Left(1)
    assert result is not left  # ap returns a new instance, not self

    # ap on a Left applicative also returns a copy of self
    assert left.ap(Left(mapper)) == Left(1)

# Generated at 2026-10-25 03:38:10.687960
# Unit test for constructor of class Right
def test_Right():
    value = 42

    result = Right(value)

    assert isinstance(result, Right)
    assert isinstance(result, Either)
    assert result.value == value
    assert result.is_right() is True
    assert result.is_left() is False

# Generated at 2026-10-25 03:38:14.686510
# Unit test for constructor of class Right
def test_Right():
    value = 42

    result = Right(value)

    assert isinstance(result, Right)
    assert isinstance(result, Either)
    assert result.value == value
    assert result.is_right() is True
    assert result.is_left() is False

# Generated at 2026-10-25 03:38:16.016767
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

# Generated at 2026-10-25 03:38:23.847217
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:38:25.209112
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Right: success handler is called with the value
    assert Right(42).case(error_handler, success_handler) == 'success: 42'

    # Left: error handler is called with the value
    assert Left('oops').case(error_handler, success_handler) == 'error: oops'

# Generated at 2026-10-25 03:38:32.603540
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either, expected in (
        (Right(42), 42),
        (Left("error"), "error"),
    ):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == expected

# Generated at 2026-10-25 03:38:38.960577
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:38:40.296055
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Right: success handler is called with the value
    assert Right(42).case(error_handler, success_handler) == 'success: 42'

    # Left: error handler is called with the value
    assert Left('oops').case(error_handler, success_handler) == 'error: oops'

# Generated at 2026-10-25 03:38:41.816372
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

# Generated at 2026-10-25 03:38:43.248824
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

# Generated at 2026-10-25 03:38:44.681466
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Right: success handler is called with the value
    assert Right(42).case(error_handler, success_handler) == 'success: 42'

    # Left: error handler is called with the value
    assert Left('oops').case(error_handler, success_handler) == 'error: oops'

# Generated at 2026-10-25 03:38:52.474417
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:38:53.898013
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Right: success handler is called with the value
    assert Right(42).case(error_handler, success_handler) == 'success: 42'

    # Left: error handler is called with the value
    assert Left('oops').case(error_handler, success_handler) == 'error: oops'

# Generated at 2026-10-25 03:39:00.144983
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 03:39:04.710597
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:39:07.249355
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:09.666673
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:12.086806
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:14.504624
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:16.919219
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:19.335800
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:21.751561
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:24.167122
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:26.582858
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:28.998459
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:39:46.538973
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.lazy import Lazy

# Generated at 2026-10-25 03:39:54.516472
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 03:40:03.843057
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:40:08.447477
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:40:14.911982
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:40:17.332558
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:19.746132
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:22.160491
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:24.574982
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:26.990655
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:29.405558
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:31.820161
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:34.235903
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:36.650107
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:39.068750
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:41.485866
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:40:44.104218
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

# Generated at 2026-10-25 03:40:51.792287
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:41:00.260576
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right("success")):
        result = either.to_lazy()

        assert isinstance(result, Lazy)
        assert result.get() == either.value

# Generated at 2026-10-25 03:41:05.485766
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Either(42).to_lazy()

# Generated at 2026-10-25 03:41:14.699235
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:41:19.716654
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Right(42).to_lazy()

# Generated at 2026-10-25 03:41:27.724631
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:41:37.024798
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:41:39.653014
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:41:42.173704
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:41:44.803828
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.lazy import Lazy

# Generated at 2026-10-25 03:41:51.565398
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:41:58.839310
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right("success")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:42:06.113109
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Either(42).to_lazy()

# Generated at 2026-10-25 03:42:14.532519
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = object()

    left_lazy = Left(value).to_lazy()
    right_lazy = Right(value).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() is value
    assert right_lazy.get() is value

# Generated at 2026-10-25 03:42:21.571432
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(42)
    left = Left("error")

    right_lazy = right.to_lazy()
    left_lazy = left.to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 03:42:30.070703
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:42:35.392712
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Right(42).to_lazy()

# Generated at 2026-10-25 03:42:42.763534
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:42:49.834753
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 03:42:58.378359
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right("success")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:43:04.058599
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():result = Either(42).to_lazy()

# Generated at 2026-10-25 03:43:10.358268
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:43:18.232898
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:43:22.718790
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:43:28.742649
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:43:33.456470
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Right(42).to_lazy()

# Generated at 2026-10-25 03:43:41.952698
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = object()

    for either in (Left(value), Right(value)):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() is value

# Generated at 2026-10-25 03:43:44.547080
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:43:48.504315
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:43:55.570026
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 03:44:04.094681
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:44:12.026974
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:44:18.518538
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either, expected in (
        (Left("error"), "error"),
        (Right(42), 42),
    ):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == expected

# Generated at 2026-10-25 03:44:22.710141
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:44:30.377091
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:44:36.224328
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 03:44:43.904909
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:44:46.436038
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

# Generated at 2026-10-25 03:44:58.653693
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either, expected in (
        (Right(42), 42),
        (Left("error"), "error"),
    ):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == expected

# Generated at 2026-10-25 03:45:03.256666
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Right(42).to_lazy()

# Generated at 2026-10-25 03:45:15.145907
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:45:29.370907
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right("success")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:45:34.902781
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:45:42.682248
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either, expected in (
        (Left("error"), "error"),
        (Right(42), 42),
    ):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == expected

# Generated at 2026-10-25 03:45:45.218602
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 03:45:50.367699
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:45:58.554086
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either, expected in (
        (Left("error"), "error"),
        (Right(42), 42),
    ):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == expected

# Generated at 2026-10-25 03:46:03.577425
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:46:09.792526
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:46:17.257910
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Right(42), Left("error")):
        lazy = either.to_lazy()

        assert isinstance(lazy, Lazy)
        assert lazy.get() == either.value

# Generated at 2026-10-25 03:46:22.961789
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():result = Right(42).to_lazy()

# Generated at 2026-10-25 03:46:29.888229
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either, expected in (
        (Left("error"), "error"),
        (Right(42), 42),
    ):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == expected

# Generated at 2026-10-25 03:46:34.602854
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():result = Right(42).to_lazy()

# Generated at 2026-10-25 03:46:41.172537
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:46:48.734584
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    for either in (Left("error"), Right(42)):
        lazy_value = either.to_lazy()

        assert isinstance(lazy_value, Lazy)
        assert lazy_value.get() == either.value

# Generated at 2026-10-25 03:46:58.253009
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 03:47:04.294905
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 03:47:13.612407
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right_lazy = Right(42).to_lazy()
    left_lazy = Left("error").to_lazy()

    assert isinstance(right_lazy, Lazy)
    assert isinstance(left_lazy, Lazy)
    assert right_lazy.get() == 42
    assert left_lazy.get() == "error"

# Generated at 2026-10-25 03:47:20.270443
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left_lazy = Left("error").to_lazy()
    right_lazy = Right(42).to_lazy()

    assert isinstance(left_lazy, Lazy)
    assert isinstance(right_lazy, Lazy)
    assert left_lazy.get() == "error"
    assert right_lazy.get() == 42

# Generated at 2026-10-25 03:47:28.973144
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left("error")
    right = Right(42)

    lazy_left = left.to_lazy()
    lazy_right = right.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert isinstance(lazy_right, Lazy)
    assert lazy_left.get() == "error"
    assert lazy_right.get() == 42

# Generated at 2026-10-25 03:47:37.472307
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left("error")
    right = Right(42)

    lazy_left = left.to_lazy()
    lazy_right = right.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert isinstance(lazy_right, Lazy)
    assert lazy_left.get() == "error"
    assert lazy_right.get() == 42