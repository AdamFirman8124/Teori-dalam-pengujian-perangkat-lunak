

# Generated at 2022-06-22 12:38:22.426590
# Unit test for function debug
def test_debug():
    # -> settings.debug is False
    settings.debug = False
    warn_count = 0
    def get_warn_count():
        nonlocal warn_count
        return warn_count
    def warn(message):
        nonlocal warn_count
        warn_count += 1

    def get_message():
        return 'debug'

    debug(get_message)
    assert get_warn_count() == 0

    # -> settings.debug is True
    settings.debug = True
    warn_count = 0
    def get_warn_count():
        nonlocal warn_count
        return warn_count
    def warn(message):
        nonlocal warn_count
        warn_count += 1

    def get_message():
        return 'debug'

    debug(get_message)
    assert get_warn_count() == 1

# Generated at 2022-06-22 12:38:24.545173
# Unit test for function get_source
def test_get_source():
    def test_fn():
        pass
    assert get_source(test_fn) == 'pass'

# Generated at 2022-06-22 12:38:32.721049
# Unit test for function eager
def test_eager():
    import time
    # Generator/Iterator
    def gen(counter):
        for i in range(counter):
            time.sleep(0.001)
            yield i

    # Iterable
    class Numbers:
        def __init__(self, counter):
            self.counter = counter

        def __iter__(self):
            for i in range(self.counter):
                time.sleep(0.001)
                yield i

    # Tests
    print('Started test_eager')
    lazy_time = time.time()
    lazy = gen(100)
    lazy_time = time.time() - lazy_time
    print('Lazy-method took', lazy_time)

    eager_time = time.time()
    eager_gen = eager(gen)
    eager_results = eager_gen(100)
    eager_time

# Generated at 2022-06-22 12:38:35.584766
# Unit test for function debug
def test_debug():
    with patch('sys.stderr', new=StringIO()) as stderr:
        debug(lambda: 'foobar')
        assert stderr.getvalue() == ''
    with patch('backwards.conf.settings.debug', True):
        with patch('sys.stderr', new=StringIO()) as stderr:
            debug(lambda: 'foobar')
            assert stderr.getvalue() == '[D] foobar\n'

# Generated at 2022-06-22 12:38:36.372709
# Unit test for function get_source
def test_get_source():
    def foo():
        pass
    assert get_source(foo) == 'pass'

# Generated at 2022-06-22 12:38:42.010650
# Unit test for function eager
def test_eager():
    def print_nums(nums: List[int]) -> None:
        print(nums)

    g = [i for i in range(5)]
    print_nums(g)
    # [0, 1, 2, 3, 4]

    print_nums(eager(g))
    # [0, 1, 2, 3, 4]
    assert False


if __name__ == '__main__':
    test_eager()

# Generated at 2022-06-22 12:38:48.232454
# Unit test for function debug
def test_debug():
    from .mock import patch, mock_input
    from .stdout import get_stdout

    with patch('builtins.input', mock_input('y')):
        debug(lambda: 'hello')

    expected = '\n'.join([
        "\x1b[33mdebug\x1b[0m",
        "\x1b[33m  \x1b[0mhello",
        '',
    ])
    assert get_stdout() == expected



# Generated at 2022-06-22 12:38:58.806956
# Unit test for function debug
def test_debug():
    import io
    import sys

    # mock stdout and stderr
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

    # import debug method
    from py_backwards.utils import debug

    # test if message is printed when settings.debug is True
    settings.debug = True
    debug(lambda: 'hello')
    assert sys.stderr.getvalue() == messages.debug('hello')

    # test if nothing is printed when settings.debug is False
    settings.debug = False
    debug(lambda: 'world')
    assert sys.stderr.getvalue() == messages.debug('hello') + '\n'

    # restore stdout and stderr
    sys

# Generated at 2022-06-22 12:39:01.889150
# Unit test for function eager
def test_eager():
    @eager
    def generator():
        yield 1
        yield 2
        yield 3

    assert generator() == [1, 2, 3]

# Generated at 2022-06-22 12:39:06.443046
# Unit test for function debug
def test_debug():
    debug_buffer = []
    old_debug = settings.debug

    def my_debug(message: str) -> None:
        debug_buffer.append(message)

    settings.debug = True
    debug(lambda: 'hello')
    settings.debug = False
    debug(lambda: 'world')
    settings.debug = old_debug
    assert debug_buffer == ['hello']



# Generated at 2022-06-22 12:39:10.754197
# Unit test for function get_source
def test_get_source():
    def a():
        pass

    def b():
        pass

    assert get_source(a) == 'pass'
    assert get_source(b) == 'pass'

# Generated at 2022-06-22 12:39:12.832561
# Unit test for function get_source
def test_get_source():
    def foo(): pass
    source = get_source(foo)
    assert source == 'def foo(): pass'



# Generated at 2022-06-22 12:39:16.414446
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'a')
    debug(lambda: 'b')
    settings.debug = False
    import os
    os.remove('debug.log')



# Generated at 2022-06-22 12:39:18.619489
# Unit test for function eager
def test_eager():
    def my_func():
        yield 1
        yield 2
        yield 3

    assert eager(my_func)() == [1, 2, 3]

# Generated at 2022-06-22 12:39:21.721954
# Unit test for function get_source
def test_get_source():
    # noinspection PyUnusedLocal
    def f(a, b):
        c = a + b
        return c
    assert get_source(f) == 'c = a + b\nreturn c'

# Generated at 2022-06-22 12:39:25.174580
# Unit test for function get_source
def test_get_source():
    def test():
        def test():
            print('TEST')
        test()
    assert get_source(test) == 'def test():\n    def test():\n        print(\'TEST\')\n    test()'

# Generated at 2022-06-22 12:39:36.666178
# Unit test for function debug
def test_debug():
    import io
    import contextlib
    from . import messages
    
    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err
    
    settings.debug = True
    with captured_output() as (out, err):
        debug(lambda: "test")
    test = err.getvalue().split("\n")[0].strip()
    assert test == messages.debug("test")
    

# Generated at 2022-06-22 12:39:42.246149
# Unit test for function debug
def test_debug():
    from unittest.mock import MagicMock
    from . import messages

    mock_print = MagicMock()
    sys.stderr = mock_print
    settings.debug = True
    message = 'message'
    debug(lambda: message)

    mock_print.assert_called_with(messages.debug(message) + '\n')



# Generated at 2022-06-22 12:39:43.684204
# Unit test for function get_source
def test_get_source():
    import doctest
    doctest.testmod(verbose=False)


# Generated at 2022-06-22 12:39:50.606968
# Unit test for function debug
def test_debug():
    def get_message():
        return 'foo'
    settings.debug = True
    debug(get_message)
    assert_in(messages.debug(get_message()), sys.stderr.getvalue())
    settings.debug = False
    sys.stderr = io.StringIO()
    debug(get_message)
    assert_not_in(messages.debug(get_message()), sys.stderr.getvalue())
    sys.stderr = sys.__stderr__

# Generated at 2022-06-22 12:39:57.117236
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass

    assert get_source(test_func) == 'pass'



# Generated at 2022-06-22 12:40:06.141005
# Unit test for function debug
def test_debug():
    def test_function(do_print):
        do_print('test')

    with patch('sys.stderr', new_callable=StringIO) as stderr:
        # Should print debug message if debugging is on
        settings.debug = True
        debug(lambda: 'Writing this message to stderr')
        assert 'Writing this message to stderr' in stderr.getvalue()

        # Should not print debug message if debugging is off
        settings.debug = False
        stderr.truncate(0)
        debug(lambda: 'Writing this message to stderr')
        assert 'Writing this message to stderr' not in stderr.getvalue()

        # Should print nothing if message is empty
        stderr.truncate(0)
        debug(lambda: '')

# Generated at 2022-06-22 12:40:16.887561
# Unit test for function get_source
def test_get_source():
    def f1(a, b):
        print(a + b)

    def f2(a, b):
        print(a + b)

    def f3():
        print(a + b)

    def f4(a, b):
        print(a + b)
        print(a + b)

    print(get_source(f1) == 'a + b')
    print(get_source(f2) == 'print(a + b)')
    print(get_source(f3) == 'print(a + b)')
    print(get_source(f4) == 'print(a + b)\n    print(a + b)')


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:40:20.613831
# Unit test for function eager
def test_eager():
    @eager
    def get_range(a: int, b: int) -> Iterable[int]:
        while a < b:
            yield a
            a += 1

    assert get_range(1, 5) == [1, 2, 3, 4]

# Generated at 2022-06-22 12:40:22.596032
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f) == 'def f():\n    pass'

# Generated at 2022-06-22 12:40:30.877325
# Unit test for function debug
def test_debug():
    _test_message = ''
    _test_call_count = 0

    def test_message():
        nonlocal _test_call_count
        _test_call_count += 1
        return 'test message'

    def test_get_message():
        nonlocal _test_message
        _test_message = test_message()
        return _test_message

    debug(test_get_message)
    assert _test_call_count == 0
    assert _test_message == ''

    settings.debug = True
    debug(test_get_message)
    assert _test_call_count == 1
    assert _test_message == 'test message'



# Generated at 2022-06-22 12:40:32.909077
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    assert get_source(function) == 'def function():\n    pass'

# Generated at 2022-06-22 12:40:35.255143
# Unit test for function get_source
def test_get_source():
    def test_func():
        pass

    source = get_source(test_func)
    assert source == 'def test_func():'

# Generated at 2022-06-22 12:40:39.641649
# Unit test for function debug
def test_debug():
    test_debug.called = 0

    def get_message():
        test_debug.called += 1
        return 'sample message'

    debug(get_message)
    assert test_debug.called == 1
    settings.debug = False
    debug(get_message)
    assert test_debug.called == 1

# Generated at 2022-06-22 12:40:41.799117
# Unit test for function debug
def test_debug():
    # It is ok if nothing prints out
    debug(lambda: 'Test debug with debug{}'.format(settings.debug))



# Generated at 2022-06-22 12:40:53.256177
# Unit test for function get_source
def test_get_source():
    def my_function():
        pass

    assert get_source(my_function) == '    pass'

# Generated at 2022-06-22 12:40:56.368995
# Unit test for function debug
def test_debug():
    sys.argv.append('--debug')
    settings._init_debug()
    assert settings.debug

    debug(lambda: 'foo')
    print('--')
    settings.debug = False
    debug(lambda: 'bar')



# Generated at 2022-06-22 12:40:58.751594
# Unit test for function debug
def test_debug():
    settings.debug = True
    message = 'Message'
    debug(lambda: message) == message

assert(test_debug() == None)

# Generated at 2022-06-22 12:41:07.379209
# Unit test for function debug
def test_debug():
    import os
    import sys
    import io
    import tempfile
    sys.stderr = io.StringIO()
    debug(lambda: 'foobar')
    assert sys.stderr.getvalue() == ''
    settings.debug = True
    try:
        sys.stderr = io.StringIO()
        debug(lambda: 'foobar')
        assert sys.stderr.getvalue() == '[py_backwards: DEBUG] foobar\n'
    finally:
        settings.debug = False
        sys.stderr = sys.__stderr__



# Generated at 2022-06-22 12:41:10.702596
# Unit test for function get_source
def test_get_source():
    def some_function():
        pass

    def nested_function():
        def some_function():
            pass

    assert get_source(nested_function) == 'def some_function():\n    pass'

# Generated at 2022-06-22 12:41:13.852880
# Unit test for function get_source
def test_get_source():
    def foo():
        print('asdf')


    print(get_source(foo).split('\n'))


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:41:21.284907
# Unit test for function debug
def test_debug():
    import io
    import sys

    def some_function():
        debug(lambda: 'I will print this in debug mode')
    # Capture stderr
    _stderr = sys.stderr
    sys.stderr = io.StringIO()
    settings.debug = False
    some_function()
    assert sys.stderr.getvalue() == ''
    sys.stderr = io.StringIO()
    settings.debug = True
    some_function()
    assert sys.stderr.getvalue().strip() == messages.debug('I will print this in debug mode')



# Generated at 2022-06-22 12:41:24.808397
# Unit test for function eager
def test_eager():
    @eager
    def do_eager():
        for i in range(10):
            yield i
    assert do_eager() == list(range(10))

# Generated at 2022-06-22 12:41:30.827866
# Unit test for function get_source
def test_get_source():
    def test_function():
        return 1

    def test_function_with_comment():
        return 1 # comment

    def test_function_with_multiline_comment():
        return 1 # comment
               # comment
    assert get_source(test_function) == 'return 1'
    assert get_source(test_function_with_comment) == 'return 1'
    assert get_source(test_function_with_multiline_comment) == 'return 1'

# Generated at 2022-06-22 12:41:37.808525
# Unit test for function debug
def test_debug():
    global DEBUG
    DEBUG = ''

    def get_message():
        return 'Hello World!'

    def test():
        global DEBUG
        DEBUG = ''
        settings.debug = True
        try:
            debug(get_message)
        finally:
            settings.debug = False

    thread = threading.Thread(target=test)
    thread.start()
    thread.join()
    assert DEBUG.endswith(get_message())

# Generated at 2022-06-22 12:41:49.347912
# Unit test for function get_source
def test_get_source():
    def some_function():
        pass

    assert get_source(some_function).strip() == 'pass'

# Generated at 2022-06-22 12:41:52.941924
# Unit test for function get_source
def test_get_source():
    def add(x: int, y: int) -> int:
        print(x + y)
        print(x - y)
        return x + y

# Generated at 2022-06-22 12:41:55.170401
# Unit test for function eager
def test_eager():
    def get_numbers():
        yield 1
        yield 2
        yield 3

    assert eager(get_numbers)() == [1, 2, 3]

# Generated at 2022-06-22 12:41:56.962249
# Unit test for function get_source
def test_get_source():  # pragma: no cover
    def fn():
        pass

    assert get_source(fn) == ' pass'

# Generated at 2022-06-22 12:41:57.971176
# Unit test for function get_source

# Generated at 2022-06-22 12:42:00.081313
# Unit test for function get_source
def test_get_source():
    def f():
        pass

    assert get_source(f) == 'def f():\n    pass'

# Generated at 2022-06-22 12:42:06.906543
# Unit test for function debug
def test_debug():
    def assert_print(n, m):
        print_called = False
        def stub_print(*args, **kwargs):
            nonlocal print_called
            print_called = True
        with mock.patch('builtins.print', stub_print):
            settings.debug = n
            debug(m)
            return print_called

    assert assert_print(False, lambda: 'foo') is False
    assert assert_print(True, lambda: 'foo') is True

# Generated at 2022-06-22 12:42:11.150156
# Unit test for function debug
def test_debug():
    from io import StringIO
    buf = StringIO()
    sys.stderr = buf
    settings.debug = True
    debug(lambda: 'foo')
    settings.debug = False
    debug(lambda: 'bar')
    assert buf.getvalue() == '[DEBUG] foo\n'



# Generated at 2022-06-22 12:42:15.003879
# Unit test for function debug
def test_debug():
    """
    >>> settings.debug = True
    >>> debug(lambda: '123')
    123
    >>> settings.debug = False
    """
    pass



# Generated at 2022-06-22 12:42:17.302404
# Unit test for function get_source
def test_get_source():
    def fn():
        """Foo."""
        pass

    assert get_source(fn) == 'def fn():\n    """Foo."""\n    pass'

# Generated at 2022-06-22 12:42:42.334029
# Unit test for function get_source
def test_get_source():
    def function_with_unittest():
        return 'test_get_source'

    expected = 'return \'test_get_source\''
    source = get_source(function_with_unittest)
    assert expected == source, 'source of function "{}" must be "{}"'.format(
        function_with_unittest.__name__, expected)


if __name__ == '__main__':
    test_get_source()

# Generated at 2022-06-22 12:42:43.675085
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    assert 'function():' in get_source(function)



# Generated at 2022-06-22 12:42:49.462071
# Unit test for function get_source
def test_get_source():
    def f(a, b):
        for _ in range(0, b):
            a += 1

        return a * b

    # expected:
    #
    # '''
    # a += 1
    # '''

    expected = '''\
for _ in range(0, b):
    a += 1'''

    assert get_source(f) == expected

# Generated at 2022-06-22 12:42:52.933049
# Unit test for function eager
def test_eager():
    lst = [1, 2, 3]
    assert eager(iter)(lst) == lst
    assert eager(list)(lst) == lst
    assert eager(lambda x, y=2: (x, y))(1) == [(1, 2)]



# Generated at 2022-06-22 12:43:02.441534
# Unit test for function debug
def test_debug():
    """
    >>> settings.debug = True

    >>> class MockStream:
    ...     def __init__(self, text):
    ...         self.text = text
    ...     def write(self, data):
    ...         self.text += data
    ...     def flush(self):
    ...         pass
    >>> mock_stream = MockStream('')
    >>> with patch('sys.stderr', mock_stream):
    ...     debug(lambda: 'test')
    >>> mock_stream.text
    'b\\x1b[90mtest\\x1b[0m\\n'

    >>> settings.debug = False
    >>> debug(lambda: 'test')
    """
    pass



# Generated at 2022-06-22 12:43:06.690024
# Unit test for function debug
def test_debug():
    message = 'something'
    with mock.patch('sys.stderr') as mock_stderr:
        debug(lambda: message)
        mock_stderr.write.assert_called_with(messages.debug(message))



# Generated at 2022-06-22 12:43:08.381472
# Unit test for function get_source
def test_get_source():
    func = lambda x: x * 3
    assert get_source(func) == 'return x * 3'



# Generated at 2022-06-22 12:43:11.107959
# Unit test for function get_source
def test_get_source():
    def function():
        pass

    try:
        assert get_source(function) == 'pass'
    except Exception as e:
        raise e
    # Remove created variable
    del function

# Generated at 2022-06-22 12:43:17.451397
# Unit test for function debug
def test_debug():
    settings.debug = True
    log = []
    def get_msg():
        return 'Hello'
    old_debug = sys.stderr.write
    sys.stderr.write = log.append
    debug(get_msg)
    assert sys.stderr.write == old_debug
    assert len(log) == 1
    settings.debug = False

# Generated at 2022-06-22 12:43:27.495231
# Unit test for function debug
def test_debug():
    from .test_functions import test_debug_success, test_debug_failure

    class GetMessage:
        def __init__(self) -> None:
            self.times_called = 0

        def __call__(self) -> str:
            self.times_called += 1
            return 'debug'

    def reset_debug() -> None:
        debug(GetMessage())
        settings.debug = False

    reset_debug()
    get_message = GetMessage()
    debug(get_message)
    assert get_message.times_called == 0

    settings.debug = True
    debug(get_message)
    assert get_message.times_called == 1

    test_debug_failure(reset_debug)
    assert get_message.times_called == 1

    settings.debug = True
    test_debug_success

# Generated at 2022-06-22 12:44:20.498282
# Unit test for function get_source
def test_get_source():
    assert get_source(test_get_source) == get_source.__doc__

# Generated at 2022-06-22 12:44:23.792877
# Unit test for function eager
def test_eager():
    def x():
        for i in range(4):
            yield i

    assert eager(x)() == [0, 1, 2, 3]


# Generated at 2022-06-22 12:44:32.176450
# Unit test for function debug
def test_debug():
    # Settings for test
    settings.debug = True

    # Test debug without print
    def test_debug_without_print(function):
        get_message = lambda : 'Hello World'
        debug(get_message)  # Debug with lambda
        debug(lambda : 'Hello World')  # Debug without lambda

    test_debug_without_print(debug)

    # Test debug with print
    def test_debug_with_print(function):
        get_message = lambda : 1 + 1
        debug(get_message)  # Debug with lambda
        debug(lambda : 1 + 1)  # Debug without lambda

    test_debug_with_print(debug)


# Generated at 2022-06-22 12:44:40.553120
# Unit test for function debug
def test_debug():
    """
    >>> import builtins
    >>> old_stderr = sys.stderr
    >>> try:
    ...     from io import StringIO
    ...     sys.stderr = StringIO()
    ...     import backwards.utils
    ...     backwards.utils.settings.debug = True
    ...     def get_message():
    ...         return 'message'
    ...     debug(get_message)
    ...     assert 'message' in sys.stderr.getvalue()
    ...     backwards.utils.settings.debug = False
    ...     debug(get_message)
    ...     assert '' == sys.stderr.getvalue()
    ... finally:
    ...     sys.stderr = old_stderr
    """
    pass

# Generated at 2022-06-22 12:44:44.110234
# Unit test for function eager
def test_eager():
    @eager
    def test():
        yield 1
        yield 2
        yield 3

    assert test() == [1, 2, 3]

# Generated at 2022-06-22 12:44:48.498049
# Unit test for function eager
def test_eager():
    assert eager(lambda: [1, 2, 3])() == [1, 2, 3]
    assert eager(lambda: (n for n in [1, 2, 3]))() == [1, 2, 3], (
        'Should convert generator to list'
    )
    assert eager(lambda: None)() == [], 'Should convert None to empty list'

# Generated at 2022-06-22 12:44:54.431751
# Unit test for function get_source
def test_get_source():

    def bar(a, b, c):
        return a * b * c

    source = get_source(bar)

    assert source.startswith('return a * b * c')

    def bar(a, b, c):
        try:
            return a * b * c
        except Exception as ex:
            return ex

    source = get_source(bar)

    assert source.startswith('return a * b * c')



# Generated at 2022-06-22 12:44:56.063123
# Unit test for function get_source
def test_get_source():
    def foo():
        return 1
    assert get_source(foo) == 'return 1'

# Generated at 2022-06-22 12:45:05.714640
# Unit test for function get_source
def test_get_source():
    def f(): pass
    assert not get_source(f).endswith('\n')
    def f():
        pass
    assert not get_source(f).endswith('\n')
    def f():
        a
        pass
    assert not get_source(f).endswith('\n')

    def f():
        #comment
        a
        pass
    assert not get_source(f).endswith('\n')
    def f():
        #comment
        a
        pass
        #comment
    assert not get_source(f).endswith('\n')

    def f():
        #comment
        a
        pass
        #comment
        b
    assert not get_source(f).endswith('\n')

# Generated at 2022-06-22 12:45:07.418898
# Unit test for function get_source
def test_get_source():
    def f():
        pass
    assert get_source(f) == 'pass'


# Generated at 2022-06-22 12:47:15.509081
# Unit test for function debug
def test_debug():
    class Mock:
        message = ''

        def __call__(self):
            return self.message

    mock = Mock()
    if settings.debug:
        debug(mock)
        assert mock.message == '\033[32mdebug: \033[0m'
    else:
        mock.message = 'error'
        debug(mock)
        assert mock.message == ''


# Generated at 2022-06-22 12:47:17.745701
# Unit test for function eager
def test_eager():
    @eager
    def eager_test():
        yield 1
        yield 2

    assert len(eager_test) == 2

# Generated at 2022-06-22 12:47:19.858405
# Unit test for function get_source
def test_get_source():
    def test_function():
        """Returns 1."""
        return 1

    assert get_source(test_function) == 'return 1'

# Generated at 2022-06-22 12:47:26.654532
# Unit test for function debug
def test_debug():
    from unittest.mock import Mock, patch

    mock_print = Mock()
    settings.debug = True

    with patch('sys.stderr', mock_print):
        debug(lambda: 'test')
        assert mock_print.call_count == 1

    settings.debug = False
    with patch('sys.stderr', mock_print):
        debug(lambda: 'test')
        assert mock_print.call_count == 1



# Generated at 2022-06-22 12:47:37.477415
# Unit test for function debug
def test_debug():
    import pytest  # type: ignore
    from io import StringIO
    from contextlib import contextmanager

    @contextmanager
    def captured_stdout():
        captured = StringIO()
        with pytest.raises(SystemExit):
            with redirect_stderr(captured) as stderr:
                yield stderr

    @contextmanager
    def redirect_stderr(stream):
        old_stderr = sys.stderr
        sys.stderr = stream
        try:
            yield sys.stderr
        finally:
            sys.stderr = old_stderr

    with captured_stdout() as stdout:
        debug(lambda: 'test message')
    assert messages.debug('test message') + '\n' == stdout.getvalue()



# Generated at 2022-06-22 12:47:39.139180
# Unit test for function get_source

# Generated at 2022-06-22 12:47:43.727476
# Unit test for function get_source
def test_get_source():
    # TODO: rewrite this test
    def test_func():
        x = 0
        y = 1
        z = 2

    assert get_source(test_func) == 'x = 0\ny = 1\nz = 2'

# Generated at 2022-06-22 12:47:45.585401
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(lambda: 'Hello debug!')
    settings.debug = False

# Generated at 2022-06-22 12:47:49.854948
# Unit test for function get_source
def test_get_source():
    def dummy_function():
        print('Hello!')

    assert get_source(dummy_function) == 'print(\'Hello!\')'



# Generated at 2022-06-22 12:47:54.546167
# Unit test for function get_source
def test_get_source():
    def fn():
        """Function for testing purposes.

        Its source should be extracted."""
        a = 1
        b = 2
        return a + b

    assert get_source(fn) == "def fn():\n    \"\"\"Function for testing purposes.\n\n    Its source should be extracted.\"\"\"\n    a = 1\n    b = 2\n    return a + b"