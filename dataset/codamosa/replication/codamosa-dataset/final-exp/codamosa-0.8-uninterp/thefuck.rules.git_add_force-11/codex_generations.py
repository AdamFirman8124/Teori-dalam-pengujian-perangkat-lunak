

# Generated at 2022-06-14 09:51:51.299822
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add remote', "fatal: Path 'remote' is in submodule 'sub/subsub'")) == 'git add --force remote'


# Generated at 2022-06-14 09:51:55.795387
# Unit test for function match
def test_match():
    """
    Test that the match returns true when it succeeds and false when
    it fails
    """

    assert(match(Command("git add .", "fatal: Path 'lib/' is in submodule 'lib'")))
    assert(not match(Command("git add .", "")))

# Generated at 2022-06-14 09:52:00.679746
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git add file", ["git", "add", "file"]) == "git add --force file"
    assert get_new_command("git add -A", ["git", "add", "-A"]) == "git add --force -A"

# Generated at 2022-06-14 09:52:05.691486
# Unit test for function match
def test_match():
    assert match(Command('git add .', '', 'error: The following untracked working tree files would be overwritten by merge:\n...\nUse -f if you really want to add them.'))
    assert not match(Command('git add .', '', 'error'))
    assert not match(Command('ls', '', ''))


# Generated at 2022-06-14 09:52:14.284064
# Unit test for function match
def test_match():
    assert match(Command('git add /git/file1 /git/file2', '', 'fatal: Not a git repository (or any of the parent directories): .git\nUse -f if you really want to add them.'))
    assert not match(Command('git add /git/file1 /git/file2', '', 'Error: /git/file1\nError: /git/file2'))
    assert not match(Command('git mv /git/file1 /git/file2', '', 'fatal: Not a git repository (or any of the parent directories): .git\nUse -f if you really want to add them.'))

# Generated at 2022-06-14 09:52:18.419801
# Unit test for function match
def test_match():
    assert match(Command("git add a b c d/e.txt",
                         "error: 'a' is ignored in .gitignore and cannot be specified on the command line. "
                         "Use -f if you really want to add them.\nfatal: bad pathspec 'b'"))
    assert not match(Command("git add a b c d/e.txt", ""))
    assert not match(Command("git add", ""))
    assert not match(Command("git branch", ""))


# Generated at 2022-06-14 09:52:21.938004
# Unit test for function match
def test_match():
    assert_true(match("git add ."))
    assert_true(match("git add ."))
    assert_false(match("git add"))
    assert_false(match("git diff"))


# Generated at 2022-06-14 09:52:25.044445
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('git add', ('Use -f if you really want to add them.', ''), '', ''))
            == ['git', 'add', '--force'])



# Generated at 2022-06-14 09:52:29.501935
# Unit test for function match
def test_match():
    assert match(Command('git add file1 file2 file3',
                         'fatal: Pathspec \'file2\' is in submodule \'sub\'\nUse --force if you really want to add them.'))
    assert not match(Command('git add file1 file2 file3',
                             'fatal: pathspec \'file2\' is in submodule \'sub\''))
    assert not match(Command('git add file1 file2 file3'))


# Generated at 2022-06-14 09:52:35.995420
# Unit test for function match
def test_match():
    assert_match(match, 'git add  .')
    assert_match(match, 'git add .')
    assert_match(match, 'git add -f .')
    assert_match(match, 'git add --force .')
    assert_match(match, 'git add -f --force .')
    assert_not_match(match, 'git add --force  .')


# Generated at 2022-06-14 09:52:41.821786
# Unit test for function match
def test_match():
    assert match(Command('git add . -m commit_message',
                         "The following paths are ignored by one of your .gitignore files:\n\
foo\n\
Use -f if you really want to add them.\n\
fatal: no files added\n"))



# Generated at 2022-06-14 09:52:50.724230
# Unit test for function match
def test_match():
    command = 'git add .'
    result = match(Command(script=command, output='git: Use -f if you really want to add them.'))
    assert result == True

    command = 'git commit'
    result = match(Command(script=command, output='git: Use -f if you really want to add them.'))
    assert result == False

    command = 'git add .'
    result = match(Command(script=command, output='git: Use -f if you really want to add them.'))
    assert result == True

    command = 'git add .'
    result = match(Command(script=command, output='git: Use -f if you really want to add them.'))
    assert result == True


# Generated at 2022-06-14 09:52:57.667512
# Unit test for function match
def test_match():
    assert match(Command('git add src/config.py', 'fatal: Path \'src/config.py\' is in submodule \'src\'.\nUse --force to continue.'))
    assert not match(Command('git add src/config.py', ''))
    assert not match(Command('ls', 'fatal: Path \'src/config.py\' is in submodule \'src\'.\nUse --force to continue.'))


# Generated at 2022-06-14 09:53:03.694741
# Unit test for function match
def test_match():
    assert match(Command('git add abc', 'fatal: Pathspec \'abc\' is in submodule \'def\'\nUse -f if you really want to add them.'))
    assert not match(Command('git branch abc', 'fatal: Pathspec \'abc\' is in submodule \'def\'\nUse -f if you really want to add them.'))


# Generated at 2022-06-14 09:53:10.558390
# Unit test for function match
def test_match():
    # Test case 1: input = git add foo.py
    #              output = The following paths are ignored by one of your .gitignore files:
    #                        foo.py
    #                        Use -f if you really want to add them.
    cmd1 = Command('git add foo.py', None, 'The following paths are ignored by one of your .gitignore files:\nfoo.py\nUse -f if you really want to add them.')
    assert match(cmd1)

    # Test case 2: input = git add --force foo.py
    #              output = The following paths are ignored by one of your .gitignore files:
    #                        foo.py
    #                        Use -f if you really want to add them.

# Generated at 2022-06-14 09:53:22.086340
# Unit test for function match
def test_match():
    # Test returning positive if output contains specific string
    assert match(Command('git add', 'The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.'))
    assert match(Command('git add', 'hello\nThe following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.'))
    # Test returning negative if output does not contain specific string
    assert not match(Command('git add', 'hello\nThe following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.\nworld'))
    assert not match(Command('git add', 'The following paths are not ignored by one of your .gitignore files:\nUse -f if you really want to add them.'))


# Generated at 2022-06-14 09:53:34.135431
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add foo bar',
              '/usr/bin/git add foo bar\n'
              'The following paths are ignored by one of your .gitignore files:\n'
              'bar\n'
              'Use -f if you really want to add them.\n'
              'fatal: no files added',
              'git')
    assert get_new_command(command) == 'git add --force foo bar'

# Generated at 2022-06-14 09:53:46.557863
# Unit test for function match
def test_match():
    assert(match(Command('git add', '', '')))
    assert(match(Command('git add BADGER', '', '')))
    assert(match(Command('git add BADGER', 'Use -f if you really want to add them.')))
    assert(match(Command('git add .', '', '')))
    assert(match(Command('git add .', 'Use -f if you really want to add them.')))
    assert(match(Command('git add -A', '', '')))
    assert(match(Command('git add -A', 'Use -f if you really want to add them.')))
    assert(match(Command('git add BADGER BADGER', 'Use -f if you really want to add them.')))
    assert(match(Command('git add BADGER BADGER', '', '')))

# Generated at 2022-06-14 09:53:52.141968
# Unit test for function match
def test_match():
    assert match(Command('git add README', 'error: The following untracked working tree files would be overwritten by merge:\n        README\nPlease move or remove them before you merge.')) is True
    assert match(Command('git add README', '')) is False

# Generated at 2022-06-14 09:53:57.618610
# Unit test for function get_new_command
def test_get_new_command():
    success_command = Command('git add .', 'Use -f if you really want to add them.')
    failure_command = Command('git add .', 'Some other error message')
    assert(get_new_command(success_command) == "git add --force .")
    assert(get_new_command(failure_command) == None)

# Generated at 2022-06-14 09:54:07.269033
# Unit test for function match
def test_match():
    command1 = Command(None, None, 'add --ignore', None, None, None)
    command2 = Command(None, None, 'add', None, None, 'Use -f if you really want to add them.')
    command3 = Command(None, None, 'commit', None, None, None)

    assert not match(command1)
    assert match(command2)
    assert not match(command3)


# Generated at 2022-06-14 09:54:14.700186
# Unit test for function match
def test_match():
    assert match(Command('git add file.cc',
                         'fatal: pathspec \'file.cc\' did not match any files\n'
                         'Use -f if you really want to add them.'))
    assert not match(Command('git add file.cc', ''))
    assert not match(Command('ls file.cc', ''))


# Generated at 2022-06-14 09:54:21.091197
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        'git add . && git commit -m"first commit"',
        'error: The following untracked working tree files would be overwritten by '
        'merge:\n\tpath1\n\tpath2') == 'git add --force . && git commit -m"first commit"'

# Generated at 2022-06-14 09:54:27.094789
# Unit test for function match
def test_match():
    assert match(Command("git add ."))
    assert match(Command("git add .", "error: The following untracked working tree files would be overwritten by merge:\n    .file_name\n    .file_name2\n    .file_name3\nPlease move or remove them before you can merge.\nAborting"))
    assert not match(Command("git checkout ."))


# Generated at 2022-06-14 09:54:31.016449
# Unit test for function match
def test_match():
    assert match(Command(script='git add .', output='warning: adding embedded git repository:'))
    assert not match(Command(script='git add .', output='fatal: pathspec'))


# Generated at 2022-06-14 09:54:38.580867
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_add_ignore_error import get_new_command
    assert get_new_command('git diff').startswith('git add --force ')
    assert get_new_command('git status').startswith('git add --force ')
    assert get_new_command('git add -A').startswith('git add --force -A')

# Generated at 2022-06-14 09:54:46.121771
# Unit test for function match
def test_match():
    assert match(Command('git add dir1/dir2/',
                         'The following paths are ignored by one of your .gitignore files:\ndir1\nUse -f if you really want to add them.\nfatal: no files added',
                         '/usr/bin/git add dir1/dir2/'))



# Generated at 2022-06-14 09:54:51.962950
# Unit test for function match
def test_match():
    assert match(Command('git add file.txt', 'The following paths are ignored by one of your .gitignore files: file.txt\nUse -f if you really want to add them.\n'))
    assert not match(Command('git add *_local.tfvars', ''))
    assert not match(Command('git add', ''))


# Generated at 2022-06-14 09:54:54.558749
# Unit test for function match
def test_match():
    assert match(Command('git add', '/root/Downloads/file1'))
    assert not match(Command('git add file2', 'some error'))



# Generated at 2022-06-14 09:55:01.950567
# Unit test for function match
def test_match():
	assert_equals(match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\nsrc\nUse -f if you really want to add them.')), True)
	assert_equals(match(Command('git add .', 'The following paths are ignored by one of your .gitignore files:\nsrc/main\nUse -f if you really want to add them.')), True)
	assert_equals(match(Command('git add src', 'The following paths are ignored by one of your .gitignore files:\nsrc\nUse -f if you really want to add them.')), True)
	assert_equals(match(Command('git add src', 'The following paths are ignored by one of your .gitignore files:\nsrc/main\nUse -f if you really want to add them.')), True)
	assert_

# Generated at 2022-06-14 09:55:10.406680
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.specific.git import git_support
    command = Command('git add --all', 'The following paths are ignored by one of your .gitignore files:', 'Use -f if you really want to add them.')
    assert get_new_command(command) == 'git add --all --force'

# Generated at 2022-06-14 09:55:12.738498
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.specific.git import git_support
    assert get_new_command("git add .").script == "git add --force ."

# Generated at 2022-06-14 09:55:20.354430
# Unit test for function match
def test_match():
    assert match(Command('git add file1.txt file2.txt',
                         stderr=('The following paths are ignored by '
                                 'one of your .gitignore files:\n'
                                 'file1.txt\n'
                                 'Use -f if you really want to add them.\n')))
    assert not match(Command('git branch', stderr=''))

# Generated at 2022-06-14 09:55:28.777404
# Unit test for function match
def test_match():
    # Example from the git documentation on how to force the command
    assert match(Command('git add -A',
                         'error: The following untracked working tree files would be overwritten by merge:\n'
                            '\ta.txt\n'
                            'Please move or remove them before you can merge.\n'
                            'Aborting'))
    # Should not match on any other commands
    assert not match(Command('git add', stdout='other'))
    assert not match(Command('git add -A', stdout='other'))
    assert not match(Command('git add .', stdout='other'))



# Generated at 2022-06-14 09:55:37.968778
# Unit test for function match
def test_match():
    assert match(Command('git add .', stderr='error: The following untracked directories were found: ... Use -f if you really want to add them.'))
    assert not match(Command('git add .', stderr='error: The following untracked directories were found: ... Use -f if you really wantn to add them.'))
    assert not match(Command('git add .', stderr='error: The following untracked directories were found: ... Use -f if you really want to add them.', script='git push'))


# Generated at 2022-06-14 09:55:45.316294
# Unit test for function match
def test_match():
    assert match(Command("git status", "", "", "")) == False
    assert match(Command("git add foo bar", "", "", "")) == False
    assert match(Command("git add foo bar baz", "fatal: LF would be replaced by CRLF in baz\n"
                                                 "The file will have its original line endings in your working directory",
                          "", "")) == True


# Generated at 2022-06-14 09:55:56.683545
# Unit test for function match
def test_match():
    assert match(Command('git add file1 file2 file3',
                         'error: pathspec \'file1\' did not match any file(s)\n'
                         'error: pathspec \'file2\' did not match any file(s)\n'
                         'error: pathspec \'file3\' did not match any file(s)\n'
                         'error: pathspec \'file1\' did not match any file(s)\n'
                         'error: pathspec \'file2\' did not match any file(s)\n'
                         'error: pathspec \'file3\' did not match any file(s)\n'
                         'fatal: no files added\nUse -f if you really want to add them.'))
                        

# Generated at 2022-06-14 09:55:59.960858
# Unit test for function get_new_command
def test_get_new_command():
    from .utils import Command

    assert get_new_command(Command('git add .',
                                   output='The following paths are ignored by one of your .gitignore files:\nUse -f if you really want to add them.')) \
        == 'git add --force .'

# Generated at 2022-06-14 09:56:03.409924
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git add'
    output = 'The following paths are ignored by one of your .gitignore files:\n.cproject\nUse -f if you really want to add them.'
    assert get_new_command(command, output) == 'git add --force'

# Generated at 2022-06-14 09:56:10.900197
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', '', '')) == 'git add --force'
    assert get_new_command(Command('git add dir/file.txt', '', '')) == 'git add --force dir/file.txt'
    assert get_new_command(Command('git add file1.txt file2.txt', '', '')) == 'git add --force file1.txt file2.txt'


# Generated at 2022-06-14 09:56:19.096013
# Unit test for function match
def test_match():
    assert not match(Command('git add foo'))
    assert match(Command('git add foo', stderr='The following untracked working tree files would be overwritten by merge:\n\twhatever\nPlease move or remove them before you merge.'))


# Generated at 2022-06-14 09:56:23.795691
# Unit test for function match
def test_match():
    assert match(Command('git stash',
                         "fatal: pathspec 'my-branch-name' did not match any files\nUse -f if you really want to add them."))
    assert not match(Command('git stash', 'No local changes to save'))


# Generated at 2022-06-14 09:56:27.186752
# Unit test for function match
def test_match():
    assert match(Command('git add file1 file2 ', 'fatal: pathspec \'file1 file2 \' did not match any files\nUse -f if you really want to add them.'))
    assert match(Command('git add file1 file2 ', '')) == False

# Generated at 2022-06-14 09:56:34.580845
# Unit test for function match
def test_match():
    assert match(Command('git add test.txt',
                         stderr='error: The following untracked working tree '
                                'files would be overwritten by merge:\n'
                                'test.txt\n'
                                'Please move or remove them before you can merge.'))
    assert not match(Command('git add',
                             stderr='error: The following untracked working tree files would be overwritten by merge:\n'
                                    'test.txt\n'
                                    'Please move or remove them before you can merge.'))

# Unit test function get_new_command

# Generated at 2022-06-14 09:56:48.164636
# Unit test for function match
def test_match():
    assert not match(Command(script = 'git commit -m "Test"'))
    assert match(Command(script = 'git add file.txt',
                         output = 'Use -f if you really want to add them.'))
    assert not match(Command(script = 'git add .',
                             output = 'Use -f if you really want to add them.'))
    assert not match(Command(script = 'git add file.txt',
                             output = 'error: Working tree has modifications.'
                                      'Cannot add.'))


# Generated at 2022-06-14 09:56:53.174221
# Unit test for function get_new_command
def test_get_new_command():
    command = "git add ."
    output = "The following paths are ignored by one of your .gitignore files:\nmigrations/\nUse -f if you really want to add them."
    assert get_new_command(Command(script=command, output=output)) == "git add --force ."

# Generated at 2022-06-14 09:57:04.979636
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         output='fatal: pathspec \'src/main/java/com/example/app/App.java\' did not match any files\nUse -f if you really want to add them.'))
    assert match(Command('git add src/main/java/com/example/app/App.java',
                         output='fatal: pathspec \'src/main/java/com/example/app/App.java\' did not match any files\nUse -f if you really want to add them.'))
    assert not match(Command('git',
                         output='fatal: pathspec \'src/main/java/com/example/app/App.java\' did not match any files\nUse -f if you really want to add them.'))

# Generated at 2022-06-14 09:57:16.640103
# Unit test for function match
def test_match():
    assert match(Command('git add foo.txt',
                         'fatal: pathspec \'foo.txt\' did not match any files\n'
                         'Use -f if you really want to add them.'))
    assert not match(Command('git add',
                             'fatal: pathspec \'foo.txt\' did not match any files\n'
                             'Use -f if you really want to add them.'))
    assert not match(Command('git add foo.txt',
                             'fatal: pathspec \'foo.txt\' did not match any files'))
    assert not match(Command('git add foo.txt',
                             'fatal: pathspec \'foo.txt\' did not match any files'))
    assert not match(Command('ls', 'Did not match any files.'))


# Generated at 2022-06-14 09:57:19.357783
# Unit test for function match
def test_match():
    assert match(Command('git add ', 'Use -f if you really want to add them.'))
    assert not match(Command('git add ', ''))

# Generated at 2022-06-14 09:57:22.397142
# Unit test for function get_new_command
def test_get_new_command():
    command = Command.from_script('git add text.txt')
    assert get_new_command(command) == 'git add --force text.txt'

# Generated at 2022-06-14 09:57:37.465269
# Unit test for function match
def test_match():
    assert not match(Command('git add'))
    assert match(Command("git add -A", "error: 'al' is outside repository", "fatal: pathspec 'al' did not match any files"))
    assert not match(Command("git add -A", "error: 'al' is outside repository", "fatal: pathspec 'al' did not match any files", error=True))
    assert match(Command("git add files-does-not-exist", "fatal: pathspec 'files-does-not-exist' did not match any files"))
    assert not match(Command("git add files-does-not-exist", "fatal: pathspec 'files-does-not-exist' did not match any files", error=True))



# Generated at 2022-06-14 09:57:43.958539
# Unit test for function match
def test_match():
    # Valid command
    assert match(
        Command('git add repo', 'The following paths are ignored by one of\
                                 your .gitignore files:\nUse -f if you\
                                 really want to add them.'))
    # Not git command
    assert not match(Command('ls', ''))
    # No match
    assert not match(
        Command('git add repo', ''))

# Generated at 2022-06-14 09:57:46.886441
# Unit test for function get_new_command
def test_get_new_command():
	new_command = get_new_command(Command('git add test.sh'))
	assert new_command == 'git add --force test.sh'


enabled_by_default = True

# Generated at 2022-06-14 09:57:55.002494
# Unit test for function match
def test_match():
    assert match(
        Command('git add hello', 'The following paths are ignored by one of your .gitignore files:\nno_such_file\nUse -f if you really want to add them.'))
    assert not match(Command(script='git add hello', output='fatal: not a git repository (or any of the parent directories): .git'))
    assert not match(Command(script='git add hello', output='fatal: I would only add what is specified on the command line.'))
    assert not match(Command(script='git add hello', output='Aborting'))



# Generated at 2022-06-14 09:58:04.780708
# Unit test for function match

# Generated at 2022-06-14 09:58:09.397407
# Unit test for function match
def test_match():
    assert match(Command('git add foo/bar',
                         'The following paths are ignored by one of your .gitignore files:\nfoo/bar\nUse -f if you really want to add them.'))
    assert not match(Command('git add .', ''))



# Generated at 2022-06-14 09:58:13.952831
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'The following paths are ignored by one of your .gitignore files:\nlib\nUse -f if you really want to add them.')) == 'git add --force'


# Generated at 2022-06-14 09:58:15.989601
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add', 'Use -f if you really want to add them.')) == 'git add --force'


# Generated at 2022-06-14 09:58:20.751750
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script="git add", output="Use -f if you really want to add them.")) == "git add --force"
    assert get_new_command(Command(script="git add somefile", output="Use -f if you really want to add them.")) == "git add --force somefile"


# Generated at 2022-06-14 09:58:26.521795
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add x.py','''On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   x.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	y.py

Use -f if you really want to add them.
''')) == 'git add --force x.py'

# Generated at 2022-06-14 09:58:36.556580
# Unit test for function match
def test_match():
    assert match(Command('git add', '', 'addfile: name is a directory (not added)', '', 1, 0))
    assert not match(Command('git add', '', '', '', 1, 0))
    assert not match(Command('git rebase -i <commit-hash>', '', 'addfile: name is a directory (not added)', '', 1, 0))

# Generated at 2022-06-14 09:58:41.152110
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git add .') == 'git add --force .'
    assert get_new_command('git add -p') == 'git add --force -p'
    assert get_new_command('git add path/to/file') == 'git add --force path/to/file'


# Generated at 2022-06-14 09:58:47.014432
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add file.txt', 'The following paths are ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.')
    assert get_new_command(command) == "git add --force file.txt"

# Generated at 2022-06-14 09:58:51.459976
# Unit test for function match
def test_match():
    assert match(Command('git add', '',
        'The following paths are ignored by one of your '.format()
        +'.gitignore files:\n'))
    assert not match(Command('git add', ''))



# Generated at 2022-06-14 09:59:04.512585
# Unit test for function match
def test_match():
    assert match(Command('git add',
        'fatal: Pathspec \'thefuck\' is in submodule \'git-tfs\'\n'
        'Use -f if you really want to add them.'))
    assert match(Command('git add', 'fatal: Pathspec \'thefuck\' is in submodule \'git-tfs\'\nUse -f if you really want to add them.'))
    assert not match(Command('git add', 'fatal: Pathspec \'thefuck\' is in submodule \'git-tfs\'\nUse -f if you really want to add them', ''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 09:59:06.388448
# Unit test for function match
def test_match():
    command = Command("git add file", "fatal: LF would be replaced by CRLF in file", "")
    assert match(command)


# Generated at 2022-06-14 09:59:09.179323
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git add')
    assert 'git add --force' == get_new_command(command)


# Generated at 2022-06-14 09:59:19.371708
# Unit test for function match
def test_match():
    assert match(Command('$ git add .',
                         'The following paths are ignored by one of your .gitignore files:\nfile1\nfile2\nUse -f if you really want to add them.\nfatal: no files added\n',
                         '', 1))
    assert match(Command('$ git add .',
                         'The following paths are ignored by one of your .gitignore files:\nfile1\nfile2\nUse -f if you really want to add them.\n',
                         '', 1))
    assert not match(Command('$ git add .', '', '', 1))


# Generated at 2022-06-14 09:59:24.771602
# Unit test for function match
def test_match():
    assert match(Command('git add', '', 'error: The following untracked working tree files would be overwritten by merge:\n'
        '\tmyfile.js\n'
        '\n'
        'Please move or remove them before you can merge.\n'
        'Aborting\n', '', ''))



# Generated at 2022-06-14 09:59:30.068412
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         'fatal: pathspec \'commit\' did not match any files'))
    assert not match(Command('git commit',
                         'fatal: pathspec \'commit\' did not match any files'))
    # Test for the no added files thing
    assert match(Command('git add',
                         'fatal: no files added'))


# Generated at 2022-06-14 09:59:39.023214
# Unit test for function get_new_command
def test_get_new_command():
	# Test case 1
	out = get_new_command('git add -A')
	assert 'git add --force' in out
	
	# Test case 2
	out = get_new_command('git add --all')
	assert 'git add --force' in out

# Generated at 2022-06-14 09:59:42.798051
# Unit test for function get_new_command
def test_get_new_command():
    assert_equals(get_new_command(Command('git add foo',
        "error: 'foo' has changes staged in the index\n(use --cached to keep the file, or -f to force removal)",
	None)), 'git add --force foo')

# Generated at 2022-06-14 09:59:44.983750
# Unit test for function match
def test_match():
    assert (match(Command('git add foo', 'fatal: pathspec \'foo\' did not match any files', '')))
    assert (not match(Command('git foo', '', '')))


# Generated at 2022-06-14 09:59:45.895561
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(match) == "git add --force ."

# Generated at 2022-06-14 09:59:47.558787
# Unit test for function match
def test_match():
    assert match(Command('git add .',
               'fatal: Pathspec \'class/__init__.py\' is in submodule \'class\'', ''))



# Generated at 2022-06-14 09:59:53.452844
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         'The following paths are ignored by one of '+
                         'your .gitignore files:\n'+
                         'src/ignore\nUse -f if you really want to add them.'))
    assert not match(Command('git add', ''))


# Generated at 2022-06-14 09:59:58.789440
# Unit test for function match
def test_match():
    command = Command('git add .', "error: The following untracked working tree files would be overwritten by merge:\n    examples/example_git_aliases\n    examples/example_bashrc\n    examples/example_gitconfig\nPlease move or remove them before you can merge.\nAborting\n")
    assert match(command)


# Generated at 2022-06-14 10:00:05.613739
# Unit test for function match
def test_match():
    assert match(Command('git add test.py', 'warning: LF will be replaced by CRLF\nUse -f if you really want to add them.\n'))
    assert match(Command('git add test.py', 'error: LF will be replaced by CRLF\nUse -f if you really want to add them.\n'))
    assert not match(Command('git add test.py', 'LF will be replaced by CRLF\nUse -f if you really want to add them.\n'))
    assert not match(Command('git add test.py', 'Use -f if you really want to add them.\n'))
    assert not match(Command('git add test.py', 'Use -f if you really want to add them.'))

# Generated at 2022-06-14 10:00:09.891352
# Unit test for function match
def test_match():
    assert match(Command('', '', '', '', 'add: \'../\':'))
    assert match(Command('', '', '', '', 'add: \'../\':'))
    assert not match(Command('', '', '', '', 'add: \'../\':'))



# Generated at 2022-06-14 10:00:12.782545
# Unit test for function match
def test_match():
    assert match(Command('git add',
                         "Use -f if you really want to add them.",
                         "", 1))

    assert not match(Command('git add',
                         "Use -f if you really want to add them.",
                         "", 0))

    assert not match(Command('git add --force',
                         "Use -f if you really want to add them.",
                         "", 0))



# Generated at 2022-06-14 10:00:28.850167
# Unit test for function match
def test_match():
    match_1=Command('git add .', 'use -f if you really want to add them.')
    assert match(match_1)
    match_2=Command('git add foobar', 'use -f if you really want to add them.')
    assert match(match_2)
    match_3=Command('git', 'use -f if you really want to add them.')
    assert not match(match_3)
    match_4=Command('git add .', 'fatal: pathspec \'xxx\' did not match any files')
    assert not match(match_4)


# Generated at 2022-06-14 10:00:34.166572
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(['./', 'git', 'add', '-A']) == \
            ['./', 'git', 'add', '--force', '-A']



# Generated at 2022-06-14 10:00:37.358452
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git add .")) == 'git add --force .'

# Generated at 2022-06-14 10:00:40.087163
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git add a', 'Use -f if you really want to add them.')) == 'git add --force a'

# Generated at 2022-06-14 10:00:49.173340
# Unit test for function match
def test_match():
	assert match(Command(script='git add file1 file2', output='fatal: Not a git repository (or any of the parent directories): .git\n')) == False
	assert match(Command(script='git add file1 file2',
				output='fatal: not a git repository (or any of the parent directories): .git\nfatal: Not a git repository (or any of the parent directories): .git\n')) == False
	assert match(Command(script='git add file1 file2',
				output='fatal: not a git repository (or any of the parent directories): .git\nfatal: Not a git repository (or any of the parent directories): .git\n\n')) == False

# Generated at 2022-06-14 10:00:58.626624
# Unit test for function match
def test_match():
    assert match(Command('git add newfile', stderr='error: The following paths are ignored by one of your .gitignore files:'))
    assert match(Command('git add differentfile', stderr='error: The following paths are ignored by one of your .gitignore files:'))
    assert not match(Command('git commit -m Fix',\
            stderr='error: The following paths are ignored by one of your .gitignore files:'))
    assert not match(Command('git add', stderr='error: The following paths are ignored by one of your .gitignore files:'))


# Generated at 2022-06-14 10:01:02.307954
# Unit test for function match
def test_match():
    assert match(Command('git add .', 'Use -f if you really want to add them.'))
    assert not match(Command('git add .', ''))
    assert not match(Command('git commit', ''))


# Generated at 2022-06-14 10:01:07.483887
# Unit test for function match
def test_match():
    assert match('git add file1')
    assert match('git add file1 file2')
    assert not match('git add --force file1')
    assert not match('git add file1 file2 --force')
    assert not match('git commit')
    assert not match('cd newdir')


# Generated at 2022-06-14 10:01:14.521021
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git add')) == 'git add --force'
    assert get_new_command(Command('git add --all')) == 'git add --all --force'
    assert get_new_command(Command('git add -A')) == 'git add -A --force'
    assert get_new_command(Command('git add -u')) == 'git add -u --force'

# Generated at 2022-06-14 10:01:21.363509
# Unit test for function match
def test_match():
    """ Test: if the function match can run correctly or not
    """
    assert match(Command('git add .', 
                         '.gitignore:33:1: warning: missing whitespace after \
                          escape\n.gitignore:37:1: warning: missing whitespace \
                          after escape\nUse -f if you really want to add them.'))


# Generated at 2022-06-14 10:01:39.073303
# Unit test for function get_new_command
def test_get_new_command():
    #assert ('git add --force' == get_new_command(Command('git add',
    #                                            'The following untracked working tree files would be overwritten by merge:\n\tfile\nPlease move or remove them before you can merge.')))
    com = Command('git add',
                  'The following untracked working tree files would be overwritten by merge:\n\tfile\nPlease move or remove them before you can merge.')
    assert ('git add --force' == get_new_command(com))


# Generated at 2022-06-14 10:01:42.614511
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git add .',
                      'fatal: pathspec . did not match any files')

    assert (get_new_command(command) == 'git add --force .')

# Generated at 2022-06-14 10:01:45.845208
# Unit test for function match
def test_match():
    assert match(Command('git add fi…', 'fatal: LF would be replaced by CRLF …',
                         '', 0, '/etc/fih'))


# Generated at 2022-06-14 10:01:53.219117
# Unit test for function get_new_command
def test_get_new_command():
    output = 'fatal: LF would be replaced by CRLF in file.txt.\n'
    output += 'Use -f if you really want to add them.'
    command = 'git add file.txt'
    new_command = get_new_command(Command(command, output))
    assert new_command == 'git add --force file.txt'