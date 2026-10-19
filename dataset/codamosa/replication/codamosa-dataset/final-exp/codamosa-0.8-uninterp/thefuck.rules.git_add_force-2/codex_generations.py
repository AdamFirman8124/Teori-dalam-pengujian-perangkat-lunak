

# Generated at 2022-06-14 09:52:05.996096
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .', 'error: The following untracked working tree files would be overwritten by merge:\n\tfile1\n\tfile2\n\tfile3\n\tfile4\n\tfile5\n\tfile6\n\tfile7\n\tfile8\n\tfile9\n\tfile10\n\tfile11\n\tfile12\n\tfile13\n\tfile14\n\tfile15\n\tfile16\n\tfile17\n\tfile18\nPlease move or remove them before you can merge.\nAborting\n', '')) == 'git add --force .'

# Generated at 2022-06-14 09:52:10.211088
# Unit test for function get_new_command
def test_get_new_command():
    # Create test command object
    command = Command('add -A', 'Use -f if you really want to add them.')

    # Test the output of get_new_command
    assert(get_new_command(command) == 'git add --force -A')




# Generated at 2022-06-14 09:52:12.863046
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt', 'Use -f if you really want to add them.'))
    assert match(Command('git add file.txt', 'hello world')) == False


# Generated at 2022-06-14 09:52:16.175737
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add .')) == 'git add --force .'
    assert get_new_command(Command('git add file.txt')) == 'git add --force file.txt'
    assert get_new_command(Command('git add . --ignore-errors')) == 'git add --force . --ignore-errors'

# Generated at 2022-06-14 09:52:18.649839
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add file', '', None)
    assert get_new_command(command) == 'git add --force file'

# Generated at 2022-06-14 09:52:24.557121
# Unit test for function match
def test_match():
    assert match(Command('git add file',
                         stderr='The following paths are ignored by one of '
                                'your .gitignore files:\nfile\n'
                                'Use -f if you really want to add them.'))
    assert not match(Command('git add file',
                             stderr='The following paths are ignored by one '
                                    'of your .gitignore files:\nfile'))

# Generated at 2022-06-14 09:52:31.051212
# Unit test for function match
def test_match():
    assert not match(Command())
    assert match(Command('git add', output='Use -f if you really want to add them.'))
    assert match(Command('git add -e'))
    assert match(Command('git add --edit'))
    assert not match(Command('git add -a', output='Use -f if you really want to add them.'))
    assert not match(Command('git add --all', output='Use -f if you really want to add them.'))
    assert not match(Command('git add --all -e', output='Use -f if you really want to add them.'))
    assert not match(Command('git add --all --edit', output='Use -f if you really want to add them.'))


# Generated at 2022-06-14 09:52:35.632738
# Unit test for function match
def test_match():
    assert match(Command('git stash', stderr="fatal: Pathspec 'setup.cfg' is in submodule '.'",))
    assert match(Command('git stash', stderr="fatal: Pathspec 'setup.cfg' is in submodule '.'",))

# Generated at 2022-06-14 09:52:36.733948
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add', '', '/Desktop')
    new_command = get_new_command(command)
    assert new_command == 'git add --force'

# Generated at 2022-06-14 09:52:40.394073
# Unit test for function match
def test_match():
    assert match(Command('git add', 'Use -f if you really want to add them.'))
    assert not match(Command('git add', 'Error: Not a git repo'))
    assert not match(Command('git add', ''))



# Generated at 2022-06-14 09:52:46.352228
# Unit test for function match
def test_match():
    assert match('git add file1.py file2.py')
    assert match('git add file1.py file2.py file3.txt')
    assert match('git add file1.py file2.py file3.mp3')
    assert not match('git add -f file1.py')


# Generated at 2022-06-14 09:52:48.807570
# Unit test for function match
def test_match():
    assert match(Command('git add fileA fileB', "fatal: pathspec 'fileA' did not match any files\nUse -f if you really want to add them.\n"))


# Generated at 2022-06-14 09:52:52.025519
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert_equals(get_new_command(Command('git add')), 'git add --force')
    assert_equals(get_new_command(Command('git add')), 'git add --force')

# Generated at 2022-06-14 09:52:59.746433
# Unit test for function match
def test_match():
    assert match(Command('git add --all',
    'The following paths are ignored by one of your .gitignore files:\n'
    'data/t10k-images-idx3-ubyte\nUse -f if you really want to add them.\nfatal: no files added')) is True
    assert match(Command('git add --all', 'fatal: no files added')) is False
    assert match(Command('', '')) is False


# Generated at 2022-06-14 09:53:04.300365
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add file.txt', 'The following paths are ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.')) == 'git add --force file.txt'


# Generated at 2022-06-14 09:53:06.782218
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git add file',
                                   output='Use -f if you really want to add them.')) == 'git add --force file'

# Generated at 2022-06-14 09:53:12.179934
# Unit test for function match
def test_match():
    command = Command('git add *', 'add/path/to/file: No such file or directory\n'
        'Use -f if you really want to add them.')
    assert match(command)



# Generated at 2022-06-14 09:53:14.284654
# Unit test for function get_new_command
def test_get_new_command():
    assert git.get_new_command('git add "testing.txt"') == 'git add --force "testing.txt"'

# Generated at 2022-06-14 09:53:21.134870
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('fuck git add', 'error: The following untracked working tree files would be overwritten by merge:\n\teasy/to/forget.txt\n\tplease/add/them.txt\n\tmanually/add/them.txt\n\nPlease move or remove them before you can merge.\nAborting\n')
    assert 'git add --force' == get_new_command(command)


# Generated at 2022-06-14 09:53:24.549498
# Unit test for function get_new_command
def test_get_new_command():
    assert (
        get_new_command(Command('git add file.txt', '',
                                '/root/file.txt: needs merge\nUse -f if you really want to add them.'))
        == 'git add --force file.txt')
    assert (
        get_new_command(Command('./file.sh test', '',
                                '/root/file.txt: needs merge\nUse -f if you really want to add them.'))
        == './file.sh --force test')



# Generated at 2022-06-14 09:53:36.079790
# Unit test for function match
def test_match():
    assert match(Command('git rm non_existent_file',
                   'fatal: pathspec \'non_existent_file\' did not match any files\n',
                   ''))
    assert not match(Command('echo $PATH',
                     '(in /usr/local/bin)\n',
                     ''))
    assert match(Command('git add a b c d e',
                     'Use -f if you really want to add them.\n',
                     ''))

# Generated at 2022-06-14 09:53:41.501937
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add file1 file2', 'The following paths are ignored by one of your .gitignore files:\n file1\n file2\nUse -f if you really want to add them.\n')
    assert get_new_command(command) == "git add --force file1 file2"

# Generated at 2022-06-14 09:53:44.271629
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('git add file.txt')
    assert get_new_command(cmd) == 'git add --force file.txt'

# Generated at 2022-06-14 09:53:50.425663
# Unit test for function match
def test_match():
	output1="""
	error: The following untracked working tree files would be overwritten by merge:
		path/to/file
		path2/to/file2
	Please move or remove them before you can merge.
	Aborting
	"""
	output2="""
	error: The following untracked working tree files would be overwritten by merge:
		path/to/file
		path2/to/file2
	Please move or remove them before you can merge.
	"""
	assert match(Command('git add path/to/file', output1))
	assert match(Command('git add path2/to/file2', output2))
	assert not match(Command('git checkout master', ''))
	assert not match(Command('git merge origin/master', ''))

# Generated at 2022-06-14 09:53:54.579956
# Unit test for function match
def test_match():
    command = Command('git add src/test.py', 'fatal: pathspec \'src/test.py\' did not match any files\nUse -f if you really want to add them.')
    assert match(command)



# Generated at 2022-06-14 09:53:56.300491
# Unit test for function get_new_command
def test_get_new_command():
    output = 'Use -f if you really want to add them.'
    command = Command('git add .', output=output)
    assert get_new_command(command) == 'git add --force .'

# Generated at 2022-06-14 09:54:07.763172
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         "use 'git add <file>...' to update what will be committed\n"
                         "use 'git checkout -- <file>...' to discard changes in working directory\n"
                         '\n'
                         'Changes not staged for commit:\n'
                         '  modified:   .gitignore\n'
                         '\n'
                         'no changes added to commit (use "git add" and/or "git commit -a")'))
    assert not match(Command('git add', ''))


# Generated at 2022-06-14 09:54:19.703813
# Unit test for function get_new_command
def test_get_new_command():
    output = ('error: The following untracked working tree files would be'
              ' overwritten by merge: a b c\n'
              'Please move or remove them before you can merge.\n'
              'Aborting')
    assert get_new_command(
        Command('git add a b c', output=output)) == 'git add --force a b c'
    assert get_new_command(
        Command('git add a b c', output='Use -f if you really want to add them.')) == 'git add --force a b c'
    assert get_new_command(
        Command('git add a b c', output='fail')) == 'git add a b c'

# Generated at 2022-06-14 09:54:29.788946
# Unit test for function match
def test_match():
    assert match(Command('git add --ignore-removal .',
                         'fatal: The following untracked working tree files would be overwritten by merge:\n'
                         '        file1\n'
                         '        file2\n'
                         '        file3\n'
                         '        file4\n'
                         'Please move or remove them before you can merge.\n'
                         'Aborting',
                         None))
    assert match(Command('git add .',
                         'fatal: The following untracked working tree files would be overwritten by merge:\n'
                         '        file1\n'
                         '        file2\n'
                         '        file3\n'
                         '        file4\n'
                         'Please move or remove them before you can merge.\n'
                         'Aborting',
                         None))

# Generated at 2022-06-14 09:54:37.603046
# Unit test for function match
def test_match():
    assert match(create_command('git add', 'fatal: not a git repository')) == False
    assert match(create_command('git add', 'fatal: not a git repository (or any of the parent directories): .git', True)) == False
    assert match(create_command('git add', 'Use -f if you really want to add them.')) == True
    assert match(create_command('git add', 'whatever')) == False


# Generated at 2022-06-14 09:54:45.562914
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add -A', '''The following paths are ignored by one of your .gitignore files:
    foo/bar
    Use -f if you really want to add them.''')
    assert get_new_command(command) == 'git add --force -A'

# Generated at 2022-06-14 09:54:50.046123
# Unit test for function match
def test_match():
    assert match(Command('git add .', '', ''))
    assert not match(Command('git add .', '', 'Use -f if you really want to add them.\nAborting'))


# Generated at 2022-06-14 09:54:54.842101
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'Use -f if you really want to add them.'))
    assert not match(Command('git ad .', 'Use -f if you really want to add them.'))
    assert not match(Command('git add .', 'Use -f if you really want to add them.', 'git'))


# Generated at 2022-06-14 09:55:02.130009
# Unit test for function match
def test_match():
	# check if is not git
	assert(match(Command("something")) == None)
	# check if is not add
	assert(match(Command("git add", "git: 'add' is not a git command. See 'git --help'.")) == None)
	# check if there is no error
	assert(match(Command("git add", "some error")) == False)
	# check if there is no error and there is add
	assert(match(Command("git add", "fatal: some error")) == False)
	# check if there is not error and there is add
	assert(match(Command("git add", "use -f if you really want to add them.")) == True)
	# check if there is error and there is add

# Generated at 2022-06-14 09:55:05.987533
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add file.log', 'fatal: pathspec \'file.log\' did not match any files\nUse -f if you really want to add them.')) == 'git add --force file.log'


# Generated at 2022-06-14 09:55:10.230764
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add *', 'fatal: Pathspec \'*\' is in submodule \'src/mongoose\'')
    assert get_new_command(command).script == 'git add --force *'


# Generated at 2022-06-14 09:55:13.792013
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add file1 file2 file3', "fatal: pathspec 'file1' did not match any files\nUse -f if you really want to add them.\n")) == 'git add --force file1 file2 file3'

# Generated at 2022-06-14 09:55:25.237081
# Unit test for function match
def test_match():
    assert match(Command(script = "git add .",
                         stderr = "The following paths are ignored by one of your .gitignore files:\n.DS_Store\nUse -f if you really want to add them.\nfatal: no files added\n"))
    assert match(Command(script = "git add .",
                         stderr = "The following paths are ignored by one of your .gitignore files:\nmyenv/bin/\nmyenv/include/\nmyenv/lib/\nmyenv/lib64/\nmyenv/man/\nmyenv/share/\nUse -f if you really want to add them.\nfatal: no files added\n"))


# Generated at 2022-06-14 09:55:28.135212
# Unit test for function match
def test_match():
    assert match(Command("git add \"file1.txt\" \"file2.txt\"",
    "fatal: LF would be replaced by CRLF in file1.txt"))



# Generated at 2022-06-14 09:55:35.885534
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('git add sssssss',
                                   'error: The following untracked working tree files would be overwritten by merge:\n\t"1.txt"\n\t"3.txt"\n\t"aaa"\nPlease move or remove them before you can merge.\nAborting\n',
                                   'git add')) == 'git add --force sssssss'

# Generated at 2022-06-14 09:55:48.119376
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt', stderr='''\
error: The following untracked working tree files would be overwritten by merge:
    file.txt
    file2.txt
    file3.txt
Please move or remove them before you can merge.
Aborting
'''))
    assert not match(Command('git add .', stderr='''\
error: The following untracked working tree files would be overwritten by merge:
    file.txt
    file2.txt
    file3.txt
Please move or remove them before you can merge.
Aborting
'''))


# Generated at 2022-06-14 09:55:53.415951
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('git add README.txt',
                'fatal: Pathspec \'filename with spaces\' is in submodule \'my submodule\'\n'
                'Use -f if you really want to add them.\n')) == \
                'git add --force README.txt'

# Generated at 2022-06-14 09:55:58.760703
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .',
                      'error: '
                      'The following untracked working tree files would be '
                      'overwritten by merge:\n'
                      '	src/README.md\n'
                      'Please move or remove them before you can merge.\n'
                      'Aborting')
    assert get_new_command(command) == 'git add --force .'

# Generated at 2022-06-14 09:56:02.935316
# Unit test for function match
def test_match():
    assert match(Command('git add foo',
                         "The following paths are ignored by one of your .gitignore files:`foo'.*Use -f if you really want to add them.",
                         ""))
    assert not match(Command('git add foo',
                             'The following paths are ignored by one of your .gitignore files.*',
                             ""))



# Generated at 2022-06-14 09:56:12.982658
# Unit test for function get_new_command
def test_get_new_command():
	import shlex
	command = shlex.split('~/test/test$ git add .')
	output = 'error: The following untracked working tree files would be overwritten by merge:\n\
			.gitignore\n\
			adir/\n\
			a.c\n\
			b.c\n\
			Please move or remove them before you can merge.\n\
			Aborting'
	command_s = Command(command, output)
	new_command = get_new_command(command_s)
	assert new_command == 'git add --force .'

# Generated at 2022-06-14 09:56:18.238107
# Unit test for function match
def test_match():
    assert match(Command('git add ', 'The following paths are ignored by one of your .gitignore files:\n.git-rewrite/\nUse -f if you really want to add them.'))
    assert not match(Command('git add README.md', ''))


# Generated at 2022-06-14 09:56:25.915383
# Unit test for function match
def test_match():
    # Unit test for function match
    assert match(Command('git add file.txt',
                   'error: The following untracked working tree files would be overwritten by merge:\nfile.txt\nPlease move or remove them before you can merge.\nAborting'))
    assert match(Command('git add file.txt',
                         'error: The following path is ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.'))
    assert match(Command('git add file.txt',
                         'fatal: Pathspec \'file.txt\' is in submodule \'vendor/bundle/ruby/1.9.1/bundler/gems/rack-0750cbd268f9\' and cannot be added.'))

# Generated at 2022-06-14 09:56:30.223407
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add dir', 'fatal: Pathspec \'dir\' is in submodule \'core/assets/js\'\nUse -f if you really want to add them.\n')
    assert get_new_command(command) == 'git add --force dir'

# Generated at 2022-06-14 09:56:34.724891
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                   'The following paths are ignored by one of your .gitignore files:\n'
                   'repository/ignored_file\n'
                   'Use -f if you really want to add them.\n'
                   'fatal: no files added',
                   ''))
    assert not match(Command('git init', '', ''))


# Generated at 2022-06-14 09:56:43.034149
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add app.py', stderr='''The following untracked working tree files would be overwritten by merge:
        app.py
        Use -f if you really want to add them.''')) == 'git add --force app.py'

# Generated at 2022-06-14 09:56:55.704360
# Unit test for function match
def test_match():
    assert match(Command('git add foo bar baz',
                         'fatal: Pathspec \'foo\' is in submodule \'baz\'.\n'
                         'fatal: Pathspec \'bar\' is in submodule \'baz\'.\n'
                         'Use -f if you really want to add them.'))


# Generated at 2022-06-14 09:56:57.842477
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add'), 'git add', 'git add --force')


# Generated at 2022-06-14 09:57:02.505142
# Unit test for function match
def test_match():
    assert match(Command('git add test.txt', '', 'test.txt: '.format(u'\u2717', u'\u2713')))
    assert not match(Command('ls -l', '', ''))



# Generated at 2022-06-14 09:57:06.237028
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'Use -f if you really want to add them.'))
    assert not match(Command('git add .', ''))
    assert not match(Command('git init', ''))



# Generated at 2022-06-14 09:57:10.286704
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add --all', 'Use -f if you really want to add them.')
    assert (get_new_command(command) == u'git add --all --force')

# Generated at 2022-06-14 09:57:16.902651
# Unit test for function get_new_command
def test_get_new_command():
    function_script = 'git add .gitignore'
    function_output = 'fatal: Pathspec \' .gitignore\' is in submodule \' .gitignore\'.\nUse --ignore-submodules to ignore'
    assert get_new_command(Command(script=function_script, output=function_output)) == 'git add --force .gitignore'

# Generated at 2022-06-14 09:57:22.360629
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt', '', ''))
    assert match(Command('git add file.txt', 'error: pathspec', ''))
    assert not match(Command('git add file.txt', '', 'pathspec'))
    assert not match(Command('', '', 'pathspec'))


# Generated at 2022-06-14 09:57:28.464664
# Unit test for function match
def test_match():
    import os
    cur_dir = os.getcwd()
    os.chdir("test_repo")
    assert match("git add file.txt")
    assert not match("git add --force file.txt")
    assert not match("git adda file.txt")
    os.chdir(cur_dir)


# Generated at 2022-06-14 09:57:31.908658
# Unit test for function match
def test_match():
    assert match(Command('git add file', 
					"The following paths are ignored by one of your .gitignore files:\nfile\nUse -f if you really want to add them."))


# Generated at 2022-06-14 09:57:40.892559
# Unit test for function match

# Generated at 2022-06-14 09:58:03.792396
# Unit test for function match
def test_match():
    # If script contains 'add' and output contains 'Use -f if you really want to add them'
    # then it should return True, otherwise it should return False
    assert match(
        Command('git add',
                output='error: The following untracked working tree files would be overwritten by merge:\n'
                       '\tfilename\n'
                       'Please move or remove them before you can merge.\n'
                       'Aborting\n'))
    assert not match(Command('git add', output='No untracked files found'))


# Generated at 2022-06-14 09:58:14.570251
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                'Use "git add <file>..." to update what will be committed.'))
    assert match(Command('git add .',
                'Use "git add <file>..." to update what will be committed.' +
                '\nUse -f if you really want to add them.'))
    assert not match(Command('git add --force .',
                    'Use "git add <file>..." to update what will be committed.'))
    assert not match(Command('git add ?',
                    'Use "git add <file>..." to update what will be committed.'
                    '\nUse -f if you really want to add them.'))

# Generated at 2022-06-14 09:58:18.996518
# Unit test for function match
def test_match():
    assert match(Command('git add file1'
                         ' >> fatal: Pathspec \'file1\' is in submodule \'thefuck\''
                         ' >> Use --force if you really want to add it.',
                         '', 0))
    assert not match(Command('git add file1', '', 0))


# Generated at 2022-06-14 09:58:26.660046
# Unit test for function get_new_command
def test_get_new_command():
    #Unit test for command 'git add -A myfile'
    command = Command(script = 'git add -A myfile',
                      output = 'fatal: pathspec \'myfile\' did not match any files\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add --force -A myfile'

    #Unit test for command 'git add myfile'
    command = Command(script = 'git add myfile',
                      output = 'fatal: pathspec \'myfile\' did not match any files\nUse -f if you really want to add them.')
    assert get_new_command(command) == 'git add --force myfile'

    #Unit test for command 'git add .'

# Generated at 2022-06-14 09:58:29.722308
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add dir/file.txt', output='file.txt: needs merge')
    assert get_new_command(command) == 'git add --force dir/file.txt'

# Generated at 2022-06-14 09:58:41.763332
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt',
                         'error: The following untracked working tree files would be overwritten by merge:\nfile.txt\n'
                         'Please move or remove them before you can merge.\n')
                 ) is True
    assert match(Command('git add file.txt',
                         'error: The following untracked working tree files would be overwritten by merge:\nfile.txt\n'
                         'Please move or remove them before you can merge.\n'
                         'Aborting\n')
                 ) is False
    assert match(Command('git add file.txt',
                         'error: The following untracked working tree files would be overwritten by merge:\nfile.txt\n'
                         'Please move or remove them before you can merge.\n'
                         'Aborting\n')
                 ) is False


# Generated at 2022-06-14 09:58:54.204597
# Unit test for function get_new_command

# Generated at 2022-06-14 09:59:00.380187
# Unit test for function match
def test_match():
    assert match(Command('git add .',
                         stderr='error: The following untracked working tree files would be overwritten by merge:\n'
                                'test\n'
                                'Please move or remove them before you can merge.\n'
                                'Aborting\n'
                                'Use -f if you really want to add them.'))
    assert not match(Command('git add .',
                             stderr='error: The following untracked working tree files would be overwritten by merge:\n'
                                    'test\n'
                                    'Please move or remove them before you can merge.\n'
                                    'Aborting\n'
                                    'Use -f if you really want to add them.'))


# Generated at 2022-06-14 09:59:10.075401
# Unit test for function match
def test_match():
    # If there is 'add' and 'Use -f if you really want to add them.' in script
    assert match(Command(script='git add .'))
    assert match(Command(script='git add --all'))
    # If there is 'add' but not 'Use -f if you really want to add them.' in script
    assert not match(Command(script='git add .',
                             output='It is now empty, nothing added.'))
    # If there is not 'add' in script
    assert not match(Command(script='git commit -am "message"'))


# Generated at 2022-06-14 09:59:16.836154
# Unit test for function get_new_command
def test_get_new_command():
    # Test on a real command example
    assert get_new_command(
        Command(script='git add',
                stderr='error: The following paths are ignored by one of your .gitignore files:\n'
                       'src/test.txt\n'
                       'Use -f if you really want to add them.\n')) == 'git add --force'

# Generated at 2022-06-14 09:59:46.617081
# Unit test for function match
def test_match():
    assert match('git add filename.py')
    assert match('git add filename.py --force')


# Generated at 2022-06-14 09:59:53.847242
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add src/File.txt')
    command.output = 'The following paths are ignored by one of your .gitignore files:\nsrc/File.txt\nUse -f if you really want to add them.\nfatal: no files added'
    assert get_new_command(command) == 'git add --force src/File.txt'


# Generated at 2022-06-14 10:00:03.583282
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .', 'fatal: Pathspec \'24\' is in submodule \'24\'\n'
                                  'Use --force if you really want to add '
                                  'it.\n'
                                  'Did you forget to \'git add\'?')
    assert get_new_command(command) == 'git add . --force'

    command = Command('git add *', 'error: The following path is ignored by '
                                   'one of your .gitignore files:\n'
                                   'package-lock.json\n'
                                   'Use -f if you really want to add it.\n'
                                   'Add this to the ignore list?')
    assert get_new_command(command) == 'git add * -f'


# Generated at 2022-06-14 10:00:16.216066
# Unit test for function match
def test_match():
    assert git.match(Command(script= 'git add /var/log'))
    assert git.match(Command(script='git add /var/log',
                             output='Use -f if you really want to add them.'))
    assert not git.match(Command(script='git add /var/log',
                                 output='Use -f if you really want to add them'))
    assert not git.match(Command(script='git add /var/log',
                                 output='Use -f if you really want to add them',
                                 stderr='Add some error'))
    assert not git.match(Command(script= 'git add /var/log', output='Use -f if you really want to add them',
                                 stderr='Add some error',))

# Generated at 2022-06-14 10:00:21.978875
# Unit test for function match
def test_match():
    assert match(Command('git add .', '', '', '', ''))
    assert match(Command('git add', 'error: The following untracked working tree files would be overwritten by merge:\ngit.txt\nPlease move or remove them before you can merge.\nAborting', '', '', ''))
    assert not match(Command('git add .', '', '', '', ''))


# Generated at 2022-06-14 10:00:26.041472
# Unit test for function match
def test_match():
    assert match(Command('git add ', 'Use -f if you really want to add them.'))
    assert not match(Command('git remote add origin git@github.com:nvbn/thefuck.git', ''))


# Generated at 2022-06-14 10:00:40.602435
# Unit test for function match
def test_match():
    # This command has correct syntax and correct git
    assert match(Command('git add file1',
                         'The following paths are ignored by one of your '.split()
                         + ['.', 'patterns', ':', 'file1', 'Use', '-f']
                         + ['.', 'if', 'you', 'really', 'want', 'to', 'add', 'them', '.']))
    # This command has correct syntax, but output is not as expected
    assert not match(Command('git add file1', ''))
    # This command has incorrect syntax

# Generated at 2022-06-14 10:00:44.429007
# Unit test for function match
def test_match():
    assert match(Script('git add *.py', 'fatal: LF would be replaced by CRLF in Makefile'))
    assert not match(Script('git add file.py', ''))
    assert not match(Script('git commit -m "Static analysis"', ''))

# Generated at 2022-06-14 10:00:55.634539
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         stderr=(
                         'The following paths are ignored by one of your .gitignore files:\n'
                         'vendor/bundle\n'
                         'Use -f if you really want to add them.\n'
                         'fatal: no files added\n')))
    assert match(Command('git add vendor/bundle',
                         'The following paths are ignored by one of your .gitignore files:\n'
                         'vendor/bundle\n'
                         'Use -f if you really want to add them.\n'
                         'fatal: no files added\n'))
    assert not match(Command('git add'))


# Generated at 2022-06-14 10:00:59.092829
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', '', 'Use -f if you really want to add them.')) == 'git add --force'

# Generated at 2022-06-14 10:01:43.433089
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt',
                         stderr='fatal: not a git repository '
                                '(or any of the parent directories): .git\n'))
    assert match(Command('git add file.txt',
                         stderr='fatal: bad revision \'HEAD^\'\n'))
    assert match(Command('git add sdfsdfsdf',
                         stderr='fatal: pathspec \'sdfsdfsdf\' did not match any files\n'))
    assert not match(Command('git add',
                             stderr='usage: git add [<options>] [--] <pathspec>...\n'))

# Generated at 2022-06-14 10:01:52.859908
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add *.txt',
                      'fatal: Pathspec \'*.txt\' is in submodule \'folder\'\n'
                      'Use \'git add <pathspec>\' to explicitly remove '
                      '\'<pathspec>\' if you really want to add it.\n'
                      'Use -f if you really want to add them.')
    assert get_new_command(command) == 'git add --force *.txt'


enabled_by_default = True

# Generated at 2022-06-14 10:01:57.726438
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        "git add --ignore-errors non-existent.txt",
        "fatal: pathspec 'non-existent.txt' did not match any files\nUse -f if you really want to add them.") == "git add --force --ignore-errors non-existent.txt"