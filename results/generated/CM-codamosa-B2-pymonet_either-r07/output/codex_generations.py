

# Generated at 2026-10-24 07:44:25.981510
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 07:44:28.399840
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 07:44:30.816330
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 07:44:33.231182
# Unit test for method is_left of class Right

# Generated at 2026-10-24 07:44:35.799918
# Unit test for method is_left of class Right

# Generated at 2026-10-24 07:44:38.215750
# Unit test for method is_left of class Right

# Generated at 2026-10-24 07:44:40.633264
# Unit test for method is_right of class Left

# Generated at 2026-10-24 07:44:43.045913
# Unit test for method is_right of class Left

# Generated at 2026-10-24 07:44:45.465196
# Unit test for method is_right of class Left

# Generated at 2026-10-24 07:44:47.878846
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:44:50.297876
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:44:56.874211
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():from pymonet.maybe import Maybe


# Generated at 2026-10-24 07:44:58.191525
# Unit test for method ap of class Left
def test_Left_ap():
    left = Left(42)

    # Left ignores the applicative, even when it holds a function
    result = left.ap(Right(lambda x: x + 1))
    assert result == Left(42)
    assert result is not left          # returns a copy, not self

    # Same result regardless of what is passed in
    assert Left(42).ap(Left(lambda x: x + 1)) == Left(42)
    assert Left('error').ap(Right(lambda x: x + 1)) == Left('error')

# Generated at 2026-10-24 07:45:10.991885
# Unit test for method is_right of class Left
def test_Left_is_right():
    from pymonet.either import Left

    left = Left(42)

    assert left.is_right() is False

# Generated at 2026-10-24 07:45:12.429777
# Unit test for method case of class Either
def test_Either_case():
    # Right -> only `success` is called, with the Right value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    right = Right(42)

    assert right.case(error, success) == 'success-result'
    success.assert_called_once_with(42)
    error.assert_not_called()

    # Left -> only `error` is called, with the Left value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    left = Left('boom')

    assert left.case(error, success) == 'error-result'
    error.assert_called_once_with('boom')
    success.assert_not_called()

    # The handler's own return value (of any type) is passed through unchanged
    assert Right(1).case(lambda _: None, lambda v: v + 1) == 2
    assert Left(1).case(lambda v: v - 1, lambda _: None) == 0

# Generated at 2026-10-24 07:45:13.755327
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:45:15.093318
# Unit test for method case of class Either
def test_Either_case():
    # Right -> only `success` is called, with the Right value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    right = Right(42)

    assert right.case(error, success) == 'success-result'
    success.assert_called_once_with(42)
    error.assert_not_called()

    # Left -> only `error` is called, with the Left value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    left = Left('boom')

    assert left.case(error, success) == 'error-result'
    error.assert_called_once_with('boom')
    success.assert_not_called()

    # The handler's own return value (of any type) is passed through unchanged
    assert Right(1).case(lambda _: None, lambda v: v + 1) == 2
    assert Left(1).case(lambda v: v - 1, lambda _: None) == 0

# Generated at 2026-10-24 07:45:16.430317
# Unit test for method case of class Either
def test_Either_case():
    # Right -> only `success` is called, with the Right value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    right = Right(42)

    assert right.case(error, success) == 'success-result'
    success.assert_called_once_with(42)
    error.assert_not_called()

    # Left -> only `error` is called, with the Left value, and its result is returned
    success = Mock(return_value='success-result')
    error = Mock(return_value='error-result')
    left = Left('boom')

    assert left.case(error, success) == 'error-result'
    error.assert_called_once_with('boom')
    success.assert_not_called()

    # The handler's own return value (of any type) is passed through unchanged
    assert Right(1).case(lambda _: None, lambda v: v + 1) == 2
    assert Left(1).case(lambda v: v - 1, lambda _: None) == 0

# Generated at 2026-10-24 07:45:46.830950
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    from pymonet.either import Right
    from pymonet.maybe import Maybe

    assert Right(42).to_maybe() == Maybe.just(42)
    assert Right("value").to_maybe() == Maybe.just("value")
    assert Right(0).to_maybe() == Maybe.just(0)
    assert Right(False).to_maybe() == Maybe.just(False)
    assert Right(None).to_maybe() == Maybe.just(None)

    result = Right(42).to_maybe()
    assert isinstance(result, Maybe)
    assert result != Maybe.nothing()

# Generated at 2026-10-24 07:45:49.249438
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:45:51.664710
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:45:54.078859
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:45:55.485361
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:46:11.922631
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    assert Right(42).to_maybe() == Maybe.just(42)

# Generated at 2026-10-24 07:46:28.340813
# Unit test for method to_maybe of class Right
def test_Right_to_maybe():
    assert Right(42).to_maybe() == Maybe.just(42)

# Generated at 2026-10-24 07:46:29.691453
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:46:31.004609
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:46:33.518737
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:46:36.028727
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:46:38.538697
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:46:40.955916
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:46:43.372630
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:46:45.788775
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:46:48.206141
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:46:50.624423
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:46:53.036096
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:46:55.449856
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:16.637855
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(42) == Left(42)

# Generated at 2026-10-24 07:47:17.948304
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:47:19.256133
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:47:20.560460
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:47:21.960988
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:47:23.261862
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:47:24.588820
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:47:25.912445
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:47:27.241334
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:47:28.621510
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:47:29.927235
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:47:31.254745
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:47:32.716124
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:47:35.145201
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:37.548740
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:40.125944
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:42.546549
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:44.957992
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:47.372745
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:49.939183
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:52.444208
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:54.855714
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:47:57.270708
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:47:59.896046
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:48:01.216189
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right

# Generated at 2026-10-24 07:48:02.547991
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:03.873439
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:05.272292
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:06.669404
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:07.989050
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:09.330036
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:10.707860
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:12.139362
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:13.910026
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:15.231253
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:16.658983
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:17.976972
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:19.410228
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:20.732611
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:22.058652
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:23.371306
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:24.690132
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:48:26.006193
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:48:30.339811
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:32.759107
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:35.169535
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:37.582387
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:39.997085
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:42.416110
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:44.830588
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:47.372012
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:49.786372
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:52.203668
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:54.621080
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:57.038332
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:48:59.450975
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:01.866461
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:04.443496
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:05.794513
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:49:07.100732
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:49:08.417463
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:49:09.718397
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:49:11.016055
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:49:15.806590
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:49:17.107769
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:49:18.410100
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:49:19.769181
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:49:21.083654
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:49:23.581556
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:49:25.995357
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:49:28.409215
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:49:30.823504
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:33.236108
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:35.649687
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:38.063843
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:40.479654
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:42.896455
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:45.310708
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:49:47.724375
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:49:50.138717
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:49:52.553120
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:54.979409
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:49:57.393121
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:50:08.913885
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:50:11.331309
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:50:13.741940
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:50:16.158869
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:50:18.575596
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:50:39.799464
# Unit test for method __eq__ of class Either
def test_Either___eq__():left = Left("value")

# Generated at 2026-10-24 07:50:41.115575
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:50:42.421964
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:50:43.728649
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:50:45.052327
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:50:46.365712
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:50:47.785497
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:50:49.101382
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:50:50.410547
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:51:14.362398
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:51:16.777214
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:51:19.192252
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:51:42.733090
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left("error") == Left("error")

# Generated at 2026-10-24 07:51:44.035312
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:51:45.339892
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:51:46.644719
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:51:47.994672
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:51:49.313621
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:51:50.686552
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:51:51.994703
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:51:53.326339
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:52:34.507361
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:36.919546
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:39.334857
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:41.751754
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:44.162716
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:46.577679
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:48.993822
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:51.410653
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:52:52.718287
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Right(1) == Right(1)

# Generated at 2026-10-24 07:52:54.038238
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:52:55.341356
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:52:56.648982
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:52:57.967505
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:52:59.306982
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:53:00.635260
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:53:01.945348
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)

# Generated at 2026-10-24 07:54:24.202156
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Right(42).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert right_lazy.get() == 42

    left_lazy = Left('error').to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert left_lazy.get() == 'error'

    # same value each call, Lazy wraps a constant thunk
    lazy = Right([1, 2]).to_lazy()
    assert lazy.get() == lazy.get() == [1, 2]

# Generated at 2026-10-24 07:54:25.507385
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # same side, same value -> equal
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    # same side, different value -> not equal
    assert Left(1) != Left(2)
    assert Right(1) != Right(2)

    # different side, same value -> not equal
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    # not an Either at all -> not equal
    assert Left(1) != 1
    assert Right(1) != 1
    assert Left(1) != None  # noqa: E711
    assert Right(1) != 'Right(1)'

    # bare Either: is_right() returns None on both sides, so it compares equal
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    # ...but never equal to a Left/Right (None != False/True)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)