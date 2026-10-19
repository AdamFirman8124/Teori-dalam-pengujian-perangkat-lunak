

# Generated at 2022-06-14 10:13:59.253504
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file') == 'git rm -r file'

# Generated at 2022-06-14 10:14:07.010493
# Unit test for function match
def test_match():
    command = Command(script="git rm file", output="fatal: not removing 'file' recursively without -r")
    assert not git_support(match)(command)

    command = Command(script="git rm file", output="fatal: not removing 'file' recursively without -r")
    assert match(command)

    command = Command(script="git rm", output="fatal: pathspec '' did not match any files")
    assert not match(command)



# Generated at 2022-06-14 10:14:10.583719
# Unit test for function match
def test_match():
    assert match(Command('git reb rm not add', stderr='fatal: not removing '+
                         ''+"'' recursively without -r"))
    assert not match(Command('git rm'))


# Generated at 2022-06-14 10:14:15.085945
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert(match(Command('git rm file', "fatal: not removing 'file' recursively without -r\n", "")))
    assert(not match(Command('git rm file', "", "")))



# Generated at 2022-06-14 10:14:20.825343
# Unit test for function get_new_command
def test_get_new_command():
    script = u'git rm -rf src/main.cpp'
    output = "fatal: not removing 'src/main.cpp' recursively without -r"
    command = Command(script, output)
    assert get_new_command(command) == u'git rm -rf -r src/main.cpp'

# Generated at 2022-06-14 10:14:24.675196
# Unit test for function get_new_command
def test_get_new_command():
    assert_that(get_new_command("git rm file.txt"), equal_to("git rm -r file.txt"))
    assert_that(get_new_command("git rm some/directory"), equal_to("git rm -r some/directory"))
    assert_that(get_new_command("git rm ./some/directory"), equal_to("git rm -r ./some/directory"))

# Generated at 2022-06-14 10:14:28.777067
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file', 'git rm file\nfatal: not removing \'file\' recursively without -r')) == 'git rm -r file'


# Generated at 2022-06-14 10:14:37.802692
# Unit test for function match
def test_match():
    """Check if match matches the correct error message from git rm command"""
    assert match(Command('git rm file/file.txt'))
    assert not match(Command('git rm -r file.txt'))
    assert not match(Command('git rm -R file.txt'))
    assert not match(Command('git rm --recursive file.txt'))
    assert not match(Command('git rm file1.txt file2.txt'))
    assert not match(Command('git remote'))
    assert not match(Command('git rm'))
    assert not match(Command('git'))
    assert not match(Command('git xyz'))


# Generated at 2022-06-14 10:14:41.889482
# Unit test for function match
def test_match():
    command = Command('git rm -r -f README.md', 'fatal: not removing \'README.md\' recursively without -r')
    assert match(command)



# Generated at 2022-06-14 10:14:53.950260
# Unit test for function match
def test_match():
    # Not a git command
    assert not match(Command('ls -l'))
    assert not match(Command('git foo'))

    # Not the right error
    assert not match(Command('git rm foo',
                             'fatal: pathspec \'foo\' did not match any files'))

    # Not the right error
    assert not match(Command('git rm foo',
                             'fatal: not removing \'.gitignore\' recursively without -r'))

    # Wrong command
    assert not match(Command('git bar foo'))

    # Wrong error
    assert not match(Command('git rm foo',
                             'fatal: pathspec \'foo\' did not match any files'))

    # The right error

# Generated at 2022-06-14 10:15:03.565717
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm src", "", "not removing 'src' recursively without -r")) == \
            u"git rm -r src"

    assert get_new_command(Command("git add src", "", "not removing 'src' recursively without -r")) == \
            u"git add src"

# Generated at 2022-06-14 10:15:07.835103
# Unit test for function match
def test_match():
	msg = u'fatal: not removing \'.gitignore\' recursively without -r\n'
	assert (match(Command('rm .gitignore', msg))
		and match(Command('git rm .gitignore', msg)))
	assert not match(Command('rm .gitignore', u''))



# Generated at 2022-06-14 10:15:12.469967
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf foo'))
    assert match(Command('git rm -rf foo',
                         'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo'))



# Generated at 2022-06-14 10:15:22.266089
# Unit test for function match
def test_match():
	# We can't just match the output because of different paths --
	# Either we need to mock the command, or ...
	# command.script are the parts of the command we've typed
	# command.script_parts are the parts of the command we've typed, but
	# split into a list on spaces
	command = Command('git rm test/file2', 'fatal: not removing \'test/file2\' recursively without -r')
	assert match(command)

	command2 = Command('git rm file2', 'fatal: not removing \'file2\' recursively without -r')
	assert match(command2)


# Generated at 2022-06-14 10:15:26.393189
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm '../test.csv'", "", "")) == "git rm -r '../test.csv'"


# Generated at 2022-06-14 10:15:36.406664
# Unit test for function match
def test_match():
    assert match(Command('git rm file'))
    assert match(Command('git rm --cached file', 'fatal: not removing '
                         '\'file\' recursively without -r\nDid you '
                         'mean this?\nyes\n'))
    assert not match(Command('git rm file',
                             'fatal: not removing \'file\' recursively '
                             'without -r\nDid you mean this?\nyes\n'))
    assert not match(Command('rm file', 'fatal: not removing \'file\' '
                     'recursively without -r\nDid you mean this?\nyes\n'))



# Generated at 2022-06-14 10:15:40.049370
# Unit test for function match
def test_match():
    assert match(Command('git rm qwertyui', ''))
    assert not match(Command('git rm qwertyui', 'qwewqeq'))
    assert not match(Command('git qwertyui', 'rm'))


# Generated at 2022-06-14 10:15:52.935952
# Unit test for function match
def test_match():
    # Basic test
    assert match(Command("git rm -z *.txt", "fatal: not removing '*.txt' recursively without -r"))
    assert match(Command("git rm -z *.txt", "fatal: not removing '*.txt' recursively without -r\n"))

    # Wrong command
    assert not match(Command("git commit -m 'message' *.txt", "fatal: not removing '*.txt' recursively without -r"))
    # Wrong message
    assert not match(Command("git rm -z *.txt", "fatal: not adding '*.txt' recursively without -r\n"))

# Generated at 2022-06-14 10:16:00.488717
# Unit test for function match
def test_match():
    assert(match('git rm file.txt'))
    assert(match(' git rm file.txt'))
    assert(match("git rm file.txt && test --flag"))
    assert(match(" git rm file.txt && test --flag"))
    assert(match("git rm file.txt && test --flag"))
    assert(not match("git rm file.txt && test --flag") == 'test')
    assert(not match("git branch"))

# Generated at 2022-06-14 10:16:06.693900
# Unit test for function match
def test_match():
    assert match(Command(script='git rm',
                        stderr=('fatal: not removing \'unit_test.py\' recursively without -r')))
    assert not match(Command(script='git rm',
                        stderr=('')))
    assert not match(Command(script='git rm',
                        stderr=('fatal: not removing \'unit_test.py\'')))



# Generated at 2022-06-14 10:16:12.888602
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file1 file2') == 'git rm -r file1 file2'
    assert get_new_command('git rm file') == 'git rm -r file'

# Generated at 2022-06-14 10:16:16.800098
# Unit test for function match
def test_match():
    assert match(Command('rm file', '', '', ''))
    assert match(Command('rm file', '', '', ''))
    assert not match(Command('git rm file', '', '', ''))


# Generated at 2022-06-14 10:16:29.069115
# Unit test for function match
def test_match():
    command_1 = "git rm test.txt"
    command_2 = "git rm -r test"
    command_3 = "git rm   test"
    command_4 = "git rm test.txt test2.txt"
    command_5 = "git rm"

    assert not match(Command(command_1, "fatal: not removing 'test/test.txt' recursively without -r"))
    assert match(Command(command_2, "fatal: not removing 'test/test.txt' recursively without -r"))
    assert match(Command(command_3, "fatal: not removing 'test/test.txt' recursively without -r"))
    assert match(Command(command_4, "fatal: not removing 'test/test.txt' recursively without -r"))

# Generated at 2022-06-14 10:16:33.653659
# Unit test for function match
def test_match():
    from thefuck.types import Command, Script

# Generated at 2022-06-14 10:16:38.019515
# Unit test for function match
def test_match():
    example_command1 = Command('git rm "some file"', 'fatal: not removing \'some file\' recursively without -r')
    assert match(example_command1)
    example_command2 = Command('git --version', 'git version 2.15.1')
    assert not match(example_command2)


# Generated at 2022-06-14 10:16:39.961314
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm -r dir")) == "git rm -r -r dir"

# Generated at 2022-06-14 10:16:41.804853
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test.txt', '')) == 'git rm -r test.txt'

# Generated at 2022-06-14 10:16:45.320013
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command('git rm file.txt', ''))


# Generated at 2022-06-14 10:16:52.960556
# Unit test for function match
def test_match():
    assert match(Command('git rm file', ''))
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r', 'Error'))
    assert not match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r', 'Error', 'Error'))


# Generated at 2022-06-14 10:16:56.644386
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm directory', '', 'fatal: not removing \'directory\' recursively without -r')
    assert get_new_command(command) == 'git rm -r directory'

# Generated at 2022-06-14 10:17:05.102743
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    output = ("fatal: not removing 'setup.py' recursively without -r")
    command = Command('git rm setup.py', output)
    new_command = get_new_command(command)
    assert new_command == 'git rm -r setup.py'

# Generated at 2022-06-14 10:17:14.802449
# Unit test for function get_new_command
def test_get_new_command():
    command_1 = """git rm file/to/remove"""
    command_2 = """git rm file/to/remove/"""
    command_3 = """git rm directory/to/remove/"""
    command_4 = """git rm -recursive directory/to/remove/"""
    command_5 = """git rm -not-rm-flag file/to/remove"""
    command_6 = """git rm -not-rm-flag directory/to/remove/"""
    command_7 = """git rm -recursive-and-not-rm-flag directory/to/remove/"""
    command_8 = """git rm -not-rm-flag -recursive-and-not-rm-flag directory/to/remove/"""
    command_9 = """git rm -recursive -recursive-and-not-rm-flag directory/to/remove/"""



# Generated at 2022-06-14 10:17:19.022009
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r test' == get_new_command(Command(
        'git rm test',
        'fatal: not removing \'test\' recursively without -r',
        ''))

# Generated at 2022-06-14 10:17:26.504570
# Unit test for function get_new_command
def test_get_new_command():
    script = "git rm 'log/development.log' [develop]"
    output = "fatal: not removing 'log/development.log' recursively without -r"
    from mock import Mock
    command = Mock(script=script, output=output, script_parts=['git', 'rm', 'log/development.log', '[develop]'])
    assert match(command)
    assert get_new_command(command) == "git rm -r log/development.log [develop]"

# Generated at 2022-06-14 10:17:28.568266
# Unit test for function match
def test_match():
    assert(match(command = Command('git rm -r')) == True)


# Generated at 2022-06-14 10:17:32.036692
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm -r folder'
    output = "fatal: not removing 'folder' recursively without -r"
    assert get_new_command(Command('', script, output)) == script

# Generated at 2022-06-14 10:17:42.586590
# Unit test for function match
def test_match():
	assert match(Command(script='git rm -r myfolder',
						 output="fatal: not removing 'myfolder' recursively without -r"))
	assert not match(Command(script='git rm -r myfile',
							 output="Success"))
	assert not match(Command(script='git rm -r myfile',
							 output="fatal: not removing 'myfile' recursively without -r"))
	assert not match(Command(script='git rm -r',
							 output="fatal: not removing 'myfile' recursively without -r"))


# Generated at 2022-06-14 10:17:49.022482
# Unit test for function match
def test_match():
    command = Command('git rm -f foo', output="fatal: not removing 'foo' "
                                              "recursively without -r")
    assert match(command)



# Generated at 2022-06-14 10:17:52.367041
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command(script='git rm -rf file', output='fatal: not removing \'file\' recursively without -r')) == 'git rm -r -rf file')



# Generated at 2022-06-14 10:17:55.764121
# Unit test for function match
def test_match():
    assert match(Command('git rm file_test',
                         'fatal: not removing \'file_test\' recursively without -r'))
    assert match(Command('git rm file_test', '')) is None


# Generated at 2022-06-14 10:18:05.545836
# Unit test for function get_new_command
def test_get_new_command():
	command = type('obj', (object,), {'script_parts': 'rm -rf filename'.split(), 'script': 'rm -rf filename', 'output': 'fatal: not removing \'filename\' recursively without -r'})
	assert (get_new_command(command) == 'rm -rf -r filename')

# Generated at 2022-06-14 10:18:13.412618
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', 'fatal: not removing \'file\''))
    assert not match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm -r file', 'fatal: not removing \'file\' recursively without -r'))



# Generated at 2022-06-14 10:18:16.048212
# Unit test for function get_new_command

# Generated at 2022-06-14 10:18:19.277972
# Unit test for function match
def test_match():
	command=Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r')
	assert match(command)


# Generated at 2022-06-14 10:18:22.252298
# Unit test for function match
def test_match():
    assert match(Command('git rm file/',
                   'fatal: not removing \'file/\' recursively without -r'))


# Generated at 2022-06-14 10:18:28.873850
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf directory', 
        'fatal: not removing \'directory\' recursively without -r', '', 0))
    assert not match(Command('git rm -rf directory', '', '', 0))
    assert not match(Command('git rm -r file', '', '', 0))


# Generated at 2022-06-14 10:18:30.615702
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm /tmp/file')) == 'git rm -r /tmp/file'

# Generated at 2022-06-14 10:18:35.154753
# Unit test for function get_new_command
def test_get_new_command():
    raw_command = u"git rm new_directory_name"
    wrong_command = Command(raw_command, u"fatal: not removing 'new_directory_name' recursively without -r\n")
    
    new_command = get_new_command(wrong_command)
    assert new_command == u"git rm -r new_directory_name"


# Generated at 2022-06-14 10:18:47.343330
# Unit test for function get_new_command
def test_get_new_command():

    # Setup test case
    # There is a space in the input, before 'rm'
    output = ["fatal: not removing '/mnt/c/Users/morga/Documents/GitHub/Django-News-Summary/src/django_news_summary_app/migrations/0011_auto_20190212_0300.py' recursively without -r"]
    script = " git rm '/mnt/c/Users/morga/Documents/GitHub/Django-News-Summary/src/django_news_summary_app/migrations/0011_auto_20190212_0300.py'"
    command = Command('test', script, output)
    # Unit test
    new_command = get_new_command(command)

# Generated at 2022-06-14 10:18:52.879989
# Unit test for function get_new_command
def test_get_new_command():
    """Tests get_new_command funtion with two tests"""
    """Test 1"""
    assert get_new_command('git rm -r dir') == 'git rm -r -r dir'
    """Test 2"""
    assert get_new_command('git rm file') == 'git rm -r file'

# Generated at 2022-06-14 10:19:04.295832
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file') == 'git rm -r file'

# Generated at 2022-06-14 10:19:07.915735
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(
        Command(script="git rm sample.txt",
                output="fatal: not removing 'sample.txt' recursively without -r"))
            == "git rm -r sample.txt")

# Generated at 2022-06-14 10:19:14.623852
# Unit test for function match
def test_match():
    command = Command('git rm -r README.md', 'fatal: not removing \'README.md\' recursively without -r')
    assert match(command)
    command = Command('git rm README.md', 'fatal: not removing \'README.md\' recursively without -r')
    assert not match(command)
    command = Command('git rm -rf README.md', 'fatal: not removing \'README.md\' recursively without -r')
    assert not match(command)


# Generated at 2022-06-14 10:19:18.516573
# Unit test for function get_new_command
def test_get_new_command():
        command = Command("git rm file_name", "fatal: not removing 'file_name' recursively without -r")
        assert 'git rm -r file_name' == get_new_command(command)

# Generated at 2022-06-14 10:19:25.204540
# Unit test for function match
def test_match():
    assert match(Command('git branch branch-name', '', '',
        'fatal: not removing \'branch-name\' recursively without -r'))
    assert not match(Command('git branch branch-name', '', '',
        'fatal: not removing branch-name recursively without -r'))
    assert not match(Command('git rm file', '', '', ''))


# Generated at 2022-06-14 10:19:28.195280
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm "my path/to/file"',
                      'fatal: not removing \'my path/to/file\' recursively without -r', 0)
    assert get_new_command(command) == 'git rm -r "my path/to/file"'

# Generated at 2022-06-14 10:19:32.626927
# Unit test for function get_new_command
def test_get_new_command():
    command = "git rm -r dir1/dir2"
    command_parts = command.split(' ')

    reordered_command = get_new_command(Command(command, '', command_parts))
    assert command != reordered_command
    assert reordered_command.split(' ')[2] == '-r'

# Generated at 2022-06-14 10:19:36.044826
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command("git rm 'src/package/'", "fatal: not removing 'src/package/' recursively without -r")) == "git rm -r 'src/package/'"

# Generated at 2022-06-14 10:19:37.388443
# Unit test for function match
def test_match():
    assert match(command="git rm foo.txt")


# Generated at 2022-06-14 10:19:47.571117
# Unit test for function get_new_command
def test_get_new_command():
    # Remove a file
    output = u"fatal: not removing 'dir1/dir2/file1.txt' recursively without -r"
    command = Command('git rm dir1/dir2/file1.txt', output)
    assert get_new_command(command) == 'git rm -r dir1/dir2/file1.txt'
    # Remove a folder
    output = u"fatal: not removing 'dir1/dir2/' recursively without -r"
    command = Command('git rm -r dir1/dir2', output)
    assert get_new_command(command) == 'git rm -r -r dir1/dir2'

# Generated at 2022-06-14 10:20:09.271303
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm -r test.py') == 'git rm -r -r test.py'


# Generated at 2022-06-14 10:20:15.504622
# Unit test for function match
def test_match():
    assert match(Command('rm file', '', 'fatal: not removing \'file\' recursively without -r'))
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', '', 'No such file or directory'))


# Generated at 2022-06-14 10:20:18.558730
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r')) == 'git rm -r foo'

# Generated at 2022-06-14 10:20:25.122514
# Unit test for function match
def test_match():
    assert match(Command("git rm test", output="fatal: not removing 'test' recursively without -r"))
    assert not match(Command("git-rm test", output="fatal: not removing 'test' recursively without -r"))
    assert not match(Command("rm -rf test", output="fatal: not removing 'test' recursively without -r"))
    assert not match(Command("git rm test", output="fatal not removing 'test' recursively without -r"))


# Generated at 2022-06-14 10:20:32.131844
# Unit test for function match
def test_match():
    assert match(Command('git rm . -rf', 'fatal: not removing \'.\' recursively without -r'))
    assert not match(Command('git rm . -rf', ''))
    assert not match(Command('git commit -m "fix git"', 'fatal: not removing \'.\' recursively without -r'))

# Generated at 2022-06-14 10:20:35.177230
# Unit test for function match
def test_match():
	assert match(Command('git rm file.py', 
		'''fatal: not removing 'file.py' recursively without -r
		'''))



# Generated at 2022-06-14 10:20:42.322791
# Unit test for function match
def test_match():
    assert match(
        Command('rm test/shell/fuck',
                'fatal: not removing \'test/shell/fuck\' recursively without -r',
                ''))
    assert not match(
        Command('rm -r test/shell/fuck',
                '',
                ''))
    assert not match(
        Command('rm test/shell/fuck',
                '',
                ''))

# Generated at 2022-06-14 10:20:44.489040
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file1')
    assert get_new_command(command) == 'git rm -r file1'

# Generated at 2022-06-14 10:20:47.047864
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command('git rm test.txt') == 'git rm -r test.txt')
    

# Generated at 2022-06-14 10:20:53.407560
# Unit test for function match
def test_match():
    assert match(Command('git rm xxx', 'fatal: not removing \'xxx\' recursively without -r'))
    assert match(Command('hg rm xxx', ''))
    assert match(Command('git rm xxx', '')) is False
    assert match(Command('git rm -r xxx', '')) is False


# Generated at 2022-06-14 10:21:38.551486
# Unit test for function get_new_command
def test_get_new_command():
    """
    Test for function get_new_command
    """
    command = Command('git rm submodule',
                      'fatal: not removing \'submodule\' recursively without -r\n'
                      'Did you mean \'rm --cached submodule\' ?')
    new_command = get_new_command(command)
    assert 'git rm -r submodule' == new_command

# Generated at 2022-06-14 10:21:42.015779
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git status', 'git status'))


# Generated at 2022-06-14 10:21:45.944549
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo/bar.txt', 'fatal: not removing \'foo/bar.txt\' recursively without -r')
    assert get_new_command(command) == 'git rm -r foo/bar.txt'

# Generated at 2022-06-14 10:21:48.976658
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file', 'fatal: not removing \'file\' recursively without -r')
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:21:57.023171
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git not-there')
    output = ('fatal: not removing \'mitosis/tests/test_core.py\' recursively '
              'without -r\n')
    command = Command(command.script, output)
    assert get_new_command(command) == 'git rm -r not-there'

# Generated at 2022-06-14 10:21:59.570629
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(' git rm -r')
    assert(get_new_command(command) == ' git rm -r -r')

# Generated at 2022-06-14 10:22:05.983197
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf dir', '', ''))
    assert not match(Command('git rm -rf dir', '', 'fatal: not removing \'dir\' recursively without -r'))
    assert not match(Command('git rm -rf dir', '', 'fatal: not removing \'dir\' recursively without -r', '', 1))



# Generated at 2022-06-14 10:22:09.073268
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r A', 'fatal: not removing \'A\' recursively without -r')
    assert get_new_command(command) == u'git rm -r -r A'

# Generated at 2022-06-14 10:22:16.844422
# Unit test for function get_new_command
def test_get_new_command():
    # Take a simple case
    command = Command('rm -ff racc/')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r -ff racc/'

    # Take a more complex case
    command = Command('git rm -ff racc/')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r -ff racc/'

# Generated at 2022-06-14 10:22:22.198210
# Unit test for function match
def test_match():
    output = "fatal: not removing 'test/test_runner.pyc' recursively without -r"
    command = Command(' rm test/test_runner.pyc', output)
    script = "git rm test/test_runner.pyc"
    assert match(command)
    command = Command(script, output)
    assert match(command)



# Generated at 2022-06-14 10:23:46.479842
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -f lib')) == 'git rm -rf -f lib'

# Generated at 2022-06-14 10:23:57.119052
# Unit test for function match
def test_match():
    from thefuck.rules.git_rm_dir import match
    command1 = FakeCommand('git rm -r test_dir', 'fatal: not removing ''test_dir'' recursively without -r\n', '')
    command2 = FakeCommand('git rm test_dir', 'fatal: not removing ''test_dir'' recursively without -r\n', '')
    command3 = FakeCommand('git rm -f test_dir', 'fatal: not removing ''test_dir'' recursively without -r\n', '')
    command4 = FakeCommand('git rm test_dir', 'fatal: not removing ''test_dir'' recursively without -r\n', '')
    
    assert not match(command1)
    assert match(command2)
    assert match(command3)
    assert match(command4)


