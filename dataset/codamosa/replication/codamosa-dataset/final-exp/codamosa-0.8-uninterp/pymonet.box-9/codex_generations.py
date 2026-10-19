

# Generated at 2022-06-14 03:01:32.769063
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(lambda: 1)
    assert box.to_lazy().value() == 1

# Generated at 2022-06-14 03:01:34.550208
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(3).to_lazy() == Lazy(lambda: 3)
    assert Box('test').to_lazy() == Lazy(lambda: 'test')



# Generated at 2022-06-14 03:01:37.711781
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:01:39.785269
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:01:50.528215
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    b = Box('foo')
    assert b.to_lazy() == Lazy(lambda: 'foo')
    assert b.to_lazy().__repr__() == 'Lazy[Function((), -> \'foo\')]'
    assert b.to_lazy().__str__() == 'Lazy[Function((), -> \'foo\')]'
    # Ensure that memoization works.
    assert b.to_lazy() is b.to_lazy()



# Generated at 2022-06-14 03:01:54.663846
# Unit test for method to_lazy of class Box

# Generated at 2022-06-14 03:01:55.814255
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(2) == Box(2)



# Generated at 2022-06-14 03:01:59.295781
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)

    assert Box(1) != Box(2)



# Generated at 2022-06-14 03:02:01.233204
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().force() == 42


# Generated at 2022-06-14 03:02:03.183012
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(lambda: 1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:02:08.556098
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:02:11.050153
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Failure

    assert Box(123).to_lazy() == 123
    assert Box(Failure(123)).to_lazy() == Box(Failure(123))



# Generated at 2022-06-14 03:02:15.912905
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    Unit test for method __eq__ of class Box
    """

    # Create few boxes with different values and compare
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(None) == Box(None)
    assert Box(None) != Box(1)
    assert Box(lambda x: x) == Box(lambda x: x)
    assert Box(lambda x: x) != Box(lambda y: y)
    assert Box(object()) == Box(object())
    assert Box(object()) != Box(1)



# Generated at 2022-06-14 03:02:17.057617
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box1 = Box(1)
    box2 = Box(1)
    assert box1.__eq__(box2) == True


# Generated at 2022-06-14 03:02:19.604469
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(2) != Box(3)
    assert Box(4) != Box(4.1)



# Generated at 2022-06-14 03:02:21.646953
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(5) == Box(5)
    assert not Box(5) == Box(7)


# Unit tests for method __str__ of class Box

# Generated at 2022-06-14 03:02:23.650242
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().map(lambda x: x + 3).value() == 6

# Generated at 2022-06-14 03:02:26.863292
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert not (Box(1) == Box('1'))



# Generated at 2022-06-14 03:02:28.927046
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 3) == Box(3).to_lazy()



# Generated at 2022-06-14 03:02:30.260607
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1

# Generated at 2022-06-14 03:02:34.606304
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().value() == 10



# Generated at 2022-06-14 03:02:36.080588
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:02:39.347804
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def assert_lazy(lazy):
        assert lazy == Box(5).to_lazy()
        assert lazy.fold() == 5

    assert_lazy(Box(5).to_lazy())



# Generated at 2022-06-14 03:02:42.450623
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    assert box.to_lazy().fold() == 1



# Generated at 2022-06-14 03:02:56.589763
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.applicative import Applicative
    from pymonet.lazy import Lazy

    # Given
    monad_try = Try(None, is_success=False)

    # When
    lazy_monad_try = monad_try.to_lazy()

    # Then
    assert isinstance(lazy_monad_try, Applicative)
    assert isinstance(lazy_monad_try, Monad)
    assert isinstance(lazy_monad_try, Functor)
    assert isinstance(lazy_monad_try, Lazy)
    assert not lazy_monad_try.is_value_

# Generated at 2022-06-14 03:03:01.840608
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box("abc").to_lazy() == Lazy(lambda: "abc")


# Generated at 2022-06-14 03:03:14.405215
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import Lazy
    from pymonet.lazy import fold

    # Test case 1 - should return lazy
    b = Box(10)
    lazy = b.to_lazy()
    result = fold(lazy)
    assert isinstance(lazy, Lazy)
    assert result == 10

    # Test case 2 - should return lazy
    b = Box(10.5)
    lazy = b.to_lazy()
    result = fold(lazy)
    assert isinstance(lazy, Lazy)
    assert result == 10.5

    # Test case 3 - should return lazy
    b = Box(None)
    lazy = b.to_lazy()
    result = fold(lazy)
    assert isinstance(lazy, Lazy)
    assert result is None

    # Test case 4 - should

# Generated at 2022-06-14 03:03:18.344331
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    box = Box(3)
    lazy = box.to_lazy()
    assert lazy.force() == 3
    assert isinstance(lazy, Lazy)


# Generated at 2022-06-14 03:03:19.933128
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:03:22.408096
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    :returns: nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    box_value = 'value'

    lazy = Box(box_value).to_lazy()

    assert lazy.value() == Lazy(lambda: box_value).value()


# Generated at 2022-06-14 03:03:30.070290
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(12).to_lazy() == Lazy(lambda: 12)
    assert Box(Try.fail('Err')).to_lazy() == Lazy(lambda: Try.fail('Err'))
    assert Box(0.0).to_lazy().to_try().value == 0.0
    try:
        Box(Try.fail('Err')).to_lazy().to_try().value
        assert False
    except RuntimeError:
        assert True



# Generated at 2022-06-14 03:03:33.567952
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Arrange
    from pymonet.lazy import Lazy

    # Act
    lazy = Box('value').to_lazy()

    # Assert
    assert lazy == Lazy(lambda: 'value')



# Generated at 2022-06-14 03:03:36.085931
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    box = Box(10)
    lazy = box.to_lazy()

    assert lazy == Lazy(lambda: 10)


# Generated at 2022-06-14 03:03:37.260379
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().fold() == 10


# Generated at 2022-06-14 03:03:43.008567
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    lazy_monad = Box(lambda x: x + 4).to_lazy()

    assert isinstance(lazy_monad, Lazy)
    assert lazy_monad.fold(lambda: 1) == 5
    assert lazy_monad.fold(x=4) == 8


# Generated at 2022-06-14 03:03:47.029603
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 'test value'
    lazy = Box(value).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == value


# Generated at 2022-06-14 03:03:49.417079
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for ``to_lazy`` method of class ``Box``.
    """
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:03:50.536060
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 03:03:53.745074
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box("test")
    assert isinstance(box.to_lazy(), Lazy)
    assert "test" == box.to_lazy().value()



# Generated at 2022-06-14 03:03:56.063114
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box class.
    """

    box = Box(20)
    lazy = box.to_lazy()

    assert lazy.unpack() == 20


# Generated at 2022-06-14 03:04:04.936505
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    value = Box(Lazy(lambda: 42)).to_lazy().value
    assert value == 42
    value = Box(Try(42)).to_lazy().value
    assert value == 42

# Generated at 2022-06-14 03:04:06.300605
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:04:09.645583
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Box(10).to_lazy()
    assert Box(10).to_lazy().fold() == 10

# Generated at 2022-06-14 03:04:11.661056
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5) == Box(5)

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:04:13.866149
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().foldr() == 5

# Generated at 2022-06-14 03:04:15.883493
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def some_function():
        return 1

    assert Box(some_function).to_lazy() == Lazy(some_function)



# Generated at 2022-06-14 03:04:18.384313
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    val = Box(10)
    assert val.to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:04:22.319219
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Tests for Box
    """
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:04:24.480332
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().force() == 2



# Generated at 2022-06-14 03:04:28.827843
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    x = lambda: 1
    y = Box(x).to_lazy()
    assert callable(y.value)
    assert y.value() == 1


# Generated at 2022-06-14 03:04:42.285270
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def assert_that_lazy_has_value(lazy: Lazy[T], value: T):
        pass
    assert_that_lazy_has_value(Box(10).to_lazy(), 10)


# Generated at 2022-06-14 03:04:48.757150
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    value = 'test'
    box = Box(value)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == value



# Generated at 2022-06-14 03:04:50.801726
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(123).to_lazy().value() == 123


# Generated at 2022-06-14 03:04:52.404231
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 1).value() == Box(1).to_lazy().value()

# Generated at 2022-06-14 03:05:02.552363
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box class.

    :return: None
    """
    from pymonet.monad_lazy import Lazy

    # Test for empty string
    assert Box('').to_lazy() == Lazy(f=lambda: '')

    # Test for non empty string
    assert Box('test').to_lazy() == Lazy(f=lambda: 'test')

    # Test for zero
    assert Box(0).to_lazy() == Lazy(f=lambda: 0)

    # Test for non zero integer
    assert Box(123).to_lazy() == Lazy(f=lambda: 123)

    # Test for empty list
    assert Box([]).to_lazy() == Lazy(f=lambda: [])

    # Test for non empty list

# Generated at 2022-06-14 03:05:05.900235
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(10).to_lazy()
    assert isinstance(lazy, Lazy), 'Should be lazy'
    assert lazy.value() == 10, 'Should be equal 10'


# Generated at 2022-06-14 03:05:07.594649
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try

    def t():
        raise Exception()

    b = Try(t(), is_success=False).to_lazy()

    assert b.is_folded() is False



# Generated at 2022-06-14 03:05:09.200131
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: Box(10).value)

# Generated at 2022-06-14 03:05:13.365194
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:15.456530
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:05:24.953770
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(10).to_lazy().get_value() == 10

# Generated at 2022-06-14 03:05:27.457891
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(5).to_lazy().eval() == 5
    assert Box("Hello").to_lazy().eval() == "Hello"


# Generated at 2022-06-14 03:05:29.410767
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def func():
        return 'hello'

    assert Box('hello').to_lazy() == Lazy(func)

# Generated at 2022-06-14 03:05:31.791705
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)

    assert box.to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:36.334948
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: Try(2, True)) == Lazy(lambda: Try(1, True)).chain(lambda x: Lazy(lambda: Try(x + 1, True)))



# Generated at 2022-06-14 03:05:39.320574
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(42)
    lazy = Lazy(lambda: 42)
    assert box.to_lazy() == lazy



# Generated at 2022-06-14 03:05:41.366561
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box
    """
    assert Box('test').to_lazy().eval() == 'test'

# Generated at 2022-06-14 03:05:43.026076
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(100).to_lazy() == Lazy(lambda: 100)


# Generated at 2022-06-14 03:05:47.543030
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box("a").to_lazy() == Lazy(lambda: "a")
    assert Box(Try("a")).to_lazy() == Lazy(lambda: Try("a"))
    assert Box(Lazy(lambda: "a")).to_lazy() == Lazy(lambda: "a")



# Generated at 2022-06-14 03:05:49.861013
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:06:10.262996
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 10
    box = Box(10)
    assert value == box.to_lazy().fold()

# Generated at 2022-06-14 03:06:13.379588
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:06:15.116856
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:06:18.914951
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:06:25.194558
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Tests Box to Lazy
    """

    from pymonet.lazy import Lazy

    value = 5
    lazy = Box(value).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == value

# Generated at 2022-06-14 03:06:30.008915
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    result = Box(5).to_lazy()
    assert result == Box(5).to_lazy()
    assert isinstance(result, Lazy)
    assert result.get() == 5


# Generated at 2022-06-14 03:06:32.616410
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Setup
    box = Box(1)

    # Exercise
    try_lazy = box.to_lazy()

    # Verification
    assert callable(try_lazy.value) and try_lazy.value() == 1

# Generated at 2022-06-14 03:06:34.091308
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(42)
    assert Lazy(lambda: 42) == box.to_lazy()


# Generated at 2022-06-14 03:06:36.286330
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:48.085278
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_lazy import Lazy, MapFunc

    """
    >>> x = Box(2)
    >>> x
    Box[value=2]
    >>> x.to_lazy()
    Lazy[value=<function Box.to_lazy.<locals>.<lambda> at 0x7f7a042d4158>]
    >>> x.to_lazy().fold()
    2
    >>> x.to_lazy().map(lambda x: x * 2).fold()
    4
    >>> x.to_lazy().map(lambda x: x * 2).map(lambda x: x * 3).fold()
    12
    >>> x.to_lazy().map(lambda x: x * 2).apply(Lazy(lambda: 3)).fold()
    6
    """

# Generated at 2022-06-14 03:07:11.890500
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """Unit test for method to_lazy of class Box."""
    box_value = Box(45)
    box_lazy = box_value.to_lazy()

    assert box_lazy.value() == box_value.value

# Generated at 2022-06-14 03:07:13.838377
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box('value')
    assert box.to_lazy().value() == 'value'


# Generated at 2022-06-14 03:07:18.332345
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.list import List
    from pymonet.lazy import Lazy

    def foo():
        return 12

    assert List.of(Lazy(foo)) == Box(foo).to_lazy().to_list()


# Generated at 2022-06-14 03:07:24.200577
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).to_lazy()
    assert Box(1).to_lazy().eval() == 1
    assert Box(1).to_lazy().map(lambda x: x + 1).eval() == 2
    assert repr(Box(1).to_lazy()) == repr(Lazy(lambda: 1))


# Generated at 2022-06-14 03:07:28.010774
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def sum(x, y):
        return x + y

    assert (
        Box(sum)
        .to_lazy()
        .fold(lambda: -1)(1, 2)
    ) == 3

# Generated at 2022-06-14 03:07:30.809773
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(True).to_lazy().get() is True
    assert Box(1).to_lazy().get() == 1
    assert Box('Hello').to_lazy().get() == 'Hello'

# Generated at 2022-06-14 03:07:32.082000
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:42.751781
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monoid import Monoid, Endo, compose
    from pymonet.lazy import Lazy

    Box(4).to_lazy() == Lazy(lambda: 4)
    Box('abc').to_lazy() == Lazy(lambda: 'abc')
    Box(Endo(lambda x: x + 3)).to_lazy() == Lazy(lambda: Endo(lambda x: x + 3))
    Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    Box(dict(a=1)).to_lazy() == Lazy(lambda: dict(a=1))
    Box(None).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:07:45.833129
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:47.348904
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:08:32.759053
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:08:36.792629
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    lazy = Box('value1').to_lazy()
    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.function(), str)
    assert lazy.function() == 'value1'

# Generated at 2022-06-14 03:08:39.658141
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 2

    result = Box(func).to_lazy()
    assert isinstance(result, Lazy)
    assert not result.is_folded
    assert 2 == result.fold()



# Generated at 2022-06-14 03:08:50.619098
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor
    from pymonet.monad import Monad

    assert Functor[Lazy].fmap(Box("1").to_lazy(), lambda x: x + "0") == Lazy(lambda: "10")
    assert Monad[Lazy].mapply(Box("1").to_lazy(), Lazy(lambda: lambda x: x + "0")) == Lazy(lambda: "10")
    assert Monad[Lazy].mapply(Lazy(lambda: lambda x: x + "0"), Box("1").to_lazy()) == Lazy(lambda: "10")

# Generated at 2022-06-14 03:08:52.160235
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().f() == 2

# Generated at 2022-06-14 03:08:53.885025
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(100).to_lazy().get() == 100


# Generated at 2022-06-14 03:08:57.480139
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 1



# Generated at 2022-06-14 03:08:59.705437
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:09:04.853418
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_lazy import LazyResult

    lazy = Box(5).to_lazy()

    assert lazy == Lazy(lambda: 5)

    assert lazy.value == LazyResult(5)



# Generated at 2022-06-14 03:09:08.107846
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    x = Box('text')
    assert isinstance(x.to_lazy(), Lazy), "result is not Lazy"
    assert x.to_lazy().value() == 'text', "result is incorrect"



# Generated at 2022-06-14 03:10:43.701408
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """Test function to_lazy of Box class."""
    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:10:50.827213
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = Lazy(lambda: 2)
    assert box.to_lazy() != lazy
    assert box.to_lazy().eval() == 1
    assert lazy != Lazy(lambda: 2)
    assert lazy.eval() == 2
    assert box.to_lazy().map(lambda x: x * 2).eval() == 2
    assert lazy.map(lambda x: x * 2).eval() == 4



# Generated at 2022-06-14 03:10:52.555139
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(1).to_lazy(), Lazy)
    assert Box(3).to_lazy().fold(lambda: 10) == 3


# Generated at 2022-06-14 03:10:56.739745
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(5).to_lazy()
    assert box == Lazy(lambda: 5)



# Generated at 2022-06-14 03:11:00.403291
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:11:04.001566
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert (Box(1).to_lazy() == Lazy(lambda: 1))

# Generated at 2022-06-14 03:11:13.424221
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Success
    from pymonet.either import Left, Right
    from pymonet.maybe import Nothing, Maybe

    assert Box(2).to_lazy() == Lazy(lambda: 2)
    assert Box(2).to_maybe() == Maybe(2, is_ok=True)
    assert Box(2).to_try() == Try(2, is_success=True)
    assert Box(2).to_validation() == Success(2)
    assert Box(2).to_either() == Right(2)

# Generated at 2022-06-14 03:11:17.776553
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(True).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: True)

# Generated at 2022-06-14 03:11:25.257904
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    box = Box(1)

    assert isinstance(box.to_lazy(), Lazy), 'Box cannot convert to Lazy'
    assert box.to_lazy().fold(identity) == 1, 'Lazy has incorrect value'


# Generated at 2022-06-14 03:11:35.333856
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5) == Box(5).to_lazy()

