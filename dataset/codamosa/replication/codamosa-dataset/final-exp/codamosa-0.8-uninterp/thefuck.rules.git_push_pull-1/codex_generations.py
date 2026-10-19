

# Generated at 2022-06-14 10:14:06.150768
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'To git@github.com:nvbn/thefuck.git\n ! [rejected] master -> master (fetch first)\nerror: failed to push some refs to \'git@github.com:nvbn/thefuck.git\'\nhint: Updates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))


# Generated at 2022-06-14 10:14:11.064930
# Unit test for function get_new_command
def test_get_new_command():
    # return 'git pull && git push'
    assert get_new_command('git push') == 'git pull && git push'
    assert get_new_command('git push origin') == 'git pull && git push origin'
    assert get_new_command('git push origin master') == 'git pull && git push origin master'

# Generated at 2022-06-14 10:14:19.720213
# Unit test for function match
def test_match():
    command = Command('git push origin develop',
                      '''
                      ! [rejected]        develop -> develop (non-fast-forward)
                      error: failed to push some refs to 'git@example.com:repo.git'
                      hint: Updates were rejected because the tip of your current branch is behind
                      hint: its remote counterpart. Integrate the remote changes (e.g.
                      hint: 'git pull ...') before pushing again.
                      hint: See the 'Note about fast-forwards' in 'git push --help' for details.
                      ''')
    assert match(command)


# Generated at 2022-06-14 10:14:21.904975
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'

# Generated at 2022-06-14 10:14:23.541758
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull'

# Generated at 2022-06-14 10:14:36.181405
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'Username for \'https://github.com\': ! [rejected]        master -> master (fetch first)',
                         'error: failed to push some refs to \'https://github.com/stuxcrystal/thefuck.git\'',
                         'hint: Updates were rejected because the tip of your current branch is behind',
                         'hint: its remote counterpart. Integrate the remote changes (e.g.',
                         'hint: \'git pull ...\') before pushing again.',
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))
    assert not match(Command('git commit', '', ''))

# Generated at 2022-06-14 10:14:37.942864
# Unit test for function get_new_command
def test_get_new_command():
	command = Command('git push')
	assert get_new_command(command) == 'git pull'

# Generated at 2022-06-14 10:14:43.813186
# Unit test for function match
def test_match():
    assert match(Command('git branch'))
    assert match(Command('git push origin master'))
    assert match(Command('git push'))
    assert not match(Command('git config --global user.name "System Failure"'))
    assert not match(Command('git config user.name "System Failure"'))


# Generated at 2022-06-14 10:14:49.287563
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git push origin master', 
                                   output=' ! [rejected]        master -> master (fetch first)')) == 'git pull origin master && git push origin master'
    assert get_new_command(Command(script='git push origin master', 
                                   output=' ! [rejected]        master -> master (non-fast-forward)')) == 'git pull origin master && git push origin master'
    assert get_new_command(Command(script='git push origin master', 
                                   output=' ! [rejected]        master -> master (fetch first)')) == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:15:05.149282
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master '
                         '(non-fast-forward)',
                         ' error: failed to push some refs to '
                         '\'git@github.com:yemyat/thefuck.git\'\n'
                         ' hint: Updates were rejected because the tip of '
                         'your current branch is behind\n'
                         ' hint: its remote counterpart. '
                         'Integrate the remote changes (e.g.\n'
                         ' hint: \'git pull ...\') before pushing again.\n'
                         ' hint: See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.'))

# Generated at 2022-06-14 10:15:20.541265
# Unit test for function match
def test_match():
    assert match(Command('git push',
            output=' ! [rejected]        master -> master (non-fast-forward)\n'
            'error: failed to push some refs to "git@git.example.com:7rlo977/example.git"'
            '\nTo prevent you from losing history, non-fast-forward updates were rejected'
            '\nMerge the remote changes (e.g. \'git pull\') before pushing again.'
            '\nSee the \'Note about fast-forwards\' section of \'git push --help\' for details.'))

# Generated at 2022-06-14 10:15:21.927682
# Unit test for function match
def test_match():
    assert match(Command('git push', 'error'))


# Generated at 2022-06-14 10:15:26.448001
# Unit test for function match
def test_match():
    assert match('git push -u origin master')
    assert match('git push origin lib:lib')
    assert match('git push --force')
    assert not match('git push origin')



# Generated at 2022-06-14 10:15:31.055301
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('git push',
                                'Updates were rejected because the tip of your current branch is behind'))
    assert 'git pull' in new_command
    assert 'git push' not in new_command


# Generated at 2022-06-14 10:15:38.556787
# Unit test for function get_new_command
def test_get_new_command():
	script = 'git push'
	command = '! [rejected]\nUpdates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nSee the \'Note about fast-forwards\' in \'git push --help\' for details.'
	new_command = get_new_command(script, command)
	if new_command != 'git pull && git push':
		print('Error!')

# Generated at 2022-06-14 10:15:49.931927
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command('git push origin master', "Some output including"
                       "'! [rejected]' and 'failed to push some refs to'")
    command2 = Command('git push origin master', "Some output including"
                       "'! [rejected]' 'failed to push some refs to' "
                       "'Updates were rejected because the tip of your"
                       " current branch is behind'")

    command3 = Command('git push origin master', "Some output including"
                       "'! [rejected]' 'failed to push some refs to' "
                       "'Updates were rejected because the remote "
                       "contains work that you do'")

    assert get_new_command(command1) == 'git pull && git push origin master'
    assert get_new_command(command2) == 'git pull && git push origin master'
    assert get_new

# Generated at 2022-06-14 10:15:55.220635
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert (get_new_command(Command('git push',
                                'remote: Permission to user/repo.git denied to otheruser.\nfatal: unable to access \'https://github.com/user/repo.git/\': The requested URL returned error: 403'))
            == 'git pull && git push')

# Generated at 2022-06-14 10:16:04.329280
# Unit test for function match
def test_match():
    assert match(Command('pus'))
    assert match(Command('push'))
    assert match(Command('  push'))
    assert match(Command('push  '))
    assert match(Command('push -f'))
    assert match(Command('git push'))
    assert match(Command('git push -f'))
    assert match(Command('git push origin master'))

    assert not match(Command('git push origin'))
    assert not match(Command('git push origin develop'))
    assert not match(Command('git push -f origin master'))



# Generated at 2022-06-14 10:16:07.240275
# Unit test for function get_new_command
def test_get_new_command():
    c = Command('git push', '! [rejected]        master -> master (non-fast-forward)')
    assert get_new_command(c) == 'git pull && git push'

# Generated at 2022-06-14 10:16:15.177219
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind'))
    assert match(Command('git push', 'Updates were rejected because the remote contains work that you do'))
    assert not match(Command('git pull', 'Updates were rejected because the tip of your current branch is behind'))
    assert not match(Command('git fetch', 'Updates were rejected because the tip of your current branch is behind'))


# Generated at 2022-06-14 10:16:31.141136
# Unit test for function match

# Generated at 2022-06-14 10:16:38.477734
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', '! [rejected] master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/python/peps.git\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert 'git pull; git push' == get_new_command(command)

# Generated at 2022-06-14 10:16:40.943819
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(command.Command('git push')) ==
           shell.and_('git pull', 'git push'))

# Generated at 2022-06-14 10:16:47.430799
# Unit test for function match
def test_match():
    assert match(Command('git push origin/master', "! [rejected]        master -> master (fetch first)\nUpdates were rejected because the remote contains work that you do\nhint: not see.\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart."))
    assert not match(Command('git push origin/master', "Everything up-to-date"))
    assert not match(Command('git push origin/master', "Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart."))

# Generated at 2022-06-14 10:16:49.478751
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command([u'git push']) == u'git pull && git push'

# Generated at 2022-06-14 10:17:00.853832
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '''
! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:my/repo.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''))

# Generated at 2022-06-14 10:17:12.814000
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '', '! [rejected]        master -> master (non-fast-forward)\n'
                                                 'error: failed to push some refs to \'git@github.com:...\'')) == 'git pull && git push'
    assert get_new_command(Command('git push', '', '! [rejected]        master -> master (fetch first)\n'
                                                 'error: failed to push some refs to \'git@github.com:...\'')) == 'git pull && git push'

# Generated at 2022-06-14 10:17:21.512859
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push',
                                   '! [rejected]        master -> master'
                                   '(non-fast-forward)\n'
                                   'error: failed to push some refs to...',
                                   '')) == 'git pull && git push'
    assert get_new_command(Command('git push origin master',
                                   '! [rejected]        master -> master'
                                   '(non-fast-forward)\n'
                                   'error: failed to push some refs to...',
                                   '')) == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:17:30.935346
# Unit test for function match
def test_match():
    command = Command('git push origin master',
                      'To https://github.com/nvbn/thefuck.git\n'
                      ' ! [rejected]        master -> master (non-fast-forward)\n'
                      'error: failed to push some refs to '
                      '\'https://github.com/nvbn/thefuck.git\''
                      '\nhint: Updates were rejected '
                      'because the tip of your current branch is behind')
    assert match(command)

# Generated at 2022-06-14 10:17:44.173248
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', 1))
    assert match(Command('git push origin master ', '', 1))
    assert match(Command('git push origin master\n', '', 1))
    assert match(Command('git push origin master',
                         '! [rejected]\nfailed to push some refs to', 1))
    assert match(Command('git push origin master',
                         '! [rejected]\nfailed to push some refs to', 1))
    assert match(Command('git push origin master',
                         'Updates were rejected because the tip of your '
                         'current branch is behind', 1))
    assert match(Command('git push origin master',
                         'Updates were rejected because the remote '
                         'contains work that you do', 1))

# Generated at 2022-06-14 10:18:04.911917
# Unit test for function match

# Generated at 2022-06-14 10:18:08.733778
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected]', ''))
    assert match(Command('git push', '! [rejected]', ''))
    assert not match(Command('git push', '', ''))


# Generated at 2022-06-14 10:18:11.452781
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command("git push", "failed to push some refs to"))
            == 'git pull && git push')

# Generated at 2022-06-14 10:18:26.218510
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'To https://github.com/nvbn/thefuck\n'
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to '
                         '\'https://github.com/nvbn/thefuck\'\n'
                         'hint: Updates were rejected because the tip'
                         ' of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the '
                         'remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' '
                         'in \'git push --help\' for details.\n'))

# Generated at 2022-06-14 10:18:36.462853
# Unit test for function match
def test_match():
    assert match(command(script='git push origin master',
                         output=' ! [rejected]        master -> master (non-fast-forward)'))
    assert match(command(script='git push origin master',
                         output='failed to push some refs to origin'))
    assert match(command(script='git push origin master',
                         output='To git@github.com:nvbn/thefuck.git ! [rejected] master -> master (fetch first)'))
    assert match(command(script='git push origin master',
                         output=' ! [rejected]        master -> master (fetch first)'))

# Generated at 2022-06-14 10:18:42.393494
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command(Command('git push', 'Updates were rejected because the tip')) == 'git pull'
	assert get_new_command(Command('git push', 'Updates were rejected because the remote ')) == 'git pull'
	assert get_new_command(Command('git push', 'Updates were rejected because the t')) == 'git pull'

# Generated at 2022-06-14 10:18:50.059103
# Unit test for function match
def test_match():
    assert match(Command('git push', "To https://github.com/bar/foo.git\n ! [rejected]        master -> master (fetch first)\nerror: failed to push some refs to 'https://github.com/bar/foo'\nhint: Updates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.", ""))

# Generated at 2022-06-14 10:19:01.766968
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master (non-fast-forward)',
                         'error: failed to push some refs to',
                         '''To git@github.com:nvbn/thefuck.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:nvbn/thefuck.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''))

# Generated at 2022-06-14 10:19:13.635484
# Unit test for function match
def test_match():
    assert match(Command('git push origin dev:dev', '', '', 0, ''))
    assert match(Command(
        'git push origin dev', '! [rejected]        dev -> dev (fetch first)',
        '', 0, ''))
    assert match(Command(
        'git push origin dev',
        'error: failed to push some refs to \'git@git.example.com:lucas/dev.git\'',
        '', 0, ''))
    assert match(Command(
        'git push origin dev', '! [rejected]        dev -> dev (non-fast-forward)',
        'error: failed to push some refs to \'git@git.example.com:lucas/dev.git\'',
        0, ''))

# Generated at 2022-06-14 10:19:24.088940
# Unit test for function get_new_command
def test_get_new_command():
    assert git_support(match)(Command('git push')) == True
    assert git_support(get_new_command)(Command('git push', '! [rejected]\n'
                                                          'failed to push som '
                                                          'refs to\n',
                                                 'Updates were rejected '
                                                 'because the tip of your '
                                                 'current branch is behind')) == 'git pull && git push'
    assert git_support(get_new_command)(Command('git push', '! [rejected]\n'
                                                          'failed to push som '
                                                          'refs to\n',
                                                 'Updates were rejected '
                                                 'because the remote contains work that you do')) == 'git pull && git push'


# Generated at 2022-06-14 10:19:57.568693
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'To https://github.com/user/repo\n ! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/user/repo\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))



# Generated at 2022-06-14 10:20:11.720737
# Unit test for function match

# Generated at 2022-06-14 10:20:23.973976
# Unit test for function match
def test_match():
    assert match(Command('git push', '\n ! [rejected]        master -> master (non-fast-forward)\n'
                                      'error: failed to push some refs to \'git@github.com:Soong/dotfiles.git\'\n'
                                      'hint: Updates were rejected because the tip of your current branch is behind\n'
                                      'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                                      'hint: \'git pull ...\') before pushing again.\n'
                                      'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))


# Generated at 2022-06-14 10:20:33.643416
# Unit test for function match
def test_match():
    assert match(command=Command('git push', '! [rejected]        master -> master (fetch first)'))
    assert match(command=Command('git push', '! [rejected]        master -> master (non-fast-forward)'))
    assert match(command=Command('git push', 'Updates were rejected because the tip of your current branch is behind'))
    assert match(command=Command('git push', 'Updates were rejected because the remote contains work that you do'))
    assert not match(command=Command('git push', 'Updates were rejected because the tip of your current branch is behind'))
    assert not match(command=Command('git push', 'Updates were rejected because the remote contains work that you do'))

# Generated at 2022-06-14 10:20:35.199330
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git pull' in get_new_command(Command('git push', '', ''))

# Generated at 2022-06-14 10:20:48.117994
# Unit test for function match

# Generated at 2022-06-14 10:21:00.202092
# Unit test for function match
def test_match():
	assert not match(Command('git push', '', '', 0, None))
	assert not match(Command('', '', '', 0, None))
	assert not match(Command('git push', "failed to push some refs to 'https://git.fau.de/gitlab/java-projekt/tipp-app.git'\nTo prevent you from losing history, non-fast-forward updates were rejected\nMerge the remote changes before pushing again.  See the 'Note about\nfast-forwards' section of 'git push --help' for details.", '', 0, None))

# Generated at 2022-06-14 10:21:11.230010
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', 'error: failed to push some refs to\n'))
    assert match(Command('git push', 'error: failed to push some refs to\n'))
    assert match(Command('git push origin master',
                         'error: failed to push some refs to\nUpdates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\n'))

# Generated at 2022-06-14 10:21:22.698563
# Unit test for function match
def test_match():
    assert match(Command('git push --set-upstream origin master',
                         'hint: Updates were rejected because the remote '
                         'contains work that you do hint: not have locally. This is '
                         'usually caused by another repository pushing hint: to the same'
                         ' ref. You may want to first integrate the hint: remote changes '
                         '(e.g., hint: ''git pull ...'') before pushing again. hint: See '
                         'the ''Note about fast-forwards'' in ''git push'' for details.'))

# Generated at 2022-06-14 10:21:29.340180
# Unit test for function match
def test_match():
    command = Command('wget https://httpbin.org/status/418')
    assert match(command)
    command = Command('wget https://httpbin.org/status/418',
                      'I\'m a teapot')
    assert not match(command)
    command = Command('wget https://httpbin.org/status/418',
                      'I\'m a teapot',
                      'wget: missing URL')
    assert not match(command)

# Generated at 2022-06-14 10:22:17.939746
# Unit test for function get_new_command
def test_get_new_command():
    command = "git push"
    output = "! [rejected]        master -> master (non-fast-forward) error: failed to push some refs to 'git@github.com:repo.git' hint: Updates were rejected because the tip of your current branch is behind hint: its remote counterpart. Integrate the remote changes (e.g. hint: 'git pull ...') before pushing again. hint: See the 'Note about fast-forwards' in 'git push --help' for details."
    assert get_new_command(Command(command,output)) == "git pull && git push"

# Generated at 2022-06-14 10:22:24.897986
# Unit test for function match
def test_match():
    file = open("tests/specific/git/push_pull_test.txt")
    output = file.read()

    assert match(Command('git push origin master', output=output))
    assert match(Command('git push origin HEAD', output=output))
    assert match(Command('git push origin HEAD:master', output=output))
    assert match(Command('git push origin master:master', output=output))
    assert match(Command('git push origin --all', output=output))
    assert match(Command('git push origin --tags', output=output))
    assert match(Command('git push --tags', output=output))
    assert match(Command('git push', output=output))
    assert not match(Command('git commit', output=output))
    assert not match(Command('git push', output=output))

# Generated at 2022-06-14 10:22:31.877039
# Unit test for function match
def test_match():
    assert (match(Command('git push origin master', '', ' ! [rejected]', 1, 5))
            is True)
    assert (match(Command('git push -u origin master', '', '', 1, 5))
            is False)
    assert (match(Command('git add', '', '', 1, 5))
            is False)


# Generated at 2022-06-14 10:22:35.805475
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind'))
    assert not match(Command('git commit', 'Updates were rejected because the tip of your current branch is behind'))
    assert match(Command('git push', 'Updates were rejected because the remote contains work that you do'))

# Generated at 2022-06-14 10:22:37.975575
# Unit test for function get_new_command
def test_get_new_command():
    assert('git pull && git push' == get_new_command(Command('git push',
        '')))

# Generated at 2022-06-14 10:22:49.691962
# Unit test for function match
def test_match():
    gitscript = "git push"
    out1 = "To ssh://repo.or.cz/srv/git/sitadel.git ! [rejected] master -> master (non-fast-forward)\nupdates were rejected because the remote contains work that you do not have locally"
    out2 = "To ssh://repo.or.cz/srv/git/sitadel.git ! [rejected] master -> master (non-fast-forward)\nupdates were rejected because the tip of your current branch is behind"

    assert match(CliCommand(gitscript, out1))
    assert match(CliCommand(gitscript, out2))
    assert not match(CliCommand('ls', ''))


# Generated at 2022-06-14 10:22:53.122990
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git pull && git push' in get_new_command('git push')
    assert 'git pull' in get_new_command('git push')
    assert get_new_command('git push') is not None

# Generated at 2022-06-14 10:23:01.152107
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master',
        '')) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:23:09.351748
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
            '''! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:...................'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.'''))

# Generated at 2022-06-14 10:23:12.436211
# Unit test for function get_new_command