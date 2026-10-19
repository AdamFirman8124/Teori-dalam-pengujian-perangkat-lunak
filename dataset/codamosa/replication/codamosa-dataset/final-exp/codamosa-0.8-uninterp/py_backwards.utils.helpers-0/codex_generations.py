

# Generated at 2022-06-22 12:38:28.112640
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f) == 'pass\n'



# Generated at 2022-06-22 12:38:33.548078
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == """def test_get_source():
    assert get_source(test_get_source) == """
"""def test_get_source():
    assert get_source(test_get_source) == '''def test_get_source():
    assert get_source(test_get_source) == '''"""



# Generated at 2022-06-22 12:38:35.330276
# Unit test for function eager
def test_eager():
    @eager
    def filtered(condition: bool) -> Iterable[int]:
        for i in range(5):
            if condition:
                yield i
    assert filtered(True) == [0, 1, 2, 3, 4]
    assert filtered(False) == []


# Generated at 2022-06-22 12:38:36.145217
# Unit test for function eager
def test_eager():
    assert eager(range)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:38:38.028239
# Unit test for function get_source
def test_get_source():
    def foo(x):
        print(x)

    assert get_source(foo) == '    print(x)\n'

# Generated at 2022-06-22 12:38:41.632144
# Unit test for function get_source
def test_get_source():
    from . import test_helpers
    # some additional characters are required here for tests
    function = test_helpers.function_with_additional_lines

    assert get_source(function) == '\n'.join(function.__doc__.split('\n')[1:])

# Generated at 2022-06-22 12:38:47.934709
# Unit test for function get_source
def test_get_source():
    def func():
        pass

    def func_with_args(a, b, c=None, *args, **kwargs):
        pass

    assert get_source(func) == 'def func():\n    pass'
    assert get_source(func_with_args) == (
        'def func_with_args(a, b, c=None, *args, **kwargs):\n'
        '    pass'
    )

# Generated at 2022-06-22 12:38:51.251968
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == getsource(fn)
    assert get_source(fn) == 'def fn():\n    pass'

# Generated at 2022-06-22 12:38:54.938499
# Unit test for function get_source
def test_get_source():
    assert get_source.__qualname__ == 'get_source'
    assert get_source.__name__ == 'get_source'
    assert get_source.__module__ == 'py_backwards'



# Generated at 2022-06-22 12:38:59.283733
# Unit test for function debug
def test_debug():
    from io import StringIO
    out = StringIO()
    debug(lambda: 'test message')
    assert out.getvalue() == ''

    settings.debug = True
    debug(lambda: 'test message')
    assert out.getvalue() == messages.debug('test message') + '\n'
    settings.debug = False



# Generated at 2022-06-22 12:39:07.113699
# Unit test for function get_source
def test_get_source():
    def fn(a: Any = 1) -> int:
        if a == 1:
            return 1
        else:
            return 0

    assert ' '.join(get_source(fn).split()) == (
        'def fn(a: Any = 1) -> int:\n'
        '  if a == 1:\n'
        '    return 1\n'
        '  else:\n'
        '    return 0'
    )


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:39:13.080995
# Unit test for function debug
def test_debug():
    if hasattr(sys, 'meta_path'):
        import unittest.mock as mock
        from contextlib import contextmanager

        with mock.patch('sys.stderr.write') as m_write:
            settings.debug = True
            debug(lambda: '{} {}'.format('this', 'works'))
            settings.debug = False
            debug(lambda: '{} {}'.format('this', 'works'))
            assert m_write.call_args_list == [
                mock.call(messages.DEBUG_FORMAT_RE.format('this works')),
            ]
    else:
        import mock

        with mock.patch('sys.stderr') as m_stderr:
            settings.debug = True
            debug(lambda: '{} {}'.format('this', 'works'))
           

# Generated at 2022-06-22 12:39:14.809838
# Unit test for function eager
def test_eager():
    assert eager(lambda: range(3))() == [0, 1, 2]

# Generated at 2022-06-22 12:39:18.765002
# Unit test for function get_source
def test_get_source():
    def test_func(x: Any = None, y: Any = 1, *args: Any, **kwargs: Any) -> Any:
        return x + y + sum(args) + sum(kwargs.values())

# Generated at 2022-06-22 12:39:21.871103
# Unit test for function get_source
def test_get_source():
    """Test function get_source"""
    def f():
        "docstring"
        pass

    assert get_source(f) == """def f():
    "docstring"
    pass""".strip()

# Generated at 2022-06-22 12:39:26.392257
# Unit test for function eager
def test_eager():
    # Before
    def f(x):
        return [x]
    a = f(1)
    assert type(a) == list
    assert a[0] == 1
    # After
    a = eager(f)(1)
    assert type(a) == list
    assert a[0] == 1


# Generated at 2022-06-22 12:39:34.014214
# Unit test for function debug
def test_debug():
    import unittest
    import sys
    import io

    class DebugTest(unittest.TestCase):
        def setUp(self) -> None:
            self.output = io.StringIO()
            self.original_stderr = sys.stderr
            sys.stderr = self.output

        def tearDown(self) -> None:
            sys.stderr = self.original_stderr

        def test_debug_print(self) -> None:
            debug(lambda: 'test')
            self.assertEqual(self.output.getvalue(), '[DEBUG] test\n')

    unittest.main()



# Generated at 2022-06-22 12:39:37.811920
# Unit test for function get_source
def test_get_source():
    from inspect import getsource
    from unittest import TestCase

    class TestFunction(TestCase):

        def test_function(self):
            def function(x):
                a = 1
                for b in range(5):
                    a += 1
                return a

            assert getsource(function) == get_source(function)

# Generated at 2022-06-22 12:39:40.391720
# Unit test for function eager
def test_eager():
    @eager
    def test() -> Iterable[int]:
        yield 3
        yield 2
        yield 1

    assert test() == [3, 2, 1]

# Generated at 2022-06-22 12:39:42.754552
# Unit test for function debug
def test_debug():
    messages.DEBUG = 'debug'
    debug(lambda: 'something')
    settings.debug = False
    debug(lambda: 'something')



# Generated at 2022-06-22 12:39:50.389165
# Unit test for function eager
def test_eager():
    def test_function(data):
        for elem in data:
            yield elem

    @eager
    def test_function2(data):
        for elem in data:
            yield elem

    assert test_function([1,2]) == [1,2]
    assert test_function2([3,4]) == [3,4]

# Generated at 2022-06-22 12:39:58.624832
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == "def test_get_source():\n    assert get_source(test_get_source) == \"def test_get_source():\\n    assert get_source(test_get_source) == \\\"def test_get_source():\\\\n    assert get_source(test_get_source) == \\\\\\\"def test_get_source():\\\\\\\\n    assert get_source(test_get_source) == \\\\\\\\\\\\\"def test_get_source():\\\\\\\\\\\\n    assert get_source(test_get_source) == \\\\\\\\\\\\\\\\\\\\\\\"\""

# Generated at 2022-06-22 12:40:02.807048
# Unit test for function get_source
def test_get_source():
    def test():
        a = 1
        b = 1+2
        c = 1+2+3
        return a + b + c
    assert get_source(test) == """
a = 1
b = 1+2
c = 1+2+3
return a + b + c"""

# Generated at 2022-06-22 12:40:05.592341
# Unit test for function get_source
def test_get_source():
    def f():
        pass
    assert get_source(f) == 'def f():\n    pass'

# Generated at 2022-06-22 12:40:08.478688
# Unit test for function get_source
def test_get_source():
    def test():
        '''
            def test():
                pass
        '''

    assert get_source(test) == 'def test():\n    pass'



# Generated at 2022-06-22 12:40:11.960674
# Unit test for function eager
def test_eager():
    @eager
    def fn(x: int) -> Iterable[int]:
        yield x * x
        yield x * x + 1
        yield x * x + 2

    assert fn(1) == [1, 2, 3]



# Generated at 2022-06-22 12:40:14.485996
# Unit test for function debug
def test_debug():
    from ..conf import set_debug
    set_debug(True)
    assert debug(lambda: 'foo') == None

# Generated at 2022-06-22 12:40:16.407115
# Unit test for function get_source
def test_get_source():
    def test():
        print(1)
    assert get_source(test) == 'print(1)'

# Generated at 2022-06-22 12:40:19.314032
# Unit test for function get_source
def test_get_source():
    import astor

    def foo(a, b, c):
        pass

    assert get_source(foo) == astor.to_source(foo).strip()

# Generated at 2022-06-22 12:40:25.985252
# Unit test for function debug
def test_debug():
    import contextlib
    from io import StringIO
    with contextlib.redirect_stderr(StringIO()) as stderr:
        debug(lambda: 'testing')
        assert stderr.getvalue() == ''
    with contextlib.redirect_stderr(StringIO()) as stderr:
        settings.debug = True
        debug(lambda: 'testing')
        settings.debug = False
        assert stderr.getvalue() == 'DEBUG: testing\n'



# Generated at 2022-06-22 12:40:34.835435
# Unit test for function get_source
def test_get_source():
    def func():
        pass

    assert get_source(func) == 'pass'

# Generated at 2022-06-22 12:40:36.280895
# Unit test for function eager
def test_eager():
    assert eager(lambda: [1, 2, 3])() == [1, 2, 3]

# Generated at 2022-06-22 12:40:46.456130
# Unit test for function get_source
def test_get_source():
    if sys.version_info < (3, 8):
        return

    class Parent:
        """Parent Doc"""

        def parent_method(self) -> None:
            """Parent Method Doc"""
            pass

    class Child(Parent):
        def child_method(self) -> None:
            """Child Method Doc"""
            pass

    child = Child()

    # Check that the source code is reported as expected.
    assert get_source(child.child_method) == (
        'def child_method(self) -> None:\n'
        '    """Child Method Doc"""\n'
    )

    # Check that the source code accounts for inheritance.

# Generated at 2022-06-22 12:40:49.039599
# Unit test for function get_source
def test_get_source():
    expected = 'def test():\n' \
               '    return False'
    assert get_source(test) == expected

# Generated at 2022-06-22 12:40:49.983308
# Unit test for function debug
def test_debug():
    debug(lambda: 'debug message')



# Generated at 2022-06-22 12:40:51.742890
# Unit test for function eager
def test_eager():
    @eager
    def f():
        yield 1
        yield 2
    assert f() == [1, 2]

# Generated at 2022-06-22 12:40:54.264518
# Unit test for function get_source
def test_get_source():
    def a():
        pass

    assert get_source(a).strip() == 'pass'



# Generated at 2022-06-22 12:40:56.340723
# Unit test for function get_source
def test_get_source():
    def test():
        """
        Test function.
        """
        pass



# Generated at 2022-06-22 12:41:00.278553
# Unit test for function eager
def test_eager():
    @eager
    def fib(n):
        a, b = 0, 1
        while n > 0:
            yield a
            a, b = b, a + b
            n -= 1

    assert fib(5) == [0, 1, 1, 2, 3]

# Generated at 2022-06-22 12:41:00.833014
# Unit test for function debug
def test_debug():
    debug(lambda: 'debug')

# Generated at 2022-06-22 12:41:11.118259
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'pass'



# Generated at 2022-06-22 12:41:14.256202
# Unit test for function debug
def test_debug():
    import io

    buf = io.StringIO()
    with settings(debug=True):
        debug(lambda: 'message')

    assert buf.getvalue() == messages.debug('message') + '\n'

# Generated at 2022-06-22 12:41:16.455139
# Unit test for function get_source
def test_get_source():
    def test_function():
        """docstring"""
        return 1

    assert get_source(test_function) == 'return 1'

# Generated at 2022-06-22 12:41:24.488359
# Unit test for function get_source

# Generated at 2022-06-22 12:41:26.644637
# Unit test for function eager
def test_eager():
    seq = [1, 2, 3]
    # noinspection PyTypeChecker
    assert eager(lambda: seq)() == seq



# Generated at 2022-06-22 12:41:28.358385
# Unit test for function get_source
def test_get_source():

    def function():
        print('Hello world')

    assert get_source(function) == "print('Hello world')"

# Generated at 2022-06-22 12:41:39.790792
# Unit test for function debug
def test_debug():
    import io

    class TextIOWrapper(io.TextIOWrapper):
        def __init__(self, buffer: io.StringIO) -> None:
            super().__init__(buffer)
            self.buffer = buffer

        def read(self) -> str:
            return self.buffer.getvalue()

    assert not settings.debug
    original_stderr = sys.stderr

# Generated at 2022-06-22 12:41:41.851972
# Unit test for function eager
def test_eager():
    def fn(a):
        return (a, a, a)
    assert eager(fn)(42) == [42, 42, 42]

# Generated at 2022-06-22 12:41:46.679133
# Unit test for function debug
def test_debug():
    debug_m = Mock()
    settings.debug = True
    debug(debug_m)
    debug_m.assert_called()
    settings.debug = False
    debug_m.reset_mock()
    debug(debug_m)
    debug_m.assert_not_called()


# Generated at 2022-06-22 12:41:49.081406
# Unit test for function get_source
def test_get_source():
    def f():
        a = 1
        return a

    assert get_source(f) == 'a = 1\nreturn a'

# Generated at 2022-06-22 12:42:12.667859
# Unit test for function eager
def test_eager():
    @eager
    def empty_generator():
        yield from []

    @eager
    def generator():
        yield from [1, 2, 3]

    @eager
    def generator_of_generators():
        yield from [1, 2, 3]

    assert empty_generator() == []
    assert generator() == [1, 2, 3]
    assert generator_of_generators() == [1, 2, 3]



# Generated at 2022-06-22 12:42:18.288277
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)
    assert set(source.split('\n')) == {
        '    source = get_source(test_get_source)',
        '    assert set(source.split(\'\\n\')) == {',
        '}',
        '',
    }

# Generated at 2022-06-22 12:42:21.979363
# Unit test for function debug
def test_debug():
    debug_messages = []
    def set_debug_message(message: str) -> None:
        debug_messages.append(message)

    settings.debug = True
    debug(lambda: messages.debug(set_debug_message))
    assert len(debug_messages) == 1

# Generated at 2022-06-22 12:42:26.200391
# Unit test for function eager
def test_eager():
    # For example, if there is a function that has the following output:
    def yield_values():
        yield 1
        yield 2
        yield 3
    # Then calling the function eager will return
    assert eager(yield_values)() == [1, 2, 3]

# Generated at 2022-06-22 12:42:31.437523
# Unit test for function debug
def test_debug():
    def print(string, file):
        assert string.strip() == '⚠ Debug: and the message'
        assert file is sys.stderr

    settings.debug = True
    debug(lambda: 'and the message')
    settings.debug = False
    debug(lambda: 'and the message')

# Generated at 2022-06-22 12:42:33.318359
# Unit test for function eager
def test_eager():
    @eager
    def f():
        yield 1
        yield 2

    assert f() == [1, 2]

# Generated at 2022-06-22 12:42:39.261477
# Unit test for function get_source
def test_get_source():
    @get_source
    def test(a, b, *c, d, e=1, **f):
        return a + b + c + (d, e) + tuple(f.items())

    assert test == '\n'.join((
        'def test(a, b, *c, d, e=1, **f):',
        '    return a + b + c + (d, e) + tuple(f.items())',
    ))



# Generated at 2022-06-22 12:42:43.372808
# Unit test for function get_source
def test_get_source():
    def foo(): pass
    assert get_source(foo) == 'def foo(): pass'

    def bar():
        """This is a documentation
        string"""
        pass
    assert get_source(bar) == 'def bar():\n    """This is a documentation\n    string"""\n    pass'

# Generated at 2022-06-22 12:42:48.452425
# Unit test for function get_source
def test_get_source():
    def test():
        """Docstring

        Args:
            not_to_be_printed

        Returns:
            not_to_be_printed
        """
        return 'to_be_printed'

    source = get_source(test)
    assert source == "return 'to_be_printed'"



# Generated at 2022-06-22 12:42:51.573205
# Unit test for function get_source
def test_get_source():
    @wraps(test_get_source)
    def wrapper():
        if get_source(test_get_source) != 'return 1':
            raise AssertionError('Function get_source is not correct')

    return 1



# Generated at 2022-06-22 12:43:45.733563
# Unit test for function eager
def test_eager():
    def foo():
        yield 1
        yield 2

    assert eager(foo)() == [1, 2]

# Generated at 2022-06-22 12:43:54.166292
# Unit test for function debug
def test_debug():
    debug_messages = []
    def test_debug_fn(message: str) -> None:
        debug_messages.append(message)
    settings.debug = True
    debug(lambda: 'some message')
    assert debug_messages == ['some message']
    debug(lambda: 'another message')
    assert debug_messages == ['some message', 'another message']
    settings.debug = False
    debug(lambda: 'third message')
    assert debug_messages == ['some message', 'another message']

assert test_debug() is None

# Generated at 2022-06-22 12:43:56.594332
# Unit test for function get_source
def test_get_source():
    function_to_test = "def f():\n    pass\n"
    print(get_source(function_to_test))

test_get_source()

# Generated at 2022-06-22 12:44:02.855211
# Unit test for function debug
def test_debug():
    class MockWriter:
        def __init__(self) -> None:
            self.log = ''

        def write(self, chars: str) -> None:
            self.log += chars

    writer = MockWriter()
    sys.stderr = writer
    settings.debug = True
    debug(lambda: 'test')
    assert writer.log.endswith('test\n')

# Generated at 2022-06-22 12:44:04.670870
# Unit test for function eager
def test_eager():
    def func():
        yield 1
        yield 2

    assert eager(func)() == [1, 2]

# Generated at 2022-06-22 12:44:09.234146
# Unit test for function get_source
def test_get_source():
    def _decorate(fn):
        return get_source(fn)

    from .test_utils import _get_source_data
    for test_case in _get_source_data():
        assert _decorate(test_case[0]) == test_case[1]

# Generated at 2022-06-22 12:44:12.666159
# Unit test for function debug
def test_debug():
    settings.debug = True
    x = 1
    debug(lambda: f'x: {x}')
    settings.debug = False
    x = 2
    debug(lambda: f'x: {x}')

# Generated at 2022-06-22 12:44:14.905084
# Unit test for function eager
def test_eager():
    @eager
    def function():
        yield 1
        yield 2
        yield 3

    assert function() == [1, 2, 3]

# Generated at 2022-06-22 12:44:20.236167
# Unit test for function get_source
def test_get_source():
    # Test for function which has only one line
    def test_fun1():
        return 1
    assert(get_source(test_fun1) == 'return 1')

    # Test for function which has many lines with different padding
    def test_fun2():
        return 2 +\
            3
    assert(get_source(test_fun2) == 'return 2 +\n    3')


# Unit tests for function warn

# Generated at 2022-06-22 12:44:30.610921
# Unit test for function eager
def test_eager():
    class EagerGenerator:
        def __init__(self):
            self.n = 0

        @eager
        def get_iterable(self) -> Iterable[int]:
            for x in range(self.n):
                yield x

        @eager
        def get_list(self) -> List[int]:
            return [self.n]

    eager_generator = EagerGenerator()

    eager_generator.n = 3
    assert eager_generator.get_iterable() == [0, 1, 2]
    assert eager_generator.get_list() == [3]

    eager_generator.n = 0
    assert eager_generator.get_iterable() == []
    assert eager_generator.get_list() == [0]

# Generated at 2022-06-22 12:45:26.556073
# Unit test for function debug
def test_debug():
    import io
    from contextlib import redirect_stderr
    from unittest import mock
    with mock.patch('backwards.utils.settings', debug=True):
        f = io.StringIO()
        with redirect_stderr(f):
            debug(lambda: 'test')
        assert 'test' in f.getvalue()
    with mock.patch('backwards.utils.settings', debug=False):
        f = io.StringIO()
        with redirect_stderr(f):
            debug(lambda: 'test')
        assert f.getvalue() == ''



# Generated at 2022-06-22 12:45:27.980708
# Unit test for function eager
def test_eager():
    assert eager(lambda: (1, 2))() == [1, 2]

# Generated at 2022-06-22 12:45:30.682708
# Unit test for function get_source
def test_get_source():
    def test(): pass
    assert get_source(test) == 'pass'
    assert get_source(test) == 'pass'



# Generated at 2022-06-22 12:45:35.328612
# Unit test for function get_source
def test_get_source():

    def decorator(fn):
        return fn

    @decorator
    def decorated():
        def nested():
            pass
        return nested

    assert get_source(decorated) == 'def nested():\n    pass\nreturn nested\n'

# Generated at 2022-06-22 12:45:38.438076
# Unit test for function get_source
def test_get_source():
    # TODO: ensure that we are handling indentation properly
    def test_function():
        pass

    assert get_source(test_function) == 'def test_function():\n    pass\n'

# Generated at 2022-06-22 12:45:41.451387
# Unit test for function get_source
def test_get_source():
    import py_backwards

    def fn():
        pass

    assert get_source(fn) == 'def fn():\n    pass'
    assert get_source(py_backwards.backwards) == 'def backwards(function, version='

# Generated at 2022-06-22 12:45:43.797514
# Unit test for function debug
def test_debug():
    debug(lambda: 'a')
    settings.debug = True
    debug(lambda: 'a')



# Generated at 2022-06-22 12:45:46.508910
# Unit test for function get_source
def test_get_source():
    def function():
        print(123)

    assert get_source(function) == 'print(123)'

# Generated at 2022-06-22 12:45:50.681683
# Unit test for function eager
def test_eager():
    from py_backwards.utils import params
    @params(
        ([1, 2, 3],),
        ([0, 1, 2],),
        ([],),
    )
    @eager
    def gen(items: List[int]) -> Iterable[int]:
        yield from items
    assert gen() == list(gen())

# Generated at 2022-06-22 12:45:54.573057
# Unit test for function eager

# Generated at 2022-06-22 12:47:07.620799
# Unit test for function debug
def test_debug():
    from unittest import TestCase
    from unittest.mock import patch, MagicMock
    from . import settings as module_settings
    from . import messages as module_messages
    from .debug import debug

    class ModuleSettingsMock(TestCase):
        def setUp(self) -> None:
            self.debug = None
            module_settings.debug = self

        def __bool__(self) -> bool:
            return self.debug

        def __eq__(self, other: Any) -> bool:
            return super().__eq__(other)

        def __repr__(self) -> str:
            return super().__repr__()

    class ModuleMessagesMock(TestCase):
        def debug(self, message: str) -> str:
            return 'messages.debug(' + message + ')'

   

# Generated at 2022-06-22 12:47:09.154730
# Unit test for function debug
def test_debug():
    test_message = "This is debug log"
    assert debug(lambda: test_message) == None

# Generated at 2022-06-22 12:47:14.007796
# Unit test for function get_source
def test_get_source():
    def foo():
        """docstring"""
        print(1)
        print(2)

    assert get_source(foo) == 'print(1)\nprint(2)'



# Generated at 2022-06-22 12:47:20.267349
# Unit test for function debug
def test_debug():
    class Dummy:
        get_message_called = False

        @staticmethod
        def get_message() -> str:
            Dummy.get_message_called = True
            return ''

    try:
        settings.debug = False
        debug(Dummy.get_message)
    finally:
        settings.debug = True

    assert not Dummy.get_message_called

    debug(Dummy.get_message)
    assert Dummy.get_message_called

# Generated at 2022-06-22 12:47:24.995787
# Unit test for function get_source
def test_get_source():
    assert get_source(get_source) == "def get_source(fn: Callable[..., Any]) -> str:\n    \"\"\"Returns source code of the function.\"\"\"\n    source_lines = getsource(fn).split('\\n')\n    padding = len(re.findall(r'^(\\s*)', source_lines[0])[0])\n    return '\\n'.join(line[padding:] for line in source_lines)"

# Generated at 2022-06-22 12:47:27.407238
# Unit test for function get_source
def test_get_source():
    def a():
        pass

    assert get_source(a).split('\n') == ['def a():', '    pass']



# Generated at 2022-06-22 12:47:35.398907
# Unit test for function get_source
def test_get_source():  # pragma: no cover
    def add(a, b):
        return a + b

    def add_with_docstring(a, b):
        '''
        Adds two numbers.

        :param a: Number to add.
        :param b: Number to add.
        :return: Sum of two numbers.
        '''
        return a + b

    print(get_source(add))
    print(get_source(add_with_docstring))


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:47:38.275165
# Unit test for function get_source
def test_get_source():
    def foo(): pass

    assert get_source(foo) == 'def foo(): pass'

    def bar():
        pass

    assert get_source(bar) == 'def bar():\n    pass'


# Generated at 2022-06-22 12:47:39.281441
# Unit test for function debug
def test_debug():
    debug(lambda: "debug message")

# Generated at 2022-06-22 12:47:46.672584
# Unit test for function get_source
def test_get_source():
    # Function is defined
    def f1():
        pass
    # Function is defined using lambda
    f2 = lambda: None
    # Function is defined using function object
    f3 = FunctionType(None, None)
    # Test simple function
    assert get_source(f1) == 'pass'
    # Test lambda
    assert get_source(f2) == 'None'
    # Test function object
    assert get_source(f3) == 'None'

