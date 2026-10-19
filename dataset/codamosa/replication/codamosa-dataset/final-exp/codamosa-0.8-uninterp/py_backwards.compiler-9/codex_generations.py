

# Generated at 2022-06-22 12:24:38.585815
# Unit test for function compile_files
def test_compile_files():
    from .tests.helpers import clean_dir, get_test_dirs
    from .tests.helpers import get_test_code

    for target in CompilationTarget:
        for input_, output in get_test_dirs(target):
            clean_dir(output)
            compile_files(input_, output, target, input_)

            for path in get_test_code(input_):
                with path.open() as f:
                    code = f.read()
                    assert compile(code, path.as_posix(), 'exec')
                    assert eval(compile(code, path.as_posix(), 'eval'))

# Generated at 2022-06-22 12:24:50.581968
# Unit test for function compile_files
def test_compile_files():
    import logging
    import os
    import shutil
    import tempfile
    import unittest

    class ModuleTestCase(unittest.TestCase):
        def setUp(self):
            # Set up fake input directories
            self.temp_root = tempfile.mkdtemp()
            os.makedirs(os.path.join(self.temp_root,
                                     "fake_nested_input",
                                     "fake_nested_input2"))


# Generated at 2022-06-22 12:24:56.072429
# Unit test for function compile_files
def test_compile_files():
    input_ = 'test/input/'
    output = 'test/output/'
    root = input_
    result = compile_files(input_, output, CompilationTarget.ES5, root)
    assert result.count == 1
    assert result.target == CompilationTarget.ES5
    assert result.dependencies == ['camelCase', 'kotlin.js', 'kotlinx.html', 'kotlinx.serialization']

# Generated at 2022-06-22 12:25:07.203914
# Unit test for function compile_files
def test_compile_files():
    """Tests that compilation results in the same files."""
    import os
    import shutil

    from .exceptions import CompilationError
    from .utils.helpers import debug
    from .types import CompilationTarget

    from .files import get_input_output_paths

    from .transformers import transformers

    test_directory = os.path.join(os.path.dirname(__file__), 'test')
    input_ = os.path.join(test_directory, 'test_in')
    output = os.path.join(test_directory, 'test_out')
    for paths in get_input_output_paths(input_, output):
        shutil.copy(paths.input.as_posix(), paths.output.as_posix())

    def check_result(result):
        assert result.count

# Generated at 2022-06-22 12:25:12.094490
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from tempfile import TemporaryDirectory
    from .test.fixtures import dummy_file, test_file, assert_compiled_with


# Generated at 2022-06-22 12:25:20.122927
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    from pathlib import Path
    from .types import CompilationTarget

    input_ = tempfile.mkdtemp()
    output = tempfile.mkdtemp()
    input_path = Path(input_)
    output_path = Path(output)
    input_path.joinpath('index.html').write_text('<body>Hello, world!</body>')
    input_path.joinpath('index.py').write_text('print("Hello, world!")')
    input_path.joinpath('config.json').write_text('{"Hello": "World"}')
    input_path.joinpath('config.json.sample').write_text('{"Hello": "World"}')
    input_path.joinpath('error.py').write_text('hello world')


# Generated at 2022-06-22 12:25:26.015485
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('compilation/test/input', 'compilation/test/output', CompilationTarget.TO_PY3)
    assert result.compiled_files == 1
    assert result.compilation_target == CompilationTarget.TO_PY3
    assert result.compilation_time > 0
    assert result.dependencies == ['compilation/test/input/user.py', 'email']
    assert result.compiled_files == 1

# Generated at 2022-06-22 12:25:32.770516
# Unit test for function compile_files
def test_compile_files():
    """Tests compile_files."""
    assert compile_files('experiments/data/file.py',
                         'experiments/data/tests/output',
                         CompilationTarget.JS) == CompilationResult(1, 0.009984493255615234,
                         CompilationTarget.JS, ['__all__ = ["class_var", "func", "variable_only_set", "variable_set_and_get"]'])

# Generated at 2022-06-22 12:25:37.278913
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/hello_world', 'bin/hello_world', CompilationTarget.DECO)
    assert result.count == 1
    assert result.target == CompilationTarget.DECO
    assert result.time > 0
    assert result.dependencies == ['deco']


# Generated at 2022-06-22 12:25:42.537893
# Unit test for function compile_files
def test_compile_files():
    # This is not a unit test, just a simple example
    result = compile_files('tests/input', 'tests/output', CompilationTarget.ES6)
    assert result.target == CompilationTarget.ES6, 'Target should be ES6'
    assert result.files_compiled == 1, 'One file compiled'
    assert result.dependencies == ['pyramid'], 'One dependency should be found'



# Generated at 2022-06-22 12:25:58.547678
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import os
    import shutil
    import unittest.mock

    class TestCompilationResult(unittest.TestCase):
        def setUp(self):
            self._tmpdir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self._tmpdir)

        def test_single_file(self):
            input_ = os.path.join(self._tmpdir, 'in')
            os.makedirs(os.path.join(input_, 'subdir'))
            output = os.path.join(self._tmpdir, 'out')


# Generated at 2022-06-22 12:26:07.365492
# Unit test for function compile_files
def test_compile_files():
    #! pytype: disable=module-attr
    if __name__ == '__main__':
        print('Compilation times:\n')
        for target in [CompilationTarget.VANILLA, CompilationTarget.CPYTHON]:
            result = compile_files(
                Path('tests/data/simple_example/simple_example.py'),
                Path('build/simple_example/simple_example.py'), target)
            print('  {}:'.format(target), result.time)

    #! pytype: enable=module-attr

# Generated at 2022-06-22 12:26:13.691530
# Unit test for function compile_files
def test_compile_files():
    input_ = 'tests/test_data/compile_files/input'
    output = 'tests/test_data/compile_files/output'
    compiled = compile_files(input_, output,
                             CompilationTarget.PY2)
    assert compiled.count == 3
    assert compiled.dependencies == []
    assert compiled.target == CompilationTarget.PY2

# Generated at 2022-06-22 12:26:17.135052
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/samples', 'tests/samples/output',
            CompilationTarget.TARGET_2)
    assert result.files == 3
    assert result.time_taken < 0.01

# Generated at 2022-06-22 12:26:22.482132
# Unit test for function compile_files
def test_compile_files():
    input_dir = Path('./test/input')
    output_dir = Path('./test/output') 
    root_dir = Path('/')
    assert compile_files(input_dir,output_dir, CompilationTarget.NODEJS, root_dir)

if __name__ == "__main__":
    test_compile_files()

# Generated at 2022-06-22 12:26:29.133602
# Unit test for function compile_files
def test_compile_files():
    code = """
    def sum(a: int, b: int) -> int:
        return a + b
    """
    result = compile_files('/path/to/file.py', '/path/to/output',
                           CompilationTarget.PYTHON_2)
    assert result.count == 1
    assert result.target == CompilationTarget.PYTHON_2
    assert result.dependencies == []
    assert result.time_spent > 0

# Generated at 2022-06-22 12:26:31.714761
# Unit test for function compile_files
def test_compile_files():
    # TODO
    pass


# Generated at 2022-06-22 12:26:35.893956
# Unit test for function compile_files
def test_compile_files():
    import pytest
    import tempfile
    input_ = tempfile.mkdtemp()
    output = tempfile.mkdtemp()

# Generated at 2022-06-22 12:26:37.724944
# Unit test for function compile_files
def test_compile_files():
    from .tests import main
    main()

# Generated at 2022-06-22 12:26:49.523940
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import pytest
    import os

    session_dir = Path(os.getcwd()) / 'test_compile_files'
    session_dir.mkdir(parents=True, exist_ok=True)

    def test_file(input_, target, expected):
        output_path = session_dir / input_.name
        output_path.mkdir(parents=True, exist_ok=True)
        output_path = output_path.joinpath(input_.name).with_suffix('.py')

        result = compile_files(input_, output_path, target)
        output_path.unlink()

        if expected is None:
            pytest.xfail(reason='Expected compilation error')
        else:
            assert result.compiled == 1
            assert result.target == target

           

# Generated at 2022-06-22 12:27:10.813431
# Unit test for function compile_files
def test_compile_files():
    import pathlib
    import shutil
    import io
    import sys

    def test_results_equal(result1: CompilationResult, result2: CompilationResult):
        assert result1.duration == result2.duration
        assert result1.target == result2.target
        assert result1.count == result2.count
        assert result1.dependencies == result2.dependencies

    # Create and fill temporary directories
    if not pathlib.Path('tmp').is_dir():
        pathlib.Path('tmp').mkdir()
    else:
        shutil.rmtree('tmp')
        pathlib.Path('tmp').mkdir()

    if pathlib.Path('tmp2').is_dir():
        shutil.rmtree('tmp2')

# Generated at 2022-06-22 12:27:14.289018
# Unit test for function compile_files
def test_compile_files():
    from .test import test_compile_files as ftest
    ftest()

if __name__ == '__main__':
    # Entry point for the command line
    from .command import main
    main()

# Generated at 2022-06-22 12:27:14.888307
# Unit test for function compile_files
def test_compile_files(): ...

# Generated at 2022-06-22 12:27:18.733559
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/data/compile_file/input/', 'tests/data/compile_file/output/', 'py2') == CompilationResult(3, 0.0006549358367919922, 'py2', ['sys'])

# Generated at 2022-06-22 12:27:23.282037
# Unit test for function compile_files
def test_compile_files():
    from . import __file__ as module
    import os.path as op
    test_file = op.join(op.dirname(module), 'test', '__init__.py')
    out_dir = op.join(op.dirname(module), 'test', '__pycache__')
    result = compile_files(test_file, out_dir, CompilationTarget.py27)
    assert result.file_count == 3
    assert result.target == CompilationTarget.py27
    assert result.dependencies == []

# Generated at 2022-06-22 12:27:27.121464
# Unit test for function compile_files
def test_compile_files():
    input_ = 'test/test_files/test_compile_files/input'
    output = 'test/test_files/test_compile_files/output'

    compile_files(input_, output, CompilationTarget.ES6)

    # TODO: test the result



# Generated at 2022-06-22 12:27:28.868676
# Unit test for function compile_files
def test_compile_files():
    compile_files('test',
                  'test_output',
                  CompilationTarget.ES6)

# Generated at 2022-06-22 12:27:37.553949
# Unit test for function compile_files
def test_compile_files():
    from tempfile import TemporaryDirectory
    from .utils.helpers import mkdir_p

    with TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        mkdir_p(temp_dir / 'a' / 'b')
        (temp_dir / 'a' / 'b' / 'c.py').touch()
        (temp_dir / 'a' / 'c.py').touch()
        (temp_dir / 'x.py').touch()
        result = compile_files(temp_dir, temp_dir, CompilationTarget.PY33)
        assert result.count == 3

# Generated at 2022-06-22 12:27:43.116871
# Unit test for function compile_files
def test_compile_files():
    paths = get_input_output_paths(Path('tests/input'),
                                   Path('tests/output'),
                                   Path('tests').resolve())

    dependencies = set(_compile_file(paths[0], 0))
    print(dependencies)
    assert dependencies == {
        'tensorflow',
        'tensorflow-estimator',
    }

# Generated at 2022-06-22 12:27:54.385151
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationTarget

    input_ = '/tmp'
    output = '/tmp/test_output'
    target = CompilationTarget.JS
    root = None

    test_obj = compile_files(input_, output, target, root)
    expected_count = 0
    assert test_obj.count == expected_count

    test_obj = compile_files(input_, output, target, root)
    expected_minutes = 0
    assert test_obj.minutes == expected_minutes

    test_obj = compile_files(input_, output, target, root)
    expected_target = CompilationTarget.JS
    assert test_obj.target == expected_target

    test_obj = compile_files(input_, output, target, root)
    expected_dependencies = []