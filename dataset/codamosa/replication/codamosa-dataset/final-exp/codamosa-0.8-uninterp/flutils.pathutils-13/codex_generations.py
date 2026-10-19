

# Generated at 2022-06-13 20:54:04.826868
# Unit test for function chmod
def test_chmod():
    assert callable(chmod)
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)
    tmpdir = Path('~/tmp/flutils.tests/osutils/')
    with tmpdir.mkdir('osutils'):
        Path().mkdir('tmp')

    chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770)



# Generated at 2022-06-13 20:54:10.404077
# Unit test for function directory_present
def test_directory_present():
    from os import PathLike
    from pathlib import (
        Path,
        PosixPath,
        WindowsPath,
    )
    from typing import Union

    _PATH = Union[
        PathLike,
        PosixPath,
        WindowsPath,
        bytes,
        str,
    ]

    path = directory_present('~/tmp/flutils.tests.osutils.txt')
    assert isinstance(path, Path) is True
    path = directory_present('~/tmp/flutils.tests.osutils.txt', user='-1')
    assert isinstance(path, Path) is True
    path = directory_present('~/tmp/flutils.tests.osutils.txt', user='foo')
    assert isinstance(path, Path) is True

# Generated at 2022-06-13 20:54:23.303219
# Unit test for function chmod
def test_chmod():
    from stat import S_IMODE

    from flutils.pathutils import chmod

    assert S_IMODE(os.stat('README.rst').st_mode) == 0o644
    assert S_IMODE(os.stat('setup.py').st_mode) == 0o644

    chmod('README.rst', 0o660)
    chmod('setup.py', 0o660)

    assert S_IMODE(os.stat('README.rst').st_mode) == 0o660
    assert S_IMODE(os.stat('setup.py').st_mode) == 0o660

    chmod('README.rst', 0o644)
    chmod('setup.py', 0o644)

    assert S_IMODE(os.stat('README.rst').st_mode) == 0

# Generated at 2022-06-13 20:54:33.327047
# Unit test for function chown
def test_chown():
    import os
    from flutils.pathutils import chown, get_os_group, get_os_user
    from flutils.pyutils import mkdtemp
    from os import (
        PathLike,
        posix_fadvise,
        stat,
    )
    from os.path import join
    from stat import ST_MODE
    from tempfile import mkstemp
    from typing import (
        cast,
        Deque,
        Generator,
    )
    from unittest import TestCase

    from hypothesis import (
        assume,
        given,
        settings,
    )
    from hypothesis.strategies import (
        binary,
        integers,
        sampled_from,
    )
    from hypothesis_jsonschema import from_schema


# Generated at 2022-06-13 20:54:38.982629
# Unit test for function directory_present
def test_directory_present():
    func = functools.partial(
        directory_present, mode=0o700, user='0', group='0'
    )
    assert func('./{{cookiecutter.package_name}}/data/tmp')
    assert func('./{{cookiecutter.package_name}}/data/tmp/')



# Generated at 2022-06-13 20:54:43.627664
# Unit test for function find_paths
def test_find_paths():
    """
    :return:
    """
    for path in find_paths('~/tmp/*'):
        assert 'tmp' in path.as_posix()
        print(path)



# Generated at 2022-06-13 20:54:49.804450
# Unit test for function exists_as
def test_exists_as():
    """Test for flutils.pathutils.exists_as()"""
    from flutils.pathutils import directory_present

    path = '/var/folders/tmp/flutils.tests.pathutils.test_exists_as'
    directory_present(path)
    assert exists_as(path) == 'directory'
    assert exists_as('/root') == 'directory'



# Generated at 2022-06-13 20:54:58.064270
# Unit test for function exists_as
def test_exists_as():
    """Test for function exists_as"""
    from flutils.pathutils import exists_as

    # Test for non-existent path
    from unittest.mock import patch
    with patch("os.listdir") as mock_listdir:
        mock_listdir.side_effect = FileNotFoundError
        assert exists_as("/tmp/flutils.tests.osutils.not_exist") == ''
    # Test for is_dir() path
    with patch("os.path.isdir") as mock_isdir:
        mock_isdir.return_value = True
        assert exists_as("/tmp/flutils.tests.osutils.dir") == "directory"
    # Test for is_file() path

# Generated at 2022-06-13 20:55:05.467822
# Unit test for function chmod
def test_chmod():
    """Test function ``chmod``."""

    import os
    import stat
    from shutil import rmtree
    from tempfile import mkdtemp

    os.umask(0o22)

    path = mkdtemp()

    Path(f'{path}/foo.txt').touch()
    Path(f'{path}/bar.txt').touch()

    # Test recursive chmod
    chmod(f'{path}/**', mode_file=0o644, mode_dir=0o770)

    assert stat.S_IMODE(os.lstat(path).st_mode) == 0o770
    assert stat.S_IMODE(os.lstat(f'{path}/foo.txt').st_mode) == 0o644

# Generated at 2022-06-13 20:55:16.713225
# Unit test for function chmod
def test_chmod():
    test_path = '~/tmp/flutils.tests.osutils.txt'
    if Path(test_path).exists() is True:
        Path(test_path).unlink()

    Path(test_path).touch()

    if Path(test_path).is_file() is False:
        raise ValueError(f'Test file {test_path} is not a file.')
    elif Path(test_path).exists() is False:
        raise ValueError(f'Test file {test_path} does not exist.')

    assert Path(test_path).stat().st_mode & 0o777 == 0o600, (
        f'Default mode is not 0o600!')
    chmod(test_path, 0o660)
    assert Path(test_path).stat().st_mode & 0o777 == 0

# Generated at 2022-06-13 20:55:35.252094
# Unit test for function chown
def test_chown():
    normalize_path('~/')


# Generated at 2022-06-13 20:55:44.047848
# Unit test for function chmod
def test_chmod():
    with tempfile.TemporaryDirectory() as tmpdir:
        txt = Path(tmpdir) / 'flutils.tests.osutils.txt'
        txt.touch()

        assert txt.exists() is True
        assert stat.S_IMODE(txt.stat().st_mode) == 0o600

        chmod(txt.as_posix(), 0o660)
        assert stat.S_IMODE(txt.stat().st_mode) == 0o660

        chmod(txt.as_posix(), 0o530)
        assert stat.S_IMODE(txt.stat().st_mode) == 0o530

        chmod(txt.as_posix(), 0o700)
        assert stat.S_IMODE(txt.stat().st_mode) == 0o700


# Generated at 2022-06-13 20:55:58.893436
# Unit test for function chown
def test_chown():
    from tempfile import TemporaryDirectory
    from .deps import make_file
    from .deps import make_dir

    with TemporaryDirectory(prefix='flutils_') as tmp_directory:
        tmp_directory = Path(tmp_directory)
        tmp_file = cast(Path, Path(tmp_directory) / 'foo.txt')
        make_file(tmp_file)
        make_dir(tmp_directory / 'bar')
        chown(tmp_directory)
        chown(tmp_file)

        current_user = getpass.getuser()
        current_group = grp.getgrgid(os.getgid()).gr_name
        assert os.stat(tmp_directory).st_uid == os.getuid()
        assert os.stat(tmp_directory).st_gid == os.getgid()
       

# Generated at 2022-06-13 20:56:04.104474
# Unit test for function find_paths
def test_find_paths():
    assert list(find_paths('~/tmp/*')) == [
        Path('/home/test_user/tmp/file_one'),
        Path('/home/test_user/tmp/dir_one'),
    ]



# Generated at 2022-06-13 20:56:10.635727
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp/flutils.tests/exists_as') == 'file'
    assert exists_as('~/tmp/flutils.tests/osutils/directory') == 'directory'
    assert exists_as('~/tmp/flutils.tests/osutils/fifo') == "FIFO"


# Generated at 2022-06-13 20:56:14.553053
# Unit test for function chmod
def test_chmod():
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)
    chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770)
    chmod('~/tmp/*')

# Generated at 2022-06-13 20:56:15.367882
# Unit test for function path_absent
def test_path_absent(): pass



# Generated at 2022-06-13 20:56:27.299387
# Unit test for function exists_as
def test_exists_as():
    """Test the function flutils.pathutils.exists_as."""
    import pathlib

    test_path_str = 'flutils.tests.osutils.txt'
    test_path = pathlib.Path(test_path_str)

    assert exists_as(test_path) == 'file'
    assert exists_as(test_path_str) == 'file'

    # Ensure we get the same results from a symlink to the file.
    os.symlink(test_path_str, 'flutils.tests.osutils.link')
    assert exists_as('flutils.tests.osutils.link') == 'file'

    # Ensure we get the same results when we use an invalid path.
    assert exists_as('/tmp/flutils/tests/osutils') == ''


# Generated at 2022-06-13 20:56:37.779614
# Unit test for function find_paths
def test_find_paths():
    from pathlib import PosixPath, WindowsPath
    from typing import List

    case_one_paths = sorted(
        [
            PosixPath('/home/test_user/tmp/file_one'),
            PosixPath('/home/test_user/tmp/dir_one')
        ]
    )

    case_one = sorted(
        find_paths('/home/test_user/tmp/*')
    )

    case_two_paths = sorted(
        [
            WindowsPath('C:/Users/test_user/tmp/file_one'),
            WindowsPath('C:/Users/test_user/tmp/dir_one')
        ]
    )

    case_two = sorted(
        find_paths('C:/Users/test_user/tmp/*')
    )

    assert type(case_one)

# Generated at 2022-06-13 20:56:49.748291
# Unit test for function path_absent
def test_path_absent():
    import pathlib
    from flutils import pathutils
    with pathutils.temp_dir() as tmp_dir:
        # Testing path_absent on file.
        file_name = tmp_dir / 'file_one'
        file_name.write_text('foo')
        pathutils.path_absent(file_name)
        assert not file_name.exists()
        # Testing path_absent on directory
        dir_name = tmp_dir / 'dir_one'
        dir_name.mkdir(parents=True, exist_ok=True)
        file_one = dir_name / 'file_one'
        file_one.write_text('foo')
        file_two = dir_name / 'file_two'
        file_two.write_text('foo')

# Generated at 2022-06-13 20:57:11.333821
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    from flutils import create_test_file
    create_test_file(path='/tmp/test_chmod.txt')
    chmod(path='/tmp/test_chmod.txt', mode_file=0o660, mode_dir=0o770)
    assert os.stat('/tmp/test_chmod.txt').st_mode == 33152

# Generated at 2022-06-13 20:57:15.441475
# Unit test for function exists_as
def test_exists_as():
    expected = 'directory'
    result = exists_as(get_tmp_dir())
    split_line = ('-' * 75)
    print(split_line)
    print('Testing: exists_as()')
    print("Expected: %s" % repr(expected))
    print("Result: %s" % repr(result))
    print(split_line)
    assert expected == result



# Generated at 2022-06-13 20:57:23.336129
# Unit test for function get_os_user
def test_get_os_user():
    """Test the :obj:`~flutils.pathutils.get_os_user` function."""
    try:
        from flutils.pathutils import get_os_user
    except ImportError:
        return
    with pytest.raises(OSError):
        get_os_user(1000000)
    with pytest.raises(OSError):
        get_os_user('gargabe')
    get_os_user()



# Generated at 2022-06-13 20:57:28.149131
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/') == 'directory'
    assert exists_as('~/tmp/') == 'directory'
    assert exists_as('/etc') == 'directory'

    if os.path.exists('/etc/hosts'):
        assert exists_as('/etc/hosts') == 'file'


# Generated at 2022-06-13 20:57:30.604380
# Unit test for function directory_present
def test_directory_present():
    result = directory_present(path='~/foo/bar/baz')
    assert isinstance(result, Path)



# Generated at 2022-06-13 20:57:42.643574
# Unit test for function chown
def test_chown():
    from . import osutils

    path = Path(osutils.TEST_FILE)
    if path.exists():
        path.unlink()

    assert Path(osutils.TEST_FILE).exists() is False

    osutils.create_file(path)

    assert Path(osutils.TEST_FILE).exists() is True

    chown(path, user='apache')

    assert path.stat().st_uid == get_os_user('apache').pw_uid

    chown(path, group='apache')

    assert path.stat().st_gid == get_os_group('apache').gr_gid

    chown(path, user=0, group=0)

    assert path.stat().st_uid == 0
    assert path.stat().st_gid == 0


# Generated at 2022-06-13 20:57:55.711950
# Unit test for function chown
def test_chown():
    import os
    import random
    import string
    import tempfile

    # Don't following the symlinks so we can test
    # the actual permissions set on the file.
    path = tempfile.mkdtemp(dir='/tmp', prefix='flutils_tests_')
    os.chmod(path, 0o755)
    os.chown(path, -1, -1)

    # Test normal operations:
    path = os.path.join(path, 'test_chown_normal.txt')
    with open(path, 'w') as f:
        f.write("test_chown")

    os.chmod(path, 0o600)

    current_user = getpass.getuser()
    current_group = getpass.getuser()

    os.chown(path, current_user, current_group)

# Generated at 2022-06-13 20:58:07.455393
# Unit test for function directory_present
def test_directory_present():
    from os import chdir
    import shutil
    from tempfile import TemporaryDirectory

    from flutils.pathutils import directory_present
    from flutils.testingutils import cd, env_var

    with TemporaryDirectory() as tmpdir:
        chdir(tmpdir)
        assert os.getcwd() == tmpdir
        p = directory_present('test_dir_1', 0o777)
        assert p.stat().st_mode == 16832
        p = directory_present('test_dir_2', 0o777, '-1', '-1')
        assert p.stat().st_mode == 16832
        p = directory_present('test_dir_3', 0o777, '-1', '-1')
        assert p.stat().st_mode == 16832

# Generated at 2022-06-13 20:58:11.421556
# Unit test for function chmod
def test_chmod():
    chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770)
    assert True
    chmod('~/tmp/*')
    assert True
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)



# Generated at 2022-06-13 20:58:24.559558
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import find_paths
    from flutils.pathutils import path_absent
    from pathlib import Path
    from shutil import rmtree
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        path = tmp / 'test_path'
        path.touch()
        path_absent(path)

        assert not os.path.exists(path)

        path.mkdir()
        path_absent(path)
        assert not os.path.exists(path)

        path.mkdir()
        (path / 'file_one').touch()
        (path / 'file_two').touch()
        (path / 'dir_one').mkdir()
        (path / 'dir_two').mkdir()

# Generated at 2022-06-13 20:58:35.000517
# Unit test for function chown
def test_chown():
    pass


# Generated at 2022-06-13 20:58:41.178822
# Unit test for function path_absent
def test_path_absent():
    """Test the :obj:`flutils.pathutils.path_absent` function."""
    # Create the directories and files to delete.
    tmp_dir = Path(tempfile.gettempdir())
    tmp_path = tmp_dir / 'flutils_test_path_absent'
    tmp_path.mkdir(mode=0o700, exist_ok=True)
    tmp_path_file = tmp_path / 'flutils_test_path_absent_file'
    tmp_path_file.touch(mode=0o600)
    tmp_path2 = tmp_path / 'flutils_test_path_absent_dir'
    tmp_path2.mkdir(mode=0o700, exist_ok=True)

# Generated at 2022-06-13 20:58:50.700709
# Unit test for function directory_present
def test_directory_present():
    with temporary_dir() as tmpdir:
        path = Path(tmpdir) / 'testpath'
        assert not path.exists()
        directory_present(path)
        assert path.exists()
        assert path.is_dir()
        assert path.stat().st_mode == 0o700

        # Changing the "login name" of the current user
        # does not affect the user of the path since the
        # current user's "login name" is used by deafult.
        user = getpass.getuser()
        old_group = grp.getgrgid(os.getgid()).gr_name

        group = old_group if old_group != 'staff' else 'wheel'
        directory_present(path, group=group)

# Generated at 2022-06-13 20:58:55.755289
# Unit test for function path_absent
def test_path_absent():
    # noinspection PyTypeChecker

    path = Path('~/tmp/test_path')
    assert normalize_path(path) == normalize_path('~/tmp/test_path')

    transformed_path = path_absent('~/tmp/test_path')
    assert transformed_path is None



# Generated at 2022-06-13 20:59:05.341671
# Unit test for function path_absent
def test_path_absent():
    try:
        os.unlink('/tmp/flutils_test_path_absent_1')
    except FileNotFoundError:
        pass
    try:
        os.rmdir('/tmp/flutils_test_path_absent_2')
    except FileNotFoundError:
        pass
    os.mkdir('/tmp/flutils_test_path_absent_2')
    with open('/tmp/flutils_test_path_absent_2/flutils_test_file.txt', 'w') as f:
        f.write('Test file')
    path_absent('/tmp/flutils_test_path_absent_1')
    path_absent('/tmp/flutils_test_path_absent_2')

# Generated at 2022-06-13 20:59:12.274294
# Unit test for function chmod
def test_chmod():
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    path = Path(temp_dir.name) / 'flutils.tests.chmod.txt'
    path.touch()
    chmod(path, 0o660)
    mode = path.stat().st_mode
    if mode != 33152:
        raise AssertionError
    path.chmod(0o777)
    temp_dir.cleanup()
    return True



# Generated at 2022-06-13 20:59:18.908571
# Unit test for function exists_as
def test_exists_as():
    from .test_data import test_file, test_dir
    assert exists_as(test_file) == 'file'
    assert exists_as(test_dir) == 'directory'
    assert exists_as(test_dir + '__does_not_exist__') == ''
    assert exists_as(test_file + '__does_not_exist__') == ''



# Generated at 2022-06-13 20:59:25.155405
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~') == 'directory'
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/flutils.tests.osutils.txt') == 'file'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/sda1') == 'block device'
    assert exists_as('/dev/sda') == 'block device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/pts/2') == 'char device'
    assert exists

# Generated at 2022-06-13 20:59:38.574288
# Unit test for function chmod
def test_chmod():
    """Test flutils.pathutils.chmod."""
    import os
    import stat

    # Create a file and write a file to it.
    test_path = Path('/tmp/flutils.tests.osutils.txt')
    test_path.touch()
    test_path.write_text('foo')
    if test_path.exists() is False:
        raise Exception('test_path not found!')

    # Test setting a file's mode.
    chmod(test_path, mode_file=0o660)
    assert stat.S_IMODE(os.lstat(test_path).st_mode) == 0o660

    # Test setting the mode of directories.
    chmod(test_path.parent, mode_dir=0o770)

# Generated at 2022-06-13 20:59:43.806908
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import normalize_path

    path = normalize_path('~/tmp')
    path.mkdir()
    assert exists_as(path) == 'directory'

    file_path = normalize_path('~/tmp/test_exists_as.txt')
    file_path.touch()
    assert exists_as(file_path) == 'file'

    path.rmdir()

test_exists_as()



# Generated at 2022-06-13 21:00:02.164650
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import directory_present
    from flutils.tests.common import (
        TEST_FILE_PATH,
        TEST_DIR_PATH,
        TEST_SYMLINK_FILE_PATH,
        TEST_SYMLINK_DIR_PATH,
    )

    # Function cannot be run as root.
    if getpass.getuser() == 'root':
        return

    # Normal operation
    result = directory_present(TEST_DIR_PATH)
    assert isinstance(result, Path)
    assert result.is_dir()
    assert result.as_posix() == TEST_DIR_PATH

    # Normal operation doesn't need to create a new path.
    result = directory_present(TEST_DIR_PATH)
    assert isinstance(result, Path)
    assert result.is_dir()

# Generated at 2022-06-13 21:00:15.240350
# Unit test for function chown
def test_chown():
    from tempfile import TemporaryDirectory
    from unittest import TestCase
    from unittest.mock import Mock, patch

    _path_obj = Mock()
    _path_obj.is_dir.return_value = True
    _path_obj.is_file.return_value = False
    _path_obj.as_posix.return_value = '/path/to/glob/**'

    with TemporaryDirectory() as tmp_dir:
        tmp_dir_obj = Path(tmp_dir)
        tmp_dir_obj.mkdir(
            mode=0o770,
            parents=True
        )

        glob_return = [
            str(tmp_dir_obj.joinpath('one')),
            str(tmp_dir_obj.joinpath('two'))
        ]

        # Create a mock of the glob.

# Generated at 2022-06-13 21:00:24.137544
# Unit test for function exists_as
def test_exists_as():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir) / 'test_dir'
        assert exists_as(dir_path) == ''
        dir_path.mkdir()
        assert exists_as(dir_path) == 'directory'
        file_path = Path(tmpdir) / 'test_file'
        assert exists_as(file_path) == ''
        file_path.touch()
        assert exists_as(file_path) == 'file'
        block_dev_path = Path(tmpdir) / 'test_block_dev'
        assert exists_as(block_dev_path) == ''
        block_dev_path.touch()
        assert exists_as(block_dev_path) == 'file'

# Generated at 2022-06-13 21:00:30.605089
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    from flutils.systemutils import get_umask

    umask = get_umask(0o0777)
    chown('~/tmp/flutils.tests.osutils.txt')
    os.unlink('~/tmp/flutils.tests.osutils.txt')



# Generated at 2022-06-13 21:00:33.041248
# Unit test for function chown
def test_chown():
    """ Test chown """
    pass


# Generated at 2022-06-13 21:00:44.220444
# Unit test for function exists_as
def test_exists_as():
    from os import mkfifo
    from pathlib import Path
    from tempfile import mkdtemp
    from unittest import TestCase

    class TestExistsAs(TestCase):
        def setUp(self):
            self.test_dir = Path(mkdtemp())

        def tearDown(self):
            if self.test_dir.exists():
                self.test_dir.rmdir()

        def test_exists_as(self):
            test_path = self.test_dir.joinpath(
                'flutils.tests.pathutils.test_exists_as'
            )
            self.assertEqual(exists_as(test_path), '')
            test_path.touch()
            self.assertEqual(exists_as(test_path), 'file')
            test_path.un

# Generated at 2022-06-13 21:00:52.990998
# Unit test for function path_absent
def test_path_absent():
    import time
    from flutils.pathutils import find_paths
    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as temp_path:
        root_path = Path(temp_path)
        file_path = root_path / 'file_one'
        file_path.touch()
        assert file_path.exists()

        dir_path = root_path / 'dir_one'
        dir_path.mkdir()
        sub_path = dir_path / 'file_two'
        sub_path.touch()
        assert sub_path.exists()

        path_absent(root_path)
        assert not root_path.exists()
        assert not file_path.exists()
        assert not sub_path.exists()


# Generated at 2022-06-13 21:00:53.786493
# Unit test for function path_absent
def test_path_absent():
    assert False

# Generated at 2022-06-13 21:01:02.668651
# Unit test for function chmod
def test_chmod():
    """Unit test for function chmod
    """
    target_path = Path('flutils.tests.osutils')
    target_path.mkdir(mode=0o700, parents=True, exist_ok=True)

    target_file = Path('flutils.tests.osutils.txt')
    target_file.touch(mode=0o600)

    assert target_path.exists() is True
    assert target_file.exists() is True

    assert target_path.stat().st_mode == 16832
    assert target_file.stat().st_mode == 33152

    chmod(target_path, mode_file=0o644, mode_dir=0o770)

    assert target_path.stat().st_mode == 40700
    assert target_file.stat().st_mode == 33152


# Generated at 2022-06-13 21:01:12.905790
# Unit test for function chmod
def test_chmod():
    """Unit test for function chmod."""
    import pytest
    import tempfile

    test_file_paths = [
        (tempfile.NamedTemporaryFile().name, '0o600'),
        (tempfile.mkdtemp(), '0o700'),
    ]

    try:
        for path, expected_mode in test_file_paths:
            yield (
                _run_test_chmod,
                path,
                0o600,
                0o700,
                expected_mode,
            )
    finally:
        for path, _expected_mode in test_file_paths:
            try:
                os.remove(path)
            except IsADirectoryError:
                os.rmdir(path)

# Generated at 2022-06-13 21:01:36.601767
# Unit test for function chmod
def test_chmod():
    import os
    import os.path
    import pathlib
    import tempfile

    from flutils.pathutils import chmod

    tmp_dir = tempfile.mkdtemp()

    # A PosixPath.
    path = pathlib.PosixPath(tmp_dir) / 'flutils.tests.osutils.txt'
    with path.open(mode='w') as f:
        f.write('test_chmod')

    assert os.path.isfile(path) is True
    assert os.stat(path).st_mode == 33188
    chmod(path, 0o660)
    assert os.stat(path).st_mode == 33188

    # A Path object.
    path = pathlib.Path(tmp_dir) / 'flutils.tests.osutils.txt'

# Generated at 2022-06-13 21:01:37.633423
# Unit test for function path_absent
def test_path_absent():
    return



# Generated at 2022-06-13 21:01:50.639282
# Unit test for function chmod
def test_chmod():
    import tempfile
    import shutil
    import stat

    tmpd = tempfile.mkdtemp(prefix='flutils_test.')
    tmpf = f'{tmpd}/tmpfile'
    tmpf2 = f'{tmpd}/tmpfile2'
    open(tmpf, 'a').close()
    open(tmpf2, 'a').close()

    mode_file = 0o666
    mode_dir = 0o777

    chmod(tmpf, mode_file=mode_file)
    chmod(tmpf2, mode_file=mode_file, include_parent=True)

    assert stat.S_IMODE(os.lstat(tmpf).st_mode) == mode_file
    assert stat.S_IMODE(os.lstat(tmpf2).st_mode) == mode_

# Generated at 2022-06-13 21:01:59.183840
# Unit test for function chown
def test_chown():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        with open(os.path.join(tmp_dir_name, 'test.txt'), 'w') as tmp_file:
            file_path = tmp_file.name
            username = pwd.getpwuid(os.stat(file_path).st_uid).pw_name
            groupname = grp.getgrgid(os.stat(file_path).st_gid).gr_name
            chown(file_path)
            assert username == pwd.getpwuid(os.stat(file_path).st_uid).pw_name
            assert groupname == grp.getgrgid(os.stat(file_path).st_gid).gr_name

# Generated at 2022-06-13 21:02:12.492113
# Unit test for function chown
def test_chown():
    user = getpass.getuser()
    group = grp.getgrgid(os.getgid())
    group = group.gr_name
    directory_present('/tmp/flutils.tests.osutils.test_chown/')
    chown('/tmp/flutils.tests.osutils.test_chown/**',
          user='-1',
          group='-1')
    chown('/tmp/flutils.tests.osutils.test_chown/**',
          user='-1',
          group=group)
    chown('/tmp/flutils.tests.osutils.test_chown/**',
          user=user,
          group='-1')
    chown('/tmp/flutils.tests.osutils.test_chown/**',
          user=user,
          group=group)

# Generated at 2022-06-13 21:02:23.531766
# Unit test for function chmod
def test_chmod():
    realpath = os.path.realpath(__file__)
    thisdir = os.path.dirname(realpath)
    path = os.path.join(thisdir, 'testfile')
    try:
        os.remove(path)
    except OSError:  # pragma: no cover
        pass

    try:
        with open(path, 'w') as f:
            f.write('somedata')
        assert os.access(path, os.W_OK) is True

        chmod(path, 0o444)
        assert os.access(path, os.W_OK) is False

    finally:
        os.remove(path)



# Generated at 2022-06-13 21:02:35.856367
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    from flutils.textutils import create_temp_file
    from tempfile import TemporaryDirectory

    tmpdir = TemporaryDirectory()

    with create_temp_file(name=f'{tmpdir.name}/test_chmod_1.txt', text='1') as fp:
        chmod(fp.name)
        assert fp.stat().st_mode == 0o600

    with create_temp_file(name=f'{tmpdir.name}/test_chmod_2.txt', text='1') as fp:
        chmod(fp.name, mode_file=0o666)
        assert fp.stat().st_mode == 0o666


# Generated at 2022-06-13 21:02:47.804813
# Unit test for function chown
def test_chown():
    import os
    import pathlib
    import sys

    if sys.platform == 'win32':
        os.system('net localgroup Administrators flutils /delete')
        return
    elif sys.platform == 'darwin':
        os.system('dscl . -list /Users UniqueID | grep flutils')
        return
    else:
        os.system('userdel --force flutils')

    os.system('groupadd --system flutils')

    os.system('useradd --system --gid flutils --no-create-home --shell /bin/false --comment "flutils testing user" flutils')
    os.system('usermod -a -G flutils flutils')

    try:
        file = pathlib.Path('/tmp/flutils_test_chown')
        file.touch()
    finally:
        os

# Generated at 2022-06-13 21:02:55.606771
# Unit test for function chown
def test_chown():
    # Should return None
    assert chown('/tmp/flutils.pathutils.chown.txt') is None
    # Should raise OSError
    try:
        chown('/tmp/flutils.pathutils.chown.txt', user='nobody')
    except OSError:
        pass
    else:
        raise AssertionError('OSError not raised')
    # Should raise OSError
    try:
        chown('/tmp/flutils.pathutils.chown.txt', group='nobody')
    except OSError:
        pass
    else:
        raise AssertionError('OSError not raised')
    # Should return None
    assert chown('/tmp/flutils.pathutils.chown.txt', user='root', group='root') is None



# Generated at 2022-06-13 21:03:08.773287
# Unit test for function exists_as
def test_exists_as():
    """
    :return:
    """
    # Path does not exist
    assert exists_as('~/does_NOT_exist') == ''

    # Path is a directory
    assert exists_as('~/does_NOT_exist_dir') == 'directory'

    # Path is a file
    assert exists_as('~/does_NOT_exist_file') == 'file'

    # Path is a block device
    assert exists_as('~/does_NOT_exist_block_device') == 'block device'

    # Path is a char device
    assert exists_as('~/does_NOT_exist_char_device') == 'char device'

    # Path is a FIFO
    assert exists_as('~/does_NOT_exist_fifo') == 'FIFO'

    # Path is a socket
    assert exists_

# Generated at 2022-06-13 21:03:37.835855
# Unit test for function chown
def test_chown():
    # test_chown
    pass
