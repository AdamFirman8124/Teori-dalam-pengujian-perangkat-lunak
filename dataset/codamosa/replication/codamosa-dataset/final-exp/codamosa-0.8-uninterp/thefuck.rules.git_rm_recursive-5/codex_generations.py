

# Generated at 2022-06-14 10:14:01.461602
# Unit test for function match
def test_match():
    assert match(Command('git rm invalid', stderr='fatal: not removing \'invalid\' recursively without -r'))
    assert not match(Command('git push', stderr='fatal: not removing \'invalid\' recursively without -r'))


# Generated at 2022-06-14 10:14:04.093838
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r directory',
                                   'git output')) == 'git rm -r -r directory'

# Generated at 2022-06-14 10:14:06.657627
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r foo bar', '')) == 'git rm -r foo bar'


# Generated at 2022-06-14 10:14:09.787433
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm -rf', 'fatal: not removing \'test\' recursively without -r')) == 'rm -r -rf'


# Generated at 2022-06-14 10:14:12.489007
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm folder')
    assert_equals(get_new_command(command), u'git rm -r folder')

# Generated at 2022-06-14 10:14:23.360495
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("rm path/to/a/file",
                                   "fatal: not removing 'path/to/a/file' recursively without -r\n")) == 'git rm -r path/to/a/file'
    assert get_new_command(Command("git rm path/to/a/file",
                                   "fatal: not removing 'path/to/a/file' recursively without -r\n")) == 'git rm -r path/to/a/file'
    assert get_new_command(Command("git rm path/to/a/file -f",
                                   "fatal: not removing 'path/to/a/file' recursively without -r\n")) == 'git rm -r path/to/a/file -f'

# Generated at 2022-06-14 10:14:30.210946
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm /home/dev/dummy')) == 'git rm -r /home/dev/dummy'
    assert get_new_command(Command('git rm /home/dev/dummy /home/dev/dummy2')) == 'git rm -r /home/dev/dummy /home/dev/dummy2'

# Generated at 2022-06-14 10:14:33.471028
# Unit test for function get_new_command
def test_get_new_command():
    assert ('git rm -r foo', get_new_command(Command('git rm foo', '',
            'fatal: not removing \'foo\' recursively without -r\n')))

# Generated at 2022-06-14 10:14:39.221891
# Unit test for function match
def test_match():
    assert match(Command('git rm bla.txt', output="\nfatal: not removing 'bla.txt' recursively without -r\n"))
    assert not match(Command('git rm bla.txt', output="\nfatal: not removing 'bla.txt' recursively without -r\n"))


# Generated at 2022-06-14 10:14:41.425097
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm -r test') == 'git rm -r -r test'

# Generated at 2022-06-14 10:14:49.357779
# Unit test for function match
def test_match():
    assert match(Command('git rm myfile',
                         'fatal: not removing \'myfile\' recursively without -r'))
    assert not match(Command('git rm myfolder/myfile',
                             'fatal: not removing \'myfolder/myfile\' recursively without -r'))
    assert not match(Command('git rm myfile', 'blabla'))


# Generated at 2022-06-14 10:14:59.780180
# Unit test for function get_new_command
def test_get_new_command():
    print (get_new_command(Command('git rm -f README.md', 'fatal: not removing \'README.md\' recursively without -r')))
    assert get_new_command(Command('git rm -f README.md', 'fatal: not removing \'README.md\' recursively without -r')) == 'git rm -r -f README.md'

# Generated at 2022-06-14 10:15:05.392625
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('git rm dir/',
                                   'fatal: not removing \'dir/\' recursively without -r',
                                   '', 1)) \
           == 'git rm -r dir/'

# Generated at 2022-06-14 10:15:12.643404
# Unit test for function match
def test_match():
    # Test for command with 'fatal: not removing' in output
    command = Command(' rm some_folder', 'fatal: not removing \'some_folder\' recursively without -r\n')
    assert match(command) == True

    # Test for command with 'fatal: not removing' not in output
    command = Command(' rm some_folder', 'Some other error message\n')
    assert match(command) == False



# Generated at 2022-06-14 10:15:18.592439
# Unit test for function get_new_command
def test_get_new_command():
    command = MagicMock(
               script="git rm -r",
               script_parts=["git", "rm", "-r"],
               output="fatal: not removing 'src/some_file' recursively without -r")
    assert u'git rm -r -r' == get_new_command(command)



# Generated at 2022-06-14 10:15:22.768908
# Unit test for function match
def test_match():
    assert match(Command('git rmdir path', "fatal: not removing 'path/to/file' recursively without -r"))
    assert match(Command('git rm path', "fatal: not removing 'path/to/file' recursively without -r"))

# Generated at 2022-06-14 10:15:25.976652
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git rm -rf foo') == 'git rm -rf -r foo'

# Generated at 2022-06-14 10:15:28.703952
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm --cached filename')) == 'git rm -r --cached filename'


enabled_by_default = True

# Generated at 2022-06-14 10:15:32.882549
# Unit test for function match
def test_match():
    assert match(Command('rm file', '')) is True
    assert match(Command('git rm file', '')) is True
    assert match(Command('git rm file', '')) is True
    assert match(Command('git rm file', '')) is True


# Generated at 2022-06-14 10:15:36.917977
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm file.txt")
    command.output = "fatal: not removing 'file.txt' recursively without -r"
    assert_equals(get_new_command(command), "git rm -r file.txt")

# Generated at 2022-06-14 10:15:48.600403
# Unit test for function get_new_command
def test_get_new_command():
    command_parts = ['git', 'rm', '-rf', 'test.txt']
    command = Command(script = u' '.join(command_parts),
                                          output = "fatal: not removing 'test.txt' recursively without -r")

    # Asserting on command.script
    assert get_new_command(command) == 'git rm -r -rf test.txt'



# Generated at 2022-06-14 10:15:50.923828
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm bad')
    assert get_new_command(command) == "git rm -r bad"

# Generated at 2022-06-14 10:15:55.578329
# Unit test for function match
def test_match():
    command = Command('git rm -rf --cached .vim/bundle/jedi-vim')
    command.output = 'fatal: not removing \'~/.vim/.vim/bundle/jedi-vim\' recursively without -r'
    assert match(command) == True


# Generated at 2022-06-14 10:16:00.894874
# Unit test for function match
def test_match():
    assert match(Command('git rm file1 file2', ''))
    assert not match(Command('git status file1 file2', ''))
    assert not match(Command('git rm -r file1 file2', ''))
    assert not match(Command('rm file1 file2', ''))


# Generated at 2022-06-14 10:16:03.498535
# Unit test for function match
def test_match():
    command_obj = Command('git rm filename.txt')
    result = match(command_obj)
    assert result == False, 'This test failed'

# Generated at 2022-06-14 10:16:12.485486
# Unit test for function match
def test_match():
    test1 = Command('git rm -r')
    assert not match(test1)

    test2 = Command.from_string('git rm -rf some_file',
                                'fatal: not removing \'some_file\' recursively without -r')
    assert match(test2)

    test3 = Command.from_string('git rm -rf some_file',
                                'fatal: not removing \'another_file\' recursively without -r')
    assert not match(test3)

    test4 = Command.from_string('git rm -rf',
                                'fatal: not removing \'some_file\' recursively without -r')
    assert match(test4)


# Generated at 2022-06-14 10:16:16.915594
# Unit test for function match
def test_match():
    assert match(Command(script='rm foo', output='fatal: not removing \'foo\' recursively without -r'))
    assert not match(Command(script='git delete foo', output='fatal: no such path \'bar\''))

# Generated at 2022-06-14 10:16:19.862629
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
        "fatal: not removing 'file' recursively without -r\n",
        "")
        )


# Generated at 2022-06-14 10:16:25.020769
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    get_new_command_response = get_new_command(Command('git rm -f foo', '', 'fatal: not removing \'foo\' recursively without -r'))
    assert get_new_command_response == 'git rm -rf foo'

# Generated at 2022-06-14 10:16:37.150273
# Unit test for function match
def test_match():
    command = Command('git rm a/b/c', 'fatal: not removing \'a/b/c\' recursively without -r\n')
    assert match(command) == True

    command = Command('git rm a', 'fatal: not removing \'a\' recursively without -r\n')
    assert match(command) == True

    command = Command('rm a/b/c', 'fatal: not removing \'a/b/c\' recursively without -r\n')
    assert match(command) == False

    command = Command('git rm -r a/b/c', 'fatal: not removing \'a/b/c\' recursively without -r\n')
    assert match(command) == False



# Generated at 2022-06-14 10:16:44.244897
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         output="fatal: not removing 'file' recursively without -r\n",
                         stderr=''))
    assert not match(Command('git rm file',
                         output="fatal: not removing '' recursively without -r\n",
                         stderr=''))


# Generated at 2022-06-14 10:16:52.344533
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf /somedir/', ''))
    assert match(Command('git rm /somedir/', "fatal: not removing 'foo' recursively without -r"))
    assert not match(Command('git rm -rf /somedir/', 'fatal: not removing \'/somedir/\' recursively without -r'))
    assert not match(Command('git rm -rf /somedir/', ''))



# Generated at 2022-06-14 10:16:56.254350
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm some_dir', 'fatal: not removing \'some_dir\' recursively without -r\n')
    assert get_new_command(command) == "git rm -r some_dir"

# Generated at 2022-06-14 10:16:59.471961
# Unit test for function match
def test_match():
    assert match(Command("git rm 'test'",
                         "fatal: not removing 'test' recursively without -r"))
    assert not match(Command("git rm 'test'", "test"))


# Generated at 2022-06-14 10:17:06.098791
# Unit test for function match
def test_match():
    assert match(Command(script='git rm', output='''fatal: not removing 'git/src/hooks/commit-msg.sample' recursively without -r
    ''')) == True
    assert match(Command(script='git rm', output='''fatal: bad revision 'origin/master'
    ''')) == False

# Generated at 2022-06-14 10:17:09.376631
# Unit test for function get_new_command
def test_get_new_command():

    output = 'fatal: not removing \'test/test_something.py\' recursively without -r'
    script = 'git rm -v test/test_something.py'
    command = Command(script=script, output=output)
    assert get_new_command(command) == 'git rm -v -r test/test_something.py'

# Generated at 2022-06-14 10:17:13.548163
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm dir/', 'fatal: not removing \'dir/\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -r dir/'

# Generated at 2022-06-14 10:17:19.032920
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object, ), {
        'script': 'git rm dir',
        'output': "fatal: not removing 'dir' recursively without -r",
        'script_parts': ['git', 'rm', 'dir']
    })

    assert get_new_command(command) == 'git rm -r dir'

# Generated at 2022-06-14 10:17:21.730255
# Unit test for function match
def test_match():
    assert match('git rm foo')
    assert match('git  rm ')
    assert not match('git rm --cached foo')

# Generated at 2022-06-14 10:17:26.710987
# Unit test for function get_new_command
def test_get_new_command():
    old_cmd = 'git branch -d branch_name'
    old_output = 'fatal: not removing \'branch_name\' recursively without -r'
    assert get_new_command(Command(old_cmd, old_output)) == \
        'git branch -d -r branch_name'

# Generated at 2022-06-14 10:17:37.691186
# Unit test for function match
def test_match():
    assert match(Command('git rm hello', '', 'fatal: not removing \'hello\' recursively without -r'))
    assert not match(Command('git rm hello', '', 'fatal: not removing hello recursively without -r'))


# Generated at 2022-06-14 10:17:40.000530
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(build_command('git rm folder/path')) == 'git rm -r folder/path'
    assert get_new_c

# Generated at 2022-06-14 10:17:46.967548
# Unit test for function match
def test_match():
    assert match(Command('git rm -f folder',
                         'fatal: not removing \'folder\' recursively without -r',
                         ''))


# Generated at 2022-06-14 10:17:49.190064
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm -r test', '', '')) == 'git rm -r -r test'

# Generated at 2022-06-14 10:17:54.688259
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git rm -r file' == get_new_command('git rm file')
    assert 'git rm -r file file2' == get_new_command('git rm file file2')
    assert 'git rm file -r file2' == get_new_command('git rm file file2')
    assert 'git rm -rf otherfile -r file' == get_new_command('git rm -rf otherfile file')

# Generated at 2022-06-14 10:18:00.176050
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm test.txt')
    command.script_parts = ['git', 'rm', 'test.txt']
    command.output = "'git' is not recognized as an internal or external command,\n"\
                    "operable program or batch file."
    command.stderr = ''
    assert get_new_command(command) == 'git rm -r test.txt'

# Generated at 2022-06-14 10:18:03.752992
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git rm -r --cached test.txt'
    assert get_new_command(Command(command, 'output')) == 'git rm -r -r --cached test.txt'

# Generated at 2022-06-14 10:18:06.231066
# Unit test for function match
def test_match():
    assert match(Command("git rm foo", "fatal: not removing 'foo' recursively without -r"))


# Generated at 2022-06-14 10:18:10.674611
# Unit test for function match
def test_match():
    assert match(Command('git add .',
            'fatal: not removing \'dir1/dir2/file3\' recursively without -r'))
    assert not match(Command('git rm -r dir1/dir2/file3', ''))
    assert not match(Command('git add .', ''))



# Generated at 2022-06-14 10:18:16.491286
# Unit test for function get_new_command
def test_get_new_command():
    assert ('git rm -r foo' == get_new_command(Command(script='git rm foo',
                                                      stderr="fatal: not removing 'foo' recursively without -r",
                                                      ))
            and 'git rm -r foo bar' == get_new_command(Command(script='git rm foo bar',
                                                               stderr="fatal: not removing 'foo' recursively without -r",
                                                               )))

# Generated at 2022-06-14 10:18:26.546207
# Unit test for function match
def test_match():
    assert match(Command(script='git rm ...',
                         output='fatal: not removing ... recursively without -r'))
    assert not match(Command(script='git rm ...',
                             output='fatal: removing ... recursively'))
    assert not match(Command(script='git status',
                             output='fatal: removing ... recursively without -r'))


# Generated at 2022-06-14 10:18:29.653690
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command('git rm script.py')
    assert new_command == 'git rm -r script.py'

# Generated at 2022-06-14 10:18:32.746414
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
        'fatal: not removing \'file\' recursively without -r'))
    assert not match(Command('git rm file', ''))


# Generated at 2022-06-14 10:18:34.938271
# Unit test for function match
def test_match():
    assert match("git rm README.md")
    assert not match("grep something")
    assert not match("rm README.md")



# Generated at 2022-06-14 10:18:40.083248
# Unit test for function match
def test_match():
    assert match(Command('rm -rf folder', ''))
    assert match(Command('rm -rf folder', 'fatal: not removing \'folder\' recursively without -r'))
    assert not match(Command('rm -rf folder', 'fatal: removing \'folder\' recursively without -r'))

# Generated at 2022-06-14 10:18:43.979163
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("git rm dummyFile", "fatal: not removing 'dummyFile' recursively without -r")
    assert get_new_command(command) == "git rm -r dummyFile"

# Generated at 2022-06-14 10:18:47.463223
# Unit test for function get_new_command
def test_get_new_command():
	assert(get_new_command(Command('git rm filename')) == 'git rm -r filename')
	assert(get_new_command(Command('git rm filename -r')) == 'git rm -r filename -r')


# Generated at 2022-06-14 10:18:51.547109
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command(script='git rm filename',
                                    stdout='fatal: not removing \'filename\' recursively without -r'))
            == u'git rm -r filename')

# Generated at 2022-06-14 10:18:55.702959
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test',
                                   'fatal: not removing "test" recursively without -r',
                                   '', 1)) == 'git rm -r test'

# Generated at 2022-06-14 10:19:00.734965
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    script = 'git rm "my folder"'
    output = "fatal: not removing 'my folder' recursively without -r"
    commands = Command(script,output)
    new_command = get_new_command(commands)
    assert new_command == 'git rm -r "my folder"'

# Generated at 2022-06-14 10:19:18.537747
# Unit test for function match
def test_match():
    assert match(Command(script = 'git rm -r file ', output = 'fatal: not removing \'file/file\' recursively without -r')) == True
    assert match(Command(script = 'git rm file', output = 'fatal: not removing \'file/file\' recursively without -r')) == False
    assert match(Command(script = 'git rm file ', output = 'fatal: not removing \'file/file\' recursively without -r')) == False
    assert match(Command(script = 'git rm -r file ', output = 'fatal: not removing \'file\' recursively without -r')) == False


# Generated at 2022-06-14 10:19:20.671369
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm test/test.txt', '', '')) == 'git rm -r test/test.txt'

# Generated at 2022-06-14 10:19:23.464350
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'foo\' recursively without -r',
                         ''))
    assert not match(Command('git rm foo', '', ''))

# Generated at 2022-06-14 10:19:25.393461
# Unit test for function match
def test_match():
    command = Command('rm filename', 'fatal: not removing \'filename\' recursively without -r')
    assert match(command)


# Generated at 2022-06-14 10:19:31.185895
# Unit test for function match
def test_match():
    assert match(Command('git status', '', '', 0, None))
    assert match(Command('git  rm   f', 'fatal: not removing \'.gitignore\' recursively without -r\n', '', 0, None))
    assert not match(Command('git  rm   f', 'not removing \'.gitignore\' recursively without -r\n', '', 0, None))
    assert not match(Command('git status', '', '', 0, None))


# Generated at 2022-06-14 10:19:36.263820
# Unit test for function match
def test_match():
    # The first example is taken directly from the above documentation, the second one is
    # a bit modified to fit the requirements:
    assert match(Command('git rm foo', "fatal: not removing 'foo' recursively without -r",
                         '')) is True
    assert match(Command('foo', '', '')) is False



# Generated at 2022-06-14 10:19:39.015004
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm subfolder', 'fatal: not removing \'subfolder/\' recursively without -r')) == 'git rm -r subfolder'

# Generated at 2022-06-14 10:19:44.087034
# Unit test for function match
def test_match():
    assert match(Command('git rm README.md',
                         'fatal: not removing \'README.md\' recursively without -r\n'))
    assert not match(Command('git rm README.md', ''))


# Generated at 2022-06-14 10:19:55.540543
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('some-command',
            script='git rm -f *',
            output="fatal: not removing 'file1' recursively without -r\n"
                 "fatal: not removing 'file2' recursively without -r")
    new_command = get_new_command(command)
    assert new_command == 'git rm -f -r *'


# Generated at 2022-06-14 10:19:59.490168
# Unit test for function match
def test_match():
    assert match(Command(script='git rm foo', output="fatal: not removing 'foo/bar' recursively without -r"))
    assert match(Command(script='git rm foo/bar', output="fatal: not removing 'foo/bar' recursively without -r"))
    assert not match(Command(script='git rm foo', output="fatal: not removing 'foo/bar' recursively without -a"))
    assert not match(Command(script='rm foo', output="fatal: not removing 'foo/bar' recursively without -r"))


# Generated at 2022-06-14 10:20:20.085232
# Unit test for function match
def test_match():
    command = Command("git rm -r config", "fatal: not removing 'config' recursively without -r")
    assert match(command) == True

    command = Command("git rm", "fatal: not removing 'config' recursively without -r")
    assert match(command) == False


# Generated at 2022-06-14 10:20:23.403011
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r'))


# Generated at 2022-06-14 10:20:34.056596
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf a b c',
                         stderr=(u"fatal: not removing 'a' recursively "
                                 u"without -r\nfatal: not removing 'b' "
                                 u"recursively without -r")))
    assert match(Command('git rm a b c',
                         stderr=(u"fatal: not removing 'a' recursively "
                                 u"without -r\nfatal: not removing 'b' "
                                 u"recursively without -r")))
    assert not match(Command('git rm a b c',
                             stderr=u"fatal: not removing 'a' recursively "
                             u"without -r"))

# Generated at 2022-06-14 10:20:38.898007
# Unit test for function match
def test_match():
    assert match(Command('git rm folder', 'fatal: not removing \'folder\' recursively without -r'))
    assert not match(Command('git rm folder', 'fatal: not removing \'folder\' recursively with -r'))
    assert not match(Command('git rm folder'))

# Generated at 2022-06-14 10:20:41.349382
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git rm lib')) == u'git rm -r lib'


enabled_by_default = True
priority = 1000

# Generated at 2022-06-14 10:20:44.959152
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm -r foo bar', 'fatal: not removing \'foo\' recursively without -r\n')
    assert get_new_command(command) == 'git rm -r -r foo bar'

# Generated at 2022-06-14 10:20:52.324512
# Unit test for function match
def test_match():
    match1 = git_rm_dir_not_empty_without_r('git rm -r folder')
    assert match1.script == 'git rm -r folder'
    assert match1.output == "fatal: not removing 'folder' recursively without -r"
    assert match1.pos == 5
    assert match1.iscorrect == True

    match2 = git_rm_dir_not_empty_without_r('git rm folder')
    assert match2.script == 'git rm folder'
    assert match2.output == ""
    assert match2.pos == 5
    assert match2.iscorrect == False


# Generated at 2022-06-14 10:21:08.194066
# Unit test for function match
def test_match():

    assert match(Command('git rm -rf /var/tmp/', 'fatal: not removing \'/var/tmp/\' recursively without -r')), 'Simple error message for git rm, but the file exists'
    assert match(Command('git rm -rf /var/tmp', 'fatal: not removing \'/var/tmp\' recursively without -r')), 'Simple error message for git rm, but the file exists'
    assert match(Command('rm -rf /var/tmp', 'fatal: not removing \'/var/tmp\' recursively without -r')), 'Simple error message for rm, but the file exists'
    assert match(Command('git rm -rf /var/tmp', 'rm \'/var/tmp\' recursively without -r')), 'Simple error message for rm, but the file exists'

# Generated at 2022-06-14 10:21:16.052903
# Unit test for function match
def test_match():
    assert_equal(match(Command('echo "fatal: not removing '
                               '/home/mohan/Gitfiles/hello/ "recursively'
                               ' without -r"',
                               'fatal: not removing '
                               '/home/mohan/Gitfiles/hello/ "recursively'
                               ' without -r"')),
                 True)
    assert_equal(match(Command('echo "fatal: not removing '
                               '/home/mohan/Gitfile/hello/ "recursively'
                               ' without -r"',
                               'fatal: not removing '
                               '/home/mohan/Gitfile/hello/ "recursively'
                               ' without -r"')),
                 False)


# Generated at 2022-06-14 10:21:17.623255
# Unit test for function match
def test_match():
    assert match('git rm -rf /home/test')


# Generated at 2022-06-14 10:21:39.406631
# Unit test for function match
def test_match():
    assert match(Command('git rm file_name',
        """[file_name]
fatal: not removing 'file_name' recursively without -r
"""))
    assert not match(Command('git rm file_name',
        """[file_name]
fatal: something else
"""))


# Generated at 2022-06-14 10:21:44.517834
# Unit test for function match
def test_match():
    # Test match with git rm
    assert match(Command('git rm -f First.c', ''))
    # Test match with git rm and output
    assert match(Command('git rm -f First.c', 'fatal: not removing \'First.c\' recursively without -r'))
    assert not match(Command('git add -f First.c', ''))

# Generated at 2022-06-14 10:21:47.561872
# Unit test for function match
def test_match():
    assert match(Command(script='git rm a/b/c',
                         stderr='fatal: not removing \'./a/b/c\' recursively without -r\n'))


# Generated at 2022-06-14 10:21:49.197250
# Unit test for function match
def test_match():
    assert match(Command('git rm file', '', 'fatal: not removing \'file\' recursively without -r'))

# Generated at 2022-06-14 10:21:52.062143
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm filename', '', 'fatal: not removing \'filename\' recursively without -r')
    asser

# Generated at 2022-06-14 10:21:58.659223
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git rm "dir/dir2/dir3/file"', '')
    assert get_new_command(command) == u'git rm -r "dir/dir2/dir3/file"'

# Generated at 2022-06-14 10:22:01.166222
# Unit test for function match
def test_match():
    assert match(Command('git rm file',
                         'fatal: not removing \'file\' recursively without -r'))


# Generated at 2022-06-14 10:22:04.882508
# Unit test for function match
def test_match():
    assert match(Command(script='git rm file', 
                         stderr="fatal: not removing 'file' recursively without -r\n"))


# Generated at 2022-06-14 10:22:07.716973
# Unit test for function match
def test_match():
    assert match(Command('git rm foo',
                         'fatal: not removing \'bar\' recursively without -r'))

# Unit tests for function get_new_command

# Generated at 2022-06-14 10:22:10.354821
# Unit test for function match
def test_match():
    assert match(Command('git rm foo', 'fatal: not removing \'foo\' recursively without -r\n', '', 1))


# Generated at 2022-06-14 10:22:53.192560
# Unit test for function match
def test_match():
    # Test if it matches
    assert match(Command(script = 'git rm -r --cached .idea',
                         output = 'fatal: not removing \'<script_parts[index]>.idea\' recursively without -r'))
    # Test if it doesn't match
    assert not match(Command(script = 'git rm -r --cached .idea',
                             output = 'fatal: not removing \'<script_parts[index]>.idea\' recursively without -r\n'
                                      'fatal: not removing \'<script_parts[index]>.idea\' recursively without -r'))


# Generated at 2022-06-14 10:22:56.106210
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='git rm', stdout='fatal: not removing \'commands.py\' recursively without -r')) == 'git rm -r'

# Generated at 2022-06-14 10:23:00.837469
# Unit test for function get_new_command
def test_get_new_command():
    command = GenericCommand(script='git rm -r test',
                             stderr='fatal: not removing \'test\' recursively without -r')
    assert get_new_command(command) == 'git rm -r -r test'

# Generated at 2022-06-14 10:23:12.020081
# Unit test for function match
def test_match():
    assert match(Command('git rm -rf dummy',
                  '/tmp/my-repo$ git rm -rf dummy\n'
                  'fatal: not removing \'dummy\' recursively without -r'))
    assert not match(Command('git rm -rf dummy',
                     '/tmp/my-repo$ git rm -rf dummy\n'
                     'fatal: not removing \'dummy\' recursively without -r'))
    assert not match(Command('git rm -rf dummy dummy2',
                     '/tmp/my-repo$ git rm -rf dummy dummy2\n'
                     'fatal: not removing \'dummy\' recursively without -r'))


# Generated at 2022-06-14 10:23:15.372092
# Unit test for function match
def test_match():
    assert match("git rm test.txt")
    assert not match("git rm -r test.txt")
    assert not match("git branch")


# Generated at 2022-06-14 10:23:20.146060
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf --target-directory /home/user/qux')
    out_command = get_new_command(command)
    assert out_command == 'rm -r -f --target-directory /home/user/qux'

# Generated at 2022-06-14 10:23:22.492185
# Unit test for function match
def test_match():
    assert match(Command('rm test.txt', ''))
    assert not match(Command('rm test.txt', 'something'))

# Generated at 2022-06-14 10:23:25.378848
# Unit test for function match
def test_match():
    assert match(Command(' rm file', 'fatal: not removing \'file\' recursively without -r'))


# Generated at 2022-06-14 10:23:29.702058
# Unit test for function match
def test_match():
    rm_error_cmd = Command('git rm a/b/c',
            u'fatal: not removing \'a/b/c\' recursively without -r', 0)

    assert match(rm_error_cmd)


# Generated at 2022-06-14 10:23:36.489479
# Unit test for function get_new_command
def test_get_new_command():
    """
    This function will give the new command if the previous command is wrongly 
    spelled or invalid. 
    """
    from thefuck.types import Command

    # If the new command is obtained, the test will return True.
    assert get_new_command(Command('git rm -f *.txt',
                                   'fatal: not removing \'*.txt\' recursively without -r',
                                   'git rm -f *.txt')) == u'git rm -r -f *.txt'