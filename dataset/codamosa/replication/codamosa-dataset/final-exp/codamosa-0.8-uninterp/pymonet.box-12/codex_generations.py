

# Generated at 2022-06-14 03:01:38.100714
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Arrange
    # Act
    result = Box(1).to_lazy()

    # Assert
    assert result.value() == 1



# Generated at 2022-06-14 03:01:39.471934
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)



# Generated at 2022-06-14 03:01:40.866889
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(2) == Box(2)



# Generated at 2022-06-14 03:01:43.638587
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(2).to_lazy().value() == Lazy(lambda: 2).value()

# Generated at 2022-06-14 03:01:47.015907
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """Check return value and type of method to_lazy of class Box"""

    value = 1
    box = Box(value)
    lazy = box.to_lazy()
    assert lazy.unfold() == value
    assert type(lazy) == Box(value).to_lazy().__class__

# Generated at 2022-06-14 03:01:48.787325
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:01:52.246098
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    test_Box___eq__ function
    """

    # Box
    box1 = Box('A')

    assert box1 == box1
    assert box1 != 'A'


# Generated at 2022-06-14 03:01:55.420591
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Transform Box of integer value into Lazy.
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1), 'Transformation from Box to Lazy test failed.'

# Generated at 2022-06-14 03:02:01.453256
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    x = Box(1)
    y = Box(1)
    z = Box(2)
    a = 1

    assert x == y
    assert x != z
    assert not isinstance(a, Box) or x != a


# Generated at 2022-06-14 03:02:05.157064
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Box('a') == Box.unit('a') == Lazy('a').get()



# Generated at 2022-06-14 03:02:09.933455
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert isinstance(Box(True).to_lazy(), Lazy)

# Generated at 2022-06-14 03:02:11.772782
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('test').to_lazy().fold(lambda: 'test') == 'test'


# Generated at 2022-06-14 03:02:14.996985
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(42)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy) and lazy.fold(lambda: 0) == 42


# Generated at 2022-06-14 03:02:16.943419
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)


# Generated at 2022-06-14 03:02:20.120937
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    Unit test for method __eq__ of class Box
    """
    assert Box(5) == Box(5)
    assert Box('5') == Box('5')
    assert Box(5) != Box('5')


# Generated at 2022-06-14 03:02:26.489395
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_try import Try

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box(5).to_lazy().get() == 5
    assert Box(5).to_lazy().get_or_else(lambda: 10) == 5
    assert Box(5).to_lazy().get_or_else(lambda: Try(10, is_success=True)).get() == 5
    assert Box(5).to_lazy().get_or_else(lambda: Try(10, is_success=False)).get_or_else(lambda: Lazy(lambda: 15)) == 15



# Generated at 2022-06-14 03:02:29.618431
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    Unit test for method __eq__ of class Box.
    """
    A = Box(1)

    assert A == Box(1)

    assert not A == Box(2)



# Generated at 2022-06-14 03:02:33.260301
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 1



# Generated at 2022-06-14 03:02:35.501023
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(0) == Box(0)



# Generated at 2022-06-14 03:02:37.220025
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(2).to_lazy().value() == 2

# Generated at 2022-06-14 03:02:41.030386
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(12)
    lazy = box.to_lazy()

    assert lazy.value() == 12


# Generated at 2022-06-14 03:02:44.088266
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:02:57.026752
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    :returns: nothing
    :rtype: None
    """
    # pylint: disable=R0915
    # pylint: disable=R1705
    # pylint: disable=C0103

    # Given: Nothing

    # When: get lazy function with Box
    lazy_box = Box(2).to_lazy()

    # Then: lazy_box must be not folded
    assert lazy_box.folded is False, "Lazy box mast be not folded"

    # When: get result value from lazy_box
    value = lazy_box.value()

    # Then: value must be same as in orginal Box
    assert value == 2, "Result must be same as in orginal Box"

# Generated at 2022-06-14 03:02:58.587777
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert lazy(lambda: 5) == Box(5).to_lazy().value()



# Generated at 2022-06-14 03:03:06.208583
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    mock_callable = Mock()

    box = Box(mock_callable)
    lazy = box.to_lazy()

    mock_callable.assert_not_called()

    lazy.value()

    mock_callable.assert_called_once_with()

    assert type(lazy) == Lazy
    assert lazy.is_fold is False



# Generated at 2022-06-14 03:03:08.771739
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 1) == Box(1).to_lazy()


# Generated at 2022-06-14 03:03:11.142745
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()
    assert lazy.value == 1



# Generated at 2022-06-14 03:03:15.167230
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(1).bind(Lazy(lambda x: x * 3).fold) == 3
    assert Box(2).bind(Lazy(lambda x: x * 3).fold) == 6

# Generated at 2022-06-14 03:03:17.754760
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()
    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 03:03:20.720689
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    """
    assert Box(1).to_lazy().fold() == 1



# Generated at 2022-06-14 03:03:25.737495
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('string').to_lazy() == Lazy(lambda: 'string')



# Generated at 2022-06-14 03:03:34.889591
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box('some data').to_lazy() == Lazy(lambda: 'some data')
    assert Box(1).to_lazy().value() == 1
    assert Box('some data').to_lazy().value() == 'some data'


# Generated at 2022-06-14 03:03:37.771245
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 123) == Box(123).to_lazy()

# Functional tests for class Box

# Generated at 2022-06-14 03:03:40.943675
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    evaluate_test_case(
        Box(42).to_lazy(),
        Lazy(lambda: 42),
        "Test case #01"
    )



# Generated at 2022-06-14 03:03:43.297861
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:45.625690
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:48.870413
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    # given
    box = Box(1)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:50.236292
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().force() == 3


# Generated at 2022-06-14 03:03:53.072227
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    tests for Box.to_lazy() method
    """
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:03:55.666201
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    box = Box(1)
    lazy = box.to_lazy()

    assert lazy.fold() == 1



# Generated at 2022-06-14 03:04:02.200932
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    assert Box(2).to_lazy()() == 2

# Generated at 2022-06-14 03:04:04.935795
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(8).to_lazy() == Lazy(lambda: 8)

# Generated at 2022-06-14 03:04:09.016864
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 1


# Generated at 2022-06-14 03:04:10.631550
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 100) == Box(100).to_lazy()

# Generated at 2022-06-14 03:04:13.219966
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # Arrange
    box = Box('value')

    # Act
    lazy = box.to_lazy()

    # Assert
    assert lazy == Lazy(lambda: 'value')

# Generated at 2022-06-14 03:04:16.139722
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of class Box.
    """

    assert Box(5).to_lazy() == Box(5).to_lazy()



# Generated at 2022-06-14 03:04:22.727035
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, fold

    def test_function():
        return 42

    lazy_box = Box(test_function).to_lazy()

    assert lazy_box == Lazy(test_function)
    assert lazy_box.is_folded() is False
    assert lazy_box.value() == 42
    assert fold(lazy_box) == 42
    assert lazy_box.is_folded() is True


# Generated at 2022-06-14 03:04:25.579243
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:04:30.112569
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Execute unit tests for method to_lazy of class Box
    """

    from pymonet.lazy import Lazy, fold

    box = Box(5)

    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert fold(lazy) == 5

# Generated at 2022-06-14 03:04:34.746465
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def add(x):
        return x + 1

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    def sub(x, y):
        return x - y

    def get_value(x):
        return x.value

    assert get_value(Box(2).to_lazy().bind(add).bind(mul, Box(5).to_lazy()).bind(div, Box(4).to_lazy()).bind(sub, Box(3).to_lazy())) == (1 + 2) * 5 / 4 - 3

# Generated at 2022-06-14 03:04:44.647503
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(10)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold(lambda: -1) == 10

# Generated at 2022-06-14 03:04:47.601369
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:51.451314
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box('foo').to_lazy() == Lazy(lambda: 'foo')

# Generated at 2022-06-14 03:04:54.395606
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('1').to_lazy() == Lazy(lambda: '1')



# Generated at 2022-06-14 03:05:00.040537
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    lazy_box = Box('lazy Box').to_lazy()

    assert isinstance(lazy_box, Lazy)
    assert isinstance(lazy_box.value(), Box)
    assert lazy_box.value().value == 'lazy Box'


# Generated at 2022-06-14 03:05:03.028144
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box
    """
    result = Box(100).to_lazy()

    assert result.value() == 100

# Generated at 2022-06-14 03:05:05.148092
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:05:09.126336
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def test_func():
        return 'test value'

    lazy = Box(test_func).to_lazy()

    assert isinstance(lazy, Lazy)
    assert not lazy.is_folded
    assert lazy.value() == 'test value'

# Generated at 2022-06-14 03:05:13.618075
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    :return: None
    :rtype: None
    """
    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:05:15.344535
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().map(lambda x: x + 3).get() == 4


# Generated at 2022-06-14 03:05:22.006352
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()
    assert lazy == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:26.137258
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for to_lazy method.
    """
    returned = Box(1).to_lazy()
    assert isinstance(returned, Box)
    assert returned.value() == 1


# Generated at 2022-06-14 03:05:31.008846
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box('hello').to_lazy() == Lazy(lambda: 'hello')
    assert Box('hello' + 'world').to_lazy() == Lazy(lambda: 'helloworld')



# Generated at 2022-06-14 03:05:33.361227
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda : 10) == Box(10).to_lazy()


# Generated at 2022-06-14 03:05:36.434693
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.test_utils import assert_equals
    from pymonet.monad_lazy import Lazy

    assert_equals(Lazy(lambda: 2), Box(2).to_lazy())

# Generated at 2022-06-14 03:05:39.952177
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    box = Box(4)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy.is_forced() is False
    assert lazy.value() == box.value



# Generated at 2022-06-14 03:05:42.047264
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:05:44.800569
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    value = 5
    box = Box(value)

    # When
    lazy = box.to_lazy()

    # Then
    assert lazy.value() == value


# Generated at 2022-06-14 03:05:49.877308
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe

    # Test for successfull try
    assert Box(Try(10)).to_lazy() == Lazy(10), 'Result of monad to_lazy should be equal expected lazy'
    assert Box(Try(10, False)).to_lazy() == Lazy(lambda: Try(10, False)), 'Result of monad to_lazy should be equal expected lazy'

    # Test for not nullary function
    assert Box(Lazy(10)).to_lazy() == Lazy(10), 'Result of monad to_lazy should be equal expected lazy'

# Generated at 2022-06-14 03:05:52.126861
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert_equal(Lazy(lambda: 1), Box(1).to_lazy())
    assert_equal(Lazy(lambda: None), Box(None).to_lazy())

# Generated at 2022-06-14 03:06:03.422766
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(True)
    assert box.to_lazy().force() is True


# Generated at 2022-06-14 03:06:06.817417
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(4).to_lazy() == Lazy(lambda: 4)


# Generated at 2022-06-14 03:06:09.526534
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(2)
    assert box.to_lazy().get() == 2



# Generated at 2022-06-14 03:06:12.267620
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box("value").to_lazy() == Lazy(lambda: "value")



# Generated at 2022-06-14 03:06:14.854878
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(123).to_lazy() == Lazy(lambda: 123)

# Generated at 2022-06-14 03:06:25.632677
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    test_value = 1
    test_box = Box(test_value)

    res_lazy = test_box.to_lazy()
    res_try = test_box.to_try()

    assert res_lazy.is_instance_of(Lazy)
    assert res_try.is_instance_of(Try)
    assert res_lazy.is_success()
    assert res_try.is_success()
    assert test_value == res_lazy.eval()
    assert test_value == res_try.get_value()


# Generated at 2022-06-14 03:06:28.589734
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:06:30.112592
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:06:35.591157
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.maybe import Maybe

    assert Box(2).to_lazy() == Lazy(lambda: 2)
    assert Box(None).to_lazy() == Lazy(lambda: None)
    assert Box([]).to_lazy() == Lazy(lambda: [])
    assert Box(tuple()).to_lazy() == Lazy(lambda: tuple())
    assert Box(set()).to_lazy() == Lazy(lambda: set())
    assert Box(dict()).to_lazy() == Lazy(lambda: dict())
    assert Box(frozenset()).to_lazy() == Lazy(lambda: frozenset())

# Generated at 2022-06-14 03:06:37.627337
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(9).to_lazy() == Lazy(lambda: 9)

# Generated at 2022-06-14 03:06:57.385787
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(13).to_lazy().value() == 13

# Generated at 2022-06-14 03:06:58.829834
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:07:00.409498
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('foo').to_lazy().fold() == 'foo'

# Generated at 2022-06-14 03:07:02.133378
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:12.559878
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    box1 = Box(1)
    box2 = Box(2)
    box3 = Box(3)
    box4 = Box(4)
    box5 = Box(5)
    assert box1.to_lazy() == box2.to_lazy() == box3.to_lazy() == box4.to_lazy() == box5.to_lazy()
    assert box1.to_lazy().fold() == box2.to_lazy().fold() == box3.to_lazy().fold() == box4.to_lazy().fold() == box5.to_lazy().fold()

# Generated at 2022-06-14 03:07:16.626699
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    some_value = 'some_value'
    box = Box(some_value)
    lazy = box.to_lazy()
    assert lazy.value() == some_value



# Generated at 2022-06-14 03:07:28.774301
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    # Checking that to_lazy of Box equal to apply lazy function to Identity constructor
    # ----------------------------------------------------------
    unit = Box(10)
    assert unit.to_lazy() == unit.to_lazy().value()
    assert unit.to_lazy() == unit.to_lazy().value().to_lazy()
    assert unit.to_lazy() == unit.to_lazy().value().to_lazy().value()
    assert unit.to_lazy() == unit.to_lazy().value().to_lazy().value().to_lazy()
    assert unit.to_lazy() == unit.to_lazy().value().to_lazy().value().to_lazy().value()

    # Checking

# Generated at 2022-06-14 03:07:34.961484
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Box((1, 2, 3)).to_lazy() == Lazy(lambda: (1, 2, 3))
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])

# Generated at 2022-06-14 03:07:37.152288
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(10).to_lazy()
    assert lazy.unfold() == 10

# Generated at 2022-06-14 03:07:38.294494
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:08:22.528879
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    expected_value = 10
    box = Box(expected_value)
    lazy = box.to_lazy()

    assert lazy.eval() == expected_value

# Generated at 2022-06-14 03:08:25.681687
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(12).to_lazy() == Lazy(lambda: 12)



# Generated at 2022-06-14 03:08:29.304840
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:08:31.390718
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert lazy_value() == 1  # pylint: disable=unnecessary-lambda



# Generated at 2022-06-14 03:08:33.792736
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('value').to_lazy() == Box('value').to_lazy().map(lambda x: x())


# Generated at 2022-06-14 03:08:40.390048
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.

    :return: nothing
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(Try(10)).to_lazy() == Lazy(lambda: Try(10))
    assert Box(Lazy(lambda: 10)).to_lazy() == Lazy(lambda: Lazy(lambda: 10))
    assert Box(Lazy(lambda: Try(10))).to_lazy() == Lazy(lambda: Lazy(lambda: Try(10)))


# Generated at 2022-06-14 03:08:42.021002
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy_value = Box(1).to_lazy()
    assert 1 == lazy_value.unwrap()

# Generated at 2022-06-14 03:08:44.622033
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(0).to_lazy() == Lazy(lambda: 0)



# Generated at 2022-06-14 03:08:47.051267
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:08:49.360910
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:10:17.471764
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:10:20.491411
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:10:23.740534
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:10:29.194958
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # GIVEN value and Box instance
    value = 'value'
    box = Box(value)

    # WHEN transform to Lazy
    lazy = box.to_lazy()

    # THEN result should be not empty Lazy with returning value function
    assert lazy.value() == value

# Generated at 2022-06-14 03:10:33.884170
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def f():
        print('Hello')
        return 'World'

    box = Box(f)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.fn(), str)


# Generated at 2022-06-14 03:10:35.242452
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().value() == 5


# Generated at 2022-06-14 03:10:37.610167
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:10:43.469113
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box to Lazy conversion
    """

    lazy_box = Box(5).to_lazy()
    assert lazy_box.is_folded is False
    assert lazy_box.value() == 5



# Generated at 2022-06-14 03:10:48.837436
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_test_helpers import lazy_spec_test

    lazy_spec_test(Box(5), Lazy(lambda: 5), lambda x: x == 5)



# Generated at 2022-06-14 03:10:52.133182
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.test_utils import eq
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def value_supplier():
        return 10

    expected = Lazy(value_supplier)

    actual = Box(10).to_lazy()

    eq(actual.get(), expected.get())