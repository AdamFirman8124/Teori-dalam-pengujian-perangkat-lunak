

# Generated at 2022-06-14 10:46:28.270810
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck import types
    from os import path
    dir_path = path.dirname(path.realpath(__file__))

    assert get_new_command(types.Command('sudo test command not found',
                                         u'echo $PATH',
                                         'echo /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin',
                                         u'/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin')) == \
        u'env "PATH=$PATH" test echo $PATH'


# Generated at 2022-06-14 10:46:34.466699
# Unit test for function match
def test_match():
    assert match(Command('sudo abc', '', 'sudo: abc: command not found'))
    assert not match(Command('sudo abc', '', ''))
    assert not match(Command('sudo abc', '', 'sudo: abc: command'))


# Generated at 2022-06-14 10:46:37.754415
# Unit test for function get_new_command
def test_get_new_command():
    script = 'sudo echo "hello"'
    command = Command(script, 'sudo: echo: command not found')
    assert get_new_command(command) == 'env "PATH=$PATH" echo "hello"'

# Generated at 2022-06-14 10:46:39.785015
# Unit test for function match
def test_match():
    assert match(Command('sudo asd', '/dev/null', 'sudo: asd: command not found'))


# Generated at 2022-06-14 10:46:42.399025
# Unit test for function match
def test_match():
    assert match(Command('sudo yum update', 'sudo: yum: command not found'))
    assert not match(Command('sudo yum update', ''))


# Generated at 2022-06-14 10:46:47.273727
# Unit test for function match
def test_match():
    output_for_test = "sudo: hidden: command not found"
    assert (match(Command(output_for_test, "test")) == True)
    output_for_test = "sudo: hidden: command is found"
    assert (match(Command(output_for_test, "test")) == False)


# Generated at 2022-06-14 10:46:50.528179
# Unit test for function match
def test_match():
    assert match(Command('sudo git branch', 'sudo: git: command not found'))
    assert not match(Command('git branch', 'git: command not found'))


# Generated at 2022-06-14 10:46:55.423940
# Unit test for function match
def test_match():
    assert match(Command('sudo foo', output=('sudo: foo: command not found\n')))
    assert not match(Command(''))
    assert not match(Command('sudo foo', output=('sudo: bar: command not found\n')))


# Generated at 2022-06-14 10:47:00.631122
# Unit test for function get_new_command
def test_get_new_command():
    script = 'sudo rm -f testfile'
    output = 'sudo: /usr/local/bin/rm: command not found'
    command = Command(script, output)

    assert get_new_command(command) == 'env "PATH=$PATH" rm -f testfile'

# Generated at 2022-06-14 10:47:03.836341
# Unit test for function match
def test_match():
    assert match(Command('sudo sudodf', 'sudo: sudodf: command not found'))
    assert not match(Command('sudo sudodf', ''))

# Generated at 2022-06-14 10:47:08.496578
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('sudo test',
                                   'sudo: test: command not found',
                                   ''))



# Generated at 2022-06-14 10:47:12.952689
# Unit test for function match
def test_match():
    assert match(Command('sudo git', '', 'sudo: git: command not found'))
    assert not match(Command('git', '', ''))
    assert not match(Command('sudo git', '', ''))



# Generated at 2022-06-14 10:47:22.099628
# Unit test for function match
def test_match():
	c = Command('test',
				'',
				'',
				'',
				'',
				'',
				'',
				'',
				'sudo: test: command not found')
	assert _get_command_name(c) == 'test'

# Generated at 2022-06-14 10:47:27.108249
# Unit test for function match
def test_match():
    assert not match(Command('sudo apt-get update', '', 'sudo: apt-get: command not found'))
    assert match(Command('sudo apt-get update', '', 'sudo: apt-get: command not found'))
    assert not match(Command('sudo apt-get update', '', ''))

# Generated at 2022-06-14 10:47:31.247452
# Unit test for function match
def test_match():
    assert match(Command('sudo abc', ''))
    assert not match(Command('sudo abc', 'sudo: abc: command not found'))


# Generated at 2022-06-14 10:47:37.709830
# Unit test for function get_new_command
def test_get_new_command():
    script = "sudo apt-get install vim"
    output = "sudo: apt-get: command not found"
    name = "apt-get"
    new_script = replace_argument(script, name, u'env "PATH=$PATH" {}'.format(name))
    assert get_new_command(Command(script, output)) == new_script


# Generated at 2022-06-14 10:47:46.263040
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ifconfig')
    new_command = get_new_command(command)
    assert new_command == 'sudo env "PATH=$PATH" ifconfig'

    command = Command('sudo apt-get update')
    new_command = get_new_command(command)
    assert new_command == 'sudo env "PATH=$PATH" apt-get update'

    command = Command('sudo apt update')
    new_command = get_new_command(command)
    assert new_command == 'sudo env "PATH=$PATH" apt update'



# Generated at 2022-06-14 10:47:57.151192
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.pip_command_not_found import get_new_command
    assert 'env' in get_new_command('sudo pip install thefuck').script
    assert 'env' in get_new_command('sudo pip3 install thefuck').script
    assert 'env' in get_new_command('sudo -H pip install thefuck').script
    assert 'env' in get_new_command('sudo -H pip3 install thefuck').script
    assert 'env' not in get_new_command('sudo pip install --user thefuck').script
    assert 'env' not in get_new_command('sudo -H pip install --user thefuck').script

# Generated at 2022-06-14 10:47:59.705549
# Unit test for function match
def test_match():
    # Test for not found command
    assert match(Command('sudo', 'sudo: ls: command not found')) == None
    # Test for found command
    assert match(Command('sudo', 'sudo: bash: command not found')) != None


# Generated at 2022-06-14 10:48:03.000920
# Unit test for function match
def test_match():
    assert match(Command('sudo date +%m-%d', '', 'sudo: date: command not found'))


# Generated at 2022-06-14 10:48:19.603146
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo aa', 'sudo: aa: command not found')) == u'sudo env "PATH=$PATH" aa'
    assert get_new_command(Command('aa', 'sudo: aa: command not found')) == u'env "PATH=$PATH" aa'
    assert get_new_command(Command('sudo aa ', 'sudo: aa: command not found')) == u'sudo env "PATH=$PATH" aa '
    assert get_new_command(Command(' sudo aa', 'sudo: aa: command not found')) == u' sudo env "PATH=$PATH" aa'
    assert get_new_command(Command('aa bb cc', 'sudo: aa: command not found')) == u'aa bb cc'

# Generated at 2022-06-14 10:48:25.673062
# Unit test for function match
def test_match():
    # Test case 1: command not found
    assert not match(Command('sudo command_not_exists', '', stderr='sudo: command_not_exists: command not found'))
    # Test case 2: command found
    assert not match(Command('sudo echo "Hello world!"', '', stderr=''))

# Generated at 2022-06-14 10:48:30.230770
# Unit test for function match
def test_match():
    assert re.findall(r'command not found',
                      'sudo: command not found') == ['command not found']
    assert re.findall(r'command not found',
                      'sudo: uname: command not found') == ['command not found']



# Generated at 2022-06-14 10:48:33.632880
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command('sudo sudo', 'sudo: sudo: command not found\n')) == 'env "PATH=$PATH" sudo sudo'

# Generated at 2022-06-14 10:48:45.160367
# Unit test for function match
def test_match():
    assert match(Command('sudo not_found',
            output='sudo: not_found: command not found'))
    # command path which was on $PATH should be found
    assert match(Command('sudo not_found',
            output='sudo: not_found: command not found',
            env={'PATH': '/usr/local/bin:/usr/bin'}))
    assert not match(Command('sudo not_found',
            output='sudo: not_found: comman.',
            env={'PATH': '/usr/local/bin:/usr/bin'}))
    # command path which was not on $PATH should not be found
    assert not match(Command('sudo not_found',
            output='sudo: not_found: command not found',
            env={'PATH': '/usr/bin'}))


# Generated at 2022-06-14 10:48:48.803403
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script = 'sudo ifconfig',
                      stdout = 'sudo: ifconfig: command not found') 
    assert get_new_command(command) == 'env "PATH=$PATH" ifconfig'

# Generated at 2022-06-14 10:48:51.986980
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('sudo git', "sudo: git: command not found\n"))
    assert new_command == "env $PATH git"

# Generated at 2022-06-14 10:48:55.741875
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo ls', "sudo: ls: command not found\n")
    assert get_new_command(command) == 'sudo env "PATH=$PATH" ls'

# Generated at 2022-06-14 10:48:58.468002
# Unit test for function match
def test_match():
    assert not match(Command('foo', ''))
    assert match(Command('sudo', 'sudo: foo: command not found\n'))



# Generated at 2022-06-14 10:49:02.853415
# Unit test for function match
def test_match():
    # Should match
    assert match(Command('sudo vim', 'sudo: vim: command not found', None))
    # Should not match
    assert not match(Command('sudo vim', '', None))
    assert not match(Command('vim', '', None))


# Generated at 2022-06-14 10:49:12.078224
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    new_cmd = get_new_command(Command('sudo foo', output='sudo: foo: command not found'))
    assert new_cmd == u'env "PATH=$PATH" foo'

# Generated at 2022-06-14 10:49:18.557444
# Unit test for function match
def test_match():
    assert (which('echo') and which('sucs') and
            match(Command('sudo echo', '')))
    assert (which('sudo') and which('sudo') and
            not match(Command('sudo sudo', '')))
    assert not match(Command('sudo echo', 'sudo: echo: command not found'))
    assert not match(Command('sudo echo', ''))



# Generated at 2022-06-14 10:49:23.663632
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('sudo echo',
                         '/tmp/test.sh: line 7: echo: command not found'))
    assert not match(Command('sudo echo', 'echo'))



# Generated at 2022-06-14 10:49:26.689884
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("sudo fuck", "sudo: fuck: command not found")
    assert get_new_command(command) == 'env "PATH=$PATH" fuck'

# Generated at 2022-06-14 10:49:29.917581
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo echo "abc"')
    command.output = u'sudo: echo: command not found'
    assert get_new_command(command) == 'env "PATH=$PATH" echo "abc"'

# Generated at 2022-06-14 10:49:32.324133
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo test', 'sudo: test: command not found\n')) == u'env "PATH=$PATH" test'

# Generated at 2022-06-14 10:49:36.849129
# Unit test for function match
def test_match():

    # Test command with output that does not match
    command = Command(script='sudo ls /')

    assert not match(command)

    # Test command with output that does match
    command = Command(script='sudo', output='''sudo: /usr/bin/colordiff: command not found
''')

    assert match(command)


# Generated at 2022-06-14 10:49:38.688936
# Unit test for function match
def test_match():
    command = Command("sudo fck", "sudo: fck: command not found")
    assert match(command)



# Generated at 2022-06-14 10:49:43.060673
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('sudo pmbc',
                     u'sudo: pmbc: command not found\nsudo: pmbc: command not found\n')
    assert get_new_command(command) == u'env "PATH=$PATH" pmbc'

# Generated at 2022-06-14 10:49:46.411002
# Unit test for function match
def test_match():
    assert match(Command('sudo fakething', 'sudo: fakething: command not found'))
    assert not match(Command('sudo ls', ''))


# Generated at 2022-06-14 10:49:58.672799
# Unit test for function get_new_command
def test_get_new_command():
    # case 1
    command = "sudo: apt: command not found"
    assert get_new_command(command) == "sudo env \"PATH=$PATH\" apt"

    # case 2
    command = "sudo: apt-get: command not found"
    assert get_new_command(command) == "sudo env \"PATH=$PATH\" apt-get"

    # case 3
    command = "sudo: apt-get install: command not found"
    assert get_new_command(command) == "sudo env \"PATH=$PATH\" apt-get install"

# Generated at 2022-06-14 10:50:01.378477
# Unit test for function match
def test_match():
    command = "sudo: /home/agustin/bin/manage.py: command not found"
    assert match(command)



# Generated at 2022-06-14 10:50:03.800142
# Unit test for function match
def test_match():
    assert match(Command(script = 'sudo apt-get update',
                         output = 'sudo: apt-get: command not found'))


# Generated at 2022-06-14 10:50:07.996603
# Unit test for function match
def test_match():
    assert match(
        Command('sudo abc', 'sudo: abc: command not found')
    )
    assert not match(
        Command('sudo abc', 'sudo: abc: command')
    )
    assert not match(
        Command('sudo abc', 'sudo: not found')
    )



# Generated at 2022-06-14 10:50:20.893725
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_env_path import get_new_command
    from thefuck.types import Command

    assert get_new_command(Command('sudo vim', 'sudo: vim: command not found')) == u'env "PATH=$PATH" vim'
    assert get_new_command(Command('sudo gvim', 'sudo: gvim: command not found')) == u'env "PATH=$PATH" gvim'
    assert get_new_command(Command('sudo emacs', 'sudo: emacs: command not found')) == u'env "PATH=$PATH" emacs'

# Generated at 2022-06-14 10:50:24.798053
# Unit test for function match
def test_match():
    assert match(Command('sudo abc', output='sudo: abc: command not found'))
    assert not match(Command('sudo abc', output='sudo: abc: command'))


# Generated at 2022-06-14 10:50:26.553630
# Unit test for function match
def test_match():
    assert match(Command('sudo echo', ''))
    assert not match(Command('sudo ls', ''))



# Generated at 2022-06-14 10:50:30.077004
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('sudo pip install', 'sudo: pip: command not found')) == 'env "PATH=$PATH" pip install'

# Generated at 2022-06-14 10:50:34.330972
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get install python-suds', '', '/usr/local/bin/suds'))
    assert not match(Command('sudo apt-get install python-suds', '', 'NOTFOUND'))


# Generated at 2022-06-14 10:50:38.197947
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script = "sudo: adb: command not found"
    assert get_new_command(Command(script, '')) == "env \"PATH=$PATH\" adb"

# Generated at 2022-06-14 10:50:49.615274
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('sudo php') == 'sudo env "PATH=$PATH" php'

# Generated at 2022-06-14 10:50:54.012332
# Unit test for function match
def test_match():
    assert match(Command('echo hello', '', 'sudo: foo: command not found'))
    assert not match(Command('echo hello', '', ''))
    assert not match(Command('echo hello', '', 'ls: command not found'))
    

# Generated at 2022-06-14 10:50:57.894101
# Unit test for function get_new_command
def test_get_new_command():
    new_script = get_new_command(Command('sudo echo $PATH', 'sudo: echo: command not found', ''))
    assert new_script == 'env "PATH=$PATH" echo $PATH'


# Generated at 2022-06-14 10:51:12.096516
# Unit test for function match
def test_match():
    # Testing that match function works perfectly with the argument "rm devrepo"
    # The output of the command "sudo rm devrepo", when not run as root, is:
    # sudo: rm: command not found
    output = 'sudo: rm: command not found'
    assert match(Command('rm devrepo', output))

    # Testing that match function does not work with the argument "sudo rm devrepo"
    # The output of the command "sudo rm devrepo", when not run as root is:
    # rm: cannot remove 'devrepo': Permission denied

# Generated at 2022-06-14 10:51:17.120573
# Unit test for function match
def test_match():
    assert match(Command('sudo apt-get install thefuck', 'sudo: apt-get: command not found'))
    assert match(Command('sudo apt-get install thefuck', 'sudo: apt-get: command not found',
                         'env "PATH=$PATH" apt-get install thefuck')) == False

# Generated at 2022-06-14 10:51:20.538173
# Unit test for function match
def test_match():
    command = Command('sudo c3pos -v', stderr='sudo: c3pos: command not found')
    print(match(command))
    print(get_new_command(command))

# Generated at 2022-06-14 10:51:32.167404
# Unit test for function match
def test_match():
    assert not match(Command(script='sudo', output="sudo: env: command not found"))
    assert match(Command(script='sudo', output="sudo: env: command not found\n"))
    assert not match(Command(script='sudo', output="sudo: env: command not found\n"\
                                                   "sudo: env: command not found\n"))
    assert match(Command(script='sudo', output="sudo: env: command not found\n"\
                                          "sudo: env: command not found"))
    assert match(Command(script='sudo', output="sudo: env: command not found\n"\
                                          "sudo: env: command not found\n"))


# Generated at 2022-06-14 10:51:37.215297
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_env_path_command_not_found import get_new_command
    assert get_new_command('sudo apt get install') == u'env "PATH=$PATH" apt get install'
    assert get_new_command('sudo aptget install') == u'env "PATH=$PATH" aptget install'
    assert get_new_command('sudo apt: command not found') == u'env "PATH=$PATH" apt'

# Generated at 2022-06-14 10:51:40.431858
# Unit test for function get_new_command
def test_get_new_command():

    test_input = Command(
        script='sudo edit webpack.config.js',
        stdout='sudo: edit: command not found',
        stderr='',
        env={},)

    assert get_new_command(test_input) == 'env "PATH=$PATH" edit webpack.config.js'

# Generated at 2022-06-14 10:51:42.336814
# Unit test for function match
def test_match():
    assert match(Command('sudo vim /etc/hosts',
                         'sudo: vim: command not found'))
    assert not match(Command('sudo vim /etc/hosts', ''))


# Generated at 2022-06-14 10:52:05.604714
# Unit test for function match
def test_match():
    assert match(Command('sudo cp file destination',
          'sudo: cp: command not found',
          '/home/ishan'))
    assert not match(Command('sudo cp file destination',
           'cp: missing destination file operand after \'file\'',
           '/home/ishan'))



# Generated at 2022-06-14 10:52:09.337408
# Unit test for function match
def test_match():
    assert match(Command('sudo aptitude install mplayer', '''sudo: aptitude: command not found'''))
    assert not match(Command('sudo aptitude install mplayer', '''done'''))


# Generated at 2022-06-14 10:52:12.613530
# Unit test for function match
def test_match():
    assert match(Command('sudo foo', 'sudo: foo: command not found'))
    assert not match(Command('sudo foo', ''))

# Generated at 2022-06-14 10:52:20.692229
# Unit test for function get_new_command
def test_get_new_command():
    script = u'sudo ls'
    output = u'sudo: ls: command not found'
    command = type('Command', (object,), {'script': script, 'output': output})
    assert get_new_command(command) == u'env "PATH=$PATH" sudo ls'

    script = u'sudo ls -l'
    output = u'sudo: ls: command not found'
    command = type('Command', (object,), {'script': script, 'output': output})
    assert get_new_command(command) == u'env "PATH=$PATH" sudo ls -l'

# Generated at 2022-06-14 10:52:26.173547
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_env_not_set import get_new_command

    new_cmd = get_new_command(Command('sudo test_cmd', '', 'sudo: test_cmd: command not found'))

    assert new_cmd == 'env "PATH=$PATH" test_cmd'

# Generated at 2022-06-14 10:52:32.177040
# Unit test for function match
def test_match():
    assert match(Command('sudo echo hello', None, u'sudo: echo: command not found', 1))
    assert match(Command('sudo echo hello', None, u'sudo: echo: command not found', 1)) is None
    assert match(Command('sudo echo hello', None, u'sudo: echo: command not found', 1)) is None


# Generated at 2022-06-14 10:52:43.076090
# Unit test for function match
def test_match():
    # Things we expect to match
    assert match(Command('sudo apt-get upgrade', output='sudo: apt-get: command not found'))
    assert match(Command('sudo darktable', output='sudo: darktable: command not found'))
    assert match(Command('sudo apt-fast upgrade', output='sudo: apt-fast: command not found'))
    assert match(Command('sudo ls', output='sudo: ls: command not found'))
    assert match(Command('sudo sh -c "apt-get upgrade && apt-get dist-upgrade"', output='sudo: apt-get: command not found'))
    assert match(Command('sudo sh -c "apt-get upgrade && apt-get dist-upgrade"', output='sudo: apt-get: command not found'))

    # Things we expect NOT to match

# Generated at 2022-06-14 10:52:47.199977
# Unit test for function match
def test_match():
    command = Command('sudo beep', 'sudo: beep: command not found')
    assert match(command)

    command = Command('sudo beep', 'sudo: beep: Permission denied')
    assert not match(command)



# Generated at 2022-06-14 10:52:48.988771
# Unit test for function match
def test_match():
    assert match(Command('sudo ls', u'sudo: ls: command not found\r'))
    assert not match(Command('sudo ls', u'No command \'ls\' found, did you mean: Command \'cls\' from package \'util-linux\' (main)\r'))


# Generated at 2022-06-14 10:52:54.058408
# Unit test for function match
def test_match():
    test_command = Command(script = 'sudo notfound', output = 
                           'sudo: notfound: command not found')
    assert match(test_command) == None

    test_command = Command(script = 'sudo notfound', output = 
                           'sudo: notfound: command not found')
    assert _get_command_name(test_command) == 'notfound'



# Generated at 2022-06-14 10:53:38.254290
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo foo', 'sudo: foo: command not found')) == u'env "PATH=$PATH" foo'


enabled_by_default = False

# Generated at 2022-06-14 10:53:40.709867
# Unit test for function match
def test_match():
    assert match(Command('sudo echo "42"', ''))
    assert not match(Command('sudo -i', ''))



# Generated at 2022-06-14 10:53:46.165955
# Unit test for function match
def test_match():
    assert match(Command(script='sudo test', output='sudo: test: command not found'))
    assert match(Command(script='sudo test', output='sudo: test: command not fo')) == False
    assert match(Command(script='sudo test', output='test: command not found')) == False


# Generated at 2022-06-14 10:53:50.041240
# Unit test for function match
def test_match():
    assert match(Command('sudo foo', stderr='sudo: foo: command not found'))
    assert not match(Command('sudo foo', stderr='bar'))
    assert not match(Command('sudo foo', stderr=''))



# Generated at 2022-06-14 10:53:51.514863
# Unit test for function match
def test_match():
    assert match(Command('sudo vim', ''))


# Generated at 2022-06-14 10:53:54.071727
# Unit test for function match
def test_match():
    assert match(Command('sudo ifconfig',''))
    assert not match(Command('sudo ifconfig','sudo: ifconfig: command not found\n'))

# Generated at 2022-06-14 10:54:00.432458
# Unit test for function match
def test_match():
    assert match(Command('sudo yo', '')) is None
    assert match(Command('sudo yo', 'sudo: yo: command not found')) is not None
    assert _get_command_name(Command('sudo yo', 'sudo: yo: command not found')) == 'yo'



# Generated at 2022-06-14 10:54:06.329515
# Unit test for function get_new_command
def test_get_new_command():
	command = Command('sudo find /root/ -name "log" | xargs rm -rf', 'find: \'xargs\': No such file or directory\nsudo: xargs: command not found\n')
	assert get_new_command(command) == 'sudo env "PATH=$PATH" find /root/ -name "log" | env "PATH=$PATH" xargs rm -rf'

# Generated at 2022-06-14 10:54:13.699629
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    command_name = 'apt-get'
    right_command = 'sudo env "PATH=$PATH" apt-get update'
    new_command = get_new_command(Command('sudo ' + command_name + ' update',
                                          command_name + ': command not found\n'))
    assert new_command == right_command

    command_name = 'apt-get'
    right_command = 'sudo env "PATH=$PATH" apt-get update'
    new_command = get_new_command(Command('sudo ' + command_name + ' update',
                                          'sudo: ' + command_name + ': command not found\n'))
    assert new_command == right_command

# Generated at 2022-06-14 10:54:16.948736
# Unit test for function match
def test_match():
    assert match(Command('sudo nmap', 'sudo: nmap: command not found'))
    assert not match(Command('sudo nmap', ''))
    assert not match(Command('sudo ls', 'sudo: nmap: command not found'))
    assert not match(Command('echo', ''))


# Generated at 2022-06-14 10:55:56.536227
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('sudo cp', 'sudo: cp: command not found')
                           ) == 'env "PATH=$PATH" cp'

# Generated at 2022-06-14 10:56:04.526043
# Unit test for function match
def test_match():
    assert match(Command('sudo echo no',
                         'sudo: echo: command not found\nsudo: id: command not found\nsudo: whoami: command not found\nsudo: echo: command not found\nsudo: echo:\n'))
    assert not match(Command('sudo echo no',
                             'sudo: echo: command not found\nsudo: id: command not found\nsudo: whoami: command not found\nsudo: echo: command not found\nsudo: echo:\n'))


# Generated at 2022-06-14 10:56:07.469561
# Unit test for function match
def test_match():
    assert match(Command('sudo something', 'sudo: something: command not found'))
    assert not match(Command('pwd', ''))


# Generated at 2022-06-14 10:56:10.296291
# Unit test for function match
def test_match():
    match_command = Command("sudo apt install", "sudo: apt: command not found")
    assert match(match_command)



# Generated at 2022-06-14 10:56:17.555346
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.sudo_chown import get_new_command
    from thefuck.types import Command

    command=Command('sudo chown --recursive $USER:$USER .',
                    "sudo: chown: command not found\n")
    assert get_new_command(command) == 'sudo env "PATH=$PATH" chown --recursive $USER:$USER .'

# Generated at 2022-06-14 10:56:22.173429
# Unit test for function match
def test_match():
    match_command = Command('sudo this is command not found', '')
    assert match(match_command)

    no_match_command = Command('sudo ls', '')
    assert not match(no_match_command)

