

# Generated at 2022-06-12 19:46:57.805767
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import python_ta
    import sys
    import time
    # Update PYTHONPATH to ensure pysnooper is found
    def _set_pythonpath_for_testing():
        pysnooper_path = os.path.dirname(os.path.realpath(__file__))
        pysnooper_path = '/'.join(pysnooper_path.split('/')[:-2])
        sys.path.append(pysnooper_path)
    _set_pythonpath_for_testing()
    import pysnooper

    @pysnooper.snoop()
    def a_function():
        time.sleep(1)
        return 'test'
    assert a_function() == 'test'
test_Tracer___exit__()

# Generated at 2022-06-12 19:47:03.530233
# Unit test for function get_local_reprs
def test_get_local_reprs():
    from .variables import Exploding
    result = get_local_reprs(inspect.currentframe())
    assert result['result'] == '{}'
    result = get_local_reprs(inspect.currentframe(),
                             watch=[Exploding()])
    assert result['result'] == '{}'
test_get_local_reprs()



# Generated at 2022-06-12 19:47:14.502640
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f(x, y):
        z = x + 2
        for a in range(x, y + 2):
            b = f(a, x)
            assert b == a + x
            del b
        return z

    frame = utils.get_caller_frame()
    locals = get_local_reprs(frame)
    assert locals['x'] == '1'
    assert locals['y'] == '2'
    assert locals['z'] == '3'
    assert isinstance(locals['a'], str)
    assert locals['a'].startswith('range(')
    assert locals['b'] == '3'

    watch = (CommonVariable('z'),)
    locals = get_local_reprs(frame, watch)
    assert locals['z'] == '3'


# Generated at 2022-06-12 19:47:21.162297
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect

    def get_frame(depth=-2): # We want to call inspect.currentframe() twice
        return inspect.currentframe()

    def get_frame_entry_point(_):
        file_name, source = get_path_and_source_from_frame(get_frame())
        assert file_name == inspect.getsourcefile(get_frame)
        assert inspect.getsource(get_frame).splitlines() == source

    [get_frame_entry_point(_) for _ in range(3)]



# Generated at 2022-06-12 19:47:28.309261
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from unittest import TestCase, mock
    from unittest.mock import MagicMock

    # Mock the visibility of the protected method _is_internal_frame
    class _MagicMock(MagicMock):
        def __getattr__(self, name):
            return MagicMock()

    mocked_is_internal_frame = _MagicMock(return_value=False)
    with mock.patch.object(Tracer, '_is_internal_frame', mocked_is_internal_frame):
        # Mock the visibility of the protected method write
        mocked_write = MagicMock()
        with mock.patch.object(Tracer, 'write', mocked_write):
            # Mock the target codes
            mocked_target_codes = MagicMock()

# Generated at 2022-06-12 19:47:30.639350
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # TODO: Test whether returns the same callable (by memory address)
    # when it's not disabled.
    # TODO: Test whether returns the same callable when it's disabled,
    # and not returning by memory address.
    pass



# Generated at 2022-06-12 19:47:31.367235
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass


# Generated at 2022-06-12 19:47:34.875561
# Unit test for function get_write_function
def test_get_write_function():
    assert get_write_function(None, None)
    assert get_write_function('/tmp/file', None)
    assert get_write_function(sys.stdout, None)
    assert get_write_function(open('/tmp/file', 'w'), None)



# Generated at 2022-06-12 19:47:42.579703
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def divide(x, y):
        return x // y

    source = inspect.getsourcelines(divide)
    frame = sys._getframe()
    while frame.f_code is not divide.__code__:
        frame = frame.f_back

    result = get_path_and_source_from_frame(frame)
    assert result == source

    def divide2(x, y):
        return x // y

    result = get_path_and_source_from_frame(frame)
    assert result == source



# Generated at 2022-06-12 19:47:50.880973
# Unit test for method trace of class Tracer
def test_Tracer_trace():
   assert debug.Tracer(__builtins__.print, (), '', False, False, (), 100, False, False).trace(debug.Tracer(__builtins__.print, (), '', False, False, (), 100, False, False)._wrap_function(test_Tracer_trace).__wrapped__.__code__, 'call', None) != debug.Tracer(__builtins__.print, (), '', False, False, (), 100, False, False).trace(debug.Tracer(__builtins__.print, (), '', False, False, (), 100, False, False)._wrap_function(test_Tracer_trace).__wrapped__.__code__, 'call', None)


# Generated at 2022-06-12 19:48:23.378065
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    with utils.temp_path() as temp_path:
        # test write
        fw = FileWriter(temp_path, True)
        fw.write('hello')
        assert open(temp_path, 'rb').read() == b'hello'
        # test append
        fw.write('world')
        assert open(temp_path, 'rb').read() == b'helloworld'



# Generated at 2022-06-12 19:48:36.463004
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from io import StringIO
    from .dicts import Dict
    from .var import Var
    from .var import Signal
    from .var import Timer
    from .var import Counter
    with StringIO() as f:
        def fact(n):
            if n == 0:
                return 1
            else:
                return n * fact(n - 1)
        with Tracer(output=f, depth=2, watch=(dict(Dict), 'n'), watch_explode=(Var, Signal, Timer, Counter)):
            fact(5)
        f.seek(0)
        lines = f.readlines()

# Generated at 2022-06-12 19:48:46.890420
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import datetime
    import pysnooper
    event = Object()
    event.a = 1
    frame = sys._getframe()
    arg = ['arg', event]
    timestamp = datetime.datetime(1,2,3,4,5,6,789)
    thread_info = "thread_info"
    sut = Tracer(event='event', arg=arg)
    sut.thread_info = True
    sut.last_source_path = "last_source_path"
    sut.thread_info_padding = 999
    result = sut.trace(frame, event, arg)
    assert result == sut.trace
    sut.thread_info_padding = 0
    result = sut.trace(frame, event, arg)
    assert result == sut.trace
   

# Generated at 2022-06-12 19:48:50.436323
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    t = Tracer()
    def foo():
        x = 6
        y = 8
        z = 9
        print(x+y*z)
    old_trace = sys.gettrace()
    sys.settrace(t.trace)
    foo()
    sys.settrace(old_trace)


# Generated at 2022-06-12 19:48:55.325667
# Unit test for constructor of class Tracer
def test_Tracer():
    def f():
        return 1
    t = Tracer(watch=('foo', 'find'))
    g = t._wrap_function(f)
    assert inspect.getsource(f) == inspect.getsource(g)
    t = Tracer(watch=('foo', 'find'), watch_explode=('bar', 'name'))
    g = t._wrap_function(f)
    assert inspect.getsource(f) == inspect.getsource(g)

# Generated at 2022-06-12 19:49:04.248263
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import unittest

    class TestTracer_trace(unittest.TestCase):
        def test_default_behavior(self):
            tracer = Tracer()

            tracer.watch = []
            tracer.frame_to_local_reprs = {}
            tracer.start_times = {}
            tracer.depth = 1
            tracer.prefix = ''
            tracer.thread_info = False
            tracer.thread_info_padding = 0
            tracer.target_codes = set()
            tracer.target_frames = set()
            tracer.thread_local = threading.local()
            tracer.custom_repr = ()
            tracer.last_source_path = None
            tracer.max_variable_length = 100
            tracer.normalize = False
            tracer.relative_

# Generated at 2022-06-12 19:49:09.138763
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    foo = Tracer()
    def func():
        pass
    assert isinstance(foo(func), types.FunctionType)
    assert hasattr(foo(func), '_pysnooper_wrapped')
    assert not inspect.isgeneratorfunction(foo(func))
    assert not inspect.iscoroutinefunction(foo(func))
    assert not inspect.isasyncgenfunction(foo(func))

# Generated at 2022-06-12 19:49:16.644568
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import traceback
    import pysnooper
    snoop = pysnooper.snoop
    class A(object):
        @snoop()
        def f(self, *args, **kwargs):
            return 12
    def g():
        A().f(3)
    def h():
        A().f(3)
    def main():
        try:
            g()
        except:
            traceback.print_exc()
    try:
        main()
    except:
        traceback.print_exc()


# Generated at 2022-06-12 19:49:23.271243
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    def __exit__(self, exc_type, exc_value, exc_traceback):
        indent = ' ' * 4 * (thread_global.depth + 1)
        self.write(
            '{indent}Elapsed time: {elapsed_time_string}'.format(**locals())
        )# test start
    # test end

# Generated at 2022-06-12 19:49:25.148801
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import datetime
    assert get_path_and_source_from_frame(sys._getframe(0))[0].endswith(
                                             'test_python_toolbox.py')
    assert get_path_and_source_from_frame(
                                   datetime.datetime.now._getframe(0))[0] \
                          .endswith('datetime.py')



# Generated at 2022-06-12 19:49:43.099339
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pysnooper.snoop
    import functools
    from functools import wraps
    import inspect
    import pysnooper.utils
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable
    import pysnooper.variable

# Generated at 2022-06-12 19:49:54.141108
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f(x, y):
        def g(z):
            return z + y
        return g(x)
    x = 5
    y = CommonVariable('y', lambda frame: frame.f_locals['y']) # noqa
    f_code = f.func_code
    frame = sys._getframe()
    while frame.f_code != f_code:
        frame = frame.f_back
    assert frame.f_locals['x'] == x
    assert frame.f_locals['y'] == y
    assert get_local_reprs(frame) == {'x': '5', 'y': 'CommonVariable: y'}

# Generated at 2022-06-12 19:50:05.871152
# Unit test for function get_write_function
def test_get_write_function():
    # Test base case: None
    assert sys.stderr
    def write(s):
        stderr = sys.stderr
        try:
            stderr.write(s)
        except UnicodeEncodeError:
            stderr.write(utils.shitcode(s))
    assert get_write_function(None, False) is write

    # Test path
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test.txt')
        original_write = get_write_function(file_path, False)
        assert isinstance(original_write, FileWriter)
        assert get_write_function(file_path, True) is original_write

        # Test callable
        def write(s):
            pass
        assert get_write_

# Generated at 2022-06-12 19:50:08.640716
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    assert pycompat.callable(Tracer(utils.DummyFile(), ()).__call__) == True

# Generated at 2022-06-12 19:50:14.340034
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def get_source_lines_from_frame(frame):
        return get_path_and_source_from_frame(frame)[1]
    def assert_source_lines(expected_lines, frame):
        '''
        Assert that the frame's source code is as expected.

        If the source code is not available, assert that the frame's parent's
        source code is as expected.
        '''
        actual_lines = get_source_lines_from_frame(frame)
        if actual_lines != expected_lines:
            # Try parent frame
            if frame.f_back:
                return assert_source_lines(expected_lines, frame.f_back)
            raise AssertionError('Expected source not found:\n' +
                                 ''.join(expected_lines))

# Generated at 2022-06-12 19:50:16.920111
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():

    import re
    import pytest

    def test_write():
        pass

    tracer0 = Tracer(output=test_write)
    scope0 = {'datetime': datetime_module}

# Generated at 2022-06-12 19:50:18.608881
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # No need to test this. It's too complicated. We'll just
    # inspect it.
    pass

# Generated at 2022-06-12 19:50:23.801534
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import sys
    import threading
    
    depth = -1
    _stack = []
    start_times = {}
    target_codes = set()
    target_frames = set()
    frame_to_local_reprs = {}
    start_times = {}
    _trace = None
    function_or_class = "function_or_class"
    attr_name = "attr_name"
    attr = "attr"
    exc_type = "exc_type"
    exc_value = "exc_value"
    exc_traceback = "exc_traceback"
    frame = "frame"
    _frame_candidate = "frame_candidate"
    thread_info = "thread_info"
    current_thread = "current_thread"
    function = "function"

# Generated at 2022-06-12 19:50:30.291034
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f():
        return [i for i in range(3)]
    frame = inspect.currentframe()
    frame = frame.f_back
    try:
        assert get_path_and_source_from_frame(frame) == \
               (__file__, inspect.getsourcelines(f)[0])
        print('Success!')
    finally:
        del frame



# Generated at 2022-06-12 19:50:39.326930
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Test for internal frame
    assert Tracer()._is_internal_frame(inspect.currentframe().f_back)
    # Test for external frame
    assert not Tracer()._is_internal_frame(inspect.currentframe())

    # Test for call event
    a = 1 # Writing variable
    def func():
        b = 2
        a = 3 # Writing variable
        return a
    tracer = Tracer()
    tracer.target_codes.add(func.__code__)
    tracer.trace(
        inspect.currentframe().f_back,
        event = 'call',
        arg = None
    )
    tracer.trace(
        inspect.currentframe().f_back,
        event = 'return',
        arg = None
    )
    # Test for return value
    assert tracer.frame_

# Generated at 2022-06-12 19:50:55.949373
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    logging.info("Testing method __call__ of class Tracer...")
    global DISABLED
    DISABLED = False
    @pysnooper.snoop()
    def add(a, b):
        return a + b
    assert add(1, 2) == 3
    

# Generated at 2022-06-12 19:51:04.697077
# Unit test for function get_write_function
def test_get_write_function():
    # Test for None
    assert isinstance(get_write_function(None, False), collections.Callable)
    # Test for path
    assert isinstance(get_write_function('path', False), collections.Callable)
    assert isinstance(get_write_function('path', True), collections.Callable)
    # Test for callable
    def callable_test():
        pass
    assert isinstance(get_write_function(callable_test, False), collections.Callable)
    # Test for utils.WritableStream
    class WritableStreamTest(utils.WritableStream):
        def write(self, val):
            pass
        def flush(self):
            pass
    assert isinstance(get_write_function(WritableStreamTest(), False), collections.Callable)



# Generated at 2022-06-12 19:51:09.309908
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    class Mock:
        def __enter__(self):
            return None

    with pytest.raises(NotImplementedError) as excinfo:
        Mock().__exit__(None, None, None)

    assert "normalize is not supported with thread_info" in str(excinfo.value)


# Generated at 2022-06-12 19:51:10.301583
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    with Tracer():
        ...


# Generated at 2022-06-12 19:51:16.521758
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        _path = f.name
        with open(_path, 'w', encoding='utf-8') as output_file:
            output_file.write('*')
        writer = FileWriter(_path, overwrite=True)
        writer.write('!')
        with open(_path, 'r', encoding='utf-8') as output_file:
            assert output_file.read() == '!'
        writer.write('?')
        with open(_path, 'r', encoding='utf-8') as output_file:
            assert output_file.read() == '!?'




# Generated at 2022-06-12 19:51:21.171024
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import nose
    import nose.tools
    import inspect
    import types

    def f_for_testing(x, y):
        x = x + y
        return x

    frame = inspect.currentframe().f_back
    assert frame.f_code == f_for_testing.func_code
    path, source = get_path_and_source_from_frame(frame)
    nose.tools.assert_equal(source[0], 'def f_for_testing(x, y):')



# Generated at 2022-06-12 19:51:26.434082
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    tracer = Tracer()
    def foo():
        pass
    foo1 = tracer(foo)
    def bar():
        pass
    bar1 = tracer(bar)
    class Test():
        def bar():
            pass
    test = Test()
    assert test.bar == bar1


# Generated at 2022-06-12 19:51:29.160232
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f():
        x = 5
        return get_local_reprs(inspect.currentframe())

    assert f() == {
        'x': '5',
    }

# Generated at 2022-06-12 19:51:38.920911
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import io
    import re
    import pysnooper
    import textwrap

    code = textwrap.dedent('''
    def foo(bar, baz=None):
        if bar:
            return bar
        else:
            return baz
    def longest_line(a, b, c=3):
        while a > b:
            if a > c:
                print(c)
            else:
                break
        return a
    ''')

    # compile the code
    code = compile(code, '<string>', 'exec')
    # write the code
    local_namespace = {}
    global_namespace = {}

# Generated at 2022-06-12 19:51:49.942531
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    from testfixtures import compare, ShouldRaise, Replacer
    from unittest import TestCase

    tracer = Tracer()
    compare(tracer._write, get_write_function.return_value)
    compare(tracer.watch, [])
    compare(tracer.frame_to_local_reprs, {})
    compare(tracer.start_times, {})
    compare(tracer.depth, 1)
    compare(tracer.prefix, '')
    compare(tracer.thread_info, False)
    compare(tracer.thread_info_padding, 0)
    compare(tracer.target_codes, set())
    compare(tracer.target_frames, set())
    compare(tracer.last_source_path, None)
    compare(tracer.max_variable_length, 100)

# Generated at 2022-06-12 19:52:30.035306
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    instr = '''def f(a, b):
        c = a + b
        return c
    '''
    frame = _fake_frame(instr, 'f')
    frame.f_back = _fake_frame(instr, 'f')
    tracer = Tracer(watch=['a', 'b'])
    tracer.trace(frame, 'call', None)
    tracer.trace(frame, 'line', None)
    tracer.trace(frame, 'return', 123)
    # print(tracer.frame_to_local_reprs)


# Generated at 2022-06-12 19:52:37.004064
# Unit test for function get_write_function
def test_get_write_function():
    def test_function(s):
        return s

    file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    # overwrite is set to True
    write_function = get_write_function(file.name, True)
    write_function('a')
    write_function('b')
    file.close()

    with open(file.name) as f:
        assert f.read() == 'b'

    os.remove(file.name)

    # overwrite is set to False
    write_function = get_write_function(file.name, False)
    write_function('a')
    write_function('b')
    file.close()

    with open(file.name) as f:
        assert f.read() == 'ab'

    os.remove(file.name)

    # output

# Generated at 2022-06-12 19:52:45.338430
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    frame = inspect.currentframe()
    frame_to_check = frame.f_back.f_back
    path, source = get_path_and_source_from_frame(frame_to_check)
    assert path == __file__
    assert frame_to_check.f_lineno - 1 < len(source)
    assert frame_to_check.f_lineno - 1 >= 0
    assert source[frame_to_check.f_lineno - 1] == 'def test_get_path_and_source_from_frame():'
test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:52:50.352374
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import sys
    import _thread
    import functools
    import inspect
    import threading

    from . import utils

    from . import pycompat
    from .utils import Traceback

    class FakeFrame(object):

        def __init__(self, code):
            self.f_code = code

    # The following is a test for method __exit__ of class Tracer

    with pycompat.mock.patch('logging.debug') as fake_logging_debug:
        DISABLED = True
        tracer = Tracer()
        tracer.__exit__(TypeError, TypeError(), None)
        DISABLED = False

    exc_info = sys.exc_info()
    frame = FakeFrame(Tracer.__exit__.__code__)


# Generated at 2022-06-12 19:52:51.957238
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    test_module_name = 'test_script'

# Generated at 2022-06-12 19:52:57.110814
# Unit test for constructor of class Tracer
def test_Tracer():
    output = io.StringIO()
    s = pysnooper.Snooper(watch=['x'], output=output)
    with s:
        a = {'d': 1}
        b = a
        c = a
        x = 1
        x = x + 1
        del x
        print('x', 'is now', x)
    captured = output.getvalue()
    expected = '''\
Starting var:.. x = 1
    New var:....... x = 2
    Modified var:.. x = 2
    Call ended by exception
'''
    assert captured == expected

# Generated at 2022-06-12 19:53:00.417540
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        pass
    path, source = get_path_and_source_from_frame(foo.__code__.co_firstlineno)
    assert path.endswith('test_navigator.py')



# Generated at 2022-06-12 19:53:03.392366
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer(output='capture')
    with tracer:
        pass
    assert tracer._write.output == (
        'Elapsed time: 0:00:00.000000\n'
    )


# Generated at 2022-06-12 19:53:08.973204
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def func(): return 1
    frame = sys._getframe()
    while frame.f_code.co_name != 'test_get_path_and_source_from_frame':
        frame = frame.f_back
    frame = frame.f_back.f_back
    assert get_path_and_source_from_frame(frame) == \
                             ('test_variables.py', UnavailableSource())
    assert func.__code__ == frame.f_code


# Generated at 2022-06-12 19:53:17.244446
# Unit test for constructor of class Tracer
def test_Tracer():

    with pytest.raises(AssertionError):
        Tracer(output=True, watch=([1], dict(a=2)),
               watch_explode=([1], dict(a=2)), depth=1, prefix='',
               overwrite=False, thread_info=False, custom_repr=(),
               max_variable_length=100, normalize=False, relative_time=False)
    with pytest.raises(AssertionError):
        Tracer(output=True, watch=('foo', dict(a=2)),
               watch_explode=([1], dict(a=2)), depth=1, prefix='',
               overwrite=False, thread_info=False, custom_repr=(),
               max_variable_length=100, normalize=False, relative_time=False)

# Generated at 2022-06-12 19:54:21.284431
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f(): pass
    frame = f.__code__.co_filename, f.__code__.co_firstlineno

    assert get_path_and_source_from_frame(frame)



# Generated at 2022-06-12 19:54:31.433672
# Unit test for function get_local_reprs
def test_get_local_reprs():
    assert get_local_reprs({'a': 123, 'b': 456}, watch=[]) == {'a': 123, 'b': 456}
    assert get_local_reprs({'a': 123, 'b': 456}, watch=[CommonVariable('c', 789)]) == {'a': 123, 'b': 456, 'c': 789}
    assert get_local_reprs({'a': 123, 'b': 456}, watch=[CommonVariable('a', 789)]) == {'a': 789, 'b': 456}
    assert get_local_reprs({'a': 123, 'b': 456}, watch=[CommonVariable('b', 789)]) == {'a': 123, 'b': 789}

# Generated at 2022-06-12 19:54:41.760978
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer()
    assert repr(tracer) == '<Tracer at 0x7f05b3ef3ac8>'
    tracer._write = lambda x: x
    tracer.prefix = '<PREFIX>'
    assert tracer.write('<TEST STRING>') == '<PREFIX><TEST STRING>'
    assert tracer.write('<TEST> <STRING>') == '<PREFIX><TEST> <STRING>'
    tracer.write('custom write function') == 'custom write function'
    assert tracer._write('custom write function') == '<PREFIX>custom write function'
    assert tracer._is_internal_frame(None) == False
    assert tracer._is_internal_frame(inspect.currentframe()) == True
    assert tr

# Generated at 2022-06-12 19:54:48.268844
# Unit test for function get_local_reprs
def test_get_local_reprs():
    frame = inspect.currentframe()
    assert get_local_reprs(frame, normalize=True) == {'frame': '?',
                                                     'result': '{}',
                                                     'variable': '?',
                                                     '__name__': "'__main__'",
                                                     '__package__': 'None',
                                                     '__doc__': 'None',
                                                     '__builtins__': '?',
                                                     '__file__': "r'?.*'",
                                                     '__cached__': '?',
                                                     '__loader__': '?',
                                                     'variable_name':
                                                     "'?'",
                                                     'variable_repr': '?',
                                                     '__spec__': 'None'}


# Generated at 2022-06-12 19:54:58.892831
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():

    try:
        # Executing this will create a frame
        exec('def my_function(a, b):\n    return a + b\n')
        loaded_frame = sys._getframe()
        while loaded_frame:
            loaded_frame.f_globals['__loader__'] = None
            if loaded_frame.f_code.co_name == 'my_function':
                break
            loaded_frame = loaded_frame.f_back

        file_name, source = get_path_and_source_from_frame(loaded_frame)
        assert source == ['def my_function(a, b):', '    return a + b']
        assert file_name.endswith('<string>')
    finally:
        del sys.modules[__name__]



# Generated at 2022-06-12 19:55:01.317252
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import doctest


# Generated at 2022-06-12 19:55:03.260224
# Unit test for constructor of class Tracer
def test_Tracer(): # TODO: Move to a unit test file
    Tracer()


# Generated at 2022-06-12 19:55:12.566776
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    global DISABLED
    DISABLED = False
    thread_global.__dict__.setdefault('depth', -1)
    calling_frame = inspect.currentframe().f_back
    if not self._is_internal_frame(calling_frame):
        calling_frame.f_trace = self.trace
        self.target_frames.add(calling_frame)

    stack = self.thread_local.__dict__.setdefault(
        'original_trace_functions', []
    )
    stack.append(sys.gettrace())
    self.start_times[calling_frame] = datetime_module.datetime.now()
    sys.settrace(self.trace)

    assert sys.gettrace() == self.trace

    calling_frame = inspect.currentframe().f_back
    self.target_frames.discard

# Generated at 2022-06-12 19:55:15.046296
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    t = Tracer()
    for i in range(10):
        s = 'some string'
        t.trace(None, None, None)



# Generated at 2022-06-12 19:55:18.431748
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    test_file_path = os.path.join(os.path.split(__file__)[0], 'test.py')
    def f():
        g()
    def g():
        frame = inspect.currentframe().f_back
        path, lines = get_path_and_source_from_frame(frame)
        return path, lines
    assert f() == (test_file_path, open(test_file_path).read().splitlines())

