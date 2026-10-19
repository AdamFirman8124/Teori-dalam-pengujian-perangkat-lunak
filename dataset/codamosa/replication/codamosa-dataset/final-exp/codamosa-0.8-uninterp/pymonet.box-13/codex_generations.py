

# Generated at 2022-06-14 03:01:33.802510
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = Box(1).to_lazy()
    assert value.fold(lambda _: False, lambda _: True)
    assert value.unfold() == 1


# Generated at 2022-06-14 03:01:42.014461
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    Test for method __eq__. Test cases for two boxes with same value, two boxes with different values, two boxes with
    different types and two boxes with different types.

    :returns: whether the test is passed
    :rtype: bool
    """
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != Box("1")
    assert Box("1") != Box(2)
    assert Box("1") != Box("2")
# Test Box method __eq__



# Generated at 2022-06-14 03:01:46.587399
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(2) == Box(2)
    assert Box(1) != Box(2) and Box(2) != Box(1)
    assert Box(2) != Box(3)
    assert Box([1, 2, 3]) != Box([1, 2, 3])


# Generated at 2022-06-14 03:01:56.656363
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    # GIVEN class Box[A]
    value_1 = 1
    value_2 = 2
    box_1 = Box(value_1)
    box_2 = Box(value_2)
    assert isinstance(box_1, Box) is True
    assert isinstance(box_2, Box) is True

    # WHEN compare two boxes with the same data type and different values
    # THEN return False
    assert box_1 == box_2 is False

    # WHEN compare two boxes with the same data type and the same values
    # THEN return True
    box_1.value = value_2
    assert box_1 == box_2 is True



# Generated at 2022-06-14 03:02:00.441980
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    :returns: Unit test if function return successfull Try monad
    :rtype: Boolean
    """

    def get_value() -> int:
        return 1

    return Box(get_value).to_lazy() == Lazy(lambda: get_value())

# Generated at 2022-06-14 03:02:02.841302
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2 + 3).to_lazy().fold() == 5

# Generated at 2022-06-14 03:02:06.266827
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != Box('test')
    assert Box(1) != 1
    assert Box(1) != 'test'



# Generated at 2022-06-14 03:02:09.259531
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    # Arrange & Act
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != Box('1')


# Generated at 2022-06-14 03:02:11.092143
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5) == Box(5).to_lazy()

# Generated at 2022-06-14 03:02:14.891947
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1)
    assert Box('cat') == Box('cat')
    assert Box([1, 2, 3]) == Box([1, 2, 3])
    assert Box(1) != Box(2)
    assert Box('cat') != Box('dog')
    assert Box('cat') != 'cat'
    assert Box(1) != [1]



# Generated at 2022-06-14 03:02:17.614786
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == lazy(lambda: 42)

# Generated at 2022-06-14 03:02:22.169138
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    # Given
    from pymonet.lazy import Lazy
    from pymonet.monad import do_monad

    @do_monad(Box)
    def boxed_result() -> Box[int]:
        x = yield Box(1)
        y = yield Box(2)

        return x + y

    # Then
    assert boxed_result().to_lazy().value() == 3

# Generated at 2022-06-14 03:02:23.902801
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().get_value()() == 1

# Generated at 2022-06-14 03:02:27.308206
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert isinstance(box.to_lazy(), Lazy)



# Generated at 2022-06-14 03:02:28.885267
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == 1


# Generated at 2022-06-14 03:02:31.267914
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Box(1).to_lazy()

# Generated at 2022-06-14 03:02:34.972209
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: Box(42).value)


# Generated at 2022-06-14 03:02:42.142830
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.monad_try import Try

    result = Lazy(lambda: 'Hello')
    assert Box('Hello').to_lazy() == result

    result = Lazy(lambda: 1)
    assert Box(1).to_lazy() == result

    result = Lazy(lambda: Try('Hello', is_success=True))
    assert Box(Try('Hello', is_success=True)).to_lazy() == result


# Generated at 2022-06-14 03:02:45.786570
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(2)

    assert isinstance(box.to_lazy(), Box) and box.to_lazy().value() == 2

# Generated at 2022-06-14 03:02:52.194962
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, LazyCallable

    def test_func(val):
        return val * 2

    lazy_callable = Lazy(lambda: test_func)

    assert isinstance(lazy_callable, Lazy)
    assert isinstance(lazy_callable.value, LazyCallable)

# Generated at 2022-06-14 03:02:56.181213
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:02:59.326028
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:02.400898
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monoid import Sum

    assert Box(Sum(3)).to_lazy().fold(lambda: 0) == 3
    assert Box(Sum(3)).to_lazy().map(lambda x: x + 1).fold(lambda: 0) == 4
    assert Box(Sum(3)).to_lazy().ap(Box(lambda x: x + 1)).fold(lambda: 0) == 4


# Generated at 2022-06-14 03:03:05.311476
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().value == 3
    assert Box(3).to_lazy().fold() == 3


# Generated at 2022-06-14 03:03:13.855798
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test converting Box to Lazy

    :return: nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    box = Box(1)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy), "Lazy is not instance of Lazy"
    assert Functor.fmap(id, lazy) == 1, "Lazy is not instance of Lazy"


# Generated at 2022-06-14 03:03:15.868867
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().force() == 1
    assert Box(1).to_lazy().map(lambda x: x * 2).force() == 2


# Generated at 2022-06-14 03:03:18.966581
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import unit

    # when
    lazy = unit(1).to_lazy()

    # then
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1


# Generated at 2022-06-14 03:03:24.561707
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.acc import Acc

    assert Box('Hello').to_lazy() == Lazy(lambda: 'Hello')
    assert Box('Hello').to_lazy() == Acc('Hello', lambda x: lambda: x)

# Generated at 2022-06-14 03:03:27.067594
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Tests that Box can be transformed into lazy.
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:03:31.859700
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(['a', 'b', 'c']).to_lazy().map(lambda x: x[0] + x[1]).force() == Box('ab').value

# Generated at 2022-06-14 03:03:34.031718
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1)


# Generated at 2022-06-14 03:03:37.699384
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(10).to_lazy().value is Lazy(lambda: 10).value
    assert Box(10).to_lazy().value() == 10

# Generated at 2022-06-14 03:03:45.949064
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(3).to_lazy()  # Lazy[Function(() -> A)]
    assert isinstance(lazy, Lazy)

    lazy_value = lazy.get()  # 3
    assert isinstance(lazy_value, int) and lazy_value == 3


if __name__ == '__main__':
    try:
        import pytest
        pytest.main(['-v', __file__])
    except ImportError:
        print('Unit test not supported without pytest module')


# Generated at 2022-06-14 03:03:47.455237
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    box = Box(3)
    assert box.to_lazy().force() == 3



# Generated at 2022-06-14 03:03:49.657692
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    assert Box(2).to_lazy().value() == 2

# Generated at 2022-06-14 03:03:51.416010
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box('foo')

    assert box.to_lazy().value() == 'foo'


# Generated at 2022-06-14 03:03:58.886422
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Box(Try('foo', is_success=True)).to_lazy() == Lazy(lambda: Try('foo', is_success=True))
    assert Box(Box('foo')).to_lazy() == Lazy(lambda: Box('foo'))
    assert Box(Lazy(lambda: 'foo')).to_lazy() == Lazy(lambda: Lazy(lambda: 'foo'))
    assert type(Box(Box(Lazy(lambda: 'foo'))).to_lazy()) == Lazy


# Generated at 2022-06-14 03:04:00.546701
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(123)
    lazy = box.to_lazy()
    assert lazy.value() == 123

# Generated at 2022-06-14 03:04:02.246432
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1


# Generated at 2022-06-14 03:04:06.108442
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(Box(1).value)
    assert Box('1').to_lazy() == Lazy(Box('1').value)


# Generated at 2022-06-14 03:04:17.112550
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    class Identity(Functor):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if not isinstance(other, Identity):
                return False
            return self.value == other.value

        def map(self, f):
            return Identity(f(self.value))

    expected_lazy = Lazy(lambda: Identity(10))
    box = Box(Identity(10))

    assert box.to_lazy() == expected_lazy



# Generated at 2022-06-14 03:04:20.374513
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:23.775990
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def value() -> int:
        return 10

    box = Box(10)

    assert box.to_lazy().value() == value()

# Generated at 2022-06-14 03:04:28.075547
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Box(5).to_lazy()

    assert lazy == Lazy(lambda: 5)

# Generated at 2022-06-14 03:04:29.222412
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(lambda: 1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:04:32.144330
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(100).to_lazy(), Lazy)

# Generated at 2022-06-14 03:04:35.089716
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def function_returning_box_with_value():
        return Box(42)

    lazy = function_returning_box_with_value().to_lazy()
    assert lazy.fold() == 42

# Generated at 2022-06-14 03:04:39.200021
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def f():
        return 1

    assert Box(1).to_lazy() == Lazy(f)


# Generated at 2022-06-14 03:04:40.769798
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() is not Box(10).to_lazy()  # lazy is lazy

# Generated at 2022-06-14 03:04:44.151663
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = Box(10)
    assert value.to_lazy().force() == value.value



# Generated at 2022-06-14 03:04:51.198642
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:04:53.406453
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().is_folded() is False
    assert Box(10).to_lazy().get()() == 10



# Generated at 2022-06-14 03:04:57.033554
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()
    assert lazy == Lazy(lambda: 1)
    assert lazy.is_folded() is False


# Generated at 2022-06-14 03:05:00.818627
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test conversion Box(2) to Lazy(lambda: 2)
    """
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:05:02.978063
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(20).to_lazy() == Lazy(lambda: 20)

# Generated at 2022-06-14 03:05:05.900129
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def test_function():
        return 'test'

    box = Box[Callable]('test')
    assert box.to_lazy() == Lazy(test_function)

# Generated at 2022-06-14 03:05:07.744736
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().force() == 10
    assert Box(None).to_lazy().force() is None


# Generated at 2022-06-14 03:05:12.109934
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy
    box = Box(1)
    lazy = box.to_lazy()
    assert isinstance(lazy, pymonet.lazy.Lazy)
    assert lazy.value() == box.value



# Generated at 2022-06-14 03:05:16.240994
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from expect import expect
    from pymonet.lazy import Lazy

    box = Box('xyz')
    wrapped_lazy = box.to_lazy()
    expect(box.value).to_equal('xyz')
    expect(wrapped_lazy.value()).to_equal('xyz')



# Generated at 2022-06-14 03:05:17.371047
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1



# Generated at 2022-06-14 03:05:26.609759
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(1).to_lazy().force() == 1


# Generated at 2022-06-14 03:05:33.649317
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2).to_lazy().run() == 2
    assert Lazy(lambda: "Test").to_lazy().run() == "Test"
    assert Lazy(lambda: {'a': 2, 'b': 3}).to_lazy().run() == {'a': 2, 'b': 3}
    assert Lazy(lambda: [1, 2, "3"]).to_lazy().run() == [1, 2, "3"]



# Generated at 2022-06-14 03:05:39.625707
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from random import randint

    def get_value() -> int:
        return my_value

    my_value = randint(0, 100)
    lazy = Box(my_value).to_lazy()
    assert isinstance(lazy, Lazy)
    assert callable(lazy.value)
    assert lazy.value() == my_value



# Generated at 2022-06-14 03:05:42.470063
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = Lazy.from_result(lambda: 2)
    result = Box(value).to_lazy()
    assert result.value() == value.value()

# Generated at 2022-06-14 03:05:46.133600
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given: define Box with value 2
    box = Box(2)

    # When: tranform Box into Lazy Monad
    lazy = box.to_lazy()

    # Then: Lazy monad contains function returning previous Box value
    result = lazy.value()
    assert result == 2

# Generated at 2022-06-14 03:05:47.170721
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().value() == 42



# Generated at 2022-06-14 03:05:50.210391
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Arrange
    value = 123
    box_instance = Box(value)

    # Act
    lazy = box_instance.to_lazy()

    # Assert
    assert lazy() == value

# Generated at 2022-06-14 03:05:51.436128
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy_monad_test_function(Box(5).to_lazy())

# Generated at 2022-06-14 03:05:55.742486
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test that after calling .to_lazy() on Box returns Lazy monad.
    """
    from pymonet.lazy import Lazy

    lazy_1 = Box(1).to_lazy()
    lazy_2 = Lazy(lambda: 1)

    assert lazy_1 == lazy_2


# Generated at 2022-06-14 03:05:58.759889
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:13.824560
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'test') == Box(Lazy(lambda: 'test')).to_lazy()


# Generated at 2022-06-14 03:06:15.501209
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy() == Lazy(lambda: 3)



# Generated at 2022-06-14 03:06:19.353109
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().value() == 5
    assert Box(5).to_lazy().map(lambda x: x * 2).value() == 10

# Generated at 2022-06-14 03:06:23.280154
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    :returns: no return
    :rtype: None
    :raises AssertionError: raises assertion error if Box is not lazy
    """
    assert Box(1).to_lazy() == Box(1).value



# Generated at 2022-06-14 03:06:25.006278
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().unsafe_get() == 1

# Generated at 2022-06-14 03:06:29.350299
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy_value = Box(1).to_lazy()

    assert lazy_value.is_folded() is False
    assert lazy_value.get_value() == 1
    assert lazy_value.is_folded() is True


# Generated at 2022-06-14 03:06:32.530285
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Box(10).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_folded() is False
    assert lazy.value() == 10



# Generated at 2022-06-14 03:06:34.468044
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 'boxed_value') == Box('boxed_value').to_lazy()



# Generated at 2022-06-14 03:06:39.290693
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(4.5).to_lazy() == Lazy(lambda: 4.5)
    assert Box('string').to_lazy() == Lazy(lambda: 'string')

# Generated at 2022-06-14 03:06:43.262266
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().force() == 1
    assert Box('1').to_lazy().force() == '1'
    assert Box('1').to_lazy().map(lambda value: value * 2).force() == '11'

# Generated at 2022-06-14 03:07:10.851366
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for Box.to_lazy method.
    """

    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:07:12.515684
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:18.143342
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad import Monad

    maybe_monad = Box('true').to_lazy()
    assert maybe_monad.is_instance_of(Monad)
    assert isinstance(maybe_monad.value(), str)
    assert maybe_monad.value() == 'true'



# Generated at 2022-06-14 03:07:20.979014
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 'value'
    assert Box(value).to_lazy() == Lazy(lambda: value)



# Generated at 2022-06-14 03:07:24.641548
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy().
    """
    from pymonet.lazy import Lazy

    assert Box('a').to_lazy() == Lazy(Box('a').value)

# Generated at 2022-06-14 03:07:28.766882
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    some_box = Box(1)
    lazy_box = some_box.to_lazy()
    assert lazy_box == Lazy(lambda: 1)
    assert lazy_box.value() == 1

# Generated at 2022-06-14 03:07:36.058479
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.either import Right
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_maybe() == Maybe.just(1)
    assert Box(1).to_either() == Right(1)
    assert Box(1).to_try() == Try(1)
    assert Box(1).to_validation() == Validation.success(1)


# Unit test to check method Box.map

# Generated at 2022-06-14 03:07:38.162437
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(5)
    lazy = Box(5).to_lazy()
    assert result == lazy.fold()

# Generated at 2022-06-14 03:07:41.620250
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy_from_box = Lazy(lambda: 'hello')

    assert str(lazy_from_box) == 'Lazy...'
    assert lazy_from_box.value() == 'hello'
    assert str(lazy_from_box) == 'Lazy[value=hello]'

# Generated at 2022-06-14 03:07:47.845293
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad
    from pymonet.spec_lazy import LazySpec

    sut = Box(42).to_lazy()
    assert isinstance(sut, Lazy)
    assert isinstance(sut, Monad)
    assert isinstance(sut, LazySpec)
    assert sut.value() == 42



# Generated at 2022-06-14 03:08:45.912993
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Success

    box = Box(10)

    lazy = box.to_lazy()

    assert lazy == Lazy(lambda: 10)
    assert lazy.force() == 10
    assert lazy.force() == 10
    assert lazy.force() == 10



# Generated at 2022-06-14 03:08:50.803860
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: 5) == Box(5).to_lazy()
    assert Lazy(lambda: 'pymonet') == Box('pymonet').to_lazy()


# Generated at 2022-06-14 03:08:55.969403
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Box(Try(1)).to_lazy() == Lazy(lambda: Try(1))
    assert Box(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:08:59.912845
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    assert isinstance(Box(1).to_lazy(), Lazy)
    assert isinstance(Box(1).to_lazy(), Functor)


# Generated at 2022-06-14 03:09:02.048472
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Test for method ap of class Box

# Generated at 2022-06-14 03:09:04.891995
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import unit

    assert Box(5).to_lazy() == Lazy(unit(5))

# Generated at 2022-06-14 03:09:11.362599
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    from pymonet.lazy import Lazy

    # Test for lazy calculation
    lazy_result = Box(lambda x: x ** 2).to_lazy()
    assert isinstance(lazy_result, Lazy)
    assert lazy_result() == Box(lambda x: x ** 2).value()
    assert lazy_result(5) == 25

    # Test for returning value
    lazy_result = Box(5).to_lazy()
    assert lazy_result() == 5
    assert lazy_result(5) == 5



# Generated at 2022-06-14 03:09:19.042782
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import Forceable
    from pymonet.maybe import Maybe

    box = Box(1)
    assert isinstance(box.to_lazy(), Lazy)
    assert isinstance(box.to_lazy(), Forceable)
    assert box.to_lazy().map(lambda x: x + 1).value() == 2

# Generated at 2022-06-14 03:09:22.422336
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def function_for_lazy():
        return "lazy value"

    lazy = Box(function_for_lazy).to_lazy()
    assert lazy() == "lazy value"

# Generated at 2022-06-14 03:09:26.379616
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    f = lambda: 10
    box = Box(f)
    lazy = box.to_lazy()
    assert lazy == Lazy(f)


# Generated at 2022-06-14 03:11:21.715339
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    Lazy = Box(1).to_lazy()

    assert isinstance(Lazy, Lazy)
    assert Lazy.is_folded() is False
    assert Lazy.get() == 1



# Generated at 2022-06-14 03:11:31.437289
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().value() == 1
    assert Box(lambda: 1).to_lazy() == Lazy(lambda: 1)
    assert Box(lambda: 1).to_lazy().value() == 1
    assert Box(Try(1)).to_lazy().value() == 1
    assert Box(Try(lambda: 1)).to_lazy().value() == 1
    assert Box(Lazy(lambda: 1)).to_lazy().value() == 1