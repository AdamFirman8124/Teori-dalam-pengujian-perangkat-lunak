

# Generated at 2022-06-14 09:41:10.754485
# Unit test for function side_effect
def test_side_effect():
    from shutil import rmtree
    from tempfile import mkdtemp
    from unittest import TestCase

    from thefuck.shells import get_all_executables

    rmtree(tmp_directory)
    tmp_directory = mkdtemp()
    os.chdir(tmp_directory)

    # Create temp directory and add in it file of different types
    # to test all cases in side_effect function
    tmp_directory_1 = mkdtemp()
    with open(os.path.join(tmp_directory_1, 'filename.txt'), 'w') as f:
        f.write('content')

    tmp_directory_2 = mkdtemp()
    with open(os.path.join(tmp_directory_2, 'file.txt'), 'w') as f:
        f.write('content')

    # Arch

# Generated at 2022-06-14 09:41:18.982662
# Unit test for function side_effect
def test_side_effect():
    from thefuck.tests.utils import Command

    # Uncomment the next line to verify the test by hand.
    # zip_file = 'tests/resources/unzip_test.zip'
    zip_file = '/tmp/unzip_test.zip'
    old_cmd = Command('unzip ' + zip_file)
    command = get_new_command(old_cmd)
    side_effect(old_cmd, command)
    os.remove(zip_file)
    os.remove(zip_file[:-4])

# Generated at 2022-06-14 09:41:27.087204
# Unit test for function side_effect
def test_side_effect():
    # Create a temporary directory for testing purposes
    pwd = os.getcwd()
    dir_name = tempfile.mkdtemp()

# Generated at 2022-06-14 09:41:34.241575
# Unit test for function side_effect
def test_side_effect():
    zip_file = 'test.zip'
    file1 = 'test1.txt'
    file2 = 'test2.txt'
    file3 = '/test/test.txt'

    # Create zip file
    archive = zipfile.ZipFile(zip_file, mode='w')
    archive.writestr(file1, 'test')
    archive.writestr(file3, 'test')
    archive.writestr(file2, 'test')

    # Test
    f = open(file1, 'w')
    f.close()
    f = open(file2, 'w')
    f.close()
    f = open(file3, 'w')
    f.close()
    assert os.path.exists(file1)
    assert os.path.exists(file2)

# Generated at 2022-06-14 09:41:41.595161
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command

    old_cmd = Command('unzip zlib-1.2.8.zip', u'', u'/usr/bin/unzip zlib-1.2.8.zip')
    side_effect(old_cmd, u'/usr/bin/unzip zlib-1.2.8.zip')

# Generated at 2022-06-14 09:41:49.819174
# Unit test for function match
def test_match():
    assert not match(Command('ls'))
    assert not match(Command('unzip -d file.zip'))
    assert not match(Command('unzip file.zip'))
    assert not match(Command('unzip file.zip another_file.zip'))
    assert not match(Command('unzip file.zip another_file.zip -x file.txt'))

    assert match(Command('unzip file.zip -x file.txt'))
    assert match(Command('unzip -l file.zip'))
    assert match(Command('unzip -h'))

# Generated at 2022-06-14 09:42:00.757017
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    tempdir = tempfile.mkdtemp()
    file_name = os.path.join(tempdir, 'file.txt')

    with open(file_name, 'w') as file:
        file.write('foo')

    with tempfile.NamedTemporaryFile() as archive:
        with zipfile.ZipFile(file=archive, mode='w') as zip_file:
            zip_file.write(file_name)

    # move archive file outside of temp dir to make sure it isn't deleted
    # by the test framework
    archive_name = archive.name
    archive.close()
    shutil.move(archive_name, '/tmp')

    os.chdir(tempdir)
    side_effect(None, 'unzip {}'.format(archive_name))

# Generated at 2022-06-14 09:42:08.855741
# Unit test for function side_effect
def test_side_effect():
    # create a dummy zip file in a temp directory
    temp_dir = tempfile.mkdtemp()
    temp_zipfile = os.path.join(temp_dir, 'test.zip')
    with open(temp_zipfile, 'w') as file:
        file.write("Test file to be extracted")

    with zipfile.ZipFile(temp_zipfile, 'w') as archive:
        archive.write(temp_zipfile)

    # script is a copy of command in match()
    script = 'unzip test.zip'
    cmd = Command(script, 'man unzip', '')

    # remove test.zip
    os.remove(temp_zipfile)

    # check if test.zip is indeed deleted
    assert not os.path.exists(temp_zipfile)

    # run the side_effect function
   

# Generated at 2022-06-14 09:42:19.040383
# Unit test for function side_effect
def test_side_effect():
    # os.getcwd() will return '/' and this is not a good idea!
    # so we must put back to our current directory
    current_path = os.getcwd()
    path = '/tmp/unzip_test'
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)

    # creation of a temporary file
    with open('test_side_effect.txt', 'w') as file:
        file.write('test_side_effect')

    # creation of a temporary zipfile with the temporary file before
    zfile = zipfile.ZipFile('test_side_effect.zip', 'w')
    zfile.write('test_side_effect.txt')
    zfile.close()

    # unzip of the temporary zipfile
    os.system

# Generated at 2022-06-14 09:42:32.137805
# Unit test for function side_effect
def test_side_effect():
    fake_dir = os.path.dirname(__file__)

    # Create a test zip file
    with zipfile.ZipFile('test.zip', 'w') as test_zip:
        test_zip.write(os.path.join(fake_dir, 'samples/unzip_sample.txt'),
                       os.path.basename('unzip_sample.txt'))
        test_zip.write(os.path.join(fake_dir, 'samples/unzip_sample2.txt'),
                       os.path.basename('unzip_sample2.txt'))

    # Test unzip, overwrite=False
    with patch('os.getcwd', return_value=fake_dir):
        side_effect(Fake('unzip test.zip', ''), Fake('', ''))

    # Test`unzip, overwrite=

# Generated at 2022-06-14 09:42:51.460301
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil

    path = tempfile.mkdtemp()
    path_file = path + '/exit.sh'
    new_path_file = path + '/exit.sh.zip'
    archive = zipfile.ZipFile(new_path_file, 'w')
    archive.write(path_file)
    archive.close()
    open(path_file, 'a').close()
    with open(path_file, 'a') as f:
        f.write('echo The Fuck!')
    command = Command('cd ' + path + ' ; unzip ' + new_path_file)
    side_effect(command, command)
    assert open(path_file, 'r').read() == 'echo The Fuck!'
    os.remove(path_file)
    os.remove(new_path_file)

# Generated at 2022-06-14 09:43:04.369819
# Unit test for function match

# Generated at 2022-06-14 09:43:08.943748
# Unit test for function match
def test_match():
    assert not match(Command('unzip -d dir file.zip'))
    assert match(Command('unzip file.zip'))
    assert match(Command('unzip file.zip file'))
    assert not match(Command('unzip nonexistent.zip'))
    assert not match(Command('unzip nonexistent.zip nonexistent'))
    assert not match(Command('unzip nonexistent'))


# Generated at 2022-06-14 09:43:21.631466
# Unit test for function side_effect
def test_side_effect():
    fd, tmp_script = tempfile.mkstemp()
    tmp_script_filename = os.path.basename(tmp_script)
    os.close(fd)
    with open(tmp_script, 'w') as f:
        f.write('#!/bin/bash\ncat unzip.py')

    command = Command('unzip {}'.format(tmp_script_filename), '', '')
    fd, tmp_zip = tempfile.mkstemp(suffix='.zip')
    os.close(fd)
    with zipfile.ZipFile(tmp_zip, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write(tmp_script)

    side_effect(command, None)

    assert not os.path.exists(tmp_script)

# Generated at 2022-06-14 09:43:28.804956
# Unit test for function match
def test_match():
    assert match(Command('unzip test.zip', '', ''))
    assert match(Command('unzip test.zip -d testdir', '', ''))
    assert not match(Command('unzip -d testdir test.zip', '', ''))
    assert not match(Command('unzip -d testdir -a test2.zip', '', ''))
    assert not match(Command('unzip test.zip -a test2.zip', '', ''))


# Generated at 2022-06-14 09:43:39.339049
# Unit test for function match
def test_match():
    from thefuck.rules.unzip_to_current_file import _is_bad_zip

    # zip file with multiple files
    with open('test.zip', 'w'):
        with open('test1.txt', 'w'):
            pass
        with open('test2.txt', 'w'):
            pass

    assert _is_bad_zip('test.zip') is True

    # zip file with single file
    with open('test.zip', 'w'):
        with open('test.txt', 'w'):
            pass

    assert _is_bad_zip('test.zip') is False


# Unit tests for function get_new_command

# Generated at 2022-06-14 09:43:49.883746
# Unit test for function match
def test_match():
    # Test with a file with more than one file in it
    # Create a zipfile with two files in it
    zipf = zipfile.ZipFile('test.zip', 'w')
    zipf.write('test.txt', 'n')
    zipf.write('test.py', 'n')
    zipf.close()

    # Test it matches on unzip test.zip
    from thefuck.types import Command

    assert match(Command('unzip test.zip', ''))
    # Test it doesn't match on unzip -d test.zip
    assert not match(Command('unzip -d test.zip', ''))
    # Test it doesn't match on unzip test
    assert not match(Command('unzip test', ''))



# Generated at 2022-06-14 09:43:52.834909
# Unit test for function match
def test_match():
    assert not match(Command('unzip test.zip', '', ''))
    assert match(Command('unzip test.zip', '', ''))


# Generated at 2022-06-14 09:44:04.426464
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        open('file.txt', 'w').close()

        try:
            os.remove('file1.txt')
        except OSError:
            pass

        with tempfile.NamedTemporaryFile() as tmpfile:
            with zipfile.ZipFile(tmpfile.name, 'w') as archive:
                archive.write('file.txt')

            command = Command('unzip -d /tmp ' + shell.quote(tmpfile.name), '', '')

            def run(command):
                if command.script_parts[-1] == 'file.txt':
                    raise CommandNotFound('rm')
                elif command.script_parts[-1] == 'file1.txt':
                    raise CommandNot

# Generated at 2022-06-14 09:44:14.958486
# Unit test for function side_effect
def test_side_effect():
    if not os.path.exists('/tmp/delete_me'):
        os.makedirs('/tmp/delete_me')
    with open('/tmp/delete_me/delete_me.txt', 'w') as f:
        f.write('This file has to be deleted')

    zip_file_path = '/tmp/delete_me.zip'
    with zipfile.ZipFile(zip_file_path, 'w') as archive:
        archive.write('/tmp/delete_me/delete_me.txt')

    old_cmd = Command('unzip ' + zip_file_path, '',
            CommandOutput('', '', 1))
    side_effect(old_cmd, None)

    with open('/tmp/delete_me/delete_me.txt', 'r') as f:
        assert f.read

# Generated at 2022-06-14 09:44:34.003087
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    import zipfile

    zip_dir = tempfile.mkdtemp()
    zip_file = os.path.join(zip_dir, 'test.zip')
    extract_dir = tempfile.mkdtemp()

    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write(os.path.join(zip_dir, 'test_dir/file'))
        archive.write(os.path.join(zip_dir, 'test_dir'))
        archive.write(os.path.join(zip_dir, 'file'))
        archive.write(os.path.join(zip_dir, '../test_file'))


# Generated at 2022-06-14 09:44:49.219104
# Unit test for function side_effect
def test_side_effect():
    from thefuck.main import Command
    from thefuck.shells import Generic
    from shutil import rmtree
    from tempfile import mkdtemp, mkstemp

    # create a temporary directory and a dummy zip file
    test_dir = mkdtemp()
    _, zip_path = mkstemp(suffix='.zip', dir=test_dir)
    with zipfile.ZipFile(zip_path, 'w') as archive:
        archive.writestr('content', 'content')

    # side_effect should not do anything in this case
    old_cmd = Command('unzip {} -d'.format(zip_path), '', Generic)
    side_effect(old_cmd, old_cmd)

    # side_effect should be able to successfully delete content

# Generated at 2022-06-14 09:44:57.500825
# Unit test for function match
def test_match():
    assert match(Command('unzip a.zip', '', ''))
    assert match(Command('unzip a.zip', '', ''))
    assert match(Command('unzip a', '', ''))
    assert not match(Command('unzip a.zip', '', ''))
    assert not match(Command('unzip a', '', ''))
    assert not match(Command('unzip', '', ''))



# Generated at 2022-06-14 09:45:07.476134
# Unit test for function match
def test_match():
    os.system('touch file1.zip')
    os.system('touch file2.zip')
    os.system('touch file3.zip')
    os.system('touch file4.zip')
    os.system('touch file5')
    with zipfile.ZipFile('file1.zip', 'w') as archive:
        archive.write('file5')
    with zipfile.ZipFile('file2.zip', 'w') as archive:
        archive.write('file5')
        archive.write('file5')
    with zipfile.ZipFile('file3.zip', 'w') as archive:
        archive.write('file5')
        archive.write('file5')
        archive.write('file5')

# Generated at 2022-06-14 09:45:20.010568
# Unit test for function match
def test_match():
    script = u"unzip /usr/local/Cellar/python3/3.5.0/Frameworks/Python.framework/Versions/3.5/Resources/Python.app/Contents/Resources/English.lproj/Welcome.zip"
    assert match(Command(script, '')) == True

    script = u"unzip /usr/local/Cellar/python3/3.5.0/Frameworks/Python.framework/Versions/3.5/Resources/Python.app/Contents/Resources/English.lproj/Welcome.zip -d path/to/folder"
    assert match(Command(script, '')) == False

    script = u"unzip Welcome/Welcome.zip -d path/to/folder"
    assert match(Command(script, '')) == False


# Generated at 2022-06-14 09:45:28.417398
# Unit test for function side_effect
def test_side_effect():
    # Set up
    old_cmd = type('old_cmd', (object,), {'script_parts': ['foo', 'bar.zip']})()
    command = type('command', (object,), {'script': 'unzip bar.zip'})()
    os.makedirs('bar')
    with open('bar/asdf.py', 'w') as file:
        file.write('asdf')
    archive = zipfile.ZipFile('bar.zip', 'w')
    archive.write('bar/asdf.py')
    archive.close()

    # Execute
    side_effect(old_cmd, command)

    # Verify
    assert os.path.exists('bar.zip')
    assert os.path.exists('bar/asdf.py')

# Generated at 2022-06-14 09:45:36.212064
# Unit test for function side_effect
def test_side_effect():
    zip_file = 'test.zip'
    with zipfile.ZipFile(zip_file, 'w') as f:
        f.write('test.txt', 'test.txt')
        f.write('test.txt', '../test.txt')
    assert side_effect('''unzip {}'''.format(zip_file), None) is None
    assert not os.path.isfile('test.txt') and not os.path.isfile('../test.txt')
    os.remove(zip_file)

# Generated at 2022-06-14 09:45:43.406407
# Unit test for function match
def test_match():
    # Test if the txt file is not a zip file
    assert not match(Command("unzip text.txt", "", ""))

    # Test if the zip file is not a zip file
    assert not match(Command("unzip text.zip", "", ""))

    # Test if the zip file is not a zip file
    assert not match(Command("unzip test.zip", "", ""))

    # Test if the zip file is not a zip file
    assert not match(Command("unzip test1.zip", "", ""))

    # Test if the zip file is a zip file
    assert not match(Command("unzip text1.zip", "", ""))

    # Test with the flags
    assert not match(Command("unzip -l text1.zip", "", ""))

    # Test with the flags

# Generated at 2022-06-14 09:45:53.193216
# Unit test for function match
def test_match():
    assert match(Command(script='unzip -l /tmp/file.zip'))
    assert match(Command(script='unzip -l file.zip'))
    assert not match(Command(script='unzip -l /tmp/file.txt'))
    assert not match(Command(script='unzip -l /tmp/file'))
    assert not match(Command(script='unzip -d /tmp/file.zip'))
    assert not match(Command(script='unzip -l /tmp/file1.zip file2.zip'))



# Generated at 2022-06-14 09:46:01.393215
# Unit test for function match
def test_match():
    script = 'unzip code.zip'
    assert not match(script)
    script = 'unzip code -d .'
    assert not match(script)
    script = 'unzip subdir/code.zip'
    assert not match(script)
    script = 'unzip dir/subdir/code.zip'
    assert not match(script)
    script = 'unzip code.zip -d subdir'
    assert not match(script)
    script = 'unzip code.zip -d dir/subdir'
    assert not match(script)
    script = 'unzip subdir/code.zip -d .'
    assert not match(script)

    script = 'unzip code.zip'
    assert match(script)
    script = 'unzip code.zip -d dir'
    assert match(script)
    script

# Generated at 2022-06-14 09:46:27.096621
# Unit test for function side_effect
def test_side_effect():
    zip_file = "test_data/test.zip"
    with zipfile.ZipFile(zip_file, 'r') as archive:
        for file in archive.namelist():
            with open(file, "w") as f:
                f.write("test")
    old_cmd = Command("unzip test_data/test.zip",
                  "error:  test.zip:  must specify dir",
                  "")
    command = get_new_command(old_cmd)
    side_effect(old_cmd, command)
    with open("test.txt", "r") as f:
        assert(f.read() == "test")

# Generated at 2022-06-14 09:46:37.670605
# Unit test for function side_effect
def test_side_effect():
    old_cmd = Command('unzip file.zip', '')
    command = Command('unzip -d new_dir file.zip', '')

    with zipfile.ZipFile('file.zip', 'w') as glb:
        glb.writestr('file.txt', 'hello world')
        glb.writestr('file2.txt', 'hello world')

    side_effect(old_cmd, command)

    assert not os.path.exists('file.txt')
    assert not os.path.exists('file2.txt')

# Generated at 2022-06-14 09:46:48.911379
# Unit test for function side_effect
def test_side_effect():
    os.makedirs('/tmp/unzip-test/')

    with open('/tmp/unzip-test/test.txt', 'w+') as f:
        f.write('content')

    with open('/tmp/unzip-test/test.zip', 'w+') as f:
        z = zipfile.ZipFile(f, 'w')
        z.writestr('test.txt', 'new content')
        z.close()

    class Command:
        def __init__(self, script_part):
            self.script_part = script_part
        @property
        def script(self):
            return self.script_part

    side_effect(Command('unzip /tmp/unzip-test/test.zip'), None)
    

# Generated at 2022-06-14 09:47:00.658512
# Unit test for function side_effect
def test_side_effect():
    # build an example archive
    example_dir = tempfile.mkdtemp()
    example_file = open(os.path.join(example_dir, 'example_file'), 'w+')
    example_file.write('example file')
    example_file.close()
    archive = zipfile.ZipFile(os.path.join(example_dir, 'example.zip'), 'w')
    archive.write(os.path.join(example_dir, 'example_file'), 'example_file')
    archive.close()
    # call the side effect
    old_cmd = Command('unzip example.zip',
                      example_dir,
                      'example_file\n')
    command = Command('unzip example.zip -d example')
    side_effect(old_cmd, command)
    # test
    example_file = open

# Generated at 2022-06-14 09:47:12.898007
# Unit test for function match
def test_match():
    assert _is_bad_zip('test_files/hello.zip')
    assert not _is_bad_zip('test_files/helloworld.zip')
    assert _zip_file(Command(script='unzip test_files/hello.zip',
                             stderr='test_files/hello.zip:  not a valid zip file')) == 'test_files/hello.zip'
    assert _zip_file(Command(script='unzip test_files/hello.zip invalid.txt',
                             stderr='test_files/hello.zip:  not a valid zip file')) == 'test_files/hello.zip'

# Generated at 2022-06-14 09:47:14.556818
# Unit test for function side_effect
def test_side_effect():
    result = side_effect(None, None)
    assert result is None

# Generated at 2022-06-14 09:47:25.644702
# Unit test for function side_effect
def test_side_effect():
    dir = "test_dir"

# Generated at 2022-06-14 09:47:31.142458
# Unit test for function match
def test_match():
    ret = match(Command(script='unzip -l /path/to/archive.zip', stderr=''))
    assert ret == False

    ret = match(Command(script='unzip /path/to/archive.zip', stderr=''))
    assert ret == False

    ret = match(Command(script='unzip /path/to/archive', stderr=''))
    assert ret == False



# Generated at 2022-06-14 09:47:38.371747
# Unit test for function match
def test_match():
    zip_file = './tests/samples/sample_text.zip'
    assert _is_bad_zip(zip_file)
    assert match(Command('unzip sample_text.zip', ''))
    assert match(Command('unzip sample_text.zip file.txt', ''))
    assert not match(Command('unzip -d folder file.zip', ''))
    assert not match(Command('unzip -d folder file.zip file.txt', ''))

# Generated at 2022-06-14 09:47:49.167454
# Unit test for function side_effect
def test_side_effect():
    # Create a file and a directory. We cannot create a zip file with a
    # directory, so we archive a file in a directory.
    import tempfile
    from shutil import rmtree

    name = '/tmp/foo'
    d_name = '/tmp/foo_dir'
    d_name2 = '/tmp/foo_dir2'

    with open(name, 'w') as f:
        f.write('foo\n')
    os.mkdir(d_name)
    archive = zipfile.ZipFile('/tmp/foo.zip', 'w')
    archive.write('/tmp/foo', 'foo')
    archive.close()

    # Test if the file foo is created
    os.system('unzip /tmp/foo.zip')
    assert os.path.exists(name)

    # Test if the

# Generated at 2022-06-14 09:48:12.441525
# Unit test for function match
def test_match():
    assert _is_bad_zip('1.zip') == True
    assert _is_bad_zip('2.zip') == False
    assert _is_bad_zip('3.zip') == False
    assert match(Command('unzip 1.zip', '')) == True
    assert match(Command('unzip 2.zip', '')) == False
    assert match(Command('unzip 3.zip', '')) == False
    assert match(Command('unzip -d dir 1.zip', '')) == False


# Generated at 2022-06-14 09:48:20.943705
# Unit test for function match
def test_match():
    # files to unzip from the archive
    assert _zip_file(shell.from_shell('unzip test.zip')) == 'test.zip'
    assert _zip_file(shell.from_shell('unzip test')) == 'test.zip'
    assert _zip_file(shell.from_shell('unzip my/test')) == 'my/test.zip'
    assert _zip_file(shell.from_shell('unzip my/test.zip')) == 'my/test.zip'
    assert _zip_file(shell.from_shell('unzip my/test.zip this_file')) == 'my/test.zip'
    # no file to unzip, only flags
    assert _zip_file(shell.from_shell('unzip -l test.zip')) is None

# Generated at 2022-06-14 09:48:31.380701
# Unit test for function side_effect
def test_side_effect():
    if not os.path.exists('test'):
        os.mkdir('test')
    with open('test/file.txt', 'w') as f:
        f.write('foo')
    with zipfile.ZipFile('test.zip', 'w') as z:
        z.write('test/file.txt')
    os.chdir('test')
    side_effect(None, None)
    assert os.path.exists('file.txt')
    os.remove('file.txt')
    assert not os.path.exists('file.txt')
    os.removedirs('../test')

# Generated at 2022-06-14 09:48:39.382702
# Unit test for function side_effect
def test_side_effect():
    import thefuck.shells.bash as bash
    import shutil
    cwd = os.getcwd()
    parent_folder = os.path.join(cwd, 'parent_folder')
    assert not os.path.isdir(parent_folder)
    assert not os.path.isdir(os.path.join(parent_folder, 'subfolder'))
    assert not os.path.isfile(os.path.join(parent_folder, 'subfolder', 'file'))
    assert not os.path.isfile(os.path.join(parent_folder, 'subfolder', 'another_file'))
    os.mkdir(parent_folder)
    os.mkdir(os.path.join(parent_folder, 'subfolder'))

# Generated at 2022-06-14 09:48:43.678347
# Unit test for function side_effect
def test_side_effect():
    temp_dir = tempfile.mkdtemp()
    with open(os.path.join(temp_dir, 'file.txt'), 'w') as f:
        f.write('Contents')

    with zipfile.ZipFile(os.path.join(temp_dir, 'file.zip'), 'w') as archive:
        archive.write(os.path.join(temp_dir, 'file.txt'), 'file.txt')

    command = Command(script='unzip file.zip', stderr='')
    side_effect(command, command)
    assert not os.access(os.path.join(temp_dir, 'file.txt'), os.F_OK)

    os.remove(os.path.join(temp_dir, 'file.zip'))
    shutil.rmtree(temp_dir)

# Generated at 2022-06-14 09:48:53.995519
# Unit test for function side_effect
def test_side_effect():
    """
    Test side effect of function
    """
    # Create a temporary folder to work in and empty files to test with
    with TemporaryDirectory() as dir_name:
        cwd = os.getcwd()
        os.chdir(dir_name)
        open('file1.txt', 'w').close()
        open('file2.txt', 'w').close()
        open('file3.txt', 'w').close()

        # Create zip archive
        zip = zipfile.ZipFile('testzip.zip', 'w')
        zip.write('file1.txt', 'file1.txt')
        zip.write('file2.txt', 'file2.txt')
        zip.write('file3.txt', 'file3.txt')

# Generated at 2022-06-14 09:49:00.732647
# Unit test for function match
def test_match():
    assert match(Command('unzip foo.zip'))
    assert match(Command('unzip bar/foo.zip'))

    assert not match(Command('zip -r foo.zip foo'))
    assert not match(Command('zip foo.zip foo'))
    assert not match(Command('unzip -r foo.zip'))
    assert not match(Command('unzip -d foo.zip foo'))

# Generated at 2022-06-14 09:49:09.631219
# Unit test for function side_effect
def test_side_effect():
    os.chdir("test_files/test_side_effect")
    subprocess.check_call("touch file1 file2 file3".split())
    subprocess.check_call("mkdir dir1 dir2 dir3".split())
    subprocess.check_call("zip -r files.zip file1 file2 file3 dir1 dir2 dir3".split())

    old_cmd = MagicMock()
    old_cmd.script = "unzip files.zip -d /tmp"
    old_cmd.script_parts = ["unzip", "file1", "file2", "file3"]

    command = MagicMock()
    command.script = "unzip files.zip -d /tmp"
    command.script_parts = ["unzip", "file1", "file2", "file3"]


# Generated at 2022-06-14 09:49:20.598049
# Unit test for function match
def test_match():
    def is_matched(script, output=None, **kwargs):
        """Helper for unit test to simplify the code."""
        command = type('Command', (object,),
                       {'script': script, 'stdout': output, 'stderr': None})
        return match(command)

    archives = [
        'some.zip',
    ]

    for f in archives:
        assert is_matched('unzip {}'.format(f))

    assert not is_matched('unzip some.zip -d some/directory')
    assert not is_matched('unzip')
    assert not is_matched('unzip some.zip some/directory')



# Generated at 2022-06-14 09:49:31.311025
# Unit test for function match
def test_match():
    assert match(Command('unzip hello.zip', None, None))
    assert match(Command('unzip -d hello.zip', None, None))
    assert match(Command('unzip hello-world.zip', None, None))
    assert match(Command('unzip -d hello-world.zip', None, None))
    assert not match(Command('unzip -d hello.zip hello-world.zip', None, None))
    assert not match(Command('unzip hello.zip hello-world.zip', None, None))



# Generated at 2022-06-14 09:50:06.095000
# Unit test for function match
def test_match():
    from thefuck.rules.unzip_inplace import match
    assert not match(Command(script='unzip archive.zip file -d dest_dir',
                             stdout=''))
    assert match(Command(script='unzip archive.zip file', stdout=''))
    assert match(Command(script='unzip archive file', stdout=''))

# Generated at 2022-06-14 09:50:15.392731
# Unit test for function side_effect
def test_side_effect():

    # We can create a fake command to test side_effect function
    class FakeCommand():
        # Since we are only testing the side effect,
        # we can create fake return script
        def __init__(self, script):
            self.script = script

        def __unicode__(self):
            return self.script
    # Creating a test folder
    os.mkdir("test_side_effect_folder")
    # Creating a fake zip file with a test file inside
    with zipfile.ZipFile("test_side_effect_file.zip", 'w') as newzip:
        newzip.write("test_side_effect_folder")

    # Now, we test side_effect by creating a fake command
    fake_command_script = 'unzip test_side_effect_file.zip'

# Generated at 2022-06-14 09:50:26.958605
# Unit test for function match
def test_match():
    assert match(Command('unzip archive.zip', '', None))
    assert match(Command('unzip -d dir_name archive.zip', '', None))
    assert not match(Command('unzip -d archive.zip', '', None))
    assert not match(Command('unzip archive.zip dir_name', '', None))
    assert not match(Command('zip archive.zip', '', None))
    assert not match(Command('unzip archive', '', None))
    assert not match(Command('unzip archive.json', '', None))
    assert not match(Command('unzip archive.zip archive.json', '', None))

# Generated at 2022-06-14 09:50:33.802060
# Unit test for function side_effect
def test_side_effect():
    # Test for function side_effect()
    # Test for available file for input
    temp_file = open("./test_side_effect.txt", 'w')
    temp_file.write("Write something")
    temp_file.close()

    side_effect_test_command = "unzip ./test_side_effect.txt"
    side_effect(side_effect_test_command, side_effect_test_command)

    assert os.path.isfile("./test_side_effect.txt") == False

    side_effect_test_command_2 = "unzip ./test_side_effect_2.txt"
    side_effect(side_effect_test_command_2, side_effect_test_command_2)

    # Test for unavailable file for input

# Generated at 2022-06-14 09:50:46.326994
# Unit test for function side_effect
def test_side_effect():
    # create directory structure
    os.mkdir('./tmp/')
    os.mkdir('./tmp/a/')
    os.mkdir('./tmp/b/')
    os.mkdir('./tmp/a/c/')
    os.mkdir('./tmp/a/d/')
    os.mkdir('./tmp/a/d/e/')

    # create files
    with open('./tmp/a/file.txt', 'w') as f:
        pass
    with open('./tmp/a/d/e/file.txt', 'w') as f:
        pass
    with open('./tmp/a/d/notfile.txt', 'w') as f:
        pass

# Generated at 2022-06-14 09:50:52.823671
# Unit test for function side_effect
def test_side_effect():
    import shutil
    import thefuck.types
    import tempfile
    import thefuck.shells

    temp_dir = tempfile.mkdtemp(prefix='thefuck-')
    test_file_name = os.path.join(temp_dir, 'test_side_effect.txt')
    zip_test_file_name = os.path.join(temp_dir, 'test_side_effect.zip')

    with open(test_file_name, 'w') as f:
        f.write('test')

    with zipfile.ZipFile(zip_test_file_name, 'w') as f:
        f.write(test_file_name)

    assert os.path.exists(test_file_name)
    assert os.path.exists(zip_test_file_name)

    # Test if file