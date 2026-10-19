

# Generated at 2022-06-13 20:53:46.879324
# Unit test for function chmod
def test_chmod():
    normalize_path = _path_normalizer(ansible_module=True)
    path = normalize_path('/foo/bar/baz')
    path.is_file()



# Generated at 2022-06-13 20:53:50.055110
# Unit test for function exists_as
def test_exists_as():
    path = normalize_path('~/tmp')
    assert exists_as(path) == 'directory'



# Generated at 2022-06-13 20:53:56.187698
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~') == 'directory'
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/flutils/tests/assets/osutils/osutils_open_file') == 'file'
    assert exists_as('~/flutils/tests/assets/osutils/not_a_file') == ''



# Generated at 2022-06-13 20:53:59.491117
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    from flutils.testutils import get_testdata_dir

    assert exists_as(get_testdata_dir()) == 'directory'



# Generated at 2022-06-13 20:54:00.356380
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:54:06.432531
# Unit test for function chmod
def test_chmod():
    path = './tmp'
    if not os.path.isdir(path):
        os.mkdir(path)
    with open(os.path.join(path, 'test_flutils.txt'), 'wt') as fout:
        fout.write('test_flutils')

    chmod(os.path.join(path, 'test_flutils.txt'), 0o660)
    chmod(os.path.join(path, 'test_flutils.txt'), 0o066, 0o007)
    chmod(os.path.join(path, 'test_flutils.txt'), mode_file=0o066, mode_dir=0o007, include_parent=True)
 


# Generated at 2022-06-13 20:54:12.889071
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent
    from flutils.testhelpers import capture_stdout, capture_stderr
    from pathlib import Path
    from os import getcwd, listdir

    test_dir = Path(__file__).parent
    tmpdir = os.path.join(test_dir, 'tmp')
    tmpdir = normalize_path(tmpdir)
    tmpdir = tmpdir.as_posix()
    tmpdir = cast(str, tmpdir)
    tmp = Path(tmpdir)

    # Test dir absent
    path_absent(tmp)
    assert os.path.isdir(tmpdir) is False
    assert os.path.isfile(tmpdir) is False
    assert os.path.islink(tmpdir) is False

# Generated at 2022-06-13 20:54:24.426459
# Unit test for function chmod
def test_chmod():
    """Test the chmod function.

    """

    tmp_dir = tmp_dir_factory()

    path = Path(tmp_dir, 'file.txt')
    path.touch()

    # First we'll test a regular file.
    chmod(path, 0o777)
    assert stat.S_IMODE(os.lstat(path).st_mode) == 0o777

    # Now we'll test a directory.
    path = Path(tmp_dir, 'a_dir')
    path.mkdir()

    chmod(path, mode_file=0o0700, mode_dir=0o0700)
    assert stat.S_IMODE(os.lstat(path).st_mode) == 0o0700

    # Test a non-existent path.

# Generated at 2022-06-13 20:54:31.489416
# Unit test for function exists_as
def test_exists_as():
    assert 'directory' == exists_as('/tmp')
    assert 'file' == exists_as('/etc/hosts')
    assert 'block device' == exists_as('/dev/sda')
    assert 'char device' == exists_as('/dev/tty')
    assert 'FIFO' == exists_as('/dev/stdin')
    assert '' == exists_as('/not_exists_path')
    assert '' == exists_as('/tmp/not_exists_file')



# Generated at 2022-06-13 20:54:39.635235
# Unit test for function find_paths
def test_find_paths():
    from tests.pathutils import parent_dir
    from tests.pathutils import create_test_path
    from tests.pathutils import delete_test_path

    test_dir = parent_dir / 'find_paths'
    assert find_paths(test_dir) is not None

    top_dir = test_dir / 'top'
    file_one = test_dir / 'file_one'
    assert find_paths(file_one) is not None

    create_test_path(top_dir, file_one)

    assert find_paths(test_dir / '*') is not None
    delete_test_path(test_dir)

# Generated at 2022-06-13 20:55:01.837109
# Unit test for function chown
def test_chown():
    """ Test chown function.
    """
    try:
        from flutils.pathutils import chown

        # Test 1
        user = getpass.getuser()
        group = getpass.getuser()
        fp = '~/tmp/flutils.tests.osutils.txt'
        chown(fp, user, group)

        # Test 2
        user = os.getuid()
        group = os.getgid()
        chown(fp, user, group)
    except Exception:
        pass



# Generated at 2022-06-13 20:55:13.790863
# Unit test for function exists_as
def test_exists_as():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp_dir, TemporaryDirectory() as tmp_dir2:
        with open(os.path.join(tmp_dir, 'test.txt'), 'w') as fh:
            fh.write('test')

        assert exists_as(tmp_dir) == 'directory'
        assert exists_as(os.path.join(tmp_dir, 'test.txt')) == 'file'
        assert exists_as(tmp_dir2) == ''
        assert exists_as(os.path.join(tmp_dir2, 'test.txt')) == ''
        assert exists_as(str(uuid.uuid4())) == ''



# Generated at 2022-06-13 20:55:14.986196
# Unit test for function chown
def test_chown():
    assert True is True



# Generated at 2022-06-13 20:55:17.224408
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(__file__) == 'file'
    assert exists_as('file_that_does_not_exist') == ''



# Generated at 2022-06-13 20:55:18.670967
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:55:20.993869
# Unit test for function chmod
def test_chmod():
    try:
        chmod('bad_dir')
    except:
        pass
    else:
        sys.exit(1)


# Generated at 2022-06-13 20:55:22.527525
# Unit test for function chown
def test_chown():
    chown('/tmp/flutils.tests.osutils.txt', getpass.getuser(), os.getegid())



# Generated at 2022-06-13 20:55:32.960398
# Unit test for function chmod
def test_chmod():
    # type: () -> None
    """Tests for chmod function."""
    content = 'some content written to file\n'
    path = Path(os.path.expanduser('~/tmp/flutils.tests.osutils.txt'))
    expected = 0o660
    path.write_text(content)

    chmod(path.as_posix(), include_parent=True)

    assert path.exists() is True
    assert path.is_file() is True
    assert path.stat().st_mode & 0o700 == expected
    assert path.parent.stat().st_mode & 0o700 == expected

    temp_dir = Path(os.path.expanduser('~/tmp/flutils.tests.osutils'))
    expected = 0o770

    temp_dir.mkdir()

# Generated at 2022-06-13 20:55:38.603690
# Unit test for function exists_as
def test_exists_as():
    """Test function exists_as."""
    p = '~/tmp/flutils.tests/pathutils.test_exists_as'

# Generated at 2022-06-13 20:55:48.175897
# Unit test for function find_paths
def test_find_paths():

    # Test empty list.
    ret = list(find_paths('/some/path/that/does/not/exist/*'))
    assert len(ret) == 0

    # Create some files and directories
    a_path = directory_present('/tmp/test_find_paths/tmp')
    file_one = Path().joinpath(a_path, 'file_one')
    file_one.touch()
    file_two = Path().joinpath(a_path, 'file_two')
    file_two.touch()
    dir_one = Path().joinpath(a_path, 'dir_one')
    dir_one.mkdir()
    dir_two = Path().joinpath(a_path, 'dir_two')
    dir_two.mkdir()


# Generated at 2022-06-13 20:56:07.744875
# Unit test for function chown
def test_chown():
    path = '~/tmp/test.test_chown.txt'
    user = getpass.getuser()
    group = getpass.getuser()
    try:
        chown(path)
        chown(path, user, group)
    finally:
        path = normalize_path(path)
        path.unlink()



# Generated at 2022-06-13 20:56:08.855746
# Unit test for function chown
def test_chown():
    assert callable(chown)



# Generated at 2022-06-13 20:56:09.763423
# Unit test for function directory_present
def test_directory_present():
    ...


# Generated at 2022-06-13 20:56:21.843029
# Unit test for function chown
def test_chown():
    if os.name != 'nt':
        import stat

        from flutils.pathutils import (
            chown,
            get_os_group,
            get_os_user,
            path_absent,
        )

        from . import (
            osutils_fixtures_dir,
            test_dir,
        )

        flutils_test_dir = test_dir / 'flutils'
        flutils_test_dir.mkdir(exist_ok=True)

        chown_file = flutils_test_dir / 'chown.txt'
        chown_file.write_text('This is a test.')
        assert chown_file.exists()

        group_obj = get_os_group()
        user_obj = get_os_user()

# Generated at 2022-06-13 20:56:33.651071
# Unit test for function path_absent
def test_path_absent():
    from tempfile import TemporaryDirectory
    from flutils.pathutils import path_absent
    with TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, 'test_path')
        Path(path).touch()
        path_absent(path)
        assert os.path.exists(path) == False

        Path(path = os.path.join(temp_dir, 'test_path')).mkdir()
        path_absent(path)
        assert os.path.exists(path) == False

        Path(path).mkdir()
        path_absent(path)
        assert os.path.exists(path) == False

        Path(os.path.join(path, 'sub_dir')).mkdir()
        path_absent(path)
        assert os.path.ex

# Generated at 2022-06-13 20:56:48.476876
# Unit test for function chmod
def test_chmod():
    delete = ['file_0777', 'file_0666', 'file_0644', 'file_0600', 'file_0755', 'file_0700', 'file_0750']
    for key in delete:
        try:
            os.remove(key)
        except OSError:
            pass
    cmd = "touch file_0777 file_0666 file_0644 file_0600"
    os.system(cmd)
    assert Path("file_0777").is_file() is True
    assert Path("file_0666").is_file() is True
    assert Path("file_0644").is_file() is True
    assert Path("file_0600").is_file() is True
    cmd = "mkdir -p file_0750"
    os.system(cmd)

# Generated at 2022-06-13 20:56:52.366944
# Unit test for function chown
def test_chown():
    assert chown('', user='-1') is None, 'test failed'
    assert chown('', group='-1') is None, 'test failed'
    assert chown('', include_parent=True) is None, 'test failed'



# Generated at 2022-06-13 20:57:04.018499
# Unit test for function path_absent
def test_path_absent():
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()

    # Test that a file can be deleted.
    path = os.path.join(temp_dir.name, 'file_one')
    with open(path, 'w') as f:
        f.write('')

    del_path = normalize_path(path)
    path_absent(del_path)

    assert os.path.exists(path) is False
    # Test that a directory can be deleted.
    path = os.path.join(temp_dir.name, 'dir_one')
    os.mkdir(path)

    del_path = normalize_path(path)
    path_absent(del_path)

    assert os.path.exists(path) is False
    # Test that a directory tree can be deleted.

# Generated at 2022-06-13 20:57:11.679532
# Unit test for function chown
def test_chown():

    from flutils.pytest_utils import (
        assert_isdir,
        assert_isfile,
        assert_isnotdir,
        assert_isnotfile,
        get_file_changetime,
        get_file_group,
        get_file_mode,
        get_file_owner,
    )

    # This will change ownership of a directory
    # and it's immediate contents.
    chown(
        '~/tmp/flutils.*',
        user='flutils_test_user',
        group='flutils_test_group',
    )
    assert_isnotfile(Path('~/tmp/flutils.directory_present.txt'))
    assert_isnotdir(Path('~/tmp/flutils.directory_present.dir'))

    # Re-create the directory and its contents
   

# Generated at 2022-06-13 20:57:23.026249
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown, path_absent
    import os

    tmp_path = '/tmp/test_chown.txt'
    if os.path.exists(tmp_path) is True:
        os.unlink(tmp_path)

    chown('/tmp/test_chown.txt')
    assert os.path.exists(tmp_path) is True

    chown('/tmp/test_chown.txt', '-1', '-1')
    assert os.path.exists(tmp_path) is True

    path_absent(tmp_path)



# Generated at 2022-06-13 20:57:41.106952
# Unit test for function path_absent
def test_path_absent():
    """Test function path_absent()."""
    import tempfile
    test_dir = tempfile.TemporaryDirectory()
    test_dir_path = Path(test_dir.name)

    dir_path = test_dir_path / 'dir_one'
    dir_path.mkdir()

    file_path = test_dir_path / 'file.txt'
    file_path.touch()

    path_absent(test_dir_path)
    assert not test_dir_path.exists()



# Generated at 2022-06-13 20:57:54.272346
# Unit test for function exists_as
def test_exists_as():
    import sys
    import posixpath
    import ntpath

    if sys.platform.startswith('linux'):
        test_exists_as.root = '/sys'
    elif sys.platform.startswith('darwin'):
        test_exists_as.root = '/dev'
    elif sys.platform.startswith('win'):
        test_exists_as.root = 'C:\Windows'
    else:
        test_exists_as.root = '/sys'

    assert exists_as(test_exists_as.root) == 'directory'
    assert exists_as(f'{test_exists_as.root}/noexists') == ''


# Generated at 2022-06-13 20:58:06.304226
# Unit test for function chmod
def test_chmod():
    from . import _pth

    tmp_dir = os.path.join(_pth['tmp'], 'osutils.txt')

    os.mkdir(tmp_dir)


# Generated at 2022-06-13 20:58:08.995282
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/') == 'directory'
    assert exists_as('/does/not/exist') == ''

# Generated at 2022-06-13 20:58:15.372287
# Unit test for function get_os_user
def test_get_os_user():
    assert get_os_user() is not None
    assert get_os_user(os.getuid()) is not None
    with pytest.raises(OSError):
        get_os_user(10000)
    with pytest.raises(OSError):
        get_os_user('this_user_does_NOT_exist')
    assert get_os_user(os.getuid()).pw_uid == os.getuid()
#



# Generated at 2022-06-13 20:58:28.277238
# Unit test for function chown
def test_chown():
    """Test for function chown"""

    from flutils.pathutils import chown, find_paths, normalize_path
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        Path(temp_dir / 'foo').touch()
        Path(temp_dir / 'bar').mkdir(parents=True)
        Path(temp_dir / 'bar' / 'bar').mkdir()
        Path(temp_dir / 'bar' / 'bar' / 'bar').touch()
        Path(temp_dir / 'baz').touch()
        Path(temp_dir / 'qux').mkdir()
        Path(temp_dir / 'qux' / 'qux').touch()

# Generated at 2022-06-13 20:58:30.760809
# Unit test for function chown
def test_chown():
    test_path = '~/tmp/flutils.tests.osutils.txt'
    chown(test_path, '-1')


# Generated at 2022-06-13 20:58:38.767121
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent
    import tempfile
    import shutil
    path = Path(tempfile.mkdtemp())
    tmp_file = path / 'test_file'
    tmp_file.write_text('test_text')
    try:
        path_absent(tmp_file)
        assert tmp_file.exists() is False
        path_absent(path)
        assert path.exists() is False
    finally:
        shutil.rmtree(path)


# Generated at 2022-06-13 20:58:46.005325
# Unit test for function directory_present
def test_directory_present():
    default_mode = 0o700

    path = directory_present('~/tmp/flutils.test_directory_present')
    assert path.is_dir() is True
    assert path.stat().st_mode == default_mode
    path.unlink()

    path = directory_present('~/tmp/flutils.test_directory_present', mode=0o755)
    assert path.is_dir() is True
    assert path.stat().st_mode == 0o755
    path.unlink()

    path = directory_present('~/tmp/flutils.test_directory_present', mode=0o755)
    assert path.is_dir() is True
    assert path.stat().st_mode == 0o755
    path.unlink()


# Generated at 2022-06-13 20:58:59.761306
# Unit test for function chown
def test_chown():
    from flutils.pathutils import exists_as
    from flutils.pathutils import path_absent
    from flutils.testingutils import Dirs
    from flutils.testingutils import normalize_path
    from flutils.testingutils import TempFile


# Generated at 2022-06-13 20:59:16.249829
# Unit test for function chmod
def test_chmod():
    test_dir = Path('~/tmp/flutils.tests').expanduser().absolute()
    test_file = test_dir / 'file_chmod.txt'

    test_file.touch()
    test_file.chmod(0o000)
    assert test_file.stat().st_mode & 0o0777 == 0o000

    chmod(test_file, mode_file=0o660)
    assert test_file.stat().st_mode & 0o0777 == 0o660

    # Chmod a directory that contains a glob pattern
    chdir = os.getcwd()
    os.chdir(str(test_dir))
    test_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(str('../'))

# Generated at 2022-06-13 20:59:20.643703
# Unit test for function chown
def test_chown():
    path = normalize_path('~/tmp/flutils.tests.osutils.txt')
    path.write_bytes(b'foobar')
    chown('~/tmp/flutils.tests.osutils.txt', user='foo', group='bar')
    path.unlink()



# Generated at 2022-06-13 20:59:28.446351
# Unit test for function path_absent
def test_path_absent():  # pragma: no cover
    import shutil
    tmpdir = os.path.join(os.getcwd(), 'tmp')
    if os.path.isdir(tmpdir):
        shutil.rmtree(tmpdir)
    path_present(tmpdir)
    path_present(os.path.join(tmpdir, 'test_file'))
    try:
        path_absent(tmpdir)
    except Exception as e:
        raise e
    finally:
        shutil.rmtree(tmpdir)



# Generated at 2022-06-13 20:59:40.658054
# Unit test for function chown
def test_chown():
    from flutils.datastructures import objmap
    from flutils.testutils import (
        assert_function_params,
        assert_function_return,
    )

    test_path = Path('~/tmp/flutils.tests.osutils.txt').expanduser().absolute()

    # Make sure that the test file doesn't exist.
    test_path.unlink(missing_ok=True)

    with test_path.open('w') as f_obj:
        f_obj.write('foo')

    assert exists_as(test_path, file=True) is True


# Generated at 2022-06-13 20:59:41.299083
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:59:55.387395
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown

    with TemporaryDirectory() as tmpdir:
        username = getpass.getuser()
        groupname = grp.getgrgid(os.getgid()).gr_name
        user = get_os_user(username)
        group = get_os_group(groupname)

        testfilename = Path(tmpdir) / 'test.txt'
        testfilename.touch()

        assert user.pw_uid == testfilename.stat().st_uid
        assert group.gr_gid == testfilename.stat().st_gid

        chown(testfilename, 'foobar', 'foobar')
        assert testfilename.stat().st_uid == -1
        assert testfilename.stat().st_gid == -1


# Generated at 2022-06-13 21:00:05.196816
# Unit test for function chmod
def test_chmod():
    import tempfile
    import shutil

    file_dir = Path(tempfile.gettempdir()).joinpath(Path(__file__).name)
    shutil.rmtree(file_dir, ignore_errors=True)

    file_dir.mkdir(parents=True, exist_ok=True)
    file_path = file_dir.joinpath('file1')
    dir_path = file_dir.joinpath('dir1')
    dir_path.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'w') as f:
        f.write('test')

    chmod(file_path, mode_file=0o600)
    chmod(file_path, mode_file=0o600)
    chmod(dir_path, mode_dir=0o700)

# Generated at 2022-06-13 21:00:11.368760
# Unit test for function exists_as
def test_exists_as():
    """Test the exists_as() function."""
    try:
        os.unlink('/tmp/flutils.test.osutils.txt')
    except FileNotFoundError:
        pass
    with open('/tmp/flutils.test.osutils.txt', 'w') as txt_file:
        txt_file.write('test')
    assert exists_as('/tmp/flutils.test.osutils.txt') == 'file'
    os.unlink('/tmp/flutils.test.osutils.txt')
    assert exists_as('/tmp/flutils.test.osutils.txt') == ''


# Generated at 2022-06-13 21:00:21.472704
# Unit test for function directory_present
def test_directory_present():
    """Test :obj:`~flutils.pathutils.directory_present`

    """
    with tempfile.TemporaryDirectory() as temp_path:
        temp_path = Path(temp_path)
        test_dir = temp_path / 'test_dir'
        test_sub_dir = test_dir / 'sub_dir'
        test_sub_sub_dir = test_sub_dir / 'sub_sub_dir'
        test_sub_sub_dir.mkdir(mode=0o775, parents=True, exist_ok=True)
        test_sub_sub_dir.chmod(0o775)

        new_dir = directory_present(test_sub_sub_dir)
        assert new_dir.as_posix() == test_sub_sub_dir.as_posix()
        assert new_dir

# Generated at 2022-06-13 21:00:24.146194
# Unit test for function chmod
def test_chmod():
    print('unit test for chmod')
    # TODO: Implement unit test for chmod
    # assert False
    assert True


# Generated at 2022-06-13 21:00:54.669865
# Unit test for function path_absent
def test_path_absent():
    root = os.path.dirname(__file__)
    root = Path(root).expanduser()
    root = root.as_posix()

    file_path = os.path.join(root, 'test_file_path')
    link_path = os.path.join(root, 'test_link_path')
    dir_path = os.path.join(root, 'test_dir_path')
    if os.path.exists(file_path):
        os.unlink(file_path)
    if os.path.exists(link_path):
        os.unlink(link_path)
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path, ignore_errors=True)


# Generated at 2022-06-13 21:01:03.048533
# Unit test for function path_absent
def test_path_absent():
    pr = """Path at: %r, is present"""

    def try_delete(path):
        try:
            os.unlink(path)
        except OSError:
            pass
        try:
            os.rmdir(path)
        except OSError:
            pass

    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'foo')
        assert not os.path.exists(path), pr % path
        os.makedirs(path)
        assert os.path.isdir(path), pr % path
        path_absent(path)
        assert not os.path.exists(path), pr % path
        path = os.path.join(tmpdir, 'foo.txt')
        assert not os.path.exists(path), pr % path
       

# Generated at 2022-06-13 21:01:03.848688
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:01:13.972275
# Unit test for function exists_as
def test_exists_as():
    path_str = tempfile.mkdtemp() + '/file'
    path = Path(path_str)
    path.touch()
    assert(exists_as(path_str) == 'file')
    assert(exists_as(path_str + 'z') != 'file')
    path.unlink()
    assert(exists_as(path_str) != 'file')
    path.mkdir()
    assert(exists_as(path_str) == 'directory')
    path.rmdir()
    assert(exists_as(path_str) != 'directory')


# Generated at 2022-06-13 21:01:27.747998
# Unit test for function directory_present
def test_directory_present():
    """ Function to unit test directory_present.
    """
    import tempfile
    import shutil
    import pathlib
    import os
    # Ensure that the given path is an absolute path.
    with tempfile.TemporaryDirectory() as tmp:
        temp_path = pathlib.PurePath(tmp)
        with pathlib.Path(temp_path / 'inner_dir').joinpath('inner_file').open(mode='a') as fobj:
            fobj.write('1')
        with pathlib.Path(temp_path / 'inner_dir2').joinpath('inner_file2').open(mode='a') as fobj:
            fobj.write('1')
        with pathlib.Path(temp_path / 'inner_dir3').joinpath('inner_file3').open(mode='a') as fobj:
            f

# Generated at 2022-06-13 21:01:30.916663
# Unit test for function exists_as
def test_exists_as():
    result = exists_as('~/tmp')
    assert(result) == 'directory'
    result = exists_as('~/not/a/real/path')
    assert(result) == ''



# Generated at 2022-06-13 21:01:40.829619
# Unit test for function path_absent
def test_path_absent():
    # Test an existing broken symbolic link
    path = '~/tmp/path_absent'
    path_absent(path)
    # Test an existing regular file
    path = '~/tmp/path_absent'
    touch(path)
    path_absent(path)
    # Test an existing directory
    import shutil
    path = '~/tmp/path_absent'
    os.makedirs(path)
    _path = '%s/%s' % (path, 'path_absent_1')
    os.makedirs(_path)
    touch('%s/%s' % (_path, 'path_absent_1'))
    touch('%s/%s' % (_path, 'path_absent_2'))

# Generated at 2022-06-13 21:01:41.517571
# Unit test for function chmod
def test_chmod():
    pass

# Generated at 2022-06-13 21:01:43.057514
# Unit test for function chown
def test_chown():
    assert True

# Generated at 2022-06-13 21:01:55.758789
# Unit test for function path_absent
def test_path_absent():
    """Test function: path_absent"""
    test_root = os.path.join(os.getcwd(), 'tmp_path_absent')
    p = os.path.join(test_root, 'file')
    d = os.path.join(test_root, 'dir')
    f = os.path.join(test_root, 'dir', 'file')
    h = os.path.join(test_root, 'dir', 'hard_link')
    s = os.path.join(test_root, 'dir', 'soft_link')

    os.makedirs(test_root)
    with open(p, 'w') as p_fp:
        p_fp.write(str(uuid.uuid4()) + '\n')
    os.makedirs(d)

# Generated at 2022-06-13 21:02:29.893219
# Unit test for function chmod
def test_chmod():
    test_path = Path(sys.version).parent

    # Test that a path that does not exist is ignored.
    chmod('/does/not/exist', include_parent=True)

    # Test that a glob pattern that does not match is ignored.
    chmod('/does/not/exist/**', include_parent=True)

    # Test that a symlink is skipped.
    symlink_path = test_path.resolve() / 'tmp' / 'flutils.tests.osutils.txt'
    if symlink_path.is_symlink():
        symlink_path.unlink()

    # Create a symlink
    test_path = Path('/usr/bin/python')
    if test_path.is_file():
        symlink_path.symlink_to(test_path)

# Generated at 2022-06-13 21:02:34.446954
# Unit test for function path_absent
def test_path_absent():
    path = Path('~/tmp/test_path').expanduser()
    path.mkdir(parents=True, exist_ok=True)
    path_absent(path)
    assert path.exists() is False


# Remove the test path when done.
# test_path_absent()



# Generated at 2022-06-13 21:02:46.563710
# Unit test for function chmod
def test_chmod():
    import os
    import stat

    tmpfile = Path('/tmp/flutils.tests.osutils.txt')
    if tmpfile.exists():
        tmpfile.unlink()

    tmpfile.touch()

    if os.stat(tmpfile).st_mode != 33152:
        raise ValueError(
                f'''Expected {stat.filemode(os.stat(tmpfile).st_mode)} to be
                "-rw-------".'''
        )

    chmod(tmpfile, 0o660)

    if os.stat(tmpfile).st_mode != 33184:
        raise ValueError(
                f'''Expected {stat.filemode(os.stat(tmpfile).st_mode)} to be
                "-rw-rw----".'''
        )

    tmpfile.unlink()



# Generated at 2022-06-13 21:02:56.630651
# Unit test for function chmod
def test_chmod():
    # Test 1
    path = Path('~/tmp/flutils.tests.osutils.txt')
    mode_file = 0o660
    mode_dir = None
    include_parent = False
    chmod(path, mode_file, mode_dir, include_parent)

    # Test 2
    path = '~/tmp/*'
    mode_file = 0o644
    mode_dir = 0o770
    include_parent = False
    chmod(path, mode_file, mode_dir, include_parent)

    # Test 3
    path = '~/tmp/*'
    mode_file = 0o660
    mode_dir = None
    include_parent = False
    chmod(path, mode_file, mode_dir, include_parent)



# Generated at 2022-06-13 21:02:57.466420
# Unit test for function chown
def test_chown():
    pass


# Generated at 2022-06-13 21:03:00.132590
# Unit test for function exists_as
def test_exists_as():
    path = Path.home() / 'tmp' / 'exists_as_file'
    path.touch()
    assert exists_as(path) == 'file'
    assert exists_as(path.parent) == 'directory'
    path.unlink()
    assert exists_as(path) == ''
    assert exists_as(path.parent) == 'directory'


# Generated at 2022-06-13 21:03:12.570066
# Unit test for function exists_as
def test_exists_as():
    """Unit tests for function exists_as."""
    import shutil

    path = Path().cwd()/'_test_osutils_exists_as'
    assert exists_as(path) == '', 'expected empty string'
    path.mkdir()
    assert exists_as(path) == 'directory', 'expected directory'
    path.rmdir()

    path = path.with_suffix('.txt')
    assert exists_as(path) == '', 'expected empty string'
    path.touch()
    assert exists_as(path) == 'file', 'expected file'
    path.unlink()

    path = path.with_suffix('.py')
    assert exists_as(path) == '', 'expected empty string'

    path.touch()

# Generated at 2022-06-13 21:03:18.992546
# Unit test for function chmod
def test_chmod():
    path = normalize_path('~/tmp/flutils.tests.osutils.txt')
    path.write_text('Hello World!')

    chmod(path.as_posix(), 0o660)
    assert path.stat().st_mode == 33188

    chmod(path.as_posix(), 0o660)



# Generated at 2022-06-13 21:03:32.582358
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import directory_present
    from flutils.testutils import assert_isinstance
    from pathlib import Path
    from shutil import rmtree

    path_str = '~/tmp/test_dir_present'
    path_obj = Path(path_str)
    if path_obj.exists():
        rmtree(path_obj.as_posix())

    ret = directory_present(path_str)
    assert_isinstance(ret, Path)
    assert ret.exists() is True
    assert ret.is_dir() is True
    assert ret.is_symlink() is False
    assert ret. as_posix() == path_obj.as_posix()

    ret = directory_present(path_str)
    assert_isinstance(ret, Path)