

# Generated at 2022-06-14 09:41:02.199188
# Unit test for function match
def test_match():
    assert not match({'script': 'unzip file.zip -d folder'})
    assert match({'script': 'unzip file.zip'})
    assert match({'script': 'unzip file1.zip file2.zip file3.zip'})
    assert match({'script': 'unzip file.zip file1 file2'})
    assert match({'script': 'unzip file.zip -x file'})
    assert match({'script': 'unzip file.zip -x file1 file2 file3'})
    assert match({'script': 'unzip file.zip -x file1 file2 file3 -d unzip_folder'})

# Generated at 2022-06-14 09:41:08.233623
# Unit test for function match
def test_match():
    # Test that match() returns True for 'unzip file.zip'
    assert match(Command('unzip file.zip', '', None))
    # Test that match() returns True for 'unzip file'
    assert match(Command('unzip file', '', None))
    # Test that match() returns False for 'unzip -d directory file'
    assert not match(Command('unzip -d directory file.zip', '', None))

# Generated at 2022-06-14 09:41:14.387896
# Unit test for function side_effect
def test_side_effect():
    """
    This will test if the side_effect function does what it is supposed to do.
    """

    # This will create a temporary file
    tempfile = open("zipdir/file.txt", "w")
    tempfile.write("This is a temporary file")
    tempfile.close()

    # The side effect function should remove the previously created file
    side_effect("unzip zipfile.zip file.txt", None)
    assert not os.path.exists("zipdir/file.txt")

# Generated at 2022-06-14 09:41:19.078880
# Unit test for function match
def test_match():
    assert match(Command('unzip test.zip'))
    assert not match(Command('unzip -d test.zip'))
    assert match(Command('unzip test.zip test'))
    assert match(Command('unzip test'))
    assert not match(Command('unzip -d test'))

# Generated at 2022-06-14 09:41:27.158709
# Unit test for function match
def test_match():
    assert not match(Command('unzip -d .', '', '', ''))
    assert not match(Command('unzip -d', '', '', ''))
    assert not match(Command('unzip', '', '', ''))

    assert match(Command('unzip file.zip', '', '', ''))
    assert match(Command(u'unzip file.zip äää.ää', '', '', ''))
    assert not match(Command('unzip -d file.zip', '', '', ''))
    assert match(Command('unzip -j file.zip', '', '', ''))
    assert match(Command('unzip -t file.zip', '', '', ''))
    assert match(Command('unzip -T file.zip', '', '', ''))

    # test for file in current directory
    current

# Generated at 2022-06-14 09:41:29.947852
# Unit test for function match
def test_match():
    assert match(Command('unzip test.zip', '', '')) == True
    assert match(Command('unzip test.zips', '', '')) == False
    assert match(Command('unzip test.zip', '', '')) == True
    assert match(Command('unzip -t test.zip', '', '')) == False
    assert match(Command('unzip -d test.zip', '', '')) == False

# Generated at 2022-06-14 09:41:42.486646
# Unit test for function side_effect
def test_side_effect():
    if not os.path.isdir("test_side_effect_test"):
        os.makedirs("test_side_effect_test")
    os.chdir("test_side_effect_test")
    test_file = "foo.txt"
    with open(test_file, 'w') as foo:
        foo.write("bar")
    zip_file = "foo.zip"
    with zipfile.ZipFile(zip_file, 'w') as foo_zip:
        foo_zip.write(test_file)
    old_cmd = Command("unzip foo.zip", "")
    command = Command("unzip -d foo foo.zip", "")
    side_effect(old_cmd, command)
    assert not os.path.isfile(test_file)
    os.chdir("..")
   

# Generated at 2022-06-14 09:41:50.875433
# Unit test for function side_effect
def test_side_effect():
    assert side_effect('unzip badzip.zip', 'unzip badzip.zip -d badzip | cat')
    assert side_effect('unzip badzip.zip', 'unzip badzip.zip -d | cat')
    # test new command
    assert get_new_command('unzip badzip.zip') == 'unzip badzip.zip -d badzip'
    assert get_new_command('unzip badzip.zip --option') == 'unzip badzip.zip --option -d badzip'
    assert get_new_command('unzip badzip.zip -d notbadzip') == 'unzip badzip.zip -d badzip'

# Generated at 2022-06-14 09:42:01.211095
# Unit test for function side_effect
def test_side_effect():
    archive = zipfile.ZipFile('test_archive.zip', 'w')
    archive.write('test_file_1.txt')
    archive.write('test_file_2.txt')
    archive.write('test_file_3.txt')
    archive.close()

    script = 'unzip test_archive.zip'
    new_script = get_new_command(FakeCommand(script, ''))
    side_effect(FakeCommand(script, ''), FakeCommand(new_script, ''))

    # Checks that the three files were removed from the current directory
    assert not os.path.isfile('test_file_1.txt')
    assert not os.path.isfile('test_file_2.txt')
    assert not os.path.isfile('test_file_3.txt')

# Generated at 2022-06-14 09:42:05.691808
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', '', '')) == True
    assert match(Command('unzip -d file.zip', '', '')) == False
    assert match(Command('unzip file', '', '')) == False
    assert match(Command('unzip file.zip file file', '', '')) == False


# Generated at 2022-06-14 09:42:25.187490
# Unit test for function side_effect
def test_side_effect():
    old_cmd = u'unzip -o /home/user/foo.zip'
    command = u'unzip -o -d /home/user/foo /home/user/foo.zip'

    command_script_parts = command.split()
    side_effect(old_cmd, command)

# Generated at 2022-06-14 09:42:37.552904
# Unit test for function side_effect
def test_side_effect():
    from .helper import capture_both

    @for_app('unzip')
    def match(_):
        return True

    with capture_both() as (out, err):
        files = []
        test_dir = tempfile.mkdtemp()
        os.chdir(test_dir)
        for x in range(10):
            with open(str(x), 'w') as f:
                f.write('')
            files.append(str(x))
        archive = zipfile.ZipFile('test.zip', 'w')
        for file in files:
            archive.write(file)
        archive.close()
        side_effect(u'unzip test.zip', u'unzip test.zip -d test')

# Generated at 2022-06-14 09:42:45.812121
# Unit test for function match
def test_match():
    assert match(Command('unzip -b file.zip'))
    assert match(Command('unzip file.zip'))
    assert match(Command('unzip -qqq file.zip'))
    assert match(Command('unzip -qqq file.zip file_in_archive.txt'))

    assert not match(Command('unzip -d unzipped file.zip'))
    assert not match(Command('unzip file_no_zip.txt'))

# Generated at 2022-06-14 09:42:49.890049
# Unit test for function match
def test_match():
    exception = Command('unzip ./Documents/TheFUCK-master.zip')
    assert match(exception)
    exception = Command('unzip ./Documents/TheFUCK-master.zip ./Documents/')
    assert match(exception) is False


# Generated at 2022-06-14 09:42:52.306809
# Unit test for function side_effect
def test_side_effect():
    side_effect('unzip z.zip',
                'unzip z.zip -d z')

# Generated at 2022-06-14 09:42:56.642491
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', ''))
    assert match(Command('unzip file', ''))
    assert not match(Command('unzip -d folder file.zip', ''))


# Generated at 2022-06-14 09:43:04.150106
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip', '', 'unzip:  cannot find or open file.zip, file.zip.zip or file.zip.ZIP'))
    assert match(Command('unzip file.zip', '', 'unzip:  cannot find or open .zip, .zip.zip or .zip.ZIP'))
    assert not match(Command('unzip file.zip', '', 'unzip:  cannot find or open .zip', False))



# Generated at 2022-06-14 09:43:06.819045
# Unit test for function side_effect
def test_side_effect():
    import mock
    side_effect('unzip file1.zip', 'unzip -d dir file1.zip')
    mock.assert_called_once_with('dir', 'file1')

# Generated at 2022-06-14 09:43:16.265677
# Unit test for function side_effect
def test_side_effect():
    import shutil

    try:
        os.mkdir('test_dir')
        with open('test_dir/test_file', 'w') as f:
            f.write('test content')
        with zipfile.ZipFile('test_dir.zip', 'w') as archive:
            archive.write('test_dir/test_file')
        side_effect(None, 'unzip test_dir.zip')
        assert not os.path.isfile('test_dir/test_file')
    finally:
        shutil.rmtree('test_dir')
        os.remove('test_dir.zip')

# Generated at 2022-06-14 09:43:26.297679
# Unit test for function side_effect
def test_side_effect():
    from thefuck.rules.unzip import side_effect
    from thefuck.shells import Shell
    from thefuck.types import Command
    import shutil
    import tempfile


# Generated at 2022-06-14 09:43:45.435869
# Unit test for function match
def test_match():
    assert match(Command("unzip file.zip", ""))
    assert match(Command("unzip file.zip -d /tmp", ""))
    assert not match(Command("unzip -d file.zip", ""))
    assert not match(Command("unzip -d file.zip -d /tmp", ""))
    assert not match(Command("zip file.zip", ""))

# Generated at 2022-06-14 09:43:56.833120
# Unit test for function side_effect
def test_side_effect():
    os.mkdir('foo')
    with open('foo/a', 'w') as file:
        file.write('')
    with open('foo/b', 'w') as file:
        file.write('')
    with open('foo/c', 'w') as file:
        file.write('')

    with zipfile.ZipFile('foo.zip', 'w') as zip_file:
        zip_file.write('foo/a')
        zip_file.write('foo/b')
        zip_file.write('foo/c')

    test_command = 'unzip foo.zip'
    assert side_effect(test_command, test_command) is None
    assert os.path.exists('foo/a') == False
    assert os.path.exists('foo/b') == False

# Generated at 2022-06-14 09:44:03.902034
# Unit test for function match
def test_match():
    # No -d in script
    command = Command('unzip doc.zip', '', '')
    assert match(command)
    assert not _zip_file(command)

    # -d in script
    command = Command('unzip -d doc.zip', '', '')
    assert not match(command)

    # Bad ZIP file
    command = Command('unzip doc.zip', '', '')
    assert match(command)
    assert _zip_file(command) == 'doc.zip'


# Unit tests for function get_new_command

# Generated at 2022-06-14 09:44:14.742235
# Unit test for function side_effect
def test_side_effect():
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_dir = tempfile.mkdtemp()
        f.write(zipfile.ZipInfo('test_file.txt').encode('utf-8'))
        f.write(u'test'.encode('utf-8'))
        f.seek(0)
        zip_file = f.name
        zip_dir = os.path.dirname(zip_file)
        output_dir = os.path.join(zip_dir, 'test_dir')
        old_cmd = 'unzip {}'.format(zip_file)
        command = 'unzip -d {} {}'.format(output_dir, zip_file)
        temp_file = os.path.join(zip_dir, 'test_file.txt')
       

# Generated at 2022-06-14 09:44:27.419983
# Unit test for function match
def test_match():
    assert _is_bad_zip('test_zipfile/test.zip'), \
           "test_zipfile/test.zip has more than 1 file"
    assert not _is_bad_zip('test_zipfile/test_single_file.zip'), \
           "test_zipfile/test_single_file.zip has more than 1 file"
    assert not _is_bad_zip('test_zipfile/test_folder/test.zip'), \
           "test_zipfile/test_single_file/test.zip has more than 1 file"

    assert match(Command("unzip test.zip", "", None))
    assert not match(Command("unzip -d test test.zip", "", None))

    assert match(Command("unzip test", "", None))

# Generated at 2022-06-14 09:44:29.091950
# Unit test for function side_effect
def test_side_effect():
    side_effect(
        Mock(script='unzip foo.zip'),
        Mock(script='unzip -d foo foo.zip')
    )

# Generated at 2022-06-14 09:44:45.079365
# Unit test for function match
def test_match():
    assert not match(Command('unzip -a somearg.zip', ''))
    assert not match(Command('unzip -a /tmp/some/arg.zip', ''))
    assert not match(Command('unzip -a somearg.zip -d somearg', ''))
    assert match(Command('unzip -a somearg.zip somearg', ''))
    assert match(Command('unzip -a /tmp/some/arg.zip /tmp/some/arg', ''))
    assert match(Command('unzip -a somearg.zip -d /tmp/some/arg', ''))
    assert match(Command('unzip -a somearg.zip', ''))
    assert match(Command('unzip somearg', ''))

# Generated at 2022-06-14 09:44:53.748527
# Unit test for function match
def test_match():
    assert _is_bad_zip('/path/to/bad.zip') is True
    assert _is_bad_zip('/path/to/good.zip') is False
    assert match(Command("unzip file.zip")) is False
    assert match(Command("unzip file.zip", "unzip file.zip")) is False
    assert match(Command("unzip file.zip", "unzip: file.zip bad zip file")) is True
    assert match(Command("unzip file.zip", "unzip: archive doesn't exist")) is False
    assert match(Command("unzip file.zip", "unzip: file.zip: no such file or directory")) is False
    assert match(Command("unzip file.zip", "unzip: file.zip: not found or empty")) is False

# Generated at 2022-06-14 09:45:01.737592
# Unit test for function side_effect
def test_side_effect():
    # Create test file
    old_cmd = ""
    old_cmd_file = open("test_unzip.py", "w+") # Create test file
    old_cmd_file.write(old_cmd)
    old_cmd_file.close()

    # Test side effect
    test_cmd = ""
    side_effect(old_cmd, test_cmd)

    # Assert
    assert test_cmd == ""

    # Clean-up
    os.remove("test_unzip.py")

# Generated at 2022-06-14 09:45:13.786646
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil
    import os

    dirpath = tempfile.mkdtemp()
    filepath = os.path.join(dirpath, 'test')
    with open(filepath, 'w'):
        pass

    class Command(object):
        def __init__(self, script_parts):
            self.script_parts = script_parts

    with open(filepath, 'w') as f:
        f.write('toto')
    command = Command(['unzip', 'test.zip', '-d', dirpath])
    side_effect(command, command)
    assert os.path.isfile(filepath)
    assert open(filepath, 'r').read() == 'toto'
    shutil.rmtree(dirpath)

# Generated at 2022-06-14 09:45:48.886196
# Unit test for function side_effect
def test_side_effect():
    file = "README.md"
    os.chdir("/tmp")
    with open(file, 'w'):
        side_effect("", "unzip -d {} {}".format(file, file))
    assert file not in os.listdir(".")

# Generated at 2022-06-14 09:45:57.501252
# Unit test for function match
def test_match():
    assert match(Command('unzip test.zip'))
    assert match(Command('unzip file.zip'))
    assert match(Command('unzip -o test.zip'))
    assert not match(Command('unzip -d test test.zip'))
    assert match(Command('unzip -d /home/test/ test.zip'))
    assert not match(Command('unzip -o -d test test.zip'))
    assert match(Command('unzip -o -d /home/test/ test.zip'))
    assert match(Command('unzip -o -d /home/test/ file.zip'))
    assert match(Command('unzip -o -d /home/test/ test_file.zip'))
    assert not match(Command('unzip -o -d /home/test/ test_file'))
   

# Generated at 2022-06-14 09:46:12.791140
# Unit test for function side_effect
def test_side_effect():
    import os
    import os.path
    import shutil
    import tempfile
    import zipfile
    import thefuck.specific.unzip as unzip
    # Create a single file in a temporary directory and a zipfile
    # containing this file
    tempdir = tempfile.mkdtemp()
    file = os.path.join(tempdir, 'test_file')

    with open(file, 'w') as f:
        f.write('test_file')
    with zipfile.ZipFile(os.path.join(tempdir, 'test.zip'), 'w') as zipf:
        zipf.write('test_file')

    # Test if the side_effect work

# Generated at 2022-06-14 09:46:24.846885
# Unit test for function match
def test_match():

    # Function match should return False if the wrong arguments are specified
    assert match(Command('unzip -d testing', '', '')) is False

    # Function match should return False if not a zip file is specified
    assert match(Command('unzip testing', '', '')) is False

    # Function match should return True if multiple files in zip file
    test_zip = open('testing.zip', 'w')

# Generated at 2022-06-14 09:46:30.016478
# Unit test for function side_effect
def test_side_effect():
    if os.path.exists('test_side_effect.zip'):
        os.remove('test_side_effect.zip')
    if os.path.exists('file'):
        os.remove('file')
    archive = zipfile.ZipFile('test_side_effect.zip', 'w')
    archive.writestr('file', '')
    archive.close()
    assert not os.path.exists('file')
    side_effect('', 'unzip test_side_effect.zip')
    assert os.path.exists('file')
    os.remove('test_side_effect.zip')
    os.remove('file')

# Generated at 2022-06-14 09:46:43.427485
# Unit test for function match
def test_match():
    ret = match(Command('unzip file.zip'))
    assert ret == False
    ret = match(Command('unzip file.zip -x test.txt'))
    assert ret == False
    ret = match(Command('unzip file.zip test.txt'))
    assert ret == False
    ret = match(Command('unzip file.zip test.txt test.txt.bak -x test.txt.bak'))
    assert ret == False
    ret = match(Command('unzip file.zip test.txt.bak -x test.txt test.txt.bak'))
    assert ret == False
    ret = match(Command('unzip file.zip test.txt.bak -x test.txt'))
    assert ret == False

# Generated at 2022-06-14 09:46:53.236865
# Unit test for function match
def test_match():
    assert match(Command('unzip file.zip'))
    assert match(Command('unzip file.zip -L foo'))
    assert match(Command('unzip foo'))
    assert match(Command('unzip baz.zip bar.zip'))
    assert match(Command('unzip foo bar.zip'))
    assert match(Command('unzip foo/baz.zip'))
    assert not match(Command('unzip -d foo'))
    assert not match(Command('foo.zip'))
    assert not match(Command('unzip foo bar'))



# Generated at 2022-06-14 09:47:07.175165
# Unit test for function side_effect
def test_side_effect():
    import pytest
    import zipfile
    from thefuck.types import Command
    from thefuck.main import wrap_settings
    from thefuck.rules.unzip_single_file import side_effect
    from thefuck.rules.unzip_single_file import get_new_command

    # prepare zip-file
    with open('test.zip', 'wb') as archive:
        writer = zipfile.ZipFile(archive, mode='w')
        writer.write('test.txt')
        writer.close()

    # prepare file to unzip
    with open('test.txt', 'w') as test_file:
        test_file.write("some text")
    test_file.close()

    # prepare environment
    settings = wrap_settings({})
    command = Command("unzip test.zip", "ERROR")

    # execute


# Generated at 2022-06-14 09:47:19.933690
# Unit test for function side_effect
def test_side_effect():
    """
    The function side_effect should remove the file in the archive
    if it already exists.
    """
    folder = tempfile.mkdtemp()
    file = os.path.join(folder, 'file')

    # Create %folder%/file
    with open(file, 'w') as f:
        f.write('content')

    # Create %folder%/archive.zip
    with zipfile.ZipFile(os.path.join(folder, 'archive.zip'), 'w') as archive:
        archive.write('file')

    old_cmd = Command(script='unzip {}/archive.zip'.format(folder),
                      stdout='', stderr='')
    side_effect(old_cmd, None)

    # %folder%/file should be removed
    assert not os.path.isfile(file)

# Generated at 2022-06-14 09:47:30.179961
# Unit test for function side_effect
def test_side_effect():
    with TemporaryDirectory() as tmpdir:
        # Create a zip file
        with zipfile.ZipFile(os.path.join(tmpdir, 'test.zip'), 'w') as archive:
            archive.write(os.path.join(tmpdir, 'test.txt'), 'test.txt')

        # Extract it
        with chdir(tmpdir):
            old_cmd = Command('unzip test.zip', 'unzip test.zip', 'unzip test.zip')
            side_effect(old_cmd, old_cmd)

        # Check that the content has been extracted
        assert os.path.exists(os.path.join(tmpdir, 'test.txt'))

# Generated at 2022-06-14 09:48:34.638582
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    import shutil

    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)

    try:
        # create a file
        fname = 'foobar'
        f = open(fname, 'w')
        f.write('')
        f.close()

        # zip it and call the function
        archive = zipfile.ZipFile('f1.zip', 'w')
        archive.write('foobar')
        archive.close()
        side_effect('', 'unzip -d f1.zip')

        # check if it still exists
        assert not os.path.exists(fname)
    finally:
        os.chdir(test_dir)
        shutil.rmtree(test_dir)

# Generated at 2022-06-14 09:48:41.276700
# Unit test for function side_effect
def test_side_effect():
    import shutil
    from thefuck.utils import temp_dir

    with temp_dir() as tempdir:
        shutil.copyfile('tests/fixtures/warning', tempdir + '/warning')

        # Error should not be raised
        side_effect('unzip some_zip.zip', 'unzip some_zip.zip')
        side_effect('unzip some_zip.zip', 'unzip some_zip.zip')

        # Error should not be raised when using -d option
        side_effect('unzip -d some_zip some_zip.zip', 'unzip -d some_zip some_zip.zip')
        side_effect('unzip -d some_zip some_zip.zip', 'unzip -d some_zip some_zip.zip')

# Generated at 2022-06-14 09:48:52.365605
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    with tempfile.NamedTemporaryFile() as tf:
        with zipfile.ZipFile(tf.name, 'w') as archive:
            archive.writestr('file1.txt', 'file 1 content')
            archive.writestr('file2.txt', 'file 2 content')
        with open('file1.txt', 'w') as f:
            f.write('overwritten content')
        os.makedirs('subfolder')
        with open('subfolder/file3.txt', 'w') as f:
            f.write('file 3 content')
        command = type('Command', (object,), {'script': 'unzip {}'.format(tf.name)})
        side_effect(command, command)
        assert not os.path.exists('file1.txt')

# Generated at 2022-06-14 09:48:57.853755
# Unit test for function side_effect
def test_side_effect():
    import tempfile
    old_dir = os.getcwd()
    old_home = os.environ.get('HOME')
    old_pwd = os.environ.get('PWD')
    os.environ['HOME'] = os.environ['PWD'] = tempfile.gettempdir()
    zip_file = os.path.join(tempfile.gettempdir(), 'test_side_effect.zip')
    with open(zip_file, mode='wb') as f:
        with zipfile.ZipFile(f, 'w') as zip:
            os.chdir(tempfile.gettempdir())
            try:
                zip.writestr('TEST', b'TEST')
            finally:
                os.chdir(old_dir)

# Generated at 2022-06-14 09:49:02.326481
# Unit test for function match
def test_match():
    assert not match(Command('unzip file.zip'))

    assert match(Command('unzip file1.zip file2.zip'))

    assert match(Command('unzip -j file1.zip file2.zip'))

    assert match(Command('unzip -a file1.zip file2.zip'))


# Generated at 2022-06-14 09:49:06.231343
# Unit test for function match
def test_match():
    from tests.utils import Command

    assert match(Command('unzip file.zip', 'zeh'))
    assert not match(Command('unzip file.zip a b -d out', 'zeh'))
    assert not match(Command('unzip file.zip -d out', 'zeh'))



# Generated at 2022-06-14 09:49:13.021725
# Unit test for function match
def test_match():
    """
    Test function `match`
    Test _is_bad_zip
    Test _zip_file
    Test get_new_command
    Test side_effect
    """

    # Test _is_bad_zip
    # Test case: tgz file
    assert not _is_bad_zip(
        os.path.join(os.path.dirname(__file__), '..', '..', 'examples',
                     'tar.tgz'))
    # Test case: zip file with one file in it
    assert not _is_bad_zip(
        os.path.join(os.path.dirname(__file__), '..', '..', 'examples',
                     'one.zip'))
    # Test case: zip file with mutiple files in it

# Generated at 2022-06-14 09:49:20.792578
# Unit test for function side_effect
def test_side_effect():
    os.chdir("/tmp/")
    list_before = os.listdir("/tmp/")
    side_effect(0, "unzip -d /tmp/ foo.zip")
    # Check that the directory foo has been created during the side-effect
    list_after = os.listdir("/tmp/")
    assert 'foo' in list_after
    # Check that list_before contains the elements of list_after
    assert all(elem in list_after for elem in list_before)

# Generated at 2022-06-14 09:49:31.716701
# Unit test for function match
def test_match():
    assert match(Command(script="unzip foo.zip"))
    assert match(Command(script="unzip folder.zip"))
    assert match(Command(script="unzip -t folder.zip"))
    assert not match(Command(script="unzip -d folder.zip"))
    assert not match(Command(script="unzip -d folder folder.zip"))
    assert not match(Command(script="unzip -d folder1 folder2.zip"))
    assert not match(Command(script="unzip -d folder1 -d folder2.zip"))


# Generated at 2022-06-14 09:49:43.322830
# Unit test for function side_effect
def test_side_effect():
    """Test to check whether side_effect works."""
    # Required modules
    import shutil
    import tempfile

    # Make a temporary directory and change to it
    tmpdir = tempfile.mkdtemp()
    olddir = os.getcwd()
    os.chdir(tmpdir)

    # Make some test files:
    #     directory/
    #     directory/file1
    #     directory/file2
    #     directory/sub/file3
    #     directory/sub/file4
    os.mkdir('directory')
    with open('directory/file1', 'w') as fp:
        fp.write('file1')
    with open('directory/file2', 'w') as fp:
        fp.write('file2')
    os.mkdir('directory/sub')