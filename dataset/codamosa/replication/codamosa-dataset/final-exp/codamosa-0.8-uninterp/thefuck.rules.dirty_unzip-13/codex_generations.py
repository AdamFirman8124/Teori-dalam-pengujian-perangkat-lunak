

# Generated at 2022-06-14 09:41:08.032463
# Unit test for function match
def test_match():
    assert match(Command('', ''))
    assert match(Command('unzip file.zip', ''))
    assert match(Command('unzip -x file.zip', ''))
    assert match(Command('unzip -x file', ''))
    assert match(Command('unzip -x file.zip file', ''))
    assert match(Command('unzip file', ''))
    assert not match(Command('unzip -x file.zip -d dir', ''))
    assert not match(Command('unzip -d dir file.zip', ''))

# Generated at 2022-06-14 09:41:15.338391
# Unit test for function match
def test_match():
    assert match(Command(script='unzip',
                         stderr=u'error:  expected one archive member'))

    assert not match(Command(script='unzip',
                             stderr=u'error:  expected one archive member',
                             stdout=u'dir1/file1'))

    assert match(Command(script='unzip -d dir file.zip',
                         stderr=u'error:  expected one archive member'))

    assert not match(Command(script='unzip -d dir file.zip',
                             stderr=u'error:  expected one archive member',
                             stdout=u'dir1/file1'))

# Generated at 2022-06-14 09:41:24.849865
# Unit test for function side_effect
def test_side_effect():
    global zip_file
    with zipfile.ZipFile('/tmp/test.zip', 'w') as archive:
        archive.writestr('/tmp/file1.txt', b'data')

    side_effect('unzip /tmp/test.zip', 'unzip -d /tmp/test.zip')
    assert os.path.isfile('/tmp/file1.txt')

    os.remove('/tmp/file1.txt')
    with open('/tmp/file1.txt', 'w') as f:
        f.write('old data')
    side_effect('unzip /tmp/test.zip', 'unzip -d /tmp/test.zip')
    assert os.path.isfile('/tmp/file1.txt')

# Generated at 2022-06-14 09:41:26.018268
# Unit test for function match
def test_match():
    assert not match(Command(script='unzip'))
    assert not match(Command(script='unzip -l archive.zip'))
    assert not match(Command(script='unzip -d directory'))

# Generated at 2022-06-14 09:41:33.927448
# Unit test for function match
def test_match():
    assert match(Command('unzip test.zip'))
    assert match(Command('unzip test.zip -d test'))
    assert not match(Command('unzip -d test test.zip'))
    assert not match(Command('unzip -d test test.zip test2.zip'))
    assert not match(Command('unzip -d test test.zip test2.zip test3.zip'))
    assert not match(Command('unzip -d test test.zip test2.zip test3.zip test4.zip'))
    assert not match(Command('unzip -d test test.zip test2.zip test3.zip test4.zip test5.zip'))
    assert match(Command('unzip -d test.zip test.zip test2.zip test3.zip test4.zip test5.zip'))


# Unit

# Generated at 2022-06-14 09:41:34.710106
# Unit test for function side_effect
def test_side_effect():
    pass

# Generated at 2022-06-14 09:41:45.183536
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import zipfile

    with tempfile.NamedTemporaryFile() as test_zip:
        with zipfile.ZipFile(test_zip.name, 'w') as archive:
            archive.write('thefuck/utils.py')
            archive.write('thefuck/utils.pyc')
            archive.write('thefuck/../setup.py')

        old_cmd = type('test_command', (object,), {
            'script': 'unzip {}'.format(test_zip.name),
            'script_parts': [
                'unzip', '{}'.format(test_zip.name)]})

# Generated at 2022-06-14 09:41:57.698385
# Unit test for function side_effect
def test_side_effect():
    with zipfile.ZipFile('/tmp/test.zip', 'w') as archive:
        archive.writestr('test/test1', '')
        archive.writestr('test/test2', '')
        archive.writestr('test/test3', '')
        archive.writestr('test/test4', '')

    assert not os.path.exists('/tmp/test')
    os.makedirs('/tmp/test')
    open('/tmp/test/test1', 'a').close()
    open('/tmp/test/test2', 'a').close()

    command = Command(script='unzip',
                      script_parts=['unzip', '-d', '/tmp/test'],
                      do_not_log=True)
    side_effect(command, command)


# Generated at 2022-06-14 09:42:05.294591
# Unit test for function match
def test_match():
    from thefuck.main import Command

    assert match(Command('unzip foo', ''))
    assert not match(Command('unzip foo', '', stderr='bar'))
    assert match(Command('unzip foo.zip', ''))
    assert match(Command('unzip -f foo.zip', ''))
    assert match(Command('unzip -f foo.zip -b', ''))
    assert not match(Command('unzip -d foo.zip', ''))
    assert not match(Command('unzip -f -d foo.zip', ''))

# Generated at 2022-06-14 09:42:17.500193
# Unit test for function side_effect
def test_side_effect():
    import os
    import tempfile

    # Create a dummy zip file to fake unzip output
    (handle, filepath) = tempfile.mkstemp()
    with os.fdopen(handle, 'w') as handle:
        handle.write('Archive:  {0}.zip\n'.format(filepath))
        handle.write('  inflating: {0}.txt         \n'.format(filepath))
        handle.write('  inflating: {0}-2.txt       \n'.format(filepath))
        handle.write('  inflating: {0}-3.txt       \n'.format(filepath))


# Generated at 2022-06-14 09:42:36.850092
# Unit test for function side_effect
def test_side_effect():
    import shutil
    from tempfile import mkdtemp
    from os import path

    def _remove_directory_tree(path):
        shutil.rmtree(path)

    def _assert_file_exists(file):
        assert path.exists(file)

    def _assert_file_does_not_exist(file):
        assert not path.exists(file)

    temp_dir = mkdtemp()
    zip_file = path.join(temp_dir, 'test.zip')
    output_file = path.join(temp_dir, 'test')
    with open(zip_file, 'w') as f:
        f.write('')
    with open(output_file, 'w') as f:
        f.write('')


# Generated at 2022-06-14 09:42:43.052989
# Unit test for function match
def test_match():
    assert match(Command('unzip -l file.zip', ''))
    assert match(Command('unzip file.zip', ''))
    assert not match(Command('unzip -d dir file.zip', ''))
    assert not match(Command('unzip file1.zip file2.zip', ''))
    assert not match(Command('unzip -l file.zip file1.zip', ''))


# Generated at 2022-06-14 09:42:45.543521
# Unit test for function match
def test_match():
    assert match(Command('unzip foo.zip', '', ''))
    assert match(Command('-d unzip', '', '')) is False


# Generated at 2022-06-14 09:42:49.887684
# Unit test for function match
def test_match():
    assert match(Command('unzip -l', ''))
    assert match(Command('unzip hello.zip', ''))
    assert match(Command('unzip hello.zip test.txt', ''))
    assert not match(Command('unzip -d output', ''))
    assert not match(Command('unzip -d output hello.zip', ''))
    assert not match(Command('unzip hello.txt test.txt', ''))
    assert not match(Command('unzip', ''))

# Generated at 2022-06-14 09:43:03.007345
# Unit test for function side_effect
def test_side_effect():
    import os
    import shutil
    from tempfile import mkdtemp

    tmpdir = mkdtemp()
    os.chdir(tmpdir)

    failsafe_folder = os.path.join(tmpdir, 'failsafe')
    os.mkdir(failsafe_folder)

    zip_file = os.path.join(tmpdir, 'test.zip')
    with open(zip_file, 'w') as f:
        f.write('')

    zip_file2 = os.path.join(failsafe_folder, 'test.zip')
    with open(zip_file2, 'w') as f:
        f.write('')

    # test the creation of a directory that does not exist
    side_effect(Command('unzip test.zip', '', CommandType.SYSTEM), '')


# Generated at 2022-06-14 09:43:09.237713
# Unit test for function match
def test_match():
    output = u'Archive:  myarchive.zip\n' \
             u'caution:  filename not matched:  it-is-a-dir/\n' \
             u'caution:  filename not matched:  it-is-a-dir/it-is-a-file\n' \
             u'  inflating: it-is-a-file          '
    assert match(Command(output, u'unzip myarchive.zip'))
    assert not match(Command(u'', u'unzip myarchive.zip'))
    assert not match(Command(output, u'unzip -d target myarchive.zip'))



# Generated at 2022-06-14 09:43:20.098199
# Unit test for function side_effect
def test_side_effect():
    # test prepare
    import os
    import shutil
    import tempfile

    o_f = tempfile.mkdtemp()
    old_dir = os.getcwd()
    os.chdir(o_f)
    os.mkdir('foo')
    os.mkdir('bar')
    with open('lol.txt', 'w') as f:
        f.write('Contents')
    with open('foo/cat.txt', 'w') as f:
        f.write('Contents')

    # test cases
    side_effect(None, None)  # dummy call

    # test run
    side_effect(None, 'unzip ./test_unzip_foolish.zip')

    # test check
    assert os.path.isdir('bar')
    assert os.path.isfile('lol.txt')


# Generated at 2022-06-14 09:43:25.569695
# Unit test for function match
def test_match():
    assert match(Command('unzip xyz.zip', '', '')) is False
    assert match(Command('unzip -x xyz.zip', '', '')) is False
    assert match(Command('unzip -d xyz.zip', '', '')) is False
    assert match(Command('unzip abc.zip', '', '')) is True
    assert match(Command('unzip abc.zip def.zip ghi.zip', '', '')) is True


# Generated at 2022-06-14 09:43:26.800123
# Unit test for function side_effect
def test_side_effect():
    assert side_effect(command, command) == None

# Generated at 2022-06-14 09:43:38.452332
# Unit test for function side_effect
def test_side_effect():
    command = "echo foo; unzip test.zip"
    command = get_new_command(shell.and_('echo foo', 'unzip test.zip'))
    assert 'echo foo && unzip -d test test.zip' == command

    with zipfile.ZipFile('test.zip', 'w') as archive:
        archive.write('test_file', 'test_file')

    side_effect('echo foo; unzip test.zip', 'echo foo && unzip -d test test.zip')

    assert not os.path.exists('test_file')
    assert os.path.exists('test/test_file')

    os.remove('test/test_file')
    os.rmdir('test')
    os.remove('test.zip')

# Generated at 2022-06-14 09:43:54.470715
# Unit test for function side_effect
def test_side_effect():
    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(tmpdir)

    archive = tempfile.NamedTemporaryFile(suffix='.zip')
    archive_name = archive.name
    archive = zipfile.ZipFile(archive.name, 'w')
    archive.writestr('file1', 'content')
    archive.writestr('file2', 'content')
    archive.close()

    # Define command for unzip file
    command = 'unzip {}'.format(archive_name)
    script = shell.and_('cd {}'.format(tmpdir), command)

    # Execute function side_effect
    side_effect(shell.and_('cd ..', command), script)
    assert not os.path.isfile('file1')

# Generated at 2022-06-14 09:44:00.280418
# Unit test for function side_effect
def test_side_effect():
    old_cmd = type('object', (object,), {'script_parts': ['unzip', '-l', 'test.zip']})()
    command = type('command', (object,), {'script_parts': ['unzip', '-d', 'test', 'test.zip']})()
    side_effect(old_cmd, command)
    assert(False)

# Generated at 2022-06-14 09:44:08.249230
# Unit test for function side_effect
def test_side_effect():
    script = 'ls -l'
    command = Command(script, '', '')

    # previous command is a related zip command
    zip_command = Command('unzip *.zip', '', '')
    side_effect(zip_command, command)
    assert side_effect(zip_command, command) is None

    # previous command is an unrelated command
    unrelated_command = Command('ls *.zip', '', '')
    assert side_effect(unrelated_command, command) is None

# Generated at 2022-06-14 09:44:18.702465
# Unit test for function match
def test_match():
    assert match(Command('', script='unzip file.zip')) == False
    assert match(Command('', script='unzip -d file.zip')) == False
    assert match(Command('', script='unzip file.zip file2.zip')) == False
    assert match(Command('', script='unzip file')) == False
    assert match(Command('', script='unzip file.zip file1 file2')) == False
    assert match(Command('', script='unzip -d file file1 file2')) == False
    assert match(Command('', script='unzip file1 file2')) == False
    assert match(Command('', script='unzip file1 file2 -d file.zip')) == False


# Generated at 2022-06-14 09:44:29.655445
# Unit test for function side_effect
def test_side_effect():
    file_contents = '12345'
    safe_file = 'safe.txt'
    unsafe_file = '../unsafe.txt'

    # unzip the file
    with open(safe_file, 'w') as f:
        f.write(file_contents)

    with open(unsafe_file, 'w') as f:
        f.write(file_contents)

    with zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(safe_file)
        zf.write(unsafe_file)

    # run the side_effect and check the effects
    script = type('Script', (object, ), {'script_parts': ['unzip', 'test.zip']})

# Generated at 2022-06-14 09:44:46.615813
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil

    testd = tempfile.mkdtemp()


# Generated at 2022-06-14 09:44:54.421535
# Unit test for function side_effect
def test_side_effect():
    from thefuck.utils import _make_command

    directory, dir_name = tempfile.mkdtemp(), 'dfadf'

# Generated at 2022-06-14 09:45:06.034575
# Unit test for function side_effect
def test_side_effect():
    # create a dummy file
    with open('old_file.txt', 'w') as f:
        f.write(u'z')
    with open('new_file.txt', 'w') as f:
        f.write(u'z')

    # create an archive with a file already present in the current directory
    zipped = zipfile.ZipFile('archive.zip', 'w')
    zipped.write('new_file.txt')
    zipped.close()

    # test the cleaning of the existing file in the current directory
    old_cmd = Command(u'unzip archive.zip')
    command = Command(u'unzip archive.zip')
    side_effect(old_cmd, command)
    assert os.path.isfile('new_file.txt')

# Generated at 2022-06-14 09:45:19.262597
# Unit test for function side_effect
def test_side_effect():
    import thefuck.shells
    import thefuck.types
    import thefuck.rules.unzip
    import zipfile
    import os
    import tempfile
    import shutil

    def _create_file(dir, file):
        f = open(os.path.join(dir, file), 'w')
        f.write('temp')
        f.close()

    def _create_dir(dir, subdir):
        os.makedirs(os.path.join(dir, subdir))

    def _create_zip_file(dir, zip_file):
        zipf = zipfile.ZipFile(os.path.join(dir, zip_file), 'w')
        zipf.write(os.path.join(dir, 'foo.txt'))
        zipf.close()



# Generated at 2022-06-14 09:45:27.986240
# Unit test for function side_effect
def test_side_effect():
    # set up paths
    outputdir = tempfile.mkdtemp()
    remove(os.path.join(outputdir, "foo"))
    remove(os.path.join(outputdir, "bar"))
    remove(os.path.join(outputdir, "baz"))
    remove(os.path.join(outputdir, "foo", "bar"))

    # set up files
    file(os.path.join(outputdir, "foo", "bar"), "w")
    file(os.path.join(outputdir, "foo", "bar"), "w")
    file(os.path.join(outputdir, "foo", "baz"), "w")

    # test side effects
    side_effect(FakeCommand(u'unzip test.zip'), FakeCommand(u'unzip -d test'))

    # check results


# Generated at 2022-06-14 09:46:00.819158
# Unit test for function match
def test_match():
    import os
    import shutil

    from thefuck.shells import shell
    from contextlib import contextmanager

    @contextmanager
    def create_zip_file(directory):
        directory = os.path.abspath(directory)
        zip_file = os.path.join(os.path.dirname(directory),
                                os.path.basename(directory) + '.zip')

        zf = zipfile.ZipFile(zip_file, 'w')
        zf.write(os.path.join(directory, 'test'), 'test.txt')
        zf.write(os.path.join(directory, 'test2'), 'test2/test.txt')
        zf.close()

        try:
            yield directory, zip_file
        finally:
            shutil.rmtree(directory)

# Generated at 2022-06-14 09:46:07.683035
# Unit test for function match
def test_match():
    """
    Calling `zip` with a file that is not a zip
    """
    command = Command('unzip file.zip', '', '', 'file.zip:  not a zipfile')
    assert match(command)
    command = Command('unzip file', '', '', 'file.zip:  not a zipfile')
    assert match(command)



# Generated at 2022-06-14 09:46:19.533067
# Unit test for function side_effect
def test_side_effect():
    with TemporaryDirectory() as tmpdir:
        # Create zip archive
        zipdir = '{}/zipdir'.format(tmpdir)
        os.makedirs(zipdir)
        file1 = '{}/file1'.format(zipdir)
        file2 = '{}/file2'.format(zipdir)
        file1_content = 'file1content'
        file2_content = 'file2content'

        with open(file1, 'w+') as f1:
            f1.write(file1_content)
        with open(file2, 'w+') as f2:
            f2.write(file2_content)

        # Create a zip file in current directory
        zip_file = '{}/archive.zip'.format(tmpdir)

# Generated at 2022-06-14 09:46:30.544310
# Unit test for function match
def test_match():
    z = ".\\test.zip"
    path = ".\\test"
    try:
        os.mkdir(path)
        with zipfile.ZipFile(z, 'w') as z:
            z.write(path)
        for c in ['unzip', z ], ['unzip', z, path ], ['unzip', path, z]:
            assert match(c)
        for c in ['unzip', z, '-d', path], ['unzip', z, path, '-d', path], ['unzip', path, z, '-d', path]:
            assert not match(c)
        assert match(["unzip", ".\\test\\test\\test.zip"])

        os.rmdir(path)
    except Exception:
        pass
    finally:
        os.remove(z)



# Generated at 2022-06-14 09:46:38.183197
# Unit test for function match
def test_match():
    assert not match(Command('unzip filename.zip', ''))
    assert match(Command('unzip filename.zip archive/file.txt', ''))
    assert not match(Command('unzip -d dir filename.zip', ''))
    assert match(Command('unzip -t filename.zip', ''))
    assert not match(Command('unzip --help', ''))



# Generated at 2022-06-14 09:46:45.532297
# Unit test for function match
def test_match():
    # If command is not unzip, should return false
    assert not match(Command('ls', ''))
    # If command is already unzip -d , should return false
    assert not match(Command('unzip -d .', ''))
    # If file not exist, should return false
    assert not match(Command('unzip test.zip', ''))
    # If archive contain more than 1 file, should return true
    assert match(Command('unzip test_multi.zip', ''))
    # If archive contain only one file, should return false
    assert not match(Command('unzip test_single.zip', ''))



# Generated at 2022-06-14 09:46:58.376035
# Unit test for function side_effect
def test_side_effect():
    old_cmd = Mock(spec_set=Command)
    old_cmd.script = 'unzip'
    old_cmd.script_parts = ['unzip', 'test.zip']
    command = Mock(spec_set=Command)
    command.script = 'unzip -d test'
    command.script_parts = ['unzip', '-d', 'test']
    # Create test directory and files
    os.chdir(tempfile.mkdtemp())
    open('test_file.txt', 'a').close()
    os.makedirs('test_dir')
    open('test_dir/test_file.txt', 'a').close()

    side_effect(old_cmd, command)

    # Test if only the directory was created
    assert os.path.isdir('test')
    assert not os.path.ex

# Generated at 2022-06-14 09:47:06.172159
# Unit test for function side_effect
def test_side_effect():
    old_env = os.environ
    dummy_file = 'dummy_file.txt'
    with zipfile.ZipFile('dummy_file.zip', 'w') as archive:
        archive.write(dummy_file)
    os.environ = {'LANG': ''}
    side_effect(Command('unzip dummy_file.zip', ''), Command('unzip -d dummy_file dummy_file.zip', ''))
    os.environ = old_env
    assert os.path.exists('dummy_file.txt') == False

# Generated at 2022-06-14 09:47:08.190148
# Unit test for function side_effect
def test_side_effect():
    output = side_effect('unzip file.zip', 'unzip -d dir1 file.zip')
    assert output is None

# Generated at 2022-06-14 09:47:13.842869
# Unit test for function match
def test_match():
    assert match(Command('unzip filename.zip', ''))
    assert match(Command('unzip filename.zip file', ''))
    assert not match(Command('unzip -d test filename.zip', ''))
    assert not match(Command('unzip -d test file1.zip file2.zip', ''))
    assert not match(Command('unzip -d test filename.zip file', ''))


# Generated at 2022-06-14 09:48:03.196526
# Unit test for function side_effect
def test_side_effect():
    old_cmd = Command("unzip test.zip", "")
    command = Command("unzip -d test/ test.zip", "")
    side_effect(old_cmd, command)

# Generated at 2022-06-14 09:48:04.053394
# Unit test for function side_effect
def test_side_effect():
    assert side_effect(0, 0) == 0

# Generated at 2022-06-14 09:48:14.013666
# Unit test for function match
def test_match():
    assert match(Command(script='unzip wrong.zip')) == True
    assert match(Command(script='unzip wrong.zip extract')) == True
    assert match(Command(script='unzip -l wrong.zip')) == False
    assert match(Command(script='unzip -d output wrong.zip')) == False
    assert match(Command(script='unzip wrong.zip -d output')) == True
    assert match(Command(script='unzip wrong.zip Extract')) == True
    assert match(Command(script='unzip wrong.zip -l -d output')) == False


# Generated at 2022-06-14 09:48:19.256482
# Unit test for function match
def test_match():
    from thefuck.rules.unzip_no_dir import match
    assert match(u'unzip /home/sam/test.zip')
    assert not match(u'unzip /home/sam/test.zip -d /home/sam/Downloads')
    assert match(u'unzip test.zip')
    assert match(u'unzip test')
    assert not match(u'unzip')



# Generated at 2022-06-14 09:48:21.344534
# Unit test for function match
def test_match():
    assert match(Command('unzip /usr/bin/unzip /tmp/test.zip'))


# Generated at 2022-06-14 09:48:26.603863
# Unit test for function side_effect
def test_side_effect():
    assert side_effect(
        shell.and_('unzip zipfile.zip', 'unzip -d zipfile zipfile.zip'),
        shell.and_('unzip -d zipfile zipfile.zip'))

# Generated at 2022-06-14 09:48:32.008624
# Unit test for function match
def test_match():
    assert match(Command('zip file1.zip file2.zip', ''))
    assert not match(Command('unzip file1.zip -d file2.zip', ''))
    assert not match(Command('zip -r file1.zip file2.zip', ''))
    assert not match(Command('zip file1.zip', ''))
    assert not match(Command('unzip', ''))

# Generated at 2022-06-14 09:48:39.698958
# Unit test for function side_effect
def test_side_effect():
    # Test file that is not in the current directory
    os.makedirs('/home/user/test_dir')
    test_file = open('/home/user/test_dir/test.txt', 'w+')
    test_file.write('This is a test.')
    test_file.close()

    with zipfile.ZipFile('test.zip', 'a') as test_zip:
        test_zip.write('/home/user/test_dir/test.txt')

    with zipfile.ZipFile('test.zip', 'r') as archive:
        for file in archive.namelist():
            if not os.path.abspath(file).startswith(os.getcwd()):
                assert file == '/home/user/test_dir/test.txt'


# Generated at 2022-06-14 09:48:47.925008
# Unit test for function match
def test_match():
    assert _zip_file('unzip file.zip') == 'file.zip'
    assert _zip_file('unzip -a file.zip') == 'file.zip'
    assert _zip_file('unzip -l file.zip') == 'file.zip'
    assert _zip_file('unzip file') == 'file.zip'
    assert _zip_file('unzip -a file') == 'file.zip'
    assert _zip_file('unzip -l file') == 'file.zip'


# Generated at 2022-06-14 09:48:52.365054
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', '', ''))
    assert not match(Command('unzip -d dir file.zip', '', ''))
    assert not match(Command('unzip -d dir file', '', ''))
    assert match(Command('unzip file', '', ''))
    assert not match(Command('zip file', '', ''))



# Generated at 2022-06-14 09:50:35.686240
# Unit test for function side_effect
def test_side_effect():
    # Set up a shell object
    sh = Shell()

    # Create a temporary directory to work in
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    # Create a zip file containing test files
    with zipfile.ZipFile(os.path.join(tmpdir, 'test.zip'), 'w') as testzip:
        testzip.write(os.path.join(tmpdir, 'foobar.pdf'), 'foobar.pdf')
        testzip.write(os.path.join(tmpdir, 'foobar.txt'), 'foobar.txt')

    # Create a script to test side_effect()
    script = 'unzip test.zip'
    cmd = Command(script, '', 0)

    # Call side_effect()
    side_effect(cmd, cmd)

    # Verify that

# Generated at 2022-06-14 09:50:43.554569
# Unit test for function side_effect
def test_side_effect():
    zip_path = os.path.join(os.path.dirname(__file__), '../..', 'data', 'tmp_folder.zip')
    side_effect(None, None)
    assert not os.path.exists('file1.txt')
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall()

    side_effect(None, None)
    assert not os.path.exists('file1.txt')

# Generated at 2022-06-14 09:50:51.729455
# Unit test for function side_effect
def test_side_effect():
    # creating archive
    test_zip = zipfile.ZipFile('test.zip', 'w')
    test_zip.writestr('file_a', '')
    test_zip.writestr('file_b', '')
    test_zip.close()

    # creating two files
    with open('file_a', 'a'):
        os.utime('file_a', None)
    with open('file_b', 'a'):
        os.utime('file_b', None)

    # running side_effect
    class Command():
        def __init__(self):
            self.script_parts = ['unzip', 'test.zip']
    side_effect(Command(), None)

    # checking if files were removed
    old_pwd = os.getcwd()
    os.chdir('test')

# Generated at 2022-06-14 09:50:54.937230
# Unit test for function match
def test_match():
    from tests.utils import Command

    assert match(Command('unzip non_existent_file'))
    assert match(Command('unzip file.zip'))
    assert match(Command('unzip file'))
    assert not match(Command('unzip another.zip -d destdir'))
    assert not match(Command('unzip -a another.zip -d destdir'))


# Unit tests for function get_new_command