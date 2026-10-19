

# Generated at 2022-06-14 09:41:11.299223
# Unit test for function side_effect
def test_side_effect():
    with zipfile.ZipFile('test.zip', 'w') as archive:
        archive.writestr('bla.sh', '#!/bin/bash')
        archive.writestr('bla/test.h', 'Ha!')
        archive.writestr('bla/test.c', 'Ha!')

    try:
        side_effect(None, u'unzip test.zip bla.sh bla/test.h')
        assert os.path.isfile('bla.sh')
        assert os.path.isfile('bla/test.h')
        assert not os.path.isfile('test.c')
        assert os.path.isdir('bla')
    finally:
        shutil.rmtree('bla')
        os.remove('bla.sh')

# Generated at 2022-06-14 09:41:22.570599
# Unit test for function match
def test_match():
    # unzip -l file.zip:
        # Archive:  file.zip
        #   Length      Date    Time    Name
        # ----------  ---------- -----   ----
        #        581  2015-09-01 20:39   file.txt
        # ----------         --- -------
        #        581             1 file
    assert _is_bad_zip('tests/test_match.txt') == True

    # unzip -l file_good.zip:
        # Archive:  file_good.zip
        #   Length      Date    Time    Name
        # ----------  ---------- -----   ----
        #        581  2015-09-01 20:39   file.txt
        #        581  2015-09-01 20:39   file2.txt
        # ----------         --- -------
        #       1162             2 files

# Generated at 2022-06-14 09:41:25.149619
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', ''))
    assert not match(Command('unzip file.zip -d dir', ''))
    assert not match(Command('unzip file.zip /home/user/', ''))


# Generated at 2022-06-14 09:41:33.599841
# Unit test for function side_effect
def test_side_effect():
    # remove tmpfile if has been created by a previous side_effect
    tmpfile = '/tmp/test_side_effect'
    try:
        os.remove(tmpfile)
    except OSError:
        pass

    # create .zip archive with a file to delete
    with zipfile.ZipFile('/tmp/test_side_effect.zip', 'w') as archive:
        archive.writestr('test_side_effect', 'content')

    from thefuck.rules.unzip import match, get_new_command, side_effect
    from thefuck.types import Command

    assert match(Command(''.format('unzip'), ''.format('unzip'))) == False
    assert match(Command(''.format('unzip -d /tmp'), ''.format('unzip -d /tmp'))) == False

# Generated at 2022-06-14 09:41:44.753501
# Unit test for function side_effect
def test_side_effect():
    import os
    import tempfile
    import shutil
    import zipfile
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)
    file_name = 'file'
    with open(file_name, 'w') as file:
        file.write('some content')
    with zipfile.ZipFile(file_name + '.zip', 'w') as zip:
        zip.write(file_name)
    with open(file_name + '_after', 'w') as file:
        file.write('some other content')
    assert os.path.isfile(file_name)
    assert os.path.isfile(file_name + '_after')

    class Command():
        def __init__(self, script):
            self.script = script


# Generated at 2022-06-14 09:41:57.187298
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command
    import tempfile
    import sys
    import os

    if sys.version_info.major == 2:
        tempfile.NamedTemporaryFile = tempfile._TemporaryFileWrapper #pylint: disable=protected-access
    with tempfile.NamedTemporaryFile() as tmp_file:
        with zipfile.ZipFile(tmp_file, 'w') as archive:
            f = tempfile.NamedTemporaryFile(delete=False)
            f.close()

# Generated at 2022-06-14 09:42:04.769722
# Unit test for function side_effect
def test_side_effect():
    old_cmd = shell.and_('unzip test.zip', 'echo $?')
    old_cmd.stdout = 0
    command = get_new_command(old_cmd)

    archive = zipfile.ZipFile('test.zip', 'w')
    try:
        archive.writestr('test_file', '')

        with archive:
            side_effect(old_cmd, command)
            assert os.path.exists('test_file')
    finally:
        os.remove('test.zip')

# Generated at 2022-06-14 09:42:11.017325
# Unit test for function match
def test_match():
    assert match(Command('unzip -q foo.zip', ''))
    assert not match(Command('unzip -q -d foo foo.zip', ''))
    assert not match(Command('unzip -q -d foo foo.tgz', ''))
    assert not match(Command('unzip -q -d foo', ''))



# Generated at 2022-06-14 09:42:12.645925
# Unit test for function match
def test_match():
    pass


# Generated at 2022-06-14 09:42:21.960368
# Unit test for function match
def test_match():
    # Define command for function match
    def centos_match(command):
        assert _zip_file(command) == './test.zip'
        return _is_bad_zip('./test.zip')

    # Create test.zip archive
    with zipfile.ZipFile('test.zip', 'w') as archive:
        archive.writestr('test.txt', 'test')
        archive.writestr('test_again.txt', 'test')

    def ubuntu_match(command):
        assert _zip_file(command) == u'./test.zip'
        return _is_bad_zip(u'./test.zip')

    # Test match function - unzip without -d option
    command = Command('unzip test.zip',
                      'test.txt  test.zip')
    assert match(command)


# Generated at 2022-06-14 09:42:32.715565
# Unit test for function match
def test_match():
    assert match(Command(script='unzip foo.zip', stderr='Hello World'))
    assert match(Command(script='unzip bar.zip', stderr='Hello World'))
    assert not match(Command(script='unzip foo.zip -d foo'))
    assert not match(Command(script='ls'))
    assert not match(Command(script='unzip foo.zip', stderr='...'))

# Generated at 2022-06-14 09:42:34.820299
# Unit test for function side_effect
def test_side_effect():
    script = 'unzip test'
    assert side_effect(script, False) == None


# Generated at 2022-06-14 09:42:46.797499
# Unit test for function side_effect
def test_side_effect():
    # Mocking a file in the current working directory
    with open('mock_file', 'w+') as f:
        f.write('mock text')
    side_effect('unzip -l mock_file.zip', 'unzip -l mock_file.zip')
    assert os.path.isfile('mock_file')
    os.remove('mock_file')

    zip_file = open('mock_file.zip', 'w+')
    # Mock folder
    os.mkdir('mock_dir')
    with zipfile.ZipFile('mock_file.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write('mock_file')

# Generated at 2022-06-14 09:42:54.029132
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command
    import subprocess

    # Try to make a directory
    subprocess.call('mkdir delete_me'.split(' '))

    # Try to make a file
    subprocess.call('touch delete_me/delete_me'.split(' '))

    # Try to make an empty zip file
    with zipfile.ZipFile('empty.zip', 'w') as myzip:
        myzip.close()

    # Try to make a zip file with a file in it
    with zipfile.ZipFile('with_file.zip', 'w') as myzip:
        myzip.write('empty.zip')

    # Try to make a zip file with a directory in it

# Generated at 2022-06-14 09:43:03.990937
# Unit test for function side_effect
def test_side_effect():
    archive_name = 'test_archive.zip'
    with zipfile.ZipFile(archive_name, 'w') as archive:
        archive.writestr('test.txt', 'hello world')
        with open('test_file_for_unzip', 'w') as test_file:
            test_file.write('test')

    old_cmd = Command(script='unzip ' + archive_name + ' -d /tmp',
                      stdout='')

    side_effect(old_cmd, None)

    assert not os.path.isfile('test_file_for_unzip')
    os.remove(archive_name)



# Generated at 2022-06-14 09:43:11.725585
# Unit test for function match
def test_match():
    # _is_bad_zip(file) returns False if file does not exist, so it is tested
    # in test_get_new_command
    assert _is_bad_zip('tests/test_unzip_list.txt')
    assert _is_bad_zip('tests/test_unzip_zip.zip')
    assert not _is_bad_zip('tests/test_unzip_real_zip.zip')

    assert match(Command('unzip test_unzip_list.txt', '', ''))
    assert not match(Command('unzip test_unzip_list.txt -d test_unzip', '', ''))
    assert match(Command('unzip test_unzip_list.txt -f', '', ''))
    assert match(Command('unzip test_unzip_list.txt -n', '', ''))

# Generated at 2022-06-14 09:43:20.317271
# Unit test for function match
def test_match():
    cmd = 'unzip a.zip'
    with open('../thefuck/tests/fixtures/1file.zip', 'rb') as onefile:
        with open('../thefuck/tests/fixtures/2files.zip', 'rb') as twofiles:
            assert match(cmd) == False
            with open('a.zip', 'wb') as f:
                f.write(onefile.read())
            assert match(cmd) == False
            with open('a.zip', 'wb') as f:
                f.write(twofiles.read())
            assert match(cmd) == True


# Unit tests for function get_new_command

# Generated at 2022-06-14 09:43:26.117764
# Unit test for function side_effect
def test_side_effect():
    script_path = os.path.join(os.path.dirname(__file__), '..', 'test_data')
    os.chdir(script_path)
    side_effect("unzip a.zip", get_new_command("unzip a.zip"))
    assert os.path.exists(os.path.join(script_path, "a"))

# Generated at 2022-06-14 09:43:38.825296
# Unit test for function side_effect
def test_side_effect():
    # Create a temporary directory
    test_dir = tempfile.mkdtemp()
    # Create a test-file in the temporary directory
    with open(os.path.join(test_dir,'test_unzip_file'), 'w') as test_file:
        test_file.write('')
    # Create a test-zip-file in the temporary directory
    with zipfile.ZipFile(os.path.join(test_dir,'test_unzip_file.zip'),
                         'w') as test_file_zip:
        test_file_zip.write(
            os.path.join(test_dir, 'test_unzip_file'), 'test_unzip_file')
    old_cmd = Command('unzip', 'unzip test_unzip_file.zip', '', '', test_dir)
    command = Command

# Generated at 2022-06-14 09:43:53.916801
# Unit test for function match
def test_match():
    assert match(Command(script = 'unzip -fq athena-dist.zip', \
                         stdout = 'unzip:  cannot find or open athena-dist.zip, athena-dist.zip.zip or athena-dist.zip.ZIP.', \
                         stderr = ''))
    assert not match(Command(script = 'unzip -d athena-dist.zip', \
                             stdout = '', \
                             stderr = ''))
    assert not match(Command(script = 'unzip -fq athena-dist', \
                             stdout = 'unzip:  cannot find or open athena-dist, athena-dist.zip or athena-dist.ZIP.', \
                             stderr = ''))


# Generated at 2022-06-14 09:44:13.976824
# Unit test for function match
def test_match():
    command = 'unzip test.zip'
    assert match(Command(command, '/bin/zsh')) is True
    assert _zip_file(Command(command, '/bin/zsh')) == 'test.zip'

    command = 'unzip -a test.zip'
    assert match(Command(command, '/bin/zsh')) is True
    assert _zip_file(Command(command, '/bin/zsh')) == 'test.zip'

    assert match(Command('unzip', '/bin/zsh')) is False
    assert match(Command('unzip -d test.zip', '/bin/zsh')) is False
    assert match(Command('unzip -d test.zip test2.zip', '/bin/zsh')) is False

    command = 'unzip test.zip test2.zip'
    assert match

# Generated at 2022-06-14 09:44:24.966986
# Unit test for function match
def test_match():
    assert match(Command('unzip test1.zip test1.java', None))
    assert match(Command('unzip test1.zip', None))
    assert match(Command('unzip -l test1.zip', None))
    assert match(Command('unzip test1.zip test1.java test2.java', None))
    assert not match(Command('unzip -d Test1 test1.zip', None))
    assert not match(Command('unzip -d Test1 test1.zip test1.java test2.java', None))
    assert not match(Command('unzip -l test1.zip test1.java test2.java', None))


# Generated at 2022-06-14 09:44:34.044349
# Unit test for function match
def test_match():
    # When the zip_file is not None (when it's a good zip file)
    command = type("Command", (object,), {
        'script_parts': ['unzip', 'a_file', 'a_file.zip'],
        'script': 'unzip a_file a_file.zip'
    })
    assert match(command)

    # When the zip_file is None (when it's a bad zip file)
    command = type("Command", (object,), {
        'script_parts': ['unzip'],
        'script': 'unzip'
    })
    assert not match(command)


# Generated at 2022-06-14 09:44:49.217747
# Unit test for function side_effect
def test_side_effect():
    test_file_name = 'test_thefuck.zip'
    with zipfile.ZipFile(test_file_name, 'w') as archive:
        archive.writestr('test', 'test')

    def shell_mock(cmd, *args, **kwargs):
        return cmd

    class CommandMock(object):
        def __init__(self, script_parts):
            self.script_parts = script_parts
            self.script = ' '.join(script_parts)

        def __str__(self):
            return self.script

    old_cmd = CommandMock(['unzip', 'test_thefuck.zip'])
    side_effect(old_cmd, CommandMock(['unzip', '-d', 'test_thefuck.zip']))

    assert os.path.isfile('test')



# Generated at 2022-06-14 09:45:03.073354
# Unit test for function side_effect
def test_side_effect():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import mkdir, getcwd
    from os.path import abspath, join

    def in_test_dir(func):
        def wrapper(arg):
            original = getcwd()
            os.chdir(test_dir)
            result = func(arg)
            os.chdir(original)
            return result
        return wrapper

    def create_files():
        @in_test_dir
        def create(name):
            with open(name, 'w') as f:
                f.write('test')

        create('foobar')
        create('foo/bar')
        create('bar')


# Generated at 2022-06-14 09:45:14.532769
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    from thefuck.conf.paths import TEST_ROOT
    from shutil import copytree
    from contextlib import contextmanager
    from os import chdir, getcwd
    from os.path import join, exists

    @contextmanager
    def current_dir(path):
        """A context manager which changes the current directory"""
        old_dir = getcwd()
        try:
            chdir(path)
            yield
        finally:
            chdir(old_dir)

    def create_test_files():
        files = (
            'file1',
            'file2',
            'file3',
            'file4'
        )
        for f in files:
            with open(f, 'a'):
                pass


# Generated at 2022-06-14 09:45:25.292418
# Unit test for function match
def test_match():
    unzip_command = 'unzip foo.zip'
    assert not match(unzip_command)
    unzip_command = 'unzip foo.zip -d foo/'
    assert not match(unzip_command)
    unzip_command = 'unzip foo.zip foo/'
    assert not match(unzip_command)
    unzip_command = 'unzip -d foo/ bar.zip'
    assert not match(unzip_command)
    unzip_command = 'unzip bar.zip'
    assert not match(unzip_command)
    unzip_command = 'unzip bar.zip bar/'
    assert not match(unzip_command)

    unzip_command = 'unzip foo.zip -d foo/'
    assert not match(unzip_command)


# Generated at 2022-06-14 09:45:37.403487
# Unit test for function side_effect
def test_side_effect():
    cmd = shell.And(
        'unzip abcd.zip',
        u'unzip -d {}'.format(shell.quote('abcd')))
    side_effect(cmd, 'unzip -d abcd')
    zip_file = zipfile.ZipFile('abcd.zip')
    # Extract the zip file
    zip_file.extractall()
    # Assert that the directory and files are created
    assert os.path.isdir('abcd')
    assert os.path.isfile('abcd/a')
    assert os.path.isfile('abcd/b')
    assert os.path.isfile('abcd/c')
    assert os.path.isfile('abcd/d')
    # Remove the directory
    shutil.rmtree('abcd')

# Generated at 2022-06-14 09:45:43.774824
# Unit test for function side_effect
def test_side_effect():
    dir_name = os.path.join(os.path.curdir, 'test')
    file_name = 'test.zip'
    file_list = ['test.txt', 'test', os.path.join(os.getcwd(), 'test.txt')]


# Generated at 2022-06-14 09:45:55.787617
# Unit test for function side_effect
def test_side_effect():
    import tempfile, os
    with tempfile.TemporaryDirectory() as temp_dir:
        test_files = ['foo/bar.txt', 'bin/baz', 'bin/baz/test.txt']
        with zipfile.ZipFile(os.path.join(temp_dir, 'test.zip'), 'w') as z:
            for file in test_files:
                z.write(os.path.join(temp_dir, file), file)

        # the current directory is temp_dir
        old_cmd = Command('unzip test.zip', temp_dir)
        command = get_new_command(old_cmd)
        assert side_effect(old_cmd, command) == None
        # dir foo should not have been removed

# Generated at 2022-06-14 09:46:20.195571
# Unit test for function match
def test_match():
    assert match(Command('unzip test'))
    assert match(Command('unzip test.zip'))
    assert match(Command('unzip -e test.zip'))
    assert not match(Command('unzip test.zip -d tes'))
    assert not match(Command('unzip test.zip -e tes'))
    assert not match(Command('unzip test.zip -d test/'))
    assert not match(Command('unzip test.zip *.jpg'))



# Generated at 2022-06-14 09:46:27.757071
# Unit test for function match
def test_match():
    command = Command('unzip some.zip')
    assert match(command)
    command = Command('unzip -j some.zip')
    assert match(command)
    command = Command('unzip -o some.zip')
    assert match(command)
    command = Command('unzip -d some.zip')
    assert not match(command)
    command = Command('unzip -d some_dir some.zip')
    assert match(command)
    command = Command('unzip -q some')
    assert match(command)
    command = Command('unzip some_dir.zip')
    assert not match(command)


# Generated at 2022-06-14 09:46:42.128330
# Unit test for function match
def test_match():
    assert(match(Command('unzip this.zip', '', '')))
    assert(match(Command('unzip -l this.zip', '', '')))
    assert(match(Command('unzip -ll this.zip', '', '')))
    assert(match(Command('unzip this.zip test1.txt', '', '')))
    assert(match(Command('unzip this.zip test1.txt test2.txt', '', '')))
    assert(match(Command('unzip this.zip test1.txt test2.txt test3.txt', '', '')))
    assert(match(Command('unzip this.zip test1.txt test2.txt test3.txt -x test4.txt', '', '')))

# Generated at 2022-06-14 09:46:50.361529
# Unit test for function match
def test_match():
    from tests.utils import Command

    assert match(Command('unzip zip.zip', stderr='error'))
    assert not match(Command('unzip zip.zip', stderr='replace '))
    assert not match(Command('unzip zip.zip', stderr='replace existing'))
    assert not match(Command('unzip zip.zip', stderr='replace file'))
    assert not match(Command('unzip zip.zip', stderr='replace file '))

    assert match(Command('unzip zip.zip file', stderr='error'))
    assert not match(Command('unzip zip.zip file', stderr='replace '))
    assert not match(Command('unzip zip.zip file', stderr='replace existing'))

# Generated at 2022-06-14 09:47:05.622793
# Unit test for function side_effect
def test_side_effect():
    from . import uzip_output as unzip_output
    from . import ls_output as ls_output
    from . import lss_output as lss_output
    from . import touch_output as touch_output
    from . import mkdir_output as mkdir_output
    from thefuck.shells import shell
    from thefuck.shells.posix import Posix
    from thefuck.shells.bash import Bash
    import os
    import sys
    import zipfile

    # Create some temporary files and directories
    os.system('touch {0}/{1} {0}/{2} {0}/{3}/{1} > /dev/null 2>&1'.format(
        os.getcwd(), 'file_a', 'file_b', 'dir_a'))

    # Create a directory and file

# Generated at 2022-06-14 09:47:18.509452
# Unit test for function side_effect
def test_side_effect():
    old_cmd = Command(u"unzip file.zip /usr/tmp/")
    command = get_new_command(old_cmd)
    side_effect(old_cmd, command)
    # Check that the file.zip file has been removed
    assert not os.path.isfile("file.zip")
    # Check that the /usr/tmp/ directory doesn't exist anymore
    assert not os.path.isdir("/usr/tmp/")
    # Check that the /tmp/test_file file has been removed
    path = os.path.join(os.getcwd(), "test_file")
    with open(path, "w"):
        pass
    old_cmd = Command(u"unzip file.zip /tmp/test_file")
    command = get_new_command(old_cmd)
    side_effect

# Generated at 2022-06-14 09:47:31.264550
# Unit test for function side_effect
def test_side_effect():
    # test case 1
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))
    file1 = "./README.md"
    file2 = "./LICENSE"
    current_dir = os.getcwd()
    with open(file1, 'w') as f:
        f.write(file1)
    with open(file2, 'w') as f:
        f.write(file2)
    assert file1 in os.listdir(current_dir)
    assert file2 in os.listdir(current_dir)
    old_cmd = Command('unzip ./test_zip.zip', 'test_zip.zip')
    side_effect(old_cmd, None)
    assert file1 not in os.listdir(current_dir)

# Generated at 2022-06-14 09:47:44.049125
# Unit test for function match
def test_match():
    # test regular unzip
    command = 'unzip test.zip'
    assert match(Command(script=command, stderr='')) == True
    assert match(Command(script=command, stderr='unzip:  cannot find or open '
                                                'test.zip, test.zip.zip or '
                                                'test.zip.ZIP.')) == False

    # test unzip with -d
    command = 'unzip -d /path/to/extract/test.zip'
    assert match(Command(script=command, stderr='')) == False
    assert match(Command(script=command, stderr='unzip:  cannot find or open '
                                                'test.zip, test.zip.zip or '
                                                'test.zip.ZIP.')) == False

    # test

# Generated at 2022-06-14 09:47:48.483319
# Unit test for function match
def test_match():
    assert(match(type('Command', (object,), {'script_parts': [u'unzip', 'foo.zip']})) == True)
    assert(match(type('Command', (object,), {'script_parts': [u'unzip', 'foo', '-d', 'bar']})) == False)


# Generated at 2022-06-14 09:47:57.198825
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command

    command = Command('unzip test_files.zip', '', 0)
    side_effect(command, u'unzip -d {}'.format(shell.quote(u'test_files')))

    expected_files = [u'test_files/Φύλλο1 - Κεφάλαιο1.txt',
                      u'test_files/Лист1 - Глава1.txt',
                      u'test_files/List1 - Chapter1.txt']

    assert all([os.path.isfile(f) for f in expected_files])

    # Removing test files
    for f in expected_files:
        os.remove(f)
    os.rmdir(u'test_files')

# Generated at 2022-06-14 09:48:37.240915
# Unit test for function side_effect
def test_side_effect():
    test_dir = os.path.dirname(__file__)
    path_to_test_data = os.path.join(test_dir, 'test_data/zip_test_file')
    assert os.path.isdir(path_to_test_data) is True

    path_to_test_file = os.path.join(path_to_test_data, 'test_zip_file.zip')
    assert os.path.isfile(path_to_test_file) is True

    path_to_test_contents = os.path.join(path_to_test_data, 'test_contents')

    os.chdir(path_to_test_contents)
    list_contents = os.listdir(path_to_test_contents)

# Generated at 2022-06-14 09:48:47.639326
# Unit test for function side_effect
def test_side_effect():
    if os.path.exists("example"):
        os.remove("example")
    if os.path.exists("example.zip"):
        os.remove("example.zip")
    os.mkdir("example")
    with open("example/example.txt", 'w') as f:
        f.write("example file")
    with zipfile.ZipFile("example.zip", 'w') as archive:
        archive.write("example/example.txt", "example.txt")
    assert side_effect(None, None) is None
    assert os.path.isfile("example.txt")

# Generated at 2022-06-14 09:48:57.249936
# Unit test for function side_effect
def test_side_effect():
    from fnmatch import fnmatch
    from thefuck.types import Command
    
    # Create mock directory tree
    # 
    # root
    # ├── bar
    # │   └── foo.txt
    # ├── baz
    # ├── foo.txt
    # ├── level2
    # │   ├── bar
    # │   └── foo.txt
    # └── root.txt
    root = tempfile.mkdtemp()
    
    bar = os.path.join(root, 'bar')
    os.makedirs(bar)
    with open(os.path.join(bar, 'foo.txt'), 'w'):
        pass
    
    os.makedirs(os.path.join(root, 'baz'))
    

# Generated at 2022-06-14 09:49:05.928803
# Unit test for function match
def test_match():
    assert _zip_file(shell.and_('unzip abc.zip', 'echo "A zip file is bad"')) == 'abc.zip'
    assert match(shell.and_('unzip abc.zip', 'echo "A zip file is bad"')) is True
    assert match(shell.and_('unzip -d abc.zip', "echo 'oh no'")) is False  # noqa
    assert match(shell.and_('unzip abc.zip -d def', "echo 'oh no'")) is False  # noqa


# Generated at 2022-06-14 09:49:08.772022
# Unit test for function side_effect
def test_side_effect():
    side_effect(command_from_arguments('unzip file.zip'), command_from_arguments('unzip -d file file.zip'))

# Generated at 2022-06-14 09:49:16.189432
# Unit test for function match
def test_match():
    assert not match(u'unzip /home/daj/venv/python3/lib/python3.6/site-packages/django_extensions-2.1.5-py3.6.egg/django_extensions/management/__init__.py')
    assert match(u'unzip /home/daj/code/github.com/m1guelpf/ultrabook/tmp/test.zip')


# Generated at 2022-06-14 09:49:27.714987
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import os
    import shutil

    test_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(os.path.join(test_dir, 'test_zip.zip'), 'w') as archive:
        archive.write(__file__, os.path.basename(__file__))

    old_cwd = os.getcwd()
    os.chdir(test_dir)


# Generated at 2022-06-14 09:49:41.146770
# Unit test for function side_effect
def test_side_effect():
    with open('test.txt', 'w') as f:
        f.write('test content')
    with open('test2.txt', 'w') as f:
        f.write('test2 content')


# Generated at 2022-06-14 09:49:48.265273
# Unit test for function match
def test_match():
    from thefuck.rules.unzip_with_dest import match
    assert match(Command(script='unzip test_zip.zip test_file.txt',
                         stderr='test_file.txt:  bad extra-field length (local header)',
                         stdout='test_file.txt'))
    assert match(Command(script='unzip test_zip.zip test_file.txt',
                         stderr='test_file.txt:  bad zipfile offset (local header):  0',
                         stdout='test_file.txt'))
    assert match(Command(script='unzip test_zip.zip test_file.txt',
                         stderr='test_file.txt:  not a valid zipfile',
                         stdout='test_file.txt'))

# Generated at 2022-06-14 09:49:58.036868
# Unit test for function match
def test_match():
    assert match(Command('unzip a.zip', None)) is True
    assert match(Command('unzip -x', None)) is False
    assert match(Command('unzip abc', None)) is True
    assert match(Command('unzip -l', None)) is False
    assert match(Command('unzip -d', None)) is False
    assert match(Command('unzip a.zip', None)) is True
    assert match(Command('unzip a.zip', None)) is True
    assert match(Command('unzip a.zip', None)) is True
    assert match(Command('unzip a.zip', None)) is True
    assert match(Command('unzip a.zip', None)) is True
