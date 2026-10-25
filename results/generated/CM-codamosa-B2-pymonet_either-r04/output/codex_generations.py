

# Generated at 2026-10-24 06:36:10.475941
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:36:12.890103
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:36:15.310555
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:36:17.723472
# Unit test for method bind of class Right

# Generated at 2026-10-24 06:36:20.225749
# Unit test for method bind of class Right

# Generated at 2026-10-24 06:36:22.639152
# Unit test for method bind of class Right

# Generated at 2026-10-24 06:36:25.062202
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 06:36:27.473355
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 06:36:29.888342
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 06:36:32.301908
# Unit test for method bind of class Left

# Generated at 2026-10-24 06:36:34.717394
# Unit test for method bind of class Left

# Generated at 2026-10-24 06:36:37.133085
# Unit test for method bind of class Left

# Generated at 2026-10-24 06:36:39.550262
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 06:36:41.963356
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 06:36:44.379708
# Unit test for method to_validation of class Right

# Generated at 2026-10-24 06:36:46.794374
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 06:36:49.209891
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 06:36:51.624025
# Unit test for method to_maybe of class Left

# Generated at 2026-10-24 06:36:54.039371
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:36:56.454929
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:36:58.868142
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:37:01.282344
# Unit test for method ap of class Left

# Generated at 2026-10-24 06:37:03.697882
# Unit test for method ap of class Left

# Generated at 2026-10-24 06:37:16.878013
# Unit test for method ap of class Left
def test_Left_ap():left = Left("error")
result = left.ap(Right(lambda value: value + 1))
assert result == Left("error")

# Generated at 2026-10-24 06:37:18.199838
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

# Generated at 2026-10-24 06:37:29.727227
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

# Generated at 2026-10-24 06:37:32.239147
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:37:34.656267
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:37:37.209290
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:37:39.629127
# Unit test for method ap of class Left

# Generated at 2026-10-24 06:37:42.163296
# Unit test for method ap of class Left

# Generated at 2026-10-24 06:37:44.579988
# Unit test for method ap of class Left

# Generated at 2026-10-24 06:37:46.995012
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:37:49.408899
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:37:51.824311
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:37:54.242525
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:37:58.453560
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Right(1) == Right(1)

# Generated at 2026-10-24 06:37:59.770626
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

# Generated at 2026-10-24 06:38:01.091366
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

# Generated at 2026-10-24 06:38:08.383204
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    from pymonet.validation import Validation

    left = Left('error')

    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.value == ['error']
    assert validation.is_success is False
    assert validation.is_failed() is True

# Generated at 2026-10-24 06:38:09.711042
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    from pymonet.maybe import Maybe

    assert Left(42).to_maybe() == Maybe.nothing()

# Generated at 2026-10-24 06:38:11.045750
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

# Generated at 2026-10-24 06:38:12.367920
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    from pymonet.maybe import Maybe

    assert Left(42).to_maybe() == Maybe.nothing()

# Generated at 2026-10-24 06:38:13.677993
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    from pymonet.maybe import Maybe

    assert Left(42).to_maybe() == Maybe.nothing()

# Generated at 2026-10-24 06:38:14.999198
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

# Generated at 2026-10-24 06:38:17.500269
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:20.112967
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:22.557130
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:24.961690
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:38:27.483047
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:38:29.898742
# Unit test for method to_validation of class Left

# Generated at 2026-10-24 06:38:32.318840
# Unit test for method case of class Either

# Generated at 2026-10-24 06:38:34.946739
# Unit test for method case of class Either

# Generated at 2026-10-24 06:38:37.363049
# Unit test for method case of class Either

# Generated at 2026-10-24 06:38:39.775049
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:42.190066
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:44.605918
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:47.021625
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:49.433864
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:51.848575
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:54.268077
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:56.690373
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:38:59.093365
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:39:01.507633
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:39:03.924173
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:39:06.339084
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:39:08.755192
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:11.175984
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:13.591408
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:16.005615
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:18.419054
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:20.834122
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:23.249134
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:39:25.663558
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:39:28.077028
# Unit test for method is_right of class Left

# Generated at 2026-10-24 06:39:30.492558
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:32.908196
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:35.320887
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:37.735044
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:39:59.045709
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:40:57.757031
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right

# Generated at 2026-10-24 06:40:59.093462
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

# Generated at 2026-10-24 06:41:00.414975
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

# Generated at 2026-10-24 06:41:01.725225
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

# Generated at 2026-10-24 06:41:03.069065
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

# Generated at 2026-10-24 06:41:04.385590
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

# Generated at 2026-10-24 06:41:05.712896
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

# Generated at 2026-10-24 06:41:07.020709
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

# Generated at 2026-10-24 06:41:08.331874
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

# Generated at 2026-10-24 06:41:09.664894
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

# Generated at 2026-10-24 06:41:10.979436
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

# Generated at 2026-10-24 06:41:12.285435
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

# Generated at 2026-10-24 06:41:13.616273
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

# Generated at 2026-10-24 06:41:14.933192
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

# Generated at 2026-10-24 06:41:17.352848
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:19.767627
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:22.183131
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:24.678294
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:27.175248
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:29.592532
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:32.010995
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:41:34.434066
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:41:36.979797
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:41:39.429988
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:41.806536
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:44.222297
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:46.636001
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:41:49.049757
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:41:51.468053
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:41:53.881348
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:56.294515
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:41:58.709816
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:01.127569
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:03.545587
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:05.959536
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:08.373646
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:42:10.788773
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:42:13.205736
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:42:15.619575
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:18.033794
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:20.449957
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:22.865470
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:25.278918
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:27.692208
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:30.106407
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:32.524904
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:34.947703
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:37.360750
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:40.757101
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:42:42.086861
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right

# Generated at 2026-10-24 06:42:43.401320
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

# Generated at 2026-10-24 06:42:44.706305
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

# Generated at 2026-10-24 06:42:46.031314
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

# Generated at 2026-10-24 06:42:47.529213
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

# Generated at 2026-10-24 06:42:48.962589
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

# Generated at 2026-10-24 06:42:50.279772
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

# Generated at 2026-10-24 06:42:52.240780
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

# Generated at 2026-10-24 06:42:53.569847
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

# Generated at 2026-10-24 06:42:54.898896
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

# Generated at 2026-10-24 06:42:56.217349
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

# Generated at 2026-10-24 06:42:57.522575
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

# Generated at 2026-10-24 06:42:58.849825
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

# Generated at 2026-10-24 06:43:00.172548
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

# Generated at 2026-10-24 06:43:01.500533
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

# Generated at 2026-10-24 06:43:02.813648
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

# Generated at 2026-10-24 06:43:04.125726
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

# Generated at 2026-10-24 06:43:07.395387
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

# Generated at 2026-10-24 06:43:08.709084
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

# Generated at 2026-10-24 06:43:11.240394
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:13.745829
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:16.160391
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:18.579284
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:20.997971
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:23.581066
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:26.014460
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:43:28.421490
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:43:30.836355
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:43:33.251682
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:35.664844
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:38.080977
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:40.496745
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:43:55.840030
# Unit test for method __eq__ of class Either
def test_Either___eq__():left = Left("error")

# Generated at 2026-10-24 06:43:57.137673
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

# Generated at 2026-10-24 06:43:58.444626
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

# Generated at 2026-10-24 06:43:59.753539
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

# Generated at 2026-10-24 06:44:04.826058
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

# Generated at 2026-10-24 06:44:06.137025
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

# Generated at 2026-10-24 06:44:07.451412
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

# Generated at 2026-10-24 06:44:08.783893
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

# Generated at 2026-10-24 06:44:11.212674
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:13.620689
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:16.039432
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:18.456840
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:20.871955
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:23.290303
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:25.704990
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:28.252138
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:30.679341
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:33.090729
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:35.515997
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:37.930317
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:40.348851
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:42.766969
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:45.178380
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:44:47.594889
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:44:50.010305
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:44:52.422502
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:45:02.364760
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

# Generated at 2026-10-24 06:45:03.687150
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

# Generated at 2026-10-24 06:45:05.116309
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

# Generated at 2026-10-24 06:45:06.448963
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

# Generated at 2026-10-24 06:45:07.771383
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

# Generated at 2026-10-24 06:45:09.087926
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

# Generated at 2026-10-24 06:45:10.405796
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

# Generated at 2026-10-24 06:45:11.814644
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

# Generated at 2026-10-24 06:45:13.152089
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

# Generated at 2026-10-24 06:45:14.456967
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

# Generated at 2026-10-24 06:45:38.387906
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:45:40.805297
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:45:43.220518
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 06:45:45.638557
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:45:48.055227
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:45:50.465151
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:45:52.880155
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:45:55.297840
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:45:57.709864
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:46:00.123476
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:46:02.534233
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:46:04.950068
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:46:07.362487
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:46:09.774301
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 06:46:12.191863
# Unit test for method __eq__ of class Either