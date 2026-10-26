

# Generated at 2026-10-25 06:28:49.031332
# Unit test for constructor of class Left
def test_Left():
    left = Left(42)

    assert left.value == 42
    assert left.is_left() is True
    assert left.is_right() is False
    assert left == Left(42)
    assert left != Left(43)
    assert left != Right(42)

# Generated at 2026-10-25 06:28:51.447112
# Unit test for method to_box of class Either

# Generated at 2026-10-25 06:28:54.305510
# Unit test for method to_box of class Either

# Generated at 2026-10-25 06:28:56.721748
# Unit test for method to_box of class Either

# Generated at 2026-10-25 06:28:59.135519
# Unit test for method map of class Right

# Generated at 2026-10-25 06:29:01.548824
# Unit test for method map of class Right

# Generated at 2026-10-25 06:29:03.963694
# Unit test for method map of class Right

# Generated at 2026-10-25 06:29:06.379313
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:29:08.793476
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:29:11.305172
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:29:13.693737
# Unit test for method map of class Right

# Generated at 2026-10-25 06:29:16.105260
# Unit test for method map of class Right

# Generated at 2026-10-25 06:29:18.525751
# Unit test for method map of class Right

# Generated at 2026-10-25 06:29:20.939254
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:29:23.355299
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:29:25.772133
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:29:27.240774
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Right: success handler is called with the value
    assert Right(42).case(error_handler, success_handler) == 'success: 42'

    # Left: error handler is called with the value
    assert Left('oops').case(error_handler, success_handler) == 'error: oops'

# Generated at 2026-10-25 06:29:28.576172
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

# Generated at 2026-10-25 06:29:30.051884
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

# Generated at 2026-10-25 06:29:46.023203
# Unit test for method bind of class Right
def test_Right_bind():
    # bind applies mapper to unwrapped value and returns mapper result directly
    assert Right(42).bind(lambda x: Right(x + 1)) == Right(43)

    # mapper receives the raw value, not the Either
    seen = []
    def mapper(value):
        seen.append(value)
        return Right(value * 2)

    result = Right(21).bind(mapper)

    assert seen == [21]
    assert result == Right(42)
    assert isinstance(result, Right)

    # bind flattens - mapper returning Left is propagated as Left
    assert Right(42).bind(lambda x: Left("error")) == Left("error")
    assert isinstance(Right(42).bind(lambda _: Left("error")), Left)

    # chaining binds
    assert (
        Right(1).bind(lambda x: Right(x + 1)).bind(lambda x: Right(x * 10))
        == Right(20)
    )

# Generated at 2026-10-25 06:29:47.460048
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

# Generated at 2026-10-25 06:29:52.576647
# Unit test for method is_left of class Right
def test_Right_is_left():
    assert Right(42).is_left() is False

# Generated at 2026-10-25 06:30:06.301937
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:07.741789
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:09.085052
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

# Generated at 2026-10-25 06:30:10.915225
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:12.354880
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:13.885742
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:15.319177
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:16.778402
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

# Generated at 2026-10-25 06:30:18.185074
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:19.621487
# Unit test for method to_validation of class Right
def test_Right_to_validation():
    assert Right(42).to_validation() == Validation.success(42)

# Generated at 2026-10-25 06:30:41.003724
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:30:43.419356
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:30:45.832748
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:30:48.582340
# Unit test for method to_validation of class Right

# Generated at 2026-10-25 06:30:51.346638
# Unit test for method to_validation of class Right

# Generated at 2026-10-25 06:30:53.921234
# Unit test for method to_validation of class Right

# Generated at 2026-10-25 06:30:56.336905
# Unit test for method to_validation of class Right

# Generated at 2026-10-25 06:30:58.737523
# Unit test for method to_validation of class Right

# Generated at 2026-10-25 06:31:01.351685
# Unit test for method to_validation of class Right

# Generated at 2026-10-25 06:31:03.768490
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:31:06.181783
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:31:08.597006
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:31:11.013852
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:31:13.430000
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:31:15.843932
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:31:18.260516
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:31:20.676549
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:31:23.090848
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:31:25.508273
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:31:27.919927
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:31:30.350320
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:31:32.764286
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:31:39.479400
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(42) == Left(42)

# Generated at 2026-10-25 06:31:42.198857
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

# Generated at 2026-10-25 06:31:44.980709
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

# Generated at 2026-10-25 06:31:46.353846
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

# Generated at 2026-10-25 06:31:49.082247
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

# Generated at 2026-10-25 06:31:51.851519
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

# Generated at 2026-10-25 06:31:54.856453
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

# Generated at 2026-10-25 06:31:57.520752
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:31:59.941323
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:02.353275
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:04.765721
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:07.183240
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:09.600757
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:12.306038
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:14.724877
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:17.142804
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:19.560077
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:32:21.976137
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:32:24.393737
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:32:26.832923
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:32:29.225701
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:32:31.642915
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:32:34.060680
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:36.475932
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:38.892665
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:32:41.362915
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:32:57.413856
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(1).__eq__(Left(1)) is True

# Generated at 2026-10-25 06:33:00.149553
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:02.724042
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:05.138279
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:07.877485
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:33:10.294057
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:33:12.708857
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 06:33:15.124249
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:17.538393
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:19.952525
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:22.370502
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:24.783046
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:27.198619
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:29.620993
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:32.038622
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:34.452391
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:36.865376
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:39.287093
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:41.703427
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:44.123947
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:46.539808
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:48.954541
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:51.368470
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:53.792798
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:56.204800
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:33:58.623901
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:01.038855
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:03.455452
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:05.870993
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:08.287540
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:10.704478
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:13.124431
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:15.539803
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:17.952304
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:20.366696
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:22.787115
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:25.202535
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:27.621253
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:30.040543
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:32.455713
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:34.873779
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:37.293716
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:39.708344
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:42.126254
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:44.545422
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:46.961011
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:34:50.051094
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

# Generated at 2026-10-25 06:34:52.874422
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

# Generated at 2026-10-25 06:34:55.689255
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

# Generated at 2026-10-25 06:34:58.406201
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

# Generated at 2026-10-25 06:35:01.323022
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

# Generated at 2026-10-25 06:35:04.088771
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:06.600075
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:08.990796
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:11.412929
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:13.848383
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:16.264092
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:18.675921
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:21.385370
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:23.801096
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:26.218626
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:28.609709
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:31.025740
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:33.447516
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:35.861387
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:38.277773
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:40.695806
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:43.111307
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:45.528197
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:47.951303
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:35:50.366329
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:07.371611
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Right(42).to_lazy()

# Generated at 2026-10-25 06:36:10.238726
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

# Generated at 2026-10-25 06:36:13.009857
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

# Generated at 2026-10-25 06:36:15.671487
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:18.243073
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:20.660414
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:23.073486
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:25.598340
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:28.292740
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:30.707901
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:33.122140
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:35.690754
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:38.637743
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:41.051629
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:43.469463
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:45.887728
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:48.302845
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:50.719176
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:53.136578
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:55.552307
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:36:57.967917
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:00.385510
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:02.799597
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:05.243767
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:07.662226
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:10.075904
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:12.493384
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:14.910502
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:17.324435
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:19.744935
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:22.160378
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:24.576274
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:26.993288
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:29.407609
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:31.854798
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:34.238867
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:36.651457
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:39.066861
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:41.499531
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:43.913208
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:46.327622
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:48.742457
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:53.459102
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:55.872434
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:37:58.289308
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:00.701145
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:03.118972
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:05.537291
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:07.950975
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:10.366381
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:12.777967
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:15.192092
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:17.608871
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:20.025978
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:22.442649
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:24.856746
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:27.270941
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:29.687098
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:32.103886
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:34.521829
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:36.936154
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:39.353426
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 06:38:41.769216
# Unit test for method to_lazy of class Either