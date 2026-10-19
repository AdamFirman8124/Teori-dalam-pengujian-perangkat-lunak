

# Generated at 2022-06-14 10:14:07.273509
# Unit test for function match
def test_match():
    # Test when script contains ' rm ' and command.output contains 'fatal: not removing ' and ' recursively without -r'
    command = Command('git rm -f package', output='fatal: not removing \'package\' recursively without -r\n')
    assert match(command)

    # Test when script doesn't contain ' rm '
    command = Command('git rm', output='fatal: not removing \'package\' recursively without -r\n')
    assert not match(command)

    # Test when command.output doesn't contains 'fatal: not removing '
    command = Command('git rm -f package', output='fatal: not removing package recursively without -r\n')
    assert not match(command)

    # Test when command.output doesn't contains ' recursively without -r'

# Generated at 2022-06-14 10:14:10.417028
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm dave',
                                 '/tmp/git_output', 1)) == 'git rm -r dave'


# Generated at 2022-06-14 10:14:17.848658
# Unit test for function match
def test_match():
    assert match(Command('git rm a -r',
                         'fatal: not removing \'a\' recursively without -r'))
    assert not match(Command('git rm a -r', ''))
    assert not match(Command('git rm -r', 'fatal: not removing \'a\' recursively without -r'))
    assert match(Command('git rm a -r', 'fatal: not removing \'a/b\' recursively without -r'))



# Generated at 2022-06-14 10:14:27.369667
# Unit test for function match
def test_match():
    match_message = ("fatal: not removing 'tests/README.md' recursively "
                     "without -r\n")
    command = Command("git rm tests/README.md", match_message)
    assert match(command)
    command = Command("git rm -r tests/README.md", match_message)
    assert not match(command)
    command = Command("rm tests/README.md", match_message)
    assert not match(command)
    command = Command("git branch", match_message)
    assert not match(command)


# Generated at 2022-06-14 10:14:30.385784
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm -f", "fatal: not removing 'file' recursively without -r")
    assert "git rm -r -f" in get_new_command(command)

# Generated at 2022-06-14 10:14:37.762985
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command(script='git rm abc def'))
            == u'git rm -r abc def')
    assert (get_new_command(Command(script='git rm -r abc def'))
            == u'git rm -r -r abc def')
    assert (get_new_command(Command(script='rm abc def'))
            == u'rm abc def')



# Generated at 2022-06-14 10:14:45.672899
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r',
                         '', 1))
    assert not match(Command('git rm file.txt', '', '', 1))
    assert not match(Command('rm file.txt',
                             'fatal: not removing \'file.txt\' recursively without -r',
                             '', 1))


# Generated at 2022-06-14 10:15:02.770919
# Unit test for function match
def test_match():
    # NOTE: Arguments are an instance of Command
    # NOTE: Arguments must be a command that will match
        
    command = Command("git rm -r dir/file.txt")
    print(command.output)
    print("-" * 40)
    print("-" * 40)
    obj = [command.script, command.output]
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print(obj)
    print("-" * 40)
    print("-" * 40)


# Generated at 2022-06-14 10:15:06.217863
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm -r file", "fatal: not removing 'file' recursively without -r")
    assert get_new_command(command) == "git rm -r -r file"

# Generated at 2022-06-14 10:15:10.556631
# Unit test for function match
def test_match():
    assert match(Command('rm -r a', '', 'fatal: not removing'))
    assert not match(Command('rm a', '', 'fatal: not removing'))
    assert not match(Command('rm a', '', ''))


# Generated at 2022-06-14 10:15:14.651826
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test.txt', '')) == 'git rm -r test.txt'

# Generated at 2022-06-14 10:15:22.472709
# Unit test for function get_new_command
def test_get_new_command():
    command_parts1 = ['git', 'rm', '-f', 'file.txt']
    assert get_new_command(Command(u'', 'fatal: not removing \'file.txt\' recursively without -r\
    Did you mean \'rm -r\'?')) == 'git rm -f -r file.txt'

    command_parts2 = ['rm', '-f', 'file.txt']
    assert get_new_command(Command(u'', 'rm: cannot remove \'file.txt\': Is a directory\
    Did you mean -r?')) == 'rm -f -r file.txt'

# Generated at 2022-06-14 10:15:26.154892
# Unit test for function match
def test_match():
    assert match(Command('git rm -r file', '', 'fatal: not removing \'file/x\' recursively without -r'))


# Generated at 2022-06-14 10:15:38.245248
# Unit test for function match
def test_match():
    # test match when rm command is used
    assert match(Command("git rm test.txt", "fatal: not removing 'test.txt' recursively without -r"))
    # test match when -r is not used
    assert match(Command("git rm test.txt", "fatal: not removing 'test.txt' recursively without -r"))
    # test match when -r is used
    assert not match(Command("git rm -r test.txt", "fatal: not removing 'test.txt' recursively without -r"))
    # test match when 'fatal: not removing' is not present in the output
    assert not match(Command("git rm test.txt", ""))
    # test match when script is not a git command

# Generated at 2022-06-14 10:15:43.256802
# Unit test for function get_new_command
def test_get_new_command():
    parts = ['git', 'rm', '-f', 'dir1', 'dir2']
    actual = get_new_command(Command(' '.join(parts), '', ''))
    expected = ' '.join(['git', 'rm', '-rf', 'dir1', 'dir2'])
    assert actual == expected

# Generated at 2022-06-14 10:15:53.902893
# Unit test for function match
def test_match():
    assert match(Command('git branch git clone https://github.com/nvbn/thefuck', 
                         "fatal: Not a git repository (or any of the parent directories): .git\n"))
    assert match(Command('git rm thefuck/utils.py', "fatal: not removing 'thefuck/utils.py' recursively without -r"))
    assert not match(Command('git branch', "fatal: Not a git repository (or any of the parent directories): .git\n"))
    assert not match(Command('rm thefuck/utils.py', "fatal: not removing 'thefuck/utils.py' recursively without -r"))


# Generated at 2022-06-14 10:16:06.587736
# Unit test for function match
def test_match():
    command = Command(script = 'git rm main.py',
                      output = "fatal: not removing 'main.py' recursively without -r")
    assert match(command)

    command = Command(script = 'git rm --cached main.py',
                      output = "fatal: not removing 'main.py' recursively without -r")
    assert match(command)

    command = Command(script = 'git rm -f main.py',
                      output = "fatal: not removing 'main.py' recursively without -r")
    assert match(command)

    command = Command(script = 'git rm main.py',
                      output = "fatal: not removing 'main.py' recursively without -r")
    assert match(command)


# Generated at 2022-06-14 10:16:14.481863
# Unit test for function get_new_command
def test_get_new_command():
    """ Function get_new_command returns correct string
    """
    match_method = MagicMock(return_value=True)
    command = MagicMock(script="""git rm -rf """,
                        output="fatal: not removing 'file_name' recursively without -r",
                        script_parts=['git', 'rm', '-rf'],
                        stderr=None,)
    command.script = command.script
    command.output = command.output
    command.script_parts = command.script_parts
    command.stderr = command.stderr
    command.match = match_method
    result = get_new_command(command)
    assert(result == "git rm -rf -r")

# Generated at 2022-06-14 10:16:17.155277
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm testtest/test')
    assert get_new_command(command) == 'git rm -r testtest/test'

# Generated at 2022-06-14 10:16:21.758233
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm abc'

# Generated at 2022-06-14 10:16:27.009420
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command("git rm -f README.md") ==
            "git rm -rf -f README.md")

# Generated at 2022-06-14 10:16:31.390719
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm_folder import get_new_command
    from thefuck.types import Command

    assert get_new_command(Command('git rm aFolder', 'error: pathspec')) == u'git rm -r aFolder'

# Generated at 2022-06-14 10:16:34.601456
# Unit test for function match
def test_match():
    assert match(Command('rm test', 'fatal: not removing \'test\' recursively without -r', ''))
    assert not match(Command('rm test', '', ''))
    assert not match(Command('ls', '', ''))


# Generated at 2022-06-14 10:16:37.212900
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r src/rm')
    get_new_command(command)
    assert command.script == command.script
    assert command.output == command.output

# Generated at 2022-06-14 10:16:40.632654
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm_non_empty_dir import get_new_command
    assert get_new_command(Command('git rm -f non_empty_dir')) == u'git rm -r -f non_empty_dir'

# Generated at 2022-06-14 10:16:43.147794
# Unit test for function match
def test_match():
    assert match(Command('git rm -r -f test.txt',
                         'fatal: not removing \'test.txt\' recursively without -r'))
    assert not match(Command('rm file', ''))


# Generated at 2022-06-14 10:16:48.421622
# Unit test for function get_new_command
def test_get_new_command():
    output = 'fatal: not removing \'abd\' recursively without -r'
    test_command = Command('git rm abd', output)
    assert get_new_command(test_command) == 'git rm -r abd'


# Generated at 2022-06-14 10:16:57.699129
# Unit test for function match
def test_match():
    assert match(Command('vim file1.txt file2.txt', 'fatal: not removing \'file1.txt\' recursively without -r'))
    assert not match(Command('vim file1.txt file2.txt', ''))
    assert not match(Command('ls file1.txt file2.txt', 'fatal: not removing \'file1.txt\' recursively without -r'))
    assert not match(Command('cat file1.txt file2.txt', 'fatal: not removing \'file1.txt\' recursively without -r'))


# Generated at 2022-06-14 10:16:58.835458
# Unit test for function match
def test_match():
    match = MagicMock(return_value = False)
    command = MagicMock(script = "git rm foo", output = "fatal: not removing 'foo' recursively without -r")
    assert match(command)

# Generated at 2022-06-14 10:17:00.720972
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r branch' in get_new_command('git rm branch')
    assert 'git rm -r branch' in get_new_command('git rm')

# Generated at 2022-06-14 10:17:08.640187
# Unit test for function get_new_command
def test_get_new_command():
    script = "git rm bar/baz"
    output = "fatal: not removing 'bar/baz' recursively without -r"
    command = Command(script, output)
    assert get_new_command(command) == "git rm -r bar/baz"



# Generated at 2022-06-14 10:17:21.473310
# Unit test for function match
def test_match():
    # Test 1
    command = Command('git rm -r file-name', 'rm: file-name: is a directory\n')
    assert match(command) is True
    # Test 2
    command = Command('git rm file-name', 'rm: file-name: No such file or \
directory\n')
    assert match(command) is False
    # Test 3
    command = Command('git rm -r file-name', 'rm: file-name: is a directory\n')
    assert get_new_command(command) == 'git rm -r -r file-name'
    # Test 4
    command = Command('git rm file-name', 'rm: file-name: is a directory\n')
    assert get_new_command(command) == 'git rm -r file-name'

# Generated at 2022-06-14 10:17:24.709683
# Unit test for function match
def test_match():
    assert match(Command('git rm text.py',
                         stderr='fatal: not removing \'text.py\' recursively without -r\n'))


# Generated at 2022-06-14 10:17:27.877579
# Unit test for function get_new_command
def test_get_new_command():
    output = u'fatal: not removing \'dir\' recursively without -r\n'
    command = Command('git rm dir', output)
    assert u'git rm -r dir' == get_new_command(command)

# Generated at 2022-06-14 10:17:31.831710
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git rm -f test',
                                    'fatal: not removing \'', '\' recursively without -r'))
            == 'git rm -r -f test')


# Generated at 2022-06-14 10:17:36.111861
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r')
    assert get_new_command(command).script == 'git rm -r -r'

# Generated at 2022-06-14 10:17:39.778430
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm path/to/file', 'fatal: not removing \'path/to/file\' recursively without -r')
    assert get_new_command(command) == 'git rm -r path/to/file'

# Generated at 2022-06-14 10:17:47.827838
# Unit test for function match
def test_match():
    assert match(Command('git rm make-readme.sh',
                   'fatal: not removing \'make-readme.sh\' recursively without -r'))
    assert not match(Command('test', 'file not found'))


# Generated at 2022-06-14 10:17:50.817578
# Unit test for function match
def test_match():
    command = Command("git rm toto", "fatal: not removing 'toto' recursively without -r")
    assert (match(command) != None)



# Generated at 2022-06-14 10:17:54.020257
# Unit test for function match
def test_match():
    command = Command('git rm -r', None)
    assert match(command)
    command = Command('git rm -r', 'fatal: not removing something recursively without -r')
    assert match(command)

# Generated at 2022-06-14 10:18:00.572948
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm duck.py', 'fatal: not removing \'duck.py\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -r duck.py'


# Generated at 2022-06-14 10:18:04.604729
# Unit test for function match
def test_match():
    command = Command(script='git rm test_file.txt', 
        stdout='fatal: not removing \'test_file.txt\' recursively without -r',
        stderr='')
    assert match(command)


# Generated at 2022-06-14 10:18:11.617888
# Unit test for function match
def test_match():
    command1 = Command('git rm file.py', 'fatal: not removing \'file.py\' recursively without -r\n')
    command2 = Command('sudo apt-get rm file.py', 'fatal: not removing \'file.py\' recursively without -r\n')
    command3 = Command('git rm -r file.py', 'fatal: not removing \'file.py\' recursively without -r\n')
    assert match(command1)
    assert not match(command2)
    assert not match(command3)


# Generated at 2022-06-14 10:18:22.429761
# Unit test for function match
def test_match():
    assert match(Command('git rm my_file',
                         'fatal: not removing '
                         '\'/Users/Guillaume/work/thefuck/thefuck/tests/examples/git/my_file\' '
                         'recursively without -r'))
    assert not match(Command('git rm my_file',
                             'fatal: not removing '
                             '\'/Users/Guillaume/work/thefuck/thefuck/tests/examples/git/my_file'))


# Generated at 2022-06-14 10:18:25.815905
# Unit test for function match
def test_match():
    assert match(Command('git rm README.md', ''))
    assert not match(Command('git rm README.md', 'fatal: not removing '))



# Generated at 2022-06-14 10:18:31.686378
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf'))
    assert not match(Command('git rm'))
    assert match(Command('git rm', stderr='fatal: not removing \'/home/user/.git/refs/remotes/origin/master\' recursively without -r'))


# Generated at 2022-06-14 10:18:36.638599
# Unit test for function get_new_command
def test_get_new_command():
	expected = u'git -r rm foo'
	assert get_new_command(Command(script='git rm foo', output='fatal: not removing \'foo\' recursively without -r')) == expected
	assert get_new_command(Command(script='git branch rm foo', output='fatal: not removing \'foo\' recursively without -r')) == None



# Generated at 2022-06-14 10:18:40.020328
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
            'fatal: not removing \'foo\' recursively without -r\n',
            ''))


# Generated at 2022-06-14 10:18:44.402868
# Unit test for function match
def test_match():
    assert_equal(
        match(Command(script='git rm hello.py',
                      stdout='fatal: not removing hello.py recursively without -r',
                      stderr='')),
        True)



# Generated at 2022-06-14 10:18:47.820015
# Unit test for function match
def test_match():
    assert match(Command('git rm foo.txt',
                         'fatal: not removing \'foo.txt\' recursively without -r'))
    assert not match(Command('git rm foo.txt', ''))


# Generated at 2022-06-14 10:19:00.357230
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', output='fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo', output="foo's not a git repo"))
    assert not match(Command('git rm foo', output='fatal: not removing \'foo\' recursively without'))
    assert not match(Command('ls foo', output='fatal: not removing \'foo\' recursively without -r'))


# Generated at 2022-06-14 10:19:04.172395
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('echo 1',
                           'fatal: not removing \'$PWD/myfile\' recursively without -r')) == 'git rm -r myfile'

# Generated at 2022-06-14 10:19:09.660678
# Unit test for function match
def test_match():
    assert match(Command('git rm dir', 'fatal: not removing \'dir\' recursively without -r'))
    assert not match(Command('git rm dir', 'fatal: not removing \'dir\' recursively with -r'))
    assert not match(Command('git rm dir', 'fatal: not removing \'dir\' without -r'))

# Generated at 2022-06-14 10:19:21.171476
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm ', output="fatal: not removing 'files/' recursively without -r")
    assert get_new_command(command) == 'git rm -r'
    command = Command(script='git rm -i', output="fatal: not removing 'files/' recursively without -r")
    assert get_new_command(command) == 'git rm -i -r'
    command = Command(script='git rm -d', output="fatal: not removing 'files/' recursively without -r")
    assert get_new_command(command) == 'git rm -d -r'
    command = Command(script='git rm f', output="fatal: not removing 'files/' recursively without -r")
    assert get_new_command(command) == 'git rm f -r'
   

# Generated at 2022-06-14 10:19:26.535711
# Unit test for function match
def test_match():
    # Example of a script which failed
    # git rm algo
    output1 = 'fatal: not removing \'algo\' recursively without -r'
    # Example of a script which not failed
    # git rm algo
    output2 = 'fatal: pathspec \'algo\' did not match any files'

    assert match(Command('git rm algo', output1))
    assert not match(Command('git rm algo', output2))


# Generated at 2022-06-14 10:19:32.152232
# Unit test for function get_new_command
def test_get_new_command():
    assert u'touch foo' == get_new_command(Command('rm foo'))
    assert u'touch foo bar' == get_new_command(Command('rm foo bar'))
    assert u'touch -f foo' == get_new_command(Command('rm -f foo'))
    assert u'touch -f foo bar' == get_new_command(Command('rm -f foo bar'))

# Generated at 2022-06-14 10:19:37.282087
# Unit test for function match
def test_match():
    from tempfile import mkdtemp
    from os import chdir, path

    direc = mkdtemp()
    chdir(direc)

# Generated at 2022-06-14 10:19:40.998117
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foldername', 'git', 1)
    assert u' '.join(get_new_command(command)) == command.script + ' -r'

# Generated at 2022-06-14 10:19:43.428480
# Unit test for function match
def test_match():
    assert match(Command('git rm file'))
    assert match(Command('git rm -r file')) is False

# Generated at 2022-06-14 10:19:47.090886
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm path/to/folder') == 'git rm -r path/to/folder'



# Generated at 2022-06-14 10:20:03.566931
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file', '')
    new_command = get_new_command(command)
    assert new_command == "git rm -r file"

# Generated at 2022-06-14 10:20:08.148751
# Unit test for function get_new_command
def test_get_new_command():
    command_script = u'git rm test'
    command_output = u"fatal: not removing 'test' recursively without -r"
    out_command = u'git rm -r test'
    assert out_command == get_new_command(Command(script = command_script, output = command_output))

# Generated at 2022-06-14 10:20:10.352203
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', '', '', 1, None))
    assert match(Command('git rm foo', '', '', 1, None)) is False


# Generated at 2022-06-14 10:20:15.084547
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively without -r', ''))
    assert not match(Command('git rm file.txt', '', ''))


# Generated at 2022-06-14 10:20:18.604483
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r foo/', 'fatal: not removing '
                                   "'foo/' recursively without -r")) == 'git rm -r -r foo/'

# Generated at 2022-06-14 10:20:23.637107
# Unit test for function match
def test_match():
    assert match(Command('git rm a b c',
                         'fatal: not removing \'a\' recursively without -r \n'
                         'fatal: not removing \'b\' recursively without -r \n'
                         'fatal: not removing \'c\' recursively without -r \n',
                         ''))



# Generated at 2022-06-14 10:20:28.444945
# Unit test for function get_new_command
def test_get_new_command():
    # no error in command
    assert get_new_command(Command('git rm README.md')) is None
    # command generating error
    assert get_new_command(Command('git rm README.md', 'fatal: not removing \'README.md\' recursively without -r'))


# Generated at 2022-06-14 10:20:39.600839
# Unit test for function match
def test_match():
    # Matches
    assert_true(
        match(Command('git rm filename',
                      'fatal: not removing \'path/filename\' recursively \
without -r', '')))
    # Does not match
    assert_false(
        match(Command('git add filename',
                      'fatal: not removing \'path/filename\' recursively \
without -r', '')))
    # Matches without spacing
    assert_true(
        match(Command('git rm filename',
                      'fatal: not removing \'path/filename\'recursively \
without -r', '')))
    assert_true(
        match(Command('git rm filename',
                      'fatal: not removing \'path/filename\'recursively \
without -r', '')))


# Generated at 2022-06-14 10:20:42.819760
# Unit test for function match
def test_match():
    assert match(Command('git rm test/test_match.py', 'fatal: not removing \'test/test_match.py\' recursively without -r') )


# Generated at 2022-06-14 10:20:47.892982
# Unit test for function match
def test_match():
	test_case1 = "git rm /tmp/test -f"
	test_output1 = "fatal: not removing '/tmp/test' recursively without -r"
	test1 = Command(test_case1, test_output1)
	assert(match(test1))


# Generated at 2022-06-14 10:21:16.415250
# Unit test for function match
def test_match():
    assert match(Command('git rm what_a_pity', 'fatal: not removing \'what_a_pity\' recursively without -r'))
    assert match(Command('git rm -f what_a_pity', 'fatal: not removing \'what_a_pity\' recursively without -r'))
    assert match(Command('git rm --force what_a_pity', 'fatal: not removing \'what_a_pity\' recursively without -r'))
    assert match(Command('git rm what_a_pity', 'fatal: not removing \'what_a_pity\' recursively without --cached'))
    assert not match(Command('git rm what_a_pity', 'fatal: not removing \'what_a_pity\''))



# Generated at 2022-06-14 10:21:23.156805
# Unit test for function get_new_command
def test_get_new_command():
   command = Command('git rm test', 'fatal: not removing \'test/\' recursively without -r')
   assert get_new_command(command) == 'git rm -r test'



# Generated at 2022-06-14 10:21:26.706871
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm dir')
    command.output = "fatal: not removing 'dir' recursively without -r"
    assert get_new_command(command) == 'git rm -r dir'

# Generated at 2022-06-14 10:21:31.192731
# Unit test for function match
def test_match():
    assert match(Command('git rm blabla', 'fatal: not removing \'blabla\' recursively without -r'))
    assert not match(Command('git rm blabla', 'fatal: not removing \'blabla\''))


# Generated at 2022-06-14 10:21:33.065256
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm a')) == 'git rm -r a'

# Generated at 2022-06-14 10:21:35.075901
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git rm file', '', '')) ==
            'git rm -r file')

# Generated at 2022-06-14 10:21:39.826501
# Unit test for function get_new_command
def test_get_new_command():

    command1 = Command('rm README')
    command2 = Command('git rm README')

    assert get_new_command(command1) == 'rm -r README'
    assert get_new_command(command2) == 'git rm -r README'

# Generated at 2022-06-14 10:21:45.480983
# Unit test for function match
def test_match():
    assert match(Command('git rm foo.txt',
        "fatal: not removing 'foo.txt' recursively without -r"))
    assert not match(Command('git rm foo.txt', ''))
    assert not match(Command('foo rm foo.txt',
        "fatal: not removing 'foo.txt' recursively without -r"))


# Generated at 2022-06-14 10:21:50.092965
# Unit test for function get_new_command
def test_get_new_command():
    assert (utils.get_new_command(u"git rm -rf tests/git_support.py",
                                  "fatal: not removing 'tests/git_support.py' recursively without -r",
                                  match, get_new_command)
            == u"git rm -r -rf tests/git_support.py")

# Generated at 2022-06-14 10:22:04.869018
# Unit test for function match
def test_match():
    assert match(Command('git rm *file*',
                    'fatal: not removing `file_dir1/file_dir2/file_dir3/downloaded.pdf'
                    '\' recursively without -r', ''))
    assert not match(Command('git rm *file*',
                       'fatal: not removing `file_dir1/file_dir2/file_dir3/downloaded.pdf'
                       '\' recursively without -r', ''), 'rm')
    assert match(Command('git rm -r *file*',
                    'fatal: not removing `file_dir1/file_dir2/file_dir3/downloaded.pdf'
                    '\' recursively with -r', ''))

# Generated at 2022-06-14 10:22:27.566014
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file.txt') == 'git rm -r file.txt'
    assert get_new_command('git rm -r file.txt') == 'git rm file.txt'

# Generated at 2022-06-14 10:22:32.065190
# Unit test for function match
def test_match():
    assert match(Command('git rm --cached foo/bar'))
    assert match(Command('git rm foo/bar'))
    assert not match(Command('rm foo/bar'))
    assert not match(Command('git rm foo/bar', 'fatal: foo'))
    assert not match(Command('git rm foo/bar', 'fatal: not removing foob'))


# Generated at 2022-06-14 10:22:40.098472
# Unit test for function match
def test_match():
    assert match(Command(' rm aaa.txt',
                         'fatal: not removing \'aaa.txt\' recursively without -r\n',
                         '', 1)) == True
    assert match(Command(' rm aaa.txt',
                         'fatal: not removing \'aaa.txt\' recursively without -r\n',
                         '', 1)) == True
    assert match(Command(' rm aaa.txt',
                         'fatal: not removing \'aaa.txt\' recursively without -r\n',
                         '', 1)) == True


# Generated at 2022-06-14 10:22:48.022962
# Unit test for function get_new_command
def test_get_new_command():
    # Case 1: Test when file is a directory
    command_test = Command('rm test_dir/', '')
    assert get_new_command(command_test) == 'git rm -r test_dir/'
    # Case 2: Test when file is not a directory
    command_test2 = Command('git rm test_dir/test_file.txt', '')
    assert get_new_command(command_test2) == 'git rm test_dir/test_file.txt'

# Generated at 2022-06-14 10:22:52.685591
# Unit test for function match
def test_match():
    assert match(Command(' rm', '', 'fatal: not removing \'src/test.py\' recursively without -r'))
    assert not match(Command(' rm', '', 'fatal: not removing \'src/test.py\''))



# Generated at 2022-06-14 10:23:00.576076
# Unit test for function match
def test_match():
    assert match(Command(script='git rm fileA fileB',
                                 stderr='fatal: not removing \'fileA\' recursively without -r',
                                 output='fatal: not removing \'fileA\' recursively without -r'))
    assert not match(Command(script='git rm fileA fileB',
                                 stderr='fatal: not removing \'fileA\' recursively without -r',
                                 output='fatal: not removing \'fileA\' recursively without -r'))
    assert not match(Command(script='git rm fileA fileB',
                                 stderr='fatal: not removing \'fileA\' recursively without -r',
                                 output='fatal: not removing \'fileA\' recursively without -r'))


# Generated at 2022-06-14 10:23:02.190179
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git branch -d branch1 branch2')
    assert get_new_command(command) == 'git branch -d -r branch1 branch2'

# Generated at 2022-06-14 10:23:04.338538
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('git rm --cached fakefile1', ''))
    assert new_command == 'git rm -r --cached fakefile1'

# Generated at 2022-06-14 10:23:08.976881
# Unit test for function get_new_command
def test_get_new_command():
    # Original command: git rm testdir
    # Expected output: git rm -r testdir
    command = Command('git rm testdir', 'fatal: not removing ' \
                      '\'testdir\' recursively without -r\nDid you ' \
                      'mean \'rm -r\'?')
    assert get_new_command(command) == command.script.replace('rm', 'rm -r')

# Generated at 2022-06-14 10:23:13.597954
# Unit test for function get_new_command
def test_get_new_command():
    command = u"git rm dir/"
    command_parts = command.split()

    function_return = get_new_command(Command(command, u"fatal: not removing 'dir/' recursively without -r", ''))
    assert function_return.split() == command_parts[:3] + ['-r'] + command_parts[3:]

# Generated at 2022-06-14 10:23:43.671870
# Unit test for function match
def test_match():
    assert(match(Command('git rm hello.py'))) != True
    assert(match(Command('git rm hello.py', 'fatal: not removing \'hello.py\' recursively without -r\n'))) != False
    assert(match(Command('git rm hello', 'fatal: not removing \'hello.py\' recursively without -r\n'))) != True


# Generated at 2022-06-14 10:23:45.759331
# Unit test for function match
def test_match():
    assert match(Command('git rm -fR test', 'fatal: not removing \'test\' recursively without -r'))

# Generated at 2022-06-14 10:23:47.619223
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git rm tmp') == 'git rm -r tmp'

# Generated at 2022-06-14 10:23:49.428985
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r src/')) == 'git rm -r -r src/'

# Generated at 2022-06-14 10:23:59.249313
# Unit test for function match
def test_match():
    assert match(Command('git rm -r foldername/',
        'fatal: not removing \'foldername/\' recursively without -r'))
    assert not match(Command('git rm foldername/',
        'fatal: not removing \'foldername/\' recursively without -r'))
    assert not match(Command('git rm',
        'fatal: not removing \'foldername/\' recursively without -r'))
    assert not match(Command('git rm -r',
        'fatal: not removing \'foldername/\' recursively without -r'))
