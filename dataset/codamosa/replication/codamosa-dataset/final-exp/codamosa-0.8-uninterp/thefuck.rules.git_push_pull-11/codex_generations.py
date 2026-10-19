

# Generated at 2022-06-14 10:14:06.813181
# Unit test for function match
def test_match():
    assert match(Command("git push origin master", "! [rejected]        master -> master (fetch first)\n"
                "error: failed to push some refs to 'https://github.com/lvgangyao/thefuck.git'\n"
                "hint: Updates were rejected because the remote contains work that you do\n"
                "hint: not have locally. This is usually caused by another repository pushing\n"
                "hint: to the same ref. You may want to first integrate the remote changes\n"
                "hint: (e.g., 'git pull ...') before pushing again.", 0))

# Generated at 2022-06-14 10:14:11.789891
# Unit test for function match
def test_match():
    assert not match(Command('git', 'status'))
    assert not match(Command('git', 'push', 'origin', 'master'))
    assert match(Command('git', 'push', 'origin', 'master'))
    assert match(Command('git', 'push', 'origin', 'master'))


# Generated at 2022-06-14 10:14:22.895334
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected] master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to ...'
                         'Updates were rejected because the tip of your '
                         'current branch is behind'))

# Generated at 2022-06-14 10:14:32.403083
# Unit test for function get_new_command
def test_get_new_command():
    output = """To https://github.com/octocat/Spoon-Knife.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/octocat/Spoon-Knife.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details."""
    assert("git pull && git push" in get_new_command(Command("git push", output)))

# Generated at 2022-06-14 10:14:44.657016
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected] master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to\''
                         ' ...\n'
                         'To prevent you from losing history, '
                         'non-fast-forward updates were rejected\n'
                         'Merge the remote changes (e.g. \'git pull\') '
                         'before pushing again. See the \'Note about'
                         ' fast-forwards\' section of \'git push --help\' for'
                         ' details.'))

# Generated at 2022-06-14 10:14:48.950159
# Unit test for function match
def test_match():
    assert match(command=Command(script='git push origin master',
                                 output='To git@github.com:nvbn/thefuck.git\n ! [rejected]        master -> master (fetch first)',))
    assert match(command=Command(script='git push origin master',
                                 output='Updates were rejected because the tip of your current branch is behind'))
    assert match(command=Command(script='git push origin master',
                                 output='To git@github.com:nvbn/thefuck.git\n ! [rejected]        master -> master (fetch first)',))
    assert not match(command=Command(script='git checkout master',
                                     output='M   app.py\nSwitched to branch \'master\''))

# Generated at 2022-06-14 10:15:05.115885
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '',
                         '/bin/git push  --porcelain'
                         ' --progress origin master! [rejected]'
                         ' failed to push some refs to'
                         ' Updatess were rejected because the tip of your'
                         ' current branch is behind'))
    assert not match(Command('git push origin master', '',
                             '/bin/git push  --porcelain'
                             ' --progress origin master! [rejected]'
                             ' failed to push some refs to'))
    assert match(Command('git push origin master', '',
                         '/bin/git push  --porcelain'
                         ' --progress origin master! [rejected]'
                         ' failed to push some refs to'
                         ' Updates were rejected because the remote'
                         ' contains work that you do'))



# Generated at 2022-06-14 10:15:18.141359
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected]        master -> master (fetch first)'))
    assert not match(Command('git push', 'Counting objects: 14, done.'))
    assert not match(Command('git push origin master', 'Everything up-to-date'))

# Generated at 2022-06-14 10:15:21.277824
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', 1, None))
    assert not match(Command('git push origin master', '', '', 1, None))



# Generated at 2022-06-14 10:15:34.551411
# Unit test for function match
def test_match():
    repo = os.path.dirname(os.path.abspath(__file__))
    git = sh.git.bake(_cwd=repo)
    git.config('user.name', 'test')
    git.config('user.email', 'test@test.com')

# Generated at 2022-06-14 10:15:42.931154
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git push'
    command = Command(script, '! [rejected]        master -> master (non-fast-forward)\nfatal: The remote end hung up unexpectedly\nUpdates were rejected because the tip of your current branch is behind\n')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:15:47.146624
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', '', ''))
    assert match(Command('git push origin master', '', '', '', ''))
    assert not match(Command('git branch', '', '', '', ''))


# Generated at 2022-06-14 10:15:49.785036
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git push", "failed to push some refs to...")
    assert 'git pull' == get_new_command(command)


enabled_by_default = False

# Generated at 2022-06-14 10:15:58.462870
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \''
                         'git@github.com:nvbn/thefuck.git\'\n'
                         'hint: Updates were rejected because the tip of your '
                         'current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes '
                         '(e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.'))


# Generated at 2022-06-14 10:16:06.895472
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'To https://github.com/nvbn/thefuck\n! [rejected] master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/nvbn/thefuck\'\nUpdates were rejected because the tip of your current branch is behind\nits remote counterpart. Integrate the remote changes (e.g.\n\'git pull ...\') before pushing again.\nSee the \'Note about fast-forwards\' in \'git push --help\' for details.'))


# Generated at 2022-06-14 10:16:19.807988
# Unit test for function match

# Generated at 2022-06-14 10:16:22.487656
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push')
    assert get_new_command(command) == "git pull"

# Generated at 2022-06-14 10:16:29.419435
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master', 'error: failed to push some refs to\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == shell.and_('git pull origin master','git push origin master')

# Generated at 2022-06-14 10:16:38.227477
# Unit test for function match
def test_match():
    correct_b = 'git push -f origin/master'
    correct_c = 'git push'
    correct_a = Command(script='git push', output='! [rejected]        master -> master (non-fast-forward)')
    wrong_a = Command(script='git push', output='! [rejected]        master -> master (non-fast-forward)')
    wrong_b = Command(script='git push', output='! [rejected]        master -> master (non-fast-forward)')
    assert match(correct_a) == True
    assert match(correct_b) == False
    assert match(correct_c) == False
    assert match(wrong_a) == False
    assert match(wrong_b) == False


# Generated at 2022-06-14 10:16:44.002257
# Unit test for function match
def test_match():
    assert match(Command(script='git push',
                         output = ' ! [rejected]master -> master(non-fast-forward)\n'
                                  'error: failed to push some refs to \'xxxxxx\'\n'
                                  'To prevent you from losing history, non-fast-forward updates were rejected\n'
                                  'Merge the remote changes(e.g. \'git pull\') before pushing again.\n'
                                  'See the \'Note about fast-forwards\' section of \'git push --help\' for details.\n'))

# Generated at 2022-06-14 10:16:59.231124
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected] master -> master (fetch first)\n'
                         'error: failed to push some refs to \'https://github.com/Vedant-Bhalgama/thefuck\'\n'
                         'hint: Updates were rejected because the remote contains work that you do\n'
                         'hint: not have locally. This is usually caused by another repository pushing\n'
                         'hint: to the same ref. You may want to first integrate the remote changes\n'
                         'hint: (e.g., \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))


# Generated at 2022-06-14 10:17:11.829992
# Unit test for function match
def test_match():
    assert match(Command(script='git push',
                         output='! [rejected]        master -> master (non-fast-forward)\n'
                                'error: failed to push some refs to '
                                '\'https://github.com/adamjonr/git-ignore.git\'\n'
                                'hint: Updates were rejected because the tip of your '
                                'current branch is behind\n'
                                'hint: its remote counterpart. Integrate the remote '
                                'changes (e.g.\n'
                                'hint: \'git pull ...\') before pushing again.\n'
                                'hint: See the \'Note about fast-forwards\' in '
                                '\'git push --help\' for details.'))


# Generated at 2022-06-14 10:17:23.345634
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '''To https://github.com/peterldowns/myrepo.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/peterldowns/myrepo.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''))

# Generated at 2022-06-14 10:17:26.174056
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '! [rejected] some files', '', 1)) == 'git pull && git push'


# Generated at 2022-06-14 10:17:35.642299
# Unit test for function match
def test_match():
    command = Command('git push origin master',
                      'To https://github.com/foobar/cmd\n ! [rejected]        master -> master (non-fast-forward)\n error: failed to push some refs to \'https://github.com/foobar/cmd\'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: \'git pull ...\') before pushing again.\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert match(command) is True



# Generated at 2022-06-14 10:17:43.755055
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('git push', 'Updates were rejected because the remote contains work that you do not have locally.  This is usually caused by another repository pushing to the same ref.  You may want to first integrate the remote changes (e.g., \'git pull ...\') before pushing again.  See the \'Note about fast-forwards\' in \'git push --help\' for details.')) == 'git pull && git push'
    assert get_new_command(Command('git push', 'Updates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g.\'git pull ...\') before pushing again.See the \'Note about fast-forwards\' in \'git push --help\' for details.')) == 'git pull && git push'

# Generated at 2022-06-14 10:17:56.640113
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected] master -> master (non-fast-forward)\n\
error: failed to push some refs to \'https://github.com/sih4sing5hong5/git-quick-stats.git\'\n\
hint: Updates were rejected because the tip of your current branch is behind\n\
hint: its remote counterpart. Integrate the remote changes (e.g.\n\
hint: \'git pull ...\') before pushing again.'))
    assert not match(Command('git push', 'Total 0 (delta 0), reused 0 (delta 0)\n\
To https://github.com/sih4sing5hong5/git-quick-stats.git\n\
   d5b9cf5..dca5bf6  master -> master'))
    assert not match

# Generated at 2022-06-14 10:17:57.902785
# Unit test for function get_new_command
def test_get_new_command():
    print(get_new_command('git push'))

# Generated at 2022-06-14 10:18:04.250839
# Unit test for function get_new_command
def test_get_new_command():
    with patch('thefuck.rules.git_push.shell') as shell_mock:
        shell_mock.and_.return_value = 'git pull && git push'
        assert git_push.get_new_command(Command('', '', '', '', '', '')) == \
                'git pull && git push'
        shell_mock.and_.assert_called_once_with(
                'git pull', 'git push')


# Generated at 2022-06-14 10:18:13.079553
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push --force', '! [rejected]        master -> master (non-fast-forward)\n'
                      'error: failed to push some refs to \'https://github.com/cwru-eecs338/assignment-1-git-workflow-alex-baker-smith.git\'\n'
                      'hint: Updates were rejected because the tip of your current branch is behind\n'
                      'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                      'hint: \'git pull ...\') before pushing again.\n'
                      'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == '&& git pull --force'

# Generated at 2022-06-14 10:18:30.524018
# Unit test for function match
def test_match():
    assert(match(Command('git push', '''
To https://github.com/someuser/proj1.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/someuser/proj1.git
''')) == True)
    assert(match(Command('git push', '''
To https://github.com/someuser/proj1.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/someuser/proj1.git
''')) == True)

# Generated at 2022-06-14 10:18:40.565636
# Unit test for function match
def test_match():

    command1 = Command("git push -f origin master", "", "")
    command2 = Command("git push origin master", "", "")
    command3 = Command("git push", "", "")
    command4 = Command("git push -f", "", "")

    assert not match(command1)
    assert not match(command2)
    assert not match(command3)
    assert not match(command4)


# Generated at 2022-06-14 10:18:47.985152
# Unit test for function match
def test_match():
    command = Command('git push origin master', "! [rejected] master -> master (non-fast-forward)\nerror: failed to push some refs to 'git@github.com:123/456.git'\nHint: Updates were rejected because the tip of your current branch is behind\nHint: its remote counterpart. Integrate the remote changes (e.g.\nHint: 'git pull ...') before pushing again.\nHint: See the 'Note about fast-forwards' in 'git push --help' for details.")
    assert match(command) is True

# Generated at 2022-06-14 10:19:00.650242
# Unit test for function match
def test_match():
    assert match(Command(script='git push origin master',
        stderr='To https://github.com/nvie/gitflow\n! [rejected] master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\n'))
    assert match(Command(script='git push',
        stderr='To git@github.com:nvie/gitflow.git\n ! [rejected] master -> master (non-fast-forward)\nUpdates were rejected because the remote contains work that you do\n'))
    assert match(Command(script='git push',
        stderr='To https://github.com/nvie/gitflow\n! [rejected] master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\n'))
   

# Generated at 2022-06-14 10:19:02.830267
# Unit test for function match
def test_match():
    assert match(Command("git push", "Updates were rejected because the tip of your current branch is behind"))


# Generated at 2022-06-14 10:19:04.839368
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').script == r'git pull && git push'

# Generated at 2022-06-14 10:19:09.097080
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_push import get_new_command

    output = "Updates were rejected because the tip of your" \
             " current branch is behind"

    assert get_new_command(output) == 'git pull'

# Generated at 2022-06-14 10:19:20.713398
# Unit test for function match
def test_match():
    assert match(Command(script='git push origin master',
                         output=" ! [rejected]        master -> master (fetch first)\n"
                                "error: failed to push some refs to "
                                "'git@github.com:vamsi-subbarao/some_repo.git'\n"
                                "hint: Updates were rejected because the tip of your current branch is behind\n"
                                "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                                "hint: 'git pull ...') before pushing again.\n"
                                "hint: See the 'Note about fast-forwards' in 'git push --help' for details."))

# Generated at 2022-06-14 10:19:28.845006
# Unit test for function match
def test_match():
    assert(match(Command('git push',
                         'remote: Permission to user/repo.git denied to User.\nfatal: unable to access \'https://github.com/user/repo.git/\': The requested URL returned error: 403')))
    assert(match(Command('git push',
                         'To https://github.com/user/repo.git\n! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/user/repo.git\'\nTo prevent you from losing history, non-fast-forward updates were rejected\nMerge the remote changes (e.g. \'git pull\') before pushing again.  See the\n\'Note about fast-forwards\' section of \'git push --help\' for details.')))


# Generated at 2022-06-14 10:19:32.550827
# Unit test for function get_new_command
def test_get_new_command():
    test_command = Command('git push')
    test_command.output = 'updates were rejected because the tip ' \
        'of your current branch is behind'
    assert get_new_command(test_command) == 'git pull && git push'

# Generated at 2022-06-14 10:20:01.045119
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         " ! [rejected]        master -> master (non-fast-forward)\n"
                         "error: failed to push some refs to 'https://github.com/faheel/ToolKit_Python.git'\n"
                         "hint: Updates were rejected because the tip of your current branch is behind\n"
                         "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                         "hint: 'git pull ...') before pushing again.\n"
                         "hint: See the 'Note about fast-forwards' in 'git push --help' for details.",
                         '', 1, None)) is True

# Generated at 2022-06-14 10:20:12.117381
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master', '',
                                   'Updates were rejected because the tip of your current')) \
        == shell.and_('git pull origin master', 'git push origin master')
    assert get_new_command(Command('git push', '',
                                   'Updates were rejected because the tip of your current')) \
        == shell.and_('git pull', 'git push')
    assert get_new_command(Command('git push origin master', '',
                                   'Updates were rejected because the remote contains')) \
        == shell.and_('git pull origin master', 'git push origin master')
    assert get_new_command(Command('git push', '',
                                   'Updates were rejected because the remote contains')) \
        == shell.and_('git pull', 'git push')

# Generated at 2022-06-14 10:20:22.956798
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
        '''To https://github.com/user/repo.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/user/repo.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.''')
            ) == True


# Generated at 2022-06-14 10:20:33.874098
# Unit test for function match

# Generated at 2022-06-14 10:20:46.713396
# Unit test for function match

# Generated at 2022-06-14 10:20:56.833668
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master').script == 'git pull origin master'
    assert get_new_command('git push master').script == 'git pull master'
    assert get_new_command('git push origin master'
                           'Updates were rejected because the tip of your'
                           ' current branch is behind'
                           'failed to push some refs to').script == 'git pull origin master'
    assert get_new_command('git push origin master'
                           'Updates were rejected because the remote '
                           'contains work that you do'
                           'failed to push some refs to').script == 'git pull origin master'

# Generated at 2022-06-14 10:20:58.820463
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master', '', '', '', '', '') == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:21:02.153360
# Unit test for function get_new_command
def test_get_new_command():
    command = Command.from_string('git push')
    assert get_new_command(command) == shell.and_(shell.from_string('git pull'),
                                                  command.script)

# Generated at 2022-06-14 10:21:13.178571
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected] master -> master (non-fast-forward)',
                         'error: failed to push some refs to'))
    assert match(Command('git push origin master',
                     'error: failed to push some refs to',
                     'Updates were rejected because the tip of your'
                     ' current branch is behind'))
    assert match(Command('git push origin master',
                         'To git@github.com:nvie/vim-mkdir.git',
                         '! [rejected] master -> master (non-fast-forward)',
                         'error: failed to push some refs to',
                         'Updates were rejected because the remote '
                         'contains work that you do'))

# Generated at 2022-06-14 10:21:23.930083
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         "error: failed to push some refs to 'git@git.com:user/repo.git'\n"
                         "hint: Updates were rejected because the tip of your current branch is behind\n"
                         "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                         "hint: 'git pull ...') before pushing again.\n"
                         "hint: See the 'Note about fast-forwards' in 'git push --help' for details.",
                         'git@git.com:user/repo.git', 'feature/test'))
    assert match(Command('git push', 'error: failed to push some refs to ..',
                         '', 'feature/test'))

# Generated at 2022-06-14 10:21:58.113925
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git push") == "git pull && git push"
    assert get_new_command("git push origin master") == "git pull && git push origin master"

# Generated at 2022-06-14 10:22:01.536310
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').script == 'git pull && git push'
    assert get_new_command('git push origin master').script == 'git pull && git push origin master'


# Generated at 2022-06-14 10:22:11.346807
# Unit test for function match
def test_match():
    assert not match(Command('sed s/foo/bar/', ''))
    assert match(Command('git push', '''
remote: error: denying non-fast-forward refs/heads/master (you should pull first)
! [remote rejected] master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/nvbn/thefuck.git'
'''))
    assert match(Command('git push', '''
error: failed to push some refs to 'https://github.com/nvbn/thefuck.git'
! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/nvbn/thefuck.git'
! [rejected]        master -> master (stale info)
'''))

# Generated at 2022-06-14 10:22:22.739740
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
        "To ..\n ! [rejected] master -> master (non-fast-forward)\n"
        "error: failed to push some refs to '..'\n"
        "hint: Updates were rejected because the tip of your current branch is behind \n"
        "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
        "hint: 'git pull ...') before pushing again.\n"
        "hint: See the 'Note about fast-forwards' in 'git push --help' for details\n"))

# Generated at 2022-06-14 10:22:33.138858
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git push',
                                    'To git@github.com:nvbn/thefuck.git\n'
                                    ' ! [rejected]        feature -> feature '
                                    '(non-fast-forward)\n'
                                    'error: failed to push some refs to '
                                    '\'git@github.com:nvbn/thefuck.git\'\n'
                                    'To prevent you from losing history, non-fast'
                                    '-forward updates were rejected\n'
                                    'Merge the remote changes (e.g. \'git pull\')'
                                    ' before pushing again.  See the\n'
                                    '\'Note about fast-forwards\' section of '
                                    '\'git push --help\' for details.\n'))
            == 'git pull')

# Generated at 2022-06-14 10:22:35.451889
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git push', '', '')) ==
            'git pull')

# Generated at 2022-06-14 10:22:46.570341
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command('git push origin master', '', 'git: \'origin\' '
                                                   'does not appear to be '
                                                   'a git repository...'
                                                   'failed to push some '
                                                   'refs to \'https://'
                                                   'github.com/SidharthArya/'
                                                   'thefuck.git\'')
    assert get_new_command(command1) == 'git pull && git push origin master'

    command2 = Command('git push', 'Failed to push branch origin',
                       'git: \'origin\' does not appear to be a git '
                       'repository...failed to push some refs to '
                       '\'https://github.com/SidharthArya/thefuck.git\'')

# Generated at 2022-06-14 10:22:53.120347
# Unit test for function match
def test_match():
    assert match(Command('git push', "! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\n  another branch, or bitbucked by a push that can not be fast-forwarded.\n "))

# Generated at 2022-06-14 10:23:00.076549
# Unit test for function match
def test_match():
    assert match(Command('git push', '\n ! [rejected] master -> master (fetch first)\n\nerror: failed to push some refs to \'https://github.com/njuzhang/test.git\'\nhint: Updates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))


# Generated at 2022-06-14 10:23:08.161975
# Unit test for function match