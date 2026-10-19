

# Generated at 2022-06-14 01:33:03.660676
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_pairs = []
    try:
        input_output_pairs = \
            [x for x in get_input_output_paths('file.py',
                                               'output.py', None)]
    except InputDoesntExists:
        pass
    assert input_output_pairs == [InputOutput(Path('file.py'),
                                              Path('output.py'))]

    input_output_pairs = []
    try:
        input_output_pairs = \
            [x for x in get_input_output_paths('dir/file.py',
                                               'output.py', None)]
    except InputDoesntExists:
        pass

# Generated at 2022-06-14 01:33:14.752960
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for get_input_output_paths"""

    # test case for single file case
    assert list(get_input_output_paths("a.py", "b.py", None)) == \
           [InputOutput(Path("a.py"), Path("b.py"))]

    # test case for single file case 2
    assert list(get_input_output_paths("a.py", "b", None)) == \
           [InputOutput(Path("a.py"), Path("b/a.py"))]

    # test case for single file case 3
    assert list(get_input_output_paths("a.py", "bb", None)) == \
           [InputOutput(Path("a.py"), Path("bb/a.py"))]

    # test case for single folder case

# Generated at 2022-06-14 01:33:25.357307
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    # pylint: disable=unused-variable
    # hf/mpl
    input_ = 'hf/mpl'
    output = '/Users/zixiu/Desktop/test'
    root = 'hf'
    input_outputs = list(get_input_output_paths(input_, output, root))
    input_output = input_outputs[0]
    assert input_output.input_file.absolute() == Path('hf/mpl/__init__.py').absolute()
    assert input_output.output_file.absolute() == Path('/Users/zixiu/Desktop/test/mpl/__init__.py').absolute()
    # hf/mpl/__init__.py

# Generated at 2022-06-14 01:33:36.376197
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    pwd = Path(os.path.dirname(__file__))

    input_1 = os.path.join(pwd, 'test_files/test_1.py')
    output_1 = os.path.join(pwd, 'test_files/test_1_output.py')
    input_2 = os.path.join(pwd, 'test_files/test_2.py')
    output_2 = os.path.join(pwd, 'test_files/test_2_output/test_2.py')
    input_3 = os.path.join(pwd, 'test_files/test_3.py')
    output_3 = os.path.join(pwd, 'test_files/test_3_output/test_3.py')

# Generated at 2022-06-14 01:33:45.971396
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # test single file
    assert list(get_input_output_paths('A.py', 'B.py', '')) == [
        InputOutput(Path('A.py'), Path('B.py'))]
    assert list(get_input_output_paths('A.py', '/', '')) == [
        InputOutput(Path('A.py'), Path('/A.py'))]
    assert list(get_input_output_paths('A.py', 'B', '')) == [
        InputOutput(Path('A.py'), Path('B/A.py'))]

    # test directory

# Generated at 2022-06-14 01:33:53.294304
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    working_dir = os.getcwd()
    test_dir = working_dir + "\\test"
    test_path = working_dir + "\\test\\test_file.py"
    test_path_output = working_dir + "\\test\\test_file_output.py"
    test_path_output_2 = working_dir + "\\test_output_2\\test_file.py"
    test_path_output_3 = working_dir + "\\test\\test_output_3\\test_file.py"


# Generated at 2022-06-14 01:34:02.707161
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:34:12.497651
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    root = './'
    input_ = 'a.py'
    output = 'b.py'

    # output file with relative path
    assert list(get_input_output_paths(input_, output, root)) == [
        InputOutput(Path('a.py'), Path('b.py'))]

    # output file with absolute path
    output = '/b.py'
    assert list(get_input_output_paths(input_, output, root)) == [
        InputOutput(Path('a.py'), Path('/b.py'))]

    # output directory with relative path
    output = 'c/'
    assert list(get_input_output_paths(input_, output, root)) == [
        InputOutput(Path('a.py'), Path('c/a.py'))]

    # output

# Generated at 2022-06-14 01:34:27.581522
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    assert(list(get_input_output_paths('input', 'output', 'root')) == [])
    assert(list(get_input_output_paths('input.py', 'output', 'root')) == [])
    assert(list(get_input_output_paths('input.py', 'output.py', 'root')) == [])
    
    assert(list(get_input_output_paths('input_dir', 'output', 'root')) == [])
    assert(list(get_input_output_paths('input_dir', 'output.py', 'root')) == [])


# Generated at 2022-06-14 01:34:36.500397
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test the get_input_output_paths function."""
    from pytest import raises
    from pathlib import Path
    with raises(InvalidInputOutput):
        list(get_input_output_paths('input.py', 'output.rst', '.'))
    with raises(InputDoesntExists):
        list(get_input_output_paths('nope', 'output.rst', '.'))
    assert list(get_input_output_paths('input.py', 'output.py', '.')) == [
        InputOutput(Path('input.py'), Path('output.py'))]
    assert list(get_input_output_paths('input.py', 'output', '.')) == [
        InputOutput(Path('input.py'), Path('output').joinpath('input.py'))]
   

# Generated at 2022-06-14 01:35:01.342437
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_paths = get_input_output_paths("C:\\Users\\Harsh Agarwal\\Desktop\\Projects\\Minesweeper\\Project\\msweeper_game.py", "C:\\Users\\Harsh Agarwal\\Desktop\\Projects\\Minesweeper\\Project\\msweeper_game.py", "C:\\Users\\Harsh Agarwal\\Desktop\\Projects\\Minesweeper\\Project\\msweeper_game.py")
    assert input_output_paths == InputOutput("C:\\Users\\Harsh Agarwal\\Desktop\\Projects\\Minesweeper\\Project\\msweeper_game.py", "C:\\Users\\Harsh Agarwal\\Desktop\\Projects\\Minesweeper\\Project\\msweeper_game.py")

# Generated at 2022-06-14 01:35:01.834379
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    pass

# Generated at 2022-06-14 01:35:16.607241
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input1 = 'a.py'
    output1 = 'b.py'
    input_output = tuple(get_input_output_paths(input1, output1, None))[0]
    assert input_output.input == Path(input1)
    assert input_output.output == Path(output1)

    input2 = 'a.py'
    output2 = 'b'
    input_output = tuple(get_input_output_paths(input2, output2, None))[0]
    assert input_output.input == Path(input2)
    assert input_output.output == Path(output2).joinpath(Path(input2).name)

    input3 = 'dir'
    output3 = 'dir2'

# Generated at 2022-06-14 01:35:24.014991
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Tests for valid inputs and outputs
    assert get_input_output_paths("test/test.py", "output/", None) == [InputOutput(Path("test/test.py"), Path("output/test.py"))]
    assert get_input_output_paths("test/", "output/", None) == [InputOutput(Path("test/test.py"), Path("output/test.py"))]
    assert get_input_output_paths("test/test.py", "output/test.py", None) == [InputOutput(Path("test/test.py"), Path("output/test.py"))]

# Generated at 2022-06-14 01:35:27.157300
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import string
    import random
    rng = random.SystemRandom()
    v = rng.choice(string.ascii_lowercase)
    assert v in string.ascii_lowercase

# Generated at 2022-06-14 01:35:38.181213
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert (list(get_input_output_paths('tests/data/class/input/',
                                        'tests/data/class/output/',
                                        'tests/data/class/input/')) ==
            [InputOutput(Path('tests/data/class/input/test_0.py'),
                         Path('tests/data/class/output/test_0.py')),
             InputOutput(Path('tests/data/class/input/test_1.py'),
                         Path('tests/data/class/output/test_1.py')),
             InputOutput(Path('tests/data/class/input/test_2.py'),
                         Path('tests/data/class/output/test_2.py'))])

# Generated at 2022-06-14 01:35:49.534770
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_dir_path = Path("input_dir")
    output_dir_path = Path("output_dir")


# Generated at 2022-06-14 01:36:04.620785
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from . import __version__
    import distutils.util
    import sys
    from .__main__ import main
    def check_input_output_paths(input_: str, output: str,
                           root: Optional[str]) -> None:
        root = sys.path[0] if root is None else root
        is_windows = distutils.util.get_platform().startswith('win32')
        argv_base = ['show_diff_pycodestyle',
                     '--version', __version__,
                     '--input', input_,
                     '--output', output]
        if root is not None:
            argv_base.extend(['--root', root])
        if is_windows:
            argv_base.append('1')
        print('\nargv: ', argv_base)


# Generated at 2022-06-14 01:36:09.824888
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Tests for the get_input_output_paths function."""
    assert list(get_input_output_paths('/a/b/c/foo.py', '/a/b/c/bar.py', None)) \
        == [InputOutput(Path('/a/b/c/foo.py'), Path('/a/b/c/bar.py'))]
    assert list(get_input_output_paths(
        '/a/b/c/foo.py', '/a/b/c', None)) == [InputOutput(Path('/a/b/c/foo.py'), Path('/a/b/c/foo.py'))]

# Generated at 2022-06-14 01:36:20.732457
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test the function get_input_output_paths.

    It should be able to handle all the cases in the help message of the module.

    """
    # Case:
    # 1. input is a file, output is a file
    # 2. input is a file, output is a directory
    test_input = 'test_input.py'
    test_output = 'test_output'
    test_root = None
    assert list(get_input_output_paths(test_input, test_output, test_root)) == [
        InputOutput(Path(test_input), Path(test_output))]

    # Case:
    # 1. input is a directory, output is a file
    test_input = 'test_input'
    test_output = 'test_output.py'

# Generated at 2022-06-14 01:37:02.703251
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Case 1: input ends with .py and output ends with .py
    input_ = "./hello.py"
    output = "./output/temp.py"
    root = None
    input_outputs = list(get_input_output_paths(input_, output, root))
    assert input_outputs[0].input_path == Path("./hello.py")
    assert input_outputs[0].output_path == Path("./output/temp.py")

    # Case 2: input ends with .py and output'doesn't end with .py
    input_ = "./hello.py"
    output = "./output/"
    root = None
    input_outputs = list(get_input_output_paths(input_, output, root))

# Generated at 2022-06-14 01:37:11.805299
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test if the output is the same as input."""
    from tempfile import TemporaryDirectory
    from shutil import make_archive

    with TemporaryDirectory() as tempdir:
        paths = [
            'folder/a.py',
            'folder/b.py',
            'folder/__init__.py',
            'folder/c/d.py',
            'e.py',
            'f.py'
            ]

        for path in paths:
            with open(os.path.join(tempdir, path), 'w') as file:
                file.write('')

        input_ = os.path.join(tempdir, 'folder')
        output = os.path.join(tempdir, 'folder2')
        root = tempdir


# Generated at 2022-06-14 01:37:19.268528
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    file_paths = get_input_output_paths('dummy_input', 'dummy_output', 'root')
    assert list(file_paths) == []
    file_paths = get_input_output_paths('dummy_input.py', 'dummy_output.py',
                                        'root')
    assert list(file_paths) == [InputOutput(Path('dummy_input.py'),
                                            Path('dummy_output.py'))]
    file_paths = get_input_output_paths('dummy_input.py', 'dummy_output',
                                        'root')

# Generated at 2022-06-14 01:37:30.118860
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # input and output type is file
    assert get_input_output_paths('a.py', 'b.py', None) == \
        [InputOutput(Path('a.py'), Path('b.py'))]

    # input and output type is folder
    assert get_input_output_paths('c/', 'd/', None) == \
        [InputOutput(Path('c/a.py'), Path('d/a.py'))]

    # input is file, output is folder
    assert get_input_output_paths('c/a.py', 'd/', None) == \
        [InputOutput(Path('c/a.py'), Path('d/a.py'))]

    # input and output type is folder and the path is relative

# Generated at 2022-06-14 01:37:40.583400
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('foo.py', 'bar.py', None)) == [
        InputOutput(Path('foo.py'), Path('bar.py'))]
    assert list(get_input_output_paths('foo.py', 'bar', None)) == [
        InputOutput(Path('foo.py'), Path('bar/foo.py'))]
    assert list(get_input_output_paths('foo/bar.py', 'baz', None)) == [
        InputOutput(Path('foo/bar.py'), Path('baz/bar.py'))]
    assert list(get_input_output_paths('foo/bar.py', 'baz', 'foo')) == [
        InputOutput(Path('foo/bar.py'), Path('baz/bar.py'))]
   

# Generated at 2022-06-14 01:37:51.796785
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest

    assert list(get_input_output_paths(
        'example/input.py', 'example/output.py', root=None),) == [
            InputOutput(Path('example/input.py'), Path('example/output.py')),
        ]

    assert list(get_input_output_paths(
        'example/input.py', 'example/', root=None),) == [
            InputOutput(Path('example/input.py'), Path('example/input.py')),
        ]

    assert list(get_input_output_paths(
        'example/', 'example/output', root=None),) == [
            InputOutput(Path('example/input.py'), Path('example/output/input.py')),
        ]


# Generated at 2022-06-14 01:37:58.135238
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Arrange
    input_ = '.'
    output = '.'

    # Act and Assert
    assert get_input_output_paths(input_, output, root=None) == []
    assert get_input_output_paths('./foo.py', '.', root=None) == [(Path('foo.py'), Path('foo.py'))]
    assert get_input_output_paths('./foo.py', './bar', root=None) == [(Path('foo.py'), Path('bar/foo.py'))]

# Generated at 2022-06-14 01:38:06.184060
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # input file is a file
    input_ = 'test/test_data/test_small.py'
    output = './test/test_data/test_output.py'
    output_paths = \
        [InputOutput(Path(input_), Path(output))]
    assert get_input_output_paths(input_, output, 'test/test_data') == output_paths

    # input file is a folder
    input_ = 'test/test_data'
    output = './test/test_data/test_output/'

# Generated at 2022-06-14 01:38:19.291074
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('a.py', 'b.py', None)) == \
        [InputOutput(Path('a.py'), Path('b.py'))]
    assert list(get_input_output_paths('a.py', '/b', None)) == \
        [InputOutput(Path('a.py'), Path('/b/a.py'))]
    assert list(get_input_output_paths('a.py', '/b', '/c')) == \
        [InputOutput(Path('a.py'), Path('/b/a.py'))]
    assert list(get_input_output_paths('a', 'b', None)) == \
        [InputOutput(Path('a/a.py'), Path('b/a.py'))]

# Generated at 2022-06-14 01:38:27.507942
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert get_input_output_paths('./tests/input/file.py',
                                  './tests/output/file.py') == (
                                      InputOutput(Path('./tests/input/file.py'),
                                                  Path('./tests/output/file.py')))
    assert get_input_output_paths('./tests/input',
                                  './tests/output') == (
                                      InputOutput(Path('./tests/input/file.py'),
                                                  Path('./tests/output/file.py')))

# Generated at 2022-06-14 01:39:13.412571
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """pytest doc."""
    from .utils import cd
    from .exceptions import InvalidInputOutput
    from .settings import DEFAULT_OUTPUT
    from .config import CONFIG
    from .types import InputOutput

    with cd('tests/fixtures'):
        with pytest.raises(InvalidInputOutput):
            assert list(get_input_output_paths('bar.py', 'foo.py', None)) == \
                [InputOutput(Path('bar.py'), Path('foo.py'))]

        with pytest.raises(InvalidInputOutput):
            assert list(get_input_output_paths('foo.py', 'bar.py', None)) == \
                [InputOutput(Path('foo.py'), Path('bar.py'))]


# Generated at 2022-06-14 01:39:21.624847
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    root = Path('.')
    input_path = root.joinpath('file.py')
    output_path = root.joinpath('file.rst')
    answer = get_input_output_paths(input_path, output_path, root)
    assert answer == [InputOutput(Path(input_path), Path(output_path))]

    input_path = root.joinpath('file.py')
    output_path = root.joinpath('a', 'file.py')
    answer = get_input_output_paths(input_path, output_path, root)
    assert answer == [InputOutput(Path(input_path), Path(output_path))]

    input_path = root.joinpath('a', 'file.py')
    output_path = root.joinpath('b', 'file.py')
   

# Generated at 2022-06-14 01:39:31.772264
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths function."""
    assert list(get_input_output_paths("invalid_path", "invalid_path", "invalid_path")) == []
    assert list(get_input_output_paths("test/data/root", "test/data/root", "invalid_path")) == []
    assert list(get_input_output_paths("test/data/root/file1.py", "test/data/root/file1.py", None)) == [InputOutput(Path("test/data/root/file1.py"), Path("test/data/root/file1.py"))]

# Generated at 2022-06-14 01:39:39.259708
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    root_path = Path(__file__).parent.absolute()

# Generated at 2022-06-14 01:39:48.683559
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for function get_input_output_paths."""
    # test input file or directory -> output file
    # output should be ignored
    result = set()
    iterator = get_input_output_paths(
        input_=__file__, output='output.py', root=None)
    for item in iterator:
        result.add(item)
    assert result == {InputOutput(Path(__file__), Path(__file__))}

    # test input file -> output directory
    # expected that file would be placed in output directory
    result = set()
    iterator = get_input_output_paths(
        input_=__file__, output='tmp/', root=None)
    for item in iterator:
        result.add(item)

# Generated at 2022-06-14 01:40:00.076487
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = Path('/home/halon/myproject/')
    output = Path('/home/halon/myproject_typecheck/')

# Generated at 2022-06-14 01:40:09.703976
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_folder = Path(__file__).parent.joinpath(
        "get_input_output_paths_test")
    paths = get_input_output_paths(
        input_=test_folder.joinpath("input"),
        output=test_folder.joinpath("output"),
        root=test_folder)
    paths = list(paths)

# Generated at 2022-06-14 01:40:17.470319
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    Test for get_input_output_paths
    """

    # Test input and output with same name
    input_path = '/home/me/myproject'
    output_path = '/homes/me/newproject'
    result = tuple(get_input_output_paths(input_path, output_path, ''))

    assert result == (
        InputOutput(Path('/home/me/myproject/setup.py'),
                    Path('/homes/me/newproject/setup.py')),
        InputOutput(Path('/home/me/myproject/myproject/__init__.py'),
                    Path('/homes/me/newproject/myproject/__init__.py')),
    )

    # Test input and output with different name
    input_path = '/home/me/myproject'


# Generated at 2022-06-14 01:40:27.786863
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:40:39.117792
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from . import validator

    # test for checking if pairs for functions are okay
    assert list(get_input_output_paths('./tests/source', './tests/output', None)) == [InputOutput(Path('./tests/source/hello.py'), Path('./tests/output/hello.py'))]
    assert validator.check_py('./tests/source/hello.py', './tests/output/hello.py')

    # test for checking if pairs for projects are okay

# Generated at 2022-06-14 01:41:53.625157
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('a.py', 'b.py', None)) == \
        [InputOutput(Path('a.py'), Path('b.py'))]

    assert list(get_input_output_paths('.', 'b', None)) == \
        [InputOutput(Path('a.py'), Path('b/a.py'))]

    assert list(get_input_output_paths('.', 'b', '.')) == \
        [InputOutput(Path('a.py'), Path('b/a.py'))]

    assert list(get_input_output_paths('.', 'b', '../')) == \
        [InputOutput(Path('a.py'), Path('b/a.py'))]

# Generated at 2022-06-14 01:42:01.335475
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test 1
    input1 = '/home/user/test'
    output1 = '/home/user/output'
    root1 = None
    io1 = [InputOutput(Path('/home/user/test/foo.py'),
                       Path('/home/user/output/foo.py')),
           InputOutput(Path('/home/user/test/foo/bar.py'),
                       Path('/home/user/output/foo/bar.py'))]

    for i, o in get_input_output_paths(input1, output1, root1):
        assert i == io1[0].input
        assert o == io1[0].output
        io1.pop(0)
    assert len(io1) == 0

    # Test 2
    input2 = '/home/user/test/foo.py'


# Generated at 2022-06-14 01:42:09.945600
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    # Single file, same paths
    assert list(get_input_output_paths('in.py', 'out.py', None)) == [
        InputOutput(Path('in.py'), Path('out.py'))
    ]

    # Single file, different paths
    assert list(get_input_output_paths('in.py', 'out_dir', None)) == [
        InputOutput(Path('in.py'), Path('out_dir/in.py'))
    ]

    # Directory, same path

# Generated at 2022-06-14 01:42:20.014324
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # test invalid input output
    with pytest.raises(InvalidInputOutput):
        # Output is a path to a file, but input is a path to directory
        get_input_output_paths('/input', '/output/a.py', None)

    with pytest.raises(InvalidInputOutput):
        # Output is a path to a directory, but input is a path to a file
        get_input_output_paths('/input/a.py', '/output', None)

    with pytest.raises(InvalidInputOutput):
        # Both input and output are paths to files
        get_input_output_paths('/input/a.py', '/output/a.py', None)


# Generated at 2022-06-14 01:42:29.967002
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import os
    os.makedirs('/tmp/test')
    os.makedirs('/tmp/test/dir1/dir2/dir3')
    os.makedirs('/tmp/test/dir4/dir5')
    with open('/tmp/test/dir1/dir2/dir3/test1.py', 'w') as f:
        f.write('')
    with open('/tmp/test/dir4/dir5/test2.py', 'w') as f:
        f.write('')
    with open('/tmp/test/test3.py', 'w') as f:
        f.write('')

# Generated at 2022-06-14 01:42:40.579665
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Ensure we get correct input/output path pairs."""
    assert list(get_input_output_paths(
        input_='foo.py', output='bar.py', root=None)) == [
            InputOutput(Path('foo.py'), Path('bar.py'))]

    assert list(get_input_output_paths(
        input_='foo.py', output='bar', root=None)) == [
            InputOutput(Path('foo.py'), Path('bar').joinpath('foo.py'))]

    assert list(get_input_output_paths(
        input_='foo', output='bar', root='.')) == [
            InputOutput(Path('foo').joinpath('a', 'b', 'c.py'),
                        Path('bar').joinpath('a', 'b', 'c.py'))]

# Generated at 2022-06-14 01:42:51.519455
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    # Test case #1
    list_of_input_output_pairs = get_input_output_paths('input.py', 'output', None)
    assert next(list_of_input_output_pairs) == InputOutput(Path('input.py'), Path('output/input.py'))

    # Test case #2
    list_of_input_output_pairs = get_input_output_paths('input.py', 'output/abc.py', None)
    assert next(list_of_input_output_pairs) == InputOutput(Path('input.py'), Path('output/abc.py'))

    # Test case #3