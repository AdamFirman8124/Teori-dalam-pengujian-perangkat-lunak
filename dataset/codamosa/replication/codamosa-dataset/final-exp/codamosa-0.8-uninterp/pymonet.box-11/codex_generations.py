

# Generated at 2022-06-14 03:01:37.520421
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert(Lazy(lambda: 1) == Box(1).to_lazy())



# Generated at 2022-06-14 03:01:38.865786
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:01:40.201331
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().force() == 5



# Generated at 2022-06-14 03:01:43.144180
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box('1') != Box(1)
    assert Box(1) != 42
    assert Box('1') != '1'
    


# Generated at 2022-06-14 03:01:45.070139
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    # Test for different types
    assert Box(1) != Box(2)

    # Test for equal Boxes
    assert Box(1) == Box(1)



# Generated at 2022-06-14 03:01:46.746561
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy: Lazy[int] = Box(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold_right(lambda v: v) == 1


# Generated at 2022-06-14 03:01:49.171215
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    test1 = Box(10)
    test2 = Box(10)
    assert test1 == test2


# Generated at 2022-06-14 03:01:51.709952
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    box = Box(1)
    assert isinstance(box.to_lazy(), Lazy)
    assert isinstance(Try(1).to_lazy(), Lazy)

# Generated at 2022-06-14 03:01:57.613736
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(3) == Box(3)
    assert Box('test') == Box('test')
    assert Box(3) != Box([1, 2, 3])
    assert Box('test') != Box({'test': 1})



# Generated at 2022-06-14 03:01:58.941954
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box('test') == 'test'
    assert not Box('test') == 'test1'
    assert Box('test') == Box('test')
    assert not Box('test') == Box('test1')


# Generated at 2022-06-14 03:02:03.509291
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()



# Generated at 2022-06-14 03:02:07.332852
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method Box.to_lazy
    """
    from pymonet.monad_try import Try

    def f():
        return Try('pymonet')

    assert Box(f).to_lazy().f() == Try('pymonet')



# Generated at 2022-06-14 03:02:15.134177
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from pymonet.either import Right
    from pymonet.maybe import Maybe

    value = 'value'

    box = Box(value)

    assert box.to_lazy().map(lambda v: v()) == Lazy(lambda: value)
    assert box.to_maybe().map(lambda v: v) == Maybe.just(value)
    assert box.to_either().map(lambda v: v) == Right(value)
    assert box.to_try().map(lambda v: v) == Try(value, is_success=True)
    assert box.to_validation().map(lambda v: v) == Validation.success(value)



# Generated at 2022-06-14 03:02:17.506115
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:02:20.080838
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()
    assert lazy.get() == 1


# Generated at 2022-06-14 03:02:23.603945
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """

    assert Box(-1).to_lazy().map(lambda i: i + 1).to_box() == Box(0)

# Generated at 2022-06-14 03:02:27.161187
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert str(Box(1).to_lazy()) == 'Lazy[() -> 1]'


# Generated at 2022-06-14 03:02:29.414726
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:02:31.710871
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(3).to_lazy().unwrap() == 3

# Generated at 2022-06-14 03:02:34.551722
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(2).to_lazy().bind(lambda x: x * x) == 4

# Generated at 2022-06-14 03:02:41.893537
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_list import List

    assert isinstance(Box(1).to_lazy().value(), int)
    assert isinstance(Box(1).to_lazy().value(), int)
    assert isinstance(Box([1]).to_lazy().value(), List)
    assert isinstance(Box(Try(1)).to_lazy().value(), Try)



# Generated at 2022-06-14 03:02:49.508407
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy as Lazy
    import pymonet.monad_lazy as MLazy

    t = 'test'
    lazy_box = Box(t).to_lazy()

    assert isinstance(lazy_box, Lazy.Lazy) is True
    assert lazy_box.fold(MLazy.Identity) == t


# Generated at 2022-06-14 03:02:52.458002
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box(23) == Box(23).to_lazy().value()

# Generated at 2022-06-14 03:02:55.888857
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    a = Box(1)
    assert a.to_lazy().fold() == a.value
    assert a.to_lazy().fold() == 1


# Generated at 2022-06-14 03:02:58.227115
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:03:02.022090
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test the to_lazy method of class Box

    :return: nothing
    """
    assert Box('This is a string') == Box('This is a string').to_lazy().force()


# Generated at 2022-06-14 03:03:08.113196
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try

    assert Box(123).to_lazy() == Box(123).to_lazy()
    assert Box(123).to_lazy() != Box(321).to_lazy()
    assert Try(321).to_lazy() != Box(123).to_lazy()

# Generated at 2022-06-14 03:03:15.205699
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy().fold(lambda: 1) == 1
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().to_maybe() == Box(Lazy(lambda: 1)).to_maybe().to_lazy()
    assert Box(1).to_lazy().to_either() == Box(Lazy(lambda: 1)).to_either().to_lazy()


# Generated at 2022-06-14 03:03:16.844969
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    box = Box(42)
    assert box.to_lazy().get() == 42

# Generated at 2022-06-14 03:03:23.862907
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest
    from pymonet.lazy import Lazy
    def test_value(result):
        assert result == 1
    box = Box(1)
    lazy = box.to_lazy()
    assert lazy == Lazy(lambda: 1)
    assert lazy.value == 1
    lazy.apply(test_value)
    assert lazy.value == 1
    lazy.apply(test_value)
    assert lazy.value == 1
    assert lazy.value == 1



# Generated at 2022-06-14 03:03:29.782339
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert (Box(1).to_lazy().get_value() == 1)

# Generated at 2022-06-14 03:03:31.320174
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().fold() == 10

# Generated at 2022-06-14 03:03:33.098995
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box('data')
    assert box.to_lazy().force() == 'data'



# Generated at 2022-06-14 03:03:34.848367
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()
    assert lazy.fold() == 1

# Generated at 2022-06-14 03:03:37.132865
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(4)
    assert box.to_lazy() == Lazy(lambda: 4)

# Generated at 2022-06-14 03:03:40.723917
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:03:44.984772
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(2).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get_value() == 2


# Generated at 2022-06-14 03:03:47.685430
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad import monad
    from pymonet.lazy import Lazy

    # Arrange
    box = Box(monad.identity_function)

    # Act
    lazy = box.to_lazy()

    # Assert
    assert isinstance(lazy, Lazy)



# Generated at 2022-06-14 03:03:52.101933
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def returning_nine():
        return 9

    box = Box(returning_nine)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy._function == returning_nine
    assert lazy.get() == 9



# Generated at 2022-06-14 03:03:53.789199
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Lazy(lambda: 100)
    assert Box(100).to_lazy() == lazy


# Generated at 2022-06-14 03:04:10.235036
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Check some constant values
    box_0 = Box(0).to_lazy()
    assert box_0() == 0

    box_1 = Box(1).to_lazy()
    assert box_1() == 1

    box_2 = Box(2).to_lazy()
    assert box_2() == 2

    box_3 = Box(3).to_lazy()
    assert box_3() == 3

    box_str = Box('str').to_lazy()
    assert box_str() == 'str'

    box_bool = Box(True).to_lazy()
    assert box_bool()

    box_list = Box([1, 2, 3, 4, 5]).to_lazy()
    assert box_list() == [1, 2, 3, 4, 5]

    box_dict = Box

# Generated at 2022-06-14 03:04:11.541614
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().value() == 5

# Generated at 2022-06-14 03:04:19.479682
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # GIVEN: Box with value
    box = Box(18)

    # WHEN: we convert it to Lazy
    actual = box.to_lazy()

    # THEN: we should get the same value
    assert isinstance(actual, Lazy), 'Should get Lazy'
    assert actual.eval() == 18, 'Should get Lazy with same value'
    assert isinstance(actual.eval(), Try), 'Should get Try wrapped value into Lazy'

# Generated at 2022-06-14 03:04:21.391364
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(2)
    assert box.to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:04:23.086939
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:04:28.074802
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:04:29.418893
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test correctness of Box.to_lazy method.

    :returns: None
    :rtype: None
    """
    assert Box(1).to_lazy().force() == 1

# Generated at 2022-06-14 03:04:30.945113
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(True).to_lazy() == Lazy(Box(True).bind).unfold()

# Generated at 2022-06-14 03:04:33.427162
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().unwrap() == 1

# Generated at 2022-06-14 03:04:35.622839
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'value') == Box('value').to_lazy()

# Generated at 2022-06-14 03:04:48.042764
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(lambda x: x**2)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy()(3) == 9

# Generated at 2022-06-14 03:04:57.603324
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.monad_maybe import Maybe

    assert Box(42).to_lazy().get_or_else(0) == 42
    assert Box(Maybe(42)).to_lazy().get_or_else(0) == 42
    assert Box(Try(42)).to_lazy().get_or_else(0) == 42
    assert Box(Try(None, is_success=False)).to_lazy().get_or_else(0) == 0
    assert Box(Try(None, is_success=False)).to_lazy().get_or_else(lambda: 0) == 0



# Generated at 2022-06-14 03:05:01.202752
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def f():
        raise RuntimeError('Error')

    box = Box(Lazy.of(f))
    result = box.to_lazy()
    assert isinstance(result, Lazy)
    assert isinstance(result.force(), Try)



# Generated at 2022-06-14 03:05:02.166235
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().value() == 10



# Generated at 2022-06-14 03:05:03.270249
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:05:04.577190
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:05:07.328345
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    lazy = Box(42).to_lazy()
    assert lazy.is_value() is False
    assert lazy.get_value() == 42

# Generated at 2022-06-14 03:05:12.753668
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def test_number(number):
        return number * 10

    box = Box(10)

    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.fold() == 10
    assert lazy.map(test_number).fold() == 100


# Generated at 2022-06-14 03:05:13.926981
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().force() == 1
    assert Box(1).to_lazy().to_box().value == 1

# Generated at 2022-06-14 03:05:16.277698
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def f(): return 2

    assert Box(2).to_lazy() == Lazy(f)

# Generated at 2022-06-14 03:05:35.780715
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:37.997961
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)



# Generated at 2022-06-14 03:05:39.584241
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(6).to_lazy().get() == 6

# Generated at 2022-06-14 03:05:41.671046
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Testing Box to_lazy method
    """
    from pymonet.monad_try import Try

    try_value = Try(1, True)
    box_value = Box(try_value).to_lazy().value()

    assert box_value == try_value.value

# Generated at 2022-06-14 03:05:43.018786
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:05:43.987676
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().value() == 5


# Generated at 2022-06-14 03:05:45.383557
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(15).to_lazy() == Lazy(lambda: 15)

# Generated at 2022-06-14 03:05:47.309086
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: Box(1).value)



# Generated at 2022-06-14 03:05:49.218388
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    x = Box(1)
    y = x.to_lazy()
    assert y.fold() == 1

# Generated at 2022-06-14 03:05:52.517006
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import Lazy
    from pymonet.test_utils import is_lazy

    result = Box(1).to_lazy()
    expected_result = Lazy(lambda: 1)

    assert result == expected_result
    assert is_lazy(result)



# Generated at 2022-06-14 03:06:14.712662
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():

    assert(callable(Box("test_value").to_lazy().value))
    assert(Box("test_value").to_lazy().value() == "test_value")

# Generated at 2022-06-14 03:06:18.497444
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()
    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 03:06:22.028124
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import unit

    assert Lazy(lambda: 1) == unit(1).to_lazy()


# Generated at 2022-06-14 03:06:31.528434
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    >>> from pymonet.monad_try import Try
    >>> from pymonet.lazy import Lazy
    >>> from pymonet.either import Right
    >>> from pymonet.maybe import Maybe
    >>> from pymonet.validation import Validation
    >>> box = Box(5)
    >>> box
    Box[value=5]
    >>> box.to_lazy()
    Lazy[Function(() -> 5)]
    >>> box.to_maybe()
    Maybe.just[value=5]
    >>> box.to_try()
    Try[value=5, is_success=True]
    >>> box.to_either()
    Right[value=5]
    >>> box.to_validation()
    Validation.success[value=5]
    """
    pass

# Generated at 2022-06-14 03:06:39.775603
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: (1, 'str')) == Box((1, 'str')).to_lazy()
    assert Lazy(lambda: {'str': 1}) == Box({'str': 1}).to_lazy()

    assert Lazy(lambda: [1, 2, 3]) == Box([1, 2, 3]).to_lazy()
    assert Lazy(lambda: set([1, 2, 3])) == Box(set([1, 2, 3])).to_lazy()

# Generated at 2022-06-14 03:06:42.461902
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    @given(integers())
    def test(i):
        assert isinstance(Box(i).to_lazy(), Lazy)

    test()

# Generated at 2022-06-14 03:06:47.657476
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import monad

    assert Box(4).to_lazy() == Lazy(Lazy.ret(4))

    @monad(Box)
    def divide(a, b):
        return a / b

    assert divide(Box(4), Box(2)).to_lazy() == Lazy(Lazy.ret(2))

# Generated at 2022-06-14 03:06:51.096797
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box.to_lazy
    """
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:06:54.586416
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet import Lazy

    box = Box(10)
    assert box.to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:06:57.470635
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    def f(x):
        return x + 1

    box = Box(1)
    assert box.to_lazy().map(f).fold() == 2

# Generated at 2022-06-14 03:07:20.445682
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # Given
    box = Box(10)

    # When
    lazy = box.to_lazy()

    # Then
    assert lazy.value() == 10

# Generated at 2022-06-14 03:07:25.872738
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return 1

    assert Box('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Box(f).to_lazy() == Lazy(f)
    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:07:29.437961
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(lambda x: x + 2).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.fold()(10) == 12

# Generated at 2022-06-14 03:07:30.762612
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Box(1)

# Generated at 2022-06-14 03:07:36.752250
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe

    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.just(5.5).to_lazy() == Lazy(lambda: 5.5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: Maybe.nothing())
    assert Maybe.just(Lazy(lambda: 6)).to_lazy() == Lazy(lambda: Lazy(lambda: 6))
    assert Maybe.just('hello').to_lazy() == Lazy(lambda: 'hello')

# Generated at 2022-06-14 03:07:41.236751
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    val = Box(1).to_lazy()
    assert isinstance(val, Lazy)
    assert val.extract() == 1

    val = Box(Try(1, is_success=True)).to_lazy()
    assert isinstance(val, Lazy)
    assert val.extract() == Try(1, is_success=True)

# Generated at 2022-06-14 03:07:43.852604
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:07:47.493568
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(3)
    lazy = box.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: 3)


# Generated at 2022-06-14 03:07:50.000187
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Box(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value == 1

# Generated at 2022-06-14 03:07:54.108681
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def assert_is_lazy():
        assert Box(10).to_lazy() == Lazy(lambda: 10)

    assert_is_lazy()

# Generated at 2022-06-14 03:08:41.171435
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()
    assert lazy.is_value == True
    assert lazy.get() == 1

# Generated at 2022-06-14 03:08:42.839630
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().map(lambda x: x + 10).value() == 15

# Generated at 2022-06-14 03:08:44.616275
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(5).to_lazy().value() == 5

# Generated at 2022-06-14 03:08:47.741222
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(100)
    assert box.to_lazy() == Lazy(lambda: 100)


# Generated at 2022-06-14 03:08:59.449026
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Test function for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy

    assert Box(Lazy(lambda: 10)).to_lazy().value() == 10
    assert Box(Lazy(_lazy_10)).to_lazy().value() == 10
    assert Box(Lazy(lambda: _lazy_10)).to_lazy().value() == 10
    assert Box(Lazy(_lazy_10)).to_lazy().value() == 10
    assert Box(Lazy(_lazy_10)).to_lazy().value() == 10
    assert Box(Lazy(lambda: _lazy_10)).to_lazy().value() == 10
    assert Box(Lazy(_lazy_10)).to_lazy().value() == 10


#

# Generated at 2022-06-14 03:09:09.628304
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(None).to_lazy() == Lazy(lambda: None)
    assert Box([]).to_lazy() == Lazy(lambda: [])
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Box(1.0).to_lazy() == Lazy(lambda: 1.0)
    assert Box(0.1).to_lazy() == Lazy(lambda: 0.1)
    assert Box("").to_lazy() == Lazy(lambda: "")
    assert Box("1").to_lazy() == Lazy(lambda: "1")

# Generated at 2022-06-14 03:09:11.436695
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return 1

    assert Box(1).to_lazy() == Lazy(f)

# Generated at 2022-06-14 03:09:13.790110
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Box
    """

    box = Box(lambda a: a + 1)
    assert box.to_lazy().eval()(2) == 3

# Generated at 2022-06-14 03:09:15.425161
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(11).to_lazy().fold(lambda x: x) == 11

# Generated at 2022-06-14 03:09:18.750840
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:10:56.780241
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:11:03.598361
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    # define lazy function
    lazy_def_inc_one = lambda a: a + 1
    lazy_def_inc_two = lambda a: a + 2

    # creating Box and Lazy monad
    box_lazy = Box(2).to_lazy()
    lazy = Lazy(lambda: 2)

    # testing creating Lazy monad
    assert box_lazy == Lazy(lambda: 2)
    assert lazy == Lazy(lambda: 2)

    # testing method map
    assert box_lazy.map(lazy_def_inc_one) == Lazy(lambda: 3)

# Generated at 2022-06-14 03:11:08.447386
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # given
    box_value = "value"
    box = Box(box_value)

    # when
    lazy = box.to_lazy()

    # then
    assert lazy.value() == box_value


# Generated at 2022-06-14 03:11:20.631771
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functors.functor import Functor

    assert isinstance(Box(1).to_lazy(), Lazy)
    assert isinstance(Box(1).to_lazy(), Functor)


# Generated at 2022-06-14 03:11:22.687991
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('test').to_lazy().get_value() == 'test'

# Generated at 2022-06-14 03:11:28.810273
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # @given(st.integers())
    def should_change_nothing(value):
        assert Box(value).to_lazy().value() == Box(value).value
    should_change_nothing()

# Generated at 2022-06-14 03:11:30.664862
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # pylint: disable=W0612,W0613
    x = Box(5)

    def f():
        return 5

    assert x.to_lazy() == Lazy(f)

