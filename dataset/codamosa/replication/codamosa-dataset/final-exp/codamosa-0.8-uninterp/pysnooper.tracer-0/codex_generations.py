

# Generated at 2022-06-12 19:47:01.500344
# Unit test for function get_write_function
def test_get_write_function():
    import os
    import tempfile
    import pathlib

    write = get_write_function(None, False)
    assert write

    tmp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    file_name = str(pathlib.Path(tmp_file.name))
    write = get_write_function(tmp_file.name, True)
    assert write

    write("hello world")
    tmp_file.close()
    content = utils.read_file(file_name)
    assert content == "hello world"
    os.unlink(file_name)
    assert not os.path.exists(file_name)

    write = get_write_function(None, True)
    assert write



# Generated at 2022-06-12 19:47:05.276560
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    assert get_path_and_source_from_frame(frame) == \
           (__file__, pycompat.source_splitter(__file__))
test_get_path_and_source_from_frame()


# Generated at 2022-06-12 19:47:16.573008
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from pytest import raises

    def get_Tracer_instance(output=None, watch=(), watch_explode=(), depth=1,
                            prefix='', overwrite=False, thread_info=False, custom_repr=(),
                            max_variable_length=100, normalize=False, relative_time=False):
        instance = Tracer()
        arguments = dict(output=output, watch=watch,
                         watch_explode=watch_explode, depth=depth,
                         prefix=prefix, overwrite=overwrite,
                         thread_info=thread_info, custom_repr=custom_repr,
                         max_variable_length=max_variable_length, normalize=normalize,
                         relative_time=relative_time)
        for key, value in arguments.items():
            setattr(instance, key, value)
       

# Generated at 2022-06-12 19:47:23.098741
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import six
    def foo():
        # This is a fake function for testing
        return 1
    def bar():
        # This is a fake function for testing
        return 2

    def make_frame():
        try:
            raise Exception()
        except Exception:
            return sys.exc_info()[2].tb_next.tb_next.tb_next.tb_frame

    frame = make_frame()
    assert get_path_and_source_from_frame(frame)[1][0] == \
           'def foo():'



# Generated at 2022-06-12 19:47:27.549994
# Unit test for function get_write_function
def test_get_write_function():
    if pycompat.PY2:
        # God damn Python 2
        sys.stderr.write('')
    write = get_write_function(None, False)
    write(u'foo')
    write('foo')

    s = utils.WritableStream()
    get_write_function(s, False)('foo')
    assert s.s == 'foo'



# Generated at 2022-06-12 19:47:34.179072
# Unit test for method trace of class Tracer
def test_Tracer_trace():

    import pysnooper
    import os.path
    from datetime import datetime
    from os import path

    class PySnooperTest():

        def __init__(self):
            print("init")

        def snoop_test(self, num1, num2):
            """
            Test for snoop_test method
            """
            result = num1 + num2
            print("result = ", result)
            return result

    py_snooper_obj = PySnooperTest()


# Generated at 2022-06-12 19:47:35.966911
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    pass

### Other stuff: ##############################################################
#                                                                             #

# Generated at 2022-06-12 19:47:44.431598
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pysnooper
    import unittest
    import pytest
    from pysnooper import _snoop_config
    _snoop_config.watch_explode = ()
    _snoop_config.watch = ()
    _snoop_config.custom_repr = ()
    _snoop_config.prefix = ''
    _snoop_config.max_variable_length = 100
    _snoop_config.normalize = False
    _snoop_config.relative_time = False
    _snoop_config.overwrite = False





# Generated at 2022-06-12 19:47:53.327780
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
  # set up context
  tracer = Tracer(None, (), (), 1, '', False, False, (), 100, False, False)
  tracer.frame_to_local_reprs = {}
  tracer.start_times = {}
  tracer.target_codes = set()
  tracer.target_frames = set()
  tracer.thread_local = threading.local()
  tracer.thread_local.__dict__['original_trace_functions'] = []
  tracer.last_source_path = None
  tracer.max_variable_length = 100
  tracer.normalize = False
  tracer.relative_time = False
  global DISABLED
  DISABLED = False
  exc_type = None
  exc_value = None
  exc_traceback = None
  # call the

# Generated at 2022-06-12 19:48:02.942799
# Unit test for function get_write_function
def test_get_write_function():
    def writer():
        output = sys.stderr
        if pycompat.PY2:
            output = utils.WritableStream(sys.stderr)
        return output

    write = get_write_function(None, False)
    assert callable(write)
    write = get_write_function(None, True)
    assert callable(write)
    write = get_write_function(writer(), False)
    assert callable(write)
    write = get_write_function(writer(), True)
    assert callable(write)
    write = get_write_function(sys.stderr, False)
    assert callable(write)
    write = get_write_function(sys.stderr, True)
    assert callable(write)



# Generated at 2022-06-12 19:48:27.560230
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import builtins
    import importlib
    import pickle
    import types
    import unittest
    import uuid

    def raise_(err):
        raise err

    class Foo:
        def method(self):
            raise_(RuntimeError("baz"))

    class Bar:
        @pysnooper.snoop()
        def method(self):
            raise_(RuntimeError("baz"))


    class BaseTestCase(unittest.TestCase):
        def test__call__(self):
            with self.assertRaises(RuntimeError) as cm:
                self.obj.method()
            self.assertEqual(cm.exception.args, ("baz",))

        def test_future_calls(self):
            obj = self.obj()

# Generated at 2022-06-12 19:48:29.985624
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def make_frame():
        def fake_function():
            def fake_function_that_was_never_defined(): pass
        return make_frame.__wrapped__()

    # Test a function with __qualname__
    make_frame.__wrapped__ = lambda: inspect.currentframe()
    frame = make_frame()
    file_name, source = get_path_and_source_from_frame(frame)
    assert file_name == __file__
    assert source == []
    make_frame.__wrapped__ = None




# Generated at 2022-06-12 19:48:33.083582
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # __exit__ of class Tracer. This is tested course-wise.
    pass


# Generated at 2022-06-12 19:48:43.523431
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import threading
    import datetime
    import sys
    import inspect
    import functools
    import os
    import pysnooper.utils as utils
    import pycompat
    import pysnooper.variable as variable
    import pysnooper.thread_global as thread_global
    import opcode
    import traceback
    import datetime

    DISABLED = True

    def test_Tracer___enter___assertions():
        calling_frame = inspect.currentframe().f_back
        assert not tracer_instance._is_internal_frame(calling_frame)
        try:
            assert stack.pop() is None
        except:
            raise AssertionError
        assert sys.gettrace() is tracer_instance.trace
        assert calling_frame.f_trace is tracer_instance.trace

# Generated at 2022-06-12 19:48:45.218275
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    with Tracer() as tracer:
        pass

# Generated at 2022-06-12 19:48:54.062209
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    import sys
    import threading
    import pycompat
    import inspect
    import functools
    import datetime
    import traceback
    import opcode
    from .utils import get_shortish_repr

    DISABLED = 1

    def test_function(a, b):
        return a + b

    test_function._snoop_ignore = False
    test_function._snoop_depth = 2
    test_function._snoop_prefix = ''
    test_function._snoop_overwrite = False
    test_function._snoop_thread_info = False
    test_function._snoop_custom_repr = ()
    test_function._snoop_max_variable_length = 100
    test_function._snoop_normalize = False
    test_function._sno

# Generated at 2022-06-12 19:48:54.811235
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
  pass


# Generated at 2022-06-12 19:48:57.823174
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    a = 1
    b = 2
    @pysnooper.snoop()
    def add(a, b):
        return a + b
    c = add(a, b)
    d = c + 1
    return d


# Generated at 2022-06-12 19:49:02.766034
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def foo():
        for i in range(3):
            print(i)
            yield i
    foo = Tracer(watch=('i', 'self',), max_variable_length=None)(foo)
    x = foo()
    next(x)
    next(x)
    next(x)
    try:
        next(x)
    except StopIteration:
        pass

test_Tracer_trace()

# Generated at 2022-06-12 19:49:06.420238
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    from pysnooper.snooper import Tracer
    # snooper = Tracer()
    # assert snooper.trace(frame, event, arg) == None
    assert True # TODO: implement your test here


# Generated at 2022-06-12 19:49:51.122993
# Unit test for function get_write_function
def test_get_write_function():
    # Test for get_write_function() function in debug.py
    assert callable(get_write_function(None, False))
    assert callable(get_write_function(None, True))
    assert callable(get_write_function('./', False))
    assert callable(get_write_function('./', True))
    assert callable(get_write_function(sys.stdout, False))
    assert callable(get_write_function(sys.stdout, True))
    def func(a, b=2):
        return a+b
    assert callable(get_write_function(func, False))
    assert callable(get_write_function(func, True))
    class C:
        def __init__(self):
            self.a = 2

# Generated at 2022-06-12 19:49:55.414134
# Unit test for method trace of class Tracer
def test_Tracer_trace():

    import pysnooper
    t = pysnooper.Tracer()

    def test(num):
        return num * num

    t.trace(None, 'call', None)

    import sys
    old_trace = sys.gettrace()
    sys.settrace(t.trace)

    test(4)

    sys.settrace(old_trace)



# Generated at 2022-06-12 19:50:06.197705
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    import re
    import os
    import sys

    def test_function():
        return inspect.currentframe()

    frame = test_function()
    path, source = get_path_and_source_from_frame(frame)
    assert path == frame.f_code.co_filename
    assert len(source) == len(inspect.getsourcelines(frame.f_code)[0])

    def make_code_object(source_code):
        import types
        source_code = '\n'.join(['    ' + line for line in source_code.splitlines()])
        return compile(source_code, '<inline>', 'exec')

    def make_frame(code_object):
        return sys._getframe(1)

    source_code = \
        '# coding=utf-8\n'

# Generated at 2022-06-12 19:50:14.587443
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer_1 = Tracer()
    tracer_1.write = MagicMock()
    tracer_2 = Tracer()
    tracer_2.write = MagicMock()
    tracers = [tracer_1, tracer_2]
    tracers = [tracer_1]
    def foo():
        x = 1
        y = 2
        z = 3
        x = 4
    def bar():
        foo()
    bar()
    try:
        bar()
    except:
        pass
    # assert tracer_1.write.call_args_list[-4][0][0] == '    Starting var:.. x = 1'
    # assert tracer_1.write.call_args_list[-3][0][0] == '    Starting var:.. y = 2'
    # assert

# Generated at 2022-06-12 19:50:16.148914
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    with pytest.raises(AssertionError):
        Tracer(depth=0)


# Generated at 2022-06-12 19:50:21.172625
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # We can't unit test Tracer in its entirety as we can't mock or
    # monkeypatch built-in trace function. Instead we test the unit
    # test-friendly parts of Tracer.
    snoop = pysnooper.snoop(max_variable_length=100, normalize=True)
    with snoop:
        print('asdf')

    assert 'asdf\n' in snoop._write.call_args[0][0]
    assert 'Elapsed time:... ' in snoop._write.call_args[0][0]
    assert len(snoop.start_times) == 0
    assert thread_global.depth == -1


# Generated at 2022-06-12 19:50:24.042952
# Unit test for constructor of class Tracer
def test_Tracer():
    """
    This method tests constructor of Tracer class
    :return:
    """
    tracer = Tracer(output=None, watch=(), watch_explode=(), depth=1,
                 prefix='', overwrite=False, thread_info=False, custom_repr=(),
                 max_variable_length=100, normalize=False, relative_time=False)
    assert isinstance(tracer, Tracer)


# Generated at 2022-06-12 19:50:34.581479
# Unit test for method trace of class Tracer
def test_Tracer_trace():    
    import datetime
    import unittest
    import inspect
    import sys
    import os
    import pysnooper
    import pycompat
    import threading
    import functools
    import traceback
    import opcode
    import utils
    import variable

    utils.DISABLED = True
    variable.DISABLED = True

    thread_global = threading.local()

    class Watch:
        def __init__(self, name):
            self.name = name
        def get_value(self, frame):
            return eval(self.name, frame.f_globals, frame.f_locals)

    class BaseVariable(Watch):
        def __init__(self, name):
            Watch.__init__(self,name)

        def get_value(self, frame):
            return

# Generated at 2022-06-12 19:50:42.814438
# Unit test for method __exit__ of class Tracer

# Generated at 2022-06-12 19:50:54.239214
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    foo = 'foo'
    assert (Tracer().trace(frame = None, event = 'call', arg = 1) == None)
    assert (Tracer().trace(frame = None, event = 'exception', arg = 1) == None)
    assert (Tracer().trace(frame = None, event = 'line', arg = 1) == None)
    assert (Tracer().trace(frame = None, event = 'return', arg = 1) == None)
    assert (Tracer().trace(frame = None, event = 'opcode', arg = 1) == None)
    assert (Tracer().trace(frame = None, event = 'c_call', arg = 1) == None)
    assert (Tracer().trace(frame = None, event = 'c_exception', arg = 1) == None)

# Generated at 2022-06-12 19:51:15.332882
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # Run Clock(__call__)
    class DummyOutput(object):
        def __init__(self):
            self.written = []
        def __call__(self, text):
            self.written.append(text)
    class Exploding(BaseVariable):
        def get_repr(self, value, custom_reprs, normalize):
            return "exploded"
    def function():
        pass
    def ex_function():
        raise NotImplementedError
    def gen_function():
        raise StopIteration()
    depth = 1

# Generated at 2022-06-12 19:51:20.121199
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    from pysnooper.tracing import Tracer
    from pysnooper.utils import suppress_stdout_stderr
    with suppress_stdout_stderr():
        tracer = Tracer()
        tracer.watch = {}
        tracer.frame_to_local_reprs = {}
        tracer.start_times = {}
        tracer.depth = 1
        tracer.prefix = ''
        tracer.thread_info = ''
        tracer.thread_info_padding = ''
        tracer.target_codes = set()
        tracer.target_frames = set()
        tracer.thread_local = threading.local()
        tracer.custom_repr = ''
        tracer.last_source_path = ''
        tracer.max_variable_length = 100
        tracer.normal

# Generated at 2022-06-12 19:51:23.500492
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    assert True # TODO: implement your test here


# Generated at 2022-06-12 19:51:33.404077
# Unit test for constructor of class Tracer
def test_Tracer():
    tracer = Tracer()
    foo = 1
    tracer.watch = ['foo']
    frame = inspect.currentframe()
    local_reprs = get_local_reprs(frame,
                                  watch=tracer.watch, custom_repr=(),
                                  max_length=100,
                                  normalize=False,
                                  )
    assert repr(local_reprs) == "OrderedDict([('foo', '1')])"

    # Test prefix
    tracer.prefix = 'ZZZ '
    assert tracer.prefix == 'ZZZ '

    # Test max_variable_length = None

# Generated at 2022-06-12 19:51:42.043853
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
  func_name = 'test_Tracer___exit__'
  tracer = Tracer()
  # In this case, there is no exception
  def test_no_exception():
    time_interval_list = []
    class fake_datetime():
      @staticmethod
      def now():
        obj = fake_datetime()
        time_interval_list.append(obj)
        obj._delta = 1
        return obj
      def __sub__(self, other):
        if isinstance(other, fake_datetime):
          return other._delta
        else:
          return NotImplemented
    def f(depth):
      with tracer:
        pass
    # The original datetime.datetime is saved before being replaced
    saved_datetime_datetime = datetime_module.datetime
    datetime

# Generated at 2022-06-12 19:51:44.430445
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    with pytest.raises(NotImplementedError):
        Tracer()(coro)



# Generated at 2022-06-12 19:51:53.218803
# Unit test for constructor of class Tracer

# Generated at 2022-06-12 19:52:01.426500
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    code = 'def foo(): pass'
    lines = code.splitlines()
    try:
        import IPython
    except ImportError:
        pass
    else:
        ipython_shell = IPython.get_ipython()
        ipython_shell.run_cell(code, store_history=True)
        ipython_shell.run_cell('foo()', store_history=True)
        assert ipython_shell.history_manager.get_range(2, 3)[0][2] == code
    assert get_path_and_source_from_frame(sys._getframe())[1] == lines



# Generated at 2022-06-12 19:52:05.065927
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    frame = sys._getframe()
    file_name, source = get_path_and_source_from_frame(frame)
    assert file_name == inspect.getsourcefile(test_get_path_and_source_from_frame)



# Generated at 2022-06-12 19:52:07.555954
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def func():
        pass
    res = Tracer()(func)
    pass



# Generated at 2022-06-12 19:52:52.405808
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import tempfile
    import os
    import sys
    import imp
    import textwrap
    source = '''
    # Some source
    a = 1
    '''
    source = textwrap.dedent(source)
    encoding = 'utf-8'
    with tempfile.NamedTemporaryFile(mode='w', suffix='py') as f:
        f.write(source)
        f.flush()
        sys.path.append(os.path.dirname(f.name))
        module = imp.load_source(os.path.basename(f.name), f.name)
        assert module.__file__ == f.name
        assert get_path_and_source_from_frame(
            inspect.currentframe(),
        ) == (f.name, source.splitlines(True))


# Generated at 2022-06-12 19:52:58.880063
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import os
    e = os.path.abspath('./testing/mock_pysnooper_files/test_Tracer___exit__.py')
    with open(e) as f:
        ex = f.read()
    assert ex.strip() == '''\
Tracer___exit__
Elapsed time: 0.0
        Elapsed time: 0.0'''.strip()


# Generated at 2022-06-12 19:53:09.465073
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    path = os.path.join(temp_dir.name, 'log.txt')
    f = FileWriter(path, False)
    f.write("1st Line\n")
    f.write("2nd Line\n")
    f.write("3rd Line\n")
    with open(path, 'r') as log_file:
        assert log_file.read() == '1st Line\n2nd Line\n3rd Line\n'
    temp_dir.cleanup()
    temp_dir = tempfile.TemporaryDirectory()
    path = os.path.join(temp_dir.name, 'log.txt')
    f = FileWriter(path, True)
    f.write("1st Line\n")

# Generated at 2022-06-12 19:53:17.441423
# Unit test for constructor of class Tracer
def test_Tracer():
    tracer = Tracer(output=None)
    assert tracer.watch == []
    assert tracer.depth == 1
    assert tracer.prefix == ''
    tracer = Tracer(output=None, watch=[1,2], watch_explode=[3,4],
                    depth=2, prefix='prefix', overwrite=True, thread_info=True,
                    custom_repr=[(object, object.__repr__), (1, object.__repr__)],
                    max_variable_length=100, normalize=True,
                    relative_time=True)
    assert isinstance(tracer.watch[0], CommonVariable) and isinstance(
                                                     tracer.watch[1], CommonVariable)

# Generated at 2022-06-12 19:53:24.077559
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    class Foo:
        @pysnooper.snoop()
        def foo(n):
            pass
    assert pysnooper.__enter__.__code__.co_filename == 'pysnooper.py'
    foo = Foo()
    with pytest.raises(AssertionError):
        foo.foo(2)

# Generated at 2022-06-12 19:53:27.596497
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, 'foo.txt')
        writer = FileWriter(path, True)
        writer.write('super')
        writer.write('califragilisticexpialidocious')
        with open(path, 'r', encoding='utf-8') as f:
            assert f.read() == 'supercalifragilisticexpialidocious'
test_FileWriter_write()



# Generated at 2022-06-12 19:53:32.531802
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    with pytest.raises(NotImplementedError):

        @pysnooper.snoop()
        async def f():
            pass

# Generated at 2022-06-12 19:53:33.702607
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    pass # TODO


# Generated at 2022-06-12 19:53:41.077638
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import pickle
    def f():
        pass
    loader = pickle.Pickler(open('./testing_unit_test_get_path_and_source_from_frame.pkl', 'wb'))
    loader.dump(f)
    with open('./testing_unit_test_get_path_and_source_from_frame.pkl', 'rb') as fp:
        unloader = pickle.Unpickler(fp)
        f = unloader.load()
    frame = f.__code__.co_firstlineno
    path, source = get_path_and_source_from_frame(frame)
    assert path == './testing_unit_test_get_path_and_source_from_frame.pkl'
    assert source == ['def f():', '    pass']



# Generated at 2022-06-12 19:53:41.831822
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass

# Generated at 2022-06-12 19:55:01.878680
# Unit test for function get_write_function
def test_get_write_function():
    for x in (None, sys.stdout, open(os.path.join(os.getcwd(),
                                                  'test_temp_file.txt'), 'w')):
        def test(output):
            write = get_write_function(output, False)
            assert callable(write)
            write('test succeeded')
        if not isinstance(x, str):
            test(x)
            test(utils.Path(x))
            test(str(utils.Path(x)))
        test(x)
    for method_name in ('write', 'writelines', 'writestr'):
        class C:
            method = method_name
            def __getattribute__(self, attribute_name):
                if attribute_name == 'write':
                    raise AttributeError
                return super(C, self).__getattribute__

# Generated at 2022-06-12 19:55:06.495903
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import builtins
    assert not hasattr(builtins, '__snoop_output')
    @Tracer(output=sys.stdout, watch=['a'])
    def foo(a):
        return a + 1

    foo(2)
    del foo
    assert not hasattr(builtins, '__snoop_output')


# Generated at 2022-06-12 19:55:10.379638
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    from io import StringIO

    def inner_function():
        pass


    def outer_function():
        inner_function()


    with pycompat.redirect_stdout(StringIO()):
        with Tracer(output=None):
            outer_function()

# Generated at 2022-06-12 19:55:17.209176
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .common_variables import __file__
    import pyramid
    def get_path_and_source():
        def test():
            return get_path_and_source_from_frame(inspect.currentframe())
        return test
    test_module_path, test_module_source = get_path_and_source()()
    assert test_module_path == __file__
    pyramid_module_path, pyramid_module_source = get_path_and_source_from_frame(
        inspect.getouterframes(inspect.currentframe())[1][0]
    )
    assert '/pyramid/__init__.py' in pyramid_module_path
    assert 'from .request import Request' in pyramid_module_source

# Generated at 2022-06-12 19:55:18.438174
# Unit test for function get_path_and_source_from_frame

# Generated at 2022-06-12 19:55:24.786563
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def test_func():
        i = 3
        j = 5
        return i * j

    test_func()
    file_name, source = get_path_and_source_from_frame(
        sys._getframe().f_back)
    assert file_name == __file__
    assert source[0] == 'def test_func():'
    assert source[1] == '    i = 3'
    assert source[-1] == '    return i * j'



# Generated at 2022-06-12 19:55:26.331085
# Unit test for constructor of class Tracer
def test_Tracer():
    def foo():
        x = 5
        return x

    tracer = Tracer()
    tracer.write('hello')

# Generated at 2022-06-12 19:55:33.026112
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer()
    tracer.write = mock.Mock()
    tracer._write = mock.Mock()
    tracer.watch = ('hello',)
    tracer.depth = 1
    tracer.prefix = ''
    tracer.thread_info = True
    tracer.thread_info_padding = 0
    tracer.target_codes = set([])
    tracer.target_frames = set([])
    tracer.thread_local = mock.Mock()
    tracer.thread_local.__dict__ = {'original_trace_functions': []}
    tracer.custom_repr = ()
    tracer.last_source_path = None
    tracer.max_variable_length = 100
    tracer.normalize = False
    tracer.relative_time = False


# Generated at 2022-06-12 19:55:40.729720
# Unit test for constructor of class Tracer
def test_Tracer():
    # Test watch
    output = io.StringIO()
    watch = Tracer(output=output, watch=(
        'var_1',
        'var_2',
        'var_3',
    ))
    assert 3 == len(watch.watch)
    assert CommonVariable('var_1') == watch.watch[0]
    assert CommonVariable('var_2') == watch.watch[1]
    assert CommonVariable('var_3') == watch.watch[2]

    # Test watch_explode
    watch = Tracer(output=output, watch_explode=(
        'var_1',
        'var_2',
        'var_3',
    ))
    assert 3 == len(watch.watch)
    assert Exploding('var_1') == watch.watch[0]

# Generated at 2022-06-12 19:55:46.916858
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import cool_module
    import foo.bar.baz
    module_name = 'foo.bar.baz'
    file_name = 'foo/bar/baz.py'
    frame = cool_module.cool_frame
    # Make sure our module is not in sys.modules, so that the function
    # get_path_and_source_from_frame calls `__loader__.get_source`.
    assert module_name not in sys.modules

    path, source = get_path_and_source_from_frame(frame)
    assert module_name == path
    assert all(isinstance(line, pycompat.text_type) for line in source)

    # Check that the same will be returned from the cache on the next
    # call: