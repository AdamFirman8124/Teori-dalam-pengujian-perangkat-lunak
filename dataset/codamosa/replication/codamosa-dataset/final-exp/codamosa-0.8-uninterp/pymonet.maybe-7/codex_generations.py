

# Generated at 2022-06-14 03:31:33.677468
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:31:41.809836
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(15, False) == Maybe(15, False)
    assert Maybe(15, False) != Maybe(15, True)
    assert Maybe(15, False) != Maybe(16, False)
    assert Maybe(15, False) != Maybe(16, True)
    assert Maybe(15, True) == Maybe(15, True)
    assert Maybe(15, True) != Maybe(16, True)
    assert Maybe(15, True) != Maybe(15, False)


# Generated at 2022-06-14 03:31:52.003957
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('abc') == Maybe.just('abc')
    assert Maybe.just('abc') != Maybe.just('aaa')
    assert Maybe.just('abc') != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just([1, 2]) == Maybe.just([1, 2])
    assert Maybe.just

# Generated at 2022-06-14 03:31:55.783715
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)


# Generated at 2022-06-14 03:32:01.163454
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:32:05.332684
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value % 2 == 0

    assert Maybe.just(1).filter(filterer) == Maybe.nothing()
    assert Maybe.just(2).filter(filterer) == Maybe.just(2)
    assert Maybe.just(0).filter(filterer) == Maybe.just(0)


# Generated at 2022-06-14 03:32:08.752564
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:32:13.172701
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Asserts that Maybe.just(2) == Maybe.just(2) is True
    assert Maybe.just(2) == Maybe.just(2)
    # Asserts that Maybe.just(2) == Maybe.nothing() is False
    assert Maybe.just(2) != Maybe.nothing()
    # Asserts that Maybe.nothing() == Maybe.nothing() is True
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:25.161134
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Case 1: Maybe is empty
    # Test that empty Maybe will return empty Maybe
    # when filterer returns false
    def test_case1_1():
        assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()

    # Test that empty Maybe will return empty Maybe
    # when filterer returns true
    def test_case1_2():
        assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()

    # Case 2: Maybe is not empty
    # Test that not empty Maybe will return empty Maybe
    # when filterer returns false
    def test_case2_1():
        assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()

    # Test that not empty Maybe will return copy of itself
    # when filterer returns true

# Generated at 2022-06-14 03:32:31.995280
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) is not Maybe.just(1)

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) is not Maybe.just(2)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() is not Maybe.nothing()

    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.nothing() is not Maybe.just(None)

    assert Maybe.just(1) != None
    assert Maybe.just(1) is not None

    assert Maybe.nothing() != None
    assert Maybe.nothing() is not None



# Generated at 2022-06-14 03:32:37.593516
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().evaluate() == 1
    assert Maybe.nothing().to_lazy().evaluate() is None

# Generated at 2022-06-14 03:32:42.888659
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert not Maybe.just(1) == Maybe.just(2)
    assert not Maybe.just(1) == Maybe.nothing()
    assert not Maybe.nothing() == Maybe.just(1)


# Generated at 2022-06-14 03:32:46.373179
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert(Maybe.just(1) == Maybe.just(1))
    assert(Maybe.just(1) != Maybe.just(2))

    assert(Maybe.nothing() == Maybe.nothing())
    assert(Maybe.just(1) != Maybe.nothing())


# Generated at 2022-06-14 03:32:49.396309
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().force() == 1
    assert Maybe.nothing().to_lazy().force() is None


# Generated at 2022-06-14 03:32:54.318976
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert (Maybe.just(2) == Maybe.just(3)) == False
    assert Maybe.nothing() == Maybe.nothing()
    assert (Maybe.nothing() == Maybe.just(2)) == False
    assert (Maybe.just(2) == Maybe.nothing()) == False



# Generated at 2022-06-14 03:32:57.584519
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()

# Generated at 2022-06-14 03:33:01.613328
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just(10) == Maybe.just(10.0)
    assert Maybe.just(10) != Maybe.just(11)
    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(10)


# Generated at 2022-06-14 03:33:07.130853
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() != [1, 2]


# Generated at 2022-06-14 03:33:12.454504
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    actual = Maybe.just(1) == Maybe.just(1)
    assert actual
    actual = Maybe.just(1) != Maybe.just(2)
    assert actual
    actual = Maybe.nothing() == Maybe.nothing()
    assert actual
    actual = Maybe.nothing() != Maybe.just(1)
    assert actual
    actual = Maybe.nothing() != Maybe.just(None)
    assert actual


# Generated at 2022-06-14 03:33:19.579083
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Given
    val1 = 1
    val2 = 5
    val3 = Maybe.just(val1)
    val4 = Maybe.just(val2)

    # When
    result1 = val3.filter(lambda x: x == 1)
    result2 = val4.filter(lambda x: x == 4)
    result3 = val3.filter(lambda x: x == 2)

    # Then
    assert result1 == val3
    assert result2 == Maybe.nothing()
    assert result3 == Maybe.nothing()



# Generated at 2022-06-14 03:33:25.489531
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    just_maybe = Maybe.just(5)
    assert just_maybe == Maybe.just(5)
    assert not (just_maybe == Maybe.nothing())
    assert not (just_maybe == Maybe.just(10))

    nothing_maybe = Maybe.nothing()
    assert nothing_maybe == Maybe.nothing()
    assert not (nothing_maybe == Maybe.just(5))



# Generated at 2022-06-14 03:33:30.557039
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe(1, True).to_lazy() == Lazy(lambda: None)
    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:33:35.567762
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:33:41.052083
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('foo') == Maybe.just('foo')
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('foo') != Maybe.just('bar')
    assert Maybe.just('foo') != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('bar')


# Generated at 2022-06-14 03:33:44.429025
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:46.526715
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:33:49.333670
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) == Maybe.just('n')



# Generated at 2022-06-14 03:33:56.421941
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy: Lazy[int] = Maybe.just(10).to_lazy()
    assert type(lazy) == Lazy
    assert lazy.value() == 10

    lazy: Lazy[None] = Maybe.nothing().to_lazy()
    assert type(lazy) == Lazy
    assert lazy.value() is None

# Generated at 2022-06-14 03:34:02.574235
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Test for when maybe is empty
    assert Maybe.nothing() == Maybe.nothing()

    # Test for not empty maybe
    assert Maybe.just('val') == Maybe.just('val')

    # Test for not empty maybe
    assert Maybe.just(1) != Maybe.just('val')

    # Test for when maybe is empty
    assert Maybe.nothing() != Maybe.just('val')



# Generated at 2022-06-14 03:34:07.296437
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(4).to_lazy() == Lazy(lambda: 4)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:34:15.203459
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(42).filter(lambda a: a % 2 == 0) == Maybe.just(42)
    assert Maybe.just(42).filter(lambda a: a % 2 != 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: a % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:34:19.301281
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.nothing() != Maybe.just(2)


# Generated at 2022-06-14 03:34:26.560292
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Unit test for method equal of class Maybe
    """

    def check_Maybe___eq__():
        assert Maybe.just(1) == Maybe.just(1)
        assert Maybe.nothing() == Maybe.nothing()
        assert Maybe.nothing() != Maybe.just(1)
        assert Maybe.just(1) != Maybe.nothing()
        assert Maybe.just(1) != Maybe.just(2)

    check_Maybe___eq__()



# Generated at 2022-06-14 03:34:38.209538
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.comparison import Equal

    # Test when Maybe is empty
    result = Maybe.nothing().filter(lambda x: isinstance(x, dict))
    assert result == Maybe.nothing()

    # Test when Maybe is not empty but filterer returns False
    result = Maybe.just({}).filter(lambda x: isinstance(x, list))
    assert result == Maybe.nothing()

    # Test when Maybe is not empty and filterer returns True
    result = Maybe.just({}).filter(lambda x: isinstance(x, dict))
    assert result == Maybe.just({})

    # Test when Maybe is not empty but filterer returns False
    result = Maybe.just([1]).filter(lambda x: x == [])
    assert result == Maybe.nothing()

    # Test when Maybe is not empty and filterer returns True

# Generated at 2022-06-14 03:34:42.008998
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    def get_left_maybe() -> Maybe[int]:
        return Maybe.just(1)

    def get_right_maybe() -> Maybe[int]:
        return Maybe.just(2)

    assert get_left_maybe() == get_right_maybe()



# Generated at 2022-06-14 03:34:48.709789
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test Maybe.to_lazy method.
    """
    from pymonet.functor import Functor

    maybe = Maybe.just(1)
    assert isinstance(maybe.to_lazy(), Functor)

    maybe = Maybe.nothing()
    assert isinstance(maybe.to_lazy(), Functor)



# Generated at 2022-06-14 03:34:53.057173
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()



# Generated at 2022-06-14 03:35:02.467757
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for filter method of Maybe.

    :returns: none
    :rtype: None
    """
    assert Maybe.just(None).filter(lambda x: x is None) == Maybe.nothing()
    assert Maybe.just(42).filter(lambda x: x is None) == Maybe.nothing()
    assert Maybe.just(42).filter(lambda x: x == 42) == Maybe.just(42)
    assert Maybe.just(42).filter(lambda x: x == 43) == Maybe.nothing()


# Generated at 2022-06-14 03:35:06.850694
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) != Maybe.just(2)
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != 2
    assert Maybe.just(2) != 4


# Generated at 2022-06-14 03:35:13.441076
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe = Maybe.just(1)
    lazy = maybe.to_lazy()
    assert lazy.value() == 1
    assert lazy.value() == 1
    assert lazy.value() == 1

    maybe = Maybe.nothing()
    lazy = maybe.to_lazy()
    assert lazy.value() is None
    assert lazy.value() is None
    assert lazy.value() is None

# Generated at 2022-06-14 03:35:18.034984
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:35:29.166952
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just([1, 2, 3]) == Maybe.just([1, 2, 3])
    assert Maybe.just((1, 2, 3)) == Maybe.just((1, 2, 3))
    assert Maybe.just({1, 2, 3}) == Maybe.just({1, 2, 3})
    assert Maybe.just({1: 'a', 2: 'b', 3: 'c'}) == Maybe.just({1: 'a', 2: 'b', 3: 'c'})
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just([1, 1, 3]) != Maybe.just([1, 2, 3])
   

# Generated at 2022-06-14 03:35:38.353538
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    is_empty = Maybe(0, True)
    is_not_empty = Maybe(2, False)
    is_not_empty2 = Maybe(3, False)

    res = is_empty.filter(lambda x: x % 2 == 0)
    assert res == is_empty

    res = is_not_empty.filter(lambda x: x % 2 == 0)
    assert res == is_not_empty

    res = is_not_empty2.filter(lambda x: x % 2 == 0)
    assert res == is_empty


# Generated at 2022-06-14 03:35:45.381092
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe

    :returns: None
    :rtype: None
    """
    assert(Maybe.just(0).filter(lambda x: True) == Maybe.just(0))
    assert(Maybe.just(0).filter(lambda x: False) == Maybe.nothing())
    assert(Maybe.nothing().filter(lambda x: True) == Maybe.nothing())


# Generated at 2022-06-14 03:35:50.583984
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:35:58.306482
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert (
        Maybe.just(1) == Maybe.just(1)
    )

    assert (
        Maybe.nothing() == Maybe.nothing()
    )

    assert (
        Maybe.just(1) != Maybe.just(2)
    )

    assert (
        Maybe.nothing() != Maybe.just(1)
    )

    assert (
        Maybe.just(1) != Maybe.nothing()
    )


# Generated at 2022-06-14 03:36:07.500659
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # given
    maybe_one = Maybe.just(1)
    maybe_two = Maybe.just(2)
    maybe_three = Maybe.just(3)
    nothing_maybe = Maybe.nothing()

    # when
    actual_maybe_one = maybe_one.filter(lambda x: x == 1)
    actual_maybe_two = maybe_two.filter(lambda x: x == 1)
    actual_maybe_three = maybe_three.filter(lambda x: x == 1)

    nothing_maybe_one = nothing_maybe.filter(lambda x: x == 1)
    nothing_maybe_two = nothing_maybe.filter(lambda x: x == 2)
    nothing_maybe_three = nothing_maybe.filter(lambda x: x == 3)

    # then
    assert actual_maybe_one == Maybe.just(1)


# Generated at 2022-06-14 03:36:11.266720
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:36:14.091866
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:36:16.641307
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(2).to_lazy().value() == 2
    assert Maybe.nothing().to_lazy().value() == None


# Generated at 2022-06-14 03:36:22.514468
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('some') == Maybe.just('some')
    assert Maybe.just('some') != Maybe.just('other')
    assert Maybe.just('some') != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:36:27.387584
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:36:29.639030
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe = Maybe.just(10)
    assert isinstance(maybe.to_lazy(), Lazy)



# Generated at 2022-06-14 03:36:34.662187
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()

# Generated at 2022-06-14 03:36:39.570963
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just("")
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just("2") == Maybe.just("2")
    assert Maybe.just("a") != Maybe.just("b")
    assert Maybe.just("a") != Maybe.nothing()


# Generated at 2022-06-14 03:36:41.738381
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    obj = Maybe.just(2)
    assert obj.to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:36:47.062793
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(x):
        return x > 0
    assert Maybe.just(1).filter(filterer).value == 1
    assert Maybe.just(0).filter(filterer).is_nothing
    assert Maybe.nothing().filter(filterer).is_nothing


# Generated at 2022-06-14 03:36:57.190030
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from parameterizedtestcase import ParameterizedTestCase

    positive_predicate = lambda x: True
    negative_predicate = lambda x: False

    tests = [
        ParameterizedTestCase(
            args=["filter with positive predicate"],
            kwargs={
                "filterer": positive_predicate,
                "expected": Maybe.nothing()
            },
            expected=Maybe.just(1),
        ),
        ParameterizedTestCase(
            args=["filter with negative predicate"],
            kwargs={
                "filterer": negative_predicate,
                "expected": Maybe.nothing()
            },
            expected=Maybe.just(1)
        )
    ]

    for test in tests:
        result = test.expected.filter(**test.kwargs)

# Generated at 2022-06-14 03:37:00.281126
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:05.909450
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    def filterer(value):
        return value > 20

    assert Maybe.just(5).filter(filterer) == Maybe.nothing()

    assert Maybe.just(21).filter(filterer) == Maybe.just(21)

    assert Maybe.just(22).filter(filterer) == Maybe.just(22)

    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:37:12.791078
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.just(4) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(4) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(4)



# Generated at 2022-06-14 03:37:17.109129
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    print('test_Maybe_filter')

    assert Maybe.just(5).filter(
        lambda x: x >= 5) == Maybe.just(5)
    assert Maybe.just(5).filter(
        lambda x: x < 5) == Maybe.nothing()
    assert Maybe.nothing().filter(
        lambda x: x >= 5) == Maybe.nothing()

    print('test_Maybe_filter passed')


# Generated at 2022-06-14 03:37:21.700157
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()


# Generated at 2022-06-14 03:37:25.378848
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value > 2

    assert Maybe.just(1).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()
    assert Maybe.just(4).filter(filterer) == Maybe.just(4)



# Generated at 2022-06-14 03:37:35.450869
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor
    from pymonet.applicative import Applicative

    def test_method_filter_with_no_value_and_empty_filterer():
        m = Maybe.just(12)

        def f():
            return m.filter([])

        assert Functor.test_identity_law(Maybe, m)
        assert Functor.test_composition_law(Maybe, m, lambda x: x + 4, lambda x: x + 4)
        assert Applicative.test_identity_law(Maybe, m)
        assert Applicative.test_composition_law(Maybe, m, lambda x: x + 4, lambda x: x + 4)
        assert Functor.test_homomorphism_law(Maybe, m, lambda x: x + 4)
        assert Functor.test_

# Generated at 2022-06-14 03:37:41.356820
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1).to_either() == Either.right(1)
    assert Maybe.just(1).filter(lambda x: x == 2).to_either() == Either.left(None)
    assert Maybe.nothing().filter(lambda x: x == 1).to_either() == Either.left(None)


# Generated at 2022-06-14 03:37:44.948033
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(2, False) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(1, True)

    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:37:52.071387
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe_with_value = Maybe.just(5)
    maybe_with_nothing = Maybe.nothing()

    even_filterer = lambda x: x % 2 == 0
    odd_filterer = lambda x: x % 2 != 0

    assert maybe_with_value.filter(even_filterer) == Maybe.just(5)
    assert maybe_with_value.filter(odd_filterer) == Maybe.nothing()
    assert maybe_with_nothing.filter(even_filterer) == Maybe.nothing()
    assert maybe_with_nothing.filter(odd_filterer) == Maybe.nothing()



# Generated at 2022-06-14 03:37:54.350719
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:38:00.376021
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda num: num > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda num: num > 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda num: num > 0) == Maybe.nothing()


# Generated at 2022-06-14 03:38:13.664577
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x < 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == None) == Maybe.nothing()


# Generated at 2022-06-14 03:38:18.266017
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:38:21.720203
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()

# Generated at 2022-06-14 03:38:25.206834
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:38:27.619865
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda _: True) == Maybe.nothing()

    assert Maybe.just(5).filter(lambda x: x > 2) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x < 2) == Maybe.nothing()

# Generated at 2022-06-14 03:38:35.668566
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just({'a': 1}) == Maybe.just({'a': 1})
    assert Maybe.just([1, 2, 3]) == Maybe.just([1, 2, 3])
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.nothing() != Maybe.just({'a': 1})
    assert Maybe.just('abc') != Maybe.just('abcd')


# Generated at 2022-06-14 03:38:45.033707
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just('a') == Maybe.just('a')
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)

    assert Maybe.just('') != Maybe.nothing()
    assert Maybe.just('') != Maybe.just('a')
    assert Maybe.just('') == Maybe.just('')

    assert Maybe.just(False) != Maybe.nothing()
    assert Maybe.just(False) != Maybe.just(True)
    assert Maybe.just(False) == Maybe.just(False)

    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.just

# Generated at 2022-06-14 03:38:52.444150
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.utils_test import is_eq

    is_eq(
        'Maybe[T].__eq__ for two empty maybes',
        Maybe.nothing(),
        Maybe.nothing()
    )
    is_eq(
        'Maybe[T].__eq__ for one empty maybe and no empty maybe',
        Maybe.nothing(),
        Maybe.just(123)
    )
    is_eq(
        'Maybe[T].__eq__ for two empty maybes with different value',
        Maybe.just(123),
        Maybe.just(100)
    )
    is_eq(
        'Maybe[T].__eq__ for two empty maybes with the same value',
        Maybe.just(123),
        Maybe.just(123)
    )


# Generated at 2022-06-14 03:38:58.211948
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    # Test case when Maybe is not empty
    maybe_value = Maybe.just(5)
    assert maybe_value.to_lazy() == Lazy(lambda: 5)

    # Test case when Maybe is empty
    maybe_value = Maybe.nothing()
    assert maybe_value.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:39:03.630763
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert not Maybe.just(5) == Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert not Maybe.nothing() == 5
    assert Maybe.nothing() != 5



# Generated at 2022-06-14 03:39:19.671897
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just('Hello').filter(lambda x: len(x) == 5) == Maybe.just('Hello')
    assert Maybe.just('Hello').filter(lambda x: len(x) == 4) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()


# Generated at 2022-06-14 03:39:25.721722
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.just(4) != Maybe.just(5)
    assert Maybe.just(4) != Maybe.nothing()

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(4)
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:39:28.505083
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assertion = Maybe.just(10) == Maybe.just(10)
    assert assertion

    assertion = Maybe.nothing() == Maybe.nothing()
    assert assertion



# Generated at 2022-06-14 03:39:30.560803
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:35.387158
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('test') == Maybe.just('test')
    assert Maybe.just(123) == Maybe.just(123)
    assert Maybe.just(123) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(123)



# Generated at 2022-06-14 03:39:45.401132
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    The test function checks the implementation of the method __eq__.

    :returns: Test result
    :rtype: Boolean
    """

    def assert_eq_maybe(a: Maybe[T], b: Maybe[T], c: bool):
        assert (a == b) == c

    assert_eq_maybe(Maybe.just(3), Maybe.just(3), True)
    assert_eq_maybe(Maybe.just(3), Maybe.nothing(), False)
    assert_eq_maybe(Maybe.just(4), Maybe.just(5), False)
    assert_eq_maybe(Maybe.nothing(), Maybe.nothing(), True)


# Generated at 2022-06-14 03:39:48.884276
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():

    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy

    def func():
        return 5

    maybe = Maybe.just(func)

    assert maybe.to_lazy() == Lazy(func)



# Generated at 2022-06-14 03:39:51.416679
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:54.120355
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:39:59.526905
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(42).filter(lambda v: v > 0) == Maybe.just(42)
    assert Maybe.just(42).filter(lambda v: v > 100) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v > 100) == Maybe.nothing()



# Generated at 2022-06-14 03:40:14.973629
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert str(Maybe.just(1).to_lazy()) == str(Lazy(lambda: 1))
    assert str(Maybe.nothing().to_lazy()) == str(Lazy(lambda: None))


# Generated at 2022-06-14 03:40:21.203796
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_class import test_monad
    from pymonet.monad_class import test_monad_fmap
    import pytest
    from pymonet.lazy import Lazy
    from pymonet.monad_class import monad_test_data
    from pymonet.validation import Validation

    def test_lazy_mapper(value):
        def mapper():
            return value
        return mapper

    test_monad(
        unit=Maybe.just,
        bind=lambda x: x.bind,
        fmap=lambda x: x.map,
        monad_test_data=monad_test_data,
        is_lazy=True,
        test_lazy_mapper=test_lazy_mapper
    )

# Generated at 2022-06-14 03:40:29.252418
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) is not Maybe.just(5)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() is Maybe.nothing()

    assert Maybe.just(10) != Maybe.just(11)
    assert Maybe.just(10) is not Maybe.just(11)

    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.just(10) is not Maybe.nothing()

    assert Maybe.nothing() != Maybe.just(10)
    assert Maybe.nothing() is not Maybe.just(10)



# Generated at 2022-06-14 03:40:31.058173
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(None) != Maybe.nothing()



# Generated at 2022-06-14 03:40:35.654373
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x % 2 == 0) == Maybe.just(10)
    assert Maybe.just(11).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x) == Maybe.nothing()



# Generated at 2022-06-14 03:40:41.656150
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    val = Maybe.just(1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert val.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:40:46.815161
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:40:57.714164
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe.

    :returns: None
    """
    import unittest

    class TestMaybeFilter(unittest.TestCase):

        def test_Maybe_filter_for_Maybe_empty(self):
            self.assertEqual(
                Maybe.nothing().filter(lambda x: x < 0),
                Maybe.nothing()
            )

        def test_Maybe_filter_for_Maybe_not_empty_and_filterer_returns_true(self):
            self.assertEqual(
                Maybe.just(5).filter(lambda x: x > 0),
                Maybe.just(5)
            )


# Generated at 2022-06-14 03:41:01.035051
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:41:06.168712
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) is not Maybe.just(3)

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() is not Maybe.nothing()

    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)
    assert Maybe.nothing() != Maybe.just(4)
    assert Maybe.just(3) != Maybe.just(4)

    assert Maybe.just(3) != 3
    assert Maybe.nothing() != None


# Generated at 2022-06-14 03:41:22.436132
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('a') == Maybe.just('a')
    assert Maybe.just('a') != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('a')
    assert Maybe.just(5) != Maybe.just('5')


# Generated at 2022-06-14 03:41:26.557923
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)

    assert Maybe.just(1) == Maybe.just(1)
    assert not (Maybe.just(1) == Maybe.just(2))
    assert Maybe.just(1) != Maybe.nothing()