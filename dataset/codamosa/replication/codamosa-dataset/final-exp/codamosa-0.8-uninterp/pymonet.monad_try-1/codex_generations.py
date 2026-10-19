

# Generated at 2022-06-14 03:44:37.796910
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(0, True).filter(lambda x: x > 0) == Try(0, False)
    assert Try(-1, True).filter(lambda x: x > 0) == Try(-1, False)
    assert Try(1, False).filter(lambda x: x > 0) == Try(1, False)


# Generated at 2022-06-14 03:44:40.291638
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1).filter(lambda prev: prev % 2 == 0).is_success == False
    assert Try.of(lambda: 2).filter(lambda prev: prev % 2 == 0).is_success == True

# Generated at 2022-06-14 03:44:48.188801
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filterer(value: str):
        return value == 'test'

    try_ = Try.of(lambda: 'test', [])
    assert try_.filter(test_filterer).is_success

    try_ = Try.of(lambda: 'test_1', [])
    assert not try_.filter(test_filterer).is_success


# Generated at 2022-06-14 03:44:53.425439
# Unit test for method filter of class Try
def test_Try_filter():
    """ """
    assert Try(1, True).filter(lambda v: v == 1) == Try(1, True)
    assert Try(1, True).filter(lambda v: v == 2) == Try(1, False)
    assert Try(1, False).filter(lambda v: v == 1) == Try(1, False)

# Generated at 2022-06-14 03:44:59.188679
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    value = 'Try test'
    try_success = Try(value, True)
    try_success_filtered = try_success.filter(lambda val: val == value)
    assert try_success == try_success_filtered
    try_success_filtered_not = try_success.filter(lambda val: val != value)
    assert try_success_filtered_not.is_success == False
    try_success_filtered_not = try_success.filter(lambda val: val != value)



# Generated at 2022-06-14 03:45:08.062645
# Unit test for method filter of class Try
def test_Try_filter():
    try_obj = Try(4, True)
    try_obj_rejected = Try(2, True)
    try_obj_exception = Try(ValueError('woops'), False)
    assert try_obj.filter(lambda x: x < 5) == Try(4, True)
    assert try_obj_rejected.filter(lambda x: x < 5) == Try(2, False)
    assert try_obj_exception.filter(lambda x: x < 5) == try_obj_exception



# Generated at 2022-06-14 03:45:14.296634
# Unit test for method filter of class Try
def test_Try_filter():
    """
    This test for method filter of class Try.
    """
    assert Try.of(lambda: 1,).filter(lambda x: x % 2 == 1) == Try(1, True)
    assert Try.of(lambda: 1,).filter(lambda x: x % 2 == 0) == Try(1, False)


# Generated at 2022-06-14 03:45:20.300138
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value
    try_value = Try(1, True)
    assert try_value.filter(filterer) == Try(1, True)

    try_value = Try(1, False)
    assert try_value.filter(filterer) == Try(1, False)


# Generated at 2022-06-14 03:45:25.758536
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 2) == Try(5, True)
    assert Try(5, True).filter(lambda x: x < 2) == Try(5, False)
    assert Try(5, False).filter(lambda x: x < 2) == Try(5, False)



# Generated at 2022-06-14 03:45:30.221359
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try
    """
    try_instance = Try(4, True)
    assert try_instance.filter(lambda value: value % 2 == 0) == Try(4, True)
    assert try_instance.filter(lambda value: value % 2 == 1) == Try(4, False)


# Generated at 2022-06-14 03:45:44.254013
# Unit test for method filter of class Try
def test_Try_filter():
    try_with_exception = Try.of(lambda: 1 / 0)
    try_without_exception = Try.of(lambda: 1 / 1)

    assert try_with_exception.filter(lambda x: x > 1)\
            == Try(ZeroDivisionError(), False)

    assert try_without_exception.filter(lambda x: x > 1)\
            == Try(ZeroDivisionError(), False)

    assert try_without_exception.filter(lambda x: x > 0)\
            == Try(1, True)

# Generated at 2022-06-14 03:45:50.179452
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x != 1) == Try(1, False)
    assert Try(1, False).filter(lambda _: True) == Try(1, False)
    assert Try(Exception, False).filter(lambda _: True) == Try(Exception, False)



# Generated at 2022-06-14 03:45:58.109580
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def f(_):
        return True
    def g(_):
        return False
    assert Try(1, True).filter(f) == Try(1, True)
    assert Try(1, True).filter(g) == Try(1, False)
    assert Try(1, False).filter(f) == Try(1, False)
    assert Try(1, False).filter(g) == Try(1, False)


# Generated at 2022-06-14 03:46:08.965619
# Unit test for method filter of class Try
def test_Try_filter():
    from datetime import datetime

    # Case when monad has successfully value
    print('-- Case when monad has successfully value')
    def format_date(date_str: str) -> Try[datetime]:
        return Try.of(datetime.strptime, date_str, '%Y-%m-%d')
    def is_valid_date(date: datetime) -> Try[bool]:
        today = datetime.now()
        is_valid = datetime(
            year=today.year,
            month=date.month,
            day=date.day,
        ) == date
        return Try.of(lambda: is_valid)
    def is_valid_date_format(date: datetime) -> Try[bool]:
        return Try.of(lambda: True)


# Generated at 2022-06-14 03:46:16.380689
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test monad Try.filter
    """
    actual_result = Try.of(lambda: 2/0)\
        .filter(lambda: True)

    assert actual_result != Try(2, True)
    assert actual_result.is_success is False

    actual_result = Try.of(lambda: 2/1)\
        .filter(lambda: True)
    assert actual_result == Try(2, True)

    actual_result = Try.of(lambda: 2/1)\
        .filter(lambda x: x == 2)

    assert actual_result == Try(2, True)

    actual_result = Try.of(lambda: 2/1)\
        .filter(lambda x: x == 1)
    assert actual_result != Try(2, True)

# Generated at 2022-06-14 03:46:20.383595
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1).filter(lambda x: True) == Try(1, True)
    assert Try.of(lambda: '').filter(lambda x: True) == Try('', True)
    assert Try.of(lambda: True).filter(lambda x: True) == Try(True, True)
    assert Try.of(lambda: Exception('Exception')).filter(lambda x: True) == Try(
        'Exception', False)
    assert Try.of(lambda: True).filter(lambda x: False) == Try('', False)
    assert Try.of(lambda: 1 / 0).filter(lambda x: False) == Try('', False)


# Generated at 2022-06-14 03:46:23.864289
# Unit test for method filter of class Try
def test_Try_filter():
    assert(Try(None, False).filter(lambda x: True) == Try(None, False))
    assert(Try(None, True).filter(lambda x: False) == Try(None, False))
    assert(
        Try(None, True)
            .filter(lambda x: True)
            .on_success(lambda x: print('---'))
            .on_fail(lambda x: print('---'))
        == Try(None, True))
    assert(
        Try(None, True)
            .filter(lambda x: False)
            .on_success(lambda x: print('---'))
            .on_fail(lambda x: print('---'))
        == Try(None, False))

# Generated at 2022-06-14 03:46:32.384873
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True)\
           .filter(lambda x: x > 0)\
           == Try(42, True)
    assert Try(0, True)\
           .filter(lambda x: x > 0)\
           == Try(0, False)
    assert Try(None, True)\
           .filter(lambda x: x)\
           == Try(None, False)
    assert Try(42, False)\
           .filter(lambda x: x > 0)\
           == Try(42, False)



# Generated at 2022-06-14 03:46:37.295981
# Unit test for method filter of class Try
def test_Try_filter():
    # given
    true_filterer = lambda x: x
    false_filterer = lambda x: False
    false_filterer_with_exception = lambda x: 1 / 0
    # when
    successfully = Try(1, True)
    unsuccessfully = Try(1, False)
    # then
    assert successfully.filter(true_filterer) == successfully
    assert unsuccessfully.filter(true_filterer) == unsuccessfully
    assert successfully.filter(false_filterer) == unsuccessfully
    assert unsuccessfully.filter(false_filterer) == unsuccessfully
    assert unsuccessfully.filter(false_filterer_with_exception) == unsuccessfully


# Generated at 2022-06-14 03:46:51.444654
# Unit test for method filter of class Try
def test_Try_filter():
    """
    To run unit test for this function use:
    python3 -c 'import monad_try; monad_try.test_Try_filter()'
    """
    print('Unit test for method filter of class Try')

    print('Test 1')
    t_value = 1
    t = Try(t_value, True)
    f = lambda x: x == t_value
    filtered = t.filter(f)
    assert filtered == t
    print('Test 1 passed\n')

    print('Test 2')
    t_value = 1
    t = Try(t_value, True)
    f = lambda x: x != t_value
    filtered = t.filter(f)
    assert filtered.value == t_value
    assert not filtered.is_success
    print('Test 2 passed\n')


# Generated at 2022-06-14 03:47:01.761858
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value != 'b'

    for key in ['a', 'b']:
        assert Try(key, True).filter(filterer) == Try(key, True if key == 'a' else False)


# Generated at 2022-06-14 03:47:05.338883
# Unit test for method filter of class Try
def test_Try_filter():
    # Successfully
    success_Try = Try(10, True)
    assert success_Try.filter(lambda x: x == 10).is_success
    # Not successful
    not_success_Try = Try(10, False)
    assert not not_success_Try.filter(lambda x: x == 10).is_success



# Generated at 2022-06-14 03:47:07.608122
# Unit test for method filter of class Try
def test_Try_filter():
    assert(Try.of(lambda: 1)
           .filter(lambda x: x == 1) ==
           Try(1, True))



# Generated at 2022-06-14 03:47:12.884371
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x > 5) == Try(10, True)
    assert Try(10, True).filter(lambda x: x > 15) == Try(10, False)
    assert Try(None, False).filter(lambda x: x > 5) == Try(None, False)
    assert Try(10, False).filter(lambda x: x > 5) == Try(10, False)


# Generated at 2022-06-14 03:47:16.935345
# Unit test for method filter of class Try
def test_Try_filter():
    def is_even(x):
        return x % 2 == 0

    assert Try.of(lambda: 1).filter(is_even) == Try(1, False)
    assert Try.of(lambda: 2).filter(is_even) == Try(2, True)


# Generated at 2022-06-14 03:47:27.880764
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(None, True).filter(lambda x: x is None).is_success
    assert not Try(None, True).filter(lambda x: x is not None).is_success
    assert Try(None, False).filter(lambda x: x is None) == Try(None, False)
    assert Try(None, False).filter(lambda x: x is not None) == Try(None, False)

    assert Try(1, True).filter(lambda x: x > 0).is_success
    assert not Try(1, True).filter(lambda x: x <= 0).is_success
    assert Try(1, False).filter(lambda x: x > 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x <= 0) == Try(1, False)


# Generated at 2022-06-14 03:47:34.619425
# Unit test for method filter of class Try
def test_Try_filter():  # pytest test_TryFilter.py -v
    """ Test for method filter of class Try """
    try_monad = Try(42, True)
    assert try_monad.filter(lambda value: value > 0).get() == 42

    try_monad = Try(42, True)
    assert try_monad.filter(lambda value: value < 0).get() == 42
    assert not try_monad.filter(lambda value: value < 0).is_success

    try_monad = Try(42, False)
    assert try_monad.filter(lambda value: value > 0).get() == 42
    assert not try_monad.filter(lambda value: value > 0).is_success

# Generated at 2022-06-14 03:47:43.351026
# Unit test for method filter of class Try
def test_Try_filter():
    # when filterer returns True
    def filterer_true(value):
        return True

    assert Try(1, True).filter(filterer_true) == Try(1, True)
    assert Try(1, False).filter(filterer_true) == Try(1, False)

    # when filterer returns False
    def filterer_false(value):
        return False

    assert Try(1, True).filter(filterer_false) == Try(1, False)
    assert Try(1, False).filter(filterer_false) == Try(1, False)



# Generated at 2022-06-14 03:47:49.787924
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda x: x % 2 == 0) == Try(42, True)
    assert Try(21, True).filter(lambda x: x % 2 == 0) == Try(21, False)
    assert Try(21, False).filter(lambda x: x % 2 == 0) == Try(21, False)


# Generated at 2022-06-14 03:47:56.564518
# Unit test for method filter of class Try
def test_Try_filter():
    # Test for successful Try and return copy of monad
    assert Try(0, True).filter(lambda i: i > 0) == Try(0, True)
    assert Try(1, True).filter(lambda i: i > 0) == Try(1, True)

    # Test for successful Try and return new not successful Try
    assert Try(0, True).filter(lambda i: i < 0) == Try(0, False)

    # Test for not successful Try and return copy of monad
    assert Try(0, False).filter(lambda i: i < 0) == Try(0, False)

    # Test for successful Try and return new not successful Try with passed exception
    assert Try.of(lambda i: i / 0, 0).filter(lambda i: i < 0) \
        == Try(ZeroDivisionError('division by zero'), False)

# Generated at 2022-06-14 03:48:19.862868
# Unit test for method filter of class Try
def test_Try_filter():
    assert_equal(
        Try(2, True).filter(lambda x: x % 2 == 0),
        Try(2, True)
    )
    assert_equal(
        Try(3, True).filter(lambda x: x % 2 == 0),
        Try(3, False)
    )
    assert_equal(
        Try(2, False).filter(lambda x: x % 2 == 0),
        Try(2, False)
    )
    assert_equal(
        Try(3, False).filter(lambda x: x % 2 == 0),
        Try(3, False)
    )


# Generated at 2022-06-14 03:48:31.004970
# Unit test for method filter of class Try
def test_Try_filter():

    class FilterTestException(Exception):
        pass

    assert isinstance(Try.of(lambda x: x, 1).filter(lambda x: x == 1), Try)
    assert isinstance(Try.of(lambda x: x, 1).filter(lambda x: False), Try)
    assert isinstance(Try.of(lambda x: 1, 1).filter(lambda x: x == 1), Try)
    assert isinstance(Try.of(lambda x: 1, 1).filter(lambda x: False), Try)
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: False) == Try(1, False)

# Generated at 2022-06-14 03:48:38.214105
# Unit test for method filter of class Try
def test_Try_filter():
    def an_exception(value):
        raise Exception(value)

    def is_greater_than(value):
        return value > 4

    assert Try.of(lambda: 5).filter(lambda value: value > 4) == Try(5, True)
    assert Try.of(an_exception, 10).filter(is_greater_than) == Try(10, False)
    assert Try.of(an_exception, 10).filter(lambda value: True) == Try(10, False)
    assert Try.of(an_exception, 4).filter(lambda value: value > 3) == Try(4, False)

test_Try_filter()

# Generated at 2022-06-14 03:48:44.761844
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1.0, True).filter(lambda x: isinstance(x, float)) == Try(1.0, True)
    assert Try(1.0, True).filter(lambda x: isinstance(x, int)) == Try(1.0, False)
    assert Try(1.0, False).filter(lambda x: isinstance(x, float)) == Try(1.0, False)

# Generated at 2022-06-14 03:48:49.348416
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1).is_success
    assert not Try(1, True).filter(lambda x: x == 2).is_success
    assert not Try(1, False).filter(lambda x: x == 1).is_success

# Generated at 2022-06-14 03:48:58.154639
# Unit test for method filter of class Try
def test_Try_filter():
    try:
        assert Try(10, True).filter(lambda x: x > 10) == Try(10, False)
        assert Try(10, True).filter(lambda x: x < 10) == Try(10, False)
        assert Try(10, True).filter(lambda x: x == 10) == Try(10, True)
        assert Try(None, False).filter(lambda x: x > 10) == Try(None, False)
        assert Try(10, False).filter(lambda x: x > 10) == Try(10, False)
    except Exception as e:  # pragma: no cover
        print('Exception in method test_filter of class Try', e)
        assert False


# Generated at 2022-06-14 03:49:08.338825
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Check Try.filter method.
    """
    def get_fizz_or_buzz_or_fizzbuzz(number):
        if number % 15 == 0:
            return Try('FizzBuzz', True)
        elif number % 3 == 0:
            return Try('Fizz', True)
        elif number % 5 == 0:
            return Try('Buzz', True)
        else:
            return Try('', False)

    result = get_fizz_or_buzz_or_fizzbuzz(10).filter(lambda x: x == '')
    assert result == Try('', False)
    assert get_fizz_or_buzz_or_fizzbuzz(15).filter(lambda x: x == 'FizzBuzz') == Try('FizzBuzz', True)
    assert get_fizz_

# Generated at 2022-06-14 03:49:19.794441
# Unit test for method filter of class Try
def test_Try_filter():
    # GIVEN
    def filterer(value):
        return value > 4

    value = 5
    successfully_try = Try(value, True)

    # WHEN
    filtered_try = successfully_try.filter(filterer)

    # THEN
    assert filtered_try
    assert filtered_try.is_success
    assert filtered_try.value == value

    # GIVEN
    value = 5
    unsuccessfully_try = Try(value, False)

    # WHEN
    filtered_try = unsuccessfully_try.filter(filterer)

    # THEN
    assert filtered_try
    assert not filtered_try.is_success
    assert filtered_try.value == value

    # GIVEN
    value = 3
    successfully_try = Try(value, True)

    # WHEN
    filtered_try = successfully_try.filter

# Generated at 2022-06-14 03:49:28.596123
# Unit test for method filter of class Try
def test_Try_filter():
    # GIVEN
    try_with_number = 7
    try_mapper = lambda x: x * 2
    try_filterer = lambda x: x == 14

    # WHEN
    try_instance = Try.of(int, try_with_number)
    try_instance_mapped = try_instance.map(try_mapper)
    try_instance_filtered = try_instance_mapped.filter(try_filterer)

    # THEN
    assert try_instance_filtered == Try(14, True)

    # GIVEN
    try_with_letter = 'a'
    try_filterer = lambda x: x == 'ab'

    # WHEN
    try_instance = Try.of(int, try_with_letter)

# Generated at 2022-06-14 03:49:35.839070
# Unit test for method filter of class Try
def test_Try_filter():
    try:
        even = lambda x: x % 2 == 0

        assert Try(4, True).filter(even) == Try(4, True)
        assert Try(4, True).filter(even).is_success
        assert Try(4, True).filter(even).get() == 4

        assert Try(3, True).filter(even).is_success == False
        assert Try(3, True).filter(even).get() == 3
    except AssertionError:
        return False
    return True



# Generated at 2022-06-14 03:50:13.884740
# Unit test for method filter of class Try
def test_Try_filter():
    value = 'value'
    failure = 'failure'
    t = Try.of(lambda: value)
    assert t.filter(lambda x: True) == Try(value, True)
    assert t.filter(lambda x: False) == Try(value, False)
    f = Try.of(lambda: failure)
    _t = f.filter(lambda x: True)
    assert _t == Try(failure, False)
    assert _t == Try(failure, False)
    _f = f.filter(lambda x: False)
    assert _f == Try(failure, False)
    assert _f == Try(failure, False)



# Generated at 2022-06-14 03:50:20.852036
# Unit test for method filter of class Try
def test_Try_filter():
    value = 'some string'

    def filterer(val):
        return val == value

    assert Try(value, True).filter(filterer) == Try(value, True)
    assert Try(value, False).filter(filterer) == Try(value, False)
    assert Try('other string', True).filter(filterer) == Try('other string', False)


# Generated at 2022-06-14 03:50:30.000413
# Unit test for method filter of class Try
def test_Try_filter():
    def test_1():
        assert Try.of(lambda x: x + 1, 1).filter(lambda x: x == 2) == Try(2, True)
    def test_2():
        assert Try.of(lambda x: x + 1, 1).filter(lambda x: x == 3) == Try(1, False)
    def test_3():
        assert Try.of(lambda x: 1 / 0, 1).filter(lambda x: x == 3) == Try(1, False)
    test_1()
    test_2()
    test_3()

# Generated at 2022-06-14 03:50:39.849510
# Unit test for method filter of class Try
def test_Try_filter():
    """
    :returns: True when success
    :rtype: Bool
    """
    def filterer(value):
        return False if value <= 0 else True

    assert Try(2, True).filter(filterer) == Try(2, True)
    assert Try(2, True).filter(filterer).get() == 2

    assert Try(-2, True).filter(filterer) == Try(-2, False)
    assert Try(-2, False).filter(filterer).get() == -2

    assert Try(-2, False).filter(filterer) == Try(-2, False)



# Generated at 2022-06-14 03:50:47.364694
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test Try filter method
    """
    def filter_fn(x):
        return x > 3

    # successfully
    try_1 = Try.of(lambda x: x, 4)
    result = try_1.filter(filter_fn)
    assert result == Try(4, True)

    # not successfully
    try_2 = Try.of(lambda x: x, 3)
    result = try_2.filter(filter_fn)
    assert result == Try(3, False)



# Generated at 2022-06-14 03:50:58.843916
# Unit test for method filter of class Try
def test_Try_filter():
    from Tests.utils import test_function

    test_function(
        'Test Try filter method',
        (
            (Try(2, True).filter(lambda x: x > 1), Try(2, True)),
            (Try(2, True).filter(lambda x: x == 1), Try(2, False)),
            (Try(2, False).filter(lambda x: x > 1), Try(2, False)),
            (Try('2', True).filter(lambda x: x > '1'), Try('2', True)),
            (Try('2', True).filter(lambda x: x == '1'), Try('2', False)),
            (Try('2', False).filter(lambda x: x > '1'), Try('2', False))
        )
    )


# Generated at 2022-06-14 03:51:06.982954
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(n: int) -> bool:
        return n > 5

    # Create successfully Try with value 3.
    t = Try.of(lambda x: x, 3)
    # result is not successfully Try with previous value 3
    result = t.filter(filterer)
    assert result.is_success == False
    assert result.value == 3

    # Create successfully Try with value 7.
    t = Try.of(lambda x: x, 7)
    # result is successfully Try with previous value 7
    result = t.filter(filterer)
    assert result.is_success == True
    assert result.value == 7

# Generated at 2022-06-14 03:51:14.802154
# Unit test for method filter of class Try
def test_Try_filter():
    try_div_exception = Try.of(lambda: 1 / 0)
    try_div_exception_not_success = try_div_exception.filter(lambda v: v > 0)

    try_div_success = Try.of(lambda: 1 / 1)
    try_div_success = try_div_success.filter(lambda v: v > 0)

    assert try_div_exception_not_success == Try(ZeroDivisionError(), False)
    assert try_div_success == Try(1, True)


# Generated at 2022-06-14 03:51:19.839329
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x > 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)



# Generated at 2022-06-14 03:51:28.864783
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(val):
        return val == '1'
    # method will return copy of try
    assert Try(1, True).filter(filterer) == Try(1, True)
    # method will return not successfully try
    assert Try(1, True).filter(filterer) != Try(1, False)
    # method will return not successfully try with previous value
    assert Try(1, True).filter(filterer).get() == 1


# Generated at 2022-06-14 03:52:35.560314
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(a):
        return a % 2 == 0
    assert Try(2, True).filter(filterer) == Try(2, True)
    assert Try(1, True).filter(filterer) == Try(1, False)
    assert Try(2, False).filter(filterer) == Try(2, False)
    assert Try(3, False).filter(filterer) == Try(3, False)
    assert Try(Exception('exception'), False).filter(filterer) == Try(Exception('exception'), False)
    assert Try.of(lambda: 1 + 2, ()).filter(filterer) == Try(3, False)
    assert Try.of(lambda: 1 + 3, ()).filter(filterer) == Try(4, True)


# Generated at 2022-06-14 03:52:44.238499
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 5, 1, 2, 3).filter(lambda x: x == 5)\
        == Try(5, True)
    assert Try.of(lambda: 5, 1, 2, 3).filter(lambda x: x == 10)\
        == Try(5, False)
    assert Try.of(lambda: 5 / 0, 1, 2, 3).filter(lambda x: x == 5)\
        == Try(5, False)



# Generated at 2022-06-14 03:52:48.043884
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Function that unit test method filter of class Try.
    """
    def filterer(value):
        return value.startswith('t')

    assert Try(5, True).filter(filterer) == Try(5, False)
    assert Try('test', True).filter(filterer) == Try('test', True)



# Generated at 2022-06-14 03:52:54.275396
# Unit test for method filter of class Try
def test_Try_filter(): # pragma: no cover
    print_message = lambda x: print(x)

    result = Try.of(lambda: 1/0) \
        .filter(lambda x: x > 0) \
        .on_success(print_message)

    if result.is_success and result.get() == 0:
        print('Test success!')
    else:
        print('Test fail!')

# Generated at 2022-06-14 03:52:59.199606
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(1, True).filter(lambda n: n == 1) == Try(1, True)
    assert Try(1, True).filter(lambda n: n == 2) == Try(1, False)
    assert Try(1, False).filter(lambda n: n == 1) == Try(1, False)

# Generated at 2022-06-14 03:53:07.542424
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, 5).bind(lambda x: Try(x + 5, True)).filter(lambda x: x > 10)\
        == Try(10, False)
    assert Try.of(lambda x: x, 5).bind(lambda x: Try(x + 5, True)).filter(lambda x: x <= 10)\
        == Try(10, True)
    assert Try.of(lambda x: x, 5).bind(lambda x: Try.of(lambda x: x / 0, x)).bind(lambda x: Try(x + 5, True))\
        .filter(lambda x: x > 10) == Try(ZeroDivisionError('division by zero'), False)


# Generated at 2022-06-14 03:53:10.958859
# Unit test for method filter of class Try
def test_Try_filter():
    def f(v):
        return v == 1
    assert Try(1, True).filter(f) == Try(1, True)
    assert Try(2, True).filter(f) == Try(2, False)
    assert Try(2, False).filter(f) == Try(2, False)

# Generated at 2022-06-14 03:53:16.741664
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of class Try.
    """
    assert Try(5, True).filter(lambda a: a % 2 == 0) == Try(5, False)
    assert Try(6, True).filter(lambda a: a % 2 == 0) == Try(6, True)



# Generated at 2022-06-14 03:53:22.241105
# Unit test for method filter of class Try
def test_Try_filter():
    # When filterer return True
    assert Try.of(lambda x: x, 10).filter(lambda x: True) == Try(10, True)
    # When filterer return False
    assert Try.of(lambda x: x, 10).filter(lambda x: False) == Try(10, False)



# Generated at 2022-06-14 03:53:26.205887
# Unit test for method filter of class Try
def test_Try_filter():
    def filter_even(value):
        return value % 2 == 0

    assert Try(1, True).filter(filter_even) == Try(1, False)
    assert Try(2, True).filter(filter_even) == Try(2, True)

