

# Generated at 2022-06-14 03:31:33.580096
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    x = Maybe.just(1)
    assert x.filter(lambda i: i == 1) == Maybe.just(1)
    y = Maybe.just(2)
    assert y.filter(lambda i: i == 1) == Maybe.nothing()
    z = Maybe.nothing()
    assert z.filter(lambda i: i == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:31:36.506084
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, is_nothing=False).filter(lambda x: x == 1) == Maybe(1, is_nothing=False)
    assert Maybe(0, is_nothing=False).filter(lambda x: x == 1) == Maybe(0, is_nothing=True)
    assert Maybe(1, is_nothing=True).filter(lambda x: x == 1) == Maybe(1, is_nothing=True)



# Generated at 2022-06-14 03:31:40.406264
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:31:43.088351
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(5).to_lazy().value() == 5
    assert Maybe.nothing().to_lazy().value() is None


# Generated at 2022-06-14 03:31:46.995167
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0).get_or_else(0) == 1
    assert Maybe.just(1).filter(lambda x: x < 0).get_or_else(0) == 0

# Generated at 2022-06-14 03:31:47.672187
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Mayb

# Generated at 2022-06-14 03:31:54.028806
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    lazy_1 = Maybe.just(42).to_lazy()
    lazy_2 = Maybe.nothing().to_lazy()
    assert lazy_1 == Lazy(lambda: 42)
    assert lazy_2 == Lazy(lambda: None)

# Generated at 2022-06-14 03:31:58.231911
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # arrange
    value = Maybe.just(5)
    filterer = lambda x: x > 3

    # act and assert
    assert value.filter(filterer) == Maybe.just(5)
    assert value.filter(lambda x: x > 6) == Maybe.nothing()


# Generated at 2022-06-14 03:32:08.751882
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe1 = Maybe.just(1)
    maybe2 = Maybe.nothing()

    maybe1_filterer_result = maybe1.filter(lambda value: value % 2 == 0)
    maybe2_filterer_result = maybe2.filter(lambda value: value % 2 == 0)

    assert isinstance(maybe1_filterer_result, Maybe)
    assert isinstance(maybe2_filterer_result, Maybe)

    assert maybe1_filterer_result == Maybe.nothing()
    assert maybe2_filterer_result == Maybe.nothing()

    maybe1_filterer_result = maybe1.filter(lambda value: value % 2 != 0)
    assert maybe1_filterer_result == Maybe.just(1)


# Generated at 2022-06-14 03:32:12.576993
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe

    :return: nothing
    """
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(0) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:23.733335
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert not Maybe.just(1) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert not Maybe.just(1) != Maybe.just(1)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:32:29.283472
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    def run(maybe, other, expected):
        actual = maybe == other
        expected == actual
        assert expected == actual

    run(Maybe.just(1), Maybe.just(1), True)
    run(Maybe.just(1), Maybe.just(2), False)
    run(Maybe.just(3), Maybe.nothing(), False)
    run(Maybe.nothing(), Maybe.nothing(), True)



# Generated at 2022-06-14 03:32:35.631184
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != None

# Unit tests for method nothing of class Maybe

# Generated at 2022-06-14 03:32:42.667668
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Create new instances of Maybe
    maybe_one = Maybe.just(1)
    maybe_one_1 = Maybe.just(1)
    maybe_two = Maybe.just(2)
    nothing = Maybe.nothing()

    # Do testing
    assert maybe_one == maybe_one_1
    assert maybe_one != maybe_two
    assert not(maybe_one == nothing)
    assert not(maybe_two == nothing)
    assert nothing == nothing



# Generated at 2022-06-14 03:32:45.649122
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)
    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:32:57.201252
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Method `__eq__` tests.
    """
    from pymonet.either import Left, Right
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Maybe(None, True) == Maybe(None, True)
    assert Maybe(None, False) == Maybe(None, False)
    assert Maybe(None, True) == Maybe.nothing()
    assert Maybe(None, True) == Left(None)
    assert Maybe(None, True) == Right(None)
    assert Maybe(None, True) == Try(None, False)
    assert Maybe(None, True) == Validation.failure(None)
    assert Maybe(None, False) == Validation.success(None)

    assert Maybe(None, True) != Maybe(None, False)

# Generated at 2022-06-14 03:32:59.419242
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    t = Maybe.just(1)
    e = Maybe.nothing()
    from pymonet.lazy import Lazy

    assert t.to_lazy() == Lazy(lambda: 1)
    assert e.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:33:06.780746
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # given
    left = Maybe.just(1)
    right = Maybe.just(2)
    wrong_right = Maybe.just(1)
    right_nothing = Maybe.nothing()

    # when
    result_1 = left == right
    result_2 = left == wrong_right
    result_3 = left == right_nothing

    # then
    assert not result_1
    assert result_2
    assert not result_3


# Generated at 2022-06-14 03:33:09.686603
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return "result"

    assert Maybe.just("result").to_lazy().value() == Lazy(func).value()



# Generated at 2022-06-14 03:33:13.236139
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    l = Maybe.just(2).to_lazy().call()
    assert l.__eq__(Lazy(lambda: 2))


# Generated at 2022-06-14 03:33:23.949998
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    print("test_Maybe___eq__")
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:33:28.366273
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(2) != Maybe.just(31)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)



# Generated at 2022-06-14 03:33:34.033150
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe(2, False)
    assert Maybe.just(2) != Maybe(3, False)
    assert Maybe.nothing() == Maybe(None, True)
    assert Maybe.nothing() == Maybe(2, True)


# Generated at 2022-06-14 03:33:38.855276
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)



# Generated at 2022-06-14 03:33:42.934823
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()

# Unit tests for method just of class Maybe

# Generated at 2022-06-14 03:33:47.845673
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_true = Maybe.just(5)
    maybe_false = Maybe.just(4)
    assert maybe_true == Maybe.just(5)
    assert not maybe_true == maybe_false
    assert not maybe_false == Maybe.nothing()
    assert maybe_true.__eq__(5) == NotImplemented



# Generated at 2022-06-14 03:33:52.196470
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(4).filter(lambda x: x % 2 == 0) == Maybe.just(4)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()

# Generated at 2022-06-14 03:34:03.778090
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    class TestClass(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return isinstance(other, TestClass) and \
                self.value == other.value

    # not empty Maybe
    assert(Maybe.just(1) == Maybe.just(1))
    assert(Maybe.just(1).__eq__(Maybe.just(1)))
    assert(Maybe.just("hh") == Maybe.just("hh"))

    test_class1 = TestClass("hh")
    test_class2 = TestClass("hh")
    assert(Maybe.just(test_class1) == Maybe.just(test_class1))
    assert(Maybe.just(test_class1) == Maybe.just(test_class2))


# Generated at 2022-06-14 03:34:15.579619
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe

    def f():
        return 1

    def g():
        raise Exception()

    def h():
        return None

    assert Maybe.just(f).to_lazy().get()() == 1
    assert Maybe.nothing().to_lazy().get()() == None

    try:
        Maybe.just(g).to_lazy().get()()
        assert False
    except:
        assert True

    try:
        Maybe.just(h).to_lazy().get()()
        assert False
    except:
        assert True

    try:
        Maybe.nothing().to_lazy().get()()
        assert False
    except:
        assert True



# Generated at 2022-06-14 03:34:20.076223
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, False) != Maybe(2, True)
    assert Maybe(1, True) != Maybe(2, False)



# Generated at 2022-06-14 03:34:35.493378
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x > 2) == Maybe.just(3)
    assert Maybe.just(2).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 2) == Maybe.nothing()


# Generated at 2022-06-14 03:34:44.284308
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Checks different cases for method __eq__ of class Maybe
    """
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just("1") # not the same type!
    assert Maybe.just("test") == Maybe.just("test")
    assert Maybe.just("test") != Maybe.just("testing")
    assert Maybe.nothing() != Maybe.just("test")
    assert Maybe.just("test") == Maybe.nothing()
    assert Maybe.nothing() == Maybe.just("None")



# Generated at 2022-06-14 03:34:48.967246
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert not Maybe.just(1) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert not Maybe.nothing() == Maybe.just(None)



# Generated at 2022-06-14 03:34:55.045736
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != True
    assert Maybe(True, False) != Maybe(1, False)



# Generated at 2022-06-14 03:35:06.211318
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """Test Maybe.to_lazy method."""
    from pymonet.lazy import Lazy

    def lazy_function():
        """Lazy function."""
        return 1

    def new_lazy_function():
        """Lazy function."""
        return None

    assert Maybe.just(lazy_function).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    # Test alternative examples
    assert Maybe.just(new_lazy_function).to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:35:12.769310
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    func = lambda x: x + 1

    result1 = Maybe.just(5).to_lazy()
    assert result1 == Lazy(lambda: 5)

    result2 = Maybe.just(func).to_lazy()
    assert result2 == Lazy(lambda: func)

    result3 = Maybe.nothing().to_lazy()
    assert result3 == Lazy(lambda: None)

# Generated at 2022-06-14 03:35:17.699023
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:35:21.286550
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # Given
    maybe = Maybe.just(2)
    lazy = maybe.to_lazy()

    # When
    result = lazy.get_value()

    # Then
    assert result == 2



# Generated at 2022-06-14 03:35:27.033480
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # Test1: test function to_lazy when maybe type is not empty
    val = Maybe.just(1)
    m = val.to_lazy()
    assert m.evaluate() == 1
 
    # Test2: test function to_lazy when maybe type is empty
    val = Maybe.nothing()
    m = val.to_lazy()
    assert m.evaluate() == None


# Generated at 2022-06-14 03:35:29.982976
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:35:56.340292
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != 1
    assert Maybe.just(1) != Maybe.just('1')


# Generated at 2022-06-14 03:36:01.613822
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False)
    assert Maybe(5, False) != Maybe(4, False)
    assert Maybe(5, False) != Maybe(5, True)
    assert Maybe(5, False) != Maybe(4, True)
    assert Maybe(5, True) != Maybe(4, False)
    assert Maybe(5, True) == Maybe(5, True)



# Generated at 2022-06-14 03:36:05.382150
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe(10, True) == Maybe(10, True)
    assert Maybe(10, False) != Maybe(11, False)
    assert Maybe(10, False) != Maybe(10, True)
    assert Maybe(10, False) != Maybe(11, True)


# Generated at 2022-06-14 03:36:13.087534
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert not Maybe.just(1) == Maybe.just(1)
    assert not Maybe.just(1) == Maybe.just(2)
    assert not Maybe.just(1) == Maybe.nothing()
    assert not Maybe.nothing() == Maybe.nothing()
    assert not Maybe.nothing() == Maybe.just(None)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:36:19.895098
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('foo') == Maybe.just('foo')
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.just('foo') == Maybe.just('bar')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('foo')



# Generated at 2022-06-14 03:36:25.065883
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:36:27.807418
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, True)



# Generated at 2022-06-14 03:36:33.987043
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test function for method to_lazy of class Maybe.

    :returns: Nothing
    :rtype: Nothing
    """
    from pymonet.lazy import Lazy

    assert Maybe(10, False).to_lazy() == Lazy(lambda: 10)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:38.228906
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:36:43.127193
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x > 1) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x > 1) == Maybe.nothing()



# Generated at 2022-06-14 03:37:25.292139
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)


# Generated at 2022-06-14 03:37:28.032657
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:37.413558
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.box import Box

    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe.just(Box(1))
    assert Maybe.just(1) == Box(1)
    assert Maybe.just(None) == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Box(2)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.nothing() != Maybe.nothing()
    assert Maybe.nothing() != Box(None)
    assert Maybe.nothing() != 1



# Generated at 2022-06-14 03:37:39.582037
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:37:46.513753
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Test for method __eq__ of class Maybe

    :returns: Nothing
    :rtype: None
    """
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    print('test_Maybe___eq__ is ok')



# Generated at 2022-06-14 03:37:49.249950
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:37:50.982259
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:37:55.919557
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:38:00.896625
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)


# Generated at 2022-06-14 03:38:02.377175
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(10).to_lazy().force() == 10



# Generated at 2022-06-14 03:39:24.107474
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.nothing() is False
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe.just(2) is False


# Generated at 2022-06-14 03:39:30.056701
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result_nothing = Maybe.just([1, 2, 3, 4, 5]).filter(lambda x: len(x) == 5)
    expected_nothing = Maybe.nothing()
    assert expected_nothing == result_nothing

    result_just = Maybe.just([1, 2, 3, 4]).filter(lambda x: len(x) == 4)
    expected_just = Maybe.just([1, 2, 3, 4])
    assert expected_just == result_just



# Generated at 2022-06-14 03:39:34.339117
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:39:40.049804
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x > 20) == Maybe.nothing()
    assert Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10)
    assert Maybe.nothing().filter(lambda x: x > 5) == Maybe.nothing()



# Generated at 2022-06-14 03:39:44.683815
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    b1 = Maybe.just(1)
    b2 = Maybe.just(1)
    n1 = Maybe.nothing()
    n2 = Maybe.nothing()

    assert b1 == b2
    assert not b1 != b2
    assert n1 == n2
    assert not n1 != n2



# Generated at 2022-06-14 03:39:55.607669
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    def true_function():
        return 1

    def wrong_function():
        return None

    lazy = Lazy(true_function)
    maybe = Maybe.just(lazy)
    assert (maybe.to_lazy() == lazy)

    maybe = Maybe.just(None)
    assert (maybe.to_lazy() == Lazy(lambda: None))

    maybe = Maybe.just(1)
    maybe_lazy = maybe.to_lazy()
    assert (maybe_lazy() == 1)

    maybe = Maybe.just(Right(2))
    maybe_lazy = maybe.to_lazy()
    assert (maybe_lazy() == 2)

    maybe = Maybe.just(Right(1))
    maybe

# Generated at 2022-06-14 03:40:02.761777
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.either import Left, Right

    test_values = [
        (Maybe.just(2).filter(lambda x: x == 2), Maybe.just(2)),
        (Maybe.just(2).filter(lambda x: x == 1), Maybe.nothing()),
        (Maybe.nothing().filter(lambda x: x == 1), Maybe.nothing()),
    ]
    for example, expectation in test_values:
        assert example == expectation, f'{str(example)} != {str(expectation)}'


# Generated at 2022-06-14 03:40:08.455097
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:40:17.740517
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe[int](1, False) == Maybe[int](1, False)
    assert Maybe[int](1, False) != Maybe[int](2, False)
    assert Maybe[int](1, False) != Maybe[int](1, True)
    assert Maybe[int](1, True) == Maybe[int](1, True)
    assert Maybe[int](1, True) != Maybe[int](2, True)
    assert Maybe[int](1, True) != Maybe[int](1, False)



# Generated at 2022-06-14 03:40:28.574619
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    m1 = Maybe.just("1")
    m2 = Maybe.just("2")
    n1 = Maybe.nothing()
    n2 = Maybe.nothing()

    assert m1 == m1
    assert m2 == m2
    assert n1 == n1
    assert n2 == n2
    assert not (m1 == n1)
    assert not (m2 == n1)
    assert not (n1 == m1)
    assert not (n1 == m2)
    assert not (n1 != n1)
    assert not (m1 != m1)
    assert m1 != m2
    assert m2 != m1
    assert n1 != m1
    assert n1 != m2
    assert m1 != n1
    assert m2 != n1
    assert m1 != "1"


# Unit test