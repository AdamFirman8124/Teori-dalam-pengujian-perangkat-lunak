

# Generated at 2022-06-14 03:44:28.578997
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)

# Generated at 2022-06-14 03:44:34.857290
# Unit test for method filter of class Try
def test_Try_filter():
    """
    When try_test have value 5, we expect that new try_test object have value 5,
    but in othercase we expect that new try_test object have value other that 5.
    """

    def filterer(value):
        return value == 5

    try_test = Try(5, True)
    try_test_1 = try_test.filter(filterer)
    try_test_2 = try_test.filter(lambda x: x != 5)
    assert try_test_1.value == 5
    assert try_test_1.is_success
    assert try_test_2.is_success == False


# Generated at 2022-06-14 03:44:40.864099
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(4, True).filter(lambda x: x % 2 == 0) == Try(4, True)
    assert Try(4, True).filter(lambda x: x % 2 == 1) == Try(4, False)
    assert Try(5, False).filter(lambda x: x % 2 == 0) == Try(5, False)
    assert Try(5, False).filter(lambda x: x % 2 == 1) == Try(5, False)


# Generated at 2022-06-14 03:44:54.376775
# Unit test for method filter of class Try
def test_Try_filter():
    # GIVEN
    def filterer(number):
        return number > 10

    def fail_filterer(number):
        return number < 15

    def on_success(value):
        print('Success, value - {}'.format(value))

    def on_fail(value):
        print('Fail, value - {}'.format(value))

    # WHEN
    try_successful = Try.of(lambda x: x + 10, 50)
    try_not_successful = Try.of(lambda x: x + 100, 5)

    # THEN
    assert try_successful.filter(filterer).on_success(on_success).on_fail(on_fail) == Try(60, True)

# Generated at 2022-06-14 03:44:56.816095
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ).filter(lambda data: data == 1)\
        == Try(1, True)
    assert Try.of(lambda: 1, ).filter(lambda data: data == 2)\
        == Try(1, False)



# Generated at 2022-06-14 03:45:03.614415
# Unit test for method filter of class Try
def test_Try_filter():
    # When predicate returns True and Try is successfully
    assert True == Try(3, True).filter(lambda _: True).is_success
    # When predicate returns False and Try is successfully
    assert False == Try(3, True).filter(lambda _: False).is_success
    # When predicate returns True and Try is not successfully
    assert False == Try(3, False).filter(lambda _: True).is_success
    # When predicate returns False and Try is not successfully
    assert False == Try(3, False).filter(lambda _: False).is_success



# Generated at 2022-06-14 03:45:10.639263
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for filter method of class Try:

    :returns: None
    :rtype: None
    """
    assert Try(34, True).filter(lambda x: x % 2 == 0) == Try(34, False)
    assert Try(36, True).filter(lambda x: x % 2 == 0) == Try(36, True)
    assert Try(36, False).filter(lambda x: x % 2 == 0) == Try(36, False)


# Generated at 2022-06-14 03:45:20.805114
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of Try class.

    :returns: None
    :rtype: None
    """
    try_success = Try.of(lambda: 1)
    try_failure = Try.of(lambda: 1 / 0, 1)

    assert try_success.filter(lambda value: value > 0).is_success, 'Try is not successfully'
    assert not try_success.filter(lambda value: value == 0).is_success, 'Try should not be successfully'
    assert not try_failure.filter(lambda value: value == 0).is_success, 'Try should not be successfully'



# Generated at 2022-06-14 03:45:30.952916
# Unit test for method filter of class Try
def test_Try_filter():
    """
    We should use some simple function to test this case.
    The function return value which we give him as a param.

    >>> fn = lambda param: param
    >>> try_success = Try.of(fn, 1)
    >>> try_success.filter(lambda x: x == 1)
    Try[value=1, is_success=True]
    >>> try_success.filter(lambda x: x == 2)
    Try[value=1, is_success=False]
    >>> try_fail = Try.of(fn, ValueError())
    >>> try_fail.filter(lambda x: x == 1)
    Try[value=ValueError(), is_success=False]
    >>> try_fail.filter(lambda x: x == ValueError())
    Try[value=ValueError(), is_success=False]

    """
    pass


# Generated at 2022-06-14 03:45:40.363393
# Unit test for method filter of class Try
def test_Try_filter():
    def __filter(value):
        return value == 'hello'

    try_success = Try('hello', True)
    try_failure_true = Try('hello', False)
    try_failure_false = Try('world', False)

    assert try_success.filter(__filter).get() == 'hello'
    assert try_failure_true.filter(__filter).is_success == False
    assert try_failure_false.filter(__filter).is_success == False



# Generated at 2022-06-14 03:45:51.712382
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Check when filter method works correctly

    :params: None
    :returns: None
    :rtype: None
    """
    t = Try(5, True)
    t2 = t.filter(lambda x: x > 5)
    assert t2.get() == 5
    assert t2.is_success is True

    t = Try(4, True)
    t2 = t.filter(lambda x: x > 5)
    assert t2.get() == 4
    assert t2.is_success is False

    t = Try(4, False)
    t2 = t.filter(lambda x: x > 5)
    assert t2.get() == 4
    assert t2.is_success is False


# Generated at 2022-06-14 03:45:54.257230
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x <= 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x <= 0) == Try(1, False)


# Generated at 2022-06-14 03:45:57.963173
# Unit test for method filter of class Try
def test_Try_filter():
    print("test_Try_filter")
    assert Try(1, True).filter(lambda a: a == 1) == Try(1, True)
    assert Try(1, True).filter(lambda a: a == 2) == Try(1, False)

# Generated at 2022-06-14 03:46:06.969337
# Unit test for method filter of class Try
def test_Try_filter():
    try_value = Try("foo", True)
    try_filter_successful = try_value.filter(lambda x: True)
    try_filter_not_successful = try_value.filter(lambda x: False)

    assert isinstance(try_value, Try)
    assert isinstance(try_filter_successful, Try)
    assert isinstance(try_filter_not_successful, Try)

    assert try_filter_successful.is_success
    assert not try_filter_not_successful.is_success

    assert try_value == try_filter_successful
    assert try_value != try_filter_not_successful



# Generated at 2022-06-14 03:46:12.798727
# Unit test for method filter of class Try
def test_Try_filter():
    assert not Try.of(lambda: 1, ).filter(lambda x: x < 1).get()
    assert not Try.of(lambda: 1, ).filter(lambda x: x < 1).is_success
    assert Try.of(lambda: 1, ).filter(lambda x: x == 1).get() == 1
    assert Try.of(lambda: 1, ).filter(lambda x: x > 0).get() == 1
    assert Try.of(lambda: 1, ).filter(lambda x: x < 2).get() == 1
    assert Try.of(lambda: 1, ).filter(lambda x: True).get() == 1
    assert Try.of(lambda: 1, ).filter(lambda x: True).is_success
    assert not Try.of(lambda: 1, ).filter(lambda x: False).get()

# Generated at 2022-06-14 03:46:16.993254
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)


# Generated at 2022-06-14 03:46:28.316197
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value % 2 == 0

    # monad is successfully and filterer returns True
    try_1 = Try(2, True)
    assert try_1.filter(filterer) == Try(2, True)

    # monad is successfully and filterer returns False
    try_2 = Try(2, True)
    assert try_2.filter(lambda x: filterer(x) == False) == Try(2, False)

    # monad is not successfully and filterer returns True
    try_3 = Try(2, False)
    assert try_3.filter(filterer) == Try(2, False)



# Generated at 2022-06-14 03:46:32.765568
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 10

    assert Try.of(lambda: 1).filter(filterer) == Try(1, False)
    assert Try.of(lambda: 11).filter(filterer) == Try(11, True)

# Generated at 2022-06-14 03:46:37.059028
# Unit test for method filter of class Try
def test_Try_filter():
    result = Try.of(lambda x: x + 1, 1)\
        .filter(lambda x: x == 2)

    assert result.is_success is True
    assert result.value == 2

    result = Try.of(lambda x: x + 1, 1)\
        .filter(lambda x: x == 3)

    assert result.is_success is False
    assert result.value == 1

# Generated at 2022-06-14 03:46:44.269512
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test successful behaviour of method filter of class Try.
    """
    assert Try(5, True).filter(lambda x: x > 4) == Try(5, True)
    assert Try(5, True).filter(lambda x: x > 5) == Try(5, False)
    assert Try(5, True).filter(lambda x: x > 6) == Try(5, False)



# Generated at 2022-06-14 03:46:51.062087
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x > 10) == Try(10, False)

# Generated at 2022-06-14 03:46:54.730232
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try.of(str, 5) == Try("5", True)
    assert Try.of(str, 5).filter(lambda x: x.isdigit()) == Try("5", True)
    assert Try.of(str, 5).filter(lambda x: not x.isdigit()) == Try("5", False)
    assert Try.of(str, 5).filte

# Generated at 2022-06-14 03:47:01.595240
# Unit test for method filter of class Try
def test_Try_filter():
    def event_filter(event):
        return event.get('id') == 1

    assert Try(None, False).filter(event_filter) == Try(None, False)
    assert Try(None, True).filter(event_filter) == Try(None, False)
    assert Try({'id': 1}, True).filter(event_filter) == Try({'id': 1}, True)
    assert Try({'id': 2}, True).filter(event_filter) == Try({'id': 2}, False)


# Generated at 2022-06-14 03:47:04.339368
# Unit test for method filter of class Try
def test_Try_filter():
    failed = Try.of(lambda: 1 / 0)
    assert failed.filter(lambda x: 5 == x) == failed

    successful = Try.of(lambda: 5)
    assert successful.filter(lambda x: 5 == x) == successful


# Generated at 2022-06-14 03:47:10.513968
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value): return value > 0
    def filterer2(value): return value < 0

    try_instance = Try(1, True)
    try_instance_2 = Try(-1, True)
    try_instance_3 = Try(0, True)

    assert try_instance.filter(filterer) == Try(1, True)
    assert try_instance.filter(filterer2) == Try(1, False)
    assert try_instance_2.filter(filterer) == Try(-1, False)
    assert try_instance_2.filter(filterer2) == Try(-1, True)
    assert try_instance_3.filter(filterer) == Try(0, False)
    assert try_instance_3.filter(filterer2) == Try(0, False)




# Generated at 2022-06-14 03:47:16.274293
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 2) == Try(1, False)
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, False) == Try(1, True).filter(lambda x: x == 1)


# Generated at 2022-06-14 03:47:22.118151
# Unit test for method filter of class Try
def test_Try_filter():
    def is_valid(x):
        return x > 0

    monad = Try(1, True)
    monad2 = Try(1, False)
    monad3 = Try(-1, True)

    assert monad.filter(is_valid) == Try(1, True)
    assert monad2.filter(is_valid) == Try(1, False)
    assert monad3.filter(is_valid) == Try(-1, False)



# Generated at 2022-06-14 03:47:32.134752
# Unit test for method filter of class Try
def test_Try_filter():
    """
    1. When try is successfully and filterer returns True,
    the method filter returns Try with previous value successfully.

    2. When try is successfully and filterer returns False,
    the method filter returns Try with previous value not successfully.

    3. When try is not successfully, the method filter returns Try with previous value
    not successfully.
    """
    value = 1

    # successfully and True
    res = Try.of(lambda: value, )\
        .filter(lambda x: x == value)
    assert res == Try(value, True)

    # successfully and False
    res = Try.of(lambda: value, )\
        .filter(lambda x: x != value)
    assert res == Try(value, False)

    # not successfully
    res = Try.of(lambda: int('a'), )\
        .filter

# Generated at 2022-06-14 03:47:40.548281
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return True if value > 10 else False

    assert Try.of(lambda: 5, None) == Try(5, True)
    assert Try.of(lambda: 5, None).filter(filterer) == Try(5, False)
    assert Try.of(lambda: 10, None).filter(filterer) == Try(10, False)
    assert Try.of(lambda: 15, None).filter(filterer) == Try(15, True)



# Generated at 2022-06-14 03:47:46.039617
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for filter method of class Try
    """
    def filterer(x):
        return x % 2 == 0

    try_1 = Try.of(lambda x: x/2, 4)
    assert try_1.filter(filterer).get() == 2
    assert try_1.filter(filterer).is_success

    try_2 = Try.of(lambda x: x/2, 5)
    assert try_2.filter(filterer).get() == 5
    assert not try_2.filter(filterer).is_success

    print('test_Try_filter was passed')



# Generated at 2022-06-14 03:48:06.624440
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(http.client.OK, True).filter(lambda x: x == http.client.OK) == Try(http.client.OK, True)
    assert Try(http.client.OK, False).filter(lambda x: x == http.client.OK) == Try(http.client.OK, False)
    assert Try(http.client.OK, True).filter(lambda x: x == http.client.FORBIDDEN) == Try(http.client.OK, False)
    assert Try(http.client.OK, False).filter(lambda x: x == http.client.FORBIDDEN) == Try(http.client.OK, False)
    assert Try(http.client.OK, True).filter(lambda x: True) == Try(http.client.OK, True)

# Generated at 2022-06-14 03:48:16.628891
# Unit test for method filter of class Try
def test_Try_filter():
    def func_1(x):
        return x

    def func_2(x):
        return x * 2

    def func_3(x):
        return x * 3

    def filterer_1(x):
        return x % 2 == 0

    t1 = Try.of(func_1, 1)
    t2 = Try.of(func_2, 2)
    assert t1.filter(filterer_1) == Try(1, False)
    assert t2.filter(filterer_1) == Try(4, True)

    t1 = Try.of(func_1, 2)
    t2 = Try.of(func_2, 4)
    assert t1.filter(filterer_1) == Try(2, True)

# Generated at 2022-06-14 03:48:21.742802
# Unit test for method filter of class Try
def test_Try_filter():
    # Initial data
    Success = Try(None, False)
    Fail = Try(None, True)

    # Test for successful value
    def filterer(value):
        return True
    assert Success.filter(filterer) == Success

    # Test for not successful value
    def filterer(value):
        return True
    assert Fail.filter(filterer) != Success

    # Test for not successful value with successful result of filterer
    def filterer(value):
        return False
    assert Fail.filter(filterer) != Success
    assert Fail.filter(filterer) == Fail

    # Test for successful value with not successful result of filterer
    def filterer(value):
        return False
    assert Success.filter(filterer) == Fail



# Generated at 2022-06-14 03:48:27.263899
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try.
    """
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)



# Generated at 2022-06-14 03:48:31.575423
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(2, True).filter(lambda x: x == 2) == Try(2, True)
    assert Try(2, False).filter(lambda x: x == 2) == Try(2, False)
    assert Try(2, True).filter(lambda x: x < 2) == Try(2, False)

# Generated at 2022-06-14 03:48:39.649707
# Unit test for method filter of class Try
def test_Try_filter():
    assert_equals(Try.of(lambda: "42").map(lambda x: int(x)).filter(lambda x: x == 42), Try(42, True))
    assert_equals(Try.of(lambda: "42").map(lambda x: int(x)).filter(lambda x: x == 43), Try(42, False))
    assert_equals(Try.of(lambda: "42")\
                            .bind(lambda x: Try.of(lambda: "42") if int(x) == 42 else Try.of(lambda: "43"))\
                            .filter(lambda x: int(x) == 42), Try(42, True))

# Generated at 2022-06-14 03:48:46.432102
# Unit test for method filter of class Try
def test_Try_filter():
    assert\
        Try(None, "foo", True).filter(lambda v: type(v) == int)\
            == Try(None, False)\
        == Try(None, "foo", False).filter(lambda v: type(v) == int)\
            == Try(None, False)\
        == Try(1, "foo", True).filter(lambda v: type(v) == int)\
            == Try(1, True)\
        == Try(1, "foo", False).filter(lambda v: type(v) == int)\
            == Try(1, False)\
        is True

# Generated at 2022-06-14 03:48:53.836631
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try

    :returns: True statements
    :rtype: Boolean
    """
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try(2, True).filter(lambda x: x % 2 != 0) == Try(2, False)
    assert Try(2, False).filter(lambda x: x % 2 != 0) == Try(2, False)

# Generated at 2022-06-14 03:48:59.322925
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> test_Try_filter()
    True
    """
    fn = lambda x: x > 5
    val = 7
    assert Try(val, True).filter(fn).get() == val
    assert Try(val, True).filter(fn).is_success is True

    assert Try(val, False).filter(fn).get() == val
    assert Try(val, False).filter(fn).is_success is False

    fn = lambda x: x < 5
    assert Try(val, True).filter(fn).get() == val
    assert Try(val, True).filter(fn).is_success is False

    return True



# Generated at 2022-06-14 03:49:06.890793
# Unit test for method filter of class Try
def test_Try_filter():
    t0 = Try(2, True)
    assert t0.filter(lambda x: x == 2) == Try(2, True)
    assert t0.filter(lambda x: x < 2) == Try(2, False)
    assert Try(2, False).filter(lambda x: x < 2) == Try(2, False)

    t1 = Try(2, True).filter(lambda x: x < 2)
    assert isinstance(t1.value, Exception) and isinstance(t1.value, AssertionError) and \
        str(t1.value) == 'Filter condition is not satisfied'


# Generated at 2022-06-14 03:49:26.404434
# Unit test for method filter of class Try
def test_Try_filter():
    # Test when filter return True
    assert Try(42, True).filter(lambda x: x > 10) == Try(42, True)
    # Test when filter return False
    assert Try(42, True).filter(lambda x: x < 10) == Try(42, False)
    # Test for not successfully try
    assert Try(42, False).filter(lambda x: x < 10) == Try(42, False)

# Generated at 2022-06-14 03:49:33.309867
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(True, True).filter(lambda value: value)\
        == Try(True, True)
    assert Try(0, True).filter(lambda value: value)\
        == Try(0, False)
    assert Try(True, False).filter(lambda value: value)\
        == Try(True, False)
    assert Try(0, False).filter(lambda value: value)\
        == Try(0, False)


# Generated at 2022-06-14 03:49:40.907273
# Unit test for method filter of class Try
def test_Try_filter():
    def f(x):
        return x > 10

    # When Try is successfully and filter returns True
    assert Try(15, True).filter(f) == Try(15, True)
    # When Try is successfully and filter returns False
    assert Try(5, True).filter(f) == Try(5, False)
    # When Try is not successfully, then filter do nothing
    assert Try(6, False).filter(f) == Try(6, False)


# Generated at 2022-06-14 03:49:44.128178
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    x = Try(10, True)
    assert x.filter(lambda x: x < 20) == Try(10, True)
    assert x.filter(lambda x: x < 5) == Try(10, False)
    assert x.filter(lambda x: x < 5).value == 10

# Generated at 2022-06-14 03:49:51.226329
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda n: n % 2 == 0) == Try(42, True)
    assert Try(42, True).filter(lambda n: n % 2 == 1) == Try(42, False)
    assert Try(42, False).filter(lambda n: n % 2 == 0) == Try(42, False)
    assert Try(42, False).filter(lambda n: n % 2 == 1) == Try(42, False)


# Generated at 2022-06-14 03:49:58.152421
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda value: value > 7) == Try(10, True)
    assert Try(7, True).filter(lambda value: value > 7) == Try(7, False)
    assert Try(7, False).filter(lambda value: value > 7) == Try(7, False)
    assert Try(Exception('Error'), False).filter(lambda value: True) == Try(Exception('Error'), False)


# Generated at 2022-06-14 03:50:04.808417
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filter(x):
        if x > 10:
            return True
        return False

    try_monad = Try(11, True)

    assert try_monad.filter(filter) == Try(11, True)

    try_monad = Try(9, True)

    assert try_monad.filter(filter) == Try(9, False)



# Generated at 2022-06-14 03:50:07.392522
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda e: e > 0) == Try(1, True)
    assert Try('', True).filter(lambda e: True) == Try('', False)

# Generated at 2022-06-14 03:50:10.346870
# Unit test for method filter of class Try
def test_Try_filter():
    assert not Try.of(int, 'a').filter(lambda x: x < 10).is_success
    assert Try.of(int, '10').filter(lambda x: x < 100).is_success
    assert Try.of(int, '10').filter(lambda x: x < 100).value == 10


# Generated at 2022-06-14 03:50:13.669737
# Unit test for method filter of class Try
def test_Try_filter():
    test = Try('test', True)

    assert test.filter(lambda x: x == 'test') == test
    assert test.filter(lambda x: x == 'test1') != test

# Generated at 2022-06-14 03:50:36.479249
# Unit test for method map of class Try
def test_Try_map():
    assert Try(10, True).map(lambda x: x + 10) == Try(20, True)
    assert Try(10, False).map(lambda x: x + 10) == Try(10, False)

# Generated at 2022-06-14 03:50:38.552838
# Unit test for method get of class Try
def test_Try_get():
    assert Try(10, True).get() == 10

# Generated at 2022-06-14 03:50:43.347418
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, True) != Try(1, False)
    assert Try(1, True) != Try(2, True)
    assert Try(1, True) != Try(2, False)



# Generated at 2022-06-14 03:50:51.468356
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    """
    Test on_fail, expected fail_callback is called when monad is not successfully.
    """
    fail_callback = Mock()
    success_callback = Mock()

    Try(-1, False).on_fail(fail_callback).on_success(success_callback)
    fail_callback.assert_called_with(-1)
    success_callback.assert_not_called()

    Try(1, True).on_fail(fail_callback).on_success(success_callback)
    success_callback.assert_called_with(1)
    fail_callback.assert_called_with(-1)



# Generated at 2022-06-14 03:50:57.527083
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(None, True) == Try(None, True)
    assert Try(None, False) == Try(None, False)
    assert Try(None, True) != Try(None, False)
    assert Try('A', True) == Try('A', True)
    assert Try('A', False) == Try('A', False)
    assert Try('A', True) != Try('A', False)

#Unit test for method of of class Try

# Generated at 2022-06-14 03:51:00.187279
# Unit test for method get of class Try
def test_Try_get():
    result = Try.of(lambda: 1 / 0, None)
    assert result.get() is not None



# Generated at 2022-06-14 03:51:02.420906
# Unit test for constructor of class Try
def test_Try():
    assert Try(10, True) == Try(10, True)
    assert Try(10, True) != Try(10, False)
    assert Try(10, False) == Try(10, False)


# Generated at 2022-06-14 03:51:04.576173
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    # given
    value = 1
    try_monad = Try(value, True)

    # when
    result = try_monad.get_or_else(10)

    # then
    assert result == value



# Generated at 2022-06-14 03:51:08.094292
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():  # pragma: no cover
    assert Try(2, True).get_or_else(0) == 2
    assert Try(3, False).get_or_else(0) == 0



# Generated at 2022-06-14 03:51:19.207496
# Unit test for method map of class Try
def test_Try_map():
    assert Try.of(int, '1').map(lambda value: value + 1) == Try(2, True)
    assert Try.of(int, '1').map(lambda value: value + 1).map(lambda value: value * 2) == Try(4, True)
    assert Try.of(int, 'qwerty').map(lambda value: value + 1) == Try('qwerty', False)
    assert Try.of(lambda x: 1 / x, 1).map(lambda value: value + 1) == Try(2, True)
    assert Try.of(lambda x: 1 / x, 0).map(lambda value: value + 1) == Try(ZeroDivisionError(), False)
    assert Try.of(lambda: 1 / 0, 0).map(lambda value: value + 1) == Try(ZeroDivisionError(), False)



# Generated at 2022-06-14 03:52:05.580635
# Unit test for method map of class Try
def test_Try_map():
    assert Try(1, True).map(lambda x: x + 1) == Try(2, True)
    assert Try('Hello', True).map(lambda x: x.upper()) == Try('HELLO', True)
    assert Try(1, False).map(lambda x: x + 1) == Try(1, False)


if __name__ == '__main__':
    import nose
    nose.main()

# Generated at 2022-06-14 03:52:13.214118
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer_func(value):
        return value == 2
    assert Try.filter(Try(1, True), filterer_func) == Try(1, False)
    assert Try.filter(Try(2, True), filterer_func) == Try(2, True)
    assert Try.filter(Try(1, False), filterer_func) == Try(1, False)


# Generated at 2022-06-14 03:52:16.644573
# Unit test for constructor of class Try
def test_Try():
    """
    Tests for constructor Try
    """
    try_value = Try("test", True)
    assert try_value
    try_value = Try("test", False)
    assert try_value


# Generated at 2022-06-14 03:52:21.489452
# Unit test for method map of class Try
def test_Try_map():
    try_obj = Try.of(int, '10')
    assert try_obj.map(lambda x: x + 1) == Try(11, True)

    try_obj = Try.of(int, '10a')
    assert try_obj.map(lambda x: x + 10) == Try(ValueError, False)



# Generated at 2022-06-14 03:52:23.207967
# Unit test for method get of class Try
def test_Try_get():
    value = Try(5, True).get()
    assert value == 5



# Generated at 2022-06-14 03:52:26.446613
# Unit test for method __str__ of class Try
def test_Try___str__():  # pragma: no cover
    assert str(Try(23, True)) == 'Try[value=23, is_success=True]'
    assert str(Try(23, False)) == 'Try[value=23, is_success=False]'


# Generated at 2022-06-14 03:52:31.992587
# Unit test for method map of class Try
def test_Try_map():
    assert Try.of(lambda: 'something').map(lambda x: x.upper()) == Try('SOMETHING', True)
    assert Try.of(lambda: 'something').map(lambda x: x.upper()).value == 'SOMETHING'
    assert Try.of(lambda: (1/0)).map(lambda x: x.upper()) == Try('division by zero', False)
    assert Try.of(lambda: (1/0)).map(lambda x: x.upper()).value == 'division by zero'


# Generated at 2022-06-14 03:52:37.032650
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try.of(lambda: 1, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1, 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda: 1, 1).filter(lambda x: x == 1).get() == 1
    assert Try.of(lambda: 1, 1).filter(lambda x: x == 2).get_or_else(0) == 0


# Generated at 2022-06-14 03:52:42.035565
# Unit test for method on_success of class Try
def test_Try_on_success():
    def my_func(a: int) -> int:
        return a + 10

    assert Try(10, True).on_success(my_func) == Try(20, True)
    assert Try(10, False).on_success(my_func) == Try(10, False)


# Generated at 2022-06-14 03:52:45.749923
# Unit test for constructor of class Try
def test_Try():
    assert Try(1, True) == Try(1, True)
    assert Try(1, True) != Try(1, False)
    assert Try(1, False) != Try(2, False)


# Generated at 2022-06-14 03:54:22.681317
# Unit test for constructor of class Try
def test_Try():
    assert Try('value', True) == Try('value', True)
    assert Try(None, False) == Try(None, False)
