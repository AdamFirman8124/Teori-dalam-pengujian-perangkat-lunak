

# Generated at 2022-06-14 09:29:52.671813
# Unit test for function match
def test_match():
    assert match(Command('cat asdf/', ''))
    assert not match(Command('cat asdf', ''))
    assert not match(Command('cat -a asdf/', ''))
    assert not match(Command('ls asdf/', ''))

# Generated at 2022-06-14 09:29:56.022922
# Unit test for function match
def test_match():
    command = Command(script = "cat /home/")
    assert not match(command)
    command = Command(script = "cat /home/abc")
    assert match(command)


# Generated at 2022-06-14 09:30:01.600127
# Unit test for function match
def test_match():
    command="cat jkl"
    assert match(Command(script='cat jkl',output='cat: jkl: Is a directory',))
    command="cat jkl2"
    if os.path.isdir(command.script_parts[1]):
        assert True
    else:
        assert False

# Generated at 2022-06-14 09:30:08.911520
# Unit test for function match
def test_match():
    assert match(Command('cat README.md', 'cat: README.md: Is a directory', ''))
    assert match(Command('cat README.md', 'cat: README.md: No such file or directory', ''))
    assert not match(Command('cat README.md', 'xxx', '', ''))
    assert not match(Command('cat README.md', 'cat: README.md: Is a directory', '', '', 2))


# Generated at 2022-06-14 09:30:11.009986
# Unit test for function match
def test_match():
    assert match(Command('cat dir', 'cat: dir: Is a directory'))
    assert not match(Command('cat file', ''))

# Generated at 2022-06-14 09:30:19.684551
# Unit test for function match
def test_match():
    # Unit tests for function match
    command = Command('cat /home/vagrant', '')
    assert match(command)
    command = Command('', '')
    assert not match(command)
    command = Command('cat /home/vagrant', 'cat: /home/vagrant: Is a directory')
    assert match(command)
    command = Command('cat /home/vagrant', 'cat: /home/vagrant: No such file or directory')
    assert not match(command)
    command = Command('cat /home/vagrant', 'cat: /home/vagrant: Permission denied')
    assert not match(command)

# Generated at 2022-06-14 09:30:24.070726
# Unit test for function match
def test_match():
    command = Command('cat .vim')
    assert match(command)
    command = Command('cat /tmp/')
    assert match(command)
    command = Command('cp /tmp/')
    assert not match(command)


# Generated at 2022-06-14 09:30:27.160099
# Unit test for function match
def test_match():
    assert match(Command('cat f'))
    assert not match(Command('cat'))
    assert not match(Command('cat test/'))


# Generated at 2022-06-14 09:30:32.035894
# Unit test for function match
def test_match():
    assert match(Command('cat /tmp/'))
    assert match(Command('cat /tmp/', 'Some Error Text'))
    assert not match(Command('cat /tmp/', ''))
    assert not match(Command('some-random-cmd', 'cat'))


# Generated at 2022-06-14 09:30:35.587789
# Unit test for function match
def test_match():
    assert match(Command('cat foo', '', 'cat: foo: Is a directory', 1))
    assert not match(Command('cat foo', '', 'cat: foo: No such file', 1))


# Generated at 2022-06-14 09:30:40.625155
# Unit test for function match
def test_match():
    command = Command("cat /bin/ls", "cat: /bin/ls: Is a directory", success=False)
    assert match(command)



# Generated at 2022-06-14 09:30:47.619217
# Unit test for function match
def test_match():
    assert not match(Command(script='echo helloworld', output='helloworld'))
    assert not match(Command(script='', output='cat: '))
    assert match(Command(script='cat ~/.bashrc', output='cat: ~/.bashrc: Is a directory'))
    assert not match(Command(script='cat ~/.bashrc', output='cat: ~/.bashrc: Is not a directory'))


# Generated at 2022-06-14 09:30:53.153995
# Unit test for function match
def test_match():
    assert match(Command('cat file.txt', 'cat: file.txt: Is a directory',
                         '', 1))
    assert not match(Command('cat file.txt', 'file.txt', '', 1))



# Generated at 2022-06-14 09:31:02.405871
# Unit test for function match
def test_match():
    assert match(Command('cat chitin.c',
             'cat: chitin.c: Is a directory',
             '/usr/local/bin/little-bobby-tables',
             'ls chitin.c'))
    assert not match(Command('cat chitin.c',
             'chitin.c: Is a directory',
             '/usr/local/bin/little-bobby-tables',
             'ls chitin.c'))
    assert not match(Command('cat chitin.c',
             'cat: chitin.c: Is a directory',
             '/usr/local/bin/little-bobby-tables',
             'ls chitin.c'))

# Generated at 2022-06-14 09:31:05.968120
# Unit test for function match
def test_match():
    assert match(Command("cat config", "cat: config: Is a directory"
    )) == True
    assert match(Command("cat adb.ini", "cat: adb.ini: No such file or directory")
    ) == False

# Generated at 2022-06-14 09:31:10.782660
# Unit test for function match
def test_match():
    command = "cat abc.txt"
    assert(match(command) == False)
    command = "cat /folder"
    assert(match(command) == True)



# Generated at 2022-06-14 09:31:12.611175
# Unit test for function match
def test_match():
    command = Command('cat /')
    assert match(command) is True


# Generated at 2022-06-14 09:31:17.422477
# Unit test for function match
def test_match():
    assert match(Command('cat file1.txt', 'cat: file1.txt: Is a directory', '', '', 'ls file1.txt', ''))
    assert not match(Command('cat file1.txt', '', '', '', 'ls file1.txt', ''))
    assert not match(Command('cat file1.txt', '', '', '', 'cat file1.txt', ''))
    assert not match(Command('cat file1.txt file2.txt', '', '', '', 'cat file1.txt file2.txt', ''))


# Generated at 2022-06-14 09:31:19.980419
# Unit test for function match
def test_match():
    command.script = "cat test.txt"
    command.output = "cat: test.txt: Is a directory"
    assert match(command) == True

# Generated at 2022-06-14 09:31:22.654037
# Unit test for function match
def test_match():
    command = Command('cat /path/to/dir')
    assert match(command) is True


# Generated at 2022-06-14 09:31:33.685027
# Unit test for function match
def test_match():
    assert match(Command("cat /usr/local/bin", output='cat: /usr/local/bin: Is a directory'))
    assert match(Command("cat /usr/local/bin", output='cat: /usr/local/bin: Is a directory\n'))
    assert not match(Command("cat: /usr/local/bin", output='Is a directory'))
    assert not match(Command("cat /usr/local/bin", output='Is a directory'))
    assert not match(Command("cat /usr/local/bin", output='cat: /usr/local/bin: No such file or directory'))
    assert not match(Command("cat /usr/local/bin", output='cat: /usr/local/bin: No such file or directory\n'))

# Generated at 2022-06-14 09:31:38.342913
# Unit test for function match
def test_match():
    assert match(
        Command('cat /home/ubuntu/Desktop', ''),
        None)
    assert not match(
        Command('cat /home/ubuntu/Desktop/fake', ''),
        None)
    assert not match(
        Command('ls /home/ubuntu/Desktop', ''),
        None)


# Generated at 2022-06-14 09:31:40.656809
# Unit test for function match
def test_match():
    assert match(Command(script='cat ./hello',
                         output='cat: ./hello: Is a directory'))

# Generated at 2022-06-14 09:31:43.938583
# Unit test for function match
def test_match():
    command = Command("cat my_dir")
    assert match(command)
    command = Command("cat my_dir/file.txt")
    assert not match(command)


# Generated at 2022-06-14 09:31:50.355936
# Unit test for function match
def test_match():
    assert match(Command('cat folder', 'cat: folder: Is a directory'))
    assert match(Command('cat   folder', 'cat: folder: Is a directory'))
    assert not match(Command('cat folder', 'cat: folder: No such file or directory'))



# Generated at 2022-06-14 09:31:56.854082
# Unit test for function match
def test_match():
    from thefuck.types import Command
	# Test 1 : valid command
    assert match(Command('cat file1 file2', '')) == False
	# Test 2 : invalid command
    assert match(Command('cat file1 file2', 'cat: file1: Is a directory')) == True


# Generated at 2022-06-14 09:31:59.572186
# Unit test for function match
def test_match():
    assert match(Command('cat', '', ''))
    assert match(Command('cat', '', '', output='cat: '))
    assert not match(Command('cat', '', '', output=''))


# Generated at 2022-06-14 09:32:04.998150
# Unit test for function match
def test_match():
    assert match(Command('cat ~/file.txt', 'cat: ~/file.txt: Is a directory'))
    assert not match(Command('cat ~/file.txt', ''))
    assert not match(Command('cat ~/file.txt', 'cat: ~/file.txt: Is a file'))
    assert not match(Command('cat file.txt', 'cat: file.txt: Is a directory'))


# Generated at 2022-06-14 09:32:07.359577
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('cat foo', 'cat: foo: Is a directory'))
    assert not match(Command('cat foo', 'foo'))


# Generated at 2022-06-14 09:32:10.440662
# Unit test for function match
def test_match():
    assert match(Command('cat /usr/bin', ''))
    assert not match(Command('cat /etc/ssh/ssh_config', '/usr/bin/cat: /etc/ssh/ssh_config: Is a directory'))
    assert not match(Command('cat /etc/ssh/ssh_config', ''))


# Generated at 2022-06-14 09:32:18.224802
# Unit test for function match
def test_match():
    assert match(Command('cat main.cpp', 'cat: main.cpp: Is a directory',
                         '', ''))
    assert not match(Command('cat', '', '', ''))
    assert not match(Command('ls', '', '', ''))
    assert not match(Command('cat main.cpp', '', '', ''))


# Generated at 2022-06-14 09:32:20.394884
# Unit test for function match
def test_match():
    command=Command('cat ~/Documents')
    assert match(command)


# Generated at 2022-06-14 09:32:24.834900
# Unit test for function match
def test_match():
    command = Command('cat test', 'cat: test: Is a directory', '', '', None)
    assert match(command)
    command = Command('cat test', 'cat: test: No such file or directory', '', '', None)
    assert not match(command)


# Generated at 2022-06-14 09:32:30.447075
# Unit test for function match
def test_match():
    # Test if 'cat: <filename is a directory>' starts with 'cat: '
    string = "cat: /test: Is a directory"
    assert match(Command(script=string))



# Generated at 2022-06-14 09:32:36.358070
# Unit test for function match
def test_match():
    from thefuck.types import Command
    from thefuck.rules.cat_is_a_directory import match

    assert match(Command('cat', '', ''))
    assert match(Command('cat', '', '', ''))
    assert not match(Command('ls', '', ''))
    assert not match(Command('echo', '', ''))
    assert not match(Command('cat', 'hello.txt', ''))
    assert not match(Command('cat', 'hello.txt', '', ''))


# Generated at 2022-06-14 09:32:39.300456
# Unit test for function match
def test_match():
    command = Command('cat /tmp/file', 'cat: /tmp/file: Is a directory')
    assert match(command)


# Generated at 2022-06-14 09:32:45.266284
# Unit test for function match
def test_match():
    assert match(Command('cat /not/exists', 'cat: /not/exists: No such file or directory'))
    assert not match(Command('cat /etc/passwd', 'root:x:0:0:root:/root:/bin/bash'))
    assert not match(Command('cat /not/exists', 'cat: /not/exists: Is a directory'))



# Generated at 2022-06-14 09:33:00.693654
# Unit test for function match
def test_match():
    assert match(Command('cat file', ''))
    assert match(Command('cat file', '', stderr='cat: file: Is a directory'))
    assert match(Command('cat file', '', stderr='cat: file: Is a Directory'))
    assert match(Command('cat file', '', stderr='cat: file: is a directory'))
    assert match(Command('cat file', '', stderr='cat: file: is a Directory'))
    assert not match(Command('cat file', '', stderr='cat: file: No such file or directory'))
    assert not match(Command('cat file', '', stderr='cat: file: No such File or directory'))
    assert not match(Command('cat file', '', stderr='cat: file: No such file or Directory'))

# Generated at 2022-06-14 09:33:03.628393
# Unit test for function match
def test_match():
    assert match(Command('cat /path/dir', 'cat: /path/dir: Is a directory'))
    assert not match(Command('cat /path/file', 'cat: /path/file: No such file or directory'))


# Generated at 2022-06-14 09:33:05.738704
# Unit test for function match
def test_match():
    run('''cat /etc''')
    command = Command('cat /etc', 'cat: /etc: Is a directory', '')
    assert match(command)


# Generated at 2022-06-14 09:33:11.525857
# Unit test for function match
def test_match():
    assert match(Command('cat /tmp'))
    assert not match(Command('cats /tmp'))
    assert not match(Command('cat /tmp/bashrc'))


# Generated at 2022-06-14 09:33:16.594267
# Unit test for function match
def test_match():
    command1 = Command('cat /etc/passwd', '')
    assert(not match(command1))

    pass_file = '/etc/passwd'
    command2 = Command('cat ' + pass_file, '')
    assert(match(command2))


# Generated at 2022-06-14 09:33:28.354805
# Unit test for function match
def test_match():

    # case 1: directory exists and output of cat starts with cat:
    command1 = MagicMock(script='cat /tmp', output='cat: /tmp: Is a directory')
    command1.script_parts = command1.script.split()

    # case 2: directory exists but output of cat doesn't start with cat:
    command2 = MagicMock(script='cat /tmp', output='/tmp: Is a directory')
    command2.script_parts = command2.script.split()

    # case 3: directory doesn't exist
    command3 = MagicMock(script='cat /abc', output='cat: /abc: No such file or directory')
    command3.script_parts = command3.script.split()

    assert match(command1)
    assert not match(command2)
    assert not match(command3)



# Generated at 2022-06-14 09:33:35.303111
# Unit test for function match
def test_match():
    assert match(Command('cat', 'cat: This_is_a_Directory'))
    assert match(Command('cat', 'cat: This is a Directory'))
    assert match(Command('cat', 'cat: This is a file')) is False
    assert match(Command('cat', 'This is a Directory')) is False
    assert match(Command('ls', 'ls: This_is_a_Directory')) is False


# Generated at 2022-06-14 09:33:37.181608
# Unit test for function match
def test_match():
	assert match(Command('cat /etc/hosts', 'cat: /etc/hosts: Is a directory'))
	assert not match(Command('cat /etc/hosts', None))


# Generated at 2022-06-14 09:33:39.640146
# Unit test for function match
def test_match():
    assert match(Command('cat asdf', 'cat: asdf: Is a directory'))
    assert not match(Command('cat asdf', 'asdf'))


# Generated at 2022-06-14 09:33:43.948660
# Unit test for function match
def test_match():
    assert match(Command('cat temp', 'cat: temp: Is a directory'))
    assert not match(Command('cat temp', ''))
    assert not match(Command('ls temp', 'cat: temp: Is a directory'))


# Generated at 2022-06-14 09:33:45.795982
# Unit test for function match
def test_match():
    command = Command('cat test', 'cat: test: Is a directory')
    assert match(command)



# Generated at 2022-06-14 09:33:49.592511
# Unit test for function match
def test_match():
    command = Command(script='cat README.md',
                      stderr='cat: README.md: Is a directory\n',
                      output='cat: README.md: Is a directory\n',
                      env={'PWD': '/home/user/thefuck'},
                      stdout='')
    assert match(command)

# Generated at 2022-06-14 09:34:01.525800
# Unit test for function match
def test_match():
    c = Command('cat test')

    # no exception for non-existing file
    assert not match(c)
        
    with open(c.script_parts[1], 'w') as f:
        f.write('')

    # no exception for existing file
    assert not match(c)

    os.mkdir(c.script_parts[1])

    # exception for existing directory
    assert match(c)

    os.unlink(c.script_parts[1])
    os.rmdir(c.script_parts[1])



# Generated at 2022-06-14 09:34:10.871775
# Unit test for function match
def test_match():
	command = 'cat test.py'
	assert match(command) is not None
	new_command = get_new_command(command)
	assert new_command == 'ls test.py'

# Generated at 2022-06-14 09:34:17.251693
# Unit test for function match
def test_match():
    assert match(Command('cat stuff', 'cat: stuff: Is a directory', ''))
    assert not match(Command('cat stuff', 'cat: stuff: No such file or directory', ''))
    assert not match(Command('cat', 'cat: stuff: No such file or directory', ''))
    assert not match(Command('cat stuff', 'stuff', ''))


# Generated at 2022-06-14 09:34:19.423479
# Unit test for function match
def test_match():
    result = match(Command('cat ./tests', '', 'cat: ./tests: Is a directory'))

    assert result


# Generated at 2022-06-14 09:34:20.226387
# Unit test for function match
def test_match():
    asse

# Generated at 2022-06-14 09:34:22.109556
# Unit test for function match
def test_match():
    assert match(Command('cat rainbow.sh', 'cat: rainbow.sh: Is a directory'))    
    

# Generated at 2022-06-14 09:34:26.223427
# Unit test for function match
def test_match():
    assert match(Command('cat', 'cat: test.txt: Is a directory', ''))
    assert not match(Command('cat', 'cat: test.txt: Is not a directory', ''))
    assert not match(Command('cat', '', ''))
     

# Generated at 2022-06-14 09:34:28.532297
# Unit test for function match
def test_match():
    command = Command('cat /home/ubuntu', '', '')
    assert match(command)


# Generated at 2022-06-14 09:34:36.076953
# Unit test for function match
def test_match():
    assert match(Command(script='cat /usr/bin/', 
                         stderr='cat: /usr/bin/: Is a directory'))
    assert not match(Command(script='cat /usr/bin/',
                             stderr='cat: /usr/bin/: Permission denied'))
    assert not match(Command(script='cat', 
                             stderr='cat: invalid option -- c'))
    assert not match(Command(script='cat'))


# Generated at 2022-06-14 09:34:41.157292
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory'))
    assert not match(Command('cat test', ''))
    assert not match(Command('ls test', 'cat: test: Is a directory'))
    assert not match(Command('cat', 'cat: : Is a directory'))


# Generated at 2022-06-14 09:34:47.183948
# Unit test for function match
def test_match():
	assert match(command=Command(script='cat testdata/', output='cat: testdata/: Is a directory')) == True
	assert match(command=Command(script='cat file1 file2', output='cat: file1: No such file or directory\ncat: file2: No such file or directory')) == False


# Generated at 2022-06-14 09:35:04.368315
# Unit test for function match
def test_match():
    assert match(Command('cat abc', 'cat: abc is a directory'))
    assert match(Command('cat', '')) == False
    assert match(Command('cat', 'cat: fopen: yes: No such file or directory')) == False


# Generated at 2022-06-14 09:35:06.108933
# Unit test for function match
def test_match():
    assert match("cat foo bar")
    assert not match("ls foo bar")

# Generated at 2022-06-14 09:35:09.213259
# Unit test for function match
def test_match():
    assert match(Command('cat /home/nagendra/hello.sh',
                         output='cat: /home/nagendra/hello.sh: Is a directory'))



# Generated at 2022-06-14 09:35:13.845465
# Unit test for function match
def test_match():
    assert match(Command('cat test', ''))
    assert not match(Command('ls test', ''))
    assert not match(Command('cat foo/bar/baz.txt', ''))

# Generated at 2022-06-14 09:35:15.791705
# Unit test for function match
def test_match():
    assert match(Command('cat /homr'))


# Generated at 2022-06-14 09:35:21.283160
# Unit test for function match
def test_match():
    assert match(Command(script="cat dos", stderr=b'cat: dos: Is a directory', output=b''))
    assert match(Command(script="cat ~/dos", stderr=b'cat: dos: Is a directory', output=b''))

# Generated at 2022-06-14 09:35:23.757320
# Unit test for function match
def test_match():
    assert match(Command('cat /home', '/home is a directory'))
    assert not match(Command('cat /home', 'foo'))

# Generated at 2022-06-14 09:35:26.184373
# Unit test for function match
def test_match():
    a = "cat: /Users/Phumrapee/Documents/dsa: Is a directory"
    assert match(Command(a, "cat ")) == True

# Generated at 2022-06-14 09:35:37.789202
# Unit test for function match
def test_match():
	assert(match(Command('cat test.txt', 'cat: test.txt: Is a directory\n')))
	assert(match(Command('cat test.txt', 'cat: test.txt: No such file or directory\n')) == False)
	assert(match(Command('cat test.txt cat.py', 'cat: test.txt: Is a directory\n')) == False)
	assert(match(Command('cat test.txt cat.py', 'cat: test.txt: Is a directory\ncat: cat.py: No such file or directory\n')) == False)

# Generated at 2022-06-14 09:35:42.506923
# Unit test for function match
def test_match():
    assert match(Command('cat /home/user/downloads', '/home/user/downloads'))
    assert not match(Command('ls /home/user/downloads', '/home/user/downloads'))
    assert not match(Command('cat foo.txt', 'foo.txt'))


# Generated at 2022-06-14 09:35:57.414374
# Unit test for function match
def test_match():
    assert match(Command('cat `echo a`', 'cat: a: Is a directory\n', ''))
    


# Generated at 2022-06-14 09:36:03.660555
# Unit test for function match
def test_match():
    assert match(Command("cat .local/share/Trash/info",
                              "cat: .local/share/Trash/info: Is a directory\n"))
    assert not match(Command("cat .local/share/Trash/info/file.txt",
                              "cat: .local/share/Trash/info/file.txt: No such file or directory\n"))


# Generated at 2022-06-14 09:36:07.344655
# Unit test for function match
def test_match():
    command = 'cat test'
    os.mkdir('test')
    assert match(Command(command, command.split(), '', 0)) is True
    os.rmdir('test')


# Generated at 2022-06-14 09:36:10.537760
# Unit test for function match
def test_match():
    assert match(Command('cat test', stderr='cat: test: Is a directory'))
    assert not match(Command('cat test', stderr='cat: test: No such file or directory'))


# Generated at 2022-06-14 09:36:13.375788
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory'))
    assert not match(Command('cat test', ''))


# Generated at 2022-06-14 09:36:15.724642
# Unit test for function match
def test_match():
    assert match(Command(script="cat /usr/share/dict/words"))


# Generated at 2022-06-14 09:36:17.860771
# Unit test for function match
def test_match():
    assert match(Command('cat ddd', output='cat: ddd: Is a directory\n'))


# Generated at 2022-06-14 09:36:19.760317
# Unit test for function match
def test_match():
    command = 'cat'
    assert match(command)


# Generated at 2022-06-14 09:36:26.569615
# Unit test for function match
def test_match():
    assert match(Command('cat --version', stderr='cat: illegal option -- -\n'))
    assert match(Command('cat test.py', stderr='cat: test.py: Is a directory\n'))
    assert not match(Command('cat -n test.py', stderr='cat: illegal option -- n\n'))
    assert not match(Command('cat test.py', stderr='cat: test.py: No such file or directory\n'))


# Generated at 2022-06-14 09:36:28.407172
# Unit test for function match
def test_match():
    assert match(Command("cat directory", "cat: directory: Is a directory"))

# Generated at 2022-06-14 09:36:45.539929
# Unit test for function match
def test_match():
    # Create a mock object of class Command
    command = type('Command', (object,), {'output': 'cat: /home/user: Is a directory', 'script_parts': ['cat','/home/user']})
    
    # Check if the error is detected
    assert match(command) == True
    # Create another Command object
    command = type('Command', (object,), {'output': 'cat: /home/user/file.txt: No such file or directory', 'script_parts': ['cat','/home/user/file.txt']})
    
    # Check if the error is not detected
    assert match(command) == False



# Generated at 2022-06-14 09:36:54.251410
# Unit test for function match
def test_match():
    assert (match(Command(script='cat',
                         output='cat: foobar: Is a directory\n',
                         stderr='cat: foobar: Is a directory\n',
                         env={},
                         stderr_raw=b'cat: foobar: Is a directory\n',
                         stdout_raw=b'cat: foobar: Is a directory\n',
                         script_parts=['cat', 'foobar']))
            == True)
    assert (match(Command('cat')) == False)


# Generated at 2022-06-14 09:36:59.138043
# Unit test for function match
def test_match():
    assert match(Command('cat hello.py', 'cat: hello.py: Is a directory'))
    assert not match(Command('cat hello.py', 'hello.py: Is a directory'))
    assert not match(Command('not cat hello.py', 'hello.py: Is a directory'))

# Generated at 2022-06-14 09:37:01.341723
# Unit test for function match
def test_match():
    assert match(Command('cat foo', 'cat: foo: Is a directory', ''))



# Generated at 2022-06-14 09:37:06.139541
# Unit test for function match
def test_match():
    command = get_command('cat test')
    assert match(command)
    command = get_command('cat non_existent_dir')
    assert not match(command)
    command = get_command('ls test')
    assert not match(command)

# Generated at 2022-06-14 09:37:09.109566
# Unit test for function match
def test_match():
    assert match(Command('cat some/dir/', ''))
    assert match(Command('cat some/dir/', '', ''))
    assert not match(Command('cat file', ''))

# Generated at 2022-06-14 09:37:24.986413
# Unit test for function match
def test_match():
    command = Command('cat /tmp/test')
    assert match(command)
    command = Command('cat /tmp/test/')
    assert match(command)
    command = Command('cp /tmp/test')
    assert not match(command)
    command = Command('cat /tmp/test', 'cat: /tmp/test: Is a directory')
    assert match(command)
    command = Command('cat /tmp/test', 'cat: /tmp/test: No such file or directory')
    assert not match(command)
    command = Command('cat /tmp/source', 'cat: /tmp/source: No such file or directory')
    assert not match(command)


# Generated at 2022-06-14 09:37:29.276791
# Unit test for function match
def test_match():
    assert match(Command(script='cat /not/a/file',
                         output='cat: /not/a/file: Is a directory'))
    assert not match(Command(script='cat /not/a/file',
                             output='cat: /not/a/file: No such file or directory'))
    assert not match(Command(script='ls /',
                             output='ls: /: Is a directory'))


# Generated at 2022-06-14 09:37:32.378281
# Unit test for function match
def test_match():
    assert match(Command('cat', '', ''))
    assert not match(Command('ls', '', ''))


# Generated at 2022-06-14 09:37:37.797388
# Unit test for function match
def test_match():
    command_output = "cat: /etc/ld.so.conf: Is a directory"
    assert(match(Command(script="cat /etc/ld.so.conf", output=command_output)))
    assert(not match(Command(script="cat /etc/ld.so.conf.d", output=command_output)))


# Generated at 2022-06-14 09:38:04.096048
# Unit test for function match
def test_match():
    command = Command('cat test', '')
    assert match(command)



# Generated at 2022-06-14 09:38:15.170777
# Unit test for function match
def test_match():
    assert match(Command(script='./cat.sh', output='cat: trash: Is a directory',
                         stderr='cat: trash: Is a directory\n'))
    assert not match(Command(script='./cat.sh', output='cat: trash',
                             stderr='cat: trash\n'))
    assert not match(Command(script='./cat.sh', output='cat: trash: Is a directory',
                             stderr='cat: trash: Is a directory\n'))


# Generated at 2022-06-14 09:38:18.375076
# Unit test for function match
def test_match():
    assert match(Command('cat .', 'cat: .: Is a directory'))
    assert not match(Command('cat /tmp/test.txt', 'test content'))


# Generated at 2022-06-14 09:38:22.838751
# Unit test for function match
def test_match():
    assert not match(Command('ls foo', output='ls: foo: Is a directory'))
    assert match(Command('cat foo', output='cat: foo: Is a directory',
        stderr='cat: foo: Is a directory'))
    assert not match(Command('pygmentize foo', output='cat: foo: Is a directory'))


# Generated at 2022-06-14 09:38:27.214599
# Unit test for function match
def test_match():
    assert for_app("cat", at_least=1)(match)(Command("cat a.txt"))
    assert not for_app("cat", at_least=1)(match)(Command("cat a.txt b.txt"))


# Generated at 2022-06-14 09:38:31.237231
# Unit test for function match
def test_match():
    command_output = "cat: tecmintxx: Is a directory"
    new_cmd = get_new_command(Command(script="cat tecmint", output=command_output))
    assert new_cmd == "ls tecmint"

# Generated at 2022-06-14 09:38:38.191484
# Unit test for function match
def test_match():
    assert match(Command('cat file', ''))
    assert match(Command('cat file1 file2', ''))
    assert match(Command('cat file1 file2', ''))
    assert match(Command('cat file1 file2', ''))
    assert not match(Command('cat file1 file2', '', '/bin/cat'))
    assert not match(Command('ls file', ''))
    assert not match(Command('touch file', ''))


# Generated at 2022-06-14 09:38:43.404525
# Unit test for function match
def test_match():
    command = Command(script='cat /home', output='cat: /home: Is a directory')
    assert match(command)
    command = Command(script='cat /home', output='cat: /home: No such file or directory')
    assert not match(command)


# Generated at 2022-06-14 09:38:46.225134
# Unit test for function match
def test_match():
    command = Command('cat ./temp', 'cat: ./temp: Is a directory', '')
    assert match(command)


# Generated at 2022-06-14 09:38:49.117640
# Unit test for function match
def test_match():
    assert match(Command(script='cat sudo',
                         output='cat: sudo: Is a directory'))
    assert not match(Command(script='cat ~/.bashrc'))

# Generated at 2022-06-14 09:39:43.052013
# Unit test for function match
def test_match():
    assert match(Command('cat foo', '/bin/cat foo', 'foo', 'cat: foo: Is a directory'))


# Generated at 2022-06-14 09:39:50.213279
# Unit test for function match
def test_match():
    # matched
    assert match(Command('cat foo', '/usr/bin/cat foo', '',
                         '/usr/bin/cat: foo: Is a directory'))
    # unmatched
    assert not match(Command('cat foo', '/usr/bin/cat foo', '',
                             'cat: foo: No such file or directory'))
    assert not match(Command('baz', '/usr/bin/baz', '', 'baz: command not found'))  # noqa

