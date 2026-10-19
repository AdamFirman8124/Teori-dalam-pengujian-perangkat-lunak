

# Generated at 2022-06-14 03:44:26.921459
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x <= 4

    def filterer_1(x):
        return x < 4

    assert Try(3, True).filter(filterer) == Try(3, True)
    assert Try(3, True).filter(filterer_1) == Try(3, False)



# Generated at 2022-06-14 03:44:34.991486
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    from random import randint
    base = [Try.of(lambda: randint(-10, 10)), Try.of(lambda: randint(-10, 10)), Try.of(lambda: randint(-10, 10))]
    positive = filter(lambda a: a >= 0, base)
    negative = filter(lambda a: a < 0, base)
    assert all(isinstance(x, Try) for x in positive)
    assert all(isinstance(x, Try) for x in negative)
    assert all(x.is_success for x in positive)
    assert all(x.is_success for x in negative)
    assert all(x.get() >= 0 for x in positive)
    assert all(x.get() < 0 for x in negative)
    raise ValueError()


# Generated at 2022-06-14 03:44:37.360657
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda x: x == 42) == Try(42, True)
    assert Try(42, True).filter(lambda x: x != 42) == Try(42, False)
    assert Try(Exception('Oops!'), False).filter(lambda x: x == 42) == Try(Exception('Oops!'), False)



# Generated at 2022-06-14 03:44:41.077841
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, False).filter(lambda value: value % 2 == 0) == Try(42, False)
    assert Try(42, True).filter(lambda value: value % 2 == 0) == Try(42, True)
    assert Try(42, True).filter(lambda value: value % 2 != 0) == Try(42, False)


# Generated at 2022-06-14 03:44:50.065695
# Unit test for method filter of class Try
def test_Try_filter():
    """
    :returns: True if all assertions passed, otherwise raise AssertionError exception
    :rtype: bool
    """
    def filterer(value):
        return value < 100

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(1, False).filter(filterer) == Try(1, False)
    assert Try(200, True).filter(filterer) == Try(200, False)
    return True


# Generated at 2022-06-14 03:44:58.393427
# Unit test for method filter of class Try
def test_Try_filter():
    m1 = Try.of(lambda: 10)  # Try[value=10, is_success=True]
    n1 = m1.filter(lambda x: x < 5)  # Try[value=10, is_success=False]
    assert isinstance(n1, Try)
    assert n1.is_success == False
    assert n1.value == 10

    m2 = Try.of(lambda: 1/0)  # Try[value=Exception("division by zero"), is_success=False]
    n2 = m2.filter(lambda x: False)  # Try[value=Exception("division by zero"), is_success=False]
    assert isinstance(n2, Try)
    assert n2.is_success == False


# Generated at 2022-06-14 03:45:01.763260
# Unit test for method filter of class Try
def test_Try_filter():
    result = None
    def filterer(a):
        nonlocal result
        result = a
        return False

    result_try = Try(1, True)\
        .filter(filterer)

    assert result == 1
    assert result_try == Try(1, False)



# Generated at 2022-06-14 03:45:09.462092
# Unit test for method filter of class Try
def test_Try_filter():
    f = lambda x: x*2

    actual = Try.of(f, 2).filter(lambda x: x == 4)
    expected = Try(4, True)
    assert actual == expected

    actual = Try.of(f, 2).filter(lambda x: x != 4)
    expected = Try(4, False)
    assert actual == expected


# Generated at 2022-06-14 03:45:16.178146
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(1, lambda: 0) == Try(0, True)
    assert Try.of(1, lambda: 1/0) == Try(ZeroDivisionError(), False)
    assert Try.of(1, lambda: 0).filter(lambda x: False) == Try(0, False)
    assert Try.of(1, lambda: 0).filter(lambda x: True) == Try(0, True)
    assert Try.of(1, lambda: 1/0).filter(lambda x: False) == Try(ZeroDivisionError(), False)
    assert Try.of(1, lambda: 1/0).filter(lambda x: True) == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:45:28.521505
# Unit test for method filter of class Try
def test_Try_filter():  # type: () -> None
    assert(Try.of(lambda x: x, 1).filter(lambda x: x == 1) == Try(1, True))
    assert(Try.of(lambda x: x, 1).filter(lambda x: x == 2) == Try(1, False))
    assert(Try.of(lambda x: 1 // x, 2).filter(lambda x: x == 1) == Try(ZeroDivisionError('division by zero'), False))
    assert(Try.of(lambda x: 1 // x, 2).map(lambda x: 1).filter(lambda x: x == 1) == Try(ZeroDivisionError('division by zero'), False))



# Generated at 2022-06-14 03:45:39.512527
# Unit test for method filter of class Try
def test_Try_filter():
    try_1 = Try.of(lambda: [1, 2, 3])
    try_2 = Try.of(lambda: [1, 2, 3, 4])
    try_3 = Try.of(lambda: [1, 2, 3, 4, 5])
    try_5 = Try.of(lambda: [])
    try_6 = Try.of(lambda: "")
    assert try_1.filter(lambda x: len(x) < 4) == Try([1, 2, 3], True)
    assert try_1.filter(lambda x: len(x) > 3) == Try([1, 2, 3], False)
    assert try_2.filter(lambda x: len(x) < 4) == Try([1, 2, 3, 4], False)

# Generated at 2022-06-14 03:45:49.739260
# Unit test for method filter of class Try
def test_Try_filter():
    class TestException(Exception):
        pass

    def tester_exc():
        raise TestException()

    def tester_ok():
        return True

    def less_than_zero(v):
        return v < 0

    assert Try.of(tester_ok).filter(less_than_zero) \
        == Try(None, True)

    assert Try.of(tester_ok).filter(lambda v: v == True) \
        == Try(None, True)

    assert Try.of(tester_exc).filter(less_than_zero) \
        == Try(TestException(), False)

    assert Try.of(lambda: -5).filter(less_than_zero) \
        == Try(-5, True)

    assert Try.of(lambda: 5).filter(less_than_zero) \
        == Try

# Generated at 2022-06-14 03:46:01.622138
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        if x > 10:
            return True
        return False

    def filterer_with_exception(x):
        raise Exception()

    # filter success
    assert Try(Try.of(lambda: 11), True).filter(filterer) == Try(Try(11, True), True)
    assert Try(Try.of(lambda: 10), True).filter(filterer) == Try(Try.of(lambda: 10).value, False)
    # filter failed
    assert Try(Try.of(lambda: 11), False).filter(filterer) == Try(Try.of(lambda: 11).value, False)
    assert Try(Try.of(lambda: 10), False).filter(filterer) == Try(Try.of(lambda: 10).value, False)

    # raise exceptions filter


# Generated at 2022-06-14 03:46:05.770687
# Unit test for method filter of class Try
def test_Try_filter():
    def even(value):
        return value % 2 == 0

    assert (Try(1, True).filter(even) == Try(1, False))
    assert (Try(2, True).filter(even) == Try(2, True))



# Generated at 2022-06-14 03:46:11.597410
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 'Success').filter(lambda value: value == 'Success') == Try('Success', True)
    assert Try.of(lambda: 'Success').filter(lambda value: value == 'Failed') == Try('Success', False)
    assert Try.of(lambda: 'Success').filter(lambda value: True) == Try('Success', True)
    assert Try.of(None).filter(lambda value: True) == Try(None, False)


# Generated at 2022-06-14 03:46:18.093478
# Unit test for method filter of class Try
def test_Try_filter():
    try_filter = Try(1, True)
    try_filter = try_filter.filter(lambda x: x == 1)

    try_filter_not = Try(1, False)
    try_filter_not = try_filter_not.filter(lambda x: x == 1)

    assert(isinstance(try_filter, Try))
    assert(isinstance(try_filter_not, Try))

    assert(try_filter == Try(1, True))
    assert(try_filter_not == Try(1, False))


# Generated at 2022-06-14 03:46:22.001494
# Unit test for method filter of class Try
def test_Try_filter():
    t = Try.of(3, 3)
    assert t.is_success

    t = t.filter(lambda x: x == 3)
    assert t.is_success

    t = t.filter(lambda x: x == 3)
    assert t.is_success

    t = t.filter(lambda x: x == 2)
    assert not t.is_success

# Generated at 2022-06-14 03:46:25.128319
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    test_value = 2
    # When
    monad = Try.of(lambda a: a, test_value)
    monad = monad.filter(lambda a: a > 1)
    result = monad.get()
    # Then
    assert result == test_value

# Generated at 2022-06-14 03:46:34.479760
# Unit test for method filter of class Try
def test_Try_filter():
    # Test for successful case
    assert Try(0, True).filter(lambda x: x == 0) == Try(0, True)
    # Test for fail case
    assert Try(0, False).filter(lambda x: x == 0) == Try(0, False)
    # Test for success case with filterer return True
    assert Try(0, True).filter(lambda x: x == 1) == Try(0, False)
    # Test for success case with filterer return False
    assert Try(0, True).filter(lambda x: x == 1) == Try(0, False)


# Generated at 2022-06-14 03:46:42.650942
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return True

    assert Try(5, True).filter(filterer) == Try(5, True)
    assert Try(5, False).filter(filterer) == Try(5, False)

    def filterer(value):
        return False

    assert Try(5, True).filter(filterer) == Try(5, False)
    assert Try(5, False).filter(filterer) == Try(5, False)


# Generated at 2022-06-14 03:46:51.041655
# Unit test for method filter of class Try
def test_Try_filter():
    # When monad is successfully and filterer returns True
    assert Try(10, True).filter(lambda x: x > 5) == Try(10, True)

    # When filterer returns False
    assert Try(10, True).filter(lambda x: x < 5) == Try(10, False)

    # When monad is not successfully
    assert Try(10, False).filter(lambda x: x > 5) == Try(10, False)



# Generated at 2022-06-14 03:46:56.215379
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter in Try class

    :returns: void
    :rtype: None
    """
    assert Try('a', True).filter(lambda a: a == 'a') == Try('a', True)
    assert Try('a', True).filter(lambda a: a == 'b') == Try('a', False)
    assert Try('a', False).filter(lambda a: a == 'a') == Try('a', False)


# Generated at 2022-06-14 03:47:03.063638
# Unit test for method filter of class Try
def test_Try_filter():
    @Try.of
    def div(x, y):
        return x / y

    def filterer(x):
        return x > 10

    assert div(20, 2).filter(filterer) == Try(10, True)
    assert div(20, 2).filter(filterer) != Try(10, False)
    assert div(5, 5).filter(filterer) != Try(1, True)
    assert div(5, 5).filter(filterer) == Try(1, False)



# Generated at 2022-06-14 03:47:11.504264
# Unit test for method filter of class Try
def test_Try_filter():
    some_value = 1
    some_value_not_eq_one = 2
    fn_filter = lambda v: v == 1

    success_try = Try(some_value, True)
    success_try_filtered = success_try.filter(fn_filter)

    assert success_try_filtered == Try(some_value, True)

    fail_try = Try(some_value_not_eq_one, False)
    fail_try_filtered = fail_try.filter(fn_filter)

    assert fail_try_filtered == Try(some_value_not_eq_one, False)


# Generated at 2022-06-14 03:47:16.694283
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)



# Generated at 2022-06-14 03:47:20.433144
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True)\
        .filter(lambda x: isinstance(x, int))\
        == Try(1, True)
    assert Try(1, True)\
        .filter(lambda x: x > 0)\
        == Try(1, True)
    assert Try(1, True)\
        .filter(lambda x: x < 0)\
        == Try(1, False)

# Generated at 2022-06-14 03:47:25.809593
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None).filter(lambda value: value == 1) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(lambda value: value == 0) == Try(1, False)
    assert Try.of(lambda: Exception('test'), None).filter(lambda value: True) == Try(Exception('test'), False)
    assert Try.of(lambda: Exception('test'), None).filter(lambda value: False) == Try(Exception('test'), False)



# Generated at 2022-06-14 03:47:30.914723
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda v: v == 1) == Try(1, True)
    assert Try(1, True).filter(lambda v: v == 2) == Try(1, False)



# Generated at 2022-06-14 03:47:35.245108
# Unit test for method filter of class Try
def test_Try_filter():
    def filter_fn(a):
        return a < 5

    assert Try.of(lambda: 10).filter(filter_fn) == Try(10, False)
    assert Try.of(lambda: 4).filter(filter_fn) == Try(4, True)


# Generated at 2022-06-14 03:47:44.284498
# Unit test for method filter of class Try
def test_Try_filter():
    class A:
        pass
    a = A()

    # filter success when value is not None
    assert Try.of(lambda x: x, a).filter(lambda value: value is not None) == Try(a, True)

    # filter not success when value is None
    assert Try.of(lambda x: x, a).filter(lambda value: value is None) == Try(a, False)

    # filter not success when fn raises exception
    assert Try.of(lambda x: None.foo, None).filter(lambda value: value is not None) == Try(None, False)



# Generated at 2022-06-14 03:47:53.350557
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try(1, True).filter(lambda x: x % 2 == 0) == Try(1, False)
    assert Try(2, False).filter(lambda x: x % 2 == 0) == Try(2, False)


# Generated at 2022-06-14 03:47:58.275246
# Unit test for method filter of class Try
def test_Try_filter():
    x = Try(32, True)
    assert x.filter(lambda x: x > 13) == Try(32, True)
    assert x.filter(lambda x: x > 0 and x < 14) == Try(32, False)

# Generated at 2022-06-14 03:48:03.560404
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(
        fn_return_True, True) \
        .filter(fn_return_True) == Try(
        fn_return_True, True)
    assert Try(
        fn_return_True, True) \
        .filter(fn_return_False) == Try(
        fn_return_True, False)


# Generated at 2022-06-14 03:48:09.106346
# Unit test for method filter of class Try
def test_Try_filter():

    def filter_condition(value):
        return value == 1

    monad = Try.of(lambda: 1)
    assert monad.filter(filter_condition) == Try.of(lambda: 1)

    monad = Try.of(lambda: 2)
    assert monad.filter(filter_condition) == Try.of(lambda: 2, False)

# Generated at 2022-06-14 03:48:16.767173
# Unit test for method filter of class Try
def test_Try_filter():
    try_success = Try(1, True)
    try_not_success = Try(1, False)
    filterer = lambda x: x == 1
    assert try_success.filter(filterer) == Try(1, True)
    assert try_not_success.filter(filterer) == Try(1, False)

    try_success = Try('a', True)
    assert try_success.filter(filterer) == Try('a', False)



# Generated at 2022-06-14 03:48:21.968480
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).bind(lambda x: Try.of(int, x)).filter(lambda x: x > 0)\
        == Try(1, True)
    assert Try(1, True).bind(lambda x: Try.of(int, x)).filter(lambda x: x < 0)\
        == Try(1, False)
    assert Try(-1, True).bind(lambda x: Try.of(int, x)).filter(lambda x: x > 0)\
        == Try(-1, False)
    assert Try(-1, True).bind(lambda x: Try.of(int, x)).filter(lambda x: x < 0)\
        == Try(-1, False)
    assert Try('a', True).bind(lambda x: Try.of(int, x)).filter(lambda x: x > 0)\
        == Try('a', False)

# Generated at 2022-06-14 03:48:31.849059
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def test_filter_with_success(successes, fails):
        successes += 1
        try:
            # Should be in successfully
            Try.of(lambda: 1/0).filter(lambda v: v == 1/0)
        except:
            fails += 1

        # Should be in success
        if not Try.of(lambda: 1) \
            .filter(lambda v: v == 1).is_success:
            fails += 1

        if not Try.of(lambda: 1) \
            .filter(lambda v: v == 1).value == 1:
            fails += 1

        # Should be in not success
        if Try.of(lambda: 1) \
            .filter(lambda v: v == 0).is_success:
            fails += 1


# Generated at 2022-06-14 03:48:39.727290
# Unit test for method filter of class Try
def test_Try_filter():
    # Successfully Try
    assert Try.of(lambda x: x, 1).map(lambda x: x).filter(lambda x: True) == Try(1, True), "Test 1 failed"
    assert Try.of(lambda x: x, 1).map(lambda x: x).filter(lambda x: False) == Try(1, False), "Test 1 failed"
    assert Try.of(lambda x: x, 1).map(lambda x: x).filter(lambda x: False) == Try(1, False), "Test 2 failed"

    # Not successfully Try
    assert Try.of(lambda x: 1 / 0, 1).map(lambda x: x).filter(lambda x: True) == Try(ZeroDivisionError, False), "Test 3 failed"

# Generated at 2022-06-14 03:48:44.389878
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x != 0) == Try(2, True)
    assert Try(2, True).filter(lambda x: x == 0) == Try(2, False)
    assert Try(2, False).filter(lambda x: x == 0) == Try(2, False)


# Generated at 2022-06-14 03:48:50.135807
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 10, None).filter(lambda _: False).get_or_else(20) == 20
    assert Try.of(lambda: 10, None).filter(lambda _: True).get_or_else(20) == 10
    assert Try.of(lambda: 10, None).filter(lambda _: True).is_success

    assert Try.of(lambda: 0, None).filter(raise_exception).get_or_else(20) == 20
    assert not Try.of(lambda: 0, None).filter(raise_exception).is_success

    assert Try.of(lambda: 10, None).filter(lambda _: True).get_or_else(20) == 10
    assert Try.of(lambda: 10, None).filter(lambda _: True).is_success

# Generated at 2022-06-14 03:49:01.612436
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value > 0
    success_try = Try(3, True)
    assert success_try.filter(filterer) == Try(3, True)
    fail_try = Try(-1, True)
    assert fail_try.filter(filterer) == Try(-1, False)
    fail_try = Try(-1, False)
    assert fail_try.filter(filterer) == Try(-1, False)


# Generated at 2022-06-14 03:49:05.895803
# Unit test for method filter of class Try
def test_Try_filter():
    try_value = Try(2, True)
    assert try_value.filter(lambda _: True) == try_value
    assert try_value.filter(lambda _: False) == Try(2, False)


# Generated at 2022-06-14 03:49:08.220269
# Unit test for method filter of class Try
def test_Try_filter():
    # given
    given = Try(1, True)
    
    # when
    actual = given.filter(lambda value: value == 1).value

    # then
    assert actual == 1

# Generated at 2022-06-14 03:49:19.738825
# Unit test for method filter of class Try
def test_Try_filter():
    # Given this function
    def operation(x):
        return (x + 1) / (x - 1)

    # When divide by zero
    t = Try.of(operation, 0)
    # On_fail nonzero values
    assert t.filter(lambda x: x != 0) == Try(ZeroDivisionError(), False)
    # On_success nonzero values
    assert t.filter(lambda x: x == 0) == Try(0, True)

    # When divide non-zero values
    t = Try.of(operation, 1)
    # On_fail zero division
    assert t.filter(lambda x: x == 0) == Try(float("inf"), False)
    # On_success zero division
    assert t.filter(lambda x: x != 0) == Try(float("inf"), True)

    # When not exception
   

# Generated at 2022-06-14 03:49:23.365531
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(a):
        return a % 2 == 0

    assert Try.of(lambda x: x, 2).filter(filterer) == Try(2, True)
    assert Try.of(lambda x: x, 3).filter(filterer) == Try(3, False)




# Generated at 2022-06-14 03:49:30.467588
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x < 20) == Try(10, True)
    assert Try(10, True).filter(lambda x: x > 20) == Try(10, False)
    assert Try(10, False).filter(lambda x: x < 20) == Try(10, False)
    assert Try(10, False).filter(lambda x: x > 20) == Try(10, False)


# Generated at 2022-06-14 03:49:35.495915
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x >= 0) == Try(5, True)
    assert Try(5, True).filter(lambda x: x < 0) == Try(5, False)
    assert Try(5, False).filter(lambda x: x >= 0) == Try(5, False)



# Generated at 2022-06-14 03:49:41.934635
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try('aaa', False).filter(lambda x: x == 2) == Try('aaa', False)
    assert Try('aaa', False).filter(lambda x: x == 'aaa') == Try('aaa', False)


# Generated at 2022-06-14 03:49:53.042146
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(x):
        return x % 2 == 0

    def test_function_filterer(x):
        return x * 2

    # test_function_filterer to apply on monad value 4
    actual = Try.of(test_function_filterer, 4).filter(filterer)

    # filter not applied on monad value 4
    expected = Try.of(test_function_filterer, 4)

    # actual and expected must be equals
    assert actual.value == 8
    assert actual == expected

    # filter applied on monad value 3
    actual = Try.of(test_function_filterer, 3).filter(filterer)

    # filter applied on monad value 3
    expected = Try(3, False)

    # actual and expected must be equals


# Generated at 2022-06-14 03:49:58.228801
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for filter method of Try class.
    """
    assert Try(10, True).filter(lambda x: x > 5) == Try(10, True)
    assert Try(10, True).filter(lambda x: x < 5) == Try(10, False)
    assert Try(10, False).filter(lambda x: x > 5) == Try(10, False)



# Generated at 2022-06-14 03:50:10.261779
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 2).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try.of(lambda: 3).filter(lambda x: x % 2 == 0) == Try(3, False)
    assert Try.of(lambda: 3).filter(lambda x: x % 2 == 0).get_or_else(0) == 0

# Generated at 2022-06-14 03:50:18.021473
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value in [2, 3, 5, 7]

    assert Try.of(lambda: 2).filter(filterer) == Try(2, True)
    assert Try.of(lambda: 2).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try.of(lambda: 3).filter(lambda x: x % 2 == 0) == Try(3, False)
    assert Try.of(lambda: 0).filter(lambda x: x % 2 == 0) == Try(0, True)
    assert Try.of(lambda: 1).filter(lambda x: x % 2 == 0) == Try(1, False)

# Generated at 2022-06-14 03:50:30.730914
# Unit test for method filter of class Try
def test_Try_filter():
    # When value is greater than 10
    try_greater_than_ten = Try(11, True)
    assert try_greater_than_ten == try_greater_than_ten.filter(lambda value: value > 10)

    # When value is 10
    try_eq_ten = Try(10, True)
    assert Try(10, False) == try_eq_ten.filter(lambda value: value > 10)

    # When value is less than 10
    try_less_than_ten = Try(9, True)
    assert Try(9, False) == try_less_than_ten.filter(lambda value: value > 10)

    # When value is 9 and not successfully
    try_less_than_ten = Try(9, False)

# Generated at 2022-06-14 03:50:42.311538
# Unit test for method filter of class Try
def test_Try_filter():
    value1 = Try.of(lambda: 1).filter(lambda value: value > 0)
    value2 = Try.of(lambda: 1).filter(lambda value: value < 0)
    value3 = Try.of(lambda: -1).filter(lambda value: value > 0)
    value4 = Try.of(lambda: -1).filter(lambda value: value < 0)
    value5 = Try.of(lambda: -1).filter(lambda value: False)
    value6 = Try.of(lambda: raise_exception()).filter(lambda value: True)
    value7 = Try.of(lambda: raise_exception()).filter(lambda value: False)
    assert value1 == Try(1, True)
    assert value2 == Try(1, False)
    assert value3 == Try(-1, False)
    assert value4

# Generated at 2022-06-14 03:50:49.520037
# Unit test for method filter of class Try
def test_Try_filter():
    # given
    true_try = Try(None, True)
    false_try = Try(None, False)

    # when
    mapped_true_try = true_try.filter(lambda x: True)
    mapped_false_try = false_try.filter(lambda x: False)

    # then
    assert true_try == mapped_true_try
    assert false_try == mapped_false_try



# Generated at 2022-06-14 03:50:56.051220
# Unit test for method filter of class Try
def test_Try_filter():
    try_value = Try.of(lambda x, y: x + y, 1, 2)
    assert try_value.filter(lambda value: value == 3) == Try(3, True)
    assert try_value.filter(lambda value: value == 4) == Try(3, False)
    assert try_value.filter((lambda value: value == 3).__call__) == Try(3, True)


# Generated at 2022-06-14 03:51:01.983885
# Unit test for method filter of class Try
def test_Try_filter():
    x = 5
    try_test = Try.of(lambda _: x, x)
    
    def filterer(x):
        return x > 6

    try_test_filtered = try_test.filter(filterer)

    assert not try_test_filtered.is_success
    assert try_test_filtered.value == 5

    try_test_filtered = try_test.filter(lambda _: True)

    assert try_test_filtered.is_success
    assert try_test_filtered.value == 5



# Generated at 2022-06-14 03:51:05.462314
# Unit test for method filter of class Try
def test_Try_filter():
    # this test validates that method filter return copy of monad when filterer return True
    t = Try.of(int, '10')
    assert t == t.filter(lambda x: x == 10)

    # this test validates that method filter return not successfully Try when filterer return False
    t = Try.of(int, '10')
    assert Try(10, False) == t.filter(lambda x: x != 10)


# Generated at 2022-06-14 03:51:11.927449
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 'some_value',).filter(lambda val: True) == Try('some_value', True)
    assert Try.of(lambda: 'some_value',).filter(lambda val: False) == Try('some_value', False)
    assert Try.of(lambda: raise_exception,).filter(lambda val: True) == Try(exception_instance, False)
    assert Try.of(lambda: raise_exception,).filter(lambda val: False) == Try(exception_instance, False)


# Generated at 2022-06-14 03:51:20.340453
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(True, True).filter(lambda x: x) == Try(True, True)
    assert Try(True, True).filter(lambda x: not x) == Try(True, False)
    assert Try(False, True).filter(lambda x: x) == Try(False, False)
    assert Try(False, True).filter(lambda x: not x) == Try(False, False)
    assert Try(Exception('exception'), False).filter(lambda x: not x) == Try(Exception('exception'), False)


# Generated at 2022-06-14 03:51:34.160402
# Unit test for constructor of class Try
def test_Try():
    @Try.of
    def div(x: int, y: int):
        return x / y

    assert div == Try(div, True)
    assert div != Try(div, False)



# Generated at 2022-06-14 03:51:38.504320
# Unit test for constructor of class Try
def test_Try():
    assert Try(5, True) == Try(5, True)
    assert Try(4, False) == Try(4, False)
    assert Try(5, True) != Try(1, True)
    assert Try(2, False) != Try(2, True)
    assert Try(5, True) != Try(6, True)
    assert Try(1, False) != Try(6, False)
    assert Try(6, True) != Try(6, False)
    assert Try(1, False) != Try(1, True)


# Generated at 2022-06-14 03:51:43.613949
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    a = Try(1, True)
    b = Try('1', True)
    c = Try(1, True)
    d = Try(1, False)

    assert(a == a)
    assert(a == c)
    assert(a != None)
    assert(a != b)
    assert(a != d)


# Generated at 2022-06-14 03:51:54.376773
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    """
    Test for comparing Try object.

        :returns: None
        :rtype: None
    """
    x = Try(100, True)
    y = Try(100, True)
    z = Try(100, False)
    x1 = Try(None, True)
    y1 = Try(None, True)
    z1 = Try(None, False)
    assert x == y, 'Objects are not equal'
    assert x != z, 'Objects are equals'
    assert x == x, 'Objects are not equal'
    assert x1 == y1, 'Objects are not equal'
    assert x1 != z1, 'Objects are equals'
    assert x1 == x1, 'Objects are not equal'


# Generated at 2022-06-14 03:51:57.513064
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    assert Try.of(lambda x: x, 1).get_or_else(2) == 1
    assert Try.of(lambda x: x, 1).bind(lambda x: Try.of(lambda y: y, 0)).get_or_else(2) == 2



# Generated at 2022-06-14 03:52:01.314183
# Unit test for method get of class Try
def test_Try_get():
    """
    Test function Try get.

    :returns: nothing
    :rtype: None
    """
    assert Try(42, True).get() == 42
    assert Try(42, False).get() == 42


# Generated at 2022-06-14 03:52:07.761127
# Unit test for method on_success of class Try
def test_Try_on_success():
    """
    It's works when on_success method of Try
    give result Try(1, True) when it argument function called with value 1.
    It's works when on_success method of Try
    give result Try(Exception(), False) when it argument function not called.

    :returns: void
    :rtype: Void
    """
    def f(value):
        return value * 2
    assert Try(1, True).on_success(f).value == 2
    assert Try(Exception(), False).on_success(f).value



# Generated at 2022-06-14 03:52:17.622069
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def thrower(x):
        raise Exception('error')

    def check(x):
        if x >= 0:
            return True
        return False

    assert Try.of(thrower, 2).filter(check) == Try(Exception('error'), False)
    assert Try.of(thrower, -1).filter(check) == Try(Exception('error'), False)
    assert Try.of(lambda: 2, -1).filter(check) == Try(2, False)
    assert Try.of(lambda: 2, 2).filter(check) == Try(2, True)

# Generated at 2022-06-14 03:52:21.873924
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    t = Try.of(divmod, 5, 0) \
        .on_fail(lambda e: print('exception:', e))
    assert t == Try(ZeroDivisionError('division by zero'), False)



# Generated at 2022-06-14 03:52:23.914489
# Unit test for method get of class Try
def test_Try_get():
    assert Try(1, True).get() == 1
    assert Try(1, False).get() == 1


# Generated at 2022-06-14 03:52:41.811984
# Unit test for constructor of class Try
def test_Try():
    assert Try(5, True) == Try(5, True)
    assert Try(5, True) != Try(5, False)
    assert Try(5, False) != Try(7, False)
    assert Try(5, False) != Try(7, True)
    assert Try(5, True) != Try(7, True)


# Generated at 2022-06-14 03:52:46.784418
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    assert Try(1, True).on_fail(print) is Try(1, True),\
        'test_Try_on_fail: in test_case1'
    assert Try(1, False).on_fail(print) is Try(1, False),\
        'test_Try_on_fail: in test_case2'


# Generated at 2022-06-14 03:52:51.342408
# Unit test for constructor of class Try
def test_Try():  # pragma: no cover
    assert Try(1, True) == Try(1, True)
    assert Try(2, False) == Try(2, False)
    assert Try(1, True) != Try(2, False)


# Generated at 2022-06-14 03:53:01.129464
# Unit test for method filter of class Try
def test_Try_filter():
    """
    This method use filtering when send value gt 0,
    and try to get value in the presence of exceptions.

    :returns: None
    :rtype: None
    """
    def filter_gt_0(number):
        return number > 0
    def get_number():
        raise ValueError('ValueError')
    def write_number(number):
        print(number)  # pragma: no cover

    number = Try.of(get_number).filter(filter_gt_0)
    number.on_success(write_number)

# Generated at 2022-06-14 03:53:08.595167
# Unit test for method bind of class Try
def test_Try_bind():
    def bind_func(x):
        return Try(x+3, True)

    def bind_func2(x):
        return Try(x, False)

    a_try = Try(5, True)

    assert a_try.bind(bind_func).get() == 8
    assert a_try.bind(bind_func2).is_success == False

# Generated at 2022-06-14 03:53:11.291038
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    def fail_callback(e):
        assert isinstance(e, Exception)

    try:
        raise Exception()
    except Exception as e:
        assert Try(e, False).on_fail(fail_callback).is_success == False


# Generated at 2022-06-14 03:53:20.523658
# Unit test for method map of class Try
def test_Try_map():
    assert Try.of(lambda x: x * 2, 2) == Try(4, True)
    assert Try(2, True).map(lambda x: x * 2) == Try(4, True)
    assert Try(2, True).map(lambda x: x ** 2) == Try(4, True)
    assert Try(2, True).map(lambda x: x + 2) == Try(4, True)
    assert Try(Exception('test'), False).map(lambda x: x + 2) == Try(Exception('test'), False)



# Generated at 2022-06-14 03:53:23.232383
# Unit test for method get of class Try
def test_Try_get():
    assert Try.of(int, "123").get() == 123
    assert Try.of(int, "error").get() == "error"


# Generated at 2022-06-14 03:53:25.243508
# Unit test for method on_success of class Try

# Generated at 2022-06-14 03:53:33.528568
# Unit test for method bind of class Try
def test_Try_bind():
    def returns_five() -> Try[int]:
        return Try(5, True)

    def test_func():
        return Try.of(lambda: 1 / 0)

    def returns_success():
        return test_func().bind(lambda _: returns_five())

    def returns_fail():
        return test_func().bind(lambda _: None)

    assert returns_success() == Try(5, True)
    assert returns_fail() == Try(ZeroDivisionError("division by zero"), False)


# Generated at 2022-06-14 03:53:49.934686
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    assert Try.of(lambda x: x + 1, 1).get_or_else(0) == 2
    assert Try.of(lambda x: 1 / x, 0).get_or_else(0) == 0
    assert Try.of(lambda x: 1 / x, 1).get_or_else(None) == 1



# Generated at 2022-06-14 03:53:54.630218
# Unit test for constructor of class Try
def test_Try():
    try_success = Try(5, True)
    assert try_success.value == 5 and try_success.is_success

    try_fail = Try(5, False)
    assert try_fail.value == 5 and not try_fail.is_success



# Generated at 2022-06-14 03:54:00.875357
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, True) != Try(1, False)
    assert Try(1, False) != Try(2, True)
    assert Try(1, False) != Try(2, False)
    assert Try(1, True) != 1
    assert Try(1, True) == Try(1, True)


# Generated at 2022-06-14 03:54:13.114516
# Unit test for method bind of class Try
def test_Try_bind():
    # examples
    m1 = Try.of(lambda x: x + 1, 1)  # Successfully Try[2]
    m2 = Try.of(lambda x: x / 0, 1)  # Error, Try[ZeroDivisionError]

    def bind(v):
        # Return successfully Try when t is successfully,
        # othercase return not successfully Try
        try:
            return Try(v + 1, True)
        except Exception as e:
            return Try(e, False)

    print(m1.bind(bind))  # Successfully Try[3]
    print(m2.bind(bind))  # Not successfully Try[ZeroDivisionError]

    print(m1.bind(lambda v: Try(v * 2, True)))  # Successfully Try[4]

# Generated at 2022-06-14 03:54:20.335065
# Unit test for method __eq__ of class Try
def test_Try___eq__():  # pragma: no cover
    assert Try(1, True) == Try(1, True)
    assert Try(None, False) == Try(None, False)
    assert Try(None, False) != Try(1, True)
    assert Try(None, False) != Try(None, True)
    assert Try(None, True) != Try(1, False)
    assert Try(None, True) != Try(1, True)

