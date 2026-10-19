

# Generated at 2022-06-14 09:41:01.764085
# Unit test for function side_effect
def test_side_effect():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import chdir, getcwd, mkdir, makedirs

    def assert_path(path, exists):
        assert os.path.exists(path) == exists

    temp_dir = mkdtemp()

# Generated at 2022-06-14 09:41:06.152136
# Unit test for function side_effect
def test_side_effect():
    with tempfile.NamedTemporaryFile() as temp:
        command = 'echo one'
        command_output = {command: 'one'}
        assert side_effect(command, command_output) is None
        assert os.path.isfile(temp.name)

# Generated at 2022-06-14 09:41:15.248804
# Unit test for function side_effect
def test_side_effect():
    old_cmd = Command('unzip file.zip')
    command = Command('unzip -d file file.zip')
    if not _zip_file(old_cmd):
        assert False
    if not _zip_file(command):
        assert False

    zip_file = _zip_file(old_cmd)
    dir_name = _zip_file(command)[:-4]
    archive = zipfile.ZipFile(zip_file, 'w')
    test_text = u'Тест'
    file_name = u'тест'
    file_path = os.path.join(dir_name, file_name)

    with archive:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)


# Generated at 2022-06-14 09:41:24.786969
# Unit test for function side_effect
def test_side_effect():
    class OldCmd:
        def __init__(self, script):
            self.script = script
            self.script_parts = script.split(' ')

    # unzip should not remove files outside the current directory
    cmd = OldCmd("unzip /root/file")
    assert side_effect(cmd, None) is None
    assert os.path.exists("/root/file")

    # unzip should not remove directories
    os.mkdir("/tmp/test_directory")
    cmd = OldCmd("unzip /tmp/test_directory")
    assert side_effect(cmd, None) is None
    assert os.path.exists("/tmp/test_directory")

    # unzip should remove files inside the current directory
    os.mkdir("/tmp/test_dir")

# Generated at 2022-06-14 09:41:27.905362
# Unit test for function match
def test_match():
    assert match(Command('unzip xy.zip'))
    assert match(Command('unzip xy.zip a.txt'))
    assert not match(Command('unzip -d xy.zip'))
    assert not match(Command('unzip -d xy.zip a.txt'))
    assert not match(Command('unzip'))


# Generated at 2022-06-14 09:41:29.437588
# Unit test for function match
def test_match():
    command = type('Command', (object,), {'script': 'unzip file1.zip'})
    assert match(command) == False



# Generated at 2022-06-14 09:41:42.061657
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import os
    import zipfile
    import shutil
    from thefuck.utils import replace_argument

    def side_effect(old_cmd, command):
        return replace_argument(old_cmd.script, '-d',
                                shell.quote('test_dir')).script

    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        side_effect(old_cmd=shell.And('', ''), command=shell.And('', ''))
        with open('test_file','w') as test_file:
            pass
        with zipfile.ZipFile('test_file.zip','w') as zipf:
            zipf.write('test_file')
        shutil.rmtree('test_dir')

# Generated at 2022-06-14 09:41:51.817958
# Unit test for function match
def test_match():
    # The function return False if there is no unzip
    assert not match(Command('unzip', 'unzip [unzip]', '', '', '', rules={}))
    assert not match(Command('unzip -d', 'unzip -d', '', '', '', rules={}))
    # The function returns False if the command is not unzip
    assert not match(Command('ls', 'ls', '', '', '', rules={}))
    # The function needs a file with the extension ".zip"
    assert not match(Command('unzip example.zip', 'unzip example.zip', '', '', '', rules={}))
    assert match(Command('unzip example.zip example.tar.gz', 'unzip example.zip example.tar.gz', '', '', '', rules={}))
    # The function checks if

# Generated at 2022-06-14 09:41:58.802925
# Unit test for function side_effect
def test_side_effect():
    with zipfile.ZipFile('test.zip', 'w') as z:
        z.writestr('test.txt', 'This is a test.')
    assert os.path.exists('test.txt')
    old_cmd = Command('unzip test.zip', '', '')
    side_effect(old_cmd, 'unzip -d test.zip')
    assert not os.path.exists('test.txt')
    os.remove('test.zip')

# Generated at 2022-06-14 09:42:11.892386
# Unit test for function match
def test_match():
    # test when command outputs null
    assert match(Command("unzip", "unzip", "")) == False

    # test when the argument is not the end of '.zip'
    assert match(Command("unzip", "unzip", "file",
                        settings={'require_confirmation': True})) == True

    # test when command outputs not null and the argument is the end of '.zip'
    assert match(Command("unzip", "unzip", "file.zip")) == True

    # test when '-d' appeared in the command
    assert match(Command("unzip", "unzip", "-d")) == False

    # test when '-d' appeared in the command
    assert match(Command("unzip", "unzip", "-d file.zip")) == False


# Generated at 2022-06-14 09:42:37.380491
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    import os
    from thefuck.rules.unzip_single_file import side_effect

    temp_dir = tempfile.mkdtemp(prefix='test_side_effect')

    zip_file = tempfile.NamedTemporaryFile(suffix='.zip')
    with zipfile.ZipFile(zip_file, 'w') as archive:
        archive.writestr('test', 'test')

    shutil.copyfile(zip_file.name, os.path.join(temp_dir, 'test.zip'))
    zip_file.close()

    side_effect(None, None)

    assert not os.path.isfile(os.path.join(temp_dir, 'test'))

    shutil.rmtree(temp_dir)

# Generated at 2022-06-14 09:42:49.179197
# Unit test for function match
def test_match():
    # Create a test zip file that should be detected as bad
    with zipfile.ZipFile('test_fix_unzip_zip_directory.zip', 'w') as archive:
        archive.write('test_fix_unzip_zip_directory/file')

    # Command that should be corrected
    old_cmd = Command('unzip test_fix_unzip_zip_directory.zip',
                      '  inflating: file')
    # Command fixed by get_new_command
    new_cmd = 'unzip -d test_fix_unzip_zip_directory test_fix_unzip_zip_directory.zip'

    assert match(old_cmd) is True
    assert get_new_command(old_cmd) == new_cmd

# Generated at 2022-06-14 09:43:01.645150
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', '')) is True
    assert match(Command('unzip file.zip file1 file2', '')) is True
    assert match(Command('unzip file', '')) is True
    assert match(Command('unzip file1 file2', '')) is True
    assert match(Command('unzip -d dir file', '')) is False
    assert match(Command('unzip file', '', None)) is False
    assert _is_bad_zip('tests/test_unzip_bad.zip') is True
    assert match(Command('unzip tests/test_unzip_bad.zip', '')) is True
    assert match(Command('unzip -d dir file', '')) is False


# Generated at 2022-06-14 09:43:05.408539
# Unit test for function match
def test_match():
    cmd = Command('unzip a.zip', '', '%d/%f:  bad zipfile offset'
                  ' (local header sig):  %d\n')
    assert match(cmd) == True


# Generated at 2022-06-14 09:43:12.437846
# Unit test for function side_effect
def test_side_effect():
    from thefuck.rules.unzip import match
    from thefuck.rules.unzip import side_effect
    from thefuck.shells import Bash

    # Prepare for test
    bash = Bash()
    tmpdir = tempfile.mkdtemp()
    testdir = tmpdir + '/testdir'
    os.makedirs(testdir)
    testfile = testdir + '/samplefile'
    testfile2 = testdir + '/samplefile2'
    archivefile = '/tmp/test.zip'
    with open(testfile, 'wb') as f:
        f.write(b'** This is the original file **\n')
    with open(testfile2, 'wb') as f:
        f.write(b'** This is the original file 2 **\n')

# Generated at 2022-06-14 09:43:21.822691
# Unit test for function side_effect
def test_side_effect():
    import shutil

    os.chdir(os.path.dirname(__file__))
    with zipfile.ZipFile('data.zip', 'r') as archive:
        archive.extractall()

    cmd = type("Command", (object,), {"script": "unzip data.zip",
                                      "script_parts": ["unzip", "data.zip"]})
    # Test if files from zip are removed and kept if not in current directory
    open("test1", 'w').close()
    open("test2", 'w').close()
    side_effect(cmd, cmd)
    assert not os.path.isfile("test1")
    assert not os.path.isfile("test2")
    assert os.path.isfile("test3")

    # Clean up (remove unzipped files and test files)
    os

# Generated at 2022-06-14 09:43:26.443919
# Unit test for function match
def test_match():
    assert match(get_command('unzip file.zip'))
    assert match(get_command('unzip file'))
    assert not match(get_command('unzip file -d target'))
    assert not match(get_command('unzip --help'))



# Generated at 2022-06-14 09:43:39.042531
# Unit test for function match
def test_match():
    # bad zip file
    assert match(Command('unzip file.zip')) == True
    # zip file to extract to current directory
    assert match(Command('unzip file.zip dir/file.txt')) == False
    # zip file to extract to specific directory
    assert match(Command('unzip file.zip -d dir')) == False
    # bad zip file to extract to current directory
    assert match(Command('unzip file.zip dir/file.txt')) == False
    # bad zip file to extract to specific directory
    assert match(Command('unzip file.zip -d dir')) == False
    # bad zip file to extract without files
    assert match(Command('unzip file.zip /path/to/unzip/file.txt')) == True
    # bad zip file to extract with other files

# Generated at 2022-06-14 09:43:46.722004
# Unit test for function match
def test_match():
    assert _is_bad_zip('tests/zip/bad_zip.zip') == True
    assert _is_bad_zip('tests/zip/good_zip.zip') == False
    assert match(Command('unzip bad_zip.zip', '')) == True
    assert match(Command('unzip bad_zip.zip', '')) == True
    assert match(Command('unzip bad_zip', '')) == True
    assert match(Command('unzip bad_zip.tar.gz', '')) == False



# Generated at 2022-06-14 09:43:53.374789
# Unit test for function match
def test_match():
    assert match(Command('unzip -o file.zip', '', '', 0, ''))
    assert not match(Command('unzip -d file.zip', '', '', 0, ''))
    assert not match(Command('unzip -o file.zip file.txt', '', '', 0, ''))
    assert not match(Command('unzip -o malformed.zip', '', '', 0, ''))


# Generated at 2022-06-14 09:44:21.161617
# Unit test for function match
def test_match():
    command = Command(script='unzip foo.zip')
    assert match(command)



# Generated at 2022-06-14 09:44:32.890302
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)

    # Create temp files and directories, similar to unzip -qq output
    import zipfile
    zip_archive = tempfile.NamedTemporaryFile(suffix='.zip')
    zip_file = zipfile.ZipFile(zip_archive.name, 'w')
    zip_file.writestr('test.txt', 'test')
    zip_file.close()
    os.mkdir('testdir')
    test_file = open('testfile', 'w')
    test_file.close()

    # Run function and check if files are removed
    command = type('test_cmd', (object,), {'script': 'unzip {}'.format(zip_archive.name)})
    side_effect(command, command)

# Generated at 2022-06-14 09:44:39.363929
# Unit test for function side_effect
def test_side_effect():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import makedirs, path

    dirpath = mkdtemp()

# Generated at 2022-06-14 09:44:46.220009
# Unit test for function match
def test_match():
    assert match(Command('unzip example.zip', '', ''))
    assert not match(Command('unzip -d example example.zip', '', ''))
    assert not match(Command('', '', ''))
    assert not match(Command('unzip', '', ''))
    assert not match(Command('unzip -d', '', ''))
    assert not match(Command('unzip data', '', ''))



# Generated at 2022-06-14 09:44:54.255776
# Unit test for function side_effect
def test_side_effect():
    zip_file = os.path.join(os.path.dirname(__file__), 'unzip.zip')
    test_file1 = os.path.join(os.path.dirname(__file__), 'unzip.test')
    test_file2 = os.path.join(os.path.dirname(__file__), 'unziptest2')
    test_file3 = os.path.join(os.path.dirname(__file__), 'a.txt')
    open(test_file1, 'a').close()
    open(test_file2, 'a').close()
    open(test_file3, 'a').close()
    command = "unzip %s" % (zip_file)
    side_effect(command, command)

# Generated at 2022-06-14 09:45:05.933521
# Unit test for function side_effect
def test_side_effect():
    from thefuck.shells import get_shell
    from thefuck.types import Command
    from thefuck.utils import create_file, replace_argument
    from thefuck.specific.unzip import side_effect

    with get_shell() as shell:
        with shell.spawn(
                'unzip -ay -o ~/test.zip',
                stdout=shell.TEST_OUTPUT,
                stderr=shell.TEST_OUTPUT):
            pass

        with create_file('~/test.zip') as zip_file:
            zip_file.write(b'test content')

        with create_file('~/normal_file.txt') as normal_file:
            normal_file.write(b'test content')

        with create_file('~/outside_dir/outside_file.txt'):
            pass

# Generated at 2022-06-14 09:45:09.328999
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip',None))
    assert not match(Command('unzip file.zip -d',None))
    assert not match(Command('unzip',None))

# Generated at 2022-06-14 09:45:22.538373
# Unit test for function side_effect
def test_side_effect():

    # Create a test zip file
    test_zip = zipfile.ZipFile('test.zip','w')

    # Add two files
    test_zip.write('test_file.py','test_file.py')
    test_zip.write('test_file_2.py', 'test_file_2.py')
    test_zip.write('test_dir/test_file_3.py', 'test_dir/test_file_3.py')
    test_zip.close()

    # Create side effects
    command = Command('unzip test.zip')
    side_effect(command, command)

    # Assert that the files should have been removed
    assert not os.path.exists('test_file.py')
    assert not os.path.exists('test_file_2.py')

# Generated at 2022-06-14 09:45:29.771743
# Unit test for function side_effect
def test_side_effect():
    """
    Should remove extracted files from current directory
    """
    from tempfile import TemporaryDirectory
    from thefuck.types import Command

    with TemporaryDirectory() as tempdir:
        os.chdir(tempdir)
        with open('file1', 'w') as file1:
            file1.write('http://taken.com')
        with open('file2', 'w') as file2:
            file2.write('http://taken2.com')
        with open('file3', 'w') as file3:
            file3.write('http://taken3.com')
        with zipfile.ZipFile('archive.zip', 'w') as archive:
            archive.write('file1', arcname='file1')
            archive.write('file2', arcname='file2')

# Generated at 2022-06-14 09:45:31.795106
# Unit test for function side_effect
def test_side_effect():
    command = ['unzip', 'bad.zip']
    side_effect(command, command)

# Generated at 2022-06-14 09:46:06.231049
# Unit test for function side_effect
def test_side_effect():
    old_cmd = type('cmd', (), {'script': 'unzip /path/to/a.zip'})
    command = type('cmd', (), {'script': 'unzip -d /path/to/a.zip'})
    side_effect(old_cmd, command)

# Generated at 2022-06-14 09:46:17.557481
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    from thefuck.shells import get_all_executables
    temp_dir = tempfile.mkdtemp(prefix='unzip_test')

# Generated at 2022-06-14 09:46:22.454313
# Unit test for function match
def test_match():
    assert _is_bad_zip('test.zip') == True
    assert _is_bad_zip('test_files/test.zip') == False
    assert _is_bad_zip('test_files/test_2.zip') == True

# Generated at 2022-06-14 09:46:30.571158
# Unit test for function side_effect
def test_side_effect():

    class Command:
        def __init__(self, script):
            self.script = script
            self.script_parts = script.split()

    old_cmd = Command("unzip test")
    os.mkdir("test")
    zip_file = zipfile.ZipFile("test.zip", "w")
    zip_file.close()
    command = Command("unzip -d test test.zip")

    side_effect(old_cmd, command)

    assert os.path.isfile("test/test.zip")
    os.remove("test/test.zip")
    os.rmdir("test")
    os.remove("test.zip")

# Generated at 2022-06-14 09:46:38.241761
# Unit test for function side_effect
def test_side_effect():
    """
    Test if side_effect works well
    """
    command = shell.and_('unzip test.zip', 'cd subfolder/subsubfolder', 'ls')
    old_cmd = shell.and_('unzip test.zip', 'ls')
    side_effect(old_cmd, command)
    assert shell.has_executable('subsubfolder')

# Generated at 2022-06-14 09:46:48.359421
# Unit test for function match
def test_match():
    # unzip doesn't exist
    assert not match(Command('unzip'))
    # unzip -d
    assert not match(Command('unzip -d aaa'))
    # test bad zip file
    assert match(Command('unzip aaa'))
    assert match(Command('unzip aaa.zip'))
    # test good zip file
    assert not match(Command('unzip aaa.zip -d aaa'))
    # test good options
    assert not match(Command('unzip -l'))
    assert not match(Command('unzip -t'))
    assert not match(Command('unzip -c'))
    assert not match(Command('unzip -Z'))
    assert not match(Command('unzip -v'))
    assert not match(Command('unzip -z'))
    assert not match

# Generated at 2022-06-14 09:46:59.947531
# Unit test for function match
def test_match():
    assert not match(command=Command(script='unzip -myfile.zip'))
    assert match(command=Command(script='unzip myfile.zip'))
    assert match(command=Command(script=r'unzip myfile.zip\*.ext'))
    assert not match(command=Command(script='unzip -d myfile.zip'))
    assert not match(command=Command(script='unzip -d -myfile.zip'))
    assert not match(command=Command(script='unzip -d myfile.zip'))


# Generated at 2022-06-14 09:47:08.609723
# Unit test for function side_effect
def test_side_effect():
    # pip install thefuck
    # unpacked_file: file_to_unpack
    with open('/tmp/file_to_unpack', 'w') as f: f.write('')
    with zipfile.ZipFile('/tmp/file_to_unpack.zip', 'w') as myzip:
       myzip.write('/tmp/file_to_unpack')

    # check if file_to_unpack exists
    with open('/tmp/file_to_unpack', 'r') as f:
       assert(True)
    # unzip the file
    os.system('unzip /tmp/file_to_unpack.zip -d /tmp/')
    # check that file_to_unpack is still there

# Generated at 2022-06-14 09:47:18.288890
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    directory = tempfile.mkdtemp()
    for filename in ['file1.py', 'file2.exe']:
        with open(os.path.join(directory, filename), 'w') as output:
            output.write('42')

    old_cmd = Command('zip -r example test', '', directory)
    command = Command('unzip -d example.zip', '', directory)
    side_effect(old_cmd, command)

    assert not os.path.exists('file1.py')
    assert not os.path.exists('file2.exe')

# Generated at 2022-06-14 09:47:23.539597
# Unit test for function match
def test_match():
    assert not match(Command('unzip test.zip', '', ''))
    assert not match(Command('unzip -d test test.zip', '', ''))
    assert match(Command('unzip test.zip', '', ''))



# Generated at 2022-06-14 09:47:54.735224
# Unit test for function side_effect
def test_side_effect():
    # Mock a function to make it easier to test
    with zipfile.ZipFile('archive.zip', 'r') as archive:
        archive.namelist = lambda: ['archive.zip', 'test/test.txt']
        old_cmd = shell.AndScript(['unzip', 'archive.zip'], 'echo')
        side_effect(old_cmd, 'unzip -d test archive.zip')
        assert os.path.exists('test/test.txt')

# Generated at 2022-06-14 09:48:04.799715
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    files_paths = [os.path.join(tempfile.gettempdir(), file) for file in files]
    with zipfile.ZipFile('/tmp/test_side_effect.zip', 'w') as archive:
        for file_path in files_paths:
            open(file_path, 'a').close()
            archive.write(file_path)

    side_effect(None, None)

    for file in files_paths:
        assert os.path.exists(file) is False

# Generated at 2022-06-14 09:48:17.186781
# Unit test for function side_effect
def test_side_effect():
    from thefuck import main
    from thefuck.shells import get_closest, FunctionNotFound
    from thefuck.types import Command

    #testing unzip -d function
    os.makedirs('test_folder')
    os.makedirs('test_folder/testin')
    os.chdir('test_folder')
    with open('test.txt', 'w') as f:
        f.write('test')
    with zipfile.ZipFile('../tests/resources/test.zip', 'r') as archive:
        archive.extractall()
    assert os.path.exists('testin/test.txt')
    old_cmd = Command('unzip', 'test.zip')
    with open('testin/test.txt', 'r') as f:
        f.read()
    assert f.read()

# Generated at 2022-06-14 09:48:25.523003
# Unit test for function match
def test_match():
    command = 'unzip wrong.zip'
    assert match(shell.from_script(command))

    command = 'unzip wrong.zip wrong2.zip'
    assert match(shell.from_script(command))

    command = 'unzip -aa wrong.zip'
    assert match(shell.from_script(command))

    command = 'unzip -d wrong.zip'
    assert not match(shell.from_script(command))

    command = 'unzip wrong.zip -aa'
    assert match(shell.from_script(command))



# Generated at 2022-06-14 09:48:33.315413
# Unit test for function match
def test_match():
    assert match(Command(script='unzip /tmp/file.zip'))
    assert match(Command(script='unzip file'))
    assert match(Command(script='unzip /tmp/file'))
    assert not match(Command(script='unzip -d /tmp/file /tmp/file.zip'))
    assert not match(Command(script='unzip /tmp/file.zip /tmp/file2.zip'))
    assert not match(Command(script='unzip /tmp/file.zip /tmp/file'))


# Generated at 2022-06-14 09:48:37.796247
# Unit test for function match
def test_match():
    assert not match(Command('unzip file.zip', '', stderr='error 1'))
    assert match(Command('unzip file.zip', '', stderr='error 2'))
    assert match(Command('unzip file', '', stderr='error 2'))
    assert not match(Command('unzip file.zip -d dest', '', stderr='error 2'))


# Generated at 2022-06-14 09:48:47.251197
# Unit test for function match
def test_match():
    assert not match(Command('unzip test.zip', '', None))
    assert not match(Command('unzip test.zip a b c', '', None))
    assert not match(Command('unzip test.zip -d dest', '', None))
    assert not match(Command('unzip file.zip', '', None))
    assert match(Command('unzip test.zip', '', '/tmp'), '')
    assert match(Command('unzip file.zip', 'zip test.zip a b c', '/tmp'), '')


# Generated at 2022-06-14 09:48:56.102062
# Unit test for function side_effect
def test_side_effect():
    class Command:
        script = u'unzip file.zip'
        def __getitem__(self, key):
            return self.script.split()[key]

    # Create test dir
    test_dir = 'test_dir'
    os.makedirs(test_dir)

    # Create test zip file
    test_zip_file = 'test.zip'
    test_file_in_zip = 'test_file'
    with zipfile.ZipFile(test_zip_file, 'w') as test_zip:
        test_zip.writestr(test_file_in_zip, "file content")

    # Create file in current directory with the same name as in zip file
    with open(test_file_in_zip, 'w') as test_file:
        test_file.write("file content")

   

# Generated at 2022-06-14 09:49:04.861836
# Unit test for function side_effect
def test_side_effect():
    old_cmd = type('Command', (object,), {
        'script': u'unzip /tmp/bad_zip.zip',
        'script_parts': [u'unzip', '/tmp/bad_zip.zip'],
    })()

    command = type('Command', (object,), {
        'script': u'unzip /tmp/bad_zip.zip -d bad_zip',
    })()

    side_effect(old_cmd, command)

    assert not os.path.exists('/tmp/foo')

# Generated at 2022-06-14 09:49:06.437489
# Unit test for function match
def test_match():
    assert match(Command('unzip a.zip'))
    assert not match(Command('unzip -d a.zip'))

# Generated at 2022-06-14 09:50:02.394768
# Unit test for function match
def test_match():
    assert not match(Command('unzip foo.zip -d foo', '', ''))
    assert match(Command('unzip foo.zip', '', ''))
    assert match(Command('unzip foo', '', ''))

# Generated at 2022-06-14 09:50:09.446606
# Unit test for function side_effect
def test_side_effect():
    assert side_effect(shell.And("unzip test.zip", "unzip:  cannot find or open test.zip",
                                 "unzip:  nothing to do"), "unzip test.zip") == None
    assert side_effect(shell.And("unzip test.zip", "test.txt"), "unzip test.zip") == None
    assert side_effect(shell.And("unzip test.zip", "test.txt", "test2.txt"), "unzip test.zip") == None

# Generated at 2022-06-14 09:50:17.559387
# Unit test for function side_effect
def test_side_effect():
    os.mkdir('/tmp/fuck-test')
    os.chdir('/tmp/fuck-test')
    # Create an empty directory
    os.mkdir('dir')
    # Create an empty file
    open('empty_file', 'w').close()
    # Create a file containing text
    with open('some_file', 'w') as f:
        f.write('some_text')

    # Create and fill the zip file
    archive = zipfile.ZipFile('fuck.zip', 'w')
    archive.write('some_file')
    archive.write('empty_file')
    archive.write('dir')
    archive.close()

    # Call the side_effect function
    curse = Command('unzip fuck.zip', '/tmp/fuck-test')
    side_effect(curse, curse)
    # Test

# Generated at 2022-06-14 09:50:24.500673
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command

    # Left empty by purpose, we don't care about what they do
    fake_cmd = Command('fake', '')
    fake_cmd.script = 'fake_script'

    # We don't care about what happens in the real side effect
    # We just want to make sure that it doesn't raise
    side_effect(fake_cmd, fake_cmd)

# Generated at 2022-06-14 09:50:34.589032
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    from thefuck.tests.utils import Command

    with tempfile.NamedTemporaryFile() as file:
        command = Command('unzip {}'.format(file.name))
        os.mkdir(file.name[:-4])
        with open(file.name[:-4] + '/file', 'w'):
            pass
        side_effect(command, command)
        assert not os.path.isfile(file.name[:-4] + '/file')
        assert os.path.isdir(file.name[:-4])

# Generated at 2022-06-14 09:50:47.014937
# Unit test for function side_effect
def test_side_effect():
    bad_zip = u"bad.zip"
    file_to_be_deleted = u"test.py"
    file_to_be_kept = u"test.txt"
    content = u"test"

    with zipfile.ZipFile(bad_zip, "w") as archive:
        archive.writestr(file_to_be_deleted, content)
        archive.writestr(file_to_be_kept, content)

    with open(file_to_be_kept, "w") as f:
        f.write(content)

    with open(file_to_be_deleted, "w") as f:
        f.write(content)

    class FakeCommand:
        def __init__(self):
            self.script = u"unzip {}".format(bad_zip)
            self

# Generated at 2022-06-14 09:50:58.597298
# Unit test for function side_effect
def test_side_effect():
    try:
        import tempfile
    except ImportError:
        return

    with tempfile.TemporaryDirectory() as tmp_dir:
        old_cmd = 'unzip foo.zip'
        os.chdir(tmp_dir)
        os.mkdir('foo')
        os.mkdir('foo/bar')
        with open(os.path.join(tmp_dir, 'foo', 'bar', 'baz.txt'), 'w'):
            pass

        with zipfile.ZipFile(os.path.join(tmp_dir, 'foo.zip'), 'w') as archive:
            archive.write(os.path.join(tmp_dir, 'foo', 'bar', 'baz.txt'))

        command = get_new_command(old_cmd)
        side_effect(old_cmd, command)
