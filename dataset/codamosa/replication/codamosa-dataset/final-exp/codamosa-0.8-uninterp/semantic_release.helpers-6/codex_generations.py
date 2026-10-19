

# Generated at 2022-06-14 04:57:38.267837
# Unit test for method __call__ of class LoggedFunction

# Generated at 2022-06-14 04:57:49.608645
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import pprint
    import sys

    def my_function(arg1, arg2, keyword1=1, keyword2=2):
        return f"{arg1}{arg2}{keyword1}{keyword2}"

    stream = sys.stderr
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(stream)
    logger.addHandler(stream_handler)

    logged_function = LoggedFunction(logger)
    my_logged_function = logged_function(my_function)

    assert my_logged_function(1, 2) == "1212"
    assert my_logged_function(1, 2, keyword1=3) == "1232"

# Generated at 2022-06-14 04:57:55.875198
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Arrange
    import logging

    logger = logging.getLogger("UnitTest_test_LoggedFunction___call__")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    l_f = LoggedFunction(logger)

    func = lambda a: a + 1

    # Act
    logged_func = l_f(func)

    # Assert
    assert logged_func.__name__ == "func"
    assert logged_func.__doc__ == "None"

    expected = "UnitTest_test_LoggedFunction___call__ DEBUG:func(1)".split(" ")
    assert logger.handlers[0].stream.getvalue().split(" ")[:5] == expected

# Generated at 2022-06-14 04:58:07.139903
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("test_logger")
    logged_func = LoggedFunction(logger)

    def add(x=None, y=None):
        return x + y

    def concat(x=None, y=None):
        return f"{x}{y}"

    log_add = logged_func(add)
    log_add(10, 3)
    log_add(15, 6)
    log_add(x=10, y=3)
    log_add(x=15, y=6)
    log_add(15, y=6)
    log_add(y=6, x=15)

    log_concat = logged_func(concat)
    log_concat(["a", "b", "c"], ["x", "y", "z"])

# Generated at 2022-06-14 04:58:14.449573
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class FakeLogger:
        def debug(self, msg):
            print(msg)
    lf = LoggedFunction(FakeLogger())
    @lf
    def f1(a, b):
        print(f'f1({a}, {b}) was called.')
        return a + b
    f1(1, 2)
    f1('a', 'b')
    f1('a', 3)
    assert f1(1, 2) == 3

# Generated at 2022-06-14 04:58:23.365875
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import logging.handlers
    import sys

    # Create a logging stream handler
    handler = logging.StreamHandler(stream=sys.stdout)

    # Create a logging formatter
    formatter = logging.Formatter("%(asctime)s | [%(levelname)s] | %(message)s")

    # Add formatter to handler
    handler.setFormatter(formatter)

    # Create a logging logger
    logger = logging.getLogger("logged_function_unit_test")

    # Add handler to logger
    logger.addHandler(handler)

    # Set logger level to DEBUG
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def test_func(a, b, c):
        return a + b + c


# Generated at 2022-06-14 04:58:25.920973
# Unit test for function build_requests_session
def test_build_requests_session():
    s = build_requests_session()

    assert s is not None
    assert s.hooks is not None



# Generated at 2022-06-14 04:58:30.907639
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    func = LoggedFunction(logger=None)
    def decorated(arg1, arg2=11):
        pass

    result = func(decorated)
    assert type(result) == types.FunctionType
    assert hasattr(result, "__wrapped__")


# Generated at 2022-06-14 04:58:42.118290
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logger = logging.getLogger("log")
    test_data = [
        (lambda a: a + 1, [2], (), 3),
        (lambda a, b, c: a + b + c, [1, 2, 3], (), 6),
        (lambda a, b, c=1: a + b + c, [1, 2], {"c": 3}, 6),
        (lambda a, b, c=1, d=2: a + b + c + d, [1, 2], {"c": 3}, 8),
    ]

    for func, arg_list, kwargs_dict, expect in test_data:
        logging.basicConfig(level=logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)


# Generated at 2022-06-14 04:58:55.082729
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest.mock as mock

    logger = logging.getLogger('unittest')

    @LoggedFunction(logger)
    def add(x, y):
        return x + y

    # Call decorated method with positional arguments
    with mock.patch.object(logger, 'debug', wraps=logger.debug) as mock_debug:
        assert add(1, 2) == 3

    assert mock_debug.call_args_list == [
        mock.call('add(1, 2)'),
        mock.call('add() -> 3')
    ]

    # Call decorated method with keyword arguments
    with mock.patch.object(logger, 'debug', wraps=logger.debug) as mock_debug:
        assert add(x=1, y=2) == 3


# Generated at 2022-06-14 04:59:08.036472
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Given
    def add(x, y):
        return x + y

    class TestLogger():
        def debug(self, msg):
            print(msg)
    logger = TestLogger()

    # When
    logged_add = LoggedFunction(logger)(add)
    logged_add(1, 2)

    # Then
    pass

# Generated at 2022-06-14 04:59:15.678495
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import Logger
    from unittest import TestCase

    logger = Logger("test")
    logged_func = LoggedFunction(logger).__call__(test_function)

    @logged_func
    def test_function(a, b, c=3, d=4):
        return a + b + c + d

    # Call function with all arguments
    assert test_function(1, 2, 3, 4) == 10
    # Call function with all arguments but default values
    assert test_function(1, 2) == 10
    # Call function with some/no arguments
    assert test_function(1, 2, d=None) == 3



# Generated at 2022-06-14 04:59:26.687387
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from loguru import logger
    from io import StringIO
    
    def test_function(a, b):
        return f'a={a}, b={b}'
    
    class Capture:
        def __init__(self):
            self.content = StringIO()

    @LoggedFunction(logger)
    def function_1(a, b):
        return test_function(a, b)
    
    capture = Capture()
    with logger.catch(depth=1, action=capture):
        assert function_1('a', 1) == 'a=a, b=1'
    
    assert capture.content.getvalue() == """DEBUG: __main__: function_1('a', 1)
DEBUG: __main__: function_1 -> a=a, b=1
"""



# Generated at 2022-06-14 04:59:31.747147
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    Test __call__ method of LoggedFunction by calling this method.
    """
    from logging import getLogger, DEBUG
    from io import StringIO

    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    handler = logging.StreamHandler(StringIO())
    handler.setLevel(DEBUG)
    # add the handlers to the logger
    logger.addHandler(handler)

    def test_func(a, b, c=3):
        return a+b+c

    logged_test_func = LoggedFunction(logger)(test_func)

    assert logged_test_func(1, 2) == 6
    assert logged_test_func(1, 2, 3) == 6
    assert logged_test_func(1, 2, c=3) == 6

# Generated at 2022-06-14 04:59:43.560718
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import tempfile
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(tempfile.mktemp())
    logger.addHandler(handler)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(format)
    
    logged_function = LoggedFunction(logger)
    @logged_function
    def test(a, b):
        return a+b

    c = test(42, 50)
    handler.close()

# Generated at 2022-06-14 04:59:49.408977
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger(__name__)
    logged_func = LoggedFunction(logger)
    @logged_func
    def some_func(a, b, c=3, d='four'):
        return a * b * c * len(d)

    some_func(2, 4)
    some_func(1, 2, d=5)
    some_func(1, 2, 3)
    some_func(1, 2, 3, 5)


# Generated at 2022-06-14 04:59:58.911958
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("chunhui")
    logger.setLevel(10)

    @LoggedFunction(logger)
    def add_func(a, b):
        return a + b

    @LoggedFunction(logger)
    def div_func(a, b):
        return a / b

    # Test with default arguments
    try:
        add_func(2, 3)
        assert False
    except ZeroDivisionError:
        pass

    # Test with default and key-value arguments
    assert div_func(a=5, b=10) == 0.5

# Generated at 2022-06-14 05:00:08.425261
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO

    # Create logger which logs to buffer
    buffer = StringIO()
    logger = logging.getLogger()
    handler = logging.StreamHandler(buffer)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Create LoggedFunction decorator
    logged_function = LoggedFunction(logger)

    # Define test function
    @logged_function
    def test_function(a, b=2, c=None):
        return a + b + (c or 0)

    # Invoke test function
    test_function(1, b=3)
    test_function(1, c=3)
    test_function(1, b=3, c=4)

    # Check call arguments and return value

# Generated at 2022-06-14 05:00:18.029699
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.Logger("test_logger")
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logged_func = LoggedFunction(logger)
    def test_func(a, b, c=1, d=2):
        pass
    a = 1
    b = 2
    c = 3
    d = 4
    logged_func(test_func)(a, b, c=c, d=d)
    assert (
        logger.handlers[0].stream.getvalue()
        == f"test_func(1, 2, c={format_arg(c)}, d={format_arg(d)})\n"
    )


# Generated at 2022-06-14 05:00:26.424354
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("test")
    test_LoggedFunction___call__.logger = logger

    logging.basicConfig(level=logging.DEBUG)

    @LoggedFunction(logger)
    def foo(a, b, c=None):
        return a + b

    foo(1, 2)
    foo(3, 4, c=5)


if __name__ == "__main__":
    test_LoggedFunction___call__()

# Generated at 2022-06-14 05:00:49.237372
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("unittest_LoggedFunction___call__")
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger)
    def func_1(arg1, arg2, arg3=1):
        return arg1 + arg2 + arg3

    @LoggedFunction(logger)
    def func_2(*args):
        return args[0]

    # Test 1:
    func_1(2, 3)
    # Test 2:
    func_1(2, 3, 4)
    # Test 3:
    func_2(4, 5, 6)



# Generated at 2022-06-14 05:01:00.918483
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class TestClass(object):
        def simple_method(self, p1, p2):
            return p1, p2

        @LoggedFunction(logging.getLogger())
        def decorated_simple_method(self, p1, p2):
            return p1, p2

        def method_with_default_arg(self, p1, p2=2):
            return p1, p2

        @LoggedFunction(logging.getLogger())
        def decorated_method_with_default_arg(self, p1, p2=2):
            return p1, p2

        def method_with_positional_default_arg(self, p1, p2=2):
            return p1, p2


# Generated at 2022-06-14 05:01:07.620173
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    
    @LoggedFunction(logger)
    def testFunc(a, b, c=2, d=3):
        return (a + b) * c * d

    result = testFunc(1, 2, 4, 5)
    assert result == 120



# Generated at 2022-06-14 05:01:13.065368
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger()
    loggedf = LoggedFunction(logger)
    @loggedf
    def sum(a, b):
        return a+b
    sum(1, 2)
    logger.propagate = False
    sum(1, 2)
    assert True

# Generated at 2022-06-14 05:01:21.538422
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from io import StringIO
    from .context import set_stream_logger_handler, get_logger
    import logging
    import sys

    logger = get_logger(__name__)
    logger.setLevel(logging.DEBUG)
    with set_stream_logger_handler(logger, sys.stdout, logging.DEBUG) as handler:
        @LoggedFunction(logger)
        def test_func(param1, param2="param2", *, param3=3, param4=4):
            return 5

        test_func(1)
        assert handler.stream.getvalue().strip() == "test_logger.py:test_func(1, param2='param2', param3=3, param4=4)\ntest_logger.py:test_func -> 5"

        handler.stream.seek

# Generated at 2022-06-14 05:01:24.203518
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    pass



# Generated at 2022-06-14 05:01:34.718875
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    logger = logging.getLogger("logged function unittest")
    handler = logging.StreamHandler(io.StringIO())
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    def func(*args, **kwargs):
        return "ret value"

    logged_func = LoggedFunction(logger)(func)
    logged_func("str arg")
    logged_func(1, 2, 3)
    logged_func(d="d value", c="c value", a="a value")

    handler.close()
    assert (
        handler.stream.getvalue()
        == """func(str arg)
func(1, 2, 3)
func(d='d value', c='c value', a='a value')
func -> ret value
"""
    )

# Generated at 2022-06-14 05:01:47.030192
# Unit test for function build_requests_session
def test_build_requests_session():
    s = build_requests_session()
    assert isinstance(s, Session)
    adapter = s.adapters["http://"]
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries == Retry()

    s = build_requests_session(retry=False)
    assert isinstance(s, Session)
    assert "http://" not in s.adapters

    s = build_requests_session(retry=5)
    assert isinstance(s, Session)
    adapter = s.adapters["http://"]
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries == Retry(5)

    s = build_requests_session(retry=Retry(10))
    assert isinstance(s, Session)

# Generated at 2022-06-14 05:01:54.802720
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logged_function = LoggedFunction(logger)

    @logged_function
    def test1(a, b, c=1, d=2):
        return 1, b, c

    assert test1(1, 2, 3, 4) == (1, 2, 3)
    assert test1(1, 2) == (1, 2, 1)

    # test raise exception in called function

# Generated at 2022-06-14 05:02:06.991412
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    logger = Mock()
    func = Mock()
    decorated_func = LoggedFunction(logger)(func)
    decorated_func(1, 2, 3, name="value")
    logger.debug.assert_called_once_with("func(1, 2, 3, name='value')")
    func.assert_called_once_with(1, 2, 3, name="value")
    assert logger.debug.call_count == 2
    logger.debug.assert_any_call("func -> None")
    # Check one more time.
    logger.reset_mock()
    func.reset_mock()
    func.return_value = "This is return value."
    decorated_func(1, 2, 3, name="value")

# Generated at 2022-06-14 05:02:31.538451
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(True, False)
    assert session is not None
    assert session.mounts is None
    assert session.hooks is not None
    session = build_requests_session(False, False)
    assert session is not None
    assert session.mounts is None
    assert session.hooks is None
    session = build_requests_session(True, True)
    assert session is not None
    assert session.mounts is not None
    assert session.hooks is not None
    assert isinstance(session.mounts["http://"][0], HTTPAdapter)
    assert isinstance(session.mounts["https://"][0], HTTPAdapter)
    assert session.mounts["http://"][0].max_retries is not None
    assert session.mounts["https://"][0].max_

# Generated at 2022-06-14 05:02:41.431687
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class StringIO():
        def __init__(self):
            self.content = ""
        def flush(self):
            pass
        def write(self, text):
            self.content = text
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(StringIO())
    logger.addHandler(handler)
    lf = LoggedFunction(logger)
    @lf
    def test1(a, b):
        return a + b
    test1(1, 2)
    assert handler.stream.content == 'test1(1, 2) -> 3'
    del handler.stream.content
    @lf
    def test2(a, b):
        return a + b
    test2(1, 2)

# Generated at 2022-06-14 05:02:54.255737
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import patch
    from loguru import logger
    from .logger import create_logger

    create_logger(level="DEBUG")
    logger = logger

    # test function with 1 argument
    @LoggedFunction(logger)
    def test_function1(arg1):
        return 1

    with patch("logging.Logger.debug") as mocked_logger:
        result1 = test_function1(1)
        assert result1 == 1
        assert mocked_logger.call_args_list[0][0][0] == "test_function1(1)"
        assert mocked_logger.call_args_list[1][0][0] == "test_function1 -> 1"

    # test function with 1 argument and 1 kwarg

# Generated at 2022-06-14 05:03:03.765041
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    from unittest import TestCase
    from logging import DEBUG

    class TestLoggedFunction(TestCase):
        def test_logged_function(self):
            log_output = StringIO()
            logger = logging.getLogger("test_logger")
            logger.setLevel(DEBUG)
            logger.handlers = [logging.StreamHandler(log_output)]
            fn = LoggedFunction(logger)

            def test_function(a, b=1, *args, c, d):
                pass

            wrapped = fn(test_function)
            wrapped(1, 2, 3, c=4, d=5)

            expected = (
                    "test_function(1, 2, 3, c=4, d=5) -> None\n"
            )

# Generated at 2022-06-14 05:03:08.446702
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("LoggedFunctionTest")
    logged_func = LoggedFunction(logger)

    # Define a test function
    buffer = io.StringIO()
    @logged_func
    def func(foo, bar=False):
        print(foo, bar, file=buffer)
        return foo + bar

    # Call it
    func(False, True)
    assert buffer.getvalue() == "False True\n"



# Generated at 2022-06-14 05:03:18.390154
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    # Mock logger
    m_logger = logging.Logger(__name__)
    m_logger.debug = mock.MagicMock()

    def test_func(x, y=5):
        return x / y

    logging_func = LoggedFunction(m_logger)(test_func)
    result = logging_func(10)
    assert result == 2
    assert logging_func(20, 2) == 10

    # Check that the function name and arguments have been logged
    m_logger.debug.assert_any_call("test_func(10)")
    m_logger.debug.assert_any_call("test_func(20, 2)")

    # Check that the result has been logged
    m_logger.debug.assert_any_call("test_func -> 2")
    m_

# Generated at 2022-06-14 05:03:30.251873
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger()
    hdlr = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    @LoggedFunction(logger=logger)
    def func(a, b=2, *c, d, e=3, **f):
        pass

    class A:
        def __init__(self):
            self.x = 1

        def __repr__(self):
            return '"A"'

    a_obj = A()

# Generated at 2022-06-14 05:03:39.719536
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    class Mock:
        pass
    mock = Mock()
    mock.debug = logging.debug
    f = LoggedFunction(mock)
    
    # f is a function wrapper
    assert not hasattr(f, 'logger')
    def func(a, b, c=3):
        assert a==1
        assert b==2
        assert c==3
        return {'a': a, 'b': b}
    f2 = f(func)
    assert hasattr(f2, 'logger')
    
    result = f2(1, 2)
    assert result['a']==1
    assert result['b']==2


# Generated at 2022-06-14 05:03:45.216453
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MockLogger:
        def debug(self, message):
            print(message)

    logger = MockLogger()
    logged_function = LoggedFunction(logger=logger)

    @logged_function
    def test_function(x, y, z):
        return x + y + z

    test_function(1, 2, 3)
    test_function(1, y=2, z=3)



# Generated at 2022-06-14 05:03:57.440063
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    import io

    # Create logger
    logger = logging.getLogger("test_LoggedFunction")
    logger.setLevel(logging.DEBUG)

    log_stream = io.StringIO()
    handler = logging.StreamHandler(log_stream)
    logger.addHandler(handler)

    # Define logged function
    @LoggedFunction(logger)
    def myfunc(a, b, c=3, d=4):
        return a + b + c + d

    # Call logged function with parameters
    myfunc(1, 2)

    # Check log
    assert log_stream.getvalue() == "test_LoggedFunction DEBUG myfunc(1, 2, c=3, d=4)\n"
    log_stream.close()
    handler.close()
    del log_stream

# Generated at 2022-06-14 05:04:37.587348
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from numpy import array
    import logging
    from io import StringIO
    from vnpy.trader.constant import Interval
    from vnpy.trader.object import BarData
    stream = StringIO()
    handler = logging.StreamHandler(stream=stream)
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)


# Generated at 2022-06-14 05:04:46.801330
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    from unittest import mock
    from .logging import get_logger

    logger = mock.MagicMock(spec=get_logger("some_logger"))

    @LoggedFunction(logger)
    def mocked_function(name, age):
        pass

    mocked_function("jack", 20)
    logger.debug.assert_called_with("mocked_function('jack', 20)")

    mocked_function("jack", 20, gender="female")
    logger.debug.assert_called_with("mocked_function('jack', 20, gender='female')")

    mocked_function("jack", 20, gender="female", extra=["haha"])
    logger.debug.assert_called_with("mocked_function('jack', 20, gender='female', extra=['haha'])")

    #

# Generated at 2022-06-14 05:04:58.993397
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import tempfile
    import logging
    import os

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger("test_logger")
    logger.propagate = False

    # Create a temporary file
    f = tempfile.mktemp()

    # Create logged function
    logged_func = LoggedFunction(logger)

    # Define a function to test

# Generated at 2022-06-14 05:05:04.219719
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    
    @LoggedFunction(logger)
    def func(a, b, c=1, d=2):
        return (a, b, c, d)
    
    func(b=1, a=2)

# Generated at 2022-06-14 05:05:15.478395
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def f1(a, b=2, c=[3, 4]):
        return a+b+c[0]

    # test invoke f1
    lg=logging.getLogger(__name__)
    lg.setLevel(logging.DEBUG)
    f1_logged=LoggedFunction(lg)(f1)
    assert f1_logged(1) == 6
    assert f1_logged(1,3) == 7
    assert f1_logged(1,2,[5,6]) == 8
    assert f1_logged(1,2,c=[5,6]) == 8
    d={"b":20, "c":[50,60]}
    assert f1_logged(1,**d) == 51

# Generated at 2022-06-14 05:05:18.248972
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    unit test for method __call__ of class LoggedFunction
    :return:
    """



# Generated at 2022-06-14 05:05:24.187672
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(retry=False)
    assert session.auth == None
    assert session.headers == {}
    assert session.hooks == None
    assert session.params == {}
    assert session.proxies == {}
    assert session.verify == True
    assert session.cert == None
    assert session.max_redirects == 30


# Generated at 2022-06-14 05:05:33.824666
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
   class DummyLogger:
       def __init__(self, name):
           # saved for testing
           self.msg = ""

       def debug(self, msg):
           self.msg = msg

   logger = DummyLogger("")
   logged_func = LoggedFunction(logger)(test_func)

   logged_func(1)
   assert logger.msg == "test_func(1)"
   logger.msg = ""

   logged_func(1, 2, 3, d=4, e=5, f=6)
   assert logger.msg == "test_func(1, 2, 3, d=4, e=5, f=6)"
   logger.msg = ""


# Generated at 2022-06-14 05:05:39.758432
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    log = logging.getLogger("test_LoggedFunction___call__")
    log.setLevel("DEBUG")

    @LoggedFunction(log)
    def test_func(a, b, c=1, d=2, e=3):
        pass

    test_func("test 1", "test 2", d="test 4 - d")

# Generated at 2022-06-14 05:05:50.941765
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import unittest
    from unittest.mock import ANY, MagicMock

    class Test(unittest.TestCase):
        def test_1(self):
            logger = MagicMock(spec=logging)
            func = LoggedFunction(logger)
            real_func = MagicMock()
            func(real_func)()
            real_func.assert_called_once_with()
            logger.debug.assert_called_once_with(
                "%s()" % real_func.__name__
            )
            logger.reset_mock()
            real_func.reset_mock()
            real_func.return_value = "test1"
            func(real_func)()
            real_func.assert_called_once_with()
            logger.debug.assert_called_

# Generated at 2022-06-14 05:06:54.408212
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Creates a mock logger
    logger = mock.Mock()

    # Define the decorated function
    @LoggedFunction(logger)
    def f(a, b):
        pass

    f(1, 2)

    # Assert the mock logger has received the log message
    logger.debug.assert_called_once_with(
        "f('1', '2')"
    )

# Generated at 2022-06-14 05:07:06.584880
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    import logging

    class TestLoggedFunction(unittest.TestCase):
        def test__call__(self):
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            @LoggedFunction(logger)
            def test_function(a, b, c=None):
                return a ** b

            test_function(2, 3)
            test_function(2, 3, c=4)

    unittest.main()

# Generated at 2022-06-14 05:07:17.174282
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock, call
    logger = Mock()

    # Test function that takes no arguments
    @LoggedFunction(logger)
    def f():
        pass

    assert f.__name__ == "f"
    f()
    logger.debug.assert_called_once_with("f()")

    # Test function that takes an arguments with a value containing a single quote
    logger.reset_mock()
    @LoggedFunction(logger)
    def f(x):
        return x

    assert f.__name__ == "f"
    assert f("'Hello'") == "'Hello'"
    assert logger.debug.mock_calls == [
        call("f('Hello')"),
        call("f -> 'Hello'"),
    ]

    # Test function that takes arguments with a value that is neither

# Generated at 2022-06-14 05:07:27.040392
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import tempfile
    import os

    def test_func(*args, **kwargs):
        return "test_result"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Temp file
    stream = tempfile.NamedTemporaryFile(mode="w+")
    stream.seek(0)

    # Log handler
    handler = logging.StreamHandler(stream=stream)
    handler.setLevel(logging.DEBUG)

    # Add handlers
    logger.handlers = []
    logger.addHandler(handler)

    # Format of messages
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    #