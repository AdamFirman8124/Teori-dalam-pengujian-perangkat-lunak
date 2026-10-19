

# Generated at 2022-06-14 10:13:53.763265
# Unit test for function get_new_command
def test_get_new_command():
    assert_equals(get_new_command(Command('rm dir', '', 'fatal: not removing \'dir\' recursively without -r')),
                u'git rm -r dir')

# Generated at 2022-06-14 10:13:59.385571
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm src/test.txt', 'fatal: not removing \'src/test.txt\' recursively without -r')
    new_command = get_new_command(command)
    assert new_command.lower() == 'git rm -r src/test.txt'.lower(), new_command

# Generated at 2022-06-14 10:14:04.833258
# Unit test for function match
def test_match():
    assert match(Command('git rm a'))
    assert match(Command('git rm a', 'fatal: not removing \'a\' recursively without -r'))
    assert not match(Command('git rm a', 'fatal: not removing \'a\' recursively without -r', 'fatal: not removing \'a\' recursively without -r'))


# Generated at 2022-06-14 10:14:12.465089
# Unit test for function match
def test_match():
    assert match(Command('git rm -r folder',
                         "fatal: not removing 'folder' recursively without -r"))
    assert match(Command('git rm folder',
                         "fatal: not removing 'folder' recursively without -r"))
    assert not match(Command('git rm -r folder',
                         "fatal: not removing 'folder' recursively"))
    assert not match(Command('git rm folder',
                         "fatal: not removing 'folder' recursively"))


# Generated at 2022-06-14 10:14:18.586998
# Unit test for function match
def test_match():
    # Test scenario where match returns false
    result = match(Command('git log', '', 'fatal: not removing \'file.txt\' recursively without -r'))
    assert result != True

    # Test scenario where match returns true
    result = match(Command('git rm file.txt', '', 'fatal: not removing \'file.txt\' recursively without -r'))
    assert result == True

# Generated at 2022-06-14 10:14:22.847799
# Unit test for function match
def test_match():
    from thefuck.rules.git_rm_fatal import match

    assert match(Command('git rm /tmp/file'))
    assert not match(Command('git rm other_file'))


# Generated at 2022-06-14 10:14:30.241903
# Unit test for function match
def test_match():
    # Test when git rm is in command
    assert match(Command('git rm file.txt', ''))
    assert not match(Command('git add file.txt', ''))

    # Test when git rm is in command and there is a failure
    assert match(Command('git rm file.txt',
                         'fatal: not removing "file.txt" '\
                         'recursively without -r'))
    assert not match(Command('git rm file.txt', 'error: file not found'))


# Generated at 2022-06-14 10:14:35.727238
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm -f'
    output = ("fatal: not removing 'abc' recursively without -r\n"
              "Did you mean 'rm'?")
    comm = Command(script, output)
    assert get_new_command(comm) == u'git rm -f -r'

# Generated at 2022-06-14 10:14:39.709637
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r\n')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r foo'

# Generated at 2022-06-14 10:14:42.700581
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r .*', '', '')
    command1 = get_new_command(command)
    assert(command1 == command.script)

# Generated at 2022-06-14 10:14:56.382133
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('git rm hello')) == \
        'git -r rm hello'

    assert get_new_command(Command('git rm hello', 'fatal: not removing \'hello\'')) == \
        'git -r rm hello'

    assert get_new_command(Command('git rm hello', 'fatal: not removing \'hello\' recursively without -r')) == \
        'git -r rm hello'

# Generated at 2022-06-14 10:15:00.436230
# Unit test for function match
def test_match():
    assert match(Command(stderr='fatal: not removing \'functions.pyc\' recursively without -r'))
    assert not match(Command(stderr='nothing happened'))


# Generated at 2022-06-14 10:15:04.717892
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf a', 'fatal: not removing \'a\' recursively without -r')) == 'git rm -rf -r a'

# Generated at 2022-06-14 10:15:11.078208
# Unit test for function get_new_command
def test_get_new_command():
    def test(script, output, assert_parts):
        new_command = get_new_command(Command(script, output))
        assert all(part in new_command for part in assert_parts)
    test('git rm hello.py',
    'fatal: not removing \'hello.py\' recursively without -r',
    ['rm', '-r', 'hello.py'])

# Generated at 2022-06-14 10:15:14.428946
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command(script='git rm foo bar', output='fatal: not removing '' recursively without -r')) == 'git rm -r foo bar'

# Generated at 2022-06-14 10:15:17.577770
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm non_existing_file', 'fatal: not removing \'non_existing_file\' recursively without -r')) == 'git rm -r non_existing_file'

# Generated at 2022-06-14 10:15:21.191198
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file') == 'git rm -r file'
    assert get_new_command('git rm -r file') == 'git rm -r file'


# Generated at 2022-06-14 10:15:23.134993
# Unit test for function match
def test_match():
    assert match(command.Command('git rm foo'))
    assert not match(command.Command('fatal: not removing "foo" recursively without -r'))

# Generated at 2022-06-14 10:15:27.269049
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(' git rm src', 'fatal: not removing \'src\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -r src'

# Generated at 2022-06-14 10:15:35.836621
# Unit test for function get_new_command
def test_get_new_command():
    import os
    import shutil
    import tempfile
    # Create a temporary directory
    path = tempfile.mkdtemp()
    try:
        # Create a file in the temporary directory
        test_file = open(os.path.join(path, 'file1'), 'w')
        test_file.close()

        assert get_new_command(Command('git rm file1', from_improper_dir=True)) == 'git rm -r file1'

    finally:
        # Remove the directory after the test
        shutil.rmtree(path)

# Generated at 2022-06-14 10:15:46.954496
# Unit test for function match
def test_match():
    assert match(Command('git rm -r {file}', output='fatal: not removing \'{file}\' recursively without -r'))
    assert not match(Command('git rm -r {file}', output='fatal: not removing \'{file}\' directory without -r'))
    assert not match(Command('git rm -rf {file}', output='fatal: not removing \'{file}\' recursively without -r'))
    assert not match(Command('svn rm -r {file}', output='fatal: not removing \'{file}\' recursively without -r'))

# Generated at 2022-06-14 10:15:56.592526
# Unit test for function get_new_command
def test_get_new_command():
    command_test = Command('git rm test')
    command_test.script_parts = ['git', 'rm', 'test']
    command_test.output = "fatal: not removing 'test' recursively without -r"
    assert get_new_command(command_test).script == u'git rm -r test'
    command_test = Command('git rm -f test')
    command_test.script_parts = ['git', 'rm', '-f', 'test']
    command_test.output = "fatal: not removing 'test' recursively without -r"
    assert get_new_command(command_test).script == u'git rm -r -f test'

# Generated at 2022-06-14 10:16:02.043823
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'bar\' recursively without -r\n'))
    assert not match(Command('git rm foo', ''))
    assert not match(Command('svn rm foo',
                             'fatal: not removing \'bar\' recursively without -r\n'))


# Generated at 2022-06-14 10:16:06.784974
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    script = ['git', 'rm', '-r']
    output = "fatal: not removing 'config/database.yml' recursively without -r\n"
    assert get_new_command(Command(script, output)) == 'git rm -r -r'

# Generated at 2022-06-14 10:16:09.170160
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm thing', 'foo', 'bar')) == 'git rm -r thing'

# Generated at 2022-06-14 10:16:15.647757
# Unit test for function match
def test_match():
	# Test for positive condition
	assert match(Command('git rm -rf .', 'fatal: not removing \'../../Desktop/scrape/../scrape\' recursively without -r', '/home/username/Documents/scrape'))
	# Test negative condition
	assert not match(Command('git rm hello.txt', '', '/home/username/Documents/scrape'))


# Generated at 2022-06-14 10:16:19.159976
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf dir/', stderr='fatal: not removing \'dir/\' recursively without -r')) == 'git rm -rf -r dir/'

# Generated at 2022-06-14 10:16:30.402545
# Unit test for function match
def test_match():
    """
    Function match is tested
    """

    assert(match(Command(script = 'git rm -r -f *.py',
        output = "fatal: not removing 'a.py' recursively without -r")) == True)

    assert(match(Command(script = 'git rm -r -f *.py',
        output = "fatal: not removing 'a.py' recursively without -rf")) == False)

    assert(match(Command(script = 'git rm -r -f *.py',
        output = "fatal: not removing 'a.py' recursively without -r")) == True)

    assert(match(Command(script = 'git rm -f *.py',
        output = "fatal: not removing 'a.py' recursively without -r")) == False)


# Generated at 2022-06-14 10:16:40.627776
# Unit test for function match
def test_match():
    assert match(Command('git rm -r filename', u'fatal: not removing \'filename\' recursively without -r'))
    assert not match(Command('git rm -r filename', u'fatal: not removing file recursively'))
    assert not match(Command('git rm -r filename', u'fatal: not removing file'))
    assert not match(Command('git rm filename', u'fatal: not removing file recursively without -r'))
    assert not match(Command('git rm filename', u'fatal: not removing file'))
    assert not match(Command('git add filename', u'fatal: not removing file'))


# Generated at 2022-06-14 10:16:43.071769
# Unit test for function match
def test_match():
    assert match(Command('git rm -r'))
    assert not match(Command('git rm -rf'))


# Generated at 2022-06-14 10:16:53.922795
# Unit test for function match
def test_match():
    # Test match function value
    assert match(Command("git rm test/fuck.pyc", "fatal: not removing 'test/fuck.pyc' recursively without -r\nrm 'test/fuck.pyc'"))
    assert not match(Command("git rm test/fuck.pyc", ""))
    # Test match function value
    assert not match(Command("git rm -r test/fuck.pyc", "fatal: not removing 'test/fuck.pyc' recursively without -r\nrm 'test/fuck.pyc'"))
    assert not match(Command("git rm -r test/fuck.pyc", ""))
    # Test match function value
    assert not match(Command("git rm test", "fatal: not removing 'test' recursively without -r\nrm 'test'"))

# Generated at 2022-06-14 10:17:00.720540
# Unit test for function match
def test_match():
    assert(match(Command('git rm filename',
                         'fatal: not removing \'<file>\' recursively without -r')))
    assert(not match(Command('git rm -r filename',
                             'fatal: not removing \'<file>\' recursively without -r')))
    assert(not match(Command('git rm -rf filename',
                             'fatal: not removing \'<file>\' recursively without -r')))



# Generated at 2022-06-14 10:17:02.690458
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm ") == "git rm -r "

# Generated at 2022-06-14 10:17:07.216379
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf src', 'error: unable to stat \'src\': Permission denied\n'))
    assert not match(Command('git rm -rf src', 'fatal: not removing \'src\' recursively without -r\n'))

# Generated at 2022-06-14 10:17:10.059720
# Unit test for function match
def test_match():
    assert match(Command('git rm non_existing_file',
                         "fatal: not removing 'non_existing_file' recursively without -r"))



# Generated at 2022-06-14 10:17:16.806911
# Unit test for function match
def test_match():
    assert not match(Command('git rm -rf gdjksg', '', ''))
    assert not match(Command('git rm --cached gdjksg', '', ''))
    assert not match(Command('git rm gdjksg', '', ''))
    assert match(Command('git rm ksdjf', 'fatal: not removing \'ksdjf\' recursively without -r', ''))



# Generated at 2022-06-14 10:17:21.046449
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file name with space')) == u'git rm -r file name with space'
    assert get_new_command(Command('git rm new_directory')) == u'git rm -r new_directory'

# Generated at 2022-06-14 10:17:25.224515
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 
    '''
    fatal: not removing 'file' recursively without -r
    '''))
    assert not match(Command('git rm file', 'git: \'rm\' is not a git command.'))

# Generated at 2022-06-14 10:17:29.408423
# Unit test for function match
def test_match():
    assert match(Command('git rm /path/to/dir',
                         'fatal: not removing \'/path/to/dir\' recursively without -r\n',
                         '',
                         1))
    assert not match(Command('git commit', '', '', 1))

# Generated at 2022-06-14 10:17:31.087838
# Unit test for function match
def test_match():
    assert match(Command('git rm unneeded_file.py'))



# Generated at 2022-06-14 10:17:40.247078
# Unit test for function get_new_command
def test_get_new_command():
    COMMAND_OUTPUT = "fatal: not removing 'path/to/file/name_of_file/' recursively without -r"
    assert get_new_command(Command('git rm path/to/file/name_of_file/',
                                   COMMAND_OUTPUT)) == 'git rm -r path/to/file/name_of_file/'

# Generated at 2022-06-14 10:17:49.474082
# Unit test for function get_new_command
def test_get_new_command():
    thefuck.shells.shell = Mock(**{'from_shell.return_value': u'git add --all'})
    assert get_new_command(Command('git rm foo/bar', 'fatal: not removing \'foo/bar\' recursively without -r\n')) == u'git rm -r foo/bar'

# Generated at 2022-06-14 10:17:52.794255
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', '', 'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo', '', ''))


# Generated at 2022-06-14 10:18:02.246835
# Unit test for function match
def test_match():
    assert match(Command('git rm folder', ''))
    assert match(Command('git rm folder', 'fatal: not removing \'folder\' recursively without -r\n'))
    assert match(Command('git rm -r folder', 'fatal: not removing \'folder\' recursively without -r\n'))
    assert not match(Command('git rm folder', 'fatal: not removing \'folder\' recursively without -r\n', ''))
    assert not match(Command('git rm folder', 'fatal: not removing \'folder\' recursively without -r\n', '', stderr='fatal: not removing \'folder\' recursively without -r\n'))
    assert not match(Command('git rm -r folder', 'fatal: not removing \'folder\' recursively without -r\n'))

# Generated at 2022-06-14 10:18:04.449629
# Unit test for function match
def test_match():
    command = Command('git rm -f LICENSE')
    assert(match(command)== True)


# Generated at 2022-06-14 10:18:07.658241
# Unit test for function match
def test_match():
    assert match(Command('git rm something', 'fatal: not removing \'something\' recursively without -r'))
    assert not match(Command('git rm something', 'fatal: not removing'))

# Generated at 2022-06-14 10:18:13.495663
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    # command, expected
    tests = [
        (Command(script=u'git rm myfile'), u'git rm -r myfile'),
        (Command(script=u'git r mye'), u'git r -r mye'),
        (Command(script=u'git remove myfile'), u'git remove -r myfile'),
        (Command(script=u'git delete myfile'), u'git delete -r myfile')
    ]

    for command, expected in tests:
        assert get_new_command(command) == expected

# Generated at 2022-06-14 10:18:20.764469
# Unit test for function match
def test_match():
    command = Command(' git branch -d branch', '', '')
    assert not match(command)

    command = Command('git rm abc', '', '')
    assert not match(command)

    command = Command('git rm abc', '', 'fatal: not removing \'abc\' recursively without -r')
    assert match(command)



# Generated at 2022-06-14 10:18:23.061963
# Unit test for function match
def test_match():
    assert match(Command('git rm', 'fatal: not removing \'/foo/bar\' recursively without -r'))

# Generated at 2022-06-14 10:18:27.094504
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('echo “fatal: not removing ‘.’ recursively without -r”', '')
    assert get_new_command(command) == 'git rm -r .'

# Generated at 2022-06-14 10:18:37.047158
# Unit test for function get_new_command
def test_get_new_command():
    """Test function get_new_command of the git plugin when input is wrong."""
    from thefuck.types import Command

    assert True == match(Command(' git rm /usr/local/bin/git',
                                 'fatal: not removing \'/usr/local/bin/git\' recursively without -r'))
    assert 'git rm -r /usr/local/bin/git' == get_new_command(Command(' git rm /usr/local/bin/git',
                                                                     'fatal: not removing \'/usr/local/bin/git\' recursively without -r'))

# Generated at 2022-06-14 10:18:43.575503
# Unit test for function match
def test_match():
    assert match(commands.Command('git rm -r test'))
    assert match(commands.Command('git rm -r test', "fatal: not removing 'test' recursively without -r"))
    assert not match(commands.Command('ls'))
    assert not match(commands.Command('git rm test', "failed: Could not remove test"))


# Generated at 2022-06-14 10:18:45.973045
# Unit test for function match
def test_match():
	commands = ['git rm fsd']
	for command in commands:
		yield isMatch, command



# Generated at 2022-06-14 10:18:48.945790
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r folder/subfolder')
    assert get_new_command(command) == "git rm -r folder/subfolder"

# Generated at 2022-06-14 10:18:52.194531
# Unit test for function match
def test_match():
    assert match(Command('git rm -r branch_name',
                         'fatal: not removing \'branch_name\' recursively without -r'))


# Generated at 2022-06-14 10:18:57.769516
# Unit test for function match
def test_match():
    assert match(Command('git rm -f test'))
    assert not match(Command('git rm -f test', 'fatal: not removing ''test'' recursively without -r'))
    assert not match(Command('git rm -f test', 'fatal: not removing test recursively without -r'))

# Generated at 2022-06-14 10:19:04.302410
# Unit test for function match
def test_match():
	# Create instance of Command class.
	command1 = Command('git rm dir', "fatal: not removing 'dir/' recursively without -r", '')
	command2 = Command('git rm file', "fatal: not removing 'file' recursively without -r", '')
	command3 = Command('git rm file dir', "fatal: not removing 'file' recursively without -r\nfatal: not removing 'dir/' recursively without -r", '')

	# Assert that match function returns expected results
	assert False == match(command1)
	assert False == match(command2)
	assert True == match(command3)



# Generated at 2022-06-14 10:19:08.514864
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    command = Command('git rm -rf test', 'fatal: not removing \'test\' recursively without -r')
    assert 'git rm -r -rf test' == get_new_command(command)

# Generated at 2022-06-14 10:19:12.659198
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm testfile'
    command = Command('{}'.format(script), script)
    assert match(command)
    assert get_new_command(command) == 'git rm -r testfile'


# Generated at 2022-06-14 10:19:20.460895
# Unit test for function match
def test_match():
	command = Command('git rm file', '', '', '', '')
	assert match(command)
	command = Command('git rm folder', '', 'fatal: not removing \'folder\' recursively without -r', '', '')
	assert match(command)
	command = Command('git rm nothing', '', '', '', '')
	assert not match(command)
	command = Command('rm nothing', '', 'fatal: not removing \'nothing\' recursively without -r', '', '')
	assert not match(command)


# Generated at 2022-06-14 10:19:29.650007
# Unit test for function match
def test_match():
    assert match(Command('git rm folder',
                         '/home/nico/test_git/test_git_repo/\nfatal: not removing \'folder\' recursively without -r\n',
                         '/home/nico/test_git/test_git_repo/\nfatal: not removing \'folder\' recursively without -r\n'))
    assert match(Command('git rm file',
                         '/home/nico/test_git/test_git_repo/\nfatal: not removing \'file\' recursively without -r\n',
                         '/home/nico/test_git/test_git_repo/\nfatal: not removing \'file\' recursively without -r\n'))


# Generated at 2022-06-14 10:19:33.071363
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -rf --cached .', 'fatal: not removing \'README.md\' recursively without -r')
    assert get_new_command(command) == 'git rm -rf --cached . -r'


# Generated at 2022-06-14 10:19:43.436169
# Unit test for function match
def test_match():
    script = ' git branch branch0 branch1'
    output = 'fatal: not removing \'branch0\' recursively without -r'
    command = Command(script, output)
    assert match(command)

    script = ' git branch branch0 branch1'
    output = 'fatal: not removing \'branch1\' recursively without -r'
    command = Command(script, output)
    assert match(command)

    script = ' git branch branch0 branch1'
    output = 'fatal: not removing \'branch2\' recursively without -r'
    command = Command(script, output)
    assert not match(command)

    script = ' git branch branch0 branch1'
    output = 'fatal: not removing \'branch\' recursively without -r'
    command = Command(script, output)

# Generated at 2022-06-14 10:19:57.569517
# Unit test for function match
def test_match():
    assert match(Command('git rm -f tests/test-file',
                         'fatal: not removing \'tests/test-file\' recursively without -r'))
    assert not match(Command('git rm -f tests/test-file',
                             'fatal: not removing \'tests/test-file\' recursively without -r',
                             'fatal: pathspec \'tests/test-file\' did not match any files'))
    assert not match(Command('git rm -f tests/test-file',
                             'Correcting: rm -f tests/test-file'))


# Generated at 2022-06-14 10:20:04.667048
# Unit test for function match
def test_match():
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r', ''))
    assert not match(Command('git rm file', '', '', ''))


# Generated at 2022-06-14 10:20:07.066259
# Unit test for function get_new_command
def test_get_new_command():
    cmd = 'git rm -r directory'
    assert get_new_command(Command(cmd, '')) == 'git rm directory'


# Generated at 2022-06-14 10:20:09.055033
# Unit test for function match
def test_match():
    # Test for match function
    assert match(Command('git rm non_empty_dir/','',''))


# Generated at 2022-06-14 10:20:13.284779
# Unit test for function get_new_command
def test_get_new_command():
   assert get_new_command(Script("git rm test/test.py", "fatal: not removing 'test/test.py' recursively without -r")) == "git rm -r test/test.py"

# Generated at 2022-06-14 10:20:20.714638
# Unit test for function match
def test_match():
    command = Command('(echo a && echo b) || (echo c && echo d)', '', '', 0)
    assert match(command)
    command = Command('(echo a && echo b) || (echo c && echo d)', '', '', 1)
    assert not match(command)
    command = Command('(echo a && echo b) || (echo c && echo d)', '', '', 2)
    assert not match(command)


# Generated at 2022-06-14 10:20:28.339735
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command('git rm file.txt', ''))
    assert not match(Command('git rm file.txt', 'fatal: not removing \'\' recursively without -r'))
    assert not match(Command('rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r'))


# Generated at 2022-06-14 10:20:35.916382
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf', 'fatal: not removing \'foo/bar\''
                         ' recursively without -r'))
    assert match(Command('git rm -rf', 'fatal: not removing \'foo/bar\''
                         ' recursively without -r\nSOMETHINGSOMETHING'))
    assert not match(Command('git rm -rf', r'''fatal: not removing 'foo/bar' recursively without -r
SOMETHINGSOMETHING'''))


# Generated at 2022-06-14 10:20:40.104311
# Unit test for function match
def test_match():
    assert match(Command('git rm file', ''))
    assert match(Command('git rm -m `cat issue-12345-description.txt`', ''))
    assert not match(Command('git config --global', ''))

# Generated at 2022-06-14 10:20:46.108904
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         """fatal: not removing 'file.txt' recursively without -r\n""",
                         '', 1))
    assert not match(Command('git remote add origin git@github.com:nvbn/thefuck',
                             """fatal: remote origin already exists.\n""",
                             '', 1))



# Generated at 2022-06-14 10:20:52.614882
# Unit test for function get_new_command
def test_get_new_command():
    # Test for both variants of the command
    c1 = Command('git rm README.md', 'fatal: not removing \'README.md\' recursively without -r')
    c2 = Command('git rm -f README.md', 'fatal: not removing \'README.md\' recursively without -r')
    assert get_new_command(c1) == 'git rm -r README.md'
    assert get_new_command(c2) == 'git rm -f -r README.md'
    assert not match(c1)
    assert not match(c2)

# Generated at 2022-06-14 10:20:59.984001
# Unit test for function match
def test_match():
    assert match(Command('git rm filename', output="'filename' recursively without -r"))
    assert match(Command('git rm filename', output="'filename' recursively without -r")) == False

# Generated at 2022-06-14 10:21:04.768182
# Unit test for function match
def test_match():
    assert match(Command('git rm -a foo', 'fatal: not removing \'bar\' recursively without -r'))
    assert not match(Command('git rm -r foo', 'fatal: not removing \'bar\' recursively without -r'))


# Generated at 2022-06-14 10:21:10.269524
# Unit test for function match
def test_match():
    assert match(Command(' git rm -p foo', 'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command(' git rm -p foo', 'fatal: pathspec \'"foo"\' did not match any file(s) known to git.'))
    assert not match(Command(' git rm -p foo', 'fatal: not removing \'foo\' recursively without -r'))

# Generated at 2022-06-14 10:21:15.792140
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm non-existent-file',
                      output='fatal: not removing \'non-existent-file\' recursively without -r',
                      conf={'git_support': 'true'})
    new_command = get_new_command(command)
    assert new_command == 'git rm -r non-existent-file'

# Generated at 2022-06-14 10:21:19.091979
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test', 'fatal: not removing \'test\' recursively without -r\n')
    assert get_new_command(command) == u'git -r rm test'

# Generated at 2022-06-14 10:21:21.912469
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test', '')) == 'git rm -r test'

# Generated at 2022-06-14 10:21:38.258257
# Unit test for function match
def test_match():
    assert match(Command('git rm a',
                         stderr=("fatal: not removing 'a' recursively without -r\n"
                                 "Did you mean 'rm -r'?"),
                         ))
    assert not match(Command('git rm a',
                             stderr="fatal: not removing 'a' recursively without -r\n"))


# Generated at 2022-06-14 10:21:40.274876
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm hello")) == "git rm -r hello"


# Generated at 2022-06-14 10:21:43.629037
# Unit test for function get_new_command
def test_get_new_command():
    assert( get_new_command(Command("git rm hello.txt", "fatal: not removing 'hello.txt' recursively without -r\n")) == "git rm -r hello.txt")

# Generated at 2022-06-14 10:21:46.238374
# Unit test for function match
def test_match():
    assert match(Command('rm foo', 'fatal: not removing \'foo\' recursively without -r\n'))


# Generated at 2022-06-14 10:21:50.044176
# Unit test for function get_new_command
def test_get_new_command():
    command_output = "fatal: not removing 'filename' recursively without -r"
    command = Command("git rm filename", command_output)
    new_command = get_new_command(command)
    assert new_command == "git rm -r filename"

# Generated at 2022-06-14 10:21:52.542058
# Unit test for function match
def test_match():
    assert(match(u'git rm -r src/') is True)
    assert(match(u'git rm file') is False)

# Generated at 2022-06-14 10:22:04.077068
# Unit test for function match
def test_match():
    command = Command('git rm DIR', stderr='fatal: not removing \'DIR\' recursively without -r\n',
                      return_code=128)
    assert match(command)
    command = Command('git rm DIR', stderr='fatal: not removing \'DIR\' recursively without -r\n',
                      return_code=128)
    assert not match(command)
    command = Command('git rm DIR', stderr='fatal: not removing \'DIR\' recursively without -r\n',
                      return_code=128)
    assert not match(command)

# Generated at 2022-06-14 10:22:07.335491
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('rm foo',
                                    'fatal: not removing \'foo\' recursively without -r',
                                    ''))
            == 'git rm -r foo')

# Generated at 2022-06-14 10:22:12.740166
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm_recursively import get_new_command
    assert get_new_command(
        Command(script='git rm {}'.format(tempfile.mkdtemp()),
                output='')).script == 'git rm -r {}'.format(tempfile.mkdtemp())


# Generated at 2022-06-14 10:22:13.601059
# Unit test for function match
def test_match():
    asser

# Generated at 2022-06-14 10:22:28.818403
# Unit test for function match
def test_match():
    command1 = Command(script='git rm filename',
                       output=command_output.FILE_NOT_REMOVED_RECURSIVELY)
    command2 = Command(script='git rm -r filename',
                       output=command_output.FILE_NOT_REMOVED_RECURSIVELY)
    assert match(command1)
    assert not match(command2)

# Generated at 2022-06-14 10:22:30.544336
# Unit test for function match
def test_match():
    assert match(Command('git rm test',
            ''))


# Generated at 2022-06-14 10:22:38.081249
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -r')) == 'git rm -r -r'
    assert get_new_command(Command(script='git rm -r --cached')) == 'git rm -r --cached -r'
    assert get_new_command(Command(script='git rm -r --cached --ignore-unmatch')) == 'git rm -r --cached --ignore-unmatch -r'

# Generated at 2022-06-14 10:22:41.820090
# Unit test for function match
def test_match():
	assert match(Command("git rm -r test", "fatal: not removing 'test' recursively without -r"))
	assert not match(Command("git rm -r test", ""))



# Generated at 2022-06-14 10:22:48.371036
# Unit test for function match
def test_match():
    assert match(Command('git rm path', '', ''))
    assert not match(Command('git rm -r path', '', ''))
    assert not match(Command('git rm path', '', 'fatal: not removing dir\n'))
    assert not match(Command('git rm -r path', '', 'fatal: not removing dir\n'))


# Generated at 2022-06-14 10:22:53.435999
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm file1',
                                   output='fatal: not removing \'file1\' recursively without -r',
                                   stderr='fatal: not removing \'file1\' recursively without -r')) == 'git rm -r file1'

# Generated at 2022-06-14 10:22:59.053464
# Unit test for function match
def test_match():
    assert match(Command('git rm',
                         'fatal: not removing /tmp/foo recursively without -r'))
    assert match(Command('git rm',
                         "fatal: not removing 'path/to/file/v2/foo.txt' recursively without -r"))
    assert not match(Command('git rm -r',
                             'fatal: not removing /tmp/foo recursively without -r'))
    assert not match(Command('git rm',
                             'fatal: not removing foo.txt'))


# Generated at 2022-06-14 10:23:05.295251
# Unit test for function get_new_command
def test_get_new_command():
    command_1 = Command('git rm -r ')
    command_2 = Command('git rm -r -r ')
    assert get_new_command(command_1) == 'git rm -r -r '
    assert get_new_command(command_2) == 'git rm -r -r -r '


# Generated at 2022-06-14 10:23:09.828475
# Unit test for function match
def test_match():
    assert match(Command('rm -r', 'fatal: not removing \'file\' recursively without -r', ''))
    assert not match(Command('rm', '', ''))
    assert not match(Command('rm -rf', '', ''))

# Generated at 2022-06-14 10:23:13.458220
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm -f file1 file2').split() == ['git', 'rm', '-f', '-r', 'file1', 'file2']
    assert get_new_command('git rm -f file1 file2').split() == ['git', 'rm', '-f', '-r', 'file1', 'file2']

# Generated at 2022-06-14 10:23:42.343678
# Unit test for function match
def test_match():
    command = Command('git rm -rf test/')
    assert match(command)
    # output = 'fatal: not removing \'.gitignore\' recursively without -r'
    command = Command('git rm -rf test/', output='fatal: not removing \'.gitignore\' recursively without -r')
    assert match(command)


# Generated at 2022-06-14 10:23:48.578847
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r newdir/newfile' == get_new_command('git rm newdir/newfile')
    assert 'git rm -r newfile' == get_new_command('git rm newfile')

# Generated at 2022-06-14 10:23:53.755410
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    command = Command('git rm -rf /tmp/git_test','-f')
    assert u'git rm -rf -r /tmp/git_test -f' == get_new_command(command)