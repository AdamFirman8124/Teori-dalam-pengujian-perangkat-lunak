

# Generated at 2022-06-22 12:24:33.932692
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/data/input', 'tests/data/output', 'javascript')
    assert True

# Generated at 2022-06-22 12:24:45.783800
# Unit test for function compile_files
def test_compile_files():
    compile_files('../test/compilation/input/input_read.py', '../test/compilation/output/output_read.py', CompilationTarget.READ)
    with open('../test/compilation/compilation_result/output_read.py') as f1:
        with open('../test/compilation/output/output_read.py') as f2:
            assert f1.read() == f2.read()
    compile_files('../test/compilation/input/input_write.py', '../test/compilation/output/output_write.py', CompilationTarget.WRITE)
    with open('../test/compilation/compilation_result/output_write.py') as f1:
        with open('../test/compilation/output/output_write.py') as f2:
            assert f1

# Generated at 2022-06-22 12:24:57.012001
# Unit test for function compile_files
def test_compile_files():
    try:
        compile_files('./tests/compilable', './tests/compiled', 'python_2_7')
    except:
        assert False


if __name__ == '__main__':
    import os
    import sys
    import pprint

    if len(sys.argv) != 4:
        print('Usage: {} [input] [output] [target]'.format(sys.argv[0]))
        sys.exit(1)

    input_, output, target = sys.argv[1:]
    if not os.path.isdir(input_):
        print('Input "{}" does not exist'.format(input_))
        sys.exit(1)

    if os.path.isdir(output):
        print('Output "{}" exists'.format(output))
        sys.exit(1)

# Generated at 2022-06-22 12:24:59.183407
# Unit test for function compile_files
def test_compile_files():
    pass
# Test by typing
# from pythran import compile_files
# compile_files('input_', 'output', 'my_py')

# Generated at 2022-06-22 12:24:59.742927
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:25:02.633490
# Unit test for function compile_files
def test_compile_files():
    from .test.test_main_compiler import compile_files as test_compile_files
    test_compile_files()

# Generated at 2022-06-22 12:25:09.596529
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from os import path

    input_ = path.abspath('test/test_compile_files/input')
    output = path.abspath('test/test_compile_files/output')

    with TemporaryDirectory() as tmpdir:
        output = path.join(tmpdir, 'output')
        compile_files(input_, output, CompilationTarget.python)
        assert path.isfile(path.join(output, 'test.py'))



# Generated at 2022-06-22 12:25:18.443930
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from pathlib import Path
    from unittest import TestCase
    from .files import InputOutput
    from .transformers import AttrAccess, ListComprehension

    class CompileFilesTestCase(TestCase):
        def compile(self, target: CompilationTarget) -> CompilationResult:
            return compile_files(self.input_, self.output, target)

        def setUp(self):
            self.input_ = Path(__file__).parent.joinpath('files/input')
            self.output = Path(__file__).parent.joinpath('files/output')

        def test_compile_files(self):
            result = self.compile(CompilationTarget.ES6)

            self.assertEqual(result.count, 6)

# Generated at 2022-06-22 12:25:22.191988
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from os import getcwd
    with TemporaryDirectory() as tmpdir:
        compile_files(getcwd() + '/tests/', tmpdir, CompilationTarget.PYTHON)

# Generated at 2022-06-22 12:25:34.664072
# Unit test for function compile_files
def test_compile_files():
    import astunparse
    input_ = 'tests/data/input'
    output = 'tests/data/output'
    target = CompilationTarget.ES5
    result = compile_files(input_, output, target)
    assert result.count == 5
    assert isinstance(result.elapsed, float)

    # with open('tests/data/output/test.js') as f:
    #     print(astunparse.dump(ast.parse(f.read())))

    # import astunparse
    # input_ = 'tests/data/input/test.js'
    # output = 'tests/data/output/test.js'
    # target = CompilationTarget.ES5

    # with open(input_) as f:
    #     code = f.read()

    # _transform(input_, code, target

# Generated at 2022-06-22 12:25:45.357306
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('input/', 'output/', CompilationTarget.ES3)
    assert compile_files('input/', 'output/', CompilationTarget.ES5)
    assert compile_files('input/', 'output/', CompilationTarget.ES6)
    assert compile_files('input/', 'output/', CompilationTarget.ES6_STRICT)
    assert compile_files('input/', 'output/', CompilationTarget.ES5_STRICT)
    assert compile_files('input/', 'output/', CompilationTarget.ES3_STRICT)

# Generated at 2022-06-22 12:25:54.275604
# Unit test for function compile_files
def test_compile_files():
    print("Testing compile_files")

    try:
        compile_files("folder_input_compile_files", "folder_output_compile_files", CompilationTarget.JAVASCRIPT)
    except Exception as ex:
        if isinstance(ex, CompilationError):
            print("Exception", ex.message)
            print("Line", ex.line_number)
            print("File", ex.file)
        elif isinstance(ex, TransformationError):
            print("Exception", ex.message)
            print("File", ex.file)
        else:
            print("Exception", ex.message)
        return False

    return True

# Generated at 2022-06-22 12:26:01.612382
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .utils.unittest import assert_compilation_result_equal

# Generated at 2022-06-22 12:26:09.184273
# Unit test for function compile_files
def test_compile_files():
    input_ = 'test/test_files/test.py'
    output = 'test/test_files/out.py'
    result = compile_files(input_, output, CompilationTarget.RUNTIME)
    expected = CompilationResult(1, 15.060352, CompilationTarget.RUNTIME, [])
    assert result.count == expected.count
    assert abs(result.time - expected.time) < 0.00001
    assert result.target == expected.target
    assert result.dependencies == expected.dependencies



# Generated at 2022-06-22 12:26:19.386086
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import os
    import shutil

    input_ = './test/test_1'
    output = './test/compiled'
    target = CompilationTarget.COMPATIBLE

    shutil.rmtree(output) # перед тестом удалить папку
    res = compile_files(input_, output, target)

    assert res.count == 2, 'Error in test compiled'
    assert res.duration > 0, 'Error in test duration'
    assert res.target == target, 'Error in test target'
    assert os.path.isfile(os.path.join(output, 'test1.py')), 'Not found file test1.py'

# Generated at 2022-06-22 12:26:26.417408
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationResult
    from .types import CompilationTarget as T
    from .files import get_input_output_paths
    from .utils.helpers import temp_directory

    with temp_directory() as tmp:
        res = compile_files('{}/input'.format(tmp),
                            '{}/output'.format(tmp), T.py_to_js)
        assert len(res.dependencies) == len(set(res.dependencies))



# Generated at 2022-06-22 12:26:37.838500
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    import shutil

    input_dir = tempfile.mkdtemp()
    output_dir = tempfile.mkdtemp()
    with open(os.path.join(input_dir, 'file.py'), 'w') as f:
        f.write('a = 1\nb = 2\nprint(a * b * 3)')
    with open(os.path.join(output_dir, 'file.py'), 'w') as f:
        f.write('a = 1\nb = 2\nprint(a * b * 3)')

    result = compile_files(input_dir, output_dir, CompilationTarget.python)
    assert os.path.isfile(os.path.join(output_dir, 'file.py'))
    assert result.count == 1
    assert result

# Generated at 2022-06-22 12:26:49.624503
# Unit test for function compile_files
def test_compile_files():
    import os, sys
    import shutil, tempfile
    import time

    from .import kores as kores
    from .utils.config import Config, ConfigOption

    # Remove temporary directory and it's contents
    def clean_tmp(tmpdir):
        shutil.rmtree(tmpdir)

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Copy one of the example packs
    os.system('cp -r ../examples/js {}'.format(tmpdir))

    # Create config
    config = Config()

    # Compile the example pack

# Generated at 2022-06-22 12:26:50.670543
# Unit test for function compile_files
def test_compile_files():
    # TODO: implement
    pass

# Generated at 2022-06-22 12:26:53.195038
# Unit test for function compile_files
def test_compile_files():
    import json
    import shutil
    import tempfile

# Generated at 2022-06-22 12:26:59.941889
# Unit test for function compile_files
def test_compile_files():
    import pytest
    input_ = 'sample_data/compiled'
    output = 'output'
    root = None
    assert compile_files(input_, output, CompilationTarget.python, root)

# Generated at 2022-06-22 12:27:08.182610
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os
    import os.path

    import autopep8
    from transformer.transformers import transformers
    from transformer.types import CompilationTarget, CompilationResult
    from transformer.exceptions import CompilationError, TransformationError
    from transformer.files import get_input_output_paths, InputOutput


# Generated at 2022-06-22 12:27:19.300532
# Unit test for function compile_files
def test_compile_files():

    def compile_files_(input_: str, output: str, target: CompilationTarget,
                       root: Optional[str] = None) -> str:
        """Compiles all files from input_ to output."""
        for paths in get_input_output_paths(input_, output, root):
            with paths.input.open() as f:
                code = f.read()
            transformed, _ = _transform(paths.input.as_posix(),
                                        code, target)
            return transformed

    def check_compile_files(input_: str, output: str, target: CompilationTarget,
                            root: Optional[str] = None,
                            expected: Optional[str] = None) -> None:
        """Compiles all files from input_ to output and checks it."""
        if expected is None:
            expected

# Generated at 2022-06-22 12:27:26.258140
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import pytest
    from .utils.helpers import chdir_to_test_root

    with chdir_to_test_root():
        res = compile_files('input/', 'output/', CompilationTarget.ES5)
        assert res.dependencies == [
            '@babel/runtime'
        ]
        assert 'async' not in (Path('output/test1.js') / 'main.js').read_text()
        assert 'async' in (Path('output/test2.js') / 'main.js').read_text()
        assert 'async' not in (Path('output/test3.js') / 'main.js').read_text()


# Generated at 2022-06-22 12:27:32.203285
# Unit test for function compile_files
def test_compile_files():
    from .utils.tempdirs import TemporaryDirs

    tempdir = TemporaryDirs()
    tempdir['input/file_a.py'] = b'''# @py_to_c.wont_translate
import file_b
print(file_b.add(1, 2))
'''

# Generated at 2022-06-22 12:27:37.313880
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('.', '.', CompilationTarget.view).count == 1
    assert compile_files('.', '.', CompilationTarget.view_inline).count == 1
    assert compile_files('.', '.', CompilationTarget.notebook).count == 1
    assert compile_files('.', '.', CompilationTarget.python).count == 1



# Generated at 2022-06-22 12:27:40.010330
# Unit test for function compile_files
def test_compile_files():
    from .test.fixtures import test_dir
    compile_files(test_dir, os.path.join(test_dir, 'build'),
                  CompilationTarget.WEB, ".")

# Generated at 2022-06-22 12:27:49.640598
# Unit test for function compile_files
def test_compile_files():
    from .test_utils import (
        create_input_file,
        create_input_folder,
        get_input_file_content,
        get_output_file_content,
        remove_input_folder,
        remove_output_folder
    )

    input_ = 'inputs/'
    output = 'outputs/'
    root = 'root/'

    create_input_folder()
    create_input_file('a.py', 'import a')
    create_input_file('b.py', 'import b')
    create_input_file('m.py', 'import m')
    create_input_file('n.py', 'import n')
    create_input_file('p.py', 'import p')

    compile_files(input_, output, CompilationTarget.WEB, root)

   

# Generated at 2022-06-22 12:27:57.472667
# Unit test for function compile_files
def test_compile_files():
    dir_name = 'test_compile_files'
    input_dir = Path(dir_name) / 'input'
    output_dir = Path(dir_name) / 'output'
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    assert compile_files(input_dir, output_dir, CompilationTarget.COMPILE)


if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:27:59.835171
# Unit test for function compile_files
def test_compile_files():
    compile_files(input_ = 'input_',
                  output = 'output',
                  target = CompilationTarget.PYTHON27)

# Generated at 2022-06-22 12:28:08.252205
# Unit test for function compile_files
def test_compile_files():
    paths = get_input_output_paths('tests/test_data', 'tests/test_data')
    assert([(p.input, p.output) for p in paths] == [
        ('tests/test_data/configs.py', 'tests/test_data/configs.json'),
        ('tests/test_data/main.py', 'tests/test_data/main.js')
    ])
    compile_files('tests/test_data', 'tests/test_data', CompilationTarget.JS)


# Generated at 2022-06-22 12:28:14.692673
# Unit test for function compile_files
def test_compile_files():
    from .files import get_input_output_paths
    from .transformers.literals import _transform
    import tempfile

    with tempfile.TemporaryDirectory() as path:
        result = compile_files(
            input_=path + '/input',
            output=path + '/output',
            target=CompilationTarget.PYTHON
        )
        assert result.count == 0 and result.time == 0

# Generated at 2022-06-22 12:28:15.359168
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:28:24.630458
# Unit test for function compile_files
def test_compile_files():
    import os.path
    input_ = os.path.join(os.path.dirname(__file__), '..', 'tests')
    output = os.path.join(os.path.dirname(__file__), '..', '__pycache__')
    result = compile_files(input_, output, CompilationTarget.PYTHON2,
                           os.path.join(os.path.dirname(__file__), '..'))
    assert result.count == 8
    assert 'typing' in result.dependencies
    assert 'typing_extensions' in result.dependencies
    assert 'mock' in result.dependencies

# Generated at 2022-06-22 12:28:31.033103
# Unit test for function compile_files
def test_compile_files():
    import os, sys
    import pytest
    from pathlib import Path
    from compile import get_output_path, get_input_output_paths
    from compile import compile_files, CompilationResult
    from compile.transformers import transformers
    from compile.types import CompilationTarget
    from compile.utils.helpers import debug
    from compile.exceptions import TransformationError
    from compile.files import discover_files

    def test_helper(inputs: List[str], exclude: List[str], output: str,
                    target: CompilationTarget, dependencies: List[str],
                    source: bool = False, fail: Optional[Exception]=None):
        test_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        input_dir = test_dir / inputs[0]
        output_dir

# Generated at 2022-06-22 12:28:39.268341
# Unit test for function compile_files
def test_compile_files():
    from .utils import project_root
    import pathlib

    count, duration, target, dependencies = compile_files(
        str(pathlib.Path(project_root, 'tests', 'example_files').resolve()),
        str(pathlib.Path(project_root, 'tests', 'C', 'out').resolve()),
        CompilationTarget.C)

    assert count == 3
    assert target == CompilationTarget.C
    assert set(dependencies) == set(['math', 'ctype', 'Ovski_vector'])

# Generated at 2022-06-22 12:28:41.087591
# Unit test for function compile_files
def test_compile_files():
    from .test.utils import create_test_environment
    create_test_environment()



# Generated at 2022-06-22 12:28:52.631307
# Unit test for function compile_files
def test_compile_files():
    code = """
    import math
    import random

    x = [1, 2, 3]
    y = []
    for x in x:
        y.append(x**2)
    """

    class CustomTransformer(object):
        target = CompilationTarget.UNIT_TEST

        def __init__(self):
            self.transform_calls = 0

        def transform(self, tree: ast.AST) -> ast.AST:
            self.transform_calls += 1
            return tree

    transformer = CustomTransformer()
    transformers.append(transformer)
    compile_files('test_compile_files', 'test_compile_files',
                  CompilationTarget.UNIT_TEST)
    # (2 + 3) * 2 == 10
    assert transformer.transform_calls == 10

    del transform

# Generated at 2022-06-22 12:28:53.253787
# Unit test for function compile_files
def test_compile_files():
    assert False

# Generated at 2022-06-22 12:29:05.169364
# Unit test for function compile_files
def test_compile_files():
    import astunparse
    import inspect
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # checks if the code string is valid python code
    def is_valid_code(code: str) -> bool:
        try:
            # checks if code is valid python code,
            # ignores any syntax errors
            tree = ast.parse(code)
            astunparse.unparse(tree)
        except SyntaxError:
            return False
        return True

    # checks if a path contains a file
    def is_file(path: str) -> bool:
        return Path(path).is_file()

    # creates a temporary directory and a function that cleans it up
    with TemporaryDirectory() as tmp_path:
        def cleanup():
            from shutil import rmtree
            rmtree(tmp_path)

        # read the