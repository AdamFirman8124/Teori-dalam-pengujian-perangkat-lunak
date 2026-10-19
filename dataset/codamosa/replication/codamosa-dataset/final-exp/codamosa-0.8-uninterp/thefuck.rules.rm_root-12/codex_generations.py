

# Generated at 2022-06-14 10:36:05.249898
# Unit test for function match
def test_match():
    assert match(Command('rm /', ''))
    assert not match(Command('sudo rm /', 'rm: preserving permissions for ‘/’: Operation not permitted'))
    assert match(Command('rm /', 'rm: preserving permissions for ‘/’: Operation not permitted'))
    assert match(Command('rm -r /', 'rm: preserving permissions for ‘/’: Operation not permitted'))
    assert not match(Command('rm -r /', 'rm: cannot remove ‘/’: Permission denied'))


# Generated at 2022-06-14 10:36:13.937614
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', '', '/: it is dangerous to operate recursively on'))
    assert match(Command('rm / -rf', '', '/: it is dangerous to operate recursively on'))
    assert not match(Command('rm -rf /', '', ''))
    assert not match(Command('rm -rf / --no-preserve-root', '', '/: it is dangerous to operate recursively on'))


# Generated at 2022-06-14 10:36:17.393127
# Unit test for function match
def test_match():
    assert match(Command('rm -r /'))
    assert not match(Command('rm -r / --no-preserve-root'))


# Generated at 2022-06-14 10:36:24.097592
# Unit test for function match
def test_match():
    """
    Tests to see if return statement is correct
    """
    assert match(Command(script='rm -r /',
                 stderr=u'rm: cannot remove \'/\': Is a directory',
                 output=u'rm: cannot remove \'/\': Is a directory',
                 script_parts=['rm', '-r', '/']))



# Generated at 2022-06-14 10:36:28.876880
# Unit test for function get_new_command
def test_get_new_command():
    command = type('obj', (object,), {'script': 'rm -i *'})()
    assert get_new_command(command) == 'rm -i * --no-preserve-root'

# Generated at 2022-06-14 10:36:32.388408
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='rm -r /', stderr='rm: refusing to remove \'/\' recursively without --no-preserve-root')
    assert get_new_command(command) == 'rm -r / --no-preserve-root'


# Generated at 2022-06-14 10:36:43.402132
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', '', ''))
    assert match(Command('rm -rf ./', '', ''))
    assert match(Command('rm -rf /tmp/foo', '', ''))
    assert not match(Command('rm -rf --no-preserve-root /tmp/foo', '', ''))
    assert not match(Command('rm -rf /tmp/foo', '', 'rm: it is dangerous to operate recursively on ‘/’\n'))
    assert match(Command('rm -rf /tmp/foo', '', 'rm: it is dangerous to operate recursively on ‘/’\n'
                                                 '--no-preserve-root'))

# Generated at 2022-06-14 10:36:48.711388
# Unit test for function match
def test_match():
    command = Command(script = 'rm /',
                      stderr='rm: it is dangerous to operate recursively on' +
                             ' ‘/’\n' +
                             'rm: use --no-preserve-root to override this' +
                             ' failsafe')
    assert match(command)

    command = Command(script = 'rm --no-preserve-root /',
                      stderr='rm: it is dangerous to operate recursively on' +
                             ' ‘/’\n' +
                             'rm: use --no-preserve-root to override this' +
                             ' failsafe')
    assert not match(command)


# Generated at 2022-06-14 10:36:55.932645
# Unit test for function get_new_command
def test_get_new_command():
    command=Command(script='sudo rm /', stderr='rm: refusing to remove path /',
                    side_effect='rm: refusing to remove path /'
                   )
    assert get_new_command(command) == 'sudo rm / --no-preserve-root'

# Generated at 2022-06-14 10:36:58.668032
# Unit test for function get_new_command
def test_get_new_command():
    assert u'rm --no-preserve-root /' == get_new_command(Command('rm /'))

# Generated at 2022-06-14 10:37:04.437712
# Unit test for function match
def test_match():
    cmd = Command('rm -r /')
    assert match(cmd)
    cmd = Command('rm -r / --no-preserve-root')
    assert not match(cmd)


# Generated at 2022-06-14 10:37:10.699282
# Unit test for function match
def test_match():
    assert match(Command('rm /', '', '')) == True
    assert match(Command('rm /', '', '', '--no-preserve-root')) == False
    assert match(Command('rm /', '', '', '--no-preserve-root')) == False



# Generated at 2022-06-14 10:37:19.963270
# Unit test for function match
def test_match():
    commands_list = ["rm", "rm -rf", "rm -fR /tmp/folder",
                     "rm --help", "rm -fr --no-preserve-root /tmp/bak",
                     "rm -fr -d /tmp/bak", "rm -rf /tmp/bak/ --preserve-root",
                     "rm --preserve-root -rf /tmp/bak/"]
    custom_command = Command("rm -rf /",
                             "rm: it is dangerous to operate recursively on '/'").script
    assert any(match(custom_command) for command in commands_list)

# Generated at 2022-06-14 10:37:24.573134
# Unit test for function match
def test_match():
    command = Command('rm -r /', '', '/bin/rm: it is dangerous to operate recursively on '/'\nUse --no-preserve-root to override this failsafe')
    assert match(command)



# Generated at 2022-06-14 10:37:36.604884
# Unit test for function match
def test_match():
    # Check if rm is used on the root directory
    assert match(Command('rm /',
                script_parts=['rm', '/'], output='', stderr=''))
    assert match(Command('rm /',
                script_parts=['rm', '/'], output='', stderr=''))

    # Check if --no-preserve-root is there
    assert match(Command('rm /',
                script_parts=['rm', '/'], output='', stderr=''))

    # Check if --no-preserve-root is not there
    assert not match(Command(
            'rm /', script_parts=['rm', '/'],
            output='missing operand', stderr=''))

    # Check if removed is not on the root directory

# Generated at 2022-06-14 10:37:46.713078
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', '/bin/rm: cannot remove \'/\': Is a directory'))
    assert not match(Command('rm -rf /', ''))
    assert not match(Command('rm -rf /', 'rm: cannot remove \'/\': Is a directory'))
    assert not match(Command('rm -rf /', '/bin/rm: cannot remove \'/\': Is a directory'))
    assert not match(Command('rm -rf /', '/bin/rm: cannot remove \'/\': Is a directory'))
    assert not match(Command('rm -rf /', '/bin/rm: cannot remove \'/\': Is a directory'))


# Generated at 2022-06-14 10:37:50.587953
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='rm -rf /', output='rm: it is dangerous to operate recursively on '/'')
    assert get_new_command(command) == 'rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:38:02.505596
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', ''))
    assert match(Command('sudo rm -rf /', ''))
    assert match(Command('rm -rf /', ''))
    assert match(Command('sudo rm -rf /', 'rm: cannot remove `/\': Is a directory'))
    assert match(Command('rm -rf /', 'rm: cannot remove `/\': Is a directory'))
    assert not match(Command('rm -rf /home/foo', 'usage'))
    assert not match(Command('rm -rf /home/foo', 'rm: cannot remove `/\': Is a directory'))


# Generated at 2022-06-14 10:38:08.618063
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm /', 'rm: it is dangerous to operate recursively on ‘/’\n'
                                           'rm: use --no-preserve-root to override this failsafe')) == 'rm / --no-preserve-root'

# Generated at 2022-06-14 10:38:17.514125
# Unit test for function match
def test_match():
    assert match(Command('rm -f /', ''))
    assert match(Command('rm -f /', '', ''))
    assert not match(Command('rm -f /', '', ''))

# Generated at 2022-06-14 10:38:30.530243
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm /', '', '/bin/rm: it is dangerous to operate recursively on ‘/’\nUse --no-preserve-root to override this failsafe\n')
    assert get_new_command(command) == 'rm / --no-preserve-root'

# Generated at 2022-06-14 10:38:33.377246
# Unit test for function match
def test_match():
    support.run_command = MagicMock(return_value=Command(script='foobar',
                                                         stdout='bar', stderr='foo',
                                                         env={'LANG': 'C', 'LC_ALL': 'C'},
                                                         not_needed_retcode=0,
                                                         script_parts=['rm', '/'],))
    assert match(Command('foobar', stderr='foo'))

# Generated at 2022-06-14 10:38:38.528093
# Unit test for function match
def test_match():
    # pylint: disable=E1103
    assert match(Command('rm -rf /', '', 'rm: descend into write-protected directory ‘/’? '))
    assert match(Command('rm -rf /', '', 'rm: remove write-protected directory ‘/’?'))

# Generated at 2022-06-14 10:38:44.118732
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(
        script="rm -rf /",
        stdout="rm: it is dangerous to operate recursively on '/'\n"
               "Use --no-preserve-root to override this failsafe",
        stderr="")) == "rm -rf --no-preserve-root /"



# Generated at 2022-06-14 10:38:48.204804
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm /')) == 'rm --no-preserve-root /'
    assert get_new_command(Command('sudo rm /')) == 'sudo rm --no-preserve-root /'

# Generated at 2022-06-14 10:38:50.645323
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /', ''))
    assert not match(Command('ls', ''))

# Generated at 2022-06-14 10:38:53.335268
# Unit test for function match
def test_match():
    command = Command("rm -r *", "", "", output, "")
    assert match(command) == True


# Generated at 2022-06-14 10:38:56.813872
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('rm / -r', 'ERROR: remove write-protected regular empty file "/" ?', '', '', '', '', '')) == 'rm / -r --no-preserve-root')

# Generated at 2022-06-14 10:39:03.361624
# Unit test for function match
def test_match():
    command = Command('rm -rf /', '/bin/rm: cannot remove \'/\': Permission denied', '', 1)
    assert match(command) == True
    command = Command('rm -rf /home/me/Desktop', '/bin/rm: cannot remove \'/\': Permission denied', '', 1)
    assert match(command) == False


# Generated at 2022-06-14 10:39:06.100868
# Unit test for function match
def test_match():
    command = Command('rm /')
    assert match(command)
    assert_not_equal(None, match(command))


# Generated at 2022-06-14 10:39:15.702742
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("rm -rf /")) == "rm -rf / --no-preserve-root"

# Generated at 2022-06-14 10:39:28.798271
# Unit test for function match
def test_match():
    assert match(Command('rm -r /'))
    assert match(Command('sudo rm -r /'))
    assert match(Command('sudo rm -r /', stderr='rm: can\'t remove \'/\': Permission denied'))
    assert match(Command('sudo rm -rf dir1 dir2 dir3', output='rm: cannot remove ‘dir1/dir2’: Permission denied\nrm: cannot remove ‘dir1/dir2/dir3’: Permission denied'))
    assert match(Command('sudo rm -rf dir1', output='rm: cannot remove ‘dir1’: Permission denied'))
    assert not match(Command('rm -rf dir1', output='rm: cannot remove ‘dir1’: Permission denied'))

# Generated at 2022-06-14 10:39:34.325052
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm /') == 'rm / --no-preserve-root'
    assert get_new_command('rm -r /') == 'rm -r / --no-preserve-root'
    assert get_new_command('rm -rf /') == 'rm -rf / --no-preserve-root'


# Generated at 2022-06-14 10:39:37.632478
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm /')) == 'rm --no-preserve-root /'



# Generated at 2022-06-14 10:39:43.367445
# Unit test for function match
def test_match():
    # Test whether function match works with certain arguments
    from thefuck.rules.rm_f_preserve_root import match
    from thefuck.types import Command
    assert match(Command('rm -f /',
                         'rm: preserve root directory (/), use --no-preserve-root'))
    assert not match(Command('rm -f /',''))


# Generated at 2022-06-14 10:39:46.869492
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf /', '')
    assert get_new_command(command) == 'rm -rf --no-preserve-root /'


# Generated at 2022-06-14 10:39:51.942566
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’ (same as ‘rm -r /’)\nrm: use --no-preserve-root to override this failsafe')
    assert get_new_command(command) == 'rm -rf --no-preserve-root /'

# Generated at 2022-06-14 10:39:56.836289
# Unit test for function match
def test_match():
    assert match(Command(script='sudo rm', output='rm: it is dangerous to operate recursively on '/'', stderr=''))
    assert not match(Command(script='sudo rm --no-preserve-root', output='rm: it is dangerous to operate recursively on '/'', stderr=''))

# Generated at 2022-06-14 10:40:01.214024
# Unit test for function match
def test_match():
    assert match(Command('rm /'))
    assert not match(Command('rm -rf /'))
    assert not match(Command('rm /', '', '', '', '--no-preserve-root'))
    asser

# Generated at 2022-06-14 10:40:06.986885
# Unit test for function match
def test_match():
    command = Command('rm -rf /', 'rm: cannot remove ‘/’: Permission denied')
    assert match(command)

# Generated at 2022-06-14 10:40:17.435869
# Unit test for function match
def test_match():
    assert match(Command('rm /', ''))
    assert not match(Command('rm /', '', ''))


# Generated at 2022-06-14 10:40:20.086941
# Unit test for function get_new_command
def test_get_new_command():
    assert u'rm --no-preserve-root' == get_new_command(u'rm')

# Generated at 2022-06-14 10:40:25.090324
# Unit test for function match
def test_match():
    assert match(command=Command('rm -rf /', None, u'rm: cannot remove \'/\': Is a directory')), 'Should be enabled'
    assert not match(command=Command('rm -rf /', None, u'rm: cannot remove \'/\': Is a directory')), 'Should be disabled'

# Generated at 2022-06-14 10:40:34.831845
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('rm -rf / --no-preserve-root', '')) == 'rm -rf / --no-preserve-root'
    assert get_new_command(Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’'
                                '\nrm: use --no-preserve-root to override this failsafe')) == 'rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:40:37.420639
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm -rf /')
    assert get_new_command(command) == 'rm --no-preserve-root -rf /'

# Generated at 2022-06-14 10:40:40.874425
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm /', '')
    assert get_new_command(command) == 'rm / --no-preserve-root'



# Generated at 2022-06-14 10:40:44.438820
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('rm /', output='illegal option -- -\n')) == 'sudo rm --no-preserve-root'


# Generated at 2022-06-14 10:40:55.209288
# Unit test for function get_new_command
def test_get_new_command():
    ''' Unit test for function get_new_command.
    '''
    # Case 1
    command = Command(script='sudo rm -R /',
                      stdout='rm: it is dangerous to operate recursively on '/
                             'as root\nrm: use --no-preserve-root to override this'
                             'deterrent\n')
    new_command = get_new_command(command)
    assert new_command == u'sudo rm -R --no-preserve-root /'

    # Case 2
    command = Command(script='sudo rm -R /',
                      stdout='rm: it is dangerous to operate recursively on '/
                             'as root\nrm: use --no-preserve-root to override this'
                             'deterrent\n')
    new_command = get_new_

# Generated at 2022-06-14 10:41:06.122457
# Unit test for function match
def test_match():
    assert match(Command('rm /', 'rm: cannot remove /: Permission denied'
                         '\nrmdir: /: Directory not empty\n'))
    assert not match(Command('rm /', 'rm: cannot remove /: Permission denied'
                         '\nrmdir: /: Directory not empty\n',
                          'rm: cannot remove /: Permission denied\n'
                          'rmdir: /: Directory not empty\n'))

# Generated at 2022-06-14 10:41:08.658971
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm / -rf', '')
    assert(get_new_command(command)=='rm / -rf --no-preserve-root')

# Generated at 2022-06-14 10:41:31.304430
# Unit test for function match
def test_match():
    # This will test if command.script_parts exists
    command = Command('rm -rf /')
    assert match(command)
    # This will test if the command has rm and /
    command = Command('rmdir /')
    assert not match(command)
    # This will test if the command has --no-preserve-root
    command = Command('rm -rf --no-preserve-root /')
    assert not match(command)
    # This will test if the output of command contains --no-preserve-root
    command = Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’')
    assert not match(command)
    # This will test if the command is sudo rm
    command = Command('sudo rm -rf /')
    assert match(command)
    # This will test if

# Generated at 2022-06-14 10:41:33.832216
# Unit test for function get_new_command

# Generated at 2022-06-14 10:41:47.344529
# Unit test for function match
def test_match():
    assert match(Command('rm -r /', stderr='rm: it is dangerous to operate recursively on `/\'\nrm: use --no-preserve-root to override this failsafe'))
    assert match(Command('rm /', stderr='rm: it is dangerous to operate recursively on `/\'\nrm: use --no-preserve-root to override this failsafe'))
    assert match(Command('rm -rf /', stderr='rm: it is dangerous to operate recursively on `/\'\nrm: use --no-preserve-root to override this failsafe'))
    assert not match(Command('rm -rf / ', stderr='rm: it is dangerous to operate recursively on `/\'\nrm: use --no-preserve-root to override this failsafe'))
    assert not match

# Generated at 2022-06-14 10:41:54.437764
# Unit test for function match
def test_match():
    assert match(Command('a / --no-preserve-root blah blah blah', ''))
    assert not match(Command('a -rf /', ''))
    assert not match(Command('a / --no-preserve-root', ''))
    assert not match(Command('a -rf / --no-preserve-root', 'REALLY WANT TO REMOVE /? y'))
    assert match(Command('a /', ''))


# Generated at 2022-06-14 10:41:58.769769
# Unit test for function get_new_command
def test_get_new_command():
    assert not get_new_command(u'rm -rf /').script.startswith(u'sudo')
    assert get_new_command(u'sudo rm -rf /').script.startswith(u'sudo')

# Generated at 2022-06-14 10:42:07.447606
# Unit test for function get_new_command
def test_get_new_command():
    output = 'rm: refusing to remove ‘/’ recursively without --no-preserve-root'
    commandToTest = Command(script='rm -rf /home/gondr', output=output)
    commandExpected = 'rm -rf --no-preserve-root /home/gondr'
    get_new_command(commandToTest) == commandExpected
# Must return false

# Generated at 2022-06-14 10:42:11.426420
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo rm -rf /', '', 'sudo: rm: cannot remove ‘/’: Operation not permitted\n')
    assert get_new_command(command) == 'sudo rm -rf / --no-preserve-root'

# Generated at 2022-06-14 10:42:15.129756
# Unit test for function match
def test_match():
    assert match(Command('sudo rm -rf /', '', '', 1))
    assert not match(Command('rm -rf /', '', '', 1))


# Generated at 2022-06-14 10:42:22.580981
# Unit test for function match
def test_match():
    command = Command('rm /',
                      'rm: it is dangerous to operate recursively on ‘/’\n'
                      'rm: use --no-preserve-root to override this failsafe')
    assert match(command)

    command = Command('rm /',
                      'rm: it is dangerous to operate recursively on ‘/’\n')
    assert not match(command)

    command = Command('rm --no-preserve-root /',
                      'rm: it is dangerous to operate recursively on ‘/’\n'
                      'rm: use --no-preserve-root to override this failsafe')
    assert not match(command)


# Generated at 2022-06-14 10:42:27.878350
# Unit test for function get_new_command
def test_get_new_command():
    result = get_new_command(Command(script="rm -rf /home/ubuntu/toto",
                                     output="rm: refusing to remove '/' recursively without --no-preserve-root"))
    assert result == "rm -rf --no-preserve-root /home/ubuntu/toto"

# Generated at 2022-06-14 10:43:03.699862
# Unit test for function match
def test_match():
    print(match(Command('rm -rf /', '', 'rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe')))
    print(not match(Command('rm -rf /', '', 'rm: it is dangerous to operate recursively on /home/bob')))

# Generated at 2022-06-14 10:43:05.819592
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('rm /etc') == 'rm --no-preserve-root /etc'

# Generated at 2022-06-14 10:43:10.354936
# Unit test for function get_new_command

# Generated at 2022-06-14 10:43:16.136339
# Unit test for function match
def test_match():
    assert match(Command('rm --no-preserve-root /'))
    assert match(Command('rm /'))
    assert match(Command('sudo rm --no-preserve-root /'))
    assert not match(Command('rm --no-preserve-root --help'))
    assert not match(Command('rm --no-preserve-root /hello'))
    assert not match(Command('rm --no-preserve-root --help /'))
    assert not match(Command('rm --no-preserve-root foo/'))
    assert not match(Command('rm --no-preserve-root --help /'))


# Generated at 2022-06-14 10:43:22.291680
# Unit test for function match
def test_match():
    assert match(Command('rm -rf /',
                    script_parts=['rm', '-rf', '/'], output='/'))
    assert not match(Command('rm -rf /',
                    script_parts=['rm', '-rf', '/'], output='output'))
    assert not match(Command('rm -rf /',
                    script_parts=['rm', '-rf', '/'], output='/'))
    assert not match(Command('rm -rf /',
                    script_parts=['rm', '-rf', '/'], output='/'))


# Generated at 2022-06-14 10:43:25.505890
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command("rm /")) == "rm --no-preserve-root /"
    assert(get_new_command("rm --recursive /")) == "rm --recursive --no-preserve-root /"
    assert(get_new_command("rm --no-preserve-root /")) == "rm --no-preserve-root /"


# Generated at 2022-06-14 10:43:29.334782
# Unit test for function match

# Generated at 2022-06-14 10:43:32.620405
# Unit test for function get_new_command
def test_get_new_command():
    command = 'rm -r /'
    new_command = get_new_command(command)
    assert new_command == command + ' --no-preserve-root'


# Generated at 2022-06-14 10:43:44.168420
# Unit test for function match
def test_match():
    assert match(command=Command(script='rm test.txt',
                                 stdout='rm: it is dangerous to operate recursively on ‘/’\n' +
                                        'rm: use --no-preserve-root to override this failsafe',
                                 stderr='',
                                 script_parts=['rm', 'test.txt'],
                                 environment={})) is True
    assert match(command=Command(script='rm test.txt',
                                 stdout='rm: it is dangerous to operate recursively on ‘/’\n' +
                                        'rm: use --no-preserve-root to override this failsafe',
                                 stderr='',
                                 script_parts=['rm', 'test.txt'],
                                 environment={})) is True

# Generated at 2022-06-14 10:43:52.731890
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('rm -rf /',
                                    ''))
            == 'rm --no-preserve-root -rf /')
    assert (get_new_command(Command('sudo rm -rf /',
                                    '',
                                    '/bin/rm'))
            == 'sudo rm --no-preserve-root -rf /')

# Generated at 2022-06-14 10:44:59.577685
# Unit test for function match
def test_match():
    command = Command('rm -rf /', '')
    assert match(command)
    command = Command('rm -rf ~/', '')
    assert not match(command)
    command = Command('rm -rf /', '')
    assert not match(command)



# Generated at 2022-06-14 10:45:03.321263
# Unit test for function match
def test_match():
    assert match(Command('rm -r /',
                         'rm: it is dangerous to operate recursively on \'/\'\n'
                         'rm: use --no-preserve-root to override this failsafe\n'))


# Generated at 2022-06-14 10:45:10.005412
# Unit test for function match
def test_match():
    # unit tests for function match
    script = Command('rm -rf /')
    assert match(script)
    script_parts = Command('ls').script_parts
    assert not match(script_parts)
    script_parts = Command('rm').script_parts
    assert not match(script_parts)
    script_parts = Command('rm -rf /').script_parts
    assert match(script_parts)


# Generated at 2022-06-14 10:45:12.421271
# Unit test for function match
def test_match():
    command = Command('rm -rf /')
    assert match(command)
    assert not match(Command('rm'))

# Generated at 2022-06-14 10:45:16.852675
# Unit test for function match

# Generated at 2022-06-14 10:45:19.427988
# Unit test for function match
def test_match():
    assert match(Command(script='rm /'))
    assert not match(Command(script='rm / --no-preserve-root'))
    assert not match(Command(script='rm'))

# Generated at 2022-06-14 10:45:24.207196
# Unit test for function match
def test_match():
    cmd = Command("rm -rf /", "rm: it is dangerous to operate recursively on `/'\nrm: use --no-preserve-root to override this failsafe\n")
    assert match(cmd)


# Generated at 2022-06-14 10:45:34.236269
# Unit test for function match
def test_match():
    from thefuck.rules.rm_rf_root import match
    command = Command('rm -rf /', 'rm: it is dangerous to operate recursively on ‘/’\n'
                              'rm: use --no-preserve-root to override this failsafe')
    assert match(command)

    command = Command('rm -rf --no-preserve-root /', 'rm: cannot remove ‘/’: Permission denied')
    assert not match(command)

    command = Command('rm -rf /', 'rm: cannot remove ‘/’: Permission denied')
    assert not match(command)

# Generated at 2022-06-14 10:45:44.694777
# Unit test for function match
def test_match():
    assert match(Command('rm . -rf',
                         'rm: refusing to remove . or .. directory: skipping "/"\n'
                         'Did you mean to run rm with --no-preserve-root?\n',
                         ''))
    assert not match(Command('rm . -rf',
                             'rm: refusing to remove . or .. directory: skipping "/"\n'
                             'Did you mean to run rm with --no-preserve-root?\n',
                             '',
                             'roo'))
    assert not match(Command('rm --no-preserve-root . -rf',
                             'rm: refusing to remove . or .. directory: skipping "/"\n'
                             'Did you mean to run rm with --no-preserve-root?\n',
                             ''))


# Generated at 2022-06-14 10:45:46.562325
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('rm /')
    assert get_new_command(command) == 'rm --no-preserve-root /'
