

# Generated at 2022-06-14 03:44:40.618076
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Assert that in the case of a successful filter
    on the successful Try, nothing changes
    in case of an unsuccessful filter, the Try becomes unfulfilled.
    """
    from hypothesis import given
    from hypothesis.strategies import integers, just, lists
    # Data for assertions
    empty_list = []
    list_of_int = [1, 2, 3]
    assert isinstance(empty_list, list)
    assert isinstance(list_of_int, list)
    # Data for testing
    list_of_int_or_empty = lists(integers(), min_size=0)\
        .filter(lambda x: isinstance(x, list))
    true_bool = just(True)
    false_bool = just(False)


# Generated at 2022-06-14 03:44:46.610545
# Unit test for method filter of class Try
def test_Try_filter():
    def predicate(x):
        return x > 1

    assert Try.of(lambda x: x, 1).filter(predicate) == Try(1, False)
    assert Try.of(lambda x: x, 2).filter(predicate) == Try(2, True)

# Generated at 2022-06-14 03:44:56.088672
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
    test example:
        >>> 'test' + 1
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: must be str, not int

    Work with error:
        >>> Try.of(lambda: 'test' + 1).filter(lambda x: isinstance(x, str)).get()
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: must be str, not int

    Work without error:
        >>> Try.of(lambda: 'test1').filter(lambda x: isinstance(x, str)).get()
        'test1'
    """
    pass

# Generated at 2022-06-14 03:45:07.330768
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x == 1

    def fail_filterer(x):
        return x != 1

    assert Try(None, True).filter(filterer) == Try(None, False)
    assert Try(None, True).filter(filterer) != Try(None, True)
    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(2, True).filter(filterer) == Try(2, False)
    assert Try(2, True).filter(filterer) != Try(2, True)
    assert Try(1, True).filter(fail_filterer) == Try(1, False)
    assert Try(1, True).filter(fail_filterer) != Try(1, True)


# Generated at 2022-06-14 03:45:11.534671
# Unit test for method filter of class Try
def test_Try_filter():
    def foo(value):
        return value > 10

    assert Try.of(lambda: 10).filter(foo).get_or_else(0) == 0
    assert Try.of(lambda: 20).filter(foo).get_or_else(0) == 20


# Generated at 2022-06-14 03:45:15.339356
# Unit test for method filter of class Try
def test_Try_filter():
    # 1
    assert Try(1, True).filter(lambda v: v == 1) == Try(1, True)
    # 2
    assert Try(1, True).filter(lambda v: v == 2) == Try(1, False)
    # 3
    assert Try('try', False).filter(lambda v: v == 'try') == Try('try', False)

# Generated at 2022-06-14 03:45:17.701953
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test method filter of class Try.
    """
    assert Try.of(lambda: 's', ()).filter(lambda x: x == 's') == Try('s', True)
    assert Try.of(lambda: 's', ()).filter(lambda x: x is not 's') == Try('s', False)


# Generated at 2022-06-14 03:45:25.151276
# Unit test for method filter of class Try
def test_Try_filter():
    value = 1
    def filterer(value):
        return value > 0

    assert Try(value, True).filter(filterer) == Try(value, True)
    assert Try(value, False).filter(filterer) == Try(value, False)
    assert Try(value, True).filter(lambda _: False) == Try(value, False)
    assert Try(value, False).filter(lambda _: True) == Try(value, False)



# Generated at 2022-06-14 03:45:32.152653
# Unit test for method filter of class Try
def test_Try_filter():
    def test(name, fn, value, expect):
        if fn.filter(lambda x: x == value).get() == expect:
            print('[{}]:  Testing {}, {}, {}, {} OK'.format(ok, name, fn, value, expect))
        else:
            print('[{}]:  Testing {}, {}, {}, {} NG'.format(ng, name, fn, value, expect))

    test('Test success filter', Try(5, True), 5, 5)
    test('Test fail filter', Try(5, False), 5, 5)
    test('Test success filter with default value and success', Try(5, True), 5, 5)
    test('Test success filter with default value and not success', Try(5, False), 5, None)

test_Try_filter()

# Generated at 2022-06-14 03:45:36.801134
# Unit test for method filter of class Try
def test_Try_filter():
    def func(value):
        if value:
            return True

    assert Try(1, True).filter(func) == Try(1, True)
    assert Try(None, False).filter(func) == Try(None, False)



# Generated at 2022-06-14 03:45:50.763944
# Unit test for method filter of class Try
def test_Try_filter():
    # test with successfully try
    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, True).filter(lambda x: True) != Try(2, True)

    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, True).filter(lambda x: True) != Try(1, False)

    # test with not successfully test
    assert Try(1, True).filter(lambda x: False) == Try(1, False)
    assert Try(1, True).filter(lambda x: False) != Try(2, False)

    assert Try(1, False).filter(lambda x: True) == Try(1, False)
    assert Try(1, False).filter(lambda x: True) != Try(2, False)



# Generated at 2022-06-14 03:46:02.214291
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda x: x == 2).on_fail(lambda x: x.__str__()) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda x: x == 2).on_success(lambda x: x.__str__()) == Try(1, False)
    assert Try.of(lambda: 1 / 0).filter(lambda x: True) == Try(ZeroDivisionError("division by zero"), False)

# Generated at 2022-06-14 03:46:12.543356
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of Try class
    """

    def assert_Try_filter(function, args, expected_value):
        """
        Test filter method with data

        :params function: function to apply on monad value
        :type function: Function(A) -> B
        :params args: argument of function
        :type args: List
        :params expected_value: expected result of function call
        :type expected_value: B
        """
        assert Try.of(function, *args).filter(lambda x: True) == expected_value
        assert Try.of(function, *args).filter(lambda x: True).is_success
        assert Try.of(function, *args).filter(lambda x: False).is_success is False


# Generated at 2022-06-14 03:46:15.771065
# Unit test for method filter of class Try
def test_Try_filter():  # type: () -> None
    """
    Unit test for method filter of class Try.
    """
    value = 'test'
    try_ = Try(value, True)
    filtered_try = try_.filter(lambda x: x == value)
    assert try_ == filtered_try
    filtered_try = try_.filter(lambda x: x != value)
    assert not filtered_try.is_success
    assert filtered_try.value == value



# Generated at 2022-06-14 03:46:18.438391
# Unit test for method filter of class Try
def test_Try_filter():
    assert (
        Try(1, True).filter(lambda num: num > 0)
        ==
        Try(1, True)
    )

    assert (
        Try(1, True).filter(lambda num: num < 0)
        ==
        Try(1, False)
    )


# Generated at 2022-06-14 03:46:23.884032
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(3, True).filter(lambda x: x < 10) == Try(3, True)
    assert Try(3, True).filter(lambda x: x < 2) == Try(3, False)
    assert Try(3, False).filter(lambda x: x < 10) == Try(3, False)

# Generated at 2022-06-14 03:46:33.546226
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    from random import randint
    from threading import Thread

    def bad_function(func):
        def wrapper(*args):
            rand = randint(0, 5)
            print("rand:", rand)
            if rand == 5:
                raise RuntimeError("bad guy happens")
            return func(*args)
        return wrapper


    @bad_function
    def function(arg):
        """
        Simple function that returns arg
        """
        return arg


    def check(value):
        try:
            function(value)
            return True
        except Exception:
            return False


    assert Try.of(function, "sasa").filter(check).get() == "sasa"
    assert Try.of(function, 5).filter(check).get() == 5

# Generated at 2022-06-14 03:46:43.170316
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def check_is_int(some_value):
        return type(some_value) is int

    def do_nothing(some_value):
        pass

    def expect_error(exception):
        assert exception.args[0] == "some_error" \
            or exception.args[0] == "some_value is not int"

    assert Try.of(int, "123").filter(check_is_int) == Try(123, True)
    assert Try.of(int, "some_value").filter(check_is_int) == Try(ValueError(), False)
    assert Try(ValueError("some_value is not int"), False).filter(check_is_int) == \
        Try(ValueError("some_value is not int"), False)

# Generated at 2022-06-14 03:46:55.305797
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x:x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x:x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x:x < 1) == Try(1, False)
    assert Try(1, True).filter(lambda x:x == 2) == Try(1, False)
    assert Try(1, True).filter(lambda x:x == 2) == Try(1, False)

    assert Try(1, False).filter(lambda x:x == 1) == Try(1, False)
    assert Try(1, False).filter(lambda x:x > 0) == Try(1, False)
    assert Try(1, False).filter(lambda x:x < 1) == Try(1, False)

# Generated at 2022-06-14 03:47:01.761212
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 2
    # Is not successfully
    assert Try(1, False).filter(filterer) == Try(1, False)
    # Is successfully, filterer return True
    assert Try(3, True).filter(filterer) == Try(3, True)
    # Is successfully, filterer return False
    assert Try(2, True).filter(filterer) == Try(2, False)


# Generated at 2022-06-14 03:47:07.005905
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 10) == Try(1, False)
    assert Try(11, True).filter(lambda x: x > 10) == Try(11, True)
    assert Try(1, False).filter(lambda x: x > 10) == Try(1, False)


# Generated at 2022-06-14 03:47:09.762265
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda v: v == 2) == Try(2, True)
    assert Try(2, True).filter(lambda v: v != 2) == Try(2, False)
    assert Try(2, False).filter(lambda v: v == 2) == Try(2, False)


# Generated at 2022-06-14 03:47:21.562026
# Unit test for method filter of class Try
def test_Try_filter():
    # success
    try_mock = Mock(
        value=1,
        is_success=True,
        side_effect=lambda a: Try(a, is_success=True)
    )
    filterer_mock = Mock(return_value=True)

    try_result = Try.of(lambda: 1, None).filter(filterer_mock)
    assert try_result == Try(1, True)
    filterer_mock.assert_called_once_with(1)
    try_mock.assert_not_called()

    filterer_mock.reset_mock()
    try_mock.reset_mock()

    # failure
    filterer_mock = Mock(return_value=False)
    try_result = Try.of(lambda: 1, None).filter

# Generated at 2022-06-14 03:47:26.035794
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x > 0) == Try(1, False)
    assert Try(-1, True).filter(lambda x: x > 0) == Try(-1, False)


# Generated at 2022-06-14 03:47:32.320485
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x + 1, 5).filter(lambda x: x % 2 == 0) == Try(5, False)
    assert Try.of(lambda x: x + 1, 6).filter(lambda x: x % 2 == 0) == Try(6, True)


# Generated at 2022-06-14 03:47:44.192255
# Unit test for method filter of class Try
def test_Try_filter():

    # Successfully Try with value None
    try_success = Try(None, True)
    assert(try_success.value is None and try_success.is_success == True)

    # Fail Try with value None
    try_fail = Try(None, False)
    assert(try_fail.value is None and try_fail.is_success == False)

    # When filterer return True, Try copy should be returned
    try_success_copy = try_success.filter(lambda x: x is None)
    assert(try_success_copy.value is None and try_success_copy.is_success == True)

    # When filterer return False, not successfully Try should be returned
    try_fail_copy = try_success.filter(lambda x: x is not None)

# Generated at 2022-06-14 03:47:49.678521
# Unit test for method filter of class Try
def test_Try_filter():

    identity = lambda x: x
    filtered = Try.of(identity, 1).filter(lambda x: x > 0)

    assert filtered.value == 1
    assert filtered.is_success is True

    filtered = Try.of(identity, 1).filter(lambda x: x < 0)

    assert filtered.value == 1
    assert filtered.is_success is False


# Generated at 2022-06-14 03:47:57.198839
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filterer(a):
        return a < 5

    test_try = Try.of(lambda x: x, 5)
    assert Try(5, True).filter(test_filterer) == test_try.filter(test_filterer)

    test_try = Try.of(lambda x: x, 4)
    assert test_try.filter(test_filterer) == test_try

    fail_try = Try.of(lambda x: 1/0, None)
    assert fail_try.filter(test_filterer) == fail_try
    assert not fail_try.filter(test_filterer).is_success


# Generated at 2022-06-14 03:47:59.004008
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x > 0) == Try(10, True)
    assert Try(10, True).filter(lambda x: x < 0) == Try(10, False)

# Generated at 2022-06-14 03:48:05.565193
# Unit test for method filter of class Try
def test_Try_filter():
    def five():
        return 5

    def big_five(x):
        return x >= 5

    assert Try.of(five).filter(big_five) == Try(5, True)
    assert Try.of(five).filter(lambda x: x < 4) == Try(5, False)
    assert Try.of(lambda: 5/0).filter(big_five) == Try(5, False)


# Generated at 2022-06-14 03:48:14.376758
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try.of(int, 2).map(lambda x: x ** 20).filter(lambda x: x > 5) == Try(1048576, True)
    assert Try.of(int, 2).map(lambda x: x ** 20).filter(lambda x: x < 5) == Try(1048576, False)



# Generated at 2022-06-14 03:48:19.492608
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x % 2 == 0

    try_wrong = Try.of(lambda: 1)
    try_success = Try.of(lambda: 2)

    assert not try_wrong.filter(filterer).is_success
    assert try_success.filter(filterer).is_success



# Generated at 2022-06-14 03:48:30.689837
# Unit test for method filter of class Try
def test_Try_filter():
    def filter_success(value): return value > 10
    def filter_fail(value): return value < 10
    def filter_exception(_): raise Exception('exception')

    assert Try.of(lambda x: x, 10).filter(filter_success).is_success == False
    assert Try.of(lambda x: x, 10).filter(filter_fail).is_success == False
    assert Try.of(lambda x: x, 10).filter(filter_exception).is_success == False

    assert Try.of(lambda x: x, 20).filter(filter_success).is_success == True
    assert Try.of(lambda x: x, 20).filter(filter_fail).is_success == False
    assert Try.of(lambda x: x, 20).filter(filter_exception).is_success == False


# Generated at 2022-06-14 03:48:32.354759
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.filter(None, None) == Try(None, False)

# Generated at 2022-06-14 03:48:37.195250
# Unit test for method filter of class Try
def test_Try_filter():
    try_func = Try(True, True)
    try_func_false = Try(False, True)
    try_func_err = Try(False, False)

    assert try_func.filter(lambda x: x).is_success
    assert not try_func_false.filter(lambda x: x).is_success
    assert not try_func_err.filter(lambda x: x).is_success



# Generated at 2022-06-14 03:48:44.205267
# Unit test for method filter of class Try
def test_Try_filter():
    try_1 = Try.of(int, '2')
    try_2 = try_1.filter(lambda x: x > 1)
    try_3 = try_1.filter(lambda x: x > 3)
    assert try_1 == Try(2, True)
    assert try_2 == Try(2, True)
    assert try_3 == Try(2, False)


# Generated at 2022-06-14 03:48:49.087668
# Unit test for method filter of class Try
def test_Try_filter():
    fn = lambda x: x % 2 == 0
    val = 10
    fn_res = fn(val)
    try_ = Try.of(lambda x: x, val).filter(fn)
    assert isinstance(try_.value, type(val))
    assert try_.value == val
    assert try_.is_success == fn_res

    val = 11
    fn_res = fn(val)
    try_ = Try.of(lambda x: x, val).filter(fn)
    assert isinstance(try_.value, type(val))
    assert try_.value == val
    assert try_.is_success == fn_res

# Generated at 2022-06-14 03:48:53.257551
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    x = Try.of(lambda: 10)
    assert x.filter(lambda a: a == 10) == Try(10, True)
    assert x.filter(lambda a: a != 10) == Try(10, False)


# Generated at 2022-06-14 03:48:57.835299
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test case for filter method of class Try.
    """
    def filter_less_than_10(x):
        return x < 10

    assert Try.of(lambda: 5).filter(filter_less_than_10) == Try(5, True)
    assert Try.of(lambda: 11).filter(filter_less_than_10) == Try(11, False)

# Generated at 2022-06-14 03:49:00.584125
# Unit test for method filter of class Try
def test_Try_filter():
    f = lambda x: x % 2 == 0

    assert Try.of(lambda x: x, 2).filter(f) == Try(2, True)
    assert Try.of(lambda x: x, 3).filter(f) == Try(3, False)

# Generated at 2022-06-14 03:49:09.126877
# Unit test for constructor of class Try
def test_Try():
    t1 = Try('success', True)
    t2 = Try('error', False)
    assert t1.value == 'success'
    assert t1.is_success
    assert t2.value == 'error'
    assert not t2.is_success
    assert t1 != t2
    assert t1 == Try('success', True)



# Generated at 2022-06-14 03:49:13.718471
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    try:
        raise Exception('Booom!')
    except Exception as e:
        try_ = Try(e, False)
        try_.on_fail(lambda e: e)



# Generated at 2022-06-14 03:49:21.440962
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    call_times = 0  # Variable for assert that function call only 1 time on monad

    def fail_callback(value):  # Function for check call_times
        nonlocal call_times
        call_times += 1

    # Check on_fail method
    not_success_monad = Try('error', False).on_fail(fail_callback)

    assert call_times == 1  # assert that function called 1 time
    assert not_success_monad.is_success is False  # assert that monad is not successfully

    # Check that on_fail not call fail_callback function on successfully monad
    success_monad = Try('success', True).on_fail(fail_callback)

    assert call_times == 1  # assert that function not called again
    assert success_monad.is_success is True  # assert that monad is successfully


# Generated at 2022-06-14 03:49:25.085318
# Unit test for method on_success of class Try
def test_Try_on_success():  # pragma: no cover
    def test_fn(value):
        assert value == 1

    Try(1, True).on_success(test_fn)



# Generated at 2022-06-14 03:49:35.260590
# Unit test for method map of class Try
def test_Try_map():
    """Unit test for method map of class Try"""
    assert Try(5, True).map(lambda x: x * 10) == Try(50, True)
    assert Try(5, False).map(lambda x: x * 10) == Try(5, False)
    assert Try(5, True).map(lambda x: x + '5') == Try(55, True)
    assert Try('5', True).map(lambda x: int(x) + 5) == Try(10, True)
    assert Try(None, False).map(lambda x: x + 5) == Try(None, False)
    assert Try(None, False).map(lambda x: x * 10) == Try(None, False)


# Generated at 2022-06-14 03:49:41.783019
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(x):
        return x > 3
    result = Try.of(lambda: 5).filter(filterer)
    assert isinstance(result, Try)
    assert result == Try(5, True)

    result = Try.of(lambda: 1).filter(filterer)
    assert isinstance(result, Try)
    assert result == Try(1, False)


# Generated at 2022-06-14 03:49:47.863021
# Unit test for method on_success of class Try
def test_Try_on_success():
    assert Try(1, True).on_success(lambda x: print(x)) == Try(1, True)
    assert Try(1, False).on_success(lambda x: print(x)) == Try(1, False)



# Generated at 2022-06-14 03:49:49.513369
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try("1", True) == Try("1", True)
    assert Try("1", True) != Try("1", False)
    assert Try("1", False) != Try("2", False)


# Generated at 2022-06-14 03:49:56.751394
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)
    assert Try(1, True) != Try(1, False)
    assert Try(1, False) != Try(1, True)
    assert Try(1, True) != Try(2, True)
    assert Try(1, True) != 'Try[value=1, is_success=True]'


# Generated at 2022-06-14 03:50:10.138231
# Unit test for method bind of class Try
def test_Try_bind():
    assert Try.of(lambda: 'a').bind(lambda x: Try(x + 'b', True)) == Try('ab', True)
    assert Try.of(lambda: 'a').bind(lambda x: Try(x + 'b', False)) == Try('a', True)
    assert Try.of(lambda: None).bind(lambda x: Try(x + 'b', False)) == Try(None, True)
    assert Try.of(lambda: 1/0).bind(lambda x: Try(x + 'b', True)) == Try(None, False)

    assert Try.of(lambda: 1/0).bind(lambda x: Try(x + 'b', True)) == Try.of(lambda: 1/0).bind(lambda x: Try(x + 'b', True))

# Generated at 2022-06-14 03:50:27.855984
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    assert Try(1, True).on_fail(lambda x: None) == Try(1, True)
    assert Try('except', False).on_fail(lambda x: None) == Try('except', False)
    assert Try('except', False).on_fail(lambda x: print('do something with', x)) == Try('except', False)
    try:
        assert Try('except', False).on_fail(lambda x: print('do something with', x)) == Try('except', False)
    except:
        pass
    else:
        assert False, "not raise exception"


# Generated at 2022-06-14 03:50:34.859694
# Unit test for constructor of class Try
def test_Try():
    try_1 = Try(1, True)
    try_2 = Try(1, True)
    try_3 = Try(2, True)
    try_4 = Try(1, False)
    try_5 = Try(2, False)
    try_6 = Try(Exception('failure'), False)

    assert try_1 == try_1
    assert try_1 == try_2
    assert try_2 == try_1
    assert try_1 != try_3
    assert try_2 != try_3
    assert try_1 != try_4
    assert try_1 != try_5
    assert try_1 != try_6



# Generated at 2022-06-14 03:50:42.479248
# Unit test for method map of class Try
def test_Try_map():
    assert Try.of(lambda: 10, None).map(lambda x: x // 2) == Try(5, True)
    assert Try.of(lambda: 10, None).map(lambda x: x // 0) == Try(ZeroDivisionError('division by zero'), False)
    assert Try.of(lambda: 1 // 0, None).map(lambda x: x // 2) == Try(ZeroDivisionError('division by zero'), False)


# Generated at 2022-06-14 03:50:46.161191
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    a = Try.of(int, 1)
    print(a.filter(lambda _: 1 == 1))
    print(a.filter(lambda _: 2 == 1))


# Generated at 2022-06-14 03:50:50.494425
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    assert Try(1, True).on_fail(lambda e: e) == Try(1, True)
    assert Try(Exception('Test'), False).on_fail(lambda e: e) == Try(Exception('Test'), False)


# Generated at 2022-06-14 03:50:56.835416
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    def fail_callback(a):
        assert a == 2, 'Expected 2, but got {}'.format(a)

    def success_callback(a):
        raise Exception('Should not be called')

    Try(1, True).on_fail(fail_callback).on_success(success_callback)
    Try(2, False).on_fail(fail_callback)

test_Try_on_fail()

# Generated at 2022-06-14 03:51:00.405110
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():  # pragma: no cover
    """
    Test for Try.get_or_else method
    """
    assert Try(100, True).get_or_else(10) == 100
    assert Try(100, False).get_or_else(10) == 10


# Generated at 2022-06-14 03:51:01.675739
# Unit test for method get of class Try
def test_Try_get():
    assert Try('test', True).get() == 'test'


# Generated at 2022-06-14 03:51:03.518874
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(2, True) == Try(2, True)
    assert Try(3, False) == Try(3, False)



# Generated at 2022-06-14 03:51:04.851944
# Unit test for method get of class Try
def test_Try_get():
    assert Try(1, True).get() == 1
    assert Try('a', True).get() == 'a'


# Generated at 2022-06-14 03:51:29.135340
# Unit test for method bind of class Try
def test_Try_bind():
    """
    Test for Try.bind method.
    """
    def double(x):
        return Try(x * 2, True)
    try_success = Try(1, True)
    try_fail = Try(1, False)
    assert try_success.bind(double) == Try(2, True)
    assert try_fail.bind(double) == Try(1, False)


# Generated at 2022-06-14 03:51:34.536786
# Unit test for method bind of class Try
def test_Try_bind():  # pragma: no cover
    def point_2(x):
        return Try(x + 2, True)

    def point_3(x):
        return Try(x + 3, True)

    assert Try(0, True).bind(point_2).bind(point_3) == Try(5, True)
    assert Try(0, True).bind(point_2).bind(point_3).get() == 5
    assert Try(None, False).bind(point_2).bind(point_3) == Try(None, False)
    assert Try(0, True).bind(point_2).bind(point_3).is_success == True



# Generated at 2022-06-14 03:51:36.316817
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert str(Try('value', True)) == 'Try[value=value, is_success=True]'


# Generated at 2022-06-14 03:51:43.556671
# Unit test for method bind of class Try
def test_Try_bind():

    # Test when monad is successfully
    def test_when_monad_is_successfully(monad, binder):
        monad.bind(binder)

        assert binder.called is True
        assert binder.args == (10, )

    # Test when monad is not successfully
    def test_when_monad_is_not_successfully(monad, binder):
        monad.bind(binder)

        assert binder.called is False

    class Binder:
        def __init__(self):
            self.called = False
            self.args = ()

        def __call__(self, *args, **kwargs):
            self.called = True
            self.args = args

        def bind(self, value):
            return Try(value + 5, True)

    binder = Binder()
   

# Generated at 2022-06-14 03:51:49.102986
# Unit test for method filter of class Try
def test_Try_filter():
    """Unit test for method filter of class Try
    """

    assert Try(3, True).filter(lambda v: v == 3) == Try(3, True)
    assert Try(3, True).filter(lambda v: v == 4) == Try(3, False)
    assert Try(3, False).filter(lambda v: v == 3) == Try(3, False)

# Generated at 2022-06-14 03:51:53.760180
# Unit test for method bind of class Try
def test_Try_bind():
    from functools import partial

    def func(value):
        return Try(value, True)
    assert Try.of(int, '1').bind(func) == func(1)
    assert Try.of(int, 'a').bind(partial(func, 2)) == Try(2, False)



# Generated at 2022-06-14 03:51:55.737506
# Unit test for method get of class Try
def test_Try_get():
    assert Try.of(lambda: 1).get() == 1
    assert not Try.of(lambda: 1 / 0).get()


# Generated at 2022-06-14 03:51:57.692366
# Unit test for method get of class Try
def test_Try_get():
    assert Try(1, True).g

# Generated at 2022-06-14 03:52:00.045349
# Unit test for method on_success of class Try
def test_Try_on_success():
    a = Try(42, True).on_success(lambda x: print(x))
    assert a.is_success == True


# Generated at 2022-06-14 03:52:04.380266
# Unit test for method on_success of class Try
def test_Try_on_success():
    try:
        True
    except Exception:
        pass
    else:
        assert Try.of(True).on_success(lambda result: result == True) is not None
        assert Try.of(None).on_success(lambda result: result) is not None



# Generated at 2022-06-14 03:52:48.887263
# Unit test for method bind of class Try
def test_Try_bind():
    fn = lambda: Try(1, True)
    t = Try.of(fn)
    assert t.bind(fn) == Try(1, True)
    fn = lambda: Try(1, False)
    t = Try.of(fn)
    assert t.bind(fn) == Try(1, False)
    fn = lambda: 1
    t = Try.of(fn)
    assert t.bind(fn) == Try(1, True)
    fn = lambda: 1
    t = Try.of(fn)
    assert t.bind(fn) == Try(1, True)


# Generated at 2022-06-14 03:52:52.882705
# Unit test for method map of class Try
def test_Try_map():
    def add_one(value: int) -> int:
        return value + 1

    assert Try(1, True).map(add_one) == Try(2, True)
    assert Try(1, False).map(add_one) == Try(1, False)


# Generated at 2022-06-14 03:53:00.344726
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 'Hello').map(lambda a: a[2])\
        .filter(lambda b: len(b) == 3)\
        == Try('l', True)
    assert Try.of(lambda: 'Hello').map(lambda a: a[2])\
        .filter(lambda b: len(b) == 2)\
        == Try('l', False)


# Generated at 2022-06-14 03:53:03.504756
# Unit test for method on_success of class Try

# Generated at 2022-06-14 03:53:11.982890
# Unit test for method map of class Try
def test_Try_map():
    """
    Unit test for method map of class Try

    :returns: True when test is success, False when test is fail
    :rtype: Boolean
    """
    def add3(x: int) -> int:
        return x + 3

    def add4(x: int) -> int:
        return x + 4

    def add5(x: int) -> int:
        return x + 5

    m = Try.of(add3, 3)
    m_to_map = m.map(add4).map(add5)
    n = Try.of(add3, 3)
    n_to_map = n.map(add4).map(add5)
    o = Try.of(add3, 4)
    o_to_map = o.map(add4).map(add5)


# Generated at 2022-06-14 03:53:24.105777
# Unit test for method bind of class Try
def test_Try_bind():
    # We have function for take a square of number without raise exception when number is negative.
    def safe_square(number):
        if number < 0:
            return number * number
        raise Exception('number {} is not negative'.format(number))

    # We want to return 0 when function raise exception, othercase return square with negative_square function
    def bind_negative_square(number):
        def negative_square(a):
            return a
        return Try.of(negative_square, number).on_fail(lambda _: 0)

    # We create Try on function call.
    square = Try.of(safe_square, -2)

    # square is successfully, bind_negative_square return result of called of negative_square function.
    assert square.bind(bind_negative_square) == Try(4, True)

    # negative_square raises exception

# Generated at 2022-06-14 03:53:30.279594
# Unit test for method bind of class Try
def test_Try_bind():
    assert Try.of(lambda: None, 1).bind(lambda x: Try.of(lambda: None, x)) == Try(None, True)
    assert Try.of(lambda: 1/0, 1).bind(lambda x: Try.of(lambda: None, x)) == Try(ZeroDivisionError, False)


# Generated at 2022-06-14 03:53:35.630462
# Unit test for method filter of class Try
def test_Try_filter():
    x = Try(1, False)
    assert x.filter(lambda x: x == 1) == Try(1, False)
    x = Try(1, True)
    assert x.filter(lambda x: x == 2) == Try(1, False)
    assert x.filter(lambda x: x == 1) == Try(1, True)



# Generated at 2022-06-14 03:53:38.618738
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    assert_equal(Try(None, False).on_fail(lambda _: None), Try(None, False))
    assert_equal(Try(11, True).on_fail(lambda _: None), Try(11, True))


# Generated at 2022-06-14 03:53:42.902317
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    Monad = Try
    assert Monad(5, True) == Monad(5, True)
    assert Monad(5, False) != Monad(5, True)
    assert Monad(None, True) == Monad(None, True)
    assert Monad(5, True) != Monad(None, True)
    assert Monad(None, True) != Monad(5, True)
