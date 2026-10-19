

# Generated at 2022-06-22 12:24:43.328487
# Unit test for function compile_files
def test_compile_files():
    import astunparse
    import unittest
    import os.path
    import subprocess
    import shutil
    import tempfile

    class TestCompileFiles(unittest.TestCase):
        def setUp(self):
            # Create a temporary directory
            self.test_dir = tempfile.mkdtemp()
            self.test_input_dir = os.path.join(self.test_dir, 'input')
            self.test_output_dir = os.path.join(self.test_dir, 'output')
            os.makedirs(self.test_input_dir)
            os.mkdir(self.test_output_dir)
            self.original_dir = os.getcwd()
            os.chdir(self.test_dir)


# Generated at 2022-06-22 12:24:53.097037
# Unit test for function compile_files
def test_compile_files():
    from . import __version__
    from .exceptions import CompilationError
    from .transformers import TestTransformer
    import tempfile
    import os
    import shutil


# Generated at 2022-06-22 12:25:03.912306
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    import shutil
    import sys
    import subprocess
    from itertools import repeat
    import aot.paths
    import doctest
    import coverage

    input_ = aot.paths.root()/'tests'/'data'/'compile'/'input'
    target = 'python3.3'
    cwd = os.path.dirname(__file__)
    test_names = ('test_add', 'test_class',
                  'test_function', 'test_lambda', 'test_while')

    tmp = tempfile.TemporaryDirectory()
    os.chdir(tmp.name)

    for name in test_names:
        with open(name, 'w') as f:
            f.write('')

# Generated at 2022-06-22 12:25:04.959814
# Unit test for function compile_files
def test_compile_files():
    # TODO make unit tests
    pass

# Generated at 2022-06-22 12:25:10.657924
# Unit test for function compile_files
def test_compile_files():
    """
    Compiles all files from input_ to output.
    """
    input_ = "../../test_data/stubs/classes"
    output = "../../test_data/stubs/classes/compiled"
    root = "../../stubs/classes"
    target = CompilationTarget.STUB

    result = compile_files(input_, output, target)
    assert result.count == 2
    assert result.target == target

# Generated at 2022-06-22 12:25:11.957043
# Unit test for function compile_files
def test_compile_files():
    """Tests function compile_files"""
    # TODO: test
    pass

# Generated at 2022-06-22 12:25:20.063744
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from .utils.helpers import remove_trailing_whitespaces, compare_results

    with TemporaryDirectory() as temp:
        input_ = input  # pylint: disable=undefined-variable
        print(compile_files(input_, temp, CompilationTarget.PYTHON))
        compare_results(input_, temp)

        txt = remove_trailing_whitespaces(r"""
            def f():
                a = 0 # Line comment
        """)

        with open(temp + '/a.py', 'w') as f:
            f.write(txt)

        # Raise on SyntaxError

# Generated at 2022-06-22 12:25:29.183217
# Unit test for function compile_files
def test_compile_files():
    input_ = './tests/fixtures/compile'
    output = './tests/fixtures/compile_output'
    all_files = [Path('./tests/fixtures/compile/test.py'),
                 Path('./tests/fixtures/compile/test2.py'),
                 Path('./tests/fixtures/compile/subfolder/test3.py')]

    result = compile_files(input_, output, CompilationTarget.target)
    assert result.count == 3
    assert result.target == CompilationTarget.target
    assert result.dependencies == [
        './tests/fixtures/compile/test.py',
        './tests/fixtures/compile/test2.py',
        './tests/fixtures/compile/subfolder/test3.py'
    ]

# Generated at 2022-06-22 12:25:40.026994
# Unit test for function compile_files
def test_compile_files():
    #pylint: disable=no-member
    from .types import CompilationTarget
    from .test.test_programs.program1 import program

    res = compile_files('foo', 'bar', CompilationTarget.SCRIPT)
    assert res.count == 0
    assert res.target == CompilationTarget.SCRIPT
    assert not res.dependencies.patches

    res = compile_files('.', '.', CompilationTarget.SCRIPT)
    assert res.count == 0
    assert res.target == CompilationTarget.SCRIPT
    assert not res.dependencies.patches

    compile_files('./tests/test_programs/program1', './tests/output',
                  CompilationTarget.SCRIPT)

# Generated at 2022-06-22 12:25:47.137060
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files"""
    # Setup
    input_ = 'tests/data'
    output = 'tests/tmp'
    target = CompilationTarget.javascript
    # Exercise
    compile_files(input_, output, target)
    # Verify
    assert sorted(os.listdir(output)) == ['a.js', 'b.js', 'c.js', 'd.js']
    assert sorted(os.listdir('tests/tmp/nested')) == ['e.js', 'f.js']

# Generated at 2022-06-22 12:26:00.718238
# Unit test for function compile_files
def test_compile_files():
    import tempfile

    input_ = tempfile.TemporaryDirectory()
    input_path = Path(input_.name)
    output_ = tempfile.TemporaryDirectory()
    output_path = Path(output_.name)

    with input_path.joinpath('main.py').open('w+') as f:
        f.write('''\
            from .api import *
            foo = 3.14
            add(foo, FOO)
            ''')

    with input_path.joinpath('api.py').open('w+') as f:
        f.write('''\
            FOO = 42
            def add(a, b):
                return str(a) + str(b)
            ''')

    result = compile_files(input_path, output_path, CompilationTarget.ES5)
   

# Generated at 2022-06-22 12:26:11.226906
# Unit test for function compile_files
def test_compile_files():
    import os
    import glob
    import subprocess

    def _compile_files(input_: str, output: str, target: CompilationTarget):
        """Helper function."""
        if not os.path.exists(output):
            os.makedirs(output)
        subprocess.call('python py2java/compile.py {} {} -t {}'.format(
                                                                        input_,
                                                                        output,
                                                                        str(target)),
                        shell=True)

    def _test_output(input_: str, output: str, target: CompilationTarget):
        """Helper function."""
        javafiles = glob.glob(os.path.join(output, '**/*.java'),
                              recursive=True)

# Generated at 2022-06-22 12:26:21.972437
# Unit test for function compile_files
def test_compile_files():
    import os
    import json
    import tempfile

    #if not os.path.isdir('test'):
    #    return

    root_dir = os.path.join(os.path.dirname(__file__), 'test')
    temp_dir = tempfile.mkdtemp()
    print('Temporary root directory:', temp_dir)
    input_dir = os.path.join(root_dir, 'input')
    output_dir = os.path.join(temp_dir, 'output')
    target = CompilationTarget.ES6

    print('Compiling files from', input_dir, 'to', output_dir)
    result = compile_files(input_dir, output_dir, target)

    result_filename = os.path.join(root_dir, 'result.json')

# Generated at 2022-06-22 12:26:26.637710
# Unit test for function compile_files
def test_compile_files():
    input_ = "./samples/build_python_ast"
    output = "./samples/build_python_ast_output"
    compile_files(input_, output, CompilationTarget.WEB)

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:26:33.709301
# Unit test for function compile_files
def test_compile_files():
    from shutil import rmtree
    import pytest

    @pytest.fixture
    def paths(tmpdir) -> Tuple[str, str, str]:
        input_dir = tmpdir.mkdir('compile_files/input')
        output_dir = tmpdir.mkdir('compile_files/output')

        yield (input_dir.strpath,
               output_dir.strpath,
               (input_dir / 'foo.py').strpath)


# Generated at 2022-06-22 12:26:34.621841
# Unit test for function compile_files
def test_compile_files():
  pass

# Generated at 2022-06-22 12:26:41.930378
# Unit test for function compile_files
def test_compile_files():

    import pytest

    from test.utils import default_project, expect_same_files

    with default_project(root='compile_files.test',
                         input='src',
                         output='out') as project:
        project.compile()

        paths = get_input_output_paths(project.input, project.output, project.root)
        assert len(list(paths)) == 5

        expect_same_files(project.input, project.output)

        with pytest.raises(FileNotFoundError):
            compile_files("not_exists", project.output, CompilationTarget.PY_TO_JS)

# Generated at 2022-06-22 12:26:53.098883
# Unit test for function compile_files
def test_compile_files():
    # Given
    import os
    import shutil

    INPUT_DIR = os.path.abspath('tests/fixtures/input')
    OUTPUT_DIR = os.path.abspath('tests/fixtures/output')
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    os.mkdir(OUTPUT_DIR)

    # When
    result = compile_files(INPUT_DIR, OUTPUT_DIR, CompilationTarget.JS)

    # Then
    assert result.count == 2
    assert result.time > 0
    assert result.target == CompilationTarget.JS
    assert len(result.dependencies) == 0


# Generated at 2022-06-22 12:27:00.945259
# Unit test for function compile_files
def test_compile_files():
    input_ = 'tests/inputs'
    output = 'tests/outputs'
    target = CompilationTarget.REPO
    root = 'tests/my_repo'
    compile_files(input_, output, target, root)
    for paths in get_input_output_paths(input_, output, root):
        output_code = ''
        with paths.output.open() as f:
            output_code = f.read()

        if paths.output.name == 'a.py':
            assert 'a' in output_code
        if paths.output.name == 'b.py':
            assert 'b' in output_code

# Generated at 2022-06-22 12:27:05.601469
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/data/input', 'tests/data/output',
                           CompilationTarget.ES5)
    print(result)
    print('Compiled {} files in {:.3f} seconds'.format(
        result.count, result.time))
    print('Dependencies: {}'.format(', '.join(result.dependencies)))

# Generated at 2022-06-22 12:27:18.883990
# Unit test for function compile_files
def test_compile_files():
    _test_compile_files()

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:27:29.475844
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tempdir:
        # Create 3 files in temp dir
        open(os.path.join(tempdir, 'a.py'), 'w').close()
        open(os.path.join(tempdir, 'b.py'), 'w').close()
        open(os.path.join(tempdir, 'c.py'), 'w').close()
        assert set(os.listdir(tempdir)) == {'a.py', 'b.py', 'c.py'}

# Generated at 2022-06-22 12:27:39.752081
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import subprocess
    import sys

    # TODO: use pyfakefs instead of tempfile
    with tempfile.TemporaryDirectory() as input_:
        path = input_ + '/test.js'
        code = '// @ts-ignore\nvar box = {x: "foo", y: "bar"}'
        with open(path, 'w') as f:
            f.write(code)

        with tempfile.TemporaryDirectory() as output:
            compile_files(input_, output, 'local')
            result = subprocess.check_output(
                [sys.executable, output + '/test.js']).decode()
            assert result == 'var box = {x: "foo", y: "bar"}'

# Generated at 2022-06-22 12:27:49.641131
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from .jsonencoder import encode

    code = '''from .compiled.bar import foo\ndef baz():\n    return foo()'''

    with TemporaryDirectory() as tempdir:
        paths = get_input_output_paths(
            Path(tempdir) / 'foo.py',
            Path(tempdir) / 'compiled/foo.py',
            tempdir
        )

        next(paths).input.write_text(code)
        next(paths).input.write_text(code.replace('from .compiled.bar', 'from bar'))

        compile_files(tempdir, tempdir, CompilationTarget.APP_TEST, tempdir)


# Generated at 2022-06-22 12:27:56.607846
# Unit test for function compile_files
def test_compile_files():
    from .tests import get_test_result
    import pytest

    run_compile_files = False
    with open("../tests/test_expected.txt", "r") as f:
        expected = f.read()
    with pytest.raises(Exception):
        result = compile_files("my-input", "output_folder", "l3")
        get_test_result(result)
    assert pytest.fail("Tests not yet implemented.")
test_compile_files()

# Generated at 2022-06-22 12:28:07.930880
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from pathlib import Path
    from itertools import zip_longest

    def get_files(path: Path) -> List[str]:
        if not path.exists():
            return []

        if path.is_file():
            return [path.as_posix()]

        return [p.as_posix() for p in path.iterdir()]

    def get_file_content(path: Path) -> str:
        with path.open() as f:
            return f.read()

    def compare_files(path1: Path, path2: Path) -> bool:
        if path1.is_file() and path2.is_file():
            return get_file_content(path1) == get_file_content(path2)

# Generated at 2022-06-22 12:28:10.801526
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('test/code', 'test/target',
                           CompilationTarget.pypy)
    assert result.files == 6



# Generated at 2022-06-22 12:28:16.574538
# Unit test for function compile_files
def test_compile_files():
    import tempfile

    target = CompilationTarget.DYNAMIC
    input_ = '../../samples/basic'
    output = tempfile.TemporaryDirectory().name
    result = compile_files(input_, output, target)
    assert result.target == target
    assert result.dependencies == ['__future__']
    assert result.processed_files == 10

# Generated at 2022-06-22 12:28:27.434575
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import re
    import pytest
    from .utils.helpers import path_set_to_string

    class TestCase:
        def __init__(self, input_: str, expected: str):
            self.input_ = input_
            self.expected = expected

    def test_case(input_: str, expected: str) -> TestCase:
        return TestCase(input_, expected)

    def run(input_, expected, target):
        """Compiles input_ to output, then checks against expected."""
        with Path('/tmp/input').as_cwd():
            input_.mkdir()
            expected.mkdir()
            result = compile_files(input_.as_posix(), expected.as_posix(), target)

# Generated at 2022-06-22 12:28:35.158682
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    import tempfile
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-22 12:29:03.334640
# Unit test for function compile_files
def test_compile_files():
    input_ = 'test/test_files'
    output = 'test/test_files_output'
    target = CompilationTarget.PYTHON
    root = 'test/test_files'
    result = compile_files(input_, output, target, root)
    print(result)

# Generated at 2022-06-22 12:29:07.121856
# Unit test for function compile_files
def test_compile_files():
    compile_files('/Users/luisramirez/Work/pytho-to-js/tests/sample/', '/Users/luisramirez/Work/pytho-to-js/tests/sample/', CompilationTarget.JAVASCRIPT)


# Generated at 2022-06-22 12:29:12.434348
# Unit test for function compile_files
def test_compile_files():
    """Unit test function compile_files."""
    result = compile_files('test/test_1/src', 'test/test_1/out', 'py38')
    assert result.target == 'py38'
    assert len(result.dependencies) == 0
    assert result.count == 14
    assert result.time > 0.0
    assert result.compile_target == None

# Generated at 2022-06-22 12:29:22.309795
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from tempfile import TemporaryDirectory
    from pathlib import Path

    from .exceptions import CompilationError
    from . import transformers

    def get_transformation_result(target: CompilationTarget) -> CompilationResult:
        with TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            in_ = tmpdir / 'in'
            out = tmpdir / 'out'
            in_.mkdir()
            (in_ / 'file1.py').write_text('file1')
            (in_ / 'file2.py').write_text('file2')
            (in_ / 'file3.py').write_text('file3')
            (in_ / 'file4.py').write_text('file4')

# Generated at 2022-06-22 12:29:30.028577
# Unit test for function compile_files
def test_compile_files():
    input_ = "/Users/dima/PycharmProjects/pythran-playground/tests/data/input/files"
    output = "/Users/dima/PycharmProjects/pythran-playground/tests/data/output/files"
    target = CompilationTarget.cpython36
    result = compile_files(input_, output, target, root=None)
    assert result.target == target
    assert result.count == 2
    assert result.time >= 0
    assert result.dependencies == []

# Generated at 2022-06-22 12:29:42.234790
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .utils.helpers import get_data_path
    from .exceptions import CompilationError
    from .transformers import remove_print_expr_transformer
    from .files import parse_root
    import json

    def check_generation(target: CompilationTarget,
                         expected_output_file: str = '',
                         expected_dependencies: Optional[List[str]] = None):
        compile_files(Path(__file__).parent / "test" / "source",
                      Path(__file__).parent / "test" / "output" /
                      target.name.lower(), target, parse_root(__file__))
        output_path = Path(__file__).parent / "test" / "output" / target.name.lower()

# Generated at 2022-06-22 12:29:45.206357
# Unit test for function compile_files
def test_compile_files():
    import pprint
    input_ = './tests/input'
    output = './tests/output'
    root = '.tests'

    print(compile_files(input_, output, CompilationTarget.JS, root))

# Generated at 2022-06-22 12:29:51.912827
# Unit test for function compile_files
def test_compile_files():
    import os
    cwd = os.path.dirname(os.path.realpath(__file__))
    input_ = os.path.join(cwd, '..', '..', 'resources')
    output = os.path.join(input_, '__pyc_cache__')
    file = 'hello.py'
    target = CompilationTarget.PY2
    result = compile_files(input_, output, target)
    assert file in result.dependencies


# Generated at 2022-06-22 12:29:59.636495
# Unit test for function compile_files
def test_compile_files():
    import os
    
    input_location = os.path.join('app')
    output_location = os.path.join('app')
    target_object = 'js'
    root_location = os.getcwd()
    compile_files(input_location, output_location,
                  target_object, root=root_location)
    # Example of output:
    # CompilationResult(
    # count=2,
    # time=0.0008646003723144531,
    # target='js',
    # dependencies=['/home/jupyter/super-transpiler-python/samples/decorators.py', '/home/jupyter/super-transpiler-python/samples/square.py']
    # )


test_compile_files()

# Generated at 2022-06-22 12:30:11.291287
# Unit test for function compile_files
def test_compile_files():
    import os
    import os.path
    import tempfile
    import shutil
    import unittest

    # Prepare a temporary directory
    dirpath = tempfile.mkdtemp()

    # Create test sketch
    sketch_path = os.path.join(dirpath, 'test_sketch')
    os.mkdir(sketch_path)