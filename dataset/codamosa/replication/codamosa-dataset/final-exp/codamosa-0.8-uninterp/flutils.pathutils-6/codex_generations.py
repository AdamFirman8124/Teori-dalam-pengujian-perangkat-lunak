

# Generated at 2022-06-13 20:54:10.492953
# Unit test for function chown
def test_chown():
    self.tmp_dir.join('test_pathutils_chown.txt').write('')
    chown(self.tmp_dir.join('test_pathutils_chown.txt'), 'root', 'root')
    assert chown.__doc__ is not None



# Generated at 2022-06-13 20:54:22.124766
# Unit test for function find_paths
def test_find_paths():
    import os
    import shutil
    import tempfile

    from flutils.pathutils import find_paths

    # Tuple of possible paths to check.
    PATHS = (
        'home/test_user/tmp/file_one',
        'home/test_user/tmp/file_two',
        'home/test_user/tmp/dir_one/file_three',
        'home/test_user/tmp/dir_one/file_four',
        'home/test_user/tmp/dir_one/dir_two/file_five'
    )

    # Tuple of expected directories.
    DIRS = (
        'home/test_user/tmp/dir_one',
        'home/test_user/tmp/dir_one/dir_two'
    )


# Generated at 2022-06-13 20:54:27.060850
# Unit test for function chown
def test_chown():  # noqa: D103
    chown('~/tmp/flutils.tests.osutils.txt')
    chown('~/tmp/**')
    chown('~/tmp/*', user='foo', group='bar')



# Generated at 2022-06-13 20:54:29.386196
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:54:34.549127
# Unit test for function chown
def test_chown():
    from tempfile import TemporaryDirectory
    from flutils.pathutils import path_absent, chown

    with TemporaryDirectory() as tmpdir:
        print(tmpdir)
        chown(tmpdir)
        chown(tmpdir, user='-1', group='-1')
        path_absent(tmpdir)



# Generated at 2022-06-13 20:54:38.400654
# Unit test for function find_paths
def test_find_paths():
    assert list(find_paths('~/tmp/*')) \
        == [Path('/home/test_user/tmp/file_one'),
            Path('/home/test_user/tmp/dir_one')]



# Generated at 2022-06-13 20:54:52.048703
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    from flutils.tests.test_decorators import random_string

    # Test directory
    directory = Path('/')
    assert exists_as(directory) == 'directory'

    # Test file
    temp_file_name = random_string(10)
    with TempDir() as temp_dir:
        temp_file = temp_dir.as_posix() + '/' + temp_file_name
        with open(temp_file, 'w'):
            pass
        assert exists_as(temp_file) == 'file'

    # Test broken symbolic link
    temp_dir_name = random_string(10)
    with TempDir() as temp_dir:
        temp_dir = temp_dir.as_posix() + '/' + temp_dir_name

# Generated at 2022-06-13 20:55:08.581212
# Unit test for function exists_as
def test_exists_as():
    # Test if a Path().exists() == False and that it returns ''
    path = Path(tempfile.mkdtemp() + '/noexist')
    assert exists_as(path) == ''

    # Test if a Path().exists() == True, is a dir and that it returns 'directory'
    path = Path(tempfile.mkdtemp())
    assert exists_as(path) == 'directory'

    # Test if a Path().exists() == True, is a file and that it returns 'file'
    path = Path(tempfile.NamedTemporaryFile().name)
    assert exists_as(path) == 'file'

    # Test if a Path().exists() == True, is a block device and that it returns
    # 'block device'
    # TODO: How to test a block device since it's OS dependent?

   

# Generated at 2022-06-13 20:55:20.339519
# Unit test for function chown
def test_chown():
    """
    Test the function chown.
    """

    test_user = get_os_user('root')
    test_group = get_os_group('wheel')
    path = Path() / 'tmp' / 'food'
    mode = 0o600
    path.mkdir(mode=mode)
    chown(path, user=test_user.pw_name, group=test_group.gr_name, include_parent=False)
    result_user = get_os_user(path.owner())
    result_group = get_os_group(path.group())
    assert result_user.pw_name == test_user.pw_name
    assert result_group.gr_name == test_group.gr_name
    path.rmdir()



# Generated at 2022-06-13 20:55:29.265152
# Unit test for function find_paths
def test_find_paths():
    """Unit test for ``find_paths`` function."""
    from flutils.pathutils import find_paths
    from typing import Generator

    matches = list(find_paths('~/tmp/*/file_one'))
    assert len(matches) == 2
    assert type(find_paths('~/tmp/*/file_one')) == Generator
    assert str(matches[0]) == '~/tmp/dir_one/file_one'
    assert str(matches[1]) == '~/tmp/dir_two/file_one'

    matches = list(find_paths('~/tmp/dir_one/file_one'))
    assert len(matches) == 1
    assert type(find_paths('~/tmp/dir_one/file_one')) == Generator

# Generated at 2022-06-13 20:55:54.184730
# Unit test for function directory_present
def test_directory_present():
    path = directory_present('/tmp/tmp_directory_present_test')
    path_exists_as = exists_as(path)
    assert path_exists_as == 'directory'



# Generated at 2022-06-13 20:55:55.045988
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:56:03.434340
# Unit test for function chmod
def test_chmod():
    # Test chmod with a simple file.
    with _create_temp_path('flutils.tests.osutils.txt') as temp_path:
        chmod(temp_path, 0o660)
        assert temp_path.stat().st_mode == 0o100660

    # Test chmod with a simple directory.
    with _create_temp_path() as temp_path:
        chmod(str(temp_path), mode_dir=0o770)
        assert temp_path.stat().st_mode == 0o40770

    # Test chmod with a nested directory.
    with _create_temp_path() as temp_path:
        nested_path = temp_path.joinpath('nested_dir')
        nested_path.mkdir()
        chmod(str(temp_path), mode_dir=0o770)

# Generated at 2022-06-13 20:56:13.522761
# Unit test for function exists_as
def test_exists_as():
    directory = normalize_path('~/tmp')
    path = '~/tmp/flutils.tests.osutils.txt'
    path = pathlib.Path(path).expanduser().resolve()
    if path.parent.exists():
        os.remove(path)
    if directory.exists() is False:
        directory.mkdir(0o700)
    assert exists_as(directory) == 'directory'
    with open(path, 'w') as file:
        file.write('some text')
    assert exists_as(path) == 'file'
    os.remove(path)
    assert exists_as(path) == ''
    assert exists_as(path) != 'directory'



# Generated at 2022-06-13 20:56:15.909163
# Unit test for function chown
def test_chown():
    """
    Unit test for function chown
    """
    assert False, "Test is not implemented"



# Generated at 2022-06-13 20:56:25.922836
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/etc/') == 'directory'
    assert exists_as('/etc') == ''
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/dev/null') == 'block device'
    assert exists_as('/dev/nulla') == ''
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/dev/randomb') == ''
    assert exists_as('/etc/passwd') == 'file'
    if Path('/tmp/flutils-test.socket').exists():
        Path('/tmp/flutils-test.socket').unlink()

# Generated at 2022-06-13 20:56:29.939718
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    chown('~/tmp/flutils.tests.osutils.txt')
    chown('~/tmp/**')
    chown('~/tmp/*', user='foo', group='bar')


# Generated at 2022-06-13 20:56:40.571153
# Unit test for function directory_present
def test_directory_present():
    from os import makedirs
    from os.path import abspath
    from pathlib import Path

    from flutils.pathutils import (
        directory_present,
        get_os_user,
        posixpath,
    )

    def _test_directory_present(
            path: str,
            expected_path: Path,
            mode: Optional[int] = None,
            user: Optional[str] = None,
            group: Optional[str] = None
    ) -> None:
        test_name = 'directory_present(%r, %r, %r, %r)' % (
            path,
            mode,
            user,
            group
        )
        print(test_name)

        if user is None:
            user = get_os_user().pw_name


# Generated at 2022-06-13 20:56:46.674986
# Unit test for function directory_present
def test_directory_present():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / 'flutils-test-path'
        path = directory_present(path)
        assert path.exists() is True
        assert path.is_dir() is True
        assert path.is_file() is False

# Generated at 2022-06-13 20:56:51.268758
# Unit test for function chown
def test_chown():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / 'foo'
        path.touch()
        path.chmod(0o640)
        path.chown(0, 0)
        stat = path.stat()
        assert stat.st_mode & 0o777 == 0o640
        assert stat.st_uid == 0
        assert stat.st_gid == 0



# Generated at 2022-06-13 20:57:17.625916
# Unit test for function chmod
def test_chmod():
    raise NotImplementedError()



# Generated at 2022-06-13 20:57:19.822503
# Unit test for function exists_as
def test_exists_as():
    path = Path(__file__)
    assert exists_as(path) == 'file'

    path = Path(__file__).parent
    assert exists_as(path) == 'directory'



# Generated at 2022-06-13 20:57:28.923407
# Unit test for function path_absent
def test_path_absent():
    path = Path('~/tmp/test_dir')
    if path.exists():
        path_absent(path)
    path.mkdir(mode=0o700)
    path_absent(path)
    assert not path.exists(),  'Unable to remove the directory: %r' % path
    path.mkdir(mode=0o700)
    Path(path / 'test_file1').write_text('foo')
    Path(path / 'test_file2').write_text('bar')
    path_absent(path)
    assert not path.exists(),  'Unable to remove the directory: %r' % path



# Generated at 2022-06-13 20:57:41.478982
# Unit test for function chown
def test_chown():
    target = Path(__file__).parent.parent.parent / 'tmp' / 'flutils' / 'tests' / 'osutils.txt'
    if target.exists():
        target.unlink()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.touch()
    chown('**', '-1', '-1')
    target.chown(os.geteuid(), os.getegid())
    chown('**')
    statinfo = os.stat(target.as_posix())
    assert getpass.getuser() == pwd.getpwuid(statinfo.st_uid).pw_name
    assert getpass.getuser() == grp.getgrgid(statinfo.st_gid).gr_name
    target.unlink()


# Generated at 2022-06-13 20:57:52.225132
# Unit test for function chmod

# Generated at 2022-06-13 20:58:04.383792
# Unit test for function chown
def test_chown():
    import os
    import shutil
    import tempfile
    import unittest
    import uuid

    from flutils.pathutils import chown

    class TestChown(unittest.TestCase):
        def setUp(self):
            self.tmp_dir = tempfile.mkdtemp()

            self.file_path1 = Path(self.tmp_dir, 'flutils.tests.osutils1.txt')
            self.file_path2 = Path(self.tmp_dir, 'flutils.tests.osutils2.txt')
            self.dir_path = Path(self.tmp_dir, uuid.uuid4().hex)

            with self.file_path1.open(mode='w') as f:
                f.write(uuid.uuid4().hex)


# Generated at 2022-06-13 20:58:14.092234
# Unit test for function chown
def test_chown():
    path = Path(__file__).parent.joinpath('osutils.txt')
    path.touch()
    assert path.is_file() is True
    assert path.stat().st_uid == 0
    assert path.stat().st_gid == 0

    chown(path)

    assert path.stat().st_uid == getpass.getuser()
    assert path.stat().st_gid == getpass.getuser()
    assert path.is_file() is True

    chown(path, user='foo', group='bar')
    assert path.stat().st_uid == 'foo'
    assert path.stat().st_gid == 'bar'
    assert path.is_file() is True

    path.unlink()



# Generated at 2022-06-13 20:58:27.294989
# Unit test for function chmod
def test_chmod():
    if exists_as('/tmp/flutils.tests.osutils.txt') is True:
        os.remove('/tmp/flutils.tests.osutils.txt')
    if exists_as('/tmp/flutils.tests.osutils') is True:
        os.rmdir('/tmp/flutils.tests.osutils')

    if exists_as('/tmp/flutils.tests') is True:
        os.rmdir('/tmp/flutils.tests')

    Path('/tmp/flutils.tests').mkdir(0o700)
    Path('/tmp/flutils.tests.osutils').mkdir(0o700)
    Path('/tmp/flutils.tests.osutils.txt').touch()


# Generated at 2022-06-13 20:58:39.706415
# Unit test for function directory_present
def test_directory_present():
    import os
    import shutil
    import tempfile
    tmproot = tempfile.mkdtemp()
    path = os.path.join(tmproot, 'path.txt')
    try:
        with open(path, 'w') as f:
            f.write('test')
        with pytest.raises(FileExistsError):
            directory_present(path)
        os.remove(path)
        path = directory_present(path)
        assert not os.path.exists(path)
        assert os.path.exists(os.path.dirname(path))
    finally:
        shutil.rmtree(tmproot)



# Generated at 2022-06-13 20:58:49.861897
# Unit test for function chmod
def test_chmod():
    import os
    import shutil
    import stat
    import tarfile
    import tempfile
    import unittest
    import warnings

    from flutils.osutils import (
        chmod,
        directory_present,
    )

    from flutils.pathutils import (
        normalize_path,
        path_absent,
    )

    tmp_dir = Path(tempfile.gettempdir())
    file_path = tmp_dir.joinpath('flutils.tests.osutils.txt')

    if file_path.exists():
        file_path.unlink()

    dir_path = tmp_dir.joinpath('flutils.tests.osutils')
    if dir_path.exists():
        shutil.rmtree(dir_path)


# Generated at 2022-06-13 20:59:25.410648
# Unit test for function chown
def test_chown():
    import os
    import shutil
    import tempfile
    import time
    import unittest
    from flutils.pathutils import chown
    import flutils.pathutils as utils  # For function to test

    class TestChown(unittest.TestCase):
        def setUp(self):
            self.temp_dirname = tempfile.mkdtemp(prefix='chown-test-')

        def tearDown(self):
            shutil.rmtree(self.temp_dirname)

        def test_chown_directories(self):
            """
            Verify directory ownership changes recursively.
            """
            # Create a few directories
            base_directory = os.path.join(self.temp_dirname, 'foo')
            os.mkdir(base_directory)

# Generated at 2022-06-13 20:59:38.682855
# Unit test for function path_absent
def test_path_absent():
    # Clean up the test directory if it is there.
    # Then create the test directory.
    ret = path_absent('~/tmp/flutils_test')
    assert ret is None
    ret = path_create('~/tmp/flutils_test')
    assert ret == Path('~/tmp/flutils_test')

    # Create the more test directories
    # and files.
    ret = path_create('~/tmp/flutils_test/test_dir_one')
    assert ret == Path('~/tmp/flutils_test/test_dir_one')
    ret = path_create('~/tmp/flutils_test/test_dir_two')
    assert ret == Path('~/tmp/flutils_test/test_dir_two')

# Generated at 2022-06-13 20:59:49.298799
# Unit test for function directory_present
def test_directory_present():
    # Return a temporary directory.  This makes cleanup easier.
    TEST_DIR = Path('~/tmp/flutils.tests.pathutils.directory_present').expanduser()
    try:
        TEST_DIR.mkdir()
    except FileExistsError:
        pass

    test_path = TEST_DIR / 'directory_present.txt'

    if test_path.exists() is True:
        os.remove(test_path.as_posix())

    test_path.touch()

    try:
        directory_present(test_path)
    except FileExistsError:
        pass
    else:
        raise Exception('This should raise a FileExistsError.')
    finally:
        if test_path.exists() is True:
            os.remove(test_path.as_posix())



# Generated at 2022-06-13 21:00:01.384757
# Unit test for function chmod
def test_chmod():
    from tempfile import mkstemp
    from shutil import rmtree
    from flutils.testutils import TempDir
    from stat import S_IMODE
    from os import stat, remove

    def _test_chmod(path, mode_file, mode_dir):
        nonlocal test_path
        nonlocal test_mode_file
        nonlocal test_mode_dir
        chmod(path, mode_file, mode_dir)
        assert stat(test_path).st_mode == test_mode_file
        assert stat(test_dir).st_mode == test_mode_dir

    test_path = mkstemp(text=True)[1]
    test_dir = mkstemp(suffix='_', dir=TempDir.temporary_directory)[1]

    test_mode_file = 0o644
    test_mode

# Generated at 2022-06-13 21:00:04.158685
# Unit test for function chown
def test_chown():
    chown('~/tmp/flutils.tests.osutils.txt')



# Generated at 2022-06-13 21:00:16.421679
# Unit test for function path_absent
def test_path_absent():
    import shutil
    import tempfile

    dir_path = tempfile.mkdtemp()
    f_path = os.path.join(dir_path, 'foo')
    d_path = os.path.join(dir_path, 'dir_foo')
    link_path = os.path.join(dir_path, 'link_foo')

    # Test against an existing directory.
    assert os.path.isdir(dir_path) is True
    path_absent(dir_path)
    assert os.path.exists(dir_path) is False

    # Test against an existing file.

# Generated at 2022-06-13 21:00:27.399714
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown

    path = relpath('~/tmp/flutils.tests.osutils.txt')
    if path.exists():
        path.unlink()

    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
    assert path.exists()

    chown(path, user='root', group='root')
    assert path.owner() == 'root'
    assert path.group() == 'root'

    chown(path, user='foo', group='bar')
    assert path.owner() == 'foo'
    assert path.group() == 'bar'

    path.unlink()
    assert path.exists() is False

    path.parent.rmdir()
    assert path.parent.exists() is False



# Generated at 2022-06-13 21:00:39.942006
# Unit test for function chmod
def test_chmod():
    from warnings import catch_warnings
    from sys import getsizeof

    path = Path('tests/tmp/flutils.tests.osutils.txt')
    good_mode = getsizeof(path.stat().st_mode) * 8

    path.touch()
    chmod(path, 0o660)

    with catch_warnings(record=True) as warn:
        chmod(path, 0o641)

    err_msg = (
        'Failed to change the mode of the path: {}\n'
        '\tThe given mode: 0o641 is invalid.'
    )

    assert len(warn) == 1
    assert warn[0].category.name == 'UserWarning'
    assert warn[0].message.args[0] == err_msg.format(path)
    assert path.stat().st_mode == good

# Generated at 2022-06-13 21:00:43.235298
# Unit test for function chown
def test_chown():
    assert(chown('~/tmp/flutils.tests.osutils.txt') is None)



# Generated at 2022-06-13 21:00:52.747290
# Unit test for function chmod
def test_chmod():
    from operator import (
        lt,
        eq,
    )
    from os import (
        stat,
    )
    from stat import (
        S_IMODE,
    )

    import flutils.osutils
    from flutils.pathutils import (
        chmod,
    )

    p = flutils.osutils.mktemp()

    chmod(p, mode_file=0o660, mode_dir=0o770)
    assert eq(S_IMODE(stat(p).st_mode), 0o660) == True

    chmod(p, mode_file=0o644, mode_dir=0o775)
    assert eq(S_IMODE(stat(p).st_mode), 0o644) == True


# Generated at 2022-06-13 21:01:20.915822
# Unit test for function path_absent
def test_path_absent():
    import pytest
    import tempfile
    from flutils.pathutils import normalize_path
    from flutils.systemutils import current_os

    if current_os() == 'linux':
        user = getpass.getuser()
        path = '~/tmp/path_absent'
        path = normalize_path(path)
        path.mkdir(parents=True)
        path_foo = path / 'foo'
        path_foo.mkdir()
        path_bar = path_foo / 'bar'
        path_bar.mkdir()
        path_baz = path_bar / 'baz'
        path_baz.touch()
        path_baz_link = path_bar / 'baz_link'
        path_baz_link.symlink_to(path_baz)
        path

# Generated at 2022-06-13 21:01:21.765806
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:01:24.022521
# Unit test for function chown
def test_chown():
    chown(path='~/tmp/flutils.tests.osutils.txt')

# Generated at 2022-06-13 21:01:36.320821
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent

    # Test that function does not raise an exception for a broken link
    test_path = Path('./tmp/test_dir_absent')
    test_path.symlink_to('/does/not/exist/')
    path_absent(test_path)

    # Test that function does not raise an exception for a file
    test_path = Path('./tmp/test_dir_absent')
    test_path.touch()
    path_absent(test_path)

    # Test that function does not raise an exception for a directory
    test_path = Path('./tmp/test_dir_absent')
    test_path.mkdir(exist_ok=True, parents=True)
    path_absent(test_path)



# Generated at 2022-06-13 21:01:38.674375
# Unit test for function path_absent
def test_path_absent():
    from .tests.pathutils import _path_absent
    _path_absent()



# Generated at 2022-06-13 21:01:51.612474
# Unit test for function path_absent
def test_path_absent():
    from tempfile import mkdtemp
    tmp = mkdtemp()

# Generated at 2022-06-13 21:01:54.495337
# Unit test for function chown
def test_chown():
    assert 1 == 1
    # chown('~/tmp/**', user='foo', group='bar')
    # assert False

# Generated at 2022-06-13 21:02:05.167858
# Unit test for function directory_present
def test_directory_present():
    from random import randint
    from pathlib import PosixPath, WindowsPath

    path = PosixPath('/tmp/flutils-tests-directorypresent-%d' % randint(0, 1000))
    f = directory_present(path)
    assert f == path
    assert f.is_dir() is True
    f.rmdir()

    path = WindowsPath('C:\\flutils-tests-directorypresent-%d' % randint(0, 1000))
    f = directory_present(path)
    assert f == path
    assert f.is_dir() is True
    f.rmdir()



# Generated at 2022-06-13 21:02:05.830720
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:02:11.016867
# Unit test for function chmod
def test_chmod():
    path = '~/tmp/test.txt'
    chmod(path, 0o660)
    stat = os.stat(path)
    mode = stat.st_mode
    assert mode == (33152 | stat.S_IFREG)
    os.unlink(path)



# Generated at 2022-06-13 21:02:35.797173
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as

    assert exists_as('/dev') == 'directory'
    assert exists_as('/dev/null') == 'character device'
    assert exists_as('/dev/zero') == 'character device'
    assert exists_as('/dev/random') == 'character device'
    assert exists_as('/dev/urandom') == 'character device'
    assert exists_as('/proc') == 'directory'
    assert exists_as('/proc/cpuinfo') == 'file'
    assert exists_as('/proc/self/cmdline') == 'file'
    assert exists_as('/proc/self/status') == 'file'
    assert exists_as('/proc/self/exe') == 'file'
    assert exists_as('/proc/self/fd') == 'directory'


# Generated at 2022-06-13 21:02:46.812755
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    from flutils.systemutils import system_is_windows
    from tempfile import TemporaryDirectory

    with TemporaryDirectory(prefix='flutils.') as tmp:
        tmp_path = Path(tmp)
        if system_is_windows():
            dir_path = Path(tmp_path, 'test_dir')
            dir_path.mkdir()
            assert exists_as(dir_path) == 'directory'
            block_dev_path = Path(tmp_path, 'block_dev_path')
            block_dev_path.touch()
            assert exists_as(block_dev_path) == 'file'

            char_path = Path(tmp_path, 'char_path')
            char_path.touch()
            assert exists_as(char_path) == 'file'

            socket

# Generated at 2022-06-13 21:02:47.450354
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:02:49.434001
# Unit test for function chown
def test_chown():
    chown('.')
    os.chown('.', 123, 123)
    

# Generated at 2022-06-13 21:02:55.682360
# Unit test for function chown
def test_chown():
    import re
    import stat
    import tempfile
    from datetime import datetime
    from pathlib import Path
    from flutils.pathutils import path_absent, chown
    from flutils.pyutils import get_random_string

    user = getpass.getuser()
    group = grp.getgrgid(os.getgid()).gr_name

    with tempfile.TemporaryDirectory(prefix='flutils.tests.') as tmp_dir:
        # Testing chown of a Path
        file_path = Path(tmp_dir + '/test_chown.txt')
        file_path.write_text('Text')
        chown(file_path, user=user)
        assert user == get_os_user(os.stat(file_path.as_posix()).st_uid).pw_name

# Generated at 2022-06-13 21:03:09.143608
# Unit test for function chown
def test_chown():
    """Test for chown."""

    from unittest.mock import patch

    # pylint: disable=no-member
    with patch('os.chown') as mock_chown, \
            patch('flutils.pathutils.get_os_user') as mock_get_os_user, \
            patch('flutils.pathutils.get_os_group') as mock_get_os_group:

        mock_get_os_user.side_effect = lambda x: getpass.getpwnam(x)
        mock_get_os_group.side_effect = lambda x: grp.getgrnam(x)

        path = Path('~/tmp/flutils.tests.pathutils.txt')
        uid = getpass.getpwnam(getpass.getuser()).pw_uid
        g

# Generated at 2022-06-13 21:03:18.545537
# Unit test for function exists_as
def test_exists_as():
    def get_six_path_types():
        path_types = [
            Path('/tmp'),
            Path('/tmp').expanduser(),
            Path('/tmp').resolve(),
            Path(b'/tmp'),
            Path(b'/tmp').expanduser(),
            Path(b'/tmp').resolve(),
        ]

        if sys.platform == 'win32':
            path_types[0] = Path('C:\\temp')
            path_types[1] = Path('C:\\temp').expanduser()
            path_types[2] = Path('C:\\temp').resolve()
            path_types[3] = Path(b'C:\\temp')
            path_types[4] = Path(b'C:\\temp').expanduser()

# Generated at 2022-06-13 21:03:19.501814
# Unit test for function chmod
def test_chmod():
    assert True



# Generated at 2022-06-13 21:03:32.918727
# Unit test for function chown
def test_chown():
    import os
    import os.path
    import random
    import stat
    import string

    from flutils.pathutils import (
        chown
    )

    from . import core

    class TestTmpDir(core.TmpDir):
        """Temporary directory class for unit testing.

        Attributes:
            uid (:obj:`int`): The "user ID" of the current user.
            gid (:obj:`int`): The "group ID" of the current user.

        """

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.uid = os.stat(self.path).st_uid
            self.gid = os.getgid()


# Generated at 2022-06-13 21:03:42.414044
# Unit test for function path_absent
def test_path_absent():
    import pathlib

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = pathlib.Path(tmpdir)

        assert os.path.exists(tmpdir) is True
        path_absent(tmpdir)
        assert os.path.exists(tmpdir) is False

        tmpdir = tmpdir / 'dir_one'
        tmpdir.mkdir()
        assert os.path.exists(tmpdir) is True
        path_absent(tmpdir)
        assert os.path.exists(tmpdir) is False

        tmpdir = tmpdir / 'dir_one'
        tmpdir.mkdir()
        assert os.path.exists(tmpdir) is True
        path_absent(tmpdir)
        assert os.path.exists(tmpdir) is False

        tmpfile = tmp