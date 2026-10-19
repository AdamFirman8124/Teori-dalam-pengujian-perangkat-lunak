

# Generated at 2022-06-14 04:57:39.767726
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    # Create a test logger which writes to the console.
    class TestLogger(logging.Logger):
        def debug(self, msg, *args, **kwargs):
            print(msg)

    test_logger = TestLogger("test_logger")
    test_logger.setLevel(logging.DEBUG)
    test_logger.propagate = False

    # Create a test handler which logs messages to the console.
    class TestHandler(logging.Handler):
        def emit(self, record):
            print(record.getMessage())

    test_handler = TestHandler()
    test_handler.setLevel(logging.DEBUG)

    # Add the test handler to the logger
    test_logger.addHandler(test_handler)

    # log function

# Generated at 2022-06-14 04:57:47.447853
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

    def sum(a, b):
        return a + b

    decorated = LoggedFunction(logger)(sum)
    assert decorated(1, 2) == 3
    assert decorated(1, b=2) == 3
    assert decorated(b=2, a=1) == 3

# Generated at 2022-06-14 04:57:51.517047
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # import logging
    # logging.basicConfig(level=logging.DEBUG)
    # logger = logging.getLogger("test_LoggedFunction")
    #
    # @LoggedFunction(logger)
    # def add1(a, b):
    #     return a + b
    #
    # add1([3, 5, 7], [3, 5, 7])
    # add1(1, 2)
    # add1("hello", "world")
    # add1({"a": 1, "b": 2}, {"c": 3})
    pass

# Generated at 2022-06-14 04:57:56.988047
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import tempfile
    import sys
    log_file = tempfile.NamedTemporaryFile(mode='w', prefix='loggedFunction', delete=False)
    log_file.close()
    logging.basicConfig(
        filename=log_file.name, filemode="w", level=logging.DEBUG, format='%(message)s'
    )
    logger = logging.getLogger(__name__)
    logged_function = LoggedFunction(logger)
    def foo(a, b, c="d", d=1):
        return a+b+c

    logged_function(foo)
    with open(log_file.name) as f:
        for line in f:
            if "foo(" in line:
                assert line == "foo(1, 2, c='d', d=1)", f

# Generated at 2022-06-14 04:57:59.860269
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert isinstance(session, Session)
    assert len(session.adapters) == 2

# Generated at 2022-06-14 04:58:09.830449
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    import sys
    import io

    class TestLoggedFunction(unittest.TestCase):
        def test_call(self):
            logger = logging.getLogger('test')
            logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.propagate = False

            string_io = io.StringIO()


# Generated at 2022-06-14 04:58:18.580114
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO

    log_capture_string = StringIO()
    log_handler = logging.StreamHandler(log_capture_string)
    logger = logging.getLogger("logged")
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    @LoggedFunction(logger)
    def test_function(a, b):
        return a + b

    test_function(1, 2)
    assert "test_function(1, 2)" in log_capture_string.getvalue()
    assert "test_function -> 3" in log_capture_string.getvalue()

# Generated at 2022-06-14 04:58:27.711924
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert session.max_redirects == 30  # Verify default value
    assert session.adapters["http://"].max_retries.total == 0  # Verify default value
    session = build_requests_session(retry=False)
    assert session.adapters["http://"].max_retries.total == 0  # Verify default value
    assert session.adapters["https://"].max_retries.total == 0  # Verify default value
    session = build_requests_session(retry=4)
    assert session.adapters["http://"].max_retries.total == 4  # Verify default value
    assert session.adapters["https://"].max_retries.total == 4  # Verify default value

# Generated at 2022-06-14 04:58:40.535853
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import sys
    from contextlib import redirect_stdout

    with io.StringIO() as buf, redirect_stdout(buf):
        def add(x, y):
            return x + y

        logger = LoggedFunction(logging.getLogger(__name__))
        add_log = logger(add)

        result = add_log(1, 2)
        assert result == 3
        assert buf.getvalue() == "add(1, 2)\n"

        result = add_log(1, 2, 3)
        assert result == 3
        assert buf.getvalue() == "add(1, 2)\n"

        result = add_log(x=2, y=1)
        assert result == 3

# Generated at 2022-06-14 04:58:54.060622
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    class MockLogger:
        def _log(self, level, msg, args, exc_info=None, extra=None):
            if level == logging.DEBUG:
                assert msg == "test_func(1, hello, x=1.9, y=2, z=3)"
                assert result == "test_result"
            elif level == logging.DEBUG:
                assert msg == "test_func -> test_result"
                assert result == "test_result"

    @LoggedFunction(logger=MockLogger())
    def test_func(a: int, b: str, x=1.1, y=2, z=3):
        return "test_result"

    result = test_func(1, "hello")


if __name__ == "__main__":
    test

# Generated at 2022-06-14 04:59:09.832981
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert session
    assert session.adapters
    session = build_requests_session(raise_for_status=False)
    assert "response" not in session.hooks
    session = build_requests_session(retry=False)
    assert not session.adapters
    session = build_requests_session(retry=1)
    assert isinstance(session.adapters["http://"].max_retries, Retry)
    session = build_requests_session(retry=Retry())
    assert isinstance(session.adapters["http://"].max_retries, Retry)
    try:
        session = build_requests_session(retry=object())
        assert False
    except:
        pass



# Generated at 2022-06-14 04:59:17.305823
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import sys

    from unittest import TestCase

    # Create fake logger
    out = io.StringIO()
    logger = type("FakeLogger", (object,), {"debug": lambda s, x: print(x, file=out)})

    @LoggedFunction(logger)
    def test_func(a, b: int, c="foo", d=None):
        pass

    test_func("bar", b=3.14)

    # Check output
    exp = "test_func('bar', b=3.14, c='foo', d=None)\n"
    assert out.getvalue() == exp, repr(out.getvalue()) + ", " + repr(exp)

# Generated at 2022-06-14 04:59:20.658857
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    @LoggedFunction(logger)
    def add(x: int, y: int) -> int:
        return x + y

    assert add(1, 2) == 3



# Generated at 2022-06-14 04:59:28.811815
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    test_logger = MagicMock()
    testFunc = LoggedFunction(test_logger)
    func = testFunc(sum([1,2]))
    func(1,2)
    test_logger.debug.assert_not_called()
    func()
    test_logger.debug.assert_called_once_with("sum((1, 2), (1, 2))")

    test_logger = MagicMock()
    testFunc = LoggedFunction(test_logger)
    func = testFunc(sum)
    func(1,2,3)
    test_logger.debug.assert_called_once_with("sum(1, 2, 3)")

# Generated at 2022-06-14 04:59:41.882096
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert session["http://localhost"]
    assert session["https://localhost"]

    session = build_requests_session(retry=False)
    assert not session["http://localhost"]
    assert not session["https://localhost"]

    session = build_requests_session(retry=0)
    assert session["http://localhost"]
    assert session["https://localhost"]

    session = build_requests_session(retry=2)
    assert session["http://localhost"]
    assert session["https://localhost"]

    retry = Retry(total=3)
    session = build_requests_session(retry=retry)
    assert session["http://localhost"]
    assert session["https://localhost"]

    with pytest.raises(ValueError) as excinfo:
        build_

# Generated at 2022-06-14 04:59:48.445474
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Arrange
    import logging
    logger = logging.getLogger("test")
    logged_func = LoggedFunction(logger)
    def func(*args, **kwargs):
        return 2*args[0]*kwargs["b"]
    args = (1, 2)
    kwargs = {"b": 2}

    # Act
    callable_func = logged_func(func)
    res = callable_func(*args, **kwargs)
    print(res)

    # Assert
    assert res == 8

# Generated at 2022-06-14 05:00:00.828714
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def func1(x: int, y: int, z: str):
        return x + y

    def func2(x: int, y: int, z: str):
        return None

    lfunc1 = LoggedFunction(logger=None)(func1)
    lfunc2 = LoggedFunction(logger=None)(func2)

    assert lfunc1(1, 2, "z") == func1(1, 2, "z")
    assert lfunc1(1.1, 2.2, "z") == func1(1.1, 2.2, "z")
    assert lfunc2(1, 2, "z") == func2(1, 2, "z")
    assert lfunc1(1, y=2, z="z") == func1(1, y=2, z="z")
    assert lfunc1

# Generated at 2022-06-14 05:00:07.068006
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import patch
    logger = patch("logging.getLogger")
    f = LoggedFunction(logger)
    f(lambda x: x + 1)(1)
    logger.debug.assert_called_with("<lambda>(1)")
    logger.debug.assert_called_with("<lambda> -> 2")

# Generated at 2022-06-14 05:00:17.583232
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    from contextlib import contextmanager

    @LoggedFunction(logging.getLogger(__name__))
    def foo(bar, baz="test"):
        return "foo"

    # Decorated function returns correct value
    assert foo(1) == "foo"

    # Decorated function was called with correct arguments
    with assert_log_output(level=logging.DEBUG) as log_stream:
        foo(1)
    assert "foo(1, baz='test')" in log_stream.getvalue()

    # Logging output contains return value
    with assert_log_output(level=logging.DEBUG) as log_stream:
        foo(1)
    assert "foo -> foo" in log_stream.getvalue()


# Generated at 2022-06-14 05:00:28.860057
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def str_cat(s1, s2, s3):
        return s1 + s2 + s3

    @LoggedFunction(logger)
    def int_sum(n1, n2):
        return n1 + n2

    @LoggedFunction(logger)
    def no_return():
        print("no return")

    str_cat("s1", "s2", "s3")
    int_sum(123, 456)
    no_return()

# Generated at 2022-06-14 05:00:45.873747
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    logger = logging.getLogger('poli')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    def test_func(a, b):
        return a+b
    decorated_func = LoggedFunction(logger)(test_func)
    decorated_func(1,2)
    decorated_func(2,4)
    decorated_func(1,6)
    decorated_func(3,6)

# Generated at 2022-06-14 05:00:55.902668
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import tempfile
    import os

    log_filename = "test_LoggedFunction.log"
    logger = logging.getLogger('LoggedFunction')
    
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.DEBUG)

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

# Generated at 2022-06-14 05:01:01.276328
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger('test_LoggedFunction')
    logger.setLevel(logging.DEBUG)
    logger.info('Begin testing LoggedFunction.__call__')
    @LoggedFunction(logger=logger)
    def test_function(x, y):
        return x + y
    test_function(1,2)
    logger.info('Finish testing LoggedFunction.__call__')

if __name__ == '__main__':
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:01:07.591830
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger
    from io import StringIO
    from logging import DEBUG
    from logging import StreamHandler

    stream = StringIO()
    handler = StreamHandler(stream)
    handler.setLevel(DEBUG)
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    @LoggedFunction(logger=logger)
    def foo(a, b):
        return 'bar'

    foo(1, 2)
    stream.seek(0)
    assert stream.getvalue().strip() == 'DEBUG:__main__:foo(1, 2) -> bar'

# Generated at 2022-06-14 05:01:14.924411
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MockLogger:
        def debug(self, message):
            print(message)
    mockLogger = MockLogger()
    loggedFunction = LoggedFunction(mockLogger)
    @loggedFunction
    def test(x, y="world", z=123):
        pass
    test(1, y=2, z=3)

# test_LoggedFunction___call__()



# Generated at 2022-06-14 05:01:21.732982
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logbook

    logger = logbook.Logger("logbook")

    @LoggedFunction(logger)
    def f(a, b, c='baz'):
        """
        This is a docstring.
        """
        pass

    assert f.__doc__ == "This is a docstring."
    assert f.__name__ == "f"
    assert f.__qualname__ == "test_LoggedFunction___call__.<locals>.f"

    f('foo', 'bar')

    assert logger.handlers[0].records[0].level_name == 'DEBUG'
    assert logger.handlers[0].records[0].message == "f('foo', 'bar', c='baz')"

# Generated at 2022-06-14 05:01:34.165311
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io

    class FakeLogger:
        def __init__(self):
            self.stream = io.StringIO()
            self.log = [ ]
        def debug(self, message):
            self.stream.write(message)
            self.log.append(message)
    def test_function(message, *args):
        return message
    def test_function_args(message, *args):
        return args
    def test_function_kwargs(message, **kwargs):
        return kwargs
    def test_function_args_kwargs(message, *args, **kwargs):
        return (args, kwargs)
    def test_function_no_return(message):
        pass
    def test_function_multiple_return(a, b, c):
        return a, b, c

    fake_

# Generated at 2022-06-14 05:01:46.468751
# Unit test for function build_requests_session
def test_build_requests_session():
    from http.client import HTTPSConnection, HTTPConnection

    session = build_requests_session(raise_for_status=False, retry=False)
    session.get("https://httpbin.org/status/404")
    assert type(session.adapters["https://"].max_retries) == Retry
    assert session.adapters["https://"].max_retries.total == 0
    assert type(session.adapters["http://"].max_retries) == Retry
    assert session.adapters["http://"].max_retries.total == 0
    assert type(session.adapters["https://"].pool_connections) == int
    assert type(session.adapters["https://"].pool_maxsize) == int
    assert type(session.adapters["https://"].pool_block) == bool


# Generated at 2022-06-14 05:01:57.943688
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from contextlib import redirect_stdout
    from io import StringIO
    import logging
    import sys

    import pytest

    # Redirect stderr
    err = StringIO()
    with redirect_stdout(err):
        logger = logging.getLogger("test")
        logger.setLevel(logging.DEBUG)

    # Create test function
    @LoggedFunction(logger)
    def test_func(x, y, z=7):
        return x + y + z

    # Test
    assert test_func(1, 2, z=3) == 6
    test_func(1, 2)

    # Test logging
    assert err.getvalue() == "test_func(1, 2, z=3)\n" + "test_func -> 6\n"
    err.close()

    # Test exceptions


# Generated at 2022-06-14 05:02:05.009188
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # class MockLogger:
    #     def __init__(self):
    #         self.debug_logs = []
    #     def debug(self, msg):
    #         self.debug_logs.append(msg)
    # test_logger = MockLogger()
    # logged_f = LoggedFunction(test_logger)
    # def f(x,y):
    #     return x + y
    # assert logged_f(f)(1,2) == 3
    assert True


# Generated at 2022-06-14 05:02:24.564395
# Unit test for function build_requests_session
def test_build_requests_session():
    # test Retry parameter is True
    session = build_requests_session(retry=True)
    assert session.max_retries.keep_alive == Retry.DEFAULT_BACKOFF_FACTOR
    # test Retry parameter is integer
    session = build_requests_session(retry=10)
    assert session.max_retries.total == 10
    # test Retry parameter is Retry instance
    retry = Retry(total=3, backoff_factor=10)
    session = build_requests_session(retry=retry)
    assert session.max_retries.total == retry.total
    assert session.max_retries.backoff_factor == retry.backoff_factor

# Generated at 2022-06-14 05:02:30.558922
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())
    logged_func = LoggedFunction(logger)(sum)
    logged_func(1, 2, 3)
    logged_func(1, 2, 3, c=4, d=5)

# Generated at 2022-06-14 05:02:40.969452
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Preparing test
    from pytest import fixture
    from unittest.mock import Mock

    from logging import DEBUG, Formatter, StreamHandler, basicConfig

    @fixture
    def logger():
        """
        Fixture which returns a mock logger.
        """
        basicConfig(format="%(levelname)s: %(message)s")
        logger = Mock()
        logger.propagate = False
        logger.setLevel(DEBUG)
        handler = StreamHandler()
        handler.setFormatter(Formatter("%(levelname)s: %(message)s"))
        logger.addHandler(handler)
        return logger

    def add(x: int, y: int) -> int:
        return x + y

    decorator = LoggedFunction(logger())

    # Executing test
    func = decorator(add)

# Generated at 2022-06-14 05:02:51.532458
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def foo(a, b=1, c=None):
        return a + b + c

    class FakeLogger:
        def __init__(self):
            self.logged = []

        def debug(self, msg):
            self.logged.append(msg)

    logger = FakeLogger()
    logged_func = LoggedFunction(logger)(foo)
    assert logged_func.__name__ == "foo"
    assert logged_func(1, 2, 3) == 6
    assert logger.logged[0] == "foo(1, 2, 3)"
    assert logger.logged[1] == "foo -> 6"

# Generated at 2022-06-14 05:03:02.180618
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import exceptions as req_exceptions

    ses = build_requests_session(False, False)
    assert not hasattr(ses.hooks, "response")
    assert not hasattr(ses, "max_retries")
    ses = build_requests_session(True, False)
    assert hasattr(ses.hooks, "response")
    assert not hasattr(ses, "max_retries")
    ses = build_requests_session(False, True)
    assert not hasattr(ses.hooks, "response")
    assert hasattr(ses, "max_retries")
    ses = build_requests_session(True, True)
    assert hasattr(ses.hooks, "response")
    assert hasattr(ses, "max_retries")

    s = build_requests_

# Generated at 2022-06-14 05:03:12.214610
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(stream=io.StringIO())
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def func1(a, b, c=3, d="4"):
        return a + b + c

    func1(1, 2)
    func1(a=1, b=2, c=4)
    func1(1, d="5", b=2)

    # print(handler.stream.getvalue())



# Generated at 2022-06-14 05:03:24.844351
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import unittest.mock
    from logging import getLogger
    from kubernetes.config.incluster_config import _LoggedFunction

    class Logger:
        def __init__(self):
            self.debug_messages = []
            self.exception_messages = []

        def debug(self, debug_message):
            self.debug_messages.append(debug_message)

        def exception(self, exception_message):
            self.exception_messages.append(exception_message)

    @LoggedFunction(getLogger("kubernetes.client.log"))
    def func():
        pass

    logger = Logger()
    func.log_logger = logger

    # Test 1: Just a function name is logged
    func()
    assert logger.debug

# Generated at 2022-06-14 05:03:33.377988
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def hello(name):
        return f"Hello {name}"

    def hello1(name, age=18):
        return f"Hello {name}"

    class Logger:
        def debug(self, message):
            print(message)

    logger = Logger()
    logged_func1 = LoggedFunction(logger)(hello)
    assert logged_func1.__name__ == "hello"
    logged_func1("Viki")

    logged_func2 = LoggedFunction(logger)(hello1)
    assert logged_func2.__name__ == "hello1"
    logged_func2("Viki", age=18)

test_LoggedFunction___call__()

# Generated at 2022-06-14 05:03:38.730743
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger()

    def func(*args, **kwargs):
        pass

    logged_func = LoggedFunction(logger).__call__(func)
    logged_func("arg1", "arg 2", kwarg1="kwarg 1", kwarg2="kwarg 2")
    # TODO: test if log messages are correct.

# Generated at 2022-06-14 05:03:45.102825
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Setup the test
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    logged_function = LoggedFunction(logger)

    # Define a test function and call it
    @logged_function
    def test_func(a, b, c, d=5):
        return str(a) + str(b)

    result = test_func(1, 2, 3)
    assert result == "12"
    result = test_func(1, "2", c=3)
    assert result == "12"
    result = test_func(d=6, c=3, a=1, b=2)
    assert result == "12"



# Generated at 2022-06-14 05:04:16.794396
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Test the case func has no input arguments and return value
    def func():
        pass
    logger = logging.getLogger()
    logged_func = LoggedFunction(logger)(func)
    logged_func()
    # Test the case func has input arguments and return value
    def func(x, y):
        return x + y
    logged_func = LoggedFunction(logger)(func)
    assert logged_func(4, 5) == 9
    # Test the case func has input kwargs and no return value
    def func(x, y):
        pass
    logged_func = LoggedFunction(logger)(func)
    logged_func(x=4, y=5)
    # Test the case func has input kwargs and return value
    def func(x, y):
        return x + y
    logged_func = Logged

# Generated at 2022-06-14 05:04:25.471467
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logging.getLogger("test").setLevel(logging.DEBUG)
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    
    @LoggedFunction(logger)
    def test_function(a, b, c="", d=None):
        return f"{a}*{b}/{c}-{d}"

    test_function("Hi", "World", d=4)

# Generated at 2022-06-14 05:04:36.033694
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Test __call__ docstring

    class Test:
        @LoggedFunction(logger=print)
        def my_function(a: int, b: int = 0, c: str = "") -> str:
            return f"{a}-{b}-{c}"

        @LoggedFunction(logger=print)
        def my_function2(a: int, b: int = 0, c: str = ""):
            pass

    Test().my_function(1, 2, c="3")
    Test().my_function(1, c="3")
    Test().my_function(1, b="2")
    Test().my_function(1, c="3-4")
    Test().my_function2(1)
    Test().my_function2(b=3, a=1)

# Generated at 2022-06-14 05:04:44.923105
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from . import tst

    # Create logger
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())

    # Create decorator
    logged = LoggedFunction(logger)

    @logged
    def my_add(a, b):
        return a + b

    # Test with debug logging turned off
    logger.setLevel(logging.INFO)
    tst.assert_equals(my_add(1, 2), 3)

    # Test with debug logging turned on
    logger.setLevel(logging.DEBUG)
    tst.assert_equals(my_add(1, 2), 3)
    tst.assert_equals(my_add(b=4, a=7), 11)

# Generated at 2022-06-14 05:04:57.990329
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    from unittest import TestCase, main

    class LoggedFunctionTest(TestCase):

        def test_success(self):
            # Start with a standard logger at warning level
            logfile = StringIO()
            logger = logging.getLogger(self.__class__.__name__)
            logger.level = logging.WARNING
            handler = logging.StreamHandler(logfile)
            logger.addHandler(handler)

            # Create a sample object and make it loggable
            class SampleObj:
                @LoggedFunction(logger)
                def addition(self, a, b):
                    return a + b

            obj = SampleObj()
            args = [15, 10]
            result = obj.addition(*args)

            # Check the output

# Generated at 2022-06-14 05:05:03.063837
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Create a logger
    logger = logging.getLogger()
    # Create a LoggedFunction decorator based on the logger
    logged_function = LoggedFunction(logger)
    # Create a function
    @logged_function
    def addition(a, b):
        return a + b
    # Test
    addition(2, 3)

# Generated at 2022-06-14 05:05:15.124635
# Unit test for function build_requests_session
def test_build_requests_session():
    from functools import reduce
    from operator import mul

    with build_requests_session() as session:
        assert isinstance(session.adapters["http://"], HTTPAdapter)
        assert isinstance(session.adapters["https://"], HTTPAdapter)
        assert session.adapters["http://"].max_retries == Retry()
        assert session.adapters["https://"].max_retries == Retry()
        assert len(session.hooks["response"]) == 0
    with build_requests_session(retry=False) as session:
        assert not isinstance(session.adapters.get("http://"), HTTPAdapter)
        assert not isinstance(session.adapters.get("https://"), HTTPAdapter)

# Generated at 2022-06-14 05:05:20.143602
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    log_stream = io.StringIO()
    logging_handler = logging.StreamHandler(log_stream)
    logger.addHandler(logging_handler)

    @LoggedFunction(logger)
    def foo(i):
        return i + 1

    foo(1)

    log_stream.seek(0)
    log = log_stream.read().strip()
    logging_handler.close()
    assert log == "foo(1) -> 2"



# Generated at 2022-06-14 05:05:26.561326
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestLogger:
        @staticmethod
        def debug(msg):
            print(f"DEBUG: {msg}")

    @LoggedFunction(TestLogger())
    def foo(x, y, z=8):
        pass

    foo(3, 4)
    foo(3, 4, z=5)
    foo([3, 4], {"z": 7})


# Generated at 2022-06-14 05:05:35.548753
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    f = LoggedFunction(logging.getLogger())
    @f
    def func(a):
        """
        :param a: input argument
        :return: a
        """
        return a
    import logging
    logging.basicConfig(level=logging.DEBUG)
    func(1)
    func(1, 2)
    func(1, 2, 3)
    func(a=1)
    func(a=1, b=2)
    func(1, a=1, b=2)
    func(1, a=2, b=2)

    # Unit test for method __call__ of class LoggedFunction
    f = LoggedFunction(logging.getLogger())
    @f
    def func(a):
        """
        :param a: input argument
        :return: a
        """
       

# Generated at 2022-06-14 05:06:29.690614
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class FakeLogger:
        def __init__(self, name=None):
            self.log = []

        def debug(self, msg):
            self.log.append(msg)

    def my_sum(a, b):
        return a + b

    my_sum_logged = LoggedFunction(FakeLogger())(my_sum)
    assert my_sum_logged(1, 2) == 3
    assert my_sum_logged.__name__ == 'my_sum'
    assert my_sum_logged.__doc__ == 'Decorator which adds debug logging to a function.\n\n    The input arguments are logged before the function is called, and the\n    return value is logged once it has completed.\n\n    :param logger: Logger to send output to.\n    '

# Generated at 2022-06-14 05:06:39.951713
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    logger = logging.getLogger("functools")
    logger.setLevel("DEBUG")
    
    buffer = io.StringIO()
    handler = logging.StreamHandler(buffer)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def foo(a, b):
        return a + b

    foo(1, 2)
    foo("abc", "def")
    foo(1, b=2)

    buffer = buffer.getvalue()
    assert buffer.strip() == "foo(1, 2)\nfoo -> 3\nfoo('abc', 'def')\nfoo -> abcdef\nfoo(1, b=2)\nfoo -> 3"

# Generated at 2022-06-14 05:06:49.289979
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(retry=False)
    assert isinstance(session, Session)
    assert session.hooks == {}
    assert len(session.adapters) == 2
    assert "http://" in session.adapters
    assert "https://" in session.adapters
    assert not isinstance(session.adapters["http://"], HTTPAdapter)
    assert not isinstance(session.adapters["https://"], HTTPAdapter)

    session = build_requests_session(retry=True)
    assert isinstance(session.adapters["http://"], HTTPAdapter)
    assert isinstance(session.adapters["https://"], HTTPAdapter)
    assert session.adapters["http://"].max_retries.total == 10
    assert session.adapters["https://"].max_retries.total == 10

    session

# Generated at 2022-06-14 05:06:57.958430
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import TestCase
    from unittest.mock import MagicMock
    from unittest.mock import call
    import logging

    logger = MagicMock(spec=logging.Logger)
    logged_function = LoggedFunction(logger=logger)

    @logged_function
    def a_function(*args, **kwargs):
        pass

    a_function(True, "argument", 123, a=1, b="b")
    assert logger.debug.call_args_list == [
        call(
            "a_function(True, 'argument', 123, a=1, b='b')",
        ),
        call(f"a_function -> None"),
    ]
    logger.reset_mock()


# Generated at 2022-06-14 05:07:01.604470
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from dcosdeploy.common.logger import get_logger

    logger = get_logger('unit_test')
    func = LoggedFunction(logger)(lambda a: a)
    func(3)



# Generated at 2022-06-14 05:07:08.421231
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    def test_function(num1, num2=100):
        return num1 + num2

    test_function_logged = LoggedFunction(logger)(test_function)

    assert test_function_logged(1, 2) == 3
    assert test_function_logged(1) == 101
    assert test_function_logged(num1=10, num2=20) == 30



# Generated at 2022-06-14 05:07:16.013282
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # an example function
    @LoggedFunction(logger)
    def add(a, b):
        return a + b

    class TestCase(unittest.TestCase):
        def test(self):
            self.assertEqual(add(1, 2), 3)

    unittest.main()

if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:07:26.495602
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    string_io = StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(string_io)
    logger.addHandler(stream_handler)

    # Test case
    @LoggedFunction(logger)
    def example(a, b, c=3, d="abc", e='"abc"', **kwargs):
        return a + b + c + len(d) + len(e)

    assert example(1, 2) == 8
    assert string_io.getvalue() == "example(1, 2, c=3, d='abc', e='\"abc\"')\n"
    string_io.truncate(0)
    string_io.seek(0)

# Generated at 2022-06-14 05:07:39.234984
# Unit test for function build_requests_session
def test_build_requests_session():
    try:
        build_requests_session(retry=1.0)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "build_requests_session() should raise ValueError if param retry is not boolean, int or Retry instance."
        )
    try:
        build_requests_session(retry=Retry(total=1))
    except ValueError:
        pass
    else:
        raise AssertionError(
            "build_requests_session() should raise ValueError if param retry is not boolean, int or Retry instance."
        )
    try:
        build_requests_session(retry=Retry)
    except ValueError:
        pass