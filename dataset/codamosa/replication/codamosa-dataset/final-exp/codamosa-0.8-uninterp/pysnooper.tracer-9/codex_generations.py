

# Generated at 2022-06-12 19:46:47.926774
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    #
    # Called from the decorator, with a frame that is two levels above
    #
    tracer = Tracer()
    tracer.depth = 1
   
    def frame_to_use(offset=2):
        return inspect.currentframe(offset + 1)

    def check(expected_set, code_name, event, arg, code_byte=None):
        result = tracer.trace(frame_to_use(), event, arg)
        assert expected_set == set(tracer.target_codes)
        assert code_name == frame_to_use().f_code.co_name

    check(set(), 'code_a', 'call', None)
    check(set(), 'code_b', 'call', None)

# Generated at 2022-06-12 19:46:49.000615
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass


# Generated at 2022-06-12 19:46:53.498336
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    t = Tracer()
    test_exc_type = Exception
    test_exc_value = "test message"
    t.__exit__(test_exc_type, test_exc_value, None)
    assert True # TODO: implement your test here


# Generated at 2022-06-12 19:47:02.130015
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # Test with filename:
    def some_function():
        pass
    frame = some_function.__code__.co_filename, some_function.__code__.co_firstlineno
    file_name, source = get_path_and_source_from_frame(frame)
    assert file_name == inspect.getsourcefile(some_function)
    assert source[0].startswith('def some_function')

    # Test with ipython filename:
    class SomeClass(object):
        __module__ = '__main__'
    frame = '<ipython-input-21-e5f5e5a5f5>', 1
    file_name, source = get_path_and_source_from_frame(frame)

# Generated at 2022-06-12 19:47:12.297359
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    global max_variable_length
    max_variable_length = 100
    with Tracer(max_variable_length=max_variable_length) as tracer:
        x = 1 # 1.
        y = 2 # 2.
    with Tracer(max_variable_length=max_variable_length) as tracer:
        counter = 0 # 1.
        while counter < 5: # 2. 3. 4. 5.
            counter += 1
    with Tracer(max_variable_length=max_variable_length) as tracer:
        class A:
            pass # 1.
    with Tracer(max_variable_length=max_variable_length) as tracer:
        def f():
            pass # 1.

# Generated at 2022-06-12 19:47:23.138279
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    saved_disabling_condition = DISABLED

# Generated at 2022-06-12 19:47:26.081286
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    t = Tracer(depth=2, thread_info=True)
    class C:
        def run(foo):
            bar = 2
            return bar
    c = C()
    d = t(C)
    d.run()

# Generated at 2022-06-12 19:47:29.754623
# Unit test for function get_write_function
def test_get_write_function():
    for output in (None, utils.StringIO(), open('a.txt', 'w'), utils.StringIO(), open('b.txt', 'w'), 'c.txt', 'd.txt'):
        for overwrite in (False, True):
            write = get_write_function(output, overwrite)
            write('hello, world!\n')



# Generated at 2022-06-12 19:47:32.798431
# Unit test for constructor of class Tracer
def test_Tracer():
    # Tracer()
    with Tracer() as tracer:
        pass
# Internally, Tracer is only called in the following two functions
# Tracer() is only called in the following two functions
# Decorator and DecoratorClass

# Generated at 2022-06-12 19:47:34.347008
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def function():
        pass
    return function

# Generated at 2022-06-12 19:47:58.653960
# Unit test for constructor of class Tracer
def test_Tracer():
    from io import StringIO
    from pysnooper.tracer import Tracer, DISABLED
    old_disabled = DISABLED
    DISABLED = False
    try:
        def foo(a, b=3):
            loc = locals()['b']
            c = a + loc
            return c
        output = StringIO()
        watch = ('a', 'c', 'loc', 'b')
        tracer = Tracer(watch=watch, output=output)
        with tracer:
            ret = foo(1)
    finally:
        DISABLED = old_disabled

    output_list = output.getvalue().split('\n')
    assert ret == 4
    assert output_list[2] == '  New var:....... a = 1'

# Generated at 2022-06-12 19:48:01.698173
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert get_path_and_source_from_frame(inspect.currentframe())[0] \
           == os.path.abspath(__file__) == os.path.abspath(sys.argv[0])



# Generated at 2022-06-12 19:48:12.388549
# Unit test for constructor of class Tracer
def test_Tracer():
    global DISABLED
    DISABLED = True
    tracer_instance = Tracer()
    assert tracer_instance.watch == ()
    assert tracer_instance.start_times == {}
    assert tracer_instance.depth == 1
    assert tracer_instance.prefix == ''
    assert tracer_instance.thread_info == False
    assert tracer_instance.thread_info_padding == 0
    assert tracer_instance.target_codes == set()
    assert tracer_instance.target_frames == set()
    assert tracer_instance.custom_repr == ()
    assert tracer_instance.max_variable_length == 100
    assert tracer_instance.last_source_path == None
    assert tracer_instance.normalize == False
    assert tracer_instance.relative_time == False

# Generated at 2022-06-12 19:48:15.998670
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    frame = inspect.currentframe()
    path, source = get_path_and_source_from_frame(frame)
    assert source[-1].strip() == u'''def test_get_path_and_source_from_frame():'''
    assert os.path.isfile(path)



# Generated at 2022-06-12 19:48:20.343910
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    snooper = Tracer()
    snooper.start_times[0] = 1
    snooper.frame_to_local_reprs[0] = {}
    with patch('pysnooper.pysnooper.datetime_module.datetime') as datetime:
        datetime.now.side_effect = [1, 2]
        snooper.__exit__(0, 0, 0)
    assert not snooper.start_times
    assert not snooper.frame_to_local_reprs


# Generated at 2022-06-12 19:48:21.326922
# Unit test for function get_path_and_source_from_frame

# Generated at 2022-06-12 19:48:27.153100
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import os
    import functools
    import sys
    import threading
    import traceback
    from pysnooper import pycompat
    from pysnooper import utils
    from pysnooper import get_write_function
    from pysnooper import opcode
    from pysnooper.utils import CommonVariable, Exploding, BaseVariable
    from pysnooper.utils import get_local_reprs
    from pysnooper.utils import get_path_and_source_from_frame
    class Tracer(object):
        DISABLED = False

# Generated at 2022-06-12 19:48:39.557025
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    test_Tracer_trace_watch_called, test_Tracer_trace_watching_called,\
    test_Tracer_trace_watch_explode_called, test_Tracer_trace_watching_explode_called =\
    False, False, False, False
    import unittest
    class TracerUnitTest(unittest.TestCase):
        def test_Tracer_trace_watch(self):
            def func():
                pass

            def TracerUnitTest_fake_get_local_reprs(frame,
                                                    watch=(),
                                                    custom_repr=(),
                                                    max_length=100):
                nonlocal test_Tracer_trace_watch_called
                test_Tracer_trace_watch_called = True
                return {}


# Generated at 2022-06-12 19:48:40.776936
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    pass


# Generated at 2022-06-12 19:48:50.363812
# Unit test for constructor of class Tracer
def test_Tracer():
    disabled = False
    watch = []
    watch_explode = ['foo']
    watch_explode += ['self']
    depth = 2
    prefix = 'ZZZ '
    overwrite = False
    thread_info = False
    custom_repr = ()
    custom_repr += ((type1, custom_repr_func1), )
    max_variable_length = 200
    normalize = False
    relative_time = False
    output = None
    write = get_write_function(output, overwrite)
    _write = write
    # _write = write
    print(_write)
    print(getattr(write,'__code__'))
    print(getattr(write,'__globals__'))
    print(getattr(getattr(write,'__code__'),'co_filename'))

# Generated at 2022-06-12 19:49:18.866808
# Unit test for constructor of class Tracer
def test_Tracer():
    mock_output = Mock()
    tracer = Tracer(output=mock_output, watch='a',
                    watch_explode=('b',), depth=2,
                    prefix='PPP ', overwrite=False, thread_info=True,
                    normalize=False, relative_time=True,
                    max_variable_length=200,
                    custom_repr=(
                    (str, lambda s: 'string'),
                    (lambda: 1/0, lambda e: 'exception'),
                    ))
    assert isinstance(tracer.watch[0], CommonVariable)
    assert tracer.watch[0].name == 'a'
    assert isinstance(tracer.watch[1], Exploding)
    assert tracer.watch[1].name == 'b'
    assert tracer.depth == 2

# Generated at 2022-06-12 19:49:29.639082
# Unit test for function get_write_function
def test_get_write_function():
    import pycompat
    import os.path
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        temp_filename = fp.name
        fp.write(b'')

# Generated at 2022-06-12 19:49:33.871633
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # It's not really a unit test, more a test of an integration of the whole
    # program, because it requires that you run it.
    #
    # I might move this to test with a separate file, e.g.
    # test_integration_enter.py or whatever.
    def f():
        return 1 + 2
    with Tracer():
        assert f() == 3


###################
# Exported stuff: #
###################


# Generated at 2022-06-12 19:49:43.859309
# Unit test for method __call__ of class Tracer

# Generated at 2022-06-12 19:49:47.927505
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    '''Test for method `__enter__` of class `Tracer`.'''
    output = StringIO()
    with Tracer(output):
        pass
    return output.getvalue()

# Generated at 2022-06-12 19:49:49.326449
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass



# Generated at 2022-06-12 19:49:50.285843
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect

# Generated at 2022-06-12 19:49:56.981916
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    from .pycompat import PathLike

    file_name = 'output.txt'
    content = utils.shitcode('helloworld')
    file_writer = FileWriter(file_name, overwrite=True)
    # Write with overwrite=True
    file_writer.write(content)
    assert isinstance(file_name, PathLike)
    assert content in open(file_name, encoding='utf-8').read()
    # Write with overwrite=False
    file_writer.write(content)
    assert isinstance(file_name, PathLike)
    assert content*2 in open(file_name, encoding='utf-8').read()



# Generated at 2022-06-12 19:50:01.486628
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_function():
        pass
    result = get_path_and_source_from_frame(
        sys._getframe(1)
    )
    expected = (__file__, open(__file__, 'rb').read().splitlines())
    assert result == expected



# Generated at 2022-06-12 19:50:08.809227
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer(watch=('x', 'y','z'))
    def f(x, y=1, z=2):
        return x+y+z
    frame = inspect.currentframe()
    frame.f_code = f.__code__
    frame.f_locals = {'y': 3, 'z':4, 'x':5}
    tracer.trace(frame, "call", None)
    tracer.trace(frame, "return", None)
    assert frame.f_locals['x'] == 5
    assert frame.f_locals['y'] == 3
    assert frame.f_locals['z'] == 4


# Generated at 2022-06-12 19:50:31.475829
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # self = <pysnooper.snooper.Tracer object at 0x7fa3edc34da0>
    # exc_type = None
    # exc_value = None
    # exc_traceback = None
    # Calling method __exit__ of parent class Tracer
    super(Tracer, self).__exit__(exc_type,exc_value,exc_traceback) # real signature unknown; restored from __doc__
    # type: (type, object, object) -> object
    # END OF TEST



# Generated at 2022-06-12 19:50:40.468069
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    class MyClass(object):
        def __init__(self):
            self.foo = 1

        @pysnooper.snoop()
        def method(self):
            """Test method."""
            self.foo = 2
            return self.foo

        @staticmethod
        @pysnooper.snoop()
        def static_method():
            """Another test method."""
            return 1

        @classmethod
        @pysnooper.snoop()
        def class_method(cls):
            """Yet another test method."""
            return 1

        @property
        @pysnooper.snoop()
        def property_method(self):
            """Property method."""
            return 1


# Generated at 2022-06-12 19:50:47.403812
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pysnooper
    import threading
    import sys
    import inspect
    import functools
    disable = None
    assert disable is None
    class pysnooper:
        class snoop:
            DISABLED = disable
            def __init__(self, output=None, watch=(), watch_explode=(), depth=1,
                        prefix='', overwrite=False, thread_info=False, custom_repr=(),
                        max_variable_length=100, normalize=False, relative_time=False):
                self._write = None
                self.watch = []
                self.frame_to_local_reprs = {}
                self.start_times = {}
                self.depth = 1
                self.prefix = ''
                self.overwrite = False
                self.thread_info = False
                self.thread

# Generated at 2022-06-12 19:50:56.792933
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import contextlib
    from types import ModuleType
    from . import utils
    from .test_utils import make_mock_frame

    def check_frame(frame_getter, file_name, source):
        with make_mock_frame(frame_getter) as frame:
            path, result_source = get_path_and_source_from_frame(frame)
            assert path == file_name
            assert result_source == source

    @contextlib.contextmanager
    def mock_module(source, **kwargs):
        module = ModuleType('mock_module')
        module.__dict__.update(kwargs)
        module.__file__ = 'mock_module.py'
        with utils.redirect_loader(module, source):
            yield

# Generated at 2022-06-12 19:50:58.390131
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pytest
    with pytest.raises(TypeError):
        import _pysnooper
        _pysnooper.Tracer.__exit__(Exception, None, None)

# Generated at 2022-06-12 19:51:09.351516
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import pycompat
    import inspect
    import functools
    import os
    import pycompat
    import opcode
    import threading
    class _threading_local:
        def __init__(self):
            self.__dict__['attr']=""
        def __setattr__(self,name,value):
            self.__dict__[name] = value
    thread_global = _threading_local()
    global DISABLED
    DISABLED = False
    class CommonVariable:
        def __init__(self, variable_name):
            self.name = variable_name

        def __repr__(self):
            return '<CommonVariable name={self.name}>'.format(**locals())


# Generated at 2022-06-12 19:51:17.112501
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def test_method1():
        a = 1
        b = 2
        c = a + b
        return c

    def test_method2():
        a = 1
        b = 2
        c = a + b
        return c

    def test_method3():
        a = 1
        b = 2
        c = a + b
        return c


    def test_method4():
        a = 1
        b = 2
        c = a + b
        return c

    def test_method5():
        a = 1
        b = 2
        c = a + b
        return c

    def test_method6():
        a = 1
        b = 2
        c = a + b
        return c


    def test_method7():
        a = 1
        b = 2

# Generated at 2022-06-12 19:51:18.065431
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    """__call__(self, function_or_class)"""
    # passing
    ##

# Generated at 2022-06-12 19:51:29.005487
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    print('Testing __exit__ ... ', end='')
    global DISABLED
    DISABLED = False

    class MyThread(threading.Thread):
        def __init__(self, tracer):
            self.tracer = tracer
            super().__init__()
        def run(self):
            with self.tracer:
                pass

    tracer = Tracer(watch=['a'], thread_info=True)
    thread = MyThread(tracer)
    thread.start()
    thread.join()
    assert 'Thread-1-' in tracer.thread_info_padding * ' '
    DISABLED = True
    print('Passed.')


# Generated at 2022-06-12 19:51:36.860138
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    class TestTracer(object):
        def __init__(self):
            self.test_data = dict(test_data_1=1,test_data_2=2,test_data_3=3,test_data_4=4)
            self.tracer = Tracer()

    test_obj = TestTracer()
    assert hasattr(test_obj, 'tracer')
    test_obj.tracer.__enter__()
    assert hasattr(test_obj.tracer, 'start_times')
    test_obj.tracer.__exit__(None, None, None)

# Generated at 2022-06-12 19:52:44.743058
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    tracer = Tracer()
    def test_function():
        a = '''def foo(bar):
    return bar + 1'''
    #print(type(a))
    with tracer:
        print('This is a test.')
    expect = '    This is a test.\n'
    actual = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    assert actual == expect

# Generated at 2022-06-12 19:52:46.900437
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import _pydevd_frame_eval
    def test_function():
        pass
    x=Tracer()
    y=x(test_function)
    assert y

# Generated at 2022-06-12 19:52:50.137487
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    a = Tracer()
    a.write = fakes.FakeWrite()
    a.start_times = [1]
    assert a.__exit__(1, 2, 3) == None
    assert a.thread_local.original_trace_functions == []
    assert a.frame_to_local_reprs == {}
    assert a.start_times == []
    assert sys.gettrace() == None


# Generated at 2022-06-12 19:53:00.704919
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    global m_frame, m_inspect, m_sys, m_thread_local, m_functools, m_DISABLED
    from unittest.mock import MagicMock, patch

    with patch.object(pysnooper, 'get_write_function', return_value=m_get_write_function) as mock_get_write_function:
        with patch.object(pysnooper, 'DISABLED', new_callable=PropertyMock) as mock_DISABLED:
            # Setup test values
            m_DISABLED.return_value = __DISABLED_return_value = MagicMock()

            m_DISABLED.return_value = __DISABLED_return_value = MagicMock()

            # Test and verify
            pysnooper.snoop()
            mock_get_

# Generated at 2022-06-12 19:53:03.174062
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    test = Tracer()
    assert test.trace(inspect.currentframe(), 'exception', None) == test.trace

# Generated at 2022-06-12 19:53:03.825412
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    pass


# Generated at 2022-06-12 19:53:13.340644
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import tempfile, shutil
    import linecache

    def get_source_lines(self, filename):
        lines = []
        linecache.checkcache(filename)
        line = linecache.getline(filename, 1)
        while line:
            lines.append(line.rstrip())
            line = linecache.getline(filename, 1 + len(lines))
        return lines

    def get_source(self, module_or_filename):
        if module_or_filename in sys.modules:
            module = sys.modules[module_or_filename]
            return get_source_lines(module.__file__)
        else:
            return get_source_lines(module_or_filename)

    class MockLoader(object):
        @classmethod
        def loads(cls, string):
            return string


# Generated at 2022-06-12 19:53:24.964880
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    source_lines = [
        'def foo():',
        '  a = 1',
    ]
    source_string = '\n'.join(source_lines)
    def foo():
        a = 1
    assert get_path_and_source_from_frame(
        foo.__code__.co_filename,
        foo.__code__,
    ) == (foo.__code__.co_filename, source_lines)
    assert get_path_and_source_from_frame(
        foo.__code__.co_filename,
        foo.__code__,
    ) == (foo.__code__.co_filename, source_lines)
    def bar():
        b = 2

# Generated at 2022-06-12 19:53:33.842176
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    global _exception_traceback_function
    class MockFrame(object):
        def __init__(self, f_globals, f_code, f_locals):
            self.f_globals = f_globals
            self.f_code = f_code
            self.f_locals = f_locals
    class MockLoader(object):
        def __init__(self):
            self.calls = 0
        def get_source(self, filename):
            if self.calls == 0:
                self.calls += 1
                raise ImportError('No module named {}'.format(filename))
            assert filename == 'my_module'
            return 'def function():\n    pass'
    class MockGlobals(object):
        pass

# Generated at 2022-06-12 19:53:36.378435
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        pass

    first_line_of_foo = get_path_and_source_from_frame(foo.__code__.co_firstlineno - 1)



# Generated at 2022-06-12 19:54:18.805476
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    global DISABLED
    DISABLED = False
    observer = Tracer(watch=('foo', 'bar'))
    def wrapped(foo, bar): return foo + bar
    wrapped = observer(wrapped)
    with observer:
        wrapped(1, 2)
    with pytest.raises(NotImplementedError):
        observer._wrap_class(object)
    def wrapped(foo, bar): raise ValueError
    with pytest.raises(ValueError):
        with observer:
            wrapped(1, 2)
    DISABLED = True
    assert observer(wrapped) is wrapped

# Generated at 2022-06-12 19:54:29.154019
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    """
    test_Tracer_trace()
    Test function for `Tracer.trace` method
    """
    print("start method Tracer.trace test...")
    try:
        import pytest
    except ImportError:
        pytest_installed = False
    else:
        pytest_installed = True
    if pytest_installed:
        # Testing with pytest
        #pytest.main(['-v', os.path.join(dir_name, 'snoop.py')])
        pytest.main(['-vvv', os.path.join(dir_name, 'snoop.py')])
    else:
        # Testing without pytest
        import test_snoop_no_pytest
        print("start test_snoop_no_pytest...")
        test_snoop_no

# Generated at 2022-06-12 19:54:31.524446
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer()
    tracer.trace(None, None, None)

snoop = Tracer

# Generated at 2022-06-12 19:54:41.835930
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import random
    random_number = str(random.randint(0, 1000))
    function_with_no_inputs_and_no_args = 'function_with_no_inputs_and_no_args'
    function_with_input_and_args = 'function_with_input_and_args'
    function_with_input_and_no_args = 'function_with_input_and_no_args'
    function_with_args_and_no_input = 'function_with_args_and_no_input'
    function_with_return_value = 'function_with_return_value'
    function_with_input_that_raises_exception = 'function_with_input_that_raises_exception'

# Generated at 2022-06-12 19:54:47.657996
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    with utils.TemporaryDirectory() as temporary_directory:
        with open(temporary_directory / 'hello.txt', 'w') as the_file:
            the_file.write('hi')

        writer = FileWriter(temporary_directory / 'hello.txt', False)
        writer.write('hello')
        with open(temporary_directory / 'hello.txt') as the_file:
            assert the_file.read() == 'hihello'

        writer = FileWriter(temporary_directory / 'hello.txt', True)
        writer.write('gene')
        with open(temporary_directory / 'hello.txt') as the_file:
            assert the_file.read() == 'gene'



# Generated at 2022-06-12 19:54:49.138339
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    ts = Tracer()
    ts.__enter__()
    assert __new_variable_1 == 1


# Generated at 2022-06-12 19:55:00.494650
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():

    if globals().get('skip_test', False):
        return

    # Test that call to Tracer.__call__() with arg 'function_or_class' returns correct value

    # Setup
    with pytest.raises(Exception):
        tracer = Tracer()
        if hasattr(tracer, '__enter__') and callable(tracer.__enter__):
            tracer.__enter__()

    # Exercise
    with pytest.raises(Exception):
        tracer = Tracer()
        if hasattr(tracer, '__exit__') and callable(tracer.__exit__):
            tracer.__exit__(exc_type=None, exc_value=None, exc_traceback=None)

    # Verify
    with pytest.raises(Exception):
        tracer = Tracer()


# Generated at 2022-06-12 19:55:11.247839
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():

    def assert_path_and_source(source_lines, expected_path, expected_source):
        def _func(x):
            return x * 2
        frame = inspect.currentframe()
        frame.f_code.co_filename = '<ipython-input-9-e71937adb342>'
        frame.f_globals['__loader__'] = None
        frame.f_globals['__name__'] = '__main__'
        frame.f_globals['__file__'] = 'foo.py'
        frame.f_globals['__doc__'] = None
        path, source = get_path_and_source_from_frame(frame)
        assert path == expected_path
        assert source == expected_source


# Generated at 2022-06-12 19:55:21.789551
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pytest
    global DISABLED
    DISABLED = False

    # Test to see if the wrapped function is called correctly
    class TestClass(object):
        _executed = False

        @pysnooper.snoop()
        def test_method(self):
            self._executed = True

    test_obj = TestClass()
    test_obj.test_method()
    assert test_obj._executed
    assert DISABLED == False

    # Test to see if the wrapped class is called correctly
    class TestClass(object):
        def __init__(self):
            self._executed = False

        @pysnooper.snoop()
        def test_method(self):
            self._executed = True

    test_obj = TestClass()
    test_obj.test_method()

# Generated at 2022-06-12 19:55:28.283084
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # Test using a mock object
    from mock import patch

    with patch.object(Tracer, '__call__',
                      return_value=(),
                      autospec=True) as mock_tracer:
        # Call the method
        mock_tracer.return_value = Tracer.__call__('foo', 'bar', baz='qux')
        # Assert mock_tracer has been called
        mock_tracer.assert_called_once_with('foo', 'bar', baz='qux')
        # Return the call args
        return mock_tracer.call_args

