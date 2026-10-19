

# Generated at 2022-06-13 08:31:54.000792
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import mock
    import ansible.playbook.task

    test_play_context = PlayContext()
    test_play_context.only_tags = set()
    test_play_context.skip_tags = set()
    test_play_context.start_at_task = "test_play"
    test_play_context.verbosity = 5

    test_task = ansible.playbook.task.Task()
    test_task.tags = "remote_user"
    test_task.only_tags = set(["foo", "bar"])
    test_task.skip_tags = set(["baz", "qux"])
    test_task.start_at_task = "test_task"
    test_task.verbosity = 1
    test_task.delegate_to = "test_delegate"
    test

# Generated at 2022-06-13 08:32:01.812375
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    import unittest
    import sys
    # Do something useful here
    test = unittest.TestCase('__init__')
    # test = unittest.TestCase()
    # test.assertEqual(PlayContext().set_attributes_from_plugin('name'), 'name')
    # test.assertEqual(PlayContext().set_attributes_from_plugin(), 'PlayContext')
    # test.assertEqual(PlayContext('name').set_attributes_from_plugin(), 'PlayContext')
    # test.assertEqual(PlayContext('name', 'password').set_attributes_from_plugin(), 'PlayContext')
    test.assertEqual(PlayContext('name', 'password', 'connection_lockfd').set_attributes_from_plugin(), 'PlayContext')

# Generated at 2022-06-13 08:32:06.031790
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    datas = {'foo':'bar'}
    settings = PlayContext(datas)
    settings.set_attributes_from_plugin('test')
    assert settings.settings['foo'] == 'bar'


# Generated at 2022-06-13 08:32:12.273202
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play = namedtuple('play', 'force_handlers')
    play_instance = play(force_handlers=None)
    passwords = {}
    connection_lockfd = None
    playcontext_instance = PlayContext(play_instance, passwords, connection_lockfd)
    assert isinstance(playcontext_instance, PlayContext)

# Generated at 2022-06-13 08:32:19.187170
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    # set_attributes_from_plugin() negative tests
    >>> test_play_context = PlayContext(play=None)
    >>> test_play_context.set_attributes_from_plugin(None)
    >>> test_play_context._attributes['_timeout']
    30

    # set_attributes_from_plugin() positive tests
    >>> test_play_context.set_attributes_from_plugin(ConnectionBase())
    >>> test_play_context._attributes['_timeout']
    30
    """
    pass



# Generated at 2022-06-13 08:32:20.871591
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    #TODO: Add unit test
    """
    pass


# Generated at 2022-06-13 08:32:35.961739
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Arrange
    ans = Ansible("", "", "", "")
    options = dict()
    options ["become"] = True
    options ["become_method"] = "test_become_method"
    options ["become_user"] = "test_become_user"
    options ["become_pass"] = "test_become_pass"
    options ["become_exe"] = "test_become_exe"
    options ["become_flags"] = "test_become_flags"
    options ["private_key_file"] = "private_key_file"
    options ["verbosity"] = "verbosity"
    options ["start_at_task"] = None
    options ["connection"] = "connection"
    options ["remote_user"] = "remote_user"
    options ["port"] = "port"

# Generated at 2022-06-13 08:32:41.856768
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Asserting that if a plugin is provided to the method, it should not raise
    # any exception and the plugin should be set to None

    task = PlayContext()
    plugin = None
    try:
        task.set_attributes_from_plugin(plugin)
        assert task._become_plugin is None
    except Exception as e:
        assert False, "Asserting that if a plugin is provided to the method, it should not raise" \
                      "any exception and the plugin should be set to None"



# Generated at 2022-06-13 08:32:52.950668
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    stdout, sys.stdout = sys.stdout, io.StringIO()
    stderr, sys.stderr = sys.stderr, io.StringIO()
    display.verbosity = 0


# Generated at 2022-06-13 08:32:57.045791
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    c = PlayContext()
    assert c.port is None
    assert c.network_os is None
    d = dict()
    d['port'] = '1234'
    d['network_os'] = 'ios'
    c.set_attributes_from_plugin(d)
    assert c.port is '1234'
    assert c.network_os is 'ios'


# Generated at 2022-06-13 08:33:23.152825
# Unit test for constructor of class PlayContext
def test_PlayContext():
    play = MagicMock()
    passwords = MagicMock()
    connection_lockfd = 1234

    pc = PlayContext(play, passwords, connection_lockfd)

    assert pc.password == passwords.get('conn_pass', '')
    assert pc.become_pass == passwords.get('become_pass', '')

    assert pc.prompt == ''
    assert pc.success_key == ''

    assert pc.connection_lockfd == connection_lockfd


# Generated at 2022-06-13 08:33:34.232692
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    host = Host('testhost')
    host.groups = ['testgroup']
    play = Play.load(dict(
        name             = "Ansible Play",
        hosts            = 'testgroup',
        gather_facts     = 'no',
        tasks            = [
            dict(action=dict(module='shell', args='ls'))
        ]
    ), variable_manager=VariableManager(), loader=DataLoader())
    play._variable_manager.set_host_variable(host, 'ansible_ssh_host', '127.0.0.1')
    play._variable_manager.set_host_variable(host, 'ansible_ssh_port', '22')
    play._variable_manager.set_host_variable(host, 'ansible_ssh_user', 'johndoe')
    play._variable_manager.set_

# Generated at 2022-06-13 08:33:50.181254
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Variables expected to be used in tests
    # --------------------------------------
    ansible_port_exp = 'ansible_port'
    ansible_port_val = '22'
    ansible_become_pass_exp = 'ansible_become_pass'
    ansible_become_pass_val = 'pass123'

    # Create a test playbook
    # ----------------------
    playbook = Playbook.load('/dev/null', variable_manager=VariableManager(), loader=DictDataLoader())

    # Create a test play
    # ------------------

# Generated at 2022-06-13 08:34:01.803218
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Unit test for method 'set_task_and_variable_override' of class 'PlayContext'
    # Create a variable list
    variables = dict()
    variables['ansible_ssh_host'] = 'localhost'
    variables['ansible_host'] = 'localhost'
    variables['ansible_connection'] = 'paramiko'
    variables['ansible_user'] = 'root'
    variables['ansible_port'] = '22'
    variables['ansible_shell_type'] = 'sh'
    variables['ansible_python_interpreter'] = '/bin/python3.6'
    variables['ansible_connection_timeout'] = 30

    # Create a templar instance
    from ansible.template import Templar
    templar = Templar(variables=variables)

    # Create a connection information instance
    play_

# Generated at 2022-06-13 08:34:07.652201
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context._init_global_context(C.load_configuration())
    cliargs = context.CLIARGS

    # Prepare test data
    # 1) valid cliargs: -T 15 -v 2
    # 2) invalid cliargs: -x 0 
    valid_cliargs = cliargs._get_kwargs()
    valid_cliargs['timeout'] = 15
    valid_cliargs['verbosity'] = 2
    invalid_cliargs = cliargs._get_kwargs()
    invalid_cliargs['executable'] = 0

    # run test with valid args
    context.CLIARGS = Namespace(**valid_cliargs)
    p = PlayContext()
    p.set_attributes_from_cli()
    assert p.timeout == 15
    assert p.verbosity == 2

    # run test

# Generated at 2022-06-13 08:34:14.276167
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    p = C.load(None)
    pc = PlayContext(play=dict())
    pc.set_attributes_from_cli()
    assert pc.verbosity == 0
    assert pc.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert pc.timeout == C.DEFAULT_TIMEOUT
    assert pc.start_at_task is None
    assert pc.step == False


# Generated at 2022-06-13 08:34:26.305820
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    module_name = 'test_PlayContext_set_task_and_variable_override'

    from ansible.playbook import Play
    from ansible.template import Templar


# Generated at 2022-06-13 08:34:26.971850
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass

# Generated at 2022-06-13 08:34:39.093918
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    facts = dict()
    facts['inventory_hostname'] = "localhost"
    facts['group_names'] = ['ungrouped']
    facts['play_hosts'] = ['localhost']
    facts['local'] = "localhost"
    facts['groups'] = {'ungrouped': {'hosts': ['localhost']}}
    facts['vars'] = dict()
    facts['vars']['version'] = "3"
    facts['vars']['ansible_python_interpreter'] = "/usr/bin/python3"

    context.CLIARGS = dict()
    context.CLIARGS['become'] = False
    context.CLIARGS['become_method'] = 'sudo'
    context.CLIARGS['become_user'] = 'root'

# Generated at 2022-06-13 08:34:42.536984
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class helper(object):
        module = None
        def __init__(self, module):
            self.module = module
        def get_option(self, option):
            return None
        def get_default(self, option):
            return None
    the_helper = helper(None)
    p = PlayContext(the_helper)
    p.set_attributes_from_plugin(the_helper)
    assert p
    assert p.connection == 'smart'


# Generated at 2022-06-13 08:35:07.451895
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    p = PlayContext()
    print ("Checking set_task_and_variable_override with task = None")
    t = None
    v = None
    try:
        p.set_task_and_variable_override(t, v)
    except AttributeError:
        print ("Expected Attribute Error")
    except:
        print ("Failed Test")
    else:
        print ("Passed Test")

if __name__ == "__main__":
    test_PlayContext_set_task_and_variable_override()

# Inheritance list for this class
# class PlayContext(object)
# class FieldAttribute(object)

# Generated at 2022-06-13 08:35:10.528403
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context = PlayContext()
    play_context.set_task_and_variable_override(task=None, variables=None, templar=None)
    # play_context.set_task_and_variable_override(task=None, variables=None, templar=None)

# Generated at 2022-06-13 08:35:22.716970
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from unittest.mock import Mock
    from ansible.vars import Variable

    class FakeOptions(object):
        def __init__(self):
            self.connection = 'local'

    # we will use the following to inject fake data into the PlayContext
    class FakeData(object):
        connection = 'smart'

    class FakeModule(object):
        def __init__(self):
            self.connection = FakeData()

    class FakeConnection(object):
        def __init__(self):
            self.connection = FakeData()


# Generated at 2022-06-13 08:35:27.929661
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    play_context = PlayContext()
    command_line_options =  {'verbosity': 3, 'connection':'smart', 'remote_user': 'abcd', 'private_key_file':'/etc/ansible/id_rsa', 'timeout': 3, 'inventory': ['/etc/ansible/hosts']}
    context.CLIARGS = command_line_options
    play_context.set_attributes_from_cli()

# Generated at 2022-06-13 08:35:40.638662
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    from ansible.vars import VariableManager
    from ansible.template import Templar

    v = VariableManager()
    play1 = Mock()
    play1.force_handlers = False
    play1.remote_user = None
    playbook_dir = os.path.dirname(os.path.dirname(ansible.__file__))
    templar = Templar(loader=DataLoader(), variables=v)
    p = PlayContext(play1)
    t = Task()
    t.delegate_to = '{"ansible_host": "delegated_host"}'
    p.set_attributes_from_play(play1)
    p.set_attributes_from_cli()

# Generated at 2022-06-13 08:35:50.783984
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # load up vars to use in our test
    try:
        vars_prompt = dict(ANSIBLE_SSH_ARGS="-o ForwardAgent=yes -o ControlMaster=auto -o ControlPersist=60s")
        context.CLIARGS = ImmutableDict(vars_prompt)
        context.CLIARGS = dict(connection="smart")
        # create an instance of PlayContext
        pc = PlayContext()
        # execute the method we want to test
        #print (pc._attributes['connection'])
        pc.set_attributes_from_plugin('ssh')
        result_conn = pc._attributes['connection']
        # make assertions on the results
        assert result_conn == 'ssh'
    finally:
        context.CLIARGS = dict()

# Unit testing for method set_

# Generated at 2022-06-13 08:35:51.663334
# Unit test for constructor of class PlayContext
def test_PlayContext():
    pc = PlayContext()
    assert pc.command_timeout

# Generated at 2022-06-13 08:36:02.969597
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    #test_PlayContext_set_task_and_variable_override()  # unit test for method set_task_and_variable_override of class PlayContext
    # Initialize the PlayContext object
    play_context = PlayContext()

    # Set the connection attributes with play
    play_context.set_attributes_from_cli()

    # Get the play object which will be used to set the PlayContext attributes

# Generated at 2022-06-13 08:36:07.142703
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pl = Play()
    passed = False
    try:
        pc = PlayContext(play=pl)
        pc.set_attributes_from_plugin('local')
        pc.set_attributes_from_plugin('raw')
        passed = True
    except:
        passed = False
        raise
    assert passed == True


# Generated at 2022-06-13 08:36:08.412567
# Unit test for constructor of class PlayContext
def test_PlayContext():
    unittest.main(module=__name__, exit=False)


# Generated at 2022-06-13 08:36:52.426021
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Testing with default arguments
    task_obj = Task()
    variables_obj = {}
    templar_obj = Templar()
    play_context_obj = PlayContext()
    play_context_obj.set_task_and_variable_override(task_obj, variables_obj, templar_obj)
    if (play_context_obj._attributes['connection'] != 'smart'):
        return False
    if (play_context_obj._attributes['connection_user'] != None):
        return False
    if (play_context_obj._attributes['executable'] != None):
        return False
    if (play_context_obj._attributes['internal_timeout'] != None):
        return False
    if (play_context_obj._attributes['module_lang'] != 'C'):
        return False

# Generated at 2022-06-13 08:36:57.779634
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
   pc = PlayContext()
   set_task_and_variable_override(pc, "task", "variables", "templar")

# test if PlayContext.set_task_and_variable_override() raises Exception

# Generated at 2022-06-13 08:37:01.354108
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    playcontext = PlayContext(play=None, passwords=None, connection_lockfd=None)
    playcontext.set_attributes_from_plugin(plugin=None)


# Generated at 2022-06-13 08:37:09.747981
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    set_missing_host_variables(VariableManager())
    p = Play().load(dict(
        name="Ansible Play",
        hosts="all",
        gather_facts="no",
        tasks=[dict(action=dict(module="shell", args="uname"))],
    ), variable_manager=variable_manager, loader=loader)

    c = PlayContext()
    c._attributes['connection'] = 'smart'
    c.set_attributes_from_play(p)

    # check if set_attributes_from_plugin takes care of choosing connection
    c.set_attributes_from_plugin(None)
    assert c._attributes['connection'] == 'smart'

    # check if plugin option are used in preference to defaults
    c.set_attributes_from_plugin(None)

# Generated at 2022-06-13 08:37:21.312609
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import copy
    import mock
    import pytest

    class Play(object):
        def __init__(self, force_handlers):
            self.force_handlers = force_handlers

    play = Play(True)
    pc = PlayContext(play)
    pc.prompt = 'prompt'
    pc.success_key = 'success_key'
    pc.remote_addr = 'remote_addr'
    pc.port = 'port'
    pc.remote_user = 'remote_user'

    password = 'password'
    passwords = {'conn_pass': password}
    pc = PlayContext(play, passwords=passwords)

    # TODO: make sure task.delegate_to is None, the rest should not matter

    connection_lockfd = 2

# Generated at 2022-06-13 08:37:28.175859
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    context.CLIARGS = dict()
    context.CLIARGS['verbosity'] = 2
    pc = PlayContext()
    pc.set_attributes_from_cli()
    pc.connection = 'ssh'
    pc.remote_addr = '10.20.30.40'
    pc.remote_user = 'xyz'
    pc.port = 22
    pc.timeout = 20
    pc.no_log = False
    pc.verbosity = 2
    pc.connection_user = 'xyz'
    pc.prompt = '#'
    pc.success_key = 'ok'
    pc.check_mode = False
    pc.diff = False
    pc.password = None
    pc.become_pass = None

    t = MagicMock(spec=Task)
    t.delegate_to

# Generated at 2022-06-13 08:37:33.745457
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import json
    import os
    from ansible.module_utils.common.removed import removed
    from ansible.plugins import connection_loader
    from ansible.module_utils.six import PY3
    from ansible.mock import patch, MagicMock
    import ansible.constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible import context


# Generated at 2022-06-13 08:37:35.319626
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    pass


# Generated at 2022-06-13 08:37:37.822474
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    '''
    Unit test for the PlayContext method set_attributes_from_plugin
    '''
    obj = PlayContext()
    pass



# Generated at 2022-06-13 08:37:39.490302
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    my_play = play_context.PlayContext()
    assert my_play is not None

# Generated at 2022-06-13 08:39:01.848579
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.connection import ConnectionBase
    from ansible.errors import AnsibleError

    class FakeConn(ConnectionBase):

        transport = 'fake'

        def __init__(self, play_context, new_stdin, *args, **kwargs):
            pass

    class NonPlugin(object):
        pass

    # patch plugin_load to return a class instead of an instance
    with mock.patch('ansible.plugins.loader.plugin_loader.get') as get_mock:
        get_mock.return_value = FakeConn

        # set options before play to allow play to override them
        if context.CLIARGS:
            context.CLIARGS._store(('connection', None, 'paramiko'))
            context.CLIARGS._

# Generated at 2022-06-13 08:39:05.690039
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # need to get plugin name for the command
    # plugn = command.split()[1]
    # plugin = cls._load_task_plugins(task)[0]
    # FIXEME

    # Note: PlayContext(play=None, passwords=None, connection_lockfd=None)
    playContext_obj = PlayContext()
    # playContext_obj.set_attributes_from_plugin(plugin)

    # TODO: Implement this test
    raise NotImplementedError

# Generated at 2022-06-13 08:39:13.887986
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    plugin_name = "example_plugin"
    try:
        plugin = get_plugin_class(plugin_name)
        plugin_instance = plugin()
        plugin_instance._load_name = plugin_name
    except:
        assert False, "Plugin {} not exists".format(plugin_name)
    play_context = PlayContext()
    play_context.set_attributes_from_plugin(plugin_instance)
    for option in plugin_instance.options_validate:
        assert getattr(play_context, option.get('name')) == plugin_instance.get_option(option.get('name'))

# Generated at 2022-06-13 08:39:25.820965
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    '''
    Test set_task_and_variable_override method of class PlayContext
    '''

    # create dummy play and task objects
    play = dict()
    task = dict()

    # create dummy variables dict and set some dummy vars
    variables = dict()
    variables['ansible_ssh_user'] = 'foo_user'
    variables['ansible_host'] = 'foo_host'
    variables['ansible_port'] = '9999'

    # create a PlayContext object
    play_context = PlayContext()
    play_context.set_attributes_from_play(play)

    # test if remote_user is set to dummy value set in variables
    assert play_context.remote_user == 'foo_user'

    # test if remote_addr is set to dummy value set in variables

# Generated at 2022-06-13 08:39:28.528320
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Tests set_task_and_variable_override of class PlayContext
    pass



# Generated at 2022-06-13 08:39:36.879568
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from test.units.mock.loader import DictDataLoader
    from test.units.mock.path import mock_unfrackpath_noop

    def test_PlayContext_set_attributes_from_plugin_1():
        p = PlayContext()
        class Test:
            _load_name = 'test'

            def __init__(self):
                self.options = dict(connection='connection_value')

        test = Test()
        p.set_attributes_from_plugin(test)
        assert p.connection == 'connection_value'

    def test_PlayContext_set_attributes_from_plugin_2():
        p = PlayContext()
        class Test:
            _load_name = 'test'

            def __init__(self):
                self.options = dict(value='value')


# Generated at 2022-06-13 08:39:38.437764
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    check = PlayContext()
    check.set_attributes_from_cli()
    assert check.timeout == int(context.CLIARGS['timeout'])

# Generated at 2022-06-13 08:39:47.321719
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from collections import namedtuple

    from ansiblelint import RulesCollection
    from ansiblelint.rules.FlagSpecifiedCheck import FlagSpecifiedCheck as checker

    rulesdir = os.path.realpath(os.path.dirname(os.path.realpath(__file__))+'/../../ansiblelint/rules')
    collection = RulesCollection.create_from_directory(rulesdir)
    rule = collection.rules[checker.id][0]

    context = PlayContext(None)
    context.set_attributes_from_plugin(module(
        "/path/to/foo.py",
        "foo",
        "_params",  # this is a connection module
        "bar=baz"
    ))

    assert rule.matchlines is not None
    assert len(rule.matchlines) == 1

# Generated at 2022-06-13 08:39:55.126728
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    attr_names = ['address', 'port', 'remote_user', 'network_os']

    plugin_options = {
        'ansible_host': 'test_host',
        'ansible_port': 123,
        'ansible_user': 'test_user',
        'ansible_network_os': 'test'
    }

    class fake_CliOptions(object):
        def __init__(self, **kwargs):
            self.cli_args = kwargs

    context.CLIARGS = fake_CliOptions(**plugin_options)

    plugin_class = get_plugin_class('network_cli')

    # create a plugin instance
    plugin = plugin_class()

    # create a PlayContext instance
    pc = PlayContext()
    # set plugin options
    pc.set_attributes_from_

# Generated at 2022-06-13 08:40:00.231730
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    context.CLIARGS = dict()
    pc = PlayContext()
    # test_task is of type Task
    # test_variables is of type dict
    # test_templar is of type Task
    pc.set_task_and_variable_override(test_task, test_variables, test_templar)
