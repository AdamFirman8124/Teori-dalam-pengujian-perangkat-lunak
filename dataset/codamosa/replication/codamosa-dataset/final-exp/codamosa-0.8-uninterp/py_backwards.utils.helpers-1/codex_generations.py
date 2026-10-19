

# Generated at 2022-06-22 12:38:29.262400
# Unit test for function eager
def test_eager():
    @eager
    def get_x():
        yield 1
        yield 2
        yield 3
    x = get_x()
    assert x == [1, 2, 3]

# Generated at 2022-06-22 12:38:32.049501
# Unit test for function get_source
def test_get_source():
    def foo(a, b, c):
        if a > 1:
            bar(a, b, c)

    assert get_source(foo) == """def foo(a, b, c):
    if a > 1:
        bar(a, b, c)"""

# Generated at 2022-06-22 12:38:34.888026
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    def g():
        def h():
            pass
    assert get_source(f) == '\n'.join(['def f():', '    pass'])
    assert get_source(g) == '\n'.join(['def g():', '    def h():', '        pass'])

# Generated at 2022-06-22 12:38:37.968283
# Unit test for function get_source
def test_get_source():
    def example():
        x = 1
        y = 2
        print(x + y)

    source = get_source(example)
    assert source == 'x = 1\ny = 2\nprint(x + y)'

# Generated at 2022-06-22 12:38:40.965775
# Unit test for function eager
def test_eager():
    x = 0

    @eager
    def yield_range() -> Iterable[int]:
        range_ = range(5)
        for x in range_:
            yield x

    # the function yields all numbers from 0 to 4
    assert yield_range() == [0, 1, 2, 3, 4]

    # the function has been evaluated and therefore
    # x should be equal to 4, which is the highest number
    # yielded in all iterations
    assert x == 4


# Generated at 2022-06-22 12:38:42.909125
# Unit test for function eager
def test_eager():
    @eager
    def some_func():
        yield 1
        yield 2
        yield 3

    assert some_func() == [1, 2, 3]

# Generated at 2022-06-22 12:38:46.737583
# Unit test for function get_source
def test_get_source():
    def foo(a, b, c=0, d=1):
        pass
    assert get_source(foo) == 'def foo(a, b, c=0, d=1):\n    pass'

# Generated at 2022-06-22 12:38:55.934702
# Unit test for function get_source
def test_get_source():

    @py_backwards.function_to_generator
    def sum_numbers_to(number):
        numbers = range(1, number + 1)
        s = 0
        for i in numbers:
            s += i
            i = 0
        return s

    def sum_numbers_to_gen(number):
        numbers = range(1, number + 1)
        s = 0
        for i in numbers:
            s += i
            i = 0
            yield
        return s

    assert get_source(sum_numbers_to) == get_source(sum_numbers_to_gen)



# Generated at 2022-06-22 12:39:01.432405
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        debug_message = 'debug message'

        try:
            debug(lambda: debug_message)
        finally:
            debug_message = 'other message'

        assert debug_message == 'other message'

        debug(lambda: debug_message)
    finally:
        settings.debug = False



# Generated at 2022-06-22 12:39:03.071630
# Unit test for function eager
def test_eager():
    def fn():
        yield 1
        yield 2
    assert eager(fn)() == [1, 2]

# Generated at 2022-06-22 12:39:08.251245
# Unit test for function get_source
def test_get_source():
    def test_fn():
        if True:
            def inner_fn():
                pass

    assert get_source(test_fn) == 'if True:\n    def inner_fn():\n' \
                                  '        pass\n'

# Generated at 2022-06-22 12:39:09.668825
# Unit test for function debug
def test_debug():
    messages.debug = lambda msg: msg
    settings.debug = True
    debug(lambda: 'Test')
    raise Exception

# Generated at 2022-06-22 12:39:12.110866
# Unit test for function get_source
def test_get_source():
    def add(a, b):
        """Returns a+b"""
        return a + b

    code = get_source(add)

    assert code == 'def add(a, b):\n' \
                   '    """Returns a+b"""\n' \
                   '    return a + b'



# Generated at 2022-06-22 12:39:13.819076
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'hello')
    assert True

# Generated at 2022-06-22 12:39:14.858045
# Unit test for function get_source
def test_get_source():
    def fn():
        print(123)



# Generated at 2022-06-22 12:39:16.808696
# Unit test for function get_source
def test_get_source():
    def function():
        a = 1

    assert get_source(function) == 'a = 1'

# Generated at 2022-06-22 12:39:20.287811
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == dedent("""
    def test_get_source():
        assert get_source(test_get_source) == dedent("""
        """
        
        """
        )

# Generated at 2022-06-22 12:39:24.300863
# Unit test for function get_source
def test_get_source():
    def foo():
        pass

    def bar():
        pass

    print(f"\nTest for function get_source:\n")
    assert get_source(foo) == "def foo():\n    pass"
    assert get_source(bar) == "def bar():\n    pass"

# Generated at 2022-06-22 12:39:27.520483
# Unit test for function get_source
def test_get_source():
    def foo():
        return 1
    foo.__all__ = ["bar"]
    assert get_source(foo) == 'return 1'



# Generated at 2022-06-22 12:39:30.065527
# Unit test for function get_source
def test_get_source():
    def fn():
        return 1
    expected = 'return 1'
    actual = get_source(fn)
    assert actual == expected
    

# Generated at 2022-06-22 12:39:34.090014
# Unit test for function get_source
def test_get_source():
    def test():
        """Test"""
        pass

    assert get_source(test) == '"""Test"""\npass'

# Generated at 2022-06-22 12:39:36.281580
# Unit test for function get_source
def test_get_source():
    def foo():
        bar()

    def bar():
        pass

    assert get_source(bar) == 'def bar():\n    pass'

# Generated at 2022-06-22 12:39:39.250766
# Unit test for function get_source
def test_get_source():
    func_text = '''def f():
    pass
'''
    func = eval(func_text)
    assert func_text == get_source(func)

# Generated at 2022-06-22 12:39:41.326261
# Unit test for function eager
def test_eager():
    @eager
    def gen():
        yield 1
        yield 2
        yield 3
    assert gen() == [1, 2, 3]

# Generated at 2022-06-22 12:39:43.786809
# Unit test for function get_source
def test_get_source():
    def test():
        """
        This is a test of
        multiline comment
        """

    return get_source(test)

# Generated at 2022-06-22 12:39:47.269704
# Unit test for function debug
def test_debug():
    settings.debug = True
    try:
        def throw():
            raise Exception('message')

        try:
            debug(throw)
            assert False
        except Exception:
            assert True
    finally:
        settings.debug = False


# Generated at 2022-06-22 12:39:49.746769
# Unit test for function debug
def test_debug():
    settings.debug = True
    message = 'Debug message'
    debug(lambda: message)
    settings.debug = False
    debug(lambda: message)



# Generated at 2022-06-22 12:39:53.208657
# Unit test for function get_source
def test_get_source():
    def example(a, b):
        return a * b
    expected = 'return a * b'
    actual = get_source(example)
    assert actual == expected



# Generated at 2022-06-22 12:39:55.739465
# Unit test for function debug
def test_debug():
    if settings.debug:
        def get_message():
            return "Test debug message"

        debug(get_message)

# Generated at 2022-06-22 12:39:58.129902
# Unit test for function debug
def test_debug():
    def debug_message():
        return 'debug message'

    settings.debug = True
    debug(debug_message)
    settings.debug = False
    debug(debug_message)



# Generated at 2022-06-22 12:40:05.646790
# Unit test for function get_source
def test_get_source():
    def test():
        pass
    assert get_source(test).strip() == 'def test():'


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:40:09.405108
# Unit test for function get_source
def test_get_source():
    def test_example(a: int) -> int:
        return a + 1

    assert ('def test_example(a: int) -> int:\n'
            '    return a + 1\n') == get_source(test_example)



# Generated at 2022-06-22 12:40:11.551139
# Unit test for function eager
def test_eager():
    @eager
    def fn():
        yield 1
        yield 2

    assert fn() == [1, 2]

# Generated at 2022-06-22 12:40:14.924725
# Unit test for function get_source
def test_get_source():
    def foo():
        return 'bar'

    assert get_source(foo) == 'def foo():\n' \
                              '    return \'bar\'\n'



# Generated at 2022-06-22 12:40:18.677557
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'test')
    debug(lambda: 'test {}'.format(1))
    settings.debug = False
    debug(lambda: 'test')
    debug(lambda: 'test {}'.format(2))

# Generated at 2022-06-22 12:40:22.866580
# Unit test for function eager
def test_eager():
    # stub
    def gen_function():
        for i in range(4):
            yield i

    # sufix eager to test function
    gen_function = eager(gen_function)

    # assert
    assert isinstance(gen_function(), list)


# Generated at 2022-06-22 12:40:28.800139
# Unit test for function get_source
def test_get_source():
    def func():
        return 0

    def func2():
        a = 0
        return a

    def func3():
        a = 0
        b = 0
        return a, b

    assert get_source(func) == 'return 0'
    assert get_source(func2) == 'a = 0\nreturn a'
    assert get_source(func3) == 'a = 0\nb = 0\nreturn a, b'

# Generated at 2022-06-22 12:40:31.317695
# Unit test for function eager
def test_eager():
    @eager
    def foo() -> Iterable[int]:
        yield 1
        yield 2
        yield 3
    assert foo() == [1, 2, 3]

# Generated at 2022-06-22 12:40:34.725408
# Unit test for function eager
def test_eager():
    @eager
    def test_function(arg: int) -> Iterable[int]:
        for i in range(arg):
            yield i

    assert test_function(3) == [0, 1, 2]

# Generated at 2022-06-22 12:40:35.770435
# Unit test for function debug
def test_debug():
    debug(lambda: 'Hello!')

# Generated at 2022-06-22 12:40:46.848618
# Unit test for function eager
def test_eager():
    @eager
    def f():
        yield 1
        yield 2

    assert f() == [1, 2]

# Generated at 2022-06-22 12:40:51.037466
# Unit test for function debug
def test_debug():
    import io
    import sys

    settings.debug = True
    sys.stderr = io.StringIO()
    debug(lambda: 'test')
    assert sys.stderr.getvalue() == messages.debug('test') + '\n'



# Generated at 2022-06-22 12:40:53.068857
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert 'def foo():' in get_source(foo)

# Generated at 2022-06-22 12:40:55.441244
# Unit test for function get_source
def test_get_source():
    @variables_generator.generate('my_function')
    def my_function():
        pass
    assert get_source(my_function) == 'pass'



# Generated at 2022-06-22 12:41:05.605948
# Unit test for function debug
def test_debug():
    with patch('sys.stderr', new=StringIO()) as fake_stderr:
        debug(lambda: "debug message1")
        debug(lambda: "debug message2")
        debug(lambda: "debug message3")
        assert fake_stderr.getvalue() == ""

    settings.debug = True
    with patch('sys.stderr', new=StringIO()) as fake_stderr:
        debug(lambda: "debug message1")
        debug(lambda: "debug message2")
        debug(lambda: "debug message3")
        assert fake_stderr.getvalue() == messages.debug("debug message1") + "\n" \
                                        + messages.debug("debug message2") + "\n" \
                                        + messages.debug("debug message3") + "\n"
    settings.debug = False



# Generated at 2022-06-22 12:41:08.366672
# Unit test for function get_source
def test_get_source():
    def function(a, b):
        c = a + b
        return c
    assert get_source(function) == "        c = a + b\n        return c"

# Generated at 2022-06-22 12:41:13.495676
# Unit test for function debug
def test_debug():
    settings.debug = True
    with patch('sys.stderr') as mock:
        debug(lambda: 'message')
        settings.debug = False
        debug(lambda: 'message')
        assert mock.write.call_args_list == [call('\x1b[35mdebug\x1b[0m: message\n')]

# Generated at 2022-06-22 12:41:16.902713
# Unit test for function debug
def test_debug():
    messages.debug('DEBUG_MESSAGE')
    try:
        settings.debug = True
        debug(lambda: 'DEBUG_MESSAGE')
    finally:
        settings.debug = False

# Generated at 2022-06-22 12:41:20.455735
# Unit test for function eager
def test_eager():
    def generator(a, b):
        yield a + b
        yield a + b + 1

    assert eager(generator)(1, 2) == [3, 4]


# Generated at 2022-06-22 12:41:22.925286
# Unit test for function eager
def test_eager():
    def test(x):
        y = 100
        x = x + 2
        while x > 0:
            yield x
            x -= 1

    assert test(1) == eager(test)(1)

# Generated at 2022-06-22 12:41:45.180048
# Unit test for function debug
def test_debug():
    debug(lambda: 'Test debug')

# Generated at 2022-06-22 12:41:47.772744
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    source = get_source(function)
    assert isinstance(source, str)
    assert source == '        pass'

# Generated at 2022-06-22 12:41:48.602885
# Unit test for function debug
def test_debug():
    debug(lambda: 'test')

# Generated at 2022-06-22 12:41:56.867318
# Unit test for function debug
def test_debug():
    from unittest.mock import call
    from ..conf import settings
    from . import sys_monkeypatch
    from . import sys_mock

    settings.debug = True

    sys_monkeypatch.monkeypatch()
    try:
        sys_mock.mock()
        debug(lambda: 'test')
        sys.stderr.write.assert_called_once_with('test\n')
    finally:
        sys_monkeypatch.unmonkeypatch()
        sys_mock.unmock()

    settings.debug = False
sys_monkeypatch.add_to_path(__name__)

# Generated at 2022-06-22 12:41:58.198015
# Unit test for function get_source
def test_get_source():
    def f():
        pass
    assert get_source(f) == 'def f():'

# Generated at 2022-06-22 12:42:00.272044
# Unit test for function get_source
def test_get_source():
    def test(): pass
    result = get_source(test)
    assert result == "def test(): pass"

# Generated at 2022-06-22 12:42:01.627336
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 1)
    settings.debug = False

# Generated at 2022-06-22 12:42:05.647561
# Unit test for function eager
def test_eager():
    def test(x):
        for i in range(x):
            yield i
    # fmt: off
    assert test(5) == [0, 1, 2, 3, 4]
    assert eager(test)(5) == [0, 1, 2, 3, 4]
    # fmt: on

# Generated at 2022-06-22 12:42:09.630028
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'pass'

    def fn_with_spaces():
        pass

    assert get_source(fn_with_spaces) == 'pass'

# Generated at 2022-06-22 12:42:11.549716
# Unit test for function debug
def test_debug():
    original = settings.debug
    settings.debug = False
    try:
        assert not debug(lambda: 'TEST')
        settings.debug = True
        assert debug(lambda: 'TEST')
    finally:
        settings.debug = original

# Generated at 2022-06-22 12:42:37.554504
# Unit test for function debug
def test_debug():
    debug_msg = []  # type: List[str]

    def get_msg() -> str:
        debug_msg.append('get_msg')
        return 'msg'

    def _test():
        settings.debug = True
        debug(get_msg)
        assert debug_msg == ['get_msg']

        debug_msg.clear()
        settings.debug = False
        debug(get_msg)
        assert debug_msg == []

    _test()



# Generated at 2022-06-22 12:42:39.432427
# Unit test for function get_source
def test_get_source():  # pylint: disable=unused-variable
    def foo():
        pass



# Generated at 2022-06-22 12:42:42.364555
# Unit test for function get_source
def test_get_source():
    def foo():
        def bar():
            return

        return

    assert get_source(foo) == 'def bar():\n    return\n\nreturn'



# Generated at 2022-06-22 12:42:47.828030
# Unit test for function debug
def test_debug():
    import io
    import sys
    out = io.StringIO()
    try:
        sys.stderr = out
        settings.debug = True
        debug(lambda: 'test')
        assert 'test' in out.getvalue()
    finally:
        sys.stderr = sys.__stderr__
        settings.debug = False

# Generated at 2022-06-22 12:42:49.555096
# Unit test for function get_source
def test_get_source():
    def fn():
        pass

    assert get_source(fn) == 'def fn():\n    pass'



# Generated at 2022-06-22 12:42:50.505824
# Unit test for function get_source

# Generated at 2022-06-22 12:42:52.548038
# Unit test for function eager
def test_eager():
    @eager
    def gen(n):
        yield n
        yield n + 1

    assert gen(1) == [1, 2]

# Generated at 2022-06-22 12:42:56.282477
# Unit test for function debug
def test_debug():
    messages.debug = lambda m: '[DEBUG] {}'.format(m)
    debug(lambda: 'Are you there?')  # Prints '[DEBUG] Are you there?' to stderr
    settings.debug = False
    debug(lambda: 'Are you there?')  # Does nothing



# Generated at 2022-06-22 12:42:59.411707
# Unit test for function eager
def test_eager():
    def lazy() -> List[int]:
        yield 1
        yield 2
        yield 3

    assert eager(lazy)() == [1, 2, 3]



# Generated at 2022-06-22 12:43:07.075709
# Unit test for function debug
def test_debug():
    def f():
        settings.debug = False
        debug(lambda: 'test')
        settings.debug = True
        debug(lambda: 'test')
    import io
    saved_stdout = sys.stdout
    saved_stderr = sys.stderr
    try:
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()
        f()
        result = sys.stderr.getvalue()
    finally:
        sys.stdout = saved_stdout
        sys.stderr = saved_stderr
    assert result == '\u001b[3mDEBUG\u001b[0;39m: test\n', "debug fails to print the message when settings.debug is True"

# Generated at 2022-06-22 12:44:09.433621
# Unit test for function debug
def test_debug():
    class MockStdErr:
        def __init__(self):
            self.lines = []

        def write(self, line: str) -> None:
            self.lines.append(line)

    if __name__ == '__main__':
        sys.stderr = MockStdErr()

        def dummy():
            pass
        debug(dummy)
        assert sys.stderr.lines == []

        settings.debug = True
        debug(lambda: 'message')
        assert sys.stderr.lines == ['Debug: message']
        settings.debug = False

if __name__ == '__main__':
    import pytest, sys
    pytest.main([__file__] + sys.argv[1:])

# Generated at 2022-06-22 12:44:11.716088
# Unit test for function debug
def test_debug():
    def get_message():
        return 'heylo'
    print(debug(get_message))




# Generated at 2022-06-22 12:44:16.001902
# Unit test for function get_source
def test_get_source():
    def foo(bar, baz):
        fizz = 42
        return bar * fizz

    assert get_source(foo) == "foo(bar, baz):\n" \
                              "    fizz = 42\n" \
                              "    return bar * fizz"



# Generated at 2022-06-22 12:44:17.509534
# Unit test for function debug
def test_debug():
    # You should see 'DEBUG: test message' in stderr
    debug(lambda: 'test message')

# Generated at 2022-06-22 12:44:19.479892
# Unit test for function eager
def test_eager():
    @eager
    def foo():
        yield 1
        yield 2
        yield 3

    assert foo() == [1, 2, 3]



# Generated at 2022-06-22 12:44:25.163990
# Unit test for function get_source
def test_get_source():
    def test_func(a: int, b: int) -> int:
        """Test function for testing get_source function."""
        return a + b

    import unittest
    from io import StringIO


# Generated at 2022-06-22 12:44:26.916328
# Unit test for function eager
def test_eager():
    from .. import funcy
    @eager
    def get_list():
        yield 1
        yield 2
        yield 3

    assert get_list() == [1, 2, 3]
    assert funcy.first(get_list()) == 1

# Generated at 2022-06-22 12:44:32.041514
# Unit test for function get_source
def test_get_source():
    settings.debug = False
    global warn
    warn_mock = Mock()
    sys.modules['__main__'].warn = warn_mock

    @debug
    def get_message():
        return 'kek'
    get_message()
    warn_mock.assert_not_called()

    settings.debug = True
    get_message()
    warn_mock.assert_called_once()

# Generated at 2022-06-22 12:44:35.820012
# Unit test for function eager
def test_eager():
    def it():
        yield 1
        yield 2
        yield 3

    assert eager(it)() == [1, 2, 3]

# Generated at 2022-06-22 12:44:39.606629
# Unit test for function eager
def test_eager():
    from itertools import count

    @eager
    def infinite_range(start: int) -> Iterable[int]:
        yield from count(start)

    assert infinite_range(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generated at 2022-06-22 12:46:35.241454
# Unit test for function get_source
def test_get_source():
    def f():
        return 1
    assert get_source(f) == 'return 1'
    def g():
        print('Hello world')
        return 1
    assert get_source(g) == 'print(\'Hello world\')\nreturn 1'

# Generated at 2022-06-22 12:46:38.846633
# Unit test for function eager
def test_eager():
    @eager
    def test():
        yield 2
        return 2
    assert test() == [2]


if __name__ == '__main__':
    test_eager()

# Generated at 2022-06-22 12:46:41.186360
# Unit test for function get_source
def test_get_source():
    def func():
        pass
    assert get_source(func) == 'def func():\n    pass\n'



# Generated at 2022-06-22 12:46:43.312160
# Unit test for function get_source
def test_get_source():
    def test():
        """Test function."""

    assert get_source(test) == 'def test():\n    """Test function."""\n'

# Generated at 2022-06-22 12:46:45.972232
# Unit test for function eager
def test_eager():
    @eager
    def fn():
        x = 0
        while x < 3:
            yield x
            x += 1

    assert fn() == [0, 1, 2]

# Generated at 2022-06-22 12:46:49.376138
# Unit test for function get_source
def test_get_source():
    def foo(x):
        return x + 1
    source = """def foo(x):
        return x + 1"""
    assert get_source(foo) == source,\
        "Test failed. Unexpected source code:\n{}".format(get_source(foo))


# Generated at 2022-06-22 12:46:51.890317
# Unit test for function get_source
def test_get_source():
    expected = '''def f1(x=1, *vars, **kw):
    """This is not important."""
    pass'''
    assert expected == get_source(f1)



# Generated at 2022-06-22 12:46:54.329555
# Unit test for function get_source
def test_get_source():
    def f():
        return 1 + 1

    assert get_source(f) == "return 1 + 1"


# Unit tests for function generate

# Generated at 2022-06-22 12:46:58.056595
# Unit test for function eager
def test_eager():
    # given
    def get_iterable():
        yield 1
        yield 2
        yield 3

    # when
    result = eager(get_iterable)()

    # then
    assert isinstance(result, list)
    assert result == [1, 2, 3]



# Generated at 2022-06-22 12:47:00.767456
# Unit test for function get_source
def test_get_source():

    def get_source_test():
        return 1

    assert get_source(get_source_test) == 'return 1'


if __name__ == '__main__':
    test_get_source()