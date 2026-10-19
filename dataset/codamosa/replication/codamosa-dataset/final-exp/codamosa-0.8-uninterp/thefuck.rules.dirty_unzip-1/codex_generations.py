

# Generated at 2022-06-14 09:41:06.777614
# Unit test for function side_effect
def test_side_effect():
    # create temporary file
    tf = tempfile.NamedTemporaryFile(delete=False)
    with tf:
        tf.write('test'.encode('utf-8'))
        # set the file as unzip file
        old_cmd = Command('unzip ' + tf.name, tf.name + ':test')
    # set up the new command
    command = get_new_command(old_cmd)
    # execute side_effect
    side_effect(old_cmd, command)
    assert os.path.isfile(tf.name) == False

# Generated at 2022-06-14 09:41:13.558994
# Unit test for function side_effect
def test_side_effect():
    os.system('touch test_file')
    command = 'echo "test" >> test_file && zip test_file.zip test_file && unzip test_file -d test/'
    old_cmd = 'unzip test_file -d test/'
    side_effect(old_cmd, command)
    file_exists = os.path.exists('test_file')
    os.remove('test_file')
    os.remove('test_file.zip')
    assert(file_exists == False)

# Generated at 2022-06-14 09:41:26.265806
# Unit test for function side_effect
def test_side_effect():
    # Create a temporary directory
    import tempfile
    dirpath = tempfile.mkdtemp()

# Generated at 2022-06-14 09:41:33.997616
# Unit test for function side_effect

# Generated at 2022-06-14 09:41:48.478969
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    from thefuck.shells import shell, get_alias
    from thefuck.types import Command
    import os

    pwd = os.path.abspath(os.getcwd())

    # Temporary directory
    tmpdir = tempfile.mkdtemp()

    # Change directory to tmpdir
    os.chdir(tmpdir)

    # Create 2 files, one directory, and one bad zipfile
    os.makedirs('bar')

    with open('foo', 'w') as f:
        f.write('foo')

    with open('baz', 'w') as f:
        f.write('baz')

    with zipfile.ZipFile('qux.zip', 'w') as z:
        z.write('qux1')
        z.write('qux2')

# Generated at 2022-06-14 09:42:00.340793
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil

    tempdir = tempfile.mkdtemp()


# Generated at 2022-06-14 09:42:14.007350
# Unit test for function side_effect
def test_side_effect():
    # create a temp dir
    os.mkdir('temp_dir')

    # create some test files
    with open('temp1.txt', 'w') as file:
        file.write('file1')
    with open('temp2.txt', 'w') as file:
        file.write('file2')
    with open('temp3.txt', 'w') as file:
        file.write('file3')
    with open('temp4.txt', 'w') as file:
        file.write('file4')
    with open('temp_dir/temp5.txt', 'w') as file:
        file.write('file5')

    # create a zip file
    zip_file = zipfile.ZipFile('temp.zip', 'w')
    zip_file.write('temp1.txt', 'temp1.txt')


# Generated at 2022-06-14 09:42:19.667503
# Unit test for function match
def test_match():
    assert match(Command('unzip -x file.zip', '')) is False
    assert match(Command('unzip -x file.zip file1.txt', '')) is True
    assert match(Command('unzip -x file.zip -d /tmp/random place', '')) is True
    assert match(Command('unzip -x file.zip -d /tmp', '')) is False


# Generated at 2022-06-14 09:42:26.668600
# Unit test for function side_effect
def test_side_effect():
    path = '/tmp/test/script'
    open(path, 'w').close()
    old_cmd = Mock(script='unzip test.zip', script_parts=['unzip', 'test.zip'])
    side_effect(old_cmd, Mock(script='unzip test.zip -d test'))

    assert not os.path.exists(path)

# Generated at 2022-06-14 09:42:35.266298
# Unit test for function side_effect
def test_side_effect():
    # Test if side_effect works correctly
    os.chdir('tests/testdata/')
    old_cmd = shell.and_('', 'unzip', 'test.zip')
    side_effect(old_cmd, '')
    test_file = open ('test.txt', 'r')
    contents = test_file.read()
    test_file.close()
    assert contents == 'Testing the unzip command'
    os.remove('test.txt')

# Generated at 2022-06-14 09:42:51.312272
# Unit test for function side_effect
def test_side_effect():
    cmd = 'unzip test.zip'
    old_cmd = 'unzip test.zip test.txt'
    with zipfile.ZipFile('test.zip', 'w') as myzip:
        myzip.write('test.txt')
    assert side_effect(old_cmd, cmd) is None

# Generated at 2022-06-14 09:43:04.201053
# Unit test for function side_effect
def test_side_effect():
    os.makedirs(u'foolib')
    with open(u'foolib/foo.txt', 'w') as f:
        f.write(u'foo')

    try:
        with zipfile.ZipFile(u'dummy.zip', 'w') as archive:
            archive.write(u'foolib/foo.txt')

        # Delete the extracted file to check that it is successfully replaced
        os.remove(u'foolib/foo.txt')

        side_effect(Command('unzip foo.zip', '', None), Command('unzip -d foo.zip'))

        with open(u'foolib/foo.txt', 'r') as f:
            assert f.read() == u'foo'
    finally:
        os.remove(u'dummy.zip')

# Generated at 2022-06-14 09:43:07.674004
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip'))
    assert match(Command('unzip file.zip file2.zip'))
    assert not match(Command('unzip -d file.zip'))
    assert not match(Command('zip file.zip'))


# Generated at 2022-06-14 09:43:18.190087
# Unit test for function match
def test_match():
    # Bad zip without directory specified
    assert match(Command('unzip test.zip', None))
    # Bad zip with directory specified
    assert match(Command('unzip test.zip -d test/', None))
    # Bad zip with directory specified and other flags
    assert match(Command('unzip test.zip -d test/ -q -foobar', None))
    # Good zip without directory specified
    assert not match(Command('unzip foo.zip', None))
    # Good zip with directory specified
    assert not match(Command('unzip foo.zip -d foo/', None))
    # Good zip with directory specified and other flags
    assert not match(Command('unzip foo.zip -d foo/ -q -foobar', None))

# Generated at 2022-06-14 09:43:26.980381
# Unit test for function match
def test_match():
    if os.path.isfile('test.zip'):
        os.remove('test.zip')
    if os.path.isfile('test'):
        os.remove('test')
    with zipfile.ZipFile('test.zip', 'w') as archive:
        archive.writestr('test', 'test')
        archive.writestr('unzip.py', 'unzip.py')

    # unzip -d test.zip
    assert not match(Command(script='unzip -d test.zip', stderr='', stdout='',
                             stdin='', env={}, shell='bash', use_shell=True))

    # unzip test.zip

# Generated at 2022-06-14 09:43:39.514671
# Unit test for function side_effect
def test_side_effect():
    import mock
    import tempfile
    import shutil

    with tempfile.TemporaryDirectory() as directory:
        zip_file = os.path.join(directory, 'zip_file.zip')
        file = os.path.join(directory, 'file')
        with open(file, 'w') as f:
            f.write('')

        with zipfile.ZipFile(zip_file, 'w') as archive:
            archive.write(file)

        shell_mock = mock.MagicMock(spec=shell)
        side_effect(mock.Mock(script_parts=['unzip', zip_file]),
                    mock.Mock(script='unzip -d {}'.format(directory)))
        assert not shell_mock.and_input.called

        shutil.rmtree(directory)


# Generated at 2022-06-14 09:43:44.522701
# Unit test for function side_effect
def test_side_effect():
    cmd = MagicMock(script=u'unzip -d test_dir test.zip',
                    script_parts=[u'unzip', '-d', 'test_dir', 'test.zip'])
    side_effect(cmd, 'unzip -d test_dir test.zip')
    pass

# Generated at 2022-06-14 09:43:56.184932
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    zip_file = tempfile.NamedTemporaryFile()
    dir_name = tempfile.mkdtemp()

# Generated at 2022-06-14 09:44:05.197694
# Unit test for function match
def test_match():
    # case 1, result is true
    assert match(Command('unzip -x', stderr='error:  cannot find zipfile directory in one of test1.zip'))

    # case 2, result is false
    assert not match(Command('unzip -x', stderr='error:  cannot find zipfile directory in one of tes.zip'))

    # case 3, result is true
    assert match(Command('unzip -x', stderr='error:  cannot find zipfile directory in one of test1.zip1'))

    # case 4, result is true
    assert match(Command('unzip -x', stderr='error:  cannot find zipfile directory in one of test1.zip.zip'))



# Generated at 2022-06-14 09:44:18.294922
# Unit test for function side_effect
def test_side_effect():
    with zipfile.ZipFile('test_zip.zip', 'w') as zf:
        zf.writestr('hello.txt', b'world')
        zf.writestr('positioned/hello.txt', b'world')

    def _check_result(expected):
        assert os.path.exists('hello.txt')
        assert os.path.exists('positioned/hello.txt') == expected


# Generated at 2022-06-14 09:44:46.266533
# Unit test for function match
def test_match():
    assert match(u'unzip foo.zip')


# Generated at 2022-06-14 09:44:48.252618
# Unit test for function match
def test_match():
    command = Command('unzip Archive.zip')
    assert match(command)
    assert not match(command)

# Generated at 2022-06-14 09:44:55.001668
# Unit test for function side_effect
def test_side_effect():
    fd, path = tempfile.mkstemp()
    zip_file = zipfile.ZipFile(path, 'w')
    zip_file.writestr('file.txt', 'some content')
    zip_file.close()
    os.close(fd)

    # We have to overwrite the current directory with tempfile.mkdtemp()
    # because our function can't overwrite files in the current directory
    # outside of our function.
    temp_dir = tempfile.mkdtemp()
    current_dir = os.getcwd()

# Generated at 2022-06-14 09:45:06.258227
# Unit test for function match
def test_match():
    from thefuck.types import Command

    zip_file = Command('unzip test.zip',
                       '  End-of-central-directory signature not found.  Either this file is not\n  a zipfile, or it constitutes one disk of a multi-part archive.  In the\n  latter case the central directory and zipfile comment will be found on\n  the last disk(s) of this archive.\nunzip:  cannot find zipfile directory in one of test.zip or\n        test.zip.zip, and cannot find test.zip.ZIP, period.')
    assert not match(zip_file)


# Generated at 2022-06-14 09:45:19.646205
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('unzip dummy.zip', 'unzip:  cannot find or open dummy.zip'))
    assert match(Command('unzip dummy', 'unzip:  cannot find or open dummy'))
    assert match(Command('unzip dummy.zip', 'unzip:  cannot find or open dummy.zip.zip'))
    assert not match(Command('unzip dummy.zip', 'unzip:  cannot find or open dumm.yzip'))
    assert not match(Command('unzip dummy.zip', 'unzip:  cannot find or open dummy.zip', stderr='unzip:  cannot find or open dummy.zip.zip'))

# Generated at 2022-06-14 09:45:28.205306
# Unit test for function side_effect
def test_side_effect():
    _zip_file = zipfile.ZipFile('test_file.zip', 'w')
    _zip_file.writestr('test_file', 'hello')
    _zip_file.close()

    with open('test_file', 'w') as _file:
        _file.write('bye')

    # Mock the command because we don't have the zip file in the shell
    # 'unzip test_file.zip'
    _command = type('Command', (object,), {
        'script': 'unzip test_file.zip'
    })

    side_effect(_command, 'unzip test_file.zip test_file')
    assert open('test_file').read() == 'hello'

    # Clean up
    os.remove('test_file')
    os.remove('test_file.zip')


# Unit

# Generated at 2022-06-14 09:45:32.164197
# Unit test for function side_effect
def test_side_effect():
    output = os.getcwd() + '/fucker.txt'
    shell.and_('touch {}'.format(shell.quote(output)))
    side_effect(None, None)
    assert not os.path.exists(output)

# Generated at 2022-06-14 09:45:41.154816
# Unit test for function match
def test_match():
    os.chdir(os.path.expanduser('~/Downloads'))

    # Good zip
    zip_file = 'good_zipfile'
    _create_zip(zip_file, ['test/test.txt'])
    assert match(Command('unzip {}'.format(zip_file), '', '')) is False
    os.remove(zip_file)

    # Bad zip
    zip_file = 'bad_zipfile'
    _create_zip(zip_file, ['test/test.txt', 'test.txt'])
    assert match(Command('unzip {}'.format(zip_file), '', '')) is True
    os.remove(zip_file)



# Generated at 2022-06-14 09:45:57.290721
# Unit test for function side_effect
def test_side_effect():
    parent_dir = 'parent'
    file_to_be_removed = 'file_to_be_removed'
    file_to_be_unchanged = 'file_to_be_unchanged'
    dir_to_be_saved = 'dir_to_be_saved'
    file_to_be_saved = 'file_to_be_saved'
    zip_file_name = 'file.zip'

    os.mkdir(parent_dir)
    os.chdir(parent_dir)
    open(file_to_be_removed, 'w').close()
    open(file_to_be_unchanged, 'w').close()
    os.mkdir(dir_to_be_saved)

# Generated at 2022-06-14 09:46:12.653633
# Unit test for function match
def test_match():
    res = match(Command(script='unzip file.zip', stderr=''))
    assert(res == False)
    res = match(Command(script='unzip file.zip', stderr='error:  file not found or no read permission'))
    assert(res == False)
    res = match(Command(script='unzip file.zip', stderr='End-of-central-directory signature not found.  Either this file is not\na zipfile, or it constitutes one disk of a multi-part archive.  In the\n'))
    assert(res == True)
    res = match(Command(script='unzip -d test dir.tar.zip', stderr='unzip:  cannot find or open dir.tar.zip, dir.tar.zip.zip or dir.tar.zip.ZIP.'))

# Generated at 2022-06-14 09:46:49.582744
# Unit test for function side_effect
def test_side_effect():
    # Test side effect when archive is empty
    old_cmd = MagicMock(script='unzip test_archive.zip')
    test_archive_name = 'test_archive.zip'
    test_contents = MagicMock()
    side_effect_archive = zipfile.ZipFile(test_archive_name, 'w')
    side_effect_archive.writestr('test_file.txt', test_contents)
    side_effect(old_cmd, '')
    with open('test_file.txt', 'r') as test_file:
        assert test_file.read() == test_contents
    os.remove(test_archive_name)
    os.remove('test_file.txt')

    # Test side effect when archive is not empty

# Generated at 2022-06-14 09:46:58.149056
# Unit test for function match
def test_match():
    assert match(Command("""unzip bomb.zip""",
            """Archive:  bomb.zip
  inflating: bomb.txt""", "")) is True
    assert match(Command("""unzip bomb.zip -d bomb""",
            """Archive:  bomb.zip
  inflating: bomb.txt""", """bomb/bomb.txt""", "")) is False
    assert match(Command("""unzip bomb.zip""",
            """bomb.zip: option -d not recognized""", "")) is False


# Generated at 2022-06-14 09:47:07.970920
# Unit test for function side_effect
def test_side_effect():
    test_dir = tempfile.mkdtemp(prefix="zip_test_")
    old_dir = os.getcwd()
    os.chdir(test_dir)

    # create file
    with open('f', 'w') as f:
        f.write('content')
    # create dir
    os.mkdir('d')
    # create nested dir
    os.makedirs('d/nested')
    # create nested file
    with open('d/nested/f', 'w') as f:
        f.write('content')

    # create zip
    with zipfile.ZipFile('z', 'w') as z:
        z.write('f')
        z.write('d/nested/f')

    # remove files
    os.remove('f')

# Generated at 2022-06-14 09:47:10.924397
# Unit test for function match
def test_match():
    assert match(Command('unzip arch.zip file1.txt', '', '', 0))



# Generated at 2022-06-14 09:47:17.971449
# Unit test for function match
def test_match():
    # The unzip command without the -d option should match
    assert match(Command('unzip', 'unzip filename.zip'))
    # The unzip command with the -d option should not match
    assert not match(Command('unzip', 'unzip -d some/directory filename.zip'))
    # The unzip command without arguments should not match
    assert not match(Command('unzip', 'unzip'))



# Generated at 2022-06-14 09:47:22.138487
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', ''))
    assert not match(Command('unzip -d file.zip', ''))

# Tests for function get_new_command

# Generated at 2022-06-14 09:47:28.485220
# Unit test for function match
def test_match():
    assert not match(Command('unzip', '~/Downloads/thefuck-3.6.tar.gz'))
    assert match(Command('unzip', '~/Downloads/thefuck-3.6.tar.gz.zip'))
    assert match(Command('unzip', '~/Downloads/thefuck-3.6.tar.gz.zip', '-d', '~/Downloads/'))

# Generated at 2022-06-14 09:47:38.085669
# Unit test for function match
def test_match():
    command = type('Command', (object,), {'script': 'unzip'})
    assert match(command) == False

    command = type('Command', (object,), {'script': 'unzip -d'})
    assert match(command) == False

    command = type('Command', (object,), {'script': 'unzip test.zip'})
    assert match(command) == True

    command = type('Command', (object,), {'script': 'unzip test'})
    assert match(command) == True

    command = type('Command', (object,), {'script': 'unzip test.zip test.py'})
    assert match(command) == True


# Generated at 2022-06-14 09:47:49.053274
# Unit test for function side_effect
def test_side_effect():
    """
    Check if the side effect works when the files are just created

    """
    # create a file example.txt
    with open("example.txt", "w") as file:
        file.write("This is a test")
    # create a dir example_dir
    os.makedirs("example_dir")
    # create a file inside the dir
    with open("example_dir/example.txt", "w") as file:
        file.write("This is a test")

    # check if content is successfully written to the file
    with open("example.txt", "r") as file:
        assert file.read() == "This is a test"

    # check if content is successfully written to the file inside the dir

# Generated at 2022-06-14 09:47:54.459194
# Unit test for function match
def test_match():
    # Output of command unzip
    output1 = "Archive: test.zip\n  inflating: test"
    output2 = "Archive: test.zip\n   creating: test/\n  inflating: test/test"
    # Command that was executed
    command1 = "unzip test"
    command2 = "unzip test.zip"

    assert match(Command(command1, output1))
    assert not match(Command(command2, output2))

# Generated at 2022-06-14 09:48:59.239890
# Unit test for function side_effect
def test_side_effect():
    with NamedTemporaryFile() as f:
        with zipfile.ZipFile(f.name, mode='w') as z:
            z.writestr("test", "")

        # We need to change working dir here because
        # side_effect function checks if file is inside current dir
        with TemporaryDirectory() as d:
            os.chdir(d)
            command = Command(script='unzip {}'.format(os.path.basename(f.name)))

            side_effect(command, Command(script='unzip -d {} {}'.format(os.path.basename(f.name)[:-4], os.path.basename(f.name))))

            # Unzip command with -d flag writes files under current dir
            assert os.path.exists(os.path.join(d, 'test'))

# Generated at 2022-06-14 09:49:00.131532
# Unit test for function side_effect
def test_side_effect():
    # TODO
    pass

# Generated at 2022-06-14 09:49:09.224029
# Unit test for function match
def test_match():
    assert not match(Command('unzip ~/Downloads/test.zip',
                    'unzip:  cannot find or open ~/Downloads/test.zip, ~/Downloads/test.zip.zip or ~/Downloads/test.zip.ZIP.'))
    assert match(Command('unzip test.zip', 'unzip:  cannot find or open test.zip, test.zip.zip or test.zip.ZIP.'))
    assert not match(Command('unzip -d ~/Downloads/test test.zip', 'unzip:  cannot find or open test.zip, test.zip.zip or test.zip.ZIP.'))
    assert not match(Command('unzip -d test ~/Downloads/test.zip', 'unzip:  cannot find or open test.zip, test.zip.zip or test.zip.ZIP.'))

# Generated at 2022-06-14 09:49:20.498060
# Unit test for function side_effect
def test_side_effect():
    tmp_dir = tempfile.mkdtemp()
    class FakeCmd(object):
        def __init__(self):
            self.script_parts = ['unzip', 'test.zip']

    old_cmd = FakeCmd()
    os.chdir(tmp_dir)
    with tempfile.NamedTemporaryFile(dir=tmp_dir) as zipf:
        zipf.write('foo')
        zipf.seek(0)
        with zipfile.ZipFile(zipf) as archive:
            archive.extract('foo', tmp_dir)
        side_effect(old_cmd, None)
        assert os.path.exists('foo') is False

# Generated at 2022-06-14 09:49:26.858512
# Unit test for function match
def test_match():
    # Test no zip
    zip_file = 'unzip'
    assert _is_bad_zip(zip_file) is None

    # Test good zip
    zip_file = 'unzip'
    assert _is_bad_zip(zip_file) is None

    # Test no zip
    zip_file = 'unzip.zip'
    assert _is_bad_zip(zip_file) is None

# Generated at 2022-06-14 09:49:33.947180
# Unit test for function match
def test_match():
    from thefuck.types import Command

    # Successful match
    command = Command('unzip file.zip')
    assert match(command)

    # Failure match
    command = Command('unzip -d folder file.zip')
    assert not match(command)

    # Zip file does not exist
    command = Command('unzip file2.zip')
    assert not match(command)



# Generated at 2022-06-14 09:49:40.384331
# Unit test for function side_effect
def test_side_effect():
    from thefuck.shells import Bash
    from thefuck.shells.bash import BashQuote, QuoteContext
    import mock

    args = {'script': 'unzip test.zip'}
    old_cmd = mock.MagicMock(**args)

    side_effect(old_cmd, [])

    BashQuote.quote_context.assert_called_once_with(QuoteContext.inner)
    Bash.from_shell.assert_called_once_with([
        'rm', '-f', Bash.from_shell.return_value])

# Generated at 2022-06-14 09:49:46.586801
# Unit test for function side_effect
def test_side_effect():
    # Create the zip file, zip it and delete the created directory
    with zipfile.ZipFile('test_file.zip', 'w') as test_zip:
        test_zip.writestr('test_file', 'test_content')
    os.mkdir(u'test_dir')
    with open('test_dir/test_file', 'w') as test_file:
        test_file.write('test content')

    # This will raise an OSError if the function does not work properly
    side_effect(None, None)

    os.remove('test_file.zip')
    os.remove('test_file')
    os.rmdir('test_dir')

# Generated at 2022-06-14 09:49:57.874201
# Unit test for function side_effect
def test_side_effect():
    import tempfile

    with tempfile.NamedTemporaryFile() as temp1:
        with tempfile.NamedTemporaryFile() as temp2:
            with tempfile.NamedTemporaryFile() as temp3:
                temp1.write("Some content")
                temp1.flush()
                temp2.write("Some other content")
                temp2.flush()
                temp3.write("Some other new content")
                temp3.flush()
                path = tempfile.mkdtemp()
                with tempfile.NamedTemporaryFile(suffix='.zip') as archive:
                    zip = zipfile.ZipFile(archive.name, 'w')
                    zip.write(temp1.name, temp1.name.split('/')[-1])

# Generated at 2022-06-14 09:50:10.429682
# Unit test for function side_effect
def test_side_effect():
    zip_file = 'files.zip'
    files = ['a', 'b/c', 'd/e/f']
    with zipfile.ZipFile(zip_file, 'w') as archive:
        for file in files:
            archive.writestr(file, b'')

    new_cmd = u'unzip -d {} {}'.format(shell.quote(zip_file[:-4]), zip_file)
    old_cmd = u'unzip {}'.format(zip_file)

    side_effect(old_cmd, new_cmd)

    for file in files:
        if os.path.split(file)[0] == '':
            # does not try to remove directories as we cannot know if they
            # already existed before
            continue

        assert not os.path.isfile(file)