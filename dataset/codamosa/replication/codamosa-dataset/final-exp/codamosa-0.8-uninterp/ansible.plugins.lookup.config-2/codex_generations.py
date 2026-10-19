

# Generated at 2022-06-13 13:16:14.468112
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text

    # Construct a request
    request = {
        'terms': ['DEFAULT_ROLES_PATH', 'nope'],
        'on_missing': 'warn'
    }

    lookup = LookupModule()
    lookup.set_loader(None) # Use default loader
    lookup._display.warning = lambda x: None # Suppress display.warning which is called by on_missing='warn'
    result = lookup.run(**request)

    assert result == [C.DEFAULT_ROLES_PATH]


# Generated at 2022-06-13 13:16:24.678740
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.constants as C
    from ansible.plugins.lookup.config import LookupModule
    C.DEFAULT_ROLES_PATH = ['/home/ansible/roles']

    lookup_plugin = LookupModule()
    terms = ['DEFAULT_ROLES_PATH']
    result = lookup_plugin.run(terms)
    assert result[0] == '/home/ansible/roles'

    # Test the on_missing behaviour
    result = lookup_plugin.run(['test'], on_missing='error')
    assert result == None
    result = lookup_plugin.run(['test'], on_missing='warn')
    assert result == None
    result = lookup_plugin.run(['test'], on_missing='skip')
    assert result == None

    # Test the ptype, pname behaviour

# Generated at 2022-06-13 13:16:30.961574
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_USER', 'SHOULD_NOT_EXIST']

    # arguments
    module = LookupModule()
    # Successes
    result = module.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result == ["root"]

    # Warnings
    result = module.run(terms, on_missing='warn')
    assert isinstance(result, list)
    assert len(result) == 1
    assert result == ["root"]

    # Skips
    result = module.run(terms, on_missing='skip')
    assert isinstance(result, list)
    assert len(result) == 1
    assert result == ["root"]

# Generated at 2022-06-13 13:16:37.989038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options( direct={"plugin": None , "plugin_type": 'cache', "plugin_name": 'memory'})
    assert lookup_module.run([]) == []

    lookup_module.set_options( direct={"plugin": None , "plugin_type": 'cache', "plugin_name": 'memory'})
    assert lookup_module.run(["cache_dir"]) == ['/var/tmp/ansible/tmpW8Vv3Z']

    lookup_module.set_options( direct={"plugin": None , "plugin_type": 'cache', "plugin_name": 'memory'})

# Generated at 2022-06-13 13:16:38.915697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True


# Generated at 2022-06-13 13:16:43.096192
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = dict(terms='test_run', variables='test_run', direct='test_run')
    k = LookupModule()
    k.set_options(var_options=args['variables'], direct=args['direct'])


# Generated at 2022-06-13 13:16:53.507889
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # generate a plugin_loader, fix the module_utils path and get the plugin_loader.connection_loader
    plugin_loader.add_directory(None)
    connection_loader = plugin_loader.connection_loader

    # generate a ConnectionModule object for netconf plugin
    conn = connection_loader.get('netconf', class_only=True)

    # generate a LookUpBase object
    lookup = LookupBase()

    # generate a set of options for the LookUpBase object
    var_options = {u'playbook_dir': u'.', u'transport': u'netconf', u'play_hosts': [u'localhost'], u'inventory_hostname': u'localhost'}
    direct = {'plugin_type': 'connection', 'plugin_name': 'netconf'}

    # Call the set_options method of the Look

# Generated at 2022-06-13 13:16:59.308660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize the class object
    myLookupModule = LookupModule()
    #Call the run method
    result = myLookupModule.run(["remote_user", "port"], plugin_name="ssh", plugin_type="connection")
    assert result != [None], "Expected not None, got None"
    result = myLookupModule.run(["remote_tmp"], plugin_name="sh", plugin_type="shell")
    assert result != [None], "Expected not None, got None"
    result = myLookupModule.run(["remote_user", "port"], plugin_name="ssh", plugin_type="connection", on_missing="warn")
    assert result != [None], "Expected not None, got None"

# Generated at 2022-06-13 13:17:07.571448
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # test with missing plugin name
    module.set_options(plugin_name='', plugin_type='', on_missing='error')
    ret = module.run(['remote_user', 'port'])
    assert ret[0] == 'root'
    assert ret[1] == '22'
    # test with valid plugin name
    module.set_options(plugin_name='ssh', plugin_type='connection', on_missing='warn')
    ret = module.run(['remote_user', 'port'])
    assert ret[0] == 'root'
    assert ret[1] == '22'
    # test with invalid plugin name
    module.set_options(plugin_name='abc', plugin_type='connection', on_missing='skip')

# Generated at 2022-06-13 13:17:16.150492
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.config import LookupModule
    import ansible.constants as constants
    import ansible.errors as errors
    from ansible.module_utils._text import to_text

    # list of ansible constants that are callables
    constants_list = ['DEFAULT_BECOME_METHOD']

    # negative test cases

# Generated at 2022-06-13 13:17:31.038167
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = 'DEFAULT_BECOME_USER'
    variables = ''
    args = {'plugin_type': '', 'plugin_name': '', 'on_missing': 'error'}
    return LookupModule().run(terms, variables, **args)

# Generated at 2022-06-13 13:17:39.172660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()

    # Simple test for run, in this dummy test for run we will only just check the
    # execution of run method. We are checking all the scenario's in LookupModule
    # in test_config_lookup_plugin.py
    c = LookupModule()
    c.set_loader(loader)
    c.set_variable_manager(variable_manager)

    # missing type is not a string or error, warn or skip.
    args = dict(terms='DEFAULT_ROLES_PATH', on_missing='something')
    try:
        c.run(**args)
    except AnsibleOptionsError as e:
        assert str(e)

# Generated at 2022-06-13 13:17:50.591561
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'on_missing':'error'})
    assert lookup_module.run(['DEFAULT_BECOME_USER'])[0] == 'root'
    assert lookup_module.run(['DEFAULT_ROLES_PATH'])[0] == ['/etc/ansible/roles', '/usr/share/ansible/roles']
    assert lookup_module.run(['COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP']) == ['green', 'yellow', 'cyan']
    assert lookup_module.run(['DEFAULT_ROLES_PATH'])[0] == ['/etc/ansible/roles', '/usr/share/ansible/roles']

# Generated at 2022-06-13 13:18:00.796040
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()

    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    plugin = LookupModule()

    # test 1

    terms = [
        'INVALID_TERM',
    ]

    plugin._display.warning = lambda text: True
    plugin.set_options(var_options=None)

    result = plugin.run(
        terms=terms,
    )
    assert result == []

    # test 2

    terms = [
        'INVALID_TERM',
    ]

    plugin._display

# Generated at 2022-06-13 13:18:09.011140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(
            _terms=dict(type='list', required=True),
            on_missing=dict(type='str', required=False),
            plugin_type=dict(type='str', required=False),
            plugin_name=dict(type='str', required=False),
            )
        )
    terms = ['_DEFAULT_ROLES_PATH', '_CACHE_PLUGIN']
    plugin_name = 'memory'
    config = LookupModule()
    result = config.run(terms, plugin_name=plugin_name)
    assert result[0] == C.DEFAULT_ROLES_PATH
    assert result[1] == C.CACHE_PLUG

# Generated at 2022-06-13 13:18:15.033141
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Input values
    terms = [
        'DEFAULT_BECOME_USER'
    ]
    variables = {'foo': 'foo'}
    kwargs = {'bar':'bar'}
    # Return value
    ret = [
        u'root'
    ]

    lookupObj = LookupModule()
    lookupObj._display = Display()
    result = lookupObj.run(terms=terms, variables=variables, **kwargs)
    assert result == ret


# Generated at 2022-06-13 13:18:25.083298
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    const_mock = Mock(return_value=None)
    const_mock.action_plugins = ['/home/runner/work/ansible/ansible/lib/ansible/plugins/action']
    const_mock.callback_plugins = ['/home/runner/work/ansible/ansible/lib/ansible/plugins/callback']
    const_mock.connection_plugins = ['/home/runner/work/ansible/ansible/lib/ansible/plugins/connection']
    const_mock.shell_plugins = ['/home/runner/work/ansible/ansible/lib/ansible/plugins/shell']
    const_mock.module_utils = ['/home/runner/work/ansible/ansible/lib/ansible/module_utils']

# Generated at 2022-06-13 13:18:26.734900
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    l.set_loader(plugin_loader)

    # test run with no parameter
    assert l.run([]) == []

# Generated at 2022-06-13 13:18:35.975122
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create instance of LookupModule class
    obj = LookupModule()

    # check runs successfully with terms
    terms = 'DEFAULT_ROLES_PATH'
    result = obj.run(terms)
    assert result is not None
    assert result[0] is not None

    # check runs successfully with multiple terms
    terms = ['DEFAULT_ROLES_PATH', 'DEFAULT_MODULE_NAME']
    result = obj.run(terms)
    assert result is not None
    assert len(result) == 2

    # check runs successfully with terms and plugin_type
    terms = 'remote_tmp'
    plugin_type = 'shell'
    result = obj.run(terms, plugin_type)
    assert result is not None
    assert isinstance(result[0], str)
    assert '$HOME/.ansible/tmp'

# Generated at 2022-06-13 13:18:46.627134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #import xmlrunner
    #import sys
    #import unittest
    #loader = unittest.TestLoader()
    #suite = loader.loadTestsFromModule(sys.modules[__name__])
    #runner = xmlrunner.XMLTestRunner(output='test-reports')
    #runner.run(suite)
    class TestLookupModule(unittest.TestCase):
        def test_run1(self):
            a = C.DEFAULT_REMOTE_TMP
            b = C.DEFAULT_ROLES_PATH
            class TestConfig:
                def __init__(self):
                    self.config = {'DEFAULT_REMOTE_TMP': a, 'DEFAULT_ROLES_PATH': b}

# Generated at 2022-06-13 13:19:03.133376
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(["foo", "bar"], on_missing="error")

# Generated at 2022-06-13 13:19:08.126691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ptype = 'lookup'
    pname = 'password'
    term = 'lookup_password_length'

    _get_plugin_config(pname, ptype, term, variables=None)
    _get_global_config(term)

# Generated at 2022-06-13 13:19:17.720352
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test to make sure the get_config() method of config.py called
    import ansible.module_utils.config as config_module
    import ansible.module_utils.six as six
    from mock import patch

    #Test case 1:
    # get_global_config() returns value
    # get_config() method called with expected parameters
    with patch.object(config_module, 'get_config') as mock_get_config:
        with patch.object(C, 'MY_GLOBAL_SETTING') as mock_attr:
            mock_attr = "MY_GLOBAL_SETTING"
            terms = ["MY_GLOBAL_SETTING"]
            mock_get_config.return_value = "test_value"
            lookup_obj = LookupModule()

# Generated at 2022-06-13 13:19:20.141957
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(terms=["CACHE_PLUGINS_ENABLE"], variables=None, on_missing='error', plugin_type=None, plugin_name=None) == [True]



# Generated at 2022-06-13 13:19:33.091022
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_dict = {
        'config_path': '/etc/ansible.cfg',
        'lookup_plugins_path': '/path/to/lookup_plugins',
        'filter_plugins_path': '/path/to/filter_plugins',
        'vars_plugins_path': '/path/to/vars_plugins'
    }
    lookup_module = LookupModule()
    result = lookup_module.run(terms=['config_path', 'lookup_plugins_path', 'filter_plugins_path', 'vars_plugins_path'],
                               variables=test_dict)
    assert result == ['/etc/ansible.cfg', '/path/to/lookup_plugins', '/path/to/filter_plugins', '/path/to/vars_plugins']

# Generated at 2022-06-13 13:19:39.989328
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    RETURNS_VALID_BOOLEAN_RESULT_FOR_VALID_VALUES = [
        (('DEFAULT_BECOME_USER',), True),
        (('DEFAULT_ROLES_PATH',), True),
        (('COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP'), True),
        (('COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP', 'COLOR_MISSING'), 'ValueError'),
        (('UNKNOWN',), 'AnsibleLookupError')
    ]
    RETURNS_RAISE_ERROR_FOR_INVALID_MISSING_OPTION = [
        ('missing_option', 'error'),
        ('missing_option', 'warn'),
        ('missing_option', 'skip')
    ]
    RETURNS_FALSE_FOR

# Generated at 2022-06-13 13:19:46.368388
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test that adding a setting that does not exist results in AnsibleLookupError
    l = LookupModule()
    l.set_options(var_options=None, direct={'on_missing':'error'})
    terms = ['FOO_BAR']
    try:
        l.run(terms)
        assert False
    except AnsibleLookupError:
        assert True


# Generated at 2022-06-13 13:19:55.114779
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This unit test verifies the expected behavior of the 'run' method
    of class LookupModule.

    It will fail if the method behaves otherwise.
    """
    C.DEFAULT_HOST_LIST = '/etc/ansible/hosts'
    terms = ['DEFAULT_HOST_LIST']
    variables = {}
    kwargs = {'ignore_errors': False, 'wantlist': True}
    lookup = LookupModule()
    assert(isinstance(lookup, LookupModule))
    expected = [C.DEFAULT_HOST_LIST]
    result = lookup.run(terms, variables, **kwargs)
    assert(result == expected)

# Generated at 2022-06-13 13:20:04.616964
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.utils import plugin_docs

    module = LookupModule()

    args = [
        '_terms=DEFAULT_ROLES_PATH',
        '_ansible_syslog_facility=LOG_USER',
        'plugin_type=shell',
        'plugin_name=sh',
        'remote_tmp',
        ]
    args = ' '.join(args).strip()
    res = module.run(terms=args.split())
    assert res == [C.DEFAULT_ROLES_PATH, C.LOG_USER, C.config.get_config_value('remote_tmp', ptype='shell', pname='sh')]

    res = module.run([])
    assert res == []

    res = module.run(args.split())


# Generated at 2022-06-13 13:20:10.592664
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Check all possible return value of method run.

    lookup_obj = LookupModule()
    lookup_obj.set_options({'on_missing': 'error'})

    # When terms is not a string
    terms = [1, 2, 3]
    try:
        lookup_obj.run(terms)
    except AnsibleOptionsError:
        print("test_LookupModule_run 1 passed")
    else:
        print("test_LookupModule_run 1 failed")

    # When terms is a string
    terms = ['DEFAULT_BECOME_USER']
    result = lookup_obj.run(terms, variables=None)
    if result == ['root']:
        print("test_LookupModule_run 2 passed")
    else:
        print("test_LookupModule_run 2 failed")

    # When  on

# Generated at 2022-06-13 13:20:43.476487
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """AnsibleLookupError is thrown when a user defined option type is passed to on_missing"""
    lookupMod = LookupModule()
    """Invalid value error is thrown when an invalid value is passed to on_missing"""
    lookupMod.run(terms=['foo'], variables={'bar': 'baz'}, on_missing='foo')

# Generated at 2022-06-13 13:20:47.207921
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(['']) == []
    assert lm.run(['a']) == []

# Generated at 2022-06-13 13:20:47.650276
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:20:50.390524
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    terms = [u'DEFAULT_BECOME_USER', u'DEFAULT_BECOME_PASS']
    result = lm.run(terms)
    assert result[0] == u'root'
    assert result[1] == u'', 'Expected empty string for DEFAULT_BECOME_PASS'

# Generated at 2022-06-13 13:21:04.189656
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._display = None

    # Result can be obtained only if configuration values exist
    assert lookup.run(['RETRY_FILES_ENABLED'], {}) == [True]

    # Result can not be obtained if there is no config value
    try:
        lookup.run(['UNKNOWN'], {})
    except AnsibleLookupError:
        pass
    else:
        assert False

    # Result can not be obtained if there is no config value
    try:
        lookup.run(['UNKNOWN'], {'on_missing': 'error'})
    except AnsibleLookupError as e:
        assert str(e) == 'Unable to find setting UNKNOWN'
    else:
        assert False

    # Result can not be obtained if there is no config value

# Generated at 2022-06-13 13:21:15.297450
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    fake_config = {'bar': 'baz'}
    fake_lookup = LookupModule()

    # test invalid on_missing
    fake_options = {'_terms': ['foo'], 'on_missing': 'invalid'}
    raised = False
    try:
        fake_lookup.run([], variables=fake_options)
    except AnsibleOptionsError as e:
        raised = True
    assert raised

    # test invalid config key
    fake_options = {'_terms': ['foo'], 'on_missing': 'warn'}
    # test warning that key is not found
    ret = fake_lookup.run([], variables=fake_options)
    assert ret == []

    # test warning that key is not found

# Generated at 2022-06-13 13:21:26.945702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', 'lookup_plugins'))

    class Options:
        remote_user = None
        remote_tmp = None
        connection = None
        shell = None

    class Config:
        def get_config_value(self, key, plugin_type, plugin_name, variables):
            return getattr(Options, plugin_name)

    class Display:
        def warning(self, msg):
            print('Warning: %s' % msg)

    class PluginLoader:
        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 13:21:29.617513
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert (LookupModule.run(LookupModule(), ['bogus']) is [None])

# Generated at 2022-06-13 13:21:33.011827
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # initialize test
    l = LookupModule()

    # simulate loading the lookup plugin
    l.set_options({
        'var_options': {},
        'direct': {},
        'plugin_type': 'config',
        'plugin_name': 'debug'
    })

    assert l.run(['DEBUG']) == [False]

# Generated at 2022-06-13 13:21:43.910234
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import ansible.plugins.loader as plugin_loader
    from ansible.errors import AnsibleOptionsError

    loader = plugin_loader.get('lookup', 'config')
    lookup_obj = loader.get()

    assert lookup_obj.run(['DEFAULT_BECOME_USER']) == ['root']
    assert lookup_obj.run(['DEFAULT_RETRY_FILES_ENABLED']) == ['False']
    assert lookup_obj.run(['DEFAULT_ROLES_PATH']) == ['/etc/ansible/roles:/usr/share/ansible/roles']
    assert lookup_obj.run(['DEFAULT_ROLES_PATH', 'DEFAULT_BECOME_USER']) == ['/etc/ansible/roles:/usr/share/ansible/roles', 'root']

   

# Generated at 2022-06-13 13:22:51.758975
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def get_global_config(config):
        if config == 'DEFAULT_REMOTE_USER':
            return 'root'
        return Sentinel

    def get_plugin_config(pname, ptype, config, variables):
        if config == 'remote_tmp':
            return '/tmp/remote_tmp'
        return Sentinel

    class MockDisplay:
        def __init__(self):
            self.warning_call_count = 0

        def warning(self, msg):
            self.warning_call_count += 1

    class MockVars:
        def __init__(self, myvar):
            self.myvar = myvar


# Generated at 2022-06-13 13:23:02.102754
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: use unittest module and remove this function
    # Test: used as test bed for bug fix of commit #e01317d
    class TestLookupModule(LookupModule):
        def __init__(self):
            self.ss = C.SubstitutionStrings()

        def run(self, terms, variables=None, **kwargs):
            print("Output:"+self.lookup('config', 'ANSIBLE_PIPELINING', on_missing='warn'))
            print("Output:"+self.lookup('config', 'PIPELINING', on_missing='warn'))

# Generated at 2022-06-13 13:23:06.990150
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup_plugin = lookup_loader.get('config')
    # test config that exists
    terms = ['DEFAULT_FORKS']
    config_value = lookup_plugin.run(terms)
    # test config that does not exist
    terms = ['UNKNOWN']
    config_value = lookup_plugin.run(terms)

# Generated at 2022-06-13 13:23:21.503262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    imports = {
        'AnsibleLookupError': AnsibleLookupError,
        'AnsibleError': AnsibleError,
        'C': C,
        'plugin_loader': plugin_loader,
        'Sentinel': Sentinel
    }
    exec(open(os.path.join(os.path.dirname(__file__), 'test_lookup_config.py')).read(), imports)
    test_LookupModule_run.__dict__.update(imports)

    terms = ['DEFAULT_ROLES_PATH', 'UNKNOWN']

    terms_with_plugin = ['remote_user', 'port']
    ptype_with_plugin = 'connection'
    pname_with_plugin = 'ssh'

    # test with invalid setting
    lm = LookupModule()
    test_

# Generated at 2022-06-13 13:23:31.848847
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # need to setup a fake class to run the tests
    class FakeVarsModuleUtil:
        def __init__(self):
            self.ansible_facts = {}

    class FakeOptions:
        def __init__(self):
            self.var_options = {}

    class FakePluginLoader:
        @staticmethod
        def become_loader():
            return FakePluginLoader

        @staticmethod
        def get(name, class_only=False):
            return FakePlugin

    class FakePlugin:
        _load_name = 'fake'
        class FakePluginSettings:
            def __init__(self):
                self.variable_manager = FakeVarsModuleUtil()
                return None

    # test setup
    fake_cls = FakePluginLoader()
    fake_opts = FakeOptions()
    fake_opts.var_

# Generated at 2022-06-13 13:23:45.667936
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    def test_missing_setting(mocker, tmp_path):
        lookup = LookupModule()

        with pytest.raises(MissingSetting, match=r'Error while trying to load settings'):
            lookup.run(['BAD_CONFIG'])

        with pytest.raises(MissingSetting, match=r'Unable to find setting BAD_CONFIG'):
            lookup.run(['BAD_CONFIG'], on_missing='error')

        with pytest.raises(AnsibleOptionsError, match=r'Invalid setting identifier, "BAD_CONFIG" is not a string'):
            lookup.run([42])


# Generated at 2022-06-13 13:23:57.728247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common._collections_compat import MutableMapping
    from operator import eq

    class TestVarsModule(MutableMapping):
        def __init__(self, host):
            self.host = host
            self.content = {
                'global_setting': 'global_setting_value',
            }
        def __getitem__(self, key):
            return self.content[key]
        def __setitem__(self, key, value):
            self.content[key] = value

# Generated at 2022-06-13 13:24:05.131796
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Test for missing option
    with pytest.raises(AnsibleOptionsError) as excinfo:
        lookup.run(terms='ansible_test')
    assert 'missing required options:' in str(excinfo.value)
    # Test for missing setting
    result = lookup.run(terms='ansible_test', on_missing='skip')
    assert result == []
    # Test for plugin_type but missing plugin_name
    with pytest.raises(AnsibleOptionsError) as excinfo:
        lookup.run(terms='remote_tmp', on_missing='skip', plugin_type='shell')
    assert 'Both plugin_type and plugin_name are required, cannot use one without the other' in str(excinfo.value)
    # Test for used setting

# Generated at 2022-06-13 13:24:16.031517
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import reload_module
    import ansible.plugins.loader as plugin_loader

    config = """
[defaults]
nocolor = 1
log_path = ansible_test.log

[inventory]
enable_plugins = ini

[privilege_escalation]
become = True
become_method = sudo
become_user = root
# This is a comment
become_ask_pass = false
    """

    # Create a file to pass in to ansible-config.
    # If ansible-config were used here, the config file would cause Ansible
    # to become root.
    with open('ansible_test.cfg', 'w') as f:
        f.write(config)

   

# Generated at 2022-06-13 13:24:30.073660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = None

    # pylint: disable=E0602
    module = sys.modules['ansible.plugins.lookup.config']
    test = module.test
    # pylint: enable=E0602

    # Test run() of LookupModule
    # 'lookup.config' is not a real plugin and does not come from 'ansible.plugins.loader'
    # which is why the module 'ansible.plugins.loader' is mocked and assigned to a local module
    # variable. The import statement for 'ansible.plugins.loader' is mocked so that this test
    # does not have to depend on the 'ansible.plugins.loader' module.