

# Generated at 2022-06-22 12:24:39.165078
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('testdata/particles', 'tests/data', CompilationTarget.PARALLEL)
    assert result.target == CompilationTarget.PARALLEL
    assert result.count == 5
    assert len(result.dependencies) == 1
    assert result.dependencies[0].endswith('pymachines/transformers/parallel.py')

# Generated at 2022-06-22 12:24:51.050541
# Unit test for function compile_files
def test_compile_files():
    from .utils.test_utils import get_test_project_path, TEST_DATA_ROOT
    from .exceptions import CompilationError
    import os
    import pytest

    def compile_test(test_data_dir, required_globals, root=None):
        test_project_path = get_test_project_path(TEST_DATA_ROOT, test_data_dir)

        def get_expected_result_path(expected_result_file):
            return os.path.join(test_project_path, 'expected_result', expected_result_file)

        result = compile_files(os.path.join(test_project_path, 'input'),
                               os.path.join(test_project_path, 'output'),
                               CompilationTarget.PYTHON27, root=root)

# Generated at 2022-06-22 12:25:01.852559
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from os import remove
    import pytest

    # Create temporary files for testing
    tmp_input = Path('tmp_input').absolute()
    tmp_output = Path('tmp_output').absolute()
    tmp_input.mkdir(parents=True)
    tmp_output.mkdir(parents=True)
    with open(tmp_input / 'test.py', 'w') as f:
        f.write('def foo():\n    pass')
    with open(tmp_input / 'test2.py', 'w') as f:
        f.write('def bar():\n    pass')

    # Check that this compiles as expected
    result = compile_files(tmp_input.as_posix(), tmp_output.as_posix(),
                           CompilationTarget.PYTHON3, '')

# Generated at 2022-06-22 12:25:04.086955
# Unit test for function compile_files
def test_compile_files():
    """Compiles simple test file using compile_files."""
    # todo


# Generated at 2022-06-22 12:25:13.570880
# Unit test for function compile_files
def test_compile_files():
    import os
    import sys
    from modules.compile.tests.utils import run_test_case, TestCase
    from modules.compile.constants import DEFAULT_TARGET
    from modules.compile.exceptions import CompilationError
    from modules.compile.files import get_input_output_paths
    from modules.compile.transformers import test_transformer
    from .utils.helpers import root_path, temporary_directory

    with temporary_directory() as temp:
        paths = get_input_output_paths(root_path('tests', 'files'),
                                       temp,
                                       root_path('tests'))

        test_transformer.transform = lambda x: test_transformer.Result(True, ['transformer.py'])


# Generated at 2022-06-22 12:25:21.022121
# Unit test for function compile_files
def test_compile_files():
    paths = get_input_output_paths('test/test_input/',
                                   'test/test_output/',
                                   'test/',
                                   ['test/test_output/']) # Don't compile test_output
    assert len(paths) == 8
    assert _compile_file(paths[0], CompilationTarget.PY27) == ['test/test_input/d1/d2/d3/ut3.py']
    assert _compile_file(paths[1], CompilationTarget.PY33) == []
    assert _compile_file(paths[2], CompilationTarget.PY27) == ['test/test_input/d1/d2/d3/ut3.py', 'test/test_input/d3/u3.py']
    assert _compile

# Generated at 2022-06-22 12:25:33.410029
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from tempfile import mkdtemp
    import pytest
    from shutil import rmtree

    curr_dir = Path('tests').resolve()
    tmp = Path(mkdtemp())
    input_ = str(curr_dir.joinpath('data').resolve())
    output = str(tmp.resolve())

    with pytest.raises(FileNotFoundError):
        _ = compile_files('/etc/passwd', output, CompilationTarget.PYTHON)

    result = compile_files(input_, output, CompilationTarget.PYTHON)
    assert result.count == 6

    for n in range(1, 7):
        with open('{}/{}-expected.py'.format(input_, n)) as f:
            expected = f.readlines()



# Generated at 2022-06-22 12:25:43.626756
# Unit test for function compile_files
def test_compile_files():
    import shutil
    import tempfile

    tmp_dir = tempfile.mkdtemp(prefix='pyx_test')
    tmp_input = tmp_dir + '/input'
    tmp_output = tmp_dir + '/output'


# Generated at 2022-06-22 12:25:54.964878
# Unit test for function compile_files
def test_compile_files():
    import os
    import json
    import unittest
    from pathlib import Path
    from .utils.helpers import unique_name, remove_paths

    class TestCompileFiles(unittest.TestCase):
        def setUp(self):
            self.input_ = unique_name()
            self.output = unique_name()
            self.files = [('aa', 'bb'), ('cc', 'dd'), ('ee', 'ff')]
            for src, dst in self.files:
                Path(self.input_, src).write_text("""
                    c1
                    c2
                    c3
                    c4
                    c5
                    c6
                    c7
                    c8
                    c9
                """)
            self.root = unique_name()
            Path(self.root, 'tst.py').write

# Generated at 2022-06-22 12:26:01.353411
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os
    import sys
