

# Generated at 2022-06-22 12:38:26.115889
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        for i in range(10):
            yield i

    assert gen() == [i for i in range(10)]
# End of unit test



# Generated at 2022-06-22 12:38:29.078070
# Unit test for function eager
def test_eager():
    assert hasattr(eager(lambda x: x), '__wrapped__')
    assert eager(lambda x: range(x))(5) == [0, 1, 2, 3, 4]
    assert eager(lambda x: x)(5) == [5]

# Generated at 2022-06-22 12:38:30.130114
# Unit test for function debug
def test_debug():
    print('DEBUG')
    debug(lambda: 'debug_message')



# Generated at 2022-06-22 12:38:33.538070
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    _foo_source = get_source(foo)
    assert _foo_source == 'def foo():\n' \
                         '    pass'
test_get_source()

# Generated at 2022-06-22 12:38:34.965959
# Unit test for function get_source
def test_get_source():
    def test():
        """
        Function test.
        """
        return 123

    assert """Function test.""" == get_source(test)

# Generated at 2022-06-22 12:38:36.812851
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'def foo():\n    pass\n'

# Generated at 2022-06-22 12:38:42.009003
# Unit test for function eager
def test_eager():
    from collections import Counter

    @eager
    def f(*args: Any, **kwargs: Any) -> Iterable[str]:
        for i in range(2):
            yield str(i)

    assert f(1, 2, 3) == ['0', '1']
    assert f(Counter('qwerty')) == ['0', '1']


# Unit tests for function get_source

# Generated at 2022-06-22 12:38:44.316575
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    assert get_source(function) == 'def function():\n    pass\n'



# Generated at 2022-06-22 12:38:52.555787
# Unit test for function debug
def test_debug():
    from .testing import capture

    debug_message = "messagemessagemessagemessagemessage"
    def get_message():
        return debug_message

    with capture(settings.debug_out) as out:
        debug(get_message)
        assert debug_message in out.getvalue()
    with capture(settings.debug_out) as out:
        settings.debug = False
        debug(get_message)
        assert debug_message not in out.getvalue()
        settings.debug = True
    with capture(settings.debug_out) as out:
        settings.debug_out = sys.stdout
        debug(get_message)
        assert debug_message in out.getvalue()
        settings.debug_out = sys.stderr


# Generated at 2022-06-22 12:38:55.470733
# Unit test for function get_source
def test_get_source():  # pragma: no cover
    source = 'def test():\n    print(1)'
    assert get_source(test) == source

# Generated at 2022-06-22 12:38:59.144629
# Unit test for function debug
def test_debug():
    def foo():
        return 'bar'
    debug(foo)
    settings.debug = True
    debug(foo)



# Generated at 2022-06-22 12:39:02.890825
# Unit test for function get_source
def test_get_source():
    def add(a, b):
        return a + b

    assert get_source(add) == 'return a + b'


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:39:05.469346
# Unit test for function eager
def test_eager():
    @eager
    def generator():
        for x in range(2):
            yield x

    assert generator() == [0, 1]

# Generated at 2022-06-22 12:39:07.078041
# Unit test for function get_source
def test_get_source():
    def foo():
        """Docstring of foo."""
        pass



# Generated at 2022-06-22 12:39:09.058436
# Unit test for function eager
def test_eager():
    @eager
    def generator():
        for i in range(4):
            yield i

    assert generator() == [0, 1, 2, 3]


# Generated at 2022-06-22 12:39:10.499790
# Unit test for function get_source
def test_get_source():
    source = 'def foo():\n    pass\n'
    assert get_source(foo) == source



# Generated at 2022-06-22 12:39:18.669397
# Unit test for function get_source
def test_get_source():
    import pytest
    def test_func():
        """This is doc
        line 1
        line 2
        """
        pass
    source_lines = get_source(test_func).split('\n')
    assert source_lines[0] == 'def test_func():'
    assert source_lines[1] == "    \"\"\"This is doc"
    assert source_lines[2] == "    line 1"
    assert source_lines[3] == "    line 2"
    assert source_lines[4] == "    \""
    assert source_lines[5] == "    pass"

# Generated at 2022-06-22 12:39:26.122296
# Unit test for function get_source
def test_get_source():
    def function_with_docstring(a, b):
        """
        Docstring.
        """
        def inner_function(a, b):
            """
            Docstring.
            """
            print(a + b)

        print(a + b)

    assert get_source(function_with_docstring) == 'def inner_function(a, b):\n    """\n    Docstring.\n    """\n    print(a + b)\n\nprint(a + b)'
    assert get_source(function_with_docstring).count('\n') == 10

# Generated at 2022-06-22 12:39:30.068412
# Unit test for function get_source
def test_get_source():
    def a():
        pass
    assert get_source(a) == "def a():\n    pass"
    def b():
        b = 1
    assert get_source(b) == "def b():\n    b = 1"

# Generated at 2022-06-22 12:39:33.051759
# Unit test for function get_source
def test_get_source(): # noqa
    def test_func():
        pass

    assert get_source(test_func) == 'def test_func():\n    pass'



# Generated at 2022-06-22 12:39:38.474053
# Unit test for function eager
def test_eager():
    def proc(num: int) -> Iterable[int]:
        for i in range(num):
            yield i
    assert eager(proc)(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert eager(proc)(1) == [0]


# Generated at 2022-06-22 12:39:39.861298
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    assert get_source(foo) == 'pass'

# Generated at 2022-06-22 12:39:42.000276
# Unit test for function get_source
def test_get_source():
    def source():
        pass

    expected = 'def source():\n    pass'
    assert get_source(source) == expected

# Generated at 2022-06-22 12:39:46.729623
# Unit test for function eager
def test_eager():
    from .. import reverse_trace
    @reverse_trace
    def function():
        yield 1
        yield 2
        return 3

    x = function()
    assert x == 3
    assert list(x) == [3, 2, 1]
    assert isinstance(function(), list)
    assert function() == [3, 2, 1]

# Generated at 2022-06-22 12:39:48.184919
# Unit test for function get_source
def test_get_source():
    def foo(x):
        return x

    assert get_source(foo) == 'return x'

# Generated at 2022-06-22 12:39:53.210063
# Unit test for function get_source
def test_get_source():
    def not_wrapped():
        pass

    def wrapped():
        pass

    assert 'def not_wrapped():' in get_source(not_wrapped)
    assert '@wraps(fn)' not in get_source(wrapped)
    assert 'def wrapped():' in get_source(wrapped)

# Generated at 2022-06-22 12:39:56.252145
# Unit test for function eager
def test_eager():
    def fn(a):
        for i in range(a):
            yield i
    assert eager(fn)(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-22 12:40:00.582879
# Unit test for function eager
def test_eager():
    @eager
    def inc(xs):
        for x in xs:
            yield x + 1
    assert inc(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    import pytest
    pytest.main(args=[__file__])

# Generated at 2022-06-22 12:40:01.786797
# Unit test for function get_source
def test_get_source():
    def function():
        pass

  

# Generated at 2022-06-22 12:40:03.778222
# Unit test for function get_source
def test_get_source():
    def fun(a: int, b: int) -> int:
        return a + b

    assert get_source(fun) == 'return a + b'

# Generated at 2022-06-22 12:40:10.177658
# Unit test for function eager
def test_eager():
    @eager
    def gen(a, b):
        yield a
        yield b

    assert gen(1, 2) == [1,2]


# Generated at 2022-06-22 12:40:13.044745
# Unit test for function debug
def test_debug():
    settings.debug = True
    assert debug(lambda: 'debug message') == None
    settings.debug = False
    assert debug(lambda: 'debug message') == None



# Generated at 2022-06-22 12:40:15.428175
# Unit test for function get_source
def test_get_source():
    def function():
        pass
    assert get_source(function) == 'def function():\n    pass'

# Generated at 2022-06-22 12:40:18.189010
# Unit test for function eager
def test_eager():
    assert eager(iter)(range(10)) == list(range(10))
    assert eager(iter)(range(10), x=10) == list(range(10))



# Generated at 2022-06-22 12:40:21.602689
# Unit test for function debug
def test_debug():
    c = []
    debug(lambda: c.append(1) or c.append(2) or c.append(3) or 'test')
    assert c == [1, 2, 3]



# Generated at 2022-06-22 12:40:26.550165
# Unit test for function debug
def test_debug():
    # Global variable debug
    debug_value = False
    def get_debug_value():
        global debug_value
        debug_value = True
        return 'unit test for debug'

    # Test for debug
    debug(get_debug_value)
    assert debug_value, 'Debug function not worked'

# Generated at 2022-06-22 12:40:29.197701
# Unit test for function get_source
def test_get_source():
    def dummy(a, b, c):
        pass

    assert get_source(dummy) == "def dummy(a, b, c):\n    pass"

# Generated at 2022-06-22 12:40:33.334594
# Unit test for function debug
def test_debug():
    global_debug = settings.debug
    settings.debug = True
    message = 'A test message'
    try:
        # Run the function
        debug(lambda: message)
    finally:
        # Restore the existing value
        settings.debug = global_debug
    assert message in sys.stderr.getvalue()

# Generated at 2022-06-22 12:40:37.855688
# Unit test for function debug
def test_debug():
    class GetMessage:
        def __init__(self, message: str) -> None:
            self.messages = [messages.debug(message)]

        def get_message(self) -> str:
            return self.messages.pop()

    message = 'foo'
    settings.debug = True

    debug(GetMessage(message).get_message)
    assert GetMessage(message).messages == []

    settings.debug = False

    debug(GetMessage(message).get_message)
    assert GetMessage(message).messages == [message]

# Generated at 2022-06-22 12:40:43.088923
# Unit test for function debug
def test_debug():
    # pylint: disable=unused-variable

    def double_debug():
        debug(lambda: 'msg1')

        def nested_debug():
            debug(lambda: 'msg2')

        nested_debug()

    try:
        original_debug = settings.debug
        settings.debug = True
        double_debug()
    finally:
        settings.debug = original_debug



# Generated at 2022-06-22 12:40:56.253127
# Unit test for function get_source
def test_get_source():
    def inner() -> str:
        """It should return source code of the function."""
        def fn() -> None:
            '''
            Code:
                1:   line 1
                  2: line 2
            '''
            pass

        return get_source(fn)


# Generated at 2022-06-22 12:41:02.177470
# Unit test for function eager
def test_eager():
    from .fixtures import test_1_a
    from .fixtures import test_1_b
    from .fixtures import test_1_c
    assert eager(test_1_a)(1, 2) == [1, 2]
    assert eager(test_1_b)(1, 2) == [3, 4]
    assert eager(test_1_c)(1, 2) == [5, 6]



# Generated at 2022-06-22 12:41:04.652288
# Unit test for function eager
def test_eager():
    def my_func():
        yield 1
        yield 2
        yield 3

    assert eager(my_func)() == [1, 2, 3]



# Generated at 2022-06-22 12:41:08.836382
# Unit test for function debug
def test_debug():
    messages.debug = lambda m: '[DEBUG]: ' + m
    debug(lambda: 'test')
    assert sys.stderr.getvalue() == '[DEBUG]: test\n'
    sys.stderr.truncate(0)
    debug(lambda: 'test2')
    assert sys.stderr.getvalue() == ''


# Generated at 2022-06-22 12:41:11.527380
# Unit test for function get_source
def test_get_source():
    def f():
        pass
    source = 'def f():\n    pass\n'
    assert get_source(f) == source

# Generated at 2022-06-22 12:41:16.769072
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    # test that we strip leading whitespace
    def g():
        pass

    assert get_source(f) == 'def f():\n        pass'
    assert get_source(g) == '    def g():\n            pass'



# Generated at 2022-06-22 12:41:21.908270
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        ctx = {'counter': 0}

        def test_func():
            ctx['counter'] += 1
            debug(lambda: 'Test debug function {}'.format(ctx['counter']))
        test_func()
        assert ctx['counter'] == 1
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:41:27.236091
# Unit test for function debug
def test_debug():
    debug_message = 'debug message'

    def test_function():
        debug(lambda: debug_message)

    test_function()
    assert debug_message not in sys.stderr.getvalue()

    settings.debug = True
    sys.stderr.truncate(0)

    test_function()
    assert debug_message in sys.stderr.getvalue()

# Generated at 2022-06-22 12:41:29.452646
# Unit test for function get_source
def test_get_source():
    def foo():
        x = 1

        def bar():
            pass

    assert get_source(foo) == 'def bar():\n    pass'

# Generated at 2022-06-22 12:41:32.338358
# Unit test for function get_source
def test_get_source():
    def fn(x, y):
        return x + y

    assert get_source(fn) == 'return x + y'



# Generated at 2022-06-22 12:42:00.178981
# Unit test for function get_source
def test_get_source():
    def foo(thing):
        if len(thing) > 1:
            return 2
        elif len(thing) == 1:
            return 1
        else:
            return 0
    assert (
        get_source(foo) == """
if len(thing) > 1:
    return 2
elif len(thing) == 1:
    return 1
else:
    return 0
""".lstrip())



# Generated at 2022-06-22 12:42:03.699392
# Unit test for function debug
def test_debug():
    def get_message(): return 'Message'
    with Patch('sys.stderr', spec=sys.stderr) as mock_stderr:
        debug(get_message)
        mock_stderr.assert_called_once_with(messages.debug('Message'))

# Generated at 2022-06-22 12:42:05.678907
# Unit test for function debug
def test_debug():
    return [
        (settings.debug, True, 1),
        (settings.debug, False, 0),
    ]


# Generated at 2022-06-22 12:42:09.989876
# Unit test for function eager
def test_eager():
    @eager
    def square_range(x: int) -> Iterable[int]:
        for i in range(x):
            yield i ** 2

    assert square_range(5) == [0, 1, 4, 9, 16]


# Generated at 2022-06-22 12:42:12.137794
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'some debug message')
    settings.debug = False

if __name__ == '__main__':
    test_debug()

# Generated at 2022-06-22 12:42:14.964859
# Unit test for function get_source
def test_get_source():
    def foo():
        """Docstring."""
        bar = 'bar'
        print(bar)


# Generated at 2022-06-22 12:42:19.569349
# Unit test for function debug
def test_debug():
    count = 0

    def get_message():
        nonlocal count
        count += 1
        return 'hi'

    debug(get_message)
    assert count == 0

    settings.debug = True
    debug(get_message)
    assert count == 1

    settings.debug = False
    debug(get_message)
    assert count == 1



# Generated at 2022-06-22 12:42:30.430651
# Unit test for function debug
def test_debug():
    test_messages = []

    def get_message():
        return 'This is the message'

    def override_print(message, file=None, **_):
        test_messages.append(message)
    orig_print = __builtins__.print
    __builtins__.print = override_print

    settings.debug = True
    debug(get_message)


# Generated at 2022-06-22 12:42:32.515489
# Unit test for function eager
def test_eager():
    def gen():
        for i in range(3):
            yield i

    assert list(gen()) == eager(gen)()

# Generated at 2022-06-22 12:42:33.570417
# Unit test for function get_source

# Generated at 2022-06-22 12:43:01.040579
# Unit test for function get_source
def test_get_source():
    def a(b, c=123):
        return 1
        5
        # This is not a comment
        """
        A
        8

        """

    # noinspection PyUnusedLocal
    def b(a, b, c=123, d=None):
        pass

    assert get_source(a) == 'def a(b, c=123):\n' \
                            '    return 1\n' \
                            '    5\n' \
                            '    # This is not a comment\n' \
                            '    """\n' \
                            '    A\n' \
                            '    8\n' \
                            '\n' \
                            '    """\n'


# Generated at 2022-06-22 12:43:02.393411
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2
    assert f() is not eager(f)()

# Generated at 2022-06-22 12:43:04.088313
# Unit test for function get_source

# Generated at 2022-06-22 12:43:05.604682
# Unit test for function get_source
def test_get_source():
    def test_function():
        pass
    assert get_source(test_function) == 'pass'

# Generated at 2022-06-22 12:43:09.045977
# Unit test for function get_source
def test_get_source():
    def foo(bar, var1, var2):
        return [var1, var2]

    assert get_source(foo) == '\n'.join(
        [
            'def foo(bar, var1, var2):',
            '    return [var1, var2]',
            '',
        ]
    )

# Generated at 2022-06-22 12:43:20.657624
# Unit test for function get_source
def test_get_source():
    def test():
        return 'test'

    def test_with_args(arg1, arg2, arg3):
        return 'test'

    def test_with_args_and_annotation(arg1, arg2, arg3: int = 5):
        return 'test'

    def test_with_args_and_annotation_and_kwargs(*args, kwarg='test'):
        return 'test'

    def test_with_two_functions():
        def sub_test():
            return 'test'

        def sub_test_2():
            return 'test'

    assert get_source(test) == 'return "test"'
    assert get_source(test_with_args) == 'return "test"'
    assert get_source(test_with_args_and_annotation) == 'return "test"'

# Generated at 2022-06-22 12:43:25.766307
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f) == 'def f():\n    pass'

    def f1():
        """Docstring at the top.

        Second docstring line.
        """
        return 1
    assert get_source(f1) == 'def f1():\n    """Docstring at the top.\n\n    Second docstring line.\n    """\n    return 1'

# Generated at 2022-06-22 12:43:28.819451
# Unit test for function get_source
def test_get_source():
    def foo():
        baz(1, 2)
        bar(3, 4)

    assert get_source(foo) == \
        "baz(1, 2)\nbar(3, 4)"

# Generated at 2022-06-22 12:43:31.375193
# Unit test for function get_source
def test_get_source():
    def func():
        pass
    expected_source = dedent('''
        def func():
            pass
    ''')
    assert get_source(func) == expected_source


# Generated at 2022-06-22 12:43:33.560149
# Unit test for function get_source
def test_get_source():
    def some_function():
        pass

    source = get_source(some_function)
    assert r'def some_function():' in source



# Generated at 2022-06-22 12:44:28.886839
# Unit test for function eager
def test_eager():
    @eager
    def test_func(n: int) -> Iterable[int]:
        for i in range(n):
            yield i
    assert test_func(5) == [0, 1, 2, 3, 4]


# Generated at 2022-06-22 12:44:33.102724
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    expected_foo_source = "def foo():\n    pass\n"
    assert get_source(foo) == expected_foo_source

    def bar():
        if True:
            pass
    expected_bar_source = "    if True:\n        pass\n"
    assert get_source(bar) == expected_bar_source

# Generated at 2022-06-22 12:44:36.589830
# Unit test for function eager
def test_eager():
    @eager
    def add_one(num: int) -> Iterable[int]:
        yield num + 1

    assert add_one(1) == [2]

# Generated at 2022-06-22 12:44:39.272984
# Unit test for function eager
def test_eager():
    def test_func(a, b):
        for i in range(a, b):
            yield i
    assert eager(test_func)(0, 1) == [0]

# Generated at 2022-06-22 12:44:47.328457
# Unit test for function get_source
def test_get_source():
    assert get_source(get_source) == ("def get_source(fn: Callable[..., Any]) -> str:\n"
            "    \"\"\"Returns source code of the function.\"\"\"\n"
            "    source_lines = getsource(fn).split('\\n')\n"
            "    padding = len(re.findall(r'^(\\s*)', source_lines[0])[0])\n"
            "    return '\\n'.join(line[padding:] for line in source_lines)\n")

# Generated at 2022-06-22 12:44:49.485650
# Unit test for function eager
def test_eager():
    def test_iterator():
        for i in range(5):
            yield i

    assert eager(test_iterator)() == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:44:53.006868
# Unit test for function eager
def test_eager():
    @eager
    def test_function(x: int) -> Iterable[int]:
        return map(lambda y: y * 2, range(x))
    assert test_function(5) == [0, 2, 4, 6, 8]

# Generated at 2022-06-22 12:44:57.977512
# Unit test for function debug
def test_debug():
    debug_messages = []
    def dbg_message():
        debug_messages.append('Debug message')
        return 'Debug message'
 
    debug(dbg_message)
    assert debug_messages == []
    settings.debug = True
    debug(dbg_message)
    assert debug_messages == ['Debug message']

# Generated at 2022-06-22 12:44:59.891147
# Unit test for function eager
def test_eager():
    def foo():
        yield 1
    bar = eager(foo)
    assert bar() == [1]


# Generated at 2022-06-22 12:45:03.045759
# Unit test for function get_source
def test_get_source():
    def f():
        """Test function for get_source."""
        pass

    assert get_source(f) == 'def f():\n    """Test function for get_source."""\n    pass'

# Generated at 2022-06-22 12:47:03.963734
# Unit test for function eager
def test_eager():
    assert eager(range)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:47:05.065844
# Unit test for function eager
def test_eager():
    assert eager(range)(5) == [0, 1, 2, 3, 4]

# Generated at 2022-06-22 12:47:08.174522
# Unit test for function eager
def test_eager():
    def f():
        yield 1
        yield 2

    g = eager(f)
    assert g() == [1, 2]

test_eager()

# Generated at 2022-06-22 12:47:13.421959
# Unit test for function debug
def test_debug():
    old_settings = settings.debug
    settings.debug = True
    debug(lambda: "debug message")
    settings.debug = False
    debug(lambda: "debug message")
    settings.debug = old_settings


# Generated at 2022-06-22 12:47:20.183263
# Unit test for function debug
def test_debug():
    import io
    import sys

    old = sys.stderr
    try:
        sys.stderr = io.StringIO()
        settings.debug = True
        debug(lambda: 'Hello')
        assert 'Hello' in sys.stderr.getvalue()
        sys.stderr = io.StringIO()
        settings.debug = False
        debug(lambda: 'Hello')
        assert not sys.stderr.getvalue()
    finally:
        sys.stderr = old



# Generated at 2022-06-22 12:47:22.462009
# Unit test for function eager
def test_eager():
    def foo():
        yield 1
        yield 2
        yield 3

    assert eager(foo)() == [1, 2, 3]

# Generated at 2022-06-22 12:47:23.901755
# Unit test for function debug
def test_debug():
    def get_message():
        return 'foo'
    debug(get_message)


# Generated at 2022-06-22 12:47:27.116317
# Unit test for function get_source
def test_get_source():
    @add_debug_info
    def func():
        pass

    assert get_source(func) == dedent("""
        @add_debug_info
        def func():
            pass
    """)

# Generated at 2022-06-22 12:47:38.372960
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    def g():
        """

        """

    def h():
        """
        Multiline
        comment
        """

    def i():
        '''
        Multiline
        comment
        '''

    # No padding
    assert get_source(f) == 'def f():\n    pass'

    # No padding
    assert get_source(g) == 'def g():\n    """\n\n    """\n'

    # Single line padding
    assert get_source(h) == 'def h():\n    """\n    Multiline\n    comment\n    """\n'

    # Single line padding

# Generated at 2022-06-22 12:47:45.370146
# Unit test for function get_source
def test_get_source():
    def test_fn_1(arg):
        # this is a test function
        return arg

    def test_fn_2(arg):
        # this is
        # another test function
        return arg

    assert get_source(test_fn_1) == 'def test_fn_1(arg):\n    return arg'
    assert get_source(test_fn_2) == 'def test_fn_2(arg):\n    return arg'