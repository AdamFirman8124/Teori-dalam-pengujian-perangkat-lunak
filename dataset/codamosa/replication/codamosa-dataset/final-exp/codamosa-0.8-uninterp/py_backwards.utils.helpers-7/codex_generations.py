

# Generated at 2022-06-22 12:38:25.261174
# Unit test for function debug
def test_debug():
    settings.debug = True

    try:
        debug(lambda: 'This is a debug message.')
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:38:26.577857
# Unit test for function get_source
def test_get_source():
    def foo():
        print(x())

    assert get_source(foo) == 'print(x())\n'

# Generated at 2022-06-22 12:38:29.857158
# Unit test for function get_source
def test_get_source():
    """
    Unit test for function get_source.
    """
    def _fn():
        pass

    assert get_source(_fn) == "def _fn():\n    pass"



# Generated at 2022-06-22 12:38:32.007506
# Unit test for function eager
def test_eager():
    items = [1, 2, 3]
    assert eager(lambda: items)() == items



# Generated at 2022-06-22 12:38:34.655201
# Unit test for function get_source
def test_get_source():
    def some_function(a: int, b: int) -> int:
        return a + b
    assert get_source(some_function) == 'return a + b'

# Generated at 2022-06-22 12:38:38.569945
# Unit test for function debug
def test_debug():
    if settings.debug:
        raise AssertionError('settings.debug should equal to False.')

    settings.debug = True

    try:
        print('Test', end=' ')
        debug(lambda: 'Log')
    finally:
        settings.debug = False


# Generated at 2022-06-22 12:38:43.735423
# Unit test for function debug
def test_debug():
    print_value = None
    def print_func(message):
        nonlocal print_value
        print_value = message

    sys.stderr.write = print_func

    debug(lambda: 'test')
    assert print_value == messages.debug('test')

    settings.debug = False
    debug(lambda: 'test')
    assert print_value == messages.debug('test')

    settings.debug = True


# Generated at 2022-06-22 12:38:46.816053
# Unit test for function eager
def test_eager():
    @eager
    def generator() -> Iterable[int]:
        yield 1
        yield 2
        yield 3
        yield 4

    assert generator() == [1, 2, 3, 4]

# Generated at 2022-06-22 12:38:50.803145
# Unit test for function eager
def test_eager():
    def func():
        yield 1
        yield 2

    @eager
    def func1():
        yield 1
        yield 2

    assert func() == [1, 2]
    assert func1() == [1, 2]

# Generated at 2022-06-22 12:38:58.130305
# Unit test for function debug
def test_debug():
    from mock import patch, call
    from io import StringIO
    from functools import partial
    stderr = StringIO()
    with patch('sys.stderr', stderr):
        settings.debug = True
        debug(lambda: 'foo')
        assert stderr.getvalue() == partial(messages.debug, 'foo')() + '\n'
        settings.debug = False
        debug(lambda: 'bar')
        assert stderr.getvalue() == partial(messages.debug, 'foo')() + '\n'



# Generated at 2022-06-22 12:39:02.562517
# Unit test for function debug
def test_debug():
    debug(lambda: 'test')
    settings.debug = False
    debug(lambda: 'test')
    settings.debug = True
    debug(lambda: 'test')

# Generated at 2022-06-22 12:39:06.751787
# Unit test for function eager
def test_eager():
    @eager
    def generate_iterable(n):
        for i in range(n):
            yield i
    assert generate_iterable(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Unit test function for function get_source

# Generated at 2022-06-22 12:39:11.985013
# Unit test for function debug
def test_debug():
    from io import StringIO
    from ..conf import settings

    debug_message = 'debug message'
    output = StringIO()
    settings.debug = False
    sys.stderr = output
    debug(lambda: debug_message)
    output = output.getvalue()
    assert output == ''

    output = StringIO()
    settings.debug = True
    sys.stderr = output
    debug(lambda: debug_message)
    output = output.getvalue()
    assert output == messages.debug(debug_message) + '\n'

    sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:18.718672
# Unit test for function debug
def test_debug():
    out = StringIO()
    with contextlib.redirect_stderr(out):
        debug(lambda: 'test')
    assert out.getvalue() == ''
    settings.debug = True
    out = StringIO()
    with contextlib.redirect_stderr(out):
        debug(lambda: 'test')
    assert out.getvalue() == '\033[1m\033[36mdebug:\033[0m test\n'
    settings.debug = False

# Generated at 2022-06-22 12:39:21.871295
# Unit test for function get_source
def test_get_source():
    def foo(*args: int, **kwargs: int) -> int:
        return sum(*args, **kwargs)

    assert get_source(foo) == 'return sum(*args, **kwargs)'

# Generated at 2022-06-22 12:39:25.671222
# Unit test for function get_source
def test_get_source():
    def fn():
        a = 1
        b = 2
        return a + b
    assert get_source(fn) == 'a = 1\nb = 2\nreturn a + b'

if __name__ == "__main__":
    from .message import Test
    Test.run()

# Generated at 2022-06-22 12:39:27.961962
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'def fn():\n    pass'

# Generated at 2022-06-22 12:39:35.030123
# Unit test for function debug
def test_debug():
    import io
    import sys
    output = io.StringIO()
    try:
        sys.stdout = output
        settings.debug = False
        debug(lambda: "shouldn't be called")
        assert(output.getvalue() == "")
        settings.debug = True
        debug(lambda: "should be called")
        assert(output.getvalue() == "DEBUG: should be called\n")
    finally:
        sys.stdout = sys.__stdout__

# Generated at 2022-06-22 12:39:36.587812
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:39:43.788792
# Unit test for function get_source
def test_get_source():
    def foo():
        print("Hello world!")

    def bar():
        print("Hello world!")
        print("Bye world!")

    def baz():
        def foo():
            print("Hello world!")

        return foo

    assert get_source(foo) == 'print("Hello world!")'
    assert get_source(baz()) == 'print("Hello world!")'
    assert get_source(bar) == '''\
print("Hello world!")
print("Bye world!")'''

# Generated at 2022-06-22 12:39:50.156830
# Unit test for function debug
def test_debug():
    from io import StringIO
    from unittest import TestCase, mock
    from . import settings

    settings.debug = True

    handler = StringIO()
    with mock.patch('sys.stderr', new=handler):
        debug(lambda: 'test')

    TestCase().assertEqual('[DEBUG] test\n', handler.getvalue())



# Generated at 2022-06-22 12:39:52.209379
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn).endswith('pass')

# Generated at 2022-06-22 12:39:55.083143
# Unit test for function debug
def test_debug():
    settings.debug = True

    debug(lambda: 'hello world')
    debug(lambda: 'hello world {0}'.format(1))

    settings.debug = False



# Generated at 2022-06-22 12:39:58.403722
# Unit test for function get_source
def test_get_source():
    def function(x: int, y: int) -> int:
        return x + y

    assert get_source(function) == \
        'def function(x, y):\n' \
        '    return x + y\n'

# Generated at 2022-06-22 12:40:01.215474
# Unit test for function get_source
def test_get_source():
    def foo():
        bar = 1
        return bar

    assert get_source(foo) == """bar = 1
return bar"""

# Generated at 2022-06-22 12:40:06.448796
# Unit test for function eager
def test_eager():
    # We need to import this way, because this file is the entry point of the
    # package and we have to avoid recursive imports
    from ..backwards import backwards

    class A:
        @backwards
        @eager
        def get_numbers(self) -> Iterable[int]:
            i = 0
            while i < 10:
                yield i
                i += 1

    assert A().get_numbers() == list(range(10))
    assert A.get_numbers() == list(range(10))
    assert A().get_numbers() == list(range(10))

# Generated at 2022-06-22 12:40:11.282351
# Unit test for function debug
def test_debug():
    messages.debug = lambda s: s.upper()
    messages.info = lambda s: s.lower()
    settings.debug = False
    debug(lambda: 'foo')
    settings.debug = True
    assert debug(lambda: 'foo') == 'FOO'
    settings.debug = False
test_debug()
del test_debug



# Generated at 2022-06-22 12:40:19.519278
# Unit test for function debug
def test_debug():
    from ..conf import set_settings, reset_settings
    import io
    import sys

    sio = io.StringIO()
    sys.stderr = sio
    set_settings(debug=False)
    debug(lambda: 'message')
    assert '' == sio.getvalue()
    reset_settings()
    set_settings(debug=True)
    debug(lambda: 'message')
    assert '\033[35m[DEBUG] message\033[0m\n' == sio.getvalue()
    reset_settings()



# Generated at 2022-06-22 12:40:23.737673
# Unit test for function eager
def test_eager():
    l = []

    @eager
    def foo() -> Iterable[int]:
        l.append(1)
        yield 2
        l.append(3)

    foo()
    assert l == [1, 3], 'eager decorator makes function execute eagerly'



# Generated at 2022-06-22 12:40:25.979972
# Unit test for function eager
def test_eager():
    @eager
    def generator() -> Iterable[int]:
        yield 1
        yield 2
    assert generator() == [1, 2]

# Generated at 2022-06-22 12:40:30.418444
# Unit test for function get_source
def test_get_source():
    def func():
        print('Hello, world!')

    assert get_source(func) == "print('Hello, world!')"

# Generated at 2022-06-22 12:40:33.300668
# Unit test for function eager
def test_eager():
    @eager
    def get_numbers() -> Iterable[int]:
        yield 10
        yield 20

    assert get_numbers() == [10, 20]

# Generated at 2022-06-22 12:40:43.858310
# Unit test for function debug
def test_debug():
    from io import StringIO
    from contextlib import redirect_stderr

    # Create a "file-like" object
    sio = StringIO()

    # Save the old stdout (sys.stdout)
    old_stdout = sys.stdout

    # Replace sys.stdout with our StringIO instance
    sys.stdout = sio

    with redirect_stderr(sio):
        debug(lambda : "debug")

    with redirect_stderr(sio):
        settings.debug = True
        debug(lambda : "debu")

    settings.debug = False

    # Get value stored in StringIO instance
    output = sio.getvalue()

    # We can now close the StringIO instance, as the
    # old sys.stdout will be restored.
    sys.stdout = old_stdout

   

# Generated at 2022-06-22 12:40:45.112007
# Unit test for function debug
def test_debug():
    debug_message = 'Debug message'
    debug(lambda: debug_message)

# Generated at 2022-06-22 12:40:47.879630
# Unit test for function get_source
def test_get_source():
    source = """    def bar():
        pass
    def foo(a,
             b):
        pass"""

# Generated at 2022-06-22 12:40:50.892038
# Unit test for function debug
def test_debug():
    settings.debug = False
    debug(lambda: 'hello world')
    settings.debug = True
    debug(lambda: 'hello world')
    settings.debug = False

# Generated at 2022-06-22 12:40:54.139066
# Unit test for function eager
def test_eager():
    @eager
    def test_fn(arg):
        for i in arg:
            yield i
    assert test_fn([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-22 12:40:56.097544
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass\n'



# Generated at 2022-06-22 12:40:57.169846
# Unit test for function debug
def test_debug():
    debug(lambda: 'test')



# Generated at 2022-06-22 12:41:04.788982
# Unit test for function debug
def test_debug():
    with patch('sys.stderr') as stderr_mock:
        debug(lambda: 'test message')
        stderr_mock.write.assert_not_called()

    with patch('sys.stderr') as stderr_mock:
        settings.debug = True
        debug(lambda: 'test message')
        stderr_mock.write.assert_called_once()
        stderr_mock.write.assert_called_with('\x1b[0;93mdebug: test message\x1b[0m\n')

    settings.debug = False

# Generated at 2022-06-22 12:41:08.565751
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    assert get_source(function) == 'pass'



# Generated at 2022-06-22 12:41:10.805810
# Unit test for function get_source
def test_get_source():
    def fn():
        pass
    assert get_source(fn) == 'def fn():\n    pass\n'

# Generated at 2022-06-22 12:41:12.331116
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    print(get_source(foo))

# Generated at 2022-06-22 12:41:17.330904
# Unit test for function get_source
def test_get_source():
    def fn1():
        pass

    assert get_source(fn1) == 'def fn1():\n    pass'

    def fn2():
        try:
            1
        finally:  # noqa: E722
            2

    assert get_source(fn2) == 'def fn2():\n    try:\n        1\n    finally:\n        2'



# Generated at 2022-06-22 12:41:20.722849
# Unit test for function eager
def test_eager():
    from ..utils import eager
    @eager
    def gen():
        yield 1
        yield 2

    assert gen() == [1, 2]

# Generated at 2022-06-22 12:41:21.962356
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass
    assert get_source(test_func) == 'def test_func():\n    pass'

# Generated at 2022-06-22 12:41:25.385815
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        for x in 'hello':
            yield x
    assert foo() == ['h', 'e', 'l', 'l', 'o']



# Generated at 2022-06-22 12:41:27.835007
# Unit test for function get_source
def test_get_source():
    def test(a, b, c=3, d=4):
        pass

    assert get_source(test) == 'def test(a, b, c=3, d=4):'

# Generated at 2022-06-22 12:41:39.267603
# Unit test for function debug
def test_debug():
    from tempfile import TemporaryFile
    from contextlib import contextmanager

    @contextmanager
    def captured_output():
        new_out, new_err = TemporaryFile(mode='w+'), TemporaryFile(mode='w+')
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    with captured_output() as (out, _):
        debug(lambda: '123')
        assert out.tell() != 0
        out.seek(0)
        assert out.read() == messages.debug('123') + '\n'


# Generated at 2022-06-22 12:41:40.767951
# Unit test for function get_source
def test_get_source():
    def source():
        pass

    assert get_source(source) == 'pass'

# Generated at 2022-06-22 12:41:48.840672
# Unit test for function get_source
def test_get_source():
    def decorator(fn):
        def wrapped():
            pass

        wrapped.__doc__ = fn.__doc__
        return wrapped

    @decorator
    def fn():
        """  This is documentation.

                Spaces should be stripped.
        """
    assert get_source(fn) == r'''def fn():
    """ This is documentation.
    
            Spaces should be stripped.
    """
'''

# Generated at 2022-06-22 12:41:50.177824
# Unit test for function get_source

# Generated at 2022-06-22 12:41:54.121854
# Unit test for function get_source
def test_get_source():
    def foo(arg1: Any) -> None:
        var = 1
        print(arg1)
        return var

    assert get_source(foo) == 'var = 1\n    print(arg1)\n    return var'

# Generated at 2022-06-22 12:42:00.506526
# Unit test for function eager
def test_eager():
    assert eager(lambda: 1)() == list(1)
    assert eager(lambda x: (x, 1))(2) == list((2, 1))
    assert eager(lambda x, y: (x, y, 1))(2, 3) == list((2, 3, 1))
    assert eager(lambda x, y, z: (x, y, z, 1))(2, 3, 4) == list((2, 3, 4, 1))



# Generated at 2022-06-22 12:42:02.621700
# Unit test for function eager
def test_eager():
    @eager
    def gen() -> Iterable[int]:
        yield 1
        yield 2

    assert gen() == [1, 2]

# Generated at 2022-06-22 12:42:03.916282
# Unit test for function eager
def test_eager():
    assert eager(range)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:42:06.706423
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:42:09.075084
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        yield 1
        yield 2
        yield 3

    assert foo() == [1, 2, 3]

# Generated at 2022-06-22 12:42:13.509558
# Unit test for function get_source
def test_get_source():
    def func():
        """Test function for get_source method.

        Args:
            arg (int): First argument.
            arg2 (str): Second argument.

        Returns:
            str: Return value.
        """
        a = 0
        b = 1
        c = 2
        return a + b + c


# Generated at 2022-06-22 12:42:21.937056
# Unit test for function debug
def test_debug():
    settings.debug = True
    warnings = []

    def get_debug_message():
        return 'some_debug_message'
    print(sys.stderr)
    sys.stderr.write = lambda message: warnings.append(message)
    debug(get_debug_message)
    assert warnings == [messages.debug(get_debug_message())]

    settings.debug = False
    debug(get_debug_message)
    assert warnings == [messages.debug(get_debug_message())]
    sys.stderr.write = sys.__stderr__.write
    settings.debug = True

# Generated at 2022-06-22 12:42:28.682067
# Unit test for function eager
def test_eager():
    def test_generator():
        yield 1
        yield 2
        yield 3

    assert eager(test_generator)() == [1, 2, 3]

# Generated at 2022-06-22 12:42:32.264708
# Unit test for function get_source
def test_get_source():
    def test_fn():
        return None

    fn_source = get_source(test_fn)

    assert fn_source == 'def test_fn():\n    return None', fn_source

# Generated at 2022-06-22 12:42:34.867082
# Unit test for function get_source
def test_get_source():
    def add(x: int, y: int) -> int:
        return x + y

    assert get_source(add) == 'return x + y'



# Generated at 2022-06-22 12:42:39.639362
# Unit test for function debug
def test_debug():
    debug_message = "foo"

    @debug
    def get_debug_message():
        return debug_message

    try:
        settings.debug = True
        get_debug_message()
        assert debug_message in sys.stderr.getvalue().strip()
    finally:
        settings.debug = False
        sys.stderr = sys.__stderr__



# Generated at 2022-06-22 12:42:43.706792
# Unit test for function debug
def test_debug():
    # Unsafe
    settings.debug = True
    debug(lambda: 'first')
    debug(lambda: 'second')
    settings.debug = False
    # Safe
    if settings.debug:
        print('first', file=sys.stderr)
        print('second', file=sys.stderr)



# Generated at 2022-06-22 12:42:48.447479
# Unit test for function eager
def test_eager():
    @eager
    def f(n: int) -> Iterable[int]:
        for i in range(n):
            yield i

    assert f(0) == []
    assert f(1) == [0]
    assert f(3) == [0, 1, 2]

# Generated at 2022-06-22 12:42:51.623394
# Unit test for function get_source
def test_get_source():
    def test(a, b):
        a += 1
        b = b / 2
        return a, b

    assert get_source(test) == 'a += 1\nb = b / 2\nreturn a, b'

# Generated at 2022-06-22 12:42:52.934070
# Unit test for function eager
def test_eager():
    assert eager(lambda: range(2))() == [0, 1]

# Generated at 2022-06-22 12:42:54.285428
# Unit test for function eager
def test_eager():
    assert eager(lambda x: ['Hello', x])('world') == ['Hello', 'world']

# Generated at 2022-06-22 12:42:57.882946
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(messages.test)
    settings.debug = False
    debug(messages.test)
    debug(messages.test)
    # restore default settings
    settings.debug = False

# Generated at 2022-06-22 12:43:13.331935
# Unit test for function get_source
def test_get_source():
    # TODO
    assert False

# Generated at 2022-06-22 12:43:19.063301
# Unit test for function get_source
def test_get_source():
    assert get_source(get_source) == '''def get_source(fn: Callable[..., Any]) -> str:
    """Returns source code of the function."""
    source_lines = getsource(fn).split('\\n')
    padding = len(re.findall(r'^(\\s*)', source_lines[0])[0])
    return '\\n'.join(line[padding:] for line in source_lines)
'''

# Generated at 2022-06-22 12:43:23.545251
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert (get_source(foo) == "def foo():\n    pass\n")
    def bar():
        pass

    class Baz:
        pass

    assert (get_source(bar) == "def bar():\n    pass\n")
    assert (get_source(Baz) == 'class Baz:\n    pass\n')

# Generated at 2022-06-22 12:43:25.343209
# Unit test for function get_source
def test_get_source():
    def _():
        pass

    assert get_source(_) == 'pass'



# Generated at 2022-06-22 12:43:29.738676
# Unit test for function debug
def test_debug():
    print('Testing debug()')

    print('\tWhen settings.debug is True')
    settings._debug = True
    debug(lambda : 'this should be printed')

    print('\tWhen settings.debug is False')
    settings._debug = False
    debug(lambda : 'this should not be printed')
    settings._debug = True # revert
    print('Done testing debug()')



# Generated at 2022-06-22 12:43:31.924951
# Unit test for function get_source
def test_get_source():
    global bar
    bar = lambda: print(1)
    expected_source = 'lambda: print(1)'

    assert get_source(bar) == expected_source

# Generated at 2022-06-22 12:43:41.446057
# Unit test for function debug
def test_debug():
    if sys.version_info.major < 3:
        return

    import io
    import unittest
    from contextlib import redirect_stderr

    class Test(unittest.TestCase):
        def setUp(self):
            self.stderr = io.StringIO()

        def tearDown(self):
            self.stderr.close()

        def test_debug_prints_message(self):
            with redirect_stderr(self.stderr):
                settings.debug = True
                debug(lambda: 'x')

            self.assertEqual(self.stderr.getvalue(), '\x1b[37mDEBUG: x\x1b[0m\n')


# Generated at 2022-06-22 12:43:46.478974
# Unit test for function debug
def test_debug():
    from unittest import mock

    with mock.patch('sys.stderr', new=mock.Mock()):
        settings.debug = True
        debug(lambda: 'message')
        sys.stderr.write.assert_called_once_with('\x1b[2mmessage\x1b[0m\n')
        settings.debug = False
        debug(lambda: 'message')
        sys.stderr.write.assert_called_once()

# Generated at 2022-06-22 12:43:49.043722
# Unit test for function debug
def test_debug():
    with pytest.warns(UserWarning):
        debug(lambda: 'message')
    settings.debug = True
    with pytest.raises(AssertionError):
        debug(lambda: 'message')

# Generated at 2022-06-22 12:43:52.946001
# Unit test for function eager
def test_eager():
    def gen() -> Generator[int, None, None]:
        yield 1
        yield 2

    assert eager(gen)() == [1, 2]

# Generated at 2022-06-22 12:44:20.735164
# Unit test for function get_source
def test_get_source():
    def func():
        return 1
    assert len(get_source(func)) > 0



# Generated at 2022-06-22 12:44:24.409451
# Unit test for function eager
def test_eager():
    def get_numbers(lst):
        for i in lst:
            yield i

    assert eager(get_numbers)([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-22 12:44:28.668487
# Unit test for function get_source
def test_get_source():
    def dummy():
        """Some docstring."""
        a = 1+2-3
        def dummy_a():
            b = 2 + 3 - 4
            return b
        return dummy_a()
    assert get_source(dummy) == inspect.getsource(dummy).strip()

# Generated at 2022-06-22 12:44:30.611028
# Unit test for function debug
def test_debug():

    settings.debug = False

    debug(lambda: 'this is debug message')

    settings.debug = True

    debug(lambda: 'this is debug message')

# Generated at 2022-06-22 12:44:33.518815
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'Test debug')
    debug(lambda: 'Test debug2')
    settings.debug = False
    debug(lambda: 'Test debug3')
    settings.debug = True
    debug(lambda: 'Test debug4')

# Generated at 2022-06-22 12:44:36.372017
# Unit test for function eager
def test_eager():
    def seq():
        for i in range(3):
            yield i
    seq = eager(seq)
    assert seq() == [0, 1, 2]

# Generated at 2022-06-22 12:44:38.920526
# Unit test for function debug
def test_debug():
    if settings.debug == False:
        settings.debug = True
        debug(lambda: 'Test message')
        settings.debug = False


# Generated at 2022-06-22 12:44:49.571447
# Unit test for function get_source

# Generated at 2022-06-22 12:44:52.050805
# Unit test for function get_source
def test_get_source():

    def test_fn():
        return ''

    assert get_source(test_fn) == 'return \'\'\n'



# Generated at 2022-06-22 12:44:54.234757
# Unit test for function get_source
def test_get_source():
    def func():
        pass

    assert get_source(func) == 'def func():\n    pass\n'

# Generated at 2022-06-22 12:45:21.886152
# Unit test for function debug
def test_debug():
    settings.debug = True
    message = "Test debug!"
    debug(lambda : message)



# Generated at 2022-06-22 12:45:25.919340
# Unit test for function get_source
def test_get_source():
    def outer_fn():
        def inner_fn():
            pass

    expected = []
    expected.append('def inner_fn():')
    expected.append('    pass')
    expected = '\n'.join(expected)
    actual = get_source(outer_fn.inner_fn)
    assert actual == expected

# Generated at 2022-06-22 12:45:29.595469
# Unit test for function debug
def test_debug():
    from io import StringIO
    import sys
    @debug
    def func():
        return "OK"
    sys.stderr = StringIO()
    func()
    assert "OK" in sys.stderr.getvalue()
    sys.stderr = sys.__stderr__



# Generated at 2022-06-22 12:45:30.970972
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'some message')


# Generated at 2022-06-22 12:45:35.809219
# Unit test for function get_source
def test_get_source():
    def test():
        get_source(test) # pragma: no cover
        print('Hello world')
        return 1

    assert get_source(test) == 'get_source(test)\nprint(\'Hello world\')\nreturn 1'

# Generated at 2022-06-22 12:45:39.224746
# Unit test for function get_source
def test_get_source():
    def a():
        b = 1

    # Tests if get_source returns the string as it is written in the definition,
    # and removes the indentation
    assert get_source(a) == 'def a():\n    b = 1'

# Generated at 2022-06-22 12:45:43.875945
# Unit test for function debug
def test_debug():
    if not settings.debug:
        settings.debug = True
        try:
            import io
            import sys
            fake_stderr = io.StringIO()
            sys.stderr = fake_stderr
            debug(lambda: 'Testing debug')
            assert "Testing debug" in fake_stderr.getvalue()
        finally:
            settings.debug = False
            fake_stderr.close()
            sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:45:54.153654
# Unit test for function get_source
def test_get_source():
    import ast
    import inspect
    from io import StringIO
    
    def test_function(a, b):
        return a + b
    test_function.__name__ = 'test_function'

    source = inspect.getsource(test_function)
    parsed = ast.parse(source)
    
    with StringIO() as out:
        ast.increment_lineno = True
        mod = ast.Module([parsed], type_ignores=[])
        ast.increment_lineno = False
        ast.fix_missing_locations(mod)
        code = compile(mod, filename='<ast>', mode='exec')
        exec(code, {'test_function': test_function})
        print(out.getvalue())
        
    #print('get_source: ' + get_source(test_function))

# Generated at 2022-06-22 12:45:56.170948
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        yield 1

    assert foo() == [1]

# Generated at 2022-06-22 12:46:01.263698
# Unit test for function eager
def test_eager():
    def gen(n):
        for i in range(n):
            yield i

    def test():
        yield from range(10)
        return None

    assert eager(gen)(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    with pytest.raises(TypeError):
        eager(test)()



# Generated at 2022-06-22 12:46:37.265485
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    if getsource(f) != get_source(f):
        raise Exception('Source code is incorrect')

    def g():
        def x():
            pass

        return 0

    if getsource(g).strip() != get_source(g):
        raise Exception('Source code is incorrect')



# Generated at 2022-06-22 12:46:40.358496
# Unit test for function eager
def test_eager():
    @eager
    def squares(iterable):
        for x in iterable:
            yield x * x

    assert squares(range(3)) == [0, 1, 4]

# Generated at 2022-06-22 12:46:45.617850
# Unit test for function get_source
def test_get_source():
    def my_function(a):
        pass

    def my_function2(a):
        return a

    def my_function3(a):
        return 3

    def test():
        assert get_source(my_function) == 'pass'
        assert get_source(my_function2) == 'return a'
        assert get_source(my_function3) == 'return 3'

    return test

# Generated at 2022-06-22 12:46:47.759122
# Unit test for function get_source
def test_get_source():
    def func():
        return 2 + 2

    assert get_source(func) == "return 2 + 2"



# Generated at 2022-06-22 12:46:49.905548
# Unit test for function eager
def test_eager():  # pragma: no cover
    import pytest
    from time import sleep

    @eager
    def f():
        yield 1
        sleep(1)
        yield 2

    assert f() == [1, 2]

# Generated at 2022-06-22 12:46:52.880122
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    source = get_source(function)
    assert source == 'def function():\n    pass'



# Generated at 2022-06-22 12:46:55.165504
# Unit test for function get_source
def test_get_source():
    def fn():
        pass
    source = get_source(fn)
    assert source == "def fn():\n    pass"

# Generated at 2022-06-22 12:46:57.212042
# Unit test for function get_source
def test_get_source():
    def test_function(a, b):
        def inner_function(c, d):
            pass


# Generated at 2022-06-22 12:47:04.558382
# Unit test for function debug
def test_debug():
    from unittest.mock import patch
    from io import StringIO
    from . import settings
    from . import messages
    from . import utils

    # Setting for test
    settings.debug = True
    message_debug = messages.debug('test')

    # Test case 1: function debug
    with patch('sys.stderr', new=StringIO()) as fake_stderr:
        utils.debug(lambda: 'test')
        assert fake_stderr.getvalue() == message_debug + '\n'

    # Test case 2: function debug with debug setting is False
    settings.debug = False
    with patch('sys.stderr', new=StringIO()) as fake_stderr:
        utils.debug(lambda: 'test')
        assert fake_stderr.getvalue() == ''



# Generated at 2022-06-22 12:47:08.860544
# Unit test for function debug
def test_debug():
    debug_message = 'Oh my!'
    with io.StringIO() as buf, contextlib.redirect_stderr(buf):
        settings.debug = True
        debug(lambda: debug_message)
        settings.debug = False
        debug(lambda: debug_message)
        got = buf.getvalue()
        assert messages.debug(debug_message) == got[:-1]

# Generated at 2022-06-22 12:48:10.744204
# Unit test for function get_source
def test_get_source():
    def test():
        return 1
    assert get_source(test) == 'return 1'

# Generated at 2022-06-22 12:48:14.005127
# Unit test for function get_source
def test_get_source():
    def fn():
        try:
            raise ValueError()
        except ValueError:
            return 'e'

    assert get_source(fn) == '''\
try:
    raise ValueError()
except ValueError:
    return 'e'''


# Generated at 2022-06-22 12:48:22.645468
# Unit test for function debug
def test_debug():
    """Test function ``debug``."""
    class Message:
        pass

    messages = Message()
    messages.debug = 'debug message'
    with patch.object(settings, 'debug', True):
        with patch('sys.stderr') as mock_stderr:
            debug(lambda: messages.debug)
            assert mock_stderr.write.called_with(
                messages.debug + '\n'
            )

    with patch.object(settings, 'debug', False):
        with patch('sys.stderr') as mock_stderr:
            debug(lambda: messages.debug)
            assert not mock_stderr.write.called

