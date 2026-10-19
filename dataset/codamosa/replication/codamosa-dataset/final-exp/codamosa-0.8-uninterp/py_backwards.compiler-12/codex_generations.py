

# Generated at 2022-06-22 12:24:39.081760
# Unit test for function compile_files
def test_compile_files():
    import unittest
    import tempfile
    import shutil
    import os

    class CompileFiles(unittest.TestCase):
        def setUp(self):
            self.test_input = tempfile.mkdtemp()
            self.test_output = tempfile.mkdtemp()
            self.test_file = os.path.join(self.test_input, 'test.py')

            with open(self.test_file, 'w') as f:
                f.write('''
    from typing import List
    ''')

        def tearDown(self):
            shutil.rmtree(self.test_input)
            shutil.rmtree(self.test_output)


# Generated at 2022-06-22 12:24:46.327083
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import os
    import shutil
    from os.path import dirname as parent_dir

    # Paths to files that will be used
    test_file = Path(__file__).parent / "test_files" / "test.py"
    tmp_dir = Path(__file__).parent / "tmp_dir"
    tmp_file = tmp_dir / "tmp.py"

    # Create temporary directory for files
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(str(tmp_dir))

    # Compile the file with the compile_files function

# Generated at 2022-06-22 12:24:49.694973
# Unit test for function compile_files
def test_compile_files():
    from .examples import test_input, test_output
    compile_files(test_input, test_output, CompilationTarget.PYTHON_35)
    assert True

# Generated at 2022-06-22 12:24:58.350260
# Unit test for function compile_files
def test_compile_files():
    from .utils.helpers import temp_dir
    from .tests.simple_tests import INPUT_DIR, OUTPUT_DIR, EXPECTED_DIR

    result = compile_files(INPUT_DIR, OUTPUT_DIR, CompilationTarget.PYTHON3,
                           temp_dir())
    assert result.files == 1
    assert result.time > 0
    assert result.target == CompilationTarget.PYTHON3

    result = compile_files(OUTPUT_DIR, EXPECTED_DIR, CompilationTarget.PYTHON3,
                           temp_dir())
    assert result.files == 4
    assert result.time > 0
    assert result.target == CompilationTarget.PYTHON3

# Generated at 2022-06-22 12:25:02.584921
# Unit test for function compile_files
def test_compile_files():
    pass


print(compile_files("tests/data/input/valid/basic.py",
                    "tests/data/output/valid/basic.js",
                    CompilationTarget.JS,
                    root="./tests/data"))

# Generated at 2022-06-22 12:25:12.710068
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .transformers import get_config, Config
    from .transformers.base_transformers import BASE_PATH
    from .transformers.base_transformers import BaseCompilationTarget, BaseCompilationResult

    def get_test_results() -> Tuple[
            Tuple[str, int, int, BaseCompilationTarget],
            Optional[Tuple[str, str]],
            str,
            str,
            BaseCompilationResult]:
        for i in [1, 2, 3]:
            with open(str(Path(BASE_PATH) / 'tests' / 'test_{}.py'.format(i))) as f:
                code = f.read()
            config = get_config(code, BASE_PATH)
            if config is None:
                continue
            tree = ast.parse(code)
            result

# Generated at 2022-06-22 12:25:16.941025
# Unit test for function compile_files
def test_compile_files():
    input_ = "./test/test_data"
    output = "./test/test_data/build"
    target = CompilationTarget.PY2
    compile_files(input_, output, target)
    assert os.path.exists(output + '/a.py')

# Generated at 2022-06-22 12:25:26.672725
# Unit test for function compile_files
def test_compile_files():
    import pathlib
    from os import environ
    pathlib.Path('./result').rmdir()
    environ['PYTHONPATH'] = 'result'
    compile_files('test', 'result', CompilationTarget.pypy, 'test')
    assert pathlib.Path('./result/testfile1.py').exists()
    assert pathlib.Path('./result/test/testfile2.py').exists()
    import testfile1
    import testfile2
    assert testfile1.x == 4
    assert testfile2.x == 4
    assert testfile2.y == 5
    assert testfile2.z == 6

# Generated at 2022-06-22 12:25:38.411044
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files"""
    import os
    import tempfile
    import shutil
    import pytest

    path = os.path.realpath(os.path.dirname(__file__))
    fd, temp_path = tempfile.mkstemp()
    os.close(fd)
    shutil.copytree(os.path.join(path, 'example'), temp_path)

    result = compile_files(input_=temp_path,
                           output=temp_path + '_out',
                           target=CompilationTarget.JS)

    assert result.count == 1
    assert result.target == CompilationTarget.JS
    assert result.time > 0
    assert set(result.dependencies) == set()

    shutil.rmtree(temp_path)
    shutil.rmtree

# Generated at 2022-06-22 12:25:42.980703
# Unit test for function compile_files
def test_compile_files():
    # given
    input_ = 'tests/fixtures/sample_dir'
    output = 'tests/tmp/sample_dir'
    target = CompilationTarget.ES5

    # when
    result = compile_files(input_, output, target)

    # then
    assert result.count == 7
    assert result.target == target
    assert len(result.dependencies) == 1
    assert result.dependencies[0] == 'third_party.js'

# Generated at 2022-06-22 12:25:57.771777
# Unit test for function compile_files
def test_compile_files():
    """Unit test for compile_files"""
    from pathlib import Path
    import shutil
    from random import randint, shuffle
    from .exceptions import CompilationError

    tests_dir = Path(__file__).parent.joinpath('tests')
    for path in tests_dir.iterdir():
        if not path.is_dir():
            continue
        if str(path).split('_')[0] != 'test':  # Checking that we are in a test directory
            continue
        if path.joinpath("__pycache__").exists():
            shutil.rmtree(path.joinpath("__pycache__"))
        

# Generated at 2022-06-22 12:26:09.069628
# Unit test for function compile_files
def test_compile_files():
    """Tests if files are compiled correctly."""
    import os
    import shutil

    from .compile import compile_files
    from . import CompilationResult

    in_ = './tests/compile/input'
    out = './tests/compile/output'
    result = compile_files(in_, out, CompilationTarget.pypi, root='.')

    assert result.count == 4
    assert result.compilation_target == CompilationTarget.pypi


# Generated at 2022-06-22 12:26:13.594539
# Unit test for function compile_files
def test_compile_files():
    from .mocks import mock_target_parser

    with mock_target_parser() as target:
        _, dependencies = _transform('test.py', 'a=1', target)
    assert dependencies == ['_make_file_import']

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:26:24.572457
# Unit test for function compile_files
def test_compile_files():
    import json
    import os
    import pytest

    def assert_output(input_, output, expected, root=None):
        import subprocess

        if root is None:
            root = os.path.join(os.path.dirname(input_), 'data')
        compiled = compile_files(input_, output, CompilationTarget.PY2, root)

        with pytest.raises(subprocess.CalledProcessError):
            subprocess.check_output(['diff', expected, os.path.join(output, 'test.py')])

        assert compiled.dependencies == []
        assert compiled.files == 1
        assert compiled.target == CompilationTarget.PY2

        compiled = compile_files(input_, output, CompilationTarget.PY3)


# Generated at 2022-06-22 12:26:29.831775
# Unit test for function compile_files
def test_compile_files():
    input_ = 'tests/simple_example/src/'
    output = 'tests/simple_example/out'
    target = CompilationTarget.PYTHON_38
    try:
        result = compile_files(input_, output, target)
    except:
        raise Exception('Unknown error during compilation.')
    assert result.count == 10 and result.total_time > 0

# Generated at 2022-06-22 12:26:35.484631
# Unit test for function compile_files
def test_compile_files():
    code = """
    def f():
        return 1
    """
    result = compile_files(input_='input', output='output', target=CompilationTarget.Q)
    assert unparse(ast.parse(code, 'test.py')) == unparse(ast.parse(result, 'test.py'))

# Generated at 2022-06-22 12:26:41.681344
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil

    output = os.path.join(os.path.dirname(__file__), "temp")
    input_ = os.path.join(os.path.dirname(__file__), "data")
    shutil.copytree(input_, output)
    try:
        result = compile_files(input_, output, CompilationTarget.STUB)
        assert result.count == 4
        assert len(result.dependencies) == 4
    finally:
        shutil.rmtree(output)



# Generated at 2022-06-22 12:26:52.848351
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import itertools
    import astunparse
    import typed_ast.ast3 as ast

    input_dir = Path(tempfile.gettempdir())
    output_dir = Path(tempfile.mkdtemp())
    print('input_dir: {}'.format(input_dir))
    print('output_dir: {}'.format(output_dir))


# Generated at 2022-06-22 12:27:02.258966
# Unit test for function compile_files
def test_compile_files():
    from .files import get_input_output_paths
    from .compilers import compile_files
    (c_in, c_out) = get_input_output_paths(
            'tests/data/tst', 'tst_out', root='tests/data')
    print(c_in, c_out)
    (py_in, py_out) = get_input_output_paths(
            'tests/data/tst_py', 'tst_out', root='tests/data')
    print(py_in, py_out)
    (c_nest_in, c_nest_out) = get_input_output_paths(
            'tests/data/dir1/dir2/dir3/c_nest', 'tst_out', root='tests/data')

# Generated at 2022-06-22 12:27:10.441798
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('_test/test.py', '_test/test_new.py', CompilationTarget.BROWSER)
    assert compile_files('_test/test.py', '_test/test_new.py', CompilationTarget.CLIENT)
    assert compile_files('_test/test.py', '_test/test_new.py', CompilationTarget.SERVER)
    assert compile_files('_test/test.py', '_test/test_new.py', CompilationTarget.SERVER, "_test/app")


if __name__ == "__main__":
    test_compile_files()

# Generated at 2022-06-22 12:27:28.916284
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    compiler = tempfile.mkdtemp()
    core = tempfile.mkdtemp()
    compiled = tempfile.mkdtemp()
    with open(core + '/core.py', 'w') as f:
        f.write('def core():\n    pass\n')
    with open(compiler + '/compiler.py', 'w') as f:
        f.write('import core\n\ncore.core()')
    result = compile_files(compiler, compiled, CompilationTarget.RUN)
    assert result.count == 1
    assert result.target == CompilationTarget.RUN
    assert result.dependencies == ['core']
    assert result.time > 0
    assert 'core' in compiled

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:27:40.064552
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os.path
    from .files import resolve_root
    from .types import CompilationTarget
    from .exceptions import CompilationError
    from .utils.helpers import ensure_path
    from .compiler import compile_files

    root = resolve_root()
    input_ = ensure_path(root, 'py-mjs')
    output = tempfile.mkdtemp()


# Generated at 2022-06-22 12:27:49.670971
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    import glob
    import filecmp

    def clear_dirs(src, out, root=None):
        dirs = [src, out]
        if root:
            dirs.append(root)
        for dir_ in dirs:
            if os.path.exists(dir_):
                shutil.rmtree(dir_)
        if root:
            os.mkdir(root)

    def test(name, code, target, expected_result):
        base_dir = os.path.join(os.path.dirname(__file__), '..',
                                'tests', 'test_compile_files')
        input_dir = os.path.join(base_dir, name, 'input')

# Generated at 2022-06-22 12:27:57.923600
# Unit test for function compile_files
def test_compile_files():
    import subprocess # type: ignore
    from pathlib import Path

    # Prepare
    subprocess.run(['python', '-m', 'pip', 'install', 'astunparse',
                    'typed-ast', 'autopep8'])
    input_ = Path('testdata/compilation/input')
    output = Path('testdata/compilation/output')

    # Run
    compile_files(input_, output, CompilationTarget.CPYTHON35)

    # Verify
    # TODO
    # python -m pytest verification.py
    # pytest verification.py

# Generated at 2022-06-22 12:28:00.480122
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/fixtures/sources', 'build/sources_py2', CompilationTarget.PY2)


# Generated at 2022-06-22 12:28:04.478593
# Unit test for function compile_files
def test_compile_files():
    output = '/tmp/wheezy.template/output'
    assert compile_files('tests/fixtures/app', output, CompilationTarget.ES5)
    assert compile_files('tests/fixtures/app', output, CompilationTarget.ES6)

# Generated at 2022-06-22 12:28:06.725714
# Unit test for function compile_files
def test_compile_files():
    assert compile_files("tests/data/helloworld", "output", CompilationTarget.PYTHON3)

# Generated at 2022-06-22 12:28:07.824529
# Unit test for function compile_files
def test_compile_files():
    # TODO
    pass

# Generated at 2022-06-22 12:28:19.996831
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from .exceptions import ExtensionError
    from .types import CompilationTarget
    from .utils.helpers import get_path
    from .utils.test_helpers import assert_code_equal

    def remove_whitespace(s: str) -> str:
        return ' '.join(s.replace(' \n', '').split())

    for target in [CompilationTarget.PYTHON_3, CompilationTarget.PYTHON_2]:
        with TemporaryDirectory() as tempdir:
            assert compile_files(
                get_path('good/hello.magma'),
                Path(tempdir, 'hello.py'),
                target)

# Generated at 2022-06-22 12:28:28.747227
# Unit test for function compile_files
def test_compile_files():
    import os
    from pytest import approx
    from time import time
    from .utils.helpers import debug, debug_off

    debug_off()
    here = os.path.dirname(__file__)
    input_ = os.path.join(here, '../tests/')
    output = os.path.join(here, '../tests_out/')
    target = CompilationTarget.fsharp
    root = os.path.join(here, '../tests/')
    dependencies = compile_files(input_, output, target, root).dependencies