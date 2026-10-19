

# Generated at 2022-06-14 03:01:38.294580
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box1 = Box(1)
    box2 = Box(1)
    box3 = Box(2)

    assert box1 == box2
    assert box1 != box3



# Generated at 2022-06-14 03:01:40.724832
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)
    
    

# Generated at 2022-06-14 03:01:43.764273
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()  # type: Lazy[int]

    assert 1 == lazy.value

# Generated at 2022-06-14 03:01:45.586401
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert not (Box(1) == Box(2))
    assert not (Box(1) == 3)


# Generated at 2022-06-14 03:01:46.641293
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box = Box(3)
    assert box == box



# Generated at 2022-06-14 03:01:49.494328
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 'test-value').equals(Box('test-value').to_lazy())



# Generated at 2022-06-14 03:01:52.126057
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Lazy.unit(5) == Box(5).to_lazy()

# Generated at 2022-06-14 03:01:54.396305
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    result = Box(1) == Box(1)
    assert result



# Generated at 2022-06-14 03:01:56.988543
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    value = 'value'
    box = Box(value)
    # when
    lazy = box.to_lazy()
    # then
    assert isinstance(lazy, Box)
    assert lazy.value == value

# Generated at 2022-06-14 03:02:00.010429
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value()() == 1
    assert Box(1).to_lazy().value()().value == 1
    assert Box(1).to_lazy().fold() == 1

# Generated at 2022-06-14 03:02:06.178927
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert str(Box(1).to_lazy()) == 'Lazy[<function Box.to_lazy.<locals>.<lambda> at 0x1040eaa60>]'



# Generated at 2022-06-14 03:02:09.485965
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box.to_lazy().

    >>> Box('a').to_lazy()
    <Lazy [λ]>
    >>> Box('a').to_lazy().value()
    'a'
    """
    pass



# Generated at 2022-06-14 03:02:13.672546
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Create some value x with type int = 1, and create Box from this value x,
    then transform Box into Lazy, and then call function to find value in Lazy
    and check that Lazy contains value x.

    :return: None
    :rtype: None
    """
    x = 1
    assert Lazy(lambda: x).value() == Box(x).to_lazy().value()

# Generated at 2022-06-14 03:02:18.772689
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad

    value = 1
    box = Box(value)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert isinstance(lazy, Monad)
    assert lazy.value() == value


# Generated at 2022-06-14 03:02:22.486288
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    box = Box(100)
    assert box.to_lazy().get() == 100

# Generated at 2022-06-14 03:02:26.050058
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    try:
        from pymonet.lazy import Lazy

        assert Box(1).to_lazy() == Lazy(lambda: 1)
        assert False
    except ImportError:
        pass

# Generated at 2022-06-14 03:02:32.136799
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().run() == 1
    assert Box('test').to_lazy().run() == 'test'
    assert Box(1.1).to_lazy().run() == 1.1
    assert Box(True).to_lazy().run() is True
    assert Box(None).to_lazy().run() is None


# Generated at 2022-06-14 03:02:43.127793
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Box(None).to_lazy() == Box(None).to_maybe().to_lazy()
    assert Box(None).to_lazy() == Box(None).to_either().to_lazy()
    assert Box(None).to_lazy() == Box(None).to_try().to_lazy()
    assert Box(None).to_lazy() == Box(None).to_validation().to_lazy()
    assert Box(None).to_lazy().bind(lambda _: Try(is_success=True)).bind(lambda t: t.to_validation()) == \
           Box(None).to_validation()


# Generated at 2022-06-14 03:02:51.728992
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import LazyFoldable

    box = Box(1)
    lazy_box = box.to_lazy()

    assert isinstance(lazy_box, LazyFoldable)
    assert isinstance(lazy_box, Lazy)

    assert lazy_box.is_folded() is False
    assert lazy_box.fold() == box.value

# Generated at 2022-06-14 03:02:56.427022
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    some_box = Box(2)
    lazy_value = some_box.to_lazy()
    assert isinstance(lazy_value, Lazy)
    assert lazy_value.value == some_box.value



# Generated at 2022-06-14 03:03:00.084894
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 1)
    box_lazy_value = Box(1).to_lazy()

    assert lazy_value.equals(box_lazy_value)

# Generated at 2022-06-14 03:03:09.697559
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    def add(x):
        return x + 1

    def mul(x):
        return x * 3

    def to_string(x):
        return 'value ' + str(x)

    b = Box(100).to_lazy().bind(Lazy.lift(add)).bind(Lazy.lift(mul)).bind(Lazy.lift(to_string))
    Functor.test_functor(b)
    assert b.unbox(full=False) == 'value 303'

# Generated at 2022-06-14 03:03:13.334662
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    :type value: int
    :type lazy: Lazy[int]
    """

    value = 5
    lazy = Box(value).to_lazy()
    assert value == lazy.fold()

# Generated at 2022-06-14 03:03:17.320778
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(lambda x: x ** 2)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold()(2) == 4


# Generated at 2022-06-14 03:03:19.420872
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = "abcd"

    def assert_equals(lazy_value):
        assert value == lazy_value

    assert_equals(Box(value).to_lazy().fold())

# Generated at 2022-06-14 03:03:21.440610
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy()



# Generated at 2022-06-14 03:03:22.332530
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:03:25.439073
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda : 42)

# Generated at 2022-06-14 03:03:29.783145
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box1 = Box(10)
    box2 = Box(None)

    lazy1 = box1.to_lazy()
    lazy2 = box2.to_lazy()

    assert isinstance(lazy1, Lazy)
    assert lazy1.get() == 10
    assert lazy1.get() == 10

    assert isinstance(lazy2, Lazy)
    assert lazy2.get() is None
    assert lazy2.get() is None

# Generated at 2022-06-14 03:03:32.480172
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(lambda a, b: a + b)
    lazy = box.to_lazy()
    assert lazy.force()(2, 3) == 5

# Generated at 2022-06-14 03:03:37.540333
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(0).to_lazy().get_value() == 0
    assert Box(1).to_lazy().get_value() == 1
    assert Box(100).to_lazy().get_value() == 100



# Generated at 2022-06-14 03:03:40.355561
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    box = Box(2)
    assert 2 == box.to_lazy().value()



# Generated at 2022-06-14 03:03:45.365835
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    box: Box[int] = Box(2)

    # When
    lazy = box.to_lazy()

    # Then
    assert isinstance(lazy, Box)
    assert 2 == lazy.value()


# Generated at 2022-06-14 03:03:46.566721
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:03:48.148249
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:52.236794
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy
    assert Lazy(lambda: True) == Box(True).to_lazy()
    assert Lazy(lambda: "String") == Box("String").to_lazy()


# Generated at 2022-06-14 03:03:55.885114
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test method to_lazy of class Box with 0 - should be return Lazy(function)
    """
    # Arrange
    box = Box(0)

    # Act
    actual = box.to_lazy()

    # Assert
    assert actual == Lazy(lambda: 0)

# Generated at 2022-06-14 03:03:58.557691
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert isinstance(Box(5).to_lazy(), Box)
    assert Box(5).to_lazy().value() == 5
    assert Box(5).to_lazy().value() == 5



# Generated at 2022-06-14 03:03:59.776209
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1

# Generated at 2022-06-14 03:04:03.373670
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import unit

    assert unit(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:04:09.992934
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:04:11.931810
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:15.901397
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    @Lazy
    def identity(x):
        return x

    assert Box(identity(4)).to_lazy() == Lazy(identity(4))

# Generated at 2022-06-14 03:04:18.277488
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Lazy(lambda: 'one') == Box('one').to_lazy()


# Generated at 2022-06-14 03:04:21.130010
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    assert box.to_lazy().value == 1

    box = Box(1)
    assert box.to_lazy() is not None



# Generated at 2022-06-14 03:04:23.274025
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().get() == 1



# Generated at 2022-06-14 03:04:25.495556
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(1)



# Generated at 2022-06-14 03:04:29.161232
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:33.312975
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    box = Box(5)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy.fold() == 5

# Generated at 2022-06-14 03:04:35.439737
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:04:41.839419
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    empty_box: Box[int] = Box(1)
    # when
    actual = empty_box.to_lazy()
    # then
    assert actual.value() == 1

# Generated at 2022-06-14 03:04:54.551594
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    from pymonet.monad_try import Try

    assert Try.unit(Box(2).to_lazy()) == Try.unit(Box(lambda: 2))
    assert Try.unit(Box([]).to_lazy()) == Try.unit(Box(lambda: []))
    assert Try.unit(Box({}).to_lazy()) == Try.unit(Box(lambda: {}))
    with pytest.raises(Exception):
        assert Try.unit(Box(None).to_lazy()) == Try.unit(Box(lambda: None))

# Generated at 2022-06-14 03:04:56.071038
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('str_value').to_lazy() == Lazy(lambda: 'str_value')

# Generated at 2022-06-14 03:04:58.255144
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monoid import SumMonoid

    assert type(Box(1).to_lazy()) == Lazy
    assert Box(1).to_lazy().value().fold(SumMonoid()) == 1


# Generated at 2022-06-14 03:05:03.073802
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # GIVEN
    box = Box(1)

    # WHEN
    lazy = box.to_lazy()

    # THEN
    assert lazy.value() == 1

    # WHEN
    lazy = box.to_lazy().to_lazy()

    # THEN
    assert lazy.value() == 1

# Generated at 2022-06-14 03:05:04.447583
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert isinstance(Box(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:05:15.763326
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(3).to_lazy() == Box(3).to_lazy()
    assert Box(3).to_lazy().to_lazy() == Box(3).to_lazy().to_lazy()
    assert Box(3).to_lazy().to_lazy() == Box(3).to_lazy()
    assert Box(3).to_lazy().to_lazy().value() == Box(3).to_lazy().to_lazy().value()
    assert Box(3).to_lazy().value() == Box(3).to_lazy().value()
    assert Box(3).to_lazy().value() == Box(3).value
    assert Box(3).value == Box(3).value
    assert Box(3).value() == Box(3).value()

# Generated at 2022-06-14 03:05:16.947157
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(10).to_lazy().value
    assert result == 10


# Generated at 2022-06-14 03:05:18.862983
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy()(()) == Box(1).to_lazy().foldr(()) == Box(1).to_lazy().unwrap() == 1



# Generated at 2022-06-14 03:05:21.063260
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('1').to_lazy().fold(lambda: None) == '1'


# Generated at 2022-06-14 03:05:34.672245
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Test that given function is invoked with data from Box monad.
    """
    from pymonet.lazy import Lazy

    value = 'some value'
    test_function = lambda x: x

    lazy = Box(value).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold(test_function) == value



# Generated at 2022-06-14 03:05:36.581105
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(4).to_lazy().fmap(lambda x: x + 2).unfold() == 6



# Generated at 2022-06-14 03:05:40.775976
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    # given
    lazy = Box('value').to_lazy()

    # when
    result = lazy.fold(lambda value: value)

    # then
    assert isinstance(lazy, Lazy)
    assert result == 'value'

# Generated at 2022-06-14 03:05:41.873628
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:05:44.017860
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    class A:
        pass

    box = Box(A())
    lazy = box.to_lazy()

    assert callable(lazy.value)
    assert lazy.value() == A()
    assert lazy.fold() == A()

# Generated at 2022-06-14 03:05:52.889608
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy_five = Box(5).to_lazy()

    assert isinstance(lazy_five, Lazy)

    assert lazy_five.value is not None
    assert lazy_five.value() == 5
    assert lazy_five.is_folded() is False

    lazy_exception = Box(5) \
        .map(lambda x: x / 0) \
        .to_try() \
        .to_lazy()

    assert isinstance(lazy_exception, Lazy)
    assert lazy_exception.value is not None
    assert isinstance(lazy_exception.value(), Try)
    assert isinstance(lazy_exception.value().exception, ZeroDivisionError)
    assert lazy

# Generated at 2022-06-14 03:05:56.483711
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(2).to_lazy()
    # check if result is really Lazy
    assert isinstance(lazy, type(Box(1).to_lazy()))
    # check if inner function of Lazy return same value as Box contains
    assert lazy.value() == 2

# Generated at 2022-06-14 03:05:59.549216
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:06:01.695358
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:06:05.920207
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().fold(lambda: 2) == 2
    assert Box(2).to_lazy().fold(lambda: 2) == Box(2).value
    assert Box('check').to_lazy().fold(lambda: 2) == 'check'


# Generated at 2022-06-14 03:06:24.562747
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:06:30.848642
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test converting Box with 'a' value to Lazy monad with function returning 'a'.

    :returns: None
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.asserts import assert_that

    assert_that(Box('a').to_lazy(), equal_to(Lazy(lambda: 'a')))

# Generated at 2022-06-14 03:06:34.180388
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('value').to_lazy() == 'value'



# Generated at 2022-06-14 03:06:35.545050
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('123').to_lazy() == Lazy(lambda: '123')

# Generated at 2022-06-14 03:06:43.514430
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Box(5).to_lazy()
    assert Box(5).to_lazy().map(lambda x: x + 1) == Box(6).to_lazy()
    assert Box(5).to_lazy().map(lambda x: x + 1).get_value() == 6
    assert Box(5).to_lazy().map(lambda x: x + 1).to_box() == Box(6)


# Generated at 2022-06-14 03:06:48.003098
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 5).fold() == Box(5).to_lazy().fold()
    assert Try(6, is_success=True).fold() == Box(6).to_try().fold()

# Generated at 2022-06-14 03:06:50.546120
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:06:53.661914
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:06:56.978580
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test: Check for correct transforming Box into Lazy monad
    """

    assert Box('value').to_lazy() == Lazy(lambda: 'value')

# Generated at 2022-06-14 03:07:01.668365
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # GIVEN function returning value 2
    f = lambda: 2

    # AND Box with value 1
    box = Box(1)

    # WHEN function is mapped to Box
    lazy = box.to_lazy()

    # THEN mapped value is Lazy with function returning 2
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 2

# Generated at 2022-06-14 03:07:38.948355
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert isinstance(Box(1).to_lazy(), Lazy)

# Generated at 2022-06-14 03:07:41.167556
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(42)
    assert box.to_lazy() == Lazy(lambda: 42)
    assert box.to_lazy().force() == 42

# Generated at 2022-06-14 03:07:46.720220
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    :returns: Nothing
    :rtype: None
    """
    # Test string value
    box_str = Box('Test')
    lazy_str = box_str.to_lazy()
    assert lazy_str.value() == 'Test'

    # Test integer value
    box_int = Box(42)
    lazy_int = box_int.to_lazy()
    assert lazy_int.value() == 42

    # Test list value
    box_list = Box([1, 2, 3])
    lazy_list = box_list.to_lazy()
    assert lazy_list.value() == [1, 2, 3]

    # Test tuple value
    box_tuple = Box((1, 2, 3))
    lazy_tuple = box

# Generated at 2022-06-14 03:07:57.288504
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy_box = Box(5).to_lazy()
    assert isinstance(lazy_box, Lazy)
    assert lazy_box.value == 5
    # assert lazy_box.get_value() == 5
    assert lazy_box.get_value() == 5

    try_box = Box("value").to_try()
    lazy_try_box = try_box.to_lazy()
    assert isinstance(lazy_try_box, Lazy)
    assert isinstance(lazy_try_box.get_value(), Try)
    assert lazy_try_box.get_value().is_success
    assert lazy_try_box.get_value().value == "value"

# Generated at 2022-06-14 03:08:01.684051
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy_box = Box(42).to_lazy()

    assert isinstance(lazy_box, Lazy)
    assert lazy_box.value() == 42


# Generated at 2022-06-14 03:08:07.774944
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    is_lazy = Box('test').to_lazy()
    assert type(is_lazy) is Lazy
    assert callable(is_lazy.value)
    assert is_lazy.value() == 'test'

# Generated at 2022-06-14 03:08:11.682326
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:08:16.755234
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    assert Box(3).to_lazy().fold() == 3, 'Wrong result of to_lazy method of Box class'



# Generated at 2022-06-14 03:08:18.783473
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:08:22.398619
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:09:43.940843
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Lazy(lambda: Box(1).value)

# Generated at 2022-06-14 03:09:46.075394
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('test').to_lazy().fold() == Box('test')

# Generated at 2022-06-14 03:09:47.342824
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('abc').to_lazy().value() == 'abc'

# Generated at 2022-06-14 03:09:50.865481
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: Lazy(lambda: 1))
    assert Box(Lazy(lambda: 2)).to_lazy() != Lazy(lambda: Lazy(lambda: 1))



# Generated at 2022-06-14 03:09:52.655501
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 5
    lazy_value = Lazy(lambda: value)
    assert Box(value).to_lazy() == lazy_value

# Generated at 2022-06-14 03:09:54.147699
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    b = Box(100)
    l = b.to_lazy()
    assert l.is_folded() is False and l.get() == b.value



# Generated at 2022-06-14 03:10:04.481639
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 1
    box = Box(value)
    lazy = box.to_lazy()
    assert lazy.unfold() == value

# Generated at 2022-06-14 03:10:09.903484
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 4) == Box(4).to_lazy()
    assert Lazy(lambda: 'pymonet') == Box('pymonet').to_lazy()


# Generated at 2022-06-14 03:10:13.409557
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Setup
    value = 15
    a = Box(value)
    expected_result = value

    # Exercise
    actual_result = lambda: a.to_lazy().force()

    # Verify
    assert actual_result() == expected_result

# Generated at 2022-06-14 03:10:15.904985
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box('text').to_lazy() == Lazy(lambda: 'text')
