

# Generated at 2022-06-14 03:31:29.426764
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x > 1) == Maybe.just(2)



# Generated at 2022-06-14 03:31:31.564850
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy().get() == None
    assert Maybe.just(42).to_lazy().get() == 42



# Generated at 2022-06-14 03:31:35.463752
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(12) == Maybe.just(12)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(12) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(12)


# Generated at 2022-06-14 03:31:41.334192
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)


# Generated at 2022-06-14 03:31:45.027140
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(2, False).to_lazy() == Lazy(lambda: 2)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:31:49.740172
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    assert Maybe.just(True).filter(lambda x: x == True) == Maybe.just(True)
    assert Maybe.just(True).filter(lambda x: x == False) == Maybe.nothing
    assert Maybe.nothing().filter(lambda x: x == True) == Maybe.nothing
    assert Maybe.nothing().filter(lambda x: x == False) == Maybe.nothing


# Generated at 2022-06-14 03:31:56.254486
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('hello') == Maybe.just('hello')
    assert Maybe.just('hello') == Maybe.just('hello')


# Generated at 2022-06-14 03:32:01.204353
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Maybe(1, False) == Maybe(1, False).to_lazy().fmap(Try).fmap(lambda x: x.value).value()

# Generated at 2022-06-14 03:32:05.194671
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:10.017853
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:17.471919
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    actual = Maybe.just(4).filter(lambda x: x > 2)
    expected = Maybe.just(4)
    assert actual == expected

    actual = Maybe.just(4).filter(lambda x: x < 2)
    expected = Maybe.nothing()
    assert actual == expected


# Generated at 2022-06-14 03:32:27.070208
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    lazy1 = Lazy(lambda: 1)
    result = Maybe.just(1).to_lazy()

    assert isinstance(result, Lazy)
    assert result == lazy1
    assert result.call() == 1
    assert result.call() == 1
    assert result.call() == 1

    result = Maybe.nothing().to_lazy()
    assert isinstance(result, Lazy)
    assert result.call() is None
    assert result.call() is None
    assert result.call() is None


# Generated at 2022-06-14 03:32:30.490514
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != 1



# Generated at 2022-06-14 03:32:34.535449
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:41.909927
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    m_1 = Maybe.just(5)
    m_2 = Maybe.nothing()

    assert m_1.filter(lambda x: x == 5) == Maybe.just(5)
    assert m_1.filter(lambda x: x != 5) == Maybe.nothing()

    assert m_2.filter(lambda x: x == 5) == Maybe.nothing()
    assert m_2.filter(lambda x: x != 5) == Maybe.nothing()



# Generated at 2022-06-14 03:32:53.622890
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe
    """
    m1 = Maybe.just(4)
    m2 = Maybe.just(10)
    m3 = Maybe.nothing()
    assert m1.filter(lambda x: x % 2 == 0) == Maybe.just(4)
    assert m1.filter(lambda x: x % 2 == 1) == Maybe.nothing()
    assert m2.filter(lambda x: x % 2 == 0) == Maybe.just(10)
    assert m2.filter(lambda x: x % 2 == 1) == Maybe.nothing()
    assert m3.filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert m3.filter(lambda x: x % 2 == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:32:56.614494
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(21).filter(lambda x: x < 21) == Maybe.nothing()
    assert Maybe.just(21).filter(lambda x: x >= 21) == Maybe.just(21)


# Generated at 2022-06-14 03:33:02.061897
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Given
    x = Maybe(1, False)
    y = Maybe(2, False)
    z = Maybe(2, False)
    nothing = Maybe.nothing()

    # Then
    assert x == x
    assert x != y
    assert z == y
    assert z != nothing
    assert nothing != nothing



# Generated at 2022-06-14 03:33:07.463496
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()


# Generated at 2022-06-14 03:33:13.740044
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, True) != Maybe(2, False)
    assert Maybe(1, False) != Maybe(2, True)


# Generated at 2022-06-14 03:33:19.747360
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:33:23.709674
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.just(True) == Maybe.nothing()


# Generated at 2022-06-14 03:33:26.852251
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x > 0) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:33:32.827718
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:33:37.001137
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value: int) -> bool:
        return value % 2 == 0

    assert Maybe.just(2).filter(filterer) == Maybe.just(2)
    assert Maybe.just(1).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:33:45.616502
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    def method_1(x: int) -> int:
        return x + 1

    def method_2(x: int) -> int:
        return x * 2

    def method_3(x: int) -> int:
        return x ** 2

    result1 = Maybe.just(1).map(method_1).map(method_2).map(method_3)
    result2 = Maybe.just(1).map(method_1).map(method_2).bind(lambda x: Maybe.just(method_3(x)))

    print(result1, result2)
    print(result1 == result2)


# Generated at 2022-06-14 03:33:49.927450
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False)
    assert Maybe(5, True) == Maybe(None, True)
    assert Maybe(5, False) != Maybe(6, False)
    assert Maybe(5, True) != Maybe(6, True)


# Generated at 2022-06-14 03:34:02.372010
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test Maybe_to_lazy function.

    :returns: Nothing
    :rtype: Nothing
    """
    from pymonet.lazy import Lazy

    def func_0():
        return 0

    def func_1():
        return 10

    lazy_object = Maybe.just(func_0).to_lazy()

    assert(lazy_object is not None)
    assert(lazy_object.evaluate() == 0)
    assert(lazy_object.evaluate() == 0)
    assert(lazy_object.evaluate() == 0)

    lazy_object = Maybe.just(func_1).to_lazy()

    assert(lazy_object is not None)
    assert(lazy_object.evaluate() == 10)
    assert(lazy_object.evaluate() == 10)

# Generated at 2022-06-14 03:34:08.378112
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:13.114678
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:34:23.944290
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    # Test case #1
    assert Maybe.nothing().to_lazy().force() is None

    # Test case #2
    assert Maybe.just(5).to_lazy().force() == 5

    # Test case #3
    assert Maybe.just(6.66).to_lazy().force() == 6.66

    # Test case #4
    assert Maybe.just([1, 2, 3]).to_lazy().force() == [1, 2, 3]

    # Test case #5
    assert Maybe.just((1, 2, 3)).to_lazy().force() == (1, 2, 3)

    # Test case #6
    assert Maybe.just([]).to_lazy().force() == []

    # Test case #7

# Generated at 2022-06-14 03:34:30.197239
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(42).filter(lambda y: y <= 0) == Maybe.nothing()
    assert Maybe.just(42).filter(lambda y: y > 0) == Maybe.just(42)
    assert Maybe.just(42.9).filter(lambda y: y <= 0) == Maybe.nothing()
    assert Maybe.just(42.9).filter(lambda y: y > 0) == Maybe.just(42.9)
    assert Maybe.just(42).filter(lambda y: y <= 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda y: y > 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda y: y <= 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:36.079975
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(
        lambda x: x < 3
    ) == Maybe.just(2)

    assert Maybe.just(2).filter(
        lambda x: x > 3
    ) == Maybe.nothing()

    assert Maybe.nothing().filter(
        lambda x: x == 3
    ) == Maybe.nothing()



# Generated at 2022-06-14 03:34:38.940625
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x == 6) == Maybe.nothing()



# Generated at 2022-06-14 03:34:44.686295
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    success = (
        Maybe.just(1) == Maybe.just(1),
        Maybe.just(1) != Maybe.just(2),
        Maybe.nothing() == Maybe.just(1),
        Maybe.nothing() == Maybe.just(2),
        Maybe.nothing() != Maybe.nothing()
    )

    if not all(s == True for s in success):
        raise AssertionError('Maybe.__eq__ is not working correctly')



# Generated at 2022-06-14 03:34:50.179329
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x % 2 == 1) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda x: x % 2 == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:34:58.758148
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Maybe.just(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert (Maybe.just(2).to_lazy()
            .map(lambda x: x + 2)
            .get() == 4)
    assert (Maybe.nothing().to_lazy()
            .map(lambda x: x + 2)
            .get() == None)
    assert (Maybe.just(2).to_lazy()
            .flat_map(lambda x: Lazy(lambda: x + 2))
            .get() == 4)

# Generated at 2022-06-14 03:35:08.844715
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.maybe import Maybe
    from pymonet.either import Left, Right
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.list import List
    from pymonet.stream import Stream
    from pymonet.maybe import Maybe

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) == Box.nothing()
    assert Maybe.just(None) == Try.fail(None)
    assert Maybe.just(None) == Lazy(lambda: None)
    assert Maybe.just(None) == Validation.success(None)
    assert Maybe.just(None)

# Generated at 2022-06-14 03:35:13.330675
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.just(3).filter(lambda x: True) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: False) == Maybe.nothing()

# Generated at 2022-06-14 03:35:17.229950
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:35:27.494331
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    eq_(Maybe.just(5), Maybe.just(5))
    assert_false(Maybe.just(5) == Maybe.just(8))
    assert_false(Maybe.just(5) == Maybe.nothing())
    assert_false(Maybe.nothing() == Maybe.just(8))
    eq_(Maybe.nothing(), Maybe.nothing())



# Generated at 2022-06-14 03:35:29.806108
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:35:37.040911
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:35:42.493875
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    val = 1
    just_maybe = Maybe.just(val)
    assert just_maybe == Maybe.just(val)
    assert not just_maybe == Maybe.just(2)
    assert not just_maybe == Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:35:50.757812
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False)  # check that not empty Maybe is equal to not empty Maybe
    assert Maybe(10, False) != Maybe(5, False)  # check that not empty Maybe is not equal to not empty Maybe
    assert Maybe(None, True) == Maybe(None, True)  # check that empty Maybe is equal to empty Maybe
    assert Maybe(None, True) != Maybe(None, False)  # check that empty Maybe is not equal to not empty Maybe
    assert Maybe(None, False) != Maybe(None, True)  # check that not empty Maybe is not equal to empty Maybe


# Generated at 2022-06-14 03:35:55.980030
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)



# Generated at 2022-06-14 03:35:59.681541
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)


# Generated at 2022-06-14 03:36:02.940772
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    a = Maybe(1, False)
    b = a.to_lazy()
    assert b.get() == 1

# Generated at 2022-06-14 03:36:09.028733
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def func(v):
        return bool(v)

    assert Maybe.just("").filter(func) == Maybe.just("")
    assert Maybe.just("1").filter(func) == Maybe.just("1")
    assert Maybe.just(1).filter(func) == Maybe.just(1)
    assert Maybe.just(None).filter(func) == Maybe.nothing()
    assert Maybe.nothing().filter(func) == Maybe.nothing()



# Generated at 2022-06-14 03:36:13.050417
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:36:21.696851
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    x = Maybe.just(1)
    assert x.filter(lambda x: x % 2 == 0).is_nothing and \
        x.filter(lambda x: x % 2 == 1) == x


# Generated at 2022-06-14 03:36:25.373445
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:36:37.246478
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    def test_Maybe_filter_with_empty_Maybe():
        Maybe.nothing().filter(lambda x: False).get_or_else(1) == None

    def test_Maybe_filter_with_not_empty_Maybe_and_filterer_which_returns_False():
        Maybe.just(1).filter(lambda x: False).get_or_else(1) == 1

    def test_Maybe_filter_with_not_empty_Maybe_and_filterer_which_returns_True():
        Maybe.just(1).filter(lambda x: True).get_or_else(1) == 1

    def test_box():
        Maybe.just(1).to_box().map(lambda x: x + 1) == Maybe.just(2)

    def test_either():
        Maybe.just(1).to_

# Generated at 2022-06-14 03:36:42.626766
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.either import Right, Left
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    # when
    result = Maybe.just(1) == Maybe.just(1)

    # expect
    assert result



# Generated at 2022-06-14 03:36:50.544619
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_nothing = Maybe.nothing()
    maybe_1 = Maybe.just(1)
    maybe_2 = Maybe.just(2)
    assert (maybe_nothing == maybe_nothing) == True
    assert (maybe_1 == maybe_1) == True
    assert (maybe_1 == maybe_2) == False
    assert (maybe_1 == maybe_nothing) == False
    assert (maybe_nothing == maybe_1) == False
    assert (maybe_nothing == 2) == False


# Generated at 2022-06-14 03:36:56.117480
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # assert Maybe(1, False) == Maybe(1, False)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:37:01.323882
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: True) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()


# Generated at 2022-06-14 03:37:05.039421
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(1)

    assert maybe.to_lazy() == Lazy(lambda: 1)

    maybe = Maybe.nothing()

    assert maybe.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:37:10.972418
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Test case 1
    assert Maybe.just(1)\
        .filter(lambda x: x == 1) == Maybe.just(1)

    # Test case 2
    assert Maybe.just(1)\
        .filter(lambda x: x != 1) == Maybe.nothing()

    # Test case 3
    assert Maybe.nothing()\
        .filter(lambda x: x == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:37:19.682689
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_just_1 = Maybe.just(1)
    maybe_just_1_copy = Maybe.just(1)
    maybe_just_2 = Maybe.just(2)
    maybe_nothing = Maybe.nothing()
    maybe_nothing_copy = Maybe.nothing()
    assert maybe_just_1 == maybe_just_1_copy
    assert maybe_just_2 == Maybe.just(2)
    assert maybe_nothing == maybe_nothing_copy
    assert maybe_just_1 != maybe_just_2
    assert maybe_just_1 != maybe_nothing
    assert maybe_nothing != maybe_just_2


# Generated at 2022-06-14 03:37:29.125876
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('one') == Maybe.just('one')
    assert Maybe.just('one') != Maybe.just('two')
    assert Maybe.just('one') == Maybe.just('one')
    assert Maybe.just('one') != Maybe.just('two')


# Generated at 2022-06-14 03:37:36.029018
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != 1
    assert Maybe.just(1) != None
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()

if __name__ == "__main__":
    test_Maybe___eq__()

# Generated at 2022-06-14 03:37:39.520112
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x == 3) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x != 3) == Maybe.nothing()

# Generated at 2022-06-14 03:37:43.388471
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe(2, False)
    lazy = maybe.to_lazy()
    assert lazy == Lazy(lambda: 2), 'test_Maybe_to_lazy'



# Generated at 2022-06-14 03:37:45.923664
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:37:49.773091
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(10)
    assert Maybe.just(10) != Maybe.just(11)


# Generated at 2022-06-14 03:37:52.119672
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(10, False).to_lazy() == Lazy(lambda: 10)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:55.917233
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:38:01.202805
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:04.173922
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, True)


# Generated at 2022-06-14 03:38:21.797019
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(None)
    assert Maybe.just(1) != Maybe.just({})
    assert Maybe.just({}) != Maybe.just(1)


# Generated at 2022-06-14 03:38:25.279611
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def test_function():
        return "test"

    assert Maybe.just("test").to_lazy() == Lazy(test_function)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:38:29.063326
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe.

    """
    print('Unit test for method __eq__ of class Maybe')
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    print('Test is OK!')


# Generated at 2022-06-14 03:38:40.551853
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor
    from pymonet.applicative import Applicative

    print('Test method filter in Maybe\n')
    # create Maybe with value 4
    maybe_test = Maybe.just(4)
    # method filter takes function and return new Maybe with value 4 because 4 < 5 is true
    maybe = maybe_test.filter(lambda x: x < 5)
    Functor(maybe).assert_functor_laws()
    Applicative(maybe).assert_applicative_laws()
    assert maybe == Maybe.just(4)

    maybe_test = Maybe.just(5)
    maybe = maybe_test.filter(lambda x: x < 5)
    assert maybe == Maybe.nothing()

    maybe_test = Maybe.nothing()
    maybe = maybe_test.filter(lambda x: x < 5)


# Generated at 2022-06-14 03:38:47.980683
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(10).__eq__(Maybe.just(10))
    assert Maybe.just(10).__eq__(Maybe.just(10)) is False
    assert Maybe.just(10).__eq__(Maybe.nothing()) is False
    assert Maybe.nothing().__eq__(Maybe.nothing())
    assert Maybe.nothing().__eq__(Maybe.nothing()) is False
    assert Maybe.nothing().__eq__(Maybe.just(10)) is False


test_Maybe___eq__()



# Generated at 2022-06-14 03:38:51.342196
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(4) != Maybe.nothing()


# Generated at 2022-06-14 03:38:56.434477
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:39:05.564903
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    actual = Maybe.just(1).to_lazy()
    expected = Lazy(lambda: 1)

    assert isinstance(actual, type(expected))
    Functor.covariant(actual.value, lambda x: x  + 1, expected, lambda x: x + 1)

    actual = Maybe.nothing().to_lazy()
    expected = Lazy(lambda: None)

    assert isinstance(actual, type(expected))
    Functor.covariant(actual.value, lambda x: x is None, expected, lambda x: x is None)


# Generated at 2022-06-14 03:39:13.981891
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just({'name': 'John', 'age': 50}) == Maybe.just({'name': 'John', 'age': 50})
    assert Maybe.just(100) != Maybe.just(200)
    assert Maybe.just(100) != Maybe.just(None)
    assert Maybe.just(None) != Maybe.just(100)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(True) != Maybe.just(False)
    assert Maybe.just(False) != Maybe.just(True)
    assert Maybe.just(False) == Maybe.just(False)
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just(None) == Maybe.nothing()

# Generated at 2022-06-14 03:39:19.120776
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:38.147702
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # When Maybe is empty
    m1 = Maybe(1, True)
    m2 = Maybe(2, True)
    m3 = Maybe(3, True)

    result1 = m1.filter(lambda x: x == 2)
    assert result1.is_nothing

    # When Maybe is not empty and filterer returns true
    result2 = m2.filter(lambda x: x == 2)
    assert not result2.is_nothing
    assert 2 == result2.value

    # When Maybe is not empty and filterer returns false
    result3 = m3.filter(lambda x: x == 2)
    assert result3.is_nothing

# Generated at 2022-06-14 03:39:45.507246
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    monad = Maybe.just(12)
    monad2 = Maybe.just(12)
    monad3 = Maybe.just(6)
    monad4 = Maybe.nothing()
    monad5 = Maybe.nothing()

    assert monad == monad2
    assert monad2 == monad
    assert not (monad3 == monad2)
    assert not (monad2 == monad3)
    assert monad4 == monad5
    assert monad5 == monad4



# Generated at 2022-06-14 03:39:49.402404
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, True) == Maybe(1, True)


# Generated at 2022-06-14 03:39:53.479605
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(1)
    lazy = maybe.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.evaluate() == 1


# Generated at 2022-06-14 03:39:58.973515
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    mb = Maybe.just(Lazy(lambda: 1))
    assert mb.to_lazy() == mb.value

    mb = Maybe.nothing()
    assert mb.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:40:03.371573
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 3) == Maybe.just(1).map(lambda x: x+2).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:40:05.673924
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:40:09.475596
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) == Maybe.just(5) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) != Maybe.nothing()


# Generated at 2022-06-14 03:40:15.542085
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:40:21.415125
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.box import Box
    from pymonet.monad_try import Try

    even = lambda x: x % 2 == 0

    assert Maybe(1, False).filter(even) == Maybe.nothing()
    assert Maybe(2, False).filter(even) == Maybe.just(2)
    assert Maybe.nothing().filter(even) == Maybe.nothing()

    # Test for Box and Try
    assert Box(1).filter(even) == Box(None)
    assert Box(2).filter(even) == Box(2)
    assert Try(1, is_success=True).filter(even) == Try(None, is_success=False)
    assert Try(2, is_success=True).filter(even) == Try(2, is_success=True)

# Generated at 2022-06-14 03:40:42.942239
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor

    class Foo(Functor):
        """
        Foo functor for tests
        """

        def __init__(self, x):
            self._x = x

        def fmap(self, f):
            return Foo(f(self._x))

        def __eq__(self, other):
            return isinstance(other, Foo) and self._x == other._x

    def is_even(a):
        return a % 2 == 0

    not_even = Maybe.just(Foo(1)).filter(is_even)
    assert isinstance(not_even, Maybe)
    assert not_even.is_nothing

    even = Maybe.just(Foo(2)).filter(is_even)
    assert isinstance(even, Maybe)
    assert not even.is_nothing


# Generated at 2022-06-14 03:40:49.216147
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe(1, False)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe(None, True)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:40:59.759034
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    import pymonet.monad as monad

    get_10 = monad.Maybe.just(10)
    get_25 = monad.Maybe.just(25)
    get_nothing = monad.Maybe.nothing()

    assert get_10.filter(lambda x: x == 10) == monad.Maybe.just(10)
    assert get_10.filter(lambda x: x < 15) == monad.Maybe.just(10)
    assert get_10.filter(lambda x: x > 15) == monad.Maybe.nothing()
    assert get_25.filter(lambda x: x == 10) == monad.Maybe.nothing()
    assert get_25.filter(lambda x: x < 15) == monad.Maybe.nothing()
    assert get_25.filter(lambda x: x > 15) == monad.Maybe

# Generated at 2022-06-14 03:41:04.933942
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:41:08.187510
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test case checking to_lazy method of class Maybe.
    """
    assert(Maybe.just(5).to_lazy() == Lazy(lambda: 5))
    assert(Maybe.nothing().to_lazy() == Lazy(lambda: None))

# Generated at 2022-06-14 03:41:14.949298
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10)
    assert Maybe.just(10).filter(lambda x: x > 15) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 5) == Maybe.nothing()



# Generated at 2022-06-14 03:41:24.943390
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    >>> test_Maybe_filter()
    True
    """
    # Check not empty Maybe
    assert Maybe.just('str').filter(lambda x: x is not None) == Maybe.just('str')
    assert Maybe.just('str').filter(lambda x: x is None) == Maybe.nothing()

    # Check empty Maybe
    assert Maybe.nothing().filter(lambda x: x is not None) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x is None) == Maybe.nothing()

    return True
