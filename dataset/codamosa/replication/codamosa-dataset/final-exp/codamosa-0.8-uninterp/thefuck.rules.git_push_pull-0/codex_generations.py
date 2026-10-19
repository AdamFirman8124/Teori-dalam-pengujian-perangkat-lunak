

# Generated at 2022-06-14 10:14:01.782331
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', 'Updates were rejected becuase the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes before pushing again.\nSee the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:14:13.303763
# Unit test for function match
def test_match():
    assert match(Command("git push",
                         "remote: Permission to Test/test.git denied to user.\n"
                         "fatal: unable to access 'https://github.com/Test/test.git/': "
                         "The requested URL returned error: 403"))
    assert match(Command("git push",
                         "! [rejected]        master -> master (non-fast-forward)\n"
                         "error: failed to push some refs to 'https://github.com/Test/test.git'"))
    assert match(Command("git push",
                         "To https://github.com/Test/test.git/\n"
                         " ! [rejected]        master -> master (non-fast-forward)\n"
                         "error: failed to push some refs to 'https://github.com/Test/test.git'"))
   

# Generated at 2022-06-14 10:14:26.006143
# Unit test for function match
def test_match():
    assert match(Command('git push origin dev',
                         ' ! [rejected]        dev -> dev (non-fast-forward)\n'
                         'error: failed to push some refs to'
                         ' \'git@github.com:mgruca/repo.git\'\n'
                         'Updates were rejected because the tip of your'
                         ' current branch is behind\n'
                         '  its remote counterpart. Integrate the '
                         'remote changes (e.g.\n'
                         '  \'git pull ...\') before pushing again.'
                         '\n'
                         'See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.\n')) == True

# Generated at 2022-06-14 10:14:31.365429
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', 'Everything up-to-date')
    assert not match(command)

    command = Command('git push', 'Updates were rejected because the remote '
                      ' contains work that you do')
    assert match(command)
    assert get_new_command(command) == shell.and_('git pull', 'git push')

# Generated at 2022-06-14 10:14:43.806465
# Unit test for function match
def test_match():


    assert match(Command('git push origin master:master')) == True
    assert match(Command('git push origin master:master',
                         'Total 0 (delta 0), reused 0 (delta 0)\n'
                         'To git@github.com:nvie/gitflow.git\n'
                         '   d26c7c6..051834f  master     -> master\n')) == False

# Generated at 2022-06-14 10:14:54.571027
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_push_rejected import get_new_command
    assert get_new_command(Command('git push origin master',
                                   '! [rejected]        master -> master (non-fast-forward)\n'
                                   'error: failed to push some refs to \'git@example.com:ui-framework.git\'\n'
                                   'To prevent you from losing history, non-fast-forward updates were rejected\n'
                                   'Merge the remote changes (e.g. \'git pull\') before pushing again.  See the\n'
                                   '\'Note about fast-forwards\' section of \'git push --help\' for details.\n')) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:15:03.346422
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected because the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes before pushing again.'))
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind'))
    assert not match(Command('git push', 'Everything up-to-date'))
    assert not match(Command('git status', 'Everything up-to-date'))


# Generated at 2022-06-14 10:15:09.101442
# Unit test for function match
def test_match():
    assert match(command=Command('git push origin master', 'git push origin master', 'To https://github.com/polowis/thefuck\n ! [rejected]        master -> master (non-fast-forward)', '', 0, 2))
    assert match(command=Command('git push origin master', 'git push origin master', 'error: failed to push some refs to \'https://github.com/polowis/thefuck\'\nTo https://github.com/polowis/thefuck\n ! [rejected]        master -> master (non-fast-forward)', '', 1, 3))

# Generated at 2022-06-14 10:15:11.190693
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == shell.and_('git pull', 'git push')

# Generated at 2022-06-14 10:15:17.802530
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(command.Command('git push master',
        'fatal: The current branch master has no upstream branch.\n'
        'To push the current branch and set the remote as upstream, use\n'
        '\n'
        '    git push --set-upstream origin master\n', '', 0,
        'git pull master')) == 'git pull master')

# Generated at 2022-06-14 10:15:23.835429
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '', '', 0, '', '', '')).script == 'git pull'
    assert get_new_command(Command('git push origin master', '', '', 0, '', '', '')).script == 'git pull origin master'

# Generated at 2022-06-14 10:15:35.667196
# Unit test for function match
def test_match():
    match_string = ('git push origin master\nTo https://github.com/settings/keys\n ! [rejected] master -> master (non-fast-forward)\nerror: failed to push some refs to '
                    '\'https://github.com/settings/keys\'\nTo prevent you from losing history, non-fast-forward updates were rejected\nMerge the remote changes (e.g. '
                    '\'git pull\') before pushing again.  See the\n\'Note about fast-forwards\' section of \'git push --help\' for details.\n')
    assert match(Command(match_string, "", ""))
    assert not match(Command("git push", "", ""))


# Generated at 2022-06-14 10:15:38.362722
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '')) == 'git pull'
    assert get_new_command(Command('git push upstream master', '')) == 'git pull upstream master'

# Generated at 2022-06-14 10:15:41.422662
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('git push fuckingorigin feature', '')) == \
        shell.and_('git pull fuckingorigin feature', 'git push fuckingorigin feature')

# Generated at 2022-06-14 10:15:45.367974
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'

# Generated at 2022-06-14 10:15:48.297748
# Unit test for function match
def test_match():
    command = Command('git push origin master')
    assert match(command)
    command = Command('git push origin master')
    assert not match(command)

# Generated at 2022-06-14 10:15:57.198130
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'https://github.com/USER/REPO/\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                         '', 0))



# Generated at 2022-06-14 10:16:06.857510
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master',
            'To https://github.com/nvbn/thefuck.git\n ! [rejected] master -> master (non-fast-forward)\n error: failed to push some refs to \'https://github.com/nvbn/thefuck.git\'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: \'git pull ...\') before pushing again.\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')
    assert 'git pull origin master' == get_new_command(command)

# Generated at 2022-06-14 10:16:18.883402
# Unit test for function match
def test_match():
    # Returns True if output from command includes message
    assert match(Command('git push origin master',
                         "To https://github.com/user/repo.git\n ! [rejected] master -> master (fetch first)\nerror: failed to push some refs to 'https://github.com/user/repo.git'\nhint: Updates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.")) == True


# Generated at 2022-06-14 10:16:30.359749
# Unit test for function match
def test_match():
    # Generic
    assert match(Command('git push', '', 'Updates were rejected because the tip'
                                             ' of your current branch is behind'))
    # Generic
    assert match(Command('git push origin master:master', '',
                         'Updates were rejected because the tip of your'
                         ' current branch is behind'))
    # Generic
    assert match(Command('git push', '', 'Updates were rejected because the'
                                             ' remote contains work that you do'
                                             ' not have locally'))
    # Generic
    assert match(Command('git push origin master:master', '',
                         'Updates were rejected because the remote'
                         ' contains work that you do not have locally'))
    # Specific

# Generated at 2022-06-14 10:16:44.301961
# Unit test for function match
def test_match():
	assert match(Command('git push',
	'''
	To https://github.com/ouranoshong/R-code.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:ouranoshong/R-code.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
''')) == True


# Generated at 2022-06-14 10:16:54.183633
# Unit test for function get_new_command
def test_get_new_command():
    command = shell.and_('git push origin master', 'git push origin master')
    old_output = ("warning: push.default is unset; its implicit value is "
                  "(currently) 'matching'")
    new_output = ("Branch master set up to track remote branch master from "
                  "origin.")
    assert(get_new_command(Command('git push origin master', old_output, None))
           == 'git pull && git push origin master')
    assert(get_new_command(Command('git push origin master', new_output, None))
           == 'git push origin master')

available = match
priority = 100

# Generated at 2022-06-14 10:17:02.870925
# Unit test for function get_new_command

# Generated at 2022-06-14 10:17:14.166174
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'https://github.com/randy3k/test.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                         '', 1))


# Generated at 2022-06-14 10:17:19.389828
# Unit test for function match
def test_match():
    assert match(Command(script='git push',
                    output=' ! [rejected]        master -> master (non-fast-forward)\n'
                           'error: failed to push some refs to \'https://github.com/JaveriaHabib/project1.git\'\n'
                           'hint: Updates were rejected because the tip of your current branch is behind\n'
                           'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                           'hint: \'git pull ...\') before pushing again.'))

# Generated at 2022-06-14 10:17:21.613402
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master')) == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:17:30.208301
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected because the remote '
                         'contains work that you do not have locally. This is '
                         'usually caused by another repository pushing to the '
                         'same ref. You may want to first integrate the remote '
                         'changes before pushing again.'))
    assert match(Command('git push', 'Updates were rejected because the tip of '
                         'your current branch is behind'))
    assert match(Command('git push', '! [rejected] push -> master'))
    assert not match(Command('git push', '! [remote rejected] master -> master (non-fast-forward)'))

# Generated at 2022-06-14 10:17:43.275319
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master '
                         '(non-fast-forward)',
                         'error: failed to push some refs to '
                         '\'git@github.com:muchen/git-tutorial.git\'',
                         'hint: Updates were rejected because the tip of '
                         'your current branch is behind',
                         'hint: its remote counterpart. Integrate the remote '
                         'changes (e.g',
                         'hint: \'git pull ...\') before pushing again.',
                         'hint: See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.'))
    assert not match(Command('git push', ''))


# Generated at 2022-06-14 10:17:52.742148
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                   '! [rejected]        master -> master (non-fast-forward)\n'
                   'Updates were rejected because the tip of your current branch is behind\n',
                   '', 1))
    assert not match(Command('git push origin master',
                             'Everything up-to-date\n', '', 1))
    assert not match(Command('git add .', '', '', 0))


# Generated at 2022-06-14 10:17:54.167530
# Unit test for function get_new_command

# Generated at 2022-06-14 10:18:11.738882
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git push origin master", "", "! [rejected]        master -> master (non-fast-forward)\n"
                                                   "error: failed to push some refs to 'git@github.com:ryanolsen/dotfiles.git'\n"
                                                   "hint: Updates were rejected because the tip of your current branch is behind\n"
                                                   "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                                                   "hint: 'git pull ...') before pushing again.\n"
                                                   "hint: See the 'Note about fast-forwards' in 'git push --help' for details.")

# Generated at 2022-06-14 10:18:17.489764
# Unit test for function get_new_command
def test_get_new_command():
    c = Command(script = 'git push -u origin master', output='! [rejected] master -> master (fetch first)')
    assert get_new_command(c) == "git pull && git push -u origin master"

# Generated at 2022-06-14 10:18:28.870519
# Unit test for function match
def test_match():
    assert match(Command('git push',
      'To https://github.com/bradtraversy/git_test.git\n ! [rejected] master -> master (non-fast-forward)\n error: failed to push some refs to \'https://github.com/bradtraversy/git_test.git\'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: \'git pull ...\') before pushing again.\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n',
      ''))

# Generated at 2022-06-14 10:18:38.886309
# Unit test for function match
def test_match():
    assert match(Command('git push', "Updates were rejected because the tip of your \
    current branch is behind its remote counterpart. Integrate the remote changes \
    (e.g. 'git pull ...') before pushing again.\n\
    See the 'Note about fast-forwards' in 'git push --help' for details.", None))
    assert match(Command('git push', "Updates were rejected because the remote contains work that you do \
    not have locally. This is usually caused by another repository pushing to the same ref. You may \
    want to first integrate the remote changes (e.g., 'git pull ...') before pushing again.", None))
    assert not match(Command('git push', "Everything up-to-date", None))

# Generated at 2022-06-14 10:18:41.347410
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '! [rejected]...')) == 'git pull'

# Generated at 2022-06-14 10:18:48.325800
# Unit test for function match
def test_match():
    command1 = Command('git push --set-upstream origin experimental', '', '', 0)
    command2 = Command('git push', '', 'Updates were rejected because the tip of your current branch is behind', 0)
    command3 = Command('git push', '', 'Updates were rejected because the remote contains work that you do', 0)
    command4 = Command('git push', '', '', 0)
    assert not match(command1)
    assert match(command2)
    assert match(command3)
    assert not match(command4)


# Generated at 2022-06-14 10:19:00.734574
# Unit test for function match
def test_match():

    # Test 1: failed push
    output = '''
To git@github.com:droslean/thefuck.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:droslean/thefuck.git'
hint: Updates were rejected because the tip of your current branch is
hint: behind its remote counterpart. Integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''
    command = Command('git push', output)
    assert match(command)

    # Test 2: failed push - no branch

# Generated at 2022-06-14 10:19:06.483636
# Unit test for function match
def test_match():
    command = Command('git push', 'Updates were rejected because the tip of '
                      'your current branch is behind its remote counterpart. '
                      'Integrate the remote changes (e.g.hint: \'git pull ...\') '
                      'before pushing again.hint: See the \'Note about fast-forwards\' '
                      'in \'git push --help\' for details.'
                      )
    assert match(command)



# Generated at 2022-06-14 10:19:15.643632
# Unit test for function match
def test_match():
    assert match(Command('git push origin maste',
                         'To git@github.com:nvbn/thefuck.git\n! [rejected] \
                          master -> master (non-fast-forward)\n error: \
                          failed to push some refs to \
                          \'git@github.com:nvbn/thefuck.git\'\n \
                          hint: Updates were rejected because the tip of \
                          your current branch is behind\n \
                          hint: its remote counterpart. Integrate the \
                          remote changes (e.g\n \
                          hint: \'git pull ...\') \
                          before pushing again.\n hint: See the \
                          \'Note about fast-forwards\' in \'git push \
                          --help\' for details.\n',
                         '', 3))


# Unit

# Generated at 2022-06-14 10:19:17.838889
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', '')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:19:35.610840
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected] master -> master (fetch first)\n'
                         'error: failed to push some refs to '
                         '\'git@github.com:vitorfs/thefuck.git\'',
                         ''))



# Generated at 2022-06-14 10:19:47.354398
# Unit test for function match

# Generated at 2022-06-14 10:20:00.571376
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push',
                      ' ! [rejected]        master -> master (non-fast-forward)\n'
                      'error: failed to push some refs to\' git@github.com:mislav/dotfiles.git\'\n'
                      'hint: Updates were rejected because the tip of your current branch is behind\n'
                      'hint: its remote counterpart. Merge the remote changes (e.g. \'git pull\')\n'
                      'hint: before pushing again.\n'
                      'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:20:11.943726
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -\u003e master (non-fast-forward)',
                         'error: failed to push some refs to \'http://github.com/user/repo.git\'',
                         'hint: Updates were rejected because the tip of your current branch is behind',
                         'hint: its remote counterpart. Integrate the remote changes (e.g.',
                         'hint: \'git pull ...\') before pushing again.',
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:20:24.068375
# Unit test for function match
def test_match():
    res = match(Command('git push',
                        'To https://github.com/tiagofilipe12/pset6.git\n ! [rejected]        master -> master (non-fast-forward)\n error: failed to push some refs to \'https://github.com/tiagofilipe12/pset6.git\'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: \'git pull ...\') before pushing again.\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n',
                        'https://github.com/tiagofilipe12/pset6.git'))

    assert(res == True)


# Generated at 2022-06-14 10:20:26.251415
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command('')
    assert new_command == 'git pull && git push'

# Generated at 2022-06-14 10:20:39.120382
# Unit test for function match

# Generated at 2022-06-14 10:20:44.309784
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind'))
    assert not match(Command('git push', 'Everything up-to-date'))
    assert not match(Command('git st', 'Updates were rejected because the tip of your current branch is behind'))

# Generated at 2022-06-14 10:20:57.903327
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', 0, None))
    assert match(Command('git push', '', '', 0, None))
    assert match(Command('git push origin master', '', '! [rejected] master -> master (non-fast-forward)', 0, None))
    assert match(Command('git push', '', '! [rejected] master -> master (non-fast-forward)', 0, None))
    assert match(Command('git push origin master', '', '! [rejected] master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind', 0, None))

# Generated at 2022-06-14 10:21:02.799424
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', 1, None))
    assert not match(Command('git push origin master', '', '', 0, None))
    assert not match(Command('git pull origin master', '', '', 1, None))



# Generated at 2022-06-14 10:21:42.233419
# Unit test for function get_new_command
def test_get_new_command():
    command_string = 'git push'
    command = Command(command_string, '! [rejected] master -> master (non-fast-forward)\n\
    error: failed to push some refs to \'git@gitlab.com:my_git_repository.git\'\n\
    hint: Updates were rejected because the tip of your current branch is behind\n\
    hint: its remote counterpart. Integrate the remote changes (e.g.\n\
    hint: \'git pull ...\') before pushing again.\n\
    hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:21:44.106622
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').script == 'git pull && git push'

# Generated at 2022-06-14 10:21:53.929088
# Unit test for function match
def test_match():
    assert match(Command('git push https://github.com/techlivezheng/thefuck',
                         ' ! [rejected]  master -> master (non-fast-forward) '
                         'error: failed to push some refs to '
                         '\'https://github.com/techlivezheng/thefuck\'\n'
                         'hint: Updates were rejected because the tip of '
                         'your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote '
                         'changes (e.g.\nhint: \'git pull ...\') before '
                         'pushing again.\nhint: See the \'Note about '
                         'fast-forwards\' in \'git push --help\' for details.',
                         ''), None)


# Generated at 2022-06-14 10:21:58.767013
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (non-fast-forward)\'',
                         'fatal: The remote end hung up unexpectedly'))
    assert not match(Command('git push origin master',
                             '',
                             'Everything up-to-date'))

# Generated at 2022-06-14 10:22:10.001924
# Unit test for function get_new_command

# Generated at 2022-06-14 10:22:22.231156
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ('! [rejected]        master -> master (non-fast-forward)\n'
                          'error: failed to push some refs to \'https://github.com/pry0cc/thefuck.git\'\n'
                          'hint: Updates were rejected because the tip of your current branch is behind\n'
                          'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                          'hint: \'git pull ...\') before pushing again.\n'
                          'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')))

# Generated at 2022-06-14 10:22:26.762454
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'Everything up-to-date',
                         ''))
    assert not match(Command('git push origin master',
                             'Everything up-to-date',
                             ''))


# Generated at 2022-06-14 10:22:38.162864
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', '! [rejected] master -> master (non-fast-forward)\n\
    error: failed to push some refs to \'https://github.com/jerryliuyx/Test.git\'\n\
    hint: Updates were rejected because the tip of your current branch is behind\n\
    hint: its remote counterpart. Integrate the remote changes (e.g.\n\
    hint: \'git pull ...\') before pushing again.\n\
    hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == 'git pull && git push'


# Generated at 2022-06-14 10:22:51.349729
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'https://github.com/szymonmaszke/thefuck\'\n'
                         'Updates were rejected because the tip of your current branch is behind\n'
                         'its remote counterpart. Integrate the remote changes (e.g.\n\'git pull ...\') '
                         'before pushing again.\n'
                         'See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))


# Generated at 2022-06-14 10:22:53.810069
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', 'failed to push some refs to something')
    assert get_new_command(command) == 'git pull && git push'