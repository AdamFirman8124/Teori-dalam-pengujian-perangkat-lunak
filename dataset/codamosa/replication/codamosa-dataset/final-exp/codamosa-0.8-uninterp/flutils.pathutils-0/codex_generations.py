

# Generated at 2022-06-13 20:54:29.497223
# Unit test for function path_absent
def test_path_absent():
    with tempfile.TemporaryDirectory() as tempdir:
        tmp_dir_path = Path(tempdir).as_posix()
        tmp_dir_path = cast(str, tmp_dir_path)
        tmp_path = os.path.join(tmp_dir_path, 'test_path')
        fname = os.path.join(tmp_path, 'test_file')

        path_absent(tmp_path)

        if os.path.exists(tmp_path):
            raise AssertionError('path_absent failed to remove the directory.')

        os.mkdir(tmp_path)

        path_absent(tmp_path)

        if os.path.exists(tmp_path):
            raise AssertionError('path_absent failed to remove an empty '
                'directory.')

        os

# Generated at 2022-06-13 20:54:38.231048
# Unit test for function find_paths
def test_find_paths():
    # Not sure how to test this function real well.
    # Because the test_data doesn't exist in ci
    # This is pretty much covered in test_normalize_path
    # but is test_data is not used in normalize_path
    # This is a fake path.
    _path = Path('/home/test_user/tmp')
    _path.mkdir(mode=0o700, parents=True)
    _path.joinpath('file_one').touch()
    _path.joinpath('dir_one').mkdir(parents=True)
    assert isinstance(find_paths('~/tmp/*'), Generator)



# Generated at 2022-06-13 20:54:51.907531
# Unit test for function find_paths
def test_find_paths():
    from flutils.pathutils import find_paths

    assert set(find_paths('~/tmp/*')) == set([])

    directory_present('~/tmp/file_one')
    directory_present('~/tmp/file_two')
    directory_present('~/tmp/file_three')
    directory_present('~/tmp/test')

    assert set(find_paths('~/tmp/*')) == set([
        Path('~/tmp/file_one'),
        Path('~/tmp/file_two'),
        Path('~/tmp/file_three'),
        Path('~/tmp/test'),
    ])

    assert set(find_paths('~/tmp/*_one')) == set([
        Path('~/tmp/file_one'),
    ])


# Generated at 2022-06-13 20:55:08.426717
# Unit test for function directory_present
def test_directory_present():
    from os import PathLike
    from pathlib import (
        Path,
        PosixPath,
        WindowsPath,
    )

    # FileExistsError for non directory.
    for path in (
        Path('/tmp/flutils/foo.txt'),
        PosixPath('/tmp/flutils/foo.txt'),
        WindowsPath('C:\\tmp\\flutils\\foo.txt'),
    ):
        should_raise = False
        try:
            assert directory_present(path) == cast(PathLike, path)
        except FileExistsError:
            should_raise = True
        assert should_raise is True

    # FileExistsError for parent non directory.
    path_parent = '~/tmp/flutils'
    path = Path('~/tmp/flutils/foo/bar')
    should_raise = False

# Generated at 2022-06-13 20:55:09.007261
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 20:55:13.704281
# Unit test for function chmod
def test_chmod():
    import logging
    import stat
    from flutils.logutils import BraceMessage as __

    logger = logging.getLogger(__name__)

    sub_path = '/tmp/flutils.tests.pathutils.test_chmod'
    logger.debug('sub_path: {}'.format(sub_path))

    try:
        os.makedirs(sub_path)
    except FileExistsError:
        pass

    logger.debug('{} created'.format(sub_path))

    try:
        with open(os.path.join(sub_path, 'test_chmod'), 'w'):
            pass
    except FileExistsError:
        pass

    logger.debug('{} created'.format(sub_path))

    os.chmod(sub_path, 0o700)

# Generated at 2022-06-13 20:55:25.121453
# Unit test for function chmod
def test_chmod():
    """Tests chmod function.
    """
    from flutils.pathutils import chmod
    from flutils.systemutils import umask
    from flutils.secureutils import randutils
    from tempfile import mkdtemp
    from shutil import rmtree

    umask(0o077)


# Generated at 2022-06-13 20:55:28.257361
# Unit test for function exists_as
def test_exists_as():

    assert exists_as('/') == 'directory'
    assert exists_as('~') == 'directory'
    assert exists_as('~/') == 'directory'
    assert exists_as('~//') == 'directory'
    assert exists_as('~/tmp/') == ''



# Generated at 2022-06-13 20:55:30.153558
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    from flutils.testingutils import capture_os_environ



# Generated at 2022-06-13 20:55:40.975580
# Unit test for function path_absent
def test_path_absent():
    with TemporaryDirectory() as d:
        base_path = Path(d)
        base_path = base_path.joinpath('tmp')
        base_path.mkdir()

        sub_dir = base_path.joinpath('tmp_dir')
        sub_dir.mkdir()

        sub_file = sub_dir.joinpath('tmp_file')
        sub_file.touch()

        sub_dir_empty = base_path.joinpath('tmp_dir_empty')
        sub_dir_empty.mkdir()

        path_absent(base_path.as_posix())
        assert base_path.exists() is False


# Generated at 2022-06-13 20:56:03.153367
# Unit test for function chown
def test_chown():
    import tempfile
    tmp_fp = tempfile.NamedTemporaryFile()
    chown(tmp_fp.name, 'root', 'root')
    assert True


# Generated at 2022-06-13 20:56:14.311919
# Unit test for function exists_as
def test_exists_as():
    from io import StringIO
    from sys import stderr

    from flutils.testing import capture_stderr
    from pathlib import Path

    real_home = Path.home()
    # Use a temp dir for testing
    Path.home = lambda _: Path('/tmp/home')

    existing_dir = Path('~/tmp')
    existing_file = existing_dir / 'flutils.tests.osutils.txt'
    # NOTE: This will not be a symlink because /proc
    # is not a real filesystem on Mac or Windows.
    if existing_dir / 'proc' != Path('/proc'):
        existing_symbolic_link = existing_dir / 'proc'
    else:
        existing_symbolic_link = existing_dir / 'symbolic_link'
        existing_symbolic_link

# Generated at 2022-06-13 20:56:26.354070
# Unit test for function chown
def test_chown():
    """Test function chown."""
    from flutils.pathutils import chown
    import os.path

    if os.name == 'posix':
        path = '/tmp/flutils.tests.pathutils.test_chown.txt'
        with open(path, 'wt') as fh:
            fh.write('TEST')

        assert os.path.isfile(path)
        assert os.path.exists(path)

        user = getpass.getuser()
        group = getpass.getuser()
        print('user: {}, group: {}'.format(user, group))
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(group).gr_gid

# Generated at 2022-06-13 20:56:36.697005
# Unit test for function directory_present
def test_directory_present():
    from tempfile import TemporaryDirectory
    from os import (
        makedirs,
        listdir,
    )
    from os.path import (
        isdir,
        join,
    )
    from shutil import rmtree
    from itertools import chain

    from flutils.pathutils import directory_present

    with TemporaryDirectory() as tmpdir:
        # test existing directory
        existing_dir = join(tmpdir, 'existing_dir')
        makedirs(existing_dir)
        assert isdir(existing_dir) is True

        directory_present(existing_dir)
        assert isdir(existing_dir) is True

        # test creating missing directory
        new_dir = join(tmpdir, 'new_dir')
        assert isdir(new_dir) is False

        directory_present(new_dir)
       

# Generated at 2022-06-13 20:56:43.808584
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/etc/') == 'directory'
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/etc/group') == 'file'
    assert exists_as('/dev/zero') == 'char device'
    assert exists_as('/dev/null') == 'char device'
    # Does not exist
    assert exists_as('/etc/asdf') == ''



# Generated at 2022-06-13 20:56:51.348011
# Unit test for function exists_as
def test_exists_as():
    import os
    import tempfile
    from pathlib import Path
    from flutils.pathutils import exists_as

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        assert exists_as(tmpdir) == 'directory'
        fd, fname = tempfile.mkstemp(dir=tmpdir)
        os.close(fd)
        fpath = Path(fname)
        assert exists_as(fpath) == 'file'
        os.unlink(fpath.as_posix())
        assert exists_as(fpath) == ''



# Generated at 2022-06-13 20:57:03.298218
# Unit test for function chown
def test_chown():
    # import os
    import os
    # dir_name = '/tmp/flutils.tests.osutils.dir'
    dir_name = '/tmp/flutils.tests.osutils.dir'
    # file_name = os.path.join(dir_name, 'foo.txt')
    file_name = os.path.join(dir_name, 'foo.txt')
    # os.makedirs(dir_name)
    os.makedirs(dir_name)
    # with open(file_name, 'w') as f:
    with open(file_name, 'w') as f:
        os.fchmod(f.fileno(), 0o600)
    # os.chmod(dir_name, 0o700)
    os.chmod(dir_name, 0o700)
    # chown

# Generated at 2022-06-13 20:57:13.181110
# Unit test for function path_absent
def test_path_absent():
    with open('tmp_file_1', 'w') as tmp_file_1:
        tmp_file_1.write('text')
    with open('tmp_file_2', 'w') as tmp_file_2:
        tmp_file_2.write('text')
    os.mkdir('tmp_dir_1')
    os.mkdir('tmp_dir_1/tmp_dir_2')
    with open('tmp_dir_1/tmp_dir_2/tmp_file_3', 'w') as tmp_file_3:
        tmp_file_3.write('text')
    os.symlink('tmp_dir_1', 'tmp_dir_1_link')
    os.symlink('tmp_dir_1/tmp_dir_2', 'tmp_dir_2_link')
    os.sy

# Generated at 2022-06-13 20:57:26.818898
# Unit test for function directory_present
def test_directory_present():
    p = directory_present('/tmp/test_path')
    assert isinstance(p, PosixPath)
    assert p.as_posix() == '/tmp/test_path'

    p = directory_present(p)
    assert isinstance(p, PosixPath)
    assert p.as_posix() == '/tmp/test_path'

    p = directory_present('/tmp/test_path_absent')
    assert isinstance(p, PosixPath)
    assert p.as_posix() == '/tmp/test_path_absent'
    assert p.exists() is True

    p = directory_present(p)
    assert isinstance(p, PosixPath)
    assert p.as_posix() == '/tmp/test_path_absent'
    assert p.exists() is True



# Generated at 2022-06-13 20:57:32.929691
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    from pathlib import Path

    assert exists_as(Path()) == ''
    assert exists_as(Path('/tmp')) == 'directory'
    assert exists_as(Path('/etc/hosts')) == 'file'
    assert exists_as(Path('/dev/sda')) == 'block device'
    assert exists_as(Path('/dev/tty')) == 'char device'



# Generated at 2022-06-13 20:57:59.584575
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/flutils.tests.osutils.txt') == 'file'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/zero') == 'block device'
    assert exists_as('/dev/log') == 'socket'
    with tempfile.NamedTemporaryFile(mode='w+') as tmp:
        tmp.write('test')
        tmp.flush()
        pathlib.Path(tmp.name).chmod(0o000)
        assert exists_as(tmp.name) == 'file'
        assert exists_as(os.path.dirname(tmp.name)) == 'directory'



# Generated at 2022-06-13 20:58:05.875049
# Unit test for function directory_present
def test_directory_present():
    directory_present('/tmp/a/b/c/d')
    directory_present('/tmp/a/b/c/d/')
    directory_present('/tmp/a/b/c/d/')
    directory_present('/tmp/a/b/c/d')
    directory_present('/tmp/a/b/c/d/')
    directory_present('/tmp/a/b/c/d/')

# Generated at 2022-06-13 20:58:12.467052
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    chown('/tmp', include_parent=True)
    chown('/tmp/*', include_parent=True)
    chown('/tmp/**', include_parent=True)
    chown('/tmp/flutils.*', include_parent=True)
    chown('/tmp/**/flutils.*', include_parent=True)



# Generated at 2022-06-13 20:58:26.234714
# Unit test for function exists_as
def test_exists_as():
    r"""Test exists_as()"""
    from flutils.pathutils import exists_as
    from flutils.pathutils import normalize_path
    from flutils.testing import FlutilsTestCase

    class TestExistsAs(FluutilsTestCase):
        def test_exists_as(self):
            self.assertEqual(exists_as(normalize_path('/foo')), '')
            self.assertEqual(exists_as(normalize_path('/bin')), 'directory')
            self.assertEqual(exists_as(normalize_path('/bin/bash')), 'file')
            self.assertEqual(exists_as(normalize_path('/dev/null')), 'char device')

# Generated at 2022-06-13 20:58:39.140468
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent as func
    from tempfile import TemporaryDirectory as tempdir

    with tempdir(dir='.') as tdir:
        os.chdir(tdir)

        subdir1 = os.path.join(tdir, 'subdir1')
        subdir2 = os.path.join(tdir, 'subdir2')
        subdir3 = os.path.join(tdir, 'subdir3')

        subdir_name = 'foo'
        foo = os.path.join(tdir, subdir_name)

        os.mkdir(subdir1)
        os.mkdir(subdir2)
        os.mkdir(subdir3)

        os.mkdir(foo)
        path = os.path.join(foo, 'bar')

# Generated at 2022-06-13 20:58:45.190304
# Unit test for function chown
def test_chown():
    from os import geteuid
    from os import getegid
    from os import getuid
    from os import getgid

    path = Path(__file__)
    if path.exists():
        path.touch()
    try:
        chown(path)
        # If we get here, the test passed.
    finally:
        path.unlink()



# Generated at 2022-06-13 20:58:52.200329
# Unit test for function exists_as
def test_exists_as():
    res = exists_as('/etc')
    assert res == 'directory'

    res = exists_as('/etc/hosts')
    assert res == 'file'

    res = exists_as('/dev/random')
    assert res == 'block device'

    res = exists_as('/dev/urandom')
    assert res == 'char device'

    res = exists_as('/dev/zero')
    assert res == 'block device'

    res = exists_as('/dev/null')
    assert res == 'char device'

    res = exists_as('/dev/console')
    assert res == 'char device'

    res = exists_as('/dev/tty')
    assert res == 'char device'

    res = exists_as('/dev/tty0')
    assert res == 'char device'

    res

# Generated at 2022-06-13 20:58:56.321721
# Unit test for function exists_as
def test_exists_as():
    the_path = Path('~/tmp/flutils.tests.pathutils.txt')
    assert exists_as(the_path.as_posix()) == ''

    the_path.touch()
    assert exists_as(the_path.as_posix()) == 'file'

    the_path.unlink()
    assert exists_as(the_path.as_posix()) == ''

    directory_present(the_path.parent)
    assert exists_as(the_path.parent.as_posix()) == 'directory'

    the_path.mkdir()
    assert exists_as(the_path.as_posix()) == 'directory'

    the_path.rmdir()
    assert exists_as(the_path.as_posix()) == ''

    the_path.touch()

# Generated at 2022-06-13 20:59:05.610660
# Unit test for function path_absent
def test_path_absent():
    """Test :func:`~flutils.pathutils.path_absent`."""
    from flutils.testhelpers import random_string, random_path

    # Test directories
    #
    _cleanup: List[str] = []
    path = random_path()
    os.mkdir(path)
    _cleanup.append(path)
    with open(os.path.join(path, random_string()), 'w') as fp:
        fp.write(random_string())
    path_absent(path)
    assert os.path.exists(path) is False

    path = random_path()
    os.mkdir(path)
    _cleanup.append(path)
    with open(os.path.join(path, random_string()), 'w') as fp:
        f

# Generated at 2022-06-13 20:59:15.858426
# Unit test for function directory_present
def test_directory_present():
    root = Path('/tmp/directory_present')
    try:
        # Using a Path object
        here = directory_present(root / 'here')
        assert here.as_posix() == '/tmp/directory_present/here'

        # Using a string
        there = directory_present(root.as_posix() + '/there')
        assert there.as_posix() == '/tmp/directory_present/there'

        # Using a bytes object
        nowhere = directory_present(root / 'nowhere')
        assert nowhere.as_posix() == '/tmp/directory_present/nowhere'

        # Force a failure
        path = root / 'there/here'
        with pytest.raises(FileExistsError):
            directory_present(path)
    finally:
        root.rmdir()



# Generated at 2022-06-13 20:59:39.893062
# Unit test for function chown
def test_chown():
    assert path_absent('~/tmp/chown.txt')
    assert path_absent('~/tmp/chown2.txt')
    assert path_absent('~/tmp/chown_group.txt')
    assert path_absent('~/tmp/chown2_group.txt')

    Path('~/tmp/chown.txt').touch()
    assert exists_as('~/tmp/chown.txt', 'file')

    Path('~/tmp/chown2.txt').touch()
    assert exists_as('~/tmp/chown2.txt', 'file')

    Path('~/tmp/chown_group.txt').touch()
    assert exists_as('~/tmp/chown_group.txt', 'file')

    Path('~/tmp/chown2_group.txt').touch()

# Generated at 2022-06-13 20:59:50.470507
# Unit test for function path_absent
def test_path_absent():
    f1 = tempfile.mkstemp()[1]
    d1 = tempfile.mkdtemp()
    f2 = os.path.join(d1, 'f2')
    open(f2, 'a').close()
    d2 = os.path.join(d1, 'd2')
    os.mkdir(d2)
    f3 = os.path.join(d2, 'f3')
    open(f3, 'a').close()
    path_absent(d1)
    assert not os.path.exists(d1)
    assert not os.path.lexists(f1)
    assert not os.path.lexists(f2)
    assert not os.path.lexists(f3)
    assert not os.path.lexists(d2)



# Generated at 2022-06-13 21:00:00.384380
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/etc/') == 'directory'
    assert exists_as('/etc') == 'directory'
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/bin/sh') == 'file'
    assert exists_as('/dev/disk0') == 'block device'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/tmp/mux') == 'FIFO'
    assert exists_as('/tmp/mux-SOME_USER_NAME') == 'socket'
    assert exists_as('/tmp/nofile') == ''


# Generated at 2022-06-13 21:00:13.864630
# Unit test for function chown
def test_chown():
    from flutils.testutils import runas
    from tempfile import NamedTemporaryFile
    from .mktestdata import mktestdata

    here = mktestdata(
        mk_pkgs=True,
        mk_modules=True,
        mk_files=True,
        mk_pkg_files=True,
        mk_pkg_modules=True,
    ).joinpath()

    tmp_f = NamedTemporaryFile().name
    tmp_f = here.joinpath(tmp_f)
    tmp_f.touch()

    test_user1 = os.getlogin()
    test_user2 = getpass.getuser()
    if test_user1 == test_user2:
        test_user2 = 'root'

    test_group1 = grp.getgrgid(os.getgid()).gr_name


# Generated at 2022-06-13 21:00:20.412300
# Unit test for function chown
def test_chown():
    path = normalize_path('~/tmp/flutils.tests.pathutils.txt')
    open(path, 'a').close()

    chown(path, user=getpass.getuser(), group=grp.getgrgid(os.getgid()).gr_name)

    assert path.exists() is True

    path.unlink()
    assert path.exists() is False



# Generated at 2022-06-13 21:00:23.664310
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/fake_path') == ''


# Generated at 2022-06-13 21:00:35.292992
# Unit test for function chown
def test_chown():
    pytest.test_import()
    pytest.skip_if_no_root()
    chown('/etc')
    chown('/etc', include_parent=True)
    chown('/etc/foo')
    chown('/etc/foo', include_parent=True)
    with pytest.raises(OSError):
        chown('/etc', user='bar')
    # chown('/etc/foo', group='bar')
    chown('/etc/foo*')
    chown('/etc/foo*', include_parent=True)
    chown('/etc/foo*', user='-1')
    chown('/etc/foo*', group='-1')



# Generated at 2022-06-13 21:00:39.763287
# Unit test for function exists_as
def test_exists_as():
    assert(exists_as(__file__) == 'file')
    assert(exists_as(__file__ + '_') == '')
    assert(exists_as(__file__ + '_\\') == '')


# Generated at 2022-06-13 21:00:50.847748
# Unit test for function get_os_user
def test_get_os_user():
    from mock import patch
    class MockStruct:
        pw_name = 'foo'
        pw_passwd = '********'
        pw_uid = 1001
        pw_gid = 2001
        pw_gecos = 'Foo Bar'
        pw_dir = '/home/foo'
        pw_shell = '/usr/local/bin/bash'

    with patch('pwd.getpwnam', return_value=MockStruct):
        # Do NOT include the quotes
        assert get_os_user('foo').pw_name == 'foo'
    with patch('pwd.getpwuid', return_value=MockStruct):
        assert get_os_user(1001).pw_name == 'foo'



# Generated at 2022-06-13 21:01:02.890414
# Unit test for function chown
def test_chown():
    from tempfile import TemporaryDirectory
    from flutils.pathutils import chown
    from flutils.systemutils import get_os_user
    from flutils.systemutils import get_os_group
    from flutils.systemutils import get_os_primary_group

    with TemporaryDirectory() as path:
        path = Path(path)
        file = path / 'flutils.tests.pathutils.txt'
        file.touch()
        chown(file)
        owner = get_os_user(file.owner())
        group = get_os_group(file.group())
        assert owner.pw_uid == os.geteuid()
        assert group.gr_gid == os.getegid()
        file_chown_1 = path / 'flutils.tests.pathutils.txt.chown.1'
        file

# Generated at 2022-06-13 21:01:20.344300
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod

    temp_dir = _create_temp_dir()
    fn_glob = os.path.join(temp_dir.as_posix(), '*')
    fn_glob_pattern = os.path.join(temp_dir.as_posix(), '*.txt')
    fn_1 = os.path.join(temp_dir.as_posix(), 'one.txt')
    fn_2 = os.path.join(temp_dir.as_posix(), 'two.txt')
    fn_3 = os.path.join(temp_dir.as_posix(), 'three.txt')
    fn_4 = os.path.join(temp_dir.as_posix(), 'four.txt')

# Generated at 2022-06-13 21:01:23.638259
# Unit test for function directory_present
def test_directory_present():
    path = directory_present('~/tmp/test_path')
    assert path.as_posix() == '/Users/len/tmp/test_path'



# Generated at 2022-06-13 21:01:25.889243
# Unit test for function chmod
def test_chmod():
    chmod('~/tmp/flutils.tests.pathutils.py')
    

# Generated at 2022-06-13 21:01:33.716218
# Unit test for function directory_present
def test_directory_present():
    """ Unit test for function directory_present """
    tmpdir = Path(__file__).parent.absolute() / 'tmp'
    tmpdir.mkdir(mode=0o700, exist_ok=True)
    path = tmpdir / 'test_path'
    result = directory_present(path, mode=0o700)
    assert isinstance(result, PosixPath)
    assert result.as_posix() == '/Users/len/tmp/test_path'
    assert path.exists() is True



# Generated at 2022-06-13 21:01:34.537881
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 21:01:48.196975
# Unit test for function chmod
def test_chmod():

    import hashlib
    import os

    from . import remove_paths

    from .osutils import touch
    from .pathutils import directory_present, normalize_path

    with directory_present('~/tmp/flutils.tests.chmod.test_chmod') as dirpath:

        test_file_path = dirpath.joinpath('flutils.tests.chmod.txt')
        ret = touch(test_file_path, 0o700)
        assert ret is True
        assert test_file_path.is_file() is True
        assert test_file_path.stat().st_mode == 0o100700
        assert test_file_path.stat().st_mode & 0o700 == 0o700

        # Testing PosixPath
        ret = chmod(PosixPath(test_file_path), 0o750)


# Generated at 2022-06-13 21:01:58.094238
# Unit test for function chmod
def test_chmod():
    # Placeholder to prevent 'unused import' error.
    assert grp and pwd and Path

    def _assert(path: _PATH, mode_file: Optional[int] = None, mode_dir: Optional[int] = None, include_parent: bool = False):
        path = normalize_path(path)
        if mode_file is None:
            mode_file = 0o600

        if mode_dir is None:
            mode_dir = 0o700

        if '*' in path.as_posix():
            for sub_path in Path().glob(path.as_posix()):
                if sub_path.is_dir() is True:
                    assert sub_path.stat().st_mode == mode_dir
                elif sub_path.is_file():
                    assert sub_path.stat().st_mode

# Generated at 2022-06-13 21:02:11.649246
# Unit test for function directory_present
def test_directory_present():
    os.chdir(os.getenv('HOME') + '/tmp')

    test_dir = 'new_dir'
    assert directory_present(test_dir) == Path('/Users/len/tmp/new_dir')
    assert os.path.isdir(test_dir) is True
    assert oct(os.stat(test_dir).st_mode)[-3:] == '700'
    assert os.stat(test_dir).st_uid == get_os_user().pw_uid
    assert os.stat(test_dir).st_gid == get_os_group().gr_gid

    test_dir = 'dirs'
    test_dir_path = directory_present(test_dir)
    assert test_dir_path == Path('/Users/len/tmp/dirs')
    assert os.path.isd

# Generated at 2022-06-13 21:02:25.071227
# Unit test for function chmod
def test_chmod():
    from contextlib import ExitStack
    from unittest.mock import patch

    from flutils.pathutils import chmod

    with ExitStack() as stack:
        chmod_ = stack.enter_context(patch('os.chmod'))
        mock_path = stack.enter_context(patch('flutils.pathutils.normalize_path'))

        mock_path.return_value = Path('/tmp/flutils.tests.pathutils.chmod.txt')

        chmod('/tmp/flutils.tests.pathutils.chmod.txt', 0o660, 0o770)

        mock_path.assert_called_once_with('/tmp/flutils.tests.pathutils.chmod.txt')

# Generated at 2022-06-13 21:02:37.258070
# Unit test for function directory_present
def test_directory_present():
    # Unit test for default invocation
    test_path = directory_present('~/tmp/flutils.tests.directory_present')
    assert test_path.is_dir() is True
    assert test_path.name == 'flutils.tests.directory_present'
    test_path.rmdir()
    # Unit test with a symlink
    Path('~/tmp/flutils.tests.directory_present.symlink').symlink_to(
        '~/tmp/flutils.tests.directory_present.txt'
    )
    test_path = directory_present('~/tmp/flutils.tests.directory_present.symlink')
    assert test_path.is_dir() is True
    assert test_path.name == 'flutils.tests.directory_present.symlink'

# Generated at 2022-06-13 21:02:52.484967
# Unit test for function chown
def test_chown():
    '''Test chown function
    '''
    print('\n====== test_chown ======')
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = os.path.join(tempdir, 'test_file')
        with open(test_file, 'w') as f:
            f.write('')
        test_dir = tempfile.TemporaryDirectory(dir=tempdir)
        test_subdir = tempfile.TemporaryDirectory(dir=test_dir.name)
        print('test if chown on file works:')
        print('before chown:')
        stat = os.stat(test_file)
        print('owner: ' + getpwuid(stat.st_uid).pw_name)

# Generated at 2022-06-13 21:03:00.761607
# Unit test for function path_absent
def test_path_absent():
    import flutils.pathutils
    import tempfile
    tmpdir = tempfile.mkdtemp()
    tmpdir = Path(tmpdir)
    path = tmpdir / 'unit_test_path_absent'
    path.mkdir()
    assert path.is_dir()
    flutils.pathutils.path_absent(path)
    assert path.exists() is False

# Generated at 2022-06-13 21:03:04.707224
# Unit test for function chown
def test_chown():
    assert 1 == 1
# Tests for Changelog
print('fix print()')
print('Tests for Changelog')
print('Tests for Changelog')
print('Tests for Changelog')

# Generated at 2022-06-13 21:03:09.921957
# Unit test for function chown
def test_chown():
    with TemporaryDirectory() as tmp_dir:
        path = normalize_path(Path(tmp_dir) / 'foo.txt')
        path.touch()

        uid = os.getuid()
        gid = os.getgid()
        chown('~' / 'foo.txt', uid, gid)



# Generated at 2022-06-13 21:03:16.008047
# Unit test for function chmod
def test_chmod():
    from textwrap import dedent
    from .osutils import file_present
    from .osutils import file_present_contents
    from .osutils import file_absent
    from .osutils import user_present
    from .osutils import group_present
    assert file_present('~/tmp/flutils.tests.osutils.chmod.txt', dedent('''\
        foo
    '''))
    assert file_present_contents('~/tmp/flutils.tests.osutils.chmod.txt', 'foo')
    assert user_present('flutils')
    assert group_present('foobar')
    # 0o777
    assert chmod('~/tmp/flutils.tests.osutils.chmod.txt', 0o660, 0o770)
    # 0o770

# Generated at 2022-06-13 21:03:23.763331
# Unit test for function chown
def test_chown():
    import flutils.pathutils as pathutils
    from flutils.testingutils.test_file import TestFile
    from flutils.pathutils import path_absent
    from mock import patch

    # Using TestFile because pathutils.chown() uses os.chown()
    # Requires a file, not just a directory
    with TestFile() as testfile:
        testfile.create()
        pathutils.chown(testfile.path, user='foo', group='bar')
        assert testfile.get_owner() == 'foo'
        assert testfile.get_group() == 'bar'

    # Test that path_absent() generates the right call args
    # to os.remove()
    with patch('os.remove') as mock_remove:
        pathutils.path_absent('~/tmp')
        mock_remove.assert_

# Generated at 2022-06-13 21:03:31.855799
# Unit test for function path_absent
def test_path_absent():
    import tempfile
    dir_name = tempfile.mkdtemp()
    path_name = os.path.join(dir_name, 'foo.bar')
    with open(path_name, 'a'):
        pass
    assert os.path.exists(path_name)
    path_absent(path_name)
    assert not os.path.exists(path_name)
    os.rmdir(dir_name)
    assert not os.path.exists(dir_name)



# Generated at 2022-06-13 21:03:39.555287
# Unit test for function chown
def test_chown():
     path = normalize_path('/tmp/file.txt')
     sys.stdout.write(path)
     user = 'oracle'
     group = 'oinstall'
     if path.exists() is True:
         os.chown(path.as_posix(), user, group)
         sys.stdout.write("chown successful")
     else:
         sys.stdout.write("chown NOT successful")
# Unit Test End