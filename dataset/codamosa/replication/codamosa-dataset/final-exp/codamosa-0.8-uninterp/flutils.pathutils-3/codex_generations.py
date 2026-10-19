

# Generated at 2022-06-13 20:54:18.402868
# Unit test for function find_paths
def test_find_paths():
    """Test: flutils.pathutils.find_paths()
    """
    directory = normalize_path('~/tmp')
    if directory.exists() is False:
        directory.mkdir(mode=0o700)

    for test_file in find_paths(directory):
        test_file.unlink()


# Generated at 2022-06-13 20:54:30.204916
# Unit test for function exists_as
def test_exists_as():
    from flutils.pathutils import exists_as
    assert exists_as(__file__) == 'file'
    assert exists_as('~') == 'directory'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('') == ''
    assert exists_as('flutils/pathutils.py') == ''
    assert exists_as('flutils') == ''
    assert exists_as('/proc/self') == ''
    assert exists_as('/proc/self/fd/2') == ''
    assert exists_as('~/flutils/tests/__init__.py') == 'file'
    assert exists_as('~/flutils/tests/') == 'directory'



# Generated at 2022-06-13 20:54:31.868517
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown

    if sys.platform == 'darwin' or sys.platform == 'linux':
        chown('/tmp/flutils.tests.pathutils.chown.txt')



# Generated at 2022-06-13 20:54:40.815050
# Unit test for function find_paths
def test_find_paths():
    import string
    from random import choice
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tempdir:
        testdir = Path(tempdir)
        subdirs = [
            'dir_one',
            'dir_two'
        ]

        files = [
            'file_one',
            'file_two'
        ]

        for sub in subdirs:
            directory_present(testdir / sub)

        for f in files:
            _ = open(testdir / f, 'w').close()

        patterns = [
            '**',
            '**/*',
            '**/*/*',
            '**/file*',
            '**/di*',
            '**/*one',
            '**/*wo'
        ]


# Generated at 2022-06-13 20:54:49.252468
# Unit test for function get_os_user
def test_get_os_user():
    g = get_os_user('foo')
    e = [
        ('pw_name', 'foo'),
        ('pw_passwd', '********'),
        ('pw_uid', 1001),
        ('pw_gid', 2001),
        ('pw_gecos', 'Foo Bar'),
        ('pw_dir', '/home/foo'),
        ('pw_shell', '/usr/local/bin/bash')
    ]
    for i in e:
        assert i[1] == g[i[0]]


# Generated at 2022-06-13 20:54:57.705033
# Unit test for function chown
def test_chown():
    from io import StringIO
    from unittest.mock import patch
    from pathlib import PosixPath
    from flutils.pathutils import chown

    patch_file = StringIO()
    patch_file.write('bar')
    patch_file.seek(0)


# Generated at 2022-06-13 20:55:04.709786
# Unit test for function chown
def test_chown():
    """Tests the usage examples in the module docstring."""
    import tempfile
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            dirname = '{}/flutils.tests.osutils'.format(tmpdir)
            fname = dirname + '.txt'
            os.mkdir(dirname)
            with open(fname, 'w'):
                pass
            chown(fname)
            chown(dirname + '*', user='-1', group='-1')
            chown(dirname + '/**', user=getpass.getuser())
    except OSError:
        # Some systems don't allow chown to run as root.
        pass



# Generated at 2022-06-13 20:55:11.965807
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/') == 'directory'
    assert exists_as('') == ''
    assert exists_as('/') == 'directory'
    assert exists_as('/etc') == 'directory'
    assert exists_as('/etc/hosts') == 'file'
    assert exists_as('/dev/sr0') == 'block device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/proc/1/fd/0') == 'socket'
    assert exists_as('/unknown/unknown') == ''

# Generated at 2022-06-13 20:55:19.922058
# Unit test for function directory_present
def test_directory_present():
    path = directory_present(
        '~/tmp/flutils.tests.pathutils.directory_present',
        0o750,
        user='-1',
        group='-1',
    )
    assert path.as_posix() == os.path.expanduser('~/tmp/flutils.tests.pathutils.directory_present')
    assert path.is_dir() is True
    path.rmdir()

# Generated at 2022-06-13 20:55:28.995780
# Unit test for function find_paths
def test_find_paths():
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        file_one = tmp_dir / 'file_one'
        file_one.touch()

        dir_one = tmp_dir / 'dir_one'
        dir_one.mkdir()

        file_two = dir_one / 'file_two'
        file_two.touch()

        find_paths_patterns = [
            '*/file_one',
            '/tmp/non_existant_path/*',
            'file_one',
            tmp_dir / '*',
            tmp_dir / '*/',
            tmp_dir / '*/file_two',
        ]

        for path in find_paths_patterns:
            for sub_path in find_paths(path):
                print(sub_path)

# Generated at 2022-06-13 20:55:59.538139
# Unit test for function get_os_user
def test_get_os_user():
    try:
        user = get_os_user('-1')
        assert isinstance(user, pwd.struct_passwd)
    except OSError:
        assert False
    try:
        user = get_os_user(None)
        assert isinstance(user, pwd.struct_passwd)
    except OSError:
        assert False



# Generated at 2022-06-13 20:56:06.850638
# Unit test for function get_os_user
def test_get_os_user():
    assert get_os_user('foobar') == pwd.struct_passwd(
        pw_name='foobar', pw_passwd='********', pw_uid=1001, pw_gid=2001,
        pw_gecos='Foo Bar', pw_dir='/home/foobar',
        pw_shell='/usr/local/bin/bash'
    )



# Generated at 2022-06-13 20:56:14.666173
# Unit test for function find_paths
def test_find_paths():
    with TemporaryDirectory() as CA_ROOT_DIR:
        file_one = Path(CA_ROOT_DIR).joinpath('file_one')
        single_dir = Path(CA_ROOT_DIR).joinpath('dir_one')

        file_one.touch()
        single_dir.mkdir()

        assert find_paths(Path(CA_ROOT_DIR).joinpath(Path('*'))) == \
            find_paths(Path(CA_ROOT_DIR).joinpath('*'))



# Generated at 2022-06-13 20:56:21.472467
# Unit test for function find_paths
def test_find_paths():
    with temporary_directory() as tmpdir:
        one_path = Path(tmpdir) / 'file_one'
        one_path.touch()
        two_path = Path(tmpdir) / 'dir_one'
        two_path.mkdir()
        paths_list = list(find_paths(tmpdir / '*'))
        for path in paths_list:
            assert os.path.exists(path.as_posix())



# Generated at 2022-06-13 20:56:33.266198
# Unit test for function chmod
def test_chmod():
    parent_path = Path('/tmp/flutils.tests')

    if not parent_path.exists():
        parent_path.mkdir(0o700)

    # Directory
    chmod_dir_path = parent_path / 'chmod_dir'
    if chmod_dir_path.exists():
        chmod_dir_path.rmdir()

    chmod_dir_path.mkdir(0o755)
    assert chmod_dir_path.exists() is True
    assert chmod_dir_path.is_dir() is True
    assert chmod_dir_path.stat().st_mode & 0o700 == 0o755
    assert chmod_dir_path.stat().st_mode & 0o777 == 0o755

# Generated at 2022-06-13 20:56:34.977860
# Unit test for function find_paths
def test_find_paths():
    pass



# Generated at 2022-06-13 20:56:36.134801
# Unit test for function chown
def test_chown():
    pass
# Unit tests for function chmod

# Generated at 2022-06-13 20:56:41.358848
# Unit test for function path_absent
def test_path_absent():
    path = '~/tmp/unittest_path'
    path = normalize_path(path)
    path = cast(str, path)
    try:
        path_present(path)
        path_absent(path)
        assert os.path.exists(path) is False
    finally:
        path_absent(path)



# Generated at 2022-06-13 20:56:42.137705
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:56:49.535636
# Unit test for function chmod
def test_chmod():
    chmod('/home/dmurawsky/tmp/flutils.tests.osutils.txt', 0o660)
    assert os.stat('/home/dmurawsky/tmp/flutils.tests.osutils.txt').st_mode & 0o700 == 0o660
    with open('/home/dmurawsky/tmp/flutils.tests.osutils.txt', 'w') as f:
        f.write('This is a test of the chmod function in osutils module')

    try:
        os.chmod('/home/dmurawsky/tmp/flutils.tests.osutils.txt', 0o660)
    except PermissionError:
        pytest.fail('Could not os.chmod()')


# Generated at 2022-06-13 20:57:17.773165
# Unit test for function exists_as
def test_exists_as():
    with pytest.raises(TypeError):
        exists_as(1)
    with pytest.raises(TypeError):
        exists_as(1.0)
    with pytest.raises(TypeError):
        exists_as(True)
    with pytest.raises(TypeError):
        exists_as(['/path'])
    assert exists_as(Path('/tmp')) == 'directory'
    assert exists_as(Path('/tmp/')) == 'directory'
    assert exists_as(Path('/tmp/.')) == 'directory'
    assert exists_as(Path('/tmp/..')) == 'directory'
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/tmp/') == 'directory'

# Generated at 2022-06-13 20:57:29.037166
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    import os
    import shutil
    import tempfile

    tmpdir = os.path.join(tempfile.gettempdir(), 'flutils.tests')
    test_dir = os.path.join(tmpdir, 'osutils_test_dir')
    test_file = os.path.join(test_dir, 'osutils_test_file.txt')

    try:
        shutil.rmtree(tmpdir)
    except OSError:
        pass
    os.makedirs(test_dir, 0o700)
    with open(test_file, 'w'):
        pass
    # Change the mode to a non-standard value
    os.chmod(test_file, 0o420)
    assert os.stat(test_file).st_mode & 0

# Generated at 2022-06-13 20:57:37.154393
# Unit test for function find_paths
def test_find_paths():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        file_one = tmpdir / 'file_one'
        file_one.touch()
        dir_one = tmpdir / 'dir_one'
        dir_one.mkdir()
        paths = list(find_paths(tmpdir / '*'))
        assert paths == [file_one, dir_one]



# Generated at 2022-06-13 20:57:41.335149
# Unit test for function find_paths
def test_find_paths():
    a = find_paths('~/tmp/*')
    b = list(find_paths('~/tmp/*'))
    assert len(a) == 2



# Generated at 2022-06-13 20:57:52.077559
# Unit test for function exists_as
def test_exists_as():
    path = directory_present(Path.home() / '.flutils.tests')
    positive_tests = [
        '',
        'directory',
        'file',
        'block device',
        'char device',
        'FIFO',
        'socket',
    ]
    negative_tests = [
        '',
        'directory',
        'file',
        'block device',
        'char device',
        'FIFO',
        'socket',
    ]
    with NamedTemporaryFile() as tst_file:
        tst_file_path = Path(tst_file.name).absolute()

        device_path = path / 'zero'

# Generated at 2022-06-13 20:58:03.819851
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(Path(__file__).resolve()) == 'file'
    assert exists_as(Path().home()) == 'directory'
    assert exists_as(Path('/dev/STDIN').resolve()) == 'char device'
    assert exists_as(Path('/dev/NULL').resolve()) == 'char device'
    assert exists_as(Path('/dev/stdout').resolve()) == 'char device'
    assert exists_as(Path('/dev/tty').resolve()) == 'char device'
    assert exists_as(Path('/dev/zero').resolve()) == 'char device'
    assert exists_as(Path('/tmp').resolve()) == 'directory'
    assert exists_as(Path('/tmp/random_file').resolve()) == 'file'

# Generated at 2022-06-13 20:58:15.219343
# Unit test for function chown
def test_chown():
    pass
    # with pytest.raises(OSError) as excinfo:
    #     chown(b'foo')
    # assert excinfo.value.strerror == 'chown: illegal user name: foo'

    # with pytest.raises(OSError) as excinfo:
    #     chown('foo')
    # assert excinfo.value.strerror == 'chown: illegal user name: foo'

    # with pytest.raises(OSError) as excinfo:
    #     chown(b'foo', group=b'bar')
    # assert excinfo.value.strerror == 'chown: illegal user name: foo'

    # with pytest.raises(OSError) as excinfo:
    #     chown('foo', group='bar')
    # assert excinfo.value.st

# Generated at 2022-06-13 20:58:28.265455
# Unit test for function find_paths
def test_find_paths():
    """Unit test for function :func:`find_paths`"""
    root = directory_present('~/tmp/foo')
    directory_present(os.path.join(root, 'bar/baz'))
    file_path = Path(os.path.join(root, 'bar/baz/test_file.txt'))
    file_path.touch()

    assert list(find_paths(os.path.join(root, 'bar'))) == [
        Path(os.path.join(root, 'bar/baz')),
        Path(os.path.join(root, 'bar/baz/test_file.txt')),
    ]


# Generated at 2022-06-13 20:58:39.442767
# Unit test for function exists_as
def test_exists_as():
    def _test(path, expected):
        path = pathlib.Path(path).expanduser()
        if exists_as(path) != expected:
            raise Exception('expected: %r got: %r' % (expected, exists_as(path)))
    _test('/dev/zero', 'char device')
    _test('/dev/sda', 'block device')
    _test('/dev/console', '')
    _test('/dev/null', 'character device')
    _test('/var/log/wtmp', 'file')
    _test('~/tmp', 'directory')
    _test('~/tmp/flutils.tests.osutils', 'directory')
    _test('~/tmp/flutils.tests.osutils.txt', 'file')


# Generated at 2022-06-13 20:58:46.307959
# Unit test for function find_paths
def test_find_paths():
    from os import makedirs, remove
    from os.path import isdir, isfile, join
    from shutil import rmtree

    from flutils.pathutils import find_paths

    tmp_dir = '/tmp/flutils.pathutils.find_paths'
    tmp_files = ['file_one', 'file_two', join('dir_one', 'file_three')]
    tmp_files = [join(tmp_dir, f) for f in tmp_files]

    makedirs(tmp_files[-1], exist_ok=True)

    for path in tmp_files:
        with open(path, 'w'):
            pass

    paths = list(find_paths(join(tmp_dir, '*')))
    paths = [p.as_posix() for p in paths]


# Generated at 2022-06-13 20:59:18.332332
# Unit test for function chown
def test_chown():
    with pytest.raises(OSError):
        chown('/tmp/flutils.tests.osutils.txt', group='foo')
    with pytest.raises(OSError):
        chown('/tmp/flutils.tests.osutils.txt', user='foo')



# Generated at 2022-06-13 20:59:26.907497
# Unit test for function chmod
def test_chmod():
    test_path = Path('/tmp/flutils.tests.osutils.txt')

    try:
        test_path.touch()
    except Exception as exp_obj:
        raise FileExistsError(f'{exp_obj}') from exp_obj

    try:
        chmod(test_path, 0o660)
        assert test_path.is_file()
        assert test_path.stat().st_mode == 33279
    finally:
        Path.unlink(test_path)



# Generated at 2022-06-13 20:59:36.221961
# Unit test for function chown
def test_chown():
    # Ensure failure when user does not exist
    import pytest
    with pytest.raises(OSError):
        chown('~/tmp/flutils.tests.osutils.txt', user='nobody')

    # Ensure failure when group does not exist
    with pytest.raises(OSError):
        chown('~/tmp/flutils.tests.osutils.txt', group='nobody')

    # Ensure success
    chown('~/tmp/flutils.tests.osutils.txt', user=getpass.getuser())



# Generated at 2022-06-13 20:59:43.844443
# Unit test for function chmod
def test_chmod():
        from flutils.pathutils import chmod
        chmod('~/tmp/flutils.tests.osutils.txt', 0o660)
        chmod('~/tmp/**', mode_file=0o644, mode_dir=0o770)
        chmod('~/tmp/*')
        chmod('~/tmp/flutils.tests.osutils.txt', 0o600)
        chmod('~/tmp/**', mode_file=0o600, mode_dir=0o700)
        chmod('~/tmp/*')


# Generated at 2022-06-13 20:59:45.851500
# Unit test for function chown
def test_chown():
    chown('~/tmp/flutils.tests.osutils.txt')


# Generated at 2022-06-13 20:59:59.193850
# Unit test for function chmod
def test_chmod():
    from os import (
        chmod,
        makedirs,
        pathsep,
        rmdir,
        stat,
    )
    from shutil import rmtree

    from flutils.pathutils import chmod

    tmp_path1 = '~/tmp/flutils.tests.osutils.chmod.test1'
    tmp_path2 = '~/tmp/flutils.tests.osutils.chmod.test2/'
    tmp_path3 = '~/tmp/flutils.tests.osutils.chmod.test3/subdir'
    tmp_path4 = '~/tmp/flutils.tests.osutils.chmod.test4/subdir/subdir2'
    tmp_path5 = '~/tmp/flutils.tests.osutils.chmod.test5/**'
   

# Generated at 2022-06-13 21:00:04.290559
# Unit test for function chmod
def test_chmod():
    # Setup
    path = Path(__file__).parent / 'tmp' / 'flutils.tests.pathutils.txt'
    path.parent.mkdir(parents=True)
    path.write_text('')

    # Exercise
    chmod(path)

    # Verify
    assert path.stat().st_mode == 33184

    # Cleanup
    path.parent.parent.rmdir()



# Generated at 2022-06-13 21:00:05.796671
# Unit test for function chmod
def test_chmod():
    assert callable(chmod)



# Generated at 2022-06-13 21:00:08.499318
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/made/up/path') == ''



# Generated at 2022-06-13 21:00:25.108460
# Unit test for function chmod
def test_chmod():
    try:
        abs_path = Path(__file__)
    except OSError:
        abs_path = None
    if abs_path is None:
        return
    txt_file = abs_path.parent / 'tmp' / 'flutils.tests.osutils.txt'
    if txt_file.exists() is True:
        txt_file.unlink()
    if txt_file.parent.exists() is False:
        txt_file.parent.mkdir()
    # Create a file so that it can test the file permissions
    txt_file.write_bytes(b'')
    assert txt_file.exists() is True
    # validate that the test files mode is correct
    assert txt_file.stat().st_mode == 33152
    # test to make sure it doesn

# Generated at 2022-06-13 21:00:45.988988
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        (tmp_dir / 'foo').write_text('')

        assert (tmp_dir / 'foo').stat().st_mode & 0o777 == 0o600
        assert tmp_dir.stat().st_mode & 0o777 == 0o700

        chmod(tmp_dir / 'foo', 0o644)
        chmod(tmp_dir, 0o750)
        chmod(tmp_dir / '**', 0o640, 0o750)

        assert (tmp_dir / 'foo').stat().st_mode & 0o777 == 0o644
        assert tmp_dir.stat().st_mode & 0o777 == 0o750


# Generated at 2022-06-13 21:00:53.074311
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/flutils.tests.osutils.socket') == 'socket'
    assert exists_as('~/tmp/flutils.tests.osutils.txt') == 'file'
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/usr/bin') == 'directory'

# Generated at 2022-06-13 21:00:57.334168
# Unit test for function chown
def test_chown():
    chown(
        '~/tmp/flutils.tests.osutils.txt',
        user=getpass.getuser(),
        group=grp.getgrgid(os.getgid()).gr_name,
    )



# Generated at 2022-06-13 21:01:07.163759
# Unit test for function chmod
def test_chmod():
    import pytest
    path = Path('/tmp/flutils.tests.osutils.txt')
    path.touch()
    try:
        chmod(path)
        assert path.stat().st_mode & 0o777 == 0o100600
    finally:
        Path('/tmp/flutils.tests.osutils.txt').unlink()
        if Path('/tmp/flutils.tests').exists() is True:
            Path('/tmp/flutils.tests').rmdir()



# Generated at 2022-06-13 21:01:18.891061
# Unit test for function chmod
def test_chmod():
    # Test for file path that does NOT exist
    assert chmod('/tmp/test_chmod_does_not_exist') is None
    # Test for file path that does exist
    tmp_file_path = Path('/tmp').joinpath('test_chmod.txt')
    if tmp_file_path.exists() is True:
        tmp_file_path.unlink()
    with tmp_file_path.open('w') as f:
        f.write('test data')
    assert chmod(tmp_file_path.as_posix(), 0o660) is None
    assert tmp_file_path.stat().st_mode & 0o777 == 0o660
    assert chmod(tmp_file_path.as_posix(), mode_file=0o660) is None

# Generated at 2022-06-13 21:01:26.879785
# Unit test for function chown
def test_chown():
    import shutil

    from os import remove

    from tempfile import mkdtemp

    path = Path(mkdtemp(prefix='flutils.tests.'))
    shutil.rmtree(path)
    path.mkdir()
    chown(
        path,
        user=getpass.getuser(),
        group=grp.getgrgid(os.getgid()).gr_name,
    )
    shutil.rmtree(path)



# Generated at 2022-06-13 21:01:27.559847
# Unit test for function chown
def test_chown():
    return


# Generated at 2022-06-13 21:01:38.635186
# Unit test for function chown
def test_chown():
    import flutils.osutils as osutils
    import flutils.pathutils as pathutils
    import time
    import uuid
    import io

    tmp_dir = os.path.join('/tmp', f'{str(uuid.uuid4())}')
    osutils.makedirs(tmp_dir, mode=0o775)

    # Basic test
    test_path1 = os.path.join(tmp_dir, 'test_chown1.txt')
    test_path2 = os.path.join(tmp_dir, 'test_chown2.txt')
    with io.open(test_path1, 'w') as fh:
        fh.write('Testing chown() function')
    pathutils.chown(test_path1)
    pathutils.chown(test_path2)

   

# Generated at 2022-06-13 21:01:44.604064
# Unit test for function chmod
def test_chmod():
    try:
        chmod('C:/Users/flutils/tmp/flutils.tests.osutils.txt', 0o600)
        chmod('C:/Users/flutils/tmp/**', 0o600, 0o700)
        chmod('C:/Users/flutils/tmp/**', mode_dir=0o700)
        chmod('C:/Users/flutils/tmp/flutils.tests.osutils.txt')
    except Exception as e:
        raise Exception('Failed to change path mode')



# Generated at 2022-06-13 21:01:56.958092
# Unit test for function chmod
def test_chmod():
    test_dir = Path('~/tmp/flutils.tests.pathutils.chmod').expanduser()
    os.makedirs(test_dir.as_posix(), 0o700, exist_ok=True)
    test_txt = (
        test_dir / 'flutils.tests.pathutils.chmod.txt'
    )
    with test_txt.open('wt') as fd:
        fd.write('')
    chmod(test_dir.as_posix())
    assert test_dir.stat().st_mode & 0o777 == 0o700
    chmod(
        test_txt.as_posix(),
        mode_dir=0o770,
        mode_file=0o644
    )
    assert test_txt.stat().st_mode & 0o777 == 0o644

# Generated at 2022-06-13 21:02:27.331031
# Unit test for function path_absent
def test_path_absent():
    from os import mkdir
    from os.path import exists, join, sep
    from tempfile import mkdtemp
    import shutil
    from pathlib import Path
    from pathlib import PurePath
    from flutils.pathutils import path_absent

    tmp_dir = mkdtemp()
    test_dir = join(tmp_dir, 'test_dir')
    Path(test_dir).mkdir()
    test_file = join(test_dir, 'test_file')
    Path(test_file).touch()
    test_link = join(tmp_dir, 'test_link')
    os.symlink(test_file, test_link)
    test_path = PurePath(tmp_dir)

# Generated at 2022-06-13 21:02:32.024636
# Unit test for function exists_as
def test_exists_as():
    path = '~/tmp/flutils.tests.osutils.txt'
    path = normalize_path(path)
    path.touch()
    assert exists_as(path) == 'file'
    path.unlink()
    assert exists_as(path) == ''



# Generated at 2022-06-13 21:02:45.017640
# Unit test for function path_absent
def test_path_absent():
    from tempfile import mkdtemp
    from shutil import rmtree

    tmpdir = mkdtemp()

    path = Path(tmpdir) / 'dir_one'
    path_absent(path)
    assert path.exists() is False

    path.mkdir()
    assert path.is_dir()

    path = path / 'dir_two'
    path.mkdir(parents=True)
    path = path / 'file_one'
    with open(path, 'w') as fh:
        fh.write('foo')
    assert path.is_file()

    path = Path(tmpdir) / 'file_two'
    with open(path, 'w') as fh:
        fh.write('foo')
    assert path.is_file()


# Generated at 2022-06-13 21:02:46.193181
# Unit test for function chown
def test_chown():
    assert True

# Generated at 2022-06-13 21:02:52.791571
# Unit test for function directory_present
def test_directory_present():
    with directory_present('~/tmp/test_path') as path:
        assert isinstance(path, PosixPath)
        assert path.as_posix() == '/Users/len/tmp/test_path'
        assert path.is_dir()

# Generated at 2022-06-13 21:02:56.237428
# Unit test for function chmod
def test_chmod():
    try:
        chmod('tests/testfile', mode_file=0o600)
    except TypeError:
        pass


# Generated at 2022-06-13 21:03:09.670133
# Unit test for function directory_present
def test_directory_present():
    with tempfile.TemporaryDirectory() as tmp_dir_path:
        path = Path(tmp_dir_path)
        tmp_dir = path / 'test_directory'
        tmp_dir.mkdir()

        # Make the path NOT exist.
        tmp_dir.rmdir()
        tmp_dir_path = directory_present(tmp_dir)
        assert tmp_dir_path.is_dir() is True

        # Make the path be a file.
        tmp_dir.touch()
        with pytest.raises(FileExistsError):
            directory_present(tmp_dir)

        # Make it a link to a file.
        tmp_dir_file = tmp_dir.with_name('tmp_dir_file.txt')
        tmp_dir_file.touch()

# Generated at 2022-06-13 21:03:18.877471
# Unit test for function path_absent
def test_path_absent():
    """Unit test for path_absent function."""
    test_path = Path(__file__).parent / 'tmp' / 'test_path'
    test_path.mkdir(exist_ok=True, parents=True)
    test_file = Path(__file__).parent / 'tmp' / 'test_path' / 'test_file'
    test_file.write_text('This is a test file.')
    test_dir = Path(__file__).parent / 'tmp' / 'test_path' / 'test_dir'
    test_dir.mkdir()
    assert test_dir.exists()
    assert test_file.exists()
    path_absent(test_path)
    assert test_path.exists() is False
    assert test_dir.exists() is False
    assert test_file

# Generated at 2022-06-13 21:03:19.488658
# Unit test for function chown
def test_chown():
    pass

# Generated at 2022-06-13 21:03:20.964624
# Unit test for function chown
def test_chown():
    chown('./tmp.txt')
