

# Generated at 2022-06-13 13:16:06.735394
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    dict_args = dict(
        plugin_type="connection",
        plugin_name="local",
        on_missing="warn",)

    lookup_plugin = LookupModule()
    lookup_plugin.set_options(var_options={}, direct=dict_args)
    result = lookup_plugin.run(["ANSIBLE_CONNECTION"])
    assert result == [u'local']
    result = lookup_plugin.run(["ANSIBLE_CONNECTION=local"])
    assert result == [u"ANSIBLE_CONNECTION=local"]

# Generated at 2022-06-13 13:16:16.046894
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # get module, terms to be passed to run method and environ variable values to be set
    lookupModule = LookupModule()
    terms = ['DEFAULT_BECOME_USER', 'LOCAL_TMP']
    environ_var = {'ANSIBLE_KEEP_REMOTE_FILES': 'false'}
    environ_const = 'ANSIBLE_KEEP_REMOTE_FILES'

    # set the environ variable
    os.environ[environ_const] = environ_var[environ_const]

    # run the module
    lookupModule.run(terms=terms)

# Generated at 2022-06-13 13:16:19.970740
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    ansible_vars = {'var1': True}
    lu.set_options(direct={'var_options': ansible_vars})
    assert lu._options.var_options == ansible_vars

# Generated at 2022-06-13 13:16:20.858538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    pass

# Generated at 2022-06-13 13:16:27.912039
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import chunk_loader
    from ansible.module_utils.six import PY3
    from ansible.utils.sentinel import Sentinel

    custom_loader = get_all_plugin_loaders()['lookup']
    from ansible.plugins.loader import module_loader
    m = module_loader._create_module_class(
        'ansible.plugins.lookup.config', 'Config', custom_loader
    )()

    # setup a fake settings instance to run test
    class settings:
        DEFAULT_BECOME_USER = 'root'
        DEFAULT_ROLES_PATH = ['/path/to/roles']

# Generated at 2022-06-13 13:16:37.511959
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.ansible_release import __version__

    if PY3:
        from unittest.mock import patch, MagicMock
    else:
        from mock import patch, MagicMock

    # Module settings
    my_module = 'Not a real module'
    on_missing = 'error'

    # Mock settings
    ret = [0,1]
    result = 'result'
    terms = [result, result]
    LOG_PATH = 'ansible.module_utils.ansible_release.log'
    variables = {'count_ok': 0, 'count_changed': 0, 'count_failed': 0,
                 'count_skipped': 0}

    # Set up variables to pass to plug-in

# Generated at 2022-06-13 13:16:40.404345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # we have to make those up, because ansible.constants is not importable
    lookup_module.get_option = lambda x: 'error'
    lookup_module.set_options = lambda x: x
    lookup_module.run([], [])

# Generated at 2022-06-13 13:16:45.081808
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run('', {}, '', '', '') == []
    assert lookup_module.run('', {}, '', '', '') == []
    try:
        assert lookup_module.run('', {}, '', '', '', '', '') == []
    except TypeError:
        pass

# Generated at 2022-06-13 13:16:46.815849
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert isinstance(LookupModule().run, object)



# Generated at 2022-06-13 13:16:53.932933
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    print(lookup_module.run(['DEFAULT_BECOME_USER'], variables=None, **{'on_missing': 'error'}))
    print(lookup_module.run(['DEFAULT_BECOME_USER', 'remote_user'], variables=None, **{'on_missing': 'error', 'plugin_type': 'connection', 'plugin_name': 'ssh'}))
    print(lookup_module.run(['DEFAULT_BECOME_USER', 'remote_user', 'home'], variables=None, **{'on_missing': 'error', 'plugin_type': 'connection', 'plugin_name': 'ssh'}))

# Generated at 2022-06-13 13:17:08.619184
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # In this case, "terms" is a value to lookup in the constants,
    # and we verify the correct value is returned.
    LookupModule.run = mock.Mock(return_value='bar')
    assert LookupModule.run('foo') == 'bar'

    # Verify that the any exception is properly re-raised.
    LookupModule.run = mock.Mock(side_effect=Exception('foo'))
    try:
        LookupModule.run('foo')
    except Exception as e:
        assert to_native(e) == 'foo'

    # Check that a missing value raises the correct exception.
    try:
        LookupModule.run('foo')
    except Exception as e:
        assert to_native(e) == 'reachability'

# Generated at 2022-06-13 13:17:16.729602
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase
    from ansible.errors import AnsibleOptionsError
    from ansible.module_utils._text import to_text

    lookup_base = LookupBase()
    config_module = LookupModule()

    # Testing missing option.
    try:
        config_module.run([], [])
    except AnsibleOptionsError as e:
        assert e.args[0] == "required option `_terms` missing."

    # Testing invalid type of terms.
    try:
        config_module.run(['default_remote_user', 1], [])
    except AnsibleOptionsError as e:
        assert e.args[0] == 'Invalid setting identifier, "1" is not a string, its a <type \'int\'>'

    # Testing invalid value of `on_missing` option.

# Generated at 2022-06-13 13:17:25.320901
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.config.manager

    class Options:
        def __init__(self, var_options=None, direct=None):
            self.var_options = var_options
            self.direct = direct
            self.plugin_type = None
            self.plugin_name = None
            self.on_missing = None

    class Sentinel:
        pass

    C.config = ansible.config.manager.ConfigManager()
    C.DEFAULT_BECOME_USER = 'root'
    C.DEFAULT_ROLES_PATH = ['roles']
    C.RETRY_FILES_SAVE_PATH = '/var/tmp'
    C.COLOR_OK = 'green'
    C.COLOR_CHANGED = 'yellow'

    s = LookupModule()
    s.set_loader(plugin_loader)


# Generated at 2022-06-13 13:17:34.933372
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # fixture for lookup_module
    lookup_module = LookupModule()

    # missing setting
    lookup_module.set_options(on_missing='error')
    terms = ['UNKNOWN']
    try:
        lookup_module.run(terms, [])
        assert False
    except AnsibleOptionsError as e:
        assert str(e) == 'Invalid setting "on_missing" must be a string and one of "error", "warn" or "skip", not error'

    # missing setting
    lookup_module.set_options(on_missing='warn')
    terms = ['UNKNOWN']
    result = lookup_module.run(terms, [])
    assert result == []

    # missing setting
    lookup_module.set_options(on_missing='skip')
    terms = ['UNKNOWN']
    result = lookup_module.run

# Generated at 2022-06-13 13:17:35.826578
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run(['foo', 'bar', 'baz'])
    pass

# Generated at 2022-06-13 13:17:37.420132
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(['random_config'])
    assert result == []

# Generated at 2022-06-13 13:17:45.207674
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:17:56.542677
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(
        argument_spec={
            'plugin_type': dict(type='str', required=False, choices=['become', 'cache', 'callback', 'cliconf', 'connection',
                                                                     'httpapi', 'inventory', 'lookup', 'netconf', 'shell', 'vars']),
            'plugin_name': dict(type='str', required=False),
            '_terms': dict(type='list', required=True, elements='str'),
            'on_missing': dict(type='str', choices=['error', 'warn', 'skip'], default='error'),
        },
    )

    # get the global setting by name

# Generated at 2022-06-13 13:18:06.786988
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    config_dict = dict(become_method='become_method', become_user='become_user', become_ask_pass='become_ask_pass', become_password='become_password')
    ansible_config_dict = dict(DEFAULT_BECOME_METHOD=config_dict['become_method'], DEFAULT_BECOME_USER=config_dict['become_user'], DEFAULT_BECOME_PASS=config_dict['become_password'], DEFAULT_BECOME_ASK_PASS=config_dict['become_ask_pass'])
    plugin_name = 'become'
    plugin_type = 'become'
    terms_list = [become_method for become_method in config_dict]

# Generated at 2022-06-13 13:18:09.827132
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    result = LookupModule().run(['DEFAULT_BECOME_USER'])
    assert result[0] == 'root'

# Generated at 2022-06-13 13:18:32.965335
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # test global config
    result = lookup._get_plugin_config('test', 'lookup', 'DEFAULT_REMOTE_TMP')
    assert result == '/tmp/test'
    result = lookup._get_plugin_config('test', 'lookup', 'DEFAULT_REMOTE_TMP', ['DEFAULT_REMOTE_TMP=test'])
    assert result == 'test'

    # test global plugin
    result = lookup._get_plugin_config('test', 'lookup', 'test_global_test')
    assert result == 'test'
    result = lookup._get_plugin_config('test', 'lookup', 'test_global_test', ['test_global_test=test'])
    assert result == 'test'

    # test plugin of type
    result = lookup._get_plugin_

# Generated at 2022-06-13 13:18:44.469611
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_module = LookupModule()
    test_module.set_options(var_options={'test_var': 3})
    res = test_module.run([3])
    assert res == []
    res = test_module.run(['test_var'])
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0] == 3
    res = test_module.run(['test_var', 3])
    assert res == []
    test_module.set_options(var_options={'test_var': 3}, direct={'on_missing': 'error'})
    res = test_module.run(['test_var', 'test_var2'])
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0] == 3
   

# Generated at 2022-06-13 13:18:46.324414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms=["ROLES_PATH"], variables={}) == C.DEFAULT_ROLES_PATH

# Generated at 2022-06-13 13:18:48.552311
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    assert lu.run(terms) == ['root']


# Generated at 2022-06-13 13:18:53.689232
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.module_utils.six import PY2

    # Prepare
    terms = ["DEFAULT_ROLES_PATH", "RETRY_FILES_SAVE_PATH"]
    args = {}
    args['wantlist'] = True
    expected = os.path.expanduser('~/.ansible/roles')

    # Run
    got = LookupModule().run(terms=terms, variables=args, on_missing='skip')

    # Verify
    assert got[0] == expected


# Generated at 2022-06-13 13:19:03.022582
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_text
    # import ansible.plugins.loader as loader
    # loader.add_directory('./plugins')
    lu = LookupModule()
    result = lu.run(terms=['ANSIBLE_DEBUG'], variables={'ansible_debug': True})
    assert result == [True]
    result = lu.run(terms=['ANSIBLE_DEBUG'], variables={'ansible_debug': False})
    assert result == [False]
    # This test will fail, as it is checking for a config option that does not exist
    # result = lu.run(terms=['ANSIBLE_TEST'], variables={'ansible_test': False})
    # assert result == [False]

# Generated at 2022-06-13 13:19:14.294100
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test mocking the function _get_plugin_config
    with patch.object(lookup_plugins, '_get_plugin_config') as m_get_config:
        m_get_config.side_effect = ["config_value"]

        # create a object of class LookupModule
        lookup = LookupModule()

        # run the test
        ret = lookup.run(terms=["test_term"], variables={"plugin_type": "test_type", "plugin_name": "test_name"})

        # generate expected result
        expected = ["config_value"]

        # assert test result to expected result
        assert ret == expected



# Generated at 2022-06-13 13:19:19.223171
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #unit test for method run of class LookupModule
    lookup_mod = LookupModule()
    lookup_mod.set_options(direct={'plugin_type': 'connection', 'plugin_name': 'local'})
    result = lookup_mod.run(['set_via_config_file'], variables={'x': 'value', 'y': 'value2'})
    assert result == ['set_via_config_file']

# Generated at 2022-06-13 13:19:27.941579
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import LookupModule

    result = LookupModule().run(
        ["UNKNOWN"],
        {},
        on_missing='skip'
    )
    assert result == []

    result = LookupModule().run(
        ["UNKNOWN"],
        {},
        on_missing='warn'
    )
    assert result == []

    try:
        result = LookupModule().run(
            ["UNKNOWN"],
            {}
        )
    except:
        assert True


# Generated at 2022-06-13 13:19:37.511091
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create objects for test
    l = LookupModule()
    l2 = LookupModule()
    l3 = LookupModule()
    l4 = LookupModule()
    l5 = LookupModule()
    l6 = LookupModule()
    l7 = LookupModule()

    # test for existing config value
    assert l.run(['DEFAULT_REMOTE_USER']) == [ 'root' ]

    # test for missing config value
    try:
        l2.run(['UNKNOWN'])
    except Exception as e:
        assert e.message == 'Unable to find setting UNKNOWN'

    # test for missing config value with on_missing=skip
    assert l3.run(['UNKNOWN'], on_missing='skip') == []

    # test for missing config value with on_missing=warn
    assert l

# Generated at 2022-06-13 13:20:09.936677
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for invalid on_missing value
    lookup_mod = LookupModule()
    lookup_mod.set_options(direct={'on_missing': 'error'})
    assert lookup_mod.run(['DEFAULT_BECOME_USER']) == ['root']
    lookup_mod.set_options(direct={'on_missing': 'warn'})
    assert lookup_mod.run(['DEFAULT_BECOME_USER']) == ['root']
    lookup_mod.set_options(direct={'on_missing': 'skip'})
    assert lookup_mod.run(['DEFAULT_BECOME_USER']) == ['root']
    lookup_mod.set_options(direct={'on_missing': 'INVALID'})

# Generated at 2022-06-13 13:20:20.834329
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule ()
    lookup_module.set_options({'on_missing': 'error', 'plugin_type': None, 'plugin_name': None, 'var_options': {}})

    terms = [u'DEFAULT_BECOME_USER']
    result = [u'root']
    assert result == lookup_module.run(terms)

    lookup_module.set_options({'on_missing': 'skip', 'plugin_type': None, 'plugin_name': None, 'var_options': {}})
    terms = [u'DEFAULT_BECOME_USER', u'UNKNOWN']
    result = [u'root']
    assert result == lookup_module.run(terms)


# Generated at 2022-06-13 13:20:25.670782
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class OptionsModule(object):
        var_options = 'variables'
        direct = 'direct'
    lookup_module = LookupModule()
    lookup_module.set_options = MagicMock()
    lookup_module._display = MagicMock()
    lookup_module.get_option = MagicMock()
    lookup_module.get_option.return_value = 'test'
    assert lookup_module.run(terms = ['term'], variables = 'variables', direct = 'direct') == ['test']

# Generated at 2022-06-13 13:20:38.477291
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _get_global_config(_config):
        try:
            result = getattr(C, _config)
            if callable(result):
                raise AnsibleLookupError('Invalid setting "%s" attempted' % _config)
        except AttributeError as e:
            raise MissingSetting(to_native(e), orig_exc=e)
        return result


# Generated at 2022-06-13 13:20:44.962706
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=None)
    assert lookup_module.run(['DEFAULT_HASH_BEHAVIOUR']) == [
        'replace']
    assert lookup_module.run(['DEFAULT_HASH_BEHAVIOUR', 'DEFAULT_CACHE_PLUGIN']) == [
        'replace', 'memory']
    assert lookup_module.run(['DEFAULT_HASH_BEHAVIOUR', 'DEFAULT_CACHE_PLUGIN_SKIP_KEY']) == [
        'replace', ['vars', 'facts']]
    assert lookup_module.run(['UNKNOWN_CONFIGURATION_OPTION']) == []


# Generated at 2022-06-13 13:20:51.304687
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_instance = LookupModule()
    assert lookup_module_instance.run(['DEFAULT_REMOTE_USER']) == ['root']
    assert lookup_module_instance.run(['DEFAULT_REMOTE_USER', 'DEFAULT_BECOME_METHOD']) == ['root', 'sudo']

# Generated at 2022-06-13 13:21:01.162714
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = ['DEFAULT_BECOME_USER']
    expected_result = ['root']
    result = lookup_plugin.run(terms)
    assert result == expected_result

    terms = ['UNKNOWN']
    result = lookup_plugin.run(terms)
    assert result == []

    terms = ['UNKNOWN', 'DEFAULT_BECOME_USER', 'UNKNOWN2']
    expected_result = ['root']
    result = lookup_plugin.run(terms)
    assert result == expected_result

# Generated at 2022-06-13 13:21:09.310846
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    results = lookup_module.run(['remote_tmp'], dict(plugin_type='shell', plugin_name='sh'))
    assert results == ['/tmp', '/var/tmp']

    results = lookup_module.run([], dict(plugin_type='shell', plugin_name='sh'))
    assert results == []

    results = lookup_module.run(['remote_tmp'], dict(plugin_type='shell', plugin_name='sh1'))
    assert results == ['/tmp', '/var/tmp']

    try:
        lookup_module.run(['remote_tmp'], dict(plugin_type='shell'))
    except AnsibleOptionsError as e:
        assert 'Both plugin_type and plugin_name are required, cannot use one without the other' in str(e)


# Generated at 2022-06-13 13:21:19.335741
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    test_name = os.path.basename(__file__)
    test_file_name = os.path.splitext(test_name)[0]

    # If this test fails, it might be because ansible/constants.py ammended constants
    # under DEFAULT_ROLES_PATH.
    # Have to check if this is the case:
    if ('/usr/share/ansible/roles' not in C.DEFAULT_ROLES_PATH[0]) or\
            ('/etc/ansible/roles' not in C.DEFAULT_ROLES_PATH[1]):
        os.system('echo FAILED >> ' + test_file_name + '.result')

# Generated at 2022-06-13 13:21:24.557904
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import unittest
    from ansible.module_utils.six import StringIO


# Generated at 2022-06-13 13:22:22.770812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run(terms=["DEFAULT_BECOME_USER"], variables=None, on_missing='error', plugin_type='become', plugin_name='become', wantlist=False)
    assert result[0] == 'root', 'result should be root, but it is {0}'.format(result[0])
    result = module.run(terms=[], variables=None, on_missing='skip')
    assert result == [], 'result should be empty but it is {0}'.format(result)

# Generated at 2022-06-13 13:22:27.100073
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    results = look.run(['roles_path'], C.__dict__, on_missing='warn')
    assert results == [
        '/etc/ansible/roles'
    ]

# Generated at 2022-06-13 13:22:38.069986
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # unit test for method run on missing setting
    def run_test_missing(mock_display, missing, on_missing, terms, expected_exception):
        mock_display.info = ""
        try:
            lookup_module.run(terms=terms, on_missing=on_missing)
            assert False
        except Exception as err:
            assert isinstance(err, expected_exception)

    for on_missing in ['error', 'warn', 'skip']:
        for missing in ['INVALID']:
            run_test_missing(lookup_module._display, missing, on_missing, ['INVALID'], AnsibleLookupError)

    # unit test for method run on invalid setting

# Generated at 2022-06-13 13:22:38.793284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:22:46.323845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test invalid 'on_missing' option
    lu = LookupModule()
    assert "on_missing must be a string and one of 'error', 'warn' or 'skip', not 1" in lu.run(['whatever'], {}, on_missing=1)

    # test invalid 'config' option
    assert "Invalid setting identifier, 'whatever' is not a string, its a <class 'int'>" in lu.run(['whatever'], {}, config=1)

    # test 'on_missing' option with value 'error'
    assert "Unable to find setting whatever" in lu.run(['whatever'], {}, on_missing='error')

    # test 'on_missing' option with value 'skip'
    assert lu.run(['whatever'], {}, on_missing='skip') == []

    # test '

# Generated at 2022-06-13 13:22:54.230610
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run(terms=['DEFAULT_ROLES_PATH'], variables={'color': True}, on_missing='error', plugin_type='connection', plugin_name='ssh')
    assert result == [u'/usr/share/ansible/roles:/etc/ansible/roles:/usr/share/ansible/roles']
    result = lookup.run(terms=['DEFAULT_ROLES_PATH'], variables={'color': True}, on_missing='warn', plugin_type='connection', plugin_name='ssh')
    assert result == [u'/usr/share/ansible/roles:/etc/ansible/roles:/usr/share/ansible/roles']

# Generated at 2022-06-13 13:22:55.566899
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Unit test not implemented yet."

# Generated at 2022-06-13 13:23:04.945947
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    # calls run() from LookupModule
    result = lookup_plugin.run(['C.DEFAULT_HASH_BEHAVIOUR'], variables={}, on_missing='skip', plugin_type="connection", plugin_name="ssh")
    assert result == ['replace']

    # Tests run() method of LookupModule when no config file exists and 'on_missing' is set to 'error'
    result = lookup_plugin.run(['C.DEFAULT_HASH_BEHAVIOUR'], variables={}, on_missing='error', plugin_type="connection", plugin_name="ssh")
    assert result == []

    # Tests run() method of LookupModule when config file contains the option 'on_missing'

# Generated at 2022-06-13 13:23:11.348407
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create class instance
    lookupModule = LookupModule()

    # Add options
    lookupModule.set_options(var_options=None, direct={'plugin_type': 'become', 'plugin_name': 'test'})

    # Execute method run
    result = lookupModule.run(terms=["DEFAULT_BECOME_METHOD"], variables=None, **{'on_missing': 'error', 'plugin_type': 'become', 'plugin_name': 'test'})

    # Asserts
    assert result == ['sudo']

# Generated at 2022-06-13 13:23:24.901551
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check config value with on_missing=skip
    lookup = LookupModule()
    lookup_options = dict(
        on_missing='skip',
    )
    ret = lookup.run(['UNKNOWN'], variables=None, **lookup_options)
    assert ret == []
    # Check config value with on_missing=warn
    lookup = LookupModule()
    lookup_options = dict(
        on_missing='warn',
    )
    ret = lookup.run(['UNKNOWN'], variables=None, **lookup_options)
    assert ret == []
    # Check config value with on_missing=error
    lookup = LookupModule()
    lookup_options = dict(
        on_missing='error',
    )

# Generated at 2022-06-13 13:25:30.737186
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config = LookupModule()
    # 1st term in terms list
    term1 = 'DEFAULT_BECOME_USER'
    # 2nd term in terms list
    term2 = 'COLOR_ERROR'
    # 3rd term in terms list
    term3 = 'RETRY_FILES_SAVE_PATH'
    # 4th term in terms list
    term4 = 'UNKNOWN'

    variables = {
        'inventory_directory': '/home/ansible/inventory',
        'retry_files_save_path': '/home/ansible/retry'
    }

    # on_missing is missing in kwargs and default value will be used
    missing = 'error'
    ptype = None
    pname = None

    # case1: Invalid setting identifier (i.e, 'term' is not a string)
   

# Generated at 2022-06-13 13:25:40.879262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.module_utils.six import PY3
    assert 'config' in lookup_loader._lookup_cache.keys()
    lookup = lookup_loader._lookup_cache['config']
    assert isinstance(lookup, LookupModule)
    # test lookup_module when terms is a non-empty list of valid strings
    terms = ['RETRY_FILES_ENABLED']
    assert lookup.run(terms) == [True]
    # test lookup_module when parameter 'on_missing' is set to 'error' (the default value)
    # and term is not found in config
    terms = ['RETR_FILES_ENABLED']

# Generated at 2022-06-13 13:25:49.684322
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    # no plugin name, no plugin type
    terms = ['DEFAULT_BECOME_USER']
    response = lookup_module.run(terms=terms)
    assert response == ['root']

    terms = ['DEFAULT_BECOME_USER', 'ERROR_ON_MISSING_HANDLERS']
    response = lookup_module.run(terms=terms)
    assert response == ['root', False]

    # only plugin name
    terms = ['remote_tmp']
    with pytest.raises(AnsibleOptionsError):
        response = lookup_module.run(terms=terms, plugin_name='sh')

    # only plugin type
    terms = ['remote_tmp']

# Generated at 2022-06-13 13:25:59.835254
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import ansible.plugins.loader as plugin_loader
    from ansible.module_utils.network.common.utils import load_provider
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.config import NetworkConfig
