

# Generated at 2022-06-22 11:40:27.743816
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    import sys
    import os
    import pytest
    sys.modules["ansible"] = type("fake_ansible", (object,), {"__version__":"1"})
    sys.modules["ansible.module_utils"] = type("fake_ansible_module_util", (object,), {"__version__":"1"})
    os.environ['ANSIBLE_VERSION_WARNING'] = "NO"

    from ansible.playbook import Playbook
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager


# Generated at 2022-06-22 11:40:33.195890
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.module_utils.six.moves import StringIO
    import sys

    target = Conditional()

    # write test simple true and false conditions
    test_list = [
        "\"foo\" == \"bar\"",
        "True",
        "False",
    ]

    # test 1 (false conditions)
    sys.stdout = io = StringIO()
    res = target.evaluate_conditional("", test_list)
    sys.stdout = sys.__stdout__
    assert res == False

    # test 2 (true conditions)
    sys.stdout = io = StringIO()
    test_list = [
        "\"foo\" != \"bar\"",
        "True",
    ]
    res = target.evaluate_conditional("", test_list)
    sys.stdout = sys.__stdout

# Generated at 2022-06-22 11:40:42.580650
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Initializing test object
    conditional_object = Conditional()

    # Positive test
    cond1 = "ansible_os_family is defined and ansible_os_family!='Windows'"
    desired_result1 = [('ansible_os_family', 'is', 'defined'), ('ansible_os_family', '!=', 'Windows')]
    result1 = conditional_object.extract_defined_undefined(cond1)
    assert desired_result1 == result1

    # Negative test
    cond2 = "ansible_os_family is defined ansible_os_family!='Windows'"
    desired_result2 = []
    result2 = conditional_object.extract_defined_undefined(cond2)
    assert desired_result2 == result2

# Generated at 2022-06-22 11:40:50.621622
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    conditional_instance = Conditional()

    # TODO: write unit tests
    assert conditional_instance.extract_defined_undefined('True') == []
    assert conditional_instance.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert conditional_instance.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert conditional_instance.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]
    assert conditional_instance.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]

# Generated at 2022-06-22 11:40:57.798471
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    myconditional = "foo is defined and (bar is defined or baz is not defined) and spam is defined"

    defined_undefined = Conditional.extract_defined_undefined(None, myconditional)

    assert defined_undefined == [('bar', 'is', 'defined'), ('foo', 'is', 'defined'), ('spam', 'is', 'defined')]

# Generated at 2022-06-22 11:41:11.039252
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # We do not use the Conditional class directly but we use the AnsibleModule
    # which has Conditional as parent class
    from ansible.module_utils.basic import AnsibleModule
    conditional = Conditional(AnsibleModule)

    # basic testcase
    conditional_expression = 'a is defined and b is defined'
    expect = [('a', 'is', 'defined'), ('b', 'is', 'defined')]
    result = conditional.extract_defined_undefined(conditional_expression)
    assert expect == result

    # test with whitespace
    conditional_expression = '    a    is defined   and b is defined   '
    expect = [('a', 'is', 'defined'), ('b', 'is', 'defined')]
    result = conditional.extract_defined_undefined(conditional_expression)

# Generated at 2022-06-22 11:41:21.909688
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    # if a regex contains 'is defined' or 'is not defined', it
    # should be extracted
    assert c.extract_defined_undefined('something is defined') == [('something', 'is', 'defined')]
    assert c.extract_defined_undefined('something is not defined') == [('something', 'is not', 'defined')]
    # if a regex contains 'is not defined', it should be extracted
    assert c.extract_defined_undefined('hostvars["something"] is defined') == [('hostvars["something"]', 'is', 'defined')]
    assert c.extract_defined_undefined('hostvars["something"] is not defined') == [('hostvars["something"]', 'is not', 'defined')]
    # if a regex contains 'is undefined', it should

# Generated at 2022-06-22 11:41:31.792684
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.template.safe_eval import unsafe_eval

    class MyClass(Conditional):
        pass

    m = MyClass()
    assert m.evaluate_conditional(None, None) is True

    m.when = ""
    assert m.evaluate_conditional(None, None) is True

    m.when = None
    assert m.evaluate_conditional(None, None) is True

    m.when = True
    assert m.evaluate_conditional(None, None) is True

    m.when = False
    assert m.evaluate_conditional(None, None) is False

    m.when = 'false'
    assert m.evaluate_conditional(None, None) is False

    m.when = 'true'
    assert m.evaluate_

# Generated at 2022-06-22 11:41:40.501145
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    # Single definition
    conditional = 'defined'
    definition = [('defined', 'is', 'defined')]
    obj = Conditional()
    res = obj.extract_defined_undefined(conditional)
    assert res == definition

    # Single definition with extra whitespaces
    conditional = '  defined  '
    definition = [('defined', 'is', 'defined')]
    obj = Conditional()
    res = obj.extract_defined_undefined(conditional)
    assert res == definition

    # Single definition, delimited with parenthesis
    conditional = '(((defined)))'
    definition = [('defined', 'is', 'defined')]
    obj = Conditional()
    res = obj.extract_defined_undefined(conditional)
    assert res == definition

    # Single definition, delimited with parenthesis, with extra

# Generated at 2022-06-22 11:41:50.841575
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    conditional = 'not ansible_os_family is defined or ansible_os_family != "RedHat"'
    expected_result = [['ansible_os_family', 'is', 'defined'], ['ansible_os_family', '!=', '"RedHat"']]
    assert cond.extract_defined_undefined(conditional) == expected_result

    conditional = 'not ansible_os_family is undefined or ansible_os_family != "RedHat"'
    expected_result = [['ansible_os_family', 'is', 'undefined'], ['ansible_os_family', '!=', '"RedHat"']]
    assert cond.extract_defined_undefined(conditional) == expected_result


# Generated at 2022-06-22 11:42:08.342368
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import sys
    import tempfile
    class TestConditional():
        _defs =  {'v': 'x', 'y': 'o'}

        def __init__(self):
            self.loader = DictDataLoader({'test.yml': '{% for x in [1,2] %} {{ x }}{% endfor %}'})
            self.when = []

        def evaluate_conditional(self, templar, all_vars):
            return Conditional.evaluate_conditional(self, templar, all_vars)

        def _get_ds(self):
            return self._ds

        def _set_ds(self, ds):
            self._ds = ds

        _ds = property(_get_ds, _set_ds)


# Generated at 2022-06-22 11:42:14.424614
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('defined foo') == [('foo', 'is', 'defined')]
    assert c.extract_defined_undefined('defined foo and bar is not undefined') == [('foo', 'is', 'defined'), ('bar', 'is not', 'undefined')]
    assert c.extract_defined_undefined('something else') == []


# Generated at 2022-06-22 11:42:26.491540
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from collections import namedtuple
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.inventory.manager
    import ansible.vars.variable_manager

    # Create namedtuples to hold variables in a simple manner
    HostVars = namedtuple('HostVars', ['hostname1', 'hostname2'])
    GroupVars = namedtuple('GroupVars', ['group1', 'group2', 'all'])
    Vars = namedtuple('Vars', ['hostvars', 'group_names'])

# Generated at 2022-06-22 11:42:31.098039
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import tempfile
    import os

    fh, path = tempfile.mkstemp()
    os.close(fh)
    os.remove(path)

    # In order to generate the all_vars, we need an inventory.
    # This is really ugly, we would need to extend this test
    # if we change the way the inventory is initialized.
    play_ds = dict(
        inventory=dict(
            plugin="auto",
            host_list=path,
            groups=dict(
                group1=["host1"],
                group2=["host2"],
            ),
            host_pattern="all",
            parser="yaml",
            cache=dict(
                _cache=False,
                enabled=False,
                expire=0
            ),
            cache_connection=None,
        )
    )

    cond

# Generated at 2022-06-22 11:42:42.477352
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('') == []
    assert c.extract_defined_undefined('1==1') == []
    assert c.extract_defined_undefined('defined') == []
    assert c.extract_defined_undefined('1==1 and defined') == []
    assert c.extract_defined_undefined('1==1 and not defined') == []
    assert c.extract_defined_undefined('1==1 and hostvars is defined') == []
    assert c.extract_defined_undefined('1==1 and hostvars is undefined') == []
    assert c.extract_defined_undefined('hostname is defined') == [('hostname', 'is', 'defined')]

# Generated at 2022-06-22 11:42:54.235902
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    assert conditional_value_1(play_context=PlayContext(), templar=Templar()) == True
    assert conditional_value_2(play_context=PlayContext(), templar=Templar()) == True
    assert conditional_value_3(play_context=PlayContext(), templar=Templar()) == True
    assert conditional_value_4(play_context=PlayContext(), templar=Templar()) == True
    assert conditional_value_5(play_context=PlayContext(), templar=Templar()) == True
    assert conditional_value_6(play_context=PlayContext(), templar=Templar()) == True

# Generated at 2022-06-22 11:43:04.185782
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    # Testing extract_defined_undefined method

    # passing a conditional with "not is defined"
    from ansible.playbook.base import Base
    conditional = Base()
    res = conditional.extract_defined_undefined('my_var is not defined')
    if res != [('my_var', 'is', 'not defined')]:
        raise AssertionError("failed to extract_defined_undefined")

    # passing a conditional with multiple "not is defined"
    conditional = Base()
    res = conditional.extract_defined_undefined('my_var is not defined and my_var2 is not defined')
    if res != [('my_var', 'is', 'not defined'), ('my_var2', 'is', 'not defined')]:
        raise AssertionError("failed to extract_defined_undefined")

    # passing a

# Generated at 2022-06-22 11:43:16.152680
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    import sys
    import os
    import pytest
    mypath = os.path.dirname(os.path.realpath(__file__))
    test_file = mypath + "/../../../test/units/modules/test_extract_defined_undefined.txt"
    with open(test_file, "r") as f:
        unit_test_lines = f.readlines()

    for line in unit_test_lines:
        test_line = line.split("#")[0]
        if test_line:
            line_split = test_line.split("|")
            assert len(line_split) > 1
            condition = line_split[0].strip()
            expected = line_split[1].strip()
            result = Conditional().extract_defined_undefined(condition)

# Generated at 2022-06-22 11:43:21.262591
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.template import Templar
    import ansible.parsing.dataloader

    loader = ansible.parsing.dataloader.DataLoader()
    variable_manager = ansible.vars.manager.VariableManager()
    variable_manager.extra_vars = {'test_var': 'foo', 'test_var2': 'bar'}
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=play))


# Generated at 2022-06-22 11:43:31.771484
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:43:50.862770
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    data = conditional.extract_defined_undefined("foo is defined and (bar is not defined or bar == True)")
    assert data == [
        ('foo', 'is', 'defined'),
        ('bar', 'is not', 'defined'),
    ]

# Generated at 2022-06-22 11:44:00.147883
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    assert cond.extract_defined_undefined("foo is defined") == [("foo", "is", "defined")]
    assert cond.extract_defined_undefined("foo is not defined") == [("foo", "is not", "defined")]

    assert cond.extract_defined_undefined("foo is defined or bar is not defined") == [("foo", "is", "defined"), ("bar", "is not", "defined")]
    assert cond.extract_defined_undefined("foo is defined and bar is not defined") == [("foo", "is", "defined"), ("bar", "is not", "defined")]

    # tests with hostvars

# Generated at 2022-06-22 11:44:07.021594
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib

    variable_manager = VariableManager()
    variable_manager._extra_vars = { 'some_var': 'some_value', 'foo': 'bar' }
    variable_manager._vault_secrets = [ VaultSecret( 'secret string', 'secret', 'testvault', False ) ]
    variable_manager._vault_pass = VaultLib([])

    play_context = PlayContext()

    c = Conditional(loader=None)
    t = Templar(loader=None, variables=variable_manager, play_context=play_context)

    # test safe_eval

# Generated at 2022-06-22 11:44:13.920410
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import unittest2 as unittest

    class TestException(Exception):
        pass

    class TestCase(unittest.TestCase):

        def test_bogus_conditional(self):
            c = Conditional()
            ret = c.evaluate_conditional('bogus', {})
            assert ret == 'bogus', 'bogus conditional should evaluate as such: %s' % ret

        def test_match_undefined_variable(self):
            c = Conditional()
            ret = c.evaluate_conditional('some_variable is defined', {'some_variable': 'foo'})
            assert ret == True, 'some_variable is defined should evaluate as True: %s' % ret

        def test_mismatch_undefined_variable(self):
            c = Conditional()
            ret = c.evaluate_

# Generated at 2022-06-22 11:44:26.681678
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    extra_vars = dict(foo='one', bar='two')
    play_context = PlayContext(extra_vars=extra_vars)

    def _test(conditional, expected):
        display.display('  conditional: "%s" (%s)' % (conditional, type(conditional)), u'info')
        t = Task()
        t.when = [conditional]
        result = t.evaluate_conditional(Task.datastructure_to_safe_templar(t, play_context), extra_vars)
        assert result is expected, '%r expected, got %r' % (expected, result)

    _test('foo == "one"', True)


# Generated at 2022-06-22 11:44:39.144195
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    vm = VariableManager()
    templar = Templar(loader=None, variables=vm)

    all_vars = dict(a=1, b='foo', c='bar', d=dict(x='y'))

    # check the basic logic of the method, the actual evaluation
    # is done in _check_conditional
    conditional = dict(when=[
        'a > 1',
        'b == "foo"',
        'a + b == "1foo"',
    ])

    conditional_obj = Conditional()
    for attr, value in conditional.items():
        setattr(conditional_obj, attr, value)

    conditional_obj.evaluate_conditional(templar, all_vars)

# Generated at 2022-06-22 11:44:50.976269
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined("test not is undefined") == [("test","not is","undefined")]
    assert c.extract_defined_undefined("test is undefined") == [("test","is","undefined")]
    assert c.extract_defined_undefined("test is defined") == [("test","is","defined")]
    assert c.extract_defined_undefined("test is not defined") == [("test","is not","defined")]
    assert c.extract_defined_undefined("A and B not is undefined") == [("A","and","B"),("B","not is","undefined")]
    assert c.extract_defined_undefined("A or B is undefined") == [("A","or","B"),("B","is","undefined")]

# Generated at 2022-06-22 11:45:02.556503
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional_test = Conditional()
    assert conditional_test.extract_defined_undefined(
            'ansible_os_family is defined and ansible_os_family != "RedHat"'
            ) == [('ansible_os_family', 'is', 'defined')]
    assert conditional_test.extract_defined_undefined(
            'ansible_os_family not is defined and ansible_os_family != "RedHat"'
            ) == [('ansible_os_family', 'not is', 'defined')]
    assert conditional_test.extract_defined_undefined(
            'ansible_os_family is not defined and ansible_os_family != "RedHat"'
            ) == [('ansible_os_family', 'is not', 'defined')]
    assert conditional_test.extract_defined_und

# Generated at 2022-06-22 11:45:08.317707
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager

    # Make a mock object for the conditional
    class MockConditional(Conditional):
        def __init__(self):
            self._ds = {
                'path': 'whatever',
                '_lineage': [],
            }

# Generated at 2022-06-22 11:45:19.780451
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:45:47.458573
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # test setup
    class TestClass:
        class C(Conditional):
            def __init__(self, loader=None):
                self._loader = loader

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])
    templar = inventory.get_basedir()

    # test case 1
    # condition: "not result.rc"
    # defined vars: {"result": {"rc": 0}}
    # expected result: False
    test_class_obj = TestClass.C(loader=loader)
    test_class_obj._when = ["not result.rc"]

# Generated at 2022-06-22 11:45:59.348115
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager(loader=None)
    variable_manager.extra_vars = dict(
        first='good', second='good', third='bad', fourth='good',
        other='good', numbers=['one', 'two', 'three'],
        some_dict=dict(a='good', b='good'),
        some_list=['good', 'good'],
        some_dict_with_list=dict(a='good', b=['good', 'good'])
    )
    variable_manager.set_nonpersistent_facts(variable_manager.extra_vars)
    templar = Templar(loader=None, variables=variable_manager)


# Generated at 2022-06-22 11:46:10.093349
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test simple True
    conditional = Conditional()
    setattr(conditional, 'when', ['test_var == "test_value"'])
    result = conditional.evaluate_conditional(
        'test_var',
        {'test_var': 'test_value'},
        loader=None,
    )
    assert result

    # Test simple False
    conditional = Conditional()
    setattr(conditional, 'when', ['test_var == "test_value"'])
    result = conditional.evaluate_conditional(
        'test_var',
        {'test_var': 'other_value'},
        loader=None,
    )
    assert not result

    # Test simple False with undefined variable
    conditional = Conditional()
    setattr(conditional, 'when', ['test_var == "test_value"'])


# Generated at 2022-06-22 11:46:20.116148
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    result = c.extract_defined_undefined("hostvars[inventory_hostname] is defined")
    assert result[0][0] == "hostvars[inventory_hostname]", result
    assert result[0][1] == "is", result
    assert result[0][2] == "defined", result

    result = c.extract_defined_undefined("some_var is not defined")
    assert result[0][0] == "some_var", result
    assert result[0][1] == "is not", result
    assert result[0][2] == "defined", result

    result = c.extract_defined_undefined("x is undefined")
    assert result[0][0] == "x", result
    assert result[0][1] == "is", result

# Generated at 2022-06-22 11:46:29.605834
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class ConditionalTest(Conditional):
        def __init__(self, loader=None):
            self.when = ['{{foo}}']
            self._loader = loader
            super(Conditional, self).__init__()

    loader = DictDataLoader({
        "vars/main.yml": "{foo: 3 == 3}",
    })

    display = Display()
    cond_test = ConditionalTest(loader)

    all_vars = dict()
    all_vars["foo"] = "bar"

    templar = Templar(loader=loader, variables=all_vars)

    assert cond_test.evaluate_conditional(templar, all_vars) == True


# Unit tests for method _check_conditional of class Conditional

# Generated at 2022-06-22 11:46:40.371306
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display = Display()
    display.verbosity = 3
    assert Conditional().evaluate_conditional(None, {}, {}, {'when': [True]})
    assert Conditional().evaluate_conditional(None, {}, {}, {'when': [False]}) is False
    assert Conditional().evaluate_conditional(None, {}, {}, {'when': ['True']})
    assert Conditional().evaluate_conditional(None, {}, {}, {'when': ['False']}) is False
    assert Conditional().evaluate_conditional(None, {}, {}, {'when': ['False', 'False', 'True']})
    assert Conditional().evaluate_conditional(None, {}, {}, {'when': ['False', 'False', 'False']}) is False

    # define a variable called 'foo'
    assert Conditional().evaluate_

# Generated at 2022-06-22 11:46:48.548527
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    pc = PlayContext()

    yaml_template = {"when": "ansible_eth0 is defined"}
    conditional = Conditional()

    templar = Templar(loader=None, variables={'hostvars':{}}, shared_loader_obj=None)

    display.verbosity = 3

    if conditional.evaluate_conditional(templar, yaml_template):
        print("Test Pass")
    else:
        print("Test Failed")


# Generated at 2022-06-22 11:46:59.007629
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.module_utils.six import StringIO

    # Mock objects for function jinja2.Compiler.compile
    def compile_mock(self):
        return None

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    templar = Templar(loader=None, variables={})
    templar._available_variables = {'foobar': 'somevalue'}
    templar.environment.compile = compile_mock

    # Case 1: Test when the conditional is instance of bool
    conditional_object = Conditional(loader=None)
    assert conditional_object.evaluate_conditional(templar, templar._available_variables)

    # Case 2: Test when the conditional is a non empty string

# Generated at 2022-06-22 11:47:11.090816
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    Test method extract_defined_undefined
    '''

    display.display("Conditional_extract_defined_undefined")

    conditional = Conditional()

    # Test all conditions
    defined = conditional.extract_defined_undefined("result is not defined")
    result = False
    if defined[0][0] == 'result' and defined[0][1] == 'not is':
        result = True
    assert result == True

    defined = conditional.extract_defined_undefined("result is defined")
    result = False
    if defined[0][0] == 'result' and defined[0][1] == 'is':
        result = True
    assert result == True

    defined = conditional.extract_defined_undefined("result is not undefined")
    result = False

# Generated at 2022-06-22 11:47:24.171111
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined('hostvars["foo"] is undefined') == [('hostvars["foo"]', 'is', 'undefined')],\
            "conditionnal.extract_defined_undefined('hostvars[\"foo\"] is undefined') gives %s, not %s as expected" \
            % (conditional.extract_defined_undefined('hostvars["foo"] is undefined'), [('hostvars["foo"]', 'is', 'undefined')])

# Generated at 2022-06-22 11:48:02.543349
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = '''(hostvars['ansible_default_ipv4']['gateway'] == "192.168.1.1" or hostvars['ansible_default_ipv4']['gateway'] == "192.168.1.2") and
                    ((inventory_hostname in groups['sabanew'] and hostvars['ansible_default_ipv4']['gateway'] == "192.168.1.1") or
                    (inventory_hostname in groups['sabav6'] and hostvars['ansible_default_ipv4']['gateway'] == "192.168.1.2"))'''

    result = Conditional().extract_defined_undefined(conditional)

# Generated at 2022-06-22 11:48:13.417402
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory=None)
    variable_manager.extra_vars = dict(a=1, b=2, c=3)
    templar = Templar(loader=None, variables=variable_manager)

    # MAKE SURE CONDITIONAL WORKS WITH LIST OR STRING
    conditional = 'hostvars[inventory_hostname]["ansible_%s"] == "eth0"' % (C.DEFAULT_MISSING_VARIABLE_NAME)
    result = Conditional()._check_conditional(conditional, templar, variable_manager.get_vars(play=None))
    assert result


# Generated at 2022-06-22 11:48:21.037975
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Create a Conditional class and instantiate it
    test_class = Conditional()

    # use extract_defined_undefined to extract from a simple string
    conditional = 'foo is defined'
    result = test_class.extract_defined_undefined(conditional)
    assert result == [('foo', 'is', 'defined')]

    # use extract_defined_undefined to extract from a slightly more complex string
    conditional = 'bar not is defined and foo is defined and name is foo'
    result = test_class.extract_defined_undefined(conditional)
    assert result == [('bar', 'not is', 'defined'), ('foo', 'is', 'defined')]

    # use extract_defined_undefined to extract from an even more complex string
    conditional = 'bar not is defined and foo is undefined and name is foo'
   

# Generated at 2022-06-22 11:48:33.713703
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:48:46.112166
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import unittest
    import sys

    # Mock
    class MockTemplar:

        def __init__(self):
            self.env = Environment()

        @staticmethod
        def is_template(conditional):
            return False

        @staticmethod
        def template(conditional, disable_lookups):
            # Mock
            if conditional == 'a == "b"':
                return 'b'
            elif conditional == 'a == "c"':
                return 'c'

            return conditional

    class MockConditional(Conditional):

        def __init__(self, when):
            self.when = when
            self._loader = None

    class TestConditional(unittest.TestCase):

        def setUp(self):
            self.templar = MockTemplar()
            self.conditional = MockCond

# Generated at 2022-06-22 11:48:56.895012
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)
    templar = Templar(loader=loader, variable_manager=variable_manager)

    conditional = Conditional()

    res = conditional.evaluate_conditional(templar, dict())
    assert res == True

    conditional.when = ['test']
    res = conditional.evaluate_conditional(templar, dict())
    assert res == False

    conditional.when = ['test', 'test2']
    res = conditional.evaluate_cond

# Generated at 2022-06-22 11:49:08.602253
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    ''' unit tests for method evaluate_conditional of class Conditional '''

    # noinspection PyUnresolvedReferences
    from ansible.playbook.play_context import PlayContext
    from ansible.template.safe_eval import safe_eval

    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import filter_loader

    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

# Generated at 2022-06-22 11:49:21.099410
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import mock
    import sys
    import unittest

    # Mock the display class of the Display module
    display_mock = mock.Mock(spec=Display())
    display_patch = mock.patch.object(sys.modules['ansible.utils.display'], 'Display', return_value=display_mock)
    display_patch.start()

    # Mock the templar class of the Templar module
    templar_mock = mock.Mock(spec=Templar())
    templar_mock.template.return_value = 'result'
    templar_mock.is_template.return_value = False
    templar_mock.available_variables = {}

    # Object under test
    conditional = Conditional()

    # Test evaluate_conditional with True

# Generated at 2022-06-22 11:49:32.654548
# Unit test for constructor of class Conditional
def test_Conditional():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    loader = 'setup'
    variable_manager = 'var_manager_setup'
    all_vars = dict()

    conditional = Conditional()
    rd = RoleDefinition()
    t = Task()
    b = Block()
    pc = PlayContext()

    conditional.set_loader(loader)
    conditional.set_variable_manager(variable_manager)
    conditional.set_play_context(pc)
    conditional.load(rd, t, b, all_vars)
    conditional.post_validate(templar=None, all_vars=all_vars)

    assert conditional._

# Generated at 2022-06-22 11:49:44.421656
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Testing the evaluate_conditional method of Conditional class
    '''
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    ###################
    # Test Setup
    ###################
    class TestFunc():
        def __init__(self):
            # Simulate class vars
            self.when = []
            self._loader = DataLoader()
            self._templar = VariableManager()

        def test(self, conditional, all_vars):
            self.when.append(conditional)
            display.debug("Testing '%s' on vars %r" % (self.when[0], all_vars))