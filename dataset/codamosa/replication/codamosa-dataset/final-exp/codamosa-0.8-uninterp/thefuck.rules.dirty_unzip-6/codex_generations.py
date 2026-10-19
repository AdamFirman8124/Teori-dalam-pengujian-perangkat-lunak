

# Generated at 2022-06-14 09:41:09.067554
# Unit test for function side_effect
def test_side_effect():
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        os.mkdir('subdir')
        with open('subdir/subsubdir1/subsubsubdir1', 'w') as subsubsubsubdir1:
            subsubsubsubdir1.write('subsubsubsubdir1')

        with open('subsubsubsubdir1', 'w') as subsubsubsubdir1:
            subsubsubsubdir1.write('subsubsubsubdir1')

        with open('subsubsubsubdir2', 'w') as subsubsubsubdir2:
            subsubsubsubdir2.write('subsubsubsubdir2')


# Generated at 2022-06-14 09:41:16.056554
# Unit test for function match
def test_match():
    assert _is_bad_zip('test-data/test-zip.zip') == False
    assert _is_bad_zip('test-data/test-bad-zip.zip') == True
    command = Command('unzip test-data/test.zip', '')
    assert match(command) == False
    command = Command('unzip test-data/test-zip.zip', '')
    assert match(command) == False
    command = Command('unzip test.zip -d last.zip', '')
    assert match(command) == False
    command = Command('unzip test-data/test-bad-zip.zip', '')
    assert match(command) == True
    command = Command('unzip test.zip', '')
    assert match(command) == False


# Generated at 2022-06-14 09:41:24.655395
# Unit test for function side_effect
def test_side_effect():
    # Ensure _zip_file() works
    assert _zip_file(Command('unzip -d test test.zip', '', '')) == 'test.zip'

    # Create a zip file and extract it to working dir
    with zipfile.ZipFile('test.zip', 'w') as archive:
        archive.writestr('test.txt', '')
    shell.and_('unzip -o test.zip', '')

    # Run side_effect
    side_effect('', Command('unzip -d test test.zip', '', ''))

    # Ensure test.txt was removed
    assert not os.path.isfile('test.txt')

    # Cleanup
    os.remove('test.txt')
    os.remove('test.zip')

# Generated at 2022-06-14 09:41:30.270178
# Unit test for function side_effect
def test_side_effect():
    for directory in ['dir/dir2', 'dir/dir']:
        os.makedirs(directory)
    with open('dir/file', 'w') as file:
        file.write('Fake file')

    with tempfile.NamedTemporaryFile() as archive:
        with zipfile.ZipFile(archive.name, 'w') as zip:
            for directory in glob.glob(os.path.join('dir', '*')):
                zip.write(directory)

    old_cmd = Command('unzip ' + archive.name, '', Error(''))
    cmd = Command('unzip -d dir_zip ' + archive.name, '', Error(''))
    side_effect(old_cmd, cmd)

    assert os.path.exists('dir_zip/file')
    assert not os.path.exists

# Generated at 2022-06-14 09:41:46.276090
# Unit test for function side_effect
def test_side_effect():
    if not os.path.isdir('test_unzip_folder'):
        os.mkdir('test_unzip_folder')

    fake_file = open('test_unzip_folder/fake_file', 'w')
    fake_file.close()
    if os.path.exists('test_unzip_folder/fake_file'):
        os.remove('test_unzip_folder/fake_file')
        assert not os.path.exists('test_unzip_folder/fake_file')
    else:
        assert False, 'test_unzip_folder/fake_file does not exist'

    fake_file = open('fake_file', 'w')
    fake_file.close()
    if os.path.exists('fake_file'):
        os.remove('fake_file')

# Generated at 2022-06-14 09:41:58.631795
# Unit test for function match
def test_match():
    # unzip test.zip -d test
    assert not match(Command(
        script='unzip test.zip -d test',
        stderr="test.zip:  bad zipfile offset (local header sig):  0"))
    assert not match(Command(
        script='unzip test.zip -d test',
        stderr="test.zip:  bad zipfile offset (local header sig):  10"))
    assert not match(Command(
        script='unzip test.zip -d test',
        stderr="test2.zip:  bad zipfile offset (local header sig):  0"))
    assert not match(Command(
        script='unzip test.zip -d test',
        stderr=u"test\xc4\x84.zip:  bad zipfile offset (local header sig):  0"))

# Generated at 2022-06-14 09:42:04.239479
# Unit test for function match
def test_match():
    assert not match(Command('foo', 'echo'))
    assert not match(Command('unzip foo.zip', 'echo'))
    assert not match(Command('unzip bar.zip -d foo', 'echo'))
    assert not match(Command('unzip wrong-zip.zip', 'echo'))


# Generated at 2022-06-14 09:42:17.005292
# Unit test for function match
def test_match():
    test_cases = (
        (u'unzip hello-world.zip', False),
        (u'unzip -d test hello-world.zip', False),
        (u'unzip -l hello-world.zip', False),
        (u'unzip hello-world', False),
        (u'unzip hello-world.zip -d test', False),
        (u'unzip hello-world.zip the-world-is-flat.txt', True),
        (u'unzip hello-world.zip the-world-is-flat.txt -d test', True),
        (u'unzip hello-world the-world-is-flat.txt', True),
        (u'unzip hello-world the-world-is-flat.txt -d test', True),
    )


# Generated at 2022-06-14 09:42:30.562019
# Unit test for function match
def test_match():
    # File is not a zip file
    command = Command('unzip not_a_file.zip', 'not_a_file.zip: not a zipfile')
    assert not _is_bad_zip('not_a_file.zip')
    assert not match(command)

    # File contains a single file and does not contain a directory
    with tempfile.NamedTemporaryFile() as f:
        # Create a zip file containing a single file
        with zipfile.ZipFile(f.name, 'w') as archive:
            archive.writestr('single_file.txt', 'test')
        command = Command('unzip {}'.format(f.name), f.name)
        assert not _is_bad_zip(f.name)
        assert not match(command)

    # File contains a directory and a file

# Generated at 2022-06-14 09:42:39.328224
# Unit test for function match
def test_match():
    assert match(Command('unzip example.zip',
                         'unzip:  cannot find or open example.zip, example.zip.zip or example.zip.ZIP.'))
    assert match(Command('unzip example.zip foo.bar',
                         'unzip:  cannot find or open example.zip, example.zip.zip or example.zip.ZIP.'))
    assert not match(Command('unzip -d example example.zip',
                             'unzip:  cannot find or open example.zip, example.zip.zip or example.zip.ZIP.'))
    assert not match(Command('unzip -d example example.zip foo.bar',
                             'unzip:  cannot find or open example.zip, example.zip.zip or example.zip.ZIP.'))

# Generated at 2022-06-14 09:42:58.103346
# Unit test for function match
def test_match():
    assert _is_bad_zip(_zip_file(Command('unzip foo.zip',
                                  "unzip error: cannot find or open foo.zip, foo.zip.zip or foo.zip.ZIP",
                                  1,
                                  '',
                                  '',
                                  ''))) == True


# Generated at 2022-06-14 09:43:08.050075
# Unit test for function side_effect
def test_side_effect():
    # create the dummy zip archive
    with zipfile.ZipFile('dummy.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('testfile', "test")
        archive.writestr('../../testfile2', "test2")

    test_cmd = shell.and_('unzip', 'dummy.zip')
    side_effect(test_cmd, test_cmd)

    # the existing testfile should be removed
    assert not os.path.exists('testfile')

    # the existing testfile2 should not have been removed
    assert os.path.exists('../../testfile2')

    # remove the dummy zip archive
    os.remove('dummy.zip')

# Generated at 2022-06-14 09:43:19.061504
# Unit test for function match
def test_match():
    assert match(Command('unzip -d desired_directory /path/to/file')) == False
    assert match(Command('unzip /path/to/file_to_unzip.zip')) == True
    assert match(Command('unzip -d /path/to/file_to_unzip.zip')) == True
    assert match(Command('unzip -d /path/to/file_to_unzip.zip /path/to/not_an_archive.txt')) == False
    assert match(Command('unzip /path/to/not_an_archive.txt')) == False
    assert match(Command('unzip -d /path/to/not_an_archive.txt')) == False


# Generated at 2022-06-14 09:43:25.537605
# Unit test for function match
def test_match():
    # Check if the zip contains only one file
    assert not match(Command('unzip test1.zip', '', False))

    # Check if the zip contains more than one file
    assert match(Command('unzip test2.zip', '', False))

    # Check if -d is not included in the command
    assert not match(Command('unzip test2.zip -d test2', '', False))

    # Check if the file is not a zip
    assert not match(Command('unzip test.txt', '', False))



# Generated at 2022-06-14 09:43:38.203296
# Unit test for function side_effect
def test_side_effect():
    import shutil
    import tempfile
    import zipfile
    from thefuck.shells import shell

    with tempfile.NamedTemporaryFile() as tmp:
        with zipfile.ZipFile(tmp.name, 'w') as tmp_zip:
            tmp_zip.writestr('existing_file', 'test')
            tmp_zip.writestr(shell.quote('dir/file'), 'test')
    with open('existing_file', 'w') as tmp:
        tmp.write('test')
    os.makedirs('dir')
    with open('dir/file', 'w') as tmp:
        tmp.write('test')


# Generated at 2022-06-14 09:43:43.025665
# Unit test for function match
def test_match():
    from thefuck.rules.zip_dot_dot import match
    assert match(
        Command('unzip filename.zip', 'unzip:  cannot find or open filename.zip'))
    assert match(
        Command('unzip filename.zip', 'unzip:  cannot find or open filename.zip',
                stderr='unzip:  cannot find or open filename.zip'))
    assert not match(
        Command('unzip filename.zip', 'unzip:  '))
    assert not match(
        Command('unzip filename.zip', 'unzip:  ',
                stderr='unzip:  '))



# Generated at 2022-06-14 09:43:48.652327
# Unit test for function match
def test_match():
    assert not match(Command('unzip test.zip', ''))
    assert match(Command('unzip test.zip file', ''))
    assert match(Command('unzip test.zip /path/to/file', ''))
    assert not match(Command('unzip -d test.zip /path/to/file', ''))

# Generated at 2022-06-14 09:43:58.932233
# Unit test for function match
def test_match():
    assert match(Command('unzip {}'.format(os.environ.get('TEST_ZIP')), None, None))
    assert match(Command('unzip {}'.format(os.environ.get('TEST_ZIP_BAD_FORMAT')), None, None))
    assert match(Command('unzip {}'.format(os.environ.get('TEST_ZIP_WITH_FOLDERS')), None, None))
    assert not match(Command('unzip {}'.format(os.environ.get('TEST_ZIP')), None, None))
    assert not match(Command('unzip {} -d {}'.format(os.environ.get('TEST_ZIP'), '.'), None, None))
    assert not match(Command('unzip', None, None))


# Generated at 2022-06-14 09:44:04.695064
# Unit test for function match
def test_match():
    assert not match(Command("unzip -d foo.zip"))
    assert match(Command("unzip foo"))
    assert match(Command("unzip foo.zip"))
    assert match(Command("unzip -d foo.zip bar"))
    assert match(Command("unzip bar foo.zip"))


# Generated at 2022-06-14 09:44:15.105254
# Unit test for function side_effect
def test_side_effect():
    from thefuck import shells
    from thefuck.shells import Bash

    def popen(args, **kwargs):
        assert args[0] == 'unzip'
        assert args[-1] == '/tmp/test.zip'
        return '''Archive:  /tmp/test.zip
   creating: /tmp/
 extracting: /tmp/foo
  inflating: /tmp/bar.txt
  inflating: /tmp/baz.txt      
'''.splitlines()

    def remove(path):
        assert path in ['/tmp/foo', '/tmp/bar.txt', '/tmp/baz.txt']

    def which(command, path=None):
        assert command == 'unzip'
        return '/usr/bin/unzip'

    orig_which = shells.which
    shells.which = which

    orig_

# Generated at 2022-06-14 09:44:50.670946
# Unit test for function match
def test_match():
    assert match(Command('unzip test.zip'))
    assert match(Command('unzip test.zip test'))
    assert match(Command('unzip -j test.zip'))
    assert match(Command('unzip -j test.zip test'))
    assert match(Command('unzip -jo test.zip test'))
    assert not match(Command('unzip -d test test.zip'))
    assert not match(Command('unzip -jo test.zip test test2'))
    assert not match(Command('unzip -jo test.zip test test2'))
    assert not match(Command('unzip -jo test.zip test test2 test3'))



# Generated at 2022-06-14 09:45:01.956339
# Unit test for function match
def test_match():
    assert not match(Command())
    assert not match(Command(script='', stdout=''))
    assert not match(Command('unzip', '-d'))
    assert match(Command('ls', '', ''))
    assert not match(Command('ls', '', ''))
    assert match(Command('unzip test.zip', '', ''))
    assert match(Command('unzip test', '', ''))
    assert not match(Command('unzip -d test', '', ''))
    assert match(Command('unzip test -x test', '', ''))
    assert not match(Command('unzip test -x test1 test2', '', ''))



# Generated at 2022-06-14 09:45:13.591080
# Unit test for function match
def test_match():
    from tests.utils import Command

    # Different types of commands, the last two are not zip files:
    assert not match(Command('unzip file.zip'))
    assert match(Command('unzip file_zip_a.zip'))
    assert match(Command('unzip file_zip_b.zip'))
    assert not match(Command('unzip file_zip'))

    # Check that an external file is not overwritten, see issue #357
    assert not match(Command('unzip /tmp/other_file.zip'))

    # Make sure a good zip file is not matched
    good_archive = 'tests/scripts/good_zip.zip'
    assert not match(Command('unzip ' + good_archive))



# Generated at 2022-06-14 09:45:18.182061
# Unit test for function side_effect
def test_side_effect():
    """
    >>> test_command = attr.evolve(command, script='unzip test.zip')
    >>> side_effect(test_command, command)
    >>> os.path.exists('test.txt')
    False
    >>> os.path.exists('fake/')
    False
    """

# Generated at 2022-06-14 09:45:22.356552
# Unit test for function match
def test_match():
    """ Test to make sure the "match" function returns the correct value"""
    from thefuck.rules.unzip_single_file import match

    assert match(u'unzip zipfile.zip')
    assert match('')
    assert not match('ls -l')


# Generated at 2022-06-14 09:45:26.260151
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('unzip', 'unzip file.zip'))
    assert not match(Command('unzip', 'unzip -d file.zip'))
    assert not match(Command('unzip', 'unzip'))
    assert not match(Command('unzip', 'unzip -l'))



# Generated at 2022-06-14 09:45:38.205168
# Unit test for function match
def test_match():
    assert match(Command('unzip a.zip', '', '')) is False
    assert match(Command('unzip -d folder a.zip', '', '')) is False
    assert match(Command('unzip -d folder', '', 'a.zip')) is False

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    zip_file = os.path.join(cur_dir, 'test_data/twofiles.zip')
    assert match(Command('unzip {}'.format(zip_file), '', '')) is True

    zip_file = os.path.join(cur_dir, 'test_data/twofiles.zip')
    assert match(Command('unzip {}'.format(zip_file), '', '')) is True



# Generated at 2022-06-14 09:45:52.778539
# Unit test for function match
def test_match():
    assert(match(Command('unzip file.zip', '', '', '')))
    assert(match(Command('unzip file', '', '', '')))
    assert(match(Command('unzip -j file.zip file1 file2',
                         '', '', '')))
    assert(not match(Command('unzip -j file.zip file1 file2',
                              '', '', '')))
    assert(not match(Command('unzip -d file.zip',
                              '', '', '')))
    assert(not match(Command('unzip -unzip -d file.zip',
                              '', '', '')))


# Generated at 2022-06-14 09:46:01.225898
# Unit test for function side_effect
def test_side_effect():
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp()
    old_cwd = os.getcwd()
    os.chdir(tmpdir)


# Generated at 2022-06-14 09:46:13.061806
# Unit test for function match
def test_match():
    # Check with one file included
    assert(match(Command('unzip tesfile.zip',
                         u'Archive:  tesfile.zip\n')) == True)

    # Check with multiple files included
    assert(match(Command('unzip tesfile.zip',
                         u'Archive:  tesfile.zip\n')) == True)

    # Check with the -d flag used
    assert(match(Command('unzip tesfile.zip -d test_folder',
                         u'Archive:  tesfile.zip\n')) == False)

    # Check with a file that does not exist

# Generated at 2022-06-14 09:46:46.488196
# Unit test for function match
def test_match():
    # True case
    assert match(Command("unzip file.zip", ""))
    # False case
    assert not match(Command("unzip -d file.zip", ""))
    assert not match(Command("unzip -t file.zip", ""))
    assert not match(Command("unzip file.zip file.txt", ""))
    assert not match(Command("not unzip file.zip", ""))

# Generated at 2022-06-14 09:46:59.241307
# Unit test for function side_effect
def test_side_effect():
    # Mocking function remove
    remove = MagicMock()
    remove_path = remove.return_value = MagicMock()
    exists = MagicMock()
    exists.return_value = MagicMock()

    # Mocking function os
    os_mod = __import__('os')
    os_path = os_mod.path
    os_path.exists = exists
    os_path.abspath = MagicMock()
    os_path.abspath.return_value = remove_path

    # Mocking function os
    os_mod = __import__('os')
    os_mod.remove = remove
    os_mod.getcwd = MagicMock()
    os_mod.getcwd.return_value = '.'

    # Mocking function zipfile

# Generated at 2022-06-14 09:47:12.743937
# Unit test for function side_effect
def test_side_effect():
    import os

    with open('tmp_file','w') as f:
        f.write('test1')
    with open('tmp_dir/tmp_file','w') as f:
        f.write('test2')
    os.mkdir('tmp_dir')
    os.mkdir('tmp_dir2')
    with zipfile.ZipFile('tmp_dir.zip', 'w') as archive:
        archive.write('tmp_dir/tmp_file')
        archive.write('tmp_dir2')
        archive.write('tmp_file')

    side_effect(None, None)

    assert not os.path.exists('tmp_file')
    assert not os.path.exists('tmp_dir/tmp_file')
    assert os.path.exists('tmp_dir2')
    assert os.path.ex

# Generated at 2022-06-14 09:47:23.635826
# Unit test for function side_effect
def test_side_effect():
    # Create file and directory
    f = open('test.txt', 'w+')
    os.mkdir('test')
    f.write('Test')
    f.close()

    # Create a zip archive
    testzip = zipfile.ZipFile('test.zip', 'w')
    testzip.write('test.txt')
    testzip.write('test')
    testzip.close()

    # Run the side_effect function and test to see if it removes the files correctly
    old_cmd = type(u'old_cmd', (object,), {'script': u'unzip test.zip'})
    command = type(u'command', (object,), {'script': u'unzip -d test.zip'})
    side_effect(old_cmd, command)
    # If the files are not removed, then the following

# Generated at 2022-06-14 09:47:34.573997
# Unit test for function match
def test_match():
    cmd = u'unzip file.zip'
    assert not match(Command(cmd, ''))
    cmd = u'unzip -d dir file.zip'
    assert not match(Command(cmd, ''))
    with mock.patch('thefuck.specific.unzip.os.path.isfile',
                    return_value=True):
        assert not match(Command(cmd, ''))
    with mock.patch('thefuck.specific.unzip.os.path.isfile',
                    return_value=True):
        with mock.patch('thefuck.specific.unzip._is_bad_zip',
                       return_value=False):
            assert not match(Command(cmd, ''))

# Generated at 2022-06-14 09:47:41.151599
# Unit test for function match
def test_match():
    assert match(
        Command(script='unzip foo.zip', stderr="error:  foo.zip existe"))
    assert not match(
        Command(script='unzip foo.zip', stderr="error:  Le fichier n'existe pas"))
    assert match(
        Command(script='unzip foo.zip', stderr="error:  Foo doesn't exist"))


# Generated at 2022-06-14 09:47:50.270120
# Unit test for function side_effect
def test_side_effect():
    from thefuck.types import Command
    from tempfile import NamedTemporaryFile
    from shutil import rmtree
    import os.path
    import zipfile

    script = 'unzip -d foo {}'.format(__file__)
    with NamedTemporaryFile('wb', suffix='.zip') as archive:
        with zipfile.ZipFile(archive, 'w') as zf:
            zf.write(__file__, 'test_side_effect.py')
            zf.write(__file__, 'foo/test_side_effect.py')
            zf.write(__file__, os.path.abspath('test_side_effect.py'))
        archive.flush()

        cmd = Command(script, '')
        side_effect(cmd, cmd)


# Generated at 2022-06-14 09:47:58.414636
# Unit test for function match
def test_match():
    from thefuck.rules.unzip_single_file import match
    assert match(Command(script='unzip test.zip'))

    assert not match(Command(script='unzip -d test.zip'))

    assert not match(Command(script='unzip test.rar'))

    assert not match(Command(script='unzip test.zip -d test'))

    assert not match(Command(script='unzip test'))



# Generated at 2022-06-14 09:48:07.522052
# Unit test for function match
def test_match():
    script = 'unzip test.zip -x'
    assert not match(Command(script, ''))
    assert match(Command(script + ' -d', ''))

    script = 'unzip test1.zip -x'
    assert match(Command(script, ''))
    assert match(Command(script + ' -d', ''))

    script = 'unzip test2.zip test1.zip -x'
    assert match(Command(script, ''))
    assert match(Command(script + ' -d', ''))

    script = 'unzip test3.zip test1.zip test2.zip -x'
    assert match(Command(script, ''))
    assert match(Command(script + ' -d', ''))

# Generated at 2022-06-14 09:48:10.633021
# Unit test for function match
def test_match():
    assert _is_bad_zip('wrong.zip') is False
    assert _is_bad_zip('good.zip') is True

# Generated at 2022-06-14 09:49:14.243596
# Unit test for function side_effect
def test_side_effect():
    import zipfile
    from thefuck.utils import which
    from shutil import rmtree
    import tempfile
    import os.path
    import os

    with tempfile.NamedTemporaryFile(suffix='.zip') as tf:
        with zipfile.ZipFile(tf.name, 'w') as zf:
            zf.writestr('test', 'test')

        with tempfile.TemporaryDirectory() as td:
            unzip_path = which('unzip')[0]
            os.chdir(td)

            side_effect(
                type('', (), {'script': unzip_path + ' {} -d .'.format(tf.name)})
                , type('', (), {'script': unzip_path + ' {} -d .'.format(tf.name)})
            )

            assert os

# Generated at 2022-06-14 09:49:24.809272
# Unit test for function match
def test_match():
    assert _is_bad_zip('test_files/test.zip')
    assert _is_bad_zip('test_files/test.only_one_file.zip') is False
    assert match(Command('unzip test.zip', '', '', '', None, None))
    assert match(Command('unzip test.zip', '', '', '', None, None))
    assert match(Command('unzip test.zip file1 file2 file3', '', '', '', None, None))
    assert match(Command('unzip -j test.zip file1 file2 file3', '', '', '', None, None))
    assert match(Command('unzip -j -n test.zip file1 file2 file3', '', '', '', None, None))

# Generated at 2022-06-14 09:49:28.860379
# Unit test for function side_effect
def test_side_effect():
    oldcmd = FakeCommand()
    oldcmd.script = u'unzip -d {} {}'.format('/tmp', '/tmp/file.zip')
    oldcmd.script_parts = oldcmd.script.split(' ')
    cmd = FakeCommand()
    cmd.script = u'unzip -d {} {}'.format('/tmp', '/tmp/file.zip')
    cmd.script_parts = cmd.script.split(' ')
    side_effect(oldcmd, cmd)
    # FIXME: Test side_effect

# Generated at 2022-06-14 09:49:34.429210
# Unit test for function match
def test_match():
    assert match(Command('unzip abc.zip', None))
    assert match(Command('unzip abc.zip -x a.txt', None))
    assert not match(Command('unzip abc.zip -o', None))
    assert not match(Command('unzip -d ./abc/ abc.zip', None))

# Generated at 2022-06-14 09:49:43.819459
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import zipfile
    from thefuck.shells import get_shell
    with get_shell() as shell:
        tmpdir = tempfile.mkdtemp()
        try:
            with open(os.path.join(tmpdir, 'x'), 'w+') as x:
                x.write('')

            with zipfile.ZipFile('x.zip', 'w') as zf:
                zf.write('x')

            side_effect(None, 'unzip x.zip')

            assert os.path.exists(os.path.join(tmpdir, 'x')) is True
        finally:
            os.remove(os.path.join(tmpdir, 'x'))
            os.remove('x.zip')

# Generated at 2022-06-14 09:49:55.508077
# Unit test for function match
def test_match():
    # Test for unzip file.zip
    command = Command('unzip file.zip', '', '', '')
    assert match(command)
    zip_file = _zip_file(command)
    assert zip_file == 'file.zip'
    assert _is_bad_zip(zip_file)

    # Test for unzip -x file.zip
    command = Command('unzip -x file.zip', '', '', '')
    assert not match(command)

    # Test for unzip file.zip -d dir
    command = Command('unzip file.zip -d dir', '', '', '')
    assert not match(command)

    # Test for unzip file
    command = Command('unzip file', '', '', '')
    assert match(command)
    zip_file = _zip_file(command)

# Generated at 2022-06-14 09:50:07.136617
# Unit test for function match
def test_match():
    # cmd = "unzip archive1.zip -d destination"
    assert not match(Command(script=u'unzip archive1.zip -d destination',
                             stdout=u'fauxpkg: invalid option -- \'d\'\n',
                             stderr=u''))

    # cmd = "unzip archive1.zip"
    assert match(Command(script=u'unzip archive1.zip',
                         stdout=u'Archive:  archive1.zip\n',
                         stderr=u'fauxpkg: invalid option -- \'d\'\n'))

    # cmd = "unzip -q archive1.zip"

# Generated at 2022-06-14 09:50:13.910766
# Unit test for function match
def test_match():
    from thefuck.shells import Bash
    assert match(Bash(u'unzip test.zip'))
    assert match(Bash(u'unzip test.zip test2.zip'))
    assert match(Bash(u'unzip test.tar'))
    assert not match(Bash(u'unzip test.zip -d test2'))
    assert not match(Bash(u'unzip test.zip -d test2'))
    assert not match(Bash(u'zip test.tar'))

# Generated at 2022-06-14 09:50:27.849454
# Unit test for function side_effect
def test_side_effect():
    test_dir = os.path.join( os.path.dirname(__file__), 'testdir')
    test_dir_all = os.path.join(os.path.dirname(__file__), 'testdir-all')


# Generated at 2022-06-14 09:50:34.155408
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import os
    import zipfile

    with tempfile.NamedTemporaryFile('w', suffix='.zip') as zip:
        zip_archive = zipfile.ZipFile(zip, 'w')
        zip_archive.writestr('test_file1.txt', 'test string')
        zip_archive.writestr('test_file2.txt', 'test string')
        zip_archive.writestr('test_dir/test_dir_file1.txt', 'test string')
        zip_archive.writestr('test_dir/test_dir_file2.txt', 'test string')
        zip_archive.writestr('test_dir/test_deep_dir/test_deep_dir_file1.txt', 'test string')