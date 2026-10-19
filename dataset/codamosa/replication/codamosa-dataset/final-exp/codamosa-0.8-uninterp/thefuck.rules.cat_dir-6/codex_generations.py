

# Generated at 2022-06-14 09:29:58.239031
# Unit test for function match
def test_match():
    command = Command('cat /home/')
    assert match(command)


# Generated at 2022-06-14 09:30:01.612524
# Unit test for function match
def test_match():
    assert match(Command(script='cat /home/elias/Documents', output='cat: /home/elias/Documents: Is a directory', stderr='', stdout=''))


# Generated at 2022-06-14 09:30:02.679564
# Unit test for function match

# Generated at 2022-06-14 09:30:05.864330
# Unit test for function match
def test_match():
    command = Command('cat test_files/test_files_1', 'cat: test_files/test_files_1: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:30:08.328009
# Unit test for function match
def test_match():
    assert match(Command('cat file.txt', 'cat: file.txt: Is a directory',
                         os.getcwd()))



# Generated at 2022-06-14 09:30:14.983012
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt', stderr='cat: test.txt: Is a directory'))
    assert match(Command('cat test.txt', stderr='cat: test.txt: No such file or directory'))
    assert match(Command('cat test.txt', stderr='cat: test.txt: No'))
    assert not match(Command('cat test.txt', stderr='cat: test.txt: No such file or directory'))


# Generated at 2022-06-14 09:30:19.684198
# Unit test for function match
def test_match():
    """
    Desc: test match function
    """
    command = MagicMock(script_parts=['cat', 'readme'])
    command.output = 'cat: readme: Is a directory'
    assert match(command)
    command.output = 'cat: readme: Is not a directory'
    assert not match(command)


# Generated at 2022-06-14 09:30:24.535131
# Unit test for function match
def test_match():
    assert match(Command('cat /home', ''))
    assert match(Command('cat /home', 'cat: /home: Is a directory'))
    assert not match(Command('cat /home', 'cat: /home: No such file or directory'))



# Generated at 2022-06-14 09:30:28.688317
# Unit test for function match
def test_match():
    from thefuck.rules.cat_is_a_directory import match
    os.path.isdir = lambda path: True
    assert match(Command('cat lol', 'cat: lol: Is a directory', 'lol'))



# Generated at 2022-06-14 09:30:39.783226
# Unit test for function match
def test_match():
    #Test if command is cat and output is error
    assert match(Command('cat a b c',
                         '/bin/cat: a: Is a directory\n'))

    #Test if command is cat & ls, output is error and 'a' is a directory
    assert match(Command('cat a b c',
                         '/bin/cat: a: Is a directory\n',
                         '/bin/ls: a: Is a directory\n'))

    #Test if command is cat & ls, output is error and 'a' is not a directory
    assert not match(Command('cat a b c',
                             '/bin/cat: a: Is a directory\n',
                             '/bin/ls: a: Is not a directory\n'))

    #Test if command is cat & ls, output is not error and 'a' is a directory
    assert not match

# Generated at 2022-06-14 09:30:44.103774
# Unit test for function match
def test_match():
    assert match(Command('cat /home/user/dire', None, 'cat: dire: Is a directory'))
    assert not match(Command('cat /home/user/file', None, '/home/user/file'))

# Generated at 2022-06-14 09:30:46.587392
# Unit test for function match
def test_match():
    assert match(Command('cat a b', 'cat: a: Is a directory', '', 1))
    assert not match(Command('cat a b', '', '', 1))


# Generated at 2022-06-14 09:30:52.811208
# Unit test for function match
def test_match():
    command = Command('cat test', 'cat: test: Is a directory\n')
    assert match(command)
    assert not match(Command('ls test',
                             'cat: test: Is a directory\n'))

# Generated at 2022-06-14 09:30:55.905244
# Unit test for function match
def test_match():
    assert match(Command('cat test', '', 'cat: test: Is a directory'))
    assert not match(Command('cat test', '', 'cat: test: No such file'))


# Generated at 2022-06-14 09:31:03.520750
# Unit test for function match
def test_match():
    command = Command('cat /tmp/dir', '', '/tmp/dir: Is a directory')
    
    # Test for correct output
    assert match(command)
    
    # Test for old command
    assert not match(Command('ls /tmp/dir', '', '/tmp/dir: Is a directory'))
    
    # Negative test
    assert not match(Command('cat /tmp/dir/file', '',
                  ''))
    
    # Test for multiple parts
    assert not match(Command('cat test /tmp/dir', '',
                  '/tmp/dir: Is a directory'))
    

# Generated at 2022-06-14 09:31:09.739461
# Unit test for function match
def test_match():
    assert match(Command(script='cat file',
                         output='cat: file: Is a directory'))
    assert match(Command(script='cat file', output='cat: file: Is a dir'))
    assert not match(Command(script='cat file', output='cat: file: No such file'))
    assert not match(Command(script='ls file', output='cat: file: Is a directory'))
    assert not match(Command(script='ls file', output='ls: file: No such file'))


# Generated at 2022-06-14 09:31:13.537580
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/hosts',
                         '/etc/hosts is a directory', ''))
    assert not match(Command('cat /etc/hosts', '', ''))

# Generated at 2022-06-14 09:31:20.550349
# Unit test for function match
def test_match():
    assert match(Command(script='cat DIR', output='cat: DIR: Is a directory'))
    assert not match(Command(script='cat DIR', output='cat: DIR: No such file or directory'))



# Generated at 2022-06-14 09:31:23.147304
# Unit test for function match
def test_match():
    command = Command('cat foo', 'cat: foo: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:31:29.872412
# Unit test for function match
def test_match():
    assert match(Command(script='cat', output='cat: foo: Is a directory'))
    assert match(Command(script='cat bar', output='cat: bar: Is a directory'))
    assert not match(Command(script='cat', output='cat: foo: No such file or directory'))
    assert not match(Command(script='cat foo', output='cat: foo: No such file or directory'))


# Generated at 2022-06-14 09:31:36.144940
# Unit test for function match
def test_match():
    assert match(Command('cat mfs', 'cat: mfs: Is a directory'))
    assert not match(Command('cat mfs', 'cat: mfs: No such file or directory'))


# Generated at 2022-06-14 09:31:44.296718
# Unit test for function match
def test_match():
    # Check that it returns true if command contains cat
    assert match(Command('cat *.png', 'cat: *.png: Is a directory'))
    
    # Check that it returns false if command does not contain cat
    assert not match(Command('ls *.png', 'ls: *.png: Is a directory'))
    
    # Check that it returns false if command does not contain a valid directory
    assert not match(Command('cat *.png', 'cat: *.png: No such file or directory'))

# Generated at 2022-06-14 09:31:48.149216
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt', 'cat: test.txt: Is a directory'))

# Generated at 2022-06-14 09:31:54.521838
# Unit test for function match
def test_match():
    match_output = match('cat new_file')
    assert match_output == False
    match_output = match('pwd | cat -n')
    assert match_output == False
    match_output = match('cat /usr/share/applications/test_file.desktop')
    assert match_output == False
    match_output = match('cat /usr/share/applications/test_file.desktop')
    assert match_output == False


# Generated at 2022-06-14 09:31:58.946864
# Unit test for function match
def test_match():
    command = Command('cat asdf', 'cat: asdf: Is a directory')
    assert match(command)
    command = Command('cat asdf')
    assert not match(command)
    command = Command('cat asdf')
    assert not match(command)


# Generated at 2022-06-14 09:32:01.150310
# Unit test for function match
def test_match():
    command = Command('cat /home', '')
    assert match(command)



# Generated at 2022-06-14 09:32:09.605974
# Unit test for function match
def test_match():
    command_1 = 'cat /etc/hosts'
    command_2 = 'cat linux.log'
    command_3 = 'cat /var/log'
    assert match(Command(script=command_1, output='cat: /etc/hosts: Is a directory'))
    assert not match(Command(script=command_2, output='cat: linux.log: Is a directory'))
    assert not match(Command(script=command_3, output='cat: /var/log: Is a directory'))



# Generated at 2022-06-14 09:32:16.170479
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/', '', 'cat: /etc/: Is a directory'))
    assert not match(Command('cat /etc/passwd', '', 'root:x:0:0:root:...'))
    assert not match(Command('cat /etc/passwod', '', "cat: '/etc/passwod': No such file or directory"))

# Generated at 2022-06-14 09:32:19.566620
# Unit test for function match
def test_match():
    assert match(Command(script='cat /boot',
                         output='cat: /boot: Is a directory'))
    assert not match(Command(script='cat /boot',
                             output='cat: /boot: Invalid argument'))
    assert not match(Command(script='cat /boot', output=''))

# Generated at 2022-06-14 09:32:22.344377
# Unit test for function match
def test_match():
    assert match(Command('cat ..', 'cat: ..: Is a directory'))
    assert not match(Command('echo test', ''))

# Unit test f

# Generated at 2022-06-14 09:32:34.692951
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt', 'cat: test.txt: Is a directory', ''))
    assert match(Command('cat -r test.txt', 'cat: test.txt: Is a directory', ''))
    assert not match(Command('cat test.txt', 'test.txt', ''))
    assert not match(Command('cat -r test.txt', 'test.txt', ''))


# Generated at 2022-06-14 09:32:47.025152
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/abc/def/12_ghi.txt',
                         '/etc/abc/def/12_ghi.txt',
                         'cat: /etc/abc/def/12_ghi.txt: Is a directory\n'))
    assert not match(Command('cat /etc/abc/def/12_ghi.txt',
                             '/etc/abc/def/12_ghi.txt',
                             'cat: /etc/abc/def/12_ghi.txt: No such file or directory\n'))
    assert not match(Command('cat /etc/abc/def/12_ghi.txt',
                             '/etc/abc/def/12_ghi.txt',
                             'cat: /etc/abc/def/12_ghi.txt: Is a directory'))



# Generated at 2022-06-14 09:32:50.412561
# Unit test for function match
def test_match():
    command = Command('cat ~/src', 'cat: ~/src: Is a directory')
    assert match(command)
    command = Command('cat ~/.vimrc', 'cat: ~/.vimrc: No such file or directory')
    assert not match(command)


# Generated at 2022-06-14 09:32:55.181299
# Unit test for function match
def test_match():
    # Test no cat
    assert not match(Command('echo "toto"'))
    # Test cat with directory
    assert match(Command('cat /tmp'))
    # Test cat with file
    assert not match(Command('cat /tmp/toto'))



# Generated at 2022-06-14 09:32:56.928715
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory'))

# Generated at 2022-06-14 09:33:00.671893
# Unit test for function match
def test_match():
    assert match(Command('cat unknown', '', 'cat: unknown: Is a directory\n'))
    assert not match(Command('cat unknown', '', 'cat: unknown: No such file or directory\n'))

# Generated at 2022-06-14 09:33:05.277779
# Unit test for function match
def test_match():
    error = 'cat: foo: Is a directory'
    assert match(None, Command('cat foo', error))
    assert match(None, Command('cat foo bar baz', error))
    assert not match(None, Command('cat', error))
    assert not match(None, Command('cat foo bar baz', ''))
    assert not match(None, Command('cat foo', ''))


# Generated at 2022-06-14 09:33:08.389901
# Unit test for function match
def test_match():
    assert match(Command(script='cat /etc/passwd'))
    assert not match(Command(script=' cat /etc/passwd'))


# Generated at 2022-06-14 09:33:10.740752
# Unit test for function match
def test_match():
    assert match(Command('cat /etc', None, 'cat: /etc: Is a directory'))

# Generated at 2022-06-14 09:33:15.749217
# Unit test for function match
def test_match():
    assert match(Command('cat Respositories', 'cat: Respositories: Is a directory', '', 0, None))
    assert not match(Command('cat Respositories', 'Respositories', '', 0, None))


# Generated at 2022-06-14 09:33:28.567241
# Unit test for function match
def test_match():
    assert match(Command(script='cat foo_dir', output='cat: foo_dir: Is a directory\n'))


# Generated at 2022-06-14 09:33:37.451361
# Unit test for function match
def test_match():
    assert match(Command('cat /proc', '', 'cat: /proc: Is a directory'))
    assert not match(Command('cat /proc', '', 'cat: /proc: No such file or directory'))
    assert not match(Command('cat /proc', '', 'Directory /proc'))
    assert not match(Command('hexdump /proc/self/stat', '', 'hexdump: /proc/self/stat: No such file or directory', '', '', ''))
    assert not match(Command('hexdump /proc/self/stat', '', 'hexdump: /proc/self/stat: Is a directory', '', '', ''))

# Generated at 2022-06-14 09:33:39.913843
# Unit test for function match
def test_match():
    assert match(Command('cat album',
                         "cat: album: Is a directory", ''))
    assert not match(Command('cat album', '', ''))


# Generated at 2022-06-14 09:33:45.320091
# Unit test for function match
def test_match():
    assert match(Command("cat test", "cat: test: Is a directory"))
    assert match(Command("cat test", "cat: test: Is a directory\n"))
    assert match(Command("cat test", "cat: test: Is a directory\n\n"))

    assert not match(Command("git branch", "cat: branch: No such file or directory"))

# Generated at 2022-06-14 09:33:48.462229
# Unit test for function match
def test_match():
	assert match(Command(script='cat test/file1.txt'))
	assert not match(Command(script='caaat test/file1.txt'))
	assert not match(Command(script='cat file1.txt'))


# Generated at 2022-06-14 09:33:53.830273
# Unit test for function match
def test_match():
    if match(command) == False:
        assert False
    else:
        assert True


# Generated at 2022-06-14 09:34:02.654792
# Unit test for function match
def test_match():
    output1 = 'cat: TestFile: Is a directory'
    output2 = 'cat: TestFile: No such file or directory'
    output3 = 'cat: TestFile: Input/output error'
    
    # Output of cat command
    assert (match(Command('cat TestFile', output=output1))
            and not match(Command('cat TestFile', output=output2)))
    # Test with other output
    assert not match(Command('cat TestFile', output=output3))
    # Test with two arguments
    assert not match(Command('cat TestFile TestFile', outpu=output1))


# Generated at 2022-06-14 09:34:06.460480
# Unit test for function match
def test_match():
    assert match(Command('cat /usr/lib'))
    assert match(Command('cat hello'))
    assert not match(Command('cat'))


# Generated at 2022-06-14 09:34:14.149309
# Unit test for function match
def test_match():
    command = Command('cat README.md', 'cat: README.md: Is a directory')
    assert match(command)
    command1 = Command('cat README.md', 'cat: README.md: No such file or directory')
    assert not match(command1)
    command2 = Command('ls README.md', 'cat: README.md: Is a directory')
    assert not match(command2)


# Generated at 2022-06-14 09:34:18.265875
# Unit test for function match
def test_match():
    assert match(Command(script='cat /etc/passwd', output='cat: /etc/passwd: is a directory',))
    assert not match(Command(script='cat /etc/passwd', output='user:x:0:0:root:/root:/bin/bash',))


# Generated at 2022-06-14 09:34:31.123614
# Unit test for function match
def test_match():
    assert match(Command('cat test', output='cat: test: Is a directory'))


# Generated at 2022-06-14 09:34:33.696044
# Unit test for function match
def test_match():
    command1 = 'cd /'
    command2 = 'cat /etc/hosts '
    assert not match(command1)
    assert match(command2)

# Generated at 2022-06-14 09:34:35.878854
# Unit test for function match
def test_match():
    command = Command('cat a', 'cat: a: Is a directory')
    assert match(command)



# Generated at 2022-06-14 09:34:36.745799
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt', 'cat: test.txt: Is a directory', ''))


# Generated at 2022-06-14 09:34:44.682135
# Unit test for function match
def test_match():
    # First case
    command = FakeCommand('cat /Users/home', '/Users/home')
    assert match(command)

    # Second case
    command = FakeCommand('cat /Users/home/foo.txt', '/Users/home/foo.txt')
    assert match(command) == False

    # Third case
    command = FakeCommand('cat file1 file2 file3', 'file1', 'file2', 'file3')
    assert match(command) == False


# Generated at 2022-06-14 09:34:50.495567
# Unit test for function match
def test_match():
    assert match(Command(script='cat',
                         stderr='cat: /etc/apt/sources.list.d/: Is a directory'))
    assert not match(Command(script='echo',
                             stderr='cat: /etc/apt/sources.list.d/: Is a directory'))
    assert not match(Command(script='cat dir',
                             stderr='cat: /etc/apt/sources.list.d/: Is a directory'))
    assert not match(Command(script='cat dir',
                             stderr='cat: /etc/apt/sources.list.d/: Is is fuck'))



# Generated at 2022-06-14 09:34:58.044753
# Unit test for function match
def test_match():
    command_list = ['cat /home/vagrant/my_project/README']
    command_list.append('cat: /home/vagrant/my_project/README: Is a directory')

# Generated at 2022-06-14 09:35:01.978932
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/',
                 'cat: /etc/: Is a directory'))
    assert not match(Command('cat /etc/passwd',
                 'good opt'))

# Generated at 2022-06-14 09:35:09.767829
# Unit test for function match
def test_match():
    # If the file exists, then this function should return True
    command = Command('cat somefile.txt')
    assert match(command)

    # If the file not exist, then this function should return False
    command = Command('cat nofile.txt')
    assert not match(command)

    # If there are other commands before 'cat', then it should return False
    command = Command('mkdir somefile.txt; cat somefile.txt')
    assert not match(command)


# Generated at 2022-06-14 09:35:18.499548
# Unit test for function match
def test_match():
    # test when such file exist
    command = Command('cat file', 'cat: file: Is a directory', '')
    assert match(command)

    # test when such file does not exist
    command = Command('cat file', 'cat: file: No such file or directory', '')
    assert not match(command)

    # test when the name of command is not cat
    command = Command('ls file', 'cat: file: Is a directory', '')
    assert not match(command)



# Generated at 2022-06-14 09:35:50.163829
# Unit test for function match
def test_match():
    assert match(Command(script='cat one two', output='cat: one: Is a directory', stderr='Is a directory'))
    assert match(Command(script='cat one two', output='cat: one: Is a directory', stderr='Is a directory'))

    assert not match(Command())
    assert not match(Command('cat one two'))
    assert not match(Command(script='cat one two', output='', stderr=''))
    assert not match(Command(script='cat one two', output='cat: one: Is a directory', stderr=''))
    assert not match(Command(script='cat one two', output='cat: one: Is a directory', stderr='No such file or directory'))


# Generated at 2022-06-14 09:35:55.436837
# Unit test for function match
def test_match():
    assert match(Command('cat foo', ''))
    assert not match(Command('cat foo bar', ''))
    assert not match(Command('cat foo/bar', 'cat: foo/bar: Is a directory\n'))
    assert match(Command('cat foo/bar', 'cat: foo/bar: No such file or directory\n'))



# Generated at 2022-06-14 09:35:57.046183
# Unit test for function match
def test_match():
    command = 'cat test'
    assert match(command) == None



# Generated at 2022-06-14 09:36:04.269062
# Unit test for function match
def test_match():
    assert match(Command('cat file', '', '', '', '', 1))
    assert match(Command('cat file', '', '', '', 'cat: file: Is a directory', 1))
    assert match(Command('cat file', '', '', '', 'cat: file: Is a directory', 1))
    assert not match(Command('cat /dev/null', '', '', '', '', 1))


# Generated at 2022-06-14 09:36:09.230975
# Unit test for function match
def test_match():
    assert match(Command('cat test', ''))
    assert match(Command('cat test', 'cat: test: Is a directory'))
    assert not match(Command('cat test', 'test'))
    assert not match(Command('cat test', 'cat: test: No such file or directory'))



# Generated at 2022-06-14 09:36:18.037787
# Unit test for function match
def test_match():
    assert match(Command('cat non-existent-file', output='cat: non-existent-file: No such file or directory'))
    assert not match(Command('cat blah blah blah'))
    assert not match(Command('cat /tmp/non-existent-file', output='cat: /tmp/non-existent-file: No such file or directory'))
    assert not match(Command('ls /tmp', output='total 128\ndrwxrwxrwt  6 root root  200 Oct  3 12:49 ..'))


# Generated at 2022-06-14 09:36:20.278320
# Unit test for function match
def test_match():
	assert match('cat /home/mao/Desktop')
	assert not match('ls /home/mao/Desktop')


# Generated at 2022-06-14 09:36:24.362879
# Unit test for function match
def test_match():
    assert match(Command('cat foo', 'cat: foo: Is a directory', ''))
    assert not match(Command('cat foo', '', ''))
    assert not match(Command('foo', 'cat: foo: Is a directory', ''))


# Generated at 2022-06-14 09:36:27.527052
# Unit test for function match
def test_match():
    assert not match(Command('', '', ''))
    assert match(Command('cat foo', '', 'cat: foo: Is a directory'))


# Generated at 2022-06-14 09:36:33.070112
# Unit test for function match
def test_match():
    command_with_output = Command('cat', 'cat: foo.txt: Is a directory', '')
    assert match(command_with_output)
    command_without_cat = Command('ls', 'cat: foo.txt: Is a directory', '')
    assert not match(command_without_cat)

# Generated at 2022-06-14 09:37:23.059812
# Unit test for function match
def test_match():
    assert match(Command('cat root', output='cat: root: Is a directory'))
    assert not match(Command('cat root', output=' '))


# Generated at 2022-06-14 09:37:31.598761
# Unit test for function match
def test_match():
    # Testing successful match
    command1 = Command("cat /etc/passwd")
    assert match(command1)

    # Testing successful match #2
    command2 = Command("cat /etc/");
    assert match(command2)

    # Testing unsuccessful match
    command3 = Command("cat file.txt")
    assert not match(command3)

    # Testing unsuccessful match #2
    command4 = Command("cat")
    assert not match(command4)

    # Testing unsuccessful match #3
    command5 = Command("cat file1.txt file2.txt")
    assert not match(command5)



# Generated at 2022-06-14 09:37:36.134485
# Unit test for function match
def test_match():
    command = Command('cat test_file')
    assert match(command) is None

    command = Command('cat test_dir')
    assert match(command) == True

    command = Command('ls test_dir; cat test_file')
    assert match(command) is None


# Generated at 2022-06-14 09:37:43.504572
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt', 'cat: test.txt: Is a directory',
        '', '', '', ''))
    assert not match(Command('cat test.txt', '', '', '', '', ''))
    assert not match(Command('ls test.txt', 'cat: test.txt: Is a directory',
        '', '', '', ''))


# Generated at 2022-06-14 09:37:45.118742
# Unit test for function match
def test_match():
    command = Command("cat test.txt", "")
 
    assert not match(command)

# Generated at 2022-06-14 09:37:48.969187
# Unit test for function match
def test_match():
    command = Command('cat /tmp', '/tmp/file.txt')
    assert match(command)
    command = Command('cat /tmp/file.txt', '/tmp/file.txt')
    assert not match(command)


# Generated at 2022-06-14 09:38:00.042877
# Unit test for function match
def test_match():
    assert match(Command(script="cat README",
                         output="cat: README: Is a directory"))
    assert match(Command(script="cat ~/test",
                         output="cat: /home/user/test: Is a directory"))
    assert not match(Command(script="cat /tmp/test",
                             output="cat: /tmp/test: Is a directory"))
    assert not match(Command(script="cat /tmp/test/",
                             output="cat: /tmp/test/: Is a directory"))
    assert not match(Command(script="cat /tmp/test",
                             output="cat /tmp/test"))
    assert not match(Command(script="cat test",
                             output="myText"))



# Generated at 2022-06-14 09:38:04.488151
# Unit test for function match
def test_match():
	assert match(Command(
        script='cat -n test',
        output='cat: test: Is a directory'))
	assert not match(Command(
        script='cat -n test',
        output='cat: test: No such file or directory'))


# Generated at 2022-06-14 09:38:15.610205
# Unit test for function match
def test_match():
    assert match(Command("cat /usr/bin/", output = 'cat: /usr/bin/: Is a directory'))
    assert not match(Command("cat /usr/bin/", output = 'c: /usr/bin/: No such file or directory'))
    assert not match(Command("cat /usr/bin/", output = 'c: /usr/bin/'))
    assert not match(Command("ls /usr/bin/", output = 'cat: /usr/bin/: Is a directory'))


# Generated at 2022-06-14 09:38:19.029468
# Unit test for function match
def test_match():
    assert match(Command(script='cat /home'))
    assert not match(Command(script='cat catfile.txt'))
    assert not match(Command(script='cd /home'))


# Generated at 2022-06-14 09:39:51.406253
# Unit test for function match
def test_match():
    assert match(Command("cat ./test_match/test_match.py"))
    assert not match(Command("cat ./test_match/test_match_not.py"))


# Generated at 2022-06-14 09:39:54.295040
# Unit test for function match
def test_match():
	assert match(Command('cat /', 'cat: /: Is a directory'))
	assert not match(Command('cat ./', 'cat: ./: Is a directory'))

# Generated at 2022-06-14 09:39:59.066229
# Unit test for function match
def test_match():
    assert match(Command('cat /etc', 
                         '/etc\nhosts\nhosts.allow\nhosts.deny\n'))
    assert not match(Command('cat /etc/hosts',
                              '127.0.0.1 localhost'))
