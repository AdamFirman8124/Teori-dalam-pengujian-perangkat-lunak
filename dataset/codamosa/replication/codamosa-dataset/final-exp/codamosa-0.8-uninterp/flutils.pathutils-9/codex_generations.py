

# Generated at 2022-06-13 20:54:01.567925
# Unit test for function path_absent
def test_path_absent():
    from tempfile import TemporaryDirectory
    from tests.base import TestCase, test_path

    class TestPathAbsent(TestCase):
        def setUp(self):
            self.test_dir = TemporaryDirectory()

        def tearDown(self):
            self.test_dir.cleanup()

        def test_path_absent_dir(self):
            try:
                path_absent(self.test_dir.name)
            except Exception as exc:
                self.fail(exc)


# Generated at 2022-06-13 20:54:04.857111
# Unit test for function path_absent
def test_path_absent():
    '''
    Unit test for path_absent
    (c) 2020, John Kohler
    '''
    run_cmd(['rm','-fr','foo'])
    run_cmd(['touch','foo/bar'])
    path_absent('foo')
    assert not os.path.exists('foo')

# Generated at 2022-06-13 20:54:08.330136
# Unit test for function chown
def test_chown():
    p = Path(tmp_path)
    assert p.exists() is False
    p.touch()
    chown(p, None, None)
    assert p.stat().st_uid == get_os_user().pw_uid
    assert p.stat().st_gid == get_os_group().gr_gid
    p.unlink()



# Generated at 2022-06-13 20:54:14.513939
# Unit test for function find_paths
def test_find_paths():

    # Find all *.py files in the directory
    pattern = '*.py'

    for path in find_paths(pattern):
        print(path)

    # Find all *.py files in the subdirectories
    pattern = '**/*.py'

    for path in find_paths(pattern):
        print(path)



# Generated at 2022-06-13 20:54:22.276796
# Unit test for function find_paths
def test_find_paths():
    path = Path('~/tmp')
    path.mkdir(parents=True, exist_ok=True)

    file_name = 'file_one'
    file_path = str(path.joinpath(file_name))
    Path(file_path).touch()

    dir_name = 'dir_one'
    dir_path = str(path.joinpath(dir_name))
    Path(dir_path).mkdir()

    assert list(find_paths('~/tmp/*')) == [Path(file_path), Path(dir_path)]



# Generated at 2022-06-13 20:54:25.483945
# Unit test for function find_paths
def test_find_paths():
    pattern = Path('~/tmp/*')
    assert list(find_paths(pattern))



# Generated at 2022-06-13 20:54:29.213217
# Unit test for function chmod
def test_chmod():
    pass  # TODO: Figure out a way to test chmod()



# Generated at 2022-06-13 20:54:33.904313
# Unit test for function get_os_group
def test_get_os_group():
    import pathlib
    import pytest
    from flutils.collectionutils import LimitedSet
    from flutils.pathutils import get_os_group, get_os_user, normalize_path
    from flutils.textutils import BASH_GLOB_EXCLAMATION_UNESCAPE_PATTERN
    from flutils.textutils import BASH_GLOB_PATTERN

    # get_os_group()

    with pytest.raises(OSError):
        _ = get_os_group(123)  # This will fail because this test is not running
        # as root.

    with pytest.raises(OSError):
        _ = get_os_group('foobar')  # This will fail because 'foobar" is not
        # a group name on this system.

    # If a name is not provided, this

# Generated at 2022-06-13 20:54:43.892254
# Unit test for function path_absent
def test_path_absent():
    import tempfile

    # Create a temporary directory to work in.
    working_dir = tempfile.TemporaryDirectory()

    # Create a temporary file.
    file = Path(working_dir.name) / 'path_one'
    file.touch()
    file.chmod(0o777)

    # Create a temporary symlink.
    link_file = Path(working_dir.name) / 'path_two'
    file.symlink_to(link_file)
    link_file.chmod(0o777)

    # Create a temporary directory.
    directory = Path(working_dir.name) / 'path_three'
    directory.mkdir(mode=0o777)

    # Create a temporary symlink to a directory.

# Generated at 2022-06-13 20:54:44.555692
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:55:22.503416
# Unit test for function exists_as
def test_exists_as():
    """Unit test for function exists_as."""
    assert exists_as('~') == 'directory'
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/unittest_file') == 'file'



# Generated at 2022-06-13 20:55:28.080992
# Unit test for function path_absent
def test_path_absent():
    p = Path('~/tmp/flutils')
    p.mkdir()
    Path('~/tmp/flutils/test_path').touch()
    path_absent('~/tmp/flutils')
    assert p.exists() is False
    p.mkdir()
    Path('~/tmp/flutils/test_path').touch()
    path_absent(Path('~/tmp/flutils'))
    assert p.exists() is False



# Generated at 2022-06-13 20:55:35.902314
# Unit test for function chown
def test_chown():
    template = """
    path = '{}'
    user = '{}'
    group = '{}'
    chown(path, user, group)
    """

    # Test glob pattern
    template = """
    path = '{}'
    user = '{}'
    group = '{}'
    chown(path, user, group)
    """

    with TempDir() as tmp_dir:
        d = tmp_dir.mkdir('foo')
        f = d.join('bar.txt')
        f.write('blah')
        # Test glob pattern
        # No pattern
        exec(template.format(f, '-1', '-1'))
        assert f.exists()
        # With pattern

# Generated at 2022-06-13 20:55:42.261318
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(Path()) == 'directory'
    assert exists_as(os.path.expanduser('~/.profile')) == 'file'
# Unit tests for exists_as()
for path in [
        '*',
        '~/tmp/flutils.tests.osutils.txt',
        '~/tmp/flutils.tests.osutils',
        '~/tmp/flutils.tests.osutils/',
]:
    assert exists_as(path) == 'file'



# Generated at 2022-06-13 20:55:49.326435
# Unit test for function path_absent
def test_path_absent():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as test_dir:
        root_dir = Path(test_dir)
        for x in range(5):
            tmp_dir = root_dir / 'tmp_dir'
            tmp_dir.mkdir()
            tmp_dir = root_dir / 'tmp_dir' / 'test_dir'
            tmp_dir.mkdir()
            tmp_file = root_dir / 'tmp_dir' / 'test_dir' / 'test_file'
            tmp_file.touch()
        path_absent(root_dir / 'tmp_dir')
        assert root_dir.exists()
        assert not (root_dir / 'tmp_dir').exists()



# Generated at 2022-06-13 20:55:51.092234
# Unit test for function get_os_user
def test_get_os_user():
    get_os_user()

# Generated at 2022-06-13 20:55:59.413751
# Unit test for function path_absent
def test_path_absent():
    test_dir = Path(__file__).absolute().parent
    test_dir = test_dir / 'path_absent_tests'
    if test_dir.exists():
        path_absent(test_dir)
    assert path_absent(test_dir) is None
    assert not test_dir.exists()
    test_dir.mkdir()
    assert test_dir.exists()
    assert path_absent(test_dir) is None
    assert not test_dir.exists()
    test_file = test_dir / 'text_file'
    touch(test_file)
    assert test_file.exists()
    assert path_absent(test_file) is None
    assert not test_file.exists()
    test_file = test_dir / 'test_file'

# Generated at 2022-06-13 20:56:12.413484
# Unit test for function exists_as
def test_exists_as():
    from .osutils import get_temp_dir
    TEMP_DIR = get_temp_dir()
    # Test for regular file
    file_path = Path(TEMP_DIR).joinpath('dirutils.txt')
    file_path.touch()
    assert exists_as(TEMP_DIR.joinpath('dirutils.txt')) == 'file'
    file_path.unlink()
    # Test for directory
    dir_path = Path(TEMP_DIR).joinpath('dirutils')
    dir_path.mkdir()
    assert exists_as(TEMP_DIR.joinpath('dirutils')) == 'directory'
    dir_path.rmdir()
    # Test for non-existent file
    assert exists_as(TEMP_DIR.joinpath('doesnt-exist')) == ''
test_exists_

# Generated at 2022-06-13 20:56:15.212781
# Unit test for function get_os_user
def test_get_os_user():
    assert(get_os_user()==pwd.getpwuid(os.getuid()))
    assert(get_os_user(1001)==pwd.getpwuid(1001))


# Generated at 2022-06-13 20:56:27.244255
# Unit test for function directory_present
def test_directory_present():
    """ Test directory_present function. """
    # pylint: disable=R0915,R0912,R0914,R0201
    # Line too long, Too many branches / statements, Too many local variables
    # , Method could be a function
    import random
    import string
    import tempfile
    from pathlib import Path
    from typing import Any, List
    from unittest.mock import patch
    from flutils.pathutils import directory_present, get_os_user

    system_user = get_os_user().pw_name

    class Glob():
        """ Mocking pathlib.Path.glob """
        def glob(self, path: str) -> List[str]:
            """ Mocking glob method. """
            if path == '/foo/*':
                return ['/foo/bar']

# Generated at 2022-06-13 20:57:03.125847
# Unit test for function chown
def test_chown():
    if sys.platform.startswith('linux'):
        import warnings
        warnings.filterwarnings('ignore', "The 'warn' parameter of use() is ignored since Python 3.7",
                                category=DeprecationWarning)
        import grp
        uid = os.getuid()
        user = pwd.getpwuid(uid).pw_name
        gid = os.getgid()
        group = grp.getgrgid(gid).gr_name
        chown('/tmp/flutils.pathutils.test_chown', user, group, include_parent=True)
        assert os.stat('/tmp').st_uid == uid
        assert os.stat('/tmp').st_gid == gid
        chown('/tmp/flutils.pathutils.test_chown')
       

# Generated at 2022-06-13 20:57:05.268999
# Unit test for function directory_present
def test_directory_present():
    assert directory_present('/tmp/test_directory_present') == Path('/tmp/test_directory_present')
# directory_present



# Generated at 2022-06-13 20:57:10.645518
# Unit test for function exists_as
def test_exists_as():
    """Test function exists_as with a directory"""
    # Get a parent directory that must exist.
    temp_dir = directory_present(
        os.path.join(os.path.expandvars('$HOME'), 'temp_dir')
    )

    zpath = exists_as(temp_dir)
    assert zpath == 'directory'



# Generated at 2022-06-13 20:57:11.810959
# Unit test for function chmod
def test_chmod():
    """flutils.pathutils.chmod()
    """



# Generated at 2022-06-13 20:57:21.503160
# Unit test for function chmod
def test_chmod():
    _tmp_path = Path('~/tmp/flutils.tests.osutils.chmod.txt').expanduser()
    _tmp_path.parent.mkdir(exist_ok=True, parents=True)
    _tmp_path.touch()
    # Change the mode of the above file.
    chmod(_tmp_path, mode_file=0o660)
    assert _tmp_path.stat().st_mode & 0o777 == 0o660
    _tmp_path.unlink()


# Generated at 2022-06-13 20:57:24.961455
# Unit test for function directory_present
def test_directory_present():
    path = directory_present('~/tmp/test_path')
    assert path.exists()
    assert path.is_dir()
test_directory_present()



# Generated at 2022-06-13 20:57:29.139890
# Unit test for function chmod
def test_chmod():
    path = Path('/tmp/flutils-tests/pathutils-test_chmod/')
    path.mkdir(parents=True, exist_ok=True)

    chmod(path.as_posix())

    assert path.stat().st_mode == 16832



# Generated at 2022-06-13 20:57:31.148731
# Unit test for function directory_present
def test_directory_present():
    path = directory_present('.dir_present', mode=0o777)
assert path.is_dir()

# Generated at 2022-06-13 20:57:43.019909
# Unit test for function chown
def test_chown():
    from pathlib import Path
    from shutil import rmtree
    from tempfile import mkdtemp
    from time import time

    class TMP(Path):
        def __new__(cls) -> 'TMP':
            directory = mkdtemp()
            path = Path(directory)
            return cast('TMP', path.__class__(path._accessor, str(path)))

    def no_such_user() -> None:
        with pytest.raises(OSError):
            chown(path, user='no_such_user')

    def no_such_group() -> None:
        with pytest.raises(OSError):
            chown(path, group='no_such_group')

    # Test 1
    tmp = TMP()
    path = tmp / f'{int(time())}.txt'


# Generated at 2022-06-13 20:57:46.934370
# Unit test for function chmod
def test_chmod():
    path = Path('/tmp/temp.txt')
    try:
        path.write_text('')
        chmod(path, 0o777)
        assert path.stat().st_mode == 33279
    finally:
        path.unlink()


# Generated at 2022-06-13 20:58:12.199465
# Unit test for function exists_as
def test_exists_as():
    # Create the temporary file.
    with tempfile.NamedTemporaryFile(mode='w') as tmpfile:
        with tempfile.TemporaryDirectory() as tmpdirname:
            # Create a symlink in tmpdirname to the tmpfile.
            Path(
                os.path.join(slash(tmpdirname), 'tmpfile.txt')
            ).symlink_to(Path(tmpfile.name))

            assert exists_as(Path(tmpfile.name)) == 'file'

            assert exists_as(Path(os.path.join(tmpdirname, 'tmpfile.txt'))) == \
                'file'

        assert exists_as(Path(tmpdirname)) == ''



# Generated at 2022-06-13 20:58:22.717007
# Unit test for function chmod
def test_chmod():
    # Test normalization
    path = '~/tmp/flutils.tests.osutils.txt'
    norm_path = normalize_path(path)

    assert norm_path == Path(path).expanduser()

    # Create the path so chmod() doesn't fail
    norm_path.parent.mkdir(parents=True, exist_ok=True)
    norm_path.touch()

    # Test chmod
    chmod(norm_path)
    assert norm_path.stat().st_mode == 0o600



# Generated at 2022-06-13 20:58:28.774586
# Unit test for function path_absent
def test_path_absent():
    """Unit test for function flutils.pathutils.path_absent."""
    tdir = None

# Generated at 2022-06-13 20:58:31.982889
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~') == 'directory'
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/does_not_exist') == ''

# Generated at 2022-06-13 20:58:42.532621
# Unit test for function directory_present
def test_directory_present():
    with pytest.raises(ValueError) as e_info:
        directory_present('path/*', mode=0o775, user='root', group='wheel')
    assert (
        e_info.value.args[0] ==
        'The path: \'path/*\' must NOT contain any glob patterns.'
    )

    with pytest.raises(ValueError) as e_info:
        directory_present('../bin', mode=0o775, user='root', group='wheel')
    assert (
        e_info.value.args[0] ==
        'The path: \'../bin\' must be an absolute path.  A path is considered '
        'absolute if it has both a root and (if the flavour allows) a drive.'
    )



# Generated at 2022-06-13 20:58:51.205144
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    chown('~/tmp/flutils.tests.osutils.txt')
    chown('~/tmp/flutils.tests.osutils.txt', user='-1', group='-1')
    chown('~/tmp/**', user='-1', group='-1')
    chown('~/tmp/*', user='-1', group='-1')
    chown('~/tmp/flutils.tests.osutils.txt', user='root', group='root')
    chown('~/tmp/flutils.tests.osutils.txt', user='root', group='-1')
    chown('~/tmp/flutils.tests.osutils.txt', user='-1', group='root')

# Generated at 2022-06-13 20:59:04.826464
# Unit test for function directory_present
def test_directory_present():
    """Unit test for function directory_present."""
    import shutil

    def _run_test(
            path: Optional[Path] = None,
            mode: Optional[int] = 0o777,
            user: Optional[str] = None,
            group: Optional[str] = None,
            **kwargs
    ) -> None:
        """Move test path and create the path."""
        if path is not None:
            if path.exists() is True:
                shutil.rmtree(path.as_posix())

            path.mkdir(mode=mode)
            if user is not None:
                path_uid = pwd.getpwnam(user).pw_uid
                os.chown(path.as_posix(), path_uid, -1)
            if group is not None:
                path

# Generated at 2022-06-13 20:59:15.539213
# Unit test for function path_absent
def test_path_absent():
    testdir = tempfile.mkdtemp(
        prefix='path_absent',
        dir=Path.home(),
    )
    def fin():
        if os.path.exists(testdir):
            shutil.rmtree(testdir)
    request.addfinalizer(fin)
    path_exists(testdir)
    path_exists(os.path.join(testdir, 'file_one.txt'))
    path_exists(os.path.join(testdir, 'file_two.txt'))
    path_dir(os.path.join(testdir, 'test_dir'))
    # Set the files to be read only.
    set_read_only(os.path.join(testdir, 'file_one.txt'), True)

# Generated at 2022-06-13 20:59:16.671131
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:59:27.181115
# Unit test for function chmod
def test_chmod():
    # Ensure the path does not exist before the test starts
    with chdir('~/tmp/'):
        remove('flutils.tests.osutils.txt', recursive=True, force=True)
    # Run the function
    chmod('~/tmp/flutils.tests.osutils.txt', mode_file=0o660)
    # Test the function results
    if exists('~/tmp/flutils.tests.osutils.txt') is True:
        mode = stat('~/tmp/flutils.tests.osutils.txt').st_mode
        if mode == 0o660:
            assert True
    # Clean up after the test
    remove('~/tmp/flutils.tests.osutils.txt', recursive=True, force=True)



# Generated at 2022-06-13 20:59:46.230149
# Unit test for function chown
def test_chown():
    try:
        chown('~/tmp/flutils.tests.osutils.txt')
    except NotImplementedError:
        pass
    else:
        pass


# Generated at 2022-06-13 20:59:59.499440
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('.') == 'directory'
    assert exists_as(__file__) == 'file'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/zero') == 'block device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/tty0') == 'char device'
    assert exists_as('/dev/tty1') == 'char device'
    assert exists_as('/dev/tty2') == 'char device'
    assert exists_as('/dev/tty3') == 'char device'
    assert exists_as('/dev/tty4') == 'char device'
    assert exists_as('/dev/tty5') == 'char device'
    assert exists_as('/dev/tty6')

# Generated at 2022-06-13 21:00:06.823894
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(__file__) == 'file'
    assert exists_as('/dev') == ''
    assert exists_as('/dev/pts') == 'directory'
    assert exists_as('/dev/sda') == 'block device'
    assert exists_as('/dev/tty') == 'char device'
    assert exists_as('/dev/loop0') == 'block device'
    assert exists_as('/dev/video0') == 'char device'
    assert exists_as('/sys/class/net') == 'directory'
    assert exists_as('/sys/class/net/eth0') == ''



# Generated at 2022-06-13 21:00:08.948707
# Unit test for function chown
def test_chown():
    chown('~/tmp/flutils.tests.osutils.txt')
    assert True



# Generated at 2022-06-13 21:00:14.911152
# Unit test for function path_absent
def test_path_absent():
    path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
    os.makedirs(path)
    path_absent(path)
    assert os.path.exists(path) is False



# Generated at 2022-06-13 21:00:22.221765
# Unit test for function chmod
def test_chmod():
    import os
    import stat

    from flutils.pathutils import chmod

    with open('tmp.txt', 'w') as f:
        f.write('tmp')
    chmod('tmp.txt', 0o640)
    os.stat('tmp.txt').st_mode & stat.S_IRWXU



# Generated at 2022-06-13 21:00:32.324178
# Unit test for function exists_as
def test_exists_as():
    from testfixtures import compare, ShouldRaise
    from flutils.pathutils import directory_present, normalize_path

    # Test for existing path
    test_path = directory_present('/tmp/flutils.pathutils.tests.exists_as')
    with compare(exists_as(test_path), 'directory'):
        pass

    # Test for non-existant path
    with compare(exists_as(normalize_path('/this/path/does/not/exist')), ''):
        pass

    # Test the error condition where an existing path
    # is not a directory.  Note that this may need
    # to be disabled on some systems (i.e. Windows)

# Generated at 2022-06-13 21:00:40.880628
# Unit test for function exists_as
def test_exists_as():
    from .pathutils import get_tempdir

    tmpdir = get_tempdir()
    fpath = tmpdir.joinpath('test_exists_as.txt')
    dpath = tmpdir.joinpath('test_exists_as_dir')
    with fpath.open('w') as f:
        f.write('foo\n')

    assert exists_as(dpath) == ''
    assert exists_as(fpath) == 'file'
    dpath.mkdir()
    assert exists_as(dpath) == 'directory'



# Generated at 2022-06-13 21:00:46.227994
# Unit test for function chmod
def test_chmod():
    """Test function chmod."""
    file_path = normalize_path('~/tmp/flutils.tests.osutils.txt')
    if file_path.exists():
        file_path.unlink()
    file_path.touch()
    chmod(file_path, 0o660)
    file_path.unlink()



# Generated at 2022-06-13 21:00:58.829404
# Unit test for function chown
def test_chown():  # pylint: disable=unused-argument
    from flutils.flutils_test import (
        get_functions_test_args,
        get_test_namespace,
        print_test_start,
        print_test_success,
        print_test_failure,
        raise_test_failure,
        run_test,
    )
    test_namespace = get_test_namespace()
    if test_namespace != 'flutils.pathutils.test_pathutils':
        raise_test_failure('Wrong test namespace, "{0}", needed '
                           '"flutils.pathutils.test_pathutils"'.
                           format(test_namespace))
    print_test_start('chown')

# Generated at 2022-06-13 21:01:13.833771
# Unit test for function chown
def test_chown():
    pass



# Generated at 2022-06-13 21:01:27.639669
# Unit test for function directory_present
def test_directory_present():
    import shutil

    from flutils.pathutils import directory_present

    test_dir = Path.home().joinpath('tmp/flutils.tests')
    test_dir.mkdir(parents=True, exist_ok=True)

# Generated at 2022-06-13 21:01:36.795473
# Unit test for function path_absent
def test_path_absent():
    cwd = os.getcwd()
    test_path = Path(cwd) / '.test_path'
    try:
        path_absent(test_path)
        test_path.mkdir()
        test_path.joinpath('foo/bar').mkdir(parents=True)
        test_path.joinpath('foo/bar/baz').touch()
        assert os.path.exists(str(test_path)) is True
        path_absent(test_path)
        assert os.path.exists(str(test_path)) is False
    finally:
        path_absent(test_path)



# Generated at 2022-06-13 21:01:50.173703
# Unit test for function chown
def test_chown():
    path = Path(
        os.environ.get('HOME')
    ) / 'tmp' / 'flutils.tests.osutils.txt'

    if path.exists():
        path.unlink()

    path.touch()
    chown(path.as_posix(), '-1', '-1')
    # chown() sets owner and group to -1
    assert path.stat().st_uid == -1 and path.stat().st_gid == -1

    # chown() sets owner and group to
    # that user's uid and gid
    username = getpass.getuser()
    user = get_os_user(username)

    chown(path.as_posix(), username)
    assert path.stat().st_uid == user.pw_uid


# Generated at 2022-06-13 21:01:51.650680
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(__file__) == 'file'



# Generated at 2022-06-13 21:02:05.446918
# Unit test for function exists_as
def test_exists_as():
    from pathlib import Path
    from unittest import mock
    from tempfile import TemporaryFile

    exists_patcher = mock.patch(
        'flutils.pathutils.exists_as', autospec=True
    )
    exists_mock = exists_patcher.start()

    exists_mock.side_effect = [
        'directory', 'socket', '', '', 'FIFO', '', 'file', '', '', '', '',
        '', '', '', '', '', '', 'block device', '', '', '', 'char device',
        '', '', '',
    ]

    assert exists_as(Path('~/tmp')) == 'directory'
    assert exists_as(Path('~/tmp')) == 'socket'
    assert exists_as(Path('~/tmp'))

# Generated at 2022-06-13 21:02:11.999999
# Unit test for function exists_as
def test_exists_as():
    import os

    TEST_FILE = 'test_file'
    TEST_DIR = 'test_dir'

    try:
        os.mkfifo(TEST_FILE)

        assert exists_as(TEST_FILE) == 'FIFO'
        assert exists_as(TEST_DIR) == ''

        os.mkdir(TEST_DIR)

        assert exists_as(TEST_DIR) == 'directory'

    finally:
        try:
            os.remove(TEST_FILE)
        except:
            pass

        try:
            os.rmdir(TEST_DIR)
        except:
            pass



# Generated at 2022-06-13 21:02:25.106897
# Unit test for function path_absent
def test_path_absent():
    import os
    import shutil
    import tempfile
    import textwrap
    import unittest

    import flutils.pathutils as fu

    class PathAbsentUnitTests(unittest.TestCase):
        """Unit tests for function path_absent."""
        def setUp(self):
            self.dirs_and_links = [
                os.path.join('foo', 'bar'),
                os.path.join('foo', 'foo_file'),
                os.path.join('foo_file'),
                os.path.join('bar')
            ]
            try:
                os.remove('foo_file')
            except OSError:
                pass

# Generated at 2022-06-13 21:02:26.968808
# Unit test for function chmod
def test_chmod():
    """Test the :func:`~flutils.pathutils.chmod` function."""
    assert True



# Generated at 2022-06-13 21:02:38.944957
# Unit test for function chmod
def test_chmod():
    """pytest for flutils.osutils.chmod."""

    from flutils.systemutils import prepare_fixtures, remove_fixtures

    prepare_fixtures()

    path = Path('./tmp/flutils.osutils/chmod_test/')

    path.mkdir(exist_ok=True, parents=True)

    file_1 = path / 'file_1.txt'
    file_2 = path / 'file_2.txt'
    file_3 = path / 'file_3.txt'

    file_1.touch()
    file_2.touch()
    file_3.touch()

    chmod(str(path / 'file_1.txt'), 0o666)

    assert file_1.stat().st_mode & 0o777 == 0o666


# Generated at 2022-06-13 21:03:18.804713
# Unit test for function exists_as
def test_exists_as():
    import os
    from flutils.pathutils import exists_as

    assert exists_as(__file__) == 'file'

    path = Path(__file__).parent / os.fspath('tmp')
    if path.exists():
        if path.is_dir():
            rmtree(path.as_posix())
        else:
            os.remove(path.as_posix())

    path.touch()
    assert exists_as(path.as_posix()) == 'file'
    os.remove(path.as_posix())
    assert exists_as(path.as_posix()) == ''

    # This is the Windows temp path on all machines.
    temp_path = Path('C:') / os.fspath('Windows') / os.fspath('Temp')

# Generated at 2022-06-13 21:03:32.019130
# Unit test for function chown
def test_chown():
    def mock_chown(path, uid, gid):
        return path, uid, gid

    old_chown = os.chown
    os.chown = mock_chown
    path = '~/tmp/flutils.tests.osutils.txt'
    normalizepath = os.path.expanduser(path)
    chown(path)
    assert normalizepath == mock_chown.__getitem__(0)
    path = '~/tmp'
    normalizepath = os.path.expanduser(path)
    chown(path, include_parent=True)
    assert normalizepath == mock_chown.__getitem__(0)
    os.chown = old_chown

