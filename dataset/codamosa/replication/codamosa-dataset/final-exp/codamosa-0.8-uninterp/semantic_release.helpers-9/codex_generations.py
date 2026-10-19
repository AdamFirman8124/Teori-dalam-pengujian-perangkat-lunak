

# Generated at 2022-06-14 04:57:32.856682
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        def __init__(self):
            self.info = []
        def debug(self, info):
            self.info.append(info)
    log_to_print = Logger()
    @LoggedFunction(logger=log_to_print)
    def addfunc(a, b):
        return a + b
    addfunc(3, 4)
    assert log_to_print.info[0] == "addfunc(3, 4)"
    assert log_to_print.info[1] == "addfunc -> 7"



# Generated at 2022-06-14 04:57:38.650519
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest.mock

    def foo(a, b="meh"):
        print("FOO")
        return a, b

    log = logging.getLogger("test")
    log.setLevel(logging.DEBUG)
    logged_foo = LoggedFunction(log)(foo)
    with unittest.mock.patch("builtins.print") as print_mock:
        logged_foo("meh", b="meh")
    print_mock.assert_called_with("FOO")

# Generated at 2022-06-14 04:57:50.089777
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import sys
    from io import StringIO
    from unittest import TestCase
    from unittest.mock import patch

    class LoggedFunctionTests(TestCase):
        class TestClass:
            def __init__(self, val1, val2=None):
                self.val1 = val1
                self.val2 = val2

            @LoggedFunction(logger=None)
            def testFunc(self, val1, val2, val3):
                return val1 + val2 * val3

            @LoggedFunction(logger=None)
            def testFunc2(self, val1, val2, val3):
                pass

        output = StringIO()


# Generated at 2022-06-14 04:57:54.517505
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestCaller():
        @LoggedFunction(logger=None)
        def test_method(self, arg1, arg2, kwarg1=5, kwarg2='hello'):
            return arg1 + arg2 + kwarg1 + len(kwarg2)

    obj = TestCaller()
    result = obj.test_method(1, 2, kwarg2='world')
    assert result == 11

# Generated at 2022-06-14 04:58:07.140790
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    import unittest.mock

    example_result = "example_result"

    # Set up logger
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    handler = logging.StringIO()
    log.addHandler(logging.StreamHandler(stream=handler))

    # Set up function to be logged
    function = unittest.mock.MagicMock(return_value=example_result)

    # Decorate function with logging
    logged = LoggedFunction(log)(function)

    # Call function and test logging
    example_arguments = "example_argument_0", "example_argument_1"

# Generated at 2022-06-14 04:58:18.099109
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # set up test
    _logger = Logger(logging.DEBUG)
    _logged_func = LoggedFunction(_logger)
    _func = _test_func()
    _args = (1, 2, 3)
    _kwargs = {'a': 4, 'b': 5}
    # execute
    _func_logged = _logged_func(_func)
    _func_logged(*_args, **_kwargs)
    # verify
    assert len(_logger._test_log_output) == 3

# Generated at 2022-06-14 04:58:29.177012
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    # Setup test logger
    logger = logging.getLogger(__name__)
    logger.level = logging.DEBUG
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    # Setup test function
    def test_function(first_arg, keyword_arg="a", *args, **kwargs):
        print(f"{first_arg} {keyword_arg} {args} {kwargs}")

    # Test __call__
    decorator = LoggedFunction(logger)
    logged_function = decorator(test_function)

# Generated at 2022-06-14 04:58:37.541203
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger: Logger = MagicMock()
    logger.debug = MagicMock(return_value=None)
    logged_function = LoggedFunction(logger=logger)

    @logged_function
    def my_function(a, b):
        return a + b

    my_function(a=1, b=1)

    logger.debug.assert_called_once_with("my_function(1, 1)")
    assert my_function(a=1, b=1) == 2

# Generated at 2022-06-14 04:58:45.627976
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestLogger:
        def __init__(self):
            self.log = []

        def debug(self, s):
            self.log.append(s)

    class TestClass:
        def __init__(self):
            self.logger = TestLogger()

        def __getattr__(self, item):
            return LoggedFunction(self.logger)(FakeFunction)

    class FakeFunction:
        @staticmethod
        def __init__():
            pass

        @staticmethod
        def __call__(*args, **kwargs):
            return

    test_object = TestClass()
    test_object.test_method()
    test_object.test_method(1, "one", kwarg=2)

    assert test_object.logger.log[0] == "test_method()"

# Generated at 2022-06-14 04:58:56.185604
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    function_name="MyFunction"
    function_args=[1, "A", None]
    function_kwargs={"first": "+", "second": "2"}

    # Method __call__ should log the function name with arguments and return value
    # when it is called
    # Solution:
    # 1. Mock the logger
    logger = mock.Mock()
    # 2. Create an object of LoggedFunction with mocked logger
    logged_function = LoggedFunction(logger)
    # 3. Define the mock function which to be logged
    def mock_function(arg1, arg2, arg3):
        return function_args[0] + function_args[1] + function_args[2]
    # 4. Call the logged function
    logged_function(mock_function)(*function_args, **function_kwargs)
    # 5

# Generated at 2022-06-14 04:59:12.516822
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # arrange
    from datetime import datetime
    from random import randint
    from unittest.mock import call, Mock
    from logging import INFO
    from logging import Logger

    def dummy_func(x, y, *args, **kwargs):
        return x + y

    logger: Logger = Mock()
    logger.debug = Mock()
    logger.level = INFO

    sut = LoggedFunction(logger)
    x = randint(0, 100)
    y = randint(0, 100)
    z = randint(0, 100)

    # act
    result = sut(dummy_func)(x, y)

    # assert
    assert result == x + y
    assert logger.debug.call_count == 2

# Generated at 2022-06-14 04:59:23.959560
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Setup
    class FakeLogger:
        def __init__(self):
            self.messages = []

        def debug(self, msg):
            self.messages.append(msg)

    f = FakeLogger()
    logger = LoggedFunction(f)

    def test(a, b, c=3, d=4):
        return a + b + c + d

    # Exercise
    logged_test = logger(test)
    logged_test(1, 2)

    # Verify
    assert len(f.messages) == 2
    assert f.messages[0] == "test(1, 2, c=3, d=4)"
    assert f.messages[1] == "test -> 10"



# Generated at 2022-06-14 04:59:33.774060
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging
    import io
    import contextlib

    class LoggedFunctionTest(unittest.TestCase):
        def setUp(self):
            self.stream = io.StringIO()
            self.handler = logging.StreamHandler(self.stream)
            self.handler.setFormatter(logging.Formatter("%(message)s"))
            self.logger = logging.getLogger()
            self.logger.addHandler(self.handler)
            self.logger.setLevel(logging.DEBUG)

        @contextlib.contextmanager
        def captured_output(self):
            new_out = io.StringIO()
            old_out = sys.stdout

# Generated at 2022-06-14 04:59:43.128578
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Arrange
    def test_func(x, y, z=1):
        return x + y + z
    logger = __create_logger_mock()

    # Act
    logged_func = LoggedFunction(logger)(test_func)
    result = logged_func(11, 22, z=33)

    # Assert
    assert result == 66
    logger.debug.assert_has_calls(
        [
            mock.call(
                "test_func(11, 22, z=33)"
            ),
            mock.call(
                "test_func -> 66"
            )
        ]
    )


# Generated at 2022-06-14 04:59:45.025241
# Unit test for function build_requests_session
def test_build_requests_session():
    import pytest
    from requests.exceptions import HTTPError
    s = build_requests_session()
    with pytest.raises(HTTPError):
        s.get("https://httpbin.org/status/500")

# Generated at 2022-06-14 04:59:58.044312
# Unit test for function build_requests_session
def test_build_requests_session():
    from collections import namedtuple

    from requests import codes

    from smsapi.settings import get_default_mapping
    from smsapi.client import SmsApiPlClient

    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

        def raise_for_status(self):
            return self.status_code

    class MockAdapter(HTTPAdapter):
        def send(self, *args, **kwargs):
            return MockResponse(self.max_retries.total)

    # test with default configuration

    with patch.object(SmsApiPlClient, "__init__", return_value=None) as init:
        mapping = get_default_mapping()
        mapping["http"] = MockAdapter

# Generated at 2022-06-14 05:00:07.985069
# Unit test for function build_requests_session
def test_build_requests_session():
    from requests.packages.urllib3.util.retry import Retry

    # session with no configration
    session = build_requests_session()
    assert session.hooks["response"][0].__name__ == "raise_for_status"
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0

    # session with Retry configured
    default_retry = Retry()
    session = build_requests_session(retry=False)
    assert session.hooks["response"][0].__name__ == "raise_for_status"
    assert session.adapters["http://"].max_retries.total == 0
    assert session.adapters["https://"].max_retries.total == 0

# Generated at 2022-06-14 05:00:18.053603
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    logger = Mock()
    lf = LoggedFunction(logger)

    @lf
    def f(a, b, c):
        return a + b + c

    assert f(1, 2, 3) == 6
    logger.debug.assert_called_once_with("f(1, 2, 3)")
    logger.debug.reset_mock()

    @lf
    def g(a, b, c=None):
        return a + b + (c or 0)

    assert g(1, 2) == 3
    assert g(1, 2, 3) == 6
    logger.debug.assert_called_once_with("g(1, 2, c=None)")
    logger.debug.reset_mock()

    # test that return value is logged if not None


# Generated at 2022-06-14 05:00:24.526641
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from logzero import logger

    logging.basicConfig(level=logging.DEBUG)

    @LoggedFunction(logger)
    def foo(a: int, b: str, c=1, *d, **e):
        pass

    foo(1, "2", 3, 4, 5, x=6, y=7)

# Generated at 2022-06-14 05:00:35.761047
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    log_handler = logging.StreamHandler()
    log_formatter = logging.Formatter("%(asctime)s %(levelname)8s [%(name)s] %(message)s")
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)
    
    @LoggedFunction(logger)
    def test_func1():
        return "result"
    test_func1()
    @LoggedFunction(logger)
    def test_func2(arg1, arg2="def_arg2"):
        return "result"
    test_func2("val1", "val2")
    test_func2("val1")



# Generated at 2022-06-14 05:00:46.885297
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    import pytest

    logger = Mock()
    logged_func = LoggedFunction(logger)

    @logged_func
    def test_func(*args, **kwargs):
        pass

    test_func(1, 2, 3, a=True, b=False)
    logger.debug.assert_called()



# Generated at 2022-06-14 05:00:57.094096
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("test")
    logger_handler = logging.StringIO()
    logger.addHandler(logging.StreamHandler(logger_handler))
    logger.setLevel(logging.DEBUG)
    log_function = LoggedFunction(logger)

    def add_nums(x, y):
        return x + y

    add_nums = log_function(add_nums)
    assert add_nums(1, 2) == 3
    assert logger_handler.getvalue() == "add_nums(1, 2)\nadd_nums -> 3\n"

# Generated at 2022-06-14 05:01:04.306577
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(raise_for_status=False, retry=True)
    assert len(session.hooks["response"]) == 1
    assert session.adapters["https://"].max_retries.total == Retry().total
    session = build_requests_session(raise_for_status=True, retry=False)
    assert len(session.hooks["response"]) == 0
    session = build_requests_session(raise_for_status=False, retry=Retry(total=1))
    assert session.adapters["https://"].max_retries.total == 1



# Generated at 2022-06-14 05:01:12.894338
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    a=1
    b=2.32
    c="string"
    d=[1, 2, 3]

    class Logger:
        def debug(self, msg):
            print(msg)
    
    logger = Logger()
    logged_function = LoggedFunction(logger)
    @logged_function
    def test_function(x, y, z, w):
        return
    
    test_function(a, b, c, d)

#test_LoggedFunction___call__()

# Generated at 2022-06-14 05:01:21.462215
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock

    # Arrange
    my_logger = mock.Mock()
    my_loggedfunc = LoggedFunction(my_logger)

    # Some dummy function
    def my_dummy_function(a: str, b: int, c: str = None) -> str:
        return f"{a}+{b}+{c}"

    # Act
    logged_my_dummy_function = my_loggedfunc(my_dummy_function)
    logged_my_dummy_function("test", 1, c="test2")

    # Assert
    my_logger.debug.assert_called_once_with(
        "my_dummy_function('test', 1, c='test2')"
    )

# Generated at 2022-06-14 05:01:33.974129
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    logger = logging.getLogger("test_LoggedFunction___call__")
    log_stream = io.StringIO()
    handler = logging.StreamHandler(log_stream)
    logger.propagate = False
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    def func1(arg1, arg2):
        return 1

    def func2(arg1, arg2, arg3=3):
        return 2

    def func3():
        return 3

    func1_logged = LoggedFunction(logger)(func1)
    func2_logged = LoggedFunction(logger)(func2)
    func3_logged = LoggedFunction(logger)(func3)

    func1_logged(2, 3)
    func2_log

# Generated at 2022-06-14 05:01:44.173209
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock
    logger = Mock()
    @LoggedFunction(logger)
    def something(x, y=1, z=None):
        return x + y
    something('a', 'b', z='c')
    logger.debug.assert_called_with("something('a', 'b', z='c')")
    something('a', z='c')
    logger.debug.assert_called_with("something('a', z='c')")
    something('a', 0.5)
    logger.debug.assert_called_with("something('a', 0.5)")
    something(1, y=2, z=3)
    logger.debug.assert_called_with("something(1, y=2, z=3)")

# Generated at 2022-06-14 05:01:47.932887
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    debug_text = "DEBUG_TEXT"
    logger.debug(debug_text)

    assert debug_text == "DEBUG_TEXT"

# Generated at 2022-06-14 05:01:55.248530
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import unittest

    # Create a buffer to which we write debug output
    stream = io.StringIO()

    # Create a logger that writes to that buffer
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(stream))

    # Create a logged function
    logged_function = LoggedFunction(logger)

    # Test a function that returns None
    @logged_function
    def none_function(a: int):
        pass

    none_function(1)
    none_function(1, 2, 3)
    none_function(range(10))
    none_function(x=1, y=2)

    # Test a function that returns a result

# Generated at 2022-06-14 05:02:03.441977
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from loguru import logger
    from metatech.step.logger_adapter import LoggerAdapter
    from metatech.step.logger import create_logger

    logger = create_logger(__name__)
    logger = LoggerAdapter(logger, "CallingLogger")
    lf = LoggedFunction(logger)
    @lf
    def add(x, y):
        return x + y
    result = add(1, y=2)
    assert result == 3

# Generated at 2022-06-14 05:02:21.291381
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    logger_stream = io.StringIO()
    logger = logging.getLogger()
    handler = logging.StreamHandler(logger_stream)
    formatter = logging.Formatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def test_func(a, b):
        return a + b

    test_func(1, b=2)
    assert logger_stream.getvalue() == "test_func(1, b=2)\n"

    test_func = LoggedFunction(logger)(test_func)
    test_func(1, b=2)

# Generated at 2022-06-14 05:02:27.181804
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("test_LoggedFunction___call__")
    logF = LoggedFunction(logger = logger)

    @logF
    def foo(*args, **kwargs):
        print(args)
        print(kwargs)

    foo(1, 2, 3, "abc", bar=4, foobar=5)

# Generated at 2022-06-14 05:02:39.527967
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    '''
    unit test for method __call__ of class LoggedFunction
    '''
    def testfunc(arg1, arg2=''):
        '''
        A function for testing.
        :param arg1: first argument.
        :param arg2: second argument.
        :return: "arg1arg2".
        '''
        return str(arg1)+str(arg2)
    import logging
    # create a logger with name "LoggedFunction"
    logger = logging.getLogger("LoggedFunction")
    # set the logging level to DEBUG
    logger.setLevel(logging.DEBUG)
    # create a logging handler
    ch = logging.StreamHandler()
    # create a formatter
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
   

# Generated at 2022-06-14 05:02:52.403585
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    import logging
    import unittest.mock as mock

    def add(a, b):
        return a + b

    def reformat_args(*args):
        return ", ".join([format_arg(x) for x in args])

    def test_LoggedFunction(
        test_case, input_args, input_kwargs, expected_logger_debug, expected_added_output
    ):
        mock_logger = mock.Mock(spec=logging.Logger)
        logged_function = LoggedFunction(mock_logger)

        output = logged_function(add)(*input_args, **input_kwargs)

        mock_logger.debug.assert_called_with(
            f"{add.__name__}({reformat_args(*input_args, **input_kwargs)})"
        )


# Generated at 2022-06-14 05:03:03.022247
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from io import StringIO
    from unittest import TestCase, mock

    log_stream = StringIO()
    logger = mock.Mock()
    logger.debug.side_effect = print

    def my_logged_func(a, b=2, c="c"):
        pass

    logged_func = LoggedFunction(logger)(my_logged_func)

    with TestCase.assertLogs(logger, level="DEBUG") as logs:
        logged_func(1, b="b")
        my_logged_func(1, b="b")

# Generated at 2022-06-14 05:03:07.913464
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class Logger:
        def debug(self, string):
            print(string)
    test_function = lambda arg1, arg2="default": arg1 == arg2
    test_function_decorated = LoggedFunction(logger=Logger())(test_function)
    assert test_function_decorated(arg1="default", arg2="default") == True
    assert test_function_decorated(arg1="default", arg2="not_default") == False
    assert test_function_decorated("default") == True
    assert test_function_decorated("not_default") == False

# Generated at 2022-06-14 05:03:12.856806
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging

    class Test(unittest.TestCase):
        def test(self):
            logger = logging.getLogger(__name__)
            decorated_function = LoggedFunction(logger)(my_function)
            decorated_function()

    def my_function():
        pass

    unittest.main()



# Generated at 2022-06-14 05:03:19.355910
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import MagicMock
    from unittest.mock import patch

    m = LoggedFunction(logger = MagicMock())

    func = MagicMock(spec = ['__name__'])
    func.__name__ = 'func'
    func.return_value = None

    args = [1, '2']
    kwargs = {'x': 3, 'y': '4'}

    logged_func = m(func)
    logged_func(*args, **kwargs)

    func.assert_called_once_with(*args, **kwargs)


# Generated at 2022-06-14 05:03:30.915734
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import unittest

    class Logger(logging.Logger):
        def __init__(self):
            super().__init__("", level=logging.DEBUG)
            self.fh = io.StringIO()
            self.addHandler(logging.StreamHandler(self.fh))

    logger = Logger()

    lf = LoggedFunction(logger)

    @lf
    def f(a, b=True, *args, **kwargs):
        return a + b

    @lf
    def g(*args, **kwargs):
        pass

    f(1, 2, 3, 4, 5)
    g()


# Generated at 2022-06-14 05:03:41.831471
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create a test function
    @LoggedFunction(logger)
    def number_adder(x, y):
        return x + y

    # Pass arguments to test function
    number_adder(1, 2)  
    number_adder(x=1, y=2)  
    number_adder(y=2, x=1)  

# Unit

# Generated at 2022-06-14 05:03:56.177339
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("testlog")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    def test_func(a, b):
        print("test_func called")
        return a + b

    test_func_logged = LoggedFunction(logger)(test_func)
    result = test_func_logged(1, b=2)
    assert result==3

# Generated at 2022-06-14 05:03:59.679168
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    wrong_loggers = [None, [], {}, 0, 1.0, True, object()]
    
    for logger in wrong_loggers:
        with pytest.raises(TypeError):
            function = LoggedFunction(logger)
            function(lambda x : x)

# Generated at 2022-06-14 05:04:08.520711
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    @LoggedFunction(logger)
    def test_function(arg1, arg2, kwarg=None):
        return "my_return_value"

    result = test_function(10, "hello world", kwarg="my_kwarg")

    # Check function return
    assert result == "my_return_value"

    # Redirect logger output to a string, in order to assert the log content
    log_output = io.StringIO()
    handler = logging.StreamHandler(log_output)
    logger.addHandler(handler)

    # Manually re-call logged function, in order to get the logged output

# Generated at 2022-06-14 05:04:17.241943
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from tempfile import TemporaryDirectory
    from common.log_config import configure_logging
    from common.logging_helpers import get_logger
    from common.jsonhelpers import normalize_json

    with TemporaryDirectory() as tmpdirname:
        configure_logging(
            {
                "mode": "DEBUG",
                "format": "%(levelname)s %(name)s:%(lineno)d: %(message)s",
                "handlers": [
                    {
                        "class": "logging.FileHandler",
                        "filename": f"{tmpdirname}/test.log",
                        "formatter": "default",
                    }
                ],
                "loggers": [
                    {"name": "test_LoggedFunction___call__", "level": "DEBUG"}
                ],
            }
        )


# Generated at 2022-06-14 05:04:24.338532
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Unit test for method __call__ of class LoggedFunction.
    """
    # Setup
    from unittest.mock import Mock

    logger = Mock()
    logged_function = LoggedFunction(logger)
    func = Mock()
    # Call
    logged_func = logged_function(func)
    logged_func("test")
    # Verify
    logger.debug.assert_called()

# Generated at 2022-06-14 05:04:33.424374
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    @LoggedFunction(logger=logger)
    def test_func(i, b, *v, s, **k):
        return ("test_func", i, b, v, s, k)

    assert test_func(1, True, 2, 3, s="hello world", k1="v1", k2=True, k3=3) == (
        "test_func",
        1,
        True,
        (2, 3),
        "hello world",
        {"k1": "v1", "k2": True, "k3": 3},
    )

# Generated at 2022-06-14 05:04:43.694512
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestLogger:
        def __init__(self):
            self.output = []

        def debug(self, msg):
            self.output.append(msg)

    f = LoggedFunction(TestLogger())
    f.__call__(lambda : None)
    assert len(f.logger.output) == 1
    f.__call__(lambda x: None)
    assert len(f.logger.output) == 3
    f.__call__(lambda x, y: None)
    assert len(f.logger.output) == 5
    f.__call__(lambda x, y, z: None)
    assert len(f.logger.output) == 7
    f.__call__(lambda x, y, z=0: None)
    assert len(f.logger.output) == 9


# Generated at 2022-06-14 05:04:54.713247
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Create a logger
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
    # Create an LoggedFunction object
    logged_function = LoggedFunction(logger)
    # Decorated a test function
    @logged_function
    def add(a, b):
        return a + b
    # Call the test function with different input arguments
    add(1, 2)
    add(1, b=2)
    # Close the logger
    logger.removeHandler(stream_handler)
    stream_handler.close()


# Generated at 2022-06-14 05:04:59.875726
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger()

    @LoggedFunction(logger)
    def test_func(arg1, arg2, kwarg1='default'):
        return [arg1, arg2, kwarg1]

    test_func('A', 3)
    test_func('A', 3, 'test')



# Generated at 2022-06-14 05:05:09.927679
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.NullHandler())

    @LoggedFunction(logger)
    def fn1(name):
        return f"Hello {name}"

    fn1("Bob")
    # ----------
    # INFO:__main__:fn1(Bob)
    # INFO:__main__:fn1 -> Hello Bob
    # ----------

    @LoggedFunction(logger)
    def fn2(x, y, *, z="Zed"):
        return f"{x} * {y} * {z}"

    fn2(2, 3, z="Zero")
    # ----------
    # INFO:__main__:fn2(2, 3, z=Zero)
    #

# Generated at 2022-06-14 05:05:42.268889
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest.mock as mock

    logger = mock.Mock(spec=logging.Logger)

    test_fn = mock.Mock()
    test_fn.__name__ = "test_fn"

    logged_fn = LoggedFunction(logger)(test_fn)
    logged_fn(1, 2, b=3)
    test_fn.assert_called_once_with(1, 2, b=3)
    logger.debug.assert_called_once_with(
        "test_fn('1', '2', b='3')",
    )

    logged_fn(4, 5)
    test_fn.assert_called_with(4, 5)
    logger.debug.assert_called_with(
        "test_fn('4', '5')",
    )

   

# Generated at 2022-06-14 05:05:52.038543
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    test__LoggedFunction___call__ - Unit test for method __call__ of class LoggedFunction
    :return:
    """
    from unittest.mock import Mock
    from unittest.mock import patch
    from unittest import TestCase
    from test.test_logging import DummyLogger

    def fake_function(*args, **kwargs):
        return args, kwargs

    #  No arguments
    with patch.object(DummyLogger, "debug") as mock_debug:
        logger = DummyLogger()
        logged_function = LoggedFunction(logger=logger)

        wrapped_function = logged_function(fake_function)
        wrapped_function()

        mock_debug.assert_called_with("fake_function()")

# Generated at 2022-06-14 05:06:02.347551
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    # Create mock logging handler
    import unittest.mock
    handler = unittest.mock.Mock()
    log = logging.getLogger("")
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    # Create decorator
    decorator = LoggedFunction(log)

    # Define a test class
    class TestClass(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

        @decorator
        def method(self, c, d):
            return self.a, self.b, c, d

    # Create an instance of TestClass
    instance = TestClass(1, 2)
    # Test call of method
    assert instance.method(3, 4)

# Generated at 2022-06-14 05:06:08.975361
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MyLogger:
        def __init__(self):
            self.message = None

        def debug(self, msg):
            self.message = msg

    lf = LoggedFunction(MyLogger())

    @lf
    def add(x, y):
        return x + y

    assert add(1,2) == 3
    assert lf.logger.message == "add(1, 2)"

    add(1, y=2)
    assert lf.logger.message == "add(1, y=2)"
    assert add.__name__ == "add"


# Generated at 2022-06-14 05:06:18.484462
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Tests the __call__ method of class LoggedFunction.

    :return: N/A
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    lf = LoggedFunction(logger = logger)

    @lf
    def myfunc(a, b, c = 1):
        return a + b + c
    
    myfunc(1, 2)
    myfunc(1, 2, c = 3)
    myfunc(1, 2, c = "abc")

if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:06:28.350993
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import Logger, ERROR

    class TestLogger(Logger):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.messages = []

        def handle(self, record):
            self.messages.append(record.getMessage())

    def dummy_function(a, b, c=1, d=2):
        return 2 * a + b + c + d

    logger = TestLogger("logger", ERROR)
    decorated_function = LoggedFunction(logger)(dummy_function)

    decorated_function(1, 2)
    assert logger.messages == [
        "dummy_function(1, 2, c=1, d=2)",
        "dummy_function -> 7",
    ]


# Generated at 2022-06-14 05:06:39.884403
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    @LoggedFunction(logger)
    def prn(a1):
        print(a1)

    prn(123)
    prn(123, 456)
    prn(a1='123')
    prn(a1='123', a2='456')


if __name__ == '__main__':
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:06:49.241354
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    class TestLogger:

        def __init__(self):
            self.log_records = []

        def debug(self, *args):
            self.log_records.append(args)

    test_logger = TestLogger()

    @LoggedFunction(test_logger)
    def test_function(arg1, arg2="default", *, kwarg1, kwarg2="default"):
        pass

    test_function(1, 2, kwarg1=3, kwarg2=4)
    print(test_logger.log_records)
    assert test_logger.log_records == [
        ("test_function(1, 2, kwarg1=3, kwarg2=4)",),
        ("test_function -> None",)
    ]



# Generated at 2022-06-14 05:06:56.425347
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MyLogger:
        def __init__(self):
            self.debug_calls = []
        
        def debug(self, s):
            self.debug_calls.append(s)
    
    mylogger = MyLogger()
    logged_foo = LoggedFunction(mylogger)(foo)
    logged_foo(x=1, y=2, z=3)
    assert mylogger.debug_calls == ['foo(x=1, y=2, z=3)', 'foo -> foo(1, 2, 3)']


# Generated at 2022-06-14 05:07:07.969759
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import os
    import sys
    import time

    class MyException(Exception): pass

    log = logging.getLogger("logger")
    log.setLevel(20)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log.addHandler(ch)

    def f1(a, b, c=None):
        return a + b + 1

    def f2():
        return

    def f3(a, b, c=[]):
        return a + b + (c[0] if c else 0)

    def f4(a, b):
        raise MyException()
