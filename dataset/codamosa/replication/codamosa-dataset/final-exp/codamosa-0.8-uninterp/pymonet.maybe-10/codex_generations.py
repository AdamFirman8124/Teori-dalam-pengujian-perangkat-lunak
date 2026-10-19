

# Generated at 2022-06-14 03:31:31.564486
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.just(4) != Maybe.just(5)
    assert Maybe.just(4) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(4) != 4


# Generated at 2022-06-14 03:31:34.551144
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:31:39.637915
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def foo():
        return 1

    assert Maybe.just(foo).to_lazy() == Lazy(foo)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:31:46.695973
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Positive case
    maybe_none = Maybe.nothing()
    maybe_none_1 = Maybe.nothing()
    maybe_value = Maybe.just('x')
    assert maybe_none == maybe_none_1
    assert not maybe_value == maybe_none
    assert maybe_value == Maybe.just('x')
    # Negative case
    assert not maybe_value == None
    assert not maybe_value == 'x'


# Generated at 2022-06-14 03:31:50.576184
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:32:00.781051
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Test for equal elements
    a = Maybe.just('123')
    b = Maybe.just('123')
    assert a == b

    a = Maybe.just([1,2,3])
    b = Maybe.just([1,2,3])
    assert a == b

    # Test for different elements
    a = Maybe.just('123')
    b = Maybe.just('321')
    assert not (a == b)

    a = Maybe.just([1,2,3])
    b = Maybe.just([3,2,1])
    assert not (a == b)

    a = Maybe.just([1,2,3])
    b = Maybe.just(123)
    assert not (a == b)


# Generated at 2022-06-14 03:32:09.438296
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:32:16.521943
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    # 1. Test case: method return not empty Lazy
    result = Maybe.just(1).to_lazy()
    assert isinstance(result, Lazy)
    assert isinstance(result.value(), int)
    assert result.value() == 1
    # 2. Test case: method return empty Lazy
    result = Maybe.nothing().to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() is None



# Generated at 2022-06-14 03:32:21.224421
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:26.606506
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert (Maybe.just(5) == Maybe.just(5)) is True
    assert (Maybe.just(5) == Maybe.just(6)) is False
    assert (Maybe.just(5) == Maybe.nothing()) is False
    assert (Maybe.nothing() == Maybe.nothing()) is True


# Generated at 2022-06-14 03:32:36.231088
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    def not_empty_maybe():
        return Maybe[int].just(1)

    def empty_maybe():
        return Maybe[int].nothing()

    assert isinstance(not_empty_maybe().to_lazy(), Lazy)
    assert not_empty_maybe().to_lazy().evaluate(
    ) == 1
    assert isinstance(empty_maybe().to_lazy(), Lazy)
    assert empty_maybe().to_lazy().evaluate() is None


# Generated at 2022-06-14 03:32:43.655135
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def some_function(x):
        return x

    result = Maybe.just(1).filter(some_function(True))
    result2 = Maybe.just(1).filter(some_function(False))
    result3 = Maybe.nothing().filter(some_function(True))
    result4 = Maybe.nothing().filter(some_function(False))
    assert result.value == 1
    assert result2.is_nothing
    assert result3.is_nothing
    assert result4.is_nothing


# Generated at 2022-06-14 03:32:47.240083
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()

# Generated at 2022-06-14 03:32:57.690849
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for Maybe class method __eq__.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.box import Box
    from pymonet.validation import Validation
    from pymonet.monad_try import Try
    from pymonet.io import IO

    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Box(1)
    assert Maybe.just(1) == Validation.success(1)
    assert Maybe.just(1) == Try(1, True)
    assert Maybe.just(1) == IO(lambda: 1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Box(2)
    assert Maybe.just(1) != Validation.success

# Generated at 2022-06-14 03:33:02.326380
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) != Maybe.just(0)
    assert Maybe.just(None) != Maybe.just('string')
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.just(False) != Maybe.nothing()
    assert Maybe.just(0) != Maybe.nothing()
    assert Maybe.just('string') != Maybe.nothing()

# Generated at 2022-06-14 03:33:08.040172
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, True) == Maybe.nothing()
    assert Maybe(1, False) == Maybe.just(1)
    assert Maybe(1, True) != Maybe.just(1)
    assert Maybe(1, False) != Maybe.nothing()
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, True) != Maybe(1, False)


# Generated at 2022-06-14 03:33:17.667573
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    result = Maybe.just("some string") == Maybe.just("some string")
    assert result == True, "test_Maybe___eq__ fail"
    result = Maybe.just("some string") == Maybe.just("some other string")
    assert result == False, "test_Maybe___eq__ fail"
    result = Maybe.nothing() == Maybe.nothing()
    assert result == True, "test_Maybe___eq__ fail"
    result = Maybe.nothing() == Maybe.just("some string")
    assert result == False, "test_Maybe___eq__ fail"
    result = Maybe.just("some string") == Maybe.nothing()
    assert result == False, "test_Maybe___eq__ fail"


# Generated at 2022-06-14 03:33:20.775744
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(5)



# Generated at 2022-06-14 03:33:23.594107
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:26.798304
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(123) == Maybe.just(123)
    assert Maybe.just([1, 2, 3]) == Maybe.just([1, 2, 3])
    assert Maybe.just("1") == Maybe.just("1")
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:33:39.943061
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right
    from pymonet.validation import Validation

    Maybe.just(1).to_lazy() | Try.fmap(lambda x: x + 1) | Try.fmap(lambda x: x + 1) | Try.fmap(lambda x: x + 1) | print
    Maybe.nothing().to_lazy() | Try.fmap(lambda x: x + 1) | Try.fmap(lambda x: x + 1) | Try.fmap(lambda x: x + 1) | print

    print(Maybe.just(1).to_lazy() == Lazy(lambda: 1))

# Generated at 2022-06-14 03:33:44.861713
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert not (Maybe.just(2) == Maybe.nothing())
    assert not (Maybe.nothing() == Maybe.just(2))
    assert not (Maybe.just(2) == Maybe.just(1))


# Generated at 2022-06-14 03:33:53.120912
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(123) == Maybe.just(123)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(123) != Maybe.nothing()
    assert Maybe.just(456) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(123)
    assert Maybe.nothing() != Maybe.just(456)
    assert Maybe.just(45) == Maybe.just(45)
    assert Maybe.just([]) == Maybe.just([])
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(0.123) == Maybe.just(0.123)
    assert Maybe.nothing() == Maybe.nothing()

# Generated at 2022-06-14 03:33:58.304077
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value is not None

    assert Maybe.just(1).filter(filterer) == Maybe.just(1)
    assert Maybe.just(None).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()

# Generated at 2022-06-14 03:34:03.946710
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, False)

    one_maybe = Maybe(1, False)
    one_maybe_copy = Maybe(1, False)
    assert one_maybe == one_maybe_copy

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)

test_Maybe___eq__()



# Generated at 2022-06-14 03:34:09.658378
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just('a')
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)



# Generated at 2022-06-14 03:34:13.432390
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe(2, False).filter(lambda x: x > 1) == Maybe.just(2)


# Generated at 2022-06-14 03:34:16.942595
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != Box(1.1)
    assert Box(1) != Box("1")
    assert Nothing == Nothing


# Generated at 2022-06-14 03:34:19.040849
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, False) != Maybe(1, True)



# Generated at 2022-06-14 03:34:24.291749
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != 1


# Generated at 2022-06-14 03:34:38.940656
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.monad_try import Try

    maybe_just = Maybe.just(1)
    maybe_nothing = Maybe.nothing()
    try_just = Try(1)
    try_nothing = Try(None, is_success=False)

    # False
    assert maybe_just == maybe_nothing
    assert maybe_just == try_nothing
    assert maybe_nothing == maybe_just
    assert maybe_nothing == try_just
    assert maybe_just == None

    # True
    assert maybe_just == Maybe.just(1)
    assert maybe_nothing == Maybe.nothing()
    assert maybe_just == try_just
    assert maybe_nothing == try_nothing


# Generated at 2022-06-14 03:34:44.046612
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value: int) -> bool:
        return value > 2

    maybe = Maybe.just(1)
    assert maybe.filter(filterer).is_nothing

    maybe = Maybe.just(2)
    assert maybe.filter(filterer).is_nothing

    maybe = Maybe.just(3)
    assert maybe.filter(filterer) == Maybe.just(3)


# Generated at 2022-06-14 03:34:47.831395
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:34:50.722968
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.just(None) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:34:54.520314
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x > 1) == Maybe.just(2)
    assert Maybe.just(3).filter(lambda x: x > 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 5) == Maybe.nothing()

# Generated at 2022-06-14 03:35:00.823091
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe.
    """
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()



# Generated at 2022-06-14 03:35:05.894607
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(0).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:35:08.278576
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(42, False).to_lazy() == Lazy(lambda: 42)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:35:16.436890
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # given
    def _resolve(value):
        return isinstance(value, str)

    # when
    result1 = Maybe.just('string').filter(_resolve)
    result2 = Maybe.just(3).filter(_resolve)
    result3 = Maybe.nothing().filter(_resolve)

    # then
    assert result1 == Maybe.just('string')
    assert result2 == Maybe.nothing()
    assert result3 == Maybe.nothing()



# Generated at 2022-06-14 03:35:21.222217
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x < 3) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x < 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 3) == Maybe.nothing()


# Generated at 2022-06-14 03:35:35.309295
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:35:40.160601
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:35:46.562126
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(4) != Maybe.just(5)
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.just(4) != Maybe.nothing()
    assert Maybe.just(4) != 4


# Generated at 2022-06-14 03:35:51.747439
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe(1).filter(lambda x: x < 2) == Maybe(1)
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 0) == Maybe.nothing()


# Generated at 2022-06-14 03:36:02.147154
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Try

    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x == 1).map(lambda x: x + 2) == Maybe.just(3)
    assert Maybe.just(1).filter(lambda x: x == 2).map(lambda x: x + 2) == Maybe.nothing()



# Generated at 2022-06-14 03:36:07.335518
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe(None, True) == Maybe(None, True)
    assert Maybe(10, False) != Maybe(10, True)
    assert Maybe(10, False) != Maybe(11, False)
    assert Maybe(None, True) != Maybe(10, False)


# Generated at 2022-06-14 03:36:11.664639
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(11).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(10).filter(lambda x: x % 2 == 0) == Maybe.just(10)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()
    print("Method test_filter passed!")


# Generated at 2022-06-14 03:36:17.943980
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    import pymonet.lazy as lazy

    assert lazy.Lazy(lambda: 5) == Maybe.just(5).to_lazy()
    assert lazy.Lazy(lambda: None) == Maybe.nothing().to_lazy()

    # __str__
    assert str(lazy.Lazy(lambda: 5)) == str(Maybe.just(5).to_lazy())
    assert str(lazy.Lazy(lambda: None)) == str(Maybe.nothing().to_lazy())

    # __repr__
    assert lazy.Lazy(lambda: 5).__repr__() == Maybe.just(5).to_lazy().__repr__()
    assert lazy.Lazy(lambda: None).__repr__() == Maybe.nothing().to_lazy().__repr__()

    # __eq__
   

# Generated at 2022-06-14 03:36:23.325051
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # test empty Maybe
    nothing_1 = Maybe.nothing()
    nothing_2 = Maybe.nothing()
    assert nothing_1 == nothing_2
    assert nothing_2 == nothing_1

    # test not empty Maybe
    just_1 = Maybe.just(5)
    just_2 = Maybe.just(5)
    assert just_1 == just_2
    assert just_2 == just_1


# Generated at 2022-06-14 03:36:35.648219
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.func import Function

    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.just("foo").filter(lambda x: True) == Maybe.just("foo")
    assert Maybe.just("foo").filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just("foo").filter(Function(lambda x: x == 1).returns(True).else_returns(False)) == Maybe.nothing()
    assert Maybe.nothing().filter(Function(lambda x: x == 1).returns(True).else_returns(False)) == Maybe.nothing()
    assert Maybe.just(1).filter(Function(lambda x: x == 1).returns(True).else_returns(False)) == Maybe.just(1)



# Generated at 2022-06-14 03:36:52.472789
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe

    :return: None
    """
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:36:56.849424
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().value() == 1
    assert Maybe.nothing().to_lazy().value() is None
    assert Maybe.just(1) == Maybe.just(1).to_lazy().value().to_maybe()
    assert Maybe.nothing() == Maybe.nothing().to_lazy().value().to_maybe()



# Generated at 2022-06-14 03:37:01.170393
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:37:05.674220
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    print('Test execution Maybe.filter')
    assert Maybe.just(3).filter(lambda x: x > 2) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x < 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()


# Generated at 2022-06-14 03:37:10.385129
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:37:12.545931
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 0) == Maybe.nothing()

# Generated at 2022-06-14 03:37:24.084762
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.either import Left, Right
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != 1
    assert Maybe.just(1) != True
    assert Maybe.just(1) != Left(1)
    assert Maybe.just(1) != Right(1)
    assert Maybe.just(1) != Box(1)
    assert Maybe.just(1) != Lazy(lambda: 1)
   

# Generated at 2022-06-14 03:37:29.687305
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0).is_nothing == True
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x % 2 == 0).is_nothing == False
    assert Maybe.nothing().filter(lambda x: x % 2 == 0).is_nothing == True
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:37:38.984141
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    Maybe.just(1)\
        .filter(lambda x: x < 2)\
        .filter(lambda x: x > 0)\
        .filter(lambda x: True) == Maybe.just(1)

    Maybe.just(1)\
        .filter(lambda x: x < 0)\
        .filter(lambda x: x > 0)\
        .filter(lambda x: True) == Maybe.nothing()

    Maybe.just(1)\
        .filter(lambda x: True) == Maybe.just(1)

    Maybe.just(1)\
        .filter(lambda x: True)\
        .filter(lambda x: False) == Maybe.nothing()

    Maybe.nothing()\
        .filter(lambda x: True) == Maybe.nothing()

    Maybe.nothing()\
        .filter(lambda x: False) == Maybe.nothing()



# Generated at 2022-06-14 03:37:41.156738
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.option import Option

    assert isinstance(
        Option.just(7).to_lazy(),
        Lazy
    )

    assert Option.just(7).to_lazy().force() == 7

    assert Option.nothing().to_lazy().force() is None

# Generated at 2022-06-14 03:37:55.968824
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe.just(23)
    maybe2 = Maybe.just(23)
    assert maybe1 == maybe2
    maybe1 = Maybe.nothing()
    maybe2 = Maybe.nothing()
    assert maybe1 == maybe2


# Generated at 2022-06-14 03:38:05.091943
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy, success, failure
    from pymonet.monad_maybe import Maybe
    from pymonet.monads import do_monad
    from pymonet.monad_maybe import Just, Nothing
    from pymonet.monad_try import Try, success, failure

    assert do_monad(Lazy)(lambda:
        Just(10).to_lazy().bind(success) ==
        Lazy(lambda: Try(10, True))
    )

    assert do_monad(Lazy)(lambda:
        Nothing().to_lazy().bind(success) ==
        Lazy(lambda: Try(None, False))
    )


# Generated at 2022-06-14 03:38:11.069264
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_a = Maybe(1, False)

    assert maybe_a == Maybe.just(1)
    assert maybe_a != Maybe.just(2)

    maybe_n = Maybe.nothing()

    assert maybe_n == Maybe.nothing()
    assert maybe_n != Maybe.just(None)
    assert maybe_n != Maybe.just(1)


# Generated at 2022-06-14 03:38:16.242503
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()

# Generated at 2022-06-14 03:38:20.174523
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:38:26.233666
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Test if empty Maybe equal to empty Maybe
    assert(Maybe.nothing() == Maybe.nothing())

    # Test if Maybe with value equal to Maybe with same value
    assert(Maybe.just(1) == Maybe.just(1))

    # Test if Maybe with value equal to Maybe with other value
    assert(Maybe.just(1) != Maybe.just(2))

    # Test if empty Maybe equal to Maybe with value
    assert(Maybe.nothing() != Maybe.just(1))

    # Test if None object equal to Maybe with value
    assert(None == Maybe.just(1))


# Generated at 2022-06-14 03:38:36.152626
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def add(number1, number2):
        return number1 + number2

    maybe = Maybe.just(add)
    maybe = maybe.ap(Maybe.just(1))
    maybe = maybe.ap(Maybe.just(2))
    result = maybe.filter(lambda x: x > 3)

    assert isinstance(result, Maybe)
    assert result.is_nothing
    assert result.get_or_else(0) == 0

    result = maybe.filter(lambda x: x == 3)

    assert isinstance(result, Maybe)
    assert not result.is_nothing
    assert result.get_or_else(0) == 3


# Generated at 2022-06-14 03:38:39.382006
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(4)
    assert Maybe.just(3) != Maybe.nothing()



# Generated at 2022-06-14 03:38:43.963082
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.nothing() != 5


# Generated at 2022-06-14 03:38:48.177082
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def f(x):
        return x

    assert Maybe.just(1).to_lazy() == Lazy(
        lambda: 1
    )
    assert Maybe.nothing().to_lazy() == Lazy(
        lambda: None
    )

# Generated at 2022-06-14 03:39:01.643012
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(None) != Maybe.just(1)


# Generated at 2022-06-14 03:39:06.606749
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just('5') == Maybe.just('5')
    assert Maybe.just('5') != Maybe.just(5)
    assert Maybe.just(5) != Maybe.just('5')
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:13.750379
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.just(1) != Maybe.just('1')


# Generated at 2022-06-14 03:39:21.264876
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('x') == Maybe.just('x')
    assert Maybe.just(None) != Maybe.just('x')
    assert Maybe.just('x') != Maybe.just(None)
    assert Maybe.just('x') != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('x')


# Generated at 2022-06-14 03:39:25.916430
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)



# Generated at 2022-06-14 03:39:28.380383
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(3).to_lazy().force() == 3
    assert Maybe.nothing().to_lazy().force() is None


# Generated at 2022-06-14 03:39:31.115855
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('a') == Maybe.just('a')
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(8)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:39:35.636808
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)

    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.just(1) != Maybe.nothing()

    assert Maybe.just(None) == Maybe.just(None)

    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:40.365465
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just('a').to_lazy() == Lazy(lambda: 'a')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:43.735149
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:58.312247
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just("test") != Maybe.just(1)
    assert Maybe.just("test") != Maybe.nothing()



# Generated at 2022-06-14 03:40:01.684390
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(5) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:40:07.687526
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:40:12.432678
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('a') == Maybe.just('a')
    assert Maybe.just('a') != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('a')
    assert Maybe.nothing() == Maybe.nothing()

test_Maybe___eq__()


# Generated at 2022-06-14 03:40:18.729555
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe.
    """
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:40:24.052721
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe(1, False)
    maybe2 = Maybe(1, False)
    maybe3 = Maybe(1, True)
    maybe4 = Maybe(2, False)

    assert maybe1 == maybe2
    assert maybe1 != maybe3
    assert maybe1 != maybe4


# Generated at 2022-06-14 03:40:27.235850
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()

# Generated at 2022-06-14 03:40:33.938517
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    mapper = lambda x: x % 2 == 0

    assert (
        Maybe.just(2).filter(mapper) ==
        Maybe.just(2)
    )

    assert (
        Maybe.just(3).filter(mapper) ==
        Maybe.nothing()
    )

    assert (
        Maybe.nothing().filter(mapper) ==
        Maybe.nothing()
    )

# Generated at 2022-06-14 03:40:36.972476
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('foo') == Maybe.nothing() is False
    assert Maybe.nothing() == Maybe.just('foo') is False
    assert Maybe.just('foo') == Maybe.just('foo')
    assert Maybe.nothing() == Maybe.nothing()

# Generated at 2022-06-14 03:40:44.481133
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    empty = Maybe.nothing()
    lazy_1 = empty.to_lazy()

    assert isinstance(lazy_1, Lazy)
    assert lazy_1() is None

    not_empty = Maybe.just(42)
    lazy_2 = not_empty.to_lazy()

    assert isinstance(lazy_2, Lazy)
    assert lazy_2() == 42


# Generated at 2022-06-14 03:40:58.888167
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:41:03.784535
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.just(2) == Maybe.just(2) and
           Maybe.just('some') == Maybe.just('some') and
           Maybe.just(2.5) == Maybe.just(2.5) and
           Maybe.nothing() == Maybe.nothing())


# Generated at 2022-06-14 03:41:07.648155
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.just(4) != Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.just(4) != Maybe.nothing()



# Generated at 2022-06-14 03:41:13.400248
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:41:17.668966
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just('abc').filter(lambda x: len(x) == 3) == Maybe.just('abc')
    assert Maybe.just('abc').filter(lambda x: len(x) == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: len(x) == 3) == Maybe.nothing()



# Generated at 2022-06-14 03:41:24.026696
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x <= 1) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x <= 1) == Maybe.nothing()

