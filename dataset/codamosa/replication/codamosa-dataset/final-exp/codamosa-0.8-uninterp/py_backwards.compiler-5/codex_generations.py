

# Generated at 2022-06-22 12:24:45.685293
# Unit test for function compile_files
def test_compile_files():
    from .config import default_config_path
    from .utils.helpers import get_fixtures
    from .transformers import Transformer
    from .types import CompilationTarget
    from .exceptions import CompilationError
    import os.path
    import shutil

    input_ = os.path.join(get_fixtures(), 'lesson_simple')
    output = os.path.join(get_fixtures(), 'lesson_simple.compiled')
    root = None

    # Check default options
    compile_files(input_, output, CompilationTarget.SIMPLE, root)
    shutil.rmtree(output)

    # Check simple mode
    compile_files(input_, output, CompilationTarget.SIMPLE, root)
    shutil.rmtree(output)

    # Check html mode

# Generated at 2022-06-22 12:24:47.679425
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:24:54.161484
# Unit test for function compile_files
def test_compile_files():
    assert compile_files(
        './tests/input', './tests/output', CompilationTarget.BROWSER)
    assert compile_files(
        './tests/input', './tests/output', CompilationTarget.NODE)
    assert compile_files('./tests/input', './tests/output',
                         CompilationTarget.NODE_NUNIT)
    assert compile_files(
        './tests/input', './tests/output', CompilationTarget.NUNIT)



# Generated at 2022-06-22 12:25:04.771178
# Unit test for function compile_files
def test_compile_files():
    from .utils.helpers import clear_cache
    from . import __file__ as root
    from .utils.exceptions import CompilationError
    from .types import CompilationTarget
    from . import tests
    from .exceptions import TransformationError
    from .types import CompilationResult
    from .utils.helpers import get_cache_directory
    from pathlib import Path

    clear_cache()
    assert compile_files(
        tests.__path__[0],
        get_cache_directory()[:get_cache_directory().rindex('/') + 1] + 'tests',
        CompilationTarget.PYTHON33) == CompilationResult(22, 0.05, CompilationTarget.PYTHON33, [])

    clear_cache()

# Generated at 2022-06-22 12:25:14.682679
# Unit test for function compile_files
def test_compile_files():
    import pytest
    import os
    import os.path
    import shutil
    from .exceptions import CompilationError
    # from .compile import compile_files
    from .types import CompilationResult

    # Cleanup after previous run
    if os.path.isdir('demo_out'):
        shutil.rmtree('demo_out')

    # Run valid file
    result = compile_files('demo', 'demo_out', CompilationTarget.ES5)

    assert isinstance(result, CompilationResult)
    assert result.file_count == 3
    assert result.dependencies == ['fibonacci', 'sum', 'sum3']
    assert os.path.exists('demo_out/main.py')

    # Run invalid files

# Generated at 2022-06-22 12:25:26.144678
# Unit test for function compile_files
def test_compile_files():
    from .exceptions import CompilationError
    from .types import CompilationResult
    import tempfile
    import shutil

    # Type check
    result = compile_files('input', 'output', CompilationTarget.ES5)
    assert isinstance(result, CompilationResult)
    assert result.files_compiled == 0
    assert result.duration > 0
    assert result.target == CompilationTarget.ES5

    # Code without errors

# Generated at 2022-06-22 12:25:30.464927
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('test', 'test', CompilationTarget.ES5)
    assert compile_files('test', 'test', CompilationTarget.BROWSER)
    assert compile_files('test', 'test', CompilationTarget.NODE)

# Generated at 2022-06-22 12:25:33.577985
# Unit test for function compile_files
def test_compile_files():
    CompilationResult(0, 0.0, CompilationTarget.TARGET_1, [])
    CompilationResult(1, 0.0, CompilationTarget.TARGET_1, [])

# Generated at 2022-06-22 12:25:42.665203
# Unit test for function compile_files
def test_compile_files():
    """Unit test for function compile_files"""
 
    import os, shutil
    # Input and output folders are the same
    input_dir = "./sample_data/extensions/lib"
    output_dir = "./sample_data/extensions/lib"
    # Remove output directory if present
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    # Compile all files from input_ to output
    CompilationResult = compile_files(input_dir, output_dir, CompilationTarget.RUNTIME)
    # Check if file has been written in output directory
    assert(os.path.exists(os.path.join(output_dir,"_test.js")))
    # Remove output directory
    shutil.rmtree(output_dir)
    # Check compilation

# Generated at 2022-06-22 12:25:46.836051
# Unit test for function compile_files
def test_compile_files():
    compile_files('test/test_src', 'test/test_compiled', CompilationTarget.ES5)
    print(compile_files('test/test_src', 'test/test_compiled', CompilationTarget.ES5))