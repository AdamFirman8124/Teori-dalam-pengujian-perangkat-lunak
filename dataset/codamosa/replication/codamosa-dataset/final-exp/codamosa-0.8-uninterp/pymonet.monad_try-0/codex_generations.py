

# Generated at 2022-06-14 03:44:32.029398
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
    Test for filter method of class Try.
    """
    assert Try.of(lambda: x, x=1).filter(lambda x: x == 2)\
           == Try(1, True)
    assert Try.of(lambda: x, x=1).filter(lambda x: x == 1)\
           == Try(1, True)
    assert Try.of(lambda: 1/0).filter(lambda x: x == 1)\
           == Try(ZeroDivisionError('division by zero'), False)

# Generated at 2022-06-14 03:44:41.741406
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    @dataclass
    class Message:
        text: str
        status: int

    # When
    message = Message('text', 0)
    mapper = lambda message: message.text + ' ' + str(message.status)
    try_message = Try(message, True)
    success_filter = try_message\
        .map(mapper)\
        .filter(lambda message: message == 'text 0')

    fail_filter = try_message\
        .map(mapper)\
        .filter(lambda message: message == 'text 100')

    # Then
    assert success_filter == Try('text 0', True)
    assert fail_filter == Try('text 0', False)

# Generated at 2022-06-14 03:44:47.202126
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x == 5) == Try(5, True)
    assert Try(5, True).filter(lambda x: x == 4) == Try(5, False)
    assert Try(5, False).filter(lambda x: x == 0) == Try(5, False)

# Generated at 2022-06-14 03:44:54.450688
# Unit test for method filter of class Try
def test_Try_filter():
    def positive_check(x) -> bool:
        return x > 0

    actual = Try.of(lambda: int('123'))\

    # check successfully
    expected = Try(123, True)
    assert actual.filter(positive_check) == expected

    # check not successfully
    actual = Try.of(lambda: int('-123'))
    expected = Try(-123, False)
    assert actual.filter(positive_check) == expected


# Generated at 2022-06-14 03:44:59.149407
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 4) == Try(5, True)
    assert Try(5, True).filter(lambda x: x < 4) == Try(5, False)
    assert Try("Some error", False).filter(lambda x: True) == Try("Some error", False)
    assert Try("Some error", False).filter(lambda x: False) == Try("Some error", False)



# Generated at 2022-06-14 03:45:10.529268
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover

    def some_function(value: int) -> Try[int]:
        return Try.of(int, value)

    res1 = some_function(None).filter(lambda x: x is not None)
    res2 = some_function('1').filter(lambda x: x is not None)
    res3 = some_function('1').filter(lambda x: int(x) == 1)
    res4 = some_function('2').filter(lambda x: int(x) == 1)

    assert res1.is_success == False
    assert res2.is_success == False
    assert res3.is_success == True
    assert res4.is_success == False


# Generated at 2022-06-14 03:45:15.008462
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try('value', True).filter(lambda v: 'value2' != v).get() == 'value'
    assert Try(None, False).filter(lambda v: 'value2' != v).get() == None



# Generated at 2022-06-14 03:45:23.592914
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value > 1

    # when is successful and filterer returns True
    assert Try(2, True).filter(filterer) == Try(2, True)

    # when is successful but filterer returns False
    assert Try(0, True).filter(filterer) == Try(0, False)

    # when is not successfully
    assert Try(0, False).filter(filterer) == Try(0, False)

# Generated at 2022-06-14 03:45:33.364516
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda: []).filter(lambda x: True) == Try([], True)
    assert Try.of(lambda: []).filter(lambda x: False) == Try([], False)
    assert Try.of(lambda x: x, []).filter(lambda x: True) == Try([], True)

# Generated at 2022-06-14 03:45:39.825665
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda v: v > 1) == Try(2, True)
    assert Try(1, True).filter(lambda v: v > 1) == Try(1, False)
    assert Try(2, False).filter(lambda v: v > 1) == Try(2, False)


# Generated at 2022-06-14 03:45:51.941681
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of Try class.
    """
    try_one = Try.of(lambda: 1, ())
    try_two = Try.of(lambda: 1, ())

    # Test for successfully and filterer returns True
    assert try_one.filter(lambda x: x == 1) == try_two
    # Test for successfully and filterer returns False
    assert try_one.filter(lambda x: x == 2) == Try(1, False)
    # Test for not successfully
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)



# Generated at 2022-06-14 03:45:58.400173
# Unit test for method filter of class Try
def test_Try_filter(): # pragma: no cover
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x > 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x < 0) == Try(1, False)


# Generated at 2022-06-14 03:46:01.660643
# Unit test for method filter of class Try
def test_Try_filter():

    def filterer(element):
        if element != '2':
            return True

    try_1 = Try(1, True)
    try_2 = Try(2, True)
    try_3 = Try(3, True)

    assert try_1.map(lambda x: x * 2).filter(filterer).get() == 2
    assert try_2.map(lambda x: x * 2).filter(filterer).get_or_else(3) == 3
    assert try_3.map(lambda x: x * 2).filter(filterer).get() == 6



# Generated at 2022-06-14 03:46:04.712867
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1 + 2, ()).filter(lambda x: x != 1) == Try(3, True)
    assert Try.of(lambda: 1 + 2, ()).filter(lambda x: x == 1) == Try(3, False)

# Generated at 2022-06-14 03:46:09.271847
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(num): return num % 2 == 0
    assert(Try(2, True).filter(filterer).get() == 2)
    assert(Try(1, True).filter(filterer).is_success == False)
    assert(Try(1, True).filter(filterer).get() == 1)


# Generated at 2022-06-14 03:46:19.260769
# Unit test for method filter of class Try
def test_Try_filter():
    with pytest.raises(Exception) as ex:
        Try.of(lambda: 1/0).filter(lambda x: True)
    assert ex is not None
    assert Try.of(lambda: 1/0).filter(lambda x: True).is_success is False
    assert Try.of(lambda: 1/0).filter(lambda x: True).value is not None
    assert Try.of(lambda: 1/0).filter(lambda x: False).is_success is False
    assert Try.of(lambda: 1/0).filter(lambda x: False).value == DivisionByZeroError()
    assert Try.of(lambda: 1).filter(lambda x: True).is_success is True
    assert Try.of(lambda: 1).filter(lambda x: True).value == 1

# Generated at 2022-06-14 03:46:27.301802
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of Try class.
    """
    # Successful with True filter
    assert Try(4, True).filter(lambda x: x > 2) == Try(4, True)
    # Successful with False filter
    assert Try(4, True).filter(lambda x: x > 5) == Try(4, False)
    # Not successful
    assert Try(4, False).filter(lambda x: x == 4) == Try(4, False)



# Generated at 2022-06-14 03:46:32.940097
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> assert Try.of(lambda: 1, ()).filter(lambda x: x == True) == Try(1, True)
    >>> assert Try.of(lambda: 1/0, ()).filter(lambda x: x == True) == Try(ZeroDivisionError(), False)
    >>> assert Try.of(lambda: 1, ()).filter(lambda x: x == False) == Try(1, False)
    """



# Generated at 2022-06-14 03:46:42.146886
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try.
    Result must be Try with monad value when filter returns True.
    Othercase result must be not successfully Try with monad value.
    """

    # Define function that not raises exception
    def fn() -> int:
        return 1

    # Return True when value is equals 1
    filter_1 = lambda x: x == 1

    # Return True when value is equals 1
    filter_2 = lambda x: x == 2

    # Run filter for successfully Try with value 1
    assert Try.of(fn).filter(filter_1) == Try(1, True)

    # Run filter for successfully Try with value 1
    assert Try.of(fn).filter(filter_2) == Try(1, False)

# Generated at 2022-06-14 03:46:45.191722
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: True) == Try(1, True), "Wrong filter method"



# Generated at 2022-06-14 03:46:55.780672
# Unit test for method filter of class Try
def test_Try_filter():
    assert (Try.of(lambda: 'value', ()).filter(lambda value: isinstance(value, str))) == Try('value', True)
    assert (Try.of(lambda: 1, ()).filter(lambda value: isinstance(value, str))) == Try(1, False)

    try:
        assert (Try.of(lambda: raise_exception, ()).filter(lambda value: isinstance(value, str))) == Try(1, False)
    except:
        pass


# Generated at 2022-06-14 03:46:59.672232
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 2, None).filter(lambda i: i % 2 == 0) == Try(2, True)
    assert Try.of(lambda: 2, None).filter(lambda i: i % 3 == 0) == Try(2, False)


# Generated at 2022-06-14 03:47:08.644758
# Unit test for method filter of class Try
def test_Try_filter():

    def is_positive(a):
        return a > 0

    def is_odd(a):
        return a % 2

    assert Try.of(int, '10').filter(is_positive) == Try(10, True)
    assert Try.of(int, '-10').filter(is_positive) == Try(-10, False)
    assert Try.of(int, '10').filter(is_odd) == Try(10, True)
    assert Try.of(int, '10').filter(is_odd) == Try(10, True)
    assert Try.of(int, '-11').filter(is_odd) == Try(-11, False)


# Generated at 2022-06-14 03:47:20.144558
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for filter operation on Try monad.
    """
    assert Try.of(lambda x: x, 2).filter(lambda x: x % 2 == 0).is_success
    assert not Try.of(lambda x: x, 2).filter(lambda x: x % 3 == 0).is_success
    assert not Try.of(lambda x: 1 / 0, 2).is_success
    assert Try.of(lambda x: 1 / 3, 2).filter(lambda x: x % 2 == 0).is_success
    assert not Try.of(lambda x: 1 / 3, 2).filter(lambda x: x % 4 > 0).is_success


# Generated at 2022-06-14 03:47:26.544784
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x > 1) == Try(2, True)
    assert Try(2, True).filter(lambda x: x < 1) == Try(2, False)
    assert Try(Exception('error'), False).filter(lambda x: x > 1) == Try(Exception('error'), False)
    assert Try(2, True).filter(lambda x: x > 1).on_success(lambda x: print(x)) == Try(2, True)
    assert Try(2, False).filter(lambda x: x > 1).on_success(lambda x: print(x)) == Try(2, False)



# Generated at 2022-06-14 03:47:35.978576
# Unit test for method filter of class Try
def test_Try_filter():
    """Unit test example."""
    def monad_value_filter(value):
        return str(value) == '1'

    t1 = Try.of(lambda x: x, 1)
    t1_filtered = t1.filter(monad_value_filter)
    assert t1_filtered == Try(1, True)

    t2 = Try.of(lambda x: x, 2)
    t2_filtered = t2.filter(monad_value_filter)
    assert t2_filtered == Try(2, False)



# Generated at 2022-06-14 03:47:40.247393
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(a):
        return True if a > 5 else False

    assert Try(5, True).filter(filterer) == Try(5, False)
    assert Try(10, True).filter(filterer) == Try(10, True)


# Generated at 2022-06-14 03:47:44.821090
# Unit test for method filter of class Try
def test_Try_filter():

    def test_init():
        assert Try(1, True) == Try(1, True)

    def test_filter():
        assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
        assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)

    test_init()
    test_filter()

# Generated at 2022-06-14 03:47:55.093484
# Unit test for method filter of class Try
def test_Try_filter():
    filter_func = lambda value: value < 5
    assert Try.of(lambda: 10).filter(filter_func) == Try(10, False)
    assert Try.of(lambda: 10).filter(filter_func).value == 10
    assert Try.of(lambda: 2).filter(filter_func) == Try(2, True)
    assert Try.of(lambda: 2).filter(filter_func).value == 2

    filter_func = lambda value: value < '5'
    assert Try.of(lambda: '10').filter(filter_func) == Try('10', False)
    assert Try.of(lambda: '2').filter(filter_func) == Try('2', True)
    assert Try.of(lambda: '2').filter(filter_func).value == '2'


# Generated at 2022-06-14 03:47:59.452119
# Unit test for method filter of class Try
def test_Try_filter():
    """
    test_Try_filter
    """
    assert Try.of(lambda: 1).filter(lambda x: x % 2 == 0) == Try(1, False)
    assert Try.of(lambda: 2).filter(lambda x: x % 2 == 0) == Try(2, True)


# Generated at 2022-06-14 03:48:17.013296
# Unit test for method filter of class Try
def test_Try_filter():
    def _filter(val):
        return val > 5

    t1 = Try(10, True)
    t2 = Try(3, True)
    t3 = Try(3, False)
    assert t1.filter(_filter) == Try(10, True)
    assert t2.filter(_filter) == Try(3, False)
    assert t3.filter(_filter) == Try(3, False)

# Unit tests for method get_or_else of class Try

# Generated at 2022-06-14 03:48:28.289926
# Unit test for method filter of class Try
def test_Try_filter():
    def is_even(value):
        return value % 2 == 0
    def is_even_param(value):
        return is_even(value.value)
    def is_not_even_param(value):
        return not is_even_param(value)

    assert Try(2, True).filter(is_even) == Try(2, True)
    assert Try(2, True).filter(is_even_param) == Try(2, True)
    assert Try(2, False).filter(is_even_param) == Try(2, False)
    assert Try(3, True).filter(is_even) == Try(3, False)
    assert Try(3, True).filter(is_not_even_param) == Try(3, False)


# Generated at 2022-06-14 03:48:35.197759
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value < 10
    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(1, False).filter(filterer) == Try(1, False)

    assert Try(11, True).filter(filterer) == Try(11, False)
    assert Try(11, False).filter(filterer) == Try(11, False)



# Generated at 2022-06-14 03:48:39.796241
# Unit test for method filter of class Try
def test_Try_filter():
    pass_filter = lambda value: value.is_success
    fail_filter = lambda value: False
    try_monad = Try(True, True)
    assert try_monad.filter(pass_filter) == Try(True, True)
    assert try_monad.filter(fail_filter) == Try(True, False)

    try_monad = Try(None, False)
    assert try_monad.filter(pass_filter) == Try(None, False)
    assert try_monad.filter(fail_filter) == Try(None, False)



# Generated at 2022-06-14 03:48:44.435626
# Unit test for method filter of class Try
def test_Try_filter():
    result = Try.of(lambda a: a * 2, 1)
    result = result.filter(lambda a: a > 0)
    assert result == Try(2, True)

    result = Try.of(lambda a: a * 2, -1)
    result = result.filter(lambda a: a > 0)
    assert result == Try(-2, False)

# Generated at 2022-06-14 03:48:49.689224
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 1

    try_value = Try(0, True)
    try_result = try_value.filter(filterer)
    assert try_result.is_success == False
    assert try_result.value == 0

    try_value = Try(2, True)
    try_result = try_value.filter(filterer)
    assert try_result.is_success == True
    assert try_result.value == 2

    try_value = Try(2, False)
    try_result = try_value.filter(filterer)
    assert try_result.is_success == False
    assert try_result.value == 2


# Generated at 2022-06-14 03:48:55.164490
# Unit test for method filter of class Try
def test_Try_filter():
    def bigger_10(value):
        return value > 10

    assert Try(15, True).filter(bigger_10) == Try(15, True)
    assert Try(5, True).filter(bigger_10) == Try(5, False)
    assert Try(5, False).filter(bigger_10) == Try(5, False)



# Generated at 2022-06-14 03:48:59.638321
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(int, '42')\
        .filter(lambda x: x > 3)\
        .value == 42

    assert Try.of(int, 'foo')\
        .filter(lambda x: x > 3) == Try(ValueError(), False)

    assert Try.of(int, 'foo')\
        .filter(lambda x: x > 3)\
        .value == ValueError()

    assert Try.of(int, 'foo')\
        .filter(lambda x: x > 3)\
        .is_success == False



# Generated at 2022-06-14 03:49:08.141075
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test method filter of class Try.
    """
    assert Try.of(lambda: 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda x: x != 1) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda x: x != 1).on_fail(lambda x: None) == Try(None, False)

    assert Try.of(lambda: 1/0).filter(lambda x: x == 1) == Try(0, False)
    assert Try.of(lambda: 1/0).filter(lambda x: x != 1) == Try(0, False)



# Generated at 2022-06-14 03:49:16.449748
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """
    def filterer(num):
        if num > 20:
            return True
        return False

    assert True == Try.of(lambda: 10, ).filter(filterer).is_success
    assert False == Try.of(lambda: 30, ).filter(filterer).is_success
    assert True == Try.of(lambda: 30, ).filter(filterer).is_success



# Generated at 2022-06-14 03:49:43.927450
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test Try.filter method on successfully monad.

    Usage:
        try:
            test_Try_filter()
        except Exception as e:
            print(e)

    :returns: nothing
    :rtype: None
    """
    def is_even(x) -> bool:
        return x % 2 == 0

    assert Try(2, True).filter(is_even) == Try(2, True)

    def is_odd(x) -> bool:
        return x % 2 != 0

    assert Try(2, True).filter(is_odd) == Try(2, False)



# Generated at 2022-06-14 03:49:47.395134
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    print('test_Try_filter')

    def filterer(value):
        return value.is_alive()

    def get_process():
        return psutil.Process(os.getpid())

    process = Try.of(get_process).filter(filterer).get()
    assert isinstance(process, psutil.Process)
    assert process.is_alive() is True


# Generated at 2022-06-14 03:49:52.439218
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda: 1, None).filter(lambda x: x == 1)\
           .bind(lambda: Try.of(lambda: 2, None)) == Try(2, True)
    assert Try.of(lambda: 1, None).filter(lambda x: x == 2)\
           .bind(lambda: Try.of(lambda: 1, None)) == Try(1, False)
    assert Try.of(lambda x: x, None).filter(lambda x: x == 1) == Try(None, False)

# Generated at 2022-06-14 03:49:57.407529
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 0) == Try(5, True)
    assert Try(0, True).filter(lambda x: x > 0) == Try(0, False)
    assert Try(exceptions.Exception(), False).filter(lambda x: x > 0) == Try(exceptions.Exception(), False)



# Generated at 2022-06-14 03:50:08.996919
# Unit test for method filter of class Try
def test_Try_filter():
    def t_f():
        return False

    def t_t():
        return True

    def t_raises():
        raise Exception('Test exception')

    assert Try(10, True).filter(t_f) == Try(10, False)
    assert Try(10, True).filter(t_t) == Try(10, True)
    assert Try(10, True).filter(t_raises) == Try(10, False)

    assert Try(None, False).filter(t_f) == Try(None, False)
    assert Try(None, False).filter(t_t) == Try(None, False)
    assert Try(None, False).filter(t_raises) == Try(None, False)


# Generated at 2022-06-14 03:50:15.304251
# Unit test for method filter of class Try
def test_Try_filter():
    # for successfully Try
    assert(Try(10, True).filter(lambda x: x > 5) == Try(10, True))
    # for not successfully Try
    assert(Try(10, False).filter(lambda x: x > 5) == Try(10, False))
    # when monad value doesn't pass filterer
    assert(Try(10, True).filter(lambda x: x > 15) == Try(10, False))

# Generated at 2022-06-14 03:50:23.544819
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer_positive(value):
        return value > 0
    def filterer_negative(value):
        return value < 0

    assert Success(1).filter(filterer_positive) == Success(1)
    assert Success(0).filter(filterer_positive) == Failure(0)
    assert Success(-1).filter(filterer_negative) == Success(-1)
    assert Success(1).filter(filterer_negative) == Failure(1)


# Generated at 2022-06-14 03:50:31.209456
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 'value', '').filter(lambda v: True) == Try('value', True)
    assert Try.of(lambda: 'value', '').filter(lambda v: False) == Try('value', True)
    assert Try.of(lambda: Exception('exception'), '').filter(lambda v: True) == Try(Exception('exception'), False)
    assert Try.of(lambda: Exception('exception'), '').filter(lambda v: False) == Try(Exception('exception'), False)


# Generated at 2022-06-14 03:50:37.279124
# Unit test for method filter of class Try
def test_Try_filter():
    first_value = Try.of(int, "1")
    second_value = Try.of(int, "a")

    assert first_value\
        .filter(lambda value: value == 1)\
        .is_success is True

    assert second_value\
        .filter(lambda value: value == 1)\
        .is_success is False

# Generated at 2022-06-14 03:50:49.759172
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try
    """
    result = Try.of(lambda: 1).filter(lambda v: v > 0)
    assert result == Try(1, True)

    result = Try.of(lambda: 1).filter(lambda v: v < 0)
    assert result == Try(1, False)

    result = Try.of(lambda: 1).filter(lambda v: v < 0)
    assert result == Try(1, False)

    result = Try.of(lambda: 0).filter(lambda v: v > 0)
    assert result == Try(0, False)

    result = Try.of(lambda: 0).filter(lambda v: v < 0)
    assert result == Try(0, False)

    result = Try.of(lambda: 0).filter(lambda v: v == 0)

# Generated at 2022-06-14 03:51:12.389954
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda val: val == 1)\
        == Try(1, True)
    assert Try(1, False).filter(lambda val: val == 1)\
        == Try(1, False)
    assert Try(1, True).filter(lambda val: val > 0)\
        == Try(1, True)
    assert Try(1, True).filter(lambda val: val < 0)\
        == Try(1, False)
    assert Try(1, False).filter(lambda val: val < 0)\
        == Try(1, False)


# Generated at 2022-06-14 03:51:17.895638
# Unit test for method filter of class Try
def test_Try_filter():
    # Arrange
    actual = 1
    expected = 1
    # Act
    def filterer(x): return x == actual
    # Assert
    assert Try.of(lambda x: x, actual)\
        .filter(filterer)\
        .get() == expected



# Generated at 2022-06-14 03:51:20.236020
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(int, '1').filter(lambda x: x == 1).get() == 1
    assert not Try.of(int, '1').filter(lambda x: x == 2).is_success


# Generated at 2022-06-14 03:51:26.559137
# Unit test for method filter of class Try
def test_Try_filter():
    def f(x):
        return x > 5

    assert Try(10, True).filter(f) == Try(10, True)
    assert Try(4, True).filter(f) == Try(4, False)
    assert Try(10, False).filter(f) == Try(10, False)



# Generated at 2022-06-14 03:51:34.555701
# Unit test for method filter of class Try
def test_Try_filter():
    fn = lambda x: x >= 0
    assert Try.of(lambda a: a, 1).filter(fn) == Try(1, True)
    assert Try.of(lambda a: a, -1).filter(fn) == Try(-1, False)
    assert Try.of(lambda a: a, -1).filter(fn).get_or_else(0) == 0
    assert Try.of(lambda a: a / 0, -1).filter(fn) == Try(ZeroDivisionError('float division by zero'), False)



# Generated at 2022-06-14 03:51:40.836341
# Unit test for method filter of class Try
def test_Try_filter():
    # function test for successful Try
    def true_func(name):
        return True

    # function test for successful Try
    def false_func(name):
        return False

    assert Try.of(lambda: 'bob')\
        .filter(true_func).is_success == True
    assert Try.of(lambda: 'bob')\
        .filter(false_func).is_success == False

    # test when value of Try is failure
    assert Try.of(lambda: 1 / 0)\
        .filter(true_func).is_success == False

# Generated at 2022-06-14 03:51:45.745986
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda a: a == 1) == Try(1, True)
    assert Try(2, True).filter(lambda a: a == 1) == Try(2, False)
    assert Try(2, False).filter(lambda a: a == 1) == Try(2, False)
# Test cases

# Generated at 2022-06-14 03:51:56.222505
# Unit test for method filter of class Try
def test_Try_filter():
    from string import ascii_lowercase

    assert Try('hello').filter(lambda v: v == 'hello') == Try(
        'hello', True), 'Test with true filter'
    assert Try('hello').filter(lambda v: v != 'hello') == Try(
        'hello', False), 'Test with false filter'
    assert Try(ascii_lowercase).filter(lambda v: all(x.islower() for x in v)) == Try(
        ascii_lowercase, True), 'Test with true filter and chain call'
    assert Try(ascii_lowercase).filter(lambda v: all(x.isupper() for x in v)) == Try(
        ascii_lowercase, False), 'Test with false filter and chain call'


# Generated at 2022-06-14 03:52:07.040042
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter(actual: Try, expected: Try):
        assert actual == expected

    def test_case(message: str, func: Callable, actual: Try, expected: Try):
        print(message, end=' ')
        test_filter(func(actual), expected)
        print('OK')

    test_case('test_filter_when_successful:', Try.filter,
            Try(1, True), Try(1, True))

    test_case('test_filter_when_failure:', Try.filter,
            Try(1, False), Try(1, False))

    test_case('test_filter_when_successful_but_filter_false:', Try.filter,
            Try(1, True).filter(lambda x: x == 2), Try(1, False))


# Generated at 2022-06-14 03:52:16.100258
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 2

    def filterer_raised(value):
        raise ValueError('I don\'t now what do you want from me')

    assert Try(2, True).filter(filterer) == Try(2, False)
    assert Try(3, True).filter(filterer) == Try(3, True)
    assert Try(5, True).filter(filterer_raised) == Try(5, True)
    assert Try(5, False).filter(filterer) == Try(5, False)

# Generated at 2022-06-14 03:52:42.788879
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x % 2 == 0) == Try(5, False)
    assert Try(4, True).filter(lambda x: x % 2 == 0) == Try(4, True)
    assert Try(5, False).filter(lambda x: x % 2 == 0) == Try(5, False)


# Generated at 2022-06-14 03:52:47.065343
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda x: 1 / 0, 1).filter(lambda x: x == 1) == Try(ZeroDivisionError('division by zero'), False)


# Generated at 2022-06-14 03:52:53.968306
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, 1).filter(lambda v: v == 1) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda v: v == 2) == Try(1, False)
    assert Try.of(lambda x: x / 0, 1).filter(lambda v: v == 1) == Try(1, False)



# Generated at 2022-06-14 03:52:57.676509
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    m = Try.of(int, "11")

    # When
    m1 = m.filter(lambda x: x > 10)
    m2 = m.filter(lambda x: x < 10)

    # Then
    assert m == Try(11, True)
    assert m1 == Try(11, True)
    assert m2 == Try(11, False)


# Generated at 2022-06-14 03:53:07.703423
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x != 5) == Try(5, False)
    assert Try(5, True).filter(lambda x: x == 5) == Try(5, True)
    assert Try(5, False).filter(lambda x: x == 5) == Try(5, False)
    assert Try(5, False).filter(lambda x: x != 5) == Try(5, False)
    assert Try(None, True).filter(lambda x: x is None) == Try(None, True)
    assert Try(None, True).filter(lambda x: x is not None) == Try(None, False)
    assert Try(None, False).filter(lambda x: x is None) == Try(None, False)

# Generated at 2022-06-14 03:53:12.305875
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(int, '10') == Try(10, True)
    assert Try.of(int, '10').filter(lambda x: x > 5) == Try(10, True)
    assert Try.of(int, '10').filter(lambda x: x > 15) == Try(10, False)
    assert Try.of(int, 'd').filter(lambda x: x > 5) == Try(ValueError, False)


# Generated at 2022-06-14 03:53:19.898559
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    success = Try(1, True)
    assert success.filter(lambda x: x == 1) == Try(1, True)
    assert success.filter(lambda x: x != 1) == Try(1, False)

    fail = Try(1, False)
    assert fail.filter(lambda x: x == 1) == Try(1, False)
    assert fail.filter(lambda x: x != 1) == Try(1, False)

# Generated at 2022-06-14 03:53:27.627011
# Unit test for method filter of class Try
def test_Try_filter():
    def call_function_with_args(fn):
        """
        Call function with args from list.

        :params fn: function to call.
        :type fn: Function(Return: Int)
        :returns: list of Try with result of callable functions
        :rtype: List[Try[Int]]
        """
        return [Try.of(fn, args) for args in [1, 2, 3, 4, 5]]


# Generated at 2022-06-14 03:53:36.802341
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(None, True).filter(lambda x: x is None) == Try(None, True)
    assert Try(None, False).filter(lambda x: x is None) == Try(None, False)
    assert Try(1, True).filter(lambda x: x is not None) == Try(1, True)
    assert Try(1, False).filter(lambda x: x is not None) == Try(1, False)
    assert Try(1, True).filter(lambda x: x is None) == Try(1, False)
    assert Try(1, False).filter(lambda x: x is None) == Try(1, False)



# Generated at 2022-06-14 03:53:44.607191
# Unit test for method filter of class Try
def test_Try_filter():
    def __filterer(value):
        return True

    def __tru_filterer(value):
        return True

    def __falsy_filterer(value):
        return False

    def __raiser(value):
        raise Exception('exhausted')

    assert Try(1, True).filter(__filterer) == Try(1, True)

    assert Try(1, False).filter(__filterer) == Try(1, False)

    assert Try(1, True).filter(__tru_filterer) == Try(1, True)

    assert Try(1, True).filter(__falsy_filterer) == Try(1, False)

    assert Try(1, False).filter(__tru_filterer) == Try(1, False)
