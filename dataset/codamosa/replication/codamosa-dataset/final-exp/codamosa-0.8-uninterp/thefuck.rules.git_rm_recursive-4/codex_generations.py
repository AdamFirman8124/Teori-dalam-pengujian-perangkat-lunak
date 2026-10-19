

# Generated at 2022-06-14 10:14:01.351374
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git rm folder',
                                   'fatal: not removing \'folder\' recursively without -r '
                                   'Did you mean this?'))\
        == 'git rm -r folder'

# Generated at 2022-06-14 10:14:05.459690
# Unit test for function match
def test_match():
    new_command = "git rm test/spam.txt"
    wrong_command = "git add test.txt"
    assert match(Command(script=new_command))
    assert not match(Command(script=wrong_command))


# Generated at 2022-06-14 10:14:09.964148
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm import get_new_command
    command = "git rm srcs"
    output = "fatal: not removing 'srcs' recursively without -r"
    assert get_new_command(command, output) == 'git rm -r srcs'

# Generated at 2022-06-14 10:14:13.989640
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -r *', output='fatal: not removing \'*\' recursively without -r')) == 'git -r rm *'
    


# Generated at 2022-06-14 10:14:15.602956
# Unit test for function match
def test_match():
    assert match(Command('git rm file'))


# Generated at 2022-06-14 10:14:23.424979
# Unit test for function match
def test_match():
    # Testing with string containing rm and error fatal: not removing
    assert match(Command('rm -r *.txt', 'fatal: not removing \'*.txt\' recursively without -r'))
    assert match(Command('rm *.txt', 'fatal: not removing \'*.txt\' recursively without -r'))
    assert not match(Command('rm', 'fatal: not removing \'*.txt\' recursively without -r'))


# Generated at 2022-06-14 10:14:30.209263
# Unit test for function match
def test_match():
    assert match(Command('git rm -r path', '', '', 1))
    assert match(Command('git rm path', 'fatal: not removing \'path\''
                         ' recursively without -r', '', 1))
    assert not match(Command('git rm path', '', '', 1))
    assert not match(Command('git pull', '', '', 1))


# Generated at 2022-06-14 10:14:37.652418
# Unit test for function get_new_command
def test_get_new_command():
  assert get_new_command("git rm blah blah blah") == "git rm -r blah blah blah"
  assert get_new_command(" git rm blah blah blah ") == "git rm -r blah blah blah"
  assert get_new_command("git rm   blah blah blah") == "git rm -r blah blah blah"
  assert get_new_command("git rm  blah  blah  blah") == "git rm -r blah blah blah"

# Generated at 2022-06-14 10:14:41.094788
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -f src', '', 'not removing ''src'' recursively without -r')
    assert get_new_command(command) == 'git rm -f -r src'

# Generated at 2022-06-14 10:14:44.570425
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf folder', ''))
    assert match(Command('git rm -rf folder', 'fatal: not removing \'folder\' recursively without -r\n',))


# Generated at 2022-06-14 10:14:58.351625
# Unit test for function get_new_command
def test_get_new_command():
    command1 = Command('git rm -r test', 'fatal: not removing \'test\' recursively without -r')
    command2 = Command('git rm test', 'fatal: not removing \'test\' recursively without -r')
    assert get_new_command(command1) == 'git rm -r -r test'
    assert get_new_command(command2) == 'git rm -r test'

# Generated at 2022-06-14 10:15:01.593680
# Unit test for function match
def test_match():
    git_cmd = 'git rm *.txt'
    output = "fatal: not removing '*.txt' recursively without -r"
    assert match(Command(script=git_cmd, output=output))



# Generated at 2022-06-14 10:15:07.967782
# Unit test for function match
def test_match():
    assert match(Command('git rm badFile', 'fatal: not removing \'badFile\' recursively without -r'))
    assert not match(Command('rm badFile', 'fatal: not removing \'badFile\' recursively without -r'))
    assert not match(Command('git rm badFile',
                             'fatal: not removing \'badFile\' recursively without'))


# Generated at 2022-06-14 10:15:13.611990
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively'
                         ' without -r\ngit rm -f file.txt',
                         'git rm -f file.txt'))
    assert not match(Command('ls', 'fatal: not removing 1', 'ls'))


# Generated at 2022-06-14 10:15:18.648918
# Unit test for function get_new_command
def test_get_new_command():
    output = "fatal: not removing 'fuck/fake.txt' recursively without -r\n"
    command = Command('git rm fuck/fake.txt', output)
    assert get_new_command(command) == 'git rm -r fuck/fake.txt'

# Generated at 2022-06-14 10:15:22.191572
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm folder',
                      'fatal: not removing \'folder\' recursively without -r')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r folder'

# Generated at 2022-06-14 10:15:27.268707
# Unit test for function match
def test_match():
    assert match(Command('rm dir', ''))
    assert not match(Command('rm', ''))
    assert not match(Command('git rm hello.txt', ''))
    assert not match(Command('echo hello', ''))


# Generated at 2022-06-14 10:15:34.376720
# Unit test for function match
def test_match():
    command = 'git status'
    assert command_output(command)
    assert 'fatal: Could not switch to' not in command_output(command)
    assert not match(Command(script=command,
                             output='fatal: Could not switch to'))
    assert match(Command(script='git rm -r a/b',
                         output="fatal: not removing 'a/b' recursively without -r"))


# Generated at 2022-06-14 10:15:39.081445
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm -r directory'
    output = """fatal: not removing 'directory' recursively without -r
Try 'git rm --cached -r directory' to unstage it."""
    new_command = 'git rm -r directory'
    assert get_new_command(Command(script, output)) == new_command

# Generated at 2022-06-14 10:15:46.236519
# Unit test for function get_new_command
def test_get_new_command():
    command = type('obj', (object,), {'script_parts': [u'git', u'rm', u'file.txt']})
    assert get_new_command(command) == u'git rm -r file.txt'

# Generated at 2022-06-14 10:15:54.650511
# Unit test for function match
def test_match():
    assert match(Command('git rm file', output='fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', output='fatal: not removing \'file\''))



# Generated at 2022-06-14 10:15:58.097715
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm test.txt", "fatal: not removing 'test.txt' recursively without -r")) == "git rm -r test.txt"

# Generated at 2022-06-14 10:16:02.116033
# Unit test for function match
def test_match():
    # Test match of git rm command output with recursive error
    command = Command('git rm lib', (
        'fatal: not removing \'lib\' recursively without -r\n'
    ))
    assert match(command)


# Generated at 2022-06-14 10:16:06.637198
# Unit test for function match
def test_match():
    assert match(Command('git rm x', '', 'fatal: not removing \'x\' recursively without -r'))
    assert not match(Command('git rm x', '', 'fatal: not removing \'x\' recursively without -r', '', 4))


# Generated at 2022-06-14 10:16:14.973554
# Unit test for function match
def test_match():
    assert (match(Command('git rm file1/file2/ file3/file4/', ''))
            == False)
    assert (match(Command('git rm file1/file2/ file3/file4/',
                'fatal: not removing \'file1/file2/\' recursively without -r'))
            == True)
    assert (match(Command('git rm file1/file2/ file3/file4/',
                'fatal: not removing \'file3/file4/\' recursively without -r'))
            == True)

# Generated at 2022-06-14 10:16:26.115434
# Unit test for function match
def test_match():
    command = Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r')
    assert match(command)

    command = Command('git rm -r test.txt', 'fatal: not removing \'test.txt\' recursively without -r')
    assert not match(command)

    command = Command('rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r')
    assert not match(command)

    command = Command('git rm test.txt', 'fatal: not removing test.txt')
    assert not match(command)

    command = Command('git rm test.txt', 'fatal: not removing recursively without -r')
    assert not match(command)


# Generated at 2022-06-14 10:16:29.223341
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git rm file', 'fatal: not removing \'file\' recursively without -r', '')) == 'git rm -r file'

# Generated at 2022-06-14 10:16:31.374066
# Unit test for function get_new_command
def test_get_new_command():
    output = "fatal: not removing 'subfolder' recursively without -r"
    command = Command("git rm subfolder", output)
    assert get_new_command(command) == "git rm -r subfolder"

# Generated at 2022-06-14 10:16:41.364445
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm file", "fatal: not removing 'file' recursively without -r")
    assert get_new_command(command) == "git rm -r file"
    command = Command("git remote rm file", "fatal: not removing 'file' recursively without -r")
    assert get_new_command(command) == "git remote rm -r file"
    command = Command("git -c receive.denyNonFastForwards=false push origin +master:master", "fatal: not removing 'file' recursively without -r")
    assert get_new_command(command) != "git -c receive.denyNonFastForwards=false push origin +master:master -r"
    command = Command("git rm file1 file2", "fatal: not removing 'file' recursively without -r")
   

# Generated at 2022-06-14 10:16:46.905765
# Unit test for function match
def test_match():
    # Testing if function match works correctly
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', 'fatal: not removing file recursively without -r'))
    assert not match(Command('git rm file', 'fatal: not removing \'file\''))



# Generated at 2022-06-14 10:16:59.727604
# Unit test for function get_new_command
def test_get_new_command():
    output = u'fatal: not removing \'README.md\' recursively without -r'
    result = get_new_command(Command('git rm README.md', output))
    assert 'git rm -r README.md' == result

# Generated at 2022-06-14 10:17:06.339102
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf foo', 'fatal: not removing \'foo\' recursively without -r'))
    assert match(Command('git rm -rf foo', 'fatal: not removing \'bar/foo\' recursively without -r'))

# Generated at 2022-06-14 10:17:15.183078
# Unit test for function get_new_command
def test_get_new_command():
    commands = [{'script': 'git rm --cached -r some_folder',
                 'output': 'fatal: not removing \'some_folder\' recursively without -r',
                 'new_cmd': 'git rm -r --cached -r some_folder'},
                {'script': 'git rm --cached -f some_folder',
                 'output': 'fatal: not removing \'some_folder\' recursively without -r',
                 'new_cmd': 'git rm -r --cached -f some_folder'},
                {'script': 'git rm -r --cached some_folder',
                 'output': 'fatal: not removing \'some_folder\' recursively without -r',
                 'new_cmd': 'git rm -r -r --cached some_folder'}]


# Generated at 2022-06-14 10:17:18.171515
# Unit test for function match
def test_match():
    assert match(Command('git rm', 'fatal: not removing \'f\' recursively without -r'))



# Generated at 2022-06-14 10:17:23.287615
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm foo/baz', 'error: pathspec \'foo/baz\' did not match any file(s) known to git.\nfatal: not removing \'foo/baz\' recursively without -r')) == 'git rm -r foo/baz'

# Generated at 2022-06-14 10:17:25.763261
# Unit test for function match
def test_match():
    assert match(Command('git rm myfile', "fatal: not removing 'myfile' recursively without -r"))


# Generated at 2022-06-14 10:17:32.308291
# Unit test for function match
def test_match():
    assert match(Command('git rm foo/bar/baz',
                         'fatal: not removing \'foo/bar/baz\' recursively without -r'))
    assert not match(Command('git rm foo/bar/baz', 'success'))
    assert not match(Command('git foo/bar/baz',
                             'fatal: not removing \'foo/bar/baz\' recursively without -r'))


# Generated at 2022-06-14 10:17:33.130513
# Unit test for function match
def test_match():
    asser

# Generated at 2022-06-14 10:17:45.034551
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r',
                          ''))
    assert not match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r',
                          '', True))
    assert not match(Command('git rm file.txt',
                         'fatal: not removing \'file.txt\' recursively without -r',
                          '', False))
    assert not match(Command('git rm file.txt', '', ''))
    assert not match(Command('git add file.txt', '', ''))
    # Regression test for #589
    assert match(Command('git rm file.txt', 'error: \'file.txt\' has changes staged in the index', ''))



# Generated at 2022-06-14 10:17:49.190525
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm .', 'fatal: not removing \'.\' recursively without -r', '', '', '')) == 'git rm -r .'

# Generated at 2022-06-14 10:18:09.869975
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file', 'fatal: not removing \'file\' recursively without -r')) == 'git rm -r file'

# Generated at 2022-06-14 10:18:12.352671
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm "test2" "test3"') == 'git rm -r "test2" "test3"'

# Generated at 2022-06-14 10:18:17.489704
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm  -d python", "fatal: not removing 'python' recursively without -r")
    assert_equals("git rm -d -r python", get_new_command(command))

# Generated at 2022-06-14 10:18:25.223514
# Unit test for function match
def test_match():
    # Save stdout
    saved_stdout = sys.stdout
    try:
        # Capture sys.stdout
        out = StringIO()
        sys.stdout = out

        # Run command
        match(Command('git rm -rf .'))
    finally:
        sys.stdout = saved_stdout

    output = out.getvalue().strip()
    assert ('fatal: not removing \'.\' recursively without -r' in output)


# Generated at 2022-06-14 10:18:28.647695
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm -r test', output='')) == 'git rm -r -r test'

# Generated at 2022-06-14 10:18:32.927432
# Unit test for function match
def test_match():
    # git cmd
    assert match(Command('git rm -rf .',
                         'fatal: not removing \'prov/sources\' recursively without -r',
                         '', 1))
    assert not match(Command('', '', '', 1))



# Generated at 2022-06-14 10:18:40.653775
# Unit test for function get_new_command
def test_get_new_command():
    script = u'git rm file.txt'
    output = u"error: oops"
    command = Command(script, output)
    assert u'git rm -r file.txt' == get_new_command(command)

    script = u'git rm file.txt'
    output = u"fatal: not removing 'file.txt' recursively without -r"
    command = Command(script, output)
    assert u'git rm -r file.txt' == get_new_command(command)

# Generated at 2022-06-14 10:18:44.040871
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm filename', 'fatal: not removing \'filename\' recursively without -r')
    assert get_new_command(command) == 'git rm -r filename'

# Generated at 2022-06-14 10:18:46.920077
# Unit test for function get_new_command
def test_get_new_command():
    assert ('git rm -r newfile', get_new_command(Command('git rm newfile',
            stderr="fatal: not removing 'newfile' recursively without -r")))

# Generated at 2022-06-14 10:18:50.975918
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm foo bar") == "git rm -r foo bar"
    assert get_new_command("git rm -f foo bar") == "git rm -f -r foo bar"

# Generated at 2022-06-14 10:19:11.297239
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm test.txt') == 'git rm -r test.txt'

# Generated at 2022-06-14 10:19:17.147115
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm -f test.txt')) == 'git rm -r -f test.txt'
    assert get_new_command(Command('git rm -f test.txt')) == 'git rm -r -f test.txt'
    assert get_new_command(Command('rm -rf test.txt')) == 'git rm -rf test.txt'

# Generated at 2022-06-14 10:19:29.737114
# Unit test for function get_new_command
def test_get_new_command():
    # Test for git
    # Has one file, the file is regular file
    data = {'script_parts': ['git', 'rm', 'foo.txt'],
            'output': "fatal: not removing 'foo.txt' recursively without -r"}
    command = Command(**data)
    assert get_new_command(command) == (
        "git rm -r foo.txt")

    # Has one file, the file is a directory
    data = {'script_parts': ['git', 'rm', 'foo.txt'],
            'output': "fatal: not removing 'foo.txt' recursively without -r"}
    command = Command(**data)
    assert get_new_command(command) == (
        "git rm -r foo.txt")

    # Has several files

# Generated at 2022-06-14 10:19:36.749768
# Unit test for function match
def test_match():

    command = Command('git rm *.txt', stderr='fatal: not removing \'*.txt\' recursively without -r\n')
    assert(match(command))

    command = Command('git rm -r', stderr='fatal: not removing \'*.txt\' recursively without -r\n')
    assert(not match(command))

    command = Command('git rm -r', stderr='fatal: not removing \'*.txt\'')
    assert(not match(command))


# Generated at 2022-06-14 10:19:45.396464
# Unit test for function match
def test_match():
    # Set up the command
    command = Command('git rm -rf')
    command.output = "fatal: not removing '" + \
                    "path/to/file" + \
                    "' recursively without -r"
    # Get correct result
    correct_result =  ' rm -r' in command.script \
                    and "fatal: not removing '" in command.output \
                    and "' recursively without -r" in command.output
    # Get result from the function
    result = match(command)
    # Assert the result
    assert(result == correct_result)


# Generated at 2022-06-14 10:19:54.400948
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm a') == 'git rm -r a'
    assert get_new_command('git rm a b c') == 'git rm -r a b c'
    assert get_new_command('git rm -r a') == 'git rm -r a'


# Generated at 2022-06-14 10:20:01.870011
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm path', 'fatal: not removing \'path\' recursively without -r')) == u'git rm -r path'

# Generated at 2022-06-14 10:20:05.181248
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_recursive_rm import get_new_command

    git_command = "git rm -rf"

    assert get_new_command(git_command) == "git rm -r -rf"

# Generated at 2022-06-14 10:20:07.608885
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf *', '', '', '')) == 'git rm -rf -r *'

# Generated at 2022-06-14 10:20:15.839984
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    from thefuck.rules.git_fatal_not_removing import get_new_command, match

    # test case 1: match is False
    command1 = Command(script='git rm file',
                        output='''fatal: not removing 'file' recursively without -r
                        ''')
    assert(match(command1) is False)

    # test case 2: match is True
    command2 = Command(script='git rm file',
                        output='''fatal: not removing 'file' recursively without -r
                        ''')
    assert(match(command2) is True)
    assert(get_new_command(command2) == 'git -r rm file')

# Generated at 2022-06-14 10:21:01.297612
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r directory', '', '')) == 'git rm -r -r directory'
    assert get_new_command(Command('git rm file', '', '')) == 'git rm -r file'
    assert get_new_command(Command('git rmdir directory', '', '')) == 'git rmdir -r directory'

# Generated at 2022-06-14 10:21:04.678913
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm a', '', 'fatal: not removing \'a\' recursively without -r')) == 'git rm -r a'

# Generated at 2022-06-14 10:21:07.927443
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(u'git rm file', u'fatal: not removing \'file\' recursively without -r')
    assert get_new_command(command) == u'git rm -r file'

# Generated at 2022-06-14 10:21:10.852915
# Unit test for function match
def test_match():
    assert match(Command(' git  rm  filea fileb ', 'fatal: not removing \'filea\' recursively without -r'))
    assert not match(Command(' git  rm  filea fileb ', ''))


# Generated at 2022-06-14 10:21:15.025645
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('git rm unsafe',
        is_correct=False, stderr='fatal: not removing \'unsafe\' recursively without -r'))
    assert new_command == 'git rm -r unsafe'

# Generated at 2022-06-14 10:21:17.458395
# Unit test for function match
def test_match():
    command = Command("git rm stuff/")
    assert match(command)
    assert not match(Command("git rm stuff"))


# Generated at 2022-06-14 10:21:20.803321
# Unit test for function get_new_command
def test_get_new_command():
    command = Script('git rm \'./a\'', 'fatal: not removing \'./a\' recursively without -r')
    assert get_new_command(command) == 'git rm -r \'./a\''

# Generated at 2022-06-14 10:21:26.431615
# Unit test for function get_new_command
def test_get_new_command():
    command_script = "git rm '/tmp/test_*m'"
    command_output = "fatal: not removing '/tmp/test_*m' recursively without -r"
    command = Command(script=command_script, output=command_output)
    assert get_new_command(command) == "git rm -r '/tmp/test_*m'"

# Generated at 2022-06-14 10:21:29.734463
# Unit test for function match
def test_match():
    assert match(Command('git rm filename',
                         '''error: unable to unlink old 'filename' (Permission denied)
fatal: not removing 'filename' recursively without -r
'''))



# Generated at 2022-06-14 10:21:31.520565
# Unit test for function get_new_command

# Generated at 2022-06-14 10:22:46.800564
# Unit test for function match
def test_match():
    assert match(Command("git rm foo"))


# Generated at 2022-06-14 10:22:56.777764
# Unit test for function match
def test_match():
    # assert match(command)
    command = make_command("git rm README")
    assert match(command)
    command = make_command("git rm README", output="fatal: not removing 'README' recursively without -r")
    assert match(command)
    command = make_command("git rm README", output="fatal: not removing 'README' recursively without -r", ignore_stderr=True)
    assert match(command)
    command = make_command("git rm README", output="fatal: not removing 'README' recursively without -r", ignore_stderr=False)
    assert match(command)
    command = make_command("git rm README", output="fatal: not removing 'README'", ignore_stderr=True)
    assert not match(command)


# Generated at 2022-06-14 10:23:02.598834
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command(script='git rm -f a.out',
                                   stderr='fatal: not removing \'a.out\' recursively without -r',
                                   stdout='Deleted a.out')) == 'git rm -r -f a.out'

# Generated at 2022-06-14 10:23:09.284249
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r C:\\Users\\Arvin Li\\Downloads\\test.txt', 'fatal: not removing \'C:\\Users\\Arvin Li\\Downloads\\test.txt\' recursively without -r')
    assert_equals(get_new_command(command), 'git rm -r -r C:\\Users\\Arvin Li\\Downloads\\test.txt')

# Generated at 2022-06-14 10:23:11.967460
# Unit test for function match
def test_match():
    assert match(Command(script='git rm'))
    assert not match(Command(script='git add'))


# Generated at 2022-06-14 10:23:18.279943
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf docs', 'fatal: not removing '
            '\'docs\' recursively without -r'))
    assert not match(Command('git rm docs', 'fatal: not removing '
            '\'docs\' recursively without -r'))


# Generated at 2022-06-14 10:23:21.718412
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf src', 'fatal: not removing \'src\' recursively without -r')) == 'git rm -rf -r src'

# Generated at 2022-06-14 10:23:30.088061
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert match(Command('git rm -r file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm', ''))
    assert not match(Command('git rm file', ''))
    assert not match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r',
        ''))


# Generated at 2022-06-14 10:23:42.549630
# Unit test for function match
def test_match():
    # case 1:
    test_case_1 = u"""git rm my-branch
error: The following untracked working tree files would be overwritten by merge:
    src/com/iflytek/cyber/evs/sdk/codec/tts/exception/TTSError.java
Please move or remove them before you merge.
Aborting
fatal: not removing 'src/com/iflytek/cyber/evs/sdk/codec/tts/exception/TTSError.java' recursively without -r
"""
    assert match(Command(script=u"git rm my-branch", output=test_case_1)) is True

    # case 2:

# Generated at 2022-06-14 10:23:51.878881
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', ''))
    # Test with paths with spaces
    assert match(Command(u'git rm "file 1"',
                u'fatal: not removing \'file 1\' recursively without -r'))
    assert not match(Command(u'git rm "file 1"', ''))
