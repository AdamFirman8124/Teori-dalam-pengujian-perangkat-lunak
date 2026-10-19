

# Generated at 2022-06-14 04:57:32.456889
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger

    logger = getLogger("example")
    logger.disabled = True
    logged_function = LoggedFunction(logger)


    @logged_function
    def run():
        return "result"


    logger.debug("Starting")
    result = run()
    logger.debug("Finished")

    assert result == "result"



# Generated at 2022-06-14 04:57:40.675487
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestLogger:
        debug_buf = []

        def debug(self, msg):
            self.debug_buf.append(msg)

    def test_func(a, b, c=2, d=3, e="foo"):
        return a + b + c + d + len(e)
    test_logger = TestLogger()
    logged_test_func = LoggedFunction(test_logger)(test_func)
    assert logged_test_func(1, 2, 3, 4, "bar") == 15
    assert (
        test_logger.debug_buf == [
            "test_func(1, 2, 3, 4, e='bar')",
            "test_func -> 15",
        ]
    )



# Generated at 2022-06-14 04:57:51.128629
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Test:
        @LoggedFunction(logging.getLogger(__name__))
        def func(*args, **kwargs):
            return args, kwargs

    with CaptureLogHandler() as clh:
        assert Test().func(1, 2, 3, a=1, b=2, c=3) == ((1, 2, 3), {"a": 1, "b": 2, "c": 3})
        assert clh.log_records[0].message == "func(1, 2, 3, a=1, b=2, c=3)"
        assert clh.log_records[1].message == "func -> ((1, 2, 3), {'a': 1, 'b': 2, 'c': 3})"

# Generated at 2022-06-14 04:57:56.778672
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # test __call__ with no value returned
    def test1():
        pass

    logger = logging.getLogger(LoggedFunction.__name__)
    test1 = LoggedFunction(logger)(test1)
    test1()

    # test __call__ with value returned
    def test2():
        return 1

    test2 = LoggedFunction(logger)(test2)
    value = test2()
    assert value == 1

    # test __call__ with function arguments
    def test3(value):
        return value

    value = test3(1)
    assert value == 1

    test3 = LoggedFunction(logger)(test3)
    value = test3(1)
    assert value == 1

    def test4(value):
        return value

    value = test4(value=1)
    assert value == 1



# Generated at 2022-06-14 04:58:07.493141
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert type(session) == requests.Session
    adapter_http = session.get_adapter("http://")
    assert type(adapter_http) == requests.adapters.HTTPAdapter
    assert type(adapter_http.max_retries) == requests.packages.urllib3.util.retry.Retry
    adapter_https = session.get_adapter("https://")
    assert type(adapter_https) == requests.adapters.HTTPAdapter
    assert type(adapter_https.max_retries) == requests.packages.urllib3.util.retry.Retry
    session = build_requests_session(retry=False)
    assert type(session) == requests.Session
    adapter_http = session.get_adapter("http://")

# Generated at 2022-06-14 04:58:11.073927
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def decorator(func):
        def decorated_func(*args, **kwargs):
            return func(*args, **kwargs)
        return decorated_func
    assert LoggedFunction(decorator)

# Generated at 2022-06-14 04:58:21.395388
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import collections.abc
    import logging

    def func(arg1, arg2=3):
        return "result"

    # Set up logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger_handler = logging.NullHandler()
    logger.addHandler(logger_handler)

    # Test: normal function
    decorated_func = LoggedFunction.__call__(
        LoggedFunction(logger), func
    )
    assert (
        decorated_func.__name__ == func.__name__
    ), "Function name should be unchanged"
    assert (
        decorated_func.__doc__ == func.__doc__
    ), "Function docstring should be unchanged"

# Generated at 2022-06-14 04:58:27.885178
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    # Create mock logger
    logger = Mock()

    # Create decorator and decorate function
    logged_func = LoggedFunction(logger)(test_func)

    # Call function and check output
    logged_func(1, "two", three=3)
    logger.debug.assert_any_call("test_func(1, 'two', three=3)")
    logger.debug.assert_any_call("test_func -> 12")



# Generated at 2022-06-14 04:58:40.651560
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    logger = logging.getLogger("test")
    logged_function = LoggedFunction(logger)
    @logged_function
    def f(a, *args, **kwargs):
        return a

    logger.debug = unittest.mock.Mock()
    # Test *args and **kwargs
    assert f(1, 2, 3, b=4) == 1
    logger.debug.assert_called_with("f('1', '2', '3', b='4')")
    # Test return value
    assert f("xyz") == "xyz"
    logger.debug.assert_called_with("f('xyz')")
    logger.debug.assert_called_with("f -> xyz")
    # Test None return value
    assert f(None) is None


# Generated at 2022-06-14 04:58:48.998495
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    from contextlib import redirect_stdout
    
    class LoggedFunctionTestTest(unittest.TestCase):
        def setUp(self):
            self.str_handler = logging.StreamHandler()
            self.str_handler.setLevel(logging.DEBUG)
            self.str_handler.setFormatter(
                logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            )
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(self.str_handler)

        def tearDown(self):
            self.logger.removeHandler(self.str_handler)
            self.str_handler.close

# Generated at 2022-06-14 04:58:58.686329
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logged_function = LoggedFunction(logger)

    @logged_function
    def foo(a, b, c=10, d=20):
        return "abc"

    val = foo(1, 2, 3, 4)
    val = foo(1, 2, d=4)
    assert val == "abc"



# Generated at 2022-06-14 04:59:10.344893
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def func(a, b=3, c=None):
        return f"{a} {b} {c}"

    # Create a fake logger with a capture StreamHandler
    logger = logging.getLogger("FakeLogger")
    logger.setLevel(logging.DEBUG)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Create LoggedFunction decorator
    decorate = LoggedFunction(logger)

    # Decorate function
    func = decorate(func)

    # Call the decorated function
    func("a", b=4)

    # Check the output
    actual = stream.getvalue().rstrip()
    expected = "FakeLogger DEBUG func(a, b=4)"

# Generated at 2022-06-14 04:59:16.879840
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys
    import unittest.mock
    from unittest import TestCase

    class Logger(logging.Logger):
        def __init__(self, logger_name):
            super().__init__(logger_name)
            self.log_stream = io.StringIO()
            self.handler = logging.StreamHandler(self.log_stream)
            self.addHandler(self.handler)

        @property
        def log_text(self):
            return self.log_stream.getvalue()

    class TestLoggedFunction__call__(TestCase):
        @unittest.mock.patch("lib.loggedfunction.logging")
        def test__success(self, pgm_logging):
            logger = Logger("logger")
            pgm_log

# Generated at 2022-06-14 04:59:27.673446
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    class Test:
        def func(self):
            return "test"

        def func_with_args(self, a, b, c=None):
            return a + b - c

    test = Test()
    test_methods = {
        "func": (test, (), {}),
        "func_with_args": (test, (1, 2), {"c": 10}),
    }

    for logger in [None, logging.getLogger("test")]:
        for function_name, (instance, args, kwargs) in test_methods.items():
            function = getattr(instance, function_name)
            decorated_function = LoggedFunction(logger)(function)
            expected_result = function(*args, **kwargs)
            assert decorated_function(*args, **kwargs) == expected_result


# Unit test

# Generated at 2022-06-14 04:59:40.590797
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    logger = logging.getLogger()

    class TestCases(unittest.TestCase):
        @LoggedFunction(logger)
        def loggerFunction(self, a, b, c=4, d="123", e=None, f=lambda x: x):  # pylint:disable=unused-argument, no-self-use
            return 1

        def test_normal(self):
            self.loggerFunction(1, 2)
            self.loggerFunction(1, 2, 3)
            self.loggerFunction(1, 2, 3, 4)
            self.loggerFunction(1, 2, 3, 4, 5)
            self.loggerFunction(1, 2, 3, 4, 5, 6)

# Generated at 2022-06-14 04:59:46.903172
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    # Capture logging output
    log_output = io.StringIO()
    stream_handler = logging.StreamHandler(log_output)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

    # Decorate function without parameters
    @LoggedFunction(logger)
    def func():
        return 2

    assert func() == 2
    log_output.seek(0)
    assert log_output.read() == "func()\nfunc -> 2\n"

    # Decorate function with parameters
    @LoggedFunction(logger)
    def func2(x: int, y: str, z: float = 1.5):
        return x * z


# Generated at 2022-06-14 04:59:48.607617
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert not session.hooks

# Generated at 2022-06-14 04:59:50.188752
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert type(session) == Session

# Generated at 2022-06-14 04:59:50.853741
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    pass



# Generated at 2022-06-14 05:00:00.901012
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging
    logger = logging.getLogger(__name__)

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            logger.handlers = []

        def test__LoggedFunction___call__debug_True(self):
            logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler()
            logger.addHandler(handler)

            @LoggedFunction(logger)
            def foo(a, b, c):
                return a + b + c

            x = foo(1, 2, 3)
            self.assertEqual(x, 6)
            self.assertEqual(
                handler.buffer[-1].rstrip(),
                "foo(1, 2, 3) -> 6",
            )


# Generated at 2022-06-14 05:00:17.239156
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    class FakeLogger:
        log_data = []

        def debug(self, arg):
            self.log_data.append(arg)

    logger = FakeLogger()

    @LoggedFunction(logger)
    def function_with_no_arg():
        pass

    @LoggedFunction(logger)
    def function_with_args(arg1, arg2, kwarg_1="one", kwarg_2=None):
        pass

    function_with_no_arg()
    assert logger.log_data[-2] == "function_with_no_arg()"
    assert logger.log_data[-1] == "function_with_no_arg -> None"

    function_with_args("A", "B", "one", None)

# Generated at 2022-06-14 05:00:26.709982
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logging.basicConfig(level=logging.DEBUG)
    from logging import getLogger

    logger = getLogger("test")
    logged_function = LoggedFunction(logger)

    def func_1(a, b=None):
        logger.debug("func_1")
        return a * b if b else a * 2

    func_1_logged = logged_function(func_1)

    func_1_logged(1, b=2)
    func_1_logged(2)



# Generated at 2022-06-14 05:00:37.887296
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    r = session.get("https://httpbin.org/delay/2")
    assert r.status_code == 200
    session = build_requests_session(retry=False)
    r = session.get("https://httpbin.org/insult")
    assert r.status_code == 200
    session = build_requests_session(retry=0)
    r = session.get("https://httpbin.org/insult")
    assert r.status_code == 200
    retry = Retry(total=3, method_whitelist=False, backoff_factor=0)
    session = build_requests_session(retry=retry)
    r = session.get("https://httpbin.org/insult")
    assert r.status_code == 200

# Generated at 2022-06-14 05:00:38.875961
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    pass



# Generated at 2022-06-14 05:00:49.077927
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    assert logger.getEffectiveLevel() == logging.DEBUG
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler) 
    
    @LoggedFunction(logger)
    def test_func(a, b, c=1, d=2):
        pass
    test_func('a', 'b', c=3, d=4)
    # The following lines may be inconsistent with the test result
    # Should change to test_func result == None (using assert)
    # test_func('a', 'b', c=3, d=4) -> test_func(a='a', b='b', c='3', d='4') -> None


# Generated at 2022-06-14 05:01:00.868412
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    from io import StringIO
    import sys
    import logging

    mock_logger = Mock()
    mock_logger.debug = lambda *args, **kwargs: print(*args, file=sys.stdout)

    target = LoggedFunction(mock_logger)

    def test_func(*args, **kwargs):
        print(
            f"test_func start: ({', '.join([str(x) for x in args])}, "
            f"{{{', '.join([f'{k}={v}' for k, v in kwargs.items()])}}})",
            file=sys.stdout,
        )
        print("test_func end", file=sys.stdout)

    result = target(test_func)()
    assert result is None

# Generated at 2022-06-14 05:01:04.529461
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)

    logged_function = LoggedFunction(logger)

    @logged_function
    def testfunc(x, y, z=1):
        return x + y + z

    testfunc(1, 1, z=1)

# Generated at 2022-06-14 05:01:17.518411
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Mock
    import logging

    class MockLogger:

        def debug(self, log_msg):
            if log_msg == "test_func_1()":
                assert True
                return

            if log_msg == "test_func_2(4, 5)":
                assert True
                return

            if log_msg == "test_func_3(1, 2, c=3)":
                assert True
                return

            if log_msg == "test_func_4 -> [1, 2, 3]":
                assert True
                return

            if log_msg == "test_func_2 -> 7":
                assert True
                return

            if log_msg == "test_func_3 -> None":
                assert True
                return

            assert False

    mock_logger = MockLogger()

    # Test
   

# Generated at 2022-06-14 05:01:28.067320
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import logging
    import requests
    import requests_mock
    import json
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    log_capture_string = io.StringIO()
    ch = logging.StreamHandler(log_capture_string)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    session = build_requests_session()
    with requests_mock.mock() as m:
        m.get("http://httpbin.org/get", text="<h1>Hello, World!</h1>")
        url = "http://httpbin.org/get"
        data = {"key": "value"}
        headers = {'User-Agent': 'Mozilla/5.0'}


# Generated at 2022-06-14 05:01:35.454576
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock, call

    logger = MagicMock()
    log_decorator = LoggedFunction(logger)

    @log_decorator
    def test_function(a, b, c):
        return 1

    test_function("'a", "b", c=3)
    expected_calls = [
        call(
            "test_function('a', 'b', c=3)"
        ),
        call("test_function -> 1"),
    ]
    logger.debug.assert_has_calls(expected_calls)

# Unit tests for method __init__ of class LoggedFunction

# Generated at 2022-06-14 05:02:30.925428
# Unit test for function build_requests_session
def test_build_requests_session():
    s = build_requests_session()
    assert isinstance(s, Session) == True



# Generated at 2022-06-14 05:02:38.324743
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock
    from unittest.mock import Mock

    logger = Mock()

    def func(*args, **kwargs):
        pass

    logged_func = LoggedFunction(logger)(func)

    logged_func(1,2," 3  ","four",five=6,seven=8.0)
    logger.debug.assert_called_with("func(1, 2, ' 3  ', 'four', five=6, seven=8.0)")

    logged_func(1,2," 3  ","four",seven=8.0)
    logger.debug.assert_called_with("func(1, 2, ' 3  ', 'four', seven=8.0)")

# Generated at 2022-06-14 05:02:51.476417
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    @LoggedFunction(logger)
    def add(x, y):
        return x + y

    @LoggedFunction(logger)
    def sub(a, b, c):
        return a - b - c


# Generated at 2022-06-14 05:03:01.770181
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    # Create a test function that returns the units argument
    def repeat_units(units):
        return units

    # Create a logger to test the output of LoggedFunction
    logger = logging.getLogger("test")
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    # Apply LoggedFunction to the test function and run it
    repeat_units_logged = LoggedFunction(logger)(repeat_units)
    assert repeat_units_logged(1.0) == 1.0

    # Check the output
    stream_handler.flush()
    _, recorded = stream_handler.stream.read().splitlines()
    assert recorded == "test:DEBUG:repeat_units(1.0) -> 1.0"

# Generated at 2022-06-14 05:03:08.541629
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    from unittest.mock import Mock

    logger = Mock()

    def func(a, b=3, *args, **kwargs):
        pass

    logged_func = LoggedFunction(logger)(func)
    logged_func(1, 2, 3)

    assert logger.debug.call_count == 1
    assert logger.debug.call_args[0][0] == "func(1, 2, 3)"


# Generated at 2022-06-14 05:03:18.452618
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    test_cases = [
        {"input":{"func": lambda x: x + 1, "args": [3], "kwargs": {"y": 4}}, "output":{"logged_func": 4}},
        {"input":{"func": lambda x: x + 1, "args": [3], "kwargs": {"y": 4, "z": 5}}, "output":{"logged_func": 4},
            "description":"no invalid formatting"},
    ]
    logger = logging.getLogger("test_LoggedFunction")
    for test_case in test_cases:
        test_case_description = test_case.get("description")
        logger.debug(f"Starting test case with description '{test_case_description}'.")
        func = test_case["input"]["func"]
        args = test_case["input"]["args"]


# Generated at 2022-06-14 05:03:23.319196
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG)
    @LoggedFunction(logger)
    def test_func(a,b,c=10):
        return a+b+c
    assert test_func("asd","fgh") == "asdfgh10"

# Generated at 2022-06-14 05:03:33.527032
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    stream = io.StringIO()
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(stream)
    formatter = logging.Formatter("%(levelname)s:%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug("Test basic function, no arguments, no return")
    @LoggedFunction(logger)
    def test():
        pass
    test()
    logger.debug("Test function with 1 argument, no return")
    @LoggedFunction(logger)
    def test(a):
        pass
    test("Hello, world")
    logger.debug("Test function with 2 arguments, no return")

# Generated at 2022-06-14 05:03:43.258975
# Unit test for function build_requests_session
def test_build_requests_session():
    import unittest
    import requests

    class TestRequestsSession(unittest.TestCase):
        def setUp(self):
            self.session = build_requests_session()

        def tearDown(self):
            pass

        def test_default(self):
            self.assertIsInstance(self.session, requests.Session)

        def test_raise_for_status(self):
            import time

            with self.assertRaises(requests.HTTPError):
                self.session.get("http://localhost:32678/404")
            # there is a connection pooling in requests.Session,
            # sometimes the error is raised by the next request.
            with self.assertRaises(requests.HTTPError):
                time.sleep(2)


# Generated at 2022-06-14 05:03:56.694690
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging
    logger = logging.getLogger('test_logger')
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    class TestLoggedFunction___call__(unittest.TestCase):
        @LoggedFunction(logger)
        def test_logged_func(self, a, b, c=1):
            print('this line will not be logged')
            return 'logged'
        def test_logged_func_call(self):
            self.test_logged_func(1, 'abc')
            self.test_logged_func(a=1, b='abc')
            self.test_logged_func(1, 'abc', 3)

# Generated at 2022-06-14 05:04:44.370973
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO

    class LogBuffer:
        def __init__(self, logger):
            self.buffer = StringIO()
            self.logger = logging.getLogger(logger)
            self.handler = logging.StreamHandler(self.buffer)
            self.logger.addHandler(self.handler)
            self.logger.setLevel(logging.DEBUG)
            self._result = None

        @staticmethod
        def _parse(buffer):
            return str(buffer.getvalue())[:-1].split("\n")

        @property
        def result(self):
            return self._result

        @result.setter
        def result(self, value):
            self._result = value

        def get_log(self):
            return self._parse(self.buffer)


# Generated at 2022-06-14 05:04:54.163303
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging
    import unittest.mock as mock
    import sys

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def test_logged(a, b=2, *args, c=3, **kwargs):
        pass

    logger.addHandler(logging.StreamHandler(sys.stdout))
    logged_test_logged = LoggedFunction(logger)(test_logged)
    logged_test_logged(1, b=5, c=7, d=9)



# Generated at 2022-06-14 05:05:02.580834
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    from unittest.mock import call

    logger = Mock()
    # A function which accepts two arguments [a, b] and returns a + b
    def target(a, b):
        return a + b

    logged_function = LoggedFunction(logger)
    logged_target = logged_function(target)

    # Call logged_target with different arguments
    logged_target(1, 2)
    logged_target("a", "b")
    logged_target([1, 2], ["a", "b"])
    logged_target({"a": 1}, {"b": 2})

    # Verify the output

# Generated at 2022-06-14 05:05:15.074903
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Setup
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    message_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    message_handler.setFormatter(formatter)
    logger.addHandler(message_handler)

    @LoggedFunction(logger)
    def hey():
        return "hey"

    @LoggedFunction(logger)
    def you(name: str, age: int) -> str:
        return f"hi {name}, you are {age} years old"

    # Testing method __call__ of Class LoggedFunction
    logger.debug(hey())
    logger.debug

# Generated at 2022-06-14 05:05:20.328803
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("unit test")
    hdlr = logging.FileHandler("unit_test_LoggedFunction___call__.txt", "w")
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def my_func(a, b, c=None):
        return "result"

    my_func("a", "b", c="c")



# Generated at 2022-06-14 05:05:31.754188
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    # Python's logging module has a default global value, but logging.basicConfig() does NOT change this default
    # value. Unset this default value to test this function without side effect.
    logging._acquireLock()
    try:
        # Python 3.8+
        del logging._handlers
    except AttributeError:
        # Python 3.7
        del logging._handlerList
    logging._releaseLock()
    logger = logging.getLogger()
    # Redirect logging output to sys.stdout to check the output
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.DEBUG)
    function = LoggedFunction(logger)(test_func)
    function()
    function(1)
    function(1, 2, 3)

# Generated at 2022-06-14 05:05:43.929326
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import ConnectionError
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    from unittest import TestCase
    from unittest.mock import patch
    from unittest.mock import Mock
    from unittest.mock import MagicMock
    from unittest.mock import ANY
    from unittest.mock import AsyncMock
    from unittest.mock import call
    from unittest.mock import create_autospec
    import asyncio
    import aiohttp
    ##########################################################################
    #test raise_for_status
    session = build_requests_session(True,Retry())
    assert isinstance(session.hooks["response"][0],functools.partial)

# Generated at 2022-06-14 05:05:53.568973
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import contextlib

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    f = io.StringIO()
    handler = logging.StreamHandler(f)
    logger.addHandler(handler)
    # default logging level of handler is NOTSET, so we need to manually set it to debug
    handler.setLevel(logging.DEBUG)
    logger.debug('test message')
    print(f.getvalue())

    @LoggedFunction(logger)
    def test_func(arg1, arg2, arg3=None, arg4=None):
        return arg1 + arg2

    with contextlib.redirect_stdout(f):
        test_func(1, 2, arg3=3, arg4=4)

# Generated at 2022-06-14 05:05:58.558846
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def foo(a, b, c=1, d=2):
        return a + b + c + d
    assert foo(1, 2, d=3) == 7
    logger = logging.getLogger()
    foo = LoggedFunction(logger)(foo)
    assert foo(1, 2, d=3) == 7

# Generated at 2022-06-14 05:06:03.643978
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    test_logger = logging.getLogger(__name__)
    test_logger.setLevel(logging.DEBUG)

    @LoggedFunction(test_logger)
    def do_log():
        return "Hello World!"

    do_log()
    do_log()



# Generated at 2022-06-14 05:06:40.369607
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import os
    import unittest
    import tempfile
    import logging

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.log_file_path = tempfile.mkstemp()[1]
            for handler in logging.root.handlers[:]:
                logging.root.removeHandler(handler)
            fp = open(self.log_file_path, "w")
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] %(module)s - %(message)s"
            )
            handler = logging.StreamHandler(fp)
            handler.setFormatter(formatter)
            self

# Generated at 2022-06-14 05:06:52.639385
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io

    class Test:
        pass

    t = Test()
    buffer = io.StringIO()
    t.logger = Logger.from_buffer(buffer)
    decorated = LoggedFunction(t.logger)(t.method)

    buffer.truncate(0)
    decorated(1)
    assert buffer.getvalue() == "method(1)\nmethod -> None\n"

    buffer.truncate(0)
    decorated(1, 2, a=3, b=4)
    assert buffer.getvalue() == "method(1, 2, a='3', b='4')\nmethod -> None\n"

    buffer.truncate(0)
    decorated(1, 2, 3)
    assert buffer.getvalue() == "method(1, 2, 3)\nmethod -> None\n"



# Generated at 2022-06-14 05:06:58.955671
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, sentinel
    from logging import Logger
    from pytest import fixture

    logger = Mock(Logger)
    wrapper = LoggedFunction(logger)
    func = Mock()

    @wrapper
    def logged_func(*args, **kwargs):
        func(*args, **kwargs)

    @fixture
    def logged_func_call(*args, **kwargs):
        logged_func(*args, **kwargs)
        logger.debug.assert_called_once()

    def test_logs_arguments_with_no_kwargs(logged_func_call):
        logged_func_call(sentinel.arg1, sentinel.arg2)


# Generated at 2022-06-14 05:07:09.522659
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging
    import sys

    class TestLoggedFunction___call__(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger()
            self.stream = sys.stderr
        def test_no_return_value(self):
            self.assertEqual(self.logger.level, logging.WARNING)
            @LoggedFunction(self.logger)
            def foo():
                pass
            foo()
            self.assertEqual(self.stream.getvalue(), "foo()\n")
        def test_with_return_value(self):
            self.assertEqual(self.logger.level, logging.WARNING)
            @LoggedFunction(self.logger)
            def foo():
                return 'bar'

# Generated at 2022-06-14 05:07:22.049223
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # import pytest
    from logging import getLogger

    mock_logger = getLogger("LoggedFunction")
    # mock_logger = pytest.mock.Mock()
    def func1(a:str, b: int, c:str="abc", d:int=5) -> str:
        ...
    lf = LoggedFunction(mock_logger)
    wrapped_func1 = lf(func1)
    wrapped_func1("a", 2, d=3)
    # mock_logger.debug.assert_called_once_with("func1('a', 2, c='abc', d=3)")

    def func2(a:str, b: int, c:str="abc", d:int=5) -> str:
        return "result"

# Generated at 2022-06-14 05:07:26.694355
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import Mock, patch

    logger = Mock(logging.Logger)

    @LoggedFunction(logger)
    def test(arg):
        return f"result for {arg}"

    test("hello")

    logger.debug.assert_called_with("test('hello')")
    logger.debug.assert_called_with("test -> result for hello")

