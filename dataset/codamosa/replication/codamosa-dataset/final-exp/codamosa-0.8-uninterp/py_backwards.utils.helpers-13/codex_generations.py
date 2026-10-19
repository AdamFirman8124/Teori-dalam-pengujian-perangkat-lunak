

# Generated at 2022-06-22 12:38:25.874247
# Unit test for function debug
def test_debug():
    assert settings.debug is False
    debug(lambda: 'hello')
    settings.debug = True
    debug(lambda: 'hello')
    settings.debug = False

# Generated at 2022-06-22 12:38:27.665960
# Unit test for function get_source
def test_get_source():
    def beta():
        return 2
    assert get_source(beta) == 'return 2'

# Generated at 2022-06-22 12:38:29.956191
# Unit test for function get_source
def test_get_source():
    code = """
    def test():
        print('Hell yea!')
    """
    assert get_source(test_get_source) == code

# Generated at 2022-06-22 12:38:32.685600
# Unit test for function eager
def test_eager():
    l = [1, 2, 3]
    def gen():
        for i in l:
            yield i
    l2 = eager(gen)() # should return the list [1,2,3]
    assert l2 == [1,2,3]


# Generated at 2022-06-22 12:38:39.004035
# Unit test for function get_source
def test_get_source():
    def inner_fn():
        pass
    def outer_fn():
        if True:
            pass

        if True:
            pass
        else:
            pass

        return inner_fn

    assert get_source(inner_fn) == 'pass'
    # pylint: disable=unreachable
    assert get_source(outer_fn) == """
        if True:
            pass

        if True:
            pass
        else:
            pass

        return inner_fn
    """

# Generated at 2022-06-22 12:38:42.188842
# Unit test for function debug
def test_debug():
    _old_debug = settings.debug
    settings.debug = True
    try:
        debug(lambda: 'test')
        assert True
    except:
        assert False
    finally:
        settings.debug = _old_debug

# Generated at 2022-06-22 12:38:45.687999
# Unit test for function eager
def test_eager():
    @eager
    def test() -> Iterable[int]:
        yield 1
        yield 2
        yield 3

    assert test() == [1, 2, 3]

# Generated at 2022-06-22 12:38:49.877795
# Unit test for function get_source
def test_get_source():
    def test():
        """Test function for get_source function"""
        print('Test function')
        return 1


# Generated at 2022-06-22 12:38:54.130253
# Unit test for function get_source
def test_get_source():
    def valid_code():
        pass

    assert get_source(valid_code) == 'def valid_code():\n    pass'


# Generated at 2022-06-22 12:38:56.156701
# Unit test for function get_source
def test_get_source():
    @backwards
    def a(x):
        return x

    assert get_source(a) == 'return x'



# Generated at 2022-06-22 12:39:04.699347
# Unit test for function eager
def test_eager():
    from hypothesis import given, assume, strategies as st

    @eager
    def hypothetical_func(data: list) -> Iterable[int]:
        assume(data)
        yield len(data)

    @given(st.lists(st.integers()))
    def test_hypothetical_func(data: list) -> None:
        assert len(hypothetical_func(data)) == len(data)

    test_hypothetical_func()

# Generated at 2022-06-22 12:39:06.723913
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2

    g = eager(f)
    assert g() == [1, 2]

# Generated at 2022-06-22 12:39:08.733278
# Unit test for function get_source
def test_get_source():
    def hello(word: str) -> str:
        return 'Hello, {}'.format(word)


# Generated at 2022-06-22 12:39:11.920116
# Unit test for function get_source
def test_get_source():
    def foo():  # pragma: no cover
        pass

    assert get_source(foo) == 'def foo():\n    pass'



# Generated at 2022-06-22 12:39:22.856645
# Unit test for function debug

# Generated at 2022-06-22 12:39:27.326071
# Unit test for function debug
def test_debug():
    settings.debug = True
    def test_function():
        debug(lambda: 'This should be displayed as debug.')

    test_function()

# Generated at 2022-06-22 12:39:33.901716
# Unit test for function debug
def test_debug():
    print('importing unittest')
    from unittest import mock      # pylint: disable=import-outside-toplevel
    print('importing unittest - done')
    debug(lambda: 'test_debug')
    with mock.patch.object(sys.stderr, 'write', mock.Mock()) as mock_write:
        debug(lambda: 'mock write')
        assert mock_write.called is True



# Generated at 2022-06-22 12:39:36.070136
# Unit test for function get_source
def test_get_source():
    def hello() -> None:
        print('Hello')

    assert get_source(hello) == 'print(\'Hello\')'

# Generated at 2022-06-22 12:39:40.140599
# Unit test for function get_source
def test_get_source():
    def foo():
        # NOTE: The number of spaces is important here
        pass

    source = get_source(foo)
    assert source.strip(' ') == 'pass', source


if '__main__' == __name__:
    test_get_source()

# Generated at 2022-06-22 12:39:42.096261
# Unit test for function debug
def test_debug():
    debug_message = 'This should be printed'
    debug(lambda: debug_message)



# Generated at 2022-06-22 12:39:50.195150
# Unit test for function debug
def test_debug():
    import io
    from pybackwards.conf import settings
    settings.debug = True
    try:
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stderr = capturedOutput             # and redirect stdout.
        debug(lambda: 'Hello')
        sys.stderr = sys.__stderr__             # Reset redirect.
        assert 'Hello' in capturedOutput.getvalue()
    finally:
        settings.debug = False


# Generated at 2022-06-22 12:39:54.884334
# Unit test for function get_source
def test_get_source():
    import py_backwards.utils
    def foo(number: int,
            flag: bool,
            name=""):
        a = 10
        b = 20
        return a + b
    assert get_source(foo) == py_backwards.utils.get_source(foo)

# Generated at 2022-06-22 12:39:56.702260
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'pass'



# Generated at 2022-06-22 12:39:58.289805
# Unit test for function get_source
def test_get_source():
    def test_fn():
        pass

    assert get_source(test_fn) == 'pass'

# Generated at 2022-06-22 12:40:01.130460
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'debug message')
    debug(lambda: 'debug message')
    settings.debug = False

# Generated at 2022-06-22 12:40:02.769332
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f).endswith('        pass\n')



# Generated at 2022-06-22 12:40:06.802800
# Unit test for function debug
def test_debug():
    """Test the function debug"""
    assert debug(lambda: 'TEST-DEBUG MESSAGE') == None
    assert debug(lambda: 'TEST-DEBUG-2 MESSAGE') == None

# Generated at 2022-06-22 12:40:12.118009
# Unit test for function get_source
def test_get_source():
    def test_function():
        '''
            This is a test function
            to test get_source
            function
        '''
        return 1
    source = '''
    def test_function():
        '''

# Generated at 2022-06-22 12:40:15.947793
# Unit test for function get_source
def test_get_source():
    # noinspection PyUnusedLocal
    def f(x):
        if x == 0:
            return 0
        x *= x
        return x

# Generated at 2022-06-22 12:40:24.519542
# Unit test for function debug
def test_debug():
    with patch('py_backwards.util.settings', debug=True):
        with patch('py_backwards.util.print') as mock_print:
            debug(lambda: 'test')
            assert mock_print.call_args[0][0] == messages.debug('test')
            assert not mock_print.call_args[1]['file'] == sys.stderr

    with patch('py_backwards.util.settings', debug=False):
        with patch('py_backwards.util.print') as mock_print:
            debug(lambda: 'test')
            assert not mock_print.called

# Generated at 2022-06-22 12:40:32.836632
# Unit test for function eager
def test_eager():
    @eager
    def simple_generator_function():
        yield 1
        yield 2

    assert simple_generator_function() == [1, 2]

    @eager
    def generator_function_with_args(start, end):
        x = start
        while x < end:
            yield x
            x += 1

    assert generator_function_with_args(2, 6) == [2, 3, 4, 5]

# Generated at 2022-06-22 12:40:36.851211
# Unit test for function eager
def test_eager():
    @eager
    def fn(n: int) -> Iterable[int]:
        i = 1
        while i <= n:
            yield i
            i += 1
    assert fn(5) == [1, 2, 3, 4, 5]


# Generated at 2022-06-22 12:40:38.783562
# Unit test for function get_source
def test_get_source():
    def fn():
        a = 1

    assert get_source(fn) == 'a = 1'

# Generated at 2022-06-22 12:40:40.982022
# Unit test for function get_source
def test_get_source():
    def foo():
        pass  # noqa

    assert get_source(foo) == 'def foo():\n    pass'



# Generated at 2022-06-22 12:40:41.946118
# Unit test for function debug
def test_debug():
    debug(lambda: 'debug')

# Generated at 2022-06-22 12:40:45.155886
# Unit test for function get_source
def test_get_source():
    def foo():
        return 'bar'

    def foo_bar():
        pass

    assert get_source(foo) == "return 'bar'"
    assert get_source(foo_bar) == ''

# Generated at 2022-06-22 12:40:47.201681
# Unit test for function get_source
def test_get_source():
    def foo():
        return 'bar'
    assert get_source(foo) == 'return \'bar\''

# Generated at 2022-06-22 12:40:57.392411
# Unit test for function debug
def test_debug():
    from unittest import TestCase, mock  # type: ignore

    logging_mock = mock.Mock()

    with mock.patch('backwards.core.sys') as mock_sys:
        mock_sys.stderr = logging_mock

        with mock.patch('backwards.core.settings') as mock_settings:
            mock_settings.debug = True
            debug(lambda: 'test')
            mock_sys.stderr.write.assert_called_with(messages.debug('test') + '\n')

            mock_sys.stderr.write.reset_mock()

            mock_settings.debug = False
            debug(lambda: 'test')
            self.assertFalse(mock_sys.stderr.write.called)



# Generated at 2022-06-22 12:41:07.729738
# Unit test for function debug
def test_debug():
    import unittest
    locals_init = locals()
    class TestDebug(unittest.TestCase):
        def test_debug(self):
            self.assertFalse(settings.debug)
            debug(lambda: 'my_message')
        def test_debug_enabled(self):
            try:
                temp_debug = settings.debug
                settings.debug = True
                self.assertTrue(settings.debug)
                debug(lambda: 'my_message')
            finally:
                settings.debug = temp_debug

# Generated at 2022-06-22 12:41:12.383384
# Unit test for function eager
def test_eager():
    def foo() -> Iterable[int]:
        for x in range(4):
            for y in range(4):
                yield x + y

    assert eager(foo)() == [0, 1, 1, 2, 1, 2, 2, 3, 2, 3, 3, 4, 3, 4, 4, 5]

# Generated at 2022-06-22 12:41:19.281669
# Unit test for function get_source
def test_get_source():
    def foo():
        x = 10
        y = 10
        print(x+y)

    src = get_source(foo)
    assert src == 'x = 10\ny = 10\nprint(x+y)'

# Generated at 2022-06-22 12:41:21.249173
# Unit test for function eager
def test_eager():
    assert eager(lambda x: (y for y in [x]))(1) == [1]

# Generated at 2022-06-22 12:41:23.332229
# Unit test for function get_source

# Generated at 2022-06-22 12:41:30.073800
# Unit test for function debug
def test_debug():
    from unittest.mock import patch, call

    with patch('sys.stderr'), patch('py_backwards.utils.messages.debug') as debug:
        debug.return_value = 'test_message'
        settings.debug = False
        debug(lambda: 'test_message')
        assert sys.stderr.write.call_args_list == []
        settings.debug = True
        debug(lambda: 'test_message')
        assert sys.stderr.write.call_args_list == [call('test_message')]

# Generated at 2022-06-22 12:41:31.799677
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass\n'

# Generated at 2022-06-22 12:41:36.476714
# Unit test for function debug
def test_debug():
    def get_message():
        return 'message'

    buffer = sys.stderr

    try:
        sys.stderr = StringIO()
        print('hello', file=sys.stderr)
        debug(get_message)
        assert sys.stderr.getvalue() == 'hello\x1b[35mDEBUG: message\x1b[0m\n'

    finally:
        sys.stderr = buffer

# Generated at 2022-06-22 12:41:39.449203
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass

    assert get_source(test_func) == 'def test_func():\n    pass'

# Generated at 2022-06-22 12:41:43.044560
# Unit test for function debug
def test_debug():
    messages.debug = 'debug:'
    messages.warn = 'warn:'
    assert debug(lambda: 'value') is None
    assert messages.settings.debug == False
    messages.settings.debug = True
    debug(lambda: 'value') == 'debug:value'



# Generated at 2022-06-22 12:41:46.132987
# Unit test for function eager
def test_eager():
    @eager
    def f():
        yield 1
        yield 2
        yield 3
    assert f() == [1,2,3]


# Generated at 2022-06-22 12:41:50.444223
# Unit test for function get_source
def test_get_source():
    def test():
        x = 0
        x = 1

    def test2():
        x = 0
    source = get_source(test)
    assert source == "x = 0\nx = 1", "function get_source does not work properly"
    source = get_source(test2)
    assert source == "x = 0", "function get_source does not work properly"

# Generated at 2022-06-22 12:41:57.486203
# Unit test for function debug
def test_debug():
    def get_message() -> str:
        return 'test'
    debug(get_message)



# Generated at 2022-06-22 12:42:03.657301
# Unit test for function get_source
def test_get_source():
    @wraps(get_source)
    def apply_get_source(fn: Callable[..., Any]) -> str:
        return get_source(fn)

    def foo():
        def bar():
            return 1

        return bar()

    expected_output = '\n'.join([
        'def bar():',
        '    return 1',
        '',
        'return bar()'
    ])

    assert apply_get_source(foo) == expected_output

# Generated at 2022-06-22 12:42:07.883773
# Unit test for function get_source
def test_get_source():
    def function():
        print('In function')
    lines = get_source(function).split('\n')
    assert len(lines) == 2
    assert lines[0] == 'def function():'
    assert lines[1] == '    print(\'In function\')'

# Generated at 2022-06-22 12:42:11.200297
# Unit test for function get_source
def test_get_source():
    def test():
        x = 5
        def inner():
            y = 6
        return inner()
    expected_output = '''def inner():
        y = 6
    return inner()'''
    assert get_source(test) == expected_output

# Generated at 2022-06-22 12:42:14.769218
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'def fn():\n    pass'



# Generated at 2022-06-22 12:42:16.515186
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:42:19.706069
# Unit test for function get_source
def test_get_source():
    def add(x, y):
        return x + y
    source = get_source(add)
    assert source == "def add(x, y):\n" \
                     "    return x + y"

# Generated at 2022-06-22 12:42:23.088023
# Unit test for function get_source
def test_get_source():
    """ test_get_source :: () -> (Bool) """
    def f():
        pass
    print(get_source(f) == """def f():
    pass""")

if __name__ == "__main__":
    test_get_source()

# Generated at 2022-06-22 12:42:29.064496
# Unit test for function get_source
def test_get_source():
    def foo():
        """ some doc string """
        if True:
            pass


# Generated at 2022-06-22 12:42:32.263831
# Unit test for function get_source
def test_get_source():
    def test_func_with_padding():
        assert True
    assert get_source(test_func_with_padding) == ' assert True'

# Generated at 2022-06-22 12:42:44.633435
# Unit test for function eager
def test_eager():
    def foo():
        yield 1
        yield 2

    assert eager(foo)() == [1, 2]

# Generated at 2022-06-22 12:42:47.030359
# Unit test for function get_source
def test_get_source():
    def foo():
        return 'bar'
    assert get_source(foo) == 'return "bar"'



# Generated at 2022-06-22 12:42:49.929853
# Unit test for function get_source
def test_get_source():
    def test():
        """Some
            test
            func
        """
        pass

    assert get_source(test) == '        """Some\n            test\n            func\n        """\n'

# Generated at 2022-06-22 12:42:50.868715
# Unit test for function debug
def test_debug():
    assert debug(lambda: 'test') is None

# Generated at 2022-06-22 12:42:52.892376
# Unit test for function get_source
def test_get_source():
    def func():
        pass

    assert get_source(func) == 'def func():\n    pass'



# Generated at 2022-06-22 12:43:00.940365
# Unit test for function debug
def test_debug():
    from io import StringIO
    from sys import stderr, _getframe
    from ..conf import settings
    from .. import messages

    prev_stderr = stderr
    prev_debug_mode = settings.debug
    try:
        out = StringIO()
        stderr = out
        settings.debug = True
        debug(lambda: 'Hello')
        assert messages.debug('Hello') + '\n' == out.getvalue()
    finally:
        stderr = prev_stderr
        settings.debug = prev_debug_mode



# Generated at 2022-06-22 12:43:05.447958
# Unit test for function debug
def test_debug():
    try:
        import StringIO
        stream = StringIO.StringIO()
        sys.stderr = stream
        settings.debug = True
        debug(lambda: 'Test message')
        assert stream.getvalue() == messages.debug('Test message') + '\n'
    finally:
        settings.debug = False
        stream.close()

# Generated at 2022-06-22 12:43:07.192615
# Unit test for function get_source
def test_get_source():
    def f():
        def g():
            return 2
    assert get_source(g) == 'return 2'

# Generated at 2022-06-22 12:43:10.167304
# Unit test for function get_source
def test_get_source():
    def test():
        def inner():
            def target():
                return 'unit test source'
            return target

        return inner()

    assert get_source(test()) == "return 'unit test source'"



# Generated at 2022-06-22 12:43:13.789445
# Unit test for function eager
def test_eager():
    @eager
    def xs() -> Iterable[int]:
        yield 1
        yield 2
    assert xs() == [1, 2]

# Generated at 2022-06-22 12:43:43.605515
# Unit test for function get_source
def test_get_source():
    def test_fun():
        return

    assert get_source(test_fun) == 'def test_fun():\n    return'


if __name__ == "__main__":
    test_get_source()

# Generated at 2022-06-22 12:43:46.046619
# Unit test for function eager
def test_eager():

    def gen(x: int) -> Iterable[int]:
        for i in range(x):
            yield i

    assert eager(gen)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:43:48.733468
# Unit test for function debug
def test_debug():
    log = []
    debug_fn = lambda: log.append(debug)
    settings.debug = True
    debug_fn()
    assert log
    log.clear()
    settings.debug = False
    debug_fn()
    assert not log



# Generated at 2022-06-22 12:43:55.060317
# Unit test for function eager
def test_eager():
    def foo() -> Iterable[int]:
        return range(10)

    assert foo() is not foo()

    assert foo() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert eager(foo)() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-22 12:43:57.902707
# Unit test for function get_source
def test_get_source():
    def foo(a, b, c):
        pass


# Generated at 2022-06-22 12:44:01.501273
# Unit test for function get_source
def test_get_source():
    def test():
        1+1

    assert get_source(test) == '1+1'
    assert get_source(test) == '1+1'



# Generated at 2022-06-22 12:44:03.741560
# Unit test for function get_source
def test_get_source():
    def simple_function():
        pass

    assert get_source(simple_function) == 'def simple_function():\n    pass'

# Generated at 2022-06-22 12:44:04.590984
# Unit test for function debug
def test_debug():
    debug(lambda: 'test')

# Generated at 2022-06-22 12:44:05.595132
# Unit test for function debug
def test_debug():
    debug(lambda: 'test')


# Generated at 2022-06-22 12:44:10.967607
# Unit test for function get_source
def test_get_source():

    def foo(a, b, c=3, d=4, e=5, f=6):
        return a + b

    assert get_source(foo) == 'def foo(a, b, c=3, d=4, e=5, f=6):\n    return a + b'

# Generated at 2022-06-22 12:45:02.174491
# Unit test for function debug
def test_debug():
    if settings.debug:
        settings.debug = False
        assert not debug(lambda: "Message")
        settings.debug = True
        assert debug(lambda: "Message")

# Generated at 2022-06-22 12:45:08.452604
# Unit test for function debug
def test_debug():
    debug_message = 'A debug message.'

    old_debug_value = settings.debug
    try:
        settings.debug = True
        debug(lambda: debug_message)
        assert messages.get_last_message(stream=sys.stderr) == messages.debug(debug_message)

        settings.debug = False
        debug(lambda: debug_message)
        assert messages.get_last_message(stream=sys.stderr) is None
    finally:
        settings.debug = old_debug_value

# Generated at 2022-06-22 12:45:10.516739
# Unit test for function eager
def test_eager():
    @eager
    def generator():
        yield 1
        yield 2

    assert generator() == [1, 2]

# Generated at 2022-06-22 12:45:12.839226
# Unit test for function debug
def test_debug():
    debug(lambda: 'debug message')

# Generated at 2022-06-22 12:45:18.588306
# Unit test for function debug
def test_debug():
    __tracebackhide__ = True

    debug_output = io.StringIO()
    with mock.patch.object(sys, 'stderr', debug_output):
        debug(lambda: 'test')

    assert debug_output.getvalue() == ''

    with mock.patch.object(settings, 'debug', True):
        debug = mock.MagicMock()
        debug(lambda: 'test')
        debug.assert_called_once_with(lambda: 'test')



# Generated at 2022-06-22 12:45:28.910923
# Unit test for function get_source
def test_get_source():
    from . import _context
    from .tests import _test_no_args
    from .tests import _test_multiple_args
    from .tests import _test_with_kwargs
    from .tests import _test_with_star_args
    from .tests import _test_with_star_kwargs
    from .tests import _test_with_both

    assert get_source(_test_no_args) == 'return 5'
    assert get_source(_test_multiple_args) == 'return a + b'
    assert get_source(_test_with_kwargs) == 'return a * b'
    assert get_source(_test_with_star_args) == 'return a + b'
    assert get_source(_test_with_star_kwargs) == 'return a * b'

# Generated at 2022-06-22 12:45:30.543574
# Unit test for function get_source
def test_get_source():
    @get_source
    def add():
        return 1 + 2
    assert add == 'return 1 + 2\n'

# Generated at 2022-06-22 12:45:35.696765
# Unit test for function get_source
def test_get_source():
    def fn(arg1, arg2):
        """Function docstring."""
        return arg1
    source = '''
    def fn(arg1, arg2):
        """Function docstring."""
        return arg1'''

    assert get_source(fn) == source

# Generated at 2022-06-22 12:45:39.850175
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'def fn():\n    pass'

    def fn():
        print('aaa')
        print('bbb')

    assert get_source(fn) == 'def fn():\n    print(\'aaa\')\n    print(\'bbb\')'

# Generated at 2022-06-22 12:45:42.670195
# Unit test for function debug
def test_debug():
    message = 'a' * settings.debug_line_length
    debug(lambda: message)

# Generated at 2022-06-22 12:47:47.647011
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'pass'

# Generated at 2022-06-22 12:47:51.822008
# Unit test for function get_source
def test_get_source():
    def test(a: int, b: int) -> int:
        return a + b

    assert get_source(test) == 'return a + b'

# Generated at 2022-06-22 12:47:54.807739
# Unit test for function eager
def test_eager():
    # type: () -> None
    xs = range(0, 10)
    assert eager(reversed)(xs) == list(reversed(xs))

    xs = ['a', 'b', 'c', 'd', 'e']
    assert eager(reversed)(xs) == list(reversed(xs))



# Generated at 2022-06-22 12:47:56.678049
# Unit test for function eager
def test_eager():
    assert eager(range)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:48:01.619625
# Unit test for function eager
def test_eager():
    from ..core import Step
    @Step()
    def f(x):
        yield x

    @eager
    def g(x):
        yield x

    assert f(1) == [1]
    assert isinstance(f(1), list)
    assert g(1) == [1]
    assert type(g(1)) is list

test_eager()

# Generated at 2022-06-22 12:48:05.686378
# Unit test for function get_source
def test_get_source():
    def func_to_get_source_from():
        pass
    # returns source code of the function
    assert get_source(func_to_get_source_from) == 'def func_to_get_source_from():\n    pass'

# Generated at 2022-06-22 12:48:13.348272
# Unit test for function debug
def test_debug():
    def get_message():
        return 'hello'
    def run():
        debug(get_message)
    run.__name__ = 'run'
    settings.debug = False
    with capture_output() as (out, err):
        run()
    assert out.getvalue() == ''
    assert err.getvalue() == ''
    settings.debug = True
    with capture_output() as (out, err):
        run()
    assert out.getvalue() == ''
    assert err.getvalue().strip() == messages.debug(get_message())
    settings.debug = False



# Generated at 2022-06-22 12:48:19.623118
# Unit test for function eager
def test_eager():
    import unittest
    class EagerTest(unittest.TestCase):
        def test_iterable(self):
            def f():
                yield 1
                yield 2
                yield 3
            self.assertEqual(eager(f)(), [1, 2, 3])
    unittest.main()



# Generated at 2022-06-22 12:48:22.399205
# Unit test for function eager
def test_eager():
    @eager
    def generator():
        yield 1
        yield 2
        yield 3
    assert generator() == [1, 2, 3]