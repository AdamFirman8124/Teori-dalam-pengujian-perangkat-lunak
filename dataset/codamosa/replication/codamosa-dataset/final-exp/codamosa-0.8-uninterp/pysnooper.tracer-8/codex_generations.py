

# Generated at 2022-06-12 19:46:47.265972
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global DISABLED
    DISABLED = False
    class Test:
        def foo(self):
            pass
        def bar(self):
            pass
    test = Test()
    tr = Tracer(watch=('self',))
    tr.trace(test.foo.__code__, 'call', 'foo')
    tr.trace(test.bar.__code__, 'call', 'bar')
    tr.trace(test.foo.__code__, 'return', 'foo')
    tr.trace(test.bar.__code__, 'return', 'bar')
    if DISABLED:
        return
    assert len(tr.watch) == 1
    assert tr.watch[0].name == 'self'
    assert tr.watch[0].obj == 'self'
    assert len(tr.target_codes) == 2


# Generated at 2022-06-12 19:46:58.732649
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class TestTracer(unittest.TestCase):
        def setUp(self):
            self.tracer = Tracer(depth=1, max_variable_length=100,
                                 normalize=False, prefix='', relative_time=False,
                                 thread_info=False, watch=[], watch_explode=[])

        def tearDown(self):
            pass


        def test_Tracer_trace_0(self):
            pass


        def test_Tracer_trace_1(self):
            pass


        def test_Tracer_trace_2(self):
            pass


        def test_Tracer_trace_3(self):
            pass


        def test_Tracer_trace_4(self):
            pass


        def test_Tracer_trace_5(self):
            pass




# Generated at 2022-06-12 19:47:09.820034
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = pysnooper.snoop(watch=('foo', 'self'))
    tracer.write = mock.Mock()
    tracer.depth = 2
    tracer.start_times[2] = 3
    tracer.target_frames.add(1)
    tracer.frame_to_local_reprs[1] = "1"
    tracer.thread_local.original_trace_functions = [1,2]
    sys.gettrace = mock.Mock(return_value=0)
    sys.settrace = mock.Mock()
    tracer.__exit__(None, None, None)
    assert tracer.frame_to_local_reprs.get(1) == None

# Generated at 2022-06-12 19:47:18.551322
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from types import FrameType
    import time
    import timeit
    class MockTraceFunction(object):
        def __init__(self):
            self.debug_message = "Trace function changed"
            self.stack = []
        def trace(self, frame, event, arg):
            self.stack.append((frame, event, arg))
    class MockFrame(object):
        def __init__(self, f_lineno=0, f_code="f_code", f_lasti=0):
            self.f_lineno = f_lineno
            self.f_code = f_code
            self.f_lasti = f_lasti
        def f_trace(self, tracefunc):
            pass
    class MockTime(datetime_module.datetime):
        def __init__(self):
            super

# Generated at 2022-06-12 19:47:19.828285
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert get_path_and_source_from_frame(sys._getframe())



# Generated at 2022-06-12 19:47:27.384911
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import os
    import sys
    import types
    import tempfile
    import unittest
    import unittest.mock
    import pysnooper.utils as utils
    import pysnooper.advanced_usage as advanced_usage
    import pysnooper.advanced_usage_test as advanced_usage_test
    import pysnooper.main as main
    import pysnooper.main_test as main_test
    import pysnooper.utils_test as utils_test
    import pysnooper.utils as utils
    from pysnooper import snoop as snoop
    from pysnooper import snoop_decorator as snoop_decorator
    from pysnooper.snoop_decorator import _Tracer as _Tracer


    # class TestTest_Tr

# Generated at 2022-06-12 19:47:34.079203
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # Test 1
    def get_write_function(): pass
    def get_path_and_source_from_frame(): pass
    def get_local_reprs(): pass
    def get_shortish_repr(): pass
    def truncate(): pass
    class BaseVariable(object): pass
    class CommonVariable(BaseVariable): pass
    class Exploding(BaseVariable): pass
    class SourcePath(object):
        def __init__(self):
            self.source_path = '.py'
    class Frame(object):
        def __init__(self):
            self.f_code = SourcePath()
            self.f_lineno = '0'
    class Pycompat(object):
        class CollectionsAbc(object):
            class Iterable(object): pass
        class TimeIsoformat(object): pass

# Generated at 2022-06-12 19:47:35.795109
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # pass  # To be implemented or nothing to test()
    # print("Nothing to test")
    pass


# Generated at 2022-06-12 19:47:38.674974
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        source = get_path_and_source_from_frame(inspect.currentframe())[1]
        return source[0]
    assert foo() == 'def foo():'



# Generated at 2022-06-12 19:47:42.358364
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    print('Test Tracer.__exit__():')

    def test_function():
        pass
    with Tracer(output=None):
        test_function()

# Generated at 2022-06-12 19:48:02.047487
# Unit test for constructor of class Tracer
def test_Tracer():
    @pysnooper.snoop()
    def foo():
        print('hello')


# Generated at 2022-06-12 19:48:07.605369
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    import os
    import pytest
    path = tempfile.mktemp()
    with pytest.raises(Exception):
        FileWriter(path, True).write('test 1')
        FileWriter(path, True).write('test 2')
    assert FileWriter(path, False).write('test 1')
    assert FileWriter(path, False).write('test 2')
    assert open(path, 'r').read() == 'test 1\ntest 2'
    # cleanup
    os.remove(path)
#test_FileWriter_write()


# Generated at 2022-06-12 19:48:12.783358
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    def test_with_depth1():
        output = []
        tracer = Tracer(lambda s: output.append(s), depth=1)
        tracer.__exit__(None, None, None)
        assert output == []
        assert 1 == 1
    test_with_depth1()


# Generated at 2022-06-12 19:48:20.936449
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    test_context = dict(__loader__=None, __name__='__main__',
                        __file__='dummy_file_name')
    test_frame = sys.getframe()
    test_frame.f_globals = test_context
    test_frame.f_code.co_filename = 'dummy_file_name'
    assert get_path_and_source_from_frame(test_frame) == \
                                               ('dummy_file_name',None)



# Generated at 2022-06-12 19:48:30.817127
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import time
    import datetime as d
    from collections import namedtuple as nt
    from pysnooper import snoop
    from pysnooper import utils
    from pysnooper import pycompat
    from pysnooper import opcode
    from pysnooper import datetime_module
    from pysnooper import inspect
    from pysnooper import traceback
    from pysnooper import threading
    from pysnooper import get_write_function
    from pysnooper import get_path_and_source_from_frame
    from pysnooper import functools
    from pysnooper import BaseVariable
    from pysnooper import CommonVariable
    from pysnooper import Exploding
    from pysnooper.utils import SHORTISH_LENGTH

# Generated at 2022-06-12 19:48:42.229762
# Unit test for constructor of class Tracer
def test_Tracer():

   @pysnooper.snoop()
   def foo():
      bar()

   def bar():
       pass

   def baz():
       pass

   tracer = Tracer()
   tracer._wrap_function(foo)

   assert tracer.target_codes == {foo.__code__}
   assert tracer.target_frames == set()
   assert tracer.frame_to_local_reprs == {}
   assert tracer.start_times == {}
   assert tracer.thread_local.__dict__ == {}
   assert tracer.watch == []
   assert tracer.depth == 1
   assert tracer.prefix == ''
   assert tracer.target_codes == {foo.__code__}
   assert tracer.thread_info == False
   assert tracer.thread_info_padding == 0

# Generated at 2022-06-12 19:48:46.758478
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    '''
    Unit test for method __exit__ of class Tracer
    '''
    # Initialize test variables
    pysnooper.snoop = Tracer()
    exc_type = None
    exc_value = None
    exc_traceback = None
    assert True


# Generated at 2022-06-12 19:48:56.758943
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_function():
        '''
        hehe
        '''
        return 3

    assert get_path_and_source_from_frame(inspect.currentframe())[0] == os.path.abspath(__file__)
    assert get_path_and_source_from_frame(test_function.__code__.co_firstlineno)[0] == os.path.abspath(__file__)

    from .cute_iter_tools import recursive_yield
    all_package_files, = recursive_yield(
        'sourcetools',
        regex_filter='\.py$',
        predicate=lambda path: os.path.realpath(path) != os.path.realpath(__file__)
    )

# Generated at 2022-06-12 19:49:01.922569
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import os
    import pathlib
    import tempfile
    import pysnooper
    import sys
    import threading
    import functools
    import traceback
    import datetime
    import itertools
    import opcode
    import inspect
    import pycompat
    import utils
    import contextlib
    import threading
    import re
    import builtins
    import threading
    import pycompat
    import ordered_set
    import datetime
    import os
    import posixpath
    import functools
    import pycompat
    import inspect
    import textwrap
    import pysnooper
    import sys
    import pathlib
    import os
    import pycompat
    import types
    import threading
    import json
    import itertools
    import inspect
    import datetime
   

# Generated at 2022-06-12 19:49:10.847706
# Unit test for function get_write_function
def test_get_write_function():
    from .testing import assert_value_equals
    assert_value_equals(get_write_function(None, False), sys.stderr.write)
    assert_value_equals(get_write_function(utils.WritableStream(), False),
                                           utils.WritableStream().write)
    assert_value_equals(get_write_function('foo', False),
                        FileWriter('foo', False).write)
    assert_value_equals(get_write_function(utils.WritableStream(), True),
                        utils.WritableStream().write)
    assert_value_equals(get_write_function('foo', True),
                        FileWriter('foo', True).write)



# Generated at 2022-06-12 19:49:34.832200
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    (path, source) = get_path_and_source_from_frame(
        inspect.currentframe()
    )
    source = ''.join(source)
    assert 'test_get_path_and_source_from_frame' in source



# Generated at 2022-06-12 19:49:37.247349
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():

    output = StringIO()

    with Tracer(output=output):
        pass

    assert 'Elapsed time' in output.getvalue()

# Generated at 2022-06-12 19:49:41.139512
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    if isinstance(snoop_module.Tracer.__enter__, str):
        pytest.skip('Tests for this method were skipped')
    # Undefined variables
    
    
    
    
    
    
    
    
    
    
    
    return None


# Generated at 2022-06-12 19:49:52.566135
# Unit test for constructor of class Tracer
def test_Tracer():
    t = Tracer()
    assert t.watch == []
    assert t.prefix == ''
    assert t.depth == 1
    assert t.overwrite is False
    assert t.thread_info is False
    assert t.custom_repr == ()
    assert t.max_variable_length == 100
    assert t.normalize is False
    assert t.relative_time is False

    t = Tracer(watch=('x', 'y'), watch_explode=('z',), prefix='Hello',
               depth=2, overwrite=True, thread_info=True, custom_repr=((int,
               lambda x: []),), max_variable_length=200, normalize=True,
               relative_time=True)
    assert t.watch == [CommonVariable('x'), CommonVariable('y'),
                       Exploding('z')]


# Generated at 2022-06-12 19:49:59.778494
# Unit test for constructor of class Tracer

# Generated at 2022-06-12 19:50:02.039503
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    print_debug_message("test_Tracer___exit__ is running")
    # TODO Implement
    print_error_message("test_Tracer___exit__ not implemented")

# Generated at 2022-06-12 19:50:09.908505
# Unit test for constructor of class Tracer

# Generated at 2022-06-12 19:50:12.846411
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    with Tracer() as tracer:
        x = 1 + 2
    return tracer.depth

# Generated at 2022-06-12 19:50:22.091045
# Unit test for function get_local_reprs
def test_get_local_reprs():
    result = get_local_reprs(frame=None)
    assert result == {}
    frame = utils.Frame(
        f_locals={
            'x': None,
            'y': None,
            'z': None,
        }
    )
    result = get_local_reprs(frame=frame)
    assert list(result.keys()) == ['x', 'y', 'z']
    assert result['x'] == 'None'

# Generated at 2022-06-12 19:50:24.568395
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import io
    import unittest
    import importlib.machinery
    import contextlib

# Generated at 2022-06-12 19:51:04.776835
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    output = io.StringIO()
    trace = Tracer(output)
    with trace:
        pass

# Generated at 2022-06-12 19:51:09.976586
# Unit test for function get_write_function
def test_get_write_function():
    assert callable(get_write_function(None, False))
    assert callable(get_write_function(sys.stderr, False))
    assert callable(get_write_function('hello.txt', False))
    assert callable(get_write_function(sys.stdout.write, False))
    assert callable(get_write_function(None, True))



# Generated at 2022-06-12 19:51:15.274736
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    '''Ensures that elapsed time is calculated correctly'''
    import io
    import contextlib
    import time
    import datetime
    from .localstack import LocalStack
    output_stream = io.StringIO()
    with Tracer(output_stream, depth=1):
        time.sleep(1)
    output_stream.seek(0)
    assert output_stream.readline().rstrip() == '    Elapsed time: 1:00:00'
    assert output_stream.read() == ''

# Generated at 2022-06-12 19:51:20.056598
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys

    def test_case(self,
                  frame, event, arg,
                  expected_result,
                  expected_attrs):
        with self.subTest(frame=frame,
                          event=event,
                          arg=arg):
            thread_global.__dict__.setdefault('depth', -1)
            frame.f_trace = self.tracer.trace
            self.tracer.target_frames.add(frame)
            self.tracer.frame_to_local_reprs.setdefault(frame, {})
            self.tracer.start_times.setdefault(frame, datetime_module.datetime.now())
            stack = self.tracer.thread_local.__dict__.setdefault('original_trace_functions', [])
            stack.append(sys.gettrace())
            sys

# Generated at 2022-06-12 19:51:30.902870
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import os
    import datetime_module
    output_path = gpath('pysnooper.log')
    if os.path.exists(output_path):
        os.remove(output_path)

    @pysnooper.snoop()
    def test():
        x = 13
        datetime_module.datetime.now()
        return 42

    test()

    with open(output_path) as f:
        lines = list(f)

# Generated at 2022-06-12 19:51:40.143018
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    import mock
    import tempfile
    with tempfile.NamedTemporaryFile(suffix='.py') as f:
        source = '# coding: utf-8\ne=10'.encode('utf-8')
        f.write(source)
        f.flush()
        frame = inspect.currentframe()
        frame.f_locals = utils.FastDict({'__file__': f.name})
        loader = mock.MagicMock()
        loader.get_source.return_value = source
        frame.f_globals = utils.FastDict({'__loader__': loader})
        with utils.opened(f.name) as source_file:
            source_from_frame = ''.join(get_path_and_source_from_frame(frame)[1])
           

# Generated at 2022-06-12 19:51:46.635502
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    if True:
        snoop = pysnooper.snoop()
        def f(x):
            y = x
            return y
        snoop(f)(123)
    else:
        snoop = Tracer()
        def f(x):
            y = x
            return y
        snoop(f)(123)

if __name__ == '__main__':
    test_Tracer_trace()

# Generated at 2022-06-12 19:51:53.950205
# Unit test for function get_write_function
def test_get_write_function():
    def write(s):
        print(str(s))
    import tempfile
    result = get_write_function(write, False)
    assert result == write
    fp = tempfile.NamedTemporaryFile('w')
    file_path = fp.name
    result = get_write_function(file_path, False)
    assert result != write
    result = get_write_function(file_path, False)
    result(u"abc")
    with open(file_path) as fp:
        assert fp.read() == "abc"
    result(u"xyz")
    with open(file_path) as fp:
        assert fp.read() == "abcxyz"



# Generated at 2022-06-12 19:51:55.299586
# Unit test for method trace of class Tracer

# Generated at 2022-06-12 19:52:03.639675
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import ast
    import json
    import os
    import pycodestyle
    import pylint
    import sys
    import time
    import tokenize
    import traceback
    import unittest
    import xmlschema
    import zipfile

    class BaseTestCase(unittest.TestCase):

        def test_example_description(self):
            pass

        def test_example_result(self):
            pass

    class Example(BaseTestCase):

        def setUp(self):
            self.longMessage = True
            self.maxDiff = None
            self.called_func = None


# Generated at 2022-06-12 19:52:49.777099
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
  snooper = Tracer(output=None, watch=(), watch_explode=(), depth=1, prefix='', overwrite=False, thread_info=False, custom_repr=(), max_variable_length=100, normalize=False, relative_time=False)
  return snooper.__enter__()

# Generated at 2022-06-12 19:52:58.920017
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from . import testutils
    with testutils.temporary_directory() as temporary_directory:
        source_filename = os.path.join(temporary_directory, 'test.py')
        with open(source_filename, 'w+') as source_file:
            source_file.write("'hello world'\n")
        source_file.close()
        with open(source_filename, 'r') as source_file:
            module = pycompat.exec_(source_file.read(), {})
        path, source = get_path_and_source_from_frame(inspect.currentframe())
        assert path == source_filename and source == ['\'hello world\'']


# Generated at 2022-06-12 19:53:09.509406
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from doctest import DocTestRunner, DocTest
    runner = DocTestRunner()

    source = '''
    def hello():
        """
        >>> hello()
        10
        """
        return 10
    '''

    with open('some_file.py', 'w') as f:
        f.write(source)

    globals_table = {
        'hello': hello,
    }
    locals_table = {}

    doctest = DocTest(globals_table['hello'])
    runner.run(doctest, globals_table, locals_table)

    frame = doctest.examples[0].frame

    path, source_ = get_path_and_source_from_frame(frame)

    assert path == 'some_file.py'
    assert '>>> hello()' in source_


# Generated at 2022-06-12 19:53:12.109403
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Setup
    def function_or_class():
        return
    instance = Tracer()
    exc_type = None
    exc_value = None
    exc_traceback = None

    # Exercise
    result = instance.__exit__(exc_type, exc_value, exc_traceback)

    # Verify
    assert result is None

# Generated at 2022-06-12 19:53:22.693351
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    @pysnooper.snoop()
    def f(x):
        return x

    import inspect
    assert inspect.isgenerator(f(3)) is True
    assert inspect.isgenerator(f(3).send(None)) is True
    gen = f(3)
    gen.next()
    gen.next()
    gen.close()

    import functools
    @pysnooper.snoop()
    @functools.lru_cache(maxsize=2)
    def f2(x):
        return x

    assert inspect.iscoroutinefunction(f2) is True

# Generated at 2022-06-12 19:53:27.845109
# Unit test for function get_local_reprs
def test_get_local_reprs():
    x = 1
    assert x == 1
    get_local_reprs(frame=inspect.currentframe())
    inputs = {'a': 1, 'b': '', 'c': 3j}
    for a, b, c in itertools.product(inputs.values(),
                                     inputs.values(),
                                     inputs.values()):
        get_local_reprs(frame=inspect.currentframe(),
                        watch=[CommonVariable('a', a),
                               CommonVariable('b', b),
                               CommonVariable('c', c)])
    get_local_reprs(frame=inspect.currentframe(),
                    watch=[CommonVariable('a', 1),
                           CommonVariable('b', ''),
                           CommonVariable('c', 3j)])

# Generated at 2022-06-12 19:53:31.117829
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass # Nothing to test

# Generated at 2022-06-12 19:53:36.937753
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    @pysnooper.snoop()
    def do_stuff():
        a=1
        b=2
        a,b=b,a
        print(a)
        c,d=1,2
        print(c,d,a)
        e=30
        # assert(a==b)
        f=True
        assert(f)
    try:
        do_stuff()
    except:
        pass


# Generated at 2022-06-12 19:53:46.684440
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    _snoop = snoop
    _output = output

    if _snoop:
        pass
    if _output:
        pass
    if DISABLED:
        pass
    thread_global.__dict__.setdefault('depth', -1)
    calling_frame = inspect.currentframe().f_back
    if not self._is_internal_frame(calling_frame):
        calling_frame.f_trace = self.trace
        self.target_frames.add(calling_frame)

    stack = self.thread_local.__dict__.setdefault(
        'original_trace_functions', [])
    stack.append(sys.gettrace())
    self.start_times[calling_frame] = datetime_module.datetime.now()
    sys.settrace(self.trace)

    return


# Generated at 2022-06-12 19:53:56.742924
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():

    def inner_function():
        source_and_path_cache.clear()

        def outer_function():
            pass

        result = get_path_and_source_from_frame(inspect.currentframe())
        assert len(result) == 2
        path, source = result
        assert path == __file__
        assert source == [u'def inner_function():']

        result = get_path_and_source_from_frame(inspect.currentframe(1))
        assert len(result) == 2
        path, source = result
        assert path == __file__
        expected = [u'def outer_function():', u'    pass']
        assert source == expected

        result = get_path_and_source_from_frame(inspect.currentframe(2))
        assert len(result) == 2

# Generated at 2022-06-12 19:54:54.080354
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    global DISABLED
    DISABLED = False
    # Test with pytest
    with pytest.raises(Exception):
        patch_write(repr(1))

    @pysnooper.snoop()
    def f():
        e = Exception()
        raise e

    def g():
        return f()

    with pytest.raises(Exception) , patch_write(repr(1)) as write:
        g()

    assert 'pysnooper.py:751: Exception:..... Exception()' in write.getvalue()

    # Test with doctest
    class Foo(object):
        def __init__(self, var):
            self.var = var

# Generated at 2022-06-12 19:55:03.696355
# Unit test for constructor of class Tracer
def test_Tracer():
    assert not os.path.exists(SNOOSTATS_FILE)
    with Tracer() as tracer:
        x = 1
        y = 2
        z = 3
        assert tracer.watch == (utils.CommonVariable('x'), utils.CommonVariable('y'), utils.CommonVariable('z'))
        assert tracer.frame_to_local_reprs == {}
        assert tracer.start_times == {}
        assert tracer.depth == 1
        assert tracer.prefix == ''
        assert tracer.target_codes == set()
        assert tracer.target_frames == set()
        assert tracer.thread_local.original_trace_functions == []
        assert tracer.custom_repr == ()
        assert tracer.last_source_path == ''
        assert tracer.max_variable_length

# Generated at 2022-06-12 19:55:07.175346
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer(prefix="test_tracer")
    tracer.watch=["a"]
    frame = inspect.currentframe()
    frame.f_globals["a"] = "A"
    tracer.trace(frame, "return", "A")

# Generated at 2022-06-12 19:55:15.593810
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    f1 = lambda x: 0
    f2 = lambda x: x + 1
    f3 = lambda x: x + 2
    class TestTracer(Tracer):
        def trace(self, frame, event, arg):
            if frame.f_code == f1.__code__:
                assert event == 'call'
            elif frame.f_code == f2.__code__:
                if event == 'call':
                    assert arg == 0
                else:
                    assert event == 'return'
                    assert arg == 1
            elif frame.f_code == f3.__code__:
                if event == 'call':
                    assert arg == 1
                else:
                    assert event == 'return'
                    assert arg == 3
            else:
                assert False

# Generated at 2022-06-12 19:55:21.629772
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import pysnooper
    import os

    @pysnooper.snoop()
    def test(s):
        print('default')

    test('ll')

    @pysnooper.snoop(normalize=True)
    def test(s):
        print('normalize')

    test('ll')


# Generated at 2022-06-12 19:55:22.770130
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    @pysnooper.snoop()
    def f():
        pass
    f()


# Generated at 2022-06-12 19:55:27.709569
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():

    import os.path
    import types

    def test_module_with_module_source(module_source):
        '''
        Run the code in `module_source` in an anonymous module; ensure that we
        can get the source code.
        '''
        import tempfile, imp

        tmp_file, tmp_name = tempfile.mkstemp(suffix='.py')
        with os.fdopen(tmp_file, 'w') as tmp_fobj:
            tmp_fobj.write(module_source)

        module = imp.load_source('module', tmp_name)
        frame = module.get_frame()
        global_ns = frame.f_globals
        assert global_ns['__name__'] == 'module'
        assert os.path.abspath(global_ns['__file__'])

# Generated at 2022-06-12 19:55:36.254220
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import sys
    import traceback
    from pysnooper.utils import override_print
    stack = []
    def test_method():
        @pysnooper.snoop()
        def called_func():
            return 1
        with override_print():
            test_method.snooper = called_func()
    test_method()
    try:
        next(test_method.snooper)
    except StopIteration:
        # We need to output the exception so that it is not swallowed,
        # because it is later used by `tb_next` in `self.exception_handler`.
        traceback.print_exc()

# Generated at 2022-06-12 19:55:46.886810
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import __main__
    import inspect
    import datetime

    tracer = Tracer(depth=1)

    def foo(x):
        y = x + 10
        return bar(x, y)

    def bar(x, y):
        z = x + y + 10
        return z

    def test():
        tracer.start_times[foo] = datetime.datetime.now()
        tracer.start_times[bar] = datetime.datetime.now()

        tracer.target_codes = set([foo.__code__, bar.__code__])

        frame = foo.__code__.co_filename
        frame = bar.__code__.co_filename

        tracer.frame_to_local_reprs[foo] = {'x':'10'}
        tracer

# Generated at 2022-06-12 19:55:53.523857
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f(): pass
    file_path, source = get_path_and_source_from_frame(f.__code__.co_firstlineno)
    assert isinstance(source, list)
    assert '\n' not in source[0]
    assert all(isinstance(line, pycompat.text_type) for line in source)
    assert isinstance(source[0], pycompat.text_type)
    assert isinstance(file_path, str)
test_get_path_and_source_from_frame()

