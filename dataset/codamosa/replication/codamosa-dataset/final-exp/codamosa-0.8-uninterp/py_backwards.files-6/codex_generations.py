

# Generated at 2022-06-14 01:33:18.068824
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test invalid input/output case
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('input', 'output.txt', None)

    # Test input doesn't exists case
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('input', 'output.py', None)

# Generated at 2022-06-14 01:33:26.500862
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('input', 'output', None)) == [InputOutput(Path('input'), Path('output'))]

    assert list(get_input_output_paths('input', 'output/foo.py', None)) == [InputOutput(Path('input'), Path('output/foo.py'))]

    assert list(get_input_output_paths('input/foo.py', 'output/foo.py', None)) == [InputOutput(Path('input/foo.py'), Path('output/foo.py'))]

    assert list(get_input_output_paths('input', 'output/foo.py', 'input')) == []


# Generated at 2022-06-14 01:33:36.959923
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    def _assert(input_: str, output: str, root: Optional[str],
                input_output_paths: Iterable[InputOutput]):
        assert list(get_input_output_paths(input_, output, root)) == input_output_paths


# Generated at 2022-06-14 01:33:48.303319
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    res = list(get_input_output_paths('a', 'b', None))
    assert len(res) == 1
    assert res[0].input == Path('a')
    assert res[0].output == Path('b') / 'a'

    res = list(get_input_output_paths('a.py', 'b', None))
    assert len(res) == 1
    assert res[0].input == Path('a.py')
    assert res[0].output == Path('b') / 'a.py'

    res = list(get_input_output_paths('a', 'b.py', None))
    assert len(res) == 0

    res = list(get_input_output_paths('a.py', 'b.py', None))
    assert len(res) == 1
    assert res

# Generated at 2022-06-14 01:33:57.106255
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths(
        input_='/tmp/geniecam.py',
        output='/tmp/geniecam.py')) == [
        InputOutput(
            Path('/tmp/geniecam.py'),
            Path('/tmp/geniecam.py'))]

    assert list(get_input_output_paths(
        input_='/tmp/geniecam.py',
        output='/tmp/autodiff')) == [
        InputOutput(
            Path('/tmp/geniecam.py'),
            Path('/tmp/autodiff/geniecam.py'))]


# Generated at 2022-06-14 01:34:06.578498
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('./a/b.py', './x', None)) == \
        [InputOutput(Path('a/b.py'), Path('x/b.py'))]

    assert list(get_input_output_paths('./a/b.py', './x/y', None)) == \
        [InputOutput(Path('a/b.py'), Path('x/y/b.py'))]

    assert list(get_input_output_paths('./a/b.py', './', None)) == \
        [InputOutput(Path('a/b.py'), Path('b.py'))]


# Generated at 2022-06-14 01:34:10.265913
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    source_paths = get_input_output_paths("./sample/source", "./sample/build", "./sample/source/sub1")
    print(source_paths)
    for src_path in source_paths:
        print(src_path)

if __name__ == "__main__":
    test_get_input_output_paths()

# Generated at 2022-06-14 01:34:25.315272
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Testing get_input_output_paths"""

# Generated at 2022-06-14 01:34:36.457448
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import os
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEST_INPUT_DIR = 'codify/tests/test_data/test_input'
    TEST_OUTPUT_DIR = 'codify/tests/test_data/test_output'
    input_file = TEST_INPUT_DIR + '/input_file.py'
    input_dir = TEST_INPUT_DIR + '/input_dir'
    output_file = TEST_OUTPUT_DIR + '/output_file.py'
    output_dir = TEST_OUTPUT_DIR + '/output_dir'
    output_subdir = TEST_OUTPUT_DIR + '/output_subdir/output_subdir_file.py'

    # assert case convert one file

# Generated at 2022-06-14 01:34:48.434935
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('./test_data', './test_data', None)) == [
        InputOutput(Path('./test_data/src/foo.py'), Path('./test_data/src/foo.py'))]
    assert list(get_input_output_paths('./test_data/', './test_data_new/', None)) == [
        InputOutput(Path('./test_data/src/foo.py'), Path('./test_data_new/src/foo.py'))]

# Generated at 2022-06-14 01:35:09.499635
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    def case_return_list(input_: str, output: str, root: Optional[str]) -> Iterable[InputOutput]:
        return list(get_input_output_paths(input_, output, root))
    def case_throw_error(input_: str, output: str, root: Optional[str]) -> Iterable[InputOutput]:
        try:
            get_input_output_paths(input_, output, root)
        except InvalidInputOutput:
            pass
        else:
            raise AssertionError("get_input_output_paths() not throwed InvalidInputOutput.")
        try:
            get_input_output_paths(input_, output, root)
        except InputDoesntExists:
            pass

# Generated at 2022-06-14 01:35:19.265597
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    from .exceptions import InvalidInputOutput

    def assert_input_output_paths(input_, output, expected):
        actual = list(get_input_output_paths(input_, output, root))
        assert actual == expected

    # When input is one file, output should be one file
    root = '/'
    input_ = '/input/file.py'
    output = '/output/file.py'
    expected = [InputOutput(Path('/input/file.py'), Path('/output/file.py'))]
    assert_input_output_paths(input_, output, expected)

    # When input is one file, output should be one file
    input_ = '/input/file.py'
    output = '/output'

# Generated at 2022-06-14 01:35:30.254163
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    print('Testing function get_input_output_paths()')
    temp_folder = Path(tempfile.mkdtemp())
    print('Using temp folder {}'.format(temp_folder))
    input_folder = temp_folder.joinpath('input')
    input_folder.mkdir()
    print('Creating {}, {}, {} inside {}'.format('a.py', 'b.py', 'c.py', str(input_folder)))
    temp_folder.joinpath('a.py').write_text('')
    temp_folder.joinpath('b.py').write_text('')
    temp_folder.joinpath('c.py').write_text('')

# Generated at 2022-06-14 01:35:39.189130
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    base_path = Path(__file__).parent

# Generated at 2022-06-14 01:35:48.353445
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths()."""
    # arguments
    input_ = "test"
    output = "output"
    root = None
    # function get_input_output_paths()
    input_output = get_input_output_paths(input_, output, root)
    # check function get_input_output_paths()
    #assert len(input_output) == 1
    #assert input_output[0].input == Path('test')
    #assert input_output[0].output == Path('output')
    assert input_output



# Generated at 2022-06-14 01:35:56.882208
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """get_input_output_paths should return input/output paths pairs."""
    pairs = get_input_output_paths(
        input_='test/test', output='test/test_output', root='test')
    assert list(pairs) == [
        InputOutput(Path('test/test/test.py'), Path('test/test_output/test.py')),
        InputOutput(
            Path('test/test/test/test.py'),
            Path('test/test_output/test/test.py')),
    ]

    pairs = get_input_output_paths(
        input_='test/test/test.py', output='test/test_output', root='test')

# Generated at 2022-06-14 01:36:08.005610
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    Test without root
    """
    input_str = '/home/example/file1.py'
    output_str = '/home/example/output/file1.py'
    root_str = None
    input_output_paths = get_input_output_paths(input_str, output_str, root_str)
    input_output_paths = list(input_output_paths)
    correct_input_output_paths = [InputOutput(Path(input_str), Path(output_str))]
    assert input_output_paths == correct_input_output_paths

    input_str = '/home/example'
    output_str = '/home/output/'
    root_str = None

# Generated at 2022-06-14 01:36:20.195337
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test empty arguments
    try:
        input_outputs = get_input_output_paths('', '')
        assert False
    except InputDoesntExists:
        pass

    # Test input doesnt exits, but output exists
    try:
        input_outputs = get_input_output_paths('tests/test_data/test_invalid_input.py',
                                               'tests/test_data/test_output')
        assert False
    except InputDoesntExists:
        pass

    # Test input is a file and output is a file
    input_outputs = get_input_output_paths('tests/test_data/test_input.py',
                                           'tests/test_data/test_output.py')
    input_outputs = list(input_outputs)

# Generated at 2022-06-14 01:36:29.116364
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('input', 'output', None)) == [InputOutput(Path('input'), Path('output'))]
    assert list(get_input_output_paths('input.py', 'output.py', None)) == [InputOutput(Path('input.py'), Path('output.py'))]
    assert list(get_input_output_paths('input', 'output', '/')) == [InputOutput(Path('input'), Path('output/input'))]
    assert list(get_input_output_paths('input.py', 'output', '/')) == [InputOutput(Path('input.py'), Path('output/input.py'))]

# Generated at 2022-06-14 01:36:34.948877
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from .exceptions import InvalidInputOutput, InputDoesntExists

    input_output_list = []


# Generated at 2022-06-14 01:37:02.674684
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "./example/data1.txt"
    output = "./example/data1_output.txt"
    root = os.path.abspath("./example")
    result = get_input_output_paths(input_, output, root)
    correct_result = [InputOutput(Path("./example/data1.txt"), Path("./example/data1_output.txt"))]
    assert list(result) == correct_result

    input_ = "./example"
    output = "./example_output"
    root = os.path.abspath("./example")
    result = get_input_output_paths(input_, output, root)

# Generated at 2022-06-14 01:37:09.620742
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              "filesystem_test")
    output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               "filesystem_test2")
    expected_paths = [
        InputOutput(Path(input_path, "test1.py"),
                    Path(output_path, "test1.py")),
        InputOutput(Path(input_path, "test2.py"),
                    Path(output_path, "test2.py")),
        InputOutput(Path(input_path, "tests", "test3.py"),
                    Path(output_path, "tests", "test3.py")),
    ]


# Generated at 2022-06-14 01:37:18.419590
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    # Test invalid input/output files
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('test.txt', 'test.txt', None))
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('test.txt', 'test.py', None))
    # Test missing input file
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('missing.txt', 'test.py', None))
    # Test input/output files
    input_output_paths = list(get_input_output_paths('test.py', 'test.py', None))
    assert len(input_output_paths) == 1

# Generated at 2022-06-14 01:37:28.519985
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'C:/PythonCode/codestyle/paths.py'
    output = 'C:/Users/Kim/Downloads/'
    root = 'C:/PythonCode/'
    result = get_input_output_paths(input_, output, root)
    assert(result.__next__().input_path == Path(input_))
    assert(result.__next__().output_path == Path(output+'/paths.py'))
    assert(result.__next__().input_path == Path(output+'/paths_py.py'))
    assert(result.__next__().output_path == Path(output+'/paths_py.py'))

# Generated at 2022-06-14 01:37:39.440076
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Input is 'test.py' and output is 'output.py', expect normal execution
    for pair in get_input_output_paths(
            'test.py', 'output.py', None):
        assert pair.input == 'test.py'
        assert pair.output == 'output.py'

    # Expect an error when the output is not .py file
    try:
        for pair in get_input_output_paths(
                'test.py', 'output', None):
            pass
        assert False
    except InvalidInputOutput:
        pass

    # Expect an error when input file does not exist
    try:
        for pair in get_input_output_paths(
                'doesn\'t exist', 'output', None):
            pass
        assert False
    except InputDoesntExists:
        pass

    # Input

# Generated at 2022-06-14 01:37:47.672708
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Get input/output paths pairs.
    test_input_1 = "tests/test_data/test_input"
    test_output_1 = "tests/test_data/test_output"
    test_root_1 = None
    iop_1 = list(get_input_output_paths(test_input_1, test_output_1, test_root_1))
    assert iop_1 == [InputOutput(Path('tests/test_data/test_input/example1.py'),
                                 Path('tests/test_data/test_output/example1.py')),
                     InputOutput(Path('tests/test_data/test_input/example2.py'),
                                 Path('tests/test_data/test_output/example2.py'))]

    # Get input/output paths pairs.
    test

# Generated at 2022-06-14 01:38:01.994589
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_paths = get_input_output_paths(
        input_="tests/data/input",
        output="tests/data/output",
        root=None,
    )
    expected = [
        InputOutput(
            Path('tests/data/input/a.py'),
            Path('tests/data/output/a.py'),
        ),
        InputOutput(
            Path('tests/data/input/b/b.py'),
            Path('tests/data/output/b/b.py'),
        ),
        InputOutput(
            Path('tests/data/input/c/c.py'),
            Path('tests/data/output/c/c.py'),
        ),
    ]
    assert list(input_output_paths) == expected

# Generated at 2022-06-14 01:38:11.971672
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    pa1 = Path('/home/julie/input/')
    pa2 = Path('/home/julie/output/')
    io3 = InputOutput(pa1, pa2)
    io4 = InputOutput(pa1, pa2.joinpath(pa1.name))
    assert list(get_input_output_paths(str(pa1), str(pa2), str(pa1))) == [io4]
    assert list(get_input_output_paths(str(pa1), str(pa2), str(pa2))) == [io3]
    assert list(get_input_output_paths(str(pa1), str(pa2.joinpath(pa1.name)), str(pa1))) == [io4]

# Generated at 2022-06-14 01:38:22.025429
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:38:29.970538
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('tests/test_data/test_input.txt',
                                       'tests/test_data/test_input.txt',
                                       None)) == \
                                       [InputOutput(Path('tests/test_data/test_input.txt'), Path('tests/test_data/test_input.txt'))]
    assert list(get_input_output_paths('tests/test_data/test_input.txt',
                                       'tests/test_data/output',
                                       None)) == \
                                       [InputOutput(Path('tests/test_data/test_input.txt'), Path('tests/test_data/output/test_input.txt'))]

# Generated at 2022-06-14 01:39:13.987598
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # ===========================
    # Output path is a directory
    # ===========================
    io_paths = get_input_output_paths('/a/b/c.py', '/x/y/z', None)
    assert None not in io_paths
    io_paths = get_input_output_paths('/a/b/c.py', '/x/y/z', '')
    assert None not in io_paths
    io_paths = get_input_output_paths('/a/b/c.py', '/x/y/z', '/')
    assert None not in io_paths

    # ===================================================
    # Output path is a file (same as input path's filename)
    # ===================================================

# Generated at 2022-06-14 01:39:22.357588
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    result = list(get_input_output_paths('./test/test_code', './output', './test/test_code'))
    assert result == [InputOutput(Path('test/test_code/test_code.py'), Path('output/test_code.py'))]

    result = list(get_input_output_paths('./test/test_code/test_code.py', './output', None))
    assert result == [InputOutput(Path('test/test_code/test_code.py'), Path('output/test_code.py'))]

    result = list(get_input_output_paths('../test/test_code/test_code.py', './output', None))

# Generated at 2022-06-14 01:39:32.515273
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths("/home/test/test1.py", "/home/test/test", "no")) == [InputOutput(Path("/home/test/test1.py"), Path("/home/test/test/test1.py"))]
    assert list(get_input_output_paths("/home/test/test", "/home/test1.py", "no")) == [InputOutput(Path("/home/test/test/test.py"), Path("/home/test1.py"))]
    assert list(get_input_output_paths("/home/test/test", "/home/test", "no")) == [InputOutput(Path("/home/test/test/test.py"), Path("/home/test/test.py"))]

# Generated at 2022-06-14 01:39:40.193951
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .types import InputOutput
    from .exceptions import  InvalidInputOutput, InputDoesntExists
    from pathlib import Path
    import os
    import tempfile
    cwd = os.getcwd()
    fd = tempfile.TemporaryDirectory()

# Generated at 2022-06-14 01:39:49.218427
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with pytest.raises(Exception):
        get_input_output_paths("", "", "")

    with pytest.raises(Exception):
        get_input_output_paths("input", "", "")

    with pytest.raises(Exception):
        get_input_output_paths("input", "output", "")

    assert get_input_output_paths("input.py", "output.py", None) == InputOutput(Path("input.py"), Path("output.py"))
    assert get_input_output_paths("/input.py", "/output/output.py", None) == InputOutput(Path("/input.py"), Path("/output/output.py"))

# Generated at 2022-06-14 01:40:00.684307
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths(
        'a.py', 'b.py', '.')) == [InputOutput(Path('a.py'), Path('b.py'))]
    assert list(get_input_output_paths(
        'a', 'b', '.')) == [InputOutput(Path('a/a.py'), Path('b/a.py'))]
    assert list(get_input_output_paths(
        'a', 'b', 'a')) == [InputOutput(Path('a/a.py'), Path('b/a.py'))]


# Generated at 2022-06-14 01:40:10.178400
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    cwd = Path('/')
    root = Path('/a')
    check_path_pairs(['a.py', 'b.py'],
                     get_input_output_paths('a.py', 'b.py', None))
    check_path_pairs(['/a/a.py', '/a/b.py'],
                     get_input_output_paths('/a/a.py', '/a/b.py', None))
    check_path_pairs(['/a/a.py', '/a/b.py'],
                     get_input_output_paths('/a/a.py', '/b', '/a'))

# Generated at 2022-06-14 01:40:17.786616
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    assert list(get_input_output_paths(
        'tests/data/simple/simple.py', 'output.py', None)) == [
            InputOutput(Path('tests/data/simple/simple.py'),
                        Path('output.py'))]
    assert list(get_input_output_paths(
        'tests/data/simple/simple.py', 'output', None)) == [
            InputOutput(Path('tests/data/simple/simple.py'),
                        Path('output/simple.py'))]

# Generated at 2022-06-14 01:40:23.889614
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output = [
        ('./path', './output/folder'),
        ('./path/to/file.py', './output/folder/file.py')
    ]
    assert get_input_output_paths('./path', './output/folder') == input_output

# Generated at 2022-06-14 01:40:27.415093
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_input = 'test/test_input'
    test_output = 'test/test_output'
    test_root = 'test'
    test_input_output_paths = get_input_output_paths(test_input, test_output, test_root)
    assert len(list(test_input_output_paths)) == 2



# Generated at 2022-06-14 01:41:54.236490
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    path_a = Path(__file__).parent.parent.joinpath('test_files')
    path_b = Path(__file__).parent.parent.joinpath("test_files", "copy_of_test_files")

    assert list(get_input_output_paths(path_a, path_b, path_a)) == list(get_input_output_paths("test_files", "test_files", None))

# Generated at 2022-06-14 01:42:04.727697
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    temp_folder = tempfile.mkdtemp()

# Generated at 2022-06-14 01:42:10.702891
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Given
    input_ = "/a/b/c"
    output = "/a/b/d"
    root = "/a/b/c"

    # When
    inputOutputPaths = get_input_output_paths(input_, output, root)

    # Then
    assert len(inputOutputPaths) == 1
    inputOutput = inputOutputPaths[0]
    assert inputOutput.input_path.as_posix() == "/a/b/c"
    assert inputOutput.output_path.as_posix() == "/a/b/c"


# Generated at 2022-06-14 01:42:20.153739
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    io_paths = get_input_output_paths(input_='test1.py', output='test_out', root=None)
    assert(len(list(io_paths)) == 1)
    io_paths = get_input_output_paths(input_='test2.txt', output='test_out', root=None)
    assert(len(list(io_paths)) == 0)
    io_paths = get_input_output_paths(input_='test_dir', output='test_out', root=None)
    assert(len(list(io_paths)) == 2)
    io_paths = get_input_output_paths(input_='test_dir', output='test_out', root='test_dir')
    assert(len(list(io_paths)) == 2)

# Generated at 2022-06-14 01:42:30.014816
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('input.py', 'output.py', None)) == \
        [InputOutput(Path('input.py'), Path('output.py'))]
    assert list(get_input_output_paths('input_dir', 'output_dir', None)) == \
        [InputOutput(Path('input_dir/input.py'), Path('output_dir/input.py'))]
    assert list(get_input_output_paths('input_dir', 'output_dir', 'input_dir')) == \
        [InputOutput(Path('input_dir/input.py'), Path('output_dir/input.py'))]

# Generated at 2022-06-14 01:42:39.156605
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    paths = list(get_input_output_paths('/foo/bar', '/tmp/bar', None))
    assert len(paths) == 1
    assert paths[0].input_path == Path('/foo/bar')
    assert paths[0].output_path == Path('/tmp/bar')

    paths = list(get_input_output_paths('/foo/bar', '/tmp', '/foo'))
    assert len(paths) == 1
    assert paths[0].input_path == Path('/foo/bar')
    assert paths[0].output_path == Path('/tmp/bar')

    paths = list(get_input_output_paths('/foo', '/tmp', None))
    assert len(paths) == 1
    assert paths[0].input_path == Path('/foo')

# Generated at 2022-06-14 01:42:50.249159
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths function."""
    from .config import Config

    config_path = Config.get_config_path()

    assert tuple(get_input_output_paths('mypath', 'mypath', 'mypath')) == (InputOutput(Path('mypath/mypath'), Path('mypath/mypath')),)
    assert tuple(get_input_output_paths('mypath', 'mypath/output', 'mypath')) == (InputOutput(Path('mypath/mypath'), Path('mypath/mypath/output')),)
    assert tuple(get_input_output_paths(str(config_path), 'mypath/output', str(config_path))) == (InputOutput(Path('mypath/mypath'), Path('mypath/mypath/output')),)
    assert tuple

# Generated at 2022-06-14 01:43:00.758026
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:43:07.420746
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    result = get_input_output_paths('data/input.py', 'data/output.py', None)
    i = InputOutput(Path('data/input.py'), Path('data/output.py'))
    assert result == [i]
    
    result = get_input_output_paths('data/inp/input.py', 'data/out', None)
    i = InputOutput(Path('data/inp/input.py'), Path('data/out/input.py'))
    assert result == [i]