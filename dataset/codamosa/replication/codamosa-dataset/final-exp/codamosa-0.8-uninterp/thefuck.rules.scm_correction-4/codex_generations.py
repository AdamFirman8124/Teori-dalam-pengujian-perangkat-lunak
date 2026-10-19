

# Generated at 2022-06-14 10:46:31.440855
# Unit test for function match
def test_match():
    command = Command('git init something')
    assert match(command)

    command = Command('git init something')
    assert not match(command)


# Generated at 2022-06-14 10:46:38.892114
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('git commit -m "test"', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'On branch master'))
    assert not match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('hg commit -m "test"', 'abort: no repository found'))
    assert not match(Command('hg status', 'no changes found'))

# Generated at 2022-06-14 10:46:42.994588
# Unit test for function match
def test_match():
    def _test_with_scm(scm):
        command = Command('svn st', wrong_scm_patterns[scm])
        assert match(command) == True

    _test_with_scm('git')
    _test_with_scm('hg')



# Generated at 2022-06-14 10:46:48.998486
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'fatal: Not a git repository (or any parent up to mount point /disk2)'))
    assert not match(Command('git add .', 'On branch master'))
    assert match(Command('hg push .', 'abort: no repository found in'))
    assert not match(Command('hg push .', 'remote: Counting objects: 3, done.'))

# Generated at 2022-06-14 10:46:58.882348
# Unit test for function match
def test_match():
    assert match(Command('git init', 'fatal: Not a git repository'))
    assert match(Command('git init', 'abort: no repository found'))
    assert match(Command('git init', 'abort: no repository found'))
    assert match(Command('hg init', 'abort: no repository found'))
    assert match(Command('hg init', 'fatal: Not a git repository'))
    assert not match(Command('hg init', 'abort: no repository found (or not yet a mercurial repository)'))
    assert not match(Command('git clone', 'abort: no repository found'))



# Generated at 2022-06-14 10:47:04.139585
# Unit test for function match
def test_match():
    assert match(Command('git status'))
    assert match(Command('hg status'))
    assert not match(Command('git branch'))
    assert not match(Command('hg path'))
    assert not match(Command('hg log', output='abort: unknown'))


# Generated at 2022-06-14 10:47:19.487141
# Unit test for function match
def test_match():
    assert match(Command('git commit -m wrong', 'fatal: Not a git repository'))
    assert match(Command('git commit -m wrong', 'abort: no repository found'))

    assert match(Command('hg commit -m wrong', 'fatal: Not a git repository'))
    assert match(Command('hg commit -m wrong', 'abort: no repository found'))

    assert not match(Command('git commit -m wrong', ''))
    assert not match(Command('git commit -m wrong', '...'))
    assert not match(Command('git commit -m wrong', 'fatal: Not a git repository\nfatal: Not a git repository'))
    assert not match(Command('git commit -m wrong', 'abort: no repository found\nabort: no repository found'))


# Generated at 2022-06-14 10:47:30.946091
# Unit test for function match
def test_match():
    # Unit test for scm is git, but folder is not a git repository
    test_script = 'git status'
    test_output = 'fatal: Not a git repository'
    assert match(Command(script=test_script, output=test_output))

    # Unit test for scm is git, but folder is a git repository
    test_script = 'git status'
    test_output = 'On branch master\n'
    assert not match(Command(script=test_script, output=test_output))

    # Unit test for scm is hg, but folder is not a hg repository
    test_script = 'hg status'
    test_output = 'abort: no repository found'
    assert match(Command(script=test_script, output=test_output))

    # Unit test for scm is hg, but folder

# Generated at 2022-06-14 10:47:35.004847
# Unit test for function match
def test_match():
    assert match(Command('git', '', 'fatal: Not a git repository'))
    assert match(Command('hg', '', 'abort: no repository found'))



# Generated at 2022-06-14 10:47:46.485655
# Unit test for function match
def test_match():
    assert match(Command('git branch', 'fatal: Not a git repository')) == True
    assert match(Command('git branch', 'fatal: Not a git repository\n')) == True
    assert match(Command('git branch', 'fatal: Not a git repository\n\n')) == True
    assert match(Command('git branch', '')) == False
    assert match(Command('hg branch', 'abort: no repository found')) == True
    assert match(Command('hg branch', 'abort: no repository found\n')) == True
    assert match(Command('hg branch', 'abort: no repository found\n\n')) == True
    assert match(Command('hg branch', '')) == False


# Generated at 2022-06-14 10:47:52.602507
# Unit test for function match
def test_match():
    wrong_git = Command("git status", "fatal: Not a git repository")
    wrong_hg = Command("hg status", "abort: no repository found")
    
    assert match(wrong_git)
    assert not match(wrong_hg)



# Generated at 2022-06-14 10:47:56.826000
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('hg status', 'abort: no repository found'))

# Generated at 2022-06-14 10:48:01.193749
# Unit test for function match
def test_match():
    # No match
    assert not match(Command(script='git status',))

    # Match
    from thefuck.types import Command
    assert match(Command(script='git status', output=u'fatal: Not a git repository (or any of the parent directories): .git\n'))

# Generated at 2022-06-14 10:48:03.492887
# Unit test for function match
def test_match():
    (True, True) == (match.__wrapped__(''), match.__wrapped__(''))

# Generated at 2022-06-14 10:48:05.634670
# Unit test for function match
def test_match():
    command = Command("git branch", "fatal: Not a git repository")
    assert match(command)

# Generated at 2022-06-14 10:48:10.727908
# Unit test for function match
def test_match():
    assert match(Command('git commit', 'fatal: Not a git repository'))
    assert match(Command('git commit', 'fatal: Not a git repository', '', 'git'))

    assert not match(Command('git commit', 'fatal: Not a git repository'))
    assert not match(Command('hg commit', 'fatal: Not a git repository', '', 'hg'))

# Generated at 2022-06-14 10:48:21.879533
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         'fatal: Not a git repository'))
    assert match(Command('git status',
                         'fatal: Not a git repository', '', ''))
    assert match(Command('git status', '', '',
                         'fatal: Not a git repository'))
    assert match(Command('git status', 'fatal: Not a git repository', '',
                         'fatal: Not a git repository'))
    assert match(Command('git status', '', '',
                         'fatal: Not a git repository', '', ''))
    assert match(Command('git status', '', 'fatal: Not a git repository', '',
                         ''))
    assert match(Command('git status', '', '',
                         'fatal: Not a git repository', '', ''))


# Generated at 2022-06-14 10:48:30.079413
# Unit test for function match
def test_match():
    assert match(Command(script=(u'wrong_scm',), output=u'fatal: Not a git repository'))
    assert match(Command(script=(u'wrong_scm',), output=u'abort: no repository found'))
    assert not match(Command(script=(u'git',), output=u'abort: no repository found'))
    assert not match(Command(script=(u'hg',), output=u'fatal: Not a git repository'))



# Generated at 2022-06-14 10:48:30.988047
# Unit test for function match
def test_match():
    pass

# Generated at 2022-06-14 10:48:37.327853
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('git status', 'On branch master'))
    assert not match(Command('hg status', '4 files changed'))


# Generated at 2022-06-14 10:48:48.858180
# Unit test for function match
def test_match():
    output = """
    fatal: Not a git repository (or any of the parent directories): .git
    """
    command = Command('git status', output)
    assert match(command)

    output1 = """
    abort: no repository found in '.' or '..'!
    """
    command1 = Command('hg status', output1)
    assert match(command1)


test_output = """
    abort: no repository found in '.' or '..'!
"""
test_command = Command('hg status', test_output)
test_new_command = get_new_command(test_command)

# Generated at 2022-06-14 10:49:00.598580
# Unit test for function match
def test_match():
    assert match(Command('git', '', 'fatal: Not a git repository'))

# Generated at 2022-06-14 10:49:05.702354
# Unit test for function match
def test_match():
    command_git_output = u'fatal: Not a git repository (or any of the parent directories): .git\n'
    command_hg_output = u'abort: no repository found!\n'

    command1 = Command('git status', command_git_output)
    command2 = Command('hg status', command_hg_output)

    assert match(command1)
    assert match(command2)


# Generated at 2022-06-14 10:49:16.635684
# Unit test for function match
def test_match():
    # One test for each possible return outcome from match
    # These tests evaluate the match function for git, but expect match to
    # return false for git. The function only returns true for a given
    # application if the error is for the wrong scm, not if it's just a regular
    # error. In other words, this test makes sure match doesn't return true if
    # no error is present or the error is not contextually related to the
    # wrong scm.
    assert_not_equals(match(Command('ls', '', 'ls: cannot access file: No such file or directory')), True)

# Generated at 2022-06-14 10:49:20.074408
# Unit test for function match
def test_match():
    assert Path('.git').is_dir()
    assert not Path('.hg').is_dir()
    assert match('git status')
    assert not match('hg status')



# Generated at 2022-06-14 10:49:23.343463
# Unit test for function match
def test_match():
    command = Command(script = 'hg diff',
                      output = 'abort: no repository found')
    assert match(command)



# Generated at 2022-06-14 10:49:26.888414
# Unit test for function match
def test_match():
    command = Command('git commit -m test', 'fatal: Not a git repository (or any of the parent directories): .git')
    _get_actual_scm.cache_clear()
    assert match(command)



# Generated at 2022-06-14 10:49:34.605855
# Unit test for function match
def test_match():
    for path, scm in path_to_scm.items():
        # Default behavior of the command
        output = [
            "bash: hg: command not found"
        ]
        command = Command("hg branch", output)
        assert not match(command)
        
        # Wrong SCM used, but we have already the correct one
        output = [
            "abort: no repository found in '/Users/mac/Documents/oss/data-analysis/analysis-python'"
        ]
        command = Command(scm + " status", output)
        assert match(command)



# Generated at 2022-06-14 10:49:37.063345
# Unit test for function match
def test_match():
    command = Command('git commit', 'fatal: Not a git repository')
    assert match(command)


# Generated at 2022-06-14 10:49:41.902180
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository', '', 3))
    assert match(Command('hg status', 'abort: no repository found', '', 3))
    assert not match(Command('git status', 'On branch master', '', 3))


# Generated at 2022-06-14 10:49:50.848085
# Unit test for function match
def test_match():
    assert match(Command('hg init', ''))
    assert match(Command('git init', ''))
    assert match(Command('git init xyz', ''))
    assert match(Command('git init xyz abc', ''))


# Generated at 2022-06-14 10:49:55.152667
# Unit test for function match
def test_match():
    assert not match(Command('git diff', '', 0))
    assert match(Command('git diff', 'fatal: Not a git repository', 0))
    assert not match(Command('hg diff', '', 0))
    assert match(Command('hg diff', 'abort: no repository found', 0))

# Generated at 2022-06-14 10:49:58.035026
# Unit test for function match
def test_match():
    command = Command('hg pwd', '')
    assert match(command)

    command = Command('git pwd', '')
    assert not match(command)



# Generated at 2022-06-14 10:50:02.999909
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('git commit', ''))
    assert not match(Command('git status', ''))


# Generated at 2022-06-14 10:50:15.082980
# Unit test for function match
def test_match():
    command_git_in_git_repo = Command('git status', 'fatal: Not a git repository')
    command_git_in_hg_repo = Command('git status', 'abort: no repository found')
    assert match(command_git_in_git_repo) == True
    assert match(command_git_in_hg_repo) == False

    command_hg_in_git_repo = Command('hg status', 'fatal: Not a git repository')
    command_hg_in_hg_repo = Command('hg status', 'abort: no repository found')
    assert match(command_hg_in_git_repo) == False
    assert match(command_hg_in_hg_repo) == True


# Generated at 2022-06-14 10:50:17.299801
# Unit test for function match
def test_match():
    assert match('git status')
    assert match('hg status')
    assert not match('svn status')


# Generated at 2022-06-14 10:50:19.161250
# Unit test for function match
def test_match():
   assert not match(Command('git status', 'fatal: Not a git repository'))


# Generated at 2022-06-14 10:50:28.026450
# Unit test for function match
def test_match():
    # test for correct scm name
    assert(match(Command('git status', 'fatal: Not a git repository')))
    assert(match(Command('hg status', 'abort: no repository found')))

    # test for incorrect scm name
    assert(not match(Command('git status', 'abort: no repository found')))
    assert(not match(Command('hg status', 'fatal: Not a git repository')))

    # test for no scm name
    assert(not match(Command('status', 'abort: no repository found')))
    assert(not match(Command('status', 'fatal: Not a git repository')))


# Generated at 2022-06-14 10:50:33.063338
# Unit test for function match
def test_match():
    command = 'git status'
    command.output = 'fatal: Not a git repository'
    assert match(command)
    command = 'hg status'
    command.output = 'fatal: Not a git repository'
    assert not match(command)


# Generated at 2022-06-14 10:50:41.775515
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository')) is True
    assert match(Command('git status', 'abort: no repository found')) is False
    assert match(Command('hg status', 'abort: no repository found')) is False
    assert match(Command('hg status', 'fatal: Not a git repository')) is False
    assert match(Command('hg status', 'abort: no repository found')) is True
    assert match(Command('hg status', 'fatal: Not a git repository')) is False


# Generated at 2022-06-14 10:50:50.995305
# Unit test for function match
def test_match():
	call = Command('git add .')
	call.output = 'fatal: Not a git repository'
	memoize._cache.clear()
	assert match(call) == True


# Generated at 2022-06-14 10:50:54.378591
# Unit test for function match
def test_match():
    assert match('hg log', 'doesntmatter') == True
    assert match('git log', 'doesntmatter') == False
    assert match('ls', 'doesntmatter') == False


# Generated at 2022-06-14 10:50:57.710910
# Unit test for function match
def test_match():
    command = Command('git commit -m "abc"')
    assert match(command)

test_get_new_command = Command('git commit -m "abc"')

# Generated at 2022-06-14 10:51:03.009326
# Unit test for function match
def test_match():
    
    # Git
    git_command = Command('git status', 'fatal: Not a git repository')
    assert match(git_command) == True
    
    # Mercurial
    hg_command = Command('hg status', 'abort: no repository found')
    assert match(hg_command) == True

# Generated at 2022-06-14 10:51:11.772226
# Unit test for function match
def test_match():
    assert match(Command('git branch', '', 'fatal: Not a git repository'))
    assert not match(Command('git branch', '', ''))
    assert match(Command('hg pull', '', 'abort: no repository found'))
    assert not match(Command('hg pull', '', ''))


# Generated at 2022-06-14 10:51:16.931373
# Unit test for function match
def test_match():
    assert match(Command('hg status', wrong_scm_patterns['hg'] + '\n'))
    assert not match(Command('hg status'))
    assert not match(Command('git status', wrong_scm_patterns['git'] + '\n'))


# Generated at 2022-06-14 10:51:24.594381
# Unit test for function match
def test_match():
    command = Command('git diff', 'fatal: Not a git repository')
    assert match(command)

    command = Command('git diff', 'tatal: Not a git repository')
    assert not match(command)

    command = Command('git diff', 'fatal: Not a git repository')
    assert match(command)

    command = Command('git diff', 'tatal: Not a git repository')
    assert not match(command)


# Generated at 2022-06-14 10:51:34.797808
# Unit test for function match
def test_match():
    assert match(Command(script='git',
                         stderr='fatal: Not a git repository',
                         env={'PWD': '/tmp/git'}))
    assert match(Command(script='hg',
                         stderr='abort: no repository found',
                         env={'PWD': '/tmp/hg'}))
    assert not match(Command(script='git',
                             stderr='fatal: Not a git repository',
                             env={'PWD': '/tmp'}))
    assert not match(Command(script='hg',
                             stderr='abort: no repository found',
                             env={'PWD': '/tmp'}))

# Generated at 2022-06-14 10:51:38.771578
# Unit test for function match
def test_match():
    assert match(Command('git status'))
    assert match(Command('hg book'))
    assert not match(Command('ls'))

# Generated at 2022-06-14 10:51:41.568888
# Unit test for function match
def test_match():
    command = Command('git status', u'fatal: Not a git repository')
    assert match(command)




# Generated at 2022-06-14 10:52:02.233978
# Unit test for function match
def test_match():
    assert not match(Command('git status', 'fatal: Not a git repository (or any of the parent directories): .git\n'))
    assert not match(Command('git status', 'fatal: Not a git repository (or any of the parent directories): .git'))
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('hg status', 'abort: no repository found!'))


# Generated at 2022-06-14 10:52:03.999008
# Unit test for function match
def test_match():
    command = Command("git status", "fatal: Not a git repository")
    assert match(command)

# Generated at 2022-06-14 10:52:06.302753
# Unit test for function match
def test_match():
    assert match(Command('git co foo bar', stderr='fatal: Not a git repository')) == True


# Generated at 2022-06-14 10:52:12.392702
# Unit test for function match
def test_match():
    assert match(Command('git status',
                        'fatal: Not a git repository (or any of the parent directories): .git',
                        ''))
    assert not match(Command('git status',
                        'On branch master\nYour branch is up-to-date with \'origin/master\'\nnothing to commit, working directory clean',
                        ''))

# Generated at 2022-06-14 10:52:15.497672
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'status'))


# Generated at 2022-06-14 10:52:17.508478
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert not match(Command('hg commit'))

# Generated at 2022-06-14 10:52:25.734813
# Unit test for function match
def test_match():
    actual_scm = _get_actual_scm()

    # Test 1: Verify that match returns true if the current directory is not
    # a git or hg repository and command is "git status"
    command = create_command('git status')
    assert match(command) == True
    # command = create_command('hg status')
    # assert match(command) == True
    # command = create_command('hg push')
    # assert match(command) == True

    # Test 2: Verify that match returns False if the current directory is
    # a git repository and command is "git status"
    # command = create_command('git status')
    # assert match(command) == False

    # Test 3: Test that match returns false if the current directory is not
    # a git repository and command is "hg status"
    # command

# Generated at 2022-06-14 10:52:27.079028
# Unit test for function match
def test_match():
    assert match(Command('git status', '/home/user'))
    assert not match(Command('hg status', '/home/user'))


# Generated at 2022-06-14 10:52:29.985338
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'up to date'))


# Generated at 2022-06-14 10:52:31.732853
# Unit test for function match
def test_match():
    command = Command("git push")
    assert match(command)


# Generated at 2022-06-14 10:52:58.862089
# Unit test for function match
def test_match():
    command = Command('git status', 'fatal: Not a git repository', [])
    assert match(command)
    command = Command('git status', 'Not a git repository', [])
    assert not match(command)



# Generated at 2022-06-14 10:53:01.850447
# Unit test for function match
def test_match():
    command = Command('./file', './file: line 1: syntax error near unexpected token `{', './file: line 1: `{')
    assert match(command)

# Generated at 2022-06-14 10:53:08.184788
# Unit test for function match
def test_match():
    assert match(Command('git some subcommands', 'git some subcommands\nfatal: Not a git repository'))
    assert match(Command('hg some subcommands', 'hg some subcommands\nabort: no repository found'))
    assert not match(Command('git some subcommands', 'git some subcommands'))
    assert not match(Command('hg some subcommands','hg some subcommands'))


# Generated at 2022-06-14 10:53:10.912046
# Unit test for function match
def test_match():
    command = Command("git", "This is not a git repository")
    assert match(command)


# Generated at 2022-06-14 10:53:15.180564
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', 'fatal: Not a git repository'))
    assert not match(Command('git commit', '', 'fatal: Not a hg repository'))


# Generated at 2022-06-14 10:53:24.786834
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'On branch master'))
    assert match(Command('git status', 'On branch master', '/path/to/git'))
    assert not match(Command('git status', 'On branch master', '/path/to/hg'))
    assert match(Command('hg status', 'abort: no repository found'))
    assert not match(Command('hg status', 'abort: search pattern not found'))
    assert match(Command('hg status', 'abort: no repository found', '/path/to/hg'))
    assert not match(Command('hg status', 'abort: no repository found', '/path/to/git'))


# Generated at 2022-06-14 10:53:29.795490
# Unit test for function match
def test_match():
    # mock the attributes of command
    command = DotDict({'script_parts': ['git', 'add', '.']})
    command.output = 'fatal: Not a git repository'

    assert match(command)



# Generated at 2022-06-14 10:53:34.390364
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert match(Command('git -v', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'fatal: Not a git repository'))
    

# Generated at 2022-06-14 10:53:36.823966
# Unit test for function match
def test_match():
    assert match(Command('git init', ''))
    assert not match(Command('git init', 'fatal: Not a git repository'))


# Generated at 2022-06-14 10:53:40.557263
# Unit test for function match
def test_match():
    assert match(Command('git status', ''))
    assert not match(Command('git status', 'On branch master\n'))
    assert not match(Command('git status', 'fatal: Not a git repository'))



# Generated at 2022-06-14 10:54:40.855170
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         'fatal: Not a git repository'))
    assert not match(Command('git status'))
    assert match(Command('hg status',
                         'abort: no repository found'))
    assert not match(Command('hg status'))

# Generated at 2022-06-14 10:54:45.899210
# Unit test for function match
def test_match():
    os.chdir(os.path.dirname(__file__))

    for cmd in ['git status', 'git', 'hg status', 'hg']:
        assert match(Command(cmd, ''))

    assert not match(Command('svn', ''))
    assert not match(Command('git clone ...', ''))

# Generated at 2022-06-14 10:54:57.192301
# Unit test for function match
def test_match():
    command = type('Command', (object,), 
                  {'script_parts': ['git', 'log'], 
                   'output': 'fatal: Not a git repository'})
    assert match(command)

    command = type('Command', (object,), 
                  {'script_parts': ['hg', 'status'], 
                   'output': 'abort: no repository found'})
    assert match(command)

    command = type('Command', (object,), 
                  {'script_parts': ['git', 'test'], 
                   'output': 'test: no such git command'})
    assert not match(command)

    command = type('Command', (object,), 
                  {'script_parts': ['hg', 'test'], 
                   'output': 'test: no such hg command'})
   

# Generated at 2022-06-14 10:55:01.803617
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'On branch master'))
    assert not match(Command('hg status', 'On branch master'))


# Generated at 2022-06-14 10:55:14.430748
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository'))
    assert not match(Command('git status', 'fatal: Not a git repository', '/home/ubu/'))
    assert match(Command('git status', 'fatal: Not a git repository', '/home/ubu/django/'))
    assert not match(Command('git status', 'fatal: Not a git repository', '/home/ubu/django/.hg/'))
    assert match(Command('hg add', 'abort: no repository found', '/home/ubu/'))
    assert not match(Command('hg add', 'abort: no repository found', '/home/ubu/django/'))

# Generated at 2022-06-14 10:55:24.079692
# Unit test for function match
def test_match():
    wrong_command = Command('git status', 'fatal: Not a git repository')
    assert match(wrong_command), 'Wrong git command'

    wrong_command = Command('hg status', 'abort: no repository found')
    assert match(wrong_command), 'Wrong hg command'

    wrong_command = Command('git status', 'Everything is perfect')
    assert not match(wrong_command), 'Wrong command'

    wrong_command = Command('hg status', 'Everything is perfect')
    assert not match(wrong_command), 'Wrong command'


# Generated at 2022-06-14 10:55:34.387769
# Unit test for function match
def test_match():
    from thefuck.rules.git_not_repo import match
    # correct function
    command = type('cmd', (object,), {
        'script': 'git status',
        'output': 'fatal: Not a git repository (or any of the parent directories): .git',
        'script_parts': ['git', 'status']
        })
    is_match = match(command)
    assert is_match is True
    # wrong function
    command = type('cmd', (object,), {
        'script': 'hg status',
        'output': 'abort: no repository found in /home/user/.config/thefuck' \
        '(.hg not found)!',
        'script_parts': ['hg','status']
        })
    is_match = match(command)
    assert is_match is True

#

# Generated at 2022-06-14 10:55:42.500356
# Unit test for function match
def test_match():
    assert match(command=Command('git', 'git: command not found')) == False
    assert match(command=Command('git', 'fatal: Not a git repository')) == False
    assert match(command=Command('hg', 'fatal: Not a git repository')) == False
    assert match(command=Command('git', 'fatal: Not a git repository')) == True
    assert match(command=Command('hg', 'abort: no repository found')) == True


# Generated at 2022-06-14 10:55:46.288716
# Unit test for function match
def test_match():

    # Call function get_actual_scm and the result is git
    command = Command('hg status', 'hg status')

    assert match(command)
    assert 'git status' == get_new_command(command)

# Generated at 2022-06-14 10:55:49.579038
# Unit test for function match
def test_match():
    assert match(Command('git status', 'fatal: Not a git repository (or any of the parent directories): .git\n'))
    assert match(Command('hg status', 'abort: no repository found!\n'))
    assert not match(Command('git status', 'On branch master\n'))
