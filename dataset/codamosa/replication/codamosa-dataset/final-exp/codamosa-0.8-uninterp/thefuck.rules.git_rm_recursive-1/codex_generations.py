

# Generated at 2022-06-14 10:14:01.187347
# Unit test for function match
def test_match():
    command = Command('git rm -f filename', 'fatal: not removing \'"filename\'" recursively without -r')
    assert(match(command))


# Generated at 2022-06-14 10:14:04.313620
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r')
    assert get_new_command(command) == 'git rm -r foo'

# Generated at 2022-06-14 10:14:07.340847
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm src', 'fatal: not removing \'src\' recursively without -r', '')) == 'git rm -r src'

# Generated at 2022-06-14 10:14:11.325568
# Unit test for function get_new_command
def test_get_new_command():
    from unittest.mock import Mock
    GitCommand = make_command('git status', 'fatal: not removing \'file\' recursively without -r')
    assert get_new_command(GitCommand) == 'git status && git rm -r file'

# Generated at 2022-06-14 10:14:19.494117
# Unit test for function match
def test_match():
    assert git_rm_r.match(Command('git rm -r a b',
                                  'fatal: not removing \'a\' recursively without -r'))
    assert git_rm_r.match(Command('git rm a b',
                                  'fatal: not removing \'a\' recursively without -r'))
    assert not git_rm_r.match(Command('git rm a b', ''))
    assert not git_rm_r.match(Command('rm a b',
                                      'fatal: not removing \'a\' recursively without -r'))


# Generated at 2022-06-14 10:14:22.672252
# Unit test for function match
def test_match():
    assert match(Command('rm foo', '', 'fatal: not removing \'foo\' recursively without -r'))



# Generated at 2022-06-14 10:14:24.550941
# Unit test for function get_new_command
def test_get_new_command():
  command = Command('git rm -rf file1 file2')
  new_command = get_new_command(command)
  assert new_command == u'git rm -r -rf file1 file2', new_command

# Generated at 2022-06-14 10:14:27.840609
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm app/models/user.rb") == "git rm -r app/models/user.rb"

# Generated at 2022-06-14 10:14:38.722474
# Unit test for function match
def test_match():
	# Test example from error message
	assert match(u'$ git rm a b c\nfatal: not removing \'a\' recursively without -r\n')
	assert not match(u'$ git rm a b c\nfatal: you can\'t do that\n')
	assert not match(u'$ git rm a b c\nfatal: not removing \'a\' recursively without -e\n')
	assert not match(u'$ git rm a b c\nfatal: not removing \'a\' recursively without -r (mismatch in pattern)\n')
	assert not match(u'$ git rm a b c\nfatal: not removing \'a\' recursively with -r\n')

# Generated at 2022-06-14 10:14:41.310296
# Unit test for function match
def test_match():
    assert(match(Command('git rm lorem/ipsum')) == 0)


# Generated at 2022-06-14 10:14:47.557235
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git foo', 'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('git rm', 'fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command('foo', 'fatal: not removing \'foo\' recursively without -r'))


# Generated at 2022-06-14 10:15:02.109661
# Unit test for function match
def test_match():
    assert(match(Command(' git rm File',
                  stderr='fatal: not removing \'File\' recursively without -r\n')))
    assert (match(Command(' git rm -rf File',
                   stderr='fatal: not removing \'File\' recursively without -r\n')))
    assert (not match(Command('git rm File2',
                      stderr='fatal: not removing \'File\' recursively without -r\n')))
    assert (not match(Command(' git checkout branchname',
                      stderr='fatal: not removing \'File\' recursively without -r\n')))


# Generated at 2022-06-14 10:15:05.862749
# Unit test for function match
def test_match():
    assert match(Command('rm file1 file2 file3', 'fatal: not removing \'file1\' recursively without -r'))
    assert not match(Command('rm file1 file2 file3', ''))
    assert not match(Command('cat file1 file2 file3', ''))


# Generated at 2022-06-14 10:15:07.762374
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm dir/') == 'git rm -r dir/'

# Generated at 2022-06-14 10:15:15.922720
# Unit test for function match
def test_match():
    # Simple test
    assert match(Command('git rm test.txt',
                         'fatal: not removing \'test.txt\' recursively without -r\n'))

    # Test if we match only with the right output
    assert not match(Command('git rm test.txt',
                             'fatal: not removing \'test.txt\' recursively without -r\n'
                             'fatal: pathspec \'test.txt2\' did not match any files'))


# Generated at 2022-06-14 10:15:19.322942
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git rm nonexistent_file'
    output = 'fatal: not removing \'nonexistent_file\' recursively without -r\n'
    assert get_new_command(Command(command, output)) == 'git rm -r nonexistent_file'

# Generated at 2022-06-14 10:15:22.625949
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_rm import get_new_command
    assert get_new_command(Command('git rm -f', 
                                   'fatal: not removing \'.gitignore\' recursively without -r')) == 'git rm -rf'

# Generated at 2022-06-14 10:15:27.819934
# Unit test for function get_new_command
def test_get_new_command():
        s = 'git rm -rf new_folder'
        c = Command(s, '/tmp/')
        c.script_parts = s.split(' ')
        assert get_new_command(c) == 'git rm -rf -r new_folder'

# Generated at 2022-06-14 10:15:31.224964
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command(script='git rm file1 file2 file3',
        stderr='fatal: not removing \'file2\' recursively without -r')) ==
        'git rm -r file1 file2 file3')

# Generated at 2022-06-14 10:15:36.957541
# Unit test for function match
def test_match():
    assert match(Command(' rm -r dir1/dir2', '', 'fatal: not removing \'dir1/dir2\' recursively without -r'))
    assert not match(Command(' rm -r dir1/dir2', '', 'fatal: not removing \'dir1/dir2\' recursively'))
    assert not match(Command(' rm dir1/dir2', '', 'fatal: not removing \'dir1/dir2\' recursively without -r'))


# Generated at 2022-06-14 10:15:50.051714
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm gitsubmodule.use.submodule.example.com.git",
                                   "fatal: not removing 'gitsubmodule.use.submodule.example.com.git' recursively without -r",
                                   0)) == "git rm -r gitsubmodule.use.submodule.example.com.git"

# Generated at 2022-06-14 10:15:54.492528
# Unit test for function match
def test_match():
    assert match(Command('git rm *.tmp',
                         'fatal: not removing \'file.tmp\' recursively without -r',
                         ''))
    assert not match(Command('git rm file.tmp',
                             "rm 'file.tmp'",
                             ''))

# Generated at 2022-06-14 10:16:02.307852
# Unit test for function match
def test_match():
    # Test for positive match
    output1 = "fatal: not removing 'repo' recursively without -r\n"
    command1 = Command('git rm -rf repo', output=output1)
    assert match(command1)

    # Test for negative match
    output2 = "fatal: not removing 'repo'\n"
    command2 = Command('git rm -rf repo', output=output2)
    assert not match(command2)



# Generated at 2022-06-14 10:16:07.502914
# Unit test for function get_new_command
def test_get_new_command():
    # git command: git rm file2 file3 -f
    # Error: fatal: not removing 'file2' recursively without -r
    command = Command('git rm file2 file3 -f', 'fatal: not removing \'file2\' recursively without -r')
    assert get_new_command(command) == 'git rm -r file2 file3 -f'

# Generated at 2022-06-14 10:16:10.273266
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file')) == 'git rm -r file'



# Generated at 2022-06-14 10:16:13.767354
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r test', 'fatal: not removing test recursively without -r')) == 'git rm -r -r test'

# Generated at 2022-06-14 10:16:17.923499
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm path/to/file',
                           output="fatal: not removing 'path/to/file' recursively without -r")) == 'git rm -r path/to/file'

# Generated at 2022-06-14 10:16:22.600905
# Unit test for function match
def test_match():
    command = Command('git rm -b index.html', 'fatal: not removing \'index.html\' recursively without -r')
    assert match(command)

    command = Command('git rm index.html', 'fatal: not removing \'index.html\' recursively without -r')
    assert match(command)


# Generated at 2022-06-14 10:16:25.245591
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm hello', 'fatal: not removing \'hello\' recursively without -r')) == 'git rm -r hello'

# Generated at 2022-06-14 10:16:28.528210
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm') == 'git rm -r'
    assert get_new_command('git rm -a') == 'git rm -a -r'

# Generated at 2022-06-14 10:16:35.205940
# Unit test for function match
def test_match():
    output = "fatal: not removing 'tests/example.py' recursively without -r"
    command = Command('git rm tests/example.py', output)
    assert match(command) is True


# Generated at 2022-06-14 10:16:40.168300
# Unit test for function match
def test_match():
    assert match(Command('rm -r app', "fatal: not removing 'app' recursively without -r"))
    assert not match(Command('rm app', "fatal: not removing 'app' recursively without -r"))
    assert not match(Command('rm -r app', "fatal: not removing 'app' recursively without -r", False))



# Generated at 2022-06-14 10:16:50.407934
# Unit test for function match
def test_match():
    with patch('thefuck.rules.git_rmdir.git_support', return_value=False):
        assert match(Command('rm -r', '')) == False
        assert match(Command('rm -r', 'fatal: not removing '' recursively without -r')) == False
        assert match(Command('rm -r', 'fatal: not removing '' recursively without -r')) == False
    with patch('thefuck.rules.git_rmdir.git_support', return_value=True):
        assert match(Command('rm', '')) == False
        assert match(Command('rm -r', '')) == False
        assert match(Command('rm -r ', 'fatal: not removing ' ' recursively without -r')) == True



# Generated at 2022-06-14 10:16:53.404019
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git status', script='git rm -r foo/')) == 'git rm -r -r foo/'


# Generated at 2022-06-14 10:16:58.598936
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm test', '', '')
    assert get_new_command(command) == 'git rm -r test'

    command = Command('git rm test', '', '')
    assert get_new_command(command) == 'git rm -r test'


enabled_by_default = True

# Generated at 2022-06-14 10:17:02.967885
# Unit test for function match
def test_match():
    assert match(
        Command('git rm test.txt', '', 'fatal: not removing \'test.txt\' recursively without -r'))
    assert not match(Command('git rm test.txt', '', ''))
    assert not match(Command('git mv test.txt', '', ''))

# Generated at 2022-06-14 10:17:11.293853
# Unit test for function match
def test_match():
    assert match(Command('git rm file1', 'fatal: not removing \'test/test_match.py\' recursively without -r'))
    assert not match(Command('git rm file1', 'fatal: not removing \'test/test_match.py\' recursively without -r', error=True))
    assert not match(Command('git rm file1', ''))
    assert not match(Command('git pull', 'fatal: not removing \'test/test_match.py\' recursively without -r', error=True))


# Generated at 2022-06-14 10:17:14.110089
# Unit test for function match
def test_match():
    assert match(Command('git rm directory',
                         stderr='fatal: not removing \'directory\' recursively without -r'))

# Generated at 2022-06-14 10:17:17.615243
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('fatal: not removing \'file.txt\' recursively without -r',
                      'git rm file.txt')
    assert get_new_command(command) == 'git rm -r file.txt'

# Generated at 2022-06-14 10:17:27.373666
# Unit test for function match
def test_match():
    assert match(Command(script='git rm foo', output="fatal: not removing 'foo' recursively without -r"))
    assert match(Command(script='git rm -r foo', output="fatal: not removing 'foo' recursively without -r"))
    assert not match(Command(script='git foo', output="fatal: not removing 'foo' recursively without -r"))
    assert not match(Command(script='git rm foo', output="fatal: not removing"))
    assert not match(Command(script='git rm foo', output="fatal: not removing 'foo' recursively without -r"), requires_output=False)


# Generated at 2022-06-14 10:17:41.534594
# Unit test for function match
def test_match():
    for x in ['git rm src/abc.py', 'git rm -r src/abc.py', 'git rm -rf src/abc.py']:
        assert not match(Command(script=x))

    for x in ['git rm src/abc.py', 'git rm -r src/abc.py', 'git rm -rf src/abc.py']:
        assert match(Command(script=x, output='''fatal: not removing 'src/abc.py' recursively without -r'''))



# Generated at 2022-06-14 10:17:56.079684
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm test") == "git rm -r test"
    assert get_new_command("git rm test test2") == "git rm -r test test2"
    assert get_new_command("git rm test/") == "git rm -r test/"
    assert get_new_command("git rm test/ test2/") == "git rm -r test/ test2/"
    assert get_new_command("git rm test/ test2/ test3") == "git rm -r test/ test2/ test3"
    assert get_new_command("git rm test/ test2/ test3") == "git rm -r test/ test2/ test3"
    assert get_new_command("git rm test/\'test2") == "git rm -r test/\'test2"


# Generated at 2022-06-14 10:18:00.459731
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo.txt', 'fatal: not removing \'foo.txt\''
            ' recursively without -r')

    assert git_rm.get_new_command(command) == 'git rm -r foo.txt'



# Generated at 2022-06-14 10:18:04.966380
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ['git', 'rm', 'file']
    index = command_parts.index('rm') + 1
    command_parts.insert(index, '-r')

    assert get_new_command('git rm file') == u'git rm -r file'

# Generated at 2022-06-14 10:18:16.563419
# Unit test for function match
def test_match():
    # git rm -rf .gitignore
    assert match(Command('git rm -rf .gitignore',
                  '/home/lizkak/py_projects/git_challenges', '', '',
                  'fatal: not removing \'.gitignore\' recursively without -r'))
    # git rm -rf .gitignore -r
    assert not match(Command('git rm -rf .gitignore -r',
                  '/home/lizkak/py_projects/git_challenges', '', '',
                  'fatal: not removing \'.gitignore\' recursively without -r'))
    # git rm -rf gitignore

# Generated at 2022-06-14 10:18:22.490279
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm foo') == 'git rm -r foo'
    assert get_new_command('git rm -f foo') == 'git rm -f -r foo'
    assert get_new_command('git rm --cached foo') == 'git rm --cached -r foo'

# Generated at 2022-06-14 10:18:27.985818
# Unit test for function get_new_command
def test_get_new_command():
    command = shell.and_("git rm bad_file  && git commit -m 'test'", "fatal: not removing 'bad_file' recursively without -r")
    assert get_new_command(command) == u"git rm -r bad_file && git commit -m 'test'"

# Generated at 2022-06-14 10:18:35.327317
# Unit test for function match
def test_match():
    assert match(Command('git rm test/file', "FROM: \":foo.bar\"\n",
                        ""))
    assert not match(Command('git log', "", ""))
    assert not match(Command('git rm test/file', "",
                             "fatal: not removing '"
                             + "test/file"
                             + "' recursively without -r"))
    assert match(Command('git rm test/file', "",
                         "fatal: not removing '"
                         + "test/file"
                         + "' recursively without -r"))


# Generated at 2022-06-14 10:18:38.420984
# Unit test for function match
def test_match():
    assert match(Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r\n', ''))



# Generated at 2022-06-14 10:18:43.447979
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
        "fatal: not removing 'file' recursively without -r"))
    assert not match(Command('git rm file',
        "fatal: not removing 'file' recursively without -r"))



# Generated at 2022-06-14 10:18:55.954588
# Unit test for function get_new_command
def test_get_new_command():
    result = get_new_command(Command('git rm -f aa.txt', 
                             'fatal: not removing \'aa.txt\' recursively without -r'))
    assert result == 'git rm -r -f aa.txt'

# Generated at 2022-06-14 10:19:03.771062
# Unit test for function match
def test_match():
    # rm git command
    assert match(Command('rm -rf .',
                'fatal: not removing \'.\' recursively without -r\n'))

    # no rm git command
    assert not match(Command('rm .',
                    'fatal: not removing \'.\' recursively without -r\n'))

    # rm git command, but wrong error output
    assert not match(Command('rm -rf .',
                    'fatal: not removing \'.as\' recursively without -r\n'))

    # rm git command, but wrong error output
    assert not match(Command('rm -rf .',
                    'fatal: not removing \'.\' recursively without -r\n'))



# Generated at 2022-06-14 10:19:06.990506
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r dir')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r -r dir'

# Generated at 2022-06-14 10:19:11.631246
# Unit test for function get_new_command
def test_get_new_command():
    from tests.types import Command
    assert_equals(get_new_command(Command.from_text('git rm foo/bar')), 'git rm -r foo/bar')
    assert_equals(get_new_command(Command.from_text('git rm foo bar')), 'git rm foo -r bar')

# Generated at 2022-06-14 10:19:13.790415
# Unit test for function match
def test_match():
    assert match(Command('git rm -R',
                         'fatal: not removing "file" recursively without -r'))


# Generated at 2022-06-14 10:19:21.461601
# Unit test for function get_new_command

# Generated at 2022-06-14 10:19:24.656179
# Unit test for function match
def test_match():
    assert match(
        Command('rm —e dirname dirother', '', 'fatal: not removing '' recursively without -r'))


# Generated at 2022-06-14 10:19:28.145048
# Unit test for function match
def test_match():
    assert match(Command('git rm TEST.txt', output='fatal: not removing \'TEST.txt\' recursively without -r'))
    assert not match(Command('git rm TEST.txt', output='fatal: not removing \'TEST.txt\''))


# Generated at 2022-06-14 10:19:33.458627
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm -A", "fatal: not removing 'src/file.cpp' recursively without -r")
    assert get_new_command(command) == "git rm -r -A"
    command = Command("git rm -A", "fatal: not removing './src/file.cpp' recursively without -r")
    assert get_new_command(command) == "git rm -r -A"

# Generated at 2022-06-14 10:19:42.116647
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r git-annex/objects/SHA256E-s8--7e4c4e55d717a8a078b7ba1d04fdd07a87ac96535b0a2ef004db0d3fb13bd765.bin', '')
    assert get_new_command(command) == 'git rm -r -r git-annex/objects/SHA256E-s8--7e4c4e55d717a8a078b7ba1d04fdd07a87ac96535b0a2ef004db0d3fb13bd765.bin'

# Generated at 2022-06-14 10:20:00.993263
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf foo')) == u'git rm -r -rf foo'
    assert get_new_command(Command('git rm -r foo')) == u'git rm -r -r foo'
    assert get_new_command(Command('git rm -f foo')) == u'git rm -r -f foo'
    assert get_new_command(Command('git rm -rf --cached foo')) == u'git rm -r -rf --cached foo'
    assert get_new_command(Command('git rm --cached foo')) == u'git rm -r --cached foo'
    assert get_new_command(Command('git rm foo')) == u'git rm -r foo'

# Generated at 2022-06-14 10:20:04.410934
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
             "fatal: not removing 'file' recursively without -r"))


# Generated at 2022-06-14 10:20:08.140638
# Unit test for function get_new_command
def test_get_new_command():
    assert "git rm -r" in get_new_command(Command("git rm TEST_FILE",
            "fatal: not removing 'TEST_FILE' recursively without -r\n",
            "/home/user/git"))

# Generated at 2022-06-14 10:20:15.511464
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.main import create_command
    output = "fatal: not removing 'src/main/java/edu/stanford/nlp/pipeline/MorphologyAnnotator.java' recursively without -r"
    command = create_command('git rm src/main/java/edu/stanford/nlp/pipeline/MorphologyAnnotator.java', output)
    new_command = get_new_command(command)
    assert new_command == 'git rm -r src/main/java/edu/stanford/nlp/pipeline/MorphologyAnnotator.java'

# Generated at 2022-06-14 10:20:21.517966
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script = 'git rm file.txt'
    output = ('fatal: not removing \'file.txt\' recursively without -r\n'
              'Did you mean this?\n'
              '\tgit rm --cached file.txt')

    command = Command(script, output)

    assert get_new_command(command) == 'git rm -r file.txt'

# Generated at 2022-06-14 10:20:29.737499
# Unit test for function match
def test_match():
    assert match(Command(script='git rm filename.txt', output='fatal: not removing \' filename.txt\' recursively without -r'))
    assert not match(Command(script='git rm filename.txt', output='fatal: not removing \'filename.txt\' recursively without -r'))
    assert not match(Command(script='git rm filename.txt', output='fatal: not removing \'filename.txt\' recursively without -r',
    stderr='fatal: not removing \'filename.txt\' recursively without -r'))


# Generated at 2022-06-14 10:20:33.331219
# Unit test for function get_new_command
def test_get_new_command():
    print("Testing get_new_command()")
    assert get_new_command("git rm -r foo bar txt") == "git rm -r -r foo bar txt"


# Generated at 2022-06-14 10:20:37.638804
# Unit test for function get_new_command
def test_get_new_command():
    index = u'fatal: not removing \'src\' recursively without -r'
    command = u'git rm src'
    new_command = get_new_command(Command(command, index))
    assert new_command == u'git rm -r src'


# Generated at 2022-06-14 10:20:44.782824
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf foo',
                                   'fatal: not removing \'foo\' recursively without -r\n')) == 'git rm -rf -r foo'
    assert get_new_command(Command('git rm bar',
                                   'fatal: not removing \'bar\' recursively without -r\n')) == 'git rm -r bar'

# Generated at 2022-06-14 10:20:49.495454
# Unit test for function match
def test_match():
    assert match(Command('git rm -f'))
    assert not match(Command('git add -f'))


# Generated at 2022-06-14 10:21:10.632813
# Unit test for function match
def test_match():
    assert match("git rm tmp.txt")
    assert match("git rm   ")
    assert match("git rm")
    assert match("git rm tmp.txt  ")
    assert match("git rm tmp.txt ")
    assert not match("git rm")
    assert not match("git")
    assert not match("git rm tmp.txt")
    assert not match("git rm tmp.txt")


# Generated at 2022-06-14 10:21:15.735373
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf', '', 'fatal: not removing '
                                          "'dir/file' recursively without -r"))
    assert not match(Command('git rm -rf', '', 'fatal: not removing '
                                          "'dir' recursively without -r"))


# Generated at 2022-06-14 10:21:22.138493
# Unit test for function match
def test_match():
    """Check if match function works as expected"""
    assert match(Command(script='git rm file',
                         output='fatal: not removing \'file\' recursively without -r'))
    assert not match(Command(script='git rm file',
                         output='fatal: could not open file'))
    assert not match(Command(script='git',
                         output='fatal: not removing \'file\' recursively without -r'))


# Generated at 2022-06-14 10:21:26.089793
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm -r',
                      output="fatal: not removing 'a' recursively without -r\n")

    new_command = get_new_command(command)
    assert new_command == 'git rm -r -r'

# Generated at 2022-06-14 10:21:28.257842
# Unit test for function match
def test_match():
    assert match(Command('git rm fred', 'fatal: not removing '
                                       "'fred' recursively without -r", ''))

# Generated at 2022-06-14 10:21:33.622841
# Unit test for function match
def test_match():
    assert match(Command(script='git rm a/b/c',
                         output="fatal: not removing 'a/b/c' recursively without -r"))
    assert not match(Command(script='git rm a/b/c',
                             output="fatal: not removing 'a/b/c' recursively"))


# Generated at 2022-06-14 10:21:34.705849
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git") == 'git'

# Generated at 2022-06-14 10:21:38.653104
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm hello.txt",
                      "fatal: not removing 'hello.txt' recursively without -r")
    assert get_new_command(command) == "git rm -r hello.txt"

# Generated at 2022-06-14 10:21:44.254100
# Unit test for function match
def test_match():
    assert match(Command(' git rm makefile',
                         "error: unable to stat 'makefile': Permission denied"))
    assert not match(Command('git rm makefile',
                             "error: unable to stat 'makefile': Permission denied"))
    assert not match(Command(' git rm  makefi',
                         "error: unable to stat 'makefile': Permission denied"))



# Generated at 2022-06-14 10:21:46.094724
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(command='git rm file.txt') == 'git rm -r file.txt')

# Generated at 2022-06-14 10:22:27.608811
# Unit test for function get_new_command
def test_get_new_command():
    # Setup mock script
    script = 'git rm file'
    # Setup mocks
    output = 'fatal: not removing \'file\' recursively without -r'
    # Execute
    command = Command(script, output)
    # Check
    assert get_new_command(command) == 'git rm -r file'


# Generated at 2022-06-14 10:22:33.946854
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm -rf "file with spaces"'
    output = "fatal: not removing 'file with spaces' recursively without -r"
    command = Command(script, output)
    assert get_new_command(command) == script + ' -r'

    script = 'git rm "file with spaces"'
    output = "fatal: not removing 'file with spaces' recursively without -r"
    command = Command(script, output)
    assert get_new_command(command) == script + ' -r'

# Generated at 2022-06-14 10:22:40.686242
# Unit test for function match
def test_match():
    assert match(Command('git rm README', 'fatal: not removing \'README\' recursively without -r'))
    assert not match(Command('git rm README', ''))
    assert match(Command('git rm README', 'fatal: not removing \'README\' recursively without -r', '', 3))
    assert not match(Command('rm README', 'fatal: not removing \'README\' recursively without -r', '', 3))


# Generated at 2022-06-14 10:22:44.731741
# Unit test for function match
def test_match():
    assert match(Command('git rm hello'))
    assert not match(Command('git', 'rm', 'hello'))
    assert not match(Command('rm hello', 'Fatal: not removing'))


# Generated at 2022-06-14 10:22:46.327834
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm README',
                                   'fatal: not removing \'README\' recursively without -r')) == 'git rm -r README'

# Generated at 2022-06-14 10:22:50.666289
# Unit test for function get_new_command
def test_get_new_command():
    match_command = Command("git rm -f foo bar", "fatal: not removing 'foo' recursively without -r\n")

    assert "git rm -f -r foo bar" == get_new_command(match_command)

# Generated at 2022-06-14 10:22:55.222527
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm abc')) == 'git rm -r abc'
    assert get_new_command(Command('git remote rm abc')) == 'git remote rm abc'
    assert get_new_command(Command('git remote add abc')) == 'git remote add abc'

# Generated at 2022-06-14 10:22:57.382426
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -f')) == 'git rm -rf'

# Generated at 2022-06-14 10:23:06.463581
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r\n',
                         '/bin/git'))
    assert match(Command('git rm -r file',
                         'fatal: not removing \'file\' recursively without -r\n',
                         '/bin/git'))
    assert not match(Command('git add', '', '/bin/git'))
    assert not match(Command('rm -r dir', '', '/bin/rm'))



# Generated at 2022-06-14 10:23:08.820746
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script="git rm bla.txt", stdout=GIT_RM_STDOUT)
    assert get_new_command(command) == "git rm -r bla.txt"

# Generated at 2022-06-14 10:23:51.794415
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm -r foo') == 'git rm -r -r foo'

# Generated at 2022-06-14 10:23:56.800292
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', 'fatal: not removing \'foo/bar\' recursively without -r'))
    assert not match(Command('git rm foo', 'fatal: not removing \'bar\' recursively without -r'))
    assert not match(Command('git rm foo', ''))
