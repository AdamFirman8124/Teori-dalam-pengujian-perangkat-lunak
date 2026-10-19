

# Generated at 2022-06-14 03:01:35.662114
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1), 'Should be equal'
    assert not (Box(1) == Box(2)), 'Should not be equal'



# Generated at 2022-06-14 03:01:39.314931
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 2
    assert Box(1) != [1]
    assert Box(1) != ('1',)
    assert Box(1) != {'1': 1}
    assert Box(1) != None


# Generated at 2022-06-14 03:01:47.758554
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('value') == Box('value')
    assert Box([]) == Box([])
    assert Box({}) == Box({})

    assert Box(1) == 1
    assert Box('value') == 'value'
    assert Box([]) == []
    assert Box({}) == {}

    assert 1 == Box(1)
    assert 'value' == Box('value')
    assert [] == Box([])
    assert {} == Box({})

    assert Box(1) != Box(2)
    assert Box('value') != Box('value2')
    assert Box([1]) != Box([])
    assert Box({'key': 1}) != Box({})

    assert Box(1) != 2
    assert Box('value') != 'value2'
    assert Box([1]) != [2]
   

# Generated at 2022-06-14 03:01:50.144396
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    result = Box(7).to_lazy()
    assert result == Lazy(lambda: 7)

# Generated at 2022-06-14 03:01:55.008616
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_lazy import unit
    from pymonet import id

    value = 4
    assert Box(value).to_lazy() == Lazy(unit(id, value))


# Generated at 2022-06-14 03:01:56.709242
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert '10' == Box(10).to_lazy().map(str).fold()


# Generated at 2022-06-14 03:01:59.295781
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(3) == Box(3)
    assert not (Box(4) == Box(5))



# Generated at 2022-06-14 03:02:04.549149
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 1
    assert Box(1) != 'string'
    assert Box(1) != None
    assert Box(1) != []


# Generated at 2022-06-14 03:02:07.247976
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1) and Box([1, 2]) == Box([1, 2])
    assert not(Box([1, 2]) == Box([1, 2, 3]))


# Generated at 2022-06-14 03:02:09.709585
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1)
    assert Box('one') == Box('one')
    assert not (Box('one') != Box('one'))


# Generated at 2022-06-14 03:02:12.984134
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    b = Box(42)
    l = b.to_lazy()
    assert type(l) == Lazy
    assert l.evaluate() == b.value

# Generated at 2022-06-14 03:02:16.550990
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1

# Generated at 2022-06-14 03:02:19.157468
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Arrange
    box = Box(2)

    # Act
    lazy = box.to_lazy()

    # Assert
    assert lazy.value() == 2


# Generated at 2022-06-14 03:02:20.956601
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().get() == 5
    assert Box('5').to_lazy().get() == '5'

# Generated at 2022-06-14 03:02:23.751196
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    box = Box(10)

    # When
    lazy = box.to_lazy()

    # Then
    assert lazy.__str__() == 'Lazy[folded=False]'
    assert lazy.get() == 10

# Generated at 2022-06-14 03:02:26.251549
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(100).to_lazy() == Lazy(lambda: 100)

# Generated at 2022-06-14 03:02:30.002680
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 42) == Box(42).to_lazy()

# Generated at 2022-06-14 03:02:32.935193
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:02:36.760612
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(10)
    lazy = box.to_lazy()

    assert (box == lazy.fold(lambda x: Box(x)))



# Generated at 2022-06-14 03:02:39.746140
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box1 = Box(42)
    result = box1.to_lazy()
    assert result == Lazy(lambda: 42)



# Generated at 2022-06-14 03:02:45.702255
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    obj = Box(lambda: 3)

    assert isinstance(obj.to_lazy(), Lazy)
    assert obj.to_lazy() == Lazy(lambda: obj)


# Generated at 2022-06-14 03:02:48.816784
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:02:52.327956
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    def function():
        return 2

    assert Box(function).to_lazy().fold() == 2, 'value not equal to initial function result'



# Generated at 2022-06-14 03:02:55.236698
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:02:56.627497
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().get() == 1

# Generated at 2022-06-14 03:02:59.757316
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def f(): return 1  # noqa
    a = Box(f).to_lazy()

    assert a.fold(lambda f: f()) == 1

# Generated at 2022-06-14 03:03:12.663728
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad import Functor
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation
    from pymonet.either import Right

    box = Box(42)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 42

    def test_function(value: int) -> Functor[int]:
        """
        Function for testing Functor interface implementation.
        """
        return box

    # Test Functor interface implementation
    assert lazy.map(test_function).value() == box

    # Test MonadTry interface implementation

# Generated at 2022-06-14 03:03:14.276638
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().eval() == 42

# Generated at 2022-06-14 03:03:16.966066
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:03:21.234574
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5) == Lazy(lambda: 5)
    assert Lazy(lambda: 5) == Box(5).to_lazy()
    assert Lazy(lambda: 7) == Box(7).to_lazy()



# Generated at 2022-06-14 03:03:25.863069
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(5)

    assert box.to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:03:30.552662
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().unfold() == 10
    assert Box(10.0).to_lazy().unfold() == 10.0
    assert Box('10').to_lazy().unfold() == '10'
    assert Box((10,)).to_lazy().unfold() == (10,)

# Generated at 2022-06-14 03:03:33.887473
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    from pymonet.lazy import Lazy

    assert Box('Hello').to_lazy() == Lazy(lambda: 'Hello')


# Generated at 2022-06-14 03:03:40.768268
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    box = Box(1)
    assert isinstance(box.to_lazy(), Lazy)
    assert box.to_lazy().value()() == 1
    assert isinstance(box.to_maybe(), Maybe)
    assert box.to_maybe().value == 1
    assert isinstance(box.to_try(), Try)
    assert box.to_try().value == 1
    assert isinstance(box.to_validation(), Validation)
    assert box.to_validation().valid == True



# Generated at 2022-06-14 03:03:44.311636
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Box(3).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 3


# Generated at 2022-06-14 03:03:49.377716
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # Arrange
    value = [1, 2, 3]
    box = Box(value)
    expected = Lazy(lambda: [1, 2, 3])

    # Act
    actual = box.to_lazy()

    # Assert
    assert isinstance(actual, Lazy)
    assert actual == expected

# Generated at 2022-06-14 03:03:52.330944
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    value = 5

    assert Box(value).to_lazy().value() == value
    assert Box(value).to_lazy() == Lazy(lambda: value)

# Generated at 2022-06-14 03:03:54.458767
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:03:56.502944
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Lazy(lambda: 10) == Box(10).to_lazy()

# Generated at 2022-06-14 03:03:59.404345
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    BOX = Box(100)
    assert BOX.to_lazy() == Lazy(lambda: 100)


# Generated at 2022-06-14 03:04:06.650911
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method ``to_lazy`` of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:04:09.737198
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    from pymonet.lazy import Lazy

    with pytest.raises(AssertionError):
        Lazy.of(lambda: 'Test').equals(Box('Test').to_lazy())

# Generated at 2022-06-14 03:04:12.044890
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy() == Lazy(lambda: 2)
    assert Box(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:04:19.480399
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(4).to_lazy() == Lazy(lambda: 4)
    assert Box(4).to_lazy().map(lambda x: x * 3) == Lazy(lambda: 12)
    assert Box(Try(4, is_success=True)).to_lazy().ap(Lazy(lambda: Try(lambda x: x * 3, is_success=True))).value.unwrap() == 12

# Generated at 2022-06-14 03:04:26.819605
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet import Box
    from pymonet.lazy import Lazy

    box = Box(1)
    actual = box.to_lazy()
    expected = Lazy(lambda: 1)

    assert(isinstance(actual, Lazy))
    assert(actual.is_equal_to(expected))

# Generated at 2022-06-14 03:04:31.822414
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    value = 1

    # When
    box = Box(value)
    lazy = box.to_lazy()
    result = lazy.eval()

    # Then
    assert result == value

# Generated at 2022-06-14 03:04:34.709877
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = b'xxx'
    box = Box(value)
    lazy_box = box.to_lazy()

    assert lazy_box.fold_left(lambda value: value) == value

# Generated at 2022-06-14 03:04:37.715469
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:04:40.402514
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import Lazy

    box = Box(lambda x: x * 2)
    assert Lazy(lambda: lambda x: x * 2) == box.to_lazy()

# Generated at 2022-06-14 03:04:43.335452
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1



# Generated at 2022-06-14 03:04:54.965221
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(None).to_lazy() == Lazy(lambda: None)
    assert Box('Hello').to_lazy() == Lazy(lambda: 'Hello')
    assert Box(('Hello', 'World')).to_lazy() == Lazy(lambda: ('Hello', 'World'))
    assert Box(('Hello', None)).to_lazy() == Lazy(lambda: ('Hello', None))
    assert Box([1, 2, 3, 4]).to_lazy() == Lazy(lambda: [1, 2, 3, 4])
    assert Box({1, 2, 3, 4}).to_lazy() == Lazy(lambda: {1, 2, 3, 4})
    assert Box

# Generated at 2022-06-14 03:04:58.668135
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Maybe.nothing().to_lazy() == Lazy(Maybe.nothing)



# Generated at 2022-06-14 03:05:04.026633
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def print_five_times(s):
        for i in range(5):
            print(s)

    lazy_five = Box(print_five_times).to_lazy()
    assert isinstance(lazy_five, Lazy)
    assert lazy_five.fold(lambda x: x('Hello')) == None


# Generated at 2022-06-14 03:05:08.639775
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy() function

    :returns: None
    :rtype: NoneType
    """
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:05:12.288470
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    value = 10
    box = Box(value)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy.value() == value

# Generated at 2022-06-14 03:05:15.799799
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold() == 1
    assert Box(2.0).to_lazy().fold() == 2.0
    assert Box("test").to_lazy().fold() == "test"
    assert Box(True).to_lazy().fold() is True

# Generated at 2022-06-14 03:05:19.042100
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    test_lazy = Box(2).to_lazy()
    assert test_lazy == Lazy(lambda: 2)
    assert test_lazy.run() == 2
    assert test_lazy.run() == 2
    assert test_lazy.run() == 2



# Generated at 2022-06-14 03:05:22.917806
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for to_lazy method of Box class.
    """
    from pymonet.lazy import Lazy

    def test_func():
        return 1

    box = Box(test_func)

    lazy = box.to_lazy()

    assert lazy == Lazy(test_func)



# Generated at 2022-06-14 03:05:25.995383
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def f():
        return 42

    assert Box(f).to_lazy().value() == 42

# Generated at 2022-06-14 03:05:27.410044
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:05:38.269260
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.functor import Functor

    def to_tuple(a: int) -> tuple:
        return a, a*a

    assert Functor[Box].fmap(to_tuple, Box(2)).__eq__((2, 4))

# Generated at 2022-06-14 03:05:43.782287
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    def make_assertions(value):
        assert isinstance(value, int)
        assert value == 42

    box = Box(42)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    lazy.fold(make_assertions)


# Generated at 2022-06-14 03:05:47.690528
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    verify_all_methods = Lazy(lambda: Lazy(lambda: Box(1).to_lazy())).map(lambda x: \
                                Lazy(lambda: x == Lazy(lambda: Box(1).to_lazy()))).map(lambda x: x.value).value

    assert verify_all_methods is True

# Generated at 2022-06-14 03:05:50.507276
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().fold(lambda: 1) == 1
    assert Box(2).to_lazy().fold(lambda: 2) == 2


# Generated at 2022-06-14 03:05:58.432034
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_validation import Validation
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().bind(lambda x: Lazy(lambda: x + 1)).value() == 2
    assert Box(1).to_try().bind(lambda x: Try(x + 1)).value() == 2
    assert Box(1).to_validation().bind(
        lambda x: Validation.success(x + 1)).value() == 2
    assert Box(1).to_validation().bind(
        lambda x: Validation.fail([x + 1])).errors == [2]



# Generated at 2022-06-14 03:06:01.419489
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    print('test Box to_lazy')
    assert Box(1).to_lazy().value() == 1
    assert Box(None).to_lazy().value() is None


# Generated at 2022-06-14 03:06:12.093167
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.

    :returns: nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy().value() == 1
    assert Box('hello').to_lazy().value() == 'hello'
    assert Box(Lazy(lambda: 1)).to_lazy().value() == 1
    assert Box(Lazy(lambda: 'hello')).to_lazy().value() == 'hello'



# Generated at 2022-06-14 03:06:14.709643
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:06:27.292603
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_either import Left
    from pymonet.monad_try import Try

    assert Box(1).to_lazy() == Lazy((lambda: 1), True)
    assert Box(1).to_maybe().to_lazy() == Lazy((lambda: 1), True)
    assert Box(1).to_try().to_lazy() == Lazy((lambda: 1), True)
    assert Box(1).to_either().to_lazy() == Lazy((lambda: 1), True)
    assert Box(1).to_validation().to_lazy() == Lazy((lambda: 1), True)
    assert Box(Left(1)).to_lazy() == Lazy(lambda: Left(1), True)

# Generated at 2022-06-14 03:06:32.654757
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy, ValueIsNotFoldedException

    assert(Box(1).to_lazy() == Lazy(lambda: 1))

    lazy = Box(1).to_lazy()
    assert(lazy.fold() == 1)
    assert(lazy.fold() == 1)

    lazy = Box(1).to_lazy()
    assert(lazy.fold() == 1)
    assert(lazy.fold() == 1)

    lazy = Box(1).to_lazy()
    try:
        lazy.fold()
        raise AssertionError('Should raise ValueIsNotFoldedException')
    except ValueIsNotFoldedException:
        pass


# Generated at 2022-06-14 03:06:50.870483
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def test_function(arg1, arg2):
        return arg1 + arg2

    assert Box(test_function).to_lazy() == Lazy(test_function)

# Generated at 2022-06-14 03:06:54.294246
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box
    """

    lazy = Box('test').to_lazy()

    assert lazy.value() == 'test'

# Generated at 2022-06-14 03:06:58.830477
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = (1, 2, 3)
    box = Box(value)
    lazy = box.to_lazy()
    result = lazy.fold(lambda: None)
    assert result == value



# Generated at 2022-06-14 03:07:06.366038
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monoid import Monoid
    from pymonet.lazy import Lazy
    from pymonet.monad_lst import MonadLst
    from pymonet.monad_try import MonadTry

    # Check Monad Laws:
    # The left identity law:
    # return a >>= f  ≡ f a

# Generated at 2022-06-14 03:07:12.084416
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy_truthy = Box(lambda: 'TEST').to_lazy().map(lambda f: f()).join()
    lazy_truthy_2 = Lazy(lambda: Box(lambda: 'TEST').bind(lambda f: f())).join()
    assert lazy_truthy == lazy_truthy_2

# Generated at 2022-06-14 03:07:14.989086
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:07:17.306904
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('test').to_lazy().get_or_else('') == 'test'



# Generated at 2022-06-14 03:07:20.047097
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().map(lambda x: x * 2).map(lambda x: x // 2).get_value() == 2



# Generated at 2022-06-14 03:07:23.456933
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Arrange
    box = Box(1)

    # Act
    lazy = box.to_lazy()

    # Assert
    assert lazy.get() == 1

# Generated at 2022-06-14 03:07:25.241631
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert(Box(10).to_lazy() == Lazy(lambda: 10))



# Generated at 2022-06-14 03:07:41.203139
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    a = Box(1)

    assert a.to_lazy().map(lambda x: x + 2) == Lazy(lambda: 3)

# Generated at 2022-06-14 03:07:42.979299
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy_box = Box(10).to_lazy()

    assert isinstance(lazy_box, Lazy)
    assert lazy_box == Lazy(lambda: 10)

# Generated at 2022-06-14 03:07:45.832317
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:48.210933
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:07:50.298712
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:54.434427
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy_box = Box(2).to_lazy()  # lazy_box = Lazy[Function(() -> 2)]

    assert lazy_box.value() == 2


# Generated at 2022-06-14 03:07:56.876332
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:07:59.848836
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(123).to_lazy() == Lazy(lambda: 123)

# Generated at 2022-06-14 03:08:01.508396
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box('test').to_lazy() == Box('test').to_lazy()

# Generated at 2022-06-14 03:08:03.019892
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().force() == 10

# Generated at 2022-06-14 03:08:40.338273
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:08:48.260822
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad import _, __

    assert Box(1).to_lazy() == _(1)
    assert Box(2).to_lazy() == _(2)
    assert Box(1).map(lambda x: x + 2).to_lazy() == __(3)
    assert Box(Box(1).to_lazy).ap(Box(_(2))).value == 2
    assert Box(Box(1).to_lazy).ap(Box(_(2).map(lambda x: x + 1))).value == 3

# Generated at 2022-06-14 03:08:57.285397
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def function_return_value(value):
        return value

    box = Box('value')
    assert box.to_lazy() == Lazy(function_return_value('value'))
    assert box.to_maybe() == Maybe.just('value')
    assert box.to_either() == Right('value')
    assert box.to_try() == Try('value', True)
    assert box.to_validation() == Validation.success('value')


# Generated at 2022-06-14 03:08:59.899134
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    actual = Lazy(lambda: 1).to_lazy()
    expected = Lazy(lambda: 1)

    assert actual == expected

# Generated at 2022-06-14 03:09:04.725535
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    value = 1
    box = Box(value)
    lazy = box.to_lazy()

    assert lazy.is_value()
    assert lazy.get() == value



# Generated at 2022-06-14 03:09:06.017748
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(1)


# Generated at 2022-06-14 03:09:08.183343
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(13).to_lazy() == Lazy(lambda: 13)



# Generated at 2022-06-14 03:09:09.700131
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().map(lambda x: x + 2).value() == 7

# Generated at 2022-06-14 03:09:11.574914
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:09:13.195773
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:10:41.171330
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(lambda x: x * 2)
    assert box.to_lazy().get()(2) == 4


# Generated at 2022-06-14 03:10:43.937496
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 'a') == Box('a').to_lazy()

# Generated at 2022-06-14 03:10:48.214590
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for class Box.
    """
    box = Box(1)
    lazy_val = box.to_lazy()

    assert lazy_val.value() == box.value

# Generated at 2022-06-14 03:11:01.147200
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test to_lazy method of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(Lazy(lambda: '1')).to_lazy() == Lazy(lambda: '1')

# Generated at 2022-06-14 03:11:03.924088
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(2).to_lazy().force() == 2



# Generated at 2022-06-14 03:11:07.886107
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:11:17.467913
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    result = Box(lambda x: x + 1).to_lazy().call(2)

    assert result == 3

# Generated at 2022-06-14 03:11:23.886710
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    value = Try(100, is_success=True)

    actual = Box(value).to_lazy()

    assert isinstance(actual, Lazy)
    assert actual.value() == value



# Generated at 2022-06-14 03:11:29.481302
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # arrange
    value = 100

    # act
    box = Box(value)
    lazy = box.to_lazy()

    # assert
    assert lazy.value() == value

# Generated at 2022-06-14 03:11:43.492854
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    assert Box(3).to_lazy().evaluate() == 3
    assert Box(Lazy(lambda: 3)).to_lazy().evaluate().evaluate() == 3
    assert Box(Try(3, True)).to_lazy().evaluate().is_success == True
    assert Box(Try(3, True)).to_lazy().evaluate().get_value() == 3
    assert Box(Right(3)).to_lazy().evaluate().is_right == True
    assert Box(Right(3)).to_lazy().evaluate().get_value() == 3