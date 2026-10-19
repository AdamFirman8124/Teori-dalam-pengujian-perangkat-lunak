

# Generated at 2022-06-14 04:57:36.791711
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestClass:
        def method_to_be_decorated(self, a, b=5, c=None):
            return a + b

    logger = logging.getLogger("test")
    logged_fn = LoggedFunction(logger)
    result = logged_fn(TestClass.method_to_be_decorated)
    result("a", b="bbb")



# Generated at 2022-06-14 04:57:47.726972
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger, Logger, DEBUG

    class MockLogger(Logger):
        @classmethod
        def __call__(cls, name):
            return cls()

        def __init__(self) -> None:
            super(MockLogger, self).__init__("Test")
            self.output = ""

        def log(self, level, msg, *args):
            if args:
                self.output += msg % args
            else:
                self.output += msg

        def get_output(self):
            output = self.output
            self.output = ""
            return output

    logger = getLogger("Test")
    logger.setLevel(DEBUG)
    logger.propagate=False
    logger.handlers=[MockLogger()]

    def f(x):
        return x



# Generated at 2022-06-14 04:57:52.541528
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Arrange
    logger = Mock(["debug"])

    # Act
    @LoggedFunction(logger)
    def test_method(*args, **kwargs):
        return args, kwargs

    # Assert
    assert test_method(1, 2, 3, c=4, d=5) == ((1, 2, 3), {"c": 4, "d": 5})

    args = logger.debug.call_args_list[0][0][0]
    kwargs = logger.debug.call_args_list[0][0][1]

# Generated at 2022-06-14 04:58:03.010741
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Initialization
    import logging
    from .utils import get_logger
    logging.basicConfig(level=logging.INFO)
    logger = get_logger(name=__name__)
    logger.setLevel(logging.DEBUG)
    debug_logging = LoggedFunction(logger=logger)
    @debug_logging
    def f(x, y=3):
        return x*y
    @debug_logging
    def g(x=1, y=2, z=3, *t, **u):
        return x*y*z
    @debug_logging
    def h():
        return None
    # Test
    assert(f(1)==3)
    assert(f(x=3, y=1)==3)
    assert(g()==6)

# Generated at 2022-06-14 04:58:13.415094
# Unit test for function build_requests_session
def test_build_requests_session():
    # Test normal usage
    import requests

    session = build_requests_session(raise_for_status=True, retry=True)
    assert isinstance(session, requests.Session)
    assert session.hooks == {"response": [lambda r, *args, **kwargs: r.raise_for_status()]}
    assert session.adapters.keys() == {'http://', 'https://'}
    retry = session.adapters['http://']._max_retries
    assert isinstance(retry, Retry)
    assert retry.total == 10
    assert retry.read == 10
    assert retry.connect == 10
    assert not retry.is_method_retryable()('GET')

    # Test raise for status = false

# Generated at 2022-06-14 04:58:23.671114
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    # Create mock logger
    class MockLogger:
        def debug(self, msg):
            self.message = msg

    logger = MockLogger()

    # Create a function to wrap
    def test_function(string: str, number: int) -> int:
        return number

    # Wrap the function
    test_function = LoggedFunction(logger)(test_function)

    # Call the wrapped function
    test_function("hello world", 3)

    # Check the logged message
    assert logger.message == "test_function('hello world', 3)"

    # Check the output
    assert test_function("hello world", 3) == 3

# Test for function build_requests_session

# Generated at 2022-06-14 04:58:36.182248
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import patch, MagicMock
    from io import StringIO

    Logger = MagicMock()

    logger = logging.getLogger('LoggedFunction__call__')
    logger.setLevel(logging.DEBUG)
    stream = StringIO()
    logger.addHandler(logging.StreamHandler(stream))

    log = LoggedFunction(logger)
    def f(a):
        return a+a
    f = log(f)

    f(1)
    stream.seek(0)
    assert stream.read() == """f(1)
f -> 2
"""

    stream.seek(0)
    f('hello')
    stream.seek(0)
    assert stream.read() == """f('hello')
f -> hellohello
"""



# Generated at 2022-06-14 04:58:42.972660
# Unit test for function build_requests_session
def test_build_requests_session():
    ses = build_requests_session()
    # it is a session
    assert isinstance(ses, Session)
    # it has raise_for_status hook
    assert isinstance(ses.hooks, dict)
    assert "response" in ses.hooks
    assert len(ses.hooks["response"]) == 1
    # it has retries
    assert ses.adapters == {"http://": HTTPAdapter(max_retries=Retry()),
                            "https://": HTTPAdapter(max_retries=Retry())}

# Generated at 2022-06-14 04:58:50.048892
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class CustomLogger:
        def __init__(self):
            self.msg = None

        def debug(self, msg):
            self.msg = msg

    def fun(a: int, b: str) -> int:
        return a + len(b)

    cl = CustomLogger()
    lf = LoggedFunction(cl)
    lf(fun)(1, "x")
    assert cl.msg == "fun(1, 'x')"
    assert fun(1, "x") == lf(fun)(1, "x")
    assert lf(fun)(1, "x") == 2

# Generated at 2022-06-14 04:58:59.225640
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys
    # Create a logger which send log to a buffer
    str_buffer = io.StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(str_buffer)
    logger.addHandler(handler)
    # Define a test function
    def test_function(a: int, b: int, c=None, d=None):
        return a + b + (c or 0) + (d or 0)
    test_function.__name__ = "test_function"  # give the function a name
    # Create a LoggedFunction instance
    wrapper = LoggedFunction(logger)
    # Wrap the above test function
    wrapped_function = wrapper(test_function)
    # Call the wrapped function with

# Generated at 2022-06-14 04:59:08.103253
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger()
    decorated_function = LoggedFunction(logger)
    @decorated_function
    def x(a=1, b=2):
        return a + b
    x()

# Generated at 2022-06-14 04:59:12.891422
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(raise_for_status=True, retry=True)
    while True:
        try:
            resp = session.get("https://httpbin.org/anything?q=abc")
            assert resp.json()["args"]["q"] == "abc"
        except:
            pass
        else:
            break


# Generated at 2022-06-14 04:59:25.110436
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    import inspect

    class MockLogger:
        def __init__(self):
            self.log = []

        def debug(self, message):
            self.log.append(message)

    logger = MockLogger()

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.logged_function = LoggedFunction(logger)

        def test_log_with_args(self):
            def dummy(a, b, c):
                pass

            logged_dummy = self.logged_function(dummy)
            logged_dummy(1, 2, 3)


# Generated at 2022-06-14 04:59:30.887199
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logged = LoggedFunction(logger)

    @logged
    def concat(x, y):
        return x + y

    concat("Hello ", "World!")
    concat("Hello ", y="World!")
    concat(x="Hello ", y="World!")
    concat(y="World!", x="Hello ")
    concat(x="Hello ", y="World!", a=1)
    concat(3, 4)
    concat(3, y=4)
    concat(x=4, y=4)
    concat(y=4, x=4)

# Generated at 2022-06-14 04:59:43.082278
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import tempfile

    logger = logging.getLogger("test")
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    Decorator = LoggedFunction(logger)

    @Decorator
    def my_func(x, y, z=None):
        return x + y * z

    my_func(1, 2, 3)
    my_func(1, 2, z=3)
    my_func(1, y=2, z=3)


# Generated at 2022-06-14 04:59:45.693085
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger(__name__)
    lf = LoggedFunction(logger)
    @lf
    def test_func(a, b, c='c', d=None):
        print(a, b, c, d)
    test_func(1, 2, 3, 4)

# Generated at 2022-06-14 04:59:46.711232
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    pass

# Generated at 2022-06-14 04:59:58.901120
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    # setup a logger and a mock function to be wrapped by LoggedFunction
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def mock_function(a, b, c=0, d=1, *args, **kwargs):
        pass

    # call the mock function
    mock_function(1, 2, 3, d=4, e=5, f=6)
    # check the log output
    output = sys.stdout.getvalue().strip()

# Generated at 2022-06-14 05:00:07.954119
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO

    import re

    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.DEBUG)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    logger.info('this is info')
    logger.warning('this is warning')
    logger.info('this is info again')

    logdata = stream.getvalue()

    assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} - INFO - this is info',logdata)



# Generated at 2022-06-14 05:00:17.978063
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest

    class LoggedFunctionTest(unittest.TestCase):
        def test_function_returns_none(self):
            import logging
            import io
            import contextlib

            @LoggedFunction(logger=logging.getLogger(__name__))
            def f(a, b):
                return a

            # Capture stdout output
            log_capture_string = io.StringIO()
            with contextlib.redirect_stdout(log_capture_string):
                result = f(1, 2)

            self.assertEqual(result, 1)
            self.assertEqual(
                log_capture_string.getvalue(), "INFO:root:f(1, 2)\nINFO:root:f -> 1\n"
            )


# Generated at 2022-06-14 05:00:33.446704
# Unit test for function build_requests_session
def test_build_requests_session():
    import contextlib
    import requests
    from requests.exceptions import ConnectionError

    with contextlib.ExitStack() as stack:
        session = stack.enter_context(build_requests_session())
        assert isinstance(session, requests.Session)
        try:
            session.get("https://www.google.com/example")
        except ConnectionError:
            pass
        else:
            assert False

        session = stack.enter_context(build_requests_session(raise_for_status=False))
        assert isinstance(session, requests.Session)
        r = session.get("https://www.google.com/example")
        assert r.status_code == 404

        session = stack.enter_context(build_requests_session(retry=False))
        assert isinstance(session, requests.Session)

# Generated at 2022-06-14 05:00:45.825410
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    from io import StringIO
    from logging import Logger, root
    from logging import DEBUG, StreamHandler

    class TestLogger(Logger):
        def debug(self, msg):
            self.msgs.append(msg)

        def reset(self):
            self.msgs = []

    logger = TestLogger("testlogger")
    logger.reset()
    logger.setLevel(DEBUG)
    logger.propagate = False

    @LoggedFunction(logger)
    def func(a, b, c=1):
        return a

    func("b", "c")
    assert logger.msgs == ["testlogger -> 'a'"]
    logger.reset()
    func("b", "c", 1)

# Generated at 2022-06-14 05:00:55.902984
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import sys
    import traceback
    import unittest

    class LoggedFunctionTest(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger("test")
            self.handler = logging.StreamHandler(sys.stderr)
            self.handler.setFormatter(logging.Formatter("%(message)s"))
            self.logger.addHandler(self.handler)
            self.logger.setLevel(logging.DEBUG)
            self.func_name = "my_func"
            self.use_retval = True
            self.retval = "my_retval"
            self.test_args = ("arg1", "arg2")
            self.test_kwargs = {"kwarg1": "val1"}


# Generated at 2022-06-14 05:01:04.722826
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger("LoggedFunction")
            self.logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)

            self.logger.addHandler(ch)

        def tearDown(self):
            self.logger.handlers.clear()

        @LoggedFunction(logger=logger)
        def test_func1(self, *args):
            return args[0] * args[1]


# Generated at 2022-06-14 05:01:13.759349
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    mock_logger = unittest.mock.MagicMock()

    def my_func(a1, a2, k1=False):
        return a1 + a2

    # Call my_func
    my_logged_func = LoggedFunction(mock_logger)(my_func)
    result = my_logged_func(1, 2)
    # Assert result
    assert result == 3

    # Assert loggers
    mock_logger.debug.assert_called_once_with("my_func(1, 2)")
    mock_logger.debug.assert_called_with("my_func -> 3")
    mock_logger.debug.reset_mock()
    # Call my_func
    my_logged_func = LoggedFunction(mock_logger)(my_func)
    result

# Generated at 2022-06-14 05:01:21.829533
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session()
    assert isinstance(session.adapters.get("http://"), HTTPAdapter)
    assert isinstance(session.adapters.get("https://"), HTTPAdapter)
    retry_config = session.adapters.get("http://")._retry.get_backoff_time()
    assert retry_config == Retry.BACKOFF_MAX
    assert not session.hooks

    session = build_requests_session(False)
    assert isinstance(session.adapters.get("http://"), HTTPAdapter)
    assert isinstance(session.adapters.get("https://"), HTTPAdapter)
    retry_config = session.adapters.get("http://")._retry.get_backoff_time()
    assert retry_config == Retry.BACKOFF_MAX

# Generated at 2022-06-14 05:01:34.164206
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Test method __call__ of LoggedFunction
    """

    import logging
    import io
    import sys

    class MockLogger(logging.Logger):
        def __init__(self):
            super(MockLogger, self).__init__(name=__name__)
            formatter = logging.Formatter(fmt="%(levelname)s: %(message)s")
            self.stream = io.StringIO()
            handler = logging.StreamHandler(self.stream)
            handler.setFormatter(formatter)
            self.addHandler(handler)

        def close(self):
            self.removeHandler(self.handlers[0])
            self.handlers[0].close()
            self.stream.close()


# Generated at 2022-06-14 05:01:46.469053
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    @LoggedFunction(logger)
    def Something():
        return 'Just a string'

    @LoggedFunction(logger)
    def SomethingWithArgs(a, b, c):
        return a + b + c

    @LoggedFunction(logger)
    def SomethingWithKwargs(a=0, b=1):
        return a + b

    @LoggedFunction(logger)
    def SomethingWithArgsAndKwargs(a, b=0, c=0):
        return a + b + c

    @LoggedFunction(logger)
    def SomethingWithDuplicatedArgsAndKwargs(a, b=0, c=0):
        return a + b + c


# Generated at 2022-06-14 05:01:53.592693
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from .logging import configure_logging

    logger = configure_logging(name="testing")

    # Create decorator
    logged_func = LoggedFunction(logger)

    # Decorate a test function
    @logged_func
    def my_func(a, b):
        return a + b
    my_func(1, 2)

    logger.setLevel(logging.INFO)
    my_func(1, 2)



# Generated at 2022-06-14 05:02:05.369884
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # The following is to make sure the test can pass, it may not be correct
    import logging
    import re
    import sys

    logger = logging.Logger("dummy")
    handler = logging.StreamHandler(sys.stdout)

    logger.addHandler(handler)

    pattern_function = r"function\((args, \*\*kwargs\))"
    pattern_args = r"args=args, kwargs=kwargs"
    pattern_log_result = r"\(\*\*kwargs\)"

    @LoggedFunction(logger)
    def function(args, **kwargs):
        return kwargs

    function(args=1, key="value")

    handler.flush()


# Generated at 2022-06-14 05:02:22.650493
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestLogger:
        def debug(self, msg):
            self.last_msg = msg
    def testfunc(a, b, c=3, d=4):
        return a + b + c + d
    logger = TestLogger()
    loggedfunc = LoggedFunction(logger)
    loggedfunc(testfunc)
    loggedfunc(testfunc)(1, 2)
    assert 'testfunc()' == logger.last_msg
    loggedfunc(testfunc)(1, 2, 3)
    assert 'testfunc(1, 2, c=3)' == logger.last_msg
    loggedfunc(testfunc)(1, 2, 3, 4)
    assert 'testfunc(1, 2, c=3, d=4)' == logger.last_msg
    loggedfunc(testfunc)(1, b=2)

# Generated at 2022-06-14 05:02:35.824840
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest

    from unittest.mock import Mock

    mocklogger = Mock()
    logged_func = LoggedFunction(mocklogger)

    def test_func(a, b, c, *, d, e, f, g=None):
        pass

    kwargs = dict(d=1, e=2, f=3, g=4)
    args = (5, 6, 7)
    log_message = "test_func(5, 6, 7, d=1, e=2, f=3, g=4)"

    logged_func(test_func)(*args, **kwargs)

    mocklogger.debug.assert_called_once_with(log_message)


if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:02:42.525694
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    logger = mock.Mock()
    decorator = LoggedFunction(logger)
    @decorator
    def test_func(arg1, arg2=2, arg3=3):
        return "result"
    test_func(1, 2)
    test_func(1, arg3=3, arg2=2)
    logger.debug.assert_has_calls([
        mock.call("test_func(1, 2)"),
        mock.call("test_func(1, arg2=2, arg3=3)")
    ])
    assert test_func(1) == "result"
    logger.debug.assert_called_with("test_func -> result")

# Generated at 2022-06-14 05:02:50.857956
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    # create an instance of LoggedFunction
    func_wrapper = LoggedFunction(logger)

    # use the instance to decorate a function
    @func_wrapper
    def log_call(a, b=None):
        pass

    # call the decorated function
    log_call('1', b='2')

# Generated at 2022-06-14 05:03:01.407959
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import patch

    from log_util import get_logger

    with patch("log_util.get_logger") as get_logger_mock:
        log_mock = get_logger_mock.return_value
        logger = get_logger()
        func = LoggedFunction(logger)
        @func
        def func_with_no_args():
            pass
        @func
        def func_with_args(a, b = "foo", c = 4):
            return "res"
        @func
        def func_with_ko_args(a, b = "foo", c = 4, *ko_args, **ko_kwargs):
            return "res"
        func_with_no_args()

# Generated at 2022-06-14 05:03:12.856773
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = Mock()

    # 0 arguments
    @LoggedFunction(logger)
    def foo():
        return "bar"

    foo()

    logger.debug.assert_called_once_with("foo()")
    logger.debug.reset_mock()

    # 1 argument
    @LoggedFunction(logger)
    def foo(arg1):
        return "bar"

    foo("f")

    logger.debug.assert_called_once_with("foo('f')")
    logger.debug.reset_mock()

    # 2 arguments
    @LoggedFunction(logger)
    def foo(arg1, arg2):
        return "bar"

    foo("f", 2)

    logger.debug.assert_called_once_with("foo('f', 2)")
    logger.debug.reset_mock

# Generated at 2022-06-14 05:03:20.010482
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import logging

    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(io.StringIO())
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

    @LoggedFunction(logger=logger)
    def get_greeting(name):
        return f'Hello, {name}!'

    logger.info('Invoke get_greeting...')
    assert get_greeting('Rob') == 'Hello, Rob!'

    logger.info('Invoke get_greeting...')
    assert get_greeting('John') == 'Hello, John!'


# Generated at 2022-06-14 05:03:31.313452
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from unittest.mock import patch
    from contextlib import contextmanager

    @contextmanager
    def capture_logger_output():
        """
        Capture output to a logger.

        Returns a context manager which logs all messages sent to the
        specified logger (and its descendants) to the given object.
        :return:
        """
        test_handler = logging.StreamHandler()
        logging.getLogger().addHandler(test_handler)
        with patch.object(test_handler, "handle") as mocked_handle:
            yield mocked_handle.call_args[0][1].strip()
        logging.getLogger().removeHandler(test_handler)

    # Case 1: The input arguments are logged before the function is called, and the return value is logged
    # once it has completed.

# Generated at 2022-06-14 05:03:37.359022
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MockLogger:
        def debug(self, msg):
            print(msg)

    mock_logger = MockLogger()
    func = lambda x, y, z=5: x + y + z
    decorated_func = LoggedFunction(mock_logger)(func)
    decorated_func(1, 2)
    decorated_func(3, 4, 5)
    print()


if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:03:44.962698
# Unit test for function build_requests_session
def test_build_requests_session():
    import requests

    def _test_session(session):
        session.get("http://httpbin.org/status/400")

    def _test_session_raise_for_status(session):
        with pytest.raises(requests.exceptions.HTTPError):
            session.get("http://httpbin.org/status/400")

    # basic test
    for raise_for_status in (True, False):
        session = build_requests_session(raise_for_status)
        if raise_for_status:
            _test_session_raise_for_status(session)
        else:
            _test_session(session)

    # test retry configuration
    for retry in (True, False, 1, Retry()):
        session = build_requests_session(retry=retry)
        _test

# Generated at 2022-06-14 05:04:01.703223
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Test logger
    class Logger:
        def debug(self, record):
            self.record = record

    logger = Logger()
    logged_func = LoggedFunction(logger)
    # logger.record should be None if no function is called
    assert logger.record is None
    
    # Test the function with only arguments
    def func1(x, y):
        return x + y

    func1 = logged_func(func1)
    func1(1, 2)
    assert logger.record == "func1(1, 2)"

    # Test the function with keyword arguments
    def func2(x, y, z=3):
        return x + y + z

    func2 = logged_func(func2)
    func2(1, 2)

# Generated at 2022-06-14 05:04:12.634382
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logger = logging.getLogger("Logger")

    @LoggedFunction(logger)
    def foo(a, b, c=3, *args, **kwargs):  # do not use this kind of args
        return a * b * c + 42

    foo(1, 2, 3, 4, 5)
    foo(1, b=2, c=3, bar=4, baz=5)
    foo(1, 2, args=[4, 5])
    foo(1, b=2, kwargs={'bar': 4, 'baz': 5})

test_LoggedFunction___call__()

# Generated at 2022-06-14 05:04:19.453123
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from app.utils.logging_helper import get_logger
    from unittest.mock import call, Mock
    
    logging = get_logger(__name__)
    mock_logger = Mock(logging.__class__)
    mock_logger.debug = Mock()
    instance = LoggedFunction(mock_logger)
    
    @instance
    def test_func(*args, **kwargs):
        return 1
    
    test_func(0, arg=-1, arg_2=0)
    assert mock_logger.debug.call_args == call("test_func(0, arg='-1', arg_2=0)")
    assert mock_logger.debug.call_args_list[1] == call("test_func -> 1")
    

# Generated at 2022-06-14 05:04:31.241749
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Unit test for method __call__ of class LoggedFunction.
    """

    import unittest
    import unittest.mock

    class TestLogger:
        def __init__(self):
            self.out = []

        def debug(self, s):
            self.out.append(s)

        def __contains__(self, s):
            return s in self.out


    class LoggedFunction_TestCase(unittest.TestCase):

        def test_simple(self):
            def foo(a, b, c):
                return a + b + c

            logger = TestLogger()
            dec = LoggedFunction(logger)

            foo2 = dec(foo)

            foo2(1, 2, 3)


# Generated at 2022-06-14 05:04:38.897388
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    class A:
        @LoggedFunction(logger)
        def square(self, x):
            return x * x

        @LoggedFunction(logger)
        def _private(self, x):
            return x * x

    # test print return of function which with __name__ square
    a = A()
    a.square(4)

    # test print return of function which start with __
    a._private(4)

# Generated at 2022-06-14 05:04:44.941581
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    :return:
    """
    def testFunc(*args, **kwargs):
        print(f"testFunc->{args},{kwargs}")

    class Logger:

        def debug(self, line):
            print(f"logger->{line}")

    logger = Logger()
    loggedFunction = LoggedFunction(logger)
    with logging.basicConfig(level=logging.DEBUG):
        loggedFunction(testFunc)('a', 'b', kwarg1='1', kwarg2='2')


# Generated at 2022-06-14 05:04:57.988964
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Test:
        def __init__(self):
            self.logger = logging.getLogger('Test')

        @LoggedFunction(logger=logging.getLogger('Test'))
        def f(self, arg1, arg2):
            return arg1 + arg2

        @LoggedFunction(logger=logging.getLogger('Test'))
        def f2(self, a, b, c=None, d='hello'):
            return (a, b, c, d)

        @LoggedFunction(logger=logging.getLogger('Test'))
        def g(self, arg1):
            return

    from sys import stdout

    logger = logging.getLogger('Test')
    handler = logging.StreamHandler(stdout)

# Generated at 2022-06-14 05:05:09.348155
# Unit test for method __call__ of class LoggedFunction

# Generated at 2022-06-14 05:05:15.027337
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    print("testing LoggedFunction.__call__")

    logger = logging.getLogger("test.logged")

    # Define a function
    @LoggedFunction(logger)
    def test(x, y):
        return x + y

    # Make sure logging is enabled
    logger.setLevel(logging.DEBUG)

    # Call the function
    print(test(3, 4))



# Generated at 2022-06-14 05:05:22.194035
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    from nose.tools import assert_true, assert_is_instance, assert_equals
    from unittest.mock import Mock

    raise_for_status = False
    retry = True
    session = build_requests_session(raise_for_status, retry)
    assert_true(callable(session.get))
    assert_true(callable(session.post))
    assert_is_instance(session.mount("http://", HTTPAdapter()), Session)
    assert_is_instance(session.mount("https://", HTTPAdapter()), Session)
    assert_equals(session.hooks["response"], [])

    raise_for_status = True

# Generated at 2022-06-14 05:05:53.340186
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import logging
    import unittest
    from contextlib import redirect_stdout

    class LoggedFunctionTests(unittest.TestCase):
        """Tests for LoggedFunction."""

        def test_addition(self):
            f = io.StringIO()
            logger = logging.getLogger("test")
            logger.addHandler(logging.StreamHandler(f))
            logger.setLevel(logging.DEBUG)
            @LoggedFunction(logger)
            def add(x, y):
                return x + y
            logger.info("Before function call")
            with redirect_stdout(f):
                add(5, 3)
            logger.info("After function call")

# Generated at 2022-06-14 05:05:55.690665
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("test")
    def f(x, y=3):
        return x**y
    test = LoggedFunction(logger)
    ff = test(f)
    ff(2)
    ff(3, 4)

# Generated at 2022-06-14 05:06:05.933072
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    test_logged_func_1 = LoggedFunction(logger)(lambda x, y, z=3: x + y + z)
    test_logged_func_2 = LoggedFunction(logger)(lambda x, y=2, z=3: x + y + z)
    test_logged_func_3 = LoggedFunction(logger)(lambda x, *args, **kwargs: x)
    test_logged_func_4 = LoggedFunction(logger)(lambda x, **kwargs: x)
    test_logged_func_5 = LoggedFunction(logger)(lambda x: x)

    test_logged_func_1(1, 2)

# Generated at 2022-06-14 05:06:16.530245
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    result_string = "test_result"
    result = None
    func_name = "test_func"
    args = [1, 2, "a", "b"]
    kwargs = {"a": 3, "b": 4}

    class DummyLogger:
        def debug(self, msg):
            nonlocal result
            result = msg

    logger = DummyLogger()
    logged_function = LoggedFunction(logger)

    @logged_function
    def test_func():
        return result_string

    test_func(args, kwargs)
    expected_msg = f"{func_name}({', '.join(map(str, args))}, a={kwargs['a']}, b={kwargs['b']})"
    assert result == expected_msg

    result = None

# Generated at 2022-06-14 05:06:17.187587
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    pass

# Generated at 2022-06-14 05:06:27.876260
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import StringIO
    from unittest.mock import patch

    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    log_stream = StringIO.StringIO()
    logger.addHandler(logging.StreamHandler(log_stream))
    
    logged_func = LoggedFunction(logger)(lambda *args: None)
    logged_func(1, 2, 3, 4, a="a", b="b", c="c", d="d")
    assert log_stream.getvalue().endswith(
        "test_logger INFO __call__: test_logger(1, 2, 3, 4, a='a', b='b', c='c', d='d')\n"
    )

    log_stream.truncate(0)


# Generated at 2022-06-14 05:06:37.920774
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def test_logged_function():
        print("It's ok")

    test_logged_function()

# Generated at 2022-06-14 05:06:47.506168
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    test_handler = logging.NullHandler()
    logger.addHandler(test_handler)
    test_logged_function = LoggedFunction(logger)
    test_decorated_func = test_logged_function(lambda a, b, c=2, d=4: a + b + c + d)
    test_decorated_func(1, 2, 3)
    test_decorated_func.__name__

# Generated at 2022-06-14 05:06:52.971271
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    @LoggedFunction(logger)
    def test_func(arg1, karg1=1, karg2=2):
        return f"{arg1} {karg1} {karg2}"

    assert test_func("this is arg1", karg2=3) == "this is arg1 1 3"

# Generated at 2022-06-14 05:06:57.581823
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import getLogger, DEBUG

    logger = getLogger("")
    function = LoggedFunction(logger)
    logger.setLevel(DEBUG)

    @function
    def test_function(string, integer):
        print("I am running.")
        return string + f"{integer}"

    assert test_function("foo", 10) == "foo10"
    # I am running
    # test_function('foo', 10) -> foo10
    # test_function('foo', 10)
