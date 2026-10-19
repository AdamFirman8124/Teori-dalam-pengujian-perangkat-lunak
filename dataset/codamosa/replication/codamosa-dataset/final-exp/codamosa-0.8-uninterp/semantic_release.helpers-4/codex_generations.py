

# Generated at 2022-06-14 04:57:34.066680
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    buffer = io.StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    log_handler = logging.StreamHandler(buffer)
    log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)

    @LoggedFunction(logger)
    def test_func(*args, **kwargs):
        return '{"a": [1,2,3], "b": "foobar"}'

    test_func(1,2,3,4,b=6)
    assert buffer.getvalue().strip

# Generated at 2022-06-14 04:57:39.505156
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    log = logging.getLogger()
    handler = logging.StreamHandler(io.StringIO())
    handler.setFormatter(logging.Formatter("%(message)s"))
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    @LoggedFunction(log)
    def add(x, y):
        return x + y

    add(5, 7)
    assert "add(5, 7) -> 12" in handler.stream.getvalue()



# Generated at 2022-06-14 04:57:50.776437
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import inspect
    
    # Set up logger
    log = logging.getLogger("test")
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    log.addHandler(handler)
    
    # Create a LoggedFunction object
    logged_func = LoggedFunction(log)
    
    # Define a function to be logged
    def test_func(a, b, *args, c=1, d=2, **kwargs):
        return a + b + c + d + sum(args) + sum(kwargs.values())
        
    logged_test_func = logged_func(test_func)
    
    # Call logged_test_func with different parameters

# Generated at 2022-06-14 04:58:01.335910
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    from logging import Logger

    test_logger = mock.create_autospec(Logger)
    test_function = mock.Mock(spec_set=["__name__"])
    test_function.__name__ = "test_function"

    logged_function = LoggedFunction(test_logger)
    logged_function(test_function)("test_arg1", kwarg1="test_kwarg1")

    test_logger.debug.assert_called_once_with(
        "test_function('test_arg1', kwarg1='test_kwarg1')"
    )
    test_function.assert_called_once_with("test_arg1", kwarg1="test_kwarg1")

# Generated at 2022-06-14 04:58:11.510077
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Test method __call__ of class LoggedFunction.
    """
    import logging
    from io import StringIO

    #Create logger
    logger = logging.getLogger("test_LoggedFunction___call__")
    logger.setLevel(logging.DEBUG)
    io = StringIO()
    log_handler = logging.StreamHandler(io)
    logger.addHandler(log_handler)

    # Create a LoggedFunction instance
    func_logger = LoggedFunction(logger)

    # Define and log the test function
    @func_logger
    def add_two(a, b):
        c = a + b
        return c

    # Test the logged function
    result = add_two(1, 2)
    assert result == 3
    # Test output of logger

# Generated at 2022-06-14 04:58:21.788450
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import unittest
    import sys

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger("test")
            self.logger.setLevel(logging.DEBUG)
            self.stdout = sys.stdout
            self.string = io.StringIO()
            sys.stdout = self.string

        def tearDown(self):
            self.string.close()
            sys.stdout = self.stdout

        def test_log_string(self):
            @LoggedFunction(self.logger)
            def test_func(s):
                return s

            test_func("test string")

# Generated at 2022-06-14 04:58:34.761171
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import StringIO

    logging.basicConfig()
    logger = logging.getLogger("LoggedFunction")
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def super_addition(a, b=3):
        """
        Add two numbers.
        :param a: first number
        :param b: second number
        :return: sum of two numbers
        """
        return a + b

    @LoggedFunction(logger)
    def other_func(a, b=4):
        """
        Do something.
        :param a: first number
        :param b: second number
        :return: None
        """
        return a + b

    # Capture output to buffer
    buffer = StringIO.StringIO()
    handler = logging.StreamHandler(buffer)


# Generated at 2022-06-14 04:58:42.150084
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()
    logged_func = LoggedFunction(logger)(lambda x: x*x)
    assert logged_func(2) == 4
    assert logger.debug.call_count == 2
    assert logger.debug.call_args_list[0][0][0] == "__call__(2)"
    assert logger.debug.call_args_list[1][0][0] == "__call__ -> 4"
    assert logger.debug.call_args_list[1][0][0] != "__call__ -> 2"

# Generated at 2022-06-14 04:58:55.138947
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    import unittest

    class Test(unittest.TestCase):
        def test_decorator_logs_arguments_and_results(self):
            """
            Tests that the decorator logs the arguments and result.
            """
            log = logging.getLogger("test")
            out = StringIO()
            log.addHandler(logging.StreamHandler(out))
            log.setLevel(logging.DEBUG)

            @LoggedFunction(log)
            def example_function(arg1, arg2, arg3):
                return f"{arg1}-{arg2}-{arg3}"

            example_function("foo", "bar", "baz")

# Generated at 2022-06-14 04:59:02.368196
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    from logging import Logger
    from functools import partial

    # Mocks
    mock_logger = mock.create_autospec(Logger)
    mock_logger.debug.return_value = None
    mock_func = mock.create_autospec(partial(print))
    mock_func.__name__ = "mock_func"
    mock_func.side_effect = None

    # Class that is being tested
    logged_function = LoggedFunction(mock_logger)

    # Actual Calls
    logged_mock_func = logged_function(mock_func)
    logged_mock_func()

    # Expected Calls
    mock_logger.debug.assert_called_with("mock_func()")
    mock_func.assert_called_once()

# Generated at 2022-06-14 04:59:06.277458
# Unit test for function build_requests_session
def test_build_requests_session():
    pass

# Generated at 2022-06-14 04:59:15.712156
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    from os import environ
    environ["LOG_LEVEL"] = "DEBUG"
    from ..utils import Logger, LoggedFunction

    test_func_name = "test_func"
    logger = Logger()
    expected_log_msg_before = f"{test_func_name}(1, '2', 3)"
    expected_log_msg_after = f"{test_func_name} -> 4"

    def test_func(num1, str2, num3):
        return num1 + num3

    b = LoggedFunction(logger)
    with mock.patch.object(logger, "debug") as mock_logger:
        b(test_func)(1, "2", 3)
        assert mock_logger.call_count == 2
        assert expected_log_msg

# Generated at 2022-06-14 04:59:21.693412
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def add(x, y=1):
        return x + y

    # import logging, logging.config
    # logging.config.fileConfig('logging.conf')
    # logger = logging.getLogger('exampleApp')
    logger = None
    func = LoggedFunction(logger)(add)

    # Call function
    result = func(1, 2)
    assert result == 3



# Generated at 2022-06-14 04:59:29.742191
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    # Create MockLogger
    class MockLogger:
        def __init__(self):
            self.log = []

        def debug(self, message):
            self.log.append(message)

    # Create Mock function
    def func(*args, **kwargs):
        pass

    # Create logger and LoggedFunction
    logger = MockLogger()
    logged_func = LoggedFunction(logger)

    # Test without arguments
    logged_func(func)
    assert logger.log[0] == 'func()'

    # Test with arguments
    logger.log = []
    logged_func(func, 1, a=2)
    assert logger.log[0] == "func(1, a=2)"


# Generated at 2022-06-14 04:59:37.163824
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Test method __call__ of class LoggedFunction
    """
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    @LoggedFunction(logger)
    def sum(*args):
        return sum(args)

    assert sum(1, 2) == 3
    assert sum(1, 2, 3, 4) == 10
    assert sum(1, 2, 3, 4, 5, 6) == 21

# Generated at 2022-06-14 04:59:44.566646
# Unit test for function build_requests_session
def test_build_requests_session():
    raise_for_status_true = build_requests_session()
    raise_for_status_false = build_requests_session(raise_for_status=False)
    retry_false = build_requests_session(retry=False)
    retry_true = build_requests_session(retry=True)
    int_retry = build_requests_session(retry=3)
    retry_instance = build_requests_session(retry=Retry())
    invalid_retry = build_requests_session(retry="a")


# Generated at 2022-06-14 04:59:55.734639
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest.mock
    def none_function(*args, **kwargs):
        return None

    mock_logger = unittest.mock.MagicMock()
    LoggedFunction(mock_logger)(none_function)(1)
    mock_logger.debug.assert_called_once_with("none_function(1)")

    LoggedFunction(mock_logger)(none_function)(1, a=2)
    mock_logger.debug.assert_has_calls([
        unittest.mock.call("none_function(1)"),
        unittest.mock.call("none_function(1, a=2)")
    ])

# Generated at 2022-06-14 04:59:58.592056
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    session.get("http://example.com")

# Generated at 2022-06-14 05:00:04.083403
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    log = logging.getLogger(__name__)

    def foo(a: str, b: str, c: int, *args, **kwargs):
        if True:
            print(a)
            print(b)
            print(c)
            print(args)
            print(kwargs)
            return "foo_return"

    decorated_foo = LoggedFunction(log)(foo)

    log.setLevel(log.DEBUG)
    try:
        decorated_foo("a", "b", 3, 4, 5, 6, x="x", y="y", z="z")
    except:
        pass



# Generated at 2022-06-14 05:00:16.089822
# Unit test for function build_requests_session
def test_build_requests_session():
    requests = build_requests_session(raise_for_status=True, retry=True)
    requests = build_requests_session(raise_for_status=True, retry=3)
    requests = build_requests_session(raise_for_status=True, retry=Retry())
    requests = build_requests_session(raise_for_status=False, retry=True)
    requests = build_requests_session(raise_for_status=False, retry=3)
    requests = build_requests_session(raise_for_status=False, retry=Retry())
    requests = build_requests_session(raise_for_status=False, retry=False)
    requests = build_requests_session(raise_for_status=True, retry=False)

# Generated at 2022-06-14 05:00:28.251131
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    log = logging.getLogger("Test_loggedfunction")
    log.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("[%(levelname)8s] %(message)s"))
    log.addHandler(stream_handler)
    @LoggedFunction(log)
    def test(param1, param2='test'):
        return param1 + param2
    test('ab')
    

# Generated at 2022-06-14 05:00:32.684632
# Unit test for function build_requests_session
def test_build_requests_session():
    assert build_requests_session().__class__== Session
    assert build_requests_session(raise_for_status=False).hooks == {}
    assert build_requests_session(retry=False).adapters.clear()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:00:45.039781
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    def func(a, b, c="c"):
        return a + b + c

    mlog = Mock()
    logger = LoggedFunction(mlog)
    func = logger(func)

    a = "a"
    b = "b"

    func(a, b)
    mlog.debug.assert_called_once_with(
        "func('a', 'b', c='c')"
    )

    mlog.reset_mock()
    assert func(1, 2) == "123"

# Generated at 2022-06-14 05:00:55.808496
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging
    import io
    import contextlib

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.stream = io.StringIO()
            self.logger = logging.getLogger("test")
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(logging.StreamHandler(self.stream))

        def test_LoggedFunction__call__(self):
            @LoggedFunction(logger=self.logger)
            def test_func(a, b, c=3):
                return a + b + c

            test_func(1, 2)
            test_func(1, 2, c=4)
            test_func(a=1, b=2)

# Generated at 2022-06-14 05:00:56.398939
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    pass

# Generated at 2022-06-14 05:00:58.933057
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def func(a, b=1, *args):
        return None

    assert LoggedFunction(logging.getLogger())(func)(1, 2) == None



# Generated at 2022-06-14 05:01:07.460343
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, patch
    from uuid import uuid4

    logger = Mock()
    logged_function = LoggedFunction(logger)

    def test_function(arg1, arg2=None, kwarg1="keyword arg 1", kwarg2="keyword arg 2"):
        return uuid4()

    result = logged_function(test_function)("argument 1", arg2="argument 2")

    logger.debug.assert_called_once_with(
        "test_function('argument 1', arg2='argument 2', kwarg1=keyword arg 1, kwarg2=keyword arg 2)"
    )
    logger.debug.assert_called_once_with(f"test_function -> {result}")



# Generated at 2022-06-14 05:01:16.598551
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock

    logger = MagicMock()
    class TestClass:
        def test_method(self, a, b, c=3):
            return a + b + c
        def test_method_no_return_value(self, a, b, c=3):
            pass

    def test_func(a, b, c=3):
        return a + b + c
    def test_func_no_return_value(a, b, c=3):
        pass

    logger.debug = MagicMock()

    logged_func = LoggedFunction(logger)(test_func)
    logged_func(1,2,3)
    logged_func(1,b=2,c=3)

# Generated at 2022-06-14 05:01:22.825355
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(retry=Retry(total=10, status_forcelist=[405]))
    assert session._adapters == {
        "http://": HTTPAdapter(max_retries=Retry(total=10, status_forcelist=[405])),
        "https://": HTTPAdapter(max_retries=Retry(total=10, status_forcelist=[405])),
    }

# Generated at 2022-06-14 05:01:29.972181
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger

    logger = getLogger("logger")
    logger.debug = lambda x: print(x)

    def f(a, b, *args, **kwargs):
        pass

    logged_function = LoggedFunction(logger)

    logged_func = logged_function(f)

    logged_func(1, 2)


if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:01:47.379400
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    from unittest.mock import sentinel
    from logging import Logger

    lf = LoggedFunction(mock.MagicMock(spec=Logger))
    func = mock.MagicMock()
    func.__name__ = sentinel.name
    func.return_value = sentinel.return_value

    args = object(), object()
    kwargs = dict(one=object(), two=object())

    @lf
    def logged_func(*args, **kwargs):
        return func(*args, **kwargs)

    logged_func(*args, **kwargs)

    func.assert_called_once_with(*args, **kwargs)

# Generated at 2022-06-14 05:01:48.826694
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert session.max_redirects == 30

# Generated at 2022-06-14 05:01:59.255272
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger('logger')
    class testLoggedFunction:
        def __call__(self, func):
            @functools.wraps(func)
            def logged_func_test(self, *args, **kwargs):
                self.logger.debug(
                    '{function}({args}{kwargs})'.format(
                        function=func.__name__,
                        args=", ".join([format_arg(x) for x in args]),
                        kwargs="".join(
                            [f", {k}={format_arg(v)}" for k, v in kwargs.items()]
                        ),
                    )
                )

                # Call function
                result = func(self, *args, **kwargs)

                # Log result
                if result is not None:
                    self.log

# Generated at 2022-06-14 05:02:08.503698
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    logger = logging.getLogger()
    class StreamLogger:
        def __init__(self):
            self.cached_log_message = ""
        def info(self, message):
            self.cached_log_message = message
    stream_logger = StreamLogger()
    logger.addHandler(stream_logger)
    class Demo:
        def foo(self, a, b, c='abc'):
            self.a = a; self.b = b; self.c = c
        @LoggedFunction(logger)
        # Another way to use LoggedFunction
        def bar(self, x, y, z=2):
            self.x = x; self.y = y; self.z = z
    d = Demo()

# Generated at 2022-06-14 05:02:21.292137
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    class LoggedFunctionTest(unittest.TestCase):
        def setUp(self):
            logging.basicConfig(level=logging.DEBUG)
            self.logger = logging.getLogger("LoggedFunctionTest")
            self.logger.setLevel(logging.DEBUG)
            self.logged_function = LoggedFunction(self.logger)

        def test_withParams(self):
            def f(x, y, z):
                return x + y + z

            logged_f = self.logged_function(f)
            self.assertEqual(logged_f(1, 2, 3), 6)

        def test_withNamedParams(self):
            def f(x, y, z):
                return x + y + z


# Generated at 2022-06-14 05:02:28.439318
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import WARNING
    from logging import getLogger

    # Create decorator
    logger = getLogger(__name__)
    logger.setLevel(WARNING)
    logged_function = LoggedFunction(logger)

    # Test decorator with a function
    @logged_function
    def test(a, b, c=3):
        return a + b + c

    assert test.__name__ == "test"
    assert test(1, 2) == 6



# Generated at 2022-06-14 05:02:40.065041
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest.mock as mock
    import numpy as np
    from mrcase.utils import LoggedFunction
    from numpy.testing import assert_equal
    logger_mock = mock.Mock()
    f = LoggedFunction(logger=logger_mock)
    func = mock.Mock(__name__='func')

    @f
    def func(x:np.ndarray,y:int,z:float,**kwargs):
       x = np.asarray(x).dot(y) + z
       return x
    func([1,2,3],y=1,z=0.5,p=0.7,q=[1,2,3])

# Generated at 2022-06-14 05:02:52.837096
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()

    s = session.get("https://httpbin.org/get")
    assert s.status_code == 200
    assert s.json()["headers"]["User-Agent"].startswith("python-requests/")
    assert s.json()["url"] == "https://httpbin.org/get"

    # test raise_for_status is set
    s = session.get("https://httpbin.org/status/404")
    assert s.status_code == 404

    session2 = build_requests_session(raise_for_status=False)
    s = session2.get("https://httpbin.org/status/404")
    assert s.status_code == 404

    # test retry
    session3 = build_requests_session(retry=3)


# Generated at 2022-06-14 05:03:03.223800
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    import cdr_cleaner.test.test_utils as tu

    class TestLoggedFunctionCall(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            logging.config.dictConfig(
                tu.logging_config_dict("OFF", "logs/test_utils_log.log")
            )
            cls.logger = logging.getLogger("test_utils")

        def test_logged_func_1(self):
            @LoggedFunction(TestLoggedFunctionCall.logger)
            def testcase_1():
                return "test case 1"

            result = testcase_1()
            TestLoggedFunctionCall.logger.info(result)
            TestLoggedFunctionCall.logger.warning("test case 1 complete")

# Generated at 2022-06-14 05:03:14.586752
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        def __init__(self):
            self.logs = []

        def debug(self, s):
            self.logs.append(s)

    func = lambda x, y, z=3: x + y + z
    func.__name__ = "func"
    logger = Logger()
    logged_func = LoggedFunction(logger)(func)
    assert logged_func(1, 2) == 6
    assert "func(1, 2)" in logger.logs[0]
    assert "func -> 6" in logger.logs[1]

    logger.logs.clear()
    assert logged_func(1, 2, z=5) == 8
    assert "func(1, 2, z=5)" in logger.logs[0]
    assert "func -> 8" in logger.log

# Generated at 2022-06-14 05:03:34.849471
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import tempfile
    import os.path

    with tempfile.TemporaryDirectory() as tempdir:
        logfile = os.path.join(tempdir, "test.log")
        logging.basicConfig(
            filename=logfile,
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
        )

        lf=LoggedFunction(logging)

        @lf
        def add(a:int,b:int):
            return a+b

        add(1,2)

        with open(logfile) as f:
            lines = f.readlines()
            assert len(lines) == 2
            assert lines[0].strip()=="add(1, 2)"

# Generated at 2022-06-14 05:03:44.189119
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    logger = Mock()
    decorated_func = LoggedFunction(logger)(lambda a, b: a + b)
    decorated_func(1, 2)
    decorated_func(1, 2, 3)
    decorated_func("aa", "bb")
    decorated_func("aa", "bb", "cc")
    decorated_func("xx", "yy", c="zz")
    assert logger.debug.call_count == 6
    assert logger.debug.call_args_list[0][0] == ("lambda(1, 2)")
    assert logger.debug.call_args_list[1][0] == (
        "lambda(1, 2, 3)"
    )
    assert logger.debug.call_args_list[2][0] == ("lambda('aa', 'bb')")
   

# Generated at 2022-06-14 05:03:57.102339
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    from unittest.mock import Mock  # type: ignore

    mock_logger = Mock()

    @LoggedFunction(mock_logger)
    def foo(param1: object, param2: object = "default") -> str:
        return f"foo({param1}, {param2})"

    foo(param1=1, param2=2)
    assert mock_logger.debug.call_count == 2
    assert mock_logger.debug.call_args_list == [
        (("foo(1, 2)",), {}),
        (("foo -> foo(1, 2)",), {}),
    ]

    foo(param1="John", param2="Doe")
    assert mock_logger.debug.call_count == 4
    assert mock_logger.debug.call_args

# Generated at 2022-06-14 05:04:01.261274
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logged_func = LoggedFunction.__call__(LoggedFunction(logging.getLogger()), lambda x: x)
    logged_func(1)
    logged_func(1, 2)
    logged_func(1, 2, 3)
    logged_func(x=1)
    logged_func(1, 2, x=1)
    logged_func(x=1, y=2)
    logged_func(1, 2, 3, x=1, y=2)



# Generated at 2022-06-14 05:04:13.205557
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import sys
    import io
    import logging
    import contextlib
    import unittest
    import functools
    import requests

    @LoggedFunction(logging.getLogger("test"))
    def add(x, y):
        return x + y

    @LoggedFunction(logging.getLogger("test"))
    def get_webpage():
        return requests.get("https://www.google.com").text

    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr

# Generated at 2022-06-14 05:04:15.364779
# Unit test for function build_requests_session
def test_build_requests_session():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    session = build_requests_session()
    print(session)


# Generated at 2022-06-14 05:04:28.507033
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Arrange
    import unittest.mock as mock
    logger = mock.Mock()
    decorator = LoggedFunction(logger)
    func = mock.Mock(__name__="function_name")

    # Act
    logged_func = decorator(func)

    # Assert

    # Check that __call__ creates a logged function
    logged_func(1, 2, 3)
    logger.debug.assert_called_once_with(
        "function_name(1, 2, 3)"
    )  # Check that function name and arguments were logged

    func.assert_called_once_with(1, 2, 3)  # Check that function was called

    # Check that return value is logged
    func.return_value = "return value"
    logged_func(1, 2, 3)
    logger.debug

# Generated at 2022-06-14 05:04:39.474093
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import Logger
    from unittest import TestCase, mock
    from unittest.mock import Mock

    class TestLogger(Logger):
        def __init__(self):
            super().__init__(name="LoggedFunctionTest")
            self.log = Mock()

    def test_func_1(a, b):
        return f"{a} {b}"

    def test_func_2(a, b, c):
        return f"{a} {b} {c}"

    def test_func_3(a, b, c=None):
        return f"{a} {b} {c}"

    def test_func_4(a="a", b="b", c=None):
        return f"{a} {b} {c}"


# Generated at 2022-06-14 05:04:45.319702
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger, INFO
    import unittest

    logger = getLogger("test")
    logger.setLevel(INFO)

    def test_func(a, b, c=3, d=4):
        return a + b + c + d

    logged_test_func = LoggedFunction(logger)(test_func)
    result = logged_test_func(1, 2)
    assert result == 10



# Generated at 2022-06-14 05:04:58.203862
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self) -> None:
            self.logger = logging.getLogger(__name__)

        def test__call__LoggedFunction(self):
            logger = self.logger
            logger.setLevel(logging.DEBUG)
            test_handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            test_handler.setFormatter(formatter)
            logger.addHandler(test_handler)

            @LoggedFunction(logger)
            def add(x, y):
                return x + y

            add(1, 1)

# Generated at 2022-06-14 05:05:31.151625
# Unit test for function build_requests_session
def test_build_requests_session():
    # test default
    session = build_requests_session()
    assert hasattr(session, "hooks")
    assert session.hooks["response"][0].__name__ == "raise_for_status"
    assert session.adapters is not None
    assert isinstance(session.adapters["http://"].max_retries, Retry)
    assert isinstance(session.adapters["https://"].max_retries, Retry)
    # test raise_for_status
    session = build_requests_session(raise_for_status=False)
    assert not hasattr(session, "hooks")
    assert session.adapters is not None
    assert isinstance(session.adapters["http://"].max_retries, Retry)

# Generated at 2022-06-14 05:05:43.518667
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Define test
    test_function_name = "test_function_name"
    test_args_list = ["arg_a", "arg_b", "arg_c"]
    test_args_kwargs = {"kwarg_a": "value_a", "kwarg_b": "value_b"}
    log_text_expectation = "test_function_name(arg_a, arg_b, arg_c, kwarg_a=value_a, " \
                           "kwarg_b=value_b)"
    result_expectation = "test"

    # Define logger
    test_logger = logging.getLogger("loggedfunction-test")
    test_logger.setLevel(logging.DEBUG)

    # Init LoggedFunction object

# Generated at 2022-06-14 05:05:53.220561
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    log_handler = logging.StreamHandler()
    class TestLogger:
        def __init__(self):
            self.logger = logging.getLogger("TestLogger")
            self.logger.addHandler(log_handler)
            self.logger.setLevel(logging.DEBUG)
            self.logs = []
        def debug(self, msg):
            self.logger.debug(msg)
            self.logs.append(msg)
    logger = TestLogger()
    @LoggedFunction(logger)
    def test_func(arg1, arg2):
        return "test result"
    test_func(1, "test string")

# Generated at 2022-06-14 05:06:03.563861
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Unit test for method __call__ of class LoggedFunction
    """
    import os
   
    class FakeLogger:
        """
        Fake logger class
        """
        def debug(self, message):
            print(message)
    
    def fake_function(a, b, c):
        """
        A fake function for testing LoggedFunction decorator
        """
        return a+b+c
    
    fake_function_decorated = LoggedFunction(FakeLogger())(fake_function)

    fake_function_decorated(1,2,3)
    fake_function_decorated(a=3, c=2, b=1)



# Generated at 2022-06-14 05:06:16.441090
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    import unittest

    class DummyLogger:
        def __init__(self):
            self.log = []

        def debug(self, message):
            self.log.append(message)

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.logger = DummyLogger()
            self.log_decorator = LoggedFunction(self.logger)

        def test_logging_without_args_nor_kwargs(self):
            def foo():
                return

            logged_foo = self.log_decorator(foo)
            logged_foo()
            self.assertEqual(self.logger.log, ["foo()"])


# Generated at 2022-06-14 05:06:27.484124
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Prepare data
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addFilter(lambda x: x.name == __name__)
    func = lambda x, y: x + y
    args = (1, 2)
    kwargs = {
        "z": 3
    }
    # Execute test
    obj = LoggedFunction(logger)
    result = obj(func)(*args, **kwargs)

# Generated at 2022-06-14 05:06:38.288334
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    # Mocked logging handler
    handler = logging.handlers.BufferingHandler(capacity=1024)

    # Mock logger to use handler
    logger = logging.getLogger("test")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Create a LoggedFunction and invoke it
    log_f = LoggedFunction(logger)
    f = log_f(lambda x: x + 1)
    r = f(3)

    # Check output was as expected
    assert r == 4
    assert len(handler.buffer) == 1
    assert handler.buffer[0].getMessage() == "f(3) -> 4"

# Generated at 2022-06-14 05:06:50.800074
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Test if function name and arguments are logged before function call
    # Test if result is logged after function call
    def test(a: int, b: str, *args, **kwargs):
        return "result"

    from logging import getLogger
    from io import StringIO
    from contextlib import redirect_stdout

    # Use StringIO as buffer for standard output to avoid logging output
    # to file or command-line console.
    f = StringIO()
    with redirect_stdout(f):
        decorated_test = LoggedFunction(getLogger("test"))(test)
        assert decorated_test(5, "string", 6, 7, c=8, d=9) == "result"

# Generated at 2022-06-14 05:06:58.553704
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("LoggedFunction__call__")
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def foo(a, b=2, c=3, d: int = 4, e: str = "five"):
        return a + b + c + d + int(e)

    logger.info(foo(1, 2, 3, 4, 5))
    logger.info(foo(1, b=2, c=3, d=4, e=5))

# Generated at 2022-06-14 05:07:09.408872
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Debugging in python, "while-else" loop, p.180
    class TestLogger:
        def __init__(self):
            self.messages = []

        def debug(self, message):
            self.messages.append(message)

        def assert_debug_log(self, pattern):
            for message in self.messages:
                if re.match(pattern, message):
                    return
            assert False, \
                f"no debug log matches '{pattern}'."

    def add(x, y):
        return x + y

    def max_of_three(x, y, z):
        return max([x, y, z])

    logger = TestLogger()

    logged_add = LoggedFunction(logger)(add)