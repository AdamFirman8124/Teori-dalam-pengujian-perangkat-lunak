

# Generated at 2022-06-13 13:16:16.078673
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        from unittest import mock
    except ImportError:
        import mock
    from ansible.module_utils._text import to_native
    from ansible.plugins.loader import lookup_loader
    C.config = mock.MagicMock()
    C.HOST_KEY_CHECKING = True
    # Remove 'config' lookup plugin from lookup_loader plugin directory
    del lookup_loader._lookup_fragment_classes['config']
    lookup_loader.add_directory(lookup_loader._real_loader, 'lookup_plugins')
    name = 'config'
    lookup_obj = lookup_loader.get(name)
    assert lookup_obj is not None, "Failed to find the 'config' lookup"
    # Test run method
    terms = ['HOST_KEY_CHECKING']
    variables=None


# Generated at 2022-06-13 13:16:26.003656
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    AnsibleOptionsError = ansible.errors.AnsibleOptionsError
    constants = ansible.constants
    loader = ansible.plugins.loader
    getattr = getattr
    string_types = ansible.module_utils.six.string_types

    # Configure test data
    terms = ["test", "var"]
    variables = "var_options"
    plugin_type = "cliconf"
    plugin_name = "test"
    C.config = "config"
    C.CONFIG_FILE = "/etc/ansible/ansible.cfg"
    args = dict(
      terms=terms,
      variables=variables,
      plugin_type=plugin_type,
      plugin_name=plugin_name
    )

    # Setup mocks
    real_getattr = getattr

# Generated at 2022-06-13 13:16:31.102693
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('Unit test for LookupModule._run')
    lookup_plugin = LookupModule()
    c_type = lookup_plugin.set_loader()
    args = 'ansible-config,list'
    results = lookup_plugin._run(terms=args, variables={})
    print(results)

# Generated at 2022-06-13 13:16:32.110198
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.run()

# Generated at 2022-06-13 13:16:40.535199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_type_error = 'Invalid setting identifier, "value" is not a string, its a'
    def test_exception(error, terms):
        try:
            lookup = LookupModule()
            lookup.set_options({'on_missing': 'error'})
            lookup.run(terms)
        except AnsibleOptionsError as e:
            assert str(e).startswith(error)

    test_exception('Unable to find setting value', ['value'])
    test_exception('Both plugin_type and plugin_name are required, cannot use one without the other', [], plugin_type='test')
    test_exception('Both plugin_type and plugin_name are required, cannot use one without the other', [], plugin_name='test')

# Generated at 2022-06-13 13:16:47.338064
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a LookupModule object
    lm = LookupModule()
    # Create a config setting name
    term = "DEFAULT_ROLES_PATH"
    # Create a list with the wantlist argument set to True
    wantlist = [term, True]
    # Retrieve the configuration value of the config setting
    result = lm.run(wantlist, None)
    # Check that the result is not empty
    assert result != []
# End of unit test for method run of class LookupModule

# Generated at 2022-06-13 13:16:55.241613
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  import os

  # Testing
  os.environ['ANSIBLE_LIBRARY'] = './library'

  #Test that terms is required
  lookup_module = LookupModule()
  try:
    lookup_module.run()
  except AnsibleOptionsError as e:
    assert '_terms is required' in e.message
  else:
    assert False, 'AnsibleOptionsError should have been raised'

  #Test that plugin_type and plugin_name are required when one of them set
  os.environ['ANSIBLE_CONFIG'] = './ansible.cfg'
  lookup_module = LookupModule()

# Generated at 2022-06-13 13:17:04.989842
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    args = (["DEFAULT_BECOME_USER"], {}, {})
    kwargs = {"wantlist": True}
    lookup_module._display = None

    #test for missing setting with on_missing as error
    try:
        ret = lookup_module._get_plugin_config("ssh","connection", "DOESNT_EXIST", {})
        lookup_module.run(*args, **kwargs)
        assert False
    except:
        assert True

    #Test for missing setting with on_missing as skip
    ret = lookup_module._get_global_config("DOESNT_EXIST")
    kwargs["on_missing"] = "skip"
    ret = lookup_module.run(*args, **kwargs)
    assert ret == []

    #Test for missing setting with on

# Generated at 2022-06-13 13:17:05.854651
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert True

# Generated at 2022-06-13 13:17:08.595111
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['DEFAULT_REMOTE_USER']
    result = module.run(terms, None)
    assert isinstance(result, list)


# Generated at 2022-06-13 13:17:25.655342
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    ret = lookup.run([], None)
    assert ret == []    
    with pytest.raises(AnsibleOptionsError):
        ret = lookup.run([], None, on_missing='bad_value')
    ret = lookup.run([], None, on_missing='error', plugin_type='become', plugin_name='sudo')
    assert ret == []
    ret = lookup.run([], None, on_missing='error', plugin_type='become', plugin_name='sudo')
    assert ret == []
    with pytest.raises(AnsibleOptionsError):
        ret = lookup.run([], None, on_missing='error', plugin_name='sudo')

# Generated at 2022-06-13 13:17:30.553824
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run(terms=["test_missing_setting"], variables={}, on_missing="error") == []
    assert module.run(terms=["DEFAULT_BECOME_USER"], variables={}, on_missing="error") == ["root"]
    assert module.run(terms=["DEFAULT_BECOME_USER"], variables={}, on_missing="skip") == ["root"]
    assert module.run(terms=["DEFAULT_BECOME_USER"], variables={}, on_missing="warn") == ["root"]
    assert module.run(terms=["DEFAULT_CALLBACK_PLUGINS"], variables={}, on_missing="error") == ["defaults", "skippy", "timer", "yaml", "json", "tree", "strace"]

# Generated at 2022-06-13 13:17:38.781117
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test when plugin_type and plugin_name is provided
    test_lookup = LookupModule()
    test_lookup.set_options(var_options=None, direct={'plugin_type': 'shell', 'plugin_name': 'sh'})
    data = test_lookup.run(terms=["remote_tmp"], variables=None, **{'plugin_type': 'shell', 'plugin_name': 'sh'})
    assert len(data) > 0
    # test when plugin_type and plugin_name is not provided
    test_lookup = LookupModule()
    test_lookup.set_options(var_options=None, direct={})
    data = test_lookup.run(terms=["DEFAULT_ROLES_PATH"], variables=None, **{})
    assert len(data) > 0
    # test

# Generated at 2022-06-13 13:17:46.001639
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    assert []   == mod.run(terms=['UNKNOWN'], on_missing='skip')
    assert []   == mod.run(terms=['UNKNOWN'], on_missing='warn')
    assert ["True"] == mod.run(terms=['ANSIBLE_DEBUG'], on_missing='skip')
    assert ["True"] == mod.run(terms=['ANSIBLE_DEBUG'], on_missing='warn')
    assert ["True"] == mod.run(terms=['ANSIBLE_DEBUG'], on_missing='error')
    try:
        mod.run(terms=['UNKNOWN'], on_missing='error')
    except AnsibleLookupError as e:
        assert 'Unable to find setting UNKNOWN' == to_native(e)

# Generated at 2022-06-13 13:17:51.108847
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class LookupModuleTest(LookupModule):

        def set_options(self, var_options=None, direct=None):

            self.options = {}

            if var_options:
                self.options = var_options
            if direct:
                self.options = direct

        def get_option(self, key):

            return self.options.get(key, None)

    # test without any exception raising
    lookup_module = LookupModuleTest()
    lookup_module.set_options(direct={'on_missing': 'error'})
    result = lookup_module.run(terms=['DEFAULT_BECOME_USER'])
    assert result == ['root']

    # on_missing has bad value
    lookup_module = LookupModuleTest()

# Generated at 2022-06-13 13:18:01.088992
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ["color_okay", "color_failed", "color_okay", "color_unreachable", "color_skipped"]
    ret = module.run(terms, on_missing="error",plugin_type="action", plugin_name="debug")
    assert ret == ["green", "red", "green", "purple", "cyan"]
    terms = ["color_okay", "color_failed", "color_okay", "color_unreachable", "color_skipped","color_not_available"]
    ret = module.run(terms, on_missing="error",plugin_type="action", plugin_name="debug")
    assert ret == ["green", "red", "green", "purple", "cyan"]

    # TODO: Write real unit-test for above, ansible-test

# Generated at 2022-06-13 13:18:09.251257
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # mock class constants to be used in the method call
    C.DEFAULT_ROLES_PATH = ["/var/ansible/roles", "/etc/ansible/roles"]

    # mock lookup class obj
    lu = LookupModule()

    # mock class loader of ansible.plugins.loader to be used in object of class LookupModule
    class MockAnsPlugLoader:
        @staticmethod
        def get(*args, **kwargs):
            return None

    class MockAnsPlugLookupBase:
        def set_options(*args, **kwargs):
            return None

    # mock ansible.plugins.loader
    plugin_loader = MockAnsPlugLoader()
    # mock ansible.plugins.lookup.LookupBase
    ansible.plugins.lookup.LookupBase = MockAnsPlugLookupBase()

# Generated at 2022-06-13 13:18:15.822016
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from __main__ import display

    lookup_plugin = LookupModule()
    lookup_plugin.set_runner(object())
    lookup_plugin._display = display
    lookup_plugin._templar = DataLoader()

    results = lookup_plugin.run(terms=['DEFAULT_HASH_BEHAVIOUR', 'DEFAULT_BECOME_USER', 'fake'])

    assert results == [C.DEFAULT_HASH_BEHAVIOUR, C.DEFAULT_BECOME_USER]

# Generated at 2022-06-13 13:18:18.507221
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_result = LookupModule().run(['remote_user'])
    assert len(my_result) == 1
    assert isinstance(my_result[0], string_types)

# Generated at 2022-06-13 13:18:29.050875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):
        def run(self, terms, variables=None, **kwargs):
            return super(TestLookupModule, self).run(terms, variables, **kwargs)

    from ansible.parsing.dataloader import DataLoader

    results = None

    data_loader = DataLoader()
    data_loader.set_vault_secrets([(None, None)])
    lookup = TestLookupModule()
    lookup.set_loader(data_loader)

    # Passing a list to lookup
    results = lookup.run(terms=['localhost', 'remote_user'], variables={'ANSIBLE_NET_SSH_PASS': 'somepass'})
    assert results == [['127.0.0.1'], 'root'], results

    # Passing a list to lookup, but with

# Generated at 2022-06-13 13:18:51.651823
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['ABCD', 'XYZ']
    assert lookup.run(terms) == [C.ABCD, C.XYZ]

    terms = ['ABCD', 'XYZ']
    missing = 'error'
    assert lookup.run(terms, on_missing=missing) == [C.ABCD, C.XYZ]

    terms = ['ABCD', 'XYZ']
    missing = 'warn'
    assert lookup.run(terms, on_missing=missing) == [C.ABCD, C.XYZ]

    terms = ['ABCD', 'XYZ']
    missing = 'skip'
    assert lookup.run(terms, on_missing=missing) == [C.ABCD, C.XYZ]

    terms = ['ABCD', 'XYZ']
    missing = 'unknown'
   

# Generated at 2022-06-13 13:19:01.768524
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test for parameters without plugin lookup
    # direct = True parameter
    lookup_module = LookupModule()

    # Term is a list of string
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']

    # Variables parameter
    variables = {}

    result = lookup_module.run(terms, variables, direct=True)

    assert result == ['root', ['./roles', './library']]

    # direct = False parameter
    lookup_module = LookupModule()

    # Term is string
    terms = 'DEFAULT_BECOME_USER'

    # Variables parameter
    variables = {}

    result = lookup_module.run(terms, variables, direct=False)

    assert result == ['root']

    # Test for parameters with plugin lookup
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:19:04.306938
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    for term in [1]:
        try:
            lm.run(terms=term)
        except Exception as e:
            assert isinstance(e, AnsibleOptionsError)

# Generated at 2022-06-13 13:19:15.977897
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import io
    from ansible.utils.color import stringc
    from ansible.plugins.lookup.config import LookupModule

    def test_run(terms, variables, on_missing, plugin_type, plugin_name, exp_rc, exp_out, exp_err, exp_msg=None, capture=io.StringIO(), patch_ansible_module=None, patch_ansible_utils=None):
        sys.stdout = capture
        sys.stderr = capture
        l = LookupModule()
        l.set_options(var_options=variables, direct={'on_missing': on_missing, 'plugin_type': plugin_type, 'plugin_name': plugin_name})
        ret = None
        try:
            ret = l.run(terms)
        except Exception as e:
            ret

# Generated at 2022-06-13 13:19:20.700155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def get_LookupModule_instance():
        return LookupModule()

    def get_terms():
        return ['DEFAULT_ROLES_PATH']

    def get_variable():
        return Sentinel

    def get_options():
        return {'on_missing': 'error'}

    lookup_module = get_LookupModule_instance()
    lookup_module.run(terms=get_terms(), variables=get_variable(), **get_options())


# Generated at 2022-06-13 13:19:33.582351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupPlugin = LookupModule()
    terms = ['localhost', 'port', 'become', 'become_ask_pass', 'become_user', 'become_method_path']
    variables = {'ansible_become_password': '1234567890'}
    plugin_type = 'connection'
    plugin_name = 'local'
    global_config = lookupPlugin.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name)
    ansible_config = [{'local': {'become': '', 'become_ask_pass': '', 'become_method': 'sudo', 'become_user': 'root', 'connector': 'local', 'port': ''}}]
    assert ansible_config == global_config

# Generated at 2022-06-13 13:19:39.954835
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # following code is for testing only
    import sys
    import os
    import unittest
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    from test.unit.ansible_module.test_ansible_module import TestAnsibleModule

    class TestHookModule(unittest.TestCase):

        def test_run_wrong_argument(self):
            # wrong argument name
            m = TestAnsibleModule(dict(
                {
                    'config': 'DEFAULT_ROLES_PATH',
                    'on_missing': 'skip'
                }
            ))
            lookup_class = m.get_lookup_plugin()

# Generated at 2022-06-13 13:19:40.355029
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:19:41.125857
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:19:52.672223
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test missing setting
    lm = LookupModule()
    lm.set_options(dict(on_missing='error'))
    try:
        lm.run(['FAKE_SETTING'])
        raise AssertionError('FAKE_SETTING should not exist')
    except MissingSetting as e:
        pass

    # Test case:
    # lookup('config', 'remote_tmp', plugin_type='shell', plugin_name='sh')
    lm = LookupModule()
    ret = lm.run(['remote_tmp'], dict(plugin_type='shell', plugin_name='sh'))
    assert ret == ['/tmp/ansible_shell_payload_cxraaAl']

    # Test case:
    # lookup('config', 'remote_user', 'port', plugin_type='connection', plugin

# Generated at 2022-06-13 13:20:28.584961
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(argument_spec={
        '_terms': dict(required=True, type='list'),
        'on_missing': dict(default='error', choices=['error', 'skip', 'warn']),
        'plugin_type': dict(choices=['become', 'cache', 'callback', 'cliconf', 'connection', 'httpapi', 'inventory', 'lookup', 'netconf', 'shell', 'vars']),
        'plugin_name': dict(type='str'),
    })

# Generated at 2022-06-13 13:20:42.086100
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    #Test failed with invalid plugin_type
    try:
        module.run(terms=['DEFAULT_ROLES_PATH'], plugin_name='ssh', plugin_type='conn')
    except AnsibleOptionsError as e:
        assert 'both' in to_native(e)

    #Test failed with invalid plugin_name
    try:
        module.run(terms=['DEFAULT_ROLES_PATH'], plugin_name='ssh', plugin_type='connection')
    except AnsibleOptionsError as e:
        assert 'not' in to_native(e)

    #Test failed due to invalid term

# Generated at 2022-06-13 13:20:54.639998
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    def set_options(var_options=None, direct=None):
        lm.options = direct
    lm.set_options = set_options
    lm.options = {}

    # terms: list of terms passed to the lookup plugin
    # variables: dict of variables passed to the lookup plugin
    # wantlist: boolean
    # on_missing: action to take if term is missing from config
    #    Error will raise a fatal error
    #    Skip will just ignore the term
    def run(terms, variables=None, wantlist=True, on_missing='error'):
        lm.options['wantlist'] = wantlist
        lm.options['on_missing'] = on_missing
        if isinstance(variables, dict):
            lm.options['var_options'] = variables
       

# Generated at 2022-06-13 13:21:06.525367
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_plugin = LookupModule()

    # Attempt to get a config setting specified by term
    term = "DEFAULT_MODULE_NAME"
    got = lookup_plugin.run(terms=[term], variables={'EXTRA_VAR': 'foo'}, on_missing='warn')
    assert got[0] == 'command'

    # Attempt to set a plugin name and type to use for validating
    # plugin config settings and test for a failure because both
    # parameters must be supplied, not just one or the other
    term = 'remote_user'

# Generated at 2022-06-13 13:21:17.061014
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # All of the tests in this file are marked xfail as PyTest doesn't handle
    # the use of the self._display.warning() method (which is a PyTest monkeypatch)
    # properly.
    import pytest
    pytest.xfail("PyTest does not support PyTest monkeypatch of self._display.warning()")
    # If on_missing is not supplied, it should default to error and raise an AnsibleOptionsError
    # exception
    lookup_module = LookupModule()
    terms = ['foo']
    try:
        lookup_module.run(terms)
    except AnsibleOptionsError:
        pass # This is expected
    # If on_missing is supplied and not in ['error', 'warn', 'skip'], an AnsibleOptionsError
    # exception should be raised
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:21:28.372454
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.modules.system.ping import ActionModule

    test_lookup = LookupModule()

    test_options = {
        'var_options': {'inventory_hostname': "localhost"},
        'direct': {'plugin_type': 'shell', 'plugin_name': 'sh'}
    }


# Generated at 2022-06-13 13:21:36.652151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 13:21:47.678875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    # Initialization
    lookup_module = LookupModule()
    lookup_module.set_options({'var_options': None, 'direct': {}})

    # Tests
    # Raise error if no plugin_type is provided
    lookup_module.set_options({'var_options': None, 'direct': {'plugin_name': 'become'}})
    assert to_text(lookup_module.run, [to_bytes('DEFAULT_BECOME_USER')]) == u'No plugin_type specified for lookup.'

    # Raise error if no plugin_name is provided
    lookup_module.set_options({'var_options': None, 'direct': {'plugin_type': 'become'}})

# Generated at 2022-06-13 13:21:55.228345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Testing _get_global_config
    result = lookup_module.run(terms=["DEFAULT_BECOME_USER"])
    assert len(result) == 1
    assert result[0] == "root"
    # Testing _get_plugin_config
    result = lookup_module.run(terms=["remote_user"], plugin_type="connection", plugin_name="ssh")
    assert len(result) == 1
    assert result[0] == "root"
    # Testing with non existent values
    result = lookup_module.run(terms=["DEFAULT_BECOME_USER", "DOES_NOT_EXIST"], on_missing="warn")
    assert len(result) == 1
    assert result[0] == "root"

# Generated at 2022-06-13 13:21:59.660189
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run([], terms=[], wantlist=True)
    assert result == []
    result = lookup.run([], terms=[], wantlist=False)
    assert result == []

# Generated at 2022-06-13 13:23:05.485122
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create test module to test LookupModule

    class TestModule(object):
        def __init__(self, display):
            self.display = display

    class TestLoader(object):
        @classmethod
        def get(cls, name, class_only=False):
            if name == 'awesome' and not class_only:
                return Awesome('awesome')
            return None

    plugin_loader.connection_loader = TestLoader
    plugin_loader.shell_loader = TestLoader

    # test terms
    terms = ['remote_user', 'port', 'remote_tmp']

    # Create a test LookupModule to test
    lu = LookupModule(loader=None, runner=None, display=TestModule('test'))

    # test for error
    # 'plugin_name' and 'plugin_type' are not specified
   

# Generated at 2022-06-13 13:23:13.702940
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:23:26.964683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(var_options=dict(log_path="logs_path"), direct=dict(on_missing="skip"))

    ret = l.run(terms=["log_path", "UNKNOWN"], variables=dict(log_path="logs_path"))
    assert ret == ["logs_path"]

    with pytest.raises(AnsibleOptionsError) as e:
        l.run(terms=["log_path", "UNKNOWN"], variables=dict(log_path="logs_path"), on_missing="not_valid_value")
    assert '"on_missing" must be a string and one of' in to_native(e)

    with pytest.raises(AnsibleOptionsError) as e:
        l.run(terms=[1])

# Generated at 2022-06-13 13:23:40.886929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    lookup = LookupModule()
    lookup_terms = ['DEFAULT_REMOTE_USER']
    lookup_variables = {
        'ansible_connection': 'local',
        'ansible_shell_type': 'csh',
        'ansible_python_interpreter': '/usr/bin/python',
        'inventory_dir': '/Users/user/ansible/test_inventory',
        'inventory_file': '/Users/user/ansible/test_inventory/inventory'
    }
    lookup_kwargs = {
        'config': {
            'DEFAULT_REMOTE_USER': 'meow',
            'RETRY_FILES_SAVE_PATH': '/tmp'
        },
        'wantlist': True
    }

# Generated at 2022-06-13 13:23:45.323494
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import connection_loader

    # test for global config
    plugin = LookupModule()

    # variable to hold config value
    config_value = "True"

    # variable to hold list of terms which need to be looked up
    terms = ['DEFAULT_LOAD_CALLBACK_PLUGINS']

    # variable to hold variables
    variables = ImmutableDict()

    # variable to hold option
    options = {}

    plugin.set_options(var_options=variables, direct=options)

    # set default value of option on_missing as "error"
    plugin.options['on_missing'] = "error"

    # get config value

# Generated at 2022-06-13 13:23:57.423781
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Basic test
    terms = ['DEFAULT_MODULE_UTILS']
    ret = lookup.run(terms=terms, variables=dict())
    assert ret[0] == 'ansible.module_utils'

    # Undefined option
    terms = ['UNKNOWN']
    ret = lookup.run(terms=terms, variables=dict())
    assert ret == []

    # Plugin test
    terms = ['DEFAULT_BECOME_METHOD']
    ret = lookup.run(terms=terms, variables=dict(), plugin_type="become", plugin_name="sudo")
    assert ret[0] == 'sudo'

    # Unsupported plugin type
    terms = ['DEFAULT_BECOME_METHOD']

# Generated at 2022-06-13 13:24:04.945192
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = [
        'DEFAULT_BECOME_USER',
        'DEFAULT_ROLES_PATH'
    ]
    result = lookup_module.run(terms)
    assert result == [u'root', [u'/etc/ansible/roles', u'/usr/share/ansible/roles']]

    result = lookup_module.run(['remote_tmp', 'remote_port'])
    assert result == [u'$HOME/.ansible/tmp', 22]

    variables = dict(ansible_port=9000)
    result = lookup_module.run(['remote_port'], variables=variables)
    assert result == [9000]

    terms = ['DEFAULT_BECOME_USER', 'UNKNOWN']

# Generated at 2022-06-13 13:24:15.907451
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:24:19.009947
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(terms="DEFAULT_BECOME_USER") == ['root']


# Generated at 2022-06-13 13:24:27.684348
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    # setup
    module = LookupModule()
    terms = ['remote_tmp', 'remote_port']
    variables = {'ansible_port': 8091}
    kwargs = {'plugin_type': 'shell', 'plugin_name': 'sh'}
    module._display = FakeDisplay()
    expected = '/tmp/$USER', 8091

    # execute
    result = module.run(terms, variables, **kwargs)

    # assert
    assert result == expected
