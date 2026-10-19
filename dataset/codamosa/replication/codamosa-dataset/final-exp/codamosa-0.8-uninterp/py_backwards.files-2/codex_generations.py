

# Generated at 2022-06-14 01:33:06.257799
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "tests/fixtures/test_directory/test1.py"
    output = "tests/fixtures/test_directory/test1_output.py"
    root = 'tests/fixtures/test_directory'
    input_output = get_input_output_paths(input_, output, root)
    assert input_output is not None
    assert len(input_output) == 1
    assert str(input_output[0].input) == input_
    assert str(input_output[0].output) == output

# Generated at 2022-06-14 01:33:15.742731
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths(input_='.', output='.', root=None)) == [
        InputOutput(Path('.', 'foo.py'),
                    Path('.', 'foo.py')),
        InputOutput(Path('.', 'bar', 'bar.py'),
                    Path('.', 'bar', 'bar.py'))]
    assert list(get_input_output_paths(input_='.', output='./output', root=None)) == [
        InputOutput(Path('.', 'foo.py'),
                    Path('.', 'output', 'foo.py')),
        InputOutput(Path('.', 'bar', 'bar.py'),
                    Path('.', 'output', 'bar', 'bar.py'))]

# Generated at 2022-06-14 01:33:22.269289
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """ Test get_input_output_paths function """
    # Test filename
    i = 'f1.py'
    o = 'f2.py'
    result = get_input_output_paths(i, o, '.')
    assert next(result) == InputOutput(Path('f1.py'), Path('f2.py'))

    # Test file in folder and output to the same folder
    i = 'test/f1.py'
    o = '.'
    result = get_input_output_paths(i, o, '.')
    assert next(result) == InputOutput(Path('test/f1.py'), Path('f1.py'))

    # Test input file doesn't exist
    with pytest.raises(InputDoesntExists):
        i = 'a/f1.py'

# Generated at 2022-06-14 01:33:35.126378
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    pass
    # TODO
    # assert get_input_output_paths(
    #     input_='.', output='.',
    #     root=None
    # ) == [InputOutput(Path('.'), Path('.'))]
    # assert get_input_output_paths(
    #     input_='.', output='..',
    #     root=None
    # ) == [InputOutput(Path('.'), Path('..'))]
    # assert get_input_output_paths(
    #     input_='test', output='test',
    #     root=None
    # ) == [InputOutput(Path('test'), Path('test'))]

# Generated at 2022-06-14 01:33:45.863394
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # directory to directory
    for input_output in get_input_output_paths('./tests/files/a', './tests/files/b', './tests/files/a'):
        assert str(input_output.input_path) == './tests/files/a/a.py'
        assert str(input_output.output_path) == './tests/files/b/a.py'

    # directory to directory
    for input_output in get_input_output_paths('./tests/files/a', './tests/files/b', None):
        assert str(input_output.input_path) == './tests/files/a/a.py'
        assert str(input_output.output_path) == './tests/files/b/a/a.py'

    # directory to file


# Generated at 2022-06-14 01:33:52.672313
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from textwrap import dedent

    with tempfile.TemporaryDirectory() as tmpdirname:
        root = dedent("""
        - a.py
        - b.py
        - c.py
        - dir1
          - a.py
          - b.py
          - c.py
          - d.py
        - dir2
          - a.py
          - c.py
          - d.py
        """)
        root = dedent2sh(root).rstrip('\n')

        os.chdir(tmpdirname)
        os.system(root)


# Generated at 2022-06-14 01:34:02.225661
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    generated_data = get_input_output_paths('input', 'output', 'root')

    # Python 2.7 doesn't have yield from (or generator chaining)
    # so I had to do this.
    generated_data_items = []
    for item in generated_data:
        generated_data_items.append(item)


# Generated at 2022-06-14 01:34:10.877127
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert get_input_output_paths('./dummy_input.txt', './dummy_output', None) == [InputOutput(Path('./dummy_input.txt'), Path('./dummy_output'))]
    assert get_input_output_paths('./dummy_input', './dummy_output', None) == [InputOutput(Path('./dummy_input/__init__.py'), Path('./dummy_output/__init__.py'))]
    assert get_input_output_paths('./dummy_input', './dummy_output', './') == [InputOutput(Path('./dummy_input/__init__.py'), Path('./dummy_output/__init__.py'))]

# Unit tests for exceptions InvalidInputOutput and Input

# Generated at 2022-06-14 01:34:17.649536
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = "test_code"
    output = "output"
    paths = get_input_output_paths(input_, output, None)
    for path_pair in paths:
        if Path(input_).joinpath(path_pair.input).is_file():
            assert Path(output).joinpath(path_pair.output).is_file()

# Generated at 2022-06-14 01:34:22.964447
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_ = './test/test_input_output.py'
    output = './test/test_input_output'
    for input_output in get_input_output_paths(input_=input_, output=output, root=None):
        if input_output.input.name == 'test_input_output.py':
            assert input_output.input == Path(input_)
            assert input_output.output == Path(output).joinpath(input_output.input.name)
        else:
            assert False

# Generated at 2022-06-14 01:34:36.496258
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_file = os.path.realpath(os.path.dirname(__file__))
    assert list(get_input_output_paths(
        os.path.join(test_file, 'input_dir', 'file.py'),
        os.path.join(test_file, 'output_dir'),
        os.path.join(test_file, 'input_dir'),
    )) == [InputOutput(
        Path(os.path.join(test_file, 'input_dir', 'file.py')),
        Path(os.path.join(test_file, 'output_dir', 'file.py')),
    )]

# Generated at 2022-06-14 01:34:43.872215
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test get_input_output_paths()"""
    assert [x for x in get_input_output_paths(
        input_='test', output='test_out', root=None)] == \
        [InputOutput(Path('test/main.py'), Path('test_out/main.py')),
         InputOutput(Path('test/submodule/submodule.py'),
                     Path('test_out/submodule/submodule.py'))]

    assert [x for x in get_input_output_paths(
        input_='test/main.py', output='test_out', root=None)] == \
        [InputOutput(Path('test/main.py'), Path('test_out/main.py'))]


# Generated at 2022-06-14 01:34:47.049568
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output = get_input_output_paths('', '', '')
    print(input_output)

# Generated at 2022-06-14 01:34:54.657396
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths"""
    python_file = 'file.py'
    input_folder = 'test_folder'
    output_folder = 'test_output'
    root = 'test_root'
    root_output = 'test_root_output'

    input_files = list(map(str, Path(input_folder).glob('**/*.py')))

    # Given a python file, .py extension is required in output
    output_file = 'file.py'
    output = [InputOutput(Path(python_file), Path(output_file))]
    assert list(get_input_output_paths(python_file, output_file, None)) == output

    # Given a python file, output can be a folder (python file is created inside folder)

# Generated at 2022-06-14 01:35:01.392296
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert tuple(get_input_output_paths(
        'a', 'b')) == (InputOutput(Path('a'), Path('b')),)
    assert tuple(get_input_output_paths(
        'a.py', 'b.py')) == (InputOutput(Path('a.py'), Path('b.py')),)
    assert tuple(get_input_output_paths(
        'a.py', 'b')) == (InputOutput(Path('a.py'), Path('b/a.py')),)
    assert tuple(get_input_output_paths(
        'a', 'b.py')) == (InputOutput(Path('a'), Path('b.py/a')),)

# Generated at 2022-06-14 01:35:08.701809
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""


# Generated at 2022-06-14 01:35:18.975930
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Test case 1: input and output are single file
    # Input
    input_ = 'test_input/a.py'
    output = 'test_output'
    root = None
    # Output
    output_ = [InputOutput(Path('test_input/a.py'), Path('test_output/a.py'))]
    # Actual output
    assert list(get_input_output_paths(input_, output, root)) == output_

    # Test case 2: input and output are single file
    # Input
    input_ = 'test_input/a.py'
    output = 'test_output/a.py'
    root = None
    # Output
    output_ = [InputOutput(Path('test_input/a.py'), Path('test_output/a.py'))]
    # Actual output
   

# Generated at 2022-06-14 01:35:30.178213
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input', 'output.py', None))

    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('input/foo.py', 'output/', None))

    with pytest.raists(InputDoesntExists):
        list(get_input_output_paths('input/foo.py', 'output/foo.py', None))

    inputs_outputs = list(get_input_output_paths('input.py', 'output/input.py', None))
    expected = [
        InputOutput(Path('input.py'), Path('output/input.py'))
    ]
    assert inputs_outputs == expected


# Generated at 2022-06-14 01:35:39.153742
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('/', '/')) == [InputOutput(Path('/'), Path('/'))]

    # one file
    assert list(get_input_output_paths('/1.py', '/')) == [InputOutput(Path('/1.py'), Path('/1.py'))]
    assert list(get_input_output_paths('/1.py', '/2.py')) == [InputOutput(Path('/1.py'), Path('/2.py'))]

    # many files


# Generated at 2022-06-14 01:35:49.964080
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    assert tuple(get_input_output_paths('in', 'out', None)) == (
        InputOutput(Path('in'), Path('out')),
    )
    assert tuple(get_input_output_paths('./test/test_data/',
                                        './test/test_data/',
                                        None)) == (
        InputOutput(Path('./test/test_data/test_data.py'),
                    Path('./test/test_data/test_data.py')),
    )

# Generated at 2022-06-14 01:36:17.223851
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    dir_input = 'test/unit/test_utils.py'
    dir_output = 'test/unit'
    dir_root = None

    # Test that a single file can be moved to a directory without errors
    input_output = get_input_output_paths(dir_input, dir_output, dir_root)
    assert input_output[0].input_ == Path('test/unit/test_utils.py')
    assert input_output[0].output == Path('test/unit/test_utils.py')

    # Test error raised when output is a file and input is a directory
    with pytest.raises(InvalidInputOutput):
        input_output = get_input_output_paths(dir_output, dir_input, dir_root)

    # Test error raise when input does not exist

# Generated at 2022-06-14 01:36:27.940504
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Input/output are different and they are files
    list(get_input_output_paths('/tmp/test1.py', '/tmp/test2.py', None))

    # Input/output are different and they are directories
    list(get_input_output_paths('/tmp/test1.py', '/tmp', None))

    # should raise error, input is directory and output is file
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('/tmp/test1', '/tmp/test2.py', None))

    # input file doesn't exist
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('/tmp/test2.py', '/tmp/test2.py', None))

    # input is directory and output is

# Generated at 2022-06-14 01:36:38.187889
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    here = Path(__file__).parent
    parent = here.parent
    def_test_dir = here.joinpath('test_dir')
    def_input = def_test_dir.joinpath('input')
    def_output = def_test_dir.joinpath('output')


# Generated at 2022-06-14 01:36:51.767903
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_paths = list(get_input_output_paths('tests/fixtures/case1', 'tests/fixtures/case1_output', None))
    assert input_output_paths[0].input_path.samefile(Path('tests/fixtures/case1/b1.py'))
    assert input_output_paths[0].output_path.samefile(Path('tests/fixtures/case1_output/b1.py'))
    assert input_output_paths[1].input_path.samefile(Path('tests/fixtures/case1/utils/b2.py'))
    assert input_output_paths[1].output_path.samefile(Path('tests/fixtures/case1_output/utils/b2.py'))

# Generated at 2022-06-14 01:37:01.838851
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for get_input_output_paths function."""
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input', 'output.py', None))

    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input.py', 'output.py', None))

    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('input.py', 'output', None))

    assert list(get_input_output_paths('input.py', 'output', None)) == [
        InputOutput(Path('input.py'), Path('output/input.py')),
    ]

# Generated at 2022-06-14 01:37:11.754078
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    from collections import namedtuple
    from pytest import raises, fixture

    @fixture
    def test_directory(tmpdir):
        TestDirectory = namedtuple('TestDirectory', 'input output root')
        directory = tmpdir.mkdir('get_input_output_paths')
        directory.mkdir('root')
        directory.mkdir('input')
        directory.mkdir('input').join('file.py').write('foo')
        directory.mkdir('input').join('directory').mkdir('file.py').write('bar')
        directory.mkdir('output')
        directory.mkdir('output').join('file.py').write('baz')
        directory.mkdir('output').join('directory').mkdir('file.py').write('qux')

# Generated at 2022-06-14 01:37:19.219175
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    from os import path
    from pathlib import Path
    from tempfile import TemporaryDirectory

    def _check_input_output(input_: str, output: str) -> None:
        with TemporaryDirectory() as tmpdir:
            for input_output in get_input_output_paths(
                    input_, output, root=None):
                input_output.input.parent.mkdir(parents=True, exist_ok=True)
                input_output.input.touch()
                input_output.output.parent.mkdir(parents=True, exist_ok=True)
                input_output.output.touch()


# Generated at 2022-06-14 01:37:28.349517
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_paths = [
        ('a/b', 'c/d', 'a/b'),
        ('a/b', 'c/d', '.'),
        ('a/b', 'd', '.'),
        ('a/b.py', 'c/d.py', '.'),
    ]
    for input_, output, root in test_paths:
        for path in get_input_output_paths(input_, output, root):
            assert path.input.is_file()
            assert path.output.parent.exists()
            assert path.output.parent.is_dir()

# Generated at 2022-06-14 01:37:43.044053
# Unit test for function get_input_output_paths

# Generated at 2022-06-14 01:37:53.394173
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert [
        InputOutput(Path('input/foo.py'), Path('output/foo.py')),
        InputOutput(Path('input/bar.py'), Path('output/bar.py')),
    ] == list(get_input_output_paths('input', 'output', None))
    assert [
        InputOutput(Path('input/foo.py'), Path('output/foo.py')),
        InputOutput(Path('input/bar.py'), Path('output/bar.py')),
    ] == list(get_input_output_paths('input/foo.py', 'output/foo.py', None))

# Generated at 2022-06-14 01:38:25.994321
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test get_input_output_paths function."""
    root = Path(__file__).parent

    assert tuple(get_input_output_paths('1.py', '2.py', str(root))) == (
        InputOutput(Path(__file__).joinpath('1.py'),
                    Path(__file__).joinpath('2.py')),
    )

    assert tuple(get_input_output_paths('1.py', '2', str(root))) == (
        InputOutput(Path(__file__).joinpath('1.py'),
                    Path(__file__).joinpath('2', '1.py')),
    )


# Generated at 2022-06-14 01:38:33.177151
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('test.py', 'test.py', '.')) == [InputOutput(Path('test.py'), Path('test.py'))]
    assert list(get_input_output_paths('test', 'test.py', '.')) == [InputOutput(Path('test.py'), Path('test').joinpath(Path('test.py')))]

    assert list(get_input_output_paths('test.py', 'test/test.py', '.')) == [InputOutput(Path('test.py'), Path('test').joinpath(Path('test.py')))]

# Generated at 2022-06-14 01:38:38.775882
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test for get_input_output_paths"""

# Generated at 2022-06-14 01:38:48.433171
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    assert list(get_input_output_paths('a.py', 'b.py', None)) == [
        InputOutput(Path('a.py'), Path('b.py'))]
    assert list(get_input_output_paths('a.py', 'b', None)) == [
        InputOutput(Path('a.py'), Path('b').joinpath('a.py'))]
    assert list(get_input_output_paths('a', 'b', None)) == [
        InputOutput(Path('a').joinpath('a.py'), Path('b').joinpath('a.py'))]

# Generated at 2022-06-14 01:38:57.495194
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output_paths = get_input_output_paths(
        './tests/fixtures/input/',
        './tests/fixtures/output/',
        './tests/fixtures/input/')


# Generated at 2022-06-14 01:39:07.226950
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    child_1 = Path('test').joinpath('file_1.py')
    child_2 = Path('test').joinpath('file_2.py')
    for input, output in get_input_output_paths('test', 'test_scrub', None):
        assert input == child_1 or input == child_2
        assert output == child_1.with_suffix('.pyc') or output == child_2.with_suffix('.pyc')

# Generated at 2022-06-14 01:39:17.986760
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """ Unit test for function get_input_output_paths """
    paths = [io for io in get_input_output_paths('tests/data', 'tests/data', None)]
    assert paths == [InputOutput(
        Path('tests/data/module.py'),
        Path('tests/data/module.py')),
        InputOutput(
            Path('tests/data/package/module.py'),
            Path('tests/data/package/module.py'))]
    paths = [io for io in get_input_output_paths('tests/data/package', 'tests/data/package', None)]
    assert paths == [InputOutput(
        Path('tests/data/package/module.py'),
        Path('tests/data/package/module.py'))]

# Generated at 2022-06-14 01:39:32.090732
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # testing InvalidInputOutput exception
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input.py', 'output.txt', None))

    # testing InputDoesntExists exception
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('non_existing_input.py', 'output.py', None))

    # testing get_input_output_paths
    # input is .py file and output is .py file
    io_list = list(get_input_output_paths('input.py', 'output.py', None))
    assert len(io_list) == 1
    assert io_list[0].input_path == Path('input.py')

# Generated at 2022-06-14 01:39:39.375980
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test function get_input_output_paths."""
    import pytest

    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('a', 'b.py', None))

    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('a.py', 'b.py', '.'))

    assert list(get_input_output_paths('a.py', 'b.py', None)) == [InputOutput(Path('a.py'), Path('b.py'))]

    assert list(get_input_output_paths('a.py', 'b', None)) == [InputOutput(Path('a.py'), Path('b/a.py'))]


# Generated at 2022-06-14 01:39:48.703852
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
	import pytest
	input_ = '/home/asf/asf/asd.py'
	output ='/home/asf/asf2/'
	root = '/home/asf/asf'

	with pytest.raises(InvalidInputOutput):
        		input_ = '/home/asf/asf/asd.py'
        		output ='/home/asf/asf2/asf.c'
        		get_input_output_paths(input_,output,root)

	with pytest.raises(InputDoesntExists):
        		input_ = '/home/asf/asf/asd.pyy'
        		output ='/home/asf/asf2/asf.c'

# Generated at 2022-06-14 01:40:57.116091
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    current_dir = Path(__file__).parent
    paths = list(get_input_output_paths(input_=current_dir,
                                        output=current_dir,
                                        root=current_dir))
    assert paths == [InputOutput(current_dir / 'test_file_system.py',
                                 current_dir / 'test_file_system.py')]

    # When a path is given
    paths = list(get_input_output_paths(input_=current_dir,
                                        output=current_dir / 'test_file_system.py',
                                        root=current_dir))
    assert paths == [InputOutput(current_dir / 'test_file_system.py',
                                 current_dir / 'test_file_system.py')]

    # When output is a file

# Generated at 2022-06-14 01:41:06.403370
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import tempfile
    import shutil
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdirname = Path(tmpdirname)
        subdir_a = tmpdirname.joinpath("a")
        subdir_b = tmpdirname.joinpath("b")
        subdir_a.mkdir()
        subdir_b.mkdir()

        input_f1 = subdir_a.joinpath("input_file_1.py")
        input_f1.touch()
        output_f1 = subdir_b.joinpath("input_file_1.py")

        input_f2 = subdir_a.joinpath("input_file_2.py")
        input_f2.touch()
        output_f2 = subdir_b.joinpath("input_file_2.py")



# Generated at 2022-06-14 01:41:15.357721
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Unit test for function get_input_output_paths."""
    print(get_input_output_paths('/home/usr/project/foo.py',
                                 '/home/usr/project/build/foo.py',
                                 '/home/usr/project/'))
    print(get_input_output_paths('/home/usr/project/foo.py',
                                 '/home/usr/project/build',
                                 '/home/usr/project/'))
    print(get_input_output_paths('/home/usr/project',
                                 '/home/usr/project/build',
                                 '/home/usr/project/'))
    print(get_input_output_paths('/home/usr/project',
                                 '/home/usr/project/build',
                                 None))

   

# Generated at 2022-06-14 01:41:21.769282
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    test_root = Path('/my/root_directory/')
    test_output = Path('/my/root_directory/output_directory')
    test_input = Path('/my/root_directory/root_script.py')
    test_input_directory = test_input.parent
    test_result = [InputOutput(test_input, test_output.joinpath('root_script.py'))]
    assert list(get_input_output_paths(str(test_input), str(test_output), None)) == test_result

    assert list(get_input_output_paths(str(test_input_directory), str(test_output), None)) == test_result

# Generated at 2022-06-14 01:41:32.123100
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    import pytest
    with pytest.raises(InvalidInputOutput):
        get_input_output_paths(
            input_=__file__,
            output=__file__,
            root=__file__,
        )
    with pytest.raises(InputDoesntExists):
        get_input_output_paths(
            input_='aaaabbbbcccc',
            output=__file__,
            root=__file__,
        )
    with pytest.raises(InputDoesntExists):
        get_input_output_paths(
            input_=__file__,
            output='aaaabbbbcccc',
            root=__file__,
        )

# Generated at 2022-06-14 01:41:47.996506
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    """Test the get_input_output_paths function."""
    import tempfile
    import shutil

    input_folder = Path(tempfile.mkdtemp())
    output_folder = Path(tempfile.mkdtemp())

    input_file = input_folder / 'file.py'
    output_file = output_folder / input_file.name

    with open(str(input_file), 'w') as file:
        pass

    for input_output in get_input_output_paths(str(input_folder), str(output_folder), None):
        assert input_output.input_file == input_file
        assert input_output.output_file == output_file


# Generated at 2022-06-14 01:41:55.436490
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    assert list(get_input_output_paths('a.py', 'test_a.py', None)) == [
        InputOutput(Path('a.py'), Path('test_a.py'))
    ]

    assert list(get_input_output_paths('sub/a.py', 'test_sub/a.py', None)) == [
        InputOutput(Path('sub/a.py'), Path('test_sub/a.py'))
    ]

    assert list(get_input_output_paths('sub', 'test_sub/sub.py', 'sub')) == [
        InputOutput(Path('sub/a.py'), Path('test_sub/sub.py'))
    ]


# Generated at 2022-06-14 01:42:06.050802
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Case 1: 1:1 input as output; input doesn't exist
    with pytest.raises(InputDoesntExists):
        paths = get_input_output_paths("foo.py", "bar.py", None)
        paths_list = list(paths)
        assert len(paths_list) == 0
    # Case 2: 1:1 input as output; input & output exist
    base_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(base_path, 'data', 'foo.py')
    output_path = os.path.join(base_path, 'data', 'bar.py')
    paths = get_input_output_paths(input_path, output_path, None)

# Generated at 2022-06-14 01:42:16.013928
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    # Case 1: when input is a file and output is a directory
    input_ = 'test/fixtures/pysource/sample.py'
    output = 'test/build'
    root = 'test/fixtures/pysource'
    result = list(get_input_output_paths(input_, output, root))
    assert len(result) == 1
    assert result[0].input_path == Path(input_)
    assert result[0].output_path == Path(output).joinpath('sample.py')

    # Case 2: when input is a directory and output is a directory
    input_ = 'test/fixtures/pysource'
    output = 'test/build'
    root = None
    result = list(get_input_output_paths(input_, output, root))

# Generated at 2022-06-14 01:42:24.027185
# Unit test for function get_input_output_paths
def test_get_input_output_paths():
    input_output = list(get_input_output_paths('a/b/c.py', 'd/e/f.py', 'a/b/'))
    assert input_output == [InputOutput(Path('a/b/c.py'), Path('d/e/f/c.py'))]

    input_output = list(get_input_output_paths('a/b/c.py', 'd/e/f', 'a/b/'))
    assert input_output == [InputOutput(Path('a/b/c.py'), Path('d/e/f/c.py'))]

    input_output = list(get_input_output_paths('a/b', 'd/e/f.py', 'a/b/'))