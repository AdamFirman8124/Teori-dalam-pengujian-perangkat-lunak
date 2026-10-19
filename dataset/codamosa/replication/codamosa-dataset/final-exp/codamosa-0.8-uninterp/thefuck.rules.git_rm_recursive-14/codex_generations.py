

# Generated at 2022-06-14 10:14:00.108876
# Unit test for function match
def test_match():
    assert match(Command("git rm -r test", "fatal: not removing 'test' recursively without -r"))

# Generated at 2022-06-14 10:14:04.529579
# Unit test for function match
def test_match():
    assert match(Command(' git rm hello', '', 'fatal: not removing \'hello\' recursively without -r'))
    assert not match(Command('git rm hello', ''))
    assert not match(Command(' git rm hello', ''))


# Generated at 2022-06-14 10:14:09.557670
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 'error: pathspec \'file\' did not match any file(s) known to git.'))
    assert match(Command('git rm directory', 'fatal: not removing \'directory\' recursively without -r'))
    assert not match(Command('git rm file', ''))

# Generated at 2022-06-14 10:14:13.523904
# Unit test for function match
def test_match():
    assert match(Command('rm foo',
                         'fatal: not removing ''foo'' recursively without -r',
                         ''))
    assert not match(Command('rm foo', '', ''))


# Generated at 2022-06-14 10:14:18.381779
# Unit test for function match
def test_match():
    # Test for false positive
    assert not match(Command('git rm false', ''))
    # Test for false negative
    assert match(Command(
        'git rm -f teste.py',
        'fatal: not removing \'teste.py\' recursively without -r'
        ))



# Generated at 2022-06-14 10:14:23.599479
# Unit test for function match
def test_match():
    assert match('git rm readme.txt')
    # Should not match
    assert not match('git rm-r readme.txt')
    assert not match('git rm readme.txt -r')
    assert not match('git rm-r readme.txt')



# Generated at 2022-06-14 10:14:31.808299
# Unit test for function match
def test_match():
    assert match(Command(script = 'git rm file.txt', output='fatal: not removing \'file.txt\' recursively without -r' ))
    assert not match(Command(script = 'git rm file.txt', output='fatal: not removing \'file.txt\' recursively without -r' ))
    assert not match(Command(script = 'git rm file.txt', output='fatal: not removing \'file.txt\' recursively without -r' ))


# Generated at 2022-06-14 10:14:34.163723
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm -r') == 'git rm -r -r'


# Generated at 2022-06-14 10:14:36.506818
# Unit test for function match
def test_match():
    assert match(Command('git rm'))
    assert not match(Command('git rm -r'))


# Generated at 2022-06-14 10:14:39.985592
# Unit test for function match
def test_match():
    command = Command('git rm file',
                      'fatal: not removing \'file\' recursively without -r\n',
                      '', 1)
    assert (match(command))




# Generated at 2022-06-14 10:14:47.156568
# Unit test for function match
def test_match():
    assert match(Command('git rm', 'fatal: not removing \'a.out\' recursively without -r'))
    assert not match(Command('git rm', 'fatal: not removing \'a.out\''))
    assert match(Command('git rm d', 'fatal: not removing \'d/e\' recursively without -r'))
    assert not match(Command('git rm d', 'fatal: not removing \'a/e\''))



# Generated at 2022-06-14 10:14:53.600504
# Unit test for function match
def test_match():
    assert match(Command('rm -r test.txt', 'fatal: not removing \'test.txt\' recursively without -r'))

# Generated at 2022-06-14 10:14:56.498516
# Unit test for function match
def test_match():
    assert match(Command('git rm a', "fatal: not removing 'c' recursively without -r"))


# Generated at 2022-06-14 10:15:05.391277
# Unit test for function match
def test_match():
    match_output = \
"""
fatal: not removing 'README' recursively without -r
Did you mean this?
        rm --cached README

"""
    assert match(Command(' rm README', match_output))
    assert not match(Command(' rm README', ''))
    assert not match(Command(' rm README', 'No manual entry for '))
    assert not match(Command(' rm README', 'fatal: not removing README'))


# Generated at 2022-06-14 10:15:07.751017
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                output='fatal: not removing \'file\' recursively without -r'))

# Generated at 2022-06-14 10:15:14.495704
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file', 'fatal: not removing '
                          '\'file\' recursively without -r')) \
           == 'git rm -r file'
    assert get_new_command(Command('git rm -rf file', 'fatal: not removing '
                          '\'file\' recursively without -r')) \
           != 'git rm -rf -r file'

# Generated at 2022-06-14 10:15:17.225869
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r file' == get_new_command('git rm file')
    assert 'git branch -D -r file' == get_new_command('git branch -D file')

# Generated at 2022-06-14 10:15:23.246550
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -rf test', 'fatal: not removing \'a/b\' recursively without -r')
    assert get_new_command(command)[1] == 'git rm -rf -r test'
    command = Command('git rm -rf test1 test2', 'fatal: not removing \'a/b\' recursively without -r')
    assert get_new_command(command)[1] == 'git rm -rf -r test1 test2'

# Generated at 2022-06-14 10:15:27.949291
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file.txt',
                      'fatal: not removing \'file.txt\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -r file.txt'

# Generated at 2022-06-14 10:15:30.636255
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm foo', '', '')
    assert get_new_command(command) == 'git rm -r foo'

# Generated at 2022-06-14 10:15:41.846400
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt', 'fatal: not removing \
    \'file.txt\' recursively  without -r\n'))
    assert match(Command('git rm file.txt', 'fatal: not removing \
    \'file.txt.txt\' recursively  without -r\n'))
    assert match(Command('something rm file.txt', 'fatal: not removing \
    \'file.txt\' recursively  without -r\n'))

    assert not match(Command(' git rm file.txt', 'fatal: not removing \'file.txt\' recursively  without -r\n'))
    assert not match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively  without -r'))

# Generated at 2022-06-14 10:15:44.752521
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm foo/bar")) == "git rm -r foo/bar"


# Generated at 2022-06-14 10:15:50.229012
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.specific.git import git_support
    git_support()  # make the monkeypatch
    command = Command('git rm test', '', 'fatal: not removing \'test\' recursively without -r')
    assert get_new_command(command) == u'git rm -r test'

# Generated at 2022-06-14 10:15:55.478549
# Unit test for function get_new_command
def test_get_new_command():
  new_command = get_new_command(Command('git rm file_to_be_removed', 'fatal: not removing ' +
                                                                    '\'file_to_be_removed\' ' +
                                                                    'recursively without -r'))
  assert new_command == 'git rm -r file_to_be_removed'

# Generated at 2022-06-14 10:15:58.896378
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm git.py', 'fatal: not removing \'git.py\' recursively without -r')) == 'git rm -r git.py'

# Generated at 2022-06-14 10:16:08.914878
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command("git rm -f file1 file2", "fatal: not removing 'file1' recursively without -r")
    assert get_new_command(command1) == "git rm -r -f file1 file2"
    command2 = Command("git rm -f file1", "fatal: not removing 'file1' recursively without -r")
    assert get_new_command(command2) == "git rm -r -f file1"
    command3 = Command("git rm file1 file2", "fatal: not removing 'file1' recursively without -r")
    assert get_new_command(command3) == "git rm -r file1 file2"
    command4 = Command("git rm file1", "fatal: not removing 'file1' recursively without -r")
    assert get_

# Generated at 2022-06-14 10:16:11.973829
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command(script='git rm target', stderr='''fatal: not removing 'target' recursively without -r\n''')
    assert get_new_command(command1) == 'git rm -r target'

# Generated at 2022-06-14 10:16:15.939624
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm -r git', '')) == 'rm -r -r git'
    assert get_new_command(Command('rm -R git', '')) == 'rm -R -r git'

# Generated at 2022-06-14 10:16:19.382343
# Unit test for function match
def test_match():
    command = Command(script=u"git rm -r a_file.txt",
                      output=u"fatal: not removing 'a_file.txt' recursively without -r")
    assert match(command)


# Generated at 2022-06-14 10:16:22.994893
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf .', 'fatal: not removing \'.\' recursively without -r\n'))
    assert not match(Command('git rm -rf .'))

# Generated at 2022-06-14 10:16:28.416089
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm target_file') == 'git rm -r target_file'

# Unit tests for function match

# Generated at 2022-06-14 10:16:31.781257
# Unit test for function match
def test_match():
    command = Command('git rm -r config',
        'fatal: not removing \'config\' recursively without -r\n')
    assert match(command)


# Generated at 2022-06-14 10:16:39.410812
# Unit test for function match
def test_match():
	from thefuck.types import Command
	assert match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively without -r\n', '', 1, ''))
	assert not match(Command('git rm -r dir', '', '', 1, ''))
	assert not match(Command('git config --global color.ui true', 'fatal: not removing \'file.txt\' recursively without -r\n', '', 1, ''))


# Generated at 2022-06-14 10:16:43.984502
# Unit test for function match
def test_match():
    match_test = match(Command('git rm -r fileWithSpace',
    r"""fatal: not removing 'fileWithSpace' recursively without -r
       hint: Use '--' to indicate path is finished
       hint: Use 'git status' to view changes to be committed
       error: The following untracked working tree files would be removed by
       operation:
       fileWithSpace
       Aborting"""))
    assert match_test


# Generated at 2022-06-14 10:16:49.719010
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm -r git-lfs.json",
                      "fatal: not removing 'git-lfs.json' recursively without -r\n")
    new_command = get_new_command(command)
    assert new_command == "git rm -r -r git-lfs.json"

# Generated at 2022-06-14 10:16:53.680075
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test.txt',
                      'fatal: not removing \'test.txt\' recursively without -r\n',
                      '', 0, None)
    assert get_new_command(command) == "git rm -r test.txt"

# Generated at 2022-06-14 10:16:58.778083
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm new_file_name',
            'fatal: not removing \'new_file_name\' recursively without -r\n')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r new_file_name'

# Generated at 2022-06-14 10:17:00.721080
# Unit test for function match
def test_match():
    assert match(Command('git rm file', ''))
    assert not match(Command('git rm -r folder', ''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 10:17:08.805931
# Unit test for function get_new_command
def test_get_new_command():
    output = u"fatal: not removing 'a/b/c/d/e' recursively without -r"
    comments = u"It seems that you're trying to remove a directory with `rm`. It's possible that you can use `rm -rf` instead"
    command = Command('rm a/b/c/d/e', output, comments)
    assert get_new_command(command) == u"git rm -r a/b/c/d/e"

# Generated at 2022-06-14 10:17:14.752633
# Unit test for function get_new_command
def test_get_new_command():
    assert u"git rm -r foo/" == get_new_command(
        Command(script=u"git rm foo/",
                output=u"fatal: not removing 'foo/' recursively without -r\n",
                stderr=u"",
                stdout=u""))

# Generated at 2022-06-14 10:17:25.060292
# Unit test for function match
def test_match():
    assert match(Command('git rm test.txt', 'fatal: not removing \'/home/user/test_python_script/test.txt\' recursively without -r'))
    assert not match(Command('git rm test.txt', ''))
    assert not match(Command('rm test.txt', ''))


# Generated at 2022-06-14 10:17:28.354465
# Unit test for function match
def test_match():
    command = Command('git rm -r file',
                      output="error: Entering directory 'file'\nfatal: not removing 'file' recursively without -r")
    assert match(command)


# Generated at 2022-06-14 10:17:31.815149
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm dir',
                                   'fatal: not removing \'dir\' recursively without -r',
                                   '', 4)) == 'git rm -r dir'

# Generated at 2022-06-14 10:17:37.901009
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command('git rm newfile.txt', 'fatal: not removing \'newfile.txt\' recursively without -r')
    new_command1 = u'git rm -r newfile.txt'
    assert get_new_command(command1) == new_command1

# Generated at 2022-06-14 10:17:42.240454
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo', ''))
    assert not match(Command('git rm -r foo', ''))
    assert not match(Command('ls foo', ''))


# Generated at 2022-06-14 10:17:48.564972
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm index.html', 'fatal: not removing \'index.html\' recursively without -r')) == 'git rm -r index.html'

# Generated at 2022-06-14 10:17:55.246612
# Unit test for function match
def test_match():
    # If a command is a git command
    git_command = 'git rm file'
    git_output = 'fatal: not removing \'file\' recursively without -r'

    assert match(Command(git_command, git_output))
    # If a command isn't a git command
    not_git_command = 'rm file'
    not_git_output = ''

    assert not match(Command(not_git_command, not_git_output))


# Generated at 2022-06-14 10:17:59.820323
# Unit test for function match
def test_match():
    command = Command('git status', 'fatal: not removing \'path/to/file/\' recursively without -r')
    assert match(command)

    command = Command('git status', 'Not removing \'path/to/file/\' recursively without -r')
    assert not match(command)


# Generated at 2022-06-14 10:18:04.757690
# Unit test for function match
def test_match():
    # Check True
    command = Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r\n', '')
    assert match(command)

    # Check False
    command = Command('git rm test.txt', '', '')
    assert not match(command)

# Generated at 2022-06-14 10:18:08.827203
# Unit test for function match
def test_match():
    assert match(Command('git rm untracked', ''))
    assert not match(Command(' git rm untracked', ''))
    assert not match(Command('git rm untracked', '', ''))

# Generated at 2022-06-14 10:18:21.833889
# Unit test for function match
def test_match():
    assert match(Command('rm foo',
                         '',
                         'fatal: not removing \'foo\' recursively without -r'))


# Generated at 2022-06-14 10:18:27.829500
# Unit test for function get_new_command
def test_get_new_command():
    old_command = u'git rm -f file.txt'
    new_command = get_new_command(type('cmd', (object,),
    {'script': old_command, 'script_parts': old_command.split()}))
    assert new_command == u'git rm -rf file.txt'

# Generated at 2022-06-14 10:18:29.594829
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm foo")) == "git rm -r foo"

# Generated at 2022-06-14 10:18:31.888670
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm -f win32-x64")) == "git rm -rf win32-x64"

# Generated at 2022-06-14 10:18:36.058396
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm a')
    assert get_new_command(command) == 'git rm -r a'

    command = Command('git rm abcdef')
    assert get_new_command(command) == 'git rm -r abcdef'

    command = Command('git rm -r abcdef')
    assert get_new_command(command) == 'git rm -r abcdef'



# Generated at 2022-06-14 10:18:40.903749
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('git rm foo/')) == 'git rm -r foo/'
    assert get_new_command(Command('git rm -f foo/')) == 'git rm -f -r foo/'

# Generated at 2022-06-14 10:18:43.794156
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm x")
    get_new_command(command)
    assert command.script == 'git rm -r x'

# Generated at 2022-06-14 10:18:47.142181
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file')
    command.output = 'fatal: not removing \'file\' recursively without -r'
    assert get_new_command(command) == 'git rm -r file'

# Generated at 2022-06-14 10:18:52.189081
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git rm -rf file1 file2',
                                    'fatal: not removing \'file1\' recursively without -r',
                                    'git rm -rf file1 file2'))
            == 'git rm -rf -r file1 file2')

# Generated at 2022-06-14 10:19:02.920850
# Unit test for function match
def test_match():
    from thefuck.types import Command

    repo_path = tempfile.mkdtemp('repo')
    with cwd(repo_path):
        os.mkdir('dir')
        os.mkdir('dir/subdir')
        open('dir/subdir/file', 'a').close()
        assert git_support(Command('git rm dir', ''))
        assert not git_support(Command('git rm dir', 'fatal: not removing'
                                                     " 'dir/subdir'"
                                                     " recursively without -r"))

# Generated at 2022-06-14 10:19:14.998736
# Unit test for function match
def test_match():
    assert match(Command('git rm',
                         'fatal: not removing \'build/static/\''
                         ' recursively without -r'))


# Generated at 2022-06-14 10:19:18.272728
# Unit test for function match
def test_match():
    assert match(Command("git rm file", "fatal: not removing 'file' recursively without -r"))
    assert not match(Command("git rm file", ""))


# Generated at 2022-06-14 10:19:23.998620
# Unit test for function match
def test_match():
    assert match(Command('git rm filename',
                         'fatal: not removing \'filename\' recursively without -r\n'))
    assert not match(Command('git rm filename',
                             'fatal: not removing \'filename\' recursively without -q\n'))
    assert not match(Command('git config --global user.name', ''))

# Generated at 2022-06-14 10:19:30.639550
# Unit test for function match
def test_match():
    assert match(Command('git rm f/d', '', ''))
    assert match(Command('git rm f/d/', '', ''))
    assert match(Command('git rm f/d/test.py', '', ''))
    assert match(Command('git rm -f f/d/test.py', '', ''))
    assert match(Command('git rm --force f/d/test.py', '', ''))
    assert match(Command('git rm -n f/d/test.py', '', ''))
    assert match(Command('git rm --dry-run f/d/test.py', '', ''))
    assert not match(Command('git rm f/d/test.py', '', ''))


# Generated at 2022-06-14 10:19:33.759063
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing '
                         'file recursively without -r'))
    assert not match(Command('git rm', None))



# Generated at 2022-06-14 10:19:38.874416
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm foo/bar") == "git rm -r foo/bar"
    assert get_new_command("git rm -f foo/bar") == "git rm -f -r foo/bar"
    assert get_new_command("git rm -f bar/foo") == "git rm -f -r bar/foo"

# Generated at 2022-06-14 10:19:43.615307
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         stderr=' fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git stash'))


# Generated at 2022-06-14 10:19:50.676706
# Unit test for function match
def test_match():
    assert match(Command(script='git rm foo',
                         output="fatal: not removing 'foo' recursively without -r"))

# Generated at 2022-06-14 10:19:55.063093
# Unit test for function get_new_command
def test_get_new_command():
    script = u'rm -rf'
    out = "fatal: not removing '"
    command = Command(script, out)
    assert(get_new_command(command) == 'rm -r -rf')
    

# Generated at 2022-06-14 10:19:57.943103
# Unit test for function get_new_command
def test_get_new_command():
   command = u'git rm file'
   new_command = get_new_command(Command(command))
   assert new_command == u'git rm -r file'

# Generated at 2022-06-14 10:20:30.053454
# Unit test for function match
def test_match():
    assert match(Command('git rm new', output='fatal: not removing \'new\' recursively without -r'))
    assert not match(Command('git rm new', output='fatal: not removing \'new\' recursively without -r', stderr='fatal: not removing \'new\' recursively without -r'))
    assert not match(Command('git rm new', output='fatal: not removing \'new\' recursively with -r'))
    assert not match(Command(' rm new', output='fatal: not removing \'new\' recursively without -r'))
    assert not match(Command('rm new'))


# Generated at 2022-06-14 10:20:33.619549
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r')
    assert get_new_command(command) == u'git rm -r test.txt'

# Generated at 2022-06-14 10:20:39.652865
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively without -r', ''))
    assert not match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively', ''))
    assert not match(Command('git rm -r file.txt', 'fatal: not removing \'file.txt\' recursively', ''))


# Generated at 2022-06-14 10:20:45.197666
# Unit test for function match
def test_match():
    assert match(Command('git rm any'))
    assert match(Command('git rm any', ''))
    assert match(Command('git rm any', '', ''))
    assert not match(Command('git rm '))
    assert not match(Command('rm any', ''))
    assert not match(Command('rm ', ''))


# Generated at 2022-06-14 10:20:48.328454
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r', '', 'fatal: not removing \'\' recursively without -r')) == 'git rm -r -r'

# Generated at 2022-06-14 10:20:54.107420
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ['git', 'rm', 'submodule', "/home/user/project"]
    expected_new_command = 'git rm -r submodule "/home/user/project"'
    assert(get_new_command(namedtuple("Command", "script script_parts output")(
        script=' '.join(command_parts), script_parts=command_parts, output="fatal: not removing 'submodule' recursively without -r\n"))
            == expected_new_command)
    assert(get_new_command(namedtuple("Command", "script script_parts output")(
        script=' '.join(command_parts), script_parts=command_parts, output=""))
            == None)

# Generated at 2022-06-14 10:20:59.189560
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm dir')) == 'git rm -r dir'

# Generated at 2022-06-14 10:21:10.551775
# Unit test for function match
def test_match():
    for command, output in [
            ('git rm unknown/path',
             'fatal: not removing \'unknown/path\' recursively without -r'),
            ('git rm --cached unknown/path',
             'fatal: not removing \'unknown/path\' recursively without -r'),
            ('git rm -n unknown/path',
             'fatal: not removing \'unknown/path\' recursively without -r'),
            ('git rm --dry-run unknown/path',
             'fatal: not removing \'unknown/path\' recursively without -r')]:
        assert match(Command(command, output))

# Generated at 2022-06-14 10:21:13.916598
# Unit test for function match
def test_match():
    assert match(Command('git rm', 'fatal: not removing \'dir/file\' recursively without -r'))
    assert not match(Command('git rm', 'rm file'))

# Generated at 2022-06-14 10:21:18.958419
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    Command.script = 'git rm -f'
    Command.script_parts = Command.script.split()
    Command.output = "fatal: not removing 'test' recursively without -r"

    assert get_new_command(Command) == 'git rm -r -f'

# Generated at 2022-06-14 10:21:42.503175
# Unit test for function get_new_command
def test_get_new_command():
    command = make_command(['git', 'rm', 'test.txt'],
                           stderr="fatal: not removing 'test.txt' recursively without -r\n")
    assert get_new_command(command) == u'git rm -r test.txt'

# Generated at 2022-06-14 10:21:49.179068
# Unit test for function match
def test_match():
    assert match(Command('git rm new_file', 'fatal: not removing \'new_file\' recursively without -r'))
    assert not match(Command('git rm new_file', ''))
    assert not match(Command('git rm new_file', 'fatal: not removing recursively without -r'))
    assert not match(Command('git rm -r new_file', 'fatal: not removing \'new_file\' recursively without -r'))


# Generated at 2022-06-14 10:22:00.071543
# Unit test for function match
def test_match():
    # Positive scenario 1 : Exact match
    assert (match(Command(script='git rm -r 101.txt',
                          output='fatal: not removing \'101.txt\' recursively without -r')) )
    # Positive scenario 2 : When command line includes numbers
    assert (match(Command(script='git rm -r 101.txt 201.txt',
                          output='fatal: not removing \'101.txt\' recursively without -r')) )
    # Negative scenario

# Generated at 2022-06-14 10:22:04.230273
# Unit test for function get_new_command
def test_get_new_command():
    command.script = "git rm file"
    command.output = "fatal: not removing 'file' recursively without -r"
    assert get_new_command(command) == "git rm -r file"

# Generated at 2022-06-14 10:22:09.330420
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm non_existant_file',
                                   'fatal: not removing non_existant_file recursively without -r')) == 'git rm -r non_existant_file'
    assert get_new_command(Command('git rm non_existant_file')) == 'git rm non_existant_file'

# Generated at 2022-06-14 10:22:12.740827
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm -rf lib", "", "")
    assert get_new_command(command) == "git rm -rf -r lib"

# Generated at 2022-06-14 10:22:14.895692
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test/test')) == 'git rm -r test/test'

# Generated at 2022-06-14 10:22:20.395433
# Unit test for function match
def test_match():
    assert match(Command(script='git commit', output=''))
    assert not match(Command(script='git push', output=''))
    assert not match(Command(script='git commit', output='rm: recursively remove '))
    assert match(Command(script='git rm stuff.txt', output='rm: recursively remove '))


# Generated at 2022-06-14 10:22:27.963359
# Unit test for function get_new_command
def test_get_new_command():
    command_script = u'git rm file.txt'
    command_output = u"fatal: not removing 'file.txt' recursively without -r"
    command = Command(script=command_script,
                      output=command_output)
    new_command = get_new_command(command)
    assert new_command == u'git rm -r file.txt'

# Generated at 2022-06-14 10:22:30.453928
# Unit test for function match
def test_match():
    assert match(Command('git rm -r dir a/file.txt', 'fatal: not removing \'dir\' recursively without -r\n'))


# Generated at 2022-06-14 10:22:51.982418
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

# Generated at 2022-06-14 10:22:57.163174
# Unit test for function get_new_command
def test_get_new_command():
    assert git_rm.get_new_command(Command('git rm abc -r', ''))
    assert git_rm.get_new_command(Command('git rm -r abc', '')) == 'git rm -r abc'
    assert git_rm.get_new_command(Command('git rm abc', 'fatal: not removing \'abc\' recursively without -r\n')) == 'git rm -r abc'

# Generated at 2022-06-14 10:22:59.654035
# Unit test for function match
def test_match():
    assert match(Command('git rm *'))
    assert not match(Command('ls'))


# Generated at 2022-06-14 10:23:03.205890
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git rm file', 'fatal: not removing \'file\' recursively without -r')) == 'git rm -r file')

# Generated at 2022-06-14 10:23:11.808567
# Unit test for function match
def test_match():
    assert match(Command('git rm -r a b c', 'fatal: not removing \'a\' recursively without -r'))
    assert not match(Command('git rm -r a b c', 'fatal: removing \'a\' recursively without -r'))
    assert not match(Command('git rm -r a b c', 'fatal: removing \'a\' recursively without -r', 'git: \'rm\' is not a git command. See \'git --help\'.'))



# Generated at 2022-06-14 10:23:15.242273
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file.txt')
    assert get_new_command(command) == 'git rm -r file.txt'

# Generated at 2022-06-14 10:23:21.074208
# Unit test for function match
def test_match():
    assert match(Command('git rm 1', ''))
    assert match(Command('git rm 1', 'fatal: not removing \'1\' recursively without -r\n'))
    assert not match(Command('git rm 1', 'fatal: not removing \'1\' recursively with -r\n'))


# Generated at 2022-06-14 10:23:24.989202
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo', ''))



# Generated at 2022-06-14 10:23:29.818723
# Unit test for function get_new_command
def test_get_new_command():
    command_string = "git rm file"
    command = Command(command_string, "fatal: not removing 'file' recursively without -r\n")
    assert get_new_command(command) == "git rm -r file"
    

# Generated at 2022-06-14 10:23:32.740488
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm file',
                                   'fatal: not removing \'file\' recursively without -r\n')) == "git rm -r file"

# Generated at 2022-06-14 10:23:58.511457
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foobar',
                      'fatal: not removing \'foobar\' recursively '\
                      'without -r')
    assert get_new_command(command) == u'git rm -r foobar'