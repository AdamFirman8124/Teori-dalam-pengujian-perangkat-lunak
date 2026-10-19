

# Generated at 2022-06-12 19:46:42.410584
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    assert True



# Generated at 2022-06-12 19:46:54.044445
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    p = Tracer()

    p.thread_local.original_trace_functions = []
    p.depth = 1
    p.target_codes = set()
    p.target_frames = set()
    p.thread_info = False
    p.start_times = {}
    p.thread_info_padding = 0
    p.last_source_path = None
    p.max_variable_length = None

    class Frame():
        f_code = 'abc'
        f_lineno = 1
        f_lasti = 1

        def __init__(self):
            self.f_locals = {}
            self.f_globals = {}

    frame = Frame()

    event = 'call'
    p.trace(frame, event, None)
    return

    # Normalizer is not done
    p

# Generated at 2022-06-12 19:47:02.422854
# Unit test for constructor of class Tracer
def test_Tracer():
    @pysnooper.snoop()
    def add_integers(x, y):
        return x + y

    @pysnooper.snoop(watch=('x', 'y'))
    def add_integers(x, y):
        return x + y

    @pysnooper.snoop(watch_explode=('x', 'y'))
    def add_integers(x, y):
        return x + y

    @pysnooper.snoop(depth=2)
    def add_integers(x, y):
        return x + y

    @pysnooper.snoop(prefix='ZZZ ')
    def add_integers(x, y):
        return x + y


# Generated at 2022-06-12 19:47:03.236253
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Preconditions
    # Should be none exiting
    
    pass



# Generated at 2022-06-12 19:47:03.957618
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
   pass

# Generated at 2022-06-12 19:47:14.847491
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import inspect
    import functools
    import sys
    import threading
    import datetime
    import pysnooper
    import pycompat
    class Tracer:
        def __init__(self):
            self._write = None
            self.watch = None
            self.frame_to_local_reprs = {}
            self.start_times = {}
            self.depth = 1
            self.prefix = ""
            self.overwrite = False
            self.thread_info = False
            self.custom_repr = ()
            self.max_variable_length = 100
            self.normalize = False
            self.relative_time = False
        def __call__(self, function_or_class):
            if True:
                return function_or_class
            if True:
                return

# Generated at 2022-06-12 19:47:24.331993
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    import os
    import sys
    def f():
        return sys._getframe(0)
    file_name = f().f_code.co_filename
    dir_name = os.path.dirname(file_name)
    source = inspect.getsource(f).splitlines()
    assert get_path_and_source_from_frame(f()) == (file_name, source)
    # Test that it's cached
    source_and_path_cache.clear()
    assert get_path_and_source_from_frame(f()) == (file_name, source)
    # Test nonexistent source
    nonexistent_file_name = file_name + u'asdf'
    def nonexistent_function():
        return sys._getframe(0)

# Generated at 2022-06-12 19:47:25.621602
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Tracer.trace()  --> this method cannot be tested
    pass


# Generated at 2022-06-12 19:47:30.700042
# Unit test for constructor of class Tracer
def test_Tracer():
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        # pylint: disable=unused-variable
        @pysnooper.snoop()
        def foo():
            pass
    assert mock_stdout.getvalue() == u'foo\n'

###############################################################################
############################### Trace Decorator ###############################
###############################################################################

# pylint: disable=invalid-name
trace = Tracer()

###############################################################################
################################# run() #######################################
###############################################################################


# Generated at 2022-06-12 19:47:40.628584
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
	# Import mock objects and get methods
	# Original classes and functions
	from pysnooper.snoop import (
		Tracer,
		DISABLED,
		get_write_function,
		utils,
		inspect,
		functools,
		threading,
		pycompat,
		datetime as datetime_module,
		sys,
		BaseVariable,
		CommonVariable,
		Exploding
	)

	# Mock classes and functions
	get_write_function_mock = MagicMock(name='get_write_function')

	utils_ensure_tuple = MagicMock(name='utils_ensure_tuple')

	inspect_isclass = MagicMock(name='inspect_isclass')

# Generated at 2022-06-12 19:48:10.124681
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # Test with default args
    import tempfile
    with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as f:
        # capture output
        with utils.Capturing() as output:
            with Tracer(output=f):
                pass
        # Test output
        f.seek(0)
        expected = ["Source path:... {}".format(Tracer.__init__.__code__.co_filename)]
        assert f.read().splitlines() == expected
    # Test with a custom output
    with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as f:
        with utils.Capturing() as output:
            with Tracer(output=f, max_variable_length=None, normalize=True):
                pass
        f.seek(0)
        expected

# Generated at 2022-06-12 19:48:18.700292
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    with open('test_Tracer_trace.txt', 'w') as f:
        global_write = f.write
        global_write('=== test_Tracer_trace ===\n')
        global_write('\n')
        tracer = Tracer(watch=('foo', 'bar.x', 'baz.y[*]'), output=f,
                        prefix='@')
        tracer.write = global_write
        frame = inspect.currentframe()
        frame.f_lineno = frame.f_lasti = 1
        frame.f_code = frame.f_code = frame.f_locals['test_Tracer_trace'].__code__
        frame.f_locals = {'foo': 1, 'bar': {'x': 2}, 'baz': {'y': [3, 4]}}
       

# Generated at 2022-06-12 19:48:24.899616
# Unit test for function get_write_function
def test_get_write_function():
    assert get_write_function(None, False)('hello') == 'hello'
    assert get_write_function(sys.stdout, False)('hello') == 'hello'
    class Output(object):
        def write(self, s):
            return s
    assert get_write_function(Output(), False)('hello') == 'hello'
    with pycompat.temp_file() as temp_file:
        assert get_write_function(temp_file, False)('hello') == 'hello'
        with open(temp_file, 'rb') as f:
            assert f.read() == b'hello'
    with pycompat.temp_file() as temp_file:
        get_write_function(temp_file, True)('hello')
        with open(temp_file, 'rb') as f:
            assert f

# Generated at 2022-06-12 19:48:29.964468
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global DISABLED  # pylint:disable=global-statement
    DISABLED = True
    utils.trace = Tracer().trace
    def foo(*args, **kwargs):
        x = 1
        y = 2
        z = 3
        return x
    foo()


# Generated at 2022-06-12 19:48:38.290619
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    with pytest.raises(NotImplementedError) as info:
        pysnooper.snoop(output="/tmp/pyout.log0", thread_info=True).__exit__(None, None, None)
    assert str(info.value) == 'normalize is not supported with thread_info'

    with pytest.raises(AssertionError) as info:
        pysnooper.snoop(output="/tmp/pyout.log0", relative_time=True).__exit__(None, None, None)



# Generated at 2022-06-12 19:48:42.138130
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_function():
        pass
    assert get_path_and_source_from_frame(test_function.__code__.co_firstlineno)


_format_split_pattern = re.compile(r'(\{.+?\})')



# Generated at 2022-06-12 19:48:51.451290
# Unit test for constructor of class Tracer
def test_Tracer():
    # non-existing file overwriting, without any entries
    def test_overwrite():
        import os
        import os.path
        import os.path
        filename = 'test.txt'
        if os.path.exists(filename):
            raise Exception('Test file "'+filename+'" already exists!')
        @pysnooper.snoop(filename, overwrite=True)
        def empty_function():
            pass
        empty_function()
        # check if file is created
        if not os.path.exists(filename):
            raise Exception('"overwrite=True" does not have effect!')
        # check if file is empty
        file_handle = open(filename)
        if file_handle.read() != '':
            raise Exception('"overwrite=True" does not work!')
        # remove file
       

# Generated at 2022-06-12 19:48:58.544916
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import unittest
    @unittest.skip("function 'trace' will be tested")
    def testcase_1():
        import io
        import pdb
        import sys
        from pysnooper.pycompat import py2k
        from pysnooper.tracer import Tracer
        from pysnooper.utils import truncate, get_shortish_repr
        from pysnooper.variables import CommonVariable, Exploding
        from pysnooper.wrappers import get_path_and_source_from_frame

        def test_func_no_var(param_1):
            print('Just a print statment')


        def test_func_start_with_var(param_1):
            var_1 = param_1
            print('Just a print statement')
        

# Generated at 2022-06-12 19:49:07.908378
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    from pysnooper.utils import get_shortish_repr, truncate
    from pysnooper.variable import CommonVariable, BaseVariable
    from pysnooper.custom_repr import custom_repr
    max_variable_length = 100
    normalize = False
    relative_time = False
    # __init__ of class Tracer
    output = None
    watch = (('watch_var',),)
    watch_explode = ()
    depth = 1
    prefix = ''
    overwrite = False
    thread_info = False
    custom_repr = ('custom_repr',)
    self_ = Tracer(output, watch, watch_explode, depth, prefix,
                   overwrite, thread_info, custom_repr,
                   max_variable_length, normalize, relative_time)

# Generated at 2022-06-12 19:49:18.724433
# Unit test for constructor of class Tracer
def test_Tracer():
    # Arrange
    class DummyFile:
        output = ''
        def write(self,s):
            self.output += s

    dummy_output = DummyFile()
    watch = 'a'
    depth = 2
    prefix = 'ZZZ '
    overwrite = False
    thread_info = True
    custom_repr = (('custom_repr', lambda x:x))
    max_variable_length = 100
    normalize = False
    relative_time = True

    tracer = Tracer(dummy_output, watch, depth=depth,
                 prefix=prefix, overwrite=overwrite, thread_info=thread_info,
                 custom_repr=custom_repr, max_variable_length=max_variable_length,
                 normalize=normalize, relative_time=relative_time)

    # Act
   

# Generated at 2022-06-12 19:49:47.142142
# Unit test for function get_write_function
def test_get_write_function():
    class MyWritableStream(object):
        def write(self, s):
            pass

    from .testing.assertions import assert_equal

    assert_equal(get_write_function(sys.stderr, overwrite=False),
                 get_write_function(output=sys.stderr, overwrite=False))
    assert_equal(get_write_function(sys.stderr, overwrite=False),
                 get_write_function(output=None, overwrite=False))

    assert_equal(get_write_function(MyWritableStream(), overwrite=False),
                 get_write_function(output=MyWritableStream(), overwrite=False))

    assert_equal(get_write_function(None, overwrite=False),
                 get_write_function(output=None, overwrite=False))

# Generated at 2022-06-12 19:49:52.306479
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    """
    This is a unit test for the method trace of class Tracer
    """
    print("*** Beginning test_Tracer_trace ***")
    a = Tracer(watch=['a'])
    a.trace(None, 'call', None)
    # If this line is executed, the test has passed
    print("*** test_Tracer_trace has passed ***")


# Generated at 2022-06-12 19:49:59.351229
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from pysnooper.tracer_callables import Tracer

    def foo():
        pass
    def foo_generator():
        yield 1
    def foo_async():
        pass

    async def foo_async_gen():
        yield 1

    assert Tracer().__call__(foo) != foo
    assert Tracer().__call__(foo_generator)() == 1
    if pycompat.isasyncgenfunction(foo_async_gen):
        assert inspect.iscoroutine(Tracer().__call__(foo_async_gen)())
    #assert inspect.iscoroutine(Tracer().__call__(foo_async)()) # FIXME: Fails with AttributeError: 'NoneType' object has no attribute 'bind'

# Generated at 2022-06-12 19:50:02.079193
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    with pytest.raises(NotImplementedError):
        tracer = Tracer()
        tracer.trace(
            frame=None,
            event=None,
            arg=None
        )



# Generated at 2022-06-12 19:50:08.761759
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    snoop = Tracer()
    # Set depth=1, overwrite=False, and thread_info=False
    # The above three info will be used to initialize Tracer class
    # See __init__(self, output=None, watch=(), watch_explode=(), depth=1, prefix='', overwrite=False, thread_info=False)
    # in pysnooper/_snoop.py
    assert snoop.depth == 1
    assert snoop.overwrite == False
    assert snoop.thread_info == False

# Generated at 2022-06-12 19:50:14.392039
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def get_path_and_source(filename):
        def function():
            pass

        frame = function.__code__.co_filename = filename
        return get_path_and_source_from_frame(frame)

    (filename1, source1) = get_path_and_source('foo')
    (filename2, source2) = get_path_and_source('/foo')
    assert isinstance(source1[0], pycompat.string_types)
    assert filename1 == filename2
    assert source1 == source2

    (filename1, source1) = get_path_and_source('<ipython-input-1-4dde1c3d2087>')

# Generated at 2022-06-12 19:50:16.182612
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer()
    tracer.write = MagicMock()
    tracer.__exit__(None, None, None)

# Generated at 2022-06-12 19:50:24.366115
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import unittest
    import pysnooper

    class TestTracerTrace(unittest.TestCase):
        def setUp(self):
            self.tracer = pysnooper.snoop()

        def test_is_internal_frame(self):
            import inspect
            import pysnooper
            calling_frame = inspect.currentframe().f_back
            self.assertFalse(self.tracer._is_internal_frame(calling_frame))
            self.assertTrue(self.tracer._is_internal_frame(pysnooper.Tracer.__enter__))

        def test_depth_first(self):
            def foo():
                with self.tracer:
                    return

            def bar():
                foo()

            def baz():
                bar()

            baz()


# Generated at 2022-06-12 19:50:34.305445
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    source_lines = ['a = 5', 'b = 7']
    source = '\n'.join(source_lines)
    module_name = 'test_get_path_and_source_from_frame'

    import types
    loader = types.ModuleType(module_name).__loader__
    def fake_get_source(module_name):
        assert module_name == 'test_get_path_and_source_from_frame'
        return source
    loader.get_source = fake_get_source
    del types

    result = get_path_and_source_from_frame(sys._getframe(0))

    assert result[1] == source_lines
    assert result[0] == '<ipython-input-1->'

_frame_cache = {}


# Generated at 2022-06-12 19:50:43.193043
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from pysnooper.tracing import Tracer
    import tempfile
    import random
    from pysnooper.utils import get_path_and_source_from_frame
    from pysnooper import snoop

    ### Sample program for testing:
    #                              #
    @snoop
    def myfunction(a, b):
        c = a + b
        d = a * b + c
        c = myfunction(c, d)
        return c

    #                              #
    ### Finished sample program. ###

    ### Executing the program:
    myfunction(1, 2)

    ### Finished executing the program.

    ### Unit test:
    #
    # We call pysnooper to generate the code. We then check the contents of
    # the file that it writes to, to make sure everything's in order.

# Generated at 2022-06-12 19:51:11.043230
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    path = utils.get_temp_file_path()
    LENGTH = 1000
    try:
        with open(path, 'w') as output_file:
            output_file.write('a' * LENGTH)
        assert os.path.getsize(path) == LENGTH
        FileWriter(path, overwrite=False).write('b' * LENGTH)
        assert os.path.getsize(path) == LENGTH * 2
        FileWriter(path, overwrite=True).write('c' * LENGTH)
        assert os.path.getsize(path) == LENGTH
    finally:
        if os.path.exists(path):
            os.remove(path)



# Generated at 2022-06-12 19:51:17.864743
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    from . import testing_tools
    expected_result = 'abcd'

    testing_tools.write_and_read(FileWriter('c:\\', False), expected_result,
                                 'w')
    testing_tools.write_and_read(FileWriter('c:\\', False), expected_result,
                                 'a')
    testing_tools.write_and_read(FileWriter('c:\\', False), expected_result,
                                 'a+')
    testing_tools.write_and_read(FileWriter('c:\\', True), expected_result,
                                 'w')
    testing_tools.write_and_read(FileWriter('c:\\', True), expected_result,
                                 'r+')



# Generated at 2022-06-12 19:51:21.764244
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import sys, threading
    sys._current_frames = threading._active.copy
    def test_target():
        pass
    kwargs = {
        'output': None,
        'watch': [],
        'watch_explode': [],
        'depth': 1,
        'prefix': '',
        'overwrite': False,
        'thread_info': False,
        'custom_repr': (),
        'max_variable_length': 100,
        'normalize': False,
        'relative_time': False,
    }
    t = Tracer(**kwargs)
    assert t.__call__(test_target) is test_target

# Generated at 2022-06-12 19:51:27.664584
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import unittest
    class TestCase(unittest.TestCase):
        def test_1(self):
            return NotImplemented

    def run_tests():
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
        unittest.TextTestRunner(verbosity=2).run(suite)

    with pysnooper.snoop():
        run_tests()



# Generated at 2022-06-12 19:51:37.651526
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import io
    import sys
    file = io.StringIO()
    sys.stderr = file
    print("Called Tracer")
    # __enter__(self: pysnooper.utils.Tracer) -> None
    # line 108
    print("Called Tracer")
    # line 115
    print("Called Tracer")
    # line 122
    print("Called Tracer")
    # line 130
    print("Called Tracer")
    # line 140
    print("Called Tracer")
    # line 144
    print("Called Tracer")
    # line 147
    print("Called Tracer")
    # line 152
    print("Called Tracer")
    # line 157
    print("Called Tracer")
    # line 168
    print("Called Tracer")
    # line

# Generated at 2022-06-12 19:51:41.553304
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import pytest
    from .utils import FakeFile, get_write_function, get_path_and_source_from_frame
    import pycompat, inspect, dis, functools
    t1 = Tracer(output='trace1.txt')
    thread_global.depth, t1.depth, t1.prefix, t1.thread_info_padding, t1.last_source_path = 0, 1, '', 0, None
    with t1:
        pass
    thread_global.depth, t1.depth, t1.prefix, t1.thread_info_padding, t1.last_source_path = 0, 1, '', 0, None
    with t1:
        pass


# Generated at 2022-06-12 19:51:51.904438
# Unit test for function get_write_function
def test_get_write_function():
    try:
        get_write_function(None, True)
    except Exception:
        pass
    else:
        raise Exception
    try:
        get_write_function(None, False)
    except Exception:
        raise Exception
    try:
        get_write_function('/path', False)
    except Exception:
        raise Exception
    try:
        get_write_function('/path', True)
    except Exception:
        raise Exception
    try:
        get_write_function('not a path')
    except Exception:
        raise Exception
    try:
        get_write_function('not a path')
    except Exception:
        raise Exception
    try:
        get_write_function(lambda s: None)
    except Exception:
        raise Exception

# Generated at 2022-06-12 19:51:59.956616
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import doctest
    import pysnooper
    globs = pysnooper.__dict__.copy()
    globs.update({'datetime_': datetime_module, 'pysnooper': pysnooper})
    globs, _, _ = doctest.testmod(pysnooper, globs=globs)
    return globs
globs = test_Tracer___call__()


### Writing the snoop output to a file: ######################################
#                                                                            #

# Generated at 2022-06-12 19:52:10.388300
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import pkgutil
    import tempfile
    import sys


    def get_test_source():
        return ['test_name = __name__', 'if test_name == "__main__":']


    def get_test_code():
        return compile(''.join(get_test_source()), 'test_source', 'exec')


    def get_test_frame():
        code = get_test_code()
        globs = {}
        return sys._getframe(1)


    def test_get_path_and_source_from_frame():
        test_frame = get_test_frame()
        file_name, source = get_path_and_source_from_frame(test_frame)
        assert source == get_test_source()


# Generated at 2022-06-12 19:52:19.649069
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    simple_global = 'simple'
    complex_global = [(x**2, x**3) for x in range(5)]
    complex_global[2] = 'Not so complex anymore'
    global_that_changes = 'A'
    def function(a, b, c, d='dd', e=None):
        local_a = a
        local_b = b
        local_b += 5
        local_c = c
        local_c += 5
        local_d = d
        local_d += 5
        local_e = e
        local_e += 5
        global_that_changes = 'B'

    wrapped_function = Tracer(overwrite=True)(function)
    # Unit test for method __init__ of class Tracer


# Generated at 2022-06-12 19:53:02.783410
# Unit test for method trace of class Tracer
def test_Tracer_trace():
  m = Tracer()
  m.trace(0, 0, 0)



# Generated at 2022-06-12 19:53:12.268972
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    __file__ = sys.modules[test_get_path_and_source_from_frame.__module__].__file__
    # `__file__` is used in the function we're testing, to find the source code
    # of the function. We need to make it point to the .py file -- not the .pyc
    if __file__[-1] in 'oc':
        __file__ = __file__[:-1]
    exec('def inner_test_function(): pass', dict(sys=sys))
    frame = sys.modules[test_get_path_and_source_from_frame.__module__].inner_test_function.__code__.co_firstlineno
    path, source = get_path_and_source_from_frame(frame)
    assert path == __file__

# Generated at 2022-06-12 19:53:18.660854
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # Make sure we get the source from the loader
    from io import StringIO

    frame = utils.get_frame(lambda: None)
    module_name = frame.f_globals['__name__']

    old_loader = frame.f_globals['__loader__']
    source = 'foo = 1'
    source_bytes = source.encode('ascii')
    try:
        frame.f_globals['__loader__'] = _FlakyLoader()
        frame.f_globals['__loader__'].source[module_name] = source_bytes
        path, lineno = get_path_and_source_from_frame(frame)
    finally:
        frame.f_globals['__loader__'] = old_loader
    assert path == frame.f_code.co_filename

# Generated at 2022-06-12 19:53:29.668707
# Unit test for function get_write_function
def test_get_write_function():
    import tempfile
    from .testing.common import assert_equal
    temp_file_path = tempfile.NamedTemporaryFile()
    write_to_temp_file = get_write_function(temp_file_path, True)
    write_to_temp_file('hello world')
    temp_file_path.flush()
    temp_file_path.seek(0)
    assert_equal(temp_file_path.read(), b'hello world')
    write_to_temp_file = get_write_function(temp_file_path.fileno(), True)
    write_to_temp_file('hello world')
    temp_file_path.flush()
    temp_file_path.seek(0)
    assert_equal(temp_file_path.read(), b'hello worldhello world')



# Generated at 2022-06-12 19:53:39.734795
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import textwrap
    from io import StringIO
    import sys

    source = textwrap.dedent('''\
        def function(foo):
            bar = 1
            return bar
        ''')

    code = compile(source, 'test_Tracer_trace', 'exec')
    frame = FrameType(code, {}, None, 'test_Tracer_trace', 1, None)
    output = StringIO()

    tracer = Tracer(output=output, depth=1)

    frame.f_code = code
    frame.f_lineno = 3
    tracer.trace(frame, 'call', None)

    frame.f_lineno = 4
    tracer.trace(frame, 'line', None)
    assert output.getvalue() == '    test_Tracer_trace:3 call\n'

    sys

# Generated at 2022-06-12 19:53:44.398528
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def foo():
        x = 10
        y = 20
        z = x * y
        local_reprs = get_local_reprs(frame=foo.__code__.__code__.co_varnames)
    assert len(local_reprs) == 3



# Generated at 2022-06-12 19:53:53.486933
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    """
    A test for method __enter__ in class Tracer
    """
    # Create a Tracer object
    t = Tracer(output="/TestTracer/test_Tracer__init__.log")
    # Test __enter__
    with t:
        print("test")
    # Read the output
    with open("/TestTracer/test_Tracer__init__.log", "r") as f:
        # It should include the line "test"
        # The order of the lines are not specified, so the test only check if
        # "test" is in it.
        assert("test" in f.read())


# Generated at 2022-06-12 19:54:03.025855
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import pysnooper
    class A(object):
        def bar(self):
            return 'foo'
    class B(A):
        def bar(self):
            return 'bar'
    obj = B()
    trace = pysnooper.Tracer().trace
    sys._getframe().f_code.co_filename = 'test_main.py'
    trace(sys._getframe(), 'call', None)
    trace(sys._getframe(), 'return', obj.bar())
    trace(sys._getframe(), 'call', None)
    trace(sys._getframe(), 'return', obj.bar())

# Generated at 2022-06-12 19:54:05.736526
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    utils.assert_equal(get_path_and_source_from_frame(sys._getframe()),
                       (__file__, open(__file__, 'r', encoding='utf-8').read().split('\n')))



# Generated at 2022-06-12 19:54:10.070963
# Unit test for function get_local_reprs
def test_get_local_reprs():
    from . import variables

    __file__
    __name__
    __package__
    __doc__
    locals()

    def foo(bar, baz=3):
        x = 1
        def qux():
            y = 2
            locals()
            return locals()
        locals()
        return qux()

    foo(2)

