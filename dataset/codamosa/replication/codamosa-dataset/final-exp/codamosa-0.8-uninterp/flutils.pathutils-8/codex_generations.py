

# Generated at 2022-06-13 20:54:33.157597
# Unit test for function chmod
def test_chmod():
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory(prefix='flutils-') as temp_dir:
        temp_dir = Path(temp_dir)

        fname = temp_dir.joinpath('flutils.tests.osutils.txt')
        with fname.open('w'):
            pass

        chmod(fname, 0o660)
        assert fname.stat().st_mode == 0o100660
        chmod(temp_dir.joinpath('*.txt'), mode_file=0o666)
        assert fname.stat().st_mode == 0o100666

        # Make sure it chmods the parent dir
        chmod(temp_dir.joinpath('*.txt'), mode_file=0o660, include_parent=True)

# Generated at 2022-06-13 20:54:36.980766
# Unit test for function find_paths
def test_find_paths():
    pattern = '~/tmp/*'
    search = normalize_path(pattern).as_posix()[len(pattern.anchor):]
    assert find_paths(pattern) == Path(pattern.anchor).glob(search)



# Generated at 2022-06-13 20:54:42.629500
# Unit test for function chown
def test_chown():
    path = Path('/tmp/foo/bar/baz.txt')
    path.parent.mkdir(parents=True)
    path.touch()
    chown(path, user='root')
    chown(path, group='root')



# Generated at 2022-06-13 20:54:53.865342
# Unit test for function find_paths
def test_find_paths():
    from pathlib import Path

    from flutils.pathutils import find_paths

    # Case 1
    # Create a directory and a file in it.
    tmp = Path('~/tmp/find_paths').expanduser()
    tmp.mkdir(exist_ok=True, parents=True)
    (tmp / 'file_one').touch()

    # Test for the file.
    paths = list(find_paths(tmp.as_posix() + '/*'))
    assert str(paths[0]) == (tmp / 'file_one').as_posix()

    # Case 2
    # Create a directory and a file in it.
    tmp = Path('~/tmp/find_paths_two').expanduser()
    tmp.mkdir(exist_ok=True, parents=True)

# Generated at 2022-06-13 20:55:01.119370
# Unit test for function path_absent
def test_path_absent():
    path_cfg = {
        'mode': 0o700,
        'user': get_os_user().pw_name,
        'group': get_os_group().gr_name
    }

    # Delete the path if it exists.
    path_absent('/tmp/foo/bar')

    # Create a directory with a couple of files in it.
    path_exists('/tmp/foo', mode=path_cfg['mode'],
                user=path_cfg['user'], group=path_cfg['group'])
    path_exists('/tmp/foo/bar', mode=path_cfg['mode'],
                user=path_cfg['user'], group=path_cfg['group'])

    open('/tmp/foo/bar/baz.txt', 'w+').close()

# Generated at 2022-06-13 20:55:09.656090
# Unit test for function path_absent
def test_path_absent():
    """Test function path_absent"""
    path = Path('~/tmp/test_path')
    path = path.expanduser()
    try:
        test_path = path_present(path)
        path_absent(test_path)
        assert not exists_as(test_path)
    finally:
        if isinstance(path, Path):
            path = path.as_posix()
        if os.path.exists(path):
            shutil.rmtree(path)



# Generated at 2022-06-13 20:55:21.707175
# Unit test for function exists_as
def test_exists_as():
    original = os.environ['PATH']
    test_path = '/tmp/flutils.test.test_pathutils.test_exists_as'

# Generated at 2022-06-13 20:55:30.018943
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod, normalize_path
    from pathlib import Path

    tmp_dir = Path(__file__).parent.parent / 'tmp' / 'flutils' / 'chmod'
    tmp_dir.mkdir(exist_ok=True, parents=True)
    tmp_file = tmp_dir / 'test.txt'
    tmp_file.touch()

    # first unchange anything that was done in a previous test
    # and make sure the files have the right mode.

# Generated at 2022-06-13 20:55:42.400680
# Unit test for function chmod
def test_chmod():
    """Unit test for function ``chmod``."""

    files = [
        '~/tmp/osutils/a/b/a.txt',
        '~/tmp/osutils/a/b/d.txt',
        '~/tmp/osutils/c/c.txt',
        '~/tmp/osutils/a/b/d/e.txt'
    ]

    for f in files:
        Path(f).parent.mkdir(parents=True, exist_ok=True)
        Path(f).touch()

    # chmod(~/tmp/osutils/a/**, 0o755, 0o750)
    chmod('~/tmp/osutils/a/**', mode_file=0o755, mode_dir=0o750)

# Generated at 2022-06-13 20:55:42.972012
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:55:59.277443
# Unit test for function chown
def test_chown():
    r"""Test function chown.
    """
    pass



# Generated at 2022-06-13 20:56:01.845735
# Unit test for function chown
def test_chown():
    raise NotImplementedError('Test functionality not covered')



# Generated at 2022-06-13 20:56:09.384605
# Unit test for function get_os_user
def test_get_os_user():
    '''
    Test the function get_os_user.
    '''
    res = get_os_user('root')
    assert '0' == res.pw_uid
    assert 'root' == res.pw_name
    assert 'root' == res.pw_dir
    res = get_os_user()
    assert '1001' == res.pw_uid
    assert 'foo' == res.pw_name
    assert '/home/foo' == res.pw_dir



# Generated at 2022-06-13 20:56:21.447793
# Unit test for function exists_as
def test_exists_as():
    """Tests for function exists_as."""
    from tempfile import TemporaryDirectory
    from datetime import datetime
    from flutils.pathutils import exists_as, __flutils_normalize_path

    now = datetime.utcnow()
    with TemporaryDirectory() as tempdir:
        tmpdir = Path(tempdir)
        # Ensure path that does NOT exist returns an empty string.
        assert exists_as(tmpdir / 'foo') == ''

        # Create some directories and files.
        # NOTE: In the future, I may want to refactor this to
        # be more explicit what the test is checking, but for
        # testing PoC, I just went with the pythonic approach.
        tmpdir.mkdir(mode=0o777)
        (tmpdir / 'foo').touch(mode=0o666)

# Generated at 2022-06-13 20:56:33.264244
# Unit test for function chown
def test_chown():
    old_passwd_getpwall = pwd.getpwall
    old_grp_getgrall = grp.getgrall

    test_user = pwd.struct_passwd(
        name='test',
        passwd='test',
        uid=1000,
        gid=1000,
        gecos='test',
        dir='test',
        shell='test'
    )

    test_group = grp.struct_group(
        gr_name='test',
        gr_passwd='test',
        gr_gid=1000,
        gr_mem=['test', ]
    )

    test_path = Path('/tmp/.flutils_test_chown_file')


# Generated at 2022-06-13 20:56:35.423962
# Unit test for function chown
def test_chown():
    assert chown is not None



# Generated at 2022-06-13 20:56:46.058421
# Unit test for function path_absent
def test_path_absent():
    # Cleanup previous test.
    path = '~/tmp/test_path'
    if os.path.exists(path):
        path_absent(path)
    # Test.
    path_present(path, dir=True)
    path_present(os.path.join(path, 'foo.txt'), content=b'Test')
    with open(os.path.join(path, 'bar.txt'), 'wb') as fh:
        fh.write(b'Test')
    path_present(os.path.join(path, 'baz.txt'))
    os.symlink('bar.txt', os.path.join(path, 'bar_link.txt'))
    os.symlink('tmp', os.path.join(path, 'tmp_link'))

# Generated at 2022-06-13 20:56:56.770638
# Unit test for function chown
def test_chown():
    import random
    import string

    random_str = ''.join([
        random.choice(string.ascii_letters) for _ in range(5)
    ])
    test_path = Path(f'/tmp/{random_str}.txt')
    test_path.touch()

    try:
        chown(test_path, include_parent=True)
        assert getpass.getuser() == test_path.owner()
    finally:
        if test_path.exists():
            test_path.unlink()

    try:
        chown(test_path, group='root')
        assert 'root' == test_path.group()
    finally:
        if test_path.exists():
            test_path.unlink()



# Generated at 2022-06-13 20:56:57.587683
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:56:59.042401
# Unit test for function get_os_group
def test_get_os_group():
    assert get_os_group('bar') == grp.struct_group(
        gr_name='bar',
        gr_passwd='*',
        gr_gid=2001,
        gr_mem=['foo']
    )



# Generated at 2022-06-13 20:57:31.960500
# Unit test for function find_paths
def test_find_paths():
    tmp_dir = Path(__file__).parent.as_posix() + '/tmp/'
    assert list(find_paths(tmp_dir + '*.txt')) == [
        Path(tmp_dir + 'file_one.txt'),
        Path(tmp_dir + 'file_two.txt')]
    assert list(find_paths(tmp_dir + '*')) == [
        Path(tmp_dir + 'dir_one'),
        Path(tmp_dir + 'file_one.txt'),
        Path(tmp_dir + 'file_two.txt')]
    assert list(find_paths(tmp_dir)) == [Path(tmp_dir)]



# Generated at 2022-06-13 20:57:43.094824
# Unit test for function chown
def test_chown():
    # short circuit if not running as root
    if 'SUDO_UID' not in os.environ:
        return None

    uid = int(os.environ.get('SUDO_UID'))
    gid = int(os.environ.get('SUDO_GID'))

    path = Path('./tmp/flutils.tests.osutils').expanduser()

    if path.exists():
        chown(path=path, user=uid, group=gid)
        assert path.stat().st_uid == uid
        assert path.stat().st_gid == gid
        chown(path=path, user='-1', group='-1')
        assert path.stat().st_uid == uid
        assert path.stat().st_gid == gid


# Generated at 2022-06-13 20:57:53.432711
# Unit test for function chmod
def test_chmod():
    from shutil import copyfile, rmtree
    from tempfile import TemporaryDirectory

    import pytest  # type: ignore
    from py._path.local import LocalPath  # type: ignore

    # Create a temp directory to do some file system operations on.
    with TemporaryDirectory() as temp_dir:
        temp_dir = LocalPath(temp_dir)

        # The data to be written to the file.
        data = '0123456789'

        # Create a file on the file system.
        file_path = temp_dir.join('flutils.tests.osutils.txt')
        file_path.write(data)

        # Create a directory on the file system.
        dir_path = temp_dir.join('tests')
        dir_path.ensure_dir()

        # Copy the file to the directory.
        copy

# Generated at 2022-06-13 20:58:05.566253
# Unit test for function chmod
def test_chmod():
    import subprocess
    import unittest

    class TestChmod(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.tmpdir = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            )
            cls.tmpdir = os.path.join(cls.tmpdir, 'tmp')

            cls.path = os.path.join(cls.tmpdir, 'chmod')
            cls.path_child = os.path.join(cls.path, 'child')

            os.mkdir(cls.path)
            os.mkdir(cls.path_child)


# Generated at 2022-06-13 20:58:06.195529
# Unit test for function chmod
def test_chmod():
    return



# Generated at 2022-06-13 20:58:16.284561
# Unit test for function find_paths
def test_find_paths():
    with tempfile.TemporaryDirectory() as tmpdir:
        current_path = Path(tmpdir)
        Path(current_path.joinpath('file_one')).touch()
        Path(current_path.joinpath('file_two')).touch()
        Path(current_path.joinpath('dir_one')).mkdir()
        Path(current_path.joinpath('dir_two')).mkdir()
        assert len(list(find_paths(current_path.joinpath('**')))) == 4
        assert len(list(find_paths(current_path.joinpath('*')))) == 4
        assert len(list(find_paths(current_path.joinpath('dir_*')))) == 2
        assert len(list(find_paths(current_path.joinpath('file_*')))) == 2


# Generated at 2022-06-13 20:58:17.592752
# Unit test for function get_os_group
def test_get_os_group():
    group_name = TEST_GROUP_NAME
    group = get_os_group(group_name)
    assert group.gr_name == group_name
    assert group.gr_gid == TEST_GROUP_ID



# Generated at 2022-06-13 20:58:30.473931
# Unit test for function find_paths
def test_find_paths():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from textwrap import dedent

    with TemporaryDirectory(suffix='_flutils_tests') as tmpdir:
        tmpdir = Path(tmpdir)
        file_one = tmpdir / 'file_one'
        file_one.touch()
        dir_one = tmpdir / 'dir_one'
        dir_one.mkdir()

        pattern = tmpdir / '*'
        results = list(find_paths(pattern))
        assert results[0] == file_one
        assert results[1] == dir_one

        assert str(find_paths(pattern)) == dedent(
            '''
            <generator object find_paths at 0x7fda5dd6f948>
            '''
        ).strip()

        pattern = tmpdir

# Generated at 2022-06-13 20:58:41.950384
# Unit test for function find_paths
def test_find_paths():
    root = Path(__file__).parent
    fixture = root / 'data' / 'find_paths'
    # Directory
    actual = find_paths(fixture / '**' / '*')
    expected = [
        fixture / 'test_one.txt',
        fixture / 'test_two.txt',
        fixture / 'test_three.txt',
        fixture / 'test_four.txt',
    ]
    assert list(actual) == expected
    # File
    actual = find_paths(fixture / '**' / '*.txt')
    expected = [
        fixture / 'test_one.txt',
        fixture / 'test_two.txt',
        fixture / 'test_three.txt',
        fixture / 'test_four.txt',
    ]
    assert list(actual) == expected
    # Anch

# Generated at 2022-06-13 20:58:51.010696
# Unit test for function path_absent
def test_path_absent():
    tmpdir = Path(tempfile.mkdtemp())

# Generated at 2022-06-13 20:59:33.604127
# Unit test for function chown
def test_chown():
    # TODO: This test needs to be written
    assert True is True



# Generated at 2022-06-13 20:59:43.614537
# Unit test for function chmod
def test_chmod():
    from ._utils import (
        FunctionTestCase,
        MockGrpModule,
        MockOsModule,
        MockPwdModule,
        PathMock,
    )

    # Mock the os related modules
    mock_os = MockOsModule()
    mock_grp = MockGrpModule()
    mock_pwd = MockPwdModule()

    # create the test case

# Generated at 2022-06-13 20:59:53.841480
# Unit test for function chmod
def test_chmod():
    import tempfile
    from flutils.testutils import capture_sys_output

    _temp_dir = tempfile.TemporaryDirectory()
    file_1 = Path(_temp_dir.name, 'file_1.txt')
    file_2 = Path(_temp_dir.name, 'file_2.txt')
    file_3 = Path(_temp_dir.name, 'file_3.txt')
    file_4 = Path(_temp_dir.name, 'file_1.txt/file_4.txt')
    file_5 = Path(_temp_dir.name, 'file_1.txt/file_5.txt')
    file_6 = Path(_temp_dir.name, 'file_1.txt/file_6.txt')
    dir_1 = Path(_temp_dir.name, 'dir_1')
    dir_

# Generated at 2022-06-13 20:59:54.542490
# Unit test for function chown
def test_chown():
    chown('~/tmp/*')



# Generated at 2022-06-13 20:59:55.765242
# Unit test for function chmod
def test_chmod():
    chmod('../docs/index.rst')
    chmod.__annotations__



# Generated at 2022-06-13 21:00:05.471420
# Unit test for function chown
def test_chown():
    if os.name == 'nt':
        raise NotImplementedError('Function not implemented on a Windows system')

    path = './testing.txt'
    with open(path, 'w'):
        pass

    # normalize_path will return a PosixPath on a Posix system.
    path = normalize_path(path)
    assert path.exists() is True

    try:
        owner = getpass.getuser()
        group = grp.getgrgid(path.stat().st_gid).gr_name
    except KeyError:
        owner = None
        group = None

    # Test that it defaults to the current user's
    # user and group.
    chown(path)
    assert path.owner() == owner
    assert path.group() == group

    # Test that an int is accepted for user

# Generated at 2022-06-13 21:00:12.354216
# Unit test for function chmod
def test_chmod():
    chmod.__doc__ = chmod.__doc__.split(u'\n')[6:]
    chmod(
        '~/tmp/flutils.tests.osutils.txt',
        0o660,
        0o770,
        '~/tmp/**',
        None,
        None,
        True,
        '~/tmp/*',
        None,
        None,
        False,
    )
    chmod.__doc__ = chmod.__doc__.split(u'\n')[2:]

# Generated at 2022-06-13 21:00:22.459326
# Unit test for function chmod
def test_chmod():
    d = Path('/tmp/flutils.tests.osutils.tmp_chmod')
    d.mkdir(parents=True, exist_ok=True)

    f = d / 'test.txt'
    with f.open(mode='wb') as fd:
        fd.write(b'test')

    assert chmod(f, 0o660) is None
    assert f.stat().st_mode & 0o777 == 0o660

    assert chmod(d, 0o770) is None
    assert d.stat().st_mode & 0o777 == 0o770

    v = Path('/tmp/flutils.tests.osutils.tmp_chmod/v')
    v.mkdir(parents=True, exist_ok=True)

    x = v / 'x'

# Generated at 2022-06-13 21:00:29.484873
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    chown('/tmp/flutils.tests.pathutils.txt', user='-1', group='-1')
    chown('/tmp/flutils.tests.pathutils.txt', user='-1', group='-1')
    chown('/tmp/flutils.tests.pathutils.txt', user='-1', group='-1')
    chown('/tmp/flutils.tests.pathutils.txt', user='-1', group='-1')



# Generated at 2022-06-13 21:00:41.510202
# Unit test for function chmod
def test_chmod():
    import os
    import shutil
    import tempfile
    from flutils.pathutils import chmod

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 21:01:09.023674
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/') == 'directory'
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/non-existing-path') == ''


# Generated at 2022-06-13 21:01:20.771773
# Unit test for function chmod
def test_chmod():
    """Unit test for function chmod.
    """
    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as td:
        Path(td).joinpath('file.txt').touch()
        path = (
            Path(td)
            .joinpath('sub')
            .joinpath('file.txt')
        )
        path.parent.mkdir()
        path.touch()
        chmod(Path(td).joinpath('sub/**'), mode_file=0o660, mode_dir=0o770)

    assert path.exists() is True
    assert path.is_dir() is False
    assert path.is_file() is True
    assert path.stat().st_mode == (0o660 | stat.S_IFREG)

    assert path.parent.exists() is True

# Generated at 2022-06-13 21:01:23.715798
# Unit test for function path_absent
def test_path_absent():
    with pytest.raises(Exception):
        path_absent('/etc/hosts')


# Generated at 2022-06-13 21:01:35.163064
# Unit test for function directory_present
def test_directory_present():
    from flutils.pathutils import directory_present
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp()
    tmpdir2 = Path(tmpdir) / 'dir2'
    tmpdir3 = tmpdir2 / 'dir3'

    tmpdir_obj = directory_present(tmpdir2)
    assert isinstance(tmpdir_obj, Path)
    assert tmpdir_obj.is_dir() is True
    assert tmpdir_obj.as_posix() == tmpdir2.as_posix()

    tmpdir3_obj = directory_present(tmpdir3)
    assert isinstance(tmpdir3_obj, Path)
    assert tmpdir3_obj.is_dir() is True
    assert tmpdir3_obj.as_posix() == tmpdir3.as_posix()

   

# Generated at 2022-06-13 21:01:48.620307
# Unit test for function chmod
def test_chmod():
    with TempDirectory(prefix='flutils_test_pathutils.chmod') as tmp_dir:
        # Test chmod a file
        file_path = os.path.join(
            tmp_dir,
            'flutils.tests.osutils.txt'
        )
        with open(file_path, 'w') as f:
            f.write('Hello world\n')

        # Ensure the file is 0o600
        fstat = os.stat(file_path)
        assert fstat.st_mode == (33188)  # 0o100600

        # Change file to 0o660
        chmod(file_path, 0o660)
        fstat = os.stat(file_path)
        assert fstat.st_mode == (33204)  # 0o100660

        # Change file to 0o600


# Generated at 2022-06-13 21:01:51.987573
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(Path(__file__)) == 'file'
    assert exists_as(Path(__file__).parent) == 'directory'
    assert exists_as('/Users/len/tmp') == ''



# Generated at 2022-06-13 21:02:05.715587
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import normalize_path
    from flutils.testhelpers import TempDir
    from flutils.testhelpers import TestCase
    import os
    import pathlib
    import shutil
    import unittest


    class TestPathAbsent(TestCase):
        def test_path_absent_directory_shallow(self):
            with TempDir() as tmpdir:
                tmpdir.create_dir('testdir')
                tmpdir.create_dir('testdir', 'subdir')
                tmpdir.create_file('testdir', 'subdir', 'file1')
                path = tmpdir.tmpdir.joinpath('testdir')
                path = pathlib.Path(path)
                assert os.path.exists(path)
                path_absent(path)

# Generated at 2022-06-13 21:02:13.400884
# Unit test for function path_absent
def test_path_absent():
    os.system("mkdir -p ~/tmp/test_path")
    assert os.path.exists("~/tmp/test_path")
    path_absent("~/tmp/test_path")
    assert not os.path.exists("~/tmp/test_path")
    os.system("mkdir -p ~/tmp/test_dir")
    os.system("touch ~/tmp/test_dir/test_file")
    assert os.path.exists("~/tmp/test_dir/test_file")
    path_absent("~/tmp/test_dir")
    assert os.path.exists("~/tmp/test_dir")
    assert not os.path.exists("~/tmp/test_dir/test_file")

# Generated at 2022-06-13 21:02:25.668924
# Unit test for function path_absent
def test_path_absent():
    with tempfile.TemporaryDirectory() as tdir:
        p1 = os.path.join(tdir, 'test_file')
        p2 = os.path.join(tdir, 'test_dir')
        p3 = os.path.join(p2, 'foo')
        with open(p1, 'w') as f:
            f.write('content')
        os.mkdir(p2)
        with open(p3, 'w') as f:
            f.write('sub directory file content')
        assert os.path.exists(p1)
        assert os.path.exists(p2)
        assert os.path.exists(p3)
        path_absent(p1)
        assert os.path.exists(p1) is False
        path_absent(p2)

# Generated at 2022-06-13 21:02:32.402166
# Unit test for function path_absent
def test_path_absent():
    path = Path('/tmp/path_absent_test_path')
    try:
        path_absent(path)
        assert not path.exists()
        assert not path.is_dir()
    finally:
        try:
            shutil.rmtree(path)
        except OSError:
            pass



# Generated at 2022-06-13 21:03:09.312163
# Unit test for function chmod
def test_chmod():
    return None



# Generated at 2022-06-13 21:03:18.661322
# Unit test for function chmod
def test_chmod():
    here = Path(__file__).parent
    tmpdir = here.joinpath('tmp')
    tmpdir.mkdir(exist_ok=True)

    fp = tmpdir.joinpath('flutils.tests.osutils.txt')
    fp.touch(exist_ok=True)
    os.chmod(fp, 0o700)
    assert oct(stat.S_IMODE(fp.stat().st_mode)) == '0o700'

    fp2 = tmpdir.joinpath('flutils.tests.osutils.txt2')
    fp2.touch(exist_ok=True)
    os.chmod(fp2, 0o400)
    assert oct(stat.S_IMODE(fp2.stat().st_mode)) == '0o400'


# Generated at 2022-06-13 21:03:34.270086
# Unit test for function directory_present
def test_directory_present():
    # pylint: disable=unused-variable
    # pylint: disable=missing-function-docstring
    def fn():
        import tempfile
        temp_dir = tempfile.TemporaryDirectory()

        assert os.path.exists(temp_dir.name) is True
        assert os.path.isdir(temp_dir.name) is True

        test_dir = directory_present(f'{temp_dir.name}/dir')
        assert test_dir.parent == Path(temp_dir.name)
        assert test_dir.is_dir() is True

        test_dir2 = directory_present(f'{temp_dir.name}/dir')
        assert test_dir2 == test_dir

    fn()
    assert True


