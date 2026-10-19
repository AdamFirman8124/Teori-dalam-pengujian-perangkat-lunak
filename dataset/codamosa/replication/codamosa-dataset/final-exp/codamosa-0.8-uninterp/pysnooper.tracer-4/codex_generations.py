

# Generated at 2022-06-12 19:46:36.197609
# Unit test for function get_local_reprs
def test_get_local_reprs():
    assert get_local_reprs(frame=None).items() == []
    def func():
        pass
    frame = func.__code__.co_firstlineno
    assert get_local_reprs(frame).items() == []
    assert get_local_reprs(frame=None,
                           watch=[CommonVariable('spam')]).items() == [('spam', '')]



# Generated at 2022-06-12 19:46:44.779789
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    tracer = Tracer(overwrite=False, depth=2, prefix='PREFIX ')
    class A(object):
        def one(self):
            return 1
    a = A()
    a.one.__globals__['pysnooper'] = pysnooper
    a.one.__globals__['DISABLED'] = DISABLED
    a.one.__globals__['tracer'] = tracer
    a.one.__code__ = pysnooper.snoop(watch = ('abc',), watch_explode = (1,)).__init__.__code__
    a.one.__code__.co_filename = tracer._is_internal_frame.__code__.co_filename
    a.one.__code__.co_firstlineno = 26

# Generated at 2022-06-12 19:46:49.101716
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
  # It is recommended that you use pytest.importorskip to avoid slow tests
  # on installations that don't have Pytest installed.
  pytest.importorskip("pytest")
  assert True

# Generated at 2022-06-12 19:46:54.533185
# Unit test for constructor of class Tracer
def test_Tracer():

    result = io.StringIO()

    with Tracer(output=result, watch='spam') as tracer:
        tracer
        spam = 'eggs'
        1/0

    expected = (
        'Source path:... {0}\n'
        '    00:00:00.000001 call        3   spam = "eggs"\n'
        '    00:00:00.000002 exception   4   Exception:..... division by zero\n'
        '    00:00:00.000003 return      5   Call ended by exception\n'
        '        Elapsed time: 0:00:00.000002'
    ).format(__file__)
    assert result.getvalue() == expected

# Generated at 2022-06-12 19:46:58.996406
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_the_function(func):
        frame = sys._getframe(1)
        return get_path_and_source_from_frame(frame)
    # Test that it works on a simple function with no arguments:
    assert test_the_function(test_the_function)



# Generated at 2022-06-12 19:47:10.051158
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import inspect
    # No need to use the test 'self' parameter
    def test_Tracer___exit__self():
        def inner():
            caller = inspect.stack()[1]
            code = caller.code_context[0]
            frame = caller.frame
            exc_type = exc_value = exc_traceback = None
            # Arrange
            tracer = Tracer()
            tracer.depth = 1
            tracer.thread_info = False
            tracer.thread_info_padding = 0
            tracer.target_codes = set()
            tracer.frame_to_local_reprs = {}
            frame_to_local_reprs = {}
            tracer.start_times = {}
            start_times = {}
            tracer.target_frames = set()
            tracer.last_source_

# Generated at 2022-06-12 19:47:12.028861
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import unittest
    class Tracer___exit___Test(unittest.TestCase):
        pass
    # TODO


# Generated at 2022-06-12 19:47:13.000464
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    return



# Generated at 2022-06-12 19:47:23.524403
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import doctest
    (failure_count, test_count) = doctest.testmod(utils)
    assert not failure_count, 'doctest failed in source.py'

    for test_case in (utils.TestCase, utils.TestCaseWithCustomRepr):
        __traceback_hide__ = True
        class FakeLoader(object):
            def __init__(self, source):
                self.source = source
            def get_source(self, module_name):
                return self.source
        #                                          012345678901234567890123
        test_case.assertEqual(get_path_and_source_from_frame(
            inspect.currentframe())[0], __file__)

# Generated at 2022-06-12 19:47:31.430821
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import io
    import unittest
    import unittest.mock
    from pysnooper import tracer
    from pysnooper.tracer import Tracer

    class Dummy:
        pass

    class Test(unittest.TestCase):
        def setUp(self):
            self.mock_write = unittest.mock.Mock()
            self.mock_write.return_value = None
            self.mock_output = unittest.mock.Mock()
            self.mock_output.write = self.mock_write

        def test__exit__01(self):
            '''Make sure things work with a simple function.
            '''
            mock_output = io.StringIO()
            mock_snoop = Tracer(output=mock_output)

# Generated at 2022-06-12 19:48:23.450401
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f():
        x = 2
        y = 3
        return x + y

    assert get_local_reprs(f.__code__.co_consts[-1].co_frame) == {
        'x': '2', 'y': '3'
    }
    assert get_local_reprs(f.__code__.co_consts[-1].co_frame, [
        CommonVariable('z', lambda frame: frame.f_locals['x'] + frame.f_locals['y'])
    ]) == {'x': '2', 'y': '3', 'z': '5'}



# Generated at 2022-06-12 19:48:36.806865
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():

    c = Tracer()
    c.target_frames = {1:2,}
    c.frame_to_local_reprs = {1:2,}
    c.start_times = {1:2,}
    c.depth = 1
    c.target_codes = {1:2,}
    c.prefix = "Tracer"
    c.thread_info = True
    c.thread_info_padding = 0
    c.thread_local = threading.local()
    c.last_source_path = "C:\\Users\\Dario\\Desktop\\File.txt"
    c.max_variable_length = 100
    c.normalize = False
    c.relative_time = False

    try:
        with c:
            pass
    except Exception:
        pass

    assert c.target_frames

# Generated at 2022-06-12 19:48:39.419310
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    output = io.StringIO()
    with Tracer(output=output):
        pass
    return output.getvalue().strip()
test_Tracer___exit__()


# Generated at 2022-06-12 19:48:47.066985
# Unit test for constructor of class Tracer
def test_Tracer():
    t = Tracer(watch=('var1', 'var2'),
               watch_explode=('var3', 'var4'),
               depth=4,
               prefix='///',
               thread_info=True,
               custom_repr=('var1', 'var2'))

    assert t.watch == [CommonVariable('var1'), CommonVariable('var2'),
        Exploding('var3'), Exploding('var4')]
    assert t.depth == 4
    assert t.prefix == '///'
    assert t.thread_info == True


# Generated at 2022-06-12 19:48:56.794481
# Unit test for function get_local_reprs
def test_get_local_reprs():
    assert get_local_reprs({'a': 1, 'b': 2}, watch=[CommonVariable('a'), CommonVariable('b')]) == {'a': '1', 'b': '2'}
    assert get_local_reprs({'a': 1, 'b': 2, 'c': 3}, watch=[CommonVariable('a'), CommonVariable('b')]) == {'a': '1', 'b': '2'}
    assert get_local_reprs({'a': 1, 'b': 2}, watch=[CommonVariable('a'), CommonVariable('b'), CommonVariable('c')]) == {'a': '1', 'b': '2', 'c': ''}

# Generated at 2022-06-12 19:49:06.691112
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer(prefix='@ ')
    frame = inspect.currentframe()
    thread_global.depth = 0
    tracer.target_codes = {func.__code__: None for func in [add]}
    tracer.target_frames.add(frame)
    tracer.target_frames.add(frame.f_back)
    tracer.start_times[frame] = datetime_module.datetime.now()
    tracer.start_times[frame.f_back] = tracer.start_times[frame]
    tracer.frame_to_local_reprs[frame] = {
        'a': '100',
        'b': '200'
    }

# Generated at 2022-06-12 19:49:15.922774
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer(watch=('self',))
    frame = Frame(tracer.watch)
    frame.locals['self'] = 'TEST'
    tracer.start_times[frame] = datetime_module.datetime.now()
    tracer.frame_to_local_reprs[frame] = {}
    thread_global.depth = 0
    tracer.target_codes.add(frame.code)
    tracer.target_frames.add(frame)
    tracer.trace(frame, 'call', None)
    assert tracer.frame_to_local_reprs[frame] == {'self': '"TEST"'}
    tracer.trace(frame, 'return', 'RETURN')
    assert tracer.start_times[frame] is None

# Generated at 2022-06-12 19:49:28.096526
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # Test function to be decorated
    def foo():
        pass

    # Call the decorated function
    with Tracer(overwrite=True)(foo)():
        pass

    # Check output format
    expected_output = """Starting var:.. foo = <function foo at 0x{foo_hex}>
Source path:... {foo_path}
Elapsed time: {elapsed_time}
"""

    with open(outfile.name, 'r') as f:
        output = f.read()

    assert output.strip() == expected_output.format(
        foo_hex=hex(id(foo)), foo_path=foo.__code__.co_filename,
        elapsed_time=pycompat.timedelta_format(datetime_module.timedelta(seconds=0))
        )


# Generated at 2022-06-12 19:49:29.614995
# Unit test for constructor of class Tracer
def test_Tracer():
    t = Tracer()
    assert isinstance(t, Tracer)
    return


# Generated at 2022-06-12 19:49:40.824943
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer(watch=('x', 'y'), max_variable_length=100)
    tracer.depth = 1
    tracer.write = mock.Mock()
    tracer.write.return_value = None
    tracer.set_thread_info_padding = mock.Mock()
    tracer.set_thread_info_padding.side_effect = utils._dummy
    frame = mock.Mock()
    frame.f_code.co_filename = '/source code name.py'
    frame.f_lineno = 10
    frame.f_code.co_code = [b'\x00']
    frame.f_back = mock.Mock()
    frame.f_back.f_code.co_filename = 'test_snoop.py'

# Generated at 2022-06-12 19:50:07.777230
# Unit test for constructor of class Tracer
def test_Tracer():
    import six
    import io
    from pysnooper.variable import CommonVariable, Exploding, Attribute, Item
    from pysnooper import pycompat

    output = six.StringIO()
    value_repr = lambda v: '{}'.format(v)
    Tracer(output, watch=('foo', 'bar'), watch_explode=(), depth=2,
           prefix='ZZZ ', overwrite=False, thread_info=False,
           custom_repr=((type, value_repr),),
           max_variable_length=100, relative_time=False, normalize=False)

    assert isinstance(output, pycompat.file)
    assert isinstance(Tracer.watch[0], CommonVariable)
    assert isinstance(Tracer.watch[1], CommonVariable)

# Generated at 2022-06-12 19:50:11.887765
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def foo():
        pass

    snooped_foo = Tracer()(foo)
    assert snooped_foo is not foo
    assert snooped_foo.__name__ == foo.__name__
    assert snooped_foo.__doc__ == foo.__doc__
    assert snooped_foo.__module__ == foo.__module__
    # ensure no trace function set in context manager, when disabled
    with Tracer(overwrite=True) as t:
        assert t is None



# Generated at 2022-06-12 19:50:19.854760
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def test_function(x, y):
        with pysnooper.snoop():
            a = x + y
            b = x + 1
            c = y + 1
            return max(a, b, c)

    test_function(1, 2)
    test_function(x=1, y=2)
    test_function(1, 2)
    test_function(y=2, x=1)
    test_function(3, 2)
    test_function(3, x=2)
    test_function(3, y=2)
    test_function(3, y=x)


# Generated at 2022-06-12 19:50:27.063974
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    with open(r"test_Tracer.txt", "r") as f:
        data=f.read()
        lines = data.split("\n")
        code=pycompat.StringIO(data)
        code_f = code.read()
        code = pycompat.StringIO(code_f)
        def test_fun():
            return 1
        tracer = Tracer(watch_explode=('self'))
        tracer.thread_info = False
        tracer.trace = Tracer.trace
        tracer.normalize = False
        frame = inspect.currentframe()
        frame_f = inspect.currentframe().f_back

# Generated at 2022-06-12 19:50:33.304113
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global DISABLED
    DISABLED = False
    t1 = Tracer()
    t1.watch_explode = ('foo')
    t1.watch = ('bar')
    t1.depth = 2
    t1.prefix = ''
    t1.overwrite = False
    t1.thread_info = True
    t1.custom_repr = ()
    t1.max_variable_length = 100
    t1.normalize = True
    t1.relative_time = True
    t1.target_codes = set()
    t1.target_frames = set()
    t1.thread_local = threading.local()
    t1.last_source_path = None
    t1.thread_info_padding = 0
    # the call to t1.trace is commented out because it has side effects,

# Generated at 2022-06-12 19:50:34.223621
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass


# Generated at 2022-06-12 19:50:34.883559
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass

# Generated at 2022-06-12 19:50:38.467425
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f():
        x = 5
        print('x is ' + repr(x))

    try:
        f()
    except:
        assert get_local_reprs(sys.exc_info()[2].tb_frame) == {'x': '5'}



# Generated at 2022-06-12 19:50:46.323366
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import io
    import types
    import pytest
    from . import utils
    from .utils import get_write_function
    from . import pysnooper
    from .watch import CommonVariable
    from .watch import Exploding
    from .watch import BaseVariable
    import pycompat
    import inspect
    import functools
    import threading
    import datetime
    import sys
    import traceback
    from . import opcode
    from .utils import get_path_and_source_from_frame

    def test_tracer_watch_explode():
        stream = io.StringIO()

        @pysnooper.snoop(stream, watch='foo', watch_explode=('bar', 'baz'))
        def foo():
            foo = 1

# Generated at 2022-06-12 19:50:51.834970
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Setup
    tracer = Tracer()
    tracer.write = mock.MagicMock(return_value=None)

    # Exercise
    tracer.__exit__(None, None, None)

    # Verify
    tracer.write.assert_called_once_with('    Elapsed time: 0:00:00')

    # Cleanup
    del tracer

# Generated at 2022-06-12 19:51:15.137694
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def g():
        pass
    def f():
        g()
    path, source = get_path_and_source_from_frame(sys._getframe(1))
    expected_path = os.path.splitext(__file__)[0] + '.py'
    expected_source = open(expected_path).read().splitlines()
    assert path == expected_path
    assert source == expected_source
# Attempt to retrieve the source code for the given frame object.
#
# If inspect.getsourcelines is able to retrieve source code, then the
# resulting list of lines is returned. Otherwise, None is returned.


# Generated at 2022-06-12 19:51:23.353984
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        pass
    frame_info = inspect.getframeinfo(foo.__code__)
    assert get_path_and_source_from_frame(frame_info) == (
        utils.get_source_file_name(foo),
        list(open(utils.get_source_file_name(foo)))
    )
    try:
        raise ValueError
    except ValueError:
        frame_info = inspect.getframeinfo(sys.exc_info()[2].tb_frame)

# Generated at 2022-06-12 19:51:27.734472
# Unit test for constructor of class Tracer
def test_Tracer():
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        with Tracer(output=f):
            pass
    f.seek(0)
    assert f.read().decode('utf-8').strip() == 'Source path:... /path/to/file.py'


# Generated at 2022-06-12 19:51:37.692913
# Unit test for method trace of class Tracer
def test_Tracer_trace():

    global snoop_exc_info

    def make_snooper(depth=1, prefix='', overwrite=False, thread_info=False,
                     custom_repr=(), max_variable_length=100,
                     normalize=False, relative_time=False):
        snoop = Tracer(output=sys.stdout, depth=depth, prefix=prefix,
                       overwrite=overwrite, thread_info=thread_info,
                       custom_repr=custom_repr,
                       max_variable_length=max_variable_length,
                       normalize=normalize, relative_time=relative_time)
        return snoop

    snoop_exc_info = None
    def custom_repr(v):
        def snoop_repr(v):
            return str(v) + '!'


# Generated at 2022-06-12 19:51:38.141636
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass

# Generated at 2022-06-12 19:51:49.818250
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, 'FileWriter_write')
        writer = FileWriter(filename, True)
        writer.write('hi')
        writer.write('bye')
        with open(filename, encoding='utf-8') as f:
            assert f.read() == 'hi'
        writer = FileWriter(filename, False)
        writer.write('hi')
        writer.write('bye')
        with open(filename, encoding='utf-8') as f:
            assert f.read() == 'hibye'
        writer = FileWriter(filename, True)
        writer.write('hi')
        with open(filename, encoding='utf-8') as f:
            assert f.read() == 'hi'



# Generated at 2022-06-12 19:52:00.613500
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    class TestTracer___call__(unittest.TestCase):
        def setUp(self):
            pass
        def test_1(self):
            # Test with string
            output = StringIO()
            def foo_1(a, b=3, *c, **d):
                e = f = 3
                return 1 + 2

            with pysnooper.snoop(output):
                foo_1(1, 2, e=1, f=1)

# Generated at 2022-06-12 19:52:09.321264
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Issue #46: Variable listing does not show up on subsequent lines in loop
    code = pycompat.compile('''
        def foo():
            i = 0
            while i < 3:
                i += 1
    ''', '<string>', 'exec')

    tracer = Tracer(watch=['i', 'i < 3'], max_variable_length=None)
    frame = sys.modules[__name__].__dict__.copy()
    frame['Tracer'] = Tracer
    frame['code'] = code
    frame['__builtins__'] = {}
    exec(code, frame)
    with tracer:
        frame['foo']()

# Generated at 2022-06-12 19:52:15.562993
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    path = utils.get_this_module_dir() / 'test_output'
    path.write_bytes(b'')

    FileWriter(path, overwrite=True).write(u'foo')
    assert path.read_bytes() == b'foo'

    FileWriter(path, overwrite=True).write(u'bar')
    assert path.read_bytes() == b'bar'

    FileWriter(path, overwrite=False).write(u'baz')
    assert path.read_bytes() == b'barbaz'



# Generated at 2022-06-12 19:52:18.147806
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    @pysnooper.snoop()
    def add(a, b):
        c = a + b
        return c
    return None


# Generated at 2022-06-12 19:53:05.570169
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    try:
        import pytest
    except ImportError:
        pytest = None

    if pytest is None:
        return
    from . import compat
    from . import utils

    @pytest.fixture
    def tracer():
        return Tracer(overwrite=True)

    def test_write_elapsed_time(tracer):
        elapsed_time = datetime_module.timedelta(microseconds=500000)
        with tracer:
            compat.sleep(elapsed_time.total_seconds())
        # XXX: This doesn't work on Windows
        assert bool(re.search(r'Elapsed time: \d+ \w+s',
                              compat.get_output()))


# Generated at 2022-06-12 19:53:13.215169
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():  
    tracer = Tracer()
    tracer.depth = 1
    tracer.write = mock.MagicMock()
    now = datetime_module.datetime.now()
    tracer.start_times = {now : now}
    tracer.frame_to_local_reprs = {now : {'now': now}}
    tracer.__exit__(None, None, None)

    tracer.write.assert_called_once_with('    Elapsed time: 0:00:00.000000')
    assert tracer.start_times == {}
    assert tracer.frame_to_local_reprs == {}


# Generated at 2022-06-12 19:53:24.923963
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pytest
    import pysnooper
    def to_be_instrumented():
        return 1
    def to_be_instrumented_generator():
        yield 1
    def not_instrumented():
        with pysnooper.snoop():
            return 1
    with pytest.raises(NotImplementedError):
        def to_be_instrumented_coroutine():
            return
        pysnooper.snoop()(to_be_instrumented_coroutine)
    with pytest.raises(NotImplementedError):
        def to_be_instrumented_async_generator():
            yield 1
        pysnooper.snoop()(to_be_instrumented_async_generator)
    assert to_be_instrumented() == 1

# Generated at 2022-06-12 19:53:29.226589
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # If a call ends due to an exception, we still get a 'return' event
    # with arg = None. This seems to be the only way to tell the difference
    # https://stackoverflow.com/a/12800909/2482744
    assert case_test.test_Tracer___exit__()

# Generated at 2022-06-12 19:53:39.553094
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # -------------------------------------------------------------------------
    # Test code
    from datetime import timedelta
    from contextlib import contextmanager

    @contextmanager
    def timer(label):
        start = datetime_module.datetime.now()
        yield
        duration = datetime_module.datetime.now() - start
        print(f'{label} duration: {pycompat.timedelta_format(duration)}')

    # -------------------------------------------------------------------------
    # Test code end
    print(f'{datetime_module.datetime.now().time()} start')
    with timer('outer timer'):
        with timer('inner timer'):
            with timer('inner-inner timer'):
                with timer('inner-inner-inner timer'):
                    print(f'do nothing')
            print(f'do nothing')
        print(f'do nothing')
   

# Generated at 2022-06-12 19:53:51.400312
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    func = Tracer.__init__
    def test_empty1(self):
        self.target_codes = set()
        self.target_frames = set()
        self.start_times = {}
        thread_global.depth = -1
        self.frame_to_local_reprs = {}
        self.thread_local = threading.local()
        frame = pysnooper.utils.get_frame(depth=2)

# Generated at 2022-06-12 19:53:58.614713
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import unittest
    from test.test_support import captured_stderr

    class Tracer___call__Test(unittest.TestCase):
        def test_should_set_f_trace_to_trace_when_applied_to_function(self):
            def foo():
                pass
            tracer = Tracer()
            tracer(foo)
            self.assertTrue(hasattr(foo, 'f_trace'))
            self.assertEqual(foo.f_trace.__name__, 'trace')

        def test_should_return_decorated_function_as_is(self):
            def foo():
                pass
            tracer = Tracer()
            result = tracer(foo)
            self.assertEqual(result, foo)


# Generated at 2022-06-12 19:54:03.569901
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class Foo(object):
        @pysnooper.snoop(prefix='*** ')
        def bar(self):
            for i in range(5):
                i += 2
                print(i)
            return 'done'

    foo = Foo()
    foo.bar()


# Generated at 2022-06-12 19:54:11.011667
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def _test_get_path_and_source_from_frame():
        frame = sys._getframe(0)
        result = get_path_and_source_from_frame(frame)
        assert result[0] == __file__
        this_file_source = open(__file__, 'rb').read().splitlines()
        assert result[1] == this_file_source
    _test_get_path_and_source_from_frame()
    del _test_get_path_and_source_from_frame



# Generated at 2022-06-12 19:54:13.461712
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # Setup
    def decorator_function(function):
        return function
    function_or_class = decorator_function
    tracer = Tracer()
    # Exercise
    tracer.__call__(function_or_class)
    # Verify


# Generated at 2022-06-12 19:55:46.513301
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        import inspect
        frame = inspect.currentframe()
        path_and_source = get_path_and_source_from_frame(frame)
        assert isinstance(path_and_source[0], pycompat.string_types)
        assert path_and_source[0].endswith('.py')
        assert isinstance(path_and_source[1], list)
    foo()



# Generated at 2022-06-12 19:55:55.309485
# Unit test for function get_local_reprs
def test_get_local_reprs():
    def f1(x, y=5):
        a = []
        a.append(b)
        return locals()
    frame1 = f1.__code__.create_frame(dict(), f1.__defaults__, f1.__globals__)
    assert get_local_reprs(frame1) == {
        'x': '<frame argument>',
        'y': '<frame argument>',
        'a': '[]',
        'b': '<undefined>',
    }

# Generated at 2022-06-12 19:56:05.444517
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pickle
    tracer = Tracer()
    tracer.__dict__["watch"] = []
    tracer.__dict__["watch_explode"] = []
    tracer.__dict__["depth"] = 1
    tracer.__dict__["prefix"] = ""
    tracer.__dict__["overwrite"] = False
    tracer.__dict__["thread_info"] = False
    tracer.__dict__["custom_repr"] = ()
    tracer.__dict__["max_variable_length"] = 100
    tracer.__dict__["normalize"] = False
    tracer.__dict__["relative_time"] = False
    from io import StringIO
    tracer._write = StringIO()
    tracer.__dict__["frame_to_local_reprs"] = {}
    tr