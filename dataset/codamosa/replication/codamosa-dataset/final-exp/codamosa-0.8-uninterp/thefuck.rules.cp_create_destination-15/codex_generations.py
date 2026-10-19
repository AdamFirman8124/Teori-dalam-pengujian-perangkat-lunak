

# Generated at 2022-06-14 09:40:59.191157
# Unit test for function match
def test_match():
    assert match(Command('cp -a /foo_bar/ /baz_bar', '/bin/cp: /foo_bar/: No such file or directory', '',
                         'cp -a /foo_bar/ /baz_bar', '', ''))
    assert match(Command('mv --help /de/invalidpath/', 'cp: directory /de/invalidpath/ does not exist', '',
                         'mv --help /de/invalidpath/', '', ''))
    assert not match(Command('ls -d foo_bar', '', '', 'ls -d foo_bar', '', ''))



# Generated at 2022-06-14 09:41:11.899558
# Unit test for function match
def test_match():
    assert match(Command('cp file1 file2 file3 /tmp/folder/', '', '', '', ''))
    assert match(Command('mv file1 file2 file3 /tmp/folder/', '', '', '', ''))
    assert match(Command('cp file1 file2 file3 /tmp/folder/', '', '', '', ''))
    assert match(Command('cp file1 file2 file3 /tmp/folder/', 'cp: cannot create regular file ‘/tmp/folder/’: No such file or directory\ncp: failed to extend ‘/tmp/folder/’: No space left on device', '', '', ''))

# Generated at 2022-06-14 09:41:18.305359
# Unit test for function match
def test_match():
    command = Command('cp ./test.c /home/test/', 'cp: cannot stat '
        '\'./test.c\': No such file or directory')
    assert match(command)
    command = Command('mv ./test.c /home/test/', 'mv: cannot stat '
        '\'./test.c\': No such file or directory')
    assert match(command)


# Generated at 2022-06-14 09:41:22.347451
# Unit test for function match
def test_match():
    correct_cmd = Command('cp a b', 'cp: target `b` is not a directory')
    wrong_cmd = Command('cp a b', 'cp: cannot stat `a`: No such file or directory')

    assert match(correct_cmd) == True
    assert match(wrong_cmd) == False

#Unit test for function get_new_command

# Generated at 2022-06-14 09:41:29.908394
# Unit test for function match
def test_match():
    assert match({'output': 'cp: directory ‘testing123’ does not exist'})
    assert match({'output': 'cp abc/def abc/xyz: No such file or directory'})
    assert match({'output': 'cp abc/def abc/xyz: No such file or directory'})
    assert not match({'output': 'cp: missing destination file operand after ‘file’'})
    assert not match({'output': 'cp: cannot stat ‘file’: No such file or directory'})
    # Unit test for function get_new_command
    assert get_new_command(Command('cp abc/def abc/xyz', '')) == 'mkdir -p abc/xyz && cp abc/def abc/xyz'

# Generated at 2022-06-14 09:41:33.655709
# Unit test for function match
def test_match():
    command = Command(script = 'cp',
                      output = 'cp: target ‘a’ is not a directory')
    assert match(command)



# Generated at 2022-06-14 09:41:39.073965
# Unit test for function match
def test_match():
    command = Command("cp ./foo.bar ./bar.foo", "cp: cannot stat ‘./foo.bar’: No such file or directory")
    assert match(command)

    command = Command("cp ./foo.bar ./bar.foo", "cp: ./bar.foo: No such file or directory")
    assert match(command)



# Generated at 2022-06-14 09:41:50.415633
# Unit test for function match
def test_match():
    assert match(Command("cp /etc/hosts /etc/hosts.bak", "cp: '/etc/hosts' and '/etc/hosts.bak' are identical",
                        "cp /etc/hosts /etc/hosts.bak"))
    assert match(Command("mv /etc/hosts /etc/hosts.bak", "mv: '/etc/hosts' and '/etc/hosts.bak' are identical",
                        "mv /etc/hosts /etc/hosts.bak"))
    assert match(Command("cp /etc/hosts /etc/hosts.bak", "cp: cannot stat '/etc/hosts.bak': No such file or directory",
                        "cp /etc/hosts /etc/hosts.bak"))

# Generated at 2022-06-14 09:41:58.866538
# Unit test for function match
def test_match():
    command = Command('cp /usr/src/python-3.6.1/pymap3/pymap3/mailbox.c .', '/usr/src/python-3.6.1/pymap3')
    #expected_result = Command('cp /usr/src/python-3.6.1/pymap3/pymap3/mailbox.c .', '/usr/src/python-3.6.1/pymap3')
    expected_result = None

    result = match(command)

    assert expected_result == result


# Generated at 2022-06-14 09:42:02.634734
# Unit test for function match
def test_match():
    output = "cp: directory './test/test2/' does not exist\n"
    assert match(Command(script="cp -r ./test/test1/ ./test/test2", output=output))


# Generated at 2022-06-14 09:42:13.431718
# Unit test for function match
def test_match():
    command = Command("cp file1 file2", 
        "cp: cannot stat ‘file1’: No such file or directory")
    assert match(command)
    command = Command("cp -r dir1 dir2", 
        "cp: cannot stat ‘dir1’: No such file or directory")
    assert match(command)
    command = Command("mv file1.txt file2.txt", 
        "mv: cannot stat ‘file1.txt’: No such file or directory")
    assert match(command)


# Generated at 2022-06-14 09:42:19.358708
# Unit test for function match
def test_match():
    assert match(Command('cp *.* *.*', 'cp: cannot stat ‘*.*’: No such file or directory\n'))
    assert match(Command('cp *.* *.*', 'mkdir: cannot create directory ‘*.*’: No such file or directory'))
    assert match(Command('cp *.* *.*', 'cp: directory ‘-t’ does not exist\n'))


# Generated at 2022-06-14 09:42:32.344158
# Unit test for function match
def test_match():
    # Case 1: cp: cannot create regular file 'asdf.txt': No such file or directory
    # Case 2: cp: target 'copy_to' is not a directory
    test_match_case1 = ("cp src/file.txt copy_to/", "cp: cannot create regular file 'asdf.txt': No such file or directory")
    test_match_case2 = ("cp src/file.txt copy_to", "cp: target 'copy_to' is not a directory")
    assert match(*test_match_case1)
    assert match(*test_match_case2)

    # Case 3: mv src/file.txt copy_to/
    # Case 4: mv src/file.txt copy_to

# Generated at 2022-06-14 09:42:34.876045
# Unit test for function match
def test_match():
    assert match('cp foo.txt lala.txt')
    assert match('mv lala.txt lolo/')


# Generated at 2022-06-14 09:42:46.846788
# Unit test for function match
def test_match():
    assert match(Command("cp lololololololololololololololololololololololololol", "cp: cannot stat 'lololololololololololololololololololololololololol': No such file or directory\n"))
    assert match(Command("cp lololololololololololololololololololololololololol", "cp: omitting directory 'lolololololololololololololololololololololololololol'\n"))

# Generated at 2022-06-14 09:42:53.602090
# Unit test for function match
def test_match():
    assert match(Command('cp text.py text2.py', 'cp: cannot stat ‘text.py’: No such file or directory'))
    assert match(Command('cp text.py text2.py', 'cp: cannot stat ‘text.py’: No such file or directory\nmv: cannot stat ‘text.py’: No such file or directory'))
    assert not match(Command('cp text.py text2.py', 'cp: cannot stat ‘text.py’: No such file or directory\n'))
    assert not match(Command('cp text.py text2.py', ''))


# Generated at 2022-06-14 09:43:00.439809
# Unit test for function match
def test_match():
    assert match(Command("cp file1 file2", output="cp: directory file2 does not exist"))
    assert match(Command("mv file1 file2", output="mv: directory file2 does not exist"))
    assert match(Command("cp file1 file2", output="cp: file1 file2"))
    assert not match(Command("mv file1 file2", output="mv: file1 file2"))


# Generated at 2022-06-14 09:43:05.884186
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('cp /home/xin/fuck.py /home/xin/fuck', 'No such file or directory'))
    assert match(Command('cp /home/xin/fuck.py /home/xin/fuck', 'cp: directory `/home/xin/fuck` does not exist'))


# Generated at 2022-06-14 09:43:17.728042
# Unit test for function match
def test_match():
	output_nonexist = "cp: cannot stat 'nonexist': No such file or directory"
	assert match(Command("cp nonexist .", output_nonexist))
	assert match(Command("mv nonexist .", output_nonexist))
	output_filedoesnotexist = "cp: cannot stat 'nonexist/file': No such file or directory"
	assert match(Command("cp nonexist/file .", output_filedoesnotexist))
	assert match(Command("mv nonexist/file .", output_filedoesnotexist))
	output_dir = "cp: omitting directory 'nonexist'"
	assert match(Command("cp nonexist .", output_dir))
	assert match(Command("mv nonexist .", output_dir))

# Generated at 2022-06-14 09:43:25.399875
# Unit test for function match
def test_match():
    cp = Command("cp test.py Django/", "cp: cannot stat ‘test.py’: No such file or directory")
    assert match(cp)
    mv = Command("mv Django/test.py Django/", "mv: cannot move 'Django/test.py' to 'Django/'test.py': No such file or directory")
    assert match(mv)
    sp = Command("mv Django/test.py Django/", "mv: cannot stat 'Django/test.py': No such file or directory")
    assert match(sp)


# Generated at 2022-06-14 09:43:40.712726
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('cp foo.bar /tmp', '',
    'cp: /tmp/foo.bar: No such file or directory'))
    assert match(Command('mv foo.bar /tmp', '',
    'mv: cannot stat ‘foo.bar’: No such file or directory'))
    assert match(Command('cp foo.bar /tmp', '',
    'cp: cannot create regular file ‘/tmp/foo.bar’: No such file or directory'))
    assert match(Command('mv foo.bar /tmp', '',
    'mv: cannot stat ‘foo.bar’: No such file or directory'))

    assert not match(Command('nano foo.bar', '',
    'nano: foo.bar: No such file or directory'))

# Generated at 2022-06-14 09:43:47.096283
# Unit test for function match
def test_match():
    assert match(Command('cp foo bar', 'cp: cannot stat \'foo\': No such file or directory'))
    assert match(Command('cp foo bar', 'cp: directory \'foo\' does not exist'))



# Generated at 2022-06-14 09:43:57.956262
# Unit test for function match

# Generated at 2022-06-14 09:44:01.135590
# Unit test for function match
def test_match():
    assert match(Command("cp file1.txt file2.txt",
                         output="cp: cannot stat `file1.txt': No such file or directory"))


# Generated at 2022-06-14 09:44:13.385741
# Unit test for function match
def test_match():
    cp_not_exist_dir_output = (
        "cp: directory paths-of-command-that-does-not-exist does not exist"
    )
    mv_not_exist_dir_output = (
        "mv: cannot move 'paths-of-command-that-does-not-exist' to 'paths-of-command-that-does-not-exist/paths-of-command-that-does-not-exist': No such file or directory"
    )

    assert match(Command("cp this.txt paths-of-command-that-does-not-exist", cp_not_exist_dir_output))
    assert match(Command("mv this.txt paths-of-command-that-does-not-exist", mv_not_exist_dir_output))


# Generated at 2022-06-14 09:44:19.719604
# Unit test for function match
def test_match():
    assert match(Command(script = "cp a/b/c a/b/d"))
    assert match(Command(script = "mv a/b/c a/b/d"))
    assert match(Command(script = "cp a/b/c a/b/d", output = "cp: directory `a/b/d' does not exist"))


# Generated at 2022-06-14 09:44:24.313195
# Unit test for function match
def test_match():
    assert match(Command("cp foo bar/baz/", "cp: cannot stat 'foo': No such file or directory"))
    assert not match(Command("cp foo bar/baz/", "cp: cannot stat 'foo': No such file or directory", "/bin/cp"))


# Generated at 2022-06-14 09:44:35.186186
# Unit test for function match
def test_match():
    assert match(Command('rm rf.txt', "rm: cannot remove 'rf.txt': No such file or directory", ''))
    assert match(Command('cp abc.txt 123/', 'cp: omitting directory ‘123/’', "abc.txt abc.txt abc.txt"))
    assert not match(Command('ls', '', ''))
    assert not match(Command('ls rf.txt', '', ''))
    assert not match(Command('ls rf.txt', 'ls: cannot access rf.txt: No such file or directory', ''))
    assert match(Command('mv abc.txt rf.txt', "mv: cannot stat 'abc.txt': No such file or directory", ''))

# Generated at 2022-06-14 09:44:37.282496
# Unit test for function match
def test_match():
    assert match(Command("cd /tmp", "cd: /tmp: No such file or directory\n"))



# Generated at 2022-06-14 09:44:42.266545
# Unit test for function match
def test_match():
    assert match(Command(script="", stdout="cp: copy directory ‘node_modules’ to ‘node_modules1’: Directory does not exist\n"))
    assert not match(Command(script="", stdout="cp: cannot stat ‘qqq’: No such file or directory\n"))


# Generated at 2022-06-14 09:44:51.345716
# Unit test for function match
def test_match():
    assert match(Command(script='cp abc.txt def', output='No such file or directory'))
    assert match(Command(script='cp -a abc.txt /def/', output='No such file or directory'))
    
    assert not match(Command(script='cp abc.txt def', output='No such file or directory1'))
    assert not match(Command(script='cp abc.txt def', output='No such file or directory1'))



# Generated at 2022-06-14 09:44:57.205468
# Unit test for function match
def test_match():
    assert match(Command("cp foo bar", "cp: cannot stat 'foo': No such file or directory"))
    assert match(Command("cp foo bar", "cp: cannot create directory 'foo': No such file or directory"))
    assert not match(Command("cp foo bar", "not enough arguments"))


# Generated at 2022-06-14 09:45:05.161725
# Unit test for function match
def test_match():
    # Case 1: cp
    assert match(Command('cp /home/jordan/foo_dir/ /home/jordan/',
                 'cp: cannot create regular file ‘/home/jordan/foo_dir/’: No such file or directory', True, 1))
    # Case 2: mv
    assert match(Command('mv test1.txt test2.txt test_dir/',
                 'mv: cannot create regular file ‘test_dir/test2.txt’: No such file or directory', True, 1))


# Generated at 2022-06-14 09:45:15.065995
# Unit test for function match
def test_match():
    command = Command("cp blah blah blah", "cp: blah: No such file or directory")
    assert match(command)
    
    command = Command("cpt blah blah blah", "cpt: blah: No such file or directory")
    assert not match(command)
    
    command = Command("cp blah blah blah", "cpt: blah: No such file or directory")
    assert not match(command)
    
    command = Command("cp blah blah blah", "cp: directory blah does not exist")
    assert match(command)
    
    command = Command("mv blah blah blah", "mv: blah: No such file or directory")
    assert match(command)
    
    command = Command("mv blah blah blah", "mv: blah: No such file or directory")
    assert match(command)
    

# Generated at 2022-06-14 09:45:24.099554
# Unit test for function match
def test_match():
    assert match(Command("cp test.txt a", "cp: cannot stat 'test.txt': No such file or directory"))
    assert match(Command("cp test.txt a", "cp: cannot create regular file 'a': No such file or directory"))
    assert match(Command("cp -R src/include a", "cp: cannot stat 'src/include': No such file or directory"))
    assert match(Command("cp -R src/include a", "cp: cannot create directory 'a': No such file or directory"))
    assert not match(Command("cp test.txt a", "cp: cannot stat 'test.txt': Permission denied"))



# Generated at 2022-06-14 09:45:36.008673
# Unit test for function match
def test_match():
    assert match(Command(script='cp /home/folder/test.txt /home/folder/test2.txt',
             output="cp: cannot create regular file '/home/folder/test2.txt': No such file or directory\n"))

    assert not match(Command(script='cp /home/folder/test.txt /home/folder/test2.txt',
             output="cp: cannot create regular file '/home/folder/test2.txt': No such file or directory\n"))

    assert match(Command(script='mv /home/folder/test.txt /home/folder/test2.txt',
             output="mv: cannot create regular file '/home/folder/test2.txt': No such file or directory\n"))


# Generated at 2022-06-14 09:45:41.055028
# Unit test for function match
def test_match():
    assert match(Command('cp foo bar', 'cp: cannot stat ‘foo’: No such file or directory'))
    assert match(Command('mv foo bar', 'cp: cannot stat ‘foo’: No such file or directory'))
    assert match(Command('mv foo bar', 'cp: directory baz does not exist'))
    assert not match(Command('rm foo bar', 'cp: cannot stat ‘foo’: No such file or directory'))


# Generated at 2022-06-14 09:45:52.779155
# Unit test for function match
def test_match():
    assert match(Command("cp file /path/to/fie", "cp: cannot stat `file': No such file or directory")) == True
    assert match(Command("mv file /path/to/fie", "mv: cannot stat `file': No such file or directory")) == True
    assert (
        match(Command("cp -r folder /path/to/fie", "cp: directory folder does not exist")) == True
    )


# Uni test for function get_new_command

# Generated at 2022-06-14 09:46:00.415323
# Unit test for function match
def test_match():

    # Unit test for function match() when
    # output contains "No such file or directory"
    command_1 = Command("cp -r /tmp/not/existing /tmp/target")
    command_1.output = "cp: cannot stat '/tmp/not/existing': No such file or directory"
    assert match(command_1)

    # Unit test for function match() when
    # output starts with "cp: directory"
    # and ends with "does not exist"
    command_2 = Command("cp -r /tmp/not/existing /tmp/target")
    command_2.output = "cp: directory '123' does not exist"
    assert match(command_2)



# Generated at 2022-06-14 09:46:12.972177
# Unit test for function match
def test_match():
    assert match(
        Command(
            script="cp test.py test2.py",
            output="cp: cannot create regular file 'test2.py': No such file or directory\n",
        )
    )
    assert match(
        Command(
            script="cp test.py test2.py",
            output="cp: directory 'test2.py' does not exist\n",
        )
    )
    assert not match(
        Command(script="cp test.py test2.py", output="cp: no such file or directory: test2.py")
    )
    # This is another error message where you simply misspelled a directory.

# Generated at 2022-06-14 09:46:29.507848
# Unit test for function match
def test_match():
    assert match(
        Command(
            script="cp file1 file2 file3 file4",
            output="cp: cannot stat 'file3' No such file or directory",
        )
    )

    assert not match(
        Command(script="cp file1 file2 file3 file4", output="cp: file1 file2 file3 file4")
    )

    assert match(
        Command(
            script="mv file1 file2 file3 file4",
            output="mv: cannot stat 'file3' No such file or directory",
        )
    )

    assert not match(
        Command(script="mv file1 file2 file3 file4", output="mv: file1 file2 file3 file4")
    )


# Generated at 2022-06-14 09:46:42.234205
# Unit test for function match
def test_match():
    assert match(Command(script='cp file.txt /tmp/path/to/',
                         output='cp: target `/tmp/path/to/\' is not a directory'))
    assert match(Command(script='mv file.txt /tmp/path/to/',
                         output='mv: target `/tmp/path/to/\' is not a directory'))
    assert match(Command(script='cp file.txt /tmp/path/to/',
                         output='cp: directory `/tmp/path/to/\' does not exist'))
    assert match(Command(script='mv file.txt /tmp/path/to/',
                         output='mv: directory `/tmp/path/to/\' does not exist'))


# Generated at 2022-06-14 09:46:48.572505
# Unit test for function match

# Generated at 2022-06-14 09:46:59.726891
# Unit test for function match
def test_match():
    assert match(
        Command("rsync -r src/ dest/", "rsync: link_stat \"src/file\" failed: No such file or directory (2)\nrsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1052) [sender=3.0.9]")
    )

    assert not match(
        Command("rsync -r src/ dest/", "rsync: link_stat \"src/file\" failed: No such file or directory (2)")
    )



# Generated at 2022-06-14 09:47:07.362922
# Unit test for function match
def test_match():
    assert match(Command('git branch a/b', '', 'No such file or directory'))
    assert match(Command('git branch a/b', '', 'mkdir: cannot create directory ‘a/b’: No such file or directory'))
    assert match(Command('cp -r a b', '', 'cp: directory b does not exist'))


# Generated at 2022-06-14 09:47:17.599853
# Unit test for function match
def test_match():
    assert match(Command("cp a b", ""))
    assert match(Command("cp a b", "cp: target `b' is not a directory"))
    assert match(Command("cp a b", "cp: cannot create regular file `b/a': No such file or directory"))
    assert match(Command("cp -r a b", "cp: cannot create directory `b': No such file or directory"))
    assert match(Command("mv a b", "mv: cannot create directory `b': No such file or directory"))
    assert not match(Command("ls", "cp: cannot create directory `b': No such file or directory"))

# Generated at 2022-06-14 09:47:21.161988
# Unit test for function match
def test_match():
    result = thefuck.patterns.match.match(command.Command("cp source/file.txt dest/file.txt"))
    assert result == False

# Generated at 2022-06-14 09:47:31.115250
# Unit test for function match
def test_match():
    assert match(Command('cp a b', 'cp: cannot create regular file ‘b’: No such file or directory'))
    assert match(Command('mv a b', 'mv: cannot create regular file ‘b’: No such file or directory'))
    assert match(Command('cp a b', 'cp: target ‘b’ is not a directory'))
    assert match(Command('cp a b', 'cp: cannot stat ‘a’: No such file or directory'))
    assert match(Command('cp a b', 'cp: cannot stat ‘b’: No such file or directory'))
    assert not match(Command('ls', 'No such file or directory'))

# Generated at 2022-06-14 09:47:43.841530
# Unit test for function match
def test_match():
    assert match(Command('cp hello.txt hello.txt', 'cp: cannot stat \'hello.txt\': No such file or directory'))
    assert match(Command('mv hello.txt hello.txt', 'mv: cannot stat \'hello.txt\': No such file or directory'))
    assert match(Command('cp hello.txt hello.txt', 'cp: directory hello.txt does not exist'))
    assert match(Command('mv hello.txt hello.txt', 'mv: directory hello.txt does not exist'))
    assert not match(Command('cp hello.txt hello.txt', 'cp: cannot stat \'hello.txt\': No such file or directory\ncat: hello.txt: No such file or directory'))

# Generated at 2022-06-14 09:47:50.194735
# Unit test for function match
def test_match():
    assert(False == match(Command("cp")))
    assert(False == match(Command("cp -r ./dir1 ./dir1")))
    assert(False == match(Command("mv ./dir")))
    assert(False == match(Command("cp ./dir ./dir1")))
    assert(False == match(Command("cp -r ./folder ./dir1")))
    assert(True == match(Command("cp -r ./folder ")))
    assert(True == match(Command("cp ./dir1 ./dir2")))
    assert(True == match(Command("cp ./dir1 ./dir2")))


# Generated at 2022-06-14 09:48:01.118915
# Unit test for function match
def test_match():
    assert match(Command("cp test.txt test1.txt", "cp: cannot stat 'test.txt': No such file or directory"))
    assert match(Command("cp test.txt test1.txt", "cp: directory `test1.txt/' does not exist"))
    assert not match(Command("cd test1.txt", "test1.txt: No such file or directory"))


# Generated at 2022-06-14 09:48:08.070343
# Unit test for function match
def test_match():
    assert match(Command(script='cp ~/test/test.py', output='cp: ~/test/test.py: No such file or directory'))
    assert not match(Command(script='cp ~/test/test.py', output='cp: ~/test/test.py: No such file or directory2'))
    assert match(Command(script='cp ~/test/test.py', output='cp: directory /Users/username/test/test.py does not exist'))
    assert not match(Command(script='cp ~/test/test.py', output='cp: directory /Users/username/test/test.py does not exist2'))
    

# Generated at 2022-06-14 09:48:14.591302
# Unit test for function match
def test_match():
    assert match(Command('cp test.txt test/', 'cp: target `test/` is not a directory'))
    assert match(Command('cp test.txt test/', 'cp: test/: No such file or directory'))
    assert not match(Command('cp test.txt test/', 'cp: test: No such file or directory'))
    assert not match(Command('cp test.txt test/'))



# Generated at 2022-06-14 09:48:26.638015
# Unit test for function match
def test_match():
    assert match(Command('cp * /path/to/file',
                         '/home/dorian/test> cp * /path/to/file',
                         'cp: cannot stat \'*\': No such file or directory'))
    assert match(Command('mv * /path/to/file',
                         '/home/dorian/test> mv * /path/to/file',
                         'cp: cannot stat \'*\': No such file or directory'))
    assert match(Command('cp * /path/to/file',
                         '/home/dorian/test> cp * /path/to/file',
                         'mv: cannot stat \'*\': No such file or directory'))

# Generated at 2022-06-14 09:48:36.708369
# Unit test for function match
def test_match():
    assert match(Command(script="foo", stderr="cp: cannot stat '/home/bob/foo'", output=""))
    assert match(Command(script="bar", stderr="cp: cannot stat '/home/bob/bar'", output=""))
    assert match(Command(script="s", stderr="cp: cannot stat '/home/bob/s'", output=""))
    assert not match(Command(script=r"foo 'bar\baz'", stderr="", output=""))
    assert not match(Command(script="cp Foo /bar/baz", stderr="", output=""))
    assert match(Command(script="cp a b", stderr="cp: cannot stat 'a': No such file or directory", output=""))

# Generated at 2022-06-14 09:48:39.577298
# Unit test for function match
def test_match():
    assert match(Command("cp test.txt test", "", "cp: directory test does not exist")).is_true()



# Generated at 2022-06-14 09:48:52.913680
# Unit test for function match
def test_match():
    assert match(Command(script="cp a b", output="cp: /target: No such file or directory"))
    assert match(Command(script="mv a b", output="mv: /target: No such file or directory"))
    assert match(Command(script="cp a b", output="cp: target: No such file or directory"))
    assert match(Command(script="mv a b", output="mv: target: No such file or directory"))
    assert match(Command(script="cp a b", output="cp: directory /target does not exist"))
    assert match(Command(script="mv a b", output="mv: directory /target does not exist"))
    assert match(Command(script="cp a b", output="cp: /target: No such file or directory"))

# Generated at 2022-06-14 09:49:05.867031
# Unit test for function match
def test_match():
    assert match(Command('cp a file.txt /path', '', 'cp: cannot stat \'a\': No such file or directory', 0))
    assert match(Command('cp -r a b', '', 'cp: cannot stat \'a\': No such file or directory', 0))
    assert match(Command('cp -r a b', '', 'cp: -r not specified; omitting directory ', 0))
    assert match(Command('cp -r a b', '', '', 0))
    assert match(Command('cp a file.txt /path', '', 'cp: omitting directory  ', 0))
    assert match(Command('mv /tmp/doesnotexist /tmp/', '', 'mv: cannot stat \'/tmp/doesnotexist\': No such file or directory', 0))

# Generated at 2022-06-14 09:49:12.623308
# Unit test for function match

# Generated at 2022-06-14 09:49:23.716932
# Unit test for function match
def test_match():
	assert match(Command("cp test.txt project/", "cp: cannot stat 'test.txt': No such file or directory")) is True
	assert match(Command("mv test.txt project/", "mv: cannot stat 'test.txt': No such file or directory")) is True
	assert match(Command("cp -r test.txt project/", "cp: cannot stat 'test.txt': No such file or directory")) is True
	assert match(Command("cp -r test.txt project/", "cp: directory 'project/' does not exist")) is True
	assert match(Command("cp -r test.txt project/", "cp: cannot stat 'test.txt': No such file or directory\ncp: cannot stat 'test.txt': No such file or directory\ncp: directory 'project/' does not exist")) is True

# Generated at 2022-06-14 09:49:41.864633
# Unit test for function match
def test_match():
    assert match(Command('cp foo bar', ''))
    assert match(Command('cp foo bar', 'cp: cannot create regular file ‘bar’: No such file or directory'))
    assert match(Command('mv foo bar', ''))
    assert match(Command('mv foo bar', 'mv: cannot create regular file ‘bar’: No such file or directory'))
    assert match(Command('cp -r foo bar', ''))
    assert match(Command('cp -r foo bar', 'cp: cannot create directory ‘bar’: No such file or directory'))
    assert match(Command('cp -r foo bar', "cp: omitting directory 'foo'"))
    assert match(Command('mv -r foo bar', ''))

# Generated at 2022-06-14 09:49:53.945856
# Unit test for function match
def test_match():
    assert match(Command('cp foo bar', 'cp: cannot stat `foo\': No such file or directory'))
    assert match(Command('cp foo bar', 'cp: directory `bar\' does not exist'))
    assert match(Command('cp -r foo bar', 'cp: cannot stat `foo\': No such file or directory'))
    assert match(Command('cp foo bar', 'cp: directory `bar\' does not exist'))
    assert not match(Command('foo', ''))
    assert not match(Command('cp foo bar', 'cp: cannot stat `foo\': No such file or directory, `bar\' does not exist'))
    assert not match(Command('cp foo bar', 'cp: cannot stat `foo\': No such file or directory'))
    assert not match(Command('cp foo bar', 'cp: `foo\' does not exist'))

# Generated at 2022-06-14 09:50:04.246272
# Unit test for function match
def test_match():
    assert (
        match(
            Command(
                "cp  -a /tmp/foo_bar /opt/lampp/htdocs/",
                "cp: cannot create regular file '/opt/lampp/htdocs/': No such file or directory\n",
            )
        )
        is True
    )
    assert (
        match(
            Command(
                "mv /tmp/foo_bar/ /opt/lampp/htdocs/",
                "mv: cannot move '/tmp/foo_bar/' to '/opt/lampp/htdocs/': No such file or directory\n",
            )
        )
        is True
    )

# Generated at 2022-06-14 09:50:10.310504
# Unit test for function match
def test_match():
    assert not match(Command(script="cd /tmp", output="/tmp: No such file or directory"))
    assert not match(Command(script="cp file target", output="cp: target: No such file or directory"))
    assert match(Command(script="cp file target", output="cp: target: No such file or directory"))
    assert match(Command(script="cp file target", output="target: No such file or directory"))


# Generated at 2022-06-14 09:50:18.001953
# Unit test for function match
def test_match():
    command = Command('mv test.py test/test.py', 'mv: cannot stat \'test.py\': No such file or directory')
    assert match(command)
    command = Command('cp -rf file/ test/', 'cp: directory file/ does not exist')
    assert match(command)
    command = Command('cp file/ test/', 'cp: directory file/ does not exist')
    assert match(command)
    command = Command('mv file/ test/', 'mv: cannot stat \'file/\': No such file or directory')
    assert match(command)
    command = Command('cp -rf file/ test/', '/bin/cp: cannot stat \'file/\': No such file or directory')
    assert not match(command)

# Generated at 2022-06-14 09:50:30.331581
# Unit test for function match
def test_match():
    assert match(Command("cp", "error: No such file or directory"))
    assert match(Command("cp file1 file2", "error: No such file or directory"))
    assert match(Command("cp file1 file2 file3", "error: No such file or directory"))
    assert match(Command("cp file1 /aaa/bbb", "cp: cannot create regular file '/aaa/bbb': No such file or directory"))

    assert not match(Command("cp", ""))
    assert not match(Command("cp", "error"))
    assert not match(Command("cp file1", ""))
    assert not match(Command("cp file1", "error"))
    assert not match(Command("cp file1 file2", ""))
    assert not match(Command("cp file1 file2", "error"))

# Generated at 2022-06-14 09:50:45.129928
# Unit test for function match
def test_match():
    cp_case = Command("cp file1 file2")
    assert match(cp_case)
    cp_case2 = Command("cp file1 file2", "cp: cannot stat 'file1': No such file or directory")
    assert match(cp_case2)
    cp_case3 = Command("cp file1 file2", "cp: cannot stat 'file1': No such file or directory\n")
    assert match(cp_case3)
    mv_case = Command("mv file1 file2")
    assert match(mv_case)
    mv_case2 = Command("mv file1 file2", "mv: cannot stat 'file1': No such file or directory")
    assert match(mv_case2)

# Generated at 2022-06-14 09:50:49.029018
# Unit test for function match
def test_match():
    assert match(Command("cp folder01/archive.zip folder02"))
    assert match(Command("mv folder01/archive.zip folder02"))
    assert not match(Command("git init"))

