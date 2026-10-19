

# Generated at 2022-06-13 13:16:05.762092
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    def _get_plugin_config(pname, ptype, config, variables):
        return config

    def _get_global_config(config):
        return config

    lookup_module = LookupModule()

    terms = ['DEFAULT_REMOTE_USER', 'DEFAULT_REMOTE_TMP']
    variables = {'DEFAULT_REMOTE_USER': 'ansible', 'DEFAULT_REMOTE_TMP': '/tmp'}
    ptype = 'shell'
    pname = 'sh'
    missing = 'error'

    # Execute
    result = lookup_module.run(terms, variables, plugin_type=ptype, plugin_name=pname, on_missing=missing)

    # Verify
    assert result == terms



# Generated at 2022-06-13 13:16:16.953286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test_helper(**kwargs):
        return LookupModule().run(['not_existed'], variables=None, **kwargs)

    # test with on_missing 'error'
    res_1 = test_helper(on_missing='error')
    assert res_1 == []

    # test with on_missing 'skip'
    res_2 = test_helper(on_missing='skip')
    assert res_2 == []

    # test with on_missing 'warn', but get warning when we run lookup
    res_3 = test_helper(on_missing='warn')
    assert res_3 == []

    # test with on_missing 'error' and valid term
    res_4 = test_helper(terms=['DEFAULT_BECOME_USER'], on_missing='error')
    assert res_

# Generated at 2022-06-13 13:16:26.325389
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os

    # check for pytest for the test
    pytest_found = False
    try:
        import pytest
        pytest_found = True
    except ImportError as e:
        print('pytest module not found. It is needed for testing. %s' % to_native(e))

    if not pytest_found:
        sys.exit(1)

    # set ansible home path to current directory, such that module can be loaded in current directory
    os.environ['ANSIBLE_HOME'] = os.getcwd()

    # load ansible module
    lookup_module = LookupModule()

    # lookup for existing parameter
    result = lookup_module.run(terms=['INVENTORY_ENABLED'], variables={})
    assert len(result) == 1
    assert result[0]

# Generated at 2022-06-13 13:16:36.668179
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:16:40.461527
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test correct path
    global C
    C = type('', (), {})

    # Test for plugin_type and plugin_name provided
    test_obj = LookupModule()
    test_terms = ['remote_user', 'port']
    test_variables = dict()
    test_kwargs = dict(plugin_type='connection', plugin_name='ssh')

    # method run
    result = test_obj.run(test_terms, test_variables, **test_kwargs)

    # Assertion
    assert result == ['remote_user', 'port']

    # Test for plugin_type and plugin_name provided
    test_obj = LookupModule()
    test_terms = ['remote_tmp']
    test_variables = dict()
    test_kwargs = dict(plugin_type='shell', plugin_name='sh')

# Generated at 2022-06-13 13:16:50.839195
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class DummyLookupPlugin(LookupBase):
        def run(self, terms, variables=None, **kwargs):
            pass

    plugin = DummyLookupPlugin()

    with pytest.raises(AnsibleOptionsError) as ansible_options_error:
        plugin.run(['unsupported'], {}, plugin_type='unsupported', plugin_name='unsupported')

    assert ansible_options_error.value.message == \
        'Both plugin_type and plugin_name are required, cannot use one without the other'

    with pytest.raises(AnsibleOptionsError) as ansible_options_error:
        plugin.run(['unsupported'], {}, plugin_type='unsupported')


# Generated at 2022-06-13 13:16:56.285740
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy

    assert ret == ['test', 'test2']

    # test on missing option
    assert ret == ['test', None]

    # test on wrong setting name
    assert ret == ['test']

    # test on plugin type
    plugin = [{'name': 'test_name', 'type': 'test_type', 'setting_name': 'test_setting_name'},
              {'name': 'test_name', 'type': 'test_type', 'setting_name': 'test_setting_name_no_exist', 'expected': None}]

    assert ret == ['test', None]

# Generated at 2022-06-13 13:17:05.452317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.cli.config import AnsibleConfigCLI
    from ansible.config.manager import ConfigManager
    from ansible.errors import AnsibleFileNotFound
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_text

    class TestConfigCLI(AnsibleConfigCLI):
        def __init__(self, args=None):
            super(TestConfigCLI, self).__init__()
            self.args = args or []

        def run(self):
            self.parse(self.args)
            self.run_subcommand()

    cm = ConfigManager()


# Generated at 2022-06-13 13:17:15.104521
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3

    from ansible.plugins.loader import connection_loader
    conn = connection_loader.get('local', class_only=True)

    # test loading of global config
    l = LookupModule()
    l.get_option = lambda *args, **kwargs: None  # skip any option processing
    assert l.run(['HOST_KEY_CHECKING']) == [C.HOST_KEY_CHECKING]
    assert l.run(['HOST_KEY_CHECKING', 'DEFAULT_BECOME_USER']) == [C.HOST_KEY_CHECKING, C.DEFAULT_BECOME_USER]


# Generated at 2022-06-13 13:17:20.002123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'on_missing': 'error'})
    terms = ['remote_tmp']
    result = lookup_module.run(terms, plugin_type="shell", plugin_name="sh")
    assert '$HOME/.ansible/tmp' in result


# Generated at 2022-06-13 13:17:43.238522
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test plugin config
    plugin = LookupModule()
    plugin.set_options({'plugin_type': 'shell',
                        'plugin_name': 'sh',
                        'var_options': {},
                        'direct': {'on_missing': 'error'}})
    ret = plugin.run(terms=["remote_tmp"])
    assert len(ret) == 1
    assert ret[0] == '/tmp/${USER}'

    # Test global config
    plugin.set_options({'plugin_type': None,
                        'plugin_name': None,
                        'var_options': {},
                        'direct': {'on_missing': 'error'}})
    ret = plugin.run(terms=["DEFAULT_REMOTE_USER"])
    assert len(ret) == 1
    assert ret[0] == 'root'

# Generated at 2022-06-13 13:17:54.351538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Fixture
    modules_path = os.path.join(os.path.dirname(__file__), '../../../')
    ansible_builtin = os.path.join(modules_path, 'ansible/modules/extras/')
    config = C.ConfigParser()
    config.ansible_managed = 'Test'
    config.rejections = 'all'
    config.roles_path = os.path.join(os.path.expanduser('~'), 'test_roles')
    config.library = '/usr/share/ansible'
    config.module_utils = os.path.join(modules_path, 'ansible/module_utils')
    config.filter_plugins = os.path.join(modules_path, 'ansible/plugins/filter')
    config.lookup_plugins = os

# Generated at 2022-06-13 13:18:01.946664
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Without arguments
    module = LookupModule()
    assert module.run(terms=None) == []

    # Bad argument "None"
    module = LookupModule()
    assert module.run(terms=[None]) == []

    # Bad argument "1"
    module = LookupModule()
    assert module.run(terms=[1]) == []

    # Bad argument "True"
    module = LookupModule()
    assert module.run(terms=[True]) == []

    # Fallback on Config value
    module = LookupModule()
    assert module.run(terms=["ANSIBLE_SSH_RETRIES"]) == [5]

# Generated at 2022-06-13 13:18:09.782424
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TEST 1: Missing Global Setting
    bad_setting_1 = "ThisSettingDoesNotExist"
    with pytest.raises(AnsibleLookupError, match='Unable to find setting %s' % bad_setting_1) as exc_info:
        LookupModule().run([bad_setting_1], on_missing='error')
    assert exc_info.type == AnsibleLookupError
    assert exc_info.value.to_native() == 'Unable to find setting %s' % bad_setting_1

    # TEST 2: Missing Global Setting - ON_MISSING = 'warn'
    bad_setting_2 = "AnotherSettingThatDoesNotExist"
    LookupModule().run([bad_setting_2], on_missing='warn')

    # TEST 3: Missing Global Setting - ON_MISSING = 'skip

# Generated at 2022-06-13 13:18:25.077602
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = []

    class look(object):
        def __init__(self):
            self.hello = 'Hello'
    lookup = look()

    ret1 = {'test1': 'test1', 'test2': 'test2'}
    ret2 = ['test1', 'test2']
    ret3 = 'test1'
    ret4 = {'t1': 't1', 't2': 't2', 't3': 't3'}

    result.append(ret1)
    result.append(ret2)
    result.append(ret3)
    result.append(ret4)

    lm = LookupModule(loader=lookup, basedir="")
    r1 = lm.run([ret1], {})
    r2 = lm.run([ret2], {})
    r3

# Generated at 2022-06-13 13:18:31.216595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.sentinel import Sentinel
    lookup_module = LookupModule
    lookup_module.set_options = lambda self, var_options=None, direct=None: None
    lookup_module.get_option = lambda self, var: None

    # on_missing != 'error'
    lookup_module.get_option = lambda self, var: "skip"
    assert lookup_module().run(terms=("DEFAULT_ROLES_PATH", )) == []



# Generated at 2022-06-13 13:18:39.415027
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test cases
    tests = [
        # First test case: Test with no plugin_type or plugin_name.
        {
            'terms': {'terms': 'TEST_RUN'},
            'variables': {'variables': 'TEST_RUN'},
            'kwargs': {'kwargs': 'TEST_RUN'},
            'expected_ret': [],
            'expected_result': False,
        },
    ]

    for test in tests:
        # Create a mock class for class LookupModule
        LookupModule_class_mock = LookupModule(
            loader=None,
            variables=test['variables'],
        )

        # Call method run of LookupModule with specifed test case

# Generated at 2022-06-13 13:18:42.282576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['_terms', 'plugin_type', 'plugin_name', 'on_missing']
    variables = {'_terms': 'var1', 'plugin_type': 'shell',
                 'plugin_name': 'sh', 'on_missing': 'error'}
    lookup = LookupModule()
    result = lookup.run(terms, variables)
    assert result



# Generated at 2022-06-13 13:18:51.172903
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Testing with invalid setting identifier
    terms = ['hello', 1, 'world']
    with pytest.raises(AnsibleOptionsError) as execinfo:
        module.run(terms, variables=None, on_missing=None, plugin_type=None, plugin_name=None)
    assert "Invalid setting identifier" in to_native(execinfo)

    # Testing with missing plugin_type and plugin_name
    terms = ['default_foo']
    with pytest.raises(AnsibleOptionsError) as execinfo:
        module.run(terms, variables=None, on_missing=None, plugin_type=None, plugin_name=None)
    assert "Both plugin_type and plugin_name are required" in to_native(execinfo)

    # Testing with missing plugin_name

# Generated at 2022-06-13 13:19:01.153073
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a LookupModule object to use
    lookup_module = LookupModule()

    # CONFIG_FILE is defined in constants
    terms = ['CONFIG_FILE']
    results = lookup_module.run(terms, variables=None)
    assert results == ['/etc/ansible/ansible.cfg']

    # CONFIG_FILE is defined in constants
    terms = ['CONFIG_FILE']
    results = lookup_module.run(terms, variables=[])
    assert results == ['/etc/ansible/ansible.cfg']

    # CONFIG_FILE is defined in constants
    terms = ['DEFAULT_ROLES_PATH']
    results = lookup_module.run(terms, variables=None)

# Generated at 2022-06-13 13:19:38.233676
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Check if empty term
    try:
        lookup_module.run()
    except Exception as e:
        assert type(e) == AnsibleLookupError
        assert e.args[0] == "with_config lookup expects one or more config terms"

    # Check term is string
    try:
        lookup_module.run([{"config_key": "some_value"}])
    except Exception as e:
        assert type(e) == AnsibleOptionsError
        assert e.args[0] == 'Invalid setting identifier, "{\'config_key\': \'some_value\'}" is not a string, its a <class \'dict\'>'

    # Check if MissingSetting exception is handled

# Generated at 2022-06-13 13:19:52.146309
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    import tempfile
    import os

    # Creating a file for testing
    (fd, fname) = tempfile.mkstemp()

# Generated at 2022-06-13 13:19:58.774513
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run(['DEFAULT_ROLES_PATH'])
    l.run(['DEFAULT_ROLES_PATH'], variables={'DEFAULT_ROLES_PATH': [u'/home/roles']}, on_missing='skip')
    l.run(['DEFAULT_ROLES_PATH'], variables={'DEFAULT_ROLES_PATH': u'/home/roles'}, on_missing='skip')
    return True

# Generated at 2022-06-13 13:20:04.539933
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    import ansible.plugins.loader as plugin_loader
    plugin_loader.find_plugin_paths()
    lu.set_options({ 'plugin_type':'connection', 'plugin_name':'local'})

    res = lu.run([ to_native("executable"), to_native("remote_tmp")])

    assert res == ['python', '/tmp']
    assert lu._display.default.warning_count == 0
    assert lu._display.default.error_count == 0

# Generated at 2022-06-13 13:20:08.125076
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["DEFAULT_BECOME_USER", "remote_user", "port", "remote_tmp"]
    result = LookupModule().run(terms)
    assert result[0] == "root"
    assert result[1] == "root"
    assert result[2] == "22"
    assert "temp" in result[3]

# Generated at 2022-06-13 13:20:19.007299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test 1: Action to take when key is missing from config
    test_cases = {
        'error': {
            'terms': ['UNKNOWN_CONFIG_KEY'],
            'on_missing': 'error',
            'error_msg': "Unable to find setting UNKNOWN_CONFIG_KEY",
        },
        'skip': {
            'terms': ['UNKNOWN_CONFIG_KEY'],
            'on_missing': 'skip',
            'expected_result': []
        },
        'warn': {
            'terms': ['UNKNOWN_CONFIG_KEY'],
            'on_missing': 'warn',
            'warning_msg': "Skipping, did not find setting UNKNOWN_CONFIG_KEY",
            'expected_result': []
        },
    }

# Generated at 2022-06-13 13:20:23.962747
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test case 1
    terms_1 = ["COLOR_HIGH", "color_low"]
    variables_1 = {}
    expected_result_1 = {'_raw': ['']}

    result_1 = LookupModule().run(terms=terms_1, variables=variables_1)

    assert(result_1[0] == expected_result_1)




# Generated at 2022-06-13 13:20:37.290925
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyC(object):

        @staticmethod
        def get_config_value(*arg, **kwargs):
            return 'test'

    C.get_config_value = DummyC.get_config_value

    class DummyLookupBase(LookupBase):

        def __init__(self, *args, **kwargs):
            self.result = None

        def get_option(self, option):
            return self.result

    class DummyAnsibleOptionsError(AnsibleOptionsError):
        pass

    class DummyAnsibleLookupError(AnsibleLookupError):
        pass

    class DummyAnsibleError(AnsibleError):
        pass

    class DummySentinel(Sentinel):
        pass

    dummy_ansible_options_error = DummyAnsibleOptionsError()

# Generated at 2022-06-13 13:20:43.574660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Find retry files, skip if missing that key'''
    os_options = dict(plugin_type='shell',
                      plugin_name='sh')
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={'playbook_dir':'/home/ansible'},
                              direct=os_options)
    result = lookup_module._templar.template("{{q('config', 'remote_tmp')}}")
    assert result == '/var/tmp'

# Generated at 2022-06-13 13:20:44.613014
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 1 == 1

# Generated at 2022-06-13 13:21:20.023959
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inventory)

    plugin_name = 'ping'
    config_term = 'remote_tmp'
    expected_result = '/tmp'

    lookup_plugin = LookupModule()
    result = lookup_plugin.run([config_term], variables=variable_manager, plugin_type='connection', plugin_name=plugin_name)

    assert result[0] == expected_result, 'Result was not equal to expected result!'

# Generated at 2022-06-13 13:21:22.077120
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_USER']
    kwargs = {'on_missing': 'error'}
    variables = {}
    kwargs = {}

    expected = ['root']

    result = LookupModule().run(terms, variables, **kwargs)
    assert result == expected


# Generated at 2022-06-13 13:21:32.934996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(None, direct={'on_missing': 'error'})
    assert l.run(['invalid_setting']) == ['error']
    assert l.run(['DEFAULT_SUDO_USER']) == [C.DEFAULT_SUDO_USER]
    assert l.run(['DEFAULT_SUDO_USER']) == [C.DEFAULT_SUDO_USER]
    assert l.run(['DEFAULT_SUDO_USER', 'DEFAULT_BECOME_USER']) == [C.DEFAULT_SUDO_USER, C.DEFAULT_BECOME_USER]
    assert l.run(['invalid_setting', 'DEFAULT_BECOME_USER']) == ['error', C.DEFAULT_BECOME_USER]

# Generated at 2022-06-13 13:21:39.866652
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_METHOD', 'remote_port', 'remote_user']
    plugin_type="connection"
    plugin_name="ssh"
    on_missing="error"

    lk = LookupModule()
    ans = lk.run(terms,plugin_type=plugin_type,plugin_name=plugin_name,on_missing=on_missing)
    print(ans)


if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 13:21:48.550228
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Initialize data for tests
    lookup_class = LookupModule()
    lookup_class.set_options()
    lookup_class.set_options(var_options={})

    # Test that correct value is returned for given settings
    result = lookup_class.run(["DEFAULT_STDOUT_CALLBACK"])
    assert result[0] == "default"

    # Test that settings that are not available raises exception
    with pytest.raises(AnsibleLookupError) as excinfo:
        lookup_class.run(["DEFAULT_STDOUT_CALLBACK123"])
    assert 'did not find setting' in to_native(excinfo.value)

# Generated at 2022-06-13 13:21:54.632723
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for find_plugin class method 
    lookup = LookupModule()
    # Test for find_plugin class method 
    def test_run_with_missing_plugin_type():
        lookup.run(terms=['httpapi'],
                   variables=dict(ansible_connection='httpapi'),
                   plugin_name='httpapi',
                   )
    # Test for find_plugin class method 
    def test_run_with_missing_plugin_name():
        lookup.run(terms=['var'],
                   variables=dict(ansible_connection='httpapi'),
                   plugin_type='connection',
                   )

# Generated at 2022-06-13 13:21:59.470511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    l = LookupModule()

    # Test cases for constants with value 'True' or 'False'
    test_cases = [
        ('C.DEFAULT_KEEP_REMOTE_FILES', True, [True]),
        ('C.COLLECT_IGNORE', ['*'], [['*']]),
        ('NOT_A_CONST', 'default_value', ['default_value'])
    ]

    for term, default, expected in test_cases:
        result = l.run([term], {}, on_missing='default', **{'default': default})
        assert result == expected

    # Test cases for constants without a default value

# Generated at 2022-06-13 13:22:06.555213
# Unit test for method run of class LookupModule
def test_LookupModule_run():
   lookup=LookupModule()

# Generated at 2022-06-13 13:22:08.538049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    try:
        lookup.run([])
    except TypeError:
        pass


# Generated at 2022-06-13 13:22:19.646055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ["DEFAULT_ROLES_PATH", "remote_user", "remote_tmp", "port", "UNKNOWN"]
    variables = {"playbook_dir": "fake/playbook/dir"}
    plugin_type = 'connection'
    plugin_name = 'ssh'
    # test with global config
    result = module.run(terms, variables=variables)
    assert(result == [['fake/playbook/dir/roles', '/etc/ansible/roles'], 'root', '/tmp', 22])
    # test with plugin config
    result = module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name)
    assert(result == ['root', '/tmp', 22])
    # test with unknown config

# Generated at 2022-06-13 13:23:28.307814
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lu = LookupModule()
    lu.set_options(var_options=None, direct=dict())
    with pytest.raises(AnsibleOptionsError):
        lu.run([])
    with pytest.raises(AnsibleOptionsError):
        lu.run(['a', 'b'])
    with pytest.raises(AnsibleOptionsError):
        lu.run(['a'], dict(one='uno'))
    with pytest.raises(AnsibleOptionsError):
        lu.run(['a'], dict(one='uno', two='dos'))
    with pytest.raises(AnsibleOptionsError):
        lu.run(['a'], dict(on_missing="meow"))

# Generated at 2022-06-13 13:23:43.789259
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup = lookup_loader.get('config')

    # Valid case - when C.DEFAULT_VAULT_IDENTITY_LIST
    setattr(C, 'DEFAULT_VAULT_IDENTITY_LIST', 'dummy-value')
    result = lookup.run([ 'DEFAULT_VAULT_IDENTITY_LIST' ], variables={})
    assert result == [ 'dummy-value' ]
    assert result[0] == 'dummy-value'

    # Valid case - when C.DEFAULT_MODULE_NAME does not exist
    # Check if sentinel value is returned
    result = lookup.run([ 'DEFAULT_MODULE_NAME' ], variables={})
    assert result == []

    # Valid case - when with more than one term

# Generated at 2022-06-13 13:23:55.949880
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test good case
    from collections import namedtuple
    fake_loader = namedtuple('fake_loader', ['__contains__', 'get'])
    fake_plugin = namedtuple('fake_plugin', ['_load_name', '_load_name'])
    fake_options = namedtuple('fake_options', ['var_options', 'direct'])
    fake_display = namedtuple('fake_display', ['warning'])

    terms = ['foo', 'bar']

    fake_loader.get.return_value = fake_plugin
    fake_loader.__contains__.return_value = True
    plugin_loader.__dict__['shell_loader'] = fake_loader
    constants = {}
    constants['BAR'] = 'Value_Of_BAR'
    C.__dict__ = constants
    config = Look

# Generated at 2022-06-13 13:24:05.117367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # test error missing on_missing option
    terms = ['CHECKMODE']
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(terms)

    # test on_missing=warn, term is missing
    kwargs = dict(on_missing='warn')
    lookup_module.run(terms, **kwargs)

    # test term is found and on_missing=warn
    kwargs = dict(on_missing='warn', port='22')
    lookup_module.run(terms, **kwargs)

    # test on_missing=error, term is missing
    kwargs = dict(on_missing='error')
    with pytest.raises(AnsibleLookupError):
        lookup_module.run(terms, **kwargs)

    # test

# Generated at 2022-06-13 13:24:16.030383
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a LookupModule instance
    lm = LookupModule()

    # create a mock srv_spec
    class MockPlayContext(dict):
        def __init__(self):
            pass

    # Create a mock set_options
    def mock_set_options(self, var_options=None, direct=None):
        return

    lm.set_options = mock_set_options

    # Create a mock get_option
    def mock_get_option(self, option_name=None):
        return None

    lm.get_option = mock_get_option

    # Create a mock set_options
    def mock_set_options(self, var_options=None, direct=None):
        pass

    lm.set_options = mock_set_options

    # Create a mock set_options

# Generated at 2022-06-13 13:24:28.444778
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test for method run of class LookupModule """
    lookup = LookupModule()
    lookup_result = lookup.run(terms=["DEFAULT_BECOME_USER"])
    assert lookup_result == ['root']
    lookup_result = lookup.run(terms=["DEFAULT_BECOME_USER", "COW_SELECTION"])
    assert lookup_result == ['root', 'random']
    lookup_result = lookup.run(terms=["DEFAULT_BECOME_USER", "UNKNOWN_VALUE"], on_missing='warn')
    assert lookup_result == ['root']
    lookup_result = lookup.run(terms=["DEFAULT_BECOME_USER", "UNKNOWN_VALUE"], on_missing='skip')
    assert lookup_result == ['root']

# Generated at 2022-06-13 13:24:37.085212
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a temporary file containing
    # some variables
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as f:
        f.write("""
---
ansible_connection: local
ansible_python_interpreter: /usr/bin/python
ansible_python_interpreter: "{{__ansible_python_interpreter}}"
""")
    # Create a lookup module using this file
    # as vars file
    l = LookupModule(loader=None, templar=None, vars_loader=VarsModule({'vars_files':[path]}))
    # Run the test
    l.run([])

# Generated at 2022-06-13 13:24:45.387348
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config_val = {
        'a': 'b',
        'c': 'd',
        'e': 'f',
    }
    actual = LookupModule().run(['a', 'c', 'e'], config_val)
    assert actual == ['b', 'd', 'f']

    actual = LookupModule().run(['a', 'c', 'missing'], config_val, on_missing='warn')
    assert actual == ['b', 'd']

    actual = LookupModule().run(['a', 'c', 'missing'], config_val, on_missing='skip')
    assert actual == ['b', 'd']

# Generated at 2022-06-13 13:24:53.318162
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test case: terms is defined as a list
    terms = ['DEFAULT_ROLES_PATH']
    ret = LookupModule().run(terms, variables={}, plugin_type=None, plugin_name=None, on_missing='error')
    assert ret == ['/Users/johndoe/ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles', '/etc/ansible/roles'], "Return value should be a list without being empty"

    # Test case: terms is defined as a list
    terms = ['remote_user']
    ret = LookupModule().run(terms, variables={}, plugin_type='connection', plugin_name='ssh', on_missing='error')
    # ret should have a list of 2 values for DEFAULT_REMOTE_USER
    assert len(ret) == 2

# Generated at 2022-06-13 13:24:58.565837
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    # 
    # Unit test for the run method of class LookupModule
    #
    # 
    # The parameters to the test method are as follows:
    # 
    # term: A term or list of terms.
    # variables: The playbook variables. Can be None.
    #
    # returns:
    # None: The test passed.
    # raise AnsibleOptionsError: The test failed.
    #
    # This unit test not does not set the callback plugin. So it is not expected to send any
    # messages to the callback. Any calls to the callback will be captured and any exceptions
    # raised by the callback will be caught.
    #
    # The tests have the following functionalities:
    #
    # test that:
    # the method should return