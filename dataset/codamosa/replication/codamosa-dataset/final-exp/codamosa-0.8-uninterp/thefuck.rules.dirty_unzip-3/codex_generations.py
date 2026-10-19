

# Generated at 2022-06-14 09:41:03.320212
# Unit test for function match
def test_match():
    from tests.utils import Command

    # unzip filename.zip
    assert match(Command(script='unzip filename.zip')) is False
    assert match(Command(script='unzip filename.zip', stdout='stderr')) is False

    # unzip -d directory filename.zip
    assert match(Command(script='unzip -d directory filename.zip')) is False
    assert match(Command(script='unzip -d directory filename.zip', stdout='stderr')) is False

    # unzip filename
    assert match(Command(script='unzip filename')) is False
    assert match(Command(script='unzip filename', stdout='stderr')) is False

    # unzip -d directory filename
    assert match(Command(script='unzip -d directory filename')) is False

# Generated at 2022-06-14 09:41:06.663447
# Unit test for function match
def test_match():
    assert match(Command('unzip foo.zip', '', '', 1, 2)) is True
    assert match(Command('unzip -d foo foo.zip', '', '', 1, 2)) is False

# Generated at 2022-06-14 09:41:14.887249
# Unit test for function side_effect
def test_side_effect():
    with tempfile.NamedTemporaryFile() as archive:
        with tempfile.NamedTemporaryFile() as file1:
            with tempfile.NamedTemporaryFile() as file2:
                archive_file = zipfile.ZipFile(archive.name, 'w')
                archive_file.write(file1.name)
                archive_file.write(file2.name)
                archive_file.close()

                side_effect(Command(u'unzip {}'.format(archive.name)), None)

                # Check if the files are not in the system
                assert not os.path.isfile(file1.name)
                assert not os.path.isfile(file2.name)

# Generated at 2022-06-14 09:41:23.047331
# Unit test for function match
def test_match():
    # test for different commands
    assert match(Command('unzip test.zip', ''))
    assert not match(Command('unzip file.zip', ''))
    assert match(Command('unzip file.zip arg', ''))

    # test for different flags
    assert match(Command('unzip file.zip -l', ''))
    assert match(Command('unzip file.zip -d', ''))

    # test for different filenames
    assert match(Command('unzip test.zip', ''))
    assert match(Command('unzip test.zip file', ''))
    assert match(Command('unzip test.zip file.txt', ''))



# Generated at 2022-06-14 09:41:30.426769
# Unit test for function match
def test_match():
    # Test when command.script_parts equals ['unzip', 'file.zip']
    command = 'unzip file.zip'
    assert match(shell.from_shell(command)) == False

    # Test when command.script_parts equals ['unzip', '-q', 'file.zip']
    command = 'unzip -q file.zip'
    assert match(shell.from_shell(command)) == False

    # Test when command.script_parts equals ['unzip', '-d', 'dir1', 'file.zip']
    command = 'unzip -d dir1 file.zip'
    assert match(shell.from_shell(command)) == False

    # Test when command.script_parts equals ['unzip', 'file']
    command = 'unzip file'
    assert match(shell.from_shell(command)) == False

   

# Generated at 2022-06-14 09:41:46.388204
# Unit test for function side_effect
def test_side_effect():
    from tempfile import TemporaryDirectory
    from shutil import copyfile, rmtree, move

    class FakeCommand:

        def __init__(self, script):
            self.script = script
            self.script_parts = script.split()

    with TemporaryDirectory() as tmpdirname:
        for dirname in ['foo', 'bar', 'baz']:
            os.mkdir(os.path.join(tmpdirname, dirname))
            copyfile('/etc/hosts', os.path.join(tmpdirname, dirname, 'hosts'))

        zip_file = os.path.join(tmpdirname, 'test_zip.zip')

# Generated at 2022-06-14 09:41:55.630355
# Unit test for function match
def test_match():
    command1 = Command('unzip NLP_HW1.zip', '', 'unzip:  cannot find or open NLP_HW1.zip, NLP_HW1.zip.zip or NLP_HW1.zip.ZIP.')
    assert match(command1)
    command2 = Command('unzip NLP_HW1.zip', '', '')
    assert match(command2) is False
    command3 = Command('unzip -d NLP_HW1.zip', '', '')
    assert match(command3) is False


# Generated at 2022-06-14 09:42:06.453690
# Unit test for function match
def test_match():
    # Testing unzip command
    command = Command('unzip archive.zip')
    assert match(command)

    # Testing unzip command with a flag
    command = Command('unzip -j archive.zip')
    assert match(command)

    # Testing unzip command without file
    command = Command('unzip')
    assert not match(command)

    # Testing unzip command with a wrong flag
    command = Command('unzip -d archive.zip')
    assert not match(command)

    # Testing unzip command with another flag
    command = Command('unzip -Z archive.zip')
    assert match(command)

    # Testing unzip command with a flag and a wrong file
    command = Command('unzip -j archive')
    assert match(command)

    # Testing unzip command with a wrong flag and a wrong file
    command = Command

# Generated at 2022-06-14 09:42:18.051216
# Unit test for function side_effect
def test_side_effect():
    from shutil import copyfile
    copyfile('tests/data/unzip_test.txt', 'tests/data/unzip_test')
    try:
        os.mkdir('tests/data/unzip_test_folder')
    except OSError:
        pass
    try:
        f = open('tests/data/unzip_test_folder/unzip_test.txt', 'w')
        try:
            f.write("test")
        finally:
            f.close()

        copyfile('tests/data/unzip_test_folder/unzip_test.txt', 'tests/data/unzip_test_folder/unzip_test')
    finally:
        os.remove('tests/data/unzip_test_folder/unzip_test.txt')

# Generated at 2022-06-14 09:42:25.764877
# Unit test for function match
def test_match():
    # # test if zip file is bad
    #Bad zip
    assert _is_bad_zip("b.zip") == True

    # # test if zip file is good
    #Good zip
    assert _is_bad_zip("a.zip") == False

    # # test for existing of file
    #file does not exist
    assert _is_bad_zip("abc.zip") == False


# Generated at 2022-06-14 09:42:50.989941
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', '/bin/unzip')) == False
    assert match(Command('unzip file.zip new_file', '/bin/unzip')) == True
    assert match(Command('unzip file.zip new_file.zip', '/bin/unzip')) == False
    assert match(Command('unzip -d file.zip new_file', '/bin/unzip')) == False
    assert match(Command('unzip -d file.zip new_file', '/bin/unzip')) == False
    assert match(Command('unzip file.zip -d new_file', '/bin/unzip')) == False
    assert match(Command('unzip file.zip -d new_file.zip', '/bin/unzip')) == False


# Generated at 2022-06-14 09:42:55.443731
# Unit test for function match
def test_match():
    command = Command('unzip a.zip', '', None)
    assert match(command)
    command = Command('unzip a.zip', '', None)
    assert match(command)



# Generated at 2022-06-14 09:43:07.167437
# Unit test for function match
def test_match():
    assert not match(Command('unzip archive.zip'))
    assert not match(Command('unzip -l archive.zip'))
    assert match(Command('unzip archive.zip -o'))
    assert match(Command('unzip archive.zip -d /tmp'))
    assert not match(Command('unzip archive.jar'))
    assert not match(Command('unzip archive.zip hola.txt'))
    assert match(Command('unzip archive.zip -o hola.txt'))
    assert match(Command('unzip archive.zip -d /tmp hola.txt'))
    assert not match(Command('unzip archive.zip hola.txt -x hola.txt'))
    assert match(Command('unzip archive.zip -o hola.txt -x hola.txt'))

# Generated at 2022-06-14 09:43:19.140268
# Unit test for function match
def test_match():
    import pathlib
    import tempfile
    with tempfile.TemporaryDirectory() as dir:
        with open(pathlib.Path(dir, 'one.txt'), 'w') as f:
            f.write('one')
        with open(pathlib.Path(dir, 'two.txt'), 'w') as f:
            f.write('two')
        with zipfile.ZipFile(pathlib.Path(dir, 'two.zip'), 'w') as archive:
            archive.write(pathlib.Path(dir, 'one.txt'), 'one.txt')
            archive.write(pathlib.Path(dir, 'two.txt'), 'two.txt')

        assert match(u"unzip two.zip '*.txt'") == True
        assert match(u"unzip 'two.zip' '*.txt'") == True
       

# Generated at 2022-06-14 09:43:21.358836
# Unit test for function match
def test_match():
    assert match(Command('unzip text.zip', ''))
    assert match(Command('unzip -h', '')) is False

# Generated at 2022-06-14 09:43:30.177706
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', '', None))
    assert match(Command('unzip file.zip long/file.txt', '', None))
    assert match(Command('unzip file.zip -x long/file.txt', '', None))
    assert not match(Command('unzip', '', None))
    assert not match(Command('unzip -d directory/', '', None))
    assert not match(Command('unzip file.zip -d directory/', '', None))
    assert not match(Command('unzip file.zip -d directory/', '', None))


# Generated at 2022-06-14 09:43:33.621159
# Unit test for function match
def test_match():
    c = 'unzip foobar.zip'
    assert not match(shell.and_(c, 'command not found'))
    assert match(shell.and_(c))


# Generated at 2022-06-14 09:43:42.342588
# Unit test for function side_effect
def test_side_effect():
    directory = tempfile.mkdtemp()
    os.chdir(directory)
    file1 = os.path.join(directory, "file1.txt")
    file2 = os.path.join(directory, "file2.txt")
    with open(file1, "w") as f:
        f.write("1")
    with open(file2, "w") as f:
        f.write("2")
    with zipfile.ZipFile("file.zip", "w") as myzip:
        myzip.write(file1)
        myzip.write(file2)
    command = shell.and_('unzip', 'file.zip')
    side_effect(command, command)
    assert open(file1).read() == "1"
    assert open(file2).read() == "2"

# Generated at 2022-06-14 09:43:45.916437
# Unit test for function match
def test_match():
    assert not match(Command('unzip', ''))
    assert not match(Command('unzip', '-d my_dir'))
    assert not match(Command('unzip', 'my_file.zip'))
    assert not match(Command('unzip', 'my_file.zip my_file'))
    assert match(Command('unzip', 'my_file.zip my_file1 my_file2 my_file3'))


# Generated at 2022-06-14 09:43:57.159616
# Unit test for function side_effect
def test_side_effect():
    f = tempfile.NamedTemporaryFile()
    with zipfile.ZipFile(f.name, 'w') as archive:
        archive.writestr('foo.txt', 'foo contents')


# Generated at 2022-06-14 09:44:16.943815
# Unit test for function side_effect
def test_side_effect():
    files = ['a.py', 'b.txt', 'sub/c.md']
    try:
        for file in files:
            with open(file, 'w') as f:
                f.write('')

        command = shell.and_('unzip archive.zip', 'ls')
        old_cmd = command
        command = get_new_command(command)
        side_effect(old_cmd, command)
        for file in files:
            assert not os.path.exists(file)
    finally:
        for file in files:
            try:
                os.remove(file)
            except OSError:
                pass

# Generated at 2022-06-14 09:44:28.798083
# Unit test for function side_effect
def test_side_effect():
    # We will test if the side effect deletes the first file in the archive
    # and does not delete the second file
    file_to_be_deleted = 'file_with_password.txt'
    file_to_be_preserved = 'README'
    path = 'tests/unzip/test_side_effect'
    archive = 'tests/unzip/test_side_effect/test_side_effect.zip' 

    # We will save the contents of the files, so that we can restore them
    # after the side effect deletes them.
    file_to_be_deleted_content = open(path + '/' + file_to_be_deleted).read()
    file_to_be_preserved_content = open(path + '/' + file_to_be_preserved).read()

    # Check if

# Generated at 2022-06-14 09:44:45.724066
# Unit test for function side_effect
def test_side_effect():
    with zipfile.ZipFile('test_side_effect.zip', 'w') as zip_file:
        zip_file.writestr('foo.txt', 'foo')
        zip_file.writestr('bar/bar.txt', 'bar')
    import shutil

# Generated at 2022-06-14 09:44:49.437299
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', ''))
    assert not match(Command('unzip file.zip a', ''))
    assert not match(Command('unzip file.zip a b c -d test', ''))



# Generated at 2022-06-14 09:45:03.069476
# Unit test for function side_effect
def test_side_effect():
    from tempfile import TemporaryDirectory
    from thefuck.types import Command
    from thefuck.shells import shell
    with TemporaryDirectory() as tempdir:
        os.chdir(tempdir)
        shell.to_shell(Command('echo a; echo b', '', 'a\nb'))
        os.mkdir('a')
        with open('b', 'w') as _b:
            _b.write('b')

        # with os.popen('zip -0 a.zip a') as _:
        #     pass

        # subprocess.call('zip -0 a.zip a', shell=True)
        # subprocess.check_call(['zip', '-0', 'a.zip', 'a'])


# Generated at 2022-06-14 09:45:10.887467
# Unit test for function match
def test_match():
    assert _is_bad_zip('tests/fixtures/bad.zip')
    assert not _is_bad_zip('tests/fixtures/good.zip')

    assert match(Command('unzip bad.zip', '', '/var/www'))
    assert not match(Command('unzip good.zip', '', '/var/www'))
    assert not match(Command('unzip -d good.zip', '', '/var/www'))

# Generated at 2022-06-14 09:45:14.698069
# Unit test for function match
def test_match():
    command = "unzip abc.zip"
    assert match(shell.from_shell(command))
    command = "unzip abc.zip -d abc"
    assert not match(shell.from_shell(command))
    command = "unzip -abc.zip"
    assert not match(shell.from_shell(command))



# Generated at 2022-06-14 09:45:23.845946
# Unit test for function match
def test_match():
	# Test 1 : All files in archive are contained within the current folder
	assert(match(Command("unzip test.zip", "unzip:  cannot find or open test.zip, test.zip.zip or test.zip.ZIP.", "", "", "", "", "", "", ""))[0])
	
	# Test 2 : The archive contains a file outside of the current folder

# Generated at 2022-06-14 09:45:33.715930
# Unit test for function side_effect
def test_side_effect():
    import tempfile

    f = tempfile.NamedTemporaryFile()
    f.write(b'hello\n')
    f.flush()

    with zipfile.ZipFile('hello.zip', 'w') as z:
        z.write(f.name)
    zip_file = os.path.join(os.getcwd(), 'hello.zip')

    side_effect('', 'unzip -d {} {}'.format(
        shell.quote(zip_file[:-4]), zip_file))
    assert os.path.isfile(f.name)
    os.remove(zip_file)

# Generated at 2022-06-14 09:45:42.237641
# Unit test for function match
def test_match():
    assert(match(Command('unzip', '', '')) == False) # no file
    assert(match(Command('unzip', 'something.zip', '')) == False) # bad zip
    assert(match('unzip something.zip') == False) # bad zip
    assert(_zip_file(Command('unzip', '-d something.zip', '')) == 'something.zip')
    assert(_zip_file(Command('unzip', 'something', '')) == 'something.zip')
    assert(_zip_file(Command('unzip', 'something.zip', '')) == 'something.zip')
    assert(match(Command('unzip', 'something', '')) == False)
    assert(match(Command('unzip', 'something.zip', '')) == True)


# Generated at 2022-06-14 09:46:23.474160
# Unit test for function side_effect
def test_side_effect():
    from thefuck.rules.zip_file import _is_bad_zip
    import tempfile

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()
    # Create a temporary file in directory
    foo_file_path = os.path.join(tmp_dir, 'foo')
    open(foo_file_path, 'w').close()

    # Make sure we have a bad zip file
    assert _is_bad_zip(foo_file_path)

    # Test the function side_effect
    side_effect(old_cmd=(), command=())

    # Test if the file is removed
    assert not _is_bad_zip(foo_file_path)

    # Remove the directory after the test
    os.rmdir(tmp_dir)

# Generated at 2022-06-14 09:46:29.881046
# Unit test for function side_effect
def test_side_effect():
    with zipfile.ZipFile("test.zip", "w") as zip:
        with open("test","w") as file:
            file.write("hello")
        zip.write("test")
    old_cmd = type("cmd",(),{'script':"unzip test.zip"})
    cmd = type("cmd",(),{'script':"unzip -d test.zip"})
    side_effect(old_cmd, cmd)
    assert not os.path.isfile("test")

# Generated at 2022-06-14 09:46:36.988125
# Unit test for function match
def test_match():
    assert match(Command('unzip archive.zip', '')) == False
    assert match(Command('unzip -d destination/ archive.zip', '')) == False
    assert match(Command('unzip file.zip', '')) == True
    assert match(Command('unzip file', '')) == True
    assert match(Command('unzip something', '')) == False

# Generated at 2022-06-14 09:46:48.883387
# Unit test for function match
def test_match():
    from thefuck.rules.unzip_single_file import match

    # Should not match
    assert not match(Command('unzip file1.zip file2.txt -d abc', None))

    # Should match
    assert match(Command('unzip file1.zip -d abc', None))
    assert match(Command('unzip file1.zip', None))

    # Should not match with bad files
    assert not match(Command('unzip /file/does/not/exist.zip', None))
    assert not match(Command('unzip /bad/file.zip', None))

    # Should match with bad files
    assert match(Command('unzip /bad/file.zip /file/does/not/exist.zip', None))
    assert match(Command('unzip /bad/file.zip /bad/file2.zip', None))

# Generated at 2022-06-14 09:47:00.669859
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    directory = tempfile.mkdtemp()
    archive = tempfile.NamedTemporaryFile(suffix=".zip")

# Generated at 2022-06-14 09:47:09.626514
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', ''))
    assert not match(Command('unzip file1.zip file2.zip', ''))
    assert not match(Command('unzip -d dest file.zip', ''))
    assert not match(Command('unzip -j file.zip', ''))
    assert not match(Command('unzip -l file.zip', ''))
    assert not match(Command('unzip -t file.zip', ''))
    assert not match(Command('unzip -v file.zip', ''))



# Generated at 2022-06-14 09:47:16.236847
# Unit test for function match
def test_match():
    command = Command('unzip test.zip', '', '')
    assert not _is_bad_zip('test.zip')
    assert not match(command)

    command = Command('unzip test.zip', '', '')
    assert _is_bad_zip('test.zip')
    assert match(command)


# Generated at 2022-06-14 09:47:26.442204
# Unit test for function match
def test_match():
    from thefuck.shells import Bash

    assert match(Bash('unzip file.zip')) is True
    assert match(Bash('unzip file.zip file')) is True
    assert match(Bash('unzip file.zip file -d new_dir')) is False
    assert match(Bash('unzip file.zip file -abc')) is True

    assert match(Bash('unzip file.zipp file')) is False
    assert match(Bash('unzip file')) is False
    assert match(Bash('unzip')) is False



# Generated at 2022-06-14 09:47:32.868810
# Unit test for function side_effect
def test_side_effect():
    # create temporary test file
    temp_file = tempfile.NamedTemporaryFile(delete=True)
    # unzip temporary file
    shell.and_('unzip', temp_file.name)
    # remove temporary file
    temp_file.close()
    # check test file exists
    assert os.path.exists(temp_file.name[:-4])
    # run side_effect function
    side_effect(None, 'unzip ' + temp_file.name)
    # check test file does not exist
    assert not os.path.exists(temp_file.name[:-4])

# Generated at 2022-06-14 09:47:45.637386
# Unit test for function match
def test_match():
    assert not match(Command(script='mkdir -p out/foo/bar'))
    assert not match(Command(script='touch out/foo/bar'))
    assert match(Command(script='unzip -nj foo.zip'))
    assert match(Command(script='unzip -l foo'))
    assert match(Command(script='unzip foo'))
    assert match(Command(script='unzip -l foo.zip'))
    assert match(Command(script='unzip -l foo.zip file1 file2'))
    assert not match(Command(script='unzip -l bar.zip file1 file2'))
    assert not match(Command(script='unzip -d bar.zip file1 file2'))
    assert match(Command(script='unzip foo.zip file1 file2'))

# Generated at 2022-06-14 09:48:22.162715
# Unit test for function match
def test_match():
    assert match(Command('unzip bad.zip', ''))
    assert not match(Command('unzip -d bad.zip', ''))
    assert match(Command('unzip bad.zip -d', ''))

# Generated at 2022-06-14 09:48:34.951530
# Unit test for function match
def test_match():
    from thefuck.types import Command

    commands = [
        Command('unzip notanarchive'),
        Command('unzip archive.zip'),
        Command('unzip archive.zip foo.txt'),
        Command('unzip archive.zip -d foo'),
        Command('unzip archive.zip -d \'foo/bar\'')]

    for c in commands:
        assert match(c) == False

    assert match(Command('unzip archive.zip notanarchive')) == False

    with zipfile.ZipFile('archive.zip', 'w') as archive:
        archive.writestr('foo.txt', 'foo')

    assert match(Command('unzip archive.zip notanarchive')) == False


# Generated at 2022-06-14 09:48:40.392569
# Unit test for function side_effect
def test_side_effect():
    from thefuck.shells import shell
    import zipfile
    import os
    from thefuck.shells import get_shell
    from thefuck.types import Command

    os.makedirs('dir')
    os.chdir('dir')

    with open('file', 'w+') as f:
        f.write('file')
    with open('dir/file', 'w+') as f:
        f.write('dir/file')

    with zipfile.ZipFile('file.zip', 'w') as f:
        f.write('file')
        f.write('dir/file')

    old_cmd = Command('unzip file.zip', '', '')
    new_cmd = Command('unzip file.zip', '', '')
    side_effect(old_cmd, new_cmd)


# Generated at 2022-06-14 09:48:51.735137
# Unit test for function side_effect
def test_side_effect():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os.path import join
    import os
    import zipfile
    from io import BytesIO

    test_dir = mkdtemp(prefix="thefuck_unzip_test_dir")

    normal_file = 'myfile.txt'
    with open(join(test_dir, normal_file), 'w') as f:
        f.write('foobar')

    nested_dir = join(test_dir, 'nested')
    os.mkdir(nested_dir)
    nested_file = join(nested_dir, 'myfile.txt')
    with open(nested_file, 'w') as f:
        f.write('foobar')

    zip_file = join(test_dir, 'test.zip')

# Generated at 2022-06-14 09:48:55.015194
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', '', '/')) == False
    assert match(Command('unzip file.zip -d folder', '', '/')) == False
    assert match(Command('unzip -d folder file.zip', '', '/')) == False


# Generated at 2022-06-14 09:49:07.926896
# Unit test for function match
def test_match():
    assert match(Command('unzip', script='unzip file.zip')) is False
    assert match(Command('unzip', script='unzip file1.zip file2.zip')) is False
    assert match(Command('unzip', script='unzip -d dir1 -d dir2 file.zip')) is False
    assert match(Command('unzip', script='unzip -o file.zip')) is False
    assert match(Command('unzip', script='unzip -d dir file.zip')) is False
    assert match(Command('unzip', script='unzip -d dir file1.zip file2.zip')) is False

    # zip files have more than 1 file in them
    assert match(Command('unzip', script='unzip file.zip')) is False

# Generated at 2022-06-14 09:49:12.833832
# Unit test for function match
def test_match():
    command = 'unzip -d'
    assert not match(command)
    command = 'unzip -d a.zip'
    assert not match(command)
    command = 'unzip -d a'
    assert not match(command)
    command = 'unzip a'
    assert not match(command)
    command = 'unzip a.zip'
    assert match(command)


# Generated at 2022-06-14 09:49:23.854682
# Unit test for function side_effect
def test_side_effect():
    cwd = os.getcwd()
    os.chdir('/tmp')
    file = open("not_a_dir", "w")
    file.close()
    os.chdir('/tmp')
    file = open("not_a_dir_either", "w")
    file.close()
    os.chdir('/tmp')
    os.mkdir("dir")
    os.chdir('/tmp')
    os.mkdir("dir_too")
    os.chdir('/tmp')
    os.mkdir("dir_too_2")
    os.chdir('/tmp')
    os.mkdir("dir_too_3")
    os.chdir('/tmp')
    os.mkdir("dir_too_4")
    os.chdir('/tmp')
    os.mkdir

# Generated at 2022-06-14 09:49:26.441009
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip'))
    assert not match(Command('unzip -d dir file.zip'))



# Generated at 2022-06-14 09:49:35.189863
# Unit test for function match
def test_match():
    assert match(Command('unzip test.zip', ''))
    assert not match(Command('unzip test', ''))
    assert not match(Command('unzip -d test', ''))
    assert not _is_bad_zip('test_zip/test_zip.zip')
    assert match(Command('unzip test_zip.zip', ''))
    assert match(Command('unzip test_zip', ''))
    assert match(Command('unzip -l test_zip', ''))


# Generated at 2022-06-14 09:50:49.723196
# Unit test for function match
def test_match():
    assert match(Command('unzip /tmp/test.zip', u'/tmp/test.zip'))
    assert not match(Command('unzip /tmp/test.zip', u'/tmp/test.zip -d /tmp'))
    assert match(Command('unzip /tmp/test.zip /tmp/test1.txt', u'/tmp/test.zip'))
    assert match(Command('unzip /tmp/test.zip /tmp/test1.txt /tmp/test2.txt', u'/tmp/test.zip'))
    assert not match(Command('unzip /tmp/test.zip', u'/tmp/test1.zip'))
    assert not match(Command('unzip /tmp/test.zip', u'/tmp/test/test.zip'))

# Generated at 2022-06-14 09:51:04.971533
# Unit test for function match
def test_match():
    # unzip with flag -d
    assert not match(Command('', 'unzip -d file.zip'))

    # unzip without flag -d
    assert not match(Command('', 'unzip file.zip'))

    # unzip with flag -d and file.zip file
    assert match(Command('', 'unzip -d file.zip file.zip'))

    # unzip with flag -d and file.ZIP file
    assert match(Command('', 'unzip -d file.zip file.ZIP'))

    # unzip without flag -d and file.ZIP file
    assert match(Command('', 'unzip file.zip file.ZIP'))

    # unzip with flag -d and file file
    assert match(Command('', 'unzip -d file.zip file'))

    # unzip without flag -