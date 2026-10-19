

# Generated at 2022-06-14 03:01:38.334657
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Identity

    identity = Identity(Box(10))
    assert isinstance(identity.to_lazy(), Lazy)
    assert identity.to_lazy().value() == identity.value.value



# Generated at 2022-06-14 03:01:40.387224
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 2



# Generated at 2022-06-14 03:01:46.537212
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    from pymonet.either import Right

    assert Box('hello') == Box('hello')
    assert Box(42) == Box(42)
    assert Box((42, Right('hello'))) == Box((42, Right('hello')))
    assert Box('hello') != Box('world')
    assert Box(42) != Box(43)
    assert Box((42, Right('hello'))) != Box((42, Right('world')))
    assert Box('hello') != 'hello'
    assert Box(42) != 42
    assert Box((42, Right('hello'))) != (42, Right('hello'))



# Generated at 2022-06-14 03:01:52.626915
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad import Monad
    from pymonet.lazy import Lazy

    monad: Monad[int] = Box(5)
    lazy_monad: Monad[int] = monad.to_lazy()
    assert isinstance(lazy_monad, Lazy)
    assert lazy_monad.get() == 5



# Generated at 2022-06-14 03:01:54.973773
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:02:01.301981
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Arrange
    from pymonet.maybe import Maybe
    from pymonet.either import Right
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    box = Box(5)

    # Act
    maybe = box.to_maybe()
    either = box.to_either()
    lazy = box.to_lazy()
    try_ = box.to_try()
    validation = box.to_validation()

    # Assert
    assert maybe == Maybe.just(5)
    assert either == Right(5)
    assert lazy() == 5
    assert try_ == Try(5, is_success=True)
    assert validation == Validation.success(5)

# Generated at 2022-06-14 03:02:05.894061
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert_that(Box(5), equal_to(Box(5)))
    assert_that(Box(5), is_not(equal_to(Box(6))))
    assert_that(Box(5), is_not(equal_to(Box('test'))))


# Generated at 2022-06-14 03:02:07.589687
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)



# Generated at 2022-06-14 03:02:09.519792
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:02:11.053398
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box("1") == Box("1")



# Generated at 2022-06-14 03:02:14.635505
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('some data').to_lazy() == Lazy(lambda: 'some data')


# Generated at 2022-06-14 03:02:18.602940
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('a') == Box('a')

    assert Box(lambda x: x+1) != Box(1)
    assert Box([1]) != Box('1')



# Generated at 2022-06-14 03:02:20.943259
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('test').to_lazy().map(lambda x: x * 2).value() == 'testtest'

# Generated at 2022-06-14 03:02:22.853830
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert type(Box(1).to_lazy()) == Lazy
    assert Box(1).to_lazy().fold() == 1

# Generated at 2022-06-14 03:02:31.985015
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('a') == Box('a')
    assert Box(1.0) == Box(1.0)
    assert Box(False) == Box(False)
    assert Box(None) == Box(None)
    assert Box(Box(1)) == Box(Box(1))
    assert Box(1) != Box('a')
    assert Box(1) != Box(False)
    assert Box(1) != Box(1.0)
    assert Box(1) != Box(Box(1))



# Generated at 2022-06-14 03:02:37.126652
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """
    Unit test for method __eq__ of class Box.
    """
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 1


# Generated at 2022-06-14 03:02:42.374614
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for constructor of class Box
    """
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box('value').to_lazy().map(lambda v: v + '1') == Lazy(lambda: 'value1')


# Generated at 2022-06-14 03:02:47.148823
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('1') != Box(1)
    assert Box('1') != Box('2')
    assert Box(1) != Ellipsis



# Generated at 2022-06-14 03:02:50.772212
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy

    assert isinstance(Box('some value').to_lazy(), pymonet.lazy.Lazy)



# Generated at 2022-06-14 03:02:54.224816
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != []
    assert Box(1) != 1



# Generated at 2022-06-14 03:02:58.865192
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(2) == Box(2)
    assert not Box(2) == Box(3)



# Generated at 2022-06-14 03:02:59.874647
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().fold() == 42

# Generated at 2022-06-14 03:03:02.735463
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad import monad_test

    monad_test(Box(5), Box(5).to_lazy())

# Generated at 2022-06-14 03:03:06.778799
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    b1 = Box(1)
    b2 = Box("a")
    assert b1 == b1
    assert b2 == b2
    assert b1 != b2
    assert b2 != b1

# Generated at 2022-06-14 03:03:10.056811
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """Unit test for method __eq__ of class Box"""
    assert Box(1) == Box(1)
    assert Box(1) == Box(2) is False
    assert Box(1) == 1 is False


# Generated at 2022-06-14 03:03:21.159009
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, catch
    from pymonet.validation import Validation

    def func():
        return 42

    lazy = Box(func).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 42
    assert lazy.is_folded is False

    lazy = lazy.map(lambda v: v * 2)
    assert lazy.fold() == 84
    assert lazy.is_folded is False

    lazy = lazy.flat_map(lambda v: Lazy(lambda: v + 2))
    assert lazy.fold() == 86
    assert lazy.is_folded is False

    lazy = lazy.filter(lambda v: Validation.success(v > 50))
    assert lazy.fold() == 86
    assert lazy.is_folded is False

    lazy

# Generated at 2022-06-14 03:03:26.884810
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    print("Unit test for method to_lazy of class Box")
    print("Input: Box('Hello World')")
    print("Expected result: Lazy(lambda: 'Hello World')")
    print("Real result:", Box('Hello World').to_lazy())

test_Box_to_lazy()

# Generated at 2022-06-14 03:03:33.567800
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    def test_function():
        """
        Function for testing to_lazy method.

        :returns: 1
        :rtype: int
        """
        return 1

    assert Box(1).to_lazy().fold(test_function) == 1

# Generated at 2022-06-14 03:03:38.398563
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    """Unit test for method __eq__ of class Box"""
    assert Box(1) == Box(1)
    assert not(Box(1) == Box(2))
    assert not(Box(1) == 2)
    assert not(Box(1) == None)
    assert Box(None) == Box(None)
    assert not(Box(None) == 2)
    assert not(Box(None) == None)


# Generated at 2022-06-14 03:03:40.774762
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:46.393830
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(40).to_lazy() == Lazy(lambda: 40)


# Generated at 2022-06-14 03:03:50.048854
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test that calling this method on Box
    resulted in Lazy object with returning
    value function

    :return: None
    """
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(10).to_lazy().unsafe_force() == 10
    assert type(Box(10).to_lazy()) == Lazy

# Generated at 2022-06-14 03:03:52.553933
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    value = Box(4)

    # When
    lazy = value.to_lazy()

    # Then
    assert lazy.value() == 4


# Generated at 2022-06-14 03:03:54.841347
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # arrange
    box = Box(10)
    # act
    result = box.to_lazy()
    # assert
    assert 10 == result.run()

# Generated at 2022-06-14 03:04:01.499563
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, UnitTestLazy
    from pymonet.maybe import Maybe
    from pymonet.either import Right

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: 2).map(lambda x: x + 1) == Box(1).to_lazy().map(lambda x: x + 1)
    assert Lazy(lambda: 3) == Lazy(lambda: 3).ap(Box(2).to_lazy().map(lambda x: lambda y: x + y))
    assert Lazy(lambda: 1) == UnitTestLazy(lambda: 1)
    assert Lazy(lambda: 1).pure(Maybe) == Maybe.pure(1)
    assert Lazy(lambda: 1).pure(Right) == Right(1)


# Unit

# Generated at 2022-06-14 03:04:12.706977
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box

    :returns: nothing
    """
    @raises(Exception)
    def test_raise_exception():
        raise Exception('Expected exception')

    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)
    assert Box('test').to_lazy() == Lazy(lambda: 'test')
    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Box({1, 2, 3}).to_lazy() == Lazy(lambda: {1, 2, 3})

# Generated at 2022-06-14 03:04:19.724182
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 5).fold() == Box(5).to_lazy().fold()
    assert Lazy(lambda: 5).fold() == Box(Lazy(lambda: 5)).to_lazy().fold()
    assert Lazy(lambda: Try(5, is_success=True)).fold() == Box(Try(5, is_success=True)).to_lazy().fold()


# Generated at 2022-06-14 03:04:25.031036
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    >>> def return_9():
    ...     return 9
    ...
    >>> box = Box(return_9)
    >>> lazy = box.to_lazy()
    >>> lazy.fold()
    9
    """
    pass

# Generated at 2022-06-14 03:04:28.074449
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().fold(lambda r: r(), lambda e: e)() == 3

# Generated at 2022-06-14 03:04:31.659560
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(4).to_lazy() == Lazy(lambda: 4)

# Generated at 2022-06-14 03:04:34.879951
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(4).to_lazy() == Lazy(lambda: 4)

# Generated at 2022-06-14 03:04:36.813093
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy().fold() == 1


# Generated at 2022-06-14 03:04:40.927046
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # when
    lazy = Box(1).to_lazy()

    # then
    assert isinstance(lazy, Lazy)
    assert lazy.is_folded is False
    assert lazy.value() == 1

# Generated at 2022-06-14 03:04:47.687976
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def assert_value(lazy_value: int) -> int:
        assert lazy_value == 5
        return 5

    box_lazy = Box(5).to_lazy()
    assert_value(box_lazy._computation())


# Generated at 2022-06-14 03:04:54.815542
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Data type for storage any type of data
    """
    assert Box(5).to_lazy() == Box(5).to_lazy()
    assert Box(5).to_lazy().is_folded() == False
    assert Box(5).to_lazy().get()() == 5


# Generated at 2022-06-14 03:05:01.621454
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # Given
    x = Box(5)
    y = Box(6)
    z = Lazy(lambda: x.value + y.value)

    # When
    to_lazy = x.to_lazy() + y.to_lazy()

    # Then
    assert isinstance(to_lazy, Lazy)
    assert isinstance(to_lazy.value(), int)
    assert to_lazy == z


# Generated at 2022-06-14 03:05:06.815704
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box('1').to_lazy()

    assert lazy == Lazy(lambda: '1')
    assert lazy.get_value() == '1'


# Generated at 2022-06-14 03:05:07.634599
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1).to_lazy()

# Generated at 2022-06-14 03:05:12.115182
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    box = Box(4)
    lazy = box.to_lazy()
    assert lazy == Lazy(lambda: 4)
    assert lazy.eval() == Lazy(4).eval()



# Generated at 2022-06-14 03:05:13.575392
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:05:19.074934
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:05:22.917719
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(15).to_lazy() == Lazy(lambda: 15)
    assert Box(15).map(lambda x: x * 2).to_lazy() == Lazy(lambda: 30)
    assert Box(15).bind(lambda x: x * 2) == 30

# Generated at 2022-06-14 03:05:28.305098
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def my_function():
        return 5

    lazy = Lazy(my_function)
    boxed = Box(my_function)
    boxed_lazy = boxed.to_lazy()

    assert lazy == boxed_lazy


# Generated at 2022-06-14 03:05:32.904736
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # prepare
    value = 1
    box = Box(value)

    # launch
    result = box.to_lazy()

    # assert
    assert result.value() == value

# Generated at 2022-06-14 03:05:35.475513
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(36).to_lazy() == Box(36).to_lazy()

# Generated at 2022-06-14 03:05:38.412157
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:42.561108
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_option import Some

    assert Box(1).to_lazy() == Lazy(Some(1))
    assert Box(2).to_lazy() == Lazy(Some(2))



# Generated at 2022-06-14 03:05:49.586484
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 'hello') == Box('hello').to_lazy()
    assert Lazy(lambda: 5) == Box(5).to_lazy()
    assert Lazy(lambda: 3.14) == Box(3.14).to_lazy()
    assert Try(5, is_success=True) == Box(5).to_try()
    assert Try('hello', is_success=True) == Box('hello').to_try()
    assert Try(3.14, is_success=True) == Box(3.14).to_try()



# Generated at 2022-06-14 03:05:54.004355
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # When we create Box with value and transform it into Lazy
    result = Box('Test').to_lazy()

    # Then result should be instance of class Lazy
    assert isinstance(result, Box)

    # And result should be equal to Lazy class with the same value
    assert result == Box('Test')



# Generated at 2022-06-14 03:06:00.564094
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    def to_lazy(value):
        return Box(value).to_lazy()

    assert to_lazy(23).value() == 23
    assert to_lazy('abc').value() == 'abc'
    assert to_lazy(None).value() is None
    assert to_lazy([]).value() == []
    assert to_lazy([1, 2, 3]).value() == [1, 2, 3]
    assert to_lazy({}).value() == {}
    assert to_lazy({'a': 1, 'b': 2}).value() == {'a': 1, 'b': 2}
    assert to_lazy(()).value() == ()
    assert to_lazy((1, 2, 3)).value() == (1, 2, 3)

# Generated at 2022-06-14 03:06:13.675627
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:06:16.374863
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_list import List

    assert Box(Try(42)).to_lazy().map(lambda a: a()).value == List([42])

# Generated at 2022-06-14 03:06:20.793372
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    print('test_Box_to_lazy')

    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:06:30.429321
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Try.pure(1).to_box() == Box(1)
    assert Try.raise_(ValueError(1)).to_box().to_try() == Try(None, False)
    assert Validation.success(1).to_box() == Box(1)
    assert Validation.fail(ValueError(1)).to_box().to_validation() == Validation.fail(ValueError(1))



# Generated at 2022-06-14 03:06:39.361730
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of Box class.
    """
    from pymonet.monad_try import Try
    from pymonet.either import Right, Left
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    try_ = Try(1, is_success=True)
    right = Right(2)
    left = Left(3)
    validation = Validation.success(4)
    lazy = Lazy(lambda: 5)

    assert Box(try_).to_maybe() == Box(try_.to_maybe()).to_maybe()
    assert Box(right).to_maybe() == Box(right.to_maybe()).to_maybe()
    assert Box(left).to_maybe() == Box(left.to_maybe()).to_maybe()
   

# Generated at 2022-06-14 03:06:44.690434
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy method
    """

    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5).to_box().to_lazy() == Lazy(lambda: 5)
    assert Lazy(lambda: 5).to_box().to_lazy().eval() == 5


# Generated at 2022-06-14 03:06:46.748710
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(lambda x: x).to_lazy() == Box(lambda x: x).to_lazy().value()


# Generated at 2022-06-14 03:06:49.086633
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(33)
    assert box.to_lazy() == Lazy(lambda: 33)

# Generated at 2022-06-14 03:06:51.864132
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(42).to_lazy() == Lazy(lambda: 42)
    assert Box(42).to_lazy().value() == 42

# Generated at 2022-06-14 03:06:56.832465
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    from pymonet.monad_try import Try

    assert isinstance(Box(1).to_lazy(), Try)
    assert Box(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:07:20.242627
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert str(Box(1).to_lazy()) == 'Lazy(<function Box.__init__.<locals>.<lambda> at {}>)'.format(hex(id(Box(1).__init__.__locals__['<lambda>'])))



# Generated at 2022-06-14 03:07:22.092599
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('Value').to_lazy().fold() == 'Value'



# Generated at 2022-06-14 03:07:25.368520
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Box to Lazy test
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()


# Generated at 2022-06-14 03:07:27.908496
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:07:31.100568
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(1).to_lazy().eval() == 1

    # Unit test for method method_that_can_cause_errors of class Box

# Generated at 2022-06-14 03:07:35.766346
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given: a lazy monad
    lazy_monad = Lazy(lambda: 'hello')

    # And: a Box contians this lazy monad
    box = Box(lazy_monad)

    # When: we transform box into lazy monad
    lazy_monad_result = box.to_lazy()

    # Then: monad value will be the same
    assert lazy_monad_result.value() == 'hello'

# Generated at 2022-06-14 03:07:37.718506
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Box(1).to_lazy(), Lazy)

# Generated at 2022-06-14 03:07:39.779132
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    _box = Box(1)

    # When
    _lazy = _box.to_lazy()

    # Then
    assert _lazy.fold() == 1

# Generated at 2022-06-14 03:07:41.131195
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def f():
        return 2

    assert Box(2).to_lazy() == Lazy(f)

# Generated at 2022-06-14 03:07:42.682785
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(3)
    assert box.to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:08:28.045718
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:08:30.325048
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(1).to_lazy()
    assert lazy.fold(lambda: 0)() == 1

# Generated at 2022-06-14 03:08:33.104696
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(5).to_lazy()
    assert 5 == lazy.evaluate()


# Generated at 2022-06-14 03:08:36.830092
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().value == 1
    assert Box(1).to_lazy().value == Lazy(lambda: 1).value



# Generated at 2022-06-14 03:08:39.481286
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:08:44.054283
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    to_lazy_result = Box(5).to_lazy()
    assert isinstance(to_lazy_result, Lazy)
    assert to_lazy_result.value() == 5


# Generated at 2022-06-14 03:08:50.986603
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    box = Box(2)
    assert box.to_lazy() == Lazy(lambda: 2)
    assert box.to_lazy().bind(lambda x: Lazy(lambda: x * 3)) == Lazy(lambda: 6)
    assert box.to_lazy().to_try() == Try(lambda: 2, is_success=True)



# Generated at 2022-06-14 03:08:54.036717
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test wether to_lazy method correctly return lazy value with stored value
    """
    assert Box(1).to_lazy() == Lazy(Lazy(lambda: 1))

# Generated at 2022-06-14 03:08:56.798004
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    lazy = Box(10).to_lazy()
    assert lazy.fold() == 10


# Generated at 2022-06-14 03:08:59.063379
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(42).to_lazy().to_list() == [42]

# Generated at 2022-06-14 03:10:31.156763
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(5)
    lazy = box.to_lazy()

    assert lazy.evaluate() == 5
    assert lazy.evaluate() == 5

# Generated at 2022-06-14 03:10:33.478384
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:10:35.520321
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:10:41.939251
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(123).to_lazy() == Lazy(lambda: 123)
    assert Box('abc').to_lazy() == Lazy(lambda: 'abc')
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Box({'a': 1}).to_lazy() == Lazy(lambda: {'a': 1})

# Generated at 2022-06-14 03:10:44.709619
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(123).to_lazy() == Lazy(lambda: 123)


# Generated at 2022-06-14 03:10:46.523181
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box_val = Box(123)

    assert box_val.to_lazy().equals(Lazy(lambda: 123))


# Generated at 2022-06-14 03:10:49.021495
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def get_string() -> str:
        return 'string'

    assert Box(get_string).to_lazy().value() == get_string()

# Generated at 2022-06-14 03:10:51.558601
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().is_lazy
    assert not Box(1).to_lazy().is_forced
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:10:52.733887
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def function():
        return 42
    assert Box(function).to_lazy().unfold() == 42

# Generated at 2022-06-14 03:10:56.139225
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    b = Box(1)
    bl = b.to_lazy()
    assert bl.value() == 1