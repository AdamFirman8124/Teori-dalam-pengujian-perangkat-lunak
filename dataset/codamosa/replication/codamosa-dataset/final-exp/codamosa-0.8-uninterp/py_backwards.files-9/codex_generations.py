

# Generated at 2022-06-14 01:33:03.893687
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .types import InputOutput
    from pathlib import Path
    from os.path import join

    examples = [
        ('a.py', 'b.py', None),
        ('a', 'b', None),
        ('a', 'b.py', None),
        ('a.py', 'b', None),
        ('a.py', 'b', 'root'),
        ('root/a.py', 'b', 'root'),
        ('root/a', 'b', 'root'),
        ('root/a', 'b.py', 'root'),
        ('root/a.py', 'b', 'root'),
    ]

# Generated at 2022-06-14 01:33:14.850051
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from .types import InputOutput

    def assert_get_input_output_paths_raises(input_: str, output: str, root: str, exception):
        try:
            for i in get_input_output_paths(input_, output, root):
                assert False
        except exception:
            pass

    # Test exceptions
    #   .py input requires .py output
    assert_get_input_output_paths_raises("input.py", "output.txt", None, InvalidInputOutput)

    #   input file must exist
    assert_get_input_output_paths_raises("input_does_not_exist.py", "output", None,
                                         InputDoesntExists)

    # Test singular files
    #   input.py output.py
    assert get_

# Generated at 2022-06-14 01:33:21.715158
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from tempfile import TemporaryDirectory
    from os import path

    with TemporaryDirectory() as tempdir:
        tmp = path.join(tempdir, 'tmp')
        test1 = path.join(tempdir, 'test1')
        test1_1 = path.join(test1, 'test1_1.py')
        test2 = path.join(tempdir, 'test2.py')
        test3 = path.join(tempdir, 'test3.py')

        Path(tmp).mkdir()

        Path(test2).touch()
        Path(test3).touch()
        Path(test1_1).touch()

        # Empty folder as input
        for ifiles, ofiles in get_input_output_paths(tmp, tmp, root=tempdir):
            assert False

        # One file as input and output

# Generated at 2022-06-14 01:33:33.158269
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths(
        './test.py', './test2.py', root='.')) == [
        InputOutput(Path('./test.py'), Path('./test2.py'))]
    assert list(get_input_output_paths(
        './test.py', './test2', root='.')) == [
        InputOutput(Path('./test.py'), Path('./test2/test.py'))]
    assert list(get_input_output_paths(
        './test/', './test2', root='.')) == [
        InputOutput(Path('./test/test.py'), Path('./test2/test.py'))]

# Generated at 2022-06-14 01:33:43.932307
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Make a directory and file, then delete afterwards
    import pytest
    import os
    test_dir = "tests/test_get_input_output_paths"
    test_dir_file = os.path.join(test_dir, "temp.py")
    test_file = "temp.py"
    test_dir_file_output = test_dir + "/temp_out.py"
    os.mkdir(test_dir)
    with open(test_dir_file, "w") as f:
        f.write("tests")

# Generated at 2022-06-14 01:33:52.589395
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pytest import raises

    with raises(InvalidInputOutput):
        list(get_input_output_paths('foo', 'bar.py', None))

    with raises(InputDoesntExists):
        list(get_input_output_paths('foo', 'bar', None))

    io = list(get_input_output_paths('foo.py', 'bar.py', '.'))
    assert io[0].input_ == Path('foo.py')
    assert io[0].output == Path('bar.py')

    io = list(get_input_output_paths('foo', 'bar.py', '.'))
    assert io[0].input_ == Path('foo')
    assert io[0].output == Path('bar.py')


# Generated at 2022-06-14 01:34:02.193764
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output = get_input_output_paths('test_data/test1.py','test_data/test1.py', None)
    # print(type(input_output))
    # print(input_output)
    assert type(input_output) == tuple
    print(input_output[0])
    print(type(input_output[0]))
    assert type(input_output[0]) == InputOutput
    print(input_output[0].input_path)
    print(input_output[0].input_path.parent)
    assert input_output[0].input_path.name == 'test1.py'
    assert input_output[0].input_path.parent.name == 'test_data'
    assert input_output[0].output_path.name == 'test1.py'

# Generated at 2022-06-14 01:34:12.077270
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    res = list(get_input_output_paths('foo', '.', None))
    assert len(res) == 1
    assert res[0].input_path == Path('foo')
    assert res[0].output_path == Path('foo')
    res = list(get_input_output_paths('foo.py', '.', None))
    assert len(res) == 1
    assert res[0].input_path == Path('foo.py')
    assert res[0].output_path == Path('foo.py')
    res = list(get_input_output_paths('foo', 'bar', None))
    assert len(res) == 1
    assert res[0].input_path == Path('foo')
    assert res[0].output_

# Generated at 2022-06-14 01:34:27.140444
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    paths = get_input_output_paths("../tests/input.py", "../tests/output.py", None)
    assert next(paths).input_path.name == "input.py"
    assert next(paths).output_path.name == "output.py"

    paths = get_input_output_paths("../tests/input.py", "../tests/output/", None)
    assert next(paths).input_path.name == "input.py"
    assert next(paths).output_path.name == "input.py"

    paths = get_input_output_paths("../tests/input.py", "../tests/output/", "../tests")
    assert next(paths).input_path.name == "input.py"

# Generated at 2022-06-14 01:34:27.993850
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # todo assert raises
    pass

# Generated at 2022-06-14 01:34:39.917955
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import tempfile
    import shutil
    import os
    import pytest
    from pathlib import Path
    from .exceptions import InputDoesntExists, InvalidInputOutput

    input_root = tempfile.mkdtemp()
    output_root = tempfile.mkdtemp()

    target_py = Path(input_root).joinpath('a', 'b', 'target.py')
    target_py.parent.mkdir(parents=True)
    target_py.touch()

    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('this/path/doesnt/exists', 'output', None))

    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths(input_root, output_root, None))

    io = list

# Generated at 2022-06-14 01:34:50.538318
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    path = Path().cwd()
    assert list(get_input_output_paths(str(path), 'output.py', None)) == [InputOutput(path.joinpath('output.py'), path.joinpath('output.py'))]
    assert list(get_input_output_paths(str(path.joinpath('output.py')), 'output.py', None)) == [InputOutput(path.joinpath('output.py'), path.joinpath('output.py'))]
    # 2
    assert list(get_input_output_paths(str(path), 'output.py', str(path.joinpath('input')))) == [InputOutput(path.joinpath('output.py'), path.joinpath('output.py'))]

# Generated at 2022-06-14 01:34:58.285801
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import tempfile
    import shutil
    import os

    src_dir = tempfile.mkdtemp()
    target_dir = tempfile.mkdtemp()
    target_dir_name = os.path.basename(target_dir)
    child_dir_name = "child"
    child_dir = os.path.join(src_dir, child_dir_name)
    os.mkdir(child_dir)
    src_file_name = os.path.join(target_dir_name, "src.py")
    os.makedirs(os.path.join(src_dir, target_dir_name))
    with open(os.path.join(src_dir, src_file_name), 'w') as f:
        f.write("test")
    child_file_name = "child.py"

# Generated at 2022-06-14 01:35:06.844569
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    try:
        input_ = './test/test_input'
        output = './test/test_output'
        root = './test/test_input'
        paths = get_input_output_paths(input_, output, root)
        paths = tuple(paths)

        assert all(not p.output.exists() for p in paths)
        for p in paths:
            p.output.parent.mkdir(parents=True, exist_ok=True)
            p.output.touch()

        assert all(p.output.exists() for p in paths)
    finally:
        for p in paths:
            p.output.unlink()
            p.output.parent.rmdir()

# Generated at 2022-06-14 01:35:18.522976
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "/home/dohia/some_folder/some_name.py"
    output = "/home/dohia/some_folder/output"
    root = "/home/dohia/some_folder"
    result = get_input_output_paths(input_, output, root)
    assert list(result)[0].input == Path(input_)
    assert list(result)[0].output == Path(output).joinpath("some_name.py")

    input_ = "/home/dohia/some_folder/"
    output = "/home/dohia/some_folder/output"
    root = None
    result = get_input_output_paths(input_, output, root)

# Generated at 2022-06-14 01:35:29.920727
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert get_input_output_paths('in.py', 'out.py', None) == [InputOutput(Path('in.py'), Path('out.py'))]
    assert get_input_output_paths('dummy.py', 'out', None) == [InputOutput(Path('dummy.py'), Path('out','dummy.py'))]
    assert get_input_output_paths('.', 'out/', None) == [InputOutput(Path('dummy.py'), Path('out/dummy.py'))]
    assert get_input_output_paths('.', 'out/', '.') == [InputOutput(Path('dummy.py'), Path('out/dummy.py'))]

# Generated at 2022-06-14 01:35:38.710888
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('./', './out', './')) == \
            [InputOutput(Path('./__init__.py'), Path('./out/__init__.py')),
             InputOutput(Path('./conftest.py'), Path('./out/conftest.py')),
             InputOutput(Path('./test_get_input_output_paths.py'),
                         Path('./out/test_get_input_output_paths.py'))]

# Generated at 2022-06-14 01:35:49.733727
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths("tests/data/test_a", "tests/data/output_a")) == [InputOutput(Path("tests/data/test_a/test_a.py"), Path("tests/data/output_a/test_a.py"))]
    assert list(get_input_output_paths("tests/data/test_b", "tests/data/output_b")) == [InputOutput(Path("tests/data/test_b/test_b.py"), Path("tests/data/output_b/test_b.py"))]

# Generated at 2022-06-14 01:36:04.845453
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pytest import raises
    from test.test_paths import get_path

    # Function with invalid input/output raises exception
    with raises(InvalidInputOutput):
        list(get_input_output_paths('path', 'path.py', ''))

    # Function with input that doesn't exists raises exception
    with raises(InputDoesntExists):
        list(get_input_output_paths('path', 'new_path', ''))

    # Function returns input/output pairs
    input_path = get_path('test.py')
    output_path = get_path('test_new.py')
    in_out = list(get_input_output_paths(input_path, output_path, ''))
    assert len(in_out) == 1
    assert in_out[0].input == input_path
   

# Generated at 2022-06-14 01:36:07.566653
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pytest import raises

    with raises(InvalidInputOutput):
        list(get_input_output_paths('tests/data/example.py', 'test.js', 'tests/data'))


# Generated at 2022-06-14 01:36:29.252108
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths function"""
    from click.testing import CliRunner
    from .cli import lint_files
    import os

    # Test with a directory
    test_dir = 'test_file_dir'
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    test_file = open(os.path.join(test_dir, 'test.py'), 'w')
    test_file.close()
    test_file2 = open(os.path.join(test_dir, 'test2.py'), 'w')
    test_file2.close()
    test_runner = CliRunner()
    result = test_runner.invoke(lint_files, [test_dir])
    assert result.exit_code == 0

    # Test

# Generated at 2022-06-14 01:36:32.017165
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    p = Path(__file__).resolve()
    input_output_paths = get_input_output_paths(p.parent / 'input', p.parent / 'output', None)
    assert list(input_output_paths) == [InputOutput(Path(p.parent / 'input' / 'main.py'), Path(p.parent / 'output' / 'main.py'))]

# Generated at 2022-06-14 01:36:40.341994
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "."
    output = "."
    root = None
    actual = get_input_output_paths(input_, output, root)
    expected = InputOutput(Path("."), Path("."))
    assert actual == expected

    input_ = "test_path.py"
    output = "."
    root = None
    actual = get_input_output_paths(input_, output, root)
    expected = InputOutput(Path("test_path.py"), Path("test_path.py"))
    assert actual == expected

    input_ = "test_path.py"
    output = "test_output"
    root = None
    actual = get_input_output_paths(input_, output, root)

# Generated at 2022-06-14 01:36:43.867355
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    def test_get_input_output_paths_error(*args):
        with pytest.raises(InvalidInputOutput):
            list(get_input_output_paths(*args))

    def test_get_input_output_paths_result(*args):
        assert list(get_input_output_paths(*args))

    test_get_input_output_paths_error('./script.py', './script.py', None)

    test_get_input_output_paths_error('./script.py', './script.json', None)
    test_get_input_output_paths_result('./script.json', './script.py', None)

    test_get_input_output_paths_error('./script.py', './script', None)
    test_get_

# Generated at 2022-06-14 01:36:49.288230
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # First case
    inputs_1 = get_input_output_paths(input_='/home/ashwin/test/test1.py',
                                      output='/home/ashwin/test_output/test1.py',
                                      root=None)
    inputs_2 = get_input_output_paths(input_='/home/ashwin/test/test1.py',
                                      output='/home/ashwin/test_output',
                                      root=None)
    assert inputs_1 == inputs_2

    # Second case
    inputs_1 = get_input_output_paths(input_='/home/ashwin/test',
                                      output='/home/ashwin/test_output',
                                      root=None)

# Generated at 2022-06-14 01:36:56.255144
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_pairs = get_input_output_paths('tests/input', 'tests/output', 'tests/input')
    for pair in input_output_pairs:
        input_ = pair.input_
        output = pair.output
        assert input_.suffix == '.py'
        assert output.suffix == '.py'
        assert input_.name == output.name
        assert input_.parent.resolve() == Path('tests/input').resolve()
        assert output.parent.resolve() == Path('tests/output').resolve()

# Generated at 2022-06-14 01:37:04.897785
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    root = Path(__file__).parent.joinpath('fixtures')
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('non-existing.py', 'output', root))

    pairs = list(get_input_output_paths('file.py', 'output', root))
    assert len(pairs) == 1
    pair = pairs[0]
    assert pair.input.relative_to(root) == Path('file.py')
    assert pair.output.relative_to(root) == Path('output').joinpath('file.py')
    assert pair.input.exists()
    assert not pair.output.exists()


# Generated at 2022-06-14 01:37:12.544996
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('foo.py', 'bar.py', '')) == \
        [InputOutput(Path('foo.py'), Path('bar.py'))]
    assert list(get_input_output_paths('foo.py', 'bar', '')) == \
        [InputOutput(Path('foo.py'), Path('bar/foo.py'))]
    assert list(get_input_output_paths('foo.py', 'bar', 'buzz')) == \
        [InputOutput(Path('foo.py'), Path('bar/foo.py'))]

# Generated at 2022-06-14 01:37:19.597809
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    # Test 1: input: foo.py, output: bar.py
    # >>> get_input_output_paths('foo.py', 'bar.py')
    # [InputOutput(input=PosixPath, output=PosixPath)]
    assert get_input_output_paths('foo.py', 'bar.py', None) == \
        [InputOutput(Path('foo.py'), Path('bar.py'))]

    # Test 2: input: foo.py, output: bar
    # >>> get_input_output_paths('foo.py', 'bar')
    # [InputOutput(input=PosixPath, output=PosixPath)]

# Generated at 2022-06-14 01:37:30.286165
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths."""
    def get_input_output(input_: str, output: str, root: str) -> List[InputOutput]:
        return list(get_input_output_paths(
            input_=input_, output=output, root=root))

    assert get_input_output(
        'foo.py', 'bar.py', None
    ) == [InputOutput(Path('foo.py'), Path('bar.py'))]
    assert get_input_output(
        'foo.py', 'bar', None
    ) == [InputOutput(Path('foo.py'), Path('bar/foo.py'))]

# Generated at 2022-06-14 01:38:05.457297
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from enum import Enum
    from pathlib import Path

    class TestCase(Enum):
        SINGLE_FILE_TO_SINGLE_FILE = (
            'a.py', 'b.py', None, [(Path('a.py'), Path('b.py'))]
        )
        SINGLE_FILE_TO_DIRECTORY = (
            'a.py', 'b', None, [(Path('a.py'), Path('b/a.py'))]
        )
        DIRECTORY_TO_DIRECTORY = (
            'c', 'd', None, [(Path('c/a.py'), Path('d/a.py'))]
        )

# Generated at 2022-06-14 01:38:14.122449
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from tempfile import mkdtemp
    from shutil import rmtree

    input_ = mkdtemp()
    output = mkdtemp()
    for child_input, child_output in get_input_output_paths(input_, output, None):
        assert child_input.endswith('.py')
        assert child_output.parent.name == output.split('/')[-1]

    rmtree(input_)
    rmtree(output)

# Generated at 2022-06-14 01:38:23.876773
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from unittest.mock import patch
    from mypy_boto3_builder.compat import Mock

    with patch('mypy_boto3_builder.input.Path.exists') as exists:
        get_input_output_paths('a', 'b', 'c')

    exists.assert_called_with()

    with patch('mypy_boto3_builder.input.Path.exists', return_value=True):
        with patch('mypy_boto3_builder.input.Path.glob', return_value=['d', 'e']) as glob:
            result = list(get_input_output_paths('a', 'b', 'c'))
            glob.assert_called_with('**/*.py')


# Generated at 2022-06-14 01:38:33.471762
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # case 1 Input/Output is a file, input and output both ends with py
    try:
        pigments = get_input_output_paths('test_folder/a.py', 'test_folder/b.py', None)
        for pigment in pigments:
            assert str(pigment.input) == 'test_folder/a.py'
            assert str(pigment.output) == 'test_folder/b.py'
    except:
        assert 0

    # case 2 Input/Output is a file, input doesn't end with py, output ends with py

# Generated at 2022-06-14 01:38:39.006546
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import tempfile
    from .testing import assert_input_output_paths_equal

    root = tempfile.TemporaryDirectory()
    input_ = root.name


# Generated at 2022-06-14 01:38:48.633280
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import shutil, tempfile, unittest
    class TestFunctions(unittest.TestCase):
        def setUp(self):
            # Create a temporary directory
            self.test_dir = tempfile.mkdtemp()
            # Create a temporary root directory
            self.test_root = tempfile.mkdtemp()
            # Create subdirectories
            for i in range(4):
                new_path = os.path.join(self.test_dir, 'dir_{}'.format(i))
                os.mkdir(new_path)
            # Create python files in subdirectories
            for i in range(4):
                new_path = os.path.join(self.test_dir, 'dir_{}'.format(i), 'file_{}.py'.format(i))
                open(new_path, 'a')

# Generated at 2022-06-14 01:38:56.542772
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for get_input_output_paths."""
    # File to file
    assert list(get_input_output_paths('a.py', 'b.py', None)) == [
            InputOutput(Path('a.py'), Path('b.py'))
            ]

    # File to directory
    assert list(get_input_output_paths('a.py', 'b', None)) == [
            InputOutput(Path('a.py'), Path('b/a.py'))
            ]

    # Directory to directory
    assert list(get_input_output_paths('a', 'b', None)) == [
            InputOutput(Path('a/a.py'), Path('b/a.py'))
            ]

    # Directory to file
    with pytest.raises(InvalidInputOutput):
        list

# Generated at 2022-06-14 01:39:11.713414
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # raise InputDoesntExists when input_ is a folder that doesn't exist
    with pytest.raises(InputDoesntExists):
        get_input_output_paths("missing_folder", "", "")

    # raise InputDoesntExists when input_ is a file that doesn't exist
    with pytest.raises(InputDoesntExists):
        get_input_output_paths("missing_file.py", "", "")

    # raise InvalidInputOutput when input_ doesn't end with '.py' but output
    # does
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths("input_file.txt", "output_file.py", "")

    # return one InputOutput pair when input_ is a file

# Generated at 2022-06-14 01:39:20.194771
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    root = Path(__file__).parent
    inputs = [
        'input/a.py',
        'input/b.py',
        'input/c.py',
        'input/d.py',
        'input/e.py',
        'input/f.py'
    ]
    outputs = [
        'output/a.py',
        'output/b.py',
        'output/c.py',
        'output/1/a.py',
        'output/2/b.py',
        'output/2/c.py',
        'output/3/d.py'
    ]

    input_output = get_input_output_paths(input_=inputs[0],
                                          output=outputs[0],
                                          root=root)

# Generated at 2022-06-14 01:39:30.372560
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    import os
    import shutil
    from distutils.dir_util import copy_tree

    root = os.path.join(os.getcwd(), 'test_data')

    # ************************
    # Input is file, output is file
    # ************************
    input_ = os.path.join(root, 'in_1.py')
    output= os.path.join(root, 'out_1.py')
    result = list(get_input_output_paths(input_, output, None))
    assert len(result) == 1
    assert result[0] == InputOutput(Path(input_), Path(output))

    # ************************
    # Input is file, output is directory
    # ************************
    input_ = os.path

# Generated at 2022-06-14 01:40:31.531468
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths function."""
    # Normal use
    result = get_input_output_paths("inputdir", "outputdir", "inputdir")
    assert len(list(result)) == 3

    # Output format error
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths("inputdir/file1.py", "outputdir.py", "inputdir")

    # Input file does not exist
    with pytest.raises(InputDoesntExists):
        get_input_output_paths("inputdir/file1.py", "outputdir.py", "inputdir")

# Generated at 2022-06-14 01:40:40.276103
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for get_input_output_paths."""
    assert list(get_input_output_paths('input.py', 'output.py', None)) == \
        [InputOutput(Path('input.py'), Path('output.py'))]

    assert list(get_input_output_paths('input.py', 'output', None)) == \
        [InputOutput(Path('input.py'), Path('output/input.py'))]

    assert list(get_input_output_paths('root', 'output', 'root')) == \
        [InputOutput(Path('root/a.py'), Path('output/a.py')),
         InputOutput(Path('root/b.py'), Path('output/b.py'))]



# Generated at 2022-06-14 01:40:54.826646
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths"""
    input_ = '/home/user/code/input.py'
    output = '/home/user/code/output/'
    root = '/home/user/code'
    assert [
        InputOutput(Path(input_), Path(output).joinpath('input.py'))
    ] == list(get_input_output_paths(input_, output, root))
    input_ = '/home/user/code/input.py'
    output = '/home/user/code/output/input.py'
    root = '/home/user/code'
    assert [
        InputOutput(Path(input_), Path(output))
    ] == list(get_input_output_paths(input_, output, root))

# Generated at 2022-06-14 01:41:04.956187
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "/home/marc/Documents/GitHub/pyrbo/pyrbo/main.py"
    output = "/home/marc/Documents/GitHub/pyrbo/pyrbo/"
    root = "/home/marc/Documents/GitHub/pyrbo/pyrbo/"
    path = [path for path in get_input_output_paths(input_, output, root)]
    assert path[0].input_path == Path(input_)
    assert path[0].output_path == Path(output).joinpath(Path(input_).relative_to(root))
    assert path[0].input_path == path[0].output_path
   
    input_ = "/home/marc/Documents/GitHub/pyrbo/pyrbo/"

# Generated at 2022-06-14 01:41:14.020161
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input/a.py', 'output/b.py', None))
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('abc.py', 'output/b.py', None))
    assert list(get_input_output_paths('input/a.py', 'output.py', None)) == [
        InputOutput(Path('input/a.py'), Path('output.py'))]

# Generated at 2022-06-14 01:41:21.898865
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:41:29.698747
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Arrange
    input_ = '../../tests/data/simple_src/simple_src.py'
    output = '../../tests/data/simple_src/simple_dst'
    root = '../../tests/data/simple_src/'

    # Act
    input_output = get_input_output_paths(input_, output, root)

    # Assert
    assert list(input_output)[0].output_path.parent == Path('../../tests/data/simple_src/simple_dst/simple_src')

# Generated at 2022-06-14 01:41:35.473080
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    path_a = Path.cwd() / 'a.py'
    path_b = Path.cwd() / 'b.py'
    path_c = Path.cwd() / 'c.py'
    path_d = Path.cwd() / 'd.py'
    # False test case
    # tests=False, args.output='dir'
    # with pytest.raises(InvalidInputOutput):
    #     list(get_input_output_paths(path_a, 'dir', 'root'))

    # tests = True, args.output = 'dir'
    assert list(get_input_output_paths(path_a, 'dir', 'root')) == [InputOutput(
        Path.cwd() / 'a.py', Path.cwd() / 'dir' / 'a.py')]

# Generated at 2022-06-14 01:41:49.518465
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    Test get_input_output_paths
    
    """
    # test 1, no exception
    assertion_list = [('./input', './output', None, 'file.py', 'file.py'), 
                      ('input', 'output', None, 'file.py', 'file.py'), 
                      ('input', 'output', '', 'file.py', 'file.py'), 
                      ('input/', 'output', None, 'file.py', 'output/file.py'), 
                      ('input/', 'output', '', 'file.py', 'output/file.py')]

    for assertion in assertion_list:
        temp_list = []

# Generated at 2022-06-14 01:41:55.094200
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('input.py', 'output.py')) == [
        InputOutput(Path('input.py'), Path('output.py')),
    ]

    assert list(get_input_output_paths('input.py', 'output')) == [
        InputOutput(Path('input.py'), Path('output').joinpath('input.py')),
    ]

    assert list(get_input_output_paths('input', 'output')) == [
        InputOutput(Path('input').joinpath('main.py'), Path('output').joinpath('main.py')),
        InputOutput(Path('input').joinpath('module.py'), Path('output').joinpath('module.py')),
    ]
