

# Generated at 2022-06-13 20:54:18.629313
# Unit test for function exists_as
def test_exists_as():
    file_path = Path().home() / 'tmp' / 'test.txt'
    dir_path = Path().home() / 'tmp' / 'test_dir'
    Path().home().mkdir()
    Path().home() / 'tmp'.mkdir()

    if file_path.is_file() is True:
        file_path.unlink()

    if dir_path.is_dir() is False:
        dir_path.mkdir()

    new_file_path = Path().home() / 'tmp' / 'new.txt'
    new_file_path.touch()

    new_dir_path = Path().home() / 'tmp' / 'new_dir'
    new_dir_path.mkdir()

    new_fifo_path = Path().home() / 'tmp' / 'newfifo'

# Generated at 2022-06-13 20:54:26.678154
# Unit test for function directory_present
def test_directory_present():
    """Test directory_present."""
    from tempfile import gettempdir
    tmpdir = Path(gettempdir())

# Generated at 2022-06-13 20:54:33.108677
# Unit test for function find_paths
def test_find_paths():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        tmp_dir = Path(tmpdir)
        tmp_file = tmp_dir.joinpath('file_one')
        tmp_file.touch()
        tmp_dir2 = tmp_dir.joinpath('dir_one')
        tmp_dir2.mkdir()

        paths: List[Path] = list(find_paths(tmp_dir.joinpath('*')))
        assert len(paths) == 2
        assert tmp_file in paths
        assert tmp_dir2 in paths



# Generated at 2022-06-13 20:54:34.290339
# Unit test for function get_os_user
def test_get_os_user():
    assert get_os_user('root').pw_uid == 0
    assert get_os_user().pw_name == getpass.getuser()



# Generated at 2022-06-13 20:54:38.513259
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/') == 'directory'
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/flutils.tmp.txt') == 'file'
    assert exists_as('~/tmp/flutils.tmp.txt2') == ''



# Generated at 2022-06-13 20:54:52.139409
# Unit test for function directory_present
def test_directory_present():
    test_path = Path('~/tmp/test_path/bar').expanduser()
    assert test_path == directory_present(test_path)
    assert test_path.exists()
    assert test_path.is_dir()

    test_path = Path('~/tmp/test_path_1')
    parent = test_path.parent
    assert exists_as(parent) == 'directory'
    assert exists_as(parent) != 'directory'
    assert parent == directory_present(test_path)
    assert parent.exists()

    test_path = Path('~/tmp/test_path_2')
    parent = parent.parent
    assert exists_as(parent) == 'directory'
    assert parent == directory_present(test_path)
    assert parent.exists()

    # Cause an exception.
   

# Generated at 2022-06-13 20:54:59.277350
# Unit test for function find_paths
def test_find_paths():
    """Test :func:`~flutils.pathutils.find_paths` function."""
    from flutils_tests.helpers import captured_output
    with captured_output() as (out, err):
        paths = list(find_paths('~/tmp/*'))

    assert len(paths) == 2
    assert paths[0].is_file()
    assert paths[1].is_dir()

    with captured_output() as (out, err):
        paths = list(find_paths('~/tmp/file*'))

    assert len(paths) == 1
    assert paths[0].is_file()

    with captured_output() as (out, err):
        paths = list(find_paths('~/tmp/dir*'))

    assert len(paths) == 1

# Generated at 2022-06-13 20:55:00.591141
# Unit test for function chown
def test_chown():
    return 'Use a unit test library to check this function.'



# Generated at 2022-06-13 20:55:02.655217
# Unit test for function chmod
def test_chmod():
    assert chmod() == None
# chmod()



# Generated at 2022-06-13 20:55:07.013959
# Unit test for function find_paths
def test_find_paths():
    path = Path(__file__).parent.joinpath('file_one')
    pattern = str(path).replace('file_one', '*')
    assert str(next(find_paths(pattern))) == str(path)



# Generated at 2022-06-13 20:55:26.268498
# Unit test for function exists_as
def test_exists_as():
    # Test for non existent path
    assert exists_as(Path('/this/path/does/not/exist')) == ''
    # Test for the case that the path is a directory
    assert exists_as(Path(__file__).parent) == 'directory'
    # Test for the case that the path is a file
    assert exists_as(Path(__file__)) == 'file'



# Generated at 2022-06-13 20:55:28.004375
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(__file__) == 'file'
    assert exists_as('/dev/null') == 'char device'



# Generated at 2022-06-13 20:55:31.430267
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/doesnotexist') == ''
    assert exists_as(__file__) == 'file'
    assert exists_as(Path(__file__)) == 'file'
    assert exists_as(__name__) == 'file'
    assert exists_as(Path(__name__)) == 'file'
    assert exists_as('.') == 'directory'
    assert exists_as(Path('.')) == 'directory'



# Generated at 2022-06-13 20:55:42.638515
# Unit test for function chmod
def test_chmod():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    import stat

    with TemporaryDirectory() as tmpdir:
        # create file and directories
        Path(tmpdir, 'a.txt').touch()
        Path(tmpdir, 'b', 'c', 'd.txt').touch()
        Path(tmpdir, 'b', 'c', 'e.txt').touch()

        # set modes on all files and directories
        chmod(Path(tmpdir, '*'), mode_file=0o600, mode_dir=0o700)
        chmod(Path(tmpdir, 'b', '*'), mode_file=0o600, mode_dir=0o700)
        chmod(Path(tmpdir, 'b', 'c', '*'), mode_file=0o600, mode_dir=0o700)

        # assert

# Generated at 2022-06-13 20:55:45.292012
# Unit test for function exists_as
def test_exists_as():
    """Tests for function exists_as."""
    assert exists_as('~/tmp/flutils.tests.osutils.txt') == 'file'
    assert exists_as('~/tmp/flutils.tests.osutils') == 'directory'
    assert exists_as('~/tmp/flutils.tests.osutils.txt_does_not_exist') == ''



# Generated at 2022-06-13 20:55:48.124696
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/foo') == ''



# Generated at 2022-06-13 20:56:01.392961
# Unit test for function chmod

# Generated at 2022-06-13 20:56:03.207587
# Unit test for function chmod
def test_chmod():
    assert 'CHANGE ME' == 'test'

# Generated at 2022-06-13 20:56:05.554056
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(__file__) == 'file'
    assert exists_as(Path.cwd()) == 'directory'



# Generated at 2022-06-13 20:56:14.907469
# Unit test for function exists_as
def test_exists_as():
    from . import osutils
    from .pathutils import exists_as

    tmp_path = osutils.get_tempfile_path('tmp_exists_as',
                                         parent_path='~/tmp')
    with open(tmp_path.as_posix(), 'w') as f:
        f.write('')

    assert exists_as(tmp_path) == 'file'
    assert exists_as(tmp_path.parent) == 'directory'
    assert exists_as('~/tmp/tmp_exists_as_does_not_exist') == ''



# Generated at 2022-06-13 20:56:37.648406
# Unit test for function chmod
def test_chmod():
    # Test for a directory
    tmpdir = Path('/tmp/test_chmod')
    path = tmpdir / 'test_chmod.txt'
    if tmpdir.exists():
        import shutil
        shutil.rmtree(tmpdir)
    tmpdir.mkdir()
    path.touch()
    if path.stat().st_mode & 0o777 != 0o600:
        raise RuntimeError("Wrong value for the mode of {}: {}".format(path, oct(path.stat().st_mode)))
    chmod(path, 0o660)
    if path.stat().st_mode & 0o777 != 0o660:
        raise RuntimeError("Wrong value for the mode of {}: {}".format(path, oct(path.stat().st_mode)))

# Generated at 2022-06-13 20:56:50.259355
# Unit test for function chmod
def test_chmod():
    from tempfile import mkstemp
    from flutils.pathutils import chmod, path_absent

    # Test with a single file
    fd, path = mkstemp(prefix='flutils.test_chmod.')
    try:
        path = Path(path)
        chmod(path, 0o660)
        mode = path.stat().st_mode
        # Get the mode bits as an octal string
        assert oct(mode & 0o777) == oct(0o660)
    finally:
        path_absent(path)

    # Test with a directory
    path = Path('/tmp/flutils_test_chmod')
    path.mkdir(parents=False, exist_ok=True)

# Generated at 2022-06-13 20:57:02.213365
# Unit test for function path_absent
def test_path_absent():
    from collections import deque
    from io import StringIO
    from os import getcwd
    from subprocess import PIPE
    from tempfile import TemporaryDirectory
    from typing import Deque
    from unittest import main, TestCase
    from unittest.mock import patch
    from shutil import rmtree
    from flutils.pathutils import (
        abs_path, chmod, chown, create_dirs, mtime, normalize_path,
        path_absent, touch, exists_as
    )

    from .helpers import (
        call_sub_process, call_sub_process_no_pipe, get_os_group, get_os_user
    )

    class TestPathAbsent(TestCase):

        def test_path_absent_broken_symlink(self):
            link_

# Generated at 2022-06-13 20:57:07.903571
# Unit test for function chown
def test_chown():
    # change it to the actual directory
    # path = normalize_path("/home/anastasiia/Documents/software_engineering/exam/flutils/tests/osutils")
    path = normalize_path("/home/anastasiia/Documents/software_engineering/exam/flutils/tests/osutils")
    chown(path, user="anastasiia", group="anastasiia")



# Generated at 2022-06-13 20:57:18.252662
# Unit test for function path_absent
def test_path_absent():
    path = '~/tmp/test_path'
    path = normalize_path(path)
    mkdirp(path)
    assert path.is_dir()
    path_absent(path)
    assert not path.exists()
    home = Path(os.environ['HOME'])
    path = home.as_posix() + '//tmp///test_path'
    mkdirp(path)
    assert path.is_dir()
    path_absent(path)
    assert not path.exists()



# Generated at 2022-06-13 20:57:19.662146
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:57:21.037461
# Unit test for function chown
def test_chown():
    assert chown



# Generated at 2022-06-13 20:57:29.259270
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import directory_present
    from flutils.osutils import remove_tree
    from tempfile import mkdtemp

    tmp_dir = mkdtemp(prefix='unit_testing')
    try:
        path = Path('%s/test_path' % tmp_dir)
        test_dir = directory_present(path)
        assert test_dir.exists() is True
        assert test_dir.is_dir() is True
        assert test_dir.is_file() is False
        assert test_dir.samefile(path) is True
    finally:
        remove_tree(tmp_dir)



# Generated at 2022-06-13 20:57:33.844261
# Unit test for function chown
def test_chown():
    path = normalize_path('~/tmp/flutils.tests.osutils.txt')
    chown(path)
    chown(path, user='foo', group='bar')



# Generated at 2022-06-13 20:57:38.888062
# Unit test for function chown
def test_chown():
    file_path = Path('~/tmp/flutils.tests.osutils.txt')
    file_path.touch()
    chown(file_path)
    os.remove(file_path.as_posix())



# Generated at 2022-06-13 20:58:04.759070
# Unit test for function chown
def test_chown():
    assert False, "TODO: Write unit tests for chown"



# Generated at 2022-06-13 20:58:15.109251
# Unit test for function chmod
def test_chmod():
    import glob
    import os
    import pytest
    from flutils.pathutils import chmod

    path = Path('~/tmp/chmod/test_chmod/').expanduser()
    path.mkdir(parents=True, exist_ok=True)

    path2 = Path('~/tmp/chmod/test_chmod/test_chmod2/').expanduser()
    path2.mkdir(parents=True, exist_ok=True)

    text_path = path.joinpath('test_chmod.txt')
    with text_path.open('w') as fh:
        fh.write('This is a test')

    text_path2 = path2.joinpath('test_chmod2.txt')
    with text_path2.open('w') as fh:
        fh.write

# Generated at 2022-06-13 20:58:17.280198
# Unit test for function chmod
def test_chmod():
    assert True



# Generated at 2022-06-13 20:58:28.582644
# Unit test for function chmod
def test_chmod():
    base_path = Path('~').expanduser() / 'tmp' / 'flutils.tests.pathutils'
    symlink_src = base_path / 'foo'
    symlink_dst = base_path / 'foo.symlink'
    sub_symlink_dst = base_path / 'subdir' / 'foo.symlink'
    sub_symlink_src = base_path / 'subdir' / 'foo'
    matching_parent_path = Path('~').expanduser() / 'tmp' / '*.txt'
    unmatching_parent_path = Path('~').expanduser() / 'tmp' / 'doesnotexist.txt'
    path_to_dir = base_path / 'subdir'

# Generated at 2022-06-13 20:58:34.268951
# Unit test for function directory_present
def test_directory_present():
    test_dir = Path().resolve().parent / 'tmp' / 'flutils.tests.test_pathutils'
    if test_dir.exists() is False:
        test_dir.mkdir(parents=True, exist_ok=True)

    directory_present(test_dir)
    assert test_dir.is_dir() is True



# Generated at 2022-06-13 20:58:46.321892
# Unit test for function chmod
def test_chmod():
    with tempfile.TemporaryDirectory(prefix='flutils.tests.osutils.') as tmpdir:
        tmpdir = Path(tmpdir)

        txt1 = tmpdir / 'tmp1.txt'

        with txt1.open('w') as f:
            f.write('Hello world')

        txt2 = tmpdir / 'tmp2.txt'

        with txt2.open('w') as f:
            f.write('Hello world')

        txt3 = tmpdir / 'tmp3.txt'

        with txt3.open('w') as f:
            f.write('Hello world')

        tmp4 = tmpdir / 'tmp4'
        tmp4.mkdir()

        txt4 = tmp4 / 'tmp4.txt'


# Generated at 2022-06-13 20:58:49.487392
# Unit test for function chmod
def test_chmod():
    assert chmod('~/tmp/flutils.tests.osutils.txt', 0o660) is None


# Generated at 2022-06-13 20:59:04.165962
# Unit test for function directory_present
def test_directory_present():
    with tempfile.TemporaryDirectory() as tmp_path:
        tmp_path = Path(tmp_path)
        test_path = directory_present(
            tmp_path / 'test_directory_present',
            mode=0o755,
            user=getpass.getuser(),
            group=grp.getgrgid(os.getgid()).gr_name
        )

    # The returned type will be PosixPath or WindowsPath
    if os.name == 'nt':
        assert isinstance(test_path, WindowsPath)
    else:
        assert isinstance(test_path, PosixPath)

    if os.name == 'nt':
        expected = r'C:\\Users\\len\\AppData\\Local\\Temp\\tmpyyy92gvf'

# Generated at 2022-06-13 20:59:15.123104
# Unit test for function path_absent
def test_path_absent():
    # Get a test directory and create a temporary directory.
    testdir = tempfile.TemporaryDirectory()
    # Get the path to the temporary directory
    testdir_path = Path(testdir.name)
    # Create a test directory
    test1_path = testdir_path.joinpath('test_one')
    # Create a temporary file
    test1_file = test1_path.joinpath('test1.txt')
    # Create a test directory
    test2_path = testdir_path.joinpath('test_two')
    # Create a temporary file
    test2_file = test2_path.joinpath('test2.txt')
    # Create the test directories and files
    path_present(test1_path)
    path_present(test1_file)
    path_present(test2_path)
    path

# Generated at 2022-06-13 20:59:17.901410
# Unit test for function get_os_user
def test_get_os_user():
    print(get_os_user('root'))
    print(get_os_user(0))



# Generated at 2022-06-13 21:00:04.814835
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    import os

    def _test_chown(user: str = None, group: str = None) -> None:
        chown('~/tmp/flutils.tests.osutils.txt', user=user, group=group)
        assert os.path.exists('~/tmp/flutils.tests.osutils.txt')

    if os.environ.get('TRAVIS') == 'true':
        _test_chown()
    else:
        _test_chown('root', 'root')



# Generated at 2022-06-13 21:00:16.751720
# Unit test for function chown
def test_chown():
    from os import path
    from shutil import rmtree
    from tempfile import mkdtemp
    from flutils.pathutils import chown

    # Test a file with a single path of the glob pattern
    tmp_dir = mkdtemp()
    tmp_path = path.join(tmp_dir, 'foo.txt')
    with open(tmp_path, 'w') as f:
        f.write('this is a test')

    chown(tmp_path, user='root', group='wheel')
    assert path.getuid(tmp_path) == 0
    assert path.getgid(tmp_path) == 0
    rmtree(tmp_dir)

    # Test a file with a glob pattern
    tmp_dir = mkdtemp()
    tmp_dir_sub = path.join(tmp_dir, 'subdir')

# Generated at 2022-06-13 21:00:20.647367
# Unit test for function get_os_user
def test_get_os_user():
    """ Test get os user
    """
    os_user = get_os_user()
    assert isinstance(os_user, pwd.struct_passwd)


# Generated at 2022-06-13 21:00:25.084884
# Unit test for function get_os_user
def test_get_os_user():
    assert get_os_user(get_os_user().pw_name) == get_os_user()
    assert get_os_user(get_os_user().pw_uid) == get_os_user()


# Generated at 2022-06-13 21:00:37.390738
# Unit test for function chmod
def test_chmod():
    from pathlib import Path
    from tempfile import TemporaryDirectory

    from flutils.pathutils import chmod

    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        fpath = Path('~/tmp/flutils.tests.osutils.txt')
        fpath = fpath.expanduser()
        fpath = fpath.resolve()
        fpath = fpath.with_name(fpath.name + '.path')
        fpath.touch()

        dpath = tmpdir / 'dummy.dir'
        dpath.mkdir()

        mode_file = 0o640
        mode_dir = 0o730

        with tmpdir.as_cwd():
            chmod('~/tmp/flutils.tests.osutils*', mode_file, mode_dir)


# Generated at 2022-06-13 21:00:49.283745
# Unit test for function directory_present
def test_directory_present():
    from tempfile import mkdtemp
    tmpdir = Path(mkdtemp(prefix='flutils.test.'))

    sub_path = tmpdir / 'test_directory_present'
    directory_present(sub_path)

    assert sub_path.exists() is True
    assert sub_path.is_dir() is True
    assert sub_path.owner() == getpass.getuser()
    assert stat.S_IMODE(sub_path.stat().st_mode) == 0o700
    assert sub_path.group() == grp.getgrgid(os.getgid()).gr_name

    tmpdir.rmdir()

    sub_path = tmpdir / 'test_directory_present'
    directory_present(sub_path, user='root', group='wheel')

    assert sub_path.exists()

# Generated at 2022-06-13 21:01:01.817977
# Unit test for function exists_as
def test_exists_as():
    """Test the exists_as function."""

    from .osutils import get_free_port
    from .osutils import get_temp_file

    expected = 'directory'
    base_path = Path(__file__).parent.parent.parent
    path = base_path / 'data'
    assert exists_as(path) == expected

    # Try a symlink and make sure it works.
    expected = 'file'
    temp_port = get_free_port()
    filepath = get_temp_file(port=temp_port)
    assert exists_as(filepath) == expected
    symlink_path = filepath + '.lnk'
    symlink_path.symlink_to(filepath)
    assert exists_as(symlink_path) == expected
    filepath.unlink()

   

# Generated at 2022-06-13 21:01:12.397771
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import directory_present
    from flutils.pathutils import exists_as
    from flutils.pathutils import file_present
    from shutil import rmtree

    tmp_dir = directory_present('./tmp/pathutils_tests/exists_as')

    # Creation of directories
    path1 = directory_present(os.path.join(tmp_dir, 'dir1'))
    path2 = directory_present(os.path.join(path1, 'dir2'))
    assert exists_as(path1) == 'directory'
    assert exists_as(path2) == 'directory'

    path3 = file_present(os.path.join(path1, 'file1'))
    assert exists_as(path3) == 'file'


# Generated at 2022-06-13 21:01:15.379059
# Unit test for function path_absent
def test_path_absent():
    # Create the path.
    path_absent('~/tmp/test_path')

    # Assert the path does not exist.
    assert not exists_as('~/tmp/test_path')



# Generated at 2022-06-13 21:01:28.677420
# Unit test for function directory_present
def test_directory_present():
    from . import mock

    source_path = normalize_path(__file__)
    source_parent = source_path.parent

    with mock.patch.object(sys, 'platform', 'darwin'):
        with mock.patch('os.getuid') as mock_getuid:
            mock_getuid.return_value = 1000
            # patch getpass.getuser to return the name "len"
            with mock.patch('getpass.getuser') as mock_getuser:
                mock_getuser.return_value = 'len'

                created_path = directory_present(
                    '%s/tmp/%s/*.txt' % (str(source_parent), 'normpath'),
                    mode=0o777
                )

# Generated at 2022-06-13 21:02:14.545323
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    from os import makedirs
    from os.path import dirname
    from os.path import join as join_path
    from random import choice
    from random import randint
    from tempfile import gettempdir

    is_root = bool(os.geteuid() == 0)

    user = getpass.getuser()
    tmp_dir = join_path(gettempdir(), '.flutils.test-chown.txt')
    try:
        makedirs(tmp_dir)
    except FileExistsError:
        pass

    def _test_chown():
        chown(tmp_dir, user=None, group=None)

    def _test_chown_pathlib():
        from pathlib import Path

# Generated at 2022-06-13 21:02:25.962953
# Unit test for function exists_as
def test_exists_as():
    path = Path().home() / 'tmp'
    try:
        exists_as(path)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError('`exists_as` should have raised a '
                             'FileNotFoundError.')
    tmp_dir = Path().home() / 'tmp' / 'test_path'
    tmp_dir.mkdir(parents=True)
    assert exists_as(tmp_dir) == 'directory'
    tmp_dir.rmdir()
    tmp_file = Path().home() / 'tmp' / 'test_file'
    tmp_file.touch(exist_ok=True)
    assert exists_as(tmp_file) == 'file'
    tmp_file.unlink()



# Generated at 2022-06-13 21:02:38.108778
# Unit test for function chown
def test_chown():
    import tempfile
    import shutil

    def _test_chown(
            tmpdir: Path, user: str, group: str,
            include_parent: bool,
    ) -> None:
        # These are the default values for chown()
        # for the arguments: user and group.
        default_user = getpass.getuser()
        default_group = grp.getgrgid(os.getgid()).gr_name

        # Make sure user is still -1 so the
        # ownership is not changed.
        if user == '-1':
            user = default_user
        if group == '-1':
            group = default_group

        # Make sure the user and group exist on the system.
        user_obj = pwd.getpwnam(user)
        group_obj = grp.getgr

# Generated at 2022-06-13 21:02:47.646451
# Unit test for function path_absent
def test_path_absent():
    import tempfile # type: ignore

    # Test a basic file removal.
    tmp_dir = tempfile.mkdtemp(prefix='tmp_')
    tmp_f = os.path.join(tmp_dir, 'tmp_file')
    open(tmp_f, 'w')
    assert os.path.isfile(tmp_f)
    path_absent(tmp_f)
    assert os.path.isfile(tmp_f) is False

    # Test a basic link removal.
    tmp_link = os.path.join(tmp_dir, 'link')
    os.symlink(tmp_f, tmp_link)
    assert os.path.islink(tmp_link)
    path_absent(tmp_link)
    assert os.path.islink(tmp_link) is False

    # Test a basic

# Generated at 2022-06-13 21:02:55.534975
# Unit test for function chmod
def test_chmod():
    from tempfile import mkdtemp
    from unittest import TestCase
    import unittest

    # In order to unit test the updating of the inode data,
    # an existing path must be used.  This code
    # runs during the import of the module.
    tmpdir = mkdtemp(prefix='flutils_test_')


# Generated at 2022-06-13 21:03:08.381031
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import (
        find_paths, get_temporary_directory, mkdir, path_absent
    )
    temp_dir = get_temporary_directory()

    test_dir = mkdir(temp_dir / 'test_dir')
    test_file = mkdir(temp_dir / 'test_file')
    test_link = mkdir(temp_dir / 'test_link')

    # Before deletion
    assert find_paths(temp_dir)
    assert find_paths(temp_dir / 'test_*')

    path_absent(temp_dir / 'test_dir')
    path_absent(temp_dir / 'test_file')
    path_absent(temp_dir / 'test_link')

    # After deletion

# Generated at 2022-06-13 21:03:15.809967
# Unit test for function chmod
def test_chmod():
    from tempfile import mkdtemp
    from contextlib import contextmanager
    import shutil
    from pathlib import Path
    from os import rmdir

    @contextmanager
    def tmp_directory(
            dir_path: _PATH = Path(mkdtemp())
    ) -> Generator[_PATH, None, None]:
        try:
            yield Path(dir_path)
        finally:
            if Path(dir_path).is_dir() is True:
                shutil.rmtree(dir_path)
            else:
                rmdir(dir_path)

    # Defaults
    def test_default_mode():
        with tmp_directory() as dir_path:
            file_path = dir_path / Path('test_file.txt')
            file_path.write_text('test')

            assert file_path.ex

# Generated at 2022-06-13 21:03:23.772329
# Unit test for function chown
def test_chown():
    from pathlib import Path
    import tempfile

    from flutils.pathutils import chown

    path = Path(tempfile.mkdtemp()) / 'foo'
    path.mkdir()

    chown(path, '-1', '-1')

    assert path.stat().st_uid == 0

    chown(path, 'nobody', 'nogroup')

    assert path.stat().st_gid == 65534

    chown(path, os.getuid(), os.getgid())

    assert path.stat().st_uid == os.getuid()
    assert path.stat().st_gid == os.getgid()

    # Test chown with a glob pattern
    path = Path(tempfile.mkdtemp()) / 'bar'
    (path / 'foo').mkdir()
    path2 = path

# Generated at 2022-06-13 21:03:24.698574
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:03:36.162324
# Unit test for function chown
def test_chown():
    # Test chown with a glob
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from stat import S_IRWXU
    from flutils.pathutils import chown

    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        file1 = tmp_dir / 'example1.txt'
        file1.touch()
        file2 = tmp_dir / 'example2.txt'
        file2.touch()

        assert file1.stat().st_mode & S_IRWXU == 0o600
        assert file2.stat().st_mode & S_IRWXU == 0o600

        chown(tmp_dir / 'example*.txt', user='foo', group='bar')

        assert os.stat(file1.as_posix()).st_uid == 1000