

# Generated at 2022-06-12 19:46:56.803530
# Unit test for function get_write_function
def test_get_write_function():
    from . import utils
    from six.moves import StringIO
    import io
    import os
    import tempfile
    import functools


    with open(__file__, 'rb') as file:
        data = file.read()


    write_to_fake_file = functools.partial(
        get_write_function,
        output=io.BytesIO(),
        overwrite=True
    )
    write_to_fake_file(data)


    write_to_fake_file = functools.partial(
        get_write_function,
        output=io.BytesIO(),
        overwrite=False
    )
    write_to_fake_file(data)



# Generated at 2022-06-12 19:47:02.340392
# Unit test for function get_local_reprs
def test_get_local_reprs():
    from . import variables
    watch_path = r'*.xxx'
    (exploding_variable, ) = tuple(variables.ScannerVariable.iter_variables(
        path=watch_path, watched_frame=None
    ))
    assert list(exploding_variable.items({}))


# Generated at 2022-06-12 19:47:09.820550
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    from io import StringIO
    from random import choice
    from string import ascii_letters
    output = StringIO()
    def random_string():
        return ''.join(choice(ascii_letters) for _ in range(10))
    with Tracer(output) as tracer:
        x = random_string()
        y = random_string()
    output_string = output.getvalue()
    assert 'x =' in output_string
    assert 'y =' in output_string
    assert 'Elapsed time:' in output_string

# Generated at 2022-06-12 19:47:12.133570
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    """Test method Tracer.__enter__"""
    print(__name__, ': Test method Tracer.__enter__')


# Generated at 2022-06-12 19:47:22.936771
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    test_frame = inspect.currentframe().f_back
    test_frame.f_locals = {'test':'test'}
    test_code = test_frame.f_code
    test_code.co_filename = 'testfilename.py'
    test_code.co_code = [b'A',b'R',b'G',b'R',b'E',b'T',b'V',b'A',b'L',b'U',b'E']
    test_code.co_lasti = 1
    test_arg = None
    tracer = Tracer()
    tracer.write = mock.MagicMock()
    tracer.trace(test_frame, 'call', test_arg)
    assert b'RETURN_VALUE' in opcode.opname

# Generated at 2022-06-12 19:47:24.381690
# Unit test for function get_local_reprs
def test_get_local_reprs():
    frame = sys._getframe()

# Generated at 2022-06-12 19:47:28.750805
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def foo():
        '''
            def bar():
                pass
        '''
        pass

    frame = inspect.currentframe()
    frame = frame.f_back.f_back
    file_name, source = get_path_and_source_from_frame(frame)
    assert file_name == inspect.getsourcefile(foo)
    assert source == ['    def bar():',
                      '        pass']



# Generated at 2022-06-12 19:47:38.718654
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import codeop, io
    frame = inspect.currentframe()
    source_code = io.StringIO('test_get_path_and_source_from_frame()\n')
    file_name_base, file_extension = os.path.splitext(__file__)
    file_name = file_name_base + '_test_get_path_and_source_from_frame' + file_extension
    with open(file_name, 'w') as f:
        f.write(source_code.getvalue())

# Generated at 2022-06-12 19:47:43.453487
# Unit test for constructor of class Tracer
def test_Tracer():
    # TODO: Add more tests for the snoop() decorator
    @snoop(watch=['variable'])
    def foo():
        variable = 5
        variable = variable + 2
        # set variable to None to test deleting old variables
        variable = None

    foo()


# Generated at 2022-06-12 19:47:50.331524
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    import doctest
    import unittest
    suite = doctest.DocTestSuite(optionflags=(doctest.REPORT_NDIFF | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS))
    suite.addTest(doctest.DocFileSuite('README.rst', optionflags=(doctest.REPORT_NDIFF | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

# Generated at 2022-06-12 19:48:15.750641
# Unit test for function get_local_reprs
def test_get_local_reprs():
    frame = sys._getframe()
    
    x = 20
    y = 40
    assert get_local_reprs(frame) == \
           {'x': '20', 'y': '40'}
    assert get_local_reprs(frame,
                           watch=[CommonVariable('x'), CommonVariable('y')]) \
              == {'x': '20', 'y': '40', "localvar_x": '20', "localvar_y": '40'}



# Generated at 2022-06-12 19:48:21.001217
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    import io
    import sys
    import textwrap
    source = textwrap.dedent('''
        def foo():
            x = 4
            y = 5
            z = 6
    ''')

    stream = io.StringIO()
    sys.stdout = stream
    s = Tracer()
    s.trace({"f_lineno": 2, "f_code": {"co_filename": "filename.txt", "co_code": b"test"}, "f_back": "test"}, "call", "test")
    sys.stdout = sys.__stdout__
    assert stream.getvalue().strip() == "    Source path:... filename.txt"

# Generated at 2022-06-12 19:48:30.963221
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    class A:
        def add(self, b):
            a = 1
            c = a + b
            return c

    def add(a, b):
        c = a + b
        return c

    class TestTracerTrace(unittest.TestCase):
        def test_lines(self):
            tracer = Tracer(output=StringIO(), watch=('a', 'b', 'c'))
            with tracer:
                add(1, 2)
                with tracer:
                    A().add(2)

            result = tracer.output.getvalue()

            self.assertTrue(result.count('Modified var:.. c ='), 1)
            self.assertTrue(result.count('Modified var:.. b ='), 2)

# Generated at 2022-06-12 19:48:42.272834
# Unit test for method write of class FileWriter
def test_FileWriter_write():
    import os
    import shutil
    import tempfile
    from __future__ import print_function
    from .tests import helpers
    with helpers.temp_folder(prefix='test_core_') as folder_path:
        file_writer = FileWriter(os.path.join(folder_path, 'output_file.txt'),
                                 overwrite=True)
        assert not os.path.exists(file_writer.path)
        file_writer.write('Writing to file\n')
        assert os.path.exists(file_writer.path)
        with open(file_writer.path, 'r') as f:
            assert f.read() == 'Writing to file\n'
        file_writer.write('Writing to file again\n')
        with open(file_writer.path, 'r') as f:
            assert f

# Generated at 2022-06-12 19:48:47.752840
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def dummy_function():
        pass
    dummy_function_frame = dummy_function.__code__.co_filename
    dummy_function_source = dummy_function.__code__.co_code.splitlines()

    assert get_path_and_source_from_frame(dummy_function.__code__.co_filename) \
           == (dummy_function_frame, dummy_function_source)



# Generated at 2022-06-12 19:48:48.458852
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    pass



# Generated at 2022-06-12 19:48:56.898960
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import contextlib
    import types
    class MockLoader(object):
        def get_source(self, module_name):
            if module_name == 'source_is_none':
                return None
            if module_name == 'source_is_empty':
                return ''
            if module_name == 'source_is_lines':
                return 'foo\nbar'
            if module_name == 'source_is_unicode':
                return u'בדיקה'
            if module_name == 'source_is_not_lines':
                return ['foo', 'bar']
            if module_name == 'source_is_bytes':
                return b'foo\nbar'

# Generated at 2022-06-12 19:49:07.032487
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    import inspect
    test_frame = inspect.currentframe()

# Generated at 2022-06-12 19:49:16.468043
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    def local_reprs_has(local_reprs, variable_name, variable_repr):
        """ local_reprs_has returns True if no variable named variable_name
            was found in local_reprs, or if it was found and its _repr is
            equal to variable_repr. """
        if variable_name not in local_reprs:
            return True
        return local_reprs[variable_name] == variable_repr

    # Let's test Tracer.trace(frame, event, arg) by calling it directly
    with mock.patch.object(Tracer, 'write', return_value=None):
        tracer = Tracer()
        frame = inspect.currentframe()
        event = 'call'
        arg = None
        assert tracer.trace(frame, event, arg) == tr

# Generated at 2022-06-12 19:49:28.502685
# Unit test for method __exit__ of class Tracer
def test_Tracer___exit__():
    test_cases = [
        # (exception_type, exception_value, exception_traceback, 
        # expected_exception_type, expected_exception_value, expected_exception_traceback):


        # No exception (regular quit):
        (None, None, None, 
         None, None, None),

        # Exceptions:
        (Exception, Exception('foo'), Exception, 
         Exception, Exception('foo'), Exception),

        (Exception, Exception('foo'), object, 
         Exception, Exception('foo'), object),

        (None, None, object, 
         None, None, object),

        (object, None, None, 
         object, None, None),
    ]

    # This test is really meant to be run with multiprocessing=False.

    # TODO: get "expected" and "actual

# Generated at 2022-06-12 19:49:53.869131
# Unit test for constructor of class Tracer
def test_Tracer():
    import pprint
    import sys

    @snoop(overwrite=False, prefix='@')
    def foo(a, b=3):
        c = a + b
        print(a)
        return c


    @snoop()
    def bar():
        return 1


    try:
        bar(1)
    except TypeError:
        pass
    foo(4)
    foo(1, 2)
    try:
        foo(1, 2, 3)
    except TypeError:
        pass
    print('Done')

# Generated at 2022-06-12 19:50:04.278401
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    # Copied from Python 2.7.13 (file_name, source) =
    def test_function(a, b, c):
        # Breakpoint at this line
        return a * b * c
    frame = utils.get_frame(test_function)
    (file_name, source) = get_path_and_source_from_frame(frame)
    assert file_name == inspect.getsourcefile(test_function)
    assert len(source) > 8
    assert source[0].startswith('def ')
    assert source[-1] == '    return a * b * c'
test_get_path_and_source_from_frame()



# Generated at 2022-06-12 19:50:05.443359
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    # No parameters
    pytest.skip("No way to test this right now.")

# Generated at 2022-06-12 19:50:14.076728
# Unit test for constructor of class Tracer
def test_Tracer():
    '''
    Test the constructor of class Tracer.
    '''
    def test_decorator(output=None, watch=(), watch_explode=(), depth=1,
                       prefix='', overwrite=False, thread_info=False,
                       custom_repr=(), max_variable_length=100,
                       normalize=False, relative_time=False):
        return Tracer(
            output=output,
            watch=watch,
            watch_explode=watch_explode,
            depth=depth,
            prefix=prefix,
            overwrite=overwrite,
            thread_info=thread_info,
            custom_repr=custom_repr,
            max_variable_length=max_variable_length,
            normalize=normalize,
            relative_time=relative_time
        )


# Generated at 2022-06-12 19:50:20.107044
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    global DISABLED
    DISABLED = False
    output = io.StringIO()
    overwrite = None
    function = None
    watch = None
    watch_explode = None
    depth = None
    prefix = None
    thread_info = None
    custom_repr = None
    max_variable_length = None
    normalize = None
    relative_time = None
    sut = Tracer(output, watch, watch_explode, depth, prefix, overwrite,
                 thread_info, custom_repr, max_variable_length, normalize,
                 relative_time)
    _frame = None
    test_utils.capture_output(sut.__enter__)()
    test_utils.assertTrue(True)


# Generated at 2022-06-12 19:50:27.311536
# Unit test for method __call__ of class Tracer
def test_Tracer___call__():
    def expected_output(function, arg):
        return utils.expected_output(function, arg, watch=[])
    def expected_output_watched(function, arg, watched_variable):
        return utils.expected_output(function, arg, watch=[watched_variable])

    #
    # Unit test for method __call__ of class Tracer, without context
    #

    @snoop(watch=[])
    def foo(x):
        x = x + 1
        return x

    _, _, actual_output = utils.capture_output(foo, (1,))
    assert actual_output == expected_output(foo, 1)

    _, _, actual_output = utils.capture_output(foo, (2,))
    assert actual_output == expected_output(foo, 2)


# Generated at 2022-06-12 19:50:29.415699
# Unit test for method __enter__ of class Tracer
def test_Tracer___enter__():
    # Test for function Tracer.__enter__
    Tracer.__enter__()
    assert 1 == 1

# Generated at 2022-06-12 19:50:35.288734
# Unit test for function get_path_and_source_from_frame
def test_get_path_and_source_from_frame():
    def dummy_func(x):
        y = x + 1
        return y
    assert get_path_and_source_from_frame(dummy_func.__code__.co_filename,
                                          dummy_func.__code__) \
        == (os.path.abspath(dummy_func.__code__.co_filename),
            ['def dummy_func(x):'])
    assert get_path_and_source_from_frame('<ipython-input-1-7bd9e67d8c7f>',
                                          dummy_func.__code__) \
        == ('<ipython-input-1-7bd9e67d8c7f>',
            ['def dummy_func(x):', '    y = x + 1', '    return y'])



# Generated at 2022-06-12 19:50:38.496184
# Unit test for function get_write_function
def test_get_write_function():
    from . import utils
    from .utils.fake_stream import FakeStream
    from .utils.text import indented
    def f(s):
        print(s)

    for output in (None, sys.stderr, sys.stdout, f, FakeStream(),
                   indented(FakeStream())):
        try:
            get_write_function_output = get_write_function(output, False)
            get_write_function_output(u'hello')
        except Exception:
            pass
    try:
        get_write_function(None, True)
    except Exception:
        pass
    
    

# Generated at 2022-06-12 19:50:46.894483
# Unit test for method trace of class Tracer
def test_Tracer_trace():
    # Tracer class
    # test_Tracer_trace()
    '''
    Testing: Tracer.trace()
    '''
    ############################################################################
    ### Variables: #############################################################
    #                                                                         #
    # The below are used to test whether the trace function is working.       #
    # They are set by the test code in `test_Tracer_trace()`.                 #
    #                                                                         #
    snoop_data = {'output': '', 'watch_expanded': False,
                  'depth_incremented': False,
                  'depth_decremented': False, 'timestamp': [],
                  'event': [], 'line': [], 'source': [],
                  'exception': [], 'return_value': []}