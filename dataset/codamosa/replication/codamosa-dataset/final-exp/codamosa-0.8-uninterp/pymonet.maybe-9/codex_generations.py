

# Generated at 2022-06-14 03:31:25.640539
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1).__eq__(Maybe.just(1))
    assert Maybe.nothing().__eq__(Maybe.nothing())



# Generated at 2022-06-14 03:31:29.946965
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.just(3) == Maybe(3, False))
    assert(Maybe.nothing() == Maybe(None, True))
    assert(Maybe.just(3) != Maybe(3, True))
    assert(Maybe.just(2) != Maybe(3, False))
    assert(Maybe.nothing() != Maybe(3, True))
    assert(Maybe.just(3) != 3)
    assert(Maybe.just(3) != Maybe.just(3))


# Generated at 2022-06-14 03:31:33.191991
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(None, False) == Maybe(None, False)
    assert Maybe(None, True) == Maybe.nothing()
    assert Maybe.just("test") == Maybe.just("test")



# Generated at 2022-06-14 03:31:36.541298
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)



# Generated at 2022-06-14 03:31:48.574019
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe("ss", False) == Maybe("ss", False)
    assert Maybe("ss", False) != Maybe("sss", False)
    assert Maybe("ss", False) != Maybe("ss", True)
    assert Maybe("ss", True) == Maybe("ss", True)
    assert Maybe("ss", True) == Maybe("sss", True)
    assert Maybe("ss", True) != Maybe("ss", False)
    assert Maybe("ss", True) != Maybe("sss", False)
    assert Maybe("ss", True) != Maybe("sss", False)
    assert Maybe(10, True) == Maybe(15, True)
    assert Maybe(10, True) != Maybe(10, False)



# Generated at 2022-06-14 03:31:52.929321
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)


# Generated at 2022-06-14 03:31:58.377445
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)

# Generated at 2022-06-14 03:32:03.284105
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:32:06.756489
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:32:12.492166
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def square(x):
        return x * x

    assert Maybe.just(10).to_lazy().flat_map(lambda x: square(x)).unsafe_get() == 100
    assert Maybe.nothing().to_lazy().flat_map(lambda x: square(x)).unsafe_get() == None


# Generated at 2022-06-14 03:32:18.156608
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
        assert Maybe.just(1) == Maybe.just(1)
        assert not Maybe.just(1) == Maybe.just(2)
        assert Maybe.nothing() == Maybe.nothing()
        assert not Maybe.nothing() == Maybe.just(None)


# Generated at 2022-06-14 03:32:23.562604
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(42) == Maybe.just(42)
    assert not (Maybe.just(42) == Maybe.just(43))

    assert Maybe.nothing() == Maybe.nothing()
    assert not (Maybe.nothing() == Maybe.just(42))


# Generated at 2022-06-14 03:32:32.064864
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just([1, 2, 3]) == Maybe.just([1, 2, 3])
    assert Maybe.just([1, 2, 3]) != Maybe.just([4, 5, 6])
    assert Maybe.nothing() != Maybe.just([1, 2, 3])
    assert Maybe.just({1: 2, 3: 4}) == Maybe.just({1: 2, 3: 4})
    assert Maybe.just({1: 2, 3: 4}) != Maybe.just({5: 6, 7: 8})
    assert Maybe.nothing

# Generated at 2022-06-14 03:32:44.210781
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)
    assert Maybe([], False).to_lazy() == Lazy(lambda: [])
    assert Maybe("str", False).to_lazy() == Lazy(lambda: "str")
    assert Maybe(123, False).to_lazy() == Lazy(lambda: 123)
    assert Maybe(1.23, False).to_lazy() == Lazy(lambda: 1.23)
    assert Maybe(True, False).to_lazy() == Lazy(lambda: True)
    assert Maybe(False, False).to_lazy() == Lazy(lambda: False)
    assert Maybe((), False).to_lazy() == Lazy(lambda: ())
    assert Maybe(object, False).to

# Generated at 2022-06-14 03:32:50.434749
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x != 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x != 1) == Maybe.nothing()

# Generated at 2022-06-14 03:32:54.992586
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Set up Maybe[str], call to_lazy and then get lazy result.

    :returns: test result
    :rtype: str
    """
    maybe = Maybe.just("result")
    lazy_result = maybe.to_lazy()

    return lazy_result.force()



# Generated at 2022-06-14 03:32:58.064015
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:33:02.717718
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != None


# Generated at 2022-06-14 03:33:10.298700
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # setup
    some_value = 5
    maybe_some = Maybe.just(some_value)
    maybe_none = Maybe.nothing()
    # assert
    assert maybe_some.filter(lambda x: x == some_value) == maybe_some
    assert maybe_some.filter(lambda x: x != some_value) != maybe_some
    assert maybe_none.filter(lambda x: x == some_value) != maybe_none
    assert maybe_none.filter(lambda x: x != some_value) != maybe_none
    # teardown - none



# Generated at 2022-06-14 03:33:14.490969
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(4)


# Generated at 2022-06-14 03:33:23.041522
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(None, False).to_lazy() == Lazy(lambda: None)
    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:33:25.392023
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(True).to_lazy() == Lazy(lambda: True)



# Generated at 2022-06-14 03:33:35.261318
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    m1 = Maybe.just(1)
    m2 = Maybe.just(1)
    m3 = Maybe.just(None)

    m4 = Maybe.nothing()
    m5 = Maybe.nothing()

    assert m1 == m2, "Maybe.__eq__ method failed"
    assert m4 == m5, "Maybe.__eq__ method failed"
    assert m1 != m4, "Maybe.__eq__ method failed"
    assert m1 != m3, "Maybe.__eq__ method failed"
    print("Maybe.__eq__ method passed")


# Generated at 2022-06-14 03:33:37.503416
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:33:48.268494
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Data
    m1 = Maybe.just(1)
    m2 = Maybe.just(2)
    m3 = Maybe.just(1)
    mn = Maybe.nothing()
    mnn = Maybe.nothing()

    # Run code and assert result
    assert m1 == m1, 'm1 == m1'
    assert m2 == m2, 'm2 == m2'
    assert m1 == m3, 'm1 == m3'
    assert mn == mn, 'mn == mn'
    assert mn == mnn, 'mn == mnn'

    assert not m1 == m2, 'm1 != m2'
    assert not m1 == mn, 'm1 != mn'
    assert not m2 == mn, 'm2 != mn'
    assert not m2 == m

# Generated at 2022-06-14 03:33:54.393007
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: x) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)


# Generated at 2022-06-14 03:34:00.000068
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1.0) == Maybe.just(1.0)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(1) != Maybe.just(1.0)
    assert Maybe.just('1') != Maybe.just('1.0')
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.just(True) != Maybe.just(False)
    assert Maybe.just(False) != Maybe.just(True)
    assert Maybe.just(None) != Maybe.just(True)
    assert Maybe.just(True) != Maybe.just(None)

# Generated at 2022-06-14 03:34:12.249981
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    x = Maybe.just(2)
    y = Maybe.just(2)
    z = Maybe.just(3)

    print('Assert Maybe(2) == Maybe(2)', end='...')
    assert x == y
    print('OK')
    print('Assert Maybe(2) != Maybe(3)', end='...')
    assert x != z
    print('OK')
    print('Assert Maybe(2) != Some(2)', end='...')
    assert x != y
    print('OK')
    print('Assert Maybe(2) != None', end='...')
    assert x != Maybe.nothing()
    print('OK')
    print('Assert Maybe(2) != None()', end='...')
    assert x != Maybe.nothing()
    print('OK')

# Generated at 2022-06-14 03:34:16.130482
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # given
    def filterer(x):
        return x > 5
    maybe = Maybe.just(8)
    # when
    result = maybe.filter(filterer)
    # then
    assert result == Maybe.just(8)



# Generated at 2022-06-14 03:34:23.148348
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe.

    :returns: Nothing
    :raises: AssertionError if test not passed
    """
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(5)


# Generated at 2022-06-14 03:34:34.409935
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    :returns: TODO
    :rtype: None
    """
    def foo():
        return 4

    assert Maybe.just(foo).to_lazy().value()() == 4
    assert Maybe.nothing().to_lazy().value()() is None

# Generated at 2022-06-14 03:34:38.844573
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    mb1 = Maybe.just(1)
    mb2 = Maybe.just(1)
    mb3 = Maybe.nothing()
    mb4 = Maybe.nothing()

    assert mb1 == mb2
    assert mb1 != 3
    assert mb3 == mb4
    assert mb3 != mb1



# Generated at 2022-06-14 03:34:48.159097
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Success, Failure
    from pymonet.box import Filled, Empty
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left
    from pymonet.validation import Validation, Success as Validation_Success

    def mapper11(value):
        return value + 1

    def mapper11_2(value):
        return value + 2

    def mapper12(value):
        return value + 12

    maybe_value = Maybe.just(10)

    def filterer(value):
        return value % 2 == 0

    assert maybe_value.filter(filterer) == Maybe.just(10)
    assert maybe_value.filter(filterer).map(mapper11) == Maybe.just(11)

# Generated at 2022-06-14 03:34:51.371921
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(123) == Maybe.just(123)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(123) != Maybe.nothing()
    assert Maybe.just(123) != Maybe.just(321)
    assert Maybe.just(123) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(321)



# Generated at 2022-06-14 03:34:57.231408
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(None) == Maybe.just(None), 'test_Maybe___eq__ failed'
    assert Maybe.just(None) != Maybe.nothing(), 'test_Maybe___eq__ failed'
    assert Maybe.just(None) == Maybe.just(None), 'test_Maybe___eq__ failed'
    assert Maybe.just(2) == Maybe.just(2), 'test_Maybe___eq__ failed'
    assert Maybe.nothing() == Maybe.nothing(), 'test_Maybe___eq__ failed'


# Generated at 2022-06-14 03:35:03.483960
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(42) == Maybe.just(42)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(42) != Maybe.nothing()
    assert Maybe.just(42) != Maybe.just(12)
    assert Maybe.just(12) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(12)



# Generated at 2022-06-14 03:35:05.602591
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.nothing()


# Generated at 2022-06-14 03:35:08.343314
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(2)
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:35:21.019321
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.box import Box
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    # Equals
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) == Maybe.just(None)

    assert Maybe.just(1) == Box(1)
    assert Maybe.just(1) == Box(1)
    assert Maybe.nothing() == Box(None)

# Generated at 2022-06-14 03:35:25.350933
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(1, True)



# Generated at 2022-06-14 03:35:33.516735
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()

# Generated at 2022-06-14 03:35:38.773264
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:35:47.546726
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try

    one = 1
    two = 2
    three = 3
    four = 4

    def divide(dividend, divider):
        return dividend / divider

    def multiply(value):
        return value * three

    def subtract(minuend, subtrahend):
        return minuend - subtrahend

    result_to_lazy = Try(
        divide(one, zero)
    ).to_lazy()

    assert result_to_lazy == Lazy(lambda: divide(one, zero))

# Generated at 2022-06-14 03:35:50.936490
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:35:55.324797
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(2, False).to_lazy() == Lazy(lambda: 2)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:35:58.553080
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)



# Generated at 2022-06-14 03:36:06.125124
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 4) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x < 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 4) == Maybe.nothing()



# Generated at 2022-06-14 03:36:10.919748
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(-1).filter(lambda x: x > 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:36:17.635375
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('Hello') == Maybe.just('Hello')
    assert Maybe.just(25) == Maybe.just(25)
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just([1, 3, 5]) == Maybe.just([1, 3, 5])
    assert Maybe.just({'foo': 'bar'}) == Maybe.just({'foo': 'bar'})

    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just('Hello') != Maybe.just('Hell0')
    assert Maybe.just('Hello') != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('Hell0')
    assert Maybe.just('Hello') != Maybe.just(25)
    assert Maybe.just(True) != Maybe.just(False)

# Generated at 2022-06-14 03:36:20.900507
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:36:38.375399
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    m = Maybe.nothing()
    assert m.__eq__(Maybe.nothing()) is True

    m1 = Maybe.just('value')
    assert m1.__eq__(Maybe.just('value')) is True
    assert m1.__eq__(Maybe.nothing()) is False
    assert m1.__eq__(Maybe.just(9)) is False


# Generated at 2022-06-14 03:36:42.920398
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    def api_call():
        return Maybe.just(1)

    def api_call_without_data():
        return Maybe.nothing()

    assert api_call() == api_call()
    assert api_call() != api_call_without_data()


# Generated at 2022-06-14 03:36:48.090009
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.just(3) != Maybe.nothing()


# Generated at 2022-06-14 03:36:52.058017
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:36:57.873358
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    The test for method filter of class Maybe.

    :return: None
    """
    def filterer(value, border=0):
        return value > border

    assert Maybe.just(1).filter(filterer) == Maybe.just(1)
    assert Maybe.just(-1).filter(filterer) == Maybe.nothing()
    assert Maybe.just(-1).filter(filterer, border=-1) == Maybe.just(-1)
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()

# Generated at 2022-06-14 03:37:00.008103
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe = Maybe(1, False)
    other = Maybe(1, False)
    assert maybe == other



# Generated at 2022-06-14 03:37:04.503166
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda n: n > 5) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda n: n > 5) == Maybe.nothing()
    assert Maybe.just(6).filter(lambda n: n > 5) == Maybe.just(6)


# Generated at 2022-06-14 03:37:08.083007
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:37:12.883079
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:37:16.609515
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, True) == Maybe(None, True)
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(None, True)
    assert Maybe(1, False) != Maybe(None, False)
    assert Maybe(1, False) != Maybe(None, True)


# Generated at 2022-06-14 03:37:45.692483
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 10) == Maybe.nothing()
    assert Maybe.just(11).filter(lambda x: x > 10) == Maybe.just(11)
    assert Maybe.nothing().filter(lambda x: x > 10) == Maybe.nothing()



# Generated at 2022-06-14 03:37:49.576247
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(10) != Maybe.just(11)
    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(10)



# Generated at 2022-06-14 03:37:51.964860
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:37:57.837678
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    print("Testing Maybe.__eq__()...", end="")

    assert Maybe.nothing() != None
    assert Maybe.just("test") == Maybe.just("test")
    assert Maybe.nothing() == Maybe.nothing()
    assert "test" != Maybe.nothing()

    print("OK")



# Generated at 2022-06-14 03:38:04.410927
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1).__eq__(Maybe.just(1)) \
        and Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing().__eq__(Maybe.nothing()) \
        and Maybe.nothing() == Maybe.nothing()
    assert not Maybe.nothing().__eq__(Maybe.just(1)) \
        and Maybe.nothing() != Maybe.just(1)
    assert not Maybe.just(1).__eq__(Maybe.nothing()) \
        and Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:38:11.288344
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__.
    """
    # Test for empty Maybes
    assert Maybe.nothing() == Maybe.nothing()
    # Test for not equal Maybes
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    # Test for equal Maybes
    assert Maybe.just(1) == Maybe.just(1)


# Generated at 2022-06-14 03:38:23.601735
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor
    from pymonet.monad import Monad

    # Check class inheritance
    assert issubclass(Maybe, Functor), "Class Maybe must inherit from class Functor"
    assert issubclass(Maybe, Monad), "Class Maybe must inherit from class Monad"

    # Check attributes
    assert hasattr(Maybe, 'value'), "Class Maybe must have attribute value"
    assert hasattr(Maybe, 'is_nothing'), "Class Maybe must have attribute is_nothing"

    # Check return values
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1), \
        "When Maybe not empty and filterer returns True method filter must return new instance of Maybe with the same value"

# Generated at 2022-06-14 03:38:28.972756
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:38:35.618636
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(4)
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)
    assert Maybe.just(3) != None
    assert Maybe.nothing() != None


# Generated at 2022-06-14 03:38:38.801627
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(6).filter(lambda x: x > 5) == Maybe.just(6)
    assert Maybe.just(6).filter(lambda x: x > 6) == Maybe.nothing()


# Generated at 2022-06-14 03:39:33.107355
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(15) == Maybe.just(15)
    assert Maybe.just(15) != Maybe.just(14)
    assert Maybe.just(15) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:40.523724
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(2)
    result = maybe.filter(lambda x: x > 1)
    assert isinstance(result, Maybe)
    assert result == maybe

    maybe = Maybe.just(1)
    result = maybe.filter(lambda x: x > 1)
    assert result.is_nothing

    maybe = Maybe.nothing()
    result = maybe.filter(lambda x: x > 1)
    assert result.is_nothing


# Generated at 2022-06-14 03:39:46.066934
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(4)
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(7) != 'Just 7'
    assert Maybe.nothing() != 'Just 7'


# Generated at 2022-06-14 03:39:49.514512
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)
    assert Maybe(5, False).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:39:54.469130
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:39:59.873751
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just("test,test,test").filter(lambda str: str == 'test,test,test') == Maybe.just('test,test,test')
    assert Maybe.just("test,test,test").filter(lambda str: str == 'test,test,test1') == Maybe.nothing()



# Generated at 2022-06-14 03:40:03.404741
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    x = Maybe.just(5)
    y = Maybe.just(5)
    z = Maybe.nothing()

    assert (x == x) == True
    assert (x == y) == True
    assert (x == z) == False
    assert (y == z) == False


# Generated at 2022-06-14 03:40:06.383040
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:40:10.359837
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_maybe import Maybe

    maybe = Maybe.just(2)
    assert maybe.filter(lambda v: v != 2) == Maybe.nothing()
    assert maybe.filter(lambda v: v == 2) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda v: False) == Maybe.nothing()


# Generated at 2022-06-14 03:40:14.839639
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:41:09.070556
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value: int) -> bool:
        return value < 10

    assert Maybe.just(5).filter(filterer) == Maybe.just(5)
    assert Maybe.just(10).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:41:15.449379
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:41:24.445475
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1).get_or_else('fail') == 1
    assert Maybe.just(1).filter(lambda x: x == 2).get_or_else('success') == 'success'
    assert Maybe.just(1).filter(lambda x: x == 1).get_or_else(2) == 1
    assert Maybe.just(1).filter(lambda x: x == 2).get_or_else(2) == 2

