

# Generated at 2022-06-14 03:44:35.969203
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value: int):
        return value < 3

    assert Try(1, True).filter(filterer).is_success == True
    assert Try(4, True).filter(filterer).is_success == False
    assert Try(Exception('asd'), False).filter(filterer).is_success == False

# Generated at 2022-06-14 03:44:43.889437
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    class Error(Exception):
        """
            Custom error for error test.
        """
        pass

    def raise_error():
        raise Error()

    def correct_action():
        pass

    def filter_true(value):
        return value > 0

    def filter_false(value):
        return value < 0

    # When
    test_with_raise_error = Try.of(raise_error, None)
    test_with_correct_action = Try.of(correct_action, None)
    try_true = Try.of(lambda: 1, None)
    try_false = Try.of(lambda: -1, None)

    # Then
    assert test_with_raise_error.filter(filter_true).is_success == False

# Generated at 2022-06-14 03:44:53.238634
# Unit test for method filter of class Try
def test_Try_filter():
    try_value = Try.of(int, 'a')
    try_value_filtered = try_value.filter(lambda x: isinstance(x, int))
    assert try_value_filtered.is_success == False
    assert try_value_filtered.value == 'a'

    try_value = Try.of(int, '1')
    assert try_value.is_success == True
    assert isinstance(try_value.value, int)

    try_value_filtered = try_value.filter(lambda x: isinstance(x, int))
    assert try_value_filtered.is_success == True
    assert isinstance(try_value_filtered.value, int)

    try_value_filtered = try_value.filter(lambda x: isinstance(x, str))
    assert try_value_

# Generated at 2022-06-14 03:44:57.287160
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try
    """
    result = Try.of(lambda: 10 / 2)
    result = result.filter(lambda x: x == 5)
    expected = Try(5, True)

    assert result == expected

    result = Try.of(lambda: 10 / 2)
    result = result.filter(lambda x: x == 10)
    expected = Try(10, False)

    assert result == expected

# Generated at 2022-06-14 03:45:05.013328
# Unit test for method filter of class Try
def test_Try_filter():
    counter = 0
    inc_counter = lambda: counter + 1

    assert Try.of(inc_counter)\
        .filter(lambda cnt: cnt > 0) == Try(1, True)
    assert Try.of(inc_counter)\
        .filter(lambda cnt: cnt < 0) == Try(1, False)


# Generated at 2022-06-14 03:45:12.014600
# Unit test for method filter of class Try
def test_Try_filter():
    actual = Try.of(lambda x: x, 1)\
        .filter(lambda x: x > 0)\
        .get()
    assert actual == 1

    actual = Try.of(lambda x: int(x), '1')\
        .filter(lambda x: x > 0)\
        .get()
    assert actual == 1

    actual = Try.of(lambda x: int(x), 'x')\
        .filter(lambda x: x > 0)\
        .get()
    assert actual == 'x'


# Generated at 2022-06-14 03:45:14.766402
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try.of(lambda _: 5, None).filter(lambda _: True) == Try(5, True)
    assert Try.of(lambda _: 5, None).filter(lambda _: False) == Try(5, False)

# Generated at 2022-06-14 03:45:16.631490
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)



# Generated at 2022-06-14 03:45:26.556637
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try

    :returns: True when all tests passed, otherwise raise error.
    :rtype: Boolean
    """
    try:
        def get_one():
            return 1

        assert Try.of(get_one).filter(lambda x: x > 1).is_success == False
        assert Try.of(get_one).filter(lambda x: x >= 1).is_success == True
        assert Try.of(get_one).filter(lambda x: x > 1).value == 1
        assert Try.of(get_one).filter(lambda x: x >= 1).value == 1

        return True
    except:
        return False


# Generated at 2022-06-14 03:45:33.518732
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try(2, True).filter(lambda x: x % 2 == 1) == Try(2, False)
    assert Try(list(), True).filter(lambda x: x == []) == Try(list(), False)
    assert Try(2, True).filter(lambda x: "a" == "a") == Try(2, True)
    assert Try(2, True).filter(lambda x: "a" == "b") == Try(2, False)



# Generated at 2022-06-14 03:45:46.172475
# Unit test for method filter of class Try
def test_Try_filter():
    # When filter with True then return successfully Try
    assert Try.of(lambda: 'Some string')\
        .filter(lambda v: True)\
        == Try('Some string', True)

    # When filter with False then return not successfully Try
    assert Try.of(lambda: 'Some string')\
        .filter(lambda v: False)\
        == Try('Some string', False)

    # When monad is not successfully then return copy
    assert Try.of(lambda: 1 / 0)\
        .filter(lambda v: True)\
        == Try(ZeroDivisionError('division by zero'), False)



# Generated at 2022-06-14 03:45:51.184916
# Unit test for method filter of class Try
def test_Try_filter():
    def successful_filter(value):
        return value == 10

    assert Try.of(lambda: 10).filter(successful_filter) == Try(10, True)
    assert Try.of(lambda: 12).filter(successful_filter) == Try(12, False)

    with pytest.raises(Exception):
        Try.of(lambda: raise_exception()).filter(successful_filter) == Try(Exception, False)



# Generated at 2022-06-14 03:45:55.894818
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, '1').filter(lambda x: x == '1') == Try('1', True)
    assert Try.of(lambda x: x, '1').filter(lambda x: x == '2') == Try('1', False)


# Generated at 2022-06-14 03:46:00.185829
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, True).filter(lambda x: False) == Try(1, False)
    assert Try(1, False).filter(lambda x: False) == Try(1, False)


# Generated at 2022-06-14 03:46:07.602792
# Unit test for method filter of class Try
def test_Try_filter():
    # Arrange
    try_success = Try(42, True)
    try_fail = Try(42, False)
    success, fail = True, False
    # Act
    try_map_success = try_success.filter(lambda x: True)
    try_map_fail_1 = try_fail.filter(lambda x: True)
    try_map_fail_2 = try_success.filter(lambda x: False)
    # Assert
    assert try_map_success == Try(42, success)
    assert try_map_fail_1 == Try(42, fail)
    assert try_map_fail_2 == Try(42, fail)

# Generated at 2022-06-14 03:46:16.904056
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    try_with_lambda = Try.of(lambda x: x * 2, 2)
    true_try = try_with_lambda.filter(lambda x: x == 4)
    false_try = try_with_lambda.filter(lambda x: x == 5)
    false_try_on_except = Try(Exception('test'), False).filter(lambda x: x == 5)

    assert true_try == Try(4, True)
    assert false_try == Try(4, False)
    assert false_try_on_except == Try(Exception('test'), False)


# Generated at 2022-06-14 03:46:20.628921
# Unit test for method filter of class Try
def test_Try_filter():
    try_success = Try(1, True)
    try_fail = Try(1, False)

    def _filterer(number):
        return number == 6

    assert try_success.filter(_filterer) == Try(1, False)
    assert try_fail.filter(_filterer) == Try(1, False)


# Generated at 2022-06-14 03:46:23.524055
# Unit test for method filter of class Try
def test_Try_filter():

    assert Try(10, True).filter(lambda x: x == 10) == Try(10, True)
    assert Try(20, True).filter(lambda x: x == 10) == Try(20, False)
    assert Try('', False).filter(lambda x: True) == Try('', False)


# Generated at 2022-06-14 03:46:29.483743
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x <= 0) == Try(1, False)
    assert Try(0, True).filter(lambda x: x <= 0) == Try(0, True)
    assert Try(1, False).filter(lambda x: x <= 0) == Try(1, False)


# Generated at 2022-06-14 03:46:36.865804
# Unit test for method filter of class Try
def test_Try_filter():
    """Unit test for method filter of class Try"""

    # Successfully Try
    try_value = Try('B', True)
    # Successfully value when filterer returns True
    result = try_value.filter(lambda x: x != 'A')
    assert result == Try('B', True)

    # Not successfully Try
    try_value = Try('B', False)
    # Not successfully value when filterer returns True
    result = try_value.filter(lambda x: x != 'A')
    assert result == Try('B', False)


# Generated at 2022-06-14 03:46:47.200719
# Unit test for method filter of class Try
def test_Try_filter():
    my_dictionary = {'hello': 'world'}
    maybe_world = Try.of(lambda: my_dictionary['hello']).filter(lambda word: word == 'world')
    assert maybe_world == Try('world', True)
    assert maybe_world.filter(lambda word: word == 'hello') == Try('world', False)


# Generated at 2022-06-14 03:46:53.105526
# Unit test for method filter of class Try
def test_Try_filter():
    assert(
        Try.of(lambda x: x, 123).filter(lambda x: x == 123)\
            == Try(123, True)
    )
    assert(
        Try.of(lambda x: x, 123).filter(lambda x: x == 124)\
            == Try(123, False)
    )
    assert(
        Try.of(lambda x: x, 123).filter(lambda x: x == 124)\
            == Try.of(lambda x: x, 123)\
                .filter(lambda x: x == 123)
    )

# Generated at 2022-06-14 03:47:03.946123
# Unit test for method filter of class Try
def test_Try_filter():
    # positive scenario
    method_input = 5
    filterer = lambda x: x > method_input
    actual = Try(6, True).filter(filterer)
    expected = Try(6, True)
    assert (expected == actual)

    # negative scenario
    method_input = 5
    filterer = lambda x: x > method_input
    actual = Try(6, False).filter(filterer)
    expected = Try(6, False)
    assert (expected == actual)

    # negative scenario
    actual = Try(5, True).filter(filterer)
    expected = Try(5, False)
    assert (expected == actual)

    # negative scenario
    actual = Try(5, False).filter(filterer)
    expected = Try(5, False)
    assert (expected == actual)




# Generated at 2022-06-14 03:47:13.075370
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    # Has to be successfully
    value = Try(42, True)\
        .filter(lambda x: x > 10)\
        .map(lambda x: x + 10)\
        .get()
    assert value == 52

    # Has not to be successfully, because filter returns False
    value = Try(1, True)\
        .filter(lambda x: x > 10)\
        .get_or_else(0)
    assert value == 0

    # Has not to be successfully, because filter raises an exception
    value = Try(1, True)\
        .filter(lambda x: x / 0)\
        .get_or_else(0)
    assert value == 0


# Generated at 2022-06-14 03:47:22.716552
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Testing method filter of class Try.
    """
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try("a", True).filter(lambda x: len(x) == 1) == Try("a", True)
    assert Try("a", True).filter(lambda x: len(x) == 2) == Try("a", False)
    assert Try(ValueError("error"), False).filter(lambda x: True) == Try(ValueError("error"), False)
    assert Try("C", True).map(lambda x: x.lower()).filter(lambda x: x == "c") == Try("c", True)



# Generated at 2022-06-14 03:47:31.622808
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
    Unit test for method filter of class Try.
    """
    def filter_function(value):
        if value > 10:
            return True
        return False

    try_ = Try(12, True)
    not_try = Try(12, False)
    failed_try = Try('Error', False)

    assert try_.filter(filter_function) == Try(12, True)
    assert not_try.filter(filter_function) == Try(12, False)
    assert failed_try.filter(filter_function) == Try('Error', False)

# Generated at 2022-06-14 03:47:37.532388
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda x: x > 42) == Try(42, False)
    assert Try(None, False).filter(lambda _: True) == Try(None, False)
    assert Try(42, True).filter(lambda x: x < 42) == Try(42, False)


# Generated at 2022-06-14 03:47:42.774853
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Return True when method filter of class Try returns correct result.
    """
    f = lambda x: x % 2 == 0
    assert Try(2, True).filter(f).get() == 2
    assert Try(1, True).filter(f).is_success is False
    assert Try(1, False).filter(f).get() == 1


# Generated at 2022-06-14 03:47:50.449215
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x == 10) == Try(10, True)
    assert Try(10, False).filter(lambda x: x == 10) == Try(10, False)
    assert Try(10, True).filter(lambda x: x == 1) == Try(10, False)
    assert Try(10, False).filter(lambda x: x == 1) == Try(10, False)
    assert Try(None, False).filter(lambda x: x is None) == Try(None, False)


# Generated at 2022-06-14 03:47:53.870196
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """
    def filter_function(value):
        return value['age'] > 40

    value = {
        'name': 'John',
        'age': 42
    }

    try_monad = Try(value, True)

    assert try_monad.filter(filter_function) == Try.of(lambda: value)

# Generated at 2022-06-14 03:48:10.112840
# Unit test for method filter of class Try
def test_Try_filter():
    from pytest import raises

    monad = Try.of(lambda a: a + 1, 1)
    assert monad.filter(lambda a: True) == Try(2, True)

    monad = Try.of(lambda a: a + 1, 1)
    assert monad.filter(lambda a: False) == Try(2, False)

    with raises(Exception):
        Try.of(lambda a, b: a + b, 1)

# Generated at 2022-06-14 03:48:14.083777
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 0
    assert Try(5, True).filter(filterer) == Try(5, True)
    assert Try(-5, True).filter(filterer) == Try(-5, False)
    assert Try(5, False).filter(filterer) == Try(5, False)


# Generated at 2022-06-14 03:48:23.914024
# Unit test for method filter of class Try
def test_Try_filter():
    """Test filter method of Try"""
    def filterer(value):
        return value is not None
    assert Try(None, True).filter(filterer) == Try(None, False)
    assert Try(None, False).filter(filterer) == Try(None, False)
    assert Try('', True).filter(filterer) == Try('', True)
    assert Try(0, True).filter(filterer) == Try(0, True)
    assert Try('', False).filter(filterer) == Try('', False)
    assert Try(0, False).filter(filterer) == Try(0, False)



# Generated at 2022-06-14 03:48:32.694713
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 100).filter(lambda x: x % 10 == 0) == Try(100, True)
    assert Try.of(lambda: 100).filter(lambda x: x % 10 == 1) == Try(100, False)
    assert Try.of(lambda: 100).filter(lambda x: x % 10 == 1).value == 100

    assert Try.of(lambda: 100, 1).filter(lambda x: x % 10 == 0) == Try(100, True)
    assert Try.of(lambda: 100, 1).filter(lambda x: x % 10 == 1) == Try(100, False)
    assert Try.of(lambda: 100, 1).filter(lambda x: x % 10 == 1).value == 100


# Generated at 2022-06-14 03:48:39.780721
# Unit test for method filter of class Try
def test_Try_filter():
    def get_exception(reason):
        return Exception('[{}] exception'.format(reason))

    def check_positive(value):
        if value > 0:
            return True
        raise get_exception('check positive')

    def check_negative(value):
        if value < 0:
            return True
        raise get_exception('check negative')

    values = [
        (1, True),
        (0, False),
        (-1, False)
    ]

    for value, expected in values:
        try_value = lambda: value
        actual = Try.of(try_value).filter(check_positive).is_success
        assert actual == expected,\
            "for value '{}' expected '{}' but actual '{}'".format(value, expected, actual)


# Generated at 2022-06-14 03:48:45.744962
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 10).filter(lambda x: x > 2) == Try(10, True)
    assert Try.of(lambda: 1).filter(lambda x: x > 2) == Try(1, False)

    assert Try.of(lambda: 10).filter(lambda x: x < 2) == Try(10, False)
    assert Try.of(lambda: 1).filter(lambda x: x > 0) == Try(1, True)



# Generated at 2022-06-14 03:48:54.250316
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    # Case 1: Try is successfully and filterer returns False
    result = Try.of(lambda: 1, 1).filter(lambda value: False)
    assert result == Try(1, False)

    # Case 2: Try is successful and filterer returns True
    result = Try.of(lambda: 1, 1).filter(lambda value: True)
    assert result == Try(1, True)

    # Case 3: Try is not successful
    result = Try(Exception, False).filter(lambda value: True)
    assert result == Try(Exception, False)

# Generated at 2022-06-14 03:49:05.116012
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1).filter(lambda a: a > 0) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda a: a < 0) == Try(1, False)
    assert Try.of(lambda: -1).filter(lambda a: a < 0) == Try(-1, True)
    assert Try.of(lambda: -1).filter(lambda a: a > 0) == Try(-1, False)
    assert Try.of(lambda: 'a').filter(lambda a: a == 'a') == Try('a', True)
    assert Try.of(lambda: 'a').filter(lambda a: a != 'a') == Try('a', False)
    assert Try.of(lambda: 0).filter(lambda a: a != 0) == Try(0, False)

# Generated at 2022-06-14 03:49:11.070550
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """
    result = Try.of(int, '1')\
        .filter(lambda x: x > 0)
    assert result == Try(1, True)


# Generated at 2022-06-14 03:49:18.073415
# Unit test for method filter of class Try
def test_Try_filter():
    try_ok = Try(10, True)
    try_nok = Try(10, False)

    assert try_ok.filter(lambda x: x == 10).get() == 10
    assert try_ok.filter(lambda x: x == 0).is_success == False
    assert try_nok.filter(lambda x: x == 10).is_success == False

    def filterer(x):
        raise Exception()

    assert try_ok.filter(filterer).is_success == False


# Generated at 2022-06-14 03:49:40.770005
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def f(x):
        return x == 2

    assert Try(2, True).filter(f) == Try(2, True)
    assert Try(1, True).filter(f) == Try(1, False)


# Generated at 2022-06-14 03:49:46.177796
# Unit test for method filter of class Try
def test_Try_filter():
    try_value = Try.of(int, 'abc')
    try_value = try_value.filter(lambda x: x > 100)
    assert try_value == Try(ValueError(), False)

    try_value = Try.of(int, '50')
    try_value = try_value.filter(lambda x: x > 100)
    assert try_value == Try(ValueError(), False)

    try_value = Try.of(int, '50')
    try_value = try_value.filter(lambda x: x < 100)
    assert try_value == Try(50, True)


# Generated at 2022-06-14 03:49:53.090266
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Simple unit test for method filter of class Try.
    """
    def test_filter(test_value):
        return test_value == 'test_value'

    try_value = Try('test_value', True)
    assert try_value.filter(test_filter) == Try('test_value', True)
    try_value = Try('test_value_fail', True)
    assert try_value.filter(test_filter) == Try('test_value_fail', False)
    try_value = Try(Exception, False)
    assert try_value.filter(test_filter) == Try(Exception, False)


# Generated at 2022-06-14 03:49:59.237429
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> f = lambda x: True
    >>> t = Try(2, True)
    >>> t.filter(f)
    Try[value=2, is_success=True]
    >>> t = Try(2, False)
    >>> t.filter(f)
    Try[value=2, is_success=False]
    >>> f = lambda x: False
    >>> t = Try(2, True)
    >>> t.filter(f)
    Try[value=2, is_success=False]
    """
    pass


# Generated at 2022-06-14 03:50:06.287488
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x < 2) == Try(1, True)
    assert Try(5, True).filter(lambda x: x < 2) == Try(5, False)
    assert Try(1, False).filter(lambda x: x < 2) == Try(1, False)



# Generated at 2022-06-14 03:50:07.797704
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of class Try.
    """
    def filter_func(value):
        return value > 3
    assert Try(1, True).filter(filter_func) == Try(1, False)
    assert Try(4, True).filter(filter_func) == Try(4, True)

# Generated at 2022-06-14 03:50:14.600251
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value) -> bool:
        return value > 3

    assert Try(2, True).filter(filterer) == Try(2, False)  # Fail filterer
    assert Try(3, True).filter(filterer) == Try(3, True)  # Successful filterer
    assert Try(4, True).filter(filterer) == Try(4, True)  # Successful filterer



# Generated at 2022-06-14 03:50:23.786358
# Unit test for method filter of class Try
def test_Try_filter():
    def is_even(x):
        return x % 2 == 0

    assert Try(2, True)\
        .filter(is_even)\
        == Try(2, True)

    assert Try(3, True)\
        .filter(is_even)\
        == Try(3, False)

    assert Try(2, True)\
        .filter(lambda x: x > 2)\
        == Try(2, False)

    assert Try(2, False)\
        .filter(is_even)\
        == Try(2, False)


# Generated at 2022-06-14 03:50:30.768412
# Unit test for method filter of class Try
def test_Try_filter():    
    def filterer(value):
        return value > 10

    assert Try(11, True).filter(filterer) == Try(11, True)
    assert Try(9, True).filter(filterer) == Try(9, False)
    assert Try(11, False).filter(filterer) ==  Try(11, False)
    assert Try(Exception, False).filter(filterer) ==  Try(Exception, False)


# Generated at 2022-06-14 03:50:38.764298
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(int, 123).filter(lambda n: n > 100) == Try(123, True)
    assert Try.of(int, 123).filter(lambda n: n < 100) == Try(123, False)
    assert Try.of(lambda: 1 / 0, 123).filter(lambda n: n > 0) == Try(ZeroDivisionError(), False)
    assert Try.of(lambda: 1 / 0, 123).filter(lambda n: 0 > 0) == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:51:03.871108
# Unit test for method filter of class Try
def test_Try_filter():
    try_success = Try(0, True)
    assert try_success.filter(lambda x: True) == Try(0, True)
    assert try_success.filter(lambda x: False) == Try(0, False)

    try_fail = Try(0, False)
    assert try_fail.filter(lambda x: True) == Try(0, False)
    assert try_fail.filter(lambda x: False) == Try(0, False)



# Generated at 2022-06-14 03:51:06.324136
# Unit test for method filter of class Try
def test_Try_filter():
    filter_true = lambda x: True
    filter_false = lambda x: False
    assert Try('success', True).filter(filter_true).is_success == True
    assert Try('success', True).filter(filter_false).is_success == False
    assert Try('success', True).filter(filter_false).get() == 'success'


# Generated at 2022-06-14 03:51:11.314618
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda v: v == 10) == Try(10, True)
    assert Try(10, False).filter(lambda v: v == 10) == Try(10, False)
    assert Try(0, True).filter(lambda v: v == 10) == Try(0, False)

# Generated at 2022-06-14 03:51:14.945817
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(4, True).filter(lambda v: v > 3) == Try(4, True)
    assert Try(4, True).filter(lambda v: v > 5) == Try(4, False)



# Generated at 2022-06-14 03:51:20.390120
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(divmod, 10, 2).filter(
        lambda x: x[1] == 0
    ) == Try(divmod(10, 2), True)

    assert Try.of(divmod, 10, 2).filter(
        lambda x: x[0] == 0
    ) == Try(divmod(10, 2), False)



# Generated at 2022-06-14 03:51:34.223316
# Unit test for method filter of class Try
def test_Try_filter():
    """Unit test for filter method of class Try.
    """
    def filter_1(x):
        return x > 0

    def filter_2(x):
        return x < 0

    def filter_3(x):
        return x == 0

    t1 = Try(0, True)
    t2 = Try(-1, True)
    t3 = Try(1, True)

    assert t1.filter(filter_1) == Try(-1, False)
    assert t1.filter(filter_2) == Try(-1, False)
    assert t1.filter(filter_3) == Try(0, True)

    assert t2.filter(filter_1) == Try(-1, False)
    assert t2.filter(filter_2) == Try(-1, True)
    assert t2.filter(filter_3)

# Generated at 2022-06-14 03:51:38.213155
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x: int) -> bool:
        return x % 2 == 0

    # Test filter in successfully monad
    assert Try(2, True).filter(filterer) == Try(2, True)

    # Test filter in not successfully monad
    assert Try(1, False).filter(filterer) == Try(1, False)

    # Test filter in successfully monad with filterer return False
    assert Try(3, True).filter(filterer) == Try(3, False)

# Generated at 2022-06-14 03:51:45.909873
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test of Try.filter method.

    :returns: True when passed, othercase False
    :rtype: Boolean
    """
    def func(a):
        return a >= 0

    t = Try(1, True)
    f = Try(1, False)

    assert f.filter(func) == Try(1, False)
    assert t.filter(func) == Try(1, True)
    assert f.filter(lambda x: x > 5) == Try(1, False)
    assert f.filter(lambda x: x < 0) == Try(1, False)

# Generated at 2022-06-14 03:51:52.367690
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x < 10) == Try(10, False)
    assert Try(10, True).filter(lambda x: x == 10) == Try(10, True)
    assert Try(10, False).filter(lambda x: x < 10) == Try(10, False)
    assert Try(10, False).filter(lambda x: x > 10) == Try(10, False)


# Generated at 2022-06-14 03:52:00.639233
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(None, True).filter(lambda x: True) == Try(None, True)
    assert Try(None, False).filter(lambda x: True) == Try(None, False)
    assert Try(None, True).filter(lambda x: False) == Try(None, False)
    assert Try(None, False).filter(lambda x: False) == Try(None, False)
    assert Try(2, True).filter(lambda x: x > 1) == Try(2, True)
    assert Try(2, True).filter(lambda x: x < 1) == Try(2, False)
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try(2, True).filter(lambda x: x % 2 == 1) == Try(2, False)


# Unit

# Generated at 2022-06-14 03:52:48.544465
# Unit test for method filter of class Try
def test_Try_filter():
    data = [1, 2, 3, 4, 5]
    data_filtered = list(filter(lambda x: x % 2 == 0, data))
    data2 = [1, 2, 3, 4, 5]
    data2_filtered = list(map(lambda x: Try.of(lambda v: v, x).filter(lambda v: v % 2 == 0).get(), data2))

    assert data_filtered == data2_filtered
    assert data2_filtered == [2, 4]


# Generated at 2022-06-14 03:52:56.233570
# Unit test for method filter of class Try
def test_Try_filter():
    a = Try.of(lambda x: x * 2, 2).filter(lambda x: x > 2)
    assert a == Try(4, True)
    b = Try.of(lambda x: x * 2, 2).filter(lambda x: x < 2)
    assert b == Try(2, False)
    c = Try.of(lambda x: x / 0, 2).filter(lambda x: x > 2)
    assert c == Try(ZeroDivisionError(r'float division by zero'), False)


# Generated at 2022-06-14 03:52:59.642964
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    monadInteger = Try.of(int, '10')
    assert monadInteger.filter(lambda value: value == 10).get() == 10
    assert monadInteger.filter(lambda value: value == 20).get() == '10'

    monadInteger = Try.of(int, 'a')
    assert monadInteger.filter(lambda value: value == 10).get() == 'a'


# Generated at 2022-06-14 03:53:05.933661
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 5
    # When value greater than 5
    assert Try(10, True) == Try.of(lambda: 10).filter(filterer)
    # When value less than 5
    assert Try(3, False) == Try.of(lambda: 3).filter(filterer)
    # When value not successfully
    assert Try(None, False) == Try(None, False).filter(filterer)



# Generated at 2022-06-14 03:53:10.105254
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer_function(a):
        return a % 2 == 0
    v1 = Try(1, True)
    v2 = Try(2, True)
    assert v1.filter(filterer_function) == Try(1, False)
    assert v2.filter(filterer_function) == Try(2, True)


# Generated at 2022-06-14 03:53:16.180599
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of class Try.
    """
    def test_filter(monad_value, filterer, is_filter_expected_result, is_expected_success):
        """
        Function for filterer testing with different monad value, expected correctness of filterer
        and expected success.

        :params monad_value: value in monad
        :params filterer: function to apply with monad value
        :params is_filter_expected_result: expected result of filterer
        :params is_expected_success: expected success of Try
        :type monad_value: A
        :type filterer: Function(A) -> Boolean
        :type is_filter_expected_result: Boolean
        :type is_expected_success: Boolean
        :rtype: Boolean
        """

# Generated at 2022-06-14 03:53:26.304874
# Unit test for method filter of class Try
def test_Try_filter():
    from itertools import starmap

    # Given
    some_try = Try.of(lambda: 1, None)
    some2_try = Try.of(lambda: 2, None)
    some3_try = Try.of(lambda: 3, None)
    none_try = Try.of(lambda: 1 / 0, None)
    none2_try = Try.of(lambda: 1 / 0, None)
    none3_try = Try.of(lambda: 1 / 0, None)

    some_list_try = Try.of(lambda: [1], None)
    some2_list_try = Try.of(lambda: [2], None)
    some3_list_try = Try.of(lambda: [3], None)
    none_list_try = Try.of(lambda: [], None)
    none

# Generated at 2022-06-14 03:53:31.435573
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def check(value):
        return isinstance(value, int)

    assert Try.of(True).filter(check) == Try(True, True)
    assert Try.of('a').filter(check) == Try('a', False)

# Generated at 2022-06-14 03:53:37.677471
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test cases for method filter.
    """
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda x: 1/0, None).filter(lambda x: x is None) == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:53:41.087895
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 0

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(1, False).filter(filterer) == Try(1, False)