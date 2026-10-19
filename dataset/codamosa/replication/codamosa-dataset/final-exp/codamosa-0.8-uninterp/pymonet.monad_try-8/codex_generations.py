

# Generated at 2022-06-14 03:44:30.062678
# Unit test for method filter of class Try
def test_Try_filter():
    # When filterer returns True
    # Then Try should be successfully
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)

    # When filterer returns False
    # Then Try should not be successfully
    assert Try(1, True).filter(lambda x: x > 1) == Try(1, False)
    assert Try(1, True).filter(lambda x: x == 0) == Try(1, False)

    # When Try is not successfully 
    # Then Try should not be successfully
    assert Try(1, False).filter(lambda x: x > 0) == Try(1, False)


# Generated at 2022-06-14 03:44:40.321068
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Function to test Try class filter method

    :params: none
    :type: none
    :returns: none
    :rtype: none
    """
    def test(a: int, b: int) -> Try[int]:
        def filterer(a):
            return a > b
        return Try.of(lambda: a + b, 1, 2).filter(filterer)

    assert test(1, 2) == Try(3, False)
    assert test(2, 1) == Try(3, True)
    assert test(1, 2) != Try(3, True)
    assert test(2, 1) != Try(3, False)


# Generated at 2022-06-14 03:44:48.188677
# Unit test for method filter of class Try
def test_Try_filter():
    def less_than_three(x):
        return x < 3

    assert Try(2, True).filter(less_than_three) == Try(2, True)
    assert Try(4, True).filter(less_than_three) == Try(4, False)
    assert Try(4, False).filter(less_than_three) == Try(4, False)


# Generated at 2022-06-14 03:44:57.534682
# Unit test for method filter of class Try
def test_Try_filter():
    filterer = lambda value: value > 0
    value = 1
    expected = True
    actual = Try(value, True).filter(filterer).is_success
    assert(expected == actual)
    #
    value = 1
    expected = False
    actual = Try(value, False).filter(filterer).is_success
    assert(expected == actual)
    #
    actual = Try(value, True).filter(filterer).get_or_else(False)
    expected = 1
    assert(expected == actual)
    #
    expected = False
    actual = Try(value, False).filter(filterer).get_or_else(False)
    assert(expected == actual)
    #
    expected = Try(0, True).filter(filterer).get_or_else(False)

# Generated at 2022-06-14 03:45:11.035497
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 0) == Try(1, False)
    assert Try('test value', True).filter(lambda x: 'value' in x) == Try('test value', True)
    assert Try('test value', True).filter(lambda x: 'test' not in x) == Try('test value', False)
    assert Try('test value', False).filter(lambda x: 'test' not in x) == Try('test value', False)
    assert Try(None, True).filter(lambda x: x) == Try(None, False)

# Generated at 2022-06-14 03:45:23.211100
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """

    def add(a, b):
        if a + b > 2:
            return a + b
        raise Exception('Not a valid number')

    def less_2(x):
        return x < 2

    def less_3(x):
        return x < 3

    assert Try.of(add, 1, 1).filter(less_2) == Try(Exception('Not a valid number'), False)
    assert Try.of(add, 1, 2).filter(less_3) == Try(3, True)
    assert Try.of(add, 2, 2).filter(less_3) == Try(Exception('Not a valid number'), False)


# Generated at 2022-06-14 03:45:30.247831
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).map(lambda x: x+1).filter(lambda x: x < 3).get() == 2
    assert not Try(1, True).map(lambda x: x+1).filter(lambda x: x > 3).get() == 2
    assert Try(1, True).map(lambda x: x+1).filter(lambda x: x < 3).is_success == True
    assert Try(1, True).map(lambda x: x+1).filter(lambda x: x > 3).is_success == False


# Generated at 2022-06-14 03:45:33.441821
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: '2').filter(lambda x: x == '2') == Try('2', True)
    assert Try.of(lambda: '3').filter(lambda x: x == '2') == Try('3', False)



# Generated at 2022-06-14 03:45:45.180617
# Unit test for method filter of class Try
def test_Try_filter():
    from datetime import datetime

    def check_date(date):
        return date > datetime(2018, 1, 1)

    assert Try(datetime(2017, 1, 1), True)\
        .filter(check_date)\
        .filter(check_date)\
        == Try(datetime(2017, 1, 1), False)

    assert Try(datetime(2019, 1, 1), True)\
        .filter(check_date)\
        == Try(datetime(2019, 1, 1), True)

    assert Try(datetime(2019, 1, 1), False)\
        .filter(check_date)\
        == Try(datetime(2019, 1, 1), False)

# Generated at 2022-06-14 03:45:53.628057
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for Filter method from Try class.

    :returns: None
    :rtype: None
    """

    def divide(top, bottom):
        return top / bottom

    def filterer(value):
        return value % 2 == 0

    assert Try.of(divide, 10, 5).filter(filterer).get() == 2
    assert not Try.of(divide, 10, 5).filter(filterer).is_success
    assert Try.of(divide, 10, 5).filter(lambda _: True).get() == 2
    assert not Try.of(divide, 10, 0).filter(filterer).is_success
    assert Try.of(lambda: {}['test'], 10, 0).filter(filterer).is_success == False

# Generated at 2022-06-14 03:46:00.210509
# Unit test for method filter of class Try
def test_Try_filter():
    """
        Test for method filter of class Try.
    """
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)

# Generated at 2022-06-14 03:46:05.805740
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x : True) == Try(10, True)
    assert Try(10, False).filter(lambda x : True) == Try(10, False)
    assert Try(10, True).filter(lambda x : x == 10) == Try(10, True)
    assert Try(10, True).filter(lambda x : x < 10) == Try(10, False)



# Generated at 2022-06-14 03:46:10.143830
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 1

    assert False == (
        Try(2, True)
        .filter(filterer)
        .is_success
    )
    assert False == (
        Try(1, True)
        .filter(filterer)
        .is_success
    )


# Generated at 2022-06-14 03:46:14.784995
# Unit test for method filter of class Try
def test_Try_filter():
    def is_two_low(x):
        return x < 2

    assert Try.of(lambda: 1).filter(is_two_low) == Try(1, False)
    assert Try.of(lambda: 2).filter(is_two_low) == Try(2, True)


# Generated at 2022-06-14 03:46:22.832980
# Unit test for method filter of class Try
def test_Try_filter():
    @Try.of
    def fail_filterer(value):
        raise Exception(value)

    @Try.of
    def success_filterer(value):
        return True

    @Try.of
    def fail_filterer_2(value):
        return False

    def assert_Try(actual: Try, expected_value: int, expected_is_success: bool):
        assert actual.is_success == expected_is_success
        assert actual.value == expected_value

    first_fail_filterer_result = fail_filterer(1) \
        .filter(success_filterer)
    assert_Try(first_fail_filterer_result, 1, False)

    # if filterer return success, filter will return original value
    second_filterer_result = Try(1, True)

# Generated at 2022-06-14 03:46:30.313071
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 5
    try_ = Try(6, True)
    assert try_.filter(filterer) == Try(6, True)

    try_ = Try(6, False)
    assert try_.filter(filterer) == Try(6, False)

    try_ = Try(4, True)
    assert try_.filter(filterer) == Try(4, False)



# Generated at 2022-06-14 03:46:34.718391
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)


# Generated at 2022-06-14 03:46:40.700495
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: True) == Try(1, True), "filter True"
    assert Try(1, True).filter(lambda x: False) == Try(1, False), "filter False"
    assert Try(1, False).filter(lambda x: True) == Try(1, False), "not successfully filter"


# Generated at 2022-06-14 03:46:54.009340
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(x):
        return x % 2 == 0

    def error_filterer(x):
        return 1 / 0

    try:
        Try(2, True).filter(filterer).get() == 2
    except Exception as e:
        print('[ERROR] test_Try_filter: function filter - incorrect behaviour')
        print(e)
    try:
        assert Try(2, False).filter(filterer).is_success == False
    except Exception as e:
        print('[ERROR] test_Try_filter: function filter - incorrect behaviour')
        print(e)

# Generated at 2022-06-14 03:47:04.092092
# Unit test for method filter of class Try
def test_Try_filter():
    try_1 = Try.of(lambda: 1, 1)
    try_2 = Try.of(lambda: 2, 2)
    try_3 = Try.of(lambda: 3, 3)
    try_4 = Try.of(lambda: 4/0, 4)

    equal_1_2 = Try.of(lambda x, y: x == y, 1, 2)
    equal_1_1 = Try.of(lambda x, y: x == y, 1, 1)

    assert try_1.filter(lambda x: x == 1) == try_1
    assert try_1.filter(lambda x: x == 2) == Try(1, False)

    assert not try_4.filter(lambda x: x == 1)

# Generated at 2022-06-14 03:47:20.824410
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test case for method filter of class Try.
    """
    def test_positive_filter(value):
        """
        Return True when value is positive, othercase False.

        :params value: Integer value
        :type value: Integer
        :returns: True when value is positive, othercase False.
        :rtype: Boolean
        """
        return value > 0

    assert Try(1, True).filter(test_positive_filter) == Try(1, True)
    assert Try(-1, True).filter(test_positive_filter) == Try(-1, False)
    assert Try(-1, False).filter(test_positive_filter) == Try(-1, False)



# Generated at 2022-06-14 03:47:27.908588
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 0
    class MyException(Exception):
        pass
    success_filter = Try(1, True).filter(filterer)
    assert success_filter == Try(1, True)
    fail_filter = Try(1, False).filter(filterer)
    assert fail_filter == Try(1, False)
    try_filter = Try.of(lambda x: x, 1).filter(filterer)
    assert try_filter == Try(1, True)

# Generated at 2022-06-14 03:47:33.887961
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x < 0) == Try(1, False)
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 1) == Try(1, False)


# Generated at 2022-06-14 03:47:39.148815
# Unit test for method filter of class Try
def test_Try_filter():
    x = Try.of(lambda x: x, 5)
    y = Try.of(lambda x: x, 5)

    assert x.filter(lambda x: x == y.get()) == Try(5, True)
    assert x.filter(lambda x: x == 10) == Try(5, False)



# Generated at 2022-06-14 03:47:44.241554
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value == 10

    try1 = Try.of(lambda: 10, None)
    try2 = Try.of(lambda: 11, None)

    assert try1.filter(filterer) == Try(10, True)
    assert try2.filter(filterer) == Try(11, False)



# Generated at 2022-06-14 03:47:51.551858
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: True) == Try(2, True)
    assert Try(2, True).filter(lambda x: False) == Try(2, False)
    assert Try(2, False).filter(lambda x: True) == Try(2, False)
    assert Try(2, False).filter(lambda x: False) == Try(2, False)



# Generated at 2022-06-14 03:47:54.306260
# Unit test for method filter of class Try
def test_Try_filter(): # pragma: no cover
    assert Try(2, True).filter(lambda value: True) == Try(2, True)
    assert Try(2, False).filter(lambda value: True) == Try(2, False)
    assert Try(1, True).filter(lambda value: value > 1) == Try(1, False)


# Generated at 2022-06-14 03:48:05.467491
# Unit test for method filter of class Try
def test_Try_filter():
    def f(x):
        return x > 0

    def f1(_):
        raise Exception('some exception')

    assert Try(2, True).filter(f).get() == Try(2, True).get()
    assert Try(2, True).filter(f).is_success == Try(2, True).is_success
    assert Try(-2, True).filter(f).get() == Try(-2, False).get()
    assert Try(-2, True).filter(f).is_success == Try(-2, False).is_success
    assert Try(-2, True).filter(f1).get() == Try(-2, False).get()
    assert Try(2, False).filter(f).get() == Try(2, False).get()

# Generated at 2022-06-14 03:48:15.110200
# Unit test for method filter of class Try
def test_Try_filter():
    assert(Try(None, True).filter(lambda v: False) == Try(None, False))
    assert(Try(None, True).filter(lambda v: True) == Try(None, True))
    assert(Try(None, False).filter(lambda v: False) == Try(None, False))
    assert(Try(None, False).filter(lambda v: True) == Try(None, False))
    assert(Try(None, True).filter(lambda v: False) != Try(None, False))
    assert(Try(None, True).filter(lambda v: True) == Try(None, True))
    assert(Try(None, False).filter(lambda v: False) == Try(None, False))
    assert(Try(None, False).filter(lambda v: True) == Try(None, False))


# Generated at 2022-06-14 03:48:19.300448
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test function for method filter of class Try.

    >>> t = Try(10, True)
    >>> assert(t.get() == 10)
    >>> t.filter(lambda x: x > 10)
    Try[value=10, is_success=False]
    >>> t.filter(lambda x: x < 10)
    Try[value=10, is_success=True]
    """
    pass

# Generated at 2022-06-14 03:48:34.367199
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: '42', None).filter(lambda value: value == '42') == Try('42', True)
    assert Try.of(lambda: '42', None).filter(lambda value: value == '43') == Try('42', False)
    assert Try.of(lambda: 42 / 0, None).filter(lambda value: value == '43') == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:48:38.569496
# Unit test for method filter of class Try
def test_Try_filter():

    # Prepare data for test method
    value = 1
    result = 2
    filterer = lambda x: (x + 1) % 2 == 0

    # Test method filter
    assert Try(value, True).filter(filterer) == Try(value, False), 'Test Try.filter: monad value is higher than filterer function.'
    assert Try(result, True).filter(filterer) == Try(result, True), 'Test Try.filter: monad value is lower than filterer function.'



# Generated at 2022-06-14 03:48:41.303273
# Unit test for method filter of class Try
def test_Try_filter():
    # Test positive case, when filterer returns True and monad is successfully
    assert Try(4, True).filter(lambda n: n % 2 == 0)\
        == Try(4, True)
    # Test negative case, when filterer returns False and monad is successfully
    assert Try(3, True).filter(lambda n: n % 2 == 0)\
        == Try(3, False)


# Generated at 2022-06-14 03:48:46.199999
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """
    assert Try(5, True).filter(lambda value: value > 0) == Try(5, True)
    assert Try(5, True).filter(lambda value: value < 0) == Try(5, False)
    assert Try(5, False).filter(lambda value: value < 0) == Try(5, False)



# Generated at 2022-06-14 03:48:54.810301
# Unit test for method filter of class Try
def test_Try_filter():
    t = Try.of(lambda: '2', 2)
    assert isinstance(t.filter(lambda x: True), Try)
    assert isinstance(t.filter(lambda x: False), Try)

    t = Try.of(lambda: '2', 2)
    assert t.filter(lambda x: True) == Try('2', True)
    assert t.filter(lambda x: False) == Try('2', False)

    t = Try.of(lambda: '2', 2)
    assert t.filter(lambda x: True).get() == '2'
    assert t.filter(lambda x: False).get() == '2'



# Generated at 2022-06-14 03:49:05.207261
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x > 0) == Try(10, True)
    assert Try(10, True).filter(lambda x: x > 5) == Try(10, True)
    assert Try(10, True).filter(lambda x: x < 0) == Try(10, False)
    assert Try(10, True).filter(lambda x: x < 5) == Try(10, False)
    assert Try(10, False).filter(lambda x: x > 0) == Try(10, False)
    assert Try(10, False).filter(lambda x: x > 5) == Try(10, False)
    assert Try(10, False).filter(lambda x: x < 0) == Try(10, False)
    assert Try(-10, False).filter(lambda x: x < 0) == Try(-10, False)

# Generated at 2022-06-14 03:49:09.373089
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method.
    """
    def greater_than_5(x):
        return x >= 5

    assert Try.of(lambda: 10).filter(greater_than_5) == Try(10, True)
    assert Try.of(lambda: 4).filter(greater_than_5) == Try(4, False)



# Generated at 2022-06-14 03:49:20.043636
# Unit test for method filter of class Try
def test_Try_filter():
    def is_success_when_value_is_positive_int(value):
        return type(value) == int and value > 0

    assert Try.of(int, 1).filter(is_success_when_value_is_positive_int) == Try(1, True)
    assert Try.of(int, 1).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(int, -1).filter(is_success_when_value_is_positive_int) == Try(-1, False)
    assert Try.of(int, 0).filter(is_success_when_value_is_positive_int) == Try(0, False)
    assert Try.of(int, '1').filter(is_success_when_value_is_positive_int) == Try('1', False)

# Generated at 2022-06-14 03:49:27.840128
# Unit test for method filter of class Try
def test_Try_filter():
    try_success = Try.of(lambda x: x, 1)
    try_fail = Try.of(lambda x: 1 / 0, 1)

    assert try_success.filter(lambda x: x == 1) == Try(1, True)
    assert try_success.filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda x: 1 / 0, 1).filter(lambda x: x == 1) == Try.of(lambda x: 1 / 0, 1)



# Generated at 2022-06-14 03:49:34.486080
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x > 9) == Try(10, True)
    assert Try(10, True).filter(lambda x: x <= 9) == Try(10, False)
    assert Try(10, False).filter(lambda x: x > 9) == Try(10, False)
    assert Try(Exception('error message'), False).filter(lambda x: x > 9) == Try(Exception('error message'), False)



# Generated at 2022-06-14 03:49:58.984933
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Method filter should return copy of monad when filterer returns True.
    Othercase return not successfully monad.
    """
    try_a = Try.of(lambda a: a, 3)
    try_b = Try.of(lambda a: a, 4)
    true_filterer = lambda a: a % 2 == 0

    assert try_a.filter(true_filterer).is_success == False
    assert try_b.filter(true_filterer).is_success == True


# Generated at 2022-06-14 03:50:08.635023
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda v: True) == Try(42, True)
    assert Try(42, True).filter(lambda v: False) == Try(42, False)
    assert Try(42, False).filter(lambda v: True) == Try(42, False)
    assert Try(None, False).filter(lambda v: True) == Try(None, False)
    assert Try(None, False).filter(lambda v: False) == Try(None, False)


# Generated at 2022-06-14 03:50:11.405122
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda x: x == 42) == Try(42, True)
    assert Try(42, True).filter(lambda x: x != 42) == Try(42, False)
    assert Try(42, False).filter(lambda x: x == 42) == Try(42, False)



# Generated at 2022-06-14 03:50:15.079161
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, 1).filter(lambda value: True) == Try(value=1, is_success=True)
    assert Try.of(lambda: 1, 1).filter(lambda value: False) == Try(value=1, is_success=False)


# Generated at 2022-06-14 03:50:19.079545
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda a: a % 2 == 0) == Try(42, True)
    assert Try(43, True).filter(lambda a: a % 2 == 0) == Try(43, False)

# Generated at 2022-06-14 03:50:24.977503
# Unit test for method filter of class Try
def test_Try_filter():
    m1 = Try.of(lambda a: a ** 2, 2)
    result1 = m1.filter(lambda x: x % 2 == 0)
    assert result1 == Try(4, True)

    result2 = result1.filter(lambda x: x % 3 == 0)
    assert result2 == Try(4, False)

# Generated at 2022-06-14 03:50:34.634010
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Filter is useful to filter value of monad.
    """
    # filter for int values
    def is_int(value):
        return isinstance(value, int)

    # first of all make sure that value is int
    # when value is int make sure that value not greater than 0
    def is_positive_int(value):
        return isinstance(value, int) and value > 0

    t = Try.of(lambda x: int(x), '1')
    assert t.filter(is_int) == Try(1, True)

    t = Try.of(lambda x: int(x), 's')
    assert t.filter(is_int) == Try('s', False)

    t = Try.of(lambda x: int(x), '1')

# Generated at 2022-06-14 03:50:40.649526
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(None, True).filter(lambda val: val is None) == Try(None, True)
    assert Try(None, True).filter(lambda val: val is not None) == Try(None, False)
    assert Try(None, False).filter(lambda val: val is None) == Try(None, False)



# Generated at 2022-06-14 03:50:44.983060
# Unit test for method filter of class Try
def test_Try_filter():
    # Arrange
    t = Try.of(lambda x: x * x, 2)

    # Act
    t2 = t.filter(lambda x: x > 5)

    # Assert
    assert t2.is_success == False



# Generated at 2022-06-14 03:50:53.368291
# Unit test for method filter of class Try
def test_Try_filter():
    """
    :returns: True when all tests are successfully, othercase False
    :rtype: Boolean
    """
    assert Try.of(lambda: 1 / 0, None).filter(lambda x: x > 0) == Try(None, False)
    assert Try.of(lambda: 1 / 0, None).filter(lambda x: x > 1) == Try(None, False)
    assert Try.of(lambda: 1 / 1, None).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(lambda: 1 / 1, None).filter(lambda x: x > 1) == Try(1, False)
    print('Test for method filter of class Try is successfully')
    return True


# Generated at 2022-06-14 03:51:38.593917
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        try:
            return x == 2
        except Exception as e:
            return False

    assert(Try(2, True).filter(filterer) == Try(2, True))
    assert(Try(2, True).filter(filterer).get() == 2)
    assert(Try(3, True).filter(filterer) == Try(3, False))
    assert(Try(3, True).filter(filterer).get_or_else(2) == 2)
    assert(Try(2, False).filter(filterer) == Try(2, False))
    assert(Try(2, False).filter(filterer).on_fail(lambda x: print("Exception: {}".format(x))))

# Generated at 2022-06-14 03:51:46.176342
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 2) == Try(1, False)
    assert Try(2, False).filter(lambda x: x == 1) == Try(2, False)


# Generated at 2022-06-14 03:51:54.192702
# Unit test for method filter of class Try
def test_Try_filter():
    from math import sqrt
    from copy import copy

    value = 100
    value_c = copy(value)

    def filterer(value):
        return sqrt(value) < 10

    try_ = Try.of(lambda v: v, value)

    try_ = try_.filter(filterer)

    assert try_.value == value_c
    assert try_.is_success

    try_ = try_.filter(filterer)

    assert try_.value == value_c
    assert not try_.is_success



# Generated at 2022-06-14 03:52:01.266460
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test method filter of class Try
    """
    t = Try.of(lambda a: a, 10)
    t1 = t.filter(lambda a: a == 10)
    t2 = t.filter(lambda a: a == 5)

    assert t1 == Try(10, True)
    assert t2 == Try(10, False)


# Generated at 2022-06-14 03:52:09.473447
# Unit test for method filter of class Try
def test_Try_filter():
    def fn():
        raise Exception('error')

    def with_arguments(arg1, arg2):
        raise Exception('error')

    def filterer(value):
        # it can be any other predicate for filtering
        return value > 7

    assert Try.of(fn) == Try(Exception('error'), False)
    assert Try.of(fn).map(lambda x: x + 3) == Try(fn(), False)
    assert Try.of(fn).bind(lambda x: Try(x + 3, False)) == Try(fn(), False)
    assert Try.of(fn).filter(lambda x: x > 5) == Try(fn(), False)

    assert Try.of(lambda: 3) == Try(3, True)

# Generated at 2022-06-14 03:52:15.934654
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    test_list = [1, 2, 3, 4, 5]
    def filter_func(value):
        if value % 2 == 0:
            return True
        return False
    value = Try.of(lambda: random.choice(test_list)).filter(filter_func)
    assert value == Try(2, True)

# Generated at 2022-06-14 03:52:24.094514
# Unit test for method filter of class Try
def test_Try_filter():
    # When monad is successfully
    x = Try(1, True)
    assert x.filter(lambda x: x > 0) == Try(1, True)

    # When monad is not successfully
    x = Try("error", False)
    assert x.filter(lambda x: x > 0) == Try("error", False)

    # When filterer return false
    x = Try(1, True)
    assert x.filter(lambda x: x < 0) == Try(1, False)



# Generated at 2022-06-14 03:52:27.713641
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x + 1, 1).filter(lambda x: x == 2) == Try(2, True)
    assert Try.of(lambda x: x + 1, 1).filter(lambda x: x == 3) == Try(2, False)


# Generated at 2022-06-14 03:52:32.441686
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda:10).filter(lambda x: x > 5) == Try(10, True)
    assert Try.of(lambda:10).filter(lambda x: x > 20) == Try(10, False)
    assert Try.of(lambda:20).filter(lambda x: x > 20) == Try(20, False)
    assert Try.of(lambda:None).filter(lambda x: x > 5) == Try(None, False)



# Generated at 2022-06-14 03:52:38.719012
# Unit test for method filter of class Try
def test_Try_filter():
    # just dummy function
    def dummy_func():
        return True

    # filter testing
    # Success(A) and filterer return True
    assert Try(True, True).filter(dummy_func()) == True

    # Success(A) and filterer return False
    assert Try(True, True).filter(dummy_func()).is_success == False
    assert Try(True, True).filter(dummy_func()).get() == True

    try:
        # Fail(A) and filterer return True
        assert Try(True, False).filter(dummy_func()) == False
        assert False
    except:
        assert True


# Generated at 2022-06-14 03:54:09.558996
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value

    def does_not_exist_filter(value):
        return False

    def exists_filter(value):
        return True

    def non_callable_filter(value):
        return value

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(2, False).filter(does_not_exist_filter) == Try(2, False)
    assert Try(3, True).filter(does_not_exist_filter) == Try(3, False)
    assert Try(4, True).filter(exists_filter) == Try(4, True)
    assert Try(5, False).filter(exists_filter) == Try(5, False)

# Generated at 2022-06-14 03:54:13.134755
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value % 2 == 0
    assert Try(2, True).filter(filterer) == Try(2, True)
    assert Try(1, True).filter(filterer) == Try(1, False)
    assert Try(1, False).filter(filterer) == Try(1, False)


# Generated at 2022-06-14 03:54:25.187477
# Unit test for method filter of class Try
def test_Try_filter():
    """ Should return not successfull Try"""
    f = lambda arg: arg < 5
    result = Try.of(lambda: 2).filter(f)
    expected = Try(2, False)
    assert result == expected

    """ Should return not successfull Try"""
    f = lambda arg: arg < 5
    result = Try.of(lambda: 2).filter(f)
    expected = Try(2, False)
    assert result == expected

    """ Should return successfull Try"""
    f = lambda arg: arg < 5
    result = Try.of(lambda: 3).filter(f)
    expected = Try(3, True)
    assert result == expected

    """ Should return not successfull Try"""
    f = lambda arg: arg < 5
    result = Try.of(lambda: 2).filter(f)