

# Generated at 2022-06-14 10:13:59.051754
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git push')) == 'git pull && git push'

# Generated at 2022-06-14 10:14:03.701611
# Unit test for function match

# Generated at 2022-06-14 10:14:11.398749
# Unit test for function match
def test_match():
    assert match(Command('git push', '', 'error: failed to push some refs to ....'))
    assert match(Command('git push', '', 'error: failed to push some refs to .... Updates were rejected because the tip of your current branch is behind'))
    assert match(Command('git push', '', 'error: failed to push some refs to .... Updates were rejected because the remote contains work that you do'))
    assert not match(Command('git push', '', 'error: failed to push something'))


# Generated at 2022-06-14 10:14:22.548171
# Unit test for function match
def test_match():
    # Function match return true
    assert match(Command('git push origin master',
        "To git.abc.com:abc/abc.git\n ! [rejected]        master -> master (fetch first)\n error: failed to push some refs to 'git@git.abc.com:abc/abc.git'\n hint: Updates were rejected because the remote contains work that you do\n hint: not have locally. This is usually caused by another repository pushing\n hint: to the same ref. You may want to first integrate the remote changes\n hint: (e.g., 'git pull ...') before pushing again.\n hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n",
        '', '', '', 'git'))

    # Function match return false

# Generated at 2022-06-14 10:14:24.862736
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('git push', 'Updates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g. git pull ...) before pushing again.', 'git push')) == 'git pull && git push'

# Generated at 2022-06-14 10:14:36.817394
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\nremote: Error: failed to push some refs to \'ssh://git@stash.dummy.com/scm/cmm/dummy.git\'', '', 1, False))
    assert not match(Command('git status', '...', '', 1, False))

# Generated at 2022-06-14 10:14:46.702325
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (fetch first)'
                         '\n error: failed to push some refs to '
                         '\'https://github.com/kevinjalbert/thefuck.git\'',
                         '', 3))
    assert match(Command('git push',
                         ' ! [rejected]        master -> master (fetch first)'
                         '\n error: failed to push some refs to '
                         '\'https://github.com/kevinjalbert/thefuck.git\'',
                         '', 3))

# Generated at 2022-06-14 10:15:03.661111
# Unit test for function match
def test_match():
    assert (match(Command('git push',
                         "The current branch master has no upstream branch.\r\n"
                         "To push the current branch and set the remote as upstream, use\r\n"
                         "    git push --set-upstream origin master\r\n"
                         "git push\r\n"
                         "To push the current branch and set the remote as upstream, use\r\n"
                         "    git push --set-upstream origin master\r\n")))


# Generated at 2022-06-14 10:15:09.273096
# Unit test for function match
def test_match():
    assert match(Command('push', '', '! [rejected] master -> master (non-fast-forward)\n'
                    'error: failed to push some refs to \'git@bitbucket.org:username/repo.git\'\n'
                    'hint: Updates were rejected because the tip of your current branch is behind\n'
                    'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                    'hint: \'git pull ...\') before pushing again.\n'
                    'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))


# Generated at 2022-06-14 10:15:21.471380
# Unit test for function match

# Generated at 2022-06-14 10:15:37.086492
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').lstrip() == 'git pull'
    assert get_new_command('git push --force').lstrip() == 'git pull'
    assert get_new_command('git push --force stuff').lstrip() == 'git pull'
    assert get_new_command('git push -u origin stuff').lstrip() == 'git pull'
    assert get_new_command('git push -u origin stuff').lstrip() == 'git pull'
    assert get_new_command('git push --foo').lstrip() == 'git pull --foo'
    assert get_new_command('git push --force --foo').lstrip() == 'git pull --force'
    assert get_new_command('git push -u origin master').lstrip() == 'git pull'

# Generated at 2022-06-14 10:15:48.595097
# Unit test for function get_new_command

# Generated at 2022-06-14 10:15:58.078177
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (fetch first)\n'
                         'error: failed to push some refs to \'git@github.com.\''
                         '\nUpdates were rejected because the tip of '
                         'your current branch is behind its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                         '', 1, None))

# Generated at 2022-06-14 10:16:07.777400
# Unit test for function match
def test_match():
    assert match(command.Command(script="git push",
                                 output='! [rejected]        master -> master (non-fast-forward)'))
    assert match(command.Command(script="git push",
                                 output='! [rejected]        master -> master (fetch first)'))
    assert match(command.Command(script="git push",
                                 output='! [rejected]        master -> master (non-fast-forward)'))
    assert match(command.Command(script="git push",
                                 output='Updates were rejected because the remote contains work that you do'))
    assert not match(command.Command(script="git push",
                                     output='Everything is up-to-date'))


# Generated at 2022-06-14 10:16:20.886515
# Unit test for function match

# Generated at 2022-06-14 10:16:24.541965
# Unit test for function match
def test_match():
    match_result = match('git push origin master')
    assert match_result
    match_result = match('git push origin master')
    assert match_result



# Generated at 2022-06-14 10:16:37.527568
# Unit test for function match
def test_match():
    assert match(Command('git push',
        '''
        ! [rejected]        master -> master (non-fast-forward)
        error: failed to push some refs to ''
        hint: Updates were rejected because the tip of your current branch is behind
        hint: its remote counterpart. Integrate the remote changes (e.g
        hint: 'git pull ...') before pushing again.
        hint: See the 'Note about fast-forwards' in 'git push --help' for details.
        '''))

# Generated at 2022-06-14 10:16:48.657903
# Unit test for function match

# Generated at 2022-06-14 10:16:55.778811
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '! [rejected]        master -> master (non-fast-forward)')).script == 'git pull && git push'
    assert get_new_command(Command('git commit -am "bugfix #42" && git push', '! [rejected]        master -> master (non-fast-forward)')).script == 'git commit -am "bugfix #42" && git pull && git push'

# Generated at 2022-06-14 10:16:59.678516
# Unit test for function match
def test_match():
    assert match(Command('git push', ''))
    assert match(Command('git push origin master','''
remote: error: denying non-fast-forward refs/heads/master (you should pull first)
To ssh://server/path/proj.git
 ! [rejected]        master -> master (non-fast-forward)
'''))

# Generated at 2022-06-14 10:17:11.545967
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '''
To git@bitbucket.org:someuser/somerepo.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@bitbucket.org:someuser/somerepo.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.'''))

# Generated at 2022-06-14 10:17:23.223119
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'To git@github.com:nvbn/thefuck.git\n! [rejected]        master -> master (fetch first)\nerror: failed to push some refs to \'git@github.com:nvbn/thefuck.git\'\nhint: Updates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))

# Generated at 2022-06-14 10:17:34.957694
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected] master -> master (fetch first)\n'
                         'error: failed to push some refs to'
                         ' \'git@github.com:Dzonata/A-Code-a-day.git\'\n'
                         'hint: Updates were rejected because the tip'
                         ' of your current branch is behind\n'
                         'hint: its remote counterpart.',
                         '/home/dzonatasavio/Documents/a-code-a-day/git'))


# Generated at 2022-06-14 10:17:43.275246
# Unit test for function match
def test_match():
    assert match(Command("git push", "error: failed to push some refs to 'https://github.com/jackzhenguo/pycharm.git'\n\
        hint: Updates were rejected because the tip of your current branch is behind\n\
        hint: its remote counterpart. Integrate the remote changes (e.g.\n\
        hint: 'git pull ...') before pushing again.\n\
        hint: See the 'Note about fast-forwards' in 'git push --help' for details.", ""))
    assert not match(Command("git push", "Everything up-to-date", ""))


# Generated at 2022-06-14 10:17:52.742157
# Unit test for function get_new_command

# Generated at 2022-06-14 10:18:02.133552
# Unit test for function match
def test_match():
    assert match(Command('git push', " ! [rejected]        master -> master (non-fast-forward)\n"
                                     "error: failed to push some refs to 'git@github.com:repo.git'\n"
                                     "hint: Updates were rejected because the tip of your current branch is behind\n"
                                     "hint: its remote counterpart. Integrate the remote changes (e.g\n"
                                     "hint: 'git pull ...') before pushing again.\n"
                                     "hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n"))

# Generated at 2022-06-14 10:18:03.867079
# Unit test for function match

# Generated at 2022-06-14 10:18:08.945084
# Unit test for function match
def test_match():
    assert(match(Command('git push', 'Updates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g.hint: git pull ...) before pushing again.\nSee the \'Note about fast-forwards\' in \'git push --help\' for details.')) == True)


# Generated at 2022-06-14 10:18:18.176285
# Unit test for function match
def test_match():
    assert match(Command('git push',
        ' ! [rejected]        master -> master (non-fast-forward)\n'
        'error: failed to push some refs to \'ssh://git@example.com/repo.git\'\n'
        'hint: Updates were rejected because the tip of your current branch is behind\n'
        'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
        'hint: \'git pull ...\') before pushing again.\n'
        'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:18:22.553500
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git push origin master").script == "git pull origin master && git push origin master"
    assert get_new_command("git push origin master").stdout == "fatal: You are not currently on a branch."


# Generated at 2022-06-14 10:18:43.979052
# Unit test for function match
def test_match():
    assert match(Command('git push', ''))
    assert match(Command('git push origin master',
        'To https://github.com/nvie/gitflow.git\n ! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/nvie/gitflow.git\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))
    assert not match(Command('git', ''))

# Generated at 2022-06-14 10:18:51.150779
# Unit test for function match
def test_match():
    assert match('qwertyuiop') == None
    assert match('git push origin master') == True
    assert match('git push') == True
    assert match('git push it') == True
    assert match('git push it') == True
    assert match('git push it') == True
    assert match('git push it') == True
    assert match('git push it it') == True
    assert match('git push it it') == True


# Generated at 2022-06-14 10:18:53.513281
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '1abc')) == 'git pull'

# Generated at 2022-06-14 10:18:55.448727
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'

# Generated at 2022-06-14 10:18:57.661543
# Unit test for function get_new_command
def test_get_new_command():
    assert git_pull.get_new_command(Command('git push')) == 'git pull && git push'

# Generated at 2022-06-14 10:19:05.096268
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master',
                           "Updates were rejected because the tip of your"
                           " current branch is behind its remote"
                           " counterpart. Integrate the remote changes"
                           " (e.g. 'git pull ...') before pushing again."
                           " See the 'Note about fast-forwards' in 'git push"
                           " --help' for details.")) == shell.and_(
            'git pull origin master',
            'git push origin master')

# Generated at 2022-06-14 10:19:07.289858
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master') == 'git pull && git push origin master'

# Generated at 2022-06-14 10:19:15.927018
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected] master -> master (non-fast-forward) \n'
                         ' error: failed to push some refs to \'git@git.git\''
                         '\n hint: Updates were rejected because the tip '
                         'of your current branch is behind',
                         'git push'))
    assert match(Command('git push',
                       ' ! [rejected] master -> master (fetch first)\n'
                       ' error: failed to push some refs to \'git@git.git\''
                       '\n hint: Updates were rejected because the remote '
                       'contains work that you do',
                       'git push'))
    assert not match(Command('git branch', '', 'git branch'))
    assert not match(Command('git push', '', 'git push'))

# Generated at 2022-06-14 10:19:25.977310
# Unit test for function match

# Generated at 2022-06-14 10:19:32.955070
# Unit test for function match

# Generated at 2022-06-14 10:20:08.333086
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'
    assert get_new_command('git push origin master') == 'git pull origin master && git push origin master'
    assert get_new_command('oh-my-zsh:master[oh-my-zsh]$ git push oh-my-zsh master') == 'oh-my-zsh:master[oh-my-zsh]$ git pull oh-my-zsh master && oh-my-zsh:master[oh-my-zsh]$ git push oh-my-zsh master'



# Generated at 2022-06-14 10:20:16.578365
# Unit test for function match
def test_match():
    assert match(Command(script='git push something',
                         output='! [rejected]        master -> master (non-fast-forward)\n\n'
                         'error: failed to push some refs to \'git@github.com:username/repo.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:20:26.572912
# Unit test for function get_new_command
def test_get_new_command():
    git_push = 'git push origin'
    git_pull = 'git pull origin'
    ShellCommand(git_push, 'Updates were rejected because the tip of your current branch is behind', 'git push origin', None)
    assert get_new_command(ShellCommand(git_push, 'Updates were rejected because the tip of your current branch is behind', 'git push origin', None)) == git_pull

# Generated at 2022-06-14 10:20:37.075023
# Unit test for function match
def test_match():
    assert match(command=Command("git push origin master:master", "! [rejected] master -> master (non-fast-forward) \nerror: failed to push some refs to 'git@github.com:damienloo/thefuck.git' \nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.\n"))
    assert not match(command=Command("git push origin master", ""))


# Generated at 2022-06-14 10:20:39.867775
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command("git push origin master") == 'git pull origin master && git push origin master')

# Generated at 2022-06-14 10:20:51.001893
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '! [rejected] master -> master (non-fast-forward)\n'
              'error: failed to push some refs to \'git@github.com:0xCS/dotfiles.git\'\n'
              'hint: Updates were rejected because the tip of your current branch is behind\n'
              'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
              'hint: \'git pull ...\') before pushing again.\n'
              'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:20:56.813370
# Unit test for function get_new_command
def test_get_new_command():
	command = Command('git push origin master')
	result = Command('git pull && git push origin master')
	assert get_new_command(command) == result

# Generated at 2022-06-14 10:21:09.338984
# Unit test for function match
def test_match():
    assert match(Command('git push', "! [rejected]        master -> master (non-fast-forward)\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details."))

# Generated at 2022-06-14 10:21:21.965397
# Unit test for function match

# Generated at 2022-06-14 10:21:32.806788
# Unit test for function get_new_command
def test_get_new_command():
    assert_equals(get_new_command(Command("git push -u origin master",
                                          "! [rejected]        master -> master (non-fast-forward)\n"
                                          "error: failed to push some refs to 'git@github.com:thomaxxl/thefuck.git'\n"
                                          "hint: Updates were rejected because the tip of your current branch is behind\n"
                                          "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                                          "hint: 'git pull ...') before pushing again.\n"
                                          "hint: See the 'Note about fast-forwards' in 'git push --help' for details.")),
                      "git pull -u origin master; git push -u origin master")

# Generated at 2022-06-14 10:22:19.974093
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master', '! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\nUpdates were rejected because the remote contains work that you do\nTo push again, use:')
    assert 'git pull origin master && git push origin master' in get_new_command(command)

# Generated at 2022-06-14 10:22:31.601176
# Unit test for function match
def test_match():
    command = Command('git push origin master',
    """
    ! [rejected]        master -> master (fetch first)
    error: failed to push some refs to 'git@github.com:MJ10/Coursera-WebDev-JHU-Assignments.git'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    """)
    assert match(command)


# Generated at 2022-06-14 10:22:33.294217
# Unit test for function get_new_command
def test_get_new_command():
    assert "git pull" in get_new_command(Command('git push', '', ''))


# Generated at 2022-06-14 10:22:36.588114
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master', '')
    assert get_new_command(command) == 'git pull origin master'

enabled_by_default = True

# Generated at 2022-06-14 10:22:37.599754
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master', '', '', '', None)) == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:22:39.282236
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').script == 'git pull && git push'


# Generated at 2022-06-14 10:22:52.185038
# Unit test for function match
def test_match():
    assert match(Command('git push origin future',
                         ' ! [rejected]        future -> future (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@******\'\n'
                         'Updates were rejected because the tip of your current branch is behind\n'
                         'its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:23:00.514340
# Unit test for function match
def test_match():
    assert match(Command(script="git push",
                          stdout="! [rejected]        master -> master (non-fast-forward)\n\
								  error: failed to push some refs to 'git@gitlab.com:michele-sanna/test.git'\n\
								  hint: Updates were rejected because the tip of your current branch is behind\n\
								  hint: its remote counterpart. Integrate the remote changes (e.g.\n\
								  hint: 'git pull ...') before pushing again.",
                          stderr=None))

# Generated at 2022-06-14 10:23:02.867335
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master') == 'git pull && git push origin master'

# Generated at 2022-06-14 10:23:14.242178
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master '
                         '(non-fast-forward)\n'
                         'error: failed to push some refs to '
                         '\'git@github.com:dennyzhang/cheat-sheets.git\'\n'
                         'hint: Updates were rejected because the tip '
                         'of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the '
                         'remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.'
                         '\nhint: See the \'Note about fast-forwards\' '
                         'in \'git push --help\' for details.',
                         '', 1)) == True