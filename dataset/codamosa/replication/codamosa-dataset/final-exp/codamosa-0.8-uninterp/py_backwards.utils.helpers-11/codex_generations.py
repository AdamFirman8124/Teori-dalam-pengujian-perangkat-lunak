

# Generated at 2022-06-22 12:38:28.066018
# Unit test for function eager
def test_eager():

    def trivial_generator():
        for i in range(4):
            yield i

    generator_iter = trivial_generator()
    assert list(generator_iter) == [0, 1, 2, 3]

    generator_eager = eager(trivial_generator)
    assert generator_eager() == [0, 1, 2, 3]
    assert isinstance(generator_eager(), list)


# Generated at 2022-06-22 12:38:30.650479
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass'


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:38:34.472055
# Unit test for function get_source
def test_get_source():
    def dummy():
        pass

    assert get_source(dummy) == 'def dummy():\n    pass'

    def dummy_multiline():
        some_var = 1
        some_var = 2
        some_var = 3

    assert get_source(dummy_multiline) == '    some_var = 1\n    some_var = 2\n    some_var = 3'

# Generated at 2022-06-22 12:38:39.204328
# Unit test for function eager
def test_eager():
    # pylint: disable=unused-variable
    def generator() -> Iterable[int]:
        yield 1
        yield 2

    @eager
    def eager_generator() -> Iterable[int]:
        yield 1
        yield 2

    assert list(generator()) == [1, 2]

    assert eager_generator() == [1, 2]

# Generated at 2022-06-22 12:38:41.151196
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'pass'



# Generated at 2022-06-22 12:38:46.707327
# Unit test for function get_source
def test_get_source():
    def function():
        """Function source"""
        width = 40
        print('*'*width)
        # Out
    source = get_source(function)
    assert source == """width = 40
print('*'*width)
# Out""", source

if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:38:49.980107
# Unit test for function debug
def test_debug():
    from .. import settings
    settings.debug = True

    try:
        debug(lambda: 'foo')
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:38:51.630910
# Unit test for function eager
def test_eager():
    @eager
    def foo(x: int) -> Iterable[int]:
        yield x

    assert foo(6) == [6]

# Generated at 2022-06-22 12:38:53.031951
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:38:58.237132
# Unit test for function eager
def test_eager():
    @eager
    def foo(n: int) -> Iterable[int]:
        for i in range(n):
            yield i

    # Check if lazy
    assert foo(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Generated at 2022-06-22 12:39:01.987289
# Unit test for function get_source
def test_get_source():
    def f():
        return 5

    assert get_source(f) == 'return 5'

# Generated at 2022-06-22 12:39:02.864099
# Unit test for function get_source

# Generated at 2022-06-22 12:39:05.432222
# Unit test for function get_source
def test_get_source():
    def f():
        def g():
            pass
        return g()


# Generated at 2022-06-22 12:39:07.066068
# Unit test for function get_source
def test_get_source():
    def test_function():
        return 1

    assert get_source(test_function) == 'return 1'

# Generated at 2022-06-22 12:39:16.908339
# Unit test for function debug
def test_debug():
    """
    >>> from importlib import reload
    >>> from ..conf import settings
    >>> settings.debug = False
    >>> class MockStdErr:
    ...     messages = []
    ...     def write(self, msg):
    ...         self.messages.append(msg)
    ...         return len(msg)
    ...     def flush(self):
    ...         pass
    >>> mock_sys = reload(sys)
    >>> mock_sys.stderr = MockStdErr()
    >>> debug(lambda: 'test_message')
    >>> mock_sys.stderr.messages
    []
    >>> settings.debug = True
    >>> debug(lambda: 'test_message_2')
    >>> mock_sys.stderr.messages
    ['test_message_2']
    """
    ...



# Generated at 2022-06-22 12:39:19.111230
# Unit test for function get_source
def test_get_source():
    def f():
        def g():
            pass
        pass

    assert get_source(f) == 'def g():\n    pass\npass'

# Generated at 2022-06-22 12:39:23.967178
# Unit test for function get_source
def test_get_source():
    @experimental 
    def test_function(x: int) -> bool:
        """Test function."""
        return x != 0

    source_code = \
        """if x != 0:
            raise ValueError('x should be equal to 0')
        """

    assert get_source(test_function)  == source_code

# Generated at 2022-06-22 12:39:31.213973
# Unit test for function debug
def test_debug():
    from . import settings

    try:
        import StringIO
        from contextlib import redirect_stderr
    except ImportError:
        from io import StringIO
        from contextlib import redirect_stderr

    settings.debug = True
    sio = StringIO()
    with redirect_stderr(sio):
        debug(lambda: 'test')
    assert 'test' in sio.getvalue()



# Generated at 2022-06-22 12:39:33.612486
# Unit test for function get_source
def test_get_source():
    def example():
        a = 1
        b = 2

    assert get_source(example).strip() == 'a = 1\nb = 2'.strip()

# Generated at 2022-06-22 12:39:35.823699
# Unit test for function get_source
def test_get_source():
    def foo():
        "docstring"
        x = 1
        print(x)

# Generated at 2022-06-22 12:39:39.531634
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'pass'

# Generated at 2022-06-22 12:39:41.675945
# Unit test for function get_source
def test_get_source():
    def func():
        """Docstring"""
        return 5

    assert get_source(func) == 'return 5'

# Generated at 2022-06-22 12:39:43.632520
# Unit test for function get_source
def test_get_source():
    def fn():
        a = 5

    assert get_source(fn) == 'a = 5'

# Generated at 2022-06-22 12:39:48.267366
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            return 3
        return bar()
    source = get_source(foo)
    assert (source ==
            "def bar():\n"
            "    return 3\n"
            "return bar()")


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:39:53.768534
# Unit test for function debug
def test_debug():
    cnt = [0]

    def get_message():
        cnt[0] += 1
        return 'foo'

    debug(get_message)
    assert cnt[0] == 0

    settings.debug = True
    debug(get_message)
    assert cnt[0] == 1

    settings.debug = Fals

# Generated at 2022-06-22 12:40:01.711075
# Unit test for function debug
def test_debug():
    import logging
    import sys

    # Patch logging.StreamHandler to get stderr
    # https://stackoverflow.com/a/27985900
    log_handler = logging.StreamHandler(sys.stderr)
    logger = logging.getLogger('py_backwards')
    logger.disabled = True
    old, logger.handlers[:] = logger.handlers, [log_handler]

    # Patch settings for debug
    old_debug = settings.debug
    settings.debug = True

    # Test
    logger.info('something')
    out, err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = StringIO(), StringIO()
    def fn():
        logger.info('Number {}'.format(2))
    debug(fn)
    assert sys.stderr

# Generated at 2022-06-22 12:40:08.045684
# Unit test for function debug
def test_debug():

    class Example:

        def __init__(self, msg: str, expected: str) -> None:
            self.msg = msg
            self.expected = expected

    class Log:
        def __init__(self) -> None:
            self.logged = []  # type: List[str]

        def __call__(self, msg: str) -> None:
            self.logged.append(msg)

        def __iter__(self) -> Iterable[str]:
            return iter(self.logged)

    @eager
    def test(msg: str, expected: str, debug_off: bool) -> Any:
        log = Log()
        old_debug = settings.debug

# Generated at 2022-06-22 12:40:12.988799
# Unit test for function debug
def test_debug():
    from unittest.mock import Mock
    settings.debug = True
    mock_stderr = Mock()
    with patch('sys.stderr', mock_stderr):
        debug(lambda: 'test')
    mock_stderr.write.assert_called_once()
    settings.debug = False



# Generated at 2022-06-22 12:40:15.384233
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'message')
    settings.debug = False



# Generated at 2022-06-22 12:40:18.138422
# Unit test for function get_source
def test_get_source():
    def _fn(a: str, b: str) -> int:
        print(a, b, sep='')
        return 42


# Generated at 2022-06-22 12:40:24.864786
# Unit test for function eager
def test_eager():
    def test_function(x: int) -> Iterable[int]:
        for i in range(x):
            yield i
    assert eager(test_function)(3) == [0, 1, 2]


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-22 12:40:28.051446
# Unit test for function eager
def test_eager():
    @eager
    def add(a, b):
        yield a + b
    assert add(1, 2) == [3]

# Generated at 2022-06-22 12:40:33.386665
# Unit test for function debug
def test_debug():
    class TestClass:
        @staticmethod
        def func():
            pass

    # Test debug.py:settings.debug == False
    settings.debug = False
    debug(lambda: "debug message")
    assert settings.debug == False

    # Test debug.py:settings.debug == True
    settings.debug = True
    debug(lambda: "debug message")
    assert settings.debug == True

# Generated at 2022-06-22 12:40:37.407423
# Unit test for function get_source
def test_get_source():

    def sample_function():
        print(2 + 3)
        print(4 + 5)

    assert get_source(sample_function) == dedent(
        '''
        print(2 + 3)
        print(4 + 5)
        '''
    )

# Generated at 2022-06-22 12:40:39.691032
# Unit test for function get_source
def test_get_source():
    def get_source_test():
        return 'foo'

    assert get_source(get_source_test) == 'return \'foo\''

# Generated at 2022-06-22 12:40:43.297082
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    def foo2():

        def _():
            pass
    assert get_source(foo).strip() == 'def foo():'
    assert get_source(foo2).strip() == 'def foo2():'

# Generated at 2022-06-22 12:40:50.141238
# Unit test for function get_source
def test_get_source():
    def source_generator(x):
        def f(y):
            print(y)
        return f

    def f(a):
        def g(b):
            print('g')

        print('f')

    assert get_source(source_generator(2)(2)) == "def f(y):\n    print(y)"
    assert get_source(f) == "def g(b):\n    print('g')\n\nprint('f')"

# Generated at 2022-06-22 12:40:54.180648
# Unit test for function debug
def test_debug():
    assert settings.debug == False
    debug(lambda: 'message') == None
    settings.debug = True
    assert debug(lambda: 'message') == None
    settings.debug = False
    assert debug(lambda: 'message') == None



# Generated at 2022-06-22 12:40:57.654279
# Unit test for function debug
def test_debug():
    settings.debug = True
    message = 'Message'
    try:
        debug(lambda: message)
    finally:
        settings.debug = False



# Generated at 2022-06-22 12:41:06.934111
# Unit test for function debug
def test_debug():
    import unittest
    import sys
    import io

    def test_func(a: int, b: int) -> int:
        return a + b

    class DebugTestCase(unittest.TestCase):
        def setUp(self) -> None:
            self.temp_stdout = sys.stdout
            sys.stdout = io.StringIO()

        def tearDown(self) -> None:
            sys.stdout = self.temp_stdout

        def test_debugging(self) -> None:
            def get_message() -> str:
                return "hello"

            debug(get_message)
            result = sys.stdout.getvalue()
            self.assertEqual(result, "PyBackwards debug: hello\n")

    unittest.main()

# Generated at 2022-06-22 12:41:14.443871
# Unit test for function get_source
def test_get_source():
    def some_func():
        '''
        Some function
        '''
        x = 1

    if get_source(some_func) != '        x = 1':
        print('Error!')


# Generated at 2022-06-22 12:41:20.055019
# Unit test for function debug
def test_debug():
    with patch('sys.stderr', new_callable=io.StringIO) as out:
        settings.debug = True
        debug(lambda: 'test_message')
        assert out.getvalue() == messages.debug('test_message') + '\n'
        out.truncate(0)
        settings.debug = False
        debug(lambda: 'test_message')
        assert out.getvalue() == ''



# Generated at 2022-06-22 12:41:22.098885
# Unit test for function get_source
def test_get_source():
    def foo(x, y=10):
        return x * y
    assert get_source(foo) == 'return x * y'



# Generated at 2022-06-22 12:41:24.305393
# Unit test for function get_source
def test_get_source():
    def test():
        pass

    assert get_source(test) == 'def test():\n    pass\n'

# Generated at 2022-06-22 12:41:34.850286
# Unit test for function debug
def test_debug():
    import io
    buffer = io.StringIO()
    try:
        sys.stderr = buffer
        settings.debug = True
        debug(lambda: "debugged foobar")
        assert buffer.getvalue().strip() == "DEBUG   debugged foobar", buffer.getvalue()
        buffer.truncate(0)
        buffer.seek(0)
        settings.debug = False
        debug(lambda: "should not appear")
        assert buffer.getvalue().strip() == "", buffer.getvalue()
        buffer.truncate(0)
        buffer.seek(0)
        settings.debug = False
        warn("should warn")
        expected = "WARNING should warn"
        assert buffer.getvalue().strip() == expected, buffer.getvalue()
    finally:
        sys.stderr = sys.__stderr

# Generated at 2022-06-22 12:41:38.432615
# Unit test for function get_source
def test_get_source():
    expected = '''
    def foo(bar):
        print(bar)
    '''
    def foo(bar: Any) -> None:
        print(bar)

    assert get_source(foo) == expected

# Generated at 2022-06-22 12:41:40.725347
# Unit test for function get_source
def test_get_source():
    def source_function():
        x = 1
        y = x + 2
        return y


# Generated at 2022-06-22 12:41:45.702076
# Unit test for function get_source
def test_get_source():
    def fn1():
        def inner():
            pass

    def fn2():
        def inner():
            pass

    # Output must be
    # def inner():
    #     pass
    assert get_source(fn1) == get_source(fn2)

# Generated at 2022-06-22 12:41:53.388594
# Unit test for function debug
def test_debug():
    import io
    import sys

    import pytest

    messages.debug = 'DEBUG: {}'
    original_stderr = sys.stderr
    stderr = io.StringIO()
    sys.stderr = stderr

    settings.debug = False
    debug(lambda: 'debug message')
    assert stderr.getvalue() == ''

    settings.debug = True
    debug(lambda: 'debug message')
    assert stderr.getvalue() == 'DEBUG: debug message\n'
    stderr.truncate(0)
    stderr.seek(0)

    try:
        yield
    finally:
        sys.stderr = original_stderr

# Generated at 2022-06-22 12:41:55.281435
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'pass'

# Generated at 2022-06-22 12:42:09.171965
# Unit test for function debug
def test_debug():
    setting_debug = settings.debug
    settings.debug = True
    try:
        debug(lambda: 'hi')
    finally:
        settings.debug = setting_debug


# Generated at 2022-06-22 12:42:10.865296
# Unit test for function get_source
def test_get_source():
    def test_function():
        return "test"
    assert get_source(test_function) == "return \"test\""

# Generated at 2022-06-22 12:42:16.870231
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    def bar():
        pass

    def baz():
        pass

    assert get_source(foo) == 'def foo():\n    pass\n', 'Can\'t get source code for function foo'
    assert get_source(bar) == 'def bar():\n    pass\n', 'Can\'t get source code for function bar'
    assert get_source(baz) == 'def baz():\n    pass\n', 'Can\'t get source code for function baz'

# Generated at 2022-06-22 12:42:19.007006
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            pass

    assert get_source(foo).strip() == 'def bar():'

# Generated at 2022-06-22 12:42:22.732877
# Unit test for function debug
def test_debug():
    old_debug = settings.debug
    result = []
    try:
        settings.debug = True
        debug(lambda: 42)
        assert result == []
        debug(lambda: result.append(1))
        assert result == [1]
    finally:
        settings.debug = old_debug

# Generated at 2022-06-22 12:42:29.617296
# Unit test for function debug
def test_debug():
    import unittest
    import logging
    import io

    class TestDebug(unittest.TestCase):
        def test_prints_debug_messages_if_debug_is_enabled(self):
            stderr = io.StringIO()

            def message():
                return 'Some message'

            old_stderr = sys.stderr
            sys.stderr = stderr
            settings.debug = True
            debug(message)
            sys.stderr = old_stderr
            settings.debug = False
            self.assertEqual(stderr.getvalue(), messages.debug('Some message') + '\n')

        def test_does_not_print_debug_messages_if_debug_is_disabled(self):
            stderr = io.StringIO()


# Generated at 2022-06-22 12:42:32.514969
# Unit test for function get_source
def test_get_source():  # pragma: no cover
    def foo(*args):
        return args
    assert get_source(foo) == 'return args'

# Generated at 2022-06-22 12:42:35.522582
# Unit test for function eager
def test_eager():
    def func() -> Iterator[int]:
        return (i for i in range(10))

    assert eager(func)() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-22 12:42:41.656034
# Unit test for function debug
def test_debug():
    messages.debug = lambda message: 'DEBUG: {}'.format(message)
    messages.warn = lambda message: 'WARN: {}'.format(message)
    debug_message = 'Debug message'

    mocked_print = mock.Mock()
    with mock.patch('builtins.print', mocked_print):
        debug(lambda: debug_message)
        debug(lambda: 'No debug')

    mocked_print.assert_called_once_with(messages.debug(debug_message), file=mock.ANY)

# Generated at 2022-06-22 12:42:43.167506
# Unit test for function eager
def test_eager():
    @eager
    def a():
        yield 1
    assert a() == [1]

# Generated at 2022-06-22 12:43:19.365988
# Unit test for function get_source
def test_get_source():
    from os import path
    from .. import module_utils

    current_dir = path.dirname(path.dirname(__file__))
    source_file = path.join(current_dir, 'module_utils.py')
    with open(source_file) as f:
        source_file_lines = f.readlines()

    def test_fn():
        pass

    function_name = 'test_fn'

    assert get_source(test_fn) == ''.join(source_file_lines[150:154])
    assert get_source(module_utils.ModuleFail) == ''.join(source_file_lines[156:161])
    assert get_source(module_utils.ModuleSuccess) == ''.join(source_file_lines[162:166])
    assert get_source(module_utils.parse_args)

# Generated at 2022-06-22 12:43:25.016198
# Unit test for function eager
def test_eager():
    @eager
    def test_func(a: str, b: str) -> Iterable[str]:
        return a + b

    assert test_func('a', 'b') == ['ab']
    # Type testing
    assert test_func.__annotations__['return'] == List[str]
    assert test_func.__annotations__['a'] == str
    assert test_func.__annotations__['b'] == str



# Generated at 2022-06-22 12:43:27.465342
# Unit test for function get_source
def test_get_source():
    def foo():
        """Simple docstring"""
        print('Hello')
        print('World')

    assert get_source(foo) == '"""Simple docstring"""\nprint(\'Hello\')\nprint(\'World\')'

# Generated at 2022-06-22 12:43:29.580359
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2

    g = eager(f)
    assert f() == g()

# Generated at 2022-06-22 12:43:32.960366
# Unit test for function eager
def test_eager():
    class Test:
        def __init__(self, lst):
            self.lst = lst

        @eager
        def add(self) -> Iterable[int]:
            for i in self.lst:
                yield i + 1

    t = Test([1, 2])
    assert t.add() == [2, 3]

# Generated at 2022-06-22 12:43:37.254010
# Unit test for function debug
def test_debug():
    calls = []
    def get_message():
        calls.append(True)
        return 'done'
    debug(get_message)
    assert calls == []
    settings.debug = True
    debug(get_message)
    assert calls == [True]
    settings.debug = False
    debug(get_message)
    assert calls == [True]


# Generated at 2022-06-22 12:43:46.519338
# Unit test for function get_source

# Generated at 2022-06-22 12:43:48.692861
# Unit test for function eager
def test_eager():
    from ...tests.test_autodiff import run_test_eager  # pylint: disable=unused-variable
    run_test_eager()



# Generated at 2022-06-22 12:43:51.026579
# Unit test for function get_source
def test_get_source():
    def foo():
        return 1
    assert get_source(foo) == 'return 1'

# Generated at 2022-06-22 12:43:56.034978
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == '    assert get_source(test_get_source) == \'    assert get_source(test_get_source) == \\\'{0}\\\'\''.format(
        get_source(test_get_source).replace('\\', '\\\\').replace('"', '\\"'))

# Generated at 2022-06-22 12:44:47.889962
# Unit test for function debug
def test_debug():
    from unittest.mock import patch

    with patch('sys.stderr') as mock_stderr:
        debug(lambda: 'message')
        mock_stderr.write.assert_called_once_with('\x1b[90mmessage\x1b[0m\n')

# Generated at 2022-06-22 12:44:51.285011
# Unit test for function get_source
def test_get_source():
    def test_function(a, b=4, c="srds"):
        def other_function(d, e=6, f="fefsd"):
            pass

    expected = '''def test_function(a, b=4, c="srds"):
    def other_function(d, e=6, f="fefsd"):
        pass'''

    assert expected == get_source(test_function)

# Generated at 2022-06-22 12:44:54.814390
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            return 1
        return bar()

    message = "expected 'return 1' got 'return {}'".format(get_source(foo))
    assert get_source(foo) == 'return 1', message



# Generated at 2022-06-22 12:44:59.222063
# Unit test for function get_source
def test_get_source():
    def test():
        '''
            This is function test()
        '''
        print('Hello')

    assert get_source(test) == '''def test():
    '''

# Generated at 2022-06-22 12:45:01.842584
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    def bar():
        return 1

    assert get_source(foo) == 'pass'
    assert get_source(bar) == 'return 1'

# Generated at 2022-06-22 12:45:04.411659
# Unit test for function eager
def test_eager():
    @eager
    def ids() -> Iterable[int]:
        for i in range(10):
            yield i
    assert ids() == list(range(10))

# Generated at 2022-06-22 12:45:10.925486
# Unit test for function debug
def test_debug():
    from unittest.mock import patch

    try:
        settings.debug = True

        with patch('sys.stderr') as stderr:
            debug(lambda: 'Hello!')
            assert list(stderr.method_calls) == [('write', ('\033[96m[DEBUG] Hello!\033[0m\n',), {})]
        
        settings.debug = False

        with patch('sys.stderr'):
            debug(lambda: 'Hello!')
            assert []
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:45:17.247985
# Unit test for function debug
def test_debug():
    import sys
    from io import StringIO
    from ..conf import settings
    from contextlib import redirect_stderr
    settings.debug = True
    with redirect_stderr(StringIO()) as stderr:
        debug(lambda: 'test debug message')
    assert 'test debug message' in stderr.getvalue()



# Generated at 2022-06-22 12:45:26.142774
# Unit test for function debug
def test_debug():
    from .utils import settings
    from functools import partial
    from contextlib import contextmanager
    from io import StringIO
    import sys
    debug('Message')

    @contextmanager
    def mock_debug():
        original = settings.debug
        settings.debug = True
        try:
            with StringIO() as stream:
                sys.stderr = stream
                yield partial(stream.getvalue)
        finally:
            settings.debug = original

    with mock_debug() as get_output:
        debug('Message')
        assert get_output().startswith('[DEBUG]')
        assert get_output().endswith('Message\n')

# Generated at 2022-06-22 12:45:28.827275
# Unit test for function eager
def test_eager():
    @eager
    def test_fn() -> Iterable[int]:
        for i in range(5):
            yield i

    assert test_fn() == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:47:33.830494
# Unit test for function get_source
def test_get_source():
    def fn():
        return "Hello, World!"

    assert get_source(fn) == "return \"Hello, World!\""



# Generated at 2022-06-22 12:47:36.581362
# Unit test for function get_source
def test_get_source():
    def func():
        x = 1
        return True

    result = get_source(func)

    assert 'def func():' in result
    assert 'x = 1' not in result
    assert 'return True' in result

# Generated at 2022-06-22 12:47:45.153163
# Unit test for function get_source
def test_get_source():
    def foo():
        """documentation"""
        bar()

    def bar():
        baz()


    def baz():
        pass

    source_foo = get_source(foo)
    source_bar = get_source(bar)
    source_baz = get_source(baz)
    assert source_foo == 'def foo():\n    """documentation"""\n    bar()\n'
    assert source_bar == 'def bar():\n    baz()\n'
    assert source_baz == 'def baz():\n    pass\n'

# Generated at 2022-06-22 12:47:49.625699
# Unit test for function get_source
def test_get_source():
    def some_function():
        var = 'x'

    expected = """
    var = 'x'
    """
    assert get_source(some_function) == expected

# Generated at 2022-06-22 12:47:53.521271
# Unit test for function get_source
def test_get_source():
    source = get_source(get_source)
    source_lines = source.split('\n')
    assert source_lines[0] == "source = get_source(get_source)"
    assert source_lines[-1] == ""
    assert len(source_lines) == 7

# Generated at 2022-06-22 12:47:58.385350
# Unit test for function get_source
def test_get_source():
    def some_function(a, b):
        return a + b
        pass
    a = get_source(some_function)
    b = '''def some_function(a, b):
    return a + b
    pass'''
    assert a == b

# Generated at 2022-06-22 12:47:59.712909
# Unit test for function get_source

# Generated at 2022-06-22 12:48:02.052769
# Unit test for function get_source
def test_get_source():
    def foo():
        return 'foo'
    assert get_source(foo) == "def foo():\n    return 'foo'"



# Generated at 2022-06-22 12:48:05.271923
# Unit test for function get_source
def test_get_source():
    def fn():
        a = 1
        def b():
            pass

    assert get_source(fn) == 'a = 1\n\ndef b():\n    pass'

# Generated at 2022-06-22 12:48:08.592221
# Unit test for function get_source
def test_get_source():

    def test():
        return 1

    source_lines = getsource(test).split('\n')
    padding = len(re.findall(r'^(\s*)', source_lines[0])[0])
    assert get_source(test) == '\n'.join(line[padding:] for line in source_lines)