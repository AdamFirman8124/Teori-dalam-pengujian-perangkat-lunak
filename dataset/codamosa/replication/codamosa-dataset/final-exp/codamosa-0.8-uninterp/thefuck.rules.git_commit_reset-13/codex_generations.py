

# Generated at 2022-06-14 10:03:19.648365
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "First commit"',
                      "fatal: 'commit' is not a git command. See 'git --help'\n", True)
    assert get_new_command(command) == 'git reset HEAD~'


# Generated at 2022-06-14 10:03:22.329028
# Unit test for function match
def test_match():
    command = Command('commit', '')
    assert match(command)
    assert not match(Command('git', ''))



# Generated at 2022-06-14 10:03:28.695066
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '', '/bin/git')) == 'git reset HEAD~'


# Generated at 2022-06-14 10:03:31.100303
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add . && git commit -m "test"') == 'git reset HEAD~'

# Generated at 2022-06-14 10:03:36.995535
# Unit test for function match
def test_match():
	#Imitate the command line
	input_line = "git commit"
	command = Command(script=input_line)
	assert match(command)
	#Imitate the command line
	input_line = "git commit"
	command = Command(script=input_line)
	assert get_new_command(command)

# Generated at 2022-06-14 10:03:41.056358
# Unit test for function get_new_command
def test_get_new_command():
    command_1 = Command('git commit -a -m "test"', None)
    command_2 = Command('git add file.py', None)
    
    assert not match(command_2)
    assert get_new_command(command_1) == 'git reset HEAD~'

# Generated at 2022-06-14 10:03:44.601050
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('git commit abc', ''))
    assert not match(Command('git push', ''))

# Generated at 2022-06-14 10:03:47.032789
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '', '/tmp')) == 'git reset HEAD~'



# Generated at 2022-06-14 10:03:49.911041
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit -m 'New commit'") == "git reset HEAD~"

# Generated at 2022-06-14 10:03:57.202755
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -m test') == 'git reset HEAD~'
    assert get_new_command('git commit -a -m test') == 'git reset HEAD~'
    assert get_new_command('git commit -a --amend') == 'git reset HEAD~'
    assert get_new_command('git commit --amend -a') == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:01.100267
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit --allow-empty-message -m') == 'git reset HEAD~'

enabled_by_default = True

# Generated at 2022-06-14 10:04:04.000365
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit')) == 'git reset HEAD~'


# Generated at 2022-06-14 10:04:07.279047
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "toto"', 'asd')
    assert_equals(get_new_command(command), 'git reset HEAD~')

# Generated at 2022-06-14 10:04:11.781281
# Unit test for function match
def test_match():
    assert match(Command('git commit -m test', '', '/home/user/project'))
    assert not match(Command('git status', '', '/home/user/project'))
    assert not match(Command('commit -m test', '', '/home/user/project'))



# Generated at 2022-06-14 10:04:15.368788
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert match(Command('git commit --verbose', '', ''))
    assert not match(Command('git status', '', ''))

# Generated at 2022-06-14 10:04:17.824686
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "Another commit"'))
    assert not match(Command('git status -m "Another commit"'))


# Generated at 2022-06-14 10:04:21.923250
# Unit test for function match
def test_match():
    assert match(Command('git status', ''))
    assert match(Command('git commit', ''))
    assert match(Command('git add . && git commit -a', ''))
    assert not match(Command('git s', ''))



# Generated at 2022-06-14 10:04:23.519053
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))


# Generated at 2022-06-14 10:04:25.897418
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit', '', None)
    assert(get_new_command(command) == 'git reset HEAD~')

# Generated at 2022-06-14 10:04:26.726957
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -a') == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:37.821921
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit --amend') == 'git reset HEAD~'
    assert get_new_command('git commit -am "test"') == 'git reset HEAD~'
    assert get_new_command('git commit -m "test"') == 'git reset HEAD~'
    assert get_new_command('git commit --amend -m "new message"') == 'git reset HEAD~'
    assert get_new_command('commit') == 'commit'

# Generated at 2022-06-14 10:04:40.063176
# Unit test for function get_new_command
def test_get_new_command():
    assert git_reset_head_is_a_valid_git_command().get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:45.029335
# Unit test for function match
def test_match():
    assert match(Command('git commit -a -m "a test"'))
    assert match(Command('git commit -am "a test"'))
    assert match(Command('git commit -a'))
    assert match(Command('git commit -a -v'))
    assert match(Command('git commit'))
    assert match(Command('git commit -v'))
    assert not match(Command('git commit --amend'))
    assert not match(Command('git push'))


# Unit tests for function get_new_command

# Generated at 2022-06-14 10:04:54.617734
# Unit test for function match
def test_match():
    assert (True == match(Command(script='git commit',
                                 stderr="error: failed to push some refs to 'git@github.com:mhinz/vim-signify.git'\n"
                                 "hint: Updates were rejected because the tip of your current branch is behind\n"
                                 "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                                 "hint: 'git pull ...') before pushing again.\n"
                                 "hint: See the 'Note about fast-forwards' in 'git push --help' for details.")))


# Generated at 2022-06-14 10:04:58.803964
# Unit test for function match
def test_match():
    assert match(Command(script='git commit -am "fix"'))
    assert match(Command(script='git commit --amend --no-edit'))
    assert not match(Command(script='commit -am "fix"'))



# Generated at 2022-06-14 10:05:00.938422
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'

# Generated at 2022-06-14 10:05:04.750506
# Unit test for function match
def test_match():
    with patch('thefuck.rules.git_commit_askpass_repo_hosting.git_support', return_value=True):
        assert match(Command('git commit', ''))
        assert not match(Command('git commit1', ''))

# Generated at 2022-06-14 10:05:07.375832
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m "Hello world"').script == 'git reset HEAD~'


# Generated at 2022-06-14 10:05:11.579001
# Unit test for function match
def test_match():
    assert match(Command('git commit file', ''))
    assert match(Command('git commit -m file', ''))
    assert not match(Command('git commit file -m ', ''))
    assert not match(Command('git commit --amend file', ''))


# Generated at 2022-06-14 10:05:11.998032
# Unit test for function get_new_command
def test_get_new_command():
    asser

# Generated at 2022-06-14 10:05:18.876682
# Unit test for function match
def test_match():
    assert match(Command('git commit', '',  ['Nothing to commit, working directory clean.']))
    assert not match(Command('git commit foo', '',  []))
    assert not match(Command('commit foo', ''))


# Generated at 2022-06-14 10:05:20.090220
# Unit test for function match
def test_match():
    assert(match(Command('git add a && git commit', '')))
    assert(not match(Command('git status', '')))


# Generated at 2022-06-14 10:05:23.767288
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', '', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit', '', '')) == 'git reset HEAD~'



# Generated at 2022-06-14 10:05:26.095366
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command("git commit") == 'git reset HEAD~')


# Generated at 2022-06-14 10:05:32.773195
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -m "New commit"') == 'git reset HEAD~'
    assert get_new_command('git commit -a') == 'git reset HEAD~'
    assert get_new_command('git commit -am "New commit"') == 'git reset HEAD~'
    assert get_new_command('git commit file.txt') == 'git reset HEAD~'
    assert get_new_command('git commit -m "New commit" file.txt') == 'git reset HEAD~'


# Generated at 2022-06-14 10:05:34.477124
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('commit', ''))


# Generated at 2022-06-14 10:05:38.117839
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit") == "git reset HEAD~"
    assert get_new_command("git commit -m") == "git reset HEAD~"



# Generated at 2022-06-14 10:05:41.285328
# Unit test for function match
def test_match():
    assert match(Command('git coomit -m "My commit"', ''))
    assert match(Command('git pull', '')) == False


# Generated at 2022-06-14 10:05:43.734044
# Unit test for function match
def test_match():
    command_git_status = Command("git status", "")
    command_git_commit = Command("git commit", "")

    assert match(command_git_status) is False
    assert match(command_git_commit) is True


# Generated at 2022-06-14 10:05:47.189538
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit m1', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit -m m1', '')) == 'git reset HEAD~'


# Generated at 2022-06-14 10:05:55.198697
# Unit test for function match
def test_match():
    assert match(Command('git add hello.txt; git commit -m "new commit"; git push'))
    assert not match(Command('gs'))
    assert not match(Command('git commit'))


# Generated at 2022-06-14 10:05:58.511671
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "Hello" --amend', '', '/tmp/')
    assert git_reset_HEAD_1.get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:01.891543
# Unit test for function match
def test_match():
    command = Command('git commit -m work', '', None)
    assert match(command)

    command = Command('git', '', None)
    assert not match(command)

# Generated at 2022-06-14 10:06:03.114862
# Unit test for function match

# Generated at 2022-06-14 10:06:06.164962
# Unit test for function match
def test_match():
    command = Command('git commit -m "commit message"')
    assert match(command)
    command = Command('commit')
    assert not match(command)



# Generated at 2022-06-14 10:06:09.773759
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(shell.from_string('git commit')) == 'git reset HEAD~'
    assert get_new_command(shell.from_string('git reset HEAD~')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:12.959270
# Unit test for function match
def test_match():
    # Should match command with 'commit'
    assert match(Command('git commit -m "mymessage"'))



# Generated at 2022-06-14 10:06:16.407090
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "Add more tests"'))
    assert not match(Command('git commit --amend'))
    assert not match(Command('git checkout -b new-branch origin/master'))


# Generated at 2022-06-14 10:06:18.739052
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git commit', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:25.387868
# Unit test for function match
def test_match():
    from thefuck.types import Command

    supported_command = Command('git commit',
                                'error: You did not specify any files to use...',
                                '')
    assert match(supported_command)

    unsupported_command = Command('git commit', '', '')
    assert not match(unsupported_command)


# Generated at 2022-06-14 10:06:31.468541
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '', ''))


# Generated at 2022-06-14 10:06:33.213029
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '/tmp'))


# Generated at 2022-06-14 10:06:36.053799
# Unit test for function match
def test_match():
    """ This function tests the function match """
    assert match(Command("git confict")) == False
    assert match(Command("git commit -m", "")) == True
    assert match(Command("git commit --m", "")) == True


# Generated at 2022-06-14 10:06:39.209684
# Unit test for function match
def test_match():
    assert match(Command('git commit', "Failed to commit!\n", 'git commit'))
    assert not match(Command('git commit', 'commit success!', 'git commit'))


# Generated at 2022-06-14 10:06:43.684486
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '', 0, False))
    assert match(Command('commit', '', '', 0, False))
    assert not match(Command('git status', '', '', 0, False))


# Generated at 2022-06-14 10:06:45.936293
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git commit abc', '')) == 'git reset HEAD~')

# Generated at 2022-06-14 10:06:49.053252
# Unit test for function match
def test_match():
    assert match(Command("git commit -m wrong", "", ""))
    assert not match(Command("git commmit -m wrong", "", ""))


# Generated at 2022-06-14 10:06:51.967255
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert match(Command('git commit -m'))
    assert not match(Command('git status'))


# Generated at 2022-06-14 10:06:56.395166
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git add;git commit') == 'git add;git reset HEAD~'
    assert get_new_command('git commit --amend') == 'git reset HEAD~'
    assert not get_new_command('git status')


# Generated at 2022-06-14 10:07:02.657481
# Unit test for function match
def test_match():
    assert(match(Command('commit -a', "git commit -a\nfatal: Not a git repository (or any of the parent directories): .git\n", ""))!=True)
    assert(match(Command('commit', "git commit -a\nfatal: Not a git repository (or any of the parent directories): .git\n", ""))!=True)
    assert(match(Command('commit -a', "git commit -a\nOn branch master\n", ""))==True)
    assert(match(Command('commit', "git add -u\nOn branch master\n", ""))==True)


# Generated at 2022-06-14 10:07:14.096244
# Unit test for function match
def test_match():
	assert match(Command('git commit'))
	assert not match(Command('git status'))


# Generated at 2022-06-14 10:07:15.792189
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit .') == 'git reset HEAD~'

# Generated at 2022-06-14 10:07:25.875719
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -a', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit -m foo', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit foo', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit -a --amend', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit -a --amend --no-edit', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:07:28.935987
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git commit -m')) == 'git reset HEAD~')
    assert(get_new_command(Command('git add foo && git commit -m')) == 'git reset HEAD~')

# Generated at 2022-06-14 10:07:33.572586
# Unit test for function match
def test_match():
    """
    Unit test for the function match
    """
    command = Command('git commit', '', '')
    assert match(command)
    command = Command('commit', '', '')
    assert not match(command)


# Generated at 2022-06-14 10:07:42.880516
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "git commit -m fixed bugs"',
                         'git commit -m fixed bugs\n',
                         '',
                         5)) is False
    assert match(Command('git commit -m "git commit -m fixed bugs"',
                         'git commit -m fixed bugs\n',
                         '',
                         1)) is False
    assert match(Command('git commit -m "git commit -m fixed bugs"',
                         'git commit -m fixed bugs\n',
                         '',
                         0)) is True
    assert match(Command('git commit -m "git commit -m fixed bugs"',
                         'git commit -m fixed bugs\n',
                         '',
                         10)) is True

# Generated at 2022-06-14 10:07:46.087404
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "Updates"', '', ''))
    assert match(Command('git commit -am "Updates"', '', ''))
    assert not match(Command('echo foo', '', ''))

# Generated at 2022-06-14 10:07:49.145788
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit', '/home/clement')
    assert get_new_command(command) == 'git reset HEAD~'


# Generated at 2022-06-14 10:07:51.355148
# Unit test for function match
def test_match():
    assert match(Command('git commit -a -m "Test"', '', ''))
    assert not match(Command('git log', '', ''))


# Generated at 2022-06-14 10:07:56.620253
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '/usr/bin/git'))
    assert match(Command('git commit message', '', '/usr/bin/git'))
    assert not match(Command('git log', '', '/usr/bin/git'))


# Generated at 2022-06-14 10:08:17.049890
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:08:21.830729
# Unit test for function match
def test_match():
    git_commands = ["git commit -m 'first commit'", "git commit", "git commit -m", "git commit -a -m 'fixed typo in README.md'"]
    for cmd in git_commands:
        assert match(command=Command(script=cmd))


# Generated at 2022-06-14 10:08:24.627314
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('commit', '', '/tmp')
    assert get_new_command(command) == 'git reset HEAD~'


# Generated at 2022-06-14 10:08:27.128815
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "test"')
    assert(get_new_command(command) == 'git reset HEAD~')

# Generated at 2022-06-14 10:08:29.238119
# Unit test for function get_new_command
def test_get_new_command():
    assert ('git reset HEAD~', get_new_command(Command('git commit', 'git commit')))



# Generated at 2022-06-14 10:08:33.243723
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert match(Command('git commit -m', ''))
    assert not match(Command('git status', ''))
    assert not match(Command('git branch', ''))


# Generated at 2022-06-14 10:08:35.273676
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:08:37.693449
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git commit -m "Some message"'
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:08:41.058374
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git status').script == 'git reset HEAD~'
    assert get_new_command('git add .').script == 'git add .'

# Generated at 2022-06-14 10:08:43.650996
# Unit test for function match
def test_match():
    assert match(Command('git commit -m test', '', ''))
    assert not match(Command('git add', '', ''))



# Generated at 2022-06-14 10:09:23.946154
# Unit test for function match
def test_match():
    assert match(Command('git commit -am "test"', ''))
    assert not match(Command('git status', ''))


# Generated at 2022-06-14 10:09:26.692991
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('git reset HEAD~', ''))


# Generated at 2022-06-14 10:09:30.962376
# Unit test for function match
def test_match():
    assert match(Command('commit', 'my.py'))
    assert not match(Command('commit', ''))
    assert not match(Command('re_commit', 'my.py'))

# Generated at 2022-06-14 10:09:34.261198
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit', '', '')
    new_command = get_new_command(command)
    assert new_command == 'git reset HEAD~'

# Generated at 2022-06-14 10:09:37.041869
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Commands('git commit -m "test"')) == 'git reset HEAD~'


# Generated at 2022-06-14 10:09:39.014763
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert not match(Command('git status'))


# Generated at 2022-06-14 10:09:41.060287
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -m "fix"')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:09:42.503752
# Unit test for function match
def test_match():
    command = Command('git commit')
    assert match(command)



# Generated at 2022-06-14 10:09:45.040160
# Unit test for function match
def test_match():
    #cmd = "commit -m 'message'"
    cmd = "git commit -m 'message'"
    assert match(Command(cmd))



# Generated at 2022-06-14 10:09:51.690736
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert match(Command('git commit a', '', ''))
    assert not match(Command('git commit a', '', ''))


# Generated at 2022-06-14 10:11:18.061452
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m "Initial commit"') == 'git reset HEAD~'
    assert get_new_command('git commit --amend -m "Initial commit"') == 'git reset HEAD~'
    assert get_new_command('git commit -am "Initial commit"') == 'git reset HEAD~'
    assert get_new_command('git commit -a -m "Initial commit"') == 'git reset HEAD~'
    assert get_new_command('git commit -am' + _any_symbol_policy) == 'git reset HEAD~'

# Generated at 2022-06-14 10:11:27.380854
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -a') == 'git reset HEAD~'
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -m') == 'git reset HEAD~'
    assert get_new_command('git commit --amend') == 'git reset HEAD~'
    assert get_new_command('git commit -a -m') == 'git reset HEAD~'
    assert get_new_command('git commit asdasd') == 'git reset HEAD~'
    assert get_new_command('git commit -m asdasd') == 'git reset HEAD~'
    assert get_new_command('git commit --amend -m') == 'git reset HEAD~'



# Generated at 2022-06-14 10:11:31.061180
# Unit test for function match
def test_match():
    assert_equal(match('git commit '), True)
    assert_equal(match('git commit file1 file2'), True)
    assert_equal(match('git add file1 file2'), False)


# Generated at 2022-06-14 10:11:39.735474
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '/git/commit/'))
    assert not match(Command('git', '', '/git/commit/'))
    assert not match(Command('git commit -m "blabla"', '', '/git/commit/'))


# Generated at 2022-06-14 10:11:44.737395
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))

# Generated at 2022-06-14 10:11:51.019522
# Unit test for function match
def test_match():
    match_output = match(Command("git commit"))
    assert match_output == True
    match_output = match(Command("git commit -m message"))
    assert match_output == True
    match_output = match(Command("git add ."))
    assert match_output == False
    match_output = match(Command("git config --global user.name \"your name\""))
    assert match_output == False


# Generated at 2022-06-14 10:11:53.941217
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -m "Simple test"')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:11:55.106470
# Unit test for function match

# Generated at 2022-06-14 10:11:59.884797
# Unit test for function match
def test_match():
    # Assert last command is matched
    command = Command("git add && git commit -m 'message'", "")
    assert match(command)
    # Assert last command is not matched
    command = Command("git commit -m 'message'", "")
    assert not match(command)


# Generated at 2022-06-14 10:12:02.159081
# Unit test for function match
def test_match():
    command_test = Command('git commit', 'echo "Message"')
    assert match(command_test) == True

