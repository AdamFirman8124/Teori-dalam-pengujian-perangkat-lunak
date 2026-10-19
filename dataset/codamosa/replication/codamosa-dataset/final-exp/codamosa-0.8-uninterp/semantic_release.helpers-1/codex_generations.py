

# Generated at 2022-06-14 04:57:40.044869
# Unit test for function build_requests_session
def test_build_requests_session():
    s = build_requests_session(retry=False)
    assert (
        s.adapters["http://"].max_retries.total == 0
    ), "Default max retry count should be 0"
    s = build_requests_session(retry=True)
    assert (
        s.adapters["http://"].max_retries.total == Retry().total
    ), "Default max retry count should be equal to default Retry()"
    s = build_requests_session(retry=Retry(3))
    assert (
        s.adapters["http://"].max_retries.total == 3
    ), "Max retry count should be equal to specified number"

# Generated at 2022-06-14 04:57:51.160992
# Unit test for function build_requests_session
def test_build_requests_session():
    s= build_requests_session()
    assert isinstance(s,Session)
    assert s.mounts == [("http://",HTTPAdapter(max_retries=Retry())),("https://",HTTPAdapter(max_retries=Retry()))]
    assert "response" in s.hooks

    s= build_requests_session(raise_for_status=False)
    assert not "response" in s.hooks
    s= build_requests_session(retry=False)
    assert not s.mounts

    retry= Retry(total=10)
    s= build_requests_session(retry=retry)
    assert s.mounts == [("http://",HTTPAdapter(max_retries=retry)),("https://",HTTPAdapter(max_retries=retry))]

# Generated at 2022-06-14 04:57:55.119589
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    import logging

    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def test_method(x, y=2, **kwargs):
        return x + y

    test_method(3)
    test_method(3, y=4)
    test_method(3, y=4, z=5)

# test_LoggedFunction___call__()

# Generated at 2022-06-14 04:58:07.140442
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        def __init__(self):
            self.debug_count = 0
            self.debug_args = []
            pass

        def debug(self, message):
            self.debug_count += 1
            self.debug_args.append(message)
            pass

    def foo(a, b, c=1, d=None):
        return a + b

    logger = Logger()
    logged_foo = LoggedFunction(logger)(foo)
    result = logged_foo(1, 2, d="abc")
    assert result == 3
    assert logger.debug_count == 2
    assert logger.debug_args == [
        "foo(1, 2, c=1, d='abc')",
        "foo -> 3",
    ]
    assert logged_foo.__name__ == "foo"

# Generated at 2022-06-14 04:58:18.098533
# Unit test for function build_requests_session
def test_build_requests_session():
    from unittest.mock import patch
    from requests.adapters import HTTPAdapter, DEFAULT_POOLSIZE
    from requests.packages.urllib3.util.retry import Retry

    session = build_requests_session()
    assert not session.hooks

    with patch("logging.Logger.warning") as mocked_warning:
        session = build_requests_session(retry=Retry(total=5, status_forcelist=[500]))
        assert session.adapters["http://"].max_retries.total == 5
        assert session.adapters["http://"].max_retries.status_forcelist == [500]
        assert session.adapters["http://"].max_retries.pool_blocklist == []
        assert mocked_warning.call_count == 0

# Generated at 2022-06-14 04:58:26.415178
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    logger = logging.getLogger("LoggedFunction")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(io.StringIO())
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def hello(arg):
        return f"hello {arg}"

    hello("world")

    handler.close()
    # Get the output of handler
    io.StringIO.getvalue(handler.stream)



# Generated at 2022-06-14 04:58:35.364376
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    class FakeLogger:
        def __init__(self):
            self.log_messages = []

        def debug(self, message):
            self.log_messages.append(message)

    logger = FakeLogger()

    # Test function without any arguments
    function_1 = LoggedFunction(logger)(lambda: "function_1")
    result = function_1()
    assert result == "function_1"
    assert logger.log_messages == [
        "function_1()",
        "function_1 -> function_1",
    ]

    # Test function with positional arguments
    logger.log_messages = []
    function_2 = LoggedFunction(logger)(lambda arg_1, arg_2: arg_1)
    result = function_2(1, 2)
    assert result == 1


# Generated at 2022-06-14 04:58:44.560735
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    class StreamHandler(logging.StreamHandler):
        """
        Wrapper around the StreamHandler class to make it easier to unit test
        that the logger is outputting the correct information.

        :param stream: The stream to output to.
        """

        def __init__(self, stream=None):
            super().__init__(stream=stream)
            self.output = []

        def emit(self, record):
            self.output.append(record)

        def clear(self):
            self.output = []

    # Create handler & logger
    handler = StreamHandler(sys.stdout)
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # Create function & decorator

# Generated at 2022-06-14 04:58:53.621709
# Unit test for method __call__ of class LoggedFunction

# Generated at 2022-06-14 04:59:01.770260
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import unittest
    import unittest.mock

    class Logger:
        def __init__(self):
            self.level = 30
            self.logs = []

        def setLevel(self, level):
            self.level = level

        def debug(self, msg):
            if self.level >= 10:
                self.logs.append(msg)

    class Test(unittest.TestCase):
        def test_logged_function(self):
            logger = Logger()
            logged_decorator = LoggedFunction(logger)

            @logged_decorator
            def add(a, b):
                return a + b

            add(1, 2)
            self.assertEqual(["add(1, 2) -> 3"], logger.logs)


# Generated at 2022-06-14 04:59:08.227162
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def func(a, b, c):
        pass

    @LoggedFunction(logger=None)
    def _(a, b, c):
        pass

    assert _.__name__ == func.__name__

# Generated at 2022-06-14 04:59:11.993169
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    @LoggedFunction(logging.getLogger('abc'))
    def test_func(a, b, c='c', d='d', e='e'):
        return 'result'
    test_func('1', 2, '3', '4')


# Generated at 2022-06-14 04:59:19.715986
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Response
    from unittest.mock import Mock

    s = build_requests_session()
    assert s.hooks == {"response": [lambda r, *args, **kwargs: r.raise_for_status()]}

    s = build_requests_session(retry=True)
    assert isinstance(s.adapters["http://"].max_retries, Retry)

    s = build_requests_session(retry=10)
    assert isinstance(s.adapters["http://"].max_retries, Retry)
    assert s.adapters["http://"].max_retries.total == 10

    retry = Retry(15)
    s = build_requests_session(retry=retry)

# Generated at 2022-06-14 04:59:25.407698
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("test")
    logger.addHandler(logging.NullHandler())
    decorator = LoggedFunction(logger)

    def func(x):
        return x

    logged_func = decorator(func)
    assert logged_func(2) == 2

    logged_func = decorator(lambda x: x)
    assert logged_func(2) == 2



# Generated at 2022-06-14 04:59:29.730567
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger('test logger')
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logged_func = LoggedFunction(logger)
    @logged_func
    def test(arg1, arg2, arg3):
        return arg1+arg2+arg3
    assert test('a', 2, "c") == "a2c"

# Generated at 2022-06-14 04:59:35.770422
# Unit test for function build_requests_session
def test_build_requests_session():
    assert isinstance(build_requests_session(), Session)
    assert isinstance(build_requests_session(retry=True), Session)
    assert isinstance(build_requests_session(retry=10), Session)
    assert isinstance(build_requests_session(raise_for_status=False), Session)


# Generated at 2022-06-14 04:59:40.402871
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import DEBUG, INFO, Formatter
    import logging
    from logging.handlers import RotatingFileHandler
    from datetime import datetime
    
    # Setup logger
    logging.basicConfig(filename='log.txt',
                        filemode='w',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=DEBUG)
    logger = logging.getLogger()

    # Test method __call__ of class LoggedFunction
    @LoggedFunction(logger)
    def add(x, y):
        return x+y
    add(1, 2)

    # Assert logger

# Generated at 2022-06-14 04:59:46.855601
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    class MockLogger:

        def __init__(self):
            self.output = ""

        def debug(self, message):
            if self.output:
                self.output = self.output + "\n"
            self.output = self.output + message

    def func(arg1, arg2, named=None):
        pass

    # Create a mock logger
    logger = MockLogger()

    # Create a LoggedFunction decorator
    logged_function = LoggedFunction(logger)

    # Apply decorator to function
    func_decorated = logged_function(func)

    # Call function with correct arguments
    func_decorated(1, 2)
    func_decorated(3, 4, named=5)

    # Call function with incorrect arguments

# Generated at 2022-06-14 04:59:59.073973
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Mock logger
    logger = Mock()
    logger.debug = Mock()

    # Test data
    args = [1, 2, "foo", "bar"]
    kwargs = {"baz": 3, "qux": 4}

    # Create LoggedFunction instance
    log_func = LoggedFunction(logger)

    # Define function to be logged
    def func(*func_args, **func_kwargs):
        return "return_value"

    # Decorate function
    logged_func = log_func(func)

    # Call logged function
    result = logged_func(*args, **kwargs)

    # Assert logger.debug() was called correctly, then return_value

# Generated at 2022-06-14 05:00:08.044772
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock

    logger = MagicMock()
    logged_func = LoggedFunction(logger)

    @logged_func
    def test_func(arg1, arg2, arg3="default", arg4=None):
        pass

    test_func("foo", 123)
    logger.debug.assert_called_with("test_func('foo', 123, arg3=default, arg4=None)")
    logger.debug.reset_mock()

    test_func("foo", 123, "new value", "new keyword")
    logger.debug.assert_called_with("test_func('foo', 123, arg3='new value', arg4='new keyword')")
    logger.debug.reset_mock()

# Generated at 2022-06-14 05:00:18.794961
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import sys, io
    import unittest
    import logging

    # Create a logger, with output sent to a string
    captured_output = io.StringIO()
    logger = logging.getLogger("captured")
    logger.addHandler(logging.StreamHandler(captured_output))

    def test_func(arg1, arg2 = "default"):
        return f"{arg1} {arg2}"
    
    import json
    with open("test_logger.json") as f:
        expect = json.loads(f.read())
    assert json.loads(captured_output.getvalue()) == expect
    # Close output
    captured_output.close()

    # Build output
    import random
    import time

# Generated at 2022-06-14 05:00:31.178568
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import numpy as np
    import logging
    import unittest
    import sys
    import io

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.capture_standard_output = io.StringIO()
            self.stdout = sys.stdout
            sys.stdout = self.capture_standard_output
            self.logger = logging.getLogger("test_logger")
            self.logger.addHandler(logging.StreamHandler())
            self.logger.setLevel(logging.DEBUG)
            self.logger.info("********** New test started **********")

        def test_LoggedFunction__call__DifferentTypesOfArguments(self):
            @LoggedFunction(self.logger)
            def test_function(*args):
                self

# Generated at 2022-06-14 05:00:40.880441
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    from unittest.mock import Mock

    class Test(unittest.TestCase):
        def test(self):
            logger = Mock(logging.Logger)
            logger.debug = Mock()

            @LoggedFunction(logger)
            def add(x, y):
                return x + y

            add(1, 2)
            self.assertEqual(logger.debug.call_count, 2)
            self.assertEqual(logger.debug.call_args_list[0][0][0], "add(1, 2)")
            self.assertEqual(logger.debug.call_args_list[1][0][0], "add -> 3")

    unittest.main()

# Generated at 2022-06-14 05:00:50.081327
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    logger = Mock()
    decorator = LoggedFunction(logger)

    @decorator
    def test_func(x, y, z=3):
        return x + y + z

    assert test_func(1, 2) == 6
    # method getLogger of class Logger
    logger.debug.assert_called_with(
        "test_func(1, 2, z=3)"
    )
    # method getLogger of class Logger
    logger.debug.assert_called_with("test_func(1, 2, z=3)")
    logger.debug.assert_called_with("test_func -> 6")



# Generated at 2022-06-14 05:01:00.544961
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    from contextlib import redirect_stdout

    class F:
        def f1(self):
            pass
    f = F()
    logger = logging.getLogger("LoggedFunction")
    logger.setLevel(logging.DEBUG)
    f1 = LoggedFunction(logger)(f.f1)
    buffer = StringIO()
    with redirect_stdout(buffer):
        f1()
    message = buffer.getvalue()
    assert "f1()" in message
    assert not message.endswith("f1()\n")

    def f2(arg, kwarg="kw"):
        return arg, kwarg

    f2 = LoggedFunction(logger)(f2)
    buffer = StringIO()
    with redirect_stdout(buffer):
        f2

# Generated at 2022-06-14 05:01:09.147178
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    import StringIO
    import random
    import string

    # Initialize logger
    s = StringIO.StringIO()
    handler = logging.StreamHandler(s)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # Generate random string
    rand_str = "".join(random.choices(string.ascii_lowercase, k=10))

    # Define function to test
    @LoggedFunction(logger)
    def add(x, y):
        return x + y

    # Call function and check output
    original_stdout

# Generated at 2022-06-14 05:01:20.099449
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from datetime import date
    from unittest import main, TestCase
    from contextlib import redirect_stdout
    from io import StringIO
    from logging import getLogger, DEBUG

    logger = getLogger()
    logger.setLevel(DEBUG)
    buffer = StringIO()
    with redirect_stdout(buffer):
        @LoggedFunction(logger)
        def f(a, b=1, *arg, **kwarg):
            pass

        f("abc", 2, "xyz", "XYZ")
        assert buffer.getvalue() == "DEBUG:root:f('abc', 2, 'xyz', kwarg='XYZ')\n"

        # call f again with different arguments and return value

# Generated at 2022-06-14 05:01:29.721206
# Unit test for function build_requests_session
def test_build_requests_session():
    from urllib3.exceptions import MaxRetryError

    try:
        from requests import __version__ as ver
    except ImportError:
        from pkg_resources import get_distribution

        ver = get_distribution("requests").version
    from distutils.version import StrictVersion

    if StrictVersion(ver) < StrictVersion("2.9"):
        return
    session = build_requests_session(raise_for_status=False, retry=False)
    assert session.adapters == {}
    assert session.hooks["response"] == []

    session = build_requests_session(raise_for_status=True, retry=False)
    assert session.adapters == {}
    assert session.hooks["response"][0].__name__ == "raise_for_status"

    session = build

# Generated at 2022-06-14 05:01:39.735142
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Create a dummy Logger, which logs everything to a StringIO for test purposes
    import io

    test_log = io.StringIO()
    logger = logging.Logger("test_class")
    logger.addHandler(logging.StreamHandler(test_log))
    logger.setLevel(logging.DEBUG)

    # Create a dummy function, which returns its argument
    def f(a, b, c=3):
        return a

    # Decorate f
    f = LoggedFunction(logger)(f)

    # Call f and check output to test_log
    d = f(5, 6, c=7)
    assert d == 5
    test_log_string = test_log.getvalue()
    assert "f(5, 6, c=7)" in test_log_string
    assert "f -> 5" in test

# Generated at 2022-06-14 05:01:51.002550
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import sys
    import io
    import unittest
    import logging

    class Logger:
        def __init__(self, level, reset_out):
            self.level = level
            self.reset_out = reset_out
        def debug(self, msg):
            if self.level == logging.DEBUG:
                self.reset_out.write("DEBUG\t%s\n" % msg)

    class TestFunction(unittest.TestCase):
        def setUp(self):
            self.reset_out = io.StringIO()
            self.old_out = sys.stdout
            sys.stdout = self.reset_out
            self.term_out = "\n"

        def tearDown(self):
            sys.stdout = self.old_out
            self.reset_out.close()


# Generated at 2022-06-14 05:02:07.623546
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    import pytest

    log_format = (
        "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)s %(funcName)s: %(message)s"
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(stream_handler)

    @LoggedFunction(logger)
    def test():
        print("Hello World!")

    test()

    @LoggedFunction(logger)
    def test1(arg):
        return arg


# Generated at 2022-06-14 05:02:16.320887
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestLogger:
        def debug(self, s):
            print(s)

    def test_func(arg1, arg2, arg3=3):
        return arg1 + arg2 + arg3

    logger = TestLogger()
    function_logger = LoggedFunction(logger)
    logged_func = function_logger(test_func)
    print(logged_func(1, 2, arg3=4))

# test_LoggedFunction___call__()

# Generated at 2022-06-14 05:02:24.643109
# Unit test for function build_requests_session
def test_build_requests_session():
    import os
    import logging
    import requests
    import time
    import uuid
    logger = logging.getLogger("test-logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(handler)
    url = os.getenv("API_BASE") + "/v1/message/send"
    r = build_requests_session()

# Generated at 2022-06-14 05:02:36.830701
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import logging
    import unittest.mock

    # Make a fake logger
    logger = logging.getLogger()
    logger.disabled = True
    log_stream = io.StringIO()
    logger.addHandler(logging.StreamHandler(log_stream))

    # Decorate and call a fake method
    logged_func = LoggedFunction(logger)(lambda x: x * x)
    result = logged_func(2, a=3)

    # Check that debug logging is output
    result = log_stream.getvalue()
    assert (
        result
        == "lambda(2, a='3')\n"
        "lambda(2, a='3') -> 4\n"
    )

# Generated at 2022-06-14 05:02:45.179297
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    # setup the test
    logger = logging.Logger("__main__.LoggedFunction")
    log_out = io.StringIO()
    logger.addHandler(logging.StreamHandler(strm=log_out))

    def test_func(a, b, c):
        return True

    logged_func = LoggedFunction(logger)(test_func)

    # run the function
    logged_func(a=1, b=2, c=3)

    # clean up the output log
    log_out.seek(0)
    log_lines = log_out.read().splitlines()
    log_out.close()

    # assert the results
    assert len(log_lines) == 2
    assert log_lines[0] == "test_func(1, 2, 3)"
   

# Generated at 2022-06-14 05:02:57.214556
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from io import StringIO
    from unittest import TestCase
    from unittest.mock import patch, mock_open, Mock, MagicMock
    import logging

    class TestLoggedFunction(TestCase):
        def setUp(self):
            self.log_file = StringIO()
            self.logger = logging.getLogger()
            self.logger.handlers = []
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(logging.StreamHandler(self.log_file))

        def test_logging(self):
            @LoggedFunction(self.logger)
            def basic(**kwargs):
                return kwargs

            basic(a=1, b=2, c=3)


# Generated at 2022-06-14 05:03:07.097674
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # noinspection PyUnusedLocal
    @LoggedFunction(logger)
    def test_func(param1, param2):
        return "return value"
    test_func.__name__ = "test_func"

    assert test_func("string1", "string2") == "return value"

    assert test_func.__name__ == "test_func"
    assert test_func.__doc__ == None
    assert test_func.__annotations__ == {}


# Generated at 2022-06-14 05:03:17.639331
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        last_warning = None
        warnings = []
        last_debug = None
        debugs = []
        last_info = None
        infos = []
        last_error = None
        errors = []

        def warning(self, msg):
            self.last_warning = msg
            self.warnings.append(msg)

        def debug(self, msg):
            self.last_debug = msg
            self.debugs.append(msg)

        def info(self, msg):
            self.last_info = msg
            self.infos.append(msg)

        def error(self, msg):
            self.last_error = msg
            self.errors.append(msg)

    logger = Logger()
    logged_function = LoggedFunction(logger)

# Generated at 2022-06-14 05:03:20.053901
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    method = LoggedFunction(logger=None)
    result = method.__call__(func=lambda x: x)
    assert result(1) == 1

# Generated at 2022-06-14 05:03:22.040151
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger()
    log_func = LoggedFunction(logger)
    @log_func
    def add(x, y):
        return x + y
    assert add(1, 2) == 3

# Generated at 2022-06-14 05:03:42.152213
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    logger.propagate = False

    @LoggedFunction(logger)
    def my_function(a, b, c=None, d=None):
        pass

    my_function("foo", "bar", "", "")
    my_function("foo", "bar", d="baz")
    my_function("foo", "bar", c="baz")
    my_function("foo", "bar")
    my_function("foo")
    my_function()

test_LoggedFunction___call__()


# Generated at 2022-06-14 05:03:48.712250
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class FakeLogger:
        def __init__(self):
            self.log = []

        def debug(self, message):
            self.log.append(message)

    fakeLogger = FakeLogger()

    def fakeFunction(a, b, c=3, d=4, e=5):
        return 1

    loggedFunction = LoggedFunction(fakeLogger)
    loggedFakeFunction = loggedFunction(fakeFunction)
    assert loggedFakeFunction(1, 2, d=7, e=8) == 1
    assert fakeLogger.log[0] == "fakeFunction(1, 2, c=3, d=7, e=8)"
    assert fakeLogger.log[1] == "fakeFunction -> 1"

# Generated at 2022-06-14 05:03:59.681298
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(levelname)s - %(asctime)s - %(name)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    a = LoggedFunction(logger)


    @a
    def func(a, b, c=None):
        return a / b


    if __name__ == "__main__":
        func(10, 2, c=1)
        func(10, b=2, c=1)
        func(10, 2)



# Generated at 2022-06-14 05:04:03.392910
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    import logging
    import sys
    import unittest

    logger = logging.getLogger(__name__)
    logger.level = logging.INFO
    logger.addHandler(logging.StreamHandler(sys.stdout))

    def test_func(a, b=None):
        return a + b

    logged_func = LoggedFunction(logger)(test_func)
    logged_func(1, b=2)
    logged_func(a=1, b=2)
    logged_func(1, 2)

    # expected output:

    # test_LoggedFunction___call__ INFO     test_func(1, b=2)
    # test_LoggedFunction___call__ INFO     test_func -> 3
    # test_LoggedFunction___call__ INFO     test_func(a=1, b=2)
   

# Generated at 2022-06-14 05:04:14.888218
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock
    from unittest.mock import call
    from logging import DEBUG

    logger = MagicMock()

    # Test with argument, keyword argument, and return value
    @LoggedFunction(logger)
    def foo(a, b=1, c=2):
        """Function description."""
        return 1

    foo("test", c=3)
    assert len(logger.mock_calls) == 2
    assert logger.mock_calls[0][1][0] == "foo('test', b=1, c=3)"
    assert logger.mock_calls[1][1][0] == "foo -> 1"

    # Test with no arguments, keyword arguments, and return value

# Generated at 2022-06-14 05:04:28.088115
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from lila.core.logging import Logger
    from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

    def test_function_with_debug_log(arg1, arg2, arg3, kwarg1=10, kwarg2=20):
        return arg1 * arg2 + arg3

    logger = Logger()
    logger.set_level(DEBUG)
    logger.attach_handler(DEBUG, logging.StreamHandler())

    assert test_function_with_debug_log(1, 2, 3, kwarg1=4) == 9

    # Test LoggedFunction decorator logging debug messages
    test_function = LoggedFunction(logger)(test_function_with_debug_log)
    assert test_function(1, 2, 3, kwarg1=4) == 9

    # Test LoggedFunction decorator does

# Generated at 2022-06-14 05:04:39.077688
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    assert isinstance(build_requests_session(), Session)
    assert isinstance(
        build_requests_session().adapters["http://"].max_retries, Retry
    )
    assert build_requests_session(raise_for_status=False).hooks == {}
    assert build_requests_session(retry=False).adapters == {}
    assert isinstance(
        build_requests_session(retry=3).adapters["http://"].max_retries, Retry
    )
    assert build_requests_session(retry=3).adapters["http://"].max_retries.total

# Generated at 2022-06-14 05:04:46.350526
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Unit test for method __call__ of class LoggedFunction.
    """
    import logging

    logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(__name__)

    @LoggedFunction(logger)
    def plus(a, b):
        return a + b

    assert plus(4, 5) == 9

    @LoggedFunction(logger)
    def none(a, b):
        pass

    assert none(4, 5) == None

if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:04:46.993863
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    :return:
    """
    pass

# Generated at 2022-06-14 05:04:57.033959
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    from requests import post
    from requests.exceptions import HTTPError

    logger = mock.Mock()
    logged_function = LoggedFunction(logger)
    logged_post = logged_function(post)

    # Call it with no arguments
    logged_post("http://example.com")
    logger.debug.assert_called_once_with("post('http://example.com')")

    # Call it with arguments
    logged_post("http://example.com", data="data")
    logger.debug.assert_called_with("post('http://example.com', data='data')")

    # Call it with keyword arguments
    logged_post("http://example.com", data="data", timeout=5)

# Generated at 2022-06-14 05:05:30.055020
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Add decorated function to call
    @LoggedFunction(logger)
    def foo(a, b, c=3):
        return a + b + c

    # Test to invoke it
    foo(1, 2)



# Generated at 2022-06-14 05:05:42.573329
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a list handler
    handler = logging.StringIO()
    streamhandler = logging.StreamHandler(handler)
    streamhandler.setLevel(logging.DEBUG)

    # Create a logging format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    streamhandler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(streamhandler)

    # Test the function which is not logged

# Generated at 2022-06-14 05:05:51.310175
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    # Create test logger
    logger = logging.getLogger("LoggedFunction")
    logger.setLevel(logging.DEBUG)
    # Create test function
    def test_function():
        return "test"

    # Test LoggedFunction
    logged_function = LoggedFunction(logger)
    assert logged_function(test_function)() == "test"
    assert "test_function() -> test" in [x.message for x in logger.handlers[0].records]
    assert "test_function()" in [x.message for x in logger.handlers[0].records]


if __name__ == "__main__":
    # Run unit tests
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:06:04.233092
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging
    import inspect

    # Patch out logger so we can assert on it
    class MockLogger:
        def __init__(self):
            self.debug_messages = []

        def debug(self, message):
            self.debug_messages.append(message)

    def get_caller_name():
        return inspect.stack()[2].function

    mockLogger = MockLogger()

    @LoggedFunction(mockLogger)
    def test_function(a, b=True, *args, **kwargs):
        return b

    test_function(1, 3, 7, b=False, c="Hello", d=0)

    # Were both calls logged?
    assert len(mockLogger.debug_messages) == 2

    # Was function name logged correctly?


# Generated at 2022-06-14 05:06:15.753752
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys
    logger_stream = io.StringIO()
    logger = logging.getLogger("test.loggedfunction")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(logger_stream)
    logger.addHandler(handler)
    @LoggedFunction(logger)
    def debug_print(*args):
        print("debug_print has been called!")

    debug_print(1, 2, 3, 4)
    result = logger_stream.getvalue()
    assert "debug_print(1, 2, 3, 4)" in result
    assert "debug_print has been called!" in result
    assert "> debug_print -> None" in result

# Generated at 2022-06-14 05:06:16.736698
# Unit test for function build_requests_session
def test_build_requests_session():
    pass

# Generated at 2022-06-14 05:06:27.663860
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    from contextlib import contextmanager

    @LoggedFunction(logging.getLogger(__name__))
    def test_method(arg1, arg2, kwarg1="", kwarg2=None, *args, **kwargs):
        pass

    with capture_log_output() as log:
        test_method("test", "moretest", "kwtest")
        test_method("test", "moretest", kwarg1="kwtest")
        test_method("test", "moretest", kwarg2="kwtest")
        test_method("test", "moretest", "kwtest", "argtest")
        test_method("test", "moretest", kwarg1="kwtest", kwarg2="kwtest")

# Generated at 2022-06-14 05:06:31.465013
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from loguru import logger

    @LoggedFunction(logger)
    def square(x):
        return x * x

    square(2)
    square(3)
    square(3, 4)

# Generated at 2022-06-14 05:06:42.436502
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from io import StringIO
    from logging import basicConfig, DEBUG, getLogger
    import logging

    stream = StringIO()

    logger = getLogger(__name__)
    basicConfig(stream=stream, level=DEBUG)
    logger.debug("test")

    def test_function(*args, **kwargs) -> None:
        pass

    test_function = LoggedFunction(logger)(test_function)

    test_function(1, 2, 3, a=1, b=2, c=3)

    stream.seek(0)
    output = stream.read().strip()
    assert output == "test\ntest_function(1, 2, 3, a=1, b=2, c=3)\ntest_function -> None"


# Unit tests for method build_requests_session

# Generated at 2022-06-14 05:06:54.455858
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MockLogger:
        def __init__(self):
            self.debug = MagicMock()

    logger = MockLogger()
    logged_func = LoggedFunction(logger)(lambda a, b: a + b)
    logged_func(3, 4)
    assert logger.debug.call_count == 2
    assert logger.debug.call_args_list[0][0][0] == "lambda(3, 4)"
    assert logger.debug.call_args_list[1][0][0] == "lambda -> 7"
    logged_func(b=4, a=3)
    assert logger.debug.call_count == 4
    assert logger.debug.call_args_list[2][0][0] == "lambda(a=3, b=4)"