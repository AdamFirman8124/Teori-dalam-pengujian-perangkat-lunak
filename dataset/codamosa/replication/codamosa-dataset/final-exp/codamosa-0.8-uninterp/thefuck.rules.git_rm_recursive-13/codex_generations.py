

# Generated at 2022-06-14 10:14:06.069458
# Unit test for function match
def test_match():
	assert not match(Command('git branch -r', '', '', 0, None))
	assert match(Command('git rm pack-a7589fc6d926b9ab04b57d328cc1ee07d2ff6e2f.idx', 'fatal: not removing \'pack-a7589fc6d926b9ab04b57d328cc1ee07d2ff6e2f.idx\' recursively without -r\n', '', 0, None))


# Generated at 2022-06-14 10:14:09.196969
# Unit test for function match
def test_match():
    assert not match(Command("git a", ""))
    assert match(Command("git rm a", """ fatal: not removing 'a' recursively without -r """))

# Generated at 2022-06-14 10:14:10.801450
# Unit test for function match
def test_match():
    assert match(Script('git rm file'))


# Generated at 2022-06-14 10:14:15.318941
# Unit test for function get_new_command
def test_get_new_command():
    # Confirm get_new_command returns expected command
    from thefuck.types import Command
    result = get_new_command(Command('git rm file.txt', '', ''))
    assert 'git rm -r file.txt' == result



# Generated at 2022-06-14 10:14:18.637240
# Unit test for function match
def test_match():
    command = Command('git rm -r file/')
    assert match(command)
    command2 = Command('git rm -r file')
    assert not match(command2)

# Generated at 2022-06-14 10:14:30.143999
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm foo',
                                   'fatal: not removing '
                                   "'.gitignore' recursively "
                                   'without -r')) \
        == 'git rm -r foo'
    assert get_new_command(Command('git rm -f foo',
                                   'fatal: not removing '
                                   "'.gitignore' recursively "
                                   'without -r')) \
        == 'git rm -f -r foo'
    assert get_new_command(Command('git rm -f foo bar',
                                   'fatal: not removing '
                                   "'.gitignore' recursively "
                                   'without -r')) \
        == 'git rm -f -r foo bar'

# Generated at 2022-06-14 10:14:37.101505
# Unit test for function match
def test_match():
    assert match(Command('git rm * -r', 'fatal: pathspec * did not match any files\n'
                         'fatal: not removing \'dir\' recursively without -r\n'))
    assert not match(Command('git rm * -r', 'fatal: pathspec * did not match any files\n'
                             'fatal: not removing \'dir\' with -r\n'))


# Generated at 2022-06-14 10:14:39.652987
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm -r new_ref") == "git rm -r new_ref"


# Generated at 2022-06-14 10:14:43.110634
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm README", "fatal: not removing 'README' recursively without -r")
    assert get_new_command(command) == "git rm -r README"

# Generated at 2022-06-14 10:14:47.995692
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r dir')
    assert get_new_command(command) == "git rm -r -r dir"

    command = Command('git rm -r dir1 dir2')
    assert get_new_command(command) == "git rm -r -r dir1 dir2"



# Generated at 2022-06-14 10:14:58.286615
# Unit test for function match
def test_match():
    assert match(Command('git rm dir',
             'fatal: not removing \'dir\' recursively without -r',
             ''))
    assert not match(Command('git rm dir',
             'fatal: not removing \'dir\' without -r',
             ''))

# Generated at 2022-06-14 10:15:00.218721
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm foo', '')) == 'git rm -r foo'

# Generated at 2022-06-14 10:15:09.807616
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -f test', 'fatal: not removing \'test\' recursively without -r')
    assert get_new_command(command) == 'git rm -r -f test'

    command = Command('git rm -f test test2', 'fatal: not removing \'test\' recursively without -r')
    assert get_new_command(command) == 'git rm -r -f test test2'

    command = Command('git a rm -f test', 'fatal: not removing \'test\' recursively without -r')
    assert get_new_command(command) != 'git a rm -r -f test'

# Generated at 2022-06-14 10:15:16.060008
# Unit test for function match
def test_match():
    assert git_support()
    assert match(Command('git rm -rf a', 'fatal: not removing \'a\''
                         ' recursively without -r'))
    assert not match(Command('git rm -r a', ''))
    assert not match(Command('git rm a', ''))


# Generated at 2022-06-14 10:15:19.471090
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r', "fatal: not removing '<directory>' recursively without -r\n", '')
    assert get_new_command(command) == u'git rm -r -r'

# Generated at 2022-06-14 10:15:21.617485
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm po/br')
    assert get_new_command(command) == 'git rm -r po/br'

# Generated at 2022-06-14 10:15:25.677133
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf foo',
                                   'fatal: not removing \'foo\' recursively without -r')) == 'git rm -r -rf foo'

# Generated at 2022-06-14 10:15:29.369065
# Unit test for function get_new_command
def test_get_new_command():
    output = 'fatal: not removing \'file\' recursively without -r\n'
    command = Command('git rm file', output)
    assert get_new_command(command) == u'git rm -r file'

# Generated at 2022-06-14 10:15:39.567516
# Unit test for function match
def test_match():
    assert match(Command('git rm file1 file2',
          'fatal: not removing \'file1\' recursively without -r\n'))
    assert match(Command('git rm file1 file2',
          'error: \'file1\' is not a valid path\nfatal: not removing \'file1\' recursively without -r\n'))
    assert match(Command('git rm file1 file2',
          'error: \'file2\' is not a valid path\nfatal: not removing \'file2\' recursively without -r\n'))
    assert not match(Command('git rm -r file1 file2',
          'fatal: not removing \'file1\' recursively without -r\n'))


# Generated at 2022-06-14 10:15:45.228594
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r directory_1')
    assert get_new_command(command) == 'git rm -r -r directory_1'

# Generated at 2022-06-14 10:15:56.529022
# Unit test for function get_new_command
def test_get_new_command():
    from types import SimpleNamespace as Ns

    command_output_str = 'fatal: not removing \'test/test_fucking.pyc\' recursively without -r'
    command_output_str += '\nDid you mean \'rm --cached test/test_fucking.pyc\'?'

    command_script_str = 'git rm test/test_fucking.pyc'

    command = Ns(script=command_script_str, script_parts=command_script_str.split(), output=command_output_str)

    assert get_new_command(command) == 'git rm -r test/test_fucking.pyc'

# Generated at 2022-06-14 10:16:00.605063
# Unit test for function get_new_command
def test_get_new_command():
    test_string = "git status"
    test_string = "git rm folder"
    command = Command(test_string)
    new_command = get_new_command(command)
    assert new_command == 'git rm -r folder'

# Generated at 2022-06-14 10:16:04.153251
# Unit test for function match
def test_match():
    assert match(Command('git rm directory/',
                        'fatal: not removing \'directory/\' recursively without -r'))
    assert not match(Command('git rm directory', ''))

# Generated at 2022-06-14 10:16:07.076392
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm keep.txt', '')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r keep.txt'

# Generated at 2022-06-14 10:16:12.156437
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r non_empty_folder/', 'fatal: not removing \'non_empty_folder/\' recursively without -r')
    assert(get_new_command(command) == 'git rm -r -r non_empty_folder/')


# Generated at 2022-06-14 10:16:21.049211
# Unit test for function match
def test_match():
    assert match(Command('rm -r foo', '', ''))
    assert match(Command('git rm -r foo', '', ''))
    assert match(Command('git rm -r /tmp/foo', "fatal: not removing '/tmp/foo' recursively without -r", ''))
    assert not match(Command('git pull', "fatal: not removing '/tmp/foo' recursively without -r", ''))
    assert not match(Command('git push', "fatal: not removing '/tmp/foo' recursively without -r", ''))



# Generated at 2022-06-14 10:16:29.675671
# Unit test for function get_new_command
def test_get_new_command():
    command1 = 'git rm foo'
    expected_command1 = 'git rm -r foo'
    assert get_new_command(Command(command1, '/home/makoto/Projects/')) == expected_command1

    command2 = 'git rm foo/bar'
    expected_command2 = 'git rm -r foo/bar'
    assert get_new_command(Command(command2, '/home/makoto/Projects/')) == expected_command2

if __name__ == '__main__':
    import pytest
    pytest.main(['-v', __file__])

# Generated at 2022-06-14 10:16:36.142752
# Unit test for function match
def test_match():
    assert match(Command('git rm file.ext', 'fatal: not removing \'file.ext\' recursively without -r\n'))
    assert match(Command('git rm file.ext', 'fatal: not removing \'file.ext\' recursively without -r'))
    assert not match(Command('git rm file.ext', ''))
    assert not match(Command('git rm file.ext', 'fatal: not removing \'file.ext\' recursively without -r', '', 3))


# Generated at 2022-06-14 10:16:42.246899
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('rm file', 'fatal: not removing \'file\' recursively without -r', '')) == True
    assert match(Command('rm -r file', '', '')) == False
    assert match(Command('rm file', '', '')) == False
    assert match(Command('git rm file', '', '')) == False
    assert match(Command('git rm -r file', '', '')) == False


# Generated at 2022-06-14 10:16:46.556805
# Unit test for function match
def test_match():
    assert match(Command(script='git rm test.txt',
                         output='fatal: not removing \'test.txt\' recursively without -r'))
    assert not match(Command(script='git rm test.txt',
                         output='fatal: not removing '))


# Generated at 2022-06-14 10:16:57.113516
# Unit test for function match
def test_match():
    assert match(Command('git branch test_branch', '', 'fatal: not removing \'dir_name\' recursively without -r'))
    assert not match(Command('git branch test_branch', '', 'fatal: branch \'test_branch\' already exists.'))
    assert match(Command('git branch test_branch', '', 'fatal: not removing \'file_name\' recursively without -r'))


# Generated at 2022-06-14 10:17:00.303062
# Unit test for function match
def test_match():
    assert match(Command('git rm f', ''))
    assert not match(Command('git rm file.txt', ''))
    assert not match(Command('python rm f', ''))


# Generated at 2022-06-14 10:17:03.252535
# Unit test for function match
def test_match():
    assert match(Command('git rm README', '', ''))
    assert not match(Command('git pull', '', ''))


# Generated at 2022-06-14 10:17:07.816886
# Unit test for function match
def test_match():
    assert match(Command('git rm -r folder',
               '', 'fatal: not removing \'folder\' recursively without -r', '', 1))
    assert not match(Command('rm file', '', '', '', 1))


# Generated at 2022-06-14 10:17:18.979882
# Unit test for function match
def test_match():
    assert match(Command("git rm tmp/cache/foo.txt", \
            "fatal: not removing 'tmp/cache/foo.txt' recursively without -r"))
    assert match(Command("git rm tmp/cache", \
            "fatal: not removing directory 'tmp/cache' recursively without -r"))
    assert match(Command("git rm tmp/cache/", \
            "fatal: not removing directory 'tmp/cache/' recursively without -r"))
    assert not match(Command("git rm tmp/cache/foo.txt", ""))
    assert not match(Command("git rm tmp/cache", ""))
    assert not match(Command("git rm tmp/cache/", ""))


# Generated at 2022-06-14 10:17:22.593727
# Unit test for function match
def test_match():
    assert match('git rm foo')
    assert not match('git rm -r foo')
    assert not match('git rm')
    assert not match('git add')
    assert not match('git status')


# Generated at 2022-06-14 10:17:30.037319
# Unit test for function match
def test_match():
    assert match(Command('git rm file1 file2 file3',
                         "fatal: not removing 'file1' recursively without -r"))
    assert not match(Command('git rm file1',
                             "fatal: not removing 'file1' recursively without -r"))
    assert not match(Command('git rm -r file1',
                             "fatal: not removing 'file1' recursively without -r"))
    assert not match(Command('git rm --cached README.md', ''))


# Generated at 2022-06-14 10:17:38.160407
# Unit test for function match
def test_match():
    command = Command('git rm -r */')
    command.output = 'fatal: not removing \'*/*/\' recursively without -r\n'
    assert match(command)

    command.output = 'fatal: not removing \'*\' recursively without -r\n'
    assert match(command)



# Generated at 2022-06-14 10:17:39.712313
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(u"git rm foo bar") == "git rm -r foo bar")

# Generated at 2022-06-14 10:17:42.782816
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm hello', '', '')) == 'git rm -r hello'
    assert get_new_command(Command('rm hello world', '', '')) == 'git rm -r hello world'

# Generated at 2022-06-14 10:17:51.817757
# Unit test for function get_new_command
def test_get_new_command():
	assert u'-r' in get_new_command('git rm -rf .')
	assert u'-r' in get_new_command('git rm .')
	assert u'-r' in get_new_command('git rm --cached .')
	assert u'-r' in get_new_command('git rm -f .')

# Generated at 2022-06-14 10:17:56.705587
# Unit test for function get_new_command
def test_get_new_command():
    # Function get_new_command do not execute a command, it returns a new command
    # Therefore, this function should return '' if the original command is ''
    if (get_new_command('') == ''):
        print("Correct return of get_new_command for '' as parameter")
    else:
        print("ERROR - Invalide return of get_new_command for '' as parameter")
        return False
    return True

# Generated at 2022-06-14 10:18:00.285298
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm folder1',
                                   'fatal: not removing \'folder1\' recursively without -r')) == u'git rm -r folder1'



# Generated at 2022-06-14 10:18:03.381560
# Unit test for function match
def test_match():
    assert (match(Command('git rm -f', 'fatal: not removing \'foo/bar\' recursively without -r')) == True)


# Generated at 2022-06-14 10:18:10.571442
# Unit test for function match
def test_match():
    match_output_1 = "fatal: not removing 'index/index/index' recursively without -r"
    match_output_2 = "fatal: not removing 'index/index/index' recursively without -r\n"
    command_1 = Command("git rm index/index/index", match_output_1)
    command_2 = Command("git rm index/index/index", match_output_2)
    assert match(command_1)
    assert match(command_2)


# Generated at 2022-06-14 10:18:13.947059
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm -r foo',
                      output="fatal: not removing 'foo' recursively without -r")
    assert(get_new_command(command) == 'git rm -r -r foo')

# Generated at 2022-06-14 10:18:26.770725
# Unit test for function match
def test_match():
    m = MagicMock(
        script='git stash rm 1',
        output='fatal: not removing \'doc/\' recursively without -r\nwarning: '
               'You ran \'git stash drop\' with neither \'--include-untracked\''
               ' nor \'--all\', but you have untracked files in your working '
               'tree. These untracked files would be overwritten by checkout.'
               'earlier stash '
               'was dropped to make room for the current (stash@{0})'
    )
    assert match(m)

# Generated at 2022-06-14 10:18:28.008912
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf file1 file2 file3'))


# Generated at 2022-06-14 10:18:31.747064
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm a b',
                                   stdout=u'fatal: not removing \'a\' recursively without -r\n')) == u'git rm -r a b'

# Generated at 2022-06-14 10:18:36.234231
# Unit test for function match
def test_match():
    assert match(Command("git rm file",
                "fatal: not removing 'file' recursively without -r\n",
                "git rm file"))

    assert not match(Command("git rm file",
                 "fatal: not removing 'file' recursively without -r\n",
                 "fuck git rm file"))

    assert not match(Command("git ls", "fatal: not removing 'file' recursively without -r\n", "git ls"))

# Generated at 2022-06-14 10:18:46.393572
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm foo", "fatal: not removing 'foo' recursively without -r")
    assert get_new_command(command) == "git rm -r foo"
    command = Command("git rm foo bar", "fatal: not removing 'foo' recursively without -r")
    assert get_new_command(command) == "git rm -r foo bar"

# Generated at 2022-06-14 10:18:55.328334
# Unit test for function match
def test_match():
    print('Testing function match')
    assert match(Command('git rm abcdefg',
                         'fatal: not removing \'abcdefg\' recursively without -r'))
    assert match(Command('git rm -r abcdefg',
                         'fatal: not removing \'abcdefg\' recursively without -r')) is False
    assert match(Command('git rm abcdefg',
                         'fatal: not removing \'abcdefg\' without -r')) is False


# Generated at 2022-06-14 10:19:00.456519
# Unit test for function match
def test_match():
    assert match(Command('rm -rf .', ''))
    assert not match(Command('rm -rf .', '', stderr='fatal: not removing '))
    assert not match(Command('rm -rf .', '', stderr='fatal: not removing '
                                                    'recursively without -r'))



# Generated at 2022-06-14 10:19:03.221237
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm file', 'fatal: not removing file recursively without -r', '')) == u'git rm -r file'

# Generated at 2022-06-14 10:19:11.050223
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r\n'))
    assert match(Command('git rm file1 file2',
                         'fatal: not removing \'file1\' recursively without -r\n',
                         'fatal: not removing \'file2\' recursively without -r\n'))
    assert not match(Command('git rm file', ''))
    assert not match(Command('git add file', ''))



# Generated at 2022-06-14 10:19:16.926304
# Unit test for function match
def test_match():
    assert match(Command('git branch abc',
                'fatal: Not removing \'abc\' recursively without -r',
                '', 0))
    assert not match(Command('git branch abc',
                '',
                '', 0))
    assert not match(Command('',
                'fatal: Not removing \'abc\' recursively without -r',
                '', 0))

# Generated at 2022-06-14 10:19:19.274441
# Unit test for function match
def test_match():
    assert match(Command('git rm new_file', 'fatal: not removing \'new_file\' recursively without -r'))


# Generated at 2022-06-14 10:19:23.012709
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -f',
                                   output='fatal: not removing \'./test\' recursively without -r')) == 'git rm -f -r'

# Generated at 2022-06-14 10:19:28.209433
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo', 'foo'))
    assert not match(Command('ls foo', 'fatal: not removing \'foo\' recursively without -r'))


# Generated at 2022-06-14 10:19:31.724568
# Unit test for function get_new_command
def test_get_new_command():
    test_command = 'test rm'
    test_output = "test: not removing '" in command.output
    assert get_new_command(test_command, test_output) == u'test rm -r'

# Generated at 2022-06-14 10:19:44.738132
# Unit test for function match
def test_match():
    assert (
        match(Command('git rm', 'fatal: not removing \'file\' recursively without -r', ''))
    )
    assert not match(Command('git rm', 'fatal: not removing \'file\' recursively without -r', ''))


# Generated at 2022-06-14 10:19:53.538867
# Unit test for function match
def test_match():
    assert match(Command('git rm file.py',
                         'fatal: not removing \'file.py\' recursively without -r'))
    assert not match(Command('git clone repo', ''))
    assert not match(Command('git status', ''))



# Generated at 2022-06-14 10:20:02.867817
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git status', 'fatal: not removing \'contracts/v1/migrations\' recursively without -r')
    assert get_new_command(command) == 'git rm -r contracts/v1/migrations'

# Generated at 2022-06-14 10:20:05.816267
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm -r [blah]', output='random output')
    assert( get_new_command(command) == 'git rm -r -r [blah]' )

# Generated at 2022-06-14 10:20:07.384132
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    #test if get_new_command successfully modify s

# Generated at 2022-06-14 10:20:11.623412
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.specific.git import git_support
    assert git_support
    # Command, script, output
    command = MagicMock(script = "git rm file.txt", output = "")
    command.script_parts = ["git", "rm", "file.txt"]
    assert "git rm -r file.txt" == get_new_command(command)

# Generated at 2022-06-14 10:20:14.897611
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -f file')) == 'git -r rm -f file'



# Generated at 2022-06-14 10:20:18.434116
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -r path',
                                   output='fatal: not removing \'path\' recursively without -r')) == 'git rm -r -r path'

# Generated at 2022-06-14 10:20:25.320607
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt', ''))
    assert not match(Command('git rm file.txt', '', error=127))
    assert match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively without -r', error=128))

# Generated at 2022-06-14 10:20:28.137673
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm')) == 'git rm -r'

# Generated at 2022-06-14 10:20:49.191068
# Unit test for function match
def test_match():
    # True cases
    # git rm file
    assert match(
        Command('git rm file',
                """fatal: not removing 'file' recursively without -r\n""")
    )
    # git rm some_folder
    assert match(
        Command('git rm some_folder',
                """fatal: not removing 'some_folder' recursively without -r\n""")
    )
    # git rm file some_folder
    assert match(
        Command('git rm file some_folder',
                """fatal: not removing 'some_folder' recursively without -r\n""")
    )
    # git rm -n some_folder

# Generated at 2022-06-14 10:20:50.967073
# Unit test for function match
def test_match():
    assert match(Command('git rm foo'))


# Generated at 2022-06-14 10:20:59.803791
# Unit test for function match
def test_match():
    assert match(Command(script='git rm file.txt'))
    assert match(Command(script='git rm -f file.txt'))
    assert not match(Command(script='git rm -r file.txt'))
    assert not match(Command(script='git commit'))


# Generated at 2022-06-14 10:21:05.032908
# Unit test for function match
def test_match():
    assert match(Command('git rm file', output='fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', output='fatal: not removing \'file\' recursively with -r'))
    assert not match(Command('git rm file'))


# Generated at 2022-06-14 10:21:07.442541
# Unit test for function match
def test_match():
    assert match(Command('rm foo'))
    assert match(Command('git rm foo'))
    assert not match(Command('git'))

# Generated at 2022-06-14 10:21:11.874070
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command('git rm -rf srv') == 'git rm -rf -r srv')
    assert (get_new_command('git rm -r srv') == 'git rm -r -r srv')
    assert (get_new_command('rm -r srv') == 'rm -r -r srv')
    assert (get_new_command('rm srv') == 'rm -r srv')

# Generated at 2022-06-14 10:21:14.010316
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    new_command = get_new_command(Command('git rm src'))
    assert new_command == 'git rm -r src'

# Generated at 2022-06-14 10:21:19.092201
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('rm file')) == 'git rm -r file'
    assert get_new_command(
        Command('git rm file')) == 'git rm -r file'
    assert get_new_command(Command('git rm it')) == 'git rm -r it'

# Generated at 2022-06-14 10:21:23.320445
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', ''))



# Generated at 2022-06-14 10:21:29.512214
# Unit test for function match
def test_match():
    assert match(Command('git rm untracked_file',
                         'fatal: not removing \'untracked_file\' recursively without -r'))
    assert not match(Command('git rm -r untracked_file',
                             'fatal: not removing \'untracked_file\' recursively without -r'))
    assert not match(Command('git rm untracked_file', ''))



# Generated at 2022-06-14 10:21:48.323871
# Unit test for function match

# Generated at 2022-06-14 10:21:52.274526
# Unit test for function match
def test_match():
    assert match(Command('rm f',
                         'fatal: not removing \'f\': \
                         it is a directory (use -r)'))
    assert not match(Command('rm f', 'fatal: not removing \'f\':'))

# Generated at 2022-06-14 10:22:02.171477
# Unit test for function match
def test_match():
    # In case of script contains "rm"
    assert match(Command('rm -r test',
                         'fatal: not removing \'test\' recursively without -r'))

    # In case of script does not contain "rm"
    assert not match(Command('ls', ''))

    # In case of script contains "rm" but the error message does not match
    assert not match(Command('rm -r test', 'fatal: not removing \'test\''))



# Generated at 2022-06-14 10:22:07.918786
# Unit test for function match
def test_match():
    assert match(Command('git rm -r <file>', 'fatal: not removing '
                         '\'.gitignore\' recursively without -r'))
    assert not match(Command('git rm -r <file>', 'fatal: not removing '
                             '\'notexist\' recursively without -r'))


# Generated at 2022-06-14 10:22:18.910513
# Unit test for function match
def test_match():
    # Command with script containing word 'rm' and output containing words 'fatal' and 'recursively'
    assert match(Command('git rm a')) is True
    # Command with script not containing word 'rm' and output containing words 'fatal' and 'recursively'
    assert match(Command('git rm')) is False
    # Command with script containing word 'rm' and output not containing words 'fatal' and 'recursively'
    assert match(Command('rm a')) is False
    # Command with script containing word 'rm' and output containing words 'fatal' and 'recursively' and not 'without'
    assert match(Command('git rm a')) is True


# Generated at 2022-06-14 10:22:29.044199
# Unit test for function match
def test_match():
    assert match(Command('git rm -r test', 'fatal: not removing \'test\' recursively without -r'))
    assert not match(Command('git rm test', 'fatal: not removing \'test\' recursively without -r'))
    assert not match(Command('rm test', 'fatal: not removing \'test\' recursively without -r'))
    assert not match(Command('git rm test', None))
    assert not match(Command('git status', None))

# Generated at 2022-06-14 10:22:33.600670
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
        output="fatal: not removing 'file' recursively without -r",
        ))
    assert not match(Command('git rm file',
        output="fatal: not removing 'file'",
        ))

# Generated at 2022-06-14 10:22:42.423295
# Unit test for function match
def test_match():
    assert match(Command('git rm -r', 'fatal: not removing \'xx\' recursively without -r'))
    assert match(Command('git rm', 'fatal: not removing \'xx\' recursively without -r'))
    assert match(Command('git rm xxx/xxx/xxx', 'fatal: not removing \'xxx/xxx/xxx\' recursively without -r'))
    assert not match(Command('git rm', 'fatal: not removing \'xx\' recursively without -r', '', None, ''))
    assert not match(Command('git', 'fatal: not removing \'xx\' recursively without -r', '', None, ''))


# Generated at 2022-06-14 10:22:48.484354
# Unit test for function match
def test_match():
    assert match(Command('git rm README.md',
                   'fatal: not removing \'README.md\' recursively without -r\n'))
    assert not match(Command('git checkout README.md',
                   'fatal: not removing \'README.md\' recursively without -r\n'))


# Generated at 2022-06-14 10:22:51.348776
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test', 'fatal: not removing test')) == 'git rm -r test'

# Generated at 2022-06-14 10:23:35.341625
# Unit test for function match
def test_match():
    assert match(Command('git rm -f', stderr='fatal: not removing \'bar\' recursively without -r\n'))
    assert match(Command('git rm', stderr='fatal: not removing \'bar\' recursively without -r\n'))
    assert not match(Command('git rm', stderr='fatal: not removing \'bar\' recursively without -f\n'))
    assert not match(Command('git rm', stderr='fatal: n ot removing \'bar\' recursively without -f\n'))


# Generated at 2022-06-14 10:23:46.995443
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('rm -r') == 'rm -r'
	assert get_new_command('rm  -r') == 'rm  -r'
	assert get_new_command('rm -r ') == 'rm -r '
	assert get_new_command('rm  -r ') == 'rm  -r '
	assert get_new_command('rm -r  ') == 'rm -r  '
	assert get_new_command('rm  -r  ') == 'rm  -r  '
	assert get_new_command('rm -r -r') == 'rm -r -r'
	assert get_new_command('rm  -r  -r') == 'rm  -r  -r'

# Generated at 2022-06-14 10:23:51.396417
# Unit test for function get_new_command
def test_get_new_command():
    command = Command.from_string('git rm -r test')
    assert get_new_command(command) == 'git rm -r -r test'

    command = Command.from_string('git rm test')
    assert get_new_command(command) == 'git rm -r test'

# Generated at 2022-06-14 10:23:53.866047
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command(Command(script = "git rm a_folder", output = "")) == "git rm -r a_folder"

# Generated at 2022-06-14 10:23:59.093281
# Unit test for function match
def test_match():
    assert match(Command('git rm non-existent'
        , "fatal: not removing 'non-existent' recursively without -r"))
    assert not match(Command('git rm non-existent'
        , "fatal: not removing 'non-existent' recursively without -r", error=True))
