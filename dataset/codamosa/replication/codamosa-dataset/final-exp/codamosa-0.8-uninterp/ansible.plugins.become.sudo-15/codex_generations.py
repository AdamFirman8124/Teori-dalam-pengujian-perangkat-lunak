

# Generated at 2022-06-13 11:29:29.495310
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os
    import glob
    import sys
    import shutil

    # Create a temp directory and write out a test ansible.cfg file
    # to use as the basis for our testing needs.
    temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
    if not os.path.isdir(temp_dir):
        os.mkdir(temp_dir)
    temp_ansible_cfg = os.path.join(temp_dir, 'ansible.cfg')
    shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../ansible.cfg'), temp_ansible_cfg)

    # Work in the temp directory
    prev_cwd = os.getcwd()

# Generated at 2022-06-13 11:29:38.121063
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    plugin_instance = BecomeModule()
    plugin_instance.prompt = ''
    plugin_instance._id = ''

    # Test without become_pass
    plugin_instance._task = {
        'become_method': 'sudo',
        'become_flags': ['-H', '-S', '-n'],
        'become_user': 'test_user',
    }
    result = plugin_instance.build_become_command('test cmd', False)
    assert result == 'sudo -H -S test_user -- test cmd'

    # Test with become_pass

# Generated at 2022-06-13 11:29:44.537918
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class Options(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    options = Options(become_exe='sudo', become_user='root', become_pass='pass', become_flags='')
    become = BecomeModule(Options(**options.__dict__))
    options.become_flags = '-H -S -n'
    become2 = BecomeModule(Options(**options.__dict__))
    options.become_flags = '-H -S'
    become3 = BecomeModule(Options(**options.__dict__))

    cmd = '/usr/bin/whoami'
    shell = '/bin/sh'


# Generated at 2022-06-13 11:29:54.505315
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible import context
    from ansible.module_utils._text import to_bytes

    context.CLIARGS = {'become_user': 'someuser', 'become_pass': 'become_password', 'become_exe': 'sudo'}
    become = BecomeModule()
    assert become.build_become_command('some_command', 'sh') == to_bytes('sudo -p "[sudo via ansible, key=somekey] password:" -u someuser some_command')
    become.prompt = None
    become.display.vvv = 1
    become.prompt = '[sudo via ansible, key=some_id] password:'

# Generated at 2022-06-13 11:30:03.599711
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # This code is only executed when this module is run directly.
    # It allows you to test your code by running: python become_exe.py
    class OptionsModule:
        def __init__(self, ansible_become_user, ansible_become_exe, ansible_become_flags, ansible_become_password):
            self.ansible_become_user = ansible_become_user
            self.ansible_become_exe = ansible_become_exe
            self.ansible_become_flags = ansible_become_flags
            self.ansible_become_password = ansible_become_password


# Generated at 2022-06-13 11:30:13.161357
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = AnsibleModule(argument_spec={'become_exe': dict(default=None, type='str'),
                                          'become_flags': dict(default=None, type='str'),
                                          'become_pass': dict(default=None, type='str'),
                                          'become_user': dict(default=None, type='str'),
                                          'become_method': dict(default='sudo', type='str')},
                           check_invalid_arguments=False,
                           bypass_checks=False)

    # result matches sudo

# Generated at 2022-06-13 11:30:20.926520
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule('test', {}, {})
    become_module._id = 'test'

    become_module.get_option = lambda x: None
    become_module._build_success_command = lambda x, y: 'success'
    cmd = become_module.build_become_command('test', 'shell')
    assert cmd == 'sudo success', 'Wrong command built'

    become_module.get_option = lambda x: 'sudo' if x == 'become_exe' else '-H -S -n' if x == 'become_flags' else None
    cmd = become_module.build_become_command('test', 'shell')
    assert cmd == 'sudo -H -S -n success', 'Wrong command built'


# Generated at 2022-06-13 11:30:31.008808
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_cmd = BecomeModule()

    result = become_cmd.build_become_command(cmd=None, shell=None)
    assert result == None

    result = become_cmd.build_become_command(cmd='ls /tmp', shell=None)
    assert result == 'sudo -H -S -n ls /tmp'

    result = become_cmd.build_become_command(cmd='ls /tmp', shell=None, become_user='centos')
    assert result == 'sudo -H -S -n -u centos ls /tmp'

    result = become_cmd.build_become_command(cmd='ls /tmp', shell=None, become_exe='/usr/bin/sudo')
    assert result == '/usr/bin/sudo -H -S -n ls /tmp'

    result = become_cmd.build_

# Generated at 2022-06-13 11:30:39.251886
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.errors import AnsibleError

    '''
    Provider of:
        - self.get_option(key)
        - self._id
        - self._build_success_command(cmd, shell)
    '''
    class mock_provide_option_id_success:
        def __init__(self):
            self.password = None
            self.record_failures = True
            self.prompted = False
            self.id = '123'
            self.name = None
            self.exe = None
            self.flags = None
            self.user = None

        def get_option(self, key):
            if key == 'become_pass':
                return self.password
            elif key == 'become_flags':
                return self.flags

# Generated at 2022-06-13 11:30:49.619570
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    args = dict(
        become_exe='sudo',
        become_user='root',
        become_pass='foobar',
        become_flags='-H -S -n',
        shell='/bin/sh',
        cmd='ls',
    )


# Generated at 2022-06-13 11:31:05.578538
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Passwords not provided
    become = BecomeModule(come_exe='sudo', become_user='root', become_pass='', become_flags='')
    cmd = become.build_become_command(cmd='cd /tmp', shell=True)
    assert 'sudo -H -S -n -u root "cd /tmp"' == cmd
    cmd = become.build_become_command(cmd='cd /tmp', shell=False)
    assert 'sudo -H -S -n -u root cd /tmp' == cmd

    # Passwords not provided
    become = BecomeModule(come_exe='sudo', become_user='root', become_pass='', become_flags='-E')
    cmd = become.build_become_command(cmd='cd /tmp', shell=True)

# Generated at 2022-06-13 11:31:16.079795
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become._id = 'test'
    become._display.verbosity = 3
    # initial checks
    assert become.build_become_command('ls /root', 'shell') == 'sudo -H -S -n ls /root'
    assert become.build_become_command('ls /root', 'command') == 'sudo -H -S -n ls /root'
    # check password prompt parsing
    become.prompt = None
    become.set_options(dict(become_pass='testpass'))
    assert become.build_become_command('ls /root', 'shell') == 'sudo -H -S -p "[sudo via ansible, key=test] password:" ls /root'

# Generated at 2022-06-13 11:31:21.691231
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule({}, 'ansible_become_module')
    become.prompt = ''

# Generated at 2022-06-13 11:31:31.919201
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    host = dict()
    t = BecomeModule(host)
    # cmd passed, shell False
    cmd = '/bin/ls -l /etc'
    assert t.build_become_command(cmd, False) == "sudo -H -S -n '/bin/ls -l /etc'"
    # cmd passed, shell True
    cmd = '/bin/ls -l /etc'
    assert t.build_become_command(cmd, True) == "sudo -H -S -n '/bin/ls -l /etc'"
    # cmd and password passed, shell False
    t.get_option = lambda x: x if x == "become_pass" else None
    cmd = '/bin/ls -l /etc'

# Generated at 2022-06-13 11:31:40.647629
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    class Options:
        def __init__(self):
            self.option_dict = {}

        def __contains__(self, item):
            return item in self.option_dict

        def __setitem__(self, key, value):
            self.option_dict[key] = value

        def get(self, key, default=None):
            return self.option_dict.get(key, default)

    class Runner:
        def __init__(self, become_flags, become_pass, become_user, become_exe):
            self.shell = '/bin/sh'
            self.become_flags = become_flags
            self.become_pass = become_pass
            self.become_user = become_user
            self.become_exe = become_exe
            self.host = 'localhost'
            self

# Generated at 2022-06-13 11:31:46.768530
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """
    Unit test for method `build_become_command` of class `BecomeModule`.
    """
    shell = 'sh'
    cmd = 'ls'
    expected_result = 'sudo -H -S -u root sh -c \'echo BECOME-SUCCESS-ijfjccrifrkfpbzkxsnxvxnldrtuhjat; %s\'' % cmd
    bm = BecomeModule()
    bm.become_cmd = 'sudo'
    bm.become_user = 'root'
    assert bm.build_become_command(cmd, shell) == expected_result

# Generated at 2022-06-13 11:31:51.229642
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    mock_args = {
        'become_user': '',
        'become_exe': '',
        'become_flags': '',
        'become_pass': '',
        'prompt': '[sudo via ansible, key=abc] password:',
        '_id': 'abc',
    }
    # Tests for empty parameters.
    m = BecomeModule(**mock_args)
    assert m.build_become_command('echo hi', True) == \
        "'echo hi' && echo 'BECOME-SUCCESS-abc'"
    assert m.build_become_command('echo hi', False) == \
        "echo hi; echo 'BECOME-SUCCESS-abc'"

    # Tests for non empty parameters.

# Generated at 2022-06-13 11:31:59.975953
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule(
        become_flags='-H -S -n',
        become_pass='dummypassword',
        become_user='dummyuser',
        become_exe=None,
        become_exe_used=None,
        become_prompt=None,
        become_ask_pass=None,
        prompt='[sudo via ansible, key=dummypassword] password:',
    )

    assert bm.build_become_command('dummycmd', 'shell') == 'sudo -H -S -p "[sudo via ansible, key=dummypassword] password:" -u dummyuser /bin/sh -c \'(dummycmd)\''

# Generated at 2022-06-13 11:32:06.485644
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class Options:
        become = True
        become_method = 'sudo'
        become_user = 'ansible-remote-user'
        become_pass = 'ansible-remote-user-password'
        become_exe = 'sudo'
        become_flags = '-H -S -n'
        prompt = '[sudo via ansible, key=%s] password:'

    class PlayContext:
        def __init__(self, **kwargs):
            self.become = Options.become
            self.become_method = Options.become_method
            self.become_user = Options.become_user
            self.prompt = Options.prompt
            self.remote_user = Options.become_user

    class BecomeModule:
        _id = 100
        DEFAULT_BECOME_PASS = False
       

# Generated at 2022-06-13 11:32:12.590185
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader

    become_plugin = become_loader.get('sudo')
    cmd = 'echo hello'
    shell = '/bin/sh'

    result = become_plugin.build_become_command(cmd, shell)

    print('test_BecomeModule_build_become_command:', result)

if __name__ == '__main__':
    test_BecomeModule_build_become_command()

# Generated at 2022-06-13 11:32:26.149846
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os
    import re
    import sys

    # Tests cases for AnsibleModule._get_option method

# Generated at 2022-06-13 11:32:34.901044
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # get a task for testing
    class Task:
        def __init__(self):
            self.args = ()
            self.su_user = None
            self.su_pass = None

    # get a become plugin for testing
    class BecomeModule:
        def __init__(self):
            self.name = 'test_BecomeModule'
            self.prompt = None
            self.get_option = __get_option

    # mock get_option method
    def __get_option(self, option):
        if option == 'become_user':
            options = ('root', None)
            return options[ord(self.name[-1]) % len(options)]
        elif option == 'become_pass':
            options = ('pass', None)

# Generated at 2022-06-13 11:32:45.435851
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_flags = "-H -S -n"
    become_user = 'bob'
    become_exe = 'sudo'
    become_pass = 'secret'
    prompt = '[sudo via ansible, key=some_id] password:'

    expected = 'sudo -H -S -p "%s" -u %s some_command' % (prompt, become_user)
    actual = BecomeModule(
        None,
        become_exe=become_exe,
        become_user=become_user,
        become_pass=become_pass,
        become_flags=become_flags,
    )._build_become_command('some_command')

    print("Expected:")
    print(expected)
    print("Actual:")
    print(actual)
    assert actual == expected

# Generated at 2022-06-13 11:32:50.008524
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    become_module.get_option = lambda _: None

    # No command
    assert become_module.build_become_command('', '/bin/sh') == 'sudo -H -S -n sh -c \\"echo BECOME-SUCCESS-jgfvqkavwtdjqjzbgqyqcqbazgzoyhbh; /sbin/ip a | sed -n \\\'/127.0.0.1/!p\\\'\\" 2>&1'

    become_module.get_option = lambda x: {'become_exe': 'become_exe', 'become_flags': 'become_flags', 'become_user': 'become_user'}[x]
    # No command
    assert become_module.build_become_

# Generated at 2022-06-13 11:32:55.186624
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module_instance = BecomeModule()
    #
    # no options, no flags
    #
    cmd = 'ls /root'
    expected = 'sudo -H -S -n ls /root'
    result = module_instance.build_become_command(cmd, '/bin/sh')
    assert result == expected, "expected=%s, result=%s" % (expected, result)
    #
    # no options, some flags
    #
    cmd = 'ls /root'
    expected = 'sudo -H -S -n ls /root'
    module_instance.options = {}
    module_instance.options['become_flags'] = '-H -n'
    result = module_instance.build_become_command(cmd, '/bin/sh')

# Generated at 2022-06-13 11:33:00.695981
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    cmd = 'echo 1'
    shell = '/bin/sh'
    _id = 'random_uuid'
    prompt = '[sudo via ansible, key=%s] password:' %  _id
    user = 'admin'
    becomecmd = 'sudo'

    # Build a class BecomeModule with no become_pass
    data = {
        'become_user': user,
        'become_exe': becomecmd,
        '_id': _id,
    }
    become_module = BecomeModule(None, data, None)
    result = become_module.build_become_command(cmd, shell)
    expected_result = ' '.join([becomecmd, '-H -S -n ', '', '-u %s' % user, become_module._build_success_command(cmd, shell)])

# Generated at 2022-06-13 11:33:09.585332
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule({'become_pass': None})
    become.name = 'sudo'
    become.prompt = '[sudo via ansible, key=%s] password:'
    become.get_option = lambda x: {'become_flags': '-H -S -n', 'become_pass': None, 'become_user': None}[x]

    assert become.build_become_command('command', 'shell') == 'sudo -H -S -n command'
    become.get_option = lambda x: {'become_flags': None, 'become_pass': None, 'become_user': None}[x]
    assert become.build_become_command('command', 'shell') == 'sudo command'

# Generated at 2022-06-13 11:33:16.846893
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    mock_self = BecomeModule([])
    mock_self.get_option = lambda x: None
    mock_self._id = "859087f1c02d"
    mock_self.prompt = None

    command = "ls"
    command_output = mock_self.build_become_command(command, None)

    assert command_output == 'sudo -H -S -n /bin/sh -c \'echo %s; %s\'' % (mock_self._id, command)


# Generated at 2022-06-13 11:33:26.800852
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.module_utils.six import binary_type, text_type
    from ansible.plugins.loader import become_loader

    with open(__file__) as f:
        cmd = [f.name]
        shell = '/bin/sh'
        prompt = '[sudo via ansible, key=12345678] password:'

        # Test become_flags = -H -S -n
        become_flags = '-H -S -n'
        sudo_test = become_loader.get('sudo')
        sudo_test.set_options({'become_pass': 'foobar', 'become_flags': become_flags})
        sudo_test.become_method = 'sudo'
        sudo_test.prompt = prompt
        sudo_test._id = '12345678'
        result = sudo_test.build_bec

# Generated at 2022-06-13 11:33:31.078064
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Setup instance
    fake_shell = 'sh'
    fake_cmd = 'fake_cmd'
    fake_become_exe = 'fake_become_exe'
    fake_become_flags = 'fake_become_flags'
    fake_become_pass = 'fake_become_pass'
    fake_become_kwargs = {
        'prompt' : '[sudo via ansible, key=%s] password:',
        'error_msg' : 'Sorry, try again.',
        'missing_key_msg' : "sudo: a password is required",
        '_id' : 'fake_id'
    }
    instance = BecomeModule()
    instance._shell = fake_shell
    instance.prompt = None
    instance.fail = fake_become_kwargs['error_msg']
   

# Generated at 2022-06-13 11:33:55.944760
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule(None)
    bm.get_option = lambda x: None
    bm.get_option.__dict__['become_user'] = None
    bm.get_option.__dict__['become_pass'] = None
    bm.get_option.__dict__['become_exe'] = None
    bm.get_option.__dict__['become_flags'] = None
    bm.get_option.__dict__['become_method'] = None
    bm.get_option.__dict__['become_info'] = None
    bm.get_option.__dict__['become'] = None
    bm.get_option.__dict__['_id'] = "abcd1"

# Generated at 2022-06-13 11:34:07.783338
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = BecomeModule(play_context={})

    cmd = 'ls -l'
    assert becomecmd.build_become_command(cmd, shell=None) == 'sudo -H -S -n ls -l'
    assert becomecmd.build_become_command(cmd, shell=None) == 'sudo -H -S -n ls -l'

    becomecmd._options = {'become_exe': 'sudo'}
    becomecmd._options['become_flags'] = ''
    becomecmd._options['become_pass'] = ''
    assert becomecmd.build_become_command(cmd, shell=None) == 'sudo -H -S -n ls -l'

    becomecmd._options['become_flags'] = '-n'
    becomecmd._options['become_pass'] = 'dummy'
   

# Generated at 2022-06-13 11:34:16.367558
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.get_option = lambda x: True
    become.get_option.__dict__ = {'prompt': True}

    cmd1 = ['ls', '-l', '/tmp']
    cmd2 = ['ls', '-l', '/foo']

    # command
    assert become.build_become_command(cmd1, None) == '/bin/sh -c "PATH=$PATH:/usr/local/bin:/usr/bin:/bin PYTHONPATH=/foo/bar: PYTHON_PATH=/foo/bar: /usr/bin/python ls -l /tmp"'

    # command with sudo
    become.name = 'sudo'
    become.get_option = lambda x: False

# Generated at 2022-06-13 11:34:23.535881
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = BecomeModule()
    becomecmd.options = dict(become_exe='sudo', become_user='root', become_flags='-H -n', become_pass='')
    cmd = becomecmd.build_become_command("useradd foo", "None")
    assert cmd == 'sudo -H -n -u root /bin/sh -c "useradd foo"'
    cmd = becomecmd.build_become_command("useradd foo", "/bin/bash")
    assert cmd == 'sudo -H -n -u root /bin/bash -c "useradd foo"'
    cmd = becomecmd.build_become_command("useradd foo", "/bin/sh")
    assert cmd == 'sudo -H -n -u root /bin/sh -c "useradd foo"'

# Generated at 2022-06-13 11:34:33.488789
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.prompt = ''
    become.get_option = lambda x: None
    become._build_success_command = lambda cmd, shell: cmd
    cmd = 'ls -la'
    shell = '/bin/sh'
    assert become.build_become_command(cmd, shell) == 'sudo -H -S ls -la'

    become.get_option = lambda x: '-k -u USER' if x == 'become_flags' else None
    assert become.build_become_command(cmd, shell) == 'sudo -H -k -u USER -S ls -la'

    become.get_option = lambda x: 'root' if x == 'become_user' else None

# Generated at 2022-06-13 11:34:41.373412
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    assert 'sudo' == become_module.name

    cmd = ['ls', '-la']
    shell = '/bin/bash'

    built_cmd = become_module.build_become_command(cmd, shell)
    assert shell == become_module.cmd_shell
    assert ' '.join(cmd) == become_module.cmd_unmodified
    assert built_cmd == 'sudo -H -S -n /bin/bash -c "ls -la"'

    become_module.become_flags = '-H -S -n'
    become_module.become_user = 'user'
    become_module.become_pass = 'password'

    built_cmd = become_module.build_become_command(cmd, shell)

# Generated at 2022-06-13 11:34:47.529018
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule()

    # Test without become_* options
    result = module.build_become_command("command", "shell")
    assert result == "sudo -H -S -n command"

    # Test with become_exe, become_flags and become_user
    module.become_args = {'become_exe': "sudoexe", 'become_flags': "flags", 'become_user': "user"}
    result = module.build_become_command("command", "shell")
    assert result == "sudoexe flags -n -u user command"

    # Test with become_pass, become_exe, become_flags and become_user

# Generated at 2022-06-13 11:35:00.814041
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # Test when all of options are missing
    becomeModule = BecomeModule(dict(become_exe='', become_flags='', become_pass=False, become_user=''))
    assert becomeModule.build_become_command(['command'], 'shell') == 'sudo command'

    # Test when all of options are set
    becomeModule = BecomeModule(dict(become_exe='new_sudo', become_flags='-H -S', become_pass='true', become_user='newuser'))

# Generated at 2022-06-13 11:35:10.909255
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class Opt():
        def __init__(self, **entries):
            self.__dict__.update(entries)

    options = Opt(become_user='testuser',
                  become_exe='/path/to/bin/become',
                  become_pass='pass')
    sudo_plugin = BecomeModule()
    sudo_plugin.set_options(options)

    cmd = ['ls', '-l']

# Generated at 2022-06-13 11:35:19.222920
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # user supplied for 'become_user' option
    module = BecomeModule()
    module.get_option = lambda option: None
    module._build_success_command = lambda cmd, shell: cmd
    module._id = 'xyz'
    module.prompt = None

    # Default 'become_exe' is 'sudo'
    module.get_option = lambda option: 'user' if option == 'become_user' else None
    assert module.build_become_command("cmd", "shell") == "sudo -H -S -n -u user cmd"

    # Default 'become_flags' is '-H -S -n'
    module.get_option = lambda option: None
    assert module.build_become_command("cmd", "shell") == "sudo -H -S -n cmd"

    # Default '

# Generated at 2022-06-13 11:35:55.741428
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # Test setup
    ######################################################################

    # Plugin instance and options
    class Options():
        def __init__(self):
            self.become_exe = '/usr/bin/sudo'
            self.become_flags = '-H -S -n'
            self.become_user = 'root'
            self.become_pass = 'abc'
    options = Options()
    plugin = BecomeModule(plugin_options={})
    plugin.set_option('become_exe', options.become_exe)
    plugin.set_option('become_flags', options.become_flags)
    plugin.set_option('become_user', options.become_user)
    plugin.set_option('become_pass', options.become_pass)

    # Functions to be mocked
    #################################################################

# Generated at 2022-06-13 11:36:04.564439
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    become_module = BecomeModule()

    # Test with become_user and become_exe
    become_module.become_options = dict(become_user='user', become_exe='become_exe')
    test_cmd = 'test command'
    test_shell = 'test shell'
    command_result = become_module.build_become_command(test_cmd, test_shell)
    assert command_result == 'become_exe -u user test shell -c \'test command\''

    # Test with become_user, become_exe and become_flags
    become_module.become_options = dict(become_user='user', become_exe='become_exe', become_flags='-H -S -n')
    test_cmd = 'test command'
    test_shell = 'test shell'
    command_result

# Generated at 2022-06-13 11:36:12.306644
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    become_module.prompt = '[sudo via ansible, key=12345678] password:'
    become_module._id = '12345678'

    # test case without options
    cmd = "/usr/bin/foo bar baz"
    cmd_expected = 'sudo -p "%s" /usr/bin/python -c \'import os;cmd="foo bar baz";os.system(cmd);\'' \
        % (become_module.prompt)
    assert cmd_expected == become_module.build_become_command(cmd, True)
    cmd_expected = 'sudo -p "%s" /bin/sh -c \'foo bar baz;\'' % (become_module.prompt)
    assert cmd_expected == become_module.build_become_command(cmd, False)

# Generated at 2022-06-13 11:36:20.373204
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule(None, {})
    assert become_module._build_success_command('ls', 'shell') == 'ls\n'
    assert become_module.build_become_command('ls', 'shell') == 'sudo ls\n'
    become_module.options = {'become_exe': 'sudo', 'become_user': 'root', 'become_pass': None}
    assert become_module.build_become_command('ls', 'shell') == 'sudo -u root ls\n'
    become_module.options = {'become_exe': 'sudo', 'become_user': 'root', 'become_pass': '1234'}

# Generated at 2022-06-13 11:36:32.867954
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    '''
    Test for the method build_become_command of the class BecomeModule
    '''
    # Setting up the test objects
    module = BecomeModule()
    module.prompt = None
    module.get_option = lambda x: None
    assert module.build_become_command('ls -l', None) == 'sudo -H -S ls -l'
    # Setting the prompt
    module.prompt = '[sudo via ansible, key=532a10d095a9b0ee] password:'
    # Setting the options

# Generated at 2022-06-13 11:36:38.484378
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule()
    bm.set_options({
        'become_exe': 'test_exe',
        'become_flags': 'flag_1 flag_2',
        'become_pass': '',
        'become_user': 'test_user',
    })

    assert bm.build_become_command('', False) == 'test_exe flag_1 flag_2 -u test_user 9<>/dev/null'

# Generated at 2022-06-13 11:36:50.989786
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule('test')
    cmd = '/usr/bin/foo'
    shell = '/bin/sh'

    become.get_option = lambda option: None
    assert become.build_become_command(cmd, shell) == '/usr/bin/foo'

    become.get_option = lambda option: 'pwd' if option == 'become_pass' else None
    assert become.build_become_command(cmd, shell) == '/usr/bin/foo'

    become.get_option = lambda option: 'sudo' if option == 'become_exe' else None
    assert become.build_become_command(cmd, shell) == '/bin/sh -c "sudo -H -S -n  /usr/bin/foo"'


# Generated at 2022-06-13 11:36:57.537394
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(
        run_command_environ_update=dict(),
        become_pass='',
    )
    become_cmd = become.build_become_command(
        'cat /etc/issue',
        '/bin/bash',
    )
    assert become_cmd == 'sudo -H -S -n -p "Sorry, a password is required to run sudo:" cat /etc/issue'

    become = BecomeModule(
        run_command_environ_update=dict(),
        become_pass='',
        become_exe='sudo',
        become_user='root',
    )
    become_cmd = become.build_become_command(
        'cat /etc/issue',
        '/bin/bash',
    )

# Generated at 2022-06-13 11:37:07.864430
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test that the expected command is returned for the given values.
    # Args are input values for the method.
    # The first arg is the return value of get_option.
    # The second arg is the cmd argument of the method.
    # The third arg is the shell argument of the method.
    # The fourth arg is the expected returned value of the method.
    def test(get_option_return, cmd, shell, expected):
        import ansible.plugins.become.sudo as sudo
        b = sudo.BecomeModule()
        b.get_option = lambda option: get_option_return
        assert b.build_become_command(cmd, shell) == expected

    test({}, 'sh -c "echo -e test"', 'sh', 'sudo -H -S -n sh -c "echo -e test"')
    test

# Generated at 2022-06-13 11:37:17.659496
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import pytest

    from ansible.module_utils.six.moves import StringIO
    buf = StringIO()
    test_become_pass = '12345678'
    test_play_context = {'become_pass': test_become_pass}
    # Test with cmd
    sudo_module_instance = BecomeModule(load_options=dict())
    (sudo_cmd, sudo_prompt, sudo_success_cmd) = sudo_module_instance.build_become_command(cmd="echo Hello",
                                                                                          play_context=test_play_context,
                                                                                          shell='/bin/bash',
                                                                                          executable='/bin/bash',
                                                                                          buf=buf)

# Generated at 2022-06-13 11:38:20.995755
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    assert(become_module.build_become_command(["ls -la /tmp"], "/bin/sh") == "sudo ls -la /tmp")
    assert(become_module.build_become_command(["ls -la /tmp"], "powershell.exe") == "sudo ls -la /tmp")
    assert(become_module.build_become_command(["ls -la /tmp"], "") == "sudo ls -la /tmp")
    assert(become_module.build_become_command(["sudo ls -la /tmp"], "") == "sudo ls -la /tmp")

# Generated at 2022-06-13 11:38:28.379245
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:38:38.141035
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    def get_option(option):
        if option == 'become_exe':
            return 'sudo'
        if option == 'become_flags':
            return '-H -S -n'
        if option == 'become_pass':
            return False
        if option == 'become_user':
            return 'adam'

    become_module = BecomeModule()
    #print become_module.build_become_command(cmd='echo "ok"', shell='/bin/bash', get_option=get_option)
    print(become_module.build_become_command(cmd='echo "ok"', shell='/bin/bash', get_option=get_option))

# Generated at 2022-06-13 11:38:52.473527
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    become_module.prompt = ''
    become_module.exe = ''
    become_module.flags = ''
    become_module.sudo = True
    become_module.su = False
    become_module.pwd = False
    become_module.user = ''
    become_module.password = ''
    cmd = ''
    shell = ''
    cmd = become_module.build_become_command(cmd, shell)
    assert cmd == 'sudo -H -S -n'

    # Test sudo with prompt
    become_module.password = 'abc123'
    become_module._id = 'aaa'
    cmd = become_module.build_become_command(cmd, shell)

# Generated at 2022-06-13 11:39:07.821671
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Simple test: no password, no user
    module = BecomeModule({}, {})
    module.build_become_command(['echo', 'hello', 'world'], True)
    assert module.cmd == "sudo -H -S -n  /bin/sh -c 'echo hello world'"

    # Tests with user
    module = BecomeModule({'become_user': 'foo'}, {})
    module.build_become_command(['echo', 'hello', 'world'], True)
    assert module.cmd == 'sudo -H -S -n -u foo /bin/sh -c ' + "'echo hello world'"

    # Tests without no-tty
    module = BecomeModule({'become_flags': '-t'}, {})

# Generated at 2022-06-13 11:39:16.661936
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    result = become.build_become_command('ls /tmp', '/bin/sh -c')
    assert result == 'sudo -H -S -n ls /tmp', 'Test 1 did not pass'

    become.set_options(become_exe='become')
    result = become.build_become_command('ls /tmp', '/bin/sh -c')
    assert result == 'become -H -S -n ls /tmp', 'Test 2 did not pass'

    become.set_options(become_user='bob')
    result = become.build_become_command('ls /tmp', '/bin/sh -c')
    assert result == 'become -H -S -n -u bob ls /tmp', 'Test 3 did not pass'


# Generated at 2022-06-13 11:39:25.600965
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    cmd = 'echo "Hello" && echo "World"'
    shell = 'sh'
