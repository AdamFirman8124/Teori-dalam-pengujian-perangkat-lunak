

# Generated at 2022-06-14 10:14:00.522613
# Unit test for function match
def test_match():
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('ls', '', 'fatal: not removing \'\' recursively without -r'))


# Generated at 2022-06-14 10:14:12.557962
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script_output = "[master 0b93c8e] Adding submodule from 'git://github.com/nvie/vim-flake8'\
    warning: LF will be replaced by CRLF in .gitmodules.\
    The file will have its original line endings in your working directory\
    fatal: not removing 'flake8/doc/tags' recursively without -r"
    assert get_new_command(Command('git add submodule git://github.com/nvie/vim-flake8 && git rm submodule git://github.com/nvie/vim-flake8', script_output)) == \
            'git add submodule git://github.com/nvie/vim-flake8 && git rm -r submodule git://github.com/nvie/vim-flake8'
    assert get_new_command

# Generated at 2022-06-14 10:14:15.490407
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git rm a b c', '', None)) == 'git rm -r a b c')

# Generated at 2022-06-14 10:14:19.319441
# Unit test for function match
def test_match():
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', '', 'error'))


# Generated at 2022-06-14 10:14:23.268249
# Unit test for function match
def test_match():
    # 1. Test for positive result
    assert match('git rm 1') == True

    # 2. Test for negative result
    assert match('git rm 1 -r') == False
    assert match('git rm') == False
    assert match('grep pattern') == False


# Generated at 2022-06-14 10:14:30.559500
# Unit test for function match
def test_match():
    def do_test(command, expected):
        assert match(Command(script=command,
                             output='fatal: not removing xxxx recursively without -r')) == expected

    do_test('git rm file', True)
    do_test('git rm', False)
    do_test('git rm -r file', False)
    do_test('git rm -r xxxx', False)



# Generated at 2022-06-14 10:14:39.820665
# Unit test for function match
def test_match():
    assert match(Command('git rm -r foo',
                         'fatal: not removing \'foo\' recursively'
                         ' without -r\n',
                         'git rm -r foo'))

    assert not match(Command('git rm -r foo',
                         'fatal: not removing \'foo\' recursively'
                         ' without -r\n',
                         'git rm foo'))

    assert not match(Command('git rm -r foo',
                         'fatal: not removing \'foo\' recursively'
                         ' without -r\n',
                         'rm foo'))


# Generated at 2022-06-14 10:14:45.728284
# Unit test for function match
def test_match():
    assert match(Command(script='git rm -rf foo bar', output='fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command(script='git rm -f foo bar', output='fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command(script='git rm -rf foo bar', output='fatal: not removing \'foo\' recursively with -r'))


# Generated at 2022-06-14 10:14:48.216288
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test.md')
    assert get_new_command(command) == 'git rm -r test.md'

# Generated at 2022-06-14 10:15:00.804288
# Unit test for function match
def test_match():
    # Test match function under default condition
    assert match(Command('git rm -f docs/'))
    # Test match function under 'fatal: not removing' condition
    assert match(Command('git rm -f docs', 'fatal: not removing'))
    # Test match function under recursively condition
    assert match(Command('git rm -f docs', 'without -r'))
    # Test not match function under normal condition
    assert not match(Command('git rm -f docs', 'good'))


# Generated at 2022-06-14 10:15:07.657194
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm test", "")) == "git rm -r test"
    assert get_new_command(Command("git rm test/", "")) == "git rm -r test/"
    assert get_new_command(Command("git rm test/ -rf", "")) == "git rm -rf -r test/"

# Generated at 2022-06-14 10:15:10.814909
# Unit test for function match
def test_match():
    # Test match first
    command = Command('rm -r test', 'fatal: not removing \'test\' recursively without -r')
    assert match(command)
    # Test no match
    command = Command('rm -r test', '')
    assert not match(command)



# Generated at 2022-06-14 10:15:17.914598
# Unit test for function match
def test_match():
	assert match(Command('git rm project/file.txt', 'fatal: not removing \'project/file.txt\' recursively without -r'))
	assert not match(Command('git rm project/file.txt', 'fatal: not removing \'project/file.txt\''))
	assert not match(Command('git rm project', 'fatal: not removing \'project\' recursively without -r'))

# Generated at 2022-06-14 10:15:22.796953
# Unit test for function match
def test_match():
    git_modules = {'git': 'git'}
    assert match(Command('git rm README', '', '', git_modules=git_modules))
    assert not match(Command('ls', '', '', git_modules=git_modules))
    assert not match(Command('git ls', '', '', git_modules=git_modules))


# Generated at 2022-06-14 10:15:32.411086
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm file').script == 'rm -r file'
    assert get_new_command('rm file1 file2').script == 'rm -r file1 file2'
    assert get_new_command('rm file1 file2 file3').script == 'rm -r file1 file2 file3'
    assert get_new_command('rm  -f file').script == 'rm -r -f file'
    assert get_new_command('rm  --cached file').script == 'rm -r --cached file'

# Generated at 2022-06-14 10:15:36.296942
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', ''))


# Generated at 2022-06-14 10:15:39.368668
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command("git rm test", "fatal: not removing 'test' recursively without -r \n")
    command2 = get_new_command(command1)
    assert command2 == "git rm -r test"

# Generated at 2022-06-14 10:15:54.808828
# Unit test for function get_new_command
def test_get_new_command():
    assert_equal(u"git rm -r file", get_new_command(Command('git rm file')))
    assert_equal(u"git rm -r file1 file2", get_new_command(Command('git rm file1 file2')))
    assert_equal(u"git rm -r file", get_new_command(Command('git rm file', 'error: pathspec file', 'Did you mean this?', 'error: pathspec file')))

    assert_equal(u"git rm -r file", get_new_command(Command('git rm file', 'fatal: not removing file recursively without -r', 'Did you mean this?')))

# Generated at 2022-06-14 10:16:00.197233
# Unit test for function match
def test_match():
    # check that we can find the correct match
    assert match(Command('git rm -rf', 'fatal: not removing \'.gitignore\' recursively without -r'))

    # check that this is a false positive
    assert not match(Command('git rm -rf', 'fatal: bad option: -f'))

# Generated at 2022-06-14 10:16:04.669338
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file1 file2')) == 'git rm -r file1 file2'
    assert get_new_command(Command('git rm -a file1 file2')) == 'git rm -a -r file1 file2'

# Generated at 2022-06-14 10:16:14.383477
# Unit test for function match
def test_match():
    assert match(Command('git rm -r',
                stderr='fatal: not removing \'path/to/dir\' recursively without -r'))
    assert not match(Command('git remote -v',
                             stderr='fatal: not removing \'path/to/dir\' recursively without -r'))

# Generated at 2022-06-14 10:16:23.688385
# Unit test for function match
def test_match():
    assert(match(Command(script='git rm -r file_without_extension'
                         , output='fatal: not removing \'file_without_extension\''
                         ' recursively without -r')) is True)
    assert(match(Command(script='git rm -r file_without_extension'
                         , output='fatal: not removing \'file_without_extension\''
                         ' recursively without -r')) is True)
    assert(match(Command(script='git rm file_without_extension'
                         , output='fatal: not removing \'file_without_extension\''
                         ' recursively without -r')) is False)

# Generated at 2022-06-14 10:16:34.361166
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    new_cmd = get_new_command(Command(script='git rm -f .idea/workspace.xml',
                                        stderr='fatal: not removing \'.idea/workspace.xml\' recursively without -r\n',
                                        script_parts=['git', 'rm', '-f', '.idea/workspace.xml'],
                                        stderr_parts=['fatal:', 'not', 'removing', '\'.idea/workspace.xml\'', 'recursively', 'without', '-r\n']))
    assert new_cmd == 'git rm -r -f .idea/workspace.xml'

# Generated at 2022-06-14 10:16:39.653562
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm foo", None, "")) \
            == "git rm -r foo"
    assert get_new_command(Command("git rm 'foo'", None, "")) \
            == "git rm -r 'foo'"
    assert get_new_command(Command("git rm \"foo\"", None, "")) \
            == "git rm -r \"foo\""

# Generated at 2022-06-14 10:16:43.805856
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf a b', 'fatal: not removing \'b\' recursively without -r'))
    assert not match(Command('git rm -rf c a', 'fatal: not removing \'b\' recursively without -r'))


# Generated at 2022-06-14 10:16:48.636944
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    command = Command("gir rm -rf --cached /home/user/testing")
    assert get_new_command(command) == "git rm -r -rf --cached /home/user/testing"

# Generated at 2022-06-14 10:16:52.726880
# Unit test for function match
def test_match():
    assert match(Command('git stash rm "stash@{0}"'))
    assert not match(Command('git stash rm "stash@{0}"'))
    assert not match(Command('git stash show -p "stash@{0}"'))

# Generated at 2022-06-14 10:16:58.222691
# Unit test for function get_new_command
def test_get_new_command():
    command_parts=['git', 'rm', '-r']
    index = command_parts.index('rm') + 1
    command_parts.insert(index, '-r')
    assert get_new_command(['git', 'rm', 'path']) == u' '.join(command_parts)

# Generated at 2022-06-14 10:17:01.784514
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm a", "", "fatal: not removing 'a' recursively without -r")
    command.script_parts = command.script.split()
    assert get_new_command(command) == 'git rm -r a'

# Generated at 2022-06-14 10:17:06.039164
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file', 'fatal: not removing \'file\' recursively without -r')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r file'

# Generated at 2022-06-14 10:17:12.105452
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm data')) == 'git rm -r data'



# Generated at 2022-06-14 10:17:16.862342
# Unit test for function match
def test_match():
    assert match(Command('git rm file1'))
    assert match(Command('git rm file1 file2'))
    assert not match(Command('git rm -r file1'))
    assert not match(Command('git rm file1 -r'))


# Generated at 2022-06-14 10:17:21.103611
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm file') == 'rm -r file'
    assert get_new_command('rm -rf file') == 'rm -rf file'
    assert get_new_command('git remote rm file') == 'git remote rm -r file'

# Generated at 2022-06-14 10:17:24.819333
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file',
        'fatal: not removing \'file\' recursively without -r\n', None, 1, None)) == 'git rm -r file'

# Generated at 2022-06-14 10:17:27.564168
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm -r dir") == "git rm -r -r dir"
    assert get_new_command("git rm dir") == "git rm -r dir"

# Generated at 2022-06-14 10:17:31.088297
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -f test',
                                   'fatal: not removing \'test\' recursively without -r', '')) == u'git rm -r -f test'

# Generated at 2022-06-14 10:17:44.173928
# Unit test for function get_new_command
def test_get_new_command():
    assert_equals(get_new_command(Command("git rm")),
                  "git rm -r")
    assert_equals(get_new_command(Command("git rm abc")),
                  "git rm -r abc")
    assert_equals(get_new_command(Command("git rm abc def")),
                  "git rm -r abc def")
    assert_equals(get_new_command(Command("git rm -f")),
                  "git rm -f")
    assert_equals(get_new_command(Command("git rm abc -f")),
                  "git rm -r abc -f")
    assert_equals(get_new_command(Command("git rm -f abc")),
                  "git rm -r -f abc")

# Generated at 2022-06-14 10:17:50.556124
# Unit test for function get_new_command
def test_get_new_command():
    command_output = "fatal: not removing 'ciao.txt' recursively without -r"
    command = Command('git rm ciao.txt', command_output)
    assert get_new_command(command) == 'git rm -r ciao.txt'


# Generated at 2022-06-14 10:17:52.958500
# Unit test for function match
def test_match():
    assert match(Command('git rm', 'fatal: not removing ...'))
    assert not match(Command('git branch', '...'))


# Generated at 2022-06-14 10:17:54.549909
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -f foo', output='fatal: not removing \'foo\' recursively without -r')) == 'git rm -r -f foo'

# Generated at 2022-06-14 10:17:59.113125
# Unit test for function match
def test_match():
    assert match(Command("git rm directory", ""))
    assert not match(Command("git rm file", ""))

# Generated at 2022-06-14 10:18:09.825186
# Unit test for function match
def test_match():
    from os import curdir

    from .utils import Command

    assert match(Command('git rm foo'))
    assert match(Command('git rm -rf foo'))
    assert match(Command('git rm -rf foo bar'))
    assert match(Command('git rm foo', "fatal: not removing 'foo' recursively without -r"))
    assert match(Command('git rm -rf foo', "fatal: not removing 'foo' recursively without -r"))
    assert match(Command('git rm foo bar', "fatal: not removing 'foo' recursively without -r"))
    assert not match(Command('git rm -r foo', curdir))
    assert not match(Command('git rm -r foo bar', curdir))


# Generated at 2022-06-14 10:18:13.684487
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git rm -r file/'
    output = 'fatal: not removing \'file/\' recursively without -r'
    assert(get_new_command(Command(command, output))) == 'git rm -r -r file/'

# Generated at 2022-06-14 10:18:25.886932
# Unit test for function match
def test_match():
    assert(match(Command('git rm folder/')) == False)
    assert(match(Command('git rm -r')) == False)
    assert(match(Command('git rm -r folder')) == False)
    assert(match(Command(
        'git rm folder',
        'fatal: not removing \'folder\' recursively without -r\n'
    )))
    assert(match(Command(
        'git rm folder',
        'fatal: not removing \'folder recursively without -r\n'
    )) == False)
    assert(match(Command(
        'git rm folder',
        'fatal: not removing \'folder\' recursively without -rfolder\'\n'
    )) == False)


# Generated at 2022-06-14 10:18:30.221838
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(
        script='git push',
        stdout='git: \'push\' is not a git command. See \'git --help\'.')
    assert get_new_command(command) == 'git push'

# Generated at 2022-06-14 10:18:33.343218
# Unit test for function match
def test_match():
    assert match(Command('rm -r foo',
                         stderr='fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git config user.name', ''))


# Generated at 2022-06-14 10:18:42.807145
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm import get_new_command
    git_rm_command = 'rm test'
    assert get_new_command(Command(script=git_rm_command,
                                   stderr='fatal: not removing \'test\' recursively without -r')) == 'git rm -r test'
    git_rm_command = 'git rm te st'
    assert get_new_command(Command(script=git_rm_command,
                                   stderr='fatal: not removing \'test\' recursively without -r')) == 'git rm -r te st'

# Generated at 2022-06-14 10:18:44.822807
# Unit test for function get_new_command
def test_get_new_command():
    assert git.get_new_command(Command('git rm test')) == 'git rm -r test'

# Generated at 2022-06-14 10:18:46.805528
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm test.py') == 'git rm -r test.py'

# Generated at 2022-06-14 10:18:56.264509
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', stderr='fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo'))
    assert not match(Command('git rm foo', stderr='fatal: not removing'))
    assert not match(Command('git rm foo', stderr='fatal: not removing \'foo\' recursively without'))
    assert not match(Command('rm foo', stderr='fatal: not removing \'foo\' recursively without -r'))


# Generated at 2022-06-14 10:19:06.052326
# Unit test for function get_new_command
def test_get_new_command():
    command_shortcut = "git rm"
    command = "git rm file.c"
    command_output = "fatal: not removing 'file.c' recursively without -r"

    assert_equals(get_new_command(Command(command, command_output,
                                          command_shortcut)),
                  "git rm -r file.c"
                  )

# Generated at 2022-06-14 10:19:09.057250
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r')) == 'git rm -r test.txt')

# Generated at 2022-06-14 10:19:15.114051
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r',
                                   'fatal: not removing \'foo\' recursively without -r', '')) == 'git rm -r -r'
    assert get_new_command(Command('git rm -r foo bar',
                                   'fatal: not removing \'foo\' recursively without -r', '')) == 'git rm -r -r foo bar'

# Generated at 2022-06-14 10:19:20.335790
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm "file with spaces"', '', 
                      script_parts=['git', 'rm', '"file with spaces"'], output='fatal: not removing "file with spaces" recursively without -r')
    assert get_new_command(command) == 'git rm -r "file with spaces"'

# Generated at 2022-06-14 10:19:23.569057
# Unit test for function get_new_command
def test_get_new_command():
    old_command = 'git rm -r -f'
    new_command = get_new_command(old_command)
    assert new_command == 'git rm -r -f -r'

# Generated at 2022-06-14 10:19:32.150816
# Unit test for function match
def test_match():
    assert match(Command('rm', 'fatal: not removing \'foo\''
                         ' recursively without -r',
                         '', ''))
    assert match(Command('git rm', 'fatal: not removing \'foo\''
                         ' recursively without -r',
                         '', ''))
    assert match(Command('git rm', 'fatal: not removing \'foo\''
                         ' recursively without -r',
                         '', ''))
    assert not match(Command('git rm', '', '', ''))
    assert not match(Command('rm', '', '', ''))


# Generated at 2022-06-14 10:19:35.504937
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm a b')) == 'git rm -r a'
    assert get_new_command(Command('rm a b/c')) == 'git rm -r a b/c'

# Generated at 2022-06-14 10:19:40.291453
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm subdir/')
    command.script_parts = ['git', 'rm', 'subdir/']
    command.output = 'fatal: not removing \'subdir/\' recursively without -r\n'
    assert get_new_command(command) == 'git rm -r subdir/'

# Generated at 2022-06-14 10:19:44.738450
# Unit test for function match
def test_match():
    assert match(Command('rm -rf config',
                         'fatal: not removing \'config\' recursively without -r',
                         '', 1))
    assert not match(Command('', '', '', 1))



# Generated at 2022-06-14 10:19:52.688834
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file', ''))


# Generated at 2022-06-14 10:20:03.422531
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command("git rm -r")
    assert get_new_command(cmd) == "git rm -r"



# Generated at 2022-06-14 10:20:05.816207
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm main.py other.py')) == 'git rm -r main.py other.py'

# Generated at 2022-06-14 10:20:15.723835
# Unit test for function match
def test_match():
    # Test when match is true
    assert match(Command('git rm -r -f'))
    assert match(Command('git rm -rf'))
    assert match(Command('git rm -rf *'))
    assert match(Command('git rm -rf * .'))
    assert match(Command('git rm -rf . .'))
    assert match(Command('git rm -rf . . .'))
    assert match(Command('git rm -rf . . . . . . . . . . . . . . . . . . . . . .'))

    # Test when match is false
    assert not match(Command('git add -r'))
    assert not match(Command('git rm -f'))
    assert not match(Command('git rm -r'))
    assert not match(Command('git rm -r -f'))

# Generated at 2022-06-14 10:20:19.230578
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r\n'))
    assert not match(Command('git status', ''))


# Generated at 2022-06-14 10:20:27.112482
# Unit test for function match
def test_match():
    assert match(Command(' git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r'))
    assert not match(Command('git rm test.txt', 'fatal: not removing \'test.txt\''))
    assert not match(Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without r'))


# Generated at 2022-06-14 10:20:30.920708
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf .', 'fatal: not removing \'dir\' recursively without -r')) == "git rm -rf -r ."

# Generated at 2022-06-14 10:20:39.328784
# Unit test for function match
def test_match():
    assert match(Command('rm /tmp/foo/baz'))
    assert not match(Command('rm /tmp/foo/baz', 'fatal: not removing \'/tmp/foo\' recursively without -r\n'))
    assert not match(Command('rm /tmp/foo/baz', '', 'fatal: not removing \'/tmp/foo\' recursively without -r'))
    assert not match(Command('rm /tmp/foo/baz', '', '', 'fatal: not removing \'/tmp/foo\' recursively without -r'))



# Generated at 2022-06-14 10:20:45.366761
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf foo/', '', 'fatal: not removing \'foo/\' recursively without -r'))
    assert not match(Command('git rm -rf foo/', '', 'fatal: not removing \'foo.txt\' recursively without -r'))
    assert not match(Command('git status', '', ''))


# Generated at 2022-06-14 10:20:46.993959
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm myfile") == 'git rm -r myfile'

# Generated at 2022-06-14 10:20:50.146656
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file.txt',
                                   'fatal: not removing \'file.txt\''
                                   ' recursively without -r')) == 'git rm -r file.txt'

# Generated at 2022-06-14 10:21:06.123603
# Unit test for function match
def test_match():
  assert match(Command('git rm test.txt', u'fatal: not removing \'test.txt\' recursively without -r\n', '', 1, None))
  assert not match(Command('git rm -r test.txt', u'fatal: not removing \'test.txt\' recursively without -r\n', '', 1, None))
  assert not match(Command('rm test.txt', u'fatal: not removing \'test.txt\' recursively without -r\n', '', 1, None))


# Generated at 2022-06-14 10:21:08.421975
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file', '',
                                   'fatal: not removing \'file\' recursively without -r'))

# Generated at 2022-06-14 10:21:14.896649
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf foo',
                         output='fatal: not removing \'foo\' recursively without -r\n'))
    assert not match(Command('git remote -v',
                             output='fatal: not removing \'foo\' recursively without -r\n'))
    assert not match(Command('git rm -rf foo',
                             output='fatal: not removing \'bar\' recursively without -r\n'))
    assert match(Command('git rm -rf foo',
                         output='fatal: not removing \'foo\' recursively without -r\n'))

# Generated at 2022-06-14 10:21:19.103748
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r folder')
    assert get_new_command(command) == 'git rm -r -r folder'
    command = Command('git rm file')
    assert get_new_command(command) != 'git rm -r file'



# Generated at 2022-06-14 10:21:24.844201
# Unit test for function match
def test_match():
    assert match(Command("git rm file", "fatal: not removing 'file' recursively without -r"))
    assert not match(Command("git rm -r file", ""))
    assert not match(Command("git cfg", "fatal: not removing 'file' recursively without -r"))


# Generated at 2022-06-14 10:21:29.075932
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command(script='cd src && git rm -r module/',
                                    output='fatal: not removing '\
                                    '\'module/\' recursively without -r'))) == \
                                    'cd src && git rm -r -r module/'

# Generated at 2022-06-14 10:21:41.127782
# Unit test for function get_new_command
def test_get_new_command():
    # run twice to ensure command is not appended twice to script_parts
    assert get_new_command(Command('rm index.html',
                                 script='git rm index.html',
                                 stdout="fatal: not removing 'index.html' recursively without -r",
                                 stderr='')) == "git rm -r index.html"

    assert get_new_command(Command('rm index.html',
                                 script='git rm -r index.html',
                                 stdout="fatal: not removing 'index.html' recursively without -r",
                                 stderr='')) == "git rm -r index.html"


# Generated at 2022-06-14 10:21:44.158384
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm dir-name', '', '', '', '')
    assert get_new_command(command) == 'git rm -r dir-name'

# Generated at 2022-06-14 10:21:48.025256
# Unit test for function get_new_command
def test_get_new_command():
    command_txt = "git rm -r folder"
    command = Command(command_txt, "fatal: not removing 'folder' recursively without -r")
    assert get_new_command(command) == u'git rm -r -r folder'

# Generated at 2022-06-14 10:22:01.976331
# Unit test for function match
def test_match():

    # regex matches when git output contains:
    # not removing 'dir-name' recursively without -r

    # The following example is taken from the following git output:
    # $ git rm file-name
    # fatal: not removing '<file-name>' recursively without -r
    assert match(Command('git rm file-name', 'fatal: not removing \'<file-name>\' recursively without -r\n'))

    # The following example is taken from the following git output:
    # $ git rm directory-name
    # fatal: not removing '<directory-name>' recursively without -r
    assert match(Command('git rm directory-name', 'fatal: not removing \'<directory-name>\' recursively without -r\n'))



# Generated at 2022-06-14 10:22:24.687090
# Unit test for function match
def test_match():
    assert match(Command(script='git add -A',
                         _err='fatal: not removing \'src/main/webapp/resources/images/pgn/rnbqkbnr/pppppppp/\' recursively without -r'))
    assert match(Command(script='git rm -rf --cached',
                         _err='fatal: not removing \'src/main/webapp/resources/images/pgn/rnbqkbnr/pppppppp/\' recursively without -r'))
    assert match(Command(script='git rm -rf --cached',
                         _err='fatal: not removing \'src/main/webapp/resources/images/pgn/rnbqkbnr/pppppppp/\' recursively without -r'))

# Generated at 2022-06-14 10:22:28.440405
# Unit test for function match
def test_match():
    command = Command('git rm new_file', '')
    assert(match(command))
    command = Command('git rm new_file', 'fatal: not removing \'new_file\' recursively without -r')
    assert(match(command))


# Generated at 2022-06-14 10:22:33.977985
# Unit test for function match
def test_match():
    command = Command('git rm -rf test', 'fatal: not removing \'test\' recursively without -r')
    assert match(command)

    command = Command('git rm -rf test', 'fatal: not removing \'test\' recursively without -r')
    assert not match(command)



# Generated at 2022-06-14 10:22:40.897462
# Unit test for function match
def test_match():
    assert git.match(Command('git rm test',
                             'fatal: not removing \'test\' recursively without -r'))
    assert git.match(Command('git rm -r test',
                             'fatal: not removing \'test\' recursively without -r'))
    assert git.match(Command('git rm -rf test',
                             'fatal: not removing \'test\' recursively without -r'))
    assert git.match(Command('git rm -r test',
                             'fatal: not removing \'test\' recursively without -r'))
    assert not git.match(Command('git rm -f test',
                                 'fatal: not removing \'test\' recursively without -r'))



# Generated at 2022-06-14 10:22:47.912530
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Correction
    correction = str(Correction(new_command='git rm -r foo',
                                output='fatal: not removing \'foo\' recursively without -r'))
    assert (test_get_new_command.__name__ in correction
            and 'git rm -r foo' in correction
            and 'fatal: not removing \'foo\' recursively without -r' in correction)

# Generated at 2022-06-14 10:22:56.681637
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_recursive_rm import get_new_command
    from thefuck.types import Command
    assert get_new_command(Command('git rm foo',
                                   'fatal: not removing \'foo\' recursively without -r',
                                   '')) == 'git rm -r foo'
    assert get_new_command(Command('git rm foo/',
                                   'fatal: not removing \'foo/\' recursively without -r',
                                   '')) == 'git rm -r foo/'
    assert get_new_command(Command('git rm foo/.',
                                   'fatal: not removing \'foo/\' recursively without -r',
                                   '')) == 'git rm -r foo/.'

# Generated at 2022-06-14 10:23:00.903746
# Unit test for function get_new_command
def test_get_new_command():
    command_to_test = "git rm directory"
    expected_output = "git rm -r directory"
    assert get_new_command(Command(script=command_to_test)) == expected_output

# Generated at 2022-06-14 10:23:04.437294
# Unit test for function match
def test_match():
    assert match(Command('rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r', 1,
                         False))
    assert not match(Command('rm file.txt', '', 1, False))
    assert not match(Command('cp /etc/test.conf ~', '', 1, False))


# Generated at 2022-06-14 10:23:08.794328
# Unit test for function match
def test_match():
    assert match(Command('git rm -r 2', 'fatal: not removing \'2\' recursively without -r'))
    assert not match(Command('git rm -r 2', 'fatal: not removing \'2\''))
    assert not match(Command('git rm 2', 'fatal: not removing \'2\' recursively without -r'))



# Generated at 2022-06-14 10:23:12.384536
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm 1 2 3 ', '''fatal: not removing '1' recursively without -r
    ''')) == 'git rm -r 1 2 3 '

# Generated at 2022-06-14 10:23:55.215404
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm dir',
                      'fatal: not removing \'dir\' recursively without -r\n',
                      '')
    assert get_new_command(command) == 'git rm -r dir'
    command = Command('git rm /usr/share/vim/vim74/syntax/cfg.vim',
                      'fatal: not removing \'/usr/share/vim/vim74/syntax/cfg.vim\' recursively without -r\n',
                      '')
    assert get_new_command(command) == 'git rm -r /usr/share/vim/vim74/syntax/cfg.vim'
