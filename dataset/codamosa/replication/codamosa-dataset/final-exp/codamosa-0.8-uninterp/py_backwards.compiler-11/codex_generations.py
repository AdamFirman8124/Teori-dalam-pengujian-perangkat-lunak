

# Generated at 2022-06-22 12:24:31.329163
# Unit test for function compile_files
def test_compile_files():
    from .exceptions import CompilationResult

    assert isinstance(compile_files('a', 'b', CompilationTarget.DEVELOPMENT),
                      CompilationResult)

# Generated at 2022-06-22 12:24:34.693768
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/inputs',
                         'tests/outputs',
                         CompilationTarget.BROWSER) == CompilationResult(9, 0, CompilationTarget.BROWSER,
                                                                         ['io'])

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:24:44.902230
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import os
    import pytest
    import subprocess

    TARGET = CompilationTarget.CPYTHON

# Generated at 2022-06-22 12:24:53.186165
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .files import get_input_output_paths
    from .types import CompilationTarget

    input_ = Path('test/compiler/input')
    output = Path('test/compiler/output')
    root = Path('test/compiler')

    target = CompilationTarget.PYTHON

    assert _compile_file(paths=get_input_output_paths(input_, output, root).__next__(), target=target) == []

# Generated at 2022-06-22 12:24:55.614187
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/integration/ant/data',
                  'tests/integration/ant/compiled',
                  CompilationTarget.PYTHON3)

# Generated at 2022-06-22 12:24:56.217098
# Unit test for function compile_files
def test_compile_files():
    assert 0 == 1

# Generated at 2022-06-22 12:25:04.961481
# Unit test for function compile_files
def test_compile_files():
    """Tests compilation of files."""
    result = compile_files(
        input_='test/fixtures/test-project/src',
        output='test/test-output/test-project-compiled',
        root='test/fixtures/test-project'
    )
    assert result == CompilationResult(
        4, 0.0, CompilationTarget.ES5,
        ['test/fixtures/test-project/node_modules/foo-bar/bar.js',
         'test/fixtures/test-project/node_modules/goo-bac/baz.js']
    )

# Generated at 2022-06-22 12:25:06.390545
# Unit test for function compile_files

# Generated at 2022-06-22 12:25:11.280454
# Unit test for function compile_files
def test_compile_files():
    assert compile_files(
        input_='tests/res/input',
        output='tests/res/output',
        target=CompilationTarget.BEGINNER
    ) == CompilationResult(
        file_count=3,
        total_time=0.0,
        target=CompilationTarget.BEGINNER,
        dependencies=['unittest']
    )

# Generated at 2022-06-22 12:25:15.809053
# Unit test for function compile_files
def test_compile_files():
    RESULT = compile_files('samples', 'samples_out', CompilationTarget.STANDARD)
    assert RESULT.success == True
    assert RESULT.target == CompilationTarget.STANDARD
    assert len(RESULT.dependencies) == 1
    assert RESULT.dependencies[0] == 'debug_bar'

test_compile_files()

# Generated at 2022-06-22 12:25:24.099713
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os
    import functools
    temp_dir = tempfile.mkdtemp('src', 'temp')
    temp_dir_dst = tempfile.mkdtemp('dst', 'temp')

# Generated at 2022-06-22 12:25:31.543331
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from pathlib import Path
    import tempfile
    from .compilers import compile_files

    input_ = Path(__file__).parent / 'test_data'
    with tempfile.TemporaryDirectory() as tmpdir:
        output = Path(tmpdir)
        r = compile_files(input_, output, CompilationTarget.WEB)
        assert not r.dependencies

        assert not open(output / 'sources/nested/test2.py').read()
        assert open(output / 'sources/test.py').read() == open(input_ / 'sources/test.py').read()

# Generated at 2022-06-22 12:25:42.340983
# Unit test for function compile_files
def test_compile_files():
    class CompilationResult:
       """Unit test for function compile_files"""
       def __init__(self, file_count: int, time_elapsed: float, target: CompilationTarget, dependencies: List[str]):
           self.file_count = file_count
           self.time_elapsed = time_elapsed
           self.target = target
           self.dependencies = dependencies
    class CompilationTarget:
       """Unit test for function compile_files"""
       def __init__(self, language_version: str, is_executable: bool):
           self.language_version = language_version
           self.is_executable = is_executable
    class InputOutput:
        """Unit test for function compile_files"""
        def __init__(self, input_, output):
            self.input = input_
            self.output

# Generated at 2022-06-22 12:25:53.849865
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from os import path, remove
    from .__main__ import get_main_parser
    from .__main__ import main as py_main

    def main(input_, output, target):
        main_parser = get_main_parser()
        main_parser.output = output
        main_parser.target = target
        main_parser.input_ = input_
        main_parser.verbose = True
        main_parser.root = path.join(path.dirname(__file__), '..')
        py_main(main_parser)

    # No python code

# Generated at 2022-06-22 12:25:57.795988
# Unit test for function compile_files
def test_compile_files():
    test_input = Path('./tests/examples/number_list.py')
    test_output = Path('./tests/examples/number_list.js')

    compile_files(
        test_input,
        test_output,
        CompilationTarget.ES5)



# Generated at 2022-06-22 12:26:05.195707
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('test/test_data/test_compile/src', 
                           'test/test_data/test_compile/out', 
                           CompilationTarget.ES5)
    with open('test/test_data/test_compile/out/m.js', 'r') as f:
        assert f.read() == '"use strict";\n\nvar x = 1;\n\nvar y = 2;'

# Generated at 2022-06-22 12:26:14.011872
# Unit test for function compile_files
def test_compile_files():
    target = CompilationTarget.RPC

    input_ = Path(__file__).parent.joinpath('input')
    output = Path(__file__).parent.joinpath('output')
    output.joinpath('.keep').touch()

    result = compile_files(input_, output, target)

    assert result.count == 2
    assert result.target == target

    for file in output.iterdir():
        with file.open() as f:
            code = f.read()
        assert 'import six' not in code
        assert 'from six.moves.http_client import HTTPSConnection' in code
        assert 'from io import StringIO' in code
        assert 'from io import BytesIO' in code
        assert 'from six.moves.urllib.parse import urlencode' in code

# Generated at 2022-06-22 12:26:23.271257
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests', '.', CompilationTarget.PYTHON) == compile_files('tests', '.', CompilationTarget.PYTHON_TYPES)
    assert compile_files('tests', '.', CompilationTarget.NEPTUNE) == compile_files('tests', '.', CompilationTarget.NEPTUNE_TYPES)

    assert compile_files('tests', '.', CompilationTarget.PYTHON).count == compile_files('tests', '.', CompilationTarget.PYTHON_TYPES).count
    assert compile_files('tests', '.', CompilationTarget.NEPTUNE).count == compile_files('tests', '.', CompilationTarget.NEPTUNE_TYPES).count

# Generated at 2022-06-22 12:26:25.710981
# Unit test for function compile_files
def test_compile_files():
  assert compile_files("../docs/examples/input", "../docs/examples/output", CompilationTarget.CUBE) is None


# Generated at 2022-06-22 12:26:30.550567
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/fixtures/python', 'tests/fixtures/output', CompilationTarget.JS)
    compile_files('tests/fixtures/python', 'tests/fixtures/output', CompilationTarget.V8)
    compile_files('tests/fixtures/python', 'tests/fixtures/output', CompilationTarget.NODE)

# Generated at 2022-06-22 12:26:41.699342
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/stubs/compilation/input', 'tests/stubs/compilation/output', CompilationTarget.ES5)


# Generated at 2022-06-22 12:26:43.112778
# Unit test for function compile_files
def test_compile_files():
    compile_files('.', '.', 'transpile', '.')



# Generated at 2022-06-22 12:26:52.264601
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os

    i = tempfile.TemporaryDirectory()
    o = tempfile.TemporaryDirectory()

    in_file = os.path.join(i.name, "input.py")
    out_file = os.path.join(o.name, "output.py")

    with open(in_file, "w") as f:
        f.write("import numpy\nimport pandas\n")

    compile_files(os.path.join(i.name, "input.py"), os.path.join(o.name, "output.py"), CompilationTarget.to_exe)

    with open(out_file, "r") as f:
        assert f.read() == "import math\nimport numpy\nimport pandas\n\n\n"

    shut

# Generated at 2022-06-22 12:26:52.690614
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:26:57.282552
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/fixtures/input',
                           '/tmp/compiled',
                           CompilationTarget.PY27)
    assert result.dependencies == ['typing']
    assert result.target == CompilationTarget.PY27
    assert result.files_compiled == 1



# Generated at 2022-06-22 12:27:06.694236
# Unit test for function compile_files
def test_compile_files():
    from pytest import raises
    from .files import compile_file_with_init
    from .exceptions import CompilationError

    with compile_file_with_init('tests/resources/dunder_init.py') as dunder_init:
        with compile_file_with_init('tests/resources/no_dunder_init.py') as no_dunder_init:
            with compile_file_with_init('tests/resources/no_dunder_init_2.py') as no_dunder_init_2:
                compile_files(
                    dunder_init.input, dunder_init.output,
                    CompilationTarget.STAGE_1, root=dunder_init.root)


# Generated at 2022-06-22 12:27:09.180353
# Unit test for function compile_files

# Generated at 2022-06-22 12:27:13.574842
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('./tests/fixtures/dist_js', './tests/fixtures/dist_py', CompilationTarget.CLI)
    assert compile_files('./tests/fixtures/dist_js', './tests/fixtures/dist_py', CompilationTarget.WEB)

# Generated at 2022-06-22 12:27:25.015807
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationTarget, CompilationResult
    from .transformers import PythranTransformer
    from .pycompilation import compile_files
    from .tests import get_test_files, TEST_FILES_DIR, TEST_FILES_OUT

    assert TEST_FILES_DIR and TEST_FILES_OUT, 'Set TEST_FILES_DIR & TEST_FILES_OUT '\
                                              'variables to run this unit test'

    orig_transformers = deepcopy(transformers)
    transformers.append(PythranTransformer)

    for input_, output in get_test_files(TEST_FILES_DIR, TEST_FILES_OUT):
        result = compile_files(input_, output,
                               CompilationTarget.pythran,
                               input_.split('test-files')[0])

# Generated at 2022-06-22 12:27:34.288516
# Unit test for function compile_files
def test_compile_files():
    import os
    import subprocess

    # Setup
    proj_path = os.path.dirname(os.path.abspath(__file__))
    test_path = os.path.join(proj_path, "examples/unit_test/")
    input_path = os.path.join(test_path, "input/")
    output_path = os.path.join(test_path, "output/")
    expected_path = os.path.join(test_path, "expected/")
    # Compile
    compile_files(input_path, output_path, CompilationTarget.node)
    # Run tests
    for dirname, _, files in os.walk(output_path):
        for filename in files:
            if filename.endswith(".js"):
                output_file = os

# Generated at 2022-06-22 12:27:44.606518
# Unit test for function compile_files
def test_compile_files():
    import doctest
    failed, attempted = doctest.testmod()
    return not failed and attempted > 0

# Generated at 2022-06-22 12:27:52.176240
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import random
    import shutil
    import os
    import pytest

    @pytest.fixture
    def base_dir(tmpdir):
        # Fixture creates temporary directory structure with files
        # in `test_files`.
        BASE_DIR = tmpdir.mkdir('test_files')

        def subdir(path):
            path[0] = BASE_DIR
            return Path(os.path.join(*path))

        def write_file(path, content):
            with open(subdir(path), 'w') as f:
                f.write(content)

        write_file(['a.py'], '# This is file a.py')
        
        write_file(['b.pyi'], '# This is file b.pyi')
        

# Generated at 2022-06-22 12:27:57.105201
# Unit test for function compile_files
def test_compile_files():
    from .tests.compilation.data import path_to_tests_data
    print('Compilation test')
    print('Normal compilation')
    compile_files(path_to_tests_data('compilation/input'),
                  path_to_tests_data('compilation/output'),
                  CompilationTarget.PYTHON)
    print('Compilation with init file')
    compile_files(path_to_tests_data('compilation/root/input2'),
                  path_to_tests_data('compilation/root/output2'),
                  CompilationTarget.PYTHON,
                  path_to_tests_data('compilation/root/input2'))
    print('Compilation with init file empty')

# Generated at 2022-06-22 12:28:00.702483
# Unit test for function compile_files
def test_compile_files():
    input_ = Path('tests/files')
    output = Path('tests/files_out')
    compile_files(str(input_), str(output), CompilationTarget.ES5)
    assert output.exists()



# Generated at 2022-06-22 12:28:12.046387
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .types import CompilationResult

    result = compile_files('./tests/data/input/',
                           './tests/data/output/',
                           CompilationTarget.PY37)
    assert result == CompilationResult(13, 0.012721061706542969,
                                       CompilationTarget.PY37,
                                       ['dataset', 'dataset/steam'])
    assert Path('./tests/data/output/dataset/steam/reviews.py').exists()
    assert Path('./tests/data/output/dataset/steam/__init__.py').exists()
    assert Path('./tests/data/output/dataset/__init__.py').exists()

# Generated at 2022-06-22 12:28:21.226179
# Unit test for function compile_files
def test_compile_files():
    import pathlib
    import subprocess
    input_ = str(pathlib.Path(__file__).parent.parent.joinpath(
        'tests', 'data', 'compilation'))
    output = str(pathlib.Path(__file__).parent.parent.joinpath(
        'tmp', 'data', 'compilation'))
    target = CompilationTarget.runtime
    compile_files(input_, output, target)
    subprocess.call(['py.test', str(pathlib.Path(__file__).parent.parent.joinpath(
        'tmp', 'data', 'compilation'))])

# Generated at 2022-06-22 12:28:29.717191
# Unit test for function compile_files
def test_compile_files():
    import os
    import re
    import sys
    import unittest
    import tempfile
    import shutil

    class TestCompileFiles(unittest.TestCase):
        def setUp(self):
            self._tmp_path = tempfile.TemporaryDirectory().name
            self._input_path = os.path.join(self._tmp_path, 'input')
            self._output_path = os.path.join(self._tmp_path, 'output')
            self._root_path = os.path.join(self._tmp_path, 'root')
            self._old_working_dir = os.getcwd()

        def tearDown(self):
            shutil.rmtree(self._tmp_path)
            os.chdir(self._old_working_dir)


# Generated at 2022-06-22 12:28:41.274186
# Unit test for function compile_files
def test_compile_files():
    from .exceptions import CompilationError, TransformationError
    from .compiler import compile_files
    from .types import CompilationTarget

    def assert_compile(input_: str, output: str, target: CompilationTarget,
                       expected_output: str):
        compile_files(input_, output, target)
        with open(output) as f:
            code = f.read()
        assert code == expected_output

    assert_compile('tests/compiler/basic', 'tmp/compiler/basic/out',
                   CompilationTarget.DISTRIBUTION,
                   'def func():\n    return 1\n\ndef main():\n    pass\n\n')

# Generated at 2022-06-22 12:28:50.824814
# Unit test for function compile_files
def test_compile_files():
    import warnings
    warnings.warn(
        "test_compile_files() will be removed in the future",
        FutureWarning,
    )

    import datetime
    from .utils import test_data_dir
    input_ = str(test_data_dir / 'typing')
    output = str(test_data_dir / 'output' / 'typing')
    results = compile_files(input_, output, CompilationTarget.web)

    assert results.target == CompilationTarget.web
    assert results.count > 1
    assert results.duration > 0
    assert results.dependencies == []



# Generated at 2022-06-22 12:28:52.407703
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/files/inputs/', 'tests/files/outputs/', CompilationTarget.JS)