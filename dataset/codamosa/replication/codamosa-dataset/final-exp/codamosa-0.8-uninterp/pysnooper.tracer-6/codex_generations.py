

# Generated at 2022-06-12 19:46:56.069325
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .. import api
    from .variables import watcher

    def test_inner():
        var = 'x'
        var = api.watch(var)
        return var
    test_outer = api.watch(test_inner)

    stack = traceback.extract_stack(limit=2)
    assert len(stack) >= 2
    stack.reverse()
    def print_frame_details(frame, source=None):
        print('\nLocation: %s:%d' % (frame.f_code.co_filename, frame.f_lineno))
        print('  Module: %s' % frame.f_globals.get('__name__', ''))
        print('  Function: %s' % frame.f_code.co_name)
        print('  Line Contents: %r' % source)

   

# Generated at 2022-06-12 19:47:08.332717
# Unit test for constructor of class Tracer
def test_Tracer():
    test_watch = ('watched_variable', 'type(watched_variable)')
    test_watch_explode = ('exploded_variable', '.items')
    test_type_watch = (type, 'type')
    test_prefix = 'snoop:'
    test_depth = 2
    test_output = 'output.txt'
    test_overwrite = False
    test_thread_info = True
    test_type_custom_repr = (type, 'type_repr')
    test_condition_custom_repr = (lambda x: True, 'lambda_repr')
    test_max_variable_length = 50
    test_normalize = False
    test_relative_time = True

# Generated at 2022-06-12 19:47:17.849369
# Unit test for function get_local_reprs
def test_get_local_reprs():
    assert get_local_reprs(frame=None) == {}
    def f(some_arg):
        return
    assert get_local_reprs(f.__code__.__globals__,
                           ('f', 'some_arg'),
                           ('some_arg',),
                           max_length=None, normalize=False) == {
        'some_arg': '...',
        'f': '<function f at 0x...>'}
    global some_global_variable

# Generated at 2022-06-12 19:47:20.626559
# Unit test for constructor of class Tracer
def test_Tracer():
    def func(x):
        y = 2
        return x + y

    snooper = Tracer()
    wrapped_func = snooper(func)
    assert wrapped_func(1) == 3


# Generated at 2022-06-12 19:47:21.594529
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass


# Generated at 2022-06-12 19:47:28.574757
# Unit test for constructor of class Tracer
def test_Tracer():
    # Make sure constructor handles all types of arguments correctly
    import sys
    sys.stderr = open("out.log", "w")
    snoop0 = Tracer(watch=("a", "b"), watch_explode=("c", "d"), prefix="ZZZ ",
                    overwrite=True, thread_info=True, custom_repr=[("a", "a"), ("b", "b")],
                    max_variable_length=100, normalize=False, relative_time=False)
    assert len(snoop0.watch) == 2
    assert isinstance(snoop0.watch[0], CommonVariable)
    assert len(snoop0.watch_explode) == 2
    assert isinstance(snoop0.watch_explode[0], Exploding)
    assert snoop0.depth == 1

# Generated at 2022-06-12 19:47:31.208325
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    self = Tracer()
    event = None
    arg = None
    frame = None
    return self.trace(frame, event, arg)

# Generated at 2022-06-12 19:47:38.074785
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import doctest
    example = '''
    >>> import inspect
    >>> frame = inspect.currentframe()
    >>> get_path_and_source_from_frame(frame) == (__file__, inspect.getsourcelines(test_get_path_and_source_from_frame)[0])
    True
    '''
    doctest.run_docstring_examples(get_path_and_source_from_frame, None,
                                   name='test_get_path_and_source_from_frame',
                                   globs={'__file__': __file__})



# Generated at 2022-06-12 19:47:48.314843
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import os; os.chdir(os.path.dirname(__file__))
    import sys; sys.path.append('..')
    def get_path_and_source_from_frame(frame):
        return frame.f_code.co_filename, frame.f_lineno
    frame_info = get_path_and_source_from_frame(test_get_path_and_source_from_frame.func_code.co_filename,
                                                test_get_path_and_source_from_frame.func_code.co_lineno)
    assert frame_info == (os.path.abspath(__file__), test_get_path_and_source_from_frame.func_code.co_lineno - 1)



# Generated at 2022-06-12 19:47:52.914989
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    s = Tracer()
    @s
    def a():
        print(1)
    @s
    def b():
        print(123)
        1/0
    a()
    b()
    # test thread_info
    @s(thread_info=True)
    def c():
        print(111)
    c()
    c()


test_Tracer___call__()


# Generated at 2022-06-12 19:48:14.323603
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def method():
        def inner_method():
            pass
        pass
    frame = sys._getframe(0).f_back.f_back.f_back
    assert get_path_and_source_from_frame(frame) == \
           inspect.getfile(method), \
           'get_path_and_source_from_frame does not work as expected'
test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:48:20.373784
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # 
    ### Test that Tracer.trace() works #######################
    # 
    # We'll do the testing in three steps:
    # 
    # 1. We'll create a Tracer and wrap a function with it.
    # 2. We'll set the tracer's trace method as the trace function on the
    #    function's frame.
    # 3. We'll call the function.
    # 
    # In the process of running, we'll check that the Tracer writes the
    # appropriate lines.
    # 
    class DummyOutput(object):
    
        def __init__(self):
            self.lines = []
    
        def __call__(self, s):
            s = s.rstrip()
            self.lines.append(s)
    

# Generated at 2022-06-12 19:48:23.733262
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    assert not DISABLED
    global snoop_count
    snoop_count = 0
    def noop_write(s):
        pass
    tracer = Tracer(output=noop_write, depth=1)
    def foo():
        pass
    foo = tracer(foo)
    foo()
    assert snoop_count == 1

# Testing the ability of Tracer to be applied to an entire class:

# Generated at 2022-06-12 19:48:36.950814
# Unit test for constructor of class Tracer
def test_Tracer():
    def function():
        a = 3
        b = 4
        c = 5

    tracer = Tracer(watch=('a', 'b', 'c'), watch_explode=('a', 'b', 'c'))
    assert tracer.watch == [
        CommonVariable('a'),
        CommonVariable('b'),
        CommonVariable('c'),
        Exploding('a'),
        Exploding('b'),
        Exploding('c'),
    ]


# Generated at 2022-06-12 19:48:47.285810
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pytest

    def constructor_test(self, pysnooper):
        self.pysnooper = pysnooper

    tester = type('', (), {
        "constructor_test": constructor_test
    })
    tester = tester(pysnooper)

    with pytest.raises(AttributeError):
        tester.pysnooper = tester.watch
    with pytest.raises(AttributeError):
        tester.watch = tester.watch
    with pytest.raises(AttributeError):
        tester.thread_info = tester.thread_info
    with pytest.raises(AttributeError):
        tester.thread_local = tester.thread_local
    with pytest.raises(AttributeError):
        tester.target_frames = tester.target_frames


# Generated at 2022-06-12 19:48:55.409127
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    test_output = StringIO()
    tracer = Tracer(output=test_output, prefix='ZZZ ', depth=2)
    assert tracer.target_codes == set()
    assert tracer.target_frames == set()

    def foo():
        pass

    tracer._wrap_function(foo)
    assert tracer.target_codes == {foo.__code__}
    assert tracer.target_frames == set()

    # Unit test for method trace of class Tracer
    def test_Tracer_trace():
        test_output = StringIO()
        tracer = Tracer(output=test_output, prefix='ZZZ ', depth=2)

        def foo():
            pass

        foo_code = foo.__code__
        foo_frame = None
        foo_event = None

        def f():
            pass



# Generated at 2022-06-12 19:49:05.294899
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def func():
        a = 3
        x = 4
        assert get_local_reprs(inspect.currentframe(), max_length=5) == {'a': '3', 'x': '4'}

        b = 4

        assert get_local_reprs(inspect.currentframe(), max_length=5) == {'a': '3', 'x': '4',
                                                                         'b': '4'}
        c = 5
        assert get_local_reprs(inspect.currentframe(), max_length=5) == {'a': '3', 'x': '4',
                                                                         'b': '4', 'c': '5'}
        d = 4

# Generated at 2022-06-12 19:49:12.155697
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import inspect
    import pycompat
    if DISABLED:
        return
    output = None
    watch = ()
    watch_explode = ()
    depth = 1
    prefix = ''
    overwrite = False
    thread_info = False
    custom_repr = ()
    max_variable_length = 100
    normalize = False
    relative_time = False
    function = test_Tracer___call__
    function_or_class = function
    result = Tracer(output, watch, watch_explode, depth, prefix, overwrite,
                    thread_info, custom_repr, max_variable_length, normalize,
                    relative_time)(function_or_class)
    #self.assertEqual(result, function)

# Generated at 2022-06-12 19:49:16.966951
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    #Setup
    output = StringIO()
    obj = Tracer(output)
    frame = None
    event = None
    arg = None
    #Stubs
    #Test
    obj.trace(frame,event,arg)
    #Verify
    assert True


# Generated at 2022-06-12 19:49:18.867498
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass



# Generated at 2022-06-12 19:49:45.812368
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import StringIO
    class Tracer:
        def __init__(self, output=None, watch=(), watch_explode=(), depth=1,
                     prefix='', overwrite=False, thread_info=False, custom_repr=(),
                     max_variable_length=100, normalize=False, relative_time=False):
            self._write = get_write_function(output, overwrite)

            self.watch = [
                v if isinstance(v, BaseVariable) else CommonVariable(v)
                for v in utils.ensure_tuple(watch)
             ] + [
                 v if isinstance(v, BaseVariable) else Exploding(v)
                 for v in utils.ensure_tuple(watch_explode)
            ]
            self.frame_to_local_reprs = {}

# Generated at 2022-06-12 19:49:51.960174
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    tracer = Tracer(output=None, watch=(), watch_explode=(),
                    depth=1, prefix='', overwrite=False, thread_info=False, custom_repr=(),
                    max_variable_length=100, normalize=False, relative_time=False)
    func = lambda: None
    result = tracer.__call__(func)
    assert result == Python26MethodWrapper(result)

# Generated at 2022-06-12 19:49:59.351455
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    global DISABLED

    print('testing Tracer.__call__()')

    def target(*args):
        '''Testing target.'''
        return args

    def check_result(target, args, expected=None, expected_type=None,
                     debug=0, overwrite=False, watch=None,
                     watch_explode=None, depth=1, prefix='', custom_repr=()):

        global DISABLED
        DISABLED = False
        output = io.StringIO()
        trace = Tracer(output=output, watch=watch, watch_explode=watch_explode,
        depth=depth, prefix=prefix, overwrite=overwrite, custom_repr=custom_repr)
        result = trace(target)(*args)
        result_string = output.getvalue()
        output.close()


# Generated at 2022-06-12 19:50:08.275523
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    ### Test for simple_wrapper
    ##################################################
    @pysnooper.snoop()
    def f(x):
        return x * 2
    output = []
    f(2)
    assert output[0] == "    12:00:00.000000000 Call.....     1 def f(x):"
    assert output[1] == "    12:00:00.000000000 Return...     2     return x * 2"
    assert output[2] == "    12:00:00.000000000 Return value:.. 4"
    ##################################################

    ### Test for generator_wrapper
    ##################################################
    @pysnooper.snoop()
    def g():
        yield 4
    output = []
    gen = g()
    gen.send(None)

# Generated at 2022-06-12 19:50:08.937659
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass

# Generated at 2022-06-12 19:50:09.727177
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    pass


# Generated at 2022-06-12 19:50:15.178245
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    t = Tracer()
    t.__enter__()
    assert t.thread_local.original_trace_functions == [None]
    assert sys.gettrace() == t.trace
    t.__exit__(None, None, None)

# Generated at 2022-06-12 19:50:23.549231
# Unit test for function get_local_reprs
def test_get_local_reprs():
    a = 3
    b = [1, 2, 3]
    inline_frame = inspect.currentframe().f_back
    assert(get_local_reprs(inline_frame, watch=[]) == {'a':'3', 'b':'[1, 2, 3]'})
    assert(get_local_reprs(inline_frame, watch=[]) == get_local_reprs(
        inline_frame, watch=[], max_length=5))
    assert(get_local_reprs(inline_frame, watch=[]) == get_local_reprs(
        inline_frame, watch=[], custom_repr=None))
    assert(get_local_reprs(inline_frame, watch=[], max_length=8) == {'a': '3', 'b': '[1, 2, 3]'})

# Generated at 2022-06-12 19:50:34.541096
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .variables import CommonVariable
    def f(a, b, c, d=4, e=5, f=6):
        7
        a, b, c, d, e, f
        asd, qwe, zxc, 123, 4567, 8901
        a == b == c == d == e == f
        a is b is c is d is e is f
        'a', 'b', 'c', 'd', 'e', 'f'
        'a' * 60 + '\n' + 'b' * 30 + 'q' + '\n' + 'c' * 15 + '\n' + 'asd' * 20 + '\n' + 'qwe' * 20 + '\n'

# Generated at 2022-06-12 19:50:39.537322
# Unit test for function get_write_function
def test_get_write_function():
    import sys
    import io
    import tempfile
    with tempfile.NamedTemporaryFile('w', encoding='utf-8') as f:
        f.write('previous content')
        f.flush()
        write_function = get_write_function(f, overwrite=True)
        write_function('my awesome content')
        output = f.read()
    assert output == 'my awesome content'



# Generated at 2022-06-12 19:51:11.839575
# Unit test for function get_local_reprs
def test_get_local_reprs():
    import types
    class MyClass:
        var1 = 1
        var2 = 2
        def __str__(self):
            return 'MyClass'

    def my_custom_repr(my_object):
        if isinstance(my_object, types.FunctionType):
            return 'a function!'
        else:
            raise TypeError()

    def test_func():
        y = 2
        my_class = MyClass()

        def inner_func():
            x = 1
            return x*y

        return inner_func

    frame = test_func().__code__.co_firstlineno
    assert frame == 11
    frame = inspect.currentframe()
    test_func_frame = None

# Generated at 2022-06-12 19:51:18.815987
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from .utils import CommonVariable, CommonVariableAccumulator
    from .utils import CommonVariableAccumulatorWithExploding, Exploding
    from .utils import get_shortish_repr
    from .utils import is_string_like
    from .utils import truncate

    def custom_repr(x):
        return 'foo'

    @pysnooper.snoop()
    def foo():
        pass

    @pysnooper.snoop(watch='bar')
    def foo1(bar):
        pass

    @pysnooper.snoop(watch=['foo', 'bar'])
    def foo2(foo, bar):
        pass


# Generated at 2022-06-12 19:51:30.038660
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pytest
    from pathlib import Path
    from pysnooper.tracer import DISABLED
    from pysnooper.tracer import Tracer
    from pysnooper.tracer import get_write_function
    from pysnooper.tracer import thread_global
    class OnceTester():
        def __init__(self, function, max_loop_times=None):
            self._function = function
            self._max_loop_times = max_loop_times
            self._loop_times = 0

        def __next__(self):
            if self.stop():
                raise StopIteration
            self._loop_times += 1
            return self._function()

        def __iter__(self):
            return self


# Generated at 2022-06-12 19:51:39.600738
# Unit test for constructor of class Tracer
def test_Tracer():
    import tempfile

    def test_function():
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        print(a + b + c + d + e)

    with tempfile.NamedTemporaryFile('r', delete=False) as f:
        s = Tracer(output=f, normalize=True)
        s(test_function)()

    with open(f.name, 'r') as f:
        lines = f.readlines()


# Generated at 2022-06-12 19:51:50.182683
# Unit test for constructor of class Tracer
def test_Tracer():
    global DISABLED

    def test():
        x = 4
        while x > 0:
            assert x % 2 == 0
            x -= 1

    assert 'test' in globals() # we assume this function is called 'test' :)

    DISABLED = True
    assert Tracer()(test) is test
    DISABLED = False

    import io
    import sys
    output = io.StringIO()
    Tracer(output=output)(test)()
    output.seek(0)

# Generated at 2022-06-12 19:51:59.148364
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def a_function(x):
        print(x)
        print(x + 2)
    frame = inspect.currentframe()
    while frame.f_code.co_name != 'a_function':
        frame = frame.f_back
    result = get_path_and_source_from_frame(frame)
    assert result[0].endswith(os.path.join('tests', 'test_cool_inspect.py'))
    assert result[1][frame.f_lineno - 1] == '        print(x + 2)'
test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:52:01.628543
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    assert (Tracer().__exit__(None, None, None)) == (None)

# Generated at 2022-06-12 19:52:11.972481
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import unittest
    import decorator
    import pdb
    import inspect
    import threading
    import time
    from utils import get_path_and_source_from_frame
    from utils import traceback_frame_name
    from utils import get_local_reprs
    from utils import truncate
    from importlib import reload
    from utils import timedelta_format
    from utils import time_isoformat
    from utils import iscoroutinefunction
    from utils import isasyncgenfunction
    from utils import get_write_function
    from utils import ensure_tuple
    from utils import BaseVariable
    from utils import CommonVariable
    from utils import Exploding

    OPEN = -1
    CLOSED = 0
    reload(unittest)
    reload(decorator)

# Generated at 2022-06-12 19:52:14.544164
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    assert Tracer().trace == Tracer().trace

# class Tracer definition
# Methods order:
# (1) special methods
# (2) public methods
# (3) private methods


# Generated at 2022-06-12 19:52:23.350309
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import io
    import unittest
    import unittest.mock

    class TracerTestCase(unittest.TestCase):
        def setUp(self):
            self.output = io.StringIO()
            self.output_list = []
            self.write_mode = 'string'
            self.patch = unittest.mock.patch('pysnooper._snoop.datetime', wraps=datetime_module)
            self.mock_datetime = self.patch.start()
            self.mock_datetime.now.return_value = datetime_module.datetime(2017, 4, 21, 1, 2, 3, 123456)
            self.patch = unittest.mock.patch('pysnooper._snoop.time')
            self.mock_time = self.patch

# Generated at 2022-06-12 19:53:00.346895
# Unit test for method __exit__ of class Tracer

# Generated at 2022-06-12 19:53:02.775202
# Unit test for constructor of class Tracer
def test_Tracer():
    import utils
    # Test Tracer constructed with no attribute
    Tracer()


# Generated at 2022-06-12 19:53:06.061080
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__(): 
    tracer = Tracer(None)
    ## test body of __enter__
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return None



# Generated at 2022-06-12 19:53:13.338748
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    def f():
        assert thread_global.depth == -1
        with Tracer():
            assert thread_global.depth == 0
            def g():
                assert thread_global.depth == 1
                with Tracer():
                    assert thread_global.depth == 2
                assert thread_global.depth == 1
            g()
            assert thread_global.depth == 0
        assert thread_global.depth == -1

    with captured_stderr() as output:
        f()
    assert output.getvalue() == '    Elapsed time: 0:00:00.000001\n'

# Generated at 2022-06-12 19:53:21.911414
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    co = compile('a = 7', '<string>', 'exec')
    frame = inspect.FrameInfo(None, None, 'my_locals', co, 0, None)
    frame.f_locals['__loader__'] = None
    frame.f_globals['__loader__'] = None
    frame.f_globals['a'] = 7
    assert get_path_and_source_from_frame(frame) == ('<string>', ['a = 7'])



# Generated at 2022-06-12 19:53:23.954436
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import doctest
    doctest.run_docstring_examples(Tracer.__exit__, globals())



# Generated at 2022-06-12 19:53:25.772363
# Unit test for constructor of class Tracer
def test_Tracer():
    print(Tracer.__init__.__doc__)
    tracer = Tracer()
    assert(tracer.depth == 1)
    assert(tracer.watch == [])


# Generated at 2022-06-12 19:53:34.388195
# Unit test for function get_write_function
def test_get_write_function():
    import io
    filename = 'test.txt'
    output = io.StringIO()
    output_path = utils.get_test_file_path(filename)
    write = get_write_function(output=output, overwrite=False)
    write('foo')
    write(' bar')
    output.seek(0)
    assert output.read() == 'foo bar'
    write = get_write_function(output=output_path, overwrite=False)
    write('foo')
    write(' bar')
    with open(output_path, 'r') as f:
        assert f.read() == 'foo bar'
    for overwrite in (True, False):
        write = get_write_function(output=output, overwrite=overwrite)
        write('foo')
        write(' bar')
        output.seek(0)


# Generated at 2022-06-12 19:53:39.704229
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tr = Tracer()
    tr.thread_info_padding = 5
    current_thread = threading.current_thread()
    tr.set_thread_info_padding(
        "{ident}-{name} ".format(ident=current_thread.ident,
                                 name=current_thread.getName()))
    assert tr.thread_info_padding == current_thread.getName() + " ".__len__() + 1


b = Tracer()
c = Tracer()


# Generated at 2022-06-12 19:53:51.669935
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    print("Test Tracer___exit__ is started!")

    import io
    import pytest
    import string

    def test_output_to_file(output_file, output_overwrite):
        import os
        # please make sure the content of output_file is empty
        assert os.path.getsize(output_file) == 0
        with pysnooper.snoop(output=output_file, overwrite=output_overwrite):
            string.ascii_letters
        assert os.path.getsize(output_file) > 0

    def test_output_to_stdout(output_file, output_overwrite):
        import sys

        if sys.version_info < (3, 3):
            pytest.skip('capture_output() not available')
            return

        import os
        output_size_before_

# Generated at 2022-06-12 19:54:45.943681
# Unit test for function get_path_and_source_from_frame

# Generated at 2022-06-12 19:54:56.549238
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer(watch=('x',))

    def foo():
        y = 1
        x = 2
        return 'bar'

    tracer.target_codes.add(foo.__code__)

    frame = inspect.currentframe().f_back
    frame.f_code = foo.__code__
    frame.f_trace = tracer.trace
    tracer.target_frames.add(frame)

    # This is really the line that makes it work when using the
    # regular unittest runner; otherwise it's treated as a generator.
    frame.__trace_function__ = tracer.trace
    sys.settrace(tracer.trace)
    with tracer:
        foo()
    sys.settrace(None)
    tracer.target_frames.remove(frame)

# Generated at 2022-06-12 19:55:04.977354
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    with pysnooper.snoop(output=StringIO()) as output:

        # x = 17
        frame = inspect.currentframe()
        frame.f_lineno = 8
        assert output.get_value() == ''
        event = 'call'
        arg = None
        Tracer(watch=('x',)).trace(frame, event, arg)
        assert output.get_value() == '    Call ended by exception\n'

        # x = 17
        frame = inspect.currentframe()
        frame.f_lineno = 14
        assert output.get_value() == '    Call ended by exception\n'
        event = 'exception'
        arg = None, None, None
        Tracer(watch=('x',)).trace(frame, event, arg)

# Generated at 2022-06-12 19:55:11.452834
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import StringIO

    with StringIO.StringIO() as string_io:
        with pysnooper.snoop(string_io):
            x = 1
            y = 2
            assert x == y
        #assert False, string_io.getvalue()


# This class's purpose is to make the test pytest-friendly,
# by wrapping the activation and deactivation of snoop()'s context manager.

# Extracted from the `with` statement from the __call__ method of the Tracer
# class

# Generated at 2022-06-12 19:55:18.475053
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import io
    import sys

    with io.StringIO() as output, pysnooper.snoop(output=output, prefix='ZZZ '):
        assert sys.gettrace() is Tracer.trace
        assert sys.gettrace() is not None
    assert sys.gettrace() is None


# pysnooper.get_write_function
# function

# Used to wrap an output file object with a lock, such that:
#
# 1. Write operations are done one at a time (thread-safe)
# 2. Writes are flushed to disk immediately

# Generated at 2022-06-12 19:55:24.190430
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import subprocess
    import pytest
    import re
    import os
    import sys
    import signal
    import time
    import subprocess
    import threading
    import unittest
    import random
    import pdb
    import inspect
    import io
    import inspect
    import tokenize
    import traceback
    import ast
    import sys
    import warnings
    import re
    import io
    import collections
    import copy
    import os
    import platform
    import ast
    import builtins
    import numbers
    import types
    import functools
    import inspect
    import weakref
    import logging
    import sys
    from pysnooper.var import _var
    from pysnooper.utils import truncate
    from pysnooper.utils import get_path_and_source_from_frame
   

# Generated at 2022-06-12 19:55:28.055449
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    @pysnooper.snoop()
    def foo(bar=None):
        a = {}
        b = ()
        c = []
        print(bar)

    foo('baz')
    assert foo.__name__ == 'foo'
    assert foo.__doc__ == 'foo()\n'

# Generated at 2022-06-12 19:55:36.793975
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # init
    tracer = Tracer()
    attrs = {}
    # starting invoking of the method __enter__
    stack = []
    tracer.thread_local.__dict__['original_trace_functions'] = stack
    sys.settrace = MagicMock(return_value=None)
    with patch('pysnooper.snoop.get_write_function', return_value=None),\
     patch('pysnooper.snoop.inspect.currentframe', return_value = MagicMock(**{'f_back': attrs})):
        tracer.__enter__()
    # asserts
    sys.settrace.assert_called_once_with(tracer.trace)
    assert len(stack) == 1
    for key in attrs.keys():
        assert key in tracer.target_

# Generated at 2022-06-12 19:55:47.161873
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .common import FakeFile
    from contextlib import contextmanager

    def assert_source(source, lines):
        source_lines = source.split('\n')
        for source_line, expected_line in zip(source_lines, lines):
            assert source_line == expected_line

    # Some tests rely on the fact that `__file__` is the last line in the
    # frame's `f_code` object's `co_filename` field
    import os
    absolute_path = os.path.abspath(__file__)
    __file__ = os.path.relpath(__file__)

    frame = inspect.currentframe()

# Generated at 2022-06-12 19:55:55.212614
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    random_folder = tempfile.mkdtemp()
    with open(os.path.join(random_folder,'test.txt'),'w') as test_file:
        test_file.write('abc')
    s = 'xyz'
    file_writer = FileWriter(os.path.join(random_folder,'test.txt'), overwrite=False)
    file_writer.write(s)
    with open(os.path.join(random_folder,'test.txt'),'r') as test_file:
        assert test_file.read() == 'abcxyz'
