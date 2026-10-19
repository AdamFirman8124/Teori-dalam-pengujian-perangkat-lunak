

# Generated at 2022-06-14 03:31:38.629216
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, True) != Maybe(2, False)
    assert Maybe(None, True) == Maybe(None, True)
    assert Maybe(None, False) != Maybe(None, True)



# Generated at 2022-06-14 03:31:41.440055
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().get == 1
    assert Maybe.nothing().to_lazy().get == None



# Generated at 2022-06-14 03:31:43.033649
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Box(5) == Box(5)



# Generated at 2022-06-14 03:31:46.949534
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(42) == Maybe.just(42)
    assert Maybe.just(42) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(42) != Maybe.just('42')


# Generated at 2022-06-14 03:31:50.912474
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(30).filter(lambda x: x >= 30) == Maybe.just(30)
    assert Maybe.just(20).filter(lambda x: x >= 30) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x >= 30) == Maybe.nothing()


# Generated at 2022-06-14 03:31:56.763012
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:31:59.087558
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:32:03.661215
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) == Maybe(2, False)
    assert Maybe(1, True) == Maybe(2, True)
    assert Maybe(1, False) == Maybe(1, True)
    assert Maybe(1, True) == Maybe(1, False)



# Generated at 2022-06-14 03:32:11.827790
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe(10, True) == Maybe(10, True)
    assert Maybe(10, False) != Maybe(20, False)
    assert Maybe(10, True) != Maybe(20, True)
    assert Maybe(10, False) != Maybe(10, True)
    assert Maybe(10, True) != Maybe(10, False)
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just(10) != Maybe.just(20)
    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(10)



# Generated at 2022-06-14 03:32:16.100918
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:32:24.045605
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x > 0) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x < 0) == Maybe.nothing()



# Generated at 2022-06-14 03:32:28.865902
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.nothing() == Maybe.nothing())
    assert(Maybe.just(1) == Maybe.just(1))
    assert(Maybe.just(1) != Maybe.just(2))
    assert(Maybe.just(1) != Maybe.nothing())
    assert(Maybe.nothing() != Maybe.just(1))


# Generated at 2022-06-14 03:32:33.887293
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 1) == Maybe.nothing()


# Generated at 2022-06-14 03:32:38.828818
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda value: value > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda value: value < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: value > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:32:41.910696
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:47.439469
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v == 1) == Maybe.just(1)
    assert Maybe.just(0).filter(lambda v: v == -1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:32:56.892624
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe
    """

    # Just one value
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()

    # Just multiple values
    assert Maybe.just(2).filter(lambda x: x == 2) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x == 3) == Maybe.nothing()

    # Nothing
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 2) == Maybe.nothing()



# Generated at 2022-06-14 03:33:01.455222
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just('a') != Maybe.just('b')
    assert Maybe.just('a') != Maybe.nothing()



# Generated at 2022-06-14 03:33:07.080311
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(q: int): return q == 1
    m = Maybe.just(1)
    m1 = m.filter(filterer)
    assert m == m1
    n = Maybe.nothing()
    n1 = n.filter(filterer)
    assert n == n1


if __name__ == '__main__':
    print(test_Maybe_filter())

# Generated at 2022-06-14 03:33:11.765031
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe(15, False) != Maybe(10, False)
    assert Maybe(15, True) == Maybe(15, True)
    assert Maybe(10, False) != Maybe(10, True)
    assert Maybe(15, True) != Maybe(10, True)


# Generated at 2022-06-14 03:33:20.655012
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe.just(5)
    maybe2 = Maybe.just(5)
    maybe3 = Maybe.just(8)
    maybe4 = Maybe.nothing()
    maybe5 = Maybe.nothing()

    assert maybe1 == maybe2
    assert maybe1 != maybe3
    assert maybe4 == maybe5
    assert maybe1 != maybe5
    assert maybe1 != maybe3



# Generated at 2022-06-14 03:33:24.991168
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    empty = Maybe.nothing()
    not_empty = Maybe.just(3)
    greater_then_4 = Maybe.just(5)

    assert empty.filter(lambda x: x > 3) == empty
    assert not_empty.filter(lambda x: x > 3) == empty
    assert greater_then_4.filter(lambda x: x > 3) == greater_then_4



# Generated at 2022-06-14 03:33:31.954388
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    nothing = Maybe.nothing()
    assert nothing.filter(lambda x: x % 2 == 0) == Maybe.nothing()

    just = Maybe.just(2)
    assert just.filter(lambda x: x % 2 == 0) == Maybe.just(2)

    assert just.filter(lambda x: x % 2 == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:33:41.202502
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Maybe instances with Equal values
    Maybe_123_is_nothing_False = Maybe(123, False)
    Maybe_123_is_nothing_False_1 = Maybe(123, False)
    Maybe_123_is_nothing_False_2 = Maybe(123, False)

    Maybe_456_is_nothing_True = Maybe(456, True)
    Maybe_456_is_nothing_True_1 = Maybe(456, True)
    Maybe_456_is_nothing_True_2 = Maybe(456, True)

    # Maybe instances with different values
    Maybe_123_is_nothing_True = Maybe(123, True)
    Maybe_456_is_nothing_False = Maybe(456, False)

    # Maybe instances with different types
    Maybe_123_nothingness = Maybe(123, True)
    Maybe_123_nothingness_

# Generated at 2022-06-14 03:33:43.607752
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:33:50.209579
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.either import Either

    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(True) != Maybe.just(False)
    assert Maybe.just(True) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(True)
    assert Maybe.just(True) != Either.right(True)
    assert Maybe.nothing() != Either.right(True)



# Generated at 2022-06-14 03:33:57.368289
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test Maybe.to_lazy() method.

    :returns: Nothing
    :raises: ValidationError
    """
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Maybe.just("lazy").to_lazy() == Lazy(lambda: "lazy")
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:34:01.565805
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:34:06.177463
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:34:07.491018
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:19.320925
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Maybe.just(42).to_lazy() == Lazy(lambda: 42)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    # Test of laziness
    global _some_var
    _some_var = 'initial'

    def set_foo():
        global _some_var
        _some_var = 'foo'
        return 'something'

    assert Try(set_foo).to_lazy().value() == 'something'
    assert _some_var == 'initial'


# Generated at 2022-06-14 03:34:24.633352
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(2)
    assert maybe.to_lazy() == Lazy(lambda: 2)

    maybe2 = Maybe.nothing()
    assert maybe2.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:34:31.783050
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def test_function(a: int) -> bool:
        return a < 10

    result = Maybe.just(5).filter(test_function)
    expected = Maybe.just(5)
    assert result == expected, "Test failed for Maybe.filter() when Maybe is not empty"

    result = Maybe.just(-1).filter(test_function)
    expected = Maybe.nothing()
    assert result == expected, "Test failed for Maybe.filter() when Maybe is empty"

    result = Maybe.nothing().filter(test_function)
    expected = Maybe.nothing()
    assert result == expected, "Test failed for Maybe.filter() when Maybe is empty"


# Generated at 2022-06-14 03:34:35.392234
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:34:40.140636
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    success_test = Maybe(1, False) == Maybe(1, False)
    fail_test = Maybe(1, False) == Maybe(2, False) \
        or Maybe(1, False) == Maybe(2, True) \
        or Maybe(1, True) == Maybe(2, False)

    assert success_test and not fail_test
# Test case finish



# Generated at 2022-06-14 03:34:46.487993
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Arrange
    m1: Maybe[int] = Maybe.just(10)
    m2: Maybe[int] = Maybe.just(10)
    m3: Maybe[int] = Maybe.nothing()

    # Act
    m11 = m1.filter(lambda value: value == 10)
    m12 = m2.filter(lambda value: value < 5)
    m13 = m3.filter(lambda value: value < 5)

    # Assert
    assert m11 == Maybe.just(10)
    assert m12 == Maybe.nothing()
    assert m13 == Maybe.nothing()

# Generated at 2022-06-14 03:34:51.785639
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: True) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()

# Generated at 2022-06-14 03:34:55.354557
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Maybe(Box(5), False).to_lazy() == Lazy(lambda: Box(5))
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:34:59.977805
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:35:06.274661
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(1)
    another_maybe = maybe.filter(lambda v: v == 1)
    assert isinstance(maybe, Maybe)
    assert isinstance(another_maybe, Maybe)
    assert maybe == another_maybe

    maybe = Maybe.just(1)
    another_maybe = maybe.filter(lambda v: v == 2)
    assert isinstance(another_maybe, Maybe)
    assert another_maybe == Maybe.nothing()

    maybe = Maybe.nothing()
    another_maybe = maybe.filter(lambda v: v == 1)
    assert isinstance(another_maybe, Maybe)
    assert another_maybe == Maybe.nothing()



# Generated at 2022-06-14 03:35:14.214567
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda _: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda _: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()

# Generated at 2022-06-14 03:35:21.128011
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy, LazyValueError
    from pymonet.maybe import Maybe
    from pymonet import lazy_invoker, LazyResult

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    def test_lazy_func():
        return 5

    maybe_lazy = Maybe.just(test_lazy_func).to_lazy()

    assert isinstance(maybe_lazy, Lazy)
    assert lazy_invoker(maybe_lazy) == LazyResult(5, False)



# Generated at 2022-06-14 03:35:31.935253
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Try

    result = \
        Maybe.just(Try.from_value(1)).filter(lambda x: True).get_or_else(None)
    expected = Try.from_value(1)
    assert result == expected

    result = \
        Maybe.just(Try.from_value(1)).filter(lambda x: False).get_or_else(None)
    expected = None
    assert result == expected

    result = Maybe.just(Try.from_exception(Exception("test")).filter(lambda x: True).get_or_else(None))
    expected = None
    assert result == expected

    result = Maybe.nothing().filter(lambda x: True).get_or_else(None)
    expected = None
    assert result == expected



# Generated at 2022-06-14 03:35:34.107380
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(1, False).to_lazy().value() == 1


# Generated at 2022-06-14 03:35:38.820366
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(True).filter(lambda a: a) == Maybe.just(True)
    assert Maybe.just(False).filter(lambda a: a) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: a) == Maybe.nothing()



# Generated at 2022-06-14 03:35:42.469129
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x < 2) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 2) == Maybe.nothing()


# Generated at 2022-06-14 03:35:48.173231
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def bigger_than_zero(num: int) -> bool:
        return num > 0

    maybe = Maybe.just(2)
    maybe_filtered = maybe.filter(bigger_than_zero)

    assert maybe_filtered == Maybe.just(2)

    maybe = Maybe.just(-1)
    maybe_filtered = maybe.filter(bigger_than_zero)

    assert maybe_filtered == Maybe.nothing()



# Generated at 2022-06-14 03:35:57.412357
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe_test = Maybe.just("test")
    assert maybe_test.filter(lambda x: x == "test") == Maybe.just("test")
    assert maybe_test.filter(lambda x: x != "test") == Maybe.nothing()
    maybe_test_2 = Maybe.just("test1")
    assert maybe_test_2.filter(lambda x: x == "test") == Maybe.nothing()
    assert maybe_test_2.filter(lambda x: x == "test1") == Maybe.just("test1")



# Generated at 2022-06-14 03:36:02.031616
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: x) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 2) == Maybe.nothing()

# Generated at 2022-06-14 03:36:06.302233
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:36:20.279275
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(2, True).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe(2, False).filter(lambda x: x == 2) == Maybe.just(2)
    assert Maybe(3, False).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe(None, True).filter(lambda x: x is None) == Maybe.nothing()


# Generated at 2022-06-14 03:36:31.552078
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.asserts import assert_maybe_equal

    # Given
    def filterer(x: int) -> bool:
        return x > 5

    # When
    maybe = Maybe(4, False)

    # Then
    assert_maybe_equal(
        # Expected
        Maybe.nothing(),

        # Actual
        maybe.filter(filterer)
    )

    # Given
    func = lambda x: x > 0

    # When
    maybe = Maybe.just(5)

    # Then
    assert_maybe_equal(
        # Expected
        Maybe.just(5),

        # Actual
        maybe.filter(func)
    )



# Generated at 2022-06-14 03:36:36.354135
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe_value = Maybe.just(5)
    lazy_value = maybe_value.to_lazy()
    assert lazy_value.value() == 5

    maybe_none = Maybe.nothing()
    lazy_none = maybe_value.to_lazy()
    assert lazy_none.value() == None



# Generated at 2022-06-14 03:36:44.589150
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        if value == 2:
            return True
        return False

    assert Maybe.just(None).filter(filterer).is_nothing == True
    assert Maybe.just(1).filter(filterer).is_nothing == True
    assert Maybe.just(2).filter(filterer).is_nothing == False
    assert Maybe.just(2).filter(filterer).value == 2

    # Test if second argument is None
    def filterer_none(value):
        return None

    assert Maybe.just(None).filter(filterer_none).is_nothing == True
    assert Maybe.just(1).filter(filterer_none).is_nothing == True
    assert Maybe.just(2).filter(filterer_none).is_nothing == False

# Generated at 2022-06-14 03:36:52.031051
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # filter
    assert Maybe(1, is_nothing=False).filter(lambda x: True) == Maybe(1, is_nothing=False)
    assert Maybe(2, is_nothing=False).filter(lambda x: x % 2 == 0) == Maybe(2, is_nothing=False)
    assert Maybe(3, is_nothing=False).filter(lambda x: x % 2 == 0) == Maybe(None, is_nothing=True)

# Generated at 2022-06-14 03:36:58.878014
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.asserts import assert_that

    number = Just(20)
    empty = Nothing()

    assert_that(
        actual=number.filter(lambda x: 10 < x < 30),
        equal_to=Just(20)
    )

    assert_that(
        actual=number.filter(lambda x: 10 > x),
        equal_to=Nothing()
    )

    assert_that(
        actual=empty.filter(lambda x: x == 10),
        equal_to=Nothing()
    )

    assert_that(
        actual=empty.filter(lambda x: x == None),
        equal_to=Nothing()
    )


# Generated at 2022-06-14 03:37:03.850075
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # Test case 1: empty Maybe
    maybe = Maybe.nothing()

    lazy = maybe.to_lazy()

    assert lazy.value() is None

    # Test case 2: not empty Maybe
    maybe = Maybe.just(23)

    lazy = maybe.to_lazy()

    assert lazy.value() == 23


# Generated at 2022-06-14 03:37:10.544900
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    m = Maybe.just(5)
    assert m == m.filter(lambda x: x > 4)
    assert m.filter(lambda x: x > 4) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing().filter(lambda x: x > 4)
    assert Maybe.nothing() == m.filter(lambda x: x < -4)
    assert Maybe.nothing() == Maybe.nothing().filter(lambda x: x < -4)



# Generated at 2022-06-14 03:37:13.486144
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:37:21.518325
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just([1, 2, 3]).filter(lambda lst: any(x == 2 for x in lst)) == Maybe.just([1, 2, 3])
    assert Maybe.just(2).filter(lambda x: x > 1) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x < 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()


# Generated at 2022-06-14 03:37:29.988536
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(1)
    assert maybe.filter(lambda x: x == 1) == Maybe.just(1)
    assert maybe.filter(lambda x: x == 0) == Maybe.nothing()

    maybe = Maybe.nothing()
    assert maybe.filter(lambda x: x == 1) == Maybe.nothing()
    assert maybe.filter(lambda x: x == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:37:34.312564
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def test_value():
        return 5

    assert Maybe.just(test_value()).to_lazy() == Lazy(test_value)


# Generated at 2022-06-14 03:37:44.526949
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_validation import Validation

    maybe, maybe2 = Maybe.just(True), Maybe.just(False)

    validation = Validation.success(True)
    maybe_validation = Maybe.just(validation)
    maybe_validation2 = Maybe.just(Validation.success(False))

    def filterer(value):
        return value

    assert maybe.filter(filterer) == Maybe.just(True)
    assert maybe2.filter(filterer) == Maybe.nothing()

    assert maybe_validation.filter(filterer) == Maybe.just(validation)
    assert maybe_validation2.filter(filterer) == Maybe.nothing()



# Generated at 2022-06-14 03:37:52.888987
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from operator import add

    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: add(1, 2)) == Maybe.just(add).to_lazy().map(lambda f: f(1, 2))
    assert Lazy(lambda: 3) == Maybe.just(add).to_lazy().map(lambda f: f(1, 2)).to_maybe().map(lambda x: x())
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()
    assert Lazy(lambda: None) == Maybe.just(1).to_lazy().filter(lambda x: x == 2)

# Generated at 2022-06-14 03:38:01.849525
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Lazy(lambda: 1).to_maybe() == Lazy(lambda: 1)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)
    assert Maybe(1, True).to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy() == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:38:10.045768
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def test_function(value, left_value=''):
        return value

    just_maybe = Maybe.just(1)
    assert just_maybe.to_lazy() == Lazy(lambda: 1), 'to_lazy of Maybe returns incorrect Lazy'

    nothing_maybe = Maybe.nothing()
    assert nothing_maybe.to_lazy() == Lazy(lambda: None), 'to_lazy of Maybe returns incorrect Lazy'



# Generated at 2022-06-14 03:38:23.525053
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.maybe import Maybe

    test_simple_value = Maybe.just(5).filter(lambda x: x > 3)
    assert test_simple_value.is_nothing == False
    assert test_simple_value == Maybe.just(5)

    test_simple_value = Maybe.just(5).filter(lambda x: x > 10)
    assert test_simple_value.is_nothing == True
    assert test_simple_value == Maybe.nothing()

    test_simple_value = Maybe.just(None).filter(lambda x: x > 5)
    assert test_simple_value.is_nothing == True
    assert test_simple_value == Maybe.nothing()

    test_simple_value = Maybe.nothing().filter(lambda x: x > 5)
    assert test_simple_value.is_nothing == True

# Generated at 2022-06-14 03:38:35.766657
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test Maybe.to_lazy method.
    """
    from pymonet.monad_maybe import Maybe, MaybeType

    from pymonet.lazy import Lazy

    monad: MaybeType = Maybe.just(6)
    print('monad.to_lazy()', monad.to_lazy(), sep=' = ')
    assert monad == Maybe.just(6)
    print('monad.to_lazy().value()', monad.to_lazy().value(), sep=' = ')
    assert monad == Maybe.just(6)
    assert isinstance(monad.to_lazy(), Lazy)
    assert monad.to_lazy().value() == 6


# Generated at 2022-06-14 03:38:39.834901
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x < 3) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x > 3) == Maybe.nothing()

# Generated at 2022-06-14 03:38:44.075419
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:58.893503
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    test_data = [
        (Maybe.just(3), lambda x: x == 3, Maybe.just(3)),
        (Maybe.just(3), lambda x: x == 2, Maybe.nothing()),
        (Maybe.nothing(), lambda x: False, Maybe.nothing())
    ]

    for value, filterer, expected in test_data:
        assert value.filter(filterer) == expected

    print('[✔] test_Maybe_filter()')


# Generated at 2022-06-14 03:39:06.642624
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(2)
    assert maybe.filter(lambda x : x > 0) == Maybe.just(2)
    assert maybe.filter(lambda x : x > 5) == Maybe.nothing()
    assert maybe.filter(lambda x : x < 0) == Maybe.nothing()
    assert maybe.filter(lambda x : x == 1) == Maybe.nothing()
    assert maybe.filter(lambda x : x == 2) == Maybe.just(2)
    assert maybe.filter(lambda x : x % 2 == 0) == Maybe.just(2)

    maybe = Maybe.nothing()
    assert maybe.filter(lambda x : x > 0) == Maybe.nothing()
    assert maybe.filter(lambda x : x < 0) == Maybe.nothing()


# Generated at 2022-06-14 03:39:12.309125
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x < 2) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda x: x < 2) == Maybe.nothing()
    assert Maybe.just(3).filter(lambda x: x < 2) == Maybe.nothing()

# Generated at 2022-06-14 03:39:18.914689
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def eq(a, b):
        return a == b

    assert Maybe.just(2).filter(lambda x: x == 2) == Maybe.just(2)
    assert Maybe.nothing().filter(eq) == Maybe.nothing()
    assert Maybe.just(1).filter(eq) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(None) == Maybe.nothing()



# Generated at 2022-06-14 03:39:22.531133
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(2).to_lazy() \
        .value() == 2
    assert Maybe.nothing().to_lazy() \
        .value() is None


# Generated at 2022-06-14 03:39:28.308144
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    expected = "Some not empty value"
    from pymonet.lazy import Lazy

    maybe = Maybe.just(expected)
    lazy = maybe.to_lazy()

    assert lazy == Lazy(lambda: expected)
    assert type(lazy) == Lazy
    assert lazy.value() == expected


# Generated at 2022-06-14 03:39:34.990756
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Test the filter method for true
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    # Test the filter method for false
    assert Maybe.just(-1).filter(lambda x: x > 0) == Maybe.nothing()
    # Test the filter method for empty
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:39:47.052295
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Try

    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()

    assert Maybe.just("as").filter(lambda x: len(x) == 2) == Maybe.just("as")
    assert Maybe.just("as").filter(lambda x: len(x) == 1) == Maybe.nothing()

    assert Maybe.just(Try.success(1)).filter(lambda x: x.is_success) == Maybe.just(
        Try.success(1)
    )

    assert Maybe.just(Try.failure(ValueError("test"))).filter(lambda x:
                                                               x.is_success) == Maybe.nothing()

# Unit

# Generated at 2022-06-14 03:39:58.867441
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Try
    from pymonet.monad_validation import Validation

    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)

    # function to be used for testing of ap for Maybe
    def _add(a: int, b: int) -> int:
        return a + b

    def _filterer(x: int) -> bool:
        return x > 2

    # testing of ap
    assert Maybe.just(_add).ap(Maybe.just(2)) == Maybe.just(2)
    assert Maybe.just(_add).ap(Maybe.nothing()) == Maybe.nothing()


# Generated at 2022-06-14 03:40:03.784160
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe.

    :returns: None
    :rtype: None
    """
    maybe = Maybe.just(1)
    maybe_filtered = maybe.filter(lambda x: x == 1)

    assert maybe_filtered == Maybe.just(1)

    maybe_filtered = maybe.filter(lambda x: x == 2)

    assert maybe_filtered == Maybe.nothing()


# Generated at 2022-06-14 03:40:20.255723
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: Lazy(lambda: 1))
    assert Maybe.nothing().to_lazy().get() is None
    assert Maybe.just(1).to_lazy().get() == 1
    assert Maybe.just(Lazy(lambda: 1)).to_lazy().get() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:40:24.104178
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:40:27.961332
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 5) == Maybe.nothing()
    assert Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10)
    assert Maybe.nothing().filter(lambda x: x > 5) == Maybe.nothing()


# Generated at 2022-06-14 03:40:30.560178
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    test_success_1()
    test_success_2()
    test_success_3()
    test_fail_1()
    test_fail_2()
    test_fail_3()


# Generated at 2022-06-14 03:40:37.958205
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x % 2 == 0) == Maybe.just(10)
    assert Maybe.just(10).filter(lambda x: x % 2 == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:40:43.086642
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def test_me():
        return 10

    assert Maybe.just(10).to_lazy() == Lazy(test_me)
    assert Maybe.nothing().to_lazy() == Lazy(test_me)

# Generated at 2022-06-14 03:40:48.008797
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.

    :returns: None
    :rtype: None
    """
    assert Maybe.just(42).to_lazy().run() == 42
    assert Maybe.nothing().to_lazy().run() is None

# Generated at 2022-06-14 03:40:53.692739
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:40:57.761454
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(None).filter(lambda x: x is None) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x > 5) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)



# Generated at 2022-06-14 03:41:04.030226
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(0).filter(lambda value: value > 0).is_nothing
    assert Maybe.just(-1).filter(lambda value: value > 0).is_nothing
    assert Maybe.just(1).filter(lambda value: value > 0) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda value: value > 0) == Maybe.just(2)

    assert Maybe.nothing().filter(lambda value: value > 0).is_nothing
    assert Maybe.nothing().filter(lambda value: value > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:41:24.973770
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:41:31.973514
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: x) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.just(False).filter(lambda x: True) == Maybe.nothing()
    assert Maybe.just(False).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(False).filter(lambda x: x) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x) == Maybe.just(1)
