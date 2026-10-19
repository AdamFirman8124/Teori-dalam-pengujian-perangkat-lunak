

# Generated at 2022-06-14 04:57:40.954600
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    log = logging.getLogger("test_LoggedFunction___call__")

    def test(a, b):
        print("inside test fn")
        return a + b

    output = []

    @LoggedFunction(log)
    def test_with_loggedFunction(a, b, x=5, y=5):
        print("inside test_with_loggedFunction fn")
        return a + b + x + y

    # Create a test logger
    handler = logging.StreamHandler(io.StringIO())
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    # Check that logging is performed for normal function
    assert log.debug("before calling test fn") is None
    assert test(1, 2) == 3

# Generated at 2022-06-14 04:57:43.364854
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    with LoggedFunction(logging.getLogger(__name__)):
        pass

# Generated at 2022-06-14 04:57:46.385810
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    class FakeLogger:
        def __init__(self):
            self.log = io.StringIO()

# Generated at 2022-06-14 04:57:52.525261
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert session is not None
    assert len(session.adapters) == 2
    assert "https://" in session.adapters
    assert "http://" in session.adapters
    session = build_requests_session(retry=False)
    assert session is not None
    assert len(session.adapters) == 0
    retry = Retry(total=10, backoff_factor=10)
    session = build_requests_session(retry=retry)
    assert session is not None
    assert len(session.adapters) == 2
    for adapter in session.adapters.values():
        assert adapter.max_retries.total == 10
        assert adapter.max_retries.backoff_factor == 10

# Generated at 2022-06-14 04:58:03.011144
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from logging import DEBUG
    from unittest.mock import patch

    function = LoggedFunction(logging.getLogger("test"))
    with patch("logging.Logger") as mock:
        function(lambda a, b, c=1, d=2: None)("a", "b", c=3, d=4)
        mock.debug.assert_called_with("lambda(a, b, c=3, d=4)")
        mock.debug.reset_mock()
        function(lambda a, b, c=1, d=2: None)("a", "b", c=3)
        mock.debug.assert_called_with("lambda(a, b, c=3, d=2)")
        mock.debug.reset_mock()

# Generated at 2022-06-14 04:58:13.415361
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import exceptions
    from requests.exceptions import RequestException

    #raise_for_status will set raise_for_status hook on requests session
    with pytest.raises(exceptions.HTTPError):
        build_requests_session(raise_for_status=True).get("http://httpbin.org/status/500", allow_redirects=True)

    #retry is set to True
    with pytest.raises(RequestException):
        build_requests_session(retry=True).get("http://httpbin.org/status/500", allow_redirects=True)

    #retry is set to False
    with pytest.raises(RequestException):
        build_requests_session(retry=False).get("http://httpbin.org/status/500", allow_redirects=True)

# Generated at 2022-06-14 04:58:22.929234
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from moto import mock_dynamodb2, mock_kms  #, mock_s3, mock_sqs
    from mypy_boto3_kms.service_resource import ServiceResource
    from mypy_boto3_kms.session import Session
    from python_freeipa.exceptions import PythonFreeIPAError
    from python_freeipa.config import FreeIPAConfig
    from python_freeipa.ipa import FreeIPA
    import logging
    import unittest


# Generated at 2022-06-14 04:58:35.425540
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        def __init__(self):
            self.mock_logs = []

        def debug(self, msg):
            self.mock_logs.append(msg)
            
    class LoggerWithName:
        def __init__(self):
            # If Logger is updated, LoggerWithName can be updated by the same logic
            self.mock_logs = []

        def debug(self, msg):
            self.mock_logs.append(msg)
            
        def getEffectiveLevel(self):
            return 1
        
        def isEnabledFor(self, level):
            if self.getEffectiveLevel() <= level:
                return True
            else:
                return False
        
        def getChild(self, suffix):
            return LoggerWithName()
        

# Generated at 2022-06-14 04:58:44.371468
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    @LoggedFunction(logger)
    def func(a, b, c="ccc", d=0):
        print(a, b, c, d)
        return "return"
    func("aaa", "bbb")
    func(d=100, c="ccccc", b="bbbbb", a="aaaaa")



# Generated at 2022-06-14 04:58:54.214307
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from tornado.options import options
    from tornado.log import LogFormatter
    from tornado.log import access_log
    from tornado.log import app_log
    from logging import StreamHandler

    def test_function():
        pass

    # Step 1: Prepare debug logger with stream handler

    # Prepare options
    options.logging = "debug"
    options.log_to_stderr = True
    options.log_file_prefix = None
    options.log_file_max_size = None
    options.log_file_num_backups = None
    options.log_rotate_interval = None
    options.log_rotate_mode = None
    options.log_rotate_when = None
    options.log_rotate_interval = None
    options.log_rotate_interval = None

    # Prepare

# Generated at 2022-06-14 04:59:10.343005
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import TestCase, main
    from unittest.mock import patch
    from io import StringIO

    class Test(TestCase):
        def setUp(self):
            self.log_output = StringIO()
            self.logger = logging.getLogger("logged_function")
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(logging.StreamHandler(self.log_output))

        def test_noparam(self):
            @LoggedFunction(self.logger)
            def test_function():
                pass

            test_function()
            self.assertEqual(self.log_output.getvalue(), "test_function()\n")


# Generated at 2022-06-14 04:59:13.325646
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger

    mock_logger = getLogger("mock")

    @LoggedFunction(mock_logger)
    def method(a, b):
        return a + b

    method(1, 2)

# Generated at 2022-06-14 04:59:25.554448
# Unit test for function build_requests_session
def test_build_requests_session():
    import logging
    import requests
    from uuid import uuid4
    from urllib3.exceptions import ReadTimeoutError

    URL = "https://httpstat.us/"
    # Create a random 404 endpoint
    endpoint = str(uuid4())
    logger = logging.getLogger("requests_session")

    def test_func(raise_for_status, retry):
        session = build_requests_session(raise_for_status, retry)
        logger.debug(f"Testing session with raise_for_status={raise_for_status}")
        logger.debug(f"Testing session with retry={retry}")

# Generated at 2022-06-14 04:59:34.128981
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Set up logging
    from logging import getLogger, DEBUG

    logger = getLogger("test_LoggedFunction___call__")
    logger.setLevel(DEBUG)

    # Set up function to be logged
    def my_func(a, b, c, d="a", e=1): return a + b + c + d + e

    # Add logging to function
    my_func = LoggedFunction(logger)(my_func)

    # Call function
    args = ("b", "c", "d")
    kwargs = {"d": "a", "e": 1}
    result = my_func(*args, **kwargs)

    # Check result
    assert result == "bcda1"

    # Check log
    #assert logger.has_info(f"{my_func.__name__}({', '.join([

# Generated at 2022-06-14 04:59:44.676314
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO

    unittest_logger = logging.getLogger()
    unittest_logger.level = logging.INFO
    unittest_logger_stream = StringIO()
    handler = logging.StreamHandler(unittest_logger_stream)
    unittest_logger.addHandler(handler)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def foo(a, b, c=None):
        return "return value of foo"

    result = foo(1, 2, 3)

    stream_contents = unittest_logger_stream.getvalue()

# Generated at 2022-06-14 04:59:58.041583
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    import unittest

    # Define a dummy function
    def foo(a: int, b: str):
        return a + len(b)

    # Define a log handler which does nothing
    class DummyLogHandler(logging.Handler):
        def emit(self, record):
            pass

    # Set up logger
    logger = logging.getLogger("test_logged_function")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(DummyLogHandler())

    # Decorate function
    foo_logged = LoggedFunction(logger)(foo)


# Generated at 2022-06-14 05:00:01.356081
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    ...
    # logger = logging.getLogger("dev")
    # logged_func = LoggedFunction(logger)(func)
    # result = logged_func("a", "b", c="c")

# Generated at 2022-06-14 05:00:14.193092
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    logger = logging.getLogger("testLogger")
    handler = logging.StreamHandler(io.StringIO())
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def example(a, b, c=5, d=6):
        return a + b + c + d

    # Capture logged data
    handler.flush()
    logged_data = handler.stream.getvalue()
    assert logged_data == ""

    assert example(1, 2, d=4) == 13
    handler.flush()
    logged_data = handler.stream.getvalue()
    assert logged_data == "example(1, 2, c=5, d=4)\n"

    assert example(2, 3) == 16
    handler.flush()

# Generated at 2022-06-14 05:00:18.162634
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    func = LoggedFunction(None)(lambda x: x + 1)
    assert func(1) == 2
    func = LoggedFunction(None)(lambda x, y=2: (x, y))
    assert func(2, 3) == (2, 3)
    assert func(2) == (2, 2)

# Generated at 2022-06-14 05:00:30.499321
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    test_logger = logging.getLogger("logged_function_test")
    test_logger.setLevel(logging.DEBUG)
    test_logger.handlers = []
    handler = logging.StreamHandler()
    handler.setLevel(level=logging.DEBUG)
    test_logger.addHandler(handler)

    @LoggedFunction(test_logger)
    def test_function(a, b, c=10):
        return a + b + c

    test_function(1, 2)
    test_function(1, 2, c=3)
    test_function(a=1, b=2, c=3)


if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:00:47.383543
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import logging.handlers
    import os
    import tempfile

    logger = logging.getLogger()
    logfile = tempfile.NamedTemporaryFile(suffix=".log", mode="a", delete=False)

# Generated at 2022-06-14 05:00:59.995472
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    with mock.patch('logging.getLogger') as mock_getLogger, \
            mock.patch('logging.Logger.debug') as mock_debug:
        mock_getLogger.return_value = 'mock_getLoggerReturnValue'
        mock_loggedFunction = LoggedFunction('mockLogger')

        # test with arguments
        @mock_loggedFunction
        def test_func(var1, var2, var3):
            print('test_func')

        # test with default arguments
        @mock_loggedFunction
        def test_func_default_args(var1, var2=2, var3=3):
            print('test_func_default_args')

        # invoke __call__ method
        mock_loggedFunction.__call__(test_func)
        mock_logged

# Generated at 2022-06-14 05:01:07.603194
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger, CRITICAL
    logger = getLogger(__name__)
    old_level = logger.level
    logger.setLevel(CRITICAL)
    logged_func = LoggedFunction(logger)
    @logged_func
    def test_func1(a, b):
        return a + b
    assert test_func1(1, 2) == 3
    assert test_func1('a', b='b') == 'ab'
    setattr(test_func1, '__name__', 'test_func2')
    assert test_func1(3, 4) == 7
    assert test_func1('a', 'b') == 'ab'
    logger.setLevel(old_level)

# Generated at 2022-06-14 05:01:19.533369
# Unit test for function build_requests_session
def test_build_requests_session():
    def test_func(retry):
        import requests
        from requests.packages.urllib3.util.retry import Retry
        from requests.adapters import HTTPAdapter
        from unittest.mock import patch
        from unittest.mock import Mock
        from unittest.mock import MagicMock
        from unittest.mock import call
        from unittest.mock import PropertyMock
        from unittest.mock import ANY
        from _pytest.monkeypatch import monkeypatch
        from requests.exceptions import HTTPError
        from urllib3 import Retry as Retry3
        import urllib3
        import functools

        with patch.object(Session, "__init__"):
            s = build_requests_session(retry=retry)

# Generated at 2022-06-14 05:01:29.281297
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger, DEBUG
    from unittest import TestCase, main

    getLogger().setLevel(DEBUG)

    class Test(TestCase):
        def setUp(self):
            self.log = []
            self.logger = getLogger()
            self.logger.debug = self.log.append

        def test1(self):
            @LoggedFunction(self.logger)
            def foo1(a, b):
                return a + b

            assert foo1(2, 3) == 5
            assert self.log[0] == "foo1(2, 3)"
            assert self.log[1] == "foo1 -> 5"

        def test2(self):
            @LoggedFunction(self.logger)
            def foo2(a: str, b: str):
                return a

# Generated at 2022-06-14 05:01:39.143397
# Unit test for function build_requests_session
def test_build_requests_session():
    import pandas as pd
    import pandas.util.testing as tm
    import pytest
    from dcm.middleware.pipeline.dcm_pipeline.utils.requests_utils import inmem_session_factory
    from dcm.middleware.pipeline.dcm_pipeline.utils.requests_utils import build_requests_session

    df = pd.DataFrame([[1, 2, "NA"], [3, 4, "NA"]], columns=["foo", "bar", "baz"])

    # This test is written to deal with https://github.com/TianhongDai/dcm-middleware/issues/354
    # It is not a perfect test and it mainly test if the requests_session passed in will overwrite the default session

# Generated at 2022-06-14 05:01:50.638713
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("test logger")
    lf = LoggedFunction(logger)
    @lf
    def test_function(a, b, c=3):
        return a + b + c
    assert test_function(1, 2) == 6
    assert test_function(1, 2, c=3) == 6
    assert test_function(1, 2, 3) == 6
    assert test_function(a=1, b=2) == 6
    assert test_function(a=1, b=2, c=3) == 6
    assert test_function(a=1, b=2, c=3) == 6

# Generated at 2022-06-14 05:02:00.942424
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    class ForLoggedFunctionTesting:
        def __init__(self):
            self.logger = logging.getLogger('ForLoggedFunctionTestingLogger')
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(logging.StreamHandler())
            self.logged_func = LoggedFunction(self.logger).__call__(
                self.func_to_be_logged
            )

        def func_to_be_logged(self, a, b=1):
            return a + b

    test_object = ForLoggedFunctionTesting()
    assert test_object.logged_func(1) == 2
    assert test_object.logged_func(0, 1) == 1

# Generated at 2022-06-14 05:02:09.258651
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    # Set up the logger
    log_output = []
    logger = logging.Logger("test_LoggedFunction___call__", level=logging.DEBUG)
    handler = logging.StreamHandler(stream=StringIO(newline=""))
    logger.addHandler(handler)
    logger.log = lambda level, msg, *args, **kwargs: log_output.append(msg.format(*args, **kwargs))

    # Define a function to decorate
    def function(arg1, kwarg1="default", *, kwarg2):
        pass

    # Apply the decorator
    logged_function = LoggedFunction(logger=logger)(function)

    # Call with different arguments and verify log output
    logged_function("a", kwarg1="b", kwarg2="c")

# Generated at 2022-06-14 05:02:17.933266
# Unit test for function build_requests_session
def test_build_requests_session():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    session = build_requests_session(retry=False)
    logger.info(session.__dict__)
    # assert hasattr(session, 'hooks')
    # assert len(session.hooks['response']) == 1
    # assert len(session.adapters) == 2

if __name__ == "__main__":
    test_build_requests_session()

# Generated at 2022-06-14 05:03:11.818603
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    resp = session.get("https://httpbin.org/status/403")
    print(resp)
    session = build_requests_session(raise_for_status=True)
    session.get("https://httpbin.org/status/403")

# Generated at 2022-06-14 05:03:21.954667
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    logger = Mock()
    logged_func = LoggedFunction(logger)(test_func)
    logged_func("a1", "a2", kwarg="xxx")
    logger.debug.assert_called_once_with("test_func('a1', 'a2', kwarg='xxx')")
    logger.debug.reset_mock()
    assert logged_func("a1", "a2", kwarg="xxx") == "test result"
    logger.debug.assert_called_once_with("test_func -> test result")


# Generated at 2022-06-14 05:03:31.874535
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    class TestLoggedFunction(LoggedFunction):
        def __init__(self):
            self.logger = logging.getLogger("test")
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(logging.StreamHandler())

    @TestLoggedFunction()
    def f(s: str, i: int = 0, b: bool = False):
        return "foo"

    class logTest(unittest.TestCase):
        def test_f(self):
            f("bar")
            f("bar", 3)
            f("bar", i=3)
            f("bar", i=3, b=True)

    unittest.main()

# Generated at 2022-06-14 05:03:39.880685
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # 클래스 생성
    logger = logging.getLogger()
    lf = LoggedFunction(logger)

    # 테스트 메소드
    def test_func(a=None, b=None):
        return "test"

    # 데코레이터 적용
    test_func = lf(test_func)
    # 테스트
    assert test_func() == "test"


# Generated at 2022-06-14 05:03:47.130353
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from mock import patch, Mock
    from logging import Logger

    logger_mock = Mock(Logger)

    class Test:
        @LoggedFunction(logger_mock)
        def test_func(self, x, y, z=3):
            return x * y + z

    t = Test()

    res = t.test_func(1, 2)

    logger_mock.debug.assert_any_call("test_func(1, 2)")
    logger_mock.debug.assert_any_call("test_func -> 5")
    assert res == 5


# Generated at 2022-06-14 05:03:58.858971
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import StringIO
    stream = StringIO.StringIO()

    logger = logging.getLogger("testlogger")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(stream=stream)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def func(arg1, arg2=2, arg3="hi"):
        pass

    func(1)
    logger.debug("test")
    func(1, 2)
    func(1, 2, 3)
    func(1, 2, 3, 4)
    func(1, 2, 3, 4, 5)
    func(1, 2, 3, 4, 5, 6)


# Generated at 2022-06-14 05:04:11.756095
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestLogger:
        def __init__(self):
            self.messages = []

        def debug(self, msg):
            self.messages.append(msg)

    def test_func(a, b, c=3):
        return a + b + c

    logger = TestLogger()
    logged_func = LoggedFunction(logger)(test_func)

    logged_func(1, 2)
    assert logger.messages == [
        "test_func(1, 2, c=3) -> 6"
    ]

    logger.messages = []
    logged_func(a=1, c=4, b=2)
    assert logger.messages == [
        "test_func(1, 2, c=4) -> 7"
    ]

# Generated at 2022-06-14 05:04:18.503200
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class DummyLogger:
        def __init__(self):
            self.logs = []
        def debug(self, message) -> None:
            self.logs.append(message)
    l = Dummylogger()
    def test_func(x, y, z=10):
        return x+y+z
    lf = LoggedFunction(l)
    test = lf(test_func)
    # No log generated at first
    assert len(l.logs) == 0
    assert test(1, 2) == 13
    # Log generated upon calling
    assert len(l.logs) == 1
    assert l.logs[0] == 'test_func(1, 2, z=10) -> 13'
    assert test(1, 2, 3) == 6
    # New log generated

# Generated at 2022-06-14 05:04:30.753583
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import mock
    import logging
    from logging import Logger
    from unittest import TestCase
    from unittest.mock import MagicMock

    class test_loggedfunction(TestCase):
        @mock.patch("logging.getLogger")
        def test_loggedfunction_call_with_integer(self, mock_logger):
            @LoggedFunction(mock_logger)
            def add(x, y):
                return x + y

            # Case 1:
            mock_logger.debug = MagicMock()
            result = add(1, 2)
            mock_logger.debug.assert_called_with("add(1, 2)")
            mock_logger.debug.assert_called_with("add -> 3")
            self.assertEqual(3, result)

    test_

# Generated at 2022-06-14 05:04:42.291533
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock, call

    # verify that 1 + 1 = 2
    mock_logger = MagicMock()
    sum_1_1 = LoggedFunction(mock_logger)(lambda x, y: x + y)

    result = sum_1_1(1, 1)
    assert result == 2

    # verify that log output is correct
    assert mock_logger.debug.call_count == 4
    #  call args should be 3 because first call is the one which logs the call to sum_1_1
    assert len(mock_logger.debug.call_args_list) == 3

    assert mock_logger.debug.call_args_list[0] == call('sum_1_1(1, 1)')

# Generated at 2022-06-14 05:06:38.324002
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    import pytest

    if "logging" not in sys.modules or "pytest" not in sys.modules:
        pytest.skip("skipping LoggedFunction unit test", allow_module_level=True)

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def func(a, b="b", c=None):
        logger.debug("func called")
        return "result"

    logged_func = LoggedFunction(logger)(func)

    logged_func(1, c="c")
    logged_func(1, b="b")
    logged_func(2)



# Generated at 2022-06-14 05:06:47.934946
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call

    logger = Mock()
    function = Mock(__name__='do_something')
    function.return_value = "Return value"

    logged_function = LoggedFunction(logger)

    logged_function(function)('arg1', arg2=2)

    assert logger.debug.call_count == 2
    logger.debug.assert_has_calls([
        call("do_something(arg1, arg2=2)"),
        call("do_something -> Return value")
    ])
    function.assert_called_once_with('arg1', arg2=2)

# Generated at 2022-06-14 05:06:53.730422
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Logger()
    decorated_fn = LoggedFunction(logger)(lambda a: None)
    assert hasattr(decorated_fn, '__name__')
    assert decorated_fn.__name__ == 'lambda'
    assert decorated_fn(1) is None
    assert logger.output.getvalue() == "lambda(1)\n"



# Generated at 2022-06-14 05:06:59.296405
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    # Initalize the logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("Test logger")

    # Create decorator
    logged = LoggedFunction(logger)

    class Test(unittest.TestCase):
        # Define test functions
        def test_func_1(self):
            @logged
            def func_1(a, b, c=5):
                assert a == 1 and b == 2 and c == 3
                return "Hello world!"

            # Define arguments
            a = 1
            b = 2
            c = 3

            # Call the function
            result = func_1(a, b, c)
            assert result == "Hello world!"


# Generated at 2022-06-14 05:07:05.200356
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert type(session) == Session
    assert len(session.adapters) == 2
    assert "http://" in session.adapters
    assert type(session.adapters["http://"]) == HTTPAdapter
    assert "https://" in session.adapters
    assert type(session.adapters["https://"]) == HTTPAdapter



# Generated at 2022-06-14 05:07:12.995009
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    self = LoggedFunction(logging.getLogger("test_LoggedFunction___call__"))
    # test that the input arguments are logged before the function is called and the return value is logged once it has completed
    @self
    def testFunc(a,b,c=3):
        return a+b+c
    testFunc(1,2)
    testFunc(1,2,3)
    testFunc(1,2,c=3)
    testFunc(a=1,b=2,c=3)

# Generated at 2022-06-14 05:07:15.362392
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    assert LoggedFunction.__call__(LoggedFunction(logging.Logger)) is not None

# Generated at 2022-06-14 05:07:24.863457
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    @LoggedFunction(logger)
    def f(a, b, c=None):
        return f"""{a} b={b} c={c}"""

    f("A", "bbb", c="cccc")
    # 2019-07-08 14:44:00,711 - __main__ - DEBUG - f('A', 'bbb', c='cccc')
    # 2019-07-08 14:44:00,711 - __main__ - DEBUG - f -> A b=bbb c=cccc

# Generated at 2022-06-14 05:07:37.668874
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import Logger
    from unittest.mock import MagicMock, sentinel

    logger = Logger("test_logger")
    logger_debug = MagicMock(return_value=sentinel)
    logger.debug = logger_debug

    logged_func = LoggedFunction(logger)(lambda x: x)
    logged_func(x=1, y=2)

    # logger.debug was called twice
    assert logger_debug.call_count == 2

    # The first call of logger.debug was a call to the first parameter of constructor LoggedFunction
    assert logger_debug.call_args_list[0][0][0] == "test_logger"

    # The second call of logger.debug was a call to lambda function with parameters x=1 and y=2