

# Generated at 2022-06-14 04:57:38.337407
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import sys
    import unittest
    import unittest.mock

    # Create a fake logger
    logger = unittest.mock.MagicMock()

    # Create a fake function that logs something
    def my_func(a, b=1):
        return a + b

    # Decorate the function
    decorated = LoggedFunction(logger)(my_func)

    # Call the function with some arguments, and check the logger output
    captured_stdout = io.StringIO()
    sys.stdout = captured_stdout
    result = decorated(1, b=2)
    sys.stdout = sys.__stdout__
    assert result == 3

# Generated at 2022-06-14 04:57:49.720807
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MockLogger:
        def __init__(self):
            self.level = 0
            self.debug_called = False
            self.level_called = False

        def setLevel(self, level):
            self.level = level
            self.level_called = True

        def debug(self, msg):
            self.level_called = False
            if msg is not None and msg != "":
                self.debug_called = True

    logger = MockLogger()
    logged_function = LoggedFunction(logger)

    def test_func(a="", b="", c=""):
        if a == "test_a" and b == "test_b" and c == "test_c":
            return "test_result"
        return "test_error"

    # check case where function has only arguments with default values
    test

# Generated at 2022-06-14 04:57:55.922276
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def test_function(a, b=None, c=None):
        return a + b + c

    test_function(1, 2, 3)
    test_function(1, 2)
    test_function(1, c=3)
    test_function(1)



# Generated at 2022-06-14 04:58:07.140975
# Unit test for function build_requests_session
def test_build_requests_session():
    assert isinstance(build_requests_session(), Session)
    assert isinstance(build_requests_session().adapters["http://"], HTTPAdapter)
    assert isinstance(
        build_requests_session().adapters["http://"].max_retries, Retry
    )
    assert isinstance(build_requests_session().adapters["https://"], HTTPAdapter)
    assert isinstance(
        build_requests_session().adapters["https://"].max_retries, Retry
    )

    assert isinstance(build_requests_session(False), Session)
    assert isinstance(build_requests_session(False).adapters["http://"], HTTPAdapter)
    assert isinstance(
        build_requests_session(False).adapters["http://"].max_retries, Retry
    )
   

# Generated at 2022-06-14 04:58:18.097940
# Unit test for function build_requests_session
def test_build_requests_session():
    from unittest.mock import MagicMock
    from requests.hooks import default_hooks

    s = build_requests_session()
    assert s.hooks["response"] == default_hooks["response"]

    s = build_requests_session(True)
    assert s.hooks["response"] == default_hooks["response"]

    s = build_requests_session(True, False)
    assert s.hooks["response"] == default_hooks["response"]

    s = build_requests_session(True, 1)
    assert s.hooks["response"] == default_hooks["response"]

    s = build_requests_session(True, Retry())
    assert s.hooks["response"] == default_hooks["response"]

    mock_response = MagicMock()
    mock_response

# Generated at 2022-06-14 04:58:20.702379
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    r = session.get("https://httpbin.org/status/418")
    assert r.status_code == 418

# Generated at 2022-06-14 04:58:26.952868
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock, call

    logger = MagicMock()
    decorator = LoggedFunction(logger)

    
    class Testing:
        @decorator
        def method(self, param1, param2):
            return

    Testing().method("test", 3)
    assert logger.debug.mock_calls == [
        call("method('test', 3)"),
        call("method -> None"),
    ]

# Generated at 2022-06-14 04:58:35.548519
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    class MockLogger:
        def __init__(self):
            self.called = False
        def debug(self, *args, **kwargs):
            self.called = True
        def __call__(self, *args, **kwargs):
            self.called = True

    # Arrange
    logger = MockLogger()
    lf = LoggedFunction(logger)

    def dummy_func(a, b, c=1, d=None, e="str", f=b"bytes", g=True):
        return "dummy"

    # Act
    logged_func = lf(dummy_func)
    logged_func(1, 2, e="string", f=b"byte")

    # Assert
    assert logger.called


# Generated at 2022-06-14 04:58:44.680202
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    @LoggedFunction(logger)
    def add(x, y):
        return x+y
    @LoggedFunction(logger)
    def minus(x, y):
        return x-y
    @LoggedFunction(logger)
    def div(x, y):
        return x/y
    @LoggedFunction(logger)
    def mul(x, y):
        return x

# Generated at 2022-06-14 04:58:54.947373
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    from unittest.mock import patch

    def test_function(a, b, c=3, d=4):
        return a + b + c + d

    with StringIO() as log_io:
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler(log_io)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        with patch("enrich_md.utils.logger", logger):
            test_function = LoggedFunction(logger)(test_function)
            test_function(1, 2)

# Generated at 2022-06-14 04:59:10.342113
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys
    import unittest

    # Redirect output to a stream
    stream = io.StringIO()
    logger = logging.getLogger("__LoggedFunction_test__")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)

    class LoggedFunction_Test(unittest.TestCase):
        def test_logging_function(self):
            @LoggedFunction(logger)
            def test_func(a, b, c=3, d=4):
                return a + b + c + d

            test_func(10, 20)

# Generated at 2022-06-14 04:59:18.273691
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest.mock as mock

    # Prepare
    test_logger = mock.MagicMock()
    input_args = (1, 2, 3)
    input_kwargs = {"a": 4, "b": 5}
    expected_result = [1]
    mock_func = mock.Mock(name='mock_func', return_value=expected_result)
    test_func = LoggedFunction(test_logger)(mock_func)

    # Run test
    actual_result = test_func(*input_args, **input_kwargs)

    # Verify test
    assert actual_result == expected_result
    mock_func.assert_called_once_with(*input_args, **input_kwargs)

# Generated at 2022-06-14 04:59:23.014936
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger()
    logger.disabled = True
    def some_function(a, b, c=3):
        return "some_result"

    logged_function = LoggedFunction(logger)
    logged_some_function = logged_function(some_function)
    logged_some_function("a", 3, c=1)
    logged_some_function("a b", 2)
    with pytest.raises(ValueError):
        logged_some_function(1, [], kwarg=None)
    with pytest.raises(ValueError):
        logged_some_function("a", 3, c=3, extra_kwarg=None)
    with pytest.raises(TypeError):
        logged_some_function()



# Generated at 2022-06-14 04:59:33.676220
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    logger = logging.getLogger()
    logger.level = logging.DEBUG

    log_stream = io.StringIO()
    handler = logging.StreamHandler(log_stream)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def test_fun(x, y=2, z=3):
        return x + y + z

    test_fun(1)
    test_fun(1, z=10)
    result = test_fun(1, 2, 3)


# Generated at 2022-06-14 04:59:36.693943
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger(__name__)
    def add(a, b):
        return a + b
    logged_add = LoggedFunction(logger)(add)
    logged_add(1, 2)
    logged_add(1, b=2)
    logger.setLevel(logging.INFO)
    logged_add(1, b=2)

# Generated at 2022-06-14 04:59:45.503474
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger('demo')
    logger.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

    @LoggedFunction(logger)
    def add(a, b=2, c=3):
        return a + b + c

    add(1, b=3)
    add(1, c=4)
    add(2)
    add(2, 4)
    add(2, 4, 6)


# Generated at 2022-06-14 04:59:55.445920
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import RequestException
    from requests.models import Response
    from unittest.mock import patch

    with patch("requests.Session.request", return_value=Response()) as mock_request:
        session = build_requests_session(raise_for_status=True)
        session.get("http://test.com")
        assert mock_request.call_count == 1
        mock_request.assert_called_with(
            "GET",
            "http://test.com",
            allow_redirects=True,
            hooks={"response": [lambda r, *args, **kwargs: r.raise_for_status()]},
        )

# Generated at 2022-06-14 05:00:06.061662
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # setUp
    class TestLogger:
        def __init__(self):
            self.logs = []
        def debug(self, msg):
            self.logs.append(msg)
    test_logger = TestLogger()
    decorator = LoggedFunction(logger=test_logger)
    # Test function without arguments
    @decorator
    def f0():
        return 10
    # exercise
    result = f0()
    # verify
    assert result == 10
    assert test_logger.logs == ["f0()","f0 -> 10"]
    # Test function with arguments
    @decorator
    def f1(a, *b, c=10, **d):
        return a*10 + c
    # exercise

# Generated at 2022-06-14 05:00:17.157185
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    import unittest


    class Test(unittest.TestCase):
        def setUp(self):
            # https://docs.python.org/3/howto/logging.html#configuring-logging
            # https://docs.python.org/3/library/logging.html?highlight=logging#logrecord-attributes
            logging.basicConfig(
                level=logging.DEBUG,
                format="%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s",
            )

        def test_args_only(self):
            @LoggedFunction(logging)
            def f(arg1, arg2):
                return arg1 * arg2


            f(1, 2)

# Generated at 2022-06-14 05:00:25.678138
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger()

    @LoggedFunction(logger)
    def test_func(a, b, c="c"):
        pass

    logger.setLevel("DEBUG")

    logger.debug("test 1")
    test_func("a", "b")
    logger.debug("test 2")
    test_func("a", "b", "c")
    logger.debug("test 3")
    test_func("a", "b", c="c")

# Generated at 2022-06-14 05:01:17.415073
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging

    class LoggedFunctionTest(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger()

        def test_logged_function_called_with_args(self):
            @LoggedFunction(self.logger)
            def foo(x):
                return x

            x = foo(1)
            self.assertEqual(x, 1)
            self.assertTrue(
                self.logger.hasMessage(
                    "foo(1)", level=self.logger.debugLevel,
                )
            )
            self.assertTrue(
                self.logger.hasMessage(
                    "foo -> 1", level=self.logger.debugLevel,
                )
            )
        

# Generated at 2022-06-14 05:01:28.067531
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    logging_mock = Mock()
    @LoggedFunction(logging_mock)
    def basic_function(a,b,c,d=1,e=2,f=3):
        return a+b+d+e+f
    @LoggedFunction(logging_mock)
    def function_without_return(a,b,c,d=1,e=2,f=3):
        pass
    @LoggedFunction(logging_mock)
    def function_with_kwargs_only(**kwargs):
        return sum(kwargs.values())
    basic_function(1,2,3)
    basic_function(1,2,3,4,5,6)
    function_without_return(1,2,3)
    function_

# Generated at 2022-06-14 05:01:36.382722
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    from io import StringIO
    import sys
    import logging

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def foo(x, y, z=3):
        return x + y + z

    # Prepare logger output
    log_output = StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(log_output)
    logger.addHandler(stream_handler)

    # Test add function without any parameters
    add_function = LoggedFunction(logger)(add)
    add_function(2, 3)

    # Test sub function with keyword arguments
    sub_function = LoggedFunction(logger)(sub)

# Generated at 2022-06-14 05:01:48.522523
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest.mock
    import logging

    class TestLogger:
        def debug(self, msg):
            print(msg)

    # Test simple arguments
    @LoggedFunction(TestLogger())
    def simple(a, b):
        return a + b

    simple(1, 2)

    # Test keyword arguments
    @LoggedFunction(TestLogger())
    def kw(a, b, c=3):
        return a * b * c

    kw(1, b=2, c=4)

    # Test arguments containing objects
    @LoggedFunction(TestLogger())
    def test_obj(obj):
        return obj

    test_obj({"a": 1})

    # Test return None

# Generated at 2022-06-14 05:01:55.539167
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    class FakeLogger:
        def __init__(self):
            self._log = []

        def debug(self, msg):
            self._log.append(msg)

        def get_log(self):
            return "\n".join(self._log)

    def test_function(a_string, a_number, a_dict=None):
        pass

    logger = FakeLogger()
    logged_function = LoggedFunction(logger)
    function = logged_function(test_function)

    function("a string", 42)
    assert (
        logger.get_log()
        == "test_function('a string', 42)\ntest_function -> None"
    )

    logger = FakeLogger()
    logged_function = LoggedFunction(logger)

# Generated at 2022-06-14 05:02:07.062811
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class FakeLogger:
        # Fake logger, just stores a list of messages that are logged
        def __init__(self):
            self.messages = []

        def debug(self, msg):
            self.messages.append(msg)

        def __getitem__(self, index):
            return self.messages[index]

    logger = FakeLogger()

    @LoggedFunction(logger)
    def foo(x, y=2, z="hello"):
        return x * y * (z + "!")

    # Call function once, and make sure the log message is correct
    assert foo(1, z="z") == "1z!"
    assert logger[0] == "foo(1, z='z')"
    assert logger[1] == "foo -> 1z!"

    # Call function again, and make

# Generated at 2022-06-14 05:02:20.000369
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import datetime
    import time
    import logging
    logger = logging.getLogger()

    @LoggedFunction(logger)
    def add(x, y):
        # Simulate some activity
        time.sleep(0.5)
        return datetime.date(2020,5,5)

    # Verify log output
    #expected_log = 'add(1, 2) -> 2020-05-05'
    #assert self.handler.messages[-1] == expected_log
    #
    #assert add(1, y=2) == datetime.date(2020,5,5)
    #assert add(1, y=2) == datetime.date(2020,5,5)

    # test
    add(1, 2)



# Generated at 2022-06-14 05:02:31.226337
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger, DEBUG, Logger

    class MockLogger(Logger):
        def __init__(self):
            super().__init__(None)
            self.messages = []

        def debug(self, message):
            self.messages.append(message)

    def test_function(a, b, c=0, d=None):
        return True

    expected_func_name = "test_function"
    expected_args = (1, 2, 3, "hello")
    expected_kwargs = {
        "c": expected_args[2],
        "d": expected_args[3],
    }
    expected_result = True

    logged_function = LoggedFunction(MockLogger())
    logged_test_function = logged_function(test_function)

    actual_result = logged_

# Generated at 2022-06-14 05:02:41.269384
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest.mock
    from requests import Response
    from requests.exceptions import RequestException

    from expecter import expect

    from .logger import Logger

    logger = Logger(__name__, level="DEBUG")
    logged_function = LoggedFunction(logger)
    response = Response()
    response.raise_for_status = unittest.mock.Mock(side_effect=RequestException)
    response.status_code = 201
    response.json = unittest.mock.Mock(return_value={"test": "success"})
    logged_function(lambda: print("test"))()
    logged_function(lambda: print("test", 1))()
    logged_function(lambda: print("test", None))()
    logged_function(lambda: print("test", b"b"))()
    logged

# Generated at 2022-06-14 05:02:47.792363
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import tempfile
    import logging
    import os

    logfile = tempfile.NamedTemporaryFile(mode="w+")
    loggers = {
        k: logging.getLogger(k)
        for k in ["logger1", "logger2", "logger3", "logger4", "logger5"]
    }
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    for logger in loggers.values():
        logger.addHandler(logging.FileHandler(logfile.name))


# Generated at 2022-06-14 05:03:03.080316
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import patch
    logger = logging.getLogger("test")
    func = LoggedFunction(logger)
    test_func = func(lambda: True)
    with patch.object(logger, "debug") as mock_debug:
        assert test_func() is True
    assert mock_debug.call_count == 2
    assert mock_debug.call_args_list[0] == ((f"<lambda>()",),)
    assert mock_debug.call_args_list[1] == ((f"<lambda> -> True",),)
    logger = logging.getLogger("test")
    func = LoggedFunction(logger)
    test_func = func(lambda x, y: x * y)

# Generated at 2022-06-14 05:03:06.483222
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(True, Retry(total=3, status_forcelist=[500]))
    assert session.hooks["response"][0].__name__ == "raise_for_status"
    assert session.adapters["http://"].max_retries.total == 3
    assert session.adapters["http://"].max_retries.status_forcelist == [500]

# Generated at 2022-06-14 05:03:16.987795
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import LoggerAdapter
    from logging import StreamHandler
    from logging import DEBUG
    from logging import Formatter
    import sys
    import unittest

    logger = LoggerAdapter(
        logging.getLogger(__name__), {"name": "LoggedFunction"}
    )

    # Create and run unit test
    class LoggedFunctionTestCase(unittest.TestCase):
        def test_logged_function_test(self):
            def test_func(x, y):
                return x + y

            logged_func = LoggedFunction(logger)(test_func)
            self.assertEqual(logged_func(1, 2), 3)

    test_case = LoggedFunctionTestCase()
    test_case.test_logged_function_test()


# Generated at 2022-06-14 05:03:28.926665
# Unit test for function build_requests_session
def test_build_requests_session():
    import pytest
    
    @LoggedFunction(logger=pytest.logger)
    def build_requests_session(
        raise_for_status=True, retry: Union[bool, int, Retry] = True
    ) -> Session:
        """
        Create a requests session.
        :param raise_for_status: If True, a hook to invoke raise_for_status be installed
        :param retry: If true, it will use default Retry configuration. if an integer, it will use default Retry
        configuration with given integer as total retry count. if Retry instance, it will use this instance.
        :return: configured requests Session
        """
        session = Session()

# Generated at 2022-06-14 05:03:40.020786
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    log_stream = StringIO()
    logging.basicConfig(stream=log_stream, level=logging.DEBUG)
    log = logging.getLogger("logged_function")
    logger = LoggedFunction(log)
    @logger
    def func(a, b, c=1, d=2):
        return a+b+c+d
    func(1, 2, c=3, d=4)
    log_stream.seek(0)
    log_info = log_stream.read()
    assert log_info == "func(1, 2, c=3, d=4)\nfunc -> 10\n"

if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:03:48.453446
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Unit test for method __call__ of class LoggedFunction
    """
    from log_utils import StringLogger, StringLoggerHandler

    logger = StringLogger("pyutil")
    handler = StringLoggerHandler()
    logger.add_handler(handler)

    @LoggedFunction(logger)
    def test_func(a, b=[], c=None):
        return "this is return value"

    test_func(1, 2, 3, c=4)
    assert handler.get_log_text().split("\n")[-2].strip() == \
        "test_func(1, 2, 3, c=4)"
    assert handler.get_log_text().split("\n")[-1].strip() == \
        "test_func -> this is return value"



# Generated at 2022-06-14 05:03:55.037720
# Unit test for function build_requests_session
def test_build_requests_session():
    build_requests_session()
    build_requests_session(raise_for_status=False)
    build_requests_session(retry=3)
    build_requests_session(retry=False)
    build_requests_session(retry=Retry())
    try:
        build_requests_session(retry=0)
    except: pass
    else: assert False

# Generated at 2022-06-14 05:04:01.710133
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def simple_function(arg1, arg2, kwarg1=None, kwarg2=None):
        return arg1 + arg2

    logger = Mock()
    function = LoggedFunction(logger)
    function(simple_function)(1, 2, kwarg1="one", kwarg2="two")
    logger.debug.assert_called_with(
        "simple_function(1, 2, kwarg1='one', kwarg2='two')"
    )
    logger.debug.assert_any_call("simple_function -> 3")

# Generated at 2022-06-14 05:04:13.557840
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger()
    logged_func = LoggedFunction(logger)

    def func(arg1, arg2=1, *args, **kwargs):
        return arg1 + arg2

    # Check for different arguments for __call__
    assert logged_func(func)(1) == 2
    assert logged_func(func)(1, arg2=2)  == 3
    assert logged_func(func)(arg2=2) == 3
    assert logged_func(func)(arg2=2, arg1=1) == 3
    assert logged_func(func)(arg2=2, arg1=1, arg3=3) == 3
    assert logged_func(func)(arg1=1, arg3=3, arg2=2) == 3

# Generated at 2022-06-14 05:04:19.902177
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    # Set up a logger that writes to a string buffer.
    sio = io.StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sio))

    # Wrap a function in a LoggedFunction decorator
    @LoggedFunction(logger)
    def foo(x, y='y', z=3):
        return (x, y, z)

    # Call the function a few times
    foo(1)
    foo('x', z='z')
    foo('x', 'y', 'z')

    # Check it logged what we expected
    logged = sio.getvalue().splitlines()

# Generated at 2022-06-14 05:04:35.593537
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    from unittest.mock import Mock

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.logger = Mock()
            self.logged_class = LoggedFunction(logger=self.logger)

        def test_log_function_call_with_no_args(self):
            func = Mock()

            logged_func = self.logged_class(func)
            logged_func()

            self.logger.debug.assert_called_once_with("func()")

        def test_log_function_call_with_basic_types_args(self):
            func = Mock()

            # Define values of the various types
            bool_values = [True, False]

# Generated at 2022-06-14 05:04:42.956391
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger()
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(logging.Formatter("%(message)s"))
    log_handler.setLevel(logging.DEBUG)
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)

    # Define a function to log
    @LoggedFunction(logger)
    def add(a, b):
        return a + b

    # Test a function call
    assert add(1, 2) == 3



# Generated at 2022-06-14 05:04:49.677431
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    handler = logging.StreamHandler(stream=io.StringIO())
    logger = logging.getLogger("test")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    lf = LoggedFunction(logger)
    @lf
    def plural(word):
        return word + "s"

    plural("apple")
    assert handler.stream.getvalue() == "test:DEBUG:plural('apple')\n" \
                                        "test:DEBUG:plural -> apples\n"



# Generated at 2022-06-14 05:04:55.018178
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    @LoggedFunction(logger)
    def foo(a, b, c=1, d=2):
        return "return-value"

    assert foo(1, 2) == "return-value"

# Generated at 2022-06-14 05:04:57.646096
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        def debug(self, str):
            pass
    logger = Logger()
    logged_func = LoggedFunction(logger)
    def f(x):
        pass
    f = logged_func(f)
    f(1)
    f(1, 2)
    f(1, 2, a=1)

test_LoggedFunction___call__()

# Generated at 2022-06-14 05:05:02.474035
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def add(a, b=4):
        return a + b

    add(2)



# Generated at 2022-06-14 05:05:15.076391
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    class log:
        def __init__(self):
            self.data = []

        def debug(self, x):
            self.data.append(x)

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    l = log()
    logger = logging.Logger(name="test_LoggedFunction___call__",handlers=[logging.StreamHandler()])

    @LoggedFunction(logger)
    def example(x, y, z=3):
        return x + y + z

    example(1, 2)
    assert l.data == ["example(1, 2, z=3)", "example -> 6"]

    example(1, 2, z=4)

# Generated at 2022-06-14 05:05:27.459740
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import json
    import logging
    from io import StringIO
    from unittest import TestCase

    class Test(TestCase):
        def test_logged_func(self):
            def func(a, b, c=None, d=1):
                return a + b + d

            buf = StringIO()
            handler = logging.StreamHandler(stream=buf)
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter("%(message)s")
            handler.setFormatter(formatter)

            logger = logging.getLogger("test")
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)

            logged_func = LoggedFunction(logger=logger)(func)
            self.assertEqual(logged_func(1, 2, 3), 3)


# Generated at 2022-06-14 05:05:34.738821
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class DummyLogger:
        def __init__(self):
            self.logs = []
        def debug(self, msg):
            self.logs.append(msg)
    def func(a, b=10):
        pass
    dummy_logger = DummyLogger()
    logger_func = LoggedFunction(dummy_logger)(func)
    logger_func(1, b=2)
    assert dummy_logger.logs[0] == "func(1, b=2)"
    assert dummy_logger.logs[1] == "func -> None"



# Generated at 2022-06-14 05:05:38.241478
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    class test_class():
        def my_method(a, b, c=3, d=4, keyword=5):
            return "a, b, c, d, keyword"
    test_class.my_method = LoggedFunction(logger)(test_class.my_method)
    assert test_class.my_method(1, 2) == "a, b, c, d, keyword"

# Generated at 2022-06-14 05:05:57.444272
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        def __init__(self):
            self.logs = []

        def debug(self, msg):
            self.logs.append(msg)

    @LoggedFunction(Logger())
    def test_func(a, b, c, d, x=5, y=6):
        pass

    test_func(1, 2, 3, 4)
    assert test_func.__name__ == "test_func"
    # self.logs.sort()

# Generated at 2022-06-14 05:06:02.957996
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("logged_func_test")
    logged_func = LoggedFunction(logger)

    @logged_func
    def foo(arg1, arg2, kwarg1=None):
        return 1

    foo("a", "b", "c")  # this should print 1 line of log



# Generated at 2022-06-14 05:06:09.958385
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from io import StringIO
    from contextlib import redirect_stdout
    def dummy_func(a, b, c=3, d=4):
        return a + b + c + d
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    f = StringIO()
    with redirect_stdout(f):
        logged_func = LoggedFunction(logger)
        result = logged_func(dummy_func)(1, 2)
    assert result == 1 + 2 + 3 + 4
    assert "dummy_func(1, 2, c=3, d=4) -> 10" in f.getvalue()

# Generated at 2022-06-14 05:06:17.087106
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)

    @LoggedFunction(logger)
    def foobar(arg1, arg2):
        return arg1 + arg2

    # Test 1
    assert foobar(1, 2) == 3

test_LoggedFunction___call__()

# Generated at 2022-06-14 05:06:27.876643
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import sys
    import logging
    import unittest

    class TestLoggedFunction(unittest.TestCase):
        def test_success(self):
            self.saved_stdout = sys.stdout
            sys.stdout = self.assert_output = TestOutput()
            logger = logging.getLogger("test_success")
            logger.setLevel(logging.DEBUG)
            logged_func = LoggedFunction(logger)(func_test_logged_function)
            self.assertEqual(logged_func(1, 2, 3), 4)
            self.assertEqual(
                self.assert_output.output,
                "func_test_logged_function(1, 2, 3)\n"
                "func_test_logged_function -> 4\n",
            )

# Generated at 2022-06-14 05:06:39.614896
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import time
    import unittest

    from unittest.mock import patch

    class TestCase(unittest.TestCase):
        @patch("logging.Logger.debug")
        def test___call__(self, mock_debug):
            mock_logger = logging.Logger("mock")
            logged_func = LoggedFunction(mock_logger)
            test_func = logged_func(lambda i: i ** 2)
            result = test_func(42)
            mock_debug.assert_any_call("test_func(42)")
            mock_debug.assert_any_call("test_func -> 1764")
            self.assertEqual(result, 1764)

    # Execute TestCase

# Generated at 2022-06-14 05:06:49.036325
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def get_func(n, kwarg=False):
        def func(*args, **kwargs):
            return (args, kwargs, func.__defaults__, func.__kwdefaults__)

        func.__defaults__ = tuple(range(n))
        func.__kwdefaults__ = {"kwarg": kwarg}
        return func

    logger = FakeLogger()
    for n in range(0, 5):
        for kwarg in (False, True):
            func = get_func(n, kwarg)
            logged_func = LoggedFunction(logger)(func)
            args = (n + 1) * [None]
            kwargs = {}
            if kwarg:
                kwargs["kwarg"] = None

# Generated at 2022-06-14 05:06:57.455212
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest.mock as mock
    from logging import DEBUG

    # Test method __call__
    mock_logger = mock.MagicMock()
    mock_logger.debug = mock.MagicMock()
    logged_function = LoggedFunction(
        logging.Logger(
            name="test",
            level=DEBUG,
            handlers=[logging.StreamHandler(stream=mock.MagicMock())],
        )
    )

    @logged_function
    def test_func(a, b, c=None):
        return (a, b, c)

    test_func(1, 2, c=3)
    assert mock_logger.debug.call_count == 2



# Generated at 2022-06-14 05:07:08.602199
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    def testFunc(a, b, c=3):
        return a + b + c

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    logged_func = LoggedFunction(logger)(testFunc)
    print(logged_func(1, 2))
    print(logged_func(1, 2, c=4))



# Generated at 2022-06-14 05:07:17.030594
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from .logging import logger
    logger.setLevel("INFO")  # for unittest

    @LoggedFunction(logger)
    def test(a, b, c=None):
        return f"{a}-{b}-{c}"

    assert test(1, 2, 3) == "1-2-3"
    assert test(1, 2) == "1-2-None"

    class A:
        def __repr__(self):
            return "A()"

    assert test(a=10.5, b=2j, c=A()) == "10.5-2j-A()"