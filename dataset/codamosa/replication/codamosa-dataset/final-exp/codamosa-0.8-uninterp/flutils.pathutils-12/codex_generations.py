

# Generated at 2022-06-13 20:54:27.312935
# Unit test for function path_absent
def test_path_absent():
    import pytest
    from flutils.pathutils import path_absent

    # test for existing file
    with scoped_cwd(os.getcwd()):
        dir_name = next(tempfile._get_candidate_names())
        dir_path = Path(dir_name)
        dir_path.mkdir(parents=True)
        file_path = Path(dir_path, 'test_file')
        file_path.touch()

        path = file_path
        path_absent(path)
        assert not path.is_file()

    # test for existing directory
    with scoped_cwd(os.getcwd()):
        dir_name = next(tempfile._get_candidate_names())
        dir_path = Path(dir_name)

# Generated at 2022-06-13 20:54:35.417832
# Unit test for function find_paths
def test_find_paths():
    with TempDirectory() as tmp_dir:
        tmp_dir.join('file_one').write('testing')
        tmp_dir.join('dir_one').mkdir('.')
        paths = list(find_paths(tmp_dir.strpath + '/*'))
        assert paths == [
            Path(tmp_dir.strpath + '/file_one'),
            Path(tmp_dir.strpath + '/dir_one')
        ]



# Generated at 2022-06-13 20:54:37.540662
# Unit test for function directory_present
def test_directory_present():
    directory_present('~/tmp/test_path')
test_directory_present()


# Generated at 2022-06-13 20:54:51.067712
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import (
        chmod,
        get_os_group,
        get_os_user,
        normalize_path,
        path_absent,
    )


# Generated at 2022-06-13 20:54:54.033931
# Unit test for function chown
def test_chown():
    chown('~/foo/bar', group='bar', user='foo')



# Generated at 2022-06-13 20:54:57.765319
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(Path(__file__)) == 'file'
    assert exists_as(Path(__file__).parent) == 'directory'
    assert exists_as(Path('')) == ''
    assert exists_as(__file__) == 'file'
    assert exists_as(os.path.dirname(__file__)) == 'directory'
    assert exists_as('') == ''



# Generated at 2022-06-13 20:55:05.340442
# Unit test for function directory_present
def test_directory_present():
    test_dir = str(Path(__file__).parent.parent / 'data' / 'test_dir')

# Generated at 2022-06-13 20:55:16.570081
# Unit test for function chown
def test_chown():
    def get_path_owner(path: _PATH) -> _STR_OR_INT_OR_NONE:
        path = normalize_path(path)
        if path.exists() is False:
            return None
        stat = path.stat()
        return pwd.getpwuid(stat.st_uid).pw_name

    def get_path_group(path: _PATH) -> _STR_OR_INT_OR_NONE:
        path = normalize_path(path)
        if path.exists() is False:
            return None
        stat = path.stat()
        return grp.getgrgid(stat.st_gid).gr_name

    import tempfile
    import shutil
    from pathlib import Path
    from flutils.pathutils import chown


# Generated at 2022-06-13 20:55:17.234816
# Unit test for function directory_present
def test_directory_present():
    pass



# Generated at 2022-06-13 20:55:18.961570
# Unit test for function chmod
def test_chmod():
    chmod("flutils/tests/osutils.py", 0o600, 0o700, False)
    pass


# Generated at 2022-06-13 20:55:38.470853
# Unit test for function path_absent
def test_path_absent():
    test_file = os.path.join(TEST_DIR, 'test_file.txt')
    test_dir = os.path.join(TEST_DIR, 'test_dir')
    test_link = os.path.join(TEST_DIR, 'test_link.txt')

# Generated at 2022-06-13 20:55:44.669483
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    chown('/tmp/flutils.tests.osutils.txt')
    chown('/tmp/*', user='root', group='root')
    chown('/tmp/', user='root', group='root')
    chown('/tmp', user='root', group='root')
    # chown('/tmp', user='root', None)
    # chown('/tmp', user='root', group=None)



# Generated at 2022-06-13 20:55:59.039369
# Unit test for function chown
def test_chown():
    import os
    import stat
    import tempfile
    import textwrap
    import time
    import unittest

    from flutils.lists import is_seq_all_equal
    from flutils.pathutils import (
        chown,
        directory_present,
        get_os_user,
        get_os_group,
        normalize_path,
    )

    from flutils.tests import do_not_run_test

    # Skip these tests if not running as root
    if do_not_run_test(reason='Not running as root') is True:
        return

    # os.chown() does not seem to work for the default
    # directory for a user when that directory is a
    # symlink to another directory.  An example of this
    # is when users log into a system that is set up
    #

# Generated at 2022-06-13 20:56:08.908595
# Unit test for function path_absent
def test_path_absent():
    path = Path('/tmp/test_absent')
    path.mkdir()
    path_absent(path)
    assert path.exists() is False
    path.mkdir()
    (path / 'test_file').touch()
    path_absent(path)
    assert path.exists() is False
    path.mkdir()
    (path / 'test_dir').mkdir()
    (path / 'test_dir' / 'test_dir_file').touch()
    path_absent(path)
    assert path.exists() is False


# Generated at 2022-06-13 20:56:11.295443
# Unit test for function directory_present
def test_directory_present():
    assert directory_present('/tmp/', user='foo') == Path('/tmp/')



# Generated at 2022-06-13 20:56:17.572745
# Unit test for function chmod
def test_chmod():
    # Test the normalize_path method first for determining which tests to run
    assert chmod.__doc__ is not None
    assert chmod('~/tmp/flutils.tests.osutils.txt', 0o660) is None
    assert chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770) is None
    assert chmod('~/tmp/*') is None



# Generated at 2022-06-13 20:56:29.995322
# Unit test for function path_absent
def test_path_absent():
    path = Path('~/tmp/test_dir')
    path = normalize_path(path)
    path = path.as_posix()
    dir_path = path + '/'
    file_path = path + '/file'
    symlink_path = path + '/symlink'
    dir_path_in_dir = path + '/foo/bar'
    file_path_in_dir = path + '/foo/baz'
    symlink_path_in_dir = path + '/foo/qux'
    os.makedirs(dir_path_in_dir, mode=0o777, exist_ok=False)
    with open(file_path_in_dir, 'w+') as f:
        f.write('test text')

# Generated at 2022-06-13 20:56:37.575542
# Unit test for function chown
def test_chown():
    with TemporaryDirectory() as td:
        path = Path(td) / 'flutils' / 'tests' / 'osutils.txt'
        path.parent.mkdir(parents=True)
        path.touch()
        assert path.is_file() is True
        assert path.exists() is True

        chown(path, user=getpass.getuser(), group=getpass.getuser())
        assert path.owner() == getpass.getuser()

        chown(path.parent, user=getpass.getuser(), group=getpass.getuser())
        assert path.parent.owner() == getpass.getuser()



# Generated at 2022-06-13 20:56:50.226026
# Unit test for function chmod
def test_chmod():
    # TODO: Improve this test
    #       (i.e. better coverage)
    tmp = Path(tempfile.mkdtemp(prefix='flutils_', suffix='_tests_osutils'))

    txt = tmp / 'flutils.tests.osutils.txt'
    txt.touch()
    assert txt.exists() is True
    assert txt.is_dir() is False
    assert txt.is_file() is True
    assert txt.is_symlink() is False
    assert txt.stat().st_mode == 33188

    chmod(txt, 0o660)
    assert txt.stat().st_mode == 33204

    tmp_lvl1 = Path(tmp / 'level_1')
    tmp_lvl1.mkdir()

# Generated at 2022-06-13 20:57:02.215311
# Unit test for function chmod
def test_chmod():
    from os import makedirs
    from pathlib import Path
    from random import randint

    from flutils.pathutils import chmod
    from flutils.tests.helpers import rm_rf

    tst_dir = Path(Path(__file__).parent, 'test_chmod')
    if tst_dir.exists() is True:
        rm_rf(tst_dir)

    files = [
        Path(tst_dir, 'file_1.txt'),
        Path(tst_dir, 'file_2.txt'),
        Path(tst_dir, 'file_3.txt'),
        Path(tst_dir, 'file_4.txt')
    ]

    for f in files:
        if f.exists() is False:
            f.touch()


# Generated at 2022-06-13 20:57:23.091678
# Unit test for function chown
def test_chown():
    file_path = str(Path(__file__).parent / 'pathutils_test_chown.txt')
    with open(file_path, 'w'):
        pass

    chown(file_path, user='nobody', group='nogroup')
    stat_info = os.stat(file_path)
    nobody_stat_info = get_os_user('nobody')
    nogroup_stat_info = get_os_group('nogroup')
    msg = (
        'Expected uid=%s and gid=%s for path "%s", '
        'but got uid=%s and gid=%s'
    )
    assert stat_info.st_uid == nobody_stat_info.pw_uid
    assert stat_info.st_gid == nogroup_stat_

# Generated at 2022-06-13 20:57:33.640522
# Unit test for function chmod
def test_chmod():
    import os
    import shutil
    import tempfile
    import json
    import sys

    from os import PathLike
    from pathlib import (
        Path,
        PosixPath,
        WindowsPath,
    )
    from typing import (
        Deque,
        Generator,
        Optional,
        Union,
        cast,
    )
    from pathlib import Path
    from flutils.pathutils import chmod
    from unittest_expander import (
        expand,
        foreach,
    )

    # Expand the following unit test

# Generated at 2022-06-13 20:57:43.841648
# Unit test for function find_paths
def test_find_paths():
    """Test the function find_paths with a '~' and without a '~'"""
    with tempfile.TemporaryDirectory(prefix='ut_') as dtemp:
        f1 = Path(dtemp, 'file_one')
        f1.touch()
        f2 = Path(dtemp, 'file_two.txt')
        f2.touch()
        d1 = Path(dtemp, 'dir_one')
        d1.mkdir()

        # Test not using a '~'
        for found_path in find_paths(dtemp + '/*'):
            assert found_path.is_absolute() is True

        # Test using a '~'
        for found_path in find_paths('~/tmp/*'):
            assert found_path.is_absolute() is True

# Generated at 2022-06-13 20:57:54.036556
# Unit test for function find_paths
def test_find_paths():
    """Unit test for function ``find_paths``."""

    # noinspection SpellCheckingInspection
    TEST_DIR = Path(normalize_path('~/tmp/flutils.tests.pathutils'))
    TEST_DIR.mkdir(parents=True, exist_ok=True)

    TEST_FILE = TEST_DIR / 'test_file.txt'
    TEST_FILE.touch()
    TEST_FILE_UNREADABLE = TEST_DIR / 'test_file_unreadable.txt'
    TEST_FILE_UNREADABLE.touch()
    TEST_FILE_UNREADABLE.chmod(mode=0o300)

    TEST_DIR_UNREADABLE = TEST_DIR / 'unreadable'
    TEST_DIR_UNREADABLE.mkdir()

# Generated at 2022-06-13 20:57:56.399506
# Unit test for function path_absent
def test_path_absent():
    return



# Generated at 2022-06-13 20:58:02.187082
# Unit test for function chmod
def test_chmod():
    path = '~/tmp/flutils.tests.pathutils.txt'
    mode_file = 0o660
    mode_dir = 0o770
    chmod(path, mode_file, mode_dir)
    assert os.stat(path).st_mode & 0o7777 == mode_file
    os.chmod(path, 0o000)

# Generated at 2022-06-13 20:58:03.200303
# Unit test for function chown
def test_chown():
    unittest.TestCase()



# Generated at 2022-06-13 20:58:04.991424
# Unit test for function chmod
def test_chmod():
    assert 1 == 1



# Generated at 2022-06-13 20:58:15.927082
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/') == 'directory'
    assert exists_as('/bin') == 'directory'
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/dev/fd') == 'directory'
    assert exists_as('/dev/fd/') == 'directory'
    assert exists_as('/dev/fd/2') == 'file'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/pts/0') == 'char device'

# Generated at 2022-06-13 20:58:27.678632
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/') == 'directory'
    assert exists_as('~/flutils') == 'directory'
    assert exists_as('~/flutils/__init__.py') == 'file'
    assert exists_as('~/flutils/pathutils.py') == 'file'
    assert exists_as(
        '~/flutils/tests/osutils.py'
    ) == 'file'
    assert exists_as('~/flutils/tests/test_osutils.py') == 'file'
    assert exists_as('~/flutils/tests/test_pytest_wrappers.py') == 'file'
    assert exists_as('~/flutils/utils.py') == 'file'



# Generated at 2022-06-13 20:58:50.106764
# Unit test for function find_paths
def test_find_paths():
    # pylint: disable=missing-docstring
    expected = [
        Path(__file__).parent / 'tests' / 'functional' / 'fixtures',
        Path(__file__).parent / 'tests' / 'functional' / 'fixtures'
        / 'file_one.txt',
        Path(__file__).parent / 'tests' / 'functional' / 'fixtures'
        / 'file_two.txt',
        Path(__file__).parent / 'tests' / 'functional' / 'fixtures'
        / 'sub_dir' / 'sub_file_one.txt',
        Path(__file__).parent / 'tests' / 'functional' / 'fixtures'
        / 'sub_dir' / 'sub_file_two.txt'
    ]

# Generated at 2022-06-13 20:59:02.581501
# Unit test for function path_absent
def test_path_absent():  # noqa: D103
    import shutil
    tmpdir = Path('~/tmp/utest').expanduser()
    tmpdir.mkdir(exist_ok=True)
    testdir = tmpdir / 'testdir'
    testdir.mkdir(exist_ok=True)
    testfile = tmpdir / 'testfile'
    testfile.touch()

# Generated at 2022-06-13 20:59:14.588012
# Unit test for function find_paths
def test_find_paths():
    from flutils.tests.osutils import (
        create_temp_file,
        create_temp_dir,
    )
    from flutils.pathutils import find_paths
    from pathlib import Path
    from typing import List
    import os

    temp_dir = Path(create_temp_dir())
    os.chmod(temp_dir.as_posix(), 0o700)

    temp_path = create_temp_file(
        prefix='test_file_',
        dirname=temp_dir
    )
    temp_file = Path(temp_path)
    os.chmod(temp_path, 0o600)

    temp_path = create_temp_file(
        prefix='test__',
        dirname=temp_dir
    )
    temp_file_two = Path(temp_path)
   

# Generated at 2022-06-13 20:59:26.752450
# Unit test for function chmod
def test_chmod():
    import unittest.mock as mock
    from flutils.pathutils import chmod

    fake_path_obj = mock.MagicMock(
        spec_set=PosixPath,
        is_dir=mock.MagicMock(return_value=False),
        is_file=mock.MagicMock(return_value=True),
        exists=mock.MagicMock(return_value=True),
        chmod=mock.MagicMock()
    )
    fake_path_obj.parent.is_dir.return_value = True
    fake_path_obj.glob.return_value = (
        PosixPath('/tmp/flutils.tests.osutils.txt'),
        PosixPath('/tmp/flutils.tests.osutils.dir')
    )

# Generated at 2022-06-13 20:59:39.693112
# Unit test for function find_paths
def test_find_paths():
    pattern = '~/tmp/**'
    path_list = list(find_paths(pattern))
    assert len(path_list) == 2, 'The path list should be 2'
    assert (
        Path('~/tmp/flutils.tests.osutils.txt').as_posix()
        in path_list[0].as_posix()
    ), (
        'The path list should contain the file: '
        '"flutils.tests.osutils.txt".'
    )
    assert (
        Path('~/tmp/flutils.tests.osutils').as_posix()
        in path_list[1].as_posix()
    ), (
        'The path list should contain the directory: '
        '"flutils.tests.osutils".'
    )



# Generated at 2022-06-13 20:59:40.847297
# Unit test for function chmod
def test_chmod():
    assert True is True



# Generated at 2022-06-13 20:59:51.136595
# Unit test for function get_os_user
def test_get_os_user():
    assert get_os_user(os.getuid()).pw_name == getpass.getuser()
    assert get_os_user(getpass.getuser()).pw_uid == os.getuid()
    assert get_os_user(-1).pw_name == get_os_user().pw_name
    assert get_os_user(-1).pw_uid == get_os_user().pw_uid
    assert get_os_user(getpass.getuser()) == get_os_user()



# Generated at 2022-06-13 21:00:02.164856
# Unit test for function find_paths
def test_find_paths():
    from os import makedirs, remove
    from os.path import exists, join
    from tempfile import mkdtemp

    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        dir_one = join(str(tmpdir), 'dir_one')
        dir_two = join(str(tmpdir), 'dir_two')
        file_one = join(dir_one, 'file_one')
        file_two = join(dir_two, 'file_two')
        makedirs(dir_one)
        # Touch file_one
        with open(file_one, 'w'):
            pass
        makedirs(dir_two)
        # Touch file_two
        with open(file_two, 'w'):
            pass


# Generated at 2022-06-13 21:00:11.722558
# Unit test for function path_absent
def test_path_absent():
    path = '/tmp/path_absent.test'
    if os.path.exists(path):
        os.unlink(path)
    assert os.path.exists(path) is False
    path_absent(path)
    assert os.path.exists(path) is False
    with open(path, 'w') as fp:
        fp.write('')
    assert os.path.exists(path)
    path_absent(path)
    assert os.path.exists(path) is False



# Generated at 2022-06-13 21:00:21.729173
# Unit test for function path_absent
def test_path_absent():
    """Test the path_absent function."""
    import shlex
    from flutils.pathutils import path_absent, normalize_path, get_os_user

    user = get_os_user()
    temp_dir = normalize_path('~/tmp')
    temp_dir = temp_dir.as_posix()

    test_dir = os.path.join(temp_dir, 'test_dir')
    os.mkdir(test_dir)

    os.chdir(test_dir)

    file1 = os.path.join(test_dir, 'file1')
    with open(file1, 'wt') as f:
        f.write("file1 contents")

    file2 = os.path.join(test_dir, 'file2')

# Generated at 2022-06-13 21:00:30.006217
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:00:31.603797
# Unit test for function chown
def test_chown():
    chown('/tmp/flutils.tests.osutils.txt', user='rbryant', group='rbryant')



# Generated at 2022-06-13 21:00:39.311269
# Unit test for function chown
def test_chown():
    if os.getuid() == 0:
        os.chown('/tmp/flutils/osutils/chown', 1000, 1000)
        os.chown('/tmp/flutils/osutils/chown', -1, 1000)
        os.chown('/tmp/flutils/osutils/chown', 1000, -1)
        os.chown('/tmp/flutils/osutils/chown', -1, -1)



# Generated at 2022-06-13 21:00:51.240505
# Unit test for function directory_present
def test_directory_present():
    ######################################################################
    # Create the directory if does not exist.
    pwd = normalize_path('~')
    path = directory_present(pwd)
    assert exists_as(path) == 'directory'
    assert path.is_absolute()

    pwd = normalize_path('~')
    path = directory_present(pwd)
    assert exists_as(path) == 'directory'
    assert path.is_absolute()

    ######################################################################
    # Create the directory and its parents if do not exist.
    path = directory_present(pwd / 'flutils')
    assert exists_as(path) == 'directory'

    ######################################################################
    # Bad mode
    path = directory_present(pwd / 'flutils', mode="foo")

# Generated at 2022-06-13 21:01:03.150963
# Unit test for function path_absent
def test_path_absent():
    """Unit test for function path_absent.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / 'dir_one' / 'dir_two'
        path.mkdir(parents=True)
        (path / 'file_one').touch()
        path = '%s/dir_one/dir_two' % tmpdir
        path_absent(path)
        assert not os.path.exists(path)

        path = Path(tmpdir) / 'dir_one' / 'dir_two'
        path.mkdir(parents=True)
        (path / 'file_one').touch()
        path = '%s/dir_one/dir_two' % tmpdir
        path_absent(path)
        assert not os.path.exists(path)



# Generated at 2022-06-13 21:01:16.828908
# Unit test for function exists_as
def test_exists_as():
    """Test the exists_as() function."""
    file_name = 'exists_as.txt'
    dir_name = 'exists_as.dir'
    path = normalize_path(
        '~/tmp/{file_name}'.format(file_name=file_name)
    )
    path_dir = path.parent
    path_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    path.touch(mode=0o600, exist_ok=True)

    assert exists_as(path) == 'file'

    path.unlink()

    assert exists_as(path) == ''

    path_dir.rename(
        '~/tmp/{dir_name}'.format(dir_name=dir_name)
    )


# Generated at 2022-06-13 21:01:29.772462
# Unit test for function chown
def test_chown():
    """Test function osutils.chown()."""

    import osutils
    import tempfile

    temp_dir = tempfile.TemporaryDirectory()
    temp_file = Path(temp_dir.name) / 'foo.txt'
    temp_file.touch()

    # Test glob pattern
    osutils.chown(str(temp_file))
    osutils.chown(str(temp_file.parent / 'foo*.txt'))

    # Test no glob pattern
    osutils.chown(str(temp_file))

    # Test include_parent=True
    osutils.chown(str(temp_file.parent / 'foo*.txt'), include_parent=True)

    # Test user= and group=
    osutils.chown(str(temp_file), user='root', group='wheel')

    # Test user=-

# Generated at 2022-06-13 21:01:40.200358
# Unit test for function directory_present
def test_directory_present():
    exc_caught = False
    target_path = Path('~/tmp/test_directory_present').expanduser()
    try:
        directory_present(target_path)
    except ValueError:
        exc_caught = True
    assert exc_caught is True
    exc_caught = False
    target_path = Path('~/.tmp/test_directory_present').expanduser()
    try:
        directory_present(target_path)
    except ValueError:
        exc_caught = True
    assert exc_caught is True
    try:
        Path(target_path).unlink()
    except FileNotFoundError:
        pass
    try:
        Path(target_path).parent.unlink()
    except FileNotFoundError:
        pass

# Generated at 2022-06-13 21:01:43.187917
# Unit test for function path_absent
def test_path_absent():
    with pytest.raises(FileExistsError):
        path_absent("")



# Generated at 2022-06-13 21:01:44.084703
# Unit test for function chmod
def test_chmod(): pass



# Generated at 2022-06-13 21:02:00.825194
# Unit test for function chmod
def test_chmod():
    chmod('~/tmp/flutils.tests.osutils.txt', 0o660)
    chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770)
    chmod('~/tmp/*')
    assert True

# Generated at 2022-06-13 21:02:12.891437
# Unit test for function chmod
def test_chmod():
    from shutil import rmtree
    from tempfile import mkdtemp

    def _test(
            test_path: Path
    ):
        # Shouldn't do anything if the path does not exist
        chmod(test_path)
        assert test_path.stat().st_mode & 0o777 == 0o600

        test_file = test_path / 'test.txt'
        with open(test_file, 'w') as fp:
            fp.write('Test 1')

        # Should change the mode of only the file
        chmod(test_file, 0o640)
        assert test_file.stat().st_mode & 0o777 == 0o640

        # Should change the mode of the file and directory
        chmod(test_path, 0o660, 0o770)

# Generated at 2022-06-13 21:02:25.389355
# Unit test for function chown
def test_chown():
    user = getpass.getuser()
    group = grp.getgrgid(pwd.getpwnam(user).pw_gid).gr_name

    path = Path('/tmp/flutils.tests.osutils.txt')
    path.write_text('')
    _path1 = Path('/tmp/flutils.tests.osutils')
    _path1.mkdir()
    _path2 = Path('/tmp/flutils.tests.osutils/flutils.tests.osutils.txt.txt')
    _path2.write_text('')
    _path3 = Path('/tmp/flutils.tests.osutils/flutils.tests.osutils.txt.txt.txt')
    _path3.write_text('')

    chown(path, user)

# Generated at 2022-06-13 21:02:37.301380
# Unit test for function chmod
def test_chmod():
    path = normalize_path('/tmp/flutils.tests.osutils/')
    path.mkdir(mode=0o700, parents=True)
    path.joinpath('test.txt').touch()
    chmod(Path('/tmp/flutils.tests.osutils/test.txt'))
    chmod(Path('/tmp/flutils.tests.osutils'))
    chmod(Path('/tmp/flutils.tests.osutils/test.txt'), mode_file=0o776)
    chmod(Path('/tmp/flutils.tests.osutils'), mode_dir=0o776)
    chmod("/tmp/flutils.tests.osutils/test.txt")
    chmod("/tmp/flutils.tests.osutils/")



# Generated at 2022-06-13 21:02:39.335249
# Unit test for function chown
def test_chown():
    assert True
# @pastefix
# def test_chown():
#     pass



# Generated at 2022-06-13 21:02:48.399011
# Unit test for function directory_present
def test_directory_present():
    import os
    import tempfile
    from flutils.pathutils import directory_present
    testpath = '~/testdirectory_present'
    testpath = directory_present(testpath)
    try:
        assert isinstance(testpath, os.fspath(testpath))
    except TypeError:
        assert isinstance(testpath, os.PathLike)
    finally:
        assert testpath.is_file() is False
        assert testpath.is_dir() is True
        testpath.chmod(0o777)
        testpath.rmdir()
    testpath = os.path.join(tempfile.gettempdir(), 'testdirectory_present')
    testpath = directory_present(testpath)

# Generated at 2022-06-13 21:02:52.599929
# Unit test for function chown
def test_chown():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpfile = Path(tmpdir) / 'foo'
        tmpfile.touch()
        chown(tmpfile)
        try:
            chown(tmpfile, 'foo')
        except OSError:
            pass
        else:
            assert False, 'Expected OSError: No such user'
        try:
            chown(tmpfile, group='foo')
        except OSError:
            pass
        else:
            assert False, 'Expected OSError: No such group'



# Generated at 2022-06-13 21:03:06.355269
# Unit test for function chown
def test_chown():
    # Test a path that doesn't exist
    chown(Path(os.environ['HOME'], 'flutils.tests.osutils.txt'))

    chown(Path(os.environ['HOME'], 'flutils.tests.osutils.txt'), '-1', '-1')

    chown(Path(os.environ['HOME'], 'flutils.tests.osutils.txt'),
          user=os.environ['USER'],
          group=os.environ['USER'])

    with open('flutils.tests.osutils.txt', 'a+'):
        pass

    chown(Path('flutils.tests.osutils.txt'))

    chown(Path('flutils.tests.osutils.txt'), '-1', '-1')


# Generated at 2022-06-13 21:03:17.101895
# Unit test for function exists_as
def test_exists_as():
    """Test the exists_as function."""
    from tempfile import TemporaryDirectory
    from flutils.pathutils import ensure_exists, exists_as
    from flutils.systemutils import get_os_user

    with TemporaryDirectory() as temp:
        ensure_exists(os.path.join(temp, 'foo', 'bar', 'baz'))
        paths = [
            os.path.join(temp, 'foo'),
            os.path.join(temp, 'foo', 'bar'),
            os.path.join(temp, 'foo', 'bar', 'baz'),
        ]
        assert [
            exists_as(p) for p in paths
        ] == ['directory', 'directory', 'directory']


# Generated at 2022-06-13 21:03:25.405093
# Unit test for function chown
def test_chown():
    path = Path('/tmp/flutils.tests/os/chown')
    path.mkdir(parents=True)
    chown(str(path), user=getpass.getuser(), group=getpass.getuser())
    assert path.stat().st_uid == os.getuid()
    assert path.stat().st_gid == os.getgid()
    path.rmdir()

