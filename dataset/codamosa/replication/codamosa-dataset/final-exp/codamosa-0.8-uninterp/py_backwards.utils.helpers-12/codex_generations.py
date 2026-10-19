

# Generated at 2022-06-22 12:38:24.352063
# Unit test for function get_source
def test_get_source():
    def f1():
        pass

    def f2():
        def f3():
            pass

    assert get_source(f1) == 'pass'
    assert get_source(f2) == 'pass'

# Generated at 2022-06-22 12:38:33.135837
# Unit test for function eager
def test_eager():
    import pytest
    from .. import steps
    from . import TEST_VECTOR

    @steps
    @eager
    def gen1(x: int, y: int) -> Iterable[str]:
        for i in range(x, y):
            yield str(i)
        return

    @steps
    def gen2(x: int, y: int) -> Iterable[str]:
        for i in range(x, y):
            yield str(i)
        return

    assert list(gen1(*TEST_VECTOR)) == list(gen2(*TEST_VECTOR))



# Generated at 2022-06-22 12:38:36.896881
# Unit test for function debug
def test_debug():
    from io import StringIO
    from sys import stderr
    stderr = stderr

    def get_message():
        return 'bla'*10

    # Without debug
    with StringIO() as stderr, StringIO() as stdout, settings.override_all():
        debug(get_message)
        assert stderr.getvalue() == ''
        assert stdout.getvalue() == ''

    # With debug
    with StringIO() as stderr, StringIO() as stdout, settings.override_all({'debug': True}):
        debug(get_message)
        assert stderr.getvalue() != ''
        assert stdout.getvalue() == ''

# Generated at 2022-06-22 12:38:37.918793
# Unit test for function get_source

# Generated at 2022-06-22 12:38:45.575299
# Unit test for function get_source

# Generated at 2022-06-22 12:38:46.641639
# Unit test for function get_source
def test_get_source():
    def f():
        return 42

    assert get_source(f) == 'return 42'

# Generated at 2022-06-22 12:38:48.990395
# Unit test for function eager
def test_eager():
    source = """def x():
    yield 1
    yield 2"""

    assert eager(x)() == [1, 2]

# Generated at 2022-06-22 12:38:50.370256
# Unit test for function eager
def test_eager():
    assert eager(lambda: (x for x in range(3)))() == [0, 1, 2]

# Generated at 2022-06-22 12:38:56.112964
# Unit test for function get_source
def test_get_source():
    assert get_source(get_source) == 'def get_source(fn: Callable[..., Any]) -> str:\n    source_lines = getsource(fn).split(\'\\n\')\n    padding = len(re.findall(r\'^(\\s*)\', source_lines[0])[0])\n    return \'\\n\'.join(line[padding:] for line in source_lines)'



# Generated at 2022-06-22 12:38:58.758669
# Unit test for function eager
def test_eager():
    nums = [1, 2, 3]
    lst = [nums[i] for i in range(len(nums))]
    assert lst == [1, 2, 3]

# Generated at 2022-06-22 12:39:05.570693
# Unit test for function debug
def test_debug():
    import io
    from contextlib import redirect_stdout

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        debug(lambda: 'foo')
    assert 'foo' in buffer.getvalue()
    assert messages.debug('foo') in buffer.getvalue()



# Generated at 2022-06-22 12:39:10.178827
# Unit test for function debug
def test_debug():
    import mock
    from .. import conf
    settings.debug = True

    mock_get_message = mock.Mock(return_value='test_message')
    with mock.patch('sys.stderr') as mock_stderr:
        debug(mock_get_message)
    mock_stderr.write.assert_called_with(messages.DEBUG_PREFIX + 'test_message\n')

    # Restore default settings
    settings.debug = conf.DEBUG

# Generated at 2022-06-22 12:39:17.086672
# Unit test for function get_source

# Generated at 2022-06-22 12:39:21.416340
# Unit test for function get_source
def test_get_source():
    def func():
        a = 1
        return 0

    assert get_source(func) == 'a = 1\nreturn 0'

    def func_with_docstring():
        """some docstring"""
        return 0

    assert get_source(func_with_docstring) == 'return 0'

# Generated at 2022-06-22 12:39:30.991882
# Unit test for function debug
def test_debug():
    class TestClass:
        def __init__(self):
            self.i = 0

        def get_message(self) -> str:
            self.i += 1
            return "msg {}".format(self.i)

    def test_with_settings(output: List[str], settings_) -> None:
        settings.update_from_dict(settings_)
        try:
            debug(test_class.get_message)
            assert len(output) == 1

            debug(test_class.get_message)
            assert len(output) == 1

            settings.debug = True
            debug(test_class.get_message)
            assert len(output) == 2

            debug(test_class.get_message)
            assert len(output) == 3
        finally:
            settings.reset()

    test_with_settings

# Generated at 2022-06-22 12:39:41.563982
# Unit test for function debug
def test_debug():
    print('Tests for function debug...')
    import io
    from contextlib import redirect_stderr
    def test(debug_enabled: bool) -> None:
        # set debug to debug_enabled
        settings.debug = debug_enabled
        # make a buffer to store stderr
        buffer = io.StringIO()
        # redirect stderr to buffer
        with redirect_stderr(buffer):
            # run debug
            debug(lambda: 'hello world')
        # get stderr
        content = buffer.getvalue()
        # clean buffer
        buffer.close()
        # assert result
        assert 'py_backwards debug: hello world' in content
    # run test
    test(True)
    test(False)
    print('Test passed.')


if __name__ == '__main__':
    test

# Generated at 2022-06-22 12:39:44.841459
# Unit test for function debug
def test_debug():
    from .. import save
    with save(settings, debug=False):
        debug(lambda: 'hi')
    with save(settings, debug=True):
        debug(lambda: 'hi')
    assert settings.debug

# Generated at 2022-06-22 12:39:46.872266
# Unit test for function eager
def test_eager():
    assert eager(lambda: range(5))() == list(range(5))

# Generated at 2022-06-22 12:39:49.950950
# Unit test for function eager
def test_eager():
    def gen_10():
        for i in range(10):
            yield i

    assert eager(gen_10)() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-22 12:39:52.106475
# Unit test for function get_source
def test_get_source():
    def function():
        return 1
    assert get_source(function) == 'return 1'

# Generated at 2022-06-22 12:39:58.249643
# Unit test for function debug
def test_debug():
    debug(lambda : 'lol')
    settings.debug = True
    debug(lambda : 'kek')

# Generated at 2022-06-22 12:40:01.958064
# Unit test for function debug
def test_debug():
    assert settings.debug is True

    calls = []

    def get_message():
        calls.append(True)
        return 'get_message'

    debug(get_message)
    assert calls == [True]



# Generated at 2022-06-22 12:40:03.067807
# Unit test for function get_source
def test_get_source():
    def test():
        return 0
    assert get_source(test) == 'return 0'

# Generated at 2022-06-22 12:40:07.649165
# Unit test for function get_source
def test_get_source():
    from .test import test_function_1
    source = get_source(test_function_1)
    assert source == '\n'.join([
        'def test_function_1():',
        '    return 2',
    ])

# Generated at 2022-06-22 12:40:16.000867
# Unit test for function debug
def test_debug():
    settings.debug = True

    try:
        with patch('sys.stderr', new_callable=StringIO) as fake_stderr:
            debug(lambda: 'foo')
            assert fake_stderr.getvalue() == messages.debug('foo') + '\n'

        with patch('sys.stderr', new_callable=StringIO) as fake_stderr:
            settings.debug = False
            debug(lambda: 'bar')
            assert fake_stderr.getvalue() == ''
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:40:21.136145
# Unit test for function eager
def test_eager():
    try:
        from unittest import mock
    except ImportError:
        import mock

    @eager
    def foo(yield_value):
        yield yield_value

    with mock.patch('builtins.list', new=mock.Mock(side_effect=list)):
        assert foo(1) == [1]
        assert list.call_args == mock.call(foo(1))

# Generated at 2022-06-22 12:40:26.088655
# Unit test for function debug
def test_debug():
    message = 'testing'
    capturer = Capturer()
    with capturer:
        debug(lambda: message)
    assert message in capturer.get()
    settings.debug = False
    with capturer:
        debug(lambda: message)
    assert message not in capturer.get()
    settings.debug = True


# Generated at 2022-06-22 12:40:28.366015
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'pass'



# Generated at 2022-06-22 12:40:30.479932
# Unit test for function eager
def test_eager():
    @eager
    def f():
        for i in range(4):
            yield i

    assert f() == [0, 1, 2, 3]



# Generated at 2022-06-22 12:40:31.986529
# Unit test for function eager
def test_eager():
    assert eager([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-22 12:40:40.588085
# Unit test for function eager
def test_eager():
    def my_gen(n: int) -> Iterable[int]:
        for i in range(n):
            yield i

    my_list = eager(my_gen)(10)

    assert type(my_list) == list
    assert list(range(10)) == my_list

# Generated at 2022-06-22 12:40:42.946862
# Unit test for function eager
def test_eager():
    assert eager(lambda: range(10))() == list(range(10))


if __name__ == '__main__':
    test_eager()

# Generated at 2022-06-22 12:40:47.374439
# Unit test for function debug
def test_debug():
    result = []
    def get_message():
        result.append(settings.debug)
        return 'Debug message'

    settings.debug = False
    debug(get_message)
    assert not result
    settings.debug = True
    debug(get_message)
    assert result

# Generated at 2022-06-22 12:40:57.791145
# Unit test for function get_source
def test_get_source():
    def some(a: int, b: int) -> int:
        """
        Documentation string.
        Returns sum of arguments.
        """
        return a + b

    def empty_doc_string():
        """ """
        return 3

    def no_doc_string():
        return 5

    def indented(a: int, b: int) -> int:
        c = a * b
        return c

    def decorator_with_args(argument: str):
        def inner(fn):
            pass

        return inner

    def decorator_without_args(fn):
        def inner():
            pass

        return inner

    def decorator_with_kwargs(argument: str):
        def inner(fn):
            pass

        return inner


# Generated at 2022-06-22 12:41:01.573471
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'test')
        assert sys.stderr.getvalue().strip() == messages.debug('test')
    finally:
        sys.stderr.truncate(0)
        settings.debug = False

# Generated at 2022-06-22 12:41:04.743899
# Unit test for function eager
def test_eager():
    @eager
    def double(iterable):
        for item in iterable:
            yield item * 2

    # Assert that the type of result is list
    assert isinstance(double([1, 2, 3]), list)


# Generated at 2022-06-22 12:41:07.418899
# Unit test for function eager
def test_eager():
    @eager
    def some_eager(argument):
        yield 2 + argument
        yield 4 + argument

    assert some_eager(10) == [12, 14]


# Generated at 2022-06-22 12:41:11.116972
# Unit test for function get_source
def test_get_source():
    @wraps(get_source)
    def clear_get_source():
        pass

    get_source_source = get_source(get_source)

    assert get_source_source.strip() == clear_get_source.__doc__.strip()

# Generated at 2022-06-22 12:41:14.255457
# Unit test for function get_source
def test_get_source():
    def my_function(a, b):
        c = 5
        d = 6
        return 7

    assert get_source(my_function) == 'c = 5\nd = 6\nreturn 7'

# Generated at 2022-06-22 12:41:16.470033
# Unit test for function get_source
def test_get_source():
    def f():
        return 'some value'

    assert get_source(f) == """    return 'some value'""".strip()

# Generated at 2022-06-22 12:41:22.022397
# Unit test for function get_source

# Generated at 2022-06-22 12:41:24.212502
# Unit test for function debug
def test_debug():
    debug_message = "test message"
    assert debug(lambda: debug_message) == None



# Generated at 2022-06-22 12:41:27.787787
# Unit test for function get_source
def test_get_source():
    def test_function(a: int, b: int) -> int:
        x = a + b
        c = 3*x

        # Comment
        return c + 1

    source = get_source(test_function)

# Generated at 2022-06-22 12:41:29.978848
# Unit test for function eager
def test_eager():
    import pytest

    def gen():
        yield 1
        yield 2

    assert eager(gen)() == [1, 2]

# Generated at 2022-06-22 12:41:32.416169
# Unit test for function get_source
def test_get_source():
    def foo():
        for i in range(10):
            print(i)

    assert get_source(foo) == 'for i in range(10):\n    print(i)\n'

# Generated at 2022-06-22 12:41:35.546460
# Unit test for function get_source
def test_get_source():
    def original_function():
        """
        This function is
        multiline
        """
        return 1


# Generated at 2022-06-22 12:41:38.344840
# Unit test for function get_source
def test_get_source():
    def foo(a=None, b=True, c=False):
        bar = 1
        if bar:  # some line
            return True
        return False


# Generated at 2022-06-22 12:41:42.128571
# Unit test for function debug
def test_debug():
    from contextlib import redirect_stderr
    from io import StringIO
    debug_output = StringIO()
    with redirect_stderr(debug_output):
        debug(lambda: 'Test')
    assert 'Test' in debug_output.getvalue()


# Generated at 2022-06-22 12:41:46.870829
# Unit test for function get_source
def test_get_source():
    def inner_function(arg) -> int:
        return arg

    def outer_function() -> None:
        for i in range(10):
            assert inner_function(i) == i

    assert get_source(outer_function) == 'for i in range(10):\n    assert inner_function(i) == i'

# Generated at 2022-06-22 12:41:51.121215
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'Hello World!')
        print(sys.stderr.getvalue())
        assert sys.stderr.getvalue() == '\x1b[1;33m[DEBUG] Hello World!\x1b[0m\n'
    finally:
        settings.debug = False
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:41:58.757760
# Unit test for function eager
def test_eager():

    @eager
    def foo():
        for i in range(5):
            yield i
    assert foo() == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:42:01.238369
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'test')
        assert True
    finally:
        settings.debug = False



# Generated at 2022-06-22 12:42:03.674483
# Unit test for function debug
def test_debug():
    assert settings.debug
    message = 'test-debug-message'
    debug(lambda : message) == 'test-debug-message'

# Generated at 2022-06-22 12:42:05.909293
# Unit test for function get_source
def test_get_source():
    def foo(x, y):
        return x + y

    assert get_source(foo) == 'def foo(x, y):\n    return x + y'

# Generated at 2022-06-22 12:42:08.937131
# Unit test for function debug
def test_debug():
    settings.debug = True

    def get_message():
        return 'foo'

    debug(get_message)
    assert 'foo' in sys.stderr.getvalue()



# Generated at 2022-06-22 12:42:11.329755
# Unit test for function get_source
def test_get_source():
    def foo(a, b, c=3, *args, **kwargs):
        print(a, b, c, args, kwargs)

    foo_source = """
        def foo(a, b, c=3, *args, **kwargs):
            print(a, b, c, args, kwargs)
    """
    assert get_source(foo) == foo_source

# Generated at 2022-06-22 12:42:19.572758
# Unit test for function debug
def test_debug():
    debug_messages = []

    def get_message():
        debug_messages.append(message)
        return message

    message = 'abc'
    debug(get_message)
    assert debug_messages == []
    settings.debug = True
    try:
        debug(get_message)
        assert debug_messages == [message]
        debug(get_message)
        assert debug_messages == [message, message]
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:42:21.194762
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'pass'



# Generated at 2022-06-22 12:42:26.928998
# Unit test for function debug
def test_debug():
    assert settings.debug is True
    import io
    buf = io.StringIO()
    sys.stderr = buf
    try:
        debug(lambda: 'abc')
        sys.stderr.flush()
        output = buf.getvalue()
        assert output == '\033[1;31mabc\033[0m\n'
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:42:33.770194
# Unit test for function debug
def test_debug():
    messages.debug = 'd {0}'
    messages.warn = 'w {0}'

    def log_func(message):
        assert message in ('d {0}', 'w {0}')

    with patch('sys.stderr.write', log_func):
        settings.debug = True
        debug(lambda: 'test')
        settings.debug = False
        debug(lambda: 'test')
        warn('test')

# Generated at 2022-06-22 12:42:46.670362
# Unit test for function debug
def test_debug():
    assert settings.debug == False
    debug(lambda: 'message')
    settings.debug = True
    debug(lambda: 'message')



# Generated at 2022-06-22 12:42:48.447634
# Unit test for function get_source
def test_get_source():
    def func():
        pass
    assert get_source(func) == 'pass'



# Generated at 2022-06-22 12:42:50.242620
# Unit test for function eager
def test_eager():
    @eager
    def eager_test():
        return 0
    assert eager_test() == [0]



# Generated at 2022-06-22 12:42:56.499799
# Unit test for function debug
def test_debug():
    from .common import capture_stderr
    with capture_stderr() as out:
        debug(lambda: 'CONF: debug')
        assert out.getvalue() == ''
        settings.debug = True
        debug(lambda: 'CONF: debug')
        assert out.getvalue() == '[DEBUG] CONF: debug\n'
        settings.debug = False
        debug(lambda: 'CONF: debug')
        assert out.getvalue() == '[DEBUG] CONF: debug\n'

# Generated at 2022-06-22 12:42:59.646501
# Unit test for function get_source
def test_get_source():
    def test():
        print('test')
    source = get_source(test)
    assert source == 'def test():\n    print(\'test\')'



# Generated at 2022-06-22 12:43:01.545897
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo).strip() == 'def foo():'

# Generated at 2022-06-22 12:43:03.318711
# Unit test for function get_source
def test_get_source():
    assert get_source(lambda: 42) == 'return 42'

# Generated at 2022-06-22 12:43:10.409264
# Unit test for function debug
def test_debug():
    global debug_str
    debug_str = ''

    def mocked_print(message, file=sys.stderr):
        global debug_str
        debug_str = debug_str + message

    def decorated_func():
        debug(lambda: 'I am debugging!')

    sys.modules['__main__'].settings.debug = True
    sys.modules['__main__'].messages.debug = lambda msg: ('', msg)
    sys.modules['__main__'].sys.stderr = print
    sys.modules['__main__'].print = mocked_print
    decorated_func()
    assert debug_str == '\n\x1b[1m\x1b[34mI am debugging!\x1b[0m\n'

    sys.modules['__main__'].settings.debug = False


# Generated at 2022-06-22 12:43:13.982131
# Unit test for function get_source
def test_get_source():
    def test():
        def test_child():
            pass

    assert get_source(test) == get_source(test_child)

# Generated at 2022-06-22 12:43:21.215813
# Unit test for function debug
def test_debug():
    # Test if debug message is printed
    import io
    import sys

    stream = io.StringIO()
    sys.stderr = stream
    settings.debug = True
    debug(lambda: 'Debug message')
    assert stream.getvalue().strip() == '{} Debug message'.format(settings.prefixes.get('debug'))

    # Test if debug message is NOT printed
    settings.debug = False
    debug(lambda: 'Debug message')
    assert stream.getvalue().strip() == '{} Debug message'.format(settings.prefixes.get('debug'))


# Generated at 2022-06-22 12:43:56.874598
# Unit test for function debug
def test_debug():
    if sys.version_info.major >= 3:
        from io import StringIO
    else:
        from StringIO import StringIO
    import contextlib

    @contextlib.contextmanager
    def capture():
        saved_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            yield sys.stderr
        finally:
            sys.stderr = saved_stderr


# Generated at 2022-06-22 12:44:00.003792
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        yield 1
        yield 2
        yield 3

    assert gen() == [1, 2, 3]



# Generated at 2022-06-22 12:44:06.801718
# Unit test for function get_source
def test_get_source():

    def example_fn():
        pass

    this_file = open(__file__, 'r')
    this_code = this_file.read()
    this_file.close()
    source_lines = this_code.split('\n')
    padding = len(re.findall(r'^(\s*)', source_lines[0])[0])
    expected = '\n'.join(line[padding:] for line in source_lines)
    assert get_source(example_fn) == expected

# Generated at 2022-06-22 12:44:13.128017
# Unit test for function get_source
def test_get_source():
    def foo():
        """Docstring 1"""

        def bar():
            """Docstring 2"""
            return 1

        return bar

    def moo(baz=1):
        """Docstring 1"""

        def far(baz: int=2):
            """Docstring 2"""
            return baz

        return far


# Generated at 2022-06-22 12:44:16.519737
# Unit test for function get_source
def test_get_source():
    def f():
        print(1)

    def f_with_docstring():
        """Some docstring"""

    assert get_source(f) == 'print(1)'
    assert get_source(f_with_docstring) == ''



# Generated at 2022-06-22 12:44:21.868129
# Unit test for function debug
def test_debug():
    class MockStdout(object):
        def __init__(self):
            self.message = ''
        def write(self, message):
            self.message += message

    saved_stdout = sys.stderr
    mock_stdout = MockStdout()
    sys.stderr = mock_stdout
    debug(lambda: '123')
    sys.stderr = saved_stdout
    assert mock_stdout.message == '\033[91m[py-backwards] 123\033[0m\n'

# Generated at 2022-06-22 12:44:23.756603
# Unit test for function get_source
def test_get_source():
    def f(): pass
    assert get_source(f) == 'def f(): pass'

# Generated at 2022-06-22 12:44:28.126669
# Unit test for function get_source
def test_get_source():
    def dummy_function():
        """This is a dummy function."""
        pass
    source = get_source(dummy_function)
    assert source == 'def dummy_function():\n' \
                     '    """This is a dummy function."""\n' \
                     '    pass\n' \



# Generated at 2022-06-22 12:44:32.653594
# Unit test for function debug
def test_debug():
    messages.debug = lambda x: x

    msg = 'test!'

    def test(expected: str) -> None:
        settings.debug = True
        print('Got: {!r}'.format(expected), file=sys.stderr)
        debug(lambda: msg)

        settings.debug = False
        debug(lambda: msg)

    test(msg)

# Generated at 2022-06-22 12:44:36.871980
# Unit test for function get_source
def test_get_source():
    def fun(a, b=1, *args, c, **kwargs):
        pass

    assert get_source(fun) == 'def fun(a, b=1, *args, c, **kwargs):'

# Generated at 2022-06-22 12:45:03.491750
# Unit test for function get_source
def test_get_source():
    def my_function():
        if True:
            pass
        if True:
            pass
        if True:
            pass
        if True:
            pass
    assert get_source(my_function) == 'if True:\n    pass'

# Generated at 2022-06-22 12:45:04.445635
# Unit test for function eager
def test_eager():
    assert sum(eager(range)(10)) == 45

# Generated at 2022-06-22 12:45:06.456443
# Unit test for function eager
def test_eager():
    def function():
        yield 1
        yield 2
        yield 3

    assert [1, 2, 3] == eager(function)()

# Generated at 2022-06-22 12:45:09.300240
# Unit test for function eager
def test_eager():
    result = []
    eager_func = eager(lambda: range(5))
    for i in eager_func():
        result.append(i)
    assert result == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:45:11.369880
# Unit test for function eager
def test_eager():
    @eager
    def generate():
        for i in range(3):
            yield i
    assert generate() == [0, 1, 2]

# Generated at 2022-06-22 12:45:16.219229
# Unit test for function get_source
def test_get_source():
    def test():
        def test_inside():
            pass

        pass

    assert get_source(test) == '    def test_inside():\n        pass\n    pass'

# Generated at 2022-06-22 12:45:18.392766
# Unit test for function debug
def test_debug():
    def some_function():
        debug(lambda: 'hello')
    some_function()

# Generated at 2022-06-22 12:45:22.114357
# Unit test for function get_source
def test_get_source():
    from .test_parser import TestParser
    import re
    source = get_source(TestParser.test_class)
    assert re.match(r'^class TestClass:\n\s+pass$', source) is not None

# Generated at 2022-06-22 12:45:31.450579
# Unit test for function debug
def test_debug():
    import unittest
    import sys
    import io
    import warnings

    class TestDebugCase(unittest.TestCase):
        def setUp(self):
            self.output = sys.stderr = io.StringIO()
            self.warnings = warnings.catch_warnings(record=True)
            self.warnings_manager, self.warnings = self.warnings
            self.warnings_manager.__enter__()

        def test_debug_false(self):
            settings.debug = False
            debug(lambda: 'the message')
            self.assertEqual(self.output.getvalue(), '')

        def test_debug_true_message(self):
            settings.debug = True
            debug(lambda: 'the message')

# Generated at 2022-06-22 12:45:35.076523
# Unit test for function eager
def test_eager():
    def make_iterator():
        for i in range(5):
            yield i
    iterator = make_iterator()
    assert iterator == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:46:41.048131
# Unit test for function get_source
def test_get_source():
    def example_function():
        asdf = 'gjusdf'
        return 2

    expected = "    asdf = 'gjusdf'\n    return 2"
    actual = get_source(example_function)
    assert expected == actual

# Generated at 2022-06-22 12:46:42.824250
# Unit test for function eager
def test_eager():

    def f():
        yield 1
        yield 2

    assert eager(f)() == [1, 2]

# Generated at 2022-06-22 12:46:49.037581
# Unit test for function debug
def test_debug():
    from . import temp_settings_context
    from unittest.mock import Mock

    print = Mock()
    message = 'message'
    with temp_settings_context(debug=True):
        debug(lambda: message)
        print.assert_called_once_with(messages.debug(message), file=sys.stderr)

    print.reset_mock()
    with temp_settings_context(debug=False):
        debug(lambda: message)
        print.assert_not_called()

# Generated at 2022-06-22 12:46:55.856367
# Unit test for function debug
def test_debug():
    from io import StringIO
    from sys import stderr
    from unittest.mock import patch
    from ..conf import settings

    buf = StringIO()
    with patch('sys.stderr', buf), patch.object(settings, 'debug', True):
        debug(lambda: 'test')
        assert buf.getvalue().strip('\n') == '\033[90mtest\033[0m'

    buf = StringIO()

# Generated at 2022-06-22 12:46:58.718214
# Unit test for function get_source
def test_get_source():
    def greet(name):
        pass
    function_source = get_source(greet)
    # assert function_source is right
    assert function_source == 'def greet(name):\n    pass'


# Generated at 2022-06-22 12:47:08.234395
# Unit test for function debug
def test_debug():
    import pytest
    from ..utils import redirect_stderr

    with redirect_stderr() as stderr:
        debug(lambda: 'Hello, world!')
        assert stderr.getvalue() == ''

    with pytest.raises(AssertionError):
        with redirect_stderr() as stderr:
            debug(lambda: 'Hello, world!')
            assert stderr.getvalue() == 'Hello, world!'

    with redirect_stderr() as stderr:
        settings.debug = True
        debug(lambda: 'Hello, world!')
        assert stderr.getvalue() == '\x1b[33mDebug: Hello, world!\x1b[0m\n'

# Generated at 2022-06-22 12:47:13.064935
# Unit test for function eager
def test_eager():
    a = [1,2,3]
    def test_func():
        for i in a:
            yield i
    assert eager(test_func)() == [1,2,3]



# Generated at 2022-06-22 12:47:15.507665
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'def test_function():\n    pass'

# Generated at 2022-06-22 12:47:18.127517
# Unit test for function eager
def test_eager():
    @eager
    def fn(numbers):
        for number in numbers:
            yield number * 2
    assert fn([10, 20]) == [20, 40]

# Generated at 2022-06-22 12:47:21.773830
# Unit test for function eager
def test_eager():
    @eager
    def return_numbers(max_num: int) -> Iterable[int]:
        for num in range(max_num):
            yield num

    assert return_numbers(4) == [0, 1, 2, 3], 'Function eager does not work correctly'

