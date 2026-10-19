

# Generated at 2022-06-13 13:16:16.126409
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test when there are no terms provided
    terms = []
    plugin_type = ''
    plugin_name = ''
    result = lookup_module.run(terms=terms, plugin_type=plugin_type, plugin_name=plugin_name)
    assert result == []

    # Test when there is plugin type and plugin name provided
    terms = ['TEST_CONFIG1', 'TEST_CONFIG2']
    plugin_type = 'connection'
    plugin_name = 'local'
    # Test when config value is retrieved successfully
    result = lookup_module.run(terms=terms, plugin_type=plugin_type, plugin_name=plugin_name)
    assert result == [None, None]
    # Test when plugin type is valid but plugin name is invalid
    plugin_name = 'local1'

# Generated at 2022-06-13 13:16:24.879546
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']
    plugin_type = 'shell'
    plugin_name = 'sh'
    lookup_module = LookupModule()

    # test for plugin config
    settings = lookup_module.run(terms, plugin_type=plugin_type, plugin_name=plugin_name)
    assert settings[0] == 'root'
    assert settings[1] == ['/etc/ansible/roles']

    # test for global config
    settings = lookup_module.run(terms)
    assert settings[0] == 'root'
    assert settings[1] == ['/etc/ansible/roles']

# Generated at 2022-06-13 13:16:25.575874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test for method run
    pass

# Generated at 2022-06-13 13:16:30.983245
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    unittest for method run of class LookupModule
    """
    lookup = LookupModule()
    lookup.set_options({'on_missing': 'error', 'plugin_type': 'vars', 'plugin_name': 'system'})
    assert lookup.run(['foo', 'bar']) == []

# Generated at 2022-06-13 13:16:37.256049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    terms = ['DEFAULT_HOST_LIST']
    lookup.set_loader('/')

    # Testing missing key
    missing = 'error'
    info = {'on_missing': missing}
    with pytest.raises(AnsibleLookupError):
        lookup.run(terms=terms, variables=info)

    # Testing success
    missing = 'skip'
    info = {'on_missing': missing}
    result = lookup.run(terms=terms, variables=info)
    assert result == []

# Generated at 2022-06-13 13:16:48.324644
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with plugin_name specified
    m = LookupModule()
    result = m.run(terms=['privilege_escalation'], variables={
        'ansible_connection': 'ssh',
        'ansible_user': 'root',
        'ansible_ssh_pass': 'foobar'
    }, plugin_type='connection', plugin_name='ssh')[0]
    assert result == 'sudo', result

    result = m.run(terms=['remote_tmp'], variables={
        'ansible_connection': 'ssh',
        'ansible_user': 'root',
        'ansible_ssh_pass': 'foobar'
    }, plugin_type='shell', plugin_name='sh')[0]
    assert result == '/tmp', result

    # test with plugin_name not specified

# Generated at 2022-06-13 13:16:56.149768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import become_loader
    from ansible.plugins.loader import cliconf_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import shell_loader
    import ansible.constants as C

    # Mock current working path
    C.DEFAULT_LOCAL_TMP = '/foo'
    C.RETRY_FILES_SAVE_PATH = '/bar'
    C.DEFAULT_ROLES_PATH = ['/baz', '/qux']
    C.ROLE_PATH.insert(0, C.DEFAULT_ROLES_PATH[0])
    C.ROLE_PATH.insert(0, C.DEFAULT_ROLES_PATH[1])
    C.DEFAULT_BECOME_USER = 'tester'

# Generated at 2022-06-13 13:17:05.410770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test get_option function with default values
    lookup_plugin = LookupModule()
    assert lookup_plugin.__class__.__name__ == 'LookupModule'
    assert lookup_plugin.get_option("on_missing") == 'error'
    assert lookup_plugin.get_option("plugin_type") == None
    assert lookup_plugin.get_option("plugin_name") == None

    # Test get_option function with values in the set_options
    lookup_plugin.set_options({"on_missing": "skip", "plugin_type": "lookup", "plugin_name": "some_plugin"})
    assert lookup_plugin.get_option("on_missing") == 'skip'
    assert lookup_plugin.get_option("plugin_type") == 'lookup'

# Generated at 2022-06-13 13:17:14.982571
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def side_effect(var):
        if var == 'UNKNOWN':
            raise MissingSetting('UNKNOWN')
        return 'override'

    class MockDisplay:
        def __init__(self):
            self.warnings = []

        def warning(self, msg):
            self.warnings.append(msg)

    class FakeVarsModule:
        def __init__(self):
            self.vars = dict(config_in_var='UNKNOWN')

    l = LookupModule(MockDisplay())
    l.set_runner(FakeVarsModule())

    class FakeTerm:
        def __init__(self, term):
            self.term = term

    # Test overridden lookup value

# Generated at 2022-06-13 13:17:24.352409
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3

    # create a test class
    class MockClass:
        pass

    # create an instance of the above class
    mock_obj = MockClass()

    # to test run method of class LookupModule, we need to create an instance of class LookupModule
    lookup_obj = LookupModule()

    # create an instance of class MockLookupBase
    lookup_obj.set_options(var_options=None, direct=None)

    # initialize mock_class attributes
    mock_obj.get_option = lambda x: 'error'

    # initilize ansible constants
    C.DEFAULT_ASK_PASS = 'default_ask_pass_value'

    # create an instance of class MockDataLoader
    class MockDataLoader:
        cache = {}

# Generated at 2022-06-13 13:17:41.443736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.sentinel import Sentinel
    from ansible.errors import AnsibleOptionsError, AnsibleLookupError
    import os

    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    lookup_params = {}
    lookup_params['_raw_params'] = 'test_setting'
    options_params = {'plugin_type': 'shell', 'plugin_name': 'sh', 'on_missing': 'error'}
    lookup_params

# Generated at 2022-06-13 13:17:48.304679
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # No exception should be raise and config values should be returned for valid parameters
    _get_global_config = LookupModule().run(terms=["RETRY_FILES_SAVE_PATH"])
    assert _get_global_config == AnsibleLookupError

    # Exception should be raise for invalid parameters
    _get_global_config = LookupModule().run(terms=[])
    assert _get_global_config == AnsibleOptionsError

# Generated at 2022-06-13 13:17:59.179823
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_USER']
    variables = {}
    variables['on_missing'] = 'error'
    variables['plugin_type'] = None
    variables['plugin_name'] = None
    variables['gathering'] = 'smart'
    variables['gather_subset'] = [u'all']
    variables['ansible_verbosity'] = 0
    variables['ansible_version'] = '2.7.0'
    variables['ansible_python_interpreter'] = u'/usr/bin/python'
    variables['ansible_playbook_python'] = u'/usr/bin/python'
    variables['ansible_inventory_sources'] = ['hosts']
    variables['ansible_host_list'] = ['hosts']
    variables['ansible_host_pattern_mismatch'] = False

# Generated at 2022-06-13 13:18:03.459753
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    os.environ['ANSIBLE_PROXY_PORT'] = '8888'
    os.environ['ANSIBLE_STDOUT_CALLBACK'] = 'json'
    assert LookupModule().run(['proxy_port']) == [8888]

if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 13:18:04.321756
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-13 13:18:10.310562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    test_terms = ['DEFAULT_BECOME_USER']
    test_terms_incorrect = ['abc']

    ret = module.run(test_terms)
    assert(ret[0] == 'root')

    # Test try/except
    ret = module.run(test_terms_incorrect)
    assert(ret[0] == 'root')

# Generated at 2022-06-13 13:18:18.006574
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # Method run of class LookupModule should return the value of config item 'DEFAULT_ROLES_PATH'
    assert isinstance(module.run(terms=['DEFAULT_ROLES_PATH']), list)
    assert module.run(terms=['DEFAULT_ROLES_PATH']) == ['./roles', './library', './actions', '/usr/share/ansible/roles']

# Generated at 2022-06-13 13:18:23.546735
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ansible_options = dict(connection='local', diff=False, syntax=False, become=None, become_method=None,
          become_user=None, check=False, listhosts=None, listtasks=None, listtags=None, module_path=None,
          forks=None, remote_user=None, private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None,
          scp_extra_args=None, become_ask_pass=None, verbosity=None,
          inventory=None, subset=None, extra_vars=[], tags=[], skip_tags=[], run_once=False, vault_password_files=None,
          vault_ids=[], vault_password=None)

    # 1. test for normal checking
    # 1

# Generated at 2022-06-13 13:18:28.301768
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    config = ['DEFAULT_BECOME_USER','DEFAULT_ROLES_PATH','RETRY_FILES_SAVE_PATH','COLOR_OK','COLOR_CHANGED','COLOR_SKIP']
    vars = {'config_in_var':'UNKNOWN'}
    lookup.run(config, vars)

# Generated at 2022-06-13 13:18:29.328744
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: write unit tests
    pass

# Generated at 2022-06-13 13:18:50.012903
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    # test with invalid option
    invalid_option = ["hosts"]
    lookup.set_options(var_options=None,direct={'plugin_name': 'ssh', 'plugin_type': 'connection'})
    with pytest.raises(AnsibleOptionsError) as error:
        lookup.run(invalid_option)
        assert error.msg == 'Invalid setting identifier'

    # test with plugin setting
    terms = ['remote_user', 'port']
    lookup.set_options(var_options=None,direct={'plugin_name': 'ssh', 'plugin_type': 'connection'})
    result = lookup.run(terms)
    assert result == [u'root', 22]

    # test with core setting
    terms = ['DEFAULT_KNOWN_HOSTS_FILE']

# Generated at 2022-06-13 13:18:50.854470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:18:58.000792
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    # setup module args
    sys.modules['ansible.constants'] = MockAnsibleConstants()
    sys.modules['ansible.plugins.loader'] = MockAnsiblePluginsLoader()

    lookup_plugin = lookup_plugin_class()
    lookup_plugin.set_options()

    # run function
    # result = lookup_plugin.run(['UNKNOWN'], {}, {})
    result = lookup_plugin.run(['C.UNKNOWN'], {}, {})
    assert result == []


# Generated at 2022-06-13 13:19:08.521541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given
    input_args = {'_terms': ['user_test_1'], 'plugin_type': 'config', 'plugin_name': 'user'}
    global_configs = {'user_test_1': 'user_test_value_1'}
    plugin_configs = {'user': {'user_test_2': 'user_test_value_2'}}
    variables = {'lookup_plugin_configs': plugin_configs}

    # when
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=variables, direct=input_args)
    with patch.object(C, 'config') as config, \
            patch.object(C, 'user_test_1', new=global_configs['user_test_1']):
        config.get

# Generated at 2022-06-13 13:19:17.938349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1
    lm = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    variables = dict()
    kwargs = dict()
    res = lm.run(terms, variables, **kwargs)
    assert len(res) == 1
    assert res[0] == 'root'
    # Test 2
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD']
    res = lm.run(terms, variables, **kwargs)
    assert len(res) == 2
    assert res[0] == 'root'
    assert res[1] == 'sudo'
    # Test 3
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD', 'INVALID_KEY']

# Generated at 2022-06-13 13:19:24.783157
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.six import StringIO
    from ansible.utils.display import Display
    from units.mock.loader import DictDataLoader

    lookup_instance = LookupModule()
    lookup_instance._display = Display()
    lookup_instance._display.verbosity = 3
    lookup_instance.set_loader(DictDataLoader({}))

    # Validate method run with valid arguments
    assert lookup_instance.run(['DEFAULT_BECOME_USER'], variables={}) == ['root']
    assert lookup_instance.run(['DEFAULT_BECOME_USER'], variables={}, on_missing='skip') == ['root']

    # Validate method run with invalid arguments
    lookup_instance._display._output = StringIO()
    lookup_instance._

# Generated at 2022-06-13 13:19:36.292247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # Set up mock configuration
    import ansible.constants as C
    C.DEFAULT_ROLES_PATH = ["/etc/ansible/roles"]
    C.RETRY_FILES_SAVE_PATH = "/tmp/ansible-retry"

    # Set up mock display
    import ansible.utils.display as D
    from ansible.utils.display import Display
    D._display = Display()
    D._display.verbosity = 2

    # Create LookupModule instance
    from ansible.plugins.lookup import LookupBase
    lookup_plugin = LookupBase()

    # Create LookupModule instance
    from ansible.plugins.lookup import LookupBase
    lookup_plugin = LookupBase()

    # Create a lookup module
    lookup_

# Generated at 2022-06-13 13:19:39.247395
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    assert lookup.run(terms) == ['root']

# Generated at 2022-06-13 13:19:40.546864
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement tests
    pass

# Generated at 2022-06-13 13:19:50.327203
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = ['DEFAULT_ROLES_PATH', 'this was not defined']
    test_variables = None
    test_plugin_type = 'connection'
    test_plugin_name = 'local'

    lookup_plugin = LookupModule()
    test_ret = lookup_plugin.run(test_terms, test_variables, plugin_type=test_plugin_type, plugin_name=test_plugin_name)

    assert test_ret == [['~/.ansible/roles', u'/etc/ansible/roles']]

# Generated at 2022-06-13 13:20:18.585907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  assert True

# Generated at 2022-06-13 13:20:27.579635
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.aggr_inventory import AggregateInventory
    from ansible.utils.sentinel import Sentinel
    from ansible.module_utils._text import to_bytes

    # Mocking classes for testing
    class MockLookupBase(LookupBase):
        def run(self, terms, variables=None, **kwargs):
            return super(MockLookupBase, self).run(terms, variables=variables, variables=variables, **kwargs)

    class MockVariableManager(object):
        def get_vars(self, loader=None, play=None):
            return {
                'var2': 'var2_val',
                'var1': 'var1_val'
            }


# Generated at 2022-06-13 13:20:39.811269
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    plugin_loader.add_directory('./test/unit/plugins/lookup')
    plugin = plugin_loader.get('lookup', 'lookup_test')
    plugin.set_options(var_options={'config': 'test'}, direct={'plugin_type': 'lookup', 'plugin_name': 'test'})
    assert plugin.run(['key1', 'key2']) == ['value1', 'value2']
    assert plugin.run(['key1', 'key2'], on_missing='skip') == ['value1', 'value2']
    assert plugin.run(['key1', 'key3'], on_missing='skip') == ['value1']
    assert plugin.run(['key1', 'key3'], on_missing='warn') == ['value1']

# Generated at 2022-06-13 13:20:47.971955
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    To run this test, use:
    python -m pytest tests/test_lookup_plugins/test_lookup_config.py
    :return:
    """
    import ansible.plugins.loader as plugin_loader
    from ansible.plugins.lookup import LookupBase

    class loader:
        def get(name, class_only=False):
            return None

    plugin_loader.get = loader.get

    lookup = LookupModule()
    lookup._display = None
    lookup.api = None

    with pytest.raises(AnsibleOptionsError):
        # Missing setting identifier
        value = lookup.run([], variables={})

# Generated at 2022-06-13 13:20:53.751479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    assert lu.run(["DEFAULT_MODULE_NAME"], dict(), dict()) == ["command"]
    assert lu.run(["DEFAULT_MODULE_NAME"], dict({u"DEFAULT_MODULE_NAME":"newcommand"}), dict()) == ["newcommand"]

# Generated at 2022-06-13 13:21:06.074107
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Note: we're not testing every option as most of them are already tested in the tests for
    # config/constants.py, only the new ones are tested here.

    # Note: the ptype and pname parameters are not documented, they are not meant to be used outside
    # of core ansible. In the future we'll want to clean them up and getting rid of them as well.

    # Note: the plugin_name parameter was added in 2.12, so we are testing without it here as well.

    # tests with plugin_type and plugin_name
    plugin_type = 'lookup'
    plugin_name = 'vars'
    terms = ['walk']
    result = LookupModule().run(terms=terms, plugin_type=plugin_type, plugin_name=plugin_name)

# Generated at 2022-06-13 13:21:16.656589
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    terms = ["ANSIBLE_NOCOLOR"]
    variables = {}
    kwargs = {}
    ptype = "test"
    pname = "test"
    assert module.run(terms, variables, ptype=ptype, pname=pname) == [C.ANSIBLE_NOCOLOR]

    terms = ["not_key"]
    assert module.run(terms, variables, ptype=ptype, pname=pname) == []

    terms = ["not_key"]
    kwargs["on_missing"] = "skip"
    assert module.run(terms, variables, ptype=ptype, pname=pname) == []

    terms = ["not_key"]
    kwargs["on_missing"] = "warn"

# Generated at 2022-06-13 13:21:23.356795
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mock_sentinel = Sentinel()
    class MockedLookupModule(LookupModule):
        def set_options(myself, var_options=None, direct=None):
            myself.options = direct
        def get_option(myself, key):
            return myself.options[key]
    # test 1 - run, on_missing = error
    result = MockedLookupModule().run(["foo"], on_missing = "error")
    assert result == []
    # test 2 - run, on_missing = skip
    result = MockedLookupModule().run(["foo"], on_missing = "skip")
    assert result == []
    # test 3 - run, on_missing = warn
    result = MockedLookupModule().run(["foo"], on_missing = "warn")
    assert result == []
    # test 4 - run

# Generated at 2022-06-13 13:21:24.176546
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:21:32.770422
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Testing error raised when invalid on_missing is given
    invalid_on_missing = dict(on_missing='invalid')
    terms = []
    try:
        result = lookup.run(terms, **invalid_on_missing)
    except AnsibleOptionsError as e:
        assert '"on_missing" must be a string' in to_native(e)

    # Testing error raised when invalid plugin type is given
    invalid_plugin_type = dict(plugin_type='invalid')
    terms = []
    try:
        result = lookup.run(terms, **invalid_plugin_type)
    except AnsibleOptionsError as e:
        assert 'plugin_type must be a string and one' in to_native(e)

    # Testing error raised if only plugin_type is given but not plugin_

# Generated at 2022-06-13 13:22:38.014621
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test to get default_become_user
    def mock_get_config_value(key, variables=None, plugin_type=None, plugin_name=None):
        assert key == 'DEFAULT_BECOME_USER'

        return 'root'

    C.config.get_config_value = mock_get_config_value

    lookup_mod = LookupModule()
    lookup_mod.set_options(var_options={}, direct={'plugin_type': None, 'plugin_name': None})
    assert lookup_mod.run(['DEFAULT_BECOME_USER']) == ['root']

    # Test to get exception for invalid setting identifier
    def mock_get_config_value_error(key, variables=None, plugin_type=None, plugin_name=None):
        assert key == 'inv_set_key'

# Generated at 2022-06-13 13:22:39.118544
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([''])

# Generated at 2022-06-13 13:22:48.973764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader
    import ansible.constants as C
    import ansible.module_utils.six as six
    import ansible.module_utils._text as t

    lookup_module = LookupModule()

    options = dict(variables=dict())

    # test with no terms
    try:
        lookup_module.run([], **options)
        raise AssertionError('run with no terms should fail with an exception')
    except AnsibleOptionsError as e:
        assert isinstance(e, AnsibleOptionsError)
        assert t.to_native(e) == 'one or more required arguments have not been provided'

    # test invalid term

# Generated at 2022-06-13 13:23:00.305182
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mod = LookupModule()
    options = dict(plugin_type="become", plugin_name="sudo", on_missing="skip")
    terms = ["ANSIBLE_DEBUG"]
    lookup_results = lookup_mod.run(terms, **options)
    assert len(lookup_results) == 1 and lookup_results[0]

    options = dict(plugin_type="callback", plugin_name="stats", on_missing="error")
    terms = ["ANSIBLE_DEBUG"]
    lookup_results = lookup_mod.run(terms, **options)
    assert len(lookup_results) == 1 and lookup_results[0]

    options = dict(plugin_type="test", plugin_name="test", on_missing="error")
    terms = ["ANSIBLE_DEBUG"]

# Generated at 2022-06-13 13:23:04.991897
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = LookupModule().run(['FOO_BAR'])
    assert ret == [], "When non existing config key provided, empty list should be returned, got: %s" % ret

    ret = LookupModule().run(['ACTION_WARNINGS'])
    assert isinstance(ret, list), "When existing config key provided, list should be returned, got: %s" % ret
    assert ACTION_WARNINGS in ret, "When existing config key provided, list should contain the value for the setting, " \
                                   "got: %s" % ret

# Generated at 2022-06-13 13:23:13.712966
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_value = [1, 2, 3]
    test_config = "DEFAULT_BECOME_USER"

    lookup = LookupModule()

    test_terms = [test_config, "UNKNOWN"]
    test_terms_invalid = [1, "INVALIDTERM", "UNKNOWN"]

    try:
        result = lookup.run(test_terms)
        assert result == test_value, "lookup.run() returned: %s, expected: %s" % (result, test_value)
    except Exception as e:
        raise AssertionError("lookup.run() returned a failure: %s" % e)


# Generated at 2022-06-13 13:23:27.017834
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test setup, before each test
    def setup():
        self.lookup_obj = LookupModule()
        self.lookup_obj.set_loader(plugin_loader)
        self.lookup_obj.set_env({'ANSIBLE_CONFIG': 'test/ansible.cfg'})

    # Test teardown, after each test
    def teardown():
        self.lookup_obj = None

    # Test cases

    # Tested method: run
    def test_run_success1():
        """This tests to see if incorrect config option is given, it should throw MissingSetting error"""
        setup()

# Generated at 2022-06-13 13:23:30.913703
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()  # pylint: disable=invalid-name
    result = lookup.run([''], {}, on_missing='ignore')
    assert result == [], result

# Generated at 2022-06-13 13:23:45.158015
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_object = LookupModule()

    # test None is not string
    try:
        lookup_object.run(terms=None, variables=None)
        assert False
    except AnsibleOptionsError as e:
        assert e.message == 'Invalid setting identifier, "None" is not a string, its a <type \'NoneType\'>'

    # test None is not empty string
    try:
        lookup_object.run(terms=u'', variables=None)
        assert False
    except AnsibleOptionsError as e:
        assert e.message == 'Invalid setting identifier, "" is not a string, its a <type \'unicode\'>'

    # test None is not integer
    try:
        lookup_object.run(terms=0, variables=None)
        assert False
    except AnsibleOptionsError as e:
        assert e

# Generated at 2022-06-13 13:23:57.240411
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible_collections.ansible.builtin.plugins.lookup.config import LookupModule

    config = LookupModule()

    # _get_global_config(config):
    assert config._get_global_config('DEFAULT_BECOME_METHOD') == 'sudo'
    with pytest.raises(Exception) as excinfo:
        assert config._get_global_config('_C.DEFAULT_BECOME_METHOD')
    assert "Invalid setting identifier" in str(excinfo.value)

    # _get_plugin_config(pname, ptype, config, variables):
    assert config._get_plugin_config('netconf', 'cliconf', 'ssh_args', 'variables') == '-o ControlMaster=auto -o ControlPersist=60s'