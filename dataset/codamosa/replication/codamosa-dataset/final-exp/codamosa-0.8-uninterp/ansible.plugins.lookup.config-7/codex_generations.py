

# Generated at 2022-06-13 13:16:15.934953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    lm = LookupModule()
    m = 'ansible.plugins.lookup.config'
    with patch("%s.AnsibleOptionsError" % m) as mock_AnsibleOptionsError:
        mock_AnsibleOptionsError.side_effect = AnsibleOptionsError
        with patch("%s.AnsibleLookupError" % m) as mock_AnsibleLookupError:
            mock_AnsibleLookupError.side_effect = AnsibleLookupError
            with patch("%s.AnsibleError" % m) as mock_AnsibleError:
                mock_AnsibleError.side_effect = AnsibleError
                with patch("%s.Sentinel" % m) as mock_Sentinel:
                    mock_Sentinel.side_effect = Sentinel

# Generated at 2022-06-13 13:16:25.901861
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit tests for method LookupModule.run
    """
    def call_lookup_module_run(terms, variables=None,
            on_missing=None, plugin_type=None, plugin_name=None):
        """Call LookupModule.run
        """
        l = LookupModule()
        l.set_options(var_options=variables,
            direct={
                'on_missing': on_missing,
                'plugin_type': plugin_type,
                'plugin_name': plugin_name,
            })
        return l.run(terms, variables)

    result = call_lookup_module_run(['DEFAULT_HOST_LIST'],
        on_missing='unknown')
    assert result == ['inventory']

    result = call_lookup_module_run(['HOST_LIST'])
   

# Generated at 2022-06-13 13:16:35.942917
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import LookupModule

    ptype = 'connection'
    plugin_name = 'ssh'

    class SSHConnection(object):
        def __init__(self):
            self._load_name = plugin_name

    loader = getattr(plugin_loader, '%s_loader' % ptype)
    loader._plugins[plugin_name] = SSHConnection

    try:
        lookup = LookupModule()
        result = lookup.run([
            'remote_user',
            'port'
            ], plugin_type=ptype, plugin_name=plugin_name)

        assert result[0] == 'remote_user'
        assert result[1] == 22
    finally:
        del loader._plugins[plugin_name]

# Generated at 2022-06-13 13:16:46.196637
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Unit test for method run of class LookupModule '''
    module = LookupModule()
    terms = ['DEFAULT_ROLES_PATH']
    kwargs = {'plugin_name': 'bash', 'plugin_type': 'shell'}
    ret = module.run(terms, **kwargs)
    assert isinstance(ret, list)
    assert len(ret) == 1
    assert isinstance(ret[0], string_types)
    print("Expected result : %s, Actual result : %s" % (C.DEFAULT_ROLES_PATH, ret[0]))
    assert ret[0] == C.DEFAULT_ROLES_PATH


# Generated at 2022-06-13 13:16:48.806233
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options()
    print(lookup_module.run(['DEFAULT_ROLES_PATH', 'DEFAULT_ROLES_PATH']))


# Generated at 2022-06-13 13:16:55.799607
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["DEFAULT_ROLES_PATH", "DEFAULT_ROLES_PATH", "DEFAULT_ROLES_PATH"]
    variables = {}
    kwargs = {} 
    lookup_object = LookupModule()
    lookup_object.set_options(var_options=variables, direct=kwargs)
    result = lookup_object.run(terms, variables=None, **kwargs)
    assert result is not None
    assert len(result) > 0
    assert isinstance(result, list)
    assert isinstance(result[0], list)
    assert len(result[0]) > 0

# Generated at 2022-06-13 13:17:05.069004
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test on get a valid config
    lookup_instance = LookupModule()
    result = lookup_instance.run(['DEFAULT_ROLES_PATH'])
    assert(isinstance(result, list))
    assert(len(result) == 1)
    assert (isinstance(result[0], str))
    assert ('roles' in result[0])

    # Test on get a invalid config
    try:
        lookup_instance.run(['test_test_test'])
        raise AssertionError('Test was supposed to raise an error')
    except AnsibleLookupError:
        pass

    # Test on get a invalid config with on_missing='warn'

# Generated at 2022-06-13 13:17:07.138721
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(direct={'on_missing': 'warn'})
    assert l.run(['UNKNOWN']) == []

# Generated at 2022-06-13 13:17:15.855699
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unittest for checking if the run method of LookupModule works
    # NOTE: I didn't define the variables and kwargs, what does work is
    #       setting them to None and {} respectively in the call
    # TODO: Set variables and kwargs

    # Importing LookupModule to a variable
    lookup_module = __import__('ansible.plugins.lookup.config')
    lookup_module = getattr(lookup_module.plugins.lookup, 'config', None)

    # Creating the object
    lookup_object = lookup_module.LookupModule()

    # Setting the object options
    # TODO: Check if variables and kwargs are correctly set (if they are needed)
    #       If a better way is found to set the variables and kwargs please change it

# Generated at 2022-06-13 13:17:19.579730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    plug = LookupModule()
    res = plug.run(terms=["DEFAULT_HASH_BEHAVIOUR", "INVALID_HASH_BEHAVIOUR"], on_missing="warn")
    assert isinstance(res, list)

# Generated at 2022-06-13 13:17:43.200810
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.config.manager import ConfigManager
    from ansible.plugins.lookup import LookupModule
    import os

    config_manager = ConfigManager()
    config_manager.get_config_value = Mock(side_effect=lambda config: {"host_key_checking": True}.get(config))
    config_manager._get_plugin_config_value = Mock(side_effect=lambda config, ptype, pname, variables: {"foo": "bar"}.get(config))
    config_manager.get_config_value.return_value = True

    lookup_module = LookupModule()
    lookup_module.set_loader = Mock()
    lookup_module.get_basedir = Mock(return_value=os.getcwd())
    lookup_module._display = Mock()
    lookup_module.set_options = Mock()


# Generated at 2022-06-13 13:17:51.820256
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module._get_plugin_config("shell", "shell", "remote_tmp", None) == '$HOME/.ansible/tmp'
    assert lookup_module._get_global_config("DEFAULT_JINJA2_NATIVE") is True
    assert lookup_module.run(["DEFAULT_JINJA2_NATIVE"], None) == [True]
    assert lookup_module.run(["UNKNOWN"], None, on_missing='skip') == []
    assert lookup_module.run(["UNKNOWN"], None, on_missing='warn') == []

# Generated at 2022-06-13 13:17:54.544505
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    terms = ['DEFAULT_BECOME_USER']
    result = lu.run(terms)
    assert result == ['root']

# Generated at 2022-06-13 13:18:02.376100
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class TestLookupModule(LookupModule):
        def __init__(self, basedir=None, **kwargs):
            self.basedir = basedir

        def run(self, terms, **kwargs):
            return terms

    terms = ['test1', 'test2']
    variables = {
        'test': 'test'
    }

    assert TestLookupModule(basedir='/test1').run(terms) == terms
    assert TestLookupModule(basedir='/test1', variable='test').run(terms, variables=variables) == terms
    assert TestLookupModule(basedir='/test1', variable='test').run(terms) == terms

# Generated at 2022-06-13 13:18:09.943688
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader
    from ansible.plugins.lookup import LookupModule
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    # prepare lookup
    lookup_instance = LookupModule()
    lookup_instance._templar = Templar()

    # run lookup with a plugin name and type (get shell plugin config for remote_tmp setting):
    ptype = 'shell'
    pname = 'sh'

    # Test the shell plugin setting value from default ansible.cfg
    expected = '/tmp'
    result = lookup_instance.run(terms=['remote_tmp'], variables={}, plugin_type=ptype, plugin_name=pname)
    assert result == [expected]

    # Test the shell plugin setting value from passed ansible configuration

# Generated at 2022-06-13 13:18:14.196502
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={}, direct={})
    lookup_module.run(terms=['DEFAULT_ROLES_PATH', 'DEFAULT_BECOME_USER'], variables={}, plugin_type='become', plugin_name=None, on_missing='error')

# Generated at 2022-06-13 13:18:24.408750
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import imp
    import pytest
    from ansible.playbook.play_context import PlayContext

    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'config_data')
    fixtures = []

    # get all the test data
    for filename in os.listdir(fixture_path):
        if (filename.endswith('.py') and filename.startswith('test_')):
            module_name = os.path.splitext(filename)[0]
            #module_name = '.'.join(['test_config_data', module_name])
            module = imp.load_source(module_name, os.path.join(fixture_path, filename))
            fixtures.append(module)

    # iterate through all test

# Generated at 2022-06-13 13:18:34.145497
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # _get_global_config(config):

    # C.BECOME_METHOD
    terms = 'BECOME_METHOD'
    assert LookupModule.run(terms, variables=None, **kwargs) == ['sudo']

    # C.DEFAULT_HASH_BEHAVIOUR
    terms = 'DEFAULT_HASH_BEHAVIOUR'
    assert LookupModule.run(terms, variables=None, **kwargs) == [None]

    # C.DEFAULT_ROLES_PATH
    terms = 'DEFAULT_ROLES_PATH'
    assert LookupModule.run(terms, variables=None, **kwargs) == ['/etc/ansible/roles', '~/.ansible/roles', '/usr/share/ansible/roles']

    # C.HASH_BEHAVIOUR


# Generated at 2022-06-13 13:18:41.288693
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:18:50.347104
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # we should get error if missing param is invalid
    lm = LookupModule()
    invalid_missing = ['fail', 'abort', '', 'error', 'warn', 'skip']
    lm.set_options(direct={'on_missing': 'fail'})
    for invalid in invalid_missing:
        assert lm.get_option('on_missing') != invalid

    # we should get error if plugin_type or plugin_name is invalid
    invalid_plugin = ['', 'cliconf', 'httpapi', 'vars']
    for invalid in invalid_plugin:
        lm.set_options(direct={'plugin_type': 'connection'})
        lm.set_options(direct={'plugin_name': invalid})
        assert lm.get_option('plugin_name') != invalid

    # we should get error if term

# Generated at 2022-06-13 13:19:31.791661
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockDisplay:
        def __init__(self):
            self.logger = []

        def warning(self, log):
            self.logger.append(log)

    class MockBase:
        def __init__(self, display_logger):
            self._display = MockDisplay()
            if display_logger is not None:
                self._display.logger = display_logger

    class MockLookupModule(LookupModule):
        def __init__(self, display_logger):
            super(MockLookupModule, self).__init__(MockBase(display_logger))
            self.set_options(var_options=None, direct=None)

    # test with missing setting in config.
    # config should not have a setting with key 'InvalidName'
    # invalid name to config will throw exception

# Generated at 2022-06-13 13:19:39.117566
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Dict for global config settings
    class _Constants:
        DEFAULT_REMOTE_TMP = '/tmp/ansible'
        DEFAULT_ROLES_PATH = ['~/.ansible/roles', '/usr/share/ansible/roles']

    terms = ['DEFAULT_REMOTE_TMP', 'DEFAULT_ROLES_PATH', 'remote_tmp', 'port']
    plugin_name = 'ssh'
    plugin_type = 'connection'

    # Patch loader module to overwrite get method
    def get(self, pname, class_only=False):
        return None

    class _Loader:
        def get(self, pname, class_only=False):
            return None

    l = _Loader()
    l.get = get
    plugin_loader.connection_loader = l

    # Create instance

# Generated at 2022-06-13 13:19:53.014388
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:19:53.371300
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:20:03.350461
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import cache_loader
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.loader import cliconf_loader
    from ansible.plugins.loader import httpapi_loader 
    from ansible.plugins.loader import inventory_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import netconf_loader
    from ansible.plugins.loader import shell_loader
    from ansible.plugins.loader import vars_loader

    lm = LookupModule()


# Generated at 2022-06-13 13:20:09.718511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global LookupBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.sentinel import Sentinel
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class FakeVarsManager:
        def __init__(self):
            self.vars = dict()

        def set_variable(self, key, value):
            self.vars[key] = value

        def get_vars(self, play=None, task=None, host=None, include_hostvars=True):
            return self.vars

    class FakePlay:
        def __init__(self, name, vars_manager):
            self

# Generated at 2022-06-13 13:20:20.628685
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._display = display = mock.Mock()
    plugin_type = 'connection'
    plugin_name = 'local'
    terms = [
        'HOST_KEY_CHECKING',
    ]
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(terms, plugin_type=plugin_type, plugin_name=plugin_name)
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(terms, plugin_type=plugin_type)
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(terms, plugin_name=plugin_name)

# Generated at 2022-06-13 13:20:28.560725
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an object of class LookupModule
    lk = LookupModule()

    # 1. Missing parameter 'terms'.
    # Uncomment the statement below to test i.e.,
    # terms = None
    # If missing parameter, then error will be raised.
    # Expected output: Missing required argument: terms
    lk.run(terms)

    # 2. Terms is not a string.
    # Uncomment the statement below to test i.e.,
    # terms = 123
    # Then error will be raised.
    # Expected output: Invalid setting identifier, "123" is not a string, its a <class 'int'>
    lk.run(terms)

    # 3. Terms are not in the configuration.
    # Uncomment the statement below to test i.e.,
    # terms = "XYZ"
    # Then error will

# Generated at 2022-06-13 13:20:38.156731
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    arv = {'plugin_type': 'connection', 'plugin_name': 'local'}
    lookupMObj = LookupModule()
    lookupMObj._display.warning = lambda a: True
    assert lookupMObj.run(['accelerate'], arv) == []
    lookupMObj.set_options(var_options=None, direct=arv)
    assert lookupMObj.run(['accelerate'], arv) == []

# Generated at 2022-06-13 13:20:39.672936
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.run(None, ['foo'])

# Generated at 2022-06-13 13:21:13.558357
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    plugin = LookupModule()
    plugin._display = DummyDisplay()
    variables = {
        'inventory_dir': '.',
        'playbook_dir': '.'
    }
    value = plugin.run(terms=['DEFAULT_ROLES_PATH'], variables=variables)
    assert value == ['roles/'], value



# Generated at 2022-06-13 13:21:16.493845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run(['ANSIBLE_LOG_PATH'])
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], str)

# Generated at 2022-06-13 13:21:27.169208
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global C
    C = type('', (), {'DEFAULT_REMOTE_TMP': 'blabla'})()

    value = _get_global_config('DEFAULT_REMOTE_TMP')
    assert value == 'blabla'

    value = _get_global_config('DEFAULT_REMOTE_TM')
    empty = []
    assert value == empty

    value = _get_global_config('DEFAULT_REMOTE_TM', 'skip')
    assert value == empty

    value = _get_global_config('DEFAULT_REMOTE_TM', 'warn')
    assert value == empty

    value = _get_global_config('DEFAULT_REMOTE_TM', 'error')
    assert value == empty



# Generated at 2022-06-13 13:21:34.528191
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {"ansible_ssh_port": 123}
    global_config = LookupModule()
    plugin_config = LookupModule()

    assert global_config.run(["unknown_val"]) == [None]
    assert global_config.run(["unknown_val"], variables=variables) == [None]
    assert global_config.run(["ansible_ssh_port"], variables=variables) == [123]
    assert global_config.run(["ansible_ssh_port", "unknown_val"], variables=variables) == [123, None]
    assert global_config.run(["ansible_ssh_port", "unknown_val"], variables=variables, on_missing="warn") == [123, None]

# Generated at 2022-06-13 13:21:44.326493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.constants as C
    C.DEFAULT_ROLES_PATH = ['1', '2', '3']

    lookup_module = LookupModule()
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']
    lookup_module.set_loader(None)
    assert lookup_module.run(terms) == [u'default_become_user', ['1', '2', '3']]

    args = dict(plugin_type='shell', plugin_name='sh')
    terms = ['remote_tmp']
    lookup_module.set_loader(None)
    assert lookup_module.run(terms, **args) == [u'~/.ansible/tmp']

# Generated at 2022-06-13 13:21:53.729929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['remote_tmp']
    variables = {}
    kwargs = {'plugin_type': 'shell', 'plugin_name': 'sh'}
    result = lookup_module.run(terms, variables, **kwargs)
    assert result == [u'/tmp/ansible-${USER}']

    lookup_module = LookupModule()
    terms = ['remote_tmp', 'host_key_auto_add']
    variables = {}
    kwargs = {'plugin_type': 'shell', 'plugin_name': 'sh'}
    result = lookup_module.run(terms, variables, **kwargs)
    assert result == [u'/tmp/ansible-${USER}', True]

    lookup_module = LookupModule()

# Generated at 2022-06-13 13:22:02.517056
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __main__
    import ansible.constants as C

    __main__.__dict__.update({
        'constants': C,
        '__file__': __file__,
    })
    lookup_plugin = LookupModule()
    terms = ['DEFAULT_ROLES_PATH']
    try:
        result = lookup_plugin.run(terms, variables=None)
    except Exception as e:
        result = "Unable to run lookup_plugin.run() for terms %s and variables %s: %s" % (terms, variables, e)
    assert result[0] == lookup_plugin._AnsibleDefaults__roles_path

# Generated at 2022-06-13 13:22:05.368717
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test function run of class LookupModule
    try:
        l = LookupModule()
        l.run('DEFAULT_BECOME_USER')
        assert True
    except Exception as e:
        assert False
    else:
        assert False

# Generated at 2022-06-13 13:22:13.617024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This test is useful to avoid regression on mentioned class.
    """
    args = dict(
        terms=["remote_user"],
        on_missing='error',
    )
    look = LookupModule()
    look.set_options(var_options=dict(), direct=args)
    res = look.run([])
    assert(len(res) == 0)
    res = look.run(["remote_user"])
    assert(len(res) == 1)
    assert(res[0] == "root")
    res = look.run(["remote_user", "port"])
    assert(len(res) == 2)
    assert(res[0] == "root")
    assert(res[1] == 22)

# Generated at 2022-06-13 13:22:19.680795
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    #C.DEFAULT_MODULE_NAME = 'script'

    # No exception raised
    lookup_module.run(terms=['DEFAULT_MODULE_NAME'], variables={})

    # No exception raised
    lookup_module.run(terms=['DEFAULT_MODULE_NAME'], variables={'DEFAULT_MODULE_NAME': 'command'})

    # No exception raised
    lookup_module.run(terms=['DEFAULT_MODULE_NAME'], variables={'DEFAULT_MODULE_NAME': 'script'})

    # No exception raised
    lookup_module.run(terms=['DEFAULT_MODULE_NAME'], variables={'DEFAULT_MODULE_NAME': 'shell'})


    # No exception raised

# Generated at 2022-06-13 13:23:27.894411
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # Test with simple value
    terms = ["DEFAULT_BECOME_USER"]
    module.run(terms)
    # Test with list as input
    terms = ["DEFAULT_ROLES_PATH"]
    results = module.run(terms, wantlist=True)
    if results == None or len(results) != 1:
        print("ERROR: Expected results to be an array with 1 value but was %s" % results)
    # Test with default values
    terms = ["UNKNOWN_VAL"]
    results = module.run(terms, on_missing="skip")
    if results != None:
        print("ERROR: Expected results to be None but was %s" % results)



# Generated at 2022-06-13 13:23:43.120915
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.removed import removed_module
    from ansible.module_utils.common.collections import ImmutableDict

    # Ensure code calling removed/renamed code fails
    with pytest.raises(AnsibleError):
        removed_module('ansible.plugins.lookup.config')

    config = LookupModule()
    assert isinstance(config.run('DEFAULT_BECOME_USER', {}), list)

    # Test valid plugin name and type
    plugin_name = 'ssh'
    plugin_type = 'connection'

    # Test missing plugin_name but valid plugin_type
    with pytest.raises(AnsibleOptionsError):
        config.run('port', dict(plugin_type=plugin_type))

    # Test missing plugin_type but plugin_name

# Generated at 2022-06-13 13:23:54.903589
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config_results = {
        "DEFAULT_REMOTE_USER": "sammy",
        "REMOTE_PORT": 22,
        "REMOTE_TMP": "/tmp"
    }

    def _get_plugin_config(pname, ptype, config, variables):
        return config_results[config]

    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    vars = VariableManager()
    vars.extra_vars = {'test_var': 'VAR1'}
    loader = DataLoader()
    lookup = LookupModule()
    lookup.set_loader(loader)
    lookup.set_vars(vars)


# Generated at 2022-06-13 13:24:03.927073
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import integer_types
    from ansible.module_utils.network.common.utils import transform_commands, transform_complex_args
    result = LookupModule().run(['DEFAULT_CONNECTION'], ImmutableDict({'ANSIBLE_CONFIG': 'config'}), False,
                                on_missing='error', plugin_type=None, plugin_name=None, _ansible_check_mode=True,
                                _ansible_debug=True, _ansible_diff=False, _ansible_verbosity=3)
    assert result == ['smart']


# Generated at 2022-06-13 13:24:15.292728
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import pytest

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    play_context = PlayContext()
    host = Host(name='localhost')
    group = Group(name='group')
    group.add_host(host)
    inventory.add_group(group)
    inventory.add_host(host)
    variable_manager.set_inventory(inventory)

    lm = LookupModule()

# Generated at 2022-06-13 13:24:28.236384
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._display = DummyDisplay()
    assert lookup.run(["DEFAULT_REMOTE_TMP"]) == [u'/tmp/ansible-${USER}']


# Generated at 2022-06-13 13:24:37.738660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    m = LookupModule()
    assert m.run([]) == []
    assert m.run(['invalid_param']) == []
    assert m.run(['open_basedir']) == ['True']
    assert m.run(['open_basedir', 'invalid_param']) == ['True']
    assert m.run(['open_basedir', 'open_basedir']) == ['True', 'True']
    assert m.run(['open_basedir', 'open_basedir'], on_missing='error') == ['True', 'True']
    assert m.run(['open_basedir', 'invalid_param'], on_missing='error') == ['True']
    assert m.run(['open_basedir', 'invalid_param'], on_missing='warn') == ['True']
    assert m

# Generated at 2022-06-13 13:24:47.652356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config_terms = {'port': 22, 'display_skipped_hosts': True}
    remote_user = "root"
    # return config_terms
    assert LookupModule().run(config_terms) == config_terms
    # look up the default remote_user and port for ssh connection
    assert LookupModule().run(['remote_user', 'port'], plugin_type="connection", plugin_name="ssh") == [remote_user, config_terms['port']]
    # find the remote_tmp for shell (sh) plugin
    remote_tmp = "/tmp"
    assert LookupModule().run(['remote_tmp'], plugin_type="shell", plugin_name="sh") == [remote_tmp]
    # return default path value if the value of variable config_in_var is not in config

# Generated at 2022-06-13 13:24:54.898268
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Invalid plugin_type and plugin_name in LookupModule
    module = LookupModule()
    result = module.run(terms=['remote_user'], variables={}, plugin_type='connection')
    assert 'Both plugin_type and plugin_name are required, cannot use one without the other' in result['exception'][0]

    module = LookupModule()
    result = module.run(terms=['remote_user'], variables={}, plugin_name='ssh')
    assert 'Both plugin_type and plugin_name are required, cannot use one without the other' in result['exception'][0]

    module = LookupModule()
    result = module.run(terms=['remote_user'], variables={}, plugin_type='connection', plugin_name='ssh')
    assert result['success']

# Generated at 2022-06-13 13:25:06.385261
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Added tests for the following
    # * Lookup module invocation through lookup plugin
    # * Invoking lookup module to read plugin configs
    # * Invoking lookup module to read global configs
    global_config = "DEFAULT_CALLBACK_WHITELIST"
    global_config_value = "yaml,json"
    plugin_config_key = "become_method"
    plugin_config_value = "sudo"
    plugin_type = "become"
    plugin_name = "sudo"
    options = {'plugin_type': plugin_type, 'plugin_name': plugin_name}

    lookup_instance = LookupModule()
    assert(lookup_instance.run([global_config])[0] == global_config_value)