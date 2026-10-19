

# Generated at 2022-06-14 10:13:56.486021
# Unit test for function match
def test_match():
    assert match(Command('git rm file'))
    assert not match(Command('git rm -r file'))
    assert not match(Command('git commit -m msg'))



# Generated at 2022-06-14 10:14:00.691877
# Unit test for function get_new_command
def test_get_new_command():
    test_command = Command(u'git rm -r tests/git-rm-r/dir', u'')
    assert get_new_command(test_command) == u'git rm -r tests/git-rm-r/dir'

# Generated at 2022-06-14 10:14:06.657686
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ["rm", "stash-msg-1291575366.txt", "^", "stash@{49}"]
    index = command_parts.index('rm') + 1
    command_parts.insert(index, '-r')
    assert u' '.join(command_parts) == "rm -r stash-msg-1291575366.txt ^ stash@{49}"

# Generated at 2022-06-14 10:14:13.619677
# Unit test for function get_new_command
def test_get_new_command():
    command_1 = Command('git rm -rf --cached .vim',
                         'fatal: not removing \'.vim\' recursively without -r')
    assert get_new_command(command_1) == 'git rm -rf -r --cached .vim'

    command_2 = Command('git rm --cached .vim',
                         'fatal: not removing \'.vim\' recursively without -r')
    assert get_new_command(command_2) == 'git rm -r --cached .vim'

# Generated at 2022-06-14 10:14:16.311500
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                 'fatal: not removing \'file\' recursively without -r\n',
                 '', 3))



# Generated at 2022-06-14 10:14:20.743895
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm hello')) == 'git rm -r hello'
    assert get_new_command(Command('git rm -r hello')) == 'git rm -r -r hello'

# Generated at 2022-06-14 10:14:30.715459
# Unit test for function get_new_command
def test_get_new_command(): 
    assert get_new_command('git rm -r *!') == 'git rm -r -r *!'
    assert get_new_command('git rm -r *') == 'git rm -r -r'
    assert get_new_command('git rm -r *.pyc') == 'git rm -r -r *.pyc'
    assert get_new_command('git rm -r *.pyc!') == 'git rm -r -r *.pyc!'
    assert get_new_command('git rm -r *.pyc !') == 'git rm -r -r *.pyc'
    assert get_new_command('git rm -r *.pyc *') == 'git rm -r -r *.pyc'

# Generated at 2022-06-14 10:14:33.116051
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm /some/file') == 'git rm -r /some/file'

# Generated at 2022-06-14 10:14:37.462152
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git rm test',
                                   'fatal: not removing \'test\' recursively without -r\n',
                                   'git rm test')) == 'git rm -r test'

# Generated at 2022-06-14 10:14:41.846871
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm_r import git_support
    command = Command('git rm directory', '')
    assert match(command)
    assert git_support is not None
    assert get_new_command(command) == 'git rm -r directory'

# Generated at 2022-06-14 10:14:46.377692
# Unit test for function get_new_command
def test_get_new_command():
    command_test = Command('git rm "nome"', 'fatal: not removing \'nome\' recursively without -r')
    assert get_new_command(command_test) == 'git rm -r "nome"'

# Generated at 2022-06-14 10:14:50.051761
# Unit test for function get_new_command
def test_get_new_command():
    command = Command.from_raw('git rm myfolder')
    command.output = "fatal: not removing 'myfolder' recursively without -r"
    assert get_new_command(command) == 'git rm -r myfolder'

# Generated at 2022-06-14 10:15:00.693728
# Unit test for function get_new_command
def test_get_new_command():
    test_cases = [
        (u'rm .gitignore', u'git rm -r .gitignore'),
        (u'rm --cached .gitignore', u'git rm -r --cached .gitignore')
    ]
    for command, new_command in test_cases:
        command = Command(command, u"fatal: not removing 'test_file' recursively without -r")
        assert get_new_command(command) == new_command

# Generated at 2022-06-14 10:15:08.055881
# Unit test for function match
def test_match():
    assert match(Command('git rm file', '', '', '', None, None))
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r',
                         '', '', None, None))
    assert not match(Command('git rm file', '', '', '', None, None))
    assert not match(Command('git rm file', '', '', '', None, None))


# Generated at 2022-06-14 10:15:18.042064
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file', ''))
    assert not match(Command('git rm file', 'fatal: not removing not \'file\' recursively without -r\n'))
    assert not match(Command('git rm file', 'fatal: not removing file recursively with -r\n'))
    assert not match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r\n', '', 3))


# Generated at 2022-06-14 10:15:20.136600
# Unit test for function match
def test_match():
    assert match(Command('git rm foo/', ''))

# Generated at 2022-06-14 10:15:23.026448
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -f file.txt', output='fatal: not removing \'file.txt\' recursively without -r')) == 'git rm -f -r file.txt'

# Generated at 2022-06-14 10:15:26.215088
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(u'rm foo bar') == u'rm -r foo bar'

# Generated at 2022-06-14 10:15:34.318588
# Unit test for function match
def test_match():
    assert match(Command('git rm -r a',
                   'fatal: not removing \'a\' recursively without -r'))
    assert not match(Command('git rm -r a b',
                             'fatal: not removing \'a\' recursively without -r'))
    assert not match(Command('git rm -r a', 'fatal: not removing \'a\''))
    assert not match(Command('git rm -r a', 'fatal: not removing recursively without -r'))


# Generated at 2022-06-14 10:15:39.332945
# Unit test for function match
def test_match():
    assert match(Command('rm -rf file', 'fatal: not removing \'./file\' recursively without -r'))
    assert not match(Command('git rm -rf file', 'fatal: not removing \'./file\' recursively without -r'))
    assert not match(Command('rm -rf file', 'file.txt'))


# Generated at 2022-06-14 10:15:52.301074
# Unit test for function match
def test_match():
    assert match(command = mock.Mock(script = 'git rm --cached -r directory', output = 'fatal: not removing \'directory\' recursively without -r')) == True
    assert match(command = mock.Mock(script = 'git rm -r directory', output = 'fatal: not removing \'directory\' recursively without -r')) == False
    assert match(command = mock.Mock(script = 'git rm -r directory', output = 'fatal: not removing \'directory\' recursively without -r')) == False
    assert match(command = mock.Mock(script = 'git rm -r .', output = 'fatal: not removing \'.\' recursively without -r')) == True

# Generated at 2022-06-14 10:15:58.272788
# Unit test for function match
def test_match():
	assert match(Command("git rm dir", "fatal: not removing 'dir' recursively without -r"))
	assert not match(Command(" ...", "fatal: not removing 'dir' recursively without -r"))
	assert not match(Command(" git rm dir", "fatal: not removing 'dir' recursively without -r"))


# Generated at 2022-06-14 10:16:04.552708
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -rf folder/file', 'fatal: not removing \'folder/file\' recursively without -r')
    assert get_new_command(command) == 'git rm -rf -r folder/file'

    command = Command('git rm file', 'fatal: not removing \'file\' recursively without -r')
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:16:12.022011
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'foo\' recursively without -r'))
    assert match(Command('git rm foo/',
                         'fatal: not removing \'foo/\' recursively without -r'))
    assert not match(Command('git rm foo', ''))
    assert not match(Command('git rm foo', 'fatal: pathspec \'foo\' did not match any files'))
    assert not match(Command('git rm foo', 'fatal: pathspec \'foo\' did not match any files'))


# Generated at 2022-06-14 10:16:14.501464
# Unit test for function match
def test_match():
    assert match(Script("git rm file_name"))
    assert not match(Script("git rm directory_name"))

# Generated at 2022-06-14 10:16:23.734649
# Unit test for function match
def test_match():
    command = Command.from_string("git rm -f bar",  "")
    assert git_rm_recursive.match(command)
    command = Command.from_string("git rm -f bar",  "fatal: not removing 'bar' recursively without -r")
    assert git_rm_recursive.match(command)
    command = Command.from_string("git rm -f bar",  "fatal: not removing 'bar' recursively without -r")
    assert git_rm_recursive.match(command)
    command = Command.from_string("git rm -f bar",  "")
    assert not git_rm_recursive.match(command)
    command = Command.from_string("rm -f bar",  "")
    assert not git_rm_recursive.match(command)


# Generated at 2022-06-14 10:16:26.624955
# Unit test for function match
def test_match():
	command = Command('git rm README.md', 'fatal: not removing \'README.md\' recursively without -r')
	assert match(command)


# Generated at 2022-06-14 10:16:32.042460
# Unit test for function match
def test_match():
    assert match(Command(script='git rm test', output='fatal: not removing'
                         ' \'test\' recursively without -r'))
    assert not match(Command(script='git rm -r', output='fatal: not removing'
                             ' \'test\' recursively without -r'))

# Generated at 2022-06-14 10:16:41.875222
# Unit test for function match
def test_match():
    assert match(Command(script = "git rm test.py", output = "fatal: not removing 'test.py' recursively without -r"))
    assert match(Command(script = "git rm  test.py", output = "fatal: not removing 'test.py' recursively without -r"))
    assert match(Command(script = "git rm -r test.py", output = "fatal: not removing 'test.py' recursively without -r"))
    assert not match(Command(script = "git rm test.py", output = "fatal: not removing 'test.py' recursively with -r"))



# Generated at 2022-06-14 10:16:45.370178
# Unit test for function match
def test_match():
    assert match(Command('git rm folder', 'fatal: not removing \'folder\' recursively without -r'))
    assert not match(Command('git rm folder', 'error: bad'))


# Generated at 2022-06-14 10:16:51.898854
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r .')) == u'git rm -r .'

# Generated at 2022-06-14 10:16:56.846636
# Unit test for function match
def test_match():
    third_command = 'git rm file'
    result = match(Command(script=third_command,
                           output="fatal: not removing 'file' recursively without -r"))
    assert result == True


#Unit test for function get_new_command

# Generated at 2022-06-14 10:17:01.314291
# Unit test for function get_new_command
def test_get_new_command():
    # Create a Command object to test get_new_command
    command = Command('git rm -f',
                      'fatal: not removing \'asdfasdf\' recursively without -r')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r -f'

# Generated at 2022-06-14 10:17:10.502835
# Unit test for function match
def test_match():
    assert match(Command('git rm filename', 
        'fatal: not removing \'filename\' recursively without -r\n'))
    assert match(Command('git add filename', 
        'fatal: not removing \'filename\' recursively without -r\n'))
    assert not match(Command('git rm filename', 
        'fatal: not removing \'filename\' recursively with -r\n'))
    assert not match(Command('git add filename', 
        'fatal: not removing \'filename\' recursively with -r\n'))


# Generated at 2022-06-14 10:17:14.290392
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ['git', 'rm', '-r', 'src']
    command = Command(u' '.join(command_parts), command_parts)
    get_new_command(command)

# Generated at 2022-06-14 10:17:18.207145
# Unit test for function get_new_command
def test_get_new_command():
    old_command = 'git rm -rf'
    output = "fatal: not removing '.' recursively without -r"
    command = Command(old_command, output)
    assert get_new_command(command) == 'git rm -rf -r'

# Generated at 2022-06-14 10:17:25.878991
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command(script='git branch',
                             stderr='fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command(script='git rm file.txt',
                             stderr='fatal: not removing \'file.txt\' recursively'))


# Generated at 2022-06-14 10:17:28.722725
# Unit test for function match
def test_match():
    assert_true(match(Command(script='git rm test.txt',
                              output="fatal: not removing 'test.txt' recursively without -r")))


# Generated at 2022-06-14 10:17:38.639377
# Unit test for function match
def test_match():
    assert match(Command('git rm test', 'fatal: not removing \'test\' recursively without -r'))
    assert match(Command('git rm test', "fatal: not removing 'test' recursively without -r"))
    assert not match(Command('git rm test', 'fatal: not removing \'test\' recursively with -r'))
    assert not match(Command('git rm test', 'fatal: not removing \'test\' recursively'))
    assert not match(Command('apt rm test', 'fatal: not removing \'test\' recursively without -r'))


# Generated at 2022-06-14 10:17:41.760002
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r')
    assert match(command)
    assert get_new_command(command) == 'git rm -r'

# Generated at 2022-06-14 10:17:49.023420
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r')) == 'git rm -r -r'

# Generated at 2022-06-14 10:17:51.930880
# Unit test for function get_new_command
def test_get_new_command():
    match = Command('git rm file', 'fatal: not removing \'file\' recursively without -r\n')
    assert get_new_command(match) == "git rm -r file"

# Generated at 2022-06-14 10:17:57.889031
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r .'
            , 'fatal: not removing \'.\' recursively without -r'
            , 'git rm -r .; exit 1')
    assert get_new_command(command) == 'git rm -r -r .'

    command = Command('git status; git rm -r .'
            , 'fatal: not removing \'.\' recursively without -r'
            , 'git status; git rm -r .; exit 1')
    assert get_new_command(command) == 'git status; git rm -r -r .'

# Generated at 2022-06-14 10:18:09.099265
# Unit test for function get_new_command
def test_get_new_command():
    assert('git rm another_test.txt' == get_new_command(Command(script='git rm another_test.txt', 
    stdout='fatal: not removing \'another_test.txt\' recursively without -r')).script)
    assert('git rm -r a_test.txt' == get_new_command(Command(script='git rm a_test.txt', 
    stdout='fatal: not removing \'a_test.txt\' recursively without -r')).script)
    assert('git rm --cached a_test.txt' == get_new_command(Command(script='git rm --cached a_test.txt', 
    stdout='fatal: not removing \'a_test.txt\' recursively without -r')).script)

# Generated at 2022-06-14 10:18:13.947314
# Unit test for function match
def test_match():
    assert match(Command('git rm file_name', 'fatal: not removing \'file_name\' recursively without -r\n'))
    assert not match(Command('git rm file_name', 'fatal: not removing \'file_name\' recursively without -r'))


# Generated at 2022-06-14 10:18:22.600719
# Unit test for function match
def test_match():
    assert(match(Command('git status',
                                 'fatal: not removing \'a\' recursively without -r'))
           is True)
    assert(match(Command('git status',
                                 'fatal: not removing \'a\' recursively without -n'))
           is False)
    assert(match(Command('git rm a',
                                 'fatal: not removing \'a\' recursively without -r'))
           is False)


# Generated at 2022-06-14 10:18:30.502855
# Unit test for function match
def test_match():
  # Create Command object
  # Set script to the command, command.output to the output of the command
  command = Command("git rm my_file.txt", "\
  fatal: not removing 'my_file.txt' recursively without -r")
  assert match(command) is True
  
  # Wrong command
  command = Command("git rm my_file.txt", "")
  assert match(command) is False


# Generated at 2022-06-14 10:18:32.796942
# Unit test for function match
def test_match():
    assert match(Command('git rm test',
                         "fatal: not removing 'test' recursively without -r", 0))

# Generated at 2022-06-14 10:18:39.947844
# Unit test for function match
def test_match():
    assert match(Command('rm README.md ', 'fatal: not removing README.md recursively without -r', ''))
    assert not match(Command('rm README.md', '', ''))
    assert not match(Command(' rm README.md', 'fatal: not removing README.md recursively', ''))
    assert not match(Command(' rm README.md', 'fatal: not removing README.md recursively without -r', ''))


# Generated at 2022-06-14 10:18:42.265701
# Unit test for function match
def test_match():
	assert match(u'git rm test')
	assert not match(u'git rm -r test')

# Generated at 2022-06-14 10:18:55.574394
# Unit test for function match
def test_match():
    command = Command("git rm foo.bar",
                      "fatal: not removing 'foo.bar' recursively without -r")
    assert match(command)



# Generated at 2022-06-14 10:19:00.311951
# Unit test for function match
def test_match():
    assert match(Command(script='git rm file',
                        output='fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command(script='git rm file',
                        output='fatal: not removing \'file\' recursively without -r\n'))


# Generated at 2022-06-14 10:19:02.885571
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test.c')
    assert get_new_command(command) == 'git rm -r test.c'

# Generated at 2022-06-14 10:19:05.882520
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    command = Command('git rm file')
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:19:13.132099
# Unit test for function match
def test_match():
    assert not match(Command('git commit', ''))
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', ''))
    assert not match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r\n'))
    assert match(Command('git rm -rf file', 'fatal: not removing \'file\' recursively without -r'))


# Generated at 2022-06-14 10:19:21.130635
# Unit test for function match
def test_match():
    assert match(Command('git rm woohoo', '', 'fatal: not removing \'woohoo\' recursively without -r'))
    assert not match(Command('git rm woohoo', '', ''))
    assert not match(Command('git rm blah', '', 'fatal: not removing \'woohoo\' recursively without -r'))
    assert not match(Command('git rm woohoo', '', 'fatal: not removing \'woohoo\' recursively without -r\nfatal: not removing \'woohoo\' recursively without -r'))


# Generated at 2022-06-14 10:19:23.925179
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git status', output='fatal: not removing \'myfile\' recursively without -r')
    assert get_new_command(command) == u'git rm -r myfile'

# Generated at 2022-06-14 10:19:27.146207
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm remote') == 'git rm -r remote'
    assert get_new_command('git rm remote') == 'git rm -r remote'

# Generated at 2022-06-14 10:19:28.767803
# Unit test for function match
def test_match():
    assert match(Command("git rm test.txt", "fatal: not removing 'test.txt' recursively without -r"))


# Generated at 2022-06-14 10:19:32.205085
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf',
                         stderr= """fatal: not removing 'src/app.ts' recursively 
                                    without -r""")
                         )


# Generated at 2022-06-14 10:19:46.130424
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm -rf a.txt", "fatal: not removing 'a.txt' recursively without -r")
    assert_equals(get_new_command(command), "git rm -rf -r a.txt")

# Generated at 2022-06-14 10:19:53.225447
# Unit test for function match
def test_match():
    command = Command('git rm -rf', "fatal: not removing 'build' recursively without -r\n")
    assert(match(command))


# Generated at 2022-06-14 10:20:05.176743
# Unit test for function match
def test_match():
    command_true = Command('git rm -r *', '', 'fatal: not removing \'*\' recursively without -r\n')
    command_false = Command('git', '', 'fatal: not removing \'*\' recursively without -r\n')
    assert match(command_true) == True
    assert match(command_false) == False


# Generated at 2022-06-14 10:20:09.378522
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(' git rm -rf --cached path/a',
                      'fatal: not removing \'path/a\' recursively without -r')
    assert_equals(get_new_command(command), 'git rm -rf -r --cached path/a')

# Generated at 2022-06-14 10:20:13.341006
# Unit test for function match
def test_match():
    output = "fatal: not removing 'dir1' recursively without -r"
    script = 'git rm dir1'
    command = Command(script, output)
    assert match(command)


# Generated at 2022-06-14 10:20:19.060199
# Unit test for function match
def test_match():
    assert match(Command('git rm filename',
                         'fatal: not removing \'filename\' recursively without -r'))
    assert not match(Command('git rm filename', 'rm: xzy: No such file or directory'))
    assert not match(Command('git rm filename', ''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 10:20:23.268933
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(ShellCommand('git rm -r abc/', '', '')) == 'git rm -r abc/'



# Generated at 2022-06-14 10:20:28.603191
# Unit test for function match
def test_match():
    assert match(Command('git rm foo.txt', 'fatal: not removing \'foo.txt\' recursively without -r'))
    assert not match(Command('git rm foo.txt', 'foo.txt'))
    assert not match(Command('ls foo.txt', 'fatal: not removing \'foo.txt\' recursively without -r'))

# Generated at 2022-06-14 10:20:32.017842
# Unit test for function match
def test_match():
    test_command = Command(script='rm  file', output='fatal: not removing \'file\' recursively without -r')
    assert match(test_command)


# Generated at 2022-06-14 10:20:33.679357
# Unit test for function match
def test_match():
    assert match(Command(' rm src/test.py'))


# Generated at 2022-06-14 10:20:49.749241
# Unit test for function match
def test_match():
    script = 'git rm'
    output = 'fatal: not removing \'build/\' recursively without -r'
    assert match(Command(script, output)) == True

# Generated at 2022-06-14 10:20:56.991334
# Unit test for function get_new_command
def test_get_new_command():
    command = GitCommand(script='git rm file',
                         stdout='fatal: not removing \'file\' recursively without -r')
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:21:00.582185
# Unit test for function match
def test_match():
    assert match(Command('git rm -r bar.txt',
                         "fatal: not removing 'foo/bar.txt' recursively without -r\n"))
    asser

# Generated at 2022-06-14 10:21:07.496672
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm_not_removing_recursive_without_r import get_new_command
    assert get_new_command('git rm file') == 'git rm -r file'
    assert get_new_command('git rm -f file') == 'git rm -r -f file'
    assert get_new_command('git rm file1 file2') == 'git rm -r file1 file2'

# Generated at 2022-06-14 10:21:10.469658
# Unit test for function match
def test_match():
    assert match(Command('git rm Resources',
        'fatal: not removing \'Resources\' recursively without -r\n'))
    assert not match(Command('ls'))
    assert not match(Command('ls Resources', '', ''))
    assert not match(Command('git rm',
        'fatal: not removing \'Resources\' recursively without -r\n'))


# Generated at 2022-06-14 10:21:16.906400
# Unit test for function match
def test_match():
	# Test 1
	command = Command('git rm -r *', 'fatal: not removing \'\' recursively without -r\n')
	
	assert(match(command) == True)
	
	# Test 2
	command = Command('git rm -r *', 'fatal: not removing \'\' recursively without -r\n')
	
	assert(match(command) == True)


# Generated at 2022-06-14 10:21:21.858623
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf  Test', '')) == 'git rm -r Test'

# Generated at 2022-06-14 10:21:28.588434
# Unit test for function match
def test_match():
    assert match(Command('git rm test',
        "fatal: not removing 'test' recursively without -r"))
    assert match(Command('git branch | grep "*"', "* master")) is None
    assert match(Command('git rm test',
        "fatal: not removing 'test' recursively without -r"))
    assert match(Command('git branch | grep "*"', "* master")) is None


# Generated at 2022-06-14 10:21:31.512502
# Unit test for function match
def test_match():
	command = Command('git rm -rf foo', 'fatal: not removing \'foo\' recursively without -r')
	print(match(command))

# Generated at 2022-06-14 10:21:35.027478
# Unit test for function get_new_command
def test_get_new_command():
    script = 'rm -rf'
    output = "fatal: not removing ' .' recursively without -r"
    command = Command(script, output)
    assert get_new_command(command) == 'rm -rf -r'

# Generated at 2022-06-14 10:22:00.726164
# Unit test for function match
def test_match():
    assert match(Command(script='git rm -rf build',
                                           output='fatal: not removing \'build\' recursively without -r'))
    assert not match(Command(script='git rm -rf build',
                                           output='fatal: not found: \'build\''))
    assert not match(Command(script='rm -rf build',
                                           output=None))

# Generated at 2022-06-14 10:22:07.073392
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
        u"fatal: not removing 'foo' recursively without -r\n", ''))
    assert not match(Command('git rm foo',
        u"fatal: not removing dir recursively without -r\n", ''))
    assert not match(Command('git rm foo', '', ''))



# Generated at 2022-06-14 10:22:16.145628
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ['git', 'rm', '--cached', '"C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\VC\\INCLUDE\\crtdefs.h"']
    index = command_parts.index('rm') + 1
    command_parts.insert(index, '-r')
    assert u' '.join(command_parts) == 'git rm -r --cached "C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\VC\\INCLUDE\\crtdefs.h"'

# Generated at 2022-06-14 10:22:18.106840
# Unit test for function match
def test_match():
    assert match(Command('rm -rf folder'))
    assert not match(Command('git stash'))

# Generated at 2022-06-14 10:22:24.563940
# Unit test for function get_new_command
def test_get_new_command():
    script = "git rm -r test.py"
    output = """To /home/user/example
 ! [rejected]        6c5a5e5..3b84cd5  test -> test (non-fast-forward)
error: failed to push some refs to '/home/user/example'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
hint: before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
"""
    command = Command(script, output)
    assert get_new_command(command) == "git pull"

# Generated at 2022-06-14 10:22:29.810000
# Unit test for function get_new_command
def test_get_new_command():
    output = '''fatal: not removing 'dir' recursively without -r'''
    cmd = Command(script='git rm dir', output=output)
    new_cmd = get_new_command(cmd)
    assert new_cmd == "git rm -r dir"

# Generated at 2022-06-14 10:22:33.855479
# Unit test for function get_new_command
def test_get_new_command():
    rules = GitRule()
    command = Command('rm *', 'fatal: not removing "*" recursively without -r')
    assert 'git rm -r *' == rules.get_new_command(command)

# Generated at 2022-06-14 10:22:36.242092
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git rm test') == 'git rm -r test'
	assert get_new_command('git rm test folder') == 'git rm -r test folder'

# Generated at 2022-06-14 10:22:42.586204
# Unit test for function match
def test_match():
    match_output = 'fatal: not removing \'lib/python2.7/site-packages/requests/packages/urllib3/packages/ssl_match_hostname/__init__.py\' recursively without -r\n'
    command = Command('rm lib/python2.7/site-packages/requests/packages/urllib3/packages/ssl_match_hostname/', match_output)
    assert(match(command))

    match_output2 = 'fatal: not removing \'lib/python2.7/site-packages/requests/packages/urllib3/packages/ssl_match_hostname/__init__.py\' recursively without -r\n'

# Generated at 2022-06-14 10:22:46.213572
# Unit test for function match
def test_match():
    assert match(Command('rm A', 'fatal: not removing \'A\' recursively without -r'))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 10:23:34.131568
# Unit test for function match
def test_match():
    assert match(Command('rm -r file.txt', 'ERROR: file.txt: is a directory\nfatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command('rm file.txt', 'fatal: not removing \'file.txt\' recursively without -r'))


# Generated at 2022-06-14 10:23:38.663065
# Unit test for function match
def test_match():
    assert match(Command('git rm a',
                         "fatal: not removing 'a' recursively without -r",
                         None))
    assert not match(Command('git rm a',
                             "fatal: not removing 'a' recursively without -r",
                             None))

# Generated at 2022-06-14 10:23:45.388503
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm test1/test2/test4 test3/test4',
                                   'fatal: not removing \'test1/test2/test4/test5\' recursively without -r\n'
                                   'git rm test1/test2/test4 test3/test4')) == 'git rm -r test1/test2/test4 test3/test4'


# Generated at 2022-06-14 10:23:53.856298
# Unit test for function match
def test_match():
    # the function returns False if the git command was not used
    assert not match(Command('ls -l'))    
    
    # Check if match function works
    assert not match(Command('git add .', 'error: pathspec '))
    
    # Check if match function works
    assert not match(Command('git test', 'fatal: not removing '))
    
    # Check if match function works
    assert not match(Command('git test', "fatal: not removing '"))
    
    # Check if match function works
    assert match(Command('git rm test', 'fatal: not removing '))