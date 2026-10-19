

# Generated at 2022-06-14 03:44:33.574570
# Unit test for method filter of class Try
def test_Try_filter():

    # not successfully try
    try_ = Try(1, False)
    try_.filter(lambda x: x > 1)
    assert try_ == Try(1, False)

    # successfully try, with value not passing filterer
    try_ = Try(1, True)
    try_.filter(lambda x: x > 1)
    assert try_ == Try(1, False)

    # successfully try, with value passing filterer
    try_ = Try(1, True)
    try_.filter(lambda x: x < 2)
    assert try_ == Try(1, True)


# Generated at 2022-06-14 03:44:42.892095
# Unit test for method filter of class Try
def test_Try_filter():
    class CustomException(Exception):
        pass

    assert Try.of(lambda a, b: a * b, 20, 5) == Try(100, True)
    assert Try.of(lambda a, b: a / b, 20, 5) == Try(4, True)
    assert Try.of(lambda a, b: a * b, 20, 0) == Try(0, True)
    assert Try.of(lambda a, b: a / b, 20, 0) == Try(ZeroDivisionError, False)
    assert Try.of(lambda a, b: a * b, 20, 5).filter(lambda r: r == 100) == Try(100, True)
    assert Try.of(lambda a, b: a / b, 20, 5).filter(lambda r: r == 4) == Try(4, True)
    assert Try.of

# Generated at 2022-06-14 03:44:54.783527
# Unit test for method filter of class Try
def test_Try_filter():
    # When monad is success and filterer returns True
    assert Try(1, True).filter(lambda v: v == 1).get() == 1
    assert Try(1, True).filter(lambda v: v == True).get() == 1
    assert Try("Some string", True).filter(lambda v: True).get() == "Some string"
    assert Try("Some string", True).filter(lambda v: v == "Some string").get() == "Some string"

    # When monad is success and filterer returns False
    assert Try(1, True).filter(lambda v: v == 2).is_success == False
    assert Try(1, True).filter(lambda v: v == False).is_success == False
    assert Try("Some string", True).filter(lambda v: v == "Not equal string").is_success == False

    #

# Generated at 2022-06-14 03:45:01.017834
# Unit test for method filter of class Try
def test_Try_filter():
    value = 0
    try_ok = Try.of(lambda: 1)
    try_ok.filter(lambda x: x == 1)
    try_ok.filter(lambda x: x == 2)
    try_not_ok = Try.of(lambda: 1/0)
    try_not_ok.filter(lambda x: False)
    try_not_ok.filter(lambda x: True)



# Generated at 2022-06-14 03:45:06.582546
# Unit test for method filter of class Try
def test_Try_filter():
    def positive(number):
        return number > 0
    assert Try.of(int, '10').filter(positive) == Try(10, True)
    assert Try.of(int, '-1').filter(positive) == Try(-1, False)


# Generated at 2022-06-14 03:45:11.279800
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(5, True).filter(lambda x: x > 5) == Try(5, False)
    assert Try(5, True).filter(lambda x: x < 10) == Try(5, True)
    assert Try(5, False).filter(lambda x: x < 10) == Try(5, False)


# Generated at 2022-06-14 03:45:16.546690
# Unit test for method filter of class Try
def test_Try_filter():
    def incr(x):
        return x + 1

    def negative_check(x):
        return x >= 0

    try_of_10_incr_negative_checked = Try.of(incr, 10).filter(negative_check)
    assert try_of_10_incr_negative_checked == Try(11, True)

    try_of_neg_10_negative_checked = Try.of(incr, -10).filter(negative_check)
    assert try_of_neg_10_negative_checked == Try(-10, False)



# Generated at 2022-06-14 03:45:26.973127
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filt_func(x): return x > 0
    assert Try.of(int, '1').filter(filt_func) == Try(1, True)
    assert Try.of(int, '-1').filter(filt_func) == Try(-1, False)
    assert Try.of(int, '-1.0').filter(filt_func) == Try(-1.0, False)
    assert Try.of(int, '-1.0').map(abs).filter(filt_func) == Try(1.0, True)
    assert Try.of(int, '1a').filter(filt_func) == Try(ValueError(), False)


# Generated at 2022-06-14 03:45:34.180930
# Unit test for method filter of class Try
def test_Try_filter():
    try_with_value = Try.of(lambda: 9)
    try_without_value = Try.of(lambda: raise_exception('fail'))

    assert try_with_value.filter(lambda value: value == 9) == Try(9, True)
    assert try_with_value.filter(lambda value: value != 9) == Try(9, False)
    assert try_without_value.filter(lambda value: value > 0) == Try(Exception('fail'), False)
    assert try_without_value.filter(lambda value: value > 0) == Try(Exception('fail'), False)



# Generated at 2022-06-14 03:45:39.398679
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def is_positive(x):
        return x > 0

    def fail_filter_test():
        assert(
            Try(-1, True).filter(is_positive) == Try(-1, False)
        ), 'Test failed!'

    def success_filter_test():
        assert(
            Try(1, True).filter(is_positive) == Try(1, True)
        ), 'Test failed!'

    fail_filter_test()
    success_filter_test()
    print('Test passed!')


# Generated at 2022-06-14 03:45:46.662704
# Unit test for method filter of class Try
def test_Try_filter():
    e = Exception('')
    Try(1, True).filter(lambda x: x == 1).get_or_else(None) == 1
    Try(1, True).filter(lambda x: x == 2).get() == e
    Try(e, False).filter(lambda x: x == 2).get() == e

# Generated at 2022-06-14 03:45:50.363322
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 0

    assert Try.of(lambda x: x, 1).filter(filterer) == Try(1, True)
    assert Try.of(lambda x: x, -1).filter(filterer) == Try(-1, False)


# Generated at 2022-06-14 03:45:58.161459
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer_return_true(i):
        return True

    def filterer_return_false(i):
        return False

    assert Try.of(lambda: 1, None) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(filterer_return_true) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(filterer_return_false) == Try(1, False)



# Generated at 2022-06-14 03:46:00.829997
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try.of(lambda: 'test string', None).filter(lambda x: isinstance(x, str)) == Try('test string', True)
    assert Try.of(lambda: 42, None).filter(lambda x: isinstance(x, str)) == Try(42, False)
    assert Try.of(lambda: 42, None).filter(lambda x: isinstance(x, str)) == Try(42, False)

# Generated at 2022-06-14 03:46:08.901045
# Unit test for method filter of class Try
def test_Try_filter():
    # when successful value and filterer returns True
    t1 = Try.of(lambda x: x + 1, 3)
    f1 = lambda x: x == 4
    assert t1.filter(f1) == Try(4, True)

    # when successful value and filterer returns False
    t2 = Try.of(lambda x: x + 10, 3)
    f2 = lambda x: x > 10
    assert t2.filter(f2) == Try(13, False)

    # when not successful value and filterer returns True
    t3 = Try.of(lambda x: (1 / 0), 12)
    f3 = lambda x: True
    assert t3.filter(f3) == Try(ZeroDivisionError(
        'division by zero'), False)

    # when not successful value and filterer returns False

# Generated at 2022-06-14 03:46:12.833160
# Unit test for method filter of class Try
def test_Try_filter():
    assert True == Try.of(
        lambda x: x, 'hello'
    ).filter(
        lambda x: x == 'hello'
    ).is_success
    assert False == Try.of(
        lambda x: int(x), 'hello'
    ).filter(
        lambda x: x == 'hello'
    ).is_success


# Generated at 2022-06-14 03:46:20.192794
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda a: a, 1).filter(lambda _: False) == Try(1, False)
    assert Try.of(lambda a: a, 1).filter(lambda _: True) == Try(1, True)
    assert Try.of(lambda a: a, 1).filter(lambda _: False).filter(lambda _: True) == Try(1, False)
    assert Try.of(lambda a: a, 1).filter(lambda _: True).filter(lambda _: False) == Try(1, False)
    assert Try.of(lambda a: a, 1).filter(lambda _: True).filter(lambda _: True) == Try(1, True)


# Generated at 2022-06-14 03:46:24.558842
# Unit test for method filter of class Try
def test_Try_filter():
    def fn():
        raise Exception()

    def check_fn(x):
        return x == 5

    def check_fn_raise_exception(x):
        raise Exception()

    assert Try.of(fn).filter(check_fn) is Try(fn(), False)
    assert Try.of(fn).filter(check_fn_raise_exception) is Try(fn(), False)
    assert Try.of(lambda x: x, 5).filter(check_fn) is Try(5, True)



# Generated at 2022-06-14 03:46:28.058644
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    class Test:
        def __init__(self, data):
            self.data = data

        def filterer(self, value):
            return value == self.data

    test_1 = Test("a")
    try_1 = Try("a", True)
    try_2 = Try("b", True)
    assert try_1.filter(test_1.filterer) == Try("a", True)
    assert try_2.filter(test_1.filterer) == Try("b", False)

# Generated at 2022-06-14 03:46:34.225327
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test Try unit method filter.
    """
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)
    assert Try("fail", False).filter(lambda x: x > 0) == Try("fail", False)



# Generated at 2022-06-14 03:46:45.125337
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value == 'value1'

    assert Try('value1', is_success=True).filter(filterer) == Try('value1', is_success=True)
    assert Try('value2', is_success=True).filter(filterer) == Try('value2', is_success=False)



# Generated at 2022-06-14 03:46:51.391347
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value == 'c'

    assert Try('c', True).filter(filterer) == Try('c', True)
    assert Try('0', True).filter(filterer) == Try('0', False)
    assert Try('0', False).filter(filterer) == Try('0', False)

    try:
        Try(Exception(), False).filter(filterer)
        assert False
    except Exception:
        assert True



# Generated at 2022-06-14 03:46:55.404163
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(4, True).filter(lambda x: x % 2 == 0) == Try(4, True)
    assert Try(4, True).filter(lambda x: x % 2 != 0) == Try(4, False)
    assert Try(5, True).filter(lambda x: x % 2 == 0) == Try(5, False)


# Generated at 2022-06-14 03:47:02.546530
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(0, True).filter(lambda x: x > 0) == Try(0, False)
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x % 2 == 1) == Try(1, True)
    assert Try(0, True).filter(lambda x: x % 2 == 0) == Try(0, True)
    assert Try(1, False).filter(lambda x: x > 0) == Try(1, False)



# Generated at 2022-06-14 03:47:06.428020
# Unit test for method filter of class Try
def test_Try_filter():
    def add(x):
        return x + 1

    def is_even(x):
        return x % 2 == 0

    try_even = Try.of(add, 0)
    try_odd = Try.of(add, 1)

    assert try_even.filter(is_even) == Try(1, True)
    assert try_odd.filter(is_even) == Try(2, False)


# Generated at 2022-06-14 03:47:10.683833
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 3) == Try(5, True)
    assert Try(5, True).filter(lambda x: x < 3) == Try(5, False)
    assert Try(5, False).filter(lambda x: x > 3) == Try(5, False)

# Generated at 2022-06-14 03:47:20.061568
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x % 10 == 0, 4)\
        .filter(lambda x: x > 0)\
        .filter(lambda x: x < 10)\
        == Try(4, True)
    assert Try.of(lambda x: x % 10 == 0, -4)\
        .filter(lambda x: x > 0)\
        .filter(lambda x: x < 10)\
        == Try(-4, False)
    assert Try.of(lambda x: x % 10 == 0, 4)\
        .filter(lambda x: x > 0)\
        .filter(lambda x: x < 3)\
        == Try(4, False)


# Generated at 2022-06-14 03:47:25.134395
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value == 1

    try_1 = Try.of(lambda: 1)
    try_2 = Try.of(lambda: 2)

    try_1 = try_1.filter(filterer)
    try_2 = try_2.filter(filterer)

    assert try_1 == Try(1, True)
    assert try_2 != Try(2, True)



# Generated at 2022-06-14 03:47:38.216396
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def add_one(x):
        return x + 1
    def is_positive_number(x):
        return x > 0
    def is_odd(x):
        return x % 2 == 0
    def add_two(x):
        return x + 2

    def monad_test(test_name, monad_value, test_filterer, expected_value, expected_is_success: bool):
        try_monad_value = Try(monad_value, True)
        try_result = try_monad_value.filter(test_filterer)
        if try_result.value == expected_value and try_result.is_success == expected_is_success:
            print('Test "{}" pass'.format(test_name))

# Generated at 2022-06-14 03:47:42.060241
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x == 2) == Try(2, True)
    assert Try(2, True).filter(lambda x: x == 1) == Try(2, False)


# Generated at 2022-06-14 03:47:53.610406
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value: str) -> bool:
        return len(value) == 2

    def check_result(value: Try[str]):
        assert value.is_success is True
        assert value.value == 'ab'

    check_result(Try('ab', True).filter(filterer))

    def check_result(value: Try[str]):
        assert value.is_success is False
        assert value.value == 'ab'

    check_result(Try('ab', True).filter(lambda value: False))



# Generated at 2022-06-14 03:48:05.023844
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(a):
        return a == 1
    try_success = Try(1, True)
    try_fail = Try(2, True)
    try_not_success = Try(3, False)
    try_fail_with_filterer = Try.of(filterer, 4)
    assert try_success.filter(filterer) == Try(1, True)
    assert try_fail.filter(filterer) == Try(2, False)
    assert try_not_success.filter(filterer) == Try(3, False)
    assert try_fail_with_filterer.filter(filterer) == Try(4, False)


# Generated at 2022-06-14 03:48:09.771301
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 0) == Try(5, True)
    assert Try(5, True).filter(lambda x: x < 0) == Try(5, False)
    assert Try(5, False).filter(lambda x: x > 0) == Try(5, False)

# Generated at 2022-06-14 03:48:14.414618
# Unit test for method filter of class Try
def test_Try_filter():
    def return_true(value):
        return True

    def return_false(value):
        return False

    assert Try.of(lambda: 1, )\
        .filter(return_true)\
        .is_success\
        is True

    assert Try.of(lambda: 1, )\
        .filter(return_false)\
        .is_success\
        is False



# Generated at 2022-06-14 03:48:19.079978
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)

# Generated at 2022-06-14 03:48:27.504546
# Unit test for method filter of class Try
def test_Try_filter():
    def divide(dividend, divisor):
        try:
            return Try(dividend / divisor, True)
        except ZeroDivisionError as e:
            return Try(e, False)

    def filterer(value):
        return value is not ZeroDivisionError

    assert divide(4, 2).filter(filterer) == Try(2, True)
    assert divide(4, 0).filter(filterer) == Try(ZeroDivisionError(), False)
    assert divide(4, 0).filter(filterer).is_success == False

# Generated at 2022-06-14 03:48:33.571197
# Unit test for method filter of class Try
def test_Try_filter():
    dict_json = {'a': 'b'}
    result = Try.of(lambda x: json.loads(x), json.dumps(dict_json))\
        .filter(lambda x: isinstance(x, dict))\
        .get()
    assert result == dict_json

    result = Try.of(lambda x: json.loads(x), json.dumps(dict_json))\
        .filter(lambda x: isinstance(x, list))\
        .get_or_else('')
    assert result == ''

# Generated at 2022-06-14 03:48:37.070520
# Unit test for method filter of class Try
def test_Try_filter():

    # Arrange
    def is_str_len_3(str: str) -> bool:
        return len(str) == 3

    # Act
    result = Try(10, True).filter(is_str_len_3)

    # Assert
    assert result == Try(10, False)


# Generated at 2022-06-14 03:48:42.512691
# Unit test for method filter of class Try
def test_Try_filter():
    if Try(2, True)\
        .bind(lambda x: Try(x + 3, True))\
        .filter(lambda x: x == 4)\
        .is_success != False:
        raise Exception('Error in test_Try_filter')


# Generated at 2022-06-14 03:48:43.093538
# Unit test for method filter of class Try
def test_Try_filter():
    pass

# Generated at 2022-06-14 03:48:56.325448
# Unit test for method filter of class Try
def test_Try_filter():
    def a(x):
        return x % 2 == 0

    f = Try.of(lambda x: x * 2 + 1, 3).filter(a)

    assert(f == Try(7, False))

    f = Try.of(lambda x: x * 2, 2).filter(a)

    assert(f == Try(4, True))



# Generated at 2022-06-14 03:49:01.110969
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x == 10)\
        == Try(10, True)
    assert Try(10, True).filter(lambda x: x == 20)\
        == Try(10, False)
    assert Try(None, False).filter(lambda x: x == 20)\
        == Try(None, False)
    assert isinstance(Try(None, False).filter(lambda x: x == 20), Try)


# Generated at 2022-06-14 03:49:06.421065
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(2, True).filter(lambda x: x == 1) == Try(2, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)


# Generated at 2022-06-14 03:49:14.901401
# Unit test for method filter of class Try
def test_Try_filter():
    assert(Try.of(lambda a: a+1, 2).filter(lambda el: el > 0) == Try(3, True))
    assert(Try.of(lambda a: a+1, 2).filter(lambda el: el < 0) == Try(2, False))
    assert(Try.of(lambda a: a+1, -2).filter(lambda el: el < 0) == Try(-2, False))


# Generated at 2022-06-14 03:49:21.841746
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)
    assert Try(Exception(), False).filter(lambda x: x > 0) == Try(Exception(), False)
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x < 0) == Try(1, False)
    assert Try.of(lambda x: None, 1).filter(lambda x: x > 0) == Try(None, False)
    assert Try.of(lambda x: None, 1).filter(lambda x: x > 1) == Try(None, False)

# Generated at 2022-06-14 03:49:30.786585
# Unit test for method filter of class Try
def test_Try_filter():
    """Testing Try class method filter"""
    #test with successfully monad
    assert Try(42, True).filter(lambda value: value % 2 == 0) == Try(42, True)
    assert Try(42, True).filter(lambda value: value % 2 != 0) == Try(42, False)
    #test with not successfully monad
    assert Try(42, False).filter(lambda value: value % 2 == 0) == Try(42, False)
    assert Try(42, False).filter(lambda value: value % 2 != 0) == Try(42, False)



# Generated at 2022-06-14 03:49:41.203724
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1) == Try.of(lambda: 1)\
        .filter(lambda num_one: num_one == 1)

    assert Try.of(lambda: 1) == Try.of(lambda: 1)\
        .filter(lambda num_one: num_one == 2)

    assert Try.of(lambda: 1, 2)\
        .filter(lambda num_one, num_two: num_one == 1 or num_two == 2)

# Generated at 2022-06-14 03:49:43.433896
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x > 22) == Try(10, False)
    assert Try(10, True).filter(lambda x: x < 22) == Try(10, True)


# Generated at 2022-06-14 03:49:49.332818
# Unit test for method filter of class Try
def test_Try_filter():
    """Return True when test is passed"""
    class CustomException(Exception):
        """Custom Exception Class"""

    def raise_exception(value):
        """Raise exception"""
        raise CustomException(value)

    assert Try.of(lambda: 1).filter(lambda x: True) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda x: False) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda x: True) != Try(1, False)

    assert Try.of(raise_exception, 1).filter(lambda x: True) == Try(1, False)
    assert Try.of(raise_exception, 1).filter(lambda x: False) == Try(1, False)

# Generated at 2022-06-14 03:49:55.142927
# Unit test for method filter of class Try
def test_Try_filter():
    filtered_some = Try.of(lambda: 1).filter(lambda x: x == 1)
    assert filtered_some == Try(1, True)

    filtered_none = Try.of(lambda: 1).filter(lambda x: x == 2)
    assert filtered_none == Try(1, False)


# Generated at 2022-06-14 03:50:27.013946
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test method filter in Try class.

    :returns: True when success, othercase raise AssertionError
    :rtype: Bool
    """
    # when filtered value is not True
    assert Try(4, True)\
        .filter(lambda value: value % 2 == 0) \
        .get_or_else(None) is None

    # when filtered value is True
    assert Try(4, True)\
        .filter(lambda value: value % 4 == 0) \
        .get_or_else(None) == 4

    # when filtered value is not True, when value is None
    assert Try(None, True)\
        .filter(lambda value: value is None)\
        .get_or_else(None) is None

    # when filtered value is True, when value is None

# Generated at 2022-06-14 03:50:34.994764
# Unit test for method filter of class Try
def test_Try_filter():

    # Successfully monad Try
    try1 = Try.of(lambda x: x, 1)
    assert try1.is_success == True
    assert try1.filter(lambda x: x < 5) == Try(1, True)
    assert try1.filter(lambda x: x == 5) == Try(1, False)

    # Not successfully monad Try
    try2 = Try.of(lambda x: 1 / x, 0)
    assert try2.is_success == False
    assert try2.filter(lambda x: x < 5) == Try(ZeroDivisionError("division by zero"), False)
    assert try2.filter(lambda x: x == 5) == Try(ZeroDivisionError("division by zero"), False)


# Generated at 2022-06-14 03:50:44.719097
# Unit test for method filter of class Try
def test_Try_filter():
    param1 = [1, 2, 3]
    param2 = 'asd'
    result = Try(param1, True).filter(isinstance)
    assert result == Try(param1, False)
    result = Try(param2, True).filter(isinstance)
    assert result == Try(param2, True)
    result = Try(param1, False).filter(isinstance)
    assert result == Try(param1, False)
    result = Try(param2, False).filter(isinstance)
    assert result == Try(param2, False)
    result = Try(param1, True).filter(isinstance).map(lambda el: el + [2])
    assert result == Try(param1 + [2], False)
    result = Try(param2, True).filter(isinstance).map(lambda el: el + [2])

# Generated at 2022-06-14 03:50:53.758855
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 5, None).filter(lambda x: x % 2 == 1) == Try(5, True)
    assert Try.of(lambda: 5, None).filter(lambda x: x % 2 == 0) == Try(5, False)
    assert Try.of(lambda: 5, None).filter(lambda x: x % 2 == 1).filter(lambda x: x > 4) == Try(5, True)
    assert Try.of(lambda: 5, None).filter(lambda x: x % 2 == 1).filter(lambda x: x < 4) == Try(5, False)
    assert Try.of(lambda: 5, None).filter(lambda x: x % 2 == 1).get() == 5

# Generated at 2022-06-14 03:51:03.519930
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter_is_success(param):
        return lambda value: value == param

    def test_filter_is_not_success(param):
        return lambda value: value != param

    assert Try(1, True).filter(test_filter_is_success(1)) == Try(1, True)
    assert Try(1, True).filter(test_filter_is_not_success(1)) == Try(1, False)
    assert Try(1, False).filter(test_filter_is_success(1)) == Try(1, False)
    assert Try(1, False).filter(test_filter_is_not_success(1)) == Try(1, False)



# Generated at 2022-06-14 03:51:11.638186
# Unit test for method filter of class Try
def test_Try_filter():
    """Test for method filter of class Try."""
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: x % 2 == 1

    result = Try.of(lambda: 5).filter(is_even)
    assert result == Try(5, False)

    result = Try.of(lambda: 5).filter(is_odd)
    assert result == Try(5, True)

    result = Try.of(lambda: 4).filter(is_even)
    assert result == Try(4, True)

    result = Try.of(lambda: 4).filter(is_odd)
    assert result == Try(4, False)


# Generated at 2022-06-14 03:51:22.860330
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    # Arrange
    def filterer(value):
        return value == 3
    def filterer_not(value):
        return value != 3
    def fail_callback(value):
        return print("I fail with", value)
    try_1 = Try(3, True)
    try_2 = Try(2, True)
    try_3 = Try(3, False)
    try_4 = Try(2, False)

    # Act
    try_1_filtered = try_1.filter(filterer)
    try_2_filtered = try_2.filter(filterer)
    try_3_filtered = try_3.filter(filterer)
    try_4_filtered = try_4.filter(filterer)
    try_1_filtered

# Generated at 2022-06-14 03:51:34.793262
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True)\
        .map(lambda x: x + 5)\
        .filter(lambda x: x % 2 == 0)\
        == Try(10, True)  # True
    assert Try(5, True)\
        .map(lambda x: x + 5)\
        .filter(lambda x: x % 3 == 0)\
        == Try(10, False)  # False
    assert Try(5, True)\
        .map(lambda x: x + 5)\
        .filter(lambda x: x % 2 == 0)\
        .filter(lambda x: x % 3 == 0)\
        == Try(10, False)  # False

# Generated at 2022-06-14 03:51:42.805589
# Unit test for method filter of class Try
def test_Try_filter():
    class CustomError(Exception):
        pass

    def test_try_with_type_error():
        try_fn = lambda: 42/0
        try_type_error = Try.of(try_fn)

        try_type_error_filtered = try_type_error.filter(lambda _: True)
        assert not try_type_error_filtered.is_success

        try_type_error_filtered = try_type_error.filter(lambda _: False)
        assert not try_type_error_filtered.is_success

    def test_try_with_value_error():
        try_fn = lambda: int('fail')
        try_value_error = Try.of(try_fn)

        try_value_error_filtered = try_value_error.filter(lambda _: True)

# Generated at 2022-06-14 03:51:47.582998
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(x):
        return x % 2 == 0

    assert Try.of(lambda: 3).filter(filterer) == Try(3, False)
    assert Try.of(lambda: 4).filter(filterer) == Try(4, True)


# Generated at 2022-06-14 03:52:35.037436
# Unit test for method filter of class Try
def test_Try_filter():
    six = 6
    t = Try.of(lambda: six).filter(lambda i: i % 2 == 0)
    assert t == Try(6, True)

    t = t.filter(lambda i: i in [0, 2, 4, 6, 8, 10])
    assert t == Try(6, True)

    t = t.filter(lambda i: i > 9)
    assert t == Try(6, False)


# Generated at 2022-06-14 03:52:45.729242
# Unit test for method filter of class Try
def test_Try_filter():
    err = Exception('Wrong')
    call_id = 1

    def mock_filterer_function(value):
        return value == call_id

    def mock_filterer_function_with_error(value):
        raise err

    def check(value):
        assert value == call_id

    print('--test_Try_filter--')
    assert Try.of(mock_filterer_function, call_id).filter(check).value == call_id
    assert not Try.of(mock_filterer_function_with_error, call_id).filter(check).is_success


# Generated at 2022-06-14 03:52:50.417921
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x < 2).is_success\
        == True
    assert Try(1, True).filter(lambda x: x > 2).is_success\
        == False



# Generated at 2022-06-14 03:52:55.614830
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value: str) -> bool:
        return len(value) > 3

    assert Try.of(lambda: 'foo').filter(filterer) == Try('foo', False)
    assert Try.of(lambda: 'foobar').filter(filterer) == Try('foobar', True)



# Generated at 2022-06-14 03:53:01.507718
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test success and fail cases when monad is successfully.
    """
    assert Try(1, True)\
        .filter(lambda x: x == 1)\
        .is_success == True

    assert Try(1, True)\
        .filter(lambda x: x == 2)\
        .is_success == False



# Generated at 2022-06-14 03:53:12.833205
# Unit test for method filter of class Try

# Generated at 2022-06-14 03:53:22.914218
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        if value == 1:
            return True
        return False

    try_one = Try(1, True)
    try_two = Try(1, False)
    try_three = Try(2, True)
    try_four = Try(2, False)

    assert try_one.filter(filterer) == Try(1, True)
    assert try_two.filter(filterer) == Try(1, False)
    assert try_three.filter(filterer) == Try(2, False)
    assert try_four.filter(filterer) == Try(2, False)


# Generated at 2022-06-14 03:53:32.953433
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 10

    def filterer2(x):
        return x > 20

    t1 = Try.of(lambda: 10)
    t2 = t1.filter(filterer)

    assert t2 == Try(10, False)

    t3 = Try.of(lambda: 20)
    t4 = t3.filter(filterer)

    assert t4 == Try(20, True)

    t4 = Try.of(lambda: 20)
    t5 = t4.filter(filterer).filter(filterer2)

    assert t5 == Try(20, False)

# Generated at 2022-06-14 03:53:38.039580
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filterer(value):
        return isinstance(value, int) and value > 5

    assert Try(Try.of(lambda: 4).filter(test_filterer), False) == Try.of(lambda: 4).filter(test_filterer)
    assert Try(Try.of(lambda: 6).filter(test_filterer), True) == Try.of(lambda: 6).filter(test_filterer)
    print('Test for method filter of class Try done successfully')

# Generated at 2022-06-14 03:53:42.526896
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover

    def check_value(value: str) -> bool:
        return value == 'a'

    assert Try('a', True).filter(check_value) == Try('a', True) is True
    assert Try('b', True).filter(check_value) == Try('b', False) is True