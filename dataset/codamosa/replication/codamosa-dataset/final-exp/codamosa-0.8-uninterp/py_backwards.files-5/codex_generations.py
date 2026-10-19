

# Generated at 2022-06-14 01:33:26.273945
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    assert list(get_input_output_paths('foo.py', '/bar.py', None)) == [
        InputOutput(Path('foo.py'), Path('bar.py'))]
    assert list(get_input_output_paths('/foo.py', '/bar.py', '/')) == [
        InputOutput(Path('/foo.py'), Path('/bar.py'))]
    assert list(get_input_output_paths('/foo.py', '/bar.py', '/foo')) == [
        InputOutput(Path('/foo.py'), Path('/bar.py'))]

# Generated at 2022-06-14 01:33:39.393779
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "tests/data/input/main.py"
    output = "tests/data/output/"
    root = None
    expected = [('tests/data/input/main.py', 'tests/data/output/main.py')]
    actual = []
    for x in get_input_output_paths(input_, output, root):
        actual.append((x.in_, x.out))
    assert(expected == actual)

    input_ = "tests/data/input/"
    output = "tests/data/output/"
    root = None
    expected = [('tests/data/input/main.py', 'tests/data/output/main.py'),
                ('tests/data/input/submod1.py', 'tests/data/output/submod1.py')]
    actual = []
   

# Generated at 2022-06-14 01:33:44.442703
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    root = Path(__file__).parent
    input_path = root.joinpath('my_script.py')
    output_path = root.joinpath('output', 'my_script.py')
    input_output_pairs = get_input_output_paths(str(input_path), str(output_path), str(root))
    assert list(input_output_pairs) == [InputOutput(input_path, output_path)]


# Generated at 2022-06-14 01:33:52.287886
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output = get_input_output_paths('tests/1/1.1/1.1.py', 'output/test_output', 'tests')
    assert input_output is not None
    iop = next(input_output)
    assert iop.input.name == '1.1.py'
    assert iop.output == Path('output/test_output/1/1.1/1.1.py')
    assert iop.output == Path('output/test_output/1/1.1/1.1.py')

    input_output = get_input_output_paths('tests/1/1.1/1.1.py', '.output/test_output', 'tests')
    assert input_output is not None
    iop = next(input_output)
    assert iop.input.name

# Generated at 2022-06-14 01:34:01.631853
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:34:10.462706
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_io_paths = get_input_output_paths('test/test_input', 'test/test_output', root=None)
    test_io_paths = list(test_io_paths)
    assert len(test_io_paths) == 6
    assert test_io_paths[0].output_path.name == 'add_one.py'
    assert test_io_paths[1].output_path.name == 'add_one_test.py'
    assert test_io_paths[2].output_path.name == 'add_two.py'
    assert test_io_paths[3].output_path.name == 'add_two_test.py'
    assert test_io_paths[4].output_path.parent.name == 'submodule1'
    assert test

# Generated at 2022-06-14 01:34:15.473539
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = './tests/data/'
    output = '/./tests/data/output/'
    assert len([p for p in get_input_output_paths(input_, output, None)]) == 3


# Generated at 2022-06-14 01:34:28.588778
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths("./tests/test_input/test_input.py", "./tests/test_output", None)) == [InputOutput(PosixPath('./tests/test_input/test_input.py'), PosixPath('./tests/test_output/test_input.py'))]
    assert list(get_input_output_paths("./tests/test_input/", "./tests/test_output", None)) == [InputOutput(PosixPath('./tests/test_input/test_input.py'), PosixPath('./tests/test_output/test_input.py'))]

# Generated at 2022-06-14 01:34:38.991622
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    
    # Valid input/output pairs
    for input_, output in [('input.py', 'output.py'),
                           ('input_dir', 'output_dir')]:
        input_output = list(get_input_output_paths(input_, output, 'root_dir'))
        assert len(input_output) == 1
        assert input_output[0].input == Path(input_)
        assert input_output[0].output == Path(output)
    
    # Exception InvalidInputOutput is raised when input is not a valid file/directory
    try:
        list(get_input_output_paths('input', 'output.py', 'root_dir'))
    except InvalidInputOutput:
        pass
    
    # Exception InputDoesntExists is raised when input does not exist

# Generated at 2022-06-14 01:34:49.250314
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Given
    input_ = 'first.py'
    output = '/home/user/dir'
    # When
    result = get_input_output_paths(input_, output, None)
    # Then
    assert list(result) == [InputOutput(Path('first.py'), Path('/home/user/dir/first.py'))]
    # Given
    input_ = 'path/to/second.py'
    output = 'dir/output/'
    # When
    result = get_input_output_paths(input_, output, None)
    # Then
    assert list(result) == [InputOutput(Path('path/to/second.py'), Path('dir/output/second.py'))]


# Generated at 2022-06-14 01:35:00.257667
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths(".", ".", ".")) == [
        InputOutput(Path("."), Path(".")),
    ]
    assert list(get_input_output_paths("a.py", "b", ".")) == [
        InputOutput(Path("a.py"), Path("b/a.py")),
    ]
    assert list(get_input_output_paths(".", "b", ".")) == [
        InputOutput(Path("."), Path("b/."))
    ]
    assert list(get_input_output_paths(".", "b", "x")) == [
        InputOutput(Path("."), Path("b"))
    ]

# Generated at 2022-06-14 01:35:14.277686
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('bar.py', 'foo.py', 'root')) == [InputOutput(Path('bar.py'), Path('foo.py'))]
    assert list(get_input_output_paths('bar', 'foo.py', 'root')) == [InputOutput(Path('bar.py'), Path('foo.py/bar.py'))]
    assert list(get_input_output_paths('bar', 'foo', 'root')) == [InputOutput(Path('bar.py'), Path('foo/bar.py'))]
    assert list(get_input_output_paths('bar', 'foo', 'root/bar')) == [InputOutput(Path('bar.py'), Path('foo/bar.py'))]

# Generated at 2022-06-14 01:35:24.687225
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    paths = list(get_input_output_paths('tests/data/simple.py', 'output', None))
    assert len(paths) == 1
    assert paths[0].input.name == 'simple.py'
    assert paths[0].output.name == 'simple.py'

    paths = list(get_input_output_paths('tests/data/simple/', 'output', 'tests/data'))
    assert len(paths) == 1
    assert paths[0].input.name == 'simple.py'
    assert paths[0].output.name == 'simple.py'

    paths = list(get_input_output_paths('tests/data/simple/', 'output', None))
    assert len(paths) == 1
    assert paths[0].input.name == 'simple.py'
    assert paths

# Generated at 2022-06-14 01:35:34.126107
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = '.'
    output = './'
    root = None
    expected = [InputOutput(Path('.').joinpath('mypython.py'),
                            Path('./').joinpath('mypython.py')),
                InputOutput(Path('.').joinpath('sample.py'),
                            Path('./').joinpath('sample.py')),
                InputOutput(Path('.').joinpath('tests.py'),
                            Path('./').joinpath('tests.py'))]
    actual = get_input_output_paths(input_, output, root)
    assert list(actual) == expected

# Generated at 2022-06-14 01:35:41.601381
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test for both input and output being files
    path_input = Path.joinpath(Path.cwd(), "testdata/input/file_input.py")
    path_output = Path.joinpath(Path.cwd(), "testdata/output/file_output.py")
    path_pairs = get_input_output_paths(str(path_input), str(path_output), None)
    for inp_out_pair in path_pairs:
        assert inp_out_pair.input.name == "file_input.py"
        assert inp_out_pair.output.name == "file_output.py"

    # Test for input being a directory and output being a file
    path_input = Path.joinpath(Path.cwd(), "testdata/input")
    path_output = Path.joinpath

# Generated at 2022-06-14 01:35:51.136353
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('a.py',
                                         'b.py',
                                         None)) == [InputOutput(Path('a.py'),
                                                               Path('b.py'))]
    assert list(get_input_output_paths('a.py',
                                         'b',
                                         None)) == [InputOutput(Path('a.py'),
                                                               Path('b/a.py'))]
    assert list(get_input_output_paths('a',
                                         'b',
                                         'a')) == [InputOutput(Path('a/a.py'),
                                                               Path('b/a.py'))]

# Generated at 2022-06-14 01:36:00.830223
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:36:07.608305
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = Path('./test_dir/test1.py')
    output = Path('output_dir/')
    paths = get_input_output_paths(input_, output, './test_dir/')
    assert next(paths) == InputOutput(Path('test1.py'), Path('output_dir/test1.py'))

    input_2 = Path('./test_dir')
    output2 = Path('output_dir')
    paths2 = get_input_output_paths(input_2, output2, './test_dir')
    assert next(paths2) == InputOutput(Path('test_dir/test1.py'), Path('output_dir/test1.py'))

# Generated at 2022-06-14 01:36:19.925493
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    assert get_input_output_paths(
        input_='input.py',
        output='output.py',
        root=None
    ) == [InputOutput(Path('input.py'), Path('output.py'))]

    assert get_input_output_paths(
        input_='input.py',
        output='output',
        root=None
    ) == [InputOutput(Path('input.py'), Path('output').joinpath('input.py'))]

    assert get_input_output_paths(
        input_='input.py',
        output='output',
        root='.'
    ) == [InputOutput(Path('input.py'), Path('output').joinpath('input.py'))]

    assert get_input_output_path

# Generated at 2022-06-14 01:36:22.581166
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    pass

# Generated at 2022-06-14 01:36:40.563244
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    # Test for single file

    # Test for input ending with .py
    # Test for output ending with .py
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths(
            "", "", None))

    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths(
            "input", "output", None))

    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths(
            "input.py", "output", None))

    result = list(get_input_output_paths(
        "input.py", "output.py", None))
    assert result[0].input_path == Path("input.py")
    assert result[0].output_path == Path("output.py")

# Generated at 2022-06-14 01:36:55.477990
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    Steps:
        1. Create a temporary directory and
           populate it with a file structure.
        2. Call ``get_input_output_paths`` and
           check results.
        3. Remove the temporary directory.
    """
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        path_a = tmpdir.joinpath('a.py')
        path_b_c_dpy = tmpdir.joinpath('b', 'c', 'd.py')
        path_b_cpy = tmpdir.joinpath('b', 'c.py')
        path_bpy = tmpdir.joinpath('b.py')
        path_epy = tmpdir.joinpath('e.py')

        path_e = tmpdir.joinpath('e')

# Generated at 2022-06-14 01:37:04.255083
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .testing import get_data_path, DATA_DIR
    import pytest

    with pytest.raises(InvalidInputOutput):
        try:
            for _ in get_input_output_paths('foo.py', 'bar.txt', None):
                pass
        except InvalidInputOutput as e:
            e.args = (e.args[0], '"bar.txt" is not a python file.')
            raise e
    with pytest.raises(InputDoesntExists):
        try:
            for _ in get_input_output_paths('foo.py', 'bar.py', None):
                pass
        except InputDoesntExists as e:
            e.args = (e.args[0],)
            raise e

# Generated at 2022-06-14 01:37:09.882825
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input = 'tests/example_app/'
    output = 'tests/example_app_out'

# Generated at 2022-06-14 01:37:17.364473
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    paths = get_input_output_paths(
        '/my/package/module.py',
        '/my/package/module2.py',
    )

    assert set(paths) == set([
        InputOutput(Path('/my/package/module.py'),
                    Path('/my/package/module2.py')),
    ])

    paths = get_input_output_paths(
        '/my/package/module.py',
        '/my/package',
    )

    assert set(paths) == set([
        InputOutput(Path('/my/package/module.py'),
                    Path('/my/package/module.py')),
    ])


# Generated at 2022-06-14 01:37:28.763274
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Using two absolute paths.
    paths = get_input_output_paths(
        input_='/input/file.py', output='/output/file.py', root=None)
    path = next(paths)
    assert path.input == Path('/input/file.py')
    assert path.output == Path('/output/file.py')
    with pytest.raises(StopIteration):
        next(paths)
    
    # Using two relative paths.
    paths = get_input_output_paths(
        input_='input/file.py', output='output/file.py', root=None)
    path = next(paths)
    assert path.input == Path('input/file.py')
    assert path.output == Path('output/file.py')

# Generated at 2022-06-14 01:37:40.438055
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('a.py', 'b.py', None)) == [
        InputOutput(Path('a.py'), Path('b.py'))
    ]
    assert list(get_input_output_paths('a.py', 'b', None)) == [
        InputOutput(Path('a.py'), Path('b/a.py'))
    ]
    assert list(get_input_output_paths('a.py', 'b', 'a')) == [
        InputOutput(Path('a.py'), Path('b/a.py'))
    ]
    assert list(get_input_output_paths('a.py', 'b', 'x')) == [
        InputOutput(Path('a.py'), Path('b/a.py'))
    ]
    assert list

# Generated at 2022-06-14 01:37:51.755685
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_cases = [
        ('test_files/test_files_1.py', 'output/test_files_1', 'test_files'),
        ('test_files/test_files_1.py', 'output/test_files_1.py',
            'test_files'),
        ('test_files', 'output', 'test_files'),
        ('test_files/', 'output', 'test_files'),
        ('test_files/', 'output', 'test_files')
    ]

# Generated at 2022-06-14 01:37:56.672798
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('testA', 'testB', 'testC')) == \
        list(get_input_output_paths('testA/testA.py', 'testB/testA.py', 'testC'))

# Generated at 2022-06-14 01:38:07.495558
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    result = list(get_input_output_paths('a.py', 'out', None))
    assert len(result) == 1
    assert result[0].input == Path('a.py')
    assert result[0].output == Path('out')

    result = list(get_input_output_paths('a.py', 'out.py', None))
    assert len(result) == 1
    assert result[0].input == Path('a.py')
    assert result[0].output == Path('out.py')

    result = list(get_input_output_paths('in/a.py', 'out.py', None))
    assert len(result) == 1
    assert result[0].input == Path('in/a.py')
    assert result[0].output == Path('out.py')

    result = list

# Generated at 2022-06-14 01:38:25.092606
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('test_file.txt',
                                       'test_output.txt', 'a_dir')) == \
        [InputOutput(Path('test_file.txt'), Path('test_output.txt'))]
    assert list(get_input_output_paths('test_file.py',
                                       'test_output.txt', 'a_dir')) == \
        [InputOutput(Path('test_file.py'), Path('test_output.txt').joinpath('test_file.py'))]

# Generated at 2022-06-14 01:38:32.535961
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    Basic test for function get_input_output_paths().
    """
    # Basic case with a file with the same name as the output.
    assert list(get_input_output_paths(
        '/path/to/file_input.py', '/path/to/file_output.py', None)) == [
            InputOutput(Path('/path/to/file_input.py'), Path('/path/to/file_output.py')
    )]

    # Test with input and output of different names.

# Generated at 2022-06-14 01:38:38.516412
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    print("--------------Test get_input_output_paths------------------")
    # Test when input_ is a file and output is a directory
    (input_, output) = ('file', 'directory')
    for (inp, out) in get_input_output_paths(input_, output, None):
        assert inp.name == 'file'
        assert out.name == 'file'
    # Test when input_ is a file and output is a file
    (input_, output) = ('file1', 'file2')
    for (inp, out) in get_input_output_paths(input_, output, None):
        assert inp.name == 'file1'
        assert out.name == 'file2'
    # Test when input_ is a directory, root is None and output is a directory

# Generated at 2022-06-14 01:38:48.227990
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Invalid Input/Output
    try:
        get_input_output_paths('baz.py', 'foo.bar', None)
    except InvalidInputOutput:
        pass
    # Input does not exists
    try:
        get_input_output_paths('foo.py', 'bar.bar', None)
    except InputDoesntExists:
        pass
    # Files
    assert list(get_input_output_paths('foo.py', 'baz.py', None)) == \
        [InputOutput(
            Path('foo.py'),
            Path('baz.py'))]
    # Directories

# Generated at 2022-06-14 01:38:56.235799
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pytest import raises
    from pathlib import Path
    from igitt import InputOutput
    with raises(InvalidInputOutput):
        get_input_output_paths('file.py', 'file.txt', None)
    with raises(InputDoesntExists):
        get_input_output_paths('file.py', 'file.py', None)
    assert tuple(get_input_output_paths('file.py', 'file.py', None)) == (InputOutput(Path('file.py'), Path('file.py')),)
    assert tuple(get_input_output_paths('file.py', 'out', None)) == (InputOutput(Path('file.py'), Path('out', 'file.py')),)
    assert tuple(get_input_output_paths('file.py', 'out', 'in'))

# Generated at 2022-06-14 01:39:11.615915
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert (list(get_input_output_paths('tests/data/input/',
                                        'tests/data/output/',
                                        'tests/data/input/')) == [
        InputOutput(Path('tests/data/input/main.py'),
                    Path('tests/data/output/main.py')),
        InputOutput(Path('tests/data/input/sub/sub.py'),
                    Path('tests/data/output/sub/sub.py')),
    ])

# Generated at 2022-06-14 01:39:20.123639
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('tests/random_file.py', 'doesnt_exist.py', None))
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('tests/random_file.py', 'tests/random_file.txt', None))
    paths = list(get_input_output_paths('test_files/hello.py', 'test_files/output.py', None))
    assert paths[0].input_path.name == "hello.py"
    assert paths[0].output_path.name == "output.py"
    paths = list(get_input_output_paths('test_files', 'test_files/output_dir', None))
    assert paths[0].input_

# Generated at 2022-06-14 01:39:30.288943
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('in.txt', 'out.py', None))
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('inexistent.py', 'out.txt', None))

    assert list(get_input_output_paths(
        'in.py', 'out.py', None)) == [InputOutput(Path('in.py'), Path('out.py'))]
    assert list(get_input_output_paths(
        'in.py', 'out.txt', None)) == [InputOutput(Path('in.py'), Path('out.txt'))]


# Generated at 2022-06-14 01:39:38.268169
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # test for case: input_path is a file, output_path is a file
    input_path = Path('/home/user/example.py')
    output_path = Path('/home/user/example_new.py')
    actual = get_input_output_paths(input_path, output_path, None)
    expected = [InputOutput(Path('/home/user/example.py'), Path('/home/user/example_new.py'))]
    assert list(actual) == expected

    # test for case: input_path is a file, output_path is a directory
    input_path = Path('/home/user/example.py')
    output_path = Path('/home/user/')
    actual = get_input_output_paths(input_path, output_path, None)

# Generated at 2022-06-14 01:39:48.342621
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    def _test(input_, output, root, expected):
        def _strify(path):
            return path.as_posix()

        assert list(map(_strify, get_input_output_paths(input_, output, root))) == list(map(_strify, expected))

    _test('input', 'output', 'root', [InputOutput(Path('input'), Path('output') / 'input')])
    _test('input', 'output', None, [InputOutput(Path('input'), Path('output') / 'input')])

    _test('input.py', 'output', 'root', [InputOutput(Path('input.py'), Path('output') / 'input.py')])
    _test('input.py', 'output.py', 'root', [InputOutput(Path('input.py'), Path('output.py'))])

# Generated at 2022-06-14 01:40:27.948200
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('test_data/test1.py', 'output/', None)) == [
        InputOutput(Path('test_data/test1.py'), Path('output/test1.py'))
    ]
    assert list(get_input_output_paths('test_data', 'output/', None)) == [
        InputOutput(Path('test_data/test1.py'), Path('output/test1.py')),
        InputOutput(Path('test_data/test2.py'), Path('output/test2.py')),
        InputOutput(Path('test_data/test3.py'), Path('output/test3.py')),
    ]

# Generated at 2022-06-14 01:40:32.729463
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path

    def str_to_path(path_str):
        return Path(path_str.lstrip('/'))

    # Trying to compare paths with Path().glob()
    assert list(get_input_output_paths("foo.py", "bar/baz.py", ".")) \
        == [InputOutput(str_to_path("foo.py"), str_to_path("bar/baz.py"))]
    assert list(get_input_output_paths("foo/foo.py", "bar/baz.py", ".")) \
        == [InputOutput(str_to_path("foo/foo.py"), str_to_path("bar/baz.py"))]

# Generated at 2022-06-14 01:40:42.910180
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .exceptions import InputDoesntExists, InvalidInputOutput
    from .types import InputOutput

    assert list(get_input_output_paths('input/name.py', 'output', None)) == [
        InputOutput(Path('input/name.py'), Path('output/name.py'))]
    assert list(get_input_output_paths('input/name.py', '/tmp/output', None)) == [
        InputOutput(Path('input/name.py'), Path('/tmp/output/name.py'))]
    assert list(get_input_output_paths('input', 'output', None)) == [
        InputOutput(Path('input/name.py'), Path('output/name.py'))]

# Generated at 2022-06-14 01:40:58.093567
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert (list(get_input_output_paths(
            'resources/boto3/setup.py',
            'solution/boto3/setup.py',
            None)) ==
            [InputOutput(Path('resources/boto3/setup.py'),
                         Path('solution/boto3/setup.py'))])
    assert (list(get_input_output_paths(
            'resources/boto3/setup.py',
            'solution',
            None)) ==
            [InputOutput(Path('resources/boto3/setup.py'),
                         Path('solution/setup.py'))])

# Generated at 2022-06-14 01:41:06.438277
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('a/b.py', 'x/y/b/c.py','a')) == \
        [InputOutput(Path('a/b.py'), Path('x/y/b/c.py'))]
    assert list(get_input_output_paths('a/b.py', 'x/y.py', 'a')) == \
        [InputOutput(Path('a/b.py'), Path('x/y.py'))]
    assert list(get_input_output_paths('a/b.py', 'x/y.py', 'c')) == \
        [InputOutput(Path('a/b.py'), Path('x/y.py'))]

# Generated at 2022-06-14 01:41:15.403254
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    import os
    import shutil
    import tempfile

    def create_files(root, files):
        for file in files:
            file_path = os.path.join(root, file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'a'):
                pass

    def assert_expected(expected, actual):
        for input_output in expected:
            assert input_output in actual

    with tempfile.TemporaryDirectory() as temp_dir:
        input_output_temp_dir = os.path.join(temp_dir, 'temp')
        input_temp_dir = os.path.join(temp_dir, 'input')
        os.makedirs

# Generated at 2022-06-14 01:41:17.290589
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    print(get_input_output_paths('tests/fixtures/input', 'tests/fixtures/output', 'tests/fixtures'))

# Generated at 2022-06-14 01:41:23.214926
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "./../static/in"
    output = "./../static/out"
    root = None
    paths = get_input_output_paths(input_, output, root)
    pairs = list(paths)

    assert len(pairs) == 2

# Generated at 2022-06-14 01:41:33.783772
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    root = Path().resolve()
    i1 = root.joinpath('file.py')
    o1 = root.joinpath('output.py')
    i2 = root.joinpath('folder')
    o2 = root.joinpath('output')
    i3 = root.joinpath('folder')
    o3 = root.joinpath('output.py')
    i4 = root.joinpath('file.py')
    o4 = root.joinpath('output')

    def t1(input_: str, output: str, root_: str):
        expected = InputOutput(i1, o1)
        actual = get_input_output_paths(input_, output, root_).__next__()
        assert expected.input_ == actual.input_
        assert expected.output == actual.output


# Generated at 2022-06-14 01:41:48.994147
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from .exceptions import InvalidInputOutput, InputDoesntExists

    input_ = Path('C:/tmp/a.py')
    output = Path('C:/output')
    root = Path('C:/tmp')
    paths = [
        (InputOutput(input_, output), []),
        (InputOutput(input_, output / 'a.py'), []),
        (InvalidInputOutput, ['output']),
        (InvalidInputOutput, ['input_']),
    ]
    output_ = list(get_input_output_paths(input_, output, root))
    assert output_ == paths

    input_ = Path('C:/tmp')
    output = Path('C:/output')
    root = Path('C:/tmp')

# Generated at 2022-06-14 01:43:10.914654
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # output is a .py file but input isn't
    with pytest.raises(InvalidInputOutput) as e_info:
        get_input_output_paths(input_='./my_package/tests/test_foo.py',
                               output='./my_package/tests/bar.py',
                               root='./my_package')

    # output is a .py file and input is a .py file
    input_output = next(
        get_input_output_paths(input_='./my_package/tests/test_foo.py',
                               output='./my_package/tests/test_bar.py',
                               root='./my_package'))
    assert input_output.input == './my_package/tests/test_foo.py'