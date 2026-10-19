

# Generated at 2022-06-14 01:33:15.628985
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    iopathes = get_input_output_paths('root/a', 'output/a', 'root/a')
    for iopath in iopathes:
        assert iopath.input.name == iopath.output.name

# Generated at 2022-06-14 01:33:22.229349
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # path, path
    paths = get_input_output_paths('a.py', 'b.py', None)
    assert list(paths) == [InputOutput(Path('a.py'), Path('b.py'))]

    # path, path
    paths = get_input_output_paths('a/b/c.py', 'd/e/f.py', None)
    assert list(paths) == [InputOutput(Path('a/b/c.py'), Path('d/e/f.py'))]

    # path, directory
    paths = get_input_output_paths('a.py', 'b', None)
    assert list(paths) == [InputOutput(Path('a.py'), Path('b/a.py'))]

    # path, directory
    paths = get_input

# Generated at 2022-06-14 01:33:32.667069
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # given
    input_ = '/root/mypackage/my_file.py'
    output = '/output/package_name'
    root = '/root'

    # when function get_input_output_paths is called
    result = get_input_output_paths(input_, output, root)

    # then Path should be returned
    assert next(result) == InputOutput(Path('/root/mypackage/my_file.py'), Path('/output/package_name/mypackage/my_file.py'))




# Generated at 2022-06-14 01:33:43.858954
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get input output paths."""
    assert get_input_output_paths('file.py', 'outfile.py') == [InputOutput(Path('file.py'), Path('outfile.py'))]

    assert get_input_output_paths('file.py', 'outdir') == [InputOutput(Path('file.py'), Path('outdir/file.py'))]
    assert get_input_output_paths('dir', 'outdir') == [InputOutput(Path('dir/file.py'), Path('outdir/file.py'))]

    assert get_input_output_paths('dir', 'outdir', 'dir') == [InputOutput(Path('dir/file.py'), Path('outdir/file.py'))]

# Generated at 2022-06-14 01:33:52.593046
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths"""
    # case 1:
    #     input_: "../test/test_data/test_input_output_paths/1.py"
    #     output: "../test/test_data/test_input_output_paths/test_output"
    input_ = "../test/test_data/test_input_output_paths/1.py"
    output = "../test/test_data/test_input_output_paths/test_output"
    input_output_paths = get_input_output_paths(input_, output, root=None)
    assert len(input_output_paths) == 1
    assert input_output_paths.__next__().input == Path(input_)
    assert input_output_paths.__next

# Generated at 2022-06-14 01:34:02.193620
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    iop = get_input_output_paths('input/', 'output/', None)
    assert list(iop) == [
        InputOutput(Path('input/a.py'), Path('output/')),
        InputOutput(Path('input/b.py'), Path('output/')),
        InputOutput(Path('input/c.py'), Path('output/')),
    ]

    iop = get_input_output_paths('input/a.py', 'output/a.py', None)
    assert list(iop) == [
        InputOutput(Path('input/a.py'), Path('output/a.py')),
    ]

    iop = get_input_output_paths('input/a.py', 'output/', None)

# Generated at 2022-06-14 01:34:10.855858
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_pairs = get_input_output_paths('/a/b/c/d/f.py', '/a/b/c/d/e/g.py', '/a/b/c/d')
    with pytest.raises(InputDoesntExists):
        get_input_output_paths('/a/b/c/d/l.py', '/a/b/c/d/e/g.py', '/a/b/c/d')
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('/a/b/c/d/l.py', '/a/b/c/d/e/g.txt', '/a/b/c/d')

# Generated at 2022-06-14 01:34:19.894077
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    inp = "test_docs"
    out = "test_out"
    in_out = get_input_output_paths(inp, out, None)
    in_out = list(in_out)
    assert len(in_out) == 2
    assert in_out[0][0] == Path("test_docs/index.py")
    assert in_out[1][0] == Path("test_docs/index2.py")
    assert in_out[0][1] == Path("test_out/index.py")
    assert in_out[1][1] == Path("test_out/index2.py")

# Generated at 2022-06-14 01:34:26.957103
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    results = get_input_output_paths('../input_folder/temp/', '../output_folder/temp/', '../input_folder/temp/')
    assert list(results) == [InputOutput(Path('../input_folder/temp/'), Path('../output_folder/temp/')), 
                             InputOutput(Path('../input_folder/temp/InputOutput.py'), Path('../output_folder/temp/InputOutput.py')), 
                             InputOutput(Path('../input_folder/temp/InputOutput.pyc'), Path('../output_folder/temp/InputOutput.pyc')), 
                             InputOutput(Path('../input_folder/temp/__init__.py'), Path('../output_folder/temp/__init__.py'))]

# Generated at 2022-06-14 01:34:38.021263
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    data_dir = os.path.dirname(os.path.realpath(__file__))
    input_dir = os.path.join(data_dir, "data/input")
    output_dir = os.path.join(data_dir, "data/output")

# Generated at 2022-06-14 01:34:52.553312
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for get_input_output_paths"""
    input_1 = './test_foo.py'
    output_1 = './test_foo.py'
    input_2 = './test_foo.py'
    output_2 = './bar'
    input_3 = './bar'
    output_3 = './bar'
    input_4 = './test_dir'
    output_4 = './test_dir'

    try:
        input_output_paths = get_input_output_paths(input_1, output_1, '.')
    except Exception as e:
        assert False, "Failed to test case 1: %s" % str(e)

# Generated at 2022-06-14 01:35:02.614097
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test unit for function get_input_output_paths"""
    # Test 1: input and output are file
    try:
        list(get_input_output_paths('a.py', 'b.py', 'root'))
    except InvalidInputOutput:
        pass
    else:
        assert False
    # Test 2: input is file
    assert list(get_input_output_paths('a.py', 'root', 'root')) ==\
        [InputOutput(Path('a.py'), Path('root/a.py'))]
    # Test 3: input is directory

# Generated at 2022-06-14 01:35:17.280410
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    assert list(get_input_output_paths('setup.py', 'b.py', None)) \
        == [InputOutput(Path('setup.py'), Path('b.py'))]
    assert list(get_input_output_paths('a.py', 'b.py', None)) \
        == [InputOutput(Path('a.py'), Path('b.py'))]
    assert list(get_input_output_paths('a.py', 'b', None)) \
        == [InputOutput(Path('a.py'), Path('b/a.py'))]

# Generated at 2022-06-14 01:35:27.403170
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    #input_: str, output: str, root: Optional[str]) -> Iterable[InputOutput]
    # Case 1: Regular Case
    input_ = "/Users/jeffreychen/Documents/SoftwareEngineering/cse-110-team-project/team_project/migrations/0014_auto_20200409_2029.py"
    output = "/Users/jeffreychen/Documents/SoftwareEngineering/cse-110-team-project/team_project/migrations/0014_auto_20200409_2029NEW.py"
    root = "/Users/jeffreychen/Documents/SoftwareEngineering/cse-110-team-project/team_project/migrations/0014_auto_20200409_2029.py"
   

# Generated at 2022-06-14 01:35:38.250477
# Unit test for function get_input_output_paths
def test_get_input_output_paths():

    # Test output end with .py
    input_ = "folder1/folder2/input.py"
    output = "folder3/folder4/output.py"
    root = None
    assert list(get_input_output_paths(input_, output, root)) == \
        [InputOutput(Path(input_), Path(output))]

    # Test input end not with .py
    input_ = "folder1/folder2/input"
    output = "folder3/folder4/output"
    root = None

# Generated at 2022-06-14 01:35:47.818218
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    paths = get_input_output_paths('tests/data/', 'tests/out/data/', 'tests/data')
    assert {str(p.input_path): str(p.output_path) for p in paths} == \
        {"tests/data/file_a.py": "tests/out/data/file_a.py",
            "tests/data/file_b.py": "tests/out/data/file_b.py",
            "tests/data/path/to/file_c.py": "tests/out/data/path/to/file_c.py"}

# Generated at 2022-06-14 01:35:56.851953
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from .helpers import mk_py_file, remove_files


# Generated at 2022-06-14 01:36:01.274527
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_path = '../'
    output_path = '../'
    root = '../'
    _ = get_input_output_paths(input_path, output_path, root)

# Generated at 2022-06-14 01:36:09.080536
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths function."""
    assert list(get_input_output_paths('tests/fixtures/input.py', 'tests/fixtures/output.py', 'tests/fixtures/input.py')) == [InputOutput(Path('tests/fixtures/input.py'), Path('tests/fixtures/output.py'))]
    assert list(get_input_output_paths('tests/fixtures/input.py', 'tests/fixtures/output/', 'tests/fixtures/input.py')) == [InputOutput(Path('tests/fixtures/input.py'), Path('tests/fixtures/output/input.py'))]

# Generated at 2022-06-14 01:36:16.887405
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Iterate over the files in the given input directory to the desired output."""
    test_path = Path(__file__).parent
    input_ = test_path.joinpath('test_input.py')
    output = test_path.joinpath('test_output.py')
    root = test_path
    paths = get_input_output_paths(input_, output, root)
    assert paths[0].input == input_
    assert paths[0].output == output

# Generated at 2022-06-14 01:36:28.808409
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Return multiple Paths if input is a directory
    result = get_input_output_paths("../tests/input/m3", "../tests/output", "../tests/input")
    result_str = [(str(x.input), str(x.output)) for x in result]
    assert result_str == [('../tests/input/m3/module1.py', '../tests/output/module1.py'), ('../tests/input/m3/module2.py', '../tests/output/module2.py'), ('../tests/input/m3/module2/module3.py', '../tests/output/module2/module3.py')]

    # Return single Path if input is a file

# Generated at 2022-06-14 01:36:34.749855
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # testing single file as input
    input_ = './tests/fixtures/simple_tests/simple_test.py'
    output = './tests/fixtures/coverage_results'
    paths = list(get_input_output_paths(input_, output, root=None))
    assert paths[0].input_path == Path(
        './tests/fixtures/simple_tests/simple_test.py')
    assert paths[0].output_path == Path(
        './tests/fixtures/coverage_results/simple_test.py')

    # testing directory as input
    input_ = './tests/fixtures/simple_tests/'
    output = './tests/fixtures/coverage_results/'
    paths = list(get_input_output_paths(input_, output, root=None))

# Generated at 2022-06-14 01:36:42.172610
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths function."""
    assert list(get_input_output_paths('test_data/test.py',
        'test_data/example.py', 'test_data')) == list([InputOutput(
        Path('test_data/test.py'), Path('test_data/example.py'))])
    assert list(get_input_output_paths('test_data/test.py',
        'test_data/', 'test_data')) == list([InputOutput(
        Path('test_data/test.py'), Path('test_data/test.py'))])

# Generated at 2022-06-14 01:36:48.213305
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Tests for function get_input_output_paths."""
    # Invalid arguments
    with pytest.raises(InvalidInputOutput):
        next(get_input_output_paths('test.txt', 'test.py', None))
    
    with pytest.raises(InputDoesntExists):
        next(get_input_output_paths('test_does_not_exist.py', 
                                    'test.py', None))
    
    # Valid arguments
    # input.py out.py
    input_output_i1 = get_input_output_paths(
        input_='test/input.py', output='test/out.py', root=None)

# Generated at 2022-06-14 01:36:58.829712
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths."""
    here = Path(__file__).parent
    input_path = here / 'sample_input/a/b/c.py'
    output_path = here / 'sample_output'
    root_path = here / 'sample_input'
    input_paths = list(get_input_output_paths(str(input_path), str(output_path), str(root_path)))
    expected_output_paths = [
        Path('./sample_output/a/b/c.py'),
        Path('./sample_output/a/b/c.pyc'),
    ]
    assert len(input_paths) == 2

# Generated at 2022-06-14 01:37:08.895664
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from nose.tools import assert_equal, assert_true
    from .utils import TemporaryDirectory
    from .config import get_paths

    with TemporaryDirectory() as root:
        root_path = Path(root)
        parent_path = root_path.joinpath('parent')
        parent_path.mkdir()
        sub_path = parent_path.joinpath('sub')
        sub_path.mkdir()
        child_input = sub_path.joinpath('child.py')
        child_input.touch()
        child_output = root_path.joinpath('child.py')
        parent_output = root_path.joinpath('parent')


# Generated at 2022-06-14 01:37:18.390598
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths"""
    from os.path import dirname
    root = dirname(__file__)

# Generated at 2022-06-14 01:37:28.477189
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths function."""
    i, o = get_input_output_paths('in.py', 'out.py', '')
    assert str(i) == 'in.py'
    assert str(o) == 'out.py'

    i, o = get_input_output_paths('in.py', 'out', '')
    assert str(i) == 'in.py'
    assert str(o) == 'out/in.py'

    i, o = get_input_output_paths('in', 'out', '')
    assert str(i) == 'in'
    assert str(o) == 'out/in'

# Generated at 2022-06-14 01:37:37.331760
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # test get_input_output_paths function
    inp1 = "foo.py"
    out1 = "bar.py"
    ret1 = list(get_input_output_paths(inp1, out1, None))
    assert [(Path(inp1), Path(out1))] == ret1

    inp2 = "foo.py"
    out2 = "bar/"
    ret2 = list(get_input_output_paths(inp2, out2, None))
    assert [(Path(inp2), Path(out2, "foo.py"))] == ret2

    # test invalid arguments
    # input file is not python file

# Generated at 2022-06-14 01:37:47.592379
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths(
        'file.py', 'output.py', None)) == [InputOutput(Path('file.py'), Path('output.py'))]
    assert list(get_input_output_paths(
        'file.py', 'folder', None)) == [InputOutput(Path('file.py'), Path('folder').joinpath('file.py'))]
    assert list(get_input_output_paths(
        'file.py', 'folder/', None)) == [InputOutput(Path('file.py'), Path('folder/').joinpath('file.py'))]

# Generated at 2022-06-14 01:38:02.370521
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths on all possible cases."""
    # Case 1: Input and output as Dir/filename.py
    input_ = "/Users/mukul/Desktop/input.py"
    output = "/Users/mukul/Desktop/output.py"
    assert list(get_input_output_paths(input_, output, None)) == [InputOutput(Path("/Users/mukul/Desktop/input.py"), Path("/Users/mukul/Desktop/output.py"))]

    # Case 2: Input as Dir/filename.py and output as Dir/
    input_ = "/Users/mukul/Desktop/input.py"
    output = "/Users/mukul/Desktop"

# Generated at 2022-06-14 01:38:12.425465
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # If all arguments are file, it should work
    assert list(get_input_output_paths('a', 'b', None)) == [(Path('a'), Path('b'))]
    # If the directory output is a file, it should raise InvalidInputOutput
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths('a', 'b', None)

    # If the root is not None, and input is a file, it should work
    assert list(get_input_output_paths('a', 'b', 'root')) == [(Path('a'), Path('b').joinpath(Path('a').relative_to(Path('root'))))]
    # If the root is not None, and input is a directory, it should work

# Generated at 2022-06-14 01:38:22.147606
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from pathlib import Path
    from .exceptions import InvalidInputOutput, InputDoesntExists

    root_path = Path.cwd()
    input_output = (root_path.parent.joinpath("test.py"),
                    root_path.parent.joinpath("test1.py"))
    input_output_lst = [(input_output[0], input_output[1])]

    # Test case 1: input is a file and output is a directory
    assert list(get_input_output_paths(str(input_output[0]),
                                       str(input_output[1].parent),
                                       str(root_path.parent))) == input_output_lst

    # Test case 2: input and output are both directories

# Generated at 2022-06-14 01:38:26.057874
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    assert get_input_output_paths(
        input_='examples/example1.py',
        output='output/example1.py',
        root=None) == [InputOutput(
            input_=Path('examples/example1.py'),
            output=Path('output/example1.py'))]

# Generated at 2022-06-14 01:38:32.067980
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import os

    iop = get_input_output_paths('path/to/input', 'path/to/output',
                                 None)
    input_paths = [x.input for x in iop]
    output_paths = [x.output for x in iop]

    base_path = os.path.abspath(os.path.dirname(__file__))
    assert input_paths == [os.path.join(base_path, 'path/to/input')]
    assert output_paths == [os.path.join(base_path, 'path/to/output')]


# Generated at 2022-06-14 01:38:37.643547
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths()"""
    try:
        for input_, output in get_input_output_paths("test.py", "test.py"):
            assert input_ == Path("test.py")
            assert output == Path("test.py")
    except Exception as e:
        print("test_get_input_output_paths() failed:", e)

# Generated at 2022-06-14 01:38:42.591930
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_get_input_output_paths_1()
    test_get_input_output_paths_2()
    test_get_input_output_paths_3()
    test_get_input_output_paths_4()
    test_get_input_output_paths_5()
    test_get_input_output_paths_6()


# Generated at 2022-06-14 01:38:52.919742
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Testing for function get_input_output_paths"""
    assert list(get_input_output_paths('aa/bb.py', 'cc/dd', 'aa')) == [
        InputOutput(Path('aa/bb.py'), Path('cc/dd/bb.py'))
    ]

    assert list(get_input_output_paths('aa', 'cc', 'aa')) == [
        InputOutput(Path('aa/aa.py'), Path('cc/aa.py')),
        InputOutput(Path('aa/bb.py'), Path('cc/bb.py')),
        InputOutput(Path('aa/cc/aa.py'), Path('cc/cc/aa.py')),
        InputOutput(Path('aa/cc/bb.py'), Path('cc/cc/bb.py'))
    ]


# Generated at 2022-06-14 01:38:59.075552
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    try:
        for _ in get_input_output_paths(input_='main.py', output='/home', root=None):
            pass
    except InputDoesntExists:
        pass
    else:
        assert False

# Generated at 2022-06-14 01:39:12.444768
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'tests/data'
    output = 'tests/data/output'

    input_child = 'tests/data/child'
    output_child = 'tests/data/output/child'

    input_grandchild = 'tests/data/child/grandchild'
    output_grandchild = 'tests/data/output/child/grandchild'

    assert get_input_output_paths(input_, output, '') == [
        InputOutput(Path(input_child), Path(output_child)),
        InputOutput(Path(input_grandchild), Path(output_grandchild)),
        InputOutput(Path(input_), Path(output))
    ]


# Generated at 2022-06-14 01:39:33.777242
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    path_pairs = get_input_output_paths("./test_files/function/function1.py",
                                        "./test_files/function", None)
    assert path_pairs.__next__() == InputOutput(Path("./test_files/function/function1.py"),
                                                Path("./test_files/function/function1.py"))
    path_pairs = get_input_output_paths("./test_files/",
                                        "./test_files/function", None)
    assert path_pairs.__next__() == InputOutput(Path("./test_files/function/function1.py"),
                                                Path("./test_files/function/function1.py"))



# Generated at 2022-06-14 01:39:43.545471
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = 'example/src'
    output = 'example/dst'

# Generated at 2022-06-14 01:39:50.269605
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    pairs = get_input_output_paths('test.py', 'destination.py', None)

    assert len(list(pairs)) == 1
    pair = next(pairs)
    assert pair.input.name == 'test.py'
    assert pair.output.name == 'destination.py'

    pairs = get_input_output_paths('test.py', 'destination', None)
    assert len(list(pairs)) == 1
    pair = next(pairs)
    assert pair.input.name == 'test.py'
    assert pair.output.name == 'test.py'


    pairs = get_input_output_paths('test', 'destination', None)
    assert len(list(pairs)) == 1
   

# Generated at 2022-06-14 01:40:01.769977
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths"""
    cases = [
        ('foo.py', 'foo.py', None),
        ('foo.py', 'bar.py', None),
        ('foo.py', 'foo/bar.py', None),
        ('foo.py', 'foo/bar.py', 'test/data'),
        ('foo.py', 'bar/bar.py', 'test/data'),
        ('test/data', 'foo', None),
        ('test/data', 'foo', 'test/data'),
        ('test/data', 'foo', 'test'),
    ]


# Generated at 2022-06-14 01:40:16.488117
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_get_input_output_paths._input_dir = Path(dirname(__file__))
    test_get_input_output_paths._input_dir1 = Path(Path(dirname(__file__)).parent).joinpath('test_dir')
    test_get_input_output_paths._input_dir2 = Path(Path(dirname(__file__)).parent).joinpath('test_dir2')
    test_get_input_output_paths._input_dir3 = Path(Path(dirname(__file__)).parent).joinpath('test_dir3')

    def test_input_exists(input_, output):
        input_path = Path(input_)
        output_path = Path(output)

# Generated at 2022-06-14 01:40:25.403103
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('foo.py', 'out', None)) == \
        [InputOutput(Path('foo.py'), Path('out/foo.py'))]

    assert list(get_input_output_paths('foo.py', 'out.py', None)) == \
        [InputOutput(Path('foo.py'), Path('out.py'))]

    assert list(get_input_output_paths('foo.txt', 'out.py', None)) == []

    assert list(get_input_output_paths('foo', 'out', None)) == \
        [InputOutput(Path('foo/a.py'), Path('out/a.py'))]


# Generated at 2022-06-14 01:40:31.414404
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    def test_get_input_output_pairs(input, output, root, pairs, has_exception):
        iter = get_input_output_paths(input, output, root)
        for i, (input, output) in enumerate(iter):
            assert input.resolve() == pairs[i][0].resolve()
            assert output.resolve() == pairs[i][1].resolve()
        try:
            next(iter)
        except StopIteration:
            assert not has_exception
        else:
            assert has_exception
    # >>> test_get_input_output_pairs

# Generated at 2022-06-14 01:40:40.499797
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """
    This is the unit test case for the function get_input_output_paths.
    """
    from pathlib import Path
    from .consts import TEST_PATH
    from .helpers import create_files_at

    with create_files_at(TEST_PATH, 'temp/temp.py', 'a.py', 'b.py') as (a_py, b_py, temp_py):
        # when input file doesn't exist
        with pytest.raises(InputDoesntExists):
            get_input_output_paths(input_='temp.py', output='out', root=None)

        # when input and output file are same, then return generator with single InputOutput tuple

# Generated at 2022-06-14 01:40:46.819554
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test with a non-existent directory
    with pytest.raises(InputDoesntExists):
        get_input_output_paths("", "", None)
    # Test with a non-existent root directory
    with pytest.raises(InputDoesntExists):
        get_input_output_paths("", "", "")

if __name__ == '__main__':
    test_get_input_output_paths()

# Generated at 2022-06-14 01:40:55.723783
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    def validate(input_, output, root, content):
        try:
            assert_equal(content, list(get_input_output_paths(input_, output, root)))
        except:
            print("input: ", input_)
            print("output: ", output)
            print("root: ", root)
            print("content: ", content)
            raise

    validate("/tmp/file.py", "/tmp/output.py", None, [(Path("/tmp/file.py"), Path("/tmp/output.py"))])
    validate("/tmp/file.py", "/tmp/output", None, [(Path("/tmp/file.py"), Path("/tmp/output/file.py"))])