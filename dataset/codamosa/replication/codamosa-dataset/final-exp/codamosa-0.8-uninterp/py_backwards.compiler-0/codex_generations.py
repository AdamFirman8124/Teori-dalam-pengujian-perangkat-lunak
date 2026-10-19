

# Generated at 2022-06-22 12:24:32.958710
# Unit test for function compile_files
def test_compile_files():
    assert compile_files("tests/in", "tests/out", CompilationTarget.PY3).count == 6



# Generated at 2022-06-22 12:24:43.881568
# Unit test for function compile_files
def test_compile_files():
    from .files import write_temp_code
    from pathlib import Path
    import shutil
    temp_dir = Path('/tmp/test_compile_files')
    input_ = temp_dir / 'input'
    output = temp_dir / 'output'
    input_.mkdir(parents=True)
    input_file_name1 = temp_dir / 'input/test1.py'
    input_file_name2 = temp_dir / 'input/test2.py'

    input_file1 = write_temp_code(input_file_name1, '''
    def foo():
        print('hello')

    foo()
    ''')
    input_file2 = write_temp_code(input_file_name2,
                                  '''import test1; test1.foo()''')
    result = compile

# Generated at 2022-06-22 12:24:49.168093
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files"""
    import tempfile
    input = tempfile.TemporaryDirectory()
    output = tempfile.TemporaryDirectory()

# Generated at 2022-06-22 12:24:51.983634
# Unit test for function compile_files
def test_compile_files():
    return compile_files(
        input_='tests/input/',
        output='tests/output/',
        root='tests/root/',
        target=CompilationTarget.PYTHON_FOR_LOOP_REPLACEMENT)

# Generated at 2022-06-22 12:25:02.918713
# Unit test for function compile_files
def test_compile_files():
    from collections import namedtuple
    from .types import CompilationResult
    import unittest
    import os.path
    import shutil
    import sys

    class TestCompileFiles(unittest.TestCase):
        def setUp(self):
            """Only for unit testing. Creates src and dst directories.
            Also, it adds the paths to sys.path to import custom modules"""
            self.src = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../test/src/')
            self.dst = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../test/dst/')
            sys.path.append(self.src)
            sys.path.append(self.dst)
            shutil.r

# Generated at 2022-06-22 12:25:12.540976
# Unit test for function compile_files
def test_compile_files():
    # get_input_output_paths returns list of tuples (input, output)
    inputs = []
    outputs = []
    root = str('src')
    output = '.'
    for (path_in, path_out) in get_input_output_paths(root, output):
        inputs.append(path_in)
        outputs.append(path_out)

    # compile_files returns object CompilationResult
    compilation_result = compile_files(root, output, CompilationTarget.STANDALONE)

    # check(inputs)
    for path in inputs:
        assert os.path.isfile(os.path.join(path)), 'File doesnt exist'

    # check(outputs)

# Generated at 2022-06-22 12:25:20.406893
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from shutil import rmtree
    from os import remove
    from .exceptions import CompilationError

    # Simple test
    input_ = Path(__file__).resolve().parent.joinpath('..', 'data', 'input',
                                                      'simple').resolve()
    output = Path(__file__).resolve().parent.joinpath('..', 'data', 'output').resolve()

    compile_files(input_, output, CompilationTarget.PY2)
    assert output.joinpath('simple.py').exists()
    assert output.joinpath('__init__.py').exists()

    # Error test: no such file
    input_ = 'fake_dir_name'

# Generated at 2022-06-22 12:25:23.040699
# Unit test for function compile_files
def test_compile_files():
    assert compile_files("tests/data/test_files/input/", "tests/data/test_files/output/", "target")

if __name__ == "__main__":
    test_compile_files()

# Generated at 2022-06-22 12:25:33.355471
# Unit test for function compile_files
def test_compile_files():
    out_files_1 = compile_files("./tests/test_input", "./tests/test_output", CompilationTarget.JS)
    out_files_2 = compile_files("./tests/test_input", "./tests/test_output", CompilationTarget.ES5)
    out_files_3 = compile_files("./tests/test_input", "./tests/test_output", CompilationTarget.ES3)
    assert out_files_1.num_success_files == 1
    assert out_files_2.num_success_files == 1
    assert out_files_3.num_success_files == 1

# Generated at 2022-06-22 12:25:35.317228
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/input/', 'tests/output/', 'py2')



# Generated at 2022-06-22 12:25:40.153950
# Unit test for function compile_files
def test_compile_files():
    # TODO: write tests
    pass

# Generated at 2022-06-22 12:25:45.357194
# Unit test for function compile_files
def test_compile_files():
    # no error
    compile_files('examples/example_test', 'tmp', CompilationTarget.PY_27)
    # error
    try:
        compile_files('examples/error_test', 'tmp', CompilationTarget.PY_27)
    except:
        return True
    
    return False
    
if __name__ == '__main__':
    print(test_compile_files())

# Generated at 2022-06-22 12:25:49.108820
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('example', 'example', CompilationTarget.PYTHON)
    print(result)
    assert result.compiled == 3
    assert set(result.dependencies) == {'bar', 'foo'}


# Generated at 2022-06-22 12:25:59.266571
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import subprocess
    from .utils.test_helper import get_test_dir
    from .types import CompilationTarget
    from .tests.compile_files_test import compile_files_test as test_function

    # Uncomment the following line to see detailed debugging logs
    # debug.set_print(True)

    test_dir = get_test_dir(test_function.__name__)

    for code in test_dir.glob('*.py'):
        output = code.parent / (code.stem + '.out')  # type: Path
        if output.exists():
            compile_files(code, output.parent, CompilationTarget.PYTHON, str(test_dir))

# Generated at 2022-06-22 12:26:10.570516
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from random import choice, randint
    from string import ascii_lowercase
    from typing import Callable, List

    def random_string(length: int) -> str:
        return ''.join(choice(ascii_lowercase) for i in range(length))

    def random_int() -> int:
        return randint(0, 100)

    def random_code(length: int) -> str:
        code = []
        for i in range(length):
            if randint(0, 1):
                code.append(random_string(randint(1, 15)))
            else:
                code.append(str(random_int()))
        return ' '.join(code)


# Generated at 2022-06-22 12:26:21.170155
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    from pathlib import Path

    from .exceptions import TransformationError, CompilationError
    from .fixtures import get_fixture_path

    # Test files locations
    tmp = Path(tempfile.mkdtemp())
    input_ = get_fixture_path('files', 'input')
    output = tmp / 'output'

    # Compile
    result = compile_files(input_, output, CompilationTarget.PY32)

    # Check result
    assert result.count == 4
    assert result.target == CompilationTarget.PY32

    # Compile again, this time there should be no files
    result = compile_files(input_, output, CompilationTarget.PY32)

    # Check result
    assert result.count == 0
    assert result.target == CompilationTarget.PY32

   

# Generated at 2022-06-22 12:26:29.627519
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    test_root = os.path.join('tests', 'files')
    output = os.path.join(test_root, 'out')
    compile_files(os.path.join(test_root, 'src'), output,
                  CompilationTarget.PYTHON)
    shutil.rmtree(output)

    output = os.path.join(test_root, 'out')
    compile_files(os.path.join(test_root, 'src'), output,
                  CompilationTarget.SQLITE)
    shutil.rmtree(output)

# Generated at 2022-06-22 12:26:40.877501
# Unit test for function compile_files
def test_compile_files():
    import os
    import os.path
    import shutil

    test_dir = os.path.abspath('tests/unittests_storage')
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    input_dir = os.path.join(test_dir, 'input')
    output_dir = os.path.join(test_dir, 'output')

    # Create a test file
    os.makedirs(os.path.join(input_dir, 'test_dir'))

# Generated at 2022-06-22 12:26:52.385969
# Unit test for function compile_files
def test_compile_files():
    import pathlib
    import shutil
    import sys
    import tempfile

    this_directory = pathlib.Path(__file__).parent

    input_ = this_directory / 'test_files' / 'input'
    output = tempfile.TemporaryDirectory()
    result = compile_files(input_.as_posix(), output.name, CompilationTarget.AUTOSTRUCT)
    assert result.count == 7

    def verify(name: str):
        actual = (pathlib.Path(output.name) / name).read_text()
        expected = (this_directory / 'test_files' / 'expected' / name).read_text()
        assert actual == expected

    verify('api.py')
    verify('base.py')
    verify('storage.py')
    verify('test_base.py')

# Generated at 2022-06-22 12:26:53.255519
# Unit test for function compile_files
def test_compile_files():
    compile_files('../../test_data', './', CompilationTarget.RUNTIME)

# Generated at 2022-06-22 12:27:05.218805
# Unit test for function compile_files
def test_compile_files():
    compile_files("/tmp/python-project/src/simple.py","/tmp/python-project/target/python/simple.py",CompilationTarget.PYTHON)

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:27:15.595794
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    import shutil
    from .types import CompilationTarget

    input_file = os.path.join(os.path.dirname(__file__), '../test/fixtures/compile_files.py')
    output_dir = tempfile.mkdtemp('compile_files')
    try:
        result = compile_files(input_file, output_dir, CompilationTarget.PY2)
        assert result.count == 2
        assert result.target == CompilationTarget.PY2
        assert result.time > 0
        assert result.dependencies == ['typed_ast']
    finally:
        shutil.rmtree(output_dir)


# Generated at 2022-06-22 12:27:25.490444
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/data', 'tests/results/compile_files', CompilationTarget.PLAIN)
    assert result.count == 5
    assert result.target == CompilationTarget.PLAIN
    assert result.duration > 0
    assert result.dependencies == ['js2py.interpreter.Interpreter.run_script',
                                   'js2py.interpreter.Interpreter.transform_filter',
                                   'js2py.interpreter.Interpreter.transform_function',
                                   'js2py.interpreter.Interpreter.transform_getter',
                                   'js2py.interpreter.Interpreter.transform_setter']

# Generated at 2022-06-22 12:27:34.974715
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    from tempfile import mkdtemp

    input_ = os.path.join(os.path.dirname(__file__), 'tests')
    output = mkdtemp()


# Generated at 2022-06-22 12:27:42.197583
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from .files import collect_files

    with pytest.raises(ValueError):
        compile_files('/tmp/a/b/c', '/tmp/a/b', CompilationTarget.UNKNOWN)

    input_ = '/tmp/a/b/c'
    output = '/tmp/a/b'
    for input_file in collect_files(['test/data'], []):
        result = compile_files('test/data', '/tmp', CompilationTarget.PY2,
                               input_file)
        assert result.count == 1

# Generated at 2022-06-22 12:27:50.753084
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from shutil import rmtree
    from tempfile import mkdtemp

    input_path = Path(mkdtemp())
    output_path = Path(mkdtemp())

    input_path.joinpath('test.py').write_text('a = 3')
    compile_files(input_path, output_path, CompilationTarget.ES5)

    output_code = output_path.joinpath('test.js').read_text()
    assert output_code == "a = 3\n"

    input_path.joinpath('another.py').write_text('a = 3')
    result = compile_files(input_path, output_path,
                           CompilationTarget.ES5)
    assert result.count == 2

# Generated at 2022-06-22 12:27:59.500475
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    import pytest

    input_ = os.path.join('test', 'in')
    output = os.path.join('test', 'out')
    target = CompilationTarget.PYTHON
    shutil.rmtree(output, ignore_errors=True)

    result = compile_files(input_, output, target, input_)

    assert result.files_count == 6
    assert set(result.dependencies) == set(['c', 'd', 'e.py'])

    with pytest.raises(SystemExit) as e:
        compile_files(input_, output, target, input_)
        assert e.code == 2

# Generated at 2022-06-22 12:28:11.464173
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import shutil
    import tempfile
    import pytest

    root_ = tempfile.mkdtemp()
    input_ = Path(root_) / 'src'
    input_.mkdir()
    (input_ / 'a.py').write_text('x = "3"')
    (input_ / 'b.py').write_text('x = 3')
    (input_ / 'c.py').write_text('x = 3')

    result = compile_files(
        input_.as_posix(),
        tempfile.mkdtemp(),
        CompilationTarget.THREE,
        root=root_
    )

    assert result.count == 3


# Generated at 2022-06-22 12:28:23.001666
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil

    def create_file(dir_: str, name: str, code: str) -> None:
        import os
        with open(os.path.join(dir_, name), "w") as f:
            f.write(code)

    temp_path = tempfile.mkdtemp()
    create_file(temp_path, "main.c",
    r'''
    #include <stdio.h>

    int main(void)
    {
        printf("Hello world!\n");
        return 0;
    }
    ''')
    result = compile_files(temp_path, temp_path, CompilationTarget.C)

    shutil.rmtree(temp_path)

    assert result.count == 1
    assert "stdio.h" in result.dependencies

# Generated at 2022-06-22 12:28:25.442577
# Unit test for function compile_files
def test_compile_files():
    for paths in get_input_output_paths('tests/data', '/tmp'):
        _compile_file(paths, CompilationTarget.ANY)