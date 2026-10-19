

# Generated at 2022-06-14 03:44:26.571623
# Unit test for method filter of class Try
def test_Try_filter():
    # Arrange
    my_try = Try.of(lambda: 10 / 0, None)

    # Act
    res = my_try.filter(lambda x: x == 2)


    # Assert
    assert res == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:44:34.776811
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(v: int) -> bool:
        if v % 2 == 0:
            return True
        return False

    try_object = Try.of(lambda x: x**2, 2)
    assert try_object.filter(filterer) == try_object
    assert try_object == Try(4, True)

    try_object = Try.of(lambda x, y: x + y, 1, 2)
    assert try_object.filter(filterer) == Try(3, False)
    assert try_object == Try(3, True)

    try_object = Try.of(lambda x: int('wrong_data'))
    assert try_object.filter(filterer) == Try(int('wrong_data'), False)
    assert try_object == Try(int('wrong_data'), False)

#

# Generated at 2022-06-14 03:44:39.816140
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, True).filter(lambda x: False) == Try(1, False)
    assert Try(1, False).filter(lambda x: True) == Try(1, False)
    assert Try(1, False).filter(lambda x: False) == Try(1, False)


# Generated at 2022-06-14 03:44:50.809083
# Unit test for method filter of class Try
def test_Try_filter():
    """Test filter method

    The filter method allows us to call filterer function with
    monad value, when function return False, method returns not
    successfully Try with previous value.

    :returns: Nothing.
    :rtype: None
    """
    # Successfully Try
    assert Try(1, True).filter(lambda i: i == 1) == Try(1, True), \
        'Try[1] should be filtered by function that return True'

    assert Try(1, True).filter(lambda i: i != 1) == Try(1, False), \
        'Try[1] should not be filtered by function that return False'


# Generated at 2022-06-14 03:44:56.002775
# Unit test for method filter of class Try
def test_Try_filter():
    def identity(x):
        return x

    def filterer(x):
        return x < 0

    monad = Try.of(identity, -1)
    assert monad.filter(filterer) == Try(-1, True)

    monad = Try.of(identity, 1)
    assert monad.filter(filterer) == Try(1, False)


# Generated at 2022-06-14 03:45:04.159507
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda a: a, 5).filter(lambda x: x > 0)\
        == Try.of(lambda a: a, 5)
    assert Try.of(lambda a: a, 5).filter(lambda x: x > 10)\
        == Try(5, False)
    assert Try.of(lambda a: a, 0).filter(lambda x: x > 0)\
        == Try(0, True)
    assert Try.of(lambda a: a, -5).filter(lambda x: x > 0)\
        == Try(-5, False)



# Generated at 2022-06-14 03:45:09.568517
# Unit test for method filter of class Try
def test_Try_filter():
    value = 'value'
    try_value = Try(value, True)

    assert try_value.filter(lambda x: x == value) == try_value
    assert try_value.filter(lambda x: x != value) == Try(value, False)
    assert Try(value, False).filter(lambda x: x == value) == Try(value, False)

# Generated at 2022-06-14 03:45:16.915171
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.

    :returns: assert when test finished.
    :rtype: Assertion
    """

    def filterer(value):
        """
        Function to call when test.

        :params value: test value.
        :type value: Integer
        :return: value < 3
        :rtype: Boolean
        """
        return value < 3

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(1, False).filter(filterer) == Try(1, False)
    assert Try(4, True).filter(filterer) == Try(4, False)
    assert Try(4, False).filter(filterer) == Try(4, False)

    return True



# Generated at 2022-06-14 03:45:22.860534
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value != 0

    monad = Try(0, True)
    assert monad.filter(filterer) == Try(0, False)

    monad = Try(1, True)
    assert monad.filter(filterer) == Try(1, True)



# Generated at 2022-06-14 03:45:26.656137
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)
    assert Try(1, False) == Try(1, False)

# Generated at 2022-06-14 03:45:32.266468
# Unit test for method filter of class Try
def test_Try_filter():
    # Test when successful
    value = 5
    is_success = True
    _Try = Try(value, is_success)

    filterer = lambda v: v > 0
    assert _Try.filter(filterer) == _Try

    # Test when fail
    filterer = lambda v: v < 0
    assert _Try.filter(filterer) == Try(value, False)

    # Test when fail
    _Try = Try(value, False)
    assert _Try.filter(filterer) == _Try


if __name__ == '__main__':  # pragma: no cover
    test_Try_filter()

# Generated at 2022-06-14 03:45:38.108756
# Unit test for method filter of class Try
def test_Try_filter():
    def is_greater_than_zero(num):
        return num > 0

    assert Try(1, True).filter(is_greater_than_zero) == Try(1, True)
    assert Try(-1, True).filter(is_greater_than_zero) == Try(-1, False)
    assert Try(1, False).filter(is_greater_than_zero) == Try(1, False)
    assert Try(-1, False).filter(is_greater_than_zero) == Try(-1, False)


# Unit tests for method bind of class Try

# Generated at 2022-06-14 03:45:45.546477
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try

    :returns: None
    :rtype: None
    """
    assert Try.of(lambda x, y: x + y, 1, 2).filter(lambda x: x > 3).is_success is False
    assert Try.of(lambda x, y: x + y, 1, 2).filter(lambda x: x > 1).is_success is True


# Generated at 2022-06-14 03:45:49.758267
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(int, '5').filter(lambda x: type(x) == int) == Try(5, True)
    assert Try.of(int, 'a').filter(lambda x: type(x) == int) == Try('a', False)


# Generated at 2022-06-14 03:45:54.140197
# Unit test for method filter of class Try
def test_Try_filter():
    result = Try.of(int, 'abc')\
        .filter(lambda x: x < 10)

    assert result != Try(123, True)
    assert result == Try(123, False)


# Generated at 2022-06-14 03:46:04.516836
# Unit test for method filter of class Try
def test_Try_filter():
    def _test_filter_true():
        actual = Try.of(lambda x: x)
        expected = Try(None, True)
        assert actual.filter(lambda x: True) == expected

    def _test_filter_false():
        actual = Try.of(lambda x: x)
        expected = Try(None, False)
        assert actual.filter(lambda x: False) != expected

    def _test_filter_fn_return_bool():
        actual = Try.of(lambda x: x)
        expected = Try(None, True)
        assert actual.filter(lambda x: "True") == expected

    _test_filter_true()
    _test_filter_false()
    _test_filter_fn_return_bool()



# Generated at 2022-06-14 03:46:08.850184
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda x: x%2 == 0) == Try(42, True)
    assert Try(42, True).filter(lambda x: x%2 == 1) == Try(42, False)
    assert Try(Exception(), False).filter(lambda x: True) == Try(Exception(), False)
    assert Try(42, True).filter(lambda x: x%2 == 1).filter(lambda x: True) == Try(42, False)


# Generated at 2022-06-14 03:46:16.695730
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 10).filter(lambda x: x > 5) == Try(10, True)
    assert Try.of(lambda: 10).filter(lambda x: x < 5) == Try(10, False)

    for i in range(1, 10):
        assert Try.of(lambda: 10 / i).filter(lambda x: x > 5) == Try(10 / i, True)
        assert Try.of(lambda: 10 / i).filter(lambda x: x <= 5) == Try(10 / i, False)



# Generated at 2022-06-14 03:46:20.377516
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda v: v > 2) == Try(1, False)
    assert Try(2, True).filter(lambda v: v > 2) == Try(2, False)
    assert Try(3, True).filter(lambda v: v > 2) == Try(3, True)


# Generated at 2022-06-14 03:46:24.663929
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True)\
        .filter(lambda x: x > 0)\
        == Try(1, True)

    assert Try(1, True)\
        .filter(lambda x: x == 1)\
        == Try(1, True)

    assert Try(1, True)\
        .filter(lambda x: x < 0)\
        == Try(1, False)

    assert Try(1, False)\
        .filter(lambda x: x > 0)\
        == Try(1, False)


# Generated at 2022-06-14 03:46:31.514980
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    t = Try(10, True)
    # When
    result = t.filter(lambda i: i > 5)
    # Then
    assert result == Try(10, True)



# Generated at 2022-06-14 03:46:37.612869
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def print_result(result):
        print(result)

    def filterer(value):
        return value % 2 == 0

    assert Try(1, True).filter(filterer) == Try(1, False)
    assert Try(2, True).filter(filterer) == Try(2, True)


if __name__ == '__main__':
    test_Try_filter()  # pragma: no cover

# Generated at 2022-06-14 03:46:44.328653
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value > 2

    assert Try(1, True).filter(filterer) == Try(1, False)
    assert Try(2, True).filter(filterer) == Try(2, False)
    assert Try(3, True).filter(filterer) == Try(3, True)



# Generated at 2022-06-14 03:46:48.382592
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    a = Try.of(lambda: 2, )
    assert a.filter(lambda x: x > 0) == a
    assert a.filter(lambda x: x < 1) == Try(2, False)



# Generated at 2022-06-14 03:46:52.941806
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 0) == Try(5, True)
    assert Try(5, True).filter(lambda x: x <= 0) == Try(5, False)
    assert Try(0, True).filter(lambda x: x > 0) == Try(0, False)
    assert Try(0, True).filter(lambda x: x <= 0) == Try(0, True)



# Generated at 2022-06-14 03:47:01.306408
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test method filter of class Try.
    """
    # Assert filter with suitable argument
    assert Try.of(str, 2).filter(lambda x: x == '2') == Try('2', True)

    # Assert filter with unsuitable argument
    assert Try.of(str, 3).filter(lambda x: x == '2') == Try('3', False)

    # Assert filter with unsuccessful monad
    assert Try(Exception(), False).filter(lambda x: x == '2') == Try(Exception(), False)


# Generated at 2022-06-14 03:47:04.938959
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x < 4) == Try(5, False)
    assert Try(5, True).filter(lambda x: x > 4) == Try(5, True)
    assert Try(5, False).filter(lambda x: x < 4) == Try(5, False)



# Generated at 2022-06-14 03:47:11.466922
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    try_ = Try(12, True)
    negative_number = -1
    is_positive = lambda x: x > 0
    is_negative = lambda x: x < 0

    # When
    try_positive = try_.filter(is_positive)
    try_negative = Try(negative_number, True).filter(is_negative)

    # Then
    assert try_positive == Try(12, True)
    assert try_negative == Try(-1, False)



# Generated at 2022-06-14 03:47:19.184672
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """

    with pytest.raises(TypeError):
        # Test 1: raise TypeError on call None with None
        Try.of(lambda x: x, None).filter(None)

    with pytest.raises(TypeError):
        # Test 2: raise TypeError when call None with not callable
        Try.of(lambda x: x, None).filter(1)

    with pytest.raises(TypeError):
        # Test 3: raise TypeError on call "Hello" with not callable
        Try.of(lambda x: x, "Hello").filter(1)


# Generated at 2022-06-14 03:47:25.408508
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(number):
        return number % 2 == 0

    try_1 = Try.of(int, '10')
    assert try_1.filter(filterer) == Try(10, True)

    try_2 = Try.of(int, '11')
    assert try_2.filter(filterer) == Try(11, False)

    try_3 = Try.of(int, 'abc')
    assert try_3.filter(filterer) == Try('abc', False)


# Generated at 2022-06-14 03:47:44.627897
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of class Try.

    :returns: No returns
    :rtype: void
    """
    assert Try(14, True).filter(lambda x: x is 14) == Try(14, True)
    assert Try(None, True).filter(lambda x: False) == Try(None, False)
    assert Try(None, True).filter(lambda x: True) == Try(None, True)
    assert Try(14, False).filter(lambda x: x is 14) == Try(14, False)
    assert Try(None, False).filter(lambda x: False) == Try(None, False)
    assert Try(None, False).filter(lambda x: True) == Try(None, False)
    print('test_Try_filter - ok')



# Generated at 2022-06-14 03:47:50.614963
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, False).filter(lambda x: x > 5) == Try(1, False)
    assert Try(10, True).filter(lambda x: x > 5) == Try(10, True)
    assert Try(1, True).filter(lambda x: x > 5) == Try(1, False)

# Generated at 2022-06-14 03:47:56.688782
# Unit test for method filter of class Try
def test_Try_filter():
    old_value = 'abc'
    not_successful_try = Try(old_value, False)
    assert not_successful_try.filter(lambda x: True) == Try(old_value, False)

    not_match_filter_try = Try(old_value, True)
    assert not_successful_try.filter(lambda x: False) == Try(old_value, False)

    match_filter_try = Try(old_value, True)
    assert match_filter_try.filter(lambda x: True) == match_filter_try

# Generated at 2022-06-14 03:48:06.672575
# Unit test for method filter of class Try
def test_Try_filter():
    t_s = Try.of(int, 1)
    assert t_s.filter(lambda x: x > 0).value == 1
    assert not t_s.filter(lambda x: x > 1).is_success
    t_f = Try.of(int, 'll')
    assert t_f.filter(lambda x: x > 0).value == 'll'
    assert not t_f.filter(lambda x: x > 1).is_success
    assert t_f.filter(lambda x: x > 0).value == t_f.value
    assert not t_f.filter(lambda x: x > 1).is_success == t_f.is_success


# Generated at 2022-06-14 03:48:14.488047
# Unit test for method filter of class Try
def test_Try_filter():
    frothy_monad = Try(45.0, True)
    assert frothy_monad.filter(lambda x: x == 45.0) == Try(45.0, True)
    assert frothy_monad.filter(lambda x: x == 'not 45.0') == Try(45.0, False)
    frothy_monad = Try(45.0, False)
    assert frothy_monad.filter(lambda x: x == 45.0) == Try(45.0, False)
    assert frothy_monad.filter(lambda x: x == 'not 45.0') == Try(45.0, False)



# Generated at 2022-06-14 03:48:26.228055
# Unit test for method filter of class Try
def test_Try_filter(): #pragma: no cover
    def safe_get_value(key):
        """
        Function defines dictionary, return value with specified key.

        :params key: key to return value
        :type key: str
        """
        d = {'a': 1, 'b': 2, 'c': 3}
        return d.get(key, None)

    # when key is exists in dictionary return successfully Try with value
    assert Try.of(safe_get_value, 'a').filter(lambda x: x > 1) == Try(1, False)
    # when key is exists in dictionary return successfully Try with value
    assert Try.of(safe_get_value, 'b').filter(lambda x: x > 1) == Try(2, True)
    # when key is not exists in dictionary return not successfully Try with exception

# Generated at 2022-06-14 03:48:34.601961
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda: 1, None).filter(lambda x: True) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(lambda x: False) == Try(1, False)
    assert Try.of(lambda: 1 / 0, None).filter(lambda x: True) == Try(ZeroDivisionError("division by zero"), False)
    assert Try.of(lambda: 1 / 0, None).filter(lambda x: False) == Try(ZeroDivisionError("division by zero"), False)

# Generated at 2022-06-14 03:48:37.126686
# Unit test for method filter of class Try
def test_Try_filter():
    answer = Try(42, True)
    even = answer.filter(lambda x: x % 2 == 0)
    odd = answer.filter(lambda x: x % 2 != 0)

    assert even == answer
    assert odd != answer

# Generated at 2022-06-14 03:48:43.329170
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)



# Generated at 2022-06-14 03:48:47.192996
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> def filter_func(x):
    ...     return x > 10
    ...
    >>> Success(11).filter(filter_func).get()
    11
    >>> Success(9).filter(filter_func).is_success
    False
    >>> Failure('fail').filter(filter_func).is_success
    False
    """
    pass



# Generated at 2022-06-14 03:49:05.849256
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> test_Try_filter()
    True
    """
    is_digit = lambda v: Try(int(v), True) if v.isdigit() else Try(None, False)
    is_even = lambda v: v % 2 == 0

    assert Try.of(lambda x: x, '2') | is_digit.bind | is_even.bind | (lambda v: Try(v, True)) == Try(True, True)
    assert Try.of(lambda x: x, '2') | is_digit.bind | is_even.bind | (lambda v: Try(v, False)) == Try(False, True)

# Generated at 2022-06-14 03:49:09.453611
# Unit test for method filter of class Try
def test_Try_filter():
    def is_odd(x):
        return x % 2 == 0
    assert Try(10, True).filter(is_odd) == Try(10, True)
    assert Try(9, True).filter(is_odd) == Try(9, False)
    assert Try(10, False).filter(is_odd) == Try(10, False)

# Generated at 2022-06-14 03:49:17.415325
# Unit test for method filter of class Try
def test_Try_filter():
    def upper(value: str) -> str:
        return value.upper()

    def is_contains_a(value: str) -> bool:
        return 'a' in value

    actual = Try.of(upper, 'foo').filter(is_contains_a)
    expected = Try('FOO', False)
    assert actual == expected

    actual = Try.of(upper, 'bar').filter(is_contains_a)
    expected = Try('BAR', True)
    assert actual == expected



# Generated at 2022-06-14 03:49:25.988161
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ).filter(lambda v: v == 1)\
        == Try(1, True)
    assert Try.of(lambda: 1, ).filter(lambda v: v != 1)\
        == Try(1, False)
    assert Try.of(lambda: 1, ).filter(lambda v: v == 1)\
        != Try(1, False)
    assert Try.of(lambda: 1, ).map(lambda v: v + 1).filter(lambda v: v == 2)\
        == Try(2, True)
    assert Try.of(lambda: 1, ).filter(lambda v: v == 2)\
        == Try(1, False)


# Generated at 2022-06-14 03:49:33.356586
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(int, "5").filter(lambda value: value > 2) == Try(5, True)
    assert Try.of(int, "5").filter(lambda value: value < 2) == Try(5, False)
    assert Try.of(int, "abc").filter(lambda value: value > 2) == Try("abc", False)
    assert Try.of(int, "abc").filter(lambda value: value < 2) == Try("abc", False)

# Generated at 2022-06-14 03:49:43.056134
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> def div2(x):
    ...     return x // 2
    >>> Empty(1) >> div2 >> div2 >> div2 >> div2
    Try[value=1, is_success=False]
    >>> Success(1) >> div2 >> div2 >> div2 >> div2
    Try[value=0, is_success=True]
    >>> SafeTry(lambda: 1, 1) >> div2 >> div2 >> div2 >> div2
    Try[value=0, is_success=True]
    >>> SafeTry(lambda: 1 / 0, 1) >> div2 >> div2 >> div2 >> div2
    Try[value=1, is_success=False]
    """



# Generated at 2022-06-14 03:49:45.372911
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(2, True).filter(lambda value: value < 3) == Try(2, True)
    assert Try(2, True).filter(lambda value: value > 3) == Try(2, False)



# Generated at 2022-06-14 03:49:52.465865
# Unit test for method filter of class Try
def test_Try_filter():
    def f(value):
        if value % 2 == 0:
            return True
        return False
    assert Try(2, True).filter(f) == Try(2, True)
    assert Try(4, True).filter(f) == Try(4, True)
    assert Try(8, True).filter(f) == Try(8, True)
    assert Try(3, True).filter(f) == Try(3, False)
    assert Try(5, True).filter(f) == Try(5, False)
    assert Try(7, True).filter(f) == Try(7, False)


# Generated at 2022-06-14 03:49:57.762585
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(number):
        return number > 5

    assert Try(8, True).filter(filterer) == Try(8, True)
    assert Try(4, True).filter(filterer) == Try(4, False)
    assert Try(Exception('error'), False).filter(filterer) == Try(Exception('error'), False)


# Generated at 2022-06-14 03:50:06.230397
# Unit test for method filter of class Try
def test_Try_filter():
    def test_lambda(val):
        return val > 10

    m1 = Try(9, True)
    m2 = Try(10, True)
    m3 = Try(11, True)

    assert m1.filter(test_lambda) == Try(9, False)
    assert m2.filter(test_lambda) == Try(10, False)
    assert m3.filter(test_lambda) == Try(11, True)



# Generated at 2022-06-14 03:50:23.963182
# Unit test for method filter of class Try
def test_Try_filter():

    def filterer(value):
        return value > 10

    assert(Try(None, False).filter(filterer) == Try(None, False))
    assert(Try(2, True).filter(filterer) == Try(2, False))
    assert(Try(10, True).filter(filterer) == Try(10, False))
    assert(Try(11, True).filter(filterer) == Try(11, True))


# Generated at 2022-06-14 03:50:33.924951
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> test_Try_filter()
    True
    """
    # Run test 1
    try:
        def raise_error():
            raise RuntimeError()
        assert Try.of(raise_error).filter(lambda _: True) == Try(RuntimeError(), False)
    except Exception as e: # pragma: no cover
        print(e)
        return False
    # Run test 2
    try:
        def return_1():
            return 1
        assert Try.of(return_1).filter(lambda _: True) == Try(1, True)
    except Exception as e: # pragma: no cover
        print(e)
        return False
    # Run test 3

# Generated at 2022-06-14 03:50:46.693904
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return x % 2 != 0

    # When
    try1 = Try(1, True).map(lambda x: x * 10)
    try2 = Try(1, True).map(lambda x: x * 10).filter(is_even)
    try3 = Try(2, True).map(lambda x: x * 10).filter(is_even)
    try4 = Try(2, True).map(lambda x: x * 10).filter(is_odd)

    # Then
    assert try1 == Try(10, True)
    assert try2 == Try(1, False)
    assert try3 == Try(20, True)
    assert try4 == Try(2, False)


# Generated at 2022-06-14 03:50:54.055027
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try.
    """
    assert Try(1, True).filter(lambda a: a == 1) == Try(1, True)
    assert Try(1, True).filter(lambda a: a == 2) == Try(1, False)
    assert Try(Exception('test'), False).filter(lambda a: a == 1) == Try(Exception('test'), False)



# Generated at 2022-06-14 03:51:01.287867
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x == 3

    assert Try(3, True).filter(filterer) == Try(3, True)
    assert Try(4, True).filter(filterer) == Try(4, False)
    assert Try(4, False).filter(filterer) == Try(4, False)
    assert Try(Exception(), False).filter(filterer) == Try(Exception(), False)



# Generated at 2022-06-14 03:51:08.132422
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test when filterer returns True.
    """
    def filterer(a: str) -> bool:
        return True

    assert Try.of(lambda: 'Try')\
        .filter(filterer)\
        .is_success

    """
    Test when filterer returns False.
    """
    def filterer(a: str) -> bool:
        return False

    assert not Try.of(lambda: 'Try')\
        .filter(filterer)\
        .is_success



# Generated at 2022-06-14 03:51:13.088848
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x > 1) == Try(2, True)
    assert Try(2, True).filter(lambda x: x < 1) == Try(2, False)
    assert Try(2, False).filter(lambda x: x > 1) == Try(2, False)
    assert Try(Exception('error'), False).filter(lambda x: isinstance(x, IOError)) == Try(Exception('error'), True)
    assert Try(Exception('error'), False).filter(lambda x: isinstance(x, Exception)) == Try(Exception('error'), False)



# Generated at 2022-06-14 03:51:19.733933
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value < 10

    assert Try(9, True).filter(filterer) == Try(9, True)
    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(11, True).filter(filterer) == Try(11, False)
    assert Try(9, False).filter(filterer) == Try(9, False)


# Generated at 2022-06-14 03:51:33.994370
# Unit test for method filter of class Try
def test_Try_filter():
    try_with_5 = Try(5, True)
    filtered_try_with_5 = try_with_5.filter(lambda x: x > 4)
    assert filtered_try_with_5 == try_with_5

    try_with_5 = Try(5, True)
    filtered_try_with_5 = try_with_5.filter(lambda x: x > 5)
    assert filtered_try_with_5 == Try(try_with_5.get(), False)

    try_with_5 = Try(5, False)
    filtered_try_with_5 = try_with_5.filter(lambda x: x > 4)
    assert filtered_try_with_5 == try_with_5

    try_with_5 = Try(5, False)
    filtered_try_with_5 = try_with_

# Generated at 2022-06-14 03:51:37.449576
# Unit test for method filter of class Try
def test_Try_filter():
    def filter_func(x: int) -> bool:
        return x < 2

    try_monad = Try(1, True)
    try_monad = try_monad.filter(filter_func)

    assert try_monad == Try(1, True)

    try_monad = Try(2, True)
    try_monad = try_monad.filter(filter_func)

    assert try_monad == Try(2, False)


# Generated at 2022-06-14 03:52:03.372961
# Unit test for method filter of class Try
def test_Try_filter():
    t = Try.of(lambda x: x, 1).filter(lambda x: x == 2)
    assert t == Try(1, False)
    t = Try.of(lambda x: x, 1).filter(lambda x: x == 1)
    assert t == Try(1, True)


# Generated at 2022-06-14 03:52:08.170273
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def positive(a):
        return a > 0

    def negative(a):
        return a < 0

    assert Try(0, True).filter(positive).is_success == False
    assert Try(0, True).filter(negative).is_success == False
    assert Try(1, True).filter(positive).is_success == True
    assert Try(1, True).filter(negative).is_success == False


# Generated at 2022-06-14 03:52:14.457736
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value: str) -> bool:
        return value == 'f'

    assert(Try("s", True).filter(filterer) == Try("s", False))
    assert(Try("f", True).filter(filterer) == Try("f", True))


# Generated at 2022-06-14 03:52:21.855894
# Unit test for method filter of class Try
def test_Try_filter():
    # Test with successfully monad
    assert(Try(2, True).filter(lambda x: x > 1).get() == 2)
    # Test with fail monad
    assert(Try(None, False).filter(lambda x: x > 1).get() == None)
    # Test with successfully monad but filterer returns False
    assert(Try(2, True).filter(lambda x: x < 1).get() == None)


# Generated at 2022-06-14 03:52:28.031395
# Unit test for method filter of class Try
def test_Try_filter():
    try1 = Try.of(lambda: 1)
    try2 = try1.filter(lambda x: x == 2)
    try3 = try1.filter(lambda x: x == 1)
    assert try2.is_success is False
    assert try3.is_success is True

    try1 = Try.of(lambda: 1)
    try2 = try1.filter(lambda x: x == 1)
    assert try2.is_success is True


# Generated at 2022-06-14 03:52:34.919754
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Run all the test cases for method filter on the class Try
    """
    assert Try(True, True).filter(bool) == Try(True, True)
    assert Try(False, True).filter(bool) == Try(False, False)
    assert Try(True, True).filter(lambda _: True) == Try(True, True)
    assert Try(True, True).filter(lambda _: False) == Try(True, False)


# Generated at 2022-06-14 03:52:44.545715
# Unit test for method filter of class Try
def test_Try_filter():
    to_int = lambda x: int(x)
    is_positive = lambda x: x > 0
    is_negative = lambda x: x < 0
    is_zero = lambda x: x == 0
    test_try = Try.of(to_int, '100500')
    assert test_try.filter(is_positive) == Try(100500, True)
    assert test_try.filter(is_negative) == Try(100500, False)
    assert test_try.filter(is_zero) == Try(100500, False)


# Generated at 2022-06-14 03:52:48.489137
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value == 'foo'

    assert Try('foo', True).filter(filterer) == Try('foo', True)
    assert Try('bar', True).filter(filterer) == Try('bar', False)
    assert Try('bar', False).filter(filterer) == Try('bar', False)



# Generated at 2022-06-14 03:52:57.992906
# Unit test for method filter of class Try
def test_Try_filter():
    e = Exception('Error!')
    div_5 = lambda x: x % 5 == 0
    plus_5 = lambda x: x + 5

    assert Try(15, True).filter(div_5).__eq__(Try(15, True))
    assert Try(15, True).filter(div_5).bind(plus_5).is_success
    assert Try(17, True).filter(div_5).bind(plus_5).__eq__(Try(17, False))
    assert Try(e, False).__eq__(Try(e, False))
    assert Try(-1, True).__eq__(Try(-1, True))

# Generated at 2022-06-14 03:53:03.814031
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test try-catch block.
    """
    def div(a, b):
        return a / b

    assert Try.of(div, 1, 2).filter(lambda a: a > 0) == Try(0.5, True)
    assert Try.of(div, 1, 0).filter(lambda a: a > 0) == Try(ZeroDivisionError, True)



# Generated at 2022-06-14 03:53:58.123422
# Unit test for method filter of class Try
def test_Try_filter():
    exc_handler = ExceptionHandler(lambda error: error.message)
    assert Try.of(lambda: 1, None).filter(lambda v: v == 1) == Success(1)
    assert Try.of(lambda: 1, None).filter(lambda v: v == 2) == Failure(1)
    assert Try.of(lambda: 1, None).filter(lambda v: v == 'str') == Failure(1)
    assert Try.of(lambda: 1, None).filter(lambda v: ''[2]) == Failure(1)
    assert Try.of(lambda: ''[2], None).filter(lambda v: ''[2]) == Failure(IndexError())
    assert Try.of(lambda: 1, None).map(lambda v: v + 1).filter(lambda v: v > 1) == Success(2)

# Generated at 2022-06-14 03:54:10.321557
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover

    def filter_function(x):
        return x == 1

    assert Try.of(lambda: 1).filter(filter_function) == Try(1, True)
    assert Try.of(lambda: 2).filter(filter_function) == Try(2, False)

    try:
        Try.of(lambda: 1 / 0).filter(filter_function)
    except ZeroDivisionError as e:
        assert Try(e, False) == Try(e, False)

    try:
        Try.of(lambda: 1 / 0, 0).filter(filter_function)
    except ZeroDivisionError as e:
        assert Try(e, False) == Try(e, False)


# Generated at 2022-06-14 03:54:16.811315
# Unit test for method filter of class Try
def test_Try_filter():
    def try_max(a, b):
        if a > b:
            return Try(a, True)
        return Try(b, True)

    def is_odd(a):
        return a % 2 == 1

    def is_even(a):
        return not is_odd(a)

    def is_right_rectangle(a, b):
        return a**2 + b**2 == 5

    assert try_max(1, 1).filter(is_even).is_success == False
    assert try_max(2, 1).filter(is_even).is_success == True
    assert try_max(2, 1).filter(is_odd).is_success == False
    assert try_max(1, 2).filter(is_odd).is_success == True

# Generated at 2022-06-14 03:54:24.798945
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter():
        assert Try(5, True).filter(lambda x: x == 5) == Try(5, True), \
            '[ERROR] Failed check filter function'
        assert Try(5, True).filter(lambda x: x == 4) == Try(5, False), \
            '[ERROR] Failed check filter function'
        assert Try(5, False).filter(lambda x: x == 4) == Try(5, False), \
            '[ERROR] Failed check filter function'
        print('test filter successful')

    test_filter()
