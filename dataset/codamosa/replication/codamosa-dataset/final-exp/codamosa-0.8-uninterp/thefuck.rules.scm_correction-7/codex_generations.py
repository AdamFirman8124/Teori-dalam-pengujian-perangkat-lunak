

# Generated at 2022-06-14 10:46:24.585278
# Unit test for function match
def test_match():
    if match(Command("git branch", "fatal: Not a git repository")):
        print("git match")

test_match()


# Generated at 2022-06-14 10:46:30.801517
# Unit test for function match
def test_match():
    command = Command('git status', 'fatal: Not a git repository')
    assert not match(command)

    command = Command('git status', 'fatal: Not a git repository', '', None, 'git')
    assert match(command)


# Generated at 2022-06-14 10:46:39.895635
# Unit test for function match
def test_match():
    assert match(Command('git checkout foo', wrong_scm_patterns['git'], None, None, None))
    assert match(Command('hg checkout foo', wrong_scm_patterns['hg'], None, None, None))
    assert not match(Command('svn checkout foo', wrong_scm_patterns['git'], None, None, None))
    assert not match(Command('git checkout foo', '', None, None, None))
    assert not match(Command('hg checkout foo', '', None, None, None))
    assert not match(Command('svn checkout foo', '', None, None, None))


# Generated at 2022-06-14 10:46:46.482314
# Unit test for function match
def test_match():
    assert match(Command('git status', 'git: \'stauts\' is not a git command. See \'git --help\'.'))
    assert match(Command('git branch', 'git: \'branc\' is not a git command. See \'git --help\'.'))

    assert not match(Command('hg status', 'abort: no repository found!'))
    assert not match(Command('hg branch', 'abort: no repository found!'))

    assert not match(Command('svn status', 'svn: \'stauts\' is not a svn command. See \'svn --help\'.'))
    assert not match(Command('svn branch', 'svn: \'branc\' is not a svn command. See \'svn --help\'.'))


# Generated at 2022-06-14 10:46:59.034424
# Unit test for function match
def test_match():
    # Existing SCM in shell
    assert match(Command('git', 'fatal: Not a git repository'))
    assert match(Command('hg', 'abort: no repository found'))
    assert match(Command('git', 'abort: no repository found'))
    assert match(Command('hg', 'fatal: Not a git repository'))

    # No SCM in shell
    assert not match(Command('git', 'fatal: Not a git repository', ''))
    assert not match(Command('hg', 'abort: no repository found', ''))

    # Existing SCM in shell, but not in current directory
    assert not match(Command('git', ''))
    assert not match(Command('hg', ''))

    # Wrong error
    assert not match(Command('git', 'fatal: No remote'))
   

# Generated at 2022-06-14 10:47:10.284497
# Unit test for function match
def test_match():
	assert match(u"git branch") == False # no git repo
	assert match(u"git status") == True # no git repo but other git command
	assert match(u"git add") == True # no git repo but other git command
	assert match(u"git stash") == False # no git repo but stash
	assert match(u"git diff") == True # no git repo but other git command
	assert match(u"git log") == True # no git repo but other git command
	assert match(u"git rm") == True # no git repo but other git command
	assert match(u"git mv") == True # no git repo but other git command
	assert match(u"git config") == True # no git repo but other git command
	assert match(u"git checkout") == False # no git repo but other git command

# Generated at 2022-06-14 10:47:14.737547
# Unit test for function match
def test_match():
    # Check if the command is matched by the plugin
    assert match(Command('gits status', 'fatal: Not a git repository'))

    # Check if the command is not matched by the plugin
    assert not match(Command('status', ''))

# Generated at 2022-06-14 10:47:17.401517
# Unit test for function match
def test_match():
    wrong_command = Command('git status', wrong_scm_patterns['git'])
    assert match(wrong_command)


# Generated at 2022-06-14 10:47:24.366330
# Unit test for function match
def test_match():
    assert not match(Command('git status', '', '', 1, ''))
    assert match(Command('git status', 'fatal: Not a git repository', '', 1, ''))
    assert match(Command('hg status', 'abort: no repository found', '', 1, ''))
    assert not match(Command('hg status', '', '', 1, ''))



# Generated at 2022-06-14 10:47:30.910708
# Unit test for function match
def test_match():
    # Output contains wrong SCM error
    assert match(Command('git stash',
                 'fatal: Not a git repository')) is True
    # Output does not contain wrong SCM error
    assert match(Command('git stash',
                 '')) is False
    # Output contains wrong SCM error
    assert match(Command('hg stash',
                 'abort: no repository found')) is True
    # Output does not contain wrong SCM error
    assert match(Command('hg stash',
                 '')) is False


# Generated at 2022-06-14 10:47:37.757883
# Unit test for function match
def test_match():
    assert match(Command('git commit -m foo', 'fatal: Not a git repository'))
    assert match(Command('hg commit', 'abort: no repository found'))
    assert not match(Command('git commit -m foo'))
    assert not match(Command('hg commit'))


# Generated at 2022-06-14 10:47:41.008123
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         wrong_scm_patterns['git']))
    assert not match(Command('git status', 'On branch master'))

# Generated at 2022-06-14 10:47:49.108686
# Unit test for function match
def test_match():
    fn_with_git_cmd         = Command('git status', 'fatal: Not a git repository')
    fn_with_git_cmd_output  = match(fn_with_git_cmd)
    assert fn_with_git_cmd_output == True

    fn_without_git_cmd      = Command('git status', 'fatal: Not a git  repository')
    fn_without_git_cmd_output = match(fn_without_git_cmd)
    assert fn_without_git_cmd_output == False

# Generated at 2022-06-14 10:47:51.645817
# Unit test for function match
def test_match():
    assert match("git status")
    assert not match("ls")
    assert match("hg status")
    assert not match("git status")


# Generated at 2022-06-14 10:47:59.196816
# Unit test for function match
def test_match():
    assert match(Command(script='git commit',
                         output='fatal: Not a git repository'))
    assert not match(Command(script='git commit',
                             output='fatal: Not a hg repository'))
    assert not match(Command(script='hg commit', output='asdf'))
    assert match(Command(script='hg commit', output='abort: no repository found'))
    assert not match(Command(script='echo', output=''))


# Generated at 2022-06-14 10:48:04.591191
# Unit test for function match
def test_match():
    assert not match(Command('git status', ''))
    assert not match(Command('hg status', ''))
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('hg status', 'abort: no repository found'))

# Generated at 2022-06-14 10:48:11.001277
# Unit test for function match
def test_match():
    # Git
    assert match(Command('git', '', 'fatal: Not a git repository'))
    assert not match(Command('git', '', 'git: \'status\' is not a git command'))
    # Mercurial
    assert match(Command('hg', '', 'abort: no repository found'))
    assert not match(Command('hg', '', 'syntax: hg push [-f] [-r REV]... [--] DEST'))

# Generated at 2022-06-14 10:48:16.180123
# Unit test for function match
def test_match():
    assert match(Command(script='git',output='fatal: Not a git repository')) == True
    assert match(Command(script='hg',output='abort: no repository found')) == True
    assert match(Command(script='hg',output='abort: no repository found')) != False


# Generated at 2022-06-14 10:48:25.985049
# Unit test for function match
def test_match():
    for scm in wrong_scm_patterns:
        assert match(Command('git', 'fatal: Not a git repository'))
        assert match(Command('git', 'git: \'status\' is not a git command. See \'git --help\'.'))
        assert match(Command('hg', 'abort: no repository found'))
        assert match(Command('hg', 'hg: unknown command \'stauts\''))
        assert not match(Command('hg', 'foo'))
        assert not match(Command('git', 'foo'))


# Generated at 2022-06-14 10:48:30.979189
# Unit test for function match
def test_match():
    from thefuck.rules.wrong_scm import match
    assert match(type('command', (object,), {'script_parts': ['git', 'commit'],
        'output': 'fatal: Not a git repository (or any of the parent directories): .git\n', 'stderr': "", 'stdout': ''}))


# Generated at 2022-06-14 10:48:37.741207
# Unit test for function match
def test_match():
    assert not match(Command(script='git', stderr='fatal: Not a git repository'))
    assert match(Command(script='hg', stderr='abort: no repository found'))

# Generated at 2022-06-14 10:48:39.353400
# Unit test for function match
def test_match():
    assert match(Command('git diff'))



# Generated at 2022-06-14 10:48:49.371999
# Unit test for function match
def test_match():
    output_from_hg = '''abort: no repository found in '/home/juan/XXXXX' (.hg not found)
abort: no repository found in '/home/juan/XXXXX' (.hg not found)'''
    output_from_git = 'fatal: Not a git repository (or any of the parent directories): .git'
    cmd = Command('hg clone XXXXX',output_from_hg)
    cmd_git = Command('git clone XXXXX',output_from_git)
    assert match(cmd)
    assert match(cmd_git)


# Generated at 2022-06-14 10:49:02.509492
# Unit test for function match
def test_match():
    command = Command(script='git status', output='fatal: Not a git repository')
    assert match(command)

    command = Command(script='hg status', output='abort: no repository found')
    assert match(command)

    command = Command(script='git status', output='fatal: Not a git repository (not in a git repo)')
    assert match(command)

    command = Command(script='hg status', output='abort: Not a git repository (not in a git repo)')
    assert match(command)

    command = Command(script='git status', output='fatal: Not a git repositor, that is good. We are a hg repo')
    assert match(command)

    command = Command(script='hg status', output='abort: no repository found, that is good. We are a git repo')


# Generated at 2022-06-14 10:49:10.626846
# Unit test for function match
def test_match():
    command=Command('git diff', 'fatal: Not a git repository (or any of the parent directories): .git')
    assert match(command)

    command=Command('git diff', 'abort: no repository found')
    assert not match(command)

    command=Command('hg diff', 'abort: no repository found')
    assert match(command)

    command=Command('hg diff', 'fatal: Not a git repository (or any of the parent directories): .git')
    assert not match(command)


# Generated at 2022-06-14 10:49:14.193731
# Unit test for function match
def test_match():
    assert match(Command(script = 'git status'))
    assert match(Command(script = 'hg commit'))
    assert not match(Command())


# Generated at 2022-06-14 10:49:20.781333
# Unit test for function match
def test_match():
    assert match(Command('git', 'status'))
    assert match(Command('git', 'status', '--haha'))
    assert match(Command('hg', 'status'))
    assert match(Command('hg', 'status', '--haha'))
    assert not match(Command('svn', 'status'))
    assert not match(Command('git', 'commi'))
    assert not match(Command('hg', 'commi'))
    

# Generated at 2022-06-14 10:49:28.542900
# Unit test for function match
def test_match():
    # Test case of git error
    assert match(Command('git init', 'fatal: Not a git repository')) == True
    assert match(Command('git init', 'hello world')) == False
    # Test case of hg error
    assert match(Command('hg init', 'abort: no repository found')) == True
    assert match(Command('hg init', 'hello world')) == False


# Generated at 2022-06-14 10:49:32.813563
# Unit test for function match
def test_match():
    output = "fatal: Not a git repository (or any of the parent directories): .git\n"
    command = Command('fatal: Not a git repository (or any of the parent directories): .git\n', None)
    assert match(command)


# Generated at 2022-06-14 10:49:34.554151
# Unit test for function match
def test_match():
    new_command = Command('git command --option', '')
    assert match(new_command)


# Generated at 2022-06-14 10:49:42.436979
# Unit test for function match
def test_match():
    assert match(Command('git', 'Not a git repository'))
    assert not match(Command('git', 'Not a git repository', './test/test1'))
    assert match(Command('hg', 'abort: no repository found'))
    assert not match(Command('hg', 'abort: no repository found', './test/test1'))


# Generated at 2022-06-14 10:49:44.140757
# Unit test for function match
def test_match():
    command = Command('git commit', 'fatal: Not a git repository')
    assert match(command) == True

# Generated at 2022-06-14 10:49:48.730848
# Unit test for function match
def test_match():
    wrong_command = Command("git status", "fatal: Not a git repository")
    assert match(wrong_command)

# Generated at 2022-06-14 10:49:52.258589
# Unit test for function match
def test_match():
    assert match(Command('git stash save',
                         'fatal: Not a git repository',
                         ''))
    assert not match(Command('git stash save',
                             '',
                             ''))



# Generated at 2022-06-14 10:50:00.153639
# Unit test for function match
def test_match():
    assert match(Command('git status', 'error: Not a git repository',
                         '')) == True
    assert match(Command('git status', 'fatal: Not a git repository',
                         '')) == True
    assert match(Command('hg status', 'error: Not a hg repository',
                         '')) == True
    assert match(Command('hg status', 'abort: no repository found',
                         '')) == True
    assert match(Command('git status', 'error: Not a git repository',
                         '')) == True


# Generated at 2022-06-14 10:50:04.757638
# Unit test for function match
def test_match():
    command = Command('git branch')
    assert match(command)
    assert get_new_command(command) == 'hg branch'

    command = Command('git log --oneline')
    assert match(command)
    assert get_new_command(command) == 'hg log --oneline'

# Generated at 2022-06-14 10:50:11.077497
# Unit test for function match
def test_match():
    assert match(Command(script='git commit',
                         output='fatal: Not a git repository')) == True
    assert match(Command(script='git commit',
                         output='abort: no repository found')) == False
    assert match(Command(script='hg commit',
                         output='fatal: Not a git repository')) == False
    assert match(Command(script='hg commit',
                         output='abort: no repository found')) == True

# Generated at 2022-06-14 10:50:18.016258
# Unit test for function match
def test_match():
    assert match(Command('git commit',
                         'fatal: Not a git repository', '', 0))
    assert not match(Command('git commit', '', '', 1))

    assert match(Command('hg push',
                         'abort: no repository found', '', 0))
    assert not match(Command('hg push', '', '', 1))

# Generated at 2022-06-14 10:50:28.668745
# Unit test for function match
def test_match():
    assert not match(Command('git branch', ''))
    assert not match(Command('git branch', 'On branch master'))
    assert not match(Command('git branch', 'fatal: Not a git repository'))
    assert not match(Command('git branch', 'abort: no repository found'))
    assert match(Command('git branch', 'fatal: Not a git repository (or any parent directory): .git'))
    assert match(Command('git branch', 'fatal: Not a git repository (or any of the parent directories): .git'))

    assert not match(Command('hg branch', ''))
    assert not match(Command('hg branch', 'abort: no repository found'))
    assert not match(Command('hg branch', 'fatal: Not a git repository'))

# Generated at 2022-06-14 10:50:34.017598
# Unit test for function match
def test_match():
    assert match(Command('git rev-parse --abbrev-ref HEAD',
                         'fatal: Not a git repository')) == True
    assert match(Command('hg push origin master',
                         'abort: no repository found')) == True
    assert match(Command('git status',
                         'On branch master')) == False

# Generated at 2022-06-14 10:50:42.181523
# Unit test for function match
def test_match():
    assert match(Command(script = "git",
             stdout = wrong_scm_patterns['git'])) # Wrong scm


# Generated at 2022-06-14 10:50:48.717954
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'fatal: Not a git repository'))
    assert not match(Command('git add .', 'something went wrong'))

    assert match(Command('hg add', 'abort: no repository found'))
    assert not match(Command('hg add', 'something went wrong'))



# Generated at 2022-06-14 10:50:55.029544
# Unit test for function match
def test_match():
    assert match(Command(script='git status',
                         output='fatal: Not a git repository'))
    assert not match(Command(script='git status',
                             output='On branch master'))
    assert match(Command(script='hg status',
                         output='abort: no repository found'))
    assert not match(Command(script='hg status',
                             output='no changes found'))



# Generated at 2022-06-14 10:51:01.546394
# Unit test for function match
def test_match():
    # No wrong scm pattern
    assert not match(Command('git status', ''))

    # Not in a repo
    assert not match(Command('git status', 'fatal: Not a git repository'))

    # In a repo
    assert match(Command('git status', 'On branch master\nYour branch is up-to-date with \'origin/master\'.\n\nnothing to commit, working tree clean'))


# Generated at 2022-06-14 10:51:09.374555
# Unit test for function match
def test_match():
    assert match(Command("git commit -m 'asd'", ""))
    assert not match(Command("git commit -m 'asd'", "", ""))
    assert not match(Command("hg commit -m 'asd'", ""))


# Generated at 2022-06-14 10:51:16.235492
# Unit test for function match
def test_match():
    # empty output
    command = Command('git')
    assert not match(command)
    
    # output from Mercurial
    command = Command('git', '', 'abort: no repository found')
    assert match(command) == True
    
    # output from Git
    command = Command('git', '', 'fatal: Not a git repository')
    assert match(command) == True


# Generated at 2022-06-14 10:51:19.347612
# Unit test for function match
def test_match():
    match = WrongScm().match
    assert not match(Command(script='git', output='git fatal'))
    assert match(Command(script='git', output='fatal: Not a git repository'))
    assert match(Command(script='git', output='fatal: Not a git repo'))

# Generated at 2022-06-14 10:51:22.113164
# Unit test for function match
def test_match():
    assert(match(Command('git status', 'fatal: Not a git repository')))
    assert(match(Command('hg status', 'abort: no repository found')))


# Generated at 2022-06-14 10:51:23.090706
# Unit test for function match
def test_match():
    command = 'gitt st'
    assert match(command)


# Generated at 2022-06-14 10:51:24.801646
# Unit test for function match
def test_match():
    command = Command(script='git commit -m',
                      stderr=wrong_scm_patterns['git'])
    assert match(command) is True

# Generated at 2022-06-14 10:51:35.123042
# Unit test for function match
def test_match():
    assert match(Command('git rebase --continue', 'fatal: Not a git repository'))
    assert not match(Command('git rebase --continue', 'asdf'))
    assert match(Command('hg commit', 'abort: no repository found'))
    assert not match(Command('hg commit', 'qwerty'))



# Generated at 2022-06-14 10:51:37.319596
# Unit test for function match
def test_match():
    assert match(Command('curl',
        output='fatal: Not a git repository'))

    assert not match(Command('git',
        output='usage: git [--version]'))


# Generated at 2022-06-14 10:51:41.782589
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository', path='~'))
    assert match(Command('hg status', 'abort: no repository found', path='~'))
    assert not match(Command('git status', 'fatal: Not a git repository', path='~/script_fuck/thefuck'))
    assert not match(Command('hg status', 'abort: no repository found', path='~/script_fuck/thefuck'))


# Generated at 2022-06-14 10:51:52.857068
# Unit test for function match
def test_match():
    def check_result(command, expected):
        command = Command(command)

        assert(match(command) == expected)
        assert(match(command) == expected)

    check_result(u'git commit',False)
    check_result(u'hg commit',False)
    check_result(u'git fetch',False)
    check_result(u'hg fetch',False)

    check_result(u'git commit',False)
    check_result(u'hg commit',False)
    check_result(u'git fetch',False)
    check_result(u'hg fetch',False)

    check_result(u'git commit',False)
    check_result(u'hg commit',False)
    check_result(u'git fetch',False)

# Generated at 2022-06-14 10:52:00.302292
# Unit test for function match
def test_match():
    assert Path('.git').is_dir() == True
    command = Command('git commit', '''
fatal: Not a git repository (or any of the parent directories): .git
    ''')
    assert match(command) == True

    command = Command('git commit', '''
fatal: Not a git repository (or any of the parent directories): .git
    ''')
    assert match(command) == True


# Generated at 2022-06-14 10:52:05.958857
# Unit test for function match
def test_match():
    assert match(Command('git status'))
    assert match(Command('git commit'))
    assert match(Command('git branch'))
    assert match(Command('hg status'))
    assert match(Command('hg commit'))
    assert match(Command('hg branch'))
    assert not match(Command('commit'))
    assert not match(Command('status'))


# Generated at 2022-06-14 10:52:15.032697
# Unit test for function match
def test_match():
    test_input = Command('git status')
    test_input.output = 'fatal: Not a git repository'
    assert match(test_input)
    test_input.output = 'abort: no repository found'
    assert not match(test_input)
    test_input = Command('hg status')
    test_input.output = 'abort: no repository found'
    assert match(test_input)
    test_input.output = 'fatal: Not a git repository'
    assert not match(test_input)


# Generated at 2022-06-14 10:52:22.660358
# Unit test for function match
def test_match():
    assert match(Command('git ls', 'fatal: Not a git repository'))
    assert match(Command('hg ls', 'abort: no repository found'))
    assert match(Command('git ls', 'fatal: Not a git repository\n'))
    assert not match(Command('git ls', 'fatal: Not a repository'))
    assert not match(Command('git ls', 'fatal: Not a git reposit'))
    assert not match(Command('hg ls', 'abort: no git repository found'))
    assert not match(Command('hg ls', 'abort: no repository found\n'))



# Generated at 2022-06-14 10:52:23.777553
# Unit test for function match
def test_match():
    command = Command('git push', wrong_scm_patterns['git'])
    assert match(command)



# Generated at 2022-06-14 10:52:27.294392
# Unit test for function match
def test_match():
    assert match(Command('git remote add origin https://github.com/nvbn/thefuck.git',
                         'fatal: Not a git repository (or any of the parent directories): .git\n'))
    assert not match(Command('git remote add origin https://github.com/nvbn/thefuck.git',
                             'fatal: remote origin already exists.\n'))

# Generated at 2022-06-14 10:52:51.190602
# Unit test for function match
def test_match():
    # If a command output contains patterns in the wrong_scm_patterns dict and
    # there is a path_to_scm pattern in the path, return true
    assert match(Command('git status', 'abort: no git repository') and \
                 _get_actual_scm() == 'hg')
    assert match(Command('hg commit', 'fatal: Not a hg repository') and \
                 _get_actual_scm() == 'git')

    # If a command output is not in the wrong_scm_patterns dict and there is a
    # path_to_scm pattern in the path, return false
    assert not match(Command('git status', '') and \
                     _get_actual_scm() == 'git')

# Generated at 2022-06-14 10:52:53.979553
# Unit test for function match
def test_match():
    assert match('git') == False
    assert match('hg') == False


# Generated at 2022-06-14 10:52:58.862152
# Unit test for function match
def test_match():
    assert match(Command('git', '', 'fatal: Not a git repository (or any of the parent directories): .git'))
    assert match(Command('hg', '', 'abort: no repository found'))
    assert not match(Command('hg', '', 'unrecognized command'))

# Generated at 2022-06-14 10:53:02.723747
# Unit test for function match
def test_match():
    # Test case without a wrong SCM
    assert not match(Command('git stash'))
    # Test case with a wrong SCM
    assert match(Command('hg add .',
                         output='fatal: Not a git repository'))


# Generated at 2022-06-14 10:53:06.261085
# Unit test for function match
def test_match():
    output = "fatal: Not a git repository (or any of the parent directories): .git"
    command = Command('git branch -a', output)
    assert match(command)


# Generated at 2022-06-14 10:53:11.944575
# Unit test for function match
def test_match():
    assert not match(Command('git branch', ''))
    assert not match(Command('hg branch', ''))
    assert match(Command('git branch', 'fatal: Not a git repository'))
    assert match(Command('hg branch', 'abort: no repository found'))



# Generated at 2022-06-14 10:53:17.028990
# Unit test for function match
def test_match():
    assert match('git commit')
    assert not match('git branch')

    # no git repository
    assert not match('hg branch')
    assert not match('hg clone')

    # git repository
    assert match('hg branch')
    assert match('hg branch')


# Generated at 2022-06-14 10:53:20.885552
# Unit test for function match
def test_match():
    assert match(Command('fatal: Not a git repository'))
    assert match(Command('abort: no repository found'))
    assert not match(Command('Not a git repository'))
    assert not match(Command('no repository found'))

# Generated at 2022-06-14 10:53:26.298288
# Unit test for function match
def test_match():
    wrong_command1 = Command('git something')
    wrong_command1.output = "fatal: Not a git repository"
    wrong_command2 = Command('hg something')
    wrong_command2.output = "abort: no repository found"
    assert (match(wrong_command1) == True)
    assert (match(wrong_command2) == True)


# Generated at 2022-06-14 10:53:32.030894
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', ''))
    assert not match(Command('hg help', 'abort: no repository found!'))
    assert not match(Command('hg help', ''))


# Generated at 2022-06-14 10:54:05.587737
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('git status', 'warning: push.default is unset'))


# Generated at 2022-06-14 10:54:10.565194
# Unit test for function match
def test_match():
    assert match(Command('git status',
        'fatal: Not a git repository', '/home/user/projects/project'))
    assert match(Command('hg status',
        'abort: no repository found', '/home/user/projects/project'))
    assert not match(Command('git status',
        'fatal: fake error', '/home/user/projects/project'))


# Generated at 2022-06-14 10:54:15.899775
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command('hg status', 'abort: no repository found ('))

# Generated at 2022-06-14 10:54:25.343676
# Unit test for function match
def test_match():
    commands = [
        Command('git commit -a', '', 'fatal: Not a git repository'),
        Command('hg ci', '', 'abort: no repository found'),
        Command('git status', '', '# On branch master'),
        Command('hg diff', '', 'HG: Not a Mercurial repository'),
    ]

    assert any(_get_actual_scm() == 'git' for _ in map(match, commands))
    assert any(_get_actual_scm() == 'hg' for _ in map(match, commands))


# Generated at 2022-06-14 10:54:27.723687
# Unit test for function match
def test_match():
    assert match('git status')
    assert not match('git-status')
    assert not match('git status')



# Generated at 2022-06-14 10:54:29.920409
# Unit test for function match
def test_match():
    command = Command("git status")
    command.run()
    assert match(command)


# Generated at 2022-06-14 10:54:42.491278
# Unit test for function match
def test_match():
    # Calling the function with a command return True if the command is the
    # wrong SCM command and there is actually a directory for another SCM in
    # the current path, otherwise return False.
    # See unit test for function _get_actual_scm for more details.
    # The values tested bellow are the ones needed to return True.
    mistaken_command = Command('git status', 'fatal: Not a git repository')
    real_scm = mistaken_command.script_parts[0]
    real_scm_wrong_pattern = wrong_scm_patterns[real_scm]
    assert(match(mistaken_command) is True)
    assert(mistaken_command.script == 'git status')
    assert(mistaken_command.script_parts[0] == 'git')

# Generated at 2022-06-14 10:54:47.747657
# Unit test for function match
def test_match():
    assert match(command='git commit') is False
    assert match(command='hg commit') is False
    assert match(command='hg commit', output='abort: no repository found') is True
    assert match(command='git commit', output='fatal: Not a git repository') is True


# Generated at 2022-06-14 10:54:59.889338
# Unit test for function match
def test_match():
    output_no_repo = "fatal: Not a git repository"
    output_wrong_repo = "fatal: Not a hg repository"
    script_wrong_repo = 'git commit'
    script_only_cmd = 'commit'
    script_no_repo = 'git commit'

    # Match function should find wrong scm's output
    assert match(Command(script_no_repo, output_no_repo))
    assert match(Command(script_no_repo, output_wrong_repo))
    assert match(Command(script_wrong_repo, output_wrong_repo))
    assert match(Command(script_only_cmd, output_wrong_repo))

    # Match function should NOT find wrong scm's output

# Generated at 2022-06-14 10:55:13.424280
# Unit test for function match
def test_match():
    command1 = Command('git pull',
                        'fatal: Not a git repository',
                        path='/home/josh/push/')
    command2 = Command('git pull',
                        'abort: no repository found',
                        path='/home/josh/push/')
    command3 = Command('git pull',
                        'abort: no repository found',
                        path='/home/josh/push/')
    command4 = Command('git pull',
                        'abort: no repository found',
                        path='/home/josh/push/.hg')
    command5 = Command('hg pull',
                        'fatal: Not a git repository',
                        path='/home/josh/push/')

# Generated at 2022-06-14 10:55:54.185612
# Unit test for function match
def test_match():
    assert match(Command('hg status',
                'abort: no repository found',
                'X:/Coding/Python/misc/fuckit/fuckit.py')) == False
    assert match(Command('git pull',
                'X:/Coding/Python/misc/fuckit/fuckit.py')) == False
    assert match(Command('git',
                'fatal: Not a git repository',
                'X:/Coding/Python/misc/fuckit/fuckit.py')) != False



# Generated at 2022-06-14 10:56:01.461240
# Unit test for function match
def test_match():
    assert match(Command('git', 'fatal: Not a git repository'))
    assert match(Command('git', 'fatal: Not a git repository (or any of the parent directories): .git'))
    assert match(Command('git', 'fatal: Not a git repository (or any of the parent directories): test/.git'))
    assert not match(Command('hg', 'abort: no repository found'))


# Generated at 2022-06-14 10:56:09.533774
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository', ''))
    assert match(Command('hg status', 'abort: no repository found', ''))
    assert not match(Command('svn status', 'abort: no repository found', ''))
    assert not match(Command('git status', 'fatal: Not a git repository', ''))
    assert not match(Command('hg status', 'abort: no repository found', ''))
    assert not match(Command('svn status', 'abort: no repository found', ''))
    assert not match(Command('git status', 'working directory clean', ''))
    assert not match(Command('hg status', 'working directory clean', ''))
    assert not match(Command('svn status', 'working directory clean', ''))



# Generated at 2022-06-14 10:56:14.037972
# Unit test for function match
def test_match():
    # For script git add .
    assert match(Command('git add .', 'fatal: Not a git repository'))
    # For script git commit .
    assert match(Command('git commit .', 'fatal: Not a git repository'))
    # Does not match the correct git script
    assert not match(Command('git status', '# On branch master'))
    # Does not match the correct hg script
    assert not match(Command('hg status', ''))


# Generated at 2022-06-14 10:56:20.238894
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository', None))
    assert not match(Command('git branch', None, None))
    assert match(Command('hg status', 'abort: no repository found', None))
    assert not match(Command('hg add', None, None))
    assert not match(Command('ls', None, None))


# Generated at 2022-06-14 10:56:26.983326
# Unit test for function match
def test_match():
    assert match(Command('git status',
        'fatal: Not a git repository')) == True

    assert match(Command('hg status',
        'abort: no repository found')) == True

    assert match(Command('git status',
        'On branch master')) == False

    assert match(Command('hg status',
        'Branch default not found')) == False
