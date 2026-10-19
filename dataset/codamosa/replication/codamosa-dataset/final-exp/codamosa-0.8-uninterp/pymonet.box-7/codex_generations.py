

# Generated at 2022-06-14 03:01:32.765619
# Unit test for method __eq__ of class Box
def test_Box___eq__():  # pragma: no cover
    assert Box(1) == Box(1)
    assert not Box(1) == Box(2)
    assert not Box(1) == Box('1')
    assert Box('A') == Box('A')


# Generated at 2022-06-14 03:01:41.166259
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(1) != 2
    assert 2 != Box(2)
    assert Box("4") == Box("4")
    assert Box("4") != Box("2")
    assert Box("4") != 4
    assert 4 != Box(4)
    assert Box(1.1) == Box(1.1)
    assert Box(1.1) != Box(2.2)
    assert Box(1.1) != 2.2
    assert 2.2 != Box(2.2)


# Generated at 2022-06-14 03:01:42.365026
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert not Box(1) == Box(2)
    assert Box(1) != Box(2)
    assert not Box(1) != Box(1)

# Generated at 2022-06-14 03:01:44.101915
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert (Box(1) == Box(1)) == True
    assert (Box(1) == Box(2)) == False



# Generated at 2022-06-14 03:01:47.495054
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    box = Box('aaa')
    other_box = Box('aaa')
    failed_box = Box('bbb')
    failed_box_type = 'bbb'

    assert box == other_box
    assert box != failed_box
    assert box != failed_box_type


# Generated at 2022-06-14 03:01:52.206695
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('123') == Box('123')
    assert Box('a') != Box(1)
    assert Box(1) != Box('1')
    assert Box(1) != Box(object)
    assert Box(1) != 1



# Generated at 2022-06-14 03:01:55.356370
# Unit test for method __eq__ of class Box
def test_Box___eq__():
    assert Box(1) == Box(1)
    assert Box('1') == Box('1')
    assert Box([1, 2, 3]) == Box([1, 2, 3])
    assert not Box(1) == Box(2)

# Generated at 2022-06-14 03:02:00.549452
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:02:02.817782
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(10).to_lazy().value() == 10

# Generated at 2022-06-14 03:02:04.198165
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(5).to_lazy().fold() == 5

# Generated at 2022-06-14 03:02:09.814970
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    _lazy = Box(3).to_lazy()

    assert isinstance(_lazy, Lazy)

    assert _lazy.value() == 3

    assert _lazy.__str__() == 'Lazy[value=<function <lambda> at {}>]'.format(_lazy.value)



# Generated at 2022-06-14 03:02:10.526354
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('test').to_lazy().fold() == 'test'

# Generated at 2022-06-14 03:02:12.280636
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:02:13.647110
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(True).to_lazy().get()


# Generated at 2022-06-14 03:02:16.800207
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box.
    """

    import pytest

    box = Box(2)

    assert box.to_lazy().eval() == 2

# Generated at 2022-06-14 03:02:18.233834
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('foo').to_lazy() == Lazy(lambda: 'foo')

# Generated at 2022-06-14 03:02:24.971265
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """

    # Test with simple string
    value = "Hello"
    expected_result = "Hello"
    result = Box(value).to_lazy().eval()
    assert expected_result == result

    # Test with simple integer
    value = 23
    expected_result = 23
    result = Box(value).to_lazy().eval()
    assert expected_result == result

    # Test with simple float
    value = 2.3
    expected_result = 2.3
    result = Box(value).to_lazy().eval()
    assert expected_result == result

    # Test with simple tuple
    value = (1, 2, 3)
    expected_result = (1, 2, 3)
    result = Box(value).to_lazy().eval()

# Generated at 2022-06-14 03:02:31.134139
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test for method to_lazy of class Box
    """
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().fold(lambda: 0) == 1


# Generated at 2022-06-14 03:02:34.605658
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:02:44.365360
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Check that Box.to_lazy correctly convert Box into Lazy.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert(Box(1).to_lazy() == Lazy(lambda: 1))
    assert(Box(1).to_lazy().has_value)
    assert(Box(1).to_lazy().get_value() == 1)
    assert(Box(1).to_lazy().map(lambda x: x + 1).get_value() == 2)
    assert(Box(1).to_lazy().bind(lambda x: Lazy(lambda: x + x)).get_value() == 2)

# Generated at 2022-06-14 03:02:48.362606
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test Box with another Monads (unit test)
    """

    assert Box(1).to_lazy().get() == 1

# Generated at 2022-06-14 03:02:50.242487
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:02:53.179009
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pytest

    with pytest.raises(AttributeError):
        Box(3).to_lazy()


# Generated at 2022-06-14 03:02:59.163967
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.lazy import Lazy
    from pymonet.lazy_functional import LazyFunctional

    assert Lazy(1) == Box(1).to_lazy()
    assert Lazy(2) == Box(Lazy(2)).to_lazy()
    assert LazyFunctional(lambda: 1) == Box(LazyFunctional(lambda: 1)).to_lazy()

# Generated at 2022-06-14 03:03:00.942357
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('foo').to_lazy() == Lazy(lambda: 'foo')

# Generated at 2022-06-14 03:03:10.005339
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_list import List
    from pymonet.monad_try import Try

    # When
    result = Box(3).to_lazy()
    list_result = List([1, 2, 3, 4]).to_lazy()
    try_result = Try(3).to_lazy()

    # Then
    assert result.value() == 3
    assert list_result.value() == List([1, 2, 3, 4])
    assert try_result.value() == Try(3, is_success=True)

# Generated at 2022-06-14 03:03:13.296636
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:03:15.954373
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:03:24.765961
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test function to lazy transformation.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy1 = Box(17).to_lazy()
    lazy2 = Box(17).to_lazy().to_lazy()
    assert lazy1 == lazy2
    assert lazy1.fold() == 17
    assert lazy1.map(lambda x: x * 2).fold() == 34
    assert lazy1.flat_map(lambda x: lazy2).fold() == 17
    assert lazy1.ap(Lazy(lambda: lambda x: x * 2)).fold() == 34
    assert lazy1.to_try() == Try(17, is_success=True)
    assert lazy1.to_maybe().is_just()



# Generated at 2022-06-14 03:03:26.986665
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert str(Box(lambda x: x + 1).to_lazy()) == 'Lazy[value=<function Box.__init__.<locals>.<lambda> at 0x7f4169c4ff28>]'


# Generated at 2022-06-14 03:03:31.498295
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:03:35.253061
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Testing Box.to_lazy method
    """

    assert Box(123).to_lazy().force() == 123
    assert Box('abc').to_lazy().force() == 'abc'
    assert Box(True).to_lazy().force() == True


# Generated at 2022-06-14 03:03:38.046267
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    from pymonet.monad_either import Failure

    assert Box(1).to_lazy().fold_right(lambda x: Failure(x)) == 1



# Generated at 2022-06-14 03:03:43.150228
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Maybe.just(10).to_lazy().fold(lambda: -1) == 10
    assert Maybe.nothing().to_lazy().fold(lambda: -1) == -1
    assert Maybe.just(10).map(lambda x: x + 10).to_lazy().fold(lambda: -1) == 20

    assert Maybe.just(10).to_lazy().bind(lambda x: Maybe.just(x + 10)).fold(lambda: -1) == 20
    assert Maybe.just(10).to_lazy().bind(lambda x: Maybe.nothing()).fold(lambda: -1) == -1

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(10).to_lazy

# Generated at 2022-06-14 03:03:45.859182
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).bind(lambda x: x + 1).to_lazy() == Box(1).to_lazy().map(lambda x: x + 1)


# Generated at 2022-06-14 03:03:54.045214
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe

    assert Box(42).to_lazy() == Lazy(lambda: 42)
    assert \
        Maybe.just([1, 2, 3]).to_maybe() \
        .bind(lambda lst: Maybe.just(lst + [4])) \
        .bind(lambda lst: Maybe.just(lst + [5])) \
        .to_lazy() \
        == \
        Lazy(lambda: [1, 2, 3]) \
        .map(lambda lst: lst + [4]) \
        .map(lambda lst: lst + [5])

# Generated at 2022-06-14 03:03:59.484231
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    test_Box_to_lazy(): Tests transforming Box into Lazy

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.monad import assert_equals

    f = lambda: 'something'
    result = Box('something').to_lazy()

    assert_equals(result, Lazy(f))


# Generated at 2022-06-14 03:04:01.448292
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 42) == Box(42).to_lazy()


# Generated at 2022-06-14 03:04:06.650154
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Lazy(lambda: 1) == Box(1).to_lazy()
    assert Lazy(lambda: [2, 3]) == Box([2, 3]).to_lazy()


# Generated at 2022-06-14 03:04:15.218493
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1).to_lazy().value() == 1

    assert Box(Try(1, True)).to_lazy() == Lazy(lambda: Try(1, True))
    assert Box(Try(1, True)).to_lazy().value() == Try(1, True)

    assert Box(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: Lazy(lambda: 1))
    assert Box(Lazy(lambda: 1)).to_lazy().value() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:04:19.619677
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box('pymonet').to_lazy().fold() == 'pymonet'


# Generated at 2022-06-14 03:04:22.320333
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()
    assert 1 == lazy.call()

# Generated at 2022-06-14 03:04:25.826123
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    boxed_value = Box(100500)
    lazy_box = boxed_value.to_lazy()
    assert lazy_box.value() == 100500

# Generated at 2022-06-14 03:04:30.185040
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try

    box = Box('123')
    assert box.to_lazy().evaluate() == '123'



# Generated at 2022-06-14 03:04:31.684419
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:04:33.721898
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().force() == 1

# Generated at 2022-06-14 03:04:37.512746
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:04:39.528381
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()

    assert lazy.get() == 1

# Generated at 2022-06-14 03:04:44.077514
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box('a').to_lazy() == Lazy(lambda: 'a')
    assert Box(1.2).to_lazy() == Lazy(lambda: 1.2)
    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:04:48.465105
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try

    box = Box(Try(100))
    assert box.to_lazy().get() == Try(100)

# Generated at 2022-06-14 03:04:54.395492
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of class Box
    """
    assert Box('foo').to_lazy().fold(lambda: '') == 'foo'

# Generated at 2022-06-14 03:04:58.022058
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Lazy(lambda: 1) == Box(1).to_lazy()

# Generated at 2022-06-14 03:05:00.197346
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    box = Box(1)
    assert box.to_lazy() == Lazy(lambda: 1)


# Unit tests for method ap of class Box

# Generated at 2022-06-14 03:05:09.402539
# Unit test for method to_lazy of class Box
def test_Box_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.lazy_sequence import Cons
    from pymonet.lazy_sequence import Nil

    assert Box(None).to_lazy() == Lazy(lambda: None)
    assert Box(True).to_lazy() == Lazy(lambda: True)
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(1.1).to_lazy() == Lazy(lambda: 1.1)
    assert Box('a').to_lazy() == Lazy(lambda: 'a')
    assert Box([]).to_lazy() == Lazy(lambda: [])
    assert Box([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
   

# Generated at 2022-06-14 03:05:12.109709
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:05:14.100550
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert (Box(1).to_lazy() == Lazy(lambda: 1))

# Generated at 2022-06-14 03:05:17.089289
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try

    monad = Box("hello world").to_lazy()

    assert monad.fold() == "hello world"

# Unit tests for method to_validation of class Box

# Generated at 2022-06-14 03:05:23.228719
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Box(0).to_lazy() == Lazy(lambda: 0)
    assert Box("t").to_lazy() == Lazy(lambda: "t")
    assert Box(Try(0)).to_lazy() == Lazy(lambda: Try(0))
    assert Box(Maybe.just(0)).to_lazy() == Lazy(lambda: Maybe.just(0))
    assert Box(Validation.success(0)).to_lazy() == Lazy(lambda: Validation.success(0))

# Generated at 2022-06-14 03:05:26.469105
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:05:27.831004
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().evaluate() == 1


# Generated at 2022-06-14 03:05:36.631633
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy
    from pymonet.lazy import Lazy, LazyFunction

    def test_Lazy_factory(value_func: LazyFunction) -> Lazy[int]:
        return Lazy(value_func)

    assert test_Lazy_factory(lambda: Box(1).value) == pymonet.lazy.Lazy(lambda: 1)

# Generated at 2022-06-14 03:05:39.718417
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try

    assert Box(True).to_lazy().map(lambda x: x()).to_try() == Try(True, is_success=True)

# Generated at 2022-06-14 03:05:47.544469
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(1).to_lazy() == Lazy.unit(1)
    assert Box('str').to_lazy() == Lazy.unit('str')
    assert Box([1, 2, 3]).to_lazy() == Lazy.unit([1, 2, 3])
    assert Box((1, 2, 3)).to_lazy() == Lazy.unit((1, 2, 3))
    assert Box({'a': 1, 'b': 2}).to_lazy() == Lazy.unit({'a': 1, 'b': 2})
    assert Box(Try(1)).to_lazy() == Lazy.unit(Try(1))

# Generated at 2022-06-14 03:05:52.318898
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Test method to_lazy() of class Box.
    """
    from pymonet.lazy import Lazy
    from pymonet import _

    box = Box(1)
    assert isinstance(box.to_lazy(), Lazy)
    assert box.to_lazy().map(lambda value: value + 1).value() == 2


# Generated at 2022-06-14 03:05:54.655448
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:06:00.898745
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy_box = Box(5).to_lazy()
    assert isinstance(lazy_box, Lazy)
    assert isinstance(lazy_box.func, Callable)
    assert lazy_box.is_folded is False
    assert lazy_box.func() == 5
    assert lazy_box.is_folded is True

    try_box = Box(6).to_try()
    assert Try(5, is_success=True) == Try(5, is_success=True)
    assert not Try(6, is_success=False) == Try(5, is_success=True)
    assert Try(6, is_success=False) != 5

    lazy_box_with_side_effect_function = lazy

# Generated at 2022-06-14 03:06:02.453598
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:06:05.376527
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(3)
    lazy = box.to_lazy()

    assert type(lazy) == type(box.to_lazy())
    assert lazy.force() == 3

# Generated at 2022-06-14 03:06:11.795094
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    # Given
    value = 'test'

    # When
    result = Box(value).to_lazy()

    # Then
    assert isinstance(result, Lazy)
    assert result == Lazy(lambda: value)

# Generated at 2022-06-14 03:06:16.830092
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    import pymonet.lazy as lazy_monad

    def test_function():
        return 'test_function_value'

    test_lazy: lazy_monad.Lazy[Callable[[], str]] = Box(test_function).to_lazy()

    assert test_lazy.fold(lambda: 'failure') == 'test_function_value'

# Generated at 2022-06-14 03:06:32.645115
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for Box to_lazy method.
    
    :return: None
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try



    # Should transform Box into not folded lazy with function returning stored value
    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: Lazy(lambda: 1))
    assert Box(Try(1, is_success=True)).to_lazy() == Lazy(lambda: Try(1, is_success=True))

# Generated at 2022-06-14 03:06:35.723032
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    value = 1
    box = Box(value)
    lazy_value = box.to_lazy()
    assert lazy_value == Lazy(lambda: value)


# Generated at 2022-06-14 03:06:41.214289
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    box = Box(1)
    lazy = box.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.equals(lazy)
    assert not lazy.is_folded
    assert lazy.value() == 1


# Generated at 2022-06-14 03:06:44.755810
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.test.test_lazy import compare_lazy

    compare_lazy(Box('test').to_lazy(), Lazy(lambda: 'test'))

# Generated at 2022-06-14 03:06:47.521266
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy = Lazy.unit(lambda: 5)
    box = Box(5)

    assert box.to_lazy() == lazy

# Generated at 2022-06-14 03:06:50.633904
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Box[int](1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:53.281477
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert lazy(lambda: 10) == Box(10).to_lazy().force()

# Generated at 2022-06-14 03:06:55.601931
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:06:59.931546
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Box(1).to_lazy() == Lazy(lambda: 1)
    assert Box(Try(10)).to_lazy() == Lazy(lambda: Try(10))

# Generated at 2022-06-14 03:07:05.323891
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box("a").to_lazy() == Lazy(lambda: "a")
    assert Box(Try(10, is_success=True)).to_lazy() == Lazy(lambda: Try(10, is_success=True))
    assert Box(Validation.success(10)).to_lazy() == Lazy(lambda: Validation.success(10))



# Generated at 2022-06-14 03:07:22.863558
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    x = Box(42)

    assert x.to_lazy().fold(lambda: 0)() == 42

# Generated at 2022-06-14 03:07:26.695679
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    # Given
    value = Lazy(lambda: 1)

    # When
    box = Box(value)

    # Then
    assert box.to_lazy() == box.value



# Generated at 2022-06-14 03:07:29.816347
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    val = 'Some value'

    assert Box(val).to_lazy() == Lazy(lambda: val)



# Generated at 2022-06-14 03:07:32.199468
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box("expected_value")
    lazy = box.to_lazy()
    result = lazy.fold(lambda: "unexpected_value")

    assert result == "expected_value"

# Generated at 2022-06-14 03:07:42.749938
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """Unit test for method to_lazy of class Box"""
    from pymonet.lazy import Lazy

    # Test for Lazy with returning value function.
    assert Box(1).to_lazy().map(lambda x: x + 1).value() == 2
    # Test for Lazy with returning not Box value
    assert Box(1).to_lazy().value() == 1
    # Test for Lazy with returning Box value
    assert Box(Box(1)).to_lazy().value() == Box(1)
    # Test for Lazy with returning function and folding function
    assert Box(lambda x: x + 1).to_lazy().map(lambda x: x(2)).value() == 3
    # Test for Lazy with returning function and folding function with not Box value

# Generated at 2022-06-14 03:07:52.536845
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.either import Right
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Box(10).to_lazy() == Lazy(lambda: 10)
    assert Box(10).to_maybe() == Maybe.just(10)
    assert Box(10).to_either() == Right(10)
    assert Box(10).to_try() == Try(10, is_success=True)
    assert Box(10).to_validation() == Validation.success(10)

# Generated at 2022-06-14 03:07:54.762370
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'value') == Box('value').to_lazy()

# Generated at 2022-06-14 03:07:59.848684
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.identity import Identity

    result = Box(Identity(Lazy(lambda: 'value'))).to_lazy()
    assert isinstance(result, Lazy)
    assert result() == 'value'



# Generated at 2022-06-14 03:08:02.937877
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():    # pragma: no cover
    """
    Unit test for method to_lazy of class Box.
    """
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy.unit(1)



# Generated at 2022-06-14 03:08:07.786860
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Box(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:08:45.714354
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    # GIVEN
    box = Box(1)

    # WHEN
    actual = box.to_lazy()

    # THEN
    assert actual.value() == 1



# Generated at 2022-06-14 03:08:48.491708
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    """
    Unit test for method to_lazy of Box

    :return: None
    """
    assert Box(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 03:08:51.262735
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.either import Left

    assert Box(10).to_lazy() == Left(10)

# Generated at 2022-06-14 03:08:57.691578
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    input_value = 'Test'
    expected_value = 'Test'
    # Init box monad
    box = Box(input_value)
    # Call to_lazy method of box monad
    lazy_monad = box.to_lazy()
    # Call get_value method of lazy monad
    result = lazy_monad.get_value()
    # Check expected_result and result are equals
    assert (expected_value == result)

# Generated at 2022-06-14 03:08:59.944994
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:09:02.942254
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:09:04.639300
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy().value() == 42


# Generated at 2022-06-14 03:09:05.928555
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    assert Box(5).to_lazy().value() == 5

# Generated at 2022-06-14 03:09:08.769345
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    value = 43
    assert Box(value).to_lazy().is_value()
    assert not Box(value).to_lazy().is_error()
    assert Box(value).to_lazy().value() == value



# Generated at 2022-06-14 03:09:11.274501
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(lambda x: x + 1).to_lazy().fold(lambda: 2)() == 3

# Generated at 2022-06-14 03:10:32.552404
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():  # pragma: no cover
    tests = [
        (1, Lazy(lambda: 1))
    ]

    for value, expected in tests:
        actual = Box(value).to_lazy()
        assert expected == actual, "Expected={}, Actual={}".format(expected, actual)


# Generated at 2022-06-14 03:10:34.579332
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy
    assert Box(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:10:35.856430
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(12).to_lazy() == Lazy(lambda: 12)

# Generated at 2022-06-14 03:10:37.911327
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    assert Box(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:10:43.145222
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box('foo')

    assert box.to_lazy().__eq__(box.to_lazy())
    assert box.to_lazy().force().__eq__(box.value)

# Generated at 2022-06-14 03:10:45.255054
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().unfold() == 1

# Generated at 2022-06-14 03:10:48.247155
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(42).to_lazy() == Lazy(lambda: 42)



# Generated at 2022-06-14 03:11:04.315591
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    from pymonet.lazy import Lazy

    def f(x):  # pragma: no cover
        print('This is example of lazy evaluation')
        return x

    lazy = Box(f).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_folded is False
    assert lazy.value() is f
    assert lazy.is_folded is True

# Generated at 2022-06-14 03:11:07.549770
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    assert Box(1).to_lazy().evaluate() == 1

# Generated at 2022-06-14 03:11:11.610753
# Unit test for method to_lazy of class Box
def test_Box_to_lazy():
    box = Box(1)
    lazy = box.to_lazy()

    assert callable(lazy.value)
    assert lazy.value() == 1

# Unit tests for method box