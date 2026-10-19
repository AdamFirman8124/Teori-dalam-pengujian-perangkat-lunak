

# Generated at 2022-06-14 10:14:00.748099
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git status') == 'git pull && git status'
    assert get_new_command('git push origin') == 'git pull && git push origin'
    assert get_new_command('git push origin master') == 'git pull && git push origin master'
    assert get_new_command('git push origin master test') == 'git pull && git push origin master test'

# Generated at 2022-06-14 10:14:12.713416
# Unit test for function match
def test_match():
    assert match(Command('git push', "remote: Resolving deltas: 100% (207/207)\nremote: error: \
failed to push some refs to 'git@github.com:laogia/test.git'\nhint: Updates were rejected because the tip of your \
current branch is behind\nhint: its remote counterpart. Integrate the remote changes (e.g.\nhint: 'git pull ...') \
before pushing again.\nhint: See the 'Note about fast-forwards' in 'git push --help' for details.",
                               ''))


# Generated at 2022-06-14 10:14:15.194757
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master') == 'git pull && git push origin master'

# Generated at 2022-06-14 10:14:28.108358
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', 'remote: Updating is not possible because you have unmerged files.'
                                              ' fix conflicts and then commit the result.'
                                               'fatal: Exiting because of an error.', 'ssh://example.com/bar.git')) == shell.and_('git pull', 'git push')
    assert get_new_command(Command('git push', 'To ssh://example.com/bar.git'
                                                ' ! [rejected]        master -> master (non-fast-forward)'
                                                'error: failed to push some refs to'
                                                '\'ssh://example.com/bar.git\'', 'ssh://example.com/bar.git')) == shell.and_('git pull', 'git push')

# Generated at 2022-06-14 10:14:38.033412
# Unit test for function get_new_command
def test_get_new_command():
    assert git.get_new_command(
        Command('git push origin foo:master',
                ' ! [rejected]       master -> master (non-fast-forward)\n\
                error: failed to push some refs to \'git@github.com:foo/bar.git\'\n\
                hint: Updates were rejected because the tip of your current branch is behind\n\
                hint: its remote counterpart. Integrate the remote changes (e.g.\n\
                hint: \'git pull ...\') before pushing again.\n\
                hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                'git push origin foo:master')) == 'git pull && git push origin foo:master'

# Generated at 2022-06-14 10:14:46.382829
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:ralphbean/mkdocs.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))



# Generated at 2022-06-14 10:15:00.579854
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         'Updates were rejected because the tip of your '
                         'current branch is behind'))
    assert match(Command('git push',
                         'Updates were rejected because the remote contains'
                         ' work that you do'))
    assert not match(Command('git push', ''))
    assert not match(Command('git push',
                             'Updates were rejected because the remote '
                             'contains work that you do'
                             'Updates were rejected because the tip of your '
                             'current branch is behind'))


# Generated at 2022-06-14 10:15:05.747503
# Unit test for function match

# Generated at 2022-06-14 10:15:18.848808
# Unit test for function match
def test_match():
    assert match(Command('git push origin dev', '', '', 1))
    assert match(Command('git push origin dev', '', 'Updates were rejected because the tip of your current branch is behind', 1))
    assert match(Command('git push origin dev', '', 'Updates were rejected because the remote contains work that you do', 1))
    assert match(Command('git push origin dev', '','', 1)) is False
    assert match(Command('git push origin dev', '', 'Updates were rejected because the tip of your current branch is behind', 1))
    assert match(Command('git push origin dev', '', 'Updates were rejected because the remote contains work that you do', 1))
    assert match(Command('git push origin dev', '', '', 1)) is False

# Generated at 2022-06-14 10:15:26.399835
# Unit test for function match

# Generated at 2022-06-14 10:15:31.131871
# Unit test for function get_new_command
def test_get_new_command():
  assert get_new_command('git push').command == 'git pull && git push'

# Generated at 2022-06-14 10:15:40.933470
# Unit test for function match
def test_match():
    # Test for match function for 'push' command
    first_command = Command(script = 'git push',
                            stdout = """
To git@github.com:prakashpandey/GitCommands.git
! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:prakashpandey/GitCommands.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.""",
                            stderr = '',
                            script_parts = ('git', 'push'),
                            )

# Generated at 2022-06-14 10:15:52.472895
# Unit test for function get_new_command
def test_get_new_command():
    script = "git push origin master"
    output = "! [rejected]        master -> master (non-fast-forward)\nTo prevent you from losing history, non-fast-forward updates were rejected\nMerge the remote changes (e.g. 'git pull') before pushing again.  See the\n'Note about fast-forwards' section of 'git push --help' for details.\n"
    command = Command(script, output)
    assert get_new_command(command) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:15:55.761676
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git push origin master'
    new_script = 'git pull origin master'
    assert get_new_command(Command(script, '')) == new_script

# Generated at 2022-06-14 10:15:59.605308
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git push origin master',
                                   output='Updates were rejected because the tip of your current branch is behind\n')) == 'git pull && git push origin master'

# Generated at 2022-06-14 10:16:01.234077
# Unit test for function match
def test_match():
    assert match(Commands("git push origin master"))



# Generated at 2022-06-14 10:16:09.864349
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '! [rejected] master -> master (fetch first)\n'
                         'error: failed to push some refs to \'git@github.com:agustim/dotfiles.git\'\n'
                         'hint: Updates were rejected because the remote contains work that you do\n'
                         'hint: not have locally. This is usually caused by another repository pushing\n'
                         'hint: to the same ref. You may want to first integrate the remote changes\n'
                         'hint: (e.g., \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))
    assert not match(Command('git push origin master', 'Everything up-to-date'))

# Generated at 2022-06-14 10:16:22.052890
# Unit test for function get_new_command
def test_get_new_command():
    assert (git.get_new_command(Command('git push', '','''To github.com:bitpwn/TheFuck
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:bitpwn/TheFuck'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.''', '')).script
           == "git pull && git push")

# Generated at 2022-06-14 10:16:26.590191
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git push origin master',
                           stderr='Updates were rejected because the tip of your current branch is behind some commits on the remote.', stdout='')) == shell.and_(replace_argument('git push origin master', 'push', 'pull'), 'git push origin master')

# Generated at 2022-06-14 10:16:38.601207
# Unit test for function match
def test_match():
    assert match(Command('git push origin master'))
    assert match(Command('git push origin master',
                         'To https://github.com/psincraian/GitHubAction.git ! [rejected] master -> master (fetch first)\n'
                         'Updates were rejected because the remote contains work that you do\n'
                         'not have locally. This is usually caused by another repository pushing\n'
                         'to the same ref. You may want to first integrate the remote changes\n'
                         '(e.g., \'git pull ...\') before pushing again.\n'
                         'See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))
    assert not match(Command('git pull origin master'))


# Generated at 2022-06-14 10:16:49.882286
# Unit test for function get_new_command
def test_get_new_command():
    c = Command('git push origin master', '! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\nits remote counterpart. Integrate the remote changes (e.g.\n\'git pull ...\') before pushing again.\nSee the \'Note about fast-forwards\' in \'git push --help\' for details.\n', '')
    new_c = get_new_command(c)
    assert new_c == shell.and_('git pull origin master', 'git push origin master')

# Generated at 2022-06-14 10:16:57.134046
# Unit test for function match
def test_match():
    assert match(Command("git push -u origin master",
                         "Updates were rejected because the remote "
                         "contains work that you do not have locally.  "
                         "This is usually caused by another repository pushing "
                         "to the same ref. You may want to first integrate the "
                         "remote changes before pushing again.  See the "
                         "'Note about fast-forwards' in 'git push --help' for details.",
                         "")) == True

# Generated at 2022-06-14 10:17:03.065619
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', '! [rejected] master -> master (fetch first)')) == 'git pull && git push'
    assert get_new_command(Command('git push', '! [rejected] master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\nUpdates were rejected because the remote contains work that you do\n')) == 'git pull && git push'
    assert get_new_command(Command('git push', '! [rejected]')) == 'git pull && git push'
    assert get_new_command(Command('git push', '! [rejected] master')) == 'git pull && git push'

# Generated at 2022-06-14 10:17:13.271166
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push', '! [rejected] master -> master (non-fast-forward)\n\
		error: failed to push some refs to \'https://github.com/mazgi/thefuck\'\n\
		hint: Updates were rejected because the tip of your current branch is behind\n\
		hint: its remote counterpart. Integrate the remote changes (e.g.\n\
		hint: \'git pull ...\') before pushing again.\n\
		hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n')
    assert get_new_command(command) == 'git pull && git push'


# Generated at 2022-06-14 10:17:17.029569
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_pull_before_push import get_new_command
    assert get_new_command(get_command('git push')) == 'git pull && git push'


# Generated at 2022-06-14 10:17:28.888501
# Unit test for function get_new_command
def test_get_new_command():
    script = [
        "git push origin +develop:master",
        "git push origin HEAD:master"
        ]
    output="""To http://gitlab-cts.ext.net.nokia.com/fi-gateog/fiservice/compiler.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'http://gitlab-cts.ext.net.nokia.com/fi-gateog/fiservice/compiler.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details."""
   

# Generated at 2022-06-14 10:17:40.586194
# Unit test for function match

# Generated at 2022-06-14 10:17:55.482609
# Unit test for function match
def test_match():

    # Tests if correct command is matched
    assert match(Command('git push',
                         'To https://github.com/user/repo\n'
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to '
                         "'https://github.com/user/repo'\n"
                         'hint: Updates were rejected because the tip of your '
                         'current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes '
                         '(e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in '
                         '\'git push --help\' for details.'))

    # Tests if no command is matched

# Generated at 2022-06-14 10:18:06.933365
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git push',
                   stdout="""error: failed to push some refs to 'git@github.com:dasix/sandbox.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again. \
See the 'Note about fast-forwards' section of 'git push --help' for details.""")
    assert get_new_command(command) == 'git pull && git push'

# Generated at 2022-06-14 10:18:13.766999
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         "! [rejected] master -> master (fetch first)\n"
                         "error: failed to push some refs to\n"
                         "'https://github.com/repo.git'\n"
                         "hint: Updates were rejected because "
                         "the tip of your current branch is behind\n"
                         "hint: its remote counterpart. Integrate the remote "
                         "changes (e.g.\nhint: 'git pull ...') before pushing "
                         "again.\nhint: See the 'Note about fast-forwards' "
                         "in 'git push --help' for details."))



# Generated at 2022-06-14 10:18:28.799018
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (non-fast-forward)',
                         'error: failed to push some refs to'))
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (fetch first)',
                         'error: failed to push some refs to'))
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (non-fast-forward)',
                         'Updates were rejected because the tip of your current branch is behind',
                         'error: failed to push some refs to'))

# Generated at 2022-06-14 10:18:37.302166
# Unit test for function match
def test_match():
    assert match(Command(script='git push origin master',
                         output=' ! [rejected]        master -> master '
                                '(non-fast-forward) error: failed to '
                                'push some refs to \'git@github.com:...\'\n'
                                'hint: Updates were rejected because the tip of '
                                'your current branch is behind\n'
                                'hint: its remote counterpart. Integrate the '
                                'remote changes (e.g.\nhint: \'git pull ...\') '
                                'before pushing again.\n'
                                'hint: See the \'Note about fast-forwards\' in '
                                '\'git push --help\' for details.\n'
                         ))

# Generated at 2022-06-14 10:18:45.275128
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         output='! [rejected] master -> master (non-fast-forward)'
                         '\nUpdates were rejected because the tip of your'
                         ' current branch is behind'))
    assert not match(Command('git commit',
                               output='! [rejected] master -> master (non-fast-forward)'
                               '\nUpdates were rejected because the tip of your'
                               ' current branch is behind'))


# Generated at 2022-06-14 10:18:52.192923
# Unit test for function match
def test_match():
    assert not match(Command('push', '', ''))
    assert match(Command('git push', '', 'Updates were rejected because the '
                                           'tip of your current branch is '
                                           'behind'))
    assert match(Command('git push', '', 'Updates were rejected because the '
                                           'remote contains work that you do'))
    assert not match(Command('git push', '', ''))

# Generated at 2022-06-14 10:19:00.311914
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push', 'failed to push some refs to remote')) == shell.and_('git pull', 'git push')
    assert get_new_command(Command('git push', 'Updates were rejected because the remote contains work that you do not have locally')) == shell.and_('git pull', 'git push')
    assert get_new_command(Command('git push', 'Updates were rejected because the tip of your current branch is behind')) == shell.and_('git pull', 'git push')

# Generated at 2022-06-14 10:19:03.547417
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git push origin master',
                      'error: failed to push some refs to ....')
    assert get_new_command(command) == u'&& git pull'

# Generated at 2022-06-14 10:19:14.425764
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected]        master -> master (fetch first)\n'
                         'error: failed to push some refs to \'git@github.com:rajaarul/thefuck.git\'\n'
                         'hint: Updates were rejected because the remote contains work that you do\n'
                         'hint: not have locally. This is usually caused by another repository pushing\n'
                         'hint:  to the same ref. You may want to first integrate the remote changes\n'
                         'hint: (e.g., \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                         '',
                         1))

# Generated at 2022-06-14 10:19:27.272102
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         '',
                         'fatal: The remote end hung up unexpectedly'))

# Generated at 2022-06-14 10:19:30.296696
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push')) == 'git pull'
    assert get_new_command(Command('git push --force')) == 'git pull --force'

# Generated at 2022-06-14 10:19:34.414600
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', '', '', 1, None))
    assert not match(Command('git push origin master', '', '', 0, None))
    assert not match(Command('git checkout master', '', '', 1, None))


# Generated at 2022-06-14 10:19:47.916994
# Unit test for function get_new_command
def test_get_new_command():
    test_command = "git push"
    new_cmd = get_new_command(Command(test_command, "! [rejected]\nUpdates were\nUpdates were rejected because the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes before pushing again.\nSee the 'Note about fast-forwards' in 'git push --help' for details."))
    assert new_cmd[0] == "git pull"

# Generated at 2022-06-14 10:19:57.988955
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git pull && git push' == get_new_command(
        CommandStub(
            script='git push',
            output='Updates were rejected because the remote contains work that you do not have locally.  '
            '    This is usually caused by another repository pushing to the same ref.  '
            '    You may want to first integrate the remote changes before pushing again.  '
            '    (see \"git pull --help\")'
        )
    )



# Generated at 2022-06-14 10:20:04.087105
# Unit test for function match
def test_match():
    assert match(Command('git push origin master'))
    assert match(Command('git push'))
    assert not match(Command('git pull'))


# Generated at 2022-06-14 10:20:06.769719
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         '! [rejected] master -> master (fetch first)'))


# Generated at 2022-06-14 10:20:16.050558
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         "! [rejected]        master -> master (non-fast-forward)\n"
                         "error: failed to push some refs to 'https://github.com/maxianglin/dotfiles.git'\n"
                         "hint: Updates were rejected because the tip of your "
                         "current branch is behind\n"
                         "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                         "hint: 'git pull ...') before pushing again.\n"
                         "hint: See the 'Note about fast-forwards' in 'git push --help' for details.",
                         ''))

# Generated at 2022-06-14 10:20:21.164222
# Unit test for function match
def test_match():
    command = Command('git push', output='! [rejected]        master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\nfailed to push some refs to \'git@github.com:SyndaxAi/git-tools.git\'')
    assert match(command)


# Generated at 2022-06-14 10:20:23.523443
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git push") == "git pull && git push"


# Generated at 2022-06-14 10:20:33.427926
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', "! [rejected]        master -> master (non-fast-forward)\n"
                                                  "error: failed to push some refs to 'git@github.com:laisheng/i2.git'\n"
                                                  "hint: Updates were rejected because the tip of your current branch is behind\n"
                                                  "hint: its remote counterpart. Integrate the remote changes (e.g.\n"
                                                  "hint: 'git pull ...') before pushing again.\n"
                                                  "hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n", None))


# Generated at 2022-06-14 10:20:36.794434
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git stash', '', '', 1)) == '')
    assert(get_new_command(Command('git push', 'error message', '', 1)) == 'git pull && git push')

# Generated at 2022-06-14 10:20:38.540513
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git push origin master') == 'git pull origin master'

# Generated at 2022-06-14 10:21:07.981049
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@example.com:user/repo.git\'\n'
                         'hint: Updates were rejected because the tip of your current branch is behind\n'
                         'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                         'hint: \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.'))

# Generated at 2022-06-14 10:21:15.912731
# Unit test for function match
def test_match():
    command = Command('git push origin branch', " ! [rejected]\n    master -> master (non-fast-forward)\nUpdates were rejected because the tip of your current branch is behind\nremote/branch")
    assert match(command)
    command = Command('git push origin branch', ' ! [rejected]\n    master -> master (non-fast-forward)\nUpdates were rejected because the remote contains work that you do\nnot have locally. This is usually caused by another repository pushing\nto the same ref. You may want to first integrate the remote changes\nremote/branch')
    assert match(command)
    command = Command('git push origin branch')
    assert not match(command)


# Generated at 2022-06-14 10:21:17.459227
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git push") == "git pull && git push"

# Generated at 2022-06-14 10:21:27.969562
# Unit test for function match
def test_match():
    assert match(Command('git push  2>&1', '', '! [rejected]        master -> master (fetch first)\n'
                                                 'error: failed to push some refs to \'git@git.git.git\'\n'
                                                 'hint: Updates were rejected because the tip of your current branch is behind\n'
                                                 'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
                                                 'hint: \'git pull ...\') before pushing again.\n'
                                                 'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\n'))

# Generated at 2022-06-14 10:21:41.608406
# Unit test for function match
def test_match():
    assert match(Command('git push origin master',
        'To git@github.com:nvbn/thefuck.git\n'
        ' ! [rejected]        master -> master (non-fast-forward)\n'
        'error: failed to push some refs to \'git@github.com:nvbn/thefuck.git\''
        '\n'
        'hint: Updates were rejected because the tip of your current branch '
        'is behind\n'
        'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
        'hint: \'git pull ...\') before pushing again.\n'
        'hint: See the \'Note about fast-forwards\' in \'git push --help\' '
        'for details.', ''))

# Generated at 2022-06-14 10:21:52.221637
# Unit test for function match
def test_match():
    assert match(command=Command('git push origin master',
                                 output='error: failed to push some refs to '
                                        '\'https://github.com/u/r.git\'\n'
                                        'hint: Updates were rejected because '
                                        'the tip of your current branch is '
                                        'behind\nhint: its remote counterpart. '
                                        'Integrate the remote changes (e.g.\n'
                                        'hint: \'git pull ...\') before pushing '
                                        'again.\nhint: See the \'Note about '
                                        'fast-forwards\' in \'git push --help\' '
                                        'for details.'))

# Generated at 2022-06-14 10:22:07.439519
# Unit test for function match
def test_match():
    assert not match(Command(script='git push',
                             output='fatal: unable to access \'https://github.com/USER/REPO.git/\':'))

    assert not match(Command(script='git push',
                             output='fatal: The current branch master has no upstream branch.'))

    assert not match(Command(script='git push',
                             output='fatal: Not a git repository (or any of the parent directories): .git'))

    assert not match(Command(script='git push',
                             output='Nothing to commit, working tree clean'))

    assert match(Command(script='git push',
                             output='Updates were rejected because the tip of your current branch is behind'))


# Generated at 2022-06-14 10:22:10.080714
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('git push', '')) == 'git pull && git push'

# Generated at 2022-06-14 10:22:16.145593
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git push',
                                   'Updates were rejected because the tip of your \
                                   current branch is behind')) == 'git pull'
    assert get_new_command(Command('git push',
                                   'Updates were rejected because the remote contains\
                                   work that you do')) == 'git pull'

# Generated at 2022-06-14 10:22:30.982976
# Unit test for function match
def test_match():
    assert match(Command('cd . && git push',
                         ' ! [rejected]        master -> master (non-fast-forward)\n'
                         'error: failed to push some refs to \'git@github.com:GoesToEleven/learngo.git\'',
                         'git push --force origin master'))

    assert not match(Command('cd . && git push',
                             ' ! [rejected]        master -> master (non-fast-forward)\n'
                             'error: failed to push some refs to \'git@github.com:GoesToEleven/learngo.git\'',
                             'git push origin master'))


# Generated at 2022-06-14 10:23:06.342295
# Unit test for function match
def test_match():
    assert match(Command('git push',
                         ' ! [rejected]        master -> master (fetch first)\n'
                         'error: failed to push some refs to \'git@github.com:test/test.git\'\n'
                         'hint: Updates were rejected because the remote contains work that you do\n'
                         'hint: not have locally. This is usually caused by another repository pushing\n'
                         'hint: to the same ref. You may want to first integrate the remote changes\n'
                         'hint: (e.g., \'git pull ...\') before pushing again.\n'
                         'hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.',
                         '')
            )

# Generated at 2022-06-14 10:23:14.269366
# Unit test for function match
def test_match():
    result=match(Command(script="git push origin master",
        output="fatal: The current branch master has no upstream branch.\ngit push --set-upstream origin master\nTo https://github.com/scottcame/configfiles.git\n ! [rejected]        master -> master (fetch first)\n error: failed to push some refs to 'git@github.com:scottcame/configfiles.git'\n hint: Updates were rejected because the remote contains work that you do\n hint: not have locally. This is usually caused by another reposi\n hint: or by a pushed branch failing to merge locally.\n hint: If you are sure you want to push it again, run 'git push --force'\n"))
    assert result == True


# Generated at 2022-06-14 10:23:18.414323
# Unit test for function match
def test_match():
    assert match(Command(script='git push'))
    assert not match(Command(script='git pull'))
    assert not match(Command(script='git push', stderr=''))


# Generated at 2022-06-14 10:23:30.765078
# Unit test for function match

# Generated at 2022-06-14 10:23:41.187876
# Unit test for function match
def test_match():
    assert match(Command('git push origin master', ''))
    assert match(Command('git push origin master',
                         '''To git@github.com:xiyouMc/thefuck.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:xiyouMc/thefuck.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
'''))

# Generated at 2022-06-14 10:23:54.486311
# Unit test for function get_new_command
def test_get_new_command():
    "python3 test_match.py"
    assert get_new_command('''
To git@github.com:Sylhare/TheFuck.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:Sylhare/TheFuck.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
''') == "git pull && git push"