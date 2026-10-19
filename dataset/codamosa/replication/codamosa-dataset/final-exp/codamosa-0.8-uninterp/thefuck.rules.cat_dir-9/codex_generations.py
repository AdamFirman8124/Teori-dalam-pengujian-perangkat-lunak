

# Generated at 2022-06-14 09:30:03.638414
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/passwd', 'cat: /etc/passwd: Is a directory'))
    assert not match(Command('cat /tmp', 'cat: /etc/passwd: Is a directory'))
    assert not match(Command('cat file not exist', 'cat: file: No such file or directory'))
    assert not match(Command('cat', 'cat: invalid option -- a\nTry `cat --help\' for more information.'))

# Generated at 2022-06-14 09:30:09.034249
# Unit test for function match
def test_match():
    assert match(Command('cat', 'cat: test.txt: Is a directory'))
    assert match(Command('cat', 'cat: foo: No such file or directory'))
    assert not match(Command('cat', 'foo'))
    assert not match(Command('cat', 'cat: test.txt: No such file or directory'))


# Generated at 2022-06-14 09:30:11.750078
# Unit test for function match
def test_match():
    assert match(Command('cat file', 'cat: not a directory'))
    assert not match(Command('cat file', 'cat: not a directory'))


# Generated at 2022-06-14 09:30:19.911055
# Unit test for function match
def test_match():
    assert match(Command('cat *.py', 'cat: *.py: No such file or directory'))
    assert not match(Command('cat *.py', 'cat: *.py: Is a directory'))
    assert not match(Command('cat *.py', ''))


# Generated at 2022-06-14 09:30:22.416786
# Unit test for function match
def test_match():
    command = Command('cat /home/test')
    assert match(command)



# Generated at 2022-06-14 09:30:27.384586
# Unit test for function match
def test_match():
    assert match(Command('cat /usr', output='cat: /usr: Is a directory'))
    assert match(Command('cat nope', output='cat: nope: No such file or directory'))
    assert not match(Command('cat nope', output='cat: nope: No such file or directory'))


# Generated at 2022-06-14 09:30:29.438572
# Unit test for function match
def test_match():
    assert match(Command('cat foo',
                         'cat: foo: Is a directory',
                         ''))

# Generated at 2022-06-14 09:30:32.542454
# Unit test for function match
def test_match():
    output = "cat: test/: Is a directory"
    command = Command("cat test/", output)
    assert match(command)



# Generated at 2022-06-14 09:30:39.815770
# Unit test for function match
def test_match():
    # positive cases
    assert match(Command('cat /etc/passwd', '/etc/passwd: '))
    assert match(Command('cat /etc', 'cat: /etc: Is a directory'))
    # negative cases
    assert not match(Command('cat /etc/passwd', '/etc/passwd: Permission denied'))
    assert not match(Command('cat /etc/passwd', 'cat: /etc/passwd: No such file or directory'))
    assert not match(Command('ls /etc/passwd', '/etc/passwd: '))


# Generated at 2022-06-14 09:30:45.081865
# Unit test for function match
def test_match():
    command = Command('cat', 'cat: /etc/resolv.conf: Is a directory')
    assert match(command)
    command = Command('cat', 'cat: /etc/resolv.conf: Is not a directory')
    assert not match(command)
    command = Command('cd', 'cd: /etc/resolv.conf: Is a directory')
    assert not match(command)


# Generated at 2022-06-14 09:30:57.123325
# Unit test for function match
def test_match():
    command = type('Command', (object,),
                   {'script': "cat /dir/dir  ",
                    'script_parts': ["cat", "/dir/dir"],
                    'output': "cat: /dir/dir: Is a directory"})
    assert match(command)
    command.script_parts[1] = "/dir/file"
    assert not match(command)
    command.output = "cat: /dir/dir: No such file or directory"
    assert not match(command)


# Generated at 2022-06-14 09:31:02.341314
# Unit test for function match
def test_match():
    assert match(Command(script='cat ', stderr='cat: ')) is False
    assert match(Command(script='cat asdf', stderr='cat: asdf: No such file or directory')) is True
    assert match(Command(script='cat asdf', stderr='cat: asdf: Is a directory')) is True

# Generated at 2022-06-14 09:31:06.618736
# Unit test for function match
def test_match():
    assert match(command='cat this_directory')
    assert match(command='cat this_file') # cat is fine
    assert not match(command='ls this_directory') # directory is ok
    assert not match(command='ls this_file') # file is ok

# Generated at 2022-06-14 09:31:12.611376
# Unit test for function match
def test_match():
    # Unit test for case: cat: path/goes/here: Is a directory
    assert match(Command('cat path/goes/here', 'cat: path/goes/here: Is a directory\n'))


# Generated at 2022-06-14 09:31:24.615216
# Unit test for function match
def test_match():
    command = type('Command', (object,), {
        'script': 'cat /etc/bash_completion.d',
        'script_parts': ['cat', '/etc/bash_completion.d'],
        'output': 'cat: /etc/bash_completion.d: Is a directory'})

    assert match(command) is True

    command = type('Command', (object,), {
        'script': 'cat /root',
        'script_parts': ['cat', '/root'],
        'output': 'cat: /root: Permission denied'})

    assert match(command) is False


# Generated at 2022-06-14 09:31:28.769843
# Unit test for function match
def test_match():
    assert match(Command('cat /tmp'))
    assert not match(Command('cat'))
    assert not match(Command('cat /tmp/toto'))
    assert not match(Command('ls /tmp'))


# Generated at 2022-06-14 09:31:33.727028
# Unit test for function match
def test_match():
    assert match(Command('cat hello', output='cat: hello: Is a directory'))
    assert not match(Command('cat hello', output='Not a directory'))



# Generated at 2022-06-14 09:31:42.729414
# Unit test for function match
def test_match():
    command_1 = Command('cat /etc/abc def ghi')
    command_2 = Command('cat /etc/abc')
    command_3 = Command('cat /etc/def /etc/ghi')
    command_4 = Command('echo "hello" > /etc/abc')
    command_5 = Command('echo "hello" > "/root"')
    command_6 = Command('cat "/root"')
    assert match(command_1)
    assert match(command_2)
    assert not match(command_3)
    assert not match(command_4)
    assert match(command_5)
    assert match(command_6)


# Generated at 2022-06-14 09:31:50.413312
# Unit test for function match
def test_match():
    assert match(Command(script='', output='cat: my_dir_name: Is a directory'))
    assert not match(Command(script='', output='cat: my_file_name: No such file or directory'))
    assert not match(Command(script='', output='cat: my_dir_name: some error'))



# Generated at 2022-06-14 09:31:55.533722
# Unit test for function match
def test_match():
	assert match("cat shit.txt")
	assert match("cat")
	assert match("cat .git")
	assert not match("cat --help")
	assert not match("catt -h")


# Generated at 2022-06-14 09:32:02.197670
# Unit test for function match
def test_match():
    assert match(Command('cat foo', 'cat: foo: Is a directory', '', 3))
    assert not match(Command('cat foo', '', '', 3))
    assert not match(Command('catt foo', 'cat: foo: Is a directory', '', 3))


# Generated at 2022-06-14 09:32:06.024816
# Unit test for function match
def test_match():
    assert match(Command('cat dir'))
    assert not match(Command('ls dir'))
    assert not match(Command('cat files'))

# Unit tests for function get_new_comman

# Generated at 2022-06-14 09:32:09.866126
# Unit test for function match
def test_match():
    command = Command("cat /home/jianwei/git/thefuck","cat: /home/jianwei/git/thefuck: Is a directory")
    assert match(command)


# Generated at 2022-06-14 09:32:13.862870
# Unit test for function match
def test_match():
    assert match(Command('./cat.txt', output='cat: txt: Is a directory'))
    assert not match(Command('ls', output='ls: txt: Is a directory'))



# Generated at 2022-06-14 09:32:16.874599
# Unit test for function match
def test_match():
    command = Command("cat file.txt")
    assert match(command) is False
    command = Command("cat foldername")
    assert match(command) is True



# Generated at 2022-06-14 09:32:20.057123
# Unit test for function match
def test_match():
    # Expect not to match
    assert match(command=Command('cat /home/test/testfile')) is False

    # Expect to match
    assert match(command=Command('cat /home/test')) is True
    assert match(command=Command('cat /home/test/')) is True


# Generated at 2022-06-14 09:32:29.080850
# Unit test for function match
def test_match():
    command = Command('cat file.txt')
    assert not match(command)

    command = Command('cat file.txt', 'cat: file.txt: No such file or directory')
    assert not match(command)

    command = Command('cat file.txt', 'cat: file.txt: Is a directory')
    assert match(command, '/tmp/foo/')

    command = Command('cat file.txt', 'cat: file.txt: Is a directory')
    assert match(command, '/tmp/foo')

    command = Command('cat file.txt', 'cat: file.txt: Is a directory')
    assert match(command, '/tmp')


# Generated at 2022-06-14 09:32:31.283361
# Unit test for function match
def test_match():
    assert match(Command('cat testdir'))
    assert not match(Command('ls testdir'))


# Generated at 2022-06-14 09:32:33.709186
# Unit test for function match
def test_match():
     assert match(Command('cat /var/www', 'cat: /var/www: Is a directory')) is True


# Generated at 2022-06-14 09:32:46.101822
# Unit test for function match
def test_match():
    command = Command(script="cat testfile.txt",
                      stderr=u'cat: testfile.txt: Is a directory',
                      output=u'')
    os.path.isdir = lambda o: True
    assert match(command)

    command = Command(script="cat testfile.txt",
                      stderr=u'cat: testfile.txt: Is a directory',
                      output=u'')
    os.path.isdir = lambda o: False
    assert not match(command)

    command = Command(script="cat testfile.txt",
                      stderr=u'cat: testfile.txt: Is a directory',
                      output=u'')
    os.path.isdir = lambda o: False
    assert not match(command)


# Generated at 2022-06-14 09:32:59.410997
# Unit test for function match
def test_match():
    assert match(Command('cat main.py', 'cat: main.py: Is a directory'))
    assert not match(Command('cat main.py', 'cat: main.py: No such file or directory'))



# Generated at 2022-06-14 09:33:05.694832
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/passwd', '/etc/passwd', '', Output('cat: /etc/passwd: Is a directory', '')))
    assert not match(Command('cat /etc/passwd', '', '', Output('', '')))
    assert not match(Command('cat /etc/passwd', '', '', Output('cat: /etc/passwd: Is a directory', '')))



# Generated at 2022-06-14 09:33:12.215569
# Unit test for function match
def test_match():
    assert match(Command('cat aa', '', '', 'cat: aa: Is a directory'))
    assert not match(Command('cat aa', '', '', 'cat: aa: No such file or directory'))
    assert not match(Command('cat aa', '', '', 'cat: aa: No directory'))
    assert not match(Command('cat aa', '', '', 'cat: aa:'))


# Generated at 2022-06-14 09:33:15.028832
# Unit test for function match
def test_match():
    command = Command('cat my_dir', '', 'cat: my_dir: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:33:18.584587
# Unit test for function match
def test_match():
    assert match(Command('cat /usr/share/', stderr='cat: /usr/share/: Is a directory'))
    assert not match(Command('cat /usr/share/', stderr='cat: /usr/share/: No such file or directory'))


# Generated at 2022-06-14 09:33:22.971460
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('cat README', 'cat: README: Is a directory'))
    assert not match(Command('ls README', 'cat: README: Is a directory'))
    assert not match(Command('cat README', ''))
    assert not match(Command('cat foo', 'cat: foo: No such file or directory'))



# Generated at 2022-06-14 09:33:27.665972
# Unit test for function match
def test_match():
    assert not match(Command('cat'))
    assert match(Command('cat foo'))
    assert not match(Command('cat foo', output='foo'))
    assert not match(Command('cat', output='cat: foo: Is a directory'))


# Generated at 2022-06-14 09:33:30.615410
# Unit test for function match
def test_match():
    command = Command('cat weird.txt', 'cat: weird.txt: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:33:35.616925
# Unit test for function match
def test_match():
    assert match(Command('cat Views/Home/index.php', 'cat: Views/Home/index.php: Is a directory'))
    assert not match(Command('cat not_exist', 'cat: not_exist: No such file or directory'))
    assert not match(Command('ls', ''))
    asser

# Generated at 2022-06-14 09:33:38.535583
# Unit test for function match
def test_match():
    assert match(Command('cat /root/'))
    assert not match(Command('ls /root/'))


# Generated at 2022-06-14 09:33:57.777330
# Unit test for function match
def test_match():
    assert match(Command('cat a', 'cat: a: Is a directory', '', 1))
    assert not match(Command('ls a', 'cat: a: Is a directory', '', 1))
    assert not match(Command('cat foo', 'foo', '', 1))


# Generated at 2022-06-14 09:34:01.327823
# Unit test for function match
def test_match():
    command = 'cat: folder: Is a directory'
    assert match(command)
    command = 'cat: folder: No such file or directory'
    assert not match(command)


# Generated at 2022-06-14 09:34:06.217636
# Unit test for function match
def test_match():
    assert match(Command('cat a'))
    assert not match(Command('cat a', 'b'))
    assert not match(Command('cat', 'a'))
    assert not match(Command('cat a', os.getcwd()))

# Generated at 2022-06-14 09:34:14.404135
# Unit test for function match
def test_match():
    command = Command('cat testdir', 'cat: testdir: Is a directory')
    assert match(command)

    command = Command('cat testdir', 'cat: testdir: No such file or directory')
    assert not match(command)

    command = Command('cat', 'cat: testdir: No such file or directory')
    assert not match(command)

    command = Command('ls testdir/', 'cat: testdir: Is a directory')
    assert not match(command)


# Generated at 2022-06-14 09:34:17.311540
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('cat main.cpp',
                         'cat: main.cpp: Is a directory',
                         ''))
    assert not match(Command('cat main.cpp', '', ''))

# Generated at 2022-06-14 09:34:24.023470
# Unit test for function match
def test_match():
    assert match(Command('cat /tmp', output='cat: /tmp: Is a directory'))
    assert not match(Command('cat /tmp'))
    assert not match(Command('cat /tmp', output='cat: /tmp: No such file or directory'))
    assert not match(Command('echo', output='cat: /tmp: Is a directory'))



# Generated at 2022-06-14 09:34:35.653854
# Unit test for function match
def test_match():
    output_0 = "cat: test/: Is a directory\n"
    output_1 = "Invalid directory\n"
    output_2 = "cat: /test/: Is a directory\n"
    output_3 = "cat: /test.txt/: Is a directory\n"

    assert match(Command(script='cat /test/', output=output_0))
    assert not match(Command(script='cat /test/', output=output_1))
    assert match(Command(script='cat /test/ /test/', output=output_2))
    assert not match(Command(script='cat /test/ /test/', output=output_3))


# Generated at 2022-06-14 09:34:40.348807
# Unit test for function match
def test_match():
	assert match(Command("cat ~/Downloads", "cat: Downloads: Is a directory"))
	assert not match(Command("cat dir/output.txt", "cat: output.txt: No such file or directory"))
	assert not match(Command("cat output.txt", "output"))

# Generated at 2022-06-14 09:34:43.213872
# Unit test for function match
def test_match():
    command = Command('cat /home/y', 'cat: /home/y: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:34:50.586461
# Unit test for function match
def test_match():
    # Unit test for cat which outputs error
    output_cat = 'cat: file: Is a directory\n'

    # Unit test for ls which outputs file content
    output_ls = 'ls: file: Is a directory\n'

    assert match(Command('cat file', output=output_cat))
    assert not match(Command('cat file', output=output_ls))
    assert not match(Command('ls file', output=output_cat))


# Generated at 2022-06-14 09:35:16.026561
# Unit test for function match
def test_match():
    # Format: Optional[Regex], Optional[String], Optional[Function]
    command = 'cat code/search_engine/search/utils.py'
    output = 'cat: code/search_engine/search/utils.py: Is a directory'
    assert_match(match, command, output)


# Generated at 2022-06-14 09:35:16.943404
# Unit test for function match
def test_match():
    command = Command('cat file.txt',
                      stderr='cat: file.txt: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:35:21.874314
# Unit test for function match
def test_match():
    assert match(Command('cat dummy', 'cat: dummy: Is a directory', ''))
    assert match(Command('cat dummy/', 'cat: dummy/: Is a directory', ''))
    assert not match(Command('cat dummy', '', ''))
    assert not match(Command('cat', 'cat: : No such file or directory', ''))


# Generated at 2022-06-14 09:35:26.604811
# Unit test for function match
def test_match():
    assert match(Command('cat test'))
    assert not match(Command('test test'))
    assert not match(Command('test test', 'cat: test: Is a directory'))
    assert not match(Command('test test', 'cat: test: Is a directory', 'test test'))


# Generated at 2022-06-14 09:35:29.230169
# Unit test for function match
def test_match():
    assert match(Command('cat README.md'))
    assert not match(Command('ls README.md'))


# Generated at 2022-06-14 09:35:34.542403
# Unit test for function match
def test_match():
    command = Command('cat nomefile', 'cat: nomefile: Is a directory')
    assert match(command)

    command = Command('cat file.txt', 'cat: file.txt: No such file or directory')
    assert not match(command)



# Generated at 2022-06-14 09:35:39.481406
# Unit test for function match
def test_match():
    command = "cat /etc/passwd"
    os.makedirs('/etc')
    assert match(Command(command, output='cat: /etc/passwd: Is a directory', script_parts=['cat', '/etc/passwd']))


# Generated at 2022-06-14 09:35:42.345474
# Unit test for function match
def test_match():
    match1 = 'cat file.txt'
    match2 = 'cat dir'

    assert not match(match1)
    assert match(match2)


# Generated at 2022-06-14 09:35:51.151861
# Unit test for function match
def test_match():
    assert match(command=Command('cat /usr/local/lib/libbash.so',
                                 'cat: /usr/local/lib/libbash.so: Is a directory'))

    assert not match(command=Command('cat /usr/local/lib/libbash.so',
                                     'cat: /usr/local/lib/libbash.so: No such file or directory'))

    assert not match(command=Command('cat /usr/local/lib/libbash.so',
                                     'cat: /usr/local/lib/libbash.so: command not found'))



# Generated at 2022-06-14 09:35:55.596918
# Unit test for function match
def test_match():
    assert match(Command("cat test", "cat: test: Is a directory"))
    assert not match(Command("cat test", ""))
    assert not match(Command("cat test", "cat: test:"))


# Generated at 2022-06-14 09:36:42.091128
# Unit test for function match
def test_match():
    # Test 1
    command = Command(script = 'cat test', stdout = 'cat: test: Is a directory')
    assert match(command) == True

    # Test 2
    command = Command(script = 'cat test', stdout = 'wtf')
    assert match(command) == False

    # Test 3
    command = Command(script = 'cat', stdout = 'wtf')
    assert match(command) == False


# Generated at 2022-06-14 09:36:47.636649
# Unit test for function match
def test_match():
    assert match(Command(script = 'cat',
                         output = 'cat: blah: Is a directory'))
    assert not match(Command(script = 'cat',
                             output = 'cat: blah: No such file or directory'))
    assert not match(Command(script = 'cat', output = 'cat: blah: No'))

# Generated at 2022-06-14 09:36:53.868829
# Unit test for function match
def test_match():
    # A directory specified
    assert match(Command('cat ~/test', 'cat: ~/test: Is a directory'))
    # A directory is not specified
    assert not match(Command('cat ~/test.txt', 'cat: ~/test.txt: Is a directory'))
    # A file specified
    assert not match(Command('cat a', 'cat: a: Is a directory'))


# Generated at 2022-06-14 09:36:58.190715
# Unit test for function match
def test_match():
    command = Command('cat testing/samples/', 'cat: testing/samples/: Is a directory')
    assert match(command)
    command = Command('some other command', 'cat: testing/samples/: Is a directory')
    assert not match(command)



# Generated at 2022-06-14 09:37:01.051698
# Unit test for function match
def test_match():
    assert match(Command('cat', '', 'cat: foo: Is a directory'))
    assert not match(Command('cat', '', ''))

# Generated at 2022-06-14 09:37:07.659014
# Unit test for function match
def test_match():
    output = """cat: /home/mohsen: Is a directory
    """
    assert match(Command('cat /home/mohsen', output=output, script_parts=['cat', '/home/mohsen']))
    assert not match(Command('ls /home/mohsen', output=output, script_parts=['ls', '/home/mohsen']))

# Generated at 2022-06-14 09:37:14.433289
# Unit test for function match
def test_match():
    assert match(Command('cat etc/fstab'))
    assert not match(Command('cat /etc/fstab'))
    assert not match(Command('echo etc/fstab | cat'))
    assert not match(Command('cat etc/*/fstab'))
    assert not match(Command('cat etc/fstab && echo success'))
    assert not match(Command('cat etc/fstab || echo failure'))
    assert not match(Command('cat etc/fstab | wc -l'))
    assert not match(Command('cat etc/fstab | less'))
    assert not match(Command('wc -l etc/fstab'))
    assert not match(Command('ls -l'))
    assert not match(Command('wc -l'))
    assert not match(Command('ls'))

# Generated at 2022-06-14 09:37:19.687535
# Unit test for function match
def test_match():
    command = Command('cat testFolder',
                      'cat: testFolder: Is a directory',
                      0)
    assert match(command)



# Generated at 2022-06-14 09:37:26.823837
# Unit test for function match
def test_match():
    command = Command('cat abc', '', None)
    assert match(command)
    command = Command('cat abc cde', '', None)
    assert not match(command)
    command = Command('cat abc cde', 'abc is not a valid path', None)
    assert not match(command)


# Generated at 2022-06-14 09:37:29.729538
# Unit test for function match
def test_match():
    assert match(Command('cat /etc',
    output='cat: /etc: Is a directory'))
    assert not match(Command('cat /etc/passwd',
    output='root:x:0:0:root:\/root:\/bin\/bash\ndebian:x:1000:1000:Kevin:'))

# Generated at 2022-06-14 09:38:56.126672
# Unit test for function match
def test_match():
    assert match(Command('cat mydir', 'cat: mydir: Is a directory'))
    assert not match(Command('cat myfile', 'hello world'))


# Generated at 2022-06-14 09:39:01.357139
# Unit test for function match
def test_match():
    assert match(Command('cat test', '')) is False
    assert match(Command('cat test', 'cat: test: Is a directory')) is True
    assert match(Command('cat test test2', 'cat: test: Is a directory')) is False



# Generated at 2022-06-14 09:39:06.142899
# Unit test for function match
def test_match():
    command = Command('cat hello.txt', 'cat: hello.txt: Is a directory')
    assert match(command)

    command = Command('cat hello.txt', 'cat: hello.txt: No such file or directory')
    assert not match(command)


# Generated at 2022-06-14 09:39:11.090333
# Unit test for function match
def test_match():
    assert match(Command("cat /home", ""))
    assert not match(Command("cat file.txt", ""))
    assert not match(Command("echo \"cat: /home: Is a directory\"", ""))



# Generated at 2022-06-14 09:39:15.059623
# Unit test for function match
def test_match():
    command = Command("cat test/testfile.txt", "cat: test/testfile.txt: Is a directory",
                      [], None)
    assert match(command)


# Generated at 2022-06-14 09:39:19.347632
# Unit test for function match
def test_match():
    command = Command('cat /home/test/')
    result = match(command)
    assert result
    command = Command('cat /home/test')
    result = match(command)
    assert not result


# Generated at 2022-06-14 09:39:28.645793
# Unit test for function match
def test_match():
  assert match(Command('cat', 'Hello')) == False
  assert match(Command('cat', 'cat')) == True
  assert match(Command('cat', 'Hello', 'Hello')) == True
  assert match(Command('cat', 'Hello', 'Hello', 'Hello')) == True
  assert match(Command('cat', 'Hello', 'Hello', 'Hello', 'Hello')) == True
  assert match(Command('cat', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello')) == True
  assert match(Command('cat', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello')) == True
  assert match(Command('cat', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello')) == True

# Generated at 2022-06-14 09:39:35.864464
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt', 'cat: test.txt: Is a directory\n'))
    assert not match(Command('cat test.txt', 'cat: test.txt: No such file'
                             ' or directory\n'))
    assert not match(Command('cat test.txt', 'test.txt\n'))
    assert not match(Command('cat test.txt', 'test.txt'))



# Generated at 2022-06-14 09:39:37.982295
# Unit test for function match
def test_match():
    command = 'cat dir'
    actual = match(Command(script=command))
    assert actual == True


# Generated at 2022-06-14 09:39:41.771680
# Unit test for function match
def test_match():
    assert match(Command('cat file.txt'))
    assert match(Command('cat directory/'))
    assert not match(Command('cat file.txt', stderr='some other err'))
    assert not match(Command('cat file.txt', stderr='cat: some other err'))
