

# Generated at 2022-06-13 13:16:15.650836
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.utils.path import unfrackpath

    base_mod = lookup_loader.get('config')
    mod = base_mod()

    mod.set_options(var_options={'playbook_dir': 'val_playbook_dir'}, direct={})

    # Test 'DEFAULT'
    assert mod.run(['DEFAULT']) == [{}]

    # Test 'DEFAULT_CALLBACK_WHITELIST'
    assert mod.run(['DEFAULT_CALLBACK_WHITELIST']) == [[]]

    # Test 'DEFAULT_BECOME_METHOD'
    assert mod.run(['DEFAULT_BECOME_METHOD']) == ['sudo']

    # Test 'DEFAULT_BECOME_USER'
    assert mod.run

# Generated at 2022-06-13 13:16:21.753892
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # creating instance of class LookupModule
    lookup_obj = LookupModule()
    # create a test dictionary of arguments to pass to run
    arg1 = ['COLOR_OK', 'COLOR_ERROR', 'COLOR_SKIP']
    arg2 = 'COLOR_ERROR'
    result = lookup_obj.run(arg1, arg2, wantlist=True)
    # assert if result is not empty
    assert result

# Generated at 2022-06-13 13:16:28.290092
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case when plugin_type and plugin_name is not specified
    lookup_module = LookupModule()
    # Test case when plugin_type and plugin_name is not specified and on_missing=error
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(terms=['C.DEFAULT_BECOME_USER'], variables=None, on_missing='error')
    # Test case when plugin_type and plugin_name is not specified and on_missing=warn
    with pytest.raises(AnsibleOptionsError):
        lookup_module.run(terms=['C.DEFAULT_BECOME_USER'], variables=None, on_missing='warn')
    # Test case when plugin_type and plugin_name is not specified and on_missing=skip

# Generated at 2022-06-13 13:16:37.797209
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    def get_config_value(config, plugin_type=None, plugin_name=None, variables=None):
        if config == 'DEFAULT_BECOME_USER':
            return 'some_user'
        if config == 'FOO':
            return 'bar'
        if config == 'BOGUS':
            raise C.errors.AnsibleOptionsError('Invalid config (%s)' % config)
        if config == 'UNKNOWN':
            raise C.errors.AnsibleError('Unable to find config (%s)' % config)


# Generated at 2022-06-13 13:16:38.538514
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:16:49.696215
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up test context
    lookup = LookupModule()
    lookup.set_loader(None)

    # Test plugin_type and plugin_name
    with pytest.raises(AnsibleOptionsError):
        lookup.run(["plugin_type", "plugin_name"], plugin_type="xxxx")
    with pytest.raises(AnsibleOptionsError):
        lookup.run(["plugin_type", "plugin_name"], plugin_name="xxxx")

    # Test invalid setting identifier
    with pytest.raises(AnsibleOptionsError):
        lookup.run([None])

    # Test invalid "on_missing" value
    with pytest.raises(AnsibleOptionsError):
        lookup.run(["plugin_type", "plugin_name"], on_missing="Invalid")

    # Test retrieval works with pname and ptype

# Generated at 2022-06-13 13:16:57.445856
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(['DEFAULT_ROLES_PATH'])
    assert result[0] == "/etc/ansible/roles:/usr/share/ansible/roles:/usr/local/share/ansible/roles"

    result = LookupModule().run(['UNKNOWN_CONFIG_VAR'], on_missing='error')
    assert result[0] == "missing settings are required"

    result = LookupModule().run(['UNKNOWN_CONFIG_VAR'], on_missing='warn')
    assert result == []

    result = LookupModule().run(['UNKNOWN_CONFIG_VAR'], on_missing='skip')
    assert result == []

    result = LookupModule().run(['UNKNOWN_CONFIG_VAR'], on_missing='bad')

# Generated at 2022-06-13 13:17:06.256956
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ## Tests for different valid combinations of plugin_type and plugin_name
    # 1. Check valid combination of plugin type and plugin name
    o1 = LookupModule()
    o1.set_options({'plugin_type': 'connection', 'plugin_name': 'ssh'})
    result1 = o1.run(['remote_user', 'port'], variables=None, **{'validate_certs': True})
    assert result1 == ['root', 22]

    # 2. Check valid combination of plugin type and plugin name
    o2 = LookupModule()
    o2.set_options({'plugin_type': 'shell', 'plugin_name': 'sh'})
    result2 = o2.run(['remote_tmp'], variables=None, **{'validate_certs': True})

# Generated at 2022-06-13 13:17:12.477056
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from collections import namedtuple
    from ansible.module_utils.six import PY3, iteritems
    from ansible.module_utils.six.moves import builtins
    from ansible.errors import AnsibleError
    from ansible.plugins.lookup import LookupBase

    Config = namedtuple('Config', 'FLAGS')
    config = Config(FLAGS=namedtuple('FLAGS', 'config_namespace')(config_namespace='ansible_config'))
    lookup = LookupModule(config, None)
    lookup.set_options(var_options=dict(), direct=dict())
    assert lookup.get_option('on_missing') == 'error'  # Default value of option `on_missing` is 'error'
    assert lookup.get_option('plugin_type') is None
    assert lookup.get_

# Generated at 2022-06-13 13:17:13.592454
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Create unit test
    pass

# Generated at 2022-06-13 13:17:26.542793
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    lookup_mock = LookupModule()
    lookup_mock.set_loader(lookup_loader)
    lookup_mock.get_basedir = lambda: '/home/user/ansible'

    assert lookup_mock.run([u'DEFAULT_ROLES_PATH'], variables={}) == [u'/home/user/ansible/roles:/usr/share/ansible/roles']
    assert lookup_mock.run([u'C.DEFAULT_ROLES_PATH'], variables={}) == [u'/home/user/ansible/roles:/usr/share/ansible/roles']

# Generated at 2022-06-13 13:17:35.667917
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockDisplay:

        def __init__(self):
            self.warning_called = False
            self.warned_about_setting = None

        def warning(self, msg):
            self.warning_called = True
            self.warned_about_setting = msg

    class MockAnsiblePluginLoader:

        def connection_loader(self, pname, class_only=False):
            if pname == 'ssh':
                return 'ssh'
            else:
                return None

    class MockAnsiblePlugin:

        def __init__(self, load_name):
            self._load_name = load_name


# Generated at 2022-06-13 13:17:44.068043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    term_list = ['DEFAULT_MODULE_NAME', 'UNKNOWN', 'COLOR_OK', 'COLOR_CHANGED']
    var_options = dict(DEFAULT_MODULE_NAME='ping')
    plugin_name = 'httpapi'
    plugin_type = 'connection'
    on_missing = 'warn'

    # Execute
    lookup_object = LookupModule()
    lookup_object.set_options(var_options=var_options, direct=dict(plugin_name=plugin_name, plugin_type=plugin_type, on_missing=on_missing))
    ret = lookup_object.run(term_list)

    # Test
    assert ret[0] == 'ping'
    assert ret[1] == []
    assert ret[2] == 'green'

# Generated at 2022-06-13 13:17:47.405965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(direct={'plugin_name': 'sh', 'plugin_type': 'shell'})
    assert l.run(['remote_tmp'])[0] == '~/.ansible/tmp'

# Generated at 2022-06-13 13:17:58.592996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Options(object):
        def __init__(self, variables=None, direct=None):
            self.var_options = variables
            self.args = direct

    # create a Mock class for LookupBase
    class Mock(LookupBase):
        def __init__(self):
            pass

        def get_option(self, option):
            if option == 'on_missing':
                return 'error'
            if option == 'plugin_type':
                return 'shell'
            if option == 'plugin_name':
                return 'sh'

    l = LookupModule()
    l.get_option = Mock.get_option
    l.set_options(var_options=None, direct=Options())

    # test the run method
    # 1. missing setting found

# Generated at 2022-06-13 13:18:07.367187
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ansible = __import__('ansible')
    constants = ansible.constants
    setattr(constants, 'HOST_KEY_CHECKING', True)
    setattr(constants, 'NOCOWS', 2)
    setattr(constants, 'DEFAULT_ROLES_PATH', '/etc/ansible/roles')
    setattr(constants, 'DEFAULT_BECOME_USER', 'becomeuser')

    lookup_base = __import__('ansible.plugins.lookup.LookupBase')
    setattr(lookup_base.LookupBase, '_display', Display())
    lookup_base_get_plugin_config = __import__('ansible.plugins.lookup.config._get_plugin_config')

# Generated at 2022-06-13 13:18:13.950381
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']
    kwargs = {}
    result = lookup.run(terms=terms, **kwargs)
    print( result )
    assert result[0] == 'root'
    assert len(result) == 2


# Generated at 2022-06-13 13:18:24.182944
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # For all method run parameters, see following file
    # https://github.com/ansible/ansible/blob/stable-2.9/lib/ansible/plugins/lookup/config.py#L64
    # terms: what we will retreive from ansible.constants
    terms = ['COLLECTION_PATH', 'DEFAULT_ROLES_METADATA_FILE']
    # variables: for this method, we are not using them
    variables = None
    # kwargs:
    kwargs = {}
    kwargs['plugin_type'] = None
    kwargs['plugin_name'] = None
    kwargs['on_missing'] = None
    # Instance class LookupModule
    lm = LookupModule()
    # Result of method run

# Generated at 2022-06-13 13:18:26.972225
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms=['DEFAULT_HOST_LIST']) == ['/etc/ansible/hosts']

# Generated at 2022-06-13 13:18:36.179253
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    # Testing global config settings
    assert lookup_plugin.run(['DEFAULT_BECOME_USER'])[0] == 'root'
    assert lookup_plugin.run(['DEFAULT_SUDO_USER'])[0] == 'root'
    assert lookup_plugin.run(['ANSIBLE_NOCOWS'])[0] is False
    assert lookup_plugin.run(['ANSIBLE_NOCOWS', 'ANSIBLE_DEPRECATION_WARNINGS'])[0] is False
    assert lookup_plugin.run(['ANSIBLE_NOCOWS', 'ANSIBLE_DEPRECATION_WARNINGS'])[1] is True
    assert lookup_plugin.run(['ANSIBLE_NOCOWS', 'ANSIBLE_DEPRECATION_WARNINGS'])[0] is False
    assert lookup

# Generated at 2022-06-13 13:19:00.354468
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('config', class_only=True)

    # Test 'on_missing' option.
    lookup.run(terms=['error'], on_missing='error')
    lookup.run(terms=['error'], on_missing='warn')
    lookup.run(terms=['error'], on_missing='skip')
    with pytest.raises(AnsibleOptionsError):
        lookup.run(terms=['error'], on_missing='nottrue')

    # Test if term is a string.
    with pytest.raises(AnsibleOptionsError):
        lookup.run(terms=['error'], on_missing=False)

    # Test if term is not a string.

# Generated at 2022-06-13 13:19:11.807404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # tests for missing global config setting
    lu = LookupModule()
    result = lu.run(["UNKNOWN_OPTION"], None)
    assert len(result) == 0
    result = lu.run(["UNKNOWN_OPTION"], None, {'on_missing': 'warn'})
    assert len(result) == 0
    result = lu.run(["UNKNOWN_OPTION"], None, {'on_missing': 'error'})
    assert len(result) == 0

    # tests for finding global config setting
    lu = LookupModule()
    result = lu.run(["DEFAULT_ROLES_PATH"], None)
    assert len(result) == 1
    assert result[0] == ['/etc/ansible/roles', '/usr/share/ansible/roles']

    # tests

# Generated at 2022-06-13 13:19:21.864630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakeVars(object):
        def __init__(self, variables):
            self.variables = variables

# Generated at 2022-06-13 13:19:34.715430
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def mock_empty_get_config_value(config, plugin_type=None, plugin_name=None, variables=None):
        return 'Config value'

    def mock_empty_get_config_value_with_callable(config, plugin_type=None, plugin_name=None, variables=None):
        return None

    variables = {'ansible_host': 'host', 'ansible_user': 'user'}
    C.config.get_config_value = mock_empty_get_config_value

    # Test invalid on_missing
    terms = ['FOO', 'BAR']
    try:
        LookupModule().run(terms, variables, on_missing='invalid')
        assert False, 'Should raise AnsibleOptionsError'
    except AnsibleOptionsError:
        pass

    # Test invalid setting identifier

# Generated at 2022-06-13 13:19:44.326424
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LO = LookupModule()
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH', 'RETRY_FILES_SAVE_PATH']
    variables = {'playbook_dir': '.'}
    kwargs = {'on_missing': 'skip'}
    LO.run(terms, variables, **kwargs)
    terms.append('UNKNOWN')    
    kwargs = {'on_missing': 'error'}
    LO.run(terms, variables, **kwargs)


# Generated at 2022-06-13 13:19:55.170350
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:19:57.030664
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    term = 'COLOR_OK'
    ret = lookup.run(terms=term, variables=None, **{})
    assert ret == ['green']

# Generated at 2022-06-13 13:20:04.729372
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.config import LookupModule
    import ansible.config.manager
    configManager = ansible.config.manager.ConfigManager()
    configManager._read_config_data()
    configManager._read_config_file()
    terms = ["DEFAULT_ROLES_PATH","DEFAULT_BECOME_USER"]
    variables = {"ansible_user":"ansible"}
    lookupPlugin = LookupModule(loader=None, variables=variables, configManager=configManager)
    result = lookupPlugin.run(terms)
    assert True == isinstance(result, list) and "~/.ansible/roles" in result and "ansible" in result

# Generated at 2022-06-13 13:20:10.678492
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test sets for class LookupModule
    dict_test = {'x': 1, 'y': 2}
    test_list1 = ['x', 'y']
    test_list2 = [1, 2]

    # Instance creation
    lookup_instance = LookupModule()

    # Test if the result obtained from the method run is equal to the expected result (test_list2)
    assert lookup_instance.run(terms=test_list1, variables=dict_test) == test_list2

    # Test if exception is raised when an unsupported user input is passed to the method run
    with pytest.raises(AnsibleOptionsError, match=r".*Invalid setting identifier.*"):
        lookup_instance.run(terms=test_list1, variables='x')


# Generated at 2022-06-13 13:20:21.116485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test function for ansible.utils.lookup_plugins.config._get_plugin_config method
    '''
    from ansible.utils.lookup_plugins.config import LookupModule
    from ansible.errors import AnsibleOptionsError

    lookup_obj = LookupModule()
    opts = {'on_missing': 'error', 'plugin_type': 'shell', 'plugin_name': 'sh'}
    terms = ['remote_tmp']

    # success
    result = lookup_obj.run(terms=terms, **opts)
    assert result == ['/tmp/ansible-tmp-1561665773.71-273043359752892/']

    # missing on_missing option
    opts = {'plugin_name': 'sh'}

# Generated at 2022-06-13 13:20:56.769123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options({'var_options': {},
                               'direct': {'on_missing': 'error',
                                          'plugin_type': 'shell',
                                          'plugin_name': 'sh'}})
    assert lookup_module.run(['remote_tmp']) == [tempfile.gettempdir()]

# Generated at 2022-06-13 13:21:01.162748
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    test.set_options(dict())
    terms = ['DEFAULT_BECOME_USER']
    actual = test.run(terms)
    expected = ['root']
    assert actual == expected

# Generated at 2022-06-13 13:21:06.159604
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test case: LookupModule.run"""
    #
    # Initialize
    #
    name = 'no_such_config'
    #
    # Exercise
    #
    try:
        C.config.get_config_value(name)
    except AnsibleLookupError as ae:
        assert ae.value == "no setting named '%s'" % name

# Generated at 2022-06-13 13:21:16.694954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Test that call to run method raises RuntimeError if not initialized with set_options
    try:
        lookup.run()
        raise RuntimeError("LookupModule.run method should raise a RuntimeError when initialized without set_options")
    except RuntimeError:
        pass

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    variable_manager.set_host_variable("host", "host")

    # Test with dummy values
    config_dict = {
        "DEFAULT_BECOME_USER": "root",
        "DEFAULT_ROLES_PATH": "roles/",
    }
    config_var = variable_manager.get_vars

# Generated at 2022-06-13 13:21:25.519674
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Test for method 'run' of class 'LookupModule' """

    ## Pre-test setup
    import ansible.plugins
    from ansible.plugins.loader import connection_loader, shell_loader
    from ansible import context
    import os
    import shutil

    # create test specific temp directory
    temp_dir = os.path.realpath('./temp_lookup_plugin')

    # define connection plugin
    connection_plugin_name = 'test_connection'

# Generated at 2022-06-13 13:21:30.631526
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # This is a valid result.
    lookup.run(terms=["DEFAULT_NETWORK_OS"],
               variables=dict(network_os='junos'))
    # This is an invalid result but only a warning is raised,
    # because the default is 'warn'.
    lookup.run(terms=["DEFAULT_PRIVATE_ROLE_VARS"],
               variables=dict(network_os='junos'))

# Generated at 2022-06-13 13:21:37.338757
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    terms = ['DEFAULT_BECOME_USER', 'project']
    ret = LookupModule().run(terms, dict())

    # Assert function returns a list containing the two string values 'root' and 'project'
    assert ret == ['root', 'project']

# Generated at 2022-06-13 13:21:48.264363
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible
    ansible_path = ansible.__path__[0]
    config = ansible_path + "/ansible.cfg"
    module = LookupModule()

    # Ansible Option error
    setattr(module, "_options", dict(plugin_name="test",plugin_type="test"))
    assert_raises(AnsibleOptionsError, module.run, terms=["core"])

    # Missing Setting error
    setattr(module, "_options", dict(plugin_name="test",plugin_type="test"))
    setattr(module, "_display", dict(warning=None))
    setattr(module, "_ds", dict(get_config_value=None))

    setattr(module, "basedir", ansible_path)

# Generated at 2022-06-13 13:21:51.885247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # prepare
    term = 'DEFAULT_REMOTE_USER'
    terms = [term]
    variables = None

    # simulate
    l = LookupModule()
    result = l.run(terms, variables)

    # verify - should raise exception as term is not present
    assert result[0] == 'root'

# Generated at 2022-06-13 13:21:58.372434
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testcase 1: no plugin specified and no config specified, should raise AnsibleLookupError
    l = LookupModule()
    l.set_options()
    l.set_loader()
    term = ["%s"]
    l.run(terms=term, variables=None, **{})
    # Testcase 3: invalid plugin type and name specified, should raise AnsibleLookupError
    variables={"plugin_type":"invalid", "plugin_name":"invalid"}
    term = ["%s"]
    l.run(terms=term, variables=variables, **{})
    # Testcase 4: plugin_type and name specified and config is present, should not raise any error
    C.DEFAULT_ROLES_PATH = "./plugins/roles"
    variables={"plugin_type":"connection", "plugin_name":"local"}


# Generated at 2022-06-13 13:23:01.209791
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()
    assert isinstance(lookup_instance, LookupBase)
    assert isinstance(lookup_instance.run(['DEFAULT_BECOME_USER']), list)
    assert lookup_instance.run(['DEFAULT_BECOME_USER'])[0] == C.DEFAULT_BECOME_USER


# Generated at 2022-06-13 13:23:07.613593
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test with valid config
    results = lookup.run(terms=["DEFAULT_BECOME_USER"])
    assert results[0] == C.DEFAULT_BECOME_USER

    # test lookup of var from inventory
    inventory_vars = {"test_var": "test_var_value"}
    results = lookup.run(terms=["test_var"], variables=inventory_vars)
    assert results[0] == inventory_vars["test_var"]

    try:
        lookup.run(terms=["test_var", "DEFAULT_HOST_LIST", "test_var2"], variables=inventory_vars, on_missing="warn")
    except AssertionError as e:
        raise AnsibleLookupError("Unable to lookup", orig_exc=e)

    # Test

# Generated at 2022-06-13 13:23:12.808173
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pname = "ssh"
    ptype = "connection"
    term = "remote_user"
    plugin_config = _get_plugin_config(pname, ptype, term, None)
    assert plugin_config == 'root'

# Generated at 2022-06-13 13:23:14.107459
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    repr(LookupModule)

# Generated at 2022-06-13 13:23:26.579932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Define some constants
    TERM = 'TERM'
    VALUE = 'xterm'
    # Prepare a mock variable object
    variable = dict()
    variable['TERM'] = VALUE # This is the variable the lookup module is
                             # interested in
    variables = dict()
    variables['vars'] = variable

    # Instantiate module and call run
    lookup_module = LookupModule()
    terms = [TERM]
    ret = lookup_module.run(terms, variables)
    assert ret == [VALUE]

    # Call run with bad on_missing value
    lookup_module = LookupModule()
    terms = [TERM]
    try:
        ret = lookup_module.run(terms, variables, on_missing='foo')
    except AnsibleOptionsError:
        pass
    else:
        raise Ass

# Generated at 2022-06-13 13:23:40.700401
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.values import Value
    from ansible.module_utils.six import PY3

    src = {'DEFAULT_SCREEN_TERM': 'screen', 'DEFAULT_BECOME_USER': 'root'}
    var = {'DEFAULT_BECOME_USER': 'user', 'DEFAULT_SCREEN_TERM': 'xterm'}
    ret = {'DEFAULT_SCREEN_TERM': 'xterm', 'DEFAULT_BECOME_USER': 'user',
           'DEFAULT_DEFAULT_BECOME_USER': 'root', 'DEFAULT_DEFAULT_SCREEN_TERM': 'screen'}
    missing = 'warn'
    lu = LookupModule(src, var)

# Generated at 2022-06-13 13:23:42.342003
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Unit test not implemented"


# Generated at 2022-06-13 13:23:54.609165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.ansible_release import __version__ as release
    from ansible.module_utils.ansible_release import __version__ as ansible_release

    # variables is an optional argument.
    # defining variables as None is a good practice.
    variables = None

    obj = LookupModule()

    # term is a mandatory argument.
    terms = ['config']
    result = obj.run(terms, variables)

# Generated at 2022-06-13 13:24:02.969538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class _Display:
        def warning(self, warning):
            pass

    c = LookupModule(_Display())
    terms = [
        'DEFAULT_BECOME_USER',
        'UNDEFINED_DEFAULT_BECOME_USER'
    ]

    # test on_missing=error
    result = c.run(terms,  dict(), on_missing='error')
    assert result == ['root']

    # test on_missing=warn
    result = c.run(terms,  dict(), on_missing='warn')
    assert result == ['root']

    # test on_missing=error
    result = c.run(terms,  dict(), on_missing='skip')
    assert result == []

# Generated at 2022-06-13 13:24:13.733518
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=None, direct=None)
    result = lookup_module.run(terms=['DEFAULT_RETRY_FILES_ENABLED'], variables=None, **{'on_missing':'error'})
    assert result == [True]

    #verify exception handling
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=None, direct=None)
    try:
        lookup_module.run(terms=['DEFAULT_RETRY_FILES_ENABLED'], variables=None, **{'on_missing':'bad-value'})
        assert False
    except AnsibleOptionsError:
        assert True