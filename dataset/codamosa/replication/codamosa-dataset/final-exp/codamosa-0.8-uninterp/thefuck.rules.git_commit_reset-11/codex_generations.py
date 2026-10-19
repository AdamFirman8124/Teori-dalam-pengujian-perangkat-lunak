

# Generated at 2022-06-14 10:03:23.025822
# Unit test for function match
def test_match():
    command = Command('git commit -a -m test', '', 0)
    assert match(command)
    command = Command('git commit -a -m test', '', 1)
    assert not match(command)
    command = Command('git push origin master', '', 1)
    assert not match(command)



# Generated at 2022-06-14 10:03:28.695830
# Unit test for function match
def test_match():
    ret = False
    command = Command('commit', '', '')
    assert match(command) == ret


# Generated at 2022-06-14 10:03:32.041211
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "test commit"', '')
    assert 'git reset HEAD~' == get_new_command(command)


enabled_by_default = True

# Generated at 2022-06-14 10:03:34.925934
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "message"', '', ''))
    assert not match(Command('git commit --amend', '', ''))


# Generated at 2022-06-14 10:03:38.575023
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert match(Command('commit', '', ''))
    assert not match(Command('git commit -m', '', ''))



# Generated at 2022-06-14 10:03:44.188389
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "Some commit"', ''))
    assert not match(Command('git push', ''))
    assert match(Command('git add -A && git commit -m "cleanup"', ''))
    assert not match(Command('la', ''))


# Generated at 2022-06-14 10:03:46.225701
# Unit test for function match
def test_match():
    assert match(ShellCommand('git commit -m "test"'))
    assert(not match(ShellCommand('git push')))

# Generated at 2022-06-14 10:03:50.105301
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert not match(Command('make commit', '', ''))
    assert not match(Command('git status', '', ''))

# Generated at 2022-06-14 10:03:51.876329
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))


# Generated at 2022-06-14 10:03:54.987156
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', stdout=''))
    assert match(Command('git commit -m "blah"', '', stdout=''))


# Generated at 2022-06-14 10:04:01.550178
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit failed', '~/some/random/path')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit failed', '~/some/random/path')) != 'git reset HEAD'


# Generated at 2022-06-14 10:04:13.710850
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert match(Command('git commit -a', ''))
    assert match(Command('git commit -v', ''))
    assert match(Command('git commit -m "test"', ''))
    assert match(Command('git commit --amend', ''))
    assert match(Command('git commit --amend --no-edit', ''))
    assert match(Command('git commit --amend --no-edit --author "test"', ''))
    assert match(Command('git commit --author "test"', ''))
    assert match(Command('git commit --author="test"', ''))
    assert match(Command('git commit --no-edit', ''))
    assert match(Command('git commit -m "test"', ''))

# Generated at 2022-06-14 10:04:16.000401
# Unit test for function match
def test_match():
    assert match(Command('cd test; git commit -m hello'))
    assert match(Command('cd test; git commit -a -m hello'))
    assert not match(Command('cd test; git add file -m hello'))
    assert not match(Command('cd test; git log'))


# Generated at 2022-06-14 10:04:20.921688
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('commit -m "This is a commit"', None)) == 'git reset HEAD~'
    assert get_new_command(Command('commit -a ', None)) == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:26.155741
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -m "some message"', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit --allow-empty -m "some message"', '')) == 'git reset HEAD~'
    assert get_new_command(Command('git commit -a', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:04:29.033978
# Unit test for function match
def test_match():
    assert not match(Command('git add foo', '', 0))
    assert not match(Command('cleanup', '', 0))
    assert match(Command('git commit', '', 0))
    assert match(Command('git commit -m "Foo bar"', '', 0))
    assert not match(Command('git blame', '', 0))



# Generated at 2022-06-14 10:04:39.196030
# Unit test for function match
def test_match():
    assert match(Command("git commit -m 'message'",
                         "fatal: Paths with -a does not make sense."))
    assert match(Command("git commit",
                         "fatal: Paths with -a does not make sense."))
    assert not match(Command("git branch",
                         "fatal: Paths with -a does not make sense."))
    assert not match(Command("git checkout",
                         "fatal: Paths with -a does not make sense."))



# Generated at 2022-06-14 10:04:40.592388
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git reset HEAD~' == get_new_command('git commit')

# Generated at 2022-06-14 10:04:43.704661
# Unit test for function match
def test_match():
	assert match(Command('git commit'))
	assert match(Command('git commit -m "first commit"'))
	assert match(Command('git commit -m "introduce some new features"'))
	assert not match(Command('git commit -m'))



# Generated at 2022-06-14 10:04:45.470276
# Unit test for function get_new_command
def test_get_new_command():
    string = 'git commit'
    assert get_new_comm

# Generated at 2022-06-14 10:04:49.910487
# Unit test for function match
def test_match():
    command = Command('git commit -m "test"')
    assert match(command)
    command = Command('git commit -m "test"')
    command.script_parts = []
    assert not match(command)
    command = Command('ls')
    assert not match(command)

# Generated at 2022-06-14 10:04:54.959575
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -a -m "Some commit"', '', stderr='error: nothing to commit')
    assert get_new_command(command) == 'git reset HEAD~'
    command = Command('git commit -m "Some commit"', '', stderr='error: nothing to commit')
    assert get_new_command(command) == 'git reset HEAD~'
    command = Command('git commit file -m "Some commit"', '', stderr='error: nothing to commit')
    assert get_new_command(command) == 'git reset HEAD~ file'


# Generated at 2022-06-14 10:04:57.750178
# Unit test for function get_new_command
def test_get_new_command():
    assert('git reset HEAD~' == get_new_command('git commit'))
    assert(False == match('hellow git'))

# Generated at 2022-06-14 10:05:00.814723
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git commit', stdout='', stderr='')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:05:02.928481
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(u'git commit -m "add python script"') == 'git reset HEAD~'

# Generated at 2022-06-14 10:05:06.545520
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'
    assert get_new_command('git commit --amend') == 'git reset HEAD~'


# Generated at 2022-06-14 10:05:11.812155
# Unit test for function match
def test_match():
    testcommand = Command('git commit -m "Edit 8.8"',
                          'git commit -m "Edit 8.8"\nOn branch master\n'
                          'Untracked files:\n'
                          '\t\033[31m.DS_Store\033[m\n'
                          '\t\033[31m.gitignore\033[m\n'
                          '\t\033[31m.project\033[m\n'
                          '\t\033[31m.settings/\033[m\n'
                          '\t\033[31m.travis.yml\033[m\nnothing added to commit '
                          'but untracked files present (use "git add" to track)')
    assert match(testcommand)



# Generated at 2022-06-14 10:05:17.539919
# Unit test for function match
def test_match():
    assert match(Command('git commit -m "fix whitespace"'))
    assert match(Command('git commit -m "fix whitespace', None))
    assert not match(Command('git log'))
    assert not match(Command('git'))
    assert not match(Command('git commit', None))


# Generated at 2022-06-14 10:05:28.077768
# Unit test for function get_new_command
def test_get_new_command():
    # If command includes 'commit'
    command = Command('git add * && git commit -m "changed"',
                      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel erat vel ante sodales bibendum et nec nisi. Nam eu nisi non mi malesuada eleifend. Nulla facilisi. Proin id purus et sapien fermentum venenatis. Proin euismod sapien nibh, at rhoncus enim pellentesque id. Etiam scelerisque pharetra ante, at rutrum diam. Ut iaculis sollicitudin lacus, id suscipit tellus imperdiet vitae. Curabitur vitae rutrum quam. Morbi nec magna ut diam fermentum malesuada eu eget massa.')
   

# Generated at 2022-06-14 10:05:30.324200
# Unit test for function match
def test_match():
    assert match(Command('git commit --amend -m "new message"', ''))
    assert not match(Command('git reset HEAD~', ''))



# Generated at 2022-06-14 10:05:36.641286
# Unit test for function match
def test_match():
    # Case 1: Case where the command is git commit
    command = Command('git commit')
    assert match(command)

    # Case 2: Case where the command is git commit -m "test"
    command = Command('git commit -m "test"')
    assert match(command)



# Generated at 2022-06-14 10:05:39.195981
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:05:44.114263
# Unit test for function match
def test_match():
    assert match(Command('git commit file.txt', '', '/bin/git'))
    assert not match(Command('git commit', '', '/bin/git'))
    assert not match(Command('commit file.txt', '', '/bin/git'))

# Generated at 2022-06-14 10:05:47.083240
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert not match(Command('commit', '', ''))
    assert not match(Command('git branch branch-name --track bugfix/1', '', ''))

# Generated at 2022-06-14 10:05:49.366045
# Unit test for function match
def test_match():
    assert match(Command('commit', '', ''))
    assert not match(Command('', '', ''))
    

# Generated at 2022-06-14 10:05:53.852241
# Unit test for function match
def test_match():
    assert match(Command(script='git commit',
                         stderr='On branch master\n',
                         stdout=''))
    assert not match(Command(script='git push',
                         stderr='On branch master\n',
                         stdout=''))

# Generated at 2022-06-14 10:05:56.809761
# Unit test for function get_new_command
def test_get_new_command():
    assert ['git', 'reset', 'HEAD'] == get_new_command('git commit')
    assert ['git', 'r', 'HEAD'] == get_new_command('git r')

# Generated at 2022-06-14 10:05:59.188439
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('commit -m "travis CI build"', '', '')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:02.080235
# Unit test for function get_new_command
def test_get_new_command():
    output = get_new_command(Command('git commit', ''))
    assert output == 'git reset HEAD~'


# Generated at 2022-06-14 10:06:05.162968
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('commit -m "woops"', '', '')
    assert_equals(get_new_command(command), 'git reset HEAD~')


# Generated at 2022-06-14 10:06:13.818324
# Unit test for function match
def test_match():
	assert match(Command('git commit foo bar','/'))
	assert match(Command('git commit foo bar baz','/'))
	assert not match(Command('git add foo','/'))
	assert not match(Command('git commit --amend foo','/'))


# Generated at 2022-06-14 10:06:16.238657
# Unit test for function get_new_command
def test_get_new_command():
    assert "git reset HEAD~" in get_new_command(Command("git commit", ""))

# Generated at 2022-06-14 10:06:18.594266
# Unit test for function match
def test_match():
    assert_equal(match(Command('git commit')), True)
    assert_equal(match(Command('git config commit')), False)


# Generated at 2022-06-14 10:06:22.909579
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert match(Command('git commit -m commit message'))
    assert match(Command('git commit -a -m commit message'))
    assert match(Command('git commit-tree -m commit message'))
    assert not match(Command('git remote'))


# Generated at 2022-06-14 10:06:30.156103
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add file1.txt && git commit -m "Add file1.txt"',
            'someshit')
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:35.671339
# Unit test for function match
def test_match():
    assert match(Command('git commit --amend', '', 0, None))
    assert match(Command('git ci --amend', '', 0, None))
    assert not match(Command('git co master', '', 0, None))
    assert not match(Command('git commit', '', 0, None))
    assert not match(Command('commit', '', 0, None))


# Generated at 2022-06-14 10:06:36.665773
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:39.042052
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('git commit ', ''))
    assert not match(Command('gitagggit commit', ''))
    assert not match(Command('gitagggit commit ', ''))


# Generated at 2022-06-14 10:06:40.678762
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))

# Generated at 2022-06-14 10:06:42.473138
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('fuck') == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:55.249657
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('Git commit Message') == 'git reset HEAD~'

# Generated at 2022-06-14 10:06:56.932804
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(['git commit']) == 'git reset HEAD~'


# Generated at 2022-06-14 10:06:58.274294
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'

# Generated at 2022-06-14 10:07:01.292453
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -m "Commit message"', '', '')) == 'git reset HEAD~'



# Generated at 2022-06-14 10:07:10.918005
# Unit test for function match
def test_match():
    assert match(command=Command('git commit'))
    assert match(command=Command('git commit -m "First commit"'))
    assert match(command=Command('git commit --amend'))
    assert match(command=Command('git commit -m "First commit" --amend'))
    assert match(command=Command('git commit -m "First commit" -a --amend'))
    assert not match(command=Command('git commit -m "First commit" --amend -a'))


# Generated at 2022-06-14 10:07:14.737446
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert match(Command('git commit -m "First commit"', '', ''))
    assert not match(Command('git commit file', '', ''))
    assert not match(Command('git commit -a', '', ''))
    assert not match(Command('git reset HEAD~', '', ''))


# Generated at 2022-06-14 10:07:21.647699
# Unit test for function match
def test_match():
    assert match(Command('something', 'git commit message'))
    assert match(Command('something', 'git commit message --amend --no-edit'))
    assert not match(Command('something', 'git st'))



# Generated at 2022-06-14 10:07:27.502744
# Unit test for function match
def test_match():
    assert match(Command('git commit ', '', '/home/user/com/test_git'))
    assert match(Command('git reset', '', '/home/user/com/test_git'))
    assert not match(Command('git commit -m "test"', '', '/home/user/com/test_git'))
    # in other repo
    assert not match(Command('git comit', '', '/home/user/test'))


# Generated at 2022-06-14 10:07:30.550582
# Unit test for function match
def test_match():
    assert match(Script('git commit', ''))
    assert match(Script('git commit -m', ''))
    assert match(Script('git commit --amend', ''))

    assert not match(Script('git commitsomething wrong', ''))
    assert not match(Script('git commit --something wrong', ''))

# Generated at 2022-06-14 10:07:33.132228
# Unit test for function match
def test_match():
    command = Command('commit', '', '')
    assert match(command)

    command = Command('reset', '', '')
    assert not match(command)


# Generated at 2022-06-14 10:08:01.920263
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(command) == 'git reset HEAD~' )


# Generated at 2022-06-14 10:08:11.335394
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m "some message"') == 'git reset HEAD~'
    assert get_new_command('git commit') == 'git reset HEAD~'
    # actual git command 'git commit -am "some message"' will be changed to
    # 'git commit -m "some message"'
    assert get_new_command('git commit -am "some message"') == 'git reset HEAD~'
    assert get_new_command('git commit --amend') == 'git reset HEAD~'
    assert get_new_command('git commit --amend -m "some message"') == 'git reset HEAD~'
    assert get_new_command('git reset --hard HEAD') == 'git reset HEAD~'
    assert get_new_command('git reset --hard HEAD~') == 'git reset HEAD~'


# Unit test

# Generated at 2022-06-14 10:08:14.367509
# Unit test for function match
def test_match():
    assert match(Command('git commit file1 file2', '', ''))
    assert match(Command('git commit -m "blah"', '', ''))
    assert not match(Command('git pull', '', ''))


# Generated at 2022-06-14 10:08:15.884035
# Unit test for function get_new_command
def test_get_new_command():
    result = get_new_command(Command('git commit'))
    assert 'git reset HEAD' in result

# Generated at 2022-06-14 10:08:18.266038
# Unit test for function match
def test_match():
    assert not match(Command('echo "foo"'))
    assert not match(Command('git commit'))
    assert match(Command('git commit -m "foo"'))


# Generated at 2022-06-14 10:08:19.443255
# Unit test for function match
def test_match():
    pass


# Generated at 2022-06-14 10:08:23.071158
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit -m 'my message'") == "git reset HEAD~"
    assert get_new_command("git commit -m") != "git reset HEAD~"


# Generated at 2022-06-14 10:08:25.686066
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git commit', '', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:08:28.197410
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert not match(Command('git branch', '', ''))



# Generated at 2022-06-14 10:08:29.821382
# Unit test for function get_new_command
def test_get_new_command():
    assert ('git reset HEAD~' == get_new_command('git commit'))

# Generated at 2022-06-14 10:08:54.835008
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('git reset HEAD~', ''))
    assert not match(Command('ls', ''))



# Generated at 2022-06-14 10:08:58.616256
# Unit test for function get_new_command
def test_get_new_command():
    script1 = 'git commit'
    command1 = Command(script1, '')
    assert get_new_command(command1) == 'git reset HEAD~'

# Generated at 2022-06-14 10:09:00.244942
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:09:02.340731
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m "Fixed something"').script == 'git reset HEAD~'


# Generated at 2022-06-14 10:09:06.494963
# Unit test for function match
def test_match():
    assert match(Command('', '', '')) == False
    assert match(Command('', '', 'git status')) == False
    assert match(Command('', '', 'git commit -m')) == False
    assert match(Command('', '', 'git commit')) == True


# Generated at 2022-06-14 10:09:08.825420
# Unit test for function match
def test_match():
    assert match(Command('git commit -m newfile', '', 0))
    assert not match(Command('git foo', '', 0))



# Generated at 2022-06-14 10:09:11.349340
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m "Some message"').script == 'git reset HEAD~'

# Generated at 2022-06-14 10:09:13.701007
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit -m "test"')

# Generated at 2022-06-14 10:09:23.411679
# Unit test for function match
def test_match():
    assert match(Command('git commit'))
    assert match(Command('git commit -m'))
    assert match(Command('git commit -am'))
    assert match(Command('git commit -am "commit message"'))
    assert not match(Command('git log'))
    assert not match(Command('git status'))
    assert not match(Command('git branch'))
    assert not match(Command('git pull'))
    assert not match(Command('git checkout'))
    assert not match(Command('git checkout -b'))
    assert not match(Command('git push'))
    assert not match(Command('git push origin'))
    assert not match(Command('git status'))


# Generated at 2022-06-14 10:09:24.774390
# Unit test for function match
def test_match():
    assert match(Command('git commit -m test'))
    assert not match(Command('git add'))


# Generated at 2022-06-14 10:10:18.168172
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git status', '', '')) == ''
    assert get_new_command(Command('git add', 'Status: On branch master\nnothing to commit, working directory clean', '')) == ''
    assert get_new_command(Command('git commit', '', '')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:10:21.526955
# Unit test for function match
def test_match():
    assert (match(Command('git commit', '', '')))
    assert (not match(Command('git add', '', '')))



# Generated at 2022-06-14 10:10:24.782181
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add file1.txt; git commit -m "message"', '', 0)
    assert get_new_command(command) == 'git reset HEAD~'

# Generated at 2022-06-14 10:10:26.589329
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:10:28.524473
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git commit -m "TEST"')) == 'git reset HEAD~'

# Generated at 2022-06-14 10:10:29.628346
# Unit test for function match
def test_match():
    assert match(get_command())



# Generated at 2022-06-14 10:10:31.386287
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git commit --amend") == ("git reset HEAD~")

# Generated at 2022-06-14 10:10:45.909254
# Unit test for function match
def test_match():
    command = Command('git commit -m "Hello World"', '', '/')
    assert match(command)

    command = Command('git commit', '', '/')
    assert match(command)

    command = Command('git commit -m "Hello World"', '', '/')
    assert match(command)

    command = Command('git commit -m "Hello World"', '', '/')
    assert match(command)

    command = Command('git commit', '', '/')
    assert match(command)

    command = Command('git commit -m "Hello World"', '', '/')
    assert match(command)

    command = Command('git commit', '', '/')
    assert match(command)

    command = Command('git commit -m "Hello World"', '', '/')
    assert match(command)


# Generated at 2022-06-14 10:10:58.027835
# Unit test for function get_new_command

# Generated at 2022-06-14 10:11:01.009068
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert not match(Command('git checkout', '', ''))
    a

# Generated at 2022-06-14 10:12:45.669312
# Unit test for function get_new_command
def test_get_new_command():
    temp = Command('git commit -m "foobar"', '', 1)
    assert get_new_command(temp) == 'git reset HEAD~'

# Generated at 2022-06-14 10:12:47.881412
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit') == 'git reset HEAD~'

# Generated at 2022-06-14 10:12:50.494077
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', ''))
    assert not match(Command('git config', '', ''))


# Generated at 2022-06-14 10:12:53.393925
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git commit', '', '')
    assert get_new_command(command) == 'git reset HEAD~'


# Generated at 2022-06-14 10:12:55.539009
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('') == 'git reset HEAD~'


# Generated at 2022-06-14 10:12:59.552486
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('commit -m "test commit"', '', '/Users/honza/dev/test_repo')
        ) == 'git reset HEAD~'

# Generated at 2022-06-14 10:13:01.635556
# Unit test for function match
def test_match():
	assert match(Command('git commit'))
	assert not match(Command('git init'))


# Generated at 2022-06-14 10:13:03.821513
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git commit -m "test"') == 'git reset HEAD~'



# Generated at 2022-06-14 10:13:09.982716
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', '/'))
    assert match(Command('git commit -a', '', '/'))
    assert match(Command('git commit -m', '', '/'))
    assert match(Command('git commit -v', '', '/'))
    assert match(Command('git commit --amend', '', '/'))
    assert not match(Command('git status', '', '/'))


# Generated at 2022-06-14 10:13:11.869062
# Unit test for function match
def test_match():
    assert match(Command('git commit', ''))
    assert not match(Command('', ''))