

# Generated at 2026-10-25 07:54:40.682056
# Unit test for method to_maybe of class Right

# Generated at 2026-10-25 07:54:43.094965
# Unit test for method to_maybe of class Right

# Generated at 2026-10-25 07:54:45.509585
# Unit test for method to_maybe of class Right

# Generated at 2026-10-25 07:54:47.924019
# Unit test for method to_maybe of class Right

# Generated at 2026-10-25 07:54:50.338512
# Unit test for method to_maybe of class Right

# Generated at 2026-10-25 07:54:52.902701
# Unit test for method to_maybe of class Right

# Generated at 2026-10-25 07:54:55.267174
# Unit test for method ap of class Either

# Generated at 2026-10-25 07:54:57.607813
# Unit test for method ap of class Either

# Generated at 2026-10-25 07:55:03.603590
# Unit test for method ap of class Either
def test_Either_ap():result = Right(lambda value: value * 2).ap(Right(3))

# Generated at 2026-10-25 07:55:13.126397
# Unit test for method to_maybe of class Left
def test_Left_to_maybe():
    result = Left("error").to_maybe()

    assert result == Maybe.nothing()
    assert result.is_nothing()

# Generated at 2026-10-25 07:55:20.396061
# Unit test for constructor of class Right

# Generated at 2026-10-25 07:55:27.359507
# Unit test for constructor of class Right
def test_Right():result = Right(42)

# Generated at 2026-10-25 07:55:31.046207
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

# Generated at 2026-10-25 07:55:33.813598
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

# Generated at 2026-10-25 07:55:36.563158
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:55:39.133404
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:55:41.824754
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:55:44.238180
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:55:46.652479
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:55:49.070082
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:55:51.485134
# Unit test for method bind of class Left

# Generated at 2026-10-25 07:55:53.897939
# Unit test for method bind of class Left

# Generated at 2026-10-25 07:55:56.313226
# Unit test for method bind of class Left

# Generated at 2026-10-25 07:55:58.946617
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

# Generated at 2026-10-25 07:56:29.006250
# Unit test for method bind of class Left
def test_Left_bind():
    left = Left("error")
    mapper_called = False

    def mapper(value):
        nonlocal mapper_called
        mapper_called = True
        return Right(value)

    result = left.bind(mapper)

    assert result is left
    assert result == Left("error")
    assert result.value == "error"
    assert result.is_left()
    assert not result.is_right()
    assert mapper_called is False

# Generated at 2026-10-25 07:56:30.439267
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.either import Left, Right

    error_handler = lambda value: 'error: {}'.format(value)
    success_handler = lambda value: 'success: {}'.format(value)

    # Right: success handler is called with the value
    assert Right(42).case(error_handler, success_handler) == 'success: 42'

    # Left: error handler is called with the value
    assert Left('oops').case(error_handler, success_handler) == 'error: oops'

# Generated at 2026-10-25 07:56:32.854690
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:56:35.384220
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:56:38.022084
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:56:40.439242
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:56:42.851334
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:56:45.267694
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:56:47.678896
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:56:50.094168
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:56:52.507977
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:56:54.926578
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:56:57.341624
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:56:59.757115
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:57:02.173218
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:04.586963
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:07.002403
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:09.416787
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:57:11.833446
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:57:14.247262
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:57:16.663059
# Unit test for method __eq__ of class Either

# Generated at 2026-10-25 07:57:19.282422
# Unit test for method __eq__ of class Either
def test_Either___eq__():assert Left(1).__eq__(Left(1)) is True

# Generated at 2026-10-25 07:57:22.043834
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

# Generated at 2026-10-25 07:57:23.403232
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

# Generated at 2026-10-25 07:57:24.727244
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

# Generated at 2026-10-25 07:57:26.055878
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

# Generated at 2026-10-25 07:57:27.457277
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

# Generated at 2026-10-25 07:57:30.291067
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

# Generated at 2026-10-25 07:57:33.014458
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

# Generated at 2026-10-25 07:57:35.876611
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

# Generated at 2026-10-25 07:57:38.662839
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:41.084374
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:43.498696
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:46.075360
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:48.489598
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:50.904642
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:53.319456
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:55.733314
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:57:58.147336
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:00.563184
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:03.014435
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:05.423553
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:07.837817
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:10.267531
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:12.775030
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:15.133827
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:17.550791
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:19.967503
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:22.380595
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:24.793795
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:58:47.344615
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():lazy = Either(42).to_lazy()

# Generated at 2026-10-25 07:58:50.117651
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

# Generated at 2026-10-25 07:58:52.784404
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

# Generated at 2026-10-25 07:58:55.495055
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

# Generated at 2026-10-25 07:58:58.227004
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:00.762983
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:03.176258
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:05.712173
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:08.127365
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:10.541586
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:12.955211
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:15.593668
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:18.080661
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:20.468563
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:22.893091
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:25.468909
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:27.883508
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:30.298399
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:32.711568
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:35.127902
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:37.541565
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:39.955493
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:42.370088
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:44.827836
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:47.299655
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:49.713960
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:52.132154
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:54.543881
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:56.961292
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 07:59:59.375675
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:01.791979
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:04.207730
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:06.623437
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:09.038679
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:11.533996
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:13.962908
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:16.373393
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:18.789263
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:21.202256
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:23.625121
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:26.034966
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:44.000848
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():from pymonet.lazy import Lazy

# Generated at 2026-10-25 08:00:46.745945
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

# Generated at 2026-10-25 08:00:49.614613
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

# Generated at 2026-10-25 08:00:52.482804
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

# Generated at 2026-10-25 08:00:55.128364
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:00:57.667322
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:00.267797
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:02.678639
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:05.093349
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:07.606071
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:10.008504
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:12.423860
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:14.837492
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:17.251710
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:19.666488
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:22.080332
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:24.493793
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:26.907934
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:29.340283
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:31.752667
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:34.164308
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:36.579729
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:38.995118
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:41.408307
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:43.823842
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:46.236115
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:48.651118
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:51.065109
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:01:53.682967
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

# Generated at 2026-10-25 08:01:56.580915
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

# Generated at 2026-10-25 08:01:59.537426
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

# Generated at 2026-10-25 08:02:02.422898
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

# Generated at 2026-10-25 08:02:05.287564
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

# Generated at 2026-10-25 08:02:08.261115
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

# Generated at 2026-10-25 08:02:11.125110
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

# Generated at 2026-10-25 08:02:13.992163
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

# Generated at 2026-10-25 08:02:16.771837
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

# Generated at 2026-10-25 08:02:19.649090
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

# Generated at 2026-10-25 08:02:22.397675
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

# Generated at 2026-10-25 08:02:24.921299
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:27.605982
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:30.019237
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:32.433110
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:34.846961
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:37.261732
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:40.622437
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:43.035865
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:45.450687
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:47.868345
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:50.278174
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:52.692523
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:02:55.106473
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:16.981087
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():either = Right(42)

# Generated at 2026-10-25 08:03:19.945023
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

# Generated at 2026-10-25 08:03:22.778619
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

# Generated at 2026-10-25 08:03:25.562489
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

# Generated at 2026-10-25 08:03:28.289847
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

# Generated at 2026-10-25 08:03:31.201440
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

# Generated at 2026-10-25 08:03:33.741338
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:36.333974
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:38.751325
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:41.686178
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:44.102112
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:46.514204
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:52.141292
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:54.559128
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:56.968653
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:03:59.893402
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

# Generated at 2026-10-25 08:04:02.714917
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

# Generated at 2026-10-25 08:04:05.607694
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

# Generated at 2026-10-25 08:04:08.482046
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

# Generated at 2026-10-25 08:04:11.241389
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

# Generated at 2026-10-25 08:04:14.001702
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

# Generated at 2026-10-25 08:04:16.872169
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

# Generated at 2026-10-25 08:04:19.649038
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

# Generated at 2026-10-25 08:04:22.413400
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:04:24.944871
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:04:27.358682
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:04:38.042236
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:04:40.527703
# Unit test for method to_lazy of class Either

# Generated at 2026-10-25 08:04:42.934901
# Unit test for method to_lazy of class Either