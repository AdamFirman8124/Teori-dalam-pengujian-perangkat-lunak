

# Generated at 2022-06-13 15:38:35.988417
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar()
    a = AnsibleJ2Vars(templar, {'a': 1, 'b': 2})
    assert a['a'] == 1
    assert a['b'] == 2
    assert a['c'] == None

# Generated at 2022-06-13 15:38:46.271898
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    locals = {"a": 1, "b": 2, "c": 3}
    variables = {"x": "foo", "y": "bar", "z": "baz"}
    globals = {"global_a": 1, "global_b": 2, "global_c": 3}
    j2vars = AnsibleJ2Vars(Templar(), globals, locals)

    def check_dict(test_dict):
        for key in test_dict:
            assert key in j2vars

    check_dict(locals)
    check_dict(variables)
    check_dict(globals)



# Generated at 2022-06-13 15:38:46.875042
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    pass

# Generated at 2022-06-13 15:38:54.187914
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader(), variables=VariableManager(), fail_on_undefined=False)
    globals = dict(a=1, b=2)
    locals = dict(a=3, c=4)

    # Test variables definition
    aj2v = AnsibleJ2Vars(templar, globals, locals)
    assert 'a' in aj2v
    assert 'b' in aj2v
    assert 'c' in aj2v
    assert 'd' not in aj2v


# Generated at 2022-06-13 15:39:02.876439
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.parsing.yaml.objects

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping

    yaml_str1 = '''
    a: "{{ b }}"
    b: "c"
    '''
    yaml_str2 = '''
    a: "{{ b }}"
    b: "c"
    d: [1,2,3]
    c: "{{ d }}"
    '''
    yaml_str3 = '''
    a: [1, 2, 3]
    '''
    yaml_str4 = '''
    a: "c"
    '''
    yaml_str5 = '''
    a: "{{ missing }}"
    '''

# Generated at 2022-06-13 15:39:15.211941
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    class Templar(object):
        def __init__(self):
            pass
        def template(self, variable):
            return variable

    locals = {'key1': 'val1', 'key2': 'val2'}
    globals = {'key3': 'val3', 'key4': 'val4'}

    templar = Templar()
    templar.available_variables = {'key1': 'val1', 'key2': 'val2'}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)

    assert 'key1' in ansible_j2_vars
    assert 'key2' in ansible_j2_vars
    assert 'key3' in ansible_j2_vars
    assert 'key4' in ansible_

# Generated at 2022-06-13 15:39:23.814572
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    templar = AnsibleJ2Vars(templar=None, globals=None)
    templar.available_variables = {
        "var1": "value1",
        "var2": "value2",
        "var3": HostVars(hostname="dummy_hostname", hostvars=dict()),
        "var4": dict(),
        #"var5": "value5",
    }
    try:
        val = templar["var1"]
        assert val == "value1"
    except KeyError as e:
        assert False, "Exception raised: {}".format(e)

# Generated at 2022-06-13 15:39:25.532422
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # TODO

    #  # AnsibleJ2Vars.__getitem__(varname)

    # TODO
    return


# Generated at 2022-06-13 15:39:31.130806
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    # testing no locals
    j2vars = AnsibleJ2Vars(Templar(), {'a_global': 'fake_global'})
    assert j2vars['a_global'] == 'fake_global'
    assert j2vars['a_global_not_exist'] == KeyError
    # testing locals
    j2vars = AnsibleJ2Vars(Templar(), {'a_global': 'fake_global'},
                           {'a_local': 'fake_local'})
    assert j2vars['a_local'] == 'fake_local'
    assert j2vars['a_local_not_exist'] == KeyError


# Generated at 2022-06-13 15:39:34.430450
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    templar = Templar()
    env = AnsibleJ2Vars(templar, {}, locals={})
    assert env.__getitem__('test_var') == 'test_var value'

# Generated at 2022-06-13 15:39:44.801821
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import ansible_safe_eval

    # Setup
    templar = ansible_safe_eval. Templar(loader=None, variables={'var': 'a'})
    j2_vars = AnsibleJ2Vars(templar, {'j2_globals': 'aa'}, locals={"local1": "b"})

    # Test that an existing var can be found
    assert 'var' in j2_vars
    # Test that a non-existing var can not be found
    assert 'var2' not in j2_vars
    # Test that a non-existing var can not be found
    assert 'local1' in j2_vars
    # Test that a non-existing var can not be found
    assert 'local2' not in j2_vars
   

# Generated at 2022-06-13 15:39:50.705015
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    templar = Templar()
    vars = { 'a': 'A' }
    globals = dict()
    j2v = AnsibleJ2Vars(templar, globals, locals=vars)
    assert len(j2v) == 1


# Generated at 2022-06-13 15:39:59.282755
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    name = "AnsibleJ2Vars"
    m_templar = Templar(
        variables=VariableManager()
    )

    # Dict with key 'ansible_managed'
    m_globals = dict(ansible_managed="Ansible managed")

    o = AnsibleJ2Vars(m_templar, m_globals, locals=None)
    assert type(o) is AnsibleJ2Vars
    assert o.__class__.__name__ == name

    # test `__getitem__` with key as string
    unsafe_text = o.__getitem__("ansible_managed")


# Generated at 2022-06-13 15:40:05.166420
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template.safe_eval
    templar = ansible.template.Template(None)
    globals = dict()
    locals = dict()
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert vars['test_var'] == None
    assert vars['test_expression'] == None
    assert vars['test_var'] == None
    assert vars['test_var'] == None

# Generated at 2022-06-13 15:40:11.533188
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # pylint: disable=import-error,no-name-in-module
    from ansible.plugins.loader import variable_loader
    from ansible.template import Templar
    # pylint: enable=import-error,no-name-in-module

    available_variables = variable_loader.get('/tmp/ansible_unittest', None)
    templar = Templar(loader=None, variables=available_variables)
    ansible_j2_vars = AnsibleJ2Vars(templar, {}, locals={})
    assert ansible_j2_vars['omit'] == '<omitted>'

# Generated at 2022-06-13 15:40:23.527128
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    '''
    This function performs a unit test on the constructor of class AnsibleJ2Vars
    '''

    from ansible.template import Templar
    templar = Templar(loader=None)

    a = AnsibleJ2Vars(templar, globals=dict())
    assert(a._templar == templar)
    assert(a._globals == dict())
    assert(a._locals == dict())

    a = AnsibleJ2Vars(templar, globals=dict(), locals=dict(abc=123))
    assert(a._templar == templar)
    assert(a._globals == dict())
    assert(a._locals == dict(abc=123))


# Generated at 2022-06-13 15:40:24.368339
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    assert len(AnsibleJ2Vars(None, None, None)) == 0


# Generated at 2022-06-13 15:40:35.130767
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.vars_loader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()

    globals = dict(some_global_one=2, some_global_complex_one=dict(a=1, b=2))
    locals = dict(some_global_complex_one=dict(a=3, c=4))
    av = loader.load_from_file('test/unit/vars/vars_file', 'test/unit/vars')

    j2vars = AnsibleJ2Vars(Templar(loader=loader), globals=globals, locals=locals)

    assert j2vars['some_global_one'] == globals['some_global_one']

# Generated at 2022-06-13 15:40:45.145388
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # Concerning the patch that implements the __len__ method in class AnsibleJ2Vars, the following example shows
    # the case where a variable is defined both in locals and in available_variables.
    # If the __len__ method is not implemented, an exception is raised.
    # The error message is the following:
    #   TypeError: object of type 'AnsibleUndefinedVariable' has no len()
    # The error is raised, because 'len' is called for the exception object, instead of for the object 'self' that
    # needs to be returned.
    templar = object()
    globals = dict()
    locals = dict()
    locals['var1'] = 'test'
    context = dict()
    environment = dict()
    template = dict()
    available_variables = dict()

# Generated at 2022-06-13 15:40:53.727506
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.parsing.yaml.objects as ansible_parsing_yaml_objects
    import ansible.parsing.dataloader as ansible_parsing_dataloader
    import ansible.template.templar as ansible_template_templar
    import ansible.template.vars as ansible_template_vars

    def init_AnsibleJ2Vars(vars, globals):
        mock_templar = FakeTemplar()
        mock_templar.available_variables = vars
        return AnsibleJ2Vars(mock_templar, globals)

    def init_AnsibleVars(vars):
        mock_loader = FakeLoader()
        mock_loader._data = vars
        mock_vars = ansible_

# Generated at 2022-06-13 15:41:02.281227
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    templar = Templar([], [])

    var1 = AnsibleJ2Vars(templar, {})
    assert(var1)


# Generated at 2022-06-13 15:41:08.509214
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    #construct a test object
    ansiblej2vars_object=AnsibleJ2Vars()
    ansiblej2vars_object._locals['test_key'] = 'test_value'
    ansiblej2vars_object._templar.available_variables['test_key1'] = 'test_value1'
    ansiblej2vars_object._globals['test_key2'] = 'test_value2'

    #test len
    len_test_result=len(ansiblej2vars_object)
    assert len_test_result == 3

# Generated at 2022-06-13 15:41:13.191326
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    templar = Templar(loader=None)

    j2vars = AnsibleJ2Vars(templar, {}, {'l_foo': 'BAR'})

    assert j2vars['foo'] == 'BAR'



# Generated at 2022-06-13 15:41:22.174071
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template.safe_eval import safe_eval

    locals = {'l_foo': 'bar'}
    globals = {'foo': 'bar'}
    play_context = PlayContext()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}

# Generated at 2022-06-13 15:41:33.770870
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Declare dependence class
    class _Templar:
        def template(self, variable):
            return variable

        available_variables = dict()

    try:
        # 1. success
        templar = _Templar()
        globals = dict()
        locals = dict()
        ansible_vars = AnsibleJ2Vars(templar, globals, locals)
        print(ansible_vars["vars"].__class__)
        print(ansible_vars["vars"])
        globals["__getitem__"] = "__getitem__"
        print(ansible_vars["__getitem__"])
    except KeyError as e:
        print("Failure: ", e)

if __name__ == '__main__':
    test_AnsibleJ2Vars

# Generated at 2022-06-13 15:41:34.597682
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    pass

# Generated at 2022-06-13 15:41:43.755297
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import unittest
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play import Play
    from ansible.playbook.helpers import load_list_of_blocks

    class AnsibleJ2VarsTestCase(unittest.TestCase):

        @staticmethod
        def __get_vars__(vars_type, var_name):
            templar_class = 'ansible.parsing.yaml.objects.AnsibleBaseYAMLObject'

# Generated at 2022-06-13 15:41:55.568928
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    params = [
        {
            'item': {'key': 'value'}
        },
        {
            'item': {'after': 'value', 'key': 'value'}
        },
        {
            'item': {'key': 'value', 'after': 'value'}
        },
        {
            'item': {'before': 'value', 'key': 'value', 'after': 'value'}
        }
    ]
    for param in params:
        item = param['item']
        item_keys = list(item.keys())
        variable_name = item_keys[0]

        templar = mock_Templar()
        templar.available_variables = item

        globals = {'key': 'value'}

# Generated at 2022-06-13 15:42:04.161010
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    templar = Templar(loader=None, variables=dict())

    # test: __contains__(k)
    #     k is in locals
    host_vars = HostVars(loader=None, variables=dict())
    host_vars.add_host()
    variable_manager = VariableManager(loader=None, host_vars=host_vars, variables=dict())
    variable_manager.set_nonpersistent_facts(dict(ansible_python_interpreter='python'))

    vars_inst = AnsibleJ2Vars(templar, variable_manager.get_vars(play=None, host=None, task=None))
   

# Generated at 2022-06-13 15:42:09.619719
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    import jinja2.runtime
    templar = jinja2.runtime.Context({}, {}, {})

    # when key is in locals
    assert AnsibleJ2Vars(templar, {}, {'jinja2': 2.8}).__getitem__('jinja2') == 2.8

    # when key is in available_variables
    templar.environment.globals['available_variables'] = {'jinja2': 2.8}
    assert AnsibleJ2Vars(templar, {}).__getitem__('jinja2') == 2.8

    # when key is in globals

# Generated at 2022-06-13 15:42:31.730860
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    '''
    A sample test to demonstrate how to mock out the AnsibleJ2Vars class.
    '''

    templar = 'templar'
    globals = {
        'globals': 'globals'}
    locals = {
        'locals': 'locals'}

    # Mock out a Templar. This is not necessary if you don't need to access the templar member of AnsibleJ2Vars.
    # Valid options for mocking out a class member are documented here: https://docs.python.org/3/library/unittest.mock.html.
    from ansible.template import Templar
    Templar.available_variables = {'avars': 'avars'}
    Templar.template = lambda x, y: y
    templar = Templar()


    # Mock out AnsibleJ2

# Generated at 2022-06-13 15:42:43.133402
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    # Setup test fixture
    import jinja2
    from ansible.template import Templar

    templar = Templar(loader=jinja2.FileSystemLoader([]))
    j2vars = AnsibleJ2Vars(templar, dict())
    assert not j2vars.__contains__('testkey')

    # Execute code to be tested
    j2vars._templar.set_available_variables({'testkey': dict(testval='testval')})
    assert j2vars.__contains__('testkey')

    # Verify state of test fixture
    assert 'testkey' in templar._available_variables
    assert 'testkey' not in templar._available_variables['testkey']



# Generated at 2022-06-13 15:42:52.148564
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.manager import VariableManager
    from AnsibleModule_utils.AnsibleJ2Templar import AnsibleJ2Templar

    variables = dict()
    templar = AnsibleJ2Templar(loader=None, variables=variables)
    vars_obj = AnsibleJ2Vars(templar, globals=dict(), locals=dict())

    try:
        temp = vars_obj['vars']
    except KeyError as e:
        if "undefined variable" not in str(e):
            raise Exception(e)
        temp = None
    assert temp is None, "'vars' not in vars_obj"

    variables['vars'] = dict()
    templar = AnsibleJ2Templar(loader=None, variables=variables)
    vars_

# Generated at 2022-06-13 15:43:01.924665
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    try:
        from ansible.template.safe_eval import ansible_safe_eval

        # Test that AnsibleJ2Vars.__getitem__() catch KeyError when variable name is undefined
        templar = ansible_safe_eval.AnsibleTemplar()
        globals = {'test_var': 'test value'}
        locals = {'templar': templar, 'globals': globals}
        ansj2vars = AnsibleJ2Vars(templar, globals, locals)
        variable = ansj2vars['undefined']
        assert False, "ansj2vars['undefined'] should raise a KeyError"
    except KeyError as e:
        assert str(e) == "undefined variable: undefined"

    # Test that AnsibleJ2Vars.__get

# Generated at 2022-06-13 15:43:10.987715
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    templar = Templar(play_context=PlayContext(), loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar, {})

    try:
        ansible_j2_vars.__getitem__('varname')
    except KeyError as e:
        assert e.args[0] == 'undefined variable: varname'

    ansible_j2_vars = AnsibleJ2Vars(templar, {'varname': 'varvalue'})
    assert ansible_j2_vars.__getitem__('varname') == 'varvalue'

# Generated at 2022-06-13 15:43:23.077901
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    locals = {
        'l_foo': 'bar',
        'context': AnsibleBaseYAMLObject(),
        'environment': AnsibleBaseYAMLObject(),
        'template': AnsibleBaseYAMLObject(),
    }

# Generated at 2022-06-13 15:43:31.365000
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    variable_manager = VariableManager()
    variable_manager._extra_vars = {'extra': 'extra'}
    variable_manager._host_vars = {'host': 'host'}
    variable_manager._group_vars = {'group': 'group'}
    variable_manager._task_vars = {'task': 'task'}
    variable_manager._fact_cache = {'fact': 'fact'}
    variable_manager._available_variables = {'available': 'available'}
    variable_manager._is_adhoc = True
    variable_manager._is_task = True
    variable_manager._is_role = True
    variable_manager._is

# Generated at 2022-06-13 15:43:42.600535
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    templar = Templar()
    globals = dict()
    locals = dict()

    ansible_j2vars = AnsibleJ2Vars(templar, globals, locals)

    globals['__getitem__'] = 'globals'
    locals['__getitem__'] = 'locals'
    templar.available_variables['__getitem__'] = 'template'

    # Var in locals
    assert ansible_j2vars['__getitem__'] == 'locals'
    # Var in template
    assert ansible_j2vars['__getitem__'] == 'template'

    # Var in globals

# Generated at 2022-06-13 15:43:50.659615
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    globals = {}
    locals = {}
    templar = ""
    ajv = AnsibleJ2Vars(templar, globals, locals)
    ajv.__setitem__("a", 1)
    ajv.__setitem__("b", 2)

    iter_result = ajv.__iter__()
    list_result = []
    try:
        while True:
            list_result.append(next(iter_result))
    except:
        pass
    assert list_result == []


# Generated at 2022-06-13 15:43:57.950340
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    j2_templar = Templar(loader=loader, variables=variable_manager)

    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars["extra_vars"] = "extra_vars"
    variable_manager.host_vars["127.0.0.1"] = {"host_vars": "host_vars"}
    variable_manager.group_vars["group"] = {"group_vars": "group_vars"}

# Generated at 2022-06-13 15:44:23.363530
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(None, loader=None)
    vars = AnsibleJ2Vars(templar, globals={'foo': 'bar'})
    assert vars['foo'] == 'bar'

# Generated at 2022-06-13 15:44:29.000202
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.template import Templar
    from ansible.template.vars import AnsibleJ2Vars
    from ansible.vars.hostvars import HostVars
    import pytest
    from collections import Mapping

    templar = Templar(loader=None, variables={'a': 1, 'b': 2})
    assert hasattr(templar, 'available_variables') and isinstance(templar.available_variables, Mapping)
    assert templar.available_variables.get('a') == 1
    assert templar.available_variables.get('b') == 2
    assert templar.available_variables.get('c') is None

    aj2vars = AnsibleJ2Vars(templar, dict(), locals=dict(d=3))
    assert isinstance

# Generated at 2022-06-13 15:44:34.220772
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar()
    vars = AnsibleJ2Vars(templar, {'foo':'bar'})
    assert 'foo' in vars
    assert 'bar' not in vars


# Generated at 2022-06-13 15:44:43.374713
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    class mock_templar():
        def __init__(self):
            self.available_variables = {"foo": "bar", "baz": "qux"}
            self.template = lambda x: x

    class mock_globals():
        def __init__(self):
            self.globals = {"aa": 1, "bb": 2}

    locals = {"cc": 3, "dd": 4}

    v = AnsibleJ2Vars(mock_templar(), mock_globals(), locals=locals)
    assert sorted(list(v)) == sorted(["foo", "baz", "aa", "bb", "cc", "dd"])

# Generated at 2022-06-13 15:44:52.219056
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.playbook.play_context import PlayContext
    assert AnsibleJ2Vars(PlayContext(), {})["host"] == "{host}"
    assert AnsibleJ2Vars(PlayContext(), {})["vars"] == "{{ vars }}"
    assert AnsibleJ2Vars(PlayContext(), {})["ansible_check_mode"] == "False"

    from ansible.vars.hostvars import HostVars
    assert AnsibleJ2Vars(PlayContext(), {}, {"ansible_check_mode": HostVars({"ansible_check_mode": "True"})})["ansible_check_mode"] == "True"
    assert AnsibleJ2Vars(PlayContext(), {}, {"ansible_check_mode": "True"})["ansible_check_mode"] == "True"


# Generated at 2022-06-13 15:45:04.602409
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.template import Templar

    # test1 - element in locals
    templar = Templar(loader=None)
    globals = {'foo': None, 'bar': None}
    locals = {'foo': None}
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'foo' in vars
    assert 'bar' in vars
    assert 'baz' not in vars

    # test2 - element in templar's available_variables
    templar = Templar(loader=None)
    globals = {'foo': None, 'bar': None}
    templar._available_variables = dict(foo=None, bar=None)
    locals = {'foo': None}
   

# Generated at 2022-06-13 15:45:11.981197
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    """
    Test AnsibleJ2Vars.__contains__ with the following cases:
        - key in locals
        - key in available_variables
        - key in globals
        - key not found in any of the dictionaries
    """
    from ansible.vars.hostvars import HostVars
    class TestTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.template = lambda x: x

    available_variables = {"key1": "value1", "key2": "value2", "key3": "value3"}
    globals = {"glob1": "glob-value1", "glob2": "glob-value2"}

# Generated at 2022-06-13 15:45:20.724787
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # create used instances
    templar = Templar()
    globals = {}
    locals = {"local1": "value1", "local2": "value2"}
    ansible_vars = {"var1": "value1", "var2": "value2"}
    for key in ansible_vars:
        templar.available_variables[key] = ansible_vars[key]
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)

    for key in locals:
        assert ansible_j2_vars[key] == locals[key]
    for key in ansible_vars:
        assert ansible_j2_vars[key] == ansible_vars[key]
    with pytest.raises(KeyError):
        ansible

# Generated at 2022-06-13 15:45:33.019805
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    test_dict = {'a': 1, 'b': 2, 'c': 3}
    test_dict_c = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    varname = 'test'
    test_dict_copy = ['a', 'c']


# Generated at 2022-06-13 15:45:43.501618
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = dict()

    from ansible.vars.unsafe_proxy import UnsafeProxy
    fake_templar = FakeTemplar()
    fake_globals = dict()
    fake_globals['g_var0'] = UnsafeProxy()
    fake_globals['g_var1'] = UnsafeProxy()
    fake_globals['g_var2'] = UnsafeProxy()

    fake_locals = dict()
    fake_locals['var0'] = UnsafeProxy()
    fake_locals['var1'] = UnsafeProxy()
    fake_locals['var2'] = UnsafeProxy()

    j2_vars = AnsibleJ2V

# Generated at 2022-06-13 15:46:35.990120
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import copy
    import jinja2

    # create a fake template, a template object and a Templar object

# Generated at 2022-06-13 15:46:42.869142
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Example data for method test_AnsibleJ2Vars___getitem__

    # NOTE: the data type of key in dictionary is str.
    #       the data type of val in dictionary is bool.
    data = [
        {
            'key': 'ansible_verbosity',
            'val': False
        },
        {
            'key': 'ansible_verbosity',
            'val': True
        }
    ]

    # Test data setup.
    for i in range(len(data)):
        data[i]['var_name'] = data[i]['key']
        data[i]['variable'] = data[i]['val']
        del data[i]['key']
        del data[i]['val']

    # Code example for method test_AnsibleJ2Vars___getitem__

# Generated at 2022-06-13 15:46:51.723569
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    class FakeTemplar(object):
        def __init__(self):
            pass
        def __repr__(self):
            return 'FakeTemplar'
    class FakeGlobals(object):
        def __init__(self):
            pass
        def __repr__(self):
            return 'FakeGlobals'
    class FakeLocals(object):
        def __init__(self):
            pass
        def __repr__(self):
            return 'FakeLocals'

    templar = FakeTemplar()
    globals = FakeGlobals()
    locals = FakeLocals()

    # __init__() only
    v = AnsibleJ2Vars(templar, globals, locals)



#==========================================


# Generated at 2022-06-13 15:46:55.548084
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    t = Templar(loader=None, variables={'a':'b'})
    data = AnsibleJ2Vars(t, {}, {})
    assert len(data) == 1


# Generated at 2022-06-13 15:47:05.692371
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None)

    globals = {
        'test_globals_1': 'test_globals_1_value'
    }

    locals = {
        'test_locals_1': 'test_locals_1_value'
    }

    vars = AnsibleJ2Vars(templar, globals, locals)

    # Only locals variable
    assert 'test_locals_1' in vars
    assert 'test_locals_2' not in vars
    assert 'test_globals_1' not in vars
    assert 'test_globals_2' not in vars

    # All variables

# Generated at 2022-06-13 15:47:13.982605
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader())
    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    host = inventory.get_host('localhost')
    variables = VariableManager(loader=DataLoader(), inventory=inventory)
    variables.extra_vars = {'a': 1, 'b': 2, 'hostvars': HostVars(host=host, variables=variables)}

# Generated at 2022-06-13 15:47:24.431528
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # import ansible.module_utils.basic
    # ansible.module_utils.basic.ANSIBLE_RETRY_FILES_ENABLED = False
    import ansible.playbook.included_file
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    from ansible.vars.reserved import DEFAULT_VAULT_ID_MATCH

    templar = Templar(loader=None, shared_loader_obj=None, variables={},
                      filter_loader=None, available_variables={})
    templar._fail_on_lookup = True

# Generated at 2022-06-13 15:47:27.661925
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    t = Templar()
    v = AnsibleJ2Vars(t, {})
    v['foo'] = 'bar'
    v['baz'] = 'aa'
    v['3'] = 'cc'
    assert sorted(list(v)) == ['3', 'baz', 'foo']


# Generated at 2022-06-13 15:47:35.255970
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import six

    from ansible.template import Templar

    templar = Templar(loader=None)

    v1 = { 'a': 'b' }
    v2 = [ 1, 2, 3 ]
    v3 = { 'a': 'b', 'c': 'd' }
    v4 = { 'a': 'b', 'c': 'd', 'e': 'f' }

    j2vars = AnsibleJ2Vars(templar, v1, locals=v2)

    if not isinstance(j2vars.__iter__(), six.IteratorType):
        raise AssertionError("test_AnsibleJ2Vars__iter__(): failed")

    j2vars = AnsibleJ2Vars(templar, v1, locals=v3)

# Generated at 2022-06-13 15:47:42.511031
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class Templar(object):
        def template(self, obj):
            return obj
    from ansible.constants import DEFAULT_HASH_BEHAVIOUR
    templar = Templar()
    parsing_cache = {
        'version': 1
    }
    jvars = AnsibleJ2Vars(templar,
                          {
                            'vars': {
                                'ansible_hash_behavior': DEFAULT_HASH_BEHAVIOUR
                            }
                          },
                          {
                            'foo': 'foo',
                            'bar': 'bar',
                            'wargo': 'wargo',
                            'nonsense': 'nonsense',
                            'l_baz': 'baz',
                            'jvars': jvars
                          })
    # Test with