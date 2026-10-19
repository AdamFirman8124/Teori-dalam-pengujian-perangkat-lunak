

# Generated at 2022-06-14 10:14:01.366493
# Unit test for function match
def test_match():
    assert match(Command(script='git push',
                         output="""
To git@github.com:nvbn/thefuck.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:nvbn/thefuck.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
hint: before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.""",
                         stderr='', stdout=''))

# Generated at 2022-06-14 10:14:11.992403
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', ' ! [rejected]        master -> master (non-fast-forward)\n'
                                 'error: failed to push some refs to \'git@github.com:xxxxxx/xxxxx.git\'\n'
                                 'hint: Updates were rejected because the tip of your current branch is behind\n'
                                 'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                                 'hint: \'git pull ...\') before pushing again.\n'
                                 'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:14:23.091564
# Unit test for function match
def test_match():
    assert (match(Command(script='git push',
                          output='! [rejected]\n'
                                 'failed to push some refs to \'git@github.com:mahfuz195/Cowrie.git\'\n'
                                 'hint: Updates were rejected because the tip of your current branch is behind\n'
                                 'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                                 'hint: \'git pull ...\') before pushing again.'))
                                 == True)

# Generated at 2022-06-14 10:14:32.480078
# Unit test for function match

# Generated at 2022-06-14 10:14:40.097702
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'remote: error: GH001: Large files detected. '
                         'You may want to try Git Large File Storage '
                         '- https://git-lfs.github.com. remote: error:'
                         ' File DataObjects-2.2.4-nuget.zip is 140.38 MB;'
                         ' this exceeds GitHub\'s file size limit of 100.00 MB'))
    assert not match(Command('git push', ''))


# Generated at 2022-06-14 10:14:46.422775
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git push --force',
                                   stdout='Updates were rejected because the tip of your current branch is behind its remote\n')) == 'git pull && git push --force'
    assert get_new_command(Command(script='git push --force',
                                   stdout='Updates were rejected because the remote contains work that you do\n')) == 'git pull && git push --force'

# Generated at 2022-06-14 10:14:51.621645
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin', 'error msg')) == 'git pull origin && git push origin'

# Generated at 2022-06-14 10:15:04.882813
# Unit test for function match
def test_match():
    command= Command('git push',
                     '! [rejected]        master -> master (non-fast-forward)\n'
                     'error: failed to push some refs to \'https://github.com/sparrow/sparrow.github.io.git\'\n'
                     'hint: Updates were rejected because the tip of your current branch is behind\n'
                     'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                     'hint: \'git pull ...\') before pushing again.\n'
                     'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    new_command= get_new_command(command)
    assert new_command=='git pull && git push'

# Generated at 2022-06-14 10:15:10.496211
# Unit test for function match

# Generated at 2022-06-14 10:15:14.319231
# Unit test for function match
def test_match():
    assert not match('echo 123')
    assert match('git push')
    assert not match('git push -v')
    assert match('git push origin master')

# Generated at 2022-06-14 10:15:21.967574
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'remote: Permission to eecs485-staff/eecs485.git denied to jharvard.\nfatal: unable to access \'https://github.com/eecs485-staff/eecs485.git/\': The requested URL returned error: 403'))


# Generated at 2022-06-14 10:15:35.377115
# Unit test for function match
def test_match():
    def git_push(script, output):
        return Mock(
            script=script,
            output=output,
            side_effect=lambda x: type(
                'Response', (object,), {'stderr': output})(),
            environ={'GIT_TRACE': '1'})


# Generated at 2022-06-14 10:15:42.803052
# Unit test for function match
def test_match():
    assert(match(Command('git push origin master','''! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'ssh://git@bitbucket.org/joe/sandbox.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
''')))

# Generated at 2022-06-14 10:15:52.434786
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'Everything up-to-date\n'))
    assert not match(Command('git push origin master', ''))

# Generated at 2022-06-14 10:16:05.075891
# Unit test for function match

# Generated at 2022-06-14 10:16:10.203535
# Unit test for function match
def test_match():
    assert match(create_command('git push origin master'))
    assert not match(create_command('git push origin master', 'Error'))
    assert not match(create_command('git push origin master', 'Error', 'Error'))
    assert match(create_command('git push origin master', 'Error', 'Error', 'Error'))


# Generated at 2022-06-14 10:16:16.680307
# Unit test for function get_new_command

# Generated at 2022-06-14 10:16:20.938189
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master').script == 'git pull && git push origin master'
    assert get_new_command('git push --set-upstream origin master').script == 'git pull && git push --set-upstream origin master'
    assert ge

# Generated at 2022-06-14 10:16:31.823157
# Unit test for function match
def test_match():
    assert match(Command(script='git push origin master',
                         stderr='''fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master
'''))
    assert match(Command(script='git push origin head',
                         stderr='''error: The requested upstream branch 'origin/head' does not exist
error: failed to push some refs to 'git@github.com:nvie/gitflow.gi
'''))

# Generated at 2022-06-14 10:16:38.436441
# Unit test for function match
def test_match():
    assert match(Command('git push -v', '! [rejected]            master -> master (fetch first)\n', ''))
    assert match(Command('git push origin master', '', ''))
    assert not match(Command('git push', '', ''))
    assert not match(Command('git clone git://github.com/nvbn/thefuck.git', '', ''))
    assert not match(Command('git clone git://github.com/nvbn/thefuck.git', '', ''))
    assert not match(Command('git stash', '', ''))

# Generated at 2022-06-14 10:16:52.544673
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '''Everything up-to-date
! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:ugurcany/thefuck.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
hint: before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.''',
                         ''))

# Generated at 2022-06-14 10:17:04.224744
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (fetch first)',
                         'error: failed to push some refs to \'...\'',
                         'hint: Updates were rejected because the tip of your current branch is behind',
                         'hint: its remote counterpart. Integrate the remote changes (e.g.',
                         'hint: \'git pull ...\') before pushing again.',
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))


# Generated at 2022-06-14 10:17:07.646913
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', '', None, None))
    assert not match(Command('git push origin master', '', '', '', None, None))

# Generated at 2022-06-14 10:17:10.589266
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push origin master', '')) == shell.and_(
        'git pull origin master', 'git push origin master')

# Generated at 2022-06-14 10:17:16.359204
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', 'error'))
    assert match(Command('git push origin master', 'error'))
    assert not match(Command('git push origin master', ''))
    assert not match(Command('git push origin master', 'error'))
    assert not match(Command('git push origin master', 'error'))


# Generated at 2022-06-14 10:17:19.090188
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', 'error message')) == 'git pull; git push'


# Generated at 2022-06-14 10:17:30.186908
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (non-fast-forward)',
                         'error: failed to push some refs to \'git@github.com:aiyanbo/thefuck.git\'',
                         'hint: Updates were rejected because the tip of your current branch is behind',
                         'hint: its remote counterpart. Integrate the remote changes (e.g.',
                         'hint: \'git pull ...\') before pushing again.',
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:17:43.977109
# Unit test for function match
def test_match():
    assert match(Command('git push', '! [rejected]        master -> master (non-fast-forward)\nerror: failed to push some refs to \'https://github.com/isantop/test.git\'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: \'git pull ...\') before pushing again.\nhint: See the \'Note about fast-forwards\' in \'git push --help\' for details.', ''))

# Generated at 2022-06-14 10:17:54.767387
# Unit test for function match
def test_match():
	command = Command('git push','', 'Updates were rejected because the tip of your branch is behind its remote\nUpdates were rejected because the remote contains work that you do not have locally.\nThis is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes before pushing again.')
	assert match(command)
	command = Command('git push','', 'Updates were rejected because the remote contains work that you do not have locally.\nThis is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes before pushing again.')
	assert match(command) == False

# Generated at 2022-06-14 10:18:06.335031
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', '', '', ''))
    assert match(Command('git push origin master', '',
        'To ssh://test@test.com/opt/git/test.git ! [rejected] master -> master (fetch first) \n'
        'error: failed to push some refs to \'ssh://test@test.com/opt/git/test.git\' \n'
        'Updates were rejected because the tip of your current branch is behind \n'
        'its remote counterpart. Integrate the remote changes before pushing again.', '', '', ''))

# Generated at 2022-06-14 10:18:15.825562
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git push origin branch") == "git pull && git push origin branch"

# Generated at 2022-06-14 10:18:27.964881
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '\nTo ../remote\n'
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'../remote\'\n'
                         'hint: Updates were rejected because the tip of your '
                         'current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes '
                         '(e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' '
                         'for details.\n',
                         ''))

# Generated at 2022-06-14 10:18:36.976825
# Unit test for function match
def test_match():
    assert match(
        Command('git push origin master',
                " ! [rejected]        master -> master (fetch first) <Updates were rejected because the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes (e.g., 'git pull ...') before pushing again.>",
                "",
                0,
                False))
    assert match(
        Command('git push origin master',
                " ! [rejected]        master -> master (fetch first) <Updates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g. 'git pull ...') before pushing again.>",
                "",
                0,
                False))

# Generated at 2022-06-14 10:18:48.227912
# Unit test for function match
def test_match():
    assert match(Command('git push origin foo', '', '', '', '', '/dev/null'))
    assert match(Command('git push origin foo', '', '', '', '', '/dev/null'))
    assert match(Command('git push', '', '', '', '', '/dev/null'))
    assert not match(Command('git add', '', '', '', '', '/dev/null'))
    assert not match(Command('git commit', '', '', '', '', '/dev/null'))
    assert not match(Command('git checkout', '', '', '', '', '/dev/null'))
    assert not match(Command('git push -n', '', '', '', '', '/dev/null'))

# Generated at 2022-06-14 10:19:00.691761
# Unit test for function match
def test_match():
        command = Command('git push', 'ssh: Could not resolve hostname git: Name or service not known\
                          ! [rejected]        master -> master (non-fast-forward)\
                          error: failed to push some refs to')
        assert match(command)
        assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:19:04.051912
# Unit test for function match
def test_match():
	assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind', ''))
	assert not match(Command('git push', '', ''))

# Generated at 2022-06-14 10:19:14.656811
# Unit test for function get_new_command
def test_get_new_command():
    command1 = 'git push'
    command2 = 'git push origin master'
    command3 = 'git push --force origin master'

    assert shell.and_('git pull', command1) == get_new_command(Command(command1,
        '! [rejected]        master -> master (non-fast-forward)\n'
        'error: failed to push some refs to \'git@github.com:nvbn/thefuck.git\'\n'
        'hint: Updates were rejected because the tip of your current branch is behind\n'
        'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
        'hint: \'git pull ...\') before pushing again.\n'
        'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:19:16.595442
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').startswith('git pull')

# Generated at 2022-06-14 10:19:23.814562
# Unit test for function match
def test_match():
    # Arbitrary test
    assert match(Command('git push', 'failed to push some refs to ..'))
    assert match(Command('git push', 'Updates were rejected because the remote contains work that you do'))
    assert match(Command('git push', 'Updates were rejected because the tip of your current branch is behind'))

    # False cases
    assert not match(Command('git push', ''))
    assert not match(Command('git', ''))

# Generated at 2022-06-14 10:19:25.071667
# Unit test for function match
def test_match():
    assert match(Command('git push'))

# Generated at 2022-06-14 10:19:40.703489
# Unit test for function get_new_command
def test_get_new_command():
    assert "git pull" == get_new_command(Command("git push")).script

# Generated at 2022-06-14 10:19:49.904629
# Unit test for function match
def test_match():
    assert match(Command('git push', "! [rejected]        master -> master (non-fast-forward)"
                         "\nerror: failed to push some refs to 'git@github.com:rishabhverma17/WT.git'"
                         "\nhint: Updates were rejected because the tip of your current branch is behind"
                         "\nhint: its remote counterpart. Integrate the remote changes"
                         "\nhint: (e.g. hint: 'git pull ...') before pushing again."
                         "\nhint: See the 'Note about fast-forwards' in 'git push --help' for details."))


# Generated at 2022-06-14 10:19:54.965434
# Unit test for function match
def test_match():
    assert match(Command(script="git push", output="! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind its remote\ncounterpart. Enrich the question with more details."))



# Generated at 2022-06-14 10:20:08.553990
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'To git@github.com:nvbn/thefuck.git\n ! [rejected] '
                         'master -> master (fetch first)\nUpdates were '
                         'rejected because the remote contains work that you '
                         'do\nhint: not want. Merge the remote changes '
                         '(e.g. \'git pull\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' '
                         'in \'git push --help\' for details.'))



# Generated at 2022-06-14 10:20:15.706419
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         "To https://github.com/nvbn/thefuck\n ! [rejected] master -> master (non-fast-forward)\n error: failed to push some refs to 'https://github.com/nvbn/thefuck'\n hint: Updates were rejected because the tip of your current branch is behind\n hint: its remote counterpart. Integrate the remote changes (e.g.\n hint: 'git pull ...') before pushing again.\n hint: See the 'Note about fast-forwards' in 'git push --help' for details.")
                 )


# Generated at 2022-06-14 10:20:25.647249
# Unit test for function match

# Generated at 2022-06-14 10:20:31.555320
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', '! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind', '')
    assert get_new_command(command) == 'git pull && git push'

available = match

# Generated at 2022-06-14 10:20:42.353718
# Unit test for function match
def test_match():
    command = Command(script='git push',
                      output='! [rejected]        master -> master (non-fast-forward)\n'
                             'error: failed to push some refs to \'git@github.com:IMAQ2/git-tutorial.git\'\n'
                             'hint: Updates were rejected because the tip of your current branch is behind\n'
                             'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                             'hint: \'git pull ...\') before pushing again.\n'
                             'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.')
    expected_command = 'git pull'
    assert get_new_command(command) == expected_command


# Generated at 2022-06-14 10:20:56.437356
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin master\n'))

# Generated at 2022-06-14 10:20:59.303443
# Unit test for function get_new_command
def test_get_new_command():
	command = 'git push origin master'
	get_new_command(command) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:21:31.087744
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         "To https://github.com/nvie/gitflow.git ! [rejected] master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g.\n'git pull ...') before pushing again.\n"))


# Generated at 2022-06-14 10:21:44.463903
# Unit test for function match
def test_match():
    assert not match(Command(script='git push',
                             output='[up to date] everything is up to date'))
    assert not match(Command(script='git push -f',
                             output='[up to date] everything is up to date'))
    assert not match(Command(script='git push origin master',
                             output='[up to date] everything is up to date'))
    assert match(Command(script='git push',
                         output='[rejected] everything is up to date'))
    assert match(Command(script='git push',
                         output='[up to date] everything is [rejected]'))
    assert match(Command(script='git push',
                         output=' Updates were rejected because'
                                ' the tip of your current branch is behind'))

# Generated at 2022-06-14 10:21:51.434812
# Unit test for function match
def test_match():
    assert match(Command('git push', ' ! [rejected]        master -> master (fetch first)'))
    assert match(Command('git push origin master', 'To https://github.com/nvbn/thefuck.git ! [rejected]        master -> master (fetch first)\nUpdates were rejected because the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes before pushing again.'))
    assert not match(Command('git push', ''))
    assert not match(Command('git push', '\nEverything up-to-date'))
    assert not match(Command('ls', '\nEverything up-to-date'))


# Generated at 2022-06-14 10:22:06.895613
# Unit test for function match
def test_match():
    # Match function should return True and create a new command
    assert match(Command('git push origin master',
        ' ! [rejected]        master -> master (fetch first)\n'
        'error: failed to push some refs to \'git@github.com:AgileVentures/WebsiteOne.git\'\n'
        'hint: Updates were rejected because the remote contains work that you do\n'
        'hint: not have locally. This is usually caused by another repository pushing\n'
        'hint: to the same ref. You may want to first integrate the remote changes\n'
        'hint: (e.g., \'git pull ...\') before pushing again.\n'
        'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'
    )) == True
    # Match

# Generated at 2022-06-14 10:22:10.082396
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push').startswith('git pull')
    assert get_new_command('git push br').startswith('git pull br')

# Generated at 2022-06-14 10:22:13.376218
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '', '', 1, 3)) ==\
           shell.and_('git pull', 'git push')

# Generated at 2022-06-14 10:22:23.391989
# Unit test for function match
def test_match():
    assert match(Command(script="git push origin master",
                         output="error: failed to push some refs to 'http://github.com/path/repo.git'\nhint: Updates were rejected because the tip of your current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: 'git pull ...') before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details."))

# Generated at 2022-06-14 10:22:26.566665
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('') == 'git pull'
    assert get_new_command('git push origin -u git-repo') == 'git pull origin -u git-repo'

# Generated at 2022-06-14 10:22:29.746765
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command([u'git', u'push',u'origin',u'master']) == u'git pull && git push origin master'

# Generated at 2022-06-14 10:22:39.692973
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git push origin master'
    output = '''To https://github.com/technology/thefuck.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/technology/thefuck.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again.  See the
'Note about fast-forwards' section of 'git push --help' for details.
'''
    assert get_new_command(Command(script, output)) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:23:47.460420
# Unit test for function match
def test_match():
    assert match(Command('git br',
                                 '! [rejected]        master -> master (non-fast-forward)',
                                 'error: failed to push some refs to\''
                                 ' \'https://github.com/danielfrg/git-open.git\''
                                 ' hint: Updates were rejected because the tip of your'
                                 ' current branch is behind')
                                 )

# Generated at 2022-06-14 10:23:57.878428
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         'To git@github.com:nvbn/thefuck.git\n ! [rejected] master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:nvbn/thefuck.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                         'git push origin master'))