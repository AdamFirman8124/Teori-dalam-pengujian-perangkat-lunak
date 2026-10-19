

# Generated at 2022-06-13 13:16:05.414305
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH', 'RETRY_FILES_SAVE_PATH', 'COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP']
    variables = {'config_in_var': 'UNKNOWN'}
    on_missing = 'skip'
    kwargs = {'plugin_type': 'shell',
              'plugin_name': 'sh'}

    assert module.run(terms, variables, **kwargs), 'Ansible configuration variables were not found!'

# Generated at 2022-06-13 13:16:16.847011
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # test case: _get_global_config: DEFAULT_UNDERSCORE_TEMPLATE_INTERPRETER
    terms = ['DEFAULT_UNDERSCORE_TEMPLATE_INTERPRETER']
    kwargs = {'on_missing': 'error'}
    ret = module.run(terms, **kwargs)
    assert ret == 'jinja2'

    # test case: _get_plugin_config: connection plugin 'ssh'
    terms = ['remote_user', 'port']
    kwargs = {'on_missing': 'error', 'plugin_type': 'connection', 'plugin_name': 'ssh'}
    ret = module.run(terms, **kwargs)
    assert ret == ['ansible_user', 22]

    # test case: _get_plugin

# Generated at 2022-06-13 13:16:26.261755
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(terms=['DEFAULT_HASH_BEHAVIOUR']) == ['merge']
    assert lookup.run(terms=['DEFAULT_HASH_BEHAVIOUR', 'DEFAULT_ROLES_PATH']) == ['merge', '~/.ansible/roles:/usr/share/ansible/roles']
    # test default option
    assert lookup.run(terms=['DEFAULT_BECOME_ASK']) == [True]
    assert lookup.run(terms=['DEFAULT_BECOME_ASK'], variables={'DEFAULT_BECOME_ASK': 'None'}) == [None]
    # test on_missing option
    assert lookup.run(terms=['UNKNOWN']) == []
    # test on_missing option
    assert lookup

# Generated at 2022-06-13 13:16:36.631528
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule

    # Test to see if missing is a string and one of 'error', 'warn' or 'skip'
    setattr(C, 'DEFAULT_BECOME_USER', 'test')
    terms = ['DEFAULT_BECOME_USER', 'UNKNOWN_CONFIG_NAME']
    terms_bad = ['DEFAULT_BECOME_USER', 'UNKNOWN_CONFIG_NAME', 123]
    kwargs = {'on_missing': 'error'}

    ret = module.run(terms, **kwargs)
    assert ret == ['test']

    kwargs = {'on_missing': 'warn'}
    ret = module.run(terms, **kwargs)
    assert ret == ['test']

    kwargs = {'on_missing': 'error'}
    ret = module.run

# Generated at 2022-06-13 13:16:39.155167
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_result = ['expected']
    expected_run_result = lookup_result

    lookup = LookupModule()
    run_result = lookup.run(lookup_result)
    assert run_result == expected_run_result

# Generated at 2022-06-13 13:16:49.940108
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['DEFAULT_HOST_LIST']
    kwargs = {'plugin_type': 'become', 'plugin_name': 'become', 'on_missing': 'error'}
    result = lookup.run(terms, **kwargs)
    assert result == ['/etc/ansible/hosts']

    kwargs = {'plugin_type': 'become', 'plugin_name': 'become', 'on_missing': 'warn'}
    result = lookup.run(terms, **kwargs)
    assert result == ['/etc/ansible/hosts']

    kwargs = {'plugin_type': 'become', 'plugin_name': 'become', 'on_missing': 'skip'}
    result = lookup.run(terms, **kwargs)

# Generated at 2022-06-13 13:16:57.389746
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    result = lookup_module.run()
    assert result == [], 'The result is incorrect'

    result = lookup_module.run(['foobar'])
    assert result == [], 'The result is incorrect'

    result = lookup_module.run(['foobar'], on_missing='error')
    assert result == [], 'The result is incorrect'

    result = lookup_module.run(['foobar'], on_missing='error')
    assert result == [], 'The result is incorrect'

    result = lookup_module.run(['system_facts_cache'])
    assert result == ['False'], 'The result is incorrect'

    result = lookup_module.run(['system_facts_cache'], on_missing='error')

# Generated at 2022-06-13 13:17:05.943313
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Assume that Ansible can find the plugins
    # Assume that we have plugins to check
    # Create a plugin manager to get the lookups
    pm = plugin_loader.LookupModule()
    tmp = pm._load_plugins()
    for key in tmp:
        lookuptype = key.split(".")[-1]
        if not hasattr(LookupModule, 'run'):
            print("Unit test for method \"run\" in class \"%s\" is missing. Please add it." % lookuptype)
            continue
        print("Unit test for method \"run\" in class \"%s\" found. Running it." % lookuptype)
        tmp[key].run(None, None)
    print("Unit test for method \"run\" in class \"LookupModule\" completed.")

# Generated at 2022-06-13 13:17:10.326664
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_native
    lookup = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    want = "root"
    got = lookup.run(terms, variables = None, **{})
    assert want == got[0]



# Generated at 2022-06-13 13:17:18.138843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(['foo']) == []
    assert lookup_module.run(['foo'], on_missing='warn') == []
    assert lookup_module.run(['foo'], on_missing='skip') == []
    assert lookup_module.run(['DEFAULT_SUDO_USER'])[0] == 'root'
    assert lookup_module.run(['DEFAULT_SUDO_USER', 'DEFAULT_BECOME_USER'])[0] == 'root'

# Generated at 2022-06-13 13:17:38.780560
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup_class = lookup_loader.get('config', class_only=True)
    lc = lookup_class()
    assert lc is not None

# Generated at 2022-06-13 13:17:45.991026
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First test with 3 terms and default options

    terms = ["FOO", "FOO_BAZ", "UNKNOWN"]
    variables = {}
    options = {}
    options['_ansible_verbosity'] = 0

    # Create instance of LookupModule class
    lkup = LookupModule()
    # Create mock object of class display
    lkup._display = MockDisplay()

    # Create mock object of class sentinel
    lkup.Sentinel = Sentinel

    # Create mock object of class constants
    lkup.C = MockConstants()

    # Create mock object of class config
    lkup.C.config = MockConfig()

    # Call the method run of class LookupModule and pass the arguments
    # terms, variables and options to it
    result = lkup.run(terms, variables, **options)



# Generated at 2022-06-13 13:17:49.530493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(terms=['DEFAULT_ROLES_PATH']) == ['/usr/share/ansible/roles:/etc/ansible/roles:/opt/ansible-role-collection/roles']



# Generated at 2022-06-13 13:17:55.077110
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    #def run(self, terms, variables=None, **kwargs):
    #missing = self.get_option('on_missing')
    #ptype = self.get_option('plugin_type')
    #pname = self.get_option('plugin_name')
    # test_valid_ptype_pname
    terms = 'test_string'
    variables = dict()
    kwargs = dict()
    kwargs['plugin_type'] = 'test_type'
    kwargs['plugin_name'] = 'test_name'
    lookup_module.run(terms, variables, **kwargs)
    # test_invalid_ptype_pname
    kwargs['plugin_type'] = 'test_type'
    del kwargs['plugin_name']
   

# Generated at 2022-06-13 13:17:59.412186
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #initializing the class with reference to the module
    module = LookupModule(None)

    #testing for error
    try:
        # testing for error when list is passed
        module.run([1,2,3,4], {}, on_missing='error')
    except AnsibleOptionsError as e:
        assert ("Invalid setting identifier, \"1\" is not a string, its a " in to_native(e))

    #testing for error
    try:
        # testing for error when on_missing is not one of 'error', 'warn' or 'skip'
        module.run(["term"], {}, on_missing='errors')
    except AnsibleOptionsError as e:
        assert ("must be a string and one of \"error\", \"warn\" or \"skip\", not errors" in to_native(e))

    #testing for error
   

# Generated at 2022-06-13 13:18:07.986740
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager

    expected_res = [u'vaultpassword', AnsibleVaultEncryptedUnicode(u'vaultsecret'), AnsibleVaultEncryptedUnicode(u'vaultoldsecret')]
    expected_res1 = [u'vaultpassword', AnsibleVaultEncryptedUnicode(u'vaultsecret')]
    expected_res2 = [u'vaultsecret']
    expected_res3 = [u'vaultoldsecret']
    expected_res4 = [u'vaultpassword', AnsibleVaultEncryptedUnicode(u'vaultoldsecret')]

# Generated at 2022-06-13 13:18:16.976587
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader

    test_data_loader = DataLoader()
    test_play_context = PlayContext()
    test_play_context.remote_user = 'remote_user'
    test_play_context.connection = 'ssh'

    lm = LookupModule()
    lm.set_loader(test_data_loader)
    lm.set_context(test_play_context)

    # testing with `remote_user` defined as `remote_user`
    lm_fixture = [to_bytes(u'remote_user')]
    result = lm.run(lm_fixture)

# Generated at 2022-06-13 13:18:23.520836
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['remote_user', 'port']
    variables = {'port': '22'}
    plugin_type = 'connection'
    plugin_name = 'ssh'
    on_missing = 'skip'

    l = LookupModule()
    assert l.run(terms, variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing) == ['root', '22']

# Generated at 2022-06-13 13:18:33.372907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    terms = ['DEFAULT_BECOME_USER']
    variables = None
    l = LookupModule()
    l.set_options(var_options=variables, direct=dict())
    assert l.run(terms, variables) == ['root']
    del l

    assert len(l.run(['DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD'], variables=None)) == 2
    with pytest.raises(AnsibleOptionsError):
        l.run(['DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD'], variables, on_missing='error')

    with pytest.raises(AnsibleOptionsError):
        l.run(terms, variables, on_missing='invalid_option')


# Generated at 2022-06-13 13:18:40.792754
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

    # Unit test case:
    # Test if LookupModule is called with on_missing set to 'error'.
    # In this case, a MissingSetting error is raised.
    with pytest.raises(AnsibleLookupError):
        lookup_instance.run(terms=['DEFAULT_NEW_SETTING'], variables=None, on_missing='error')

    # Unit test case:
    # Test if LookupModule is called with on_missing set to 'warn'.
    # In this case, the function will print a warning and not return any value.
    assert not lookup_instance.run(terms=['DEFAULT_NEW_SETTING'], variables=None, on_missing='warn')

    # Unit test case:
    # Test if LookupModule is called with on_missing set to 'skip'.


# Generated at 2022-06-13 13:19:17.968684
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import cache_loader
    from ansible.plugins.loader import lookup_loader

    # *** Create lookup module instance
    lookup_plugin = LookupModule()

    # *** Create variables for lookup plugin
    myvars = {
        'myvar1' : 'test1',
        'myvar2' : 'test2'
    }

    # ***
    # *** Test plugin_name option
    # ***
    # *** set plugin_type option
    # ***
    lookup_plugin.set_options(plugin_type='cache')

    # *** Cache dir should be '/tmp/.ansible_cache'
    lookup_plugin.set_options(plugin_name='memory')
    # *** Cache dir should be '/tmp/.ansible_cache'

# Generated at 2022-06-13 13:19:24.831151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

    def getattr(attr):
        if attr == 'DEFAULT_BECOME_USER':
            return 'root'
        elif attr == 'DEFAULT_ROLES_PATH':
            return '/etc/ansible/roles'
        elif attr == 'RETRY_FILES_SAVE_PATH':
            return '/var/tmp/ansible-retry'

    class C(object):
        getattr = getattr

    lookup_instance.set_loader()
    lookup_instance.set_environment({'C': C})

    assert lookup_instance.run(['DEFAULT_BECOME_USER']) == ['root']

    result = lookup_instance.run(['DEFAULT_ROLES_PATH'])

# Generated at 2022-06-13 13:19:36.348508
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    test_terms = ['foo','bar','baz']
    test_dict = {'foo': 'not_called', 'bar': 'called', 'baz': 'not_called'}
    test_result = [test_dict['foo'], test_dict['bar']]
    test_result.append("plugin_name is mandatory")
    test_result.append("Both plugin_type and plugin_name are required, cannot use one without the other")
    test_dict_invalid_on_missing = {'error': 'Unable to find setting foo',
                                    'warn': 'Skipping, did not find setting foo',
                                    'skip': ''}

# Generated at 2022-06-13 13:19:50.006577
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # test when term is not string
    try:
        lookup_module.run(["abc", 1])
    except AnsibleOptionsError as e:
        pass

    # test when on_missing is invalid
    try:
        lookup_module.run(["abc"], {'on_missing': 'abc'})
    except AnsibleOptionsError as e:
        pass

    # test when plugin name is missing
    try:
        lookup_module.run(["abc"], {"plugin_type": "shell"})
    except AnsibleOptionsError as e:
        pass

    # test when plugin type is missing
    try:
        lookup_module.run(["abc"], {"plugin_name": "sh"})
    except AnsibleOptionsError as e:
        pass

    # test when variable option is invalid
   

# Generated at 2022-06-13 13:20:01.538821
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Normal test cases
    lm = LookupModule()
    lm.set_options([])
    result = lm.run(['DEFAULT_BECOME_USER'], [], on_missing='warn', plugin_type='become', plugin_name='sudo')

    assert(isinstance(result, list))
    assert('root' in result)

    # Negative test cases
    lm = LookupModule()
    lm.set_options([])

    # Failure case 1: on_missing has invalid value
    try:
        result = lm.run(['DEFAULT_BECOME_USER'], [], on_missing='invalid', plugin_type='become', plugin_name='sudo')
    except AnsibleOptionsError:
        pass

# Generated at 2022-06-13 13:20:08.149083
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader
    from ansible import constants as C
    from ansible.errors import AnsibleError, AnsibleLookupError, AnsibleOptionsError
    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.sentinel import Sentinel

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.lookup import config

    lookup_module = config.LookupModule()


# Generated at 2022-06-13 13:20:16.689449
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # no plugin
    assert lookup.run(["DEFAULT_ROLES_PATH"], variables={"ansible_connection": "local"}) == [C.DEFAULT_ROLES_PATH]
    assert lookup.run(["UNKNOWN"], variables={"ansible_connection": "local"}, on_missing="skip") == []
    # plugin_type and plugin_name
    assert lookup.run(["remote_user"], variables={"ansible_connection": "local"}, plugin_type="connection",
                      plugin_name="ssh") == [C.DEFAULT_REMOTE_USER]

# Generated at 2022-06-13 13:20:25.083459
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Test with a valid configuration
    result = lookup.run([C.DEFAULT_STDOUT_CALLBACK], variables={})
    assert result[0] == [C.DEFAULT_STDOUT_CALLBACK]
    # Test with on_missing set to 'skip'
    result = lookup.run(['UNKNOWN_CONFIG'], variables= {}, on_missing='skip')
    assert result[0] == []
    # Test with on_missing set to 'warn'
    result = lookup.run(['UNKNOWN_CONFIG'], variables= {}, on_missing='warn')
    assert result[0] == []
    # Test with on_missing set to 'error'

# Generated at 2022-06-13 13:20:38.086796
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with two terms
    lookup_module = LookupModule()
    result_global =  lookup_module.run(["DEFAULT_ROLES_PATH", "DEFAULT_ROLES_PATH"], {})
    result_plugin = lookup_module.run(["remote_tmp", "remote_user"], {"plugin_type" : "shell", "plugin_name" : "sh"},)
    assert result_global == [C.DEFAULT_ROLES_PATH, C.DEFAULT_ROLES_PATH]
    assert result_plugin == ['~/.ansible/tmp', 'default']
    # Test with one terms
    result_global =  lookup_module.run(["DEFAULT_ROLES_PATH"], {})

# Generated at 2022-06-13 13:20:40.821819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(None, None, None).run(["localhost"]) == []


# Generated at 2022-06-13 13:21:40.536612
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First run test
    print("Test run() method of class LookupModule")
    # Initialize constructor
    lookup_1 = LookupModule()
    # Try to run lookup_base with following parameters
    # No parameter
    lookup_1.run()
    # 2 parameters - self and terms
    lookup_1.run(['_ansible_version'])
    # 3 parameters - self, terms and variables
    lookup_1.run(['_ansible_version'], variables=None)
    # 5 parameters - self, terms, variables and keyword parameters
    lookup_1.run(['_ansible_version'], variables=None, plugin_name="sh")

    # Second run test
    print("Test run() method of class LookupModule when raise MissingSetting")
    lookup_2 = LookupModule()
    # Try to run lookup_base

# Generated at 2022-06-13 13:21:50.997785
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests for global configs
    assert LookupModule().run([
            # A global config which exists
            'DEFAULT_CACHE_PLUGIN',
            # A global config which does not exist
            'TEST_DOES_NOT_EXIST',
            # A global config for a setting that is a callable
            'DEFAULT_CACHE_PLUGIN',
        ]
    ) == [
            dict(type='memory', config=dict(), dir_mode=None, file_mode=None),
            [],
            dict(type='memory', config=dict(), dir_mode=None, file_mode=None),
    ]


# Generated at 2022-06-13 13:21:57.668256
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

    def _get_global_config(config):
        return 123

    def _get_plugin_config(pname, ptype, config, variables):
        return config

    lookup_instance._get_global_config = _get_global_config
    lookup_instance._get_plugin_config = _get_plugin_config

    lookup_instance._display = None

    # tests for no config provided
    try:
        lookup_instance.run(terms=None, variables=None, **{})
        assert False
    except AnsibleOptionsError:
        pass

    # tests for valid global config
    assert lookup_instance.run(terms=["UNKNOWN"], variables=None, **{}) == [123]

    # tests for valid global config with callback

# Generated at 2022-06-13 13:22:08.270358
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.sentinel import Sentinel
    import pytest

    # To test this method, first set the value of 'C.DEFAULT_CONNECTION_ATTEMPTS' in ansible.cfg
    # to some integer value.
    test_terms = ['DEFAULT_CONNECTION_ATTEMPTS']
    test_missing = 'error'
    test_plugin_type = ''
    test_plugin_name = ''
    test_variables = None

    result = LookupModule.run(test_terms, test_variables, test_missing, test_plugin_type, test_plugin_name)
    assert result == C.DEFAULT_CONNECTION_ATTEMPTS, 'lookup.config lookup failed'

    # To test the plugin type and plugin name, set the value of 'default_remote_user' to some
    # user

# Generated at 2022-06-13 13:22:16.561624
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = dict(ANSIBLE_VAR_A=10, ANSIBLE_VAR_B=20)
    terms = dict(remote_user='admin', format='yaml', ssh=True, ansible_ssh_user='admin', ansible_ssh_pass='admin')

    lm = LookupModule()

    for term in terms:
        lm.set_options(var_options=variables, direct=dict(on_missing='skip'))
        actual = lm.run([term], variables=variables)
        assert actual == [terms[term]]

# Generated at 2022-06-13 13:22:23.976252
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from six import assertRegex
    from ansible.module_utils._text import to_bytes
    from ansible.plugin.manager import lookup_loader

    y = lookup_loader.get('config', class_only=True)
    x = y()

    def _test_lookup_error(terms, parameters, expected_regex):
        #calls the method run of class LookupModule
        try:
            x._templar.available_variables = {'x': 24}
            x.run(terms,
            plugin_type=parameters.get('plugin_type'),
            plugin_name=parameters.get('plugin_name'),
            on_missing=parameters.get('on_missing'))
        except AnsibleLookupError as e:
            assertRegex(e.message, expected_regex)

# Generated at 2022-06-13 13:22:28.261531
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([]) is None
    assert LookupModule().run(None) is None
    assert LookupModule().run(list()) is None
    assert LookupModule().run("") is None

# Generated at 2022-06-13 13:22:38.617651
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import unittest
    import ansible.utils

    class TestLookupModule(unittest.TestCase):
        def setUp(self):
            self.lookup = LookupModule()
            self.lookup.set_loader(ansible.utils.plugins._PluginsLoader({'lookup': os.path.join(os.path.dirname(__file__), '../../lookup_plugins')}))
            self.lookup.set_options(var_options={'ansible_connection': 'local'})

        def test_run_1(self):
            self.assertEqual(self.lookup.run(['ANSIBLE_CALLBACK_WHITELIST']), ['default'])


# Generated at 2022-06-13 13:22:48.609687
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:22:53.339576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Provide the set of parameters to run method of class LookupModule
    terms = ['DEFAULT_BECOME_USER']
    variables = {}
    kwargs = dict(on_missing='error', plugin_type='connection', plugin_name='ssh')

    # Provide expected results
    expected = ['root']

    # Get result from run method
    result = LookupModule().run(terms, variables, **kwargs)

    # Check if results are matching
    assert result == expected

# Generated at 2022-06-13 13:24:50.391148
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.context import CLIContext
    from ansible.plugins.loader import connection_loader
    lu = LookupModule()
    global_config = ('DEFAULT_ANSIBLE_NET_TRANSPORT',
                     'DEFAULT_ANSIBLE_NET_USERNAME',
                     'DEFAULT_ANSIBLE_NET_PASSWORD',
                     'DEFAULT_ANSIBLE_NET_SSH_KEYFILE',
                     'DEFAULT_ANSIBLE_NET_AUTH_PASS',
                     'DEFAULT_ANSIBLE_NET_TIMEOUT',
                     'DEFAULT_ANSIBLE_NET_SSH_ARGS',
                     'DEFAULT_ANSIBLE_NET_SSH_CUSTOM_ARGS',)

# Generated at 2022-06-13 13:24:56.164386
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.action as action_plugin
    from ansible.plugins.action import ActionModule
    from ansible.utils.sentinel import Sentinel
    from ansible.errors import AnsibleLookupError, AnsibleOptionsError

    loader = plugin_loader.action_loader

    # test plugin config
    assert _get_plugin_config('ping', 'action', 'ping_timeout', None) == 5
    assert _get_plugin_config('foo', 'action', 'ping_timeout', None) == Sentinel
    assert _get_plugin_config('ping', 'action_foo', 'ping_timeout', None) == Sentinel

    # test global config
    assert _get_global_config('DEFAULT_BECOME_USER') == 'root'

# Generated at 2022-06-13 13:25:06.967140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test run method of class LookupModule"""

    import sys
    import os
    import pytest

    try:
        os.symlink("../ansible/plugins/lookup", os.path.join(os.path.dirname(__file__), "lookup"))
    except OSError:
        pass

    sys.path.insert(0, os.path.dirname(__file__))

    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('config')

    #
    # Success scenario tests
    #
    assert lookup.run(["DEFAULT_MODULE_NAME"], None, on_missing="error") == [b"command"]

    #
    # Failure scenario tests
    #

# Generated at 2022-06-13 13:25:14.421188
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Get a object of the LookupModule class
    lookup_module = LookupModule()

    # Set the data structure of the 'terms' variable
    # Required argument for the run method
    terms = ["DEFAULT_ROLES_PATH"]

    # Set the data structure of the 'variables' variable
    # Optional argument for the run method
    variables = {}

    # Set the data structure of the 'kwargs' variable
    # Optional argument for the run method
    kwargs = {"on_missing": "error"}

    # Invoke the run method of the LookupModule class with the required arguments
    lookup_module.run(terms, variables, **kwargs)

# Generated at 2022-06-13 13:25:24.946865
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # this will just test the run method, code coverage included to show that it works
    # if you want to see the coverage, run "setup.py test --coverage" and check out the htmlcov file
    l = LookupModule()

    # set up these values that are normally read in from the playbook
    terms = ["color", "unset"]
    kwargs = {"plugin_type": "task", "plugin_name": "debug", "on_missing": "skip"}
    l.set_options(None, kwargs)

    # run the code for the lookup method
    result = l.run(terms)
    assert result[0] == 'blue', "color was expected to be blue"

# Generated at 2022-06-13 13:25:32.045078
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  lookup = LookupModule()
  try:
    # 1) LookupModule.run must return list
    assert isinstance(lookup.run([]), list)
    assert isinstance(lookup.run([], plugin_name='yum'), list)
    assert isinstance(lookup.run([], plugin_type='inventory'), list)
    assert isinstance(lookup.run([], plugin_name='yum', plugin_type='inventory'), list)
    # 2) check when invalid setting identifier are used
    try:
      lookup.run([1])
    except AnsibleOptionsError:
      pass
  except Exception as e:
    # 3) check when invalid setting identifier are used
    assert str(e) == 'Invalid setting identifier, "1" is not a string, its a <class \'int\'>'

# Generated at 2022-06-13 13:25:41.511730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # https://github.com/ansible/ansible/issues/52726
    plugin = LookupModule()

    # Invalid setting identifier
    term = 1
    variables = None
    exc = AnsibleOptionsError
    try:
        plugin.run(terms=term, variables=variables)
    except exc as e:
        assert str(e) == 'Invalid setting identifier, "1" is not a string, its a <class \'int\'>'
    else:
        raise AssertionError('AnsibleOptionsError not raised')

    # Plugin name is required
    term = 'remote_user'
    plugin_type = 'connection'
    plugin_name = None
    variables = None
    exc = AnsibleOptionsError

# Generated at 2022-06-13 13:25:47.309062
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Tests if the call to run works correctly when parameters are
    provided correctly.
    """
    # GIVEN
    test_obj = LookupModule()
    test_obj.set_options({'plugin_type':'become',
                          'plugin_name':'pam'})

    # WHEN
    result = test_obj.run(terms=['DEFAULT_BECOME_METHOD'])

    # THEN
    assert result == ['sudo']

