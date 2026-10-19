

# Generated at 2022-06-13 11:29:28.900635
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from io import StringIO
    from ansible.module_utils.basic import AnsibleModule

    # Arrange
    # Mock method arguments
    cmd = "commando"
    shell = 1

    # Mock attributes
    becomecmd = 'sudo'
    flags = '-H -S -n'
    prompt = ''
    user = ''

    # Mock return values
    build_success_command_side_effect = "success"

    # Arrange
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    become = BecomeModule(module)

    # Mock
    become._build_success_command = lambda *args, **kwargs: build_success_command_side_effect

    # Act
    become.get_option = lambda *args, **kwargs: "fake"
    result

# Generated at 2022-06-13 11:29:36.297041
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader

    # Setup a BecomeModule object
    become_plugin = become_loader.get('sudo', class_only=True)()
    become_plugin.set_options(become_user='another_user')
    become_plugin.set_options(become_pass=True)
    become_plugin.set_options(become_exe='foo')
    become_plugin.set_options(become_flags='bar')

    # Test a command that requires shell
    command = become_plugin.build_become_command('echo "test"', True)
    assert command == 'foo bar -p "[sudo via ansible, key=%s] password:" -u another_user /bin/sh -c \'"echo \\"test\\""\'' % become_plugin._id

    # Test a command that

# Generated at 2022-06-13 11:29:42.995754
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os
    import ansible.plugins.become.sudo

    mock_instance = ansible.plugins.become.sudo.BecomeModule(None)

    # Test password pass
    # Test with a command, shell and beome_pass
    cmd = 'ls'
    shell = 'bash'
    become_pass = 'yeah@123'
    mock_instance._id = '1'
    result = mock_instance.build_become_command(cmd, shell)
    assert 'sorry' not in result.lower()
    assert '-h' in result.lower()
    assert '-s' in result.lower()
    assert '-p' in result.lower()
    assert '-n' in result.lower()
    assert '-u' in result.lower()
    assert shell in result.lower()
    assert cmd in result

# Generated at 2022-06-13 11:29:50.968322
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(dict(
        become_flags="-H -S -n",
        become_exe="sudo",
        become_user="ansible",
        become_pass=False,
        become_exe_cmd=True,
        executable=None
    ))

    cmd_test = """/bin/sh -c 'echo ~ && sleep 0'"""
    shell_cmd = "/bin/sh -c"
    result = """sudo -H -S -n -u ansible /bin/sh -c 'echo ~ && sleep 0'"""

    assert result == become.build_become_command(cmd_test, shell_cmd)



# Generated at 2022-06-13 11:30:01.497538
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Check if BecomeModule.build_become_command() raises no exception.
    bm = BecomeModule()
    bm._id = '123'
    bm.prompt = None
    bm.set_options({
        "become_user": "foo",
        "become_flags": "-H -S",
        "become_pass": "test"
    })
    bm.build_become_command("ls", True)

if __name__ == '__main__':
    import sys
    import ansible.plugins.become.sudo as sudo
    if sys.argv[-1] == 'test_BecomeModule_build_become_command':
        test_BecomeModule_build_become_command()
    else:
        sudo.main()

# Generated at 2022-06-13 11:30:10.714891
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    # Case 1:
    become_module._id = '1234'
    become_module.prompt = ''
    become_module.get_option = get_option_mocked
    cmd = 'ls -al'
    expected_cmd = "sudo  -H -S -n -p \"Sorry, try again.\" -u root /bin/sh -c 'echo BECOME-SUCCESS-1234; /bin/sh -c ls -al'"
    shell = '/bin/sh'

    actual_cmd = become_module.build_become_command(cmd, shell)

    assert(actual_cmd == expected_cmd)

    # Case 2:
    become_module._id = '4321'
    become_module.prompt = '[sudo via ansible, key=1234] password:'

# Generated at 2022-06-13 11:30:19.630887
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.get_option = mock_get_option


# Generated at 2022-06-13 11:30:29.415366
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(None, {})
    cmd = 'ls'
    shell = '/bin/sh'
    become.prompt = '[sudo via ansible, key=unit_test] password: '
    assert(become.build_become_command(cmd, shell) == 'sudo -H -S -p \'[sudo via ansible, key=unit_test] password: \' ls')
    become.become_flags = '-H -S'
    become.become_user = 'root'
    assert(become.build_become_command(cmd, shell) == 'sudo -H -S -p \'[sudo via ansible, key=unit_test] password: \' -u root ls')
    become.become_pass = 'pass'

# Generated at 2022-06-13 11:30:41.703561
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    cmd = 'bin/foobar -a "baz arg"'
    shell = 'sh'

    assert b.build_become_command(cmd, shell) == 'sudo -H -S -n -u root bin/foobar -a "baz arg"'
    # set options
    b.set_options({'become_exe': 'su', 'become_flags': '', 'become_pass': True, 'become_user': 'test'})
    assert b.build_become_command(cmd, shell) == 'su -p "[sudo via ansible, key=…] password:" -u test bin/foobar -a "baz arg"'

# Generated at 2022-06-13 11:30:51.126374
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    m = BecomeModule()
    cmd = 'echo %s' % 'test string'

    # if shell is bash, add 'exec' to the command that is passed to
    # sudo so that the variable expansions are done in the sudo environment
    shell = 'bash'
    m.prompt = ''
    m.get_option = lambda x: ''
    exec_cmd = 'exec ' if shell == 'bash' else ''
    assert m.build_become_command(cmd, shell) == 'sudo -H -S -n %sexec echo test string' % exec_cmd

    # if the --ask-become-pass flag is set, add the -p option to pass a
    # prompt string to sudo, and ensure no shell expansions in the sudo env

# Generated at 2022-06-13 11:31:06.233237
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    #Test with a command and a shell
    cmd_str = "echo test_cmd"
    cmd_list = ['"echo test_cmd"', '"sudo via ansible, key=1" password:', '-n', '-H', '-S', '-p', '"sudo via ansible, key=1" password:', '-u', '"test_user"', '"/bin/sh -c echo test_cmd"']
    cmd_list_2 = ['"echo test_cmd"', '"sudo via ansible, key=1" password:', '-H', '-S', '-p', '"sudo via ansible, key=1" password:', '-u', '"test_user"', '"/bin/sh -c echo test_cmd"']
    cmd_list_3

# Generated at 2022-06-13 11:31:20.788441
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test when become_pass is set as True
    become_module = become_module_initializer(become_pass=True)
    command_str = ' '.join(['sudo', '-H', '-S', '-n', '-p', '"%s"' % become_module.prompt, '-u', become_module.get_option('become_user'), become_module._build_success_command('ls -al', 'sh')])
    assert command_str == become_module.build_become_command("ls -al", "sh")

    # Test when become_pass is set as False
    become_module = become_module_initializer(become_pass=False)

# Generated at 2022-06-13 11:31:28.894124
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_plugin_obj = BecomeModule()
    become_plugin_obj._id = 'ABC'
    expected_result = 'sudo -H -S -n  -p "[sudo via ansible, key=ABC] password:"  -u test "echo hello"'
    result = become_plugin_obj.build_become_command('echo hello', None)
    assert result == expected_result, "Expected sudo command is: %s, Actual sudo command is: %s, Expected result %s" % (expected_result, result, result == expected_result)

# Generated at 2022-06-13 11:31:37.706596
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # subclasses BecomeBase
    assert issubclass(BecomeModule, BecomeBase)
    
    # executes the following command
    assert BecomeModule().build_become_command('ls', 'shell') == "sudo -H -S -n -p \"[sudo via ansible, key=] password:\" ls"
    assert BecomeModule().build_become_command('ls', 'shell') == "sudo -H -S -n -p \"[sudo via ansible, key=] password:\" ls"
    assert BecomeModule().build_become_command('ls', 'shell') == "sudo -H -S -n -p \"[sudo via ansible, key=] password:\" ls"
    # which becomes the following command

# Generated at 2022-06-13 11:31:41.700501
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule()
    module.become_pass = 'password'
    module.prompt = '[sudo via ansible, key=%s] password:' % module._id
    assert module.build_become_command("cmd", "") == 'sudo -p "%s" -u "" echo "BECOME-SUCCESS-cmd"' % (module.prompt)

# Generated at 2022-06-13 11:31:49.920925
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    cmd = ['/bin/ls', '-l']
    shell = '/bin/sh'
    become_pass = 'pwd'
    become_user = 'user'
    become_exe = 'sudo'
    become_flags = '-H -S'
    expected_cmd = 'sudo -H -S -u user -p "[sudo via ansible, key=ansible_become_pass] password:"  ansible_become_password=pwd /bin/sh -c \'/bin/ls -l\' 2>/dev/null'
    test_become = BecomeModule(None, None)
    test_become.set_options(become_pass=become_pass, become_user=become_user, become_exe=become_exe, become_flags=become_flags)

# Generated at 2022-06-13 11:31:59.658290
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = BecomeModule()
    cmd = 'ls'

    # Test case 1
    becomecmd.prompt = ''
    becomecmd.get_option = lambda x: None
    shell = 'sh'
    becomecmd.set_options(dict(become=True, become_user=None, become_method='sudo'))
    # Test case 1.1
    result = becomecmd.build_become_command(cmd, shell)
    assert result == 'sudo -H -S -n /bin/sh -c \'setfacl -m u:ansible:r-- /etc/shadow && LS_COLORS="" ls\' && sleep 0', result
    # Test case 1.2
    becomecmd.set_options(dict(become=True, become_user='root', become_method='sudo'))
    result = becomecmd.build_

# Generated at 2022-06-13 11:32:06.316841
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Without password, without user
    become = BecomeModule(dummy_for_test_become_options(
        become_flags='-H -S -n',
        become_exe='sudo',
        become_pass=None,
        become_prompt=None,
        become_user=None,
    ))

    assert become.build_become_command('/bin/true', shell=False) == \
        'sudo -H -S -n "/bin/true"'

    # With password, without user
    become = BecomeModule(dummy_for_test_become_options(
        become_flags='-H -S -n',
        become_exe='sudo',
        become_pass='mypassword',
        become_prompt=None,
        become_user=None,
    ))

    assert become.build_become

# Generated at 2022-06-13 11:32:16.590762
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = ('becomecmd')
    flags = ('becomeflags')
    prompt = ('prompthint')
    user = ('becomeuser')
    successcmd = ('successcmd')

    # Test Default values
    sudo = BecomeModule()
    sudo._id = 0
    command = sudo.build_become_command(successcmd, False)
    assert command == 'becomecmd -H -S -n successcmd'

    # Test with Prompt
    sudo = BecomeModule()
    sudo._id = 1
    sudo.become_pass = ('pass')
    sudo.get_option = lambda x: ''
    sudo._build_success_command = lambda x, y: successcmd
    command = sudo.build_become_command(successcmd, False)

# Generated at 2022-06-13 11:32:19.512629
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_cmd = BecomeModule()
    cmd_executed = 'echo $USER'
    shell = '/bin/sh'
    sudo_command = become_cmd.build_become_command(cmd_executed, shell)
    assert (sudo_command == 'sudo -H -S -n /bin/sh -c \'echo $USER\'')

# Generated at 2022-06-13 11:32:39.190468
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    sudo = BecomeModule(None)
    sudo.prompt = "password:"
    sudo.name = "sudo"
    sudo.flags = "-H -S -n"
    sudo.user = ""
    sudo.pass_prompt = "password:"

    assert sudo.build_become_command('echo 1', None) == 'sudo -H -S -n /bin/sh -c \'echo 1\''
    assert sudo.build_become_command('echo 1', '/bin/sh') == 'sudo -H -S -n /bin/sh -c \'echo 1\''
    assert sudo.build_become_command('echo 1', '/bin/ksh') == 'sudo -H -S -n /bin/ksh -c \'echo 1\''
    sudo.user = "ansible"

# Generated at 2022-06-13 11:32:48.756029
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    instance = BecomeModule()

    # default to sudo
    assert 'sudo -H -S -n' == instance.build_become_command(None, None)

    # default to another value when executable is not sudo
    instance.get_option = lambda x: 'not-sudo' if x == 'become_exe' else ''
    assert 'not-sudo -H -S -n' == instance.build_become_command(None, None)

    # propagate flags argument
    instance.get_option = lambda x: ('not-sudo', 'a b c')[x == 'become_exe']
    assert 'not-sudo a b c' == instance.build_become_command(None, None)

    # propagate become_pass argument

# Generated at 2022-06-13 11:32:55.193923
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # setup
    become_module = BecomeModule()
    become_module.get_option = lambda x: None
    become_module.prompt = None

    # check
    assert become_module.build_become_command('testcmd', 'testshell') == 'sudo -H -S -n testcmd'
    assert become_module.prompt is None

    become_module.get_option = lambda x: 'testsudo'
    assert become_module.build_become_command('testcmd', 'testshell') == 'testsudo -H -S -n testcmd'
    assert become_module.prompt is None

    become_module.get_option = lambda x: None
    become_module.prompt = 'testprompt'
    become_module.get_option = lambda x: 'testsudo'
    assert become_module.build

# Generated at 2022-06-13 11:32:57.613259
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # arranges
    sudo = BecomeModule()
    cmd = "/usr/bin/test"
    shell = "bash"

    # acts
    actual = sudo.build_become_command(cmd, shell)

    # asserts
    assert actual == "sudo -H -S -n /usr/bin/test"

# Generated at 2022-06-13 11:33:07.441747
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    become_module.prompt = '[sudo via ansible, key=%s] password:' % become_module._id
    become_module.get_option = lambda option: {
        'become_exe': 'sudo',
        'become_user': 'root',
        'become_pass': True,
        'become_flags': '-H -S -n'
    }[option]
    cmd = 'whoami'
    shell = '/bin/sh'
    assert become_module.build_become_command(cmd, shell) == 'sudo -H -S -p "%s" -u root "%s"' % (become_module.prompt, cmd)

# Generated at 2022-06-13 11:33:18.360846
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.module_utils.common.collections import ImmutableDict
    become = BecomeModule()
    become.get_option = lambda x: None

    cmd = 'command'
    shell = False
    assert become.build_become_command(cmd, shell) == 'sudo -H -S -n command'

    become.get_option = lambda x: 'becomeuser'
    assert become.build_become_command(cmd, shell) == 'sudo -H -S -n -u becomeuser command'

    become.get_option = lambda x: None
    assert become.build_become_command(cmd, shell) == 'sudo -H -S -n command'

    become.get_option = lambda x: 'become_flags'

# Generated at 2022-06-13 11:33:22.981923
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    become_module._id = '0d84810e89fa'
    assert become_module.build_become_command('my_command', 'my_shell') == "sudo  -p \"\[sudo via ansible, key=0d84810e89fa\] password:\"  'my_command'"

# Generated at 2022-06-13 11:33:31.482282
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(become_pass=None, become_exe=None)
    assert 'foo' == become._build_success_command('foo', False)
    assert 'foo' == become._build_success_command('foo', True)

    # With bash, everything needs to be quoted and the strings need to be joined
    assert '"foo" && echo BECOME-SUCCESS-aaejfhfmdpsmhfzpcexgbbpodpzkyjeu' == become._build_success_command('foo', True)

    # Without bash, everything needs to be quoted and the strings need to be joined

# Generated at 2022-06-13 11:33:41.837055
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    test_cmd1 = 'ls'
    test_cmd2 = '/bin/ls'
    test_res1 = 'sudo -u testuser ls'
    test_res2 = 'sudo -u testuser /bin/ls'

    # Override get_option
    def get_option_test(op):
        if op == 'become_user':
            return 'testuser'
        return None

    become.get_option = get_option_test
    res_cmd1 = become.build_become_command(test_cmd1, True)
    res_cmd2 = become.build_become_command(test_cmd2, False)

    assert res_cmd1 == test_res1
    assert res_cmd2 == test_res2

# Generated at 2022-06-13 11:33:55.882220
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Create a BecomeModule object
    become_module = BecomeModule()
    become_module._id = 'test'
    # Test build_become_command for no flags
    command_expected = 'sudo test'
    command_built = become_module.build_become_command('test', None)
    assert command_expected == command_built
    # Test build_become_command for -n flag
    become_module.set_become_option('become_flags', '-n')
    command_expected = 'sudo -p "[sudo via ansible, key=test] password:" -u %s test' % os.environ['LOGNAME']
    command_built = become_module.build_become_command('test', None)
    assert command_expected == command_built
    # Test build_become_command for --preserve

# Generated at 2022-06-13 11:34:21.045612
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.prompt = ''
    become.passwd = ''
    become.get_option = lambda name: None

    # default
    cmd = '/sbin/mycommand'
    assert become.build_become_command(cmd, None) == 'sudo /sbin/mycommand'

    become.get_option = lambda name: ''
    assert become.build_become_command(cmd, None) == 'sudo -H -S -n /sbin/mycommand'

    become.get_option = lambda name: 'username'
    assert become.build_become_command(cmd, None) == 'sudo -H -S -n -u username /sbin/mycommand'

    become.get_option = lambda name: '-n'
    assert become.build_become_command(cmd, None)

# Generated at 2022-06-13 11:34:31.292629
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule()
    user, flags, prompt, cmd = 'root', '', '', 'ls'
    testcmd = 'sudo -H -S -u root ls'
    assert (module.build_become_command(cmd, user, flags, prompt) == testcmd)
    flags, prompt = '-H -S -n', ''
    testcmd = 'sudo -H -S -u root ls'
    assert (module.build_become_command(cmd, user, flags, prompt) == testcmd)
    flags, prompt = '-H -S', '-p "password:"'
    testcmd = 'sudo -H -S -p "password:" -u root ls'
    assert (module.build_become_command(cmd, user, flags, prompt) == testcmd)
    cmd = '$HOME'
    test

# Generated at 2022-06-13 11:34:39.722625
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """
    Unit test for method build_become_command of class BecomeModule.
    """
    # Test default options
    become = BecomeModule()
    cmd = become.build_become_command(cmd='testcmd', shell='/test/shell')
    assert cmd == 'sudo -H -S -n /test/shell -c "testcmd"'

    # Test become_user
    become = BecomeModule()
    options = {'become_user': 'testuser'}
    become.set_options(options=options)
    cmd = become.build_become_command(cmd='testcmd', shell='/test/shell')
    assert cmd == 'sudo -H -S -n -u testuser /test/shell -c "testcmd"'

    # Test become_flags
    become = BecomeModule()

# Generated at 2022-06-13 11:34:46.648421
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule('/usr/bin/python', become_user='testuser', become_password='password')
    assert module.build_become_command('whoami', True) == 'sudo -H -S -p "[sudo via ansible, key=1qaz2wsx] password:" -u testuser whoami; (( $? != 0 )) && echo \'BECOME-SUCCESS-1qaz2wsx\' || echo \'BECOME-SUCCESS-1qaz2wsx\''

# Generated at 2022-06-13 11:35:00.196918
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    fake_play_context = {
        'become_user': 'foo',
        'become_pass': 'bar',
        'become_flags': '-f',
        'become_exe': 'sudo',
        'prompt': None
    }

    fake_loader = lambda: ''
    fake_shell = '/bin/bash'
    fake_command = 'ls -la'

    actual = BecomeModule(fake_play_context, fake_loader).build_become_command(fake_command, fake_shell)
    assert actual == 'sudo -f  -u foo /bin/bash -c \'echo %s; %s\' 2>/dev/null' % (fake_command, fake_command)


# Generated at 2022-06-13 11:35:08.777285
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = 'sudo'
    flags = '-n'
    user = 'subeasy'
    prompt = '[sudo via ansible, key=12345] password:'
    cmd = 'ls'
    shell = '/bin/bash'
    shell_escape = False

    _become_module = BecomeModule()
    _become_module.prompt = ''
    _become_module._id = '12345'
    _become_module._build_success_command = lambda cmd, shell: cmd
    assert _become_module.build_become_command(cmd, shell) == '%s %s -u %s %s' % (becomecmd, flags, user, cmd)


# Generated at 2022-06-13 11:35:17.405198
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Initial version of become_flags:  "-H -S"
    become_flags = "-H -S"

    # Check the case with become_flags "-H -S" and no become_user
    become_user = ""
    become_exe = "sudo"
    become_pass = ""
    host_variable_become = False
    become_user_variable_name = ""
    become_pass_variable_name = ""
    become_exe_variable_name = ""
    become_flags_variable_name = ""

    cmd = "uptime"
    shell = "bash"


# Generated at 2022-06-13 11:35:27.686608
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """Unit test for build_become_command of class BecomeModule."""
    becomecmd = 'sudo'
    flags = ''
    prompt = ''
    user = ''
    cmd = 'ls -l'
    shell_type = 'sh'
    success_cmd = 'echo BECOME-SUCCESS-mvhtunmewnlutpxquoojxrtjbxrhfomn; exit 0'
    expected = ' '.join([becomecmd, flags, prompt, user, success_cmd])

    def _build_success_command(cmd, shell_type):
        return success_cmd

    become = BecomeModule()
    become._build_success_command = _build_success_command
    assert expected == become.build_become_command(cmd, shell_type)

    flags = '-H -S'
    prompt

# Generated at 2022-06-13 11:35:34.522119
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    become_module.get_option = lambda *args, **kwargs: None
    become_module.prompt = None

    cmd = 'foo'
    shell = False

    # Without become_pass, become_flags or become_user
    become_module.set_options(dict())
    result = become_module.build_become_command(cmd, shell)
    assert result == 'sudo -H -S -n foo'

    # With become_pass
    become_module.set_options(dict(become_pass='bar'))
    result = become_module.build_become_command(cmd, shell)
    assert result == 'sudo -H -S -p "[sudo via ansible, key=] password:" bar'

    # With become_pass and become_flags
    become_module.set

# Generated at 2022-06-13 11:35:43.427120
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # These tests are not meant to be executed
    assert False

    # Tests for Module.build_become_command(cmd, shell):

    # Command with become options: Build the become command
    #    -- become_exe: sudo
    #    -- become_flags: -H -S -n
    #    -- become_pass: pass
    #    -- become_user: admin
    #
    #    command = "id"
    #    assert become_module.build_become_command("id", None) == "sudo -H -S -p \"$prompt\" -u admin $command"

    # Command without become options: Build the become command
    #    -- become_exe: sudo
    #    -- become_flags: None
    #    -- become_pass: None
    #    -- become_user: None
    #
    #

# Generated at 2022-06-13 11:36:14.614624
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    result = become.build_become_command('/bin/ls -la', '/sbin/nologin')
    assert result  ==  "sudo -H -S -n /bin/ls -la"

    become.prompt = '[sudo via ansible, key=abc] password:'
    result = become.build_become_command('/bin/ls -la', '/bin/sh')

# Generated at 2022-06-13 11:36:22.288276
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class become_module():
        def __init__(self):
            self.prompt = None
            self.get_option_called = 0
            self.return_values = {
                'become_user': None,
                'become_pass': None,
                'become_flags': None,
            }
        def get_option(self, key):
            self.get_option_called += 1
            return self.return_values[key]
        def _build_success_command(self, cmd, shell):
            return 'echo 1'

    become = become_module()
    # Test 1: No become user, become pass, and become flags
    expected_cmd = '%s echo 1' % (become.name)
    actual_cmd = become.build_become_command('echo 1', '/bin/sh')


# Generated at 2022-06-13 11:36:34.925258
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    m = BecomeModule()
    c = m.build_become_command(cmd='', shell='')
    assert c == ''

    m = BecomeModule()
    m._id = '123'
    c = m.build_become_command(cmd='', shell='')
    assert c == ''

    m = BecomeModule()
    m.get_option = lambda x: ''
    c = m.build_become_command(cmd='', shell='')
    assert c == ''

    m = BecomeModule()
    m._id = '123'
    m.get_option = lambda x: ''
    c = m.build_become_command(cmd='', shell='')
    assert c == ''

    m = BecomeModule()
    m._id = '123'

# Generated at 2022-06-13 11:36:42.061227
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomemodule = BecomeModule()

    # user is not provided, cmd is not provided
    becomemodule.get_option = lambda x: None
    assert becomemodule.build_become_command(None, None) is None

    # user is not provided, cmd is provided
    cmd = '/bin/sh'
    shell = '/bin/sh'
    expected = 'sudo -H -S /bin/sh'
    assert becomemodule.build_become_command(cmd, shell) == expected

    # user is provided, cmd is not provided
    becomemodule.get_option = lambda x: 'core' if x == 'become_user' else None
    assert becomemodule.build_become_command(None, None) is None

    # user is provided, cmd is provided


# Generated at 2022-06-13 11:36:50.370242
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """Test if output of build_become_command of class BecomeModule is expected."""
    m = BecomeModule()

# Generated at 2022-06-13 11:36:55.800316
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.prompt = 'prompt'
    become.get_option = lambda key: None
    assert become._build_success_command('ls', shell=False) == 'ls', '_build_success_command must add shell=False to command'
    assert become._build_success_command('ls', shell=True) == 'bash -c \'ls\'', '_build_success_command must create a new shell for command'
    assert become.build_become_command('ls', shell=False) == 'sudo ls -n', 'incorrect become command without flags or password'
    become.get_option = lambda key: 'my_flags' if key == 'become_flags' else None

# Generated at 2022-06-13 11:37:01.093672
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # create instance of class BecomeModule
    become_module = BecomeModule()

    # execute method build_become_command of class BecomeModule with some arguments
    ret = become_module.build_become_command('ping', 'bash')

    # check if the returned value is correct
    assert ret == 'sudo -H -S -n ping'

    # execute method build_become_command of class BecomeModule with some arguments
    ret = become_module.build_become_command('ping', 'bash', 'test_user')

    # check if the returned value is correct
    assert ret == 'sudo -H -S -n -u test_user ping'

    # execute method build_become_command of class BecomeModule with some arguments

# Generated at 2022-06-13 11:37:11.767136
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule()
    module.get_option = lambda x: None
    module._build_success_command = lambda cmd, shell: ' '.join(['`', cmd, '`'])

    # With no options
    cmd = module.build_become_command('foo', False)
    assert cmd == '[sudo] password: `foo`'

    # With become_pass
    module.get_option = lambda x: "abcd" if x == "become_pass" else None
    module._id = "1"
    cmd = module.build_become_command('foo', False)
    assert '`foo`' in cmd
    assert 'abcd' not in cmd
    assert '[sudo via ansible, key=1]' in cmd

    # With become_user
    module.get_option = lambda x: "joe"

# Generated at 2022-06-13 11:37:20.889286
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    import unittest
    import sys
    import os

    build_become_command_inputs = {
        'cmd': 'id',
        'shell': False,
        'success_cmd': '',
        'password': '',
        'become_exe': 'sudo',
        'become_flags': '-H -S -n',
        'become_user': 'root',
        'become_pass': 'pass',
        'prompt': '[sudo via ansible, key=%s] password:' % 'test_id',
        'becomecmd': 'sudo',
        'flags': '-H -S -p "test_id"',
        'user': 'root',
    }

    build_become_command_output = 'sudo -H -S -p "test_id" -u root id'

# Generated at 2022-06-13 11:37:26.687551
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    from ansible.plugins.loader import become_loader
    from ansible.inventory.host import Host

    become_module = become_loader.get('sudo')

    become_module.prompt = '[sudo via ansible, key=%s] password:' % '12345'

    become_module.set_options({
        'become_exe': '/usr/bin/sudo',
        'become_flags': '-H -S -n',
        'become_pass': '12345',
        'become_user': 'root',
    })

    cmd = 'cat /etc/hosts'
    host = Host()
    host.set_options({'ansible_user': 'myuser', 'ansible_connection': 'smart'})


# Generated at 2022-06-13 11:38:23.111189
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # simple validation of password, no flags
    become_plugin = BecomeModule(dict(prompt='password: '), dict(become_pass='testpassword'))
    cmd = become_plugin.build_become_command('/usr/bin/testcommand', '/bin/sh')
    assert '-p "password: "' in cmd

    # simple validation of password, no flags
    become_plugin = BecomeModule(dict())
    cmd = become_plugin.build_become_command('/usr/bin/testcommand', '/bin/sh')
    assert '-p "password: "' not in cmd

    # simple validation of password, with flags
    become_plugin = BecomeModule(dict(become_flags='-n'), dict(become_pass='testpassword'))

# Generated at 2022-06-13 11:38:29.756023
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule()
    bm.get_option = lambda x: None
    assert 'sudo  -H -S  -p "sudo via ansible, key=a password:"  -u user command' == bm.build_become_command('command', '')
    bm.become_user = 'user'
    bm._id = 'a'
    bm.become_pass = False
    assert 'sudo   -H -S  -u user command' == bm.build_become_command('command', '')
    bm.become_pass = True
    assert 'sudo   -H -S -p "sudo via ansible, key=b password:"  -u user command' == bm.build_become_command('command', '')
    bm.become_flags = '-i'

# Generated at 2022-06-13 11:38:39.055180
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = 'sudo'
    cmd_input = ('whoami\n',)
    cmd_output = 'whoami\n'

    # Setup become plugin
    sudo_plugin = BecomeModule(load_options=dict(become_exe=becomecmd, become_flags='-H -S -n', become_user='root'),
                               prompt=None, success_cmd=None, password=None)

    # Test for no input command
    assert sudo_plugin.build_become_command(None, False) is None

    # Test for empty input command
    assert sudo_plugin.build_become_command('', False) == ''

    # Test for non-empty input command without flags, prompt, etc
    assert sudo_plugin.build_become_command(cmd_input[0], False) == cmd_output

    # Test for non

# Generated at 2022-06-13 11:38:52.643900
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(load_options_module=False, become_method='sudo')
    cmd = 'cat /tmp/yay'
    assert become.build_become_command(cmd, None) == 'sudo -H -S -n cat /tmp/yay'

    cmd = '/bin/foo'
    assert become.build_become_command(cmd, None) == 'sudo -H -S -n /bin/foo'

    become = BecomeModule(load_options_module=False, become_method='sudo', become_user='jerry')
    assert become.build_become_command(cmd, None) == 'sudo -H -S -n -u jerry /bin/foo'

    become = BecomeModule(load_options_module=False, become_method='sudo', become_pass='yay')
    assert become.build

# Generated at 2022-06-13 11:38:59.526313
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_user = 'fakeuser'
    become_pass = 'fakepass'
    become_exe = 'fakeexe'
    become_flags = 'fakeflags'
    become_args = 'fakeargs'
    command = 'fakecommand'
    shell = 'fakeshell'

    module = BecomeModule()
    module._id = 'fakeid'

    module.get_option = MagicMock(return_value=become_user)
    module.get_option.side_effect = lambda x, default=False: {
        'become_user': become_user,
        'become_pass': become_pass,
        'become_exe': become_exe,
        'become_flags': become_flags,
        'become_args': become_args,
    }[x]

    module._build_success_command

# Generated at 2022-06-13 11:39:01.837075
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    b.prompt = None
    becomecmd = b.build_become_command('echo hello world', shell=True)
    assert becomecmd == 'sudo -H -S -n CMD_STDERR_TO_STDOUT echo hello world'


# Generated at 2022-06-13 11:39:12.595444
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    cmd = "/home/user/.local/bin/parent_script.sh"
    shell = 'zsh'
    become.prompt = None
    become.build_become_command(cmd, shell)

    assert become.prompt is None

    become.prompt = None
    become.build_become_command("", shell)

    assert become.prompt is None

    become.prompt = None
    become.build_become_command("", "")

    assert become.prompt is None

    become.prompt = None
    become.build_become_command(cmd, "")

    assert become.prompt is None

    become.prompt = None
    become.build_become_command("", shell)

    assert become.prompt is None

# Generated at 2022-06-13 11:39:18.832317
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    become_module = BecomeModule()

    becomecmd = become_module.get_option('become_exe') or become_module.name

    flags = become_module.get_option('become_flags') or ''
    prompt = ''
    if become_module.get_option('become_pass'):
        become_module.prompt = '[sudo via ansible, key=%s] password:' % become_module._id
        if flags:  # this could be simplified, but kept as is for now for backwards string matching
            flags = flags.replace('-n', '')
        prompt = '-p "%s"' % (become_module.prompt)

    user = become_module.get_option('become_user') or ''
    if user:
        user = '-u %s' % (user)

    cmd = become