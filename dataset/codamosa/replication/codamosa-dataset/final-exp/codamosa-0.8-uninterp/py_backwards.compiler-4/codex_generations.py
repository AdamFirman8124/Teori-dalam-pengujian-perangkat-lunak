

# Generated at 2022-06-22 12:24:43.928556
# Unit test for function compile_files
def test_compile_files():
    from .utils.fake_package import create_fake_package
    from .types import CompilationTarget
    import os
    import shutil
    input_, output = '.tmp_input', '.tmp_output'
    try:
        with create_fake_package(input_):
            compile_files(input_, output, CompilationTarget.dev)
            # Check that file "pkg/__init__.py" was created
            assert os.path.exists(os.path.join(output, 'pkg',
                                               '__init__.py'))
    finally:
        shutil.rmtree(input_)
        shutil.rmtree(output)



# Generated at 2022-06-22 12:24:53.535128
# Unit test for function compile_files
def test_compile_files():
    import json
    import pathlib
    import subprocess
    from .exceptions import CompilationError
    from itertools import product
    from .files import get_input_output_paths, InputOutput
    from .transformers import transformers
    from .types import CompilationTarget

    input_ = pathlib.Path(__file__).parent / 'data' / 'input'
    output = pathlib.Path(__file__).parent / 'data' / 'output'
    root = pathlib.Path(__file__).parent

    if input_.exists():
        input_.unlink()
    if output.exists():
        output.unlink()

    subprocess.check_call(['virtualenv', '-p', 'python3', 'tmp/env'])

# Generated at 2022-06-22 12:25:04.320928
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationTarget, CompilationResult
    from .utils.helpers import remove_test_dir_content
    from .utils.test_constants import TEST_INPUT_PATH, TEST_OUTPUT_PATH, TEST_ROOT_PATH
    from pprint import pprint as pp

    remove_test_dir_content()

    res = compile_files(TEST_INPUT_PATH, TEST_OUTPUT_PATH, CompilationTarget.ES6, TEST_ROOT_PATH)
    assert isinstance(res, CompilationResult)
    assert res.count == 4
    assert res.target == CompilationTarget.ES6

# Generated at 2022-06-22 12:25:05.224735
# Unit test for function compile_files
def test_compile_files():
    pass



# Generated at 2022-06-22 12:25:08.013612
# Unit test for function compile_files
def test_compile_files():
    compile_files('tests/files/test_from', 'tests/files/test_to', CompilationTarget.PY2)

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:25:11.866298
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('tests/data', 'output', CompilationTarget.PYTHON_3)
    assert result.count == 8
    assert result.target == CompilationTarget.PYTHON_3
    assert result.time > 0



# Generated at 2022-06-22 12:25:19.972880
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path

    from .types import CompilationResult

    res = compile_files(Path(__file__).parent/'tests'/'input',
                        Path(__file__).parent/'tests'/'output',
                        CompilationTarget.ES5)

    assert res == CompilationResult(19, 0, CompilationTarget.ES5, ['foo'])
    assert (Path(__file__).parent/'tests'/'output'/'index.js').read_text() == (
        '// This is my comment\n'
        '(function (foo) {\n'
        '    \'use strict\';\n'
        '    console.log(foo);\n'
        '})(\'foo\');\n'
    )



# Generated at 2022-06-22 12:25:32.219434
# Unit test for function compile_files
def test_compile_files():
    import os, shutil
    import tempfile
    assert compile_files(
        os.path.join(os.path.dirname(__file__), 'test_data', 'compile', 'input'),
        os.path.join(os.path.dirname(__file__), 'test_data', 'compile', 'output'),
        CompilationTarget.CPP,
        os.path.join(os.path.dirname(__file__), 'test_data')
    ) == CompilationResult(4, 0.0, CompilationTarget.CPP, [])


# Generated at 2022-06-22 12:25:41.585662
# Unit test for function compile_files
def test_compile_files():
    import os
    import tempfile
    input_ = 'test_data/test_compile_files'
    output = tempfile.mkdtemp()
    os.mkdir(os.path.join(output, 'test_compile_files'))
    result = compile_files(input_, output, CompilationTarget.PYTHON)
    assert result.count == 2
    with open(os.path.join(output, 'test_compile_files', 'simple.repy')) as f:
        assert f.read() == 'def foo():\n    return True\n'
    assert result.target == CompilationTarget.PYTHON
    assert result.dependencies == ['mccabe', 'typed-ast']

# Generated at 2022-06-22 12:25:53.000393
# Unit test for function compile_files
def test_compile_files():
    import os
    # import shutil
    import sys
    import unittest
    import subprocess
    from pathlib import Path
    from .exceptions import CompilationError
    from . import targets
    from .utils.helpers import temp_dir
    from .utils.logging import enable_debug

    enable_debug()

    # pylint: disable=no-member

    # pylint: disable=missing-docstring
    class Test(unittest.TestCase):
        @temp_dir(__name__)
        def test_success(self, tempdir: Path):
            sample = input_ = tempdir / 'sample'
            sample.mkdir()
            for name in ('foo', 'bar', 'baz'):
                (sample / name).write_text('print("{}")'.format(name))
            output

# Generated at 2022-06-22 12:26:04.713179
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/data/input', 'output', CompilationTarget.BROWSER) == CompilationResult(3, 30)
    assert compile_files('tests/data/input', 'output', CompilationTarget.BROWSER) == CompilationResult(0, 1)

# Generated at 2022-06-22 12:26:07.957538
# Unit test for function compile_files
def test_compile_files():
    # Just make sure that it's working
    compile_files('tests/input', 'tests/output', CompilationTarget.PYTHON2)

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:26:13.788551
# Unit test for function compile_files
def test_compile_files():
    def test(target):
        try:
            compile_files('tests/files/src', 'tests/files/dst', target)
        except CompilationError as e:
            raise AssertionError(e)

    test(CompilationTarget.PYTHON2)
    test(CompilationTarget.PYTHON3)

# Generated at 2022-06-22 12:26:24.842304
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil

    input_ = 'tests/stubs'
    output = 'tests/tmp'
    target = CompilationTarget.PY3

    shutil.rmtree(output, ignore_errors=True)
    compile_files(input_, output, target)
    with open(output + '/__init__.py', 'r') as f:
        assert f.read() == ''

    for entry in os.scandir(input_):
        if entry.is_file() and not entry.name.startswith('__'):
            with open(entry.path, 'r') as f:
                input_code = f.read()
            with open(output + '/' + entry.name, 'r') as f:
                output_code = f.read()
            assert input_code != output_code

# Generated at 2022-06-22 12:26:30.489378
# Unit test for function compile_files
def test_compile_files():
    assert len(compile_files('test', '/tmp/test', CompilationTarget.PYTHON).dependencies) == 3
    assert compile_files('test', '/tmp/test', CompilationTarget.PYTHON).count == 3
    assert compile_files('test', '/tmp/test', CompilationTarget.PYTHON).target == CompilationTarget.PYTHON

test_compile_files()

# Generated at 2022-06-22 12:26:40.994572
# Unit test for function compile_files
def test_compile_files():
    import io, os, tempfile, unittest
    from contextlib import redirect_stdout

    class CompileFilesTest(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.TemporaryDirectory()
            self.input_ = os.path.join(self.tmpdir.name, 'input')
            os.makedirs(self.input_)

        def tearDown(self):
            self.tmpdir.cleanup()


# Generated at 2022-06-22 12:26:50.699583
# Unit test for function compile_files
def test_compile_files():
    import pytest
    from .test_data import compilation
    from .files import get_input_output_paths
    from .transformers import transformers
    from .exceptions import CompilationError, TransformationError
    from .utils.helpers import debug

    def _transform(path: str, code: str, target: CompilationTarget) -> Tuple[str, List[str]]:
        """Applies all transformation for passed target."""
        debug(lambda: 'Compiling "{}"'.format(path))
        dependencies = []  # type: List[str]
        tree = ast.parse(code, path)
        debug(lambda: 'Initial ast:\n{}'.format(dump(tree)))


# Generated at 2022-06-22 12:26:57.767306
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .files import TestsPaths

    tests = TestsPaths.from_config()

    def get_output(file):
        return tests.output / file.relative_to(tests.input)

    for file in tests.files:
        assert file.read_text() == get_output(file).read_text()

    assert compile_files(tests.input.as_posix(),
                         tests.output.as_posix(),
                         'python').count == len(tests.files)

# Generated at 2022-06-22 12:27:06.841410
# Unit test for function compile_files
def test_compile_files():
    from .files import get_input_output_paths
    from .utils.helpers import capture_output
    from .transformers import native as native_transformers
    from .transformers import targets

    # Add code to write __debug__ variable.
    transformers.append(native_transformers.RemovePrintTransformer)
    code = """
# Compile with native.
import sys
print(sys.copyright)
    """
    input_path = Path('some/path')

    with capture_output() as (stdout, stderr):
        result = compile_files(
            input_path.as_posix(),
            'other/path',
            targets.NATIVE)
    assert result.target == targets.NATIVE
    assert len(result.dependencies) == 0
    assert result.time_spent == 0

# Generated at 2022-06-22 12:27:08.220974
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:27:17.117085
# Unit test for function compile_files
def test_compile_files():
    from . import compile_files
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as d:
        result = compile_files(d + '/input',
                               d + '/output',
                               CompilationTarget.ES5)

    assert result.file_count == 0
    assert result.target == CompilationTarget.ES5
    assert result.dependencies == []

# Generated at 2022-06-22 12:27:26.344082
# Unit test for function compile_files
def test_compile_files():
    from .files import test_get_input_output_paths
    from .tests import test_transformers

    input_ = test_transformers.__file__
    output = test_transformers.__file__ + '_output'
    root = test_get_input_output_paths.__file__

    result = compile_files(input_, output, CompilationTarget.ANNOTATIONS_ONLY, root)
    assert result.count == 1, "count should be 1"
    assert result.time >= 0, "time should be >= 0"
    assert result.target == CompilationTarget.ANNOTATIONS_ONLY
    assert result.dependencies == ['typed_ast', 'typing']

# Generated at 2022-06-22 12:27:30.546447
# Unit test for function compile_files
def test_compile_files():
    input_ = 'resources/src/'
    output = 'resources/dist/'
    root = 'resources/'
    target = CompilationTarget.PRODUCTION
    result = compile_files(input_, output, target, root)

    assert result.count == 3
    assert result.target == target
    assert result.dependencies == ['aiohttp', 'gino', 'pytest']

# Generated at 2022-06-22 12:27:41.754226
# Unit test for function compile_files
def test_compile_files():
    import io
    import tempfile

    # Create an empty name space.
    ns = globals().copy()
    ns['__name__'] = '__main__'

    # Create a temporary file.
    f = tempfile.TemporaryFile()

    # Write original code to file.
    f.write(b'import click\n@click.command()\ndef main():\n  pass\n')

    # Set the cursor position.
    f.seek(0)

    # Make the file appear to be a valid Python module.
    ns['__file__'] = 'teco.py'

    # Load the content into a code object.
    code = compile(f.read().decode('utf-8'), ns['__file__'], 'exec')

    # Execute the code.
    exec(code, ns)

    #

# Generated at 2022-06-22 12:27:48.034452
# Unit test for function compile_files
def test_compile_files():
    test_input = "tests/io_example"
    test_output = "tests/build"
    compile_files(test_input, test_output, CompilationTarget.NODE)
    assert Path('tests/build/build_io/mod.js').exists()
    assert Path('tests/build/build_io/sub/mod2.js').exists()
    assert Path('tests/build/build_io/sub/subsub/mod3.js').exists()

# Generated at 2022-06-22 12:27:58.909326
# Unit test for function compile_files
def test_compile_files():
    from .files import get_files, get_files_with_dependencies
    from .types import CompilationResult

    result = compile_files('tests/files/input',
                           'tests/files/output',
                           CompilationTarget.partial)
    assert result.count == 3
    assert result.dependencies == ['module_2']
    assert result.target == CompilationTarget.partial
    assert 0 < result.duration < 1

    with open('tests/files/output/module_1.py', 'r') as file:
        assert file.read() == 'def test(a, b):\n    x, y = 1, 2\n    return x + y\n'

# Generated at 2022-06-22 12:28:10.889414
# Unit test for function compile_files
def test_compile_files():
    from tempfile import mkdtemp
    from pathlib import Path
    import os

    tmp = Path(mkdtemp())
    tmp.joinpath('src/static/a.py').write_text('import sys\nimport os')
    tmp.joinpath('src/a.py').write_text('import sys\nimport os')
    tmp.joinpath('src/b.py').write_text('import sys\nimport os')

    assert compile_files(tmp / 'src', tmp / 'build', CompilationTarget.ES5) == CompilationResult(
        2, 0.0, CompilationTarget.ES5, ['sys', 'os'])
    os.remove(tmp / 'build' / 'static' / 'a.py')
    assert compile_files(tmp / 'src', tmp / 'build', CompilationTarget.ES5)

# Generated at 2022-06-22 12:28:12.319358
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('./test/test_files/test_input',
                         './test/test_files/test_output', target=0).count == 3

# Generated at 2022-06-22 12:28:23.925269
# Unit test for function compile_files
def test_compile_files():
    import os
    argparse.ArgumentParser().parse_args(['-v', '-r=python3', 'c:\\Users\\Jimmy\\my\\py-compilation\\test\\test-input',
                                          'c:\\Users\\Jimmy\\my\\py-compilation\\test\\test-output'])
    input_ = "test/test_input"
    output = "test/test_output"
    target = CompilationTarget.PYTHON27
    root = "c:\\Users\\Jimmy\\my\\py-compilation\\test\\test-input"

    for paths in get_input_output_paths(input_, output, root):
        with paths.input.open() as f:
            code = f.read()
        print(paths.output.parent.as_posix())

# Generated at 2022-06-22 12:28:30.843346
# Unit test for function compile_files
def test_compile_files():
    from pytest import raises
    from .utils.helpers import with_test_data
    from .exceptions import CompilationError

    with with_test_data('test_compile_files') as data:
        result = compile_files(str(data.input), str(data.output),
                               CompilationTarget.TARGET_JAVASCRIPT,
                               data.root.as_posix())

        assert result.dependencies == [
            'foo.py',
            'test/test_path_test.py',
            'test/test_path.py'
        ]
        assert result.count == 5
        assert result.target == CompilationTarget.TARGET_JAVASCRIPT

        assert result.compilation_time > 0
        assert result.compilation_time < 30
