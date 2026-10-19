

# Generated at 2022-06-12 19:46:43.328223
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    _self = Tracer(output=None, watch=('foo',), watch_explode=('bar',), depth=1,
                   prefix='', max_variable_length=100, normalize=False, overwrite=True,
                   thread_info=False, custom_repr=())
    _frame = PassFrame()
    _event = 'call'
    _arg = None
    _frame.f_lineno = 5
    _frame.f_lasti = 10
    _frame.f_code = PassCode()
    _frame.f_globals = {'foo':'0', 'bar':{'1':2}}
    _frame._frame_repr = {'foo':'0', 'bar':{'1':2}}


# Generated at 2022-06-12 19:46:48.079889
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = pysnooper.Snooper(watch_explode=('foo', 'self'), depth=1)

    @tracer
    def bar(foo):
        print('hi', foo)

    bar(foo='bar')


# Generated at 2022-06-12 19:46:59.327071
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    tracer = Tracer(overwrite=True)
    tracer._write = MagicMock()
    tracer.write = MagicMock()

    # exc_type = exc_value = exc_traceback = None
    tracer.__exit__(None, None, None)

    # exc_type = exc_value = exc_traceback = Exception("test exception")
    # tracer.write("Elapsed time")
    # tracer._write("... ")
    tracer.write.assert_called_with("    Elapsed time: 0:00:00")
    tracer._write.assert_called_with("")
## END OF SNOOPER: do NOT delete this line and below this line ##


# Generated at 2022-06-12 19:47:00.466980
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    pass


# Generated at 2022-06-12 19:47:11.441442
# Unit test for function get_write_function
def test_get_write_function():
    from .tests.test_utils import assert_raises, output_tester, assert_equal
    import contextlib

    assert_equal(get_write_function('blah.txt', overwrite=False)('a'),
                 FileWriter('blah.txt', overwrite=False).write('a'))

    with output_tester(strip=True) as ot:
        get_write_function(None, overwrite=False)('b')
    assert_equal(ot.output, 'b')

    def do_nothing(s):
        pass

    assert_equal(get_write_function(do_nothing, overwrite=False)('c'),
                 do_nothing('c'))

    with assert_raises(Exception):
        get_write_function(None, overwrite=True)
    with assert_raises(Exception):
        get_write_

# Generated at 2022-06-12 19:47:20.997021
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    from combi._python_toolbox.third_party import temp_file
    with temp_file.TemporaryFile(delete=False, mode='w+') as fp:
        f1 = FileWriter(fp.name, False)
        f1.write('This is the first line.\n')
        f2 = FileWriter(fp.name, True)
        f2.write('This is the second line.\n')
        f3 = FileWriter(fp.name, False)
        f3.write('This is the third line.\n')
        assert fp.read() == "This is the second line.\nThis is the third line.\n"



# Generated at 2022-06-12 19:47:22.640166
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    tracer = Tracer()
    tracer.trace(None, None, None)

 

# Generated at 2022-06-12 19:47:30.928827
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import pysnooper
    with OutputCollector() as output:
        @pysnooper.snoop(watch=('self'))
        def f():
            local = 'local'
            nonlocal_ = locals()
            nonlocal_.update(globals())
            return nonlocal_

        class C:
            @pysnooper.snoop()
            def m(self, n):
                return self, n
    # Should trigger the watch
    assert f() == {'local': 'local', 'nonlocal_': {'local': 'local', 'nonlocal_': {'nonlocal_': {...}}, 'nonlocal_': {...}}}
    # Should keep the watch on several calls

# Generated at 2022-06-12 19:47:33.212268
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    @pysnooper.snoop()
    def foo():
        def bar():
            pass
        var = 42
        var2 = 'hello'


# Generated at 2022-06-12 19:47:44.046147
# Unit test for constructor of class Tracer
def test_Tracer():
    class Dummy:
        def __init__(self):
            self.s = 'spam'
        def __repr__(self):
            return self.s

    def my_custom_repr(x):
        return 'abc'

    tracer = Tracer(watch=('x', 'y', 'z', 'a', 'b', 'self', 'cls'),
                    watch_explode=('x', 'a', 'self', 'cls', 'never_used_variable'),
                    depth=2, prefix='', overwrite=False, thread_info=False,
                    custom_repr=((type(Dummy()), my_custom_repr),
                                 (lambda x: x > 5, lambda x: 'over 5')),
                    max_variable_length=None, normalize=False, relative_time=False)
   

# Generated at 2022-06-12 19:48:13.056788
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import re
    import pycompat
    import collections
    import datetime
    import threading
    import datetime_module
    import inspect
    import functools
    import sys
    import os
    import traceback
    import opcode
    import pycompat
    import threading
    import pycompat
    import inspect
    import functools
    import threading
    import pycompat
    import inspect
    import functools
    import threading
    import os
    import pycompat
    import inspect
    import threading
    import inspect
    import functools
    import threading
    import pycompat
    import inspect
    import functools
    import datetime_module
    import threading
    import pycompat
    import inspect
    import functools
    import threading
    import traceback

# Generated at 2022-06-12 19:48:17.831352
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def function(x):
        return x + 1
    frame = sys._getframe(1)
    result = get_path_and_source_from_frame(frame)
    source = result[1]
    assert source[frame.f_lineno - 1].strip() == 'return x + 1'



# Generated at 2022-06-12 19:48:24.189022
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def foo(): pass
    def bar(): pass
    class Foo:
        def aa(self): pass
        def bb(self): pass
    # Test case #0
    foo_tracer = Tracer(watch=('foo', ), watch_explode=('self', ))
    assert foo_tracer(foo) == foo
    assert foo_tracer(bar) == bar
    foo_instance = Foo()
    assert foo_tracer(Foo) == Foo
    # Test case #1
    bar_tracer = Tracer(watch=('foo', ), watch_explode=('self', ),
                        depth=1, prefix='', overwrite=False, thread_info=False,
                        custom_repr=(), max_variable_length=100, normalize=False,
                        relative_time=False)

# Generated at 2022-06-12 19:48:37.315326
# Unit test for constructor of class Tracer
def test_Tracer():
    class A:
        def __init__(self, x):
            self.x = x
            self.y = 7
            self.z = 9
            self.q = [1, 2, 3]
            self.w = {'a': 1, 'b': 2}

        @pysnooper.snoop(watch=('self', 'self.x'), watch_explode=('self.q',),
                         depth=2, prefix='{z}: ', overwrite=True)
        def method1(self, b, c):
            self.y = 8
            self.q.append('x')
            self.q.append('y')
            d = 4
            self.q.append(d)
            self.temp = [b]
            self.temp.append(c)

# Generated at 2022-06-12 19:48:47.670068
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def test_func(a, *args, **kwargs):
        b = [1]
        c = 2
        d = [3]
        e = 4
        print(a)
        yield 1
        print(a, b, c, d, e)
        b.append(5)
        yield 2

    test_func(a=0)

    # test_snooper = Tracer()
    # test_snooper._write = lambda x: print(x, end="")
    # test_snooper.watch = (
    #     CommonVariable('a'),
    #     CommonVariable('b'),
    #     CommonVariable('c'),
    #     CommonVariable('d'),
    #     CommonVariable('e'),
    # )
    # test_snooper.depth = 1
    # test_snooper

# Generated at 2022-06-12 19:48:55.639849
# Unit test for method trace of class Tracer
def test_Tracer_trace():	
    # Python >= 2.7
    from unittest import TestCase
    from pysnooper import tracer
    if (sys.version_info > (3, 0)):
        from io import StringIO
    else:
        from StringIO import StringIO
    from types import FrameType
    from datetime import datetime
    from contextlib import contextmanager

    tracer.DISABLED = False
    tracer.datetime_module = datetime

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys

# Generated at 2022-06-12 19:49:04.544402
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    import pysnooper.utils
    import datetime

    class AssertingWrite:
        def __init__(self):
            self.written = []

        def __call__(self, text):
            self.written.append(text)

    class TargetClass:
        @pysnooper.snoop()

        def test_function(self):
            return 1

        @pysnooper.snoop()
        def test_function1(self):
            return 1

    asserting_write = AssertingWrite()
    with Tracer(asserting_write) as tracer:
        target_class_instance = TargetClass()
        target_class_instance.test_function()
    target_class_instance.test_function1()

    # Find the start time of the snoop
    time_start = datetime.dat

# Generated at 2022-06-12 19:49:11.845168
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def run_Tracer_trace():
        # print('Entering run_Tracer_trace')
        snooper = pysnooper.Snooper('some_file_to_write')
        snooper._write = lambda x: None
        # print('Created snooper')
        snooper.watch = ['a', 'b']
        snooper.frame_to_local_reprs = {
        }
        # print('Running Tracer.trace')
        snooper.trace(None, 'line', None)
        # print('Exiting run_Tracer_trace')
        return snooper
    import sys
    sys.setrecursionlimit(100000)
    snooper = run_Tracer_trace()
    # print(snooper.frame_to_local_reprs)



# Generated at 2022-06-12 19:49:13.912200
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Raise AssertionError if the method has no docstring
    assert Tracer.__exit__.__doc__


# Generated at 2022-06-12 19:49:25.272161
# Unit test for constructor of class Tracer
def test_Tracer(): 
    t = Tracer()
    assert t.watch == []
    assert t.frame_to_local_reprs == {}
    assert t.start_times == {}
    assert t.depth == 1
    assert t.prefix == ''
    assert t.target_codes == set()
    assert t.target_frames == set()
    assert isinstance(t.thread_local, threading.local)
    assert t.custom_repr == ()
    assert t.last_source_path is None
    assert t.max_variable_length == 100
    assert t.normalize is False
    assert t.relative_time is False


# Generated at 2022-06-12 19:50:07.541875
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    try:
        import IPython
    except ImportError:
        return
    ipython_shell = IPython.get_ipython()
    ipython_shell.run_cell("def foo(a):\n    a = 7\n    b = 8")
    foo = ipython_shell.user_ns['foo']
    frame = foo.__code__.co_firstlineno
    assert get_path_and_source_from_frame(frame)[1][0] == 'def foo(a):'




# Generated at 2022-06-12 19:50:13.100298
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from .fake import get_fake_frame
    frame = get_fake_frame('')
    frame.f_globals = {'__name__': 'hello.world'}
    frame.f_code.co_filename = 'hello.py'
    frame.f_lineno = 15
    path, source = get_path_and_source_from_frame(frame)
    assert path == 'hello.py'
    assert isinstance(source, (list, UnavailableSource))
    assert source[0] == 'SOURCE IS UNAVAILABLE'



# Generated at 2022-06-12 19:50:16.795749
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    instance = pysnooper.snoop()
    exc_type = type
    exc_value = type()
    exc_traceback = None
    instance.__exit__(exc_type, exc_value, exc_traceback)



# Generated at 2022-06-12 19:50:17.781266
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    pass



# Generated at 2022-06-12 19:50:22.009970
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class TestCase(unittest.TestCase):
        def test_case(self):
            @pysnooper.snoop()
            def function():
                a = 1
                b = 'te'
                raise Exception('test')
            function()
    unittest.main(module=__name__, argv=[sys.argv[0], __file__])


# Generated at 2022-06-12 19:50:28.513527
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Simple 'Hello World' program.
    s = "print('Hello World')"
    # Root logger:
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    # Root logger's handler:
    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)
    # Create Tracer:
    tracer = Tracer(logger)
    # Create frame object:
    frame = utils.create_frame(s)
    # Trace frame:
    tracer.trace(frame=frame, event='call', arg=None)
    # Assertion 1:
    assert tracer.target_codes == {frame.f_code}, \
            "test_Tracer_trace: Assertion 1 failed."

# Generated at 2022-06-12 19:50:35.341367
# Unit test for constructor of class Tracer
def test_Tracer():
    assert Tracer().depth == 1
    assert Tracer(depth=3).depth == 3

    custom_repr = (lambda x: 'CUSTOM',)
    assert Tracer(watch=custom_repr).watch == [CommonVariable(custom_repr)]
    assert Tracer(watch_explode=custom_repr).watch == [Exploding(custom_repr)]

    multiple_vars = (custom_repr, custom_repr)
    assert Tracer(watch=multiple_vars).watch == [CommonVariable(custom_repr),
                                                 CommonVariable(custom_repr)]


# Generated at 2022-06-12 19:50:37.907558
# Unit test for constructor of class Tracer
def test_Tracer():
    def bar():
        pass

    def foo():
        a = 1
        b = 2
        bar()

    with Tracer(watch=["a"]):
        foo()

# Generated at 2022-06-12 19:50:42.468468
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    global DISABLED
    DISABLED = False
    def test(x):
        return x ** 2
    tracer = Tracer()
    tracer.trace(test.__closure__, 'call', None)
    # DISABLED status check
    DISABLED = True
    tracer.trace(test.__closure__, 'call', None)
    print('test_Tracer_trace succeeded')

# Generated at 2022-06-12 19:50:53.611590
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
  import io
  import tempfile
  import unittest.mock

  from pysnooper.utils import get_frame_code, get_path_and_source_from_frame

  from pysnooper.tracer import Tracer

  def test_method(self):
    pass

  def test_function():
    pass

  def test_coroutine():
    pass

  def test_generator():
    pass

  def test_async_gen():
    pass

  try:
    test_coroutine = asyncio.coroutine(test_coroutine)
    test_async_gen = asyncio.coroutine(test_async_gen)
  except NameError:
    pass

  spied_method_code = test_method.__code__
  spied_function_code = test_function.__code__

# Generated at 2022-06-12 19:52:09.279192
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    # Initialized instance of class Tracer
    # self = <pysnooper.tracing.Tracer object at 0x7f8a25d1f5f8>
    pass

# Generated at 2022-06-12 19:52:14.128039
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # Set up test objects
    with ExitStack() as stack:
        output = Output(stack)
        depth = 1
        prefix = ' '
        overwrite = False
        thread_info = False
        custom_repr = ()
        max_variable_length = 100
        normalize = False
        relative_time = False
        b = Tracer(output, depth, prefix, overwrite, thread_info, custom_repr,
                   max_variable_length, normalize, relative_time)
        # Call method __enter__
        b.__enter__()
        # Check whether output is correct
        assert output.output == []



# Generated at 2022-06-12 19:52:22.936757
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def trace(frame, event, arg):
        '''
        模拟python的trace function的返回值
        '''
        if frame.f_code.co_filename == __file__:
            # only trace pysnooper
            return trace
        return None

    def method_trace_function(*args, **kwargs):
        '''
        测试method_trace的测试函数
        '''
        print('Hello, World')
        print('My name is', __name__)
        # 抛出异常
        raise ValueError('TestExceptin')

    # 创建Tracer对象

# Generated at 2022-06-12 19:52:32.504747
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    global DISABLED
    DISABLED = False

    import io
    import sys
    import os
    import tempfile
    import contextlib
    import tempfile
    import threading
    import functools
    import inspect

    import pysnooper.utils

    # Import the "unscrambled" version of pysnooper so we can use it to
    # compare traces.
    sys.path.append('.')
    import unscrambled.pysnooper

    import pytest

    def get_new_tmp_file():
        fd, fname = tempfile.mkstemp()
        f = os.fdopen(fd, 'w')
        return f, fname

    def get_trace(fname):
        with open(fname, 'r') as f:
            trace = f.read()
       

# Generated at 2022-06-12 19:52:42.105174
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    make_test_file(
        'main.py',
        "from pysnooper import snoop"
        "@snoop()"
        "def main():"
        "  for i in range(5):"
        "    print(i)"
    )
    with captured_output() as (out, err):
        result = run_subprocess(['python', 'main.py'])
    stdout, stderr = out.getvalue().strip(), err.getvalue().strip()
    assert not stderr
    assert result == 0
    assert '>' in stdout

# setattr(Tracer, 'trace', Tracer.trace) # Add method to non_callable_member_names

# Generated at 2022-06-12 19:52:49.869548
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def f():
        source_and_path = get_path_and_source_from_frame(sys._getframe())
        assert source_and_path[0] == __file__

# Generated at 2022-06-12 19:52:52.785620
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    tracer = Tracer()
    try:
        with tracer:
            pass
    except Exception as exception:
        pytest.fail("Unexpected exception: " + str(exception))
    return tracer

# Generated at 2022-06-12 19:53:00.814613
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    from _py_stack_walker import utils
    from .test_utils import _py_stack_walker_dir
    file_name = os.path.join(_py_stack_walker_dir, 'utils.py')
    import inspect
    def get_source(function):
        frame = inspect.currentframe()
        while frame:
            function_in_frame = frame.f_locals.get(
                inspect.getframeinfo(frame)[2]
            )
            if function_in_frame is function:
                break
            frame = frame.f_back
        else:
            raise RuntimeError("Couldn't find function in any frame!")
        path_and_source = get_path_and_source_from_frame(frame)
        return path_and_source

# Generated at 2022-06-12 19:53:09.075166
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    state = {'setup_count': 0, 'teardown_count': 0, 'case_count': 0, 'error_count': 0}
    def setup_function(function):
        # This code runs before *EVERY* test function
        state['setup_count'] += 1

    def teardown_function(function):
        # This code runs after *EVERY* test function
        state['teardown_count'] += 1

    def test_numbers_3_4():
        assert 3 * 4 == 12
        state['case_count'] += 1

    def test_strings_a_3():
        assert 'a' * 3 == 'aaa'
        state['case_count'] += 1

    def test_strings_a_4():
        assert 'a' * 3 == 'aaa'

# Generated at 2022-06-12 19:53:15.038911
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import time
    import random
    import unittest.mock
    # mock the following function: time.time()
    time.time = unittest.mock.MagicMock(return_value=1540371665.5)
    # mock the following function/method: random.randint(0, number)
    random.randint = unittest.mock.MagicMock(return_value=3)
    # create an instance of Tracer for testing
    tracer = Tracer()

# Generated at 2022-06-12 19:55:52.664905
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    @pysnooper.snoop()
    def f(x, y, z):
        return x + y + z

    assert f(1, 2, 3) == 6
    assert f(7, 8, 9) == 24


# Generated at 2022-06-12 19:56:03.074461
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import tempfile

    def create_module(code, module_name='mod'):
        file_ = tempfile.NamedTemporaryFile('w', suffix='.py', delete=False)
        file_.write(code)
        file_.close()
        import sys
        import types
        import imp
        module = types.ModuleType(module_name)
        module.__file__ = file_.name
        sys.modules[module_name] = module
        imp.load_source(module_name, file_.name)
        return module

    # Testing source in file
    module0 = create_module("""def f(x): return x + 7""")
    module0.__loader__ = None
    frame = module0.f.__code__.co_firstlineno + 1
    path, source = get_path_and_source_