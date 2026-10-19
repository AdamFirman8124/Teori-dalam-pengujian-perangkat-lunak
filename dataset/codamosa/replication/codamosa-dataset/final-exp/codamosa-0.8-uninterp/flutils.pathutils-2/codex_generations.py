

# Generated at 2022-06-13 20:54:33.034389
# Unit test for function get_os_user
def test_get_os_user():
    assert isinstance(get_os_user(), pwd.struct_passwd)
    assert isinstance(get_os_user('root'), pwd.struct_passwd)
    with pytest.raises(OSError):
        get_os_user('foo')
    assert get_os_user(0).pw_name == 'root'
    with pytest.raises(OSError):
        get_os_user(-1)



# Generated at 2022-06-13 20:54:43.892255
# Unit test for function find_paths
def test_find_paths():
    with TemporaryDirectory() as td:
        directory_present(Path(td, 'test_dir'))
        directory_present(Path(td, 'test_dir', 'test_dir_2'))
        directory_present(Path(td, 'test_dir', 'test_dir_2', 'test_dir_3'))
        directory_present(Path(td, 'test_dir', 'test_dir_2', 'test_dir_3', 'test_dir_4'))
        touch(Path(td, 'test_file'))
        touch(Path(td, 'test_file_2'))
        touch(Path(td, 'test_dir', 'test_file.txt'))
        touch(Path(td, 'test_dir', 'test_file_2.txt'))

# Generated at 2022-06-13 20:54:54.936596
# Unit test for function exists_as
def test_exists_as():
    import tempfile
    import unittest.mock

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_file = Path(tmp_dir) / 'tmp_file.txt'
        tmp_file.touch()
        tmp_link = Path(tmp_dir) / 'tmp_link.txt'
        tmp_link.symlink_to(tmp_file)

        sub_dir = Path(tmp_dir) / 'sub_dir'
        sub_dir.mkdir()

        sub_link = Path(tmp_dir) / 'sub_link'
        sub_link.symlink_to(sub_dir)

        dir_link = Path(tmp_dir) / 'dir_link'
        dir_link.symlink_to(Path('/foo/bar'))

        # Test normalize_path

# Generated at 2022-06-13 20:55:02.635012
# Unit test for function chmod
def test_chmod():
    from .osutils import path_absent

    test_file = Path('~/tmp/flutils.tests.pathutils.txt').expanduser()
    test_file.write_text('hello world')

    chmod(test_file, 0o660)
    assert test_file.stat().st_mode & 0o777 == 0o660

    chmod('~/tmp/*', mode_file=0o664, mode_dir=0o770)
    assert test_file.stat().st_mode & 0o777 == 0o664

    path_absent(test_file)

# Generated at 2022-06-13 20:55:07.777644
# Unit test for function chown
def test_chown():
    assert chown == cast(
        Callable,
        functools.partial(
            chown,
            user=getpass.getuser(),
            group=getpass.getuser()
        )
    )

    assert chown('/tmp/osutils.chown.test').return_code is None



# Generated at 2022-06-13 20:55:19.871880
# Unit test for function chmod
def test_chmod():
    from random import randint
    from shutil import copyfile
    from tempfile import TemporaryDirectory

    from flutils.pathutils import chmod

    tmp = TemporaryDirectory()

    paths = (
        Path(tmp.name, 'a.txt'),
        Path(tmp.name, 'b.txt'),
        Path(tmp.name, 'c.txt'),
        Path(tmp.name, 'd.txt'),
    )


# Generated at 2022-06-13 20:55:26.678656
# Unit test for function find_paths
def test_find_paths():
    for path in find_paths('~/tmp/*'):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            path.rmdir()

    path = Path() / 'tmp' / 'file_one'
    path.write_text('file one')
    path = Path() / 'tmp' / 'dir_one'
    path.mkdir()

    paths = list(find_paths('~/tmp/*'))
    assert len(paths) == 2



# Generated at 2022-06-13 20:55:31.560476
# Unit test for function path_absent
def test_path_absent():
    try:
        path_absent('~/tmp/test_path')
        path_absent('~/tmp/test_path/one')
        path_absent('~/tmp/test_path/one/two')
        path_absent('~/tmp/test_path/one/two/three')
        path_absent('~/tmp/test_path/four')
        path_absent('~/tmp/test_path/five')
        path_absent('~/tmp/test_path/six')
    finally:
        path_absent('~/tmp/test_path')

# Generated at 2022-06-13 20:55:32.572908
# Unit test for function chmod
def test_chmod():
    assert callable(chmod)

# Generated at 2022-06-13 20:55:42.837894
# Unit test for function path_absent
def test_path_absent():
    # This test only makes sense if run as root or root equivalent.
    if os.geteuid() != 0:
        return
    # Create a temporary directory for testing.
    temp_dir = mkdtemp()
    temp_file = os.path.join(temp_dir, 'temp_file')
    temp_link = os.path.join(temp_dir, 'temp_link')
    os.mkdir(temp_link)
    os.chown(temp_link, os.geteuid(), os.getegid())
    # Create a file with different types of links.
    open(temp_file, 'w').close()
    os.symlink(temp_file, 'temp_hard_link')

# Generated at 2022-06-13 20:56:03.106303
# Unit test for function chown
def test_chown():
    """Test for :func:`flutils.pathutils.chown`."""

    import tempfile

    from unittest.mock import patch

    from xdg.BaseDirectory import xdg_cache_home

    from . import create_file_object
    from . import create_temp_directory
    from . import create_temp_file
    from . import hide_stdout

    tmppath = create_temp_directory()

    # Change to a temp directory
    with create_file_object('r'):
        with patch('os.getcwd') as mock_os_getcwd:
            mock_os_getcwd.return_value = tmppath.as_posix()
            assert tmppath.is_dir() is True

            # Normalize a path that is not a file

# Generated at 2022-06-13 20:56:14.270230
# Unit test for function exists_as
def test_exists_as():
    """Test function exists_as."""
    import tempfile  # noqa

    # Note: The tempfile module does NOT work with pathlib.
    # directory = tempfile.mkdtemp()
    directory = '/tmp/flutils.tests.pathutils.exists_as'
    if os.path.exists(directory) is False:
        os.makedirs(directory)

    path = os.path.join(directory, 'exists_as.txt')
    with open(path, 'a') as fh:
        fh.write('This is a unit test for function exists_as.\n')

    # just a dir
    assert exists_as(directory) == 'directory'
    assert exists_as(directory + '/') == 'directory'

    # file
    assert exists_as(path) == 'file'

   

# Generated at 2022-06-13 20:56:24.897116
# Unit test for function chmod
def test_chmod():
    _test_path = Path('~/.tmp/test_chmod').expanduser()
    _test_path.mkdir(parents=True, exist_ok=True)

    chmod('~/.tmp/test_chmod', mode_file=0o600, mode_dir=0o700)

    assert _test_path.stat().st_mode == 33261

    chmod('~/.tmp/test_chmod', mode_file=0o644, mode_dir=0o755, include_parent=True)

    _test_path = Path('~/.tmp/test_chmod').expanduser().parent

    assert _test_path.stat().st_mode == 16895


# Generated at 2022-06-13 20:56:35.765262
# Unit test for function path_absent
def test_path_absent():

    test_path = Path(Path.cwd(), 'tmp', 'test_path')
    test_dir = Path(test_path, 'dir')
    test_file = Path(test_path, 'file')
    test_file2 = Path(test_dir, 'file2')
    test_symlink = Path(test_path, 'symlink')
    test_symlink2 = Path(test_dir, 'symlink2')

    assert not test_path.exists(), "Test path already exists."

    assert not test_dir.exists(), "'test_dir' already exists."
    assert not test_file.exists(), "'test_file' already exists."
    assert not test_file2.exists(), "'test_file2' already exists."

# Generated at 2022-06-13 20:56:48.316651
# Unit test for function chown
def test_chown():
    path = Path("~/tmp/flutils/osutils/chown").expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode != 0o660:
        raise AssertionError("mode is {}".format(mode))
    chown("~/tmp/flutils/osutils/chown/test.txt", user="-1", include_parent=True)
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode != 0o660:
        raise AssertionError("mode is {}".format(mode))


# Generated at 2022-06-13 20:57:00.484003
# Unit test for function chmod
def test_chmod():
    """Ensure that the function chmod works as expected."""
    from collections import deque
    from os import PathLike
    from pathlib import Path
    from shutil import rmtree

    from flutils.pathutils import chmod

    TMP_DIR = Path('~/tmp/flutils.tests').expanduser()
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    TMP_FILE = TMP_DIR / 'test.txt'
    TMP_FILE.write_text('foobar')

    TMP_DIR_EMPTY = TMP_DIR / 'empty_dir'
    TMP_DIR_EMPTY.mkdir()

    TMP_DIR_POP = TMP_DIR / 'populated_dir'
    TMP_DIR_POP.mkdir()

    TMP

# Generated at 2022-06-13 20:57:09.815840
# Unit test for function chown
def test_chown():
    path = normalize_path('~/tmp/flutils.tests.osutils.txt')
    if '*' in path.as_posix():
        try:
            for sub_path in Path().glob(path.as_posix()):
                if sub_path.is_dir() or sub_path.is_file():
                    assert os.chown(sub_path.as_posix(), uid, gid)
        except NotImplementedError:
            # Path().glob() returns an iterator that will
            # raise NotImplementedError if there
            # are no results from the glob pattern.
            pass
        else:
            if include_parent is True:
                path = path.parent

# Generated at 2022-06-13 20:57:17.349326
# Unit test for function exists_as
def test_exists_as():
    path = Path().home() / 'tmp' / 'flutils.tests.pathutils'

# Generated at 2022-06-13 20:57:18.399834
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:57:29.333745
# Unit test for function path_absent
def test_path_absent():
    import glob
    import tempfile
    tmpdir = cast(str, tempfile.mkdtemp())

# Generated at 2022-06-13 20:57:50.232558
# Unit test for function chmod
def test_chmod():
    import os
    import tempfile
    import shutil
    import stat

    def _test_chmod(mode_file, mode_dir, include_parent):

        path = Path(tempfile.mkdtemp())
        paths = []
        for name in ['dir_one', 'dir_two', 'file_one', 'file_two']:
            paths.append(path.joinpath(name))
            paths[-1].touch()

        for idx, item in enumerate(paths):
            if item.is_dir() is True:
                os.chmod(item.as_posix(), 0o770)
            else:
                os.chmod(item.as_posix(), 0o600)

        chmod(path, mode_file, mode_dir, include_parent)


# Generated at 2022-06-13 20:57:53.812520
# Unit test for function path_absent
def test_path_absent():
    # Normal Usage
    path = Path(gettempdir(), str(uuid.uuid4()))
    path.mkdir()
    assert path.is_dir()
    path_absent(path)
    assert path.is_dir() is False



# Generated at 2022-06-13 20:58:05.918623
# Unit test for function directory_present
def test_directory_present():
    abspath = os.path.abspath(os.path.dirname(__file__))
    abspathparent = os.path.dirname(abspath)

    expected = Path(abspath).parent.joinpath('.test_directory_present')
    directory_present(expected, mode=0o755)
    assert expected.exists() is True
    assert expected.is_dir() is True
    expected.rmdir()

    expected = cast(Path, Path(abspath) / '..' / '..' / '..' / '.test_directory_present')
    directory_present(expected)
    assert expected.exists() is True
    assert expected.is_dir() is True
    expected.rmdir()


# Generated at 2022-06-13 20:58:10.348153
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent
    from tempfile import TemporaryDirectory
    with TemporaryDirectory(prefix='flutils_') as tmp_dir:
        tmp_dir = Path(tmp_dir)
        tmp_file_path = os.path.join(tmp_dir, 'tmp_file.txt')
        with open(tmp_file_path, 'w') as tmp_file:
            print('foo', file=tmp_file)
        tmp_dir_path = os.path.join(tmp_dir, 'tmp_dir')
        os.mkdir(tmp_dir_path)
        tmp_file_path = os.path.join(tmp_dir_path, 'tmp_file.txt')
        with open(tmp_file_path, 'w') as tmp_file:
            print('foo', file=tmp_file)

# Generated at 2022-06-13 20:58:17.015569
# Unit test for function chown
def test_chown():
    # Setup
    tmpdir = Path(tempfile.mkdtemp())
    test_file_name = 'flutils.tests.pathutils'
    test_file = tmpdir / test_file_name
    test_file.touch()
    # Execute
    chown(test_file)
    # Verify
    assert test_file.stat().st_uid == os.geteuid()
    assert test_file.stat().st_gid == os.getegid()
    # Teardown
    test_file.unlink()
    tmpdir.rmdir()


# Generated at 2022-06-13 20:58:28.482770
# Unit test for function chown
def test_chown():
    import shutil

    path = Path(__file__).parent / 'flutils.tests.osutils.txt'
    assert path.exists() is False


# Generated at 2022-06-13 20:58:39.956486
# Unit test for function chown
def test_chown():
    import tempfile
    import os

    # Basic tests
    new_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 20:58:41.534623
# Unit test for function chown
def test_chown():
    """
    >>> from flutils.pathutils import chown
    """



# Generated at 2022-06-13 20:58:50.139173
# Unit test for function chown
def test_chown():
    user = getpass.getuser()
    group = grp.getgrgid(os.getgid()).gr_name
    path = normalize_path('~/.flutils.tests.pathutils.tmp.txt')
    if path.exists():
        path.unlink()
    path.touch()
    assert path.exists() is True
    assert path.is_file() is True
    chown(path, user, group)
    assert path.owner() == user
    assert path.group() == group
    path.unlink()
    assert path.exists() is False
    path.parent.rmdir()
    assert path.parent.exists() is False



# Generated at 2022-06-13 20:58:54.692123
# Unit test for function directory_present
def test_directory_present():
    path = directory_present('~/tmp/flutils.tests.pathutils.test_dir', 0o700)
    assert path.is_dir()



# Generated at 2022-06-13 20:59:14.875563
# Unit test for function exists_as
def test_exists_as():
    from os.path import expanduser
    from pathlib import Path
    from textwrap import dedent

    if os.name == 'nt':
        pipe = r'\\.\pipe\test_pipe'
    else:
        pipe = '/tmp/test_pipe'

    pytest.importorskip('psutil')

    root_path = Path(expanduser('~/tmp'))

    path = root_path / 'foo'
    assert 'directory' == exists_as(path)

    path = root_path / 'bar'
    assert '' == exists_as(path)

    path = root_path / 'foo.txt'
    assert 'file' == exists_as(path)

    path = root_path / 'baz'
    assert '' == exists_as(path)

    # Write some data to the file so that

# Generated at 2022-06-13 20:59:18.064198
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(Path('.')) == 'directory'
    assert exists_as(Path('__init__.py')) == 'file'



# Generated at 2022-06-13 20:59:28.659472
# Unit test for function get_os_user
def test_get_os_user():
    """Unit tests for the :obj:`get_os_user` function.
    """
    # Test get_os_user() with no arguments and no errors thrown
    user = get_os_user()
    assert isinstance(user, pwd.struct_passwd)
    assert user.pw_name == getpass.getuser()

    # Test get_os_user() with a "login name" and no errors thrown
    # Add a test user if the current user is root
    if getpass.getuser() == 'root':
        pwd.getpwnam('test_user')

# Generated at 2022-06-13 20:59:40.754536
# Unit test for function chown
def test_chown():
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        chown_file = cwd / '.chown_file'
        chown_file.touch(mode=0o660)

        chown_symlink = cwd / '.chown_symlink'
        chown_symlink.symlink_to(chown_file, target_is_directory=False)

        chown_dir = cwd / '.chown_dir'
        chown_dir.mkdir(mode=0o770)

        chown_dir_symlink = cwd / '.chown_dir_symlink'
        chown_dir_symlink.symlink_to(chown_dir, target_is_directory=True)


# Generated at 2022-06-13 20:59:45.851963
# Unit test for function path_absent
def test_path_absent():
    path = '~/tmp/path_absent_test'
    path_absent(path)
    path = normalize_path(path)
    assert str(path) == (os.getcwd() + '/path_absent_test')



# Generated at 2022-06-13 20:59:50.306002
# Unit test for function path_absent
def test_path_absent():
    os.chdir(os.path.expanduser('~'))
    p = 'tmp/test_path'
    create_path(p)
    assert os.path.exists(p)
    path_absent(p)
    assert not os.path.exists(p)



# Generated at 2022-06-13 21:00:01.921010
# Unit test for function chmod
def test_chmod():
    import tempfile
    import pytest
    import flutils.pathutils as pathutils

    tmpdir = Path(tempfile.mkdtemp())
    tmpdir.joinpath('test1.txt').write_text('just a test')
    tmpdir.chmod(0o755)
    tmpdir.joinpath('test1.txt').chmod(0o600)
    subdir = tmpdir.joinpath('subdir')
    subdir.mkdir(0o755)
    subdir.joinpath('subsubdir').mkdir(0o755)
    subdir.joinpath('subsubdir').joinpath('test1.txt').write_text('just a test')
    subdir.joinpath('subsubdir').joinpath('test1.txt').chmod(0o600)

    # test a single dir

# Generated at 2022-06-13 21:00:15.188990
# Unit test for function directory_present
def test_directory_present():
    from pathlib import Path
    from sys import platform
    from os import chmod, chown
    from tempfile import NamedTemporaryFile, TemporaryDirectory
    import pytest

    test_paths = [
        '~/tmp/tester/test/this_path',
        '~/tmp/tester/test/this_path/',
        str(Path('~/tmp/tester/test/this_path')),
        str(Path('~/tmp/tester/test/this_path/')),
    ]

    with TemporaryDirectory(prefix='flutils.') as temp_dir:
        temp_dir = Path(temp_dir)
        chmod(temp_dir.as_posix(), 0o700)
        chown(temp_dir.as_posix(), os.getuid(), os.getgid())

       

# Generated at 2022-06-13 21:00:24.103231
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('') == ''
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/etc') == 'directory'
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/etc/hosts.allow') == 'file'
    assert exists_as('/etc/hosts.deny') == 'file'
    assert exists_as('/etc/hosts.subdomain.allow') == 'file'

# Generated at 2022-06-13 21:00:36.679375
# Unit test for function directory_present
def test_directory_present():
    from flutils.tests.pathutils import (
        PATH_TEST_DIR,
        PATH_TEST_DIR_CHOWN,
    )

    path = directory_present(PATH_TEST_DIR_CHOWN)
    assert path == PATH_TEST_DIR_CHOWN
    assert path.is_dir() is True
    assert path.stat().st_uid == os.getuid()
    group = grp.getgrgid(path.stat().st_gid)
    assert group.gr_name == getpass.getuser()
    assert path.stat().st_mode == 0o700

    path = directory_present(Path(PATH_TEST_DIR, 'foobar'), mode=0o755)
    assert path == Path(PATH_TEST_DIR, 'foobar')

# Generated at 2022-06-13 21:00:53.439361
# Unit test for function chmod
def test_chmod():
    import filecmp
    import shutil
    import tempfile
    import unittest

    data_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'data'
    )

    file_path = os.path.join(
        data_dir,
        'flutils.tests.osutils.txt'
    )

    orig_file_path = file_path + '.orig'

    if os.path.exists(orig_file_path):
        shutil.copyfile(
            orig_file_path, file_path
        )

    actual_file_path = os.path.join(
        data_dir, 'flutils.tests.osutils.txt.copy'
    )


# Generated at 2022-06-13 21:01:04.898839
# Unit test for function chmod
def test_chmod():
    print("flutils.pathutils.test_chmod")
    # If a path exists, we want to make sure that chmod() works
    tmp_path = Path("~/tmp/") / "flutils.tests.osutils.txt"
    if not tmp_path.exists():
        tmp_path.touch()
    chmod(tmp_path, 0o660, include_parent=True)
    assert tmp_path.stat().st_mode & 0o700 == 0o660
    assert tmp_path.parent.stat().st_mode & 0o700 == 0o700
    tmp_path.chmod(0o777)
    tmp_path.parent.chmod(0o777)
    # If a path does not exist, we want to make sure that chmod() does nothing
    tmp_path = Path("~/tmp/")

# Generated at 2022-06-13 21:01:15.105383
# Unit test for function chmod
def test_chmod():
    """
    Unit test for ``chmod``.

    """

    mode_dir = 0o770
    mode_file = 0o660
    path_dir = normalize_path('~/tmp/flutils.tests.osutils_chmod')
    path_file = normalize_path('~/tmp/flutils.tests.osutils.txt')

    os.makedirs(path_dir, exist_ok=True)

    Path(path_file).touch()

    chmod(path_dir, mode_file=mode_file, mode_dir=mode_dir)

    stat_dir = os.stat(path_dir)
    assert stat_dir.st_mode == (stat.S_IFDIR | mode_dir)

    Path(path_file).touch()


# Generated at 2022-06-13 21:01:28.457139
# Unit test for function chown
def test_chown():
    from unittest.mock import patch
    from tests.pathutils import TEST_DIR, TEST_GLOB
    from tests.pathutils import get_stat

    uid, user = getpass.getuser(), get_os_user()
    gid, group = user.pw_gid, get_os_group(user.pw_gid)

    with patch(
            'flutils.pathutils.get_os_user',
            return_value=user):

        with patch(
                'flutils.pathutils.get_os_group',
                return_value=group):

            chown(TEST_DIR)
            assert get_stat(TEST_DIR).st_uid == uid
            assert get_stat(TEST_DIR).st_gid == gid

            # Change user and group to non-existent

# Generated at 2022-06-13 21:01:29.247637
# Unit test for function chmod
def test_chmod():
    assert True



# Generated at 2022-06-13 21:01:39.739323
# Unit test for function chmod

# Generated at 2022-06-13 21:01:50.402959
# Unit test for function chown
def test_chown():
    path = Path('/tmp/test_chown.txt')
    assert path.exists() is False
    path.touch()
    assert path.exists() is True

    # test with defaults
    chown(path)
    # assert os.stat(path).st_uid == os.getuid()
    # assert os.stat(path).st_gid == os.getgid()

    # test with -1 as user and group
    chown(path, user='-1', group='-1')
    # assert os.stat(path).st_uid == os.getuid()
    # assert os.stat(path).st_gid == os.getgid()

    # test with 'nobody' as the user and group
    chown(path, user='nobody', group='nobody')
    # assert os.

# Generated at 2022-06-13 21:01:50.989818
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:01:59.400231
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import exists_as, path_absent
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'foo')
        path_absent(path)
        assert exists_as(path) == ''
        path_file = path
        with open(path_file, 'w') as fileobj:
            fileobj.write('foo argle bargle')
        assert exists_as(path) == 'file'
        path = os.path.join(tmpdir, 'foo', 'bar', 'baz')
        path_absent(path)
        assert exists_as(path) == ''
        path_absent(path)
        os.mkdir(path)
        path_file = os.path.join(path, 'bar')
       

# Generated at 2022-06-13 21:02:05.918402
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(osutils.TEMP_DIR) == 'directory'
    assert exists_as(osutils.TEMP_DIR / 'flutils.txt') == 'file'
    assert exists_as(osutils.TEMP_DIR / 'flutils.txt.hidden') == ''
    assert exists_as('/dev/null') == 'char device'



# Generated at 2022-06-13 21:02:19.504121
# Unit test for function exists_as
def test_exists_as():
    test_data = (
        ('~/tmp', 'directory'),
        ('~/tmp/nonexistent.txt', ''),
    )
    for datum in test_data:
        assert exists_as(datum[0]) == datum[1]



# Generated at 2022-06-13 21:02:20.243803
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:02:22.323220
# Unit test for function exists_as
def test_exists_as():
    from flutils.tests.pathutils import _test_exists_as
    _test_exists_as()



# Generated at 2022-06-13 21:02:28.374598
# Unit test for function path_absent
def test_path_absent():
    import tempfile
    tmpdir = Path(tempfile.gettempdir())
    test_path = create_directory(tmpdir / 'flutils_test_path_absent')
    test_file_1 = create_file(test_path / 'test_one.txt')
    test_file_2 = create_file(test_path / 'test_two.txt')
    create_symlink(test_path / 'test_link', test_file_2)
    test_sub_dir = create_directory(test_path / 'sub_dir')
    test_sub_sub_dir = create_directory(test_sub_dir / 'sub_sub_dir')
    test_sub_sub_file = create_file(test_sub_sub_dir / 'sub_sub_file.dat')


# Generated at 2022-06-13 21:02:37.432260
# Unit test for function chmod
def test_chmod():
    for path in find_paths('~/tmp'):
        path.chmod(0o600)
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)
    chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770)
    chmod('~/tmp/*')
    chmod('~/tmp/flutils.tests.osutils.txt', 0o600)
    chmod('~/tmp/*', 0o700)
    chmod('~/tmp/**', mode_file=0o600, mode_dir=0o700)
# End unit test



# Generated at 2022-06-13 21:02:40.848681
# Unit test for function exists_as
def test_exists_as():
    """Tests for function `exists_as`."""
    import doctest
    from flutils.pathutils import exists_as
    doctest.testmod(exists_as)



# Generated at 2022-06-13 21:02:51.335487
# Unit test for function chown
def test_chown():
    filename = '/tmp/flutils.tests.pathutils.txt'
    with open(filename, 'w') as f:
        f.write('foo')
    chown(filename)
    if sys.platform == 'win32':
        assert os.path.isfile(filename)
        with open(filename, 'r') as f:
            assert f.read() == 'foo'
    else:
        assert os.path.isfile(filename)
        assert pwd.getpwuid(os.stat(filename).st_uid).pw_name == getpass.getuser()
        assert grp.getgrgid(os.stat(filename).st_gid).gr_name == grp.getgrgid(os.getuid()).gr_name
        with open(filename, 'r') as f:
            assert f

# Generated at 2022-06-13 21:03:05.306339
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/usr') == 'directory'
    assert exists_as('/sbin/init') == 'file'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/sda') == 'block device'
    assert exists_as('/tmp/foo') == ''
    assert exists_as('/sbin/foo') == ''
    assert exists_as('/root/foo') == ''
    assert exists_as('/root/foo') == ''
    assert exists_as('/dev/foo') == ''
    if sys.platform == "win32":
        assert exists_as('C:\\Windows\\System32\\drivers\\etc\\hosts') == 'file'
        assert exists_as('C:\\Windows\\System32') == 'directory'

# Generated at 2022-06-13 21:03:14.482687
# Unit test for function directory_present
def test_directory_present():
    """Test function ``directory_present``.
    """
    from pathlib import Path
    import tempfile

    def cleanup(path: Path) -> None:
        """Helper function to cleanup the given path.
        """
        import shutil
        if path.is_dir() is True:
            shutil.rmtree(path.as_posix())
        elif path.is_file() is True:
            path.unlink()
        elif path.is_symlink() is True:
            path.unlink()

    def create_and_validate(path: Path, mode: Optional[int],
                            user: Optional[str], group: Optional[str]) -> Path:
        """Helper function to create a directory and validate its attributes.
        """
        import stat
        if mode is None:
            mode = 0o700

# Generated at 2022-06-13 21:03:21.461599
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    import tempfile
    import os
    directory = tempfile.TemporaryDirectory()
    fd, path = tempfile.mkstemp(dir=directory.name, prefix='')
    os.close(fd)
    assert exists_as(directory.name) == 'directory'
    assert exists_as(path) == 'file'
    directory.cleanup()
    try:
        exists_as(path)
    except FileNotFoundError:
        pass
    else:
        assert False


# Generated at 2022-06-13 21:03:37.033279
# Unit test for function path_absent
def test_path_absent():
    from hypothesis import given
    from hypothesis.strategies import text
    from flutils.pathutils import path_absent

    @given(text())
    def test_path_absent(path: str) -> None:
        path_absent(path)

    test_path_absent()

