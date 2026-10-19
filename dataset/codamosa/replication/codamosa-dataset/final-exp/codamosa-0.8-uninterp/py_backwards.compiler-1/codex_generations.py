

# Generated at 2022-06-22 12:24:33.794012
# Unit test for function compile_files
def test_compile_files():
    assert False



# Generated at 2022-06-22 12:24:35.618888
# Unit test for function compile_files
def test_compile_files():
    compile_files('test/input', 'test/output',
                  CompilationTarget.PYTHON27, 'test')

# Generated at 2022-06-22 12:24:45.616010
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files."""
    # TODO: probably move this function to tests/ directory
    import tempfile
    import shutil

    input_ = tempfile.mkdtemp()
    output = tempfile.mkdtemp()

    input_.joinpath('foo.py').write_text('a = 1')

    compile_files(input_.as_posix(), output.as_posix(), CompilationTarget.PY2, input_.as_posix())

    print(output.joinpath('foo.py').read_text())

    shutil.rmtree(input_)
    shutil.rmtree(output)


# Generated at 2022-06-22 12:24:54.166295
# Unit test for function compile_files
def test_compile_files():
    from .test.test_fs import random_file
    from .test.test_helpers import random_directory

    input_ = random_directory()
    output = random_directory()
    input_file = input_.joinpath(random_file())
    output_file = output.joinpath(input_file.relative_to(input_))
    with input_file.open('w') as f:
        f.write('1+1')
    compile_files(input_, output, CompilationTarget.BROWSER)
    with output_file.open() as f:
        assert f.read() == '1 + 1;'

if __name__ == '__main__':
    test_compile_files()

# Generated at 2022-06-22 12:25:00.211162
# Unit test for function compile_files
def test_compile_files():
    compile_files('test/test_files', 'test/test_files_output', CompilationTarget.PYTHON)
    compile_files('test/test_files', 'test/test_files_output', CompilationTarget.JS)
    compile_files('test/test_files', 'test/test_files_output', CompilationTarget.WASM)

# Generated at 2022-06-22 12:25:06.288347
# Unit test for function compile_files
def test_compile_files():
    result = compile_files(
        'tests/files/compile',
        'tests/files/compile_compiled',
        CompilationTarget.CPYTHON32,
        'tests'
    )
    assert result.count == 4
    assert result.dependencies == ['typed-ast', 'typed-astunparse']
    assert result.time > 0

# Generated at 2022-06-22 12:25:12.272364
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    tmp_dir = tempfile.TemporaryDirectory()
    try:
        c = compile_files(tmp_dir.name + '/in/a.py',
                          tmp_dir.name + '/out/a.py',
                          CompilationTarget.PY2,
                          tmp_dir.name)
        assert c.dependencies == []
        assert c.target == CompilationTarget.PY2
    finally:
        tmp_dir.cleanup()

# Generated at 2022-06-22 12:25:17.008341
# Unit test for function compile_files
def test_compile_files():
    import pathlib
    input_ = pathlib.Path(__file__).absolute().parent.parent / 'test' / 'input'
    output = pathlib.Path(__file__).absolute().parent.parent / 'test' / 'output'
    target = CompilationTarget.STANDARD
    compile_files(input_, output, target)
# print(compile_files(input_, output, target))

# Generated at 2022-06-22 12:25:28.775617
# Unit test for function compile_files
def test_compile_files():
    from .cli import cli
    from .utils.helpers import debug
    import click
    import click.testing
    import runner
    import sys

    @click.command()
    @click.argument('target', type=CompilationTarget)
    @click.argument('input_')
    @click.argument('output')
    def test(input_, output, target):
        """This is a test command."""
        click.echo(cli._compile_files(input_, output, target))

    runner = click.testing.CliRunner()
    result = runner.invoke(test, ['t', 'fixtures/compile_files/input', 'fixtures/compile_files/output'])

    assert result.exit_code == 0

# Generated at 2022-06-22 12:25:35.688328
# Unit test for function compile_files
def test_compile_files():
    input_ = 'tests/data/code'
    output = '/tmp/test'
    target = CompilationTarget.ES5
    res = compile_files(input_, output, target)
    assert res.count == 5
    assert res.time > 0

    try:
        res = compile_files('tests/data/code_invalid', output, target)
    except CompilationError:
        pass
    else:
        assert False

# Generated at 2022-06-22 12:25:51.787113
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil
    import os
    import re

    outdir = tempfile.mkdtemp()


# Generated at 2022-06-22 12:25:54.990079
# Unit test for function compile_files
def test_compile_files():
    assert compile_files("docs/examples/hello", "docs/examples/test", CompilationTarget.ALL) == CompilationResult(1, 0, CompilationTarget.ALL, [])

# Generated at 2022-06-22 12:26:04.612133
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    import tempfile
    import shutil
    import pytest

    test_dir = tempfile.mkdtemp()

    input_dir = Path(test_dir) / 'input'
    output_dir = Path(test_dir) / 'output'

    def check(path: str, target: CompilationTarget = CompilationTarget.ANY) -> None:
        input_path = input_dir / path
        output_path = output_dir / path
        input_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        input_path.write_text('def a():\n  x = 3\n  return x')

        compile_files(input_dir, output_dir, target, input_dir)

# Generated at 2022-06-22 12:26:05.367176
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('tests/examples', 'build/examples', CompilationTarget.CPYTHON)

# Generated at 2022-06-22 12:26:14.453342
# Unit test for function compile_files
def test_compile_files():
    import shutil
    import os
    from .files import DUMMY_SRC, DUMMY_OUT
    from .types import CompilationTarget
    from .utils import compile_files
    from .transformers import (ImportTransformer, ImportContainsTransformer,
                               FunctionTransformer, ParameterTransformer,
                               MethodTransformer, AttributeTransformer,
                               GlobalTransformer, ClassTransformer,
                               DecoratorTransformer,
                               ComprehensionTransformer, LambdaTransformer,
                               ListTransformer)

    shutil.rmtree(DUMMY_OUT, ignore_errors=True)
    os.makedirs(DUMMY_OUT)

    # compile a single file with all features

# Generated at 2022-06-22 12:26:25.605859
# Unit test for function compile_files
def test_compile_files():
    from pathlib import Path
    from .files import rmtree
    from .exceptions import CompilationError
    import os
    import sys

    rmtree(Path('__target__'))
    rmtree(Path('__input__'))

    Path('__input__').mkdir()

    Path('__input__/test.py').write_text('a\nb\nc')

    # Test correct compile
    assert compile_files('__input__',
                         '__target__',
                         CompilationTarget.PYTHON27) == \
        CompilationResult(1, 0, CompilationTarget.PYTHON27, [])

    assert Path('__target__/test.py').read_text() == 'a\nb\nc'

    # Test compile with syntax error

# Generated at 2022-06-22 12:26:37.076194
# Unit test for function compile_files
def test_compile_files():
    from .types import CompilationTarget
    from .compiler import compile_files, get_input_output_paths

    input_ = 'tests/data/compiler/input'
    output = 'tests/data/compiler/output'

    input_output_paths = list(get_input_output_paths(input_, output, 'tests/data/compiler'))

    # Test standard compilation
    assert compile_files(input_, output, CompilationTarget.STANDARD).count == 2
    assert input_output_paths[0].output.read_text() == 'a = \'foo\'\n'
    assert input_output_paths[1].output.read_text() == 'a = \'bar\'\n'

    # Test transpilation for browser compilation target

# Generated at 2022-06-22 12:26:37.969272
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:26:38.980695
# Unit test for function compile_files
def test_compile_files():
    assert __doc__ == compile_files.__doc__

# Generated at 2022-06-22 12:26:39.706436
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:26:58.977273
# Unit test for function compile_files
def test_compile_files():
    import os

    # Sets the environment variable
    os.environ['MYENVVAR'] = "import os\nmsg='MYENVVAR set to '+os.environ['MYENVVAR']\nprint(msg)\n"

    input_ = 'tests/data/compiler/input'
    output = 'tests/data/compiler/output'

    result = compile_files(input_, output, CompilationTarget.EXEC)

    assert result.count == 4

    assert result.durations > 0

    assert result.target == CompilationTarget.EXEC

    assert len(result.dependencies) == 3

    assert 'sys' in result.dependencies

    assert 'os' in result.dependencies

    assert 'compiler' in result.dependencies

# Generated at 2022-06-22 12:27:06.551675
# Unit test for function compile_files
def test_compile_files():
    input_ = Path(__file__).parent.parent / 'test' / 'fixture'
    output = input_ / 'output'
    result = compile_files(str(input_), str(output), CompilationTarget.PYTHON27)
    assert result.count == 3
    assert output.exists()
    assert (output / 'file_with_dependencies.py').exists()
    assert (output / 'empty_file.py').exists()
    assert (output / 'subdir' / 'subsubdir' / 'subsub_file.py').exists()
    assert result.dependencies == []

# Generated at 2022-06-22 12:27:12.838649
# Unit test for function compile_files
def test_compile_files():
    """Performs a single unit test for compile_files."""
    import os
    import shutil
    import unittest

    try:
        shutil.rmtree('test')
    except FileNotFoundError:
        pass

    os.makedirs('test', exist_ok=True)

    file = open('test/test.py', 'w')

# Generated at 2022-06-22 12:27:19.484150
# Unit test for function compile_files
def test_compile_files():
    from .testing import test_target_all
    from .types import CompilationTarget
    from .exceptions import CompilationError

    def run(input_: str, target: CompilationTarget = CompilationTarget.JS) -> CompilationResult:
        import textwrap
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            input_path = tmpdir + '/input'
            output_path = tmpdir + '/output'
            input_path.mkdir()
            output_path.mkdir()
            (input_path + '../test.js').write_text(textwrap.dedent(input_))
            return compile_files(str(input_path), str(output_path), target)

    test_target_all(CompilationTarget.JS, run)

# Generated at 2022-06-22 12:27:26.454182
# Unit test for function compile_files
def test_compile_files():
    import os
    import shutil
    import tempfile
    import filecmp

    SOURCE = os.path.join(os.path.dirname(__file__), '..', 'test')
    TARGET = 'test_compile_files'
    INPUT_ = os.path.join(SOURCE, TARGET, 'input')
    OUTPUT = os.path.join(SOURCE, TARGET, 'output')
    TMP = tempfile.mkdtemp()
    RESULT = compile_files(INPUT_, os.path.join(TMP, TARGET), 'js-min')

    assert RESULT.count == 5
    assert RESULT.time > 0
    assert RESULT.target == 'js-min'
    assert RESULT.dependencies == []


# Generated at 2022-06-22 12:27:36.667728
# Unit test for function compile_files
def test_compile_files():
    from .tests.test_helpers import get_testing_path

    def test(code: str, transformed: str, error: Optional[str],
             target: CompilationTarget):
        try:
            result = compile_files(get_testing_path('input'),
                                   get_testing_path('output'), target)
            count = result.count
            assert count == 1
            assert result.target == target
            assert not result.dependencies
            with open(get_testing_path('output/input.py'), 'r') as f:
                assert f.read() == transformed
        except Exception as e:
            e = str(e)
            if error is None:
                raise AssertionError('{!r} != None'.format(e))
            assert e.startswith(error)

    # Pythonic code

# Generated at 2022-06-22 12:27:47.462316
# Unit test for function compile_files
def test_compile_files():
    import tempfile
    import shutil

    import pytest

    from .types import CompilationResult
    from .utils.helpers import debug


# Generated at 2022-06-22 12:27:58.753336
# Unit test for function compile_files
def test_compile_files():
    from .files import get_input_output_paths, InputOutput
    from .types import CompilationErrorDetails
    from typing import List, Dict, Union
    import shutil
    import tempfile
    import pytest
    import os
    import re

    @pytest.fixture
    def recorder(request) -> List:
        """Collects exception details during execution."""
        recorder = []
        def record(exception):
            recorder.append(exception.exc_info[1])
        request.addfinalizer(lambda: record(exception))
        return recorder

    @pytest.fixture
    def code_to_errors() -> Dict[str, Union[List[CompilationErrorDetails], List[int]]]:
        """Collects mapping from code to exceptions."""
        code_to_errors = {}

# Generated at 2022-06-22 12:28:05.135988
# Unit test for function compile_files
def test_compile_files():
    results = compile_files("test/files/compile_files/input",
                            "test/files/compile_files/output",
                            CompilationTarget.ALL)
    assert 1 == results.compiled_files
    assert 0 != results.time
    assert CompilationTarget.ALL == results.target
    assert ['test/files/compile_files/input/A.py'] == results.dependencies

# Generated at 2022-06-22 12:28:10.572779
# Unit test for function compile_files
def test_compile_files():
    result = compile_files('test_files', 'output', 'ecma5')
    assert result.target == 'ecma5'
    assert len(result.dependencies) == 3
    assert 'one' in result.dependencies
    assert 'deps/two' in result.dependencies
    assert 'subdir/subsub/three' in result.dependencies