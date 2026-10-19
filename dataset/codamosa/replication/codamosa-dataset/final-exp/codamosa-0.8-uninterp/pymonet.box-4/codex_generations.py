

# Generated at 2022-06-14 03:01:30.848157
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert (Box(1) == Box(1)) is True
    assert (Box(1) == 1) is False

# Generated at 2022-06-14 03:01:32.391101
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box = Box(1)

    assert box == box
    assert box == Box(1)
    assert not box == Box(2)
    assert box == box and not box == Box(2)
#--------------------------------------------------------------------

# Generated at 2022-06-14 03:01:34.161985
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().get() == Box(1).value
    assert Box([]).to_lazy().get() == Box([]).value
    assert Box('test string').to_lazy().get() == Box('test string').value


# Generated at 2022-06-14 03:01:38.051980
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert not Box(1) == None
    assert not Box(1) == Box(2)
    assert not Box(1) == 1

# Generated at 2022-06-14 03:01:42.241338
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(2) == Box(2)
    assert not (Box(2) == Box(1))
    assert Box('s') == Box('s')
    assert Box(None) == Box(None)
    assert not (Box(2) == Box(None))
    assert not (Box(None) == Box(2))



# Generated at 2022-06-14 03:01:44.455813
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:01:45.961884
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('1') == Box('1')



# Generated at 2022-06-14 03:01:49.359502
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a') == Box('a').to_lazy()

# Generated at 2022-06-14 03:01:52.734822
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) is not Box(1)
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != Box('1')


# Generated at 2022-06-14 03:02:04.090243
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test method to_lazy that transform Box into Lazy with returning value function.
    """

    # Test case: successful transform Box into Lazy
    def test_case_1():
        """
        Test case successful transform Box into Lazy.
        """
        from pymonet.monad_state import State
        from pymonet.lazy import Lazy

        def plus_one(value):
            return value + 1

        def square(value):
            return value * value

        value = 3
        lazy_value = State.unit(value).unit(Box).to_lazy()
        assert lazy_value == Lazy(lambda: value)

        lazy_squares = lazy_value.fmap(plus_one).fmap(square)

# Generated at 2022-06-14 03:02:07.074017
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(3)


# Generated at 2022-06-14 03:02:09.495165
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: Box(1).value)


# Generated at 2022-06-14 03:02:11.350108
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    lazy = Box(lambda x: x + 1).to_lazy()
    # then
    assert lazy().value()(100) == 101

# Generated at 2022-06-14 03:02:13.304901
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def test_value():
        return 10

    assert Box(test_value).to_lazy() == Lazy(test_value)

# Generated at 2022-06-14 03:02:16.402801
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def f() -> int:
        return 3

    assert Box(3).to_lazy() == Lazy(f)

# Generated at 2022-06-14 03:02:19.367151
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(5).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.__repr__(), 'Lazy[Unfolded]'

# Generated at 2022-06-14 03:02:21.431067
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert isinstance(Box(10).to_lazy(), Lazy)
    assert Box(10).to_lazy().get_value()() == Box(10).value



# Generated at 2022-06-14 03:02:23.602834
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:02:26.132755
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(42)

    assert box.to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:02:28.748034
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert (type(Box(123).to_lazy()) == type(Box(123).value_to_lazy())) == True

# Generated at 2022-06-14 03:02:33.118634
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(5).to_lazy(), Lazy)
    assert Box(5).to_lazy().force() == 5


# Generated at 2022-06-14 03:02:36.129229
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    val = Box(1).to_lazy()
    assert(val.value() == 1)

# Generated at 2022-06-14 03:02:38.201149
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 1).fold() == Box(1).to_lazy().fold()

# Generated at 2022-06-14 03:02:40.783989
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def call() -> str:
        return "test"

    assert Box(call).to_lazy() == Lazy(call)

# Generated at 2022-06-14 03:02:43.446658
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:02:51.861929
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    :returns: True if all unit tests pass
    :rtype: bool
    """

    from pymonet.lazy import Lazy

    lazy_instance = Lazy(lambda: 'b')

    box_a = Box(3)
    box_b = Box('a')

    return box_a.to_lazy() == Lazy(lambda: 3) and box_b.to_lazy() == lazy_instance

# Generated at 2022-06-14 03:02:59.844260
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from typing import Callable
    from pymonet.dataloader import Dataloader

    data = Dataloader()

    def mapper(a: int) -> int:
        return a + 5

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box(5).to_lazy().map(mapper) == Lazy(lambda: 10)

    assert data.load_data(Box(5).to_lazy()) == 10
    assert data.load_data(Box(5).to_lazy().map(mapper)) == 15


# Generated at 2022-06-14 03:03:02.150478
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(5)
    lazy = box.to_lazy()

    assert lazy.value() == 5

# Generated at 2022-06-14 03:03:05.119557
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:07.847012
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box class.
    """
    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:03:11.949726
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import thunk

    value = thunk(lambda: 'value')

    lazy = Box(value)
    assert lazy.to_lazy() == value

# Generated at 2022-06-14 03:03:16.522308
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: 1 + 1) == Box(1).to_lazy().map(lambda value: value + 1)
    assert Lazy(lambda: 2) == Box(1).to_lazy().map(lambda value: value + 1).map(lambda value: value ** 2)

# Generated at 2022-06-14 03:03:24.144312
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy().to_value() == Lazy(lambda: 1).to_value()
    assert Box("str").to_lazy().to_value() == Lazy(lambda: "str").to_value()
    assert Box(1.1).to_lazy().to_value() == Lazy(lambda: 1.1).to_value()
    assert Box(True).to_lazy().to_value() == Lazy(lambda: True).to_value()
    assert Box(None).to_lazy().to_value() == Lazy(lambda: None).to_value()


# Generated at 2022-06-14 03:03:25.666672
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(4).to_lazy() == Lazy(lambda: 4)

# Generated at 2022-06-14 03:03:27.352337
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:32.948061
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    # Initialize Box with 1
    box = Box(1)

    # Ensure that Box is equals to Lazy
    assert box.to_lazy() == Lazy(lambda: 1)

    # Ensure that Lazy is callable
    assert box.to_lazy()() == 1

# Generated at 2022-06-14 03:03:36.000403
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)
    assert Box('5').to_lazy() == Lazy(lambda: '5')
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Box(dict(name='Vasya')).to_lazy() == Lazy(lambda: dict(name='Vasya'))


# Generated at 2022-06-14 03:03:37.771447
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    >>> box = Box(1)
    >>> laz = box.to_lazy()
    >>> laz.value
    1
    """

# Generated at 2022-06-14 03:03:41.759292
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(Lazy(lambda: 'bla')).to_lazy() == Lazy(lambda: 'bla')

# Unit tests for method to_try of class Box

# Generated at 2022-06-14 03:03:44.072655
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)

    assert box.to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:46.934965
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('Hello') == Box('Hello').to_lazy().get_or_else('')

# Generated at 2022-06-14 03:03:48.490649
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    val = 5
    assert Box(5).to_lazy() == Lazy(lambda: val)

# Generated at 2022-06-14 03:03:49.902013
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:03:55.187397
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test function test_Box_to_lazy is used to verify that method to_lazy
    of class Box is working properly.
    """

    @given(integers())
    @settings(max_examples=10)
    def _test_Box_to_lazy(value):
        assert Box(value).to_lazy().value() == Box(value).value

    _test_Box_to_lazy()


# Generated at 2022-06-14 03:03:56.303011
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:04:00.314496
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(lambda a: a + 5)
    lazy = Lazy(lambda: box.value)

    assert Lazy.unit(lazy.value(5)) == box.to_lazy().unit(5)


# Generated at 2022-06-14 03:04:04.518234
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try

    from pymonet.lazy import Lazy

    result = Try('someValue', is_success=True).to_lazy()

    assert isinstance(result, Lazy)

# Generated at 2022-06-14 03:04:12.803321
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    @Lazy
    def lazy_func():
        return 2

    def func():
        return 3

    assert Box(2).to_lazy() == Lazy(func)
    assert Box(2).to_lazy() == Box(lazy_func()).to_lazy()

    @Lazy
    def lazy_func():
        return "test"

    def func():
        return "test"

    assert Box("test").to_lazy() == Lazy(func)
    assert Box("test").to_lazy() == Box(lazy_func()).to_lazy()


# Generated at 2022-06-14 03:04:15.852821
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.list import List

    assert Box(List([1, 2, 3, 4])).to_lazy().value() == List([1, 2, 3, 4])

# Generated at 2022-06-14 03:04:21.471551
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box_value = Box("string")

    assert isinstance(box_value.to_lazy(), Lazy)

    assert box_value.to_lazy().fold(lambda: "default value") == "string"



# Generated at 2022-06-14 03:04:26.904821
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:04:35.845126
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.either import Right
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def func():
        return 10

    box = Box(func)

    assert Lazy(func) == box.to_lazy()
    assert Maybe.just(func) == box.to_maybe()
    assert Right(func) == box.to_either()
    assert Try(func, is_success=True) == box.to_try()
    assert Validation.success(func) == box.to_validation()


# Generated at 2022-06-14 03:04:39.333525
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # GIVEN
    box = Box(1)

    # WHEN
    lazy = box.to_lazy()

    # THEN
    assert lazy.bind(int) == 1

# Generated at 2022-06-14 03:04:41.701422
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    r = Box('test').to_lazy()
    assert isinstance(r, Lazy)
    assert r.value() == 'test'



# Generated at 2022-06-14 03:04:45.341922
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:04:51.342855
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for Box.to_lazy function

    :returns: None
    :rtype: None
    """
    from pymonet.lazy import Lazy
    import pytest
    assert Lazy(lambda: 5) == Box(5).to_lazy()
    with pytest.raises(TypeError):
        Box(None).to_lazy()


# Generated at 2022-06-14 03:04:54.725545
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    @Lazy
    def return_one():
        return 1

    assert Try(return_one(), is_success=True) == Box(return_one()).to_try()

# Generated at 2022-06-14 03:04:59.290143
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(2)
    lazy = box.to_lazy()
    assert type(lazy) == Lazy
    assert lazy.value() == box.value


# Generated at 2022-06-14 03:05:01.579500
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:05:02.987996
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().force() == 1
    assert Box("Hello").to_lazy().force() == "Hello"


# Generated at 2022-06-14 03:05:06.355567
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.utils import identity

    assert Box(5).to_lazy() == Lazy(identity(5))


# Generated at 2022-06-14 03:05:12.157278
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box_lazy = Box(lambda x: x + 1).to_lazy()

    assert isinstance(box_lazy, Lazy)
    assert box_lazy.value == Box(lambda x: x + 1).value
    assert box_lazy.value(1) == Box(lambda x: x + 1).value(1)


# Generated at 2022-06-14 03:05:15.344700
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box can be transformed into Lazy by calling to_lazy method.
    """
    from pymonet.lazy import Lazy
    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:05:17.092275
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(100).to_lazy() == Lazy(lambda: 100)  # pragma: no cover

# Generated at 2022-06-14 03:05:18.706693
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:05:21.510811
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given monad Box
    box = Box(1)

    # when transform Box into Lazy
    lazy = box.to_lazy()

    # then Box and Lazy should be equal
    assert box == lazy.value()

# Generated at 2022-06-14 03:05:26.705617
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for to_lazy method of Box class.
    """
    # Given
    box = Box(1)

    # When
    actual = box.to_lazy()

    # Then
    assert actual.value() == 1
    assert not actual.is_folded()


# Generated at 2022-06-14 03:05:28.017185
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Lazy(lambda: 5) == Box(5).to_lazy()

# Generated at 2022-06-14 03:05:31.009938
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    box = Box(10)

    assert box.to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:05:32.655108
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:44.800299
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    value = 2

    assert isinstance(Box(value).to_lazy(), Lazy)
    assert Box(value).to_lazy() == Lazy(lambda: value)

    assert isinstance(Box(Maybe(value)).to_lazy(), Lazy)
    assert Box(Maybe(value)).to_lazy() == Lazy(lambda: Maybe(value))

    assert isinstance(Box(Lazy(lambda: value)).to_lazy(), Lazy)
    assert Box(Lazy(lambda: value)).to_lazy() == Lazy(lambda: Lazy(lambda: value))


# Generated at 2022-06-14 03:05:46.997371
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def get_three():
        return 3

    assert Box(3).to_lazy().get_value() == 3
    assert Box(get_three).to_lazy().get_value()() == 3

# Generated at 2022-06-14 03:05:50.342052
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_test_common import test_to_lazy

    test_to_lazy(Box(42), 42, Lazy, True)


# Generated at 2022-06-14 03:05:51.573898
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert 1 == Box(1).to_lazy().value()



# Generated at 2022-06-14 03:05:59.378277
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box.to_lazy method
    """

    # Test case 1
    # Create Box with value 123
    box = Box(123)
    # Transform this box into Lazy
    lazy = box.to_lazy()
    # Value should be 123
    assert lazy.value() == 123

    # Test case 2
    # Create Box with value 456
    box = Box(456)
    # Transform this box into Lazy
    lazy = box.to_lazy()
    # Value should be 456
    assert lazy.value() == 456

    # Test case 3
    # Create Box with value 789
    box = Box(789)
    # Transform this box into Lazy
    lazy = box.to_lazy()
    # Value should be 789
    assert lazy.value() == 789



# Generated at 2022-06-14 03:06:01.536292
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:06:04.018257
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:06:05.962319
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    with pytest.raises(TypeError):
        Box(10).to_lazy()

# Generated at 2022-06-14 03:06:09.380448
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:06:13.333130
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(10)
    result = box.to_lazy()

    assert isinstance(result, Lazy)
    assert result.value() == 10

# Generated at 2022-06-14 03:06:27.549368
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    target = Box(1)
    # when
    result = target.to_lazy()
    # then
    assert isinstance(result, Lazy)
    assert isinstance(result.fn, FunctionType)
    assert result.is_folded is False
    assert result.fn() == 1



# Generated at 2022-06-14 03:06:31.451574
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(lambda x: x)
    tmp = box.to_lazy()
    assert isinstance(tmp, Lazy)
    assert tmp()(5) == 5



# Generated at 2022-06-14 03:06:35.202414
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:06:43.407684
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Transform Box into Lazy with returning value function.

    :returns: not folded Lazy monad with function returning previous value
    :rtype: Lazy[Function(() -> A)]
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    actual = Box(Try(ValueError())).to_lazy()

    assert isinstance(actual, Lazy)
    assert actual.fold(lambda: 'Failed call') == 'Failed call'

# Generated at 2022-06-14 03:06:45.320853
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:06:48.237153
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_try import Try

    assert Box("abc").to_lazy() == Lazy(lambda: "abc")

    assert Box(Try("123")).to_lazy().fold() == Try("123")

# Generated at 2022-06-14 03:06:49.701409
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(30).to_lazy().fold() == 30



# Generated at 2022-06-14 03:06:51.885848
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(23).to_lazy().fold() == 23

# Generated at 2022-06-14 03:06:54.585473
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(5).to_lazy().map(lambda x: x ** 2).get() == 25


# Generated at 2022-06-14 03:06:58.704812
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(5).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_folded is False
    assert lazy.value() == 5

# Generated at 2022-06-14 03:07:19.130375
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:27.376731
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    assert Box(1).to_lazy().force() == 1
    assert Box('1').to_lazy().force() == '1'
    assert Box([1, 2]).to_lazy().force() == [1, 2]
    assert Box({'value': 1}).to_lazy().force() == {'value': 1}
    assert Box(True).to_lazy().force() is True


# Generated at 2022-06-14 03:07:33.294004
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def f():
        raise TypeError

    assert Box(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: 1)
    assert Box(Try(Lazy(lambda: 1), is_success=True)).to_lazy() == Lazy(lambda: 1)
    assert Box(Try(Lazy(f), is_success=True)).to_lazy() == Lazy(f)



# Generated at 2022-06-14 03:07:36.930508
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy_box = Box(10).to_lazy()
    value = lazy_box.eval()
    assert value == 10


# Generated at 2022-06-14 03:07:39.387176
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    lz = Box(5).to_lazy()
    assert lz == Lazy(lambda: 5)
    assert lz.value == 5



# Generated at 2022-06-14 03:07:41.270471
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:44.236834
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    x = Box(5)
    l = x.to_lazy()

    assert l.to_box() == Box(5)


# Generated at 2022-06-14 03:07:47.446556
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.monad_try
    
    def complete():
        return pymonet.monad_try.Try(123)

    assert Box(complete).to_lazy().value() == complete

# Generated at 2022-06-14 03:07:57.189873
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Tests for Box.to_lazy()
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 3) == Box(3).to_lazy()
    assert Lazy(lambda: '3') == Box('3').to_lazy()
    assert Lazy(lambda: [3]) == Box([3]).to_lazy()
    assert Lazy(lambda: (3,)) == Box((3,)).to_lazy()
    assert Lazy(lambda: {3}) == Box({3}).to_lazy()
    assert Lazy(lambda: {'3': '3'}) == Box({'3': '3'}).to_lazy()

# Generated at 2022-06-14 03:08:00.677703
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:08:42.690121
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()


# Generated at 2022-06-14 03:08:49.256832
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_test import test_monad_laws
    from pymonet.monad_test.test_lazy import test_lazy_laws

    # Test monad laws of Lazy
    test_monad_laws(lambda value: Box(value).to_lazy(), Lazy)
    # Test Lazy behavior
    test_lazy_laws()



# Generated at 2022-06-14 03:08:53.676925
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(4)
    lazy = box.to_lazy()

    assert lazy.is_folded is False
    assert lazy.get() == box.value

# Generated at 2022-06-14 03:08:55.151276
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(7).to_lazy() == Lazy(lambda: 7)

# Generated at 2022-06-14 03:08:59.900319
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)
    assert Box(3).to_lazy().value() == Lazy(lambda: 3).value()
    assert Box(3).to_lazy().value() == 3


# Generated at 2022-06-14 03:09:05.073736
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(Maybe(1)).to_lazy() == Lazy(lambda: Maybe(1))


# Generated at 2022-06-14 03:09:11.212514
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad import Option, Maybe

    value = Option.just(Maybe.just(2))

    lazy_value = value.to_lazy()

    assert isinstance(lazy_value, Lazy)
    assert lazy_value.is_evaluated() is False
    assert lazy_value.get_result() == option(option(2))

    assert lazy_value.is_evaluated() is True
    assert lazy_value.get_result() == option(option(2))



# Generated at 2022-06-14 03:09:14.255283
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(123).to_lazy() == Lazy(lambda: 123)

# Generated at 2022-06-14 03:09:19.186034
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of Box monad.
    """
    box = Box(2)

    lazy = box.to_lazy()

    assert lazy.is_folded is False
    assert lazy.value() == 2

# Generated at 2022-06-14 03:09:26.417563
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.imperative import identity

    assert(Box(5).to_lazy() == Lazy(lambda: 5))
    assert(Box('foo').to_lazy() == Lazy(lambda: 'foo'))
    assert(Box(identity).to_lazy() == Lazy(lambda: identity))

# Generated at 2022-06-14 03:10:13.138080
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy_box = Box(42).to_lazy()

    assert isinstance(lazy_box, Lazy)
    assert lazy_box.force() == 42

# Generated at 2022-06-14 03:10:23.138610
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:10:27.983927
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    box = Box(lambda x: x + 5)

    assert isinstance(box.to_lazy(), Lazy)

# Generated at 2022-06-14 03:10:31.926405
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(True).to_lazy() == Lazy(lambda: True)



# Generated at 2022-06-14 03:10:33.566671
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:10:43.605421
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    # Test different types of input data
    assert Box(10).to_lazy() == Box(10).to_lazy()
    assert Box(10).to_lazy() != Box(20).to_lazy()
    assert Box(20).to_lazy() == Box(20).to_lazy()
    assert Box(20).to_lazy() != Box(10).to_lazy()
    assert Box(10).to_lazy() == Box(10).to_lazy()
    assert Box(20).to_lazy() != Box(10).to_lazy()

    # Test different types of input data
    assert Box('10').to_lazy() == Box('10').to_lazy()
    assert Box('10').to_

# Generated at 2022-06-14 03:10:48.615773
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    result = Box(lambda x: x).to_lazy()
    assert isinstance(result, Lazy)
    assert result.get()(2) == 2



# Generated at 2022-06-14 03:10:57.900427
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == \
        Lazy(lambda: 1)

# Generated at 2022-06-14 03:11:03.459809
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    value = 0
    box = Box(value)

    # When
    lazy = box.to_lazy()

    # Then
    assert lazy.fold() == value


# Unit tests for method to_maybe of class Box

# Generated at 2022-06-14 03:11:07.356577
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
