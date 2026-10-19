

# Generated at 2022-06-13 20:54:20.934603
# Unit test for function find_paths
def test_find_paths():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdirname = normalize_path(tmpdirname)
        file_one = tmpdirname / 'file_one'
        file_one.touch()
        file_two = tmpdirname / 'file_two'
        file_two.touch()
        dir_one = tmpdirname / 'dir_one'
        dir_one.mkdir()
        dir_two = tmpdirname / 'dir_two'
        dir_two.mkdir()
        assert list(find_paths(tmpdirname / '*')) == [file_one, dir_one]
        assert list(find_paths(tmpdirname / 'file_*')) == [file_one, file_two]

# Generated at 2022-06-13 20:54:27.147353
# Unit test for function chown
def test_chown():
    path = Path(__file__).parent / 'test_chown'
    if path.exists():
        path.unlink()

    if path.parent.exists():
        path.parent.rmdir()

    path.parent.mkdir()

    with path.open('w') as f:
        f.write('foo')

    uid = pwd.getpwnam(getpass.getuser()).pw_uid
    gid = grp.getgrnam(pwd.getpwuid(uid).pw_name).gr_gid

    path_st = os.stat(path.as_posix())
    assert path_st.st_uid == uid
    assert path_st.st_gid == gid

    chown(path)


# Generated at 2022-06-13 20:54:30.700265
# Unit test for function exists_as
def test_exists_as():
    assert exists_as("/") == "directory"


# Generated at 2022-06-13 20:54:38.190159
# Unit test for function find_paths
def test_find_paths():
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = normalize_path(tmp_dir)
        file_one = tmp_dir.joinpath('file_one')
        file_one.touch()
        dir_one = tmp_dir.joinpath('dir_one')
        dir_one.mkdir()
        found_paths = list(find_paths(tmp_dir))
        assert file_one in found_paths, "The file was not found as expected."
        assert dir_one in found_paths, "The directory was not found as expected."



# Generated at 2022-06-13 20:54:51.907550
# Unit test for function find_paths
def test_find_paths():
    from flutils.mock import MagicMock
    from flutils.mock import patch
    from flutils.pathutils import find_paths
    from pathlib import Path

    # Test if not iterable
    results = find_paths('~/tmp/')
    assert isinstance(results, Generator) is True

    mock_glob = MagicMock()

    with patch('flutils.pathutils.Path') as mock_path:
        mock_path.return_value.glob.return_value = mock_glob
        assert list(find_paths('~/tmp/**')) == mock_glob

    with patch('flutils.pathutils.Path') as mock_path:
        mock_path.return_value.glob.side_effect = NotImplementedError

# Generated at 2022-06-13 20:55:02.752612
# Unit test for function chmod
def test_chmod():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from pprint import pformat
    from flutils.pathutils import normalize_path
    from flutils.testutils import (
        FULL_MODE_FILE_AS_INT,
        NO_MODE_FILE_AS_INT,
        NO_MODE_DIR_AS_INT,
    )
    from flutils import osutils

    with TemporaryDirectory() as temp_dir:
        temp_dir = normalize_path(temp_dir)

        # Check if the temporary directory
        # has the correct mode (0700)
        assert temp_dir.stat().st_mode == NO_MODE_DIR_AS_INT

        # Create a file in the temporary directory
        # and make sure it's mode is correct (0600)

# Generated at 2022-06-13 20:55:14.935139
# Unit test for function exists_as
def test_exists_as():
    """Unit test for the function exists_as."""
    try:
        import pytest
    except ImportError:
        print('pytest module not found')
    else:
        from flutils.pathutils import exists_as

        # This is a test to make sure that if
        # exists_as() is run with a glob pattern
        # then it raises a ValueError.
        def test_exists_as_glob_pattern():
            with pytest.raises(ValueError):
                exists_as('/tmp/foo*')

        test_exists_as_glob_pattern()
        # End exists_as_glob_pattern test

        # This test makes sure that a non-existent
        # file or directory returns ''

# Generated at 2022-06-13 20:55:26.142092
# Unit test for function find_paths
def test_find_paths():
    with temppathlib.TemporaryDirectory(prefix='test_find_paths_') as tmpdir:
        path = Path(tmpdir)
        file_one = path / 'file_one'
        file_one.touch()
        dir_one = path / 'dir_one'
        dir_one.mkdir()

        glob_dotted_files = path / '.glob_*'
        glob_dotted_files.touch()

        dotted_dir = path / '.dotted_dir'
        dotted_dir.mkdir()

        pattern_one = str(path / file_one.name)
        pattern_two = str(path / 'dir_*')
        pattern_three = str(path / '*.glob_*')
        pattern_four = str(path / '.dotted_dir')


# Generated at 2022-06-13 20:55:31.430960
# Unit test for function path_absent
def test_path_absent():
    import tempfile
    tmp_dir = tempfile.TemporaryDirectory()
    tmp_path = Path(tmp_dir.name)
    test_dir: Path = tmp_path / 'test_dir'
    test_dir.mkdir()
    test_file: Path = test_dir / 'test_file'
    test_file.touch()
    test_link: Path = test_dir / 'test_link'
    test_link.symlink_to(test_file)
    path_absent(test_dir)
    assert not os.path.exists(test_dir.as_posix())
    tmp_dir.cleanup()



# Generated at 2022-06-13 20:55:37.844190
# Unit test for function chown
def test_chown():
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        fh, path = tempfile.mkstemp(dir=tmpdir)
        os.close(fh)

        chown(os.path.join(tmpdir, '*'), user=os.getuid(), group=os.getgid())

# Generated at 2022-06-13 20:55:55.700291
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:55:59.318596
# Unit test for function chmod
def test_chmod():
    """Unit test for function ``chmod``.

    Returns:
        :obj:`None`

    """

    import doctest

    doctest.testmod(sys.modules[__name__])



# Generated at 2022-06-13 20:56:06.517042
# Unit test for function chown
def test_chown():
    import tempfile
    from flutils.pathutils import chown

    if sys.platform.startswith('win'):
        pass

    else:
        with tempfile.TemporaryDirectory() as tempdir:
            path = Path(tempdir, 'test.txt')
            path.touch()

            chown(path, user=getpass.getuser(), group=getpass.getuser())



# Generated at 2022-06-13 20:56:17.416484
# Unit test for function chown
def test_chown():
    from .test import _tmp_dir
    from .test import *
    from .pathutils import *

    tmp_dir = _tmp_dir()
    put_file(
        'foo.txt',
        '',
        tmp_dir,
        mode_file=0o600,
        mode_dir=0o700
    )
    chown('{}/foo.txt'.format(tmp_dir))
    # Change ownership (with pattern)
    chown('{}/**'.format(tmp_dir), user='root', group='wheel')
    # Change ownership (without pattern)
    chown('{}/foo.txt'.format(tmp_dir), user='root', group='wheel')
    # Change ownership (without pattern, but with use of '-1')

# Generated at 2022-06-13 20:56:26.837652
# Unit test for function exists_as
def test_exists_as():
    from flutils.testing import capture_output

    path = tmpdir / 'exists_as'
    path.mkdir()
    assert exists_as(path) == 'directory'

    path = tmpdir / 'exists_as.txt'
    path.touch()
    assert exists_as(path) == 'file'

    def test_exists_as_mkfifo():
        path = tmpdir / 'exists_as.fifo'
        path.mkfifo()
        assert exists_as(path) == 'FIFO'

    if not is_windows():
        test_exists_as_mkfifo()

    def test_exists_as_socket():
        path = tmpdir / 'exists_as.socket'
        path.mkfifo()

# Generated at 2022-06-13 20:56:36.935819
# Unit test for function exists_as
def test_exists_as():
    import tempfile

    path = Path(tempfile.mkdtemp())

    # This tests against a directory.
    assert exists_as(path) == 'directory'

    # Create a file
    path.joinpath('test.txt').write_text('test')

    # Test against a file.
    assert exists_as(path.joinpath('test.txt')) == 'file'

    # Test against a broken symlink.
    # This should return an empty string.
    assert exists_as(path.joinpath('test.txt.link')) == ''

    # Create a symlink to the test file
    symlink_path = path.joinpath('test.txt.link')
    symlink_path.symlink_to(path.joinpath('test.txt'))

    # Test against a symlink
   

# Generated at 2022-06-13 20:56:49.910483
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    from flutils.tests import (
        TEST_DIRECTORY,
        TEST_DIRECTORY_PATH,
    )
    from pathlib import Path

    # Setup
    TEST_DIRECTORY_READ_PATH = Path(TEST_DIRECTORY) / 'read'
    TEST_DIRECTORY_READ_PATH.mkdir(mode=0o700, parents=True, exist_ok=True)

    TEST_DIRECTORY_READ_WRITE_PATH = Path(TEST_DIRECTORY) / 'read-write'
    TEST_DIRECTORY_READ_WRITE_PATH.mkdir(mode=0o700, parents=True, exist_ok=True)

    TEST_FILE_READ_PATH = TEST_DIRECTORY_READ_PATH / 'file.txt'
    TEST

# Generated at 2022-06-13 20:56:57.127593
# Unit test for function chown
def test_chown():
    import pytest
    from flutils.pathutils import chown

    with pytest.raises(OSError):
        chown('~/tmp/flutils.tests.osutils.txt', user='missing_user')

    with pytest.raises(OSError):
        chown('~/tmp/flutils.tests.osutils.txt', group='missing_group')

    with pytest.raises(TypeError):
        chown(('a', 'b', 'c'))



# Generated at 2022-06-13 20:56:57.904534
# Unit test for function chown
def test_chown():
    assert True



# Generated at 2022-06-13 20:57:09.595859
# Unit test for function exists_as
def test_exists_as():
    """Test the exists_as() function."""
    import tempfile
    import shutil

    tmp_dir = tempfile.mkdtemp()

    path1 = os.path.join(tmp_dir, 'test_file1.txt')
    path2 = os.path.join(tmp_dir, 'test_file2.txt')
    path3 = os.path.join(tmp_dir, 'test_file3.txt')

    touch(path1, create_new=True)
    touch(path2, create_new=True)
    os.symlink(path1, path3)

    assert exists_as(path1) == 'file'
    assert exists_as(path2) == 'file'
    assert exists_as(path3) == 'file'


# Generated at 2022-06-13 20:57:33.019357
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:57:43.644022
# Unit test for function chmod
def test_chmod():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from pyfakefs.fake_filesystem_unittest import Patcher

    with Patcher() as patcher:
        # Create a temporary directory and
        # set the fake filesystem to it
        with TemporaryDirectory() as tmpdirname:
            tmpdir = Path(tmpdirname)
            patcher.fs.root = tmpdir.as_posix()

            # Make a directory and file
            tmpdir.joinpath('bar').mkdir()
            tmpdir.joinpath('foo.txt').touch()

            # Directory starts with mode 0o755
            assert tmpdir.joinpath('bar').stat().st_mode & 0o777 == 0o755

            # File starts with mode 0o644
            assert tmpdir.joinpath('foo.txt').stat().st_mode & 0o777

# Generated at 2022-06-13 20:57:53.899095
# Unit test for function chmod
def test_chmod():
    import tempfile

    test_path = tempfile.mkdtemp()
    test_file = Path(test_path, 'test_file.txt')
    test_file.touch()

    chmod(test_file, 0o644)
    os.chmod(test_file, 0o644)
    chmod(test_path, mode_file=0o600, mode_dir=0o700)

    if os.name != 'nt':
        import pwd
        import grp

        users_group = 'users'
        users_gid = 0
        for group in grp.getgrall():
            if group.gr_name == 'users':
                users_gid = group.gr_gid
                break

        path_owner = ''

# Generated at 2022-06-13 20:58:07.122193
# Unit test for function chmod
def test_chmod():
    from tempfile import TemporaryDirectory
    from flutils.pathutils import chmod

    path = None
    with TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / 'test_chmod.txt'
        path.touch()

        chmod(path, 0o600)
        assert path.stat().st_mode == 0o100600
        path.chmod(0o644)

        chmod(path, mode_dir=0o777)
        assert path.stat().st_mode == 0o100644

        chmod(path, 0o600, 0o777)
        assert path.stat().st_mode == 0o100600

        chmod(path.as_posix(), 0o600)
        assert path.stat().st_mode == 0o100600

        chmod(path, 0o600)

# Generated at 2022-06-13 20:58:07.750379
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:58:17.568425
# Unit test for function exists_as
def test_exists_as():
    """Run unit test for flutils.pathutils.exists_as()."""
    path = tempfile.mkdtemp()
    assert exists_as(path) == 'directory'

    path = tempfile.mktemp()
    open(path, 'w').close()
    assert exists_as(path) == 'file'

    path = tempfile.mktemp()
    if os.name == 'nt':
        # Windows (nt) does not have os.mknod
        assert exists_as(path) == ''
    else:
        os.mknod(path, 0o600 | stat.S_IFBLK)
        assert exists_as(path) == 'block device'

    path = tempfile.mktemp()
    os.mknod(path, 0o600 | stat.S_IFCHR)
    assert exists_

# Generated at 2022-06-13 20:58:28.745248
# Unit test for function exists_as
def test_exists_as():
    """Test the exists_as function."""
    from pathlib import Path
    from shutil import rmtree

    from flutils.pathutils import exists_as

    test_path = Path('/tmp/test_path')
    try:
        # Already exists as a symlink.
        assert exists_as(test_path) == ''

        test_path.symlink_to('/tmp/')
        assert exists_as(test_path) == 'directory'

        test_path.unlink()

        # Non existent
        assert exists_as(test_path) == ''

        test_path.mkdir()
        assert exists_as(test_path) == 'directory'

    finally:
        if test_path.exists():
            test_path.rmdir()
            assert exists_as(test_path)

# Generated at 2022-06-13 20:58:36.127225
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/bin') == 'directory'
    assert exists_as('/bin/bash') == 'file'
    assert exists_as('/dev') == 'directory'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/dev/sda1') == 'block device'
    assert exists_as('/dev/sda2') == 'block device'
    assert exists_as('/dev/sda3') == 'block device'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/urandom') == 'char device'

# Generated at 2022-06-13 20:58:43.711654
# Unit test for function chown
def test_chown():
    user = getpass.getuser()
    group = grp.getgrgid(os.getgid()).gr_name
    _path = normalize_path('/tmp/foo.txt')
    try:
        chown(_path, user, group)
        uid = get_os_user(user).pw_uid
        gid = get_os_group(group).gr_gid
        assert os.stat(_path.as_posix()).st_uid == uid
        assert os.stat(_path.as_posix()).st_gid == gid
    finally:
        _path.unlink()



# Generated at 2022-06-13 20:58:47.387207
# Unit test for function chown
def test_chown():
    chown('~/tmp/flutils.tests.osutils.txt')
    chown('~/tmp/**', user='foo', group='bar')
    chown('~/tmp/flutils.tests.osutils.txt', include_parent=True)



# Generated at 2022-06-13 20:59:14.630551
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('') == ''
    assert exists_as(Path().cwd()) == 'directory'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/dev/full') == 'char device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/dev/stdin') == 'char device'
    assert exists_as('/dev/stdout') == 'char device'
    assert exists_as('/dev/stderr') == 'char device'

# Generated at 2022-06-13 20:59:26.797343
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import tmpdir
    from flutils.osutils import rm_rf
    from pathlib import Path

    def _chmod(path: Path, mode: int) -> None:
        from stat import S_IWUSR, S_IRUSR, S_IWGRP, S_IRGRP
        from os import chmod

        if mode not in (0, 2):
            raise ValueError(
                'Unknown mode value: %r' % mode
            )
        if mode == 0:
            chmod(str(path), S_IRUSR | S_IRGRP)
        else:
            chmod(str(path), S_IRUSR | S_IRGRP | S_IWUSR | S_IWGRP)


# Generated at 2022-06-13 20:59:33.013691
# Unit test for function directory_present
def test_directory_present():
    assert (
        directory_present(
            '~/tmp/flutils.tests.osutils/test_directory_present'
        )
        ==
        normalize_path(
            '~/tmp/flutils.tests.osutils/test_directory_present'
        )
    )



# Generated at 2022-06-13 20:59:43.371231
# Unit test for function directory_present
def test_directory_present():
    from shutil import rmtree
    from tempfile import mkdtemp
    from unittest import TestCase

    from flutils.pathutils import directory_present


# Generated at 2022-06-13 20:59:56.898611
# Unit test for function chown
def test_chown():
    from os import getuid
    from os import getgid
    from os import path
    from os import stat
    from shutil import rmtree
    from tempfile import mkdtemp
    from flutils.pathutils import chown
    from flutils.pathutils import get_os_user
    from flutils.pathutils import get_os_group

    orig_uid, orig_gid = getuid(), getgid()
    target_dir = mkdtemp()

    # Test a basic file change
    with open(path.join(target_dir, 'file.txt'), 'w') as fd:
        fd.write('foo')

    file_stats = stat(path.join(target_dir, 'file.txt'))

    # The login name of the current user
    user = get_os_user().pw_name

# Generated at 2022-06-13 21:00:08.055108
# Unit test for function get_os_user
def test_get_os_user():
    from flutils.pathutils import get_os_user
    user = get_os_user()
    assert isinstance(user, pwd.struct_passwd)
    assert isinstance(user.pw_name, str)
    assert isinstance(user.pw_passwd, str)
    assert isinstance(user.pw_uid, int)
    assert isinstance(user.pw_gid, int)
    assert isinstance(user.pw_gecos, str)
    assert isinstance(user.pw_dir, str)
    assert isinstance(user.pw_shell, str)
    assert user.pw_name == getpass.getuser()

    # The below if statement is to resolve an issue on macOS.  If a user has
    # the UNIX ``id`` of 501 and then that user is

# Generated at 2022-06-13 21:00:12.645787
# Unit test for function path_absent
def test_path_absent():
    path_absent('~/tmp/test_path')

if __name__ == '__main__':
    test_path_absent()

# Generated at 2022-06-13 21:00:15.434965
# Unit test for function chmod
def test_chmod():
    # Ensure normalize_path() is tested
    from flutils.pathutils import normalize_path
    normalize_path('/tmp/')
    assert True



# Generated at 2022-06-13 21:00:24.281711
# Unit test for function chown
def test_chown():
    path = Path('~/tmp/flutils.tests.osutils.txt')
    chown(path)

    assert path.exists() is True
    assert os.stat(path.as_posix()).st_uid == getpass.getuser()
    assert (os.stat(path.as_posix()).st_gid == getpass.getuser())

    path = Path('~/tmp/flutils.tests.osutils.txt')
    chown(path, user='-1', group='-1')

    assert path.exists() is True
    assert os.stat(path.as_posix()).st_uid == getpass.getuser()
    assert os.stat(path.as_posix()).st_gid == getpass.getuser()


# Generated at 2022-06-13 21:00:36.830874
# Unit test for function chown
def test_chown():
    with pytest.raises(TypeError):
        chown(123)
        
    with pytest.raises(TypeError):
        assert chown('/tmp/flutils.tests.pathutils.txt', None)
        
    with pytest.raises(TypeError):
        assert chown('/tmp/flutils.tests.pathutils.txt', user=123)
        
    with pytest.raises(TypeError):
        assert chown('/tmp/flutils.tests.pathutils.txt', group=123)
        
    with pytest.raises(TypeError):
        assert chown('/tmp/flutils.tests.pathutils.txt', include_parent=123)
        

# Generated at 2022-06-13 21:00:50.085277
# Unit test for function path_absent
def test_path_absent():
    pass

# Generated at 2022-06-13 21:00:52.197899
# Unit test for function chmod
def test_chmod():
    """Test the ``chmod`` function."""
    # TODO
    pass



# Generated at 2022-06-13 21:01:01.728671
# Unit test for function chown
def test_chown():
    """Test function 'chown'"""
    path = normalize_path('/tmp/flutils.tests.tmp')
    try:
        path.mkdir()
        chown('/tmp/flutils.tests.tmp', 'root', 'root')
        assert path.owner() == 'root'
        assert path.group() == 'root'
        chown('/tmp/flutils.tests.tmp', include_parent=True)
        assert path.owner() == getpass.getuser()
        assert path.group() == grp.getgrgid(os.getgid()).gr_name
    finally:
        path.rmdir()


# Generated at 2022-06-13 21:01:13.026969
# Unit test for function chown
def test_chown():
    path = normalize_path('~/tmp/flutils.tests.osutils.txt')
    user = getpass.getuser()
    group = grp.getgrgid(os.getgid()).gr_name
    chown(path)
    assert os.stat(path.as_posix()).st_uid == os.getuid()
    assert os.stat(path.as_posix()).st_gid == os.getgid()
    assert os.stat(path.as_posix()).st_uid == pwd.getpwnam(user).pw_uid
    assert os.stat(path.as_posix()).st_gid == grp.getgrnam(group).gr_gid
    chown(path, user='-1', group='-1')

# Generated at 2022-06-13 21:01:22.176412
# Unit test for function chown
def test_chown():
    """pytest for chown."""
    import tempfile
    from os.path import sep as SEP
    from os import makedirs

    from flutils.pathutils import (
        chown,
        normalize_path,
    )

    from flutils.posixutils import (
        get_current_uname,
        get_current_gname,
    )

    from flutils.tests.helpers import TestHelpers

    th = TestHelpers()

    tmp_path = normalize_path(tempfile.gettempdir()) / 'flutils_test'

    def teardown_module():
        try:
            th.remove_temp_folder(tmp_path)
            if tmp_path.is_dir() is True:
                tmp_path.rmdir()
        except OSError:
            pass

# Generated at 2022-06-13 21:01:27.236532
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod

    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)
    chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770)
    chmod('~/tmp/*')



# Generated at 2022-06-13 21:01:32.715240
# Unit test for function chown
def test_chown():
    with tempfile.NamedTemporaryFile() as fh:
        chown(fh.name, user='root', group='root')
        assert pathlib.Path(fh.name).owner() == 'root'
        assert pathlib.Path(fh.name).group() == 'root'



# Generated at 2022-06-13 21:01:46.902155
# Unit test for function path_absent
def test_path_absent():  # noqa: WPS501, WPS442
    """Test the path_absent function."""
    import random  # noqa: WPS433
    import string  # noqa: WPS433
    dir = '/tmp/%s' % ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(21)
    )
    os.mkdir(dir)
    assert os.path.isdir(dir)

    for _ in range(21):
        file_name = '%s/%s' % (dir, ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(21)
        ))
        with open(file_name, 'w') as fp:
            fp.write('')



# Generated at 2022-06-13 21:01:59.861400
# Unit test for function path_absent
def test_path_absent():
    """Test the flutils.pathutils.path_absent function."""
    import time
    import shutil
    import tempfile
    now = time.time()  # pylint: disable=invalid-name

    test_path = Path(tempfile.gettempdir()) / 'test_path'
    assert test_path.exists() is False

    test_path.mkdir(0o700)
    assert test_path.exists() is True
    assert test_path.is_dir()

    for i in range(1, 4):
        (test_path / 'tmp_%s' % i).mkdir(0o700)

    for i in range(1, 6):
        Path(test_path / 'tmp_%s' % i).touch(mode=0o600, exist_ok=True)
        Path

# Generated at 2022-06-13 21:02:01.157054
# Unit test for function chown
def test_chown():
    assert True == True

# Generated at 2022-06-13 21:02:25.032560
# Unit test for function path_absent
def test_path_absent():
    """Test the function path_absent().

    *New in version 0.4.*

    Example:
        >>> from flutils.pathutils import path_absent
        >>> path_absent('~/tmp/test_path')
    """
    path = normalize_path('~/tmp/test_path')
    path = path.as_posix()
    path = cast(str, path)
    if os.path.exists(path):
        if os.path.islink(path):
            os.unlink(path)
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    p = os.path.join(root, name)

# Generated at 2022-06-13 21:02:26.870204
# Unit test for function chown
def test_chown():

    assert chown('~/tmp/flutils.tests.osutils.txt', include_parent=True)



# Generated at 2022-06-13 21:02:29.052536
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:02:39.222870
# Unit test for function chown
def test_chown():
    """Test the chown() function"""
    from flutils.pathutils import chown
    import tempfile
    f = tempfile.TemporaryFile()
    chown(f.name, 'nobody', '')

    import os
    import pwd
    import grp
    print(os.stat(f.name))

    if pwd.getpwnam('nobody'):
        user = pwd.getpwnam('nobody').pw_uid
    else:
        user = pwd.getpwuid(os.getuid())[0]

    group = grp.getgrnam('').gr_gid
    print(os.stat(f.name).st_uid, user)
    print(os.stat(f.name).st_gid, group)

# Generated at 2022-06-13 21:02:40.595357
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:02:51.205216
# Unit test for function chmod
def test_chmod():
    # setup
    import os
    import shutil
    import time
    import tempfile

    tmpdir = tempfile.mkdtemp(prefix='flutils_test_pathutils_')

    TEST_FILES = {
        'a': 0o700,
        'b': 0o777,
        'c': 0o754,
        'd': 0o600,
        'e': 0o700,
    }

    # Create file
    for file_name, mode in TEST_FILES.items():
        path_ = tmpdir / file_name
        path_.open('w').close()
        os.chmod(path_.as_posix(), mode)

    # Make a directory
    path_ = tmpdir / 'subdir'
    path_.mkdir(mode=0o700)

# Generated at 2022-06-13 21:03:05.138219
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import directory_present
    from pathlib import PosixPath
    from shutil import rmtree
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp_dir:
        tmp_dir = PosixPath(tmp_dir)
        base_path = tmp_dir / 'base'
        path = base_path / 'test_path'
        assert path.exists() is False
        assert base_path.exists() is False
        directory_present(path, mode=0o711)
        assert path.exists() is True
        assert path.is_dir() is True
        assert path.stat().st_mode & 0o777 == 0o711
        assert base_path.stat().st_mode & 0o777 == 0o711

        # Ensure the parent path was chmod'd
       

# Generated at 2022-06-13 21:03:15.324683
# Unit test for function exists_as
def test_exists_as():
    import os
    assert exists_as(Path(__file__).parent) == 'directory'
    assert exists_as(Path(__file__).parent.as_posix()) == 'directory'
    assert exists_as(__file__) == 'file'
    assert exists_as(os.fspath(Path(__file__).parent)) == 'directory'
    assert exists_as(os.fspath(Path(__file__))) == 'file'
    assert exists_as(1) is None
    assert exists_as(Path()) is None
    assert exists_as(Path('~/tmp')) == ''
    assert exists_as(Path('~/tmp').as_posix()) == ''



# Generated at 2022-06-13 21:03:21.096177
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    from flutils.osutils import get_temp_directory
    from pathlib import Path
    temp_dir = get_temp_directory()
    path = Path(temp_dir).joinpath('test_exists_as')
    path.mkdir()
    assert exists_as(path) == 'directory'
    path.rmdir()
    assert exists_as(path) == ''



# Generated at 2022-06-13 21:03:23.822733
# Unit test for function chmod
def test_chmod():
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)

