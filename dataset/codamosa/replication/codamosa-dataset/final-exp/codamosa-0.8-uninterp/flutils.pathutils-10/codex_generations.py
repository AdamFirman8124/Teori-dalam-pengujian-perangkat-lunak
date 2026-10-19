

# Generated at 2022-06-13 20:54:08.711296
# Unit test for function chmod
def test_chmod(): pass



# Generated at 2022-06-13 20:54:20.901509
# Unit test for function chown
def test_chown():
    from . import pathutils

    path = '~/tmp/flutils.tests.osutils.txt'
    user = getpass.getuser()
    group = grp.getgrgid(os.getgid()).gr_name

    pathutils.chown(path, user=user, group=group)

    e_user = pwd.getpwnam(user).pw_uid
    e_group = grp.getgrnam(group).gr_gid

    assert os.stat(path).st_uid == e_user
    assert os.stat(path).st_gid == e_group

    os.remove(path)

# Generated at 2022-06-13 20:54:29.736568
# Unit test for function path_absent
def test_path_absent():
    # TODO: Add test for Windows
    test_path = Path(tempfile.gettempdir()) / 'test_path'
    test_path.mkdir(exist_ok=True)
    _test_path = Path(test_path) / 'test_path_absent.txt'
    _test_path.write_text('test')
    path_absent(test_path)
    assert test_path.exists() is False
    assert _test_path.exists() is False



# Generated at 2022-06-13 20:54:31.455105
# Unit test for function chown
def test_chown():
    chown('/tmp/foo_user', user='foo')



# Generated at 2022-06-13 20:54:32.072086
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:54:43.709628
# Unit test for function normalize_path
def test_normalize_path():
    assert normalize_path(b'/foo') == Path('/foo')
    assert normalize_path('/foo') == Path('/foo')
    assert normalize_path(Path('/foo')) == Path('/foo')
    assert normalize_path('/Foo') == Path('/Foo')
    assert normalize_path('/FOO') == Path('/FOO')
    assert normalize_path('/Foo/bar') == Path('/Foo/bar')
    assert normalize_path('/Foo//bar') == Path('/Foo/bar')
    assert normalize_path('.') == Path(os.getcwd())
    assert normalize_path('./') == Path(os.getcwd())
    assert normalize_path('./.') == Path(os.getcwd())


# Generated at 2022-06-13 20:54:44.817237
# Unit test for function chown
def test_chown():
    assert chown is not None



# Generated at 2022-06-13 20:54:55.547824
# Unit test for function exists_as
def test_exists_as():
    """Function ``exists_as()``.
    """
    from tempfile import TemporaryDirectory
    from unittest import TestCase
    import os
    import pathlib
    from flutils.pathutils import exists_as, normalize_path

    class TestExistsAs(TestCase):
        """Test ``exists_as()``."""

        def setUp(self) -> None:
            """Test pre-conditions."""
            self.tmp_path = pathlib.Path(TemporaryDirectory().name)
            os.chmod(self.tmp_path.as_posix(), 0o700)

        def test_exists_as_file(self) -> None:
            """Test a file path."""
            path = pathlib.Path(self.tmp_path) / 'test_file.txt'

# Generated at 2022-06-13 20:54:58.903689
# Unit test for function get_os_user
def test_get_os_user():
    # pylint: disable=protected-access
    u = get_os_user()
    assert get_os_user(u.pw_name) == u
    assert get_os_user(u.pw_uid) == u
    with pytest.raises(OSError):
        get_os_user(1)
        get_os_user('root')
# test_get_os_user()



# Generated at 2022-06-13 20:55:13.501701
# Unit test for function chmod
def test_chmod():
    from os import mkdir
    from os.path import isdir
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    from flutils.pathutils import chmod

    with TemporaryDirectory() as tmp_dir:
        test_path_1 = Path(tmp_dir).joinpath('test_chmod_1')
        test_path_2 = Path(tmp_dir).joinpath('test_chmod_2')
        test_path_3 = Path(tmp_dir).joinpath('test_chmod_3')
        test_glob = Path(tmp_dir).joinpath('test_*')
        location_1 = Path(tmp_dir).joinpath('location_1')
        location_2 = Path(tmp_dir).joinpath('location_2')

# Generated at 2022-06-13 20:55:48.699702
# Unit test for function find_paths
def test_find_paths():
    """Unit tests for flutils.pathutils.find_paths."""
    from flutils.pathutils import find_paths
    from flutils.pathutils import Path
    from pathlib import PosixPath

    try:
        from tempfile import TemporaryDirectory
    except ImportError:
        from backports.tempfile import TemporaryDirectory

    test_paths = [
        'tmp',
        '1.txt',
        'dir_one',
        'dir_two',
        'dir_one/1.txt',
        'dir_one/2.txt',
        'dir_two/1.txt',
        'dir_two/2.txt',
        'dir_one/dir_two/1.txt',
        'dir_one/dir_two/2.txt',
    ]

# Generated at 2022-06-13 20:55:58.236583
# Unit test for function find_paths
def test_find_paths():
    pattern = Path('/home/test_user') / 'tmp/*'
    # Validate basic functionality
    paths = list(find_paths(pattern))
    assert len(paths) == 2
    assert paths == [
        Path('/home/test_user/tmp/file_one'),
        Path('/home/test_user/tmp/dir_one')
    ]
    # Validate broken globs are ignored
    assert list(find_paths(pattern.as_posix() + '*')) == paths



# Generated at 2022-06-13 20:56:11.947570
# Unit test for function find_paths
def test_find_paths():
    # Able to find files
    assert list(find_paths('~/tmp/flutils.tests.fileutils.txt')) == [Path('~/tmp/flutils.tests.fileutils.txt')]

    # Able to find directories
    assert list(find_paths('~/tmp/flutils.tests.fileutils.txt.d')) == [Path('~/tmp/flutils.tests.fileutils.txt.d')]

    # Able to find wildcarded files
    assert list(find_paths('~/tmp/flutils.tests.*')) == [
        Path('~/tmp/flutils.tests.fileutils.txt'),
        Path('~/tmp/flutils.tests.fileutils.txt.d')
    ]

    # Able to find wildcarded directories

# Generated at 2022-06-13 20:56:23.400313
# Unit test for function chmod
def test_chmod():
    """Unit tests for :func:`~flutils.osutils.chmod`."""

    from flutils.pathutils import normalize_path

    from .testutils import (
        TEST_TMPDIR,
        TEST_TMPDIR_TEXT,
    )

    from unittest.mock import (
        patch,
    )

    import os
    import stat

    def _get_mode(path):
        return os.stat(str(path)).st_mode & 0o777

    # Test simple file change
    test_file = normalize_path(TEST_TMPDIR_TEXT)
    test_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.touch()

    test_file.chmod(0o700)

# Generated at 2022-06-13 20:56:24.404336
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:56:25.540944
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(__file__) == 'file'



# Generated at 2022-06-13 20:56:36.272885
# Unit test for function path_absent
def test_path_absent():
    """Path absent unittest."""
    import turtle
    import tempfile
    tempdir = tempfile.TemporaryDirectory()
    tempdir.cleanup()
    path = os.path.join(tempdir.name, 'foo/bar')
    path_absent(path)
    assert not os.path.exists(path)
    with open(path, 'w') as f:
        f.write('foo')
    path_absent(path)
    assert not os.path.exists(path)
    path = normalize_path(path)
    with open(path, 'w') as f:
        f.write('bar')
    path_absent(path)
    assert not os.path.exists(path)
    path = normalize_path(path)
    os.mkdir(path)
   

# Generated at 2022-06-13 20:56:49.619049
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod, exists_as

    tmp_dir = '/tmp/flutils.pathutils.test_chmod'
    tmp_file = f'{tmp_dir}/flutils.tests.osutils.txt'

    chmod(tmp_dir, mode_file=0o700)
    assert exists_as(tmp_dir, type='dir') is True

    chmod(tmp_file, mode_file=0o660)
    assert exists_as(tmp_file, type='file') is True

    chmod(f'{tmp_dir}/*', mode_dir=0o755)
    assert exists_as(tmp_dir, type='dir') is True

    chmod(f'{tmp_dir}/*', mode_dir=0o770)

# Generated at 2022-06-13 20:56:51.528871
# Unit test for function get_os_user
def test_get_os_user():
    assert get_os_user('root') == pwd.getpwnam('root')



# Generated at 2022-06-13 20:57:03.440243
# Unit test for function chown
def test_chown():
    from shutil import rmtree

    from pathlib import Path

    from flutils.pathutils import chown

    from . import (
        TEST_DIR_BASE,
        TEST_DIR_EXTRA,
        TEST_FILES,
        TEST_RECURSIVE_PATH,
        TEST_SUBDIR_BASE,
        safe_rmtree,
    )

    root_path = Path(TEST_DIR_BASE)
    subdir_path = Path(TEST_SUBDIR_BASE)
    recursive_path = Path(TEST_RECURSIVE_PATH)
    test_files = (Path(TEST_DIR_BASE) / TEST_FILES[0],
                  Path(TEST_DIR_BASE) / TEST_FILES[1],)


# Generated at 2022-06-13 20:57:29.320373
# Unit test for function exists_as
def test_exists_as():
    path = normalize_path('~/tmp/flutils.tests.osutils.txt')
    path.touch()
    assert exists_as(path) == 'file'
    path.unlink()
    assert exists_as(path) == ''



# Generated at 2022-06-13 20:57:30.922137
# Unit test for function chmod
def test_chmod():
    print()
    return None
# Test runner for function chmod

# Generated at 2022-06-13 20:57:38.939429
# Unit test for function chmod
def test_chmod():
    os.mkdir('~/tmp')
    with open('~/tmp/flutils.tests.osutils.txt', 'w') as f:
        f.write('Hola!')
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)
    os.remove('~/tmp/flutils.tests.osutils.txt')
    os.rmdir('~/tmp/')



# Generated at 2022-06-13 20:57:50.583853
# Unit test for function path_absent
def test_path_absent():
    """Test function path_absent."""
    with TemporaryDirectory() as tmpdir_path:
        tmpdir_path = Path(tmpdir_path)
        file_one = tmpdir_path.joinpath('file_one')
        file_one.touch()
        file_one.write_text('foo')
        dir_one = tmpdir_path.joinpath('dir_one')
        dir_one.mkdir(mode=0o700)
        file_two = dir_one.joinpath('file_two')
        file_two.touch()
        file_two.write_text('bar')

        path_absent(tmpdir_path)

        assert not file_two.exists()
        assert not file_one.exists()
        assert not dir_one.exists()
        assert not tmpdir_path.ex

# Generated at 2022-06-13 20:58:01.752476
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/tmp/') == 'directory'
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/tmp/../tmp/') == 'directory'
    assert exists_as('/tmp/../tmp') == 'directory'

    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/etc/hosts/') == 'file'
    assert exists_as('/etc/hosts/../hosts') == 'file'

    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/urandom/') == 'char device'
    assert exists_as('/dev/urandom/../urandom') == 'char device'

    assert exists_as('/dev/sda1') == 'block device'
   

# Generated at 2022-06-13 20:58:13.346918
# Unit test for function chmod
def test_chmod():
    """Unit test for module function chmod."""

    # Creating some test files to work with
    path = Path('tmp_dir')
    path.mkdir(0o777, exist_ok=True)
    file1 = path / 'file1.txt'
    file1.touch()
    file1_child = path / 'file1_child.txt'
    file1_child.touch()
    file2 = path / 'file2.txt'
    file2.touch()


# Generated at 2022-06-13 20:58:26.849609
# Unit test for function directory_present
def test_directory_present():
    """Test the directory_present function."""
    from flutils.pathutils import directory_present
    from flutils.testing import (
        get_temp_directory,
        remove_temp_directory,
    )

    from pathlib import PosixPath
    from sys import version_info

    current_user = getpass.getuser()

    # Test that it is not supported for glob pattern paths.
    # TODO:  Flush out other test cases.
    with get_temp_directory() as tmp_dir:
        try:
            directory_present((tmp_dir / '*'))
        except ValueError as e:
            assert 'The path: %r must NOT contain any glob patterns.' \
                % (tmp_dir / '*').as_posix() == str(e)

# Generated at 2022-06-13 20:58:41.576091
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod

    chmod('flutils.tests.osutils.txt', 0o644)
    assert oct(os.stat('flutils.tests.osutils.txt').st_mode)[-3:] == '644'
    os.unlink('flutils.tests.osutils.txt')


# Generated at 2022-06-13 20:58:43.738865
# Unit test for function exists_as
def test_exists_as():
    test_path = Path(__file__).parent.as_posix()
    assert exists_as(test_path) == 'directory'
    assert exists_as(test_path + '/doesnotexist') == ''


# Generated at 2022-06-13 20:58:55.757656
# Unit test for function chown
def test_chown():
    p = Path('/tmp/foo')
    if p.exists() is True:
        p.unlink()
    try:
        p.mkdir(0o700, parents=True)
        chown(p, user='-1', group='-1', include_parent=True)
        stats = Path('/tmp').stat()
        assert stats.st_uid == os.getuid()
        assert stats.st_gid == os.getgid()
        stats = p.stat()
        assert stats.st_uid == os.getuid()
        assert stats.st_gid == os.getgid()
    finally:
        if p.exists() is True:
            p.unlink()



# Generated at 2022-06-13 20:59:16.553121
# Unit test for function chmod
def test_chmod():
    import os
    file1 = '~/tmp/flutils.tests.osutils.txt'
    file2 = '~/tmp/flutils.tests.osutils2.txt'
    if os.path.isfile(file1):
        os.remove(file1)

    if os.path.isfile(file2):
        os.remove(file2)

    assert not os.path.isfile(file1)
    assert not os.path.isfile(file2)

    open(file1, 'a').close()
    open(file2, 'a').close()
    
    assert os.path.isfile(file1)
    assert os.path.isfile(file2)

    chmod(file1, mode_file=0o600)

# Generated at 2022-06-13 20:59:22.398815
# Unit test for function exists_as
def test_exists_as():
    """Unit test for function `flutils.pathutils.exists_as`."""
    from pathlib import Path
    from tempfile import TemporaryDirectory
    import unittest

    from flutils.pathutils import get_os_user, exists_as

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    class TestExistsAs(unittest.TestCase):
        def setUp(self):
            self.user = str(get_os_user())
            self.td = TemporaryDirectory(prefix='flutils.tests.pathutils.')
            self.path = Path(self.td.name)

        def tearDown(self):
            self.td.cleanup()
            self.path = None


# Generated at 2022-06-13 20:59:31.222137
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import normalize_path
    from flutils.pathutils import exists_as
    from os import makedirs
    from os.path import abspath
    from os.path import dirname
    from os.path import join
    from os.path import realpath
    from tempfile import gettempdir
    from unittest import TestCase

    from pathlib import Path

    class Test_exists_as(TestCase):
        def tearDown(self):
            '''Cleanup after the test functions have completed.'''
            if Path().home().exists():
                Path().home().rmdir()
            test_path.rmdir()

        def test_with_pathlib(self):
            path = Path(test_path)
            self.assertEqual(exists_as(path), 'directory')

       

# Generated at 2022-06-13 20:59:34.028760
# Unit test for function chmod
def test_chmod():
    """Unit tests for flutils.pathutils.chmod."""

    assert callable(chmod)

    assert True is True

# Generated at 2022-06-13 20:59:46.065003
# Unit test for function chown
def test_chown():
    """Test function chown."""
    import shutil
    import tempfile
    from os.path import isdir
    from flutils.pathutils import chown
    from flutils.osutils import get_group_name, get_user_name
    # test the chown creation and deletion

# Generated at 2022-06-13 20:59:59.343892
# Unit test for function chown
def test_chown():
    from .pathutils import _temp_dir

    with _temp_dir() as td:
        td = Path(td)
        text_file = td / 'text_file'
        text_file.touch()
        (td / 'text_file2').touch()

        # test with just a file
        chown(text_file, '-1')
        chown(text_file, user='-1')
        chown(text_file, group='-1')
        usr = getpass.getuser()
        group = grp.getgrgid(pwd.getpwnam(usr).pw_gid).gr_name
        chown(text_file)
        assert text_file.owner() == usr
        assert text_file.group() == group

        chown(text_file, 'nobody')

# Generated at 2022-06-13 21:00:09.091976
# Unit test for function directory_present
def test_directory_present():
    this_test_name = sys._getframe().f_code.co_name
    path = Path().cwd().joinpath('test_tmp', this_test_name)
    if path.exists() is True:
        rmtree(str(path))

    try:
        Path().mkdir(path)
    except OSError:
        # Don't care if this fails.
        # If the path exists we will handle it in the next
        # block of code.
        pass

    path = directory_present(path)

    assert path.exists() is True
    assert path.is_file() is False
    assert path.is_symlink() is False

    path = path.joinpath('sub_path', 'sub_sub')
    assert path.exists() is False

    path = directory_present(path)

# Generated at 2022-06-13 21:00:10.500584
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:00:15.873211
# Unit test for function path_absent
def test_path_absent():
    path = Path('~/tmp/test_path').expanduser()
    path.rmdir()
    path_absent(path)
    assert path.exists() is False, 'Missing unit tests for function'



# Generated at 2022-06-13 21:00:26.757730
# Unit test for function chown
def test_chown():
    """Tests for flutils.pathutils.chown"""
    from tempfile import TemporaryDirectory

    tmpdir = None

# Generated at 2022-06-13 21:00:58.823190
# Unit test for function chmod
def test_chmod():
    import os
    import glob
    import stat
    from flutils.pathutils import chmod
    from flutils.pathutils import directory_present

    chmod('~/tmp', mode_dir=0o755, mode_file=0o644)

    directory_present(
        '~/tmp',
        owner='joe.smith',
        group='staff',
        mode_dir=0o755,
        mode_file=0o644,
        mode_file_executable=0o770,
    )

    directory_present(
        '~/tmp',
        owner=1000,
        group=1001,
        mode_dir=0o755,
        mode_file=0o644,
        mode_file_executable=0o770,
    )

    # Test with Path class

# Generated at 2022-06-13 21:01:04.269121
# Unit test for function chown
def test_chown():
    chown('~/tmp/flutils.tests.osutils.txt')
    chown('~/tmp/**')
    chown('~/tmp/*', user='foo', group='bar')
# get_os_group

# Generated at 2022-06-13 21:01:13.706381
# Unit test for function chmod
def test_chmod():
    from tempfile import (
        gettempdir,
        mkdtemp,
        mkstemp,
    )
    from os import (
        listdir,
        lstat,
        stat,
    )

    tmp_dir = gettempdir()
    tpl_dir = mkdtemp()
    tpl_dst_dir = Path(tpl_dir).joinpath('dst')
    tpl_src_dir = Path(tpl_dir).joinpath('src')
    tpl_dst_dir.mkdir()
    tpl_src_dir.mkdir()

    tpl_file = Path(mkstemp()[1])
    tpl_dst_dir.joinpath(tpl_file.name).touch()
    tpl_src_dir.joinpath(tpl_file.name).touch()

# Generated at 2022-06-13 21:01:27.520116
# Unit test for function chown
def test_chown():
    # Create the necessary local test paths
    temp_path = Path(os.path.dirname(__file__)) / 'tmp'
    temp_path.mkdir(mode=0o700, parents=True, exist_ok=True)
    parent_dir = temp_path / 'test_chown'
    grandchild_dir_1 = parent_dir / 'child_dir_1' / 'grandchild_dir_1'
    grandchild_dir_2 = parent_dir / 'child_dir_1' / 'grandchild_dir_2'
    grandchild_dir_3 = parent_dir / 'child_dir_2' / 'grandchild_dir_1'
    grandchild_dir_4 = parent_dir / 'child_dir_2' / 'grandchild_dir_2'

    # Create the directories
    # Using mk

# Generated at 2022-06-13 21:01:38.635685
# Unit test for function chown
def test_chown():
    import os
    import os.path as path
    import shutil
    import tempfile

    from flutils.pathutils import chown

    tempdir = tempfile.mkdtemp()


# Generated at 2022-06-13 21:01:48.890148
# Unit test for function chown
def test_chown():

    from stat import S_IRWXU

    from flutils.tests.helpers import generate_file
    from flutils.tests.helpers import mkdir_and_chdir

    from flutils.pathutils import chown
    from flutils.pathutils import get_os_user
    from flutils.pathutils import get_os_group
    from flutils.pathutils import normalize_path

    with mkdir_and_chdir('~/tmp/flutils.tests.osutils.chown') as old_dir:

        # Test when user and group None
        with generate_file('~/tmp/flutils.tests.osutils.chown/test.txt') as path:
            assert normalize_path(path).stat().st_uid == get_os_user().pw_uid

# Generated at 2022-06-13 21:01:57.010112
# Unit test for function exists_as
def test_exists_as():
    TEST_PATH = '~/tmp/test/test_exists_as'
    try:
        directory_present(TEST_PATH)
        assert exists_as(TEST_PATH) == 'directory'
        test_file = Path().joinpath(TEST_PATH, 'test_file.txt')
        test_file.touch()
        assert exists_as(test_file) == 'file'
    finally:
        Path().rmdir(TEST_PATH, parents=True)


# Generated at 2022-06-13 21:02:03.436343
# Unit test for function chown
def test_chown():
    os.chown('test_file', -1, -1)
    os.chown('test_file', get_os_user('bar').pw_uid,
             get_os_group('baz').gr_gid)
    os.chown('test_file', -1, -1)



# Generated at 2022-06-13 21:02:14.054223
# Unit test for function chown
def test_chown():
    path = Path(__file__).parent.joinpath('test_chown.txt')
    with open(path, 'w') as f:
        f.write('test_chown')

    # chown twice
    chown(path, user=getpass.getuser(), group=grp.getgrgid(os.getgid()).gr_name)
    chown(path, user=getpass.getuser(), group=grp.getgrgid(os.getgid()).gr_name)

    # chown a glob pattern
    chown(path.parent.joinpath('*.txt'), user=getpass.getuser(), group=grp.getgrgid(os.getgid()).gr_name)


# Generated at 2022-06-13 21:02:20.237565
# Unit test for function path_absent
def test_path_absent():
    cwd = os.getcwd()
    test_path = os.path.join(cwd, 'tmp', 'test_path')
    path_present(test_path)

    path_absent(test_path)
    assert exists_as(test_path) == ''



# Generated at 2022-06-13 21:02:45.963764
# Unit test for function path_absent
def test_path_absent():
    test_path = '/tmp/flutils_test_path_absent'
    test_file = os.path.join(test_path, 'test_file.txt')
    test_dir = os.path.join(test_path, 'test_dir')
    os.mkdir(test_path)
    with open(test_file, 'w') as f:
        f.write('Hello World')
    os.mkdir(test_dir)
    path_absent(test_path)
    assert not os.path.exists(test_path)
    assert not os.path.exists(test_file)
    assert not os.path.exists(test_dir)



# Generated at 2022-06-13 21:02:54.513299
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import path_absent
    from flutils.testingutils import temp_directory
    with temp_directory() as tmp_dir:
        dir_path = tmp_dir / 'tmp' / 'some' / 'path'

        assert path_absent(dir_path) is True

        ret_dir = directory_present(
            dir_path, mode=0o700, user='root', group='wheel'
        )
        assert ret_dir.as_posix() == dir_path.as_posix()
        assert path_absent(dir_path) is False

        # Test that trying to create a path if the parent does not exist
        # will raise an exception.

        # Note that we are using str instead of PosixPath to create the
        # path as a string that is invalid on a POSIX system.  This

# Generated at 2022-06-13 21:02:57.028768
# Unit test for function chown
def test_chown():
    assert chown('/Users/foo/tmp/flutils.tests.osutils.txt') == None

# Generated at 2022-06-13 21:03:06.903503
# Unit test for function directory_present
def test_directory_present():
    from tempfile import TemporaryDirectory
    t_dir = TemporaryDirectory()
    t_path = t_dir.__enter__()
    n_path = normalize_path(t_path)
    r_path = directory_present(n_path)
    assert isinstance(r_path, (PosixPath, WindowsPath))
    assert r_path.as_posix() == n_path.as_posix()
    assert r_path.exists() is True
    assert r_path.is_dir() is True
    t_dir.__exit__(None, None, None)
test_directory_present()



# Generated at 2022-06-13 21:03:16.380344
# Unit test for function path_absent
def test_path_absent():
    tmp_path = Path(normalize_path('~/tmp'))
    assert exists_as(tmp_path) == 'directory'
    test_path = Path(tmp_path, 'test_path')
    test_path.touch()
    assert exists_as(test_path) == 'file'
    path_absent(test_path)
    assert exists_as(test_path) == ''
    assert exists_as(tmp_path) == 'directory'
    test_path.mkdir()
    assert exists_as(test_path) == 'directory'
    path_absent(test_path)
    assert exists_as(test_path) == ''



# Generated at 2022-06-13 21:03:20.183982
# Unit test for function chown
def test_chown():
    """Unit test for function chown."""
    chown('~/tmp/osutils.txt', user='foo', group='bar')
    assert True



# Generated at 2022-06-13 21:03:28.735141
# Unit test for function exists_as
def test_exists_as():
    # create the temp file
    p = Path('~/tmp/flutils.tests.pathutils.txt').expanduser()
    p.write_text('\n', encoding='ascii')

    assert exists_as(p) == 'file'
    assert exists_as(Path(p.as_posix() + '_BAD')) == ''

    # remove the temp file
    p.unlink()



# Generated at 2022-06-13 21:03:37.712039
# Unit test for function exists_as
def test_exists_as():
    pytest.importorskip('pathlib')
    existing = directory_present('/tmp/flutils/osutils')
    assert exists_as(existing) == 'directory'
    assert exists_as('/tmp/flutils/osutils/test.txt') == 'file'
    assert exists_as('/tmp/flutils/osutils/test') == ''
    assert exists_as('/tmp/flutils/osutils/test_dir') == ''

