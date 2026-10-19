

# Generated at 2022-06-22 12:24:45.877327
# Unit test for function compile_files
def test_compile_files():
    with pytest.raises(FileNotFoundError) as e:
        compile_files('test_files/test1', 'test/test1', CompilationTarget.PY27)
    assert str(e.value) == 'test_files/test1/test1.py'
    with pytest.raises(FileNotFoundError) as e:
        compile_files('test_files', 'test', CompilationTarget.PY27)
    assert str(e.value) == 'test_files/test1/test1.py'
    with pytest.raises(FileNotFoundError) as e:
        compile_files('test_files', 'test', CompilationTarget.PY27, 'test_files1')
    assert str(e.value) == 'test_files/test1/test1.py'


# Generated at 2022-06-22 12:24:56.635130
# Unit test for function compile_files
def test_compile_files():
    import pathlib

    # Define test input and output directories
    input_ = 'test/test_compile/input'
    output = 'test/test_compile/output'

    # Create output directory if it does not exist
    if not pathlib.Path(output).exists():
        pathlib.Path(output).mkdir()

    # Compile input to output with specified target
    test_result = compile_files(input_, output, CompilationTarget.ES5)

    # Assert the expected test result
    expected_result = CompilationResult(1, 0, CompilationTarget.ES5,
                                        ['test/test_compile/input/test.js'])
    assert test_result == expected_result

    # Manual test: 

    # # Compile to output/test.js
    # compile_files(input_

# Generated at 2022-06-22 12:25:06.310083
# Unit test for function compile_files
def test_compile_files():
    from . import __main__ as main
    from . import test
    from .exceptions import CompilationError

    assert compile_files(test.tests_path / 'test1',
                         test.tests_path / 'test1-compiled', CompilationTarget.PY36) == CompilationResult(2, 0.0, CompilationTarget.PY36, ['sub'])

    assert compile_files(test.tests_path / 'test2',
                         test.tests_path / 'test2-compiled', CompilationTarget.PY36) == CompilationResult(1, 0.0, CompilationTarget.PY36, [])


# Generated at 2022-06-22 12:25:09.994273
# Unit test for function compile_files
def test_compile_files():
    #setup
    input_ = "tests/test_files/input/"
    output = "tests/test_files/output/"
    target = CompilationTarget.NODE
    #call
    compile_files(input_, output, target)
    #assert
    assert True

# Generated at 2022-06-22 12:25:17.944090
# Unit test for function compile_files
def test_compile_files():
    class FakePath(object):
        def __init__(self, parent, name):
            self.parent = parent
            self.name = name
        def open(self, mode=None):
            return self
        def read(self):
            return self.name
        def write(self, data):
            return
        def as_posix(self):
            return self.name
        def mkdir(self, parents=False):
            return

    # Check for all compilation levels
    for target in ['js', 'py']:
        paths = [InputOutput(FakePath(object(), name), FakePath(object(), name)) for name in ['a', 'b']]
        compile_files(object(), object(), target, paths)

# Generated at 2022-06-22 12:25:29.829410
# Unit test for function compile_files
def test_compile_files():
    import shutil
    import os
    import tempfile
    import pathlib

    input_ = tempfile.mkdtemp()
    output = tempfile.mkdtemp()

    with open(os.path.join(input_, "test.cpp"), "w") as f:
        f.write("""\
#include <iostream>

void main() {
    std::cout << "Hello World!";
}
""")

    compile_files(input_, output, CompilationTarget.CSharp,
                  pathlib.Path())

    # Check that the file exists
    assert os.path.exists(os.path.join(output, "Program.cs"))

    # Check that the temp dirs are empty
    shutil.rmtree(input_)
    shutil.rmtree(output)

# Generated at 2022-06-22 12:25:40.897952
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationTarget, CompilationResult
    from .exceptions import CompilationError
    from tempfile import mkdtemp
    from pathlib import Path
    from .utils.helpers import cleanup
    from .utils.mock import mock_package, mock_paths

    def test(input_: str, output: str, target: CompilationTarget,
             root: Optional[str] = None,
             expected_dependencies: Optional[List[str]] = None,
             expected_error: Optional[str] = None):
        if expected_error:
            with pytest.raises(CompilationError) as excinfo:
                compile_files(input_, output, target, root)
                assert expected_error in str(excinfo.value)
        else:
            result = compile_files(input_, output, target, root)

# Generated at 2022-06-22 12:25:44.025474
# Unit test for function compile_files
def test_compile_files():
    compile_result = compile_files('../test_input/', '../test_output/', 'js')
    assert compile_result.count == 8
    assert compile_result.target == 'js'
    assert compile_result.time > 0

# Generated at 2022-06-22 12:25:46.631495
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('test/test_data', 'test/test_compile_files_out',
                         CompilationTarget.JSX)

# Generated at 2022-06-22 12:25:53.920495
# Unit test for function compile_files
def test_compile_files():
    class TestResult(CompilationResult):
        def __eq__(self, other):
            return (self.count == other.count and
                    self.time == other.time and
                    self.target == other.target and
                    self.dependencies == other.dependencies)

    assert compile_files('tests/files/input', 'test_output',
                         CompilationTarget.ES5) == TestResult(4, 0.0,
                         CompilationTarget.ES5, [])

# Generated at 2022-06-22 12:26:08.797929
# Unit test for function compile_files
def test_compile_files():
    from .utils.helpers import get_fixture_path
    from .utils.test_data import assert_compilation_result

    with get_fixture_path('test_compile').open() as f:
        result = compile_files(f.read(), 'target', CompilationTarget.BROWSER)
        assert_compilation_result(
            result, 4, CompilationTarget.BROWSER, ['alert.js', 'prompt.js', 'confirm.js'])


if __name__ == '__main__':
    import sys
    compile_files(sys.argv[1], sys.argv[2], CompilationTarget.BROWSER)

# Generated at 2022-06-22 12:26:19.655442
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import os
    import sys
    from subprocess import run
    from pathlib import Path
    
    # compile_files(input_, output, target, root = None)
    # imports a file in input_, and assigns it to main.py, compiles it to main.pyc,
    # and assigns output to main.pyc. Runs the program and tests if main.pyc works
    # with just the imports.

    # a simple file to test
    text = '''
import os
import sys
import tempfile

run_test = True

if run_test:
    run(["python3", "main.pyc"])
'''
    # create necessary files to perform the test
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)

    # write file

# Generated at 2022-06-22 12:26:24.096650
# Unit test for function compile_files
def test_compile_files():
    assert compile_files("tests\input",
                         "tests\output",
                         CompilationTarget.PYTHON)
    assert compile_files("tests\input",
                         "tests\output",
                         CompilationTarget.PYTHON,
                         "tests")


# Generated at 2022-06-22 12:26:27.715521
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/resources/',
                           'output',
                           CompilationTarget.PYTHON3)
    print(result)


if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:26:37.454113
# Unit test for function compile_files
def test_compile_files():
    def _assert(result: CompilationResult) -> None:
        assert result.target == CompilationTarget.JAVASCRIPT
        assert result.count == 2
        assert result.time > 0
        assert result.dependencies == ['assertions', 'sys']

    _assert(compile_files('src/python-runtime', 'build/python-runtime',
                          CompilationTarget.JAVASCRIPT))
    _assert(compile_files('src/python-runtime', 'build/python-runtime',
                          CompilationTarget.JAVASCRIPT, 'src'))

# Generated at 2022-06-22 12:26:49.214443
# Unit test for function compile_files
def test_compile_files():
    from .files import InputOutput
    from .types import CompilationTarget
    from .exceptions import CompilationError
    from .utils.helpers import debug
    debug(lambda: 'Start testing function compile_files')
    # test compilation to minimal target
    paths_list = [InputOutput('/foo/bar.py', '/foo/bar.py'),
                  InputOutput('/foo/baz.py', '/foo/baz.py')]
    result = compile_files("/foo", "/foo", CompilationTarget.MINIMAL, "/")
    assert (result.successful is True)
    assert (result.count == 2)
    # test compilation to maximal target

# Generated at 2022-06-22 12:26:59.704254
# Unit test for function compile_files
def test_compile_files():
    import os
    import pkgutil
    import tempfile

    from .exceptions import CompilationError
    from .types import CompilationResult

    def compare_results(expected: CompilationResult, actual: CompilationResult):
        assert expected.count == actual.count
        assert expected.runtime > 0
        assert expected.runtime - 0.0003 < actual.runtime < expected.runtime + 0.0003
        assert expected.target == actual.target
        assert expected.dependencies == actual.dependencies

    test_data = pkgutil.get_data('no4lj', 'test_data/compile_files/*').decode('utf-8').split('===')

# Generated at 2022-06-22 12:27:02.549018
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/test_input', 'tests/test_output', CompilationTarget.PYTHON36)
    pass

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:27:13.377030
# Unit test for function compile_files
def test_compile_files():
    import unittest
    import shutil
    import os
    import glob
    import json
    import os.path as osp
    import pathlib

    class CompileFilesTest(unittest.TestCase):

        def setUp(self):
            self.tmpdir = pathlib.Path(osp.abspath(osp.join(osp.split(__file__)[0], '..', 'tmp')))
            if self.tmpdir.exists():
                shutil.rmtree(str(self.tmpdir))
            shutil.copytree(str(osp.abspath(osp.join(osp.split(__file__)[0], '..', 'tests', 'tmp'))), str(self.tmpdir))

            os.chdir(str(self.tmpdir / 'input'))


# Generated at 2022-06-22 12:27:24.812410
# Unit test for function compile_files
def test_compile_files():
    from .files import get_path, compile_files
    from .types import CompilationTarget
    result = compile_files(get_path('tests/01_simple/01_simple'),
                           get_path('tests/01_simple/result'),
                           CompilationTarget.CPYTHON)
    assert result.count == 1
    assert result.target == CompilationTarget.CPYTHON
    assert result.time > 0
    assert result.dependencies == []

    result = compile_files(get_path('tests/01_simple/01_simple'),
                           get_path('tests/01_simple/result'),
                           CompilationTarget.RUBY)
    assert result.count == 1
    assert result.target == CompilationTarget.RUBY
    assert result.time > 0
    assert result.dependencies == []

   

# Generated at 2022-06-22 12:27:38.406846
# Unit test for function compile_files
def test_compile_files():
    for func in [compile_files]:
        func(
            input_='./tests/compile/input',
            output='./tests/compile/output',
            target=CompilationTarget.PYTHON_35
        )

# Generated at 2022-06-22 12:27:42.029891
# Unit test for function compile_files
def test_compile_files():
    global_dependencies = set(['time'])

    compile_files(input_='test/fixtures/input',
                  output='test/target',
                  target=CompilationTarget.jvm_bytecode,
                  root='test')



# Generated at 2022-06-22 12:27:53.544488
# Unit test for function compile_files
def test_compile_files():
    import pytest
    import os

    outdir = os.path.join(os.path.dirname(__file__), 'out')
    indir = os.path.join(os.path.dirname(__file__), 'in')

    for f in os.listdir(outdir):
        os.remove(os.path.join(outdir, f))
    assert compile_files(indir, outdir, CompilationTarget.JS) == \
            CompilationResult(2, 0, CompilationTarget.JS, [])

    #Test exception handling
    with pytest.raises(CompilationError):
      compile_files(indir, outdir, CompilationTarget.REST)

# Generated at 2022-06-22 12:28:03.052109
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    def _exec(code: str, target: CompilationTarget) -> List[str]:
        from io import StringIO
        import sys
        from .transformers.call import CallTransformer
        from .transformers.class_ import ClassTransformer
        from .transformers.import_ import ImportTransformer
        from .transformers.number import NumberTransformer
        from .transformers.op import OperatorTransformer
        from .transformers.property import PropertyTransformer
        from .transformers.tuple_ import TupleTransformer
        from .transformers.with_ import WithTransformer
        from .transformers.yield_ import YieldTransformer

# Generated at 2022-06-22 12:28:07.019470
# Unit test for function compile_files
def test_compile_files():
    result = compile_files("tests/examples/test1",
                           "tests/output",
                           CompilationTarget.PYTHON36,
                           "tests")
    print("---- Result: ", result)

test_compile_files()

# Generated at 2022-06-22 12:28:07.669427
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:28:19.839209
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os

    DIR = os.path.dirname(__file__)
    INPUT = os.path.join(DIR, 'testdata')
    OUTPUT = tempfile.mkdtemp()

    result = compile_files(INPUT, OUTPUT, CompilationTarget.PYTHON)
    if result.error:
        print(result.error)
        assert False

    for root, _, files in os.walk(OUTPUT):
        for name in files:
            out_file = os.path.join(root, name)
            in_file = out_file.replace(OUTPUT, INPUT).replace('.py', '.in.py')
            with open(in_file) as f:
                code = f.read()

# Generated at 2022-06-22 12:28:28.704970
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .expectations import Expectation
    from .expectations import expect_compilation_result
    from .utils.helpers import create_dirs, remove_dirs

    def _compile_files(expectation: Expectation, target: CompilationTarget,
                       root: Optional[str] = None) -> None:
        output = str(Path(expectation.input_).joinpath('output').resolve())
        remove_dirs(output)
        create_dirs(expectation.input_)
        result = compile_files(expectation.input_, output, target, root)
        expect_compilation_result(result, expectation, output, target)
        remove_dirs(output)


# Generated at 2022-06-22 12:28:40.551069
# Unit test for function compile_files
def test_compile_files():
    import io
    import os
    import sys
    import tempfile

    if sys.version_info < (3, 6):
        return None  # pragma: no cover

    input_test = tempfile.TemporaryDirectory()
    output_test = tempfile.TemporaryDirectory()
    input_ = input_test.name
    output = output_test.name

    # Create test files
    (Path(input_) / 'foo.py').write_text('print("Hello, world")')
    (Path(input_) / 'bar.py').write_text('print("Bye, world")')

    # Compile files
    result = compile_files(input_, output, CompilationTarget.STANDARD_LIBRARY)

    # Check
    assert result.compiled == 2
    assert result.target == CompilationTarget.ST

# Generated at 2022-06-22 12:28:52.118484
# Unit test for function compile_files
def test_compile_files():
    from .tests.test_helpers import assert_result
    result = compile_files('tests/resources/empty', 'out',
                           CompilationTarget.BINARY)
    assert_result(result, CompilationTarget.BINARY, 0,
                  0, ['out'])

    result = compile_files('tests/resources/simple', 'out',
                           CompilationTarget.BINARY)
    assert_result(result, CompilationTarget.BINARY, 4,
                  0, ['out/a.js', 'out/b.js', 'out/x.js', 'out'])

    result = compile_files('tests/resources/simple',
                           'out', CompilationTarget.LIBRARY)

# Generated at 2022-06-22 12:29:17.210995
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/input',
                         'tests/output',
                         'native') == CompilationResult(0, 0, 'native', [])

# Generated at 2022-06-22 12:29:22.657503
# Unit test for function compile_files
def test_compile_files():
    with open('/tmp/test.py', 'w') as f:
        f.write('def foo(x, y):\n    return x+y')

    compile_files('/tmp/test.py', '/tmp/output.js',
                  CompilationTarget.pymath, '/tmp')

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:29:29.916619
# Unit test for function compile_files
def test_compile_files():
    import os
    input_ = os.path.expanduser('~/.config/smart-pylint/tests/input/')
    output = os.path.expanduser('~/.config/smart-pylint/tests/test/')
    compile_files(input_, output, CompilationTarget.BASH)
    compile_files(input_, output, CompilationTarget.PYTHON2)
    compile_files(input_, output, CompilationTarget.PYTHON3)

# Generated at 2022-06-22 12:29:37.468442
# Unit test for function compile_files
def test_compile_files():
    input_ = 'test/examples/prog'
    output = 'temp/prog'
    result = compile_files(input_, output, CompilationTarget.JS_BARE_FUNCTIONS)
    assert result.time_taken > 0
    assert result.target == CompilationTarget.JS_BARE_FUNCTIONS
    assert result.dependencies == ['numpy']

# Run unit tests, if run on its own
if __name__ == "__main__":
    test_compile_files()

# Generated at 2022-06-22 12:29:41.933369
# Unit test for function compile_files
def test_compile_files():
    compile_files('examples/module.py', 'output', 'module')
    compile_files('examples/module.py', 'output', 'script')

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:29:52.952739
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationResult
    from .files import get_input_output_paths
    from .exceptions import CompilationError, TransformationError
    import pytest
    from pathlib import Path
    from tempfile import TemporaryDirectory

    def get_compiled_names(compiler):
        """Returns a list of the path of the files in the output directory."""
        return list(map(lambda p: p.name,
                        compiler.result.output.glob('**/*.js')))

    def get_content(compiler, filename):
        """Returns the content of the given file in the output directory."""
        return compiler.result.output.joinpath(filename).open().read()

    def test_compilation(compiler):
        """Checks that the compilation succeed."""

# Generated at 2022-06-22 12:30:04.887352
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files"""
    paths = get_input_output_paths('test_data/test_compile/input',
                                   'test_data/test_compile/output')
    assert CompilationResult(2, _, CompilationTarget.EMPTY) == compile_files(
        'test_data/test_compile/input',
        'test_data/test_compile/output',
        CompilationTarget.EMPTY
    )
    for paths_ in paths:
        with paths_.input.open() as input_file:
            with paths_.output.open() as output_file:
                assert input_file.read() == output_file.read()

# Generated at 2022-06-22 12:30:15.216820
# Unit test for function compile_files
def test_compile_files():
    import shutil
    import pytest
    import tempfile
    import subprocess
    import os

    old_cwd = os.path.abspath(os.curdir)
    with tempfile.TemporaryDirectory() as d:
        os.chdir(d)
        shutil.copytree('tests/integration/nonstandard_flow', 'src')
        shutil.copytree('tests/integration/nonstandard_flow', 'lib')
        subprocess.check_call(['pipenv', 'install'])
        subprocess.check_call(['pipenv', 'run', 'pip', 'install', '--requirement', 'lib/requirements.txt'])

# Generated at 2022-06-22 12:30:26.177710
# Unit test for function compile_files
def test_compile_files():
    compile_files("/Users/karanpat/PycharmProjects/unpythonic_python/unpythonic/src",
                 "/Users/karanpat/PycharmProjects/unpythonic_python/unpythonic/dist",
                 target=CompilationTarget.PYTHON)
    compile_files("/Users/karanpat/PycharmProjects/unpythonic_python/examples/fibonacci",
                  "/Users/karanpat/PycharmProjects/unpythonic_python/examples/fibonacci/dist",
                  target=CompilationTarget.UNPYTHONIC)

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:30:27.839808
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('test', 'output', CompilationTarget.PYTHON)

# Generated at 2022-06-22 12:31:27.133908
# Unit test for function compile_files
def test_compile_files():
    from .utils.tempdir import TempDir
    from .transformers import transformers
    from .types import CompilationTarget
    from .exceptions import CompilationError

    # create temp directory
    with TempDir() as temp_dir:
        input_ = temp_dir / 'input'
        input_.mkdir()
        (input_ / 'file1.py').write_text('''
''')
        (input_ / 'file2.py').write_text('''
print
''')
        (input_ / 'file3.py').write_text('''
a = 'abc
''')
        (input_ / 'dir1/file4.py').write_text('''
''')
        output = temp_dir / 'output'


# Generated at 2022-06-22 12:31:31.149165
# Unit test for function compile_files
def test_compile_files():
    compile_files('./test/fixtures/unit_test_compile_files', './test/output/unit_test_compile_files', CompilationTarget.PYTHON_TO_PYTHON)

# Generated at 2022-06-22 12:31:35.555696
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('.', '.', CompilationTarget.PYTHON)
    assert result.count == 0
    assert result.target == CompilationTarget.PYTHON



# Generated at 2022-06-22 12:31:44.559834
# Unit test for function compile_files
def test_compile_files():
    import os
    import pytest
    from pathlib import Path
    from shutil import rmtree
    from tempfile import mkdtemp
    from unittest.mock import patch, Mock

    def test_compile_files_sets_dependencies():
        mock = Mock()
        mock.return_value = CompilationResult(1, 1, CompilationTarget.EVAL_BUILTINS,
                                              ['__import__'])
        with patch('shiv.compiler.compile_files') as mock:
            compile_files('a', 'b', CompilationTarget.EVAL_BUILTINS)
            mock.assert_called_once_with('a', 'b', CompilationTarget.EVAL_BUILTINS, root = None)

    # CompilationResult object returned by compile_files function has attributes:
    #

# Generated at 2022-06-22 12:31:52.911417
# Unit test for function compile_files
def test_compile_files():
    tmpdir = Path(tempfile.mkdtemp())
    input_ = tmpdir / 'input'
    output = tmpdir / 'output'
    Path(input_ / '__init__.py').touch()
    Path(input_ / '__future__.py').touch()

# Generated at 2022-06-22 12:32:02.416002
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from .exceptions import CompilationError
    from .utils.helpers import write_file
    with TemporaryDirectory() as d:
        path = Path(d)
        input_ = path / 'input.py'
        output = path / 'output'
        write_file(input_, 'print(1)')
        result = compile_files(input_, output, CompilationTarget.PYTHON27)
        assert result.count == 1
        assert result.target == CompilationTarget.PYTHON27
        assert not result.dependencies
        assert write_file(input_, '1/0')
        try:
            compile_files(input_, output, CompilationTarget.PYTHON27)
        except CompilationError as e:
            assert e.path

# Generated at 2022-06-22 12:32:08.362836
# Unit test for function compile_files
def test_compile_files():
    input_ = './tests'
    output = './output'
    target = CompilationTarget.PYTHON3
    root = './tests'
    path1 = input_ + '/test1.py'
    path2 = input_ + '/test2.py'
    path1_output = output + '/test1.py'
    path2_output = output + '/test2.py'
    result = compile_files(input_, output, target, root)
    assert(result.get_path_count() == 2)
    assert(path1 in result.get_dependencies())
    assert(path2 in result.get_dependencies())
    assert(path1_output in result.get_dependencies())
    assert(path2_output in result.get_dependencies())

# Generated at 2022-06-22 12:32:13.765265
# Unit test for function compile_files
def test_compile_files():
    from .fake_data import SAMPLE_DATA
    from .config import DEFAULT_CONFIG
    import tempfile
    import shutil
    import os

    input_ = SAMPLE_DATA.input_path('TEST')
    output = tempfile.mkdtemp()


# Generated at 2022-06-22 12:32:26.044728
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/', 'var/compiled/',
                           CompilationTarget.PYTHON_IF_ELSE_STATEMENT)
    assert result.count == 36
    assert result.execution_time < 1
    assert result.target == CompilationTarget.PYTHON_IF_ELSE_STATEMENT

# Generated at 2022-06-22 12:32:32.602543
# Unit test for function compile_files
def test_compile_files():
    import os.path
    from .types import CompilationTarget
    from .utils.helpers import debug
    from .utils.resources import copy_resources_to, remove_resources_from
    from .utils.asserts import assert_compilation_result_match

    input_ = './input_'
    output = './output'
    target = CompilationTarget.PRODUCTION

    copy_resources_to('compilation/simple', input_)
    result = compile_files(input_, output, target)
    remove_resources_from('./output')
    remove_resources_from('./input_')
