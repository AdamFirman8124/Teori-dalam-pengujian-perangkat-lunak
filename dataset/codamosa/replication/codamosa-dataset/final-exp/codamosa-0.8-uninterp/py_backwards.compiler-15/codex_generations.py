

# Generated at 2022-06-22 12:24:40.870773
# Unit test for function compile_files
def test_compile_files():
    import os
    from .files import get_input_output_paths
    from .tests.fixtures.base import BASE_INPUT, BASE_OUTPUT, BASE_OUTPUT_DEPS, BASE_OUTPUT_DEPS_AST, BASE_DEPS
    from .tests.fixtures.base import BASE_INPUT_NONSTD, BASE_OUTPUT_NONSTD, BASE_OUTPUT_NONSTD_DEPS, BASE_NONSTD_DEPS

    # Cleanup first
    for path in get_input_output_paths(BASE_INPUT, BASE_OUTPUT):
        if path.output.exists():
            path.output.unlink()
        path.output.parent.rmdir()

    # Compile files with dependencies

# Generated at 2022-06-22 12:24:45.172677
# Unit test for function compile_files
def test_compile_files():
    try:
        compile_files('/tmp/input', '/tmp/output', 'objc')
    except CompilationError as e:
        assert(e.path == '/tmp/input')


# Generated at 2022-06-22 12:24:48.089409
# Unit test for function compile_files
def test_compile_files():
    raise NotImplementedError()

# Generated at 2022-06-22 12:24:52.708292
# Unit test for function compile_files
def test_compile_files():
    start = time()
    compile_files('/PyNsource/tests/unittest/input_for_transformers', '/PyNsource/tests/unittest/output_for_transformers', CompilationTarget.COMPATIBLE)
    print('Time taken is ', time() - start)

# test_compile_files()



# Generated at 2022-06-22 12:24:54.734639
# Unit test for function compile_files
def test_compile_files():
    compile_files(input_="tests/assets/src", output="tests/assets/out",
                  target=CompilationTarget.PYTHON3)

# Generated at 2022-06-22 12:24:55.315670
# Unit test for function compile_files
def test_compile_files():
    pass

# Generated at 2022-06-22 12:24:59.780265
# Unit test for function compile_files
def test_compile_files():
    compile_files('/Users/sidmishra/PycharmProjects/ast-transformer/test',
                  '/Users/sidmishra/PycharmProjects/ast-transformer/test_out',
                  CompilationTarget.TEST)

# Generated at 2022-06-22 12:25:01.192961
# Unit test for function compile_files
def test_compile_files():
    # TODO: add tests
    return True

# Generated at 2022-06-22 12:25:10.665166
# Unit test for function compile_files
def test_compile_files():
    from .files import relative_path_generator
    from .utils import default_target
    result = compile_files('./tests/data', './tests/output', default_target)

    assert result.count == 1
    assert result.target == default_target
    assert all(path.startswith('./tests/data') for path in result.dependencies)

    for paths in relative_path_generator('./tests/data', './tests/output', './tests/data'):
        with open(paths.input.as_posix()) as fin,\
                open(paths.output.as_posix()) as fout:
            assert fout.read() == fin.read()

# Generated at 2022-06-22 12:25:21.126214
# Unit test for function compile_files
def test_compile_files():
    assert compile_files('', '', CompilationTarget.PYTHON) == \
        CompilationResult(0, 0, CompilationTarget.PYTHON, [])

    assert compile_files('./compile.py', '', CompilationTarget.PYTHON) == \
        CompilationResult(1, 0, CompilationTarget.PYTHON, [])

    assert compile_files('./test.js', '', CompilationTarget.PYTHON) == \
        CompilationResult(1, 0, CompilationTarget.PYTHON, [])

    assert compile_files('./test.js', '', CompilationTarget.JAVA_SCRIPT) == \
        CompilationResult(1, 0, CompilationTarget.JAVA_SCRIPT, [])

