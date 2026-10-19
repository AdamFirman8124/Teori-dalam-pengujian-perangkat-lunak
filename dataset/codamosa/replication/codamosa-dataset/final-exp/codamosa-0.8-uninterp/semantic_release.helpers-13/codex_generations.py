

# Generated at 2022-06-14 04:57:34.020929
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger=logging.getLogger()
    a = LoggedFunction(logger)
    f = a(test)
    f("hello","world",1,2,k=1,l="2")

# Generated at 2022-06-14 04:57:41.114328
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logs = []
    results = []

    class Test:
        def __init__(self, _logger):
            self.logger = _logger

        @LoggedFunction(logger=self.logger)
        def test_func(self, x, y, z=11):
            results.append([x, y, z])

    logger = mock.MagicMock()
    logger.debug = lambda arg: logs.append(arg)

    test = Test(logger)
    test.test_func(5, "hello")

    # TODO:
    #assert len(results) == 1
    #assert results == [5, "hello", 11]
    #assert len(logs) == 2
    #assert logs[0] == "test_func(5, 'hello', z=11)"
    #assert logs[1

# Generated at 2022-06-14 04:57:50.423009
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    @LoggedFunction(logger=None)
    def testMethod(arg1, arg2, kwarg1="value1", kwarg2="value2"):
        return "Hello world!"

    assert testMethod(1, "test", kwarg1="value1") == "Hello world!"
    assert testMethod(2, "test", kwarg2="value2") == "Hello world!"
    assert testMethod(3, "test", kwarg1="value1", kwarg2="value2") == "Hello world!"


# Generated at 2022-06-14 04:57:56.655862
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    from contextlib import redirect_stdout

    # Setup logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Setup output
    output = StringIO()
    handler = logging.StreamHandler(output)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def func(x, y, z=10):
        return x + y + z

    with redirect_stdout(output):
        assert func(10, 20) == 40
        assert func(10, 20, z=30) == 60


# Generated at 2022-06-14 04:58:07.495316
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(raise_for_status=True, retry=False)
    assert not session.mounts
    session = build_requests_session(raise_for_status=True, retry=True)
    assert session.mounts
    session = build_requests_session(raise_for_status=True, retry=1)
    assert session.mounts
    session = build_requests_session(raise_for_status=True, retry=Retry())
    assert session.mounts
    try:
        session = build_requests_session(raise_for_status=True, retry=None)
        assert False, "ValueError is expected to be raised"
    except ValueError:
        pass

# Generated at 2022-06-14 04:58:18.421153
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    # Capture output
    capture = io.StringIO()
    handler = logging.StreamHandler(capture)
    # Enable debug level logging
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logged_function = LoggedFunction(logger)

    # Call function
    def test_function(a, b=3, c=None):
        return a + b

    logged_function(test_function)(1, 2, 3)

    # Check output
    output = capture.getvalue()
    assert output == "test_function(1, 2, 3)\ntest_function -> 3\n"
    sys.stdout.write(output)
    sys.stdout

# Generated at 2022-06-14 04:58:29.618784
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import TestCase, main
    from unittest.mock import patch, MagicMock
    from datetime import datetime
    import pytz

    class LoggedFunctionTest(TestCase):
        def setUp(self):
            self.func_name = 'func_name'
            self.args = (1, 2)
            self.kwargs = {'k1': 3, 'k2': 4}
            self.result = 100
            
            patcher1 = patch('logging.Logger')
            self.addCleanup(patcher1.stop)
            self.mock_logger_class = patcher1.start()
            
            patcher2 = patch('functools.wraps')
            self.addCleanup(patcher2.stop)
            self.mock_wraps = patcher2

# Generated at 2022-06-14 04:58:34.860764
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("test")
    log = LoggedFunction(logger)

    @log
    def add_one(x):
        return x + 1

    add_one(5)
    add_one(10)
    add_one(15)



# Generated at 2022-06-14 04:58:43.235505
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class DummyLogger:
        def debug(self, msg):
            if not hasattr(self, "messages"):
                self.messages = []
            self.messages.append(msg)

    dummy_logger = DummyLogger()

    @LoggedFunction(dummy_logger)
    def test_function(i, j, k=2):
        return i + j + k

    test_function(1, 2, k=3)

    assert dummy_logger.messages[0] == "test_function(1, 2, k=3)"
    assert dummy_logger.messages[1] == "test_function -> 6"



# Generated at 2022-06-14 04:58:46.797582
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class DummyLogger:
        def debug(self, message):
            print(f"> {message}")

    func = lambda x: x**2
    logged_func = LoggedFunction(DummyLogger())(func)
    print(f"{func(3)}")
    print(f"{logged_func(3)}")

# test_LoggedFunction___call__()

# Generated at 2022-06-14 04:58:59.111778
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging


    log_stream = logging.StreamHandler()
    log_stream.setLevel(logging.DEBUG)
    log_stream.setFormatter(logging.Formatter("%(name)s: %(message)s"))

    logging.basicConfig(handlers=[log_stream])


    # test function with no argument and no return value
    @LoggedFunction(logging.getLogger("test case 1"))
    def f():
        print("in f")


    # test function with no argument and a return value
    @LoggedFunction(logging.getLogger("test case 2"))
    def g():
        print("in g")
        return 1
    
    
    # test function with argument and no return value

# Generated at 2022-06-14 04:59:09.650521
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    import unittest

    class TestCase(unittest.TestCase):
        def test_call(self):
            # Setup logger
            logger = logging.getLogger("test_LoggedFunction___call__.test_call")
            handler = logging.StreamHandler(sys.stdout)
            logger.addHandler(handler)

            @LoggedFunction(logger=logger)
            def test(a, b, c, d=7, e=9):
                return a * b + c * d * e

            test(1, 2, 3, 4, 5)
            self.assertEqual("test -> 94", logger.handlers[0].stream.getvalue().strip())

    unittest.main()

# Generated at 2022-06-14 04:59:18.075464
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Test function with none return value
    def test_func1(x, y=1):
        pass

    # Test function with return value
    def test_func2(x, y=1):
        return x

    # Mock the logger
    from unittest.mock import MagicMock

    logger = MagicMock()

    # Apply decorator
    logged_fun1 = LoggedFunction(logger)(test_func1)
    logged_fun2 = LoggedFunction(logger)(test_func2)

    # Call function
    args1 = (1, 2)
    kwargs1 = {"y": 3}
    logged_fun1(*args1, **kwargs1)
    args2 = (1, 2)
    kwargs2 = {"y": 3}
    logged_fun2(*args2, **kwargs2)

# Generated at 2022-06-14 04:59:28.412408
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class DummyLogger:
        def __init__(self):
            self.logged_lines = []

        def debug(self, msg):
            self.logged_lines.append(msg)

    def f1(x, y):
        return x * y

    def f2(x, y=None):
        return x * y

    def f3(x, *args, **kwargs):
        return x * functools.reduce(lambda x, y: x + y, args, 0)

    logger = DummyLogger()

    f1_wrapper = LoggedFunction(logger)(f1)
    assert f1_wrapper(3, 4) == 12
    assert f1_wrapper(3, y=4) == 12

# Generated at 2022-06-14 04:59:34.532576
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    f = LoggedFunction(logging.getLogger("test"))

    @f
    def g(a, b):
        return a + b

    assert g.__name__ == "g"
    assert g(1, 2) == 3
    g(1, 2)



# Generated at 2022-06-14 04:59:44.858753
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import StringIO

    class StringLogger:
        def __init__(self):
            self.log_capture = StringIO.StringIO()

        def debug(self, msg):
            self.log_capture.write(msg + "\n")

        def get_log(self):
            return self.log_capture.getvalue()

    @LoggedFunction(StringLogger())
    def add(x, y):
        return x + y

    add(1, 2)
    assert add.logger.get_log() == "add(1, 2)\nadd -> 3\n"

    @LoggedFunction(StringLogger())
    def gcd(x, y):
        return math.gcd(x, y)

    gcd(12, 18)
    assert gcd.logger.get

# Generated at 2022-06-14 04:59:58.040867
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import random
    import io

    random.seed(0)
    
    # LoggedFunction args
    logger = logging.getLogger(__name__)
    LF = LoggedFunction(logger)

    # Method args
    args = [random.randint(0, 100) for _ in range(3)]
    kwargs = {f"arg_{i}": random.random() for i in range(4)}

    stream = io.StringIO()
    logging.basicConfig(stream=stream, level=logging.DEBUG)

    assert LF.__call__(lambda a, b, c, d, e, f, g, h=1, i=2: a * b * c * d * e * f * g * h * i)(
        *args, **kwargs
    ) == 0
    
    # compare recorded

# Generated at 2022-06-14 05:00:07.157851
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger("test")
    counter = 0
    def function_to_count():
        nonlocal counter
        counter += 1
        return counter
    logged_function_to_count = LoggedFunction(logger)(function_to_count)
    assert logged_function_to_count() == 1
    assert logged_function_to_count() == 2
    assert logged_function_to_count("1", "2", "3") == 3
    assert logged_function_to_count("1", "2", "3") == 4
    assert logged_function_to_count(a=1, b=2) == 5
    assert logged_function_to_count(a=1, b=2) == 6

# Generated at 2022-06-14 05:00:17.212935
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging


    class Logger:
        def __init__(self):
            self.logger = logging.getLogger(__name__)


    logger = Logger()
    LoggedFunction.logger = Logger()

    @LoggedFunction(logger)
    def MyFunction(a, b, c=None, d=None):
        data = {"a": a, "b": b, "c": c, "d": d}
        return data


    MyFunction(1, 2, 3, 4)
    MyFunction(1, 2, 4)
    MyFunction(1, 2)
    MyFunction(1, 2, d=4)
    MyFunction(1, 2, c=3)


# Generated at 2022-06-14 05:00:30.218818
# Unit test for function build_requests_session
def test_build_requests_session():
    assert(build_requests_session() == Session())
    assert(build_requests_session(True) == Session())
    assert(build_requests_session(False) == Session())
    assert(build_requests_session(False, True) == Session())
    assert(build_requests_session(True, True) == Session())
    assert(build_requests_session(False, False) == Session())
    assert(build_requests_session(True, Retry(total=1)) == Session())
    assert(build_requests_session(False, Retry(total=1)) == Session())
    assert(build_requests_session(False, 1) == Session())
    assert(build_requests_session(True, 1) == Session())
    assert(build_requests_session(False, 0) == Session())

# Generated at 2022-06-14 05:00:41.351370
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class MockLogger:
        def debug(self, msg):
            pass

    mockLogger = MockLogger()
    loggedFunction = LoggedFunction(mockLogger)
    decoratedFunc = loggedFunction(lambda x : [i+1 for i in x])
    assert decoratedFunc([1,2,3]) == [2,3,4]


# Generated at 2022-06-14 05:00:48.786917
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from io import StringIO
    from contextlib import redirect_stdout

    class FakeLogger:
        def __init__(self):
            self.output = StringIO()

        def debug(self, msg):
            print(msg, file=self.output)

    logger = FakeLogger()
    dec = LoggedFunction(logger=logger)

    def func_with_args_and_kwargs(pos, kw="world"):
        return pos + kw

    dec_func = dec(func_with_args_and_kwargs)
    with redirect_stdout(StringIO()):
        dec_func("hello", "world")

    output = logger.output.getvalue()

# Generated at 2022-06-14 05:01:00.819160
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import io
    import logging
    import unittest

    class MyTestResult(unittest.TestResult):
        def __init__(self):
            super().__init__()
            self.__failed = False
            self.__errors = []

        @property
        def failed(self):
            return self.__failed

        @property
        def errors(self):
            return self.__errors

        def addError(self, test, err):
            self.__failed = True
            self.__errors.append(err)

    class TestLoggedFunction(unittest.TestCase):
        def test(self):
            temp = io.StringIO()
            logger = logging.getLogger()
            logger.addHandler(logging.StreamHandler(temp))
            # logger.setLevel(logging.DEBUG)
            #

# Generated at 2022-06-14 05:01:09.311354
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class FakeLogger:
        def __init__(self):
            self.logs = []

        def debug(self, msg):
            self.logs.append(msg)

    # Test for function with no paramater
    logger = FakeLogger()
    func_name = "dummy_function"

    @LoggedFunction(logger)
    def dummy_function():
        pass

    getattr(LoggedFunction(logger), func_name)()
    assert len(logger.logs) == 2
    assert logger.logs[0] == f"{func_name}()"
    assert logger.logs[1] == f"{func_name} -> None"

    # Test for function with zero paramater
    logger = FakeLogger()

# Generated at 2022-06-14 05:01:19.894704
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    from unittest import TestCase

    class TestCase(TestCase):
        def test_call(self):
            logger = mock.Mock()
            logging_decorator = LoggedFunction(logger)

            @logging_decorator
            def test_func():
                return True

            test_func()
            logger.debug.assert_called_once()
            logger.reset_mock()

            test_func(1, 2, 3)
            logger.debug.assert_called_once()
            logger.reset_mock()
            # __call__(self, func)

    # unit_test(logging_decorator, logger)
    test_case = TestCase()
    test_case.test_call()

# Generated at 2022-06-14 05:01:24.867315
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)
    @LoggedFunction(log)
    def f(arg1, arg2="test"):
        return arg2

    f(arg1=1)
    f(1, arg2="test2")
    f(3, "test3")
    f(4, arg2="test4")
    assert True

# Generated at 2022-06-14 05:01:34.985105
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import StringIO

    class TestLogger(logging.Logger):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.out = StringIO.StringIO()
            self.addHandler(logging.StreamHandler(self.out))

        def get_output(self):
            output = self.out.getvalue()
            self.out.truncate(0)
            self.out.seek(0)
            return output


    @LoggedFunction(logger=TestLogger(name="test_logger"))
    def test_func(a, b, *vargs, **kwargs):
        pass

    test_func(1, 2, 3, 4, a=3, b=4)
    output = test_func

# Generated at 2022-06-14 05:01:46.060705
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging

    logger = logging.getLogger("test_LoggedFunction___call__")

    class DummyObject:
        @LoggedFunction(logger)
        def do_something(self, a, b):
            return (a, b)

        @LoggedFunction(logger)
        def do_something_with_kwargs(self, a, b, c=None):
            return (a, b, c)

    obj = DummyObject()
    obj.do_something("a", "b")
    obj.do_something_with_kwargs("a", "b", c="c")
    obj.do_something_with_kwargs("a", "b")


# Generated at 2022-06-14 05:01:57.562054
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import unittest
    from unittest.mock import MagicMock
    import logging

    class TestLoggedFunction(unittest.TestCase):
        def setUp(self):
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            self.logname = "unittest_LoggedFunction___call__"
            self.handler = logging.FileHandler(self.logname, "w")
            self.handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
            )
            self.handler.setFormatter(formatter)

# Generated at 2022-06-14 05:02:07.686062
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest import mock
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    from requests.utils import default_headers
    from pprint import pprint
    import copy

    # logger = mock.MagicMock()
    logger = mock.Mock()
    logger.info = mock.Mock()
    logger.debug = mock.Mock()
    # logger = mock.Mock()
    # logger = mock.MagicMock()
    lg_f = LoggedFunction(logger)
    # lg_f = LoggedFunction(logger=logger)
    # lg_f = LoggedFunction(logger=mock.Mock())
    # lg_f = LoggedFunction(logger=mock.MagicMock())
    # lg_f

# Generated at 2022-06-14 05:02:24.809078
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """
    unit test for __call__ method in LoggedFunction.

    """
    import unittest
    import os
    from loguru import logger
    test_dir_path = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(test_dir_path, "test_logged_function_log.txt")
    logger.add(log_file_path, rotation='10 MB')

    def test_func(a, b, *arg):
        return a + b

    test_logged_function = LoggedFunction(logger)
    test_logged_func = test_logged_function(test_func)
    test_logged_func(1, 2, 3)
    with open(log_file_path) as f:
        assert test

# Generated at 2022-06-14 05:02:38.311596
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Set the test logger
    logger = logging.getLogger("LoggedFunction") 
    logger.disabled = False
    logger.setLevel(logging.DEBUG)
    logger.handlers = []

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set the test target
    @LoggedFunction(logger)
    def test_target(arg1, arg2):
        print(f"arg1 = {arg1}, arg2 = {arg2}")
        return True


# Generated at 2022-06-14 05:02:51.476604
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # create mock logger
    class MockLogger:
        def debug(self, msg):
            self.msg = msg

    logger = MockLogger()
    # create mock function
    def mock_func(a, b=2):
        pass
    
    # test function
    wrapped_func = LoggedFunction(logger)(mock_func)

    # test 1
    wrapped_func(1)
    assert logger.msg == "mock_func(1)"

    # test 2
    wrapped_func(1, b=2)
    assert logger.msg == "mock_func(1, b=2)"

    # test 3
    wrapped_func(1, "a")
    assert logger.msg == "mock_func(1, 'a')"


if __name__ == "__main__":
    test_Logged

# Generated at 2022-06-14 05:03:01.773201
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    logger = logging.getLogger()
    Logger_Debug = logger.debug
    logger.debug = lambda x: print(x)
    logged_func = LoggedFunction(logger)
    func = lambda x,y,z=1,a=2:"".join([str(x),str(y),str(z),str(a)])
    assert logged_func(func)(1.0,2.0) == "1212"
    assert logged_func(func)(1,2) == "1212"
    assert logged_func(func)(1,2,z=3) == "1213"
    assert logged_func(func)(1,y=2) == "1212"
    assert logged_func(func)(x=1, y=2, z=3) == "1213"
    logger.debug = Logger_Debug

# Generated at 2022-06-14 05:03:13.626708
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class FakeLogger:
        def __init__(self):
            self.log = []

        def debug(self, s):
            self.log.append(s)

        def clear(self):
            self.log.clear()

    def f1(a, b, c=1, d="d"):
        return a + b + c

    fake_logger = FakeLogger()
    lf = LoggedFunction(fake_logger)

    @lf
    def f2(a, b, c=1, d="d"):
        return a + b + c

    @lf
    def f3():
        return "nothing"

    for f, name in zip([f1, f2, f3], ["f1", "f2", "f3"]):
        fake_logger.clear()

# Generated at 2022-06-14 05:03:19.676756
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    class MockLogger:
        def __init__(self):
            self.logs = []

        def debug(self,s):
            self.logs.append(s)

    @LoggedFunction(MockLogger())
    def add(x,y):
        return x + y

    add(2,3)

    assert ["add(2, 3)", "add -> 5"] == MockLogger.logs

# Generated at 2022-06-14 05:03:29.907802
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io

    # Prepare logger
    logger = logging.getLogger("LoggedFunction")
    logger.setLevel(logging.DEBUG)

    # Prepare stream
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Log function
    @LoggedFunction(logger)
    def echo(text):
        return text

    # Run test
    echo("Hello, world!")

    # Clean up logger
    logger.removeHandler(handler)

    # Check result
    assert stream.getvalue().strip() == "echo('Hello, world!')\necho -> Hello, world!"

# Generated at 2022-06-14 05:03:40.924772
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import Mock

    mock_logger = Mock()
    logger = LoggedFunction(mock_logger)

    def func(a, b, c):
        return a + b + c


# Generated at 2022-06-14 05:03:48.768004
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO

    # LOG OUTPUT
    # TODO: configure for logger for test only
    log_output = StringIO()
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler(log_output)
    stream_handler.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG, stream=log_output)
    logger.addHandler(stream_handler)

    @LoggedFunction(logger)
    def test_func(a, b, c=3, d=4, e="test"):
        return (a, b, c, d, e)

    test_func(1, 2, c=5, e=6)

    log_output.seek(0)
    log_

# Generated at 2022-06-14 05:03:59.706762
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():

    # Setup
    from io import StringIO
    from logging import Logger, DEBUG
    from logging import StreamHandler
    from pprint import pprint

    # Exercise
    output = StringIO()
    logger = Logger("logger")
    logger.setLevel(DEBUG)
    logger.addHandler(StreamHandler(output))

    log_func = LoggedFunction(logger)
    def my_func(x, y, z=5, *args,  **kwargs):
        return (x, y, z)

    my_log_func = log_func(my_func)

    # Verify
    my_log_func(1, 2, 3, 4, a=5, b=6)

# Generated at 2022-06-14 05:04:26.383879
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def lf(a,b):
        pass
    
    new_logger = LoggedFunction(lf)
    assert new_logger.__call__(lf)(1,2) == None
    assert ("lf(1,2)" in new_logger.logger.__repr__()) == True
    assert new_logger.logger.__repr__().split()[0] == 'DEBUG'
    assert ("lf -> None" in new_logger.logger.__repr__()) == True



# Generated at 2022-06-14 05:04:33.892533
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from io import StringIO
    import sys

    out = StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers = []
    logger.addHandler(logging.StreamHandler(out))

    logged_func = LoggedFunction(logger)(lambda x, y: x + y)
    assert logged_func(1, 2) == 3
    assert out.getvalue() == "logged_func(1, 2) -> 3\n"



# Generated at 2022-06-14 05:04:44.606837
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from logging.config import dictConfig
    from io import StringIO

    # Create logger
    log_stream = StringIO()
    dictConfig(
        {
            "version": 1,
            "handlers": {
                "default": {"class": "logging.StreamHandler", "stream": log_stream}
            },
            "root": {"handlers": ["default"], "level": "DEBUG"},
        }
    )
    log = logging.getLogger()

    # Create LoggedFunction decorator
    logged_function = LoggedFunction(log)

    # Decorate function
    @logged_function
    def func(a, b, c="test", d=None):
        return a + b + len(c)

    # Call the decorated function
    result = func(1, 2, 3, d=4)

   

# Generated at 2022-06-14 05:04:57.711423
# Unit test for function build_requests_session
def test_build_requests_session():
    expected_raise_for_status = True
    session = build_requests_session(raise_for_status=expected_raise_for_status)
    assert session.hooks["response"][0].__name__ == "lambda"
    assert session.hooks["response"][0].__closure__[0].cell_contents == expected_raise_for_status
    assert session.adapters["http://"].max_retries.total == Retry().total
    assert session.adapters["https://"].max_retries.total == Retry().total

    expected_raise_for_status = False
    expected_retry_total = -1
    session = build_requests_session(
        raise_for_status=expected_raise_for_status, retry=expected_retry_total
    )

# Generated at 2022-06-14 05:05:03.653650
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    print("LoggedFunction.__call__()")
    import logging
    import unittest

    from io import StringIO

    from helpers import LoggedFunction


    class LoggedFunctionTest(unittest.TestCase):
        def setUp(self):
            self.log_handler = StringIO()
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            self.log_handler = logging.StreamHandler(self.log_handler)
            self.log_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.log_handler)

            self.func = lambda x, y: x * y
            self.log_func = LoggedFunction(self.logger)(self.func)


# Generated at 2022-06-14 05:05:09.536691
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys

    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logger = logging.getLogger("LoggedFunction test_LoggedFunction___call__")

    @LoggedFunction(logger)
    def test_function(x):
        return x

    test_function("a")



# Generated at 2022-06-14 05:05:17.239328
# Unit test for function build_requests_session
def test_build_requests_session():
    # raise for status
    session = build_requests_session(True)
    with pytest.raises(requests.exceptions.HTTPError):
        resp = session.get("https://httpbin.org/status/404")
    assert resp.status_code == 404
    session = build_requests_session(False)
    resp = session.get("https://httpbin.org/status/404")
    assert resp.status_code == 404
    # retry
    session = build_requests_session(True)
    with pytest.raises(requests.exceptions.RetryError):
        resp = session.get("https://httpbin.org/status/500")
    assert resp.status_code == 500
    session = build_requests_session(True, False)

# Generated at 2022-06-14 05:05:29.447534
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import io
    import sys

    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    def my_function(first_arg, second_arg='my default val'):
        return 42

    my_logged_function = LoggedFunction(logger)(my_function)
    result = my_logged_function(1, second_arg='bla')

    assert result == 42
    assert stream.getvalue() == 'my_function(1, second_arg=\'bla\')\nmy_function -> 42\n'

# Generated at 2022-06-14 05:05:40.974434
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from logging import Logger
    from unittest import mock

    def func(num1, num2):
        return num1+num2

    logger = mock.Mock(spec=Logger)
    logged_func = LoggedFunction(logger)(func)

    logged_func(1,2)
    log_msg1 = "func(1, 2)"
    logger.debug.assert_called_once_with(log_msg1)

    logged_func(num1=1, num2=2)
    log_msg2 = "func(num1=1, num2=2)"
    logger.debug.assert_any_call(log_msg2)

    assert 2 == logged_func(1, 2)

# Generated at 2022-06-14 05:05:51.600809
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def foo(x, y=1):
        return x * y

    logger = unittest.mock.Mock()
    logged_func = LoggedFunction(logger)(foo)
    assert logged_func(2) == 2
    logger.debug.assert_called_with("foo(2, y=1)")
    logger.debug.reset_mock()

    assert logged_func(2, y=3) == 6
    logger.debug.assert_called_with("foo(2, y=3)")
    logger.debug.reset_mock()

    assert logged_func(2, 3) == 6
    logger.debug.assert_called_with("foo(2, 3)")
    logger.debug.reset_mock()


if __name__ == "__main__":
    unittest.main()

# Generated at 2022-06-14 05:06:27.628456
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    import sys
    from io import StringIO

    # Capture stdout
    captured_stdout = StringIO()
    stdout = sys.stdout
    sys.stdout = captured_stdout

    # Configure logging and create logger
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logger = logging.getLogger()

    # Add print() method to logger (to allow us to verify its output)
    logger.print = lambda: captured_stdout.getvalue()

    # Create LoggedFunction decorator and use it to decorate function
    logged_function = LoggedFunction(logger)

    @logged_function
    def f(a, b, c="c"):
        return a + b + c

    # Call decorated function and check output

# Generated at 2022-06-14 05:06:38.110888
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # test logged_func
    @LoggedFunction(logging.getLogger())
    def sum(a, b):
        return a + b
    sum(1, 2)

    # test logged_func with kwargs
    @LoggedFunction(logging.getLogger())
    def sum_kwargs(a, b = 3):
        return a + b
    sum_kwargs(1, b = 2)

    # test logged_func with no output
    @LoggedFunction(logging.getLogger())
    def sum_no_output(a, b = 3):
        return
    sum_no_output(1, b = 2)

# Generated at 2022-06-14 05:06:49.889895
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    import logging
    from logging import StreamHandler, DEBUG

    handler = StreamHandler()
    handler.setLevel(DEBUG)
    handler.setFormatter(logging.Formatter("%(message)s"))

    logger = logging.getLogger("test")
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    @LoggedFunction(logger)
    def test_function(a, b, c=None):
        return f"{a} {b} {c}"

    test_function("a", "b", "c")
    test_function("a", "b", c="c")
    test_function("a", b="b", c="c")
    test_function(1, 2, c=3)

# Generated at 2022-06-14 05:06:56.302012
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    from unittest.mock import patch

    debug = patch("logging.Logger.debug").start()

    @LoggedFunction(logger="TEST")
    def func1(a, b, c="foo"):
        pass

    func1(1, 2)
    func1(1, 2, c=3)
    debug.assert_any_call("func1(1, 2)")
    debug.assert_any_call("func1(1, 2, c=3)")
    patch.stopall()

# Generated at 2022-06-14 05:07:05.292622
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class DummyLogger:
        def debug(self, *args):
            self.args = args

    logger = DummyLogger()
    logged_func = LoggedFunction(logger)(
        lambda a, b, c, d=None, e="helloworld", f=0.00305, g=1: (a, b, c, d, e, f, g)
    )
    logged_func(1, 2, 3, d=None, e="helloworld", f=0.00305, g=1)
    print(logger.args)

# Generated at 2022-06-14 05:07:10.659784
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    class logger:
        def debug(self, string):
            print(string)

    my_logging_function = LoggedFunction(logger())
    @my_logging_function
    def f(a, b, c):
        return a*b + c
    r = f(1, 2, 3)
    print(r)

# Generated at 2022-06-14 05:07:22.552035
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    # Get a logger
    logger = logging.getLogger("test_LoggedFunction___call__")
    # Add some handlers to log everything to the console
    logger.addHandler(logging.StreamHandler())
    # Log all messages
    logger.setLevel(logging.DEBUG)
    # Wrap a function and return the wrapper
    @LoggedFunction(logger)
    def foooo(arg1, arg2=True):
        print("This function is called")
        return arg1, arg2
    print("Before the function is called")
    result = foooo("this is a test", False)
    print("After the function is called")
    # Assert that the result is what we expect
    assert result == ("this is a test", False)


# Generated at 2022-06-14 05:07:25.779116
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    def f(a, b, c, d=3, e=5):
        return a + b + c + d + e

    logged_f = LoggedFunction()(f)
    logged_f(1, 2, 3, 4)

# Generated at 2022-06-14 05:07:33.659285
# Unit test for method __call__ of class LoggedFunction
def test_LoggedFunction___call__():
    """Test method __call__ of class LoggedFunction"""
    import logging
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    logged = LoggedFunction(logger)

    @logged
    def add_nums(x: int, y: int) -> int:
        return x + y

    assert add_nums(2, 3) == 5