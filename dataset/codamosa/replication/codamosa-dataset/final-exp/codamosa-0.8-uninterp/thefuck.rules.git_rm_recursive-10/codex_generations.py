

# Generated at 2022-06-14 10:14:00.802015
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r')
    assert get_new_command(command) == 'git rm -r foo'

# Generated at 2022-06-14 10:14:03.981015
# Unit test for function match
def test_match():
    assert match(Command('git rm -r <file>', stderr='fatal: not removing '
                         "'<file>' recursively without -r"))


# Generated at 2022-06-14 10:14:08.462733
# Unit test for function match
def test_match():
	#not match
	assert match(Command('git status', '', '')) == False
	#match
	assert match(Command('git rm', '', 'fatal: not removing \'bla.txt\' recursively without -r')) == True


# Generated at 2022-06-14 10:14:11.455757
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm', 'fatal: not removing \'file.txt\' recursively without -r')
    assert get_new_command(command) == 'git rm -r'

# Generated at 2022-06-14 10:14:14.315222
# Unit test for function match
def test_match():
    git = Command('git rm -rf',
                  "fatal: not removing '?' recursively without -r")
    assert match(git)
    git2 = Command('git rm',
                   'fatal: not removing ')
    assert not match(git2)

# Generated at 2022-06-14 10:14:16.346400
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r')
    assert get_new_command(command) == 'git rm -r -r'

# Generated at 2022-06-14 10:14:29.546799
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm -rf foo")).script == "git rm -rf -r foo"
    assert get_new_command(Command("git rm -rf foo bar")).script == "git rm -rf -r foo bar"
    assert get_new_command(Command("git rm -rf foo/bar")).script == "git rm -rf -r foo/bar"
    assert get_new_command(Command("git rm -rf foo/bar --cached")).script == "git rm -rf -r foo/bar --cached"
    assert get_new_command(Command("git rm -rf foo/bar --force")).script == "git rm -rf -r foo/bar --force"

# Generated at 2022-06-14 10:14:33.236167
# Unit test for function get_new_command

# Generated at 2022-06-14 10:14:38.980199
# Unit test for function get_new_command
def test_get_new_command():
    old_command = u'git rm -rf *'
    old_output = "fatal: not removing 'src/' recursively without -r"
    command = Command(old_command, old_output)

    new_command = get_new_command(command)

    assert new_command == u'git rm -rf -r *'

# Generated at 2022-06-14 10:14:46.080646
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         """fatal: not removing 'path/to/something' recursively without -r""",
                         ''))
    assert not match(Command('git status',
                             """'path/to/something' recursively without -r""",
                             ''))
    assert not match(Command('git status',
                             """fatal: not removing 'path/to/something'""",
                             ''))


# Generated at 2022-06-14 10:14:55.344645
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git rm file1 file2'
    new_command = get_new_command(Command(command, '', ''))
    assert 'git rm -r file1 file2' == new_command

# Generated at 2022-06-14 10:15:01.420668
# Unit test for function match
def test_match():
    assert match(Command('git rm file1 file2', '', '', 1, 3))
    assert not match(Command('git commit file1 file2', '', '', 1, 3))
    assert not match(Command('git rm file1 file2', '', '', 0, 1))


# Generated at 2022-06-14 10:15:07.923943
# Unit test for function match
def test_match():
    output = dedent("""
    error: The following untracked working tree files would be overwritten by merge:
            README.md
    Please move or remove them before you can merge.
    Aborting
    fatal: not removing 'README.md' recursively without -r""")
    assert match(Command('git rm README.md', output=output))


# Generated at 2022-06-14 10:15:09.618921
# Unit test for function get_new_command
def test_get_new_command():
    assert "git rm -r" in get_new_command(Command('git rm'))

# Generated at 2022-06-14 10:15:11.747398
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file')
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:15:16.210244
# Unit test for function get_new_command
def test_get_new_command():
    from mock import Mock
    command = Mock(script="git rm test", script_parts=["git", "rm", "test"],
                   output="fatal: not removing 'test' recursively without -r")
    assert get_new_command(command) == "git rm -r test"

# Generated at 2022-06-14 10:15:18.826296
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command({'script': 'rm test', 'output': "fatal: not removing 'test' recursively without -r"}) == u'git rm -r test'

# Generated at 2022-06-14 10:15:21.760281
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm foo',
                                   'fatal: not removing \'foo\' '
                                   'recursively without -r')) \
        == u'git rm -r foo'

# Generated at 2022-06-14 10:15:33.236506
# Unit test for function match
def test_match():
    assert match(Command('git branch test'))
    assert match(Command('git branch test', 'fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command('git checkout test'))
    assert not match(Command('git checkout test', 'fatal: Not a git repository (or any of the parent directories): .git'))

# To run unit tests,
#
#  $ python -m pytest test_git.py
#
# or
#
#  $ python -m pytest -v test_git.py
#
# will print more details.
if __name__ == '__main__':
    test_match()

# Generated at 2022-06-14 10:15:38.433549
# Unit test for function match
def test_match():
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file', '', 'fatal: not removing \'file2\' recursively without -r\n'))
    assert not match(Command('git checkout file', '', 'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm \'foo bar\'', '', 'fatal: not removing \'foo bar\' recursively without -r\n'))



# Generated at 2022-06-14 10:15:45.774119
# Unit test for function match
def test_match():
    assert match(Command('git rm test'))
    assert match(Command('git rm -rf test'))



# Generated at 2022-06-14 10:15:48.392850
# Unit test for function match
def test_match():
    assert match(Command('rm -rf foo bar', 'fatal: not removing \'foo/bar\' recursively without -r'))


# Generated at 2022-06-14 10:15:53.453878
# Unit test for function get_new_command
def test_get_new_command():
    git_rm_r_fatal = Command('git rm somedir', '/dev/null', 'fatal: not removing \'somedir\' recursively without -r\n', 0)
    assert get_new_command(git_rm_r_fatal) == 'git rm -r somedir'

# Generated at 2022-06-14 10:16:00.605039
# Unit test for function get_new_command
def test_get_new_command():
    # We need to set command instead of script
    # because the function needs access to command.output
    command = Command('git rm -rf .', '')
    assert(get_new_command(command) == 'git rm -rf -r .')
    command = Command('git rm -rf subfolder', '')
    assert(get_new_command(command) == 'git rm -rf -r subfolder')

# Generated at 2022-06-14 10:16:05.529356
# Unit test for function get_new_command
def test_get_new_command():
    assert u'git rm -r file' == get_new_command(Command(script='git rm file',
                                                        output='fatal: not removing \'file\' recursively without -r',
                                                        stderr='fatal: not removing \'file\' recursively without -r'))


# Generated at 2022-06-14 10:16:08.842210
# Unit test for function match
def test_match():
    assert match(Command('git rm -r dir/',
                 'fatal: not removing \'dir/\' recursively without -r'))
    assert not match(Command('git status'))



# Generated at 2022-06-14 10:16:11.076087
# Unit test for function get_new_command
def test_get_new_command():
  command = Command('git rm -r x')
  assert 'git rm -r -r x' == get_new_command(command)

# Generated at 2022-06-14 10:16:14.148316
# Unit test for function get_new_command
def test_get_new_command():
	assert 'git rm -r .' == get_new_command(Command('git rm .', 'fatal: not removing \'\' recursively without -r'))

# Generated at 2022-06-14 10:16:18.233661
# Unit test for function get_new_command
def test_get_new_command():
    output = 'fatal: not removing \'release/\': Directory not empty'
    command = Command(script='git rm release/',
                      output=output)
    assert get_new_command(command) == 'git rm -r release/'

# Generated at 2022-06-14 10:16:25.405122
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm tpl') == 'git rm -r tpl'
    assert get_new_command('git rm -f tpl') == 'git rm -f -r tpl'
    assert get_new_command('git rm -rf tpl') == 'git rm -rf tpl'
    assert get_new_command('git rm -r tpl') == 'git rm -r tpl'

# Generated at 2022-06-14 10:16:31.845526
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', ''))
    assert not match(Command('git init', ''))

# Generated at 2022-06-14 10:16:33.202298
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm -f directory") == "git rm -rf directory"

# Generated at 2022-06-14 10:16:39.315302
# Unit test for function match
def test_match():
    # Tests that the match function returns True if the command begins with 'git'
    # and the output includes the following text: fatal: not removing 'foo/bar' recursively without -r
    t = 'git rm foo/bar'
    c = Command(t, 'fatal: not removing \'foo/bar\' recursively without -r\n')
    assert match(c)


# Generated at 2022-06-14 10:16:45.031169
# Unit test for function match
def test_match():
    assert match(Command('git rm file_name', 'fatal: not removing \'file_name\' recursively without -r'))
    assert not match(Command('git rm file_name'))
    assert not match(Command('git rm file_name', 'fatal: not removing \'file_name\' recursively without -r', 'fatal: not removing \'file_name\' recursively without -r'))
    assert not match(Command('git add file_name', 'fatal: not removing \'file_name\' recursively without -r'))


# Generated at 2022-06-14 10:16:51.986139
# Unit test for function match
def test_match():
    command = Command('git rm -r file.txt', None, 'fatal: not removing \'file.txt\' recursively without -r')
    assert match(command)
    command = Command('git rm file.txt', None, 'fatal: not removing \'file.txt\' recursively without -r')
    assert not match(command)
    command = Command('git rm -r file.txt', None, 'fatal: not removing \'file.txt\' without -r')
    assert match(command)


# Generated at 2022-06-14 10:16:57.521932
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm a')
    full_output = '''
    fatal: not removing 'a' recursively without -r
    '''
    new_command = get_new_command(Command('git rm a', full_output))
    assert new_command == 'git rm -r a'

# Generated at 2022-06-14 10:17:02.759220
# Unit test for function match
def test_match():
    assert match(Command("git rm -r dir/ folder/", "fatal: not removing 'dir/' recursively without -r\nwtf?\n"))
    assert not match(Command("git rm -r dir/ folder/", ""))
    assert not match(Command("git rm -r dir/ folder/", "fatal: not removing 'dir/' recursively without -r\n"))

# Generated at 2022-06-14 10:17:06.287586
# Unit test for function get_new_command
def test_get_new_command():
    assert "git rm -r a" == get_new_command(Command("git rm a", "fatal: not removing 'a' recursively without -r", ""))

# Generated at 2022-06-14 10:17:09.693220
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git rm repo',
                                    'fatal: not removing \'repo\' recursively without -r'))
            == u'git rm -r repo')

# Generated at 2022-06-14 10:17:11.676380
# Unit test for function match
def test_match():
    assert_match(match, "git rm file1 file2 file3")



# Generated at 2022-06-14 10:17:16.661302
# Unit test for function match
def test_match():
    command = Command('git rm foo/bar/baz', 'fatal: not removing \'foo/bar/baz\' recursively without -r')
    assert match(command)
    command = Command('git rm foo/bar', 'fatal: not removing \'foo/bar/baz\' recursively without -r')
    assert not match(command)


# Generated at 2022-06-14 10:17:28.550888
# Unit test for function get_new_command
def test_get_new_command():
    output = '''
    fatal: not removing 'fizz/buzz/' recursively without -r
    Did you mean this?
    You asked to pull from the remote 'fizz', but did you mean
    this?
    idk@idk.com:fizz/buzz.git
    If you still want to pull, you must set the configuration
    variable
    .git/config
    Did you mean this?
    You asked to pull from the remote 'origin', but did you mean
    this?
    idk@idk.com:fizz/buzz.git
    Did you mean this?
    You asked to pull from the remote 'fizz', but did you mean
    this?
    idk@idk.com:fizz/buzz.git
    '''

# Generated at 2022-06-14 10:17:30.683200
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm test')) == 'git rm -r test'

# Generated at 2022-06-14 10:17:44.175431
# Unit test for function match
def test_match():
    command = Command('git rm somefile', 'fatal: not removing \'somefile\' recursively without -r')
    assert match(command)

    # Ignore case
    command = Command('git Rm somefile', 'fatal: not removing \'somefile\' recursively without -r')
    assert match(command)

    command = Command('git rm --cached somefile', 'fatal: not removing \'somefile\' recursively without -r')
    assert match(command)

    command = Command('git rm somefile', 'fatal: not removing foo')
    assert not match(command)

    command = Command('git rm somefile', 'fatal: not removing foo recursively without -r')
    assert not match(command)


# Generated at 2022-06-14 10:17:53.176532
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('git rm /tmp/',
            'fatal: not removing \'/tmp/\' recursively without -r')
    print(get_new_command(cmd))
    assert get_new_command(cmd) == 'git rm -r /tmp/'
    cmd2 = Command('git rm -r /tmp/',
            'fatal: not removing \'/tmp/\' recursively without -r')
    assert get_new_command(cmd2) == cmd2.script

# Generated at 2022-06-14 10:17:55.121276
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm Hello.java', 'fatal: not removing \'Hello.java\' recursively without -r')
    assert get_new_command(command) == 'git rm -r Hello.java'

# Generated at 2022-06-14 10:17:59.820350
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', ''))
    assert not match(Command('git rm file',
                             'fatal: not removing \'file\' recursively without'))

# Generated at 2022-06-14 10:18:01.961992
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm a') == 'git rm -r a'



# Generated at 2022-06-14 10:18:06.777937
# Unit test for function match
def test_match():
    assert match(Command('git rm some_file', u'fatal: not removing \'some_file\' recursively without -r'))
    assert not match(Command('rf some_file', u''))
    assert not match(Command('./rf some_file', u''))


# Generated at 2022-06-14 10:18:09.200664
# Unit test for function match
def test_match():
    assert match(Command('git rm dir', 'fatal: not removing \'dir\' recursively without -r\n'))


# Generated at 2022-06-14 10:18:19.212964
# Unit test for function match
def test_match():
    assert match(Command('git rm "some_dir"', "fatal: not removing 'some_dir' recursively without -r"))
    assert not match(Command('git rm -r "some_dir"', ""))
    assert not match(Command('rm "some_dir"', ""))


# Generated at 2022-06-14 10:18:24.448357
# Unit test for function get_new_command
def test_get_new_command():
    curr_command = 'git rm file1 file2'
    output = 'fatal: not removing \'file1\' recursively without -r'
    com = Command(script=curr_command, output=output)
    assert get_new_command(com) == 'git rm -r file1 file2'

# Generated at 2022-06-14 10:18:28.820476
# Unit test for function match
def test_match():
    assert match(Command('git rm it',
                         "fatal: not removing 'it' recursively without -r"))
    assert not match(Command('git rm it', ''))


# Generated at 2022-06-14 10:18:31.506270
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm foo', '')) == 'git rm -r foo'


enabled_by_default = True

# Generated at 2022-06-14 10:18:34.176408
# Unit test for function match
def test_match():
    assert match(Command("git rm -r file.txt",
                         "fatal: not removing 'file.txt' recursively without -r"))


# Generated at 2022-06-14 10:18:36.709327
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm file")
    assert get_new_command(command) == "git rm -r file"



# Generated at 2022-06-14 10:18:41.091208
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file')
    assert get_new_command(command) == 'git rm -r file'
    command = Command('git rm directory')
    assert get_new_command(command) == 'git rm -r directory'

# Generated at 2022-06-14 10:18:45.388772
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r')
    assert get_new_command(command) == 'git rm -r test.txt'
# end unit test

# Generated at 2022-06-14 10:18:49.324382
# Unit test for function match
def test_match():
    assert match(Command('git rm fuck', '', 'fatal: not removing \'fuck\' recursively without -r'))
    assert not match(Command('git rm fuck', '', ''))


# Generated at 2022-06-14 10:19:01.349763
# Unit test for function match
def test_match():
	assert match(Command(' rm -rf .vim/bundle/fugitive', '')) == True
	assert match(Command(' rm -rf .vim/bundle/fugitive', 'fatal: not removing \'path/to/file\' recursively without -r\n')) == True
	assert match(Command(' rm -rf .vim/bundle/fugitive', 'fatal: not removing \'path/to/file\'')) == False

# Generated at 2022-06-14 10:19:06.403484
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm -rf test.txt") == "git rm -rf -r test.txt"

# Generated at 2022-06-14 10:19:09.389823
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm file", "", "fatal: not removing 'file' recursively without -r")) == "git rm -r file"

# Generated at 2022-06-14 10:19:13.573294
# Unit test for function match
def test_match():
    command_output = '''
fatal: not removing 'bash_history' recursively without -r
'''
    command = Command('git rm bash_history', command_output)
    assert match(command)


# Generated at 2022-06-14 10:19:16.806225
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm '-r'", "Sorry, we are not here")
    assert get_new_command(command) == "git rm '-r' -r"

# Generated at 2022-06-14 10:19:21.005325
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    output = u"""fatal: not removing 'https://github.com/' recursively without -r
    """
    command = Command('rm https://github.com/', output)
    assert get_new_command(command) == 'git rm -r https://github.com/'

# Generated at 2022-06-14 10:19:23.103056
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm README.md')
    assert get_new_command(command) == 'git rm -r README.md'

# Generated at 2022-06-14 10:19:25.393078
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file',
                                   'fatal: not removing \'file\' recursively without -r')) == 'git rm -r file'

# Generated at 2022-06-14 10:19:27.905426
# Unit test for function match
def test_match():
    assert match(
        Command('git rm file.txt', 'fatal: not removing '
                '\'.gitignore\' recursively without -r'))
    assert not match(Command('git rm file.txt', 'foo'))

# Generated at 2022-06-14 10:19:30.427496
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file1 file2', '')) == 'git rm -r file1 file2'

# Generated at 2022-06-14 10:19:32.652866
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command(('git rm file', '', ''), 'git')) == 'git rm -r file'

# Generated at 2022-06-14 10:19:38.636765
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm -r -- foo'
    output = 'fatal: not removing \'-r--\' recursively without -r'
    command = Command(script, output)
    assert get_new_command(command) == 'git rm -r -r -- foo'

# Generated at 2022-06-14 10:19:47.279233
# Unit test for function get_new_command
def test_get_new_command():
    command_out_str = """
    error: The following untracked working tree files would be removed by checkout:
        .gitignore
    Please move or remove them before you switch branches.
    Aborting
    """
    command = type('obj', (object,), {
        'script': 'git rm .gitignore',
        'script_parts': ['git', 'rm', '.gitignore'],
        'output': command_out_str})
    new_command = get_new_command(command)
    assert 'git rm -r .gitignore' == new_command

# Generated at 2022-06-14 10:19:54.010455
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
    '''fatal: not removing 'some/non_existent_path' recursively without -r''',
    ''))


# Generated at 2022-06-14 10:20:01.770482
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git rm -r')) == "git rm -r -r")
    assert(get_new_command(Command('git rm')) == "git rm -r")
    assert(get_new_command(Command('git rm file0 file1')) == "git rm -r file0 file1")
    assert(get_new_command(Command('git rm -f file0 file1')) == "git rm -f -r file0 file1")
    assert(get_new_command(Command('git rm -r file0 file1')) == "git rm -r -r file0 file1")

# Generated at 2022-06-14 10:20:07.222754
# Unit test for function match
def test_match():
    assert match(Command('git rm "file.txt"',
                         'fatal: not removing \'"file.txt"\' recursively without -r'))
    assert not match(Command('git rm "file.txt"', ''))
    assert not match(Command('git rm', ''))
    assert not match(Command('git rm -r', ''))


# Generated at 2022-06-14 10:20:13.924932
# Unit test for function match
def test_match():
    assert match(Command('git rm dir', '', 'fatal: not removing \'dir\' recursively without -r'))
    assert match(Command('git rm dir', '', 'fatal: not removing \'dirs\' recursively without -r'))
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', '', ''))
    assert not match(Command('git rm dir', ''))


# Generated at 2022-06-14 10:20:17.734372
# Unit test for function get_new_command
def test_get_new_command():
    command = Mock(script='git rm -r',output='fatal: not removing '
                   'directory \'config\' recursively without -r')
    assert get_new_command(command) == 'git rm -r -r'

# Generated at 2022-06-14 10:20:25.706408
# Unit test for function match
def test_match():
    assert match(Command('git rm file1 file2',
                         'fatal: not removing \'file1\' recursively without -r'))
    assert not match(Command('git rm file1 file2', ''))
    assert not match(Command('git rm file1 file2', 'some error'))


# Generated at 2022-06-14 10:20:30.094802
# Unit test for function match
def test_match():
    assert match(Command('git rm -r file',
                         'fatal: not removing \'file\' recursively without -r'))

#Unit test for function get_new_command

# Generated at 2022-06-14 10:20:34.145957
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm file1 file2',
                      output="fatal: not removing 'file1' recursively without -r")
    assert get_new_command(command) == u'git rm -r file1 file2'

# Generated at 2022-06-14 10:20:44.136307
# Unit test for function match
def test_match():
    assert match(Command('git rm *.pyc', 'fatal: not removing \'requirements.txt\' recursively without -r'))
    assert match(Command('git rm -r *.pyc', 'fatal: not removing \'requirements.txt\' recursively without -r')) is False


# Generated at 2022-06-14 10:20:53.712840
# Unit test for function match
def test_match():
    assert match(Command('git rm 1', stderr='fatal: not removing \'1\' recursively without -r'))
    assert not match(Command('git rm 1', stderr='fatal: not removing \'1\' recursively without -r', stdout='No such file'))
    assert match(Command('git rm 1', stderr='fatal: not removing \'1\' recursively without -r', stdout='No such file or directory'))



# Generated at 2022-06-14 10:21:01.122797
# Unit test for function get_new_command
def test_get_new_command():
    output = "fatal: not removing 'nothing.txt' recursively without -r"
    command = Command("git rm nothing.txt", output)
    assert get_new_command(command) == "git rm -r nothing.txt"

# Generated at 2022-06-14 10:21:04.508732
# Unit test for function match
def test_match():
    command = Command('git rm hello.md', 'fatal: not removing \'hello.md\' recursively without -r')
    assert match(command)


# Generated at 2022-06-14 10:21:07.753913
# Unit test for function get_new_command
def test_get_new_command():
    # type: () -> None
    assert get_new_command(Command(
        script='git rm file',
        output='fatal: not removing \'file\' recursively without -r')) == 'git rm -r file'

# Generated at 2022-06-14 10:21:08.734722
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm file', '', '', '', '', '')) == 'git rm -r file'

# Generated at 2022-06-14 10:21:13.946125
# Unit test for function match
def test_match():
    assert match(Command('git rm -r file', ''))
    assert not match(Command('git rm file',
                             "fatal: not removing 'file' recursively without -r\n"))
    assert match(Command('git rm -r file', "fatal: not removing 'file' recursively without -r\n"))
    assert not match(Command('git rm file', ''))


# Generated at 2022-06-14 10:21:20.511386
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file') == 'git rm -r file'
    assert get_new_command('git rm -rm file') == 'git rm -rm -r file'

# Generated at 2022-06-14 10:21:23.321871
# Unit test for function match

# Generated at 2022-06-14 10:21:32.584845
# Unit test for function match
def test_match():
    assert(match(Command('git rm file.php', 'fatal: not removing \'file.php\' recursively without -r')))
    assert(not match(Command('git rd file.php', 'fatal: not removing \'file.php\' recursively without -r')))
    assert(not match(Command('git rm file.php', 'fatal: not removing \'file.php\'  recursively without -r')))
    assert(not match(Command('git rm file.php', 'fatal: not removing \'file.php\' recursively ')))
    assert(not match(Command('git rm file.php', 'fatal: not removing \'file.php\'  recursively ')))


# Generated at 2022-06-14 10:21:45.329582
# Unit test for function get_new_command
def test_get_new_command():
    command = u'git rm build ../../test/test_utils.pyc'
    new_command = get_new_command(Command(command, ''))
    assert new_command == command.replace('rm', 'rm -r')

# Generated at 2022-06-14 10:21:51.466558
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm --cached -r test') == 'git rm -r --cached test'
    assert get_new_command('git rm test') == 'git rm -r test'
    assert get_new_command('git rm') != 'git rm -r'
    assert get_new_command('git rm -r') == 'git rm -r'
    assert get_new_command('git rm --cached') == 'git rm -r --cached'

# Generated at 2022-06-14 10:21:59.344436
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         stderr='fatal: not removing "file" recursively without -r\n'))
    assert not match(Command('git rm -r file',
                         stderr='fatal: not removing "file" recursively without -r\n'))



# Generated at 2022-06-14 10:22:02.385631
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file', 'fatal: not removing \'file\' recursively without -r', None)) == 'git rm -r file'

# Generated at 2022-06-14 10:22:05.873254
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('git rm foo',
                         'fatal: not removing \'foo\' recursively without -r\n'))



# Generated at 2022-06-14 10:22:07.812852
# Unit test for function match

# Generated at 2022-06-14 10:22:13.543063
# Unit test for function match
def test_match():
    """
    Unit test for function match
    """

    output = u'fatal: not removing \'steps/chain/tuning/decode.sh\' recursively without -r'
    assert match(Command('git stash', output)) == True
    assert match(Command('git reset', output)) == False



# Generated at 2022-06-14 10:22:16.087888
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf dir', '')) ==\
        'git rm -r -f dir'

# Generated at 2022-06-14 10:22:19.267357
# Unit test for function match
def test_match():
    assert (match(Command('git rm qqq', 
        stderr='fatal: not removing \'qqq\' recursively without -r\n',
        )))


# Generated at 2022-06-14 10:22:27.963828
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         "fatal: not removing 'file.txt' recursively without -r"))
    assert not match(Command('git rm file.txt', ""))
    assert not match(Command('git rm file.txt',
                             "fatal: not removing 'file.txt' recursively without -r",
                             'other_error'))

# Generated at 2022-06-14 10:22:52.902493
# Unit test for function match
def test_match():
    assert match(Command('git rm file0 file1 file2 file3',
                         'fatal: not removing \'file1\' recursively without -r'))
    assert not match(Command('git rm file0 file1 file2 file3', 'rm file1'))
    assert not match(Command('git rm file0 file1 file2 file3',
                             'fatal: not removing \'file1\' recursively without -r',
                             'rm: missing operand'))



# Generated at 2022-06-14 10:22:57.465478
# Unit test for function match
def test_match():
    assert match(Command('rm -f demo.txt',
                         'fatal: not removing \'demo.txt\' recursively without -r\n',
                         ''))
    assert not match(Command('rm -f demo.txt',
                             'fatal: not removing \'demo.txt\' recursively without -r\n',
                             '',
                             shortcut='a'))


# Generated at 2022-06-14 10:23:03.273516
# Unit test for function match
def test_match():
    command = Command('git rm foo', '', 'fatal: not removing \'foo\' recursively without -r')
    assert match(command) == True
    command = Command('git rm foo', '', 'fatal: not removing \'foo\' recursively with -r')
    assert match(command) == False


# Generated at 2022-06-14 10:23:14.447124
# Unit test for function match
def test_match():
    # Check if match function return true when git command has rm and right error
    assert match(Command('git rm file',
                         "fatal: not removing 'file' recursively without -r"))
    # Check if match function return true when git command has rm in another directory and right error
    assert match(Command('git rm directory',
                         "fatal: not removing 'directory' recursively without -r"))
    # Check if match function return false when git command has rm and wrong error
    assert not match(Command('git rm directory',
                             "fatal: not removing 'directory' recursively without -i"))
    # Check if match function return false when git command has rm and the error is put before command
    assert not match(Command('git rm directory',
                             "fatal: not removing 'directory' recursively without -r\ngit rm directory"))

# Generated at 2022-06-14 10:23:22.318432
# Unit test for function match
def test_match():
    # Test for error when rm is used on directory
    # from: https://github.com/nvbn/thefuck/issues/677
    command = Command(' rm -rfv ./buck')
    assert(match(command) is True)

    # Test for error when rm is used on directory
    # from: https://github.com/nvbn/thefuck/issues/677
    command = Command(' rm -rfv ./buck')
    assert(match(command) is True)

    # Test for error when rm is used on single file
    # from: https://github.com/nvbn/thefuck/issues/677
    command = Command(' rm -rfv ./file.m')
    assert(match(command) is False)

    # Test for multiple files

# Generated at 2022-06-14 10:23:25.705146
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r ./fstest/test')
    assert get_new_command(command) == 'git rm -r -r ./fstest/test'
    assert command

# Generated at 2022-06-14 10:23:28.012641
# Unit test for function match
def test_match():
    assert match(Command('git branch -D branch', "fatal: not removing 'file'"))


# Generated at 2022-06-14 10:23:31.244276
# Unit test for function get_new_command
def test_get_new_command():
    command.script = 'git rm dir'
    command.output = "fatal: not removing 'dir' recursively without -r"
    assert get_new_command(command) == 'git rm -r dir'

# Generated at 2022-06-14 10:23:36.680921
# Unit test for function match
def test_match():
    match_results = ['rm one', 'rm -r two']

    nonmatch_results = ['git rm', 'git rm one']

    # match
    for result in match_results:
        assert match(Command(script=result))

    # non-match
    for result in nonmatch_results:
        assert not match(Command(script=result))


# Generated at 2022-06-14 10:23:43.671794
# Unit test for function match
def test_match():
    assert match(Command('git rm folder', 'fatal: not removing \'folder\' recursively without -r', None))
    assert not match(Command('git rm folder', 'fatal: not removing \'folder\' recursively with -r', None))
    assert not match(Command('git rm -r folder', 'fatal: not removing \'folder\' recursively without -r', None))

