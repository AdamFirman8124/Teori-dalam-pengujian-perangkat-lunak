

# Generated at 2022-06-14 03:31:31.531165
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:31:37.115944
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False)
    assert Maybe(5, False) != Maybe(8, False)
    assert Maybe(5, False) != Maybe(8, True)
    assert Maybe(5, False) != Maybe(8, False)
    assert Maybe(None, True) == Maybe(None, True)


# Generated at 2022-06-14 03:31:43.088321
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    @Given(st.from_type(Maybe))
    def _(maybe: Maybe):
        monad = maybe.to_lazy()
        assert isinstance(monad.value, type(lambda: None))
        assert monad == maybe.to_lazy()
        assert monad.value() == maybe.value

    _()



# Generated at 2022-06-14 03:31:45.326600
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(None, True) != Maybe(None, True)
    assert Maybe("", False) == Maybe("", False)
    assert Maybe(None, True) == Maybe.nothing()
    assert Maybe("") != Maybe("")


# Generated at 2022-06-14 03:31:47.667355
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().evaluate() == 1
    assert Maybe.nothing().to_lazy().evaluate() is None

# Generated at 2022-06-14 03:31:54.040824
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 3) == Maybe.just(5)
    assert Maybe.nothing().filter(lambda x: x > 3) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x > 7) == Maybe.nothing()


# Generated at 2022-06-14 03:31:57.839421
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.just(4) != Maybe.just(3)
    assert Maybe.just(4) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:02.510170
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(4).filter(lambda x: x % 2 == 0) == Maybe.just(4)
    assert Maybe.just(5).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:32:10.443817
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(None, True)
    assert Maybe(1, False) != Maybe(None, False)
    assert Maybe(1, False) != Maybe(None, True)
    assert Maybe(1, False) != Maybe(None, None)
    assert Maybe(1, False) != 1


# Generated at 2022-06-14 03:32:17.813562
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(2, False) == Maybe(2, False)
    assert Maybe(2, False) != Maybe(2, True)
    assert Maybe(2, False) != Maybe(1, False)
    assert Maybe(2, False) != Maybe(1, True)
    assert Maybe(2, False) != Maybe(2, None)
    assert Maybe(2, False) != Maybe(None, False)
    assert Maybe(2, False) != Maybe(None, True)
    assert Maybe(2, False) != Maybe(None, None)


# Generated at 2022-06-14 03:32:27.162949
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(
        100
    ).filter(lambda value: value > 10) == Maybe.just(
        100
    )

    assert Maybe.just(
        -100
    ).filter(
        lambda value: value > 10
    ) == Maybe.nothing()

    assert Maybe.nothing().filter(
        lambda value: value > 10
    ) == Maybe.nothing()



# Generated at 2022-06-14 03:32:30.283072
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Basic
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(2)


# Generated at 2022-06-14 03:32:40.612784
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Maybe.just(3).to_lazy() == Lazy(lambda: 3)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy().eval() == None
    assert Maybe.nothing().to_lazy().eval(Box(3)).get_value() == 3
    assert Maybe.just(3).to_lazy().eval(Box(4)).get_value() == 3
    assert Maybe.just(3).to_lazy().map(Lazy(lambda x: x * 2)).eval() == 6

# Generated at 2022-06-14 03:32:47.810938
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    just_1 = Maybe.just(1)
    just_2 = Maybe.just(2)
    assert not just_1.__eq__(just_2)

    just_1 = Maybe.just(1)
    just_3 = Maybe.just(1)
    assert just_1.__eq__(just_3)

    nothing_1 = Maybe.nothing()
    nothing_2 = Maybe.nothing()
    assert nothing_1.__eq__(nothing_2)

    assert not just_1.__eq__(nothing_1)
    assert not just_1.__eq__(None)



# Generated at 2022-06-14 03:32:51.198354
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:32:55.077944
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:32:59.093122
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.just(1) == Maybe.just(1))
    assert(Maybe.just(1) != Maybe.just(2))
    assert(Maybe.nothing() == Maybe.nothing())
    assert(Maybe.nothing() != Maybe.just(1))
    assert(Maybe.just(1) != Maybe.nothing())


# Generated at 2022-06-14 03:33:01.794035
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    def test_function(value: Maybe[str]):
        return value.to_lazy().value()

    assert 'abc' == test_function(Maybe.just('abc'))
    assert None is test_function(Maybe.nothing())



# Generated at 2022-06-14 03:33:04.505166
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:33:09.046900
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.nothing() is False
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) == Maybe.just(3) is False
    assert Maybe.nothing() == Maybe.just(2) is False
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:33:14.634795
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:33:17.886602
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_0 = Maybe.just(0)
    maybe_1 = Maybe.just(1)
    maybe_0_copy = Maybe.just(0)

    assert maybe_0 == maybe_0
    assert maybe_0 == maybe_0_copy
    assert not maybe_0 == maybe_1


# Generated at 2022-06-14 03:33:22.922602
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # test for just with truthy filterer
    assert Maybe.just("test").filter(lambda x: x is not None) == Maybe.just("test")
    # test for just with falsey filterer
    assert Maybe.just("test").filter(lambda x: x is None) == Maybe.nothing()
    # test for nothing
    assert Maybe.nothing().filter(lambda x: x is not None) == Maybe.nothing()



# Generated at 2022-06-14 03:33:25.888590
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(0).filter(lambda i: i % 2 == 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda i: i % 2 == 1) == Maybe.just(1)



# Generated at 2022-06-14 03:33:35.720345
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Check that filter works correctly.

    :returns: True when tests are passed, in other case raises error
    :rtype: Boolean
    """
    from pymonet.util import is_even

    result = Maybe.just(5).filter(is_even)
    assert result is Maybe.nothing()

    result = Maybe.just(4).filter(is_even)
    assert result == Maybe.just(4)

    result = Maybe.nothing().filter(is_even)
    assert result is Maybe.nothing()
    print(result)

    return True


# Generated at 2022-06-14 03:33:39.361346
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:33:46.518167
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(4).to_lazy() == Lazy(lambda: 4)
    assert Maybe.just(8).to_lazy().to_lazy() == Lazy(lambda: 8)
    assert Maybe.nothing().to_lazy().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:33:54.192477
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor
    from pymonet.functor.function import apply_function, identity

    assert Maybe.nothing().filter(identity) == Maybe.nothing()
    assert Maybe.just(1).filter(identity) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 2) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe.just(1).filter(apply_function(identity)) == Maybe.just(1)



# Generated at 2022-06-14 03:34:01.522721
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(1)


# Generated at 2022-06-14 03:34:08.378064
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.just('1')
    assert Maybe.just(1).__eq__(0) == NotImplemented


# Generated at 2022-06-14 03:34:16.799239
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:34:20.396869
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert not Maybe.nothing() == Maybe.just(10)


# Generated at 2022-06-14 03:34:23.430706
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(4).to_lazy().call() == 4
    assert Maybe.nothing().to_lazy().call() == None



# Generated at 2022-06-14 03:34:26.930212
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:31.162257
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('a') == Maybe.just('a')
    assert Maybe.nothing() != Maybe.just('b')
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(True) != Maybe.nothing()



# Generated at 2022-06-14 03:34:36.410681
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:34:38.914592
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(2)



# Generated at 2022-06-14 03:34:47.030437
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Test with equal Maybes
    maybe = Maybe.just(42)
    another_maybe = Maybe.just(42)
    assert maybe == another_maybe
    # Test with Maybes with different values
    maybe = Maybe.just(42)
    another_maybe = Maybe.just(21)
    assert maybe != another_maybe
    # Test with empty Maybes
    maybe = Maybe.nothing()
    another_maybe = Maybe.nothing()
    assert maybe == another_maybe
    # Test with not equal Maybes
    maybe = Maybe.nothing()
    another_maybe = Maybe.just(1)
    assert maybe != another_maybe
    maybe = Maybe.just(1)
    another_maybe = Maybe.nothing()
    assert maybe != another_maybe



# Generated at 2022-06-14 03:34:55.046171
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe(None, True) == Maybe.nothing()
    assert Maybe(2, False) != Maybe(1, False)
    assert Maybe(2, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(2, True) != Maybe(1, True)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe(1, False) != Maybe(1, True)

# Unit tests for class methods

# Generated at 2022-06-14 03:35:06.893162
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    add1 = lambda value: value + 1

    # Test 1: empty Maybe
    try:
        assert Maybe.nothing() == Maybe.nothing()
        assert Maybe.nothing() == None
    except Exception as e:
        print('Exception in test 1: ', e)

    # Test 2: not empty Maybe
    try:
        assert Maybe.just(1) == Maybe.just(1)
        assert Maybe.just(1) == 1
    except Exception as e:
        print('Exception in test 2: ', e)

    # Test 3: different maybes
    try:
        assert Maybe.just(1) != Maybe.nothing()
        assert Maybe.just(1) != Maybe.just(2)
    except Exception as e:
        print('Exception in test 3: ', e)

# Generated at 2022-06-14 03:35:24.900103
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_list import List

    # Setup test data
    filter_1: Callable[[int], bool] = lambda x: x % 2 == 0
    filter_2: Callable[[int], bool] = lambda x: x % 3 == 0
    filter_3: Callable[[int], bool] = lambda x: x % 5 == 0
    items: List[int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

    # Perform test

# Generated at 2022-06-14 03:35:30.168056
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    m1 = Maybe.just(1)
    m2 = Maybe.just(2)
    m3 = Maybe.just(1)
    m4 = Maybe.nothing()
    m5 = Maybe.nothing()

    assert m1 == m3
    assert m1 != m2
    assert m4 == m5
    assert m1 != m4

# Generated at 2022-06-14 03:35:35.771813
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_maybe import Maybe

    some_str = Maybe.just('my name')
    assert some_str.filter(lambda value: value == 'my name') == Maybe.just('my name')
    assert some_str.filter(lambda value: False) == Maybe.nothing()
    assert some_str.filter(lambda value: True) == Maybe.just('my name')
    assert Maybe.nothing().filter(lambda value: True) == Maybe.nothing()


# Generated at 2022-06-14 03:35:38.456727
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().get() == 1
    assert Maybe.nothing().to_lazy().get() is None



# Generated at 2022-06-14 03:35:45.815945
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    def runner():
        return 1
    lazy1 = Maybe.just(runner).to_lazy()
    assert isinstance(lazy1, Lazy)
    assert lazy1.value()() == 1
    lazy2 = Maybe.nothing().to_lazy()
    assert isinstance(lazy2, Lazy)
    assert lazy2.value()() is None



# Generated at 2022-06-14 03:35:49.816150
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert not Maybe(1, False) == Maybe(2, False)
    assert Maybe(1, False) != Maybe(2, False)


# Generated at 2022-06-14 03:35:56.340142
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(5)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:36:01.565723
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    value = [5, 5]
    result1 = Maybe.just(value) == Maybe.just(value)
    result2 = Maybe.nothing() == Maybe.nothing()
    result3 = Maybe.just(value) == Maybe.nothing()
    expected1, expected2, expected3 = True, True, False

    assert result1 == expected1
    assert result2 == expected2
    assert result3 == expected3



# Generated at 2022-06-14 03:36:06.834747
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just("test")
    assert maybe.to_lazy() == Lazy(lambda: "test")

    maybe = Maybe.nothing()
    assert maybe.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:36:09.852480
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1) == Maybe.nothing()
    assert Maybe.just(None) == Maybe.just(None) == Maybe.nothing()



# Generated at 2022-06-14 03:36:19.844167
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().perform() == 1
    assert Maybe.nothing().to_lazy().perform() == None


# Generated at 2022-06-14 03:36:26.630675
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) is Maybe.nothing()
    assert Maybe.just(4).filter(lambda x: x % 2 == 0) == Maybe.just(4)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) is Maybe.nothing()



# Generated at 2022-06-14 03:36:35.030895
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_maybe import Maybe

    def one():
        return 1
    assert (isinstance(
        Maybe.just(1).to_lazy(),
        Lazy
    ))
    assert (Maybe.just(1).to_lazy() == Lazy(one))
    assert (isinstance(
        Maybe.nothing().to_lazy(),
        Lazy
    ))
    assert (Maybe.nothing().to_lazy()() == None)


# Generated at 2022-06-14 03:36:36.897813
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(None)

# Generated at 2022-06-14 03:36:40.688424
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:36:44.519163
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(5, False).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:52.287954
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x != 2) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x != 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()

# Generated at 2022-06-14 03:36:55.458336
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:37:03.320811
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def func_with_side_effects(x):
        print("func_with_side_effects", x)
        return x

    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    maybe = Maybe.just(4).to_lazy()

    assert maybe == Lazy(lambda: 4)
    assert maybe.open() == 4
    assert maybe.map(func_with_side_effects).open() == 4


# Generated at 2022-06-14 03:37:08.502328
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 3) == Maybe.just(5), 'Maybe filter method test failed'
    assert Maybe.just(5).filter(lambda x: x < 3) == Maybe.nothing(), 'Maybe filter method test failed'
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing(), 'Maybe filter method test failed'


# Generated at 2022-06-14 03:37:22.562376
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # maybe = Maybe.just(1)
    # assert maybe.to_lazy().get() == 1
    # maybe = Maybe.nothing()
    # assert maybe.to_lazy().get() is None
    pass



# Generated at 2022-06-14 03:37:29.142097
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Given
    test_value = 1
    maybe = Maybe.just(test_value)

    # When
    result = maybe.filter(lambda x: x > 0)
    # Then
    assert result == Maybe.just(test_value)

    # When
    result = maybe.filter(lambda x: x < 0)
    # Then
    assert result == Maybe.nothing()

    # When
    maybe = Maybe.nothing()
    result = maybe.filter(lambda x: x < 0)
    # Then
    assert result == Maybe.nothing()

# Generated at 2022-06-14 03:37:38.654507
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.box import Box

    assert Maybe.just(3).filter(lambda x: x == 3) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x == 4) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 3) == Maybe.nothing()

    assert Maybe.just(Box(3)).filter(lambda x: x.unbox() == 3) == Maybe.just(Box(3))
    assert Maybe.just(Box(3)).filter(lambda x: x.unbox() == 4) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x.unbox() == 3) == Maybe.nothing()

    assert Maybe.just(Box(3)).filter(lambda x: x.unbox() == 3).unbox() == 3

# Unit test

# Generated at 2022-06-14 03:37:44.991988
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # GIVEN
    maybe = Maybe.just(5)
    def filterer(value):
        return value > 2
    empty_maybe = Maybe.nothing()

    # WHEN
    result = maybe.filter(filterer)
    empty_result = empty_maybe.filter(filterer)

    # THEN
    assert result.is_nothing is False
    assert empty_result.is_nothing is True


# Generated at 2022-06-14 03:37:50.430331
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    value = {
        'a': None,
        'b': 'hello'
    }

    def filterer(x):
        return x is not None and len(x) > 0

    assert Maybe.just(value['a']).filter(filterer) == Maybe.nothing()
    assert Maybe.just(value['b']).filter(filterer) == Maybe.just(value['b'])
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:37:53.559137
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x > 0) == Maybe(1, False)
    assert Maybe(1, False).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(
        lambda x: x > 0) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)



# Generated at 2022-06-14 03:37:56.778400
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().get_value() == 1
    assert Maybe.nothing().to_lazy().get_value() is None



# Generated at 2022-06-14 03:38:02.708307
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    maybe = Maybe(Box(1), False)
    lazy = maybe.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == Box(1)
    assert maybe.to_lazy().value() == maybe.to_box()


# Generated at 2022-06-14 03:38:14.702126
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.either import Left
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from pymonet.maybe import Maybe

    assert Maybe.just(1).filter(lambda i: i % 2 == 0) == Maybe.nothing()

    assert Maybe.just(2).filter(lambda i: i % 2 == 0) == Maybe.just(2)

    assert Maybe.nothing().filter(lambda i: i % 2 == 0) == Maybe.nothing()

    assert Maybe.just(2).filter(lambda i: i % 2 == 0).to_either() == Left(None)

    assert Maybe.just(2).filter(lambda i: i % 2 == 0).to_box() == Box(2)

# Generated at 2022-06-14 03:38:19.061252
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe
    """
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy().value() is None
    assert Maybe.just(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:38:32.609529
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(1)
    assert maybe.filter(lambda x: x < 2) == Maybe.just(1)
    assert maybe.filter(lambda x: x < 0) == Maybe.nothing()


# Generated at 2022-06-14 03:38:38.046619
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(
        lambda value: value > 0
    ) == Maybe.just(1)
    assert Maybe.just(1).filter(
        lambda value: value < 0
    ) == Maybe.nothing()
    assert Maybe.nothing().filter(
        lambda value: value > 0
    ) == Maybe.nothing()



# Generated at 2022-06-14 03:38:49.685670
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe.
    """
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    x = Maybe.just(2)
    y = Maybe.just(3)
    z = Maybe.nothing()

    assert x.filter(lambda x: x % 2 == 0) == x
    assert x.filter(lambda x: x % 2 == 1) == Lazy(lambda: None)
    assert y.filter(lambda x: x % 2 == 0) == Lazy(lambda: None)
    assert y.filter(lambda x: x % 2 == 1) == y

# Generated at 2022-06-14 03:38:54.226495
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)
    assert Maybe(None, True).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:38:58.697091
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just("a").filter(lambda _: True) == Maybe.just("a")
    assert Maybe.just("a").filter(lambda _: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda _: False) == Maybe.nothing()

# Generated at 2022-06-14 03:39:04.505289
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test for Maybe to Lazy converter.

    :returns: None
    :rtype: None
    """
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Maybe.just(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:13.866848
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Create Maybe with None value
    maybe_no_value = Maybe.nothing()

    # Create Maybe with some value
    maybe_value = Maybe.just(5)

    # Create Maybe with some value
    maybe_value1 = Maybe.just(None)

    # Check when value is None
    assert maybe_no_value.filter(lambda x: x + 1 > 10) == maybe_no_value
    assert maybe_no_value.filter(lambda x: x + 1 < 10) == maybe_no_value

    # Check when value is not None
    assert maybe_value.filter(lambda x: x + 1 > 10) == maybe_value
    assert maybe_value.filter(lambda x: x + 1 < 10) == maybe_no_value

    # Check when value is None

# Generated at 2022-06-14 03:39:20.601266
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(True).filter(lambda x: x).value == True
    assert Maybe.just(True).filter(lambda x: not x).is_nothing == True

    assert Maybe.just(False).filter(lambda x: x).is_nothing == True
    assert Maybe.just(False).filter(lambda x: not x).value == False

    assert Maybe.nothing().filter(lambda x: True).is_nothing == True
    assert Maybe.nothing().filter(lambda x: False).is_nothing == True

# Generated at 2022-06-14 03:39:25.024960
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet import Just, Nothing
    from pymonet.functions import identity

    assert Just(1).filter(lambda a: a % 2 == 0) == Nothing
    assert Just(2).filter(lambda a: a % 2 == 0) == Just(2)
    assert Nothing.filter(identity) == Nothing


# Generated at 2022-06-14 03:39:38.130496
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.monad_either import Left, Right

    assert Maybe(2, True).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe(1, True).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe(2, True).filter(lambda x: x > 1).to_try().is_success == True
    assert Maybe(2, True).filter(lambda x: x > 1).to_try().value == Try(None, True).value
    assert Maybe(1, True).filter(lambda x: x > 1).to_try().is_success == True

# Generated at 2022-06-14 03:40:04.568611
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: x > 2) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x < 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 2) == Maybe.nothing()


# Generated at 2022-06-14 03:40:11.125497
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test filter method of Maybe.

    :returns: None when succeed
    :rtype: None
    """
    def bigger_than_five(num):
        return num > 5

    assert Maybe.just(6).filter(bigger_than_five).get_or_else(None) == 6
    assert Maybe.nothing().filter(bigger_than_five).get_or_else(None) is None
    assert Maybe.just(1).filter(bigger_than_five).get_or_else(None) is None



# Generated at 2022-06-14 03:40:17.597362
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.

    :returns: Nothing
    :rtype: None
    """

    from pymonet.no_exceptions import no_exceptions

    with no_exceptions():
        assert Maybe.just(5).to_lazy().value() == 5
        assert Maybe.nothing().to_lazy().value() is None


# Generated at 2022-06-14 03:40:19.928448
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # returns Lazy(None) when Maybe is empty
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    # returns Lazy(1) when Maybe has value 1
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:40:25.391878
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:40:30.915337
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    m1 = Maybe.just(0)
    m2 = m1.filter(lambda i: i % 2 == 0)
    assert m2 == Maybe.just(0)
    m3 = Maybe.just(1)
    m4 = m3.filter(lambda i: i % 2 == 0)
    assert m4 == Maybe.nothing()
    m5 = Maybe.nothing()
    m6 = m5.filter(lambda i: i % 2 == 0)
    assert m6 == Maybe.nothing()


# Generated at 2022-06-14 03:40:36.527464
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe(1, False).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe(1, True).filter(lambda x: x == 2) == Maybe.nothing()



# Generated at 2022-06-14 03:40:42.437404
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: x) is Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x > 3) is Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x > 3) is Maybe.just(5)


# Generated at 2022-06-14 03:40:46.754944
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    import pytest

    # create Maybe with some value
    maybe = Maybe.just(1)
    # transform Maybe to Lazy monad
    lazy = maybe.to_lazy()

    # expected and actual results must be equal
    assert lazy.get == 1

# Generated at 2022-06-14 03:40:52.453380
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x > 1) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x < 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 1) == Maybe.nothing()

