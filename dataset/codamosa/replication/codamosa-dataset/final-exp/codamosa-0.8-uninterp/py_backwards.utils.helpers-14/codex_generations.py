

# Generated at 2022-06-22 12:38:25.212557
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    def g():
        pass

    assert get_source(f) == 'def f():\n    pass\n'
    assert get_source(g) == 'def g():\n    pass\n'

# Generated at 2022-06-22 12:38:27.128282
# Unit test for function get_source
def test_get_source():
    def source_tester():
        pass
    assert get_source(source_tester) == "def source_tester():\n" \
                                        "    pass"

# Generated at 2022-06-22 12:38:28.791846
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source)



# Generated at 2022-06-22 12:38:33.032462
# Unit test for function get_source
def test_get_source():
    def function_1():
        a = 1
        b = 2
        return a + b

    def function_2():
        a = 1
        b = 2
        return a + b

    assert get_source(function_1) == get_source(function_2)

# Generated at 2022-06-22 12:38:34.345907
# Unit test for function eager
def test_eager():
    def f():
        yield 1
    g = eager(f)

    assert g() == [1]



# Generated at 2022-06-22 12:38:36.660264
# Unit test for function get_source
def test_get_source():
    """
    >>> fn = lambda arg: arg
    >>> get_source(fn).strip()
    'return arg'
    """

# Generated at 2022-06-22 12:38:38.461157
# Unit test for function eager
def test_eager():
    fn = lambda: range(3)
    assert eager(fn)() == [0, 1, 2]



# Generated at 2022-06-22 12:38:41.679381
# Unit test for function eager
def test_eager():
    @eager
    def get_numbers() -> Iterable[int]:
        yield 1
        yield 2
        yield 3

    assert get_numbers() == [1, 2, 3]
    assert isinstance(get_numbers(), list)

# Generated at 2022-06-22 12:38:46.459717
# Unit test for function get_source
def test_get_source():
    # This code is a little bit weird, but it works well.
    def function():
        x = 1
        y = 2 # comment
        return x + y

    assert get_source(function) == 'x = 1\ny = 2 # comment\nreturn x + y'

# Generated at 2022-06-22 12:38:49.226861
# Unit test for function get_source
def test_get_source():
    def some():
        if True:
            return True
    assert get_source(some) == 'if True:\n    return True\n'

# Generated at 2022-06-22 12:38:58.929286
# Unit test for function debug
def test_debug():
    from .contextmanager import capture_stderr
    from . import settings as module_settings
    settings = module_settings.settings

    message = 'Test debug message'

    settings.debug = False
    with capture_stderr() as stderr:
        debug(lambda: message)
    assert stderr.getvalue() == ''

    settings.debug = True
    with capture_stderr() as stderr:
        debug(lambda: message)
    assert stderr.getvalue() == messages.debug(message) + '\n'

# Generated at 2022-06-22 12:39:02.713182
# Unit test for function get_source
def test_get_source():
    def test():
        return 1

    # the test for \t symbol
    assert get_source(test) == 'return 1'
    assert get_source(get_source) == get_source(get_source)

# Generated at 2022-06-22 12:39:06.533533
# Unit test for function debug
def test_debug():
    message = 'Something happened'
    captured_output = io.StringIO()  # Create StringIO object
    sys.stderr = captured_output    #  and redirect stdout.
    debug(lambda: message)
    assert captured_output.getvalue() == messages.debug(message) + '\n'



# Generated at 2022-06-22 12:39:09.094556
# Unit test for function get_source
def test_get_source():
    def foo():
        a = 2
        b = 3
        print(a + b)

    expected = '''
a = 2
b = 3
print(a + b)
'''
    assert get_source(foo) == expected



# Generated at 2022-06-22 12:39:10.753906
# Unit test for function eager
def test_eager():
    def foo():
        yield 1
        yield 2
        yield 3

    assert eager(foo)() == [1, 2, 3]

# Generated at 2022-06-22 12:39:12.832146
# Unit test for function eager
def test_eager():
    def foo(s):
        for i in range(s):
            yield i

    assert list(foo(3)) == eager(foo)(3)

# Generated at 2022-06-22 12:39:16.016045
# Unit test for function get_source
def test_get_source():
    def test(): return 1
    if __name__ == '__main__':
        test()

    assert get_source(test) == 'def test(): return 1\n'

# Generated at 2022-06-22 12:39:17.397660
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == 'return 42'

# Generated at 2022-06-22 12:39:19.227162
# Unit test for function debug
def test_debug():
    messages.debug('hello')
    settings.debug = True
    debug(lambda: 'world')



# Generated at 2022-06-22 12:39:21.519873
# Unit test for function eager
def test_eager():
    result = [i * 2 for i in range(10000000)]
    assert list(eager(enumerate)(result)) == list(enumerate(result))

# Generated at 2022-06-22 12:39:30.784972
# Unit test for function debug
def test_debug():
    import mock

    @debug
    def a():
        return "foo"

    with mock.patch('sys.stderr.write'):
        settings.debug = True
        a()
        assert sys.stderr.write.call_count == 1
        settings.debug = False
        a()
        assert sys.stderr.write.call_count == 1



# Generated at 2022-06-22 12:39:33.995844
# Unit test for function eager
def test_eager():
    lst = None
    def inner():
        nonlocal lst
        lst.append(1)
        return lst
    lst = [0]
    assert eager(inner)() == [0, 1]

# Generated at 2022-06-22 12:39:36.469404
# Unit test for function debug
def test_debug():
    def test_debug_with_message():
        print('Test debugging message:')
        debug(lambda: 'Hello, world!')
    test_debug_with_message()

# Generated at 2022-06-22 12:39:39.861007
# Unit test for function get_source
def test_get_source():
    def test():
        return 1

    assert get_source(test) == 'return 1'
    n = 0
    def test2():
        return 2

    assert get_source(test2) == 'return 2'

# Generated at 2022-06-22 12:39:42.602611
# Unit test for function eager
def test_eager():
    def generator():
        for i in range(3):
            yield i

    assert eager(generator)() == [0, 1, 2]


# Generated at 2022-06-22 12:39:44.046126
# Unit test for function eager
def test_eager():
    assert eager(lambda: range(3))() == [0, 1, 2]

# Generated at 2022-06-22 12:39:46.728919
# Unit test for function get_source
def test_get_source():
    def foo():
        """
        foo docstring
        """
        a = 1
    assert get_source(foo) == dedent(foo.__doc__)



# Generated at 2022-06-22 12:39:53.255890
# Unit test for function debug
def test_debug():
    messages.debug = lambda message: "DEBUG: " + message
    from io import StringIO

    try:
        captured = StringIO()
        sys.stderr = captured
        settings.debug = True

        counter = [0]

        def get_message():
            counter[0] += 1
            return "Counter is: " + str(counter[0])

        debug(get_message)
        assert captured.getvalue() == "DEBUG: Counter is: 1\n"
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:56.525104
# Unit test for function get_source
def test_get_source():
    def foo(x):
        return x

    assert get_source(foo) == dedent("""
        def foo(x):
            return x
    """)

# Generated at 2022-06-22 12:39:59.301074
# Unit test for function eager
def test_eager():
    def get_it() -> Iterable[int]:
        for i in range(10):
            yield i

    assert eager(get_it)() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-22 12:40:03.814619
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'test')
        return True
    except:
        return False
# >>> test_debug()
# True
# >>>


# Generated at 2022-06-22 12:40:06.802196
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'hello')
    settings.debug = False
    debug(lambda: 'hello')

# Generated at 2022-06-22 12:40:09.675322
# Unit test for function get_source
def test_get_source():
    def foo():
        return 'Hello World'

    def foo1():
        return 'Hello World'

    assert get_source(foo) == get_source(foo1)



# Generated at 2022-06-22 12:40:11.920983
# Unit test for function get_source
def test_get_source():
    def example():
        def fn():
            pass
        return fn

    assert get_source(example) == 'def fn():\n    pass\n'

# Generated at 2022-06-22 12:40:14.426003
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass'



# Generated at 2022-06-22 12:40:23.028692
# Unit test for function debug
def test_debug():
    debug_messages: List[str]
    debug_messages = []
    backup = settings.debug

    def get_message() -> str:
        message: str
        message = 'This is a debug message'
        debug_messages.append(message)
        return message

    try:
        settings.debug = True
        debug(get_message)
        assert debug_messages == ['This is a debug message']
        settings.debug = False
        debug(get_message)
    finally:
        settings.debug = backup
    assert debug_messages == ['This is a debug message', 'This is a debug message']

# Generated at 2022-06-22 12:40:26.513686
# Unit test for function get_source
def test_get_source():
    """It should return source code of the function."""
    def fn_to_test():
        x = 'hello'
        return x
    assert get_source(fn_to_test) == "x = 'hello'\nreturn x\n"

# Generated at 2022-06-22 12:40:29.151241
# Unit test for function get_source
def test_get_source():

    def func():
        a = 1
        b = 2
        return a + b

    assert get_source(func) == '''a = 1
b = 2
return a + b'''

# Generated at 2022-06-22 12:40:31.561401
# Unit test for function get_source
def test_get_source():
    def func():
        a = 1
        a = 2

    assert get_source(func) == \
        """a = 1
a = 2"""

# Generated at 2022-06-22 12:40:32.589018
# Unit test for function eager
def test_eager():
    pass

# Generated at 2022-06-22 12:40:39.188647
# Unit test for function eager
def test_eager():
    # Define function
    def test(n: int) -> Iterable[int]:
        for i in range(n):
            yield i

    # Make test eager
    test_eager = eager(test)

    # Check that behavior is the same
    assert test(3) == test_eager(3)

# Generated at 2022-06-22 12:40:40.588110
# Unit test for function eager
def test_eager():
    assert eager(lambda: range(3))() == [0, 1, 2]



# Generated at 2022-06-22 12:40:44.990369
# Unit test for function debug
def test_debug():
    from ..conf import set_debug, get_debug

    def get_debug_message():
        return 'some debug message'

    set_debug(True)
    debug(get_debug_message)

    set_debug(False)
    debug(get_debug_message)



# Generated at 2022-06-22 12:40:46.650397
# Unit test for function get_source
def test_get_source():
    def test(a, b):
        pass

    assert get_source(test).startswith('def test(')

# Generated at 2022-06-22 12:40:52.610065
# Unit test for function get_source
def test_get_source():
    def f1():
        pass
    def f2():
        def f3():
            pass
    def f4():
        def f5():
            def f6():
                pass
    assert get_source(f1) == "def f1():\n    pass"
    assert get_source(f2) == "def f2():\n    def f3():\n        pass"
    assert get_source(f4) == "def f4():\n    def f5():\n        def f6():\n            pass"

# Generated at 2022-06-22 12:40:56.246506
# Unit test for function get_source
def test_get_source():
    def my_func():
        print('Hello')

    assert get_source(my_func) == 'print(\'Hello\')'
    assert get_source(test_get_source) != ''

# Generated at 2022-06-22 12:41:00.581299
# Unit test for function debug
def test_debug():
    args = []
    def get_message():
        args.append(1)
        return 'test'

    debug(get_message)
    assert len(args) == 0, 'message was not evaluated'

    settings.debug = True
    debug(get_message)
    assert args == [1], 'message was evaluated'

# Generated at 2022-06-22 12:41:04.815352
# Unit test for function get_source
def test_get_source():
    def test() -> None:
        def test_inner() -> None:
            pass
        pass
    result = get_source(test)

# Generated at 2022-06-22 12:41:06.848580
# Unit test for function get_source
def test_get_source():
    def f():
        def g():
            pass
    assert get_source(f).strip() == 'def g():\n    pass'

# Generated at 2022-06-22 12:41:08.145960
# Unit test for function eager
def test_eager():
    assert eager(range)(10) == list(range(10))

# Generated at 2022-06-22 12:41:17.961171
# Unit test for function debug
def test_debug():
    def get_message():
        return 'Hello world'
    sys_stderr = sys.stderr
    sys.stderr = ''
    debug(get_message)
    assert sys.stderr == ''
    settings.debug = True
    debug(get_message)
    assert sys.stderr
    sys.stderr = sys_stderr



# Generated at 2022-06-22 12:41:27.081419
# Unit test for function get_source

# Generated at 2022-06-22 12:41:30.025844
# Unit test for function debug
def test_debug():
    from .. import settings

    def test_function():
        settings.debug = True
        debug(lambda: 'debug_message')
        settings.debug = False
        debug(lambda: 'debug_message')
    test_function()

# Generated at 2022-06-22 12:41:31.387104
# Unit test for function debug
def test_debug():
    debug('foo')
    settings.debug = True
    debug('foo')

# Generated at 2022-06-22 12:41:34.206153
# Unit test for function debug
def test_debug():
    """Test function `debug`."""
    from ..conf import settings
    settings.debug = True
    debug(lambda: 'Sample message')

# Generated at 2022-06-22 12:41:36.780878
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == 'assert get_source(test_get_source) == \'"assert get_source(test_get_source) == \\\'test_get_source\\\'\\n\\\'"\'\n'



# Generated at 2022-06-22 12:41:44.560245
# Unit test for function get_source
def test_get_source():
    assert get_source(get_source) == dedent(
        '''
        def get_source(fn: Callable[..., Any]) -> str:
            "Returns source code of the function."
            source_lines = getsource(fn).split('\\n')
            padding = len(re.findall(r'^(\\s*)', source_lines[0])[0])
            return '\\n'.join(line[padding:] for line in source_lines)
        '''.lstrip()
    )


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:41:46.321052
# Unit test for function get_source
def test_get_source():
    def some_function():
        x = 1
        y = 2
        print(x + y)

    source = get_source(some_function)
    expected = '''x = 1
y = 2
print(x + y)
'''
    assert source == expected



# Generated at 2022-06-22 12:41:48.768348
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass

    assert get_source(test_func) == "def test_func():\n    pass"



# Generated at 2022-06-22 12:41:50.016131
# Unit test for function eager
def test_eager():
    result = [1, 2, 3]
    assert eager(lambda: result)() == result

# Generated at 2022-06-22 12:42:04.183327
# Unit test for function eager
def test_eager():
    @eager
    def test_func(a: List[int]) -> Iterable[int]:
        for i in range(0, 2):
            yield a[i]

    assert test_func([0, 1]) == [0, 1]



# Generated at 2022-06-22 12:42:07.342257
# Unit test for function get_source
def test_get_source():
    def test():
        """Test docstring"""
        pass

    expected = '"""Test docstring"""\n'
    source = get_source(test)
    assert source == expected

# Generated at 2022-06-22 12:42:11.497147
# Unit test for function get_source
def test_get_source():
    """Tests get_source function"""
    def source_test():
        """Function to test get_source with"""
        pass

    def padding_test():
        """Function to test get_source with"""
        pass

    lines = getsource(source_test).split('\n')
    assert lines == get_source(source_test).split('\n')

    lines = getsource(padding_test).split('\n')
    assert lines[1:] == get_source(padding_test).split('\n')

# Generated at 2022-06-22 12:42:14.887013
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f) == 'def f():\n    pass'



# Generated at 2022-06-22 12:42:16.516467
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        yield 1
        yield 2

    assert gen() == [1, 2]

# Generated at 2022-06-22 12:42:19.380268
# Unit test for function get_source
def test_get_source():
    def test(a: int, b: int) -> int:
        return a + b
    assert get_source(test) == 'return a + b'



# Generated at 2022-06-22 12:42:21.591183
# Unit test for function eager
def test_eager():
    @eager
    def i_generate_numbers():
        for i in range(10):
            yield i
    assert i_generate_numbers() == list(range(10))

# Generated at 2022-06-22 12:42:22.716745
# Unit test for function eager
def test_eager():
    """Unit test for function eager."""
    assert eager(range)(3) == [0, 1, 2]

# Generated at 2022-06-22 12:42:25.414403
# Unit test for function get_source
def test_get_source():
    import os
    import inspect
    import py_backwards
    path = inspect.getfile(py_backwards)
    source = open(path, 'r').read()
    src = get_source(py_backwards)
    assert src == source
# Test suite for function get_source

# Generated at 2022-06-22 12:42:28.301250
# Unit test for function get_source
def test_get_source():
    def function_with_source(x: int) -> int:
        return x * 2

    assert get_source(function_with_source) == "return x * 2"

# Generated at 2022-06-22 12:42:53.500393
# Unit test for function get_source
def test_get_source():
    import inspect
    def get_source(fn):
        return inspect.getsource(fn)

    def test_function():
        pass

    source = get_source(test_function).split('\n')
    assert source[0] == 'def test_function():'

if __name__ == "__main__":
    test_get_source()

# Generated at 2022-06-22 12:42:55.319065
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        yield 1
        yield 2

    assert foo() == [1, 2]

# Generated at 2022-06-22 12:43:05.445170
# Unit test for function get_source
def test_get_source():
    def test(arg1, arg2=''):
        """Test function.

        Arguments:
            arg1: first argument
            arg2: second argument
        """
        pass

    lines = get_source(test).split('\n')

    assert len(lines) == 4
    assert re.match(r'^def test', lines[0]) is not None
    assert (re.match(r'^    pass\s*$', lines[1]) is not None
            or re.match(r'^    return 0\s*$', lines[1]) is not None)
    assert len(lines) == 4
    assert re.match(r'^    Arguments:', lines[2]) is not None
    assert re.match(r'^        arg1: first argument', lines[3]) is not None

# Generated at 2022-06-22 12:43:11.277840
# Unit test for function debug
def test_debug():
    DEBUG_MESSAGE = "debug message"

    def get_message():
        return DEBUG_MESSAGE

    class DebugSettings:
        debug = False

    backup_settings = settings.debug

    try:
        settings.debug = DebugSettings
        sys.stderr = StringIO()
        debug(get_message)
        print(sys.stderr.getvalue())
        assert sys.stderr.getvalue() == ""

        settings.debug = True
        sys.stderr = StringIO()
        debug(get_message)
        print(sys.stderr.getvalue())
        assert sys.stderr.getvalue() == messages.debug(DEBUG_MESSAGE) + "\n"
    finally:
        settings.debug = backup_settings

# Generated at 2022-06-22 12:43:15.086239
# Unit test for function eager
def test_eager():
    # type: () -> None
    def foo():
        # type: () -> Iterable[int]
        yield 1
        yield 2
    assert eager(foo)() == [1, 2]

# Generated at 2022-06-22 12:43:25.015679
# Unit test for function get_source

# Generated at 2022-06-22 12:43:26.701238
# Unit test for function get_source
def test_get_source():
    def f(x):
        print(x)
    assert get_source(f) == 'print(x)'



# Generated at 2022-06-22 12:43:29.813760
# Unit test for function debug
def test_debug():
    with settings.override(debug=True):
        def get_message():
            return 'This is debug message'

        debug(get_message)
    with settings.override(debug=False):
        debug(get_message)

# Generated at 2022-06-22 12:43:32.707493
# Unit test for function eager
def test_eager():
    from collections.abc import Iterable
    @eager
    def foo() -> Iterable[int]:
        yield 1
        yield 2
        yield 3
    assert isinstance(foo(), list)
    assert foo() == [1, 2, 3]


# Generated at 2022-06-22 12:43:38.283994
# Unit test for function get_source
def test_get_source():
    def func(a, b, c=42, *args, d=None, **kwargs):
        return a + b + c + d
    assert func.__code__.co_argcount == 5
    assert func.__defaults__ == (42,)
    assert get_source(func) == dedent('''\
        def func(a, b, c=42, *args, d=None, **kwargs):
            return a + b + c + d
    ''')

# Generated at 2022-06-22 12:44:31.383613
# Unit test for function eager
def test_eager():
    # This function should be eager in order to pass the test
    @eager
    def gen():
        yield 1
        yield 2
    assert gen() == [1, 2]



# Generated at 2022-06-22 12:44:39.377584
# Unit test for function debug
def test_debug():
    global settings

    # Turn off debugging
    settings.debug = False

    # Assert that the message is not printed
    def set_message():
        '''This function returns non-empty string.'''
        return 'Message'
    debug(set_message)
    assert set_message() == 'Message'
    assert True

    # Turn on debugging
    settings.debug = True

    # Assert that the message is printed
    def set_message():
        '''This function returns non-empty string.'''
        return 'Message'
    debug(set_message)
    assert set_message() == 'Message'
    assert True

if __name__ == '__main__':
    test_debug()

# Generated at 2022-06-22 12:44:49.874502
# Unit test for function eager
def test_eager():
    from py_backwards.utils import get_source
    import ast
    import dis

    def f():
        for i in range(3):
            yield i

    assert get_source(eager(f)) == '\n'.join([
        '@wraps(fn)',
        'def wrapped(*args: Any, **kwargs: Any) -> List[T]:',
        '    return list(fn(*args, **kwargs))',
    ])

    compiled_eager = compile('def f():\n' + get_source(eager(f)), filename='<string>', mode='exec')
    exec(compiled_eager)

    assert f() == [0, 1, 2]

    def g():
        for i in range(3):
            yield i

    def h():
        for i in g():
            yield

# Generated at 2022-06-22 12:44:55.510585
# Unit test for function debug
def test_debug():
    import sys
    from io import StringIO
    from ..conf import settings
    settings.debug = True
    stdout = sys.stderr
    sys.stderr = StringIO()
    try:
        debug(lambda: 'Hello, World!')
        debug(lambda: 'Hello, World!')
        assert sys.stderr.getvalue() == messages.debug('Hello, World!') * 2
    finally:
        sys.stderr = stdout



# Generated at 2022-06-22 12:44:57.977697
# Unit test for function get_source
def test_get_source():
    def func():
        pass
    assert get_source(func) == 'def func():\n    pass'


# Generated at 2022-06-22 12:44:59.507881
# Unit test for function eager
def test_eager():
    assert eager(iter)([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-22 12:45:03.402976
# Unit test for function get_source
def test_get_source():
    def foo():
        """My function.

        Used for testing purposes.
        """

        def bar():
            return 'bar'
        return 'foo'

    expected = """def bar():
    return 'bar'
return 'foo'"""
    assert get_source(foo) == expected

# Generated at 2022-06-22 12:45:12.640916
# Unit test for function debug
def test_debug():
    import unittest
    import unittest.mock

    class Test(unittest.TestCase):
        def test_debug_with_debug_is_true(self):
            with unittest.mock.patch('sys.stderr') as stderr_mock:
                settings.debug = True
                debug(lambda: '42')
                stderr_mock.write.assert_called_once_with(
                    messages.debug('42') + '\n',
                )

        def test_debug_with_debug_is_false(self):
            with unittest.mock.patch('sys.stderr') as stderr_mock:
                settings.debug = False
                debug(lambda: '42')
                stderr_mock.write.assert_not_called()

    un

# Generated at 2022-06-22 12:45:16.118597
# Unit test for function get_source
def test_get_source():
    def fn_to_get_source():
        return 1 + 1
    assert get_source(fn_to_get_source) == 'return 1 + 1'

# Generated at 2022-06-22 12:45:18.245213
# Unit test for function get_source
def test_get_source():
    def test(): pass
    assert get_source(test) == 'test()'



# Generated at 2022-06-22 12:47:22.281175
# Unit test for function eager
def test_eager():
    def some_generator(how_many):
        for i in range(how_many):
            yield i

    result = eager(some_generator)(5)

    assert len(result) == 5
    assert result[0] == 0

# Generated at 2022-06-22 12:47:25.134298
# Unit test for function get_source
def test_get_source():
    def test_function(a, b):
        print(a, b)

    assert get_source(test_function) == "print(a, b)"

# Generated at 2022-06-22 12:47:26.691544
# Unit test for function debug
def test_debug():
    debug('test_debug')

# Generated at 2022-06-22 12:47:34.045000
# Unit test for function debug
def test_debug():
    import io
    capture = io.StringIO()
    sys.stderr = capture

    settings.debug = True
    debug(lambda: 'foo')
    assert 'foo' in capture.getvalue()

    capture = io.StringIO()
    sys.stderr = capture
    settings.debug = False
    debug(lambda: 'foo')
    assert 'foo' not in capture.getvalue()
    sys.stderr = sys.__stderr__



# Generated at 2022-06-22 12:47:35.745159
# Unit test for function get_source
def test_get_source():
    def add(a, b):
        return a + b

    assert get_source(add) == 'return a + b'

# Generated at 2022-06-22 12:47:47.049932
# Unit test for function debug
def test_debug():
    import re
    import sys
    from io import StringIO
    from ..conf import settings
    from ..utils import debug
    from contextlib import contextmanager

    test_case = [
        (

            'foo',
            'foo',
        ),

        (
            'foo\nbar\n',
            'foo\nbar\n',
        ),
    ]

    @contextmanager
    def capture_stdout():
        old_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            try:
                yield sys.stdout
            finally:
                sys.stdout = old_stdout
        finally:
            sys.stdout = old_stdout

    @contextmanager
    def capture_stderr():
        old_stderr = sys.stderr

# Generated at 2022-06-22 12:47:52.921608
# Unit test for function get_source
def test_get_source():
    def foo(a=''):
        """Function docstring."""
        pass
    assert get_source(foo) == 'def foo(a=\'\'):\n    """Function docstring."""\n    pass'

# Generated at 2022-06-22 12:48:00.316653
# Unit test for function debug
def test_debug():
    debug_info = []
    def fake_debug_message_generator():
        debug_info.append('hello world')
        return 'this should not be printed'

    debug(fake_debug_message_generator)
    assert len(debug_info) == 0

    with settings(debug=True):
        debug(fake_debug_message_generator)
        assert len(debug_info) == 1
        assert debug_info[0] == 'hello world'



# Generated at 2022-06-22 12:48:03.237298
# Unit test for function get_source
def test_get_source():
    def foo():
        if True:
            pass
    if get_source(foo) != 'if True:\n    pass':
        raise AssertionError

# Generated at 2022-06-22 12:48:06.395329
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            pass

        pass

    source = get_source(foo)
    assert '        def bar():' in source
    assert '        pass' in source

