

# Generated at 2022-06-12 19:47:00.960272
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    
    

    @pysnooper.snoop()
    def foo():
        print("from foo")

    def bar(b):

        @pysnooper.snoop()
        def foo():
            pass
    
    
    

# Generated at 2022-06-12 19:47:11.796549
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import pdb
    import logging
    import multiprocessing as mp
    import tempfile as tf
    import time

    logging.basicConfig(filename=tf.NamedTemporaryFile(suffix='.log'),
                        filemode='w', level=logging.DEBUG, format='%(message)s')
    mp.log_to_stderr(logging.INFO)

    def f():
        time.sleep(0.1)

    with Tracer(logging.debug):
        f()

    with Tracer(logging.debug):
        for i in range(10):
            f()

    with Tracer(logging.debug):
        f()
        with Tracer(logging.debug):
            f()

    class C:
        def __init__(self):
            pass


# Generated at 2022-06-12 19:47:14.168756
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    with pytest.raises(Exception):
        Tracer()

# Generated at 2022-06-12 19:47:19.877218
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    fw = FileWriter('/tmp/FileWriter_write_test.txt', True)
    # This should write to a file:
    fw.write("testing")
    # This should write to the same file, appending to it:
    fw.write("testing2")
    # This should write to the same file, appending to it:
    fw.write("testing3")



# Generated at 2022-06-12 19:47:24.614910
# Unit test for function get_write_function
def test_get_write_function():
    with open('test_output', 'w') as f:
        write = get_write_function(f, overwrite=False)
        write('test_output')
    with pycompat.open('test_output', 'r') as f:
        text = f.read()
    assert text == 'test_output'
    if os.path.exists('test_output'):
        os.remove('test_output')



# Generated at 2022-06-12 19:47:32.217532
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    '''
    Unit test for method trace of class Tracer.
    '''
    context = {}
    context['depth'] = 1
    context['target_codes'] = set()
    context['target_frames'] = set()
    tracer = Tracer()
    tracer.target_codes.add('test_Tracer_trace')
    def test():
        return 1
    def test2():
        return test()
    def test3():
        return 0
    def test4():
        return test3()
    def test5():
        return test5()
    def test6():
        return test5()
    def test7():
        return test5()
    def test8():
        return test5()
    def test9():
        return test5()
    def test10():
        return test5()

# Generated at 2022-06-12 19:47:42.885752
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # Code taken from http://stackoverflow.com/a/5067604/2988730
    import tempfile
    import linecache
    import random

    # We need to create a file that will be readable by the test function
    file_descriptor, path = tempfile.mkstemp()
    file = open(path, mode='w')
    file.writelines(['print("hi")\n', 'print("hello")\n'])
    file.close()

    def f():
        linecache.getline(path, 1)
        linecache.getline(path, 2)


    c = f.__code__
    line_no = random.randint(1, c.co_firstlineno + len(c.co_lnotab) / 2)
    my_frame = sys._getframe()
    my

# Generated at 2022-06-12 19:47:52.116451
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    """Unit test for method trace of class Tracer"""
    def say_hi():
        print('hi')
    class Foo(object):
        @pysnooper.snoop()
        def hi(self):
            print('hi')

    with mock.patch('pysnooper.tracer.get_write_function') as mock_getwrite:
        mock_getwrite.return_value = mock.MagicMock()
        tracer = Tracer()
        tracer.watch = []
        tracer.prefix = ''
        tracer.destination_path = ''
        tracer.thread_info = False
        tracer.thread_info_padding = 0
        tracer.max_variable_length = 100
        tracer.normalize = False
        tracer.relative_time = False
        tracer.depth = 1
       

# Generated at 2022-06-12 19:48:02.160022
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # Unit tests should be run from inside the `tests/` folder.
    current_directory = os.path.split(__file__)[0]
    assert current_directory.endswith('tests')
    def get_frame(filename, line_number):
        def dummy_function():
            return dummy_function()
        dummy_frame = inspect.currentframe()
        dummy_frame.f_code.co_filename = filename
        dummy_frame.f_lineno = line_number
        return dummy_frame
    def check(filename, line_number, line_text):
        frame = get_frame(filename, line_number)
        file_name, source = get_path_and_source_from_frame(frame)
        assert source[line_number - 1].rstrip() == line_text

# Generated at 2022-06-12 19:48:13.326588
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import pytest
    from pysnooper.tracing import Tracer
    from pysnooper.utils import get_path_and_source_from_frame, utils
    from pysnooper.variables import CommonVariable, TracingVariable, Exploding
    import inspect
    import os
    import sys
    import re
    import threading
    import functools
    import pycompat
    import traceback
    import sys
    import dis
    import opcode
    import datetime
    import datetime
    import datetime
    import imp
    import unittest.mock
    import datetime
    import pysnooper.variables
    import pysnooper.utils
    import pysnooper.variables
    import pysnooper.utils
    import pysnooper.variables
    import pysno

# Generated at 2022-06-12 19:48:34.891793
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .test_utils import foo, bar
    assert get_path_and_source_from_frame(foo.__code__.co_filename) == \
                                                                  (foo)
    assert get_path_and_source_from_frame(bar.__code__.co_filename) == \
                                                                  (bar)


# Generated at 2022-06-12 19:48:36.023261
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def asdf():
        pass


# Generated at 2022-06-12 19:48:46.430784
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    def f(arg):
        pass

    # __enter__
    snoop = pysnooper.Snoop()
    with snoop:
        f()

    snoop = pysnooper.Snoop()
    with pytest.raises(Exception):
        with snoop:
            raise Exception

    snoop = pysnooper.Snoop()
    with pytest.raises(AssertionError):
        with snoop:
            assert False

    snoop = pysnooper.Snoop()
    with pytest.raises(KeyError):
        with snoop:
            a = {}
            b = a[1]

    snoop = pysnooper.Snoop()
    with pytest.raises(ZeroDivisionError):
        with snoop:
            a = 1 / 0



# Generated at 2022-06-12 19:48:54.871799
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # See test_Tracer_trace for unit tests for methods __enter__, __exit__ and
    # trace.
    import doctest
    doctest.testmod()

    def call_logger(s):
        call_logger.calls.append(s)


# Generated at 2022-06-12 19:49:03.911161
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global call_trace_result
    call_trace_result = 'No call'
    def method(arg1, arg2):
        global call_trace_result
        call_trace_result = 'call'
        return arg1 + arg2
    test_instance = Tracer()
    test_frame = inspect.currentframe()
    test_frame.f_code = method.__code__
    test_frame.f_lasti = 50
    test_frame.f_lineno = 42
    test_frame.f_code.co_code = 'DUMMY'
    test_frame.f_locals = {}
    test_frame.f_locals['arg1'] = 'one'
    test_frame.f_locals['arg2'] = 'two'
    test_arg = None
    test_event = 'call'

# Generated at 2022-06-12 19:49:11.458569
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import os
    import subprocess

    def _assert_snoop_output(out, s):
        assert out == s.strip() + '\n', out

    def _call_file(filename, stdin=None):
        out = subprocess.check_output(
            PYTHON_EXECUTABLE + ' ' + filename,
            input=stdin,
            shell=True,
        )
        assert out == out.decode(), out
        return out.decode()

    def test_simple_function():
        filename = os.path.join(tempfile.gettempdir(), 'simple_function.py')

# Generated at 2022-06-12 19:49:16.342538
# Unit test for constructor of class Tracer
def test_Tracer():
    assert Tracer
    assert Tracer.__doc__
    assert inspect.isclass(Tracer)
    assert callable(Tracer)

    assert hasattr(Tracer, '__init__')
    assert Tracer.__init__.__doc__
    assert callable(Tracer.__init__)


# Generated at 2022-06-12 19:49:17.892355
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
	pass



# Generated at 2022-06-12 19:49:29.170834
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    test_source = os.linesep.join(('def func(x):',
                                   '    # comment',
                                   '    y = 5',
                                   '    return x * y'))
    module_name = '__temp_testing_wingdbstub'
    file_name = module_name + '.py'
    with open(file_name, 'wb') as f:
        f.write(test_source.encode('utf-8'))
    loader = importlib.machinery.SourceFileLoader(module_name, file_name)
    frame = sys._getframe()
    frame.f_globals['__loader__'] = loader
    frame.f_globals['__name__'] = module_name
    frame.f_code.co_filename = file_name

    path, source = get_path

# Generated at 2022-06-12 19:49:32.687180
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def test_inner(t):
        t.write('t')
        with t:
            t.write('sub')
    t = Tracer()
    test_inner(t)


# Generated at 2022-06-12 19:49:51.703406
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def function():
        1 + 1
    frame = function.__code__.co_filename, function.__code__.co_firstlineno
    file_name, source = get_path_and_source_from_frame(frame)
    assert file_name == frame.co_filename
    assert source[0] == 'def function():'



# Generated at 2022-06-12 19:49:54.047424
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    """
    @pysnooper.snoop(watch=())
    def foo():
        print(1)

    ^
    """
    

# Generated at 2022-06-12 19:49:56.980820
# Unit test for constructor of class Tracer
def test_Tracer():
    tracer = Tracer(watch='foo', watch_explode=('self',))
    assert tracer.watch == [CommonVariable('foo'), Exploding('self')]
    assert tracer.depth == 1
    assert tracer.prefix == ''


# Generated at 2022-06-12 19:50:06.685257
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    def do_test(output, watch, watch_explode, depth, prefix, overwrite, thread_info, custom_repr, max_variable_length, normalize, relative_time, expected_output):
        print("Testing with inputs:")
        print("output = {0}".format(output))
        print("watch = {0}".format(watch))
        print("watch_explode = {0}".format(watch_explode))
        print("depth = {0}".format(depth))
        print("prefix = {0}".format(prefix))
        print("overwrite = {0}".format(overwrite))
        print("thread_info = {0}".format(thread_info))
        print("custom_repr = {0}".format(custom_repr))

# Generated at 2022-06-12 19:50:07.372159
# Unit test for function get_path_and_source_from_frame

# Generated at 2022-06-12 19:50:14.709234
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def frame_maker(code_string):
        frame = sys._getframe(0)
        frame.f_code.co_filename = '<string>'
        frame.f_globals['__name__'] = '__fake_module__'
        loader = FakeLoader(code_string)
        frame.f_globals['__loader__'] = loader
        return frame

    frame = frame_maker('spam\neggs\nbacon')
    assert get_path_and_source_from_frame(frame) == ('<string>',
                                                     ['spam', 'eggs', 'bacon'])

    frame = frame_maker('# -*- coding: ascii -*-\nspam\neggs\nbacon')

# Generated at 2022-06-12 19:50:23.157327
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class TestTracerTrace():
        def __init__(self):
            self.trace = Tracer()

        def test_Tracer_trace_without_watch(self):
            # arrange
            self.trace = Tracer()
            # act
            self.trace.set_thread_info_padding('thread-123 ')
            self.trace.trace(None, 'call', None)
            self.trace.write('indent-return-123')
            self.trace.write('indent-exception-123')
            self.trace.write('indent-return-123')
            # assert
            self.trace.write('indent-return-123')


# Generated at 2022-06-12 19:50:34.502536
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # setUp
    tracer = Tracer()
    tracer.write = MagicMock()
    frame = MagicMock()
    frame.f_code = MagicMock()
    frame.f_code.co_filename = 'pysnooper.py'
    frame.f_lineno = 49
    frame.f_code.co_code = b'\x64\x0a\x64\x04\x00\x64\x00\x00\x00\x64\x00\x00\x00'
    frame.f_lasti = 7
    event = 'call'
    arg = None
    thread_global.depth = 0
    # Test
    res = tracer.trace(frame, event, arg)
    # Assert
    assert res == tracer.trace
    assert tracer.write

# Generated at 2022-06-12 19:50:43.379687
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import textwrap
    import io
    sio = io.StringIO()
    tracer = pysnooper.snoop(sio, max_variable_length=10)
    with tracer:
        x = [10 ** 10] * 10
    assert sio.getvalue() == textwrap.dedent("""
        Starting var:.. x = [10000000000, ...]
        Var modified:. x = [10000000000, ...]
        """).strip()

    sio = io.StringIO()
    tracer = pysnooper.snoop(sio, max_variable_length=None)
    with tracer:
        x = [10 ** 10] * 10

# Generated at 2022-06-12 19:50:53.369814
# Unit test for constructor of class Tracer
def test_Tracer():
    @Tracer(output='/tmp/snoop')
    def f1(a, b):
        c = a + b
        d = a * b
        f = a / b
        e = 1 / 0
        return d, f, e

    f1(2, 3)

    assert f1.__name__ == "f1"
    assert inspect.getsource(f1) == inspect.getsource(test_Tracer)

    with open('/tmp/snoop', 'r') as f:
        assert f.read() == '\n'

if __name__ == '__main__':
    test_Tracer()

# Generated at 2022-06-12 19:51:14.356700
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import tempfile
    output = tempfile.NamedTemporaryFile(mode='r', encoding='utf-8')
    tracer = Tracer(output=output, max_variable_length=None)
    frame = inspect.currentframe()
    tracer.target_codes.add(frame.f_code)
    tracer.trace(frame, 'call', None)
    assert output.read() == pipe_to_string(
'''
    Starting var:.. __file__ = '{__file__}'
'''.format(**locals()))
    output.close()


# Generated at 2022-06-12 19:51:18.838117
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from pysnooper.fallbacks.utils import get_write_function, utils, inspect, functools, threading, pycompat
    from pysnooper.fallbacks.base_variable import BaseVariable, CommonVariable, Exploding
    import pysnooper.fallbacks.constants as constants

    def test_decorator():
        @pysnooper.snoop()
        def foo():
            print('hi')
        foo()

    test_decorator()
    output, _ = capsys.readouterr()
    assert 'hi' in output



# Generated at 2022-06-12 19:51:26.143149
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    my_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'test_get_path_and_source_from_frame.py')

# Generated at 2022-06-12 19:51:28.411077
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert get_path_and_source_from_frame(sys._getframe()) == \
                                                      (__file__, __file__.splitlines())




# Generated at 2022-06-12 19:51:38.290762
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    with Tracer(watch=[]) as tracer:
        with tracer:
            assert tracer.target_codes == {test_Tracer_trace.__code__}
            frame = inspect.currentframe()
            assert frame in tracer.target_frames
            assert frame.f_back.f_trace == tracer.trace
            assert frame.f_trace == tracer.trace
            assert thread_global.depth == -1
            tracer.trace(frame, 'call', None)
            assert thread_global.depth == 0
            tracer.trace(frame, 'exception', ['', '', None])
            assert thread_global.depth == 0
            tracer.trace(frame, 'return', None)
            assert thread_global.depth == -1
            assert frame not in tracer.target_frames
            assert frame.f_back

# Generated at 2022-06-12 19:51:40.156407
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass


# Generated at 2022-06-12 19:51:42.698803
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    f = lambda a, b: a + b
    tf = Tracer()(f)
    assert tf(1, 2) == 3


# Generated at 2022-06-12 19:51:52.366155
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # The test case is not used in __main__.
    # If pytest is not installed, comment out this function.
    # import pytest # pytest >= 3.6 is required.

    def foo():
        a = 'a'
        b = 'b'
        return a + '+' + b

    def test1():
        output = io.StringIO()

        code = foo.__code__
        trace = Tracer(output)
        frame = inspect.currentframe().f_back
        event = 'call'
        arg = None
        trace(frame, event, arg)
        frame.f_code = code
        frame.f_lineno = 2
        source = foo.__code__.co_code.splitlines()

# Generated at 2022-06-12 19:52:02.411050
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import test_pysnooper
    import test_pysnooper_test_pysnooper
    import test_pysnooper_test_pysnooper_test_pysnooper
    import test_pysnooper_test_pysnooper_test_pysnooper_test_pysnooper
    import pdb

    import io
    import mock
    import os
    import pycompat
    import pytest
    import StringIO
    import sys
    import threading
    import traceback
    import unittest
    import warnings

    import pysnooper
    from pysnooper import snoop
    from pysnooper import utils
    from pysnooper.utils import get_missing_modules, get_repr_function
    

# Generated at 2022-06-12 19:52:03.300971
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass

# Generated at 2022-06-12 19:52:20.806909
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # That method doesn't do anything
    t = pysnooper.Snooper()
    assert t.__exit__() == None

# Generated at 2022-06-12 19:52:23.115261
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert isinstance(get_path_and_source_from_frame(sys._getframe())[0],
                      str)
test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:52:32.577231
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    with open('test_FileWriter_write.txt', 'w') as test_FileWriter_write_file:
        test_FileWriter_write_file.write('initial')
    as_string = b'12\xc3\xa5\xc3\xa5'
    as_unicode = as_string.decode('utf-8')
    initial_as_string = 'initial'
    initial_as_unicode = initial_as_string.decode('utf-8')

# Generated at 2022-06-12 19:52:43.256853
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import os
    import tempfile
    import pytest
    for overwrite in (False, True):
        with tempfile.NamedTemporaryFile('w', encoding='utf-8') as output_file:
            fw = FileWriter(output_file.name, overwrite)
            fw.write(u'bla bla\n')
            fw.write(u'bla bla\n')
            output_file.seek(0)
            assert output_file.read() == (overwrite and (u'bla bla\n' * 2)
                                          or (u'bla bla\n'))
        assert overwrite == os.path.isfile(output_file.name)
    with pytest.raises(Exception):
        FileWriter('/tmp/test.log', True)

# Generated at 2022-06-12 19:52:50.640375
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import inspect
    import traceback
    import pysnooper
    
    
    
    
    
    source_path = ".../test.py"
    source = ["def foo():", "    return 2 + 2", "", "foo()"]
    line_no = 2
    event = 'exception'
    arg = None
    arg = arg
    _frame_candidate = None
    current_thread = None
    _frame_candidate = _frame_candidate
    current_thread = current_thread
    source_line = source[line_no - 1]
    indents = [" " * 4 * thread_global.depth]
    calling_frame = sys._getframe()
    frame = sys._getframe(1)
    calling_frame = calling_frame

# Generated at 2022-06-12 19:52:58.010530
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import shutil
    import tempfile
    import traceback
    store_folder = tempfile.mkdtemp()
    try:
        assert os.path.exists(store_folder)
        t = Tracer(output=store_folder)
        try:
            raise Exception('Ouch')
        except Exception:
            exc = sys.exc_info()[1]
            e = exc
        finally:
            t.__exit__(*exc)
        assert os.path.exists(os.path.join(store_folder, 'output.log'))
        with open(os.path.join(store_folder, 'output.log')) as f:
            content = f.read()
    finally:
        shutil.rmtree(store_folder)
    assert e.__class__.__name__ in content

# Generated at 2022-06-12 19:52:58.900135
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    pass # Nothing to test.

# Generated at 2022-06-12 19:53:03.734900
# Unit test for function get_write_function
def test_get_write_function():
    def writer(s):
        open(os.path.join(utils.get_temp_dir(), 'output.txt'), 'w').write(s)
    get_write_function(writer, True)
    get_write_function(utils.WritableStream(), False)



# Generated at 2022-06-12 19:53:10.822519
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    def test_Tracer___exit___case_3(self):
        assert self.start_times == {}
    def test_Tracer___exit___case_2(self):
        assert self.frame_to_local_reprs.pop() == None
    def test_Tracer___exit___case_1(self):
        assert self.thread_local.original_trace_functions.pop() == None
    def test_Tracer___exit___case_0(self):
        assert sys.settrace(None) == self.trace
 

# Generated at 2022-06-12 19:53:18.066694
# Unit test for function get_write_function
def test_get_write_function():
    class MyWritableStream(object):
        def __init__(self):
            self.written = ''
        def write(self, s):
            self.written += s
    output = MyWritableStream()
    write = get_write_function(output)
    write('abc')
    assert output.written == 'abc'
    output = MyWritableStream()
    try:
        get_write_function('abc', True)('def')
    except Exception as e:
        assert str(e) == '`overwrite=True` can only be used when writing ' \
                         'content to file.'
    else:
        raise Exception('Failed to raise an exception!')
    import tempfile
    file_name = tempfile.NamedTemporaryFile().name
    write = get_write_function(file_name, overwrite=True)

# Generated at 2022-06-12 19:53:54.390538
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from pysnooper.tracer import Tracer

    tracer = Tracer()
    tracer.__call__("string")
    with pytest.raises(NotImplementedError):
        class TestClass:
            pass
        tracer.__call__(TestClass)
    with pytest.raises(NotImplementedError):
        def coroutine():
            yield
        tracer.__call__(coroutine)

# Generated at 2022-06-12 19:54:05.021051
# Unit test for constructor of class Tracer
def test_Tracer():

    # Test for watch
    tracer = Tracer(watch=["foo", "bar"])
    assert isinstance(tracer.watch, list)
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], CommonVariable)
    assert isinstance(tracer.watch[1], CommonVariable)
    assert tracer.watch[0].name == "foo"
    assert tracer.watch[1].name == "bar"
    tracer = Tracer(watch=["foo"])
    assert isinstance(tracer.watch, list)
    assert len(tracer.watch) == 1
    assert isinstance(tracer.watch[0], CommonVariable)
    assert tracer.watch[0].name == "foo"

    # Test for watch_explode

# Generated at 2022-06-12 19:54:07.994699
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    tracer = Tracer()
    tracer.trace = lambda *args, **kwargs: None
    tracer.__enter__()
    assert thread_global.depth == -1

# Generated at 2022-06-12 19:54:17.452956
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    tracer = Tracer()
    frame = inspect.currentframe().f_back
    assert tracer._is_internal_frame(frame) == False
    assert tracer.target_codes == {test_Tracer.__code__}
    assert tracer.target_frames == {frame}
    assert tracer.frame_to_local_reprs == {}
    assert tracer.start_times == {}
    assert len(tracer.watch) == 0
    assert tracer.frame_to_local_reprs == {}
    assert tracer.start_times == {}
    assert len(tracer.watch) == 0
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info == False
    assert tracer.thread_info_padding == 0
    assert tracer.last_source

# Generated at 2022-06-12 19:54:19.957922
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from . import tests
    assert get_path_and_source_from_frame(inspect.currentframe())[0] == \
           tests.__file__



# Generated at 2022-06-12 19:54:23.520062
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    with open(__file__, 'r') as f:
        file_contents = f.read()

    def function(x):
        return x

    result = get_path_and_source_from_frame(function.__code__.co_firstlineno)
    if result[0] != __file__:
        print(result)
        raise AssertionError

    if result[1] != file_contents.splitlines():
        print(result)
        raise AssertionError



# Generated at 2022-06-12 19:54:28.711484
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
  import datetime
  import sys

  from . import main
  from . import utils
  from . import thread_global

  from .utils import BaseVariable
  from .utils import CommonVariable
  from .utils import Exploding

  # Define arg values for test
  arg_function_or_class = main
  arg_output = None
  arg_watch = ((),)
  arg_watch_explode = ((),)
  arg_depth = 1
  arg_prefix = ''
  arg_overwrite = False
  arg_thread_info = False
  arg_custom_repr = ((),)
  arg_max_variable_length = 100
  arg_normalize = False
  arg_relative_time = False

# Generated at 2022-06-12 19:54:34.718379
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert get_path_and_source_from_frame(sys._getframe(0))[0] == os.path.join(
                    os.path.dirname(__file__), 'stack.py')
    assert get_path_and_source_from_frame(sys._getframe(0))[1][0] == \
            u'# Unit test for function get_path_and_source_from_frame'



# Generated at 2022-06-12 19:54:42.165656
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_function(x):
        return x + 1
    # It's a local function, so it's not in sys.modules:
    assert get_path_and_source_from_frame(test_function.__code__.co_filename)
    # Let's make it global, which should make it work
    globals()['test_function'] = test_function
    # It's a global function, so it's in sys.modules:
    assert get_path_and_source_from_frame(test_function.__code__.co_filename)
    del globals()['test_function']



# Generated at 2022-06-12 19:54:52.164273
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    max_variable_length = 100
    prefix = ''
    depth = 1
    overwrite = False
    output = None
    watch = ()
    watch_explode = ()
    thread_info = False
    custom_repr = ()
    relative_time = False
    normalize = False

# Generated at 2022-06-12 19:55:32.539432
# Unit test for constructor of class Tracer
def test_Tracer():
    # pylint: disable=W0612
    if _pysnooper_test:
        def dummy():
            pass
        path, source = get_path_and_source(dummy)
        tracer = Tracer(watch=['x'], watch_explode=('y', 'z'), depth=2,
                        prefix='', overwrite=False, thread_info=True,
                        custom_repr=((None, lambda x: x),),
                        max_variable_length=100, normalize=False,
                        relative_time=True)
        assert tracer.watch == [CommonVariable('x'), Exploding('y'),
                                Exploding('z')]
        assert tracer.depth == 2
        assert tracer.prefix == ''
        assert tracer.thread_info == True

# Generated at 2022-06-12 19:55:40.318131
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import sys
    import os
    import collections

    class Spy(object):

        def __init__(self):
            self.events = []

        def trace(self, frame, event, arg):
            self.events.append((event, frame, arg))
            return self.trace

    @unittest.mock.patch('pysnooper.pycompat.get_path_and_source_from_frame')
    @unittest.mock.patch('pysnooper.pycompat.time_isoformat')
    def test(time_isoformat, get_path_and_source_from_frame):
        watch = ('watch',)
        class BaseVariable(object):
            def get_value(self, local_dict, global_dict):
                return [], None


# Generated at 2022-06-12 19:55:40.871867
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
  pass

# Generated at 2022-06-12 19:55:51.396566
# Unit test for function get_write_function
def test_get_write_function():
    from . import pycompat
    from .output_wrappers import CatchupStream
    # Test get_write_function() when output is None
    if sys.version_info[0] < 3:
        class FakeStderr(object):
            def write(self, s):
                try:
                    return str(s)
                except UnicodeEncodeError:
                    return utils.shitcode(s)
    else:
        FakeStderr = io.StringIO
    fake_stderr = FakeStderr()
    write_function = get_write_function(None, False)
    assert write_function('test') == 'test'
    # Test get_write_function() when output is a path-like object
    output = os.path.join(tempfile.gettempdir(), 'test.txt')

# Generated at 2022-06-12 19:55:58.149640
# Unit test for constructor of class Tracer
def test_Tracer():
    import sys, io

    output = io.StringIO()

    def foo():
        a = 1
        b = 2
        c = 3

    with Tracer(output=output, watch=('a',)):
        foo()
    assert output.getvalue() == '''
        Source path:... {source_path}
        Starting var:.. a = 1
        Elapsed time: {elapsed_time_string}
    '''.format(
        source_path=foo.__code__.co_filename,
        elapsed_time_string=pycompat.timedelta_format(pycompat.timedelta(0)),
    )

    output = io.StringIO()
    with Tracer(output=output, watch=('a',)):
        a = 1
        b = 2
        c = 3
