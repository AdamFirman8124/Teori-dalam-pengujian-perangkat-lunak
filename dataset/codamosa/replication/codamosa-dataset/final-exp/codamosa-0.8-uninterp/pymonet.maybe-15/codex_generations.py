

# Generated at 2022-06-14 03:31:30.439777
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Checks if method filter of class Maybe works properly
    """
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()


# Generated at 2022-06-14 03:31:32.590858
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:31:42.928030
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1), 'Maybe(1) == Maybe(1)'
    assert Maybe.just(1) != Maybe.just(2), 'Maybe(1) != Maybe(2)'
    assert Maybe.just(1) != Maybe.nothing(), 'Maybe(1) != Maybe.nothing()'
    assert Maybe.nothing() == Maybe.nothing(), 'Maybe.nothing() == Maybe.nothing()'
    assert Maybe.just(1) != 1, 'Maybe(1) != 1'
    assert Maybe.just(1) != '1', 'Maybe(1) != \'1\''

# Unit tests for method just of class Maybe

# Generated at 2022-06-14 03:31:45.625900
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:31:51.153882
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just('string') == Maybe.just('string')
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just(['lst']) == Maybe.just(['lst'])
    assert Maybe.just({'dict': 1}) == Maybe.just({'dict': 1})


# Generated at 2022-06-14 03:31:57.792921
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(4)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:02.462721
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x % 3 == 0) \
        == Maybe.just(10)

    assert Maybe.just(9).filter(lambda x: x % 3 == 0) \
        == Maybe.just(9)

    assert Maybe.nothing().filter(lambda x: x % 3 == 0) \
        == Maybe.nothing()

# Generated at 2022-06-14 03:32:07.816296
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 10) == Maybe.just(10).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()



# Generated at 2022-06-14 03:32:11.603671
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:32:16.230423
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def foo():
        return "foo"

    assert Maybe(42, False).to_lazy() == Lazy(lambda: 42)
    assert Maybe(foo, False).to_lazy() == Lazy(foo)



# Generated at 2022-06-14 03:32:27.254198
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    lazy_one = Maybe.just(1).to_lazy()
    assert 1 == lazy_one.evaluate(lambda: None), "Maybe.to_lazy - fail on to_lazy with not empty maybe"

    lazy_none = Maybe.nothing().to_lazy()
    assert None == lazy_none.evaluate(lambda: None), "Maybe.to_lazy - fail on to_lazy with empty maybe"



# Generated at 2022-06-14 03:32:33.460525
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(1)
    lazy = maybe.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.eval() == 1

    maybe = Maybe.nothing()
    lazy = maybe.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.eval() is None


# Generated at 2022-06-14 03:32:37.462866
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)



# Generated at 2022-06-14 03:32:41.966767
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value: int) -> bool:
        return value > 10

    assert Maybe(11, False).filter(filterer) == Maybe(11, False)
    assert Maybe(1, False).filter(filterer) == Maybe(None, True)


# Generated at 2022-06-14 03:32:44.249309
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:32:54.078310
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just('x').filter(lambda x: x == 'x') == Maybe.just('x')
    assert Maybe.just('y').filter(lambda x: x == 'x') == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()

    # Unit test for method bind of class Maybe
    def test_Maybe_bind():
        assert Maybe.just('x').bind(Maybe.just) == Maybe.just('x')
        assert Maybe.just('y').bind(Maybe.nothing) == Maybe.nothing()
        assert Maybe.nothing().bind(Maybe.just) == Maybe.nothing()



# Generated at 2022-06-14 03:33:02.355052
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    class CustomClass:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return isinstance(other, CustomClass) and self.value == other.value

    assert Maybe(None, True) == Maybe(None, True)
    assert Maybe(None, True) == Maybe.nothing()
    assert Maybe(None, True) != Maybe(0, True)
    assert Maybe(None, True) != Maybe(0, False)
    assert Maybe(None, True) != Maybe.just(0)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(0)
    assert Maybe.just(0) == Maybe.just(0)
    assert Maybe.just(0) != Maybe.just(1)

# Generated at 2022-06-14 03:33:06.881399
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:33:11.344878
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()

    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()

# Generated at 2022-06-14 03:33:16.204336
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)



# Generated at 2022-06-14 03:33:23.757244
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:33:27.273198
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe_one = Maybe.just(1)
    maybe_one_copy = Maybe.just(1)
    maybe_nothing = Maybe.nothing()
    maybe_one_another = Maybe.just(1)
    maybe_one_another_subclass_box = Box.just(1)

    assert maybe_one == maybe_one_copy and not maybe_one == maybe_nothing and not maybe_one == None and not maybe_one == maybe_one_another_subclass_box


# Generated at 2022-06-14 03:33:33.810199
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy().eval() == 1
    assert Maybe.just(1).to_lazy() == Lazy(lambda: Maybe.just(1).value)
    assert Maybe.nothing().to_lazy().eval() is None
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:33:45.933189
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.maybe import Maybe

    # Case 1: Maybe is empty and other is empty
    print('Case 1')
    maybe = Maybe.nothing()
    other = Maybe.nothing()
    assert maybe == other, 'Error in __eq__ method of Maybe class'

    # Case 2: Maybe is empty and other is not empty
    print('Case 2')
    maybe = Maybe.nothing()
    other = Maybe.just(1)
    assert not maybe == other, 'Error in __eq__ method of Maybe class'

    # Case 3: Maybe is not empty and other is empty
    print('Case 3')
    maybe = Maybe.just(1)
    other = Maybe.nothing()
    assert not maybe == other, 'Error in __eq__ method of Maybe class'

    # Case 4: Maybe has the same value and other has the same value
    print

# Generated at 2022-06-14 03:33:50.303528
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # arrange
    maybe_input = Maybe.just(10)
    def filterer(x):
        return x > 10

    # act
    maybe_result = maybe_input.filter(filterer)

    # assert
    assert maybe_result == Maybe.nothing()

# Generated at 2022-06-14 03:33:57.422772
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test for method filter of class Maybe.

    :returns: None
    """
    def condition(x): return x > 2

    assert Maybe.just(3).filter(condition) == Maybe.just(3)
    assert Maybe.just(0).filter(condition) == Maybe.nothing()
    assert Maybe.just(None).filter(condition) == Maybe.nothing()
    assert Maybe.nothing().filter(condition) == Maybe.nothing()



# Generated at 2022-06-14 03:34:02.574139
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)

test_Maybe___eq__()



# Generated at 2022-06-14 03:34:07.714160
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1).__eq__(Maybe.nothing()) == False
    assert Maybe.just(1).__eq__(None) == False
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:13.988019
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Test case for method __eq__ of class Maybe.
    """
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)

    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:34:17.038227
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(True).filter(lambda x: x) == Maybe.just(True)
    assert Maybe.just(False).filter(lambda x: x) == Maybe.nothing()


# Generated at 2022-06-14 03:34:25.499580
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just('string') == Maybe.just('string')
    assert Maybe.just([1, 2, 3]) == Maybe.just([1, 2, 3])
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(10)


# Generated at 2022-06-14 03:34:29.913733
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x < 6) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x > 6) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 6) == Maybe.nothing()



# Generated at 2022-06-14 03:34:35.034227
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x != 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()

# Generated at 2022-06-14 03:34:39.027455
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    m = Maybe.just(1)
    assert m.to_lazy() == Lazy(lambda: 1)
    assert m.to_lazy().get() == 1
    assert Maybe.nothing().to_lazy().get() is None



# Generated at 2022-06-14 03:34:48.315080
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Check method '__eq__' for class Maybe.
    """
    # Test for None value
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() == Maybe.just(None)
    assert Maybe.just(None) == Maybe.nothing()

    # Test for str value
    assert Maybe.just("some string") == Maybe.just("some string")
    assert Maybe.just("some string") != Maybe.just("some other string")
    assert Maybe.just("some string") != Maybe.nothing()

    # Test for int value
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()

    # Test for float

# Generated at 2022-06-14 03:34:50.633099
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:34:57.298844
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Given
    x = lambda x: x % 2 == 0
    monad_1 = Maybe.just(2)
    monad_2 = Maybe.just(3)
    monad_3 = Maybe.nothing()

    # When
    result_1 = monad_1.filter(x)
    result_2 = monad_2.filter(x)
    result_3 = monad_3.filter(x)

    # Then
    assert result_1 == Maybe.just(2)
    assert result_2 == Maybe.nothing()
    assert result_3 == Maybe.nothing()

# Generated at 2022-06-14 03:35:08.081043
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    expectation = Lazy(lambda: 123)
    expectation_value = 123
    actual = Maybe.just(123).to_lazy()
    actual_value = actual.value()
    if actual != expectation:
        raise Exception('Maybe.to_lazy should return Lazy monad with function returning value stored in Maybe\n'
                        f'Expectation: {expectation}\n'
                        f'Actual: {actual}\n'
                        f'Expectation value: {expectation_value}\n'
                        f'Actual value: {actual_value}\n')
    expectation = Lazy(lambda: None)
    expectation_value = None
    actual = Maybe.nothing().to_lazy()
    actual_value = actual.value()

# Generated at 2022-06-14 03:35:18.035547
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Right(1) == Just(1)
    assert Maybe.just(1) == Maybe.just(1)
    # Nothing == Left(None)
    assert Maybe.nothing() == Maybe.nothing()
    # Right(1) is not Nothing
    assert Maybe.just(1) != Maybe.nothing()
    # Nothing is not Right(1)
    assert Maybe.nothing() != Maybe.just(1)
    # Maybe(Right(1), Maybe(Right(1))) != Maybe(Right(1), Maybe(Right(2)))
    assert Maybe.just(Maybe.just(1)) != Maybe.just(Maybe.just(2))


# Generated at 2022-06-14 03:35:21.970079
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:35:31.886702
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:35:36.931723
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:35:43.194311
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(4).filter(lambda x: x % 2 == 0) == Maybe.just(4)
    assert Maybe.just(4).filter(lambda x: x % 2 == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:35:50.959150
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.utils import pluck

    cases = [
        (
            Maybe.just("43"),
            lambda x: x.isdigit(),
            Maybe.just("43")
        ),
        (
            Maybe.just("hello"),
            lambda x: x.isdigit(),
            Maybe.nothing()
        ),
        (
            Maybe.nothing(),
            lambda x: x.isdigit(),
            Maybe.nothing()
        ),
    ]


# Generated at 2022-06-14 03:36:02.471635
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy, call
    from pymonet.monad_try import Try, Success, Failure

    assert Maybe(True, False) \
        .to_lazy() == Lazy(lambda: True)

    assert Maybe(None, False) \
        .to_lazy() == Lazy(lambda: None)

    assert Maybe(None, True) \
        .to_lazy() == Lazy(lambda: None)

    assert Maybe("test", False) \
        .to_lazy() == Lazy(lambda: "test")

    assert Maybe("test", True) \
        .to_lazy() == Lazy(lambda: None)

    assert Maybe(Try(5, True), False) \
        .to_lazy() == Lazy(lambda: Try(5, True))

    assert Maybe

# Generated at 2022-06-14 03:36:07.481070
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe = Maybe.just(1)
    maybe_copy = Maybe.just(1)
    maybe_another = Maybe.just(2)
    nothing = Maybe.nothing()

    assert(maybe == maybe_copy)
    assert(maybe != maybe_another)
    assert(nothing == Maybe.nothing())
    assert(maybe != nothing)



# Generated at 2022-06-14 03:36:14.478400
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    actual = Maybe(1, False) == Maybe(1, False)
    assert actual is True

    actual = Maybe(1, False) == Maybe(2, False)
    assert actual is False

    actual = Maybe(1, True) == Maybe(1, True)
    assert actual is True

    actual = Maybe(1, True) == Maybe(2, True)
    assert actual is True

    actual = Maybe(1, True) == Maybe(1, False)
    assert actual is False

    actual = Maybe(1, False) == Maybe(2, True)
    assert actual is False


# Generated at 2022-06-14 03:36:20.061324
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(1, True)

    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, True)


# Generated at 2022-06-14 03:36:26.700414
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    maybe = Maybe.nothing()
    lazy = maybe.to_lazy()
    assert lazy == Lazy(lambda: None)
    maybe = Maybe.just(1)
    lazy = maybe.to_lazy()
    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 03:36:31.764130
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()

# Generated at 2022-06-14 03:36:40.339008
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:36:47.740616
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(
        lambda x: x % 2 == 0
    ).get_or_else('Nope') == 'Nope'

    assert Maybe.just(4).filter(
        lambda x: x % 2 == 0
    ).get_or_else('Nope') == 4

    assert Maybe.nothing().filter(
        lambda x: x % 2 == 0
    ).get_or_else('Nope') == 'Nope'


# Generated at 2022-06-14 03:36:52.191007
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda n: n > 0) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda n: n < 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda n: n > 0) == Maybe.nothing()

# Generated at 2022-06-14 03:36:56.075797
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(10).filter(lambda x: x > 9) == Maybe.just(10)
    assert Maybe.just(10).filter(lambda x: x > 10) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 9) == Maybe.nothing()


# Generated at 2022-06-14 03:37:04.045324
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(None).filter(lambda x: x is None) == Maybe.nothing()
    assert Maybe.just(None).filter(lambda x: x is not None) == Maybe.just(None)
    assert Maybe.just(0).filter(lambda x: x == 0) == Maybe.just(0)
    assert Maybe.just(0).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()



# Generated at 2022-06-14 03:37:08.451368
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 2) == Maybe.nothing()


# Generated at 2022-06-14 03:37:15.478235
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.just(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Maybe.just(Try(1, True)).to_lazy() == Lazy(lambda: Try(1, True))



# Generated at 2022-06-14 03:37:22.382856
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.validation import Validation, Error

    assert Maybe.just(2).filter(
        lambda x: x % 2 == 0
    ) == Maybe.just(2)
    assert Maybe.just(3).filter(
        lambda x: x % 2 == 0
    ) == Maybe.nothing()
    assert Maybe.nothing().filter(
        lambda x: x % 2 == 0
    ) == Maybe.nothing()



# Generated at 2022-06-14 03:37:25.930198
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result = Maybe.just(1).filter(lambda x: x == 1)
    expected = Maybe.just(1)
    assert result == expected



# Generated at 2022-06-14 03:37:28.474210
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    
    assert Maybe.just(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:37:44.856692
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)
    assert Maybe.just(6).filter(lambda x: x == 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()


# Generated at 2022-06-14 03:37:48.456702
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    maybe_1 = Maybe.just(1)
    assert maybe_1.to_lazy().value() == 1

    maybe_2 = Maybe.nothing()
    assert maybe_2.to_lazy().value() == None


# Generated at 2022-06-14 03:37:51.548584
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def return_true(new_value):
        return new_value > 0

    result = Maybe.just(-1).filter(return_true)
    assert isinstance(result, Maybe)
    result = Maybe.just(1).filter(return_true)
    assert isinstance(result, Maybe)


# Generated at 2022-06-14 03:37:57.495888
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 0) == Maybe.nothing()



# Generated at 2022-06-14 03:38:01.849003
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda a: a == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda a: a == 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: a == 2) == Maybe.nothing()

# Generated at 2022-06-14 03:38:06.252024
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from random import randint
    from pymonet.equals import equals

    a = randint(1, 100)
    m = randint(1, 100)
    maybe_value = Maybe.just(a)
    equals(maybe_value.filter(lambda a: a % m == 0), Maybe.just(a)).should_be_true()
    equals(Maybe.just(a).filter(lambda a: a % m != 0), Maybe.nothing()).should_be_true()


# Generated at 2022-06-14 03:38:09.049030
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just('test').to_lazy() == Lazy(lambda: 'test')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:16.057047
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.monad_try import Try

    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0).to_try() == Try(None, is_success=False)


# Generated at 2022-06-14 03:38:19.810211
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:25.641299
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    :returns: True
    :rtype: Boolean
    """
    return (Maybe.just(1) == Maybe.just(1).filter(lambda n: n == 1))  \
        and (Maybe.nothing() == Maybe.just(1).filter(lambda n: n == 2))



# Generated at 2022-06-14 03:38:40.551391
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:38:47.649435
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(1, False).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe(2, False).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe(3, False).filter(lambda x: x > 2) == Maybe.just(3)
    assert Maybe.nothing().filter(lambda x: x > 2) == Maybe.nothing()

if __name__ == '__main__':
    test_Maybe_filter()

# Generated at 2022-06-14 03:38:54.226849
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x < 2) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x == 2) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x > 2) == Maybe.nothing()

    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()

# Generated at 2022-06-14 03:38:57.481096
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    box = Maybe.just(1).to_lazy()
    assert box.value() == 1
    box = Maybe.nothing().to_lazy()
    assert box.value() is None


# Generated at 2022-06-14 03:39:04.870023
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    none_maybe = Maybe.nothing()
    int_lazy = none_maybe.to_lazy()

    assert int_lazy.value() == None

    some_lazy = Maybe.just(10).to_lazy()
    assert some_lazy.value() == 10

# Generated at 2022-06-14 03:39:08.529774
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(1, False).to_lazy().evaluate() == 1
    assert Maybe(None, True).to_lazy().evaluate() is None

# Generated at 2022-06-14 03:39:13.980876
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    f = lambda x: x >= 3
    assert Maybe.just(0).filter(f) == Maybe.nothing()
    assert Maybe.just(3).filter(f) == Maybe.just(3)
    assert Maybe.nothing().filter(f) == Maybe.nothing()



# Generated at 2022-06-14 03:39:17.848865
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:39:27.608165
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for function filter of class Maybe.

    :returns: None
    :rtype: None
    """
    from pymonet.test_utils import assert_maybe

    assert_maybe(
        Maybe.just(1).filter(lambda v: v == 1),
        Maybe.just(1)
    )
    assert_maybe(
        Maybe.just(1).filter(lambda v: v == 2),
        Maybe.nothing()
    )
    assert_maybe(
        Maybe.nothing().filter(lambda v: v == 1),
        Maybe.nothing()
    )


# Generated at 2022-06-14 03:39:31.063935
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert(
        Maybe.just(3).filter(lambda x: x > 2) == Maybe.just(3)
    )
    assert(
        Maybe.just(3).filter(lambda x: x > 10) == Maybe.nothing()
    )
    assert(
        Maybe.nothing().filter(lambda x: x > 10) == Maybe.nothing()
    )


# Generated at 2022-06-14 03:39:43.069578
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    m = Maybe(1, False)
    assert m.to_lazy().force() == 1



# Generated at 2022-06-14 03:39:49.146765
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    func = lambda x: x > 10
    maybe = Maybe.just(5)
    maybe2 = maybe.filter(func)
    assert maybe2 == Maybe.nothing()

    maybe = Maybe.just(15)
    maybe2 = maybe.filter(func)
    assert maybe2 == Maybe.just(15)

    maybe = Maybe.nothing()
    maybe2 = maybe.filter(func)
    assert maybe2 == Maybe.nothing()


# Generated at 2022-06-14 03:39:53.232204
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:39:57.919039
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test filter method of Maybe class.
    """
    maybe_empty = Maybe.nothing()
    maybe_with_5 = Maybe.just(5)

    assert maybe_empty.filter(lambda x: x == 5).to_box().value == maybe_empty.to_box().value
    assert maybe_with_5.filter(lambda x: x == 5) == Maybe.just(5)

# Generated at 2022-06-14 03:40:00.449626
# Unit test for method filter of class Maybe
def test_Maybe_filter():

    func = maybe_with_five.filter(lambda x: x >= 5)
    assert isinstance(func, Maybe) and (func == maybe_with_five)
    assert isinstance(maybe_with_two.filter(lambda x: x >= 5), Maybe) and (maybe_with_two.filter(lambda x: x >= 5) == maybe_with_nothing)


# Generated at 2022-06-14 03:40:04.770809
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test for method filter of class Maybe.

    :returns: None
    :rtype: NoneType
    """

    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:40:10.117180
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value: int) -> bool:
        return value % 2 == 0

    maybe = Maybe.just(7)
    assert maybe.filter(filterer) == Maybe.nothing()

    maybe = Maybe.just(8)
    assert maybe.filter(filterer) == Maybe.just(8)

    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:40:13.481765
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe(1, False).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:40:18.465709
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:40:21.834219
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe(3, False).to_lazy() == Lazy(lambda: 3)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:40:47.423763
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:40:51.755346
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Given
    value = 2
    maybe = Maybe.just(value)
    filterer = lambda x: True
    expected = Maybe.just(value)

    # When
    actual = maybe.filter(filterer)

    # Then
    assert actual == expected



# Generated at 2022-06-14 03:41:00.894177
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # arrange
    even_is_empty_maybe = Maybe.nothing()
    even_maybe = Maybe.just(20)
    odd_maybe = Maybe.just(21)

    # act
    even_is_empty_result = even_is_empty_maybe.filter(lambda x: x % 2 == 0)
    even_result = even_maybe.filter(lambda x: x % 2 == 0)
    odd_result = odd_maybe.filter(lambda x: x % 2 == 0)

    # assert
    assert even_is_empty_result == Maybe.nothing()
    assert even_result == Maybe.just(20)
    assert odd_result == Maybe.nothing()

# Generated at 2022-06-14 03:41:06.654228
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just("a").filter(None) == Maybe.just("a")
    assert Maybe.just("a").filter(lambda x: x == "b") == Maybe.nothing()
    assert Maybe.just("a").filter(lambda x: x == "a") == Maybe.just("a")
    assert Maybe.nothing().filter(lambda x: x == "b") == Maybe.nothing()


# Generated at 2022-06-14 03:41:09.964959
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.utils import test_equal

    a = Maybe.just(42)
    test_equal(a.filter(lambda it: it > 41), Maybe.just(42))
    test_equal(a.filter(lambda it: it > 43), Maybe.nothing())

    a = Maybe.nothing()
    test_equal(a.filter(lambda it: it > 41), Maybe.nothing())

# Generated at 2022-06-14 03:41:15.695750
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()



# Generated at 2022-06-14 03:41:21.199101
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Maybe.just(10).to_lazy()
    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:41:28.061315
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x % 3 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x == 0) == Maybe.nothing()

    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()
