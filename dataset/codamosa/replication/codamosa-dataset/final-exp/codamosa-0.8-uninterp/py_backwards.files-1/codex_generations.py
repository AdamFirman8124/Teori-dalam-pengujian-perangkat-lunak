

# Generated at 2022-06-14 01:33:09.347498
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    import pytest
    from .exceptions import InputDoesntExists

    # ERRORS
    # Test for invalid input/output pairs
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('./tests/fixtures/non_exists.py', '.dist', None))
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('./tests/fixtures/', '.dist/non_exists.py', None))

    # Test for non-exists input
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('./non_exists.py', '.dist', None))

    # Test for single file

# Generated at 2022-06-14 01:33:15.369982
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test for valid input, output and root
    input_ = os.path.join(os.getcwd(), "tests/input")
    output = os.path.join(os.getcwd(), "tests/output")

    if not os.path.exists(os.path.join(input_, "input.py")):
        os.mkdir(input_)

    if not os.path.exists(os.path.join(input_, "input.py")):
        open(os.path.join(input_, "input.py"), 'w')

    i_o_paths = get_input_output_paths(input_, output, os.getcwd())

    assert next(i_o_paths).input_path.name == "input.py"

# Generated at 2022-06-14 01:33:25.706227
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Check invalid input file
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('foo.py', '/tmp/bar.py', None)
        get_input_output_paths('/tmp/foo.py', '/tmp/bar.py', None)

    # Check invalid output file
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('/tmp/foo.py', 'foo.py', None)
        get_input_output_paths('/tmp/foo.py', '/tmp/bar.py', None)

    # Check valid output file

# Generated at 2022-06-14 01:33:36.715536
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_input = '/foo/bar/baz'
    test_output = '/bar/foo/baz'
    test_output_root = '/bar/foo'

    case_1 = InputOutput(Path(test_input),Path(test_input))
    case_2 = InputOutput(Path(test_input),Path(test_output))
    case_3 = InputOutput(Path(test_input),Path(test_output_root).joinpath(Path(test_input).name))

    output = list(get_input_output_paths(test_input, test_output_root, None))
    assert len(output) == 1
    assert output[0] == case_1

    output = list(get_input_output_paths(test_input, test_output, None))
    assert len(output) == 1
   

# Generated at 2022-06-14 01:33:46.008237
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    assert list(get_input_output_paths('a.py', 'b.py', None)) == [InputOutput(Path('a.py'), Path('b.py'))]
    assert list(get_input_output_paths('a.py', 'b', None)) == [InputOutput(Path('a.py'), Path('b/a.py'))]
    assert list(get_input_output_paths('d/a.py', 'b/c.py', 'd')) == [InputOutput(Path('d/a.py'), Path('b/c.py'))]
    assert list(get_input_output_paths('d/a.py', 'b', 'd')) == [InputOutput(Path('d/a.py'), Path('b/a.py'))]

# Generated at 2022-06-14 01:33:53.350763
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('./tests/fixtures/hello1.py', './tests/fixtures/hello1.py.out','./tests/fixtures')) == [InputOutput(Path('./tests/fixtures/hello1.py'), Path('./tests/fixtures/hello1.py.out'))]
    assert list(get_input_output_paths('./tests/fixtures/hello1.py', './tests/fixtures/path','./tests/fixtures')) == [InputOutput(Path('./tests/fixtures/hello1.py'), Path('./tests/fixtures/path/hello1.py'))]

# Generated at 2022-06-14 01:34:02.709827
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'input'
    output = 'output'
    root = 'root'
    input_paths = [
        input_,
        'input/',
        'input/file.py',
        'input/file.py/',
    ]
    output_paths = [
        output,
        'output/',
        'output/file.py',
        'output/file.py/',
    ]


# Generated at 2022-06-14 01:34:12.494126
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import os
    # test when output directory doesn't end with .py
    # and input file is a single python file
    output_dir = "test_get_input_output_paths_1"
    input_file = "test_files/test_get_input_output_paths_1/test_1.py"
    root_dir = os.getcwd()
    result = get_input_output_paths(input_file, output_dir, root_dir)
    assert next(result) == InputOutput(Path(input_file), Path(output_dir + "/test_1.py"))

    # test when input and output are both python files
    output_file = "test_files/test_get_input_output_paths_2/test_2.py"

# Generated at 2022-06-14 01:34:27.581519
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    root = Path("/home/foo/bar")

    paths = list(get_input_output_paths("foobar.py", "foobar.py", str(root)))
    assert paths == [
        InputOutput(Path("foobar.py"), Path("foobar.py")),
    ]

    paths = list(get_input_output_paths("/home/foo/bar/foobar.py", "foobar-output.py", str(root)))
    assert paths == [
        InputOutput(Path("/home/foo/bar/foobar.py"), Path("foobar-output.py")),
    ]

    paths = list(get_input_output_paths("/home/foo/bar/foobar.py", "foobar-output", str(root)))

# Generated at 2022-06-14 01:34:36.487033
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import tempfile
    import shutil


# Generated at 2022-06-14 01:34:50.022899
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    # normal use cases
    list_paths = list(get_input_output_paths('input', 'output', None))
    assert(len(list_paths) == 4)
    assert(list_paths[0].input_path.name == 'a.py')
    assert(list_paths[0].output_path.name == 'a.py')
    assert(list_paths[1].input_path.name == 'b.py')
    assert(list_paths[1].output_path.name == 'b.py')
    assert(list_paths[2].input_path.name == 'c.py')
    assert(list_paths[2].output_path.name == 'c.py')

# Generated at 2022-06-14 01:34:56.927065
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
  import pytest
  res = []
  with pytest.raises(InvalidInputOutput):
    res = list(get_input_output_paths("", "", None))
  with pytest.raises(InputDoesntExists):
    res = list(get_input_output_paths("", "", None))
  assert len(res) == 0

# Generated at 2022-06-14 01:35:06.331419
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:35:18.173938
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
        # input: file, output: file
        input_ = '/tmp/a.py'
        output = '/tmp/b.py'
        assert [InputOutput(Path(input_), Path(output))] == list(get_input_output_paths(input_, output, None))

        # input: file, output: directory
        input_ = '/tmp/a.py'
        output = '/tmp/b'
        assert [InputOutput(Path(input_), Path(output) / 'a.py')] == \
               list(get_input_output_paths(input_, output, None))

        # input: file, output: directory
        input_ = '/tmp/a.py'
        output = '/tmp/b'

# Generated at 2022-06-14 01:35:25.251220
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # case: wrong input output pair
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('a.py', 'b.txt', '.'))
    # case: file doesn't exist
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('a.py', '.', '.'))
    # case: input is a file
    # expected: returns [(input_path, output_path)]
    input_path = Path('a.py')
    output_path = Path('b.py')
    assert list(get_input_output_paths('a.py', 'b.py', '')) \
        == [(input_path, output_path)]
    # case: input is a directory and has no root
    # expected: returns [(

# Generated at 2022-06-14 01:35:36.785986
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    from pathlib import Path

    # Testing when input is a file
    file_input_outputs_list = [InputOutput(Path("test_data/test_roots/test_root_1/test_file.py"), Path("test_data/test_roots/test1.py"))]

    assert file_input_outputs_list == list(get_input_output_paths("test_data/test_roots/test_root_1/test_file.py","test_data/test_roots/test1.py",None))
    assert file_input_outputs_list == list(get_input_output_paths("test_data/test_roots/test_root_1/test_file.py","test_data/test_roots/test1.py","test_data/test_roots"))

    # Testing when input is a directory

# Generated at 2022-06-14 01:35:46.021832
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # imports
    from neatpy.exceptions import InputDoesntExists
    from neatpy.exceptions import InvalidInputOutput

    # tests
    # valid input/output
    input_ = 'test_data/test_input'
    output = 'test_data/test_output'

    assert get_input_output_paths(input_, output, None)

    output = 'test_data/test_output/'

    assert get_input_output_paths(input_, output, None)

    input_ = 'test_data/test_input/a.py'
    output = 'test_data/test_output/'

    assert get_input_output_paths(input_, output, None)

    input_ = 'test_data/test_input/a.py'

# Generated at 2022-06-14 01:35:57.601652
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest
    assert list(get_input_output_paths('a.py', 'b', None)) == \
        [InputOutput(Path('a.py'), Path('b/a.py'))]
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('aaaaaaaaa.py', 'b', None))
    assert list(get_input_output_paths('a', 'b', '../')) == \
        [InputOutput(Path('a/a.py'), Path('b/a.py'))]
    assert list(get_input_output_paths('a', 'b', None)) == \
        [InputOutput(Path('a/a.py'), Path('b/a.py'))]

# Generated at 2022-06-14 01:36:01.828045
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('test/test.py', 'test/test_out.py', None)
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('test/test_in.py', 'test/test_out', None)
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('test/test_in', 'test/test_out.py', None)
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('test/test_in', 'test/test_out', None)

# Generated at 2022-06-14 01:36:08.865443
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    from .test_utils import assert_equal
    cases = [
        (('foo/in.py', 'out.py', 'foo'), [('foo/in.py', 'out.py')]),
        (('foo', 'bar', 'foo'), [('foo/a.py', 'bar/a.py'), ('foo/b.py', 'bar/b.py')]),
        (('foo', 'bar', None), [('foo/a.py', 'bar/a.py'), ('foo/b.py', 'bar/b.py')]),
    ]
    data_dir = Path(__file__).parent.parent / 'data'

# Generated at 2022-06-14 01:36:21.010700
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert (
        list(get_input_output_paths(
            input_='path/to/input.py',
            output='path/to/output.py',
            root=None))
        == [InputOutput(Path('path/to/input.py'),
                        Path('path/to/output.py'))])
    assert (
        list(get_input_output_paths(
            input_='path/to/input/',
            output='path/to/output/',
            root=None))
        == [InputOutput(Path('path/to/input/file.py'),
                        Path('path/to/output/file.py'))])

# Generated at 2022-06-14 01:36:29.571245
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .types import InputOutput
    io_pairs = get_input_output_paths(
        'tests/resource/in_folder',
        'tests/resource/out_folder',
        'tests/resource/in_folder'
    )
    
    for pair in io_pairs:
        assert isinstance(pair, InputOutput)
        assert pair.input_path.exists()
        assert not pair.output_path.exists()
    
    io_pairs = get_input_output_paths(
        'tests/resource/in_folder',
        'tests/resource/out_folder',
    )
    for pair in io_pairs:
        assert isinstance(pair, InputOutput)
        assert pair.input_path.exists()
        assert not pair.output_path.exists()

    io

# Generated at 2022-06-14 01:36:33.930320
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    iop = get_input_output_paths('test/test.py', 'output/test.py', 'test')
    for i, o in iop:
        assert str(i) == 'test/test.py'
        assert str(o) == 'output/test.py'

# Generated at 2022-06-14 01:36:41.758096
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('test/input.py', 'test/output.py', None)) == \
        [InputOutput(Path('test/input.py'), Path('test/output.py'))]
    assert list(get_input_output_paths('test/input.py', 'test/output', None)) == \
        [InputOutput(Path('test/input.py'), Path('test/output/input.py'))]
    assert list(get_input_output_paths('test/input/a.py', 'test/output', None)) == \
        [InputOutput(Path('test/input/a.py'), Path('test/output/input/a.py'))]

# Generated at 2022-06-14 01:36:47.956958
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test the input output path function."""
    result = list(get_input_output_paths(
        input_='./tests/sample_1', output='./tests/out'))
    expected = [
        InputOutput(
            Path('./tests/sample_1/example.py'),
            Path('./tests/out/example.py')
        ),
        InputOutput(
            Path('./tests/sample_1/sub_folder/sample.py'),
            Path('./tests/out/sub_folder/sample.py')
        ),
        InputOutput(
            Path('./tests/sample_1/sub_folder/sub_sub_folder/another.py'),
            Path('./tests/out/sub_folder/sub_sub_folder/another.py')
        )
    ]
   

# Generated at 2022-06-14 01:36:57.386880
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from more_itertools import pairwise
    from .exceptions import InvalidInputOutput, InputDoesntExists

    def test_cases(cases):
        def case(input_, output, root=None):
            return InputOutput(Path(input_), Path(output))

        for input_, output, root, expected in cases:
            actual = list(get_input_output_paths(input_, output, root))
            assert actual == expected

    # Check InputDoesntExists
    try:
        list(get_input_output_paths('foo', 'bar', None))
    except InputDoesntExists:
        pass
    else:
        assert False

    # Check InvalidInputOutput

# Generated at 2022-06-14 01:37:05.327510
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('a', 'b', '.')) == [InputOutput(Path('a'), Path('b'))]
    assert list(get_input_output_paths('a.py', 'b.py', '.')) == [
        InputOutput(Path('a.py'), Path('b.py'))
    ]
    assert list(get_input_output_paths('a.py', 'b', '.')) == [
        InputOutput(Path('a.py'), Path('b/a.py'))
    ]

# Generated at 2022-06-14 01:37:12.808913
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test Input Output Paths Pairs."""
    # Input Output is valid, with same name
    input_ = 'main/__init__.py'
    output = 'main'
    result = get_input_output_paths(input_, output, None)
    expected_result = [InputOutput(Path(input_), Path(output + '/__init__.py'))]
    assert isinstance(result, list)
    assert len(result) == len(expected_result)
    assert result == expected_result
    
    
    # Input Output is not valid
    input_ = 'main/__init__.py'
    output = '__init__.py'
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths(input_, output, None)


    # Input doesn't exist

# Generated at 2022-06-14 01:37:19.746883
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'share/bin/python'
    output = 'share/bin/python'
    root = None
    result = list(get_input_output_paths(input_, output, root))
    assert len(result) == 1
    assert result[0].input.name == 'python'
    assert result[0].output.name == 'python'
    assert str(result[0].input) == 'share/bin/python'
    assert str(result[0].output) == 'share/bin/python'

    input_ = 'share/bin'
    output = 'share/bin'
    root = None
    result = list(get_input_output_paths(input_, output, root))
    assert len(result) == 2
    assert result[0].input.name == 'python'

# Generated at 2022-06-14 01:37:21.137409
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert get_input_output_paths('.', 'output', None)

# Generated at 2022-06-14 01:37:32.368409
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_path = 'tests/code'
    output_path = 'tests/converted'
    input_outputs = list(get_input_output_paths(input_path, output_path, None))
    assert len(input_outputs) == 3
    assert Path(input_outputs[0].input_path) == Path(input_path).joinpath('test.py')
    assert Path(input_outputs[0].output_path) == Path(output_path).joinpath('test.py')
    assert Path(input_outputs[1].input_path) == Path(input_path).joinpath('test1/test.py')
    assert Path(input_outputs[1].output_path) == Path(output_path).joinpath('test1').joinpath('test.py')

# Generated at 2022-06-14 01:37:46.164549
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .utils import get_input_output_paths
    from pathlib import Path

    assert list(get_input_output_paths('a.py', 'b.py', '.')) == [
        InputOutput(Path('a.py'), Path('b.py'))]
    assert list(get_input_output_paths('a.py', 'b', '.')) == [
        InputOutput(Path('a.py'), Path('b/a.py'))]
    assert list(get_input_output_paths('a', 'b.py', '.')) == [
        InputOutput(Path('a/a.py'), Path('b.py'))]

# Generated at 2022-06-14 01:38:01.058226
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from .exceptions import InvalidInputOutput, InputDoesntExists

    # mode 1
    for iop in get_input_output_paths('example', 'example/copy', root=None):
        assert Path('./example/sample.py').samefile(iop.input_path)
        assert Path('./example/copy/sample.py').samefile(iop.output_path)

    # mode 2
    for iop in get_input_output_paths('example/sample.py', '.', root=None):
        assert Path('./example/sample.py').samefile(iop.input_path)
        assert Path('./sample.py').samefile(iop.output_path)

    # mode 3

# Generated at 2022-06-14 01:38:08.816092
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths."""

# Generated at 2022-06-14 01:38:16.529596
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    path_pairs = get_input_output_paths("./tests/data/input1", "./tests/output/", "./tests/data/input1")
    assert len(list(path_pairs)) == 1
    assert path_pairs.__next__() == InputOutput(Path("./tests/data/input1/test.py"), Path("./tests/output/test.py"))

# Generated at 2022-06-14 01:38:24.650851
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths function."""
    from pathlib import Path
    import pytest

    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('foo.py', 'foo', 'root'))

    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('foo.py', 'bar.py', 'root'))

    # when input is file, output is file
    assert list(get_input_output_paths('foo.py', 'bar.py', 'root')) == [
        InputOutput(Path('foo.py'), Path('bar.py'))]

    # when input is file, output is dir

# Generated at 2022-06-14 01:38:32.215673
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    from .exceptions import InvalidInputOutput, InputDoesntExists

    input_ = 'test/input/'
    output = 'test/output/'

    for input_output in get_input_output_paths(input_, output, None):
        assert input_output.input_path.exists()
        assert not input_output.output_path.exists()

    input_ = 'test/input/one_file.py'
    output = 'test/output/'

    for input_output in get_input_output_paths(input_, output, None):
        assert input_output.input_path.exists()
        assert not input_output.output_path.exists()

    input_ = 'test/input/'

# Generated at 2022-06-14 01:38:38.498284
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'test_project/test_module.py'
    output = 'test_project/test_output'
    inputoutputpaths = get_input_output_paths(input_, output, root=None)
    inputoutputpaths = list(inputoutputpaths)
    assert len(inputoutputpaths) == 1
    input_path, output_path = iter(inputoutputpaths).__next__()
    assert input_path == Path(input_)
    assert output_path == Path(output).joinpath(Path(input_).name)

    output = 'test_project/.coveragerc'
    inputoutputpaths = get_input_output_paths(input_, output, root=None)
    inputoutputpaths = list(inputoutputpaths)
    assert len(inputoutputpaths) == 1
   

# Generated at 2022-06-14 01:38:48.225932
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test 1: Input and Output are both directories
    input_ = "./example/functions"
    output = "./example/output"
    root = None
    for i in get_input_output_paths(input_, output, root):
        assert i.input == Path("./example/functions/def_and_lambda.py")
        assert i.output == Path("./example/output/def_and_lambda.py")
        break
    
    # Test 2: Input is directory, output is file
    input_ = "./example/functions"
    output = "./example/output/def_and_lambda.py"
    root = None

# Generated at 2022-06-14 01:38:57.290448
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    # Source: https://github.com/pycqa/flake8/blob/master/src/flake8/main/cli.py
    # Input:
    #     cwd = /home/user/pytest-test
    #     input_ = pytest-test/subdir/subsubdir/file.py
    #     output = pytest-test/output
    #     root = None
    cwd = Path(__file__).parent.parent
    input_ = cwd.joinpath('subdir', 'subsubdir', 'file.py')
    output = cwd.joinpath('output')
    root = None
    expected_result = [Path(input_), Path(output.joinpath('subdir', 'subsubdir', 'file.py'))]

# Generated at 2022-06-14 01:39:14.917786
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Imports
    import shutil
    import tempfile

    # Constants
    ROOT = Path("my_root")
    OUTPUT = Path("my_output")

    # Create temp file
    tempdir = tempfile.mkdtemp()
    temp_input_path = Path(tempdir, "my_input.py")
    temp_input_path.write_text("input")
    temp_output_path = Path(tempdir, "my_output.py")
    temp_output_path.write_text("output")

    # Test for input file and output file
    paths = list(get_input_output_paths(
        input_=temp_input_path.as_posix(),
        output=temp_output_path.as_posix(),
        root=None,
    ))

# Generated at 2022-06-14 01:39:26.395671
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from .types import InputOutput
    import tempfile, inspect, os
    def test_case(input, output, root):
        for i, o in get_input_output_paths(input, output, root):
            print(i, o)
    test_case('', '', None)
    test_case('a.py', '', None)
    test_case('a.py', '', '.')
    test_case('a.py', 'b.py', None)
    test_case('a.py', 'b', None)
    test_case('a.py', 'b', '.')
    test_case('a.py', 'b', '/')
    test_case('a.py', 'b', '/usr')

# Generated at 2022-06-14 01:39:35.917327
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test setting valid paths
    paths = get_input_output_paths(input_='./foo/bar/baz.py',
                                   output='./foo/bar/baz.py',
                                   root=None)
    assert next(paths) == InputOutput(
        Path('./foo/bar/baz.py'),
        Path('./foo/bar/baz.py')
    )

    # test setting valid paths
    paths = get_input_output_paths(input_='./foo/bar/baz.py',
                                   output='./out/dir',
                                   root=None)
    assert next(paths) == InputOutput(
        Path('./foo/bar/baz.py'),
        Path('./out/dir/baz.py')
    )



# Generated at 2022-06-14 01:39:47.242270
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    
    # This is test case1, testing the case where input is a path to a file and output is a directory.
    input_ = 'test_dir1/test_dir2/test_dir3/a.py'
    output = 'test_dir4/test_dir5'
    output_path = Path(output).joinpath(Path(input_).name)
    input_output = InputOutput(Path(input_), output_path)
    assert(next(get_input_output_paths(input_, output, None)) == input_output)
    # This is test case2, testing the case where input is a directory and output is a directory.
    input_ = 'test_dir1/test_dir2/test_dir3'
    output = 'test_dir4/test_dir5'
    input_output1 = Input

# Generated at 2022-06-14 01:39:56.025072
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_input_output_paths = [
        InputOutput(Path(__file__), Path('tmp/test_inputoutput.py')),
        InputOutput(Path(__file__), Path('/tmp/test_inputoutput.py')),
        InputOutput(Path('tmp/test.py'), Path('tmp/test_inputoutput.py')),
        InputOutput(Path('tmp/test.py'), Path('/tmp/test_inputoutput.py')),
        InputOutput(Path('tmp/test.py'), Path('/tmp')),
        InputOutput(Path('tmp/test.py'), Path('.')),
        InputOutput(Path('tmp/test.py'), Path('/tmp/test.py'))
    ]
    for test in test_input_output_paths:
        test_input = str(test.input)
       

# Generated at 2022-06-14 01:40:06.532639
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # create directory path
    dir_path = 'test_folder'
    # create file paths
    file_paths = ['test1.py', 'test2.py', 'test3.py', 'test4.py', 'test5.py']
    for file_path in file_paths:
        file_path = Path(dir_path).joinpath(file_path)
        file_path.touch()
    # create expected output
    exp_output = list()
    for file_path in file_paths:
        input_path = Path(dir_path).joinpath(file_path)
        output_path = Path(dir_path).joinpath(file_path)
        exp_output.append(InputOutput(input_path, output_path))
    # get output

# Generated at 2022-06-14 01:40:16.172363
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Given
    root = 'root'

    input_output = (
        ('foo.py', 'bar.py', ('foo.py', 'bar.py')),
        ('foo.py', 'out', ('root/foo.py', 'root/out/foo.py')),
        ('foo', 'out', ('root/foo.py', 'root/out/foo.py')),
        ('foo', 'out/bar', ('root/foo.py', 'root/out/bar/foo.py')),
        ('foo', 'out/bar.py', ('root/foo.py', 'root/out/bar.py')),
    )

    # When/Then
    for input_, output, paths in input_output:
        input_path, output_path = paths

# Generated at 2022-06-14 01:40:25.403585
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # test input_ and output_ in the same folder
    input_ = './test/sub_dir/subfile.py'
    output = './output/'
    root = './test/'
    expected_input = './test/sub_dir/subfile.py'
    expected_output = './output/sub_dir/subfile.py'
    result = list(get_input_output_paths(input_, output, root))
    assert len(result) == 1
    assert result[0].input_path == Path(expected_input)
    assert result[0].output_path == Path(expected_output)

    # test input_ and output_ in the different folders
    input_ = './test/sub_dir/subfile.py'
    output = './output/'
    root = ''
    expected

# Generated at 2022-06-14 01:40:38.642752
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from unittest import TestCase

    class Test(TestCase):
        def test_output_doesnot_endwith_py(self):
            with self.assertRaises(InvalidInputOutput):
                get_input_output_paths('a.py', 'b', '.')

        def test_input_doesnot_exist(self):
            with self.assertRaises(InputDoesntExists):
                get_input_output_paths('a.py', 'b.py', '.')


# Generated at 2022-06-14 01:40:50.109530
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert (list(get_input_output_paths('./tests/example',
                                        './test-output',
                                        './tests/example'))
            == [InputOutput(
                    Path('./tests/example/example.py'),
                    Path('./test-output/example.py'))])
    assert (list(get_input_output_paths('./tests/example',
                                        './test-output',
                                        None))
            == [InputOutput(
                    Path('./tests/example/example.py'),
                    Path('./test-output/example.py'))])

# Generated at 2022-06-14 01:41:14.989606
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # case 1
    assert get_input_output_paths('fixtures/input/empty.py',
                                  'fixtures/output/empty.py',
                                  None) == InputOutput(
                                      Path('fixtures/input/empty.py'),
                                      Path('fixtures/output/empty.py'))

    # case 2
    assert get_input_output_paths('fixtures/input/empty.py',
                                  'fixtures/output',
                                  None) == InputOutput(
                                      Path('fixtures/input/empty.py'),
                                      Path('fixtures/output/empty.py'))

    # case 3

# Generated at 2022-06-14 01:41:22.259528
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Get input/output paths pairs."""

    assert get_input_output_paths('test.py', 'out.py', '') == \
           [InputOutput(Path('test.py'), Path('out.py'))]
    assert get_input_output_paths('test.py', 'out', '') == \
           [InputOutput(Path('test.py'), Path('out/test.py'))]
    assert get_input_output_paths('test', 'out', '') == \
           [InputOutput(Path('test/test.py'), Path('out/test.py'))]
    assert get_input_output_paths('test', 'out', 'test') == \
           [InputOutput(Path('test/test.py'), Path('out/test.py'))]
    assert get_input_output

# Generated at 2022-06-14 01:41:32.193228
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    cases = [
        ('foo.py', 'bar.py'),
        ('foo.py', 'bar/bar.py'),
        ('foo/foo.py', 'bar.py'),
        ('foo/foo.py', 'bar/bar.py')
    ]

    for case in cases:
        input_, output = case
        assert list(get_input_output_paths(input_, output, None)) == [InputOutput(Path(input_), Path(output))]

    cases = [
        ('foo', 'bar.py'),
        ('foo', 'bar/bar.py'),
        ('foo/foo', 'bar.py'),
        ('foo/foo', 'bar/bar.py')
    ]

    for case in cases:
        input_, output = case

# Generated at 2022-06-14 01:41:48.076917
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    paths = list(get_input_output_paths('a/b.py', 'c/d.py', None))
    assert paths == [InputOutput(Path('a/b.py'), Path('c/d.py'))]

    paths = list(get_input_output_paths('a/b.py', 'c', None))
    assert paths == [InputOutput(Path('a/b.py'), Path('c/b.py'))]
    paths = list(get_input_output_paths('a/b.py', 'c', 'a'))
    assert paths == [InputOutput(Path('a/b.py'), Path('c/b.py'))]
    paths = list(get_input_output_paths('a/b.py', 'c', 'a/b'))

# Generated at 2022-06-14 01:41:55.016879
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test to see if paths are working correctly"""
    #basic file to file test
    assert list(get_input_output_paths('test_py2const.py', 'output.py', None)) == \
        [InputOutput(Path('test_py2const.py'), Path('output.py'))]

    #basic folder to file test
    assert list(get_input_output_paths('test_py2const', 'output.py', None)) == \
        [InputOutput(Path('test_py2const'), Path('output.py/test_py2const'))]

    #basic folder to folder test

# Generated at 2022-06-14 01:42:05.718810
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('test/test_input', 'test/test_output', None)) == [
        InputOutput(Path('test/test_input/test.py'), Path('test/test_output/test.py')),
        InputOutput(Path('test/test_input/test1.py'), Path('test/test_output/test1.py')),
        InputOutput(Path('test/test_input/test2.py'), Path('test/test_output/test2.py')),
        InputOutput(Path('test/test_input/dir/dir.py'), Path('test/test_output/dir/dir.py'))
    ]

# Generated at 2022-06-14 01:42:16.017644
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .helpers import rmtree
    from .exceptions import InvalidInputOutput
    from tempfile import mkdtemp

    input_1 = mkdtemp()
    input_2 = mkdtemp()
    output_1 = mkdtemp()
    output_2 = mkdtemp()

    def mock_input_outputs(input_, output, root=None):
        return input_, output, root

    def mock_input_outputs_error(input_, output, root=None):
        raise InvalidInputOutput


# Generated at 2022-06-14 01:42:24.026948
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths(input_='test.py', output='./test/test.py', root=None)) ==\
        [InputOutput(Path('test.py'), Path('./test/test.py'))]
    assert list(get_input_output_paths(input_='test', output='./test/test.py', root=None)) ==\
        [InputOutput(Path('test'), Path('./test/test.py'))]
    assert list(get_input_output_paths(input_='test', output='./test', root=None)) ==\
        [InputOutput(Path('test'), Path('./test'))]

# Generated at 2022-06-14 01:42:35.351153
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    ios = list(get_input_output_paths("tests/example1", "tests/output", "tests"))
    assert len(ios) == 3
    ios = list(get_input_output_paths("tests/example1", "tests/output", None))
    assert len(ios) == 3
    ios = list(get_input_output_paths("tests/example1/foo.py", "tests/output/foo.py", "tests"))
    assert len(ios) == 1
    ios = list(get_input_output_paths("tests/example1/foo.py", "tests/output/foo.py", None))
    assert len(ios) == 1

# Generated at 2022-06-14 01:42:41.451263
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    input_ = "path"
    output = "path2"
    root = "root"
    input_output = InputOutput('path', 'path2')
    assert get_input_output_paths(input_, output, root) == input_output
