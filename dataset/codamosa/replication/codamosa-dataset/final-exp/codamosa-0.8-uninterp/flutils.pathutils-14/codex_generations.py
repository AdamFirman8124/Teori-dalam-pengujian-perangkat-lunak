

# Generated at 2022-06-13 20:54:30.610107
# Unit test for function chown
def test_chown():
    import os

    def _test(path, user=None, group=None, include_parent=False):
        try:
            chown(path, user=user, group=group, include_parent=include_parent)
        except OSError:
            pass
        else:
            return True

        path = normalize_path(path)
        if '*' in path.as_posix():
            path = path.parent
        else:
            return os.path.exists(path) is False

        parent = path.parent
        if parent.is_dir() is True:
            return True
        else:
            return False

    assert _test('/root/tmp') is False
    assert _test('~/tmp/flutils.tests.osutils.txt', user='-1') is False

# Generated at 2022-06-13 20:54:32.820462
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('/dev/null') == 'char device'



# Generated at 2022-06-13 20:54:43.820808
# Unit test for function path_absent
def test_path_absent():
    path = os.path.join(
        cast(str, os.getcwd()),
        'tmp',
        'my_file'
    )
    path_dir = os.path.join(
        cast(str, os.getcwd()),
        'tmp',
        'my_dir'
    )
    path_sub_dir = os.path.join(
        cast(str, os.getcwd()),
        'tmp',
        'my_dir',
        'sub_dir'
    )

    # Test simple file deletion
    with open(path, "w") as fd:
        fd.write('foo')
    path_absent(path)
    if os.path.exists(path):
        raise RuntimeError('%s was not deleted.' % path)

    # Test that a nonexistent

# Generated at 2022-06-13 20:54:45.771127
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    assert exists_as(__file__) == 'file'



# Generated at 2022-06-13 20:54:49.743306
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as(Path(os.path.dirname(__file__)) / 'test.txt') == "file"



# Generated at 2022-06-13 20:54:55.478121
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import directory_present
    assert directory_present('/tmp/flutils_test_directory_present/')
    assert directory_present('/tmp/flutils_test_directory_present/child/')
    assert directory_present('/tmp/flutils_test_directory_present/child/grand_child/')
    assert directory_present('/tmp/flutils_test_directory_present/child/grand_child/great_grand_child/')


# Generated at 2022-06-13 20:55:04.452752
# Unit test for function exists_as
def test_exists_as():
    """Unit test for function exists_as
    """
    import os
    import tempfile
    from flutils.pathutils import exists_as, normalize_path, temporary_directory

    dir_path = normalize_path(tempfile.mkdtemp())

    with temporary_directory(dir=dir_path) as dir_path:
        assert exists_as(dir_path) == 'directory'
        assert exists_as(os.path.join(dir_path, 'foo')) == ''

    with open(os.path.join(dir_path, 'bar'), 'w') as f:
        f.write('some content')

    with open(os.path.join(dir_path, 'bar')) as f:
        assert exists_as(f.name) == 'file'



# Generated at 2022-06-13 20:55:05.791245
# Unit test for function directory_present
def test_directory_present():
    directory_present('~/tmp/flutils.tests.pathutils/')

# Generated at 2022-06-13 20:55:17.073146
# Unit test for function chown
def test_chown():
    """
    Test this function.
    """
    from flutils.pathutils import chown
    import stat

    assert chown(__file__) is None

    assert chown(__file__, user='root') is None

    assert chown(__file__, group='root') is None

    assert chown(__file__, user='root', group='root') is None

    assert chown(__file__, user='-1', group='-1') is None

    assert chown(__file__, user=-1, group=-1) is None

    assert chown(__file__, user=-1, group='-1') is None

    assert chown(__file__, user='-1', group=-1) is None

    assert chown(__file__, user=0, group=0) is None

    assert chown

# Generated at 2022-06-13 20:55:27.788268
# Unit test for function exists_as
def test_exists_as():
    # Create the test.txt file
    path = normalize_path('~/tmp/test.txt')
    path.touch()

    # Create the test directory
    path = normalize_path('~/tmp/test')
    path.mkdir()

    # Create the test.fifo file
    path.parent.joinpath('test.fifo').touch()

    # Create the test.socket file
    path.parent.joinpath('test.socket').touch()

    # Create the test.block file
    path.parent.joinpath('test.block').touch()

    # Create the test.char file
    path.parent.joinpath('test.char').touch()

    # Check all the file types.
    result = exists_as('~/tmp/test.txt')
    assert result == 'file'


# Generated at 2022-06-13 20:55:48.092522
# Unit test for function find_paths
def test_find_paths():
    """Unit test for function :obj:`find_paths`."""
    with TemporaryDirectory() as tmpd:
        t_root = Path(tmpd)
        Path(t_root / 'file_one').touch()
        Path(t_root / 'file_two').touch()
        Path(t_root / 'dir_one').mkdir()
        Path(t_root / 'dir_two').mkdir()
        paths = list(find_paths(str(t_root / '*')))
        assert len(paths) == 4
        for p in paths:
            assert p.exists()

        paths = list(find_paths(str(t_root / 'dir_*')))
        assert len(paths) == 2
        for p in paths:
            assert p.exists()

# Generated at 2022-06-13 20:55:49.241236
# Unit test for function chown
def test_chown():
    assert True



# Generated at 2022-06-13 20:55:50.942477
# Unit test for function chmod
def test_chmod():
    assert 1 == 1


# Generated at 2022-06-13 20:56:02.509717
# Unit test for function chmod
def test_chmod():
    import filecmp
    import os
    import random
    import shutil
    import tempfile

    from flutils.pathutils import chmod, find_paths

    # Temporary directory to use for testing
    tmp_dir = tempfile.mkdtemp()

    # Create a temporary file
    test_file = os.path.join(tmp_dir, 'test_file.txt')
    with open(test_file, 'wb') as tmp_fp:
        tmp_fp.write(os.urandom(random.randint(15000, 16000)))

    # Create a temporary directory
    test_dir = os.path.join(tmp_dir, 'test_dir')
    os.mkdir(test_dir)

    # Create another temporary file in the temporary directory

# Generated at 2022-06-13 20:56:09.757862
# Unit test for function find_paths
def test_find_paths():
    """Tests for the find_paths module.

    This path was generated with:
    >>> from flutils.pathutils import find_paths
    >>> from pprint import pprint
    >>> pprint(list(find_paths('~/tmp/*')))
    """
    assert list(find_paths('~/tmp/*')) == [
        Path('/Users/len/tmp/file_one'),
        Path('/Users/len/tmp/dir_one')
    ]



# Generated at 2022-06-13 20:56:21.317012
# Unit test for function find_paths
def test_find_paths():
    from tempfile import mkdtemp
    from shutil import rmtree
    import os

    # Create a temprary directory to run the test in
    temp_dir = Path(mkdtemp())
    # Create ~tmp
    tmp_dir = Path(temp_dir.as_posix(), 'tmp')
    tmp_dir.mkdir()
    # Create ~/tmp/file_one
    path = Path(tmp_dir.as_posix(), 'file_one')
    path.touch()
    # Create ~/tmp/dir_one
    path = Path(tmp_dir.as_posix(), 'dir_one')
    path.mkdir()
    # Return a list of paths found
    found_paths = list(find_paths(os.path.join(tmp_dir, '*')))
    # Cleanup
   

# Generated at 2022-06-13 20:56:33.164178
# Unit test for function chown
def test_chown():
    from flutils.testing import (
        hide_stdout,
        hide_stdout_and_stderr,
        unittest,
    )
    import textwrap
    import tempfile
    import os
    import stat

    class TestChown(unittest.TestCase):
        @classmethod
        def setUpClass(cls) -> None:
            cls.tst_dir = tempfile.mkdtemp(prefix='flutils_')

        @classmethod
        def tearDownClass(cls) -> None:
            for fname in (
                'file.txt',
                'file.passed',
                'file.failed',
                'file.nested',
                'file.nested.passed',
                'file.nested.failed',
            ):
                tst_file = os.path

# Generated at 2022-06-13 20:56:38.302383
# Unit test for function chmod
def test_chmod():
    (z0, z1) = mkstemp()
    os.close(z0)
    assert os.path.exists(z1)
    # Cleanup
    Path(z1).unlink()
    assert os.path.exists(z1) is False


# Generated at 2022-06-13 20:56:44.366002
# Unit test for function chmod
def test_chmod():
    """Unit test for module level "chmod" function."""
    from flutils.pathutils import chmod

    Path('/tmp/flutils_tests.txt').touch()
    chmod('/tmp/*', mode_file=0o660, mode_dir=0o770)

    assert Path('/tmp/flutils_tests.txt').stat().st_mode == 33060

    Path('/tmp/flutils_tests.txt').unlink()



# Generated at 2022-06-13 20:56:56.644779
# Unit test for function chmod
def test_chmod():
    """ Function to test the functionality of chmod."""
    tempDir = str(Path(Path(__file__).parent.resolve(), 'temp'))
    os.makedirs(tempDir, mode=0o700, exist_ok=True)
    with open(os.path.join(tempDir, 'testFile.txt'), 'w') as f:
        f.write('Hello World!')
    with open(os.path.join(tempDir, 'testFile2.txt'), 'w') as f:
        f.write('Hello World!')
    chmod(os.path.join(tempDir, 'testFile.txt'), 0o600)
    with open(os.path.join(tempDir, 'testFile.txt'), 'r') as f:
        contents = f.read()
    assert contents == 'Hello World!'

# Generated at 2022-06-13 20:57:11.188115
# Unit test for function chmod
def test_chmod(): # unit test for function chmod

    from os.path import join
    from pathlib import Path
    from tempfile import TemporaryDirectory

    def test_file(name, tmp_dir):
        path = Path(join(tmp_dir, name))
        chmod(path, mode_file=0o660)
        assert path.stat().st_mode == 33188
        chmod(path, mode_file=0o646)
        assert path.stat().st_mode == 33182
        chmod(path)  # 0o600
        assert path.stat().st_mode == 33152

    def test_dir(name, tmp_dir):
        path = Path(join(tmp_dir, name))
        chmod(path, mode_dir=0o770)
        assert path.stat().st_mode == 40777

# Generated at 2022-06-13 20:57:18.162675
# Unit test for function exists_as
def test_exists_as():
    """Tests for flutils.pathutils.exists_as."""

    # Test: No path was given.
    try:
        exists_as(None)
        assert False, 'No exception was raised'
    except TypeError:
        pass

    # Test: Path does not exist.
    assert exists_as('~/tmp/doesnotexist') == ''

    # Test: Path exists as a directory.
    assert exists_as('~/tmp') == 'directory'

    # Test: Path exists as a file.
    assert exists_as('~/tmp/flutils.tests.pathutils.txt') == 'file'

    # Test: Path exists as a block device.
    if os.stat.S_IFBLK:
        assert exists_as('/dev/null') == 'block device'

    # Test: Path exists as a

# Generated at 2022-06-13 20:57:29.641522
# Unit test for function chmod
def test_chmod():
    """Test the chmod function."""
    from flutils.pathutils import chmod  # type: ignore
    import tempfile
    import shutil
    import os
    import stat

    tmp = Path(tempfile.gettempdir()) / Path(__file__).stem

# Generated at 2022-06-13 20:57:30.805648
# Unit test for function chown
def test_chown():
    assert 1 == 1



# Generated at 2022-06-13 20:57:42.798630
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/') == 'directory'
    assert exists_as('/etc') == 'directory'
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/dev/disk0s1') == 'block device'
    assert exists_as('/dev/console') == 'char device'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/stdin') == 'char device'
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/proc/self/fd/2') == ''
    assert exists_as('/dev/null') == ''
    assert exists_as('/dev/urandom') == ''



# Generated at 2022-06-13 20:57:53.223349
# Unit test for function chmod
def test_chmod():
    """
    Unit test for function flutils.osutils.chmod.
    """
    import os
    import stat
    import tempfile
    import textwrap
    import unittest
    from flutils.osutils import chmod


# Generated at 2022-06-13 20:57:55.604224
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown

    chown('flutils.tests.osutils.txt.example')

# Generated at 2022-06-13 20:58:07.070471
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/test_file.txt') == 'file'
    assert exists_as('~/tmp/test_file2.txt') == ''
    assert exists_as('~/..') == ''
    assert exists_as('~/.bash_profile') == 'file'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/tty1') == ''
    assert exists_as('/proc/devices') == 'file'
    assert exists_as('/proc/devices.txt') == ''
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/ram') == ''



# Generated at 2022-06-13 20:58:16.840589
# Unit test for function chmod
def test_chmod():
    from flutils.runcheck import run_function_with_changed_umask
    from flutils.pathutils import chmod
    from flutils.pyutils import generate_random_string

    p = Path.home().joinpath(
        '.flutils.tests',
        '%s.txt' % generate_random_string()
    )

    if p.exists() is True:
        p.unlink()

    # Create the file with permissions 0o777
    # This will allow both reading and writing
    p.touch()
    p.chmod(0o777)
    assert p.exists() is True

    # Now change the permissions of the created file
    # to 0o600
    chmod(p, mode_file=0o600)
    assert p.stat().st_mode & 0o777 == 0o600

   

# Generated at 2022-06-13 20:58:28.405939
# Unit test for function chmod
def test_chmod():
    from .mocks import MockPath
    from .osutils import MockChmod
    chmod(MockPath('flutils.tests.pathutils.chmod.txt', exists=True, isdir=False, isfile=True), mode_file=0o660, mode_dir=0o770)
    assert MockChmod.mode_file == 0o660
    assert MockChmod.mode_dir == 0o770
    chmod(MockPath('flutils.tests.pathutils.chmod.txt', exists=True, isdir=True, isfile=False), mode_file=0o660, mode_dir=0o770)
    assert MockChmod.mode_file == 0o660
    assert MockChmod.mode_dir == 0o770

# Generated at 2022-06-13 20:58:36.013257
# Unit test for function chown
def test_chown():
    pass


# Generated at 2022-06-13 20:58:47.224183
# Unit test for function get_os_user
def test_get_os_user():
    """Test for function get_os_user."""
    name = get_os_user()
    assert isinstance(name, pwd.struct_passwd)
    assert name.pw_name == getpass.getuser()

    name = get_os_user('')
    assert isinstance(name, pwd.struct_passwd)
    assert name.pw_name == getpass.getuser()

    name = get_os_user(get_os_user().pw_name)
    assert isinstance(name, pwd.struct_passwd)
    assert name.pw_name == getpass.getuser()

    # On Windows platforms 'nobody' is not a valid name.
    if os.name != 'nt':
        name = get_os_user('nobody')

# Generated at 2022-06-13 20:58:56.218910
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod, directory_present
    import os

    path = os.path.expanduser('~/tmp/flutils.tests.pathutils.txt')

    directory_present(os.path.dirname(path))

    os.open(path, os.O_CREAT | os.O_RDWR)

    mode_file = 0o640

    chmod(path, mode_file=mode_file)

    assert os.stat(path).st_mode & 0o777 == mode_file



# Generated at 2022-06-13 20:59:07.222479
# Unit test for function chmod
def test_chmod():
    testfile = '~/tmp/flutils.tests.osutils.txt'
    chmod(testfile, 0o600, 0o700)
    assert os.stat(os.path.expanduser(testfile)).st_mode & 0o777 == 0o600
    chmod(testfile, 0o660, 0o770)
    assert os.stat(os.path.expanduser(testfile)).st_mode & 0o777 == 0o660
    chmod('~/tmp/**', 0o644, 0o770)
    assert os.stat(os.path.expanduser(testfile)).st_mode & 0o777 == 0o664
    chmod('~/tmp/*', 0o644)

# Generated at 2022-06-13 20:59:16.507125
# Unit test for function chown
def test_chown():
    os.chown = MagicMock()
    p = MagicMock(spec_set=Path)
    p.exists.return_value = True
    p.is_dir.return_value = False
    p.is_file.return_value = True
    p.as_posix.return_value = '/tmp/test/testpath'
    normalize_path = MagicMock(return_value=p)
    os_user = MagicMock()
    os_user.pw_uid = 42
    get_os_user = MagicMock(return_value=os_user)
    os_group = MagicMock()
    os_group.gr_gid = 1337
    get_os_group = MagicMock(return_value=os_group)
    test_path = '/tmp/test/testpath'

# Generated at 2022-06-13 20:59:22.451266
# Unit test for function chown
def test_chown():
    chown('~/tmp/flutils.tests.osutils.txt', include_parent=True)

    chown('~/tmp/*', include_parent=True)

    chown('~/tmp/flutils.tests.osutils.txt','-1','-1',include_parent=True)

    # Supports a glob pattern.  So to recursively change the ownership
    # of a directory just do:
    chown('~/tmp/**')



# Generated at 2022-06-13 20:59:26.519244
# Unit test for function path_absent
def test_path_absent():
    test_dir = '~/tmp/test_path'
    path_absent(test_dir)
    assert exists_as(test_dir) == '', 'path_absent() should delete a path'



# Generated at 2022-06-13 20:59:34.144299
# Unit test for function chown
def test_chown():
    normalize_path('~/tmp')
    chown('~/tmp/flutils.tests.osutils.txt', user='-1')
    chown('~/tmp/flutils.tests.osutils.txt', user='foo', group='bar', include_parent=True)
    path = normalize_path('~/tmp/**')
    chown(path, user='foo', group='bar')



# Generated at 2022-06-13 20:59:46.117443
# Unit test for function chmod
def test_chmod():
    import shutil
    import tempfile
    tmpdir = tempfile.mkdtemp()
    f = os.path.join(tmpdir, 'test1.txt')
    with open(f, 'w') as fd:
        fd.write('test')
    os.chmod(f, 0o600)
    f2 = os.path.join(tmpdir, 'test2.txt')
    os.symlink(f, f2)

# Generated at 2022-06-13 20:59:59.396958
# Unit test for function chmod
def test_chmod():
    import io
    import logging
    import os
    import shutil
    import stat
    import sys
    import tempfile

    from flutils.pathutils import find_paths, get_os_functions
    from flutils.pathutils import normalize_path
    from flutils.osutils import chmod

    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())

    logger.debug('Starting unit test for: chmod')
    logger.debug('Python version: %s', sys.version)

    os_stat = get_os_functions().stat
    os_unlink = get_os_functions().unlink

    # Create test data
    userid = os.getuid()


# Generated at 2022-06-13 21:00:05.748017
# Unit test for function path_absent
def test_path_absent():
    pass



# Generated at 2022-06-13 21:00:08.101405
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(__file__) == 'file'
test_exists_as()



# Generated at 2022-06-13 21:00:25.059885
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as, normalize_path
    from flutils import pytest_helpers
    from pathlib import Path
    from string import ascii_letters, digits
    from tempfile import TemporaryDirectory

    def _create_file_spec(path: Path) -> None:
        """Create a file."""
        with path.open('w') as fd:
            fd.write('%r = %r' % (path.as_posix(), path))

    def _create_dir_spec(path: Path, mode: int) -> None:
        """Create a directory."""
        path.mkdir(mode=mode)

    def _create_block_spec(path: Path) -> None:
        """Create a block device."""
        path.touch()
        path.chmod(0o600)

# Generated at 2022-06-13 21:00:26.202416
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:00:29.800929
# Unit test for function directory_present
def test_directory_present():
    status = directory_present('~/tmp/flutils_test_directory')
    assert status.as_posix() == '/Users/len/tmp/flutils_test_directory'



# Generated at 2022-06-13 21:00:36.576669
# Unit test for function chown
def test_chown():
    test_path = Path('~/tmp/flutils.tests.osutils.txt').expanduser()
    test_path.touch()
    chown(test_path, user='-1', group='-1', include_parent=True)
    user_group = test_path.parent.stat().st_uid, test_path.parent.stat().st_gid
    test_path.unlink()
    assert user_group == os.getuid(), os.getgid()



# Generated at 2022-06-13 21:00:39.361312
# Unit test for function chown
def test_chown():
    """Test function chown.

    :rtype: :obj:`bool`
    """
    import pytest
    return pytest.main()



# Generated at 2022-06-13 21:00:51.282805
# Unit test for function path_absent
def test_path_absent():
    import shutil
    import tempfile
    from flutils.pathutils import path_absent

    def make_path(path):
        open(path, 'w').close()
        return path

    def make_dir(path):
        os.mkdir(path)
        return path

    def make_symlink(path):
        os.symlink('/dev/null', path)
        return path

    paths = [
        # Path exists as a file.
        make_path('tmp/test_path/foo'),
        # Path exists as a directory.
        make_dir('tmp/test_path/bar'),
        # Path exists as a symlink.
        make_symlink('tmp/test_path/baz')
    ]


# Generated at 2022-06-13 21:01:00.701157
# Unit test for function exists_as
def test_exists_as():
    from os import makedirs
    from os import remove
    from os import symlink
    from tempfile import mkdtemp
    from tempfile import mkstemp

    # Basic directory test.
    tmpdir = mkdtemp()
    assert exists_as(tmpdir) == 'directory'
    rmdir(tmpdir)

    # Check that mkdtemp still works in /tmp if root owned.
    tmpdir = mkdtemp()
    assert exists_as(tmpdir) == 'directory'
    rmdir(tmpdir)

    # Broken symbolic link.
    tmpdir = mkdtemp()
    broken_link = '%s/broken_link' % tmpdir
    symlink('%s/DOES_NOT_EXIST' % tmpdir, broken_link)
    assert exists_as(broken_link) == ''


# Generated at 2022-06-13 21:01:12.879956
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import (
        chmod,
        directory_exists,
    )

    normalize_path = functools.partial(
        str,
        functools.partial(
            Path,
            Path(__file__).parent,
            'flutils.tests.osutils'
        )
    )

    # Create a temporary directory and file.
    #
    # pathlib.mkdir() creates the directory with
    # the mode being octal 0o40777, which fails the
    # tests.  So chmod() to fix that.
    directory_exists(
        Path(__file__).parent,
        'flutils.tests.osutils'
    )
    Path(__file__).parent / 'flutils.tests.osutils' / 'temp_dir'

# Generated at 2022-06-13 21:01:27.406482
# Unit test for function path_absent
def test_path_absent():
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        path = normalize_path(tempdir)
        assert os.path.exists(path.as_posix())
        assert os.path.isdir(path.as_posix())
        path_absent(path)
        assert not os.path.exists(path.as_posix())
        assert not os.path.isdir(path.as_posix())



# Generated at 2022-06-13 21:01:35.791209
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/flutils.tests.pathutils') == 'directory'
    assert exists_as('~/tmp/flutils.tests.pathutils/test_file.txt') == 'file'
    assert exists_as('~/tmp/flutils.tests.pathutils/test_file_404.txt') == ''
    assert exists_as('~/tmp/flutils.tests.pathutils/test_dir_404') == ''
    assert exists_as('~/tmp/flutils.tests.pathutils/test_file_500.txt') == ''



# Generated at 2022-06-13 21:01:45.050082
# Unit test for function directory_present
def test_directory_present():
    # Testing with an existing path that is a file.
    p1 = Path('/tmp/flutils_test_directory_present.txt')
    p1.touch()
    # Testing with an existing path that is a directory.
    p2 = Path('/tmp/flutils_test_directory_present.txt/bar/foo')
    p2.mkdir(parents=True, mode=0o600)
    # Testing with a non-existing path.
    p3 = Path('/tmp/flutils_test_directory_present.txt.bar/foo')
    # Testing with an existing path that is a symlink.
    p4 = Path('/tmp/flutils_test_directory_present.txt.bar/link')
    p4.symlink_to('/tmp')
    # Testing with a path that is a dir and a

# Generated at 2022-06-13 21:01:57.325690
# Unit test for function chown
def test_chown():
    import os
    import tempfile
    import shutil
    import filecmp
    tmp_dir, tmp_dir_path = tempfile.mkdtemp()
    tmp_file, tmp_file_path = tempfile.mkstemp(dir=tmp_dir, text=True)

# Generated at 2022-06-13 21:02:09.485099
# Unit test for function chown
def test_chown():
    """Test flutils.pathutils.chown

    """
    # Test with a glob pattern
    all_dirs = Path('/tmp').glob('*')
    parent_dir = Path('/tmp/foo-bar')
    parent_dir.mkdir(parents=True)
    delete_files = [parent_dir]
    for _dir in all_dirs:
        if '/foo-bar' in str(_dir):
            continue
        if _dir.is_dir():
            delete_files.append(_dir)
            chown(str(_dir), 'root', 'root')
            assert os.stat(str(_dir)).st_uid == 0
            assert os.stat(str(_dir)).st_gid == 0
    chown(str(parent_dir), 'root', 'root')

# Generated at 2022-06-13 21:02:14.454487
# Unit test for function get_os_user
def test_get_os_user():
    import os
    import pwd
    from flutils.pathutils import get_os_user
    assert(get_os_user() == pwd.getpwuid(os.getuid()))



# Generated at 2022-06-13 21:02:26.143011
# Unit test for function exists_as
def test_exists_as():
    from . import BaseTestCase
    from . import MockPrePostMixin

    class TestExistsAs(MockPrePostMixin, BaseTestCase):
        path = '/path/to/file'

        def setUp(self):
            super().setUp()
            self.set_module_attr(
                'exists_as', 'flutils.normalize_path', self.path_mock
            )
            self.path_mock.return_value = self.path
            self.set_module_attr(
                'exists_as', 'os.path.exists', self.exists_mock
            )
            self.set_module_attr(
                'exists_as', 'os.path.isdir', self.isdir_mock
            )

# Generated at 2022-06-13 21:02:35.694393
# Unit test for function exists_as
def test_exists_as():
    """Test function: flutils.pathutils.exists_as"""
    import os

    assert exists_as('/dev/null') == 'character device'
    assert exists_as('/dev/console') == 'character device'
    assert exists_as('/dev/tty') == 'character device'
    assert exists_as('/dev/sda') == 'block device'
    assert exists_as('/dev/sdb') == 'block device'
    assert exists_as('/dev/sdc') == 'block device'
    assert exists_as('/proc') == 'directory'
    assert exists_as('/root') == 'directory'
    assert exists_as('/root/.bashrc') == 'file'
    assert exists_as('/root/.bashrc.backup') == 'file'

# Generated at 2022-06-13 21:02:38.751468
# Unit test for function chown
def test_chown():
    assert chown is not None, '''Function "chown" is not defined.'''



# Generated at 2022-06-13 21:02:45.716210
# Unit test for function chmod
def test_chmod():
    test_path = 'flutils.tests.osutils.txt'
    if os.path.isfile(test_path):
        os.path.unlink(test_path)
    f = open(test_path, 'w+')
    if f:
        f.close()
    chmod(test_path, 0o1)
    if os.path.isfile(test_path):
        os.path.unlink(test_path)



# Generated at 2022-06-13 21:03:09.376531
# Unit test for function chown
def test_chown():
    assert True



# Generated at 2022-06-13 21:03:11.062645
# Unit test for function path_absent
def test_path_absent():
    """Unit tests for function ``path_absent``."""
    os.listdir()

# Generated at 2022-06-13 21:03:22.041233
# Unit test for function chmod
def test_chmod():
    """Unit test for the function chmod."""

    from .mockutils import (
        create_mock_file,
        create_mock_dir,
    )

    from .osutils import (
        get_os_file_mode,
        get_os_dir_mode,
    )

    mock = create_mock_file()
    chmod(mock.path, 0o666)
    mode = get_os_file_mode(mock.path)
    assert mode == 0o666

    chmod(mock.path, 0o644)
    mode = get_os_file_mode(mock.path)
    assert mode == 0o644

    mock = create_mock_dir()
    chmod(mock.path, mode_dir=0o775)
    mode = get_os_dir

# Generated at 2022-06-13 21:03:33.678264
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import (
        chmod,
        exists_as,
        normalize_path,
    )
    from tempfile import (
        TemporaryDirectory,
    )

    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        file1 = tmpdir / 'flutils.tests.osutils.file1.txt'
        file1.touch()
        assert file1.stat().st_mode == 33206

        file2 = tmpdir / 'flutils.tests.osutils.file2.txt'
        file2.touch()
        assert file2.stat().st_mode == 33206

        file3 = tmpdir / 'flutils.tests.osutils.file3.txt'
        file3.touch()
        assert file3.stat().st_mode == 33206


# Generated at 2022-06-13 21:03:41.628592
# Unit test for function directory_present
def test_directory_present():
    """Test the flutils.pathutils.directory_present function.
    """
    from tempfile import TemporaryDirectory
    from pytest import raises

    tmpdir = TemporaryDirectory()
    try:
        tmp_path = Path(tmpdir.name)
        parent = directory_present(tmp_path / 'new_dir')
        assert parent.is_dir() is True
        child = directory_present(parent / 'child')
        assert child.is_dir() is True
        with raises(FileExistsError):
            directory_present(tmp_path / 'file2.txt')
    finally:
        tmpdir.cleanup()

