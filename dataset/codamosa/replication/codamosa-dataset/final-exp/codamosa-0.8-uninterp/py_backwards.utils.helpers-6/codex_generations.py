

# Generated at 2022-06-22 12:38:33.842189
# Unit test for function debug
def test_debug():
    result = []
    def fake_print(message: str, file: Any=None) -> None:
        result.append(message)

    original_print = __builtins__.print
    __builtins__.print = fake_print

    try:
        settings.debug = True
        debug(lambda: 'test')
        assert result == [messages.debug('test')]

        settings.debug = False
        debug(lambda: 'test')
        assert result == [messages.debug('test')]
    finally:
        __builtins__.print = original_print

# Generated at 2022-06-22 12:38:42.949693
# Unit test for function debug
def test_debug():
    from . import settings_with_debug_enabled
    import mock

    settings.enable_debug()
    func = lambda: 'Some message'
    func.__name__ = 'my_func'
    with mock.patch('sys.stderr', new_callable=lambda: sys.stdout):
        debug(func)
    assert sys.stdout.getvalue() == '\x1b[94m{}(): Some message\x1b[0m\n'.format(func.__name__)

    settings.disable_debug()
    with mock.patch('sys.stderr', new_callable=lambda: sys.stdout):
        debug(func)
    assert sys.stdout.getvalue() == ''

# Generated at 2022-06-22 12:38:46.777414
# Unit test for function get_source
def test_get_source():
    from .test_decorators import test_get_source as fn
    assert get_source(fn) == '''\
        def test_get_source():
            return 1
        '''



# Generated at 2022-06-22 12:38:49.144849
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        yield 1
        yield 2

    assert foo() == [1, 2]

# Generated at 2022-06-22 12:38:51.935336
# Unit test for function debug
def test_debug():
    import sys
    import io
    import contextlib
    oldstdout = sys.stderr
    try:
        sys.stderr = io.StringIO()
        debug(lambda: 'warning message')
        assert sys.stderr.getvalue() == '\x1b[90mwarning message\n\x1b[0m'
    finally:
        sys.stderr = oldstdout

# Generated at 2022-06-22 12:38:56.583382
# Unit test for function get_source
def test_get_source():
    """Tests function get_source."""
    # noinspection PyUnusedLocal
    def foo(a, b):
        """This is a function for testing."""
        # noinspection PyUnresolvedReferences
        return a / b + 1

    assert get_source(foo) == 'return a / b + 1'

# Generated at 2022-06-22 12:38:58.041585
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'pass'

# Generated at 2022-06-22 12:39:01.196179
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2
        yield 3

    assert eager(f)() == [1, 2, 3]

# Generated at 2022-06-22 12:39:02.482069
# Unit test for function get_source
def test_get_source():
    def test():
        return False

    assert get_source(test) == 'return False'

# Generated at 2022-06-22 12:39:04.475772
# Unit test for function eager
def test_eager():
    def get_iterator():
        yield 1
        yield 2

    f = eager(get_iterator)
    assert f() == [1, 2]

# Generated at 2022-06-22 12:39:07.946597
# Unit test for function get_source
def test_get_source():
    def function():
        # A comment
        pass

    assert get_source(function) == 'pass'

# Generated at 2022-06-22 12:39:09.669065
# Unit test for function eager
def test_eager():
    @eager
    def lst() -> Iterable[int]: yield 1; yield 2; yield 3
    assert lst() == [1, 2, 3]

# Generated at 2022-06-22 12:39:14.511128
# Unit test for function debug
def test_debug():
    def get_message(): return 'message'
    settings.debug = False
    sys.stderr = open('/dev/null', 'w')
    debug(message)
    sys.stderr = sys.__stderr__
    settings.debug = True
    sys.stderr = open('/dev/null', 'w')
    debug(message)
    sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:16.859708
# Unit test for function get_source
def test_get_source():
    def f(x, y):  # Dummy function
        return x + y

    assert get_source(f) == 'return x + y'

# Generated at 2022-06-22 12:39:19.482188
# Unit test for function eager
def test_eager():
    @eager
    def eager_function(number):
        for i in range(number):
            yield 0
    assert eager_function(10) == [0] * 10

# Generated at 2022-06-22 12:39:21.771184
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass\n'



# Generated at 2022-06-22 12:39:24.857070
# Unit test for function eager
def test_eager():
    @eager
    def get_data() -> Iterable[int]:
        yield 1
        yield 2
        yield 3

    assert get_data() == [1, 2, 3]



# Generated at 2022-06-22 12:39:30.244699
# Unit test for function get_source
def test_get_source():
    def func():
        def inner_func():
            pass

        pass

    assert re.match(r'\n\s*def func\(\):\n\s*def inner_func\(\):\n\s*pass\n\n\s*pass',
                    get_source(func))

# Generated at 2022-06-22 12:39:33.202521
# Unit test for function eager
def test_eager():
    assert list(eager(range(5))()) == [0, 1, 2, 3, 4]


if __name__ == '__main__':
    test_eager()

# Generated at 2022-06-22 12:39:38.952606
# Unit test for function debug
def test_debug():
    settings.debug = False
    debug_messages = []

    def get_message():
        debug_messages.append('getting message')
        return 'this is a message'

    debug(get_message)
    assert not debug_messages

    settings.debug = True
    debug(get_message)
    assert debug_messages == ['getting message']

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-22 12:39:43.839471
# Unit test for function debug
def test_debug():
    with settings(debug=True):
        debug(lambda: 'Works')
    with settings(debug=False):
        debug(lambda: 'Does not work')



# Generated at 2022-06-22 12:39:54.986581
# Unit test for function get_source

# Generated at 2022-06-22 12:40:01.513621
# Unit test for function debug
def test_debug():
    global settings
    test_debug.output = ''

    def print_to_output(*args, **kwargs):
        test_debug.output = ' '.join(*args)

    settings = settings.copy()
    settings['debug'] = True

    sys.stderr.write = print_to_output
    sys.stderr.flush = print_to_output
    sys.stderr.writelines = print_to_output

    debug(lambda: 'oh no')
    assert test_debug.output.find('oh no') != -1

# Generated at 2022-06-22 12:40:04.115496
# Unit test for function get_source
def test_get_source():
    assert 'x = 1\nprint(x)' == get_source(lambda: (x for x in [1]))
    assert 'x = 1\n  print(x)' == get_source(lambda: [x for x in [1]])

# Generated at 2022-06-22 12:40:11.239603
# Unit test for function debug
def test_debug():
    debugs = []
    def _debug(m): debugs.append(m)
    def m(): return 'M'
    system_debug = sys.modules['py_backwards.utils.debug'].debug
    try:
        sys.modules['py_backwards.utils.debug'].debug = _debug
        debug(m)
        assert debugs == ['M']
    finally:
        sys.modules['py_backwards.utils.debug'].debug = system_debug



# Generated at 2022-06-22 12:40:13.847560
# Unit test for function get_source
def test_get_source():
    def f(x):
        a = 1
        return a + x

    assert get_source(f) == 'a = 1\nreturn a + x'

# Generated at 2022-06-22 12:40:21.033532
# Unit test for function debug
def test_debug():
    print_output = []
    sys.stderr.write = print_output.append
    settings.debug = True
    debug(lambda: 'Debug message!!')
    assert print_output == ['\x1b[94mDebug message!!\x1b[0m\n']

    print_output = []
    sys.stderr.write = print_output.append
    settings.debug = False
    debug(lambda: 'Debug message!!')
    assert print_output == []

# Generated at 2022-06-22 12:40:29.150997
# Unit test for function debug
def test_debug():
    import sys
    import pytest
    from io import StringIO
    stream = StringIO()
    sys.stderr = stream
    settings.debug = True
    debug(lambda: 'Hello')
    assert stream.getvalue() == 'WARNING! py-backwards: Hello\n'
    stream.truncate(0)
    debug(lambda: 'Hi')
    assert stream.getvalue() == 'WARNING! py-backwards: Hi\n'
    stream.truncate(0)
    settings.debug = False
    debug(lambda: 'Hello')
    assert stream.getvalue() == ''

# Generated at 2022-06-22 12:40:32.187055
# Unit test for function get_source
def test_get_source():
    def fn():
        a = 1
        b = 2
        return a + b

    assert get_source(fn) == 'a = 1\nb = 2\nreturn a + b\n'



# Generated at 2022-06-22 12:40:36.180195
# Unit test for function get_source
def test_get_source():
    def myfunc():
        return 'Hello world'

    assert get_source(myfunc) \
        == "def myfunc():\n" \
           "    return 'Hello world'\n"


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:40:47.675360
# Unit test for function debug
def test_debug():
    from io import StringIO
    from contextlib import redirect_stdout
    from .context import settings
    settings.debug = True
    with redirect_stdout(StringIO()) as stdout:
        debug(lambda: 'Hello, world')
    assert stdout.getvalue() == "DEBUG: Hello, world\n"
    with redirect_stdout(StringIO()) as stdout:
        debug(lambda: 'Bye bye')
    assert stdout.getvalue() == "DEBUG: Bye bye\n"

# Generated at 2022-06-22 12:40:50.295439
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            pass

    assert get_source(foo) == '\n    def bar():\n        pass\n'

# Generated at 2022-06-22 12:40:59.348757
# Unit test for function debug
def test_debug():
    from io import StringIO
    from unittest import TestCase
    from ...conf import set_debug

    class TestDebug(TestCase):
        def setUp(self):
            self.std_stream = sys.stderr
            sys.stderr = StringIO()

        def tearDown(self):
            sys.stderr = self.std_stream

        def test_works(self):
            set_debug(True)

            def get_message():
                return 'hello'

            debug(get_message)
            self.assertIn('hello', sys.stderr.getvalue())

            set_debug(False)
            sys.stderr.truncate(0)
            sys.stderr.seek(0)
            debug(get_message)

# Generated at 2022-06-22 12:41:04.147868
# Unit test for function get_source
def test_get_source():
    def some_function(a, b):
        if a > 3:
            b = a + b
        else:
            return b

    assert get_source(some_function) == 'if a > 3:\n    b = a + b\nelse:\n    return b'

# Generated at 2022-06-22 12:41:06.597307
# Unit test for function get_source
def test_get_source():
    def func():
        """Hello world"""
        return

    assert get_source(func) == "def func():\n    \"\"\"Hello world\"\"\"\n    return"

# Generated at 2022-06-22 12:41:17.135229
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)

# Generated at 2022-06-22 12:41:20.112757
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn).startswith('def fn()')

# Generated at 2022-06-22 12:41:22.100556
# Unit test for function get_source
def test_get_source():
    def fn():
        return 1

    assert get_source(fn) == (
        'def fn():\n'
        '    return 1'
    )

# Generated at 2022-06-22 12:41:24.669198
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2
        yield 3

    assert eager(f)() == [1, 2, 3]

# Generated at 2022-06-22 12:41:26.404265
# Unit test for function get_source
def test_get_source():
    def f():
        print(1)

    assert get_source(f) == 'print(1)'



# Generated at 2022-06-22 12:41:35.928670
# Unit test for function debug
def test_debug():
    settings.debug = True
    msg = 'test'

    def get_message():
        return msg

    import io
    import sys
    try:
        sys.stderr = io.StringIO()
        debug(get_message)
        assert str(sys.stderr) == '[pybackwards][DEBUG] ' + msg + '\n'
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:41:40.470907
# Unit test for function eager
def test_eager():
    from collections import Iterable
    from itertools import count

    @eager
    def f() -> Iterable[int]:
        for i in count(0):
            yield i

    for i in f():
        assert i == 0
        break



# Generated at 2022-06-22 12:41:44.250512
# Unit test for function get_source
def test_get_source():
    def foo(a, b):
        pass
    assert get_source(foo) == 'def foo(a, b):\n    pass'



# Generated at 2022-06-22 12:41:47.730489
# Unit test for function debug
def test_debug():
    assert not settings.debug
    debug(lambda: 'bar')
    try:
        settings.debug = True
        debug(lambda: 'foo')
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:41:48.905341
# Unit test for function eager
def test_eager():
    func = lambda: range(5)
    assert eager(func)() == list(func())

# Generated at 2022-06-22 12:41:52.458948
# Unit test for function get_source
def test_get_source():
    def foo():
        a = 1
        b = 2
    assert get_source(foo) == 'a = 1\nb = 2', 'Should return correct source code of the function'


# Generated at 2022-06-22 12:41:55.464569
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        for i in range(10):
            yield i

    assert gen() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-22 12:41:58.382385
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'debug')
    settings.debug = False
    debug(lambda: 'debug')

if __name__ == '__main__':
    test_debug()

# Generated at 2022-06-22 12:42:03.423561
# Unit test for function debug
def test_debug():
    debug_messages = []
    def get_message():
        if len(debug_messages) == 0:
            return 'message 1'
        return 'message 2'

    debug(get_message)
    debug(get_message)
    settings.debug = False
    debug(get_message)

    assert debug_messages == ['message 1']



# Generated at 2022-06-22 12:42:05.444870
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass'



# Generated at 2022-06-22 12:42:12.489456
# Unit test for function debug
def test_debug():
    import sys
    from cStringIO import StringIO

    try:
        old_stderr = sys.stderr
        sys.stderr = StringIO()
        settings.debug = True
        debug(lambda: 'test debug')
        assert sys.stderr.getvalue() == '\x1b[34m[DEBUG] \x1b[0mtest debug\n'
    finally:
        sys.stderr = old_stderr

# Generated at 2022-06-22 12:42:16.140197
# Unit test for function eager
def test_eager():
    def eager_func() -> Iterable[int]:
        yield 1
        yield 2
        yield 3
    assert eager(eager_func)() == [1, 2, 3]


# Generated at 2022-06-22 12:42:19.334261
# Unit test for function get_source
def test_get_source():
    def test_function(foo, bar='abc'):
        """This is docstring."""
        # Here is some comment
        return foo * bar


# Generated at 2022-06-22 12:42:27.674901
# Unit test for function debug
def test_debug():
    message = 'Hello world'
    with patch.object(settings, 'debug', True) as debug_mock:
        debug(lambda: message)
        stderr_mock = mock_open()
        with patch('sys.stderr', stderr_mock):
            debug_mock.assert_called_once_with()
            stderr_mock.write.assert_called_once_with(messages.debug(message) + '\n')


try:
    # Python 3.5
    from contextlib import ExitStack
except ImportError:
    # Python 3.4
    from contextlib2 import ExitStack

# Generated at 2022-06-22 12:42:38.645925
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    def function_with_body():
        pass
    function_with_body.__code__ = compile(
        '''if True:
            pass
        ''', '<string>', 'exec')

    def function_with_two_statements():
        pass
    function_with_two_statements.__code__ = compile(
        '''if True:
            pass
        elif True:
            pass
        ''', '<string>', 'exec')

    def function_with_padding():
        pass
    function_with_padding.__code__ = compile(
        '''
            if True:
                pass
        ''', '<string>', 'exec')

    def function_with_padding_and_tabs():
        pass
    function_with_padding_and_tabs.__

# Generated at 2022-06-22 12:42:40.257917
# Unit test for function get_source
def test_get_source():
    def test():
        print('test')

    assert get_source(test) == "print('test')"

# Generated at 2022-06-22 12:42:42.364247
# Unit test for function get_source
def test_get_source():
    def fn():
        return 42
    assert 'return 42' in get_source(fn)

# Generated at 2022-06-22 12:42:49.734345
# Unit test for function debug
def test_debug():
    from ..conf import settings
    import io

    value = 'debug message'
    settings.debug = True
    out = io.StringIO()
    sys.stderr = out
    try:
        debug(lambda: value)
        assert getattr(sys.stderr, 'getvalue')() == '\033[34mdebug: {}\033[0m\n'.format(value)
    finally:
        settings.debug = False
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:42:52.449942
# Unit test for function eager
def test_eager():
    from random import randrange
    a = iter(range(1000000))
    b = eager(iter)(range(1000000))
    assert randrange(1000) not in a
    assert randrange(1000) in b

# Generated at 2022-06-22 12:42:55.784183
# Unit test for function get_source
def test_get_source():
    source = '''def test_function(a):
    b = 1
    return a
    '''
    def test_function(a: int) -> int:
        b = 1
        return a
    assert get_source(test_function) == source

# Generated at 2022-06-22 12:43:08.293224
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'a')
    settings.debug = False
    debug(lambda: 'b')


# Generated at 2022-06-22 12:43:17.966011
# Unit test for function debug
def test_debug():
    message = 'test'
    with patch('sys.stderr') as stderr_mock:
        with patch('backwards.utils.settings') as settings_mock:
            settings_mock.debug = True

            debug(lambda: message)
            stderr_mock.write.assert_called_once_with('\033[90mDEBUG: ' + message + '\033[0m\n')

            del stderr_mock.write.call_args_list[:]

            settings_mock.debug = False
            debug(lambda: message)
            assert not stderr_mock.write.called

# Generated at 2022-06-22 12:43:19.661105
# Unit test for function debug
def test_debug():
    string = ''
    debug_ = debug(lambda: string)
    string = 'Hello'
    debug_()



# Generated at 2022-06-22 12:43:22.931922
# Unit test for function get_source
def test_get_source():
    import inspect
    def f(a, b, c):
        """Test function"""
        def g():  # noqa
            a = 1
        return a + b + c

    assert get_source(f) == inspect.getsource(f)



# Generated at 2022-06-22 12:43:23.959485
# Unit test for function debug
def test_debug():
    assert debug is not None

# Generated at 2022-06-22 12:43:24.735460
# Unit test for function debug
def test_debug():
    assert 10 == 11

# Generated at 2022-06-22 12:43:29.180989
# Unit test for function eager
def test_eager():
    def gen(n):
        while n != 0:
            yield n
            n -= 1

    @eager
    def foo():
        yield 1
        yield 2
        yield 3

    assert foo() == [1, 2, 3]
    assert eager(gen)(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# Generated at 2022-06-22 12:43:31.737767
# Unit test for function debug
def test_debug():
    _global_debug = settings.debug

    settings.debug = False
    debug(lambda: 'hello')
    settings.debug = True
    debug(lambda: 'hello')

    settings.debug = _global_debug



# Generated at 2022-06-22 12:43:43.826006
# Unit test for function debug
def test_debug():
    import io
    import sys

    class Stream:
        def __init__(self) -> None:
            self.io = io.StringIO()

        def __enter__(self) -> 'Stream':
            self.old_stderr = sys.stderr
            sys.stderr = self.io
            return self

        def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
            sys.stderr = self.old_stderr

        def __str__(self) -> str:
            return self.io.getvalue()

    with Stream() as stream:
        debug(lambda: 'Debug message')
    assert not stream.io.getvalue()

    with Stream() as stream:
        settings.debug = True
        debug(lambda: 'Debug message')

# Generated at 2022-06-22 12:43:50.553129
# Unit test for function debug
def test_debug():
    stdout = sys.stdout
    try:
        from io import StringIO
        sys.stdout = StringIO()
        settings.debug = True
        debug(lambda: 'foo')
        assert sys.stdout.getvalue() == messages.debug('foo') + '\n'
        sys.stdout.truncate(0)
        settings.debug = False
        debug(lambda: 'foo')
        assert sys.stdout.getvalue() == ''
    finally:
        sys.stdout = stdout



# Generated at 2022-06-22 12:44:13.005043
# Unit test for function get_source
def test_get_source():
    def func():
        a = 1
        b = 2
        return a + b
    assert get_source(func) == 'a = 1\nb = 2\nreturn a + b'

# Generated at 2022-06-22 12:44:14.856057
# Unit test for function get_source
def test_get_source():
    def fn():
        pass
    assert get_source(fn) == 'def fn():\n    pass'

# Generated at 2022-06-22 12:44:20.864251
# Unit test for function get_source
def test_get_source():
    def test_function(x: int, y: int) -> str:
        """
        Function for unit testing of get_source function.
        """
        return 'x + y = {}'.format(x + y)

    assert get_source(test_function) == """def test_function(x: int, y: int) -> str:
    """ + '"""\n    Function for unit testing of get_source function.\n    """'+ '\n    return \'x + y = {}\'.format(x + y)'

# Generated at 2022-06-22 12:44:26.596563
# Unit test for function debug
def test_debug():
    with patch('sys.stderr', new=StringIO()) as fake_stderr:
        debug(lambda: '42')
        assert fake_stderr.getvalue() == ''

        settings.debug = True

        debug(lambda: '42')
        assert fake_stderr.getvalue() == 'debug: 42\n'

        settings.debug = False



# Generated at 2022-06-22 12:44:28.795230
# Unit test for function get_source
def test_get_source():
    def function(): pass
    assert get_source(function) == 'def function(): pass'



# Generated at 2022-06-22 12:44:31.869696
# Unit test for function debug
def test_debug():
    called = []

    def get_message():
        return 'Hello, world!'

    debug(get_message)
    assert not called
    settings.debug = True
    debug(get_message)
    assert called == ['Hello, world!']



# Generated at 2022-06-22 12:44:36.843334
# Unit test for function get_source
def test_get_source():
    
    def my_function():
        x = 1 + 2
        y = 2 * x

        if x > 2:
            z = x / 2
        else:
            z = x * 3

        return x + y + z

    expected = '''
    x = 1 + 2
    y = 2 * x

    if x > 2:
        z = x / 2
    else:
        z = x * 3

    return x + y + z
    '''

    assert get_source(my_function) == expected.strip()

# Generated at 2022-06-22 12:44:39.494527
# Unit test for function eager
def test_eager():
    @eager
    def square(numbers):
        for number in numbers:
            yield number * number

    assert square([1, 2, 3]) == [1, 4, 9]

# Generated at 2022-06-22 12:44:41.829022
# Unit test for function get_source
def test_get_source():
    def test(_a: int, _b: int) -> int:
        return _a + _b

    assert get_source(test) == 'return _a + _b'

# Generated at 2022-06-22 12:44:44.622679
# Unit test for function get_source

# Generated at 2022-06-22 12:45:24.449658
# Unit test for function get_source
def test_get_source():
    def foo(a, b, c):
        pass

    assert get_source(foo) == 'pass'

# Generated at 2022-06-22 12:45:27.214890
# Unit test for function debug
def test_debug():
    assert settings.debug == False
    debug(lambda: 'hello') == None
    settings.debug = True
    assert debug(lambda: 'hello') == None
    assert settings.debug == True



# Generated at 2022-06-22 12:45:28.459613
# Unit test for function eager
def test_eager():
    assert eager(list)(range(4)) == [0, 1, 2, 3]

# Generated at 2022-06-22 12:45:31.296262
# Unit test for function get_source
def test_get_source():
    def test_fn():
        var1 = 1
        var2 = 2

        return var1 + var2

    assert get_source(test_fn) == 'var1 = 1\nvar2 = 2\n\nreturn var1 + var2\n'

# Generated at 2022-06-22 12:45:34.452240
# Unit test for function get_source
def test_get_source():
    def foo():
        bar = 0
        return bar


    assert get_source(foo) == ['bar = 0', 'return bar']

# Generated at 2022-06-22 12:45:40.521066
# Unit test for function get_source
def test_get_source():
    from .test_doc_extraction import test_blank_docstring, test_multiline_docstring
    assert get_source(test_blank_docstring) == 'def test_blank_docstring():\n    pass'
    assert get_source(test_multiline_docstring) == 'def test_multiline_docstring():\n    """Hello world\n\n    This is a test."""\n    pass'

# Generated at 2022-06-22 12:45:43.102559
# Unit test for function get_source
def test_get_source():
    def foo():
        return 'bar'
    assert get_source(foo) == "return 'bar'"

# Generated at 2022-06-22 12:45:46.731925
# Unit test for function eager
def test_eager():
    def gen() -> Iterable[T]:
        yield 1
        yield 2
        yield 3

    assert eager(gen)() == [1, 2, 3]

# Generated at 2022-06-22 12:45:47.686103
# Unit test for function debug
def test_debug():
    debug(lambda: 'hi!')



# Generated at 2022-06-22 12:45:58.092776
# Unit test for function get_source

# Generated at 2022-06-22 12:47:55.630182
# Unit test for function debug
def test_debug():
    old_debug = settings.debug
    settings.debug = False
    debug_message = "debug message"
    with captured_output() as (out, err):
        debug(lambda: debug_message)
    assert not err.getvalue()
    settings.debug = True
    with captured_output() as (out, err):
        debug(lambda: debug_message)
    assert err.getvalue() == messages.debug(debug_message)
    settings.debug = old_debug


# Generated at 2022-06-22 12:47:59.044839
# Unit test for function get_source
def test_get_source():
    def outer_function(a, b, c):
        def inner():
            pass
        return inner
    assert get_source(outer_function) == '\n    def inner():\n        pass\n    return inner\n'

# Generated at 2022-06-22 12:48:02.042575
# Unit test for function get_source
def test_get_source():
    def get_source_test():
        "multiline \n docstring"
        a = 10
        # a comment
        return a

    assert get_source(get_source_test) == "def get_source_test():\n    \"multiline \\n docstring\"\n    a = 10\n    # a comment\n    return a"

# Generated at 2022-06-22 12:48:05.216035
# Unit test for function debug
def test_debug():
    with settings.override_settings(debug=True):
        debug(lambda: 'message')
    with settings.override_settings(debug=False):
        debug(lambda: 'message')

# Generated at 2022-06-22 12:48:07.313063
# Unit test for function get_source
def test_get_source():
    def b():
        pass
    def a():
        pass

    assert get_source(b) == 'pass'
    assert get_source(a) == 'pass'

# Generated at 2022-06-22 12:48:11.065697
# Unit test for function debug
def test_debug():
    from io import StringIO

    string = StringIO()
    sys.stderr = string
    debug(lambda: 'Hello World!')
    assert string.getvalue() == '\x1b[34m[py-backwards] DEBUG: Hello World!\n\x1b[0m'
    del string
    string = StringIO()
    debug(lambda: 'Hello World!')
    assert string.getvalue() == ''
    del string

# Generated at 2022-06-22 12:48:16.001579
# Unit test for function get_source
def test_get_source():
    def foo(a, b=1, c=1):
        pass

    assert get_source(foo) == 'def foo(\n    a,\n    b=1,\n    c=1,\n):\n    pass'

# Generated at 2022-06-22 12:48:19.841656
# Unit test for function debug
def test_debug():
    '''test debug function'''
    test_str = 'test'
    messages_mockup = messages.debug(test_str)
    def get_message():
        return test_str
    debug(get_message)
    messages.debug = messages_mockup
    settings.debug = False


# Generated at 2022-06-22 12:48:24.762858
# Unit test for function eager
def test_eager():
    import random
    @eager
    def rands(upto: int, times: int) -> Iterable[int]:
        for _ in range(times):
            yield random.randint(0, upto)
    assert rands(100, 10) == list(rands(100, 10))

