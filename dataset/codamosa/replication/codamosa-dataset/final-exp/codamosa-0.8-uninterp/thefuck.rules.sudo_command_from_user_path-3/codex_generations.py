

# Generated at 2022-06-14 10:46:31.679426
# Unit test for function match
def test_match():
    command = Command("sudo ifconfig", "sudo: ifconfig: command not found\n")
    assert match(command)
    command = Command("sudo ifconfig", "")
    assert not match(command)



# Generated at 2022-06-14 10:46:34.784765
# Unit test for function match
def test_match():
    assert match(Command('dry-run sudo su',
                         'dry-run: sudo: command not found'))
    assert not match(Command('sudo', ''))


# Generated at 2022-06-14 10:46:36.393684
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('sudo ls').script == 'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:46:40.084157
# Unit test for function get_new_command
def test_get_new_command():
    """
    Check if get_new_command() works correctly
    """
    command_output = Command('sudo ls', '')
    assert get_new_command(command_output) == 'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:46:43.706161
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script = 'sudo -u test1 ls /tmp')) == \
           'env "PATH=$PATH" sudo -u test1 ls /tmp'

# Generated at 2022-06-14 10:46:47.010993
# Unit test for function match
def test_match():
    assert match(Command('sudo pwd', 'sudo: pwd: command not found'))
    assert not match(Command('sudo pwd', 'sudo: pwd: permission denied'))


# Generated at 2022-06-14 10:46:53.209470
# Unit test for function match
def test_match():
    assert match(Command("sudo apt update", "sudo: apt: command not found"))
    assert not match(Command("sudo apt update", "sudo: apt-get: command not found"))
    assert not match(Command("sudo apt update", "sudo: apt update"))
    assert not match(Command("sudo apt update", "sudo: apt(command not found)"))


# Generated at 2022-06-14 10:46:57.487595
# Unit test for function match
def test_match():
    assert (match(Command('sudo apt-get update', '', "sudo: apt-get: command not found\n"))
            == which('apt-get'))
    assert not match(Command('sudo apt-get update', ''))


# Generated at 2022-06-14 10:47:01.314119
# Unit test for function match
def test_match():
    result = match("sudo smartctl --test=long --scan")
    assert result == True
    output = "sudo: smartctl: command not found"
    result = match(output)
    assert result == True


# Generated at 2022-06-14 10:47:03.527615
# Unit test for function match
def test_match():
    assert match(Command('sudo abc',
                         "sudo: abc: command not found"))



# Generated at 2022-06-14 10:47:10.610591
# Unit test for function match
def test_match():
    # test no match
    assert not match(Command('sudo ls'))
    # test match
    assert match(Command('sudo ls not_found_command'))


# Generated at 2022-06-14 10:47:17.385391
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.shells import Shell

    def _get_new_command(script, debug=False):
        command = Command(script, '', '')
        new_command = get_new_command(command)
        return Shell(debug=debug,
                     require_confirmation=lambda cmd: False).and_(new_command)

    assert _get_new_command("sudo hello") == "env 'PATH=$PATH' hello"

# Generated at 2022-06-14 10:47:21.034765
# Unit test for function match
def test_match():
    assert match(Command('sudo gedit', 'sudo: gedit: command not found', ''))
    assert match(Command('sudo gedit', '', '')) is None

# Generated at 2022-06-14 10:47:24.488436
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo su', 'sudo: su: command not found')
    assert get_new_command(command) == 'env "PATH=$PATH" sudo su'

# Generated at 2022-06-14 10:47:26.551135
# Unit test for function match
def test_match():
    """`sudo x` should return True"""
    assert match(Command('sudo d', ''))


# Generated at 2022-06-14 10:47:31.029842
# Unit test for function match
def test_match():
    assert not match(Command('', ''))
    assert not match(Command('sudo pwd', ''))
    assert match(Command('sudo ls', 'sudo: ls: command not found'))



# Generated at 2022-06-14 10:47:37.219537
# Unit test for function match
def test_match():
    # When the output from "sudo" contains "command not found"
    assert match(Command('sudo ls',
                         'sudo: ls: command not found'))

    # When the output from "sudo" does not contain "command not found"
    assert not match(Command('sudo ls',
                         'ls: command not found'))



# Generated at 2022-06-14 10:47:40.045312
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', 'sudo: ls: command not found'))
    assert not match(Command('sudo ls', ''))


# Generated at 2022-06-14 10:47:46.096932
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command(script='sudo echo',
                                   output="sudo: echo: command not found")) == \
        "env 'PATH=$PATH' echo"
    assert get_new_command(Command(script='sudo blah',
                                   output="sudo: blah: command not found")) == \
        "env 'PATH=$PATH' blah"

# Generated at 2022-06-14 10:47:49.637627
# Unit test for function match
def test_match():
    command = re.compile(r'.*(sudo.*)|(sudo.*)')
    output = 'sudo: cd: command not found'
    assert match(command, output)



# Generated at 2022-06-14 10:47:59.812457
# Unit test for function match
def test_match():
    try:
        assert(match(Command(script="sudo test_cmd", output="sudo: test_cmd: command not found")) == None)
        assert(match(Command(script="sudo test_cmd", output="sudo: test_cmd: command found")) == None)
        assert(match(Command(script="sudo test_cmd", output="test_cmd: command not found")) == None)
        assert(match(Command(script="sudo test_cmd", output="test_cmd: command found")) == None)
    except:
        print("test_match - Unit test failed!")


# Generated at 2022-06-14 10:48:04.420235
# Unit test for function match
def test_match():
    command = Command('sudo vim', output='sudo: vim: command not found')
    assert match(command)
    command = Command('sudo vim', output='kalamazoococo')
    assert not match(command)


# Generated at 2022-06-14 10:48:06.881811
# Unit test for function match
def test_match():
    assert not match(Command(script='sudo ls bla', output='bla'))
    assert match(Command(script='sudo ls bla',
                         output='sudo: ls: command not found'))



# Generated at 2022-06-14 10:48:10.990272
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    current_command = Command('sudo echo hello', 'sudo: echo: command not found')
    assert get_new_command(current_command) \
        == u'env "PATH=$PATH" echo hello'

# Generated at 2022-06-14 10:48:18.910898
# Unit test for function match
def test_match():
    """
    Checks if the function match returns true for the given input
    """
    assert match(Command('sudo apt-get update', 'sudo apt-get update\nsudo: apt-get: command not found'))
    assert match(Command('sudo apt-get update', 'sudo apt-get update\nsudo: apt-get: command not found\nsudo: 3 update: command not found'))
    assert not match(Command('sudo apt-get update', 'sudo apt-get update'))


# Generated at 2022-06-14 10:48:22.736511
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ls', 'sudo: ls: command not found')
    assert get_new_command(command) == 'env "PATH=$PATH" sudo ls'

# Generated at 2022-06-14 10:48:26.613824
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='sudo blabla', output="sudo: blabla: command not found")
    assert get_new_command(command).script == u'env "PATH=$PATH" blabla'

# Generated at 2022-06-14 10:48:32.712508
# Unit test for function match
def test_match():
    result = match(Command('sudo cmd --enable-flow-control',
                           'sudo: cmd: command not found'))
    assert result.which('cmd')

    assert match(Command('sudo blah blah blah', '')) is None
    assert match(Command('sudo blah blah blah', 'sudo: blah: command not found')) is None
    assert match(Command('sudo blah blah blah', 'sudo: cmd: command not found')) is None

test_match.match = match


# Generated at 2022-06-14 10:48:35.711340
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo ls', 'sudo: ls: command not found'))\
        == 'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:48:39.285511
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get',
                         stderr='sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get',
                         stderr='sudo: apt-get: command found'))


# Generated at 2022-06-14 10:48:46.715308
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get upgade', '')) == False
    assert match(Command('sudo apt-get upgade', 'sudo: apt-get: command not found')) == True


# Generated at 2022-06-14 10:48:48.440166
# Unit test for function match
def test_match():
    assert match(Command(script=' sudo git', stderr='sudo: git: command not found'))



# Generated at 2022-06-14 10:49:01.574709
# Unit test for function get_new_command
def test_get_new_command():
    # command with one parameter
    assert get_new_command(Command("sudo iptables -U","sudo: iptables: command not found",1)) == "env 'PATH=$PATH' iptables -U"
    # command with multiple parameters
    assert get_new_command(Command("sudo iptables -L -U","sudo: iptables: command not found",1)) == "env 'PATH=$PATH' iptables -L -U"
    # command with sudo options
    assert get_new_command(Command("sudo -S iptables -L -U","sudo: iptables: command not found",1)) == "sudo -S env 'PATH=$PATH' iptables -L -U"
    # command with multiple sudo options

# Generated at 2022-06-14 10:49:03.270132
# Unit test for function match
def test_match():
    assert match(Command(script='sudo apt', output='sudo: apt: command not found'))


# Generated at 2022-06-14 10:49:07.775356
# Unit test for function match
def test_match():
    assert match(Command('sudo blah blah blah', output='sudo: blah: command not found'))
    assert which('blah')
    assert not match(Command('sudo doodoo', output='sudo: doodoo: command not found'))


# Generated at 2022-06-14 10:49:14.311077
# Unit test for function get_new_command
def test_get_new_command():
    command_name = 'blabla'
    script = 'sudo {}'.format(command_name)
    command = Command(script, 'sudo: {}: command not found'.format(command_name), None)
    new_command = get_new_command(command)
    assert new_command == 'env "PATH=$PATH" blabla'

# Generated at 2022-06-14 10:49:18.173771
# Unit test for function get_new_command
def test_get_new_command():
    output_command = Command('sudo echo', '', 'sudo: echo: command not found\n')
    assert get_new_command(output_command).script == 'sudo env "PATH=$PATH" echo'

# Generated at 2022-06-14 10:49:21.416147
# Unit test for function match
def test_match():
    script = Script('sudo command not found')
    script.output = 'sudo: command: command not found'
    assert match(script)



# Generated at 2022-06-14 10:49:24.615869
# Unit test for function match
def test_match():
    assert _get_command_name("sudo: dpkg-reconfigure: command not found") == 'dpkg-reconfigure'


# Generated at 2022-06-14 10:49:29.763292
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script = u'sudo echo foo'
    output = u'sudo: echo: command not found'
    command = Command(script=script, output=output)
    get_new_command(command) == u'env "PATH=$PATH" echo foo'

# Generated at 2022-06-14 10:49:36.460202
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo vi',
                      "/usr/bin/sudo: vi: command not found", 0, "")
    test_command = "env \"PATH=$PATH\" vi"

    assert get_new_command(command) == test_command


priority = 100

# Generated at 2022-06-14 10:49:40.015568
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', ''))
    assert match(Command('sudo ls', 'sudo: ls: command not found'))
    assert not match(Command('sudo ls', 'sudo: ls: command found'))
    assert not match(Command('ls', 'sudo: ls: command not found'))


# Generated at 2022-06-14 10:49:43.258334
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo apt-get install vim', output='sudo: apt-get: command not found')) == 'env "PATH=$PATH" apt-get install vim'

# Generated at 2022-06-14 10:49:45.007914
# Unit test for function match
def test_match():
    assert match('sudo mv bar foo')


# Generated at 2022-06-14 10:49:46.849412
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', ''))


# Generated at 2022-06-14 10:49:53.543968
# Unit test for function match
def test_match():
    assert match(Command('sudo apm -v', 'sudo: apm: command not found',
                         '', 123))
    assert match(Command('sudo aptitude', 'sudo: aptitude: command not found',
                         '', 123))
    # sudo: add-apt-repository: command not found
    assert match(Command('sudo add-apt-repository ppa:danzilio/ppa', 'sudo: add-apt-repository: command not found', '', 123))

# Generated at 2022-06-14 10:49:56.610152
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get update',
                         'sudo: apt-get: command not found',
                         '', 1))



# Generated at 2022-06-14 10:50:00.453916
# Unit test for function match
def test_match():
    assert which('ls')
    assert match(Command('ls', '', 'sudo: ls: command not found'))
    assert not match(Command('ls', '', ''))



# Generated at 2022-06-14 10:50:04.223357
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    command = Command('sudo ls', 'sudo: ls: command not found\nsudo: sudo: command not found', '', '')
    assert get_new_command(command) == 'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:50:06.316583
# Unit test for function match
def test_match():
    assert match(Command('sudo ka', ''))
    assert not match(Command('sudo k', ''))

# Generated at 2022-06-14 10:50:16.791574
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo clear', 'sudo: clear: command not found'))\
        == u"env 'PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin' clear"

# Generated at 2022-06-14 10:50:25.331830
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_env_path import _get_command_name, get_new_command
    from thefuck.types import Command
    import os
    import shutil
    
    cwd = os.getcwd()
    if os.path.isdir(cwd+'/testdir') is False:
        os.mkdir('testdir')

   # If target file doesn`t exist
    if os.path.isfile(cwd+'/testdir/pathtest') is False:
        with open(cwd+'/testdir/pathtest', mode='w') as f:
            f.write('Hello World')

    command = Command('sudo pathtest', 'sudo: pathtest: command not found\n')
    assert _get_command_name(command) == 'pathtest'

# Generated at 2022-06-14 10:50:26.630870
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get install vim'))
    assert not match(Command('sudo vim'))

# Generated at 2022-06-14 10:50:36.649747
# Unit test for function match
def test_match():
    assert not match(Command('sudo apt-get install'))
    assert not match(Command('sudo apt-get install nope', '', '', 1, ''))
    assert match(Command('sudo apt-get install nope',
                         'sudo: apt-get: command not found', '', 1, ''))
    assert match(Command('sudo apt-get install nope',
                         'sudo: apt-get: command not found', '', 1, ''))
    assert match(Command('sudo apt-get install nope',
                         'sudo: apt-get: command not found', '', 1, ''))


# Generated at 2022-06-14 10:50:41.189214
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', 'sudo: ls: command not found'))
    assert not match(Command('sudo ls', ''))
    assert not match(Command('sudo ls', 'ls: command not found'))
    assert not match(Command('sudo ls', 'sudo: ls: command not found'))


# Generated at 2022-06-14 10:50:43.144452
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck import shells
    script = 'sudo foo'
    output = "sudo: foo: command not found"


# Generated at 2022-06-14 10:50:52.001712
# Unit test for function match
def test_match():
    # Unit test 1
    output = "sudo: firefox: command not found"
    res = match(Command(script=" ", output=output))
    assert res is not None
    assert res == output

    # Unit test 2
    assert match(Command(script=" ", output="")) is None

    # Unit test 3
    output = "sudo: fire: command not found"
    res = match(Command(script=" ", output=output))
    assert res is None
    assert res != output



# Generated at 2022-06-14 10:50:57.638852
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('sudo echo "hi"', "sudo: echo: command not found\n", "")) == \
        u'env "PATH=$PATH" echo "hi"'
    assert get_new_command(Command('sudo echo \'hi\'', "sudo: echo: command not found\n", "")) == \
        u'env "PATH=$PATH" echo \'hi\''

# Generated at 2022-06-14 10:50:59.648068
# Unit test for function match
def test_match():
    assert match(Command('sudo command not found'))
    assert not match(Command('sudo env'))



# Generated at 2022-06-14 10:51:01.788583
# Unit test for function match
def test_match():
    assert match(Command('sudo abc', 'sudo: abc: command not found')) is not None


# Generated at 2022-06-14 10:51:18.709353
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get update', 'sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get update', 'update'))



# Generated at 2022-06-14 10:51:20.740974
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(u'sudo vi') == u'env "PATH=$PATH" vi'

# Generated at 2022-06-14 10:51:22.880486
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ls -a', 'sudo: ls: command not found')
    assert get_new_command(command) == 'env "PATH=$PATH" ls -a'

# Generated at 2022-06-14 10:51:25.211056
# Unit test for function match
def test_match():
    command = Command('sudo abc -h', 'sudo: abc: command not found')
    assert match(command)
    assert not match(Command('ls abc -h'))


# Generated at 2022-06-14 10:51:28.141173
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo tessetact', 'sudo: tessetact: command not found\n')
    assert get_new_command(command) == "env \"PATH=$PATH\" tessetact"

# Generated at 2022-06-14 10:51:32.311445
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(
        Command('sudo rm /home/moo',
                error='sudo: rm: command not found')) == 'env "PATH=$PATH" rm /home/moo'

# Generated at 2022-06-14 10:51:35.045102
# Unit test for function match
def test_match():
    assert match(Command('sudo lsdd'))

    assert match(Command('sudo apt-get'))
    assert not match(Command('sudo apt-get', ''))


# Generated at 2022-06-14 10:51:44.193113
# Unit test for function match
def test_match():
    assert match(Command('sudo -- foo', 'sudo: --: command not found'))
    assert match(Command('sudo -a foo', 'sudo: -a: command not found'))
    assert match(Command('sudo -abc foo', 'sudo: -abc: command not found'))
    assert not match(Command('sudo foo', 'sudo: foo: command not found'))
    assert not match(Command('sudo ls', 'sudo: foo: command not found'))


# Generated at 2022-06-14 10:51:47.115602
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo foo', 'sudo: foo: command not found')) \
        == "env 'PATH=$PATH' foo"

# Generated at 2022-06-14 10:51:51.103245
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("sudo ls -a", "sudo: ls: command not found", "", 1, "")).script == u'sudo env "PATH=$PATH" ls -a'
    assert get_new_command(Command("sudo ls", "sudo: ls: command not found", "", 1, "")).script == u'sudo env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:52:24.856502
# Unit test for function match
def test_match():
    assert match(Command('sudo vim not_exisiting', 'sudo: vim: command not found\r\r', '', '', ''))
    assert not match(Command('sudo gedit not_exisiting', 'sudo: gedit: command not found', '', '', ''))

# Generated at 2022-06-14 10:52:26.345106
# Unit test for function match
def test_match():
    assert match(Command('sudo apt install git', ''))
    assert not match(Command('sudo apt-get install git', ''))


# Generated at 2022-06-14 10:52:30.296309
# Unit test for function match
def test_match():
    """
        The test case for match
    """
    assert match(Command(script="""sudo: command not found""", output="""sudo: command not found""", stderr="""sudo: command not found"""))


# Generated at 2022-06-14 10:52:34.045856
# Unit test for function match
def test_match():
    assert match(Command('sudo abc', 'sudo: abc: command not found'))
    assert not match(Command('sudo abc', 'sudo: abc: No such file or directory'))


# Generated at 2022-06-14 10:52:36.389549
# Unit test for function match
def test_match():
    assert match(Command('sudo dokku local:command', 'sudo: dokku: command not found'))


# Generated at 2022-06-14 10:52:38.604872
# Unit test for function match
def test_match():
    assert match(Command('sudo ls',
                  'sudo: ls: command not found\n'))



# Generated at 2022-06-14 10:52:41.879955
# Unit test for function match
def test_match():
    assert match(Command('sudo echo yolo', ''))
    assert not match(Command('sudo echo yolo', 'sudo: echo: command not found'))
    

# Generated at 2022-06-14 10:52:44.782099
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo rm', 'sudo: rm: command not found')) == 'env "PATH=$PATH" rm'

# Generated at 2022-06-14 10:52:50.016438
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo -i foo', 'sudo: foo: command not found')) == \
        'env "PATH=$PATH" foo'
    assert get_new_command(Command('sudo -i foo bar', 'sudo: bar: command not found')) == \
        'sudo -i foo env "PATH=$PATH" bar'

# Generated at 2022-06-14 10:52:52.931163
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get install aptitude',
                         'sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get install aptitude', '   '))

# Generated at 2022-06-14 10:54:01.438366
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get upgrade', ''))
    assert not match(Command('sudo apt-get upgrade', 'sudo: apt-get: command not found\n'))
    assert not match(Command('sudo apt-get upgrade', 'E: Unable to locate package upgrade\n'))


# Generated at 2022-06-14 10:54:05.261504
# Unit test for function match
def test_match():
    output = 'sudo: npm: command not found'
    assert _get_command_name(output) == 'npm'
    assert match(output) == which('npm')


# Generated at 2022-06-14 10:54:07.596133
# Unit test for function match
def test_match():
    assert match(Command('sudo nano', 'sudo: nano: command not found'))
    assert not match(Command('sudo echo test', ''))


# Generated at 2022-06-14 10:54:10.096862
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo ls', 'sudo: ls: command not found\n')) == \
           'env "PATH=$PATH" sudo ls'

# Generated at 2022-06-14 10:54:22.984322
# Unit test for function match
def test_match():
    # Does not match if sudo command succeeded
    assert not match(Command("sudo -u user 'ls'"))
    # Does not match if command not found for another reason
    assert not match(Command("sudo -u user 'ls'", ''))
    # Does not match if no command found
    assert not match(Command("sudo -u user 'ls'",
                             'sudo: ls: command not found'))
    # Does not match if command is found
    assert not match(Command("sudo -u user 'ls'",
                             'sudo: ls: command not found',
                             '/usr/bin/ls'))
    # Matches if command is not found
    assert match(Command("sudo -u user 'ls'",
                         'sudo: ls: command not found', None))



# Generated at 2022-06-14 10:54:25.744060
# Unit test for function match
def test_match():
    assert which('ls')
    assert not match(Command('foo', '', '', 'sudo: foo: command not found'))
    assert match(Command('ls', '', '', 'sudo: ls: command not found'))


# Generated at 2022-06-14 10:54:28.448805
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('sudo vim', '', 'sudo: vim: command not found')) == 'env "PATH=$PATH" vim'

# Generated at 2022-06-14 10:54:33.825736
# Unit test for function get_new_command
def test_get_new_command():
    arg_test = Command('sudo missing_command arg1 arg2', 'sudo: missing_command: command not found')
    env_test = Command('sudo env PATH=$PATH missing_command arg1 arg2', 'sudo: missing_command: command not found')
    assert get_new_command(env_test) == u'env "PATH=$PATH" missing_command arg1 arg2'
    assert get_new_command(arg_test) == u'env "PATH=$PATH" missing_command arg1 arg2'

# Generated at 2022-06-14 10:54:36.591072
# Unit test for function match
def test_match():
    assert match(Command('sudo vim a', 
 'sudo: vim: command not found', None)) == True
    assert match(Command('sudo vim a', 
 'sudo: vim: command not foun', None)) == False


# Generated at 2022-06-14 10:54:41.520504
# Unit test for function get_new_command
def test_get_new_command():
    # Run command: $sudo ls
    # Show command not found error
    # Try to run command: $sudo env PATH=$PATH ls
    command = Command('sudo ls', 'sudo: ls: command not found')
    assert get_new_command(command) == 'sudo env PATH=$PATH ls'