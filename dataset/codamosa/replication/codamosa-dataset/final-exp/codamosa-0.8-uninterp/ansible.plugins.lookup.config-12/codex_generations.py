

# Generated at 2022-06-13 13:16:15.965295
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import sys

    class MockDisplay():
        def warning(self, msg):
            print("warning: %s" % msg, file=sys.stderr)

    class MockConfig():
        def __init__(self):
            self.data = {'REMOTE_USER': "test_remote_user", 'RETRY_FILES_SAVE_PATH': "/tmp"}

        def get_config_value(self, value, plugin_type=None, plugin_name=None, variables=None):
            if plugin_name and plugin_type:
                return self.data.get(value, Sentinel)
            else:
                return self.data.get(value, Sentinel)

    class MockPluginLoader():
        def __init__(self, plugin_type):
            self.plugin_type = plugin_type


# Generated at 2022-06-13 13:16:16.960467
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(True)

# Generated at 2022-06-13 13:16:26.325138
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._display.display = lambda msg, color=None, stderr=False, screen_only=False, log_only=False: msg
    lookup_module._display.verbosity = 1
    lookup_module._display.warning = lambda msg, color=None, stderr=False, screen_only=False, log_only=False: msg
    lookup_module.set_options({'var_options': {}, 'direct': {}})

    assert isinstance(lookup_module.run(['DEFAULT_ROLES_PATH'], {}), list)
    assert isinstance(lookup_module.run(['DEFAULT_ROLES_PATH'], {}, on_missing='error'), list)

# Generated at 2022-06-13 13:16:34.767845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["connection", "fake_plugin"]
    variables = "ssh"
    mock_variable = {'ansible_connection':'ssh'}
    expected = [
        "ssh",
        {}
    ]
    lookup = LookupModule()
    description = "Test the method run of class LookupModule"
    with patch.object(C, 'get_config_value', return_value=expected):
        with pytest.raises(AnsibleOptionsError, match="Both plugin_type and plugin_name are required, cannot use one without the other"):
            lookup.run(terms=terms,variables=variables)


# Generated at 2022-06-13 13:16:42.159773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    variables = {'DEFAULT_BECOME_USER': 'root'}
    results = module.run(terms, variables=variables)
    assert len(results) == 1
    assert results[0] == 'root'

    terms = ['UNKNOWN']
    try:
        results = module.run(terms, variables=variables)
    except AnsibleLookupError as e:
        assert e.orig_exc.args[0] == "'UNKNOWN' was not defined"

    results = module.run(terms, variables=variables, on_missing='skip')
    assert len(results) == 0

    terms = ['DEFAULT_BECOME_USER', 'UNKNOWN']

# Generated at 2022-06-13 13:16:52.573329
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Testing with no plugin_type, plugin_name
    terms = ['TEST']
    terms += ['TEST1']
    terms += ['C.DEBUG']
    terms += ['C.PIPELINING']
    terms += ['C.DEFAULT_ROLES_PATH']
    terms += ['C.DEFAULT_CACHE_PLUGIN_TIMEOUT']
    variables = None
    kwargs = dict(on_missing='error')
    kwargs['plugin_type'] = None
    kwargs['plugin_name'] = None

    with pytest.raises(AnsibleLookupError):
        module.run(terms, variables, **kwargs)

    # Testing with plugin_type, plugin_name
    terms = ['TEST']
    terms += ['TEST1']


# Generated at 2022-06-13 13:16:55.071435
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    terms = ['DEFAULT_ROLES_PATH']
    ret = []

    # Act
    lm = LookupModule()
    result = lm.run(terms)

    # Assert
    assert result == ret

# Generated at 2022-06-13 13:16:57.935812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms='DEFAULT_BECOME_USER') == ['root']


# Generated at 2022-06-13 13:17:04.406984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup valid test path
    import os
    test_path = os.getcwd()
    # Test a good lookup
    test_lookup = LookupModule()
    test_lookup.set_options(direct={'plugin_type':'shell', 'plugin_name':'sh'})
    ret = test_lookup.run(["remote_tmp"], variables={"playbook_dir":test_path})
    assert ret[0] == C.DEFAULT_REMOTE_TMP, 'Should be the same file path'
    # Test a bad lookup (bad plugin_type)
    test_lookup.set_options(direct={'plugin_type':'shella', 'plugin_name':'sh'})

# Generated at 2022-06-13 13:17:13.516744
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager
    from ansible.utils import context_objects as co
    from ansible.plugins.loader import plugin_loader, LookupModule

    variable_manager = VariableManager()
    variable_manager.extra_vars['some_config'] = 'This is a test value'

    kw = {
        'plugin_type' : 'lookup',
        'plugin_name' : 'test_lookup',
        'on_missing' : 'error'
        }

    lookup_module = LookupModule()

    result = lookup_module.run(['some_config'], variable_manager, **kw)

    assert result == ['This is a test value']

# Generated at 2022-06-13 13:17:34.407244
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test_global_config():
        lookup_plugin = LookupModule()
        assert lookup_plugin.run(['DEFAULT_ROLES_PATH']) == [C.DEFAULT_ROLES_PATH.split(':')]
        assert lookup_plugin.run(['DEFAULT_ROLES_PATH', 'DEFAULT_MODULE_UTILS_PATH']) == [C.DEFAULT_ROLES_PATH.split(':'), C.DEFAULT_MODULE_UTILS_PATH.split(':')]

    def test_plugin_config():
        lookup_plugin = LookupModule()

# Generated at 2022-06-13 13:17:37.236707
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants

    assert LookupModule.run is not None

    module = LookupModule()
    try:
        result = module.run(['DEFAULT_BECOME_USER'], variables={'inventory_dir': '/some/path'}, direct={'on_missing': 'warn'})
        assert len(result) == 1
        assert result[0] == constants.DEFAULT_BECOME_USER
    except AssertionError:
        raise AssertionError('LookupModule.run() test failed')

# Generated at 2022-06-13 13:17:45.192725
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    lm = LookupModule(loader=loader)
    var_manager = VariableManager()
    var_manager.set_inventory(loader.load_inventory_from_list([host for host in []]))

    assert lm.run(['DEFAULT_BECOME_USER'], variables=var_manager.get_vars()) == ['root']
    assert lm.run(['NON_EXISTENT'], variables=var_manager.get_vars(), on_missing='skip') == []
    assert lm.run(['NON_EXISTENT'], variables=var_manager.get_vars(), on_missing='warn') == []

# Generated at 2022-06-13 13:17:56.537122
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # 3.3 and 3.4 do not support mocking the unittest way
    import sys
    python_version = sys.version_info

    if python_version.major == 2 and python_version.minor == 7:
        import unittest2 as unittest
    else:
        import unittest

    import errno
    import os
    import tempfile

    import yaml

    yaml.warnings({'YAMLLoadWarning': False})
    from ansible import constants as C


# Generated at 2022-06-13 13:18:05.534525
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with invalid plugin type
    terms = ['host_key_checking']
    variables = {}
    kwargs = {}
    lookup_plug = LookupModule()
    with pytest.raises(AnsibleOptionsError):
        lookup_plug.run(terms, variables, plugin_type='bad')

    # Test with invalid plugin name
    with pytest.raises(AnsibleOptionsError):
        lookup_plug.run(terms, variables, plugin_type='connection', plugin_name='bad')

    # Test with invalid on_missing
    with pytest.raises(AnsibleOptionsError):
        lookup_plug.run(terms, variables, on_missing='bad')

# Generated at 2022-06-13 13:18:20.449190
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test if plugin_name and plugin_type are not both present
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=None, direct={'plugin_type': 'shell'})
    terms = ['remote_tmp']
    try:
        lookup_module.run(terms)
    except AnsibleOptionsError as e:
        assert 'Both plugin_type and plugin_name are required, cannot use one without the other' == str(e)
    else:
        assert 'Both plugin_type and plugin_name are required, cannot use one without the other' == ''

    # Test when plugin_name and plugin_type are both present
    lookup_module.set_options(var_options=None, direct={'plugin_name': 'sh', 'plugin_type': 'shell'})
    result = lookup_module.run

# Generated at 2022-06-13 13:18:30.658472
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms=['DEFAULT_BECOME_USER'], variables={}) == [None]
    assert lookup_module.run(terms=['DEFAULT_ROLES_PATH'], variables={}) == [['~/.ansible/roles', '/usr/share/ansible/roles']]
    assert lookup_module.run(terms=['RETRY_FILES_SAVE_PATH'], variables={}) == ['/home/bill/data/ansible_retry']
    assert lookup_module.run(terms=['COLOR_OK'], variables={}) == ['green']
    assert lookup_module.run(terms=['COLOR_CHANGED'], variables={}) == ['yellow']
    assert lookup_module.run(terms=['COLOR_SKIP'], variables={})

# Generated at 2022-06-13 13:18:39.068968
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils import basic
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.sentinel import Sentinel

    class AnsibleOptions(object):
        def __init__(self):
            self.connection = None
            self.module_path = None
            self.forks = None
            self.become = None
            self.become_method = None
            self.become_user = None
            self.check = None
            self.diff = None

    class AnsibleConfig(object):
        def __init__(self):
            self.DEFAULT_SUDO_USER = "ansible"


# Generated at 2022-06-13 13:18:48.415219
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    os.environ['ANSIBLE_DISPLAY_SKIPPED_HOSTS'] = 'false'
    lookup_module = LookupModule()
    terms = ['ANSIBLE_LOG_PATH', 'ANSIBLE_KEEP_REMOTE_FILES', 'ANSIBLE_CALLBACK_WHITELIST']
    result = lookup_module.run(terms=terms, on_missing='skip')
    assert result == ["/tmp/ansible.log", False, []]
    result = lookup_module.run(terms=terms, on_missing='warn')
    assert result == ["/tmp/ansible.log", False, []]

# Generated at 2022-06-13 13:18:51.196626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = LookupModule.run(
        obj=None,
        terms=[
            'DEFAULT_BECOME_USER',
            'UNKNOWN_TERM',
        ],
        variables=None,
        on_missing='warn',
    )
    assert ret == [C.DEFAULT_BECOME_USER]



# Generated at 2022-06-13 13:19:11.086230
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # SetUp
    lookup_module = LookupModule()
    terms = []
    terms.append('DEFAULT_BECOME_METHOD')
    variable = os.environ

    # Because the result of lookup is not fixed, it is not possible for test here.
    # Therefore, test for the exception.
    lookup_module.run(terms, variable)

# Generated at 2022-06-13 13:19:21.547805
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test for invalid term
    lm = LookupModule()
    try:
        lm.run([1234], None)
        assert False, "Invalid term shouldn't be allowed"
    except AnsibleOptionsError:
        pass
    except Exception as e:
        assert False, "Should throw AnsibleOptionsError, not {}".format(e)

    # Test for invalid on_missing arguments
    try:
        lm.run(['foo'], None, on_missing='invalid')
        assert False, "Invalid 'on_missing' argument shouldn't be allowed"
    except AnsibleOptionsError:
        pass
    except Exception as e:
        assert False, "Should throw AnsibleOptionsError, not {}".format(e)

    # Test for missing term in config
    from ansible.config.manager import ConfigManager

# Generated at 2022-06-13 13:19:34.420827
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()    # Create instance of the class LookupModule
    
    # Test config in plugin
    term = 'remote_tmp'
    variables = None
    ptype = 'shell'
    pname = 'sh'
    kwargs = {'plugin_type': ptype, 'plugin_name': pname}
    result = lookup_module.run(terms=[term], variables=variables, **kwargs)
    assert result == ['$HOME/.ansible/tmp']

    # Test global config
    term = 'DEFAULT_ROLES_PATH'
    variables = None
    kwargs = {}
    result = lookup_module.run(terms=[term], variables=variables, **kwargs)
    assert result == ['/etc/ansible/roles:/usr/share/ansible/roles']



# Generated at 2022-06-13 13:19:40.585591
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=missing-docstring
    # pylint: disable=invalid-name
    # pylint: disable=no-name-in-module
    # pylint: disable=organization-imported-from-dynamic-module
    import pytest

    def test_fail(*args, **kwargs):
        # pylint: disable=unused-argument
        import sys
        raise AssertionError("expected pytest to exit")
        sys.exit(1)

    #  ansible.constants.DEFAULT_SYSLOG_FACILITY = environ.get('DEFAULT_SYSLOG_FACILITY', "LOG_USER")
    kwargs = {'environ': {'DEFAULT_SYSLOG_FACILITY': 'LOG_USER'}}

# Generated at 2022-06-13 13:19:41.022763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:19:51.435138
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_module = LookupModule()
    result = test_module.run(terms=[None], variables=None, direct=None)
    assert result is None

    test_module2 = LookupModule()
    try:
        result = test_module2.run(terms=['unknow_word'], variables=None, direct=None)
    except TypeError:
        print('Excepted TypeError')
        result = None
    assert result is None

    test_module3 = LookupModule()
    result = test_module3.run(terms=['DEFAULT_REMOTE_USER'], variables=None, direct=None)
    assert result[0] == 'root'

# Generated at 2022-06-13 13:20:01.885137
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.sentinel import Sentinel

    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    lookup_module.set_environment(None)
    lookup_module._display = None

    # No option is provided
    assert lookup_module.run([]) == []

    # Empty term list is provided
    assert lookup_module.run([], variables={}, on_missing="error") == []
    assert lookup_module.run([], variables={}, on_missing="warn") == []
    assert lookup_module.run([], variables={}, on_missing="skip") == []

    # term contains non-string
    try:
        assert lookup_module.run(['test', None], variables={}, on_missing="error")
    except AnsibleOptionsError:
        pass 

    # on_missing contains invalid

# Generated at 2022-06-13 13:20:08.497371
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a new instance of the LookupModule
    test_instance = LookupModule()
    ############################################################################
    # Basic test, get global configuration value
    ############################################################################
    # Set the test terms
    terms = [ 'DEFAULT_SUDO_USER' ]
    # Create an instance of the ansible.constants class
    test_constants = C
    # Set the current DEFAULT_SUDO_USER
    test_constants.DEFAULT_SUDO_USER = 'test_user'
    # Set the variables class
    test_variables = {}
    # Call the run method
    result = test_instance.run(terms=terms,variables=test_variables)
    # Verify the results
    assert result[0] == 'test_user'
    ############################################################################
    # Basic

# Generated at 2022-06-13 13:20:19.399936
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    res = lookup.run(['DEFAULT_BECOME_USER'], on_missing='skip')
    # print(res)
    res = lookup.run(['DEFAULT_ROLES_PATH'], on_missing='skip')
    # print(res)
    res = lookup.run(['RETRY_FILES_SAVE_PATH'], on_missing='skip')
    # print(res)
    res = lookup.run(['COLOR_OK'], on_missing='skip')
    # print(res)
    res = lookup.run(['COLOR_CHANGED'], on_missing='skip')
    # print(res)
    res = lookup.run(['COLOR_SKIP'], on_missing='skip')
    # print(res)

# Generated at 2022-06-13 13:20:20.956029
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # There is no test_LookupModule_run() unit test
    assert(False)



# Generated at 2022-06-13 13:20:54.192081
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['DEFAULT_ROLES_PATH']
    term = 'DEFAULT_ROLES_PATH'
    setting = [C.DEFAULT_ROLES_PATH]

    assert lookup.run(terms) == setting
    assert lookup.run([term]) == setting

# Generated at 2022-06-13 13:21:06.292601
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit test for module lookup_plugin.config
    :return:
    '''
    # config.py is a module inside "lookups/" directory of the Ansible repository
    # this is the reason for the config module not being a package
    # The class name is LookupModule and the instance used to run tests is "test_"
    # So from an import statement we can import the non package module and the class
    # and then initialize the instance
    from lookup_plugins.config import LookupModule
    test_ = LookupModule()

    print("\n\n\n*****begin test run unit test*******")
    # run method of the LookupModule class needs 2 mandatory arguments
    # 1. term - setting in the ansible configuration file(ansible.cfg) for which value is to be retrieved
    # 2. variables - User defined variables used

# Generated at 2022-06-13 13:21:16.854538
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create an instance of LookupModule
    lookup_module = LookupModule()
    # set a fake value for C.HOST_KEY_CHECKING
    C.HOST_KEY_CHECKING = "False"

    # test with no terms, no options and no variables
    with pytest.raises(AnsibleOptionsError) as e:
        lookup_module.run(terms=[], variables=None, **{})
    assert e.value.args[0] == "No value was passed to lookup for lookup_plugin.config"

    # test with terms and no variables and no options
    terms = ["HOST_KEY_CHECKING"]
    result = lookup_module.run(terms=terms, variables=None, **{})
    assert result[0] == C.HOST_KEY_CHECKING

    # test with a term and options and

# Generated at 2022-06-13 13:21:22.001729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test=LookupModule()
    test.set_options(var_options=['port', '-m', 'ssh'])
    test.set_options(direct=['plugin_type', 'plugin_name'])
    assert test.run('remote_user') == ['root']

# Generated at 2022-06-13 13:21:31.417011
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:21:37.486317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_list = ['DEFAULT_ROLES_PATH']
    test_variables = {'playbook_dir': '/path/to/playbook'}
    lookup_obj = LookupModule()
    assert lookup_obj.run(test_list, test_variables, 'warn') == ['../../../roles']

# Generated at 2022-06-13 13:21:38.903546
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "something"

# Generated at 2022-06-13 13:21:49.420797
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader
    ansible.plugins.loader.find_plugin_filepaths = lambda *args, **kwargs: []
    import os

    # Fake the global config, add class vars to the global config
    c = os.path.dirname(os.path.realpath(__file__))
    os.environ['ANSIBLE_CONFIG'] = os.path.join(c, "ansible.cfg.test")
    C.load_config_file()

    # Add needed variables to the environment
    os.environ['TEST_LOOKUP_MODULE_1'] = 'MEGA'
    os.environ['TEST_LOOKUP_MODULE_2'] = 'YOLO'
    os.environ['TEST_LOOKUP_MODULE_3'] = 'MAGIC'



# Generated at 2022-06-13 13:21:56.225928
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        'DEFAULT_BECOME_USER',
        'UNDEFINED_TERM'
    ]
    variables = {
        'inventory_dir': '/path/to/inventory',
        'playbook_dir': '/path/to/playbook',
        'private_key_file': '/path/to/key',
        'roles_path': '/path/to/roles',
        'vault_password_file': '/path/to/vault'
    }
    expected = [
        str(C.DEFAULT_BECOME_USER)
    ]
    lookup_obj = LookupModule()
    result = lookup_obj.run(terms, variables=variables, wantlist=True)
    assert result == expected


# Generated at 2022-06-13 13:22:07.486719
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myLookupModule = LookupModule()
    # Test that setting the plugin_type and plugin_name correctly will
    # return the correct value
    # Test that other method calls that use the plugin_type and plugin_name
    # setters will return correct value.
    ret = myLookupModule.run(terms=['_ansible_tmpdir'], plugin_type='shell', plugin_name='sh')
    assert ret[0] == '$HOME/.ansible/tmp'
    ret = myLookupModule.run(terms=['_ansible_tmpdir', '_ansible_keep_remote_files'], plugin_type='shell', plugin_name='sh')
    assert ret[0] == '$HOME/.ansible/tmp'
    assert ret[1] is False
    # Test that a single term is returned
    ret = myLook

# Generated at 2022-06-13 13:23:13.069709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_options({'on_missing': 'warn'})
    assert lookup.run(['C', 'DEFAULT_ROLES_PATH'], None) == [C.DEFAULT_ROLES_PATH]
    assert lookup.run(['C', 'DEFAULT_ROLES_PATH'], {'DEFAULT_ROLES_PATH': '/tmp'}) == ['/tmp', C.DEFAULT_ROLES_PATH]

    lookup.set_options({'plugin_type': 'vars', 'plugin_name': 'extra_vars'})
    assert lookup.run(['CACHEDIR'], {'CACHEDIR': '/tmp', 'C': 'C'}) == ['/tmp']


# Generated at 2022-06-13 13:23:17.046794
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''
    lookup_module = LookupModule()
    assert lookup_module.run(['DEFAULT_BECOME_USER']) == ['root']

# Generated at 2022-06-13 13:23:27.635993
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils._text import to_bytes
    import sys

    class MockPluginLoader(object):
        def connection_loader(*args, **kwargs):
            return True

    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.params['plugin_name'] = 'ssh'
            self.params['plugin_type'] = 'connection'
            self.params['on_missing'] = 'skip'

        def fail_json(*args, **kwargs):
            raise Exception('fail_json')

        def display(self, msg, color=None):
            pass

    class MockSentinel(object):
        def __init__(self):
            self.value = 'MY_SENTINEL_VALUE'
            self

# Generated at 2022-06-13 13:23:36.183671
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    list_of_configs = ['DEFAULT_HOST_LIST', 'DEFAULT_SUBSET', 'DEFAULT_VAULT_ID_MATCH']
    terms = {'ansible_configs': list_of_configs}
    configs = module.run(terms['ansible_configs'])
    assert (configs[0] == '/etc/ansible/hosts')
    assert (configs[1] == '')
    assert (configs[2] == None)

# Generated at 2022-06-13 13:23:47.994965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    loader = plugin_loader.action_loader
    action_plugin_pname = 'assert'
    action_plugin = loader.get(action_plugin_pname)

    test_terms = dict()
    test_terms['DEFAULT_ASSERT'] = (None, None, 'assert', 'DEFAULT_ASSERT', None, action_plugin.DEFAULT_ASSERT)
    test_terms['DEFAULT_ASSERT'] = (Sentinel(), None, 'assert', 'DEFAULT_ASSERT', None, action_plugin.DEFAULT_ASSERT)
    test_terms['DEFAULT_ASSERT'] = (Sentinel(), None, 'assert', 'DEFAULT_ASSERT', None, action_plugin.DEFAULT_ASSERT)

# Generated at 2022-06-13 13:23:55.917943
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    import shutil
    import filecmp

    tmp_dir = tempfile.mkdtemp(prefix='ansible_test_config')


# Generated at 2022-06-13 13:24:05.068356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    import copy
    from ansible.parsing.plugin_docs import read_docstring


# Generated at 2022-06-13 13:24:15.990946
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins
    lookup_plugin = LookupModule()
    # Test Cases
    # with plugin_name and plugin_type
    terms = ['remote_tmp']
    options = {'plugin_name': 'sh', 'plugin_type': 'shell'}
    assert _get_global_config(terms[0]) == lookup_plugin.run(terms, **options)
    assert isinstance(_get_global_config(terms[0]), string_types)
    # with plugin_name and plugin_type
    options = {'plugin_name': 'sh', 'plugin_type': 'shell', 'on_missing': 'skip'}
    assert _get_global_config(terms[0]) == lookup_plugin.run(terms, **options)
    assert isinstance(_get_global_config(terms[0]), string_types)
    #

# Generated at 2022-06-13 13:24:28.817667
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock class LookupModule
    class LookupModule():
        class config():
            class DEFAULT_ROLES_PATH():
                pass
            class DEFAULT_BECOME_USER():
                pass
            class UNKNOWN():
                pass
            class RETRY_FILES_SAVE_PATH():
                pass
            class COLOR_OK():
                pass
            class COLOR_CHANGED():
                pass
            class COLOR_SKIP():
                pass
            class remote_user():
                pass
            class port():
                pass
            class remote_tmp():
                pass

    import ansible.plugins.loader as plugin_loader

    class plugins_loader():
        class connection_loader:
            def get(pname, class_only=True):
                class connection_class:
                    _load_name = 'ssh'
               

# Generated at 2022-06-13 13:24:38.002100
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    with pytest.raises(AnsibleOptionsError) as excinfo:
        result = LookupBase().run()
    assert "Unrecognized option" in str(excinfo.value)  # Test if _terms is required

    with pytest.raises(AnsibleOptionsError) as excinfo:
        result = LookupModule().run(["host_key_checking", "on_missing=bad"],
                                    dict(host_key_checking=True))
    assert "Invalid value" in str(excinfo.value)  # Test if on_missing is set correctly

    # Test if DEFAULT_ROLES_PATHS is saved correctly
    result = LookupModule().run(["DEFAULT_ROLES_PATH"], dict(DEFAULT_ROLES_PATH=True))
    assert result
