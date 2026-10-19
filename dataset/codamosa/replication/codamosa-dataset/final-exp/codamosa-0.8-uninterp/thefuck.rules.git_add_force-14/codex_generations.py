

# Generated at 2022-06-14 09:52:01.951828
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt',
                         'fatal: pathspec \'file.txt\' did not match any files'))
    assert not match(Command('git commit -m fix',
                             'On branch master\n'
                             'Your branch is up to date with \'origin/master\'.'
                             '\n nothing to commit, working tree clean'))


# Generated at 2022-06-14 09:52:11.870682
# Unit test for function match
def test_match():
    assert not match(Command('git add file', '', 'fatal: Pathspec'))
    assert match(Command('git add file', '',
                         'fatal: Pathspec \'file\' is in submodule \'sm\'\n\
Use \'git add --force ...\' if you really want to add \'sm/file\''))
    assert match(Command('git add file', '',
                         'fatal: Pathspec \'file\' is in submodule \'sm\'\n\
Use \'--force\' if you really want to add \'sm/file\''))
    assert match(Command('git add file', '',
                         'fatal: Pathspec \'file\' is in submodule \'sm\'\n\
Use -f if you really want to add them.'))

# Generated at 2022-06-14 09:52:14.098073
# Unit test for function match
def test_match():
    command = Command("git add '*.py'")
    assert match(command) is True



# Generated at 2022-06-14 09:52:19.350565
# Unit test for function match
def test_match():
    assert match(Command('git add .',
        '/home/user/repo/file.txt: No such file or directory',
        '/home/user/repo'))
    assert not match(Command('git add .',
        'Nothing specified, nothing added.'
        'Maybe you wanted to say \'git add .\'?'))



# Generated at 2022-06-14 09:52:27.748449
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                         'fatal: pathspec \'filename.txt\' did not match any files',
                         '',
                         '',
                         ''))
    assert match(Command('git add file.txt',
                         'fatal: pathspec \'file.txt\' did not match any files',
                         '',
                         '',
                         ''))
    assert match(Command('git add file.txt',
                         'fatal: pathspec \'file.txt\' did not match any files',
                         'Use -f if you really want to add them.',
                         '',
                         ''))
    assert not match(Command('sudo git add .'))



# Generated at 2022-06-14 09:52:29.976736
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add foo', '', '')) == 'git add --force foo'

# Generated at 2022-06-14 09:52:38.640226
# Unit test for function get_new_command
def test_get_new_command():
    import sys
    import os
    current_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, current_path + '/../')

    from git import git_support
    from git import get_new_command

    command = type('obj', (object,), {'script': 'git add my_file.py', 'output': 'Use -f if you really want to add them.'})

    new_command = get_new_command(command)

    assert new_command == 'git add --force my_file.py'

# Generated at 2022-06-14 09:52:41.412412
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .', 'Use -f if you really want to add them.\n')
    assert get_new_command(command) == 'git add --force .'

# Generated at 2022-06-14 09:52:44.858095
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add .') == 'git add --force .'
    assert get_new_command('git add -p .') == 'git add --force -p .'


# Generated at 2022-06-14 09:52:48.243622
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add',
        'fatal: Pathspec \'16-1\'/\'16-3/\'16-3/ChecklistVault/*.txt\' is in submodule \'16-3/ChecklistVault\'')) == 'git add --force'

# Generated at 2022-06-14 09:52:52.541731
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', 'The following untracked working tree files would be overwritten by merge:\n Use -f if you really want to add them.')).script == 'git add --force .'


# Generated at 2022-06-14 09:52:54.349701
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add ', '')) == 'git add --force '

# Generated at 2022-06-14 09:52:57.446718
# Unit test for function match
def test_match():
	assert not match(Command('git add .', '',''))
	assert match(Command('git add .', 'Use -f if you really want to add them.',''))


# Generated at 2022-06-14 09:53:04.884781
# Unit test for function match
def test_match():
    assert match(Command('git add -A', "fatal: LF would be replaced by CRLF in Makefile\n"
                                       "The file will have its original line endings in your working directory.",
                                       "Use -f if you really want to add them."))
    assert not match(Command('git add -A', "fatal: LF would be replaced by CRLF in Makefile\n"
                                           "The file will have its original line endings in your working directory.",
                                            ""))

# Generated at 2022-06-14 09:53:14.847897
# Unit test for function match
def test_match():
    assert match(Command('git add',
           output = ('The following paths are ignored by one of your .gitignore files:\n'
                     '.gitignore\n'
                     '.gitignore\n'
                     'Use -f if you really want to add them.\n'
                     'fatal: no files added\n')))
    assert not match(Command('git add .',
            output = ('fatal: The following paths are ignored by one of your .gitignore files:\n'
                      'Use -f if you really want to add them.\n'
                      'fatal: no files added\n')))

# Generated at 2022-06-14 09:53:17.629833
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add *', 'At least one parameter is invalid: *')) == 'git add --force *'

# Generated at 2022-06-14 09:53:24.289116
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                         'fatal: pathspec \'P\' did not match any files',
                         '', 1))
    assert match(Command('git add .', 'fatal: pathspec \'P\' did not match any files', '', 1))
    assert not match(Command('git branch', 'fatal: pathspec \'P\' did not match any files', '', 1))
    assert not match(Command('git branch', '', '', 1))

# Generated at 2022-06-14 09:53:33.062292
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('git add *.py',
                'fatal: LF would be replaced by CRLF in testfile.py\n'
                'Use -f if you really want to add them.\n')
    ) == 'git add --force *.py'

# Generated at 2022-06-14 09:53:45.031206
# Unit test for function match
def test_match():
    assert match(Command(script = 'git add .',
                         output = 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.'))

    assert match(Command(script = 'git add -A',
                         output = 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.'))

    assert not match(Command(script = 'git add .',
                             output = 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.\nfoo'))

    assert not match(Command(script = 'git add .',
                             output = 'fatal: not a git repository'))


# Generated at 2022-06-14 09:53:50.617460
# Unit test for function get_new_command

# Generated at 2022-06-14 09:53:57.284424
# Unit test for function match
def test_match():
	output = """The following paths are ignored by one of your .gitignore files:
dist/
Use -f if you really want to add them.
fatal: no files added"""
	assert match(Command('git add ', output))


# Generated at 2022-06-14 09:54:02.798453
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'Use -f if you really want to add them.')) == 'git add --force'

# Generated at 2022-06-14 09:54:12.700958
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_add_force import (
        get_new_command as test_func,
    )
    from thefuck.types import Command

    def call_test_func(*args):
        return test_func(*args)

    command = Command('git add file',
                      'The following paths are ignored by one of your .gitignore files:\nfile\nUse -f if you really want to add them.')
    assert call_test_func(command) == 'git add --force file'

    command = Command('git add -p',
                      'The following paths are ignored by one of your .gitignore files:\nfile\nUse -f if you really want to add them.')
    assert call_test_func(command) == 'git add -p --force'

# Generated at 2022-06-14 09:54:19.535798
# Unit test for function match
def test_match():
    assert not match(Command('git add', ''))
    assert not match(Command('git add', 'fatal: Not a git repository'))
    assert match(Command('git add', 'The following paths are ignored'))
    assert match(Command('git add', 'The following paths are ignored (and many other lines)'))
    assert not match(Command('git add', 'Use -f if you really want to add them.'))



# Generated at 2022-06-14 09:54:26.240762
# Unit test for function match
def test_match():
    assert match(Command('git add foo.txt', '', '', 1, None))
    assert match(Command('git add foo.txt', '', '', 1, 2))
    assert not match(Command('add foo.txt', '', '', 1, None))
    assert not match(Command('git add', '', '', 1, None))
    assert not match(Command('foo add foo.txt', '', '', 1, None))


# Generated at 2022-06-14 09:54:31.383847
# Unit test for function match
def test_match():
    assert match(Command('git add file',
                         stderr='error: The following paths are ignored by '
                                'one of your .gitignore files:',
                         output='Use -f if you really want to add them.'))
    assert not match(Command('git add file'))

# Generated at 2022-06-14 09:54:37.483252
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add file.txt', '', 'The following paths are ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.\n')) == 'git add --force file.txt'

# Generated at 2022-06-14 09:54:41.044042
# Unit test for function match
def test_match():
    assert match(Command('git stash',
                         'fatal: pathspec \'\' did not match any files',
                         '', 1))
    assert not match(Command('git stash',
                             '',
                             '', 1))

# Generated at 2022-06-14 09:54:45.631857
# Unit test for function match
def test_match():
    assert match('git add .')
    assert not match('git add -f .')
    assert not match('git commit -m "Change file"')


# Generated at 2022-06-14 09:54:53.868379
# Unit test for function match
def test_match():
    assert match(Command('git add README.md', '', "The following paths are ignored by one of your .gitignore files:\r\nREADME.md\r\nUse -f if you really want to add them.\r\n"))
    assert not match(Command('git add README.md', '', 'git: \'add\' is not a git command. See \'git --help\'.\r\n\r\nDid you mean this?\r\n\tstage'))


# Generated at 2022-06-14 09:55:07.222574
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', "fatal: LF would be replaced by CRLF in Test.py\nThe file will have its original line endings in your working directory.\nUse -f if you really want to add them.")) == 'git add --force .'
    assert get_new_command(Command('git add .', "The file will have its original line endings in your working directory.\nUse -f if you really want to add them.")) == "git add ."

# Generated at 2022-06-14 09:55:12.348712
# Unit test for function match
def test_match():
	output = """
The following paths are ignored by one of your .gitignore files:
a.txt
Use -f if you really want to add them.
fatal: no files added
	"""
	check = match(Command(script='git add .', output=output))
	assert(check == True)


# Generated at 2022-06-14 09:55:14.973036
# Unit test for function get_new_command
def test_get_new_command():
   assert get_new_command(prueba)[3] == 'git add --force file'

# Generated at 2022-06-14 09:55:18.003848
# Unit test for function match
def test_match():
    command = Command('git add file', 'The following paths are ignored by one of your .gitignore files:')
    assert match(command)


# Generated at 2022-06-14 09:55:20.240614
# Unit test for function match
def test_match():
    assert match(Command('git add', output='Use -f if you really want to add them.'))


# Generated at 2022-06-14 09:55:23.604527
# Unit test for function match
def test_match():
    assert match(Command('git add file1', 'file1: needs merge\nUse -f if you really want to add them.'))
    assert not match(Command('git add file1', 'Aborting'))


# Generated at 2022-06-14 09:55:29.054316
# Unit test for function match
def test_match():
    assert match(Command('git add',
        stderr='error: The following untracked working tree files would be overwritten by merge:\n' +
        '\tlib/add.py\n\tlib/ignore.py\nPlease move or remove them before you can merge.\n' +
        'Aborting\n'))
    assert not match(Command('git add',
        stderr='There is no tracking information for the current branch.'))

# Generated at 2022-06-14 09:55:37.713248
# Unit test for function match
def test_match():
   result = match(Command('git add file', '', 'The following paths are ignored by one of your .gitignore files:\nfile\nUse -f if you really want to add them.'))
   assert result == True
   result = match(Command('git add', '', 'The following paths are ignored by one of your .gitignore files:\nfile\nUse -f if you really want to add them.'))
   assert result == False
   result = match(Command('git status', '', ''))
   assert result == False


# Generated at 2022-06-14 09:55:40.545232
# Unit test for function get_new_command
def test_get_new_command():
    assert _get_new_command("git add --file/with/spaces") == "git add --force --file/with/spaces"

# Generated at 2022-06-14 09:55:43.560767
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .', 'invalid path spec')
    assert get_new_command(command) == 'git add --force .'

# Generated at 2022-06-14 09:55:52.619686
# Unit test for function get_new_command
def test_get_new_command():
	command_test = Command("git add &something", "error: pathspec '&something' did not match any file(s) known to git.\nUse 'git add --force &something' to add the path to the index.\n")

	assert get_new_command(command_test) == 'git add --force &something'

# Generated at 2022-06-14 09:56:00.269842
# Unit test for function match
def test_match():
    assert match(Command('git add', 'The following paths are ignored by one'
                         ' of your .gitignore files:', 'Use -f if you really'
                         ' want to add them.'))
    assert not match(Command('git add', 'The following paths are ignored by'
                             ' one of your .gitignore files:', 'Use -f if you'
                             ' really want to add them.', 'Please move or'
                             ' remove them before you commit.'))
    assert not match(Command('git add', 'The following paths are ignored by'
                             ' one of your .gitignore files:', 'Please move or'
                             ' remove them before you commit.'))


# Generated at 2022-06-14 09:56:02.518083
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add --all', "git add --all error: The following paths are ignored ...")
    assert get_new_command(command) == 'git add --all --force'

# Generated at 2022-06-14 09:56:07.155741
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command('git add --force added_files') ==
            'git add --force added_files')
    assert (get_new_command('git add added_files') ==
            'git add --force added_files')

# Generated at 2022-06-14 09:56:13.590964
# Unit test for function get_new_command
def test_get_new_command():
    command_test = "git add"
    output_test = "fatal: The following untracked working tree files would be overwritten by merge:\n" \
                  "file1.txt\n" \
                  "Please move or remove them before you can merge.\n" \
                  "Aborting\n"
    assert (get_new_command(Command(script=command_test, output=output_test)) ==
            "git add --force")

# Generated at 2022-06-14 09:56:18.318809
# Unit test for function match
def test_match():
    assert match(Command('git add *', '', '', '', '', '', '', ''))
    assert not match(Command('git add file.txt', '', '', '', '', '', '', ''))



# Generated at 2022-06-14 09:56:21.041087
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                         "fatal: pathspec 's' did not match any files",
                         ''))
    assert match(Command('git add .',
                         "fatal: pathspec 's' did not match any files",
                         ''))
    assert not match(Command('ls', 'Use -f if you really want to add them.'))



# Generated at 2022-06-14 09:56:22.733392
# Unit test for function match
def test_match():
    assert match(Command('git add',
    'Use "-i" to selectively add some of the untracked files.'))
    assert not match(Command('git add',
    'fatal: No names found, cannot describe anything.'))


# Generated at 2022-06-14 09:56:27.299671
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git add -A",
                      "fatal: This operation must be run in a work tree\n",
                      "cd /home/kame/Development/Linux/Thefuck/")
    assert get_new_command(command) == "git add -A --force"

# Generated at 2022-06-14 09:56:29.639399
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .')) == 'git add --force .'



# Generated at 2022-06-14 09:56:42.966795
# Unit test for function match

# Generated at 2022-06-14 09:56:53.685011
# Unit test for function match

# Generated at 2022-06-14 09:56:57.979758
# Unit test for function match
def test_match():
    assert match(Command('git add foo.py',
                         'fatal: pathspec \'foo.py\' did not match any files\n'
                         'Use -f if you really want to add them.'))
    assert not match(Command('git add foo.py', 'some_error'))


# Generated at 2022-06-14 09:57:00.431383
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', 'use -f if you really want to add them')) == 'git add --force .'

# Generated at 2022-06-14 09:57:04.935793
# Unit test for function match
def test_match():
    command = Command(script='git add', output='The following untracked working tree files would be overwritten by merge:\n\n        c:\n\nPlease move or remove them before you can merge.\nAborting\n')
    assert match(command)


# Generated at 2022-06-14 09:57:08.947443
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add file.txt', 'Use -f if you really want to add them.')) == 'git add --force file.txt'

# Generated at 2022-06-14 09:57:18.773453
# Unit test for function match
def test_match():
    # 1. Test whether it will match when the command is "git add" but the
    #    error message is not the one we expected
    assert not match(command=Command('git add foo',
                                     'error: The following untracked working tree files would be overwritten by merge:',
                                     ''))

    # 2. Test whether it will match when the command is "git add -f"
    assert not match(command=Command('git add -f foo',
                                     'error: The following untracked working tree files would be overwritten by merge:',
                                     ''))

    # 3. Test whether it will match when the command is "git add" and the
    #    error message is the one we expected

# Generated at 2022-06-14 09:57:23.796498
# Unit test for function get_new_command
def test_get_new_command():
    mCommand = MagicMock(script="git add bad_file.py")
    mCommand.output = "fatal: pathspec 'bad_file.py' did not match any files\nUse -f if you really want to add them.\n"
    assert(get_new_command(mCommand) == "git add --force bad_file.py")

# Generated at 2022-06-14 09:57:35.140383
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add foo', 'fatal: pathspec \'foo\' did not match any files\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add foo --force'
    command = Command('git add foo bar', 'fatal: pathspec \'foo\' did not match any files\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add foo bar --force'
    command = Command('git add', 'fatal: pathspec \'foo\' did not match any files\nUse -f if you really want to add them.\nfatal: pathspec \'bar\' did not match any files\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add --force'

# Generated at 2022-06-14 09:57:43.714462
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         stderr='The following untracked working tree files ' +
                                'would be overwritten by merge:'))
    assert match(Command('git add',
                         stderr='The following untracked working tree files ' +
                                'would be overwritten by checkout:'))
    assert not match(Command('git add file1',
                             stderr='The following untracked working tree ' +
                                    'files would be overwritten by merge:'))


# Generated at 2022-06-14 09:57:55.442689
# Unit test for function match
def test_match():
    output = '''
    The following paths are ignored by one of your .gitignore files:
    .idea
    Use -f if you really want to add them.
    fatal: no files added
    '''
    assert (match(Command('git add .', output))
            and not match(Command('git add .')))

# Generated at 2022-06-14 09:58:00.343996
# Unit test for function match
def test_match():
    assert match(Command('git add file1 file2 file3',
                         'Use -f if you really want to add them.'))
    assert not match(Command('git add file1 file2 file3', ''))
    assert not match(Command('cd wrong', ''))


# Generated at 2022-06-14 09:58:03.856970
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                         'Use -f if you really want to add them.'))
    assert match(Command('git add .', '')) is False


# Generated at 2022-06-14 09:58:06.892640
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git add --force", "", "Use -f if you really want to add them.", "")
    get_new_command(command)

# Generated at 2022-06-14 09:58:08.809389
# Unit test for function match

# Generated at 2022-06-14 09:58:11.292183
# Unit test for function match
def test_match():
    args = "git add ."

    command = Command(script = args)

    assert match(command)


# Generated at 2022-06-14 09:58:24.540481
# Unit test for function match
def test_match():
	assert match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\n.gitignore\nUse -f if you really want to add them.')) == True
	assert match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\n.gitignore\nNewPaths\nUse -f if you really want to add them.')) == True
	assert match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\n.gitignore\nNewPaths\nSecond Line')) == False
	assert match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\n.gitignore\n')) == False

# Generated at 2022-06-14 09:58:30.380555
# Unit test for function match
def test_match():
    result = match(Command('git add src/file1.py src/file2.py', '',
                           'fatal: Pathspec \'src/file1.py\' is in submodule \'src/file2.py\'\nUse --force if you really want to add them.'))
    assert result == True


# Generated at 2022-06-14 09:58:35.814698
# Unit test for function match
def test_match():
    assert match(Command('git add', "The following paths are ignored by one of your .gitignore files:", True))
    assert match(Command('git add', "Use -f if you really want to add them.", True))
    assert match(Command('git add', "bad output", True)) is False


# Generated at 2022-06-14 09:58:40.447280
# Unit test for function match
def test_match():
    match_result = match(Command('git add file',
                                 '''The following paths are ignored by one of your .gitignore files:
file
Use -f if you really want to add them.'''))
    assert match_result, "Should be true!"


# Generated at 2022-06-14 09:58:54.832118
# Unit test for function match
def test_match():
    assert(match("git add ."))
    assert(not match("git add"))

# Generated at 2022-06-14 09:58:59.832702
# Unit test for function match
def test_match():
    assert match(Command('git add file.py', ''))



# Generated at 2022-06-14 09:59:03.925473
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', '', 'fatal: pathspec \'commit\' did not match any files\nUse -f if you really want to add them.')) == 'git add --force'

# Generated at 2022-06-14 09:59:07.256642
# Unit test for function match
def test_match():
    assert not match(Command('git add'))
    assert match(Command('git add "*"', stderr="Use -f if you really want to add them."))


# Generated at 2022-06-14 09:59:09.156786
# Unit test for function get_new_command
def test_get_new_command():
    # It should return the correct new command
    command = 'git add "./newFile"'
    assert get_new_command(command) == 'git add --force "./newFile"'

# Generated at 2022-06-14 09:59:19.259202
# Unit test for function match
def test_match():
    assert match(Command('git add README.md', stderr='error: The following patterns did not match any file(s): README.md\nUse -f if you really want to add them.\n'))
    assert not match(Command('git add README.md', stderr='error: The following patterns did not match any file(s): README.md\n'))
    assert not match(Command('git pull', stderr='From github.com:nvbn/thefuck\n * branch            master     -> FETCH_HEAD\nAlready up-to-date.\n'))
    assert not match(Command('vim test.py'))


# Generated at 2022-06-14 09:59:22.562103
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_add_force import get_new_command

    assert get_new_command(Command('git add hello', '')) == 'git add --force hello'

# Generated at 2022-06-14 09:59:32.059096
# Unit test for function get_new_command
def test_get_new_command():
	git_add_output = "error: The following untracked working tree files would be overwritten by merge:\n" \
					 "	public/img/\n" \
					 "	public/img/1.jpg\n" \
					 "	public/img/2.jpg\n" \
					 "Please move or remove them before you can merge.\n" \
					 "Aborting"
	git_add_script_parts = ['git', 'add', 'public/img']
	command = CommandWithOutput(script=git_add_script_parts, output=git_add_output)
	new_command = get_new_command(command)
	assert ' '.join(new_command.script) == 'git add --force public/img'

# Generated at 2022-06-14 09:59:41.461643
# Unit test for function match
def test_match():
    from thefuck.rules.git_add_ignored import match
    assert match(Command('git add .', 'fatal: pathspec \'file\' did not match any files\nUse -f if you really want to add them.\n'))
    assert not match(Command('git add .', 'fatal: pathspec \'file\' did not match any files'))
    assert not match(Command('git commit', 'fatal: pathspec \'file\' did not match any files\nUse -f if you really want to add them.\n'))


# Generated at 2022-06-14 09:59:45.305858
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('git add Test.py', 'fatal: not adding Test.py: '
        'You told me to ignore Test.py\nUse -f if you really want to add them.'
        )
    ) == 'git add --force Test.py'

# Generated at 2022-06-14 10:00:10.541887
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git add file1.py') == 'git add --force file1.py'

# Generated at 2022-06-14 10:00:15.116870
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         'error: The following untracked working tree files '
                         'would be overwritten by merge:', '', '',
                         'The following untracked working tree files '
                         'would be overwritten by merge:', ''))
    assert not match(Command())


# Generated at 2022-06-14 10:00:20.715331
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add src/lib.rs')
    command.stderr = 'The following paths are ignored by one of your .gitignore files:\n\
  src/lib.rs\nUse -f if you really want to add them.\nfatal: no files added'
    assert get_new_command(command) == 'git add --force src/lib.rs'

# Generated at 2022-06-14 10:00:24.146270
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert (get_new_command(Command('git add .', '')) ==
            'git add --force .')


# Generated at 2022-06-14 10:00:25.823583
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git add .").script == "git add --force ."

# Generated at 2022-06-14 10:00:34.225922
# Unit test for function match
def test_match():
    assert match(Command('git add', 'warning: adding embedded git repository'))
    assert match(Command('git add', "fatal: pathspec 'abc' did not match any files"))
    assert not match(Command('git add', 'warning: adding embedded git repository'))
    assert not match(Command('git add', "fatal: pathspec 'abc' did not match any files"))


# Generated at 2022-06-14 10:00:42.801249
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git status') == 'git status'
    assert get_new_command('git add .') == 'git add --force .'
    assert get_new_command('git add --force .') == 'git add --force .'
    assert get_new_command(
        'git add --force .',
        'The following paths are ignored by one of your .gitignore files:\n.DS_Store\nUse -f if you really want to add them.'
    ) == 'git add --force .'

# Generated at 2022-06-14 10:00:49.971479
# Unit test for function match
def test_match():
    command = Command('git add file.txt', 'The following paths are ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.')
    assert match(command)

    command = Command('git add file.txt', '')
    assert not match(command)

    command = Command('cd ~/temp', '')
    assert not match(command)



# Generated at 2022-06-14 10:00:53.917451
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add foo', 'The following paths are ignored by one of your .gitignore files:\r\nfoo\r\nUse -f if you really want to add them.')
    get_new_command(command) == 'git add --force foo'

# Generated at 2022-06-14 10:00:58.051237
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'Use --force if you really want to add them.')) == 'git add --force'

# Generated at 2022-06-14 10:01:37.642511
# Unit test for function match
def test_match():
    assert match(Command('git add README.md', '', 'The following paths are ignored by one of your .gitignore files:\nREADME.md\nUse -f if you really want to add them.\nabort: no files added\n'))
    assert not match(Command('git add README.md', '', 'The following paths are ignored by one of your .gitignore files:\nREADME.md\nUse -f if you really want to add them.\nabort: no files added\n'))


# Generated at 2022-06-14 10:01:42.459979
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .', '', 'The following paths are ignored by one of your .gitignore files:\n\tpublic/uploads\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add --force .'

# Generated at 2022-06-14 10:01:45.450953
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git add',
                                    '/dev/null: open failed: No such file or directory',
                                    True)) == 'git add --force')

# Generated at 2022-06-14 10:01:59.132029
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(parse_script(
        'git add x.txt')) == 'git add --force x.txt'
    assert get_new_command(parse_script(
        'git add .')) == 'git add --force .'
    assert get_new_command(parse_script(
        'git add -A')) == 'git add --force -A'
    assert get_new_command(parse_script(
        'git add file1')) == 'git add --force file1'
    assert get_new_command(parse_script(
        'git add *')) == 'git add --force *'
    assert get_new_command(parse_script(
        'git add -f x.txt')) == 'git add --f --force x.txt'