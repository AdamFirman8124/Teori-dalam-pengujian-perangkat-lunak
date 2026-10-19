

# Generated at 2022-06-14 10:03:22.683861
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit --amend -m "Code file"') == 'git reset HEAD~'

# Generated at 2022-06-14 10:03:29.173874
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "test"')
    
    assert get_new_command(command) == 'git reset HEAD~'



# Generated at 2022-06-14 10:03:32.435121
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -a', '', '', '.git/index.lock: File exists')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:03:39.609285
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "message"',
        'error: failed to push some refs to \'ssh://git@...\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))



# Generated at 2022-06-14 10:03:41.992445
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit -m'first commmit'") == 'git reset HEAD~'

# Generated at 2022-06-14 10:03:53.663845
# Unit test for function get_new_command

# Generated at 2022-06-14 10:03:56.593288
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit --amend', '')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:00.148415
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git commit', stderr='error: empty commit message')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:04.721282
# Unit test for function match
def test_match():
    assert match(Command('a', 'b', 'c')) == False
    assert match(Command('git', 'add', 'c')) == False
    assert match(Command('git', 'commit', 'c')) == True


# Generated at 2022-06-14 10:04:06.524984
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:10.442803
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(script(""" git commit -m "Commit"
""")[0]) == 'git reset HEAD~'



# Generated at 2022-06-14 10:04:13.843489
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "bug fixed"', '',
        '')) is True
    assert match(Command('git add .', '', '')) is False


# Generated at 2022-06-14 10:04:15.042776
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'


# Generated at 2022-06-14 10:04:18.810622
# Unit test for function match
def test_match():
    assert match(Command('commit -m "some changes"', 
        '')) is True
    assert match(Command('git reset --soft HEAD~ ', '')) is False


# Generated at 2022-06-14 10:04:21.028434
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'


# Generated at 2022-06-14 10:04:23.677672
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit') != 'git reset HEAD'

# Generated at 2022-06-14 10:04:26.052185
# Unit test for function match
def test_match():
    """Match function should return true if there is a commit command"""
    assert match(Command('git commit', ''))



# Generated at 2022-06-14 10:04:28.281270
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(ommand.Command('git ciomit -m'))[0] == 'git reset HEAD~'
    assert g

# Generated at 2022-06-14 10:04:30.122552
# Unit test for function match
def test_match():
    command = Command(script='git commit -m "test"', output='None')
    assert match(command)


# Generated at 2022-06-14 10:04:35.722688
# Unit test for function match
def test_match():
    assert match(GitCommand(script='git commit'))
    assert not match(GitCommand(script='git push'))


# Generated at 2022-06-14 10:04:39.730740
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert not match(Command('git config'))



# Generated at 2022-06-14 10:04:41.791562
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -a', '')).script == 'git reset HEAD~'
    

# Generated at 2022-06-14 10:04:51.593937
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "Commit message"', "git commit -m 'Commit message'\nOn branch master\n\nInitial commit\n\nUntracked files:\n  (use \"git add <file>...\" to include in what will be committed)\n\n\t.gitignore\n\nnothing added to commit but untracked files present (use \"git add\" to track)"))
    assert not match(Command('git commit', "git commit -m 'Commit message'\nfatal: pathspec 'message'' did not match any files"))



# Generated at 2022-06-14 10:04:53.055755
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert not match(Command('git reset'))


# Generated at 2022-06-14 10:04:55.911414
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert match(Command('git commit --amend', '', ''))
    assert not match(Command('git', '', ''))


# Generated at 2022-06-14 10:05:00.573279
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert match(Command('git commit -m'))
    assert match(Command('git reset --hard HEAD'))

    assert not match(Command('cd git commit'))


# Generated at 2022-06-14 10:05:03.151485
# Unit test for function get_new_command
def test_get_new_command():
    output = get_new_command('git commit -m "Doing things"')
    assert 'git reset HEAD~' in output



# Generated at 2022-06-14 10:05:04.940350
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit').script == 'git reset HEAD~'

# Generated at 2022-06-14 10:05:09.444354
# Unit test for function match
def test_match():
    assert match(Command('commit'))
    assert match(Command('git commit'))
    assert match(Command('commit -m "message"'))
    assert match(Command('commit -a'))
    assert not match(Command('push'))

# Generated at 2022-06-14 10:05:15.587629
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -a') == 'git reset HEAD~'
    assert get_new_command('git commit --amend') == 'git reset HEAD~'



# Generated at 2022-06-14 10:05:27.057138
# Unit test for function get_new_command
def test_get_new_command():
    command_example = Command('git commit -F file.txt', 'my_file.txt\n# On branch master\n# Changes to be committed:\n#   (use "git reset HEAD <file>..." to unstage)\n#\n#   new file:   my_file.txt\n#')
    assert get_new_command(command_example) == 'git reset HEAD~'

# Generated at 2022-06-14 10:05:31.758250
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git reset HEAD~1' == get_new_command(MagicMock(script='git commit -m bla'))
    assert 'git reset HEAD~' == get_new_command(MagicMock(script='git commit -m bla bla'))

# Generated at 2022-06-14 10:05:35.891975
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -a -m "test"') == 'git reset HEAD'
    assert get_new_command('git commit -a -m "test"') != 'git reset HEAD~'

# Generated at 2022-06-14 10:05:37.610037
# Unit test for function match
def test_match():
    from thefuck.rules.git_reset_head_caret import match
    assert match("git commit --amend")

# Unit 

# Generated at 2022-06-14 10:05:39.783181
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '/bin/git'))
    assert not match(Command('git add', '', '/bin/git'))



# Generated at 2022-06-14 10:05:42.927493
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert not match(Command('git push'))

# Unit test function get_new_command

# Generated at 2022-06-14 10:05:45.826353
# Unit test for function match
def test_match():
    command = Command('git commit')
    assert match(command)
    command = Command('git log')
    assert not match(command)


# Generated at 2022-06-14 10:05:48.827553
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "foobar"', "Nothing to commit, working directory clean\n"))


# Generated at 2022-06-14 10:05:53.929706
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit") == "git reset HEAD~"
    assert get_new_command("git commit -m") == "git reset HEAD~"
    assert get_new_command("git commit -m \"commit message\"") == "git reset HEAD~"


# Generated at 2022-06-14 10:05:55.978955
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git commit') == 'git reset HEAD~'


# Generated at 2022-06-14 10:06:09.288331
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -m') == 'git reset HEAD~'


# Generated at 2022-06-14 10:06:14.238359
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -m "comment"') == 'git reset HEAD~'
    assert get_new_command('git commit') == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:17.222318
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '', ''))
    assert not match(Command('git pull', '', '', ''))


# Generated at 2022-06-14 10:06:18.688357
# Unit test for function match
def test_match():
    command = Command('git commit')
    assert match(command)
    

# Generated at 2022-06-14 10:06:22.955989
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -m "commit"') == 'git reset HEAD~'
    assert get_new_command('git commit --allow-empty -m "commit"') == 'git reset HEAD~'


# Generated at 2022-06-14 10:06:38.780891
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit --amend') == 'git reset HEAD~'
    assert get_new_command('git commit --date') == 'git reset HEAD~'
    assert get_new_command('git commit -m --amend') == 'git reset HEAD~'
    assert get_new_command('git commit -m --date') == 'git reset HEAD~'
    assert get_new_command('git commit -m --amend --signoff') == 'git reset HEAD~'
    assert get_new_command('git commit -m --date --signoff') == 'git reset HEAD~'

    # Function get_new_command should not be triggered by unrelated commands
    assert not get_new_command('git stash')
    assert not get_new_command('git checkout')
    assert not get_new_command('git diff')
   

# Generated at 2022-06-14 10:06:41.684046
# Unit test for function match
def test_match():
    assert match(Command(script = 'git commit -m "This is a test"'))
    # Unit test for function get_new_command

# Generated at 2022-06-14 10:06:43.837529
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '', ''))


# Generated at 2022-06-14 10:06:48.459156
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '', '/')) == 'git reset HEAD~'
    assert not get_new_command(Command('git commit -v', '', '/'))
    assert not get_new_command(Command('aptitude update', '', '/'))

# Generated at 2022-06-14 10:06:50.550659
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -m "test"', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:07:12.410286
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit -m 'test'") == 'git reset HEAD~'
    assert get_new_command("git commit") == 'git reset HEAD~'
    assert get_new_command("git commit -a -m 'test'") == 'git reset HEAD~'
    assert get_new_command("git commit -m 'test' 'test2'") == 'git reset HEAD~'
    assert get_new_command("pull && git commit -m 'test'") == 'pull && git reset HEAD~'
    assert get_new_command("git commit --amend") == 'git reset HEAD~'
    assert get_new_command("git commit -m 'test' -m 'test2'") == 'git reset HEAD~'


# Generated at 2022-06-14 10:07:13.784586
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '')) == 'git reset HEAD~'


# Generated at 2022-06-14 10:07:22.985143
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m test') == 'git reset HEAD~'
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -a') == 'git reset HEAD~'
    assert get_new_command('git commit -m') == 'git reset HEAD~'
    assert get_new_command('git commit -m -a') == 'git reset HEAD~'


# Generated at 2022-06-14 10:07:27.763850
# Unit test for function match
def test_match():
    assert match(Command('git add README.md'))
    assert match(Command('git add README.md', '', '', '', '', ''))
    assert not match(Command('git commit --amend'))
    assert not match(Command('git commit --amend', '', '', '', '', ''))


# Generated at 2022-06-14 10:07:29.557706
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "My commit message"')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:07:34.744466
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command('git commit') == 'git reset HEAD~')
    assert (get_new_command('git commit ') == 'git reset HEAD~')
    assert (get_new_command('git commit -m') == 'git reset HEAD~')



# Generated at 2022-06-14 10:07:36.870329
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add . && git commit') == 'git reset HEAD~'


# Generated at 2022-06-14 10:07:39.781963
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git comit -m "hello world"')
    assert get_new_command(command) == 'git reset HEAD~'


# Generated at 2022-06-14 10:07:41.923443
# Unit test for function match
def test_match():
    assert(match(script_klass(script='git commit')))
    assert(not match(script_klass(script='git add')))


# Generated at 2022-06-14 10:07:43.381673
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit', '', '')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:07:55.370804
# Unit test for function match
def test_match():
    # Assign
    from thefuck.rules.git_reset_commit import match
    # Act
    command = 'commit'
    new_command = match(command)
    # Assert
    assert new_command == 'git reset HEAD~'

# Generated at 2022-06-14 10:08:01.529795
# Unit test for function match
def test_match():
    assert match(ShellCommand('git commit', ''))
    assert match(ShellCommand('git commit -m "abc"', ''))
    assert match(ShellCommand('git commit -am "abc"', ''))
    assert not match(ShellCommand('git status', ''))
    assert not match(ShellCommand('commit', ''))


# Generated at 2022-06-14 10:08:05.598502
# Unit test for function match
def test_match():
    example_inputs = ['git commit', 'git add -A && git commit']
    for input in example_inputs:
        assert match(Command(script=input)) is True
    assert match(Command(script='git status')) is False


# Generated at 2022-06-14 10:08:07.080140
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('git log', ''))



# Generated at 2022-06-14 10:08:10.121290
# Unit test for function match
def test_match():
    match_single_command = match(Command('git commit -m "message"'))
    match_sequence_command = match(Command('git commit -m "message" && git commit -m "message"'))
    assert match_single_command
    assert match_sequence_command



# Generated at 2022-06-14 10:08:12.831154
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -a') == 'git reset HEAD~'


# Generated at 2022-06-14 10:08:17.000771
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('git commit')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit -m "hello"')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit -a -m "hello"')) == 'git reset HEAD~'


# Generated at 2022-06-14 10:08:18.345021
# Unit test for function get_new_command
def test_get_new_command():
	assert(get_new_command('git commit') == 'git reset HEAD~')

# Generated at 2022-06-14 10:08:21.523109
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script="git commit")
    get_new_command(command)
    assert get_new_command(command) == "git reset HEAD~"


# Generated at 2022-06-14 10:08:26.200628
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit foo') == 'git reset HEAD~'
    assert get_new_command('git commit --foo bar') == 'git reset HEAD~'
    assert get_new_command('git commit foo bar') == 'git reset HEAD~'


# Generated at 2022-06-14 10:08:51.868712
# Unit test for function get_new_command
def test_get_new_command():
    command_git1 = Command('git commit files', '/home/usr/test')
    command_git2 = Command('git commit', '/home/usr/test')
    command_not_git = Command('ls', '/home/usr/test')
    assert(get_new_command(command_git1) == get_new_command(command_git2) ==
      'git reset HEAD~')
    assert(get_new_command(command_not_git) == None)

# Generated at 2022-06-14 10:08:54.719203
# Unit test for function get_new_command
def test_get_new_command():
    assert (git_reset() \
            .match('git commit -m "message"') \
            .get_new_command() == 'git reset HEAD~')

# Generated at 2022-06-14 10:09:04.419088
# Unit test for function match
def test_match():
    assert(match(Command('git commit file.txt')) == True)
    assert(match(Command('git commit -a')) == True)
    assert(match(Command('git commit file1 file2')) == True)
    assert(match(Command('git commit -m "Bla bla"')) == True)
    assert(match(Command('git add file1 file2')) == False)
    assert(match(Command('add file1 file2')) == False)
    assert(match(Command('git commit file.txt')) == True)
    assert(match(Command('git commit')) == True)


# Generated at 2022-06-14 10:09:06.924041
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('commit -m "My Message"',
                      'Aborting commit due to empty commit message.')
    assert get_new_command(command) == 'git reset HEAD~'


# Generated at 2022-06-14 10:09:10.610459
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -m "adsf"')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit', 'git')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:09:14.946540
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '', '', 1, None)) == 'git reset HEAD~'
    assert get_new_command(Command('git commit', '', '', 1, None)) != 'git commit'

# Generated at 2022-06-14 10:09:18.043249
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('git add', ''))
    assert not match(Command('commit', ''))


# Generated at 2022-06-14 10:09:20.168143
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:09:22.730757
# Unit test for function match
def test_match():
    command = Command('git commit -m "shadfee"', '', None)
    assert match(command)



# Generated at 2022-06-14 10:09:26.489228
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        'git commit -m "foo"') == 'git reset HEAD~'
    assert get_new_command(
        'git commit -a') == 'git reset HEAD~'

# Generated at 2022-06-14 10:10:12.975853
# Unit test for function match
def test_match():
    assert match(Command('git commit -am "First commit"', ''))
    assert not match(Command('git commit file', ''))


# Generated at 2022-06-14 10:10:15.387326
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '', '', ''))
    assert not match(Command('test', '', '', '', ''))


# Generated at 2022-06-14 10:10:17.238795
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit', '', [])
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:10:21.033803
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit')) == 'git reset HEAD~'



# Generated at 2022-06-14 10:10:23.572476
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('commit -m "stupid comment"', '', '')
    assert(get_new_command(command) == 'git reset HEAD~')

# Generated at 2022-06-14 10:10:28.495177
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -m "pushing"') == 'git reset HEAD~'
    assert get_new_command('git commit -a') == 'git reset HEAD~'
    

# Generated at 2022-06-14 10:10:32.048278
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert match(Command('git commit -m'))
    assert match(Command('git commit -m'))

    assert not match(Command('git add .'))


# Generated at 2022-06-14 10:10:39.240788
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit") == "git reset HEAD~"
    assert get_new_command("git commit -m 'initial'") == "git reset HEAD~"
    assert get_new_command("git commit --allow-empty -m 'initial'") == "git reset HEAD~"

# Generated at 2022-06-14 10:10:41.863117
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -am "test"')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:10:45.982035
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit -f') == 'git reset HEAD~'
    assert get_new_command('git commit -m "foo"') == 'git reset HEAD~'

# Generated at 2022-06-14 10:11:38.686011
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('git commit', '', ''))


# Generated at 2022-06-14 10:11:44.930738
# Unit test for function get_new_command
def test_get_new_command():
    command_with_script = Command('git commit -m "test1"', 'git commit -m "test1"')
    assert get_new_command(command_with_script) == "git reset HEAD~"
    command_without_script = Command('git commit -m "test2"', '$ git commit -m "test2"')
    assert get_new_command(command_without_script) == "git reset HEAD~"


# Generated at 2022-06-14 10:11:48.226675
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git commit -m 'initial commit'", "", "")
    new_command = get_new_command(command)
    assert new_command == "git reset HEAD~"

# Generated at 2022-06-14 10:12:00.875624
# Unit test for function match
def test_match():
    assert match(Command(script='git commit',
             stderr=u'''
git commit
interactive rebase in progress; onto f9a9a8b
You are currently rebasing branch 'master' on 'f9a9a8b'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Changes to be committed:

        new file:   random.txt

Unmerged paths:
        (use "git add <file>..." to mark resolution)

'''))

# Generated at 2022-06-14 10:12:15.807242
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert match(Command('git commit -m', ''))
    assert match(Command('git commit -m "message"', ''))
    assert match(Command('git commit -m message', ''))
    assert match(Command('git commit -a -m "message"', ''))
    assert match(Command('git commit -a -m "message" --author=giginet', ''))
    assert match(Command('git commit -a --amend --author=giginet', ''))
    assert match(Command('git commit -am', ''))
    assert match(Command('git commit -am "message"', ''))
    assert match(Command('git commit -am message', ''))
    assert match(Command('git commit -am --author=giginet', ''))

# Generated at 2022-06-14 10:12:21.854416
# Unit test for function match
def test_match():
    command = 'git commit -m "test"'
    assert match(command)

    command = 'git commit -m "test"'
    assert not match(command)

# Generated at 2022-06-14 10:12:22.941020
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '')) == 'git reset HEAD~'



# Generated at 2022-06-14 10:12:28.311580
# Unit test for function match
def test_match():
    assert match(Command('git commit -m \'first commit\'', None))
    assert not match(Command('git commit -m', None))
    assert not match(Command('git commit -m', None))
    assert not match(Command('commit -m test', None))
    assert not match(Command('commit -m test', None))



# Generated at 2022-06-14 10:12:31.946744
# Unit test for function match
def test_match():
    assert match(Command('vim README.md', 'git commit -m "message"'))
    assert not match(Command('vim README.md', 'add README.md'))


# Generated at 2022-06-14 10:12:35.469563
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m "test"') == 'git reset HEAD~'
    assert get_new_command('git commit') == 'git reset HEAD~'