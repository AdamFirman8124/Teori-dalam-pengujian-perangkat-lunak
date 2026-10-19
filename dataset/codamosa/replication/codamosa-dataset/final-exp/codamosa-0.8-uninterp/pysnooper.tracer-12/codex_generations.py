

# Generated at 2022-06-12 19:46:57.639001
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    t = Tracer(None, watch=(), watch_explode=(), depth=1,
                         prefix='', overwrite=False, thread_info=False, custom_repr=(),
                         max_variable_length=100, normalize=False, relative_time=False)
    t.frame_to_local_reprs = {inspect.currentframe(): {'a': '1'}}
    t.start_times = {inspect.currentframe(): datetime_module.datetime.now()}
    f1 = inspect.currentframe()
    f2 = inspect.currentframe().f_back
    t.target_codes.add(f1.f_code)
    t.target_codes.add(f2.f_code)
    t.target_frames.add(f1)

# Generated at 2022-06-12 19:47:08.684969
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # No exception occured, not a generator

    with mock.patch('pysnooper.core.get_path_and_source_from_frame') as (
                                                mock_get_path_and_source_from_frame):
        snoop = Tracer()
        frame = mock.create_autospec(FrameType, f_code=CodeType(name='baz'))
        frame.f_back = FrameType(f_code=CodeType(name='baz'))
        frame.f_back.f_back = FrameType(f_code=CodeType(name='foo'))
        snoop._write = mock.Mock()
        with snoop:
            pass

        assert snoop._write.call_count == 2
        __, kwargs = snoop._write.call_args
        # First call


# Generated at 2022-06-12 19:47:18.151730
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from . import pysnooper_tests
    from . import pysnooper_tests_internal
    from . import variable
    from .variable import Exploding

    min_variable_length = 50

# Generated at 2022-06-12 19:47:20.504039
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    @pysnooper.snoop()
    def test2():
        return 1
    test2()
    return
    test3()



# Generated at 2022-06-12 19:47:22.477457
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import doctest
    doctest.run_docstring_examples(Tracer.__exit__, globals(), verbose=True)

# Generated at 2022-06-12 19:47:24.575225
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer()
    frame, event, arg = inspect.currentframe(), 'return', True
    tracer.trace(frame, event, arg)

# Generated at 2022-06-12 19:47:32.190228
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import time
    import pysnooper.utils
    from pysnooper.encoding import ensure_text
    import pysnooper.compat

    self = Tracer()
    self.write = lambda x: sys.stdout.write(ensure_text(x))
    self.depth = 1
    self.prefix = ''
    self.thread_info = False
    self.thread_info_padding = 0
    self.target_codes = set()
    self.target_frames = set()
    self.frame_to_local_reprs = {}
    self.start_times = {}
    self.thread_local = threading.local()
    self.custom_repr = ()
    self.last_source_path = None
    self.max_variable_length = 100
    self.normalize

# Generated at 2022-06-12 19:47:42.977780
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from .test_integration import dummy_get_write_function
    from .test_integration import dummy_write
    from .test_integration import dummy_datetime
    from .test_integration import dummy_datetime_now
    from .test_integration import dummy_time_isoformat
    import sys
    import functools
    import inspect

    dummy_get_write_function.write_function = dummy_write
    datetime_module = dummy_datetime
    datetime_module.now = dummy_datetime_now
    pycompat.time_isoformat = dummy_time_isoformat

    class Noop(object):
        pass

    DISABLED = Noop()
    # First test of Tracer.__call__, with depth=1
    tracer = Tracer()

# Generated at 2022-06-12 19:47:52.116076
# Unit test for function get_local_reprs
def test_get_local_reprs():
    frame = sys._getframe()
    while frame:
        if frame.f_code.co_name == 'test_get_local_reprs':
            break
        frame = frame.f_back
    else:
        assert False, 'Could not find function test_get_local_reprs.'

    assert get_local_reprs(frame) == {'frame': '...'}
    assert get_local_reprs(frame, max_length=2) == {'fr': '...'}
    assert get_local_reprs(frame, max_length=3) == {'fra': '...'}
    assert get_local_reprs(frame, max_length=4) == {'fram': '...'}
    assert get_local_reprs(frame, max_length=5)

# Generated at 2022-06-12 19:47:56.502519
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():

    def simple_function():
        return simple_function()

    path, source = get_path_and_source_from_frame(
        inspect.currentframe().f_back
    )
    assert path == __file__
    assert source == ['def simple_function():', '    return simple_function()', '']



# Generated at 2022-06-12 19:48:17.821040
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame(): # pragma: no cover
    import types
    code = types.CodeType(0, 0, 0, 0, 0, u"dummy_code", (), (),
                          ("some_bytes".encode('utf-8'),), 'ENGLISH', (), (), ())

# Generated at 2022-06-12 19:48:21.878274
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import builtins
    assert get_path_and_source_from_frame(builtins.any.__code__.co_consts[-1]) == \
           (__file__, open(__file__).read().splitlines())



# Generated at 2022-06-12 19:48:25.481784
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Calling __exit__ of Tracer on an instance
    instance = Tracer()
    with pytest.raises(AttributeError):
        instance.__exit__()

    # Calling __exit__ as a class method of Tracer (should not raise)
    Tracer.__exit__(instance)


# Generated at 2022-06-12 19:48:38.025614
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import sys, os, types
    def foo():
        pass
    class Foo(object):
        def bar(self):
            pass
    foo_filename = foo.__code__.co_filename
    foo_source = inspect.getsource(foo)
    assert foo_source.endswith('\n')
    foo_source = foo_source[:-1]
    foo_path, foo_source = get_path_and_source_from_frame(sys._getframe())
    assert foo_path == foo_filename
    assert foo_source == foo_source.splitlines(True)

    foo_filename = Foo.bar.__func__.__code__.co_filename
    foo_source = inspect.getsource(Foo.bar)
    assert foo_source.endswith('\n')
    foo_source = foo_

# Generated at 2022-06-12 19:48:42.952859
# Unit test for constructor of class Tracer
def test_Tracer():
    tracer = Tracer(watch='ID_')
    assert len(tracer.watch) == 1
    assert isinstance(tracer.watch[0], CommonVariable)
    assert tracer.watch[0].name == 'ID_'
    assert tracer.watch[0].watch_all is False
    assert tracer.watch[0].max_length == 100

    tracer = Tracer(watch=('ID_',), watch_explode=('ID_', ))
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], CommonVariable)
    assert tracer.watch[0].name == 'ID_'
    assert tracer.watch[0].watch_all is False
    assert tracer.watch[0].max_length == 100

# Generated at 2022-06-12 19:48:52.126021
# Unit test for function get_local_reprs
def test_get_local_reprs():
    r1 = {'ber': '(1, 2, 3)', 'foo': '23', 'zoo': '(5, 6)'}
    assert get_local_reprs(test_get_local_reprs,
                           watch=(CommonVariable('foo'), CommonVariable('zoo')),
                           custom_repr={tuple:
                                        lambda t: '({})'.format(', '.join(str(x) for x in t))},
                           max_length=None, normalize=False) == r1

# Generated at 2022-06-12 19:48:59.896912
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    import os
    import contextlib
    with tempfile.TemporaryDirectory() as directory_path:
        path = os.path.join(directory_path, 'file.txt')
        with contextlib.closing(FileWriter(path, overwrite=True)) as file_writer:
            file_writer.write('abc')
        with open(path, 'r') as fixed_file:
            assert fixed_file.read() == 'abc'
        with contextlib.closing(FileWriter(path, overwrite=False)) as file_writer:
            file_writer.write('123')
        with open(path, 'r') as fixed_file:
            assert fixed_file.read() == 'abc123'



# Generated at 2022-06-12 19:49:08.893244
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer()
    tracer.write = mock.Mock()
    tracer.target_codes = {1}
    tracer.target_frames = {2}
    tracer.depth = 5
    tracer.watch = {}
    tracer.frame_to_local_reprs = {}
    tracer.start_times = {}
    tracer.thread_info_padding = 0
    tracer.thread_info = True
    tracer.normalize = False
    tracer.relative_time = False
    tracer.last_source_path = None
    test_frame = mock.Mock()
    test_frame.f_code = mock.Mock()
    test_frame.f_code.co_filename = 3
    test_frame.f_lineno = 4
    test_frame.f_

# Generated at 2022-06-12 19:49:15.606612
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import types
    test_module = types.ModuleType(__name__)
    frame = sys._getframe(0)
    frame.f_globals = test_module.__dict__
    frame.f_code.co_filename = __file__
    test_module.__loader__ = None
    assert get_path_and_source_from_frame(frame) == (
        __file__, source_and_path_cache[(__name__, __file__)][1]
    )


# Generated at 2022-06-12 19:49:16.911440
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    Tracer(overwrite=True)

# Generated at 2022-06-12 19:49:43.273159
# Unit test for function get_write_function
def test_get_write_function():
    import io
    import tempfile

    write('') # Make sure that this function works on empty strings
    stream = io.StringIO()
    dest = stream.write
    write = get_write_function(dest, overwrite=False)
    assert write is dest, 'write is not the same as dest'
    write, dest = dest, write
    stream.write('asdf')
    assert stream.getvalue() == 'asdf'
    write('bloop')
    assert stream.getvalue() == 'asdfbloop'

    path = tempfile.NamedTemporaryFile().name
    write = get_write_function(path, overwrite=True)
    write('bleep')
    with open(path) as f:
        assert f.read() == 'bleep', "File didn't get written to"
    write('')


# Generated at 2022-06-12 19:49:54.293834
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def func1(): pass
    func2 = lambda: None
    def func3():
        func4 = lambda: None
        return func4()
    func3()
    assert (get_path_and_source_from_frame(func1.__globals__) ==
            get_path_and_source_from_frame(func2.__globals__) ==
            get_path_and_source_from_frame(func3.__globals__) ==
            get_path_and_source_from_frame(func4.__globals__))
    func5 = get_path_and_source_from_frame

# Generated at 2022-06-12 19:50:06.091088
# Unit test for function get_local_reprs
def test_get_local_reprs():
    from . import variables
    from .utils import normalize_windows_path
    from . import pycompat
    from . import utils
    from .testing.utils import (assert_equal, assert_not_equal,
                                make_set_of_module_names_for_future_py3)

    def sample(a, b=2):
        print('In sample now')
        return a + b

    frame = inspect.currentframe()
    try:
        caller_frame = frame.f_back
    finally:
        del frame


# Generated at 2022-06-12 19:50:08.305682
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    snooper = pysnooper.Snooper()
    result = snooper.__enter__()
    assert result is None
    expected = None
    assert result == expected


# Generated at 2022-06-12 19:50:14.158632
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import sys
    import threading
    import traceback
    import pysnooper.utils
    with Tracer(watch=('a', 'b')) as tracer:
        a = '1'
        b = 2
    locals_reprs = tracer.frame_to_local_reprs[sys._getframe()]
    locals_reprs['a'] == "'1'"
    locals_reprs['b'] == '2'
    exit_frame = sys._getframe(1)
    tracer.frame_to_local_reprs.pop(exit_frame, None)
    tracer.start_times.pop(exit_frame, None)
    thread_global.depth -= 1

# Generated at 2022-06-12 19:50:20.516758
# Unit test for function get_write_function
def test_get_write_function():
    import sys
    import io
    import tempfile

    old_stderr = sys.stderr
    old_stdout = sys.stdout

    assert get_write_function(io.StringIO(), overwrite=True) == None
    assert get_write_function(io.StringIO(), overwrite=False) == None

    sys.stderr = io.StringIO()
    get_write_function(None, overwrite=False)('test')
    assert sys.stderr.getvalue() == 'test'


# Generated at 2022-06-12 19:50:22.401591
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    #self.assertEqual(expected, Tracer.trace(frame, event, arg))
    assert False # TODO: implement your test here


# Generated at 2022-06-12 19:50:29.037715
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pytest
    import inspect
    import functools
    import threading
    import types
    patch_datetime()
    patch_time()
    patch_trace()
    class MockInspect(object):
        def currentframe(self):
            return 'mock inspect currentframe'
    def mock_inspect_isclass(x):
        return x == 'mock inspect isclass'
    def mock_inspect_isfunction(x):
        return x == 'mock inspect isfunction'
    def mock_inspect_isgeneratorfunction(x):
        return x == 'mock inspect isgeneratorfunction'
    def mock_ensure_tuple(x):
        return x == 'mock ensure_tuple'

# Generated at 2022-06-12 19:50:38.123809
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def some_function(x, y):
        return x + y
    def some_other_function(x, y):
        return x + y

    t = Tracer()
    p = t(some_function)
    assert p == some_function
    assert p.__name__ == 'some_function'
    assert p.__doc__ == 'some_docstring'
    assert p.__dict__ == {}

    ########################################################################
    # Class decorator
    ########################################################################
    class SomeClass:
        def some_method(self, x, y):
            return x + y
        def some_other_method(self, x, y):
            return x + y


# Generated at 2022-06-12 19:50:44.459113
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    with Tracer():
        pass
## END OF USER INPUT -- DO NOT EDIT BELOW THIS LINE ###########################
###############################################################################
#                                                                             #
###############################################################################

if pycompat.is_py2:
    # This is to make pylint happy:
    # pylint: disable=undefined-variable
    from future_builtins import filter, map, zip
    import imp
    builtins.file = imp.load_source('_file', '/usr/lib/python3.6/__pycache__/_io.cpython-36.pyc')


# Generated at 2022-06-12 19:51:12.019756
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():

    '''
    if not DISABLED:
        if reload_module:

            reload_module(False)
        if 0:
            pytest.skip("This doesn't work right now; "
                        "it breaks test_Tracer.test_method_definition_inside_if")
        DISABLED = True
'''
    def _test_call(function_or_class):
        if inspect.isclass(function_or_class):
            return _test_call(function_or_class.__init__)
        else:
            return _test_call(function_or_class.__call__)
    globals()['_test_call'] = _test_call
    @snoop()
    def _test_call2():
        return 42
    globals()['_test_call2'] = _test_call2


# Generated at 2022-06-12 19:51:18.007657
# Unit test for method trace of class Tracer

# Generated at 2022-06-12 19:51:24.570162
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # __exit__(self, exc_type, exc_value, exc_traceback)
    assert_raises(NotImplementedError, Tracer().__exit__, None, None, None)


# Generated at 2022-06-12 19:51:33.625355
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f():
        g()
    def g():
        pass


# Generated at 2022-06-12 19:51:42.166926
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from . import variables
    from . import utils
    from . import pycompat
    from . import units
    filename_a, source_a = get_path_and_source_from_frame(
        inspect.currentframe()
    )
    filename_b, source_b = get_path_and_source_from_frame(
        inspect.currentframe().f_back
    )
    assert filename_a.endswith('tests/test_commands.py')
    assert filename_b.endswith('tests/test_commands.py')
    assert source_a[0].startswith('"""Unit test for')
    assert source_b[0].startswith('"""Unit test for')
    assert source_a[-1] == source_b[-1]

# Generated at 2022-06-12 19:51:44.082281
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    t = Tracer()
    t.write = lambda x: x


# Generated at 2022-06-12 19:51:53.033160
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from pysnooper import snoop
    global DISABLED
    DISABLED = False
    code = 'code'
    event = 'call'
    arg = 'arg'
    class Mock(object):
        def __init__(self, name=None):
            self.name = name
        def __enter__(self):
            pass
        def __exit__(self, exc_type, exc_value, exc_traceback):
            pass

    @snoop()
    def test(a,b):
        return a+b
    stack = [1,2]
    frame = Mock()
    frame.f_code = Mock(name='f_code')
    frame.f_lasti = Mock(name='f_lasti')
    frame_back = Mock()
    frame.f_back = frame_back
   

# Generated at 2022-06-12 19:51:57.909550
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    params = {
        'exc_type': 'NoneType',
        'exc_value': None,
        'exc_traceback': None
    }
    obj = Tracer(**params)
    assert(obj.__exit__(*params) == None)


# Generated at 2022-06-12 19:52:08.949732
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import os
    import sys
    import tempfile
    import unittest

    from . import utils

    class Tracer___call__Tests(unittest.TestCase):
        def test_it(self):
            f, f_path = tempfile.mkstemp()
            os.close(f)
            try:
                with open(f_path, 'w') as outfile:
                    try:
                        Tracer(outfile)(utils.decorated_function_with_locals)(1)
                    finally:
                        outfile.flush()
            finally:
                os.remove(f_path)
            with open(f_path) as infile:
                actual = infile.read()

# Generated at 2022-06-12 19:52:18.226868
# Unit test for constructor of class Tracer
def test_Tracer():
    import tempfile

    with tempfile.TemporaryFile(mode='w+') as f:
        def foo(): pass
        def bar(): pass
        def test_method(self): pass
        class TestClass(object):
            def test_method(self): pass

        t = Tracer(f)
        t(foo)()
        t(foo)(watch=('a', 'b'), watch_explode=('foo', 'bar'))
        t(lambda: None)()
        t(test_method)()
        t(TestClass())()
        t(TestClass).test_method()
        t(TestClass.test_method)()
        t(test_method)()
        t(TestClass)()
        t(bar)()
    f.seek(0)

# Generated at 2022-06-12 19:53:28.228841
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import sys
    import os
    import imp
    import unittest

    class TestGetPathAndSourceFromFrame(unittest.TestCase):
        def test_normal_file(self):
            def f():

                def g(x):
                    def h(y):
                        pass
            f()

            frame = sys._getframe(0)
            file_name, source = get_path_and_source_from_frame(frame)
            self.assertEqual(file_name, __file__)
            self.assertEqual(len(source), 11)
            self.assertEqual(source[0], 'def f():')

        def test_ipython_file(self):
            import IPython
            ipython_shell = IPython.get_ipython()


# Generated at 2022-06-12 19:53:35.467442
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from . import __file__ as this_file
    from . import __name__ as this_module_name
    def function():
        return function.__code__.co_firstlineno
    source = inspect.getsource(function).splitlines()
    assert get_path_and_source_from_frame(function.__code__.co_firstlineno)[1]


# Generated at 2022-06-12 19:53:39.165677
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # random seed is not set
    # inputs
    t = Tracer()
    # results
    # pysnooper.tracing.thread_global.depth = 0
    try:
        with t:
            pass
    except Exception as e:
        utils.printexception(e)
    else:
        assert False

# Generated at 2022-06-12 19:53:50.481799
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
	import pysnooper
	with pysnooper.snoop():
		pass

if __name__ == '__main__':
	test_Variable___init__()
	test_CommonVariable___init__()
	test_CommonVariable__get_value()
	test_Exploding___init__()
	test_Exploding__get_value()
	test_Variable__get_value()
	test_get_path_and_source_from_frame()
	test_get_write_function()
	test_get_local_reprs()
	test_trace()
	test_Tracer___init__()
	test_Tracer___call__()
	test_Tracer_write()
	test_Tracer___enter__()
	test_Tracer___exit__()

# Generated at 2022-06-12 19:54:00.701851
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import datetime
    import os
    import threading
    import sys
    import unittest
    import warnings
    import math

    class TestTracer_call_TestCase(unittest.TestCase):
        def test_decorator_func(self):
            import logging
            log_file_name = '_temp.log'
            try:
                os.remove(log_file_name)
            except:
                pass

            def my_function(a, b):
                return a + b

            my_tracer = Tracer(watch=('a',), output=log_file_name, normalize=False)
            my_tracer(my_function)
            result = my_function(1, 2)
            with open(log_file_name, 'r') as f:
                log_content = f.read

# Generated at 2022-06-12 19:54:08.216760
# Unit test for function get_write_function
def test_get_write_function():
    from . import utils
    from .utils import test
    # Testing output=None
    write = get_write_function(None, False)
    write(u'abc')
    # Testing output=<path>
    utils.oo(u'abc', write=get_write_function('tmp/abc.txt', False))
    test.assert_equal(u'abc', utils.o('tmp/abc.txt'))
    utils.oo(u'bcd', write=get_write_function('tmp/abc.txt', True))
    test.assert_equal(u'bcd', utils.o('tmp/abc.txt'))
    # Testing output=<callable>
    result = []
    def write(s):
        result.append(s)

# Generated at 2022-06-12 19:54:13.987559
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test():
        source_and_path = get_path_and_source_from_frame(sys._getframe())
        assert source_and_path[0].endswith('test_stack_viewer.py')
        assert source_and_path[1][0].startswith('def test_get_path_and_source_from_frame')
    test()
test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:54:21.328142
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import json

    def test_class():
        def test_method():
            pass
        return test_method
    with pysnooper.snoop() as snooper:
        tracer = snooper._snoopers.popitem()[1]
        tracer.target_codes.add(test_class.__code__)
        tracer.target_frames.add(test_class)
        stack = tracer.thread_local.__dict__.setdefault(
            'original_trace_functions', []
        )
        stack.append(sys.gettrace())
        tracer.start_times[test_class.__code__] = datetime_module.datetime.now()
        sys.settrace(tracer.trace)
        tracer.__exit__(None, None, None)


# Generated at 2022-06-12 19:54:29.230292
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import unittest

    class Test_Tracer___exit__(unittest.TestCase):
        def test_without_context_manager(self):
            tracer = Tracer()
            @tracer
            def foo():
                pass
            self.assertRaises(RuntimeError, foo)
            self.assertRaises(RuntimeError, foo)
            self.assertRaises(RuntimeError, foo)

        def test_with_context_manager(self):
            tracer = Tracer()
            @tracer
            def foo():
                pass
            with tracer:
                foo()
                foo()
                foo()


# Generated at 2022-06-12 19:54:29.790012
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    pass



# Generated at 2022-06-12 19:55:15.174841
# Unit test for constructor of class Tracer
def test_Tracer():
    output = StringIO()
    tracer = Tracer(output=output)
    assert tracer._write == output.write
    assert tracer.watch == []
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info is False
    assert tracer.custom_repr == ()
    assert tracer.max_variable_length == 100

    tracer2 = Tracer(watch='foo', depth=2, prefix='AAAA ',
                     thread_info=True, custom_repr=('foo', 'foo'),
                     max_variable_length=200)
    assert tracer2.watch == [CommonVariable('foo')]
    assert tracer2.depth == 2
    assert tracer2.prefix == 'AAAA '
    assert tracer2.thread_info is True

# Generated at 2022-06-12 19:55:25.773377
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    """Test for method test_Tracer_snoop on class Tracer"""
    import sys
    import io
    import threading
    import time
    import pdb
    import sys
    import pycompat
    import pysnooper
    import inspect
    import functools
    import datetime
    import itertools
    import traceback
    import types
    import dis
    import types
    import opcode
    from . import utils
    from . import check_case
    import pycompat
    import threading
    import inspect
    import functools
    import dis
    import sys
    import types
    import opcode
    TraceFunc = check_case.Tracer
    check_case.test_Tracer_snoop()
    # try: #

# Generated at 2022-06-12 19:55:29.698807
# Unit test for function get_write_function
def test_get_write_function():
    sink = utils.Sink()
    write = get_write_function(sink, False)
    assert write == sink.write
    write2 = get_write_function(sink.write, False)
    assert write == write2
    write = get_write_function(None, False)
    assert write != sink.write
    assert write
    assert callable(write)



# Generated at 2022-06-12 19:55:38.162398
# Unit test for function get_write_function
def test_get_write_function():
    def test_stderr(maybe_write_function, target_string):
        old_stderr = sys.stderr
        sys.stderr = target_string
        try:
            maybe_write_function('foo')
            if isinstance(maybe_write_function, FileWriter):
                maybe_write_function.close()
            assert isinstance(target_string, str)
            assert target_string == 'foo'
        finally:
            sys.stderr = old_stderr

    def test_output(maybe_write_function, target_object):
        maybe_write_function('foo')
        if isinstance(maybe_write_function, FileWriter):
            maybe_write_function.close()
        assert isinstance(target_object, str)
        assert 'foo' in target_object


# Generated at 2022-06-12 19:55:47.821545
# Unit test for constructor of class Tracer
def test_Tracer():

    def some_function():
        x = 5

    def some_other_function():
        y = 10

    def test_get_path_and_source_from_frame():
        assert get_path_and_source_from_frame(some_function.__code__)\
            == (__file__, inspect.getsourcelines(some_function)[0])
        assert get_path_and_source_from_frame(some_other_function.__code__)\
            == (__file__, inspect.getsourcelines(some_other_function)[0])

    def test_watch():
        def foo():
            x = 15

        def test_watch_as_string():
            with Tracer(watch='x'):
                foo()


# Generated at 2022-06-12 19:55:55.653697
# Unit test for function get_write_function
def test_get_write_function():
    func_called = []
    class Output:
        def write(self, s):
            func_called.append('func')
            assert s == 'wow'
    def other_func(s):
        func_called.append('other_func')
        assert s == 'wow again'
    class Path:
        def __fspath__(self):
            return '/tmp/wow-file'
    write = get_write_function(Output(), overwrite=False)
    write('wow')
    write = get_write_function(other_func, overwrite=False)
    write('wow again')
    write = get_write_function(Path(), overwrite=True)
    write('wow again')


