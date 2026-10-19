

# Generated at 2022-06-14 10:46:30.965065
# Unit test for function match
def test_match():
    assert not match(Command('example'))
    assert match(Command('sudo example', 'sudo: example: command not found'))
    assert which('ls') # test know a command that exists, to be sure that match returns True


# Generated at 2022-06-14 10:46:33.559400
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo hello', 'sudo: hello: command not found')) == u'env "PATH=$PATH" hello'

# Generated at 2022-06-14 10:46:36.172323
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo foo', 'sudo: foo: command not found')) == "env \"PATH=$PATH\" foo"



# Generated at 2022-06-14 10:46:39.991869
# Unit test for function match
def test_match():
    from thefuck.rules.sudo import match
    command = Command('sudo abc', 'sudo: abc: command not found\n')
    assert match(command) is not None
    command = Command('sudo abc', 'abcd')
    assert match(command) is None


# Generated at 2022-06-14 10:46:42.942506
# Unit test for function match
def test_match():
    assert match(Command('sudo nonexistent-sudo-command',
                         'sudo: nonexistent-sudo-command: command not found'))



# Generated at 2022-06-14 10:46:45.169795
# Unit test for function match
def test_match():
    command = Command('sudo dpkg --purge package', '')
    assert match(command) is True


# Generated at 2022-06-14 10:46:47.117397
# Unit test for function match
def test_match():
    assert match('sudo foo') is None
    assert match('sudo: foo: command not found')


# Generated at 2022-06-14 10:46:51.359803
# Unit test for function match
def test_match():
    assert (match(Command('sudo fakeOperation', '')) == None)
    assert (match(Command('sudo apt-get install', 'sudo: apt-get: command not found')) == '/usr/bin/apt-get')


# Generated at 2022-06-14 10:46:57.128482
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("sudo ls", "sudo: ls: command not found")
    assert get_new_command(command) == u'env "PATH=$PATH" ls'
    command = Command("sudo ls -l", "sudo: ls: command not found")
    assert get_new_command(command) == u'env "PATH=$PATH" ls -l'

# Generated at 2022-06-14 10:47:01.501056
# Unit test for function get_new_command
def test_get_new_command():
    from .tools import Command
    command = Command('sudo google-chrome')
    command.output = u'sudo: google-chrome: command not found'
    assert get_new_command(command) == 'sudo env "PATH=$PATH" google-chrome'

# Generated at 2022-06-14 10:47:11.148110
# Unit test for function match
def test_match():
    assert match(Command('sudo vim you.txt', 'sudo: vim: command not found'))
    assert match(Command('sudo vim you.txt', 'sudo:  vim: command not found'))
    assert match(Command('sudo vim you.txt', 'sudo:  :vim: command not found'))
    assert match(Command('sudo vim you.txt', 'sudo: :vim: command not found'))
    assert match(Command('sudo vim you.txt', 'sudo: :  vim: command not found'))
    assert match(Command('sudo vim you.txt', 'sudo: :  :vim: command not found'))

    assert not match(Command('vim you.txt', 'sudo: vim: command not found'))



# Generated at 2022-06-14 10:47:13.315097
# Unit test for function match
def test_match():
    assert match(Command('sudo yaourt',
                         'sudo: yaourt:command not found'))


# Generated at 2022-06-14 10:47:16.242797
# Unit test for function match
def test_match():
    assert match(Command('sudo echo', 'sudo: echo: command not found'))
    assert not match(Command('ls', ''))

# Generated at 2022-06-14 10:47:19.908123
# Unit test for function match
def test_match():
    assert match(Command('sudo netstat', 'sudo: netstat: command not found'))
    assert not match(Command('sudo netstat', 'sudo: netstat: command found'))

# Generated at 2022-06-14 10:47:24.112570
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo echo "Hello"', 'sudo: echo: command not found',
                                   '/bin')) == 'env "PATH=$PATH" echo "Hello"'


disabled_by_default = True

# Generated at 2022-06-14 10:47:26.266034
# Unit test for function match
def test_match():
    command = """sudo: ls: command not found"""
    assert match(command) == True


# Generated at 2022-06-14 10:47:31.394577
# Unit test for function match
def test_match():
    assert _get_command_name('sudo: passwd: command not found') == 'passwd'
    assert _get_command_name('sudo: : command not found') == ''
    assert _get_command_name('sudo: passwd') == ''

# Generated at 2022-06-14 10:47:33.362067
# Unit test for function match
def test_match():
    assert match(Command('sudo echo hello', ''))


# Generated at 2022-06-14 10:47:37.564062
# Unit test for function match
def test_match():
    assert match(Command(script='sudo echo foo', output="sudo: echo: command not found"))
    assert not match(Command(script='sudo ls', output=""))
    assert not match(Command(script='sudo ls', output="ls: command not found"))

# Generated at 2022-06-14 10:47:39.817717
# Unit test for function match
def test_match():
    assert match(Command('sudo git status -v', "sudo: git: command not found"))


# Generated at 2022-06-14 10:47:48.138694
# Unit test for function match
def test_match():
    # Test match when command is found
    assert match(Command('sudo mkdir test', 'mkdir: cannot create directory'
                         ' `test\': Permission denied'))

    # Test match when comand isn't found
    assert not match(Command('sudo make', 'make: *** No targets specified'
                             ' and no makefile found.  Stop.'))

# Generated at 2022-06-14 10:47:55.840270
# Unit test for function get_new_command
def test_get_new_command():
    script = "sudo service"
    new_script = "env \"PATH=$PATH\" sudo service"
    assert get_new_command(Command(script, "sudo: service: command not found", "")) == new_script
    new_script = "env \"PATH=$PATH\" sudo ufw"
    assert get_new_command(Command(script, "sudo: ufw: command not found", "")) == new_script

# Generated at 2022-06-14 10:48:00.422295
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo vi',
                      'sudo: vi: command not found',
                      '/home')
    new_command = get_new_command(command)
    assert new_command == 'env "PATH=$PATH" vi', new_comma

# Generated at 2022-06-14 10:48:08.356340
# Unit test for function match
def test_match():
    assert not match(Command(script=u'cd ~/fuck'))
    assert not match(Command(script=u'cd ~/foo && sudo ls', output=u''))
    assert match(Command(script=u'sudo foo', output=u'sudo: foo: command not found'))
    assert not match(Command(script=u'sudo foo', output=u'sudo: bar: command not found'))
    assert not match(Command(script=u'sudo foo', output=u'foo: command not found'))

# Generated at 2022-06-14 10:48:12.834829
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get update', ''))
    assert match(Command('sudo apt-get update', "sudo: apt-get: command not found"))
    assert not match(Command('sudo apt-get update', 'Hit'))



# Generated at 2022-06-14 10:48:19.183247
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo echo foo', 'sudo: echo: command not found', output='sudo: echo: command not found')) == \
           'env "PATH=$PATH" echo foo'

    assert get_new_command(Command('sudo grep bar', 'sudo: grep: command not found', output='sudo: grep: command not found')) == \
           'env "PATH=$PATH" grep bar'

# Generated at 2022-06-14 10:48:29.492831
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo emacs /fandom/magic.txt', 'sudo: emacs: command not found')
    assert 'env "PATH=$PATH" emacs /fandom/magic.txt' == get_new_command(command).script
    command = Command('sudo su', 'sudo: su: command not found')
    assert 'env "PATH=$PATH" su' == get_new_command(command).script
    command = Command('sudo su -', 'sudo: su: command not found')
    assert 'env "PATH=$PATH" su -' == get_new_command(command).script

# Generated at 2022-06-14 10:48:32.517432
# Unit test for function match
def test_match():
    # No test needed because all logic is in get_new_command
    pass



# Generated at 2022-06-14 10:48:36.509496
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    assert get_new_command(Command(script='sudo echo hello', output='sudo: echo: command not found')) == 'sudo env "PATH=$PATH" echo hello'

# Generated at 2022-06-14 10:48:39.073299
# Unit test for function match
def test_match():
    assert which('ls')
    assert match(Command('sudo ls', 'sudo: ls: command not found'))



# Generated at 2022-06-14 10:48:46.775414
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo pacman-key --help', 'sudo: pacman-key: command not found')
    assert get_new_command(command) == "sudo env 'PATH=$PATH' pacman-key --help"



# Generated at 2022-06-14 10:48:48.557596
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', "sudo: /usr/bin/ls: command not found"))
    

# Generated at 2022-06-14 10:48:51.658362
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ls',
                      'sudo: ls: command not found')
    assert get_new_command(command) == u'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:48:56.981321
# Unit test for function match
def test_match():
    check_output = u'sudo: composer: command not found'
    command = '/usr/local/bin/composer update --profile'
    assert match(Command(command, check_output))
    assert not match(Command('sudo dnf install aspell', ''))


# Generated at 2022-06-14 10:48:59.752884
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('sudo ll', 'sudo: ll: command not found'))) == u'sudo env "PATH=$PATH" ll'

# Generated at 2022-06-14 10:49:01.931725
# Unit test for function match
def test_match():
    assert (match(Command('sudo cd', 'sudo: cd: command not found')))


# Generated at 2022-06-14 10:49:05.211413
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get install fuck'))
    assert not match(Command('sudo apt-get install python'))


# Generated at 2022-06-14 10:49:10.833279
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('sudo dpkg -i file.deb').script == 'env "PATH=$PATH" dpkg -i file.deb'
    assert get_new_command('sudo apt-get update && sudo apt-get dist-upgrade').script == \
            'env "PATH=$PATH" apt-get update && env "PATH=$PATH" apt-get dist-upgrade'

# Generated at 2022-06-14 10:49:14.371005
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo echo test', 'sudo: echo: command not found\n')
    assert get_new_command(command) == 'env "PATH=$PATH" echo test'

# Generated at 2022-06-14 10:49:19.078266
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.fix_sudo import get_new_command
    from thefuck.rules.sudo import Command
    assert get_new_command(Command('sudo gedit', "sudo: gedit: command not found\n", '', 1)) == "env \"PATH=$PATH\" gedit"

# Generated at 2022-06-14 10:49:28.360592
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo test --1', '', '')) == 'env "PATH=$PATH" test --1'

# Generated at 2022-06-14 10:49:32.054567
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', stderr='sudo: ls: command not found'))
    assert not match(Command('sudo ls', stderr='ls: command not found'))


# Generated at 2022-06-14 10:49:35.319759
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_env_path import get_new_command
    assert get_new_command(Command('sudo ls', 'sudo: ls: command not found\nnone')) == u'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:49:37.509670
# Unit test for function match
def test_match():
    command = Command('sudo sudkfl', 'sudo: sudkfl: command not found')
    assert match(command)


# Generated at 2022-06-14 10:49:39.845287
# Unit test for function match
def test_match():
    assert not match(command_output='sudo: time: command not found')
    assert not match(command_output='sudo: time haha')
    assert match(command_output='sudo: time: command not found')


# Generated at 2022-06-14 10:49:45.006286
# Unit test for function match
def test_match():
    assert re.match(r'sudo: super(user|group)?: command not found', match(Command('sudo super', 'sudo: super: command not found')))
    assert not re.match(r'sudo: super(user|group)?: command not found', match(Command('sudo super', 'sudo: super: no such file or directory')))


# Generated at 2022-06-14 10:49:51.732232
# Unit test for function match
def test_match():
    assert which("pwd")

    assert match(Command("sudo pwd", "sudo: pwd: command not found\n"))
    assert not match(Command("sudo pwd", ""))
    assert not match(Command("sudo pwd", "sudo: pwd: command not found",
                             err=True))



# Generated at 2022-06-14 10:49:55.617099
# Unit test for function match
def test_match():

    cmd_ls = Command('sudo ls',
'''sudo: ls: command not found
''')

    assert match(cmd_ls)

    cmd_ls2 = Command('sudo ls',
'''[sudo] password for a:
ls
''')

    assert not match(cmd_ls2)

# Generated at 2022-06-14 10:49:59.622192
# Unit test for function match
def test_match():
    assert match(Command('sudo su', 'su: command not found'))
    assert not match(Command('echo "Hello World !"', ''))


# Generated at 2022-06-14 10:50:01.306996
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('sudo ls') == 'sudo env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:50:17.218870
# Unit test for function match
def test_match():
    assert match(Command('sudo git commit', 'sudo: git: command not found'))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 10:50:19.382766
# Unit test for function match
def test_match():
    assert(match(Command('sudo echo test', 'sudo: echo: command not found\n')))


# Generated at 2022-06-14 10:50:22.336760
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('sudo ./test') == \
           'sudo env "PATH=$PATH" ./test'



# Generated at 2022-06-14 10:50:25.760957
# Unit test for function get_new_command
def test_get_new_command():
    import pytest
    from thefuck.types import Command

    command = Command("sudo sss", "sudo: sss: command not found")
    assert get_new_command(command) == u'sudo env "PATH=$PATH" sss'

# Generated at 2022-06-14 10:50:28.702097
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo abc', '''sudo: abc: command not found
''')) == 'env "PATH=$PATH" abc'
    assert get_new_command(Command('sudo ll', '''sudo: ll: command not found
''')) == 'env "PATH=$PATH" ll'

# Generated at 2022-06-14 10:50:31.509442
# Unit test for function match
def test_match():
    expected = 'ls'

    command = Command('sudo ls ', 'sudo: ls: command not found')
    assert match(command) == expected



# Generated at 2022-06-14 10:50:37.142229
# Unit test for function match
def test_match():
    # Test with found command
    command = Command('sudo apt-get install python3-dev', 'sudo: apt-get: command not found')
    assert match(command)

    # Test with not found command
    command = Command('sudo apt-get install python3-dev', '')
    assert not match(command)



# Generated at 2022-06-14 10:50:40.404517
# Unit test for function match
def test_match():
    assert match(Command('sudo foobar',
                         'sudo: foobar: command not found\r\n'))
    assert not match(Command('sudo foobar', 'sudo: foobar: something'))



# Generated at 2022-06-14 10:50:43.526979
# Unit test for function match
def test_match():
    command = type('obj', (object,), {'output': 'sudo: sudoedit: command not found'})()
    assert match(command) is False
    command = type('obj', (object,), {'output': 'sudo: git: command not found'})()
    assert match(command) is not False


# Generated at 2022-06-14 10:50:47.004539
# Unit test for function match
def test_match():
    assert match(Command('sudo lss', '', 'sudo: lss: command not found'))
    assert match(Command('sudo lss', '', '')) is None

# Generated at 2022-06-14 10:51:16.003822
# Unit test for function match
def test_match():
    assert match(Command('sudo echo hello world', ''))
    assert not match(Command('echo hello world', ''))


# Generated at 2022-06-14 10:51:18.247894
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo rm test.txt', 'sudo: rm: command not found')) == 'env "PATH=$PATH" rm test.txt'

# Generated at 2022-06-14 10:51:22.253342
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_env import get_new_command

    command = 'sudo: npm: command not found'
    assert get_new_command(command) == u'env "PATH=$PATH" npm'

# Generated at 2022-06-14 10:51:34.739598
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    apps = ['ls', 'vim', 'cd', 'cal', 'pwd', 'emacs', 'bash']
    errors = ['sudo: ls: command not found', 'sudo: vim: command not found',
              'sudo: cd: command not found', 'sudo: cal: command not found', 'sudo: pwd: command not found',
              'sudo: emacs: command not found', 'sudo: bash: command not found']
    commands = ['sudo ls', 'sudo vim', 'sudo cd', 'sudo cal', 'sudo pwd', 'sudo emacs', 'sudo bash']

# Generated at 2022-06-14 10:51:38.263935
# Unit test for function match
def test_match():
    assert match(Command('sudo dmesg', None))
    assert not match(Command('sudo apt-get update', None))

# Generated at 2022-06-14 10:51:41.567552
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ls')
    command._output = "sudo: ls: command not found"

    assert get_new_command(command) == u'sudo env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:51:46.977461
# Unit test for function match
def test_match():
    assert match(Command('sudo a', """'a' is not recognized as an internal or external command,
operable program or batch file."""))
    assert not match(Command('sudo a', """'a' is recognized as an internal or external command,
operable program or batch file."""))


# Generated at 2022-06-14 10:51:51.708978
# Unit test for function get_new_command
def test_get_new_command():
    script = "sudo " + "echo " + "\"hello\""
    output = "sudo: echo: command not found"
    command = Command(script, output)
    assert get_new_command(command) == "env \"PATH=$PATH\" echo \"hello\""

# Generated at 2022-06-14 10:51:55.330359
# Unit test for function match
def test_match():
    assert match(Command('doit', stderr='sudo: sudo: command not found'))
    assert not match(Command('sudo whoami', ''))
    assert not match(Command('sudo whoami', '', 1))


# Generated at 2022-06-14 10:51:59.750874
# Unit test for function get_new_command
def test_get_new_command():

    from thefuck.types import Command

    command = Command('sudo vim', 'sudo: vim: command not found')
    assert get_new_command(command) == u'env "PATH=$PATH" vim'

# Generated at 2022-06-14 10:52:56.602757
# Unit test for function get_new_command
def test_get_new_command():
    command = '$ sudo sl'
    command_name = _get_command_name(command)
    assert get_new_command(command) == 'env "PATH=$PATH" sl'

# Generated at 2022-06-14 10:53:03.281315
# Unit test for function match
def test_match():
    assert not match(Command('', ''))
    assert not match(Command('sudo ls', ''))
    assert not match(Command('sudo ls', 'sudo:ls:command not found'))
    assert which('sudo') == match(Command('sudo',
                                          'sudo: sudo: command not found'))
    assert which('git') == match(Command('sudo git',
                                         'sudo: git: command not found'))


# Generated at 2022-06-14 10:53:06.315051
# Unit test for function match
def test_match():
    assert match(Command(script="sudo echo test", output="sudo: echo: command not found")) is not None
    assert match(Command(script="sudo echo test", output="test")) is None

# Generated at 2022-06-14 10:53:09.698574
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ./env_path.py')
    assert get_new_command(command) == 'sudo env "PATH=$PATH" ./env_path.py'

# Generated at 2022-06-14 10:53:15.646837
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {
        'script': u'sudo pacman -Syyu',
        'output': u'sudo: pacman: command not found'
    })
    assert get_new_command(command) == (u'sudo env "PATH=$PATH" pacman -Syyu')

# Generated at 2022-06-14 10:53:23.429880
# Unit test for function match
def test_match():
    assert match(Command('sudo gedit',
           'sudo: gedit: command not found\n'))
    assert not match(Command('sudo gedit',
                             'gedit: unrecognized option \'--version\''))


# Generated at 2022-06-14 10:53:26.298784
# Unit test for function match
def test_match():
    assert match(Command("sudo mkdir /tmp/example", ""))
    assert not match(Command("sudo mkdir /tmp/example",
                             "sudo: mkdir: command not found"))


test_match.expect = ['sudo']



# Generated at 2022-06-14 10:53:32.490888
# Unit test for function match
def test_match():
    assert match(Command('sudo touch testfile.txt', ''))
    assert match(Command('sudo touch testfile.txt', 'sudo: touch: command not found'))
    assert not match(Command('touch testfile.txt', ''))
    assert not match(Command('touch testfile.txt', 'sudo: touch: command not found'))


# Generated at 2022-06-14 10:53:35.377646
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ls', 'sudo: ls: command not found\n')
    assert get_new_command(command) == 'env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:53:37.162481
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('sudo command', 'sudo: command: command not found')) == 'env "PATH=$PATH" sudo command'

# Generated at 2022-06-14 10:55:49.255782
# Unit test for function get_new_command
def test_get_new_command():
    input_ = (Command('These are not the droids sudo: ', 'sudo: droid: command not found'),
              Command('sudo: somedroid: command not found', ''))
    output = [u'These are not the droids env "PATH=$PATH" sudo: droid',
              u'env "PATH=$PATH" sudo: somedroid']
    for idx, cmd in enumerate(input_):
        assert get_new_command(cmd) == Command(cmd.script, output[idx])

# Generated at 2022-06-14 10:55:51.289671
# Unit test for function match
def test_match():
    assert(for_app('sudo') is not None)


# Generated at 2022-06-14 10:55:55.607367
# Unit test for function match
def test_match():
    assert match(Command('sudo hello-world', ''))
    assert match(Command('sudo nope nope', 'sudo: nope: command not found'))
    assert not match(Command('sudo nope nope', ''))



# Generated at 2022-06-14 10:55:58.684631
# Unit test for function match
def test_match():
    assert match(Command('sudo fg', 'sudo: fg: command not found'))
    assert not match(Command('sudo fg', 'fg: command not found'))


# Generated at 2022-06-14 10:56:02.786172
# Unit test for function match
def test_match():
    assert match(Command('sudo abc', 'sudo: abc: command not found'))
    assert not match(Command('sudo', ''))
    assert not match(Command('sudo apt-get', ''))

# Generated at 2022-06-14 10:56:09.514534
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('su', output='sudo: lsh: command not found',
                                   script='su')) == 'env "PATH=$PATH" lsh'
    assert get_new_command(Command('su', output='sudo: lsh: command not found',
                                   script='su lsh')) == 'env "PATH=$PATH" lsh'

# Generated at 2022-06-14 10:56:19.833255
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(type('', (), {'script': 'sudo rpms', 'output': 'sudo: rpms: command not found\n'})) == 'env "PATH=$PATH" rpms'
    assert get_new_command(type('', (), {'script': 'sudo ls', 'output': 'sudo: ls: command not found\n'})) == 'env "PATH=$PATH" ls'
    assert get_new_command(type('', (), {'script': 'sudo cat', 'output': 'sudo: cat: command not found\n'})) == 'env "PATH=$PATH" cat'

# Generated at 2022-06-14 10:56:22.878506
# Unit test for function match
def test_match():
    assert match(Command('sudo restart', 'sudo: restart: command not found'))
    assert not match(Command('sudo restart', 'sudo: not the right command'))


# Generated at 2022-06-14 10:56:26.360145
# Unit test for function match
def test_match():
    assert match(Command('sudo reboot', "sudo: reboot: command not found\n"))
    assert not match(Command('sudo reboot', 'reboot: no reboot command\n'))