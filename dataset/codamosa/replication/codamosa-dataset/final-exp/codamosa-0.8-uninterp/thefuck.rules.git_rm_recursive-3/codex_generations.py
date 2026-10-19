

# Generated at 2022-06-14 10:14:02.142890
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script = 'git rm ', output = 'fatal: not removing \'.gitignore\' recursively without -r')) == 'git rm -r .gitignore'
    assert get_new_command(Command(script = 'git rm .gitignore', output = 'fatal: not removing \'.gitignore\' recursively without -r')) == 'git rm -r .gitignore'

# Generated at 2022-06-14 10:14:04.692313
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r', ''))


# Generated at 2022-06-14 10:14:08.697477
# Unit test for function get_new_command
def test_get_new_command():
    command_ = Command("git rm -r 'folder'", "fatal: not removing 'folder' recursively without -r")
    _ = get_new_command(command_)
    assert command_.script == u'git rm -r -r folder'

# Generated at 2022-06-14 10:14:14.533620
# Unit test for function match
def test_match():
    assert match(Command('git rm file1', '', 'fatal: not removing \'dir/\' recursively without -r'))
    assert match(Command('git rm -r file1', '', 'fatal: not removing \'dir/\' recursively without -r'))
    assert not match(Command('git rm file1', '', ''))
    assert not match(Command('git mv file1', '', 'fatal: not removing \'dir/\' recursively without -r'))


# Generated at 2022-06-14 10:14:25.608877
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm foo/',
                                   output='fatal: not removing \'foo/\' recursively without -r')) == \
                                   'git rm -r foo/'
    assert get_new_command(Command(script='git rm -f foo/',
                                   output='fatal: not removing \'foo/\' recursively without -r')) == \
                                   'git rm -rf foo/'
    assert get_new_command(Command(script='git rm -n foo/',
                                   output='fatal: not removing \'foo/\' recursively without -r')) == \
                                   'git rm -rn foo/'

# Generated at 2022-06-14 10:14:29.794184
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {'script_parts': ['git', 'rm', 'file1', 'file2'], 'output': ''})
    assert get_new_command(command) == 'git rm -r file1 file2'

# Generated at 2022-06-14 10:14:33.827492
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm hello.py', "fatal: not removing 'hello.py' recursively without -r")
    assert get_new_command(command) == 'git rm -r hello.py'

# Generated at 2022-06-14 10:14:38.053344
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script = "git rm -rf test",
                      output = "fatal: not removing 'test' recursively without -r")
    assert(get_new_command(command) == "git rm -rf -r test")

# Generated at 2022-06-14 10:14:50.630952
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf foo', 'fatal: not removing \'foo\' recursively without -r'))
    assert match(Command('git rm -rf foo/bar', 'fatal: not removing \'foo/bar\' recursively without -r'))
    assert match(Command('git rm foo bar', 'fatal: not removing \'foo\' recursively without -r'))
    assert match(Command('git rm foo/bar', 'fatal: not removing \'foo/bar\' recursively without -r'))
    assert not match(Command('git rm foo/bar', 'fatal: not removing \'foo/bar\' recursively without -r\n'))
    assert not match(Command('git rm -r foo/bar', 'fatal: not removing \'foo/bar\' recursively without -r'))
    assert not match

# Generated at 2022-06-14 10:14:59.294085
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    script = "git rm --cached -r -- path/to/file"
    output = "fatal: not removing 'path/to/file' recursively without -r"
    assert u'git rm -r --cached -- path/to/file' == get_new_command(Command(script, output))

# Generated at 2022-06-14 10:15:04.875364
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test')) == u'git rm -r test'

# Generated at 2022-06-14 10:15:06.913399
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo')
    assert get_new_command(command) == 'git -r rm foo'

# Generated at 2022-06-14 10:15:10.735363
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm makedir', output='fatal: not removing \'makedir\' recursively without -r')
    assert get_new_command(command) == 'git rm -r makedir'

# Generated at 2022-06-14 10:15:22.426852
# Unit test for function match
def test_match():
    assert match(Command(script="git rm README.md", output="fatal: not removing 'README.md' recursively without -r")), 'match function should return True since the error message is matched correctly'
    assert not match(Command(script="git rm README.md", output="fatal: not removing 'README.md' recursively with -r")), 'match function should return False since the error message is not matched'
    assert not match(Command(script="git add README.md", output="fatal: not removing 'README.md' recursively without -r")), 'match function should return False since the command is not git rm'

# Generated at 2022-06-14 10:15:27.083878
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm import get_new_command
    command = Command('git rm -r a.txt')
    assert get_new_command(command) == 'git rm -r a.txt'

# Generated at 2022-06-14 10:15:30.758949
# Unit test for function match
def test_match():
    command = Mock(script='git rm file1 file2 file3 file4',
                   output="fatal: not removing 'file2' recursively without -r")
    assert (match(command) == True)


# Generated at 2022-06-14 10:15:36.364335
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm README.md',
                                   'fatal: not removing '
                                   '\'README.md\' recursively without -r'
                                   '\ngit rm: use \'git rm --cached '
                                   'README.md\' to unstage')) == 'git rm -r README.md'

# Generated at 2022-06-14 10:15:39.236612
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r')
    assert get_new_command(command) == 'git rm -r foo'

# Generated at 2022-06-14 10:15:46.422493
# Unit test for function match
def test_match():
    assert match(Command('rm test', 'fatal: not removing \'test\' recursively without -r'))
    assert not match(Command('rm -r test', 'fatal: not removing \'test\' recursively without -r'))


# Generated at 2022-06-14 10:15:55.270110
# Unit test for function match
def test_match():
    assert match(Command(script = 'git rm file.txt',stderr='fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command(script = 'ls',stderr='fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command(script = 'git rm file.txt',stderr='usage: git rm [--force|--interactive] [--dry-run] [--cached] [--recursive] [--ignore-unmatch] file...'))



# Generated at 2022-06-14 10:15:59.972366
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file', '')
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:16:09.366058
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert match(Command('git mv file',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git mv file  ',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert match(Command('git rm file ',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file\n',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r'))
   

# Generated at 2022-06-14 10:16:16.801428
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file', 'fatal: not removing ...')) == 'git rm -r file'
    assert get_new_command(Command('$ git rm file', 'fatal: not removing ...')) == '$ git rm -r file'
    assert get_new_command(Command('$ git rm -f file', 'fatal: not removing ...')) == '$ git rm -f -r file'

# Generated at 2022-06-14 10:16:20.625613
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r file' == get_new_command(types.Command('git rm file',
                                                             'fatal: not removing \'file\' recursively without -r',
                                                             'git rm file'))

# Generated at 2022-06-14 10:16:31.579589
# Unit test for function match
def test_match():
    assert match(Mock(script='git rm lol'))
    assert match(Mock(script='git rm -r lol'))
    assert match(Mock(script='git rm -rf lol'))
    assert match(Mock(script='git rm lol/'))
    assert match(Mock(script='git rm -r lol/'))
    assert match(Mock(script='git rm -rf lol/'))
    assert match(Mock(script='git rm foo/lol'))
    assert match(Mock(script='git rm -r foo/lol'))
    assert match(Mock(script='git rm -rf foo/lol'))
    assert match(Mock(script='git rm foo/lol/'))
    assert match(Mock(script='git rm -r foo/lol/'))

# Generated at 2022-06-14 10:16:33.683680
# Unit test for function match
def test_match():
    assert match(command='git rm -rf test')
    assert not match(command='rm -rf test')
    assert not match(command='git push origin master')

# Generated at 2022-06-14 10:16:36.712672
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -f', u'fatal: not removing \'src/test.pyc\' recursively without -r')) == 'git rm -f -r'

# Generated at 2022-06-14 10:16:38.604759
# Unit test for function match
def test_match():
    assert match(Command('git branch | grep master | rm'))
    assert not match(Command('rm -rf /'))


# Generated at 2022-06-14 10:16:41.832503
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(u'git rm -r') == u'git rm -r'
    assert get_new_command(u'git rm -r file testfile') == u'git rm -r file testfile'

# Generated at 2022-06-14 10:16:43.589913
# Unit test for function match
def test_match():
    assert match(Command('git rm -r * --cached'))


# Generated at 2022-06-14 10:16:53.073987
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'foo\' recursively without -r',
                         ''))
    assert match(Command('git rm foo bar',
                         'fatal: not removing \'bar\' recursively without -r',
                         ''))

    assert not match(Command('git rm foo bar',
                             'fatal: not removing \'bar\' recursively without -r',
                             ''))


# Generated at 2022-06-14 10:16:58.008699
# Unit test for function match
def test_match():
	# Check when command is correct
	subprocess.check_output = MagicMock(return_value="fatal: not removing 'somefile' recursively without -r")
	command = Command('git rm somefile', '', '')
	assert match(command)


# Generated at 2022-06-14 10:17:00.853792
# Unit test for function get_new_command
def test_get_new_command():
    command_str = u'git rm to_delete'
    command_obj = Command(command_str, '')
    assert get_new_command(command_obj) == u'git rm -r to_delete'



# Generated at 2022-06-14 10:17:05.104305
# Unit test for function match
def test_match():
    command = 'git rm .'
    command_output = "fatal: not removing '.' recursively without -r"
    assert(match(Command(command, command_output)))


# Generated at 2022-06-14 10:17:13.362927
# Unit test for function match
def test_match():
    assert match(Command('git rm test/test_fuck.py', 'fatal: not removing \'test/test_fuck.py\' recursively without -r'))
    assert not match(Command('git rm -r test', 'fatal: not removing \'test\' recursively without -r'))
    assert not match(Command('git rm test/test_fuck.py', 'Deleted test/test_fuck.py'))
    assert not match(Command('git rm test/test_fuck.py', 'fatal: not removing \'test/test_fuck.py\' recursively without -r'))

# Generated at 2022-06-14 10:17:16.243707
# Unit test for function match

# Generated at 2022-06-14 10:17:26.609716
# Unit test for function match
def test_match():
    assert match(Command('git rm a', "fatal: not removing 'a' recursively without -r", ""))
    assert match(Command('git rm a/b', "fatal: not removing 'a/b' recursively without -r", ""))
    assert match(Command('git rm a/b/c', "fatal: not removing 'a/b/c' recursively without -r", ""))
    assert match(Command('git rm a/b/c d', "fatal: not removing 'd' recursively without -r", ""))
    assert not match(Command('git rm', "fatal: not removing '' recursively without -r", ""))


# Generated at 2022-06-14 10:17:34.847749
# Unit test for function match
def test_match():
    assert match(Command('git pull origin master', 'fatal: not removing \'drivers/net/ethernet/freescale/dpmac.c\' recursively without -r'))
    assert not match(Command('git pull origin master', 'fatal: not removing \'drivers/net/ethernet/freescale/dpmac.c\' recursively without -r', stderr='fatal: not removing \'drivers/net/ethernet/freescale/dpmac.c\' recursively without -r'))


# Generated at 2022-06-14 10:17:38.590562
# Unit test for function match
def test_match():
    assert match(Command('rm file',
                         "fatal: not removing 'file' recursively without -r"))
    assert not match(Command('rm file', ""))


# Generated at 2022-06-14 10:17:42.355870
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf', stderr=
    'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('rm'))


# Generated at 2022-06-14 10:17:49.819457
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm /tmp/sweet_child_omine") == "git rm -r /tmp/sweet_child_omine"

# Generated at 2022-06-14 10:17:55.855837
# Unit test for function match
def test_match():
    assert match(Command('git rm f*', "fatal: not removing 'f*' recursively without -r", ""))
    assert not match(Command('git rm f*', "fatal: not removing 'f*'", ""))
    assert not match(Command('git rm -r f*', "fatal: not removing 'f*' recursively without -r", ""))
    assert not match(Command('git push', 'fatal: not removing ', ''))

# Generated at 2022-06-14 10:18:00.104902
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'dir/bar\' recursively without -r\n'))
    assert not match(Command('git rm foo', ''))
    assert not match(Command('git push foo', ''))


# Generated at 2022-06-14 10:18:05.080941
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf not/a/real/path', 
        'fatal: not removing \'not/a/real/path\' recursively without -r',
        '', None, None)) == 'git rm -rf -r not/a/real/path'

# Generated at 2022-06-14 10:18:09.201361
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -r',
                                   stdout='fatal: not removing '
                                          '\'.travis.yml\' recursively without -r',
                                   stderr='')) == 'git rm -r -r'

# Generated at 2022-06-14 10:18:13.138032
# Unit test for function match
def test_match():
    assert match(Command('git rm test', 'fatal: not removing \'.travis.yml\' recursively without -r'))
    assert not match(Command('git rm test', 'fatal: command not found'))


# Generated at 2022-06-14 10:18:17.003909
# Unit test for function match
def test_match():
    assert match(Command('git rm some/dir/that/isnt/empty', ''))
    assert not match(Command('git rm', ''))


# Generated at 2022-06-14 10:18:21.898012
# Unit test for function match
def test_match():
    assert match(Command('git rm abc', '', 'abc: is a directory (not removed)', '', '', ''))
    assert not match(Command('git rebase', '', '', '', '', ''))


# Generated at 2022-06-14 10:18:34.288638
# Unit test for function match
def test_match():
    assert match(Command('git rm dsfadf', '',
                         'fatal: not removing \'dsfadf\' recursively without -r', 1))
    assert match(Command('git rm dsfadf', '',
                         'fatal: not removing \'dsfadf\' recursively without -r', 1))
    assert match(Command('git rm -r dsfadf', '',
                         'fatal: not removing \'dsfadf\' recursively without -r', 1))
    assert not match(Command('git rm -r dsfadf', '',
                         'fatal: not removing \'dsfadf\' recursively without -r', 1))

# Generated at 2022-06-14 10:18:36.828008
# Unit test for function match
def test_match():
    assert match(Command('git rm foo.txt',
            "fatal: not removing 'foo.txt' recursively without -r"))


# Generated at 2022-06-14 10:18:52.818377
# Unit test for function match
def test_match():
    command = Command('git rm -rf .')
    assert match(command) is False

    command = Command('git rm file')
    assert match(command) is False

    command = Command('git rm file',
                      stderr='fatal: not removing \'file\' recursively without -r\n')
    assert match(command) is True



# Generated at 2022-06-14 10:18:55.956469
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(
        Command('git rm file'))
    assert new_command == 'git rm -r file'

# Generated at 2022-06-14 10:18:58.826863
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file', ''))

# Generated at 2022-06-14 10:19:00.505242
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm filename') == 'git rm -r filename'

# Generated at 2022-06-14 10:19:05.460411
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r README.md',
                                   'fatal: not removing \'README.md\' recursively without -r\n',
                                   '', 0)) == 'git rm -r -r README.md'

# Generated at 2022-06-14 10:19:09.667796
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm --cached file.name', output='fatal: not removing \'file.name\' recursively without -r')
    assert get_new_command(command) == 'git rm -r --cached file.name'

# Generated at 2022-06-14 10:19:13.927928
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r file_name' == get_new_command(
        Command('git rm file_name',
                'fatal: not removing \'file_name\' recursively without -r',
                '', 1, None))

# Generated at 2022-06-14 10:19:16.174748
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file')
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:19:20.404312
# Unit test for function match
def test_match():
    assert ([('rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r')]
            == [(command, command.output) for command in filter(match, (Command('rm test.txt', ''),))])



# Generated at 2022-06-14 10:19:21.694555
# Unit test for function match
def test_match():
	assert match(Command('git rm -r src'))



# Generated at 2022-06-14 10:19:34.518774
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf folder',
    'fatal: not removing \'folder\' recursively without -r\n'))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 10:19:37.750426
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm foo')) == 'git rm -r foo'
    assert get_new_command(Command('git rm -f bar')) == 'git rm -f -r bar'

# Generated at 2022-06-14 10:19:39.605494
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r')
    assert get_new_command(command) == 'git rm -r -r'

# Generated at 2022-06-14 10:19:47.782299
# Unit test for function get_new_command
def test_get_new_command():
    # Test if return value is correct
    assert get_new_command(Command('git branch -d foo')) == 'git branch -d -r foo'
    assert get_new_command(Command('git rm foo')) == 'git rm -r foo'
    # Make sure that -r is inserted correctly, without breaking command
    assert get_new_command(Command('git branch a -d b c')) == 'git branch a -d -r b c'
    assert get_new_command(Command('git rm a b c')) == 'git rm -r a b c'

# Generated at 2022-06-14 10:20:01.616770
# Unit test for function match
def test_match():
    assert match(Command('git branch | grep \'master$\' | rm',
                         'fatal: not removing \'things/things.txt\' recursively without -r'))
    assert not match(Command('git branch | grep \'master$\' | rm', ''))
    assert not match(Command('git branch | grep \'master$\' | rm',
                             'fatal: not removing \'things/things.txt\''))
    assert not match(Command('git branch | grep \'master$\' | rm',
                             'fatal: not removing \'things/things.txt\' recursively without'))
    assert not match(Command('git branch | grep \'master$\' | rm',
                             'fatal: not removing \'things/things.txt\' recursively without -r -f'))

# Generated at 2022-06-14 10:20:04.839931
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm super_important_file', '', '')) == 'git rm -r super_important_file'

# Generated at 2022-06-14 10:20:08.137328
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm foo', 'fatal: not removing ' +
                                   "'foo' recursively without -r\n")) == \
                                   'git rm -r foo'


# Generated at 2022-06-14 10:20:12.467055
# Unit test for function match
def test_match():
    assert match(Command('git rm dir', output="fatal: not removing 'dir' recursively without -r"))
    assert not match(Command('git rm dir', output="fatal: not removing 'dir'"))
    assert not match(Command('git lg', output="fatal: not removing 'dir'"))


# Generated at 2022-06-14 10:20:17.320940
# Unit test for function match
def test_match():
    assert match(Command('git rm -r'))
    assert not match(Command('git rm -r file'))
    assert not match(Command('git rm -r file1 file2 file3'))
    assert not match(Command('git branch'))


# Generated at 2022-06-14 10:20:24.666864
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm file.txt', output="fatal: not removing 'file.txt' recursively without -r")
    new_command = get_new_command(command)
    assert new_command == 'git rm -r file.txt'

# Generated at 2022-06-14 10:20:45.306041
# Unit test for function match
def test_match():
    # Test case 1:
    command = Command('git rm -r *',
                      'fatal: not removing \'blabla.py\' recursively without -r')
    assert match(command) == True
    # Test case 2:
    command = Command('git rm blabla.py',
                      'fatal: not removing \'blabla.py\' recursively without -r')
    assert match(command) == False
    # Test case 3:
    command = Command('git rm -r *',
                      'fatal: not removing \'blabla.py\' recursively without -r')
    assert get_new_command(command) == 'git rm -r -r *'

# Generated at 2022-06-14 10:20:51.805102
# Unit test for function match
def test_match():
    command = Command('git rm README.md')
    assert match(command)
    command = Command('git rm README.md; echo $?')
    assert not match(command)
    command = Command('git rm README.md\nfatal: not removing \'README.md\' recursively without -r')
    assert match(command)
    command = Command('git rm README.md\nfatal: not removing \'README.md\' recursively without -r', '', 3)
    assert not match(command)


# Generated at 2022-06-14 10:20:59.681719
# Unit test for function match
def test_match():
    assert match(Command('git rm aDir/',
                         'fatal: not removing \'aDir/\' recursively without -r\n'))
    assert not match(Command('git rm aDir/', ''))
    

# Generated at 2022-06-14 10:21:01.781587
# Unit test for function get_new_command
def test_get_new_command():
    f = git_support(get_new_command)

    command_test = Command("git rm -r folder/",
                           ("fatal: not removing 'folder/' recursively without -r"))

    assert f(command_test) == u"git rm -r -r folder/"

# Generated at 2022-06-14 10:21:10.711294
# Unit test for function match
def test_match():
    assert match(Command(script='git rm .git',
                         output='fatal: not removing \'.git\' recursively without -r'))
    assert not match(Command(script='git', output='fatal: not removing \'.git\' recursively without -r'))
    assert not match(Command(script='git rm', output='fatal: not removing \'.git\' recursively without -r'))
    assert not match(Command(script='git rm', output='Something else'))
    assert not match(Command(script='git rm -r', output='fatal: not removing \'.git\' recursively without -r'))


# Generated at 2022-06-14 10:21:16.684387
# Unit test for function get_new_command
def test_get_new_command():
    command_script_parts = ['git', 'rm', 'README.md']
    command_output = 'fatal: not removing \'README.md\' recursively without -r'
    command = Type('git', command_script_parts, command_output)
    assert get_new_command(command) == u'git rm -r README.md'

# Generated at 2022-06-14 10:21:23.264454
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm *', output='fatal: not removing \'*\' recursively without -r')
    assert get_new_command(command) == 'git rm -r *'

# Generated at 2022-06-14 10:21:28.147833
# Unit test for function get_new_command
def test_get_new_command():
    output_1 = ("fatal: not removing 'tests/tests.py' recursively without -r")
    command_1 = Command('git rm tests/tests.py', '', output_1)
    assert get_new_command(command_1) == 'git rm -r tests/tests.py'



# Generated at 2022-06-14 10:21:33.924829
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert (get_new_command(Command(script='git rm -r abc',
                                    stderr='fatal: not removing \'abc\''
                                           ' recursively without -r\n',
                                    stdout='',
                                    env={})) == 'git rm -r -r abc')


# Generated at 2022-06-14 10:21:38.702374
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', '', output="fatal: not removing 'foo' recursively without -r"))
    assert not match(Command('git commit foo', '', output=''))
    assert not match(Command('ls rm', '', output=''))


# Generated at 2022-06-14 10:22:03.237911
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm falcon', 'error: pathspec \'falcon\' did not match any file(s) known to git.\nfatal: not removing \'falcon\' recursively without -r', '')) == 'git rm -r falcon'

# Generated at 2022-06-14 10:22:05.269828
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r 2' == get_new_command(Command('', '', '', 'rm 2'))

# Generated at 2022-06-14 10:22:08.683563
# Unit test for function match
def test_match():
    assert match(Command('git rm package.json',
                         'fatal: not removing \'package.json\' recursively without -r'))

    assert not match(Command('git rm package.json',
                         'fatal: not removing \'package.json\' recursively without -r',
                         ''))


# Generated at 2022-06-14 10:22:12.905105
# Unit test for function match

# Generated at 2022-06-14 10:22:19.814909
# Unit test for function match
def test_match():
    # Test for lowercase
    command = Command('git rm foo')
    assert match(command)
    assert not match(Command('git rm -rf foo'))
    assert not match(Command('git rm foo bar'))
    assert not match(Command('git rm'))
    assert not match(Command('git add foo'))
    assert not match(Command('git rm foo bar', 'fatal: not removing \'foo\' recursively without -r'))

# Generated at 2022-06-14 10:22:29.043980
# Unit test for function match
def test_match():
    assert match(Command('git rm -r log',
                         'fatal: not removing \'log\' recursively without -r\n'
                         'Use --cached to keep the file, or add it to your '
                         'ignore list to avoid this message.'))
    assert not match(Command('git rm file',
                             'fatal: pathspec \'file\' did not match any files'))
    assert not match(Command('git rm file', ''))


# Generated at 2022-06-14 10:22:32.549051
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test','''fatal: not removing 'test' recursively without -r
''')) == 'git rm -r test'

# Generated at 2022-06-14 10:22:36.331620
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r test', 'fatal: not removing test recursively without -r')
    assert get_new_command(command) == u'git rm -r -r test'

# Generated at 2022-06-14 10:22:39.873673
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(command=FakeCommand(script='git rm file -r', output="fatal: not removing 'file' recursively without -r"))
    assert_equal(new_command, u'git rm -r file')

# Generated at 2022-06-14 10:22:42.474550
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm a b')
    assert(get_new_command(command) == "git rm -r a b")

# Generated at 2022-06-14 10:23:04.847810
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git rm -f dir1/dir2/file2',
                                   '', '')) == 'git rm -f -r dir1/dir2/file2'

# Generated at 2022-06-14 10:23:07.549829
# Unit test for function match
def test_match():
    assert match(Command('git rm file1.txt',
                         "fatal: not removing 'file1.txt' recursively without -r"))
    assert not match(Command('git stash', ""))


# Generated at 2022-06-14 10:23:14.418215
# Unit test for function match
def test_match():
    assert match(Command('git rm file'))
    assert match(Command('git rm *.zip'))
    assert match(Command('git rm file', output='fatal: not removing \'file\' recursively without -r'))
    assert match(Command('git rm *.zip', output='fatal: not removing \'*.zip\' recursively without -r'))
    assert not match(Command('git rm file'))
    assert not match(Command('git rm file', output='fatal: not removing \'file\' recursively without -r'))


# Generated at 2022-06-14 10:23:22.284872
# Unit test for function match
def test_match():
    assert match(u'git rm foo')
    assert match(u'git rm foo/')
    assert match(u'git rm foo/file.txt')
    assert match(u'git rm foo/file.txt another_file.txt')
    assert match(u'git rm foo/file.txt another_file.txt more_files/')
    assert match(u'git rm foo/file.txt another_file.txt more_files/another_file.txt')

    assert not match(u'git add foo')
    assert not match(u'git commit foo')
    assert not match(u'git commit foo/')
    assert not match(u'git checkout foo')
    assert not match(u'git branch foo')
    assert not match(u'git checkout foo/')
    assert not match(u'git branch foo/')
   

# Generated at 2022-06-14 10:23:25.704362
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git rm file',
        'fatal: not removing \'file\' recursively without -r\n'))
        == 'git rm -r file')

# Generated at 2022-06-14 10:23:29.242109
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm /path/to')) == \
           u'git rm -r /path/to'
    assert get_new_command(Command('git rm /path/to')) == \
           u'git rm -r /path/to'

# Generated at 2022-06-14 10:23:32.630602
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -f file')
    command.output = 'fatal: not removing \'file\' recursively without -r'
    assert 'git rm -r -f file' in get_new_command(command)

# Generated at 2022-06-14 10:23:35.500303
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm -f ./file_path")
    assert(get_new_command(command) == "git rm -rf -f ./file_path")

# Generated at 2022-06-14 10:23:43.903588
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf',
        stderr='fatal: not removing \'app/assets/javascripts/.keep\' recursively without -r\n'))
    assert match(Command('git rm -rf',
        stderr='fatal: not removing \'app/assets/javascripts/.keep\' recursively without -r'))
    assert not match(Command('git rm -rf',
        stderr='fatal: not removing without -r'))

# Test get_new_command

# Generated at 2022-06-14 10:23:46.964855
# Unit test for function match
def test_match():
    assert match(Command('git rm test',
                         output="""fatal: not removing 'test' recursively without -r
usage: git rm [--cached] [--ignore-unmatch] [--] <file>..."""))

