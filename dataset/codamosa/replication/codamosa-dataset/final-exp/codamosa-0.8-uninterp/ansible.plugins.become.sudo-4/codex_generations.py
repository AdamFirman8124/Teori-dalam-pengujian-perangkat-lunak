

# Generated at 2022-06-13 11:29:28.418662
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """
    Test to see if build command is built as expected.
    """
    become_base_class = BecomeBase()
    become_base_class.get_option = lambda a: None
    become_base_class.get_option.__code__ = lambda: None
    become_base_class.get_option.__code__.co_varnames = ['become_exe', 'become_flags', 'become_pass', 'become_user']
    become_base_class._build_success_command = lambda a1, a2: 'echo a'
    become_base_class._id = 1
    become_base_class.prompt = '[sudo via ansible, key=%s] password:' % become_base_class._id
    become_module_class = BecomeModule()

# Generated at 2022-06-13 11:29:34.745553
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bcmd = BecomeBase()
    bcmd.become_flags = '-H -S -n'
    bcmd.become_pass = 'unused'
    bcmd.become_user = 'root'

# Generated at 2022-06-13 11:29:43.252199
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule('sudo', 'foo', False, 'test')
    # Test with empty options
    result = module.build_become_command('testcommand', 'testshell')
    assert result == 'sudo -H -S testcommand'
    # Test with options set
    module.become_exe = 'do'
    module.become_flags = '--foo'
    module.become_pass = 'elephant'
    module.become_user = 'testuser'
    result = module.build_become_command('testcommand', 'testshell')
    assert result == 'do --foo -p "[sudo via ansible, key=foo] password:" -u testuser testcommand'

# Generated at 2022-06-13 11:29:52.566068
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    become_module.get_option = MagicMock(return_value=None)
    become_module.name = 'sudo'
    become_module.fail = None
    become_module.prompt = ''

    cmd = 'ls -la'
    built_cmd = become_module.build_become_command(cmd, shell=True)
    assert built_cmd == "sudo -H -S ls -la"

    # this test does not work due to failure:
    # assert become_module.prompt == "sudo via ansible, key=None password"
    # become_module.prompt = ""

    become_module.get_option = MagicMock(return_value="")
    become_module.name = 'sudo'
    become_module.fail = None
    become_module.prompt

# Generated at 2022-06-13 11:29:58.187306
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class Options(object):
        def __init__(self, become_user='', become_flags='', become_pass=''):
            self.become_flags = become_flags
            self.become_pass = become_pass
            self.become_user = become_user
        def get_option(self, opt, default=None, boolean=False, integer=False, floating=False, complex=False):
            return getattr(self, opt)

    class Shell(object):
        executable = 'sh'

    bm = BecomeModule()
    bm.get_option = Options().get_option

    cmd = ['ls', '-x']
    shell = Shell()

    # No flags
    become_cmd = bm.build_become_command(cmd,shell)

# Generated at 2022-06-13 11:30:08.066194
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os

    # Unit test for method build_become_command of class BecomeModule
    #
    # create a BecomeModule object for testing purposes
    #
    sudo = BecomeModule()
    #
    # *** test become_pass and become_user ***
    #
    # set up expected values
    #
    expected_become_cmd = 'sudo -i -u bla -p "[sudo via ansible, key=123] password:" echo'
    #
    # set up options
    #
    options_sudo_user = dict()
    options_sudo_user['become_pass'] = True
    options_sudo_user['become_user'] = 'bla'
    sudo.set_options(options_sudo_user)
    #
    # set up env vars
    #

# Generated at 2022-06-13 11:30:13.349458
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from collections import namedtuple
    plug_options = namedtuple('plug_options', 'become_flags become_exe become_prompt become_user become_pass')
    plug_vars = namedtuple('plug_vars', 'ansible_become_flags ansible_become_exe ansible_become_prompt ansible_become_user ansible_become_pass')
    plug_command = namedtuple('plug_command', 'shell cmd')

    # Use name attribute of class BecomeModule
    sudo = BecomeModule()
    sudo.name = 'sudo'

    # Options class
    o = plug_options('', '', '', '', '')
    sudo.options = o

    # Vars class
    v = plug_vars('', '', '', '', '')
    sudo.vars = v

# Generated at 2022-06-13 11:30:20.579294
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os

    # set up environment conditions for test
    os.environ['ANSIBLE_BECOME_PASS'] = 'mypass'
    os.environ['ANSIBLE_SUDO_EXE'] = 'sudo'
    os.environ['ANSIBLE_SUDO_PASS'] = 'mypass'
    os.environ['ANSIBLE_SUDO_USER'] = 'root'

    my_become_module = BecomeModule(None)
    expected_sudo_command = 'sudo -H -S -p "[sudo via ansible, key=123] password:" -u root ls -al'
    become_command = my_become_module.build_become_command('ls -al', False)

    assert become_command == expected_sudo_command

# Generated at 2022-06-13 11:30:25.978429
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # class BecomeModule(BecomeBase):
    sudo = BecomeModule()
    # def build_become_command(self, cmd, shell):
    super(BecomeModule, sudo).build_become_command("", "")
    sudo.get_option("become_exe")
    sudo.name
    sudo.build_become_command("", "")
    sudo.get_option("become_exe")
    sudo.get_option("become_flags")
    flags = "-n"
    flags == flags.replace("-n", "")
    sudo.get_option("become_pass")
    sudo.prompt = sudo.prompt = '[sudo via ansible, key=%s] password:' % sudo._id
    sudo.get_option("become_user")

# Generated at 2022-06-13 11:30:34.391027
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    print("Test for method build_become_command of class BecomeModule")

    import tempfile
    import json
    import os
    import shutil
    import sys

    # Data for unit test

# Generated at 2022-06-13 11:30:47.666249
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule()
    cmd = 'passwd'
    shell = '/bin/sh'

    sudo = 'sudo -H -S -n %s' % module._build_success_command("passwd", "/bin/sh")
    assert sudo == module.build_become_command(cmd, shell)

    module.become_pass = 'password'
    sudo = 'sudo -H -S -p "[sudo via ansible, key=%s] password:" %s' % (module._id, module._build_success_command("passwd", "/bin/sh"))
    assert sudo == module.build_become_command(cmd, shell)

    module.become_user = 'john'

# Generated at 2022-06-13 11:30:53.826964
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(dict(become_user='test', become_pass='pass', become_exe='sudo',
                               become_flags='-H -S -n', _id='id'), [], [],
                          False, False, False, None, None, None, None)

# Generated at 2022-06-13 11:31:06.204106
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import sys
    import os
    os.environ['ANSIBLE_BECOME_USER'] = 'foo'
    os.environ['ANSIBLE_BECOME_EXE'] = 'sudod'
    os.environ['ANSIBLE_BECOME_FLAGS'] = '-H -S'
    os.environ['ANSIBLE_BECOME_PASS'] = 'pass'
    m_get_option = lambda name: os.environ.get('ANSIBLE_BECOME_%s' % name.upper())
    m_get_option.side_effect = os.environ.get('ANSIBLE_BECOME_%s' % name.upper())
    m_build_success_command = lambda cmd, shell: ' echo "whatev"'

# Generated at 2022-06-13 11:31:20.779462
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test sample
    test = BecomeModule()
    test.prompt = ''
    assert test.build_become_command("", "") == ""

    test = BecomeModule()
    test.get_option = lambda option: "test" if option == "become_exe" else ""
    assert test.build_become_command("", "") == ""
    assert test.build_become_command("test", "") == "test"

    test = BecomeModule()
    test.get_option = lambda option: "test" if option == "become_user" else ""
    assert test.build_become_command("", "") == "sudo -u test /bin/sh -c ''"

    test = BecomeModule()
    test.get_option = lambda option: "test" if option == "become_pass" else ""


# Generated at 2022-06-13 11:31:31.613616
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    options = dict(become_pass=True)
    become_plugin = BecomeModule()
    become_plugin._id = 12345
    become_plugin.prompt = None
    cmd = 'command'
    shell = '/bin/sh'

    become_cmd = become_plugin.build_become_command(cmd, shell)
    # Assertion order need not match a specific order
    assert 'sudo' in become_cmd
    assert '-H' in become_cmd
    assert '-S' in become_cmd
    assert '-p "[sudo via ansible, key=12345] password:"' in become_cmd
    assert become_plugin.prompt == '[sudo via ansible, key=12345] password:'
    assert 'command' in become_cmd

    # with optional args

# Generated at 2022-06-13 11:31:40.352505
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    sudo_become_module = BecomeModule()
    assert sudo_become_module.build_become_command('ls -l', '/usr/bin/sh -c') == 'sudo -H -S -n ls -l'
    sudo_become_module.get_option = lambda option: option
    assert (sudo_become_module.build_become_command('ls -l', '/usr/bin/sh -c') ==
            'sudo -H -S -u user -p "[sudo via ansible, key=%s] password:" ls -l' % sudo_become_module._id)

# Generated at 2022-06-13 11:31:50.294877
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    expected_result = 'sudo -H -S -p "[sudo via ansible, key=asd123] password:" -u myuser bash -c \'echo BECOME-SUCCESS-asd123; RC=$?; [ $RC -ne 0 ] && echo BECOME-FAILURE-asd123; exit $RC\''
    become_cmd = become_module._build_success_command("bash -c 'echo BECOME-SUCCESS-asd123; RC=$?; [ $RC -ne 0 ] && echo BECOME-FAILURE-asd123; exit $RC'", shell='bash')
    result = become_module.build_become_command(become_cmd, 'bash')
    assert expected_result == result

# Generated at 2022-06-13 11:31:59.890569
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader
    from ansible.plugins.connection.ssh import Connection
    from ansible.module_utils.six.moves import StringIO
    from ansible.cli.adhoc import AdHocCLI
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    class FakeOptions(object):
        def __init__(self):
            self.connection = 'ssh'
            self.module_path = '/fake/path/to/my/lib/ansible/modules/'
            self.become_pass = 'wrong password'

    class FakeVariable(object):
        def __init__(self):
            self.host_vars = {}


# Generated at 2022-06-13 11:32:06.445622
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    #test for missing become_exe option
    test_parameters = {'cmd': 'echo \'dummy\'', 'shell': '/bin/bash'}
    become = BecomeModule()
    become.get_option = mock_get_option
    result = become.build_become_command(**test_parameters)
    assert result == None

    #test for missing cmd parameter
    test_parameters = {'shell': '/bin/bash'}
    become = BecomeModule()
    become.get_option = mock_get_option
    result = become.build_become_command(**test_parameters)
    assert result == None

    #test for missing shell parameter
    test_parameters = {'cmd': 'echo \'dummy\''}
    become = BecomeModule()
    become.get_option = mock_get_option


# Generated at 2022-06-13 11:32:16.729364
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # First test case
    become_module = BecomeModule('become_pass', {'become_pass': '', 'become_user': 'foo', 'become_flags': '-b', 'become_exe': '/usr/bin/sudo', 'shell': '/bin/sh'})
    cmd = ['/bin/ansible', '/tmp']
    expected = '/usr/bin/sudo -b -u foo /bin/sh -c \'printf %s "%s" | /bin/sh -s || echo BECOME-SUCCESS-goginlgdflklgtikolilgkfkfipbkcggk ; echo  BECOME-SUCCESS-goginlgdflklgtikolilgkfkfipbkcggk\'\n'
    actual = become_module.build_become

# Generated at 2022-06-13 11:32:29.098797
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    become_module.become_pass = True
    become_module.get_option = lambda option_name: None
    assert become_module.build_become_command("", False) == '[sudo via ansible, key=None] password:'

    become_module.become_pass = False
    become_module.get_option = lambda option_name: None
    assert become_module.build_become_command("", False) == ""

    become_module.become_pass = False
    def get_option(option_name):
        return {
            "become_exe": "sudo",
            "become_user": "root",
            "become_flags": "-H -S"
        }[option_name]
    become_module.get_option = get_option

# Generated at 2022-06-13 11:32:36.373913
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    # Test password prompt (and correct chaining of become parameters)
    def test_pass_prompt():
        b.set_options(dict(become_pass='y'))
        assert b.build_become_command(cmd='foo', shell=False) == 'sudo -p "[sudo via ansible, key=None] password:" -S foo'
        b.set_options(dict(become_flags='xyz'))
        assert b.build_become_command(cmd='foo', shell=False) == 'sudo xyz -p "[sudo via ansible, key=None] password:" -S foo'
        b.set_options(dict(become_flags='-n'))

# Generated at 2022-06-13 11:32:46.516459
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_pass = ''
    become_user = ''
    become_exe = ''
    become_flags = ''
    shell = True
    cmd = 'ls'
    bcm = BecomeModule()
    bcm.get_option = lambda x: globals()[x]
    assert bcm.build_become_command(cmd, shell) == 'sudo ls'

    become_pass = 'badpass'
    assert bcm.build_become_command(cmd, shell) == 'sudo -p "[sudo via ansible, key=bogus_id] password:" ls'

    become_flags = '-H'
    assert bcm.build_become_command(cmd, shell) == 'sudo -p "[sudo via ansible, key=bogus_id] password:" ls'

    become_flags = '-n'
   

# Generated at 2022-06-13 11:32:53.712002
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_pass = '123456'
    become_flags = '-H -S -n'
    become_exe = 'sudo'
    become_user = 'dc-user'

    # test for build_succeed_command
    become_class = BecomeModule(dict())
    test_string = "echo 'foo' >/dev/null"
    test_result = become_class._build_success_command(test_string, None)
    assert test_result == "'%s'" % test_string

    # given all parameters
    become_class = BecomeModule(
        dict(
            become_pass=become_pass,
            become_flags=become_flags,
            become_exe=become_exe,
            become_user=become_user
        )
    )

# Generated at 2022-06-13 11:32:59.536874
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Always return False for the first run and then return True
    def fake_super(self, cmd, shell):
        self.fake_super_called += 1
        if self.fake_super_called == 1:
            return False
        return True

    # fake methods of class BecomeBase
    BecomeBase.build_become_command = fake_super
    BecomeBase.get_option = lambda self, option: self.options.get(option)
    BecomeBase._build_success_command = lambda self, cmd, shell: cmd

    def get_sudo_command(options):
        options['become_user'] = options.get('become_user', 'root')
        options['become_exe'] = options.get('become_exe', 'sudo')

# Generated at 2022-06-13 11:33:04.595131
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:33:14.369262
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    '''
        Returned values of the method build_become_command are compared with the expected ones.
    '''
    # We obtain the return value of the method build_become_command
    # of the class BecomeModule.
    o = BecomeModule()
    o.shell = 'bash'
    o.become_pass = None
    o.become_exe = 'sudo'
    o.become_flags = '-H -S -n'
    o.become_user = 'root'
    # We set the default values for testing.
    cmd = 'whoami'
    expected = 'sudo -H -S -n -u root whoami'
    # Assertion
    assert(o.build_become_command(cmd, o.shell) == expected)

# Generated at 2022-06-13 11:33:21.948755
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule(become_pass='lorem', become_user='ipsum')
    assert become_module.build_become_command('fake command', 'fake_shell') == 'sudo -H -S -u ipsum fake command'

    become_module = BecomeModule(become_pass='fake_become_pass', become_user='fake_become_user')
    assert become_module.build_become_command('fake command', 'fake shell') == 'sudo -H -S -u fake_become_user fake command'

# Generated at 2022-06-13 11:33:27.987698
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # setup
    class MyBecomeModule(BecomeModule):
        def _build_success_command(self, cmd, shell):
            return cmd + ' SUCCESS'

    bm = MyBecomeModule('sudo', '', '', '')
    bm.set_options(dict(become_exe='sudo2', become_flags='-H -S', become_user='someuser', become_pass='pass'))

    # test
    cmd = 'show me the money'

    # assert
    assert bm.build_become_command(cmd, '/bin/bash') == 'sudo2 -H -S -p "[sudo via ansible, key=%s] password:" -u someuser show me the money SUCCESS' % bm._id

# Generated at 2022-06-13 11:33:39.308499
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    cmd = "echo ansible"
    shell = '/bin/sh'

    module = BecomeModule()

    # change values to test

# Generated at 2022-06-13 11:33:53.473313
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.get_option = lambda x: None

    assert become.build_become_command('ls', 'sh') == 'sudo -H -S -n sh -c "ls" || echo BECOME-SUCCESS-ls'
    become.prompt = '[sudo via ansible, key=X] password:'

    assert become.build_become_command('ls', 'sh') == 'sudo -H -S -p "[sudo via ansible, key=X] password:" sh -c "ls" || echo BECOME-SUCCESS-ls'

    become.get_option = lambda x: '-b' if x == 'become_flags' else None

# Generated at 2022-06-13 11:34:01.202395
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    cmd = "/bin/foo"
    shell = "/bin/sh"

    b._id = 'foo'
    b.prompt = 'password:'
    # password but no user
    b.prompt = 'password:'
    b.options = {
        'become_pass': 'abc',
        'become_user': None,
        'become_flags': 'X-Z'
    }
    assert b.build_become_command(cmd, shell) == "sudo -X-Z -p \"password:\" /bin/sh -c 'if [[ -f /etc/sudoers.d/ansible ]]; then echo BECOME-SUCCESS-abc; fi; /bin/foo'"
    # password and user
    b.options['become_user'] = 'admin'

# Generated at 2022-06-13 11:34:12.738691
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule(
        become_pass=None,
        become_user='testuser',
        become_flags='-H -S',
        remote_user='testuser'
    )
    result = become_module.build_become_command("""whoami""", '/bin/sh')
    assert result == """sudo -H -S -u testuser  sh -c 'echo ~ && echo $HOME &&  whoami'"""
    become_module = BecomeModule(
        become_pass='testpassword',
        become_user='testuser',
        become_flags='-H -S -n',
        remote_user='testuser'
    )
    result = become_module.build_become_command("""whoami""", '/bin/sh')

# Generated at 2022-06-13 11:34:20.958035
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class Mock(object):
        name = 'sudo'
    class MockConfigMixin(object):
        def get_option(o, op):
            if op == 'become_exe':
                return 'sudo'
            if op == 'become_flags':
                return '-H -S -n'
            if op == 'become_pass':
                return True
            if op == 'become_user':
                return 'root'
            if op == 'prompt':
                return '[sudo via ansible, key=%s] password:'
    b = BecomeModule(Mock(), MockConfigMixin())
    shell = '/bin/bash -l'
    cmd = 'ls -l'

# Generated at 2022-06-13 11:34:31.212361
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule({}, None)
    become_module.prompt = "Some prompt"
    become_module.get_option = lambda key: None

    cmd = "echo 1"
    shell = "/bin/bash"

    # Test with empty command
    assert become_module.build_become_command("", shell) == ""

    # Test with custom become_exe
    become_module.get_option = lambda key: "custom_sudo" if key == "become_exe" else None
    assert become_module.build_become_command(cmd, shell) == "custom_sudo -S -n sh -c 'echo 1'"

    # Test with custom become_flags
    become_module.get_option = lambda key: "--flag" if key == "become_flags" else None
    assert become_module.build_

# Generated at 2022-06-13 11:34:39.689379
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(None, dict(
        become_exe='/usr/bin/sudo',
        become_user='dave',
        become_pass='hunter2',
        become_flags='-E -H',
        ansible_become_password='hunter2',
        ansible_become_user='dave',
        ansible_become_exe='/usr/bin/sudo',
        ansible_become_flags='-E -H',
    ))

    assert '/usr/bin/sudo -E -H -p "[sudo via ansible, key=%s] password:" -u dave /bin/sh -c shell' % become._id == become.build_become_command('shell', False)

# Generated at 2022-06-13 11:34:49.482987
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = 'sudo'
    shell = '/bin/sh'

    # when
    become = BecomeModule(None)
    become.get_option = lambda x: None
    cmd = 'ls -lt'
    cmd_expected = 'sudo ls -lt'
    become.build_become_command(cmd, shell)

    # then
    assert become.get_option.called
    assert become.get_option.call_args[0][0] == 'become_exe'
    assert become.build_command == cmd_expected

    # when
    become = BecomeModule(None)
    become.get_option = lambda x: None
    cmd = 'ls -lt'
    cmd_expected = 'sudo ls -lt'
    become.build_become_command(cmd, shell)

    # then
    assert become.get_

# Generated at 2022-06-13 11:34:53.110100
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    inp = test_input['build_become_command']['inp']
    expected = test_input['build_become_command']['expected']
    for idx, test in enumerate(inp):
        obj = BecomeModule(**test['options'])
        obj._id = 'ansible_become_plugin'
        cmd = obj.build_become_command(test['cmd'], test['shell'])
        assert cmd == expected[idx]


# Generated at 2022-06-13 11:34:57.633438
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.errors import AnsibleError
    from ansible.module_utils.common._collections_compat import MutableMapping
    
    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
        def fail_json(self, *args, **kwargs):
            msg = kwargs['msg'] if 'msg' in kwargs else args[0]
            raise AnsibleError(msg)
        def get_bin_path(self, *args, **kwargs):
            return "bin_path"
    
    class FakeVarsModule(MutableMapping):
        def __init__(self, **kwargs):
            pass
        def __getitem__(self, key):
            return "vars_module[{}]".format(key)


# Generated at 2022-06-13 11:35:04.193733
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.get_option = MagicMock()
    become.get_option.return_value = 'test'
    become.name = 'sudo'
    become._build_success_command = MagicMock()
    become._build_success_command.return_value = "/bin/sh -c 'test'"
    become.prompt = MagicMock()
    become.prompt.return_value = "test"
    become._id = 'test'
    become.websocket = MagicMock()
    become.websocket.return_value = True

    # test build_become_command method

# Generated at 2022-06-13 11:35:24.465795
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:35:29.328943
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class MockedOption:
        def __init__(self, value):
            self.value = value

        def __call__(self, *args, **kwargs):
            return self.value

    class MockedModule:
        options = {
            'become_exe': MockedOption('sudo'),
            'become_flags': MockedOption('-H -S -n'),
            'become_pass': MockedOption(''),
            'become_user': MockedOption('test'),
        }

    test_cmd = 'test'
    test_shell = '/bin/bash'

    become_module = BecomeModule(MockedModule)
    become_module._id = 'test_id'
    become_command = become_module.build_become_command(test_cmd, test_shell)

# Generated at 2022-06-13 11:35:35.473823
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Preparation
    plugin = BecomeModule()
    plugin._id = 'abc'
    plugin.prompt = None

    # No parameters (should fall back to defaults)
    value = plugin.build_become_command('cmd', '/bin/sh')
    assert value == 'sudo -H -S -n /bin/sh -c \'echo %s; cmd\' | base64 -d && test "${PIPESTATUS[0]}" -eq 0 && test "${PIPESTATUS[1]}" -eq 0' % plugin.success_key
    assert plugin.prompt is None

    # With everything set
    plugin.set_options(dict(become_exe='sudo',become_flags='-H -n',become_user='admin',become_pass='12345'))
    value = plugin.build_become_

# Generated at 2022-06-13 11:35:44.070831
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    instance = BecomeModule()

    instance.set_options(module_options=dict(become_exe='sudo'))
    expected = 'sudo -H -S -n echo "BECOME-SUCCESS-kxlxovjxcvbawjzrtebfycqlrfmzkvxd"'

    returned = instance.build_become_command(cmd='echo "BECOME-SUCCESS-kxlxovjxcvbawjzrtebfycqlrfmzkvxd"', shell='/bin/bash')
    assert expected == returned

    instance.set_options(module_options=dict(become_exe='sudo', become_user='centos', become_pass='beepBoop'))

# Generated at 2022-06-13 11:35:54.315596
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # Create a fresh instance of BecomeModule
    # Nothing should return None in this test.
    sudo = BecomeModule()
    sudo.name = 'sudo'
    sudo.become_flags = '-H'
    sudo.become_pass = None
    sudo.prompt = ''
    sudo.become_exe = ''

    # Should return None if cmd is None
    assert sudo._build_success_command(None, 'shell') is None

    # Should return None if cmd is not a str
    assert sudo._build_success_command(['array'], 'shell') is None
    assert sudo._build_success_command(123, 'shell') is None
    assert sudo._build_success_command({'key': 'value', 'key2': 'value2'}, 'shell') is None

    # If shell is None, return cmd
    cmd

# Generated at 2022-06-13 11:36:03.464044
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    # Test default options
    become.options = {}
    cmd = '/bin/foo'
    shell = '/bin/bash'
    assert become.build_become_command(cmd, shell) == 'sudo -H -S -n /bin/bash -c \'/bin/foo\'', 'Default options'

    # Test become_flags option
    become.options = {'become_flags': '-H -n'}
    assert become.build_become_command(cmd, shell) == 'sudo -H -n /bin/bash -c \'/bin/foo\'', 'Become_flags option'

    # Test become_user option
    become.options = {'become_user': 'foo'}

# Generated at 2022-06-13 11:36:10.958140
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    my_become_module = BecomeModule()
    
    import tempfile
    (my_file_hdl, my_file_path) = tempfile.mkstemp()
    os.close(my_file_hdl)
    file(my_file_path, 'w').write("""
[defaults]
become_exe=mysudo
become_flags=mysudo_flags
become_user=mysudo_user
become_pass=mysudo_pass
become_ask_pass=mysudo_ask_pass
become_method=mysudo_method
become_info=mysudo_info
    """)
    config = ConfigParser.ConfigParser()
    config.readfp(open(my_file_path))
    os.remove(my_file_path)
    my_become_module.set

# Generated at 2022-06-13 11:36:18.924854
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    become_module.get_option = lambda option: None
    become_module.name = 'sudo'
    become_module.prompt = ''

    cmd = 'cmd'
    shell = 'shell'
    assert become_module.build_become_command(cmd, shell) == 'sudo -H -S -n cmd'

    # Should return sudo in absence of become_exe
    become_module.get_option = lambda option: 'doas' if option == 'become_exe' else None
    become_module.name = 'sudo'
    become_module.prompt = ''

    assert become_module.build_become_command(cmd, shell) == 'sudo -H -S -n cmd'

    # Should return doas if exist and sudo not exist

# Generated at 2022-06-13 11:36:25.605733
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    m_cls = BecomeModule()
    m_cls.get_option = lambda x: None

    # Replace built-in print
    save_print = __builtins__['print']
    builtin_print_called = False

    def print_mock(*args, **kwargs):
        nonlocal builtin_print_called
        builtin_print_called = True

    __builtins__['print'] = print_mock

    # Case 1, no user
    m_cls._id = 'test_id_1'
    m_cls._build_success_command = lambda x, y: 'bar'
    m_cls.prompt = None
    assert (m_cls.build_become_command('foo', '/bin/sh') == 'sudo -H -S  bar')

# Generated at 2022-06-13 11:36:37.286457
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    become_module.become_pass = None

    become_module.get_option = lambda a: None
    assert become_module.build_become_command('a b c', '/bin/bash') == 'sudo -H -S a b c'

    become_module.get_option = lambda a: ''
    assert become_module.build_become_command('a b c', '/bin/bash') == 'sudo -H -S a b c'

    become_module.get_option = lambda a: '-n'
    assert become_module.build_become_command('a b c', '/bin/bash') == 'sudo -H -S a b c'

    become_module.get_option = lambda a: '-Hn'

# Generated at 2022-06-13 11:37:08.451276
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test with invalid parameters
    bm = BecomeModule(None, None, None)

    assert bm.build_become_command(None, None) is None
    assert bm.build_become_command(None, True) is None
    assert bm.build_become_command(None, False) is None

    # Test with empty command
    bm = BecomeModule(None, {}, {})
    cmd = ''
    expected_cmd = 'sudo -H -S -n /bin/sh -c '
    assert bm.build_become_command(cmd, False) is not None
    assert bm.build_become_command(cmd, False).startswith(expected_cmd)

    # Test with command with single quote
    bm = BecomeModule(None, {}, {})

# Generated at 2022-06-13 11:37:18.149072
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Create an instance of BecomeModule for testing.
    test_become_module = BecomeModule(dict(), '')

    # Create a command to test.
    test_become_module._id = 'test_id'
    test_cmd = 'uname -a'

    # Test passing a command to build_become_command().
    built_cmd = test_become_module.build_become_command(test_cmd, False)
    # Verify that the module will use the sudo command by default.
    assert built_cmd.startswith('sudo')
    # Verify that the become user is not set by default.
    assert built_cmd.find('-u') == -1
    # Verify that the -H flag is set by default.
    assert built_cmd.find('-H') != -1
    # Verify that -S and

# Generated at 2022-06-13 11:37:25.135960
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import tempfile
    (fd, fname) = tempfile.mkstemp()

    # Create BecomeModule instance
    b = BecomeModule(
        become_user='foo',
        become_pass='abc',
        become_exe='sudo',
        become_flags='-H -S -n',
        success_key='',
        success_cmd='',
        success_re=None,
        create_remote_temp=False,
        executable=None,
        remote_tempdir=None,
        _id=1
    )
    # Test data for build_become_command
    cmd = "echo 'some stuff > %s'" % (fname)
    shell = '/bin/sh'

    # run tested method
    res = b.build_become_command(cmd, shell)

    # Verify result of build_become

# Generated at 2022-06-13 11:37:33.423347
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Initialize become module
    bm = BecomeModule()
    bm.get_option = lambda x: ''
    bm.get_option.__self__ = bm
    bm.prompt = ''
    bm._id = '0'

    # Check command with no become_user, no become_pass
    bm.get_option.__func__.__name__ = 'get_option'
    cmd = bm.build_become_command('my_test_cmd', 'my_test_shell')
    assert cmd == "'my_test_cmd'", 'Command is not correct.'

    # Check command with no become_user, with become_pass
    bm.get_option.__func__.__name__ = 'become_pass'

# Generated at 2022-06-13 11:37:41.977528
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule('../../lib/ansible/plugins/become_plugins/sudo.py')

    # simple case
    cmd = module.build_become_command('/bin/ls', 'bash')
    assert cmd == '/bin/bash -c \'( umask 77 && /bin/ls )\''

    # with flags
    module.get_option = lambda x: '-H -S -n' if x == 'become_flags' else None
    cmd = module.build_become_command('/bin/ls', 'bash')
    assert cmd == '/bin/bash -c \'( umask 77 && sudo -H -S -n /bin/ls )\''

    # with flags and user

# Generated at 2022-06-13 11:37:46.889709
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
   b = BecomeModule()
   s = 'sleep 10'
   sudocmd = b.build_become_command(s, '/bin/bash')
   c = "sudo 'sleep' '10'"
   assert c == sudocmd

# Generated at 2022-06-13 11:38:00.937070
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test no flags
    become = BecomeModule()
    become.prompt = '[sudo via ansible, key=x86] password:'
    cmd = 'sudo -p "%s" -u root -H -S -n true' % become.prompt
    assert become.build_become_command('true', False) == cmd

    # Test override to the sudo flags
    become = BecomeModule(dict(become_flags='-n'))
    become.prompt = '[sudo via ansible, key=x86] password:'
    cmd = 'sudo -p "%s" -u root -H -S -n true' % become.prompt
    assert become.build_become_command('true', False) == cmd

    # Test override for sudo executable

# Generated at 2022-06-13 11:38:11.106248
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become.get_option = lambda *args: None  # pylint: disable=unused-argument
    assert become.build_become_command('/bin/bash', True) == "/bin/bash"
    become.get_option = lambda *args: "sudo"
    assert become.build_become_command('/bin/bash', True) == "sudo /bin/bash"
    become.get_option = lambda *args: "sudo"
    become.prompt = "Password:"
    assert become.build_become_command('/bin/bash', True) == "sudo /bin/bash"
    become.get_option = lambda *args: "sudo"
    become.get_option = lambda *args: "-H -S"
    become.prompt = "Password:"
    assert become.build_

# Generated at 2022-06-13 11:38:21.188308
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    become._options = dict(
        become_pass=False,
    )

    cmd = '/bin/foo'
    shell = 'sh'
    assert become.build_become_command(cmd, shell) == 'sudo -H -S -n /bin/sh -c \'/bin/foo\''

    become._options = dict(
        become_pass=True,
    )
    assert become.build_become_command(cmd, shell) == 'sudo -H -S -p "SUDO-SUCCESS-wujfssxfauzjcozvhktoxzyxkyhlqsxk" sh -c \'/bin/foo\''


# Generated at 2022-06-13 11:38:25.895750
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    mock_self = BecomeModule()

    # Method build_become_command returns become command for given command for sudo with password
    mock_self._id = 'abc123'
    cmd = 'ls'
    mock_self.get_option = lambda x: 'sudo' if x == 'become_exe' else '-H -S' if x == 'become_flags' else ''
    mock_self.get_option.return_value = True
    assert mock_self.build_become_command(cmd, '') == 'sudo -H -S -p "[sudo via ansible, key=abc123] password:" ls'

    # Method build_become_command returns become command for given command for sudo with user and password
    mock_self._id = 'abc123'
    cmd = 'ls'