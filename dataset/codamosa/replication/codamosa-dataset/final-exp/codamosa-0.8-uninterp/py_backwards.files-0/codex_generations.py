

# Generated at 2022-06-14 01:33:23.817907
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    def _get_input_output_paths(input_: str, output: str,
                           root: Optional[str]) -> Iterable[InputOutput]:
        return list(get_input_output_paths(input_, output, root))

    all_paths = _get_input_output_paths('./input', './output', None)
    print(all_paths)
    assert len(all_paths) == 2
    assert all_paths[0].input == Path('input') / 'test1.py'
    assert all_paths[0].output == Path('output') / 'test1.py'
    assert all_paths[1].input == Path('input') / 'test2.py'
    assert all_paths[1].output == Path('output') / 'test2.py'



# Generated at 2022-06-14 01:33:38.727961
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    # Get two .py files
    assert tuple(get_input_output_paths('a.py', 'b.py', None)) == (InputOutput(Path('a.py'), Path('b.py')),)

    # Get two .py files from different directories
    assert tuple(get_input_output_paths('a.py', 'c/d/b.py', None)) == (InputOutput(Path('a.py'), Path('c/d/b.py')),)

    # Get all .py files in a directory and its subdirectories

# Generated at 2022-06-14 01:33:42.385133
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    a = get_input_output_paths('./test/test_dir', './test/test_dir/test_dir/test_dir', None)
    for i in a:
        print(i)


if __name__ == '__main__':
    test_get_input_output_paths()

# Generated at 2022-06-14 01:33:52.526785
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    paths = list(get_input_output_paths('a.py', 'b.py', None))
    assert len(paths) == 1
    assert paths[0].input_ == Path('a.py')
    assert paths[0].output == Path('b.py')

    paths = list(get_input_output_paths('a.py', 'b', 'src'))
    assert len(paths) == 1
    assert paths[0].input_ == Path('a.py')
    assert paths[0].output == Path('b').joinpath('a.py')

    paths = list(get_input_output_paths('a', 'b', 'src'))
    assert len(paths) == 1
    assert paths[0].input_ == Path('a').joinpath('a.py')

# Generated at 2022-06-14 01:34:01.636092
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert input_output_paths == list(get_input_output_paths(input_, output, root))

input_ = 'tests/input/foo/bar.py'
output = 'tests/output'
root = 'tests'
input_output_paths = [InputOutput(
    Path('tests/input/foo/bar.py'),
    Path('tests/output/foo/bar.py'))]

input_ = 'tests/input/foo/bar.py'
output = 'tests/output/plex'
root = None
input_output_paths = [InputOutput(
    Path('tests/input/foo/bar.py'),
    Path('tests/output/plex/bar.py'))]

input_ = 'tests/input/foo'
output = 'tests/output'
root = None
input_output

# Generated at 2022-06-14 01:34:11.637226
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths"""
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('/tmp/test.txt', '/tmp/test.py', '/tmp')
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('/tmp/doesn\'t/exists', '/tmp/test.txt', '/tmp')
    assert list(get_input_output_paths('/tmp', '/tmp', None)) == [
        InputOutput(Path('/tmp/t.py'), Path('/tmp/t.py')),
        InputOutput(Path('/tmp/t.py'), Path('/tmp/t.py'))
    ]

# Generated at 2022-06-14 01:34:18.412381
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pdb
    path_of_src_dir = Path(__file__).resolve().parent.parent/'src'
    pdb.set_trace()
    for pair in get_input_output_paths(path_of_src_dir/"test_input.py", path_of_src_dir/"test.py", path_of_src_dir):
        print(pair)
    # assert pair == InputOutput()

# Generated at 2022-06-14 01:34:26.077473
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    pairs = get_input_output_paths('fixtures', 'output', None)
    assert list(pairs) == [
        InputOutput(Path('fixtures/a.py'), Path('output/a.py')),
        InputOutput(Path('fixtures/b.py'), Path('output/b.py')),
    ]

    pairs = get_input_output_paths('fixtures', 'output/c.py', 'fixtures')
    assert list(pairs) == [
        InputOutput(Path('fixtures/a.py'), Path('output/c.py/a.py')),
        InputOutput(Path('fixtures/b.py'), Path('output/c.py/b.py')),
    ]

# Generated at 2022-06-14 01:34:36.511713
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:34:48.512690
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('pkg', 'pkg_out', 'pkg')) == [
        InputOutput(Path('pkg/__init__.py'), Path('pkg_out/__init__.py'))]
    assert list(get_input_output_paths('pkg/a.py', 'pkg_out', 'pkg')) == [
        InputOutput(Path('pkg/a.py'), Path('pkg_out/a.py'))]
    assert list(get_input_output_paths('pkg', 'pkg_out/b.py', 'pkg')) == [
        InputOutput(Path('pkg/__init__.py'), Path('pkg_out/b.py'))]

# Generated at 2022-06-14 01:35:01.158082
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Testing get_input_output_paths"""

    # Test case 1: dir to dir
    inputs = [
        'tests/data/dict1'
        ]
    output = 'tests/output/'
    res = []
    for i in get_input_output_paths(inputs[0], output, None):
        res.append(i)
    assert len(res) == 2
    assert res[0].in_path == 'tests/data/dict1/file1.py'
    assert res[0].out_path == 'tests/output/file1.py'
    assert res[1].in_path == 'tests/data/dict1/file2.py'
    assert res[1].out_path == 'tests/output/file2.py'

    # Test case 2: dir to dir, custom root


# Generated at 2022-06-14 01:35:08.482169
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert get_input_output_paths('./tests/source_files/module3.py',
                                  './tests/output/module3_output.py',
                                  None) == [(Path('./tests/source_files/module3.py'),
                                             Path('./tests/output/module3_output.py'))]

    assert get_input_output_paths('./tests/source_files/module3.py',
                                  './tests/output/',
                                  None) == [(Path('./tests/source_files/module3.py'),
                                             Path('./tests/output/module3.py'))]


# Generated at 2022-06-14 01:35:18.836749
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    # Test for case: input 'y' output 'z'
    paths = get_input_output_paths('y', 'z', None)
    assert next(paths) == InputOutput(Path('y'), Path('z/y'))
    with pytest.raises(StopIteration):
        next(paths)

    # Test for case: input 'y' output 'z' with root 'x'
    paths = get_input_output_paths('y', 'z', 'x')
    assert next(paths) == InputOutput(Path('y'), Path('z/y'))
    with pytest.raises(StopIteration):
        next(paths)

    # Test for case: input 'y/x.py' output 'z'
    paths = get

# Generated at 2022-06-14 01:35:30.099079
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Case 1 : input_ is a .py file and output ends with .py
    input_ = 'test.py'
    output = 'test2.py'
    paths = list(get_input_output_paths(input_, output))
    assert list(paths) == [InputOutput(Path('test.py'), Path('test2.py'))]

    # Case 2 : input_ is a .py file and output doesn't end with .py
    input_ = 'test.py'
    output = 'test2'
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths(input_, output))

    # Case 3 : input_ doesnt' exists
    input_ = 'test.py'
    output = 'test2'

# Generated at 2022-06-14 01:35:39.090044
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest
    from pathlib import Path
    # Test for the exception InvalidInputOutput
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('package', 'output', 'package'))

    # Test for normal case
    expect = [
        InputOutput(Path('package/module.py'), Path('output/module.py')),
        InputOutput(Path('package/subpackage/another_module.py'), Path('output/subpackage/another_module.py')),
    ]
    expect = sorted(expect, key=lambda p: p.input.name)
    result = list(get_input_output_paths('package', 'output', 'package'))
    result = sorted(result, key=lambda p: p.input.name)

    assert expect == result

    # Test for

# Generated at 2022-06-14 01:35:49.930265
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    # Create path
    input_py = Path("./test_input.py")
    output_py = Path("./test_output.py")
    output_dir = Path("./test_output/test_input.py")

    # Create file
    input_py.touch()
    output_py.touch()

    # Check pair creation
    paths = list(get_input_output_paths(str(input_py), str(output_py), None))
    assert paths == [InputOutput(input_py, output_py)]

    # Check exception
    try:
        list(get_input_output_paths("./nonexist.py", str(output_py), None))
        assert False
    except InputDoesntExists:
        pass

    # Check pair creation with root

# Generated at 2022-06-14 01:36:05.066149
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for function get_input_output_paths"""
    assert list(get_input_output_paths('aa.py', 'bb', None)) == [InputOutput(
        Path('aa.py'), Path('bb/aa.py'))]
    assert list(get_input_output_paths('aa.py', 'bb.py', None)) == [InputOutput(
        Path('aa.py'), Path('bb.py'))]
    assert list(get_input_output_paths('aa', 'bb', None)) == [InputOutput(
        Path('aa/zzz.py'), Path('bb/zzz.py'))]

# Generated at 2022-06-14 01:36:17.223191
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:36:27.942380
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Ensure output directory created
    get_input_output_paths('tests/types.py', 'output', None)
    # This is invalid.
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('tests', 'tests.py', None)
    # This is invalid.
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('tests/none', 'tests.py', None)
    # Root is None, just for safety.
    io_paths1 = list(get_input_output_paths(
        'tests/types.py', 'output/tests', None))
    assert io_paths1 == [InputOutput(Path('tests/types.py'),
                                     Path('output/tests/types.py'))]
    # Root equals

# Generated at 2022-06-14 01:36:38.187195
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    INPUT_PATH = Path('/input/path')
    OUTPUT_PATH = Path('/output/path')
    ROOT_PATH = Path('/root/path')
    def _test_run(input_, output, root, expected_outputs):
        actual_outputs = list(get_input_output_paths(input_, output, root))
        assert actual_outputs == expected_outputs

    _test_run(str(INPUT_PATH), str(OUTPUT_PATH), None, [InputOutput(INPUT_PATH, OUTPUT_PATH)])
    _test_run(str(INPUT_PATH.joinpath('a.py')), str(OUTPUT_PATH), None, [InputOutput(INPUT_PATH.joinpath('a.py'), OUTPUT_PATH.joinpath('a.py'))])

# Generated at 2022-06-14 01:37:00.528494
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:37:11.696837
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    test_get_input_output_paths
    """
    input_ = 'abc.py'
    output = 'def.py'
    root = None
    assert(get_input_output_paths == [(input_, output)])

    input_ = 'abc/'
    output = 'def/'
    root = 'abc'
    assert(get_input_output_paths == [('abc/', 'def/'), ('abc/py', 'def/py')])

    input_ = 'abc.py'
    output = 'def/'
    root = None
    assert(get_input_output_paths == [('abc.py', 'def/py')])

    input_ = 'abc'
    output = 'def.py'
    root = None

# Generated at 2022-06-14 01:37:19.193537
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .types import InputOutput

# Generated at 2022-06-14 01:37:30.117673
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .types import InputOutput
    # Test invalid arguments
    invalid_arguments = [
        ('abc.py', 'abc.py'),
        ('abc.py', 'def.txt'),
        ('abc', 'def.txt'),
        ('abc.txt', 'def'),
        ('abc.txt', 'def.py')
    ]

    for args in invalid_arguments:
        with pytest.raises(InvalidInputOutput):
            get_input_output_paths(*args, root='root')

    # Test missing input
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('abc.py', 'def', root='root')

    input_outputs = get_input_output_paths('abc', 'def', root='root')
    assert input_outputs == []

   

# Generated at 2022-06-14 01:37:40.595784
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = Path('tests/fixtures/input_output/input')
    output = Path('tests/fixtures/input_output/output')
    root = Path('tests/fixtures/input_output')


# Generated at 2022-06-14 01:37:52.196318
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .__main__ import get_input_output_paths
    from io import StringIO
    from contextlib import redirect_stdout
    
    input_ = "./test_input/test.py"
    input_2 = "./test_input/test2.py"
    input_3 = "./test_input"
    input_4 = "./test_input/test3.py"
    out_put = "./test_output"

    f = StringIO()
    with redirect_stdout(f):
        get_input_output_paths(input_, out_put, None)
        get_input_output_paths(input_2, out_put, None)
        get_input_output_paths(input_3, out_put, None)

# Generated at 2022-06-14 01:38:02.349566
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test case 1:
    # Input: input_ = "./tests/data/tests_in", output = "./tests/data/tests_out", root = None
    # output: InputOutput(input=Path('./tests/data/tests_in/test_in_file.py'), output=Path('./tests/data/tests_out/test_in_file.py'))
    # InputOutput(input=Path('./tests/data/tests_in/nested/test_in_file.py'), output=Path('./tests/data/tests_out/nested/test_in_file.py'))
    inputs_outputs = get_input_output_paths(
        "./tests/data/tests_in", "./tests/data/tests_out", None)


# Generated at 2022-06-14 01:38:12.429040
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # InvalidInputOutput exception
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('a/b', 'a.py', 'a/b'))

    # InputDoesntExists exception
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('a/b.py', 'a/b.py', 'a/b'))

    # Valid inputs/outputs
    io_paths = get_input_output_paths('a/b.py', 'a/b.py', 'a/b')
    assert len(list(io_paths)) == 1
    io_paths = get_input_output_paths('a/b.py', 'a/b.py', 'a')

# Generated at 2022-06-14 01:38:22.703761
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths"""
    assert list(get_input_output_paths('my_file.py', 'my_file.py',
                                       None)) == [InputOutput(Path('my_file.py'),
                                                             Path('my_file.py'))]
    assert list(get_input_output_paths('my_file.py', 'my_folder/my_file.py',
                                       None)) == [InputOutput(Path('my_file.py'),
                                                             Path('my_folder/my_file.py'))]

# Generated at 2022-06-14 01:38:33.426710
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths"""
    assert list(
        get_input_output_paths(
            '/home/simon/mypy_src/stubs/3.5/typing.py',
            '/home/simon/mypy_stubs/3.5/typing.py',
            '/home/simon/mypy_src/stubs/3.5')
    ) == [
        InputOutput(
            Path('/home/simon/mypy_src/stubs/3.5/typing.py'),
            Path('/home/simon/mypy_stubs/3.5/typing.py'))
    ]


# Generated at 2022-06-14 01:38:53.032343
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'C:/github/typed-ast/'
    output = 'C:/github/typed-ast/'
    root = 'C:/github'
    assert get_input_output_paths(input_, output, root) == [InputOutput(Path('C:/github/typed-ast/typed_ast/ast3.py'), Path('C:/github/typed-ast/typed_ast/ast3.py.copy'))]

# Generated at 2022-06-14 01:39:02.666007
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    assert get_input_output_paths('/foo/bar.py', '/tmp', None) == [
        InputOutput(Path('/foo/bar.py'), Path('/tmp/bar.py'))]
    assert get_input_output_paths('/foo/bar.py', '/tmp/', None) == [
        InputOutput(Path('/foo/bar.py'), Path('/tmp/bar.py'))]
    assert get_input_output_paths('/foo/bar', '/tmp', None) == [
        InputOutput(Path('/foo/bar/foo.py'), Path('/tmp/foo.py'))]

# Generated at 2022-06-14 01:39:13.453526
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths."""
    from .tests.example_source import root

    inputs = [
        (Path(root).joinpath('b.py'), Path(root).joinpath('b.py')),
        (Path(root).joinpath('b.py'), Path(root)),
        (Path(root).joinpath('b.py'), Path(root).joinpath('dst')),
        (Path(root), Path(root)),
        (Path(root), Path(root).joinpath('dst')),
        (Path(root), Path(root).joinpath('dst')),
    ]


# Generated at 2022-06-14 01:39:21.681621
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from os import mkdir, rmdir
    from os.path import join, abspath

    # Create test files for input
    test_dir = "./test_get_input_output_paths_test"
    mkdir(test_dir)

    test1 = join(test_dir, "test1.py")
    with open(test1, "w") as f:
        f.write("test1.py")

    test2 = join(test_dir, "test2.py")
    with open(test2, "w") as f:
        f.write("test2.py")

    test3 = join(test_dir, "test3.py")
    with open(test3, "w") as f:
        f.write("test3.py")

    # Test function get_input_output_paths


# Generated at 2022-06-14 01:39:31.895342
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('foo.py', 'bar', '')) == [
        InputOutput(Path('foo.py'), Path('bar/foo.py'))]
    assert list(get_input_output_paths('foo.py', 'bar/', '')) == [
        InputOutput(Path('foo.py'), Path('bar/foo.py'))]
    assert list(get_input_output_paths('foo.py', 'bar', '.')) == [
        InputOutput(Path('foo.py'), Path('bar/foo.py'))]

# Generated at 2022-06-14 01:39:39.323503
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # GIVEN a file, a directory and a root specified
    input_ = '/root/f.py'
    output = '/output/f.py'
    root = '/root'

    # WHEN the file, the directory and the root are used as parameters
    # in the get_input_output_paths function
    result = list(get_input_output_paths(input_, output, root))
    # THEN it should only give back one input/output pair
    # that consists of the input file with its relative path and
    # the output file with its absolute path
    assert len(result) == 1
    input_output = result[0]
    assert input_output.input == Path(input_)
    assert input_output.output == Path(output)

    # WHEN the file, the directory and the root are used as parameters
    #

# Generated at 2022-06-14 01:39:48.707567
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert get_input_output_paths('a.py', 'b.py', None) == [InputOutput(Path('a.py'), Path('b.py')),]
    assert get_input_output_paths('a.py', 'b', None) == [InputOutput(Path('a.py'), Path('b/a.py')),]
    assert get_input_output_paths('a.py', 'b', 'b') == [InputOutput(Path('a.py'), Path('a.py')),]

# Generated at 2022-06-14 01:39:59.691111
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(
        get_input_output_paths('a.py', 'b.py', 'c'),
    ) == [InputOutput(Path('a.py'), Path('b.py'))]
    assert list(
        get_input_output_paths('a.txt', 'b.txt', 'c'),
    ) == []
    assert list(
        get_input_output_paths('a', 'b/c', 'd/e/f'),
    ) == [InputOutput(Path('d/e/f/a/b.py'), Path('b/c/b.py'))]
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('a.txt', 'b.py', 'c'))


# Generated at 2022-06-14 01:40:08.994609
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    Test get_input_output_paths.
    """
    # Test 1.1 : input is *.py end output is *.py
    # output_paths = get_input_output_paths("test/test_cases/file/test1.py", "test/test_cases/file/test1_out.py", None)
    # print("output_paths")
    # for path in output_paths:
    #     print(path)

    # Test 1.2 : input is *.py end output is not *.py
    output_paths = get_input_output_paths("test/test_cases/file/test1.py", "test/test_cases/file", None)
    print("output_paths")
    for path in output_paths:
        print(path)
    # Test 2

# Generated at 2022-06-14 01:40:15.921218
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    assert list(get_input_output_paths('main.py', 'output', None)) == [
        InputOutput(Path('main.py'), Path('output/main.py'))
    ]

    assert list(get_input_output_paths('src', 'output', None)) == [
        InputOutput(Path('src/main.py'), Path('output/main.py'))
    ]

    assert list(get_input_output_paths('src', 'output', 'src')) == [
        InputOutput(Path('src/main.py'), Path('output/main.py'))
    ]

# Generated at 2022-06-14 01:40:50.255828
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .exceptions import InvalidInputOutput, InputDoesntExists
    import pytest
    with pytest.raises(InvalidInputOutput):
        tuple(get_input_output_paths('input_dir', 'output_dir/output_file.py', None))
    with pytest.raises(InputDoesntExists):
        tuple(get_input_output_paths('input_dir', 'output_dir', None))

    input_output = tuple(get_input_output_paths('input_dir', 'output_dir', None))
    assert len(input_output) == 1

    input_output = tuple(get_input_output_paths(
        'input_dir/input_file.py', 'output_dir/output_file.py', None))
    assert len(input_output) == 1
    assert input

# Generated at 2022-06-14 01:41:00.503154
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('input', 'output', None)) == \
           [InputOutput(Path('input'), Path('output'))]
    assert list(get_input_output_paths('input.py', 'output.py', None)) == \
           [InputOutput(Path('input.py'), Path('output.py'))]
    assert list(get_input_output_paths('input.py', 'output', None)) == \
           [InputOutput(Path('input.py'), Path('output/input.py'))]
    assert list(get_input_output_paths('input', 'output', 'root')) == \
           [InputOutput(Path('input'), Path('output/input'))]

# Generated at 2022-06-14 01:41:08.167210
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Testing get_input_output_paths."""
    from .test import create_test_project
    with create_test_project() as proj:
        proj.add_module('a', 'import b\nprint(b)')
        proj.add_module('b', 'import c\nprint(c)')
        proj.add_module('c', 'print("c")')
        gen = get_input_output_paths(proj.root, proj.root, None)
        assert len(list(gen)) == 3

    with create_test_project() as proj:
        proj.add_module('a', 'import b\nprint(b)')
        proj.add_module('b', 'import c\nprint(c)')

# Generated at 2022-06-14 01:41:16.859731
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:41:25.921317
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'tests/data/dir1'
    output = 'tests/data/dir2'
    root = 'tests/data'
    input_output = list(get_input_output_paths(input_, output, root))
    assert len(input_output) == 4
    assert input_output[0].input_path.name == 'file1.py'
    assert input_output[1].input_path.name == 'file2.py'
    assert input_output[2].input_path.name == 'file3.py'
    assert input_output[3].input_path.name == 'file4.py'
    assert input_output[0].output_path.name == 'file1.py'
    assert input_output[1].output_path.name == 'file2.py'
    assert input_

# Generated at 2022-06-14 01:41:34.639145
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    test_inputs = [
        {
            'input': 'a.py',
            'output': 'b.py',
            'expected_input': 'a.py',
            'expected_output': 'b.py',
        },
        {
            'input': 'a.py',
            'output': 'b',
            'expected_input': 'a.py',
            'expected_output': 'b/a.py',
        },
        {
            'input': 'a',
            'output': 'b.py',
            'expected_input': 'a/a.py',
            'expected_output': 'b.py',
        },
    ]


# Generated at 2022-06-14 01:41:49.288419
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .types import InputOutput

    assert get_input_output_paths('test/test.py', 'test/output.py', None) == [InputOutput(Path('test/test.py'), Path('test/output.py'))]
    assert get_input_output_paths('test/test.py', 'test/output/', None) == [InputOutput(Path('test/test.py'), Path('test/output/test.py'))]
    assert get_input_output_paths('test/', 'test/output/', None) == [InputOutput(Path('test/test.py'), Path('test/output/test.py'))]

# Generated at 2022-06-14 01:41:54.932646
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    project_dir = Path(__file__).parent.parent
    tests_dir = project_dir / 'tests'
    cases_dir = tests_dir / 'cases'
    ios = list(get_input_output_paths(str(cases_dir),
                                      str(tests_dir / "__pycache__"),
                                      str(project_dir)))
    assert len(ios) == 10
    assert ios[0].input == (cases_dir / "single_quotes.py")
    assert ios[0].output == (tests_dir / "__pycache__" / "cases" / "single_quotes.py")
    assert ios[1].input == (cases_dir / "square_brackets.py")

# Generated at 2022-06-14 01:42:05.537728
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""

    assert(list(get_input_output_paths("a.py", "b.py", None)) == [InputOutput(Path("a.py"), Path("b.py"))])
    assert(list(get_input_output_paths("a.py", "", None)) == [InputOutput(Path("a.py"), Path("a.py"))])
    assert(list(get_input_output_paths("b", "c", None)) == [InputOutput(Path("b"), Path("c"))])
    assert(list(get_input_output_paths("b", "c", "a")) == [InputOutput(Path("b"), Path("c"))])

# Generated at 2022-06-14 01:42:12.791933
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_path_pairs = get_input_output_paths("./test/test_folder/*.py", "./test/output", "./test/test_folder")
    pairs = [(input_output_pair.input, input_output_pair.output) for input_output_pair in input_output_path_pairs]
    expected_pairs = [
        (Path('./test/test_folder/temp.py'), Path('./test/output/temp.py')),
        (Path('./test/test_folder/temp2.py'), Path('./test/output/temp2.py')),
        (Path('./test/test_folder/temp_folder/temp3.py'), Path('./test/output/temp_folder/temp3.py'))
    ]
