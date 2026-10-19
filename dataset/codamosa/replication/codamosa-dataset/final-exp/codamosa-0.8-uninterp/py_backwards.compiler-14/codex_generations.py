

# Generated at 2022-06-22 12:24:33.627282
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('example/src', 'example/build', CompilationTarget.ES5).count
    assert compile_files('example/src', 'example/build', CompilationTarget.ES6).count

# Generated at 2022-06-22 12:24:44.160164
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    import shutil
    import unittest
    import doctest

    def get_temp_dir():
        return tempfile.mkdtemp(prefix='tmp-py-to-js-')

    class CompileTestCase(unittest.TestCase):
        def setUp(self):
            self.input_ = get_temp_dir()
            self.output = get_temp_dir()

        def tearDown(self):
            shutil.rmtree(self.input_)
            shutil.rmtree(self.output)


# Generated at 2022-06-22 12:24:56.919487
# Unit test for function compile_files
def test_compile_files():
    from .files import InputOutput
    from .types import CompilationResult
    res = compile_files("./tests/sample_files/input",
                        "./tests/sample_files/output",
                        CompilationTarget.WEB)
    assert res == CompilationResult(1, 0, CompilationTarget.WEB, [])

    # Check directory tree is equal
    import filecmp
    assert filecmp.dircmp("./tests/sample_files/input",
                          "./tests/sample_files/output").diff_files == []

    # Check output file is identical

# Generated at 2022-06-22 12:25:08.109316
# Unit test for function compile_files
def test_compile_files():
    import pytest
    import os
    import sys

    # Directory with input files
    input_directory = os.path.join("..",
        "tests",
        "test_compiler",
        "test_compile_files")
    # Check input root directory exists
    test_directory = os.path.dirname(os.path.realpath(__file__))
    input_directory = os.path.join(test_directory, input_directory)
    if (not os.path.exists(input_directory)):
        print("Error: input root directory does not exist")
        print(input_directory)
        sys.exit(1)

    # Directory with expected output files
    expected_output = os.path.join("..",
        "tests",
        "test_compiler",
        "expected_output")
    #

# Generated at 2022-06-22 12:25:18.164139
# Unit test for function compile_files
def test_compile_files():
    from .files import get_input_output_paths
    from .transformers import transformers
    from .types import CompilationTarget
    from .utils.mocks import mock_ast_module
    from astunparse import dump
    from typing import List

    def _compile_file(paths: InputOutput, target: CompilationTarget) -> List[str]:
        with paths.input.open() as f:
            code = f.read()

        try:
            transformed, dependencies = _transform(paths.input.as_posix(),
                                                   code, target)
        except SyntaxError as e:
            raise CompilationError(paths.input.as_posix(),
                                   code, e.lineno, e.offset)


# Generated at 2022-06-22 12:25:25.813070
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from shutil import rmtree
    from tempfile import mkdtemp

    assert compile_files('input', 'output', CompilationTarget.PYTHON2,
                         root=mkdtemp()).count == 0
    
    assert compile_files(str(Path(__file__).parent / 'tests' / 'data' / 'test_file.py'),
                         'output', CompilationTarget.PYTHON2,
                         root=mkdtemp()).count == 1

# Generated at 2022-06-22 12:25:37.680408
# Unit test for function compile_files

# Generated at 2022-06-22 12:25:38.356751
# Unit test for function compile_files
def test_compile_files():
    assert True

# Generated at 2022-06-22 12:25:39.585805
# Unit test for function compile_files
def test_compile_files():
    from .autotests import run_tests
    run_tests(compile_files)

# Generated at 2022-06-22 12:25:50.793950
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationResult
    from .files import InputOutput
    from .transformers import FooTransformer, BarTransformer
    from .exceptions import TransformationError, CompilationError
    import os
    import types
    import collections
    import unittest

    class TestCompileFiles(unittest.TestCase):
        def test_it_returns_compilation_result(self):
            result = compile_files('input', 'output', CompilationTarget.DEFAULT)
            self.assertIsInstance(result, CompilationResult)

        def test_compile_single_file(self):
            result = compile_files(
                'tests/fixtures/single.py',
                'tests/outputs/single.py',
                CompilationTarget.DEFAULT)
            self.assertEqual(result.compiled, 1)
           

# Generated at 2022-06-22 12:25:59.141258
# Unit test for function compile_files
def test_compile_files():
    ast.parse('x = 1')
    r = compile_files('tests/fixtures/convert/input',
                      'tests/fixtures/convert/output',
                      CompilationTarget.PY2, 'tests/fixtures/convert')
    assert r.target == CompilationTarget.PY2
    assert r.compiled == 3
    assert r.dependencies == ['six']
    assert r.time > 0.0

# Generated at 2022-06-22 12:26:07.101776
# Unit test for function compile_files
def test_compile_files():
    import shutil
    from pattern_matching import _compile_file
    from .utils.helpers import get_test_module_path

    shutil.rmtree('test', ignore_errors=True)

    _compile_file(InputOutput(get_test_module_path('test.py'),
                              Path('test')),
                  CompilationTarget.PATTERN_MATCHING)

    shutil.rmtree('test', ignore_errors=True)
    assert True

# Generated at 2022-06-22 12:26:18.576226
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import os
    import shutil
    import pytest
    import json

    def _get_file_content(path: str) -> str:
        with open(path) as f:
            return f.read()

    input_ = tempfile.mkdtemp()
    output = tempfile.mkdtemp()
    os.makedirs(os.path.join(input_, 'dir1', 'dir2'))
    os.makedirs(os.path.join(output, 'dir1', 'dir2'))
    with open(os.path.join(input_, 'dir1', 'dir2', 'file1.py'), 'w') as f:
        f.write('print(42)')

# Generated at 2022-06-22 12:26:24.895900
# Unit test for function compile_files
def test_compile_files():
    input_ = 'tests/test_data'
    output = '_test_compile_files'
    target = CompilationTarget.js

    result = compile_files(input_, output, target, root=output)

    assert result.count == 9
    assert result.target == target
    assert result.time > 0
    assert result.dependencies == ['__future__', 'builtins', 'functools']

# Generated at 2022-06-22 12:26:36.382017
# Unit test for function compile_files
def test_compile_files():
    from .tests import tempdir
    with tempdir() as d:
        source = d.join('source')
        source.join('__init__.py').write('')
        source.join('a.py').write('a=1')
        source.join('b.py').write('from .a import a\nb=a')
        source.join('c.py').write('from .a import a\nc=a')
        source.join('d.py').write('from . import a, b, c\nd=a+b+c')
        result = compile_files(str(source), str(d.join('result')),
                               CompilationTarget.ES5)
        assert str(result) == 'Compiled 3 files in 0.0s.\nES5 target'

# Generated at 2022-06-22 12:26:45.832890
# Unit test for function compile_files
def test_compile_files():
    assert compile_files(
        input_="/Users/tung/CSR-Project/src/compiler/input",
        output="/Users/tung/CSR-Project/src/compiler/output",
        target=CompilationTarget.PYTHON,
    ) != None
    assert compile_files(
        input_="/Users/tung/CSR-Project/src/compiler/input",
        output="/Users/tung/CSR-Project/src/compiler/output",
        target=CompilationTarget.PYTHON,
    ).count == 1
test_compile_files()

# Generated at 2022-06-22 12:26:57.155444
# Unit test for function compile_files
def test_compile_files():
    class MyCompilationResult(CompilationResult):
        def __eq__(self, o):
            return self.count == o.count and \
                   self.duration < o.duration + 1 and \
                   self.duration > o.duration - 1 and \
                   self.target == o.target and \
                   self.dependencies == o.dependencies
    import os.path
    test_input = os.path.join(os.path.dirname(__file__), 'test_input')
    test_outpur = os.path.join(os.path.dirname(__file__), 'test_output')
    # assert compile_files(test_input, test_outpur, CompilationTarget.CPYTHON) == \

# Generated at 2022-06-22 12:26:58.560623
# Unit test for function compile_files
def test_compile_files():
    import shutil
    import tempfile
    import os
    import filecmp


# Generated at 2022-06-22 12:27:00.845208
# Unit test for function compile_files
def test_compile_files():
    from .test.test_cannon_common import make_cannon_test, test_compiler
    make_cannon_test(test_compiler, compile_files)

# Generated at 2022-06-22 12:27:03.700744
# Unit test for function compile_files
def test_compile_files():
    result = compile_files(input_='./test/test_files/src', output='./test/test_files/dst', target=CompilationTarget.python2)
    print(result)

# Generated at 2022-06-22 12:27:23.222376
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('./test/test_files/input/basic',
                         './test/test_files/output/basic',
                         CompilationTarget.JAVASCRIPT_EXTENDED) == \
        CompilationResult(16, 0, CompilationTarget.JAVASCRIPT_EXTENDED, ["foo", "bar"])
    assert compile_files('./test/test_files/input/good1',
                         './test/test_files/output/good1',
                         CompilationTarget.JAVASCRIPT_EXTENDED) == \
        CompilationResult(1, 0, CompilationTarget.JAVASCRIPT_EXTENDED, ["foo"])

# Generated at 2022-06-22 12:27:27.814087
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('input', 'output', CompilationTarget.ES5)
    assert result.count == 3
    assert result.compilation_time > 0
    assert result.compilation_target == CompilationTarget.ES5
    assert result.dependencies == ['foo.js', 'bar.js', 'baz.js']



# Generated at 2022-06-22 12:27:32.065532
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    test_dir = '/tmp/test/'
    os.makedirs(test_dir)
    shutil.copy('dynqt/transformers/test/test.py', test_dir)
    compile_files(test_dir, test_dir, CompilationTarget.PYTHON)
    assert len(list(get_input_output_paths(test_dir, test_dir, None))) == 1
    shutil.rmtree(test_dir)


# Generated at 2022-06-22 12:27:42.755984
# Unit test for function compile_files
def test_compile_files():
    input_ = "test/test_files/test_input"
    output = "test/test_files/test_output"
    result = compile_files(input_, output, CompilationTarget.PYTHON_TO_PYTHON)

    assert(result.count == 3)
    assert(result.target == CompilationTarget.PYTHON_TO_PYTHON)
    assert(result.dependencies == ['typed_ast', 'autopep8'])

    def assert_file_equal(in_path: str, out_path: str):
        with open(in_path, 'r') as f1:
            with open(out_path, 'r') as f2:
                assert(f1.read() == f2.read())

# Generated at 2022-06-22 12:27:45.252175
# Unit test for function compile_files
def test_compile_files():
    res = compile_files('examples/test', 'examples/output', CompilationTarget.ES5)
    print(res)

# Generated at 2022-06-22 12:27:56.554548
# Unit test for function compile_files
def test_compile_files():
    # Test on a dummy file
    result = compile_files("./test/input/test_dummy.py", "./test/output", CompilationTarget.ES5)
    assert result.count == 1
    assert result.target == CompilationTarget.ES5
    assert result.dependencies == []

    # Test on a less dummy file
    result = compile_files("./test/input/test_less_dummy.py", "./test/output", CompilationTarget.ES5)
    assert result.count == 1
    assert result.target == CompilationTarget.ES5
    assert result.dependencies == ['document', 'console']

    # Test on a input directory
    result = compile_files("./test/input", "./test/output", CompilationTarget.ES5)
    assert result.count == 4

# Generated at 2022-06-22 12:28:02.454898
# Unit test for function compile_files
def test_compile_files():
    import os.path
    import sys
    def helper(name):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
    input_file = helper('test.py')
    output_file = helper('test_compiled.py')
    result = compile_files(input_file, output_file, CompilationTarget.PYTHON_AS)
    with open(output_file) as f:
        print(f.read())


# Generated at 2022-06-22 12:28:14.230038
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from .exceptions import CompilationError
    from .utils.testutils import assert_equal, assert_true
    from .files import get_directory_hash

    with TemporaryDirectory() as d:
        # The file
        path = (Path(d)/'hello.py').with_suffix('')
        path.touch()
        with path.open('w') as f:
            f.write("print('hello')")

        # Compile
        compile_files(path, path, CompilationTarget.NODE)

        # Check that the transformed file is there
        assert_true(path.with_suffix('.js').exists())

    with TemporaryDirectory() as d:
        # The file
        path = (Path(d)/'hello.py').with_suffix('')
        path.touch

# Generated at 2022-06-22 12:28:24.472907
# Unit test for function compile_files
def test_compile_files():
    code = """
        def test(x):
            return x+1
        """

    trans = """
        function test(x)
            return x + 1
        end
        """

    res = compile_files('test_files/test.jl', 'test_files/test_res.jl', CompilationTarget.BASIC)
    with open('test_files/test_res.jl', 'r') as f:
        result = f.read()

    print(result)
    assert(res.duration > 0)
    assert(res.count == 1)
    assert(res.target == CompilationTarget.BASIC)
    assert(res.dependencies == [])
    assert(result == trans)

# Generated at 2022-06-22 12:28:33.071401
# Unit test for function compile_files
def test_compile_files():
    # Setup
    input_dir = Path('/home/user/python-js/tests/mock_files/')
    output_dir = Path('/home/user/python-js/tests/compiled/')
    if not input_dir.exists():
        raise FileNotFoundError('Input directory does not exist!')
    if not output_dir.exists():
        raise FileNotFoundError('Output directory does not exist!')

    # Actual
    try:
        result = compile_files(input_dir, output_dir, CompilationTarget.JS_ES5)
    except Exception:
        raise

    # Expected result
    assert result.compiled_files == len(input_dir.iterdir())
    assert result.time > 0.0
    assert result.target == CompilationTarget.JS_ES5

# Generated at 2022-06-22 12:28:52.774202
# Unit test for function compile_files
def test_compile_files():
    output = Path('./test_data/output')
    output.mkdir(parents=True, exist_ok=True)
    paths = get_input_output_paths('./test_data/input', output)
    for path in paths:
        compile_files(str(path.input), str(path.output), CompilationTarget.PYTHON)

# Generated at 2022-06-22 12:29:04.724607
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    import unittest

    from .examples import hello_world

    class TestCompileFiles(unittest.TestCase):
        def setUp(self):
            self.output_path_ = tempfile.mkdtemp()

        def tearDown(self):
            import shutil
            shutil.rmtree(self.output_path_)

        def test_compile_hello_world(self):
            self.assertNotIn('Hello World!',
                             hello_world.as_module().__doc__)
            compile_files(hello_world.path, self.output_path_,
                          CompilationTarget.module)

# Generated at 2022-06-22 12:29:12.585660
# Unit test for function compile_files
def test_compile_files():
    import os
    import sys

    sys.path.append('..')
    os.chdir('..')

    with open('test/test.py', 'w') as f:
        f.write('a, b = 1, 2\n')

    try:
        compile_files('test', 'test_build', CompilationTarget(3))
    except:
        pass

    with open('test_build/test.py') as f:
        assert f.read() == 'a, b = 1, 2\n'

    os.remove('test/test.py')
    os.remove('test_build/test.py')
    os.rmdir('test_build')



# Generated at 2022-06-22 12:29:22.415854
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os
    import pytest

    test_root = 'tests/resources/compiler'

    # TODO: Replace tempfile with pathlib.Path.home()
    #       when PyPy 3.5.1 will be released
    #       https://bitbucket.org/pypy/pypy/issues/2664
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_input = os.path.join(tmp_dir, 'input')
        tmp_output = os.path.join(tmp_dir, 'output')
        shutil.copytree(os.path.join(test_root, 'input'), tmp_input)
        result = compile_files(tmp_input, tmp_output,
                               CompilationTarget.JS)
        assert result.count == 3

# Generated at 2022-06-22 12:29:34.129771
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    import subprocess
    import collections
    import shutil

    # Create a temporary directory

# Generated at 2022-06-22 12:29:35.229956
# Unit test for function compile_files
def test_compile_files():
    # FIXME: Add unit test
    pass

# Generated at 2022-06-22 12:29:38.315169
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('../test/test_input',
                         '../test/test_output',
                         CompilationTarget('bundle', '1.0'))

# Generated at 2022-06-22 12:29:47.830275
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    import tempfile
    import subprocess

    temp = tempfile.mkdtemp()

# Generated at 2022-06-22 12:29:53.753154
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/1.py', './', CompilationTarget.STANDALONE)
    compile_files('tests', './', CompilationTarget.STANDALONE)
    compile_files('tests', './', CompilationTarget.BUNDLE)
    compile_files('tests', './', CompilationTarget.BROWSER)

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:29:57.953660
# Unit test for function compile_files
def test_compile_files():
    input_ = "./tests/examples/input"
    output = "./tests/examples/output"
    root = "./tests/examples"
    target = CompilationTarget.STD
    result = compile_files(input_, output, target, root)
    assert result.count == 3