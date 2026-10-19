

# Generated at 2022-06-13 20:54:03.336305
# Unit test for function find_paths
def test_find_paths():
    """Test find_paths() to ensure the function returns the expected outputs."""
    with TemporaryDirectory(prefix='flutils.tests.') as tmpdir:
        # Create a directory and a file that has a space in it's filename.
        # This will be used to generate an exception.
        Path(tmpdir).joinpath('test user').mkdir()
        Path(tmpdir).joinpath('test_file.txt').touch()
        Path(tmpdir).joinpath('test user').joinpath('test_file.txt').touch()

        # find_paths() returns a generator in a list
        # which will return True when compared
        # to the list of the expected results.

# Generated at 2022-06-13 20:54:05.840448
# Unit test for function find_paths
def test_find_paths():
    pass



# Generated at 2022-06-13 20:54:17.537087
# Unit test for function find_paths
def test_find_paths():
    # Check glob pattern with a partial path.
    pattern = '~/tmp'
    pattern = normalize_path(pattern)
    search = pattern.as_posix()
    assert list(Path().glob(search))

    # Check glob pattern with a partial path.
    pattern = '~/tmp/*'
    pattern = normalize_path(pattern)
    search = pattern.as_posix()
    assert list(Path().glob(search))

    # Check glob pattern with a partial path.
    pattern = '~/tmp/*/flutils.tests'
    pattern = normalize_path(pattern)
    search = pattern.as_posix()
    assert list(Path().glob(search))



# Generated at 2022-06-13 20:54:22.533030
# Unit test for function get_os_user
def test_get_os_user():
    test = get_os_user('test')
    assert isinstance(test, pwd.struct_passwd)
    assert test[0] == 'test'
    assert test.pw_name == 'test'



# Generated at 2022-06-13 20:54:31.229018
# Unit test for function chown
def test_chown():
    from .pathutils import chown
    from .osutils import directory_present
    from .osutils import path_absent

    directory_present('/tmp/test_chown', mode=0o700)
    chown('/tmp/test_chown', user='-1')
    path_absent('/tmp/test_chown/flutils.tests.osutils.txt')
    chown('/tmp/test_chown', user=getpass.getuser())
    path_absent('/tmp/test_chown')



# Generated at 2022-06-13 20:54:37.596259
# Unit test for function chown
def test_chown():
    # Test for any Path
    chown('/', user='foo', group='bar')
    chown(Path('/'), user='foo', group='bar')
    chown(PosixPath('/'), user='foo', group='bar')
    chown(WindowsPath('C:\\'), user='foo', group='bar')
    # Test for glob pattern
    assert 'bar' in subprocess.check_output(['ls', '-lha', '/']).decode()



# Generated at 2022-06-13 20:54:45.293643
# Unit test for function directory_present
def test_directory_present():
    assert directory_present(
            '~/tmp/flutils.tests.pathutils.directory_present.txt'
        ).as_posix() == os.path.realpath(
            '~/tmp/flutils.tests.pathutils.directory_present.txt'
        )
    assert directory_present(
            '~/tmp/flutils.tests.pathutils/directory_present.txt'
        ).as_posix() == os.path.realpath(
            '~/tmp/flutils.tests.pathutils/directory_present.txt'
        )

# Generated at 2022-06-13 20:54:47.602297
# Unit test for function get_os_user
def test_get_os_user():
    name = 'dummy'
    pwd.getpwnam(name)



# Generated at 2022-06-13 20:54:54.857099
# Unit test for function get_os_user
def test_get_os_user():
    rtn = get_os_user()
    assert rtn.pw_uid == os.getuid()
    assert rtn.pw_gid == os.getgid()
    assert isinstance(rtn, pwd.struct_passwd)

    get_os_user(0)
    get_os_user(os.getuid())
    with pytest.raises(OSError):
        get_os_user(-1)

    with pytest.raises(OSError):
        get_os_user(os.getuid() + 1)


# Generated at 2022-06-13 20:55:04.120691
# Unit test for function directory_present
def test_directory_present():
    import pytest
    from shutil import rmtree
    from tempfile import TemporaryDirectory
    from flutils.pathutils import directory_present

    path = directory_present(
        '~/tmp/test_directory_present_path/test1/test2',
        mode=0o751
    )
    assert path.is_dir() is True
    assert path.stat().st_mode == 33261
    assert path.owner() == getpass.getuser()
    assert path.group() == grp.getgrgid(os.getgid()).gr_name

    path = directory_present(
        '~/tmp/test_directory_present_path/test1',
        mode=0o751
    )
    assert path.is_dir() is True
    assert path.stat().st_mode == 33261

# Generated at 2022-06-13 20:55:27.967687
# Unit test for function find_paths
def test_find_paths():
    from tempfile import mkdtemp
    from shutil import rmtree
    from pathlib import Path
    from flutils.pathutils import find_paths

    tmp_dir = Path(mkdtemp())
    file_one = Path(tmp_dir / 'file_one')
    dir_one = Path(tmp_dir / 'dir_one')
    dir_one.mkdir(mode=0o700)

    try:
        with file_one.open(mode='w', encoding='utf-8') as fh:
            fh.write('testing')

        pattern = Path(f'{tmp_dir}/*')

        result = list(find_paths(pattern))
        assert result == [file_one, dir_one]

    finally:
        rmtree(tmp_dir)



# Generated at 2022-06-13 20:55:31.008650
# Unit test for function directory_present
def test_directory_present():
    path = directory_present('~/tmp/test_path')
    assert str(path) == '/Users/len/tmp/test_path'
    assert path.is_dir() is True



# Generated at 2022-06-13 20:55:33.024954
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:55:38.600373
# Unit test for function find_paths
def test_find_paths():
    import functools
    import tempfile

    test_dir = tempfile.TemporaryDirectory()

    def write_temp_file():
        import random
        import string

        f_path = Path(test_dir.name) / Path(
            ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(8)
            )
        )

        f_path.touch()
        return f_path

    sample_file_paths = [write_temp_file() for _ in range(3)]
    test_dir.cleanup()

    try:
        assert find_paths(test_dir.name) is None
    except AssertionError:
        assert False


# Generated at 2022-06-13 20:55:47.868221
# Unit test for function find_paths
def test_find_paths():
    tmp_path = Path().cwd() / 'tmp/find_paths.test'
    tmp_path.mkdir(parents=True, exist_ok=True)

    (tmp_path / 'file_one').touch()
    (tmp_path / 'file_two').touch()
    (tmp_path / 'dir_one').mkdir()
    (tmp_path / 'dir_one' / 'file_three').touch()

    found_paths = list(find_paths(tmp_path.as_posix()))
    assert sorted(found_paths) == sorted([
        tmp_path / 'dir_one', tmp_path / 'dir_one' / 'file_three',
        tmp_path / 'file_one', tmp_path / 'file_two'
    ])


# Generated at 2022-06-13 20:55:54.542946
# Unit test for function path_absent
def test_path_absent():
    """Unit test for function path_absent."""
    test_path = Path('~/tmp/test_path').expanduser()
    test_path.mkdir(parents=True)
    test_path.joinpath('test_file').touch()
    test_path.joinpath('test_dir').mkdir()
    path_absent(test_path)

# Generated at 2022-06-13 20:56:03.589982
# Unit test for function chown
def test_chown():
    with TemporaryDirectory() as tmpdir:
        user = getpass.getuser()
        group = grp.getgrgid(os.getgid()).gr_name

        # create a test directory and files
        path = Path(tmpdir)
        file1 = path / 'flutils.tests.osutils_file.txt'
        file2 = path / 'flutils.tests.osutils_file2.txt'

        dir1 = path / 'flutils.tests.osutils_dir'
        dir1.mkdir()

        file1.touch()
        file2.touch()

        chown(dir1, user, group)
        chown(file1, user, group)

        chown(path / 'flutils.tests.osutils_*', user, group)


# Generated at 2022-06-13 20:56:14.661157
# Unit test for function directory_present
def test_directory_present():
    kwargs = {
        'mode': 0o660,
        'user': getpass.getuser(),
        'group': getpass.getuser(),
    }
    directory = '~/tmp/flutils.tests/osutils/directory_present.{}'.format(
        os.getpid()
    )
    path = directory_present(directory, **kwargs)
    assert path.as_posix() == directory
    assert path.is_dir() is True
    assert path.stat().st_mode == 0o40700
    assert path.stat().st_uid == os.getuid()
    assert path.stat().st_gid == os.getgid()
    assert path.parent.as_posix() == '~/tmp/flutils.tests/osutils'
    assert path.parent.is_dir()

# Generated at 2022-06-13 20:56:21.877545
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    import os
    import pathlib

    path = 'example.txt'

    if os.path.exists(path):
        os.remove(path)

    with open(path, 'w') as fh:
        fh.write('Example')

    chmod(path, mode_file=0o600)
    assert os.stat(path).st_mode & 0o777 == 0o600

    os.remove(path)



# Generated at 2022-06-13 20:56:23.131483
# Unit test for function chown
def test_chown():
    assert 2 == 2

# Generated at 2022-06-13 20:56:36.078863
# Unit test for function chown
def test_chown():
    chown(Path.cwd() / "file.txt")
    assert True



# Generated at 2022-06-13 20:56:37.469358
# Unit test for function chmod
def test_chmod():
    assert callable(chmod)



# Generated at 2022-06-13 20:56:50.190416
# Unit test for function chmod
def test_chmod():
    #
    # simple file
    with tempfile.NamedTemporaryFile(mode='w', dir=os.path.expanduser('~/tmp'), delete=False) as f:
        f.write('test')
        basename = os.path.basename(f.name)

    try:
        chmod(f'~/tmp/{basename}', 0o660)
        file_mode = stat.S_IMODE(os.lstat(f'~/tmp/{basename}').st_mode)
        assert file_mode == 0o660
    finally:
        os.remove(f'~/tmp/{basename}')

    #
    # simple directory
    os.makedirs(f'~/tmp/{basename}')

# Generated at 2022-06-13 20:57:01.293032
# Unit test for function chmod
def test_chmod():
    path = Path(__file__).parent
    try:
        chmod(path, mode_file=0o444, mode_dir=0o555)
        assert path.exists()
        assert (path.stat().st_mode & 0o777) == 0o555
        assert (path.parent.stat().st_mode & 0o777) == 0o555
    finally:
        chmod(path, mode_file=0o600, mode_dir=0o700)
        assert path.exists()
        assert (path.stat().st_mode & 0o777) == 0o700
        assert (path.parent.stat().st_mode & 0o777) == 0o700
    assert path.exists()



# Generated at 2022-06-13 20:57:02.176645
# Unit test for function chmod
def test_chmod():
    pass

# Generated at 2022-06-13 20:57:04.675474
# Unit test for function find_paths
def test_find_paths():
    pattern = normalize_path('~/tmp/**')
    actual = list(find_paths(pattern))
    assert actual



# Generated at 2022-06-13 20:57:08.894049
# Unit test for function find_paths
def test_find_paths():
    path = '/home/test_user/tmp'
    pattern = os.path.join(path, '*')
    paths = find_paths(pattern)
    paths = [path.resolve() for path in paths]
    assert len(paths) == 2
    assert os.path.join(path, 'file_one') in paths
    assert os.path.join(path, 'dir_one') in paths



# Generated at 2022-06-13 20:57:23.405907
# Unit test for function find_paths
def test_find_paths():
    from flutils.pathutils import find_paths
    from flutils import get_temp_directory
    from flutils.osutils import makedirs
    from flutils.osutils import touch


# Generated at 2022-06-13 20:57:30.455692
# Unit test for function exists_as
def test_exists_as():
    # directory
    assert exists_as(__file__) == 'file'
    assert exists_as(Path(__file__).parent) == 'directory'
    # broken symbolic link
    assert exists_as(Path(__file__).with_name('._stub_pathutils.py')) == ''
    # permission errors
    assert exists_as(Path(__file__).with_name('_stub_pathutils.py')) == 'file'
# Unit test function exists_as



# Generated at 2022-06-13 20:57:42.523012
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/dev/stdin') == 'char device'
    assert exists_as('/dev/stdout') == 'char device'
    assert exists_as('/dev/stderr') == 'char device'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/dev/full') == 'char device'
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/tty0') == 'char device'
    assert exists_as('/dev/console') == 'char device'

# Generated at 2022-06-13 20:57:54.111859
# Unit test for function exists_as
def test_exists_as():
    """Test :obj:`flutils.pathutils.exists_as`.
    """
    assert exists_as('/etc') == 'directory'
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/etc/hosts.t_does_not_exist') == ''



# Generated at 2022-06-13 20:58:01.558014
# Unit test for function chmod
def test_chmod():
    # chmod a file
    test_file = normalize_path('~/tmp/flutils.tests.osutils.txt')
    test_file.write_text('')

    chmod(test_file, mode_file=0o664, mode_dir=0o770)

    assert test_file.stat().st_mode & 0o7777 == 0o664



# Generated at 2022-06-13 20:58:03.180649
# Unit test for function path_absent
def test_path_absent():  # pylint: disable=unused-argument
    """ Unit test for flutils.pathutils.path_absent() """
    assert True
# end unit_test



# Generated at 2022-06-13 20:58:05.246734
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    assert exists_as('~/tmp') == 'directory'



# Generated at 2022-06-13 20:58:05.933250
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:58:08.648109
# Unit test for function chown
def test_chown():
    if sys.platform == 'linux':
        import doctest
        doctest.run_docstring_examples(chown, globals())


# Generated at 2022-06-13 20:58:17.969213
# Unit test for function chown
def test_chown():
    import stat
    uid = os.getuid()
    gid = os.getgid()
    mode_file = 0o660
    mode_dir = 0o775
    path = normalize_path('./tmp/flutils.tests.osutils.txt')
    path2 = normalize_path('./tmp/flutils.tests/osutils')
    fpath = path.parent

# Generated at 2022-06-13 20:58:28.917190
# Unit test for function chown
def test_chown():
    import tempfile
    import unittest

    class TestChown(unittest.TestCase):
        def setUp(self):
            self.path = Path(tempfile.mkdtemp())

        def tearDown(self):
            if self.path.exists():
                self.path.rmdir()

        def _get_stats(self, path: Path) -> dict:
            st = {}
            if path.exists() is True:
                st = path.stat()
            return {'uid': st.st_uid,
                    'gid': st.st_gid}

        def test_chown_basics(self):
            # chown by user that exists
            user = getpass.getuser()
            group = grp.getgrgid(os.getgid()).gr_name

            self

# Generated at 2022-06-13 20:58:40.530105
# Unit test for function exists_as
def test_exists_as():
    """Test for flutils.pathutils.exists_as"""

    assert exists_as('/tmp/test1') == ''
    assert exists_as('/tmp/test2/test3') == ''

    # Exists as directory
    os.mkdir('/tmp/test1')
    assert exists_as('/tmp/test1') == 'directory'

    # Exists as file
    fd = open('/tmp/test1/test2', 'w')
    fd.close()
    assert exists_as('/tmp/test1/test2') == 'file'

    # Exists as block device
    assert exists_as('/tmp/test1/test3') == ''
    os.mknod('/tmp/test1/test3', 0o660 | stat.S_IFBLK)
    assert exists_as

# Generated at 2022-06-13 20:58:46.730511
# Unit test for function directory_present
def test_directory_present():
    from pathlib import Path
    import stat

    path = directory_present('/tmp/test_directory_present')
    assert type(path) is Path
    assert path.is_dir() is True
    assert path.exists() is True
    assert os.stat(path.as_posix()).st_mode & stat.S_IRWXU == stat.S_IRWXU



# Generated at 2022-06-13 20:59:03.722991
# Unit test for function chown
def test_chown():
    def _test_chown(user):
        uid = user.pw_uid
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / 'tmp'
            path.write_text('Test')
            assert path.is_dir() is False
            assert path.exists() is True
            assert path.stat().st_uid != uid
            chown(path, user.pw_name, include_parent=True)
            assert path.stat().st_uid == uid
            assert path.parent.stat().st_uid == uid

    try:
        some_user = pwd.getpwnam(getpass.getuser())
    except KeyError:
        some_user = pwd.getpwuid(os.getuid())

# Generated at 2022-06-13 20:59:14.877547
# Unit test for function chown
def test_chown():
    """
    Unit test for function chown
    """

    from ..pytestutils import (
        find_all_strings,
        find_one_string,
        run_func,
        write_test_file
    )

    path = write_test_file(
        'pathutils_test_chown',
        'test_chown',
        'test_chown',
    )

    # Test with user and group
    aspect_list_1 = [
        'bruno is the owner',
        'writer is the group',
        'mode of 644',
    ]
    test_result = run_func(
        chown,
        (path, 'bruno', 'writer')
    )
    assert test_result[0] == 0

# Generated at 2022-06-13 20:59:27.054823
# Unit test for function directory_present
def test_directory_present():

    path = normalize_path('/tmp/test_directory_present')

    # directory_present should create the path as a directory
    assert directory_present(path=path).exists() is True

    # directory_present should NOT raise an exception if the directory
    # already exists.
    assert directory_present(path=path).exists() is True

    # Test passing a PosixPath object
    p_path = normalize_path(path)
    assert directory_present(path=p_path).exists() is True

    # Test passing a WindowsPath object
    p_path = normalize_path(path)
    assert directory_present(path=p_path).exists() is True

    # Test with a glob pattern
    p_path = normalize_path(path)
    with pytest.raises(ValueError):
        directory

# Generated at 2022-06-13 20:59:32.166754
# Unit test for function chmod
def test_chmod():
    test_str = "~/tmp/flutils.tests.osutils.txt"
    chmod(test_str, mode_file=0o640)
    assert os.stat(test_str).st_mode & 0o777 == 0o640



# Generated at 2022-06-13 20:59:33.419123
# Unit test for function chmod
def test_chmod():
    # Not implemented
    pass



# Generated at 2022-06-13 20:59:43.545305
# Unit test for function path_absent
def test_path_absent():
    if os.path.exists('./test_dir'):
        path_absent('./test_dir')
    assert os.path.exists('./test_dir') is False
    mkdir('./test_dir')
    path_absent('./test_dir')
    assert os.path.exists('./test_dir') is False
    with open('./test_dir', 'w') as fh:
        fh.write("foo")
    path_absent('./test_dir')
    assert os.path.exists('./test_dir') is False
    os.symlink('./test_dir', './test_dir')
    path_absent('./test_dir')
    assert os.path.exists('./test_dir') is False



# Generated at 2022-06-13 20:59:46.693797
# Unit test for function chmod
def test_chmod():
    chmod(os.path.join(os.path.expanduser('~'), 'tmp', 'test*'))



# Generated at 2022-06-13 20:59:59.860267
# Unit test for function exists_as
def test_exists_as():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmpdir:
        # Test for a block device
        block_device = Path(tmpdir, 'block_device')
        os.mknod(block_device.as_posix(), 0o600 | stat.S_IFBLK)
        assert exists_as(block_device) == 'block device'

        # Test for a character device
        char_device = Path(tmpdir, 'char_device')
        os.mknod(char_device.as_posix(), 0o600 | stat.S_IFCHR)
        assert exists_as(char_device) == 'char device'

        directory = Path(tmpdir, 'dir')
        directory.mkdir(0o770)
        assert exists_as(directory) == 'directory'

        # Test for a symbolic link to

# Generated at 2022-06-13 21:00:01.551010
# Unit test for function chown
def test_chown():
    chown(os.path.abspath('test.txt'))



# Generated at 2022-06-13 21:00:15.188957
# Unit test for function path_absent
def test_path_absent():
    test_dir = normalize_path('~/tmp/flutils_test_files/test_dir')
    test_file = test_dir / 'test_file.txt'
    test_link = test_dir / 'test_link'
    path_present(test_dir, mode_dir=0o754)
    path_present(test_file, mode_file=0o644)
    os.symlink(test_file.as_posix(), test_link.as_posix())
    path_absent(test_dir)
    assert os.path.exists(test_dir.as_posix()) is False
    assert os.path.exists(test_file.as_posix()) is False
    assert os.path.exists(test_link.as_posix()) is False

# Generated at 2022-06-13 21:00:31.856142
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import directory_present
    from flutils.pathutils import exists_as
    from flutils.pathutils import normalize_path
    from flutils.osutils import remove

    path = normalize_path('~/tmp/flutils/osutils/test_directory_present')
    path_exists_as = exists_as(path)
    if path_exists_as == 'directory':
        remove(path, recursive=True)

    _path = directory_present(path)
    assert _path.as_posix() == path.as_posix()

    _path = directory_present(path, mode=0o755)
    assert _path.as_posix() == path.as_posix()


# Generated at 2022-06-13 21:00:41.269460
# Unit test for function path_absent
def test_path_absent():
    test_ok = False
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        dir_path = tmpdir / 'dir_dir'
        file_path = tmpdir / 'dir_file'
        dir_path.mkdir()
        file_path.touch()
        path_absent(dir_path)
        path_absent(file_path)
        if not dir_path.exists():
            if not file_path.exists():
                test_ok = True
    assert test_ok is True, 'path_absent failed.'



# Generated at 2022-06-13 21:00:51.402415
# Unit test for function exists_as
def test_exists_as():
    """Test exists_as().

    Test exists_as() by first testing exists_as() against a path that does not
    exist and  then exist_as() on a directory to ensure the
    directory_present() function works for directories that already exist.

    """
    path = Path('/tmp')
    path = path / 'flutils'
    path = path / 'unit_tests'
    path = path / 'exists_as.txt'

    directory_present(path.parent)

    assert exists_as(path) == '', \
        'The exists_as() function did not return the expected value.'

    assert exists_as(path.parent) == 'directory', \
        'The exists_as() function did not return the expected value.'



# Generated at 2022-06-13 21:01:03.253297
# Unit test for function chmod
def test_chmod():
    _temp_dir = Path('/tmp/fltests')
    _temp_dir.mkdir(parents=True, exist_ok=True)

    _src_file = _temp_dir / 'chmod.src.txt'
    _src_file.touch()
    _src_file.chmod(0o744)
    _dest_dir = _temp_dir / 'chmod.dest'
    _dest_dir.mkdir(parents=True, exist_ok=True)

    chmod(_src_file)
    chmod(_dest_dir)
    assert _src_file.stat().st_mode == 33279
    assert _dest_dir.stat().st_mode == 16877

    chmod(_src_file, mode_file=0o660, mode_dir=0o770)

# Generated at 2022-06-13 21:01:16.885365
# Unit test for function path_absent
def test_path_absent():
    """ Test path_absent
    """
    # For this test, we will use the /tmp directory.
    path = normalize_path('~/tmp/path_absent%d' % time.time())
    path_absent(path)
    assert not os.path.exists(path.as_posix())

    # Test happy path with a regular file
    path_one = path / 'path_one'
    with path_one.open('w') as file_object:
        file_object.write('foo')
    assert os.path.exists(path_one.as_posix())
    path_absent(path)
    assert not os.path.exists(path_one.as_posix())
    assert not os.path.exists(path.as_posix())

    # Test happy path with

# Generated at 2022-06-13 21:01:22.499179
# Unit test for function directory_present
def test_directory_present():
    path = directory_present(
        Path(__file__).parent / 'data' / 'directory_present.txt'
    )
    assert isinstance(path, Path) is True
    assert path.exists() is True
    assert path.is_dir() is True



# Generated at 2022-06-13 21:01:34.469631
# Unit test for function directory_present
def test_directory_present():
    path = Path('/tmp/flutils_test_directory_present')
    directory_present(path)
    assert path.exists() is True
    assert path.is_dir() is True
    path.rmdir()

    path = Path('/tmp/flutils_test_directory_present/sub_dir')
    directory_present(path)
    assert path.exists() is True
    assert path.is_dir() is True
    path.rmdir()
    path.parent.rmdir()

    path = Path('~/tmp/flutils_test_directory_present/sub_dir/sub_sub_dir')
    directory_present(path)
    assert path.exists() is True
    assert path.is_dir() is True
    path.rmdir()
    path.parent.rmdir()

# Generated at 2022-06-13 21:01:40.319896
# Unit test for function path_absent
def test_path_absent():
    path = normalize_path('~/tmp/foo/bar/baz')
    path = cast(Path, path)
    path.mkdir(mode=0o700, parents=True)
    path_absent('~/tmp/foo')
    assert path.exists() is False



# Generated at 2022-06-13 21:01:50.982005
# Unit test for function chmod
def test_chmod():
    """Test function chmod()."""
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from os import stat

    with TemporaryDirectory() as tmpdir:
        tmpfile = Path(tmpdir, 'tmp.txt')
        tmpfile.write_text('this is a temp file')

        chmod(tmpfile)
        assert stat(tmpfile).st_mode & 0o777 == 0o600

        chmod(tmpfile, 0o660)
        assert stat(tmpfile).st_mode & 0o777 == 0o660

        chmod(tmpfile, 0o660, mode_dir=0o770)
        assert stat(tmpfile).st_mode & 0o777 == 0o660

        chmod(tmpfile, 0o660, 0o770)

# Generated at 2022-06-13 21:01:59.401204
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod, path_absent
    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as tmpdir:
        # Create a file and check the file mode.
        Path(tmpdir, 'flutils.tests.osutils.txt').touch()
        chmod(Path(tmpdir, 'flutils.tests.osutils.txt'), 0o664)
        assert path_absent(
            Path(tmpdir, 'flutils.tests.osutils.txt'),
            mode_file=0o664
        ) is False

        # Create the directories and the associated test files.
        Path(tmpdir, 'flutils.tests.osutils.a').mkdir(parents=True)

# Generated at 2022-06-13 21:02:14.912869
# Unit test for function chown
def test_chown():
    from flutils.pathutils import (
        chown,
        get_os_user_id,
    )
    from flutils.osutils import which
    from pathlib import Path

    import os
    import sys
    import tempfile

    existing_user = get_os_user_id()
    existing_group = os.getgid()
    if sys.platform == 'darwin':
        bin_touch = which('touch')
    else:
        bin_touch = which('/bin/touch')
    if bin_touch is None:
        raise AssertionError('touch command is required.')

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        file = tmpdir / 'flutils.tests.osutils.txt'
        subdir = tmpdir / 'subdir'


# Generated at 2022-06-13 21:02:26.325092
# Unit test for function chmod
def test_chmod():
    import os
    import os.path
    import random

    def _test_chmod_single():
        dpath = Path('test_chmod_single_dir')
        fpath = Path.joinpath(dpath, 'test_chmod_single_file')

        dpath.mkdir()
        Path(fpath).touch()
        stat = os.stat(fpath)
        old_mode = stat.st_mode

        chmod(fpath, 0o660)

        stat = os.stat(fpath)
        assert stat.st_mode != old_mode
        Path(fpath).unlink()
        Path(dpath).rmdir()

    def _test_chmod_multiple_pattern():
        dpath = Path('test_chmod_multiple_pattern_dir')

# Generated at 2022-06-13 21:02:31.732254
# Unit test for function chown
def test_chown():
    chown('./bob_dylan', '-1', '-1')
    chown('./bob_dylan')
    chown('./bob_dylan', include_parent=True)

# Generated at 2022-06-13 21:02:32.408324
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:02:45.195212
# Unit test for function chmod
def test_chmod():
    import os
    import tempfile
    import shutil

    tmp_dir = tempfile.mkdtemp()
    tmp = os.path.join(tmp_dir, '__unit_tests__')
    tmp_sub = os.path.join(tmp, 'sub')
    tmp_sub_a = os.path.join(tmp_sub, 'sub_a')
    tmp_sub_b = os.path.join(tmp_sub, 'sub_b')
    tmp_sub_a_sub_sub = os.path.join(tmp_sub_a, 'sub_sub')
    tmp_sub_b_sub_sub = os.path.join(tmp_sub_b, 'sub_sub')

# Generated at 2022-06-13 21:02:54.099829
# Unit test for function chmod
def test_chmod():
    import os
    import shutil
    import tempfile
    #
    # Setup
    #
    directory = tempfile.TemporaryDirectory()
    os.makedirs(
        os.path.join(directory.name, 'a/b/c'),
        mode=0o700
    )
    a_path = Path().joinpath(
        directory.name, 'a/b/c/a.txt'
    )
    a_path.write_text('a')
    b_path = Path().joinpath(
        directory.name, 'a/b/c/b.txt'
    )
    b_path.write_text('b')
    b_path.chmod(0o600)

# Generated at 2022-06-13 21:02:57.382315
# Unit test for function chmod
def test_chmod():
    assert chmod('./test/test_pathutils/test_chmod/test_dir/file1.txt')



# Generated at 2022-06-13 21:03:01.544842
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(Path(os.path.dirname(__file__))) == 'directory'
    assert exists_as(__file__) == 'file'



# Generated at 2022-06-13 21:03:13.343769
# Unit test for function chown
def test_chown():
    import os
    import pathlib
    import pytest

    from flutils.pathutils import chown

    def create_test_file(path):
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        with open(path, 'w') as file_obj:
            file_obj.write('')
        return path.owner(), path.group()

    def _get_os_user(uid):
        '''Get information about an os user by id.
        '''
        return pwd.getpwuid(uid)

    def _get_os_group(gid):
        '''Get information about an os group by id.
        '''
        return grp.getgrgid(gid)

    def test_chown_normal():
        temp_file = path

# Generated at 2022-06-13 21:03:23.103085
# Unit test for function path_absent
def test_path_absent():
    """Unit test for function path_absent."""
    # Setup
    emptydir = os.path.join(TEST_DIR, 'empty')
    subdir = os.path.join(emptydir, 'sub')
    fileone = os.path.join(emptydir, 'file_one')
    filetwo = os.path.join(emptydir, 'file_two')
    link = os.path.join(emptydir, 'link')
    if sys.version_info.minor > 6:
        broken_link = os.path.join(emptydir, 'broken-link')
    # Cleanup
    if os.path.exists(emptydir):
        shutil.rmtree(emptydir)
    os.makedirs(emptydir, mode=0o700)
    os

# Generated at 2022-06-13 21:03:30.666686
# Unit test for function exists_as
def test_exists_as():
    mypath = Path('.')
    assert(exists_as(mypath) == 'directory')


# Generated at 2022-06-13 21:03:31.664359
# Unit test for function chown
def test_chown():
    pass

# Generated at 2022-06-13 21:03:33.254261
# Unit test for function chown
def test_chown():
    # Set up test fixtures
    pass



# Generated at 2022-06-13 21:03:34.064469
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:03:42.841871
# Unit test for function chown
def test_chown():
    import filecmp
    path = Path().absolute() / 'tests' / 'test_pathutils.py'
    path2 = Path().absolute() / 'tests' / 'test_chown.txt'
    path.touch()
    path2.touch()
    path.chown(0, 0)
    path2.chown(0, 0)
    assert os.stat(path.as_posix()).st_uid == 0
    assert os.stat(path2.as_posix()).st_uid == 0
    assert os.stat(path.as_posix()).st_gid == 0
    assert os.stat(path2.as_posix()).st_gid == 0
    chown(path)
    chown(path2)
    assert os.stat(path.as_posix()).st_