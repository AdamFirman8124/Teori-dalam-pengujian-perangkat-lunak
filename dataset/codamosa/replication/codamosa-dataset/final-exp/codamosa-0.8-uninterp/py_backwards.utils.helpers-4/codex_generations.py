

# Generated at 2022-06-22 12:38:24.596589
# Unit test for function get_source

# Generated at 2022-06-22 12:38:32.720398
# Unit test for function get_source
def test_get_source():
    def dummy():
        pass

    assert get_source(dummy) == 'dummy()'
    def dummy(a):
        pass

    assert get_source(dummy) == 'dummy(a)'
    def dummy(a, b=1):
        pass

    assert get_source(dummy) == 'dummy(a, b=1)'
    def dummy(a, b=1, *args, **kwargs):
        pass

    assert get_source(dummy) == 'dummy(a, b=1, *args, **kwargs)'
    def dummy(a, b=1, *args, **kwargs):
        print('\n'.join(['', '', '', '']))


# Generated at 2022-06-22 12:38:34.309972
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass\n'



# Generated at 2022-06-22 12:38:36.661409
# Unit test for function get_source
def test_get_source():
    def test_fn(self):
        pass
    assert 'self):\n        pass' == get_source(test_fn)



# Generated at 2022-06-22 12:38:38.696288
# Unit test for function get_source
def test_get_source():
    @backwards
    def f():
        a = 1
        b = 2
    assert get_source(f) == '\n'.join(('def f():',
                                       '    a = 1',
                                       '    b = 2'))

# Generated at 2022-06-22 12:38:44.076733
# Unit test for function debug
def test_debug():
    debug_text = 'debug text'
    with io.StringIO() as f:
        sys.stderr = f
        debug(lambda: debug_text)
        sys.stderr = sys.__stderr__
        assert(f.getvalue() == messages.debug(debug_text) + '\n')



# Generated at 2022-06-22 12:38:52.635000
# Unit test for function debug
def test_debug():
    if settings.debug:
        def t_debug_function():
            # Call debug function with unique variable
            unique_variable = 0
            debug(lambda: unique_variable)

        # Check debug function is called
        with settings.debug:  # pylint: disable=no-member
            with mock.patch('sys.stderr') as t_mock_stderr:
                t_debug_function()
                self.assertEqual(t_mock_stderr.write.call_count, 2)
                self.assertEqual(t_mock_stderr.write.call_args[0], ('(debug) %s\n' % unique_variable,))

        # Check debug function is not called
        settings.debug = False

# Generated at 2022-06-22 12:38:55.837162
# Unit test for function eager
def test_eager():
    @eager
    def x() -> Iterable[int]:
        yield 1
        yield 2
        yield 3
    assert x() == [1, 2, 3]



# Generated at 2022-06-22 12:38:57.996531
# Unit test for function get_source
def test_get_source():
    def test():
        # Test function body
        print()

    # Test function header
    assert get_source(test) == 'print()'

# Generated at 2022-06-22 12:39:01.528212
# Unit test for function eager
def test_eager():
    @eager
    def mygen():
        for i in range(5):
            yield i

    assert list(mygen()) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:39:08.074482
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == 'def test_get_source():\n    assert get_source(test_get_source) == \'def test_get_source():\\n    assert get_source(test_get_source) == \\\'def test_get_source():\\\\n    assert get_source(test_get_source) == \\\'\\\'\\\'\\\'\''

# Generated at 2022-06-22 12:39:18.035553
# Unit test for function eager
def test_eager():
    from .. import generators
    from . import lib
    assert eager(generators.range)(10) == list(range(10))
    assert eager(generators.range)(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert eager(generators.range)(0) == [0]
    assert eager(generators.range)(-10) == list(range(-10))
    assert eager(generators.range)(-10) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    assert eager(generators.range)(0, 10) == list(range(0, 10))

# Generated at 2022-06-22 12:39:28.219966
# Unit test for function debug
def test_debug():
    from . import test
    from . import debug
    import io

    def test_fn():
        debug(lambda: "There is debug message!")

    with test.captured_output() as (out, err):
        test_fn()
    assert out.getvalue() == ""
    assert err.getvalue() == ""

    with io.StringIO() as fake_stderr:
        with test.captured_output(stderr=fake_stderr) as (out, err):
            test_fn()
        assert out.getvalue() == ""
        assert err.getvalue() == messages.debug("There is debug message!") + '\n'

    with test.captured_output() as (out, err):
        test_fn()
    assert out.getvalue() == ""

# Generated at 2022-06-22 12:39:33.662620
# Unit test for function debug
def test_debug():
    warnings = []
    def test_func(val):
        "Test function"
        debug(lambda: "Value received: {}".format(val))
        warnings.append('Warning message')

    warning = "Value received: 3"
    test_func(3)
    warnings = warnings[0].split('\n')[0]
    assert warnings == warning

# Generated at 2022-06-22 12:39:38.976693
# Unit test for function debug
def test_debug():
    call = 0
    def wrapper(get_message: Callable[[], str]) -> None:
        nonlocal call
        call += 1
    def get_message() -> str:
        return 'message'
    debug(get_message)
    debug(get_message)
    assert call == 0
    global settings
    settings.debug = True
    debug(get_message)
    debug(get_message)
    assert call == 2

# Generated at 2022-06-22 12:39:41.092334
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'Hello World!')
    finally:
        settings.debug = False


# Generated at 2022-06-22 12:39:47.985698
# Unit test for function debug
def test_debug():
    from io import StringIO

    class TestClass:
        def test_method(self):
            pass

    _module_name = TestClass.test_method.__module__
    assert _module_name is not None

    try:
        settings.debug = True
        out = StringIO()
        sys.stderr = out
        debug(lambda: 'TEST')
        assert out.getvalue().endswith('TEST\n')
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:50.073446
# Unit test for function eager
def test_eager():
    value = 1
    @eager
    def one():
        while True:
            yield value

    assert one() == [value]

# Generated at 2022-06-22 12:39:56.838874
# Unit test for function get_source
def test_get_source():
    def foo():
        '''
        Weirdly formatted docstring
        '''
        # Weirdly formatted
        # comment
        print('Hello world!')  # Another weirdly formatted comment

    assert get_source(foo) == '''\
        def foo():
            '''

# Generated at 2022-06-22 12:39:58.691466
# Unit test for function eager
def test_eager():
    @eager
    def echo(x: int) -> Iterable[int]:
        yield x

    assert echo(1) == [1]

# Generated at 2022-06-22 12:40:03.326952
# Unit test for function get_source
def test_get_source():
    def fn():
        pass
    assert get_source(fn) == 'pass'

# Generated at 2022-06-22 12:40:06.726090
# Unit test for function debug
def test_debug():
    settings.debug = True

    def get_message():
        return 'Some test message'

    debug(get_message)



# Generated at 2022-06-22 12:40:15.693357
# Unit test for function debug
def test_debug():
    message = 'hello!'
    with patch('sys.stderr', new=StringIO()) as fake_stderr, patch('py_backwards.utils.settings') as fake_settings:
        fake_settings.debug = True
        debug(lambda: message)
        assert fake_stderr.getvalue() == messages.debug(message)

        fake_stderr.seek(0)
        fake_stderr.truncate(0)
        fake_settings.debug = False
        debug(lambda: message)
        assert fake_stderr.getvalue() == ''

test_debug()

# Generated at 2022-06-22 12:40:18.986928
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'hello')
        debug(lambda: 'there')
        debug(lambda: 'printer')
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:40:22.323696
# Unit test for function debug
def test_debug():
    file = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    assert debug(lambda: 'Yay') is None
    sys.stderr = file



# Generated at 2022-06-22 12:40:25.934968
# Unit test for function debug
def test_debug():
    settings.debug = True

    message = 'foo'

    @debug
    def gen_message():
        assert 0  # should not be called
        return message

    gen_message()

    settings.debug = False

# Generated at 2022-06-22 12:40:30.645638
# Unit test for function debug
def test_debug():
    settings.debug = True
    msg = "debug message"
    try:
        debug(lambda: msg)
        assert False, "debug() should print the message"
    except AssertionError as e:
        pass
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:40:32.638383
# Unit test for function eager
def test_eager():
    assert eager(range)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:40:34.571237
# Unit test for function get_source
def test_get_source():
    def foo(a):
        return a
    assert get_source(foo) == 'return a'



# Generated at 2022-06-22 12:40:37.736419
# Unit test for function eager
def test_eager():
    def test_input() -> Iterable[int]:
        for i in range(1, 4):
            yield i

    assert eager(test_input)() == [1, 2, 3]



# Generated at 2022-06-22 12:40:45.358282
# Unit test for function get_source
def test_get_source():
    def test_function(a: int):
        def inner_function():
            return a
        return inner_function()
    assert get_source(test_function) == 'def test_function(a):\n    def inner_function():\n        return a\n    return inner_function()'

# Generated at 2022-06-22 12:40:53.981882
# Unit test for function debug
def test_debug():
    messages.debug = lambda s: s
    class FakeStdErr:
        def __init__(self):
            self.last_message = None

        def write(self, message: str) -> None:
            self.last_message = message
    fake_stderr = FakeStdErr()
    f = debug(lambda: 'Some message')
    settings.debug = False
    f()
    assert fake_stderr.last_message == None    
    settings.debug = True
    f()
    assert fake_stderr.last_message == 'Some message'



# Generated at 2022-06-22 12:41:00.680292
# Unit test for function debug
def test_debug():
    import io
    from contextlib import redirect_stderr
    stderr = io.StringIO()

    def get_message():
        return 'hello'

    debug(get_message)
    with redirect_stderr(stderr):
        debug(get_message)

    assert stderr.getvalue() == '\x1b[33m[DEBUG]\x1b[0m hello\n'



# Generated at 2022-06-22 12:41:03.535588
# Unit test for function debug

# Generated at 2022-06-22 12:41:11.734979
# Unit test for function get_source
def test_get_source():
    def simple_function():
        pass
    assert get_source(simple_function) == dedent(simple_function)

    def compound_function():
        def inner_function():
            pass
    assert get_source(compound_function) == dedent(compound_function)

    def indentation_function():
        pass
    assert get_source(indentation_function) == dedent(indentation_function)

    def super_indentation_function():
        x = 1
        y = 2
        z = 3
    assert get_source(super_indentation_function) == dedent(super_indentation_function)

# Generated at 2022-06-22 12:41:15.286583
# Unit test for function eager
def test_eager():
    @eager
    def f():
        yield 1
        yield 2

    assert f() == [1, 2]

# Generated at 2022-06-22 12:41:16.379721
# Unit test for function get_source
def test_get_source():
    def f():
        return 123
    assert get_source(f) == 'return 123'

# Generated at 2022-06-22 12:41:20.372666
# Unit test for function debug
def test_debug():
    from unittest import mock
    settings.debug = True
    debug(lambda: 'foo')
    settings.debug = False
    with mock.patch('sys.stderr') as mock_stderr:
        debug(lambda: 'foo')
    assert not mock_stderr.write.called

# Generated at 2022-06-22 12:41:22.570471
# Unit test for function debug
def test_debug():
    from .. import conf
    with settings.override(conf.debug, True):
        debug(lambda: 'One two')
        debug(str)

test_debug()

# Generated at 2022-06-22 12:41:24.128492
# Unit test for function get_source
def test_get_source():
    def foo():
        return 1

    assert get_source(foo) == 'return 1'

# Generated at 2022-06-22 12:41:33.547464
# Unit test for function eager
def test_eager():
    # pylint: disable=missing-docstring
    @eager
    def function_that_generates_ints() -> Iterable[int]:
        for i in range(5):
            yield i
    assert function_that_generates_ints() == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:41:35.440068
# Unit test for function eager
def test_eager():
    def generator():
        n = 1
        while n <= 5:
            yield n
            n += 1

    assert eager(generator)() == [1, 2, 3, 4, 5]

# Generated at 2022-06-22 12:41:37.998432
# Unit test for function get_source
def test_get_source():
    def sum(a, b):
        return a + b
    sum_source = ('def sum(a, b):\n'
                  '    return a + b')
    assert get_source(sum) == sum_source

# Generated at 2022-06-22 12:41:40.633237
# Unit test for function eager
def test_eager():
    from functools import partial

    g = eager(partial(range, 10))
    assert g() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-22 12:41:43.540266
# Unit test for function get_source
def test_get_source():
    def test():
        pass

    assert get_source(test) == 'pass'



# Generated at 2022-06-22 12:41:46.218209
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'def test_function():\n    pass\n'

# Generated at 2022-06-22 12:41:48.103632
# Unit test for function get_source
def test_get_source():
    def func():
        pass

    print(get_source(func))

# Generated at 2022-06-22 12:41:55.858427
# Unit test for function debug
def test_debug():
    debug_message = None
    def get_message():
        global debug_message
        return "Debug message"
    mock_sys = Mock()

    def sys_stderr_writer(message):
        global debug_message
        debug_message = message

    mock_sys.stderr.write = sys_stderr_writer
    with patch('sys', mock_sys):
        settings.debug = True
        debug(get_message)
        assert debug_message is not None and debug_message == "Debug message"
        settings.debug = False


# Generated at 2022-06-22 12:42:03.288740
# Unit test for function get_source
def test_get_source():

    def foo1(my_argument=1, my_argument2=2, my_argument3=3):
        pass

    def foo2():
        pass

    def foo3(
        my_argument=1, my_argument2=2, my_argument3=3, *args, **kwargs
    ):
        pass

    def foo4(**kwargs):
        pass

    def foo5():
        def foo_in_foo():
            pass

    for foo in [foo1, foo2, foo3, foo4, foo5]:
        assert(get_source(foo))

# Generated at 2022-06-22 12:42:07.268228
# Unit test for function get_source
def test_get_source():
    def example():
        if 1:
            print('test')

    assert get_source(example) == """
if 1:
    print('test')
""".strip()


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:42:20.872545
# Unit test for function eager
def test_eager():
    def mock(a, b, c=3):
        yield a
        yield b
        yield c
        yield c + 1
        yield c + 2

    assert eager(mock)(1, b=2) == [1, 2, 3, 4, 5]
    assert eager(mock)(1, 2, 3) == [1, 2, 3, 4, 5]
    assert eager(mock)(1, 3) == [1, 3, 3, 4, 5]
    assert eager(mock)(1, b=3) == [1, 3, 3, 4, 5]

# Generated at 2022-06-22 12:42:23.904836
# Unit test for function get_source
def test_get_source():
    def get(msg):
        pass
    # assert
    source = get_source(get).split('\n')
    assert source[0].startswith('def get(msg):')
    assert source[1].startswith('    pass')

# Generated at 2022-06-22 12:42:26.342932
# Unit test for function eager
def test_eager():
    a = eager(x for x in range(10))
    b = list(range(10))
    assert a() == b

# Generated at 2022-06-22 12:42:28.539897
# Unit test for function get_source
def test_get_source():
    def foo(a, b, c, d=None, *args, e=1, f=2, g=3, **kwargs):
        pass
    assert get_source(foo) == 'def foo(a, b, c, d=None, *args, e=1, f=2, g=3, **kwargs):\n    pass'

# Generated at 2022-06-22 12:42:31.700073
# Unit test for function get_source
def test_get_source():
    def func_to_test():
        return 1
    assert get_source(func_to_test) == 'return 1'


# Generated at 2022-06-22 12:42:33.621307
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        yield 1
        yield 2

    assert foo() == [1, 2]

# Generated at 2022-06-22 12:42:36.515715
# Unit test for function eager
def test_eager():
    @eager
    def add(x: int, y: int) -> Iterable[int]:
        yield x + y

    assert add(1, 2) == [3]



# Generated at 2022-06-22 12:42:45.134857
# Unit test for function debug
def test_debug():
    msg_text = 'message text'

    def get_message() -> str:
        return msg_text

    def assert_message_was_not_printed():
        assert sys.stderr.read() == b''

    def assert_message_was_printed():
        assert sys.stderr.read().decode() == messages.debug(msg_text) + '\n'

    sys.stderr.seek(0)
    sys.stderr.truncate()

    settings.debug = False
    debug(get_message)
    assert_message_was_not_printed()

    settings.debug = True
    debug(get_message)
    assert_message_was_printed()



# Generated at 2022-06-22 12:42:48.585664
# Unit test for function eager
def test_eager():
    l = [1, 2, 3]
    assert eager(lambda x: x)(l) == l
    assert eager(lambda x: x)(l) is not l

# Generated at 2022-06-22 12:42:51.000533
# Unit test for function debug
def test_debug():
    settings.debug = True
    messages.debug('ABC: {}', 'DEF')
    settings.debug = False
    messages.debug('ABC: {}', 'DEF')

# Generated at 2022-06-22 12:43:08.254929
# Unit test for function debug
def test_debug():
    import io
    import sys

    stream = io.StringIO()
    sys.stderr = stream

    settings.debug = False
    debug(lambda: 'test')
    assert(stream.getvalue() == '')

    settings.debug = True
    debug(lambda: 'test')
    assert(stream.getvalue() == messages.debug('test\n'))

# Generated at 2022-06-22 12:43:18.695250
# Unit test for function eager
def test_eager():
    data = {'list': [0, 1, 2], 'tuple': (0, 1, 2), 'generator': (x for x in [0, 1, 2])}
    @eager
    def test(obj: Any) -> Any:
        return data[obj]

    for _, values in data.items():
        assert test(_) == values

    data = {'set': {0, 1, 2}, 'dict': {'zero': 0, 'one': 1, 'two': 2}}
    @eager
    def test2(obj: Any) -> Any:
        return data[obj]

    for _, values in data.items():
        assert test2(_) == list(values)



# Generated at 2022-06-22 12:43:22.611498
# Unit test for function get_source
def test_get_source():
    def foo():
        print('Hello world!')

    def bar():
        print('Hello world!')
        print('Hello world!')
    assert get_source(foo) == "print('Hello world!')"
    assert get_source(bar) == "print('Hello world!')\nprint('Hello world!')"

# Generated at 2022-06-22 12:43:32.591833
# Unit test for function get_source
def test_get_source():
    import inspect
    import re

    def f():
        """
        This is a function
        I'm going to write some words
        """
        pass

    source = inspect.getsource(f)
    source_lines = source.split('\n')
    padding = len(re.findall(r'^(\s*)', source_lines[0])[0])

    assert source_lines == [
        '    def f():',
        '        """',
        '        This is a function',
        '        I\'m going to write some words',
        '        """',
        '        pass',
        ''
    ]


# Generated at 2022-06-22 12:43:42.153436
# Unit test for function debug
def test_debug():
    from unittest.mock import patch
    from io import StringIO
    from .. import conf
    from . import common

    orig_debug = conf.debug


# Generated at 2022-06-22 12:43:46.981928
# Unit test for function get_source
def test_get_source():
    source_lines = getsource(test_get_source).split('\n')
    padding = len(re.findall(r'^(\s*)', source_lines[0])[0])
    expected = '\n'.join(line[padding:] for line in source_lines)
    assert expected == get_source(test_get_source)

# Generated at 2022-06-22 12:43:48.998588
# Unit test for function debug
def test_debug():
    fn = mock.Mock(spec=Callable)
    debug(fn)
    fn.assert_called_once_with()



# Generated at 2022-06-22 12:43:50.713482
# Unit test for function debug
def test_debug():
    debug(lambda: 'test message')

# Generated at 2022-06-22 12:43:58.072293
# Unit test for function debug
def test_debug():
    from io import StringIO
    from contextlib import redirect_stderr

    stderr = StringIO()
    with redirect_stderr(stderr):
        debug(lambda: 'a')
        debug(lambda: 'b')

    assert stderr.getvalue() == ''

    settings.debug = True
    stderr = StringIO()
    with redirect_stderr(stderr):
        debug(lambda: 'a')
        debug(lambda: 'b')

    assert stderr.getvalue() == messages.debug('a') + '\n' + messages.debug('b') + '\n'
    settings.debug = False

# Generated at 2022-06-22 12:44:01.501333
# Unit test for function eager
def test_eager():
    def f():
        yield 'a'
        yield 'b'
        yield 'c'
    assert eager(f)() == ['a', 'b', 'c']

# Generated at 2022-06-22 12:44:29.926430
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == """
    assert get_source(test_get_source) == """

# Generated at 2022-06-22 12:44:34.350825
# Unit test for function get_source
def test_get_source():
    def sum_numbers(a, b):
        return a + b

    if sys.version_info.major == 2:
        expected = """def sum_numbers(a, b):
    return a + b"""
    else:
        expected = """def sum_numbers(a, b):
    return a + b""".replace(' ', '')

    assert get_source(sum_numbers) == expected, "Source code is not being returned correctly"



# Generated at 2022-06-22 12:44:38.005645
# Unit test for function get_source
def test_get_source():

    def f():
        pass

    def g(a, b, c=5, *args, **kwargs):
        pass

    assert get_source(f) == 'def f():\n    pass'
    assert get_source(g) == 'def g(a, b, c=5, *args, **kwargs):\n    pass'

# Generated at 2022-06-22 12:44:39.836921
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)
    assert 'def test_get_source():' in source


# Generated at 2022-06-22 12:44:46.085238
# Unit test for function get_source
def test_get_source():
    def test() -> None:
        """Function to test get_source function.

        Doctest:
        >>> test()
        """

    assert get_source(test) == 'def test():\n    """Function to test get_source function.\n\n    Doctest:\n    >>> test()\n    """\n'



# Generated at 2022-06-22 12:44:47.853287
# Unit test for function debug
def test_debug():
    with CaptureStdout() as capture:
        debug(lambda: 'Hello')
    assert capture.stdout == 'DEBUG: Hello\n'



# Generated at 2022-06-22 12:44:49.625668
# Unit test for function debug
def test_debug():
    with settings.debug(True):
        debug(lambda: 'message')

    with settings.debug(False):
        debug(lambda: 'message')

# Generated at 2022-06-22 12:44:53.375192
# Unit test for function get_source
def test_get_source():
    def f(): pass
    assert get_source(f) == 'def f(): pass'

    def g(x: int) -> bool:
        return x > 0
    assert get_source(g) == 'def g(x: int) -> bool:\n    return x > 0'

# Generated at 2022-06-22 12:44:56.109331
# Unit test for function get_source
def test_get_source():
    def my_func():
        def inner_func():
            x = 1
            print(x)

        x = 2
        print(x)


# Generated at 2022-06-22 12:44:59.890087
# Unit test for function eager
def test_eager():
    from .magic import magic

    @magic
    @eager
    def g(n: int) -> Iterable[int]:
        for i in range(n):
            yield i ** i

    assert g(4) == [0, 1, 4, 27]

# Generated at 2022-06-22 12:45:29.287756
# Unit test for function debug
def test_debug():
    # settings.debug = True
    debug(lambda: 'message')

# Generated at 2022-06-22 12:45:40.563921
# Unit test for function debug
def test_debug():
    debug_messages = []
    def test_debug_fn_1(*args, **kwargs):
        debug_messages.append((args, kwargs))
    def test_debug_fn_2():
        debug_messages.append("debug me")
    settings.debug = True
    debug(test_debug_fn_1)
    assert len(debug_messages) == 0
    debug(test_debug_fn_1)
    assert len(debug_messages) == 1
    assert len(debug_messages[0]) == 0
    debug(test_debug_fn_1, 1, 2, three=3, four=4)
    assert len(debug_messages) == 2
    assert len(debug_messages[1]) == 2
    args, kwargs = debug_messages[1]

# Generated at 2022-06-22 12:45:48.431260
# Unit test for function get_source
def test_get_source():

    def function(): pass

    def function_with_args(a, b=None, *args, **kwargs): pass

    def function_with_comment():
        # This is a comment
        pass

    def function_with_docstring():
        """
        This is a docstring
        """
        pass

    def function_with_decorator(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            fn(*args, **kwargs)
        return inner

    def function_with_decorator_and_comment(fn):
        # This is a comment
        @wraps(fn)
        def inner(*args, **kwargs):
            fn(*args, **kwargs)
        return inner


# Generated at 2022-06-22 12:45:53.003697
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'foo_debug')
        with patch('sys.stderr', new_callable=StringIO) as stderr:
            debug(lambda: 'debug')
            assert 'Warning: Debug mode is on!\n' in stderr.getvalue()
    finally:
        settings.debug = False



# Generated at 2022-06-22 12:45:58.376466
# Unit test for function debug
def test_debug():
    """
    >>> import sys

    >>> print = lambda *args, **kwargs: sys.stdout.write(*args) #type: ignore
    >>> settings.debug = True
    >>> debug(lambda: 'foo')
    ⚠️  foo
    >>> settings.debug = False
    >>> debug(lambda: 'foo')
    """



# Generated at 2022-06-22 12:46:02.192000
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)
    assert source.startswith('source = get_source(test_get_source)')
    assert source.endswith('assert source.endswith(\'test_get_source()\')')

# Generated at 2022-06-22 12:46:03.331372
# Unit test for function eager
def test_eager():
    assert eager(lambda: 1)(2) == [1]

# Generated at 2022-06-22 12:46:06.984647
# Unit test for function debug
def test_debug():
    called = False

    def get_message() -> str:
        nonlocal called
        called = True
        return 'test message'

    debug(get_message)
    assert not called

    settings.debug = True
    debug(get_message)
    assert called

# Generated at 2022-06-22 12:46:12.673781
# Unit test for function get_source
def test_get_source():
    def test_function(a, b, *args):
        pass

    res = get_source(test_function)
    assert res == (
        'def test_function(a, b, *args):\n'
        '    pass'
    )


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-22 12:46:16.381733
# Unit test for function get_source
def test_get_source():
    def foo_bar_baz():
        def nested_foo_bar_baz():
            if True:
                return True


    assert ('def nested_foo_bar_baz():\n'
            "    if True:\n"
            '        return True\n') == get_source(foo_bar_baz.nested_foo_bar_baz)

# Generated at 2022-06-22 12:46:51.509999
# Unit test for function get_source
def test_get_source():
    @backwards
    def foo(a, b, c, d=4, e=5, f=6):
        pass

    foo_source = inspect.getsource(foo)
    backwards_source = inspect.getsource(backwards)
    assert(foo_source != backwards_source)

# Generated at 2022-06-22 12:46:55.992979
# Unit test for function debug
def test_debug():
    import builtins
    messages.debug = lambda x: 'debug: ' + x

    builtins.print = lambda *x: None

    settings.debug = False
    debug(lambda: 'hello')

    settings.debug = True
    debug(lambda: 'world')

    builtins.print = print

# Generated at 2022-06-22 12:46:57.681199
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'pass'

# Generated at 2022-06-22 12:47:02.807534
# Unit test for function debug
def test_debug():
    print_mock = mock.Mock()
    with mock.patch('backwards.utils.messages.debug', return_value='<MESSAGE>') as debug_mock, \
            mock.patch('backwards.utils.sys.stderr', print_mock):
        debug(lambda: '<MESSAGE>')

    debug_mock.assert_called_once_with('<MESSAGE>')
    print_mock.assert_called_once_with('<MESSAGE>')

# Generated at 2022-06-22 12:47:11.178563
# Unit test for function get_source
def test_get_source():
    from functools import partial
    def nested(a, b):
        def nested(x):
            pass
        def nested2(y):
            pass
        pass

    def nested2(a, b):
        pass

    def outer():
        pass

    assert get_source(partial(nested, 1, 2)) == """
        def nested(x):
            pass
        def nested2(y):
            pass
        pass
    """.strip()

    assert get_source(partial(nested2, 1, 2)) == """
        pass
    """.strip()

    assert get_source(outer) == """
        pass
    """.strip()

# Generated at 2022-06-22 12:47:14.885631
# Unit test for function get_source
def test_get_source():
    def fn() -> None:
        pass

    assert get_source(fn) == 'def fn() -> None:\n    pass'

# Generated at 2022-06-22 12:47:17.502952
# Unit test for function eager
def test_eager():
    values = range(10)

    @eager
    def test_function():
        for value in values:
            yield value
    assert test_function() == list(values)

# Generated at 2022-06-22 12:47:19.646570
# Unit test for function eager
def test_eager():
    @eager
    def foo() -> Iterable[int]:
        yield 1
        yield 2

    assert foo() == [1, 2]

# Generated at 2022-06-22 12:47:22.728385
# Unit test for function get_source
def test_get_source():  # type: ignore
    def foo():  # type: ignore
        pass
    assert get_source(foo) == 'pass'
    assert get_source(lambda x: x).startswith('lambda')
    assert get_source(lambda: None).startswith('lambda')

# Generated at 2022-06-22 12:47:28.519292
# Unit test for function get_source
def test_get_source():
    def func():
        """
        Some foo.

        .. code-block:: python

            some line 1
            another line
            yet another line
        """
        pass

    assert (
        get_source(func)
        == '"""\nSome foo.\n\n.. code-block:: python\n\n    some line 1\n    another line\n    yet another line\n"""'
    )


if __name__ == '__main__':
    test_get_source()