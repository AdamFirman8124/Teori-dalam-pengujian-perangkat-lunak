

# Generated at 2022-06-14 10:14:07.576743
# Unit test for function get_new_command

# Generated at 2022-06-14 10:14:18.633576
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         "To https://github.com/xxx/xxx.git\n ! [rejected]      HEAD -> master (non-fast-forward)\nerror: failed to push some refs to '',\n hint: Updates were rejected because the tip of your current branch is behind,\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: 'git pull ...') before pushing again.\n hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n"))

# Generated at 2022-06-14 10:14:29.869399
# Unit test for function match
def test_match():
    command = Command('git push origin develop',
                      'git push origin develop\n! [rejected]        develop -> develop (non-fast-forward)\n'
                      'error: failed to push some refs to "https://github.com/wuguanghua/test.git"\n'
                      'hint: Updates were rejected because the tip of your current branch is behind\n'
                      'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                      'hint: \'git pull ...\') before pushing again.\n'
                      'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert match(command)


# Generated at 2022-06-14 10:14:42.531439
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         stderr=' ! [rejected]        master -> master (fetch first)\n'
                                'error: failed to push some refs to \'git@example.org:test/test.git\'\n'
                                'hint: Updates were rejected because the remote contains work that you do\n'
                                'hint: not have locally. This is usually caused by another repository pushing\n'
                                'hint: to the same ref. You may want to first integrate the remote changes\n'
                                '(e.g.,\n'
                                'hint: \'git pull ...\') before pushing again.\n'
                                'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:14:45.614296
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '! [rejected]', 'error: failed to push some refs to')) == 'git pull && git push'

# Generated at 2022-06-14 10:14:50.631180
# Unit test for function get_new_command
def test_get_new_command():
    function = get_new_command
    assert function(Command('git push', '', '', 1, 2)) == 'git pull && ' \
           'git push'
    assert function(Command('git push origin master', '', '', 1, 2)) == \
           'git pull origin master && git push origin master'



# Generated at 2022-06-14 10:14:54.649202
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git push --force', '', '')),
            'git pull --force')

# Generated at 2022-06-14 10:15:06.254744
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'To https://github.com/nvbn/thefuck.git\n ! [rejected] master -> master (fetch first)\n error: failed to push some refs to \'https://github.com/nvbn/thefuck.git\'\n hint: Updates were rejected because the remote contains work that you do\n hint: not have locally. This is usually caused by another repository pushing\n hint: to the same ref. You may want to first integrate the remote changes\n hint: (e.g., \'git pull ...\') before pushing again.\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:15:11.577578
# Unit test for function match
def test_match():
    assert match(Command('git push', output='\'! [rejected]\''))
    assert not match(Command('git push', output='\'! [rejected] abc\''))
    assert not match(Command('git push', output='\'! [rejected] xyz\''))


# Generated at 2022-06-14 10:15:22.473073
# Unit test for function match
def test_match():
    assert match('git push')
    assert match('git push origin master')
    assert match('git push origin')
    assert match('git push -f')
    assert match('git push -u')
    assert match('git push -u origin master')
    assert match('git push --force')
    assert match('git push --force-with-lease')
    assert match('git -c color.ui=false push')
    assert match('git -c color.ui=true push')
    assert match('git push -o')
    assert match('git push -o simple')
    assert match('git push -o matching')
    assert match('git push -o upstream')
    assert match('git push -o nothing')
    assert match('git push origin HEAD:refs/for/master')

# Generated at 2022-06-14 10:15:35.782099
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git push origin master',
                                   output='! [rejected]        master -> master (non-fast-forward) \n error: failed to push some refs to \'git@github.com:anto23/Informatique-methodologie.git\' \n hint: Updates were rejected because the tip of your current branch is behind \n hint: its remote counterpart. Integrate the remote changes (e.g. \n hint: \'git pull ...\') before pushing again. \n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')) == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:15:42.976140
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:MaryamSa/Random-Quote-Machine.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:15:49.241956
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected] master -> master (non-fast-forward)',
                         'error: failed to push some refs to ''git@github.com:xxx/xxx.git''',
                         'Updates were rejected because the tip of your current branch is behind',
                         'Updates were rejected because the remote contains work that you do',
                         'To pull it',
                         'git pull'))



# Generated at 2022-06-14 10:15:50.971461
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', 0))


# Generated at 2022-06-14 10:15:58.810801
# Unit test for function match
def test_match():
    assert match(Command('git push',
        "! [rejected]        master -> master (non-fast-forward)\n"
        "error: failed to push some refs to 'https://github.com/tootallnate/test.git'\n"
        "hint: Updates were rejected because the tip of your current branch is behind\n"
        "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
        "hint: 'git pull ...') before pushing again.\n"
        "hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n"))


# Generated at 2022-06-14 10:16:08.858311
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '''
                         ! [rejected]        master -> master (non-fast-forward)
                         error: failed to push some refs to 'git@github.com:SineSim/fake-repo'
                         '''))

# Generated at 2022-06-14 10:16:11.653205
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master', 'fatal: git pull origin master')
    new_command = get_new_command(command)
    assert new_command == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:16:20.625513
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (non-fast-forward)',
                         'error: failed to push some refs to ''git@github.com:user/repo.git''',
                         'hint: Updates were rejected because the tip of your current branch is behind',
                         'hint: its remote counterpart. Integrate the remote changes ('', ''git pull...'') before pushing again.',
                         'hint: See the ''Note about fast-forwards'' in ''git push --help'' for details.'))



# Generated at 2022-06-14 10:16:24.236628
# Unit test for function match
def test_match():
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind', ''))
    assert not match(Command('git push', '', ''))

# Generated at 2022-06-14 10:16:27.824934
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git push origin master'
    new_command = replace_argument(command, 'push', 'pull')
    assert get_new_command(command) == shell.and_(new_command, command)

# Generated at 2022-06-14 10:16:34.136405
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin dev',
                                   'error: failed to push some refs to ...'),
                           None) == 'git pull origin dev && git push origin dev'

# Generated at 2022-06-14 10:16:44.624307
# Unit test for function match
def test_match():
    assert match(Command('git push some changes',
                         ' ! [rejected]        master -\> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:ai/hellogitworld.git\'',
                         '', 1))
    assert not match(Command('git push some changes', ' ! [rejected]        master -\> master (non-fast-forward)\n'
                                                      'error: failed to push some refs to \'https://github.com:ai/hellogitworld.git\'',
                             '', 1))

# Generated at 2022-06-14 10:16:50.299308
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git push', 'fatal: The current branch feature has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin feature\n')) == 'git pull && git push')


# Generated at 2022-06-14 10:17:01.203587
# Unit test for function match

# Generated at 2022-06-14 10:17:13.096119
# Unit test for function match
def test_match():
    # Test if function match works
    # Test if command has all the right arguments
    command = Command("git push tijs master", "Updates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g.hint: 'git pull ...') before pushing again.\nSee the 'Note about fast-forwards' in 'git push --help' for details.", "git", 0)
    assert match(command)
    # Test if command has all the right arguments

# Generated at 2022-06-14 10:17:24.020300
# Unit test for function match
def test_match():
    # Example of a command with no output and a script of "lol"
    assert match(Command('git push', '', '', stderr="error: failed to push some refs to 'git@github.com:Clement-L-G/Unused-Files-Remover.git'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details."))

    # Example of a command with no output and a script of "lol"

# Generated at 2022-06-14 10:17:35.642628
# Unit test for function match
def test_match():
    assert not match(Command('push', ''))
    assert not match(Command('git push', ''))
    assert not match(Command('git push', '! [rejected]\n'))
    assert not match(Command('git push',
                             '! [rejected]\n'
                             'failed to push some refs to\n'
                             'Updates were rejected because the tip'
                             ' of your current branch is behind\n'))
    assert match(Command('git push',
                         '! [rejected]\n'
                         'failed to push some refs to\n'
                         'Updates were rejected because the tip'
                         ' of your current branch is behind\n'
                         'Updates were rejected because the remote '
                         'contains work that you do\n'))


# Generated at 2022-06-14 10:17:39.262569
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'
    assert get_new_command('git push origin master') == 'git pull && git push origin master'

# Generated at 2022-06-14 10:17:42.819533
# Unit test for function match
def test_match():
	assert(match('git push origin development') == True)
	assert(match('git push origin development') == True)
	assert(match('git push origin master') == False)

# Generated at 2022-06-14 10:17:56.639313
# Unit test for function get_new_command
def test_get_new_command():
    with patch('thefuck.tools.get_all_executables', return_value=['git']):
        assert match(Command('git push'
                             ' ! [rejected]        master -> master (non-fast-forward)', '', 1, None))
        assert get_new_command(Command('git push'
                                       ' ! [rejected]        master -> master (non-fast-forward)', '', 1, None)) \
            == shell.and_('git pull && git push', 'git push')

        assert match(Command('git push'
                             ' ! [rejected]        master -> master (fetch first)', '', 1, None))
        assert get_new_command(Command('git push'
                                       ' ! [rejected]        master -> master (fetch first)', '', 1, None)) \
           

# Generated at 2022-06-14 10:18:12.581033
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '! [rejected]        master -> master (fetch first)',
                         'error: failed to push some refs to \'ssh://pfeilbr@'
                         'stash.bcbsnc.com/scm/~pfeilbr/gittest.git\'',
                         'hint: Updates were rejected because the tip of your'
                         ' current branch is behind',
                         'hint: its remote counterpart. Integrate the remote '
                         'changes (e.g.',
                         'hint: \'git pull ...\') before pushing again.',
                         'hint: See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.')) is not None

# Generated at 2022-06-14 10:18:19.760717
# Unit test for function match
def test_match():
    # command.script = 'git pull'
    # command.output = 'Updates were rejected because the tip of your current branch is behind'
    assert match(Command('git push origin master'))
    assert not match(Command('git pull'))
    assert match(Command('git push'))
    assert not match(Command('git push origin'))


# Generated at 2022-06-14 10:18:30.325506
# Unit test for function match
def test_match():
    assert not match(Command('echo hi', '', ''))
    assert match(Command('git push', '', '''error: failed to push some refs to 'git@github.com:repo/abc.git'
'''))
    assert match(Command('git push', '', '''error: failed to push some refs to 'git@github.com:repo/abc.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again.  See the
'Note about fast-forwards' section of 'git push --help' for details.
'''))

# Generated at 2022-06-14 10:18:38.796003
# Unit test for function match
def test_match():
    newcommand = "git push origin master"
    output = "! [rejected]        master -> master (non-fast-forward)\n\
 error: failed to push some refs to 'git@github.com:syl20bnr/spacemacs.git'\n\
 hint: Updates were rejected because the tip of your current branch is behind\n\
 hint: its remote counterpart. Integrate the remote changes (e.g.\n\
 hint: 'git pull ...') before pushing again.\n\
 hint: See the 'Note about fast-forwards' in 'git push --help' for details."
    assert match(Command(newcommand, output)) == True


# Generated at 2022-06-14 10:18:48.963699
# Unit test for function get_new_command
def test_get_new_command():
	# Test 1
	command = Command('git push', ' ! [rejected]        master -> master (non-fast-forward)\n'
								   'error: failed to push some refs to \'https://github.com/username/repo.git\'\n'
								   'hint: Updates were rejected because the tip of your current branch is behind\n'
								   'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
								   'hint: \'git pull ...\') before pushing again.\n'
								   'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')
	assert get_new

# Generated at 2022-06-14 10:18:51.150846
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master', '')) == 'git pull origin master && git push origin master'

# Generated at 2022-06-14 10:19:01.838559
# Unit test for function match
def test_match():
    output = '''To https://github.com/The-Fuck-Lang/fuck-Git.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/The-Fuck-Lang/fuck-Git.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''
    assert match(Command('git push', output))
    assert not match(Command('git push', '''Everything up-to-date
'''))

# Generated at 2022-06-14 10:19:13.659218
# Unit test for function match
def test_match():
    # Test check function
    assert match(Command('git push origin master',
              'To https://github.com/nvbn/thefuck\n ! [rejected]        master -> master (fetch first)\n error: failed to push some refs to \'https://github.com/nvbn/thefuck\'\n hint: Updates were rejected because the remote contains work that you do\n hint: not have locally. This is usually caused by another repository pushing\n hint: to the same ref. You may want to first integrate the remote changes\n hint: (e.g., \'git pull ...\') before pushing again.\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n',
              'nvbn@nvbn-linux:~/dev/thefuck$ '
    )) == True

# Generated at 2022-06-14 10:19:21.837462
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(shell.and_('git push', 'git push'),
                           'git push') == 'git pull & git push'
    assert get_new_command(shell.and_('git push origin master',
                                      'git push origin master'),
                           'git push origin master') == 'git pull origin master & git push origin master'
    assert get_new_command(shell.and_('git push', 'git push'),
                           'git push origin master') == 'git pull & git push origin master'

# Generated at 2022-06-14 10:19:28.154020
# Unit test for function match
def test_match():
    command = Command('git push', "git push To https://github.com/peterldowns/myrepo.git! [rejected]        master -> master (fetch first)\nUpdates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.")
    assert match(command) is True


# Generated at 2022-06-14 10:19:42.250676
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         "To https://github.com/nvbn/thefuck.git\n ! [rejected]        master -> master (fetch first)\nerror: failed to push some refs to 'git@github.com:nvbn/thefuck.git'\nhint: Updates were rejected because the remote contains work that you do\nhint: not have locally. This is usually caused by another repository pushing\nhint: to the same ref. You may want to first integrate the remote changes\nhint: (e.g., 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.")) == True

# Generated at 2022-06-14 10:19:50.581469
# Unit test for function match
def test_match():
    command = Command('git push', '! [rejected]        master -> master (non-fast-forward)\n'
     'error: failed to push some refs to \'some/remote\'\n'
     'hint: Updates were rejected because the tip of your current branch is behind\n'
     'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
     'hint: \'git pull ...\') before pushing again.\n'
     'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert match(command)


# Generated at 2022-06-14 10:20:01.776035
# Unit test for function match
def test_match():
    assert match(Command('git push origin master:master',
                         'remote: Permission to dimier/thefuck.git denied to alexdimen.\nfatal: unable to access \'https://github.com/dimier/thefuck.git/\': The requested URL returned error: 403'))
    assert not match(Command('git push origin master:master', ''))

# Generated at 2022-06-14 10:20:03.125949
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').script == 'git pull; git push'

# Generated at 2022-06-14 10:20:11.335518
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '\
    ! [rejected]        master -> master (non-fast-forward)\
    error: failed to push some refs to \'git@gitserver:user/myrepo.git\'\
    hint: Updates were rejected because the tip of your current branch is behind\
    hint: its remote counterpart. Integrate the remote changes (e.g.\
    hint: \'git pull ...\') before pushing again.\
    hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))



# Generated at 2022-06-14 10:20:13.409891
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push') == 'git pull && git push'

# Generated at 2022-06-14 10:20:24.830498
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                 'To https://github.com/USERNAME/OTHERREPOSITORY.git\n ! [rejected]        master -> master (non-fast-forward)\n'
                 'error: failed to push some refs to \'git@github.com:USERNAME/OTHERREPOSITORY.git\'\n'
                 'hint: Updates were rejected because the tip of your current branch is behind\n'
                 'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                 'hint: \'git pull ...\') before pushing again.\n'
                 'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n',
                 'git push origin master',
                 'git push origin master'))

# Generated at 2022-06-14 10:20:38.239134
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'https://github.com/arielfr/thefuck.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.'))

# Generated at 2022-06-14 10:20:41.027545
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git pus', ''))) == 'git pull && git pus'

# Generated at 2022-06-14 10:20:51.601643
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', '', '', ''))
    assert match(Command('git push origin master', '', '', '', '', 'To https://github.com/mallesh06/cron.git! [rejected]        master -> master (fetch first)error: failed to push some refs to \'https://github.com/mallesh06/cron.git\'hint: Updates were rejected because the tip of your current branch is behindhint: its remote counterpart. Integrate the remote changes (e.g.hint: \'git pull ...\' ) before pushing again.hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:21:06.321959
# Unit test for function match
def test_match():
    assert match(Command(script='git push',
                  output='! [rejected]        master -> master (fetch first)\n'
                  'error: failed to push some refs to \'git@bitbucket.org:thraxil/forktail.git\'\n'
                  'hint: Updates were rejected because the remote contains work that you do\n'
                  'hint: not have locally. This is usually caused by another repository pushing\n'
                  'hint: to the same ref. You may want to first integrate the remote changes\n'
                  'hint: (e.g., \'git pull ...\') before pushing again.'))

# Generated at 2022-06-14 10:21:14.009891
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master:master',
                      ' ! [rejected]        master -> master (non-fast-forward)\n'
                      'error: failed to push some refs to \'git@github.com:user/repo.git\'\n'
                      'hint: Updates were rejected because the tip of your current branch is behind\n'
                      'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                      'hint: \'git pull ...\') before pushing again.\n'
                      'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == 'git pull origin master:master && git push origin master:master'

# Generated at 2022-06-14 10:21:24.575060
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'Everything up-to-date\n'))
    assert not match(Command('git push', ''))

# Generated at 2022-06-14 10:21:35.018596
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected]\n'
                         'Updates were rejected because the tip of your'
                         ' current branch is behind',
                         '', 0, '', ''))
    assert match(Command('git push', '! [rejected]\n'
                         'Updates were rejected because the remote '
                         'contains work that you do', '', 0, '', ''))
    assert not match(Command('git push', 'Everything up-to-date', '', 0, '',
                             ''))
    assert not match(Command('git push', '! [rejected]\n'
                         'Updates were rejected because the remote '
                         'contains work that you do', '', 0, '', ''))


# Generated at 2022-06-14 10:21:43.024218
# Unit test for function match
def test_match():
    assert match(Command('git push',
        '''Total 0 (delta 0), reused 0 (delta 0)
        ! [rejected] master -> master (non-fast-forward)
        error: failed to push some refs to
        '''))

# Generated at 2022-06-14 10:21:44.461158
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master') == 'git pull origin master'

# Generated at 2022-06-14 10:21:46.694085
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master').script == 'git pull && git push origin master'

# Generated at 2022-06-14 10:21:56.577306
# Unit test for function match
def test_match():
    assert match(Command('git push origin dev',
        '/home/user/foo/bar',
        'To git@github.com:nvbn/thefuck.git\r\n ! [rejected] dev -> dev (non-fast-forward)\r\n error: failed to push some refs to \'git@github.com:nvbn/thefuck.git\'\r\n hint: Updates were rejected because the tip of your current branch is behind\r\n hint: its remote counterpart. Integrate the remote changes (e.g.\r\n hint: \'git pull ...\') before pushing again.\r\n hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\r\n'))

# Generated at 2022-06-14 10:21:59.679257
# Unit test for function match
def test_match():
    assert match('git push origin master')
    assert match('git push')
    assert not match('git push origin master --force')
    assert not match('echo')


# Generated at 2022-06-14 10:22:02.281663
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('push origin :blah', '')
    assert get_new_command(command) == 'pull origin :blah'

# Generated at 2022-06-14 10:22:08.683689
# Unit test for function match
def test_match():
    assert match(Command('git push', 'error'))
    assert match(Command('git push', 'error', output='! [rejected] '
                                                     'error'))
    assert not match(Command('git push origin master', 'error',
                    output='! [rejected] error'))


# Generated at 2022-06-14 10:22:21.403015
# Unit test for function match
def test_match():
	# Test for Upstream branch
	assert match(Command('git push', 
						'To https://github.com/TuxDude/Hello-World.git\n ! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/TuxDude/Hello-World.git\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'
						))==True

	# Test for same branch

# Generated at 2022-06-14 10:22:28.436423
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', 1))
    assert not match(Command('git push origin master', '', '', 0))
    assert not match(Command('sudo git push origin master', '', '', 0))
    assert not match(Command('ragit push origin master', '', '', 0))
    assert not match(Command('git push origin master', '', '', 0))



# Generated at 2022-06-14 10:22:40.551472
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '! [rejected] master->master (non-fast-forward)\n\
    error: failed to push some refs to \'ssh://...\'\n\
    hint: Updates were rejected because the tip of your current branch is behind\n\
    hint: its remote counterpart. Merge the remote changes (e.g. \'git pull\')\n\
    hint: before pushing again.\n\
    hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')) == 'git pull && git push'

# Generated at 2022-06-14 10:22:45.609891
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'https://github.com/user/repo.git\'',
                         ''))



# Generated at 2022-06-14 10:22:55.114199
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '',
                         'To https://github.com/nvbn/thefuck'
                         ' ! [rejected]        master -> master'
                         ' (fetch first) error: failed to push some refs to'
                         ' \'https://github.com/nvbn/thefuck\''
                         ' hint: Updates were rejected because the tip of your'
                         ' current branch is behind hint: its remote counterpart.'
                         ' Integrate the remote changes (e.g.'
                         ' hint: \'git pull ...\') before pushing again.'
                         ' hint: See the \'Note about fast-forwards\''
                         ' in \'git push --help\' for details.'))



# Generated at 2022-06-14 10:23:02.269447
# Unit test for function get_new_command
def test_get_new_command():
    assert ('&& git pull https://github.com/nvbn/thefuck.git master'
            == get_new_command('git push https://github.com/nvbn/thefuck.git master'))
    assert ('git pull https://github.com/nvbn/thefuck.git master'
            == get_new_command('git pull https://github.com/nvbn/thefuck.git master'))


# Generated at 2022-06-14 10:23:05.125464
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push --all') == shell.and_('git pull', 'git push --all')
    assert get_new_command('git push origin master') == shell.and_('git pull', 'git push origin master')

# Generated at 2022-06-14 10:23:15.666799
# Unit test for function match
def test_match():
    cur_dir = os.getcwd()
    os.chdir('tests/fixtures/git/push')
    assert(match(Command('git push', '''
git push
To https://github.com/nvbn/thefuck.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/nvbn/thefuck.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
''')) is True)
    os

# Generated at 2022-06-14 10:23:28.234145
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'Updates were rejected because the tip of your '
                         'current branch is behind its remote counterpart. '
                         'Integrate the remote changes (e.g.hint: '
                         '\'git pull ...\') before pushing again.'))
    assert match(Command('git push origin master',
                         'Updates were rejected because the remote contains '
                         'work that you do not have locally. This is usually '
                         'caused by another repository pushing to the same '
                         'ref. You may want to first integrate the '
                         'remote changes (e.g., hint: \'git pull ...\') '
                         'before pushing again.'))
    assert not match(Command('git push origin master', ''))


# Generated at 2022-06-14 10:23:41.810585
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected]        master -> master (non-fast-forward)\n\
error: failed to push some refs to \'https://github.com/thomassileo/dotfiles\n\
Updates were rejected because the tip of your current branch is behind\n\
its remote counterpart. Integrate the remote changes (e.g.\n\
\'git pull ...\') before pushing again.\n\
See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))
    assert not match(Command('git push', '! [rejected]        master -> master (non-fast-forward)\n'))
    assert not match(Command('git push', 'Everything up-to-date\n'))

# Generated at 2022-06-14 10:23:55.500990
# Unit test for function match
def test_match():
    assert match(Command("git push", "! [rejected]        master -> master (fetch first)\n"
                                     "error: failed to push some refs to 'git@.......git'\n"
                                     "hint: Updates were rejected because the remote contains work that you do\n"
                                     "hint: not have locally. This is usually caused by another repository pushing\n"
                                     "hint: to the same ref. You may want to first integrate the remote changes\n"
                                     "hint: (e.g., 'git pull ...') before pushing again.\n"
                                     "hint: See the 'Note about fast-forwards' in 'git push --help' for details."))