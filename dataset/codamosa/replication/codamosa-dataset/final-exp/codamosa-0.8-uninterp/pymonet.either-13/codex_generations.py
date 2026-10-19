

# Generated at 2022-06-14 03:16:58.617395
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Right(lambda x: x + 10).to_lazy()

    assert right.get()(10) == 20
    assert Right(10).to_lazy().get() == 10
    assert Left(10).to_lazy().get() == 10
    assert Right(lambda x: x + 10).to_lazy().get()(10) == 20
    assert Right(lambda x: x + 10).to_lazy().get()(10) == 20
    assert Left(lambda x: x + 10).to_lazy().get()(10) == 20
    assert Left(lambda x: x + 10).to_lazy().get()(10) == 20


# Generated at 2022-06-14 03:17:00.897595
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Right(1) != Left(1)



# Generated at 2022-06-14 03:17:06.410072
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.box import Box
    from pymonet.monad_try import Try

    a = Left(1)
    b = Left(1)
    assert a == b
    assert a != Box(1)
    assert a != Try(1, is_success=True)

    a = Right(1)
    b = Right(1)
    assert a == b
    assert a != Box(1)
    assert a != Try(1, is_success=True)



# Generated at 2022-06-14 03:17:15.744902
# Unit test for method case of class Either
def test_Either_case():
    # Given
    left_either = Left(10)
    right_either = Right(11)
    # When
    result_of_left = left_either.case(lambda v: v * 2, lambda v: v * 3)
    result_of_right = right_either.case(lambda v: v * 2, lambda v: v * 3)
    # Then
    assert result_of_left == 20
    assert result_of_right == 33

# Generated at 2022-06-14 03:17:21.357138
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.t_lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1) == Try(1).to_lazy() == Right(1).to_lazy() == Left(1).to_lazy()


# Generated at 2022-06-14 03:17:29.198037
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1), "Should be equal"
    assert Left(2) == Left(2), "Should be equal"
    assert not Right(1) == Left(1), "Shouldn't be equal"
    assert not Left(1) == Right(1), "Shouldn't be equal"


# Generated at 2022-06-14 03:17:34.384958
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(2) == Left(2)
    assert Left(2) != Left("2")
    assert Left(2) == Right("2")
    assert Right("2") == Right("2")
    assert Right("2") != Right(2)
    assert Right("2") != Left("2")



# Generated at 2022-06-14 03:17:39.442805
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert not(Right(1) == Right(2))
    assert not(Left(1) == Left(2))
    assert not(Left(1) == Right(1))
    assert not(Left(1) == Right(2))
    assert not(Right(1) == Left(1))
    assert not(Right(2) == Left(1))


# Generated at 2022-06-14 03:17:42.553448
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert not Either(3) == Either(3)
    assert Left(3) == Left(3)
    assert Right(2) == Right(2)
    assert not Right(2) == Left(3)



# Generated at 2022-06-14 03:17:48.931160
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Given
    left = Left("left")
    right = Right("right")

    # When
    eq1 = left == right
    eq2 = right == right
    eq3 = left == left

    # Then
    assert eq1 is False
    assert eq2 is True
    assert eq3 is True


# Generated at 2022-06-14 03:17:54.271031
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    def identity(x): return x

    lazy_either = Either(Maybe.just(10)).to_lazy()
    assert isinstance(lazy_either, Lazy)
    assert lazy_either.apply(identity) == Maybe.just(10)

# Generated at 2022-06-14 03:17:57.711085
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either."""
    assert Right(1).to_lazy().eval() == Left(1).to_lazy().eval() == 1


# Generated at 2022-06-14 03:18:02.614005
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Either.to_lazy()
    (Either[A] -> Lazy[Function() -> A])
    """
    v = Left(2).to_lazy()
    assert isinstance(v, Lazy)
    assert v.get() == 2


# Generated at 2022-06-14 03:18:05.276213
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy().value() == 2
    assert Left("e").to_lazy().value() == "e"


# Generated at 2022-06-14 03:18:11.139835
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    a = Right(2).to_lazy()
    b = Left(2).to_lazy()

    assert isinstance(a, Lazy)
    assert isinstance(b, Lazy)
    assert a.value() == 2
    assert b.value() == 2


# Generated at 2022-06-14 03:18:13.767093
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy().__class__.__name__ == 'Lazy'

# Generated at 2022-06-14 03:18:19.429103
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    :returns: True if test passed, false if not
    :rtype: Boolean
    """
    from pymonet.lazy import Lazy

    x = Left(1)
    assert x.to_lazy() == Lazy(lambda: 1), 'Incorrect result of to_lazy in class Maybe'

    x = Right(1)
    assert x.to_lazy() == Lazy(lambda: 1), 'Incorrect result of to_lazy in class Maybe'

    return True


# Generated at 2022-06-14 03:18:22.416253
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Left(1).to_lazy().value()() == 1)
    assert(Right(1).to_lazy().value()() == 1)

# Generated at 2022-06-14 03:18:24.956248
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left(None)).evaluate() == None
    assert Either.to_lazy(Right(1)).evaluate() == 1



# Generated at 2022-06-14 03:18:26.941602
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left(None)) == Either.to_lazy(Right(None))


# Generated at 2022-06-14 03:18:30.449588
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left("error").to_lazy().__value__() == "error"
    assert Right("success").to_lazy().__value__() == "success"



# Generated at 2022-06-14 03:18:35.302472
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(6).to_lazy() == Lazy(lambda: 6)
    assert Left('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 03:18:37.767588
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().get == 1
    assert Right(2).to_lazy().get == 2


# Generated at 2022-06-14 03:18:40.583266
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    l = Either.Left("left")
    r = Either.Right("right")
    assert l.to_lazy().evaluate() == "left"
    assert r.to_lazy().evaluate() == "right"

# Generated at 2022-06-14 03:18:48.785068
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_to_lazy = Right(10).to_lazy()
    left_to_lazy = Left(10).to_lazy()
    assert right_to_lazy.is_forced() is False and right_to_lazy.value == 10
    assert left_to_lazy.is_forced() is False and left_to_lazy.value == 10


# Generated at 2022-06-14 03:18:50.466169
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def f():
        return 'Hello'
    assert Right(f).to_lazy() == Right(f)

# Generated at 2022-06-14 03:19:09.437827
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Right(1).to_lazy().value() == 1)

# Generated at 2022-06-14 03:19:14.082537
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test Either to_lazy function"""
    value = 9
    right = Right(value)
    lazy = right.to_lazy()
    assert lazy.value() == value
    left = Left(value)
    lazy = left.to_lazy()
    assert lazy.value() == value


# Generated at 2022-06-14 03:19:16.229927
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy().get() == 10
    assert Right(10).to_lazy().get() == 10


# Generated at 2022-06-14 03:19:19.242311
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('Error').to_lazy() == Lazy(lambda: 'Error')
    assert Right('Success').to_lazy() == Lazy(lambda: 'Success')


# Unit tests for method to_try of class Either

# Generated at 2022-06-14 03:19:25.754436
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:19:28.636396
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().force() == 1
    assert Right(1).to_lazy().force() == 1


# Generated at 2022-06-14 03:19:35.479373
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Perform unit test for method to_lazy of class Either.

    :returns: None
    :raises: AssertionError if test is failed
    """

    def _to_lazy_right():
        return Right(5)

    def _to_lazy_left():
        return Left(5)

    assert _to_lazy_right().to_lazy().value() == 5
    assert _to_lazy_left().to_lazy().value() == 5



# Generated at 2022-06-14 03:19:38.952899
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(10).to_lazy().value() == 10
    assert Left(10).to_lazy().value() == 10



# Generated at 2022-06-14 03:19:41.639297
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def to_lazy():
        return Right("a").to_lazy().get()

    assert to_lazy() == "a"



# Generated at 2022-06-14 03:19:47.676901
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def test_case(x):
        return x + 10

    assert Left(1).to_lazy().force() == 1
    assert Right(1).to_lazy().force() == 1
    assert Left(test_case).to_lazy().force()(10) == 10
    assert Right(test_case).to_lazy().force()(10) == 20



# Generated at 2022-06-14 03:19:49.687867
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """
    assert Right(3).to_lazy().force() == 3
    assert Left(3).to_lazy().force() == 3


# Generated at 2022-06-14 03:19:56.858722
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1
    assert Lazy(lambda: 1) == Right(1).to_lazy()
    assert Lazy(lambda: 1) == Left(1).to_lazy()


# Generated at 2022-06-14 03:20:00.074984
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Given
    either = Right(1)

    # When
    lazy = either.to_lazy()

    # Then
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1



# Generated at 2022-06-14 03:20:03.961794
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either = Left(1)
    assert either.to_lazy() is not None
    assert type(either.to_lazy()) == Lazy
    assert either.to_lazy().value() == 1

    either = Right(1)
    assert either.to_lazy() is not None
    assert type(either.to_lazy()) == Lazy
    assert either.to_lazy().value() == 1



# Generated at 2022-06-14 03:20:08.669845
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy() == Lazy(lambda: 10)
    assert Right(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:20:12.497014
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(0).to_lazy().force() == 0
    assert Right(1).to_lazy().force() == 1


# Generated at 2022-06-14 03:20:24.306339
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from operator import add
    from pymonet.either import Either, Left, Right

    def test_Either_to_lazy_should_transform_Left_to_Lazy_containing_function_returning_None():
        # Given
        either = Left[int]("error")

        # When
        lazy = either.to_lazy()

        # Then
        assert isinstance(lazy, Lazy)
        assert lazy.value == either.value

    def test_Either_to_lazy_should_transform_Right_to_Lazy_containing_function_returning_previous_value():
        # Given
        either = Right[int](1)

        # When
        lazy = either.to_lazy()

        # Then
        assert isinstance(lazy, Lazy)

# Generated at 2022-06-14 03:20:33.568920
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def test_value():
        test_value.times_called += 1
        return "data"

    test_value.times_called = 0

    right_lazy = Right(test_value).to_lazy()
    assert isinstance(right_lazy, Lazy)
    assert test_value.times_called == 0
    assert right_lazy.value == "data"
    assert test_value.times_called == 1

    left_lazy = Left(test_value).to_lazy()
    assert isinstance(left_lazy, Lazy)
    assert test_value.times_called == 1
    assert left_lazy.value == "data"
    assert test_value.times_called == 2


# Generated at 2022-06-14 03:20:36.494247
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:20:40.603504
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def assert_lazy_resolves_to(expected_value, lazy):
        assert lazy.f() == expected_value

    assert_lazy_resolves_to(10, Left(10).to_lazy())
    assert_lazy_resolves_to(20, Right(20).to_lazy())

# Unit tests for method either of class Either

# Generated at 2022-06-14 03:20:43.146914
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy = Either(3).to_lazy()
    assert lazy.value() == 3


# Generated at 2022-06-14 03:20:45.711107
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:20:58.175436
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy as L

    def f_1(x: int, y: int) -> int:
        return x * y

    def f_2(x: str) -> int:
        return int(x)

    def f_3(x: int, y: int, z: int) -> int:
        return x + y + z

    assert Right(1).to_lazy() == L.Lazy(lambda: 1)
    assert Left(1).to_lazy() == L.Lazy(lambda: 1)
    assert Right(f_1).to_lazy() == L.Lazy(lambda: f_1)
    assert Left(f_1).to_lazy() == L.Lazy(lambda: f_1)

# Generated at 2022-06-14 03:21:02.257309
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Test for function to_lazy of class Either
    from pymonet.lazy import Lazy

    assert Left(10).to_lazy() == Lazy(lambda: 10)
    assert Right(20).to_lazy() == Lazy(lambda: 20)



# Generated at 2022-06-14 03:21:08.624608
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(2).to_lazy().value() == 2


# Generated at 2022-06-14 03:21:14.416475
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    def callback(value):
        return value

    right = Right(callback)
    lazy = right.to_lazy()
    assert isinstance(lazy.value(), Lazy)
    assert lazy.value()(1) == 1

    left = Left(callback)
    lazy = left.to_lazy()
    assert isinstance(lazy.value(), Lazy)
    assert lazy.value()(1) == 1


# Generated at 2022-06-14 03:21:17.611197
# Unit test for method to_lazy of class Either
def test_Either_to_lazy(): # pylint: disable=invalid-name
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1) # pylint: disable=comparison-with-callable


# Generated at 2022-06-14 03:21:19.407917
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    expected_value = 'test value'
    either = Right(expected_value)
    # WHEN
    lazy = either.to_lazy()
    # THEN
    assert lazy.get() == expected_value


# Generated at 2022-06-14 03:21:23.974970
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left('error').to_lazy() == Lazy(lambda: 'error')


# Generated at 2022-06-14 03:21:28.981206
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    start = Lazy(lambda: Box(1))
    end = start.map(lambda x: lambda: x).value()
    result = end()
    assert isinstance(result, Box)
    assert result.value == 1

# Generated at 2022-06-14 03:21:38.048262
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Left('failure').to_lazy() == Lazy(lambda: 'failure')
    assert Right('success').to_lazy() == Lazy(lambda: 'success')
    assert Right(Try(1)).to_box() == Box(Try(1, is_success=True))
    assert Left(Try(1)).to_box() == Box(Try(1, is_success=False))
    assert Right(Box(1)).to_try() == Try(Box(1), is_success=True)
    assert Left(Box(1)).to_try() == Try(Box(1), is_success=False)


# Generated at 2022-06-14 03:21:43.121486
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.function import Function

    for i in range(1, 1000):
        assert Either[int](i).to_lazy() == Lazy(Function(i))
    else:
        assert Either[int](i).to_lazy() is not Lazy(Function(i))

# Generated at 2022-06-14 03:21:44.898907
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Either(2).to_lazy()


# Generated at 2022-06-14 03:21:47.012168
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left("a").to_lazy() == Lazy("a")
    assert Right("a").to_lazy() == Lazy("a")



# Generated at 2022-06-14 03:21:59.083722
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    right = Lazy(lambda: Try(9))
    other_right = right.flat_map(lambda x: Lazy(lambda: Try(x+1)))
    assert Either.to_lazy(Either.to_lazy(Either.to_lazy(right))) == right
    assert Either.to_lazy(Either.to_lazy(other_right)) == other_right


# Generated at 2022-06-14 03:22:03.370900
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 55) == Right(55).to_lazy()
    assert Lazy(lambda: 55) == Left(55).to_lazy()


# Unit tests for method ap of class Either

# Generated at 2022-06-14 03:22:13.517307
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy
    from pymonet.either import Right, Left

    try:
        from pymonet.box import Box
        from pymonet.monad_try import Try
    except:
        pass

    # Test for class Either
    assert Right('value').to_lazy() == pymonet.lazy.Lazy(lambda: 'value')
    assert Left('value').to_lazy() == pymonet.lazy.Lazy(lambda: 'value')
    assert Right(['value', 'another value']).to_lazy() == pymonet.lazy.Lazy(lambda: ['value', 'another value'])

    # Test for class Box

# Generated at 2022-06-14 03:22:19.378352
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def test_function():
        return 42

    from pymonet.lazy import Lazy

    assert Left(42).to_lazy() == Lazy(lambda: 42)
    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left(test_function).to_lazy() == Lazy(lambda: test_function)
    assert Right(test_function).to_lazy() == Lazy(lambda: test_function)
    assert Left(42).to_lazy().value() == 42
    assert Right(42).to_lazy().value() == 42


# Generated at 2022-06-14 03:22:24.178710
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()


# Generated at 2022-06-14 03:22:30.003445
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:22:34.138848
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(7).to_lazy() == Lazy(lambda: 7)
    assert Left(7).to_lazy() == Lazy(lambda: 7)


# Generated at 2022-06-14 03:22:36.938003
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:22:41.130432
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    from pymonet.lazy import Lazy

    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:22:43.991927
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:22:59.621492
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    monad = Either.unit(1)
    lazy = monad.to_lazy()

    assert lazy == Lazy(lambda: 1)



# Generated at 2022-06-14 03:23:05.318261
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    try:
        assert Left(1).to_lazy().value() == 1
        assert Right(1).to_lazy().value() == 1
    except Exception as e:
        print(e)
        raise


# Generated at 2022-06-14 03:23:07.938296
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:23:12.951889
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    Left('test')\
        .ap(Lazy(lambda: Either.to_lazy(Left('test'))).map(lambda x: x.value.value))\
        .to_lazy()\
        .value()\
        .to_lazy()\
        .value()\
        .should.be.eql(Left('test'))


# Generated at 2022-06-14 03:23:21.758873
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet import chain, lazy_to_list
    from pymonet.lazy import Lazy

    assert chain([1, 2, 3]).to_lazy().fmap(lambda value: value * 2).to_list() == lazy_to_list(Lazy(lambda: [1, 2, 3]).fmap(lambda value: value * 2))

# Generated at 2022-06-14 03:23:24.812014
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy()().value == 1
    assert Left(1).to_lazy()().value == 1

# Generated at 2022-06-14 03:23:36.810656
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    try:
        assert Right(10).to_lazy().get() == 10
    except Exception as exc:
        assert False, exc


# Generated at 2022-06-14 03:23:41.035716
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Lazy(lambda: 'foo') == Right('foo').to_lazy()
    assert Lazy(lambda: 'bar') == Left('bar').to_lazy()


# Generated at 2022-06-14 03:23:46.314633
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Either[int](1).to_lazy()
    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1).equals(Right(1).to_lazy())


# Generated at 2022-06-14 03:23:48.716082
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test Either.to_lazy"""

    assert Left(1).to_lazy().value == 1
    assert Right(1).to_lazy().value == 1


# Generated at 2022-06-14 03:24:12.797843
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box

    assert Either(Box(1)).to_lazy().value() == Box(1)

# Generated at 2022-06-14 03:24:18.845198
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy, LazyValue

    def function():
        print('executed')
        return 5

    e = Left(5)
    error_lazy = Lazy(lambda: e)
    assert error_lazy.value == LazyValue.already_resolved
    assert error_lazy.force() is e

    e = Right(5)
    right_lazy = e.to_lazy()
    assert right_lazy.value == LazyValue.not_resolved_yet
    right_lazy = right_lazy.map(function)
    assert right_lazy.value == LazyValue.not_resolved_yet
    assert right_lazy.force() == 5



# Generated at 2022-06-14 03:24:29.760056
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.maybe import Maybe

    assert Lazy(lambda: 'foo') == Either.to_lazy('foo') != Lazy(lambda: None)
    assert Lazy(lambda: 'foo') == Either.to_lazy(Box('foo')) != Lazy(lambda: None)
    assert Lazy(lambda: 'foo') == Either.to_lazy(Try('foo', is_success=True)) != Lazy(lambda: None)
    assert Lazy(lambda: 'foo') == Either.to_lazy(Validation.success('foo')) != Lazy(lambda: None)

# Generated at 2022-06-14 03:24:32.610676
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert "lazy" == Right("lazy").to_lazy().force()
    assert "lazy" == Left("lazy").to_lazy().force()


# Unit tests for method case of class Either

# Generated at 2022-06-14 03:24:34.254534
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert not Left(123).to_lazy().value()
    assert Right(123).to_lazy().value() == 123


# Generated at 2022-06-14 03:24:36.484294
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = Lazy(lambda: 1)
    result = Right(1).to_lazy()
    assert value.force() == result.force()



# Generated at 2022-06-14 03:24:44.692766
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.monad_maybe import Maybe

    value = 'value'
    success = Try(value)
    assert success.is_success()
    assert success.to_lazy() == Lazy(lambda: value)
    assert success.to_lazy().value == value

    error = Try(None, is_success=False)
    assert not error.is_success()
    assert error.to_maybe() == Maybe.nothing()
    assert error.to_maybe().value is None


# Generated at 2022-06-14 03:24:48.887969
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    left_either = Left("value")
    right_either = Right("value")

    assert left_either.to_lazy().value() == "value"
    assert right_either.to_lazy().value() == "value"


# Generated at 2022-06-14 03:24:53.776819
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    :returns: assertion error if method Either.to_lazy doesn't work correct, no error if correct
    :rtype: Exception
    """
    # Create new Either
    either = Right(3)

    # Test to_lazy
    assert either.to_lazy().value() == 3


# Generated at 2022-06-14 03:25:02.511031
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe

    def hello_world(monad):
        return monad.map(lambda name: 'Hello, {}!'.format(name)).case(lambda err: '', identity)

    assert hello_world(Right(Maybe.just('World'))) == 'Hello, World!'
    assert hello_world(Right(Lazy(lambda: Maybe.just('World')))) == 'Hello, World!'
    assert hello_world(Right(Try(Maybe.just('World')).map(lambda value: value.value))) == 'Hello, World!'
    assert hello_world(Right(Try('World').map(lambda value: Maybe.just(value)))) == 'Hello, World!'

# Generated at 2022-06-14 03:26:00.989166
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either = Right(1)
    assert 1 == either.to_lazy().value(), either.to_lazy()


# Generated at 2022-06-14 03:26:03.651424
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 3) == Left(3).to_lazy()
    assert Lazy(lambda: 4) == Right(4).to_lazy()


# Generated at 2022-06-14 03:26:09.466184
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: None)
    assert Left(lazy).to_lazy() == lazy
    assert Right(lazy).to_lazy() == lazy



# Generated at 2022-06-14 03:26:13.366092
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left('error').to_lazy() == Lazy(lambda: 'error')


# Generated at 2022-06-14 03:26:27.964370
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.box import Box

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()

# Generated at 2022-06-14 03:26:30.357791
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right('foo').to_lazy() == Lazy('foo')
    assert Left('foo').to_lazy() == Lazy('foo')


# Generated at 2022-06-14 03:26:32.878695
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Right(1).to_lazy().value() == 1)
    assert(Left('error').to_lazy().value() == 'error')


# Generated at 2022-06-14 03:26:34.764583
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy


# Generated at 2022-06-14 03:26:39.647725
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor
    from pymonet.monoid import Monoid
    from pymonet.utils import is_successful

    def is_empty_lazy(lazy: Lazy[T]) -> bool:
        return not isinstance(lazy, Lazy) or\
            not isinstance(lazy.value, Callable)

    assert is_successf

# Generated at 2022-06-14 03:26:47.979971
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy
    import pymonet.monad_try

    assert isinstance(Either.to_lazy(Right(2)), pymonet.lazy.Lazy)
    assert isinstance(Either.to_lazy(Left("some error")), pymonet.lazy.Lazy)

    assert Either.to_lazy(Right(2)).value() == 2
    assert isinstance(Either.to_lazy(Left("some error")).value(), pymonet.monad_try.Try)
    assert Either.to_lazy(Left("some error")).value().is_success() is False
    assert Either.to_lazy(Left("some error")).value().value() == "some error"
