

# Generated at 2022-06-14 03:31:35.803346
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(item: int) -> bool:
        return item % 2 == 0

    result = Maybe.just(1).filter(filterer)
    assert result is Maybe.nothing()
    result = Maybe.just(2).filter(filterer)
    assert result is Maybe.just(2)
    result = Maybe.nothing().filter(filterer)
    assert result is Maybe.nothing()



# Generated at 2022-06-14 03:31:37.713158
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def is_even(num):
        return num % 2 == 0

    assert Maybe.just(2).filter(is_even).get_or_else(None) == 2
    assert Maybe.just(3).filter(is_even).get_or_else(None) == None



# Generated at 2022-06-14 03:31:41.753576
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('test') == Maybe.just('test')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(5) != Maybe.just(3)


# Generated at 2022-06-14 03:31:49.252844
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Arrange
    # @formatter:off
    maybe1 = Maybe.just(2)
    maybe2 = Maybe.just(2)
    maybe3 = Maybe.just(3)
    maybe4 = Maybe.nothing()
    # @formatter:on

    # Act, Assert
    assert maybe1 == maybe2
    assert maybe2 == maybe1
    assert maybe1 != maybe3
    assert maybe1 != maybe4
    assert maybe2 != maybe3
    assert maybe2 != maybe4
    assert maybe3 != maybe4



# Generated at 2022-06-14 03:31:55.168666
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:32:06.065839
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Maybe[Bool] == Maybe[Bool]
    maybe_a = Maybe(True, is_nothing=False)
    maybe_b = Maybe(True, is_nothing=False)
    assert maybe_a.__eq__(maybe_b)

    maybe_a = Maybe(True, is_nothing=False)
    maybe_b = Maybe(False, is_nothing=False)
    assert not maybe_a.__eq__(maybe_b)

    # Maybe[None] == Maybe[None]
    maybe_a = Maybe(None, is_nothing=True)
    maybe_b = Maybe(None, is_nothing=True)
    assert maybe_a.__eq__(maybe_b)

    # Maybe[Bool] != Maybe[None]
    maybe_a = Maybe(True, is_nothing=False)
    maybe

# Generated at 2022-06-14 03:32:10.596053
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:32:12.601033
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:32:17.813299
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert not (Maybe([1, 2]) == Maybe.just(1))
    assert NotImplemented == Maybe.just(1).__eq__(1)
    assert Maybe([1, 2]) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:22.823267
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:29.394093
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    :return: Success of the unit test
    :rtype: Boolean
    """
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    return True



# Generated at 2022-06-14 03:32:37.976182
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)
    assert Maybe.nothing().filter(lambda x: x == 5) == Maybe.nothing()

    assert Maybe.nothing().filter(lambda x: x == 5).value is None
    assert Maybe.nothing().filter(lambda x: x == 5).is_nothing is True

    assert Maybe.just(5).filter(lambda x: x == 5).value == 5
    assert Maybe.just(5).filter(lambda x: x == 5).is_nothing is False


# Generated at 2022-06-14 03:32:45.227514
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: x is None) == Maybe.nothing()
    assert Maybe.just(None).filter(lambda x: x is None) == Maybe.nothing()
    assert Maybe.just(None).filter(lambda x: x is not None) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x is None) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x is not None) == Maybe.just(1)


# Generated at 2022-06-14 03:32:49.828045
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == (Lazy(lambda: 1))
    assert Maybe.nothing().to_lazy() == (Lazy(lambda: None))


# Generated at 2022-06-14 03:33:00.014140
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_test_helpers import string_length_gt_n_def, string_length_gt_n
    from pymonet.monad_test_helpers import string_length_gt_five_def, string_length_gt_five
    from pymonet.monad_test_helpers import string_length_gt_ten_def, string_length_gt_ten

    assert Maybe.just('').filter(string_length_gt_five_def) == Maybe.nothing()
    assert Maybe.just('').filter(string_length_gt_five) == Maybe.nothing()
    assert Maybe.just('hi').filter(string_length_gt_ten_def) == Maybe.nothing()
    assert Maybe.just('hi').filter(string_length_gt_ten) == Maybe.nothing()
    assert Maybe

# Generated at 2022-06-14 03:33:10.535378
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(4)
    assert maybe.filter(lambda v: v % 2 == 0) == Maybe.just(4)
    assert maybe.filter(lambda v: v % 2 == 1) == Maybe.nothing()

    assert Maybe.just(4).filter(lambda v: v % 2 == 0).get_or_else(1) == 4
    assert Maybe.just(5).filter(lambda v: v % 2 == 0).get_or_else(1) == 1

    assert Maybe.nothing().filter(lambda v: v % 2 == 0).get_or_else(1) == 1
    assert Maybe.nothing().filter(lambda v: v % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:33:15.490521
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()



# Generated at 2022-06-14 03:33:18.856395
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(2, False).to_lazy() == Lazy(lambda: 2)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:33:23.152717
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()

    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 1) == Maybe.nothing()

# Generated at 2022-06-14 03:33:28.490266
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.either import Left

    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda _: False) == Maybe.nothing()
    assert Maybe \
        .just(0) \
        .filter(lambda x: x == 0) == Maybe.just(0)
    assert Maybe \
        .just(1) \
        .filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe \
        .just(1) \
        .filter(lambda x: x == 1) == Maybe.just(1).filter(lambda x: False)


# Generated at 2022-06-14 03:33:39.532238
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Try

    maybe = Maybe.just(None)
    assert maybe.filter(lambda x: x <= 5) == Try(None, is_success=False)

    maybe = Maybe.just(10)
    assert maybe.filter(lambda x: x <= 5) == Try(None, is_success=False)

    maybe = Maybe.just(3)
    assert maybe.filter(lambda x: x <= 5) == Try(3, is_success=True)

    maybe = Maybe.nothing()
    assert maybe.filter(lambda x: x <= 5) == Try(None, is_success=False)


# Generated at 2022-06-14 03:33:44.469110
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()
test_Maybe_filter()


# Generated at 2022-06-14 03:33:48.013362
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:56.777437
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor
    import pymonet.functor as FP
    from pymonet.either import Either
    from pymonet.monad_list import MonadList
    from pymonet.monad_try import Try
    from pymonet.monad_tuple import MonadTuple
    from pymonet.monad_set import MonadSet
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def test_map(functor: Functor):
        assert functor.map(lambda x: x ** 2) == Functor(
            [i ** 2 for i in functor.list])


# Generated at 2022-06-14 03:34:05.118852
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    empty_maybe: Maybe[int] = Maybe.nothing()
    filled_maybe_odd_value: Maybe[int] = Maybe.just(5)
    filled_maybe_even_value: Maybe[int] = Maybe.just(6)

    empty_maybe = empty_maybe.filter(lambda x: x%2)
    assert empty_maybe == Maybe.nothing()

    filled_maybe_odd_value = filled_maybe_odd_value.filter(lambda x: x%2)
    assert filled_maybe_odd_value == Maybe.just(5)

    filled_maybe_even_value = filled_maybe_even_value.filter(lambda x: x%2)
    assert filled_maybe_even_value == Maybe.nothing()

# Generated at 2022-06-14 03:34:09.658650
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:34:15.152534
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    lazy_just = Maybe(2, False).to_lazy()
    lazy_nothing = Maybe.nothing().to_lazy()
    assert lazy_just.value() == 2, "Test for Maybe.to_lazy()"
    assert lazy_nothing.value() is None, "Test for Maybe.to_lazy()"


# Generated at 2022-06-14 03:34:15.765142
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    pass

# Generated at 2022-06-14 03:34:19.656182
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test for Maybe.filter

    Examples:
    >>> from pymonet.functor import Maybe
    >>> from pymonet.functor import test_Maybe_filter
    >>> test_Maybe_filter()
    True
    """
    m = Maybe.just(1)
    n = Maybe.nothing()

    assert m.filter(lambda x: x == 1) == Maybe.just(1)
    assert m.filter(lambda x: x == 2) == Maybe.nothing()
    assert n.filter(lambda x: x == 1) == Maybe.nothing()
    return True


# Generated at 2022-06-14 03:34:23.615307
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.either import Left

    m = Maybe.just(Left(1))
    m2 = m.filter(lambda x: x.is_nothing())

    assert m2 == Maybe.nothing()

# Generated at 2022-06-14 03:34:30.851512
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value > 0

    assert Maybe.just(1).filter(filterer) == Maybe.just(1)
    assert Maybe.just(0).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()

# Generated at 2022-06-14 03:34:34.077255
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().value() == 1
    assert Maybe.nothing().to_lazy().value() == None



# Generated at 2022-06-14 03:34:42.693173
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    a = Maybe.just(1)
    b = Maybe.just(2)
    c = Maybe.nothing()

    def is_greater_than_zero(x: int) -> bool:
        """
        Returns True for greater than zero, in other case False.

        :param x: value to check
        :type x: int
        :returns: True when value is greater than zero, in other case False
        :rtype: boolean
        """
        return x > 0

    assert a.filter(is_greater_than_zero) == a
    assert b.filter(is_greater_than_zero) == b
    assert c.filter(is_greater_than_zero) == c

# Generated at 2022-06-14 03:34:47.377732
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:34:49.611338
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just("test").filter(lambda x: x != "test") == Maybe.nothing()
    assert Maybe.just("test").filter(lambda x: x == "test") == Maybe.just("test")
    assert Maybe.nothing().filter(lambda x: x == "test") == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x != "test") == Maybe.nothing()


# Generated at 2022-06-14 03:34:54.274189
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(str) == Maybe.nothing()
    assert Maybe.just(1).filter(str) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()


# Generated at 2022-06-14 03:35:00.626165
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x : True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x : False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x : True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x : False) == Maybe.nothing()


# Generated at 2022-06-14 03:35:04.936088
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # Arrange
    val = 23
    data = Maybe.just(val)

    # Action
    result = data.to_lazy()

    # Assert
    assert isinstance(result, Lazy)
    assert result.get() == val


# Generated at 2022-06-14 03:35:10.356674
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe.

    :returns: None
    :rtype: None
    """
    a = Maybe.just(1)
    b = Maybe.just(2)
    c = Maybe.just(3)
    d = Maybe.just(4)

    assert a.filter(lambda x: x > 2) == Maybe.nothing()
    assert b.filter(lambda x: x > 2) == Maybe.nothing()
    assert c.filter(lambda x: x > 2) == Maybe.just(3)
    assert d.filter(lambda x: x > 2) == Maybe.just(4)

# Generated at 2022-06-14 03:35:15.728887
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(x):
        return x % 2 == 0

    assert Maybe.just(2).filter(filterer) == Maybe.just(2)
    assert Maybe.just(3).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()

# Generated at 2022-06-14 03:35:25.101154
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet import Maybe

    def filterer(value):
        return value % 2 == 0

    maybe_1 = Maybe.just(12)
    assert maybe_1.filter(filterer).value == 12

    maybe_2 = Maybe.just(9)
    assert maybe_2.filter(filterer).is_nothing



# Generated at 2022-06-14 03:35:29.940428
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:35:34.659457
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    test_value = 1

    assert Maybe.just(test_value).filter(lambda x: x - 1 < 0) == Maybe.nothing()
    assert Maybe.just(test_value).filter(lambda x: x - 1 == 0) == Maybe.just(test_value)
    assert Maybe.nothing().filter(lambda x: x - 1 <= 0) == Maybe.nothing()



# Generated at 2022-06-14 03:35:38.668098
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # Test when Maybe is not empty
    maybe = Maybe.just(3)
    assert maybe.to_lazy().force() == 3

    # Test when Maybe is empty
    maybe = Maybe.nothing()
    assert maybe.to_lazy().force() is None

# Generated at 2022-06-14 03:35:44.437494
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe(2, False).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe(1, True).filter(lambda x: x == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:35:48.594801
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(3).filter(lambda x: True) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: False) == Maybe.nothing()


# Generated at 2022-06-14 03:35:56.845697
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Maybe.just('100').filter(lambda x: x != '100') == Maybe.nothing()
    assert Maybe.just('100').filter(lambda x: x == '100') == Maybe.just('100')
    assert Maybe.just(100).filter(lambda x: x != 100) == Maybe.nothing()
    assert Maybe.just(100).filter(lambda x: x == 100) == Maybe.just(100)

    assert Maybe.just([1, 2, 3, 4]).filter(lambda x: all(i < 10 for i in x)) == Maybe.just([1, 2, 3, 4])

# Generated at 2022-06-14 03:36:00.712777
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # given
    maybe = Maybe.just(42)
    # then
    assert maybe.filter(lambda x: x == 42) == Maybe.just(42)
    assert maybe.filter(lambda x: x != 42) == Maybe.nothing()


# Generated at 2022-06-14 03:36:11.593674
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Tests filter method of Maybe.

    :returns: None
    """
    print("[INFO] Tests filter method of Maybe:")
    def filterer(value):
        return value % 2 == 0
    maybe1 = Maybe.just(1)
    maybe2 = Maybe.just(2)
    maybe3 = Maybe.nothing()
    print("[INFO] Should return nothing:")
    print("[INFO] 1 / 2")
    print("[INFO] ", maybe1.filter(filterer) == Maybe.nothing())
    print("[INFO] 1 / 2")
    print("[INFO] ", maybe3.filter(filterer) == Maybe.nothing())
    print("[INFO] Should return itself when condition is true:")
    print("[INFO] 1 / 1")

# Generated at 2022-06-14 03:36:15.779704
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)


# Generated at 2022-06-14 03:36:30.464312
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Maybe.just(1).to_lazy() == Lazy(lambda: Maybe.just(1))
    assert Maybe.nothing().to_lazy() == Lazy(lambda: Maybe.nothing())

# Generated at 2022-06-14 03:36:39.937277
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Even number
    def is_even(value: int) -> bool:
        return not value % 2

    # Odd number
    def is_odd(value: int) -> bool:
        return value % 2

    # Empty Maybe
    assert Maybe.just(None).filter(is_even).get_or_else(0) == 0
    assert Maybe.just(None).filter(is_odd).get_or_else(0) == 0

    # Not empty Maybe
    assert Maybe.just(-2).filter(is_even).get_or_else(0) == -2
    assert Maybe.just(-1).filter(is_odd).get_or_else(0) == -1


# Generated at 2022-06-14 03:36:44.688983
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:36:51.438473
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from random import randint
    from pymonet.lazy import Lazy

    def rnd():
        return randint(1, 10)

    m1 = Maybe.just(rnd())
    m2 = Maybe.nothing()
    assert m1.to_lazy() == Lazy(lambda: m1.value)
    assert m2.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:36:55.543301
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x > 5) == Maybe.just(10)
    assert Maybe.just(5).filter(lambda x: x > 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 5) == Maybe.nothing()


# Generated at 2022-06-14 03:37:01.026287
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()

# Generated at 2022-06-14 03:37:07.729100
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    from pymonet.test.test_lazy import test_Lazy_apply

    test_cases = [
        (Maybe.just(4), Lazy(lambda: 4)),
        (Maybe.nothing(), Lazy(lambda: None))
    ]

    for d, expected in test_cases:
        assert d.to_lazy() == expected
        test_Lazy_apply(d.to_lazy())


# Generated at 2022-06-14 03:37:10.645642
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0).value == 1
    assert Maybe.just(1).filter(lambda x: x < 0).is_nothing



# Generated at 2022-06-14 03:37:15.509193
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    import pytest
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    # Given
    def test_fun():
        return 5

    maybe = Maybe.just(test_fun)
    # When
    lazy_value = maybe.to_lazy()
    # Then
    assert lazy_value.value() == test_fun()


# Generated at 2022-06-14 03:37:20.982526
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x % 2 == 0) == Maybe.just(10)
    assert Maybe.just(5).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()

# Generated at 2022-06-14 03:37:48.926842
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.monad_lazy import MonadLazy

    my_functor = Functor()
    my_monad = Monad()
    my_monad_lazy = MonadLazy()
    x = my_monad_lazy.pure(lambda: 4)
    y = my_monad_lazy.pure(lambda: 5)
    z = my_functor.map(
        my_monad.bind(
            x,
            lambda x: my_monad.bind(
                y,
                lambda y: (x + y)
            )
        ),
        lambda x: x()
    )

# Generated at 2022-06-14 03:37:50.650079
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    x = Maybe(0, False)
    assert isinstance(x.to_lazy(), Lazy)

# Generated at 2022-06-14 03:37:55.138379
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    num = Maybe.just(45)
    assert num.filter(lambda x: x % 2 == 1) == Maybe.just(45)
    assert num.filter(lambda x: x % 2 == 0) == Maybe.nothing()

# Generated at 2022-06-14 03:38:01.973361
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test method filter of class Maybe.

    :returns: None
    :rtype: None
    """
    assert Maybe.just(2).filter(lambda x: x == 2) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x != 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()

# Generated at 2022-06-14 03:38:04.242364
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x <= 2) == Maybe.just(2)


# Generated at 2022-06-14 03:38:07.672542
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_maybe import Maybe

    def return_five():
        return 5

    assert Maybe.just(return_five).to_lazy().force()() == 5


# Generated at 2022-06-14 03:38:12.574562
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:38:17.385458
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:38:23.410073
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda _: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda _: False) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda _: True) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x > 4) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x > 5) == Maybe.nothing()

# Generated at 2022-06-14 03:38:28.773567
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    :returns: None
    """
    is_even = lambda i: i % 2 == 0
    assert Maybe.just(2).filter(is_even) == Maybe.just(2)
    assert Maybe.just(3).filter(is_even) == Maybe.nothing()


# Generated at 2022-06-14 03:39:09.455868
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:13.865371
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def test_function(x):
        print('Function is called')
        return 'Some'

    m = Maybe(test_function, False)
    lazy_result = m.to_lazy()

    assert lazy_result.value() == 'Some'

# Generated at 2022-06-14 03:39:20.916627
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value == 2

    assert Maybe.just(2).filter(filterer) == Maybe.just(2)
    assert Maybe.just(1).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:39:30.237588
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit tests for method filter of class Maybe

    :return: None
    """
    # filter for None and None
    assert Maybe(None, True).filter(lambda x: x is None) == Maybe.nothing() == Maybe(None, True)

    # filter for None and not None
    assert Maybe(None, True).filter(lambda x: x is not None) == Maybe.nothing() == Maybe(None, True)

    # filter for not None and not None
    assert Maybe('not none', False).filter(lambda x: x.startswith('not')) == Maybe.just('not none')

    # filter for not None and None
    assert Maybe('not none', False).filter(lambda x: x.startswith('wrong')) == Maybe.nothing()

# Generated at 2022-06-14 03:39:34.888205
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just('foo')
    assert maybe.to_lazy() == Lazy(lambda: 'foo')

    maybe = Maybe.nothing()
    assert maybe.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:39:40.418543
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x >= 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x >= 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x >= 1) == Maybe.nothing()


# Generated at 2022-06-14 03:39:45.951313
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    @add_type_info
    def double_positive(x: int) -> bool:
        return x > 0

    assert Maybe.just(5).filter(double_positive) == Maybe.just(5)
    assert Maybe.just(-5).filter(double_positive) == Maybe.nothing()
    assert Maybe.nothing().filter(double_positive) == Maybe.nothing()



# Generated at 2022-06-14 03:39:51.035414
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 0) == Maybe.just(5)
    assert Maybe.just(-1).filter(lambda x: x > 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:39:54.222353
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    _ = Maybe(4, False)
    assert _.to_lazy().evaluate() == 4
    _ = Maybe(None, True)
    assert _.to_lazy().evaluate() is None

# Generated at 2022-06-14 03:39:59.629472
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 0) == Maybe.nothing()


# Generated at 2022-06-14 03:41:16.168857
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # Given
    maybe = Maybe.just(3)

    # When
    value = maybe.to_lazy()

    # Then
    assert callable(value.value)
    assert value.value() == 3

# Generated at 2022-06-14 03:41:25.441468
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test method filter of class Maybe.
    """
    assert Maybe(50, False).filter(lambda x: x < 60) == Maybe(50, False)
    assert Maybe(50, False).filter(lambda x: x > 60) == Maybe.nothing()
    assert Maybe(50, False).filter(lambda x: x == 50) == Maybe(50, False)
    assert Maybe.nothing().filter(lambda x: x < 60) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 60) == Maybe.nothing()


# Generated at 2022-06-14 03:41:27.365886
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()

