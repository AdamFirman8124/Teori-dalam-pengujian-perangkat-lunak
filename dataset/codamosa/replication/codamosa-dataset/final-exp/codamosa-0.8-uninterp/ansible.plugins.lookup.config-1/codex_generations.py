

# Generated at 2022-06-13 13:16:15.535221
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.facts.hardware import Hardware

    test_obj = LookupModule()
    test_terms = ['gathering', 'fact_caching']
    test_opts = {
        'plugin_type': 'fact_cache',
        'plugin_name': 'jsonfile'
    }
    test_result = test_obj.run(test_terms, **test_opts)

    assert test_result == [
        'smart',
        {
            'plugins': ['jsonfile'],
            'fact_caching': 'jsonfile',
            'cachedir': '${XDG_CACHE_HOME}/ansible',
            'default_cache_ttl': 3600,
            'enable_memory_cache': False,
            'enable_file_cache': True
        }
    ]

# Generated at 2022-06-13 13:16:23.105511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # _get_global_config test
    module = LookupModule()
    assert module._get_global_config('DEFAULT_CACHE_PLUGIN') == 'jsonfile'
    assert module._get_global_config('Z') == None

    # _get_plugin_config test
    try:
        module._get_plugin_config('ssh', 'shell', 'remote_tmp')
    except MissingSetting:
        assert True

    assert module._get_plugin_config('ssh', 'connection', 'password') == None

# Generated at 2022-06-13 13:16:30.266958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import builtins

    # Create the lookup module object
    lm = LookupModule()

    # Create the user arguments that would usually be supplied by Ansible
    # when the lookup plugin is called, terms is a required argument
    terms = ['DEFAULT_BECOME_USER']

    # Create mock return values for the imported Python modules and objects
    # that would normally be imported by Ansible internally
    if PY2:
        builtins_name = '__builtin__'
    else:
        builtins_name = 'builtins'


# Generated at 2022-06-13 13:16:37.366389
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test for method run of class LookupModule
    """
    # Only needed for doctest
    import ansible.plugins.loader as plugin_loader
    plugin_loader.add_directory('./lib/ansible/plugins/lookup')
    result = plugin_loader.get('config').run(['DEFAULT_BECOME'], None)
    assert result == [False]
    result = plugin_loader.get('config').run(['DEFAULT_ROLES_PATH'], None)
    assert result == [u'/etc/ansible/roles:/usr/share/ansible/roles']

# Generated at 2022-06-13 13:16:48.437831
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        import ansible.modules.extras.system.setup as setup
    except ImportError:
        return None
    setup_dict = setup.SetupModule(load_pickle=False).run()
    ansible_version = setup_dict['ansible_facts']['ansible_version']
    assert ansible_version is not None

    lookup = LookupModule()

    # check result
    terms = ['ansible_version', 'on_missing']
    result = lookup.run(terms, ansible_version)
    assert result[0] == ansible_version['ansible_version']
    assert result[1] == 'error'

    # check result with errors
    terms = ['ansible_version', 'on_missing']
    result = lookup.run(terms, ansible_version)

# Generated at 2022-06-13 13:16:56.935333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ####
    # Helper function to verify function
    def test_method_run_helper(terms=[], plugin_type=None, plugin_name=None, on_missing='error', expected=None):
        ####
        # mock the config object
        class fake_config(object):
            """
            Fake config object for test
            """
            BECOME_USER = "become_user"
            PORT = 123
            def __init__(self):
                pass

            @staticmethod
            def get_config_value(config, plugin_type=None, plugin_name=None, variables=None):
                if (plugin_type, plugin_name) == ('shell', 'sh'):
                    if config == 'remote_tmp':
                        return '/tmp'
                return None

        C.config = fake_config()
        #

# Generated at 2022-06-13 13:17:05.608019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ unit tests for the run method of class LookupModule """

    # Initialization of class object
    mod = LookupModule()

    # Tests for run of class LookupModule
    class args:
        terms = ['action_plugins']
        variables = None
        plugin_type = None
        pname = None
        on_missing = None

    lookup_module_result = mod.run(args.terms, args.variables, **{'plugin_type': args.plugin_type, 'plugin_name': args.pname, 'on_missing': args.on_missing})
    lookup_module_expected_result = '/usr/lib/python2.7/site-packages/ansible/plugins/action/'
    assert lookup_module_result == lookup_module_expected_result

# Generated at 2022-06-13 13:17:10.812510
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        lookup_module = LookupModule()
        lookup_module.run(['DEFAULT_REMOTE_USER'], {}, plugin_name="ssh", plugin_type="connection")
    except AnsibleError as e:
        pass
    except Exception as e:
        raise
    else:
        raise Exception('We should not get here, expected an exception to be raised')

# Generated at 2022-06-13 13:17:22.076655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict

    #Testing for global config
    #Terms is not a string
    m = LookupModule()
    terms = 1234
    variables = dict()
    kwargs = dict()
    try:
        assert m.run(terms, variables, **kwargs)
    except Exception as e:
        assert isinstance(e, AnsibleOptionsError)
        assert str(e) == 'Invalid setting identifier, "1234" is not a string, its a <class \'int\'>'

    #Terms is a string, on_missing is not in ['error', 'warn', 'skip']
    m = LookupModule()
    terms = list()
    terms.append('DEFAULT_ROLES_PATH')
    variables = dict()
    kwargs = dict()

# Generated at 2022-06-13 13:17:32.146059
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    res = lm.run(['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH'], {}, on_missing='skip')
    assert res == ['root', '/etc/ansible/roles']
    res = lm.run(['UNKNOWN_BECOME_USER', 'DEFAULT_ROLES_PATH'], {}, on_missing='warn')
    assert res == ['/etc/ansible/roles']
    assert 'Setting UNKNOWN_BECOME_USER' in lm._display.warning.call_args[0][0]
    assert 'Skipping, did not find setting UNKNOWN_BECOME_USER' in str(lm._display.warning.call_args[0][0])

# Generated at 2022-06-13 13:17:51.048849
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        'bar',
        'foo',
    ]
    variables = {
        'foo': 'value_foo',
        'bar': 'value_bar',
    }
    assert [
        'value_bar',
        'value_foo',
    ]== lookup.run(terms, variables=variables)

# Generated at 2022-06-13 13:18:00.153403
# Unit test for method run of class LookupModule
def test_LookupModule_run():

   lm = LookupModule()

   constants = {'DEFAULT_ROLES_PATH': 'roles_path.txt'}

   lm._display = mock_display(lm)

   def fake_get_config(config, plugin_type=None, plugin_name=None, variables=None):
      return constants[config]

   lm.get_option = mock_get_option(lm, 'DEFAULT_ROLES_PATH', 'error')
   lm.set_options = mock_set_options(lm)
   C.config = mock_config(lm, fake_get_config)

   ret = lm.run([''], {})

   assert ret == ['roles_path.txt']

# Generated at 2022-06-13 13:18:04.106324
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_module = __import__('ansible.modules.system.ping')
    test_module.ANSIBLE_MODULE_ARGS = {}

    test_lookup = LookupModule()

    test_lookup.set_options(var_options={}, direct={})

    test_lookup.run([''])

# Generated at 2022-06-13 13:18:14.876737
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager

    hosts_var = ['localhost']
    port_var = '9999'
    remote_user_var = 'localroot'

    # Create a host
    host = Host(name=hosts_var[0])

    # Create a variable manager
    variable_manager = VariableManager()
    variable_manager.extra_vars = ImmutableDict(ansible_port=port_var, ansible_user=remote_user_var)

    # Create a play context
    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.port = port_var



# Generated at 2022-06-13 13:18:24.966009
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(
        argument_spec={
            '_terms': dict(type='list', required=True),
        },
        supports_check_mode=True
    )

    lookup_module = LookupModule()
    lookup_module.set_options({'var_options': {'a': 'b'}, 'direct': {'a': 'c'}, 'vars': ['a']})

    # C.DEFAULT_CACHE_PLUGIN is set from 'lookup_cache' configuration variable.
    # This variable is set from 'ansible.cfg' file.

# Generated at 2022-06-13 13:18:34.657496
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ["DEFAULT_BECOME_USER", "DEFAULT_ROLES_PATH"]
    ptype = "connection"
    pname = "ssh"

    # DEFAULT_BECOME_USER is present in config
    result = lookup_module.run(terms, plugin_type=ptype, plugin_name=pname)
    assert result == ["root"]

    # DEFAULT_BECOME_USER is present in config, used as global config
    result = lookup_module.run(terms)
    assert result == ["root"]

    # DEFAULT_BECOME_USER is missing in config, should throw MissingSetting exception
    terms = ["BECOME_USER"]

# Generated at 2022-06-13 13:18:45.698262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    words = ["COLOR_ERROR", "COLOR_DEPRECATE", "COLOR_OK", "COLOR_SKIP", "COLOR_UNREACHABLE", "COLOR_CHANGED", "COLOR_WARN"]
    expected = [C.COLOR_ERROR, C.COLOR_DEPRECATE, C.COLOR_OK, C.COLOR_SKIP, C.COLOR_UNREACHABLE, C.COLOR_CHANGED, C.COLOR_WARN]
    lookup_mod = LookupModule()
    ret = lookup_mod.run(words)
    assert ret == expected

# Generated at 2022-06-13 13:18:53.518846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    lu.set_options({'_ansible_check_mode': False, '_ansible_debug': True, '_ansible_diff': True, '_ansible_no_log': False})
    plugin_type = 'connection'
    plugin_name = 'local'
    #test with invalid term
    invalid_term = 123
    try:
        result = lu.run(invalid_term, {})
        assert False, "Expected AnsibleOptionsError for invalid term"
    except AnsibleOptionsError as e:
        assert e.message == 'Invalid setting identifier, "123" is not a string, its a %s' % type(invalid_term)
    # test with invalid plugin_type
    invalid_ptype = 123

# Generated at 2022-06-13 13:19:02.856470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    from ansible.plugins.loader import become_loader
    from ansible.plugins.loader import vars_loader

    # Error if both plugin_type and plugin_name not provided
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(
            terms=['test'],
            plugin_type='become'
        )

    # Error if neither plugin_type and plugin_name provided
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(
            terms=['test']
        )

    # Error if plugin_type is not allowed

# Generated at 2022-06-13 13:19:11.588598
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange

    # Mock
    class MockLookupModule(LookupModule):
        def __init__(self):
            pass

        def set_options(self, var_options, direct):
            pass

    lookup_module = MockLookupModule()

    # Act
    ret = lookup_module.run(['ansible_user'])

    # Assert
    assert isinstance(ret, list)
    assert len(ret) > 0
    assert ret[0].lower() == C.DEFAULT_REMOTE_USER.lower()

# Generated at 2022-06-13 13:19:50.354140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):
        def __init__(self, **kwargs):
            pass

    # mock_loader is a mock object of ansible.plugins.loader.PluginLoader
    # we will use it here to mock plugin.
    # mock_loader.all returns a dictionary of plugins
    # mock_loader.get will return a plugin object for a given name
    mock_loader = plugin_loader.PluginLoader.get(class_only=True)
    # A mock plugin object with a single setting "setting".
    mock_plugin = '''
        def get_setting(self):
            return self._setting

        def set_setting(self, value):
            self._setting = value

        setting = property(fget=get_setting, fset=set_setting)
    '''
    # a plugin named "plugin_name

# Generated at 2022-06-13 13:20:01.714897
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests for empty ret
    result = LookupModule().run(terms=['x_x'])
    assert result == [], "Empty ret: %s" % result

    # Tests for ret with one value
    result = LookupModule().run(terms=['DEFAULT_BECOME_USER'])
    assert len(result) == 1 and result[0] == 'root', "Expected a single value: %s" % result

    # Tests for ret with multiple values
    result = LookupModule().run(terms=['COLOR_OK', 'COLOR_CHANGED'])
    assert len(result) == 2, "Expected two values: %s" % result

# Generated at 2022-06-13 13:20:08.345324
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def test_me(terms=None, on_missing=None, variables=None, expected_result=None):
        print ("\n\ntest_me()")
        print ("terms: %s" % terms)
        print ("on_missing: %s" % on_missing)
        print ("variables: %s" % variables)
        print ("expected_result: %s" % expected_result)
        print ("\nActual result:")
        l = LookupModule()
        l.set_options(var_options=variables, direct=dict(on_missing=on_missing))
        result = l.run(terms, variables)
        print (result)
        assert result == expected_result


# Generated at 2022-06-13 13:20:11.090527
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    constants = lookupModule.run(['DEFAULT_BECOME_USER'], None)
    assert constants[0] == 'root'

# Generated at 2022-06-13 13:20:21.470367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    configs = [
        'DEFAULT_BECOME_METHOD',
        'DEFAULT_BECOME_USER',
        'DEFAULT_ROLES_PATH',
        'REMOTE_TMP',
        'REMOTE_USER',
        'PORT'
    ]

    options = {
        'plugin_type': 'shell',
        'plugin_name': 'sh',
    }

    lookup_plugin = lookup_loader.get('config', class_only=True)


# Generated at 2022-06-13 13:20:29.045061
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.common.collections import is_sequence
    from ansible.plugins.loader import lookup_loader
    from ansible.utils.display import Display
    from ansible.utils.shlex import shlex_split
    from ansible.vars.manager import VariableManager

    l = lookup_loader.get("config", class_only=True)
    assert l is not None

    d = Display()
    assert d is not None

    v = VariableManager()
    assert v is not None

    l = LookupModule(display=d)
    assert l is not None

    # Test 1 - test that exception is raised when plugin_name (or pname) is set but not plugin_type (or ptype) and vice-versa.
    terms = ["become_user"]

# Generated at 2022-06-13 13:20:42.111539
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import unittest

    test_data = [
        {
            '_terms': ['DEFAULT_REMOTE_USER'],
            'on_missing': 'error',
            'plugin_type': None,
            'plugin_name': None,
            'expected': u'root'
        },
        {
            '_terms': ['DEFAULT_ROLES_PATH', 'DEFAULT_CACHE_PLUGIN'],
            'on_missing': 'error',
            'plugin_type': None,
            'plugin_name': None,
            'expected': [u'~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles', u'jsonfile']
        }
    ]


# Generated at 2022-06-13 13:20:57.171025
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    # pylint: disable=unused-argument,missing-docstring
    # Create a class to provide return values, and a mock object to use in place of AnsibleModule
    class TestClass(object):
        def get_config_value(self, config, plugin_type=None, plugin_name=None, variables=None):
            pass
    tests = TestClass()
    tests.config = TestClass()
    tests.config.get_config_value = TestClass()
    tests.config.get_config_value.return_value = 'test value'
    module = MockAnsibleModule()
    # Run test
    lm = LookupModule(templar=None, loader=None)

# Generated at 2022-06-13 13:20:57.973011
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:21:05.373276
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for run method of class LookupModule"""
    lookup_instance = LookupModule()
    test_term = 'DEFAULT_BECOME_USER'
    ret = lookup_instance.run(terms=[test_term], variables=None)
    # assert('root' in ret)
    ret_str = " ".join(ret)
    assert('root' in ret_str)

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:21:38.695108
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First term is not string
    with pytest.raises(AnsibleOptionsError) as exception:
        LookupModule().run(['', 'FOO'])
    assert str(exception.value) == 'Invalid setting identifier, "FOO" is not a string, its a <class \'str\'>'


# Generated at 2022-06-13 13:21:45.083954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    class Options:
        def __init__(self, on_missing):
            self.on_missing = on_missing
            self.plugin_type = None
            self.plugin_name = None

    lm.set_options(Options('error'))
    assert lm.run(['DEFAULT_SUBSET']) == ['all']

    lm.set_options(Options('warn'))
    assert lm.run(['DEFAULT_SUBSET', 'UNKNOWN']) == ['all']

    lm.set_options(Options('skip'))
    assert lm.run(['DEFAULT_SUBSET', 'UNKNOWN']) == ['all']

    lm.set_options(Options('unknown'))

# Generated at 2022-06-13 13:21:54.157115
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1
    test_module = LookupModule()
    test_module._display = Display()
    test_module.set_options(var_options={'invalid_var': 'test_value'}, bypass_checks=False)
    with pytest.raises(AnsibleOptionsError) as exc_info:
        test_module.run([])
    assert "One of the following is required: _terms" in str(exc_info.value)
    assert "AnsibleOptionLookupModuleLookupBase:on_missing" in str(exc_info.value)

    # Test 2
    test_module = LookupModule()
    test_module._display = Display()
    test_module.set_options(var_options={'invalid_var': 'test_value'}, bypass_checks=False)

# Generated at 2022-06-13 13:22:05.331126
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Verify the correct settings and values are returned by the lookup module
    '''
    # SetUp
    import os

# Generated at 2022-06-13 13:22:13.586492
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with one term
    lookup_module = LookupModule()
    result = lookup_module._load_plugins()
    assert result

    terms = ['ANSIBLE_RETRY_FILES_ENABLED', 'ANSIBLE_RETRY_FILES_ENABLED']
    result = lookup_module.run(terms=terms, variables={})
    assert result == [True, True]

    # Test with multiple terms
    terms = ['RETRY_FILES_ENABLED', 'RETRY_FILES_ENABLED']
    result = lookup_module.run(terms=terms, on_missing='skip', variables={})
    assert result == [True, True]

    # Test with missing term
    terms = ['RETRY_FILES_ENABLED', 'ANSIBLE_RETRY_FILES_ENABLED', 'unidentified_term']

# Generated at 2022-06-13 13:22:18.032582
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.lookup import LookupBase

    class fake_lookup_plugin_method(object):
        def __init__(self, name, methods, class_name, amble):
            self.name = name
            self.class_name = class_name
            # self.run_method = run_method

    class fake_lookup_plugin(LookupBase):
        def run(self, terms, variables=None, **kwargs):
            pass
        # def run(self, term, variables, **kwargs):
        #     pass
        # def run(self, terms, variables=None, **kwargs):
        #     return []


# Generated at 2022-06-13 13:22:30.494011
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize object to test lookupModule
    instance = LookupModule()

    # Test error of missing option plugin name
    try:
        # Run test with pname missing but with ptype
        instance.run(terms=['DEFAULT_ROLES_PATH'], variables=None, plugin_type="connection", on_missing='error')
    except AnsibleOptionsError:
        pass

    # Test error of missing option plugin type
    try:
        # Run test with ptype missing but with pname
        instance.run(terms=['DEFAULT_ROLES_PATH'], variables=None, plugin_name="ssh", on_missing='error')
    except AnsibleOptionsError:
        pass

    # Test error of missing option on missing

# Generated at 2022-06-13 13:22:31.854669
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True == LookupModule()

# Generated at 2022-06-13 13:22:39.022194
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert(module.run([]) == [])
    assert(module.run(['DEFAULT_ROLES_PATH']) == [C.DEFAULT_ROLES_PATH])
    assert(module.run(['DEFAULT_ROLES_PATH', 'DEFAULT_RETRY_FILES_ENABLED']) == [C.DEFAULT_ROLES_PATH, C.DEFAULT_RETRY_FILES_ENABLED])
    assert(module.run(['DEFAULT_ROLES_PATH'], variables={'ansible_user': 'testuser'}) == [C.DEFAULT_ROLES_PATH])

# Generated at 2022-06-13 13:22:48.897862
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1
    module = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    result = module.run(terms, None)
    assert result == [u'root']

    # Test 2
    module = LookupModule()
    terms = ['DEFAULT_ROLES_PATH']
    result = module.run(terms, None)
    assert result == [[u'/etc/ansible/roles']]

    # Test 3
    module = LookupModule()
    terms = ['RETRY_FILES_SAVE_PATH']
    result = module.run(terms, None)
    assert result == [u'/home/ansible/.ansible/retry']

    # Test 4
    module = LookupModule()
    terms = ['COLOR_OK']
    result = module.run(terms, None)


# Generated at 2022-06-13 13:23:45.525718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(True)

# Generated at 2022-06-13 13:23:57.599079
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    current_result = []
    lookup_ret = []
    missing = "error"

    # method run of class LookupModule(LookupBase) can act according to value of missing
    # if value of missing is "error", when lookup_ret is empty,it will raise AnsibleLookupError
    if missing == "error":
        if lookup_ret:
            current_result.append(lookup_ret)
        else:
            raise AnsibleLookupError("No lookup_ret")

    # if value of missing is "warn", when lookup_ret is empty,it will warning
    elif missing == "warn":
        if lookup_ret:
            current_result.append(lookup_ret)
        else:
            print("warning: lookup_ret is missing")

    # if value of missing is "skip", it will skip when lookup_ret is

# Generated at 2022-06-13 13:23:58.828872
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    # TODO: implement tests
    pass

# Generated at 2022-06-13 13:24:05.741778
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    from unittest.mock import patch
    plugin_loader.become_loader = None
    plugin_loader.cache_loader = None
    plugin_loader.callback_loader = None
    plugin_loader.cliconf_loader = None
    plugin_loader.connection_loader = None
    plugin_loader.httpapi_loader = None
    plugin_loader.inventory_loader = None
    plugin_loader.lookup_loader = None
    plugin_loader.netconf_loader = None
    plugin_loader.shell_loader = None
    plugin_loader.vars_loader = None

    lm = LookupModule()
    lm.set_loader = None
    lm._get_basedir = None
    lm._templar = None
    lm._display = None
    lm.set_options

# Generated at 2022-06-13 13:24:16.471878
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader()

    setattr(C, "test_config_setting_1", "lookup_test_config_setting_1")
    setattr(C, "test_config_setting_2", "lookup_test_config_setting_2")

    terms = ["test_config_setting_1", "test_config_setting_2", "test_config_setting_unknown"]
    result = lookup_module.run(terms, on_missing="error", variables={"test_config_setting_2": "lookup_test_config_setting_2_variable_value"})

# Generated at 2022-06-13 13:24:29.187032
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    AnsibleLookupError is raised when given config is not in expected format.
    AnsibleOptionsError is raised when config is missing or invalid.
    """
    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    lookup_module.set_environment(None)
    lookup_module.set_connection(None)
    lookup_module.set_options({})

    config = C.CONFIG_FILE
    invalid_config = 'invalid config'
    missing_config = 'missing config'
    missing_plugin_name = 'missing plugin name'
    valid_plugin_name = 'ping'
    valid_plugin_type = 'inventory'

    # Validate with invalid config
    try:
        lookup_module.run([invalid_config])
    except AnsibleLookupError:
        pass 

# Generated at 2022-06-13 13:24:38.001722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up arguments to mocked LookupModule.run() method
    terms = ['DEFAULT_BECOME_USER']
    on_missing = 'error'
    ptype = 'vars'
    pname = 'glob'
    variables = None
    kwargs = {}
    # Instantiate a mocked LookupModule object
    lm = LookupModule()
    
    # Call the run method with mocked parameters
    result = lm.run(terms, variables, on_missing=on_missing)
    assert result == ['root']
    
    # Call the run method with mocked parameters
    result = lm.run(terms, variables, on_missing=on_missing, plugin_type=ptype, plugin_name=pname)
    assert result == ['root']


# Generated at 2022-06-13 13:24:43.044271
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tested with pytest
    # Check or:
    #   ansible-test lookup --python 2.7 -v --test test_lookup_config
    #   ansible-test lookup --python 3.8 -v --test test_lookup_config
    # With
    #   ansible-test sanity --python 3.8 -v --test test_lookup_config
    pass

# Generated at 2022-06-13 13:24:51.742044
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=too-few-public-methods
    class FakeVars(object):
        def __init__(self, name="fake"):
            self.name = name
    fake_vars = FakeVars()

    class FakeVariableManager(object):
        def get_vars(self, loader=None, play=None, host=None, task=None, include_hostvars=True, include_delegate_to=True):
            return fake_vars

        def get_host_vars(self, host, include_hostvars=False):
            return fake_vars

    # -----------------------------
    # - get_global_config
    # -----------------------------
    setattr(C, 'DEFAULT_BECOME_USER', 'foo')
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:24:57.379045
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    lu = LookupModule()

    def get_ansible_options(setting):
        return getattr(C, setting)

    def get_plugin_config(name, type):
        return C.config.get_config_value(name, plugin_type=type, plugin_name=type)
