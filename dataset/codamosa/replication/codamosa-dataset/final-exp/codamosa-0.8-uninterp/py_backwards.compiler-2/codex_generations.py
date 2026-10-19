

# Generated at 2022-06-22 12:24:32.795811
# Unit test for function compile_files
def test_compile_files():
    compile_files()

# Generated at 2022-06-22 12:24:41.346950
# Unit test for function compile_files
def test_compile_files():
    input_ = 'input/'
    output = 'output/'
    target = 'uPython'
    root = 'root/'

    # Test 1
    assert compile_files(input_, output, target, root) == CompilationResult(5, 4.5, target, [])
    # Test 2
    assert compile_files(input_, output, target, None) == CompilationResult(5, 4.5, target, [])
    # Test 3
    assert compile_files(input_, output, target, root) == CompilationResult(5, 4.5, target, [])

# Generated at 2022-06-22 12:24:52.056349
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationResult
    num_files = 0
    total_time = 0
    target = 'PYTHON'
    deps = set()
    result = compile_files('tests/data/compile/input', 'tests/data/compile/output', target)
    num_files += result.num_files
    total_time += result.total_time
    target = result.target
    deps.update(result.dependencies)
    result = compile_files('tests/data/compile/input_sub', 'tests/data/compile/output_sub', target)
    num_files += result.num_files
    total_time += result.total_time
    target = result.target
    deps.update(result.dependencies)

# Generated at 2022-06-22 12:25:03.037156
# Unit test for function compile_files
def test_compile_files():
    import pytest

    from .tests.helpers import create_test_file, remove_test_file
    from .utils.helpers import unittest_aware

    f_in = create_test_file('in.py', 'print("Hello world")')

    @unittest_aware
    def test_with_root():
        f_out = create_test_file('out.py')
        result = compile_files(f_in, f_out, CompilationTarget.PY2,
                               root=f_in)
        assert result.count == 1
        assert result.target == CompilationTarget.PY2
        assert result.duration > 0
        assert result.dependencies == []
        remove_test_file(f_out)

    @unittest_aware
    def test_without_root():
        f_

# Generated at 2022-06-22 12:25:06.160796
# Unit test for function compile_files
def test_compile_files():
    import sys
    import tempfile

    tempdir = tempfile.mkdtemp()

    p = tempdir + "/input/a.py"

# Generated at 2022-06-22 12:25:15.767006
# Unit test for function compile_files
def test_compile_files():
    from os import remove
    from os.path import exists
    from tempfile import mkdtemp
    from .tests.test import test_compile_files as test
    input_ = mkdtemp()
    output = mkdtemp()
    result = compile_files(input_, output, CompilationTarget.JS)
    try:
        assert result.count == test.count
        assert result.dependencies == test.dependencies
        assert result.target == test.target
        assert exists(output + '/' + test.dependencies[0])
        assert exists(output + '/' + test.dependencies[1])
    finally:
        remove(input_ + '/' + test.dependencies[0])
        remove(input_ + '/' + test.dependencies[1])
        remove(output + '/' + test.dependencies[0])


# Generated at 2022-06-22 12:25:27.380745
# Unit test for function compile_files
def test_compile_files():
    from unittest.mock import Mock
    from tempfile import NamedTemporaryFile
    from os import remove
    from .files import get_input_output_paths
    from .exceptions import CompilationError, TransformationError
    from .utils.helpers import debug

    assert compile_files('/', '/', CompilationTarget.VANILLA) == CompilationResult(
        count=0, elapsed_time=0, target=CompilationTarget.VANILLA, dependencies=[])

    with NamedTemporaryFile(open=open) as tmp:
        tmp.write('\n')
        tmp.flush()
        assert compile_files(tmp.name, '/', CompilationTarget.VANILLA) == CompilationResult(
            count=1, elapsed_time=0, target=CompilationTarget.VANILLA, dependencies=[])

   

# Generated at 2022-06-22 12:25:39.016117
# Unit test for function compile_files
def test_compile_files():
    import hashlib
    import subprocess
    import shutil
    import os

    abs_path = os.path.dirname(os.path.abspath(__file__))
    in_path = abs_path + '/test_files/input/'
    out_path = abs_path + '/test_files/output/'

    if os.path.isdir(out_path):
        shutil.rmtree(out_path)

    compile_files(in_path, out_path, CompilationTarget.PY35)

    files = os.listdir(out_path)
    assert len(files) == 2

    filenames = [out_path + f for f in files]

# Generated at 2022-06-22 12:25:49.936727
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path

    def compare_file(path1: Path, path2: Path) -> None:
        with path1.open() as f:
            string1 = f.read()
        with path2.open() as f:
            string2 = f.read()
        assert string1 == string2

    input_ = Path(__file__).parent.joinpath('../test/test_compile_files/input/')
    output = Path(__file__).parent.joinpath('../test/test_compile_files/output/')
    root = Path(__file__).parent.joinpath('../test/test_compile_files/root/')

    compile_files(str(input_), str(output), CompilationTarget.PYTHON3)
    compare_file(input_, output)

    compile_

# Generated at 2022-06-22 12:25:59.138173
# Unit test for function compile_files
def test_compile_files():
    import subprocess
    import shutil

    def test_compile_files_inner(input_: str, output: str, target: CompilationTarget,
                  root: Optional[str] = None) -> str:
        input_path = os.path.join("tests", "compiler", "input", input_)
        output_path = os.path.join("tests", "compiler", "output", output)
        temp = os.path.join("tests", "compiler", "temp", output)
        os.makedirs(temp)
        compile_files(input_path, temp, target, root)
        output_content = subprocess.check_output(["diff", "-ur", output_path, temp]).decode()
        shutil.rmtree(temp)
        return output_content


# Generated at 2022-06-22 12:27:58.908142
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    import pytest
    from tempfile import mkdtemp

    root = mkdtemp()
    input_ = os.path.join(root, 'input')
    output = os.path.join(root, 'output')
    os.makedirs(input_)
    test_files_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'test_files')
    for file in os.listdir(test_files_path):
        if not file.endswith('.py'):
            continue


# Generated at 2022-06-22 12:28:10.889459
# Unit test for function compile_files
def test_compile_files():
    import unittest
    import tempfile
    import shutil
    from .exceptions import CompilationError, TransformationError
    from .types import CompilationTarget, CompilationResult
    from .files import get_input_output_paths
    from .transformers import apply_transforms
    from .utils import dir
    try:
        directory = dir()
    except ValueError:
        directory = tempfile.mkdtemp()
        print('Cannot get path to directory, compilation tests temporary directory was created at {}'.format(directory), end='\n')
    # add a file
    with open(dir()+'/file.py', 'w') as f:
        f.write('print("Hello, world!")')
    # add a file with error

# Generated at 2022-06-22 12:28:14.349891
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationTarget
    from .helpers import load_file
    from .utils.helpers import debug

    debug(True)
    compile_files("tests/fixtures/input/", "tests/fixtures/output/",
                  CompilationTarget.es5)
    assert load_file("tests/fixtures/output/tree.js") == load_file("tests/fixtures/expected/tree.js")

# Generated at 2022-06-22 12:28:19.524149
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/data/input',
                         'tests/data/output',
                         CompilationTarget.SCRIPT,
                         'mypy_boto3') ==\
                             CompilationResult(1, _, CompilationTarget.SCRIPT, ['botocore'])



# Generated at 2022-06-22 12:28:27.956037
# Unit test for function compile_files
def test_compile_files():
    from .utils import temp_directories
    from .exceptions import CompilationError
    from .utils.helpers import get_generics_path

    path = get_generics_path()
    with temp_directories() as (i, o):
        with path.joinpath('fixtures', 'generics.py').open() as f:
            with i.joinpath('file.py').open('w') as g:
                g.write(f.read())

        try:
            compile_files(i.as_posix(), o.as_posix(), CompilationTarget.ES5)
        except CompilationError:
            pass
        else:
            assert False

# Generated at 2022-06-22 12:28:28.472833
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:28:40.258976
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile

    from pathlib import Path

    from .utils.helpers import get_directory_name

    input_ = './tests/input'
    output = './tests/output'

    with tempfile.TemporaryDirectory() as dir:
        output = Path(dir)
        compile_files(input_, output.as_posix(), CompilationTarget.TYPES)

        assert os.path.isfile(os.path.join(output, '__init__.py'))
        assert os.path.isfile(os.path.join(output, 'main.py'))
        assert os.path.isfile(os.path.join(output, 'controllers', '__init__.py'))

# Generated at 2022-06-22 12:28:51.782397
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from .parser import parse
    from .transformers.imports import ImportResolver
    from .transformers.names import NameResolver
    from .transformers.symbols import SymbolResolver
    from .transformers.types import TypesResolver
    from .transformers.qualified_names import QualifiedNameResolver
    from .transformers.variables import VariableResolver
    from .transformers.references import ReferenceResolver
    from .transformers.calls import CallResolver
    from .transformers.references_visitor import ReferencesVisitor
    from .transformers.initialize import InitializeVisitor
    from .transformers.comments import CommentResolver
    from .transformers.visitors import Visitor
    from .transformers.output import OutputResolver
    from .transformers.deffered import DeferredResolver



# Generated at 2022-06-22 12:28:58.309866
# Unit test for function compile_files
def test_compile_files():
    pass

# Module testing
if __name__ == '__main__':
    import sys
    try:
        compile_files(*sys.argv[1:])
    except CompilationError as e:
        print('Compilation error:\n{}\n'.format(e.long))
        print(e.short)
        sys.exit(1)

__all__ = ['compile_files']

# Generated at 2022-06-22 12:28:58.923210
# Unit test for function compile_files
def test_compile_files():
    assert True