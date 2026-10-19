

# Generated at 2022-06-22 12:38:28.713140
# Unit test for function eager
def test_eager():
    @eager
    def fn(n):
        i = 0
        while i < n:
            yield i
            i += 1

    assert fn(3) == [0, 1, 2]

# Generated at 2022-06-22 12:38:30.517481
# Unit test for function get_source
def test_get_source():
    def fn():
        """
        Function description.

        Function description.
        """
        pass


# Generated at 2022-06-22 12:38:41.166428
# Unit test for function eager
def test_eager():
    from collections import namedtuple
    from inspect import signature

    TestResult = namedtuple('TestResult', 'name result')

    def test(fn: Callable, args: Iterable, kwargs: dict={}, result: list=None) -> TestResult:
        try:
            actual = fn(*args, **kwargs)
        except Exception as e:
            return TestResult(fn.__name__, e)
        else:
            if result is None:
                return TestResult(fn.__name__, actual)
            else:
                return TestResult(fn.__name__, actual == result)

    def get_tests() -> Iterable[Callable]:
        def test_function(a, b, c):
            yield a
            yield b
            yield c

        yield eager(test_function)


# Generated at 2022-06-22 12:38:47.868272
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == 'def get_source(fn: Callable[..., Any]) -> str:\n    """Returns source code of the function."""\n    source_lines = getsource(fn).split(\'\\n\')\n    padding = len(re.findall(r\'^(\\s*)\', source_lines[0])[0])\n    return \'\\n\'.join(line[padding:] for line in source_lines)'

# Generated at 2022-06-22 12:38:57.328181
# Unit test for function get_source
def test_get_source():

    def func():
        pass

    def func2():
        return 5

    def func3():
        x = 5

    def func4():
        x = 5
        return x

    def func5():
        return func2()

    def func6():
        return 5 + 5

    assert get_source(func) == 'pass'
    assert get_source(func2) == 'return 5'
    assert get_source(func3) == 'x = 5'
    assert get_source(func4) == 'x = 5\nreturn x'
    assert get_source(func5) == 'return func2()'
    assert get_source(func6) == 'return 5 + 5'



# Generated at 2022-06-22 12:38:59.479054
# Unit test for function get_source
def test_get_source():
    def get_source_test():
        return 'get_source_test'
    assert get_source(get_source_test) == 'return \'get_source_test\''

# Generated at 2022-06-22 12:39:02.486284
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: "Hello world")
        # TODO: Capture stdout and check the message
    finally:
        settings.debug = False



# Generated at 2022-06-22 12:39:06.084874
# Unit test for function debug
def test_debug():
    lines = []
    for message in ['1', '2', '3']:
        def f():
            return message
        debug(f)
        lines.append(f())
    assert lines == ['1', '2', '3']

# Generated at 2022-06-22 12:39:07.727229
# Unit test for function get_source
def test_get_source():
    def func():
        pass
    assert get_source(func) == 'def func():\n    pass'


# Generated at 2022-06-22 12:39:10.038512
# Unit test for function get_source
def test_get_source():
    def abc(): pass
    assert get_source(abc) == 'def abc(): pass'
    def def_(): pass
    assert get_source(def_) == 'def def_(): pass'

# Generated at 2022-06-22 12:39:18.035577
# Unit test for function debug
def test_debug():
    class Message:
        def __init__(self) -> None:
            self.debug = False

        def get_message(self) -> str:
            self.debug = True
            return 'Test debug message'

    message = Message()
    settings.debug = True
    debug(message.get_message)
    assert message.debug
    settings.debug = False
    debug(message.get_message)
    assert not message.debug



# Generated at 2022-06-22 12:39:26.619147
# Unit test for function debug
def test_debug():
    from ..conf import set_settings
    from io import StringIO

    # Check that debug does not print anything if debug is disabled
    set_settings(debug=False)
    stream = StringIO()
    sys.stderr = stream
    debug(lambda: 'A')
    assert stream.getvalue() == ''

    # Check that debug prints the message if debug is enabled
    set_settings(debug=True)
    stream = StringIO()
    sys.stderr = stream
    debug(lambda: 'B')
    assert stream.getvalue() == messages.debug('B') + '\n'
    sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:28.727808
# Unit test for function debug
def test_debug():
  debug(lambda: "Debug me!")
  debug(lambda: "Debug still me!")
  debug(lambda: "Debug still me!")

# Generated at 2022-06-22 12:39:35.733099
# Unit test for function debug
def test_debug():
    import io
    import sys

    def test_warn():
        def get_message():
            return 'Hello, World!'
        sys.stderr = io.StringIO()
        debug(get_message)
        message = sys.stderr.getvalue()
        sys.stderr = sys.__stderr__
        assert message == '\x1b[33mDebug: Hello, World!\x1b[0m\n', message

    test_warn()

# Generated at 2022-06-22 12:39:37.731152
# Unit test for function get_source
def test_get_source():
    def f():
        pass


    assert get_source(f) == 'def f():\n    pass'

# Generated at 2022-06-22 12:39:41.713620
# Unit test for function get_source
def test_get_source():
    def f():
        """Docstring of f."""
        return 1

    source = get_source(f)

    assert "def f():" in source
    assert "return 1" in source
    assert "\"\"\"Docstring" not in source

# Generated at 2022-06-22 12:39:45.388432
# Unit test for function eager
def test_eager():
    def f1(x):
        print('f', x)
        yield x ** 2
        yield x ** 3
        yield x ** 4

    assert eager(f1)(2) == [4, 8, 16]



# Generated at 2022-06-22 12:39:48.314747
# Unit test for function eager
def test_eager():
    def my_generator():
        for i in range(3):
            yield i

    assert eager(my_generator)() == [0, 1, 2]


# Unit tests for class VariablesGenerator

# Generated at 2022-06-22 12:39:53.718181
# Unit test for function debug
def test_debug():
    messages.debug = lambda text: f'DEBUG{text}!'

    debug(lambda: 'abc')
    assert sys.stderr.getvalue() == ''
    sys.stderr.truncate(0)

    settings.debug = True
    debug(lambda: 'abc')
    assert sys.stderr.getvalue() == 'DEBUGabc!\n'
    sys.stderr.truncate(0)

# Generated at 2022-06-22 12:40:03.236872
# Unit test for function debug
def test_debug():
    def func(arg_1: int) -> int:
        debug(lambda: 'debug message')
        return arg_1

    import tempfile
    import unittest.mock
    from contextlib import contextmanager

    with unittest.mock.patch('sys.stderr', tempfile.TemporaryFile('w+')) as mock_stderr:
        func(123)
        mock_stderr.seek(0)
        assert mock_stderr.read() == ''

    with unittest.mock.patch('sys.stderr', tempfile.TemporaryFile('w+')) as mock_stderr:
        with debug_mode():
            func(123)
            mock_stderr.seek(0)

# Generated at 2022-06-22 12:40:08.432245
# Unit test for function get_source
def test_get_source():
    def a(b):
        pass

    def x(y):
        pass

    assert get_source(a) == 'pass'
    assert get_source(x) == 'pass'

# Generated at 2022-06-22 12:40:13.360113
# Unit test for function get_source
def test_get_source():
    def foo():
        """Function with some docstring."""
        a = 1
        b = 2
        c = 3
        return a, b, c

    source_lines = 'a = 1\nb = 2\nc = 3\nreturn a, b, c'
    assert get_source(foo) == source_lines


# Generated at 2022-06-22 12:40:20.614630
# Unit test for function get_source
def test_get_source():
    def test_function(arg1, arg2):
        print('arg1: {}'.format(arg1))
        print('arg2: {}'.format(arg2))
        return arg1 + arg2

    assert get_source(test_function) == '''def test_function(arg1, arg2):
    print('arg1: {}'.format(arg1))
    print('arg2: {}'.format(arg2))
    return arg1 + arg2
'''

# Generated at 2022-06-22 12:40:24.761421
# Unit test for function eager
def test_eager():
    from collections import deque
    from functools import partial

    @eager
    def fn(start: int, stop: int) -> deque:
        return deque(range(start, stop))

    assert fn(3, 5) == [3, 4]

# Generated at 2022-06-22 12:40:28.051219
# Unit test for function get_source
def test_get_source():
    def foo() -> None:
        pass
    source = inspect.getsource(foo)
    assert source == get_source(foo)

# Generated at 2022-06-22 12:40:32.308618
# Unit test for function get_source
def test_get_source():
    def func(x, y):
        a = x + 1
        b = 2 + y
        return (a, b)
    assert  get_source(func) == "a = x + 1\n        b = 2 + y\n        return (a, b)"

# Generated at 2022-06-22 12:40:34.253615
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'pass'

# Generated at 2022-06-22 12:40:38.252041
# Unit test for function get_source
def test_get_source():
    def fn(a: int, b: str) -> None:
        x = a + 1
        return b

    expected = '''def fn(a: int, b: str) -> None:
    x = a + 1
    return b'''
    assert get_source(fn) == expected

# Generated at 2022-06-22 12:40:44.496055
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    def bar():
        def foo():
            pass
        return foo

    def baz():
        def foo():
            pass
        return foo()

    assert get_source(foo) == 'def foo():\n    pass'
    assert get_source(bar()) == 'def foo():\n    pass'
    assert get_source(baz()) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:40:49.606179
# Unit test for function get_source
def test_get_source():
    def foo(a, b, c=1, d=1, e=1):
        """blabla"""
        return a + b + c + d + e

    assert get_source(foo) == """def foo(a, b, c=1, d=1, e=1):
    return a + b + c + d + e"""

# Generated at 2022-06-22 12:41:02.890346
# Unit test for function debug
def test_debug():
    from . import helpers
    from . import messages

    settings.debug = True
    try:
        def get_message() -> str:
            return 'test'
        assert helpers.capture_output(helpers.debug, get_message) == messages.debug('test') + '\n'

        settings.debug = False
        assert helpers.capture_output(helpers.debug, get_message) == ''
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:41:05.417112
# Unit test for function get_source
def test_get_source():
    def test_function(x):
        return x + 2

    test_source_code = 'return x + 2'
    assert get_source(test_function) == test_source_code  # type: ignore

# Generated at 2022-06-22 12:41:06.675907
# Unit test for function debug
def test_debug():
    from .test_cases import get_debug_message
    debug(get_debug_message)

# Generated at 2022-06-22 12:41:09.978983
# Unit test for function debug
def test_debug():
    from collections import namedtuple
    Message = namedtuple('Message', 'msg')
    messages.debug = lambda msg: Message(msg)
    settings.debug = True
    debug(lambda: 'Hello, world!')



# Generated at 2022-06-22 12:41:20.007136
# Unit test for function debug
def test_debug():
    import io
    import sys
    stream = io.StringIO()
    sys.stderr = stream
    settings.debug = True
    assert not stream.getvalue()
    debug(lambda: 'hello')
    assert stream.getvalue() == '\n'.join(('py_backwards debug:', 'hello', ''))
    settings.debug = False
    debug(lambda: 'hello')
    assert stream.getvalue() == '\n'.join(('py_backwards debug:', 'hello', ''))
    settings.debug = True
    debug(lambda: 'hello')
    assert stream.getvalue() == '\n'.join(('py_backwards debug:', 'hello', '',
                                           'py_backwards debug:', 'hello', ''))
    settings.debug = False

# Generated at 2022-06-22 12:41:22.981709
# Unit test for function eager
def test_eager():

    @eager
    def x(i: int) -> Iterable[int]:
        return range(i)

    assert x(5) == [0, 1, 2, 3, 4]



# Generated at 2022-06-22 12:41:27.329144
# Unit test for function get_source
def test_get_source():
    def test(a, b):
        '''
        This is a docstring.
        '''
        return a + b

    test_source = get_source(test)
    assert test_source == '''def test(a, b):
    '''

# Generated at 2022-06-22 12:41:31.755567
# Unit test for function debug
def test_debug():
    out = StringIO()
    with patch('sys.stderr', out):
        debug(lambda: 'hi')
        assert out.getvalue() == ''
        settings.debug = True
        debug(lambda: 'hi')
        assert out.getvalue().strip() == 'DEBUG: hi'
        settings.debug = False

test_debug()

# Generated at 2022-06-22 12:41:35.405518
# Unit test for function get_source
def test_get_source():
    def doc():
        """
        This function is just for testing.
        """
        pass

    assert get_source(doc) == '"""\n        This function is just for testing.\n        """\n        pass'

# Generated at 2022-06-22 12:41:45.621797
# Unit test for function get_source

# Generated at 2022-06-22 12:42:08.936996
# Unit test for function get_source
def test_get_source():
    def f():
        print(10)
        print(20)

    assert get_source(f) == 'print(10)\nprint(20)'



# Generated at 2022-06-22 12:42:10.287871
# Unit test for function get_source
def test_get_source():
    def fn():
        return 1
    test_source = 'return 1'
    assert get_source(fn) == test_source

# Generated at 2022-06-22 12:42:14.832898
# Unit test for function get_source
def test_get_source():
    import pytest
    def f(a, b, c):
        x = a + b + c

    assert get_source(f) == 'x = a + b + c'
    assert get_source(test_get_source) == pytest.__file__

# Generated at 2022-06-22 12:42:16.514882
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'def fn():\n    pass\n'

# Generated at 2022-06-22 12:42:19.007486
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2
        yield 3
    assert eager(f)() == [1, 2, 3]



# Generated at 2022-06-22 12:42:21.300614
# Unit test for function get_source
def test_get_source():
    import re
    def f():
        print('Hi')
    assert re.match(r'print\s*\(.*fdafds', get_source(f))

# Generated at 2022-06-22 12:42:23.991899
# Unit test for function get_source
def test_get_source():
    def some_function():
        pass

    assert get_source(sum) == 'sum(iterable, start=0)'

    assert get_source(test_get_source) == """    def some_function():
        pass"""

# Generated at 2022-06-22 12:42:35.861290
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == 'def test_get_source():\n    assert get_source(test_get_source) == \'def test_get_source():\\n    assert get_source(test_get_source) == \\\'def test_get_source():\\\\n    assert get_source(test_get_source) == \\\\\'def test_get_source():\\\\\\\\n    assert get_source(test_get_source) == \\\\\\\\\'def test_get_source():\\\\\\\\\\\\n    assert get_source(test_get_source) == \\\\\\\\\\\\\'def test_get_source():\\\\\\\\\\\\\\n    assert get_source(test_get_source) == \\\\\\\\\\\\\\\'def test_get_source():\\\\\\\\\\\\\\\''

if __name__ == '__main__':
    test_get_source

# Generated at 2022-06-22 12:42:42.333602
# Unit test for function debug
def test_debug():
    assert settings.debug == False
    messages.debug = lambda x : x
    import io 
    captured_output = io.StringIO()
    sys.stderr = captured_output
    debug(lambda : "Hello world")
    assert captured_output.getvalue().rstrip() == ""
    settings.debug = True
    debug(lambda : "Hello world")
    assert captured_output.getvalue().rstrip() == "d: Hello world"

# Generated at 2022-06-22 12:42:44.152899
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == "def foo():\n    pass"

# Generated at 2022-06-22 12:43:36.791326
# Unit test for function get_source
def test_get_source():

    def foo():
        bar = 1
        return bar

    assert get_source(foo) == 'bar = 1\nreturn bar\n'

# Generated at 2022-06-22 12:43:38.612348
# Unit test for function debug
def test_debug():
    def get_message():
        return "message_1"
    debug(get_message)



# Generated at 2022-06-22 12:43:41.036809
# Unit test for function get_source
def test_get_source():
    def foo():
        a = 1
        return a

    assert get_source(foo) == 'a = 1\nreturn a'

# Generated at 2022-06-22 12:43:41.951590
# Unit test for function debug
def test_debug():
    debug(lambda: "Hello world")
    assert True

# Generated at 2022-06-22 12:43:45.360231
# Unit test for function get_source
def test_get_source():
    def bar():
        """doc string"""
        return 123
    assert 'def bar():' in get_source(bar)
    assert '"""doc string"""' in get_source(bar)
    assert 'return 123' in get_source(bar)
    assert '    return 123' not in get_source(bar)

# Generated at 2022-06-22 12:43:47.699738
# Unit test for function get_source
def test_get_source():
    def inner(x: int) -> int:
        print('var')
        return x * x
    assert get_source(inner) == 'print(\'var\')\nreturn x * x\n'


# Generated at 2022-06-22 12:43:50.713696
# Unit test for function eager
def test_eager():
    @eager
    def double(x):
        yield x
        yield x

    assert double(1) == [1, 1]

# Generated at 2022-06-22 12:43:55.060654
# Unit test for function eager
def test_eager():
    @eager
    def f(n: int) -> Iterable[int]:
        i = 0
        while (i < n):
            yield i
            i += 1

    assert list(range(10)) == f(10)



# Generated at 2022-06-22 12:44:06.106672
# Unit test for function debug
def test_debug():
    msg = 'This is a test message'

    def get_msg():
        return msg

    with patch('builtins.print') as print_mock:
        debug(get_msg)
        print_mock.assert_called_once_with('{}: {}'.format(messages.debug, msg), file=sys.stderr)

    with patch('py_backwards.utils.settings.debug'):
        with patch('builtins.print') as print_mock:
            debug(get_msg)
            assert print_mock.called

    with patch('py_backwards.utils.settings.debug', False):
        with patch('builtins.print') as print_mock:
            debug(get_msg)
            assert not print_mock.called

# Generated at 2022-06-22 12:44:10.329125
# Unit test for function debug
def test_debug():
    from .test_utils import captured_stderr

    settings.debug = True

    with captured_stderr() as stderr:
        debug(lambda: 'Debug message')

    assert 'Debug message' in stderr.getvalue()

# Generated at 2022-06-22 12:46:00.699068
# Unit test for function debug
def test_debug():
    import sys
    import tempfile
    from contextlib import redirect_stderr

    # no debug
    with redirect_stderr(open(os.devnull, 'w')):
        debug(lambda: "foo")
    assert not open(os.devnull).read()

    # debug
    with tempfile.TemporaryFile('w+') as file:
        with redirect_stderr(file):
            debug(lambda: "foo")
        file.seek(0)
        assert file.read() == 'DEBUG: foo\n'

# Generated at 2022-06-22 12:46:07.608643
# Unit test for function debug
def test_debug():
    import sys
    import inspect
    from io import StringIO
    from ..conf import settings
    from .. import messages
    from . import debug

    settings.debug = True

    captured_output = StringIO()
    sys.stderr = captured_output

    debug(lambda: 'message')

    try:
        assert captured_output.getvalue() == messages.debug('message') + '\n'
    finally:
        sys.stderr = sys.__stderr__
        settings.debug = False

# Generated at 2022-06-22 12:46:08.827296
# Unit test for function debug
def test_debug():
    debug(lambda: 'Debug message')

# Generated at 2022-06-22 12:46:10.980579
# Unit test for function eager
def test_eager():
    @eager
    def foo(n):
       for i in range(n):
           yield i

    assert foo(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:46:13.033643
# Unit test for function get_source
def test_get_source():
    def f(a):
        return a

    assert get_source(f).strip() == 'return a'

# Generated at 2022-06-22 12:46:18.335798
# Unit test for function debug
def test_debug():
    """
    >>> _counter = 0
    >>> def _increment_counter():
    ...     global _counter
    ...     _counter += 1
    ...     return _counter

    >>> debug(_increment_counter)
    >>> _counter
    1

    >>> settings.debug = False
    >>> debug(_increment_counter)
    >>> _counter
    1

    >>> settings.debug = True
    >>> debug(_increment_counter)
    >>> _counter
    2
    """


# Generated at 2022-06-22 12:46:30.050286
# Unit test for function debug
def test_debug():
    class MockStdErr:
        def __init__(self) -> None:
            self.called = False

        def write(self, message: str) -> None:
            self.called = True
            assert message == messages.debug('test') + '\n'

    class MockSettings:
        debug = True

    sys.stderr = MockStdErr()
    _settings = sys.modules['py_backwards.conf.settings']
    original = sys.modules['py_backwards.conf.settings']
    sys.modules['py_backwards.conf.settings'] = MockSettings()
    try:
        debug(lambda: 'test')
    finally:
        sys.modules['py_backwards.conf.settings'] = original
    assert sys.stderr.called



# Generated at 2022-06-22 12:46:32.074310
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    assert get_source(function) == 'def function():\n    pass'

# Generated at 2022-06-22 12:46:33.972570
# Unit test for function get_source
def test_get_source():
    def dummy():
        return 42

    assert get_source(dummy) == 'return 42'

# Generated at 2022-06-22 12:46:37.202425
# Unit test for function debug
def test_debug():
    def get_message() -> str:
        return "this is the message of debug"
    # test when settings.debug == False
    settings.debug = False
    debug(get_message)
    # test when settings.debug == True
    settings.debug = True
    debug(get_message)