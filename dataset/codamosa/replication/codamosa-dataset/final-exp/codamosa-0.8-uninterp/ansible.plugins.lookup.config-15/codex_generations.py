

# Generated at 2022-06-13 13:16:06.954751
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    lookup = lookup_loader.get('config')

    ret = lookup.run(['FOO'], dict(), on_missing='error')
    assert ret == [], ret

    ret = lookup.run(['DEFAULT_BECOME_METHOD'], dict(), on_missing='error')
    assert ret == ['sudo'], ret

    ret = lookup.run(['DEFAULT_BECOME_METHOD'], dict(DEFAULT_BECOME_METHOD='su'), on_missing='error')
    assert ret == ['su'], ret


# Generated at 2022-06-13 13:16:12.757597
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    import sys
    import os

    # Fake the display class to avoid error
    class _display:
        class Display:
            verbosity = 0
            warning = lambda self, msg: None
        display = Display()

    class AnsibleOptionsError(Exception):
        pass

    lu = None

    def _get_global_config(config):
        if config == 'DEFAULT_ROLES_PATH':
            return 'roles'
        elif config == 'DEFAULT_BECOME_USER':
            return 'root'
        elif config == 'COLOR_OK':
            return 'blue'
        elif config == 'COLOR_CHANGED':
            return 'yellow'
        elif config == 'COLOR_SKIP':
            return 'green'

# Generated at 2022-06-13 13:16:22.668231
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''

    # Pexpect does not work in Python 3.6
    import sys
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 6:
        return

    import os
    import re
    import unittest
    import pexpect
    from ansible.plugins.loader import lookup_loader

    con = pexpect.spawnu('ansible-console')
    con.expect('localhost')
    con.sendline('config list')
    con.expect('localhost')
    con.sendline('quit')
    con.expect(pexpect.EOF)

    class Mock(object):

        def __init__(self):
            self.config = con.before.splitlines()


# Generated at 2022-06-13 13:16:26.079967
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock Ansible variables
    ansible_vars = dict()
    module = LookupModule()
    terms = ['DEFAULT_ROLES_PATH']
    result =  module.run(terms, ansible_vars, on_missing='error')
    assert result[0] == C.DEFAULT_ROLES_PATH

# Generated at 2022-06-13 13:16:36.633633
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.config
    import ansible.plugins.loader

    lookup_module = ansible.plugins.lookup.config.LookupModule()

    class MockDisplay(object):
        def __init__(self):
            self.warnings = []

        def warning(self, msg):
            self.warnings.append(msg)

    display = MockDisplay()


# Generated at 2022-06-13 13:16:48.125546
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    from ansible.parsing.plugin_docs import read_docstring

    display = Display()
    # We can't use display.verbosity here in this test because it defaults to - 1
    display._verbosity = 99

    #
    # Test User Error
    #
    l = LookupModule()

    l.set_display(display)
    try:
        # noinspection PyUnusedLocal
        result = l.run([1, 2, 3])
    except AnsibleOptionsError as e:
        assert to_native(e) == 'Invalid setting identifier, "1" is not a string, its a <type \'int\'>'
    else:
        assert False, "l.run should have raised AnsibleOptionsError"

# Generated at 2022-06-13 13:16:55.957474
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create the object
    lm = LookupModule()

    # This is a list of terms that are available

# Generated at 2022-06-13 13:17:05.194444
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup = lookup_loader.get('config')
    assert lookup
    assert lookup.run([
        'DEFAULT_ROLES_PATH',
        'DEFAULT_BECOME_USER',
        'DEFAULT_BECOME_METHOD',
        'RETRY_FILES_SAVE_PATH',
        'C.COLOR_OK',
        'C.COLOR_CHANGED',
        'C.COLOR_SKIP',
    ])


# Generated at 2022-06-13 13:17:06.547110
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 1 == 1

# Generated at 2022-06-13 13:17:15.515959
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile, shutil
    from ansible.plugins.lookup import LookupBase

    class TestLookupModule(LookupBase):
        def __init__(self, basedir=None, **kwargs):
            self.basedir = basedir
            super(TestLookupModule, self).__init__(**kwargs)
        def run(self, terms, variables=None, **kwargs):
            return terms

    lookup = TestLookupModule()

    try:
        temp_dir = tempfile.mkdtemp()
        print('temporary directory created: %s' % temp_dir)
        lookup.run(terms='testing', basedir=temp_dir, variables={'testing': 'foo'})

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

# Generated at 2022-06-13 13:17:36.443393
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockLookupModule(LookupModule):
        def __init__(self):
            self._display = DummyDisplay()
            self._options = dict(on_missing='error', plugin_type='connection')

    lookup = MockLookupModule()

    # Connection config is not defined
    terms = ['remote_user', 'port', 'bad_setting']
    res = lookup.run(terms)
    assert res == ['root', 22]

    # Connection config is defined
    # Connection config is not defined
    with pytest.raises(AnsibleLookupError) as e:
        terms = ['bad_setting']
        res = lookup.run(terms)
    assert 'Unable to find setting bad_setting' in to_native(e.value)


# Generated at 2022-06-13 13:17:42.877851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = ['DEFAULT_BECOME_USER', 'remote_user', 'UNKNOWN']
    test_ptype = 'connection'
    test_pname = 'ssh'
    test_missing = 'error'
    test_variables = {'async_timeout': 'foo'}

    lookup_obj = LookupModule()
    with pytest.raises(AnsibleOptionsError) as exec_info:
        lookup_obj.run(terms=test_terms, plugin_name=test_pname, on_missing=test_missing, variables=test_variables)
    assert "Both plugin_type and plugin_name are required, cannot use one without the other" in str(exec_info.value)


# Generated at 2022-06-13 13:17:53.961811
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.sentinel import Sentinel
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.display import Display

    # Ensure default value of on_missing is 'error'
    lookup_module = LookupModule()
    lookup_module.set_loader(plugin_loader)
    lookup_module.set_display(Display())

    try:
        lookup_module.run([None])
    except AnsibleOptionsError as e:
        assert 'is not a string' in str(e)
    else:
        assert False, 'Expected AnsibleOptionsError'

    try:
        lookup_module.run([''])
    except AnsibleLookupError as e:
        assert 'Unable to find setting' in str(e)

# Generated at 2022-06-13 13:17:56.003786
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    plugin = LookupModule()
    plugin.set_options({})
    plugin.run(None, None)

# Generated at 2022-06-13 13:17:58.623658
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # LookupModule.run()
    assert True == True

# Generated at 2022-06-13 13:18:06.208184
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    t_lookup_module = LookupModule()

    t_lookup_module.set_options(var_options=None, direct={})

    assert t_lookup_module.run(terms=['DEFAULT_BECOME_USER'], variables=None, **{}) == ['root']

    assert t_lookup_module.run(terms=['UNKNOWN'], variables=None, **{}) == []

    try:
        t_lookup_module.run(terms=['UNKNOWN'], variables=None, **{'on_missing':'error'})
    except AnsibleLookupError as e:
        assert str(e) == 'Unable to find setting UNKNOWN'

# Generated at 2022-06-13 13:18:11.350793
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _get_global_config(config):
        return {'env': C.DEFAULT_MODULE_LANG}

    module = LookupModule()
    module._get_global_config = _get_global_config

    assert module.run(terms=['env'], variables=None) == [C.DEFAULT_MODULE_LANG]

# Generated at 2022-06-13 13:18:22.336149
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:18:25.989944
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #test method run of class LookupModule
    terms = []
    variables = None
    kwargs = {}
    test1 = LookupModule(terms, variables, **kwargs)
    result = test1.run(terms, variables, **kwargs)
    assert result == []

# Generated at 2022-06-13 13:18:35.378229
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_cases = dict()
    test_cases[0] = dict(
        terms=['DEFAULT_BECOME_USER'],
        variables={'DEFAULT_BECOME_USER': 'root'},
        expected=['root'],
    )
    test_cases[1] = dict(
        terms=['DEFAULT_BECOME_USER'],
        variables={},
        expected=['test_lookup_plugin_config'],
    )
    test_cases[2] = dict(
        terms=['DEFAULT_BECOME_USER'],
        variables={'DEFAULT_BECOME_USER': 'root'},
        expected=['root'],
        on_missing='warn',
    )

# Generated at 2022-06-13 13:18:56.206101
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import ansible.plugins.loader as plugin_loader
    from ansible.constants import ANSIBLE_CACHE_PLUGIN
    from ansible.errors import AnsibleError, AnsibleLookupError
    from ansible.module_utils._text import to_native, to_text
    from ansible.module_utils.six import string_types

    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from io import BytesIO as StringIO

    # create a fake plugin to trick base plugin_loader
    class DummyPlugin(object):
        class DocsLookupModule(LookupBase):
            def run(self, terms, variables=None, **kwargs):
                return terms


# Generated at 2022-06-13 13:19:11.118360
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    dataloader = DataLoader()
    tmp = dataloader.get_basedir()
    variables = VariableManager()

    # Test basic run case
    terms = ['DEFAULT_BECOME_USER']
    test_lookup = LookupModule()
    result = test_lookup.run(terms)
    assert result[0] == 'root'

    # Test the color run case
    terms = ['COLOR_SKIP', 'COLOR_OK', 'COLOR_CHANGED']
    result = test_lookup.run(terms)

# Generated at 2022-06-13 13:19:18.325542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.utils.vars
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']
    ret = LookupModule().run(terms)
    assert (ret == [ansible.utils.vars.get_config_value('DEFAULT_BECOME_USER'), ansible.utils.vars.get_config_value('DEFAULT_ROLES_PATH')])

# Generated at 2022-06-13 13:19:31.844949
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class AnsibleOptionsError:
        pass
    class AnsibleLookupError:
        pass
    class AnsibleError:
        pass
    class MissingSetting:
        pass
    import ansible
    from ansible.plugins.loader import LookupModule as LookupModule_class
    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup import LookupBase as LookupBase_class
    from ansible.utils.sentinel import Sentinel
    class C:
        loader = None
    class Sentinal:
        pass
    lu = LookupModule()
    lu.set_options(None, None, Sentinal)
    lu.get_option("on_missing")
    lu.get_option("plugin_type")
   

# Generated at 2022-06-13 13:19:39.159257
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # object initialization
    l = LookupModule()

    # Test 1: value lookup with no error
    terms=["DEFAULT_BECOME_USER"]
    result = l.run(terms,variables=None,**{})
    assert result == ['root']

    #Test 2: value lookup with error
    terms=["UNKNOWN_BECOME_USER"]
    result = l.run(terms,variables=None,**{})
    assert result == ['root']

    #Test 3: value lookup with warn
    terms=["UNKNOWN_BECOME_USER"]
    result = l.run(terms,variables=None,**{"on_missing":"warn"})
    assert result == ['root']

#Unit test for method run_of class LookupModule with plugin type and plugin name

# Generated at 2022-06-13 13:19:39.579444
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:19:53.254019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test LookupModule.run() using default global settings
    lookup_module_1 = LookupModule()
    lookup_module_1.set_options(var_options=None, direct=None)
    terms_1 = ['callback_whitelist']
    global_setting_1 = lookup_module_1.run(terms_1)
    global_callback_whitelist = C.callback_whitelist 
    if global_callback_whitelist == global_setting_1[0]:
        print('=== PASS: test_LookupModule_run() ===')
    else:
        print('=== FAIL: test_LookupModule_run() ===')


    # test LookupModule.run() using specific plugin settings
    lookup_module_2 = LookupModule()

# Generated at 2022-06-13 13:19:59.565886
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible import context

    assert len(context._results) == 0

    # Test with plugin_type and plugin_name
    # These tests can only pass without changes to the core since the plugin itself will never be mocked
    try:
        LookupModule().run(terms=['remote_tmp'], plugin_type='shell', plugin_name='sh')
        assert ('sh' in context._results and context._results['sh'] == 'echo $TMPDIR')
    except LookupError:
        pass
    finally:
        context._results = {}

    try:
        LookupModule().run(terms=['remote_user'], plugin_type='connection', plugin_name='ssh')
        assert ('ssh' in context._results and context._results['ssh'] == 'ansible')
    except LookupError:
        pass
    finally:
        context

# Generated at 2022-06-13 13:20:07.410475
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Options(object):
        def __init__(self, var=None, direct={}):
            self.var = var
            self.direct = direct

    class Tqm(object):
        def __init__(self):
            self.vars = dict()

    class FakeDisplay(object):
        def __init__(self):
            self.verbosity = 3
            self.display = True

        def vvv(self, msg, *args, **kwargs):
            print(msg, *args, **kwargs)

    class FakeLoader(object):
        def get(pname, class_only=True):
            return None

        def all(ptype, class_only=True):
            return None


# Generated at 2022-06-13 13:20:18.208416
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    # Fixed term
    term = "DEFAULT_ROLES_PATH"
    result = lookup_module.run([term], variables=None)
    assert 'library' in result, "Result is not correct"

    # Fixed term with variable
    term = "${rpath}"
    result = lookup_module.run([term], variables={"rpath": "DEFAULT_ROLES_PATH"})
    assert 'library' in result, "Result is not correct"

    # List of terms
    terms = [term, term]
    result = lookup_module.run(terms, variables={"rpath": "DEFAULT_ROLES_PATH"})
    # Test if it returns 2 elements replicated
    assert 'library' in result and 'library' in result[1], "Result is not correct"

# Generated at 2022-06-13 13:21:01.026626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import lookup_loader

    # load a valid playbook
    pbfile = "/etc/ansible/playbooks/example.yaml"
    p = PlaybookExecutor(
        playbooks=[pbfile],
        inventory=InventoryManager(loader=DataLoader(), sources=['localhost', ]),
        variable_manager=VariableManager(),
        loader=DataLoader(),
    )
    p._tqm._stdout_callback = None
    p.run()

    # this needs to be done to setup the lookup plugin cache
    lookup_loader.get('file')



# Generated at 2022-06-13 13:21:06.325284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['BECOME_METHOD']) == ['sudo']
    assert LookupModule().run(['BECOME_METHOD', 'BECOME_USER']) == ['sudo', 'root']
    assert LookupModule().run(['BECOME_METHOD', 'BECOME_USER'], {'ANSIBLE_BECOME_USER': 'test'}) == ['sudo', 'test']



# Generated at 2022-06-13 13:21:16.850621
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    A simple class that demonstrates the unit testing of method run of class LookupModule.
    It creates an instance of LookupModule and calls its run method with the arguments of test_terms and test_variables.
    '''
    # test_terms is a list of lookup terms.
    test_terms = ["DEFAULT_BECOME_USER", "DEFAULT_ROLES_PATH", "COLOR_OK", "COLOR_CHANGED", "COLOR_SKIP"]
    # test_variables is a dict of extra variables
    test_variables = {"config_in_var": "UNKNOWN"}

    # Create an instance of LookupModule class.
    lookup_module = LookupModule()

    # call run method on instance of LookupModule class.
    result = lookup_module.run(test_terms,test_variables)
   

# Generated at 2022-06-13 13:21:22.418280
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['DEFAULT_BECOME_USER']
    variables = {}
    kwargs = {}
    test_obj = LookupModule()
    ret = test_obj.run(terms, variables, **kwargs)

    assert ret == ['root']
    assert ret[0] == 'root'

# Generated at 2022-06-13 13:21:23.022768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 1 == 1

# Generated at 2022-06-13 13:21:32.168597
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils.six import string_types
    from ansible.errors import AnsibleLookupError

    import ansible.plugins.loader as plugin_loader

    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_ROLES_PATH']

    kwargs = {'wantlist': True}
    variables = {'DEFAULT_ROLES_PATH': '/usr/local/ansible'}

    lookup_module = LookupModule()
    lookup_module.set_options(var_options=variables, direct=kwargs)

    # Get plugin configuration value
    ptype = 'connection'
    pname = 'local'
    kwargs['plugin_type'] = ptype
    kwargs['plugin_name'] = pname

# Generated at 2022-06-13 13:21:43.527434
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a lookup class
    lookup = LookupModule()

    # create a TerminateException class
    class TerminateException(Exception):
        pass

    try:
        # test the run method with args other than string list
        terms = [None, {}]
        lookup.run(terms)
    except AnsibleOptionsError as e:
        pass
    else:
        raise TerminateException

    try:
        # test the run method with args other than string list
        terms = ['DEFAULT_BECOME_USER', None, {}]
        lookup.run(terms)
    except AnsibleOptionsError as e:
        pass
    else:
        raise TerminateException

    # test the run method with args other than string list
    terms = ['DEFAULT_BECOME_USER', 'DEFAULT_BECOME_METHOD']

# Generated at 2022-06-13 13:21:53.023597
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test for method run of class LookupModule """
    # set up constants for test
    DEFAULT_HOST_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    DEFAULT_HOST_PATTERN = 'all'
    DEFAULT_PATTERN = '*'
    DEFAULT_CACHE_PLUGIN = 'memory'
    DEFAULT_FILE_CHECK_PLUGIN = 'file'
    DEFAULT_CONNECTION_PLUGIN = 'smart'
    DEFAULT_GATHER_PLUGIN = 'smart'
    DEFAULT_INVENTORY_PLUGIN = 'auto'
    DEFAULT_LOCAL_TMP = '$LOCAL_TMP,$remote_tmp,/tmp'

# Generated at 2022-06-13 13:21:59.575819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['DEFAULT_BECOME_USER']) == [
        'root']
    assert LookupModule().run(['UNKNOWN_SETTING'], on_missing='warn') == []
    assert LookupModule().run(['UNKNOWN_SETTING'], on_missing='skip') == []
    assert LookupModule().run(['UNKNOWN_SETTING'], on_missing='error') == []

# Generated at 2022-06-13 13:22:00.983398
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "We need a test for LookupModule.run"

# Generated at 2022-06-13 13:23:04.590360
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    configs = {
        'test': {
            'connection': ['ssh'],
            'ptype': 'connection',
            'pname': 'ssh'
        }
    }

    for item in configs:
        terms = [configs[item]['connection']]
        ptype = configs[item]['ptype']
        pname = configs[item]['pname']
        ret = LookupModule().run(terms, plugin_type=ptype, plugin_name=pname)
        assert ret == terms

# Generated at 2022-06-13 13:23:13.189593
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with plugin type and name
    terms = ['shell','sh']
    ptype = 'shell'
    pname = 'sh'

    # for test case pass plugins type as 'shell' and plugin name as 'sh'
    lookup_plugin = LookupModule()
    result = lookup_plugin.run(terms, plugin_type=ptype, plugin_name=pname)
    assert result == [C.DEFAULT_REMOTE_TMP]

    # in this case we are providing only type and no plugin name
    terms = ['shell']
    result = lookup_plugin.run(terms, plugin_type=ptype, plugin_name='sh')
    assert result == [C.DEFAULT_REMOTE_TMP]

    # in this case we are providing only plugin name and no type

# Generated at 2022-06-13 13:23:24.318860
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule
    l1 = LookupModule()
    # Test run with invalid on_missing value
    l1.run(["anyterm"],{"plugin_type": "connection", "plugin_name": "local"}, on_missing="anystring")
    # Test run with missing plugin_type and plugin_name
    l1.run(["anyterm"],{"plugin_type": "connection"}, on_missing="anystring")
    # Test run with invalid term
    l1.run([1], on_missing="skip")
    # Test run with invalid term
    l1.run(["anyterm"], on_missing="skip")

# Generated at 2022-06-13 13:23:33.220323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    # global config test
    assert lu.run([u'DEFAULT_REMOTE_TMP'], variables={}) == [u'/tmp/ansible-${USER}'], "Error in DEFAULT_REMOTE_TMP"
    # ensure that variables are substituted
    assert lu.run([u'DEFAULT_REMOTE_TMP'], variables={u'USER': u'bob'}) == [u'/tmp/ansible-bob'], "Error in DEFAULT_REMOTE_TMP with variable"

    # plugin config test
    # TODO: replace with ansible.plugins.connection.local once it is moved outside of core

# Generated at 2022-06-13 13:23:46.113764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
   

    mock_variable = {
        'ansible_ssh_private_key_file': 'keys/test_rsa',
        'ansible_ssh_host': '127.0.0.1',
        'ansible_ssh_port': 22,
        'ansible_ssh_user': 'root'
    }

    # Validating plugin_type and plugin_name
    with pytest.raises(AnsibleOptionsError) as exc:
        LookupModule().run([], plugin_type='connection')
    assert 'plugin_name is required' in str(exc.value)

    with pytest.raises(AnsibleOptionsError) as exc:
        LookupModule().run([], plugin_name='ssh')
    assert 'plugin_type is required' in str(exc.value)

    # Validating plugin_type
   

# Generated at 2022-06-13 13:23:52.506187
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test code with valid options, which return value
    params = dict(
        _terms = [
            'DEFAULT_ROLES_PATH'
        ],
        plugin_type = 'vars',
        plugin_name = 'ansible_facts'
    )
    lookup_obj = LookupModule()
    assert lookup_obj.run(**params) == [C.DEFAULT_ROLES_PATH]


# Unit test case to test run method of LookupModule class with invalid option on_missing

# Generated at 2022-06-13 13:24:02.184236
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # --- Setup --------------------------------------
    # Set the options
    var_options = {
        'CONFIG': 'value1',
        'config': 'value2'
    }
    direct_options = {
        'var': 'value1',
        'on_missing': 'error',
        'plugin_type': 'test_type',
        'plugin_name': 'test_name'
    }

    # Create the test lookup object
    lookup = LookupModule()
    lookup.set_options(var_options, direct=direct_options)

    # Create test terms
    terms = ['CONFIG', 'config', '', 'a', True]

    # Create test variables
    variables = {'var2': 'value2'}

    # --- Test run when no config exists ---------------
    # Execute the run

# Generated at 2022-06-13 13:24:04.293522
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    terms = ["DEFAULT_ROLES_PATH"]
    result = look.run(terms)
    assert result != []

# Generated at 2022-06-13 13:24:15.546655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.config
    _variables = dict()
    _variables['host_key_checking'] = True
    _variables['ansible_connection'] = 'local'
    _variables['ansible_python_interpreter'] = '/usr/bin/python'
    _variables['nocows'] = 1
    _terms = list()
    _terms.append('host_key_checking')
    _terms.append('ansible_connection')
    _terms.append('ansible_python_interpreter')
    _terms.append('nocows')
    _kwargs = dict()
    _kwargs['plugin_name'] = 'shell'
    _kwargs['plugin_type'] = 'shell'
    _kwargs['on_missing'] = 'error'
    assert ansible.plugins

# Generated at 2022-06-13 13:24:28.446181
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The following two plugins are always present
    fake_plugin_type = 'connection'
    fake_plugin_name = 'local'

    # tests for a global setting
    global_setting_name = 'DEFAULT_ROLES_PATH'

    try:
        my_lookup = LookupModule()
        my_lookup._display = FakeDisplay()
        my_result = my_lookup.run([global_setting_name], on_missing='error')
        if not my_result:
            assert False, 'Expected not-empty result for global setting, got empty'
    except Exception as e:
        assert False, 'Expected success, got failure with error: %s' % str(e)
