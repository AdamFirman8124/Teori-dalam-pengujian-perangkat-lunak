

# Generated at 2022-06-14 10:14:02.629436
# Unit test for function match
def test_match():
    assert match(Command('git rm *.txt', 'fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command('git rm *.txt', 'fatal: not removing recursively without -r'))
    assert not match(Command('git rm file.txt', 'fatal: not removing \'file.txt\' recursively without -r'))
    assert not match(Command('echo', 'fatal: not removing \'file.txt\' recursively without -r'))
    

# Generated at 2022-06-14 10:14:04.692496
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test/')) == 'git rm -r test/'

# Generated at 2022-06-14 10:14:10.583720
# Unit test for function match
def test_match():
    assert match(Command('git rm *', 'fatal: not removing \'*\' recursively without -r'))
    assert not match(Command('git rm *', 'fatal: not removing \'*\' recursively without -r', 'Whatever'))
    assert not match(Command('git config --global user.name "John Doe"', '', ''))


# Generated at 2022-06-14 10:14:16.385248
# Unit test for function match
def test_match():
    # Test matching function
    assert match(Command('git rm -r abc'))
    assert not match(Command('git rm -r abc', ''))
    assert not match(Command('git rm abc', ''))
    assert not match(Command('git rm abc', ''))
    assert not match(Command('git rm', ''))


# Generated at 2022-06-14 10:14:22.377996
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm tests/test.py', 'fatal: not removing \'tests/test.py\' recursively without -r')
    matching = match(command)
    assert matching
    new_command = get_new_command(command)
    assert new_command == 'git rm -r tests/test.py'

# Generated at 2022-06-14 10:14:25.837656
# Unit test for function match
def test_match():
	command = Command('git branch | grep -v "master" | xargs git branch -D', 'fatal: not removing \'README.md\' recursively without -r')
	match(command) == True


# Generated at 2022-06-14 10:14:28.077530
# Unit test for function match
def test_match():
    assert match(u'git rm myfile')
    assert not match(u'git clone https:')


# Generated at 2022-06-14 10:14:32.895964
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm test',
                                  'fatal: not removing \'test\' recursively without -r\n'
                                  'Use --cached to keep the file, or make sure the file is removed from all tracked branches',
                                  '', False, 1)) == 'git rm -r test'

# Generated at 2022-06-14 10:14:44.294462
# Unit test for function match
def test_match():
    # Use only 'git' command
    assert match(Command('git rm -r', '', ''))
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r'))
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r\n'))
    assert not match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -i'))
    assert not match(Command('rm file', '', 'fatal: not removing \'file\' recursively without -i'))
    assert not match(Command('git file', '', 'fatal: not removing \'file\' recursively without -i'))


# Generated at 2022-06-14 10:14:47.773097
# Unit test for function match
def test_match():
    assert match(Command("git rm filename.txt",
                         "fatal: not removing 'filename.txt' recursively without -r"))
    assert not match(Command("git rm filename.txt", ""))


# Generated at 2022-06-14 10:14:59.295609
# Unit test for function match
def test_match():
    assert match(Command('git rm foo'))
    assert match(Command('git rm foo/'))
    assert match(Command('git rm --cached foo'))
    assert match(Command('git rm bar/foo'))
    assert not match(Command('git rm'))
    assert not match(Command('rm foo'))


# Generated at 2022-06-14 10:15:10.560393
# Unit test for function match
def test_match():
    assert match(Command('git rm com_box_service.h', 'fatal: not removing '
        "'com_box_service.h' recursively without -r",
        None, 'github.com/box/box-ios-sdk-v2_box-ios-sdk-v2'))
    assert match(Command('git rm README', 'fatal: not removing '
        "'README' recursively without -r",
        None, 'github.com/box/box-ios-sdk-v2_box-ios-sdk-v2'))

# Generated at 2022-06-14 10:15:14.805927
# Unit test for function get_new_command
def test_get_new_command():
    command_funct = get_new_command(command='git rm -rf directory1')
    assert command_funct == 'git rm -r -rf directory1'

# Generated at 2022-06-14 10:15:18.324758
# Unit test for function get_new_command
def test_get_new_command():
    actual = get_new_command(Command('git rm file.txt',
                                     'fatal: not removing \'file.txt\' recursively without -r',
                                     '', []))
    assert actual == 'git -r rm file.txt'

# Generated at 2022-06-14 10:15:21.401672
# Unit test for function match
def test_match():
    # test case doesn't work
    assert match(Command('git rm foo'))
    assert not match(Command('git rm -r foo'))


# Generated at 2022-06-14 10:15:29.792743
# Unit test for function match
def test_match():
    assert(match(Command('git rm -rf .idea',
                         'fatal: not removing \'.idea\' recursively without -r')))
    assert (not
            match(Command('git rm -rf .idea',
                          'fatal: not removing \'.idea\'')))
    assert (not
            match(Command('git rm -rf .idea',
                          'fatal: not removing \'.idea\' recursively with -r')))



# Generated at 2022-06-14 10:15:31.580541
# Unit test for function match
def test_match():
    a = Command('git rm foo.py')
    assert match(a) == False
    a = Command('git rm foo.py', 'fatal: not removing \'foo.py\' recursively without -r')
    assert match(a) == True


# Generated at 2022-06-14 10:15:34.356874
# Unit test for function match
def test_match():
    assert match(Script('git rm file'))
    assert match(Script('git rm -r file'))
    assert not match(Script('git clone https://github.com/nvbn/thefuck'))


# Generated at 2022-06-14 10:15:39.043864
# Unit test for function match
def test_match():
    assert match(Command('git rm a/b/c',
            "fatal: not removing 'a/b/c' recursively without -r",
            ''))
    assert not match(Command('git rm a/b/c',
            "fatal: not removing 'a/b/c' recursively without checking",
            ''))

# Generated at 2022-06-14 10:15:47.335487
# Unit test for function match
def test_match():
    from tests.utils import Command
    assert match(Command(script='git rm file',
                         output='fatal: not removing \'file\' recursively without -r'))
    assert not match(Command(script='git rm file',
                         output='fatal: not removing \'file\' recursively'))



# Generated at 2022-06-14 10:15:54.861987
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm a/b/c', 'fatal: not removing \'a/b/c\' recursively without -r')
    assert get_new_command(command) == 'git rm -r a/b/c'

# Generated at 2022-06-14 10:15:57.374824
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm ffffff") == "git -r rm ffffff"

# Generated at 2022-06-14 10:16:03.321635
# Unit test for function match
def test_match():
    command = Command('git rm foo',
                      'fatal: not removing \'foo\' recursively without -r\n',
                      '')
    assert match(command)
    command = Command('git rm foo', '', '')
    assert not match(command)
    command = Command('rm foo', '', '')
    assert not match(command)


# Generated at 2022-06-14 10:16:07.568851
# Unit test for function match
def test_match():
    assert match(Command('git branch | grep master', stderr='fatal: not removing ''/root/dev' '/recursively without -r'))
    assert not match(Command('git status', stderr="fatal: pathspec 'master' did not match any files"))


# Generated at 2022-06-14 10:16:18.938367
# Unit test for function match
def test_match():
    script1 = 'git rm -r filename'
    output1 = "fatal: not removing 'filename' recursively without -r"

    script2 = 'ls dirname'
    output2 = "fatal: not removing 'filename' recursively without -r"

    script3 = 'git rm filename'
    output3 = "fatal: not removing 'filename' recursively without -r"

    command1 = Command(script1, output1)
    command2 = Command(script2, output2)
    command3 = Command(script3, output3)

    assert match(command1)
    assert not match(command2)
    assert match(command3)


# Generated at 2022-06-14 10:16:23.250431
# Unit test for function match

# Generated at 2022-06-14 10:16:32.744929
# Unit test for function match
def test_match():
    assert match(Command('rm folder', 'fatal: not removing \'folder\' recursively without -r', ''))
    assert not match(Command('git rm folder', 'fatal: not removing \'folder\' recursively without -r', ''))
    assert not match(Command('git folder', 'fatal: not removing \'folder\' recursively without -r', ''))
    assert not match(Command('rm link', 'fatal: not removing \'link\' recursively without -r', ''))
    assert not match(Command('rm folder', 'fatal: not removing \'folder\' recursively without -r', ''))


# Generated at 2022-06-14 10:16:35.522692
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -r test.txt'

# Generated at 2022-06-14 10:16:37.684323
# Unit test for function match
def test_match():
    assert match(Command('git branch -D master', "fatal: not removing 'master' recursively without -r", None, 1))


# Generated at 2022-06-14 10:16:41.622297
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm foo', ''))
    assert not match(Command('git rm foo', 'fatal: not removing anything'))


# Generated at 2022-06-14 10:16:55.575174
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    assert get_new_command(Command("git rm foo", "", "fatal: not removing 'foo' recursively without -r")) == u"git rm -r foo"
    assert get_new_command(Command("git rm -r foo", "", "fatal: not removing 'foo' recursively without -r")) == u"git rm -r -r foo"

# Generated at 2022-06-14 10:17:02.267589
# Unit test for function match
def test_match():
    assert match(Script('git rm file', 'fatal: not removing \'folder\' recursively without -r\n'))

    assert not match(Script('git rm file', 'fatal: not removing \'\' recursively without -r\n'))
    assert not match(Script('git rm file', 'fatal: not removing \'folder\' recursively without -r'))
    assert not match(Script('git rm file', 'fatal: not removing \'\' recursively without -r'))
    assert not match(Script('git rm file', ''))

    assert not match(Script('ls file'))


# Generated at 2022-06-14 10:17:06.466539
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git rm -rf myfile', 'fatal: not removing \'/myfile\' recursively without -r'))
           == 'git rm -r -rf myfile')

# Generated at 2022-06-14 10:17:09.847287
# Unit test for function get_new_command
def test_get_new_command():
    import pytest
    assert u'git rm -r file' == get_new_command(Command(script='git rm file', output='fatal: not removing "file" recursively without -r'))

# Generated at 2022-06-14 10:17:13.609934
# Unit test for function get_new_command
def test_get_new_command():
    a = Command("git rm txt", "fatal: not removing 'txt' recursively without -r")
    b = get_new_command(a)
    assert(b == "git rm -r txt")

# Generated at 2022-06-14 10:17:15.818540
# Unit test for function match
def test_match():
    assert match(Command('git branch test; git rm test', "fatal: not removing 'test' recursively without -r"))
    assert not match(Command('git branch test; git rm -r test', "fatal: not removing 'test' recursively without -r"))


# Generated at 2022-06-14 10:17:19.422732
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file') == 'git rm -r file'
    assert get_new_command('git rm file1 file2') == 'git rm -r file1 file2'

# Generated at 2022-06-14 10:17:21.675320
# Unit test for function match
def test_match():
    assert match('git branch -d bug')
    assert not match('git rm')


# Generated at 2022-06-14 10:17:24.491280
# Unit test for function match
def test_match():
    assert match(Command('git rm -r src/file', ''))
    assert not match(Command('git rm src/file', ''))


# Generated at 2022-06-14 10:17:28.248495
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf dir/'))
    assert not match(Command('git rm dir/'))
    assert not match(Command('git rm -rf dir/', stderr='fatal: not removing directory'))


# Generated at 2022-06-14 10:17:49.645543
# Unit test for function get_new_command
def test_get_new_command():
    assert "git branch -D feature/foo" == get_new_command("git rm feature/foo")
    assert "git branch -D feature/bar" == get_new_command("git rm feature/bar")

# Generated at 2022-06-14 10:17:51.332041
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file', 'fatal: not removing \'file/\' recursively without -r\n', script_parts=['git', 'rm', 'file'])
    assert(get_new_command(command) == "git rm -r file")

# Generated at 2022-06-14 10:17:56.298320
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.specific.git import match
    import shlex
    command = type('cmd', (object,), {
        'script_parts': shlex.split('git rm file.txt'),
        'output': 'fatal: not removing \'file.txt\' recursively without -r'})
    assert get_new_command(command) == 'git rm -r file.txt'

# Generated at 2022-06-14 10:18:02.134400
# Unit test for function match
def test_match():
    assert match(Command('git rm test_file.py', 'fatal: not removing \'test_file.py\' recursively without -r\n'))
    assert not match(Command('ls', '\n'))
    assert not match(Command('git rm test_file.py', 'fatal: not removing \'test_file.py\''))


# Generated at 2022-06-14 10:18:05.681919
# Unit test for function match
def test_match():
    assert(match(Command('rm file',
                        'fatal: not removing \'file\' recursively without -r')))
    assert(not match(Command('rm file', '')))


# Generated at 2022-06-14 10:18:08.481775
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         u"fatal: not removing 'test/test_git.py' recursively without -r"))


# Generated at 2022-06-14 10:18:15.162346
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('git rm a',
                                   'fatal: not removing \'a\' recursively without -r')) == 'git rm -r a'
    assert get_new_command(Command('git rm -f a',
                                   'fatal: not removing \'a\' recursively without -r')) == 'git rm -f -r a'
    assert get_new_command(Command('git rm -f  a',
                                   'fatal: not removing \'a\' recursively without -r')) == 'git rm -f -r  a'
    assert get_new_command(Command('git rm a b',
                                   'fatal: not removing \'a\' recursively without -r')) == 'git rm -r a b'
    assert get_new_

# Generated at 2022-06-14 10:18:19.887302
# Unit test for function match
def test_match():
    assert match(Command('git rm non_existing', '', 'fatal: not removing \'non_existing\' recursively without -r'))
    assert not match(Command('git status', '', 'On branch master'))



# Generated at 2022-06-14 10:18:23.231736
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm foo') == 'git rm -r foo'
    assert get_new_command('git rm foo bar') == 'git rm -r foo bar'

# Generated at 2022-06-14 10:18:26.629690
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm 'a'", "fatal: not removing 'a' recursively without -r")) == "git rm -r 'a'"

# Generated at 2022-06-14 10:18:59.463317
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script = "git rm README.txt", output = "fatal: not removing 'README.txt' recursively without -r")) == "git rm -r README.txt"

# Generated at 2022-06-14 10:19:11.480005
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('git rm -f third.txt', ''))
    assert not match(Command('git rm -f third.txt', '', ''))
    assert not match(Command('git rm -f third.txt', '', '', ''))
    assert not match(Command('git rm -f third.txt', '', '', '', '', ''))
    assert not match(Command('git rm -f third.txt', '', '', '', '', '', ''))
    assert not match(Command('git rm -f third.txt', '', '', '', '', '', '', ''))
    assert not match(Command('git rm -f third.txt', '', '', '', '', '', '', '', ''))

# Generated at 2022-06-14 10:19:19.362560
# Unit test for function match
def test_match():
    assert match(Command('git rm test', 'fatal: not removing \'test\' recursively without -r\n'))
    assert not match(Command('git rm test', 'fatal: not removing \'test\' recursively without -r'))
    assert not match(Command('git rm test', 'fatal: not removing \'test\' recursively without\n -r'))
    assert not match(Command('git rm test', 'fatal: not removing \'test\' recursively without -r\n', 'git'))



# Generated at 2022-06-14 10:19:22.585973
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm test',
            stdout="fatal: not removing 'test' recursively without -r")) == "git rm -r test"

# Generated at 2022-06-14 10:19:30.381832
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm a') == u'git rm -r a'
    assert get_new_command('git rm -a') == u'git rm -r -a'
    assert get_new_command('git rm --a') == u'git rm -r --a'
    assert get_new_command('git rm -f') == u'git rm -r -f'
    assert get_new_command('git rm --force') == u'git rm -r --force'

# Generated at 2022-06-14 10:19:32.868765
# Unit test for function match
def test_match():
    command = Command('git rm toto', 'fatal: not removing \'toto\' recursively without -r')
    assert match(command)


# Generated at 2022-06-14 10:19:37.122929
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file', 'fatal: not removing ...')) == u'git rm -r file'
    assert get_new_command(Command('git rm -f *', 'fatal: not removing ...')) == u'git rm -f -r *'

# Generated at 2022-06-14 10:19:39.414859
# Unit test for function match
def test_match():
    assert match(Command('git rm filename' , 'fatal: not removing \'filename\' recursively without -r'))


# Generated at 2022-06-14 10:19:43.678399
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file1 file2 file3', 'fatal: not removing \'file2\' recursively without -r', '')) == 'git rm -r file1 file2 file3'

# Generated at 2022-06-14 10:19:52.467762
# Unit test for function match
def test_match():
    assert match(Command('git rm -r wrong.txt',
                         'fatal: not removing \'test/test_repo/wrong.txt\' recursively without -r\n'))



# Generated at 2022-06-14 10:20:57.550035
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r file', '')
    assert get_new_command(command) =='git rm -r -r file'



# Generated at 2022-06-14 10:21:00.462453
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm file.txt')
    assert(get_new_command(command)), 'git rm -r file.txt'

# Generated at 2022-06-14 10:21:03.828088
# Unit test for function match
def test_match():
    assert match(Command(' git rm a', 'fatal: not removing \'a\' recursively without -r', ''))
    assert not match(Command(' git rm a', '', ''))


# Generated at 2022-06-14 10:21:07.058927
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(command=MagicMock(script='git rm yolo', output="fatal: not removing 'yolo' recursively without -r")) == u'git rm -r yolo'

# Generated at 2022-06-14 10:21:11.073231
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm file',
                      stderr="fatal: not removing 'file' recursively without -r")
    new_command = get_new_command(command)
    assert new_command == "git rm -r file"


# Generated at 2022-06-14 10:21:19.579996
# Unit test for function get_new_command
def test_get_new_command():
    test_cases = (
        (Command('git rm -r', 'fatal: not removing \'filename\' recursively without -r', '', 0), 'git rm -r -r'),
        (Command('git status', 'fatal: not removing \'filename\' recursively without -r', '', 0), None),
    )

    for test_case, expected_result in test_cases:
        with patch('thefuck.specific.git.git_support', return_value=True):
            assert expected_result == get_new_command(test_case)


# Generated at 2022-06-14 10:21:27.759097
# Unit test for function match
def test_match():
    strings = [' git rm -f splash.jpg', ' git status', ' echo 1']
    fails = [' git rm splash.jpg', ' git rm -r splash.jpg']
    for s in strings:
        assert match(Command(s, s + 'fatal: not removing \'splash.jpg\' recursively without -r'))
    for s in fails:
        assert not match(Command(s, s + 'fatal: not removing \'splash.jpg\' recursively without -r'))


# Generated at 2022-06-14 10:21:38.314024
# Unit test for function match
def test_match():
    assert match(Command(script='git rm', output='fatal: not removing \'.gitignore\' recursively without -r\n'))
    assert match(Command(script='git rm', output='fatal: not removing \'foo\' recursively without -r\n'))
    assert not match(Command(script='git rm', output='fatal: not removing \'foo\' without -r\n'))
    assert not match(Command(script='git rm', output=''))
    assert not match(Command(script='ls', output=''))


# Generated at 2022-06-14 10:21:42.609114
# Unit test for function match
def test_match():
    assert match(Command('git rm test', 'fatal: not removing \'test\' recursively without -r', ''))
    assert not match(Command('git rm src', '', ''))
    assert not match(Command('git rm -r src', '', ''))


# Generated at 2022-06-14 10:21:45.943075
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm file.txt') == 'rm -r file.txt'
    assert get_new_command('rm -f file.txt') == 'rm -f -r file.txt'