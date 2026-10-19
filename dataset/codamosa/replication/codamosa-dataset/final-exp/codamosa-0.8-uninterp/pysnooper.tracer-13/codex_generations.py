

# Generated at 2022-06-12 19:47:00.049248
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def do_fake_test(arg):
        return arg
    frame = inspect.currentframe()
    frame = frame.f_back # `get_path_and_source_from_frame`
    frame = frame.f_back # `do_fake_test`
    frame = frame.f_back # `test_get_path_and_source_from_frame`
    assert get_path_and_source_from_frame(frame) == (__file__, source)

source = inspect.getsource(get_path_and_source_from_frame)
assert test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:47:04.762176
# Unit test for constructor of class Tracer
def test_Tracer():
    print('\nTest the construct of class Tracer')
    snoop = Tracer(watch='b')
    assert snoop.watch == [CommonVariable('b')]
    print('All passed!')

if __name__ == '__main__':
    test_Tracer()

# Generated at 2022-06-12 19:47:16.106775
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    states = []
    def _write(s):
        states.append(s)
    tr = Tracer(_write, overwrite=True, prefix='XX ')
    assert states == []
    with tr:
        assert states == []
    assert states == ['XX Starting var:.. __file__ = <repr truncated>\n', 'XX Source path:... xyz.py\n',
                      'XX New var:....... x = 3\n', 'XX New var:....... y = 4\n',
                      'XX Modifie... .. d var:.... x = 5\n',
                      'XX Modifie... .. d var:.... y = 6\n',
                      'XX Modifie... .. d var:.... z = 7\n', 'XX Elapsed time... 0:00:00.000001\n']


# Generated at 2022-06-12 19:47:19.577035
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    write_function = FileWriter(tempfile.NamedTemporaryFile().name,
                                overwrite=True).write
    write_function(u'hello\n')
    write_function(u'world\n')



# Generated at 2022-06-12 19:47:27.249130
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # assertion: should raise NotImplementedError
    import inspect
    import sys
    import pycompat
    import threading
    import functools
    import datetime
    import pysnooper
    import utils
    # Unit test for method _wrap_function of class Tracer
    def test_Tracer__wrap_function():
        # assertion: should raise NotImplementedError
        # assertion: should raise NotImplementedError
        # assertion: should raise NotImplementedError
        # Unit test for method _wrap_class of class Tracer
        def test_Tracer__wrap_class():
            pass
        pass
    # Unit test for method _is_internal_frame of class Tracer
    def test_Tracer__is_internal_frame():
        pass
    # Unit test for method set_thread_info_padding of class

# Generated at 2022-06-12 19:47:30.001200
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        pass
    
    assert get_path_and_source_from_frame(inspect.currentframe()) \
               == (foo.__code__.co_filename, foo.__code__.co_code)



# Generated at 2022-06-12 19:47:39.506499
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    trace = Tracer(output=None)
    assert trace.depth == 1
    assert trace.thread_info == False
    assert trace.thread_info_padding == 0
    assert trace.target_codes == set()
    assert trace.target_frames == set()
    assert trace.thread_local == threading.local()
    assert trace.last_source_path == None
    assert trace.max_variable_length == 100
    assert trace.relative_time == False

    thread_global.depth = -1
    frame = inspect.currentframe().f_back
    if not trace._is_internal_frame(frame):
        frame.f_trace = trace.trace
        trace.target_frames.add(frame)
        assert trace.target_frames == set([frame])
    else:
        assert trace.target_frames == set()

   

# Generated at 2022-06-12 19:47:50.162013
# Unit test for constructor of class Tracer
def test_Tracer():
    import unittest
    import io
    import sys

    class Test_Tracer_Constructor(unittest.TestCase):
        def setUp(self):
            self.tracer = Tracer(watch=('my_var', 'my_list_var[1]'),
                                 watch_explode=('my_list_var',),
                                 prefix='TRACE ')

        def test_output_and_write(self):
            self.assertEqual(sys.stdout, self.tracer._write)
            self.assertEqual(type(self.tracer), Tracer)

        def test_watch_and_watch_explode(self):
            self.assertEqual('my_var', self.tracer.watch[0].name)

# Generated at 2022-06-12 19:47:57.183941
# Unit test for method __enter__ of class Tracer

# Generated at 2022-06-12 19:48:00.649284
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        return 7 # line 3
    frame = inspect.currentframe().f_back
    file_name, lines = get_path_and_source_from_frame(frame)
    assert lines[3] == '    return 7 # line 3'



# Generated at 2022-06-12 19:48:26.107795
# Unit test for function get_write_function
def test_get_write_function():
    frame = inspect.currentframe()

    assert get_write_function(output=sys.stderr, overwrite=False) is not None
    assert get_write_function(output=sys.stdout, overwrite=True) is not None
    assert get_write_function(output='file.txt', overwrite=False) is not None
    assert get_write_function(output=frame, overwrite=True) is None

    output_stream = utils.WritableStream(sys.stdout)
    assert get_write_function(output=output_stream, overwrite=False) is not None
    assert get_write_function(output=output_stream, overwrite=True) is None



# Generated at 2022-06-12 19:48:31.493705
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def test_decorator(function_or_class):
        return Tracer()(function_or_class)

    def test_function():
        return True
    test_decorator(test_function)()
    #assert False # TODO: implement your test here


# Generated at 2022-06-12 19:48:42.719159
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import types
    import doctest
    _test_program_source = '''
    def foo(x):
        return x + 2  # <-- Line where the bug happens
        return x ** 2

    '''
    _test_program = imp.new_module('_test_program')
    exec(_test_program_source, _test_program.__dict__)
    _test_program_foo = _test_program.foo
    _test_program_foo.__name__ = 'foo'

    _test_program_foo_frame = _test_program_foo.func_code.co_filename
    _test_program_foo_source = _test_program_foo.func_code.co_consts[0]

# Generated at 2022-06-12 19:48:52.035429
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # Test that the decorated function can be called successfully
    # Actual implementation is tested in test_pysnooper_decorator
    import os
    import io

    def test_method(a, b, c=1, d='a'):
        return a + b + c + len(d)

    tracer = Tracer(output=io.StringIO())
    wrapper = tracer._wrap_function(test_method)
    assert wrapper(1, 2, c=3, d='abe') == 7

    # Test that we can call a recursive function -- this is tricky because we
    # set the tracing function in __enter__ and use a variable to keep track
    # of the depth level, so we make sure the tracer does the right thing
    # even when the function calls itself recursively in the same stack frame.

# Generated at 2022-06-12 19:48:58.859415
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class CustomException(Exception):
        pass

    # Case 1: a return event in the middle of a function
    with Tracer():
        pass

    # Case 2: a return event at the end of a function
    with Tracer():
        # append return value
        return 1

    # Case 3: a return event terminated by exception
    with Tracer():
        return None

    # Case 4: a return event at the end of a generator
    def gen():
        yield 1
        return TestTracer.return_value
    TestTracer.return_value = 10
    with Tracer():
        assert list(gen()) == [1]

    # Case 5: a return event terminated by exception
    with Tracer():
        raise CustomException()

    # Case 6: a line event
    with Tracer():
        pass

    # Case 7: a call

# Generated at 2022-06-12 19:49:08.145219
# Unit test for constructor of class Tracer
def test_Tracer():
    tracer = Tracer()
    tracer = Tracer(watch='foo')
    tracer = Tracer(watch=('foo', 'bar'))
    tracer = Tracer(watch_explode='foo')
    tracer = Tracer(watch_explode=('foo', 'bar'))
    tracer = Tracer(watch=['foo', 'bar'])
    tracer = Tracer(watch_explode=('foo', 'bar'))
    tracer = Tracer(prefix='XX ')
    tracer = Tracer(relative_time=True)
    tracer = Tracer(prefix='XX ', relative_time=True)
    tracer = Tracer(thread_info=True)
    tracer = Tracer(custom_repr=((str, str.upper),))

# Generated at 2022-06-12 19:49:19.837757
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import os
    import tempfile
    import pytest

    @pysnooper.snoop()
    def f():
        pass

    with pytest.raises(IOError):
        f()
    with tempfile.TemporaryDirectory() as tempdir:
        path = os.path.join(tempdir, 'output.log')
        with pytest.raises(IOError):
            pysnooper.snoop(path)(f)()

    with tempfile.TemporaryDirectory() as tempdir:
        path = os.path.join(tempdir, 'output.log')
        f = pysnooper.snoop(path, overwrite=True)(f)
        with pytest.raises(IOError):
            f()
        f()

    with tempfile.TemporaryDirectory() as tempdir:
        path

# Generated at 2022-06-12 19:49:29.994787
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import six
    import os.path
    import tempfile
    from six.moves import Reloader
    import site
    import sys

    def get_path_and_source_from_frame_from_module():
        def func():
            return get_path_and_source_from_frame(sys._getframe())
        return func

    def run(code, checker):
        with tempfile.NamedTemporaryFile('w+t') as temp_file:
            temp_file.write(code)
            temp_file.flush()


# Generated at 2022-06-12 19:49:39.465885
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def some_function(x):
        '''
        >>> a = 1
        >>> b = 'a'
        '''
        return x + 3

    frame = sys._getframe(0)
    (filename, source) = get_path_and_source_from_frame(frame)
    assert source == ['    def some_function(x):',
                      "        '''",
                      '        >>> a = 1',
                      "        >>> b = 'a'",
                      "        '''",
                      '        return x + 3',
                      '']
    assert os.path.abspath(filename) == inspect.getsourcefile(some_function)



# Generated at 2022-06-12 19:49:50.909655
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    from io import StringIO
    from datetime import datetime, timedelta
    from threading import Thread
    import logging

    import pysnooper
    import re
    import pysnooper
    import pytest

    # context manager that always used in test case
    class StreamCapture(object):
        def __init__(self):
            self.capture = StringIO()

        def __enter__(self):
            self.original_write = pysnooper.utils.write
            pysnooper.utils.write = self.capture.write
            return self.capture

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.capture.close()
            pysnooper.utils.write = self.original_write

    # make depth = 1

# Generated at 2022-06-12 19:51:11.585745
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import pysnooper
    @pysnooper.snoop()
    def test():
        a = 1
        global a
        a = 3
    test()
    print('\n')

    @pysnooper.snoop()
    def test():
        a = 1
        b = 1
        c = 1
        global a
        try:
            a = 1/0
        except ZeroDivisionError:
            pass
        a = 3
    test()
    print('\n')

    @pysnooper.snoop()
    def test():
        a = 1
        b = 1
        c = 1
        global a
        a = 3
        return 10
    test()
    print('\n')


# Generated at 2022-06-12 19:51:12.234526
# Unit test for function get_path_and_source_from_frame

# Generated at 2022-06-12 19:51:16.658378
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def function1(arg):
        'This is function 1.'
        return 1

    def function2(arg):
        'This is function 2.'
        return 2

    filename, source = get_path_and_source_from_frame(function1.__code__.co_filename)
    assert filename == function1.__code__.co_filename
    assert source == inspect.getsource(function1).splitlines()

    filename, source = get_path_and_source_from_frame(function2.__code__.co_filename)
    assert filename == function2.__code__.co_filename
    assert source == inspect.getsource(function2).splitlines()



# Generated at 2022-06-12 19:51:20.484442
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    snoop = Tracer(watch=('a',))
    def foo():
        a = 1
        return
    frame = inspect.currentframe()
    snooper.Tracer.trace(snoop, frame, 'call', 1)
    assert snoop.frame
    snoop.frame_to_local_reprs[frame] = {'a':10}
    snooper.Tracer.trace(snoop, frame, 'return', 2)
    assert not snoop.frame

# Generated at 2022-06-12 19:51:26.969837
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import re, subprocess
    from contextlib import contextmanager
    if os.path.exists('/usr/local/bin/python3.7'): python = '/usr/local/bin/python3.7'
    else: python = 'python3.7'

# Generated at 2022-06-12 19:51:36.989619
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import inspect
    import io
    import mock
    import pysnooper
    import six.moves
    import sys
    import threading
    import unittest
    import warnings
    import os
    import shutil
    import tempfile
    import datetime
    import time

    from . import utils
    from .utils import PY2

    class Test(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.StringIO = io.StringIO if six.PY3 else six.StringIO

        def get_output(self, function, *args, **kwargs):
            file_obj = self.StringIO()

# Generated at 2022-06-12 19:51:43.891554
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        pass
    module_name, _, _, _, _, _ = inspect.getouterframes(inspect.currentframe()
                                                       )[1]
    assert get_path_and_source_from_frame(sys._getframe()) == (
        os.path.join(utils.get_human_readable_path(__file__), 'utils.py'),
        UnavailableSource()
    )
    foo.__module__ = module_name

# Generated at 2022-06-12 19:51:49.730540
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    output_file = tempfile.NamedTemporaryFile(mode='r+')
    output_file_path = output_file.name
    writer = FileWriter(output_file_path, overwrite=True)
    writer.write('ABC')
    output_file.flush()
    output_file.seek(0)
    assert output_file.read() == 'ABC'


# todo: move this to utils

# Generated at 2022-06-12 19:52:00.515780
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    if __verbose__:
        print('Running ' + __file__)

    # Create a file for output
    output_file = tempfile.NamedTemporaryFile(delete=False)
    output_file.close()

    # Call the method
    output = output_file.name
    watch=()
    watch_explode=()
    depth=1
    prefix=''
    overwrite=False
    thread_info=True
    custom_repr=()
    max_variable_length=100
    normalize=False
    relative_time=True

# Generated at 2022-06-12 19:52:10.589252
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from . import frame
    from . import function_wrapping
    from . import decorator
    from . import hook
    from . import tracing
    from . import stepping
    from . import event
    from . import common
    from . import states
    from . import events
    from . import frames
    from . import variables
    from . import line_ranges
    from . import utils
    from . import watched_values
    from . import my_assertions
    from . import fake_module
    from . import pyi_source
    from . import pycompat
    from . import breakpoints
    from . import watches
    from . import call_handlers
    from . import tools
    from . import tools
    from . import tools

    # Common test


# Generated at 2022-06-12 19:52:58.799372
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # See https://github.com/cool-RR/PySnooper/pull/58 for context
    sys.settrace(None)
    with pysnooper.snoop():
        assert pysnooper._thread_local.original_trace_functions == [None]
        sys.settrace(lambda *_: None)
    assert pysnooper._thread_local.original_trace_functions == [None]


# Generated at 2022-06-12 19:53:05.288028
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    '''
    Tests the entering of a Tracer object.
    '''
    tracer = Tracer(watch=(), watch_explode=(), depth=1, prefix='', overwrite=False, thread_info=False, custom_repr=(), max_variable_length=100, normalize=False, relative_time=False)
    
    return tracer.__enter__() # should not raise AttributeError

# Generated at 2022-06-12 19:53:10.663618
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    path = pycompat.text_type(tempfile.mkstemp()[1])
    try:
        fw = FileWriter(path, True)
        fw.write(u'content1')
        fw.write(u'content2')
        with open(path, 'r') as f:
            assert f.read() == 'content2'
    finally:
        os.remove(path)


# Generated at 2022-06-12 19:53:16.737369
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    file_writer = FileWriter('file.txt', overwrite=True)
    file_writer.write('foo')
    file_writer.write('bar')
    with open('file.txt', 'r') as foo:
        assert foo.readlines() == ['foo']
    file_writer = FileWriter('file.txt', overwrite=False)
    file_writer.write('foo')
    file_writer.write('bar')
    with open('file.txt', 'r') as foo:
        assert foo.readlines() == ['foo', 'bar', 'foo', 'bar']
    os.remove('file.txt')



# Generated at 2022-06-12 19:53:27.257086
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # This is a test to see that the trace method of Tracer works
    import pysnooper

    # We first need to create a function that can be traced
    @pysnooper.snoop()
    def simple():
        a = 10
        print(a)

    # This is the Tracer instance that will be used
    snoop = pysnooper.Snooper().__enter__()

    # We can now call the trace method
    trace_value = snoop.trace(None, 'call', None)

    # I don't know what the trace method actually does
    print(trace_value)

# Generated at 2022-06-12 19:53:38.927137
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
  lcl = locals()
  # lcl = {'Tracer': pysnooper.Tracer, 'watch': (), 'watch_explode': (), 'depth': 1, 'prefix': '', 'overwrite': False, 'thread_info': False, 'custom_repr': (), 'max_variable_length': 100, 'normalize': False, '__annotations__': {'watch': tuple, 'watch_explode': tuple, 'depth': int, 'prefix': str, 'overwrite': bool, 'thread_info': bool, 'custom_repr': tuple, 'max_variable_length': int, 'normalize': bool, 'relative_time': bool}, 'relative_time': False, 'DISABLED': False, 'output': None, 'function_or_class': None, 'function': None, 'cls': None, 'snooper': p

# Generated at 2022-06-12 19:53:39.770882
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pytest.skip('Not implemented')



# Generated at 2022-06-12 19:53:51.671290
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_function(x):
        y = 2
        return x + y

    def fake_loader(path):
        return ['def fake_function(x):', '    y = 2', '    return x + y']

    assert(get_path_and_source_from_frame(
        inspect.currentframe())[1][1] == '    y = 2')


# Generated at 2022-06-12 19:53:58.560615
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    globs = {}
    module_name = globs['__name__'] = 'my_module'
    file_name = 'my_module.py'
    frame = utils.Frame(globs=globs, code=utils.Code(co_filename=file_name))
    loader = utils.Loader()
    globs['__loader__'] = loader
    source = u'This is a test.\n'
    loader.get_source = lambda module_name: source
    assert get_path_and_source_from_frame(frame) == \
           (file_name, source.splitlines())
    del globs['__loader__']
    assert get_path_and_source_from_frame(frame) == \
           (file_name, [source])



# Generated at 2022-06-12 19:54:04.455812
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    frame = sys._getframe()
    path, source = get_path_and_source_from_frame(frame)
    assert path == __file__
    assert source[frame.f_lineno - 1].strip() == 'path, source = get_path_and_source_from_frame(frame)'
    assert source[-1].strip() == 'test_get_path_and_source_from_frame()'


# Generated at 2022-06-12 19:54:46.225609
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import copy
    import difflib
    import functools
    import io
    import linecache
    import random
    import re
    import string
    import sys
    import unittest

    import pysnooper

    def random_string(max_length=None):
        length = random.randint(0, max_length or 100)
        return ''.join(random.choice(string.printable)
                       for _ in range(length))

    # Note: using a global to enable special handling of mock `open` in
    # `open_module_source`
    global _saved_open

    def open_module_source(module):
        if module.__name__ == 'mock':
            global _saved_open
            saved_open = _saved_open
            _saved_open = open
            globals

# Generated at 2022-06-12 19:54:56.904555
# Unit test for constructor of class Tracer
def test_Tracer():
    output = StringIO()
    @pysnooper.snoop(output=output, watch=("my_variable",),
          watch_explode=("my_dictionary",), depth=2,
          prefix='ZZZ ', overwrite=False, thread_info=True, custom_repr=(),
          max_variable_length=100, normalize=False, relative_time=False)
    def test(a, b):
        print("test", a, b)
        my_dictionary = {(1, 2): "hello"}
        for i in [1, 2]:
            my_variable = my_dictionary
            print("test_function")

    test(1,2)
    print(output.getvalue(), end="")
    # output_should_be =
# ZZZ Starting var:.. a = 1
# ZZZ

# Generated at 2022-06-12 19:55:04.455256
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    # When writing to file, FileWriter will append to the file if overwrite is
    # True
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        path = f.name
        f.write("first")

    fw = FileWriter(path, False)
    fw.write("second")

    with open(path, encoding='utf-8') as f:
        assert f.read() == "firstsecond"

    fw = FileWriter(path, True)
    fw.write("third")
    with open(path, encoding='utf-8') as f:
        assert f.read() == "third"


# Generated at 2022-06-12 19:55:13.613483
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def method_test():
        with pysnooper.snoop():
            pass
        print("hello")
    snoop = pysnooper.Snooper(watch=('self',))
    snoop.target_codes = set()
    snoop.target_codes.add(method_test.__code__)
    snoop.frame_to_local_reprs = {}
    snoop.thread_info_padding = 0
    snoop.depth = 1
    snoop.start_times = {}
    frame = inspect.currentframe()
    snoop.target_frames = set()
    snoop.target_frames.add(frame)
    snoop.start_times[frame] = datetime_module.datetime.now()
    snoop.max_variable_length = 100
    calling_frame = inspect.current

# Generated at 2022-06-12 19:55:20.309456
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    with pytest.raises(NotImplementedError) as exc_info:
        Tracer(output=None, watch=(), watch_explode=(), depth=1,
               prefix='', overwrite=False, thread_info=False, custom_repr=(),
               max_variable_length=100, normalize=False, relative_time=False).__enter__()
    assert exc_info.type is NotImplementedError


# Generated at 2022-06-12 19:55:24.509781
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer()
    tracer.depth = 1
    tracer.depth = 1
    tracer.thread_local = threading.local()
    thread_global = threading.local()

    tracer.thread_local.original_trace_functions = []
    tracer.__exit__(None, None, None)
    if tracer.thread_local.original_trace_functions:
        return 1
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(test_Tracer___exit__())

# Generated at 2022-06-12 19:55:31.976056
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = pysnooper.Snooper()
    DISABLED = False
    thread_global = threading.local()
    for _, __, ___ in [({}, None, None)]:
        if DISABLED:
            return
        thread_global.depth = -1
        calling_frame = inspect.currentframe().f_back
        if not tracer._is_internal_frame(calling_frame):
            calling_frame.f_trace = tracer.trace
            tracer.target_frames.add(calling_frame)

        stack = tracer.thread_local.__dict__.setdefault(
            'original_trace_functions', []
        )
        stack.append(sys.gettrace())
        tracer.start_times[calling_frame] = datetime_module.datetime.now()

# Generated at 2022-06-12 19:55:39.779263
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import pytest
    import tempfile
    path = tempfile.mktemp()
    file_writer = FileWriter(path, overwrite = True)
    s = 'abc'
    with open(path, mode = 'w', encoding = 'utf-8') as file:
        file.write(s)
    with open(path, mode = 'r', encoding = 'utf-8') as file:
        assert file.read() == s
    file_writer.write(s)
    with open(path, mode = 'r', encoding = 'utf-8') as file:
        assert file.read() == s
    file_writer.overwrite = True
    file_writer.write(s)
    with open(path, mode = 'r', encoding = 'utf-8') as file:
        assert file.read() == s
    file_writer

# Generated at 2022-06-12 19:55:42.810385
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def func():
        pass
    from .utils import FakeFrame
    frame = FakeFrame(func, {})
    path, source = get_path_and_source_from_frame(frame)
    assert path.endswith('snoop.py')
    assert source[0].startswith('# Copyright 2019 Ram Rachum and collaborators.')



# Generated at 2022-06-12 19:55:48.696343
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    t = Tracer(watch=['foo'])
    initial_var_list = {'foo':{'foo': ['hi'], 'bar': 'baz'}, 'baz': ['fruit', 'bar', 'cake'], 'qux': 1}
    frame = inspect.currentframe()
    frame.f_globals.update(initial_var_list)
    assert t.frame_to_local_reprs == {}
    assert t.watch == [CommonVariable('foo'), CommonVariable('baz')]
    assert t.depth==1
    assert t.start_times == {}
    assert t.target_codes == set()
    assert t.target_frames == set()
    assert t.thread_info==False

    t.trace(frame,'return',{'foo':['hi', 'bye']})
    frame.f