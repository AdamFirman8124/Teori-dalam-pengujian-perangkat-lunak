

# Generated at 2022-06-14 09:51:59.827558
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command('git add .', 'Use -f if you really want to add them.')
    command2 = Command('git stash', 'Use -f if you really want to add them.')
    assert get_new_command(command1) == 'git add --force .'
    assert get_new_command(command2) == 'git stash'

# Generated at 2022-06-14 09:52:05.199162
# Unit test for function match
def test_match():
    assert match(Command('git add hello.txt',
                         'fatal: pathspec \'hello.txt\' did not match any files\nUse -f if you really want to add them.'))
    assert not match(Command('git add hello.txt', ''))
    assert not match(Command('git add hello.txt', '\n'))

# Generated at 2022-06-14 09:52:08.593027
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\nfatal: no files added\nUse -f if you really want to add them.'))
    

# Generated at 2022-06-14 09:52:11.558301
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(command=Command(script='git add x', output="fatal: pathspec 'x' did not match any files")) == 'git add --force x'

# Generated at 2022-06-14 09:52:13.334782
# Unit test for function get_new_command

# Generated at 2022-06-14 09:52:24.502464
# Unit test for function match
def test_match():
    assert match("git add . && git commit -m 'test'")
    assert match("git add -A && git commit -m 'test'")
    assert match("git add --ignore-removal")
    assert match("git add --ignore-removal ." )
    assert match("git add *")
    assert match("git add * ")
    assert match("git add * .")
    assert match("git add * ." )
    assert match("git add * ./")
    assert match("git add * ./ ")
    assert match("git add * ./ .")
    assert match("git add * ./ .")
    assert match("git add * ./ ." )
    assert match("git add . . . . . . .")
    assert match("git add . . . . . . ..")

# Generated at 2022-06-14 09:52:27.786647
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .')
    command.output = '''The following paths are ignored by one of your .gitignore files:
Rakefile
Use -f if you really want to add them.'''
    assert(get_new_command(command) == 'git add --force .')

# Generated at 2022-06-14 09:52:31.432213
# Unit test for function match
def test_match():
    assert match(Command('git add . --force', '', '', '', '', ''))
    assert not match(Command('git status', '', '', '', '', ''))



# Generated at 2022-06-14 09:52:36.002450
# Unit test for function match
def test_match():
    assert match(Command('git status',
                         "Your branch is up-to-date with 'origin/master'.\n\nnothing to commit, working directory clean"))

    assert not match(Command('git status', 'fatal: Not a git repository'))


# Generated at 2022-06-14 09:52:42.431629
# Unit test for function match
def test_match():
    assert not match(Command('git add', ''))
    assert match(Command('git add', 'fatal: Not a git repository'))
    assert match(Command('git add', 'fatal: Pathspec \'abc\' is in submodule '
                                     '\'xyz\' Use \'--force\' if you really '
                                     'want to add it.'))
    assert not match(Command('git add', 'fatal: Pathspec \'abc\' is in '
                                          'submodule \'xyz\' '))


# Generated at 2022-06-14 09:52:46.080978
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add *', 'fatal: Pathspec * is in submodule.')
    assert get_new_command(command) == 'git add --force *'

# Generated at 2022-06-14 09:52:49.180752
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         stderr='Use -f if you really want to add them.\n'))
    assert not match(Command('git add .',
                             stderr='Use -f if you really want to add them.\n'))



# Generated at 2022-06-14 09:52:53.816920
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('git add .', '', 'fatal: LF would be replaced by CRLF in .tox/py33/lib/python3.3/site-packages/httplib2/cacerts.txt.\n'
                               'The file will have its original line endings in your working directory.\n'
                               'Use -f if you really want to add them.')) == 'git add --force .'

# Generated at 2022-06-14 09:52:59.315211
# Unit test for function match
def test_match():
    assert match(Command('git add', 'fatal: The following untracked working tree files would be overwritten by merge:\ntest\nPlease move or remove them before you can merge.\nAborting'))
    assert not match(Command('git add something', ''))
    assert not match(Command('git', ''))


# Generated at 2022-06-14 09:53:03.000745
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add foo').script == 'git add --force foo'
    assert get_new_command('git add .').script == 'git add --force .'



# Generated at 2022-06-14 09:53:05.471990
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git add', '')) == 'git add --force')

# Generated at 2022-06-14 09:53:06.652178
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add lala') == 'git add --force lala'

# Generated at 2022-06-14 09:53:14.459623
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt', '', 'The following paths are ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.'))
    assert not match(Command('git add file.txt', '', 'The following paths are ignored by one of your .gitignore files:\nfile.txt'))


# Generated at 2022-06-14 09:53:16.348371
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git add .'
    assert get_new_command(script) == 'git add --force .'

# Generated at 2022-06-14 09:53:28.785061
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                                 'fatal: Pathspec \' .\' is in submodule \'a\'\nfatal: Pathspec \' .\' is in submodule \'a\'\nUse --ignore-submodules to keep going anyway',
                                 'git'))
    assert match(Command('git add a',
                                 'fatal: Pathspec \'a\' is in submodule \'a\'\nUse --ignore-submodules to keep going anyway',
                                 'git'))
    assert not match(Command('git add .',
                            'fatal: Pathspec \' .\' is in submodule \'a\'\nfatal: Pathspec \' .\' is in submodule \'a\'\nUse --ignore-submodules to keep going anyway',
                            'svn'))

# Generated at 2022-06-14 09:53:37.449669
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add foo.bar',
            '/usr/local/bin/git add foo.bar\nfatal: pathspec \'foo.bar\' did not match any files\nUse -f if you really want to add them.')) == 'git add --force foo.bar'

# Generated at 2022-06-14 09:53:42.760095
# Unit test for function match
def test_match():
    assert match(Command('git add foo.py',
                         'error: The following untracked working tree files would be overwritten by merge:\n'
                         '\tfoo.py\n'
                         'Please move or remove them before you can merge.\n'
                         'Aborting',
                         ''))


# Generated at 2022-06-14 09:53:44.217130
# Unit test for function match
def test_match():
    assert match(Command('git add .'))


# Generated at 2022-06-14 09:53:47.681448
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add --all',
                             'fatal: Pathspec \'--all\' is in submodule \'Apps/MyApp\'\ngit add --all\nUse -f if you really want to add them.\n')) == 'git add --all --force'

# Generated at 2022-06-14 09:53:53.880490
# Unit test for function match
def test_match():
    assert match(Command('git add .',
            '/home/user/software_universe/: error: The following untracked '
            'working tree files would be overwritten by merge:\na\nb\nc\n'
            'Please move or remove them before you can merge.\n'
            'Aborting',
            ''))


# Generated at 2022-06-14 09:54:04.784623
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git add .', '')) == 'git add . --force')
    assert (get_new_command(Command('git add .', 'error: The following untracked working tree files would be overwritten by merge:\nUse -f if you really want to add them.')) == 'git add . --force')
    assert (get_new_command(Command('git add file.txt', 'error: The following untracked working tree files would be overwritten by merge:\nUse -f if you really want to add them.')) == 'git add file.txt --force')

# Generated at 2022-06-14 09:54:11.440552
# Unit test for function match

# Generated at 2022-06-14 09:54:12.271750
# Unit test for function match
def test_match():
	pass

# Generated at 2022-06-14 09:54:19.650171
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .',
                                   'fatal: The following paths are ignored (use -f to override):',
                                   'Use -f if you really want to add them.')) == 'git add --force .'
    assert get_new_command(Command('git add -A',
                                   'The following paths are ignored by one of your .gitignore files:',
                                   'Use -f if you really want to add them.')) == 'git add -A --force'

# Generated at 2022-06-14 09:54:24.211871
# Unit test for function match
def test_match():
    assert match(Command('git add', 'The following paths are ignored by one of your .gitignore files:\n', error=True))
    assert match(Command('git add', 'The following paths are ignored by one of your .gitignore files:\n', error=True))



# Generated at 2022-06-14 09:54:32.241057
# Unit test for function match
def test_match():
    assert match(Command('git add file.py', 'fatal: Pathspec \'file.py\' is in submodule \'type/python\''))
    assert not match(Command('git add  file.py', ''))
    assert not match(Command('git status', 'On branch master'))


# Generated at 2022-06-14 09:54:34.690444
# Unit test for function match
def test_match():
    assert match(Command('git', 'add', 'file'))


# Generated at 2022-06-14 09:54:45.696962
# Unit test for function match
def test_match():
    assert match(
        Command('git add -A', 'The following paths are ignored by one of your .gitignore files: \nUse -f if you really want to add them.', 'e255'))
    assert match(
        Command('git add -A', "The following paths are ignored by one of your .gitignore files:\n	.DS_Store\n	.classpath\n	.project\n	.settings/\n	.springBeans\n	.tmp/\n	.vscode/\n	.xx\n	.git/\n	pom.xml\n	.pom.xml\n	target/\nUse -f if you really want to add them.", 'e255'))

# Generated at 2022-06-14 09:54:53.481117
# Unit test for function match
def test_match():
    assert match(Command('git add hello.py', 'fatal: pathspec \'hello.py\' did not match any files\nUse -f if you really want to add them.'))
    assert match(Command('git add .', 'fatal: pathspec \'hello.py\' did not match any files\nUse -f if you really want to add them.'))

# Generated at 2022-06-14 09:54:57.344877
# Unit test for function get_new_command
def test_get_new_command():
    assert [get_new_command(Command('git add', 'error: The following untracked working tree files would be overwritten by merge:\nUse -f if you really want to add them.'))] == [['git add --force']]

# Generated at 2022-06-14 09:55:08.513819
# Unit test for function match
def test_match():
        #Test 1
        #Input
        mock_command = type("Command", (object,), {"script": "git add .", "output": "Use -f if you really want to add them."})
        #Expected output
        expected_output = True
        #Test
        assert match(mock_command) == expected_output
        #Test 2
        #Input
        mock_command = type("Command", (object,), {"script": "git add .", "output": "modified:   .gitignore (modified content)"})
        #Expected output
        expected_output = False
        #Test
        assert match(mock_command) == expected_output


# Generated at 2022-06-14 09:55:14.249261
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.shells import shell
    from thefuck.types import Command
    command = Command('git add .', 'error: The following untracked working tree files would be overwritten by merge:\n'
                                    'Please move or remove them before you can merge.')
    assert get_new_command(command) == 'git add --force .'
    assert get_new_command(command, shell) == 'git add --force .'

# Generated at 2022-06-14 09:55:21.926059
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('git add myfile') == 'git add --force myfile'
	assert get_new_command('git add myfile.txt') == 'git add --force myfile.txt'
	assert get_new_command('git add myfile.c') == 'git add --force myfile.c'
	assert get_new_command('git add myfile.sh') == 'git add --force myfile.sh'

# Generated at 2022-06-14 09:55:28.451234
# Unit test for function match
def test_match():
	assert(match('git add .'))
	assert(match('git add .'))
	assert(match('git add'))
	assert(match('git add .'))
	assert(match('git add .'))
	assert(match('git add .'))
	assert(match('git add .'))
	assert(match('git add .'))
	assert(match('git add .'))
	assert(match('git add .'))


# Generated at 2022-06-14 09:55:30.238967
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add foo') == 'git add --force foo'

# Generated at 2022-06-14 09:55:38.790678
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git add -A', 'fatal: Pathspec \'new\' is in submodule \'old\'\nUse -f if you really want to add them.')) ==
            'git add --force -A')

# Generated at 2022-06-14 09:55:42.992604
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', '', 'Use -f if you really want to add them.')) == 'git add --force .'

# Generated at 2022-06-14 09:55:45.563560
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add',
                                   output='The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.')) == 'git add --force'

# Generated at 2022-06-14 09:55:48.990937
# Unit test for function match
def test_match():
    assert match(Command('git add', stderr="Use -f if you really want to add them."))
    assert not match('git add')



# Generated at 2022-06-14 09:55:56.243810
# Unit test for function match
def test_match():
    assert match(Command('git add hello.txt', 'error: pathspec '
                         '"hello.txt" did not match any file(s) known to git.'
                         '\nUse --ignore-missing to keep going.'))
    assert not match(Command('git add', 'error: pathspec '
                             'did not match any file(s) known to git.'
                             '\nUse --ignore-missing to keep going.'))


# Generated at 2022-06-14 09:56:01.461311
# Unit test for function match
def test_match():
    command_sample = Command('git add *',
                             'The following paths are ignored by one of your .gitignore files:\n'
                             '\t*.dat\n'
                             'Use -f if you really want to add them.',
                             '/tmp')
    assert match(command_sample)

    command_sample = Command('git add .',
                             'nothing to commit, working directory clean',
                             '/tmp')
    assert not match(command_sample)



# Generated at 2022-06-14 09:56:04.906117
# Unit test for function get_new_command
def test_get_new_command():
    script = "git add README.rst"
    new_script = get_new_command(script, "")
    assert new_script == "git add --force README.rst"

# Generated at 2022-06-14 09:56:09.783859
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add file', stderr = 'fatal: pathspec \'file\' is in submodule '.encode('utf-8') + '\'sub\'')
    assert get_new_command(command) == 'git add --force file'

# Generated at 2022-06-14 09:56:13.274471
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'Use -f if you really want to add them.')) == 'git add --force'

# Generated at 2022-06-14 09:56:17.047366
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add')) == 'git add --force'
    assert get_new_command(Command('git add folder')) == 'git add --force folder'

# Generated at 2022-06-14 09:56:31.493261
# Unit test for function match
def test_match():
    assert match(Command('git add', 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.\n'))
    assert not match(Command('git add', 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.'))

# Generated at 2022-06-14 09:56:35.971999
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'fatal: LF would be replaced by CRLF in .gitignore.\n'
                         'Use -f if you really want to add them.'))
    assert not match(Command('git add ', 'fatal: LF would be replaced by CRLF in .gitignore.\n'
                         'Use -f if you really want to add them.'))


# Generated at 2022-06-14 09:56:46.425821
# Unit test for function match
def test_match():
    assert match(Command('git add test.txt', 'The following untracked working files would be overwritten by merge:\n    test.txt\n    readme.txt\nPlease move or remove them before you can merge.'))
    assert not match(Command('git add test.txt', 'warning: LF will be replaced by CRLF'))


# Generated at 2022-06-14 09:56:49.589719
# Unit test for function match
def test_match():
    assert match(Command(script='git add', output='Use -f if you really want to add them.'))
    assert not match(Command(script='git add', output='No file changed'))


# Generated at 2022-06-14 09:56:59.884200
# Unit test for function match
def test_match():
	assert match(Command('git add foo.txt', 'fatal: pathspec \x27foo.txt\x27 did not match any files\nUse \x27git add --force\x27 to add the path to the index anyway.\n'))
	assert not match(Command('git add', 'On branch master\nYour branch is up-to-date with \'origin/master\'.\n\nUntracked files:\n  (use "git add <file>..." to include in what will be committed)\n\tfoo.txt\n\nnothing added to commit but untracked files present (use "git add" to track)\n'))


# Generated at 2022-06-14 09:57:04.204133
# Unit test for function get_new_command

# Generated at 2022-06-14 09:57:13.941502
# Unit test for function match
def test_match():
    assert match(Command('git add file1 file2 file3', 'warning: LF will be replaced by CRLF in file1.\nThe file will have its original line endings in your working directory.\nwarning: LF will be replaced by CRLF in file2.\nThe file will have its original line endings in your working directory.\nerror: unable to add file3: File exists.\nUse -f if you really want to add them.'))
    assert not match(Command('git add file1', 'warning: LF will be replaced by CRLF in file1.\nThe file will have its original line endings in your working directory.'))

# Generated at 2022-06-14 09:57:16.457530
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', '')) == 'git add --force .'

# Generated at 2022-06-14 09:57:21.973445
# Unit test for function match
def test_match():
    assert match(Command('git add foo faa', ''))
    assert not match(Command('git add foo faa', 'fatal: pathspec',
                             'fatal: pathspec \'foo\' did not match any files'))
    assert not match(Command('git add', '', 'fatal: no files added'))
    

# Generated at 2022-06-14 09:57:27.750383
# Unit test for function match
def test_match():
	assert match(Command("git add .", "fatal: core.longpaths is set to true, \
but core.ignorecase is not set.  This will break in future versions of Git, \
and should be set to false.\nUse -f if you really want to add them.\n"))


# Generated at 2022-06-14 09:57:51.698083
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git add .',
                                    'The following paths are ignored by one of your .gitignore files:\n',
                                    'Use -f if you really want to add them.')) == 'git add --force .')

# Generated at 2022-06-14 09:58:01.623757
# Unit test for function match
def test_match():

    @git_support
    def match_sub(command):
        return command.script_parts == ['git', 'add', 'e']

    def _assert(script, result):
        assert match_sub(Command(script, 'Use -f if you really want to add them.')) == result

    _assert('git add e', True)
    _assert('git add e', True)
    _assert('git add e e', False)
    _assert('git add', False)
    _assert('git add e --force', False)
    _assert('fuck add e', False)


# Generated at 2022-06-14 09:58:08.737223
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git status") == "git status"
    assert get_new_command("git add") == "git add --force"
    assert get_new_command("git add app/models/ ") == "git add --force app/models/ "
    assert get_new_command("git add .") == "git add --force ."
    assert get_new_command("git add --all") == "git add --all"
    assert get_new_command("git add app/models/ ") == "git add --force app/models/ "
    assert get_new_command("git add --all") == "git add --all"
    assert get_new_command("git add app/models/ ") == "git add --force app/models/ "

# Generated at 2022-06-14 09:58:17.729381
# Unit test for function match
def test_match():
    command1 = Command('git add', '')
    assert not match(command1)
    
    command2 = Command('git add --force', '')
    assert not match(command2)
    
    command3 = Command('git add', 'error: The following paths are ignored by one of your .gitignore files:')
    assert not match(command3)
    
    command4 = Command('git add', 'Use -f if you really want to add them.')
    assert match(command4)
        

# Generated at 2022-06-14 09:58:20.483997
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add foo') == 'git add --force foo'
    assert get_new_command('git add foo bar') == 'git add --force foo bar'


# Generated at 2022-06-14 09:58:21.566518
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add filename') ==  'git add --force filename'


# Generated at 2022-06-14 09:58:25.513764
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add --all', 'The following paths are ignored by one of your .gitignore files:\n\tfile1.txt\n\tfile2.txt\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add --all --force'



# Generated at 2022-06-14 09:58:37.268362
# Unit test for function match
def test_match():
    assert match(Command('git add', 
                         stderr='error: The following untracked working tree files would be overwritten by merge:\n\tREADME\n\tRakefile',
                         script='git add'))
    assert not match(Command('git add', 
                             stderr='error: The following untracked working tree files would be overwritten by merge:\n\tREADME\n\tRakefile',
                             script='git add --force'))
    assert not match(Command('sudo git add', 
                             stderr='error: The following untracked working tree files would be overwritten by merge:\n\tREADME\n\tRakefile',
                             script='sudo git add'))


# Generated at 2022-06-14 09:58:40.342882
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git add', 'Use -f if you really want to add them.')) == 'git add --force')



# Generated at 2022-06-14 09:58:44.594125
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('git add file.txt', 'warning: LF will be replaced by CRLF')) == 'git add --force file.txt'

# Generated at 2022-06-14 09:59:32.082882
# Unit test for function match
def test_match():
    # test when command has add
    assert match(Command('git add', '', 'some/file.txt: needs update'))

    # test when output contains message
    assert match(Command('git add', '', 'some/file.txt: needs update\n\
Aborting\n\
Use -f if you really want to add them.'))

    # test when command has add and output contains message
    assert match(Command('git add some/file.txt', '', 'some/file.txt: needs update\n\
Aborting\n\
Use -f if you really want to add them.'))

    #test wen command has add and output just contains message
    assert match(Command('git add some/file.txt', '', 'Aborting\n\
Use -f if you really want to add them.'))

    #test when command has add

# Generated at 2022-06-14 09:59:36.513778
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add ', 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.')) == 'git add --force'

# Generated at 2022-06-14 09:59:40.826860
# Unit test for function match
def test_match():
    assert match(Command('git add --force',
                         'Use -f if you really want to add them.'))
    assert not match(Command('git add --force', ''))
    assert not match(Command('git reset --hard', ''))


# Generated at 2022-06-14 09:59:47.684474
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('name', 'add --force', 'Use -f if you really want to add them.')
    new_command = get_new_command(command)
    assert new_command == 'name add --force'

# Generated at 2022-06-14 09:59:54.933804
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_add_without_f_option import get_new_command

    assert(get_new_command(Command('git add foo', 'Use -f if you really want to add them.')) == 'git add --force foo')
    assert(get_new_command(Command('git add foo --bar', 'Use -f if you really want to add them.')) == 'git add --bar --force foo')

# Generated at 2022-06-14 09:59:59.352251
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('git add foobar/', 'fatal: Pathspec \'foobar/\' is in submodule \'bar\'\nUse -f if you really want to add them.')
    assert get_new_command(cmd) == 'git add --force foobar/'

# Generated at 2022-06-14 10:00:02.263759
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add test.py', 'The following paths are ignored')
    new_command = get_new_command(command)
    assert new_command == 'git add --force test.py'

# Generated at 2022-06-14 10:00:11.598104
# Unit test for function match
def test_match():
    assert match(
        Command("git add . && git commit -m 'foo'",
                "fatal: LsWildcard: expanding file names would overwrite files in use in",
                "/usr/home/foo"))

    assert not match(
        Command("git add . && git commit -m 'foo'",
                "fatal: Expand wildcards would overwrite files in use in",
                "/usr/home/foo"))

    assert not match(
        Command("git add . ",
                "fatal: Expand wildcards would overwrite files in use in",
                "/usr/home/foo"))


# Generated at 2022-06-14 10:00:16.438745
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_add import get_new_command
    assert get_new_command(Command('git add test.py', '', 'The following paths are ignored by one of your .gitignore files...')) == "git add --force test.py"

# Generated at 2022-06-14 10:00:20.280931
# Unit test for function get_new_command
def test_get_new_command():
    output = "The following paths are ignored by one of your .gitignore files:"
    cmd = "git add ."
    assert get_new_command(Command(cmd, output)) == "git add --force ."


enabled_by_default = True

# Generated at 2022-06-14 10:01:57.403976
# Unit test for function match
def test_match():
    """test_match():
    If a command returns a message that the 
    following files are in the .gitignore
    the function should return True
    """
    # Arrange
    from thefuck.types import Command

    # Act