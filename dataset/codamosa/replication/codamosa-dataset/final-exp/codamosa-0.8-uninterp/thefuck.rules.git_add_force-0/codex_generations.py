

# Generated at 2022-06-14 09:51:59.286219
# Unit test for function match
def test_match():
    command = Command('git add',
                      'error: The following untracked working tree files would be overwritten by merge:\n a\nAdd them to the commit or stash them away with "git add <filename>".\n')
    assert match(command)


# Generated at 2022-06-14 09:52:02.122013
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git add .', '', 'Use -f if you really want to add them.') == 'git add --force .'

# Generated at 2022-06-14 09:52:07.121754
# Unit test for function match
def test_match():
    output_of_command = "The following paths are ignored by one of your .gitignore files:\n"\
                        ".idea\nUse -f if you really want to add them.\nfatal: no files added"
    command_given = "git add ."
    assert match(Command(script = command_given, output = output_of_command))



# Generated at 2022-06-14 09:52:08.267831
# Unit test for function match
def test_match():
    assert match(Command('git add *'))


# Generated at 2022-06-14 09:52:13.295787
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:', 'Use -f if you really want to add them.'))
    assert not match(Command('git add .', '', '', ''))
    assert not match(Command('git add .', '', '', '', '/usr/local/bin/git'))
    assert not match(Command('git commit .', '', '', '', '/usr/local/bin/git'))



# Generated at 2022-06-14 09:52:24.454590
# Unit test for function match
def test_match():
    supported_shells = ['bash', 'zsh']
    for shell in supported_shells:
        assert match(Command('git add file1 file2 file3', '',
                             'The following paths are ignored by one '
                             'of your .gitignore files:\n'
                             'file1\nfile2\nfile3\n'
                             'Use -f if you really want to add them.\n'
                             'The following paths are ignored by your '
                             'gitignore files:\n'))

# Generated at 2022-06-14 09:52:28.342338
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_add_f import get_new_command
    command = type('Command', (object,), {
        'script': 'git add',
        'output': 'Use -f if you really want to add them.'})
    assert get_new_command(command) == 'git add --force'

# Generated at 2022-06-14 09:52:36.354375
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add test.txt', f"""error: test.txt: 'utf-8' codec can't decode byte 0x92 in position 5: invalid start byte
    test.txt: error: pathspec 'test.txt' did not match any file(s) known to git.
    Add anyway? [y/N] error: unable to read test.txt
    Use -f if you really want to add them.""")
    assert get_new_command(command) == """git add --force test.txt"""


# Generated at 2022-06-14 09:52:39.383314
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add foo.txt', 'fatal: Not a git repository (or any of the parent directories): .git\nUse -f if you really want to add them.\n')) == 'git add --force foo.txt'
    
    

# Generated at 2022-06-14 09:52:43.169326
# Unit test for function match
def test_match():
    assert match(Command('git add',
             'The following paths are ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.'))
    assert not match(Command('git clone', ''))


# Generated at 2022-06-14 09:52:56.549335
# Unit test for function match
def test_match():
    assert match(Command('git foo',
                         'error: The following untracked working tree files would be overwritten by merge:\n  xxxxx.yyyy\nPlease move or remove them before you can merge.'))
    assert not match(Command('git foo',
                             'error: The following untracked working tree files would be overwritten by merge:\n  xxxxx.yyyy\nPlease move or remove them before you can merge.\n'
                             'And you can use this to prevent the error'))
    assert match(Command('git add xxxxx.yyyy',
                         'The following untracked working tree files would be overwritten by merge:\n  xxxxx.yyyy\nPlease move or remove them before you can merge.'))

# Generated at 2022-06-14 09:52:59.118987
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add src/WTF.java')) == 'git add --force src/WTF.java'


# Generated at 2022-06-14 09:53:00.910367
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add .') == 'git add --force .'

# Generated at 2022-06-14 09:53:14.537505
# Unit test for function match
def test_match():
    """
    Test for match function

    """
    assert git.match(Command('git branch --track origin/feature', 'fatal: Not a git repository (or any parent up to mount point /home)\nStopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).', 'git branch --track origin/feature\nfatal: Not a git repository (or any parent up to mount point /home)\nStopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).')) == None

    assert git.match(Command('git add --track origin/feature', "error: open('1.py'): Permission denied", 'git add --track origin/feature\nerror: open(\'1.py\'): Permission denied')) == None


# Generated at 2022-06-14 09:53:18.693880
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         'fatal: pathspec \'file\' did not match any files\n'
                         'Use "git add --force..." to add matching paths.'))
    assert not match(Command('git add', ''))


# Generated at 2022-06-14 09:53:23.138515
# Unit test for function match
def test_match():
    assert match(Command(script="git add .",
                         output="error: The following untracked working tree files would be overwritten by merge:\n    .travis.yml\n    doc/Doxyfile\n    doc/examples/CMakeLists.txt\n    doc/examples/fibonacci.cpp\n    doc/examples/fibonacci.hpp\n    doc/examples/fibonacci.o\nPlease move or remove them before you can merge.\nAborting"))
    assert not match(Command(script="git add .",
                             output=""))
    assert not match(Command(script="git add .",
                             output=""))
    assert not match(Command(script="git add .",
                             output="'add' is not a git command"))


# Generated at 2022-06-14 09:53:31.334156
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git add hello.py", "fatal: hello.py: '*.py' is outside repository", None)
    assert get_new_command(command) == 'git add --force hello.py'

# Generated at 2022-06-14 09:53:36.483268
# Unit test for function match
def test_match():
    assert match(Command('git add xyz', '', 'fatal: Pathspec \'xyz\' is in submodule \'xyz\'.\nUse --force to continue adding it.\n', 1))
    assert not match(Command('git add xyz', '', 'fatal: Pathspec \'xyz\' is in submodule \'xyz\'.', 1))

# Generated at 2022-06-14 09:53:41.697629
# Unit test for function get_new_command

# Generated at 2022-06-14 09:53:45.263874
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git add . --force' == get_new_command(Command('git add .', 
            'warning: adding embedded git repository: .git\nUse -f if you really want to add them.'))

# Generated at 2022-06-14 09:53:51.613959
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .')
    command.status = 1
    command.output = 'Use -f if you really want to add them.'
    new_command = get_new_command(command)
    assert new_command == 'git add --force .'

# Generated at 2022-06-14 09:53:55.779592
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git add',
                                   output=r"error: The following untracked working tree files would be overwritten by merge: \n\n Use -f if you really want to add them.")) == 'git add --force'

# Generated at 2022-06-14 09:54:02.574898
# Unit test for function match
def test_match():
    assert match(Command('git add ', 'Use -f if you really want to add them.'))
    assert not match(Command('git add ', ''))



# Generated at 2022-06-14 09:54:06.411960
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'Use -f if you really want to add them.'))
    assert not match(Command('git add .', ''))
    assert not match(Command('git add folder/', ''))



# Generated at 2022-06-14 09:54:11.581917
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git add to_add', 'Use -f if you really want to add them.'))
            == 'git add --force to_add')



# Generated at 2022-06-14 09:54:15.951157
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\nfoo\nUse -f if you really want to add them.'))
    assert not match(Command('git add .', ''))

# Generated at 2022-06-14 09:54:20.621565
# Unit test for function match
def test_match():
    assert match(Command('git add --all'))
    assert not match(Command('git add'))
    assert not match(Command('git add --force'))


# Generated at 2022-06-14 09:54:25.459511
# Unit test for function get_new_command
def test_get_new_command():
	command = command = Command('git diff xxx/xxx | git add -p',
		'fatal: pathspec xxx/xxx did not match any files',
		[])
	assert get_new_command(command) == 'git diff xxx/xxx | git add --force -p'


# Generated at 2022-06-14 09:54:31.748773
# Unit test for function match
def test_match():
	assert match(Command('git add foo', 'foo: needs merge\nUse -f if you really want to add them.'))
	assert not match(Command('git add foo', 'foo: needs merge'))
	assert not match(Command('ls', 'foo: needs merge\nUse -f if you really want to add them.'))


# Generated at 2022-06-14 09:54:41.057011
# Unit test for function match
def test_match():
    assert match(Command('git add e',
            output='fatal: pathspec \'e\' did not match any files'))
    assert match(Command('git add ',
            output='fatal: pathspec \'\' did not match any files'))
    assert not match(Command('git add e'))
    assert not match(Command('git add e',
            output='fatal: pathspec \'e\' did not match any files\n'
                   'Use -f if you really want to add them.'))



# Generated at 2022-06-14 09:54:46.513307
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert (get_new_command(Command('git add', 'Use -f if you really want to add them.'))
            == 'git add --force')

# Generated at 2022-06-14 09:54:52.463412
# Unit test for function match
def test_match():
    assert match(Command('git add file', 'The following paths are ignored by one of your .gitignore files:\nfile\nUse -f if you really want to add them.'))
    assert not match(Command('git add file.txt', "warning: LF will be replaced by CRLF in file.txt.\nThe file will have its original line endings in your working directory."))


# Generated at 2022-06-14 09:54:54.641469
# Unit test for function get_new_command
def test_get_new_command():
    assert git_forced_add.get_new_command('git add foo/bar/baz') == 'git add --force foo/bar/baz'

# Generated at 2022-06-14 09:54:59.990747
# Unit test for function match
def test_match():
    assert match(Command('git add', stderr='fatal: cannot do dry run without --force.\n'))
    assert match(Command('git add .', stderr='fatal: cannot do dry run without --force.\n'))
    assert not match(Command('git add'))
    assert not match(Command('git add .'))
    assert not match(Command('git add -f'))
    assert not match(Command('git add -f'))


# Generated at 2022-06-14 09:55:08.978151
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add foo.txt', '', 'error: foo.txt: ' +
                                      'You need to have exactly one of --cached ' +
                                      'or --no-cached, not both error: ' +
                                      'bar.txt: You need to have exactly ' +
                                      'one of --cached or --no-cached, not both'
                                      '\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add --force foo.txt'

# Generated at 2022-06-14 09:55:11.218417
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'error')) == 'git add --force'


# Generated at 2022-06-14 09:55:14.372374
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add A')
    command.stderr = 'The following paths are ignored by one of your .gitignore files: A\nUse -f if you really want to add them.'
    assert get_new_command(command) == 'git add --force A'

# Generated at 2022-06-14 09:55:19.123443
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.shells import Bash
    command = Bash('git add . && git commit', 'The following untracked directories have been added: docs')
    assert get_new_command(command) == \
        'git add --force . && git commit'

# Generated at 2022-06-14 09:55:22.001077
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         'fatal: LF would be replaced by CRLF in foo.\n'
                         'Use -f to force'))



# Generated at 2022-06-14 09:55:27.861212
# Unit test for function get_new_command
def test_get_new_command():
    command = "git add . && git commit -m 'my message'"
    output = 'The following paths are ignored by one of your .gitignore files:\n.gitignore\nUse -f if you really want to add them.'
    assert get_new_command(Command(command, output)) == 'git add --force . && git commit -m \'my message\''

# Generated at 2022-06-14 09:55:34.653940
# Unit test for function match
def test_match():
	assert match(Command('git add my-file', '', 'fatal: LF would be replaced by CRLF in my-file', ''))
	assert match(Command('git add my-file', '', 'fatal: LF would be replaced by CRLF in my-file', ''))


# Generated at 2022-06-14 09:55:44.716264
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', 'ttt', '')) == 'git add --force .'
    assert get_new_command(Command('git add ttt', 'ttt', '')) == 'git add --force ttt'
    assert get_new_command(Command('git add -A', 'ttt', '')) == 'git add --force -A'
    assert get_new_command(Command('git add ', 'ttt', '')) == 'git add --force '
    assert get_new_command(Command('git add', 'ttt', '')) == 'git add --force'


# Generated at 2022-06-14 09:55:46.803797
# Unit test for function match
def test_match():
    assert match(Command('git status'))
    assert match(Command('git add'))
    assert not match(Command('git commit -m "blah"'))


# Generated at 2022-06-14 09:55:51.127630
# Unit test for function match
def test_match():
    assert match(Command('git add', '\nOn branch master\nChanges not staged for commit:\n        modified:   README.md\nUse "-f" to force files to be added.', '', 1))


# Generated at 2022-06-14 09:55:54.876241
# Unit test for function match
def test_match():
	assert match(Command('git add',
	                     'The following paths are ignored by one of your .gitignore files:',
	                     'Use -f if you really want to add them.'))


# Generated at 2022-06-14 09:56:02.124140
# Unit test for function match
def test_match():
    assert not match(Command('git add', ''))
    assert match(Command('git add .', 'fatal: pathspec . did not match any files'))

    assert not match(Command('git add .', ''))
    assert match(Command('git add .', 'The following paths are ignored (see the '
                        'include-list in the .git/info/exclude file):\n\t.pyc\n'
                        'Use -f if you really want to add them.\n'))



# Generated at 2022-06-14 09:56:05.588683
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add',
                                   'fatal: LF would be replaced by CRLF in somefile.py',
                                   '')) == 'git add --force'

# Generated at 2022-06-14 09:56:10.434544
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add', 'The following paths are ignored by one of your .gitignore files:', 'Use -f if you really want to add them.')
    new_command = get_new_command(command)
    assert new_command == 'git add --force'

# Generated at 2022-06-14 09:56:22.035913
# Unit test for function match
def test_match():
	script = 'git add file.py'
	out = 'The following paths are ignored by one of your .gitignore files:\nfile.py\nUse -f if you really want to add them.'
	with pytest.raises(SystemExit):
		assert match(Command(script, out))
	script = 'git add file.py'
	out = 'The following paths are ignored by one of your .gitignore files:\nfile.py\nUse -f if you really want to add them.'
	assert match(Command(script, out))
	script = 'git add file.py'
	out = 'The following paths are ignored by one of your .gitignore files:\nfile.py'
	assert not match(Command(script, out))

# Generated at 2022-06-14 09:56:26.623347
# Unit test for function get_new_command
def test_get_new_command():
    command=Command('git add -A lib/spam.py',
        'The following paths are ignored by one of your .gitignore files: lib/eggs.py\n'
        'Use -f if you really want to add them.\n')
    assert(get_new_command(command)) == 'git add --force -A lib/spam.py'

# Generated at 2022-06-14 09:56:32.285311
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add aaa.txt', '', 'Use -f if you really want to add them.')) == 'git add --force aaa.txt'



# Generated at 2022-06-14 09:56:36.482187
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add', ('The following paths are ignored by one of '
                                  'your .gitignore files:\n'
                                  ' .DS_Store\n'
                                  'Use -f if you really want to add them.\n'
                                  'fatal: no files added\n'))
    assert get_new_command(command) == 'git add --force'



# Generated at 2022-06-14 09:56:44.184748
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'The following untracked working tree files would be overwritten by merge:\n	file1.txt\n	file2.txt\nPlease move or remove them before you can merge.')) == 'git add --force'

# Generated at 2022-06-14 09:56:48.512299
# Unit test for function get_new_command
def test_get_new_command():
    assert git_add_to_force().get_new_command('git add file') == 'git add --force file'

# Unit test to check function match

# Generated at 2022-06-14 09:56:53.648569
# Unit test for function match
def test_match():
    assert match(Command('git add test',
            "The following paths are ignored by one of your .gitignore files:\nnon_exist_file\nUse -f if you really want to add them.\nfatal: no files added",
            ''))

# Generated at 2022-06-14 09:56:58.138226
# Unit test for function match
def test_match():
    assert match(Command('git add cow',
                         'The following paths are ignored by one of your .gitignore files:\r\ncow\r\nUse -f if you really want to add them.'))
    assert not match(Command('git add cow', ''))


# Generated at 2022-06-14 09:57:02.847613
# Unit test for function match
def test_match():
    assert match(Command('git add file',
        stderr='The following paths are ignored by one of your '.split()))
    assert not match(Command('git add file', stderr=''))



# Generated at 2022-06-14 09:57:11.834943
# Unit test for function match
def test_match():
    assert match(Command('git add .',
        'The following paths are ignored by one of your .gitignore files:',
        'Use -f if you really want to add them.'))
    assert match(Command('git add',
        'The following paths are ignored by one of your .gitignore files:',
        'Use -f if you really want to add them.'))
    assert match(Command('git add .',
        'The following paths are ignored by one of your .gitignore files:',
        'Use -f if you really want to add them.'))
    assert not match(Command('git add .', ''))
    assert not match(Command('git add .', '', ''))


# Generated at 2022-06-14 09:57:23.974742
# Unit test for function match
def test_match():
	command = Command('git add .', 'fatal: LF would be replaced by CRLF'
	+ ' in README.md\n'
	+ 'fatal: LF would be replaced by CRLF in requirements.txt\n'
	+ 'fatal: LF would be replaced by CRLF in test_uninstall.py\n'
	+ 'Use -f if you really want to add them.'
	+ 'error: src refspec master does not match any.'
	+ 'error: failed to push some refs to', '')
	assert match(command)

# Generated at 2022-06-14 09:57:25.842501
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git add .')=='git add . --force'

# Generated at 2022-06-14 09:57:36.232438
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'error: The following untracked working directory files would be overwritten by merge:\n', '')) == True
    assert match(Command('git add .', 'The following untracked working directory files would be overwritten by merge:\n', '')) == False


# Generated at 2022-06-14 09:57:41.175036
# Unit test for function match
def test_match():
    assert not match(Command('git add', ''))
    assert match(Command('git add', 'Use -f if you really want to add them.'))
    assert not match(Command('git config', 'Use -f if you really want to add them.'))
    assert not match(Command('git add . ', ''))


# Generated at 2022-06-14 09:57:43.422539
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git add')) == 'git add --force')

# Generated at 2022-06-14 09:57:48.783146
# Unit test for function match
def test_match():
    assert match(Command('git add foo.txt',
                         "error: The following untracked working tree files would be overwritten by merge:\n"
                         "        \"foo.txt\"\n"
                         "Please move or remove them before you can merge.\n"
                         "Aborting\n", ""))
    assert not match(Command('git stash', '', ''))


# Generated at 2022-06-14 09:57:55.279533
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'Use -f if you really want to add them.')) == 'git add --force'
    assert get_new_command(Command('git add foo', 'Use -f if you really want to add them.')) == 'git add --force foo'
    assert get_new_command(Command('git add --ignore-all-space foo bar', 'Use -f if you really want to add them.')) == 'git add --ignore-all-space --force foo bar'


# Generated at 2022-06-14 09:58:04.937688
# Unit test for function match
def test_match():
    assert match(Command('git add test.py',
                         'fatal: pathspec \'test.py\' did not match any files',
                         '', 1))
    assert match(Command('git add test.py',
                         'fatal: pathspec \'test.py\' did not match any files\nUse -f if you really want to add them.',
                         '', 1))
    assert not match(Command('git add -f test.py',
                             'fatal: pathspec \'test.py\' did not match any files\nUse -f if you really want to add them.',
                             '', 1))


# Generated at 2022-06-14 09:58:12.656014
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         'fatal: Pathspec \'test\' is in submodule '
                         '\'modules/test\'.\n'
                         'Use --ignore-submodules to ignore this path.'))
    assert match(Command('git add .',
                         'fatal: Pathspec \'test.yml\' is in submodule '
                         '\'modules/test\'.\n'
                         'Use --ignore-submodules to ignore this path.'))
    assert not match(Command('git add', 'fatal: Pathspec \'test\' is in'))


# Generated at 2022-06-14 09:58:16.949607
# Unit test for function get_new_command
def test_get_new_command():
    assert ('git add --force test.txt' == get_new_command(
        Command('git add test.txt', 'error: The following untracked working tree files would be overwritten by merge:\n    test.txt\nPlease move or remove them before you can merge.\nAborting\n', 'Use -f if you really want to add them.')))

# Generated at 2022-06-14 09:58:21.531491
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                         output='"*.pyc" would be added to the commit.'))
    assert not match(Command('git add .',
                             output='"*.pyc" would be added to the commit'))
    assert not match(Command('git add .',
                             output='Not a git repository'))


# Generated at 2022-06-14 09:58:22.382350
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', '')) == 'git add --force'

# Generated at 2022-06-14 09:58:29.776797
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command(u'git add -b hello').script == u'git add --force -b hello'

# Generated at 2022-06-14 09:58:40.765009
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         'fatal: pathspec \'master\' did not match any files',
                         ''))
    assert match(Command('git add',
                         'fatal: pathspec \'master\' did not match any files',
                         ''))
    assert match(Command('git add',
                         'fatal: pathspec \'master\' did not match any files',
                         ''))
    assert not match(Command('git add',
                             'fatal: pathspec \'master\' did not match any files',
                             ''))
    assert not match(Command('git add',
                             'fatal: pathspec \'master\' did not match any files',
                             ''))


# Generated at 2022-06-14 09:58:45.090287
# Unit test for function match
def test_match():
    assert match(Command('git add foo bar', '', '', 1, False))
    assert not match(Command('git add', '', '', 1, False))


# Generated at 2022-06-14 09:59:01.095624
# Unit test for function match
def test_match():
    assert match(Command('git add', '', 'warning: some warning'))
    assert not match(Command('git add', '', 'error: some warning'))

    assert match(Command('git add', '', 'Use -f if you really want to add them.'))
    assert match(Command('git add --force', '', 'Use -f if you really want to add them.'))
    assert match(Command('git add .', '', 'Use -f if you really want to add them.'))
    assert match(Command('git add foo', '', 'Use -f if you really want to add them.'))
    assert match(Command('git add foo bar', '', 'Use -f if you really want to add them.'))

    # Unit test for function get_new_command

# Generated at 2022-06-14 09:59:10.586358
# Unit test for function match
def test_match():
    assert match(command=Command('git add .', '', 'Fatal: CRLF would be replaced by LF in .gitmodules.\nThe file will have its original line endings in your working directory.\nUse -f if you really want to add them.')) is True
    assert match(command=Command('git add .', '', 'Fatal: CRLF would be replaced by LF in .gitmodules.\nThe file will have its original line endings in your working directory.\nUse -f if you really want to add them.')) is True

#Unit test for function get_new_command

# Generated at 2022-06-14 09:59:22.614128
# Unit test for function match
def test_match():
    assert ('add' in thefuck.types.Command(script='git add', output='Use -f if you really want to add them.').script_parts
            and 'Use -f if you really want to add them.' in thefuck.types.Command(script='git add', output='Use -f if you really want to add them.').output) == match(thefuck.types.Command(script='git add', output='Use -f if you really want to add them.'))

# Generated at 2022-06-14 09:59:26.471913
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt', '', '', 1))
    assert not match(Command('git add', '', 'fatal: no files added', 1))
    assert not match(Command('git file.txt', '', '', 1))

# Generated at 2022-06-14 09:59:30.762989
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add file', 'fatal: Path \'file\' is in submodule \'sub\'.\n'
                                      'Use -f if you really want to add them.\n')
    assert get_new_command(command) == 'git add --force file'

# Generated at 2022-06-14 09:59:32.601645
# Unit test for function match
def test_match():
    assert match(Command('git add --force'))
    assert not match(Command('git add'))



# Generated at 2022-06-14 09:59:41.105392
# Unit test for function get_new_command
def test_get_new_command():
    #commands = ["git add dir/"]
    #command = Command("", commands, "Use  -f if you really want to add them.")
    #print("get_new_command: " + get_new_command(command))

    commands = ["git add dir/"]
    command = Command("", commands, "Use  -f if you really want to add them.")
    print("get_new_command: " + get_new_command(command))



# Generated at 2022-06-14 09:59:59.044423
# Unit test for function match
def test_match():
    assert match(Command('git add', stderr='The following untracked working tree files would be overwritten by merge: \nfile1 \nUse -f if you really want to add them.'))
    assert not match(Command('git stash', stderr='The following untracked working tree files would be overwritten by merge: \nfile1 \nUse -f if you really want to add them.'))


# Generated at 2022-06-14 10:00:01.745142
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', 'The following patterns did not match any file(s):  .', '', '')) \
           == 'git add --force .'

# Generated at 2022-06-14 10:00:04.963030
# Unit test for function match
def test_match():
    command = Command('git add --dry-run README.md', "fatal: pathspec 'README.md' did not match any files\nDid you forget to 'git add'?\n")
    assert match(command)
    assert not match(Command('git add README.md', ''))
    


# Generated at 2022-06-14 10:00:09.912575
# Unit test for function get_new_command
def test_get_new_command(): 
 test_output = "error: 'add' is not a git command. See 'git --help'. Did you mean one of these?"
 test_command = Command('git add', test_output )
 assert get_new_command(test_command) == "git add --force"

# Generated at 2022-06-14 10:00:13.466244
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git add .' 
    assert('git add --force .' == get_new_command(Command(script, '')))
    script = 'git add .' 
    assert('git add --force .' == get_new_command(Command(script, '')))

# Generated at 2022-06-14 10:00:21.468371
# Unit test for function match
def test_match():
    assert match(Command('git add 123', '', 'error: The following untracked working tree files would be overwritten by merge:\n'))
    assert match(Command('git add', '', 'error: The following untracked working tree files would be overwritten by merge:\n'))
    assert not match(Command('git add 123', ''))
    assert not match(Command('git diff', '', 'error: The following untracked working tree files would be overwritten by merge:\n'))


# Generated at 2022-06-14 10:00:25.537072
# Unit test for function match
def test_match():
    assert match(Command('git add', '', 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.\nfatal: no files added\n'))


# Generated at 2022-06-14 10:00:31.797515
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .', 'error: The following untracked working tree files would be overwritten by merge:\n\nREADME.md\nUse -f if you really want to add them.\nAborting ')
    assert get_new_command(command) == 'git add --force .'

# Generated at 2022-06-14 10:00:38.904990
# Unit test for function match
def test_match():
    assert_true(match(Command('git add file1 file2',
                              'fatal: LF would be replaced by CRLF in file1.\n'
                              'fatal: LF would be replaced by CRLF in file2.\n'
                              'Use -f if you really want to add them.')))
    assert_true(match(Command('git add *',
                              'fatal: LF would be replaced by CRLF in file1.\n'
                              'fatal: LF would be replaced by CRLF in file2.\n'
                              'Use -f if you really want to add them.')))

# Generated at 2022-06-14 10:00:43.301729
# Unit test for function match
def test_match():
    assert match(Command('git add a', 'fatal: Pathspec \'a\' is in submodule \'c\'.\nUse --ignore-submodules to skip cdiff', ''))
    assert not match(Command('git add a', '', ''))
    assert not match(Command('git add a', '', ''))



# Generated at 2022-06-14 10:01:09.241166
# Unit test for function match
def test_match():
	assert match("git add some/file") == False
	assert match("git add some/file") == False
	assert match("git add some/file") == False

# Generated at 2022-06-14 10:01:11.572135
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add foo', 'Please commit your changes')) == 'git add --force foo'

# Generated at 2022-06-14 10:01:17.227201
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .', """
The following paths are ignored by one of your .gitignore files:
    path/to/file1
    path/to/file2
Use -f if you really want to add them.
fatal: no files added
""")
    assert(get_new_command(command) == ('git add --force .'))

# Generated at 2022-06-14 10:01:21.946752
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git add '*.py'", "fatal: pathspec '*.py' did not match any files\nUse -f if you really want to add them.")
    assert get_new_command(command) == "git add --force '*.py'"

# Generated at 2022-06-14 10:01:28.600271
# Unit test for function match
def test_match():
    assert match(Command('git add foo.txt',
                         'fatal: Pathspec \'foo.txt\' is in submodule \'bar\''))
    assert match(Command('git add bar/foo.txt',
                         'fatal: Pathspec \'bar/foo.txt\' is in submodule \'bar\''))
    assert match(Command('git add foo.txt',
                         'fatal: Pathspec \'foo.txt\' is in submodule \'bar\''
                         'Use -f if you really want to add them.'))
    assert match(Command('git add bar/foo.txt',
                         'fatal: Pathspec \'bar/foo.txt\' is in submodule \'bar\''
                         'Use -f if you really want to add them.'))

# Generated at 2022-06-14 10:01:38.618084
# Unit test for function match
def test_match():
    assert match(Command('git add', \
                         'fatal: pathspec \'README.md\' did not match any files', ''))
    assert match(Command('git add', 'Use -f if you really want to add them.', ''))
    assert not match(Command('git add', '', ''))
    assert not match(Command('git add', 'error: pathspec \'README.md\' did not match any files', ''))
    assert not match(Command('git add', 'error: Use -f if you really want to add them.', ''))


# Generated at 2022-06-14 10:01:42.300211
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert (get_new_command(Command('git add --force .', 'use -f if you really want to add them', '')) == 'git add --force --force .')

# Generated at 2022-06-14 10:01:50.220845
# Unit test for function match
def test_match():
    command = Command('git add src/',
                      'fatal: pathspec \'src/\' did not match any files', 'git add src/')
    assert not match(command)

    command = Command('git add src/',
                      'fatal: pathspec \'src/\' did not match any files\nUse -f if you really want to add them.', 'git add src/')
    assert match(command)


# Generated at 2022-06-14 10:01:53.740284
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add .') == 'git add --force .'
    assert get_new_command('git add a b') == 'git add --force a b'