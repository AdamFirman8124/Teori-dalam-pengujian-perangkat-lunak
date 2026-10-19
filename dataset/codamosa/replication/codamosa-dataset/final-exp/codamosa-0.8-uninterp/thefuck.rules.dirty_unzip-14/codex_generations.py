

# Generated at 2022-06-14 09:41:04.053708
# Unit test for function side_effect
def test_side_effect():
    shell.from_string('')

    old_cmd = Mock(script='unzip t.zip',
                   script_parts=['unzip', 't.zip', 'file.txt'])
    command = Mock(script='unzip -d out t.zip',
                   script_parts=['unzip', '-d', 'out', 't.zip', 'file.txt'])
    archive = Mock()
    archive.namelist = Mock(return_value=['file.txt', 'file.txt.csv'])
    with patch('os.remove') as rm:
        with patch('zipfile.ZipFile') as z:
            z.return_value.__enter__.return_value = archive
            with patch('os.getcwd') as cwd:
                cwd.return_value = '/'

# Generated at 2022-06-14 09:41:09.575983
# Unit test for function match
def test_match():
    #Test when unzip is correctly used
    command = Command('unzip file.zip', '')
    assert not match(command)

    #Test when unzip is wrongly used
    command = Command('unzip file', '')
    assert match(command)



# Generated at 2022-06-14 09:41:14.768065
# Unit test for function match
def test_match():
    assert match(Command('unzip test', 'sudo unzip test.zip'))
    assert not match(Command('unzip -d test', 'sudo unzip -d test test.zip'))
    assert not match(Command('unzip -d test', 'sudo unzip -d test'))
    assert not match(Command('unzip test', 'sudo unzip'))
    assert not match(Command('unzip test', 'sudo unzip -d'))
    assert not match(Command('unzip test', ''))
    assert not match(Command('unzip test', ''))

# Generated at 2022-06-14 09:41:27.479866
# Unit test for function side_effect
def test_side_effect():
    from thefuck.shells import shell
    shell.from_shell('foo')
    assert shell.from_shell('echo foo').script == 'foo'
    assert shell.from_shell('mkdir test').script == 'mkdir test'
    assert shell.to_shell('foo', Key('esc')) == 'foo'
    assert shell.to_shell('echo foo', Key('esc')) == 'echo foo'

    zip_filename = u'{}/{}'.format(os.getcwd(), 'TheFuck.zip')
    archive = zipfile.ZipFile(zip_filename, 'w')
    try:
        archive.write('requirements.txt')
    finally:
        archive.close()

    assert not os.path.isfile('TheFuck')
    assert not os.path.isfile('requirements.txt')


# Generated at 2022-06-14 09:41:33.494921
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    tmp_file_path = tempfile.mkdtemp()
    file_name = u'hello_world.txt'
    archive_name = u'{}.zip'.format(tmp_file_path)
    with zipfile.ZipFile(archive_name, 'w') as archive:
        archive.write(file_name)
    side_effect(
        Command(
            script='unzip {}'.format(archive_name),
            cmd='unzip',
            stdout='',
            stderr=''), Command(
                script='unzip {}'.format(archive_name),
                cmd='unzip',
                stdout='',
                stderr=''))
    assert not os.path.isfile(os.path.join(tmp_file_path, file_name))

# Generated at 2022-06-14 09:41:44.699128
# Unit test for function side_effect
def test_side_effect():
    from tempfile import mkdtemp
    from thefuck.types import Command
    from shutil import rmtree
    tmpdir = mkdtemp(prefix='thefuck')
    new_path = u'{}/new'.format(tmpdir)
    old_path = u'{}/old'.format(tmpdir)
    with open(new_path, 'w') as new_file:
        new_file.write(u'new content')
    with open(old_path, 'w') as old_file:
        old_file.write(u'old content')
    old_cmd = Command('unzip test.zip', new_path)
    side_effect(old_cmd, old_cmd)
    with open(new_path) as new_file:
        assert new_file.read() == u'old content'
   

# Generated at 2022-06-14 09:41:49.541028
# Unit test for function side_effect
def test_side_effect():
    old_cmd = type('FakeCommand', (object,), {'script': 'unzip bug.zip'})
    new_cmd = type('FakeCommand', (object,), {'script': 'unzip -d bug bug.zip'})
    side_effect(old_cmd, new_cmd)

# Generated at 2022-06-14 09:41:54.230774
# Unit test for function match
def test_match():
    assert match(Command('unzip', 'unzip foo.zip'))
    assert not match(Command('unzip', 'unzip -d foo.zip'))
    assert match(Command('unzip', 'unzip -x foo.zip'))


# Generated at 2022-06-14 09:42:02.654421
# Unit test for function side_effect
def test_side_effect():
    import shutil
    import tempfile
    import zipfile
    script_parts = [
        u'/usr/bin/unzip',
        u'unzip_test.zip',
        u'unzip_test.txt'
    ]

    test_dir = tempfile.mkdtemp()

    with open(os.path.join(test_dir, 'unzip_test.txt'), 'w+') as f:
        f.write('Sample file')

    with zipfile.ZipFile(os.path.join(test_dir, 'unzip_test.zip'), 'w+') as f:
        f.write(os.path.join(test_dir, 'unzip_test.txt'))

    class Command(object):
        pass

    command = Command()
    command.script = u' '.join(script_parts)

# Generated at 2022-06-14 09:42:05.655257
# Unit test for function side_effect
def test_side_effect():
    os.chdir('tests/')
    old_cmd = Command(script=u'unzip test.zip')
    side_effect(old_cmd, Command(script=old_cmd.script))
    assert os.path.exists('test')

# Generated at 2022-06-14 09:42:31.414253
# Unit test for function side_effect
def test_side_effect():
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    with open('tmp/file.txt', 'wb') as f:
        f.write('Some text')

    with zipfile.ZipFile('tmp/file.zip', 'w') as archive:
        archive.write('tmp/file.txt')

    old_cmd = Mock()
    old_cmd.script = 'unzip tmp/file.zip'
    old_cmd.script_parts = ['unzip', 'tmp/file.zip']

    side_effect(old_cmd, None)

    assert not os.path.isfile('tmp/file.txt')
    assert os.path.isfile('file.txt')

    os.remove('file.txt')
    assert os.path.isfile('tmp/file.zip')

    os

# Generated at 2022-06-14 09:42:35.555777
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command

    cmd = Command("unzip file.zip", "unzip:  cannot find or open file.zip, file.zip.zip or  file.zip.ZIP.")
    side_effect(cmd, cmd)

# Generated at 2022-06-14 09:42:47.218146
# Unit test for function match
def test_match():
    assert match(Command('unzip', 'unzip archive.zip')) == False
    assert match(Command('unzip', 'unzip archive.zip -d test-dir')) == False
    assert match(Command('unzip', 'unzip archive.zip -d test-dir/')) == False
    assert match(Command('unzip', 'unzip -j archive.zip')) == False
    assert match(Command('unzip', 'unzip -j archive.zip -d test-dir')) == False
    assert match(Command('unzip', 'unzip -j archive.zip -d test-dir/')) == False
    assert match(Command('unzip', 'unzip -d test-dir archive.zip')) == False
    assert match(Command('unzip', 'unzip archive.zip -j')) == True

# Generated at 2022-06-14 09:42:56.684674
# Unit test for function match
def test_match():
    # It is a good zip file
    assert match(Command(script='unzip file.zip',
                         stderr='foo', stdout='bar')) is False
    # It is a good zip file
    assert match(Command(script='unzip file.zip -d blah',
                         stderr='foo', stdout='bar')) is False
    # It is a bad zip file
    assert match(Command(script='unzip file.zip',
                         stderr='foo', stdout='bar\nbar')) is True
    # It is a bad zip file
    assert match(Command(script='unzip file',
                         stderr='foo', stdout='bar\nbar')) is True
    # It is a bad zip file

# Generated at 2022-06-14 09:43:07.897315
# Unit test for function side_effect
def test_side_effect():
    archive = zipfile.ZipFile('test.zip', 'w')
    try:
        archive.write('test_unzip.py')
        archive.write('test_file.txt')
        archive.write('test_dir/test_file.txt')
        archive.write('test_dir/test_file_2.txt')
    finally:
        archive.close()

    old_cmd = type('', (object,), {'script': 'unzip test.zip',
                                   'script_parts': ['unzip', 'test.zip']})
    command = type('', (object,), {'script': 'unzip -d test test.zip',
                                   'script_parts': ['unzip', '-d', 'test',
                                                    'test.zip']})

    side_effect(old_cmd, command)

   

# Generated at 2022-06-14 09:43:20.406408
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command


# Generated at 2022-06-14 09:43:27.102918
# Unit test for function match
def test_match():
    assert _is_bad_zip('test_artifacts/test.zip')
    assert not _is_bad_zip('test_artifacts/test_ok.zip')
    assert match(Command('unzip test_artifacts/test.zip', '', ''))
    assert not match(Command('unzip -d test_artifacts/test.zip', '', ''))
    assert not match(Command('unzip test_artifacts/test_ok.zip', '', ''))



# Generated at 2022-06-14 09:43:34.690407
# Unit test for function match
def test_match():
    assert match(Command('unzip z.zip'))
    assert match(Command('unzip z.zip file'))
    assert match(Command('unzip z.zip file -x file'))
    assert not match(Command('unzip -d dir z.zip'))
    assert not match(Command('unzip -d dir z.zip file'))
    assert not match(Command('unzip -d dir z.zip file -x file'))

# Generated at 2022-06-14 09:43:41.348988
# Unit test for function match
def test_match():
    assert not match(Command('unzip archive.zip'))
    assert not match(Command('unzip archive.zip -d dir'))
    assert match(Command('unzip archive.zip document.txt'))
    assert match(Command('unzip archive.zip docume'))
    assert match(Command('unzip archive.zip document.txt other.txt'))

# Generated at 2022-06-14 09:43:51.133253
# Unit test for function side_effect
def test_side_effect():
    os.makedirs('/tmp/file1')
    os.makedirs('/tmp/file2')
    open('/tmp/file3', 'a').close()

    with open('/tmp/test.zip', 'a') as zipf:
        zf = zipfile.ZipFile(zipf, 'w')
        zf.write('/tmp/file1')
        zf.write('/tmp/file2')
        zf.write('/tmp/file3')
        zf.close()

    old_cmd = Command('unzip /tmp/test.zip')
    command = Command('unzip -d /tmp/test /tmp/test.zip')
    side_effect(old_cmd, command)
    os.rmdir('/tmp/file1')

# Generated at 2022-06-14 09:44:14.900575
# Unit test for function match
def test_match():
    assert(match(Command(script='unzip winpy2.7.zip -d winpy2.7',
                         stderr='Archive:  winpy2.7.zip\n'
                                ' error:  invalid zipfile signature\n'
                                ' (winpy2.7.zip)\n',
                         exit_code=1)))
    assert(match(Command(script='unzip winpy2.7.zip -d winpy2.7',
                         stderr='Archive:  winpy2.7.zip\n'
                                'End-of-central-directory signature not found.\n'
                                ' (winpy2.7.zip)\n',
                         exit_code=1)))

# Generated at 2022-06-14 09:44:27.491868
# Unit test for function side_effect
def test_side_effect():
    import os
    import tempfile
    zip_file = tempfile.NamedTemporaryFile(delete=False, suffix='.zip')
    zip_file.close()
    with zipfile.ZipFile(zip_file.name, 'w') as archive:
        archive.writestr('preexisting_dir/', '')
        archive.writestr('preexisting_dir/overwrite_me', 'some content')
        archive.writestr('preexisting_dir/dont_overwrite_me', 'another content')
        archive.writestr('overwrite_me', 'some content')
    os.makedirs('preexisting_dir')
    with open('preexisting_dir/dont_overwrite_me', 'w') as f:
        f.write('another content')
   

# Generated at 2022-06-14 09:44:32.902779
# Unit test for function side_effect
def test_side_effect():
    import os
    import tempfile
    import zipfile

# Generated at 2022-06-14 09:44:48.752839
# Unit test for function match
def test_match():
    from thefuck.types import Command

    # when unzip is used with -d flag (i.e. extracting to a directory), no
    # correction should be done
    assert not match(Command('unzip -d some.zip',
                             script='unzip -d some.zip'))

    # when unzip tries to extract two or more files to the current directory,
    # it will unzip to current directory by default. Thus, correction should be
    # done.
    assert match(Command('unzip some.zip', script='unzip some.zip'))

    # when unzip tries to extract one file, which is not a zip archive, it will
    # extract it anyway. Thus, correction should be done.
    assert match(Command('unzip some', script='unzip some'))

    # when unzip tries to extract one file, which is a

# Generated at 2022-06-14 09:44:52.195340
# Unit test for function match
def test_match():
    assert match(Command('unzip', 'unzip test_file.zip'))


# Generated at 2022-06-14 09:44:59.078468
# Unit test for function side_effect
def test_side_effect():
    import tempfile

    directory = tempfile.mkdtemp()
    os.chdir(directory)
    old_cmd = shell.and_('unzip file.zip', 'unzip file.zip file', 'unzip file')
    side_effect(old_cmd, 'unzip file.zip -d {}'.format(directory))
    assert os.path.exists(os.path.join(directory, 'file'))

# Generated at 2022-06-14 09:45:09.228113
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', None, None))
    assert match(Command('unzip file.zip non_existing_file', None, None))
    assert not match(Command('unzip -d dest file.zip', None, None))
    assert not match(Command('unzip -L file.zip', None, None))
    assert not match(Command('unzip -t file.zip', None, None))
    assert not match(Command('unzip file', None, None))



# Generated at 2022-06-14 09:45:16.895395
# Unit test for function side_effect
def test_side_effect():
    old_cmd = 'unzip test'
    command = 'unzip -d test_zip test'

    with open('test', 'w') as test:
        test.write('test')

    with zipfile.ZipFile('test_zip.zip', 'w') as test_zip:
        test_zip.writestr('test_2', 'test')
        test_zip.writestr('test_3', 'test')

    side_effect(old_cmd, command)

    assert not os.path.exists('test_zip.zip')
    assert os.path.exists('test_zip')
    assert os.path.exists('test_zip/test_2')
    assert os.path.exists('test_zip/test_3')
    assert not os.path.exists('test')

    os.remove

# Generated at 2022-06-14 09:45:27.182602
# Unit test for function match
def test_match():
    assert(match(Command('unzip')).is_disabled())
    assert(match(Command('unzip -l')).is_disabled())
    assert(match(Command('unzip -d')).is_disabled())
    assert(not match(Command('unzip -d foo.zip')))
    assert(not match(Command('unzip foo.zip')))
    assert(not match(Command('unzip foo')))
    assert(not match(Command('unzip foo.bar')))
    assert(match(Command('unzip foo.zip bar')))
    assert(match(Command('unzip foo bar')))
    assert(not match(Command('unzip foo bar baz')))
    assert(not match(Command('unzip foo baz')))
    assert(match(Command('unzip foo.zip bar baz')))

# Generated at 2022-06-14 09:45:36.536506
# Unit test for function side_effect
def test_side_effect():
    try:
        os.mkdir('a_dir')
        shell.and_('touch a_file')

        old_cmd = Command('unzip thefuck.zip', '')
        side_effect(old_cmd, 'unzip -d a_dir')

        # File has been deleted
        assert os.path.exists('a_file') == False

        # Directory can't been deleted
        assert os.path.exists('a_dir') == True

        # Clean up
        os.removedirs('a_dir')
    except:
        print("can't delete a_file")

    return 0

# Generated at 2022-06-14 09:46:13.498295
# Unit test for function side_effect
def test_side_effect():
    import os
    import tempfile
    import zipfile
    from thefuck.tests.utils import Command

    cwd = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    # Create a zip file with two files
    os.mknod('bar')
    os.mknod('baz')
    with zipfile.ZipFile('foo.zip', 'w') as f:
        f.write('bar')
        f.write('baz')

    # Create files before unzip
    os.mknod('bar')
    os.mkdir('baz')

    side_effect(Command('unzip foo.zip'), Command('unzip foo.zip'))
    assert not os.path.isfile('bar')

# Generated at 2022-06-14 09:46:22.702468
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    directory = tempfile.mkdtemp()
    filename = os.path.join(directory, 'my_file.zip')
    import shutil
    shutil.copyfile(os.path.join(os.path.dirname(__file__), 'test_side_effect.zip'), filename)
    os.chdir(directory)
    side_effect(None, None)
    files_in_dir = os.listdir(directory)
    os.remove(filename)
    shutil.rmtree(directory)
    assert files_in_dir == ['toto', 'titi']

# Generated at 2022-06-14 09:46:31.222864
# Unit test for function side_effect
def test_side_effect():

    # create a temporary directory
    tmp_dir = tempfile.mkdtemp()

    # copy the files from the package's 'test' directory to the temporary directory
    for f in ['File.java', 'Foo.java', 'Foo2.java']:
        shutil.copy(os.path.join('test', f), tmp_dir)

    os.chdir(tmp_dir)
    try:
        side_effect('unzip a.zip', 'unzip a.zip -d a')
        assert not os.path.exists('File.java')
        assert not os.path.exists('Foo.java')
        assert not os.path.exists('Foo2.java')
    finally:
        os.chdir('..')

# Generated at 2022-06-14 09:46:38.242593
# Unit test for function match
def test_match():
    command1 = "unzip -q ~/bad.zip"
    command2 = "unzip -q ~/bad.zip -d ~/output"
    command3 = "unzip -q ~/bad.zip -d ~/"
    assert match(command1)
    assert not match(command2)
    assert not match(command3)



# Generated at 2022-06-14 09:46:42.437918
# Unit test for function side_effect
def test_side_effect():
    from thefuck.shells import get_shell
    # First we create zip file with content
    zip_file = './test_side_effect.zip'
    with zipfile.ZipFile(zip_file, 'w') as zip_archive:
        zip_archive.writestr('test_side_effect.txt', 'test_side_effect')

    # Then we create some files
    get_shell().run('touch ./test_side_effect.txt')
    get_shell().run('mkdir ./test_side_effect')

    # Now we can always run the function
    _side_effect(zip_file)

# Generated at 2022-06-14 09:46:53.596391
# Unit test for function side_effect
def test_side_effect():
    # Command to to run side_effect with
    import tempfile
    dirName = tempfile.mkdtemp()
    old_cmd = Command('unzip %s -d %s' % ('dummyarchive.zip', dirName))
    comm = get_new_command(old_cmd)
    shell = Shell()
    # Make sure the file is there to begin with
    f1 = open(dirName + '/dummyfile', 'w')
    f1.close()
    side_effect(old_cmd, comm)
    # Make sure the file was removed
    if os.path.isfile(dirName + '/dummyfile'):
        raise Exception('The file wasn\'t removed')

# Generated at 2022-06-14 09:47:07.347399
# Unit test for function side_effect
def test_side_effect():
    import os
    import shutil
    import tempfile
    import zipfile

    created_files = []

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpfile = os.path.join(tmpdir, 'file.zip')
        dirname = os.path.join(tmpdir, 'dir')
        os.mkdir(dirname)
        with open(os.path.join(tmpdir, 'test'), 'w') as test:
            test.write('test')
        with open(os.path.join(dirname, 'test'), 'w') as test:
            test.write('test2')
        with zipfile.ZipFile(tmpfile, 'w') as archive:
            archive.write(os.path.join(tmpdir, 'test'))

# Generated at 2022-06-14 09:47:16.765438
# Unit test for function side_effect
def test_side_effect():
    """
    Create a blank zip archive, unzip it and check that there are no more
    files left in the directory
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    tmp_dir = tempfile.mkdtemp()
    os.chdir(tmp_dir)

    zip_file = os.path.join(tmp_dir, 'test.zip')

    with zipfile.ZipFile(zip_file, 'w') as archive:
        archive.writestr('test/test.txt', b'')
    os.system('unzip {}'.format(zip_file))

    # Unzip test.txt

# Generated at 2022-06-14 09:47:25.959222
# Unit test for function match
def test_match():
    assert match(Command('unzip', 'unzip a.zip')) == False
    assert match(Command('unzip', 'unzip a.zip -d a')) == False
    assert match(Command('unzip', 'unzip a.zip -d a.zip')) == True
    assert match(Command('unzip', 'unzip a.zip -d a.zip -d a')) == False
    assert match(Command('unzip', 'unzip a.zip -d ../a')) == True

# Generated at 2022-06-14 09:47:31.966824
# Unit test for function match
def test_match():
    # Case 1: 'unzip file.zip'
    assert match(Command(script='unzip file', stdout=''))
    # Case 2: 'unzip file.zip -d dir'
    assert not match(Command(script='unzip file -d dir', stdout=''))
    # Case 3: 'unzip file.zip -d dir'
    assert not match(Command(script='unzip file file2 -d dir', stdout=''))



# Generated at 2022-06-14 09:48:35.998806
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    import os
    import zipfile
    dirname = tempfile.mkdtemp()
    shutil.copytree('tests/res/zip_directory', os.path.join(dirname, 'zip'))

    old_cmd = 'cd {} && unzip -d zip_extracted zip/zip_directory.zip'.format(dirname)
    command = 'cd {} && unzip -d zip_extracted zip/zip_directory.zip'.format(dirname)
    output = side_effect(old_cmd, command)
    assert output == None
    assert zipfile.is_zipfile(os.path.join(dirname, 'zip', 'zip_directory.zip'))

# Generated at 2022-06-14 09:48:49.292187
# Unit test for function side_effect
def test_side_effect():

    from os import getcwd
    from os.path import join
    from tempfile import mkdtemp
    from shutil import rmtree
    from unittest import TestCase

    from .shell import Bash

    class SideEffectTest(TestCase):
        def setUp(self):
            self.tmp = mkdtemp()
            self.path = join(self.tmp, 'a')
            os.mkdir(self.path)
            self.file = join(self.path, 'b')
            open(self.file, 'a').close()

        def tearDown(self):
            rmtree(self.tmp)

        def test_side_effect(self):
            with zipfile.ZipFile(join(self.tmp, 'a.zip'), 'w') as archive:
                archive.write(self.file, 'b')

# Generated at 2022-06-14 09:48:58.821259
# Unit test for function side_effect
def test_side_effect():
    old_cmd = type('old_cmd', (object,),  {'script': 'unzip a.zip',
                                           'script_parts': ['unzip', 'a.zip']})()
    command = type('command', (object,),  {'script': 'unzip -d a a.zip',
                                           'script_parts': ['unzip', '-d', 'a', 'a.zip']})()
    test_dir = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(os.path.join(test_dir, 'a')):
        os.mkdir(os.path.join(test_dir, 'a'))

# Generated at 2022-06-14 09:49:08.210452
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil

    # Create a temporary directory:
    tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 09:49:13.563244
# Unit test for function side_effect
def test_side_effect():
    from thefuck.rules.unzip_in_the_same_folder import side_effect

    old_cmd = shell.And('unzip', 'a.zip')
    command = u'unzip -d {}'.format(shell.quote('a'))
    side_effect(old_cmd, command)
    assert len(os.listdir('.')) == 0

    old_cmd = shell.And('unzip', 'b.zip')
    command = u'unzip -d {}'.format(shell.quote('b'))
    side_effect(old_cmd, command)
    assert len(os.listdir('.')) == 1
    assert 'b' in os.listdir('.')
    assert not os.path.isfile('b')
    assert os.path.isdir('b')

# Generated at 2022-06-14 09:49:26.537212
# Unit test for function side_effect
def test_side_effect():
    import unittest
    import shutil
    # initialize, create temp directory and create a zip file
    test_dir = "/tmp/thefuck_zip_unzip_test"
    test_zip = "/tmp/thefuck_zip_unzip_test.zip"
    test_file = "/tmp/thefuck_zip_unzip_test/test_file"
    test_directory = "/tmp/thefuck_zip_unzip_test/test_directory"
    os.mkdir(test_dir)
    os.mkdir(test_directory)
    with open(test_file, "w") as f:
        f.write("test")

    with zipfile.ZipFile(test_zip, "w") as z:
        z.write(test_file)
        z.write(test_directory)

    # execute the side

# Generated at 2022-06-14 09:49:40.030805
# Unit test for function side_effect
def test_side_effect():
    from thefuck.rules.unzip_bad_cmd import side_effect
    from thefuck.shells import get_shell
    import tempfile
    import shutil

    with tempfile.TemporaryDirectory() as tmpdir:
        open('unittest.zip', 'a').close()
        zipf = zipfile.ZipFile('unittest.zip', 'w', zipfile.ZIP_DEFLATED)
        zipf.write(__file__, 'unittest.txt')
        zipf.write(__file__, os.path.join(tmpdir, 'unittest.txt'))
        zipf.close()
        old_cmd = get_shell().and_('unzip', 'unittest.zip')

        side_effect(old_cmd, old_cmd)


# Generated at 2022-06-14 09:49:43.251517
# Unit test for function match
def test_match():
    from tests.utils import Command

    assert not match(Command('unzip file.zip filename'))
    assert not match(Command('unzip -d file.zip filename'))
    assert not match(Command('unzip file.zip'))
    assert match(Command('unzip bad-file.zip'))



# Generated at 2022-06-14 09:49:55.248619
# Unit test for function match
def test_match():
    assert not match(Command(script='unzip file.zip -d folder',
                             stderr='unzip:  cannot find or open folder.zip, folder.ZIP or folder.z'))
    assert match(Command(script='unzip file.zip',
                         stderr='unzip:  cannot find or open file.zip, file.ZIP or file.z'))
    assert not match(Command(script='unzip file.zip -d folder',
                             stderr='unzip:  cannot find or open folder.zip'))
    assert not match(Command(script='unzip file.zip -d folder',
                             stderr='unzip:  cannot find or open folder.zip, folder.ZIP'))

# Generated at 2022-06-14 09:49:59.188189
# Unit test for function side_effect
def test_side_effect():
    from tempfile import TemporaryDirectory
    from shutil import make_archive, copyfile
    from os import remove
    from os.path import join

    with TemporaryDirectory() as tmp_dir:
        zip_name = join(tmp_dir, 'zippy.zip')
        dir_name = join(tmp_dir, 'dir')
        file_name = join(dir_name, 'file')
        copyfile('tests/fixtures/unzip_match.py', file_name)
        make_archive(zip_name[:-4], 'zip', root_dir=dir_name)

        side_effect(FakeCommand(u'unzip {} -d {}'.format(zip_name, dir_name)), None)

        # just making sure the side effect has run fine
        assert not os.path.exists(file_name)
        assert not os