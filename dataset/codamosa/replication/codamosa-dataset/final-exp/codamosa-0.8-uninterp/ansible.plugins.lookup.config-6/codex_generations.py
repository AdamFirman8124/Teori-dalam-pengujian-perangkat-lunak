

# Generated at 2022-06-13 13:16:10.493830
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']
    variables = None
    on_missing = 'error'
    plugin_type = None
    plugin_name = None

    # Returned variable - print result
    result = LookupModule().run(terms, variables, on_missing=on_missing, plugin_type=plugin_type, plugin_name=plugin_name)
    print(result)

# Generated at 2022-06-13 13:16:18.244969
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(var_options=None, direct={})
    assert (l.run(terms=["COLOR_OK"],variables=None, on_missing="error") == ['green'])
    assert (l.run(terms=["COLOR_CHANGED"],variables=None, on_missing="error") == ['yellow'])
    assert (l.run(terms=["COLOR_SKIP"],variables=None, on_missing="error") == ['blue'])
    assert (l.run(terms=["COLOR_DIFF_ADD"],variables=None, on_missing="error") == ['diff_add'])
    assert (l.run(terms=["COLOR_DIFF_REMOVE"],variables=None, on_missing="error") == ['diff_remove'])

# Generated at 2022-06-13 13:16:20.287696
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = "DEFAULT_ROLES_PATH"
    kwargs = {'on_missing': 'error'}
    result = module.run(terms, None, **kwargs)
    assert result == ['/etc/ansible/roles:/usr/share/ansible/roles']

# Generated at 2022-06-13 13:16:28.358443
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    lookup_module.set_templar(None)
    lookup_module.set_loader_object(None)

    # test for get_global_config
    assert lookup_module.run(['DEFAULT_SUDO_USER']) == ['root']
    assert lookup_module.run(['DEFAULT_SUDO_USER'], on_missing='warn') == ['root']

    # test for get_plugin_config
    assert lookup_module.run(['ssh_executable'], plugin_type='connection', plugin_name='ssh') == ['/usr/bin/ssh']

# Generated at 2022-06-13 13:16:31.534290
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._display = type('object', (object,), {'warning': lambda self, msg: None})()
    assert l.run(terms=[], variables={}) == []

# Generated at 2022-06-13 13:16:40.168224
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={}, direct={})

    # Test with on_missing option set to 'error'
    lookup_module.set_options(var_options={}, direct={'on_missing': 'error'})
    try:
        lookup_module.run(terms=['INVALID_CONFIG_KEY'])
    except AnsibleLookupError:
        pass

    # Test with on_missing option set to 'warn'
    lookup_module.set_options(var_options={}, direct={'on_missing': 'warn'})
    try:
        lookup_module.run(terms=['INVALID_CONFIG_KEY'])
    except AnsibleLookupError:
        pass

    # Test with on_missing option set to 'skip' and DEFAULT_

# Generated at 2022-06-13 13:16:49.031967
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    lookup_ret = []
    lookup_ret.append({'_terms': 'DEFAULT_BECOME_USER', '_raw': 'root'})
    lookup_ret.append({'_terms': 'DEFAULT_ROLES_PATH',
                       '_raw': '["/etc/ansible/roles", "/usr/share/ansible/roles"]'})

# Generated at 2022-06-13 13:16:57.118462
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # 1. DEFAULT_BECOME_USER is one of the configuration variable and its value is set to root by default.
    #    In this case, DEFAULT_BECOME_USER should be root.
    module = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    result = module.run(terms,None)
    assert result == ['root']

    # 2. DEFAULT_BECOME_USER is not set in constants.py and its value is 'ansible'.
    #    So if the lookup plugin finds it, the value will be ansible.
    #    This can be achieved by changing configuration variable DEFAULT_BECOME_USER from root to ansible.
    orig_become_user = C.DEFAULT_BECOME_USER
    C.DEFAULT_BECOME_USER = 'ansible'

# Generated at 2022-06-13 13:17:06.053583
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #create an instance of LookupModule
    import ansible
    lookup = LookupModule()

    #Use tests/unit/mock_contexts to temporarily setup context so tests may be run
    import tests
    import tests.unit
    import tests.unit.mock_contexts
    tests.unit.mock_contexts.mock_contexts()

    #setup values for use in test
    terms = ["DEFAULT_BECOME_USER"]
    plugin_type = "become"
    plugin_name = "sudo"
    variables = dict()

    #run test run with no plugin type or name
    result = lookup.run(terms, variables=variables)
    #check that result expected is the same as result from test
    assert(result[0] == "sudo")

    #run test run with plugin type and name
    result

# Generated at 2022-06-13 13:17:15.330466
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # "on_missing" options test
    lookup = LookupModule()
    # on_missing is not a string, raise exception
    assert_exception(AnsibleOptionsError, "Invalid setting identifier", lookup.run, ['test'], variables=None, on_missing=['error'])
    # on_missing is an invalid string, raise exception
    assert_exception(AnsibleOptionsError, '"on_missing" must be a string and one of "error", "warn" or "skip", not invalid', lookup.run, ['test'], variables=None, on_missing='invalid')
    # on_missing is a valid string, return an empty list
    assert lookup.run(['test'], variables=None, on_missing='skip') == []

    # "plugin_type" and "plugin_name" options test
    # "plugin_

# Generated at 2022-06-13 13:17:43.966380
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    # Test with plugin_type, plugin_name and terms
    terms = ('remote_tmp',)
    kwargs = {'plugin_type': 'shell', 'plugin_name': 'sh'}
    ret = lm.run(terms, **kwargs)
    assert ret == [C.DEFAULT_REMOTE_TMP]

    # Test with global config and terms
    terms = ('DEFAULT_REMOTE_TMP',)
    kwargs = {}
    ret = lm.run(terms, **kwargs)
    assert ret == [C.DEFAULT_REMOTE_TMP]

    # Test with plugin_name and terms, but no plugin_type
    terms = ('remote_tmp',)
    kwargs = {'plugin_name': 'sh'}

# Generated at 2022-06-13 13:17:49.100959
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display

    ls = LookupModule(Display())
    ret = ls.run(['DEFAULT_ROLES_PATH'])
    assert ret != []

    ret = ls.run(['DEFAULT_ROLES_PATH', 'DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD'], on_missing='warn')
    assert len(ret) == 3
    ret = ls.run(['DEFAULT_ROLES_PATH', 'DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD', 'DEFAULT_foo'], on_missing='warn')
    assert len(ret) == 3

# Generated at 2022-06-13 13:17:59.834564
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # ansible.utils.color.colorize not defined
    # ret = [u'blue', u'1;36', u'1;36']
    # assert LookupModule(['COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP'], {}, Sentinel, Sentinel, Sentinel, Sentinel, True, on_missing='skip', wantlist=True).run() == ret

    # ansible.utils.color.colorize defined
    ret = ['\x1b[0m', '\x1b[0m']
    assert LookupModule(['COLOR_OK', 'COLOR_CHANGED'], {}, Sentinel, Sentinel, Sentinel, Sentinel, True, on_missing='skip', wantlist=True).run() == ret

    # ansible.utils.color.colorize not defined
    # ret = [u'blue', u'1;

# Generated at 2022-06-13 13:18:08.347381
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.config.manager import ConfigManager, ConfigData

    # init config
    config = ConfigManager()
    config.set_config_data(ConfigData('.', None, None))

    # collect plugin configs
    configs = {}
    for src in config.get_config_sources():
        for plugin_type, plugin_name in C.config.get_all_plugin_names(src):
            configs.setdefault(plugin_type, {})[plugin_name] = {}
            for plugin_config_item in C.config.get_plugin_config_keys(plugin_type, plugin_name):
                configs[plugin_type][plugin_name][plugin_config_item] = C.config.get_config_value(plugin_config_item, plugin_type=plugin_type, plugin_name=plugin_name)



# Generated at 2022-06-13 13:18:13.206014
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = _get_plugin_config('netconf', 'connection', 'remote_user', None)
    assert ret == 'root'

    ret = _get_plugin_config('netconf', 'connection', 'port', None)
    assert ret == 830

    ret = _get_global_config('CONFIG_FILE')
    assert ret == '/etc/ansible/ansible.cfg'

# Generated at 2022-06-13 13:18:20.217691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test for global setting
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'on_missing': 'error'})
    assert lookup_module.run(['DEFAULT_ROLES_PATH']) == [C.DEFAULT_ROLES_PATH]

    # test for plugin setting
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'plugin_name': 'ssh', 'plugin_type': 'connection', 'on_missing': 'error'})
    assert lookup_module.run(['remote_user']) == [C.REMOTE_USER]

    # test plugin setting with unexpected plugin name
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:18:30.478997
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup instance of LookupModule
    lookup = LookupModule()

    # Test Run method
    # Success
    # test_term - list of one string item
    lookup.run([['test_term']], {})
    # test_terms - list of three string items
    lookup.run([['test_term1', 'test_term2', 'test_term3']], {})

    # Failures
    # empty_list
    try:
        lookup.run([[]], {})
        assert False
    except AnsibleOptionsError:
        pass

    # empty_term
    try:
        lookup.run([['']], {})
        assert False
    except AnsibleOptionsError:
        pass

    # non_string_term

# Generated at 2022-06-13 13:18:38.948812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test_term(terms, on_missing=None, plugin_type=None, plugin_name=None, result=None):
        lu = LookupModule()
        variables = {}
        if on_missing:
            variables['on_missing'] = on_missing
        if plugin_type:
            variables['plugin_type'] = plugin_type
        if plugin_name:
            variables['plugin_name'] = plugin_name

        assert result == lu.run(terms, variables)

    # test different types of terms
    test_term(terms=['INVALID_TERM'], result=[])
    test_term(terms=['INVALID_TERM'], on_missing='warn', result=[])
    test_term(terms=['INVALID_TERM'], on_missing='skip', result=[])
    test_

# Generated at 2022-06-13 13:18:48.301640
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create an instance of LookupModule
    lookup = LookupModule()
    
    # _display attribute should be None
    assert lookup._display == None

    # when no terms are given, the run method should return empty list
    terms = []
    ret = lookup.run(terms)
    assert ret == []

    # when no terms are given and on_missing is set to warn, a warning should be displayed
    terms = []
    variables = {}
    kwargs = {'on_missing':'warn'}
    ret = lookup.run(terms, variables, **kwargs)
    assert ret == []

    # when on_missing is set to error, an error should be raised
    terms = []
    variables = {}
    kwargs = {'on_missing':'error'}

# Generated at 2022-06-13 13:18:52.150945
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = 'DEFAULT_BECOME_USER'
    variables = {}
    plugin_type = 'shell'
    plugin_name = 'sh'
    opts = {'plugin_type': plugin_type, 'plugin_name': plugin_name}
    l = LookupModule()
    result = l.run(terms, variables, **opts)
    assert result == [None]

# Generated at 2022-06-13 13:19:21.902546
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run('config')

# Generated at 2022-06-13 13:19:34.650511
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.lookup import LookupModule
    from ansible.plugins.loader import lookup_loader
    from ansible import constants as C

    # Initialize and load LookupModule instance
    lm = LookupModule()
    lm.set_loader(lookup_loader)

    # Load all plugins (to set constants)
    plugin_loader.all(class_only=True)

    # Create terms and variables dicts
    terms = ['INVENTORY_UNPARSED_FAILED', 'FAKE_CONSTANT']
    variables = {'FAKE_CONSTANT': 'FAKE_CONSTANT_VALUE'}

    # Test default on_missing option
    lm.run(terms=terms, variables=variables)
    assert lm.on_missing == 'error'

    # Test on_missing

# Generated at 2022-06-13 13:19:48.406768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ The following test checks the get method for LookupModule class with different inputs """

    # Tests for normal functionality
    _terms = ['lookup_plugin_path', 'lookup_plugins', 'lookup_task_plugins']
    _variables = {'lookup_plugin_path': 'list of paths'}
    _kwargs = {}
    _result = ['list of paths', ['file', 'yaml_file', 'hiera', 'env', 'template', 'redis_kv'], []]

    lookup_module = LookupModule()
    assert lookup_module.run(_terms, variables=_variables, **_kwargs) == _result

    # Tests for common error
    _terms = ['lookup_plugin_path', 'lookup_plugins', 'lookup_task_plugins']

# Generated at 2022-06-13 13:19:59.449388
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """LookupModule - run()"""
    lookup_module = LookupModule()

    with pytest.raises(AnsibleOptionsError):
        terms = {'foo': 'bar'}
        lookup_module.run(terms, variables=None, **{})

    with pytest.raises(AnsibleOptionsError):
        terms = ['foo', 'bar']
        lookup_module.run(terms, variables=None, **{'plugin_type': 'become', 'plugin_name': 'foo'})

    with pytest.raises(AnsibleOptionsError):
        terms = ['foo', 'bar']
        lookup_module.run(terms, variables=None, **{'plugin_type': 'become'})

    with pytest.raises(AnsibleOptionsError):
        terms = ['foo', 'bar']


# Generated at 2022-06-13 13:20:03.001520
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    variables = {'ansible_become_user': 'root', 'ansible_become': 'true'}
    kwargs = {'on_missing': 'skip'}
    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['root']


# Generated at 2022-06-13 13:20:04.738854
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['DEFAULT_BECOME_USER']) == [C.DEFAULT_BECOME_USER]

# Generated at 2022-06-13 13:20:14.932212
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _get_global_config_output = C.DEFAULT_PRIVATE_ROLE_VARS
    _get_plugin_config_output = 'Ansible'

    class mock_plugin_loader:
        class shell_loader:
            @staticmethod
            def get(pname, class_only=True):
                return mock_plugin_loader.ansible_plugin

    class mock_sentinel:
        pass

    class mock_ansible_plugin:
        _load_name = 'Ansible'

    mock_sentinel = mock_sentinel()
    mock_ansible_plugin = mock_ansible_plugin()
    mock_plugin_loader = mock_plugin_loader()
    mock_plugin_loader.shell_plugin = mock_ansible_plugin

    terms = ['DEFAULT_PRIVATE_ROLE_VARS']

# Generated at 2022-06-13 13:20:16.858206
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    expected_results = [u'root']
    results = lookup_module.run(terms=terms)
    assert results == expected_results

# Generated at 2022-06-13 13:20:18.741044
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.run(terms=None, variables=None)

# Generated at 2022-06-13 13:20:26.380405
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=unused-variable
    global C
    C = type('', (), {})
    global plugin_loader
    plugin_loader = type('', (), {})
    global to_native
    def to_native(obj):
        # pylint: disable=unused-argument
        return obj
    global to_text
    to_text = lambda x: x
    global to_bytes
    to_bytes = lambda x: x
    global split_args
    def split_args(txt):
        # pylint: disable=unused-argument
        return txt.split(' ')
    global to_bool
    to_bool = lambda x: bool(x)

    from ansible.parsing.vault import VaultLib as vault
    options = lambda x: None
    options.ask_vault_

# Generated at 2022-06-13 13:21:24.431773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['DEFAULT_VM_TYPE', 'DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']
    result = module.run(terms)
    assert result == ['openstack', 'root', [u'/etc/ansible/roles']]

# Generated at 2022-06-13 13:21:26.854245
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(['DEFAULT_HASH_BEHAVIOUR'])
    assert result == [C.DEFAULT_HASH_BEHAVIOUR]

# Generated at 2022-06-13 13:21:34.359912
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test(terms, result, variables=None, ptype=None, pname=None, on_missing=None):
        lookup_module = LookupModule()
        options = {}
        terms = terms if isinstance(terms, list) else [terms]
        result = result if isinstance(result, list) else [result]
        if ptype:
            options['plugin_type'] = ptype
        if pname:
            options['plugin_name'] = pname
        if on_missing:
            options['on_missing'] = on_missing
        options['var_options'] = variables
        options['direct'] = options
        lookup_module.set_options(options)
        assert lookup_module.run(terms) == result
    # lookup config value from globals

# Generated at 2022-06-13 13:21:42.987342
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Call the function
    options = {'on_missing': 'error', 'plugin_type': 'shell', 'plugin_name': 'sh', '_terms': ['remote_tmp']}
    l = LookupModule()
    l.set_options(options)
    #assert l.run() == os.path.expanduser("~/.ansible/tmp")

# Generated at 2022-06-13 13:21:52.501514
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Case 1: Try to run without valid 'on_missing' option
    # Expected: Raise AnsibleOptionsError
    try:
        lookup.run(terms=['DEFAULT_BECOME_USER'], on_missing='dummy')
        raise Exception('run() should raise AnsibleOptionsError')
    except AnsibleOptionsError:
        pass

    # Case 2: Try to run with invalid 'plugin_type' option
    # Expected: Raise AnsibleOptionsError
    try:
        lookup.run(terms=['DEFAULT_BECOME_USER'], plugin_type='dummy', plugin_name='dummy')
        raise Exception('run() should raise AnsibleOptionsError')
    except AnsibleOptionsError:
        pass

    # Case 3: Try to run without 'plugin_name' option when 'plugin

# Generated at 2022-06-13 13:21:58.846281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms=['DEFAULT_BECOME_USER'], variables={'a': 1}) == [u'sudo'], "The return value is not correct."

    lookup_module_other = LookupModule()
    assert lookup_module_other.run(terms=['UNDEFINED_DEFAULT_BECOME_USER'], variables={'a': 1}) == [], "The return value is not correct."

    lookup_module_other2 = LookupModule()
    assert lookup_module_other2.run(terms=[], variables={'a': 1}) == [], "The return value is not correct."

    lookup_module_other3 = LookupModule()

# Generated at 2022-06-13 13:22:09.182777
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_loader()
    l.set_environment(None, None, None, loader=None, variable_manager=None)
    terms = ['DEFAULT_ROLES_PATH']
    result = l.run(terms=terms)
    assert isinstance(result, list)
    assert result[0] == l._templar._available_variables['DEFAULT_ROLES_PATH']

    terms = ['UNKNOWN_DEFAULT_ROLES_PATH', 'DEFAULT_ROLES_PATH']
    #result = l.run(terms=terms)
    #assert isinstance(result, AnsibleLookupError)

    terms = ['DEFAULT_ROLES_PATH']
    result = l.run(terms=terms, plugin_type='shell', plugin_name='sh')

# Generated at 2022-06-13 13:22:19.954603
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # set globals
    C.DEFAULT_REMOTE_USER = "root"

    # test with missing value
    terms = ("DEFAULT_REMOTE_USER1")
    look = LookupModule()
    assert look.run(terms) == ['root']
    terms = ("DEFAULT_REMOTE_USER1")
    look = LookupModule()
    assert look.run(terms) == ['root']
    terms = ["DEFAULT_REMOTE_USER1"]
    look = LookupModule()
    assert look.run(terms) == ['root']
    terms = ["DEFAULT_REMOTE_USER1", "DEFAULT_REMOTE_USER", "DEFAULT_REMOTE_USER1"]
    look = LookupModule()
    assert look.run(terms) == ['root', 'root', 'root']

# Generated at 2022-06-13 13:22:33.620151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #import pdb;pdb.set_trace()

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_text

    #setup_class(LookupModule,self)
    self = LookupModule()
    self.config = {}

    terms = []
    terms.append('DEFAULT_BECOME_USER')
    terms.append('ANSIBLE_SSH_ARGS')

    variables = {}
    kwargs = {}

    kwargs['on_missing'] = 'error'
    kwargs['plugin_type'] = None
    kwargs['plugin_name'] = None

    #self.set_options(var_options=variables, direct=kwargs)

# Generated at 2022-06-13 13:22:44.479207
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # NOTE: For this test to work, the class LookupModule must be defined
    #       with class Method resolve (lookup_loader.get in this case)
    #       defined with "self" as the first argument

    # invoke the tests
    from ansible.utils.vars import combine_vars
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.lookup import LookupModule
    import ansible.constants as C
    from ansible.errors import AnsibleLookupError, AnsibleOptionsError
    from ansible import context
    from collections import namedtuple

    test_cases = list()

# Generated at 2022-06-13 13:23:47.482367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # args
    terms = []
    variables = {}

    # return
    ret = {"ret":0}

    # _get_plugin_config
    pname = ""
    ptype = ""

    # _get_global_config
    config = ""

    # get_option
    var_options = {}
    direct = {}
    # option
    on_missing = ""

    lm = LookupModule()
    lm.set_options(var_options=variables, direct=direct)
    lm.get_option("on_missing")
    lm.get_option("plugin_type")
    lm.get_option("plugin_name")

    lm.run(terms, variables=variables, **kwargs)

    _get_plugin_config(pname, ptype, config, variables)
    _get

# Generated at 2022-06-13 13:23:55.658584
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._display = DummyDisplay()  # set a display object to avoid warning message if DEBUG is set to True
    lookup_module._templar = DummyTemplar()
    lookup_module._loader = DummyLoader()
    lookup_module.set_options(direct={'on_missing': 'error'})
    original_get_config_value = C.get_config_value

    # use dummy get_config_value
    def dummy_get_config_value(key, plugin_type=None, plugin_name=None, variables=None):
        if key == 'COLOR_OK':
            return 'green'
        elif key == 'COLOR_CHANGED':
            return 'yellow'
        elif key == 'COLOR_SKIP':
            return 'blue'

# Generated at 2022-06-13 13:24:04.067240
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mod = LookupModule()
    ans_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    ansible_config_file_path = ans_dir + os.path.sep + 'ansible.cfg'
    C.load_config_file(ansible_config_file_path)
    terms = ['DEFAULT_ROLES_PATH', 'UNKNOWN']
    result = lookup_mod.run(terms)
    assert result == [C.DEFAULT_ROLES_PATH]
    terms = ['DEFAULT_ROLES_PATH', 'UNKNOWN']
    result = lookup_mod.run(terms, on_missing='warn')
    assert result == []

# Generated at 2022-06-13 13:24:13.551137
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    # "name" of the checkers plugin
    pname = 'checkers'
    # "type" of the plugin
    ptype = 'lookup'
    # config value to search in the checkers plugin
    term = 'paths'
    # set the plugin_name to lookup_plugin
    lookup_plugin.set_options(plugin_name=pname, plugin_type=ptype)
    # test the run function
    result = lookup_plugin.run(terms=[term])
    assert isinstance(result[0], list)
    assert ptype in result[0][0]


# Generated at 2022-06-13 13:24:20.279847
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # test with default option values
    module.run(terms=['DEFAULT_BECOME_USER'])
    module.run(terms=['DEFAULT_BECOME_USER'], variables={'DEFAULT_BECOME_USER':'root'})
    module.run(terms=['DEFAULT_BECOME_USER'], variables={'DEFAULT_BECOME_USER':'root'}, on_missing='skip')
    module.run(terms=['DEFAULT_BECOME_USER'], variables={'DEFAULT_BECOME_USER':'root'}, on_missing='warn')
    module.run(terms=['DEFAULT_BECOME_USER'], variables={'DEFAULT_BECOME_USER':'root'}, on_missing='error')

# Generated at 2022-06-13 13:24:31.869336
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Positive test case for method run
    # test_LookupModule_run_positive()
    terms = ['DEFAULT_BECOME_USER']
    variables = {}
    kwargs = {'plugin_type': 'become', 'plugin_name': 'sudo', 'on_missing': 'error'}
    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['root']

    # Negative test case for method run
    # test_LookupModule_run_negative()
    terms = ['DEFAULT_ROLES_PATH']
    variables = {}
    kwargs = {'plugin_type': 'become', 'plugin_name': 'sudo', 'on_missing': 'error'}

# Generated at 2022-06-13 13:24:40.160344
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Prerequisite
    from ansible.errors import AnsibleLookupError
    import ansible.plugins.loader as plugin_loader
    from ansible.utils.sentinel import Sentinel
    from ansible.utils.display import Display

    def test_display(msg, color=None, stderr=False, screen_only=False, log_only=False, runner=None):
        print (msg)

    display = Display()
    display.display = test_display

    # Test case 1
    terms = ['DEFAULT_BECOME_USER']
    variables = None
    kwargs = {'on_missing':'error'}
    lookup_module = LookupModule(loader=None, templar=None, shared_loader_obj=None)
    lookup_module._display = display

# Generated at 2022-06-13 13:24:44.117315
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create object for class LookupModule
    lookup = LookupModule()
    # pass the test data to the run method
    result = lookup.run(['ANSIBLE_RETRY_FILES_ENABLED'])
    assert 'True' in result

# Generated at 2022-06-13 13:24:52.509720
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(terms=['DEFAULT_BECOME_USER'], variables=None, on_missing='error') == list(C.DEFAULT_BECOME_USER)
    # error if ansible config value is not present
    try:
        lookup.run(terms=['UNKNOWN_CONFIG'], variables=None, on_missing='error')
    except AnsibleLookupError as e:
        assert to_native(e) == 'Unable to find setting UNKNOWN_CONFIG'
    else:
        assert False, 'AnsibleLookupError not raised'
    # skip and warning if ansible config value is not present
    assert lookup.run(terms=['UNKNOWN_CONFIG'], variables=None, on_missing='warn') == []

# Generated at 2022-06-13 13:25:02.538946
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.config import LookupModule, _get_global_config, _get_plugin_config

    from ansible.module_utils.six import string_types
    from ansible.errors import AnsibleLookupError, AnsibleOptionsError

    import ansible.plugins.loader as plugin_loader
    from ansible.constants import DEFAULT_HOST_LIST

    def _get_plugin(ptype, pname):
        # plugin creates settings on load, this is cached so not too expensive to redo
        loader = getattr(plugin_loader, '%s_loader' % ptype)
        return loader.get(pname, class_only=True)


    assert _get_global_config('DEFAULT_VAULT_IDENTITY_LIST') == [C.DEFAULT_VAULT_IDENTITY]
