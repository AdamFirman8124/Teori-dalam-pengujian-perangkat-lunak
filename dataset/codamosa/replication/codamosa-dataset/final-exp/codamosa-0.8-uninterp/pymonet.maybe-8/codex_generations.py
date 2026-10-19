

# Generated at 2022-06-14 03:31:32.059618
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """Tests unitary of Maybe.to_lazy()"""

    def run_test_case(expected, value):
        maybe = Maybe.just(value)
        assert maybe.to_lazy() == expected

    run_test_case(Lazy(lambda: 15), 15)
    run_test_case(Lazy(lambda: "1"), "1")
    run_test_case(Lazy(lambda: True), True)
    run_test_case(Lazy(lambda: None), None)

    run_test_case(Lazy(lambda: None), Maybe.nothing())


# Generated at 2022-06-14 03:31:41.334994
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda a: a) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: not a) == Maybe.nothing()
    assert Maybe.just(None).filter(lambda a: a) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda a: a) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda a: not a) == Maybe.nothing()
    assert Maybe.just(True).filter(lambda a: a) == Maybe.just(True)


# Generated at 2022-06-14 03:31:46.216827
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just("foo") == Maybe.just("foo")
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just("foo") != Maybe.just("bar")
    assert Maybe.just("foo") != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just("foo")


# Generated at 2022-06-14 03:31:50.575793
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    def dummy_callable() -> str:
        return "We have a value!"

    assert Maybe(dummy_callable, False) == Maybe.to_lazy(Maybe.just(dummy_callable))
    assert Maybe(None, True) == Maybe.to_lazy(Maybe.nothing())

# Generated at 2022-06-14 03:31:54.507472
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 1) == Maybe.nothing()
    assert Maybe.just(-1).filter(lambda x: x > 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 1) == Maybe.nothing()


# Generated at 2022-06-14 03:31:59.964335
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda v: True) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda v: v % 2 == 0) == Maybe.just(2)

    assert Maybe.just(3).filter(lambda v: v % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda v: v % 2 == 0) == Maybe.nothing()



# Generated at 2022-06-14 03:32:10.393903
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just([1]) == Maybe.just([1])
    assert Maybe.just({'a': 1}) == Maybe.just({'a': 1})
    assert Maybe.just(Maybe.just(1)) == Maybe.just(Maybe.just(1))
    assert Maybe.just(lambda x: x) == Maybe.just(lambda x: x)
    assert Maybe.just(0.1) == Maybe.just(0.1)
    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just([1])
    assert Maybe.just(1) != Maybe.just({'a': 1})

# Generated at 2022-06-14 03:32:15.366436
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda value: value != 1) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda value: value == 1) == Maybe.just(1)
    assert Maybe.nothing().filter(lambda value: value == 1) == Maybe.nothing()



# Generated at 2022-06-14 03:32:19.004203
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, False)


# Generated at 2022-06-14 03:32:25.312261
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    maybe = Maybe.just(1)
    lazy = maybe.to_lazy()
    assert lazy == Lazy(lambda: 1)

    maybe = Maybe.nothing()
    lazy = maybe.to_lazy()
    assert lazy == Lazy(lambda: None)


# Generated at 2022-06-14 03:32:36.994455
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda a: a > 5) == Maybe.nothing()
    assert Maybe.just(6).filter(lambda a: a > 5) == Maybe.just(6)
    assert Maybe.just(6).filter(lambda a: a < 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: a > 5) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda a: a < 5) == Maybe.nothing()



# Generated at 2022-06-14 03:32:40.391892
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(2, False) == Maybe(2, False)
    assert Maybe(2, False) != Maybe(2, True)
    assert Maybe(2, False) != Box(2)



# Generated at 2022-06-14 03:32:44.601846
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(2).filter(lambda x: x < 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()

# Generated at 2022-06-14 03:32:54.766225
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.either import Left
    from pymonet.validation import Validation

    assert Maybe(6, False) == Maybe(6, False)
    assert Maybe(6, False) != Maybe(5, False)
    assert Maybe(6, False) != Maybe(6, True)
    assert Maybe(6, True) == Maybe(6, True)
    assert Maybe(6, True) != Maybe(5, True)
    assert Maybe(6, False) != None
    assert Maybe(6, True) != None
    assert Maybe(6, True) != Left(5)
    assert Maybe("abc", False) != Validation(1, [])


# Generated at 2022-06-14 03:32:59.902127
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(lambda x: x) == Maybe.just(lambda x: x)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe(2, False)
    assert Maybe.nothing() != Maybe(3, True)
    assert Maybe.just(1) != Maybe(1, True)


# Generated at 2022-06-14 03:33:05.249470
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert(Maybe.just(42) == Maybe.just(42))
    assert(Maybe.just(42) != Maybe.just("42"))
    assert(Maybe.nothing() == Maybe.nothing())
    assert(Maybe.just(42) != Maybe.nothing())


# Generated at 2022-06-14 03:33:09.383857
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x % 2 == 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()



# Generated at 2022-06-14 03:33:13.621290
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.monad_maybe import Maybe
    from pymonet.lazy import Lazy

    assert Lazy(lambda: None) == Maybe.nothing().to_lazy()
    assert Lazy(lambda: 'value') == Maybe.just('value').to_lazy()


# Generated at 2022-06-14 03:33:17.116460
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:33:20.614235
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, False)



# Generated at 2022-06-14 03:33:36.895223
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Test equality of Maybe.
    """
    # Arrange
    maybe_one = Maybe.just(1)
    maybe_two = Maybe.just(2)
    maybe_one_1 = Maybe.just(1)
    maybe_none = Maybe.nothing()

    # Assert
    assert maybe_one == maybe_one
    assert maybe_two == maybe_two
    assert maybe_one_1 == maybe_one_1
    assert maybe_none == maybe_none
    assert maybe_one != maybe_two
    assert maybe_one != maybe_none
    assert maybe_one != maybe_one_1
    assert maybe_two != maybe_one
    assert maybe_two != maybe_none
    assert maybe_two != maybe_one_1
    assert maybe_one_1 != maybe_one

# Generated at 2022-06-14 03:33:41.850419
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe.just(10)
    maybe2 = Maybe.just(10)
    maybe3 = Maybe.just(20)
    maybe4 = Maybe.nothing()
    maybe5 = Maybe.nothing()
    assert maybe1 == maybe2
    assert maybe3 != maybe2
    assert maybe4 != maybe3
    assert maybe4 == maybe5

# Generated at 2022-06-14 03:33:46.074686
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda v: v == 0) == Maybe.nothing()
    assert Maybe.just(3).filter(lambda v: v == 3) == Maybe.just(3)
    assert Maybe.nothing().filter(lambda v: v == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:33:51.909864
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    a = Maybe.just(42)
    b = Maybe.just(42)
    c = Maybe.just(42.0)
    d = Maybe.just('forty two')
    e = Maybe.nothing()
    f = Maybe.nothing()

    assert a == b
    assert a != c
    assert a != d
    assert a != e

    assert e == f
    assert e != a



# Generated at 2022-06-14 03:33:57.879672
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(x):
        return x > 10

    assert Maybe.just(1).filter(filterer) == Maybe.nothing()
    assert Maybe.just(11).filter(filterer) == Maybe.just(11)
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:34:03.122110
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just('Just_value').filter(lambda value: len(value) > 10) == Maybe.nothing()
    assert Maybe.just('Just_value').filter(lambda value: len(value) < 10) == Maybe.just('Just_value')
    assert Maybe.nothing().filter(lambda value: len(value) < 10) == Maybe.nothing()



# Generated at 2022-06-14 03:34:14.124968
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    to_lazy_test_cases = {
        'test empty Maybe': {
            'given': Maybe.nothing(),
            'expected': Maybe.nothing().to_lazy(),
            'return': Lazy(lambda: None)
        },
        'test not empty Maybe': {
            'given': Maybe.just(2),
            'expected': Maybe.just(2).to_lazy(),
            'return': Lazy(lambda: 2)
        }
    }

    for test_case, params in to_lazy_test_cases.items():
        assert params['expected'] == params['return'], 'test cases failure: {}'.format(test_case)

test_Maybe_to_lazy()



# Generated at 2022-06-14 03:34:19.357924
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result = Maybe(42, False).filter(lambda x: True)
    assert result == Maybe(42, False)

    result = Maybe(42, False).filter(lambda x: False)
    assert result == Maybe(None, True)

    result = Maybe(42, True).filter(lambda x: True)
    assert result == Maybe(None, True)

    result = Maybe(42, True).filter(lambda x: False)
    assert result == Maybe(None, True)



# Generated at 2022-06-14 03:34:22.028224
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:34:26.789681
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(5, False).filter(lambda x: x > 0) == Maybe.just(5)
    assert Maybe(5, False).filter(lambda x: x > 10) == Maybe.nothing()
    assert Maybe(5, True).filter(lambda x: x > 10) == Maybe.nothing()


# Generated at 2022-06-14 03:34:35.184303
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(2, False).filter(lambda x: x == 2) == Maybe(2, False)
    assert Maybe(3, False).filter(lambda x: x == 2) == Maybe(None, True)

# Generated at 2022-06-14 03:34:39.157858
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 4) == Maybe.just(5)
    assert Maybe.just(4).filter(lambda x: x > 4) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 4) == Maybe.nothing()



# Generated at 2022-06-14 03:34:43.222193
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(x):
        return x < 5

    assert Maybe.just(4).filter(filterer) == Maybe.just(4)
    assert Maybe.just(6).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()

# Generated at 2022-06-14 03:34:47.958910
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda value: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda value: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda value: True) == Maybe.nothing()



# Generated at 2022-06-14 03:34:52.803902
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    just_result = Maybe.just('test').filter(lambda s: s != 'test')
    assert isinstance(just_result, Maybe)
    assert just_result.is_nothing is True

    just_result = Maybe.just('test').filter(lambda s: s == 'test')
    assert isinstance(just_result, Maybe)
    assert just_result.is_nothing is False
    assert just_result.value == 'test'

    nothing_result = Maybe.nothing().filter(lambda s: s == 'test')
    assert isinstance(nothing_result, Maybe)
    assert nothing_result.is_nothing is True


# Generated at 2022-06-14 03:35:00.919706
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """Performs unit tests for method filter of class Maybe."""
    # Test 1
    assert Maybe.just(5).filter(
        lambda value: value == 5
    ) == Maybe.just(5)
    # Test 2
    assert Maybe.just(5).filter(
        lambda value: value > 5
    ) == Maybe.nothing()
    # Test 3
    assert Maybe.nothing().filter(
        lambda value: value == 5
    ) == Maybe.nothing()


# Generated at 2022-06-14 03:35:09.566854
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Test for equality of Maybe instances.

    :returns: None
    """
    assert Maybe(10, False) == Maybe(10, False)
    assert Maybe(10, True) == Maybe(10, True)
    assert Maybe(10, False) != Maybe(100, False)
    assert Maybe(10, True) != Maybe(100, True)
    assert Maybe(10, False) != Maybe(10, True)
    assert Maybe(10, True) != Maybe(10, False)
    assert Maybe(10, False) != Maybe(None, False)
    assert Maybe(10, True) != Maybe(None, True)
    assert Maybe(10, False) != Maybe(None, True)
    assert Maybe(10, True) != Maybe(None, False)


# Generated at 2022-06-14 03:35:13.441305
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()


# Generated at 2022-06-14 03:35:19.552110
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(2, True) == Maybe(2, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(2, True) != Maybe(1, True)
    assert Maybe(1, False) != None


# Generated at 2022-06-14 03:35:23.145784
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:35:33.000150
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1) == Maybe(1, False)
    assert Maybe.just(1) != Maybe.just(2) == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing() == Maybe(None, True)
    assert Maybe.nothing() != Maybe.just(1) == Maybe(1, False)



# Generated at 2022-06-14 03:35:36.699278
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    f = lambda m: m.to_lazy()

    result = f(Maybe.just(10))
    assert isinstance(result, Lazy)
    assert result.eval() == 10

    result = f(Maybe.nothing())
    assert isinstance(result, Lazy)
    assert result.eval() is None


# Generated at 2022-06-14 03:35:40.387041
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:35:45.969738
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(42).filter(lambda x: x == 42) == Maybe.just(42)
    assert Maybe.just(42).filter(lambda x: x == 43) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x == 42) == Maybe.nothing()


# Generated at 2022-06-14 03:35:51.314190
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Test 1
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    # Test 2
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()
    # Test 3
    assert Maybe.nothing().filter(lambda x: x == 1) == Maybe.nothing()


# Generated at 2022-06-14 03:35:57.262383
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(2)
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)


# Generated at 2022-06-14 03:36:01.565958
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(7)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.nothing() != Maybe.just(7)
test_Maybe___eq__()



# Generated at 2022-06-14 03:36:08.800811
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.monad_validation import Validation

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing().to_validation() == Maybe.just(Validation.success(1)).ap(Validation.success(lambda x: Validation.success(x + 1)))
    assert Maybe.just(1).to_validation() == Maybe.just(Validation.success(1)).ap(Validation.success(lambda x: Validation.success(x + 1)))
    assert Maybe.just(1).to_validation() == Maybe.just(Validation.success(1)).ap(Validation.success(lambda x: Validation.success(x + 1)))

# Generated at 2022-06-14 03:36:16.812883
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(4) == Maybe.just(4)

    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(3)
    assert Maybe.just(1) != Maybe.just(4)

    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:36:24.296341
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    def f(x: int) -> int:
        return x + 10

    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.just(20) == Maybe.just(20)
    assert Maybe.just(10) != Maybe.just(20)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(f(10)) == Maybe.just(f(10))
    assert Maybe.just(f(20)) == Maybe.just(f(20))

# Unit tests for method map of class Maybe

# Generated at 2022-06-14 03:36:32.673314
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()


# Generated at 2022-06-14 03:36:37.934291
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # given
    maybe = Maybe.just(1)
    # when
    lazy = maybe.to_lazy()
    # then
    assert lazy == Lazy(lambda: 1)

    # given
    maybe = Maybe.nothing()
    # when
    lazy = maybe.to_lazy()
    # then
    assert lazy == Lazy(lambda: None)

# Generated at 2022-06-14 03:36:44.554554
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(0, False) == Maybe(0, False)
    assert Maybe(0, True) == Maybe(0, True)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(0, False) != Maybe(1, False)
    assert Maybe(0, True) != Maybe(0, False)
    assert Maybe(1, True) != Maybe(0, True)
    assert Maybe(1, False) != Maybe(0, False)
    assert Maybe(1, False) != Maybe(0, True)
    assert Maybe(1, True) != Maybe(0, False)


# Generated at 2022-06-14 03:36:48.715572
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe(3, False).filter(lambda x: x > 2) == Maybe(3, False)
    assert Maybe(3, False).filter(lambda x: x > 3) == Maybe(None, True)

# Generated at 2022-06-14 03:36:52.195658
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    assert Maybe.just(42).to_lazy().get() == Maybe.just(42).value
    assert Maybe.nothing().to_lazy().get() is Maybe.nothing().value


# Generated at 2022-06-14 03:36:56.036218
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(42).filter(lambda x: x > 40) == Maybe.just(42)
    assert Maybe.just(42).filter(lambda x: x < 40) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x < 40) == Maybe.nothing()
    return True



# Generated at 2022-06-14 03:37:01.682383
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(4).filter(lambda x: x > 2) == Maybe.just(4)
    assert Maybe.just(2).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 2) == Maybe.nothing()


# Generated at 2022-06-14 03:37:05.820075
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    m = Maybe(1, False)
    l = m.to_lazy()
    assert l == Lazy(lambda: 1)
    l = Maybe.nothing().to_lazy()
    assert l == Lazy(lambda: None)


# Generated at 2022-06-14 03:37:10.924033
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)
    assert Maybe.just(3) != 3
    assert Maybe.nothing() != 3


# Generated at 2022-06-14 03:37:18.999769
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.
    """
    def side_effect_function():
        nonlocal call_counter
        call_counter += 1
        return 2

    maybe = Maybe.just(2)
    lazy = maybe.to_lazy()
    call_counter = 0
    one = lazy.value().value()
    two = lazy.value().value()
    assert one == two == 2
    assert call_counter == 1

    maybe = Maybe.nothing()
    lazy = maybe.to_lazy()
    call_counter = 0
    one = lazy.value().value()
    two = lazy.value().value()
    assert one == two is None
    assert call_counter == 1

    maybe = Maybe.just(side_effect_function)
    lazy = maybe.to_lazy()
   

# Generated at 2022-06-14 03:37:27.523604
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # For non-empty Maybe and non-empty Maybe
    assert Maybe.just("test") == Maybe.just("test")

    # For non-empty Maybe and empty Maybe
    assert Maybe.just("test") != Maybe.nothing()

    # For empty Maybe and empty Maybe
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:37:37.861264
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    m_1 = Maybe.just(1)
    m_2 = Maybe.just(1)
    m_3 = Maybe.just(2)
    m_4 = Maybe.nothing()

    assert m_1 == m_2
    assert not m_1 == m_3
    assert not m_1 == m_4
    assert m_2 == m_1
    assert not m_2 == m_3
    assert not m_2 == m_4
    assert not m_3 == m_1
    assert not m_3 == m_2
    assert not m_3 == m_4
    assert not m_4 == m_1
    assert not m_4 == m_2
    assert not m_4 == m_3

    assert "just(1)" == str(m_1)

# Generated at 2022-06-14 03:37:43.073913
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value > 1

    assert Maybe.just(2).filter(filterer) == Maybe.just(2)
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()
    assert Maybe.just(1).filter(filterer) == Maybe.nothing()



# Generated at 2022-06-14 03:37:44.576702
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    # given
    maybe = Maybe.nothing()

    # when
    lazy = maybe.to_lazy()

    # then
    assert lazy.force() == None



# Generated at 2022-06-14 03:37:49.844160
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    test_cases = [
        (Maybe.just(1), Maybe.just(1), True),
        (Maybe.just(2), Maybe.just(1), False),
        (Maybe.just(2), Maybe.nothing(), False),
        (Maybe.nothing(), Maybe.nothing(), True)
    ]

    for monad, other, result in test_cases:
        assert monad == other == result


# Generated at 2022-06-14 03:37:56.074389
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)
    assert Maybe.just(None) == Maybe.just(None)

# Generated at 2022-06-14 03:38:02.353191
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe.just(1.0)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:38:09.821787
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test of method filter of class Maybe

    :returns: None
    """

    srcMaybe = Maybe.just(5)

    filteredMaybe = srcMaybe.filter(lambda x: x % 2 == 0)

    assert filteredMaybe == Maybe.nothing()

    srcMaybe = Maybe.just(4)

    filteredMaybe = srcMaybe.filter(lambda x: x % 2 == 0)

    assert filteredMaybe == Maybe.just(4)

# Generated at 2022-06-14 03:38:17.751141
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != 1



# Generated at 2022-06-14 03:38:22.718820
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert (Maybe.just(1) == Maybe.just(1)) == True
    assert (Maybe.just("Any text") == Maybe.just("Another text")) == False
    assert (Maybe.just(1) == Maybe.nothing()) == False
    assert (Maybe.nothing() == Maybe.nothing()) == True
    assert (Maybe.just("Any text") == "Any text") == False



# Generated at 2022-06-14 03:38:33.840326
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.auxiliary import identity
    assert Maybe.just(4).to_lazy() == Lazy(lambda: 4)
    assert Maybe.just(4).to_lazy().map(identity) == Lazy(lambda: 4)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.nothing().to_lazy().map(identity) == Lazy(lambda: None)



# Generated at 2022-06-14 03:38:40.282097
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    '''
    >>> from pymonet.maybe import Maybe, Lazy
    >>> a1 = Maybe.just(lambda: 'Hello')
    >>> a2 = Maybe.nothing()
    >>> [a1.to_lazy(), a2.to_lazy()]
    [Lazy(function at 0x000001C28101B620), Lazy(function at 0x000001C28101B598)]
    '''
    pass


# Generated at 2022-06-14 03:38:45.819197
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:38:52.608883
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # case when filterer returns False
    nothing = Maybe.nothing()
    assert nothing.filter(lambda x: x > 5) == Maybe.nothing()
    assert nothing.filter(lambda x: x < 5) == Maybe.nothing()

    # case when filterer returns True for empty Maybe
    some_empty = Maybe.just(None)
    assert some_empty.filter(lambda x: True) == Maybe.nothing()
    assert some_empty.filter(lambda x: False) == Maybe.nothing()

    # case when filterer returns True
    assert Maybe.just(2).filter(lambda x: x < 5) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x > 5) == Maybe.nothing()


# Generated at 2022-06-14 03:39:00.423573
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('1') == Maybe.just('1')
    assert Maybe.just('1') != Maybe.just('2')
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(lambda x: x) == Maybe.just(lambda x: x)
    assert Maybe.just(lambda x: x) != Maybe.just(lambda y: y)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('1')
    # TODO: check if types are different
    # assert Maybe.just('1') != Maybe.nothing()



# Generated at 2022-06-14 03:39:05.007355
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(0) == Maybe.just(0)
    assert Maybe.just(0) != Maybe.just(1)
    assert Maybe.just(0) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(None) != Maybe.just(0)
    assert Maybe.just(None) == Maybe.just(None)


# Generated at 2022-06-14 03:39:09.972566
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(5).filter(lambda x: x > 3) == Maybe.just(5)
    assert Maybe.just(2).filter(lambda x: x > 3) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()

# Generated at 2022-06-14 03:39:17.932717
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, False) != Maybe(2, True)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, True) != Maybe(2, False)


# Generated at 2022-06-14 03:39:29.564819
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(5)
    assert maybe.filter(lambda x: x > 4) == Maybe.just(5)
    assert maybe.filter(lambda x: x > 5) == Maybe.nothing()

    maybe1 = Maybe.just('asd')
    assert maybe1.filter(lambda x: x == 'asd') == Maybe.just('asd')
    assert maybe1.filter(lambda x: x > 'asd') == Maybe.nothing()

    maybe2 = Maybe.just('5')
    assert maybe2.filter(lambda x: x == 5) == Maybe.nothing()
    assert maybe2.filter(lambda x: x == '5') == Maybe.just('5')

    maybe3 = Maybe.just('5')
    assert maybe3.filter(lambda x: x > 4) == Maybe.just('5')
    assert maybe

# Generated at 2022-06-14 03:39:33.928280
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(3)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:45.507343
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert_that(Maybe.just("value")).is_equal_to(Maybe.just("value"))
    assert_that(Maybe.nothing()).is_equal_to(Maybe.nothing())
    assert_that(Maybe.just("value")).not_equal_to(Maybe.just("value1"))
    assert_that(Maybe.just("value")).not_equal_to(Maybe.nothing())
    assert_that(Maybe.nothing()).not_equal_to(Maybe.just("value"))



# Generated at 2022-06-14 03:39:48.983817
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:39:55.723322
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    maybe1 = Maybe.just(1)
    maybe2 = Maybe.just(2)
    maybe3 = Maybe.just(3)
    maybe4 = Maybe.nothing()
    maybe5 = Maybe.nothing()
    assert maybe1 == maybe1
    assert not maybe1 == maybe2
    assert not maybe2 == maybe3
    assert maybe4 == maybe4
    assert not maybe4 == maybe5
    assert not maybe4 == maybe1
    assert not maybe1 == nothing()


# Generated at 2022-06-14 03:40:03.107906
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Test for empty Maybe
    assert Maybe.nothing().filter(lambda a: True) == Maybe.nothing()
    # Test for empty Maybe if filterer returns False
    assert Maybe.just(1).filter(lambda a: a > 1) == Maybe.nothing()
    # Test if filterer returns True
    assert Maybe.just(1).filter(lambda a: a == 1) == Maybe.just(1)
    # Test for Maybe with None value
    assert Maybe.just(None).filter(lambda a: a is None) == Maybe.just(None)


# Generated at 2022-06-14 03:40:10.117325
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # Given
    maybe_value = Maybe.just(5)
    maybe_no_value = Maybe.nothing()
    # When
    maybe_value_filtered = maybe_value.filter(lambda x: x == 2)
    maybe_no_value_filtered = maybe_no_value.filter(lambda x: x == 2)
    # Then
    assert maybe_value_filtered == Maybe.nothing()
    assert maybe_no_value_filtered == Maybe.nothing()


# Generated at 2022-06-14 03:40:17.224870
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.just('a')


# Generated at 2022-06-14 03:40:18.599468
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('1') != 1



# Generated at 2022-06-14 03:40:25.073391
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)



# Generated at 2022-06-14 03:40:27.909546
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:40:29.896534
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:40:38.428103
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1.0) == Maybe.just(1.0)
    assert Maybe.just(1.0) != Maybe.just(2.0)
    assert Maybe.just(1.0) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:40:41.627084
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)


# Generated at 2022-06-14 03:40:45.614172
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just('test').to_lazy() == Lazy(lambda: 'test')
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:40:52.459929
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result = Maybe.just(42).filter(lambda x: x % 2 == 0)
    expected = Maybe.just(42)
    assert result == expected

    result = Maybe.just(42).filter(lambda x: x % 3 == 0)
    expected = Maybe.nothing()
    assert result == expected

    result = Maybe.nothing().filter(lambda x: x % 2 == 0)
    expected = Maybe.nothing()
    assert result == expected


# Generated at 2022-06-14 03:41:00.397698
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.functor import Functor
    from pymonet.applicative import Applicative

    class TestFunctor(Functor[T]):
        def __init__(self, value: T) -> None:
            self.value = value

        def map(self, mapper: Callable[[T], U]) -> 'TestFunctor[U]':
            return TestFunctor(mapper(self.value))

    class TestApplicative(Applicative[T]):
        def __init__(self, value: T) -> None:
            self.value = value

        def map(self, mapper: Callable[[T], U]) -> 'TestApplicative[U]':
            return TestApplicative(mapper(self.value))

        def ap(self, applicative):
            return applicative.map(self.value)



# Generated at 2022-06-14 03:41:08.708860
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    class TestClass:
        def __init__(self, value: int) -> None:
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    test_1 = Maybe.just(TestClass(4)).filter(lambda test: test.value == 4)
    assert test_1 == Maybe.just(TestClass(4))

    test_2 = Maybe.just(TestClass(4)).filter(lambda test: test.value == 5)
    assert test_2 == Maybe.nothing()

    test_3 = Maybe.nothing().filter(lambda test: test.value == 5)
    assert test_3 == Maybe.nothing()



# Generated at 2022-06-14 03:41:16.494516
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    No unittest for constructor __init__.

    >>> Maybe.just(1).__eq__(Maybe.just(1))
    True

    >>> Maybe.just(1).__eq__(Maybe.just(2))
    False

    >>> Maybe.nothing().__eq__(Maybe.nothing())
    True

    >>> Maybe.just(1).__eq__(Maybe.nothing())
    False
    """
    pass



# Generated at 2022-06-14 03:41:27.508982
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just({}) == Maybe.just({})
    assert Maybe.just({}) != Maybe.just(object())
    assert Maybe.just({}) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just(True) != Maybe.just(False)
    assert Maybe.just(True) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
