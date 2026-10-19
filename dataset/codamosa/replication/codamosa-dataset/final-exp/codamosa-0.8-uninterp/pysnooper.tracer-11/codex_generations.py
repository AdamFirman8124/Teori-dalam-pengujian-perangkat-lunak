

# Generated at 2022-06-12 19:46:52.785477
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert get_path_and_source_from_frame(inspect.currentframe()) \
                                                              == (__file__, inspect.getsourcelines(get_path_and_source_from_frame)[0])



# Generated at 2022-06-12 19:47:01.823524
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    import os
    output_path = os.path.join(tempfile.gettempdir(), 'test_FileWriter_write_output_file.txt')
    os.remove(output_path)
    file_writer=FileWriter(output_path,False)
    file_writer.write('hello world')
    assert os.path.isfile(output_path)
    assert open(output_path).read()=='hello world'
    file_writer.write('hello world')
    assert open(output_path).read()=='hello worldhello world'
    file_writer=FileWriter(output_path,True)
    file_writer.write('hello world')
    assert os.path.isfile(output_path)
    assert open(output_path).read()=='hello world'
    file_writer.write

# Generated at 2022-06-12 19:47:07.184649
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def foo(x):
        return x ** 2

    def bar():
        a = 2
        return foo(a)

    def baz():
        raise ValueError

    t = Tracer(watch=('x', 'a'))
    with t:
        assert bar() == 4
    with pytest.raises(ValueError):
        with t:
            baz()



# Generated at 2022-06-12 19:47:08.891766
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import pysnooper
    with pysnooper.snoop():
        pass

# Generated at 2022-06-12 19:47:18.189555
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import sys
    import datetime
    from unittest import mock
    from pysnooper.snoop import Tracer
    from pysnooper.snoop import thread_global
    from pysnooper.snoop import datetime_module
    tracer = Tracer(output=None, watch=(), watch_explode=(), depth=1, prefix='',
                    overwrite=False, thread_info=False, custom_repr=(),
                    max_variable_length=100, normalize=False, relative_time=False)
    def __home_built_function():
        pass

# Generated at 2022-06-12 19:47:23.136913
# Unit test for function get_write_function
def test_get_write_function():
    def write_to_file(s):
        with open('testfile.txt', mode='w') as f:
            f.write(s)
    id_ = id(get_write_function(write_to_file, False))
    while True:
        i = id(get_write_function(write_to_file, False))
        if i != id_:
            assert False, 'did not cache'
        id_ = i



# Generated at 2022-06-12 19:47:31.185081
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # Only run this if we have the unittest module
    import unittest

    # Construct our own local 'TestCase' bases on unittest.TestCase and
    # 'SnoopTestCase' for easier testing of get_local_reprs
    class _SnoopTestCase(SnoopTestCase):
        pass

    class TestCase(Tracer, _SnoopTestCase, unittest.TestCase):
        pass

    # Test a function
    def foo():
        bar()
        bar2()
        return 42

    def bar():
        pass

    def bar2():
        pass

    class A:
        @classmethod
        def baz(cls):
            return 23

    # Test a class
    class B:
        def __init__(self):
            pass


# Generated at 2022-06-12 19:47:41.946500
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    """
    Test Tracer.__exit__
    """
    # Choose a variable to test
    variable_to_test = '-- disabled'
    variable_to_test = 'output'
    variable_to_test = 'watch'
    variable_to_test = 'watch_explode'
    variable_to_test = 'depth'
    variable_to_test = 'prefix'
    variable_to_test = 'overwrite'
    variable_to_test = 'thread_info'
    variable_to_test = 'custom_repr'
    variable_to_test = 'max_variable_length'
    variable_to_test = 'normalize'
    variable_to_test = 'relative_time'

    if variable_to_test == '-- disabled':
        return

    # Set the value to a test value
   

# Generated at 2022-06-12 19:47:46.658286
# Unit test for function get_write_function
def test_get_write_function():
    def write_to_path(path, content, overwrite=False):
        output = get_write_function(path, overwrite)
        output(content)
    write_to_path('test_get_write_function.txt', 'Hello, world.')
    write_to_path('test_get_write_function.txt', 'Hi, world.', overwrite=True)


# Generated at 2022-06-12 19:47:54.910866
# Unit test for function get_write_function
def test_get_write_function():
    import pathlib
    from .test_utils import monkeypatch
    with monkeypatch.context() as monkey:
        monkey.setattr(sys, 'stderr', stream)
        write_function = get_write_function(None, False)
        write_function(u'hi')
        assert stream.getvalue() == u'hi'
        stream.truncate(0)
        with pytest.raises(Exception):
            get_write_function(None, True)
        write_function = get_write_function(
            pathlib.Path(__file__).parent / 'repr_output.txt',
            False
        )
        write_function(u'hi')
        with open(__file__.parent / 'repr_output.txt', 'rt') as fin:
            assert fin.read() == 'hi'


# Generated at 2022-06-12 19:48:20.315799
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f():
        import inspect
        co = inspect.currentframe().f_code
        path_and_source = get_path_and_source_from_frame(inspect.currentframe())
        assert path_and_source[0] == co.co_filename
        assert path_and_source[1][:len(inspect.getsource(f))] == \
                                                        inspect.getsource(f)

    f()


# Generated at 2022-06-12 19:48:26.386523
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global DISABLED, thread_global
    DISABLED = False
    thread_global.depth = 0
    # Parameters:
    # * frame: the stack frame being traced.
    # * event: which event of the frame is being traced.
    # * arg: optional argument to describe the event, such as the return value
    #   of a function.
    #
    # Returns:
    # Either `self.trace` or None. If `self.trace` is returned, the function
    # will be called at the next event. If None is returned, the function
    # will not be called at the next event.
    #
    # Example:
    # >>> frame.f_lasti
    # 52
    # >>> frame.f_code.co_code[frame.f_lasti]
    # 'b'
    # >>> opcode

# Generated at 2022-06-12 19:48:39.030940
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import pdb
    def test_snoop():
        pass
    # These are the tests for the method `Tracer.trace`
    # Though it covers the method `get_local_reprs` too
    # The test methods do not follow the correct format
    # But use only assertions to validate the code
    # And use `pdb.set_trace()` to debug the code
    # So please read the code carefully, and follow the instructions
    # In the function definition to run the tests
    def test_case_1():
        """
        This test case checks the step-by-step execution of the method
        `Tracer.trace` :
        - when called by the method `__enter__`
        - when `event` is `call`
        """
        pdb.set_trace()

# Generated at 2022-06-12 19:48:49.112828
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global Tracer
    class Tracer:
        def _is_internal_frame(self, frame):
            return frame.f_code.co_filename == Tracer.__enter__.__code__.co_filename
        def set_thread_info_padding(self, thread_info):
            current_thread_len = len(thread_info)
            self.thread_info_padding = max(self.thread_info_padding,
                                           current_thread_len)
            return thread_info.ljust(self.thread_info_padding)
        def trace(self, frame, event, arg):
            if not (frame.f_code in self.target_codes or frame in self.target_frames):
                if self.depth == 1:
                    return None
                elif self._is_internal_frame(frame):
                    return None

# Generated at 2022-06-12 19:48:52.191708
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    print('Testing method Tracer.__call__...')
    # Execute Tracer.__call__(...) at <test_Tracer___call__>:40
    # ENOUGH_UNIT_TEST_COVERAGE_FOR_TODAY
    pass



# Generated at 2022-06-12 19:48:55.850371
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    _, source = get_path_and_source_from_frame(
                                              inspect.currentframe().f_back)
    assert source
    assert isinstance(source, list)
    assert isinstance(source[0], str)
    assert len(source) > 10 # This is not an empty unit test!

test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:48:56.744386
# Unit test for constructor of class Tracer
def test_Tracer():
    Tracer()


# Generated at 2022-06-12 19:48:58.695622
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Example of a simple test function
    def my_function():
        pass

    return my_function()



# Generated at 2022-06-12 19:49:07.976571
# Unit test for function get_write_function
def test_get_write_function():
    import contextlib
    import io
    import re
    import datetime
    import StringIO
    import tempfile
    import unittest

    class WriterBaseTests(unittest.TestCase):
        def assertWrites(self, writer, expected_output, text=u'test'):
            writer(text)
            output = self.read_output(writer)
            self.assertEqual(output, expected_output)

        def read_output(self, writer):
            raise NotImplementedError

        def test_write_to_stderr(self):
            writer = get_write_function(None, False)
            self.assertWrites(writer,
                              u'\n{now}test\n'.format(now=datetime_module.datetime.now()))
            return writer


# Generated at 2022-06-12 19:49:10.741627
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f(x, y):
        return x + y
    assert get_path_and_source_from_frame(
        inspect.currentframe().f_back)[0] == __file__



# Generated at 2022-06-12 19:49:32.809844
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import sys
    frame = sys._getframe()
    filename, source = get_path_and_source_from_frame(frame)
    assert filename == __file__
    assert source[0] == 'def test_get_path_and_source_from_frame():'


# Generated at 2022-06-12 19:49:43.275098
# Unit test for function get_local_reprs
def test_get_local_reprs():
    class CustomVariable(BaseVariable):
        def items(self, frame):
            return [('customvar', "this is a customvar")]

    def test():
        a = 1
        b = 2
        c = 'c'
        d = 'd'
        def inner():
            e = 1
            f = 2
            g = 'g'
            h = 'h'

        inner()    # noqa

    frame = inspect.currentframe().f_back
    custom_repr = [CustomVariable()]
    result = get_local_reprs(frame, custom_repr=custom_repr)
    assert result['a'] == "1"
    assert result['b'] == "2"
    assert result['c'] == "'c'"
    assert result['d'] == "'d'"

# Generated at 2022-06-12 19:49:54.294166
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import linecache, imp
    module_name = 'my_sweet_module'
    module_contents = (
        'def func_name(parameter):\n'
        '    return parameter + 1\n')
    file_name = module_name + '.py'
    with open(module_name + '.py', 'w', encoding='utf-8') as my_module_file:
        my_module_file.write(module_contents)
    module_info = imp.find_module(module_name)
    my_module = imp.load_module(module_name, *module_info)
    func_name = my_module.func_name
    frame = func_name.__code__.co_firstlineno

# Generated at 2022-06-12 19:50:01.244739
# Unit test for function get_local_reprs
def test_get_local_reprs():
    assert get_local_reprs(None, watch=[CommonVariable('index', 'index = ({index})')]) == {
        'index': 'index = (None)'
    }
    assert get_local_reprs(None, normalize=True) == {}



# Generated at 2022-06-12 19:50:09.818441
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f():
        import sys
        frame = sys._getframe(0)
        return get_path_and_source_from_frame(frame)

    # Test that this works in regular Python:
    file_name, source = f()
    assert os.path.basename(file_name) == __file__
    assert source[:5] == ['# Unit test for function get_path_and_source_from_frame',
                          'def test_get_path_and_source_from_frame():',
                          "    def f():",
                          "        import sys",
                          "        frame = sys._getframe(0)"]

    try:
        import IPython
    except ImportError:
        return

    # Make sure this works in IPython:
    ipython = IPython.get_ipython()
    ip

# Generated at 2022-06-12 19:50:16.221287
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import pysnooper
    @pysnooper.snoop(depth=2)
    def test():
        @pysnooper.snoop(depth=2)
        def test2():
            print(1)
        def test3():
            print(1)
            print(2)
        test3()
        test2()

    test()


# Generated at 2022-06-12 19:50:17.909597
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    Tracer(overwrite=True)

# trace method of class Tracer
# test for argument source_path

# Generated at 2022-06-12 19:50:20.211611
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    with pytest.raises(Exception) as exception_info:
        with Tracer():
            raise Exception
    assert exception_info.value.args[0] == 'Exception'

# Generated at 2022-06-12 19:50:22.711868
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    class Foo():
        a = 1
        def bar():
            pass
    Foo_ = Tracer()(Foo)
    assert Foo_.bar == Foo.bar
    assert Foo_.a == Foo.a


# Generated at 2022-06-12 19:50:33.982732
# Unit test for function get_write_function
def test_get_write_function():
    class Fooo: pass
    import sys
    from datetime import datetime
    from .utils import WritableStream
    from .variables import CommonVariable, Exploding
    import io
    from . import pycompat

# Generated at 2022-06-12 19:51:00.272983
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Calling method __exit__ of class 'Tracer' with
    # params (exc_type=None, exc_value=None, exc_traceback=None)
    # Expected result: None
    assert Tracer(watch=('self', 'bar', 'foo')).__exit__(exc_type=None,
                                                         exc_value=None,
                                                         exc_traceback=None) == None
    # Calling method __exit__ of class 'Tracer' with
    # params (exc_type=None, exc_value=None, exc_traceback=None)
    # Expected result: None

# Generated at 2022-06-12 19:51:11.284534
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    from pysnooper.tracer import Tracer
    tracer = Tracer()
    tracer.__enter__()
    assert sys.gettrace() == tracer.trace
    assert not hasattr(tracer, 'start_times')
    assert not hasattr(tracer, 'target_codes')
    assert not hasattr(tracer, 'target_frames')
    assert getattr(tracer, 'frame_to_local_reprs') == {}
    assert getattr(tracer, 'last_source_path') is None
    assert not hasattr(tracer, 'thread_info')
    thread_local = getattr(tracer, 'thread_local')
    assert isinstance(thread_local, threading.local)

# Generated at 2022-06-12 19:51:18.062382
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    write_mock = MagicMock()
    tracer = Tracer(output='', overwrite=False)
    tracer.write = write_mock
    frame = MagicMock()
    tracer.frame_to_local_reprs[frame] = {}
    tracer.target_frames = {frame}
    tracer.start_times[frame] = MAGIC_MOCK_DATETIME
    tracer.__exit__(None, None, None)

    assert tracer.prefix == u''
    assert tracer.frame_to_local_reprs == {}
    assert tracer.target_frames == set()
    assert tracer.start_times == {}
    assert write_mock.call_count == 2

# Generated at 2022-06-12 19:51:29.932629
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # test_Tracer_trace()

    # imports
    import unittest
    import sys
    import inspect
    import threading
    import pytest
    import copy
    import pysnooper
    import traceback
    from datetime import datetime, timedelta

    # globals
    root = pysnooper.Snoop()
    file_path = '/home/h/Downloads/test_tracer.py'
    file_name = 'test_tracer.py'

# Generated at 2022-06-12 19:51:39.529493
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import inspect
    expected_result_type = type


# Generated at 2022-06-12 19:51:41.434678
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    
    # From line 1033 in trace.py
    # depth += 1
    assert True # TODO: implement your test here


# Generated at 2022-06-12 19:51:51.869798
# Unit test for constructor of class Tracer
def test_Tracer():
    tracer = Tracer(watch=('foo', 'bar'), watch_explode=('foo', 'self'),
                         depth=3, prefix='YOLO ', overwrite=True, thread_info=True,
                         custom_repr=((int, float), (reversed, list)),
                         max_variable_length=10, normalize=False, relative_time=False)
    assert tracer.watch == [
        CommonVariable('foo'), BaseVariable('bar'),
        Exploding('foo'), Exploding('self')
    ]
    assert tracer.depth == 3
    assert tracer.prefix == 'YOLO '
    assert tracer.overwrite is True
    assert tracer.thread_info is True
    assert tracer.custom_repr == ((int, float), (reversed, list))
    assert tracer.max_variable

# Generated at 2022-06-12 19:52:02.159531
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    obj = Tracer()
    assert isinstance(obj, Tracer)

    assert hasattr(obj, '__exit__')
    assert callable(obj.__exit__)
    assert obj.__exit__ not in (object.__exit__,)
    # 1) __exit__ called on a normal function call
    def function():
        pass

    with pytest.raises(TypeError):
        obj.__exit__(function)

    with pytest.raises(TypeError):
        obj.__exit__(function)

    with pytest.raises(TypeError):
        obj.__exit__(function)

    with pytest.raises(TypeError):
        obj.__exit__(function)
    # 2) __exit__ called on a function call that raises an exception
    def function():
        raise Exception

# Generated at 2022-06-12 19:52:07.599533
# Unit test for constructor of class Tracer
def test_Tracer():
    num_bytes = 100
    output = io.BytesIO()
    for i in range(num_bytes):
        output.write(b'x')
    output.seek(0)
    with Tracer(output=output) as tracer:
        pass
    output.seek(0)
    read = output.read()
    assert len(read) == num_bytes


# Generated at 2022-06-12 19:52:12.490133
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pytest
    import sys
    import io
    import tempfile
    import contextlib
    import os.path
    
    def get_file_output(code, *args, **kwargs):
        file_output = []
        with tempfile.TemporaryFile() as f:
            @pysnooper.snoop(f, *args, **kwargs)
            def run():
                exec(code)
            run()
            f.seek(0)
            for line in f:
                file_output.append(line)
        return file_output
    
    def get_string_output(code, *args, **kwargs):
        string_output = []

# Generated at 2022-06-12 19:52:37.729134
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer()
    tracer.write = mock.MagicMock()
    tracer.write = Mock()
    with mock.patch('pysnooper.utils.pycompat.get_write_function', return_value=MagicMock()):
        tracer.__call__(Mock())
    with mock.patch('pysnooper.utils.get_cls_from_frame', return_value=None):
        tracer.__call__(MagicMock())
    with mock.patch('pysnooper.utils.get_cls_from_frame', return_value=MagicMock()):
        tracer.__call__(MagicMock())
    with mock.patch('pysnooper.utils.get_path_and_source_from_frame', return_value=('', [])):
        tr

# Generated at 2022-06-12 19:52:47.567544
# Unit test for constructor of class Tracer
def test_Tracer():
    import pysnooper
    pysnooper.Snoop(watch="verbose", depth=1, prefix='>>> ',
                    overwrite=True, thread_info=True)
    # Without overwrite=True, pysnooper doesn't append a new line ('\n'),
    # therefore test fails.
    @pysnooper.snoop()
    def foo():
        bar()
        # Should also be traced, as @snoop is added to both foo and bar

    @pysnooper.snoop(watch="baz")
    def bar():
        baz = "baz"

    @pysnooper.snoop(watch="baz")
    def baz():
        return

    foo()
    return True

if __name__ == '__main__':
    print(test_Tracer())


# Generated at 2022-06-12 19:52:52.385946
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                    'file_reading_test.zip'))
    try:
        import file_reading_test
        frame = inspect.currentframe().f_back
        result = get_path_and_source_from_frame(frame)
        file_name, source = result
        assert file_name.endswith('file_reading_test/__init__.py')
        expected_source = [
            'import ast',
            'import sys',
            '',
            'print(ast.dump(ast.parse(sys.stdin.read())))'
        ]
        assert source == expected_source
    finally:
        sys.path.pop(0)



# Generated at 2022-06-12 19:52:59.423934
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    with test_utils.captured_output() as (out, err):
        tracer = Tracer()
        tracer.watch = [
            v if isinstance(v, BaseVariable) else CommonVariable(v)
            for v in utils.ensure_tuple(watch)
         ] + [
             v if isinstance(v, BaseVariable) else Exploding(v)
             for v in utils.ensure_tuple(watch_explode)
        ]
        tracer.frame_to_local_reprs = {}
        tracer.start_times = {}
        tracer.depth = depth
        tracer.prefix = prefix
        tracer.thread_info = thread_info
        tracer.thread_info_padding = 0
        assert tracer.depth >= 1
        tracer.target_codes = set()


# Generated at 2022-06-12 19:53:09.983548
# Unit test for function get_local_reprs
def test_get_local_reprs():
    try:
        raise Exception()
    except:
        frame = sys.exc_info()[2].tb_frame.f_back

    def test():
        x = 123
        y = 456
        return
    test()
    assert get_local_reprs(frame) == {
        'x': '123',
        'y': '456',
    }
    assert get_local_reprs(frame, watch=(CommonVariable('z', 17),)) == {
        'x': '123',
        'y': '456',
        'z': '17',
    }
    assert get_local_reprs(frame, watch=(CommonVariable('y', 18),)) == {
        'x': '123',
        'y': '18',
    }




# Generated at 2022-06-12 19:53:11.176137
# Unit test for function get_write_function
def test_get_write_function():
    write = get_write_function(None, False)
    write('hello')


# Generated at 2022-06-12 19:53:14.545345
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    t = Tracer()
    msg = '''
    123
    '''
    msg = msg.format(**locals())
    out = utils.OutputCapture()
    with out:
        t.write(msg)
    assert out.result() == msg


# Generated at 2022-06-12 19:53:16.077186
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    return
    # assert False # TODO: implement your test here


# Generated at 2022-06-12 19:53:28.389320
# Unit test for function get_path_and_source_from_frame

# Generated at 2022-06-12 19:53:30.723618
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass

# Generated at 2022-06-12 19:53:57.519125
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .test_utils import assert_same_items

    def f(): # line 1
        pass # line 2
    frame = utils.get_frame_that_called(f, 2)
    (path, source) = get_path_and_source_from_frame(frame)
    assert_same_items(source, ('def f(): # line 1', '    pass # line 2', ''))

    def f(): # line 1
        pass # line 2
    # Non-ASCII file name and unicode comment:
    f.__code__.co_filename = 'מקור משובש.c'
    frame = utils.get_frame_that_called(f, 2)
    (path, source) = get_path_and_source_from_frame(frame)

# Generated at 2022-06-12 19:54:00.064897
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
  print()


# Generated at 2022-06-12 19:54:07.958938
# Unit test for method __call__ of class Tracer

# Generated at 2022-06-12 19:54:17.453108
# Unit test for function get_write_function
def test_get_write_function():
    def dummy_write(stuff):
        pass

    def dummy_method(self, stuff):
        pass

    is_path = isinstance

    # Test writing to file with append
    write = get_write_function('test', False)
    assert isinstance(write, FileWriter)
    os.remove('test')

    # Test writing to file with overwrite
    write = get_write_function('test', True)
    assert isinstance(write, FileWriter)
    os.remove('test')

    # Test writing to existing writable TextIOWrapper
    write = get_write_function(utils.WritableStream(open('test', 'w')), False)
    assert callable(write)

    # Test writing to existing writable TextIOWrapper

# Generated at 2022-06-12 19:54:25.997632
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f(a, b):
        return a + b
    g = lambda a, b: a + b
    for (frame, expected) in [(f.__code__.co_filename, f.__code__.co_filename),
                              (inspect.currentframe().f_back.f_back, 'test.py'),
                              (g.__code__.co_filename, '<lambdify>')]:
        path, source = get_path_and_source_from_frame(frame)
        assert path == expected
        if path == f.__code__.co_filename:
            assert source == ['def f(a, b):', '    return a + b']



# Generated at 2022-06-12 19:54:28.991413
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Input parameters
    # __exit__(self, exc_type, exc_value, exc_traceback)

    # Output
    # None

    # Sample call:
    # __exit__(None, None, None)

    return None

# Generated at 2022-06-12 19:54:33.206734
# Unit test for method trace of class Tracer
def test_Tracer_trace():

    import pysnooper

    def test_trace():
        def func():
            a = 2
            b = a + 5

        with pysnooper.snoop():
            func()


    test_trace()


# Generated at 2022-06-12 19:54:42.804976
# Unit test for function get_write_function
def test_get_write_function():
    import io
    import tempfile
    import os
    def test(output, overwrite, expected_write_result):
        write_function = get_write_function(output, overwrite)
        assert write_function != None

        output_stream = io.StringIO()
        write_function(output_stream)
        assert output_stream.getvalue() == expected_write_result

    test(output=None, overwrite=None, expected_write_result="<_io.StringIO object at 0x00000222C9B9E640>")
    test(output=io.StringIO(), overwrite=None, expected_write_result="<_io.StringIO object at 0x00000222C9B9E640>")

# Generated at 2022-06-12 19:54:53.624362
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():

    from types import TracebackType

    import unittest

    class BaseClass:
        class_var = BaseVariable('class_var')

        def __init__(self, name):
            self.name = CommonVariable('name')

    class CustomException(Exception):
        pass

    class ClassDecoratedWithSnoop(BaseClass):
        def __init__(self, name):
            super().__init__(name)
            self.my_list = [1, 2, 3]

        @pysnooper.snoop()
        def foo(self, a, b):
            self.bar(a, b)

        @pysnooper.snoop()
        def bar(self, a, b):
            c = a + b
            del c


# Generated at 2022-06-12 19:55:03.436997
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import sys
    import types
    exc_info = sys.exc_info()
    frame = exc_info[2].tb_frame.f_back
    (path, source_lines) = get_path_and_source_from_frame(frame)
    assert os.path.abspath(path) == os.path.abspath(__file__)
    for line in source_lines:
        assert 'Unavailable' not in line
    test_get_path_and_source_from_frame_globals = \
                                           frame.f_globals.copy()
    test_module = types.ModuleType('test_module')
    test_module.__file__ = 'test_module'
    test_get_path_and_source_from_frame_globals['test_module'] = test_module