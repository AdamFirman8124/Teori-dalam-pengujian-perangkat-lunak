

# Generated at 2022-06-13 13:16:11.679334
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    with pytest.raises(AnsibleOptionsError, match='must be a string and one of "error", "warn" or "skip"'):
        LookupModule().run([], on_missing=True)
    with pytest.raises(AnsibleOptionsError, match='Invalid setting identifier, "C.DEFAULT_ROLES_PATH" is not a string'):
        LookupModule().run([C.DEFAULT_ROLES_PATH])

# Generated at 2022-06-13 13:16:20.704598
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create test fixture
    class plugin_loader():

        class become():

            class become_plugin():

                def __init__(self):
                    self._load_name = 'become'
            class mode_plugin():

                def __init__(self):
                    self._load_name = 'mode'
            class su():

                def __init__(self):
                    self._load_name = 'su'

        class connection():

            class ssh():
                def __init__(self):
                    self._load_name = 'ssh'
            class local():
                def __init__(self):
                    self._load_name = 'local'
            class winrm():
                def __init__(self):
                    self._load_name = 'winrm'


# Generated at 2022-06-13 13:16:27.861892
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialise the LookupModule object which can be used to test the run() method.
    # Config object contains key-value pairs of settings.
    from ansible.config.manager import ConfigManager
    configManager = ConfigManager()
    C = configManager.get_config()
    lookupModule = LookupModule()
    lookupModule.set_options({'_ansible_config': C, '_ansible_no_log': True})

    # Following are the test cases:
    # 1. Unexistant plugin name and plugin type.
    # 2. Plugin name is not valid.
    # 3. Plugin type is not valid.
    # 4. Plugin name and type valid.
    # 5. Unexistant setting name.
    # 6. Valid setting name.
    # 7. Setting name not valid for the given plugin name.
    # 8. Setting

# Generated at 2022-06-13 13:16:37.476885
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class OptionsModule(object):
        def __init__(self, info, **kwargs):
            self.info = info
            self.kwargs = kwargs

    # Initialize the lookup module
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=dict(), direct=dict())

    # Test with options on_missing=error and plugin_type=shell
    term = ['remote_tmp']
    ptype = 'shell'
    options_module = OptionsModule(info=None, on_missing='error', plugin_type=ptype)
    lookup_module.set_options(var_options=options_module.kwargs, direct=options_module.info)
    lookup_module.run(terms=term)

    # Test with options on_missing=warn and plugin_name=sh
    pname

# Generated at 2022-06-13 13:16:38.214916
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:16:49.415805
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule(loader=None, variables=None)
    assert getattr(C, lookup_module.run(["ANSIBLE_DEBUG_CALLBACKS"], variables=None, plugin_name=None, plugin_type=None, on_missing='error')[0])
    assert 'DEFAULT_ROLES_PATH' in lookup_module.run(["DEFAULT_ROLES_PATH"], variables=None, plugin_name=None, plugin_type=None, on_missing='error')[0]
    assert lookup_module.run(["UNKNOWN_CONST"], variables=None, plugin_name=None, plugin_type=None, on_missing='error') == []

# Generated at 2022-06-13 13:16:57.308813
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LookupModule_run_obj = LookupModule()
    terms = [ 'remote_user', 'port' ]

    ## testcase 1: check whether the method returns the expected output
    # with input:
    #       terms: [ 'remote_user', 'port' ]
    #       pname: 'ssh'
    #       ptype: 'connection'
    # in config.py:
    #       AnsibleLookupError: Unable to find setting port
    # Expected Result:  should return exception
    pname = 'ssh'
    ptype = 'connection'
    try:
        result = LookupModule_run_obj.run(terms, plugin_name=pname, plugin_type=ptype)
    except AnsibleLookupError as e:
        assert e.message == 'Unable to find setting port'

# Generated at 2022-06-13 13:17:06.156042
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test global config
    # testing 'DEFAULT_LOG_PATH' case
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'on_missing': 'skip'})
    result = lookup_module.run([u'DEFAULT_LOG_PATH'])
    assert result == [u'/var/log/ansible.log']
    assert 'DEFAULT_LOG_PATH' in lookup_module._display.deprecations

    # testing 'DEFAULT_LOG_PATH' case with 'error' value for on_missing
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'on_missing': 'error'})
    result = lookup_module.run([u'DEFAULT_LOG_PATH'])
    assert result == [u'/var/log/ansible.log']
   

# Generated at 2022-06-13 13:17:12.999610
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import get_all_plugin_loaders
    for loader in get_all_plugin_loaders():
        for p_type, p in loader.all().items():
            for name in p:
                config = C.config.get_config_value(
                    config='remote_tmp',
                    plugin_type=p_type,
                    plugin_name=name
                )
                assert config == LookupModule.run(terms=['remote_tmp'], plugin_type=p_type, plugin_name=name)

# Generated at 2022-06-13 13:17:23.445364
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config = [
        ['DEFAULT_BECOME_USER', 'user1', {}],
        ['PORT', None, {'plugin_type': 'connection', 'plugin_name': 'ssh'}],
        ['DEFAULT_ROLES_PATH', '/path/to/role', {}],
        ['RETRY_FILES_SAVE_PATH', '/path/to/retry', {}],
        ['COLOR_OK', 'green', {}],
        ['COLOR_CHANGED', 'yellow', {}],
        ['COLOR_SKIP', 'cyan', {}],
        ['UNKNOWN', None, {}],
        ['module_utils', None, {'plugin_type': 'shell', 'plugin_name': 'sh'}],
    ]


# Generated at 2022-06-13 13:17:38.400919
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    config = ['DEFAULT_BECOME_USER']
    terms = terms = ['DEFAULT_BECOME_USER']

    # Test DEFAULT_BECOME_USER
    result = lookup_plugin.run(terms=config, variables=dict())
    assert result == ['root']

    # Test RETRY_FILES_SAVE_PATH
    result = lookup_plugin.run(terms=['RETRY_FILES_SAVE_PATH'], variables=dict())
    assert result == ['~/.ansible/retry']

# Generated at 2022-06-13 13:17:44.269762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.connection import Connection
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'ansible_user': 'root',
        'ansible_password': 'secret'
    }
    variable_manager.options_vars = {
        'ansible_user': 'root',
        'ansible_password': 'secret'
    }
    connection = Connection()
    assert connection.transport == 'paramiko'
    assert connection.local.transport == 'connection'
    assert connection.local.connection == 'paramiko'
    #assert connection.randomizer == 1
    #assert connection._is_persistent == True
    lookup_module = LookupModule()
    # Testing different results/scenarios.

# Generated at 2022-06-13 13:17:55.409334
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    # Setup test object
    lu = LookupModule()

    # Check that default value of on_missing is 'error'
    assert lu.get_option('on_missing') == 'error'

    # Check that on_missing is accepted as 'warn'
    lu.set_options(on_missing='warn')
    assert lu.get_option('on_missing') == 'warn'

    # Check that on_missing is accepted as 'error'
    lu.set_options(on_missing='error')
    assert lu.get_option('on_missing') == 'error'

    # Check that on_missing is accepted as 'skip'
    lu.set_options(on_missing='skip')
    assert lu.get_option('on_missing') == 'skip'

    # Check that

# Generated at 2022-06-13 13:18:03.964053
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Preparation
    class Module(object):
        def __init__(self):
            self.params = dict()

    class Runner(object):
        def __init__(self):
            self.module = Module()


    # Test wrong 'on_missing'
    lookup_module = LookupModule()
    runner = Runner()
    lookup_module.runner = runner
    lookup_module.set_runner_properties(runner)
    terms = ['ansible_user']
    variables = None
    on_missing = 'abc'
    args = {'on_missing': on_missing}
    try:
        lookup_module.run(terms, variables, **args)
        assert False
    except AnsibleOptionsError:
        pass

    # Test success
    lookup_module = LookupModule()
    runner = Runner()

# Generated at 2022-06-13 13:18:10.837624
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    setting_terms = ['ANSIBLE_CALLBACK_WHITELIST', 'ANSIBLE_CALLBACK_WHITELIST', 'ANSIBLE_CALLBACK_WHITELIST', 'ANSIBLE_CALLBACK_WHITELIST', 'ANSIBLE_CALLBACK_WHITELIST']
    # Test that there is a returned list when all config settings are present
    expected_result = ['default', 'default', 'default', 'default', 'default']
    result = lookup_module.run(setting_terms)
    assert result == expected_result, "The lookup config plugin is not returning a list of the config settings when all the settings are present"

    # Test that there is a returned list when not all config settings are present
    expected_result = ['default', 'default', 'default', 'default', None]


# Generated at 2022-06-13 13:18:19.384494
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["DEFAULT_REMOTE_TMP", "UNKNOWN"]
    kwargs = dict(plugin_type='shell', plugin_name='sh')

    lookup_mock = LookupModule()
    lookup_mock.set_options(**kwargs)
    data = lookup_mock.run(terms, on_missing='error', **kwargs)

    assert data == [".ansible/tmp", "/tmp"]

# Generated at 2022-06-13 13:18:23.662133
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(direct={})
    terms = ['DEFAULT_ROLES_PATH', 'RETRY_FILES_SAVE_PATH', 'COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP']
    assert lookup_module.run(terms)

# Generated at 2022-06-13 13:18:28.458996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestVars:
        private_key_file = "~/.ssh/id_rsa"

    lookup_map = LookupModule()
    results = lookup_map.run(["DEFAULT_PRIVATE_KEY_FILE"], TestVars())
    assert results[0] == "~/.ssh/id_rsa"


# Generated at 2022-06-13 13:18:37.275013
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with invalid 'missing' option value
    lookup_module = LookupModule()
    try:
        result = lookup_module.run(terms=[], variables={}, on_missing='xyz')
    except AnsibleOptionsError:
        result = None
        # Expected error
    assert result is None

    # Test with missing global config key
    lookup_module = LookupModule()
    try:
        result = lookup_module.run(terms=['missing_config'], variables={}, on_missing='error')
    except AnsibleError:
        result = None
        # Expected error
    assert result is None

    # Test with passed global config key
    lookup_module = LookupModule()
    result = lookup_module.run(terms=['DEFAULT_SUDO_USER'], variables={}, on_missing='error')
   

# Generated at 2022-06-13 13:18:47.401678
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import vars_loader

    C.DEFAULT_HASH_BEHAVIOUR = 'md5'
    constants_dict = {'vars': {'DEFAULT_HASH_BEHAVIOUR': 'md5'}}
    constants = ImmutableDict(constants_dict, constants_loader=vars_loader)

    C.initialize_global_vars(constants, None)

    module_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'hacking', 'environment.py')
    module = imp.load_source(os.path.splitext(os.path.basename(module_path))[0], module_path)
   

# Generated at 2022-06-13 13:19:15.609572
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    ansible.plugins.loader.find_plugin_by_name = lambda x, y: y._load_name == '_success'

    def test_LookupModule_run_with_success_option(tmpdir, monkeypatch):
        plugin_type = 'connection'
        plugin_name = '_success'
        settings = [True, False]
        for setting in settings:
            t = tmpdir.mkdir(plugin_type).mkdir(plugin_name)
            t.join('__init__.py').write('from ansible.plugins.connection.%s import Connection as %s' % (plugin_name, plugin_name))

# Generated at 2022-06-13 13:19:23.050209
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global C
    C.DEFAULT_ROLES_PATH = [
        '/Users/my-user/myansible/roles',
        '/Users/my-user/.ansible/roles',
        '/usr/share/ansible/roles'
    ]
    C.ANSIBLE_CONFIG = '/Users/my-user/myansible/ansible.cfg'
    C.DEFAULT_REMOTE_TMP = '/tmp/ansible-tmp'
    lm = LookupModule()
    assert lm.run(['DEFAULT_ROLES_PATH']) == ['/Users/my-user/myansible/roles', '/Users/my-user/.ansible/roles', '/usr/share/ansible/roles']

# Generated at 2022-06-13 13:19:35.272847
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:19:49.056458
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise RuntimeError(msg)

    class MockPlugin(object):

        def __init__(self, *args, **kwargs):
            self._load_name = kwargs.get('plugin_name')

    class MockLoader(object):
        def __init__(self, *args, **kwargs):
            self._plugins = {'mock': MockPlugin}

        def get(self, plugin_name, class_only=False):
            return self._plugins.get(plugin_name)

    # mock constants
    module = {'DEFAULT_BECOME_METHOD': 'sudo'}
    module.update({'__ansible_module__': MockModule()})

    # mock config

# Generated at 2022-06-13 13:20:00.235566
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # get_option method
    assert lookup_module.get_option('on_missing') == 'error'
    assert lookup_module.get_option('plugin_type') is None
    assert lookup_module.get_option('plugin_name') is None

    # set_options method
    lookup_module.set_options(var_options=None, direct=dict(on_missing='warn'))
    assert lookup_module.get_option('on_missing') == 'warn'
    lookup_module.set_options(var_options=None, direct=dict(plugin_type='lookup'))
    assert lookup_module.get_option('plugin_type') == 'lookup'

    # run method

# Generated at 2022-06-13 13:20:07.101331
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create instance of LookupModule
    look = LookupModule()

    # test on_missing option with value 'error'
    assert look.run(["DEFAULT_ROLES_PATH"], {'on_missing': 'error'}), 'Returned value is not same as expected'

    # test on_missing option with value 'warn'
    assert look.run(["UNKNOWN_LOOKUP"], {'on_missing': 'warn'}), 'Returned value is not same as expected'

    # test on_missing option with value 'skip'
    assert look.run(["ANSI_COLOR_GREEN"], {'on_missing': 'skip'}), 'Returned value is not same as expected'

    # test with plugin_type and plugin_name options

# Generated at 2022-06-13 13:20:16.426684
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # get_plugin_config
    pname = 'httpapi'
    ptype = 'httpapi'
    config = 'remote_tmp'
    variables = {}
    result = _get_plugin_config(pname, ptype, config, variables)
    assert result == C.REMOTE_TMP

    # get_global_config
    config = 'PASSWORD_STARS'
    result = _get_global_config(config)
    assert result == C.PASSWORD_STARS

    # config
    terms = ["REMOTE_TMP"]
    result = LookupModule().run(terms)
    assert result[0] == C.REMOTE_TMP

# Generated at 2022-06-13 13:20:20.492775
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  class t_LookupBase(LookupBase):
      def get_option(self, opt_name):
          return None
      def set_options(self, var_options=None, direct=None):
          pass
      def _display(self, *args, **kwargs):
          pass

  lookup = t_LookupBase()
  lookup.run(terms=['foo'])

# Generated at 2022-06-13 13:20:27.586667
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils._text import to_bytes
    # Test Case 1 - config option is not a string
    # Result: Lookup should fail with exception
    lookup_module = LookupModule()
    try:
        lookup_module.run(terms=[123])
    except AnsibleOptionsError as e:
        assert 'Invalid setting identifier' in to_text(e)

    # Test Case 2 - config option is not a valid Ansible config option
    # Result: Lookup should fail with exception
    lookup_module = LookupModule()
    try:
        lookup_module.run(terms=['wrong_config'])
    except AnsibleLookupError as e:
        assert 'Unable to find setting wrong_config' in to_text(e)

# Generated at 2022-06-13 13:20:39.865729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):
        def __init__(self, **kwargs):
            self.get_option_called = False
            self.set_options_called = False
            self.set_options_called_with_var_options = None
            self.set_options_called_with_direct = None

        def get_option(self, key):
            self.get_option_called = True
            return self.get_options()[key]

        def set_options(self, var_options=None, direct=None):
            self.set_options_called = True
            self.set_options_called_with_var_options = var_options
            self.set_options_called_with_direct = direct

        def __getitem__(self, key):
            return self.get_option(key)

# Generated at 2022-06-13 13:21:18.621265
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.sentinel import Sentinel

    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.lookup.config import LookupModule
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 1

    l = LookupModule(display=display)

    term = "test_None"
    variables = {}
    expected = Sentinel
    result = l.run(terms=[term], variables=variables, on_missing="error")

    assert result[0] == Sentinel

    term = "DEFAULT_BECOME_USER"
    expected = "root"
    variables = {}
    result = l.run(terms=[term], variables=variables, on_missing="error")

    assert result[0] == expected

    term = "DEFAULT_UNKNOWN"
   

# Generated at 2022-06-13 13:21:22.719932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["DEFAULT_BECOME_USER"]
    #expected = ['root']
    result = lookup.run(terms)
    print(result)

test_LookupModule_run()

# Generated at 2022-06-13 13:21:33.135665
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test for lookup('config', 'DEFAULT_BECOME_USER')
    from ansible.plugins.loader import become_loader
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.lookup.config import LookupModule
    from ansible.template import Templar
    import ansible.constants as C
    import ansible.module_utils._text as to_native
    import json
    import pytest

    ret = []
    result = None
    setattr(C, 'DEFAULT_BECOME_USER', 'root')
    method = become_loader._create_directories(setattr(C, 'DEFAULT_BECOME_USER', 'root')).__get__(True)
    lookup_base = LookupBase()
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:21:35.712042
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    global ret
    module = LookupModule()
    module.run(["DEFAULT_BECOME_USER"])

# Generated at 2022-06-13 13:21:49.591920
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    class FakeVars(object):
        def __init__(self):
            self.DEFAULT_BECOME_USER = 'root'
            self.DEFAULT_REMOTE_USER = 'vagrant'
            self.DEFAULT_ROLES_PATH = '/home/vagrant/'
            self.RETRY_FILES_ENABLED = False

    class FakeDisplay(object):
        def __init__(self):
            self.warning_called = False

        def warning(self, msg):
            self.warning_called = True

    fake_vars = FakeVars()
    fake_display = FakeDisplay()

    # Test missing on_missing
    terms = ["DEFAULT_BECOME_USER", "DEFAULT_ROLES_PATH"]

# Generated at 2022-06-13 13:21:56.610724
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import base64
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # yaml.load not available until PyYAML 3.11
    # from ansible.parsing.yaml.loader import AnsibleLoader
    # from ansible.parsing.vault import VaultLib

    # Define a couple of dicts for testing...

# Generated at 2022-06-13 13:22:07.543515
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = []
    test_variables = {
        'connection': 'ansible.netcommon.network_cli',
        'ansible_ssh_user': 'ubuntu',
        'ansible_ssh_pass': 'ubuntu',
        'ansible_ssh_host': '10.240.0.10',
        'ansible_ssh_port': '22',
        'ansible_connection': 'ssh',
        'ansible_network_os': 'ios'
    }

    lookup_obj = LookupModule()
    result = lookup_obj.run(test_terms, test_variables)
    assert isinstance(result, list)

    test_terms = ['DEFAULT_MODULE_INVENTORY_SORT_ORDER']
    result = lookup_obj.run(test_terms, test_variables)
   

# Generated at 2022-06-13 13:22:14.940406
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.module_utils.basic
    import ansible.plugins.loader
    import ansible.module_utils.six

    import json
    # Required for instance creation, so run method of base class LookupBase can find it
    ansible.plugins.loader.plugins = ansible.plugins.loader.PluginLoader(None, None, '', '', '', None)

    l = LookupModule()

    l.set_options(var_options={'a': 'A', 'b': 'B'}, direct={'c': 'C', 'd': 'D'})

    # Test for invalid on_missing option

# Generated at 2022-06-13 13:22:18.759876
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    mod.set_options(var_options=None, direct={'on_missing':'error'})
    mod.run(terms=['DEFAULT_ROLES_PATH'])


import unittest
from ansible.module_utils._text import to_bytes

# Generated at 2022-06-13 13:22:19.673659
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-13 13:23:28.146696
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # This method will return result of the key in method run of lookup_module.py.
    def _get_config(config):
        return config

    def get_config_value(config, plugin_type=None, plugin_name=None, variables=None):
        return config

    # This method will return the global setting of the key used.
    def get_all_config_values(config):
        return config

    # This method will return the value of the key used.
    def get_all_config_values(config, plugin_type=None, plugin_name=None, variables=None):
        return config

    #Lists of expected result after running method run.

# Generated at 2022-06-13 13:23:43.382146
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup test data
    terms = ["UNKNOWN"]

# Generated at 2022-06-13 13:23:55.156377
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = {
        'plugin_type': 'connection',
        'plugin_name': 'ssh',
        'on_missing': 'skip',
        '_terms': ['remote_user', 'port'],
    }
    configs = [
        {
            'remote_user': 'root',
            'port': 22,
        },
        {
            'remote_user': 'user1',
            'port': 22,
        },
        {
            'port': 22,
        },
    ]
    results = [
        ['root', 22],
        ['user1', 22],
        [None, 22],
    ]
    for config, result in zip(configs, results):
        m = LookupModule()
        m.set_options(var_options=config)
        assert m.run(**args) == result

# Generated at 2022-06-13 13:23:58.245109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # unit tests have been moved to the test_utils/plugins/test_lookup_plugins.py
    # in order to unblock the release of Ansible 2.5
    pass

# Generated at 2022-06-13 13:24:05.417220
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, play_context=PlayContext())
    variable_manager.set_inventory(inventory)
    play_context = PlayContext(variable_manager=variable_manager)


# Generated at 2022-06-13 13:24:16.222360
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import is_sequence
    assert LookupModule.run.__doc__ == """
    This method is mainly for testing purposes.
    """
    try:
        lookup_module = LookupModule()
    except Exception as e:
        print('Exception raised: {0!r}'.format(e))
        assert False
    # As of Ansible 2.8, an error is raised if 'var_options'
    # is not set in the 'set_options' call.

# Generated at 2022-06-13 13:24:30.246938
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    from ansible.context import CLIContext
    import pytest

    res = None
    plugin = LookupModule()
    loader = DataLoader()
    display = Display()
    context = CLIContext()
    variable_manager = VariableManager()

    config_key = C.ANSIBLE_CONFIG
    C.ANSIBLE_CONFIG = None

    with pytest.raises(AnsibleOptionsError) as excinfo:
        plugin.run('string')
    assert 'Missing required plugin_type and plugin_name' in to_native(excinfo.value)


# Generated at 2022-06-13 13:24:38.900738
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test module
    module = LookupModule()

    # Test run method
    assert 'Default' in module.run(["ANSIBLE_ANSIBLE_MODULE_ARGS"], {'ansible_module_args': 'Default'})[0]

    assert 'TestValue' in module.run(["ANSIBLE_NET_USERNAME"], {'ansible_net_username': 'TestValue', 'ansible_password': 'PasswordValue'})[0]
    assert 'PasswordValue' in module.run(["ANSIBLE_NET_PASSWORD"], {'ansible_net_username': 'TestValue', 'ansible_password': 'PasswordValue'})[0]

    assert 'Default' in module.run(["ANSIBLE_LOG_PATH"], {'ansible_module_args': 'Default'})[0]

# Generated at 2022-06-13 13:24:39.451248
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:24:49.431730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test 1: global settings
    result = lookup.run(["DEFAULT_REMOTE_TMP"])
    expected = [u"$HOME/.ansible/tmp"]
    assert result == expected

    # Test 2: plugin settings
    result = lookup.run(["autoremove", "config_dir"], plugin_type="vars", plugin_name="yum")
    expected = [False, "/etc/yum"]
    assert result == expected

    # Test 3: drop missing settings
    result = lookup.run(["A", "B"], on_missing="skip")
    expected = []
    assert result == expected

    # Test 4: warn about missing settings
    result = lookup.run(["DEFAULT_REMOTE_TMP", "C", "D"], on_missing="warn")