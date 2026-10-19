

# Generated at 2022-06-14 10:13:53.780916
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm non-empty-directory', '', '')) == 'git rm -r non-empty-directory'

# Generated at 2022-06-14 10:13:57.786317
# Unit test for function match
def test_match():
    assert match(Command('git rm file -r',
                         'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file -f', ''))


# Generated at 2022-06-14 10:14:00.108622
# Unit test for function get_new_command
def test_get_new_command():
	new_command = get_new_command(command.Command('git rm -r'))
	assert new_command == 'git rm -r -r'

# Generated at 2022-06-14 10:14:02.170093
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(' git rm testfile') == 'git rm -r testfile'

# Generated at 2022-06-14 10:14:06.658109
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm some_file', 'fatal: not removing \'some_file\' recursively without -r\n')
    new_command = get_new_command(command)
    assert new_command == 'git rm -r some_file'


# Generated at 2022-06-14 10:14:10.249226
# Unit test for function match
def test_match():
    assert match(Command('git rm filename', 'Error msg'))
    assert not match(Command('git rm  -r filename'))
    assert not match(Command('git rm  -n filename'))


# Generated at 2022-06-14 10:14:13.450283
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -rf test')
    assert get_new_command(command) == 'git rm -rf -r test'

# Generated at 2022-06-14 10:14:23.645961
# Unit test for function match
def test_match():
    match_checker = re.compile(' rm ')
    
    # Tested function has to return False if no match
    assert(match(Command('git commit -m "some message"', 
                        'some output', 'some error', 0)) == None)
    # Tested function has to return False if no match
    assert(match(Command('git commit -m "some message"', 
                        'fatal: not removing', 'some error', 0)) == None)
    assert(match(Command('git commit -m "some message"', 
                        'fatal: not removing "somefile" recursively without -r', 
                        'some error', 0)) == None)
    # Tested function has to return True if it matches

# Generated at 2022-06-14 10:14:26.776372
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script = 'git rm')) == 'git rm -r'

# Generated at 2022-06-14 10:14:35.281415
# Unit test for function match
def test_match():
    assert match(Command('git rm a',
            "fatal: not removing 'a' recursively without -r",
            ''))
    assert not match(Command('git rm a',
            "fatal: blah blah blah 'a' recursively without -r",
            ''))
    assert not match(Command('git rm a',
            "fatal: not removing 'a recursively without -r",
            ''))
    assert not match(Command('git rm a',
            "fatal: not removing 'a' recursively without -r",
            '',
            ))


# Generated at 2022-06-14 10:14:39.408702
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm testfile', 'fatal: not removing \'testfile\' recursively without -r')) == 'git rm -r testfile'
    assert get_new_command(Command('rm testfile', '')) == 'git rm testfile'

# Generated at 2022-06-14 10:14:42.467823
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm -rf /', 'fatal: not removing \'/\' recursively without -r', '')) == 'git rm -r -rf /'

# Generated at 2022-06-14 10:14:50.373469
# Unit test for function match
def test_match():
  # rule for match
  assert match(Command("git rm * -r", u"""fatal: not removing 'lib/application/assets/javascripts/lib/jquery-ui.js' recursively without -r
  rm 'lib/application/assets/javascripts/lib/jquery-ui.js'""", "C:\\Users\\ming\\Desktop\\project"))

  # rule for not match
  assert not match(Command("git rm * -r", u"""""", "C:\\Users\\ming\\Desktop\\project"))


# Generated at 2022-06-14 10:14:58.809006
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
    			u"error: unable to unlink old 'file' (Permission denied)\n"
        		"fatal: not removing 'file' recursively without -r",
    			None, None, None, '', '')) == True


# Generated at 2022-06-14 10:15:03.931707
# Unit test for function get_new_command
def test_get_new_command():
    output = u'fatal: not removing \'file\' recursively without -r\n'
    command = Command('git rm file', output)
    assert get_new_command(command) == "git rm -r file"


# Generated at 2022-06-14 10:15:05.891299
# Unit test for function match
def test_match():
    assert match(Command('git rm file'))
    assert not match(Command('git mv file'))


# Generated at 2022-06-14 10:15:12.238978
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.specific.git import git_support
    assert git_support()
    assert get_new_command(
        Command('git rm test.txt', 'fatal: not removing '
                +"'test.txt' recursively without -r\nDid you mean 'rm'?\n",
                '')
        ) == 'git rm -r test.txt'

# Generated at 2022-06-14 10:15:17.318047
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm file') == 'git rm -r file'
    assert get_new_command('git rm -r file') == 'git rm -r file'
    assert get_new_command('git rm -r') == 'git rm -r -r'

# Generated at 2022-06-14 10:15:21.363266
# Unit test for function get_new_command
def test_get_new_command():
    # Testing positive match, with correct expected output
    command = Command("git rm path/to/file.txt", "")

    assert match(command)
    assert get_new_command(command) == "git rm -r path/to/file.txt"

# Generated at 2022-06-14 10:15:28.241834
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ["git", "rm", "--cached", "file.conf"]
    assert(get_new_command(Command(script=' '.join(command_parts),
                                   script_parts=command_parts,
                                   output='fatal: not removing '
                                   "'file.conf' recursively without -r")) == 'git rm -r --cached file.conf')

# Generated at 2022-06-14 10:15:33.612547
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("git rm help/install.txt") == "git rm -r help/install.txt"

# Generated at 2022-06-14 10:15:36.341611
# Unit test for function get_new_command

# Generated at 2022-06-14 10:15:38.822482
# Unit test for function match
def test_match():
    assert match(Command('git branch master|grep master',
                         '',
                         'fatal: not removing \'\' recursively without -r'))



# Generated at 2022-06-14 10:15:44.093500
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -rf ./test_dir/', '')) == 'git rm -rf -r ./test_dir/'

# Generated at 2022-06-14 10:15:51.668188
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rn file',
                         'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r',
                         ''))
    assert not match(Command(''))


# Generated at 2022-06-14 10:15:54.484808
# Unit test for function match
def test_match():
    assert match(Command('git rm test',
               'fatal: not removing \'test\' recursively without -r\n'))
    assert match(Command('git rm test', '')) is None

# Generated at 2022-06-14 10:15:58.540340
# Unit test for function get_new_command
def test_get_new_command():
    command= Command('git rm foo', 'fatal: not removing \'bar\' recursively without -r')
    assert get_new_command(command) == 'git rm -r foo'


# Generated at 2022-06-14 10:16:00.663462
# Unit test for function match
def test_match():
    cmd = Command('git rm -r abc')
    assert(match(cmd) == True)
    

# Generated at 2022-06-14 10:16:03.260466
# Unit test for function match
def test_match():
	assert match("git rm somefile")
	assert not match("git rebase")
	assert not match("git rm somefile -r")


# Generated at 2022-06-14 10:16:07.082841
# Unit test for function get_new_command
def test_get_new_command():
    assert ' '.join(get_new_command(Command(script = 'git rm a',
        output = "fatal: not removing 'a' recursively without -r\n")).script_parts) == 'git rm -r a'

# Generated at 2022-06-14 10:16:16.917132
# Unit test for function match
def test_match():
    assert match(Command('git rm gs.py',
            "fatal: not removing 'gs.py' recursively without -r"))
    assert not match(Command('git rm gs.py',
            "fatal: not removing 'gs.py'"))
    assert not match(Command('rm gs.py'))



# Generated at 2022-06-14 10:16:20.312441
# Unit test for function match
def test_match():
    assert match(Command(script = 'git rm test.py',
                         output = 'fatal: not removing \'test.py\' recursively without -r'))


# Generated at 2022-06-14 10:16:25.020217
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(('rm -r folder '),
                      ('fatal: not removing \'folder \' recursively without -r'),
                      ('',''), None)
    assert get_new_command(command) == 'rm -r -r folder '

# Generated at 2022-06-14 10:16:29.379906
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ["git", "rm", "file1", "file2"]
    assert get_new_command(Command(script_parts=command_parts, output="")) == "git rm -r file1 file2"


# Generated at 2022-06-14 10:16:32.744816
# Unit test for function get_new_command
def test_get_new_command():
    # Old command
    command = Command('git rm -r .')
    # Should return new command
    assert 'git rm -r .' == get_new_command(command)

# Generated at 2022-06-14 10:16:38.150268
# Unit test for function match
def test_match():
	assert match(command=Command(script='git rm -r'))
	assert match(command=Command(script='git rm'))
	assert not match(command=Command(script='git rm -rf'))
	assert not match(command=Command(script='git rm -r -f'))


# Generated at 2022-06-14 10:16:40.266828
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm subdirectory')) == 'git rm -r subdirectory'

# Generated at 2022-06-14 10:16:43.404025
# Unit test for function match
def test_match():
    assert match(Command(script='git rm',
                         output="fatal: not removing 'src/app.js' recursively without -r"))
    assert not match(Command(script='git rm',
                             output="fatal: not removing 'src/app.js' recursively without -r"))



# Generated at 2022-06-14 10:16:46.292106
# Unit test for function match
def test_match():
    assert match(Command('git rm file'))


# Generated at 2022-06-14 10:16:50.413645
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r /some/file', 'fatal: not removing \'/some/file\' recursively without -r')
    assert get_new_command(command) == 'git rm -r -r /some/file'



# Generated at 2022-06-14 10:17:01.061570
# Unit test for function get_new_command
def test_get_new_command():
    TEST_CASES = [
        ('git rm -r a/b/c/d/e/f', 'git rm -r -r a/b/c/d/e/f'),
        ('git rm -r -r a/b/c/d/e/f', 'git rm -r -r -r a/b/c/d/e/f'),]
    for command, expected in TEST_CASES:
        assert get_new_command(Command(command, '', '')) == expected

# Generated at 2022-06-14 10:17:03.970971
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm test_dir')
    assert get_new_command(command) == 'git rm -r test_dir'

# Generated at 2022-06-14 10:17:10.848433
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r',
                         '', 1))
    assert not match(Command('git rm file',
                             'fatal: not removing \'file\' recursively without -r',
                             '', 1))
    assert not match(Command('rm file', 'fatal: not removing \'file\' recursively without -r', '', 1))


# Generated at 2022-06-14 10:17:17.454876
# Unit test for function match
def test_match():
  assert match(Command('git rm Test_File', 'fatal: not removing \'Test_File\' recursively without -r\n'))
  assert match(Command('git rm Test_File', 'fatal: not removing \'Test_File\' recursively without -r'))
  assert not match(Command('git rm Test_File', 'some other failure\n'))
  assert not match(Command(''))


# Generated at 2022-06-14 10:17:27.270877
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r. '
                         'Use -f if you really want to remove it.'))
    assert not match(Command('git add file',
                             'fatal: not removing \'file\' recursively without -r.'
                             ' Use -f if you really want to remove it.'))
    assert not match(Command('git branch branch', ''))
    assert not match(Command('git branch branch',
                             'fatal: not removing \'file\' recursively.'
                             ' Use -f if you really want to remove it.'))



# Generated at 2022-06-14 10:17:37.344229
# Unit test for function match
def test_match():
    assert match(Command('git rm xxx', 'fatal: not removing \'xxx\' recursively without -r'))
    assert not match(Command('git rm xxx', 'fatal: not removing \'xxx\' recursively without --r'))
    assert match(Command('git rm xxx', 'fatal: not removing \'xxx\' recursively without -r'))
    assert not match(Command('git rm xxx', 'fatal: not removing \'xxx\' recursively without -r',
                     'test'))
    assert not match(Command('xxx', 'fatal: not removing \'xxx\' recursively without -r'))


# Generated at 2022-06-14 10:17:41.016792
# Unit test for function match
def test_match():
    assert match(Command('git rm filename',
                         'fatal: not removing \'filename\' recursively without -r'))
    assert not match(Command('git diff filename', ''))



# Generated at 2022-06-14 10:17:49.023168
# Unit test for function match
def test_match():
    assert match(Command('git rm -rv blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah')) == True


# Generated at 2022-06-14 10:17:51.716404
# Unit test for function match
def test_match():
    assert match(Command(script = "git rm tests/test.py", output = "fatal: not removing 'tests/test.py' recursively without -r"))

# Generated at 2022-06-14 10:17:54.735199
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r', '', ''))
    assert not match(Command('git rm file', '', '', ''))

# Generated at 2022-06-14 10:18:00.860644
# Unit test for function get_new_command

# Generated at 2022-06-14 10:18:10.474658
# Unit test for function get_new_command

# Generated at 2022-06-14 10:18:17.085960
# Unit test for function match
def test_match():
    assert match(Script('git rm README.md',
"""[Error]
$ git rm README.md
fatal: not removing 'README.md' recursively without -r
""",
        stderr=True))
    assert not match(Script('git rm README.md',
"""[Error]
$ git rm README.md
fatal: not removing 'README.md' recursively without -r
$ git rm -r README.md
""",
        stderr=True))


# Generated at 2022-06-14 10:18:21.258509
# Unit test for function get_new_command
def test_get_new_command():
    script ="git rm hello.java"
    command = Command(script, "fatal: not removing 'hello.java' recursively without -r")
    assert get_new_command(command) == script + ' -r'

# Generated at 2022-06-14 10:18:31.512614
# Unit test for function match
def test_match():
    assert_true(match(Command('  rm -f fname', 'fatal: not removing \
            \'fname\' recursively without -r', '', 1)))
    assert_false(match(Command('  rm -f fname', 'fatal: not removing \
            \'fname\' without -r', '', 1)))
    assert_false(match(Command('  rm -f fname', 'fatal: not removing \
            \'fname1\' without -r', '', 1)))
    assert_false(match(Command('  rm fname', 'fatal: not removing \
            \'fname\' recursively without -r', '', 1)))
    assert_false(match(Command('  rm -rf fname', 'fatal: not removing \
            \'fname\' recursively without -r', '', 1)))



# Generated at 2022-06-14 10:18:36.919815
# Unit test for function match
def test_match():
    assert(match(Command(script = 'git rm -r',
                         output = 'fatal: not removing directory ' +
                                  "'branch_name' recursively without -r"))
           == True)
    assert(match(Command(script = 'git rm',
                         output = 'fatal: not removing directory ' +
                                  "'branch_name' recursively without -r"))
           == False)


# Generated at 2022-06-14 10:18:43.394550
# Unit test for function match
def test_match():
    # Test if the command rm is not found with -r or -f options
    assert match(Command('rm -f -r test'))
    # Test if the command rm is not found with -r option
    assert match(Command('rm -r test'))
    # Test if the command has removed the file in a git directory
    assert not match(Command('git rm test'))
    

# Generated at 2022-06-14 10:18:54.960241
# Unit test for function match
def test_match():
    assert match(Command('git rm foo/bar'))
    assert match(Command('git rm foo/bar/'))
    assert match(Command('git rm foo/bar/baz/'))
    assert match(Command('git rm foo/bar/baz', 'fatal: not removing \'foo/bar/baz\' recursively without -r'))
    assert not match(Command('rm -r foo/bar baz'))
    assert not match(Command('git rm -r foo/bar baz'))
    assert not match(Command('git status'))
    #assert not match(Command('git rm foo/bar', 'fatal: not removing \'foo/bar\' recursively without -r\n'))


# Generated at 2022-06-14 10:18:59.127421
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm .',
                      stdout=u"fatal: not removing '.gitignore' recursively "
                             u"without -r\n")
    assert get_new_command(command) == u'git rm -r .'

# Generated at 2022-06-14 10:19:02.544638
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm -r a b c') == 'git rm -r a b c'
    assert get_new_command('git rm a -r b c') == 'git rm a -r b c'

# Generated at 2022-06-14 10:19:13.692019
# Unit test for function match
def test_match():
    assert match(Command('git rm non_existing_file', '', stderr='fatal: not removing \'non_existing_file\' recursively without -r'))
    assert not match(Command('ls',''))


# Generated at 2022-06-14 10:19:26.249278
# Unit test for function match
def test_match():
    assert match(Command('git rm src/main.cpp', 'fatal: not removing \'src/main.cpp\' recursively without -r'))
    assert match(Command('git rm build/', 'fatal: not removing \'build/\' recursively without -r'))
    assert match(Command('git rm -rf src/main.cpp', 'fatal: not removing \'src/main.cpp\' recursively without -r'))
    assert not match(Command('echo git rm src/main.cpp', 'fatal: not removing \'src/main.cpp\' recursively without -r'))
    assert not match(Command('rm -f src/main.cpp', 'fatal: not removing \'src/main.cpp\' recursively without -r'))

# Generated at 2022-06-14 10:19:30.273884
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script="git rm -r test")
    command.output = "fatal: not removing 'test' recursively without -r"
    assert get_new_command(command) == "git rm -r test"


# Generated at 2022-06-14 10:19:33.388300
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf /home/user/foo', ''))
    assert not match(Command('git rm -rf /home/user/foo', 'fatal: rm --cached uses...'))

# Generated at 2022-06-14 10:19:36.804126
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("git rm file1")) == "git rm -r file1"
    assert get_new_command(Command("git rm file1 file2")) == "git rm -r file1 file2"

# Generated at 2022-06-14 10:19:41.869028
# Unit test for function get_new_command
def test_get_new_command():
    result = get_new_command(
        Command('git rm -rf test.txt',
                '',
                'fatal: not removing \'test.txt\' recursively without -r'))
    assert(result == 'git rm -rf -r test.txt')

# Generated at 2022-06-14 10:19:44.738804
# Unit test for function match
def test_match():
    assert match(get_command('rm test', 'not removing test'))
    assert not match(get_command('rm test', 'not removing dir'))

# Generated at 2022-06-14 10:19:52.686618
# Unit test for function match
def test_match():
    assert match(Command('git rm hello',
        output='fatal: not removing \'hello\' recursively without -r'))
    assert not match(Command('git rm hello', output='hello'))


# Generated at 2022-06-14 10:20:02.300856
# Unit test for function match
def test_match():
    # test_git_rm_file_in_directory
    assert match(Command('git rm shit/fuck',
                         'fatal: not removing \'shit/fuck\' recursively without -r'))


# Generated at 2022-06-14 10:20:05.711595
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command(script='git rm -rf cache',
                                    output='fatal: not removing \'cache\' recursively without -r'))
            == 'git rm -r -rf cache')

# Generated at 2022-06-14 10:20:22.266582
# Unit test for function match
def test_match():
    assert match(Command(script='git rm -r filename',
                         output="fatal: not removing 'filename' recursively without -r"))
    assert not match(Command(script='git rm filename',
                             output="fatal: not removing 'filename' recursively without -r")) 
    assert not match(Command(script='git rm filename',
                             output='fatal: not removing filename recursively without -r'))
    assert not match(Command(script='git rm filename',
                             output="fatal: not removing 'filename' recursively without -a"))


# Generated at 2022-06-14 10:20:26.426725
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script = 'git rm test_dir'
    output = "fatal: not removing 'test_dir' recursively without -r"
    get_new_command(Command(script, output))

# Generated at 2022-06-14 10:20:30.109846
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ['git', 'rm', 'filename']
    command = Command(command_parts, command_parts, 'fatal: not removing blah blah blah')
    assert get_new_command(command) == 'git rm -r filename'

# Generated at 2022-06-14 10:20:32.248222
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test/')) == 'git rm -r test/'


# Generated at 2022-06-14 10:20:35.682637
# Unit test for function get_new_command
def test_get_new_command():
    # Input
    command = 'git rm theFile'
    # Output
    new_command = 'git rm -r theFile'
    # Test
    assert get_new_command(command) == new_command

# Generated at 2022-06-14 10:20:39.308916
# Unit test for function get_new_command
def test_get_new_command():
    assert git_support(lambda: True).get_new_command() == get_new_command(Command('', '', '', '', ''))


# Generated at 2022-06-14 10:20:44.429102
# Unit test for function match
def test_match():
    assert match(Command('git rm a',
                         'fatal: not removing \'a\' recursively without -r',
                         ''))
    assert not match(Command('git rm -r a',
                             'fatal: not removing \'a\' recursively without -r',
                             ''))


# Generated at 2022-06-14 10:20:57.902292
# Unit test for function match
def test_match():
    assert match(command=Command(script=u'git rm -r test',
                                 output=u"fatal: not removing 'test/file' recursively without -r"))
    assert match(command=Command(script=u'git rm -r test',
                                 output=u"fatal: not removing 'test/file' recursively without -r"))
    assert match(command=Command(script=u'git rm  -r test',
                                 output=u"fatal: not removing 'test/file' recursively without -r"))
    assert not match(command=Command(script=u'git rm test',
                                     output=u"fatal: not removing 'test/file' recursively without -r"))

# Generated at 2022-06-14 10:21:00.701977
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm foo', '')
    assert u'git rm -r foo' == get_new_command(command)


# Generated at 2022-06-14 10:21:07.169750
# Unit test for function get_new_command
def test_get_new_command():
    command = u'git rm directory'
    new_command = u'git rm -r directory'
    assert get_new_command(Command(command, u'', u'')) == new_command

    command = u'git rm directory file'
    new_command = u'git rm -r directory file'
    assert get_new_command(Command(command, u'', u'')) == new_command

# Generated at 2022-06-14 10:21:18.153202
# Unit test for function match
def test_match():
    assert (match("git rm test.py") is True)
    assert (match("git rm test.py ") is False)
    assert (match("git print test.py") is False)



# Generated at 2022-06-14 10:21:27.430804
# Unit test for function match
def test_match():
    assert(match(Command('git rm file1 file2',
                         'file_1: not removing \'file1\' recursively without -r\nfile_2: not removing \'file2\' recursively without -r'))) is True
    assert(match(Command('git rm file1 file2',
                         'file_1: not removing \'file1\' recursively\nfile_2: not removing \'file2\' recursively without -r'))) is False
    assert(match(Command('rm file1 file2',
                         'file_1: not removing \'file1\' recursively without -r\nfile_2: not removing \'file2\' recursively without -r'))) is False


# Generated at 2022-06-14 10:21:31.512518
# Unit test for function get_new_command
def test_get_new_command():
    script = 'git rm -t file'
    output = "fatal: not removing 'file' recursively without -r"
    assert get_new_command(Command(script=script, output=output)) == 'git rm -t -r file'

# Generated at 2022-06-14 10:21:34.173097
# Unit test for function match
def test_match():
    assert match(Command('git rm test/file.txt',
                         "fatal: not removing 'test/file.txt' recursively without -r"))


# Generated at 2022-06-14 10:21:37.773457
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('git rm dir', 'fatal: not removing \'dir\' recursively without -r', None))
           == u'git rm -r dir')

# Generated at 2022-06-14 10:21:41.136284
# Unit test for function get_new_command
def test_get_new_command():

    command = Command('git rm test.txt', 'fatal: not removing \'test.txt\' recursively without -r')

    assert get_new_command(command) == 'git rm -r test.txt'

# Generated at 2022-06-14 10:21:50.186781
# Unit test for function match
def test_match():
    assert match(Command('cd /tmp', '', '', '', '')) is None
    assert match(Command('git rm foo', '', '', '', '')) is None
    assert match(Command('git rm foo', 'fatal: not removing', '', '', '')) is None
    assert match(Command('git rm foo', 'fatal: not removing foo', '', '', '')) is None
    assert match(Command('git rm foo', 'fatal: not removing foo recursively', '', '', '')) is None
    assert match(Command('git rm foo', 'fatal: not removing foo recursively without -r', '', '', ''))



# Generated at 2022-06-14 10:21:59.868262
# Unit test for function match
def test_match():
    assert match(Command('git rm file.txt',
        'fatal: not removing \'file.txt\' recursively without -r\n',
        '', 0))
    assert not match(Command('git rm file.txt', '', '', 0))
    assert not match(Command('git file.txt',
        'fatal: not removing \'file.txt\' recursively without -r\n',
        '', 0))


# Generated at 2022-06-14 10:22:05.818291
# Unit test for function match
def test_match():
    assert match(Command('git rm bug.txt',
                         'fatal: not removing \'bug.txt\' recursively without -r\n'))
    assert not match(Command('git rm -r bug.txt',
                             'fatal: not removing \'bug.txt\' recursively without '
                             '-r\n'))



# Generated at 2022-06-14 10:22:08.176331
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm file.txt'))=='git rm -r file.txt'

# Generated at 2022-06-14 10:22:23.562368
# Unit test for function match
def test_match():
    assert match(Command(script='git rm a.file', output='fatal: not removing \'a.file\' recursively without -r'))


# Generated at 2022-06-14 10:22:30.739027
# Unit test for function get_new_command
def test_get_new_command():
    """ Unit test for function get_new_command """
    from thefuck.types import Command

    assert get_new_command(Command('', '', '')) == ''
    assert get_new_command(Command('', '', 'fatal: not removing '
                                   "'folder/file' recursively without -r")) == ''
    assert get_new_command(
        Command('git rm folder/file', '', 'fatal: not removing '
                "'folder/file' recursively without -r")) == 'git rm -r folder/file'

# Generated at 2022-06-14 10:22:34.292391
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -i test')
    assert Extension(command=command).get_new_command() == 'git rm -r -i test'

# Generated at 2022-06-14 10:22:38.667326
# Unit test for function match
def test_match():
    output = u"""fatal: not removing 'src/tests/test_runner.py' recursively without -r
usage: git rm [--cached] [--dry-run] [--ignore-unmatch] [--quiet] [--] <file>..."""
    command = Command(script="git rm src/tests/test_runner.py", output=output)
    assert match(command)



# Generated at 2022-06-14 10:22:43.917598
# Unit test for function match
def test_match():
    assert match(Command('git branch -d test', '', 'fatal: not removing \'test\' recursively without -r'))
    assert not match(Command('git branch', '', 'fatal: not removing \'test\' recursively without -r'))


# Generated at 2022-06-14 10:22:53.803504
# Unit test for function match
def test_match():
    from thefuck import utils
    # Git rm with an error
    output = utils.io.StdOut(
        u'fatal: not removing \'src/conf/catalina.properties\''
        u' recursively without -r\n')
    assert match(utils.get_command(u'git rm src/conf/catalina.properties',
                                   output))
    # Git with no error
    output_no_error = utils.io.StdOut(u'')
    assert not match(utils.get_command(
        u'git rm src/conf/catalina.properties', output_no_error))


# Generated at 2022-06-14 10:22:55.937375
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
        'fatal: not removing \'bar\' recursively without -r\n'))


# Generated at 2022-06-14 10:23:00.135755
# Unit test for function match
def test_match():
    command = Command('git rm foo', 'fatal: not removing "foo" \
recursively without -r')
    assert match(command)
    assert not match(Command('not a git command'))



# Generated at 2022-06-14 10:23:03.448032
# Unit test for function match
def test_match():
    assert match(Command('git rm aaa.txt', 'fatal: not removing \'aaa.txt\' recursively without -r'))
    assert not match(Command('git rm aaa.txt', 'fatal: not removing \'aaa.txt\' recursively with -r'))


# Generated at 2022-06-14 10:23:05.834713
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r file')) == 'git rm -r -r file'

# Generated at 2022-06-14 10:23:16.687441
# Unit test for function match
def test_match():
    assert match(Command(script='git commit',
        output='fatal: not removing \'path/to/file\' recursively without -r'))


# Generated at 2022-06-14 10:23:30.045511
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm . && git commit -m "test"', 'fatal: not removing \'.\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -r . && git commit -m "test"'
    command = Command('git rm -f . && git commit -m "test"', 'fatal: not removing \'.\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -f -r . && git commit -m "test"'
    command = Command('git rm -rf . && git commit -m "test"', 'fatal: not removing \'.\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -rf -r . && git commit -m "test"'

# Generated at 2022-06-14 10:23:33.739716
# Unit test for function match
def test_match():
    assert match(Command('git rm file', 'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', 'fatal: not removing'))



# Generated at 2022-06-14 10:23:38.930468
# Unit test for function match
def test_match():
    assert match(Command('git rm a', 
                         '', 
                         'fatal: not removing \'a\' recursively without -r\n'))
    assert not match(Command('rm', '', ''))
    assert not match(Command('git rm a', '', ''))


# Generated at 2022-06-14 10:23:43.073827
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='git rm file.txt',
                      output="fatal: not removing 'file.txt' recursively without -r")
    assert get_new_command(command) == u'git rm -r file.txt'

# Generated at 2022-06-14 10:23:49.731467
# Unit test for function match
def test_match():
    assert match(Command(script='git rm -r',
                       output='''fatal: not removing 'a/b/c' recursively without -r '''))
    assert match(Command(script='git rm -rf',
                        output='''fatal: not removing 'a/b/c' recursively without -r '''))
    assert not match(Command(script='git rm',
                       output='''fatal: not removing 'a/b/c' recursively without -r '''))
    assert not match(Command(script='echo rm -r',
                        output='''fatal: not removing 'a/b/c' recursively without -r '''))
