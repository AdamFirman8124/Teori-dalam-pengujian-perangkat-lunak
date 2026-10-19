

# Generated at 2022-06-14 03:31:34.200230
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.
    """
    # GIVEN
    monad = Maybe.just(6)

    # WHEN
    result = monad.to_lazy()

    # THEN
    assert isinstance(result, Lazy)
    assert result.val() == 6

# Generated at 2022-06-14 03:31:40.405186
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(3, False) == Maybe(4, False) == Maybe(3, False)
    assert Maybe(3, True) == Maybe(3, False) == Maybe(4, True)
    assert Maybe(3, True) != Maybe(4, False)
    assert Maybe(3, True) != Maybe(4, True)


# Generated at 2022-06-14 03:31:46.359757
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.just(10) == Maybe.just(10) == Maybe.just(10))
    assert(Maybe.nothing() == Maybe.nothing() == Maybe.nothing())
    assert(Maybe.just(10) != Maybe.just(20))
    assert(Maybe.just(20) != Maybe.nothing())
    assert(Maybe.nothing() != Maybe.just(20))


# Generated at 2022-06-14 03:31:48.574164
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:31:56.068712
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    # if we are comparing None with Maybe(None, False) methods
    # will return True becouse Maybe.__eq__(Maybe(None, False))
    # will return True
    assert Maybe.just(None) == Maybe.just(None)


# Generated at 2022-06-14 03:32:01.788562
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:32:07.039413
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(123) == Maybe.just(123)
    assert Maybe.just(123) != Maybe.just(123.0001)
    assert Maybe.just(123) != Maybe.nothing()



# Generated at 2022-06-14 03:32:13.770233
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    m1 = Maybe.just(2)
    val1 = m1.to_lazy()
    assert isinstance(val1, Lazy) and val1.evaluate() == 2

    m2 = Maybe.nothing()
    val2 = m2.to_lazy()
    assert isinstance(val2, Lazy) and val2.evaluate() == None

# Generated at 2022-06-14 03:32:19.845428
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe.

    :return: If test passed than None, else raises assertion error
    """
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:32:25.312674
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    lazy_func = lambda: 42
    lazy_monad = Lazy(lazy_func)
    maybe_monad = Maybe.just(lazy_func)
    assert lazy_monad == maybe_monad.to_lazy()


# Generated at 2022-06-14 03:32:38.990715
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    Maybe(None, True) == Maybe(None, True)
    Maybe(0, True) == Maybe(None, True)
    Maybe(0, False) == Maybe(0, False)
    Maybe(0, False) == Maybe(1, False)
    Maybe(0, True) == Maybe(1, False)
    Maybe(0, True) == Maybe(0, True)
    Maybe(0, True) == Maybe(1, True)
    Maybe(0, True) == Maybe(None, False)
    Maybe(0, True) == Maybe(0, False)
    Maybe(None, True) == Maybe(0, False)
    Maybe(0, True) == Maybe(None, True)
    Maybe(0, False) == Maybe(None, True)



# Generated at 2022-06-14 03:32:44.900447
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Create equal instances
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    # Create not equal instances
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() != None


# Generated at 2022-06-14 03:32:56.615663
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_try import Success
    from pymonet.monad_try import Failure
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.box import Box

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    with pytest.raises(AssertionError):
        assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    assert Try.success(1).to_lazy() == Maybe.just(1).to_lazy()
    assert Try.failure(None).to_lazy() == Maybe.nothing().to_lazy()

# Generated at 2022-06-14 03:33:02.861057
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_maybe import Maybe

    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()


# Generated at 2022-06-14 03:33:05.744375
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:33:14.590833
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    print('Test __eq__ method of class Maybe')

    print('\tTest __eq__ when two object are equal')
    m1 = Maybe(1, False)
    m2 = Maybe(1, False)
    assert m1 == m2

    print('\tTest __eq__ when two object are differ')
    m1 = Maybe(1, False)
    m2 = Maybe(1, True)
    assert not m1 == m2

    print('\tTest __eq__ when two object are differ')
    m1 = Maybe(2, False)
    m2 = Maybe(1, False)
    assert not m1 == m2


# Generated at 2022-06-14 03:33:23.750558
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # if both mappers are None
    if Maybe.nothing() == Maybe.nothing():
        pass
    else:
        raise AssertionError('Maybe.nothing() should be equal Maybe.nothing()')

    # if only one mapper is None
    if Maybe.nothing() != Maybe.just(1):
        pass
    else:
        raise AssertionError('Maybe.nothing() should be not equal Maybe.just(1)')
    if Maybe.just(1) != Maybe.nothing():
        pass
    else:
        raise AssertionError('Maybe.just(1) should be not equal Maybe.nothing()')

    # if both mappers are not None
    if Maybe.just(1) == Maybe.just(1):
        pass

# Generated at 2022-06-14 03:33:26.434398
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:33.754829
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != None


# Generated at 2022-06-14 03:33:41.793360
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1).__eq__(Maybe.just(1))
    assert not Maybe.just(1).__eq__(Maybe.nothing())
    assert Maybe.nothing().__eq__(Maybe.nothing())
    assert not Maybe.just(1).__eq__(Maybe.just(2))
    assert not Maybe.just(1).__eq__(Maybe.just('1'))
    assert not Maybe.just(1).__eq__(None)



# Generated at 2022-06-14 03:33:47.917706
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(1, True).to_lazy() == \
        Lazy(lambda: None)
    assert Maybe(1, False).to_lazy() == \
        Lazy(lambda: 1)


# Generated at 2022-06-14 03:33:52.559421
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def is_even(value):
        return value % 2 == 0

    assert Maybe(1, False).filter(is_even).is_nothing
    assert Maybe(2, False).filter(is_even) == Maybe(2, False)
    assert Maybe(None, True).filter(is_even).is_nothing



# Generated at 2022-06-14 03:34:03.914252
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe(1, False).filter(lambda x: x < 1) == Maybe.nothing()
    assert Maybe(1, False).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe(1, False).filter(lambda x: x != 1) == Maybe.nothing()
    assert Maybe(1, False).filter(lambda x: True) == Maybe.just(1)
    assert Maybe(1, False).filter(lambda x: False) == Maybe.nothing()

    assert Maybe(1, True).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe(1, True).filter(lambda x: x < 1) == Maybe.nothing()

# Generated at 2022-06-14 03:34:10.366547
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Test when Maybe is empty
    assert Maybe.nothing().filter(lambda x: isinstance(x, int)) == Maybe.nothing()
    # Test when filterer returns True
    assert Maybe.just(2).filter(lambda x: isinstance(x, int)) == Maybe.just(2)
    # Test when filterer returns False
    assert Maybe.just("a").filter(lambda x: isinstance(x, int)) == Maybe.nothing()

# Generated at 2022-06-14 03:34:21.142542
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Maybe(None, True).filter(lambda x: x) == Maybe.nothing()
    assert Maybe(1, False).filter(lambda x: x) == Maybe.just(1)
    assert Maybe(1, False).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe(1, False).filter(lambda x: x < 0) == Maybe.nothing()
    assert isinstance(Maybe(None, True).get_or_else(1), int)
    assert isinstance(Maybe(None, True).get_or_else([]), list)
    assert isinstance(Maybe(None, True).get_or_else(Try(1, True)), Try)

# Generated at 2022-06-14 03:34:31.240053
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy().force() == Lazy(lambda: 1).force()
    assert Maybe.nothing().to_lazy().force() == Lazy(lambda: None).force()

    from pymonet.monad_try import Try
    assert Maybe.just(1).to_try() == Try(1, is_success=True)
    assert Maybe.nothing().to_try() == Try(None, is_success=False)

    from pymonet.box import Box
    assert Maybe.just(1).to_box() == Box(1)
    assert Maybe.nothing().to_box() == Box(None)

    from pymonet.either import Left, Right
    assert Maybe.just(1).to_either() == Right(1)

# Generated at 2022-06-14 03:34:35.738744
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0).equals(Maybe.nothing())
    assert Maybe.just(2).filter(lambda x: x % 2 == 0).equals(Maybe.just(2))



# Generated at 2022-06-14 03:34:42.096527
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.maybe import Maybe as M
    from pymonet.lazy import Lazy as L

    empty_maybe = M.nothing()
    lazier = empty_maybe.to_lazy()

    assert lazier.value == L(lambda: None)

    not_empty_maybe = M.just(Box(5))
    lazier = not_empty_maybe.to_lazy()
    assert lazier.value == L(lambda: Box(5))


# Generated at 2022-06-14 03:34:54.396702
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test for method filter of class Maybe.
    """
    from pymonet.functor import fmap
    from pymonet.applicative import pure

    assert fmap(lambda x: x * 2, Maybe.just(3)) == Maybe.just(6)

    assert fmap(lambda x: x * 2, Maybe.just(None)) == Maybe.just(None)

    assert fmap(lambda x: x * 2, Maybe.nothing()) == Maybe.nothing()

    assert fmap(lambda x: x * 2, pure(3)) == Maybe.just(6)

    assert fmap(lambda x: x + ' world', pure('Hello')) == Maybe.just('Hello world')

    assert fmap(lambda x: x * 2, pure(None)) == Maybe.just(None)


# Generated at 2022-06-14 03:35:02.125623
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # y = x + 1
    def filterer(x: int) -> bool:
        return True if x % 2 == 0 else False

    assert Maybe.nothing().filter(filterer) == Maybe.nothing()
    assert Maybe.just(0).filter(filterer) == Maybe.just(0)
    assert Maybe.just(1).filter(filterer) == Maybe.nothing()



# Generated at 2022-06-14 03:35:06.696854
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(123, False).to_lazy().force() == 123
    assert Maybe(None, True).to_lazy().force() is None


# Generated at 2022-06-14 03:35:09.906115
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(2).to_lazy().get() == 2
    assert Maybe.nothing().to_lazy().get() is None

# Generated at 2022-06-14 03:35:20.786775
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Failure

    assert Maybe.just(Box(10)).to_lazy().map(lambda a: a().get_or_else(0)).map(lambda a: a * 2).get_or_else(0) == 20
    assert Maybe.just(Failure(10)).to_lazy().map(lambda a: a()).map(lambda a: a.get_or_else(20)).get_or_else(0) == 20
    assert Maybe.nothing().to_lazy().map(lambda a: a()).map(lambda a: a.get_or_else(20)).get_or_else(0) == 0


# Generated at 2022-06-14 03:35:24.715942
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    lazy_nothing = Maybe.nothing().to_lazy()
    assert(lazy_nothing.run() == None)
    lazy_just = Maybe.just(10).to_lazy()
    assert(lazy_just.run() == 10)


# Generated at 2022-06-14 03:35:31.473256
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy in class Maybe.

    :return: True when test was passed, otherwise False
    :rtype: Boolean
    """
    from pymonet.lazy import Lazy

    if (Lazy(lambda: "Result") == Maybe.just("Result").to_lazy()):
        if (Lazy(lambda: None) == Maybe.nothing().to_lazy()):
            return True
    return False


# Generated at 2022-06-14 03:35:35.268579
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(42).to_lazy().resolve() == Lazy(lambda: 42).resolve()
    assert Maybe.nothing().to_lazy().resolve() == Lazy(lambda: None).resolve()


Maybe.__name__ = 'Maybe'

# Generated at 2022-06-14 03:35:39.318887
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # given
    maybe = Maybe.just(2)

    # when
    lazy = maybe.to_lazy()

    # then
    assert isinstance(lazy, Maybe)
    res = lazy.value()
    assert res == 2

# Generated at 2022-06-14 03:35:44.644254
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_lazy import Lazy
    assert(Maybe.just(1).to_lazy() == Lazy(lambda: 1))
    assert(Maybe.nothing().to_lazy() == Lazy(lambda: None))



# Generated at 2022-06-14 03:35:49.461265
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def side_effect():
        print("This is side effect")

    def some_func(x:int) -> int:
        return 2 * x

    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy().map(some_func).map(lambda _: side_effect()).get() == 2
    assert Maybe.nothing().to_lazy().map(some_func).get() is None



# Generated at 2022-06-14 03:35:54.827038
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe(42, False).to_lazy() == Lazy(lambda: 42)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:36:03.884102
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    from pymonet.monad_try import Try

    m_value = Maybe.just("test")

    assert m_value.to_lazy().get() == Lazy(lambda: "test").get()
    assert m_value.to_lazy() == Try(Lazy(lambda: "test"), is_success=True)

    m_value = Maybe.nothing()

    assert m_value.to_lazy().get() == Lazy(lambda: None).get()
    assert m_value.to_lazy() == Try(Lazy(lambda: None), is_success=True)


# Generated at 2022-06-14 03:36:07.148302
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:36:12.083937
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    res = Maybe.just(1).to_lazy()
    assert res == Lazy(lambda: 1)

    res = Maybe.nothing().to_lazy()
    assert res == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:14.475560
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_maybe import Maybe
    from pymonet.lazy import Lazy

    # The Maybe is not empty
    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)

    # The Maybe is empty
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:18.642966
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.
    """
    assert Maybe(1, False).to_lazy().force() == 1
    assert Maybe(None, True).to_lazy().force() is None

# Generated at 2022-06-14 03:36:22.746291
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def f() -> int: return 3

    assert Maybe(4, False).to_lazy().get()() == 4
    assert Maybe(None, True).to_lazy().get()() is None

    result = Maybe(f, False).to_lazy()
    assert result.get()()() == 3



# Generated at 2022-06-14 03:36:27.638743
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    m1 = Maybe.just(1)
    assert Lazy(lambda: 1) == m1.to_lazy()

    m2 = Maybe.nothing()
    assert Lazy(None) == m2.to_lazy()

# Generated at 2022-06-14 03:36:30.405752
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(3).to_lazy() == Lazy(lambda: 3)



# Generated at 2022-06-14 03:36:31.729102
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:36.851779
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.either import Left
    from pymonet.lazy import Lazy

    maybe = Maybe.just(1)
    maybe2 = Maybe.nothing()

    assert maybe.to_lazy() == Lazy(lambda: 1)
    assert maybe2.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:44.269637
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:49.568745
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    # Check if Maybe is empty returns Lazy(None)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    # Check if Maybe is empty returns Lazy(value)
    assert Maybe.just("Test").to_lazy() == Lazy(lambda: "Test")


# Generated at 2022-06-14 03:36:53.698212
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:36:56.602445
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:37:02.704021
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    # Test to_lazy when Maybe is empty
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()
    # Test to_lazy when Maybe is not empty
    val = 2
    assert Lazy(lambda: val) == Maybe.just(val).to_lazy()

# Generated at 2022-06-14 03:37:05.227972
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(42).to_lazy() == Lazy(lambda: 42)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:37:13.729983
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert(
        Maybe.nothing().to_lazy() ==
        Lazy(lambda: None)
    )

    assert(
        Maybe.just(Try('a')).to_lazy() ==
        Lazy(lambda:  Try('a'))
    )

    assert(
        Maybe.just(Try('a', is_success=False)).to_lazy() ==
        Lazy(lambda:  Try('a', is_success=False))
    )



# Generated at 2022-06-14 03:37:18.260648
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def a() -> int:
        return 1

    assert Maybe.just(a).to_lazy() == Lazy(a)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:37:21.916824
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    import pytest

    assert Maybe.just(1).to_lazy().force() == 1
    assert Maybe.nothing().to_lazy().force() is None



# Generated at 2022-06-14 03:37:25.846290
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def func():
        return 'test'

    assert Maybe.just(func).to_lazy().force()() == 'test'
    assert Maybe.nothing().to_lazy().force()() == None



# Generated at 2022-06-14 03:37:39.160853
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    import pytest
    from pymonet.lazy import Lazy

    assert Maybe.just('M').to_lazy() == \
           Lazy(lambda: 'M')

    assert Maybe.nothing().to_lazy() == \
           Lazy(lambda: None)


# Generated at 2022-06-14 03:37:43.021367
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:48.887824
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    from pymonet.lazy import Lazy

    def value_function():
        return 5

    def nothing_function():
        return None

    assert Maybe(11, False).to_lazy() == Lazy(value_function)
    assert Maybe(11, True).to_lazy() == Lazy(nothing_function)
    assert Maybe.just(11).to_lazy() == Lazy(value_function)
    assert Maybe.nothing().to_lazy() == Lazy(nothing_function)


# Generated at 2022-06-14 03:37:52.826717
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def test_case(value, is_nothing, expected_value):
        maybe = Maybe(value, is_nothing)
        lazy = maybe.to_lazy()

        assert expected_value == lazy.value()

    test_case('a', False, 'a')
    test_case('a', True, None)


# Generated at 2022-06-14 03:37:59.453771
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe_monad = Maybe.just(lambda: 1 + 1)
    lazy_monad = maybe_monad.to_lazy()

    assert lazy_monad == Lazy(lambda: 1 + 1)
    assert lazy_monad.value() == 2


# Generated at 2022-06-14 03:38:05.191237
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import identity

    def lazy_adder_function(num): return lambda: num + 1

    monad = Maybe.just(3)
    assert identity(monad).to_lazy() == Lazy(lazy_adder_function(3))

    monad = Maybe.nothing()
    assert identity(monad).to_lazy() == Lazy(lazy_adder_function(None))


if __name__ == "__main__":
    test_Maybe_to_lazy()

# Generated at 2022-06-14 03:38:08.317437
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just('1').to_lazy() == Lazy(lambda: '1')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:19.586291
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """Tests Maybe_to_lazy method"""
    def test_instance(value):
        """
        Tests Maybe instance.

        :param value: value to test
        :type value: Any
        :returns: True is test successful, in other case False
        :rtype: Boolean
        """
        maybe = Maybe.just(value)
        lazy = maybe.to_lazy()
        return lazy.value() == value


# Generated at 2022-06-14 03:38:25.387439
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """Unit test for method to_lazy of class Maybe."""
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:27.536120
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # given
    maybe = Maybe.just(42)

    # when
    lazy = maybe.to_lazy()

    # then
    assert lazy.evaluate() == 42
    assert lazy.evaluate() == 42


# Generated at 2022-06-14 03:38:40.398340
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    def f():
        return 1
    assert Maybe.just(f).to_lazy().f() == Maybe.just(1).to_lazy().f()
    assert Maybe.nothing().to_lazy().f() == Maybe.just(None).to_lazy().f()



# Generated at 2022-06-14 03:38:45.105519
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    value = 18
    maybe = Maybe.just(value)
    lazy = maybe.to_lazy()
    assert lazy.get() == value

    maybe = Maybe.nothing()
    lazy = maybe.to_lazy()
    assert lazy.get() is None


# Generated at 2022-06-14 03:38:50.641731
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """ Unit test for method to_lazy of class Maybe """
    from pymonet.lazy import Lazy

    def f1() -> None:
        print('f1')

    def f2() -> int:
        return 2

    assert Maybe.just(f1).to_lazy() == Lazy(f1)
    assert Maybe.just(f2).to_lazy() == Lazy(f2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:55.328120
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:01.950753
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe
    """
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:39:05.462705
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:39:07.941134
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return Just(4).value

    assert Just(4).to_lazy() == Lazy(f)



# Generated at 2022-06-14 03:39:14.681079
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.just(None).to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:39:17.359047
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    from pymonet.lazy import Lazy

    m = Maybe.just(1)

    assert Lazy(lambda: 1) == m.to_lazy()


# Generated at 2022-06-14 03:39:29.291120
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy().to_either() == Left(None)
    assert Maybe.nothing().to_lazy().to_box() == Box(None)
    assert Maybe.nothing().to_lazy().to_try() == Try(None, is_success=False)
    assert Maybe.nothing().to_lazy().to_validation() == Validation.success(None)


# Unit test

# Generated at 2022-06-14 03:39:41.151722
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def f():
        return 42
    assert Maybe(f, False).to_lazy().get() == f()
# /Unit test for method to_lazy of class Maybe


# Generated at 2022-06-14 03:39:43.066856
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe(1, False)
    assert maybe.to_lazy() == Lazy(lambda: 1)

    maybe = Maybe(1, True)
    assert maybe.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:44.151536
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    result = Maybe.just('Hello')
    result = result.to_lazy()

    assert callable(result.value)


# Generated at 2022-06-14 03:39:47.304127
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy() == Maybe.just(None).to_lazy()
    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:39:50.285366
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().run() == 1
    assert Maybe.nothing().to_lazy().run() is None


# Generated at 2022-06-14 03:39:57.306651
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functions import identity
    lazy = Maybe.just(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1
    assert lazy.map(identity) == lazy
    lazy = Maybe.nothing().to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() is None
    assert lazy.map(identity) == lazy



# Generated at 2022-06-14 03:39:59.698953
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.validation import Validation

    assert Maybe.just(None).to_lazy() == Lazy(lambda: None)
    assert Maybe.just(Validation.success(1)).to_lazy() == Lazy(lambda: Validation.success(1))

# Generated at 2022-06-14 03:40:07.208317
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy().value == 1
    assert Maybe.nothing().to_lazy().value is None


if __name__ == '__main__':
    test_Maybe_to_lazy()

# Generated at 2022-06-14 03:40:11.599023
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def maybe_to_lazy():
        return Maybe.just(3).to_lazy().value

    assert maybe_to_lazy() == 3
    assert Maybe.nothing().to_lazy().value() is None



# Generated at 2022-06-14 03:40:25.799094
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy, Thunk

    def test_mapper(value):
        return value

    def test_filterer(value):
        return value

    assert Maybe.just(1).to_lazy() == Lazy(Thunk(lambda: 1))
    assert Maybe.nothing().to_lazy() == Lazy(Thunk(lambda: None))

    assert Maybe.just(1).map(test_mapper).to_lazy() == Lazy(Thunk(lambda: 1))
    assert Maybe.nothing().map(test_mapper).to_lazy() == Lazy(Thunk(lambda: None))

    assert Maybe.just(1).filter(test_filterer).to_lazy() == Lazy(Thunk(lambda: 1))

# Generated at 2022-06-14 03:40:39.158694
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Testing of method to_lazy of maybe class.
    """
    from pymonet.lazy import Lazy
    Lazy.unit = staticmethod(None)

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:40:42.787543
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:40:47.647967
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    value = Maybe(1, False)
    assert Lazy(lambda: 1) == value.to_lazy()

    value = Maybe(1, True)
    assert Lazy(lambda: None) == value.to_lazy()

# Generated at 2022-06-14 03:40:51.533777
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def __function():
        return "result"

    assert Maybe(__function(), False).to_lazy() == Lazy(__function)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:40:54.013343
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:41:04.696076
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def some_function(arg: int) -> int:
        return arg + 1

    maybe = Maybe.just(2)
    lazy = maybe.to_lazy()

    assert lazy == Lazy(lambda: 2)

    lazy_func = lazy.map(some_function)
    assert lazy_func == Lazy(lambda: some_function(2))
    assert lazy_func.force() == 3

    maybe_nothing = Maybe.nothing()
    lazy_nothing = maybe_nothing.to_lazy()
    assert lazy_nothing == Lazy(lambda: None)

    lazy_nothing_func = lazy_nothing.map(some_function)
    assert lazy_nothing_func == Lazy(lambda: None)
    assert lazy_nothing_func.force() == None


# Generated at 2022-06-14 03:41:06.944785
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    test Maybe.to_lazy(self)
    """
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:41:12.287729
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy().unwrap() == None
    assert Maybe.just(5).to_lazy().unwrap() == 5
    assert Maybe.nothing().to_try() == Try(None, is_success=False)
    assert Maybe.just(5).to_try() == Try(5, is_success=True)


# Unit tests for method bind of class Maybe

# Generated at 2022-06-14 03:41:16.127858
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(42)
    assert maybe.to_lazy() == Lazy(lambda: 42)
    assert maybe.to_lazy().get() == 42

# Generated at 2022-06-14 03:41:22.769530
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(4).to_lazy() == Lazy(lambda: 4)
    assert Maybe.just('abc').to_lazy() == Lazy(lambda: 'abc')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

