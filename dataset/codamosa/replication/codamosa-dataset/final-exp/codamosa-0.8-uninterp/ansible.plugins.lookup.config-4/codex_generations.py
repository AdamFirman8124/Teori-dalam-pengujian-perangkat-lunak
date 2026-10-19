

# Generated at 2022-06-13 13:16:05.843210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module_name = "LookupModule"
    result = LookupModule().run([], [])
    assert result == [], "test_%s_run - failed" % module_name

# Generated at 2022-06-13 13:16:11.662498
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class LookupModule_run_helper:
        def __init__(self, config_file_path, config_file_directory, config_file_name, config_file_content):
            self.config_file_path = config_file_path
            self.config_file_directory = config_file_directory
            self.config_file_name = config_file_name
            self.config_file_content = config_file_content
            self.finish_called = False
            self.default_called = False
            self.files_called = False
            self.raw_called = False
            self.filter_called = False
            self.run_called = False
            self.format_called = False
            self.safe_called = False
            self.present_called = False
            self.path_exists_called = False


# Generated at 2022-06-13 13:16:20.702718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    l.run(["TEST_LIST"])
    l.run(["TEST_LIST"], on_missing='skip')
    l.run(["TEST_LIST"], on_missing='warn')
    l.run(["TEST_LIST", None], on_missing='warn')
    l.run(["TEST_LIST"], on_missing='error')
    l.run(["TEST_LIST", None], on_missing='error')
    l.run(["TEST_LIST"], on_missing='warn')
    l.run(["TEST_LIST"], plugin_type='shell', plugin_name='sh', on_missing='warn')
    l.run(["remote_tmp"], plugin_type='shell', plugin_name='sh', on_missing='warn')

# Generated at 2022-06-13 13:16:28.587723
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    terms = ['DEFAULT_BECOME_USER']

    result = lookup.run(terms, on_missing='skip')

    assert result == ['root'], "Incorrect returned value"

    terms = ['DEFAULT_ROLES_PATH']

    result = lookup.run(terms, on_missing='skip')

    assert result is not None, "Incorrect returned value : null value"

    assert len(result) == 5, "Incorrect returned value"

    terms = ['COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP']

    result = lookup.run(terms, on_missing='skip', wantlist=True)

    assert isinstance(result, list), "Incorrect returned value: term not a list"

    assert len(result) == 3, "Incorrect returned value"


# Generated at 2022-06-13 13:16:37.961503
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.plugins.loader import LookupModuleLoader
    import sys

    # Bypasses colorama import bug for testing on non-Windows
    if sys.platform == 'win32':
        import colorama
        colorama.init()
    sys.stdout = sys.stderr = StringIO()

    # Successful lookup with C.config term
    loader = LookupModuleLoader()
    c = loader.get("config", class_only=True)
    assert c != None
    ret = c.run(["DEFAULT_ROLES_PATH"], variables=dict())
    assert ret[0] == C.DEFAULT_ROLES_PATH

# Generated at 2022-06-13 13:16:44.657994
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_options(direct={'on_missing':'error', 'plugin_type':'shell', 'plugin_name':'sh'})
    rc = lookup.run(terms=['config_file', 'remote_tmp'], variables={'config_file':'/home/roger/test.cfg'})
    assert rc == ['/home/roger/test.cfg', '/tmp'], rc
    return rc

# Generated at 2022-06-13 13:16:53.561662
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    hostvars = {
        'inventory_hostname': 'testhost',
        'ansible_host': 'testhost.example.org',
        'ansible_connection': 'ssh',
    }
    config = {'on_missing': 'error'}
    args = {'terms': ['DEFAULT_REMOTE_USER', 'remote_tmp'],
            'variables': hostvars, 'plugin_type': 'shell',
            'plugin_name': 'sh'}
    terms = args['terms']
    variables = args['variables']
    ptype = args['plugin_type']
    pname = args['plugin_name']
    missing = config.get('on_missing', 'error')
    ret = []
    for term in terms:
        if not isinstance(term, string_types):
            raise AnsibleOptions

# Generated at 2022-06-13 13:17:00.073456
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options()
    l._display = DummyDisplay()
    # both plugin_type and plugin_name must be specified
    assert_raises_AnsibleOptionsError(l, 'config', 'KEYWORD_CONSTANT', plugin_type='anything')
    # unknown plugin_type
    assert_raises_AnsibleOptionsError(l, 'config', 'KEYWORD_CONSTANT', plugin_type='foo', plugin_name='whatever')
    # unknown plugin_name with known plugin type
    assert_raises_AnsibleLookupError(l, 'config', 'KEYWORD_CONSTANT', plugin_type='connection', plugin_name='foobar')
    # invalid setting

# Generated at 2022-06-13 13:17:02.210818
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["COLOR_OK"]
    result = LookupModule().run(terms, variables={})
    assert result == ['green']

# Generated at 2022-06-13 13:17:14.171925
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    terms_list = []
    terms_list.append('DEFAULT_ROLES_PATH')
    terms_list.append('DEFAULT_BECOME_USER')

    try:
        result = lookup_module.run(terms_list)
    except AnsibleOptionsError as e:
        print('Error caught : ' + to_native(e))

    terms_list = []
    terms_list.append('DEFAULT_ROLES_PATH')
    terms_list.append('DEFAULT_BECOME_USER')
    terms_list.append('unknown')

    try:
        result = lookup_module.run(terms_list)
    except AnsibleLookupError as e:
        print('Error caught : ' + to_native(e))

# Generated at 2022-06-13 13:17:34.407918
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm._display = FakeDisplay()
    lm.set_options(direct={'on_missing': 'skip'})

    # test that a config var is found
    result = lm.run(['DEFAULT_ROLES_PATH'])
    assert result == [C.DEFAULT_ROLES_PATH]

    # test that an error is raised when a config var is not found
    try:
        lm.run(['UNKNOWN_VAR'])
        assert False, 'AnsibleLookupError not raised'
    except AnsibleLookupError as e:
        assert 'Unable to find setting UNKNOWN_VAR' in to_native(e)

    # test that a config var can be skipped if not found

# Generated at 2022-06-13 13:17:36.478396
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.config import LookupModule
    lookup = LookupModule()
    ret = lookup.run([])
    assert [] == ret


# Generated at 2022-06-13 13:17:44.676064
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins import lookup_loader

    lookup = lookup_loader.get('config')

    #######################################################
    # Test lookups with missing values
    #######################################################

    # Case 1: on_missing = error (default)
    # Lookup single missing config
    try:
        lookup.run(
            terms=['TEST_MISSING'],
            variables=ImmutableDict(ansible_user='test')
        )
    except AnsibleLookupError as e:
        assert e.orig_exc.args[0] == 'Unable to find setting TEST_MISSING'

    # Case 2: on_missing = warn
    # Lookup multiple missing configs

# Generated at 2022-06-13 13:17:55.900310
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up a fake LookupModule
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.lookup.config import LookupModule

    class FakeLookupModule(LookupModule):
        def __init__(self, terms, **kwargs):
            self.variables = {
                'ansible_connection': 'local',
            }
            self.params = {
                'plugin_name': 'local_action',
            }
            self.params.update(kwargs)
            self.terms = terms

    sentinel = object()

    # Mock out the _get_plugin_config() method, so that we can look at the parameters
    # and return a dummy value
    LookupModule._get_plugin_config = lambda self, pname, ptype, config, variables: sentinel

# Generated at 2022-06-13 13:18:04.238316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = LookupModule()

    # test for missing on_missing options
    try:
        result = t.run([])
    except AnsibleOptionsError as e:
        assert "on_missing" in str(e)

    # test for on_missing as a string and one of 'error', 'warn' or 'skip'
    try:
        result = t.run([], on_missing="missing")
    except AnsibleOptionsError as e:
        assert "on_missing" in str(e)

    # test for invalid setting identifier
    try:
        result = t.run(["*^&&^%$"], on_missing="error")
    except AnsibleLookupError as e:
        assert "Invalid setting identifier" in str(e)

    # test for plugin_name and plugin_type options

# Generated at 2022-06-13 13:18:14.955276
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockContext():
        def __init__(self):
            self.display = None

    class MockConstant():
        def __init__(self):
            self.DEFAULT_UNDEFINED_VAR_BEHAVIOR = None
            self.host_key_checking = None
            self.DEFAULT_STDOUT_CALLBACK = None
            self.DEFAULT_CACHE_PLUGIN = None

    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    mock_global_constant = MockConstant()

    builtins.__dict__['C'] = mock_global_constant

    mock_context = MockContext()
    mock_context.display = "msg"
    lookup_plugin = LookupModule()
    lookup_plugin.set_loader(None)
   

# Generated at 2022-06-13 13:18:21.800247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['remote_user']
    assert lookup_module.run(terms)[0] == C.REMOTE_USER
    terms = ['DEFAULT_BECOME_USER']
    assert lookup_module.run(terms)[0] == C.DEFAULT_BECOME_USER
    terms = ['foo']
    try:
        lookup_module.run(terms)
    except AnsibleLookupError:
        pass
    else:
        assert False, 'AnsibleLookupError not raised'


# Generated at 2022-06-13 13:18:31.217483
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    ansible_config = '{"DEFAULT_ROLES_PATH": "some/path", "remote_user": "ansible", "COLOR_OK": "\u001b[32m", "COLOR_CHANGED": "\u001b[34m", "COLOR_SKIP": "\u001b[36m", "DEFAULT_BECOME_USER": "root"}'
    terms = ["DEFAULT_ROLES_PATH", "DEFAULT_BECOME_USER", "remote_user", "COLOR_OK", "COLOR_CHANGED", "COLOR_SKIP", "UNKNOWN_PARAMTER"]
    for term in terms:
        assert lookup.run([term]) == [ansible_config.get(term)]

# Generated at 2022-06-13 13:18:38.122043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_ROLES_PATH']
    variables = None
    kwargs = None
    C.DEFAULT_ROLES_PATH = 'default_roles_path'
    l = LookupModule()
    result = l.run(terms=terms, variables=variables, **kwargs)
    assert result == ['default_roles_path']

# Generated at 2022-06-13 13:18:38.696846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:18:55.104130
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  # to run this test comment out the following line
  return
  t = LookupModule()
  t.run("DEFAULT_BECOME_USER")

# Generated at 2022-06-13 13:19:01.110356
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    _test = LookupModule()

    # test for plugin names and plugin type
    result = _test.run(terms=['remote_tmp'], plugin_name='sh', plugin_type='shell', variables={})
    assert result == ['/tmp']

    # test for caching
    result = _test.run(terms=['action_plugins'], plugin_name='sh', plugin_type='shell', variables={})
    assert result == ['~/.ansible/plugins/action']

# Generated at 2022-06-13 13:19:07.213494
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    call_args_list = [
        ({'terms': ['host_key_checking']},),
        ({'terms': ['host_key_checking'], 'plugin_type': 'connection', 'plugin_name': 'local'},),
        ({'terms': ['host_key_checking'], 'plugin_type': 'connection', 'plugin_name': 'ssh'},),
    ]
    for call_args in call_args_list:
        assert lookup_module.run(*call_args)

# Generated at 2022-06-13 13:19:17.150820
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.lookup import get_lookup_plugin_class
    from ansible.errors import AnsibleLookupError
    from ansible.utils.sentinel import Sentinel
    lookup_loader.args = ['config', get_lookup_plugin_class('config'), {}]
    cfg = LookupModule()
    result = []
    try:
        result = cfg.run(['DEFAULT_BECOME_USER'])
    except AnsibleLookupError:
        result = []
    assert result == [C.DEFAULT_BECOME_USER]
    result = []

# Generated at 2022-06-13 13:19:25.147296
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    direct = dict(plugin_type='shell', plugin_name='sh')
    option = dict(var_options={}, direct=direct)
    lookup_module = LookupModule()
    lookup_module.set_options(option)
    assert lookup_module.run('remote_tmp') == getattr(C, 'remote_tmp')
    assert lookup_module.run('remote_tmp', variables={}, **direct) == getattr(C, 'remote_tmp')

# Generated at 2022-06-13 13:19:35.551800
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test global config lookup
    assert lookup.run(['DEFAULT_BECOME_USER']) == [None]
    assert lookup.run(['DEFAULT_BECOME_USER']) != ['root']

    # Test error handling
    try:
        lookup.run([23])
        assert False, "AnsibleOptionsError was not raised"
    except AnsibleOptionsError:
        assert True

    # Test plugin config lookup
    assert lookup.run(['remote_user'], plugin_type="connection", plugin_name="local") == ["local"]

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:19:37.619371
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([]) is None

# Generated at 2022-06-13 13:19:51.494024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    lookup_module = LookupModule()

    try:
        lookup_module.run("test")
    except AnsibleOptionsError as expexted:
        pass
    else:
        raise Exception("Got wrong exception")

    try:
        lookup_module.run("test", plugin_name="test")
    except AnsibleOptionsError as expexted:
        pass
    else:
        raise Exception("Got wrong exception")

    try:
        lookup_module.run("test", plugin_name="test", plugin_type="test")
    except AnsibleError as expexted:
        pass
    else:
        raise Exception("Got wrong exception")


# Generated at 2022-06-13 13:20:01.927840
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    lookup_module = LookupModule()
    lookup_module.set_options()

    # Test 'on_missing = error'
    try:
        lookup_module.run(['UNKNOWN'], variables={}, on_missing='error')
    except AnsibleOptionsError as e:
        assert e.message == 'Invalid setting identifier, "UNKNOWN" is not a string, its a <class \'set\'>'

    try:
        lookup_module.run(['DEFAULT_ROLES_PATH'], variables={}, on_missing='error')
    except AnsibleLookupError as e:
        assert e.orig_exc.message == 'Could not find any roles defined in /usr/local/etc/ansible/roles'

    # Test 'on_missing = warn'

# Generated at 2022-06-13 13:20:02.611275
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False


# Generated at 2022-06-13 13:20:42.084225
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create lookup module object
    lookup = LookupModule()

    # check for exception when "terms" is not of type list or string
    with pytest.raises(AnsibleOptionsError) as e_info:
        lookup.run(terms=10)
        assert 'Invalid settings identifier' in e_info.value

    # check for exception when "terms" is of type string
    with pytest.raises(AnsibleOptionsError) as e_info:
        lookup.run(terms='DEFAULT_BECOME_USER')
        assert 'Invalid settings identifier' in e_info.value

    # check for exception when "terms" is of list of strings

# Generated at 2022-06-13 13:20:49.056714
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup = LookupModule()
    test_lookup.set_options(_terms=["DEFAULT_BECOME_USER","COLOR_OK"], on_missing="error")
    result = test_lookup.run()
    assert(len(result) == 2)
    assert(result[1] == 'ok')

# Generated at 2022-06-13 13:20:50.888091
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.run([])

# Generated at 2022-06-13 13:20:55.481624
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup._get_plugin_config('sh', 'shell', 'executable', variables = None) == '/bin/sh'
    assert lookup._get_global_config('DEFAULT_DEBUG') == False

# Generated at 2022-06-13 13:21:06.940384
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:21:17.275439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock self.get_option
    source = LookupModule()
    source._display = MagicMock()
    source.get_option = MagicMock(return_value="error")
    # Use default plugin_type and plugin_name, do not exist
    # expected: raise AnsibleLookupError
    try:
        source.run(terms=["UNKNOWN_SETTING"], variables={"UNKNOWN_KEY": "123"})
    except AnsibleLookupError as e:
        assert e.message.startswith("Unable to find setting UNKNOWN_SETTING")
    # Use default plugin_type and named plugin_name, exist
    # expected: None
    # This check is skipped if the config is missing

# Generated at 2022-06-13 13:21:26.579718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run(['DEFAULT_ROLES_PATH'])
    assert isinstance(result, list), 'Result type should be list'
    assert len(result) == 1, 'Returned list should have 1 item'
    assert isinstance(result[0], list), 'Returned list item should be list'
    assert len(result[0]) > 0, 'Returned list item should not be empty'
    assert isinstance(result[0][0], string_types), 'Returned list item content should be string'
    assert len(result[0][0]) > 0, 'Returned list item content should not be empty'

# Generated at 2022-06-13 13:21:35.798323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.sentinel import Sentinel
    import ansible.plugins.loader as plugin_loader
    from ansible.utils.display import Display
    display = Display()
    terms = ['term1', 'term2', 'term3', 'term4']
    variables = {}
    ptype = 'shell'
    pname = 'sh'
    options = {'var_options': variables, 'direct': dict(plugin_type=ptype, plugin_name=pname)}
    mod_lookup = LookupModule(loader=None, display=display, options=options)
    terms_len = len(terms)
    terms_itr = iter(terms)
    terms_output = mod_lookup.run(terms)
    for term in terms_output:
        term_expected = next(terms_itr)

# Generated at 2022-06-13 13:21:36.980168
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:21:47.952185
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    input_terms = 'DEFAULT_BECOME_USER'
    input_variables = None
    input_on_missing = 'error'
    input_plugin_type = ''
    input_plugin_name = ''
    expected_output = 'root'

    module_args = dict(
        _terms=input_terms,
        on_missing=input_on_missing,
        plugin_type=input_plugin_type,
        plugin_name=input_plugin_name)
    lm_instance = LookupModule()
    lm_instance.set_loader(None)
    lm_instance.set_options(var_options=input_variables)
    actual_output = lm_instance.run(terms=[input_terms], variables=input_variables, **module_args)

# Generated at 2022-06-13 13:22:51.869683
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest
    from ansible.plugins.loader import get_all_plugin_loaders

    plugins = get_all_plugin_loaders()
    constants_dict = {}
    for name in dir(C):
        if not name.startswith("_"):
            constants_dict[name] = getattr(C, name)

    def test_function(type_, keys, constants_dict):

        class MockAnsibleModule(object):
            def __init__(self, *args, **kwargs):
                self.ansible_facts = {
                    'is_linux': True,
                    'os_family': 'RedHat',
                    'os_name': 'RedHat',
                    'os_distribution': 'RedHat',
                    'ansible_facts_modules': 'core'
                }


# Generated at 2022-06-13 13:22:56.142289
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    variables = {}
    result = lookup_module.run(terms, variables)
    if result[0] != 'root':
        raise Exception('test_LookupModule_run failed')

# Generated at 2022-06-13 13:23:05.480854
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # initializing the required objects to call the run method

    # Values and variables used to call the run method
    terms = ["DEFAULT_BECOME_USER", "DEFAULT_ROLES_PATH", "RETRY_FILES_SAVE_PATH", "COLOR_OK", "COLOR_CHANGED", "COLOR_SKIP", "UNKNOWN",
             "remote_user", "port", "remote_tmp"]
    variables = dict()
    variables['config_in_var'] = 'UNKNOWN'
    variables['q'] = 'DEFAULT_BECOME_USER'
    variables['playbook_dir'] = '.'
    kwargs = dict()
    kwargs['plugin_type'] = 'connection'
    kwargs['plugin_name'] = 'ssh'
    kwargs['on_missing'] = 'error'
   

# Generated at 2022-06-13 13:23:13.725823
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit tests for the LookupModule class
    """

    class CacheModuleMock(LookupBase):
        def __init__(self):
            self._plugin_options = {}
            self.rows = [
                {'basic_key': 1, 'basic_0': 'ok'},
                {'basic_key': 2, 'basic_0': 'ok'},
                {'basic_key': 3, 'basic_0': 'ok'},
                {'basic_key': 4, 'basic_0': 'ok'},
                {'basic_key': 5, 'basic_0': 'ok'},
            ]

        def run(self, terms, variables=None, **kwargs):
            # pylint: disable=unused-argument
            results = []

# Generated at 2022-06-13 13:23:26.454403
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.lookup.config as lookup_config
    import ansible.utils.sentinel as sentinel
    from ansible.plugins.loader import lookup_loader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    lookup_config.__loader__ = lookup_loader
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../../plugins/lookup'))
    lookup_config.init_cache()

    test_terms = ['DEFAULT_BECOME_USER', 'UNKNOWN_TERM']
    test_variables = {'test_variable': True}
    test_kwargs = {'plugin_name': 'ios', 'plugin_type': 'cliconf'}

   

# Generated at 2022-06-13 13:23:40.642555
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.playcontext import PlayContext

    lookup_module = LookupModule()

    options = {'plugin_type': 'connection', 'plugin_name': 'ssh'}
    results = lookup_module.run(terms=['remote_user'], variables={'ansible_ssh_user': 'foo'}, **options)
    assert results[0] == 'foo'

    # test case where a config setting is not set
    options = {'on_missing': 'warn'}
    results = lookup_module.run(terms=['remote_user'], variables={'ansible_ssh_user': 'foo'}, **options)
    assert results == []

    # test

# Generated at 2022-06-13 13:23:50.692924
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assert lookup.run([1], dict()) == []
    assert lookup.run(['foo', 'bar'], dict()) == []
    assert lookup.run(['DEFAULT_BECOME_USER'], dict()) == ['root']
    assert lookup.run(['DEFAULT_BECOME_USER', 'DEFAULT_JINJA2_NATIVE'], dict(), on_missing='warn') == ['root']
    assert lookup.run(['DEFAULT_BECOME_USER', 'DEFAULT_JINJA2_NATIVE'], dict(), on_missing='error') == ['root']
    assert lookup.run(['DEFAULT_BECOME_USER', 'DEFAULT_JINJA2_NATIVE'], dict(), on_missing='skip') == ['root']

# Generated at 2022-06-13 13:24:01.315438
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert isinstance(lookup_module, LookupBase)
    # test value for terms
    terms = ['local_tmp', 'roles_path', 'forks']
    # test value for variables
    variables = dict()
    variables['local_tmp'] = '/temp/'
    variables['roles_path'] = ['/user/username/roles', '/etc/ansible/roles']
    variables['forks'] = 20
    assert lookup_module.run(terms, variables=variables) == ['/temp/', ['/user/username/roles', '/etc/ansible/roles'], 20]
    # test value for terms
    terms = ['remote_tmp', 'roles_path', 'forks']
    # test value for variables
    variables = dict()
    # variables

# Generated at 2022-06-13 13:24:03.840908
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myMM = LookupModule()
    result = myMM.run(terms=[''],context={},variables={},**{'on_missing':'error'})
    assert result == ['']


# Generated at 2022-06-13 13:24:04.765960
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass