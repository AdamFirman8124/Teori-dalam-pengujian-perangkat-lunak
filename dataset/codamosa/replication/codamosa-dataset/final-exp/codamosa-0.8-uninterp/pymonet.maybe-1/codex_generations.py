

# Generated at 2022-06-14 03:31:34.150368
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Test Maybe class method to_lazy.

    :return: None
    """
    from pymonet.lazy import Lazy

    assert Maybe.just(4).to_lazy() == Lazy(lambda: 4)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:31:41.440103
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    funcs = [
        lambda func: func(42).filter(lambda x: x % 2 == 0),
        lambda func: func(42).filter(lambda x: x % 5 == 0)
    ]
    results = [
        42,
        Maybe.nothing()
    ]
    for i in range(len(funcs)):
        assert funcs[i](Maybe.just) == results[i]


# Generated at 2022-06-14 03:31:45.127002
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:31:51.085563
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.nothing() != Maybe.just(None)
    assert Maybe.just(2) != Maybe.just(5)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.just(2) != 2
    assert Maybe.just(2) != Maybe(2, False)



# Generated at 2022-06-14 03:31:59.946749
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    first_just = Maybe.just(42)
    second_just = Maybe.just(10)
    nothing = Maybe.nothing()

    assert first_just.filter(lambda x: x > 40) == Maybe.just(42)
    assert second_just.filter(lambda x: x > 40) == Maybe.nothing()
    assert nothing.filter(lambda x: x > 40) == Maybe.nothing()



# Generated at 2022-06-14 03:32:03.989829
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    m = Maybe.just(1)
    l = m.to_lazy()
    assert l.force() == 1

    m = Maybe.nothing()
    l = m.to_lazy()
    assert l.force() is None


# Generated at 2022-06-14 03:32:08.201149
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda val: val > 1) == Maybe.just(2)
    assert Maybe.just(1).filter(lambda val: val > 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda val: val > 1) == Maybe.nothing()



# Generated at 2022-06-14 03:32:14.618694
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    just_value: Maybe[int] = Maybe.just(17)
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.either import Either

    # success test
    assert just_value.filter(lambda x: x < 20) == Maybe.just(17)
    assert just_value.filter(lambda x: x < 5) == Maybe.nothing()
    # failure test
    assert just_value.filter(lambda x: False) == Maybe.nothing()
    assert just_value.filter(lambda x: True) == Maybe.just(17)


# Generated at 2022-06-14 03:32:19.151815
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(5) != 5


# Generated at 2022-06-14 03:32:24.722233
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert (
        Maybe.just(1) == Maybe.just(1) and
        Maybe.nothing() == Maybe.nothing() and
        Maybe.just(1) != Maybe.nothing() and
        Maybe.nothing() != Maybe.just(1)
    )


# Generated at 2022-06-14 03:32:34.520539
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test Maybe filter method.

    :returns: None
    """
    def filter_fn(value):
        return value % 2 == 0

    assert(Maybe.just(2).filter(filter_fn) == Maybe.just(2))
    assert(Maybe.just(1).filter(filter_fn) == Maybe.nothing())
    assert(Maybe.nothing().filter(filter_fn) == Maybe.nothing())



# Generated at 2022-06-14 03:32:37.648461
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just("foo") == Maybe.just("foo")
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just("foo") != Maybe.nothing()



# Generated at 2022-06-14 03:32:41.578597
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:32:45.493481
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def test_func(arg):
        if arg % 2 == 0:
            return True
        return False

    result = Maybe.just(2) \
        .filter(test_func)

    expected = Maybe.just(2)

    assert result == expected



# Generated at 2022-06-14 03:32:57.087529
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Test for method __eq__ of class Maybe.
    """
    assert Maybe(1, False) == Maybe(1, False)
    assert Maybe(1, True) == Maybe(1, True)
    assert Maybe(1, False) != Maybe(2, False)
    assert Maybe(1, True) != Maybe(2, True)
    assert Maybe(1, False) != Maybe(1, True)
    assert Maybe(1, True) != Maybe(1, False)
    assert Maybe(1, False) != Maybe(2, True)
    assert Maybe(1, True) != Maybe(2, False)
    assert Maybe(1, False) != Maybe([1], False)
    assert Maybe([1], False) != Maybe(1, False)
    assert Maybe(1, False) != Maybe([1], True)

# Generated at 2022-06-14 03:33:00.919492
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()



# Generated at 2022-06-14 03:33:05.744133
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x > 1) == Maybe.just(2)
    assert Maybe.just(2).filter(lambda x: x < 1) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 1) == Maybe.nothing()

# Generated at 2022-06-14 03:33:10.673437
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != 1


# Generated at 2022-06-14 03:33:15.625762
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:33:22.682056
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    def eq_test(test_case, a, b, true_or_false):
        assert (a == b) is true_or_false, \
            '{} == {} is {}'.format(a, b, true_or_false)

    eq_test('test 1', Maybe.just(1), Maybe.just(1), True)
    eq_test('test 2', Maybe.just(1), Maybe.just(2), False)
    eq_test('test 3', Maybe.just(1), Maybe.nothing(), False)
    eq_test('test 4', Maybe.nothing(), Maybe.nothing(), True)


# Generated at 2022-06-14 03:33:31.606841
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) == Maybe.just(2).map(lambda x: x)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(2)



# Generated at 2022-06-14 03:33:35.451250
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(10) == Maybe.just(10)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(10) != Maybe.nothing()
    assert Maybe.just(10) != Maybe.just(20)


# Generated at 2022-06-14 03:33:41.051400
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    maybe = Maybe.just(1).filter(lambda value: value % 2 == 0)
    assert maybe == Maybe.nothing()

    maybe = Maybe.just(2).filter(lambda value: value % 2 == 0)
    assert maybe == Maybe.just(2)

    maybe = Maybe.nothing().filter(lambda value: value % 2 == 0)
    assert maybe == Maybe.nothing()


# Generated at 2022-06-14 03:33:44.222013
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(1, False) == Maybe(1, False)

    assert Maybe(1, False) != Maybe(1.1, False)
    assert Maybe(1, False) != Maybe(1, True)


# Generated at 2022-06-14 03:33:49.287014
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # filter for not empty Maybe
    assert Maybe.just(1).filter(lambda x: x == 1) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x == 2) == Maybe.nothing()

    # filter for empty Maybe
    assert Maybe.nothing().filter(lambda x: x == 2) == Maybe.nothing()

# Generated at 2022-06-14 03:33:53.121067
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert isinstance(Maybe.just(3), Maybe)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)


# Generated at 2022-06-14 03:34:04.045068
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.validation import Validation

    assert Maybe.just(None).filter(lambda _: True).get_or_else(None) == None
    assert Maybe.just(None).filter(lambda _: False).get_or_else(None) == None
    assert Maybe.nothing().filter(lambda _: True).get_or_else(None) == None
    assert Maybe.nothing().filter(lambda _: False).get_or_else(None) == None

    assert Maybe.just(Validation.success(None)).filter(lambda value: value.is_success).get_or_else(None) == Validation.success(None)
    assert Maybe.just(Validation.success(None)).filter(lambda value: not value.is_success).get_or_else(None) == None



# Generated at 2022-06-14 03:34:10.408353
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just("something") == Maybe.just("something")
    assert Maybe.just("something") != Maybe.just("nothing")
    assert Maybe.just(1) != Maybe.just("nothing")
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1) or Maybe.nothing() != Maybe.just("nothing")



# Generated at 2022-06-14 03:34:16.164037
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # test with given value
    assert Maybe.just(5) == Maybe.just(5)
    # test with none
    assert Maybe.nothing() == Maybe.nothing()
    # test if empty
    assert Maybe.nothing() != Maybe.just(5)
    assert Maybe.just(5) != Maybe.nothing()
    # test if different
    assert Maybe.just(1) != Maybe.just(2)


# Generated at 2022-06-14 03:34:20.827829
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    def compare_maybe(m1, m2):
        return (m1.is_nothing, m1.__getattribute__('value')) \
                == (m2.is_nothing, m2.__getattribute__('value'))

    assert compare_maybe(Maybe.just(4), Maybe.just(4)) == True
    assert compare_maybe(Maybe.just(4), Maybe.just(5)) == False
    assert compare_maybe(Maybe.just('hello'), Maybe.just('hello')) == True
    assert compare_maybe(Maybe.just('hello'), Maybe.just('world')) == False
    assert compare_maybe(Maybe.nothing(), Maybe.just(4)) == False
    assert compare_maybe(Maybe.nothing(), Maybe.just('hello')) == False
    assert compare_maybe(Maybe.nothing(), Maybe.nothing()) == True

# Generated at 2022-06-14 03:34:25.720103
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:34:29.469321
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != True


# Generated at 2022-06-14 03:34:35.740600
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    m = Maybe.just(1)
    n = Maybe.just(2)
    l = Maybe.nothing()
    assert (m == m) and not (m == n) and not (m == l) and not (n == m) and (n == n) and not (n == l) and not (l == m) and not (l == n) and (l == l)



# Generated at 2022-06-14 03:34:38.984223
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:34:43.762803
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: True) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: True) != Maybe.just(4)
    assert Maybe.just(3).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()



# Generated at 2022-06-14 03:34:47.724743
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x < 0) == Maybe.nothing()

# Generated at 2022-06-14 03:34:52.704165
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.just(3).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:34:58.361737
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()


# Generated at 2022-06-14 03:35:02.017227
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:35:06.075549
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    func = lambda t: True if t % 2 == 0 else False
    assert Maybe.just(2).filter(func) == Maybe.just(2)
    assert Maybe.just(3).filter(func) == Maybe.nothing()
    assert Maybe.nothing().filter(func) == Maybe.nothing()



# Generated at 2022-06-14 03:35:16.581331
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.either import Left

    test_cases = {
        Left(None): Left(None),
        Maybe.just(None): Maybe.nothing(),
        Maybe.just(3): Maybe.just(3),
        Maybe.just(True): Maybe.just(True),
        Maybe.nothing(): Maybe.nothing(),
    }

    for maybe, result in test_cases.items():
        assert maybe.filter(lambda x: x is not None) == result



# Generated at 2022-06-14 03:35:21.747213
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()


# Generated at 2022-06-14 03:35:27.947263
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result = (Maybe.just(1)
              .filter(lambda x: x >= 0)
              .get_or_else(-1))
    assert(result == 1)

    result = (Maybe.just(-1)
              .filter(lambda x: x >= 0)
              .get_or_else(-2))
    assert(result == -2)

    result = (Maybe.nothing()
              .filter(lambda x: x >= 0)
              .get_or_else(-3))
    assert(result == -3)



# Generated at 2022-06-14 03:35:30.855587
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x % 2 == 0) == Maybe.nothing()
    assert Maybe.just(2).filter(lambda x: x % 2 == 0) == Maybe.just(2)
    assert Maybe.nothing().filter(lambda x: x % 2 == 0) == Maybe.nothing()

# Generated at 2022-06-14 03:35:34.078280
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    def some_fun():
        return 'a'
    assert Maybe.just(some_fun).to_lazy().force() == 'a'
    assert Maybe.nothing().to_lazy().force() is None


# Generated at 2022-06-14 03:35:37.791945
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    """
    Test for check method __eq__ of class Maybe.

    :return: nothing
    """
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.just(6) != Maybe.just(5)
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:35:48.988273
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # should return non-empty Maybe after filter
    print(Maybe.just(1).filter(lambda x: x < 5))
    print(Maybe.just(1).filter(lambda x: x < 5).value == 1)
    print(Maybe.just(1).filter(lambda x: x > 5))
    print(Maybe.just(1).filter(lambda x: x > 5).is_nothing)
    # should return empty Maybe after filter
    print(Maybe.just(1).filter(lambda x: x > 5))
    print(Maybe.just(1).filter(lambda x: x > 5).is_nothing)
    print(Maybe.nothing().filter(lambda x: True))
    print(Maybe.nothing().filter(lambda x: True).is_nothing)
    print(Maybe.nothing().filter(lambda x: False))

# Generated at 2022-06-14 03:35:56.732144
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just('a') == Maybe.just('a')
    assert Maybe.just('a') != Maybe.just('b')
    assert Maybe.just('a') != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just('a')
    assert Maybe.nothing() != Maybe.just('b')

# Unit tests for method just of class Maybe

# Generated at 2022-06-14 03:35:59.937865
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just([1]) != Maybe.just([1, 2])
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:36:07.065556
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    with pytest.raises(AssertionError):
        Maybe.nothing() == 'a'

    assert Maybe.nothing() == Maybe.nothing()

    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(5)
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.just(3) != Maybe.just('3')



# Generated at 2022-06-14 03:36:14.245193
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(4)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)



# Generated at 2022-06-14 03:36:18.480876
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(2) != Maybe.just(3)
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:36:21.364699
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()


# Generated at 2022-06-14 03:36:26.070400
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(None) == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) == Maybe.just(2)


# Generated at 2022-06-14 03:36:31.659846
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: True) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: False) == Maybe.nothing()

    assert Maybe.nothing().filter(lambda x: True) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()


# Generated at 2022-06-14 03:36:35.594693
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just("String")
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:36:38.948232
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:36:43.230823
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(3) == Maybe.just(3)
    assert Maybe.just(3) != Maybe.just(4)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(3) != Maybe.nothing()



# Generated at 2022-06-14 03:36:54.739099
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    from pymonet.box import Box

    m = Maybe.just(3)
    s = "3"
    assert m == m
    assert m != s

    m1 = Maybe.just('1')
    m2 = Maybe.just('2')
    m3 = Maybe.just('1')
    n1 = Maybe.nothing()
    n2 = Maybe.nothing()
    n3 = Maybe.nothing()

    assert m1 == m1
    assert m1 == m3
    assert m1 != m2
    assert m2 != m3
    assert m2 != n1

    assert n1 == n1
    assert n1 == n3
    assert n1 != n2

    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(3)
    assert Maybe.nothing() != Maybe.just

# Generated at 2022-06-14 03:37:00.345121
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():

    assert Maybe.just('str') == Maybe.just('str')
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just('str').get_or_else('str') == 'str'
    assert Maybe.nothing().get_or_else('str') == 'str'



# Generated at 2022-06-14 03:37:16.439971
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    import pytest

    def test_function():
        maybe = Maybe.just(10)
        assert maybe.to_lazy().call() == 10

    def test_function_with_nothing():
        maybe = Maybe.nothing()
        with pytest.raises(TypeError) as e_info:
            assert maybe.to_lazy().call() == Maybe.nothing()
        assert 'Maybe has nothing' in str(e_info.value)

    test_function()
    test_function_with_nothing()


# Generated at 2022-06-14 03:37:27.233895
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just("Hello") == Maybe.just("Hello")
    assert Maybe.just(None) == Maybe.just(None)
    assert Maybe.just(True) != Maybe.just(False)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just("Hello") != Maybe.just("World")
    assert Maybe.just(None) != Maybe.just("Hello")
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just("Hey")
    assert Maybe.just("Hey") != Maybe.nothing()
    assert Maybe.just("Hey") != 1
    maybe = Maybe.just("Hey")
    assert maybe == maybe


# Unit tests

# Generated at 2022-06-14 03:37:30.922235
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    # case: empty maybe
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

    # case: not empty maybe
    assert Maybe.just(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:37:35.971001
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    # Test when values are equal and when they are not
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) != Maybe.just(1)

    # Test for empty Maybe
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:37:39.053075
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    result = Maybe.just(5).filter(lambda value: value == 5)

    expected_result = Maybe.just(5)

    assert result.__eq__(expected_result)



# Generated at 2022-06-14 03:37:43.760719
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.nothing().filter(lambda x: x == 2) == Maybe.nothing()
    assert Maybe.just(5).filter(lambda x: x == 5) == Maybe.just(5)
    assert Maybe.just(5).filter(lambda x: x == 2) == Maybe.nothing()



# Generated at 2022-06-14 03:37:46.876665
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()

# Generated at 2022-06-14 03:37:49.809268
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(45) == Maybe.just(45)
    assert Maybe.just(45) != Maybe.just(34)
    assert Maybe.just(45) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:37:54.082690
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(42).to_lazy() == Lazy(lambda: 42)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:38:01.639735
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    actual = Maybe.just(1) == Maybe.just(1)
    assert actual
    actual = Maybe.just(1) == Maybe.just(2)
    assert not actual
    actual = Maybe.just(1) == Maybe.nothing()
    assert not actual
    actual = Maybe.nothing() == Maybe.nothing()
    assert actual
    actual = Maybe.nothing() == Maybe.just(1)
    assert not actual



# Generated at 2022-06-14 03:38:17.687317
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)



# Generated at 2022-06-14 03:38:19.623317
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)


# Generated at 2022-06-14 03:38:24.414649
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    x = Maybe.just(5)
    y = x.to_lazy()

    assert isinstance(y, Lazy)
    assert y.value() == 5


# Generated at 2022-06-14 03:38:29.954619
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Test case for testing filter method of Maybe.
    """
    value = Maybe.just(1)
    empty = Maybe.nothing()
    assert 1 == value.filter(lambda x: True).get_or_else(None)
    assert empty.filter(lambda x: True).get_or_else(None) is None

# Generated at 2022-06-14 03:38:35.212956
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(True) == Maybe.just(True)
    assert Maybe.just(True) != Maybe.just(False)
    assert Maybe.just(True) != None
    assert Maybe.just(True) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:38:39.674059
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(lambda x: x > 0) == Maybe.just(1)
    assert Maybe.just(1).filter(lambda x: x > 2) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: x > 2) == Maybe.nothing()



# Generated at 2022-06-14 03:38:50.035443
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate
    from pymonet.predicate import Predicate

# Generated at 2022-06-14 03:38:55.015386
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.just(6)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()



# Generated at 2022-06-14 03:38:58.698741
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    result = Maybe.just(21).to_lazy()
    assert result.value() == 21


# Generated at 2022-06-14 03:39:02.154094
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() != Maybe.just(None)


# Generated at 2022-06-14 03:39:16.530888
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Check function to_lazy of class Maybe.

    :return: None
    """
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 03:39:20.152574
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(5) == Maybe.just(5)
    assert Maybe.just(5) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:24.183328
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:29.325117
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert isinstance(Maybe.just(1), Maybe)
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:39:34.644478
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(4) == Maybe.just(4)
    assert Maybe.just(4) != Maybe.just(3)
    assert Maybe.just(4) != Maybe.just(None)
    assert Maybe.just(4) != Maybe.nothing()


# Generated at 2022-06-14 03:39:41.100866
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe(5, False) == Maybe(5, False)
    assert not (Maybe(5, False) == Maybe(None, False))
    assert not (Maybe(5, False) == Maybe(5, True))
    assert Maybe(None, True) == Maybe(None, True)
    assert not (Maybe(None, True) == Maybe(None, False))


# Generated at 2022-06-14 03:39:45.769894
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:39:51.078975
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.just(2) == Maybe.just(2)
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.just(1) != Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:39:55.402468
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert Maybe.nothing() == Maybe.nothing()
    assert Maybe.just(2) != Maybe.nothing()
    assert Maybe.just(1) != Maybe.just(2)
    assert Maybe.nothing() != Maybe.just(1)


# Generated at 2022-06-14 03:39:59.675219
# Unit test for method __eq__ of class Maybe
def test_Maybe___eq__():
    assert Maybe.just(1) == Maybe.just(1)
    assert not Maybe.just(1) == Maybe.just(2)
    assert not Maybe.just(1) == Maybe.nothing()
    assert Maybe.nothing() == Maybe.nothing()


# Generated at 2022-06-14 03:40:22.624112
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    # GIVEN
    maybe_with_value = Maybe.just(5)
    maybe_without_value = Maybe.nothing()

    # WHEN
    result_with_true_filterer = maybe_with_value.filter(lambda val: val == 5)
    result_with_false_filterer = maybe_with_value.filter(lambda val: val == 6)
    result_with_filterer_for_empty = maybe_without_value.filter(lambda val: val == 5)

    # THEN
    assert result_with_true_filterer == Maybe.just(5)
    assert result_with_false_filterer == Maybe.nothing()
    assert result_with_filterer_for_empty == Maybe.nothing()



# Generated at 2022-06-14 03:40:28.642124
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(3).filter(lambda x: True) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x > 1) == Maybe.just(3)
    assert Maybe.just(3).filter(lambda x: x == 1) == Maybe.nothing()
    assert Maybe.just(3).filter(lambda x: False) == Maybe.nothing()
    assert Maybe.nothing().filter(lambda x: False) == Maybe.nothing()


# Generated at 2022-06-14 03:40:36.147205
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    """
    Unit test for method filter of class Maybe.

    :returns: true if test passed else false
    :rtype: Boolean
    """
    predicate = lambda x: x > 10
    maybe_number = Maybe.just(15)
    maybe_number_2 = Maybe.just(5)
    maybe_number_3 = Maybe.nothing()

    assert maybe_number.filter(predicate) == Maybe.just(15)
    assert maybe_number_2.filter(predicate) == Maybe.nothing()
    assert maybe_number_3.filter(predicate) == Maybe.nothing()



# Generated at 2022-06-14 03:40:42.631389
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    assert Maybe.just(1).filter(
        lambda x: x == 1
    ) == Maybe.just(1)

    assert Maybe.just(1).filter(
        lambda x: x != 1
    ) == Maybe.nothing()

    assert Maybe.nothing().filter(
        lambda x: x == 1
    ) == Maybe.nothing()


# Generated at 2022-06-14 03:40:47.042799
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert Maybe.just(42).to_lazy() == Lazy(lambda: 42)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:40:57.896798
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.box import Box
    from pymonet.either import Right, Left
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    assert Maybe.just(1).to_lazy() == Lazy(lambda: 1)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
    assert Maybe.just(1).to_box() == Box(1)
    assert Maybe.nothing().to_box() == Box(None)
    assert Maybe.just(1).to_either() == Right(1)
    assert Maybe.nothing().to_either() == Left(None)
    assert Maybe.just(1).to_try() == Try(1, is_success=True)

# Generated at 2022-06-14 03:41:03.589335
# Unit test for method filter of class Maybe
def test_Maybe_filter():
    def filterer(value):
        return value > 2

    assert Maybe.just(3).filter(filterer) == Maybe.just(3)
    assert Maybe.just(1).filter(filterer) == Maybe.nothing()
    assert Maybe.nothing().filter(filterer) == Maybe.nothing()


# Generated at 2022-06-14 03:41:06.796542
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    """
    Unit test for method to_lazy of class Maybe.
    """

    assert Maybe.just(1).to_lazy().force() == 1
    assert Maybe.nothing().to_lazy().force() is None


# Generated at 2022-06-14 03:41:09.200064
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    assert(Maybe.just(3).to_lazy() == Lazy(lambda: 3))
    assert(Maybe.nothing().to_lazy() == Lazy(lambda: None))


# Generated at 2022-06-14 03:41:15.270552
# Unit test for method to_lazy of class Maybe
def test_Maybe_to_lazy():
    from pymonet.lazy import Lazy

    def function() -> int:
        return 2
    assert Maybe.just(function).to_lazy() == Lazy(function)
    assert Maybe.nothing().to_lazy() == Lazy(lambda: None)
