

# Generated at 2022-06-14 10:46:29.446879
# Unit test for function match
def test_match():
    assert match("git add main.py")
    assert not match("hg add main.py")


# Generated at 2022-06-14 10:46:34.905601
# Unit test for function match
def test_match():
    assert match(Command('git init', 'fatal: Not a git repository'))
    assert match(Command('spam', 'fatal: Not a git repository'))
    assert not match(Command('spam', 'fatal'))
    assert not match(Command('spam', 'fatal: git repository'))


# Generated at 2022-06-14 10:46:42.324899
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         'fatal: Not a git repository'
                         '(or any of the parent directories): .git\n'))

    assert match(Command('hg status', 'abort: no repository found'))

    assert not match(Command('git status', 'On branch master'))

    assert not match(Command('hg status', 'nothing to commit (working directory clean)'))

    assert not match(Command('ls a', ''))


# Generated at 2022-06-14 10:46:48.845793
# Unit test for function match
def test_match():
    assert match(Command('git not_a_git', ''))
    assert not match(Command('git not_a_git', 'Not a git repository'))
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('git commit', 'fatal: Not a git repository'))
    assert match(Command('git commit stuff', 'fatal: Not a git repository'))


# Generated at 2022-06-14 10:46:51.060143
# Unit test for function match
def test_match():
    actual = Command('git status', 'abort: no repository found')
    assert match(actual)


# Generated at 2022-06-14 10:46:55.484632
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('git status', '', ''))
    assert not match(Command('hg status', '', ''))
    assert not match(Command('svn status', '', ''))



# Generated at 2022-06-14 10:46:57.536508
# Unit test for function match
def test_match():
    assert match(Command(script = 'git pull'))


# Generated at 2022-06-14 10:47:00.817468
# Unit test for function match
def test_match():
    assert match(Command('git stash', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'fatal: Not a git repository'))



# Generated at 2022-06-14 10:47:05.833850
# Unit test for function match
def test_match():
    # True
    command = Command('git status')
    command.output = "fatal: Not a git repository"
    assert match(command)

    # False
    command = Command('git status')
    command.output = "fatal: Not a git repository"
    assert match(command) == False



# Generated at 2022-06-14 10:47:07.336466
# Unit test for function match
def test_match():
    command = Command('git commit')
    assert match(command)


# Generated at 2022-06-14 10:47:12.095274
# Unit test for function match
def test_match():
    command = Command('git push origin master', '', 'fatal: Not a git repository (or any of the parent directories): .git')
    assert match(command)



# Generated at 2022-06-14 10:47:18.552200
# Unit test for function match
def test_match():
    assert match(Command('git stash apply', ''))
    assert not match(Command('hg push', 'search: no matches found'))
    assert match(Command('hg diff', 'abort: no repository found'))
    assert not match(Command('hg pull', ''))
    assert match(Command('git config --global user.name', 'fatal: Not a git repository'))



# Generated at 2022-06-14 10:47:27.067013
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         'fatal: Not a git repository'
                         '(or any of the parent directories): .git'))
    assert match(Command('git status',
                         'fatal: Not a git repository'
                         '(or any of the parent directories): .hg'))
    assert not match(Command('git status',
                         'On branch master'
                         'nothing to commit, working directory clean'))
    assert not match(Command('hg status', 'abort: no repository found'))



# Generated at 2022-06-14 10:47:33.508980
# Unit test for function match
def test_match():
    output0 = 'fatal: Not a git repository'
    output1 = 'abort: no repository found'
    command0 = Command('git log', output0)
    command1 = Command('hg log', output1)
    assert match(command0)
    assert match(command1)



# Generated at 2022-06-14 10:47:38.381483
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('git status', 'On branch master'))
    assert not match(Command('hg status', 'stable'))

# Generated at 2022-06-14 10:47:49.050995
# Unit test for function match
def test_match():
    wrong_command = Command(script='git add main.py')
    wrong_command.output = 'fatal: Not a git repository'
    assert match(wrong_command)

    wrong_command = Command(script='git add main.py')
    wrong_command.output = 'Not a git repository'
    assert not match(wrong_command)

    wrong_command = Command(script='hg add main.py')
    wrong_command.output = 'Not a mercurial repository'
    assert not match(wrong_command)

    wrong_command = Command(script='hg add main.py')
    wrong_command.output = 'abort: no repository found'
    assert match(wrong_command)



# Generated at 2022-06-14 10:47:55.783074
# Unit test for function match
def test_match():
    assert match(Command('git st', wrong_scm_patterns['git']))
    assert match(Command('hg st', wrong_scm_patterns['hg']))
    assert not match(Command('git st', 'On branch master'))
    assert not match(Command('hg st', 'On branch master'))


# Generated at 2022-06-14 10:48:06.964423
# Unit test for function match
def test_match():
    _get_actual_scm.cache_clear()
    m_function = MagicMock(return_value='.git')
    _get_actual_scm.cache_clear(m_function)
    command = MagicMock(script_parts=['git', 'branch', '-a'], output='fatal: Not a git repository')
    assert match(command)
    command = MagicMock(script_parts=['git', 'commit', '--amend'], output='fatal: Not a git repository')
    assert match(command)
    command = MagicMock(script_parts=['git', 'status'], output='abort: no repository found')
    assert match(command)
    command = MagicMock(script_parts=['git', 'stash'], output='abort: no repository found')

# Generated at 2022-06-14 10:48:16.658052
# Unit test for function match
def test_match():
    assert match(Command(script='git clone',
                         stderr='fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command(script='git clone',
                             stderr='Cloning into \'vim-latex\'...'))
    assert match(Command(script='hg clone',
                         stderr='abort: no repository found in \'../.hg\''))
    assert not match(Command(script='hg clone',
                             stderr='pulling from https://vim.googlecode.com/hg'))

# Generated at 2022-06-14 10:48:20.286514
# Unit test for function match
def test_match():
    assert match('git status')
    assert match('hg status')

    assert not match('tar -zxvf ~/Downloads/foo.tar.gz')
    assert not match('ls -l')

# Generated at 2022-06-14 10:48:30.773417
# Unit test for function match
def test_match():
    assert match(Command(script='git pull origin master',
                         stderr='fatal: Not a git repository'))
    assert match(Command(script='hg pull origin master',
                         stderr='abort: no repository found'))
    assert not match(Command(script='git pull origin master',
                         stderr='abort: no repository found'))
    assert not match(Command(script='hg pull origin master',
                         stderr='fatal: Not a git repository'))


# Generated at 2022-06-14 10:48:42.848840
# Unit test for function match
def test_match():
    get_new_command = lambda command: get_new_command(command)

    # Test for git
    git_match_cmd = 'git status'
    git_match_result = match(Command(git_match_cmd, 'fatal: Not a git repository'))
    assert git_match_result is True

    # Test for mercurial
    mercurial_match_cmd = 'hg status'
    mercurial_match_result = match(Command(mercurial_match_cmd, 'abort: no repository found'))
    assert mercurial_match_result is True

    no_match_cmd = 'git remote'
    no_match_result = match(Command(no_match_cmd, 'Nothing'))
    assert no_match_result is False



# Generated at 2022-06-14 10:48:45.725102
# Unit test for function match
def test_match():
    command = Command('git status', wrong_scm_patterns['git'])
    assert match(command) == True


# Generated at 2022-06-14 10:48:48.751429
# Unit test for function match
def test_match():
    matches = match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('git status', 'fatal: Not a git repository'))



# Generated at 2022-06-14 10:48:50.874476
# Unit test for function match
def test_match():
    assert match(Command('git status', None, 'fatal: Not a git repository'))



# Generated at 2022-06-14 10:48:55.087546
# Unit test for function match
def test_match():
    command = Command('git status', 'fatal: Not a git repository')
    assert match(command)
    command = Command('git status', 'abort: no repository found')
    assert not match(command)


# Generated at 2022-06-14 10:49:01.431368
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git' \
                         ' repository (or any of the parent directories): .git'))
    assert not match(Command('git status', 'On branch master'))
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('hg status', 'On branch master'))



# Generated at 2022-06-14 10:49:05.592439
# Unit test for function match
def test_match():
    assert not match(Command('git push', '', stderr='fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command('git push', '', stderr=''))
    assert match(Command('git push', '', stderr='fatal: Not a git repository (or any of the parent directories): .git'))


# Generated at 2022-06-14 10:49:08.631150
# Unit test for function match
def test_match():
    match_output = match(Command('git status', 'fatal: Not a git repository',
        path='~'))
    assert match_output



# Generated at 2022-06-14 10:49:12.672940
# Unit test for function match
def test_match():
    command = Command('git commit',
        'fatal: Not a git repository (or any of the parent directories): .git')
    assert match(command)



# Generated at 2022-06-14 10:49:29.358347
# Unit test for function match
def test_match():
    command1 = Command('git commit', 'fatal: Not a git repository')
    assert match(command1) == True

    command2 = Command('git commit', 'fatal: Not a git repository')
    assert match(command2) == True

    command3 = Command('git commit', 'fatal: Not a git repository')
    assert match(command3) == True

    command4 = Command('git commit', 'fatal: Not a git repository')
    assert match(command4) == True

    command5 = Command('git commit', 'fatal: Not a git repository')
    assert match(command5) == True


# Generated at 2022-06-14 10:49:33.810478
# Unit test for function match
def test_match():
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('svn status', 'abort: no repository found'))


# Generated at 2022-06-14 10:49:34.921258
# Unit test for function match
def test_match():
    assert match('git branch')
    assert not match('hg branch')


# Generated at 2022-06-14 10:49:42.391278
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('git status', 'abort: no repository found'))
    assert not match(Command('git status', 'fatal: Not a git'))
    assert not match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('echo test', 'fatal: Not a git repository'))


# Generated at 2022-06-14 10:49:53.424342
# Unit test for function match
def test_match():
    #test for git
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('git status', 'fatal: Not a git repository (or any of the parent directories): .git'))
    #test for hg
    assert match(Command('hg status', 'abort: no repository found'))
    assert match(Command('hg status', 'abort: no repository found in /tmp/fool'))
    #test for svn
    assert not match(Command('svn status', 'svn: E155007: '))
    assert not match(Command('svn status', 'svn: E155007: '))


# Generated at 2022-06-14 10:50:01.080159
# Unit test for function match
def test_match():
    assert (match(Command('git status', 'fatal: Not a git repository'))
            == True)
    assert (match(Command('git status', 'no repository found'))
            == False)
    assert (match(Command('hg status', 'no repository found'))
            == True)
    assert (match(Command('hg status', 'no repository found'))
            == True)


# Generated at 2022-06-14 10:50:04.758592
# Unit test for function match
def test_match():
    command = Command('git push origin master', 'fatal: Not a git repository\n')
    assert match(command)
    command = Command('hg push origin master', 'abort: no repository found\n')
    assert match(command)


# Generated at 2022-06-14 10:50:08.328435
# Unit test for function match
def test_match():
    assert match('yes | ls')
    assert match('yes --help')
    assert match('echo abc | git')
    assert match('ls')
    assert match('watch -n 1 "ls -ls"')
    assert match('git fasdf')



# Generated at 2022-06-14 10:50:15.072279
# Unit test for function match
def test_match():
    assert match(Command('git branch', "fatal: Not a git repository"))
    assert not match(Command('git branch', "  master"))
    assert not match(Command('git branch', "  master"))

# Generated at 2022-06-14 10:50:21.716994
# Unit test for function match
def test_match():
    from thefuck.shells import shell
    assert match(Command('git status', 'fatal: Not a git repository', None))
    assert not match(Command('git status', 'nothing', None))

    assert match(Command('hg status', 'abort: no repository found', None))
    assert not match(Command('hg status', 'nothing', None))



# Generated at 2022-06-14 10:50:40.381608
# Unit test for function match
def test_match():
    # Unit testing for match function
    def set_output(output, script=None):
        command = Command(script, '') if script else Command('', '')
        command.output = output
        return command

    assert match(set_output('fatal: Not a git repository', 'git commit'))
    assert match(set_output('abort: no repository found', 'hg commit'))
    assert not match(set_output('fatal: Not a git repository', 'hg commit'))


# Generated at 2022-06-14 10:50:45.744504
# Unit test for function match
def test_match():
    # If the return value of match() is wrong
    assert match(command_run(u'merge master')) is False
    assert match(command_run(u'vim .gitignore')) is False

    # If the return value of match() is right
    assert match(command_run(u'git merge master')) is True
    assert match(command_run(u'hg merge master')) is True


# Generated at 2022-06-14 10:50:48.714404
# Unit test for function match
def test_match():
    command = Command('git add .', '', wrong_scm_patterns['git'], 1)
    assert match(command) == True


# Generated at 2022-06-14 10:50:55.301372
# Unit test for function match
def test_match():
        assert match(Command('git status', 'fatal: Not a git repository'))
        assert not match(Command('git status', 'On branch master'))
        assert not match(Command('hg status', 'abort: no repository found'))
        assert not match(Command('hg status', 'abort: Not a git repository'))
        assert match(Command('hg status', 'abort: no repository found'))


# Generated at 2022-06-14 10:51:05.311549
# Unit test for function match
def test_match():
    # Case 1: script_parts[0] == command.output
    assert match(Command('git', 'fatal: Not a git repository', 'git pull'))
    assert match(Command('hg', 'abort: no repository found', 'hg pull'))

    # Case 2: output = 'some string' + script_parts[0]
    assert match(Command('git', 'some string fatal: Not a git repository', 'git pull'))
    assert match(Command('hg', 'some string abort: no repository found', 'hg pull'))

    # Case 3: script_parts[0] == command.output + 'some string'
    assert match(Command('git', 'fatal: Not a git repository some string', 'git pull'))

# Generated at 2022-06-14 10:51:16.178025
# Unit test for function match
def test_match():
    command1 = Command('git status', 'fatal: Not a git repository')
    command2 = Command('git staus', 'fatal: Not a git repository')
    command3 = Command('hg staus', 'abort: no repository found')
    command4 = Command('hg status', 'abort: no repository found')
    assert match(command1)
    assert not match(command2)
    assert match(command3)
    assert not match(command4)


# Generated at 2022-06-14 10:51:19.312233
# Unit test for function match
def test_match():
    assert match(Command('git status'))
    assert not match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('hg status'))
    assert not match(Command('hg status', 'abort: no repository found'))


# Generated at 2022-06-14 10:51:26.788834
# Unit test for function match
def test_match():
    assert match('git commit -am "fuu"') == False
    assert match('hg commit -am "fuu"') == False
    # Actual git repo with git commit command
    assert match('git commit -am "fuu"') == False
    # Actual hg repo with git commit command
    assert match('git commit -am "fuu"') == False
    # Actual git repo with hg commit command
    assert match('hg commit -am "fuu"') == False
    # Actual hg repo with hg commit command
    assert match('hg commit -am "fuu"') == False
    # Neither hg nor git repo with hg commit command
    assert match('hg commit -am "fuu"')
    # Neither hg nor git repo with git commit command
    assert match('git commit -am "fuu"')


# Generated at 2022-06-14 10:51:29.697912
# Unit test for function match
def test_match():
    result = match(Command('git status', 'fatal: Not a git repository'))
    assert(result == True)


# Generated at 2022-06-14 10:51:31.468225
# Unit test for function match
def test_match():
    assert match(Command('git push', ''))
    assert match(Command('hg push', ''))



# Generated at 2022-06-14 10:51:58.935737
# Unit test for function match
def test_match():
    command = """
fatal: Not a git repository (or any of the parent directories): .git
    """
    wrong = Command('git status', output=command)
    right = Command('git status')
    assert match(wrong)
    assert not match(right)



# Generated at 2022-06-14 10:52:07.460928
# Unit test for function match
def test_match():
    expected_scm = 'git'
    script_parts = ['git', 'config', '--get', 'remote.origin.url']
    assert(match(script_parts) == True)

    expected_scm = 'git'
    script_parts = ['git', 'log']
    assert(match(script_parts) == True)

    expected_scm = 'hg'
    script_parts = ['hg', 'log']
    assert(match(script_parts) == True)

    expected_scm = 'hg'
    script_parts = ['hg', 'log', '-r', '20130606']
    assert(match(script_parts) == True)


# Generated at 2022-06-14 10:52:16.460718
# Unit test for function match
def test_match():
    assert match(Command('git push', '')) is True
    assert match(Command('hg push', '')) is True
    assert match(Command('git push', wrong_scm_patterns['git'])) is True
    assert match(Command('git push', wrong_scm_patterns['hg'])) is False
    assert match(Command('hg status', wrong_scm_patterns['hg'])) is True
    assert match(Command('hg status', wrong_scm_patterns['git'])) is False


# Generated at 2022-06-14 10:52:21.922560
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('git a', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command('hg status', 'abort: no repository found in /home/tylor/Downloads!'))
    assert not match(Command('hg status', ''))

# Generated at 2022-06-14 10:52:26.668430
# Unit test for function match
def test_match():
    assert not match(Command('git --version'))
    assert match(Command('git init', stderr='fatal: Not a git repository'))
    assert match(Command('git init', stderr='fatal: Not a git repository (or any of the parent directories): .git'))
    assert match(Command('hg init', stderr='abort: no repository found'))
    assert match(Command('hg init', stderr='abort: no repository found in ..'))


# Generated at 2022-06-14 10:52:30.224376
# Unit test for function match
def test_match():
    command = Command('git branch')
    command.script_parts = ['git', 'branch']
    command.output = 'fatal: Not a git repository'
    command.return_code = 1
    assert match(command)



# Generated at 2022-06-14 10:52:37.642080
# Unit test for function match
def test_match():
    # Wrong command
    assert not match(Command('wrong command', ''))
    assert not match(Command('wrong command', 'fatal: Not a git repository'))
    assert not match(Command('hg wrong command', 'fatal: Not a git repository'))
    assert not match(Command('hg wrong command', 'abort: no repository found'))

    # Wrong scm
    assert match(Command('git wrong command', 'fatal: Not a git repository'))
    assert match(Command('hg wrong command', 'abort: no repository found'))



# Generated at 2022-06-14 10:52:42.288794
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', ''))
    assert match(Command('hg status', 'abort: no repository found'))

# Generated at 2022-06-14 10:52:50.992321
# Unit test for function match
def test_match():
    ret = match(Command('git commit', 'fatal: Not a git repository'))
    assert ret == True

    ret = match(Command('hg commit', 'abort: no repository found'))
    assert ret == True

    ret = match(Command('git commit', 'fatal: Not a git repos'))
    assert ret == False

    ret = match(Command('hg commit', 'abort: no repo found'))
    assert ret == False

    ret = match(Command('hg commit', 'abort: no repository found'))
    assert ret == True


# Generated at 2022-06-14 10:53:03.734705
# Unit test for function match

# Generated at 2022-06-14 10:54:00.343332
# Unit test for function match
def test_match():
    command = 'git commit -m \'foo\''
    new_command = get_new_command(command)
    assert match(command, None) == True
    assert get_new_command(command) == u'hg commit -m \'foo\''



# Generated at 2022-06-14 10:54:02.801366
# Unit test for function match
def test_match():
    output = 'fatal: Not a git repository'
    assert match(Command(script='git', output=output))



# Generated at 2022-06-14 10:54:06.855181
# Unit test for function match
def test_match():
    # match -> wrong SCM
    assert(match(Command("git commit", "fatal: Not a git repository")) == True)
    # match -> correct SCM
    assert(match(Command("git commit", "On branch master")) == False)


# Generated at 2022-06-14 10:54:13.255367
# Unit test for function match
def test_match():
    def get_output(scm):
        if scm == 'git':
            return '''fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.'''
        elif scm == 'hg':
            return '''error: no repository found in '/Users/mmozg/Dev/python/simple_uploader' (.hg not found)!'''

    def get_command(scm):
        return Command('ls -al', get_output(scm), '', 1)

    for path, scm in path_to_scm.items():
        with PatchedEnv({'PWD': '/Users/mmozg/Dev/python/simple_uploader'}):
            assert match(get_command(scm))



# Generated at 2022-06-14 10:54:15.190031
# Unit test for function match
def test_match():
    assert match(Command(script='git foo', output='fatal: Not a git repository'))
    assert not match(Command(script='git foo', output='bar'))



# Generated at 2022-06-14 10:54:17.241192
# Unit test for function match
def test_match():
    output = u'fatal: Not a git repository (or any of the parent directories): .git'
    assert match(Command(script='git', output=output))


# Generated at 2022-06-14 10:54:25.940812
# Unit test for function match
def test_match():
    assert match(Command('git', 'fatal: Not a git repository'))
    assert match(Command('git', 'fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command('git', 'Nothing to commit, working directory clean'))
    assert match(Command('hg', "abort: no repository found in '/home/user' (.hg not found)"))
    assert not match(Command('hg', "abort: no repository found (.hg not found)"))


# Generated at 2022-06-14 10:54:28.209139
# Unit test for function match
def test_match():
    assert match(Command(script='git status',
                         stderr='fatal: Not a git repository'))



# Generated at 2022-06-14 10:54:31.186224
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', ''))

# Unit tests for function get_new_command

# Generated at 2022-06-14 10:54:36.423114
# Unit test for function match
def test_match():
    # Test that a valid command output is caught
    assert match(Command('git rebase master', 'fatal: Not a git repository'))
    # Test that a command that is not in the wrong scm is not caught
    assert not match(Command('git rebase master', 'fatal: Not a hg repository'))
    # Test that command that aren't even in the wrong scm are not caught
    assert not match(Command('hg rebase master', 'fatal: Not a git repository'))
