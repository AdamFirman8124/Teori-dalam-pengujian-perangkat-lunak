

# Generated at 2022-06-14 10:13:58.361364
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         stderr='! [rejected] master -> master (non-fast-forward)',
                         output='Updates were rejected because the tip of your current branch is behind'))



# Generated at 2022-06-14 10:14:07.627267
# Unit test for function match
def test_match():
    assert match(command=Command('git push origin master:master',
                                 '! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind'))
    assert match(command=Command('git push origin master:master',
                                 '! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the remote contains work that you do'))
    assert not match(command=Command('git pull origin master',
                                     'Already up-to-date.'))
    assert not match(command=Command('git commit -m "test"',
                                     'hahaha'))



# Generated at 2022-06-14 10:14:08.745142
# Unit test for function match
def test_match():
    command = Command('$ git push')
    assert match(command)


# Generated at 2022-06-14 10:14:15.264559
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:aiham/dotfiles.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))


# Generated at 2022-06-14 10:14:28.221589
# Unit test for function get_new_command

# Generated at 2022-06-14 10:14:37.706540
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'hint: Updates were rejected because the remote contains work that you do\r\n'
                         'hint:   not have locally. This is usually caused by another repository pushing\r\n'
                         'hint:   to the same ref. You may want to first integrate the remote changes\r\n'
                         'hint:   (e.g., \'git pull ...\') before pushing again.\r\n'
                         'hint:   see the \'Note about fast-forwards\' in \'git push --help\' for details.\r\n'
                         '(non-fast-forward)',
                         ''))


# Generated at 2022-06-14 10:14:47.119731
# Unit test for function match

# Generated at 2022-06-14 10:15:04.066470
# Unit test for function match
def test_match():
    assert (match(Command('git push',
                         "! [rejected]        master -> master (non-fast-forward)\n"
                         "error: failed to push some refs to 'git@github.com:aiyanbo/awesome-python3-webapp.git'\n"
                         "hint: Updates were rejected because the tip of your current branch is behind\n"
                         "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                         "hint: 'git pull ...') before pushing again.\n"
                         "hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n")))

# Generated at 2022-06-14 10:15:05.310514
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'

# Generated at 2022-06-14 10:15:08.111913
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', 'remote: error: GH001: ...')) == shell.and_('git pull', 'git push')

# Generated at 2022-06-14 10:15:22.426847
# Unit test for function match

# Generated at 2022-06-14 10:15:33.469283
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '''! [rejected] master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/firatkucuk/MERN-boilerplate.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 10:15:36.959738
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master') == 'git pull origin master && git push origin master'
    assert get_new_command('git push origin') == 'git pull origin && git push origin'
    assert get_new_command('git push') == 'git pull && git push'

# Generated at 2022-06-14 10:15:43.268671
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push',
                      '! [rejected]        l2r -> l2r (non-fast-forward)\n'
                      'error: failed to push some refs to '
                      '\'git@github.com:XXXX/XXXX.git\'\n'
                      'hint: Updates were rejected because the tip of your '
                      'current branch is behind\n'
                      'hint: its remote counterpart. Integrate the remote '
                      'changes (e.g.\n'
                      'hint: \'git pull ...\') before pushing again.\n'
                      'hint: See the \'Note about fast-forwards\' in '
                      '\'git push --help\' for details.\n')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:15:48.609684
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git push evil master'
    output = ('! [rejected]        master -> master (non-fast-forward)\n'
              'fatal: The remote end hung up unexpectedly')
    assert get_new_command(Command(script, output)) == 'git pull && git push evil master'

# Generated at 2022-06-14 10:15:58.091349
# Unit test for function match
def test_match():
    assert match(Command('git push origin dev:master',
                         ' ! [rejected]        dev -> master (non-fast-forward)\n'
                         'error: failed to push some refs to '
                         '\'https://github.com/zhangguanzhang/douban-music-google-chrome-extension.git\'\n'
                         'hint: Updates were rejected because the tip of your '
                         'current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes '
                         '(e.g.\nhint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push '
                         '--help\' for details.'))

# Generated at 2022-06-14 10:16:01.639740
# Unit test for function get_new_command
def test_get_new_command():
	command = NewCommand('git push', 'git push\n! [rejected] up to date', '! [rejected] up to date')
	assert get_new_command(command) == 'git pull'

# Generated at 2022-06-14 10:16:07.688802
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command('git push origin master').script == 'git pull origin master')
    assert (get_new_command('git push origin branch').script == 'git pull origin branch')
    assert (get_new_command('git push origin commit_branch').script == 'git pull origin commit_branch')
    assert (get_new_command('git push origin').script == 'git pull origin')

enabled_by_default = True

# Generated at 2022-06-14 10:16:17.692817
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    f_command = Command('git push origin master:master', '',
                        'Updates were rejected because the tip of your'
                        ' current branch is behind its remote')
    assert get_new_command(f_command) == 'git pull && git push origin master:master'
    s_command = Command('git push origin master:master', '',
                        'Updates were rejected because the remote '
                        'contains work that you do')
    assert get_new_command(s_command) == 'git pull && git push origin master:master'

# Generated at 2022-06-14 10:16:29.452914
# Unit test for function match
def test_match():
	print("testing match function\n")
	command_input = Command("git push origin master", "! [rejected]        master -> master (non-fast-forward)\n")
	assert match(command_input)

	command_input = Command("git push origin master", "! [rejected]        master -> master (non-fast-forward)\n")
	assert match(command_input)

	command_input = Command("git push origin master", "Updates were rejected because the tip of your current branch is behind")
	assert match(command_input)

	command_input = Command("git push origin master", "! [rejected]        master -> master (non-fast-forward)\n")
	assert match(command_input)

	command_input = Command("git push origin master", "Updates were rejected because the tip of your current branch is behind\n")

# Generated at 2022-06-14 10:16:45.009954
# Unit test for function match
def test_match():
    assert(match(Command('git push',
                         '! [rejected] master -> master (non-fast-forward)'
                         '\nfatal: The remote end hung up unexpectedly')) == True)
    assert(match(Command('git push',
                         '! [rejected] master -> master (non-fast-forward)'
                         '\nfatal: The remote end hung up unexpectedly'
                         '\nUpdates were rejected because the remote '
                         'contains work that you do')) == True)
    assert(match(Command('git push',
                         '! [rejected] master -> master (non-fast-forward)'
                         '\nfatal: The remote end hung up unexpectedly'
                         '\nUpdates were rejected because the tip of your'
                         ' current branch is behind')) == True)

# Generated at 2022-06-14 10:16:53.727451
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (fetch first)'
                         '\nerror: failed to push some refs to ...', 1))
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (fetch first)'
                         '\nUpdates were rejected because the remote contains'
                         ' work that you do not have locally.', 1))
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (fetch first)'
                         '\nUpdates were rejected because the tip of your'
                         ' current branch is behind', 1))

# Generated at 2022-06-14 10:17:01.967372
# Unit test for function match
def test_match():
    command = Command('git push origin master', " ! [rejected]        master -> master (non-fast-forward)\n error: failed to push some refs to 'git@github.com:GochoMugo/thefuck.git'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: 'git pull ...') before pushing again.\n hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n")
    assert match(command)
    assert get_new_command(command) == 'git pull origin master && git push origin master'



# Generated at 2022-06-14 10:17:13.635905
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)',
                         'error: failed to push some refs to'
                         ' \'git@gitlab.com:user/test.git\''))
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)',
                         'error: failed to push some refs to'
                         ' \'https://gitlab.com/user/test.git\''))
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)',
                         'error: failed to push some refs to'
                         ' \'git@github.com:user/test.git\''))

# Generated at 2022-06-14 10:17:18.968792
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (fetch first)\n'
                         'error: failed to push some refs to \'git@github.com:yyx990803/vue-hackernews-2.0.git\'\n'
                         'hint: Updates were rejected because the remote contains work that you do\n'
                         'hint: not have locally. This is usually caused by another repository pushing\n'
                         'hint: to the same ref. You may want to first integrate the remote changes\n'
                         'hint: (e.g., \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:17:27.665310
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git push origin master", "! [rejected] master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind its remote\nhint: counterpart. Check out this branch and integrate the remote changes\nhint: (e.g. 'git pull ...') before pushing again.\nerror: failed to push some refs to 'git@github.com:user/repo.git'")
    new_command = get_new_command(command)
    assert new_command == shell.and_("git pull origin master", "git push origin master")

# Generated at 2022-06-14 10:17:37.256980
# Unit test for function match
def test_match():
    assert match(Command('git push',
    '''To https://github.com/XXX/XXX.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:XXX/XXX.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.'''))
    assert not match(Command('git push','''
    Everything up-to-date'''))


# Generated at 2022-06-14 10:17:47.060386
# Unit test for function match
def test_match():
	output = ''' ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:nklot/git-stuff.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

git add .
git commit -m "commit message"
git push origin branchname
'''
	assert match(Command('git push origin branchname', output))
	assert match(Command('git commit -m "hello"', output))

#

# Generated at 2022-06-14 10:17:57.184074
# Unit test for function match
def test_match():
    assert match(Command(script='git push origin master', output = '! [rejected]        master -> master (fetch first)'))
    assert match(Command(script='git push origin master', output = '! [rejected]        master -> master (non-fast-forward)'))
    assert match(Command(script='git push origin master', output = '! [rejected]        master -> master (non-fast-forward)'))
    assert match(Command(script='git push origin master', output = '! [rejected]        master -> master (non-fast-forward)'))
    assert match(Command(script='git push origin master', output = '! [rejected]        master -> master (non-fast-forward)'))

# Generated at 2022-06-14 10:18:09.163769
# Unit test for function match
def test_match():
	assert match(Command('git push origin master', "error: failed to push some refs to 'https://github.com/RohitRaja/git-testing.git'\n\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.\n", '', 0))

# Generated at 2022-06-14 10:18:20.895741
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master', '')) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:18:25.588715
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git push origin master", "! [rejected]        master -> master (fetch first)", "")
    assert get_new_command(command) == "git pull origin master && git push origin master"


# Generated at 2022-06-14 10:18:36.207424
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:FuckThisShit/FuckThisShit.github.io.git\'',
                         '', 1,
                         'Updates were rejected because the tip of your current branch is behind'))
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:FuckThisShit/FuckThisShit.github.io.git\'',
                         '', 1,
                         'Updates were rejected because the remote contains work that you do'))

# Generated at 2022-06-14 10:18:38.421484
# Unit test for function match

# Generated at 2022-06-14 10:18:48.806495
# Unit test for function match

# Generated at 2022-06-14 10:19:01.004447
# Unit test for function match
def test_match():
    assert match(Command('git push', '', '! [rejected] master -> master (non-fast-forward)\n'
                                 'error: failed to push some refs to \'https://github.com/Rudnitsky/thefuck.git\'\n'
                                 'hint: Updates were rejected because the tip of your '
                                 'current branch is behind\n'
                                 'hint: its remote counterpart. Integrate the remote changes'
                                 ' (e.g.\n'
                                 'hint: \'git pull ...\') before pushing again.\n'
                                 'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')) == True


# Generated at 2022-06-14 10:19:12.971850
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('git push origin --no-verify', '! [rejected]        master -> master (non-fast-forward)'
                '\nUpdates were rejected because the tip of your current branch is behind'
                '\nhint: its remote counterpart. Integrate the remote changes (e.g.'
                '\nhint: \'git pull ...\') before pushing again.'
                '\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                '', True)) == 'git pull origin --no-verify && git push origin --no-verify'


# Generated at 2022-06-14 10:19:22.214172
# Unit test for function match
def test_match():
    assert gitmatch('git push origin master') \
           .output == '! [rejected]        master -> master (non-fast-forward)'
    assert gitmatch('git push origin master').output \
           == '! [rejected]        master -> master (non-fast-forward)'
    assert gitmatch('git push origin master').output \
           == 'Updates were rejected because the remote contains work that '
    assert gitmatch('git push origin master').output \
           == 'Updates were rejected because the tip of your current branch is behind'
    assert gitmatch('git push origin master').output \
           == 'Updates were rejected because the tip of your current branch is behind'



# Generated at 2022-06-14 10:19:29.623209
# Unit test for function match
def test_match():
    command = Command("git push", "! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\n  (use \"git push\" to publish your local commits)\nerror: failed to push some refs to 'https://github.com/kennypank/thefuck'")
    assert match(command)
    command = Command("git push origin master", "! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\n  (use \"git push\" to publish your local commits)\nerror: failed to push some refs to 'https://github.com/kennypank/thefuck'")
    assert match(command)

# Generated at 2022-06-14 10:19:37.486436
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(command.Command('git push origin master', '! [rejected] master -> master (non-fast-forward) error: failed to push some refs to \'git@github.com:user/pydotorg-web.git\' To prevent you from losing history, non-fast-forward updates were rejected Merge the remote changes (e.g. \'git pull\') before pushing again. See the \'Note about fast-forwards\' section of \'git push --help\' for details.'))
    assert new_command.script == "git pull && git push origin master"

# Generated at 2022-06-14 10:19:54.452367
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'
    assert get_new_command('git push origin') == 'git pull origin && git push origin'


# Generated at 2022-06-14 10:20:09.225125
# Unit test for function match
def test_match():
    assert (match(Command('git push origin master', stderr='''
To https://github.com/nvbn/thefuck.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/nvbn/thefuck.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''))
            == True)

# Generated at 2022-06-14 10:20:21.722490
# Unit test for function match
def test_match():
    # Valid case
    underlying_command = "git push --origin develop"
    valid_output = "! [rejected]        develop -> develop (non-fast-forward)\n" \
                   "error: failed to push some refs to 'ssh://username@172.16.2.249:29418/projectname'\n" \
                   "hint: Updates were rejected because the tip of your current branch is behind\n" \
                   "hint: its remote counterpart. Integrate the remote changes (e.g.\n" \
                   "hint: 'git pull ...') before pushing again.\n" \
                   "hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n"
    command = Command(underlying_command, valid_output)
    assert(match(command) == True)



# Generated at 2022-06-14 10:20:33.232197
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', '! [rejected]        master -> master (fetch first)\n'
                                 'error: failed to push some refs to \'git@github.com:mislav/dotfiles.git\'\n'
                                 'hint: Updates were rejected because the remote contains work that you do\n'
                                 'hint: not have locally. This is usually caused by another repository pushing\n'
                                 'hint: to the same ref. You may want to first integrate the remote changes\n'
                                 'hint: (e.g., \'git pull ...\') before pushing again.\n'
                                 'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                      None)


# Generated at 2022-06-14 10:20:34.831865
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command('git push') == 'git pull && git push')

# Generated at 2022-06-14 10:20:39.980934
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected\n...', ''))
    assert match(Command('git push', 'Updates were rejected\n...', ''))
    assert not match(Command('git branch', 'Updates were rejected\n...', ''))


# Generated at 2022-06-14 10:20:49.358199
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:iacn/thefuck.git\'\n'
                         'To prevent you from losing history, non-fast-forward updates were rejected\n'
                         'Merge the remote changes (e.g. \'git pull\') before pushing again.  See the\n'
                         '\'Note about fast-forwards\' section of \'git push --help\' for details.\n'
                         ))
    

# Generated at 2022-06-14 10:21:00.452359
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '! [rejected]        master -> master (non-fast-forward)\n'
    'error: failed to push some refs to \'https://github.com/SarthakSwaroop/git_commands.git\'\n'
    'hint: Updates were rejected because the tip of your current branch is behind\n'
    'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
    'hint: \'git pull ...\') before pushing again.\n'
    'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))
    assert not match(Command('git push -u origin master', ''))
    assert not match(Command('git commit -m "Initial commit"', ''))
    assert match

# Generated at 2022-06-14 10:21:11.488259
# Unit test for function match
def test_match():
	assert match(Command('git push', 'remote: ! [rejected]        master -> master (non-fast-forward)\nremote: error: failed to push some refs to \'https://github.com/user/repo.git/\'\nTo https://github.com/user/repo.git/\n! [rejected] master -> master (non-fast-forward) \nerror: failed to push some refs to \'https://github.com/user/repo.git/\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n', 'git'), None)


# Generated at 2022-06-14 10:21:17.190723
# Unit test for function match

# Generated at 2022-06-14 10:21:47.561943
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'To git@github.com:ngs/thefuck.git ! [rejected] master -> master (non-fast-forward)',
                         'error: failed to push some refs to '
                         '\'git@github.com:ngs/thefuck.git\'',
                         'hint: Updates were rejected because the tip of your '
                         'current branch is behind',
                         'hint: its remote counterpart. Integrate the remote changes '
                         '(e.g.\nhint: \'git pull ...\') before pushing again.',
                         'hint: See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.'),
                None)


# Generated at 2022-06-14 10:21:53.187446
# Unit test for function match
def test_match():
	# Setup
	from thefuck.rules.git_push_pull import match
	from thefuck.types import Command

	# Exercise
	actual = match(Command('git push', 'Updates were rejected because the remote contains work that you do not have locally.\n  (use "git pull" to update your local branch)'))

	# Verify
	assert_equal(actual, True)



# Generated at 2022-06-14 10:22:07.896061
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g. hint: \'git pull ...\') before pushing again.\nfatal: The upstream branch of your current branch does not match\nthe name of your current branch.  To push to the upstream branch\non GitHub, use:\n    git push origin HEAD:master\n\nTo push to the branch of the same name on the remote, use\n    git push origin master\n\n'))

# Generated at 2022-06-14 10:22:12.339161
# Unit test for function get_new_command
def test_get_new_command():
    newcommand = 'git pull'
    assert get_new_command('git push') == newcommand
    assert get_new_command('git push --some-option') == newcommand
    assert get_new_command('git push branch') == newcommand

# Generated at 2022-06-14 10:22:23.113957
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'Updates were rejected because the tip of your '
                         'current branch is behind its remote counterpart. '
                         'Integrate the remote changes (e.g. hg pull ...) '
                         'before pushing again.\n', stderr=True))
    assert match(Command('git push',
                         'Updates were rejected because the remote '
                         'contains work that you do\n'
                         'not have locally. This is usually caused by '
                         'another repository pushing\n'
                         'to the same ref. You may want to first '
                         'integrate the remote changes\n'
                         '(e.g., hg pull ...)\n'
                         'before pushing again.\n', stderr=True))
    assert not match(Command('git push', ''))                                                                                                                

# Generated at 2022-06-14 10:22:30.502793
# Unit test for function match
def test_match():
	c = Command('git push', '! [rejected]        master -> master (fetch first)\nerror: failed to push some refs to \'http://git.xxx.com/xxx.git\'\nhint: Updates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., \'git pull ...\') before pushing again.')
	assert (match(c))


# Generated at 2022-06-14 10:22:41.876371
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '', '', 1)) == 'git pull'
    assert get_new_command(Command('git commit -m "me"', '', '', 1)) == 'git commit -m "me"'
    assert get_new_command(Command('git push origin master', '', '', 1)) == 'git pull origin master'
    assert get_new_command(Command('git push origin master:master', '', '', 1)) == 'git pull origin master:master'
    assert get_new_command(Command('git push --set-upstream origin master', '', '', 1)) == 'git pull --set-upstream origin master'

# Generated at 2022-06-14 10:22:53.697547
# Unit test for function match
def test_match():
    assert not match(Command(script = 'git sfsdfsd'))
    assert not match(Command(script = 'git push',
                             output = 'error: failed to push some refs to'))
    assert not match(Command(script = 'git push',
                             output = 'Updates were rejected because the '
                                      'tip of your current branch is behind'))
    assert match(Command(script = 'git push',
                         output = 'Updates were rejected because the tip of your current branch is behind'
                                  '\n'
                                  'Updates were rejected because the remote contains work that you do'))
    assert match(Command(script = 'git push',
                         output = 'Updates were rejected because the remote contains work that you do'))


# Generated at 2022-06-14 10:23:01.559566
# Unit test for function match
def test_match():
    assert match(Command(script = 'git push',
                         output = '! [rejected]\tmaster -> master (fetch first)\n error: failed to push some refs to \'git@github.com:xantares/dev.git\'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: \'git pull ...\') before pushing again.\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))
    assert not match(Command(script = 'git push',
                             output = 'To git@github.com:nvbn/thefuck.git\n   60d7f82..3f3b1ab  master -> master'))

# Generated at 2022-06-14 10:23:10.471440
# Unit test for function match
def test_match():
    incorrect_cmd = Command('git push origin master', '',
                            " ! [rejected] master -> master (fetch first) "
                            "error: failed to push some refs to"
                            " 'git@github.com:xxxxx/xxxxx.git'\n"
                            "hint: Updates were rejected because the tip of"
                            " your current branch is behind\n"
                            "hint: its remote counterpart. Integrate the "
                            "remote changes")
    assert match(incorrect_cmd)
    correct_cmd = Command('git push origin master', '', 'Total 0 (delta 0), reused 0 (delta 0)\nTo git@github.com:xxxx/xxxx.git\n * [new branch]      master -> master\n')
    assert not match(correct_cmd)