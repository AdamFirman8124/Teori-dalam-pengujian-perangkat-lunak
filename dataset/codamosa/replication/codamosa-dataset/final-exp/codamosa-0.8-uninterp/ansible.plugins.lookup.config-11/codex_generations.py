

# Generated at 2022-06-13 13:16:06.931162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arranges
    class C(object):
        RE_JINJA_PATTERN = 'RE_JINJA_PATTERN'
        DEFAULT_MODULE_NAME = 'DEFAULT_MODULE_NAME'
        DEFAULT_REMOTE_TMP = 'DEFAULT_REMOTE_TMP'
        ANSIBLE_ROLES_PATH = ['ANSIBLE_ROLES_PATH1', 'ANSIBLE_ROLES_PATH2']
        DEFAULT_CACHE_PLUGIN = 'DEFAULT_CACHE_PLUGIN'
        DEFAULT_CACHE_PLUGIN_CONNECTION = 'DEFAULT_CACHE_PLUGIN_CONNECTION'
        DEFAULT_GATHERING = 'DEFAULT_GATHERING'


# Generated at 2022-06-13 13:16:16.299465
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    terms = ['DEFAULT_ROLES_PATH']
    variables = {}
    ptype = 'connection'
    pname = 'local'

    lookup_instance = LookupModule()
    lookup_instance.set_options({'var_options':variables, 'plugin_type':ptype, 'plugin_name':pname, 'on_missing':'error'})
    result = lookup_instance.run(terms)
    
    #first check the array is not empty
    assert len(result) > 0
    
    #then check that at least one element in the array is a string
    assert isinstance(result[0], str)

# Generated at 2022-06-13 13:16:22.163185
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import mock
    import ansible.plugins.loader as loader
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.six import string_types
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.six.moves import builtins

    # setting up a mock object for the plugin loader to return
    p = mock.MagicMock()
    p._load_name = 'sh'

    # setting up a mock object to return for the plugin loader
    loader_obj = mock.MagicMock()
    loader_obj.get = mock.MagicMock(return_value = p)

    # setting up a mock object to return for the plugin loader
    loader_get_obj = mock.MagicMock()

# Generated at 2022-06-13 13:16:26.758534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # set up args
    terms = ["DEFAULT_BECOME_USER"]
    variables = {}
    kwargs = {}
    kwargs["on_missing"] = False
    kwargs["plugin_type"] = False
    kwargs["plugin_name"] = False

    # get result
    result = LookupModule().run(terms, variables, **kwargs)
    print("result = ", result)

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:16:31.493599
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['remote_user', 'port']
    result_list = lookup_module.run(terms=terms, plugin_name='ssh', plugin_type='connection')
    assert result_list[0] == 'remote_user'
    assert result_list[1] == 22

# Generated at 2022-06-13 13:16:36.145790
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # If a config value is not present in constants,
    # getattr(C, config) will return an AttributeError
    # So, here we are testing the execution with missing
    # config value.
    try:
        test = LookupModule()
        terms = ['TEST']
        test.run(terms)
    except AttributeError:
        pass


# Generated at 2022-06-13 13:16:47.846668
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import json
    from ansible.vars.hostvars import HostVars

    # Tests run of LookupModule with different options.
    # This function tests the method run of class LookupModule. All the possible test cases are listed below.
    # 1. term is not a string, in this case "on_missing" is "error", error message is raised.
    # 2. term is not a string, in this case "on_missing" is "warn", warning is raised.
    # 3. term is not a string, in this case "on_missing" is "skip", no exception is raised.
    # 4. term is not valid, in this case "on_missing" is "error", error message is raised.
    # 5. term is not valid, in this case "on_missing" is "warn", warning is raised.
    # 6. term is

# Generated at 2022-06-13 13:16:54.479543
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for the method run of the class LookupModule
    """
    terms = ['DEFAULT_BECOME_USER']
    variables = {}
    kwargs = {}
    kwargs['on_missing'] = 'error'
    kwargs['plugin_type'] = None
    kwargs['plugin_name'] = None
    lookup_module = LookupModule()
    assert lookup_module.run(terms, variables, **kwargs) == [u'root']



# Generated at 2022-06-13 13:17:03.264589
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test error if on_missing is not a string or not one of error,warn and skip
    assert_raises(AnsibleOptionsError, assert_raises(AnsibleLookupError, LookupModule().run))

    # Test error if plugin_type or plugin_name is given but not both
    assert_raises(AnsibleOptionsError, assert_raises(AnsibleLookupError, LookupModule().run, [], plugin_type='connection'))
    assert_raises(AnsibleOptionsError, assert_raises(AnsibleLookupError, LookupModule().run, [], plugin_name='network_cli'))

# Generated at 2022-06-13 13:17:14.580471
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    a = LookupModule()

# Generated at 2022-06-13 13:17:35.058433
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    # Test case with missing setting and on_missing=error
    try:
        lm.run(terms=['FOOBAR'], variables=None, on_missing='error')
    except AnsibleLookupError as e:
        assert e.message=='Unable to find setting FOOBAR'

    # Test case with missing setting and on_missing=warn
    lm.run(terms=['FOOBAR'], variables=None, on_missing='warn')

    # Test case with missing setting and on_missing=skip
    assert lm.run(terms=['FOOBAR'], variables=None, on_missing='skip')

    # Test case with non-string values passed in terms

# Generated at 2022-06-13 13:17:35.606344
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert True


# Generated at 2022-06-13 13:17:38.842524
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    var_options = None
    result = lookup_instance.run(terms, var_options, direct=None)
    assert result == ['root']

# Generated at 2022-06-13 13:17:46.014182
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    # load test vars and a config plugin
    config = os.path.join(os.path.dirname(__file__), 'fixtures', 'config.yml')
    if config not in sys.path:
        sys.path.append(config)
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    lm = LookupModule()
    inventory = DataLoader().load_from_file('inventory.yml')
    variable_manager = VariableManager(loader=inventory)
    option_values = dict(
        var_options = variable_manager,
        direct = dict()
    )
    lm.set_options(**option_values)
    # find

# Generated at 2022-06-13 13:17:48.858178
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['ANSIBLE_INVENTORY', 'ANSIBLE_CACHE_PLUGIN_CONNECTION', 'ANSIBLE_EXAMPLES_DIR']
    module_args = {'plugin_type': 'cache', 'plugin_name': 'jsonfile'}
    lookup_plugin = LookupModule()
    result = lookup_plugin.run(terms=terms, variables=None, **module_args)[0]
    assert isinstance(result, string_types)
    assert result == '~/.ansible/cache'

# Generated at 2022-06-13 13:17:59.631315
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    # Test when plugin_name param is not provided
    module = LookupModule()
    module.set_loader(DataLoader())

    result = module.run([
        'default_remote_tmp',
        'default_remote_tmp',
        'plugin_filters_core',
        'remote_user',
        'retry_files_save_path',
    ])
    assert result == ['/tmp/ansible-${USER}', '/tmp/ansible-${USER}', '', '', '~/.ansible/retry']

    # Test when plugin_name param is provided
    module = LookupModule()
    module.set_loader(DataLoader())
    module.set_options(dict(plugin_type='shell', plugin_name='sh'))

   

# Generated at 2022-06-13 13:18:01.236373
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["C.DEFAULT_MODULE_NAME"])[0] == 'command'

# Generated at 2022-06-13 13:18:09.307498
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    lm = LookupModule(loader=None, variable_manager=variable_manager, templar=None, shared_loader_obj=None)
    result = lm.run(terms=['DEFAULT_BECOME_METHOD'], variables=None, **{})
    assert result == ['sudo']

# Generated at 2022-06-13 13:18:10.312406
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-13 13:18:14.209601
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    cls = LookupModule()
    # test with terms
    terms = "bar"
    actual = cls.run(terms)
    assert [] == actual
    # test with no terms
    terms = []
    actual = cls.run(terms)
    assert [] == actual


# Generated at 2022-06-13 13:18:36.572478
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lm = LookupModule()

    assert lm.run([
        "INVALID",
        "UNDEF"
    ]) == []

    assert lm.run([
        "INVALID",
        "INVALID",
        "UNDEF"
    ]) == []

    assert lm.run([
        "INVALID",
        "INVALID",
        "UNDEF"
    ], on_missing='warn') == []

    assert lm.run([
        "INVALID",
        "INVALID",
        "UNDEF"
    ], on_missing='skip') == []

    assert lm.run([
        "INVALID",
        "INVALID",
        "UNDEF"
    ], on_missing='error') == []

# Generated at 2022-06-13 13:18:46.917223
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''
    lookup_module = LookupModule()

    # Case 1: Plugin type and name specified, configuration retrieved for plugin
    result = lookup_module.run(terms=["remote_tmp"], variables=None, plugin_type="shell", plugin_name="sh")
    assert result == ['/tmp']

    # Case 2: Plugin type and name specified, configuration not found for plugin and missing is error
    try:
        result = lookup_module.run(terms=["remote_tmp"], variables=None, plugin_type="shell", plugin_name="csh", on_missing="error")
        assert False
    except AnsibleLookupError as e:
        assert e.__str__() == 'Unable to find setting remote_tmp'

    # Case 3: Plugin type and name specified, configuration not found for

# Generated at 2022-06-13 13:18:54.419905
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    got_sentinel = 0

# Generated at 2022-06-13 13:19:03.695522
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_USER']
    pname = 'sh'
    ptype = 'shell'
    # Create an object of class LookupModule, initialize with arguments and run method
    a = LookupModule().run(terms)
    assert isinstance(a, list)
    a = LookupModule(basedir='ansible/').run(terms)
    assert isinstance(a, list)
    a = LookupModule(basedir='ansible/', basedir_expanduser=True).run(terms)
    assert isinstance(a, list)
    a = LookupModule(plugin_name=pname, plugin_type=ptype).run(terms)
    assert isinstance(a, list)
    a = LookupModule(plugin_name=pname).run(terms)

# Generated at 2022-06-13 13:19:15.646489
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """This function is used to check that lookup module is working as expected"""
    #pylint: disable=too-many-locals
    import os
    import sys
    import unittest
    # Get the absolute path of this file.
    # All the testing files will be relative to this file.
    TEST_DIR = os.path.abspath(os.path.dirname(__file__))
    # Get the path of the 'lib' directory
    LIB_DIR = os.path.join(TEST_DIR, '..', 'lib')
    sys.path.append(LIB_DIR)
    from AnsibleModuleUtils.config_init import get_config
    from AnsibleModuleUtils.config_init import get_plugin_config
    from AnsibleModuleUtils.config_init import get_global_config
    import ansible

# Generated at 2022-06-13 13:19:23.077569
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # test raise AnsibleLookupError('Invalid setting identifier, "foo" is not a string, its a <class 'bool'>')
    try:
        lookup.run(['foo'], skip=True)
        assert False,'should have raise an exception'
    except AnsibleLookupError as e:
        assert 'Invalid setting identifier, "foo" is not a string, its a <class \'bool\'>' == to_native(e)

    # test raise AnsibleOptionsError("'on_missing' must be a string and one of 'error', 'warn' or 'skip', not foo")

# Generated at 2022-06-13 13:19:35.303384
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config_term = "default_module_name"
    ptype = "connection"
    pname = "ssh"
    variable = "ansible_default_module_name"
    variable_value = "command"
    missing_term = "not_set"

    # Create a LookupModule object
    LookupModule_obj = LookupModule()

    # Add default variable value
    LookupModule_obj.set_default('_ansible_vars', {variable: variable_value})

    # Test run method with value found in config
    result = LookupModule_obj.run([config_term])
    assert result == [variable_value]

    # Test run method with plugin_type and plugin_name
    result = LookupModule_obj.run([config_term], plugin_type=ptype, plugin_name=pname)
   

# Generated at 2022-06-13 13:19:49.056208
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import tempfile
    import os
    import sys
    import io
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import callback_loader

    class FakePlayContext(object):
        def __init__(self):
            self.connection = None
            self.become_method = None
            self.become_user = None
            self.become_password = None

    class FakeOptions(object):
        def __init__(self):
            self.verbosity = 0
            self.listtags = False
            self.listtasks = False
            self.listhosts = False
            self.syntax = False
            self.connection = 'default'
            self.module_path = None
            self.forks = 5
            self.remote_user = 'test_user'

# Generated at 2022-06-13 13:19:53.894155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    #Pre-validate the constants.py module
    assert hasattr(C, 'ANSIBLE_CONFIG')
    #Run the lookup
    result = lookup_module.run([C.ANSIBLE_CONFIG], variables=None)
    assert result == [C.ANSIBLE_CONFIG]

# Generated at 2022-06-13 13:20:03.862726
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    kwargs = {'_terms':['C'], 'plugin_type':'connection', 'plugin_name':'local'}
    lookup = LookupModule()
    assert type(lookup.run(**kwargs)) is list

    kwargs = {'_terms':['C'], 'plugin_type':'connection', 'plugin_name':'local'}
    lookup = LookupModule()
    assert type(lookup.run(**kwargs)) is list

    kwargs = {'_terms':['C'], 'plugin_type':'connection', 'plugin_name':'local'}
    lookup = LookupModule()
    assert type(lookup.run(**kwargs)) is list

    kwargs = {'_terms':['C'], 'plugin_type':'connection', 'plugin_name':'local'}

# Generated at 2022-06-13 13:20:33.774701
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    assert lookup.run("DEFAULT_BECOME_USER") == [u'root']

# Generated at 2022-06-13 13:20:34.642214
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert False

# Generated at 2022-06-13 13:20:44.104856
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    tester = LookupModule()
    tester.set_options(Direct({'plugin_name': 'shell', 'plugin_type': 'shell'}))

    # invalid setting identifier
    term = 0
    try:
        tester.run([term])
        assert False
    except AnsibleOptionsError as e:
        pass

    # valid setting identifier
    term = 'ansible_shell_type'
    value = tester.run([term])
    assert len(value) == 1
    assert value[0] == C.DEFAULT_SHELL

    try:
        tester.run([term], variables={'ansible_shell_type': 'not_a_shell'})
        assert False
    except AnsibleError as e:
        pass


# Generated at 2022-06-13 13:20:59.406532
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _test_LookupModule_run(terms, variables, **kwargs):
        # Make the following attributes accessible for testing.
        lookup_module = LookupModule()
        lookup_module._display = _display
        lookup_module._loader = _loader

        return lookup_module.run(terms, variables=variables, **kwargs)

    # Setup fixtures
    _display = _display_fixture()
    _loader = _loader_fixture()

    # Test with one term
    terms = ['DEFAULT_BECOME_USER']
    variables = {}
    assert _test_LookupModule_run(terms, variables, on_missing='error') == ['root']

    # Test with multiple terms
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD']
    variables = {}
    assert _

# Generated at 2022-06-13 13:21:08.233512
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup_plugin = lookup_loader.get('config')

    terms = ['DEFAULT_REMOTE_TMP', 'remote_tmp', 'x', 'UNKNOWN']
    variables = dict(
        TERM='config',
        TERM1='remote_tmp',
        TERM2='x',
        TERM3='UNKNOWN',
        plugin_type='shell',
        plugin_name='sh',
        on_missing='error'
    )

    ret = lookup_plugin.run(terms, variables)

    assert ret[0] == '~/.ansible/tmp'
    assert ret[1] == '~/.ansible/tmp'
    assert ret[2] == 'x'
    assert ret[3] is None

# Generated at 2022-06-13 13:21:17.678457
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a fake LookupModule instance
    lookup_module = LookupModule()

    # Create a fake terms param with a list of config parameters
    terms = ['DEFAULT_ROLES_PATH', 'DEFAULT_BECOME_USER']

    # Create a fake variable for the variable parameter
    variable = {'ansible_color': 'false'}

    # Create a fake config variable
    config = 'DEFAULT_ROLES_PATH'

    # Define a fake variable for the config variable
    C.DEFAULT_ROLES_PATH = 'fake_role_path'

    # Call run method
    result = lookup_module.run(terms, variable)

    # Assert the result
    assert result == [C.DEFAULT_ROLES_PATH]



# Generated at 2022-06-13 13:21:28.639260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Checks for error when we define both plugin_name and plugin_type
    try:
        lookup.run(terms="testcase", variables=None, plugin_type="shell", plugin_name="sh", on_missing="error")
        assert False
    except AnsibleOptionsError:
        assert True

    # Checks for error when we define plugin_name but not plugin_type
    try:
        lookup.run(terms="testcase", variables=None, plugin_name="sh", on_missing="error")
        assert False
    except AnsibleOptionsError:
        assert True

    # Checks for error when we define plugin_type but not plugin_name

# Generated at 2022-06-13 13:21:36.848262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Declare Testing class
    class TestLookupModule(LookupModule):
        def __init__(self):
            pass

    lookup_module = TestLookupModule()
    setattr(lookup_module, "_display", Mock())

    # Test without plugin_type and plugin_name options
    # Test with default value for on_missing
    terms = ['host_key_checking']
    variables = None
    result = lookup_module.run(terms, variables)
    assert result==[C.DEFAULT_HOST_KEY_CHECKING]

    # Test with on_missing=warn
    terms = ['DEFAULT_ROLES_PATH']
    variables = None
    result = lookup_module.run(terms, variables, on_missing='warn')
    assert result==[C.DEFAULT_ROLES_PATH]

    # Test

# Generated at 2022-06-13 13:21:47.816772
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestPlugin():
        def __init__(self, name, path):
            self._load_name = name
            self._load_path = path

    class TestPluginLoader():
        def __init__(self, name):
            self.name = name
            self._plugins = {}

        def get(self, name, class_only):
            try:
                return self._plugins[name]
            except KeyError:
                raise AnsibleLookupError('Unable to load %s plugin "%s"' % (self.name, name))

        def add(self, name, path):
            self._plugins[name] = TestPlugin(name, path)

    class TestConfig():
        def __init__(self, lookup_plugin=None, module_path=None, plugin_path=None, variable_manager=None):
            self.lookup

# Generated at 2022-06-13 13:21:55.621374
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockDisplay(object):
        def __init__(self):
            self.msg = []
        def warning(self, msg):
            self.msg.append(msg)

    def _get_global_config(config):
        if config == '_test_':
            return 'ok'

    lu = LookupModule()
    setattr(lu, 'set_options', lambda terms: None)
    setattr(lu, 'get_option', lambda x: None)
    lu._display = MockDisplay()
    lu.run(['_test_'])
    assert lu.run(['_test_']) == ['ok']
    lu.run(['_test_', '_test_'])
    assert lu.run(['_test_', '_test_']) == ['ok', 'ok']


# Generated at 2022-06-13 13:23:03.316069
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Testing the lookup plugin config
    # GOOD PARAMETERS
    lookup_plugin = LookupModule()
    lookup_plugin.set_options({})
    terms = ['DEFAULT_BECOME_USER']
    assert lookup_plugin.run(terms, variables=dict(), on_missing='skip') == ['root']

    # case with no arguments
    lookup_plugin = LookupModule()
    lookup_plugin.set_options({'on_missing': 'skip'})
    terms = []
    assert lookup_plugin.run(terms, variables=dict()) == []

    # case with invalid term
    lookup_plugin = LookupModule()
    lookup_plugin.set_options({'on_missing': 'error'})
    terms = ['UNKNOWN']

# Generated at 2022-06-13 13:23:07.533572
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule(templar=None, loader=None)
    lm.set_options(var_options={}, direct={})

    lm.get_option('on_missing')
    lm.get_option('plugin_type')
    lm.get_option('plugin_name')

    terms = ['DEFAULT_ROLES_PATH', 'BAR']
    variables = None
    kwargs = {}
    lm.run(terms=terms, variables=variables, **kwargs)
    return True

# Generated at 2022-06-13 13:23:22.211307
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock inventory
    inventory = mock.Mock()
    inventory.hosts = {}
    inventory.get_hosts.return_value = {}
    inventory.get_host.return_value = None
    inventory.get_group.return_value = None
    inventory.get_group_variables.return_value = {}
    inventory.get_host_variables.return_value = {}

    # Make a mock play and task
    play = mock.Mock()
    play.hosts.return_value = {}
    play.get_variables.return_value = {}

    task = mock.Mock()
    task.hosts.return_value = {}
    task.get_variables.return_value = {}

    # Set up our fake loader
    loader = mock.Mock()

# Generated at 2022-06-13 13:23:24.339366
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["DEFAULT_BECOME_METHOD"]) == ["sudo"]

# Generated at 2022-06-13 13:23:33.219984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule

    lookup = LookupModule()
    try:
        lookup.run(terms='invalid_setting', variables={}, on_missing='error')
    except AnsibleLookupError as err:
        assert str(err) == "Unable to find setting invalid_setting", err
    else:
        raise AssertionError('Expected failure of lookup.run(terms="invalid_setting", variables={}, on_missing="error")')

    try:
        lookup.run(terms=['invalid_setting1', 'invalid_setting2'], variables={}, on_missing='error')
    except AnsibleLookupError as err:
        assert str(err) == "Unable to find setting ['invalid_setting1', 'invalid_setting2']", err
    else:
        raise Ass

# Generated at 2022-06-13 13:23:46.115529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        from __main__ import display
    except ImportError:
        display = None

    lookup = LookupModule(loader=None, variables=None, templar=None, display=display)
    try:
        lookup.run([])
    except AnsibleOptionsError as e:
        assert 'A term is required' in str(e)

    try:
        lookup.run([123])
    except AnsibleOptionsError as e:
        assert 'Invalid setting identifier' in str(e)

    try:
        lookup.run([u'foo'])
    except AnsibleLookupError as e:
        assert 'Unable to find setting foo' in str(e)


# Generated at 2022-06-13 13:23:49.761843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test the method run of the class LookupModule
    """
    # run method of class LookupModule cannot be tested as it is calling getattr of class C, which cannot be mocked

    # test file ansible/test/unit/plugins/lookup/test_config.py describes this test

# Generated at 2022-06-13 13:24:00.711859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(terms=['DEFAULT_ROLES_PATH'], variables={}) == C.DEFAULT_ROLES_PATH
    assert lookup_plugin.run(terms=['DEFAULT_ROLES_PATH'], on_missing='skip', variables={}) == C.DEFAULT_ROLES_PATH
    assert not lookup_plugin.run(terms=['x_x_x'], on_missing='skip', variables={})

    assert lookup_plugin.run(terms=['DEFAULT_ROLES_PATH'], on_missing='warn', variables={}) == C.DEFAULT_ROLES_PATH
    assert lookup_plugin.run(terms=['x_x_x'], on_missing='warn', variables={}) == []


# Generated at 2022-06-13 13:24:11.624317
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _get_global_config(config):
        return 'in_memory'

    def _get_plugin_config(config, variables):
        plugin_config = {
            'plugin_type': {
                'plugin_name': {
                    'key1': 'value1'
                }
            }
        }
        return plugin_config['plugin_type']['plugin_name'].get(config)

    with patch.object(LookupModule, 'run_command', return_value=('Hello User', '', 0)):
        lookup_obj = LookupModule()

# Generated at 2022-06-13 13:24:18.444986
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["DEFAULT_BECOME_USER"]
    variables = {"ansible_connection": "network_cli"}
    config = {"on_missing": "warn", "plugin_type": "cliconf", "plugin_name": "eos"}

    lookup = LookupModule()
    result = lookup.run(terms=terms, variables=variables, **config)
    assert result != None
    assert result == ['ansible']