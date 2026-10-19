

# Generated at 2022-06-14 09:29:55.564704
# Unit test for function match
def test_match():
    command = Command('cat /tmp/asdf', 'cat: /tmp/asdf: Is a directory')
    assert match(command)



# Generated at 2022-06-14 09:30:00.079385
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory\n'))
    assert not match(Command('echo test', 'echo test'))
    assert not match(Command('cat test', 'test'))


# Generated at 2022-06-14 09:30:09.725396
# Unit test for function match
def test_match():
    assert match(Command('cat', '', 'cat: blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah'))
    assert not match(Command('cat', '', 'cat: cat: blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah'))


# Generated at 2022-06-14 09:30:18.153562
# Unit test for function match
def test_match():
    assert match(Command('cat /path/to/file',
                         '/path/to/file: is a directory\n'))
    assert not match(Command('cat /path/to/file',
                             '/path/to/file: No such file or directory'))
    assert not match(Command('cat /path/to/file',
                             '/path/to/file: is a file\n'))
    assert not match(Command('mv -f /path/to/file',
                             '/path/to/file: No such file or directory'))


# Generated at 2022-06-14 09:30:20.658164
# Unit test for function match
def test_match():
    assert match(
        Command('cat /etc/', '/etc/'),
        '/etc/'
    )


# Generated at 2022-06-14 09:30:28.482980
# Unit test for function match
def test_match():
    command = Command('cat test.txt 3', '/bin/bash')
    assert not match(command)
    command = Command('cat test.txt', '/bin/bash')
    assert not match(command)
    command = Command('cat test.txt', '/bin/bash',
                      'cat: test.txt: Is a directory')
    assert match(command)
    command = Command('cat /', '/bin/bash',
                      'cat: /: Is a directory')
    assert match(command)



# Generated at 2022-06-14 09:30:33.472014
# Unit test for function match
def test_match():
    from thefuck.rules.cat_is_directory import match
    assert match(Command('cat file', 'cat: file: Is a directory', 'file'))
    assert not match(Command('cat file', 'cat: file: Is not a directory', 'file'))


# Generated at 2022-06-14 09:30:36.343670
# Unit test for function match
def test_match():
    # If there is no error
    assert not match(Command('cat main.c'))
    # If the directory exists
    assert match(Command('cat main.c'))



# Generated at 2022-06-14 09:30:39.677694
# Unit test for function match
def test_match():
    command = Command('cat test', 'cat: test: Is a directory', '')
    assert match(command)


# Generated at 2022-06-14 09:30:41.014285
# Unit test for function match
def test_match():
    command = Command('cat /etc/')
    assert match(command)


# Generated at 2022-06-14 09:30:44.972363
# Unit test for function match
def test_match():
    assert match(Command('cat', 'cat: foo: Is a directory', ''))
    assert match(Command('cat', 'cat: bar: No such file or directory', ''))
    assert not match(Command('cat', 'cat: baz: Is a directory', ''))


# Generated at 2022-06-14 09:30:53.098411
# Unit test for function match
def test_match():
    assert match(Command('cat /home/username', '/home/username', 'cat: /home/username: Is a directory')).output == 'cat: /home/username: Is a directory'
    assert match(Command('cat /home/username/', '/home/username', 'cat: /home/username: Is a directory')).output == 'cat: /home/username: Is a directory'
    assert match(Command('cat /home/username/test.txt', '/home/username', 'test \n text \n')).output == 'test \n text \n'
    assert match(Command('cat /home/username/test.txt', '/home/username', 'cat: /home/username/test.txt: No such file or directory')).output == 'cat: /home/username/test.txt: No such file or directory'

# Generated at 2022-06-14 09:30:55.807330
# Unit test for function match
def test_match():
	assert match(Command('cat /usr/bin', '', 'cat: /usr/bin: Is a directory'))
	assert not match(Command('cat', '', ''))

# Generated at 2022-06-14 09:31:00.744640
# Unit test for function match
def test_match():
    # When cat path is a directory, return True
    assert match(Command('cat xxx', 'cat: xxx: Is a directory'))
    # When cat path is not a directory, return False
    assert not match(Command('cat xxx', 'cat: xxx: No such file or directory'))


# Generated at 2022-06-14 09:31:09.366490
# Unit test for function match
def test_match():
    assert not match(Command('ls foo', 'foo'))
    assert match(Command('cat foo', 'cat: foo: Is a directory'))
    assert match(Command('cat /foo', 
                         'cat: /foo: Is a directory'))
    assert match(Command('cat /foo bar', 
                         'cat: /foo: Is a directory'))
    assert not match(Command('rm /foo', 
                             'rm: /foo: Is a directory'))
    assert not match(Command('cat "foo bar"', 
                             'cat: foo bar: No such file or directory'))


# Generated at 2022-06-14 09:31:12.203105
# Unit test for function match
def test_match():
    assert match(Command('cat file.txt', 'cat: file.txt: Is a directory',
                         ('cat: ', 'file.txt', ': Is a directory')))
    assert not match(Command('cat file.txt', 'other error',
                             ('other error')))


# Generated at 2022-06-14 09:31:17.128768
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/'))


# Generated at 2022-06-14 09:31:20.286271
# Unit test for function match
def test_match():
    assert match(Command('cat test', (
            'cat: test: Is a directory\n', '')))
    assert not match(Command('cat test', (
            '', '')))

# Generated at 2022-06-14 09:31:22.984596
# Unit test for function match
def test_match():
    assert match(Command('cat a/', 'cat: a/: Is a directory', '/a/'))


# Generated at 2022-06-14 09:31:25.231955
# Unit test for function match
def test_match():
    assert match(Command('cat /dev', '', 'cat: /dev: Is a directory'))


# Generated at 2022-06-14 09:31:32.544228
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory\n'))
    assert not match(Command('cat test', 'cat: test: No such file or directory\n'))

# Generated at 2022-06-14 09:31:35.793244
# Unit test for function match
def test_match():
    import os

# Generated at 2022-06-14 09:31:37.108287
# Unit test for function match
def test_match():
    assert match('cat testfile')


# Generated at 2022-06-14 09:31:40.070003
# Unit test for function match
def test_match():
  assert match('cat /path/to/a/directory/')
  assert not match('cat /path/to/a/file')


# Generated at 2022-06-14 09:31:43.877452
# Unit test for function match
def test_match():
    assert match(Command('cat FILE', output='cat: FILE: Is a directory'))
    assert not match(Command('cat FILE1 FILE2', output='file1\nfile2'))


# Generated at 2022-06-14 09:31:53.105998
# Unit test for function match
def test_match():
    assert match(Command('cat path', 'cat: path: Is a directory', ''))
    assert not match(Command('cat path', '', ''))
    assert not match(Command('cat path', 'cat: path: No such file or directory', ''))
    assert not match(Command('cat path', 'cat: path: Is not a directory', ''))


# Generated at 2022-06-14 09:32:01.718806
# Unit test for function match
def test_match():
    assert match(Command('cat file1 file2', 'cat: file2: Is a directory', '', ''))
    assert match(Command('cat file1 dir', 'cat: dir: Is a directory', '', ''))
    assert match(Command('cat file1 dir/', 'cat: dir/: Is a directory', '', ''))
    assert not match(Command('cat file1 dir/file2', 'cat: dir/file2: Is a directory', '', ''))
    assert not match(Command('cat file1 dir2/file2', 'cat: dir2/file2: Is a directory', '', ''))
    assert not match(Command('cat file1 dir1/dir2/file2', 'cat: dir1/dir2/file2: Is a directory', '', ''))

# Generated at 2022-06-14 09:32:05.193571
# Unit test for function match
def test_match():
    assert match(Command('cat', 'cat: file: Is a directory\n'))
    assert not match(Command('cat', 'cat: file: No such file or directory\n'))

# Generated at 2022-06-14 09:32:07.499003
# Unit test for function match
def test_match():
    assert match(Command('cat test',None,'cat: test: Is a directory','',''))


# Generated at 2022-06-14 09:32:10.413890
# Unit test for function match
def test_match():
    assert True == match(Command('cat test.txt'))
    assert False == match(Command('cat ./test.txt'))


# Generated at 2022-06-14 09:32:16.916699
# Unit test for function match
def test_match():
    assert not match(Command('cat foo bar', stderr='cat: foo: Is a directory'))

    assert match(Command('cat foo bar', stderr='cat: foo: Is a directory',
                         script='cat foo bar'))



# Generated at 2022-06-14 09:32:23.733272
# Unit test for function match
def test_match():
    c = Command('cat test', 'cat: test: Is a directory')
    assert match(c)
    # test for cat command with only flags
    c = Command('cat -n test test1', 'cat: test: Is a directory')
    assert match(c)
    c = Command('cat test', 'cat: test: Is a directory')
    assert match(c)
    # test for cat command without space between command & file
    c = Command('cat test', 'cat: test: Is a directory')
    assert match(c)
    # test with 2 files
    c = Command('cat test test1 test2', 'cat: test: Is a directory')
    assert match(c)
    # test for non-existent file
    c = Command('cat test', 'cat: test: No such file or directory')
    assert not match(c)

# Generated at 2022-06-14 09:32:29.331456
# Unit test for function match
def test_match():
    assert match('cat /tmp/bash')
    assert not match('cat /tmp/bash/get')
    assert not match('cat /tmp/bash/')


# Generated at 2022-06-14 09:32:33.300126
# Unit test for function match
def test_match():
    assert match(Command('cat file_name'))
    assert not match(Command('cat'))
    assert not match(Command('cat /etc/passwd', '', 'cat: /etc/passwd: Is a directory', '', 1))


# Generated at 2022-06-14 09:32:38.378882
# Unit test for function match
def test_match():
    command = Command('cat temp_dir', 'cat: temp_dir: Is a directory')
    assert match(command)

    command = Command('cat temp.f', 'cat: temp.f: No such file or directory')
    assert not match(command)


# Generated at 2022-06-14 09:32:48.772169
# Unit test for function match
def test_match():
    """
    match should return True when given a command
    that starts with 'cat' and the second argument
    is a valid directory name, otherwise it should
    return False.
    """
    # GIVEN a 'cat' command with a valid directory name
    command = Command('cat validDir')
    
    # WHEN match() is called
    result = match(command)

    # THEN it should return True
    result | should.be.true
    
    # GIVEN a 'cat' command with an invalid directory name
    command = Command('cat invalidDir')

    # WHEN match() is called
    result = match(command)

    # THEN it should return False
    result | should.be.false


# Generated at 2022-06-14 09:32:51.960882
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory'))
    assert not match(Command('cat test', 'test'))


# Generated at 2022-06-14 09:32:57.241740
# Unit test for function match
def test_match():
    assert match(Command('cat $HOME', 'cat: $HOME: Is a directory'))
    assert match(Command('cat $HOME', 'cat: $HOME: Datei oder Verzeichnis nicht gefunden'))
    assert not match(Command('cat $HOME', 'hello world'))


# Generated at 2022-06-14 09:33:02.401283
# Unit test for function match
def test_match():
    with open('temp', 'w+') as file:
        file.write('Testing')
    
    command = Command('cat temp', '/')
    assert match(command)
    os.remove('temp')

    command = Command('cat', '/')
    assert not match(command)

    command = Command('ls temp', '/')
    assert not match(command)


# Generated at 2022-06-14 09:33:05.507445
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/passwd', 'cat: /etc/passwd: Is a directory', ''))
    assert match(Command('cat /etc/passwd', 'cat: /etc/passwd: Is a directory', '')) == False


# Generated at 2022-06-14 09:33:15.757201
# Unit test for function match
def test_match():
    assert match(Command('cat abc', 'cat: abc: is a directory'))
    assert not match(Command('cat abc', ''))
    assert not match(Command('cat abc', 'cat: abc: No such file or directory'))



# Generated at 2022-06-14 09:33:20.248733
# Unit test for function match
def test_match():
    assert match(Command("cat /etc/passwd", "/etc/passwd\ndump file"))
    assert not match(Command("cat /etc/passwd", "dump file"))
    assert not match(Command("cat /etc/passwd/foo", "dump file"))



# Generated at 2022-06-14 09:33:25.144416
# Unit test for function match
def test_match():
    assert match(Command('cat', 'fhqwhgads', output='cat: fhqwhgads: Is a directory'))
    assert not match(Command('cat', 'fhqwhgads', output='fhqwhgads: Is a directory'))



# Generated at 2022-06-14 09:33:35.500312
# Unit test for function match
def test_match():

    # Test 1: Command returns error
    with open('/tmp/test_file', 'w') as f:
        f.write('')
    os.chmod('/tmp/test_file', 0o222)
    command = Command('cat /tmp/test_file')
    assert match(command)

    # Test 2: Command returns error for directory
    command = Command('cat /tmp')
    assert match(command)
    os.chmod('/tmp/test_file', 0o777)
    os.remove('/tmp/test_file')

    # Test 3: Command does not return error
    command = Command('cat /bin')
    assert not match(command)



# Generated at 2022-06-14 09:33:37.371965
# Unit test for function match
def test_match():
    assert match(Command(script='cat hello'))


# Generated at 2022-06-14 09:33:39.670282
# Unit test for function match
def test_match():
    command = Command('cat /bin', '')
    assert match(command)


# Generated at 2022-06-14 09:33:43.509429
# Unit test for function match
def test_match():
    from thefuck.main import Command
    assert match(Command('cat', 'cat: inputfile: Is a directory', ''))
    assert not match(Command('cat', 'oops: inputfile', ''))



# Generated at 2022-06-14 09:33:50.097102
# Unit test for function match
def test_match():
    # set up mock
    script = 'cat path_to_dir'
    command = type('x', (object,), {'script': script, 'script_parts': script.split(), 'output': 'cat: path_to_dir: Is a directory'})

    # unit test
    assert match(command)

    # set up mock
    command = type('x', (object,), {'script': script, 'script_parts': script.split(), 'output': 'cat: path_to_dir: No such file or directory'})
    
    # unit test
    assert not match(command)


# Generated at 2022-06-14 09:33:59.912136
# Unit test for function match
def test_match():
    assert match(Command(script = 'cat file.txt', output = 'cat: file.txt: Is a directory'))
    assert not match(Command(script = 'cat file.txt', output = 'cat: file.txt: No such file or directory'))
    assert not match(Command(script = 'cat file.txt', output = 'The file is too large to display'))


# Generated at 2022-06-14 09:34:02.291189
# Unit test for function match
def test_match():
    assert(match(Command("cat ./test/", "cat: ./test/: Is a directory")) == True)

# Generated at 2022-06-14 09:34:14.244552
# Unit test for function match
def test_match():
    assert match(Command('cat /dev', None, 'cat: /dev: Is a directory', ''))
    assert not match(Command('cat /de', None, 'cat: /de: No such file or directory', ''))


# Generated at 2022-06-14 09:34:17.966429
# Unit test for function match
def test_match():
    # True case
    assert match(Command('cat file/', 'cat: file/: Is a directory\n', '', 0))
    # False case
    assert not match(Command('ls file/', 'cat: file/: Is a directory\n', '', 0))


# Generated at 2022-06-14 09:34:22.349669
# Unit test for function match
def test_match():
    assert match(Command('cat nop',
                         output='cat: nop: Is a directory'))
    assert not match(Command('cat nop',
                             output='cat: nop: No such file or directory'))



# Generated at 2022-06-14 09:34:24.326266
# Unit test for function match
def test_match():
    assert match(Command('cat /home'))
    assert not match(Command('cat xyz'))



# Generated at 2022-06-14 09:34:29.111078
# Unit test for function match
def test_match():
    command_1 = "cat makefile"
    assert match(command_1) == False
    command_2 = "cat /home/"
    assert match(command_2) == True


# Generated at 2022-06-14 09:34:30.112392
# Unit test for function match
def test_match():
    assert match(Command(script='cat /etc/passwd /usr/lib',
                         output='''cat: /usr/lib: Is a directory'''))



# Generated at 2022-06-14 09:34:31.011633
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory'))


# Generated at 2022-06-14 09:34:35.333841
# Unit test for function match
def test_match():
    assert match(Command('cat test', ''))
    assert match(Command('cat src/test/java/com', ''))
    assert not match(Command('cat src/test/java/com/test.java', ''))
    assert not match(Command('cat test', ''))



# Generated at 2022-06-14 09:34:39.126629
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/ssh/sshd_config'))
    assert match(Command('cat /dev/null > /etc/ssh/sshd_config'))


# Generated at 2022-06-14 09:34:44.525536
# Unit test for function match
def test_match():
    assert(match(Command('cat test.txt test.py', 'cat: test.txt: Is a directory')))
    assert(not match(Command('cat test.txt test.py', 'test.py testing')))
    assert(not match(Command('ls test.txt', 'something')))


# Generated at 2022-06-14 09:35:07.480136
# Unit test for function match
def test_match():
    assert match(Command('cat test', output='cat: test: Is a directory\n'))
    assert not match(Command('cat test', output='cat: test: No such file or directory\n'))


# Generated at 2022-06-14 09:35:13.149454
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/host', 'cat: /etc/host: Is a directory', ''))
    assert not match(Command('cat /etc/host', "cat: '/etc/host': No such file or directory", ''))

# Generated at 2022-06-14 09:35:16.263080
# Unit test for function match
def test_match():
    assert match(Command('cat /home', 'cat: /home: Is a directory'))
    assert not match(Command('cat /home/file.txt', ''))


# Generated at 2022-06-14 09:35:19.599374
# Unit test for function match
def test_match():
    assert match(Command('cat asdf', 'cat: asdf: Is a directory'))
    assert not match(Command('cat asdf', 'cat: asdf: No such file or directory'))



# Generated at 2022-06-14 09:35:21.875205
# Unit test for function match
def test_match():
    command = Command('cat README.md', 'cat: README.md: Is a directory')
    assert match(command)



# Generated at 2022-06-14 09:35:25.433423
# Unit test for function match
def test_match():
    def assert_match(command):
        return match(Command(script=command))

    assert assert_match('cat file')
    assert assert_match('cat dir')
    assert not assert_match('cat')


# Generated at 2022-06-14 09:35:37.512573
# Unit test for function match
def test_match():
    is_dir = os.path.isdir
    os_path_isdir = os.path.isdir
    os.path.isdir = lambda x: True
    assert match(Command('cat a'))
    assert match(Command('cat a b c'))
    assert match(Command('cat a b c', ''))

    assert not match(Command('cat a', ''))
    assert not match(Command('cat a', 'a\nb\nc'))
    assert not match(Command('cat a', '', 'a\nb\nc'))
    assert not match(Command('cat a b c', 'a\nb\nc'))

    # Restore state
    os.path.isdir = os_path_isdir


# Generated at 2022-06-14 09:35:45.851423
# Unit test for function match
def test_match():
    assert match(Command('cat "/dev/null"',
                        stdout='cat: /dev/null: Is a directory',
                        stderr='',
                        script='cat "/dev/null"'))

    assert match(Command('cat README.md',
                        stdout='cat: README.md: Is a directory',
                        stderr='',
                        script='cat README.md'))

    assert not match(Command('cat test.txt',
                        stdout='some text',
                        stderr='',
                        script='cat test.txt'))



# Generated at 2022-06-14 09:35:50.223139
# Unit test for function match
def test_match():
    assert match(Command(script='cat oops', output='cat: oops: Is a directory\n'))
    assert not match(Command(script='cat oops', output='oops\n'))

# Generated at 2022-06-14 09:35:53.240115
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/hosts', '/etc/hosts')) == True
    assert match(Command('cat /etc/hosts', 'hosts')) == False
    assert match(Command('cat test', 'test')) == False
    assert match(Command('cat', 'cat')) == False


# Generated at 2022-06-14 09:36:37.238540
# Unit test for function match
def test_match():
    assert match(Command('cat test'))
    assert not match(Command('ls test'))
    assert match(Command('cat test/'))
    assert not match(Command('ls test/'))
    assert not match(Command('cat file_that_doesnt_exist'))


# Generated at 2022-06-14 09:36:39.785057
# Unit test for function match
def test_match():
    assert match(Command("cat /var/log/", "/var/log/"))
    assert not match(Command("cat file", "file"))


# Generated at 2022-06-14 09:36:41.803422
# Unit test for function match
def test_match():
    command = Command('cat test.txt', 'cat: test.txt: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:36:44.644001
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory',
                         '', '-bash', ''))


# Generated at 2022-06-14 09:36:47.446439
# Unit test for function match
def test_match():
	assert match(Command('cat folder', 'cat: folder: Is a directory'))
	assert not match(Command('cat file', 'file content'))

# Generated at 2022-06-14 09:36:54.029240
# Unit test for function match
def test_match():
    assert match(Command('cat /proc/cpuinfo', '', 'cat: /proc/cpuinfo: Is a directory'))
    assert not match(Command('cat /proc/cpuinfo', '', 'cat: /proc/cpuinfo: Permission denied'))
    assert match(Command('cat /proc/cpuinfo', '', 'cat: /proc/cpuinfo: Permission denied'))


# Generated at 2022-06-14 09:36:57.966508
# Unit test for function match
def test_match():
    assert match(Command(script = 'cat file.txt', output = 'cat: file.txt: Is a directory')) == True
    assert match(Command(script = 'cat file.txt', output = 'cat file.txt')) == False



# Generated at 2022-06-14 09:36:59.975231
# Unit test for function match
def test_match():
    match_output = match(command)
    assert match_output == True

# Generated at 2022-06-14 09:37:08.010755
# Unit test for function match
def test_match():
    with patch('os.path.isdir') as mock_function:
        mock_function.return_value = True
        command = Command('echo "hello" | cat /etc/letsencrypt')
        assert match(command) is True

        command = Command('cat /etc/letsencrypt')
        assert match(command) is True

        command = Command('echo "hello" | cat /etc/letsencrypt/name.pem')
        assert match(command) is False



# Generated at 2022-06-14 09:37:10.022802
# Unit test for function match
def test_match():
    command = Command('cat test', 'cat: test: Is a directory')
    assert match(command)



# Generated at 2022-06-14 09:38:35.258856
# Unit test for function match
def test_match():
    assert match(Command("cat foo.txt", "cat: foo.txt: Is a directory"))
    assert not match(Command("ls foo.txt", ""))


# Generated at 2022-06-14 09:38:39.620760
# Unit test for function match
def test_match():
    assert match(Command('cat file', stderr='cat: file: Is a directory'))
    assert not match(Command('cat file', stderr='cat: file: File not found'))
    assert not match(Command('cat file', stderr='nothing'))


# Generated at 2022-06-14 09:38:47.301618
# Unit test for function match
def test_match():
    cmd = Command("cat package.json", "cat: package.json: Is a directory")
    assert match(cmd)

    cmd = Command("cat package.json", "cat: package.json: No such file or directory")
    assert not match(cmd)

    cmd = Command("cat package.json", "cat: package.json: No such file or directory")
    assert not match(cmd)


# Generated at 2022-06-14 09:38:49.785292
# Unit test for function match
def test_match():
    command = Command('cat index.html test.js',
                      'cat: index.html: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:38:54.877990
# Unit test for function match
def test_match():
    from thefuck.types import Command
    wrong_command = Command('cat file1.txt file2.txt', 'cat: file2.txt: Is a directory', '')
    right_command = Command('cat file1.txt', '', '')
    assert match(wrong_command)
    assert not match(right_command)


# Generated at 2022-06-14 09:38:58.653834
# Unit test for function match
def test_match():
    command = Command(script='cat file', stderr='cat: file: Is a directory\n')
    assert match(command)
    command.script_parts[1] = 'test'
    assert match(command)
    command.script_parts[1] = '~'
    assert not match(command)



# Generated at 2022-06-14 09:39:02.900256
# Unit test for function match
def test_match():
    assert match(Command('cat doesnt_exist.txt', 'cat: doesnt_exist.txt: No such file or directory\n'))
    assert not match(Command('cat --help', ''))


# Generated at 2022-06-14 09:39:06.908778
# Unit test for function match
def test_match():

    test_command = type('test', (object,), {'script':'cat /usr/local/bin',
        'output':'cat: /usr/local/bin: Is a directory'})

    assert match(test_command)




# Generated at 2022-06-14 09:39:10.676200
# Unit test for function match
def test_match():
    assert match(Command('cat ./test_file.txt',
        'cat: ./test_file.txt: Is a directory'))
    asser

# Generated at 2022-06-14 09:39:14.696215
# Unit test for function match
def test_match():
    command = Command('cat abcd', 'cat: abcd: Is a directory\n')
    result = match(command)
    assert result == True
