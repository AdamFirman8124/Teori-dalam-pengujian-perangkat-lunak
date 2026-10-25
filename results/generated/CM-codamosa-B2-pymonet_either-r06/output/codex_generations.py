

# Generated at 2026-10-24 07:18:21.550369
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:18:23.966406
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:18:26.390415
# Unit test for method to_maybe of class Right

# Generated at 2026-10-24 07:18:28.800589
# Unit test for method bind of class Left

# Generated at 2026-10-24 07:18:31.217197
# Unit test for method bind of class Left

# Generated at 2026-10-24 07:18:33.630378
# Unit test for method bind of class Left

# Generated at 2026-10-24 07:18:36.044239
# Unit test for method bind of class Right

# Generated at 2026-10-24 07:18:38.467122
# Unit test for method bind of class Right

# Generated at 2026-10-24 07:18:40.880035
# Unit test for method bind of class Right

# Generated at 2026-10-24 07:18:43.295230
# Unit test for method is_right of class Left

# Generated at 2026-10-24 07:18:45.707779
# Unit test for method is_right of class Left

# Generated at 2026-10-24 07:18:48.123361
# Unit test for method is_right of class Left

# Generated at 2026-10-24 07:18:50.538910
# Unit test for method to_box of class Either

# Generated at 2026-10-24 07:18:52.954897
# Unit test for method to_box of class Either

# Generated at 2026-10-24 07:18:55.367704
# Unit test for method to_box of class Either

# Generated at 2026-10-24 07:19:09.995585
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    result = Right(42).to_validation()

    assert isinstance(result, Validation)
    assert result == Validation.success(42)

# Generated at 2026-10-24 07:19:11.634124
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    from pymonet.validation import Validation

    left = Left('error')

    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.value == ['error']
    assert validation.is_success is False
    assert validation.is_failed() is True

# Generated at 2026-10-24 07:19:12.967978
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    from pymonet.validation import Validation

    left = Left('error')

    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.value == ['error']
    assert validation.is_success is False
    assert validation.is_failed() is True

# Generated at 2026-10-24 07:19:14.405036
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

# Generated at 2026-10-24 07:19:30.885692
# Unit test for method is_right of class Right
def test_Right_is_right():
    from pymonet.either import Right, Left

    assert Right(42).is_right() is True
    assert Right(None).is_right() is True   # right-ness is independent of value
    assert Left("error").is_right() is False

# Generated at 2026-10-24 07:19:45.323818
# Unit test for method is_right of class Right
def test_Right_is_right():
    right = Right("success")

    assert right.is_right() is True

# Generated at 2026-10-24 07:19:46.629804
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

# Generated at 2026-10-24 07:19:48.093152
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    from pymonet.validation import Validation

    left = Left('error')

    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.value == ['error']
    assert validation.is_success is False
    assert validation.is_failed() is True

# Generated at 2026-10-24 07:19:49.458411
# Unit test for method to_validation of class Left
def test_Left_to_validation():
    from pymonet.validation import Validation

    left = Left('error')

    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.value == ['error']
    assert validation.is_success is False
    assert validation.is_failed() is True

# Generated at 2026-10-24 07:19:52.116127
# Unit test for method is_right of class Right

# Generated at 2026-10-24 07:19:54.496652
# Unit test for method is_right of class Right

# Generated at 2026-10-24 07:19:56.921054
# Unit test for method is_right of class Right

# Generated at 2026-10-24 07:20:12.929991
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(1) == Left(1)

# Generated at 2026-10-24 07:20:14.247805
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

# Generated at 2026-10-24 07:20:15.588915
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

# Generated at 2026-10-24 07:20:16.893000
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

# Generated at 2026-10-24 07:20:18.211290
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

# Generated at 2026-10-24 07:20:19.533131
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

# Generated at 2026-10-24 07:20:22.036118
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:20:24.459239
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:20:26.874136
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:20:29.291058
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:31.847234
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:34.262036
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:36.688476
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:39.098868
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:41.507705
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:43.919888
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:20:46.336771
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:20:48.752764
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:20:51.164776
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:53.579179
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:55.994088
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:20:58.409006
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:21:00.821455
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:21:03.236144
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:21:05.649883
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:08.067498
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:10.482932
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:12.897236
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:15.309607
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:17.734381
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:20.139331
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:22.553188
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:24.966508
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:27.380050
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:29.795222
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:32.208999
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:34.624148
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:21:58.576610
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Right(1) == Right(1)

# Generated at 2026-10-24 07:22:01.159481
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:22:03.784233
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:22:06.425946
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:22:08.840591
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:11.258946
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:13.896473
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:16.312218
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:18.729085
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:21.143049
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:23.559880
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:22:25.977876
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:22:28.392138
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:22:30.807152
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:33.221938
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:35.641581
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:38.050885
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:40.467351
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:42.880124
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:45.293661
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:22:46.687618
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right

# Generated at 2026-10-24 07:22:48.022874
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

# Generated at 2026-10-24 07:22:49.328863
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

# Generated at 2026-10-24 07:22:50.639541
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

# Generated at 2026-10-24 07:22:51.963397
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

# Generated at 2026-10-24 07:22:53.276432
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

# Generated at 2026-10-24 07:22:54.585071
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

# Generated at 2026-10-24 07:22:55.899862
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

# Generated at 2026-10-24 07:22:57.234784
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

# Generated at 2026-10-24 07:22:58.545941
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

# Generated at 2026-10-24 07:22:59.859265
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

# Generated at 2026-10-24 07:23:01.169633
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

# Generated at 2026-10-24 07:23:02.505474
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

# Generated at 2026-10-24 07:23:03.809510
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

# Generated at 2026-10-24 07:23:05.129644
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

# Generated at 2026-10-24 07:23:07.658994
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:10.173442
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:12.586684
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:15.002472
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:17.417334
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:19.831001
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:22.275596
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:24.691264
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:27.106468
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:29.522040
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:23:31.934844
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:23:34.348626
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:23:36.763943
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:39.181971
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:41.598906
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:44.014837
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:46.431118
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:48.842714
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:51.263743
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:53.673433
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:56.086374
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:23:58.501095
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:00.916885
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:03.332331
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:05.746796
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:08.161200
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:10.574889
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:12.992770
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:15.405869
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:17.819806
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:20.233056
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:24:22.650175
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:24:25.067786
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:24:27.481668
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:29.895792
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:32.310008
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:35.946684
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:38.361800
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:40.775702
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:24:43.188854
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:24:44.653857
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right

# Generated at 2026-10-24 07:24:45.991505
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

# Generated at 2026-10-24 07:24:47.311559
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

# Generated at 2026-10-24 07:24:48.639945
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

# Generated at 2026-10-24 07:24:49.950889
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

# Generated at 2026-10-24 07:24:51.264500
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

# Generated at 2026-10-24 07:24:52.589022
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

# Generated at 2026-10-24 07:24:53.941767
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

# Generated at 2026-10-24 07:24:55.245790
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

# Generated at 2026-10-24 07:25:00.305104
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

# Generated at 2026-10-24 07:25:01.623658
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

# Generated at 2026-10-24 07:25:02.943383
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

# Generated at 2026-10-24 07:25:04.302049
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

# Generated at 2026-10-24 07:25:06.719149
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:09.231522
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:11.798960
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:14.294238
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:16.708865
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:19.128086
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:21.541297
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:25:23.956969
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:25:26.371345
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:25:28.784059
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:31.198652
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:33.613798
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:36.032627
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:25:38.446241
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:25:40.863589
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:25:43.277897
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:45.696279
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:48.121216
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:25:59.274628
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:00.616051
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.either import Left, Right

# Generated at 2026-10-24 07:26:01.948648
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

# Generated at 2026-10-24 07:26:03.285941
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

# Generated at 2026-10-24 07:26:04.594416
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

# Generated at 2026-10-24 07:26:05.925330
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

# Generated at 2026-10-24 07:26:07.237217
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

# Generated at 2026-10-24 07:26:08.567487
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

# Generated at 2026-10-24 07:26:09.879624
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

# Generated at 2026-10-24 07:26:11.241567
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

# Generated at 2026-10-24 07:26:12.548967
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

# Generated at 2026-10-24 07:26:32.945692
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:26:35.366183
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:26:37.776556
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:26:40.189952
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:42.603811
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:45.018227
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:47.436664
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:49.850860
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:52.265714
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:54.678305
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:57.095193
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:26:59.511756
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:27:01.927493
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:27:04.339624
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:27:06.794581
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:27:08.179568
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

# Generated at 2026-10-24 07:27:09.571623
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

# Generated at 2026-10-24 07:27:10.889270
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

# Generated at 2026-10-24 07:27:12.213081
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

# Generated at 2026-10-24 07:27:13.525834
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

# Generated at 2026-10-24 07:27:59.488966
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:01.908225
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:04.325606
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:07.181855
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:09.621283
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:12.042525
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:14.456639
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:16.869198
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:19.281094
# Unit test for method __eq__ of class Either

# Generated at 2026-10-24 07:28:21.693833
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:28:24.110409
# Unit test for method to_lazy of class Either

# Generated at 2026-10-24 07:28:26.522980
# Unit test for method to_lazy of class Either