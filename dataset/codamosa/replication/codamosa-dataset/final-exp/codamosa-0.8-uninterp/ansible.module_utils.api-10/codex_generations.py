

# Generated at 2022-06-12 22:41:19.718414
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    backoff_iterator = [1,2,3]

    class TestException(Exception):
        pass

    class TestException2(Exception):
        pass

    @retry_with_delays_and_condition(backoff_iterator)
    def no_errors_test_function(test_arg):
        return test_arg

    @retry_with_delays_and_condition(backoff_iterator)
    def errors_test_function(test_arg):
        if test_arg == "first_error":
            raise TestException("first_error")
        elif test_arg == "second_error":
            raise TestException2("second_error")

    assert(no_errors_test_function("first_error") == "first_error")

# Generated at 2022-06-12 22:41:31.739942
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    backoff_iterator = generate_jittered_backoff(3, 1, 4)
    def function(throws_an_error):
        if throws_an_error:
            raise Exception('throws an error')
        else:
            return True

    func_no_error = retry_with_delays_and_condition(backoff_iterator, should_retry_error=retry_never)(function)
    assert func_no_error(False) == True

    func_throws_an_error = retry_with_delays_and_condition(backoff_iterator, should_retry_error=lambda e: e.args[0] == 'throws an error')(function)
    assert func_throws_an_error(True) == True

test_retry_with_delays_and_condition()

# Generated at 2022-06-12 22:41:40.126535
# Unit test for function rate_limit
def test_rate_limit():
    """Test rate_limit"""
    import time
    one_second = 1
    zero = 0

    rate_limit_one = rate_limit(rate=2, rate_limit=one_second)

    # The logic of rate_limit_one: sleep if needed such that
    #   time.time() - last[0] >= 0.5
    #
    # delayed_one_second() will force one second to elapse after it receives
    # control.  So, because of the logic in rate_limit_one, if delayed_one_second
    # is called twice (without additional rate limiting) with an initial
    # time.time() of zero, then the second call should be delayed by at least 0.5
    # seconds.

    start_time = zero


# Generated at 2022-06-12 22:41:48.543792
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    # Normal success case with single call
    @retry_with_delays_and_condition(generate_jittered_backoff(retries=0))
    def run_fewer_than_max_times(call_number=0):
        return call_number

    assert run_fewer_than_max_times() == 0

    # Normal success case with three calls
    @retry_with_delays_and_condition(generate_jittered_backoff(retries=2))
    def run_fewer_than_max_times(call_number=0):
        return call_number

    assert run_fewer_than_max_times() == 2

    # error on final attempt

# Generated at 2022-06-12 22:41:49.106698
# Unit test for function retry
def test_retry():
    pass

# Generated at 2022-06-12 22:41:51.168901
# Unit test for function retry
def test_retry():
    @retry(retries=2)
    def test_f():
        return False

    retval = test_f()
    assert retval is False, "Function didn't return expected value"


# Generated at 2022-06-12 22:41:59.526155
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    from nose.tools import assert_equal
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(FakeModule, self).__init__(*args, **kwargs)
            self.exit_json = self.exit_args = self.fail_json = self.fail_args = None

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

        def fail_json(self, **kwargs):
            self.fail_args = kwargs

    @retry_with_delays_and_condition(backoff_iterator=[0])
    def func_a():
        """A wrapper function with no args"""
        return "success"


# Generated at 2022-06-12 22:42:07.084496
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    def not_always_failing(random_variable):
        if random_variable:
            return 'success!'
        raise Exception('fail.')

    # Never retry
    retry_fn = retry_with_delays_and_condition(generate_jittered_backoff())

    @retry_fn
    def always_failing(random_variable):
        return not_always_failing(random_variable)

    assert always_failing(1) == 'success!'
    try:
        always_failing(0)
    except Exception:
        pass
    else:
        raise AssertionError('Exception should have been raised')

    # Retry if exception is instance of ValueError

# Generated at 2022-06-12 22:42:10.881961
# Unit test for function retry
def test_retry():
    @retry(retries=3, retry_pause=1)
    def foo():
        return None
    try:
        foo()
    except Exception as e:
        assert('Retry limit exceeded: 3' in str(e))

# Generated at 2022-06-12 22:42:15.351839
# Unit test for function retry
def test_retry():
    retry_count = [0]
    # This function will always fail the first time, but then succeed the second time
    @retry(retries=2)
    def retry_test():
        retry_count[0] += 1
        if retry_count[0] < 3:
            raise Exception("Fail")
        return True
    assert retry_test()


# Generated at 2022-06-12 22:42:26.295029
# Unit test for function retry
def test_retry():
    tries = 0
    max_tries = 3

    @retry(retries=max_tries, retry_pause=0)
    def test():
        global tries
        tries += 1
        return False

    test()

    assert tries == max_tries, "expected %s tries but got %s" % (max_tries, tries)


# Generated at 2022-06-12 22:42:36.065906
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    import unittest

    def assertRaisesRegex(exception):
        def fn(function, *args):
            with unittest.TestCase():
                with self.assertRaises(exception):
                    function(*args)
        return fn

    class TestRetry(unittest.TestCase):
        def test_retry_never(self):
            # This test is to show how to use the function. It is not a regression/unit test.

            @retry_with_delays_and_condition(generate_jittered_backoff(), retry_never)
            def raise_exception():
                raise Exception('Hello')

            with assertRaisesRegex(Exception):
                raise_exception()


# Generated at 2022-06-12 22:42:39.828032
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(rate=2, rate_limit=2)
    def test_function(arg1, arg2=None, arg3=None):
        return arg1

    assert test_function('my_arg') == 'my_arg'

# Generated at 2022-06-12 22:42:51.148356
# Unit test for function retry
def test_retry():
    # noinspection PyUnusedLocal
    @retry(retries=3)
    def test(succeed=True):
        if succeed:
            return True
        else:
            return False

    # noinspection PyUnusedLocal
    @retry(retries=3)
    def test_except(succeed=True):
        if succeed:
            return True
        else:
            raise Exception("failed")

    test()
    test(succeed=False)
    test(succeed=False)
    test(succeed=False)
    try:
        test(succeed=False)
    except Exception:
        pass
    else:
        raise AssertionError("didn't raise exception, retries exceeded")

    test_except()

# Generated at 2022-06-12 22:43:00.348907
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    # pylint: disable=too-many-locals
    @retry_with_delays_and_condition(generate_jittered_backoff())
    def test_function(a, b):
        test_function.counter += 1
        if test_function.counter <= test_function.max_iteration:
            raise Exception(f'Test exception number {test_function.counter}')
        return a + b

    test_function.counter = 0
    test_function.max_iteration = 3

    result = test_function(2, 3)
    assert result == 5
    assert test_function.counter == test_function.max_iteration + 1

    try:
        test_function(4, 5)
    except Exception:
        assert test_function.counter == test_function.max_iteration + 1

# Generated at 2022-06-12 22:43:06.753531
# Unit test for function retry
def test_retry():
    @retry(retries=3, retry_pause=1)
    def test_func():
        return True
    assert test_func()
    counter = [0]

    @retry(retries=3, retry_pause=1)
    def test_func_fail():
        counter[0] += 1
        return False
    assert not test_func_fail()
    assert counter[0] == 3



# Generated at 2022-06-12 22:43:17.823739
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    import unittest
    import mock
    from ansible.module_utils.basic import AnsibleModule

    class RetryWithDelaysConditionTest(unittest.TestCase):
        """
        This class tests the `retry_with_delays_and_condition` decorator.
        """

        def setUp(self):
            self.return_code = 0
            self.function_call_count = 0
            self.ansible_module = AnsibleModule(
                argument_spec=dict()
            )

        def function_to_retry(self):
            self.function_call_count += 1
            if self.function_call_count > 1:
                self.ansible_module.exit_json(changed=True)

            self.ansible_module.fail_json(failed=True)


# Generated at 2022-06-12 22:43:23.290796
# Unit test for function retry
def test_retry():
    """
    Unit test for function retry.
    """
    attempts = 0

    @retry(retries=3, retry_pause=0)
    def test_function():
        global attempts
        attempts += 1
        raise Exception('test')

    try:
        test_function()
    except Exception:
        pass

    assert attempts == 3



# Generated at 2022-06-12 22:43:32.951067
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    @retry_with_delays_and_condition(generate_jittered_backoff(retries=5, delay_base=1, delay_threshold=1), retry_never)
    def fail_every_time(fail_with_exception=False):
        if fail_with_exception:
            raise Exception("Hard failure")
        return False

    @retry_with_delays_and_condition(generate_jittered_backoff(retries=5, delay_base=1, delay_threshold=1), retry_never)
    def fail_some_times(fail_with_exception=False):
        if fail_with_exception:
            raise Exception("Hard failure")
        return True

    assert fail_every_time(fail_with_exception=False) is False
    assert fail_every

# Generated at 2022-06-12 22:43:44.576681
# Unit test for function retry
def test_retry():
    """Run some tests on the retry decorator"""

    # Fail the first three times before succeeding
    @retry(retries=5, retry_pause=1)
    def test_function_fail_3_times():
        test_function_fail_3_times.attempts += 1
        if test_function_fail_3_times.attempts < 4:
            raise Exception("foo")
        return "success"
    test_function_fail_3_times.attempts = 0

    # This should fail even with retries
    @retry(retries=5, retry_pause=1)
    def test_function_fail():
        raise Exception("foo")
        return "success"

    # This should not fail

# Generated at 2022-06-12 22:44:05.521425
# Unit test for function rate_limit
def test_rate_limit():
    rate_limit_count = 0
    last = [0]

    @rate_limit(rate=2, rate_limit=2)
    def rate_limited():
        nonlocal rate_limit_count
        rate_limit_count += 1
        if sys.version_info >= (3, 8):
            real_time = time.process_time
        else:
            real_time = time.clock
        elapsed = real_time() - last[0]
        last[0] = real_time()
        assert elapsed >= 1
        assert elapsed < 2.2

    for _ in range(0, 10):
        rate_limited()

    assert rate_limit_count == 10

# Generated at 2022-06-12 22:44:14.812869
# Unit test for function retry
def test_retry():
    # Test retry_with_delays_and_condition and generate_jittered_backoff
    @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff(retries=10, delay_base=1, delay_threshold=2))
    def failing_function(i):
        if i > 5:
            return True
        else:
            raise Exception("Failed")

    assert failing_function(0)

    @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff(retries=3, delay_base=1, delay_threshold=2))
    def failing_function(i):
        if i > 5:
            return True
        else:
            raise Exception("Failed")

    # Test we handle exception when retry

# Generated at 2022-06-12 22:44:24.006828
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    class AlwaysRetryError(Exception):
        pass

    class NeverRetryError(Exception):
        pass

    def should_retry_error(error):
        return not isinstance(error, NeverRetryError)

    def failing_function():
        raise AlwaysRetryError()

    def always_failing_function():
        raise NeverRetryError()

    function = failing_function

    retry_decorated = retry_with_delays_and_condition(generate_jittered_backoff())
    with pytest.raises(AlwaysRetryError):
        retry_decorated(function)()

    retry_decorated = retry_with_delays_and_condition(generate_jittered_backoff(), should_retry_error=should_retry_error)

# Generated at 2022-06-12 22:44:34.916871
# Unit test for function rate_limit
def test_rate_limit():
    from datetime import datetime

    rate_limit = 1
    rate_limit_window_secs = 5

    num_calls = 100
    start_time = datetime.now()

    @rate_limit(rate=rate_limit, rate_limit=rate_limit_window_secs)
    def call_print():
        print("Inside call_print")

    # do 100 calls, with rate limit of 1/sec and window of 5 sec,
    # we expect the total time to be 5 secs
    for i in range(num_calls):
        call_print()

    end_time = datetime.now()
    delta = end_time - start_time
    assert delta.seconds <= rate_limit_window_secs
    assert delta.seconds >= rate_limit_window_secs - 1


# Generated at 2022-06-12 22:44:42.535189
# Unit test for function retry
def test_retry():
    def run_test(retries, expected_retry_count):
        @retry(retries=retries)
        def fail_test(run_number):
            if run_number > 3:
                return True
            else:
                return False
        # Mock time.clock to increment from 0.0 to 1.0 in time.sleep(1)
        time.clock = lambda: time.clock.counter
        time.clock.counter = 0.0
        time.clock.ticks = 0.0
        time.sleep = lambda x: time.sleep.counter
        time.sleep.counter = 0.0
        retry_count = 0
        try:
            fail_test(retry_count)
        except:
            pass
        while time.clock.ticks < 3:
            retry_count += 1

# Generated at 2022-06-12 22:44:52.425130
# Unit test for function rate_limit
def test_rate_limit():
    time.sleep = lambda x: None
    time.time = lambda: 0.0
    rate_limit_decorator = rate_limit(rate=5, rate_limit=10)
    rate_limited_method = rate_limit_decorator(lambda: None)
    assert rate_limited_method() is None
    time.time = lambda: 0.21
    assert rate_limited_method() is None
    time.time = lambda: 0.41
    assert rate_limited_method() is None
    time.time = lambda: 0.61
    assert rate_limited_method() is None
    time.time = lambda: 0.81
    assert rate_limited_method() is None
    time.time = lambda: 1.1
    assert rate_limited_method() is None
    time.time = lambda: 1.11

# Generated at 2022-06-12 22:44:59.919431
# Unit test for function rate_limit
def test_rate_limit():
    # Collect all the rate limits
    rate_limits = list()
    last_call = [0.0]

    @rate_limit(rate=3, rate_limit=3)
    def rate_limited(rate_limits, last_call):
        time.sleep(1.0)
        rate_limits.append(time.clock() - last_call[0])
        last_call[0] = time.clock()

    for i in range(0, 10):
        rate_limited(rate_limits, last_call)

    # One second between calls, check that the difference
    # between calls is never less than 1 second.
    for rate_limit in rate_limits:
        assert rate_limit >= 1


# Generated at 2022-06-12 22:45:03.453656
# Unit test for function retry
def test_retry():
    @retry(retries=5)
    def test_func():
        if not getattr(test_func, 'counter', None):
            test_func.counter = 0
        test_func.counter += 1
        if test_func.counter < 3:
            return None
        return True
    assert(test_func() is True)
    assert(test_func.counter == 3)



# Generated at 2022-06-12 22:45:11.544604
# Unit test for function retry
def test_retry():
    """Retry test helper"""
    from ansible.module_utils.api import retry
    from ansible.module_utils.api import RateLimitError, RetryError

    @retry(retries=2, retry_pause=1)
    def test_retry_param(value):
        if value:
            return value
        raise RetryError("retry")

    @retry
    def test_no_retry(value):
        if value:
            return value
        raise RetryError("noretry")

    @retry(retries=1, retry_pause=0)
    def test_retry_fail(value):
        if value:
            return value
        raise RetryError("fail")

    test = test_retry_param("value")
    assert test == "value", test

    test

# Generated at 2022-06-12 22:45:21.349709
# Unit test for function rate_limit
def test_rate_limit():
    ''' Test rate_limit function '''
    import time

    def func(a, b):
        return a + b

    counter = 0

    rate = 10  # 10 calls per second
    calls = 100  # Run each function 100 times
    rate_limit_test = rate_limit(rate=rate, rate_limit=1)(func)

    begin = time.time()

    try:
        while counter < calls:
            rate_limit_test(1, 1)
            counter += 1
    except Exception as error:
        raise error

    end = time.time() - begin
    assert round(end, 2) == 0.1, "rate limit failed, should be: 0.1, actual: {0}".format(round(end, 2))

# Generated at 2022-06-12 22:45:48.148826
# Unit test for function retry
def test_retry():
    '''Test that the retry decorator works'''
    tries = [0]

    @retry(retries=3, retry_pause=0)
    def test_this():
        tries[0] += 1
        return False

    try:
        test_this()
    except Exception as e:
        # if we didn't hit it 3 times, fail
        if tries[0] != 3:
            raise
        else:
            return e.message



# Generated at 2022-06-12 22:45:57.677652
# Unit test for function rate_limit
def test_rate_limit():
    import inspect
    import time

    # get the function
    f = rate_limit(rate=5, rate_limit=10)
    assert inspect.isfunction(f)

    # get the wrapper
    w = f(lambda: None)
    assert inspect.isfunction(w)

    # first call, too soon
    time.sleep(0)
    w()
    time.sleep(0)
    w()
    time.sleep(0)
    w()
    time.sleep(0)
    w()

    # next call should wait
    start = time.time()
    w()
    end = time.time()
    assert abs(end - start) > 1.79
    assert abs(end - start) < 1.81


# Generated at 2022-06-12 22:46:06.815555
# Unit test for function retry
def test_retry():
    """Test retry with full jitter backoff"""
    @retry_with_delays_and_condition(backoff_iterator=generate_jittered_backoff(retries=10, delay_base=1, delay_threshold=1))
    def raise_exception_on_odd_number(number):
        if number % 2 == 0:
            print('success')
            return True
        else:
            print('raise')
            raise Exception('failed')

    raise_exception_on_odd_number(0)
    raise_exception_on_odd_number(1)
    raise_exception_on_odd_number(2)
    raise_exception_on_odd_number(3)

# Generated at 2022-06-12 22:46:12.108129
# Unit test for function rate_limit
def test_rate_limit():
    def w_rate_limit(rate=3, rate_limit=100):
        def wrapper(f):
            last = [0.0]

            def ratelimited(*args, **kwargs):
                if rate is not None and rate_limit is not None:
                    minrate = float(rate_limit) / float(rate)

                    elapsed = time.clock() - last[0]
                    left = minrate - elapsed
                    if left > 0:
                        time.sleep(left)
                    last[0] = time.clock()
                ret = f(*args, **kwargs)
                return ret

            return ratelimited
        return wrapper

    @w_rate_limit(rate=3, rate_limit=100)
    def foo():
        print("hello")


    # check rate limit with no arg
    foo()
    foo()
   

# Generated at 2022-06-12 22:46:19.153482
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    test_number = 0
    function_calls = 0

    class RetryableError(Exception):
        pass

    class NeverRetryError(Exception):
        pass

    class AlwaysRetryError(Exception):
        pass

    def test_function(should_raise_error, should_be_retried):
        nonlocal test_number
        nonlocal function_calls
        function_calls += 1

        test_number += 1
        if test_number == 1 and should_raise_error:
            if should_be_retried:
                raise RetryableError('test_function raised RetryableError on first call')
            else:
                raise NeverRetryError('test_function raised NeverRetryError on first call')

# Generated at 2022-06-12 22:46:22.210002
# Unit test for function retry
def test_retry():
    calls = 0

    @retry(retries=3, retry_pause=1)
    def call_me():
        global calls
        calls += 1
        raise Exception()

    try:
        call_me()
    except Exception:
        pass
    assert calls == 3



# Generated at 2022-06-12 22:46:31.453461
# Unit test for function rate_limit
def test_rate_limit():
    global count
    count = 0
    @rate_limit(rate=10, rate_limit=10)  # limit to 10 calls in 10 seconds
    def foo():
        global count
        count += 1
        return count

    # First call
    assert foo() == 1

    # Assert rate limit not violated (loop should complete before 1 second)
    start_time = time.time()
    for _ in range(1, 11):
        if time.time() - start_time > 1:
            assert False, 'rate_limit should allow 10 calls in 1 second.  Iteration %s' % _
        foo()
    end_time = time.time()
    assert (end_time - start_time) < 1

    # Assert rate limit is violated (loop should take more than 1 second)
    start_time = time.time()
   

# Generated at 2022-06-12 22:46:39.721056
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    class CustomRetryError(Exception):
        pass

    def should_retry_error(e):
        return not isinstance(e, CustomRetryError)

    @retry_with_delays_and_condition([0, 1, 2], should_retry_error)
    def retryable_function(should_fail):
        if should_fail:
            raise Exception()
        return "Success!"

    assert retryable_function(False) == "Success!"

    assert retryable_function(True) == "Success!"

    try:
        retryable_function(True)
    except Exception:
        pass
    else:
        raise Exception("Expected exception")


# Generated at 2022-06-12 22:46:43.266779
# Unit test for function retry
def test_retry():
    """Function testing retry"""
    @retry(retries=10, retry_pause=2)
    def fail_then_succeed(i):
        if i == 5:
            return ('OK')
        else:
            return ('Failed')
    result = fail_then_succeed(4)
    assert result == 'OK'



# Generated at 2022-06-12 22:46:53.741632
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    class CustomError(Exception):
        pass

    @retry_with_delays_and_condition(generate_jittered_backoff(retries=10))
    def function_raises_exception(should_raise=False):
        if should_raise:
            raise CustomError()
        return 1

    @retry_with_delays_and_condition(generate_jittered_backoff(retries=10), should_retry_error=lambda exc: isinstance(exc, CustomError))
    def function_raises_custom_error(should_raise=False):
        if should_raise:
            raise CustomError()
        return 1

    assert function_raises_exception(should_raise=False) == 1

# Generated at 2022-06-12 22:47:44.510693
# Unit test for function retry
def test_retry():
    """Test the retry decorator"""
    def test_function(*args, **kwargs):
        """docstring for test_function"""
        raise Exception('test exception')

    @retry(retries=5)
    def test_function_retried(*args, **kwargs):
        """docstring for test_function_retried"""
        return test_function(*args, **kwargs)

    assert test_function_retried() == None

# Generated at 2022-06-12 22:47:47.209628
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(rate=2, rate_limit=1)
    def rate_test():
        return True

    assert rate_test()
    assert not rate_test()
    assert rate_test()
    assert not rate_test()

# Generated at 2022-06-12 22:47:57.029719
# Unit test for function rate_limit
def test_rate_limit():
    """
    Unit test for function rate_limit
    """
    import unittest

    class TestRateLimit(unittest.TestCase):
        def setUp(self):
            self.func = rate_limit()
            self.count = 0

        def count_me(self):
            self.count += 1

        def test_rate_limit(self):
            """ Rate limit function should return the same number of calls as
            the rate if it is greater than the rate
            """

            @self.func
            def count_me_func(this):
                this.count_me()

            for i in range(10000):
                count_me_func(self)
            self.assertEqual(10000, self.count)

            # now test limiting the calls

# Generated at 2022-06-12 22:48:01.803183
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    call_count = 0
    @retry_with_delays_and_condition(backoff_iterator=[2, 5], should_retry_error=lambda e: e != None)
    def my_function():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise Exception("my_function")
        return "my_function"

    assert call_count == 0
    my_function()
    assert call_count == 2



# Generated at 2022-06-12 22:48:07.173162
# Unit test for function retry_with_delays_and_condition
def test_retry_with_delays_and_condition():
    # This passes if no exception is raised.
    @retry_with_delays_and_condition(generate_jittered_backoff(), retry_never)
    def function_with_no_retries():
        return "Success"

    # This passes if exception is raised once only before success.
    @retry_with_delays_and_condition(generate_jittered_backoff(), retry_never)
    def function_with_one_retry():
        try:
            raise Exception()
        except Exception:
            return "Success"

    assert function_with_no_retries() == "Success"
    assert function_with_one_retry() == "Success"


# Generated at 2022-06-12 22:48:09.132578
# Unit test for function rate_limit
def test_rate_limit():
    @rate_limit(rate=10, rate_limit=60)
    def test_fun():
        print("I just got delayed")

    for i in range(0, 20):
        test_fun()

# Generated at 2022-06-12 22:48:15.403593
# Unit test for function rate_limit
def test_rate_limit():
    """ Unit test for rate_limit """

    @rate_limit(3, 60)
    def do_rate():
        """ dummy function """
        return True

    timeit = False
    if timeit:
        import timeit
        start = timeit.default_timer()
    else:
        start = time.time()

    for _ in range(0, 15):
        do_rate()

    stop = time.time() if not timeit else timeit.default_timer()
    print("API rate limit function test took %s seconds" % (stop - start))



# Generated at 2022-06-12 22:48:24.999024
# Unit test for function rate_limit
def test_rate_limit():
    # no rate limit:
    _r = rate_limit()
    _f = _r(lambda *args, **kwargs: None)
    _f()

    # no rate limit at all
    _r = rate_limit(rate=None)
    _f = _r(lambda *args, **kwargs: None)
    _f()

    # rate limit is rate less than 1 req/sec
    _r = rate_limit(rate=1, rate_limit=2)
    _f = _r(lambda *args, **kwargs: None)
    _t = time.time()
    _f()
    _p = time.time() - _t
    assert _p >= 1 and _p <= 1.1

    # rate limit is 2 req/sec

# Generated at 2022-06-12 22:48:32.903745
# Unit test for function rate_limit
def test_rate_limit():
    """
    Unit tests for the rate_limit decorator
    
    These tests mock the time.time() and time.sleep() methods so
    the rate_limit can be tested deterministically. In order to
    do this the unit tests are imported and run in the ansible
    connection.winrm and connection.local connections, as they
    are core to Ansible
    """
    import time
    import unittest

    class TimeMock(object):
        def __init__(self):
            self.time = None

        def gettime(self):
            return self.time

    class SleepMock(object):
        def __init__(self):
            self.sleep_args = None
            self.sleep_called = 0

        def sleep(self, *args):
            self.sleep_args = args

# Generated at 2022-06-12 22:48:36.799978
# Unit test for function retry
def test_retry():
    # Add the decorators to the function
    # Reference: http://stackoverflow.com/a/7644321
    @retry(retries=3, retry_pause=1)
    def will_fail():
        # Always returns None
        return None

    # Call the function
    assert will_fail() is None



# Generated at 2022-06-12 22:50:32.487434
# Unit test for function retry
def test_retry():
    """Unit test for retry decorator"""

    def myfunc(n):
        if n == 2:
            return True
        else:
            return False

    a = retry(myfunc, 1, 1)(myfunc)(2)
    try:
        a = retry(myfunc, 1, 1)(myfunc)(1)
    except Exception as e:
        assert 'exceeded' in str(e)

    a = retry(myfunc, 3, 1)(myfunc)(1)
    assert a is False

if __name__ == '__main__':
        test_retry()

# Generated at 2022-06-12 22:50:40.512791
# Unit test for function retry
def test_retry():
    """ This should print 0, 1, 2, 3, 4 (in random order with pauses between each one) """
    @retry(retries=5, retry_pause=1)
    def ex_function():
        """ this function always fails """
        raise Exception("i failed")

    @retry(retries=5, retry_pause=1)
    def function(retry_count):
        """ print the retry_count, if its not 5, raise an exception triggering a retry """
        print(retry_count)
        if retry_count < 4:
            raise Exception("i failed")
        return "done"

    if function(0) != "done":
        raise Exception("failed")

    # this should never return, if it does raise an exception

# Generated at 2022-06-12 22:50:46.779821
# Unit test for function retry
def test_retry():
    @retry(retries=3, retry_pause=2)
    def foo():
        return 1
    assert foo() == 1

    @retry(retries=3, retry_pause=2)
    def foo_fail():
        return None
    assert foo_fail() is None

    @retry(retries=3, retry_pause=2)
    def fail():
        raise Exception("")
    failed = False
    try:
        fail()
    except:
        failed = True
    assert failed



# Generated at 2022-06-12 22:50:50.456717
# Unit test for function retry
def test_retry():
    @retry(retries=3, retry_pause=0)
    def is_two():
        global retries
        retries += 1
        if retries < 2:
            return False
        else:
            return True

    global retries
    retries = 0
    assert is_two()
    assert retries == 2



# Generated at 2022-06-12 22:50:56.921524
# Unit test for function rate_limit
def test_rate_limit():
    # pylint: disable=import-error,unused-import,wrong-import-position
    import pytest
    import contextlib
    # pylint: disable=redefined-outer-name

    @rate_limit(rate=2, rate_limit=2)
    def rate_limited_function():
        return True
    with contextlib.suppress(Exception):
        assert rate_limited_function()
        assert not rate_limited_function()
        assert rate_limited_function()
        assert not rate_limited_function()
        assert rate_limited_function()

    with pytest.raises(Exception):
        rate_limited_function()



# Generated at 2022-06-12 22:51:04.838972
# Unit test for function rate_limit
def test_rate_limit():

    expected_rate = 5.0
    expected_rate_limit = 30.0

    real_time = time.time

    def tick():
        return real_time() * 1000

    def timeTravel(ms):
        real_time.now += ms

    def wait(ms):
        real_time.now += ms

    # record time.time() calls
    rate_limit.now = 0.0
    rate_limit.tick = tick

    # set time.time() mock
    time.time = lambda: rate_limit.now / 1000.0

    @rate_limit(rate=expected_rate, rate_limit=expected_rate_limit)
    def test():
        """A dummy function to apply the rate_limit decorator"""
        return

    # run a bunch of calls and make sure they get rate limited
    # Math:
    #