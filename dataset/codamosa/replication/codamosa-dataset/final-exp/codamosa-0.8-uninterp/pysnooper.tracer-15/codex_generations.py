

# Generated at 2022-06-12 19:46:35.720756
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .utils import working_directory_guard
    from . import debug_me_raw

    with working_directory_guard():
        debug_me_raw.test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:46:44.377799
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import sys
    import os
    import pytest
    import tempfile
    import pysnooper
    def test_basic_usage():
        global count, a, b
        def f(a, b):
            count += 1
        #
        count = 0
        f = pysnooper.snoop(f)
        f(1, 2)
        assert count == 1
    def test_method_usage():
        global count, a, b
        class Foo:
            def __init__(self):
                pass
            def f(self, a, b):
                count += 1
        #
        count = 0
        foo = Foo()
        foo.f = pysnooper.snoop(foo.f)
        foo.f(1, 2)
        assert count == 1

# Generated at 2022-06-12 19:46:50.140462
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def foo(x, y, z):
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        return a, b, c, d, e
    frame = inspect.currentframe()
    execution_frame = inspect.getinnerframes(frame)[1][0]
    test_frame = inspect.getinnerframes(frame)[2][0] # The frame of this test
    locals_repr = get_local_reprs(test_frame)
    assert locals_repr['x'] == "foo"
    assert locals_repr['y'] == "foo"
    assert locals_repr['z'] == "foo"

# Generated at 2022-06-12 19:47:00.439337
# Unit test for constructor of class Tracer
def test_Tracer():
    def f():
        pass
    def g():
        pass
    write = get_write_function(output=None, overwrite=False)
    assert Tracer(output=None, watch=(), watch_explode=(), depth=1,
                 prefix='', overwrite=False, thread_info=False, custom_repr=(),
                 max_variable_length=100, normalize=False, relative_time=False)._write == write
    assert Tracer(output=None, watch=(), watch_explode=(), depth=2,
                 prefix='', overwrite=False, thread_info=False, custom_repr=(),
                 max_variable_length=200, normalize=True, relative_time=False)._write == write

# Generated at 2022-06-12 19:47:11.401129
# Unit test for function get_write_function
def test_get_write_function():
    class FakeFile(object):
        def __init__(self):
            self.writes = []
        def write(self, s):
            self.writes.append(s)
    def save_or_write_result(output, expected_text):
        write = get_write_function(output, overwrite=False)
        write(expected_text)
        return output
    expected_text = 'meow'
    output = save_or_write_result(None, expected_text)
    assert sys.stderr.buffer.writes == [utils.shitcode(expected_text)]
    saved_stderr = sys.stderr.buffer
    output = save_or_write_result(FakeFile(), expected_text)
    assert output.writes == [expected_text]
    output = save_or_write_result

# Generated at 2022-06-12 19:47:19.821230
# Unit test for constructor of class Tracer
def test_Tracer():
    # All data used in the test
    watch = 'bar'
    watch_explode = 'foo'
    depth = 3
    output = io.StringIO()
    overwrite = False
    prefix = "[Test] "
    thread_info = True
    custom_repr = (('custom', lambda x: 'custom_repr_func'),
                   (re.compile('custom_regex'), lambda x: 'custom_regex_repr'))
    max_variable_length = 60
    normalize = False
    relative_time = True

    # Normal constructor

# Generated at 2022-06-12 19:47:28.428669
# Unit test for method trace of class Tracer
def test_Tracer_trace():
  module_name = 'snoop'
  # We do not use module_name as object id, because other tests might use it
  # as well, so Tracer will be confused.
  object_id = module_name + '_Tracer_trace'
  import_string = module_name + '.snoop'

  source = inspect.getsource(Tracer.trace)
  source = utils.remove_initial_indent(source)
  source = utils.remove_trailing_whitespace(source)
  source = utils.remove_trailing_empty_lines(source)
  source = utils.remove_blank_lines_in_the_middle(source)

# Generated at 2022-06-12 19:47:31.779882
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # This is meant to be run from within a worker thread.
    def f():
        x = 1
        inspect.currentframe()
        def g():
            x = 2
            inspect.currentframe()
    f()



# Generated at 2022-06-12 19:47:35.385087
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_function():
        assert get_path_and_source_from_frame(inspect.currentframe()) == \
               (__file__, inspect.getsource(test_get_path_and_source_from_frame))
    test_function()



# Generated at 2022-06-12 19:47:46.214341
# Unit test for method trace of class Tracer

# Generated at 2022-06-12 19:48:04.317642
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    tracer = Tracer()
    class Collection:
        def __init__(self):
            self.x = 'x'
    tracer.watch = Collection()
    def outer():
        def inner():
            tracer.watch.x = 'y'
        inner()
    sys.settrace(tracer.trace)
    outer()



# Generated at 2022-06-12 19:48:15.055317
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # NOTE: This test is not run by `make test` as it requires pysnooper as
    # a dependency
    import pysnooper
    import StringIO
    import sys

    def get_output(code, **kwargs):
        output = StringIO.StringIO()
        sys.stdout = output
        snoop = pysnooper.snoop(output=output, **kwargs)
        with snoop:
            eval(code, {})
        sys.stdout = sys.__stdout__
        return output.getvalue()

    assert "Source path:..." in get_output(
        "a = 1\n"
        "b = 2\n",
        watch=('a', 'b')
    )

# Generated at 2022-06-12 19:48:21.276884
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from pysnooper.tracer import Tracer
    import sys
    import inspect
    import pycompat
    import functools
    import threading
    import __main__
    import datetime
    import itertools
    import opcode
    import traceback
    DISABLED = False
    class Utils:
        def ensure_tuple(self, thing):
            if not isinstance(thing, pycompat.collections_abc.Iterable):
                return (thing,)
            return thing
        def truncate(self, s, max_length):
            if len(s) > max_length:
                s = s[:max_length-3] + '...'
            return s

# Generated at 2022-06-12 19:48:21.806280
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    return

# Generated at 2022-06-12 19:48:23.127457
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global DISABLED
    DISABLED = False
    with Tracer(output=None):
        1 + 1


# Generated at 2022-06-12 19:48:36.318825
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    get_write_function = Mock()
    inspect = Mock()
    utils = Mock()
    pysnooper = Mock()
    threading = Mock()
    datetime_module = Mock()
    pycompat = Mock()

    class TestTracer:
        def __init__(self, output=None, watch=(), watch_explode=(), depth=1, prefix='', overwrite=False, thread_info=False, custom_repr=(), max_variable_length=100, normalize=False, relative_time=False):
            self.watch = watch
            self.depth = depth
            self.prefix = prefix
            self.overwrite = overwrite
            self.thread_info = thread_info
            self.custom_repr = custom_repr
            self.max_variable_length = max_variable_length
            self.normal

# Generated at 2022-06-12 19:48:39.644373
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    f = lambda: None
    a = get_path_and_source_from_frame(inspect.currentframe())
    assert a == (f.__code__.co_filename, inspect.getsourcelines(f)[0])



# Generated at 2022-06-12 19:48:49.605015
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def use_get_path_and_source_from_frame():
        return get_path_and_source_from_frame(inspect.currentframe())
    current_file_name = inspect.getfile(lambda: None)
    result = use_get_path_and_source_from_frame()
    assert result[0] == current_file_name
    assert result[1][-1].startswith('def test_get_path_and_source_from_frame():')
    _ = globals()
    result = use_get_path_and_source_from_frame()
    assert result[0] == current_file_name
    assert result[1][0].startswith('def test_get_path_and_source_from_frame():')
    result = use_get_path_and_source_from_frame

# Generated at 2022-06-12 19:48:50.798776
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    assert True # TODO: implement your test here


# Generated at 2022-06-12 19:48:53.958597
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    tracer = Tracer()

    @tracer
    def foo():
        pass

    assert foo.__name__ == 'foo'
    assert foo.__doc__ == 'test_Tracer___call__.<locals>.foo'



# Generated at 2022-06-12 19:49:10.021968
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Create VariableVariable
    VariableVariable = CommonVariable
    VariableVariable = CommonVariable
    # Create CommonVariable
    CommonVariable = CommonVariable
    CommonVariable = CommonVariable
    # Create Watch
    Watch = CommonVariable
    Watch = CommonVariable
    # Create Exploding
    Exploding = Exploding
    Exploding = Exploding
    # Create BaseVariable
    BaseVariable = BaseVariable
    BaseVariable = BaseVariable
    # Create Frame
    Frame = Frame
    Frame = Frame
    # Create Thread
    Thread = Thread
    Thread = Thread
    # Create Traceback
    Traceback = Traceback
    Traceback = Traceback
    # Create Event
    Event = Event
    Event = Event
    # Create Argument
    Argument = Argument
    Argument = Argument
    # Create Exception
    Exception = Exception
    Exception = Exception
    # Create DatetimeModule


# Generated at 2022-06-12 19:49:10.926199
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass


# Generated at 2022-06-12 19:49:13.233196
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    @pysnooper.snoop()
    def func_1():
        return 2
    with pysnooper.snoop():
        func_1()

# Generated at 2022-06-12 19:49:26.597058
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import re
    
    #
    # Call Control
    #
    
    def return_args(*args, **kwargs):
        return args, kwargs
    
    def return_None():
        return
    
    #
    # Asserts
    #
    
    def _make_timestamp_regex(prefix):
        return re.compile(
            "{prefix}[0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}} [0-9]{{2}}:[0-9]{{2}}:[0-9]{{2}}\\.[0-9]{{6}} ".format(prefix=prefix)
        )
    

# Generated at 2022-06-12 19:49:34.364063
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import os
    import inspect
    import pycompat

    import datetime_module
    from datetime_module import datetime_module
    import pysnooper
    from pysnooper import get_path_and_source_from_frame
    from pysnooper import pycompat
    from pysnooper.pycompat import *

# Generated at 2022-06-12 19:49:45.209754
# Unit test for function get_write_function
def test_get_write_function():
    # import pytest
    # import six
    with pycompat.open(r'C:\Users\Ram\Desktop\test.txt', 'w') as f:
        def test_writing_to_file(output, overwrite):
            write = get_write_function(output, overwrite)
            write('r')
            write('r')

        test_writing_to_file(f, False)
        test_writing_to_file(f, True)
        with pytest.raises(Exception):
            test_writing_to_file(f, True)

        class TestWritableStream(object):
            def write(self, s):
                assert s == u'rr'
            def __del__(self):
                pass
        test_writable_stream = TestWritableStream()

# Generated at 2022-06-12 19:49:47.264281
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pytest
    with pytest.raises(ImportError):
        import builtins

# Generated at 2022-06-12 19:49:50.950358
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    '''
    Unit test for the function `get_path_and_source_from_frame`.
    '''
    def f():
        return get_path_and_source_from_frame(inspect.currentframe())
    assert f()

# Generated at 2022-06-12 19:49:58.696106
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # Fixture:
    tracer = Tracer()
    targets = [
        (int, "foo = 42"),
        ("def foo(): return 42", "foo()"),
    ]
    for target, expression in targets:
        if isinstance(target, str):
            # The target is a string containing a function definition, which we
            # must transform into a function.
            import ast
            function_definition = ast.parse(target).body[0]
            function_name = function_definition.name
            locals_ = locals()
            exec(target, globals(), locals_)
            target = locals_[function_name]

# Generated at 2022-06-12 19:50:08.180314
# Unit test for function get_local_reprs
def test_get_local_reprs():
    x = 10
    y = 20
    z = 30
    a = {'x': x, 'y': y, 'z': z}
    frame = inspect.currentframe().f_back

    assert get_local_reprs(frame, normalize=True) == {
        'a': '{...}',
        'x': '10',
        'y': '20',
        'z': '30',
    }
    assert get_local_reprs(frame, normalize=False) == {
        'a': ('{\'z\': 30, \'y\': 20, \'x\': 10}'),
        'x': '10',
        'y': '20',
        'z': '30',
    }

# Generated at 2022-06-12 19:50:27.001331
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    frame = sys._getframe()
    if frame.f_globals['__name__'] == '__main__':
        frame = inspect.currentframe()
    path, source = get_path_and_source_from_frame(frame)

    assert path == inspect.getsourcefile(test_get_path_and_source_from_frame)
    assert source == inspect.getsourcelines(test_get_path_and_source_from_frame)[0]
test_get_path_and_source_from_frame()
del test_get_path_and_source_from_frame


# Generated at 2022-06-12 19:50:33.452278
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import unittest
    class test_Tracer___call__(unittest.TestCase):
        def test_Tracer___call__(self):
            # Arrange
            def function_or_class():
                pass

            # Act and Assert
            with self.assertRaises(NotImplementedError):
                sut = Tracer()
                sut(function_or_class)

    unittest.main(module=__name__, exit=False, verbosity=2)

# Generated at 2022-06-12 19:50:37.813859
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def frame_of(f):
        return f.__code__.co_firstlineno, f.__code__.co_filename

    def source_of(f):
        return get_path_and_source_from_frame(f)[1]

    def assert_source(f, expected_source):
        actual_source = source_of(f)
        assert actual_source == expected_source, \
               '{0!r} != {1!r}'.format(actual_source, expected_source)

    def some_function():
        """Line 1
        Line 2

        Line 4

        """
        pass

    def check(f, expected_source):
        frame = frame_of(f)
        assert_source(f, expected_source)
        del source_and_path_cache[frame]

    bad_enc

# Generated at 2022-06-12 19:50:41.057521
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    snooper = pysnooper.Snooper(watch=('value',))

    def function():
        value = 42
        # line function                                        
        return value

    function = snooper(function)

    function()

# END

# Generated at 2022-06-12 19:50:47.897235
# Unit test for function get_write_function
def test_get_write_function():
    from .tests import test_utils

    s = 'abc'
    output = test_utils.StdoutMock()
    write = get_write_function(output, False)
    write(s)
    assert output.getvalue() == s

    output = test_utils.StdoutMock()
    write = get_write_function(output, True)
    write(s)
    assert output.getvalue() == s

    write = get_write_function(None, False)
    write(s)

    s_filename = 'abc.txt'
    write = get_write_function(s_filename, False)
    write(s)
    with open(s_filename, 'r') as f:
        s_output = f.read()
    assert s_output == s
    os.remove(s_filename)

# Generated at 2022-06-12 19:50:52.158386
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    global watch, cnt
    cnt = 0
    @pysnooper.snoop()
    def f():
        global cnt
        cnt += 1
        return None
    with pytest.raises(TypeError):
        f()
    assert cnt == 1


# Generated at 2022-06-12 19:51:00.005190
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # __exit__(self, exc_type, exc_value, exc_traceback)
    # pytest: disable=no-member
    test_case_1_expected_output = ["Source path:... /Users/paulnguyen/Documents/GitHub/pysnooper/pysnooper/test_cases/test_cases_2.py", "19:02:51.986400 returning f()", 'Return value:.. None']
    test_case_1_output = []
    def test_case_1(self, exc_type, exc_value, exc_traceback):
        def get_output(s):
            test_case_1_output.append(s)
        s = pysnooper.Snooper(get_output, depth=5)
        s.__enter__()
        f()


# Generated at 2022-06-12 19:51:11.004575
# Unit test for method trace of class Tracer
def test_Tracer_trace():
	# If a call ends due to an exception, we still get a 'return' event
	# with arg = None. This seems to be the only way to tell the difference
	# https://stackoverflow.com/a/12800909/2482744
	def ended_by_exception(event, arg):
		event == 'return' and arg is None

	# If a function decorator is found, skip lines until an actual
	# function definition is found.

# Generated at 2022-06-12 19:51:18.230677
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    filename = 'test.py'
    try:
        os.remove(filename)
    except:
        pass
    with open(filename, 'w') as f:
        f.write(
            '''def myfunc(a, b, c=5, *args, **kwargs):
    if a > 3:
        b += 1
    elif a < 7:
        b -= 2
    return b'''
        )

# Generated at 2022-06-12 19:51:27.518663
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    for _ in range(100):
        with Tracer(overwrite=False, max_variable_length=100) as tracer:
            pass
        assert tracer.frame_to_local_reprs == {}
        assert tracer.start_times == {}
        assert not tracer.target_codes
        assert not tracer.target_frames
        assert not tracer.thread_local.original_trace_functions
        assert tracer.thread_info_padding == 0


# Generated at 2022-06-12 19:51:59.651015
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)


# Generated at 2022-06-12 19:52:10.189092
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import io
    import random

    def random_string():
        return ''.join((random.choice(('qwertyuiop', 'asdfghjkl', 'zxcvbnm'))
                        for _ in range(10)))

    def random_python_code(n):
        return '\n'.join((random_string() + (' = 3\n' * random.randint(1, 5)))
                         for _ in range(n))

    def get_source(code):
        frame = sys._getframe()
        frame.f_globals['__loader__'] = None
        old_source_paths = list(sys.path)

# Generated at 2022-06-12 19:52:14.163682
# Unit test for function get_write_function
def test_get_write_function():
    # with open('test_file.txt', 'w') as f:
        # pass
    print(get_write_function(open('test_file.txt', 'w'), False))
    # print(get_write_function(None, False))
    # print(get_write_function(open('test_file.txt', 'w'), True))



# Generated at 2022-06-12 19:52:16.926289
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import os
    import doctest
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    doctest.testmod()



# Generated at 2022-06-12 19:52:24.626730
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def test_Tracer___call__1():
        import unittest
        
        from pysnooper.tracing import Tracer

        class TestTracer(unittest.TestCase):
            def test_tracer_object(self):
                for arg in ('foo', ('foo', 'bar'), 'foo', ('foo', 'bar')):
                    g = Tracer(*arg)
                    for arg in ('foo', ('foo', 'bar'), 'foo', ('foo', 'bar')):
                        f = g(*arg)
        
                        self.assertTrue(callable(f))
        
                        def test_foo():
                            a = 1
                        setattr(self, 'test_foo', test_foo)
        
                        self.assertEqual(self.test_foo(), None)
        

# Generated at 2022-06-12 19:52:33.930839
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pysnooper

    # Test invalid variable types
    tracer = pysnooper.Tracer()
    (exc_type, exc_value, exc_traceback) = (None, None, None)
    tracer.__exit__(exc_type, exc_value, exc_traceback)

    # Test invalid variable types
    tracer = pysnooper.Tracer()
    (exc_type, exc_value, exc_traceback) = (None, None, None)
    tracer.__exit__(exc_type, exc_value, exc_traceback)

    # Test invalid variable types
    tracer = pysnooper.Tracer()
    (exc_type, exc_value, exc_traceback) = ('string', None, None)

# Generated at 2022-06-12 19:52:44.704578
# Unit test for method trace of class Tracer
def test_Tracer_trace():
  # Step 0
  import pysnooper
  Tracer = pysnooper.Tracer
  DISABLED = pysnooper.DISABLED
  # Step 1
  pysnooper.DISABLED = False
  # Step 2
  t = Tracer()
  # Step 3
  t.depth = 1
  # Step 4
  t.watch = [
    v if isinstance(v, BaseVariable) else CommonVariable(v)
    for v in utils.ensure_tuple(())
  ] + [
    v if isinstance(v, BaseVariable) else Exploding(v)
    for v in utils.ensure_tuple(())
  ]
  # Step 5
  t.frame_to_local_reprs = {}
  # Step 6
  t.start_times = {}


# Generated at 2022-06-12 19:52:52.154394
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    snoop = Tracer()

    def func():
        pass
    assert snoop(func) is func

    @snoop
    def func2():
        pass
    assert func2.__name__ == 'func2'
    assert inspect.isfunction(func2)

    class Class(object):
        def __init__(self):
            self.x = 1

        def method(self):
            pass

        def __str__(self):
            return 'str'

        def __repr__(self):
            return 'repr'

        @classmethod
        def classmethod(cls):
            pass

    assert str(Class()) == 'str'
    assert repr(Class()) == 'repr'

    cls = snoop(Class)
    assert str(cls()) == 'str'

# Generated at 2022-06-12 19:52:59.163822
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    global DISABLED
    DISABLED = False
    start_times = {1: datetime_module.datetime.now()}
    duration = datetime_module.datetime.now() - start_times[1]
    elapsed_time_string = pycompat.timedelta_format(duration)
    snooper = Tracer()
    snooper.frame_to_local_reprs[1] = {}
    snooper.start_times = start_times

    snooper.write = MagicMock()
    calling_frame = inspect.currentframe().f_back
    snooper.__exit__(calling_frame, None, None)

# Generated at 2022-06-12 19:53:05.772162
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    t = Tracer(output = sys.stderr, watch = ("list",), watch_explode = ('a',), depth = 1, prefix = '', overwrite = False, thread_info = False, custom_repr = (), max_variable_length = 100, normalize = False, relative_time = False)
    t.__call__('method')
    t.__call__(t)


# Generated at 2022-06-12 19:54:13.158346
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pysnooper
    import logging
    with pysnooper.snoop(logging.error):
         cls = 0
         pysnooper.snoop()
         [1, 2, 3][1]
         {}
         {'uname': 'yyin'}
         [1, 2, 3].pop(1)[1]
         {1, 2, (1, 2, 3)}
         def my_func():
             pass
         class MyClass():
             pass
         class MyClass(list):
             pass
         class MyClass(Exception):
             pass
         my_func()
         MyClass()
         MyClass()


# Generated at 2022-06-12 19:54:19.866216
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f(x, y=3):
        a = 1
        b = 2
        c = None
        v = x * y
        return v
    while 1:
        f(1)
    locals_dict = get_local_reprs(sys._getframe(1))
    assert locals_dict == {'a': '1', 'b': '2', 'x': '1', 'y': '3', 'v': '3'}
    locals_dict = get_local_reprs(sys._getframe(1), watch=(
        CommonVariable(re.compile('v')),
    ))
    assert locals_dict == {'v': '3', 'x * y': '3'}



# Generated at 2022-06-12 19:54:21.507822
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    frame = inspect.currentframe()
    assert get_path_and_source_from_frame(frame)[0][-7:] == 'spyder.py'
    del frame



# Generated at 2022-06-12 19:54:31.806417
# Unit test for constructor of class Tracer
def test_Tracer():
    import io
    output = io.StringIO()
    tracer = Tracer(output)
    assert tracer.watch == []
    assert tracer.depth == 1
    assert tracer.prefix == ""
    assert tracer.thread_info is False
    assert tracer.custom_repr == ()
    assert tracer.max_variable_length == 100
    assert tracer.normalize is False
    assert tracer.relative_time is False

    tracer = Tracer(output, watch=('foo', 'bar'), watch_explode=('baz',), depth=2,
                    prefix='ZZZ ', overwrite=True, thread_info=True,
                    custom_repr=((type, lambda x: "custom"),), max_variable_length=200,
                    normalize=True, relative_time=True)

# Generated at 2022-06-12 19:54:42.128366
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    class C:
        def foo(self):
            pass

    orig_func = C.foo
    snoop = Tracer()
    wrapped_func = snoop._wrap_function(orig_func)
    assert orig_func is not wrapped_func

    snooped_func = snoop._wrap_function(wrapped_func)
    assert orig_func is not snooped_func
    assert wrapped_func is not snooped_func
    assert wrapped_func.__code__ is not snooped_func.__code__

    snooped_method = snoop._wrap_function(C().foo)
    assert orig_func is not snooped_method
    assert wrapped_func is not snooped_method
    assert wrapped_func.__code__ is not snooped_method.__code__
    assert snooped_

# Generated at 2022-06-12 19:54:46.315457
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    my_trace = Tracer()
    my_trace.depth = 2
    my_trace.target_codes.add(inspect.currentframe().f_back.f_code)
    my_trace.target_frames.add(inspect.currentframe().f_back)
    # TODO: get start_time, duration and elapsed_time_string
    # TODO: get indent
    assert my_trace.__exit__(None, None, None) is None

# Generated at 2022-06-12 19:54:57.039852
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer()
    tracer.write = mock_write = mock.Mock()
    tracer.watch = [BaseVariable('foo')]
    mock_frame = mock.Mock()
    mock_get_path_and_source_from_frame = mock.Mock()
    mock_get_path_and_source_from_frame.return_value = ('path', 'source')
    mock_get_local_reprs = mock.Mock()
    mock_get_local_reprs.return_value = {'foo': 'bar'}
    mock_thread_info_padding = mock.Mock()
    mock_thread_info_padding.return_value = 0
    mock_timestamp = mock.Mock()
    mock_timestamp.return_value = 'timestamp'
    tracer.thread

# Generated at 2022-06-12 19:55:05.213839
# Unit test for constructor of class Tracer
def test_Tracer():
    from io import StringIO
    from unittest import TestCase

    class Test(TestCase):
        def test_basic(self):
            output = StringIO()
            with Tracer(output=output, watch=('x',)):
                x = 1
                x = 2
            self.assertEqual(output.getvalue(),
                             u'Starting var:.. x = 1\n'
                             u'Modified var:.. x = 2\n'
                             u'Return value:.. 2\n'
                             )

        # `return 4` is ignored, because there's no user code after it
        def test_inner(self):
            output = StringIO()
            with Tracer(output=output, watch=('x',)):
                x = 1

                def inner():
                    x = 3
                    return 4
               

# Generated at 2022-06-12 19:55:06.413279
# Unit test for constructor of class Tracer
def test_Tracer():
    pass


# Generated at 2022-06-12 19:55:14.949281
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f():
        x = [1, 2, 3]
        y = {'a': 1, 'b': 2}
        return
    g = f.__globals__
    fc = f.__code__
    frame = fc.co_nlocals * (None,)
    frame = frame[:fc.co_nlocals]
    frame = type(frame)(
        frame[:fc.co_argcount] +
        tuple(g[var] for var in fc.co_varnames[:fc.co_argcount]) +
        frame[fc.co_argcount:]
    )
    frame = frame.__class__(frame, g, 'bla.py', 5)