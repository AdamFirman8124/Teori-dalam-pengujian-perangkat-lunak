

# Generated at 2022-06-12 19:46:57.835921
# Unit test for function get_write_function
def test_get_write_function():
    # Test outputting to stdout
    stdout = sys.stdout
    with utils.Sys.stdout_swap(utils.StringIO()) as stream:
        write = get_write_function(None, False)
        write('this is stdout.')
        assert stream.getvalue() == 'this is stdout.'
    # Test outputting to stderr
    stderr = sys.stderr
    with utils.Sys.stderr_swap(utils.StringIO()) as stream:
        write = get_write_function(None, False)
        write('this is stderr.')
        assert stream.getvalue() == 'this is stderr.'
    # Test outputting to a file in overwrite mode

# Generated at 2022-06-12 19:47:06.025849
# Unit test for constructor of class Tracer
def test_Tracer():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w') as f:
        with Tracer(f.name, watch=('foo', 'bar'), watch_explode=('baz', 'quux'),
                    depth=2, prefix='ZZZ ', overwrite=False, thread_info=True,
                    custom_repr=((type1, custom_repr_func1),
                                 (condition2, custom_repr_func2), ...),
                    max_variable_length=100, normalize=False, relative_time=False):
            ...


# Generated at 2022-06-12 19:47:11.795566
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global DISABLED  # pylint: disable=global-statement
    DISABLED = False
    class TestClass:
        def __init__(self, foo):
            self.foo = foo
        @pysnooper.snoop(watch_explode=('foo', 'self'))
        def bar(self):
            return self.foo
    instance = TestClass('bar')
    assert instance.bar() == 'bar'


# Generated at 2022-06-12 19:47:17.028480
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from . import test_source

    def f():
        return get_path_and_source_from_frame(inspect.currentframe())
    assert f()[0] == os.path.abspath(test_source.__file__)


# `.` is line continuation on Python 3

# Generated at 2022-06-12 19:47:25.734253
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class DummyTracer(Tracer):
        source_path = None
        source = None

        def __init__(self):
            super().__init__()
            self.write = lambda s: None

        def setUp(self):
            self.source_path = inspect.getsourcefile(self.trace)
            with open(self.source_path) as f:
                self.source = f.readlines()

        def test_Tracer_trace_event_call(self):
            self.setUp()
            frame = inspect.currentframe()
            result = self.trace(frame, 'call', None)
            assert result == self.trace

        def test_Tracer_trace_event_return(self):
            self.setUp()
            frame = inspect.currentframe()

# Generated at 2022-06-12 19:47:26.674583
# Unit test for function get_local_reprs
def test_get_local_reprs():
    assert get_local_reprs(frame=None) == {}

# Generated at 2022-06-12 19:47:29.499581
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    frame = inspect.currentframe()
    path, source = get_path_and_source_from_frame(frame)
    assert getattr(source, '__iter__', None) is not None
    assert path == __file__



# Generated at 2022-06-12 19:47:35.386033
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Instantiate mock objects
    trace_ = mock.Mock(wraps=Tracer.trace)
    frame = mock.Mock()
    event = mock.Mock()
    arg = mock.Mock()
    # Call method
    result = trace_(frame, event, arg)
    # Check asserts
    assert result == trace_.return_value
    # Check calls
    assert trace_.mock_calls == [mock.call(frame, event, arg)]

# Generated at 2022-06-12 19:47:39.111243
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tr = Tracer(watch=("a", "b"))
    tr.trace(inspect.currentframe(), 'call', None)
    a = "a"
    b = "b"
    tr.trace(inspect.currentframe(), 'return', None)


# Generated at 2022-06-12 19:47:45.206129
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    assert DISABLED == 0
    output = sys.stdout
    overwrite = 0
    watch = ()
    watch_explode = ()
    depth = 1
    prefix = ''
    custom_repr = ()
    thread_info = False
    max_variable_length = 100
    normalize = False
    relative_time = False
    tracer = Tracer(output=output, watch=watch, watch_explode=watch_explode,
                    depth=depth, prefix=prefix, overwrite=overwrite,
                    thread_info=thread_info, custom_repr=custom_repr,
                    max_variable_length=max_variable_length,
                    normalize=normalize, relative_time=relative_time)
    if not (not DISABLED):
        return

# Generated at 2022-06-12 19:48:14.152221
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    frame = inspect.currentframe()
    assert get_path_and_source_from_frame(frame) == (__file__,
                                                     inspect.getsourcelines(test_get_path_and_source_from_frame)[0])



# Generated at 2022-06-12 19:48:18.362562
# Unit test for constructor of class Tracer
def test_Tracer():
    c = Tracer(watch='foo', watch_explode='bar')
    assert len(c.watch) == 2
    assert isinstance(c.watch[0], CommonVariable)
    assert isinstance(c.watch[1], Exploding)
    assert c.watch[0].var_name == 'foo'
    assert c.watch[1].var_name == 'bar'
    assert c.depth == 1
    assert c.prefix == ''
    assert c.max_variable_length == 100
    assert c.normalize == False
    assert c.relative_time == False


# Generated at 2022-06-12 19:48:23.991085
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    path ='test.txt'
    f = FileWriter(path, True)
    f.write('this is test')
    f = FileWriter(path, False)
    f.write(' this is append')
    with open(path, 'r') as input_file:
        s = input_file.read()
    assert s == 'this is test this is append'
    os.remove(path)


# Generated at 2022-06-12 19:48:37.270422
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import pysnooper
    from pysnooper.utils import get_local_reprs, CommonVariable, \
        Exploding, BaseVariable, get_shortish_repr
    tracer = pysnooper.Tracer()
    tracer.depth = 1
    tracer.write = print
    tracer.watch = [CommonVariable('a'), Exploding('b')]
    tracer.custom_repr = [
        (lambda x: True, lambda x: x + 1)
    ]
    tracer.max_variable_length = 100
    tracer.normalize = True
    tracer.relative_time = True
    tracer.thread_info = True
    f_locals = {'a': 2, 'b': 3}
    tracer.frame_to_local_reprs = {}

# Generated at 2022-06-12 19:48:47.627212
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    c = True
    i = True
    while True:
        if c:
            c = False
        else:
            break
        if i:
            i = False
        else:
            break
    it = iter([1, 2, 3])
    try:
        next(it)
        next(it)
        next(it)
        next(it)
    except StopIteration:
        pass
    for i in [1, 2, 3]:
        pass
    for i in [1, 2, 3]:
        if i % 2 == 0:
            break
    for i in [1, 2, 3]:
        if i % 2 == 0:
            continue
    l = Tracer()

# Generated at 2022-06-12 19:48:55.615430
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import sys
    import pycompat
    import pysnooper
    import os
    import collections
    import six
    import pysnooper
    import pytest
    import inspect
    import pycompat
    import six
    import datetime
    import time
    import functools
    import threading
    import utils
    import opcode
    import traceback
    import pycompat
    import threading
    import inspect
    import itertools
    import datetime
    import threading
    import pysnooper
    import pycompat
    import functools
    import six
    import os
    import time
    import time
    import sys
    from pysnooper.utils import get_write_function
    from pysnooper.variables import Exploding, BaseVariable, CommonVariable

# Generated at 2022-06-12 19:49:04.544381
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import os
    import sys
    import pycompat
    import pycompat.collections_abc
    import pycompat.functools_wraps
    import pycompat.inspect_isfunction
    import pycompat.inspect_isgeneratorfunction
    import pycompat.inspect_iscoroutinefunction
    import pycompat.inspect_getfullargspec
    import pycompat.inspect_getfile
    import pycompat.isasyncgenfunction
    import pycompat.iscoroutinefunction
    import datetime
    import inspect
    import functools
    import threading
    import types
    import libfuturize.fixes.fix_getcwdfix_getcwdu
    Tracer_instance_0 = Tracer()

# Generated at 2022-06-12 19:49:08.654599
# Unit test for function get_local_reprs
def test_get_local_reprs():
    frame = inspect.currentframe()
    local_reprs = get_local_reprs(frame, normalize=False)
    assert local_reprs['frame'] == '<frame object at %s>' % id(frame)
del test_get_local_reprs



# Generated at 2022-06-12 19:49:20.694787
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from sys import version_info
    from pytest import raises
    from collections import UserDict
    from . import snoop
    from .pysnooper import Tracer, DISABLED
    from .pysnooper import pysnooper_epilogue as pysnooper_epilogue
    from .pysnooper import pysnooper_prologue as pysnooper_prologue
    from .pysnooper import pysnooper_pre_write as pysnooper_pre_write
    from .pysnooper import pysnooper_post_write as pysnooper_post_write

    # Setup
    @snoop()
    def foo():
        return
    def bar():
        return
    def baz():
        yield

    # Exercise
    foo_wrapper = foo
    bar_

# Generated at 2022-06-12 19:49:24.592449
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    t = Tracer()
    t.write = mock.MagicMock()
    test_frame = inspect._empty
    t.trace(test_frame, 'call', None)
    assert t.write.called


# Generated at 2022-06-12 19:49:55.930022
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f():
        l = []
        l.append(())
        l.append([])
        l.append({})
    f.__code_object__

    frame = f.__code_object__.create_frame(None)

    assert get_local_reprs(frame, normalize=True) == {}

    frame.f_locals['l'] = [1, 2, 3]
    assert get_local_reprs(frame, normalize=True) == {'l': '[1, 2, 3]'}

    frame.f_locals['l'] = [1, 2, 3]
    assert get_local_reprs(frame, watch=(CommonVariable('l'),),
                           normalize=True) == {'l': '[1, 2, 3]'}

    frame.f_locals['l']

# Generated at 2022-06-12 19:50:06.233840
# Unit test for function get_write_function
def test_get_write_function():
    from . import utils
    import sys
    import pycompat

    output = None
    write = get_write_function(output, overwrite=False)
    # Checking write function is properly created
    assert write.__name__ == "write"
    # Checking that write function itself works properly
    with pycompat.redirect_stdout(utils.StringIO()):
        with pycompat.redirect_stderr(utils.StringIO()):
            write("hi")
            assert len(sys.stderr.getvalue()) == 2
            assert sys.stderr.getvalue()[0] == "h"
            assert sys.stderr.getvalue()[1] == "i"

    output = "test"
    write = get_write_function(output, overwrite=True)
    # Checking write function is properly created

# Generated at 2022-06-12 19:50:14.588143
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class TestTracer(Tracer):
        def __init__(self, *args, **kwargs):
            super(Tracer, self).__init__(*args, **kwargs)
            self.mock_trace = Mock()
    tracer = TestTracer(watch=['a'])
    line_no = None
    timestamp = None
    event = None
    source_line = None
    thread_info = '0-MainThread '
    local_repr = 'a = 1'
    # Assert that _wrap_function and __enter__ are called

# Generated at 2022-06-12 19:50:20.913068
# Unit test for constructor of class Tracer
def test_Tracer():

    output = StringIO()

    # test configuration options
    pysnooper.snoop(output=output.write, watch=('var',),
                    watch_explode=('var',), depth=2, prefix='prefix: ',
                    overwrite=False, thread_info=False, custom_repr=(),
                    max_variable_length=100, normalize=False,
                    relative_time=False,
                    )

    # test Tracer method __call__
    @pysnooper.snoop()
    def func(): pass
    assert func.__name__ == 'func'
    assert func.__doc__ == ''

    @pysnooper.snoop()
    def func():
        """docstring"""
        pass
    assert func.__name__ == 'func'

# Generated at 2022-06-12 19:50:27.908595
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():

    def test_wrapped_class(self):
        pass

    def test_wrapped_class_method(self):
        pass

    def test_wrapped_regular_function():
        pass

    def test_wrapped_generator_function():
        pass

    def test_wrapped_coroutine_function():
        pass

    def test_wrapped_async_generator_function():
        pass

    # test for wrapped class
    wrapped_class = Tracer()(TestClass)
    assert isinstance(wrapped_class, type)
    assert wrapped_class.__name__ == 'Tracer'
    assert callable(wrapped_class)
    assert wrapped_class.__module__ == 'pysnooper.snoop'

# Generated at 2022-06-12 19:50:29.412581
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    #TODO: implement
    assert False


# Generated at 2022-06-12 19:50:30.027777
# Unit test for method write of class FileWriter
def test_FileWriter_write(): pass



# Generated at 2022-06-12 19:50:33.329513
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from pysnooper.utils import run_in_thread
    from pysnooper import snoop
    import sys
    raise NotImplementedError()


from pysnooper.utils import run_in_thread
from pysnooper import snoop

# Generated at 2022-06-12 19:50:42.275129
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    line_no = lineno()
    global snooped_line_no, snooped_event, snooped_source_line, \
           snooped_return_value, snooped_exception
    snooped_line_no = snooped_event = snooped_source_line = ""
    snooped_return_value = snooped_exception = None

    def my_function(x):
        try:
            return 1 / x
        except ZeroDivisionError:
            return 'infinity'

    def my_function_with_function_definition_before_decorator(x):
        def my_function(x):
            try:
                return 1 / x
            except ZeroDivisionError:
                return 'infinity'
        return my_function(x)


# Generated at 2022-06-12 19:50:48.318802
# Unit test for function get_local_reprs
def test_get_local_reprs():
    import inspect
    vara = 123
    varb = 456
    frame = inspect.currentframe()
    assert get_local_reprs(frame) == {'vara': '123', 'varb': '456'}
    for i in range (1, 10):
        exec('var{} = {} * {}'.format(chr(ord('a') + i), i, i))

# Generated at 2022-06-12 19:51:49.820150
# Unit test for function get_write_function
def test_get_write_function():
    assert get_write_function(None, False)('hello') is None
    assert get_write_function(None, True)('hello') is None
    assert get_write_function(sys.stdout, False)('hello') is None
    assert get_write_function(sys.stdout, True)('hello') is None
    import io
    assert get_write_function(io.StringIO(), False)('hello') is None
    assert get_write_function(io.StringIO(), True)('hello') is None
    assert get_write_function('temp.txt', False)('hello') is None
    assert get_write_function('temp.txt', True)('hello') is None
    assert get_write_function(lambda s: None, False)('hello') is None

# Generated at 2022-06-12 19:51:51.455596
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    tracer = pysnooper.snoop()
    assert tracer.depth == 1

# Generated at 2022-06-12 19:52:01.866362
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import os
    tracer = Tracer(None)
    tracer.set_thread_info_padding('')
    frame = {'f_code': {'co_filename': 'filename'}, 'f_lineno': 1, 'f_lasti': 1, 'f_back': None}
    traceback = {'format_exception_only': lambda *arg1: ['\n'.join(['filename']), 'exception']}
    tracer.frame_to_local_reprs = {frame: {'a': 'b', 'c': 'd'}}
    tracer.start_times = {frame: datetime_module.datetime(2020, 8, 10, 20, 7, 25, 614292)}
    thread_global = {'depth': 0}
    import sys

# Generated at 2022-06-12 19:52:11.972475
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    s = 'text s'
    with pycompat.temp_file() as fp:
        path = fp.name
        wf = FileWriter(path, False)
        wf.write(s)
        with open(path, 'r', encoding='utf-8') as fp:
            assert fp.read() == s
        wf.write(s)
        wf.write(s)
        wf.write(s)
        with open(path, 'r', encoding='utf-8') as fp:
            assert fp.read() == s*4
        wf = FileWriter(path, True)
        wf.write(s)
        with open(path, 'r', encoding='utf-8') as fp:
            assert fp.read() == s



# Generated at 2022-06-12 19:52:17.835882
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def print_a():
        print('a')
    t = pysnooper.snoop()
    t.trace(print_a.__code__, 'call', 'arg')
    t.trace(print_a.__code__, 'exception', 'arg')
    t.trace(print_a.__code__, 'return', 'arg')
    t.trace(print_a.__code__, 'line', 'arg')
    

# Generated at 2022-06-12 19:52:25.154825
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def inner_test(test_string, exp_path, exp_source, encoding=None):
        import marshal, types
        code = compile(test_string, exp_path, 'exec')
        code_bytes = b'\1' + marshal.dumps(code)

# Generated at 2022-06-12 19:52:34.272065
# Unit test for function get_write_function
def test_get_write_function():
    class TestWritableStream(utils.WritableStream):
        def write(self, s):
            return s

    def test_output(s):
        return s

    def test_stderr(s):
        sys.stderr.write(s)

    assert get_write_function(None, False) == test_stderr
    assert get_write_function(None, True) == test_stderr
    assert get_write_function(test_output, False) == test_output
    assert get_write_function(test_output, True) == test_output
    assert get_write_function(TestWritableStream(), False) == TestWritableStream.write
    assert get_write_function(TestWritableStream(), True) == TestWritableStream.write

# Generated at 2022-06-12 19:52:35.786265
# Unit test for constructor of class Tracer
def test_Tracer():
    function_1()


# Generated at 2022-06-12 19:52:37.258569
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    t = Tracer()
    if t is None:
        pass


# Generated at 2022-06-12 19:52:41.228894
# Unit test for constructor of class Tracer
def test_Tracer():
    with pytest.warns(DeprecationWarning):
        with Tracer(watch=('self', 'self.foo', 'foo', 'bar', 'baz.qux')):
            pass


# Generated at 2022-06-12 19:54:07.853438
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import unittest
    import unittest.mock
    import test.test_tracer
    test_instance = test.test_tracer.Tracer()
    test_instance._write = unittest.mock.MagicMock(return_value=None)
    test_instance.frame_to_local_reprs = {}
    test_instance.target_codes = set()
    test_instance.target_frames = set()
    test_instance.thread_local = unittest.mock.MagicMock()
    test_instance.thread_local.original_trace_functions = []
    test_instance.thread_local.thread_local = unittest.mock.MagicMock()
    test_instance.thread_local.thread_local.__dict__ = {}
    test_instance.thread_local.thread

# Generated at 2022-06-12 19:54:14.454822
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # Test that this doesn't raise an exception
    try:
        import IPython
    except ImportError:
        pass
    else:
        ipython_shell = IPython.get_ipython()
        if ipython_shell:
            frame = sys._getframe(0)
            get_path_and_source_from_frame(frame)

    def f():
        return f
    frame = f().__code__.co_filename
    get_path_and_source_from_frame(frame)



# Generated at 2022-06-12 19:54:19.209689
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    fw = FileWriter(os.devnull, True)
    fw.write(u'Δ')
    fw.write(u'x')
    fw.overwrite = True
    fw.write(u'<')
    fw.overwrite = False
    fw.write(u'>')
    assert os.system('diff <(printf "Δ<x>") %s' % os.devnull) == 0


# noinspection PyUnresolvedReferences

# Generated at 2022-06-12 19:54:29.349018
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    # Tests `FileWriter.write()` in this module

    import os.path
    import shutil

    from .test_python_toolbox import TempFolder

    with TempFolder() as temp_folder:
        file_writer = FileWriter(temp_folder / 'test', overwrite=True)
        file_writer.write('abc123')
        assert os.path.isfile(temp_folder / 'test')
        with open(temp_folder / 'test') as f:
            assert f.read() == 'abc123'
        file_writer.overwrite = False
        file_writer.write('xyz')
        with open(temp_folder / 'test') as f:
            assert f.read() == 'abc123xyz'
        file_writer.overwrite = True
        file_writer.write('aaaaa')

# Generated at 2022-06-12 19:54:40.310533
# Unit test for constructor of class Tracer
def test_Tracer():
    def _tracer_test():
        """
        This function is used to test the __init__ function of Tracer
        """
        # First, we test the output
        import io
        import sys

        sys.stdout = io.StringIO()
        class TestFunc:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            @pysnooper.snoop()
            def test(self, people):
                print(f'I am {self.name} and my age is {self.age}.')
                print(f'My friends are {people}')

        a = TestFunc('Tom', 21)
        a.test(['Jerry', 'Mary'])
        print(repr(sys.stdout.getvalue()))


# Generated at 2022-06-12 19:54:41.760934
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pysnooper.snoop()


# Generated at 2022-06-12 19:54:48.319367
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from .context import pysnooper

    # Missing module
    try:
        from .context import missing_module
    except ImportError:
        pass
    else:
        raise Exception('Missing module incorrectly imported.')

    # Test passing in a function
    @pysnooper.snoop()
    def hello(name):
        return 'Hello, {}!'.format(name)

    got = hello('John')
    assert got == 'Hello, John!', got

    # Test passing in a class
    @pysnooper.snoop()
    class Hello2:

        def __init__(self, name):
            self.name = name

        def __call__(self):
            return 'Hello, {}!'.format(self.name)

    got = Hello2('John')()

# Generated at 2022-06-12 19:54:59.441956
# Unit test for function get_write_function
def test_get_write_function():
    assert get_write_function(None, False)('hello') is None
    assert get_write_function(sys.stdout, False)('hello') is None
    assert get_write_function('argh.txt', False)('hello') is None
    with open('argh.txt') as f:
        assert f.read() == 'hello'
    os.remove('argh.txt')
    with pycompat.StringIO() as s:
        assert get_write_function(s, False)('hello') is None
        assert s.getvalue() == 'hello'
    write = get_write_function(None, False)
    try:
        write('''héllò''')
    except UnicodeEncodeError:
        pass
    else:
        raise Exception("This test should not pass when running on Python 2.")

# Generated at 2022-06-12 19:55:04.625965
# Unit test for function get_local_reprs
def test_get_local_reprs():
    from .variables import SimpleVariable
    variable_1 = SimpleVariable('tomato', 'tomato.color')
    variable_2 = SimpleVariable('spinach', 'spinach.color')
    variable_3 = SimpleVariable('mango', 'mango.color')
    variable_4 = SimpleVariable('hi', 'the_string')
    q = 'the_string'



# Generated at 2022-06-12 19:55:13.682848
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import tempfile
    import sys
    with tempfile.NamedTemporaryFile(suffix='.py', mode='w', delete=False) as f:
        f.write('# coding: cp1255\n')
        f.write('def _():\n    u"\u05d0\u05d9\u05de\u05ea"\n')
        f.flush()
        sys.path.append(os.path.dirname(f.name))
        __import__(os.path.basename(f.name)[:-3])
        # The following is a bit hacky, but it's the way things are done.
        _ = sys.modules[os.path.basename(f.name)[:-3]]._
        __tracebackhide__ = True