

# Generated at 2022-06-22 12:38:23.836303
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        yield 1
        yield 2
        yield 3
    assert foo() == [1, 2, 3]

# Generated at 2022-06-22 12:38:29.039807
# Unit test for function get_source
def test_get_source():
    def get_source_test():
        # inner function
        var = 'test'
        return var
    expected = "var = 'test'\nreturn var"
    actual = get_source(get_source_test)
    assert actual == expected, actual


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:38:34.457082
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: "hello ")
        import sys
        assert sys.stderr.getvalue() == "\x1b[90m[DEBUG]\x1b[0m hello \n"
    finally:
        settings.debug = False
        from io import StringIO
        sys.stderr = StringIO()



# Generated at 2022-06-22 12:38:37.969151
# Unit test for function get_source
def test_get_source():
    def fn(arg: str) -> int:
        """Test function."""
        return len(arg)

    assert get_source(fn) == 'def fn(arg: str) -> int:\n    """Test function."""\n    return len(arg)'

# Generated at 2022-06-22 12:38:41.584606
# Unit test for function eager
def test_eager():
    def _to_test():
        return [int(input('> ')) for _ in range(4)]
    assert _to_test() == [0, 1, 2, 3]
    assert eager(_to_test)() == [0, 1, 2, 3]

# Generated at 2022-06-22 12:38:43.724313
# Unit test for function get_source
def test_get_source():
    def f(a, b=1, *args, **kwargs):
        return (a, b)

    assert get_source(f) == 'return (a, b)'

# Generated at 2022-06-22 12:38:48.231730
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    src = get_source(foo)
    assert src == 'def foo():\n    pass'

    def foo():
        def bar():
            pass
    src = get_source(foo)
    assert src == 'def foo():\n    def bar():\n        pass'



# Generated at 2022-06-22 12:38:50.856701
# Unit test for function eager
def test_eager():
    @eager
    def func():
        yield 1
        yield 2

    assert func() == [1, 2]

# Generated at 2022-06-22 12:38:55.554042
# Unit test for function get_source
def test_get_source():
    def fn(a, b):
        a, c = b, 'a'
        return a

    assert get_source(fn) == '''def fn(a, b):
    a, c = b, 'a'
    return a
'''

# Generated at 2022-06-22 12:38:57.726071
# Unit test for function get_source
def test_get_source():
    def foo():
        """
        This is docstring
        """
        pass

    assert get_source(foo) == "def foo():\n    pass"

# Generated at 2022-06-22 12:39:02.064523
# Unit test for function debug
def test_debug():
    def do_debug():
        debug('{1} {2}'.format(1, 2, 3))
    do_debug()

# Generated at 2022-06-22 12:39:03.702505
# Unit test for function get_source
def test_get_source():
    def get_source_of_me():
        def inside():
            pass

        pass


# Generated at 2022-06-22 12:39:06.443346
# Unit test for function get_source
def test_get_source():
    fn = """def test():
    print('abc')
    print('def')"""
    assert get_source(fn) == "print('abc')\nprint('def')"

test_get_source()

# Generated at 2022-06-22 12:39:08.823873
# Unit test for function eager
def test_eager():
    @eager
    def some_generator():
        yield 1
        yield 2
        yield 3

    assert some_generator() == [1, 2, 3]

# Generated at 2022-06-22 12:39:10.514485
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        yield 1
        yield 2
        yield 3
    assert gen() == [1, 2, 3]

# Generated at 2022-06-22 12:39:11.858372
# Unit test for function get_source
def test_get_source():
    assert get_source == 'def get_source()'



# Generated at 2022-06-22 12:39:14.013138
# Unit test for function get_source
def test_get_source():
    def test(a, b): pass
    assert get_source(test) == 'pass'



# Generated at 2022-06-22 12:39:18.838553
# Unit test for function debug
def test_debug():
    settings.debug = True
    calls_count = 0

    def get_message():
        nonlocal calls_count
        calls_count += 1
        return '{}'.format(calls_count)

    debug(get_message)

    assert calls_count == 1
    settings.debug = False

    debug(get_message)
    assert calls_count == 1



# Generated at 2022-06-22 12:39:27.011333
# Unit test for function debug
def test_debug():
    import tempfile
    import io
    with tempfile.TemporaryDirectory() as tmpdirname:
        settings.debug = False
        debug(lambda: 1/0)
        settings.debug = True

        fd, path = tempfile.mkstemp(dir=tmpdirname)
        fp = io.open(fd, 'w')
        sys.stderr = fp
        debug(lambda: 1/0)
        fp.close()
        result = io.open(path, 'r').read()
        sys.stderr = sys.__stderr__
        assert 'Exception: division by zero' in result
test_debug()

# Generated at 2022-06-22 12:39:31.061070
# Unit test for function get_source
def test_get_source():
    def foo():
        """docstring"""
        print("debug")
        return "some_result"

    assert get_source(foo) == '''"""docstring"""
print("debug")
return "some_result"'''



# Generated at 2022-06-22 12:39:41.413288
# Unit test for function debug
def test_debug():
    import io
    import sys
    import unittest.mock
    sys.stderr = io.StringIO()

    def wrap(call):
        settings.debug = True
        debug(lambda: call)
        settings.debug = False
        debug(lambda: call)

    with unittest.mock.patch('sys.stderr.write') as mock:
        wrap("test")
        assert mock.call_count == 1
        assert mock.call_args[0][0] == messages.debug("test")
        mock.reset_mock()
        wrap("test")
        assert mock.call_count == 0



# Generated at 2022-06-22 12:39:43.428610
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:39:52.313641
# Unit test for function debug
def test_debug():
    from .test_helper import TestCase, StdoutCapture

    class Test(TestCase):
        @staticmethod
        def debug_test() -> None:
            debug(lambda: 'test debug')

        def test(self) -> None:
            with StdoutCapture() as output:
                Test.debug_test()
            self.assertEqual(output.stderr, '')

        def test_debug(self) -> None:
            with StdoutCapture() as output:
                settings.debug = True
                Test.debug_test()
            self.assertIn('test debug', output.stderr)

    Test().run()

# Generated at 2022-06-22 12:39:54.344654
# Unit test for function eager
def test_eager():
    def foo():
        yield 1
        yield 2
    assert eager(foo)() == [1, 2]

# Generated at 2022-06-22 12:39:58.125901
# Unit test for function debug
def test_debug():
    global_settings = settings
    settings = settings._replace(debug=False)
    debug(lambda: 'hello')
    settings = settings._replace(debug=True)
    debug(lambda: 'hello')
    settings = global_settings



# Generated at 2022-06-22 12:40:01.374405
# Unit test for function eager
def test_eager():
    assert eager(lambda: (1, 2, 3))() == [1, 2, 3]
    assert eager(lambda: iter((2, 3)))() == [2, 3]

# Generated at 2022-06-22 12:40:03.291858
# Unit test for function get_source
def test_get_source():
    def foo():
        print('Hello')

    assert get_source(foo) == 'print(\'Hello\')'



# Generated at 2022-06-22 12:40:07.450023
# Unit test for function get_source
def test_get_source():
    def test_function():
        # Function body.
        pass

    expected_source = '''def test_function():
    # Function body.
    pass'''
    assert get_source(test_function) == expected_source

# Generated at 2022-06-22 12:40:09.836980
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass'

    def bar():
        pass
    assert get_source(bar) == 'def bar():\n    pass'

# Generated at 2022-06-22 12:40:12.105250
# Unit test for function get_source
def test_get_source():
    def foo():
        """This is docstring.

        This is more docstring.
        """


# Generated at 2022-06-22 12:40:18.128329
# Unit test for function eager
def test_eager():
    def gen_test():
        i = 0
        while i < 3:
            yield i
            i += 1
    assert eager(gen_test)() == [0, 1, 2]



# Generated at 2022-06-22 12:40:21.547503
# Unit test for function get_source
def test_get_source():
    def f(x: int) -> int:
        return x
    assert get_source(f) == dedent('''
    def f(x: int) -> int:
        return x
    ''')

# Generated at 2022-06-22 12:40:25.980118
# Unit test for function get_source
def test_get_source():
    from inspect import getsource
    from . import VariablesGenerator

    def f():
        x = 1
        y = 2
        return x + y

    assert get_source(f) == getsource(f)


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:40:29.097518
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2
        yield 3

    assert eager(f)() == [1, 2, 3]

# Generated at 2022-06-22 12:40:32.457122
# Unit test for function debug
def test_debug():
    debug_message = 'Debug message'
    sys.stderr.write = fake_write
    sys.stdin.read = lambda: '1'
    debug(lambda: debug_message)
    print(output)


output = ''

# Generated at 2022-06-22 12:40:36.488173
# Unit test for function debug
def test_debug():
    from unittest.mock import patch

    def mock_print(*args, **kwargs):
        pass

    with patch('sys.stderr', new=mock_print):
        debug(lambda: 'test')
        settings.debug = True
        debug(lambda: 'test')

# Generated at 2022-06-22 12:40:39.641459
# Unit test for function eager
def test_eager():
    @eager
    def power(base: int) -> Iterable[int]:
        while True:
            yield base ** 2
    assert power(2) == [4, 4, 4, 4, 4]

# Generated at 2022-06-22 12:40:47.418485
# Unit test for function debug
def test_debug():
    with patch('sys.stderr', new_callable=TextIOWrapper) as mock_stderr:
        with tempfile.TemporaryFile('w+') as mock_temporary_file:
            mock_stderr.name = mock_temporary_file.name

            debug(lambda: 'Hello')
            mock_temporary_file.seek(0)
            assert mock_temporary_file.read() == \
                   '\x1b[38;5;3m[py_backwards] Hello\x1b[0m\n'



# Generated at 2022-06-22 12:40:50.795496
# Unit test for function get_source
def test_get_source():
    def f1():
        def f2():
            x = 1
        pass
    f2 = f1.__code__.co_consts[1]
    assert get_source(f2) == 'x = 1'

# Generated at 2022-06-22 12:40:53.209008
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:40:59.724427
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass

    assert get_source(test_func) == 'def test_func():\n    pass'



# Generated at 2022-06-22 12:41:02.268859
# Unit test for function eager
def test_eager():
    a = [1,2,3]
    def fn():
        for item in a:
            yield item
    assert fn() == [1,2,3]

# Generated at 2022-06-22 12:41:05.984066
# Unit test for function get_source
def test_get_source():
    def fn():
        if True:
            pass
        else:
            pass
    assert get_source(fn) == '    if True:\n        pass\n    else:\n        pass'



# Generated at 2022-06-22 12:41:09.616090
# Unit test for function get_source
def test_get_source():
    lines = get_source(test_get_source).split('\n')
    assert lines[0].startswith('def test_get_source():')
    assert not lines[1].strip()
    assert lines[2].startswith('    ')

# Generated at 2022-06-22 12:41:12.382214
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    source = get_source(test_function)

    assert source == inspect.getsource(test_function).strip()

# Generated at 2022-06-22 12:41:18.157780
# Unit test for function debug
def test_debug():
    from ..conf import get_settings
    settings.update(debug=True)
    counter = 0
    debug(lambda: 'test' + str(counter))
    assert counter == 1
    settings.update(debug=False)
    debug(lambda: 'test')
    settings.update(debug=True)
    debug(lambda: 'test' + str(counter))
    assert counter == 2
    settings.update(debug=False)
    settings = get_settings()

# Generated at 2022-06-22 12:41:22.570166
# Unit test for function debug
def test_debug():
    from io import StringIO
    from contextlib import redirect_stderr
    with StringIO() as buffer, redirect_stderr(buffer):
        debug(lambda: 'testing debug function')
        assert 'testing debug function' == buffer.getvalue().strip(), 'Debug message is incorrect'

# Generated at 2022-06-22 12:41:26.788869
# Unit test for function eager
def test_eager():
    assert eager([2, 3, 4, 7])(eager(frozenset([1, 2, 3]))) == [1, 2, 3, 2, 3, 4, 7]
    assert eager(frozenset([1, 2, 3]))() == [1, 2, 3]



# Generated at 2022-06-22 12:41:28.501357
# Unit test for function get_source
def test_get_source():
    def test_fn():
        pass

    assert get_source(test_fn) == 'pass'



# Generated at 2022-06-22 12:41:38.153154
# Unit test for function debug
def test_debug():
    class TestPrint:
        def __init__(self):
            self.message = None
        def __call__(self, text: str) -> None:
            self.message = text

    print_stderr = TestPrint()
    backup_print = sys.stderr
    sys.stderr = print_stderr
    settings.debug = False
    debug(lambda: "debug")
    assert print_stderr.message is None

    settings.debug = True
    debug(lambda: "debug")
    assert print_stderr.message is not None
    assert "debug" in print_stderr.message

    sys.stderr = backup_print

# Generated at 2022-06-22 12:41:50.914110
# Unit test for function debug
def test_debug():
    settings.debug = True
    message = 'Test'
    debug(lambda: message)
    settings.debug = False
    debug(lambda: message)



# Generated at 2022-06-22 12:41:52.796752
# Unit test for function eager
def test_eager():
    assert eager(range)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:41:55.416271
# Unit test for function debug
def test_debug():
    for enabled in (True, False):
        settings.debug = enabled
        debug(lambda: 'unittest_debug')
        assert settings.debug == enabled


# Generated at 2022-06-22 12:41:59.484440
# Unit test for function debug
def test_debug():
    with open('test.debug', 'w') as f:
        with redirect_stdout(f):
            debug(lambda: 'Message for debug')
    with open('test.debug', 'r') as f:
        assert f.read() == 'Debug: Message for debug\n'
    os.remove('test.debug')

# Generated at 2022-06-22 12:42:02.881896
# Unit test for function get_source
def test_get_source():
    def foo():
        """Docstring."""
        a = 1
        b = 2
        return a + b

    actual = get_source(foo)

# Generated at 2022-06-22 12:42:04.890813
# Unit test for function debug
def test_debug():
    for debug_mode in [False, True]:
        settings.debug = debug_mode
        debug(lambda: 'debug mode: ' + str(debug_mode))

# Generated at 2022-06-22 12:42:08.629840
# Unit test for function eager
def test_eager():
    """Test function eager."""
    def generator():
        yield 1
        yield 2
        yield 3

    assert eager(generator)() == [1, 2, 3]

# Generated at 2022-06-22 12:42:10.818981
# Unit test for function debug
def test_debug():
    with pytest.raises(RuntimeError):
        def get_message():
            raise RuntimeError
        debug(get_message)

# Generated at 2022-06-22 12:42:12.429132
# Unit test for function get_source
def test_get_source():
    def test(): pass
    assert get_source(test) == 'def test(): pass'



# Generated at 2022-06-22 12:42:15.002426
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        yield 1
        yield 2
        yield 3
    assert gen() == [1,2,3]

# Generated at 2022-06-22 12:42:38.129617
# Unit test for function debug
def test_debug():
    print('Running tests for function `debug`... ', end='')
    settings.debug = False
    debug(lambda: 'test')
    settings.debug = True
    debug(lambda: 'test')
    assert 1 == 1
    print('OK')



# Generated at 2022-06-22 12:42:42.021723
# Unit test for function eager
def test_eager():
    from unittest.mock import MagicMock

    iterable = MagicMock()
    iterable.__iter__.return_value = iter([1, 2, 3])
    iterable.__len__.return_value = 0

    assert eager(iterable)() == [1, 2, 3]



# Generated at 2022-06-22 12:42:44.141351
# Unit test for function get_source
def test_get_source():
    def foo(x: Any = 1) -> Any:
        return x

    assert get_source(foo).strip() == 'return x'

# Generated at 2022-06-22 12:42:47.312533
# Unit test for function get_source
def test_get_source():
    def useless_function():
        pass

    source = get_source(useless_function)

    assert source == 'def useless_function():'

# Generated at 2022-06-22 12:42:49.796582
# Unit test for function debug
def test_debug():
    class Test:
        debug_message = 'test'
    
    test = Test()

    def get_message():
        return test.debug_message

    debug(get_message)

# Generated at 2022-06-22 12:42:50.731940
# Unit test for function debug
def test_debug():
    assert debug.__name__ == 'debug'

# Generated at 2022-06-22 12:42:54.148903
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)
    assert source == r'''source = get_source(test_get_source)
assert source == r''' + "'''" + r'''
source = get_source(test_get_source)
assert source == r''' + "'''" + r'''
source
'''

# Generated at 2022-06-22 12:42:58.196222
# Unit test for function eager
def test_eager():
    def empty() -> Iterable[int]:
        return []

    def some() -> Iterable[int]:
        return [1, 2, 3]

    assert eager(empty)() == []
    assert eager(some)() == [1, 2, 3]


# Generated at 2022-06-22 12:42:59.386311
# Unit test for function eager
def test_eager():
    assert eager(lambda: iter([0, 1]))() == [0, 1]



# Generated at 2022-06-22 12:43:02.764560
# Unit test for function debug
def test_debug():
    msg = 'hello'
    buff = io.StringIO()
    with contextlib.redirect_stdout(buff):
        with contextlib.redirect_stderr(buff):
            debug(lambda: msg)
    assert msg in buff.getvalue()

# Generated at 2022-06-22 12:43:59.767662
# Unit test for function get_source
def test_get_source():  # pragma: no cover
    def test(a: int, b: int) -> int:
        return a + b
    print(get_source(test))


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:44:02.763446
# Unit test for function get_source
def test_get_source():
    def foo():
        print(2)
        print(3)
    assert get_source(foo) == 'print(2)\nprint(3)'


# Generated at 2022-06-22 12:44:12.154125
# Unit test for function get_source
def test_get_source():
    test_source_1 = '''
    def test_source_fn(arg1, arg2):
        return arg1 + arg2
    '''
    test_source_2 = '''
    def test_source_fn(arg1, arg2):
        return arg1 + arg2
    '''
    test_source_3 = '''
    def test_source_fn(arg1, arg2):
        return arg1 + arg2
    '''
    test_source_1 = get_source(test_source_1)
    assert test_source_1 == test_source_2
    assert test_source_2 == test_source_3

# Generated at 2022-06-22 12:44:14.003490
# Unit test for function eager
def test_eager():
    def test():
        yield 1
        yield 2
    assert eager(test)() == [1, 2]

# Generated at 2022-06-22 12:44:15.785609
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'pass'



# Generated at 2022-06-22 12:44:17.518309
# Unit test for function get_source
def test_get_source():
    def some_function():
        pass

    assert get_source(some_function) == 'def some_function():'

# Generated at 2022-06-22 12:44:18.855549
# Unit test for function get_source
def test_get_source():
    def hello(): pass

    assert get_source(hello) == 'def hello(): pass'

# Generated at 2022-06-22 12:44:25.449232
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: '1' + '2')
    with mock.patch('sys.stderr', new=StringIO()) as mock_stderr:
        debug(lambda: '3' + '4')
    settings.debug = False
    assert mock_stderr.getvalue() == '\x1b[31mDEBUG: 34\x1b[39m\n'


# Generated at 2022-06-22 12:44:30.423662
# Unit test for function eager
def test_eager():
    from random import randrange

    @eager
    def test():
        for _ in range(randrange(2, 5)):
            yield 1

    x = test()
    assert x

    if not x:
        raise Exception('Test failed')

    assert len(x) == randrange(2, 5)
    assert all(y == 1 for y in x)



# Generated at 2022-06-22 12:44:38.631755
# Unit test for function get_source
def test_get_source():
    # pylint: disable=unused-argument
    def test1(a: Any, *args: Any, **kwargs: Any) -> None:
        """Docstring."""
        b = 'a'
        print('a')
    def test2(a: Any, *args: Any, **kwargs: Any) -> None:
        """Docstring."""
        print('a')
    def test3(a: Any, *args: Any, **kwargs: Any) -> None:
        """Docstring."""
        b = 'a'
        print('a')

    def baz_foo(a: Any) -> Any:
        return 1

    def baz(b: Any) -> Any:
        return baz_foo(b)

    source_lines = get_source(test1).split('\n')
   

# Generated at 2022-06-22 12:46:35.388379
# Unit test for function eager
def test_eager():
    class A:
        @eager
        def iterable(self, n: int) -> Iterable[int]:
            i = 0
            while i < n:
                yield i
                i += 1

        def iterable_not_eager(self, n: int) -> Iterable[int]:
            i = 0
            while i < n:
                yield i
                i += 1

        @eager
        @staticmethod
        def static(n: int) -> Iterable[int]:
            i = 0
            while i < n:
                yield i
                i += 1

        @classmethod
        @eager
        def cls(cls, n: int) -> Iterable[int]:
            i = 0
            while i < n:
                yield i
                i += 1


# Generated at 2022-06-22 12:46:41.482612
# Unit test for function debug
def test_debug():
    from unittest import mock
    import sys

    settings.debug = True
    stdout = sys.stderr
    message = 'Hello, World!'
    assert debug(lambda: message) is None
    assert stdout.write.call_count == 1
    assert stdout.write.call_args[0][0] == messages.debug(message)


# Generated at 2022-06-22 12:46:48.151348
# Unit test for function eager
def test_eager():
    def check(fn):
        assert eager(fn)() == [1, 2, 3]
        # Check that eager preserves docstring
        assert eager(fn).__doc__ == 'Some docstring'

    def fn():
        '''Some docstring'''
        yield 1
        yield 2
        yield 3

    check(fn)

    # Check that eager works if the function has args and kwargs
    def fn1(a, b='b'):
        yield a
        yield b
        yield 'c'

    check(fn1)



# Generated at 2022-06-22 12:46:50.567757
# Unit test for function get_source
def test_get_source():
    import re
    from .test_fixtures import function_with_some_whitespace

    assert re.match(r'x = 0\n', get_source(function_with_some_whitespace))

# Generated at 2022-06-22 12:46:53.919436
# Unit test for function get_source
def test_get_source():
    def test_function():  # pylint: disable=unused-variable
        pass

    assert get_source(test_function) == 'def test_function():\n    pass'



# Generated at 2022-06-22 12:46:55.397807
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f) == 'def f():'

# Generated at 2022-06-22 12:46:58.149863
# Unit test for function eager
def test_eager():
    @eager
    def add_one(x: int) -> Iterable[int]:
        yield x + 1
        yield x + 20

    assert add_one(2) == [3, 22]

# Generated at 2022-06-22 12:46:59.154156
# Unit test for function debug
def test_debug():
    def _get_message():
        return 'foo'

    debug(_get_message)

# Generated at 2022-06-22 12:47:01.610641
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    source = get_source(foo)
    assert source.startswith('def foo():')



# Generated at 2022-06-22 12:47:04.523335
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    def expected_function():
        pass

    assert get_source(test_function) == getsource(expected_function)