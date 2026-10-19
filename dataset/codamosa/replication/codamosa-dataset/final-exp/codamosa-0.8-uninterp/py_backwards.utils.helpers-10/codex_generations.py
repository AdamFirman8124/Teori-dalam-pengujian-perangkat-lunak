

# Generated at 2022-06-22 12:38:29.355792
# Unit test for function get_source
def test_get_source():
    def foo():
        """
        This is a function that has 4 spaces indented.

        """
        return 0
    source = get_source(foo)
    assert '"""\n        This is a' in source
    assert """        return 0
    """ in source

# Generated at 2022-06-22 12:38:34.408635
# Unit test for function eager
def test_eager():
    from nose.tools import raises, assert_equal

    @eager
    def test(x, y):
        for i in range(x):
            for j in range(y):
                yield i, j

    assert_equal(test(2, 3), [(i, j) for i in range(2) for j in range(3)])

# Generated at 2022-06-22 12:38:40.977147
# Unit test for function get_source
def test_get_source():
    from . import ast
    from . import visitor

    ast_nodes = list(ast.iter_ast(get_source))
    visitor.log_ast(ast_nodes)
    assert ast_nodes[0].type == 'Module'
    assert ast_nodes[1].type == 'FunctionDef'
    assert ast_nodes[2].type == 'Expr'
    assert ast_nodes[3].type == 'Name'
    assert ast_nodes[4].type == 'Return'

# Generated at 2022-06-22 12:38:51.216927
# Unit test for function get_source
def test_get_source():
    def foo():
        '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
        ex ea commodo consequat.
        '''
        pass

    def bar():
        pass

    assert get_source(foo) == '''
        def foo():
            '''

# Generated at 2022-06-22 12:38:59.134610
# Unit test for function debug
def test_debug():
    settings.debug = True
    message = 'hello'
    def get_message():
        return message
    with patch('sys.stderr', new_callable=StringIO) as stderr:
        debug(get_message)
        assert message in stderr.getvalue()
    settings.debug = False

ALIASES = {
    'import': 'from {} import *'.format(__name__),
    'reload': 'from importlib import reload',
    'copy': 'from copy import copy',
    'deepcopy': 'from copy import deepcopy',
    'check_type': 'from typing import get_type_hints'
}

# Generated at 2022-06-22 12:39:02.525866
# Unit test for function get_source
def test_get_source():
    def f(x):
        return x

    assert get_source(f) == dedent("""
        def f(x):
            return x
        """)[1:]

# Generated at 2022-06-22 12:39:04.281153
# Unit test for function get_source
def test_get_source():
    def f():
        pass
    
    assert get_source(f) == """def f():
    pass"""

# Generated at 2022-06-22 12:39:06.262214
# Unit test for function eager
def test_eager():
    from itertools import count

    def get_generator() -> Iterable[int]:
        for i in count():
            yiel

# Generated at 2022-06-22 12:39:08.222611
# Unit test for function get_source
def test_get_source():
    def test():
        """
        Test function,
        Here is documentation.
        """
        pass
    code = get_source(test)

# Generated at 2022-06-22 12:39:11.219714
# Unit test for function get_source
def test_get_source():
    def sample_function(variable: int) -> int:
        return variable

    sample_source_lines = ["def sample_function(variable: int) -> int:",
                           "    return variable"]

    assert get_source(sample_function) == '\n'.join(sample_source_lines)

# Generated at 2022-06-22 12:39:18.667453
# Unit test for function debug
def test_debug():
    output = io.StringIO()
    sys.stderr = output

    try:
        settings.debug = False
        debug(lambda: 'foo')
        assert output.getvalue() == ''

        settings.debug = True
        debug(lambda: 'bar')
        assert output.getvalue() == messages.debug('bar') + '\n'
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:26.122121
# Unit test for function debug
def test_debug():
    class StdOutput:
        def __init__(self) -> None:
            self.out = ''

        def write(self, text) -> None:
            self.out += text

        def get_out(self) -> str:
            return self.out

    old_err = sys.stderr
    sys.stderr = StdOutput()
    settings.debug = True
    debug(lambda: 'Log some debug')
    assert '[DEBUG]' in sys.stderr.get_out()
    sys.stderr = old_err
    settings.debug = False

# Generated at 2022-06-22 12:39:32.952849
# Unit test for function eager
def test_eager():
    def generator(x):
        yield x
        yield x

    print(list(range(1)))
    print(list(range(10)))
    print(list(range(0)))
    print(list(range(-10)))

    print(eager(generator)(1))
    print(eager(generator)(10))
    print(eager(generator)(0))
    print(eager(generator)(-10))

# Generated at 2022-06-22 12:39:37.129461
# Unit test for function debug
def test_debug():
    from mock import Mock
    from .conf import settings

    settings.debug = True
    get_message = Mock()
    debug(get_message)
    get_message.assert_called_once_with()

    settings.debug = False
    get_message = Mock()
    debug(get_message)
    get_message.assert_not_called()

# Generated at 2022-06-22 12:39:39.388610
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == dedent(get_source.__doc__)

# Generated at 2022-06-22 12:39:42.908230
# Unit test for function get_source
def test_get_source():
    def test_fn(a, b):
        """Function docstring.

        Arguments:
            a -- this is a
            b -- this is b
        """
        print(a)
        return a + b


# Generated at 2022-06-22 12:39:44.374850
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        yield 1
    assert gen() == [1]

# Generated at 2022-06-22 12:39:51.472705
# Unit test for function debug
def test_debug():
    from .testing import captured_output

    with captured_output() as (stdout, stderr):
        debug(lambda: 'foobar')
        assert stderr.getvalue() == ''

    with captured_output() as (stdout, stderr):
        with settings.override_settings(DEBUG=True):
            debug(lambda: 'foobar')
        assert stderr.getvalue() == '{} {}\n'.format(
            messages.PREFIX, messages.debug('foobar'))



# Generated at 2022-06-22 12:39:56.348435
# Unit test for function debug
def test_debug():
    warnings = []
    sys.stderr = warnings
    settings.debug = True
    debug(lambda: 'Test debug')
    assert warnings[0] == messages.debug('Test debug')
    settings.debug = False
    debug(lambda: 'Test debug')
    assert not warnings
    sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:57.695792
# Unit test for function eager
def test_eager():
    assert eager(list)([1, 2]) == [1, 2]

# Generated at 2022-06-22 12:40:07.167256
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    def goo():
        def foo():
            pass

    assert get_source(fn) == 'def fn():\n    pass'
    assert get_source(goo).count('\n') == 3
    assert 'def foo' in get_source(goo)

# Generated at 2022-06-22 12:40:15.212517
# Unit test for function get_source
def test_get_source():
    def foo():
        return 1 + 3

    def bar():
        a = 4 + 5
        b = 6 + 7
        return a + b

    def plus(a, b):
        return a + b

    assert get_source(foo) == 'return 1 + 3', get_source(foo)
    assert get_source(bar) == 'a = 4 + 5\nb = 6 + 7\nreturn a + b', get_source(bar)
    assert get_source(plus) == 'return a + b', get_source(plus)

# Generated at 2022-06-22 12:40:19.366595
# Unit test for function debug
def test_debug():
    from io import StringIO
    import sys
    sys.stderr = StringIO()
    debug(lambda: 'message')
    assert sys.stderr.getvalue().strip() == messages.debug('message')
    sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:40:25.637998
# Unit test for function debug
def test_debug():
    class Mock:
        messages: List[str] = []
    sys.stderr = Mock()
    init_settings = settings.debug
    settings.debug = True
    debug(lambda: 'hey')
    settings.debug = False
    debug(lambda: 'ho')
    settings.debug = True
    debug(lambda: 'lets go')
    settings.debug = init_settings
    assert sys.stderr.messages == ['hey', 'lets go']

# Generated at 2022-06-22 12:40:32.589130
# Unit test for function eager
def test_eager():
    import unittest
    from . import setup_test_module

    class Test(unittest.TestCase):
        def test_eager(self):
            @eager
            def range_generator(start, end):
                while start != end:
                    yield start
                    start += 1

            self.assertEqual(range_generator(1, 4), [1, 2, 3])

    setup_test_module(__name__)

# Generated at 2022-06-22 12:40:35.769829
# Unit test for function eager
def test_eager():
    @eager
    def gen(n):
        i = 0
        while i < n:
            yield i
            i += 1
    assert gen(3) == [0, 1, 2]

# Generated at 2022-06-22 12:40:38.099661
# Unit test for function get_source
def test_get_source():
    def test_code():
        pass

    assert get_source(test_code) == 'def test_code():\n    pass\n'

# Generated at 2022-06-22 12:40:40.342218
# Unit test for function debug
def test_debug():
    flag = False

    def func():
        nonlocal flag
        flag = settings.debug

    debug(func)
    assert flag == settings.debug

# Generated at 2022-06-22 12:40:43.811619
# Unit test for function get_source
def test_get_source():
    def func():
        def nested():
            return 1

        return nested

    assert get_source(func) == dedent(
        """
        def nested():
            return 1
        """
    ).strip()



# Generated at 2022-06-22 12:40:50.339578
# Unit test for function debug
def test_debug():
    sys.argv += ["--debug"]

    settings.debug = True
    debug(lambda: "debug function test")
    assert sys.stderr.getvalue() == "\x1b[36mDEBUG: debug function test\x1b[0m\n"

    sys.stderr = StringIO()

    settings.debug = False
    debug(lambda: "debug function test")
    assert sys.stderr.getvalue() == ""


# Generated at 2022-06-22 12:41:00.252736
# Unit test for function debug
def test_debug():
    debug(lambda: 'debug')

# Generated at 2022-06-22 12:41:02.407000
# Unit test for function get_source
def test_get_source():
    def test_func():
        return 'test'
    source = get_source(test_func)
    assert source == 'return "test"'

# Generated at 2022-06-22 12:41:04.879944
# Unit test for function get_source
def test_get_source():
    def test_function():
        all = "hello world"
        return 1, 2

    source = get_source(test_function)
    assert source == 'return 1, 2'

# Generated at 2022-06-22 12:41:08.107223
# Unit test for function debug
def test_debug():
    sys.stderr = StringIO()
    settings.debug = True
    debug(lambda: 'test message')
    assert 'test message' in sys.stderr.getvalue()
    settings.debug = False

# Generated at 2022-06-22 12:41:10.701044
# Unit test for function get_source
def test_get_source():
    # testing get_source
    def foo():
        """
        Something
        """


# Generated at 2022-06-22 12:41:20.104964
# Unit test for function debug
def test_debug():
    class OutputCapture:
        def __init__(self) -> None:
            self.output = []

        def write(self, message) -> None:
            self.output.append(message)

        def __str__(self) -> str:
            return ' '.join(self.output)

    output = OutputCapture()
    old_stderr = sys.stderr
    sys.stderr = output
    settings.debug = True
    try:
        debug(lambda: 'debug message')
        assert 'debug message' == output.output[0]
        assert '\x1b[0m' == output.output[1], 'output should be reset'
    finally:
        sys.stderr = old_stderr



# Generated at 2022-06-22 12:41:22.625715
# Unit test for function debug
def test_debug():
    from .testing import MockFile
    from ..conf import settings
    settings.debug = True
    mock_file = MockFile()
    sys.stderr = mock_file
    message = 'Foo bar'
    debug(lambda: message)
    assert mock_file.read() == messages.debug(message) + '\n'



# Generated at 2022-06-22 12:41:33.215860
# Unit test for function debug
def test_debug():
    import unittest
    import io
    import sys

    class TestDebug(unittest.TestCase):

        def _get_stderr(self) -> str:
            self.__old_stderr = sys.stderr
            sys.stderr = io.StringIO()
            return sys.stderr

        def tearDown(self) -> None:
            sys.stderr = self.__old_stderr

        def test_enabled(self) -> None:
            settings.debug = True
            stderr = self._get_stderr()
            debug(lambda: 'test')
            self.assertEqual('test\n', stderr.getvalue())

        def test_disabled(self) -> None:
            settings.debug = False
            stderr = self._get_stderr()

# Generated at 2022-06-22 12:41:38.020739
# Unit test for function debug
def test_debug():
    # pylint: disable=unused-argument, missing-function-docstring
    def my_function(arg: Any) -> None:
        pass

    assert not settings.debug

    message = 'Here goes the message'
    debug(lambda: message)

    settings.debug = True

    debug(lambda: message)

# Generated at 2022-06-22 12:41:43.584552
# Unit test for function debug
def test_debug():
    from . import testutils

    with testutils.ContextMock(debug=True) as context_mock:
        debug(lambda: 'message')
        assert context_mock.mock_calls[0][2]['file_'] == sys.stderr
    with testutils.ContextMock(debug=False) as context_mock:
        debug(lambda: 'message')
        assert len(context_mock.mock_calls) == 0

# Generated at 2022-06-22 12:42:08.113196
# Unit test for function debug
def test_debug():
    def test_func(debug_message):
        def get_message():
            return debug_message
        return get_message

    assert debug(test_func("one")) is debug(test_func("two")) is None

# Generated at 2022-06-22 12:42:09.945048
# Unit test for function get_source
def test_get_source():
    def f(a):
        pass
    assert get_source(f) == 'def f(a):\n    pass'

# Generated at 2022-06-22 12:42:12.992527
# Unit test for function eager
def test_eager():
    @eager
    def function_with_yield(*args, **kwargs):
        for i in range(args[0]):
            yield i
    assert function_with_yield(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:42:17.174450
# Unit test for function eager
def test_eager():
    @eager
    def some_iterable(number: int) -> Iterable[int]:
        for i in range(number):
            yield i
    assert some_iterable(3) == [0, 1, 2]

# Generated at 2022-06-22 12:42:23.220134
# Unit test for function debug
def test_debug():
    global __debug_output__
    __debug_output__ = []
    original_settings_debug = settings.debug

    try:
        settings.debug = True
        debug(lambda: 'test')
        assert __debug_output__ == ['test']

        settings.debug = False
        debug(lambda: 'test')
        assert __debug_output__ == ['test']
    finally:
        settings.debug = original_settings_debug


__debug_output__: List[str] = []

# Generated at 2022-06-22 12:42:27.214912
# Unit test for function eager
def test_eager():
    @eager
    def test_func() -> Iterable[int]:
        for i in range(3):
            yield i

    assert test_func() == list(range(3))


# Unit tests for class VariablesGenerator

# Generated at 2022-06-22 12:42:28.863922
# Unit test for function get_source
def test_get_source():

    def inner_function():
        pass

    test_function = get_source(inner_function)

    expected_result = 'def inner_function():\n    pass'
    assert test_function == expected_result

# Generated at 2022-06-22 12:42:34.473999
# Unit test for function get_source
def test_get_source():
    source_lines = getsource(test_get_source).split('\n')
    padding = len(re.findall(r'^(\s*)', source_lines[0])[0])
    expected = '\n'.join(line[padding:] for line in source_lines)
    assert get_source(test_get_source) == expected

# Generated at 2022-06-22 12:42:38.173131
# Unit test for function eager
def test_eager():
    def some_func():
        for x in range(10):
            yield x

    assert callable(eager(some_func))
    assert eager(some_func)() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-22 12:42:42.763509
# Unit test for function eager
def test_eager():
    from collections.abc import Iterable
    from operator import add
    @eager
    def one_to(limit):
        i = 0
        while i < limit:
            i += 1
            yield i

    assert isinstance(one_to(5), Iterable)
    assert add(*one_to(5)) == 15



# Generated at 2022-06-22 12:43:34.971173
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        for i in range(5):
            yield i

    assert foo() == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:43:38.791311
# Unit test for function debug
def test_debug():
    from io import StringIO
    from contextlib import redirect_stderr
    output = StringIO()
    with redirect_stderr(output):
        debug(lambda: 'Test debug message')
    assert output.getvalue().strip() == messages.debug('Test debug message')


# For testing purposes

# Generated at 2022-06-22 12:43:43.855572
# Unit test for function debug
def test_debug():
    def debug_equal(expected, input):
        import io
        with io.StringIO() as buf, settings(debug=True):
            debug(input)
            assert buf.getvalue() == expected
        with io.StringIO() as buf, settings(debug=False):
            debug(input)
            assert buf.getvalue() == ''
    debug_equal('[DEBUG] 1\n', lambda: 1)

# Generated at 2022-06-22 12:43:45.130325
# Unit test for function debug
def test_debug():
    debug(lambda: 'debug message')



# Generated at 2022-06-22 12:43:46.548655
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f) == 'def f():\n    pass'

# Generated at 2022-06-22 12:43:47.666201
# Unit test for function debug
def test_debug():
    def get_message():
        return "Provided message"
    debug(get_message)

# Generated at 2022-06-22 12:43:57.944355
# Unit test for function get_source

# Generated at 2022-06-22 12:44:01.100295
# Unit test for function debug
def test_debug():
    debug(lambda: 'x')
    settings.debug = False
    debug(lambda: 'x')
    settings.debug = True



# Generated at 2022-06-22 12:44:09.285308
# Unit test for function debug
def test_debug():
    class FakeStream:
        def __init__(self):
            self.messages = []

        def write(self, message: str) -> None:
            self.messages.append(message)

    fake_stream = FakeStream()
    settings.debug = True
    sys.stderr = fake_stream
    debug(lambda: 'fake message')
    sys.stderr = sys.__stderr__
    settings.debug = False

    assert len(fake_stream.messages) == 1
    assert fake_stream.messages[0] == messages.debug('fake message')

# Generated at 2022-06-22 12:44:15.157071
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == \
        """    assert get_source(test_get_source) == \\\n"""\
        """        '''    assert get_source(test_get_source) == \\\n"""\
        """            \\\\\\\\\\\\\\n"""\
        """            '''"""

if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:45:05.264449
# Unit test for function get_source
def test_get_source():

    def test_fn(a: int) -> int:
        b = a + a
        c = a + a
        return b + c

    assert get_source(test_fn) == 'b = a + a\nb + c'



# Generated at 2022-06-22 12:45:09.505635
# Unit test for function get_source
def test_get_source():
    import copy

    def func():
        a = 1
        return copy.copy(a)

    lines = get_source(func).split('\n')
    assert lines[0] == 'def func():'
    assert lines[1] == '    a = 1'
    assert lines[2] == '    return copy.copy(a)'

# Generated at 2022-06-22 12:45:12.218310
# Unit test for function get_source
def test_get_source():
    def foo():
        return bar()

    def bar():
        return 2

    assert get_source(foo) == 'return bar()'
    assert get_source(bar) == 'return 2'

# Generated at 2022-06-22 12:45:15.756224
# Unit test for function debug
def test_debug():
    import io
    import sys
    import unittest
    from contextlib import contextmanager

    @contextmanager
    def capture_output():
        old_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            yield sys.stdout
        finally:
            sys.stdout = old_stdout

    class Test(unittest.TestCase):
        def test_debug(self):
            def get_message():
                return "debug message"

            with capture_output() as stdout:
                debug(get_message)
                self.assertIn("debug message", stdout.getvalue())

        def test_no_debug(self):
            def get_message():
                return "debug message"

            with capture_output() as stdout:
                settings.debug = False

# Generated at 2022-06-22 12:45:19.970561
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    def g():
        def f():
            pass

    assert get_source(f) == 'def f():\n    pass'
    assert get_source(g) == 'def g():\n    def f():\n        pass'


# Generated at 2022-06-22 12:45:22.497631
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            pass

    assert get_source(foo) == 'def bar():\n    pass'

# Generated at 2022-06-22 12:45:26.898295
# Unit test for function debug
def test_debug():
    for debug_mode in (True, False):
        settings.debug = debug_mode
        debug_called = [False]

        def get_debug_message():
            debug_called[0] = True
            return 'debug_called'

        debug(get_debug_message)
        assert debug_called[0] == debug_mode

# Generated at 2022-06-22 12:45:30.187238
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        yield 1
        yield 2
        yield 3

    assert gen() == [1, 2, 3]


# Generated at 2022-06-22 12:45:32.645846
# Unit test for function eager
def test_eager():
    assert eager(lambda: range(5))() == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:45:36.439056
# Unit test for function debug
def test_debug():
    if settings.debug:
        final_output = ""
        final_output += messages.debug("test")
        final_output += messages.debug("test")
        assert debug(lambda: "test") == final_output

# Generated at 2022-06-22 12:47:44.894215
# Unit test for function eager
def test_eager():
    from random import random
    from operator import floordiv

    list_random_ints = list(map(int, map(lambda: random(), range(3))))

    def lazy_random_ints():
        for i in range(3):
            yield int(random())

    assert eager(random_ints)() == list_random_ints


# Generated at 2022-06-22 12:47:45.849566
# Unit test for function get_source

# Generated at 2022-06-22 12:47:52.340646
# Unit test for function get_source
def test_get_source():
    def some_function():
        return 1

    assert get_source(some_function) == 'return 1'

    def another_function():
        variable = 1  # noqa: F841
        return variable

    assert get_source(another_function) == 'return variable'

# Generated at 2022-06-22 12:47:55.631082
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass
    assert get_source(test_func) == 'def test_func():\n    pass'



# Generated at 2022-06-22 12:47:57.584374
# Unit test for function get_source
def test_get_source():
    def function():
        return 1
    assert get_source(function) == 'return 1'



# Generated at 2022-06-22 12:48:03.765413
# Unit test for function debug
def test_debug():
    print('Testing function debug ...')

    def get_message():
        return 'Test'

    debug = debug
    debug_origin = debug

    def debug(message):
        debug_origin('A')
        debug_origin('B')
        assert message == 'Test'
        debug_origin('C')
        debug_origin('D')

    debug(get_message)

    debug = debug_origin

    print('Success!')



# Generated at 2022-06-22 12:48:08.458868
# Unit test for function get_source
def test_get_source():
    def _my_function():
        def _my_inner_function():
            pass

        code = '''
            for i in range(10):
                print(i)
            '''
        exec(code)


    assert get_source(_my_function) == '''
for i in range(10):
    print(i)
    '''

# Generated at 2022-06-22 12:48:13.065126
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)
    
    assert len(source) > 0, '\n'.join([
        'Source code of the function is empty, check get_source function'
        'you can add some "  " padding to def line and see if the code is correct'
    ])



# Generated at 2022-06-22 12:48:14.798589
# Unit test for function eager
def test_eager():
    assert eager(range)(0, 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-22 12:48:19.201141
# Unit test for function get_source
def test_get_source():
    def get_source_test():
        def bar(a, b):
            return a * b

        return bar

    assert get_source(get_source_test) == 'def bar(a, b):\n' \
                                         '    return a * b'