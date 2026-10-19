

# Generated at 2022-06-13 20:54:02.094115
# Unit test for function chmod
def test_chmod():
    pass


# Generated at 2022-06-13 20:54:06.512178
# Unit test for function path_absent
def test_path_absent():
    # make a test directory
    with tempfile.TemporaryDirectory(prefix='flutils_test_') as tmp:
        tmp = Path(tmp)
        # create test path
        test_path = Path(tmp.as_posix(), 'test_path')
        test_path.mkdir()
        # make sure the test path exists
        assert test_path.exists()
        # run the function
        path_absent(test_path)
        # test to see the path is absent
        assert not test_path.exists()



# Generated at 2022-06-13 20:54:09.113620
# Unit test for function directory_present
def test_directory_present():
    tmp_dir = Path('/tmp/flutils.tests.pathutils')
    try:
        if exists_as(tmp_dir) == '':
            directory_present(tmp_dir)
        tmp_dir = directory_present(tmp_dir)
    except:
        if tmp_dir.exists():
            tmp_dir.rmdir()
        raise

    return tmp_dir



# Generated at 2022-06-13 20:54:09.869708
# Unit test for function chmod
def test_chmod():
    pass



# Generated at 2022-06-13 20:54:22.754280
# Unit test for function path_absent
def test_path_absent():
    # Create a test directory and file.
    tdir = './test_dir/'
    tfile = './test_dir/test.txt'
    tlink = './test_dir/test.link'
    tdir2 = './test_dir/sdir'

    # Remove the test directory if it exists.
    path_absent(tdir)

    # Create the test directory and a file to test with.
    os.mkdir(tdir)
    open(tfile, 'a').close()

    # Create a symlink
    os.symlink(tfile, tlink)

    # Create a sub-directory
    os.mkdir(tdir2)

    # First test without recursion
    path_absent(tdir)
    assert (not os.path.exists(tdir))
   

# Generated at 2022-06-13 20:54:33.196390
# Unit test for function chmod
def test_chmod():
    file_path = Path('/tmp/flutils.tests.osutils.txt')
    file_path.touch()

    directory_path = Path('/tmp/flutils.tests.osutils.dir')
    directory_path.mkdir(parents=True, exist_ok=True)

    assert file_path.exists() is True
    assert directory_path.exists() is True

    chmod(file_path, 0o660)
    chmod(directory_path, 0o720)

    assert file_path.stat().st_mode == 420
    assert directory_path.stat().st_mode == 544

    file_path.unlink()
    directory_path.rmdir()

    assert file_path.exists() is False
    assert directory_path.exists() is False



# Generated at 2022-06-13 20:54:41.006009
# Unit test for function find_paths
def test_find_paths():
    from tempfile import mkdtemp
    from pathlib import Path
    import os

    assert list(find_paths(Path(mkdtemp()))) == []

    try:
        d = Path(mkdtemp())
        assert list(find_paths(d)) == []

        Path(os.path.join(d, 'f1')).touch()
        assert list(find_paths(d)) == [d/'f1']

        Path(os.path.join(d, 'd1')).mkdir()
        assert list(find_paths(d)) == [d/'f1', d/'d1']
    finally:
        shutil.rmtree(d)



# Generated at 2022-06-13 20:54:51.907979
# Unit test for function find_paths
def test_find_paths():
    tmp_path = Path.home() / 'tmp'
    tmp_path.mkdir(exist_ok=True)

    # Create a file and a directory in the temporary directory.
    file_one = tmp_path / 'file_one'
    file_one.write_text('Test Message')
    dir_one = tmp_path / 'dir_one'
    dir_one.mkdir()

    # Get the directory's immediate contents.
    results = list(find_paths(tmp_path / '*'))
    assert len(results) == 2
    assert results[0] == tmp_path / 'file_one'
    assert results[1] == tmp_path / 'dir_one'

    shutil.rmtree(tmp_path)



# Generated at 2022-06-13 20:54:57.580339
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent
    from flutils.pathutils import path_present
    import tempfile
    def make_path():
        tf = tempfile.NamedTemporaryFile()
        tf.close()
        return tf.name

    test_path = make_path()
    path_present(test_path, user='root', mode_file=0o700)
    assert os.path.exists(test_path)

    path_absent(test_path)
    assert os.path.exists(test_path) == False



# Generated at 2022-06-13 20:55:08.209099
# Unit test for function exists_as
def test_exists_as():
    tmpdir = tempfile.mkdtemp(dir='/tmp')

# Generated at 2022-06-13 20:55:27.518030
# Unit test for function path_absent
def test_path_absent():
    with temporary_directory(prefix='test_path_utils_') as path:
        path = Path(path)
        path_file = path / 'file'
        path_file.write_bytes(b'@')
        path_dir = path / 'dir'
        path_dir.mkdir()

        assert os.path.isfile(path_file)
        assert os.path.isdir(path_dir)
        path_absent(path_file)
        path_absent(path_dir)
        assert os.path.isfile(path_file) is False
        assert os.path.isdir(path_dir) is False



# Generated at 2022-06-13 20:55:33.688356
# Unit test for function path_absent
def test_path_absent():
    test_path = Path('~/tmp/test_path')
    test_path.mkdir(mode=0o777, parents=True)
    test_path.joinpath('test_file').touch()
    test_path.joinpath('test_dir').mkdir(mode=0o777)
    with test_path.joinpath('test_dir').joinpath('test_file').open('w') as f:
        f.write('test')
    test_path.joinpath('test_dir').joinpath('test_link').symlink_to('test_file')
    test_path.joinpath('test_link').symlink_to('test_dir')
    test_path.joinpath('test_file2.txt').touch()
    test_path.joinpath('test_file3').touch()

# Generated at 2022-06-13 20:55:35.799861
# Unit test for function exists_as
def test_exists_as():
    """Test function `exists_as` using the pytest framework."""
    assert exists_as('') == ''
    assert exists_as('/tmp') == 'directory'
    assert exists_as('/etc/hosts') == 'file'



# Generated at 2022-06-13 20:55:44.363012
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('/') == 'directory'
    assert exists_as('/bin') == 'directory'
    assert exists_as('/usr') == 'directory'
    assert exists_as('/etc') == 'directory'
    assert exists_as('/etc/group') == 'file'
    assert exists_as('/etc/passwd') == 'file'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/random') == 'char device'
    assert exists_as('/dev') == 'directory'
    assert exists_as('/dev/mapper') == 'directory'
    assert exists_as('/dev/mapper/control') == 'block device'

# Generated at 2022-06-13 20:55:49.846885
# Unit test for function chown
def test_chown():
    assert_raises(OSError, chown, '~/tmp', user='somenotrealexist')
    assert_raises(OSError, chown, '~/tmp', group='somenotrealexist')



# Generated at 2022-06-13 20:56:02.130714
# Unit test for function exists_as
def test_exists_as():
    # Test the happy path
    assert exists_as('README.md') == 'file'
    assert exists_as('fixtures') == 'directory'
    assert exists_as('/dev/urandom') == 'char device'
    assert exists_as('/dev/random') == 'block device'
    assert exists_as('/dev/tty') == 'char device'

    # Test the error paths
    assert exists_as('/path/that/does/not/exist') == ''
    assert exists_as('/dev/urandom/foo/bar') == ''
    assert exists_as('/etc/passwd/foo/bar') == ''
    assert exists_as('/etc/passwd/foo/bar') == ''
    assert exists_as('/etc/passwd/../etc/shadow') == ''


# Generated at 2022-06-13 20:56:13.398914
# Unit test for function path_absent
def test_path_absent():
    with open('/tmp/test_file', 'w', encoding='utf-8') as f:
        f.write('test')
    if os.path.isdir('/tmp/test_dir'):
        shutil.rmtree('/tmp/test_dir')
    os.mkdir('/tmp/test_dir')
    os.symlink('/tmp/test_file', '/tmp/test_dir/test_file_link')
    path_absent('/tmp/test_dir')
    assert not os.path.exists('/tmp/test_dir')
    assert not os.path.islink('/tmp/test_dir/test_file_link')
    assert os.path.isfile('/tmp/test_file')



# Generated at 2022-06-13 20:56:24.457703
# Unit test for function chown
def test_chown():
    path = '~/tmp/flutils.tests.osutils.txt'
    user = getpass.getuser()
    group = grp.getgrgid(pwd.getpwnam(user).pw_gid).gr_name

    # '-1' should preserve ownership
    chown(path, user='-1', group='-1')
    # Get current ownership and make sure it doesn't change.
    pre_path_stat = os.stat(normalize_path(path).as_posix())
    chown(path)
    post_path_stat = os.stat(normalize_path(path).as_posix())
    assert pre_path_stat.st_uid == post_path_stat.st_uid
    assert pre_path_stat.st_gid == post_path_stat.st_

# Generated at 2022-06-13 20:56:30.227840
# Unit test for function find_paths
def test_find_paths():
    path = Path().cwd().absolute()
    path.mkdir(0o700, exist_ok=True)
    file_one = (path / 'file_one').as_posix()
    open(file_one, 'a').close()
    dir_one = (path / 'dir_one').as_posix()
    os.mkdir(dir_one)
    paths = list(find_paths(path.as_posix()))
    for i in range(0, len(paths)):
        paths[i] = str(paths[i].absolute())
    assert sorted([file_one, dir_one]) == sorted(paths)



# Generated at 2022-06-13 20:56:34.574540
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/__init__.py') == 'file'
    assert exists_as('~/tmp/__init__.pyt') == ''
    assert exists_as('~/foo/bar') == ''



# Generated at 2022-06-13 20:57:09.686500
# Unit test for function find_paths
def test_find_paths():
    test_path = Path(Path.home(), 'tmp', 'test_path')

# Generated at 2022-06-13 20:57:24.073895
# Unit test for function find_paths
def test_find_paths():
    with mock.patch(
        'flutils.pathutils.Path',
        new_callable=mock.MagicMock,
        autospec=True,
        spec_set=True
    ) as Path:
        pattern = '~/tmp/*'
        search = '~/tmp/*'
        path_mock = mock.MagicMock(spec_set=Path)
        path_mock.as_posix.return_value = '~/tmp/*'
        path_mock.__len__.return_value = 8
        path_mock.anchor = '~'
        Path.return_value = path_mock
        path_mock.glob.return_value = [
            'file_one',
            'dir_one'
        ]

# Generated at 2022-06-13 20:57:34.632638
# Unit test for function find_paths
def test_find_paths():
    from flutils.testutils import Printer
    from pathlib import Path

    tmp_path = Path('/tmp/flutils/test_find_paths')
    tmp_path.mkdir(parents=True, exist_ok=True)

    # Create some files and directories
    for path in ('file1', 'file2', 'dir1', 'dir2', 'dir3'):
        (tmp_path / path).touch()

    assert len(list(tmp_path.glob('*'))) == 5

    # Things to match
    all_things = list(find_paths(tmp_path / '*'))
    assert len(all_things) == 5
    assert all([path.is_file() for path in all_things]) is True

    test_file = tmp_path / 'file1'

# Generated at 2022-06-13 20:57:42.680103
# Unit test for function find_paths
def test_find_paths():
    """Test the result of the function, find_paths."""
    created_paths = []
    with TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        created_paths.append(
            temp_dir_path.joinpath('file_one').touch()
        )
        created_paths.append(
            temp_dir_path.joinpath('dir_one').mkdir()
        )
        yield assert_equal, list(find_paths(temp_dir_path.as_posix())),\
            created_paths



# Generated at 2022-06-13 20:57:55.711613
# Unit test for function find_paths
def test_find_paths():
    """Find all paths that match the given :term:`glob pattern`."""
    from pathlib import Path
    from tempfile import mkdtemp
    import warnings
    from unittest import TestCase
    from unittest.mock import MagicMock, patch

    from flutils.pathutils import find_paths

    class Test_find_paths(TestCase):
        def setUp(self):
            self.directories = []
            self.temp_dir = mkdtemp(prefix='test_find_paths.')
            self.addCleanup(rmtree, self.temp_dir)

        def tearDown(self):
            # Clean up the directories created.
            for dir_path in self.directories:
                try:
                    dir_path.rmdir()
                except OSError:
                    pass

# Generated at 2022-06-13 20:58:07.455145
# Unit test for function find_paths
def test_find_paths():
    base = 'testuser'
    if Path('/Users/').exists():
        base = 'Users'
    with tempfile.TemporaryDirectory(
            prefix='testuser_',
            dir='/{}/'.format(base)
    ) as tmpdir:
        testdir = Path(tmpdir)

        file_one = testdir / 'file_one'
        file_two = testdir / 'file_two'
        file_three = testdir / 'file_three'

        for file in [
                file_one,
                file_two,
                file_three
        ]:
            file.touch()

        dir_one = testdir / 'dir_one'
        dir_two = testdir / 'dir_two'
        for dir in [dir_one, dir_two]:
            dir.mkdir()



# Generated at 2022-06-13 20:58:10.729818
# Unit test for function chown
def test_chown():
    chown(__file__, group='-1')
    assert get_os_group(os.stat(__file__).st_gid).gr_gid == get_os_group().gr_gid



# Generated at 2022-06-13 20:58:18.646943
# Unit test for function exists_as
def test_exists_as():
    """Unit test for function exists_as."""
    sub_dir = getfixture('test_dir') / 'test_exists_as'
    sub_dir.mkdir(parents=True)

    path1 = sub_dir / 'test_symlink'
    symlink_target = sub_dir / 'data'

    # The following will create a dead symlink
    path1.symlink_to(symlink_target,  target_is_directory=True)
    assert exists_as(path1) == ''

    # The following will create a dead symlink
    path1.symlink_to(symlink_target)
    assert exists_as(path1) == ''

    # The following will create a block device
    path1.touch(mode=0o600)
    path1.chmod

# Generated at 2022-06-13 20:58:28.720916
# Unit test for function chmod
def test_chmod():
    from flutils.tests.pathutils import (
        setup_files,
        teardown_files,
    )

    try:
        file_path_str = (
            '{}/flutils.tests.pathutils.osutils.txt'.format(
                Path.home()
            )
        )
        file_path = setup_files(file_path_str)
        chmod(file_path, mode_file=0o660)
        assert file_path.stat().st_mode & 0o777 == 0o660
    finally:
        teardown_files(file_path_str)



# Generated at 2022-06-13 20:58:31.932379
# Unit test for function find_paths
def test_find_paths():
    assert set(find_paths('~/tmp/*')) == set(
        [Path('~/tmp/file_one'),
         Path('~/tmp/dir_one')]
    )



# Generated at 2022-06-13 20:58:51.323044
# Unit test for function chown
def test_chown():
    log_fmt = '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)s][%(funcName)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_fmt)
    logging.getLogger('flutils.pathutils').setLevel(logging.DEBUG)
    # Find the log file
    log_path = os.path.join(os.path.dirname(__file__), 'flutils.pathutils.log')
    # Create temporary directory to write test files
    dname = tempfile.mkdtemp()
    logging.info('dname = {!r}'.format(dname))
    user = pwd.getpwuid(os.geteuid()).pw_name
    group = gr

# Generated at 2022-06-13 20:58:57.787792
# Unit test for function exists_as
def test_exists_as():
    data = [
        ('~/tmp', 'directory'),
        ('~/tmp/flutils.tests.pathutils.test_exists_as.txt', 'file'),
    ]
    for path, expected in data:
        result = exists_as(path)
        assert result == expected



# Generated at 2022-06-13 20:59:06.091662
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    from .osutils import RandomTestPath
    from .osutils import TEST_MODE_FILE
    from .osutils import TEST_MODE_DIR
    from .osutils import TEST_MODE_PARENT

    rnd_path = RandomTestPath(is_dir=True)
    assert rnd_path.exists() is True
    assert rnd_path.parent.exists() is True

    rnd_file = RandomTestPath(is_dir=False)
    assert rnd_file.exists() is True
    assert rnd_file.parent.exists() is True

    # Test the function with a non-glob and non-existent path.
    chmod('/tmp/does-not-exist')

    # Test the function with a non-glob and a directory.
    chmod

# Generated at 2022-06-13 20:59:16.108245
# Unit test for function path_absent
def test_path_absent():
    import os
    import shutil
    import tempfile

    test_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 20:59:18.116365
# Unit test for function exists_as
def test_exists_as():
    """
    The file pathutils.exists_as() has not been tested.
    """
    pass



# Generated at 2022-06-13 20:59:28.687555
# Unit test for function get_os_user
def test_get_os_user():
    # There is really not much to test since this function is
    # simply a wrapper for the pwd.getpwuid() and pwd.getpwnam().
    # Just make sure the functions are called and try to handle
    # the exceptions that may be thrown.

    # Mock the pwd module to reduce the test code.
    import pwd
    getpwuid_mock = MagicMock()
    getpwnam_mock = MagicMock()
    getpass_getuser_mock = MagicMock()
    pwd.getpwuid = getpwuid_mock
    pwd.getpwnam = getpwnam_mock
    getpass.getuser = getpass_getuser_mock

    # Test calling the function without any arguments.
    get_os_user()
    # Called four times

# Generated at 2022-06-13 20:59:34.259262
# Unit test for function path_absent
def test_path_absent():
    path = Path(testing_path).joinpath('test_path')
    path.mkdir(parents=True)
    p = path.joinpath('test')
    p.touch()
    path_absent(path)
    assert path.exists() is False
    assert p.exists() is False



# Generated at 2022-06-13 20:59:40.054899
# Unit test for function directory_present
def test_directory_present():
    directory_present('~/tmp/flutils.tests.osutils.txt', mode=0o700)
    directory_present('~/tmp/flutils.tests.osutils.txt')
    directory_present('~/tmp/flutils.tests.osutils.txt', mode=0o700)



# Generated at 2022-06-13 20:59:50.559380
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent
    from flutils.pathutils import path_contains
    from flutils.pathutils import path_exists
    from flutils.pathutils import path_present
    from flutils.testing import capture_stdout_stderr

    # Setup
    path = path_present('~/tmp/path_absent')
    path_present('~/tmp/path_absent/foo/bar')
    path_present('~/tmp/path_absent/fizz/buzz')
    path_present('~/tmp/path_absent/fizz/buzz/file_one')
    path_present('~/tmp/path_absent/fizz/buzz/file_two')

# Generated at 2022-06-13 20:59:55.559051
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    user = getpass.getuser()
    group = grp.getgrgid(os.getgid()).gr_name
    chown('/tmp/flutils.tests.osutils.txt', user=user, group=group)



# Generated at 2022-06-13 21:00:12.377930
# Unit test for function chown
def test_chown():
    """
    Function to test chown
    """
    # create temp directory
    tempdir = Path(tempfile.mkdtemp())
    # create test files
    file1 = tempdir / 'file1'
    file1.touch()
    file1_path = file1.as_posix()

    file2 = tempdir / 'file2'
    file2.touch()
    file2_path = file2.as_posix()

    # create test directories
    subdir1 = tempdir / 'subdir1'
    subdir1.mkdir(parents=True)
    subdir1_path = subdir1.as_posix()

    subdir2 = tempdir / 'subdir2'
    subdir2.mkdir(parents=True)
    subdir2_path = subdir2.as_posix

# Generated at 2022-06-13 21:00:15.233024
# Unit test for function exists_as
def test_exists_as():
    assert exists_as(Path(__file__)) == 'file'
    assert exists_as(Path(__file__).parent) == 'directory'



# Generated at 2022-06-13 21:00:24.101989
# Unit test for function chown
def test_chown():
  import os
  import tempfile
  from flutils.pathutils import chown, normalize_path
  uid = os.getuid()
  gid = os.getgid()
  folder = tempfile.gettempdir()
  p = normalize_path(os.path.join(folder, 'foo'))
  p.mkdir(mode=0o700, parents=False, exist_ok=True)
  assert p.owner() == uid
  assert p.group() == gid
  chown(p, user='-1', group='-1')
  assert p.owner() == uid
  assert p.group() == gid
  chown(p, user=uid, group=gid)
  assert p.owner() == uid
  assert p.group() == gid
  os.rmd

# Generated at 2022-06-13 21:00:29.212635
# Unit test for function chown
def test_chown():
    assert chown('~/tmp/flutils.tests.osutils.txt') is None
    assert chown('~/tmp/**') is None
    assert chown('~/tmp/*', user='foo', group='bar') is None


# Generated at 2022-06-13 21:00:41.116055
# Unit test for function directory_present
def test_directory_present():
    # From function directory_present
    path = directory_present('~/tmp/test_path')
    assert path.as_posix() == '/home/len/tmp/test_path'
    path = directory_present('~/tmp/test_path', user='-1')
    assert path.as_posix() == '/home/len/tmp/test_path'
    path = directory_present('~/tmp/test_path', user='flutils')
    assert path.as_posix() == '/home/len/tmp/test_path'
    path = directory_present('~/tmp/test_path', user='flutils', mode=0o660)
    assert path.as_posix() == '/home/len/tmp/test_path'

# Generated at 2022-06-13 21:00:48.146347
# Unit test for function path_absent
def test_path_absent():
    from flutils.pathutils import path_absent
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdirname = Path(tmpdirname)
        path = tmpdirname.joinpath('foo').as_posix()
        with open(path, 'w') as fp:
            fp.write('')
        assert Path(path).exists()
        path_absent(path)
        assert Path(path).exists() is False

# Generated at 2022-06-13 21:01:01.420151
# Unit test for function chmod
def test_chmod():
    assert os.path.exists('tmp/flutils.tests.osutils.txt') is True
    chmod('tmp/flutils.tests.osutils.txt', 0o660)
    assert os.stat('tmp/flutils.tests.osutils.txt').st_mode & 0o700 == 0o660

    assert os.path.exists('tmp/flutils.tests.osutils.txt') is True
    chmod('tmp/flutils.tests.osutils.txt', 0o600)
    assert os.stat('tmp/flutils.tests.osutils.txt').st_mode & 0o700 == 0o600

    with pytest.raises(TypeError):
        chmod('tmp/flutils.tests.osutils.txt', mode_file=3.0)


# Generated at 2022-06-13 21:01:12.981107
# Unit test for function chown
def test_chown():
    from flutils.pathutils import chown
    from pathlib import Path
    import os
    import tempfile

    user = getpass.getuser()
    group = grp.getgrgid(os.getgid()).gr_name


    def user_is(path, usr):
        return os.stat(path.as_posix()).st_uid == pwd.getpwnam(usr).pw_uid


    def group_is(path, grp):
        return os.stat(path.as_posix()).st_gid == grp.gr_gid


    with tempfile.TemporaryDirectory() as d:
        tmp_path = Path(d)
        files = tmp_path / 'files'
        files2 = tmp_path / 'files2'

# Generated at 2022-06-13 21:01:13.622200
# Unit test for function chmod
def test_chmod():
    assert True



# Generated at 2022-06-13 21:01:17.210868
# Unit test for function exists_as
def test_exists_as():
    return_message = exists_as('./exists_as')
    assert return_message == 'directory'
    remove_all('./exists_as')



# Generated at 2022-06-13 21:01:38.424944
# Unit test for function path_absent
def test_path_absent():
    import flutils.pathutils
    import os.path

    def _assert(value: bool) -> None:
        assert value

    def _assert_not(value: bool) -> None:
        assert not value

    def _test1() -> None:
        """Test deleting a non-directory file."""
        path = flutils.pathutils.Path('/tmp/file_one.txt')
        path.touch()
        flutils.pathutils.path_absent(path)
        _assert_not(os.path.exists(path))

    def _test2() -> None:
        """Test deleting a directory."""
        path = flutils.pathutils.Path('/tmp/sub_dir')
        path.mkdir(parents=True)
        path.joinpath('file_one.txt').touch()

# Generated at 2022-06-13 21:01:51.415577
# Unit test for function exists_as
def test_exists_as():
    import os
    import pwd
    import time

    from ..tests.osutils import RESOURCES_DIR as RESOURCES

    path = RESOURCES/'exists_as.dir'
    os.mkdir(path.as_posix())
    assert exists_as(path) == 'directory'

    path = RESOURCES/'exists_as.file'
    with open(path.as_posix(), 'w') as f:
        f.write('foo')
    assert exists_as(path) == 'file'

    # Need to be root to create devices. Skip if not root.
    if pwd.getpwuid(os.geteuid())[0] != 'root':
        return

    path = RESOURCES/'exists_as.block_device'
    os.m

# Generated at 2022-06-13 21:01:52.170524
# Unit test for function chmod
def test_chmod():
    assert True



# Generated at 2022-06-13 21:01:59.848530
# Unit test for function directory_present
def test_directory_present():
    path = Path('~/tmp/test_directory_present').expanduser()
    path_obj = directory_present(path)
    assert path_obj.exists() is True
    assert path_obj.is_dir() is True
    path_obj.rmdir()

    path = Path('~/tmp/test_directory_present/foo').expanduser()
    path_obj = directory_present(path)
    assert path_obj.exists() is True
    assert path_obj.is_dir() is True
    path_obj.parent.rmdir()

    # Test that the directory has been created with the given mode
    path = Path('~/tmp/test_directory_present').expanduser()
    path_obj = directory_present(path, mode=0o777)
    assert path_obj.exists()

# Generated at 2022-06-13 21:02:10.481591
# Unit test for function exists_as
def test_exists_as():
    path = normalize_path(__file__)
    assert exists_as(path) == 'file'
    assert exists_as(path.parent) == 'directory'
    assert exists_as(path.parent.parent) == 'directory'
    assert exists_as(path.parent.parent.parent) == 'directory'
    assert exists_as(path.parent.parent.parent.parent) == 'directory'
    assert exists_as(path / 'does_not_exist') == ''
    assert exists_as(path.parent / 'does_not_exist') == ''
    assert exists_as(path.parent.parent / 'does_not_exist') == ''
    assert exists_as(path.parent.parent.parent / 'does_not_exist') == ''

# Generated at 2022-06-13 21:02:24.027178
# Unit test for function chmod
def test_chmod():
    from flutils.pathutils import chmod
    from tempfile import TemporaryDirectory
    import os

    with TemporaryDirectory() as tmp_dir:
        test_data_dir = os.path.join(tmp_dir, 'data_dir')
        test_data_file = os.path.join(test_data_dir, 'data_file.txt')

        os.mkdir(test_data_dir)
        Path(test_data_file).touch()

        # Test default mode of 0o700 and 0o600
        chmod(test_data_dir)
        chmod(test_data_file)

        assert oct(os.stat(test_data_dir).st_mode & 0o777) == '0o700'

# Generated at 2022-06-13 21:02:30.105000
# Unit test for function chmod
def test_chmod():
    with tempdir() as location:
        dir_path = Path(location).joinpath('tmp')
        txt_path = Path(location).joinpath('tmp/flutils.tests.osutils.txt')
        dir_path.mkdir()
        txt_path.touch()
        chmod(txt_path, 0o660)


# Generated at 2022-06-13 21:02:39.633662
# Unit test for function chmod
def test_chmod():
    """Unit testing for function chmod."""
    import os
    import random
    import string
    from subprocess import PIPE
    from subprocess import run

    def random_string(str_len: int) -> str:
        """Generate a random string of specified length."""
        return ''.join(
            random.SystemRandom().choice(
                string.ascii_lowercase) for _ in range(str_len)
        )

    def get_mode(path: _PATH) -> int:
        """Get the octal mode of a file."""
        cmd = ['stat', '--format=%a', str(path)]
        output = run(cmd, check=True, stdout=PIPE)
        return int(output.stdout.decode())


# Generated at 2022-06-13 21:02:43.115877
# Unit test for function directory_present
def test_directory_present():
    path = normalize_path('./test_directory_present')
    directory_present(path)
    # cleanup
    if path.exists():
        path.rmdir()

test_directory_present()


# Generated at 2022-06-13 21:02:53.140433
# Unit test for function exists_as
def test_exists_as():

    f = Path(__file__)
    assert exists_as(f) == 'file'

    d = f.parent
    assert exists_as(d) == 'directory'
    assert exists_as('/dev/null') == 'char device'
    assert exists_as('/dev/ttys000') == 'char device'
    assert exists_as('/dev/disk0s1') == 'block device'
    assert exists_as('/dev/disk2s2') == 'block device'
    assert exists_as('/dev/fd/0') == 'socket'
    assert exists_as('/dev/fd/1') == 'socket'
    assert exists_as('/dev/fd/2') == 'socket'
    assert exists_as('/dev/fd/3') == 'socket'

# Generated at 2022-06-13 21:03:13.669406
# Unit test for function chmod
def test_chmod():
    import stat

    # Create a file to chmod
    temp_path = Path(gettempdir()) / 'flutils_osutils_chmod.txt'
    temp_path.touch()

    assert temp_path.exists() is True

    # Change the mode of the file so we can test for it later
    chmod(temp_path, 0o666)
    assert temp_path.exists() is True
    assert stat.S_IMODE(temp_path.stat().st_mode) == 0o666

    # Attempt to change the mode of a non-existing path
    tmp_path = Path(gettempdir()) / 'flutils_osutils_chmod_not_exist'
    assert tmp_path.exists() is False
    chmod(tmp_path, 0o666)

# Generated at 2022-06-13 21:03:22.010254
# Unit test for function exists_as
def test_exists_as():
    """Unit test for function :obj:`~flutils.pathutils.exists_as`.
    """
    from tempfile import TemporaryFile
    from flutils.pathutils import directory_present
    from flutils.pathutils import exists_as
    from flutils.pathutils import normalize_path

    path = normalize_path('~/tmp')
    if exists_as(path) == '':
        path = directory_present(path)

    try:
        tf = TemporaryFile(dir=path)

        assert type(tf) is TemporaryFile
        assert exists_as(tf.name) == 'file'
    finally:
        tf.close()



# Generated at 2022-06-13 21:03:24.531746
# Unit test for function exists_as
def test_exists_as():
    assert exists_as('~/tmp') == 'directory'
    assert exists_as('~/tmp/foo.txt') == 'file'


# Generated at 2022-06-13 21:03:35.295385
# Unit test for function chmod
def test_chmod():
    from flutils.testutils import UnitTester
    from flutils.pathutils import chmod
    from flutils import osutils

    tester = UnitTester(chmod)

    # test with non-existent file
    tests = [
        'test_normal_path',
        'test_normal_path_exists_as_file',
        'test_normal_path_exists_as_dir',
        'test_normal_path_exists_as_symlink',
        'test_normal_path_exists_as_symlink_file',
        'test_normal_path_exists_as_symlink_dir',
        'test_glob_path',
        'test_glob_path_single',
        'test_glob_path_empty',
    ]

    temp_dir = os