

# Generated at 2022-06-22 12:24:45.685273
# Unit test for function compile_files
def test_compile_files():
    import compileall
    from shutil import rmtree
    from tempfile import mkdtemp
    from .stubs import stubs_directory
    from .utils.test import get_test_paths

    target = CompilationTarget.from_string("python35")

    for paths in get_test_paths(stubs_directory / 'input'):
        input_ = mkdtemp(prefix='input-')
        output = mkdtemp(prefix='output-')

        paths.input.copy(input_)
        try:
            compile_files(input_, output, target)
            assert compileall.compile_dir(output) == 0
        finally:
            rmtree(input_)
            rmtree(output)

# Generated at 2022-06-22 12:24:56.871683
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from os.path import join
    from .utils.testing import patch_sys_path
    from .types import CompilationTarget
    from .exceptions import CompilationError

    with patch_sys_path('tests/test_compile_files/simple'):
        compile_files('source', 'build', CompilationTarget.PYTHON_27)

    with patch_sys_path('tests/test_compile_files/simple/source'):
        with Path('build/my_module.py').open() as f:
            assert f.read() == 'if True:\n    pass\n\n'

    with patch_sys_path('tests/test_compile_files/simple'):
        compile_files('source', 'build', CompilationTarget.PYTHON_27)


# Generated at 2022-06-22 12:25:08.058367
# Unit test for function compile_files
def test_compile_files():
    """Tests for function compile_files"""
    import os
    import shutil
    import tempfile
    import unittest
    from pathlib import Path

    class TestCompileFiles(unittest.TestCase):
        """Tests for function compile_files"""
        def setUp(self) -> None:
            """Creates test files and dirs."""
            self.temp_dir = Path(tempfile.mkdtemp())
            self.basic_code = """
# A comment
# and this is a comment line
# And This is yet another comment
1 + 1"""
            self.basic_code_expected = """1 + 1 # foo"""
            self.temp_dir.joinpath('foo.py').write_text(self.basic_code)

# Generated at 2022-06-22 12:25:17.432492
# Unit test for function compile_files
def test_compile_files():
    from .exceptions import CompilationError
    from .files import write_input_file

    write_input_file('test/test_input', '')
    result = compile_files('test/test_input', 'test/test_output', CompilationTarget.GENERATOR)
    assert result.count == 1
    assert result.target == CompilationTarget.GENERATOR
    assert result.dependencies == []

    write_input_file('test/test_input', 'def foo(x):\n  return x**2')
    result = compile_files('test/test_input', 'test/test_output', CompilationTarget.GENERATOR)
    assert result.count == 1
    assert result.target == CompilationTarget.GENERATOR
    assert result.dependencies == ['map', 'pow']

# Generated at 2022-06-22 12:25:20.778002
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('./test/examples/valid_src'
                         , './test/examples/ok_dst'
                         , CompilationTarget.PYTHON3)


# Generated at 2022-06-22 12:25:33.116208
# Unit test for function compile_files
def test_compile_files():
    from .utils.helpers import root_dir
    from os import makedirs
    from os.path import join
    from shutil import rmtree

    input_ = join(root_dir, 'tests', 'sample', '.tmp', 'input')
    output = join(root_dir, 'tests', 'sample', '.tmp', 'output')
    root = join(root_dir, 'tests', 'sample', 'sample')

    makedirs(input_, exist_ok=True)
    makedirs(output, exist_ok=True)

    with open(join(input_, 'sample.py'), 'w') as f:
        f.write('def foo():\n    print(1)')


# Generated at 2022-06-22 12:25:33.798708
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:25:42.764900
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import pathlib
    import shutil
    from .test.test_cases import TEST_CASES

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-22 12:25:54.230010
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import os.path

    input_ = Path('input')
    output = Path('output')
    target = CompilationTarget.CSV
    root = os.path.normpath('/root/path')

    def compile_files_faked(input_: Path, output: Path, target: CompilationTarget,
                  root: Optional[str] = None) -> CompilationResult:
        return CompilationResult(0, 0, target, [])

    def get_input_output_paths_faked(input_: Path, output: Path,
                                     root: Optional[str] = None):
        for paths in [[Path('input'), Path('output')]]:
            yield paths


# Generated at 2022-06-22 12:26:01.463018
# Unit test for function compile_files
def test_compile_files():
    from os.path import join
    from .utils.resources import get_resources
    from simplejson import dump

    target = CompilationTarget.RUNTIME
    input_ = get_resources('test_compiler')
    output = get_resources('test_compiler_runtime_output')
    result = compile_files(input_, output, target)

    with Path(get_resources('test_compiler_runtime_result.json')).open() as f:
        expected = load(f)

    expected['time'] = result.time
    expected['count'] = result.count

    assert result == CompilationResult(**expected)

    with Path(join(output, 'a.js')).open() as f:
        assert f.read() == 'var z = 123;\n'


# Generated at 2022-06-22 12:26:13.349231
# Unit test for function compile_files
def test_compile_files():
    output = '/tmp/compile'
    result = compile_files('tests/success', output, CompilationTarget.ES6)
    assert result.success == True
    assert result.count >= 1
    assert result.target == CompilationTarget.ES6
    assert len(result.dependencies) >= 0
    assert len(result.dependencies) <= 1

# Generated at 2022-06-22 12:26:22.865491
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from typing import Dict, Union
    from ..exceptions import CompilationError
    from .files import get_input_output_paths
    from .transform import CompilationResult

    def mock_compile_file(paths: InputOutput,
                          target: CompilationTarget) -> List[str]:
        # type: (InputOutput, CompilationTarget) -> List[str]
        "\n        Mocks single compilation steps.\n\n        :param paths: \n            Input and output paths.\n        :param target: \n            Target of compilation.\n        :return: \n            List of dependencies.\n        "
        input_ = paths.input.as_posix()
        output = paths.output.as_posix()

# Generated at 2022-06-22 12:26:33.192776
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil

    # Change this to 'true' if you want to enable tests
    if os.environ.get('COMPILER_TESTS') != 'true':
        return

    def run_test(in_, out, target):
        print('========== Running test ==========')
        print('in:', in_)
        print('out:', out)
        print('target:', target)
        print()

        # Actually run
        result = compile_files(in_, out, target, 'compiler/test')
        print('Compiled {} files in {:.3f} seconds'.format(result.count,
                                                           result.duration))
        print('Dependencies: ', result.dependencies)

        # Show the files

# Generated at 2022-06-22 12:26:42.793897
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files."""
    import os

    def _compile_test_file(input_name: str, output_name: str,
                           expected_output_name: str):
        """Compiles a single test file."""
        output_name = os.path.join(TEST_DIRECTORY, 'compiled', output_name)
        expected_output_name = os.path.join(TEST_DIRECTORY, 'compiled',
                                            expected_output_name)

        try:
            compile_files(
                os.path.join(TEST_DIRECTORY, 'src', input_name),
                output_name,
                CompilationTarget.GENERIC)
        except:
            with open(output_name, 'r') as f:
                result = f.read()
           

# Generated at 2022-06-22 12:26:48.712986
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .files import get_input_output_paths

    import_file = Path('import_file.py')
    output_file = Path('output_file.py')
    import_file.write_text('import x')
    compile_files(str(import_file), str(output_file), CompilationTarget.Python)
    assert output_file.exists()

# Generated at 2022-06-22 12:26:59.305447
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import unittest
    import subprocess
    import os.path

    class PythonCompilerTest(unittest.TestCase):
        def test_simple(self):
            with tempfile.TemporaryDirectory() as tempdir:
                input_ = os.path.join(tempdir, 'input')
                output = os.path.join(tempdir, 'output')

                for d in (input_, output):
                    os.mkdir(d)

                for i in range(1, 4):
                    with open(os.path.join(
                            input_, 'compiler_test{}.py'.format(i)), 'w') as f:
                        f.write('def f{}():\n  return {}\n'.format(i, i))


# Generated at 2022-06-22 12:27:03.577989
# Unit test for function compile_files
def test_compile_files():
    res = compile_files('tests/input', 'tests/output', CompilationTarget.ES5)
    assert res.target == CompilationTarget.ES5
    assert res.count == 6
    assert res.duration > 1
    assert 'jsonschema' in res.dependencies
    assert 'dataclasses' in res.dependencies

# Generated at 2022-06-22 12:27:09.588587
# Unit test for function compile_files
def test_compile_files():
    target = CompilationTarget.LATEST
    result = compile_files('tests/sample_program/src',
                           'tests/sample_program/out',
                           target)

    assert result.count == 3
    assert result.target == target
    assert result.dependencies == [
        'src/alsodummy.nj',
        'src/dummy.nj',
        'src/python/dummy.py',
    ]

# Generated at 2022-06-22 12:27:11.805043
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/data', 'target', CompilationTarget.WEB) == CompilationResult(
        2, 0.06, CompilationTarget.WEB, [])

# Generated at 2022-06-22 12:27:17.872022
# Unit test for function compile_files
def test_compile_files():
    import os, sys
    import pathlib
    import io
    import contextlib
    import nose
    @contextlib.contextmanager
    def capture_stdout() -> None:
        """Captures stdout."""
        oldout, olderr = sys.stdout, sys.stderr
        try:
            out = [io.StringIO(), io.StringIO()]
            sys.stdout, sys.stderr = out
            yield out
        finally:
            sys.stdout, sys.stderr = oldout, olderr
            out[0] = out[0].getvalue()
            out[1] = out[1].getvalue()

    def test_output(path: pathlib.Path, files: List[str]):
        """Checks if output was generated and does not contain errors."""
        error_ms

# Generated at 2022-06-22 12:27:40.115133
# Unit test for function compile_files
def test_compile_files():
    def check(code, target, expected, error=None):
        if error is None:
            error = []
        try:
            result = compile_files('./', './', target, './')
            assert len(result.dependencies) == len(expected)
            for dep in expected:
                assert dep in result.dependencies
        except e:
            assert type(e) == error
        assert result.files == 0

    check('', CompilationTarget.NONE, [])
    check('def f(): pass', CompilationTarget.NONE, [])
    check('def f(): pass', CompilationTarget.NODE, [])
    check('def f(): pass', CompilationTarget.BROWSER, [])

    code = '''
    def f():
        return break
    '''

# Generated at 2022-06-22 12:27:43.677722
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('input/functions.py', 'build/functions.py',
                         CompilationTarget.PYTHON) == CompilationResult(1, 0,
                                                                       CompilationTarget.PYTHON)

# Generated at 2022-06-22 12:27:51.786025
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('/home/ubuntu/autocode/tests/compiler', '../compiled', CompilationTarget.JAVA)
    assert result.count == 2
    assert result.target == CompilationTarget.JAVA
    with open('../compiled/compiler/test.py') as f:
        assert f.read() == 'from com.google.common.collect import ImmutableList\n\n' \
                           'from typing import List\n\n\n' \
                           'def main(args: List[str]) -> None:\n    ' \
                           'ImmutableList.of(args)\n'

# Generated at 2022-06-22 12:27:56.221140
# Unit test for function compile_files
def test_compile_files():
    # Create input and output directories
    input_ = mkdtemp()
    output = Path(mkdtemp())
    # Copy test file to input directory
    path = Path(__file__).parent / 'test_data'
    file_path = path / 'test.py'
    shutil.copy2(file_path, input_)
    # Compile file
    result = compile_files(input_, output, CompilationTarget.RELEASE)
    # Delete input and output directories
    shutil.rmtree(input_)
    shutil.rmtree(output)
    # Run test function
    test(result)

# Unit test function

# Generated at 2022-06-22 12:27:59.985389
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('./tests/input', './tests/output', CompilationTarget.JS) == CompilationResult(
        count=3, time=0.0002529621124267578, target=CompilationTarget.JS, dependencies=['babel-polyfill', 'babel-runtime'])

# Generated at 2022-06-22 12:28:04.970524
# Unit test for function compile_files
def test_compile_files():
    input_ = 'test/test_files/test_compile_files'
    output = 'test/output'
    result = compile_files(input_, output, CompilationTarget.PY36)
    assert result.compiled_files == 2
    assert result.dependencies == ['a', 'b']



# Generated at 2022-06-22 12:28:16.844967
# Unit test for function compile_files
def test_compile_files():
    import shutil
    import os
    test_dir = os.path.join('temp', 'test')
    try:
        shutil.rmtree(test_dir)
    except:
        pass
    shutil.copytree(os.path.join('tests', 'input'), test_dir)

    result = compile_files(os.path.join(test_dir, 'input', 'python'),
                           os.path.join(test_dir, 'input', 'javascript'),
                           CompilationTarget.ES6)

    assert result.count == 8, 'Files count {} != 8'.format(result.count)
    assert len(result.dependencies) == 4, 'Dependencies count {} != 4'.format(result.count)
    assert result.target == CompilationTarget.ES6, 'Expected target ES6'

# Generated at 2022-06-22 12:28:22.014394
# Unit test for function compile_files
def test_compile_files():
    input_ = 'tests/data/input'
    output = 'tests/data/output'
    target = CompilationTarget.TARGET_PYTHON_3
    result = compile_files(input_, output, target)
    assert result.paths == 2
    assert len(result.dependencies) == 2
    assert result.target == target

# Generated at 2022-06-22 12:28:30.110943
# Unit test for function compile_files
def test_compile_files():
    input_ = './test/test-project'
    output = './test/test-output'
    root = './test/test-project'
    target = CompilationTarget(1)
    result = compile_files(input_, output, target, root)
    assert result.count == 4
    assert result.target == target
    assert result.elapsed > 0
    assert result.dependencies == ['core.pyi']


if __name__ == '__main__':
    """Main entry point for command line interface.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Compiles Python to PPCI.")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='turn on verbose mode')

# Generated at 2022-06-22 12:28:41.640522
# Unit test for function compile_files
def test_compile_files():
    from .examples.particles import particle_001 as particle
    from pathlib import Path
    import tempfile

    input = tempfile.TemporaryDirectory()
    output = tempfile.TemporaryDirectory()
    root = Path(input.name) / 'sketch'

    # Create input structure
    (root / 'sketch.py').write_text(particle)
    (root / 'subfolder' / 'helper.py').touch()

    # Compile
    compile_files(input.name, output.name, CompilationTarget.ESP8266)

    # Check output
    output = Path(output.name)
    assert (output / 'sketch' / 'sketch.ino').is_file()
    assert (output / 'sketch/subfolder' / 'helper.js').is_file()



# Generated at 2022-06-22 12:29:15.597062
# Unit test for function compile_files
def test_compile_files():
    assert compile_files("./tests/files/unit/compiler", "./tests/files/unit/compiler", "python-ast") == CompilationResult(
        3, 0.0, "python-ast", [
            "https://raw.githubusercontent.com/python/cpython/master/Lib/test/test_asyncio/test_async.py",
            "./tests/files/unit/compiler/test_1.py",
            "./tests/files/unit/compiler/test_2.py",
            "./tests/files/unit/compiler/test_3.py"
        ])

# Generated at 2022-06-22 12:29:23.999331
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from py.path import local
    from .types import CompilationTarget
    from .files import InputOutput
    from .transformers.fixers import FixerVisitor
    from .exceptions import CompilationError, TransformationError

    # Test compilation of file with syntax error
    with pytest.raises(CompilationError):
        compile_files('tests/compiler/fixtures/hello.py',
                      'tests/compiler/fixtures/compiled/hello.py',
                      CompilationTarget.PY2)

    # Test compilation of file with runtime error
    with pytest.raises(CompilationError):
        compile_files('tests/compiler/fixtures/runtime_error.py',
                      'tests/compiler/fixtures/runtime_error_compiled.py',
                      CompilationTarget.PY2)



# Generated at 2022-06-22 12:29:27.881680
# Unit test for function compile_files
def test_compile_files():
    
    result = compile_files('../tests/input', '../tests/output', CompilationTarget.STANDARD)
    assert result.count == 1
    assert result.dependencies == ['coverage']

test_compile_files()



# Generated at 2022-06-22 12:29:31.278909
# Unit test for function compile_files
def test_compile_files():
    from .utils.test_runner import run_test
    from .testsuite.test_compile_files import testcases
    run_test(compile_files, testcases, CompilationResult)


# Generated at 2022-06-22 12:29:34.412828
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .mock import MockCompilationTarget
    from .utils.helpers import create_file
    import shutil
    import tempfile


# Generated at 2022-06-22 12:29:39.572196
# Unit test for function compile_files
def test_compile_files():
    # It should compile all files from input_ folder to output folder
    assert compile_files("input_", "output", target=CompilationTarget.BUILD) != None

test_compile_files()

# Generated at 2022-06-22 12:29:48.554967
# Unit test for function compile_files
def test_compile_files():
    from tempfile import mkdtemp
    from pathlib import Path
    from .utils.helpers import touch
    from . import __version__ as version

    with mkdtemp() as tmp:
        input_ = Path(tmp)
        output = Path(tmp) / 'output'
        output.mkdir()

# Generated at 2022-06-22 12:29:50.121410
# Unit test for function compile_files
def test_compile_files():
    compile_files('input', 'output', CompilationTarget.JS)


# Generated at 2022-06-22 12:29:53.339248
# Unit test for function compile_files
def test_compile_files():
    input_ = 'tests/input'
    output = 'tests/output'
    target = CompilationTarget.PYTHON_3_5

    compile_files(input_, output, target)

# Generated at 2022-06-22 12:30:02.521005
# Unit test for function compile_files
def test_compile_files():
    # test: compile js to py
    code = """
        var a = 1
        var b = a + 1
        function f1(a) {
            return a + 1
        }
        var b = f1(a)
    """
    result = compile_files('unittest_input', 'unittest_output', CompilationTarget.PY, None)
    assert result == CompilationResult(1, 0.0, CompilationTarget.PY,
                                       ['system', 'web', 'document'])

# Generated at 2022-06-22 12:31:02.267250
# Unit test for function compile_files
def test_compile_files():
    target = CompilationTarget.JAVA
    result = compile_files('testdata/compile_test', 'testdata/compile_test_output', target)
    assert result.count == 2
    assert result.target == target
    assert result.compilation_time > 0

# Generated at 2022-06-22 12:31:04.078403
# Unit test for function compile_files
def test_compile_files():
    assert compile_files.__name__ == 'compile_files'
    assert compile_files.__doc__ is not None

# Generated at 2022-06-22 12:31:12.321306
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from .utils.helpers import path_str
    from .utils.context import cwd

    with TemporaryDirectory() as tempdir:
        path = Path(tempdir) / 'a.py'
        with path.open('w') as f:
            f.write('x=2')

        with cwd(path.parent):
            result = compile_files(path_str(path), path_str(path),
                                   CompilationTarget.STDLIB)

        assert result.files_compiled == 1
        assert result.time >= 0
        assert result.target == CompilationTarget.STDLIB
        assert result.dependencies == []

        assert path.read_text() == '__x = 2\n'

        dependencies = set()

# Generated at 2022-06-22 12:31:20.824348
# Unit test for function compile_files
def test_compile_files():
    import unittest

    class CompileFilesTest(unittest.TestCase):
        def test_0(self):
            result = compile_files(
                'tests/fixtures/compile/input/classy',
                'tests/fixtures/compile/output',
                CompilationTarget.BROWSER)

            self.assertEqual(result.count, 3)
            self.assertEqual(
                result.dependencies,
                ['__main__',
                 'classy',
                 'classy.mixin'])

# Generated at 2022-06-22 12:31:27.989462
# Unit test for function compile_files
def test_compile_files():
    import unittest
    from pprint import pformat
    from pyfakefs.fake_filesystem_unittest import TestCase
    from . import fakefs
    from .fakefs_helpers import FakeFile

    class CompileFilesTests(TestCase):

        def setUp(self):
            self.setUpPyfakefs()
            fakefs.file_system = self.fs
            self.fs.add_real_directory(__file__[:-11])

        def test_simple(self):
            self.fs.create_dir('test')

            test = FakeFile(
                'test/test.py',
                '''
                    assert True
                '''
            )

            result = compile_files(test.path, 'test/test.py', 'js')

# Generated at 2022-06-22 12:31:28.678427
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:31:31.373532
# Unit test for function compile_files
def test_compile_files():
    # TODO
    pass

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:31:34.592724
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+t') as f:
        compile_files('../test/include', f.name, CompilationTarget.PROTO)
        print(f.read())

# Generated at 2022-06-22 12:31:44.381314
# Unit test for function compile_files
def test_compile_files():
    target = CompilationTarget.Python3
    input_dir = './tests/input/'
    output_dir = './tests/output/'

    result = compile_files(input_dir, output_dir, target)
    assert result.count == 2, 'Wrong count'
    assert target == result.target, 'Wrong target'
    assert result.dependencies == ['re', 'ast', 'cli'], 'Wrong dependencies'

    input_dir = './tests/smoke/'
    output_dir = './tests/output/smoke/'
    result = compile_files(input_dir, output_dir, target)
    assert result.count == 3, 'Wrong count'
    assert target == result.target, 'Wrong target'

# Generated at 2022-06-22 12:31:47.407867
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('input_files', 'output_files', 'js') == CompilationResult(1, 0, 'js', ['utils.py'])