

# Generated at 2022-06-12 22:41:18.202646
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    calls = []

    @retry_with_delays_and_condition(
        backoff_iterator=generate_jittered_backoff(retries=2),
        should_retry_error=lambda e: e.value == "Error to be retried",
    )
    def function_that_raises():
        calls.append(1)
        if len(calls) < 2:
            exception = Exception("Error to be retried")
            exception.value = "Error to be retried"
            raise exception
        else:
            return "Success"

    assert function_that_raises() == "Success"
    assert len(calls) == 2

# Generated at 2022-06-12 22:41:23.996312
# Unit test for function retry
def test_retry():
    # Test that retry returns the value on the first try
    @retry(retries=2, retry_pause=1)
    def test_function_success_first_try(*args, **kwargs):
        return True

    assert test_function_success_first_try() is True

    # Test that retry retries and fails
    @retry(retries=3, retry_pause=1)
    def test_function_success_second_try(*args, **kwargs):
        test_function_success_second_try.counter += 1
        if test_function_success_second_try.counter > 1:
            return True
        else:
            return False

    test_function_success_second_try.counter = 0

# Generated at 2022-06-12 22:41:34.475162
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():

    # Test that the decorator works on a function with no exceptions.
    @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff())
    def example_function_1():
        return "success"
    assert example_function_1() == "success"

    # Test that the decorator works on a function that raises errors.
    @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff())
    def example_function_2():
        raise ValueError("Triggered exception.")
        return "success"
    try:
        example_function_2()
    except ValueError:
        pass
    except:
        raise AssertionError("Expected ValueError to be raised.")

    # Test should_retry_error function

# Generated at 2022-06-12 22:41:40.211820
# Unit test for function retry
def test_retry():
    @retry(retries=3)
    def test3(a, b, c=None):
        global test0_calls
        test0_calls += 1
        if c:
            return a + b + c
        else:
            raise Exception()

    global test0_calls
    test0_calls = 0
    assert test3(1, 2) == 6
    assert test0_calls == 3
    test0_calls = 0
    assert test3(1, 2, 4) == 7
    assert test0_calls == 1


# Generated at 2022-06-12 22:41:48.349180
# Unit test for function retry
def test_retry():
    class TestException(Exception):
        pass

    # Test decorator
    @retry(3, 2)
    def test_decorator():
        print("test")
        return True

    # Test retry
    @retry(1, 0.001)
    def test_retry_raise():
        raise TestException('test')

    @retry(2, 0.001)
    def test_retry_false():
        return False

    @retry(20, 0.001)
    def test_retry_true():
        return True

    assert test_decorator()
    try:
        test_retry_raise()
        assert False
    except TestException:
        assert True
    assert not test_retry_false()
    assert test_retry_true()

# Generated at 2022-06-12 22:41:53.222782
# Unit test for function rate_limit
def test_rate_limit():
    rate = 100
    rate_limit = 10
    minrate = 10

    @rate_limit(rate, rate_limit)
    def _test(x):
        print(x)

    start = time.time()
    for x in range(rate):
        _test(x)
    end = time.time()
    actual_duration = end - start
    assert actual_duration > rate_limit

# Generated at 2022-06-12 22:42:02.809708
# Unit test for function rate_limit
def test_rate_limit():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-12 22:42:07.140782
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    def test_function():
        return True

    new_function = retry_with_delays_and_condition(generate_jittered_backoff())(test_function)
    assert new_function() is True


# Generated at 2022-06-12 22:42:10.549839
# Unit test for function generate_jittered_backoff
def test_generate_jittered_backoff():
    backoff_iterator = generate_jittered_backoff()
    delays = list(backoff_iterator)

    assert delays == [0, 0, 1, 3, 7, 15, 31, 63, 63, 63]

# Generated at 2022-06-12 22:42:18.678998
# Unit test for function retry
def test_retry():
    import doctest
    import os
    import sys
    import tempfile

    @retry(retries=2)
    def test_function(return_value):
        if not return_value:
            raise Exception("Foo Error")
        return return_value

    # Test success
    res = test_function(True)
    assert res is True

    # Test retry
    retry_count = [0]
    @retry(retries=2)
    def test_function_retry(return_value):
        retry_count[0] += 1
        if not return_value:
            raise Exception("Foo Error")
        return return_value
    res = test_function_retry(False)
    assert res is None
    assert retry_count[0] == 2

    # Test retry limit
    ret

# Generated at 2022-06-12 22:42:35.187509
# Unit test for function retry
def test_retry():
    # f1 is decorated with functools.wraps(f)
    # this make f1.__doc__ be 'Do not retry'

    @retry(2, 2)
    def f1(i):
        print('f1')
        return i

    @retry(1, 1)
    def f2(i):
        print('f2')
        return i

    @retry(2, 2)
    def f3(i):
        print('f3')
        raise Exception()

    @retry(2, 2)
    def f4(i, j):
        print('f4')
        return i + j

    # f1(i) should not retry
    assert f1(3) == 3

    # f2(i) should retry 1 time

# Generated at 2022-06-12 22:42:37.776673
# Unit test for function retry
def test_retry():
    # Set up a test function
    def test_function():
        print("Running test function")
        return False

    # Retry 3 times with a 1 second delay
    retried_function = retry(retries=3, retry_pause=1)(test_function)
    retried_function()


if __name__ == '__main__':
    test_retry()

# Generated at 2022-06-12 22:42:48.363551
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    import unittest

    class FunctionReturningNumber(object):
        def __init__(self, return_value, raises=Exception):
            self.return_value = return_value
            self.raises = raises
            self.num_calls = 0

        def __call__(self, *args, **kwargs):
            self.num_calls += 1
            if self.num_calls > 1:
                raise self.raises("foo")
            else:
                return self.return_value

    @retry_with_delays_and_condition([0, 0, 0, 0], retry_never)
    def decorated_function():
        return FunctionReturningNumber(1)()


# Generated at 2022-06-12 22:42:56.608569
# Unit test for function rate_limit
def test_rate_limit():
    limit = 5
    window = 10
    min_rate = float(window) / float(limit)
    import time
    count = 1
    last = time.time()

    @rate_limit(rate=limit, rate_limit=window)
    def f():
        global count
        global last
        count += 1
        print('f called %d times' % count)
        print('time elapsed: %f' % (time.time()-last))
        last = time.time()

    while True:
        f()


if __name__ == '__main__':
    test_rate_limit()

# Generated at 2022-06-12 22:43:01.044898
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(rate=3, rate_limit=10)
    def test_func():
        print("This function will be called 3 times in 10 seconds")
    test_func()
    test_func()
    test_func()
    test_func()
    test_func()
    test_func()
    test_func()
    test_func()
    test_func()
    test_func()



# Generated at 2022-06-12 22:43:10.547401
# Unit test for function retry
def test_retry():
    """Test the retry function.

    Note that the test is not very exhaustive and is merely meant to ensure that the function
    behaves as intended (gracefully) and does not fail with a SyntaxError or similar.
    """
    # Imports in test function, to not pollute the global scope.
    from mock import Mock

    def method_with_retry_and_error(arg1, arg2, **_):
        """A function to test retry with"""
        return Mock()

    # Method should be retried with no exception, ensuring no infinite loop.
    success_method = Mock(side_effect=[Exception("a"), Exception("b"), 5])
    assert 3 == success_method.call_count
    assert 5 == retry(retries=3, retry_pause=1)(success_method)()

    # Method should fail with exception "

# Generated at 2022-06-12 22:43:12.760574
# Unit test for function rate_limit
def test_rate_limit():
    """ Only run this if we're actually testing"""
    if 'python-nose' in sys.modules.keys():
        print("******** TESTING rate_limit ********")
        @rate_limit(rate=3,rate_limit=30)
        def test():
            print ("I was called")
            return True
        test()



# Generated at 2022-06-12 22:43:14.415249
# Unit test for function rate_limit
def test_rate_limit():
    import doctest
    doctest.testmod()



# Generated at 2022-06-12 22:43:22.044171
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    """Unit test for retry_with_delays_and_condition"""
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    backoff_iterator = iter([0,1,3,5])
    should_retry_error = lambda e: isinstance(e, Exception)

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error)
    def raises_exceptions(*args, **kwargs):
        raise Exception

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error)
    def returns_false_result(*args, **kwargs):
        return False


# Generated at 2022-06-12 22:43:32.475410
# Unit test for function rate_limit
def test_rate_limit():
    import time
    import math

    @rate_limit(rate=10, rate_limit=10)
    def limited(arg):
        return arg

    beg = time.time()
    for x in range(0, 9):
        result = limited(x)
        assert result == x

    for x in range(10, 19):
        result = limited(x)
        assert result == x

    # make sure more than a second has passed
    assert time.time() - beg > 1.0

    @rate_limit()
    def limited(arg):
        return arg

    beg = time.time()
    for x in range(0, 9):
        result = limited(x)
        assert result == x

    assert math.isclose(time.time() - beg, 0, abs_tol=0.01)


# Unit test

# Generated at 2022-06-12 22:43:53.394945
# Unit test for function retry

# Generated at 2022-06-12 22:44:05.224272
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    from nose.tools import assert_equal

    @retry_with_delays_and_condition(generate_jittered_backoff(retries=2, delay_base=1, delay_threshold=60))
    def constant_failure():
        return False

    @retry_with_delays_and_condition(generate_jittered_backoff(retries=3, delay_base=1, delay_threshold=60))
    def never_failure():
        return True

    @retry_with_delays_and_condition(generate_jittered_backoff(retries=2, delay_base=1, delay_threshold=60))
    def error():
        raise Exception("Failed to call")


# Generated at 2022-06-12 22:44:14.295567
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    from unittest import TestCase

    class TestRetryWithDelaysAndCondition(TestCase):
        def test_retry_never(self):
            def test_function():
                return True

            retry_never = retry_with_delays_and_condition(backoff_iterator=[], should_retry_error=retry_never)
            retry_never_function = retry_never(test_function)
            self.assertTrue(retry_never_function())

        def test_full_jitter(self):
            def test_function():
                print("test_function")
                return True

            full_jitter_retry_function = retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff())(test_function)

# Generated at 2022-06-12 22:44:23.635427
# Unit test for function retry
def test_retry():
    """Unit test for retry decorator.

    This tests the decorator directly with a simple function.
    """
    # The counts of calls to the wrapped function
    successful_call_count = 0
    retry_call_count = 0
    retry_fail_count = 0

    MAX_RETRIES = 10
    RETRY_SUCCESS_COUNT = 4
    RETRY_FAIL_FIRST_COUNT = 6

    def should_retry_error(e):
        """Decide whether to retry or not based on the raised exception.

        In this case, we want to retry based on the index of the call.
        """
        nonlocal retry_call_count, retry_fail_count
        retry_call_count += 1

# Generated at 2022-06-12 22:44:34.499466
# Unit test for function rate_limit
def test_rate_limit():
    """Test for rate_limit"""
    import unittest

    class TestRateLimit(unittest.TestCase):
        """Test for rate_limit"""

        def setUp(self):
            """Create a test function to use with the decorator"""
            self.called = 0
            self.time_spent = 0

            def test_function():
                """a test function that waits 0.1 second"""
                t1 = time.time()
                time.sleep(0.1)
                self.time_spent = time.time() - t1
                self.called += 1
            self.test_function = test_function

        def test_basic_rate_limit(self):
            """test a rate limit of 10 calls per second"""
            wrapped = rate_limit(rate=10, rate_limit=1)(self.test_function)

# Generated at 2022-06-12 22:44:41.210603
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    @retry_with_delays_and_condition(generate_jittered_backoff())
    def always_fails_and_raises_exception(fail_count):
        if fail_count <= 0:
            raise Exception("Failed once, retrying 20 times...")
        fail_count -= 1
        return always_fails_and_raises_exception(fail_count)

    with pytest.raises(Exception) as excinfo:
        always_fails_and_raises_exception(20)

    message = str(excinfo.value)
    assert "Failed once, retrying 20 times..." in message

# Generated at 2022-06-12 22:44:51.634752
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    """Unit test for function retry_with_delays_and_condition."""

    RETRIES_WITH_PAUSE = [1, 3, 5]
    RETRIES_WITHOUT_PAUSE = [1, 0, 0]
    RETRIES_ZERO_ITEMS = [0, 0, 0]

    def do_retry(delay):
        # print "delay={}".format(delay)
        if not delay:
            return True
        return False

    @retry_with_delays_and_condition(RETRIES_WITH_PAUSE, do_retry)
    def test_retry_with_delays():
        """Unit test for retries with delays."""
        # print "retry: {}".format(test_retry_with_delays.retries)

# Generated at 2022-06-12 22:45:00.072147
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    def error(msg):
        raise RuntimeError(msg)

    def raise_error():
        error("Error")

    @retry_with_delays_and_condition([], retry_never)
    def test_partial_retry_never():
        raise_error()

    @retry_with_delays_and_condition([], lambda e: e.args[0] == "Error")
    def test_partial_retry_with_lambda():
        raise_error()

    @retry_with_delays_and_condition([], retry_never)
    def test_partial_retry_with_retry_never_callable():
        raise_error()


# Generated at 2022-06-12 22:45:06.744880
# Unit test for function retry
def test_retry():
    @retry(retries=5, retry_pause=1)
    def retry_test(a=None):
        if a:
            return a
        raise Exception("test")
    assert retry_test() is None
    assert retry_test() is None
    assert retry_test(True) is True
    assert retry_test(True) is True


# Generated at 2022-06-12 22:45:12.960807
# Unit test for function rate_limit
def test_rate_limit():
    class rl_test:
        def __init__(self):
            self.last = 0.0

        @rate_limit(rate=4, rate_limit=3)
        def ratelimited(self):
            if sys.version_info >= (3, 8):
                real_time = time.process_time
            else:
                real_time = time.clock
            elapsed = real_time() - self.last
            self.last = real_time()
            return elapsed

    test = rl_test()
    assert test.ratelimited() >= 0.75
    assert test.ratelimited() < 0.05
    assert test.ratelimited() < 0.05
    assert test.ratelimited() < 0.05
    assert test.ratelimited() >= 0.75


# Generated at 2022-06-12 22:45:45.192459
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    import unittest

    class CustomException(Exception):
        pass

    class TestRetry(unittest.TestCase):
        def test_function_fails_at_first_attempt(self):
            """This test gives the function to be decorated one chance, but the function will fail at the first attempt.
            It should not retry, but it should throw the exception."""
            @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff())
            def test_function_fails_at_first_attempt():
                raise CustomException("Failed")

            # Assert that the function call succeeded (no exception)
            self.assertRaises(CustomException, test_function_fails_at_first_attempt)


# Generated at 2022-06-12 22:45:55.007129
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    import unittest

    def retry_on_typeerror(exception):
        return isinstance(exception, TypeError)

    def retry_with_typeerror_only_once(exception):
        return isinstance(exception, TypeError) and exception.args[0] == "should retry only once"

    def retry_on_every_typeerror(exception):
        return isinstance(exception, TypeError) and exception.args[0] == "always retry"

    def raise_typeerror_once():
        raise TypeError("should retry only once")

    def raise_typeerror_twice():
        raise TypeError("always retry")


# Generated at 2022-06-12 22:46:03.469034
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    @retry_with_delays_and_condition(generate_jittered_backoff(retries=10, delay_base=1, delay_threshold=2))
    def test_function():
        return 0

    assert test_function() == 0

    @retry_with_delays_and_condition(generate_jittered_backoff(retries=10, delay_base=1, delay_threshold=2), should_retry_error=retry_never)
    def test_function():
        raise Exception()

    raised = False
    try:
        test_function()
    except:
        raised = True

    assert raised == True

# Generated at 2022-06-12 22:46:12.926337
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(rate=20, rate_limit=10)
    def f():
        pass

    if sys.version_info >= (3, 8):
        real_time = time.process_time
    else:
        real_time = time.clock

    # no rate limit, should finish immediately
    t1 = real_time()
    f()
    t2 = real_time()
    assert(t2 - t1 < 0.01)

    # low rate, should finish in 0.5 seconds
    t1 = real_time()
    f()
    t2 = real_time()
    assert(t2 - t1 > 0.45 and t2 - t1 < 0.55)

    # consider a delay in the second call
    time.sleep(0.1)
    t1 = real_time()
    f

# Generated at 2022-06-12 22:46:21.044762
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    global was_function_called  # This global is used for the unit tests to keep track of how many times the function was actually called.
    was_function_called = 0

    @retry_with_delays_and_condition(generate_jittered_backoff(10), should_retry_error=retry_never)
    def test_function(func_arg):
        global was_function_called
        was_function_called += 1
        return func_arg

    assert test_function(1) == 1
    assert was_function_called == 1

    assert test_function(2) == 2
    assert was_function_called == 2

    def should_retry(exception):
        return isinstance(exception, IOError)

    num_run_retryable_function_calls = 0


# Generated at 2022-06-12 22:46:24.973143
# Unit test for function rate_limit
def test_rate_limit():

    # object func will be decorated
    def func(i, **kwargs):
        print(i)
        return i

    # let's decorate func
    func = rate_limit(rate=10, rate_limit=1000)(func)

    # run poller
    for i in range(20):
        func(i)

# Generated at 2022-06-12 22:46:33.664991
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    TEST_ATTEMPTS = 3
    TEST_DELAY = 3.0
    TEST_DELAY_THRESHOLD = 6.0

    def test_function_with_error(attempt):
        if attempt < TEST_ATTEMPTS - 1:
            raise Exception('test')
        else:
            return True

    backoff_iterator = generate_jittered_backoff(TEST_ATTEMPTS, TEST_DELAY, TEST_DELAY_THRESHOLD)
    retryable_function = retry_with_delays_and_condition(backoff_iterator)(test_function_with_error)

    # Test 3 attempts: 1st 2 attempts should fail, 3rd attempt should succeed
    assert retryable_function(0)
    assert retryable_function(1)

# Generated at 2022-06-12 22:46:38.237715
# Unit test for function retry
def test_retry():
    @retry(retries=5)
    def retryable_function():
        if retryable_function.retries_left > 0:
            retryable_function.retries_left -= 1
            return False
        return True

    retryable_function.retries_left = 3
    retryable_function()
    assert retryable_function.retries_left == 0



# Generated at 2022-06-12 22:46:45.411429
# Unit test for function retry
def test_retry():
    retry_test = False
    if retry_test:
        # Attempt to import the required modules
        try:
            from ansible.module_utils.basic import AnsibleModule
            HAS_MODULES = True
        except ImportError:
            HAS_MODULES = False

        @retry(retries=3, retry_pause=1)
        def retry_test_func(arg):
            if retry_test:
                print('arg:')
                print(arg)
            return arg

        @retry(retries=3, retry_pause=1)
        def retry_error_func():
            raise Exception('test error')

        print(retry_test_func('test'))
        print()


# Generated at 2022-06-12 22:46:56.481944
# Unit test for function retry
def test_retry():
    """Test retry"""
    expect = dict(
        success=0,
        retries=3,
        rets=dict(
            result='Success',
            result2='Success',
            result3='Success',
            result4='Success',
        ),
        err=None,
    )

    # check retry on all errors
    @retry(retries=expect['retries'])
    def all_retry(arg=0):
        """retry on all errors"""
        expect['success'] += 1
        if arg < expect['retries']:
            raise Exception(arg)
        return 'Success'
    expect['rets']['result'] = all_retry()

    # check retry on certain error

# Generated at 2022-06-12 22:47:50.488883
# Unit test for function retry
def test_retry():
    retries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    @retry_with_delays_and_condition(generate_jittered_backoff(delay_base=1))
    def retry_never_function():
        if retries:
            return len(retries)
        else:
            raise Exception("Failure")

    assert(retries == [])

    retries.append(1)

    @retry_with_delays_and_condition(generate_jittered_backoff(delay_base=1))
    def retry_until_exhausted_function():
        if retries:
            retries.pop()
        else:
            raise Exception("Failure")

    assert(retries == [])


# Generated at 2022-06-12 22:47:58.702418
# Unit test for function retry
def test_retry():
    """
    Unit Test for function retry decorator
    """
    # Test retry without limit
    @retry()
    def get_zero():
        """
        get zero.
        """
        return 0

    assert get_zero() == 0

    # Test retry with limit
    @retry(retries=5)
    def get_one():
        """
        get one.
        """
        return 1

    assert get_one() == 1

    # Test retry with limit
    @retry(retries=5)
    def get_random():
        """
        get random.
        """
        return random.randint(0, 10)

    assert get_random() != 0


# Generated at 2022-06-12 22:48:04.058072
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    def function(*args, **args_kw):
        return args, args_kw

    arg_list = ['foo', 'bar']
    arg_dict = {'foo': 'foo', 'bar': 'bar'}

    for arg in arg_list:
        for kw in arg_dict:
            for backoff in generate_jittered_backoff():
                retried_function = retry_with_delays_and_condition(generate_jittered_backoff(retries=1))(function)
                assert retried_function(arg, kw=kw) == ((arg,), {'kw':kw})



# Generated at 2022-06-12 22:48:11.276196
# Unit test for function retry
def test_retry():
    class TestException(Exception):
        pass

    @retry(retries=10, retry_pause=0.2)
    def raise_exception():
        raise TestException("Retry test")

    assert raise_exception() is None

    def retry_never(exception):
        return False

    retry_count = 0

    @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff(retries=3), should_retry_error=retry_never)
    def raise_exception_with_retry():
        nonlocal retry_count
        retry_count += 1
        raise TestException("Retry test")

    assert raise_exception_with_retry() is None
    assert retry_count == 1


# Generated at 2022-06-12 22:48:16.403175
# Unit test for function retry
def test_retry():

    import doctest
    src = """
    >>> @retry(retries=5, retry_pause=3)
    ... def never_true():
    ...     return False

    >>> never_true()
    Traceback (most recent call last):
    Exception: Retry limit exceeded: 5

    >>> @retry(retries=5, retry_pause=3)
    ... def always_true():
    ...     return True

    >>> always_true()
    True
    """

    (failed, total) = doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS, name='retry')
    if failed == 0:
        print('%s' % __file__)
        print('Doctest: result of testing documentation: %d failures out of %d tests.' % (failed, total))
   

# Generated at 2022-06-12 22:48:22.828626
# Unit test for function retry
def test_retry():
    """
    Executes a function that throws an exception the first time,
    but not the second time.
    """
    @retry(retries=2, retry_pause=1)
    def failing_function(fail_first_time=False):
        if fail_first_time:
            raise Exception('Failing')
        return True

    assert failing_function(fail_first_time=True) is True



# Generated at 2022-06-12 22:48:30.193859
# Unit test for function retry
def test_retry():
    # Count calls
    counter = [0]
    # Error on 4th attempt
    def failthrice(x):
        counter[0] += 1
        if counter[0] == 4:
            raise Exception('failed')
        return x
    # Retry on exceptions
    rfailthrice = retry(retries=10)(failthrice)
    # Run it
    output = rfailthrice(1)
    assert counter[0] == 4
    assert output == 1
    # Retries exhausted
    with pytest.raises(Exception):
        _ = retry(retries=3)(failthrice)(1)
    # Don't retry
    with pytest.raises(Exception):
        _ = retry(retries=0)(failthrice)(1)



# Generated at 2022-06-12 22:48:38.495944
# Unit test for function rate_limit
def test_rate_limit():
    # Call initialization
    init_time = time.time()
    time.sleep(1)

    @rate_limit(rate=3, rate_limit=5)
    def run_test():
        # In any case we should wait at least one second
        if time.time() <= init_time + 1:
            assert False, "rate limit did not wait at least 1 second"
        # If the limit is exceeded we should wait at least 2 seconds
        if time.time() <= init_time + 3:
            assert False, "rate limit did not wait at least 2 seconds"
        # If the limit is exceeded again, we should wait at least 3 seconds
        if time.time() <= init_time + 6:
            assert False, "rate limit did not wait at least 3 seconds"

    run_test()
    run_test()
    run_test()

# Generated at 2022-06-12 22:48:40.575161
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(1000, 3600)
    def rate_limited():
        print('rate_limited')
    rate_limited()

# Unit Test for function retry

# Generated at 2022-06-12 22:48:42.952525
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(rate=5, rate_limit=1)
    def test_function(*args, **kwargs):
        return True
    assert test_function() is True

# Generated at 2022-06-12 22:50:37.460462
# Unit test for function retry
def test_retry():
    import unittest

    class TestRetry(unittest.TestCase):
        def test_retry_normal(self):
            @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff())
            def divide(x, y):
                return x / y

            # No exception
            self.assertEqual(divide(10, 2), 5)
            self.assertEqual(divide(2, 0), 2)

        def test_retry_with_exception(self):
            @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff())
            def divide(x, y):
                if y == 0:
                    raise ValueError()

                return x / y

            # No exception

# Generated at 2022-06-12 22:50:40.238896
# Unit test for function retry
def test_retry():
    @retry(retries=10)
    def test():
        print('run test')
        return random.randint(0, 1)

    try:
        test()
    except Exception:
        print('Retry limit exceeded')


# Generated at 2022-06-12 22:50:45.934329
# Unit test for function retry
def test_retry():
    class TestError(Exception):
        pass

    def err_func(count, message):
        if count > 0:
            count -= 1
            raise TestError(message)
        return True

    err_func = retry(retries=3, retry_pause=0)(err_func)
    try:
        err_func(3, 'test_retry')
    except Exception as e:
        raise
    assert err_func(0, 'test_retry') is True



# Generated at 2022-06-12 22:50:47.601289
# Unit test for function retry
def test_retry():
    @retry_with_delays_and_condition(iter((0, 0)))
    def f():
        return True

    assert f()

# Generated at 2022-06-12 22:50:50.754063
# Unit test for function retry
def test_retry():
    @retry(retries=3, retry_pause=0.001)
    def raise_error():
        time.sleep(0.01)
        raise Exception("Boom")

    try:
        raise_error()
    except Exception:
        pass



# Generated at 2022-06-12 22:50:58.848472
# Unit test for function rate_limit
def test_rate_limit():
    """tests for rate_limit"""
    from ansible.module_utils.basic import AnsibleModule

    argspec = rate_limit_argument_spec(rate=3, rate_limit=4)
    module = AnsibleModule(argument_spec=argspec, supports_check_mode=True)

    # need to use check_mode=False to get the decorated function to run
    module.params['CHECKMODE'] = False
    mock = module.params['CHECKMODE']

    if not mock:
        @rate_limit(rate=module.params['rate'], rate_limit=module.params['rate_limit'])
        def slow_function():
            print('do something slow')
            return True

    slow_function()


# Generated at 2022-06-12 22:51:03.185165
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(rate=2, rate_limit=2)
    def my_func(value, factor=1):
        return value * factor

    assert my_func(3, factor=10) == 30
    assert my_func(3, factor=10) == 30
    try:
        my_func(3, factor=10)
        assert False
    except Exception as e:
        assert e.message == 'Retry limit exceeded: 2'

