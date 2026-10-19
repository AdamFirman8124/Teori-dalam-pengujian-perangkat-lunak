

# Generated at 2022-06-14 03:31:35.753873
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # arrange
    m1 = Maybe.just(1)
    m2 = Maybe.just(1)
    m3 = Maybe.just(2)
    m4 = Maybe.just(False)
    m5 = Maybe.just(None)

    # act

    # assert
    assert m1 == m2
    assert m1 != m3
    assert m1 != m4
    assert m1 != m5



# Generated at 2022-06-14 03:31:38.933314
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(5).to_lazy().call() == 5
    assert Maybe.nothing().to_lazy().call() == None



# Generated at 2022-06-14 03:31:48.082876
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # When Maybe is empty and filterer returns True:
    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()
    # When Maybe is empty and filterer returns False:
    assert Maybe.nothing().filter(lambda _: False) == Maybe.nothing()
    # When Maybe is not empty and filterer returns True:
    assert Maybe.just(1).filter(lambda _: True) == Maybe.just(1)
    # When Maybe is not empty and filterer returns False:
    assert Maybe.just(1).filter(lambda _: False) == Maybe.nothing()



# Generated at 2022-06-14 03:31:58.076537
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # True
    assert Maybe.just(True).filter(lambda x: x == True) == Maybe.just(True)
    assert Maybe.just(True).filter(lambda x: x == False) == Maybe.nothing()

    # False
    assert Maybe.just(False).filter(lambda x: x == False) == Maybe.just(False)
    assert Maybe.just(False).filter(lambda x: x == True) == Maybe.nothing()

    # Empty
    assert Maybe.nothing().filter(lambda x: x == False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == True) == Maybe.nothing()



# Generated at 2022-06-14 03:32:08.918060
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Arrange
    class A:
        pass
    instance1 = A()
    instance2 = A()
    some_maybe = Maybe.just(instance1)
    nothing_maybe = Maybe.nothing()

    # Act and assert
    assert some_maybe == some_maybe, 'Some maybe not equals to itself'
    assert some_maybe != nothing_maybe, 'Some maybe still equals to nothing'
    assert nothing_maybe == nothing_maybe, 'Nothing maybe not equals to itself'

    other_some_maybe = Maybe.just(instance1)
    assert some_maybe == other_some_maybe, 'Some maybe not equals to the same maybe'

    other_some_maybe.value = instance2
    assert some_maybe != other_some_maybe, 'Some maybe still equals to maybe with another value'


# Generated at 2022-06-14 03:32:11.605758
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:32:18.425627
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(5)
    lazy_object = maybe.to_lazy()
    assert isinstance(lazy_object, Lazy)
    assert lazy_object.evaluate() == 5

    maybe_nothing = Maybe.nothing()
    lazy_object_nothing = maybe_nothing.to_lazy()
    assert isinstance(lazy_object_nothing, Lazy)
    assert lazy_object_nothing.evaluate() is None


# Generated at 2022-06-14 03:32:25.832411
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe.
    """
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) == Maybe.just(2.0)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:29.689970
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe(1, False)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.nothing() == Maybe(None, True)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:32:42.123580
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just({1, 2, 3}) == Maybe.just({3, 2, 1})
    assert Maybe.just({1, 2, 3}) != Maybe.just({1, 2})
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just({1, 2, 3}) == Maybe.just({3, 2, 1})
    assert Maybe.just({1, 2, 3}) != Maybe.just({1, 2})
    assert Maybe.just(None) != Maybe.nothing()
   

# Generated at 2022-06-14 03:32:53.622592
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe_1 = Maybe.just(10)
    maybe_2 = Maybe.nothing()

    maybe_3 = maybe_1.filter(lambda x: x > 1)
    maybe_4 = maybe_1.filter(lambda x: x < 1)
    maybe_5 = maybe_2.filter(lambda x: x > 1)
    maybe_6 = maybe_2.filter(lambda x: x < 1)

    assert maybe_3 == maybe_1
    assert maybe_4 == maybe_2
    assert maybe_5 == maybe_2
    assert maybe_6 == maybe_2


# Generated at 2022-06-14 03:32:58.429422
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.monads import Just

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() == Just(None)
    assert Maybe.nothing() != Just(1)
    assert Maybe.just(1) == Just(1)
    assert Maybe.just(1) != Just(1.0)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:33:03.393969
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    m1 = Maybe.just(2)
    m2 = Maybe.just(2)
    m3 = Maybe.just(3)
    m4 = Maybe.nothing()
    m5 = Maybe.nothing()

    assert m1 == m2
    assert m1 != m3
    assert m4 == m5
    assert m1 != m4
    assert m3 != m4

    assert m1 == m2
    assert m1 != m3
    assert m4 == m5
    assert m1 != m4
    assert m3 != m4



# Generated at 2022-06-14 03:33:09.203762
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result = Maybe.just(1).filter(lambda x: x == 1)
    expected = Maybe.just(1)
    assert result == expected

    result = Maybe.just(1).filter(lambda x: x != 1)
    expected = Maybe.nothing()
    assert result == expected

    result = Maybe.nothing().filter(lambda x: x == 1)
    expected = Maybe.nothing()
    assert result == expected



# Generated at 2022-06-14 03:33:12.912532
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda v: v > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v > 0) == Maybe.nothing()

# Generated at 2022-06-14 03:33:18.822525
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy

    lazy1: Maybe[Lazy] = Maybe.just(Lazy(lambda: "value"))
    lazy2: Maybe[Lazy] = Maybe.nothing()

    assert lazy1.to_lazy() == Lazy(lambda: "value")
    assert lazy2.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:20.900854
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:33:25.661406
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for Maybe.filter

    :returns: True when Maybe.filter works as expected
    :rtype: Boolean
    """
    def is_even(num):
        return num % 2 == 0

    return Maybe.just(2).filter(is_even) == Maybe.just(2) \
        and Maybe.just(1).filter(is_even) == Maybe.nothing() \
        and Maybe.nothing().filter(is_even) == Maybe.nothing()


# Generated at 2022-06-14 03:33:32.507111
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2).__eq__(Maybe.just(2)) == True
    assert Maybe.just(1).__eq__(Maybe.just(2)) == False
    assert Maybe.nothing().__eq__(Maybe.just(2)) == False
    assert Maybe.just(2).__eq__(Maybe.nothing()) == False


# Generated at 2022-06-14 03:33:41.578999
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    print(
        Maybe.just(1).filter(lambda x: x == 1) ==
        Maybe.just(2).filter(lambda x: x == 1)
    )  # False
    print(
        Maybe.just(1).filter(lambda x: x == 1).filter(lambda x: x == 1) ==
        Maybe.just(1).filter(lambda x: x == 1)
    )  # True
    print(
        Maybe.just(1).filter(lambda x: x == 1) ==
        Maybe.nothing().filter(lambda x: x == 1)
    )  # True
    print(
        Maybe.nothing().filter(lambda x: x == 1) ==
        Maybe.nothing().filter(lambda x: x == 1)
    )  # True

# Generated at 2022-06-14 03:33:51.564962
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) \
        .map(lambda x: x + 1) == Maybe.just(2)
    assert Maybe.nothing() \
        .map(lambda x: x + 1) == Maybe.nothing()


# Generated at 2022-06-14 03:33:58.409310
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(2, False) == Maybe(2, False)
    assert Maybe(2, True) == Maybe(2, True)
    assert Maybe(2, False) != Maybe(2, True)
    assert Maybe(2, True) != Maybe(2, False)
    assert Maybe(2, False) != Maybe(3, False)
    assert Maybe(2, True) != Maybe(3, True)


# Generated at 2022-06-14 03:34:02.167801
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.just(1) == Maybe.just(1))
    assert(Maybe.just(1) != Maybe.just(0))
    assert(Maybe.just(1) != Maybe.nothing())
    assert(Maybe.nothing() == Maybe.nothing())


# Generated at 2022-06-14 03:34:08.181159
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """__eq__ method is equal when it the same types with the same value."""
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(None) != Maybe.nothing()



# Generated at 2022-06-14 03:34:14.368922
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    print('test_Maybe___eq__')
    assert Maybe.just(42) == Maybe.just(42)
    assert Maybe.just(43) != Maybe.nothing()
    assert Maybe.just(44) != Maybe.just(45)
    assert Maybe.nothing() == Maybe.nothing()
    print('passed')


# Generated at 2022-06-14 03:34:17.746923
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just('string').to_lazy() == Lazy(lambda: 'string')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:34:20.945805
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(6)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:34:24.770912
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:28.740969
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(4).filter(lambda x: x > 0) == Maybe.just(4)
    assert Maybe.just(4).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:34.524690
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False)
    assert Maybe(5, False) != Maybe(7, False)
    assert Maybe(5, False) != Maybe(7, True)
    assert Maybe(5, False) != Maybe(7, False)
    assert Maybe(5, True) == Maybe(7, True)


# Generated at 2022-06-14 03:34:47.375420
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe
    """
    assert Maybe.just(12).filter(lambda x: x >= 10) == Maybe.just(12)



# Generated at 2022-06-14 03:34:51.916744
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:35:00.249354
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # test for True if two Maybe instances contains the same data
    assert Maybe(5, False) == Maybe(5, False)
    assert Maybe(5, True) == Maybe(5, True)

    # test for False if two Maybe instances contains different data
    assert not (Maybe(5, False) == Maybe(5, True))
    assert not (Maybe(5, False) == Maybe(None, False))
    assert not (Maybe(5, True) == Maybe(None, True))


# Generated at 2022-06-14 03:35:04.605286
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.just(123) == Maybe.just(123))
    assert(Maybe.just(123) != Maybe.just(321))
    assert(Maybe.nothing() == Maybe.nothing())
    assert(Maybe.nothing() != Maybe.just(123))


# Generated at 2022-06-14 03:35:08.965180
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, True) == Maybe(5, True)
    assert Maybe(5, False) == Maybe(5, False)
    assert Maybe(5, False) != Maybe(5, True)
    assert Maybe(5, True) != Maybe(5, False)
    assert Maybe(5, False) != Maybe(10, False)
    assert Maybe(5, True) != Maybe(10, True)


# Generated at 2022-06-14 03:35:17.100659
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe.just(4)
    maybe2 = Maybe.just(4)
    maybe3 = Maybe.just('4')
    assert maybe1 == maybe2
    assert not maybe1 == maybe3
    assert not maybe2 == maybe3
    assert Maybe.nothing() == Maybe.nothing()
    assert not Maybe.nothing() != Maybe.nothing()
    assert not maybe1 == Maybe.nothing()
    assert not Maybe.nothing() == maybe1

# Unit tests for methods __init__, just, nothing of class Maybe

# Generated at 2022-06-14 03:35:28.699074
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # setup
    from pymonet.functions import compose, identity
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.either import Left
    from pymonet.box import Box
    from pymonet.functions import compose
    number_to_validation = compose(Maybe.just, Validation.success)
    number_to_lazy = compose(Maybe.just, Lazy)
    number_to_try = compose(Maybe.just, Try)
    number_to_left = compose(Maybe.just, Left)
    number_to_box = compose(Maybe.just, Box)

    def filterer(value):
        return value % 2 == 0

    # generate values for testing for class Maybe
   

# Generated at 2022-06-14 03:35:33.088497
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    import pytest

    # GIVEN
    maybe = Maybe.just(100)
    expected_result = Lazy(lambda: 100)

    # WHEN
    actual_result = maybe.to_lazy().value

    # THEN
    assert actual_result == expected_result.value



# Generated at 2022-06-14 03:35:35.925409
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def identity(x: int) -> int:
        return x

    assert identity(Maybe.just(1).to_lazy().get()) == 1
    assert identity(Maybe.nothing().to_lazy().get()) == None


# Generated at 2022-06-14 03:35:43.806173
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    a = Maybe.just(1)
    b = Maybe.just(2)
    c = Maybe.just(3)

    assert a.filter(lambda x: x == 1) == Maybe.just(1)
    assert a.filter(lambda x: x == 2) == Maybe.nothing()
    assert b.filter(lambda x: x == 1) == Maybe.nothing()
    assert c.filter(lambda x: x == 3) == Maybe.just(3)

# Generated at 2022-06-14 03:35:59.506469
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    first_lazy = Maybe.just(42).to_lazy()
    second_lazy = Maybe.nothing().to_lazy()

    assert isinstance(first_lazy, Lazy)
    assert isinstance(second_lazy, Lazy)
    assert first_lazy.calc() == 42
    assert second_lazy.calc() is None



# Generated at 2022-06-14 03:36:07.260836
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Maybe.just(Box(Lazy(lambda: 10))).to_lazy() == Lazy(lambda: 10)
    assert Maybe.just(Lazy(lambda: 10)).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:36:11.847263
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    def is_integer(value):
        return isinstance(value, int)

    assert Maybe.just(2).filter(is_integer) == Maybe.just(2)
    assert Maybe.just('2').filter(is_integer) == Maybe.nothing()
    assert Maybe.nothing().filter(is_integer) == Maybe.nothing()

# Generated at 2022-06-14 03:36:14.937793
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def is_even(x: int) -> bool:
        return x % 2 == 0

    assert Maybe(1, False).filter(is_even) == Maybe.nothing(), 'function filter is not work with odd number'
    assert Maybe(2, False).filter(is_even) == Maybe.just(2), 'function filter is not work with even number'
    assert Maybe(None, True).filter(is_even) == Maybe.nothing(), 'function filter is not work with None'

# Generated at 2022-06-14 03:36:21.645893
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monoid import maybe_mempty_instance

    # Test when Maybe is not empty
    value = Maybe.just('toto')
    assert value.to_lazy() == Lazy(lambda: value.value)

    # Test when Maybe is empty
    value = Maybe.nothing()
    assert value.to_lazy() == maybe_mempty_instance



# Generated at 2022-06-14 03:36:28.221364
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    may = Maybe.just(10)
    lazy = may.to_lazy()
    assert lazy == Lazy(lambda: 10)

    may = Maybe.nothing()
    lazy = may.to_lazy()
    assert lazy == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:33.503361
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(1)
    assert maybe.filter(lambda number: number % 2 == 0) == Maybe.nothing()
    assert maybe.filter(lambda number: number % 2 == 1) == Maybe.just(1)


if __name__ == "__main__":
    test_Maybe_filter()

# Generated at 2022-06-14 03:36:36.204011
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:36:40.138405
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for to_lazy method of class Maybe.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert isinstance(Maybe.just(25).to_lazy(), Lazy)

# Generated at 2022-06-14 03:36:46.612825
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(12)
    assert maybe.filter(lambda x: x == 12) == Maybe.just(12)
    assert maybe.filter(lambda x: x == 13) == Maybe.nothing()
    maybe = Maybe.nothing()
    assert maybe.filter(lambda x: x == 12) == Maybe.nothing()
    assert maybe.filter(lambda x: x == 13) == Maybe.nothing()

# Generated at 2022-06-14 03:37:00.494047
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: True) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()



# Generated at 2022-06-14 03:37:06.543928
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # fn is true
    assert Maybe.just(1).filter(lambda v: v == 1) == Maybe.just(1)
    assert Maybe.just([1, 2]).filter(lambda v: 1 in v) == Maybe.just([1, 2])

    # fn is false
    assert Maybe.just(1).filter(lambda v: v > 1) == Maybe.nothing()
    assert Maybe.just([1, 2]).filter(lambda v: 3 in v) == Maybe.nothing()

    # Nothing
    assert Maybe.nothing().filter(lambda v: v == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:37:09.532545
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(1)
    assert maybe.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:37:12.183168
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:37:15.629530
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    result = Maybe.just(5).to_lazy().force()
    assert result == 5

    result = Maybe.nothing().to_lazy().force()
    assert result == None


# Generated at 2022-06-14 03:37:21.094580
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert (Maybe.just(5).filter(lambda x: x > 2) == Maybe.just(5))
    assert (Maybe.just(5).filter(lambda x: x < 2) == Maybe.nothing())
    assert (Maybe.nothing().filter(lambda x: True) == Maybe.nothing())



# Generated at 2022-06-14 03:37:26.073317
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(True).filter(lambda x: x == True) == Maybe.just(True)
    assert Maybe.just(False).filter(lambda x: x == True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == True) == Maybe.nothing()


# Generated at 2022-06-14 03:37:29.182280
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x % 3 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()

# Generated at 2022-06-14 03:37:34.152878
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe

    m = Maybe.just(1)
    l = m.to_lazy()

    assert(m == l.force())


# Generated at 2022-06-14 03:37:45.131288
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # GIVEN
    val_1 = Maybe.just(2)
    val_2 = Maybe.just(3)
    val_3 = Maybe.nothing()
    val_4 = Maybe.nothing()
    # WHEN
    # THEN
    assert Maybe.just(2).filter(lambda x: x == 2) == val_1
    assert Maybe.just(2).filter(lambda x: x == 3) == val_3
    assert Maybe.nothing().filter(lambda x: x == 3) == val_4
    assert Maybe.just(3).filter(lambda x: x == 2) == val_3
    assert Maybe.just(3).filter(lambda x: x == 3) == val_2
    assert Maybe.nothing().filter(lambda x: x == 2) == val_4


# Generated at 2022-06-14 03:37:57.988291
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(2, False).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:38:02.474876
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert (Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10))
    assert (Maybe.just(10).filter(lambda x: x < 5) == Maybe.nothing())
    assert (Maybe.nothing().filter(lambda x: x > 5) == Maybe.nothing())



# Generated at 2022-06-14 03:38:07.728624
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(4, False).filter(lambda x : x > 3) == Maybe(4, False)
    assert Maybe(4, False).filter(lambda x : x < 3) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x : x > 3) == Maybe.nothing()


# Generated at 2022-06-14 03:38:11.810935
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    from pymonet.lazy import Lazy

    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)
    assert Maybe(1, True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:17.160429
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe_value = Maybe.just(1)
    maybe_empty = Maybe.nothing()

    assert maybe_empty.to_lazy().from_lazy() == None
    assert maybe_value.to_lazy().from_lazy() == 1



# Generated at 2022-06-14 03:38:24.680835
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    maybe = Maybe.just(2)
    assert maybe.to_lazy() == Lazy(lambda: 2)
    assert maybe.to_try() == Try(2, is_success=True)
    assert maybe.to_validation() == Validation.success(2)

    maybe = Maybe.nothing()
    assert maybe.to_lazy() == Lazy(lambda: None)
    assert maybe.to_try() == Try(None, is_success=False)
    assert maybe.to_validation() == Validation.success(None)



# Generated at 2022-06-14 03:38:28.238018
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe_1 = Maybe.just(True)

    maybe_2 = Maybe.just(False)

    maybe_3 = Maybe.nothing()

    assert maybe_1.filter(lambda value: value is True) == Maybe.just(True)

    assert maybe_2.filter(lambda value: value is True) == Maybe.nothing()

    assert maybe_3.filter(lambda value: value is True) == Maybe.nothing()



# Generated at 2022-06-14 03:38:33.245997
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda a: a == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda a: a == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: a == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:38:38.142932
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:38:49.685356
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.either import Left, Right
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()

    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(-1).filter(lambda x: x > 0) == Maybe.nothing()

    assert Maybe.just(1).filter(lambda x: x > 0).to_either() == Right(1)
    assert Maybe.just(-1).filter(lambda x: x > 0).to_either() == Left(None)

    assert Maybe.just(1).filter(lambda x: x > 0).to_box() == Box(1)

# Generated at 2022-06-14 03:39:03.804156
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe(2, False).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert (Maybe.nothing().filter(lambda x: x % 2 == 0) ==
            Maybe.nothing())


# Generated at 2022-06-14 03:39:11.040207
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    f = lambda x: x in range(0,10)
    maybe = Maybe(5, False)

    assert maybe.filter(f).__eq__(Maybe.just(5))

    maybe = Maybe(5, True)

    assert maybe.filter(f).__eq__(Maybe.nothing())

    maybe = Maybe(15, False)

    assert maybe.filter(f).__eq__(Maybe.nothing())


# Generated at 2022-06-14 03:39:16.328315
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(2, False).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe(3, False).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:39:19.394864
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().get() == 1
    assert Maybe.nothing().to_lazy().get() == None

# Generated at 2022-06-14 03:39:24.543855
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 5) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x < 5) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)


# Generated at 2022-06-14 03:39:27.695714
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:30.702870
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda v: v == 2) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda v: v == 3) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v == 2) == Maybe.nothing()



# Generated at 2022-06-14 03:39:34.593658
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:40.681578
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def gt_5(x: int) -> bool:
        return x > 5

    assert Maybe.just(10).filter(gt_5) == Maybe.just(10)
    assert Maybe.just(4).filter(gt_5) == Maybe.nothing()
    assert Maybe.nothing().filter(gt_5) == Maybe.nothing()


# Generated at 2022-06-14 03:39:42.613731
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe(1, False).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:40:03.037779
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    func = lambda x: x > 4
    assert Maybe.just(5).filter(func).value == 5
    assert Maybe.just(1).filter(func) == Maybe.nothing()
    assert Maybe.nothing().filter(func) == Maybe.nothing()


# Generated at 2022-06-14 03:40:12.847308
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import FunctorTest
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    functor_test = FunctorTest(Maybe, lambda x: Maybe.just(x * 2), lambda x: Maybe.just(x - 2), Maybe.nothing())
    functor_test.check_identity()
    functor_test.check_associativity()
    functor_test.check_map()

    assert Maybe.just(2).filter(lambda x: x < 3).get_or_else(5) == 2
    assert Maybe.just(2).filter(lambda x: x > 3).get_or_else(5) == 5
    assert Maybe.nothing().filter(lambda x: x > 3).get_or_else(5)

# Generated at 2022-06-14 03:40:24.837760
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.either import Left
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Maybe.just(1).filter(
        lambda x: x == 1
    ) == Maybe.just(1)
    assert Maybe.just(2).filter(
        lambda x: x == 1
    ).is_nothing
    assert Maybe.nothing().filter(
        lambda x: x == 1
    ).is_nothing

    # Unit test for class Maybe with another monads
    assert Maybe.just(1).to_either() == Right(1)
    assert Maybe.nothing().to_either().left == None
    assert Maybe.just(1).to_box() == Box(1)
    assert Maybe.nothing().to_box().get_value() == None

# Generated at 2022-06-14 03:40:28.640690
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x < 2) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x > 2) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)


# Generated at 2022-06-14 03:40:34.837534
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left

    def my_function():
        return "hello"

    result = Maybe.just(my_function).to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == my_function()

    result = Maybe.nothing().to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == None



# Generated at 2022-06-14 03:40:37.363806
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    unit = Maybe.just(2)
    assert unit.to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:40:43.537945
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # create Box with value 10
    assert Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10)
    assert Maybe.just(10).filter(lambda x: x > 15) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 5) == Maybe.nothing()


# Generated at 2022-06-14 03:40:48.514121
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    Just = Maybe.just
    Nothing = Maybe.nothing
    assert Just(1).filter(lambda x: x < 5) == Just(1)
    assert Just(5).filter(lambda x: x < 5) == Nothing()
    assert Nothing().filter(lambda x: x < 5) == Nothing()

# Generated at 2022-06-14 03:40:55.044776
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def throwing() -> int:
        raise Exception("Error")
    assert Maybe.just(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(throwing()).to_lazy() == Lazy(lambda: throwing())
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:40:57.294933
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
