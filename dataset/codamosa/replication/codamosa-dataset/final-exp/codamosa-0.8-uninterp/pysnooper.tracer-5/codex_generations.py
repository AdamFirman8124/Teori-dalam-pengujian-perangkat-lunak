

# Generated at 2022-06-12 19:47:21.074385
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import attr
    
    
    @attr.s(slots=True)
    class Person():
        
        name = attr.ib(type=str)
        age = attr.ib(type=int)
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        def __repr__():
            return '{0}(name={1}, age={2})'.format(
                type(self).__name__,
                repr(self.name),
                repr(self.age),
            )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Generated at 2022-06-12 19:47:22.051797
# Unit test for constructor of class Tracer
def test_Tracer():
    assert Tracer
    assert Tracer()


# Generated at 2022-06-12 19:47:24.506224
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    
    a = 0
    pysnooper.snoop(watch=[a])
    
    
    a = 1
    a = 2
    return a
test_Tracer_trace()


# Generated at 2022-06-12 19:47:32.134113
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # Test with default args
    tracer = pysnooper.snoop()
    stack = tracer.thread_local.original_trace_functions
    assert len(stack) == 0
    tracer.__enter__()
    assert len(stack) == 1
    assert sys.gettrace() == tracer.trace
    frame = inspect.currentframe().f_back
    assert frame in tracer.target_frames
    assert frame in tracer.start_times
    tracer.__exit__(None, None, None)
    assert frame not in tracer.target_frames
    assert frame not in tracer.start_times
    assert len(stack) == 0
    assert sys.gettrace() == stack[-1]

    tracer = pysnooper.snoop()
    stack = tracer.thread_local.original

# Generated at 2022-06-12 19:47:34.963495
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert get_path_and_source_from_frame(sys._getframe(0)) == (
        __file__, inspect.getsourcelines(test_get_path_and_source_from_frame)[0])



# Generated at 2022-06-12 19:47:45.785083
# Unit test for constructor of class Tracer
def test_Tracer():
    os.environ['PYSNOOPER_DISABLED'] = '1'
    # Normal output that does not need overwrite, such as output file or
    #  stdout and stderr.
    test_snooper = Tracer(output=StringIO())
    assert test_snooper.watch == ()

    # Overwritable output that has to be cleared before being used
    #  such as stdout and stderr.
    test_snooper_overwrite = Tracer(output=StringIO(), overwrite=True)
    assert test_snooper_overwrite._write != test_snooper._write

    # Depth
    test_snooper_depth = Tracer(output=StringIO(), depth=2)
    assert test_snooper_depth.depth == 2

    # watch_explode, depth, prefix and

# Generated at 2022-06-12 19:47:52.499508
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    """
    Tests a combination of `get_path_and_source_from_frame` and `get_local_reprs`.

    """
    # Python 2 must be on because of `__loader__`.

    def internal():
        return get_path_and_source_from_frame(inspect.currentframe())

    result = internal()
    assert len(result) == 2
    path, source = result
    if os.path.samefile(path, __file__):
        assert isinstance(source, list)
        assert all(isinstance(s, pycompat.text_type) for s in source)



# Generated at 2022-06-12 19:47:53.932809
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    @pysnooper.snoop()
    def f():
        a = 1


# Generated at 2022-06-12 19:47:57.235439
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # __exit__ actual vs expected
    assert Tracer(watch=())

    # __exit__ actual vs expected
    assert Tracer(watch=())

    # __exit__ actual vs expected
    assert Tracer(watch=())

    # __exit__ actual vs expected
    assert Tracer(watch=())


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-12 19:48:02.051723
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import pytest
    def test_function():
        return
    def test_function2():
        return
    def test_function3():
        return
    def test_function4():
        return
    def test_function5():
        return
    def test_function6():
        return
    def test_function7():
        return
    def test_function8():
        return

    def test_function_not_covered():
        test_function_not_covered.inc()
        return

    test_function_not_covered.inc = lambda : None
    @pysnooper.snoop(watch=("test_function_not_covered.inc",))
    def test_function_not_covered():
        test_function_not_covered.inc()
        return
    test_function_not_covered()


# Generated at 2022-06-12 19:48:37.985872
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # monkey-patching `traceback.extract_stack` so that it puts us in a fake
    # file:
    original_extract_stack = traceback.extract_stack
    def extract_stack(f, limit=None):
        stack = original_extract_stack(f, limit)
        stack[-1] = (os.path.join('user', 'test.py'), stack[-1][1], '<line>', None)
        return stack
    traceback.extract_stack = extract_stack

    class Loader(object):
        def get_source(self, module_name):
            assert module_name == '__main__'
            return 'print(1)'
    stack = traceback.extract_stack()
    frame = inspect.getouterframes(inspect.currentframe())[1][0]

# Generated at 2022-06-12 19:48:42.672106
# Unit test for constructor of class Tracer
def test_Tracer():
    # FIXME (use a TestCase class)
    # Test initialization of Tracer:
    # Test output path and overwrite
    # Test watch and watch_explode
    # Test depth
    # Test prefix
    # Test thread_info
    # Test max_variable_length
    # Test custom_repr
    pass


# Generated at 2022-06-12 19:48:50.724494
# Unit test for constructor of class Tracer
def test_Tracer():
    if _PY37:
        f, g, h = types.SimpleNamespace(), types.SimpleNamespace(), types.SimpleNamespace()
        _ = Tracer(watch=f, watch_explode=g, custom_repr=h, normalize=True, relative_time=True)
    f = lambda: 'foo'
    f2 = lambda: 101
    f3 = lambda: 'bar'
    _ = Tracer(watch=f, watch_explode=f2, custom_repr=f3, normalize=True, relative_time=True)

################################################################################
### Tools for unit testing: ###################################################
#                                                                             #

# Generated at 2022-06-12 19:48:54.624426
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import sys
    import os
    import random
    sys.path.append('../../')
    from pysnooper import snoop

    @snoop
    def fun():
        return random.randint(1, 100)

    def test_snoop():
        a = fun()

    test_snoop()


# Generated at 2022-06-12 19:48:59.337026
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():

    # Tracer.__call__(self, function_or_class)

    def foo():  # noqa
        pass

    class Foo:  # noqa
        pass

    output = io.StringIO()
    tracer = pysnooper.Tracer(output=output)

    assert isinstance(tracer(foo), types.FunctionType)
    assert isinstance(tracer(Foo), type)



# Generated at 2022-06-12 19:49:02.181814
# Unit test for constructor of class Tracer
def test_Tracer():

    @Tracer(watch=('i', 'j'), watch_explode=('foo'))
    def foo(i):
        bar(i)

    def bar(j):
        pass

    foo(1)

# Generated at 2022-06-12 19:49:10.597961
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    file_name = os.path.join(os.path.dirname(__file__), 'test_stuff.py')
    with open(file_name, 'r') as f:
        source = f.readlines()
    globals_dict = {'__name__': 'test_stuff'}
    code = compile(source, file_name, 'exec')
    frame = inspect.FrameInfo(None, None, None, code, globals_dict, None)
    actual_file_name, actual_source = get_path_and_source_from_frame(frame)
    assert actual_file_name == file_name
    assert actual_source == source



# Generated at 2022-06-12 19:49:23.529338
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer(None)
    thread_global.__dict__.setdefault('depth', -1)
    depth_before = thread_global.depth
    duration = datetime_module.datetime.datetime.now()
    start_time = duration
    calling_frame = inspect.currentframe()
    calling_frame.f_trace = tracer.trace
    tracer.target_frames.add(calling_frame)
    tracer.start_times[calling_frame] = duration
    def test_func():
        functions_stack = tracer.thread_local.__dict__.setdefault(
            'original_trace_functions', []
        )
        functions_stack.append(sys.gettrace())
        sys.settrace(tracer.trace)
    test_func()

# Generated at 2022-06-12 19:49:32.237039
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f(x, y):
        z = (x, y)
        a = [y, z]
        b = {'c': x}
        d = functools.partial(f, x)
        e = functools.partial(f, x, y)

        g = 1
        return g

    class CustomRepr:
        def __repr__(self):
            return 'whatever'

    class CustomRepr2:
        def __repr__(self):
            return 'I am CustomRepr2'

    def custom_repr(x):
        if isinstance(x, CustomRepr2):
            return 'I am a CustomRepr2'
        else:
            return 'whatever'

    frame = inspect.currentframe()
    frame = frame.f_back
    result = get_local_re

# Generated at 2022-06-12 19:49:35.001122
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    param = pysnooper.snoop(watch=('foo', 'self'))
    param.__enter__()


# Generated at 2022-06-12 19:50:29.064803
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    """
    Unit test for module method trace of class Tracer
    """
    s = Tracer()
    assert s.trace
    

# Generated at 2022-06-12 19:50:35.076146
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import unittest
    import unittest.mock
    class Args: pass
    args = Args()
    args.output = None
    args.watch = []
    args.watch_explode = []
    args.depth = 1
    args.prefix = ''
    args.overwrite = False
    args.thread_info = False
    args.custom_repr = ()
    args.max_variable_length = 100
    args.normalize = False
    args.relative_time = False
    tracer = Tracer(**vars(args))
    class TestTracer___call__(unittest.TestCase):

        def test_Tracer___call__(self):
            def decorated_function():
                pass

# Generated at 2022-06-12 19:50:43.847716
# Unit test for constructor of class Tracer
def test_Tracer():
    class MockFile(object):
        def __init__(self):
            self._text = ""

        def write(self, text):
            self._text += text

        def __eq__(self, other):
            return self._text == other

        def __repr__(self):
            return self._text

    mf = MockFile()
    t = Tracer()
    t._write = mf.write
    t.thread_info = True
    t.thread_info_padding = 0
    t.set_thread_info_padding("")
    t.set_thread_info_padding("        ")

    def no_op():
        pass

    def no_op_2():
        pass

    def return_val_func():
        return 42

    def call_func():
        no_op()


# Generated at 2022-06-12 19:50:55.450403
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Arrange
    DISABLED = False
    function = None
    frame = 'aa'
    event = 'call'
    arg = None
    _ = Tracer()
    _.__enter__()
    _._is_internal_frame = MagicMock(return_value=True)
    _.depth = 1
    _.depth = -1
    _.depth = 0
    # Act
    result = _.trace(frame, event, arg)
    # Assert
    assert result == None
    # Arrange
    DISABLED = False
    function = None
    frame = 'aa'
    event = 'call'
    arg = None
    _ = Tracer()
    _.__enter__()
    _._is_internal_frame = MagicMock(return_value=True)
    _.depth = 1

# Generated at 2022-06-12 19:51:02.258532
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():

    def test_Tracer___call___return_tracer():
        assert isinstance(pysnooper.snoop(), Tracer)

    def test_Tracer___call___return_tracer_with_output():
        assert isinstance(pysnooper.snoop(output=StringIO()), Tracer)

    def test_Tracer___call___return_decorated_function():
        result = pysnooper.snoop()(lambda x: x+1)
        assert callable(result)


# Generated at 2022-06-12 19:51:12.616828
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    from pyfakefs.fake_filesystem_unittest import TestCase
    import pysnooper
    class Tracer___enter__(TestCase):
        def setUp(self):
            self.fs = patcher.fs
            self.fs.add_real_directory(os.path.abspath(os.path.dirname(__file__)))
            self.fs.add_real_directory(os.path.abspath(pysnooper.__file__))
            self.fs.add_real_directory(os.path.abspath(pysnooper.__file__.replace('pysnooper.py','__pycache__')))
            self.output = io.StringIO()
            self.watch = ()
            self.watch_explode = ()
            self.depth = 1

# Generated at 2022-06-12 19:51:18.652721
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    with sf.ThreadedUnbufferedStream(stream=StringIO()) as stream, \
            patch('sys.stdout', stream):
        local_var = None
        with pysnooper.snoop():
            def raise_exception():
                raise Exception("hi")
            raise_exception()
        lines = stream.read().splitlines()
        assert lines[0].split() == ['Source', 'path:...', 'pysnooper.py']
        assert lines[1].split() == ['Starting', 'var:..', 'local_var', '=']
        assert lines[2].split() == ['Exception:...', 'Exception:', 'hi']
        assert lines[3].split() == ['Elapsed', 'time:', '0:00:00.000001']


# Generated at 2022-06-12 19:51:30.039407
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def check_func(func, expected_prefix, expected_output_file, expected_output_overwrite,
                   expected_watch, expected_watch_explode, expected_depth, expected_prefix,
                   expected_overwrite, expected_thread_info, expected_max_variable_length,
                   expected_normalize, expected_relative_time, expected_custom_repr):
        assert func._snooper._write == expected_write_func
        assert func._snooper.watch == expected_watch
        assert func._snooper.depth == expected_depth
        assert func._snooper.prefix == expected_prefix
        assert func._snooper.thread_info == expected_thread_info

    import io
    import mock
    import os

    def func_to_decorate():
        pass


# Generated at 2022-06-12 19:51:35.604970
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def function(x):
        y = 2
        z = y * x
        return z
    frame = inspect.currentframe().f_back
    frame.f_locals['x'] = 5
    result = get_local_reprs(frame, watch=(CommonVariable('x', 7), ))
    assert result == {'x': '7', 'y': '2', 'z': '10'}



# Generated at 2022-06-12 19:51:43.167354
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import inspect
    import sys
    import threading
    from . import pycompat
    from . import utils
    from .debug import get_path_and_source_from_frame
    from .utils_test import get_write_function
    logger.info('Testing test_Tracer___call__')
    
    
    
    try:
        class Foo:
            def foo(self, bar):
                pass
            def bar(self, **kwargs):
                pass
            def baz(self, *args):
                pass
    except Exception as e:
        logger.exception('Exception occured in try block')
        raise e
    
    
    

# Generated at 2022-06-12 19:52:49.649170
# Unit test for constructor of class Tracer
def test_Tracer():
    normalize_output = "    New var:....... a = [1, 2, 3]\n    New var:....... b = [[1, ...], [2, ...]]\n    New var:....... c = {'a': 1, 'b': ...}\n"

    with patch.object(sys, 'stdout') as mock_print:
        with pysnooper.snoop(watch=('a', 'b', 'c'), normalize=True):
            a = [1, 2, 3]
            b = [[1,2], [2,3]]
            c = {'a': 1, 'b': 2}
            assert mock_print.call_args[0][0] == normalize_output

test_Tracer()

snoop = Tracer

# Generated at 2022-06-12 19:52:52.572420
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    print('Testing test_Tracer_trace ...', end='')
    with pysnooper.snoop('out.log'):
        for i in range(10):
            print(i)
    print('Done!')

test_Tracer_trace()


# Generated at 2022-06-12 19:52:59.999802
# Unit test for method trace of class Tracer
def test_Tracer_trace():
  depth = 1
  target = Tracer(output="", watch = (), watch_explode = (), depth = depth, 
                    prefix = "", overwrite = False, thread_info = False,
                    custom_repr = (), max_variable_length = 100, normalize = False,
                    relative_time = False)
  frame = frame = inspect.currentframe().f_back
  target_codes = set()
  target_frames = set()
  target_codes.add(frame.f_code)
  target_frames.add(frame)
  target.target_codes = target_codes
  target.target_frames = target_frames
  stack = []
  stack.append(sys.gettrace())
  thread_local = threading.local()
  thread_local.__dict__.setdefault('original_trace_functions', stack)


# Generated at 2022-06-12 19:53:03.370225
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def f():
        pass
    tracer = Tracer(None)
    obj = tracer(f)
    assert callable(obj)


# Generated at 2022-06-12 19:53:12.973911
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    output = io.StringIO()
    watch = (
        'maximum_length_of_all_the_variables_in_the_decorated_function',
    )
    tracer = Tracer(output, watch=watch)

    def _get_frame(**kwargs):  # pragma: no cover
        frame = types.FrameType(
            f_code=types.CodeType(
                co_argcount=0,
            ),
            f_globals={'__name__': kwargs.get('__name__', '__main__')},
        )
        frame.f_lineno = kwargs.get('f_lineno', 1)
        frame.f_lasti = kwargs.get('f_lasti', 1)

# Generated at 2022-06-12 19:53:14.126328
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    assert True

# Generated at 2022-06-12 19:53:16.391795
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    try:
        with Tracer():
            pass
    except Exception as e:
        print("{}".format(e))

# Generated at 2022-06-12 19:53:27.176472
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f(x):
        y = x
        return y
    f_filename = inspect.getsourcefile(f)
    f_source = inspect.getsource(f)
    frame = sys._getframe()
    while frame.f_code.co_name != 'f':
        frame = frame.f_back
    (path, source) = get_path_and_source_from_frame(frame)
    assert path == f_filename
    assert source == f_source.splitlines()
test_get_path_and_source_from_frame()
del test_get_path_and_source_from_frame



# Generated at 2022-06-12 19:53:38.856047
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    expected = (
        u'Source path:... ' + __file__ + '\n'
        u'    ' + 'Starting var:.. i = 5' + '\n'
        u'    ' + '    ' + 'Starting var:.. n = 12' + '\n'
        u'    ' + '    ' + '    ' + 'Starting var:.. s = "Hello"' + '\n'
    )
    capture_output = pysnooper.capture()
    with capture_output():
        with Tracer(watch=('i', 'n', 's')):
            i = 5
            with Tracer(watch=('i', 'n', 's')):
                n = 12
                with Tracer(watch=('i', 'n', 's')):
                    s = 'Hello'
    assert capture_output

# Generated at 2022-06-12 19:53:50.427139
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import StringIO
    from pysnooper.utils import get_write_function
    import inspect
    import os
    import threading
    import functools
    import sys
    import traceback
    from pysnooper import pycompat
    from pysnooper import BaseVariable
    from pysnooper import CommonVariable
    from pysnooper import Exploding
    old_output = sys.stdout
    sys.stdout = StringIO.StringIO()
    output = sys.stdout
    overwrite = True
    write = get_write_function(output, overwrite)
    assert write is not None, 'Write can not be none.'
    watch = ()
    watch_explode = ()
    depth = 1
    prefix = ''
    thread_info = False
    custom_repr = ()

# Generated at 2022-06-12 19:55:35.086588
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    import os
    tempdir = tempfile.mkdtemp()
    temp_path = os.path.join(tempdir, 'test.txt')
    file_writer = FileWriter(temp_path, overwrite=True)
    assert not os.path.isfile(temp_path)
    file_writer.write('abc')
    assert os.path.isfile(temp_path)
    assert open(temp_path).read() == 'abc'
    file_writer = FileWriter(temp_path, overwrite=False)
    file_writer.write('def')
    assert os.path.isfile(temp_path)
    assert open(temp_path).read() == 'abcdef'
    file_writer = FileWriter(temp_path, overwrite=False)
    file_writer.write('ghi')

# Generated at 2022-06-12 19:55:42.395517
# Unit test for method trace of class Tracer

# Generated at 2022-06-12 19:55:52.408296
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    global DISABLED
    from . import thread_utils
    # key stubs
    output = None
    watch =  'watch'
    watch_explode =  'watch_explode'
    depth =  1
    prefix = ''
    overwrite =  False
    thread_info =  False
    custom_repr =  'custom_repr'
    max_variable_length =  100
    normalize =  False
    relative_time =  False
    # mock dependencies and attributes
    get_write_function = unittest.mock.MagicMock()
    get_write_function.return_value = None
    inspect = unittest.mock.MagicMock()
    inspect.currentframe.return_value = 'currentframe'
    inspect.currentframe.return_value.f_back = 'f_back'

# Generated at 2022-06-12 19:55:58.619207
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer(output=None, watch=(), watch_explode=(), depth=10, prefix='',
                    overwrite=False, thread_info=False, custom_repr=(), max_variable_length=100,
                    normalize=False)
    # tracer.target_codes = set()
    # tracer.target_frames = set()
    tracer.start_times = {}
    # tracer.thread_local = threading.local()
    # tracer.last_source_path = None
    tracer.write = mock.Mock(return_value=None)
    tracer.__exit__(None, None, None)
    tracer.write.assert_called_with('    Elapsed time: 0:00:00')
