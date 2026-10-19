

# Generated at 2022-06-22 12:38:24.596709
# Unit test for function get_source
def test_get_source():
    def f():
        to_remove = 1
        return to_remove
    code = get_source(f)
    assert code == 'return to_remove'

# Generated at 2022-06-22 12:38:26.753732
# Unit test for function debug
def test_debug():
    message = None
    debug(lambda: message)

    message = 'foo'
    assert(debug(lambda: message) == None)
#test_debug()



# Generated at 2022-06-22 12:38:37.369441
# Unit test for function eager
def test_eager():
    from inspect import isgeneratorfunction, isfunction
    from ..conf import load_settings

    @eager
    def numbers():
        for i in range(3):
            yield i

    @eager
    def get_list():
        return list(range(3))

    @eager
    def do_nothing(*args, **kwargs):
        pass

    assert isfunction(numbers)
    assert numbers() == [0, 1, 2]

    assert isfunction(get_list)
    assert get_list() == [0, 1, 2]

    assert isfunction(do_nothing)
    do_nothing()


# Generated at 2022-06-22 12:38:38.547961
# Unit test for function get_source
def test_get_source():
    def f():
        a = 1
        b = 2
        return a + b

    assert get_source(f) == 'a = 1\n' \
                            'b = 2\n' \
                            'return a + b'

# Generated at 2022-06-22 12:38:41.293116
# Unit test for function eager
def test_eager():
    def foo() -> Iterable[int]:
        yield 1
        yield 2
        yield 3
    
    assert foo() == [1, 2, 3]

# Generated at 2022-06-22 12:38:45.876505
# Unit test for function get_source
def test_get_source():
    def foo():
        """Foo."""
        a = 1
        return a
    print(get_source(foo))
    assert get_source(foo) == """    a = 1
    return a"""



# Generated at 2022-06-22 12:38:48.440764
# Unit test for function eager
def test_eager():
    @eager
    def test_fn():
        yield 1
        yield 2
        yield 3

    assert test_fn() == [1, 2, 3]

# Generated at 2022-06-22 12:38:58.993341
# Unit test for function debug
def test_debug():
    messages.DEBUG_MARK = 'TEST-DEBUG'
    messages.WARN_MARK = 'TEST-WARN'
    get_message = lambda: 'test message'
    output = StringIO()
    debug_backup = sys.stderr, sys.stderr.write
    sys.stderr, sys.stderr.write = output, output.write
    try:
        debug(get_message)
        assert output.getvalue() == messages.debug(get_message()) + '\n'
        settings.debug = False
        output.seek(0)
        output.truncate()
        debug(get_message)
        assert output.getvalue() == ''
    finally:
        settings.debug = True
        sys.stderr, sys.stderr.write = debug_backup

# Generated at 2022-06-22 12:39:02.395882
# Unit test for function eager
def test_eager():
    from inspect import signature

    @eager
    def my_range(n):
        return range(n)

    assert signature(my_range) == signature(list)

# Generated at 2022-06-22 12:39:04.439343
# Unit test for function get_source
def test_get_source():
    
    def test_fn():
        pass

    assert """def test_fn():
    pass""" == get_source(test_fn)

# Generated at 2022-06-22 12:39:07.873159
# Unit test for function get_source
def test_get_source():
    def foo(x: str) -> int:
        return int(x)

    assert get_source(foo) == 'return int(x)'

# Generated at 2022-06-22 12:39:10.177721
# Unit test for function get_source
def test_get_source():
    @get_source
    def test_function():
        print("test")
        return "test"

    assert test_function.__wrapped__() == 'print("test")\nreturn "test"'



# Generated at 2022-06-22 12:39:11.577819
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'test')

# Generated at 2022-06-22 12:39:12.475259
# Unit test for function debug
def test_debug():
    debug(lambda: "message")



# Generated at 2022-06-22 12:39:21.375757
# Unit test for function debug
def test_debug():
    assert settings.debug is False
    debug_messages = []

    def get_message():
        debug_messages.append('test_debug_message')
        return 'test_debug_message'

    debug(get_message)

    assert len(debug_messages) == 0

    with settings.update(debug=True):
        assert settings.debug
        debug(get_message)
        assert len(debug_messages) == 1

        debug(get_message)
        assert len(debug_messages) == 2

    assert len(debug_messages) == 2
    with settings.update(debug=False):
        assert settings.debug is False



# Generated at 2022-06-22 12:39:30.954498
# Unit test for function get_source

# Generated at 2022-06-22 12:39:33.757086
# Unit test for function get_source
def test_get_source():
    def my_func():
        """Doc string."""
        first = 1
        second = 2
        return first + second


# Generated at 2022-06-22 12:39:38.679787
# Unit test for function get_source
def test_get_source():
    def f(x):
        def g(y):
            def h(z):
                return z+1
            return h(y)+1
        return g(x)+1
    assert get_source(f) == 'def f(x):\n    def g(y):\n        def h(z):\n            return z+1\n        return h(y)+1\n    return g(x)+1'

# Generated at 2022-06-22 12:39:42.605034
# Unit test for function get_source
def test_get_source():
    source = get_source(test_get_source)
    assert re.search(r'^def test_get_source\(\)', source)
    assert re.search(r'get_source\(test_get_source\)$', source)



# Generated at 2022-06-22 12:39:44.478773
# Unit test for function get_source
def test_get_source():
    def test():
        """Test docstring"""
        pass

    assert get_source(test) == 'pass'

# Generated at 2022-06-22 12:39:50.835601
# Unit test for function get_source
def test_get_source():
    def function():
        line1 = 1
        line2 = 1
        line3 = 1
    assert get_source(function) == '\n'.join(['line1 = 1', 'line2 = 1', 'line3 = 1'])

# Generated at 2022-06-22 12:39:55.863423
# Unit test for function get_source
def test_get_source():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    expected = '''
if n == 0:
    return 1
else:
    return n * factorial(n - 1)
'''
    assert get_source(factorial).strip() == expected.strip()

# Generated at 2022-06-22 12:39:57.878290
# Unit test for function get_source
def test_get_source():
    @add_one
    def foo():
        return 2
    
    assert get_source(foo) == 'return 2 + 1'



# Generated at 2022-06-22 12:40:00.566409
# Unit test for function get_source
def test_get_source():
    def f(a: int, b: int) -> int:
        return a + b

    assert get_source(f) == 'return a + b'

# Generated at 2022-06-22 12:40:02.118152
# Unit test for function get_source
def test_get_source():
    def func():
        pass

    assert 'pass' in get_source(func)

# Generated at 2022-06-22 12:40:05.093323
# Unit test for function get_source
def test_get_source():
    def foo():
        """Some doc"""
        return True

    source = get_source(foo)

# Generated at 2022-06-22 12:40:08.580505
# Unit test for function get_source
def test_get_source():
    def foo() -> None:
        pass

    assert get_source(foo) == 'pass\n'

    def bar():
        pass

    assert get_source(bar) == 'pass\n'

# Generated at 2022-06-22 12:40:11.194322
# Unit test for function get_source
def test_get_source():
    def test():
        # This line is indented.
        pass

    assert '\n'.join(['# This line is indented.', 'pass']) == get_source(test)

# Generated at 2022-06-22 12:40:23.031480
# Unit test for function debug
def test_debug():
    # pylint: disable=unused-variable, missing-docstring
    import sys

    class FakeFile:
        def __init__(self) -> None:
            self.lines = []

        def write(self, line: str) -> None:
            self.lines.append(line)

        def flush(self) -> None:
            assert False, 'FakeFile.flush() should not be called'

    def test_msg(msg: str) -> None:
        saved_stderr = sys.stderr  # type: ignore
        try:
            _file = FakeFile()
            sys.stderr = _file  # type: ignore
            debug(lambda: msg)
            assert _file.lines == [messages.debug(msg)]
        finally:
            sys.stderr = saved_stderr  # type

# Generated at 2022-06-22 12:40:30.690272
# Unit test for function debug
def test_debug():
    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        settings.debug = True
        debug(lambda: 'foo')
        assert mock_stderr.getvalue() == messages.debug('foo') + '\n'

        mock_stderr.truncate(0)

        settings.debug = False
        debug(lambda: 'foo')
        assert mock_stderr.getvalue() == ''



# Generated at 2022-06-22 12:40:40.589446
# Unit test for function get_source
def test_get_source():
    """Get source code of function and test it."""
    source = get_source(test_get_source)

# Generated at 2022-06-22 12:40:45.990697
# Unit test for function get_source
def test_get_source():
    def test_get_source_inner():
        pass

    expected_source = '        pass'

    assert get_source(test_get_source_inner) == expected_source

    def test_get_source_inner2():
        pass
        pass

    expected_source = '        pass\n        pass'

    assert get_source(test_get_source_inner2) == expected_source



# Generated at 2022-06-22 12:40:49.039282
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    result = get_source(function)
    assert result == 'def function():\n    pass\n'

# Generated at 2022-06-22 12:40:51.131266
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            pass
    assert get_source(foo) == '\n    def bar():\n        pass\n'

# Generated at 2022-06-22 12:40:56.970820
# Unit test for function get_source
def test_get_source():
    source_lines = []

    def test_fn():
        source_lines.append('def test_fn():')
        source_lines.append('    source_lines.append("def test_fn():")')
        source_lines.append('    source_lines.append("    source_lines.append(\\"def test_fn():\\")")')

    assert get_source(test_fn) == '\n'.join(source_lines)

# Generated at 2022-06-22 12:40:58.883134
# Unit test for function eager
def test_eager():
    def generator():
        for i in range(10):
            yield i
    print(eager(generator)())

# Generated at 2022-06-22 12:41:01.081542
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass

    assert get_source(test_func) == 'def test_func():\n    pass'

# Generated at 2022-06-22 12:41:11.016815
# Unit test for function get_source

# Generated at 2022-06-22 12:41:12.939618
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'Hello debug')
    settings.debug = False

# Generated at 2022-06-22 12:41:15.980000
# Unit test for function eager
def test_eager():
    def a(n):
        i = 0
        while i < n:
            yield i
            i += 1

    a = eager(a)
    assert a(10) == list(range(10))

# Generated at 2022-06-22 12:41:41.039323
# Unit test for function get_source
def test_get_source():
    def test():
        """Test function"""
        var = 1
        for _ in range(3):
            pass

    expected_result = '''def test():
    """Test function"""
    var = 1
    for _ in range(3):
        pass
'''
    assert get_source(test) == expected_result

# Generated at 2022-06-22 12:41:44.155913
# Unit test for function get_source
def test_get_source():
    def f():
        pass
    assert get_source(f) == 'def f():\n    pass\n'



# Generated at 2022-06-22 12:41:49.656486
# Unit test for function get_source
def test_get_source():
    def sample1_fn():
        pass

    def sample2_fn():
        pass

    sample1_source = 'def sample1_fn():\n    pass\n'
    assert get_source(sample1_fn) == sample1_source
    sample2_source = 'def sample2_fn():\n    pass\n'
    assert get_source(sample2_fn) == sample2_source

# Generated at 2022-06-22 12:41:54.071986
# Unit test for function eager
def test_eager():
    from typing import List
    @eager
    def gen(colors: List[str]) -> List[int]:
        for color in colors:
            yield len(color)
    assert gen(colors=['red', 'green', 'blue']) == [3, 5, 4]

# Generated at 2022-06-22 12:42:04.139328
# Unit test for function get_source
def test_get_source():
    def source() -> str:
        return 'def source() -> str:\n  return 1\n'

    def no_arguments() -> str:
        return '    return 1\n'

    def no_return() -> str:
        return 'def no_return() -> str:\n'

    def with_args(*args: Any, **kwargs: Any) -> str:
        return 'def with_args(*args: Any, **kwargs: Any) -> str:\n'

    def with_module() -> str:
        return 'import module\ndef with_module() -> str:\n    return 1\n'

    assert get_source(source) == 'return 1'
    assert get_source(no_arguments) == 'return 1'
    assert get_source(no_return) == ''

# Generated at 2022-06-22 12:42:05.680006
# Unit test for function get_source
def test_get_source():
    def source_fn():
        pass

    assert get_source(source_fn) == 'pass\n'

# Generated at 2022-06-22 12:42:11.815478
# Unit test for function debug
def test_debug():
    from io import StringIO
    import sys
    sys.stderr = StringIO()
    settings.debug = True
    def get_message():
        return "yay"
    debug(get_message)
    settings.debug = False
    debug(get_message)
    get_message = "boo"
    sys.stderr = sys.__stderr__


# Generated at 2022-06-22 12:42:14.924523
# Unit test for function debug
def test_debug():
    try:
        settings.debug = True
        debug(lambda: 'testing debug')
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:42:16.153717
# Unit test for function eager
def test_eager():
    assert eager(range)(1, 4) == [1, 2, 3]

# Generated at 2022-06-22 12:42:26.594685
# Unit test for function debug
def test_debug():
    # pylint: disable=W0212
    class MockStream:
        def __init__(self):
            self.written = []

        def write(self, text):
            self.written.append(text)

    old_stdout = sys.stderr
    old_debug = settings.debug

    try:
        sys.stderr = MockStream()
        settings.debug = True
        debug(lambda: 'foo')
        assert sys.stderr.written == ['\x1b[0;30m\x1b[47mDEBUG:foo\x1b[0m\n']
        sys.stderr.written = []
        settings.debug = False
        debug(lambda: 'bar')
        assert sys.stderr.written == []
    finally:
        sys.stderr = old_std

# Generated at 2022-06-22 12:43:16.546042
# Unit test for function get_source
def test_get_source():
    def foo():
        if True:
            a = 1 + 1
        return a

    assert get_source(foo) == (
        "if True:\n"
        "    a = 1 + 1\n"
        "return a"
    )

# Generated at 2022-06-22 12:43:19.413135
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == """def test_get_source():
    assert get_source(test_get_source) == get_source_string"""



# Generated at 2022-06-22 12:43:21.853040
# Unit test for function debug
def test_debug():
    settings.debug = True
    messages._debug_format = lambda message: 'DEBUG: {}'.format(message)
    debug(lambda: 'Hello, world!')



# Generated at 2022-06-22 12:43:26.624466
# Unit test for function debug
def test_debug():
    output = StringIO()
    sys.stderr = output
    try:
        settings.debug = True
        debug(lambda: 'test message')
        assert 'test message' in output.getvalue()
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:43:30.811366
# Unit test for function get_source
def test_get_source():
    """Unit test for function get_source.

    This is a bit tricky test, but this function should return the following:
        def foo():
            pass
    """
    # noinspection PyUnusedLocal
    def foo():
        pass
    expected = "def foo():\n    pass"
    assert get_source(foo) == expected

# Generated at 2022-06-22 12:43:32.873926
# Unit test for function get_source
def test_get_source():
    def get_source(input):
        return get_source(input)

    assert get_source(get_source) == '    return get_source(input)\n'

# Generated at 2022-06-22 12:43:34.134730
# Unit test for function eager
def test_eager():
    assert eager(set)([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-22 12:43:35.799855
# Unit test for function get_source
def test_get_source():

    def func():
        pass

    assert get_source(func) == "def func():\n    pass"

# Generated at 2022-06-22 12:43:40.443424
# Unit test for function debug
def test_debug():
    from unittest import TestCase, mock
    from io import StringIO
    from .conf import Settings
    Settings.debug = True
    with mock.patch('sys.stderr', new=StringIO()) as mocked_stderr:
        debug(lambda: 'test message')
        assert mocked_stderr.getvalue() == 'DEBUG: test message\n'
    Settings.debug = False

# Generated at 2022-06-22 12:43:47.441204
# Unit test for function debug
def test_debug():
    def get_message():
        return "message"

    class Capturing(list):
        def __enter__(self):
            self._stdout = sys.stderr
            sys.stderr = self._stringio = StringIO()
            return self
        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio    # free up some memory
            sys.stderr = self._stdout

    with Capturing() as output:
        debug(get_message)
        assert len(output) == 0

    with Capturing() as output:
        with settings.override(debug=True):
            debug(get_message)
            assert len(output) == 1
            assert messages.debug("message") in output[0]



# Generated at 2022-06-22 12:44:39.159130
# Unit test for function debug
def test_debug():
    messages.test_mode = True
    debug(lambda: 'test')
    messages.test_mode = False

# Generated at 2022-06-22 12:44:44.480596
# Unit test for function debug
def test_debug():
    saved_debug = settings.debug
    try:
        settings.debug = False
        output = StringIO()
        with redirect_stdout(output):
            debug(lambda: 'This message should not be printed.')
        assert output.getvalue() == ''
    finally:
        settings.debug = saved_debug



# Generated at 2022-06-22 12:44:46.510092
# Unit test for function get_source
def test_get_source():
    def test_function():
        return 2
    assert get_source(test_function) == "return 2"

# Generated at 2022-06-22 12:44:48.727417
# Unit test for function get_source
def test_get_source():
    def add(x: int, y: int) -> int:
        return x + y
    assert get_source(add) == 'return x + y'



# Generated at 2022-06-22 12:44:55.843456
# Unit test for function debug
def test_debug():
    settings.debug = True
    print_counter = 0

    def print_message(string):
        nonlocal print_counter
        assert string.startswith('DEBUG')
        print_counter += 1

    with mock.patch('sys.stderr', spec=sys.stderr, autospec=True) as stderr:
        stderr.write.side_effect = print_message
        debug(lambda: 'foo')
        assert print_counter == 1

        settings.debug = False
        debug(lambda: 'bar')
        assert print_counter == 1


# Generated at 2022-06-22 12:45:01.702522
# Unit test for function debug
def test_debug():
    from unittest.mock import patch
    stderr = patch('sys.stderr')
    setting_debug = patch.object(settings, 'debug', True)

    with stderr as mock_stderr, setting_debug:
        debug(lambda: 'foo')

    mock_stderr.assert_called_with(messages.debug('foo'), file=sys.stderr)



# Generated at 2022-06-22 12:45:03.535885
# Unit test for function eager
def test_eager():
    assert eager(lambda x: range(x))(5) == list(range(5))



# Generated at 2022-06-22 12:45:05.580123
# Unit test for function get_source
def test_get_source():
    def foo(x, y=2):
        return x + y

    assert get_source(foo) == 'return x + y'



# Generated at 2022-06-22 12:45:07.280913
# Unit test for function eager
def test_eager():
    assert eager(range)(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-22 12:45:11.530755
# Unit test for function get_source
def test_get_source():
    def func():
        pass

    assert get_source(func) == 'pass'

    def func():
        if 1:
            pass

    assert get_source(func) == 'if 1:\n    pass'

    def func():
        if 1:

            pass

    assert get_source(func) == 'if 1:\n\n   pass'

# Generated at 2022-06-22 12:46:17.113651
# Unit test for function get_source
def test_get_source():
    from textwrap import dedent
    source_path = 'tests/fixtures/source.py'
    def f():
        print(1)
    assert get_source(f) == dedent(getsource(f)).strip()
    def f():
        print(1)
    assert get_source(f) == dedent(getsource(f)).strip()
    assert get_source(open) == dedent(getsource(open)).strip()

# Generated at 2022-06-22 12:46:21.436086
# Unit test for function eager
def test_eager():
    @eager
    def range_function(i):
        """Yields numbers 1 to i"""
        for j in range(i, 0, -1):
            yield j

    assert range_function(10) == list(range(10, 0, -1))

# Generated at 2022-06-22 12:46:30.335849
# Unit test for function debug
def test_debug():
    from ..conf import settings
    from unittest import mock

    debug_value = False

    def get_message():
        return 'message'

    with mock.patch('sys.stderr', new=mock.Mock()) as stderr:
        debug(get_message)
        assert stderr.write.called == False

        settings.debug = True

        debug(get_message)
        stderr.write.assert_called_with('{}message{}\n'.format(
            messages.DEBUG_COLOR, messages.ENDC))

        settings.debug = False

# Generated at 2022-06-22 12:46:39.040975
# Unit test for function get_source
def test_get_source():
    @test_get_source.test_decorator_test
    def test_decorator_test():
        def test_func_1(a, b):
            a = b
            return a + b
        def test_func_2(a, b):
            '''
            This is a docstring
            '''
            if a:
                b = a + 1
            for b in a:
                pass
        expected_source_1 = (
            'def test_func_1(a, b):\n'
            '    a = b\n'
            '    return a + b'
        )

# Generated at 2022-06-22 12:46:45.488891
# Unit test for function debug
def test_debug():
    import sys
    import io

    sys.stderr = io.StringIO()
    settings.debug = True
    debug(lambda: 'aaa')
    settings.debug = False
    debug(lambda: 'bbb')
    assert sys.stderr.getvalue() == '\x1b[1m\x1b[94m'\
                                    'py: debug: aaa'\
                                    '\x1b[0m\n'
    sys.stdout = sys.__stderr__


# Generated at 2022-06-22 12:46:48.283276
# Unit test for function get_source
def test_get_source():
    def _test(fn):
        return get_source(fn)

    assert _test(test_get_source) == get_source(test_get_source)

# Generated at 2022-06-22 12:46:49.610804
# Unit test for function get_source
def test_get_source():
    def f():
        return 'hello'

    assert (get_source(f) == 'return \'hello\'')

# Generated at 2022-06-22 12:46:55.945976
# Unit test for function get_source
def test_get_source():
    def fn(a, b, c=3, *args, **kwargs):
        if a and b:
            raise Exception('haha')
        return [x for x in args]

    source = get_source(fn)
    assert source == (
        'def fn(a, b, c=3, *args, **kwargs):\n'
        '    if a and b:\n'
        '        raise Exception(\'haha\')\n'
        '    return [x for x in args]')


# Generated at 2022-06-22 12:46:58.010451
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug(lambda: 'debug message')
    finally:
        settings.debug = False



# Generated at 2022-06-22 12:47:05.038675
# Unit test for function get_source
def test_get_source():

    class TestClass:
        """Class for testing get_source function."""

        def __init__(self):
            self.attr = 'test'

        def test_method(self):
            """Method test_method for testing get_source function."""
            return True

        @staticmethod
        def test_static_method():
            """Method test_static_method for testing get_source function."""
            return True

    def test_function():
        """Function test_function for testing get_source function."""
        return True

    def test_function_with_kwargs(arg1, arg2, *args, arg3,  arg4=True, arg5=False, **kwargs):
        """Function test_function_with_kwargs for testing get_source function."""
        return True
