

# Generated at 2022-06-14 10:14:06.045676
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         output='! [rejected]        master -> master (non-fast-forward)\n'
                                'error: failed to push some refs to \'git@github.com:mislav/git-ui.git\'\n'
                                'Updates were rejected because the tip of your current branch is behind\n'
                                'its remote counterpart. Integrate the remote changes (e.g.\n'
                                '\'git pull ...\') before pushing again.\n'
                                'See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))

# Generated at 2022-06-14 10:14:15.020520
# Unit test for function match
def test_match():
    assert match(Command("git push", "! [rejected] master -> master (fetch first)\n"
                                     "error: failed to push some refs to 'git@github.com:IanMurfin/git_scripts.git'\n"
                                     "hint: Updates were rejected because the remote contains work that you do\n"
                                     "hint: not have locally. This is usually caused by another repository pushing\n"
                                     "hint: to the same ref. You may want to first integrate the remote changes\n"
                                     "hint: (e.g., 'git pull ...') before pushing again.\n"
                                     "hint: See the 'Note about fast-forwards' in 'git push --help' for details."
            ))


# Generated at 2022-06-14 10:14:27.999488
# Unit test for function get_new_command

# Generated at 2022-06-14 10:14:35.177670
# Unit test for function match
def test_match():
    assert match(Command('git push origin master:foo', '', '', 2))
    assert match(Command('git push origin master', '', '', 2))
    assert not match(Command('git pull origin master:foo', '', '', 2))
    assert not match(Command('git pull origin master', '', '', 2))
    assert not match(Command('git push', '', '', 2))
    assert not match(Command('push', '', '', 2))


# Generated at 2022-06-14 10:14:41.219562
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to '
                         '\'https://github.com/github/hubot.git\'\n'
                         'To prevent you from losing history, non-fast-forward updates were rejected\n'
                         'Merge the remote changes (e.g. \'git pull\') before pushing again.  See\n'
                         'the \'Note about fast-forwards\' section of \'git push --help\' for details.\n'))


# Generated at 2022-06-14 10:14:53.322301
# Unit test for function match
def test_match():
    assert (match(Command('git push origin master',
                          ' ! [rejected]        master -> master (non-fast-forward)',
                          err='error',
                          in_progress=False))
            is False)
    assert (match(Command('git push origin master',
                          ' ! [rejected]        master -> master (non-fast-forward)',
                          err='error',
                          in_progress=True))
            is False)
    assert (match(Command('git push',
                          ' ! [rejected]        master -> master (non-fast-forward)',
                          err='error',
                          in_progress=False))
            is False)

# Generated at 2022-06-14 10:15:05.181530
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
	'''To https://github.com/AooJ/git-push-pull-with-rebase.git
    55e50ae..29aef51  master -> master
    ! [rejected]        master -> master (non-fast-forward)
    error: failed to push some refs to 'https://github.com/AooJ/'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Integrate the remote changes (e.g.
    hint: 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    '''))


# Generated at 2022-06-14 10:15:07.241628
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master')) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:15:10.616807
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git push origin master')) ==
            shell.and_('git pull origin master', 'git push origin master'))



# Generated at 2022-06-14 10:15:15.706612
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git push'
    new_command = 'git pull && git push'
    command = Command(script, 'Updates were rejected because the tip of your current branch is behind its remote')
    assert get_new_command(command) == new_command

# Generated at 2022-06-14 10:15:26.731580
# Unit test for function match

# Generated at 2022-06-14 10:15:38.595154
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'To https://github.com/user/repo\n! [rejected] master -> master (fetch first)\n',
                         '', 1))
    assert not match(Command('git push origin master', '', '', 1))
    assert match(Command('git push origin master',
                         "To https://github.com/user/repo\n! [rejected] master -> master (fetch first)\n",
                         "error: failed to push some refs to 'git@github.com:user/repo'\nhint: Updates were rejected because the tip of your current branch is behind\n", 1))

# Generated at 2022-06-14 10:15:54.011582
# Unit test for function match
def test_match():
    assert match(Command('git push origin master:master',
                         'Everything up-to-date'))

# Generated at 2022-06-14 10:16:00.256476
# Unit test for function get_new_command
def test_get_new_command():
    result = get_new_command(Command(script='git push', output='Updates were rejected because the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes before pushing again.'))
    assert result == 'git pull && git push'

enabled_by_default = True

# Generated at 2022-06-14 10:16:08.664438
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected] master -> master (fetch first)\n'
                         'error: failed to push some refs to\''
                         'origin\'\n'
                         'Updates were rejected because '
                         'the tip of your current branch is behind'
                         'its remote\n'
                         'hint: '
                         'Fetching the remote branch will allow you '
                         'to perform the update cleanly.\n'
                         'hint: See the \'Note about '
                         'fast-forwards\' in git push --help for '
                         'details.'))
    assert not match(Command('git status', ''))

# Generated at 2022-06-14 10:16:16.063528
# Unit test for function match
def test_match():
    assert match(Command("git push -u origin master",
                         "To http://github.com/nvie/gitflow.git\n ! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to 'git@github.com:nvie/gitflow.git'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.\n",
                         "git push -u origin master"))


# Generated at 2022-06-14 10:16:28.409597
# Unit test for function match

# Generated at 2022-06-14 10:16:41.156105
# Unit test for function match
def test_match():
    assert match(Command('git push origin branch',
                ' ! [rejected]        dev -> dev (non-fast-forward)',
                'error: failed to push some refs to'
                ' \'http://github.com/user/repo\'',
                'hint: Updates were rejected because the tip of your current'
                ' branch is behind',
                'hint: its remote counterpart. Integrate the remote changes'
                ' (e.g.',
                'hint: git pull ...) before pushing again.',
                'hint: See the \'Note about fast-forwards\' in '
                '\'git push --help\' for details.'))


# Generated at 2022-06-14 10:16:52.130861
# Unit test for function match
def test_match():
    assert match(command=Command('foo', '', '')) == False
    assert match(Command('git push', '', '')) == False
    assert match(Command('git push', '', '! [rejected] master -> master (non-fast-forward)\n'
                                           'error: failed to push some refs to \'https://github.com/mgechev/angular-seed.git\'\n'
                                           'hint: Updates were rejected because the tip of your current branch is behind\n'
                                           'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                                           'hint: \'git pull ...\') before pushing again.\n'
                                           'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')) == True

# Generated at 2022-06-14 10:17:03.789026
# Unit test for function match
def test_match():
    assert not match(Command('git push origin master'))
    assert match(Command('git push origin master',
                         'To git@github.com:nvbn/thefuck.git\n ! [rejected] '
                         'master -> master (non-fast-forward)\n error: failed '
                         'to push some refs to '
                         '\'git@github.com:nvbn/thefuck.git\'\n '
                         'hint: Updates were rejected because the tip of your '
                         'current branch is behind\n hint: its remote '
                         'counterpart. Integrate the remote changes (e.g.\n '
                         'hint: \'git pull ...\') before pushing again.\n '
                         'hint: See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.'))
   

# Generated at 2022-06-14 10:17:21.674683
# Unit test for function match
def test_match():
    assert match(Command('git push', 'fatal: The current branch master has no upstream branch.\n'
                                      'To push the current branch and set the remote as upstream, use\n'
                                      '\n'
                                      '    git push --set-upstream origin master\n'
                                      '\n'))

# Generated at 2022-06-14 10:17:23.858330
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('git push')
    assert get_new_command(cmd) == 'git pull'

# Generated at 2022-06-14 10:17:35.485723
# Unit test for function match
def test_match():
    assert match(Command(script='git push',
                         output=' ! [rejected]        master -> master '
                                '(non-fast-forward)\n'
                                'error: failed to push some refs to '
                                '\'git@gitlab.com:wiktort/TheFuck.git\'\n'
                                'To prevent you from losing history, '
                                'non-fast-forward updates were rejected\n'
                                'Merge the remote changes (e.g. \'git pull\') '
                                'before pushing again.  See the \'Note about '
                                'fast-forwards\' section of \'git push '
                                '--help\' for details.\n'))

# Generated at 2022-06-14 10:17:45.875863
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected]        master -> master (non-fast-forward)\n'
                                     'error: failed to push some refs to \'https://github.com/oshliaer/dotfiles\'.\n'
                                     'hint: Updates were rejected because the tip of your current branch is behind\n'
                                     'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                                     'hint: \'git pull ...\') before pushing again.\n'
                                     'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))

# Generated at 2022-06-14 10:17:56.748047
# Unit test for function match
def test_match():
    assert not match(Command('git br', stderr=''))
    assert match(Command('git push', stderr=(
        '! [rejected]   master -> master (non-fast-forward)\n'
        'error: failed to push some refs to \'https://github.com/nvbn/thefuck\'')))
    assert match(Command('git push', stderr=(
        '! [rejected]   master -> master (non-fast-forward)\n'
        'error: failed to push some refs to \'https://github.com/nvbn/thefuck\'')))

# Generated at 2022-06-14 10:18:08.482451
# Unit test for function get_new_command

# Generated at 2022-06-14 10:18:13.193986
# Unit test for function get_new_command
def test_get_new_command():
    assert git_support.get_new_command(git_support.Command('git push','/','git push','','','','','','','','','! [rejected]\nUpdates were rejected because the tip of your current branch is behind')) == 'git pull && git push'


# Generated at 2022-06-14 10:18:18.268228
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', ''))
    assert not match(Command('git push origin master', '',
                             '\nEverything up-to-date'))
    assert not match(Command('git pull origin master', '', ''))

# Generated at 2022-06-14 10:18:31.862701
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                    'Updates were rejected because the tip of your '
                    'current branch is behind its remote counterpart.'
                    'Use `git push --set-upstream origin master`'
                    ' to set the upstream branch'))
    assert match(Command('git push origin master',
                         'Updates were rejected because the remote contains'
                         ' work that you do not have locally.'
                         'This is usually caused by another repository pushing'
                         ' to the same ref. You may want to first integrate'
                         ' the remote changes (e.g., `git pull ...`) before'
                         ' pushing again.'
                         'See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.'))
    assert not match(Command('git push origin master', ''))

# Generated at 2022-06-14 10:18:38.473969
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                                 '''To git@github.com:foobar/hellogitworld.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:foobar/hellogitworld.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Merge the remote changes (e.g.
hint: 'git pull') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''))


# Generated at 2022-06-14 10:18:56.572377
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'To https://github.com/nvbn/thefuck\n'
                         ' ! [rejected]        master -> master (fetch first)\n'
                         'error: failed to push some refs to \'https://github.com/nvbn/thefuck\'\n'
                         'hint: Updates were rejected because the remote contains work that you do\n'
                         'hint: not have locally. This is usually caused by another repository pushing\n'
                         'hint: to the same ref. You may want to first integrate the remote changes\n'
                         'hint: (e.g., \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))


# Generated at 2022-06-14 10:19:01.876882
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('') == 'git pull'
    assert get_new_command('git push -u origin master') == 'git pull && git push -u origin master'
    assert get_new_command('git push origin master') == 'git pull && git push origin master'
    assert get_new_command('git push --set-upstream origin master') == 'git pull && git push --set-upstream origin master'

# Generated at 2022-06-14 10:19:08.148714
# Unit test for function get_new_command
def test_get_new_command():
    with patch('thefuck.rules.git_push_failed.shell') as shell_mock:
        shell_mock.and_ = Mock(return_value='thefuck git pull')
        command = Mock(script='git push', output='Updates were rejected because the tip of your current branch is behind')
        assert get_new_command(command) == 'thefuck git pull'



# Generated at 2022-06-14 10:19:10.997749
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git push') == 'git pull && git push'
	assert get_new_command('git push origin master') == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:19:12.553809
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master').script == 'git pull origin master'

# Generated at 2022-06-14 10:19:22.605802
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected] master -> master (fetch first)', 'git push'))
    assert match(Command('git push', '! [rejected] master -> master (non-fast-forward)', 'git push'))
    assert match(Command('git push', 'error: failed to push some refs to', 'git push'))
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind', 'git push'))
    assert match(Command('git push', 'Updates were rejected because the remote contains work that you do', 'git push'))
    assert not match(Command('ls', '! [rejected] master -> master (fetch first)', 'git push'))


# Generated at 2022-06-14 10:19:33.584124
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected] master -> master (fetch first)\n'
                                     'error: failed to push some refs to \'https://github.com/user/repo.git\''
                                     '\nUpdates were rejected because the remote contains work that you do'
                                     '\nhint: not want. Merge the remote changes (e.g. \'git pull\')'
                                     '\nhint: before pushing again.\nhint: See the \'Note about fast-forwards\' in '
                                     '\nhint: \'git push --help\' for details.'))

# Generated at 2022-06-14 10:19:43.902321
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master', 'git push origin master ! [rejected] master -> master (non-fast-forward) error: failed to push some refs to \'https://github.com/ccorcos/thefuck.git\' hint: Updates were rejected because the tip of your current branch is behind hint: its remote counterpart. Integrate the remote changes (e.g. hint: \'git pull ...\') before pushing again. hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')) == shell.and_('git pull origin master', 'git push origin master')

# Generated at 2022-06-14 10:19:58.697461
# Unit test for function get_new_command
def test_get_new_command():
    output = '''
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:nvbn/thefuck.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

'''
    script = "git push"
    command = Command(script, output)
    assert get_new_command(command) == "git pull & git push"

# Generated at 2022-06-14 10:20:10.282312
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', '! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to \'git@github.com:MunGell/awesome-for-beginners.git\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:20:32.370517
# Unit test for function match

# Generated at 2022-06-14 10:20:42.754596
# Unit test for function match
def test_match():
  script1 = "git push"
  script2 = "git push -f"
  script3 = "git push origin master"
  script4 = "git push -u origin master"
  script5 = "git push --set-upstream origin master"
  script6 = "git push origin master:master"
  script7 = "git push -u origin br-feature"
  script8 = "git push origin br-feature:master"
  script9 = "git push origin br-feature:br-feature"
  script10 = "git push origin feature"
  script11 = "git push origin feature:master"
  script12 = "git push origin feature_branch:master"
  script13 = "git push origin feature_branch:feature_branch"
  script14 = "git push -u origin feature_branch"

# Generated at 2022-06-14 10:20:52.402721
# Unit test for function match
def test_match():
    command = Command('git push origin master',
                      'To https://github.com/nvbn/thefuck.git\n ! [rejected] master -> master (fetch first)\n error: failed to push some refs to \'https://github.com/nvbn/thefuck.git\'\n hint: Updates were rejected because the remote contains work that you do\n hint: not have locally. This is usually caused by another repository pushing\n hint: to the same ref. You may want to first integrate the remote changes\n hint: (e.g., \'git pull ...\') before pushing again.')
    assert match(command)

# Generated at 2022-06-14 10:21:05.631098
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
        "To git@github.com:nvbn/pyte.git\n ! [rejected]        master -> master (non-fast-forward)\n error: failed to push some refs to 'git@github.com:nvbn/pyte.git'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: 'git pull ...') before pushing again.\n hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n"))


# Generated at 2022-06-14 10:21:08.032400
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git push'
    print(get_new_command(script))
    assert get_new_command(script) == 'git pull && git push'

# Generated at 2022-06-14 10:21:20.210510
# Unit test for function get_new_command

# Generated at 2022-06-14 10:21:31.886703
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'fatal: The current branch master has no '
                         'upstream branch.\n'
                         'To push the current branch and set the remote as upstream, use\n'
                         '\n'
                         '    git push --set-upstream origin master\n'
                         '\n'
                         '! [rejected] master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to '
                         '\'git@github.com:nvbn/thefuck.git\''))


# Generated at 2022-06-14 10:21:43.990026
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         "! [rejected]        master -> master (non-fast-forward)\n"
                         "error: failed to push some refs to\n"
                         "'git@test.test.test:test/test.git)\n"
                         "hint: Updates were rejected because the tip of your\n"
                         "hint: current branch is behind its remote\n"
                         "hint: counterpart. Integrate the remote changes\n"
                         "hint: (e.g.\n"
                         "hint: 'git pull ...') before pushing again.\n"
                        ))

# Generated at 2022-06-14 10:21:53.848553
# Unit test for function match

# Generated at 2022-06-14 10:22:06.202607
# Unit test for function match
def test_match():
    if match(Command("git push origin master",output='To https://github.com/6/6.git\n! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/6/6.git\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n', stderr='error:\n')) == 'git pull origin master':
        print('test passed!')
    else:
        print('test failed!')

# Generated at 2022-06-14 10:22:39.602751
# Unit test for function match
def test_match():
    assert match(Command('git push', '', '', '', stderr='! [rejected] master -> master (non-fast-forward) \n'
    'error: failed to push some refs to \n'
    'Updates were rejected because the tip of your current branch is behind.'))
    assert match(Command('git push', '', '', '', stderr='! [rejected] master -> master (non-fast-forward) \n'
    'error: failed to push some refs to \n'
    'Updates were rejected because the remote contains work that you do not have locally. '))

# Generated at 2022-06-14 10:22:52.463465
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         "To https://github.com/nvbn/thefuck.git\n ! [rejected] master -> master (non-fast-forward)\n error: failed to push some refs to 'https://github.com/nvbn/thefuck.git'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: 'git pull ...') before pushing again.\n hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n",
                         ""))


# Generated at 2022-06-14 10:22:54.803775
# Unit test for function get_new_command
def test_get_new_command():
    git_script = "git push -f"
    assert get_new_command(Command(git_script, "", "")) == git_script

# Generated at 2022-06-14 10:23:08.216348
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (non-fast-forward)\
                         \n'
                         'error: failed to push some refs to \'git@gitlab.com:name/repo.git\'\
                         \n'
                         'hint: Updates were rejected because the tip of your \
                         \ncurrent branch is behind its remote counterpart. Integrate the \
                         \nremote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\
                         \n'
                         'hint: See the \'Note about fast-forwards\' in \'git push \
                         \n--help\' for details.\n'))

# Generated at 2022-06-14 10:23:10.388082
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git push', 'git pull')) ==
            'git pull && git push')

# Generated at 2022-06-14 10:23:13.047682
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master', '! [rejected] master -> master (non-fast-forward)')
    eq_(git_support.get_new_command(command), 'git pull && git push origin master')


# Generated at 2022-06-14 10:23:15.826986
# Unit test for function get_new_command
def test_get_new_command():
    command = "git push"
    command_correct = "git pull && git push"
    assert get_new_command(command) == command_correct

# Generated at 2022-06-14 10:23:29.417676
# Unit test for function get_new_command
def test_get_new_command():
    assert git.get_new_command(Command('git push',
                                       'To https://github.com/nvbn/thefuck.git\n'
                                       '! [rejected]        master -> master (non-fast-forward)\n'
                                       'error: failed to push some refs to '
                                       '\'https://github.com/nvbn/thefuck.git\'\n'
                                       'To prevent you from losing history, non-fast-forward updates were rejected\n'
                                       'Merge the remote changes (e.g. \'git pull\') before pushing again.  See the\n'
                                       '\'Note about fast-forwards\' section of \'git push --help\' for details.')) == 'git pull && git push'

# Generated at 2022-06-14 10:23:32.356857
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master:master', '', 1)) == 'git pull origin master:master && git push origin master:master'


# Generated at 2022-06-14 10:23:42.306257
# Unit test for function match
def test_match():
    assert(match(Command(script='git push origin master', 
        output='! [rejected] master -> master (non-fast-forward)\n\
 error: failed to push some refs to \'https://github.com/ElbenShira/Compiladores.git\'\n\
 hint: Updates were rejected because the tip of your current branch is behind\n\
 hint: its remote counterpart. Integrate the remote changes (e.g.\n\
 hint: \'git pull ...\') before pushing again.\n\
 hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')))
    