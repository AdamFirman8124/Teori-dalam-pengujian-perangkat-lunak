

# Generated at 2022-06-14 03:01:34.500278
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('py') == Box('py')
    assert not Box(True) == Box(False)


# Generated at 2022-06-14 03:01:38.486171
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('1') == Box('1')
    assert Box('test') == Box('test')
    assert Box(1) != Box('1')


# Generated at 2022-06-14 03:01:40.925759
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(2) == Box(2)
    assert Box(2) != Box(3)
    assert Box(2) != 42


# Generated at 2022-06-14 03:01:44.318624
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    Test for method __eq__ of class Box
    """
    assert Box(1) != Box(2)
    assert not(Box(1) == Box(2))
    assert Box(1) == Box(1)
    assert not(Box(1) != Box(1))



# Generated at 2022-06-14 03:01:46.162970
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()

    assert lazy
    assert lazy.get() == 1

# Generated at 2022-06-14 03:01:50.401781
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for Box.to_lazy() method.
    """
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:01:52.400685
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    x = Box(1)
    y = Box(1)
    assert x == y


# Generated at 2022-06-14 03:01:59.689598
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box('test') == Box('test')
    assert Box('test') != Box('test2')
    assert Box('test') != 1
    # noinspection PyTypeChecker
    assert Box('test') != None  # type: ignore
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 'test'
    # noinspection PyTypeChecker
    assert Box(1) != None  # type: ignore
    assert 1 != Box(1)
    assert Box(None) == Box(None)



# Generated at 2022-06-14 03:02:06.266940
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_test_fn(x):
        return lambda: x + 5

    assert Box(10).to_lazy() == Lazy(lazy_test_fn(10))
    assert Box(10).to_lazy().fold() == 15
    assert Lazy(lazy_test_fn(10)) == Lazy(lazy_test_fn(10))

# Generated at 2022-06-14 03:02:08.621968
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box_1 = Box(1)
    box_2 = Box(2)
    assert box_1 == box_1
    assert box_1 != Box(2)
    assert Box(1) == box_1


# Generated at 2022-06-14 03:02:11.757876
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(42).to_lazy()

    assert isinstance(result, Lazy)
    assert result.value() == 42


# Generated at 2022-06-14 03:02:12.839637
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('Hello world!').to_lazy().value() == 'Hello world!'

# Generated at 2022-06-14 03:02:16.798724
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box(True).to_lazy() != Lazy(lambda: False)



# Generated at 2022-06-14 03:02:19.680764
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monoid import Sum

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box(Sum(10)).to_lazy() == Lazy(lambda: Sum(10))

# Generated at 2022-06-14 03:02:20.847313
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    assert Box(2).to_lazy().run() == 2



# Generated at 2022-06-14 03:02:24.358568
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.functor import Functor
    from pymonet.lazy import Lazy
    from typing import Any

    assert isinstance(Box(1).to_lazy(), Lazy)
    assert Functor.fmap(lambda x: x + 2, Box(1).to_lazy()) == Box(3)



# Generated at 2022-06-14 03:02:28.391025
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(lambda x: x + 1).to_lazy().f()(1) == 2



# Generated at 2022-06-14 03:02:40.769706
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.function import identity, compose

    # compose(f, g, x) = f(g(x))

    lazy = Box(3).to_lazy()
    assert lazy == Lazy(lambda: 3)

    lazy = Box(3).to_lazy()
    assert lazy.map(lambda x: 2 * x).force() == 6

    lazy = Box(3).to_lazy()
    assert lazy.ap(Box(lambda x: 2 * x)).force() == 6

    assert lazy.to_maybe().is_just()
    assert lazy.to_maybe().from_just() == 3

    assert lazy.to_either().is_right()
    assert lazy.to_either().from_right() == 3

    assert lazy.to_try().is_success()

# Generated at 2022-06-14 03:02:43.913778
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:02:51.264901
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Lazy(lambda: 1)
    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: 1) != Lazy(lambda: 2)
    assert Lazy(lambda: 1) != Box(2).to_lazy()



# Generated at 2022-06-14 03:02:55.524154
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1

# Generated at 2022-06-14 03:03:00.751103
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    input = Box(Try(10))
    actual = input.to_lazy()

    expected = Lazy(lambda: Try(10))

    assert expected == actual



# Generated at 2022-06-14 03:03:13.965821
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_either import Either
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.monad_validation import Validation

    assert Maybe(1).to_lazy() == Lazy(lambda: 1)
    assert Either.left('err').to_lazy() == Lazy(lambda: 'err')
    assert Either.right(3).to_lazy() == Lazy(lambda: 3)
    assert Lazy(lambda: 2).to_lazy() == Lazy(lambda: 2)
    assert Try(True).to_lazy() == Lazy(lambda: True)

# Generated at 2022-06-14 03:03:17.636399
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box.to_lazy() method
    """

    def return_value() -> Box:
        return Box(1)

    assert return_value().to_lazy().unwrap()() == 1



# Generated at 2022-06-14 03:03:20.392212
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1
    assert Box(None).to_lazy().fold() is None
    assert Box('Hello').to_lazy().fold() == 'Hello'
    assert Box(False).to_lazy().fold() is False

# Generated at 2022-06-14 03:03:22.093734
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).to_lazy()



# Generated at 2022-06-14 03:03:25.393976
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 3) == Lazy(lambda: 3)



# Generated at 2022-06-14 03:03:27.694035
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def add_one(value):
        return value + 1
    assert Box(1).to_lazy().map(add_one).get_or_else(100) == 2



# Generated at 2022-06-14 03:03:31.952246
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()

    assert lazy.is_sufficient
    assert lazy.get_value() == 1



# Generated at 2022-06-14 03:03:36.657524
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().is_not_forced()
    assert Box(1).to_lazy().map(lambda i: i + 1).is_not_forced()
    assert Box(1).to_lazy().fold() == 1
    assert Box(1).to_lazy().map(lambda i: i + 1).fold() == 2



# Generated at 2022-06-14 03:03:40.421697
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 5
    box = Box(value)
    lazy = box.to_lazy()
    assert lazy.fold(lambda: 0)() == value

# Generated at 2022-06-14 03:03:43.199465
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    box = Box(42)
    lazy = box.to_lazy()
    assert lazy.value() == 42


# Generated at 2022-06-14 03:03:45.906457
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 1
    assert Lazy(lambda: value) == Box(value).to_lazy()



# Generated at 2022-06-14 03:03:46.754998
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().force() == 1

# Generated at 2022-06-14 03:03:48.314698
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:51.273420
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(11).to_lazy() == Lazy(lambda: 11)

# Generated at 2022-06-14 03:03:52.566620
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().value() == 10

# Generated at 2022-06-14 03:03:55.001849
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Lazy(lambda: 42) == Box(42).to_lazy()


# Generated at 2022-06-14 03:03:58.557581
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    x = 1
    box = Box(x)
    lazy = box.to_lazy()
    assert x == lazy.value()
    assert x == lazy.value()
    assert x == lazy.value()



# Generated at 2022-06-14 03:04:00.862906
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(100).to_lazy()
    assert lazy.is_folded()
    assert lazy.value == 100

# Generated at 2022-06-14 03:04:09.897311
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Arrange
    value = 'test'
    box = Box(value)

    # Act
    lazy = box.to_lazy()
    result = lazy.get()

    # Assert
    assert box == result


# Generated at 2022-06-14 03:04:11.541047
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().fold(lambda: 'nope') == 42


# Generated at 2022-06-14 03:04:13.642764
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:04:19.677970
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy
    from pymonet.functor_lazy import Lazy
    from pymonet.tools import identity

    box_lazy_func = Box(identity).to_lazy()
    assert isinstance(box_lazy_func, Lazy)
    assert pymonet.lazy.is_lazy(box_lazy_func)
    assert box_lazy_func.fold() == identity

# Generated at 2022-06-14 03:04:24.320603
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    def f():
        yield "test"

    assert Box(f).to_lazy().value() == "test"

# Generated at 2022-06-14 03:04:27.233069
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().get().get_or_else(0) == Box(5).value

# Generated at 2022-06-14 03:04:33.468670
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda x: x + 1) == 2



# Generated at 2022-06-14 03:04:35.693055
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Box('foobar').to_lazy() == Lazy(lambda: 'foobar')

# Generated at 2022-06-14 03:04:39.141857
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 'lazy'
    assert Box(value).to_lazy() == Lazy(lambda: value)



# Generated at 2022-06-14 03:04:40.023732
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert lazy(Box(1)).force() == 1

# Generated at 2022-06-14 03:04:51.688580
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_error import MonadException

    value = 1
    box = Box(value)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == value
    try:
        lazy.fold_with_exception()
        assert False
    except MonadException:
        assert True



# Generated at 2022-06-14 03:04:56.996542
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    # given
    first_box = Box(1)
    second_box = Box(lambda x: x + 1)

    # when
    boxed = first_box.to_lazy()

    # then
    assert boxed.value == 1

    # and when
    boxed = second_box.to_lazy()

    # and then
    assert boxed.value(1) == 2


# Generated at 2022-06-14 03:05:00.347071
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    lazy = Box(1).to_lazy()

    assert Box(lazy.value()) == Box(1)



# Generated at 2022-06-14 03:05:04.380050
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Make test for Box to_lazy method.

    :return: None
    :rtype: None
    """
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1
    assert lazy.is_folded() is False
    assert lazy.fold() == 1
    assert lazy.is_folded() is True


# Generated at 2022-06-14 03:05:06.766538
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Checks that mapping of Box to Lazy return the same value as Box
    """
    assert Box('test').to_lazy().value() == Box('test')

# Generated at 2022-06-14 03:05:09.180250
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).to_lazy()
    assert Box(1).to_lazy() != Box(2).to_lazy()



# Generated at 2022-06-14 03:05:15.238553
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Box(1).to_lazy()
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: 1).to_box() == Box(1).to_lazy()

# Generated at 2022-06-14 03:05:17.382292
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()

    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 03:05:18.967673
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:05:21.766335
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    box = Box(42)
    assert box.to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:05:34.487869
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:05:36.826817
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().value() == 10
    assert isinstance(Box(10).to_lazy(), Lazy)

# Generated at 2022-06-14 03:05:39.904411
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    def return_int() -> int:
        return 10
    assert Box(return_int).to_lazy() == Lazy(return_int)


# Generated at 2022-06-14 03:05:48.004463
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.validation import Validation, Failure
    from pymonet.validation import Success
    from pymonet.either import Right
    from pymonet.either import Left
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    # Test to lazy
    assert Box(5).to_lazy() == Lazy(lambda: 5)

    # Test to try
    assert Box(5).to_try() == Try(5, is_success=True)

    # Test to either
    assert Box(5).to_either() == Right(5)

    # Test to validation
    assert Box(5).to_validation() == Validation.success(5)



# Generated at 2022-06-14 03:05:52.162601
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    a = Try(5, is_success=True)

    assert isinstance(a.to_lazy(), Lazy)
    assert a.to_lazy().folded_value() == 5



# Generated at 2022-06-14 03:05:55.817682
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 12
    box = Box(value)
    lazy = box.to_lazy()
    result = lazy.value()
    assert result == value

    assert isinstance(lazy.value(), Box)
    assert lazy.value().value == box.value


# Generated at 2022-06-14 03:06:01.121615
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def function():
        return 'Hello'

    # Test to_lazy with function
    assert Box(function).to_lazy() == Box(Lazy(lambda: Box('Hello').value))
    assert Box(function).to_lazy().value() == Box('Hello').value

# Generated at 2022-06-14 03:06:03.046411
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().fold() == 3

# Generated at 2022-06-14 03:06:05.961893
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # first test
    assert Box(3).to_lazy().get_value() == 3
    # second test
    assert Box('str').to_lazy().get_value() == 'str'

# Generated at 2022-06-14 03:06:07.875841
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:06:29.125488
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:06:30.788593
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(1).to_lazy()
    assert 1 == lazy()

# Generated at 2022-06-14 03:06:35.096163
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box.
    """
    assert Box(10).to_lazy().fold() == 10


# Generated at 2022-06-14 03:06:39.559722
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def get_box_value() -> int:
        return 1

    assert Lazy(get_box_value) == Box(get_box_value).to_lazy()



# Generated at 2022-06-14 03:06:45.260213
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    a = Box(1)
    lazy = a.to_lazy()
    assert lazy.fold() == 1


# Generated at 2022-06-14 03:06:47.659013
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 42

    lazy_value = Lazy(lambda: value)
    assert Box(value).to_lazy() == lazy_value

# Generated at 2022-06-14 03:06:50.763248
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: [1, 2, 3]) == Box([1, 2, 3]).to_lazy()



# Generated at 2022-06-14 03:06:54.239695
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'foobar') == Box('foobar').to_lazy()



# Generated at 2022-06-14 03:06:57.607383
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)
    assert Box(42).to_lazy() == Lazy.wrap(42)



# Generated at 2022-06-14 03:06:59.445881
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:45.492721
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(True).to_lazy() == Lazy(True)



# Generated at 2022-06-14 03:07:46.275358
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(lambda: 5).to_lazy().get()() == 5

# Generated at 2022-06-14 03:07:47.885694
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(10)

    assert box.to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:07:50.000940
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert(Box(1).to_lazy() == Lazy(lambda: 1))


# Generated at 2022-06-14 03:07:50.602681
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:07:57.332211
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor
    from pymonet.monad import Monad

    box = Box('a').to_lazy()

    assert box == Lazy(lambda: 'a')
    assert isinstance(box, Box)
    assert isinstance(box, Lazy)
    assert isinstance(box, Functor)
    assert isinstance(box, Monad)


# Generated at 2022-06-14 03:08:05.854868
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.monad_try import Success
    from pymonet.monad_try import Failure
    from pymonet.validation import Validation
    from pymonet.validation import Success as ValidationSuccess
    from pymonet.validation import Fail as ValidationFail
    from pymonet.lazy import Lazy
    from pymonet.either import Left
    from pymonet.either import Right
    from pymonet.maybe import Nothing
    from pymonet.maybe import Just
    assert Box("test").to_lazy() == Lazy(lambda: 'test')
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:08:10.462364
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for function 'test_Box_to_lazy' of class 'Box'
    """
    box = Box('lazy')
    lazy = box.to_lazy()

    assert lazy.val() == 'lazy'



# Generated at 2022-06-14 03:08:14.559267
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:08:16.751480
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(1).to_lazy()

    assert lazy.fold() == 1


# Generated at 2022-06-14 03:10:00.435066
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().get() == 1

# Generated at 2022-06-14 03:10:07.378631
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy = Lazy(lambda: 5)
    maybe = Try.success(lazy)

    assert maybe.to_lazy() == lazy


# Generated at 2022-06-14 03:10:11.620979
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    from pymonet.validation import Validation

    box = Box(Validation('test_error', []))

    assert box.to_lazy().value() == Validation('test_error', [])

# Generated at 2022-06-14 03:10:24.649107
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    value = 10
    box = Box(value)
    value_from_lazy = box.to_lazy().force()
    assert value == value_from_lazy

# Generated at 2022-06-14 03:10:30.727406
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    import pymonet.lazy

    result = Box('foo').to_lazy()
    assert isinstance(result, pymonet.lazy.Lazy)
    assert isinstance(result.to_callable(), pymonet.lazy.Lazy)
    assert 'foo' == result.get()
    assert 'foo' == result.to_callable().get()

# Generated at 2022-06-14 03:10:43.062918
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    # Arrange
    value = 42
    box = Box(value)

    # Act
    result = box.to_lazy()

    # Assert
    assert result.value() == value



# Generated at 2022-06-14 03:10:45.178137
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('x').to_lazy() == Lazy(lambda: 'x')

# Generated at 2022-06-14 03:10:51.731063
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy on Box
    """
    # Arrange
    from pymonet.lazy import Lazy

    box_value = Box(1)

    # Act
    box_to_lazy = box_value.to_lazy()

    # Assert
    assert box_to_lazy is not None
    assert isinstance(box_to_lazy, Lazy)

    assert box_to_lazy.is_folded is False
    assert box_to_lazy.is_failed is False

    assert box_to_lazy.value == 1


# Generated at 2022-06-14 03:10:53.667327
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def f():
        return 'result'

    assert str(  # type: ignore
        Box(f).to_lazy()) == '<Lazy[function(() -> result)]>'



# Generated at 2022-06-14 03:10:55.032410
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(2)
    lazy_box = box.to_lazy()

    assert lazy_box == Lazy(lambda: 2)