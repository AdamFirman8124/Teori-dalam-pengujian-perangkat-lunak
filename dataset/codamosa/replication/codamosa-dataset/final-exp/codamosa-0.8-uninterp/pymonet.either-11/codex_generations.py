

# Generated at 2022-06-14 03:16:42.412798
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)
    assert Right(1) != 2


# Generated at 2022-06-14 03:16:45.844376
# Unit test for method __eq__ of class Either
def test_Either___eq__():

    class LeftClass(Left[T]):
        pass

    class RightClass(Right[T]):
        pass

    assert LeftClass("left") == LeftClass("left")
    assert LeftClass("left") != RightClass("left")
    assert LeftClass("left") != RightClass("right")
    assert LeftClass("left") != "left"

    assert RightClass("right") == RightClass("right")
    assert RightClass("right") != LeftClass("right")
    assert RightClass("right") != LeftClass("left")
    assert RightClass("right") != "right"



# Generated at 2022-06-14 03:16:50.723486
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:16:53.827129
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    eith = Either.unit(1)
    assert eith.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:16:57.245451
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(3) == Left(3)
    assert Right('a') == Right('a')
    assert Right(Left(3)) == Right(Left(3))
    assert Left(Right(3)) == Left(Right(3))



# Generated at 2022-06-14 03:17:11.313904
# Unit test for method __eq__ of class Either
def test_Either___eq__():

    assert Left(5) == Left(5)
    assert Right(5) == Right(5)
    assert Left(5) != Left(6)
    assert Left(5) != Right(5)
    assert Right(5) != Left(5)


# Unit tests for method case of class Either

# Generated at 2022-06-14 03:17:22.800349
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.either import Left
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Left(1) == Left(1)
    assert not Left(1) == Left(2)
    assert not Left(1) == Right(1)

    assert Right(1) == Right(1)
    assert not Right(1) == Right(2)
    assert not Right(1) == Left(1)

    assert Left(1) == Box(1)
    assert not Left(1) == Box(2)

    assert Left(1) == Try(1, False)
    assert not Left(1) == Try(2, False)


# Generated at 2022-06-14 03:17:29.434156
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(2) == Right(2)
    assert Left(2) == Left(2)
    assert Right(2) != Left(2)
    assert Right(2) != Right(3)
    assert Left(2) != Left(3)
    assert Left(2) != Right(2)

# Generated at 2022-06-14 03:17:35.624903
# Unit test for method case of class Either
def test_Either_case():
    def is_zero(x):
        if x == 0:
            return True
        return False

    def negative(x):
        return -x

    assert Right(10).case(is_zero, negative) == -10
    assert Left(-10).case(is_zero, negative) == False


# Generated at 2022-06-14 03:17:40.118734
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    a = Right(5)
    b = Right(5)
    assert a == b

    a = Right(5)
    b = Left(5)
    assert a != b

    a = Left(5)
    b = Left(5)
    assert a == b



# Generated at 2022-06-14 03:17:52.877244
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_either import Right
    from pymonet.monad_either import Left
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    assert isinstance(Right(1).to_lazy(), Lazy)
    assert isinstance(Left('bad').to_lazy(), Lazy)
    assert Right(1).to_lazy().is_value_computed() == False
    assert Left('bad').to_lazy().is_value_computed() == False
    assert Right(1).to_lazy().force() == 1
    assert Left('bad').to_lazy().force() == 'bad'

# Generated at 2022-06-14 03:18:06.521059
# Unit test for method to_lazy of class Either
def test_Either_to_lazy(): 
    def is_right(v):
        return isinstance(v, (Right,))
    def is_left(v):
        return isinstance(v, (Left,))
    v = 1
    assert (Either(v).to_lazy().get() == v)
    v = "1"
    assert (Either(v).to_lazy().get() == v)
    v = 2.0
    assert (Either(v).to_lazy().get() == v)
    v = ()
    assert (Either(v).to_lazy().get() == v)
    v = []
    assert (Either(v).to_lazy().get() == v)
    v = {}
    assert (Either(v).to_lazy().get() == v)
    v = set()

# Generated at 2022-06-14 03:18:16.636039
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Left(1).to_lazy()
    assert Right(1).to_lazy() == Right(1).to_lazy()
    assert repr(Left(1).to_lazy()) == repr(Left(1).to_lazy())
    assert repr(Right(1).to_lazy()) == repr(Right(1).to_lazy())
    assert str(Left(1).to_lazy()) == str(Left(1).to_lazy())
    assert str(Right(1).to_lazy()) == str(Right(1).to_lazy())


# Generated at 2022-06-14 03:18:19.145495
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Either.to_lazy(None) == None
    assert Left(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:18:22.511293
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:18:27.798972
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    GIVEN: Either and callable function
    WHEN: call to_lazy
    THEN: Lazy with previous value must be returned
    """
    def func():
        return 5
    assert Either(5).to_lazy() == Lazy(func)
    assert Either('str').to_lazy() == Lazy(lambda: 'str')


# Generated at 2022-06-14 03:18:30.412939
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    assert Right(True).to_lazy().evaluate() is True
    assert Left(False).to_lazy().evaluate() is False


# Generated at 2022-06-14 03:18:33.397987
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Right(4).to_lazy(), Lazy)

# Generated at 2022-06-14 03:18:48.706993
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:18:51.200127
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(lambda x: x + 10).to_lazy() == Left(lambda x: x + 10).to_lazy()


# Generated at 2022-06-14 03:18:56.820818
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left('Error').to_lazy() == Lazy(lambda: 'Error')


# Generated at 2022-06-14 03:19:00.021545
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def _fail():
        raise Exception('fail')

    def _ok():
        return 'ok'
    assert Lazy(_fail) == Left('fail').to_lazy()
    assert Lazy(_ok) == Right('ok').to_lazy()



# Generated at 2022-06-14 03:19:02.096187
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().get() == 1
    assert Left('error').to_lazy().get() == 'error'


# Generated at 2022-06-14 03:19:05.909566
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('message').to_lazy() == Lazy(lambda: 'message')
    assert Right('message').to_lazy() == Lazy(lambda: 'message')



# Generated at 2022-06-14 03:19:25.202157
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(2).to_lazy() == Lazy(lambda: 2)
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() != Lazy(lambda: 2)
    assert Right(1).to_lazy() != Lazy(lambda: 2)
    assert Right(1).to_lazy().bind(lambda x: x*2) == Lazy(lambda: 2)
    assert Left(1).to_lazy().bind(lambda x: x*2) == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:37.480933
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(10).to_lazy() == Lazy(lambda: 10)
    assert Right(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:19:40.135972
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Either(None).to_lazy(), Lazy)


# Generated at 2022-06-14 03:19:42.901244
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(23).to_lazy().force() == 23
    assert Right(23).to_lazy().force() == 23


# Generated at 2022-06-14 03:19:46.757573
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    # test Left to_lazy
    assert Left(1).to_lazy().evaluate() == 1

    # test Left to_lazy
    assert Right('a').to_lazy().evaluate() == 'a'



# Generated at 2022-06-14 03:19:49.073659
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().evaluate() == 1
    assert Left(1).to_lazy().evaluate() == 1


# Generated at 2022-06-14 03:19:58.092430
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(22).to_lazy() == Lazy(lambda: 22)


# Generated at 2022-06-14 03:20:02.462238
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left(1)
    right = Right(1)

    assert left.to_lazy() == Lazy(lambda: 1)
    assert right.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:20:10.734738
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monoid import Sum
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.functors import Functor

    def add3(num):
        return Sum(num + 3)

    assert Functor.fmap(add3, Right(Sum(1))) == Right(Sum(4))
    assert Functor.fmap(add3, Left(Sum(1))) == Left(Sum(1))
    assert Functor.fmap(add3, Right(Sum(1)).to_lazy()) == Lazy(lambda: Sum(4))
    assert Functor.fmap(add3, Left(Sum(1)).to_lazy()) == Lazy(lambda: Sum(1))



# Generated at 2022-06-14 03:20:22.438674
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation, Success, Fail
    from pymonet.lazy import Lazy

    # Box monad
    box = Box(3)
    lazy_box = box.to_lazy()
    assert lazy_box.get() == 3

    # Try monad
    try_success = Try(3)
    lazy_try_success = try_success.to_lazy()
    assert lazy_try_success.get() == 3

    try_fail = Try('')  # will be treated as failed try
    lazy_try_fail = try_fail.to_lazy()
    assert lazy_try_fail.get() == ''

    # Maybe monad


# Generated at 2022-06-14 03:20:25.289335
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert (Left(1).to_lazy()).value() == 1
    assert (Right(-1).to_lazy()).value() == -1



# Generated at 2022-06-14 03:20:34.036816
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    unit test for method to_lazy of class Either
    """
    # given
    value = "some value"
    either = Right(value)

    # when
    lazy = either.to_lazy()

    # then
    assert isinstance(lazy, Lazy)
    assert value == lazy.force_value()


# Generated at 2022-06-14 03:20:39.926124
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    from pymonet.lazy import Lazy

    # test for Left
    result = Left(1).to_lazy()

    assert isinstance(result, Lazy)
    assert result.value() == 1

    # test for Right
    result = Right(2).to_lazy()

    assert isinstance(result, Lazy)
    assert result.value() == 2



# Generated at 2022-06-14 03:20:45.811810
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Lazy(lambda: 'test') == Right(Lazy(lambda: 'test')).to_lazy()



# Generated at 2022-06-14 03:20:49.710578
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Either.to_lazy(Left("test")), Lazy)
    assert isinstance(Either.to_lazy(Right("test")), Lazy)


# Generated at 2022-06-14 03:20:54.317755
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    >>> test_Either_to_lazy()
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Lazy(lambda: 2)
    assert Lazy(lambda: 2) != Lazy(lambda: 3)



# Generated at 2022-06-14 03:21:02.819833
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:21:04.754910
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(42).to_lazy().force() == 42
    assert Left(42).to_lazy().force() == 42



# Generated at 2022-06-14 03:21:08.593136
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right("abc").to_lazy().value() == "abc"


# Generated at 2022-06-14 03:21:13.687819
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_right = Either.right(10).to_lazy()
    lazy_left = Either.left(10).to_lazy()

    assert isinstance(lazy_right, Lazy)
    assert isinstance(lazy_left, Lazy)

    assert lazy_right.value() == 10
    assert lazy_left.value() == 10


# Generated at 2022-06-14 03:21:16.743829
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_test():
        return 2

    assert Right(2).to_lazy() == Lazy(lazy_test)
    assert Left(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:21:20.960218
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    def error_handler(value):
        return value

    def success_handler(value):
        return value

    # Test: Right value
    assert Right(1).case(error_handler, success_handler) == 1
    assert Right(1).to_lazy().evaluate() == 1

    # Test: Left value
    assert Left(2).case(error_handler, success_handler) == 2
    assert Left(2).to_lazy().evaluate() == 2

# Generated at 2022-06-14 03:21:23.687271
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # when
    result = Either.to_lazy(Right(1))

    # then
    assert result == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:28.162079
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Right([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])


# Generated at 2022-06-14 03:21:31.890481
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(2).to_lazy(), Lazy)
    assert Right(2).to_lazy()() == 2
    assert isinstance(Left(2).to_lazy(), Lazy)
    assert Left(2).to_lazy()() == 2


# Generated at 2022-06-14 03:21:33.617824
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:21:44.813288
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    either_right = Right("right")
    assert either_right.to_lazy() == Lazy(lambda: "right")
    assert either_right.to_lazy().get() == "right"

    either_left = Left("left")
    assert either_left.to_lazy() == Lazy(lambda: "left")
    assert either_left.to_lazy().get() == "left"


# Generated at 2022-06-14 03:21:53.911842
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Test on Left
    val1 = Lazy(lambda: 1)
    res1 = Left(val1).to_lazy()
    assert res1.value() == val1.value()
    # Test on Right
    val2 = Lazy(lambda: 2)
    res2 = Right(val2).to_lazy()
    assert res2.value() == val2.value()


# Generated at 2022-06-14 03:21:57.066764
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:22:03.462531
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    lazy_3 = Either.Right(3).to_lazy()
    assert isinstance(lazy_3, Lazy)
    assert lazy_3.force() == 3

    lazy_5 = Either.Left(5).to_lazy()
    assert isinstance(lazy_5, Lazy)
    assert lazy_5.force() == 5



# Generated at 2022-06-14 03:22:06.921688
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5) == Left(5).to_lazy()
    assert Lazy(lambda: 'toto') == Right('toto').to_lazy()


# Generated at 2022-06-14 03:22:08.663388
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'right') == Right('right').to_lazy()
    assert Lazy(lambda: 'left') == Left('left').to_lazy()



# Generated at 2022-06-14 03:22:10.961421
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:22:15.810542
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_value(x):
        def value():
            return x()
        return Lazy(value)

    assert lazy_value(Right(5)) == Right(5).to_lazy() == Lazy(lambda: 5)
    assert lazy_value(Left("error")) == Left("error").to_lazy() == Lazy(lambda: "error")

# Unit tests for method case of class Either

# Generated at 2022-06-14 03:22:18.598028
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(10)
    left = Left(10)

    assert right.to_lazy() == Lazy(lambda: 10)
    assert left.to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:22:26.011991
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.validation import Validation
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:22:42.527872
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    result = Right(4).to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == 4
    result = Left("error").to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == "error"


# Generated at 2022-06-14 03:22:50.214921
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.tuple import Tuple2
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Right(Tuple2(5, 3)).to_lazy() == Lazy(lambda: Tuple2(5, 3))
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:22:57.099498
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert (Right(10).to_lazy()).run() == 10
    assert (Left(10).to_lazy()).run() == 10

    assert (Right(Lazy(Box(10))).to_lazy()).run() == Lazy(Box(10))
    assert (Left(Lazy(Box(10))).to_lazy()).run() == Lazy(Box(10))

    assert (Right(Lazy(Try(10, is_success=True))).to_lazy()).run() == Lazy(Try(10, is_success=True))
    assert (Left(Lazy(Try(10, is_success=True))).to_lazy()).run

# Generated at 2022-06-14 03:23:01.022482
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Either(None).to_lazy(), Lazy)



# Generated at 2022-06-14 03:23:08.141142
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Arrange
    left = Left(10)
    right = Right(20)
    # Act
    result_left = left.to_lazy()
    result_right = right.to_lazy()
    # Assert
    assert isinstance(result_left, Left) is True
    assert isinstance(result_right, Right) is True
    assert result_left.value == 10
    assert result_right.value == 20


# Generated at 2022-06-14 03:23:10.889202
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    result = Right(5).to_lazy()
    assert result.get() == 5
    result = Left(5).to_lazy()
    assert result.get() == 5

# Generated at 2022-06-14 03:23:13.322401
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Right(1)) == Lazy(lambda: 1)
    assert Either.to_lazy(Left(1)) == Lazy(lambda: 1)



# Generated at 2022-06-14 03:23:22.983011
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Make sure that method to_lazy of class Either returns Lazy monad with None value for Left
    and with previous value for Right.
    """
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert Left(None).to_lazy() == Lazy(None)
    assert Right(1).to_lazy() == Lazy(1)



# Generated at 2022-06-14 03:23:26.358261
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def value() -> str:
        return 'test'

    def error() -> str:
        return 'test'

    assert Right('test').to_lazy().value()() == 'test'
    assert Left('test').to_lazy().value()() == 'test'



# Generated at 2022-06-14 03:23:30.250867
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    assert Right(5).to_lazy().get_value() == 5
    assert Left(5).to_lazy().get_value() == 5

    with pytest.raises(TypeError):
        assert Left(5).to_lazy().get_value(6)


# Generated at 2022-06-14 03:23:58.467101
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Right(1).to_lazy().value() == 1)
    assert(Left(1).to_lazy().value() == 1)

# Generated at 2022-06-14 03:24:02.224509
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a') == Either[str].to_lazy()(Right('a'))
    assert Lazy(lambda: 'b') == Either[str].to_lazy()(Left('b'))

# Generated at 2022-06-14 03:24:03.930806
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(2).to_lazy().force() == 2
    assert Right(2).to_lazy().force() == 2


# Generated at 2022-06-14 03:24:06.591842
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:24:10.109847
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_instance = Right(1).to_lazy()
    assert lazy_instance.value() == 1

    lazy_instance = Left("error").to_lazy()
    assert lazy_instance.value() == "error"



# Generated at 2022-06-14 03:24:12.881361
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:24:24.169050
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # Case to return Box
    either = Either(0)
    box = either.to_box()

    assert isinstance(box, Box)
    assert box.value == either.value

    # Case to return Try
    either = Either(0)
    try_monad = either.to_try()

    assert isinstance(try_monad, Try)
    assert try_monad.is_success == either.is_right()
    assert try_monad.value == either.value

    # Case to return Lazy
    either = Either(0)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.evaluate() == either

# Generated at 2022-06-14 03:24:25.984706
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:24:27.755489
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:24:30.902641
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:25:33.147255
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Right(1)).force() == 1
    assert isinstance(Either.to_lazy(Right(1)), Lazy)



# Generated at 2022-06-14 03:25:40.053706
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test if Either.to_lazy() return Lazy with the same value.

    :returns: exception if test fails
    :rtype: Exception
    """
    from pymonet.lazy import Lazy

    def test1():
        def func():
            return 'value1'

        return Lazy(func)

    assert Right('value1').to_lazy() == test1()
    assert Left('value1').to_lazy() == test1()



# Generated at 2022-06-14 03:25:42.724710
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)

    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:25:47.190548
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.eith import Left, Right

    assert Right(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: 1)
    assert Left(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:25:49.543883
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left('err')).value() == 'err'
    assert Either.to_lazy(Right('value')).value() == 'value'


# Generated at 2022-06-14 03:26:01.426183
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    assert isinstance(Right(10).to_lazy(), Lazy)
    assert isinstance(Left(10).to_lazy(), Lazy)
    assert isinstance(Right(10).to_lazy(), Functor)
    assert isinstance(Left(10).to_lazy(), Functor)
    assert Functor.fmap(lambda value: value + 10, Right(10).to_lazy()) == Functor.fmap(lambda value: value + 10, Lazy(lambda: 10))
    assert Functor.fmap(lambda value: value + 10, Left(10).to_lazy()) == Functor.fmap(lambda value: value + 10, Lazy(lambda: 10))


# Generated at 2022-06-14 03:26:02.943368
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:26:07.702531
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:26:09.953745
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Lazy(lambda: 1) == Either('whatever').to_lazy

# Generated at 2022-06-14 03:26:14.264223
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Either(1).to_lazy().value() == Lazy(lambda: 1).value()
    assert Either(Maybe.just(1)).to_lazy().value() == Lazy(lambda: Maybe.just(1)).value()

