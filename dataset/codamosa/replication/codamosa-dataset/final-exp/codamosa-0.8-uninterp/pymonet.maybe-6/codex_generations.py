

# Generated at 2022-06-14 03:31:34.748302
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.either import Left
    assert Maybe.just(10).__eq__(Maybe.just(10))
    assert not Maybe.just(5) == Maybe.just(10)
    assert Maybe.nothing().__eq__(Maybe.nothing())
    assert not Maybe.nothing() == Maybe.just(10)
    assert not Maybe.nothing() == Left(10)



# Generated at 2022-06-14 03:31:39.385282
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:31:45.679663
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert not Maybe.just(1) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert not Maybe.just(2) == Maybe.nothing()
    assert not Maybe.nothing() == Maybe.just(1)
    assert not Maybe.nothing() == Maybe.just(None)


# Generated at 2022-06-14 03:31:52.294189
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(42).filter(lambda x: x != 0) == Maybe.just(42)
    assert Maybe.nothing().filter(lambda x: x != 0) == Maybe.nothing()
    assert Maybe.just(0).filter(lambda x: x != 0) == Maybe.nothing()

    assert Maybe.just(42).filter(lambda x: x == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 0) == Maybe.nothing()
    assert Maybe.just(0).filter(lambda x: x == 0) == Maybe.just(0)


# Generated at 2022-06-14 03:31:58.171164
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    lazy_maybe = Maybe.just(2).map(lambda x: x * 2).to_lazy()
    assert lazy_maybe.value() == 4, "lazy_maybe.value() must be equal 4"


# Generated at 2022-06-14 03:32:08.998743
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from unittest import TestCase
    from pymonet.lazy import Lazy

    class ExtendedTestCase(TestCase):
        def assertEqual(self, first, second):
            if isinstance(first, Lazy):
                first = first.evaluate()
            if isinstance(second, Lazy):
                second = second.evaluate()
            super().assertEqual(first, second)

    test_case = ExtendedTestCase()

    test_case.assertEqual(
        Maybe.nothing().to_lazy(),
        Lazy(lambda: None)
    )

    test_case.assertEqual(
        Maybe.just(1).to_lazy(),
        Lazy(lambda: 1)
    )


if __name__ == '__main__':
    import unittest

    unittest.main()

# Generated at 2022-06-14 03:32:12.772091
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    a = Maybe.just(1)
    b = Maybe.just(2)
    c = Maybe.nothing()
    assert a == Maybe.just(1)
    assert b == Maybe.just(2)
    assert c == Maybe.nothing()
    assert not a == b
    assert not a == c
    assert not b == c


# Generated at 2022-06-14 03:32:19.911616
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_1 = Maybe(1, False)
    maybe_2 = Maybe(1, False)
    maybe_3 = Maybe(2, False)
    maybe_4 = Maybe(None, True)
    maybe_5 = Maybe(None, True)

    assert maybe_1 == maybe_2
    assert not maybe_1 == maybe_3
    assert maybe_4 == maybe_5
    assert not maybe_4 == maybe_1
    assert maybe_1 != maybe_3
    assert maybe_4 != maybe_1
    assert not maybe_1 != maybe_2
    assert not maybe_4 != maybe_5



# Generated at 2022-06-14 03:32:30.779087
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Arrange
    maybe_none = Maybe.nothing()
    maybe_zero = Maybe.just(0)
    maybe_1 = Maybe.just(1)
    maybe_181 = Maybe.just(181)

    # Act
    maybe_zero_filtered = maybe_zero.filter(lambda x: x % 2 == 0)
    maybe_1_filtered = maybe_1.filter(lambda x: x % 2 == 0)
    maybe_181_filtered = maybe_181.filter(lambda x: x % 2 == 0)
    none_filtered = maybe_none.filter(lambda x: x % 2 == 0)

    # Assert
    assert maybe_zero_filtered == Maybe.just(0)
    assert maybe_1_filtered == Maybe.nothing()
    assert maybe_181_filtered == Maybe.nothing()
   

# Generated at 2022-06-14 03:32:36.895163
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe.just('1')
    assert Maybe.just(1) != Maybe.just('2')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('1')
    assert Maybe.just('1') != Maybe.nothing()


# Generated at 2022-06-14 03:32:51.619030
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor
    from pymonet.functor_laws import test_maybe_functor_laws

    def test_filter_value_to_True(value):
        return value > 0

    def even_check(value):
        return (value % 2) == 0

    def test_filter_value_to_False(value):
        return value == 0

    def test_filter_nothing_to_True(value):
        return True

    def test_filter_nothing_to_False(value):
        return False

    maybe_0 = Maybe.just(0)
    maybe_1 = Maybe.just(1)
    maybe_2 = Maybe.just(2)
    nothing = Maybe.nothing()


# Generated at 2022-06-14 03:32:57.427122
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.maybe import Maybe as MyMaybe
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    def get_value() -> int:
        return 42

    lazy_value_eager_box = MyMaybe.just(Lazy(get_value)).to_lazy()
    assert lazy_value_eager_box == \
        Lazy(lambda: Box(42))

# Generated at 2022-06-14 03:33:08.600647
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert Maybe(42, False) == Maybe(42, False)
    assert Maybe(42, False) != Maybe(42, True)
    assert Maybe(42, False) != Maybe(12, True)
    assert Maybe(42, True) != Maybe(42, False)
    assert Maybe(42, True) == Maybe(42, True)
    assert Maybe(42, False) != Maybe(12, False)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() == Maybe(None, True)
    assert Maybe.nothing() == Maybe(43, True)
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.nothing() != Maybe.just(43)

    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) == Maybe(None, False)
    assert Maybe

# Generated at 2022-06-14 03:33:14.558300
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    value = 'someValue'
    maybe = Maybe.just(value)
    lazy = maybe.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get_value() == value

    maybe = Maybe.nothing()
    lazy = maybe.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get_value() is None


# Generated at 2022-06-14 03:33:19.452914
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda v: v == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:33:23.108220
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:26.525004
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()


# Generated at 2022-06-14 03:33:32.277303
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()


# Generated at 2022-06-14 03:33:40.882073
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.box import Box
    from pymonet.validation import Validation

    assert Maybe.just(42) == Maybe.just(42)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(42) != Maybe.just(55)
    assert Maybe.just(42) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(55)
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.just(42) != Maybe.just('42')
    assert Maybe.just('42') != Maybe.just(42)
    assert Maybe.just(42) != Box(42)
    assert Maybe.just(42) != Validation.success(42)



# Generated at 2022-06-14 03:33:44.972192
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('a') == Maybe.just('a')
    assert Maybe.just(None) == Maybe.just(None)


# Generated at 2022-06-14 03:33:56.550691
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe

    :returns: None
    :rtype: None
    """
    from pymonet import Box

    Maybe.just(Box('haha')).filter(lambda box: box.value.startswith('ha')).get_or_else(Box('not found')).value == 'haha'
    Maybe.just(Box('haha')).filter(lambda box: box.value.startswith('he')).get_or_else(Box('not found')).value == 'not found'
    Maybe.just(Box('haha')).filter(lambda box: box.value.startswith('hh')).get_or_else(Box('not found')).value == 'not found'

# Generated at 2022-06-14 03:34:05.639223
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.box import Box
    from pymonet.either import Left

    good_maybe_1 = Maybe.just(4)
    good_maybe_2 = Maybe.just(4)
    good_maybe_3 = Maybe.nothing()
    good_maybe_4 = Maybe.nothing()

    assert (good_maybe_1 == good_maybe_2)
    assert (good_maybe_3 == good_maybe_4)
    assert (good_maybe_3 != good_maybe_1)
    assert (good_maybe_1 != good_maybe_3)
    assert (good_maybe_1 != good_maybe_4)
    assert (good_maybe_4 != good_maybe_1)
    assert (good_maybe_1 != 1)
    assert (good_maybe_1 != 1.1)

# Generated at 2022-06-14 03:34:10.366029
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    # We want to test that class Maybe returns True when
    # __eq__ method is called with some values or other
    # instances of Maybe class.
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:34:15.468557
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.maybe import Maybe

    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:23.267728
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.exceptions import UnsupportedOperationError

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    try:
        Maybe.just(1).to_lazy().value()
    except UnsupportedOperationError:
        assert False

    try:
        Maybe.nothing().to_lazy().value()
    except UnsupportedOperationError:
        assert False


# Generated at 2022-06-14 03:34:26.050054
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    x = Maybe.just(0)
    y = Maybe.just(0)
    z = Maybe.just(1)

    assert x == y and x != z


# Generated at 2022-06-14 03:34:30.105419
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(4).filter(lambda x: x % 2 != 0) == Maybe.nothing()
    assert Maybe.just(3).filter(lambda x: x % 2 != 0) == Maybe.just(3)
    assert Maybe.nothing().filter(lambda x: x % 2 != 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:34.826715
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:38.028834
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(4)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:46.990884
# Unit test for method __eq__ of class Maybe

# Generated at 2022-06-14 03:34:54.686528
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    l = Lazy(lambda: 2)

    assert l.eval() == Maybe.just(2).to_lazy().eval()
    assert Lazy(lambda: None).eval() == Maybe.nothing().to_lazy().eval()


if __name__ == "__main__":
    test_Maybe_to_lazy()

# Generated at 2022-06-14 03:35:06.890676
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != Maybe(2, True)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, True) != Maybe(2, False)
    assert Maybe(1, True) != Maybe.just(1)
    assert Maybe(1, True) != Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()

# Generated at 2022-06-14 03:35:15.226430
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe1 = Maybe.just(30)
    maybe2 = Maybe.just(30)
    maybe3 = Maybe.just(10)
    maybe4 = Maybe.nothing()

    def _is_even(x):
        return x % 2 == 0

    assert maybe1 == maybe2
    assert maybe2.filter(_is_even) == maybe1
    assert maybe3.filter(_is_even) == maybe4
    assert maybe4.filter(_is_even) == maybe4



# Generated at 2022-06-14 03:35:18.035090
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:35:24.615523
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(True) == Maybe.just(True).filter(lambda x: x is True)
    assert Maybe.just(True) != Maybe.just(True).filter(lambda x: x is False)
    assert Maybe.nothing() == Maybe.nothing().filter(lambda x: x)
    assert Maybe.nothing() == Maybe.just(False).filter(lambda x: x)


# Generated at 2022-06-14 03:35:29.167012
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(2)


# Generated at 2022-06-14 03:35:37.433609
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    from pymonet.monad_try import Try

    # Assert that filter return copy of self when filterer returns True
    assert \
        Try.of(Maybe.just(5).filter(lambda x: x == 5)) == \
        Try.of(Maybe.just(5))

    # Assert that filter return empty Maybe when filterer returns False
    assert \
        Try.of(Maybe.just(5).filter(lambda x: x == 4)) == \
        Try.of(Maybe.nothing())

    # Assert that filter return empty Maybe when self is empty
    assert \
        Try.of(Maybe.nothing().filter(lambda x: x == 4)) == \
        Try.of(Maybe.nothing())



# Generated at 2022-06-14 03:35:42.494526
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2) == Maybe.nothing().map(lambda a: a == 2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()



# Generated at 2022-06-14 03:35:51.042614
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just("a") == Maybe.just("a")
    assert Maybe.just(1) != Maybe.just("a")
    assert Maybe.just("a") != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just("a")
    assert Maybe.just("a") != Maybe.nothing()
    assert Maybe.nothing() == Maybe.just(None)
    assert Maybe.just(None) == Maybe.nothing()
    assert Maybe.just(None) != Maybe.just(1)


# Generated at 2022-06-14 03:35:59.030539
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0).to_either() == Right(1)
    assert Maybe.just(2).filter(lambda x: x % 2 == 0).to_either() == Right(2)
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) != Left(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0).to_either() == Left(None)

# Generated at 2022-06-14 03:36:08.071492
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda v: v < 5) == Maybe.just(1)
    assert Maybe.just(5).filter(lambda v: v < 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v < 5) == Maybe.nothing()

# Generated at 2022-06-14 03:36:14.612377
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(0).filter(lambda x: x == 0) == Maybe.just(0)
    assert Maybe.just(0).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(0).filter(lambda x: True) == Maybe.just(0)
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.just(0).filter(None) == Maybe.just(0)
    assert Maybe.nothing().filter(None) == Maybe.nothing()



# Generated at 2022-06-14 03:36:19.674175
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test for method to_lazy of class Maybe.
    """

    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:36:25.066462
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    m = Just(True)
    assert m.filter(lambda x: x) == m
    m = Just(False)
    assert m.filter(lambda x: x) != m
    assert m.filter(lambda x: x) == Nothing


# Generated at 2022-06-14 03:36:27.602222
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    empty_maybe = Maybe.nothing()
    assert empty_maybe == Maybe.nothing()
    assert empty_maybe != Maybe.just(2)

    s = Maybe.just(1)
    assert s == Maybe.just(1)
    assert s != Maybe.just(2)
    assert s != Maybe.nothing()


# Generated at 2022-06-14 03:36:39.045225
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_try import Try

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy().value == 1
    assert Maybe.nothing().to_lazy().value is None
    assert Maybe.just(1).to_lazy() == Box(1).to_lazy()
    assert Maybe.nothing().to_lazy() == Box(None).to_lazy()
    assert Maybe.just(1).to_lazy() == Try(1, is_success=True).to_lazy()

# Generated at 2022-06-14 03:36:44.183106
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    def func(x: int) -> bool:
        return x % 2 == 0

    assert Maybe.just(1).filter(func) == Maybe.nothing()
    assert Maybe.just(2).filter(func) == Maybe.just(2)
    assert Maybe.nothing().filter(func) == Maybe.nothing()


# Generated at 2022-06-14 03:36:48.605401
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:53.988158
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(6)
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:36:58.937858
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method __eq__ of class Maybe.

    :returns: None
    :rtype: None
    :raises AssertionError: when test failed
    """
    assert Maybe.just('one') == Maybe.just('one')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.just('') != Maybe.nothing()
    assert Maybe.just(None) != Maybe.just('')



# Generated at 2022-06-14 03:37:13.688082
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:37:16.422911
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:37:23.241492
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just("test")
    filtered = maybe.filter(lambda x: x == "test")
    assert filtered == Maybe.just("test")
    maybe = Maybe.just("test")
    filtered = maybe.filter(lambda x: x == "t")
    assert filtered == Maybe.nothing()
    maybe = Maybe.nothing()
    filtered = maybe.filter(lambda x: x == "test")
    assert filtered == Maybe.nothing()



# Generated at 2022-06-14 03:37:34.070407
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.test import expect

    m = Maybe.just(None)
    expect(m.filter(lambda x: x is None)).to_be(Maybe.just(None))

    m = Maybe.just(None)
    expect(m.filter(lambda x: x is not None)).to_be(Maybe.nothing())

    m = Maybe.just(1)
    expect(m.filter(lambda x: x is None)).to_be(Maybe.nothing())

    m = Maybe.just(1)
    expect(m.filter(lambda x: x is not None)).to_be(Maybe.just(1))

    m = Maybe.nothing()
    expect(m.filter(lambda x: x is None)).to_be(Maybe.nothing())

    m = Maybe.nothing()

# Generated at 2022-06-14 03:37:38.006890
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Given
    maybe1 = Maybe.just(2)
    maybe2 = Maybe.just(2)
    maybe3 = Maybe.just(3)

    # Then
    assert maybe1 == maybe2
    assert maybe1 != maybe3



# Generated at 2022-06-14 03:37:42.806505
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:37:46.139181
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:37:51.279246
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe.nothing()
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, True)



# Generated at 2022-06-14 03:37:59.874676
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result = Maybe.just(1).filter(lambda x: x > 1)
    assert result == Maybe.nothing()

    result = Maybe.just(1).filter(lambda x: x < 1)
    assert result == Maybe.nothing()

    result = Maybe.nothing()
    assert result == Maybe.nothing()

    result = Maybe.just(1).filter(lambda x: x == 1)
    assert result == Maybe.just(1)


# Generated at 2022-06-14 03:38:04.875434
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    m1 = Maybe.just(1)
    m2 = Maybe.just(1)
    m3 = Maybe.just(1)
    m4 = Maybe.just('hello')
    m5 = Maybe.nothing()
    m6 = Maybe.nothing()
    assert m1 == m2
    assert m1 == m3
    assert m2 == m3
    assert m1 != m4
    assert m1 != m5
    assert m5 == m6


# Generated at 2022-06-14 03:38:21.683179
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)
    assert Maybe.just(10).filter(lambda x: x == 5) == Maybe.nothing()
    assert Maybe.just(10).filter(lambda x: x == 10) == Maybe.just(10)
    assert Maybe.nothing().filter(lambda x: x == 10) == Maybe.nothing()



# Generated at 2022-06-14 03:38:24.256807
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)



# Generated at 2022-06-14 03:38:36.381879
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Cases:
        * Nothing == Nothing
        * Nothing != Just
        * Nothing == Just(None)
        * Just(None) == Just(None)
        * Just(None) == Just(Value)
    """
    # Nothing == Nothing
    assert Maybe.nothing() == Maybe.nothing()

    # Nothing != Just
    assert Maybe.nothing() != Maybe.just(2)

    # Nothing == Just(None)
    assert Maybe.nothing() == Maybe.just(None)

    # Just(None) == Just(None)
    assert Maybe.just(None) == Maybe.just(None)

    # Just(None) == Just(Value)
    assert Maybe.just(2) != Maybe.just(None)



# Generated at 2022-06-14 03:38:48.485631
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.validation import Validation
    from pymonet.either import Either
    from pymonet.lazy import Lazy

    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just(10) != Maybe.just(20)
    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(10) != 1
    assert Maybe.nothing() != None
    assert Maybe.just(10) != Try(10, is_success=True)
    assert Maybe.just(10) != Try(10, is_success=False)
    assert Maybe.nothing() != Try(10, is_success=True)
    assert Maybe.nothing()

# Generated at 2022-06-14 03:38:55.454650
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(None, True) == Maybe(None, True)

    assert Maybe(1, False) != Maybe(3, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, True) != Maybe(3, True)
    assert Maybe(1, True) != Maybe(1, False)


# Generated at 2022-06-14 03:39:01.590780
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Create test monads
    m1 = Maybe.just(1)
    m2 = Maybe.just(2)
    m3 = Maybe.just(1)

    # Assert they are equals
    assert m1 == m3
    assert not m1 == m2


# Generated at 2022-06-14 03:39:08.754314
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(None)
    assert Maybe.just(1) != Maybe.just('1')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.just(1) != None
    assert Maybe.just(1) != Maybe.just(1).to_box()
    assert Maybe.just(1) != Maybe.just(1).to_try()
    assert Maybe.just(1) != Maybe.just(1).to_validation()


# Generated at 2022-06-14 03:39:14.953083
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(
        lambda value: value > 0
    ) == Maybe.just(1)
    assert Maybe.just(1).filter(
        lambda value: value < 0
    ) == Maybe.nothing()
    assert Maybe.nothing().filter(
        lambda value: value > 0
    ) == Maybe.nothing()



# Generated at 2022-06-14 03:39:21.753759
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.monoid import Sum

    assert Maybe.just(Sum(1)) == Maybe.just(Sum(1))
    assert Maybe.just(Sum(1)) != Maybe.just(Sum(2))
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(Sum(1))



# Generated at 2022-06-14 03:39:25.915230
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(4).filter(lambda x: x % 2 == 0) == Maybe.just(4)
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()

# Generated at 2022-06-14 03:39:54.671403
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda a: a > 2) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda a: a < 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: a > 2) == Maybe.nothing()



# Generated at 2022-06-14 03:39:58.666606
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet import maybe

    assert maybe.just(2) == maybe.just(2)
    assert maybe.nothing() == maybe.nothing()
    assert not (maybe.just(1) == maybe.nothing())



# Generated at 2022-06-14 03:40:05.311868
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(0)
    assert maybe.value == 0
    assert maybe.is_nothing == False
    maybe = Maybe.nothing()
    assert maybe.is_nothing == True

    maybe = Maybe.just(1)
    maybe = maybe.filter(lambda x: x > 0)
    assert maybe.value == 1

    maybe = Maybe.just(1)
    maybe = maybe.filter(lambda x: x < 0)
    assert maybe.is_nothing == True

    maybe = Maybe.nothing()
    maybe = maybe.filter(lambda x: x < 0)
    assert maybe.is_nothing == True



# Generated at 2022-06-14 03:40:10.665611
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(None) != Maybe.just(1)
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:40:16.707736
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:40:22.971618
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__(): # pragma: no cover
    from copy import deepcopy

    assert Maybe.just(1) == Maybe.just(1)
    maybe_copy = deepcopy(Maybe.just(1))
    assert Maybe.just(1) == maybe_copy
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:40:28.194493
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    from pymonet.lazy import Lazy

    maybe = Maybe.just('a')
    t = Lazy(lambda: 'a')
    assert maybe.to_lazy() == t

    maybe = Maybe.nothing()
    t = Lazy(lambda: None)
    assert maybe.to_lazy() == t



# Generated at 2022-06-14 03:40:32.563239
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:40:41.176314
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    # Test when all parameters are equal
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()

    # Test when one of parameter is not equal
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)

    # Test when parameters have different types
    assert Maybe.just(1) != 1
    assert Maybe.just(1) != '1'


# Generated at 2022-06-14 03:40:43.770320
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    _maybe = Maybe(10, False)

    assert _maybe.filter(lambda x: x > 5) == Maybe(10, False)
    assert _maybe.filter(lambda x: x > 15) == Maybe(None, True)



# Generated at 2022-06-14 03:41:15.114116
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    left = Maybe.just(1).filter(lambda x: x == 1)
    right = Maybe.just(2).filter(lambda x: x == 1)
    assert left.is_nothing is False
    assert right.is_nothing is True



# Generated at 2022-06-14 03:41:22.826991
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe.just(1)
    maybe2 = Maybe.just(2)
    maybe3 = Maybe.just(1)
    maybe4 = Maybe.nothing()

    assert maybe1 == maybe3
    assert not maybe1 == maybe2
    assert not maybe1 == maybe4
    assert not maybe2 == maybe4
    assert maybe4 == maybe4


# Generated at 2022-06-14 03:41:31.025727
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_1 = Maybe.just(1)
    maybe_2 = Maybe.just(2)
    maybe_2_copy = Maybe.just(2)
    maybe_nothing = Maybe.nothing()
    maybe_nothing_copy = Maybe.nothing()
    maybe_tuple = Maybe.just((1, 2))
    maybe_list = Maybe.just([1, 2])
    maybe_dict = Maybe.just({'a': 1, 'b': 2})


assert not maybe_1 == maybe_2
assert not maybe_2 == maybe_tuple
assert not maybe_tuple == maybe_list
assert maybe_2 == maybe_2_copy
assert maybe_nothing == maybe_nothing_copy

