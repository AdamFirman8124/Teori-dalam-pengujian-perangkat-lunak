

# Generated at 2022-06-22 12:24:40.742157
# Unit test for function compile_files
def test_compile_files():
    expected_code = textwrap.dedent("""
        def hello():
            print('Hello World')""")

    def test_case(inp: str, output: str, target: CompilationTarget,
                  dependencies: List[str]=[]):
        result = compile_files('tests/fixtures/compiler/input', output, target)
        assert result.transpiled_files == 1
        assert result.dependencies == dependencies
        with open(output) as f:
            assert f.read() == expected_code

    test_case(
        'tests/fixtures/compiler/input',
        'tests/fixtures/compiler/sut',
        CompilationTarget.RELEASE
    )


# Generated at 2022-06-22 12:24:51.984635
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .exceptions import CompilationError

    input_dir = Path(__file__).parent.joinpath('files')
    output_dir = input_dir.parent.joinpath('files_output')

    # Simple test
    result = compile_files(input_dir, output_dir, CompilationTarget.JS)
    assert result.time > 0  # Some time should be passed
    assert result.count == 3

    # Test with invalid code
    with open(input_dir.joinpath('fail.py'), 'w') as f:
        f.write('fail')

    with pytest.raises(CompilationError):
        compiler = compile_files(input_dir, output_dir, CompilationTarget.JS)

    # Test with invalid target

# Generated at 2022-06-22 12:25:02.918585
# Unit test for function compile_files
def test_compile_files():
    path = Path(__file__).parent
    input_ = path / 'input_files'
    output = path / 'output_files'
    result = compile_files(str(input_), str(output), CompilationTarget.COCOS2D_JS)
    output = path / 'output_files' / 'js'

    assert len(result.dependencies) == 2


# Generated at 2022-06-22 12:25:12.846091
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from datetime import datetime as dt
    from pathlib import Path
    from os import path

    # create and test temp directory
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        input_dir = tmpdir.joinpath('in')
        output_dir = tmpdir.joinpath('out')
        input_dir.mkdir(parents=True, exist_ok=True)
        output_dir.mkdir(parents=True, exist_ok=True)
        init_file = input_dir.joinpath('__init__.py')
        init_file.touch(exist_ok=True)
        test_file = input_dir.joinpath('test.py')

# Generated at 2022-06-22 12:25:16.755821
# Unit test for function compile_files
def test_compile_files():
    import os
    path = os.path.dirname(__file__)
    compile_files(__file__, path, CompilationTarget.GPCI)

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:25:28.496765
# Unit test for function compile_files
def test_compile_files():
    from pytest import fixture, raises
    from py.path import local
    from os import path

    @fixture
    def fixture_data_path():
        return local(path.dirname(__file__)) / 'fixture'

    with raises(ValueError):
        compile_files(fixture_data_path / 'input',
                      fixture_data_path / 'output',
                      CompilationTarget.PYTHON)

    result = compile_files(fixture_data_path / 'input',
                           fixture_data_path / 'output',
                           CompilationTarget.PYTHON,
                           fixture_data_path.as_posix())
    assert result.count == 3
    assert result.dependencies == ['bar.py', 'foo.py', 'quux.py']



# Generated at 2022-06-22 12:25:39.806595
# Unit test for function compile_files
def test_compile_files():
    import os
    import filecmp
    expected_result = [
        'def main():',
        '    return 42',
        ''
    ]

    input_ = 'test_directory'
    output = 'test_output'
    target = 'default'
    os.makedirs(input_)
    os.makedirs(output)
    with open(os.path.join(input_,'main.py'),'w') as f:
        f.write('main\n')
    compile_files(input_, output, target)

    assert filecmp.cmp(os.path.join(output,'main.cpp'),
                        os.path.join('test_directory_result','main.cpp'))

# Generated at 2022-06-22 12:25:45.081203
# Unit test for function compile_files
def test_compile_files():
    input_ = "tests/code/input"
    output = "tests/code/output"
    result = compile_files(input_, output, "js", "tests")

    assert result.count == 5
    assert result.target == "js"
    assert result.duration > 0
    assert "tests/code/compiler.py" in result.dependencies
    assert "tests/code/input/a.py" in result.dependencies
    assert "tests/code/input/b.py" in result.dependencies
    assert "tests/code/input/c.py" not in result.dependencies

    with open(output + "/a.js") as f:
        assert "var b = new B();" in f.read()


# Generated at 2022-06-22 12:25:45.948656
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:25:56.529027
# Unit test for function compile_files
def test_compile_files():
    # Create files
    input_ = Path('./input/')
    output = Path('./output/')
    for name in ('a.py', 'b.py', 'c.py', 'd.py'):
        input_.joinpath(name).touch()
    assert compile_files('./input/', './output/', CompilationTarget.PYTHON) == CompilationResult(4, 0, CompilationTarget.PYTHON, [])
    assert compile_files('./input/', './output/', CompilationTarget.JAVASCRIPT) == CompilationResult(4, 0, CompilationTarget.JAVASCRIPT, [])
    # Delete files
    shutil.rmtree('./input/')
    shutil.rmtree('./output/')
test_compile_files()

# Generated at 2022-06-22 12:26:07.577721
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationResult
    from .exceptions import CompilationError
    from .files import get_path
    from .utils.helpers import tmp_dir

    with tmp_dir() as d:
        input_path = get_path(d, 'src')
        output_path = get_path(d, 'dst')
        input_path.mkdir(parents=True)

# Generated at 2022-06-22 12:26:15.836591
# Unit test for function compile_files
def test_compile_files():
    from .testing import get_test_input, get_test_output
    assert compile_files(get_test_input('one'),
                         get_test_output(),
                         CompilationTarget.STANDALONE).count == 1
    assert compile_files(get_test_input('call'),
                         get_test_output(),
                         CompilationTarget.STANDALONE).count == 1
    assert compile_files(get_test_input('modules/my_module.py'),
                         get_test_output(),
                         CompilationTarget.STANDALONE).count == 1

# Generated at 2022-06-22 12:26:17.965236
# Unit test for function compile_files
def test_compile_files():
    _ = compile_files('./tests/files/input', './tests/files/output', CompilationTarget.AST)
    assert _.count == 2

# Generated at 2022-06-22 12:26:27.071312
# Unit test for function compile_files
def test_compile_files():
    from .context import compile, run, CompilationTarget
    import json

    input_ = 'tests/test_data'
    output = './test.py'
    compile(input_, output, CompilationTarget.python_v3_6)

    a = run(output)

    assert json.dumps(a) == '{"a":"1","b":"2","c":"3"}'

    input_ = 'tests/test_data'
    output = './test.py'
    compile(input_, output, CompilationTarget.python_v3_7)

    a = run(output)

    assert json.dumps(a) == '{"a":"1","b":"2","c":"3"}'
    assert a['a'] == "1"
    assert a['b'] == "2"

# Generated at 2022-06-22 12:26:38.519099
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    import shutil
    import subprocess

    test_path = os.path.split(__file__)[0]
    temp_path = tempfile.gettempdir()

    compile_files(test_path, temp_path, CompilationTarget.C99)
    compile_files(test_path, temp_path, CompilationTarget.C89)
    compile_files(test_path, temp_path, CompilationTarget.C89, 'regex')

    C99_generated = subprocess.check_output([
        os.path.join(temp_path, 'Compilation', 'C99', 'regex', 'regex.c')
    ]) .decode()

    assert(C99_generated == 'int main() {\n\treturn 0;\n}\n')

    shutil.rmt

# Generated at 2022-06-22 12:26:45.292049
# Unit test for function compile_files
def test_compile_files():
    with open('tests/files/unit/tests_compile_files.py', 'r') as f:
        code = f.read()
    tree = ast.parse(code, 'tests/files/unit/tests_compile_files.py')
    tree = transformers[0].transform(tree).tree
    #print(unparse(tree))

if __name__ == "__main__":
    test_compile_files()

# Generated at 2022-06-22 12:26:48.310405
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/packages/import_package/', 'tests/output/import_package/python/', target=CompilationTarget.PYTHON)

# Generated at 2022-06-22 12:26:52.128564
# Unit test for function compile_files
def test_compile_files():
    source = "./test_data/test.py"
    target = "./test_data/test.js"
    compile_files(source, target, 'node')
    import subprocess
    print(subprocess.check_output(['node', target]))

# Generated at 2022-06-22 12:27:01.798462
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from tempfile import TemporaryDirectory
    import json

    example = '''
    """Hello, world!"""

    import math


    def square(x):
        return x * x


    def main():
        print(square(10))
    '''

    input_ = 'example.py'
    output = 'compiled/example.py'
    with TemporaryDirectory() as tmp:
        with open(tmp + '/' + input_, 'w') as f:
            f.write(example)
        res = compile_files(input_, output, CompilationTarget.INTERPRETER, tmp)
        assert res.count == 1
        with open(tmp + '/' + output, 'r') as f:
            output = unparse(ast.parse(f.read(), output))

# Generated at 2022-06-22 12:27:11.663928
# Unit test for function compile_files
def test_compile_files():
    import pytest
    import re
    import os
    import shutil
    from pathlib import Path
    from .utils.helpers import ProjectPath

    @pytest.fixture(scope='module', autouse=True)
    def cleanup():
        yield
        if os.path.exists(ProjectPath.test_output):
            shutil.rmtree(ProjectPath.test_output)

    def test_compile(source, expected_files, target):
        result = compile_files(ProjectPath.test_input,
                               ProjectPath.test_output,
                               target)
        assert result.count == len(expected_files)
        assert sorted(path.as_posix() for path in expected_files) == \
            sorted(result.dependencies)
        for path in expected_files:
            assert path.exists

# Generated at 2022-06-22 12:27:22.864219
# Unit test for function compile_files
def test_compile_files():
    from .files import get_paths_from_string
    tmp_input = get_paths_from_string('data/input.py')[0]
    tmp_output = get_paths_from_string('data/output.py')[0]
    compile_files(tmp_input, tmp_output, CompilationTarget.STUB)
    print('Done')

# Generated at 2022-06-22 12:27:31.446879
# Unit test for function compile_files
def test_compile_files():
    import pathlib
    import tempfile
    import shutil
    import doctest
    import tests
    import tests.test_internals
    import tests.test_compiler

    tmpdir = pathlib.Path(tempfile.mkdtemp())


# Generated at 2022-06-22 12:27:33.712760
# Unit test for function compile_files
def test_compile_files():
    pass


if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:27:38.015995
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('examples', 'tests/output/examples',
                      CompilationTarget.PYTHON, 'examples') == CompilationResult(4, 0.0, CompilationTarget.PYTHON,
                                                                                 ['sys', 'os', 'sys', 'os'])

# Generated at 2022-06-22 12:27:47.893892
# Unit test for function compile_files
def test_compile_files():
    from .utils import get_test_files, assert_files_equal

    assert_files_equal('file1.py', 'file1.js')
    assert_files_equal('file2.py', 'file2.js')
    assert_files_equal('file3.py', 'file3.js')

    input_ = get_test_files('test_files')
    output = get_test_files('test_compiled_files')
    result = compile_files(input_, output, CompilationTarget.READABLE)
    assert result.files_processed == 3
    assert result.dependencies == ['math']
    assert_files_equal('test_compiled_files/file1.js', 'file1.js')
    assert_files_equal('test_compiled_files/file2.js', 'file2.js')

# Generated at 2022-06-22 12:27:49.104124
# Unit test for function compile_files
def test_compile_files():
    # TODO: add file test
    pass

# Generated at 2022-06-22 12:27:59.608546
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import os
    import shutil

    p = lambda path: os.path.join(tempfile.gettempdir(), path)
    root = tempfile.mkdtemp()


# Generated at 2022-06-22 12:28:04.589292
# Unit test for function compile_files
def test_compile_files():
    from . import run
    from .consts import DEFAULT_TARGET
    from .exceptions import CompilationError

    try:
        run('test/test_data/compile_files', 'test/test_data/dist',
            DEFAULT_TARGET)
    except CompilationError:
        assert False

# Generated at 2022-06-22 12:28:16.457368
# Unit test for function compile_files
def test_compile_files():
    import datetime
    input_ = './tests/data/compile_files/input'
    output = './tests/data/compile_files/output'
    target = CompilationTarget.PYTHON3
    result = compile_files(input_, output, target)
    test = 'compile_files({!r}, {!r}, {!r})'.format(input_, output, target)
    assert result.count == 3, '{} count '.format(test)
    assert result.elapsed < 0.1, '{} elapsed'.format(test)
    assert result.target == target, '{} target '.format(test)
    expected_dep = {
        'foo.txt',
        'bar.txt',
    }

# Generated at 2022-06-22 12:28:21.668529
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/data/modules',
                         'tests/output/modules',
                         CompilationTarget.PYTHON_VERSION) == CompilationResult(count=3,
                                                                               time=0.0,
                                                                               target=CompilationTarget.PYTHON_VERSION,
                                                                               dependencies=['six'])

# Generated at 2022-06-22 12:28:44.816743
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files"""
    from pathlib import Path
    from .types import CompilationTarget
    from .utils import invoke
    from tempfile import TemporaryDirectory
    from shutil import rmtree
    import os
    import sys

    with TemporaryDirectory() as temp_dir:
        temp_input = os.path.join(temp_dir, 'temp_input')
        temp_output = os.path.join(temp_dir, 'temp_output')
        os.mkdir(temp_input)
        os.mkdir(temp_output)

        with open(os.path.join(temp_input, 'path.py'), 'w') as f:
            f.write("""def foo():
    return 2 * 2
""")


# Generated at 2022-06-22 12:28:51.349747
# Unit test for function compile_files
def test_compile_files():
    from .files import OutputPath
    from .types import CompilationTarget, CompilationResult
    from pytest import raises
    from .exceptions import CompilationError
    from pathlib import Path
    import os
    import tempfile
    import shutil
    import sys
    import io


# Generated at 2022-06-22 12:28:55.133568
# Unit test for function compile_files
def test_compile_files():
    # Compile example program
    output = './unit_tests/output'
    input_ = './unit_tests/input/example'
    result = compile_files(input_, output, 'py')
    # Check compilation result
    assert result.count == 8
    assert result.target == 'py'
    assert result.dependencies == []
    assert result.duration >= 0

# Generated at 2022-06-22 12:29:07.033446
# Unit test for function compile_files
def test_compile_files():
    class fake_path:
        parent = True
        def __init__(self, path: str):
            self.path = path
            self.posix = path
        def open(self, mode: str = 'r'):
            return self
        def read(self):
            return self.path
        def write(self, code: str):
            pass
        def __call__(self, path: str, mode: str = 'r'):
            return self
    expected = CompilationResult(2, 1, CompilationTarget.BACKEND, [])
    class fake_get_input_output_paths:
        count = 0
        paths = None
        def __call__(self, input_: str, output: str, root: Optional[str] = None):
            if self.count == 0:
                self.count += 1


# Generated at 2022-06-22 12:29:09.004095
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/test.yaml', 'tests/test_out', CompilationTarget.CLIENT)

# Generated at 2022-06-22 12:29:17.463815
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os
    import glob
    test_root = tempfile.mkdtemp()
    test_input = os.path.join(test_root, "input")
    test_output = os.path.join(test_root, "output")
    os.mkdir(test_input)
    os.mkdir(test_output)
    test_file_path = os.path.join(test_input, "test_file.py")

# Generated at 2022-06-22 12:29:29.191261
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import os
    from .test import test_input_path, test_output_path

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_input = os.path.join(tmp_dir, 'input')
        tmp_output = os.path.join(tmp_dir, 'output')

        os.makedirs(tmp_input)

        with open(os.path.join(tmp_input, 'test.js'), 'w') as f:
            f.write('print("test")')

        compile_files(tmp_input, tmp_output, CompilationTarget.EXTENSION)

        with open(os.path.join(tmp_output, 'test.py'), 'r') as f:
            assert f.read() == """import js

js.document.print("test")
"""

# Generated at 2022-06-22 12:29:41.401624
# Unit test for function compile_files
def test_compile_files():
    from .compiler import compile_files
    from .types import CompilationTarget
    paths = ['./tests/samples/pizza-compiler-test/', './tests/samples/pizza-compiler-output/']
    input_, output = paths
    target = CompilationTarget.LAMBDA_SIMPLIFIED
    root = './tests/samples/'
    result = compile_files(input_, output, target, root)
    assert result.target == target
    assert result.count == 3
    assert result.dependencies == ['Base', 'HasCheese', 'HasMeat']
    assert result.time > 0


if __name__ == '__main__':
    import sys
    from .types import CompilationTarget
    from .exceptions import CompilationError
    import argparse

    argparser = argparse

# Generated at 2022-06-22 12:29:50.447034
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .exceptions import CompilationError
    from .helpers import get_path, remove_path

    # Unit test for the compilation of a valid file
    def test_valid_file():
        input_ = get_path('compiler', 'input', 'valid')
        output = get_path('compiler', 'output', 'valid')
        remove_path(output)
        result = compile_files(input_, output, CompilationTarget.PYTHON)
        assert result.count == 5
        assert result.dependencies == ['typing']
        assert result.duration > 0
        assert result.target == CompilationTarget.PYTHON

# Generated at 2022-06-22 12:29:53.295072
# Unit test for function compile_files

# Generated at 2022-06-22 12:30:37.028071
# Unit test for function compile_files
def test_compile_files():
    input_folder = Path(__file__).parent.parent.joinpath('tests', 'test_input')
    output_folder = Path(__file__).parent.parent.joinpath('tests', 'test_output')
    # compile_files(input_folder, output_folder, CompilationTarget.PYTHON)


if __name__ == '__main__':
    print(compile_files(Path('example/input'), Path('example/output'),
                        CompilationTarget.PYTHON))

# Generated at 2022-06-22 12:30:45.396022
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os
    import os.path
    import sys

    # To generate test files we need to install typing_extensions
    #
    # pip3 install typing_extensions
    from .examples import generate_module

    # Create an input file
    input_dir = tempfile.mkdtemp()
    output_dir = tempfile.mkdtemp()
    generate_module(os.path.join(input_dir, 'input_file.py'), force_run=True)

    # Create an output file
    target = CompilationTarget.PY2
    CompilationResult(1, 0, target, [])

    # Compile the input file
    result = compile_files(input_dir, output_dir, target)

    # Make sure the output file is present
    assert os.path.ex

# Generated at 2022-06-22 12:30:54.662609
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    import tempfile
    import textwrap

    def assertEqual(first, second):
        assert first == second

    def assertNotEqual(first, second):
        assert first != second

    def assertTrue(x):
        assert x

    def assertFalse(x):
        assert not x

    def assertRaises(exception, func, *args, **kwds):
        try:
            func(*args, **kwds)
        except exception:
            return
        except:
            raise AssertionError("%s is raised instead of %s" %
                                 (sys.exc_info()[0], exception))
        else:
            raise AssertionError("%s is not raised" % exception)


# Generated at 2022-06-22 12:31:00.929240
# Unit test for function compile_files
def test_compile_files():
    import unittest
    import tempfile
    import shutil
    import os.path as path
    import pathlib

    class CompileFilesTest(unittest.TestCase):
        def setUp(self):
            self.__tmp = tempfile.TemporaryDirectory()
            self.__input = path.join(self.__tmp.name, 'input')
            self.__output = path.join(self.__tmp.name, 'output')
            shutil.copytree(path.join(path.dirname(__file__), '..', 'test',
                                      'test_data', 'input'), self.__input)
            shutil.copytree(path.join(path.dirname(__file__), '..', 'test',
                                      'test_data', 'expected'), self.__output)


# Generated at 2022-06-22 12:31:10.051786
# Unit test for function compile_files
def test_compile_files():
    import subprocess
    from .test import test_path

    def compile(input_: str, output: str, root: str) -> CompilationResult:
        return compile_files(input_, output, CompilationTarget.PY35, root)

    def prepare(dir: str) -> None:
        subprocess.call(["rm", "-rf",
                         str(test_path("test_compile/output/{}".format(dir)))])

    def compare(dir: str) -> bool:
        return subprocess.call(["diff",
                                str(test_path("test_compile/expected/{}".format(dir))),
                                str(test_path("test_compile/output/{}".format(dir)))]) == 0

    def test(dir: str) -> None:
        prepare(dir)
       

# Generated at 2022-06-22 12:31:17.951202
# Unit test for function compile_files
def test_compile_files():
    test_compile_file = compile_files("/Users/yevgeniy/PycharmProjects/pypypypypypypypypypypypypypypypypypypypy/compile/tests/input", "/Users/yevgeniy/PycharmProjects/pypypypypypypypypypypypypypypypypypypypy/compile/tests/output", CompilationTarget.RUNTIME)
    assert test_compile_file.count == 4, "there should be 4 files in the input"
    assert test_compile_file.target == CompilationTarget.RUNTIME, "target should be RUNTIME"
    assert test_compile_file.dependencies == ['sys'], "dependencies should be equal to sys"



# Generated at 2022-06-22 12:31:26.401543
# Unit test for function compile_files
def test_compile_files():
    from .testing import assert_compile
    assert_compile('tests/input_data/simple/', 'tests/output_data/simple/', 'tests/expected_data/simple/')
    assert_compile('tests/input_data/deeper/', 'tests/output_data/deeper/', 'tests/expected_data/deeper/')
    assert_compile('tests/input_data/simple_package/', 'tests/output_data/simple_package/', 'tests/expected_data/simple_package/', 'tests/input_data')

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:31:30.851034
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from tempfile import TemporaryDirectory
    from os import path
    from pathlib import Path
    from .testcases import TEST_CASES
    from glom import glom

    def pre_compile_test_cases():
        for test_case in TEST_CASES:
            for target in CompilationTarget:
                if target > test_case.target:
                    continue

                # Compile test case with target
                with TemporaryDirectory() as dirname:
                    output = path.join(dirname, 'out')
                    compile_files(test_case.input_, output, target)

                    # Check compiled result
                    compiled = Path(output)
                    expected = compiled.parent / 'expected{}.py'.format(target.value)

                    # Create expected file if not exists

# Generated at 2022-06-22 12:31:42.515129
# Unit test for function compile_files
def test_compile_files():
    from .utils.testing import project_path
    import sys

    if sys.version_info < (3, 6):
        sys.stderr.write('WARNING: Skipped unit test with target {} '
                         'due to Python version {}.{} is less then needed '
                         '3.6.\n'.format(CompilationTarget.PYTHON_36,
                                         sys.version_info.major,
                                         sys.version_info.minor))
        return

    result = compile_files(project_path('tests/data/strict'),
                           project_path('tests/data/strict_compiled'),
                           CompilationTarget.PYTHON_36)
    assert result.count == 5

# Generated at 2022-06-22 12:31:53.012524
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil

    tmp = tempfile.mkdtemp()
    try:
        with open(tmp + '/input.py', 'w') as f:
            f.write('def add(x, y):\n    return x + y\n')

        compile_files(tmp + '/input.py', tmp + '/output.py', CompilationTarget.JAVA)

        with open(tmp + '/output.py', 'r') as f:
            assert f.read() == 'def add(x, y):\n    return int(x) + int(y)\n'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)