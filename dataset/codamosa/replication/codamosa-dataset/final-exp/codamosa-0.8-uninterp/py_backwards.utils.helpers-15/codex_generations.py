

# Generated at 2022-06-22 12:38:20.558882
# Unit test for function eager
def test_eager():
    @eager
    def f():
        yield 1
        yield 2

    assert f() == [1, 2]

# Generated at 2022-06-22 12:38:23.396518
# Unit test for function eager
def test_eager():
    fn = lambda: (i for i in [1, 2, 3])
    assert eager(fn)() == [1, 2, 3]

# Generated at 2022-06-22 12:38:25.769858
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'def fn():\n    pass\n'



# Generated at 2022-06-22 12:38:28.792399
# Unit test for function eager
def test_eager():
    def test(n):
        for i in range(n):
            yield i
    assert eager(test)(3) == [0, 1, 2]

# Generated at 2022-06-22 12:38:30.915991
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass

    assert get_source(test_func) == 'def test_func():\n    pass'

# Generated at 2022-06-22 12:38:34.833093
# Unit test for function get_source
def test_get_source():
    def hello():
        return 6

    if __name__ == '__main__':
        def main():
            return 5

    assert get_source(hello) == 'return 6\n'
    assert get_source(main) == 'return 5\n'

# Generated at 2022-06-22 12:38:36.272696
# Unit test for function debug
def test_debug():
    def get_message():
        return 'test message'
    debug(get_message)

# Generated at 2022-06-22 12:38:37.319549
# Unit test for function debug
def test_debug():
    debug(lambda: 'test message')



# Generated at 2022-06-22 12:38:39.102998
# Unit test for function eager
def test_eager():
    @eager
    def get_range(n: int) -> Iterable[int]:
        yi

# Generated at 2022-06-22 12:38:42.908824
# Unit test for function get_source
def test_get_source():
    def func_to_test():
        pass
    func_to_test.__name__ = 'test_func'
    lines = get_source(func_to_test).split('\n')
    assert(lines[0] == 'def test_func():')
    assert(lines[-1] == '    pass')

# Generated at 2022-06-22 12:38:48.188198
# Unit test for function eager
def test_eager():
    from collections.abc import Iterable

    @eager
    def f(a: Iterable[int]) -> Iterable[int]:
        return a

    assert isinstance(f([1, 2]), list)

# Generated at 2022-06-22 12:38:58.758946
# Unit test for function debug
def test_debug():
    import os
    import sys
    import io
    import tempfile
    import unittest.mock

    class Test(unittest.TestCase):
        def setUp(self):
            self.temp_file = tempfile.TemporaryFile('w+')
            self.stdout = sys.stderr
            sys.stderr = self.temp_file
            settings.debug = False

        def tearDown(self):
            sys.stderr = self.stdout
            self.temp_file.close()

        def test_debug_basic(self):
            debug(lambda: 'test debug')
            self.temp_file.seek(0)
            self.assertEqual(self.temp_file.read(), '')
            settings.debug = True
            debug(lambda: '')

# Generated at 2022-06-22 12:39:05.819107
# Unit test for function get_source
def test_get_source():
    def simple(): pass
    def complex():
        def nested(): pass

    assert re.match(r'\n?^def simple\(\) -> None: pass\n?\Z', get_source(simple))
    assert re.match(r'\n?^def complex\(\) -> None:$\n?^\s*def nested\(\) -> None: pass\n?\Z', get_source(complex))


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:39:08.207180
# Unit test for function get_source
def test_get_source():
    def foo():
        bar = 1

    assert get_source(foo) == 'bar = 1'


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:39:10.920804
# Unit test for function get_source
def test_get_source():
    source = "def foo():\n    return 1"
    source2 = "    def foo():\n        return 1"

    def foo():
        return 1

    assert get_source(foo) == source
    assert get_source(foo) == source2

# Generated at 2022-06-22 12:39:17.199706
# Unit test for function eager
def test_eager():
    @eager
    def simple_eager():
        yield 1
        yield 2
    assert simple_eager() == [1, 2]

    def simple_eager_with_argument(argument):
        @eager
        def simple_eager():
            yield 1
            yield 2
            yield argument
        return simple_eager()
    assert simple_eager_with_argument(42) == [1, 2, 42]



# Generated at 2022-06-22 12:39:21.922583
# Unit test for function debug
def test_debug():
    with patch('sys.stderr') as mock_stderr:
        settings.debug = True
        debug(lambda: 'foobar')
        assert mock_stderr.write.call_count == 1
        assert mock_stderr.write.call_args[0] == (messages.debug('foobar'),)
        settings.debug = False

# Generated at 2022-06-22 12:39:24.254755
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass'


# Generated at 2022-06-22 12:39:27.104994
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)
    assert source.startswith('def test_get_source():')

# Generated at 2022-06-22 12:39:29.476630
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'def test_function():\n    pass'

# Generated at 2022-06-22 12:39:35.521608
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:39:37.999246
# Unit test for function get_source
def test_get_source():
    def foo():
        """Function doc"""
        print('Hello')


# Generated at 2022-06-22 12:39:43.527492
# Unit test for function get_source
def test_get_source():
    global a
    a = 1
    @get_source
    def aa():
        global b
        b = 2
        return 'hello'

    @get_source
    def bb():
        c = 3
        return 'hello'

    assert aa == '\nreturn \'hello\''
    assert bb == '\nc = 3\nreturn \'hello\''
    assert b == 2

# Generated at 2022-06-22 12:39:45.661524
# Unit test for function get_source
def test_get_source():
    def foo():
        return True

    def bar():
        return True

    assert get_source(foo) == get_source(bar)

# Generated at 2022-06-22 12:39:47.718436
# Unit test for function eager
def test_eager():
    def foo() -> Iterable[int]:
        yield 1
        yield 2
        yield 3

    assert eager(foo)() == [1, 2, 3]

# Generated at 2022-06-22 12:39:48.699193
# Unit test for function debug
def test_debug():
    debug(lambda: 'info')


# Tests

# Generated at 2022-06-22 12:39:53.756595
# Unit test for function debug
def test_debug():
    collected = []

    def get_message() -> str:
        return 'Hello!'

    def test():
        debug(get_message)

    output = sys.stderr
    sys.stderr = collected
    settings.debug = True
    test()
    assert collected[0] == messages.debug(get_message())
    sys.stderr = output

# Generated at 2022-06-22 12:39:57.450776
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    assert not get_source(function)

    def function():
        pass

    assert not get_source(function)
    #assert get_source(function).startswith('    pass')

# Generated at 2022-06-22 12:40:06.339471
# Unit test for function debug
def test_debug():
    from ..conf import settings
    from . import messages
    from mock import Mock

    debug_message = 'This is a debug message'
    print_mock = Mock()
    stderr_mock = Mock()

    def template_for_debug_message(debug_message: str) -> str:
        return 'Debug: {}'.format(debug_message)

    def get_message() -> str:
        return debug_message

    template_wrapper = ''.join(template_for_debug_message('').split(' '))
    non_template_wrapper = ''.join(template_for_debug_message(debug_message).split(' '))


# Generated at 2022-06-22 12:40:08.785100
# Unit test for function eager
def test_eager():

    @eager
    def l():
        yield 1
        yield 2
        yield 3

    assert l() == [1, 2, 3]

# Generated at 2022-06-22 12:40:16.935856
# Unit test for function get_source
def test_get_source():
    def f():
        def g():
            """
            Function that returns 23.
            """

            return 23
        return g
    assert get_source(f) == inspect.getsource(f)

# Generated at 2022-06-22 12:40:19.461097
# Unit test for function get_source
def test_get_source():
    source1 = get_source(test_get_source)
    source2 = get_source(test_get_source.__call__)
    assert source1 == source2

# Generated at 2022-06-22 12:40:24.103236
# Unit test for function debug
def test_debug():
    debug_log = []

    def get_msg():
        debug_log.append(1)
        return ''

    debug(get_msg)
    assert debug_log == []

    settings.debug = True
    debug(get_msg)
    assert debug_log == [1]



# Generated at 2022-06-22 12:40:26.319949
# Unit test for function get_source
def test_get_source():
    def test_function():
        return 'Hello World'
    assert get_source(test_function) == 'return \'Hello World\''

# Generated at 2022-06-22 12:40:28.976676
# Unit test for function debug
def test_debug():
    def test():
        debug(lambda: "test")

    debug(lambda: "asdf")

# Generated at 2022-06-22 12:40:31.763564
# Unit test for function get_source
def test_get_source():
    def hello():
        print('hello world')

    def foo():
        return 42


    assert get_source(hello) == "print('hello world')"
    assert get_source(foo) == 'return 42'

# Generated at 2022-06-22 12:40:33.834547
# Unit test for function eager
def test_eager():
    assert eager(lambda: (1, 2, 3))() == [1, 2, 3]


# Generated at 2022-06-22 12:40:36.127848
# Unit test for function get_source
def test_get_source():
    def foo():
        """Function."""
        pass

    assert get_source(foo) == "def foo():\n    pass\n"

# Generated at 2022-06-22 12:40:45.070584
# Unit test for function debug
def test_debug():
    messages.debug = lambda mes: mes
    warn_ = []
    print_ = []

    class X:
        def __init__(self):
            self.x = 123

    def original(x: X) -> None:
        print(x.x)

    def traced(x: X) -> None:
        print_[:] = []
        warn_[:] = []

        def get_message():
            return 'x.x'

        debug(get_message)
        try:
            original(x)
        except Exception:
            warn_.append(1)
        assert len(warn_) == 0
        assert print_ == [x.x]

    traced(X())



# Generated at 2022-06-22 12:40:51.742853
# Unit test for function debug
def test_debug():
    import io
    from contextlib import redirect_stderr

    f = io.StringIO()
    with redirect_stderr(f):
        debug(lambda: 'test message')
    assert f.getvalue() == '\n'

    settings.debug = True
    f = io.StringIO()
    with redirect_stderr(f):
        debug(lambda: 'test message')
    assert f.getvalue() == '\nDEBUG: test message\n'

# Generated at 2022-06-22 12:41:02.602461
# Unit test for function eager
def test_eager():
    @eager
    def iterable() -> Iterable[int]:
        return range(3)
    assert iterable() == [0, 1, 2]

# Generated at 2022-06-22 12:41:05.481648
# Unit test for function get_source
def test_get_source():
    def a():
        def b():
            pass
    assert get_source(a) == 'def b():\n    pass\n'

# Generated at 2022-06-22 12:41:08.257802
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'test')
        debug(lambda: 'test2')
    finally:
        settings.debug = False



# Generated at 2022-06-22 12:41:09.578097
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'hi')

# Generated at 2022-06-22 12:41:18.706764
# Unit test for function debug
def test_debug():
    import unittest.mock
    mock_print = unittest.mock.Mock()
    with unittest.mock.patch('sys.stderr.write', mock_print):
        debug(lambda: 'foo')
        mock_print.assert_not_called()
    with unittest.mock.patch('sys.stderr.write', None):
        settings.debug = True
        debug(lambda: 'foo')
        assert mock_print.call_args[0][0].startswith(messages.DEBUG_COLOR)
        assert mock_print.call_args[0][0].endswith('foo\n')
        settings.debug = False

# Generated at 2022-06-22 12:41:21.043631
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert(get_source(foo).strip() == 'def foo():')



# Generated at 2022-06-22 12:41:26.304754
# Unit test for function debug
def test_debug():
    class MyException(Exception):
        pass

    caught_exception = None

    def get_message():
        try:
            raise MyException()
        except Exception as e:
            raise

    def set_exception(e: Exception) -> None:
        nonlocal caught_exception
        caught_exception = e

    debug(get_message)
    assert caught_exception is None

    settings.debug = True
    debug(get_message)

    assert isinstance(caught_exception, MyException)



# Generated at 2022-06-22 12:41:27.604331
# Unit test for function get_source
def test_get_source():
    def f(): pass
    assert get_source(f) == "def f(): pass"

# Generated at 2022-06-22 12:41:29.449750
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'def foo():\n    pass'

# Generated at 2022-06-22 12:41:34.564044
# Unit test for function get_source
def test_get_source():
    def func(arg1, arg2='keyword'):
        """
        This is docstring.
        """
        return arg1 + arg2
    assert get_source(func) == '''def func(arg1, arg2='keyword'):
    """
    This is docstring.
    """
    return arg1 + arg2'''

# Generated at 2022-06-22 12:41:57.248831
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    assert get_source(function) == 'def function():\n    pass'

    def function_with_empty_line():

        pass

    assert get_source(function_with_empty_line) == 'def function_with_empty_line():\n\n    pass'



# Generated at 2022-06-22 12:41:58.226827
# Unit test for function eager
def test_eager():
    def foo():
        yield 1
        yield 2
        yield 3

    assert eager(foo)() == [1, 2, 3]

# Generated at 2022-06-22 12:42:00.691065
# Unit test for function debug
def test_debug():
    for func in lambda: None, str:
        func.__name__ = 'test'
    debug(lambda: 'message')


# Generated at 2022-06-22 12:42:03.602916
# Unit test for function eager
def test_eager():
    def numbers():
        yield 1
        yield 2
        yield 3

    assert eager(numbers)() == [1, 2, 3]

# Generated at 2022-06-22 12:42:09.322980
# Unit test for function get_source
def test_get_source():
    def add_1_to_2():
        return 1 + 2

    assert(get_source(add_1_to_2) == "return 1 + 2")

    def add_1_to_2():
        return 1 + 2

    assert(get_source(add_1_to_2) == "return 1 + 2")


# Generated at 2022-06-22 12:42:13.430622
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass

    assert get_source(test_function) == 'def test_function():\n    pass'

    def test_function_indent():
        return True

    assert get_source(test_function_indent) == \
        'def test_function_indent():\n    return True'

# Generated at 2022-06-22 12:42:15.279726
# Unit test for function get_source
def test_get_source():
    def fn():
        return 1

    source = get_source(fn)
    assert source == 'return 1'

# Generated at 2022-06-22 12:42:19.520479
# Unit test for function eager
def test_eager():
    @eager
    def range_eager(n: int) -> Iterable[int]:
        for i in range(n):
            yield i
    assert range_eager(5) == [0, 1, 2, 3, 4]
    assert range_eager(0) == []


# Generated at 2022-06-22 12:42:22.506634
# Unit test for function get_source
def test_get_source():
    from .fixtures.get_source import source, source_multi_line

    def source_function():
        pass

    assert get_source(source_function) == source
    assert get_source(source_multi_line) == source_multi_line

# Generated at 2022-06-22 12:42:29.557883
# Unit test for function get_source
def test_get_source():
    def t(a, b, c=1, d=2, e=3, f=4, g=5, h=6, i=7, j=8, k=9, l=10, m=11,
          n=12, o=13, p=14, q=15, r=16, s=17, t=18, u=19, v=20, w=21, x=22,
          y=23, z=24, aa=25, bb=26, cc=27, dd=28, ee=29, ff=30):
        pass

    source = get_source(t)


# Generated at 2022-06-22 12:43:17.965952
# Unit test for function get_source
def test_get_source():
    def some_function(first, second, third):
        print('some_function')
        print('some_function')
    get_source(some_function)

# Generated at 2022-06-22 12:43:20.166316
# Unit test for function eager
def test_eager():
    @eager
    def test(argument):
        for i in range(argument):
            yield i
    assert test(5) == [i for i in range(5)]


# Generated at 2022-06-22 12:43:25.686737
# Unit test for function get_source
def test_get_source():
    def f():
        x = 1

    assert get_source(f) == 'x = 1'

    def g():
        x = 1
    y = 2
    z = 3

    assert get_source(g) == textwrap.dedent(
        '''
        x = 1
        z = 3
        '''
    )

    def h():
        x = 1
    # Comment

    assert get_source(h) == 'x = 1'

# Generated at 2022-06-22 12:43:27.382572
# Unit test for function debug
def test_debug():
    def message():
        return 'Debug message'

    debug(message)

# Generated at 2022-06-22 12:43:35.977093
# Unit test for function debug
def test_debug():

    def assert_error_message_in(message: str, expected_message: str) -> None:
        # This will throw an exception if message is not in the error stream.
        if not message in messages.debug(expected_message) or not expected_message in message:
            raise AssertionError(messages.THERE_IS_A_PROBLEM_WITH_DEBUG_FUNCTION_MESSAGE.format(message))


# Generated at 2022-06-22 12:43:40.596996
# Unit test for function get_source
def test_get_source():
    def func():
        """Sentence 1.
        Sentence 2.
        """
        pass

# Generated at 2022-06-22 12:43:46.157975
# Unit test for function get_source
def test_get_source():
    # function inside a function
    def get_source_function():
        def bar():
            pass

        return get_source(bar)

    # class
    class GetSourceClass():
        def get_source_class_method(self):
            pass

    # class method
    get_source_class_method = GetSourceClass().get_source_class_method

    assert get_source_function() == 'def bar():\n    pass'
    assert get_source(get_source_class_method) == 'def get_source_class_method(self):\n    pass'

# Generated at 2022-06-22 12:43:47.593397
# Unit test for function get_source
def test_get_source():
    def some_fn(x):
        return x

    assert get_source(some_fn).strip() == 'return x'

# Generated at 2022-06-22 12:43:50.506153
# Unit test for function get_source
def test_get_source():
    def add(a: int, b: int) -> int:
        return a + b

    assert get_source(add) == 'return a + b'

# Generated at 2022-06-22 12:43:54.327733
# Unit test for function eager
def test_eager():
    @eager
    def get_array() -> Iterable[int]:
        for i in range(3):
            yield i
    assert get_array() == [0, 1, 2]

# Generated at 2022-06-22 12:45:36.620423
# Unit test for function debug
def test_debug():
    debug_value = 'foo'

    def get_message():
        return debug_value

    debug(get_message)



# Generated at 2022-06-22 12:45:42.971915
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    if get_source(foo) != '''def foo():
    pass
''':
        raise Exception('Wrong source of function {}'.format(foo))

    def bar():
        pass

    def baz():
        def foo():
            pass

    if get_source(foo) != '''def foo():
    pass
''':
        raise Exception('Wrong source of function {}'.format(foo))

    if get_source(baz) != '''def baz():
    def foo():
        pass
''':
        raise Exception('Wrong source of function {}'.format(baz))

# Generated at 2022-06-22 12:45:53.827958
# Unit test for function debug
def test_debug():
    # given
    setting = settings
    settings.debug = True
    warnings = []

    # when
    _debug = debug

    def mock_print(*args, **kwargs):
        warnings.append((args, kwargs))

    debug = mock_print
    try:
        debug(lambda: 'lorem')
        debug(lambda: 'ipsum')
    finally:
        debug = _debug
        settings = setting

    # then
    assert len(warnings) == 2
    assert warnings[0][0] == (messages.debug('lorem'),)
    assert warnings[0][1] == {'file': sys.stderr}
    assert warnings[1][0] == (messages.debug('ipsum'),)
    assert warnings[1][1] == {'file': sys.stderr}

# End

# Generated at 2022-06-22 12:45:57.606939
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar(a):
            pass

    assert get_source(foo) == 'def bar(a):\n    pass\n'
    assert get_source(lambda: 1) == '1\n'

# Generated at 2022-06-22 12:46:00.511066
# Unit test for function debug
def test_debug():
    debug(lambda: 'I\'m alive')  # -> no output to stderr
    settings.debug = True
    debug(lambda: 'I\'m alive')  # -> output to stderr
    settings.debug = False

# Generated at 2022-06-22 12:46:07.454130
# Unit test for function eager
def test_eager():
    from random import randint
    from pytest import raises

    # TODO: test using mock
    f = lambda l: (randint(0, 100) for _ in l)
    r = eager(f)(range(10))

    assert set(map(type, r)) == {int}
    assert all(isinstance(x, int) for x in eager(f)(range(10)))
    assert len(r) == 10

    with raises(TypeError):
        eager(lambda: 5)()



# Generated at 2022-06-22 12:46:10.422775
# Unit test for function get_source
def test_get_source():
    def f():
        x = 2
        y = 3
        return x + y
    assert get_source(f) == 'x = 2\ny = 3\nreturn x + y\n'

# Generated at 2022-06-22 12:46:12.766950
# Unit test for function get_source
def test_get_source():
    @get_source
    def function():
        a = 'foo'
        b = 'bar'
        print(a, b)



# Generated at 2022-06-22 12:46:15.793318
# Unit test for function eager
def test_eager():
    def generator(n):
        for i in range(n):
            yield i

    assert eager(generator)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:46:20.339397
# Unit test for function get_source
def test_get_source():
    def fn1():
        return 1

    assert get_source(fn1) == 'return 1'

    def fn2():
        if True:
            return 1

    assert get_source(fn2) == 'if True:\n    return 1'