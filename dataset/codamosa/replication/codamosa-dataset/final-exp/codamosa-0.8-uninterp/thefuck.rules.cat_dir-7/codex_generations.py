

# Generated at 2022-06-14 09:29:56.639986
# Unit test for function match
def test_match():
    command = Command('cat test/')
    assert match(command)
    command = Command('cat test')
    assert not match(command)
    command = Command('cat')
    assert not match(command)



# Generated at 2022-06-14 09:29:59.660073
# Unit test for function match
def test_match():
    output = "cat: dir/"
    assert match(Command(script = "cat dir/", output=output)) is True


# Generated at 2022-06-14 09:30:04.207316
# Unit test for function match
def test_match():
    assert match(Command('cat foo', 'cat: foo: Is a directory', 'cat: foo: Is a directory'))
    assert not match(Command('cat foo', 'foo', 'cat: foo: Is a directory'))
    assert not match(Command('cat foo', '', ''))


# Generated at 2022-06-14 09:30:10.805317
# Unit test for function match
def test_match():
    command = Command('cat _cats/')
    assert match(command)

    command = Command('cat dogs/')
    assert not match(command)

    command = Command('cat not_exisitng_file')
    assert not match(command)

    command = Command('ls not_exisitng_file')
    assert not match(command)

    command = Command('echo this is a cat')
    assert not match(command)


# Generated at 2022-06-14 09:30:18.141509
# Unit test for function match
def test_match():
    assert match(Command('cat folder', ''))
    assert not match(Command('cat file', ''))
    assert not match(Command('ls folder', ''))
    assert not match(Command('ls file', ''))



# Generated at 2022-06-14 09:30:21.666269
# Unit test for function match
def test_match():
    command = type('Command', (object,),
                   dict(script='cat aaa',
                        output='cat: aaa: Is a directory'))
    assert match(command)



# Generated at 2022-06-14 09:30:25.741596
# Unit test for function match
def test_match():
    command = 'cat /usr/local/share/thefuck/'
    output = 'cat: /usr/local/share/thefuck/: Is a directory'
    assert match(Command(command, output=output))



# Generated at 2022-06-14 09:30:35.144008
# Unit test for function match
def test_match():
    output = "cat: cow: Is a directory"
    script = "cat cow"
    command = Command(script, output)
    assert match(command)
   
    output = "cat: cow: Is a directory"
    script = "cat help.txt"
    command = Command(script, output)
    assert not match(command)

    output = "cat: cow: Is a directory"
    script = "cat cow"
    command = Command(script, output)
    assert get_new_command(command) == "ls cow"

# Generated at 2022-06-14 09:30:36.999727
# Unit test for function match
def test_match():
    assert match(Command('cat ~/'))


# Generated at 2022-06-14 09:30:47.448295
# Unit test for function match
def test_match():
    assert match(Command(script='cat asdf', stderr='cat: asdf: Is a directory\n',
                         env={'PWD': '/home/user/Documents'}))
    assert not match(Command(script='cat asdf', stderr='cat: asdf: No such file or directory\n',
                             env={'PWD': '/home/user/Documents'}))
    assert not match(Command(script='cat asdf', stderr='cat: asdf: No such file or directory\n',
                             env={'PWD': '/home/user/Documents'}))


# Generated at 2022-06-14 09:30:58.074382
# Unit test for function match
def test_match():
    assert match(Command(script='cat test.txt',
                         stderr='cat: test.txt: Is a directory'))
    assert match(Command(script='cat /home/',
                         stderr='cat: /home/: Is a directory'))
    assert match(Command(script='cat test.txt',
                         stderr='cat: test.txt: No such file or directory'))
    assert not match(Command(script='cat test.txt',
                         stderr='cat: test.txt: No such file or directory'))



# Generated at 2022-06-14 09:31:00.677074
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory'))
    assert not match(Command('cat test', 'cat: test: No such file or directory'))

# Generated at 2022-06-14 09:31:06.571796
# Unit test for function match
def test_match():
    assert match(Command('cat foo bar',
                         output='cat: bar: Is a directory'))
    assert match(Command('cat foo',
                         output='cat: No such file or directory'))
    assert not match(Command('cat foo',
                             output='cat: foo: No such file or directory'))



# Generated at 2022-06-14 09:31:08.513441
# Unit test for function match
def test_match():
    assert match(command='cat /home')


# Generated at 2022-06-14 09:31:13.369444
# Unit test for function match
def test_match():
    assert match(Command('cat zero',
                         stderr='cat: zero: Is a directory',
                         script='cat zero',
                         stdout='',
                         env={}))


# Generated at 2022-06-14 09:31:20.858908
# Unit test for function match
def test_match():
    assert (match(Command('cat test.txt', 'cat: test.txt: Is a directory\n', '')))
    assert (match(Command('cat test.txt', 'cat: test.txt: No such file or directory\n', ''))) == False


# Generated at 2022-06-14 09:31:25.354245
# Unit test for function match
def test_match():
    command = MagicMock(script_parts=['cat', 'is_dir'])
    command.output.startswith.return_value = True
    os.path.isdir.return_value = True
    assert match(command)


# Generated at 2022-06-14 09:31:30.898416
# Unit test for function match
def test_match():
    assert (match(Command(script='cat this_dir/')) == True)
    assert (match(Command(script='echo yo | cat')) == False)
    assert (match(Command(script='cat this_file.txt')) == False)
    assert (match(Command(script='cat this_dir')) == True)



# Generated at 2022-06-14 09:31:38.343780
# Unit test for function match
def test_match():
    # Expected true
    assert match(Command('cat README.md', ''))
    assert match(Command('cat .', ''))

    # Expected false
    assert match(Command('ls README.md', ''))
    assert match(Command('ls README.md > README.md', ''))
    assert match(Command('cat README.md > README.md', ''))



# Generated at 2022-06-14 09:31:42.774844
# Unit test for function match
def test_match():
    assert match(Command(script='cat a b', output='cat: a: Is a directory'))
    assert match(Command(script='cat a b', output='cat: a: No such file or directory')) is False



# Generated at 2022-06-14 09:31:52.061343
# Unit test for function match
def test_match():
    assert match(Command(script='cat abc', output=r'cat: abc: Is a directory'))
    assert not match(Command(script='cat abc', output=r'cat: abc: No such file or directory'))



# Generated at 2022-06-14 09:31:55.594528
# Unit test for function match
def test_match():
    assert match(Command("cat data", "cat: data: Is a directory"))
    assert not match(Command("cat data.txt", "data.txt content"))


# Generated at 2022-06-14 09:31:58.598733
# Unit test for function match
def test_match():
    command = 'cat ../'
    output = 'cat: ../: Is a directory'
    command = Command(command, output)
    assert match(command)

# Generated at 2022-06-14 09:32:01.703627
# Unit test for function match
def test_match():
    output = "cat: mydir: Is a directory\n"
    assert match(Command('cat mydir', output))
    assert not match(Command('cat otherdir', output))

# Generated at 2022-06-14 09:32:05.644540
# Unit test for function match
def test_match():
    assert match(Command('cat test'))
    assert not match(Command('ls test'))
    assert not match(Command('test test'))
    assert not match(Command('test test', '', ''))

# Generated at 2022-06-14 09:32:11.673557
# Unit test for function match
def test_match():
    assert match(
        Command('cat file.txt', 'cat: file.txt: Is a directory', '', ''))
    assert match(
        Command('cat file', 'cat: file: Is a directory', '', ''))
    assert match(
        Command('cat file.txt file2.txt', '', "", ""))



# Generated at 2022-06-14 09:32:14.457486
# Unit test for function match
def test_match():
    assert match(Command('cat /var/log/', '', 'cat: /var/log/: Is a directory'))


# Generated at 2022-06-14 09:32:16.999404
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/apt/', 'cat: /etc/apt/: Is a directory'))



# Generated at 2022-06-14 09:32:18.197048
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/shadow'))



# Generated at 2022-06-14 09:32:20.893126
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/blabla/', '', '', ''))


# Generated at 2022-06-14 09:32:36.357819
# Unit test for function match
def test_match():
    assert match(Command(script='cat /tmp'))
    assert match(Command(script='cat /tmp/blah/blah'))
    assert not match(Command(script='cat /tmp/blah/blah', output='cat: /tmp/blah/blah: Is a directory'))
    assert not match(Command(script='cat /tmp/blah/blah', output='cat: /tmp/blah/blah: Is a file'))

# Generated at 2022-06-14 09:32:41.336348
# Unit test for function match
def test_match():
    command=Command("cat /mnt/c/Users/manoj/Documents/Java", "")
    assert(match(command))

    command = Command("cat /mnt/c/Users/manoj/Documents/Python", "")
    assert(not match(command))



# Generated at 2022-06-14 09:32:50.681135
# Unit test for function match
def test_match():
    assert match(Command('cat /home/codio/workspace/src/fizzbuzz', 'cat: /home/codio/workspace/src/fizzbuzz: Is a directory', ''))
    assert not match(Command('cat /home/codio/workspace/src/fizzbuzz', 'cat: /home/codio/workspace/src/fizzbuzz: No such file or directory', ''))
    assert not match(Command('ls /home/codio/workspace/src/fizzbuzz', 'ls: cannot access /home/codio/workspace/src/fizzbuzz: No such file or directory', ''))

# Generated at 2022-06-14 09:32:58.876772
# Unit test for function match
def test_match():
    assert match(Command('cat /path/', '/path/', 'cat: /path/: Is a directory'))
    assert not match(Command('cat /path/', '/path/', 'cat: /path/: No such file or directory'))

# Generated at 2022-06-14 09:33:02.480004
# Unit test for function match
def test_match():
    assert match(Command(script=u'cat temm.txt', output=u'cat: temm.txt: Is a directory'))
    assert not match(Command(script=u'cat temm.txt', output=u'cat: temm.txt: No such file or directory'))


# Generated at 2022-06-14 09:33:05.277855
# Unit test for function match
def test_match():
    command = Command('cat ~')
    assert not match(command)
    command = Command('cat this_is_a_folder_name')
    assert match(command)
    command = Command('cat .')
    assert match(command)


# Generated at 2022-06-14 09:33:14.506426
# Unit test for function match
def test_match():
    # first argument is command output
    # second argument is command script
    assert match(Command('cat file.txt', 'cat file.txt')) == False
    assert match(Command('cat dir', 'cat file.txt')) == False
    assert match(Command('cat: dir: Is a directory', 'cat dir')) == True
    assert match(Command('cat: file.txt: No such file', 'cat file.txt')) == False
    assert match(Command('cat: dir: Is a directory', 'cat /dir')) == True
    assert match(Command('cat: dir: Is a directory', 'cat /dir/')) == True



# Generated at 2022-06-14 09:33:18.033709
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt test.txt',
                         'cat: test.txt: Is a directory'))
    assert not match(Command('cat test.txt', 'test.txt content'))


# Generated at 2022-06-14 09:33:22.723686
# Unit test for function match
def test_match():
    assert match(Command('cat', 'cat: hom: Is a directory'))
    assert not match(Command('cat', 'cat: hom: Is a directory', stderr='hom: Is a directory\n'))
    assert not match(Command('cat', 'cat: hom: Is a directory', script='cat', stderr='No such file or directory'))

# Generated at 2022-06-14 09:33:27.904052
# Unit test for function match
def test_match():
	os.system("mkdir test_cat_for_dir")
	command = Command("cat test_cat_for_dir", "cat: test_cat_for_dir: Is a directory")
	assert match(command)
	os.system("rm -rf test_cat_for_dir")


# Generated at 2022-06-14 09:33:36.479926
# Unit test for function match
def test_match():
    assert match(Command('cat test.txt'))
    assert match(Command('cat file1 file2 file3'))
    assert not match(Command('cat file1 file2 file3', 'cat: file1: Is a directory'))


# Generated at 2022-06-14 09:33:39.228566
# Unit test for function match
def test_match():
    assert match(Command('cat test_dir'))
    assert not match(Command('ls test_dir'))


# Generated at 2022-06-14 09:33:47.098054
# Unit test for function match
def test_match():
    command = Command('cat /etc', '')
    assert match(command)

    command = Command('cat /etc', "cat: /etc: Is a directory\n")
    assert match(command)

    command = Command('cat /etc', "cat: /etc: No such file or directory\n")
    assert not match(command)

    command = Command('cat /etc', "ls: /etc: No such file or directory\n")
    assert not match(command)


# Generated at 2022-06-14 09:33:49.351358
# Unit test for function match
def test_match():
    assert match(Command('cat dumb', 'cat: dumb: Is a directory'))


# Generated at 2022-06-14 09:33:54.106304
# Unit test for function match

# Generated at 2022-06-14 09:33:59.012977
# Unit test for function match
def test_match():
    assert match(Command('cat file', None, '', 'cat: file: Is a directory'))
    assert not match(Command('cat file', None, '', 'file: Is a directory'))



# Generated at 2022-06-14 09:34:04.829194
# Unit test for function match
def test_match():
    assert not match(Command('cat', '', ''))
    assert not match(Command('cat', '', '', ''))
    assert match(Command('cat', '', 'cat: test: Is a directory', ''))
    assert match(Command('cat', 'filename', 'cat: test: Is a directory', ''))

# Generated at 2022-06-14 09:34:09.829784
# Unit test for function match
def test_match():
    assert match(Command('cat foo', '', '[b]cat: foo: Is a directory[/b]'))
    assert match(Command('cat test.txt', '', '[b]cat: foo: Is a directory[/b]'))
    assert not match(Command('cat test.txt', '', 'test'))

# Generated at 2022-06-14 09:34:11.541737
# Unit test for function match
def test_match():
    assert match(Command('cat file', 'file: Is a directory'))
    assert not match(Command('cat file'))



# Generated at 2022-06-14 09:34:13.475549
# Unit test for function match
def test_match():
    assert match(Command('cat test', output='cat: test: Is a directory'))
    assert not match(Command('cat test', output='cat: test: nothing'))

# Generated at 2022-06-14 09:34:32.283450
# Unit test for function match
def test_match():
    assert match(Command('cat path/to/data', 'cat: path/to/data: Is a directory', '/bin/cat'))
    assert not match(Command('rm path/to/data', 'cat: path/to/data: Is a directory', '/bin/cat'))
    assert not match(Command('cat path/to/data', 'No such file or directory', '/bin/cat'))


# Generated at 2022-06-14 09:34:37.362867
# Unit test for function match
def test_match():
    command = Command(script = 'cat sample.txt',
                      output = 'cat: sample.txt: Is a directory')
    command1 = Command(script = 'cat sample.txt',
                      output = 'sample.txt')
    assert match(command)
    assert match(command1) == False


# Generated at 2022-06-14 09:34:44.827059
# Unit test for function match
def test_match():
    assert match(Command('cat app.py', 'cat: app.py: Is a directory', '', ''))
    assert not match(Command('', '', '', ''))
    assert not match(Command('cat', '', '', ''))
    assert not match(Command('cat app.py', '', '', ''))
    assert not match(Command('cat app.py', 'cat: app.py: No such file or directory', '', ''))


# Generated at 2022-06-14 09:34:52.479504
# Unit test for function match
def test_match():
    assert match(Command(script='cat /usr/bin'))
    assert match(Command(script='cat /usr/bin/thefuck'))
    assert not match(Command(script='ls /usr/bin'))
    assert match(Command(script='cat /usr/bin', output='cat: /usr/bin: Is a directory'))
    assert not match(Command(script='cat /usr/bin', output='cat: /usr/bin: No such file or directory'))


# Generated at 2022-06-14 09:34:56.174448
# Unit test for function match
def test_match():
    # Check if command
    assert match('cat /home') is True
    assert match('cat /home2') is False
    assert match('cat') is False


# Generated at 2022-06-14 09:35:00.675719
# Unit test for function match
def test_match():
    assert match(Command('cat /root/file', None, 'cat: /root/file: Is a directory'))
    assert not match(Command('ls /root/file'))
    assert not match(Command('cat /root/file', None, 'cat: /root/file: No such file or directory'))


# Generated at 2022-06-14 09:35:10.512818
# Unit test for function match
def test_match():
    assert match(Command('cat /home/linuxbrew/.linuxbrew/bin',
                         '/home/linuxbrew/.linuxbrew/bin: Is a directory',
                         '/home/linuxbrew/.linuxbrew/bin'))
    assert not match(Command('ls /home/linuxbrew/.linuxbrew/bin',
                             'total 80',
                             '/home/linuxbrew/.linuxbrew/bin'))
    assert not match(Command('cat /home/linuxbrew/.linuxbrew/bin',
                             '/home/linuxbrew/.linuxbrew/bin: Is a directory',
                             '/home/linuxbrew/.linuxbrew/bin'))


# Generated at 2022-06-14 09:35:16.498681
# Unit test for function match
def test_match():
    assert match(Command('cat test'))
    assert match(Command('cat test/hello'))
    assert match(Command('cat test/hello.txt'))
    assert not match(Command('ls test/hello'))
    assert not match(Command('ls test'))
    assert not match(Command('catd test'))


# Generated at 2022-06-14 09:35:21.881254
# Unit test for function match
def test_match():
    command_1 = Command('cat foo', 'cat: foo: Is a directory')
    assert match(command_1)
    command_2 = Command('cat foo', 'cat: no such file or directory: foo')
    assert not match(command_2)
    command_3 = Command('cat foo', '')
    assert not match(command_3)



# Generated at 2022-06-14 09:35:25.841652
# Unit test for function match
def test_match():
    assert match(Command('cat foo', 'foo', 'cat: foo: Is a directory', None))
    assert not match(Command('rm foo', 'rm: cannot remove `foo\': Is a directory', 'rm: cannot remove `foo\': Is a directory', None))

# Generated at 2022-06-14 09:35:53.253847
# Unit test for function match
def test_match():
    output = 'cat: file.txt: Is a directory'
    assert match(Command('cat /home/user/file.txt', output, '', '', '', '', '', ''))
    assert not match(Command('cat /home/user/file.txt', '', '', '', '', '', '', ''))

# Generated at 2022-06-14 09:35:54.983079
# Unit test for function match
def test_match():
    assert match('cat .')
    assert not match('ls .')


# Generated at 2022-06-14 09:36:02.938642
# Unit test for function match
def test_match():
    assert match(Command('cat file.txt',
                         'cat: file.txt: No such file or directory',
                         ''))
    assert not match(Command('cat path/to/file.txt',
                             '',
                             ''))
    assert match(Command('cat path/to/dir/',
                         'cat: path/to/dir/: Is a directory\n',
                         ''))
    assert not match(Command('cat path/to/dir/',
                         '',
                         ''))


# Generated at 2022-06-14 09:36:04.979829
# Unit test for function match
def test_match():
    assert match(Command('cat /etc'))
    assert not match(Command('ls /etc'))


# Generated at 2022-06-14 09:36:08.955949
# Unit test for function match
def test_match():
    command = Command('cat folder', '', 'cat: folder: Is a directory')
    assert match(command)
    command = Command('cat folder', '', 'cat: folder: No such file or directory')
    assert not match(command)



# Generated at 2022-06-14 09:36:12.415572
# Unit test for function match
def test_match():
    assert match(Command('cat d', 'cat: d: Is a directory'))
    assert not match(Command('cat a', 'cat: d: Is a directory'))

# Generated at 2022-06-14 09:36:15.576332
# Unit test for function match
def test_match():
    assert match(Command('cat /home/user/'))
    assert not match(Command('cat file.txt'))



# Generated at 2022-06-14 09:36:18.669200
# Unit test for function match
def test_match():
    assert match(Command('cat testdir', 'cat: testdir: Is a directory'))
    assert not match(Command('cat testdir', 'cat: testdir: Is a file'))


# Generated at 2022-06-14 09:36:23.948296
# Unit test for function match
def test_match():
    assert match('cat file.txt')
    assert match('cat file.txt >> file.txt')
    assert match('cat file1.txt file2.txt')
    assert not match('less file.txt')
    assert not match('cat')
    assert not match('cat .')



# Generated at 2022-06-14 09:36:26.788645
# Unit test for function match
def test_match():
    assert match(Command('cat', 'cat: example: Is a directory'))
    assert match(Command('cat', 'cat: example: Is a directory')) is False


# Generated at 2022-06-14 09:37:18.270191
# Unit test for function match
def test_match():
    assert match(Command('cat /home/arthurnn', '', 'cat: /home/arthurnn: Is a directory'))
    assert not match(Command('cat /tmp/doesnotexist', '', 'cat: /tmp/doesnotexist: No such file or directory'))


# Generated at 2022-06-14 09:37:26.283968
# Unit test for function match
def test_match():
    from thefuck.rules.cat_is_a_directory import match
    assert match(Command('cat dir', 'cat: dir: Is a directory', ''))
    assert not match(Command(
        'cat dir', 'cat: dir: No such file or directory', ''))
    assert not match(Command('cat dir', 'cat: dir: No such file', ''))


# Generated at 2022-06-14 09:37:28.792739
# Unit test for function match
def test_match():
    assert match(Command('cat README.md', 'cat: README.md: Is a directory'))
    assert not match(Command('ls README.md', 'cat: README.md: Is a directory'))


# Generated at 2022-06-14 09:37:34.132163
# Unit test for function match
def test_match():
    assert match(Command('cat my_folder', '', 'cat: my_folder: Is a directory'))
    assert match(Command('cat my_folder other_file', '', 'cat: my_folder: Is a directory'))
    assert not match(Command('cat my_file', '', ''))


# Generated at 2022-06-14 09:37:38.883793
# Unit test for function match
def test_match():
    command1 = Command('cat /usr/lib/', '')
    command2 = Command('cat /etc/', '')
    command3 = Command('cat /var/log/', '')
    assert match(command1)
    assert match(command2)
    assert match(command3)



# Generated at 2022-06-14 09:37:45.979074
# Unit test for function match
def test_match():
    # global command
    # command = Command('cat 127.0.0.1', 'cat: 127.0.0.1: Is a directory')
    assert match(Command('cat 127.0.0.1', 'cat: 127.0.0.1: Is a directory'))

    assert not match(Command('cat 127.0.0.1', 'cat: 127.0.0.1: No such file or directory'))


# Generated at 2022-06-14 09:37:49.183877
# Unit test for function match
def test_match():
    assert match(Command('cat test', 'cat: test: Is a directory'))
    assert not match(Command('cat test', ''))
    assert not match(Command('echo test', ''))


# Generated at 2022-06-14 09:37:56.487027
# Unit test for function match
def test_match():
    # assert match(Command('cat file.txt', '', '')) is False
    # assert match(Command('cat /home', '', '')) is False
    assert match(Command('cat dir', '', 'cat: dir: Is a directory')) is True
    # assert match(Command('cat file.txt', '', '')) is False
    # assert match(Command('cat /home', '', '')) is False


# Generated at 2022-06-14 09:37:58.551854
# Unit test for function match
def test_match():
    assert match(Command("cat foo", ""))
    assert not match(Command("cat foo", "foo"))


# Generated at 2022-06-14 09:38:04.644418
# Unit test for function match
def test_match():
    command = Command('cat dir')
    assert match(command)
    command = Command('cat file')
    assert match(command) is False
#
# # Unit test for function get_new_command
# def test_get_new_command():
#     command = Command('cat dir')
#     assert get_new_command(command) == 'ls dir'

# Generated at 2022-06-14 09:39:39.010571
# Unit test for function match
def test_match():
    assert not match(Command('cat /'))
    assert match(Command('cat /tmp/'))



# Generated at 2022-06-14 09:39:41.377456
# Unit test for function match
def test_match():
    assert match(Command('cat hello', 'cat: hello: Is a directory'))
    assert not match(Command('cat hello.txt', 'hello'))



# Generated at 2022-06-14 09:39:45.115659
# Unit test for function match
def test_match():
    assert match(Command('cat /etc/hosts'))
    assert not match(Command('ls ~'))
    assert not match(Command('cat /etc/hosts', output='cat: /etc/hosts: Is a directory\n'))



# Generated at 2022-06-14 09:39:48.003610
# Unit test for function match
def test_match():
    assert match(Command('cat /home/user/test'))
    assert not match(Command('cat test'))
    assert not match(Command('cat'))


# Generated at 2022-06-14 09:39:53.128966
# Unit test for function match
def test_match():
    assert match(Command(script='cat test_file', output='cat: test_file: Is a directory'))
    assert not match(Command(script='ls test_file', output='cat: test_file: Is a directory'))
    assert not match(Command(script='cat', output='cat: test_file: Is a directory'))
