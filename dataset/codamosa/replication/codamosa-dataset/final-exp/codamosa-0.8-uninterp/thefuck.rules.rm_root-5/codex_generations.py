

# Generated at 2022-06-14 10:36:06.258665
# Unit test for function match
def test_match():
    command1 = 'rm /'
    command2 = 'rm -r /'
    command3 = 'rm -rf /'
    command4 = 'rm -rf / --no-preserve-root'
    command5 = 'rm -rf / --no-preserve-root --recursive'

    assert match(Command(command1, '', '', ''))
    assert match(Command(command2, '', '', ''))
    assert match(Command(command3, '', '', ''))
    assert not match(Command(command4, '', '', ''))
    assert not match(Command(command5, '', '', ''))

# Generated at 2022-06-14 10:36:10.352739
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf /')
    assert get_new_command(command) == u'rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:36:15.159668
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’\n'
            'rm: use --no-preserve-root to override this failsafe\n')
    assert get_new_command(command) == 'rm -rf --no-preserve-root /'



# Generated at 2022-06-14 10:36:19.081512
# Unit test for function get_new_command
def test_get_new_command():
    # Prepare
    command = Command("rm -rf /", "")

    # Assert
    expected_result = u"rm -rf / --no-preserve-root"
    assert get_new_command(command) == expected_result

# Generated at 2022-06-14 10:36:29.121872
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', '', 'rm: it is dangerous to operate recursively on ‘/’\n'
                         'rm: use --no-preserve-root to override this failsafe'))
    assert not match(Command('rm -rf  /', '', ''))
    assert not match(Command('rm -rf /', '', 'rm: it is dangerous to operate recursively on ‘/’\n'
                             'rm: use --preserve-root to override this failsafe'))



# Generated at 2022-06-14 10:36:33.050418
# Unit test for function match
def test_match():
    assert match('rm /')
    assert match('rm /tmp/')
    assert match('rm / --preserve-root --quiet')
    assert not match('rm /home/')
    assert not match('rm -rf /')
    assert not match('mkdir /')



# Generated at 2022-06-14 10:36:37.219687
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('cd / | rm -rf somearg', '', '')
    assert get_new_command(command) == 'cd / | rm -rf --no-preserve-root somearg'

# Generated at 2022-06-14 10:36:41.613959
# Unit test for function match
def test_match():
    command_output = Command('rm /', '\nrm: it is dangerous to operate rm recursively on '/'\nUse --no-preserve-root to override this failsafe\n')
    assert match(command_output)
    assert not match(Command('ls', ''))

# Generated at 2022-06-14 10:36:51.120025
# Unit test for function match
def test_match():
    assert match(Command('rm /', '', 'rm: it is dangerous to operate recursively on '/'\n' + 'Use --no-preserve-root to override this failsafe'))
    assert match(Command('rm /home', '', 'rm: it is dangerous to operate recursively on '/'\n' + 'Use --no-preserve-root to override this failsafe'))
    assert not match(Command('ls /', '', 'ls: it is dangerous to operate recursively on '/'\n' + 'Use --no-preserve-root to override this failsafe'))
    assert not match(Command('rm home', '', 'ls: it is dangerous to operate recursively on '/'\n' + 'Use --no-preserve-root to override this failsafe'))


# Generated at 2022-06-14 10:37:00.160541
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -f /', 'rm: it is dangerous to operate recursively on \'/\'\nrm: use --no-preserve-root to override this failsafe\n')
    assert get_new_command(command) == 'rm -f / --no-preserve-root'


# Generated at 2022-06-14 10:37:04.982104
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm -rf /') == 'rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:37:17.440917
# Unit test for function match
def test_match():
    assert_true(match(Command('rm -rf / --no-preserve-root', '', 0, '')))
    assert_true(match(Command('rm -rf /', '', 2, 'rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe')))
    assert_false(match(Command('rm -rf / --no-preserve-root', '', 2, '')))
    assert_false(match(Command('rm -rf /', '', 2, 'rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe\n')))
    assert_false(match(Command('rm -rf /', '', 0, '')))

# Generated at 2022-06-14 10:37:21.864630
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm -r /', 'rm: cannot remove \'/\': Is a directory',
    'echo "rm: cannot remove \'/\': Is a directory"; exit 1')) == 'rm -r --no-preserve-root /'



# Generated at 2022-06-14 10:37:27.674958
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("rm /", "rm: it is dangerous to operate recursively on '/'\n"
                              "rm: use --no-preserve-root to override this failsafe")
    new_command = get_new_command(command)
    assert new_command == "rm --no-preserve-root /"

# Generated at 2022-06-14 10:37:37.077380
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', ''))
    assert match(Command('rm -r /', '', ''))
    assert match(Command('rm -rf /', 'ERROR: / is used in essential ways.'))
    assert match(Command('rm -rf', ''))
    assert match(Command('rm -rf /', ''))
    assert match(Command('rm -rf /', '', ''))
    assert match(Command('rm -rf /', '', ''))
    assert match(Command('rm -rf /', '', ''))
    assert match(Command('rm -rf /', '', ''))
    assert match(Command('rm -rf /', '', ''))



# Generated at 2022-06-14 10:37:43.869622
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='rm -r /', output='rm: it is dangerous to operate recursively on '/'', stderr='use --no-preserve-root to override this failsafe')
    get_new_command(command)
    assert command.script == 'rm -r --no-preserve-root /'

# Generated at 2022-06-14 10:37:53.396836
# Unit test for function match
def test_match():
    # test for enabled by default
    assert match(Command('rm'))
    assert not match(Command('rm /'))
    assert match(Command('rm / --no-preserve-root'))
    assert not match(Command('rm / --no-preserve-root'
                             ' && echo \'Error: not preserved root\''))
    assert match(Command('sudo rm /'))
    assert not match(Command('sudo rm / --no-preserve-root'))
    assert not match(Command('rm / --no-preserve-root'
                             ' && echo \'Error: not preserved root\''
                             ' && sudo rm /'))



# Generated at 2022-06-14 10:38:02.111605
# Unit test for function match
def test_match():
    command = Command('rm -rf /')
    assert match(command)
    command = Command('rm /')
    assert not match(command)
    command = Command('rm --no-preserve-root -rf /')
    assert match(command)
    command = Command('rm --no-preserve-root /')
    assert not match(command)


# Unit test function get_new_command

# Generated at 2022-06-14 10:38:09.285947
# Unit test for function match
def test_match():
    # test if rm -rf / is detected
    command_output = Command('rm', '-rf', '/')
    assert match(command_output)

    # test if rm -rf --no-preserve-root / is not detected
    command_output = Command('rm', '-rf', '--no-preserve-root', '/')
    assert not match(command_output)


# Generated at 2022-06-14 10:38:16.579345
# Unit test for function match
def test_match():
    assert match(Command(script='rm -rf /',
                         output='rm: it is dangerous to operate recursively on ‘/’'))
    assert not match(Command(script='rm -rf /',
                             output='rm: cannot remove ‘/’: Is a directory'))
    assert not match(Command(script='rm -rf /',
                             output='rm: missing operand'))



# Generated at 2022-06-14 10:38:30.529676
# Unit test for function match
def test_match():
    string = u'rm: cannot remove \'foo\': Permission denied'
    mock_command = Mock(script=u'rm foo',
                        output=string,
                        script_parts = command.script.split(' '))
    assert match(mock_command)


# Generated at 2022-06-14 10:38:32.803097
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /'))
    assert not match(Command('git rm -rf /'))
    assert match(Command('rm -rf --no-preserve-root /'))
    assert not match(Command('rm -rf --no-preserve-root /', '', ''))

# Generated at 2022-06-14 10:38:37.159308
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('sudo rm /home/')) == 'sudo rm --no-preserve-root /home/'

# Generated at 2022-06-14 10:38:42.160142
# Unit test for function get_new_command
def test_get_new_command():
	script = 'rm file1 file2 file3'

# Generated at 2022-06-14 10:38:45.919589
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm /') == 'rm / --no-preserve-root'
    assert get_new_command('sudo rm /') == 'sudo rm / --no-preserve-root'


# Generated at 2022-06-14 10:38:49.449332
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf /', '', '/bin/rm: cannot remove \'/\': Is a directory\n')
    assert get_new_command(command) == 'rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:38:56.757216
# Unit test for function match
def test_match():
    command = Command('rm /', '', '/')
    assert match(command)
    command = Command('rm -rf /', '', '/')
    assert match(command)

# Generated at 2022-06-14 10:39:00.991145
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', 0, u'', u'', u'rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe'))


# Generated at 2022-06-14 10:39:06.507034
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

# Generated at 2022-06-14 10:39:09.307752
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo rm -rf /')) == 'sudo rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:39:17.805756
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf /', '', '', '')
    assert get_new_command(command) == 'rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:39:25.120965
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('rm -r /',
                output="rm: it is dangerous to operate recursively on '/'\n" +
                       "rm: use --no-preserve-root to override this " +
                       "warning\nrm: when possible, remove '/' rather than " +
                       "recurse on it\n")) == "rm -r / --no-preserve-root"

# Generated at 2022-06-14 10:39:33.059865
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command(script='rm', output='rm: cannot remove ‘/’: Is a directory', stderr=True)) == u'rm --no-preserve-root'
    assert get_new_command(Command(script='rm', output='rm: cannot remove ‘/’: Is a directory', stderr=True, sudo=True)) == u'sudo rm --no-preserve-root'

# Generated at 2022-06-14 10:39:35.651372
# Unit test for function match
def test_match():
    assert match(Command('rm / --no-preserve-root', ''))



# Generated at 2022-06-14 10:39:39.498020
# Unit test for function get_new_command
def test_get_new_command():  # pragma: no cover
    command = "rm -rf /"
    new_command = get_new_command(command)
    assert new_command == "sudo rm -rf / --no-preserve-root"

# Generated at 2022-06-14 10:39:42.849102
# Unit test for function get_new_command
def test_get_new_command():
    # Test get_new_command for non-sudo command
    command = Command('sudo rm /')
    assert get_new_command(command) == 'sudo rm --no-preserve-root /'

# Generated at 2022-06-14 10:39:48.189884
# Unit test for function get_new_command
def test_get_new_command():
    # This command will trigger match function
    assert get_new_command('rm -rf /') == 'rm --no-preserve-root -rf /'
    # This command will not trigger match function
    assert get_new_command('rm -rf /tmp') == 'rm -rf /tmp'

# Generated at 2022-06-14 10:39:52.382005
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm /', '', "/bin/rm: it is dangerous to operate recursively on '/'\nUse --no-preserve-root to override this failsafe.")
    assert get_new_command(command) == "rm / --no-preserve-root"


# Generated at 2022-06-14 10:39:58.072209
# Unit test for function match
def test_match():
    assert match(Command('rm -r /', output='ERROR: --no-preserve-root'))
    assert not match(Command('rm -r /', output='ERROR: --no-preserve-roote'))
    assert not match(Command('rm -r /'))
    assert not match(Command('rm -r /', output=''))



# Generated at 2022-06-14 10:40:11.796116
# Unit test for function match
def test_match():
    string = "rm -rf /"
    assert match(Command(script = string, output = "rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe"))
    string = "rm -rf"
    assert not match(Command(script = string, output = "rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe"))
    string = "rm -rf / --no-preserve-root"
    assert not match(Command(script = string, output = "rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe"))


# Generated at 2022-06-14 10:40:25.406947
# Unit test for function match
def test_match():
    assert match(Command('rm -r /',
                         'rm: it is dangerous to operate recursively on ‘/’\n'
                         'rm: use --no-preserve-root to override this failsafe'))


# Generated at 2022-06-14 10:40:35.101749
# Unit test for function match
def test_match():
    output = 'rm: it is dangerous to operate recursively'
    output += ' on `/\' so we fail by default.  If you really want'
    output += ' this, then use --no-preserve-root to overcome this'
    output += ' failsafe.'
    assert_true(match(Command('rm -rf /', output)))
    assert_true(match(Command('sudo rm -rf /', output)))


# Generated at 2022-06-14 10:40:37.582417
# Unit test for function match
def test_match():
    command = Command('rm /')

    assert match(command)

    command = Command('rm -rf /')

    assert match(command)


# Generated at 2022-06-14 10:40:43.967522
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='rm -rf /', output='rm: it is dangerous to operate recursively on ‘/’\n'
                                                 'rm: use --no-preserve-root to override this failsafe')
    assert get_new_command(command) == "rm -rf / --no-preserve-root"

# Generated at 2022-06-14 10:40:54.789515
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', 'mystdout', 'mystderr')) is True
    assert match(Command('rm -rf /', 'mystdout', 'mystderr', 'myscript')) is True
    assert match(Command('rm -rf /', 'mystdout', 'mystderr', 'myscript', 'myscript_parts')) is True
    assert match(Command('rm -rf /', 'mystdout', 'mystderr', 'myscript', 'myscript_parts')) is True
    assert match(Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’\n'
                                     'rm: use --no-preserve-root to override this failsafe', 'mystderr')) is True

# Generated at 2022-06-14 10:41:07.357299
# Unit test for function match
def test_match():
    command = Command(script=u'rm -f /',
        stdout=u'rm: it is dangerous to operate recursively on \'\'/\nrm: use --no-preserve-root to override this failsafe\n')

    assert match(command)

    command = Command(script=u'rm -f / --no-preserve-root',
        stdout=u'rm: it is dangerous to operate recursively on \'\'/\nrm: use --no-preserve-root to override this failsafe\n')

    assert not match(command)



# Generated at 2022-06-14 10:41:13.065011
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm /', 'rm: it is dangerous to operate recursively on ‘/’\n'
                              'rm: use --no-preserve-root to override this failsafe\n',
                      script_parts={'rm', '/'})
    assert get_new_command(command) == 'rm / --no-preserve-root'

# Generated at 2022-06-14 10:41:24.234335
# Unit test for function match
def test_match():
    assert match(Command('rm /', '', '/bin/rm: it is dangerous to operate recursively on '/', use --no-preserve-root'))
    assert not match(Command('rm /'))
    assert not match(Command('rm', ''))
    assert not match(Command('rm /', '', 'lalala'))
    assert match(Command('sudo rm /', '', '/bin/rm: it is dangerous to operate recursively on '/', use --no-preserve-root'))
    assert match(Command('sudo rm /', '', '/bin/rm: warning: it is dangerous to operate recursively on '/', use --no-preserve-root'))

# Generated at 2022-06-14 10:41:31.597692
# Unit test for function match
def test_match():
    command = Command('rm -rf /', '')
    assert match(command)
    
    command = Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’\nUse --no-preserve-root to override this failsafe.')
    assert match(command)
    
    command = Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’\nUse --no-preserve-root to override this failsafe.\nrm: it is dangerous to operate recursively on ‘/’\nUse --no-preserve-root to override this failsafe.')
    assert match(command)
    

# Generated at 2022-06-14 10:41:44.287331
# Unit test for function match
def test_match():
    # -rw-rw-r-- 1 testuser testuser 0 Aug  2 11:28 testfile
    assert not match('rm testfile')
    assert match('rm -rf /')
    assert match('rm -rf / -rf /')
    assert not match('rm -rf --no-preserve-root / -rf --no-preserve-root /')

    assert not match('rm /')
    assert not match(u'rm \u00f6')
    assert not match('rm -r1 /')



# Generated at 2022-06-14 10:42:15.670529
# Unit test for function match
def test_match():
    command = Command('rm /', 'rm: it is dangerous to operate recursively on '
        '<target>\nrm: use --no-preserve-root to override this failsafe\n')
    assert match(command) == True
    command = Command('rm file', 'rm: it is dangerous to operate recursively on '
        '<target>\nrm: use --no-preserve-root to override this failsafe\n')
    assert match(command) == False
    command = Command('rm testfile', 'rm: it is dangerous to operate '
        'recursively on <target>\nrm: use --no-preserve-root to override '
        'this failsafe\n')
    assert match(command) == False

# Generated at 2022-06-14 10:42:21.244570
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /',
                                '',
                                'rm: it is dangerous to operate recursively on ‘/’\n'
                                'rm: use --no-preserve-root to override this failsafe', 2))
    assert not match(Command('rm -rf /', '', '', 2))
    assert not match(Command('rm -rf /', '', 'rm: missing operand\n', 1))


# Generated at 2022-06-14 10:42:32.864376
# Unit test for function match
def test_match():

    script_parts = ['rm', 'asdf', 'asdf/']
    script = 'rm asdf asdf/'
    output = 'rm: cannot remove ‘asdf/’: Permission denied'

    command = Command(script,script_parts,output)


    assert match(command) == True

    script_parts = ['rm', '-asdf', '--preserve-root']
    script = 'rm -asdf --preserve-root'
    output = 'rm: missing operand'

    command = Command(script,script_parts,output)

    assert match(command) == True

    script_parts = ['rm', '-asdf', '--preserve-root']
    script = 'rm -asdf --preserve-root'
    output = 'rm: missing operand'


# Generated at 2022-06-14 10:42:35.020268
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo rm / -r')) == u'sudo rm / -r --no-preserve-root'

# Generated at 2022-06-14 10:42:38.803607
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm /', "rm: cannot remove `/' directory\nremoving write-protected regular empty file `/file1'\nrm: cannot remove `/file1'\n", '', 9)) == 'rm --no-preserve-root /'

# Generated at 2022-06-14 10:42:45.816379
# Unit test for function match
def test_match():
    command = "rm -rf /"
    assert match(command) is True, "rm -rf / exec without --no-preserve-root"
    command = "rm -rf / --no-preserve-root"
    assert match(command) is False, "rm -rf / exec with --no-preserve-root"
    command = "echo rm -rf /"
    assert match(command) is False
    command = "rm /"
    assert match(command) is True

# Generated at 2022-06-14 10:42:52.151261
# Unit test for function match
def test_match():

    # Case1
    # Case1.1
    # command1
    command1 = Command('rm -rf /')
    # command2
    # The function get_new_command is not applicable to command2
    command2 = Command('rm -rf .')

    # Test
    # Case1.1
    assert match(command1) == True
    # Case1.2
    assert match(command2) == False



# Generated at 2022-06-14 10:42:58.868209
# Unit test for function match
def test_match():
    print ("testing match()")

# Generated at 2022-06-14 10:43:02.370403
# Unit test for function match
def test_match():
    command = create_command('rm /')
    assert match(command)
    command = create_command('rm / --no-preserve-root')
    assert not match(command)


# Generated at 2022-06-14 10:43:07.689444
# Unit test for function match
def test_match():
    assert match(Command('rm -rf a b ', '', '', 1))
    assert match(Command('rm a b', "rm: it is dangerous to operate recursively on '/'", '', 1))
    assert not match(Command('rm a b', "", '', 1))


# Generated at 2022-06-14 10:43:52.666782
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm / --no-preserve-root', '')) == 'rm / --no-preserve-root'

# Generated at 2022-06-14 10:44:01.069692
# Unit test for function match

# Generated at 2022-06-14 10:44:07.480657
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /',
            'rm: refusing to remove ‘/’ recursively without --no-preserve-root\n'))
    assert not match(Command('rm -rf /'))
    assert not match(Command('rm -rf /', 'whoops'))
    assert not match(Command('rm -rf /', stderr='whoops'))

# Generated at 2022-06-14 10:44:15.323487
# Unit test for function match
def test_match():
    command = Command('rm /', '')
    assert(not match(command))
    command = Command('rm -rf /', '')
    assert(match(command))
    command = Command('rm --no-preserve-root /', '')
    assert(not match(command))


# Generated at 2022-06-14 10:44:18.961541
# Unit test for function match
def test_match():
    command = Command('sudo rm /', "rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe")
    assert match(command) == (True and True)


# Generated at 2022-06-14 10:44:20.412349
# Unit test for function match
def test_match():
    assert match(Command(script = 'rm -rf /'))


# Generated at 2022-06-14 10:44:32.615823
# Unit test for function match

# Generated at 2022-06-14 10:44:38.934463
# Unit test for function match
def test_match():
    """ Test case for match() """
    # Test 1: `rm /`
    assert match(Command('rm /')) is True

    # Test 2: `rm / `
    assert match(Command('rm / ')) is True

    # Test 3: `rm -rf / `
    assert match(Command('rm -rf / ')) is True

    # Test 4: `rm -rf / `
    assert match(Command('rm -rf / ')) is True

    # Test 5: `rm -rf --no-preserve-root / `
    assert match(Command('rm -rf --no-preserve-root / ')) is False

    # Test 6: `rm -rf --no-preserve-root / `

# Generated at 2022-06-14 10:44:50.638438
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', '', '', 1, 'rm: refusing to remove ‘/’ recursively without --no-preserve-root'))
    assert match(Command('rm -rf /home/user/Desktop', '', '', 1, 'rm: refusing to remove ‘/’ recursively without --no-preserve-root'))
    assert not match(Command('rm -rf /home/user/Desktop', '', '', 1, 'rm: cannot remove '))
    assert not match(Command('rm -rf /home/user/Desktop', '', '', 0, 'rm: cannot remove '))
    assert not match(Command('rm -rf /home/user/Desktop', '', '', 0, ''))

# Generated at 2022-06-14 10:44:56.615935
# Unit test for function match
def test_match():
    assert match(u"rm /")
    assert not match(u"rm --no-preserve-root /")
    assert not match(u"rm / --no-preserve-root")
    assert not match(u"rm / -rf")
