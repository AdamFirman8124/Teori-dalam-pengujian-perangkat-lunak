

# Generated at 2022-06-13 20:54:20.282211
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    from flutils.pathutils import directory_present

    _path = Path('~/tmp/flutils.tests.osutils.txt').expanduser()
    try:
        directory_present('~/tmp')
        _path.touch()

        tmp_uid = os.getuid()
        tmp_gid = os.getgid()
        chown(_path, '-1', '-1')
        assert tmp_uid == os.getuid()
        assert tmp_gid == os.getgid()
    finally:
        if _path.exists():
            _path.unlink()
        if _path.parent.exists():
            _path.parent.rmdir()



# Generated at 2022-06-13 20:54:32.085872
# Unit test for function chmod
def test_chmod():
    import os
    import tempfile

    from flutils.pathutils import chmod

    # os.chmod doesn't work in Windows.  This needs a fix.
    if os.name == 'nt':
        return

    _tmp_dir = tempfile.TemporaryDirectory()

    # Test for a non-existent file.
    try:
        chmod(f'{_tmp_dir.name}/file.txt', 0o660)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError('Should have raised a FileNotFoundError')

    # Test with a file.
    file_path = os.path.join(_tmp_dir.name, 'file.txt')
    with open(file_path, 'w'):
        pass
    chmod(file_path, 0o660)

# Generated at 2022-06-13 20:54:36.366390
# Unit test for function chmod
def test_chmod():
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)



# Generated at 2022-06-13 20:54:43.306498
# Unit test for function exists_as
def test_exists_as():
    # Basic tests.
    assert exists_as('/bin') == 'directory'
    assert exists_as('/bin/bash') == 'file'
    assert exists_as('/dev/sda') == 'block device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/var/lib/systemd/notify') == 'socket'
    assert exists_as('/dev/pts/ptmx') == 'file'
    # Test for a non-existent file.
    assert exists_as('/foo/bar') == ''
    # Test for a broken symlink.
    assert exists_as('/bin/ba') == ''
    # Test for symlink dangling symlink.
    assert exists_as('/dev/stdout') == ''
    # Test for symlink to

# Generated at 2022-06-13 20:54:54.528862
# Unit test for function directory_present
def test_directory_present():
    path = directory_present('~/tmp/test_dir_present')
    assert path == Path('/Users/len/tmp/test_dir_present')
    assert path.exists() is True
    assert path.is_dir() is True
    assert path.is_file() is False

    try:
        directory_present('~/tmp/test_dir_present/test_path1/test_path2')
        print("TEST FAIL 1")
        assert 0
    except FileExistsError:
        pass

    try:
        directory_present('~/tmp/test_dir_present/test_path1/*')
        print("TEST FAIL 2")
        assert 0
    except ValueError:
        pass


# Generated at 2022-06-13 20:55:02.323665
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    from flutils.osutils import is_file
    from pathlib import Path
    _ = chown('tests/test_chown/test_chown.txt')
    assert is_file('tests/test_chown/test_chown.txt') is False
    Path('tests/test_chown/test_chown.txt').touch()
    chown('tests/test_chown/test_chown.txt')
    #
    assert is_file('tests/test_chown/test_chown.txt') is True
    #



# Generated at 2022-06-13 20:55:14.114662
# Unit test for function chmod
def test_chmod():
    from glob import glob
    from os import chmod, mkdir, remove, rmdir
    from os.path import exists, join
    from tempfile import mkdtemp
    from time import sleep

    tmpdir = None

# Generated at 2022-06-13 20:55:25.498070
# Unit test for function exists_as
def test_exists_as():
    """Ensure flutils.pathutils.exists_as() is working as expected."""
    from flutils.pathutils import exists_as, tmp_dir
    from flutils.pathutils import directory_present

    tmp = tmp_dir()
    dir_created = directory_present(tmp.as_posix())
    assert dir_created == tmp

    dir_exists_as = exists_as(dir_created)
    assert dir_exists_as == 'directory'

    file_created = tmp.joinpath('flutils.tests.pathutils.txt')
    file_created.touch(mode=0o666)
    assert file_created.is_file() is True

    file_exists_as = exists_as(file_created)
    assert file_exists_as == 'file'

    tmp.rmdir()


# Generated at 2022-06-13 20:55:26.100851
# Unit test for function chmod
def test_chmod():
    assert True



# Generated at 2022-06-13 20:55:35.166799
# Unit test for function chmod
def test_chmod():
    # set a mode of 0o764 and ensure that it is set.
    Path(os.path.join(os.getcwd(), 'mkdir_test')).mkdir(parents=True, exist_ok=True)
    target_path = Path(os.path.join(os.getcwd(), 'mkdir_test', 'chmod_test'))
    target_path.mkdir(parents=True, exist_ok=True)
    Path(os.path.join(os.getcwd(), 'mkdir_test', 'chmod_test', 'chmod2_test')).mkdir(parents=True, exist_ok=True)
    target_path.chmod(0o764)

# Generated at 2022-06-13 20:56:01.125627
# Unit test for function find_paths
def test_find_paths():
    from pathlib import Path
    import tempfile
    from shutil import rmtree

    path = Path(tempfile.mkdtemp())
    sub_dir = path.joinpath('sub_dir1')
    sub_dir.mkdir()
    expected = list(find_paths(path))
    rmtree(path.as_posix())
    assert expected == [path]

    path = Path(tempfile.mkdtemp())
    sub_dir = path.joinpath('sub_dir1')
    sub_dir.mkdir()
    expected = list(find_paths(path.joinpath('*')))
    rmtree(path.as_posix())
    assert expected == [path.joinpath('sub_dir1')]

    path = Path(tempfile.mkdtemp())
    sub_dir = path

# Generated at 2022-06-13 20:56:13.190870
# Unit test for function chmod
def test_chmod():
    # Create a test file
    path_file = Path(Path().cwd(), 'flutils.tests.osutils.txt')
    path_file.touch()

    # Create a test directory
    path_dir = Path(Path().cwd(), 'flutils.tests.osutils')
    path_dir.mkdir()

    # Create test directories and files
    path_sub1 = Path(Path().cwd(), 'flutils.tests.osutils.sub1')
    path_sub1.mkdir()
    path_sub2 = Path(Path().cwd(), 'flutils.tests.osutils.sub2')
    path_sub2.mkdir()
    path_sub1_file1 = Path(path_sub1, 'file1.txt')
    path_sub1_file1.touch()
    path_sub1_file

# Generated at 2022-06-13 20:56:24.305553
# Unit test for function exists_as
def test_exists_as():
    # create some fake files for testing
    test_base_dir = os.path.dirname(os.path.dirname(__file__))
    fake_dir_path = os.path.join(test_base_dir, 'fake_dir')
    fake_file_path = os.path.join(test_base_dir, 'fake_file')
    fake_block_path = os.path.join(test_base_dir, 'fake_block')
    fake_char_path = os.path.join(test_base_dir, 'fake_char')
    fake_fifo_path = os.path.join(test_base_dir, 'fake_fifo')
    fake_socket_path = os.path.join(test_base_dir, 'fake_socket')
    fake_link_path = os.path.join

# Generated at 2022-06-13 20:56:35.348834
# Unit test for function chown
def test_chown():
    path_ = os.path.join(os.path.expanduser('~'), 'tmp')
    new_path = os.path.join(path_, 'flutils.tests.osutils.txt')
    with open(new_path, 'w'):
        pass

    expected_result = pwd.getpwuid(os.getuid()).pw_uid
    assert expected_result == os.stat(new_path).st_uid

    chown(new_path, 'root')
    assert 0 == os.stat(new_path).st_uid

    chown(new_path, '-1')
    assert 0 == os.stat(new_path).st_uid

    chown(new_path, user='-1')
    assert 0 == os.stat(new_path).st_uid

    os.remove

# Generated at 2022-06-13 20:56:36.161635
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:56:41.451236
# Unit test for function exists_as
def test_exists_as():
    """Unit test for function exists_as"""
    assert exists_as(__file__) == 'file'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/random') == 'char device'



# Generated at 2022-06-13 20:56:51.692438
# Unit test for function chown
def test_chown():
    import os
    my_cwd = os.getcwd()
    my_path = Path(my_cwd, "testing_chown.txt")
    if my_path.exists():
        my_path.unlink()
    my_path.touch()
    my_path.chmod(0o644)
    assert my_path.stat().st_mode & 0o777 == 0o644

    try:
        chown(my_path, user='-1', group='-1')
        assert my_path.stat().st_mode & 0o777 == 0o644
    except Exception as e:
        print(e)
    finally:
        my_path.unlink()
        assert not my_path.exists()
    print("Finished test_chown")


# Generated at 2022-06-13 20:57:06.571054
# Unit test for function find_paths
def test_find_paths():
    """Unittest for function: find_paths()."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = Path(tmpdir)
        tmp_dirs = [
            'one', 'two', 'two/three', 'two/three/four', 'two/three/five',
            'two/three/five/six', 'seven'
        ]
        for tdir in tmp_dirs:
            dir_path = test_dir / tdir
            dir_path.mkdir(mode=0o700, parents=True)

# Generated at 2022-06-13 20:57:11.812606
# Unit test for function chown
def test_chown():
    if os.getuid() == 0:
        chown('/tmp/flutils.tests.pathutils.chown.txt', user='bar')
        chown('/tmp/flutils.tests.pathutils.chown.txt', group='foo')
        chown('/tmp/flutils.tests.pathutils.chown.txt', user='bar', group='foo')



# Generated at 2022-06-13 20:57:25.813836
# Unit test for function chown
def test_chown():
    # Create a temporary directory with a file to chmod
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        tmp_file = tmp_dir / 'foo'
        tmp_file.write_text('foo')

        assert tmp_file.is_file() is True

        chown(path=tmp_file)
        tmp_file_stat = tmp_file.stat()
        assert tmp_file_stat.st_uid == os.geteuid()
        assert tmp_file_stat.st_gid == os.getegid()

        chown(path=tmp_dir, user='root', group='root')
        tmp_dir_stat = tmp_dir.stat()
        assert tmp_dir_stat.st_uid == 0
        assert tmp_dir_stat.st_gid == 0

# Generated at 2022-06-13 20:57:55.898221
# Unit test for function chmod
def test_chmod():
    from .osutils import makedirs

    fname = 'tmp/file.txt'
    makedirs(fname)
    assert os.access(fname, os.F_OK) is True
    assert os.access(fname, os.R_OK) is True
    assert os.access(fname, os.W_OK) is True
    assert os.access(fname, os.X_OK) is True

    chmod(fname, mode_file=0o600)
    assert os.access(fname, os.R_OK) is False
    assert os.access(fname, os.W_OK) is True
    assert os.access(fname, os.X_OK) is False

    chmod(fname, mode_file=0o644)

# Generated at 2022-06-13 20:58:00.663504
# Unit test for function find_paths
def test_find_paths():
    ANCHOR = Path('~/tmp/test_find_paths').expanduser()
    FILE_ONE = ANCHOR.joinpath('file_one.txt')
    DIR_ONE = ANCHOR.joinpath('dir_one')
    DIR_TWO = ANCHOR.joinpath('dir_two')
    FILE_TWO = DIR_TWO.joinpath('file_two.txt')
    DIR_TWO.mkdir(parents=True)
    FILE_ONE.touch()
    FILE_TWO.touch()
    PATTERNS = ['file*', '*/file*']
    for pattern in PATTERNS:
        # Gather the results from the function being tested to be compared.
        function_results: List[Path] = list(find_paths(pattern))
        # Gather the expected

# Generated at 2022-06-13 20:58:12.763954
# Unit test for function find_paths
def test_find_paths():

    def _mkdir(path: _PATH):
        path = normalize_path(path)
        os.makedirs(path.as_posix(), mode=0o777, exist_ok=True)

    def _mkfile(path: _PATH):
        path = normalize_path(path)
        os.makedirs(path.parent.as_posix(), mode=0o777, exist_ok=True)
        open(path.as_posix(), 'w').close()

    # Create file_one and dir_one.
    test_dir = os.path.join(tempfile.gettempdir(), 'tmp')
    _mkdir(test_dir)
    file_one = os.path.join(test_dir, 'file_one')
    _mkfile(file_one)
    dir_one = os

# Generated at 2022-06-13 20:58:25.983597
# Unit test for function find_paths
def test_find_paths():
    expected = [
        PosixPath('/tmp/dir_one/dir_three'),
        PosixPath('/tmp/dir_one/dir_two'),
    ]
    actual = list(find_paths('/tmp/dir_one/*'))
    assert len(expected) == len(actual)
    for pth in expected:
        assert pth in actual
    expected = [
        PosixPath('/tmp/dir_one/dir_three/file_three'),
        PosixPath('/tmp/dir_one/dir_two/file_two'),
    ]
    actual = list(find_paths('/tmp/dir_one/*/*'))
    assert len(expected) == len(actual)
    for pth in expected:
        assert pth in actual


# Generated at 2022-06-13 20:58:39.106122
# Unit test for function chmod
def test_chmod():
    import os
    import tempfile
    import shutil

    tmpdir = Path(tempfile.gettempdir())
    tmpdir = tmpdir / 'flutils_test_osutils'

    # Cleanup and make sure a clean slate.
    if tmpdir.exists() is True:
        shutil.rmtree(tmpdir)

    tmpdir.mkdir(mode=0o700, parents=True)
    tmpfile = tmpdir / 'flutils_test_osutils.txt'
    tmpfile.touch()

    chmod(tmpfile, include_parent=True)
    assert os.stat(tmpfile).st_mode == 33152
    assert os.stat(tmpdir).st_mode == 45824

    dirdata = tmpdir / 'data'
    dirdata.mkdir()
    datafile = dirdata

# Generated at 2022-06-13 20:58:41.119550
# Unit test for function chown
def test_chown():
    '''
    >>> assert osutils.chown('test.txt','test','test') is None
    '''



# Generated at 2022-06-13 20:58:49.601097
# Unit test for function find_paths
def test_find_paths():
    from flutils.pathutils import find_paths
    from _pytest.monkeypatch import MonkeyPatch

    mock_path_list = ['~/tmp/file_one', '~/tmp/dir_one']

    class MockPath(Path):
        @classmethod
        def glob(cls, pattern: _PATH) -> Generator[Path, None, None]:
            yield from mock_path_list

    monkeypatch = MonkeyPatch()

    monkeypatch.setattr('pathlib.Path', MockPath)
    # Monkey patch the Path.glob() method to return a fixed list.
    assert list(find_paths('~/tmp/*')) == mock_path_list



# Generated at 2022-06-13 20:59:04.192668
# Unit test for function chmod
def test_chmod():
    """Test the flutils.osutils.chmod() function.

    """

    with tempdir() as tmpdir:
        tmpdir.join('file.txt').write('file.txt')
        tmpdir.mkdir('dir')
        tmpdir.join('dir', 'file.txt').write('dir/file.txt')

        chmod(str(tmpdir.join('file.txt')), 0o666)
        chmod(str(tmpdir.join('dir')), 0o777)
        chmod(str(tmpdir.join('dir', 'file.txt')), 0o666)

        chmod(str(tmpdir.join('file.txt')), mode_file=0o666)
        chmod(str(tmpdir.join('dir')), mode_dir=0o777)

# Generated at 2022-06-13 20:59:14.500668
# Unit test for function find_paths
def test_find_paths():
    try:
        with TemporaryDirectory() as tmp_path:
            tmp_path = Path(tmp_path)
            tmp_file = tmp_path / 'file_one'
            tmp_file.touch()
            tmp_dir = tmp_path / 'dir_one'
            tmp_dir.mkdir()
            result = sorted(list(find_paths(tmp_path / '*')))
            assert len(result) == 2
            assert result[0] != result[1]
            assert str(result[0]) == str(tmp_file)
            assert str(result[1]) == str(tmp_dir)
    except (OSError, IOError):
        pytest.xfail('Not able to create temporary directory.')

# Generated at 2022-06-13 20:59:19.706236
# Unit test for function chown
def test_chown():
    from os import getuid, getgid
    from tempfile import TemporaryDirectory
    tmp_dir = TemporaryDirectory()
    path = Path(tmp_dir.name, 'file.txt')
    path.touch()
    chown(path, user=getuid(), group=getgid())



# Generated at 2022-06-13 20:59:55.791811
# Unit test for function path_absent
def test_path_absent():
    # Create a base directory.
    path = normalize_path(tempfile.mkdtemp())
    # Create a sub directory.
    sub_path = path / 'sub_path'
    sub_path.mkdir()
    # Create a file.
    file_path = sub_path / 'file.txt'
    file_path.touch()
    # Create a symbolic link pointing to a file.
    symlink_file_path = path / 'file'
    symlink_file_path.symlink_to(file_path)
    # Create a symbolic link pointing to the sub path.
    symlink_sub_path = path / 'sub_path_2'
    symlink_sub_path.symlink_to(sub_path)
    # Create a symbolic link pointing to a file.
    symlink

# Generated at 2022-06-13 21:00:06.254568
# Unit test for function chmod
def test_chmod():
    from os.path import expanduser
    from shutil import rmtree
    from flutils.pathutils import chmod
    from tempfile import mkdtemp

    tmp_dir = mkdtemp()

    file_path = (Path(tmp_dir) / 'flutils.tests.osutils.txt').resolve()
    file_path.touch()
    with assert_raises(NotImplementedError):
        chmod('missing_file')

    chmod(file_path, mode_file=0o644)
    assert_equal(file_path.stat().st_mode, 33152)

    glob_path = Path(tmp_dir) / '*'
    chmod(glob_path, mode_dir=0o770, include_parent=True)

# Generated at 2022-06-13 21:00:08.452069
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    chmod('test_osutils.txt')

# Generated at 2022-06-13 21:00:25.107789
# Unit test for function chmod
def test_chmod():
    from shutil import rmtree
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as temp_dir_path:
        temp_dir = Path(temp_dir_path)
        os_path = temp_dir / 'os.txt'
        os_path.write_text('')

        pathlib_path = temp_dir / 'pathlib.txt'
        pathlib_path.write_text('')

        glob_path = temp_dir / 'glob*'
        glob_path.write_text('')

        chmod(os_path, include_parent=True)
        assert os_path.stat().st_mode == 0o100600

        chmod(glob_path)
        glob_path.unlink()
        assert glob_path.exists() is False
        assert pathlib_path.stat

# Generated at 2022-06-13 21:00:26.636872
# Unit test for function chmod
def test_chmod():
    # TODO: Add unit test coverage
    pass



# Generated at 2022-06-13 21:00:38.530193
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    import tempfile
    import pathlib
    import os

    with tempfile.TemporaryDirectory() as tmp_dir:
        for file_count in range(15):
            file_path = str(pathlib.Path(tmp_dir).joinpath(f"tmp_{file_count}.txt"))
            with open(file_path, 'a'):
                os.utime(file_path, None)
        chmod(str(pathlib.Path(tmp_dir).joinpath("tmp*")), mode_file=0o644)
        mode = []
        for item in os.scandir(tmp_dir):
            mode.append(item.stat().st_mode)

# Generated at 2022-06-13 21:00:49.917335
# Unit test for function chmod
def test_chmod():
    # Set up some state for the test
    os.makedirs('~/tmp/flutils.test/test')
    fpath = '~/tmp/flutils.test/test/flutils.test.txt'
    with open(fpath, 'w') as f:
        f.write('flutils.test')


    # Perform the test
    chmod('~/tmp/flutils.test/**', mode_file=0o640, mode_dir=0o750)


    # Perform the asserts
    assert Path('~/tmp/flutils.test').is_dir() is True
    assert bin(Path('~/tmp/flutils.test').stat().st_mode)[-3:] == '750'
    assert Path('~/tmp/flutils.test/test').is_dir() is True

# Generated at 2022-06-13 21:00:54.524346
# Unit test for function chown
def test_chown():
    import tempfile
    path = Path(tempfile.mkdtemp()).joinpath('flutils.tests.pathutils.txt')
    path.write_text('abc123')
    chown(path)



# Generated at 2022-06-13 21:01:05.459030
# Unit test for function path_absent
def test_path_absent():
    tmp_dir = Path(tempfile.mkdtemp(prefix='test_path_absent_'))

# Generated at 2022-06-13 21:01:07.267137
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:01:53.032196
# Unit test for function chown
def test_chown():
    path = '~/tmp/flutils.tests.osutils.txt'
    user = getpass.getuser()
    group = getpass.getuser()
    chown(path, user, group)



# Generated at 2022-06-13 21:02:06.214161
# Unit test for function chmod
def test_chmod():
    dir_path = Path().cwd() / 'testdir'
    dir_path.mkdir(exist_ok=True)

    txt_path = dir_path / 'test.txt'
    txt_path.touch(exist_ok=True)
    txt_path.chmod(0o700)

    assert txt_path.exists() is True
    assert txt_path.is_file() is True
    assert txt_path.stat().st_mode & 0o777 == 0o700

    chmod(str(txt_path), 0o660)

    assert txt_path.exists() is True
    assert txt_path.is_file() is True
    assert txt_path.stat().st_mode & 0o777 == 0o660

    txt_path.unlink()
    dir

# Generated at 2022-06-13 21:02:15.072336
# Unit test for function chmod
def test_chmod():
    import os
    import stat
    import tempfile
    from os import chmod as os_chmod
    from os.path import join

    # Create a temp directory.
    temp_dir = tempfile.TemporaryDirectory()

    # Create a directory in the temp directory.
    sub_dir = join(temp_dir.name, 'sub_dir')
    os.mkdir(sub_dir)

    # Create a file in the sub directory.
    sub_file = join(sub_dir, 'my_file.txt')
    with open(sub_file, 'w'):
        pass

    # Create a symlink to the subfile.
    symlink_target = join(temp_dir.name, 'symlink')
    os.symlink(sub_file, symlink_target)

    # Change the mode of

# Generated at 2022-06-13 21:02:26.434981
# Unit test for function chown
def test_chown():
    if os.getenv('UNIT_TEST_FLUTILS_OSUTILS') is not None:
        from os.path import join
        from shutil import rmtree
        import tempfile
        from unittest import TestCase

        from pathlib import Path

        from flutils.tests.utils import (
            mkdir,
            mkfile,
        )

        from flutils.osutils import chown

        from ..pathutils import normalize_path

        class Test_chown(TestCase):
            TEST_DIRECTORY = None  # type: Optional[str]
            TEST_PATH = None  # type: Optional[Path]


# Generated at 2022-06-13 21:02:27.281286
# Unit test for function chown
def test_chown():
    pass

# Generated at 2022-06-13 21:02:29.819679
# Unit test for function chown
def test_chown():
    assert chown.__doc__



# Generated at 2022-06-13 21:02:33.971725
# Unit test for function chmod
def test_chmod():
    path = Path('/tmp/flutils.tests.osutils.test_chmod.txt')
    path.write_text('foo')
    chmod(path, 0o660)
    assert path.stat().st_mode == 33152
    path.unlink()



# Generated at 2022-06-13 21:02:37.740092
# Unit test for function chown
def test_chown():
    try:
        chown('test_chown')
    except Exception as e:
        raise e


# Generated at 2022-06-13 21:02:47.413669
# Unit test for function chown
def test_chown():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        # Dummy file
        test_path = Path(tmpdir) / 'flutils_test_file.txt'
        test_path.touch()

        # Get current user info
        current_uid = os.getuid()
        current_gid = os.getgid()

        # Verify current file owner
        assert test_path.stat().st_uid == current_uid
        assert test_path.stat().st_gid == current_gid

        # Change owner
        chown(test_path, user='root', group='root')

        # Verify new file owner
        expected_uid = pwd.getpwnam('root').pw_uid
        expected_gid = grp.getgrnam('root').gr_gid
        assert test_

# Generated at 2022-06-13 21:02:55.459548
# Unit test for function path_absent
def test_path_absent():
    from tempfile import TemporaryDirectory  # type: ignore[import]
    from getpass import getuser  # type: ignore[import]
    from shutil import copytree, rmtree  # type: ignore[import]
    from pathlib import Path  # type: ignore[import]
    from os.path import join  # type: ignore[import]
    username = getuser()
    with TemporaryDirectory() as tempdir:
        copytree(
            join('tests', 'data', 'test_path_absent'),
            join(tempdir, 'test_path_absent')
        )
        path = Path(tempdir, 'test_path_absent')
        path_absent(path)
        assert path.exists() is False
        assert path.is_dir() is False
        assert path.is_symlink() is False

# Generated at 2022-06-13 21:03:22.695757
# Unit test for function path_absent
def test_path_absent():
    pass



# Generated at 2022-06-13 21:03:33.399343
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent
    import shutil
    if sys.platform == 'win32':
        base_dir = 'C:\\windows\\temp'
    else:
        base_dir = Path(os.getcwd()) / 'tmp'
    base_dir = Path(base_dir)
    (base_dir / 'test_path').mkdir(parents=True, exist_ok=True)
    path = base_dir / 'test_path'
    assert os.path.exists(path.as_posix()) is True
    path_absent(path)
    assert os.path.exists(path.as_posix()) is False
    shutil.rmtree(base_dir)



# Generated at 2022-06-13 21:03:38.079440
# Unit test for function chown
def test_chown():
    chown('~/tmp/flutils.tests.osutils.txt')
    chown('~/tmp/**')
    chown('~/tmp/*', user='foo', group='bar')
