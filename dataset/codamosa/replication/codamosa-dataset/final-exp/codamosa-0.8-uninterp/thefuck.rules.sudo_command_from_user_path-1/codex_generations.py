

# Generated at 2022-06-14 10:46:32.331426
# Unit test for function match
def test_match():
    assert match(Command('sudo sudo', 'sudo: sudo: command not found'))
    assert not match(Command('sudo sudo', 'sudo: su: command not found'))
    assert not match(Command('sudo sudo', 'sudo: sudo'))


# Generated at 2022-06-14 10:46:35.430398
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('sudo nano', 'sudo: nano: command not found')) == 'env "PATH=$PATH" nano'

# Generated at 2022-06-14 10:46:43.101112
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo ls',
                                   'sudo: ls: command not found')) == \
        'env "PATH=$PATH" sudo ls'
    assert get_new_command(Command('sudo ls -l',
                                   'sudo: ls: command not found')) == \
        'env "PATH=$PATH" sudo ls -l'
    assert get_new_command(Command('sudo script -a -b',
                                   'sudo: script: command not found')) == \
        'env "PATH=$PATH" sudo script -a -b'

# Generated at 2022-06-14 10:46:45.730057
# Unit test for function match
def test_match():
    assert match(Command('sudo fuck', err='sudo: fuck: command not found'))
    assert not match(Command('fuck'))


# Generated at 2022-06-14 10:46:50.049705
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', 'command not found'))
    assert match(Command('sudo ls', 'sudo: ls: command not found'))


# Generated at 2022-06-14 10:46:54.177531
# Unit test for function match
def test_match():
    assert match(Command('sudo nano',
                         'sudo: nano: command not found\n'))
    assert not match(Command('sudo nano',
                             'sudo: /usr/bin/nano: Permission denied\n'))



# Generated at 2022-06-14 10:46:56.572984
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get',
                         'sudo: apt-get: command not found'))



# Generated at 2022-06-14 10:47:03.956554
# Unit test for function match
def test_match():
    assert match(Command(script = 'sudo apt-get xxx', output = 'sudo: apt-get: command not found'))
    assert match(Command(script = 'sudo sh -c "apt-get xxx"', output = 'sudo: apt-get: command not found'))
    assert not match(Command(script = 'sudo apt-get xxx', output = 'sudo: apt-get: command not found\n'))


# Generated at 2022-06-14 10:47:17.172804
# Unit test for function match
def test_match():
    command1 = Command('sudo apt-get install python', 'sudo: apt-get: command not found')

    command2 = Command('sudo apt-get install python2.7',
                       'sudo: apt-get: command not found')
    assert match(command1)
    assert match(command2)

    command3 = Command('sudo apt-get install python', 'sudo: apt-get: command not found\n')
    assert match(command3)

    command4 = Command('sudo apt-get install python', 'sudo: apt-get: not found')
    assert not match(command4)



# Generated at 2022-06-14 10:47:19.721859
# Unit test for function match
def test_match():
    assert match(Command(u'sudo ls'))
    assert not match(Command('ls'))

# Generated at 2022-06-14 10:47:27.107835
# Unit test for function match
def test_match():
    assert match(Command('sudo get-pip.py',
                         'sudo: get-pip.py: command not found'))
    assert not match(Command('sudo get-pip.py', 'get-pip.py: command not found'))
    assert not match(Command('sudo get-pip.py', ''))

# Generated at 2022-06-14 10:47:30.584332
# Unit test for function match
def test_match():
    assert match(Command('sudo ss', 'ss: command not found'))
    assert not match(Command('sudo ss', ''))


# Generated at 2022-06-14 10:47:32.635749
# Unit test for function match
def test_match():
    assert match(Command('sudo guake', ''))



# Generated at 2022-06-14 10:47:36.220343
# Unit test for function get_new_command
def test_get_new_command():
    command = 'sudo foobar'
    new_command = get_new_command(command)
    assert new_command == 'sudo env "PATH=$PATH" foobar'

# Generated at 2022-06-14 10:47:39.760231
# Unit test for function match
def test_match():
    assert match('sudo: cd: command not found')
    assert match('sudo: basename: command not found')
    assert not match('sudo cd')


# Generated at 2022-06-14 10:47:51.085668
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.fix_sudo_path import _get_command_name, get_new_command
    from thefuck.shells import Shell
    class Command(object):
        def __init__(self, script, output):
            self.script = script
            self.output = output
    output  = "sudo: /usr/local/bin/certbot: command not found\n"
    command = Command('sudo /usr/local/bin/certbot --agree-tos --register-unsafely-without-email --standalone', output)
    assert _get_command_name(command) == '/usr/local/bin/certbot'

# Generated at 2022-06-14 10:47:55.766808
# Unit test for function get_new_command
def test_get_new_command():
    script = 'sudo echo test'
    command = Command(script, 'sudo: echo: command not found')
    assert get_new_command(command) == 'env "PATH=$PATH" sudo echo test'

# Generated at 2022-06-14 10:47:59.985634
# Unit test for function match
def test_match():
    assert which('sudo')
    assert not match(Command('sudo', 'sudo: xargs: command not found'))
    assert match(Command('sudo xargs', 'sudo: xargs: command not found'))


# Generated at 2022-06-14 10:48:03.538047
# Unit test for function match
def test_match():
    assert match(Command('sudo fafse'))
    assert match(Command('sudo a b c'))
    assert not match(Command('sudo -l'))



# Generated at 2022-06-14 10:48:07.873664
# Unit test for function match
def test_match():
    # Return True if error message matches
    assert match(Command('sudo ntifs', ''))
    # Return False if error message does not match
    assert not match(Command('sudo ntfs', output='Error: ntfs-3g not found.'))



# Generated at 2022-06-14 10:48:17.479429
# Unit test for function get_new_command
def test_get_new_command():
    # Test the scenario where PATH is not set
    command = Command('sudo ll', 'sudo: ll: command not found')
    assert get_new_command(command) == u'sudo env "PATH=$PATH" ll'

    # Test the scenario where PATH is set
    command = Command('sudo ll', 'sudo: PATH=/usr/bin: ll: command not found')
    assert get_new_command(command) == u'sudo env "PATH=$PATH" ll'

# Generated at 2022-06-14 10:48:20.757788
# Unit test for function match
def test_match():
    assert match(Command('sudo vim', 'sudo: no vim in /etc/sudoers'))
    assert not match(Command('sudo vim', 'vim not found'))

# Generated at 2022-06-14 10:48:25.672736
# Unit test for function get_new_command
def test_get_new_command():
    command = "sudo apt-get"
    assert get_new_command(command) == "env 'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' apt-get"

# Generated at 2022-06-14 10:48:29.280702
# Unit test for function match
def test_match():
    assert match(Command('sudo vi', 'sudo: vi: command not found'))
    assert not match(Command('sudo vi', 'sudo: vi command not found'))


# Generated at 2022-06-14 10:48:39.903178
# Unit test for function match
def test_match():
    assert match(Command(u'sudo -h', u'sudo: /usr/bin/sudo must be owned by uid 0 and have the setuid bit set',
                         u'sudo: /usr/bin/sudo must be owned by uid 0 and have the setuid bit set\r\n', 1,
                         u' sudo -h'))
    assert not match(Command(u'sudo -h', u'usage: sudo -h | -K | -k | -V', u'usage: sudo -h | -K | -k | -V\r\n', 0,
                             u' sudo -h'))


# Generated at 2022-06-14 10:48:43.442699
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo vi', 'sudo: vi: command not found')) == 'env "PATH=$PATH" vi'


enabled_by_default = True

# Generated at 2022-06-14 10:48:50.235052
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('sudo npm install',
                         ''))
    assert match(Command('sudo app',
                         'sudo: app: command not found'))
    assert not match(Command('sudo ls',
                         'sudo: ls: command not found'))
    assert not match(Command('sudo --reset-timestamp',
                         'sudo: --reset-timestamp: command not found'))


# Generated at 2022-06-14 10:48:58.038868
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get install vim', 'sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get install vim', 'sudo: unknown option'))
    assert match(Command('sudo apt-get install vim', 'sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get install vim', 'sudo: "apt-get": command not found'))


# Generated at 2022-06-14 10:49:01.758754
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -Qi nonexistent', ''))
    assert not match(Command('sudo pacman -Qi nonexistent', '', ''))
    assert not match(Command('cd nonexistent', ''))


# Generated at 2022-06-14 10:49:06.253230
# Unit test for function match
def test_match():
    assert which('aaa')
    assert not match(Command('aaa', ''))
    assert match(Command('aaa -q', 'sudo: aaa: command not found'))
    assert match(Command(u'fábíá', 'sudo: fábíá: command not found'))
    assert not match(Command('', ''))
    assert not match(Command('vim /etc/resolv.conf', ''))



# Generated at 2022-06-14 10:49:11.091931
# Unit test for function get_new_command
def test_get_new_command():
    assert 'env "PATH=$PATH" ls' == get_new_command('sudo ls').script

# Generated at 2022-06-14 10:49:21.027358
# Unit test for function match
def test_match():
    """
    Check if the function match() behaves properly as expected
    """
    from thefuck.rules.sudo_env_path import match
    # Case: Command 'sudo' has been inputted, then check if the output is correct
    command = "sudo apt-get insatll curl"
    output = "sudo: apt-get insatll curl: command not found"
    assert match(command, output) == True

    # Case: Command 'sudo' has not been inputted, then check if the output is correct
    command = "apt-get insatll curl"
    output = "sudo: apt-get insatll curl: command not found"
    assert match(command, output) == None


# Generated at 2022-06-14 10:49:24.993639
# Unit test for function match
def test_match():
    assert match(Command('sudo su', '', 'sudo: su: command not found'))
    assert not match(Command('sudo su', '', 'sudo: su: command not execute'))



# Generated at 2022-06-14 10:49:29.640695
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_env_path import get_new_command

    command = Command(script='sudo command', output='sudo: command: command not found')
    assert get_new_command(command) == 'sudo env "PATH=$PATH" command'

# Generated at 2022-06-14 10:49:35.315423
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo import get_new_command
    assert get_new_command(Command('sudo apt-get', 'sudo: apt-get: command not found')).script == 'env "PATH=$PATH" apt-get'
    assert get_new_command(Command('sudo apt-cache', 'sudo: apt-cache: command not found')).script == 'env "PATH=$PATH" apt-cache'

# Generated at 2022-06-14 10:49:37.963417
# Unit test for function match
def test_match():
    assert match(Command('sudo sudo', 'zsh: command not found: sudo'))
    assert not match(Command('sudo ls', ''))



# Generated at 2022-06-14 10:49:40.846183
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('sudo rm /etc/foo/bar')) == "env 'PATH=$PATH' rm '/etc/foo/bar'")

# Generated at 2022-06-14 10:49:50.621782
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get something', 'sudo: apt-get: command not found'))
    assert match(Command('sudo apt-get update', 'sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get upgrade', 'error'))
    assert not match(Command('sudo apt-get update', 'apt-get: command not found'))
    assert not match(Command('su -c "apt-get upgrade"', 'su: command not found'))


# Generated at 2022-06-14 10:49:52.647584
# Unit test for function match
def test_match():
    assert match(Command('sudo echo "a"', ''))
    assert not match(Command('echo "a"', ''))



# Generated at 2022-06-14 10:50:04.305423
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo find', '', 'sudo: find: command not found')) == 'env "PATH=$PATH" find'
    assert get_new_command(Command('sudo find . -name foo', '', 'sudo: find: command not found')) == 'env "PATH=$PATH" find . -name foo'
    assert get_new_command(Command('sudo apt-get install', '', 'sudo: apt-get: command not found')) == 'env "PATH=$PATH" apt-get install'
    assert get_new_command(Command('sudo traceroute -p 80 google.com', '', 'sudo: traceroute: command not found')) == 'env "PATH=$PATH" traceroute -p 80 google.com'

# Generated at 2022-06-14 10:50:13.906223
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("sudo ls foo").script == "ls foo"
    assert get_new_command("sudo env PATH=$PATH ls foo").script == "ls foo"

# Generated at 2022-06-14 10:50:15.685064
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('sudo vim') == u'env "PATH=$PATH" vim'

# Generated at 2022-06-14 10:50:19.943738
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo sduo', 'sduo: command not found')) == 'sudo env "PATH=$PATH" sduo'
    assert get_new_command(Command('sduo', 'sudo: sduo: command not found')) == 'env "PATH=$PATH" sduo'


enabled_by_default = False

# Generated at 2022-06-14 10:50:28.739961
# Unit test for function get_new_command

# Generated at 2022-06-14 10:50:36.528810
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo lssss')) == (
        'sudo env \'PATH=$PATH\' lssss')
    assert get_new_command(Command('sudo ls -la')) == (
        'sudo env \'PATH=$PATH\' ls -la')
    assert get_new_command(Command('sudo ls /tmp/jdk_home')) == (
        'sudo env \'PATH=$PATH\' ls /tmp/jdk_home')
    

# Generated at 2022-06-14 10:50:39.419764
# Unit test for function get_new_command
def test_get_new_command():
    script = "sudo foo"
    command = Command(script, "sudo: foo: command not found")
    assert get_new_command(command) == "env 'PATH=$PATH' sudo foo"

# Generated at 2022-06-14 10:50:41.709137
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get install sshfs', ''))
    assert not match(Command('vim', ''))


# Generated at 2022-06-14 10:50:45.047002
# Unit test for function match
def test_match():
    assert not match(Command('make hello',
                             stderr='sudo: make: command not found'))
    assert match(Command('make hello',
                         stderr='sudo: make: command not found'))


# Generated at 2022-06-14 10:50:50.513432
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_command_not_found import get_new_command
    command = "sudo echo 'hello world'; echo $?"
    new_command = get_new_command(command)
    assert new_command == "env \"PATH=$PATH\" sudo echo 'hello world'; echo $?"

# Generated at 2022-06-14 10:50:53.516485
# Unit test for function get_new_command
def test_get_new_command():
    com = Command('sudo ls', 'sudo: ls: command not found\n')
    assert get_new_command(com) == u'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:51:02.658429
# Unit test for function match
def test_match():
    command_name = "fucking_command"
    command = MagicMock(output=u'sudo: {}: command not found'.format(command_name))
    assert match(command)


# Generated at 2022-06-14 10:51:05.306831
# Unit test for function match
def test_match():
    assert match(Command('sudo vim', '', ''))
    assert not match(Command('sudo ls', '', ''))


# Generated at 2022-06-14 10:51:10.704829
# Unit test for function match
def test_match():
    assert match(Command(script='sudo docker', output='sudo: docker: command not found'))


# Generated at 2022-06-14 10:51:13.874268
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo rm file', 'sudo: rm: command not found')) == 'env "PATH=$PATH" rm file'



# Generated at 2022-06-14 10:51:17.007191
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script = "sudo ll", output = "sudo: ls: command not found")
    assert get_new_command(command) == "env \"PATH=$PATH\" sudo ll"

# Generated at 2022-06-14 10:51:19.853928
# Unit test for function match
def test_match():
    """
    Assert if function match is working properly
    """
    assert match(Command('foo sudo apt-get install hello', ''))



# Generated at 2022-06-14 10:51:22.253925
# Unit test for function match
def test_match():
    command = Command('sudo dnf install bash-completion', '')
    assert match(command) is not None



# Generated at 2022-06-14 10:51:25.456053
# Unit test for function match
def test_match():
    assert which('zsh')
    assert match(Command('sudo zsh',
                         'sudo: zsh: command not found', 1))

# Generated at 2022-06-14 10:51:28.425911
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo echo foo', 'sudo: echo: command not found')) == 'env "PATH=$PATH" echo foo'

# Generated at 2022-06-14 10:51:31.197872
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo programe', '')) == 'env "PATH=$PATH" programe'

# Generated at 2022-06-14 10:51:43.191527
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo foo --bar', 'sudo: foo: command not found')) == 'env "PATH=$PATH" foo --bar'

# Match unit test

# Generated at 2022-06-14 10:51:45.466588
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo lase', '')) == u'env "PATH=$PATH" lase'

# Generated at 2022-06-14 10:51:53.146758
# Unit test for function match
def test_match():
    # Test for expected behaviour if there is no error
    command = type("Command", (object,), {})
    command.output = type("Output", (object,), {})
    command.output.__str__ = lambda self: "nope"
    assert match(command) is None
    # Command is valid - should match
    command.output = "sudo: firefox: command not found"
    assert (match(command) == "/usr/bin/firefox")
    # Command is not valid - shouldn't match
    command.output = "sudo: firefoxxxxx: command not found"
    assert (match(command) == None)


# Generated at 2022-06-14 10:51:55.627844
# Unit test for function get_new_command
def test_get_new_command():
    
    assert get_new_command(Command('sudo python', 'sudo: python: command not found'))
    

# Generated at 2022-06-14 10:52:01.242015
# Unit test for function match
def test_match():
    assert match(Command('sudo anaconda', '/usr/bin/sudo anaconda'), None)
    assert match(Command('sudo fakething', 'sudo: fakething: command not found'), None)
    assert not match(Command('sudo ls', '$ sudo ls'), None)


# Generated at 2022-06-14 10:52:03.073738
# Unit test for function match
def test_match():
    assert match(Command('sudo vi', 'sudo: vi: command not found')).output == which('vi')


# Generated at 2022-06-14 10:52:05.027790
# Unit test for function match
def test_match():
    assert match(Command("sudo hello world", "sudo: hello: command not found"))



# Generated at 2022-06-14 10:52:08.137959
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('sudo vim', 'sudo: vim: command not found')) == 'env "PATH=$PATH" vim'

# Generated at 2022-06-14 10:52:10.553655
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', 'sudo: ls: command not found\n'))



# Generated at 2022-06-14 10:52:13.120473
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(u'sudo lslsls') == u'env "PATH=$PATH" lslsls'

# Generated at 2022-06-14 10:52:37.637287
# Unit test for function match
def test_match():
    assert match(Command('sudo vim /etc/not-exist',
                         'sudo: vim: command not found'))
    assert not match(Command('sudo emacs /etc/not-exist',
                             'sudo: emacs: command not found'))
    assert not match(Command('sudo vim /etc/not-exist', ''))



# Generated at 2022-06-14 10:52:41.336764
# Unit test for function match
def test_match():
    assert which('ls')
    assert for_app('sudo').match(Command('sudo ls',
                                         'sudo: ls: command not found'))



# Generated at 2022-06-14 10:52:44.219532
# Unit test for function match
def test_match():
    assert match(Command('sudo something', 'sudo: something: command not found'))
    assert not match(Command('sudo something', ''))



# Generated at 2022-06-14 10:52:49.132066
# Unit test for function get_new_command
def test_get_new_command():
    script = 'sudo -iu ec2-user /home/ec2-user/.pyenv/shims/python --version'
    command = Command(script, 'sudo: python: command not found\n')

    assert get_new_command(command) == 'env "PATH=$PATH" python --version'

# Generated at 2022-06-14 10:52:51.770144
# Unit test for function match
def test_match():
    assert guess.match(Command('sudo foobar', "sudo: foobar: command not found"))
    assert not guess.match(Command('sudo foobar', ""))


# Generated at 2022-06-14 10:52:57.801362
# Unit test for function match
def test_match():
    assert match('sudo abcdefg') == False
    assert match('sudo: abcdefg: command not found') == False
    assert match('sudo aaa') == False
    assert match('sudo: aaa: command not found') == True
    assert match('sudo ls') == True


# Generated at 2022-06-14 10:53:03.650182
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo sduo', 'sudo: sduo: command not found\n', 1)) == u'sudo env "PATH=$PATH" sduo'
    assert get_new_command(Command('sudo sduo', 'sudo: sduo: command not found\n', 2)) == u'sudo env "PATH=$PATH" sduo'

# Generated at 2022-06-14 10:53:07.539052
# Unit test for function get_new_command
def test_get_new_command():
    command = type("", (), {})()
    command.script = 'sudo echo 1'
    command.output = 'sudo: echo: command not found'
    assert get_new_command(command) == 'env "PATH=$PATH" echo 1'

# Generated at 2022-06-14 10:53:13.098119
# Unit test for function match
def test_match():
    assert not match(Command(script = 'sudo ls'))
    assert not match(Command(script = 'ls', output = 'Invalid command'))
    assert match(Command(script = 'sudo ls', output = 'sudo: ls: command not found'))


# Generated at 2022-06-14 10:53:16.325721
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', 'sudo: ls: command not found', ''))
    assert not match(Command('ls', '', ''))



# Generated at 2022-06-14 10:54:08.111348
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get update', ''))
    assert match(Command('sudo apt-get update', 'sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get update', 'sudo: apt-get: unable to open temp file'))


# Generated at 2022-06-14 10:54:10.161925
# Unit test for function match
def test_match():
    assert match(Command('sudo yo', 'sudo: yo: command not found'))
    assert not match(Command('sudo yo', ''))



# Generated at 2022-06-14 10:54:14.183090
# Unit test for function match
def test_match():
    assert not match(Command('sudo ls', output='sudo: ls: command not found'))
    assert match(Command('sudo htop', output='sudo: htop: command not found'))


# Generated at 2022-06-14 10:54:17.494492
# Unit test for function match
def test_match():
    assert match(Command('sudo a', output='sudo: a: command not found'))
    assert not match(Command('sudo a', output='real command not found'))


# Generated at 2022-06-14 10:54:27.293408
# Unit test for function get_new_command
def test_get_new_command():
    # Replace the same path with sudo and new command
    old = Command('sudo /sbin/start-stop-daemon --stop --quiet '
                  '--pidfile /var/run/nginx.pid --name nginx')
    new = Command('env "PATH=$PATH" /sbin/start-stop-daemon --stop --quiet '
                  '--pidfile /var/run/nginx.pid --name nginx')
    assert get_new_command(old) == new

    # Replace path with sudo and new command
    old = Command('sudo /sbin/start-stop-daemon --stop --quiet '
                  '--pidfile /var/run/nginx.pid --name nginx')

# Generated at 2022-06-14 10:54:29.239764
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('sudo echo lol', 'sudo: echo: command not found', 2)) == 'env "PATH=$PATH" echo lol')

# Generated at 2022-06-14 10:54:32.432430
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_command_not_found import get_new_command
    print(get_new_command('sudo lsb_release -a'))

# Generated at 2022-06-14 10:54:33.897786
# Unit test for function match
def test_match():
    assert match(Command('sudo foo', 'sudo: foo: command not found'))



# Generated at 2022-06-14 10:54:37.763798
# Unit test for function match
def test_match():
    output = 'sudo: gcc: command not found'
    assert match(Command('gcc', output))
    assert _get_command_name(Command('gcc', output)) == 'gcc'
    # Test to assert match fails if there is no command not found in the output
    assert not match(Command('gcc', 'gcc is the awesomest'))


# Generated at 2022-06-14 10:54:42.414637
# Unit test for function match
def test_match():
    command = Command('sudo ls')
    assert not match(command)
    command = Command('sudo command_not_found')
    assert match(command)
    command = Command('sudo: command_not_found: command not found')
    assert match(command)


# Generated at 2022-06-14 10:56:27.328069
# Unit test for function match
def test_match():
    command = 'sudo: ping: command not found'
    assert match(command) == 'ping'