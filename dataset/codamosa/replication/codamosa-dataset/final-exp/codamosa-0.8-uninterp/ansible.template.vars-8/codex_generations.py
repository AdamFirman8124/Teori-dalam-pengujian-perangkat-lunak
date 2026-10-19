

# Generated at 2022-06-13 15:38:38.761052
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)

# Generated at 2022-06-13 15:38:49.336486
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = dict()
    globals = dict()
    locals = dict()
    vars = AnsibleJ2Vars(templar, globals, locals=locals)
    assert("k" not in vars)
    templar["k"] = "v"
    assert("k" in vars)
    locals["k"] = "v"
    assert("k" in vars)
    globals["k"] = "v"
    assert("k" in vars)
    templar = dict()
    globals = dict()
    locals = dict()
    vars = AnsibleJ2Vars(templar, globals, locals=locals)
    assert("k" not in vars)
    locals["k"] = "v"
    assert("k" in vars)
    templar

# Generated at 2022-06-13 15:39:00.486427
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.parsing.yaml.objects import AnsibleMapping

    display = Display()
    variable_manager = VariableManager()
    variable_manager.extra_vars = AnsibleMapping({"extra_var": "extra_var_value"})
    templar = Templar(variable_manager=variable_manager, display=display)

    vars = AnsibleJ2Vars(templar, {'global_var': 'global_var_name'}, {'local_var': 'local_var_name'})

    assert 'extra_var' in vars
    assert 'local_var' in vars
    assert 'global_var' in vars
    assert 'undefined_var'

# Generated at 2022-06-13 15:39:01.276815
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # todo
    pass

# Generated at 2022-06-13 15:39:06.428897
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'var_1': 'my_var_1'})

    globals = {
        'var_2': 'my_var_2',
        'l_var_3': 'my_l_var_3',
    }
    ajv = AnsibleJ2Vars(templar, globals)

    assert 'var_1' in ajv
    assert 'var_2' in ajv
    assert 'l_var_3' in ajv
    assert 'var_4' not in ajv



# Generated at 2022-06-13 15:39:18.081549
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible import constants as C
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    # Variable loaded in loader
    variable_in_loader = '{{ variable_in_loader }}'
    variable_in_loader_value = 'value of variable_in_loader'
    # Variable loaded in loader and also in templar
    variable_in_loader_and_templar = 'variable_in_loader_and_templar'
    variable_in_loader_and_templar_value = 'value of variable_in_loader_and_templar'
    # Variable loaded both in loader and globals
    variable_in_loader_and_globals = 'variable_in_loader_and_globals'
    variable_in_loader_and_globals

# Generated at 2022-06-13 15:39:27.556707
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    def test_getitem(varname, vars):
        '''
        Returns the result of __getitem__ of AnsibleJ2Vars with argument varname and
        globals and locals set to vars.
        '''
        templar = Templar(loader=DataLoader())
        return AnsibleJ2Vars(templar, globals=vars, locals=vars)[varname]

    # Basic test: varname and value are string
    assert test_getitem

# Generated at 2022-06-13 15:39:39.064603
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # create environment and get jinja2 environment variables
    # myspecialvar should not be present in the jinja2 environment variables
    assert not "myspecialvar" in dict(templar._available_variables)
    assert "myspecialvar" not in static_vars
    assert "myspecialvar" not in self_vars
    assert "myspecialvar" not in dynamic_vars

    # add myspecialvar to static_vars and self_vars and create j2vars object for this vars
    static_vars["myspecialvar"] = "test"
    self_vars["myspecialvar"] = "test"

    j2vars = AnsibleJ2Vars(templar, static_vars, self_vars)

    # myspecialvar should be present in the jinja

# Generated at 2022-06-13 15:39:44.132183
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = {'test1': 'test1'}
    locals = {'test2': 'test2'}
    j2_vars = AnsibleJ2Vars(templar=templar, globals=globals, locals=locals)
    assert ('test1' in j2_vars)
    assert ('test2' in j2_vars)
    assert ('test3' not in j2_vars)



# Generated at 2022-06-13 15:39:50.788813
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = Templar(loader=None, variables={'testvar': 'testvalue'})
    vars_proxy = AnsibleJ2Vars(templar, {})
    assert 'testvar' in vars_proxy
    assert 'testvar2' not in vars_proxy
    assert 'testvar3' not in vars_proxy


# Generated at 2022-06-13 15:40:01.354082
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.template import Templar
    templar = Templar(loader=None, variables={'a': 42, 'b': '{{a}}'})
    aj2v = AnsibleJ2Vars(templar, globals={'foo': 'bar'})

    print('get "a"')
    print(aj2v.__getitem__(varname='a') == 42)

    print('get "b"')
    print(aj2v.__getitem__(varname='b') == '42')

    print('get "foo"')
    print(aj2v.__getitem__(varname='foo') == 'bar')

    print('get "undefined"')

# Generated at 2022-06-13 15:40:10.098714
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()

    templar = Templar(loader=loader, variables=variable_manager, play_context=play_context)

    globals = {
        'test_global_variable': 'test_global_variable_value',
        'test_global_dict': dict(test_key='test_value'),
    }
    locals = {
        'test_local_variable': 'test_local_variable_value',
        'test_local_dict': dict(test_key='test_value'),
    }


# Generated at 2022-06-13 15:40:22.181641
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    def my_display(msg, color=None, stderr=False, screen_only=False, log_only=False):
        print("DISPLAY %s" % msg)

    display.display = my_display

    from ansible.template import Templar


# Generated at 2022-06-13 15:40:33.074903
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar()
    globals_ = {'ANSIBLE_VAR_1': '1', 'ANSIBLE_VAR_2': '2'}
    locals_ = {'ANSIBLE_VAR_1': '1', 'ANSIBLE_VAR_2': '3'}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_, locals_)

    assert ansible_j2_vars.__contains__('ANSIBLE_VAR_1')

    assert ansible_j2_vars.__contains__('ANSIBLE_VAR_2')

    assert not ansible_j2_vars.__contains__('ANSIBLE_VAR_3')

    assert ansible_j2_vars.__contains

# Generated at 2022-06-13 15:40:41.692938
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar()
    templar.available_variables = {}
    templar.available_variables["test1"] = "{{test2}}"
    templar.available_variables["test2"] = "test3"
    templar.available_variables["test4"] = HostVars()

    globals = {}
    globals["test0"] = "test0"
    globals["test1"] = "test1"

    local = {}
    local["test3"] = "test3"

    ansibleJ2vars = AnsibleJ2Vars(templar, globals, locals=local)

    # variable is in local
    assert ansibleJ2vars.__getitem

# Generated at 2022-06-13 15:40:47.897808
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar
    def __contains__(self, k):
        if k in self._locals:
            return True
        if k in self._templar.available_variables:
            return True
        if k in self._globals:
            return True
        return False

    def __getitem__(self, varname):
        if varname in self._locals:
            return self._locals[varname]
        if varname in self._templar.available_variables:
            variable = self._templar.available_variables[varname]
        elif varname in self._globals:
            return self._globals[varname]

# Generated at 2022-06-13 15:40:56.523671
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode
    import jinja2
    key = 'key'
    locals = {
        key: AnsibleUnicode('local value'),
    }
    globals = {
        key: AnsibleUnicode('global value'),
    }
    templar = AnsibleMapping()
    templar.available_variables = {
        key: AnsibleUnicode('available value'),
    }
    ansible_vars = AnsibleJ2Vars(templar, globals, locals)
    assert key in ansible_vars


# Generated at 2022-06-13 15:41:06.073152
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar

    def get_templar(variables):
        # return an AnsibleJ2Vars
        return AnsibleJ2Vars(
            # return a Templar
            # mock the method Templar.template
            variables=variables
        )

    # test when variable is in available_variables
    test_variable = {
        # test variable
        "name": "ansible",
        # values of variable
        "value": {
            "test": {
                "test": "test"
            }
        },
        # values of variable after template
        "result": {
            "test": {
                "test": "test"
            }
        }
    }
    result = get_templar({test_variable["name"]: test_variable["value"]})[test_variable["name"]]

# Generated at 2022-06-13 15:41:07.086205
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    raise NotImplementedError()


# Generated at 2022-06-13 15:41:17.096317
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # test to ensure that AnsibleJ2Vars.__contains__ works correctly
    class AnsibleJ2Vars_test(AnsibleJ2Vars):
        def __contains__(self, k):
            if self.__dict__.__contains__(k):
                return True
            else:
                return False

    aj2v = AnsibleJ2Vars_test(templar={}, globals={}, locals={'test':True})
    assert 'test' in aj2v
    assert 'tast' not in aj2v
    assert 'test' in aj2v._locals
    assert 'test' not in aj2v._templar
    assert 'test' not in aj2v._globals

# Generated at 2022-06-13 15:41:26.949160
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Create mock objects of classes Templar, AnsibleJ2Vars
    import ansible.plugins.loader as loader_plugin
    import ansible.template.template as template
    templar = template.Templar(loader=loader_plugin)

# Generated at 2022-06-13 15:41:34.592881
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar

    templar = Templar()
    globals = {'g1': 1, 'g2': 2}
    locals = {'l1': 3, 'l2': 4}
    j2vars = AnsibleJ2Vars(templar, globals=globals, locals=locals)

    assert set(j2vars.__iter__()) == set(['g1', 'g2', 'l1', 'l2'])



# Generated at 2022-06-13 15:41:40.371852
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    # Prepare required objects
    templar = Templar(loader=DataLoader())
    globals = dict()
    locals = dict()
    j2_vars = AnsibleJ2Vars(templar, globals, locals=locals)
    # Test ensures that __contains__ doesn't throw an exception
    assert 'foo' not in j2_vars

# Generated at 2022-06-13 15:41:45.459568
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():

    # Create mock of AnsibleJ2Vars
    mock_templar = mock.MagicMock()
    mock_globals = {}
    mock_locals = {}
    subject = AnsibleJ2Vars(mock_templar, mock_globals, mock_locals)
    result = len(subject)

    # Assert that AnsibleJ2Vars(mock_templar, mock_globals, mock_locals).__len__() == 0
    assert result == 0



# Generated at 2022-06-13 15:41:58.175444
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import tempfile
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.jinja2.vault import VaultSecret
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars

    # test: s[k] returns the expected result
    # test: s[k] raises KeyError when k is missing
    def test(s, k, expected, raises):
        try:
            result = s[k]
        except KeyError:
            if not raises:
                raise AssertionError('Unexpected KeyError')

# Generated at 2022-06-13 15:42:03.910561
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    # The code under test
    from ansible.playbook.templar import Templar
    from ansible.template.safe_eval import safe_eval

    templar = Templar(loader=None, variables={'foo': 'bar'})

    result = set(AnsibleJ2Vars(templar, None).__iter__())

    assert result == set(['foo'])


# Generated at 2022-06-13 15:42:12.937754
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    class AnsibleJ2Vars_mockup(AnsibleJ2Vars):
        def __init__(self, templar, globals, locals=None):
            self._templar = templar
            self._globals = globals
            self._locals = dict()
            if isinstance(locals, dict):
                for key, val in iteritems(locals):
                    if val is not missing:
                        if key[:2] == 'l_':
                            self._locals[key[2:]] = val
                        elif key not in ('context', 'environment', 'template'):
                            self._locals[key] = val
            self._vars_dict = {}

        def __contains__(self, k):
            if k in self._locals:
                return True

# Generated at 2022-06-13 15:42:23.426753
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(loader=None, variables={'test': {'test': {'test': 'value'}}})
    variable = templar.available_variables['test']
    variable_expected = {'test': {'test': 'value'}}
    variable_json = AnsibleJSONEncoder().encode(variable)
    variable_expected_json = AnsibleJSONEncoder().encode(variable_expected)
    assert variable_json == variable_expected_json
    variable = HostVars()
    assert variable.__UNSAFE__ == True
    variable = 'vars'
    assert variable == 'vars'


# Generated at 2022-06-13 15:42:33.567840
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar(loader=None)

    locals = {'l_foo': 'bar', 'not_local': 'baz'}
    globals = {'g_baz': 'foo'}

    ajv = AnsibleJ2Vars(templar, globals, locals)

    assert 'foo' in ajv
    assert 'g_baz' in ajv
    assert 'l_foo' in ajv
    assert 'not_local' in ajv
    assert 'invalid_var' not in ajv

    # check if it raises KeyError when __contains__ is not overridden
    # NOTE: no easy way to test this separately, so we test this here

# Generated at 2022-06-13 15:42:45.211248
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vars import combine_vars

    add_all_plugin_dirs()
    vault_secrets = VaultLib()
    templar = Templar(loader=None, shared_loader_object=None, variables=None)
    host = Host(name='localhost')
    inventory = VariableManager()
    inventory.set_host_variable(host, 'ansible_ssh_host', '127.0.0.1')
    inventory.set_host_variable(host, 'ansible_connection', 'local')
    inventory.set_host

# Generated at 2022-06-13 15:42:57.760996
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    globals = dict()
    locals = dict()
    vars = AnsibleJ2Vars(Templar(loader=None, variables={}), globals, locals)
    globals['test_key1'] = 'test_value1'
    locals['test_key2'] = 'test_value2'
    assert 'test_key1' in vars
    assert 'test_key2' in vars
    assert 'test_key3' not in vars


# Generated at 2022-06-13 15:43:06.626690
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    class Templar:
        def __init__(self):
            self.available_variables = {'k1': 'v1', 'k2': 'v2'}

    def run_test(method, expect_iter):
        locals = {'l1': 'v1', 'l2': 'v2'}
        globals = {'g1': 'v1', 'g2': 'v2'}
        vars = AnsibleJ2Vars(Templar(), globals, locals)
        got_iter = [k for k in method(vars)]
        assert got_iter == expect_iter

    expect_iter = ['l1', 'l2', 'k1', 'k2', 'g1', 'g2']
    run_test(lambda x: x, expect_iter)

# Generated at 2022-06-13 15:43:11.511627
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    def check_AnsibleJ2Vars___contains__(inp, outp):
        templar = None
        globals = {'inp':1}
        locals = None
        my_AnsibleJ2Vars = AnsibleJ2Vars(templar, globals, locals)
        assert outp == (inp in my_AnsibleJ2Vars)

    for inp, outp in [['inp', True], ['not_inp', False]]:
        yield check_AnsibleJ2Vars___contains__, inp, outp

# Generated at 2022-06-13 15:43:23.873266
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class TestJ2Templar():
        def __init__(self):
            self.available_variables = {
                                'list1': "list1_value",
                                'dict1': {'a': 1, 'b': 2, 'c': 3},
                                's1': "s1_value",
                                's2': "s2_value"
                            }

    globals = {'v1': 'v1_value', 'v2': 'v2_value'}
    locals = {'b': 2}
    ajvars = AnsibleJ2Vars(TestJ2Templar(), globals, locals)
    assert isinstance(ajvars, AnsibleJ2Vars)
    assert ('list1' in ajvars)

# Generated at 2022-06-13 15:43:30.700158
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None, variables={'var1': 'value1'})
    globals = {
        'var2': HostVars(loader=None, variable_manager=None, host_name='some_host')
    }

    proxy = AnsibleJ2Vars(templar, globals)

    assert len(proxy) == 2
    assert proxy['var1'] == 'value1'
    assert proxy['var2'] == globals['var2']
    assert proxy['var3']  # should raise KeyError



# Generated at 2022-06-13 15:43:41.961111
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.template.templar import Templar

    class Host(object):
        def __init__(self, name):
            self.name = name

    class PlayContext(object):
        def __init__(self):
            self.verbosity = 0
            self.remote_addr = '127.0.0.1'

    class Play(object):
        def __init__(self):
            self.basedir = '.'
            self.vars = dict(
                x=1,
                y=2,
            )

    variables = dict(
        z=3,
    )

    host = Host('test_host')
    context = PlayContext()
    play = Play()
    variable_

# Generated at 2022-06-13 15:43:53.485760
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    def test_data():
        import sys
        from ansible.errors import AnsibleUndefinedVariable
        from ansible.module_utils.six import iteritems
        from ansible.template import Templar

        def get_test_var(test_item):
            return {'test_item': test_item}

        class AnsibleJ2VarsProxy(object):
            pass

        class AnsibleModule(object):
            # private helper to return the _name_ of the module
            def _load_params(self):
                params = AnsibleJ2VarsProxy()
                params.ansible_module_name = 'test_module'
                self.params = params

        class someVar(object):
            def __init__(self, value):
                self.value = value

            def __str__(self):
                return self.value

       

# Generated at 2022-06-13 15:44:04.741117
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import unittest

    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # Set up a 'templar' for the mock_j2vars_getitem to use.
    templar = Templar(loader=None)
    templar._available_variables = {}

    def mock_ansible_native(python_text):
        return python_text

    templar.ansible_native = mock_ansible_native

    # This is the real test fixture
    def mock_j2vars_getitem(jinja_var_name, expected_result):
        j2vars = AnsibleJ2Vars(templar, {})

# Generated at 2022-06-13 15:44:14.751075
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars
    import os
    import tempfile

    playbook_vars = {'foo': 'foo'}

    with tempfile.NamedTemporaryFile() as vars_file:
        vars_file.file.write(b'foo: bar')
        vars_file.file.flush()

        context = PlayContext()
        context.variable_manager = VariableManager()
        context.variable_manager.extra_vars = playbook_vars
        context.variable_manager.extra_vars['foo'] = 'not_foobar'
        context.variable_manager.extra_vars['bar'] = 'barfoo'
       

# Generated at 2022-06-13 15:44:21.531379
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    from ansible.template import Templar

    # expected value
    locals = set(['d', 'b', 'a', 'e', 'f'])

    # create an instance of AnsibleJ2Vars
    vars = AnsibleJ2Vars(Templar(), {'a': 1, 'b': 2, 'c': 3}, locals={'c': 3, 'd': 4, 'e': 5, 'f': 6})

    # check the result
    assert set(vars.__iter__()) == locals



# Generated at 2022-06-13 15:44:39.520222
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = None
    globals = {
        'bar': 'this is bar',
        'baz': 'this is baz',
    }
    locals = {'foo': 'this is foo'}
    testobj = AnsibleJ2Vars(templar, globals, locals)
    assert set(testobj.__iter__()) == set(['bar', 'baz', 'foo'])

# Generated at 2022-06-13 15:44:48.837756
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    hostvars = HostVars(hostname=AnsibleUnicode('host1'), ansible_host=AnsibleUnicode('1.1.1.1'))

# Generated at 2022-06-13 15:44:56.061996
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import boolean
    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar(loader=None)
    var_manager = VariableManager()
    hostvars = HostVars(loader=None, variables=dict(a=1))
    var_manager._hostvars = hostvars
    templar._available_variables = var_manager.get_vars(play=dict(vars=dict(b=2, c=1)))

# Generated at 2022-06-13 15:45:05.187431
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import SafeEval
    from ansible.template.templar import Templar
    from ansible.template.template import Templar as Templar_v2
    from ansible.vars.hostvars import HostVars

    globals1 = {'a': {'b': {'c': 1}} }
    globals2 = {'a': {'b': {'c': 2}} }
    hostvars3 = HostVars('hostvars3')

    templar1 = Templar(variables={}, loader=None, shared_loader_obj=None, fail_on_undefined=False, environment=SafeEval(), **dict())
    templar2 = Templar_v2(**dict())

# Generated at 2022-06-13 15:45:12.380975
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    templar = Templar(loader=None, variables={})
    variables = {'foo': AnsibleVaultEncryptedUnicode('bar'),
                 'baz': 'fizz'}
    j2vars = AnsibleJ2Vars(templar=templar,
                           globals=None,
                           locals=variables)

    # Test AnsibleVaultEncryptedUnicode
    value = j2vars['foo']
    assert isinstance(value, AnsibleVaultEncryptedUnicode)

    # Test other types
    value = j2vars['baz']

# Generated at 2022-06-13 15:45:18.620033
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'test_variable': 12})
    globals = dict()
    locals = dict({'test_local_variable': 13})
    obj = AnsibleJ2Vars(templar, globals, locals)
    obj_iter = obj.__iter__()
    for key in obj_iter:
        if key not in obj._templar.available_variables:
            raise AssertionError("Unexpected Key: '%s'" % key)


# Generated at 2022-06-13 15:45:25.052165
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Test AnsibleJ2Vars.__contains__()
    '''
    import ansible.template
    templar = ansible.template.Templar(loader=None)
    templar._available_variables = {'a': 1}

    globals = {}
    locals_ = {}
    vars = AnsibleJ2Vars(templar, globals, locals_)
    assert 'a' in vars
    assert 'b' not in vars

    globals = {'b': 2}
    locals_ = {}
    vars = AnsibleJ2Vars(templar, globals, locals_)
    assert 'a' in vars
    assert 'b' in vars
    assert 'c' not in vars

    globals = {}

# Generated at 2022-06-13 15:45:36.023716
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    # nothing in self._locals, nothing in self._templar, nothing in self._globals
    assert "key" not in AnsibleJ2Vars(Templar(), dict())

    # nothing in self._locals, nothing in self._templar, yes in self._globals
    assert "key" not in AnsibleJ2Vars(Templar(), dict(key=None))

    # nothing in self._locals, yes in self._templar, yes in self._globals
    assert "key" in AnsibleJ2Vars(Templar(variables=dict(key="value")), dict(key="value"))

    # yes in self._locals, yes in self._templar, yes in self._globals
    assert "key" in AnsibleJ2

# Generated at 2022-06-13 15:45:46.330146
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.template.template import Templar
    template_uid = 'test_AnsibleJ2Vars_contains__'

    templar = Templar(loader=None, variables={'foo': 'bar', 'xyzzy': 'abc'}, shared_loader_obj=None,
                      environment=None, fail_on_undefined=False)
    locals_ = None
    globals = {'xyzzy': '123', 'xyzzyx': '456'}
    ajv = AnsibleJ2Vars(templar, globals, locals=locals_)

    assert 'foo' in ajv
    assert 'xyzzy' in ajv
    assert 'xyzzyx' in ajv
    assert 'bar' not in ajv


# Generated at 2022-06-13 15:45:52.369456
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # Create a mock Templar class
    class Templar:
        def __init__(self):
            self.available_variables = dict(k1=1, k2=2)
        def template(self, s):
            return s

    # Create a mock AnsibleJ2Vars instance
    globals = dict(global_key="global_value")
    locals = dict(local_key="local_key")
    vars = AnsibleJ2Vars(Templar(), globals, locals)

    # Check __len__ works properly
    assert len(vars) == 3


# Generated at 2022-06-13 15:46:23.053097
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    class Templar():
        def __init__(self, available_variables):
            self.available_variables = available_variables

        def template(self, variable):
            return variable

    locals = {}
    globals = {'foo': 'bar'}

    v = AnsibleJ2Vars(Templar({}), globals, locals)
    # Test direct access to global variables
    assert v['foo'] == 'bar'

    # Test direct access to local variables
    locals = {'foo': 'baz'}
    v = AnsibleJ2Vars(Templar({}), globals, locals)
    assert v['foo'] == 'baz' # locals always take precedence over globals

    # Test direct access to template variables
    template_vars

# Generated at 2022-06-13 15:46:33.788157
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    available_variables = {'variable1': 'I am Variable 1', 'variable2': 'I am Variable 2', 'variable3': 'I am Variable 3'}
    templar = Templar(loader=None, variables=available_variables)
    globals = {'global1': 'I am Global 1', 'global2': 'I am Global 2', 'global3': 'I am Global 3'}
    locals = {'local1': 'I am Local 1', 'local2': 'I am Local 2', 'local3': 'I am Local 3'}
    ansible_j2_vars = AnsibleJ2Vars(templar=templar, globals=globals, locals=locals)

    assert ansible_j2_vars['variable1'] == 'I am Variable 1'

# Generated at 2022-06-13 15:46:38.296535
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import wrap_var
    import ansible.constants as C
    a = AnsibleJ2Vars(Templar({}), {})
    assert a == {}
    assert a != {'any': 'thing'}
    assert isinstance(a, dict)
    assert isinstance(a, AnsibleBaseYAMLObject)
    b = AnsibleJ2Vars(Templar({C.DEFAULT_HASH_BEHAVIOUR: 'merge'}), {'a': 'a'})
    assert b['a'] == 'a'

# Generated at 2022-06-13 15:46:48.995279
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    templar = Templar(loader=None)
    vars = {"varname": "test"}
    ansible_vars = AnsibleJ2Vars(templar, {})
    assert ansible_vars["varname"] == "test"
    ansible_vars._templar._available_variables = vars
    assert ansible_vars["varname"] == "test"
    vars = {"varname": "{{ something }}"}
    ansible_vars._templar._available_variables = vars
    assert ansible_vars["varname"] == ""
    ansible_vars._globals = {"something": "test"}
    assert ansible_vars["varname"] == "test"

# Generated at 2022-06-13 15:46:54.713798
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from collections import namedtuple

    vault_secrets = namedtuple('vault_secrets', ['id'])('c8a4e4d2-d2f2-46e1-9309-b64c9931908d')
    vault = VaultLib([])
    vault.secrets = [vault_secrets]
    templar = Templar(loader=None, variables={}, vault_secrets=[vault_secrets])

    aj2v = AnsibleJ2Vars(templar, {}, locals={})

    # test access to global var
    result = aj2v['omg']

# Generated at 2022-06-13 15:47:04.952489
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    
    variable_manager = VariableManager()
    templar = Templar(loader=None, shared_loader_obj=None, variable_manager=variable_manager)
    proxy = AnsibleJ2Vars(templar, dict(), dict())
    # Test env is empty
    assert len(proxy) == 0
    
    # Test env with one variable
    variable_manager.set_nonpersistent_facts(variable_manager.get_vars(loader=None, play=None, host=None, task=None))
    variable_manager.set_host_variable(host='', varname='h', value=dict())
    variable_manager.set_host_variable(host='', varname='hostvars', value=dict())
    variable_manager

# Generated at 2022-06-13 15:47:11.210641
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import sys
    import os
    import unittest2 as unittest

    from ansible.module_utils.six import PY3
    from ansible.plugin.loader import TemplateLoader
    from ansible.parsing.dataloader import DataLoader

    from ansible.template import Templar

    ############################
    # Setup for the data loader
    ############################

    class Options:
        Tags = {}
        module_path = None
        inventory = None
        connection = None
        module_name = None
        forks = None
        become = False
        become_method = None
        become_user = None
        check = False
        diff = False
        extra_vars = []
        listhosts = None
        listtasks = None
        listtags = None
        syntax = None
        sudo = False
       

# Generated at 2022-06-13 15:47:17.912023
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = Templar(loader=None, variables={'v1':'value1'})
    globals = {'gv1':'global-value1'}
    locals = {'v2':'value2'}
    jinja_vars = AnsibleJ2Vars(templar, globals, locals)

    assert 'v1' in jinja_vars
    assert 'v2' in jinja_vars
    assert 'gv1' in jinja_vars

    assert 'v3' not in jinja_vars


# Generated at 2022-06-13 15:47:27.526066
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    variable_manager = VariableManager()
    templar = Templar(loader=None, variables=variable_manager)
    play = Play().load({}, variable_manager=variable_manager, loader=None)
    play_context.variable_manager = variable_manager
    play_context._task_vars = {}
    templar._play_context = play_context

    # test __contains__ with simple hosts
    var_list = []
    # TODO: remove the list() below when ansible-base is not needed

# Generated at 2022-06-13 15:47:35.150893
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # Assume:
    #  - globals is a dict
    #  - locals is a dict
    globals = {'global1': 'value1', 'global2': 'value2'}
    locals = {'local1': 'value1', 'local2': 'value2'}
    # Given:
    #  - templar is a Templar object
    templar = Templar()
    #  - self is a AnsibleJ2Vars instance
    self = AnsibleJ2Vars(templar, globals, locals)
    # When:
    #  - I call AnsibleJ2Vars.__len__
    # Then:
    #  - method __len__ returns the sum of number of keys in globals
    #    and locals.
    assert len(self) == 4
    #  - method __len

# Generated at 2022-06-13 15:48:27.560803
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = dict()
            self.available_variables['var_in_available_variables'] = ""

    class FakeContext(object):
        def __init__(self):
            self.templar = FakeTemplar()

    context = FakeContext()
    j2vars_obj = AnsibleJ2Vars(templar=context.templar, globals=dict())
    assert 'var_in_available_variables' in j2vars_obj
    assert 'var_not_exist' not in j2vars_obj