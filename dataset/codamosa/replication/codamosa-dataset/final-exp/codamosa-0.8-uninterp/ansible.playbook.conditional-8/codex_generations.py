

# Generated at 2022-06-22 11:40:26.696675
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from units.mock.loader import DictDataLoader


# Generated at 2022-06-22 11:40:32.574484
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    display.debug("Testing Conditional().extract_defined_undefined")

    assert cond.extract_defined_undefined("website_files is defined or ssh_key is defined") == [('website_files', 'is', 'defined'), ('ssh_key', 'is', 'defined')]
    assert cond.extract_defined_undefined("website_files is defined or ssh_key is undefined") == [('website_files', 'is', 'defined'), ('ssh_key', 'is', 'undefined')]
    assert cond.extract_defined_undefined("website_files is undefined") == [('website_files', 'is', 'undefined')]

# Generated at 2022-06-22 11:40:42.954783
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    all_vars = dict(foo='foo!')
    templar = Templar(loader=None, variables=all_vars)

    conditional = Conditional()
    if not hasattr(conditional, '_when'):
        raise Exception("constructor test failed: conditional does not have a _when attribute")
    elif not hasattr(conditional, '_loader'):
        raise Exception("constructor test failed: conditional does not have a _loader attribute")

    # test with missing loader specified

# Generated at 2022-06-22 11:40:46.187473
# Unit test for constructor of class Conditional
def test_Conditional():
    c = Conditional()
    assert c._when == []
    assert c._loader == None
    assert c._name == None


# Generated at 2022-06-22 11:40:59.355580
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    loader = DataLoader()
    tqm = TaskQueueManager(loader=loader, inventory=None, variable_manager=None, stdout_callback=None)
    play_context = PlayContext()
    play = Play()
    block = Block()
    task = Task()
    task.action = 'shell sleep 30'
    block.block = [task]
    play.block = [block]


# Generated at 2022-06-22 11:41:13.600555
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.task import Task
    task_obj = Task()
    conditional = task_obj.extract_defined_undefined("fact_not_is_defined and not fact_is_undefined")
    assert conditional == [('fact_not', 'not is', 'defined'), ('fact_is', 'is', 'undefined')]
    conditional = task_obj.extract_defined_undefined("s|not fact_is_defined and not fact_is_undefined")
    assert conditional == []
    conditional = task_obj.extract_defined_undefined("foo is defined")
    assert conditional == [('foo', 'is', 'defined')]
    conditional = task_obj.extract_defined_undefined("foo is not undefined")
    assert conditional == [('foo', 'is not', 'undefined')]
    conditional

# Generated at 2022-06-22 11:41:23.833333
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    conditional = Conditional()
    class B:
        foo = 'bar'
    class A:
        def __init__(self):
            self.vars = B()
    a = A()
    # TODO: In a first time, test valid conditions
    # TODO: Then, test invalid conditions
    # TODO: Then, test conditions with undefined vars
    # TODO: Then, test conditions with undefined and defined vars
    # TODO: Then, test conditions with undefined vars with ansible_check_mode = True
    # TODO: Then, test conditions with undefined and defined vars with ansbile_check_mode = True


# Generated at 2022-06-22 11:41:36.154310
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    con = Conditional()
    assert con.extract_defined_undefined('a not is defined') == [('a', 'not is', 'defined')]
    assert con.extract_defined_undefined('a not is defined and b not is defined') == [('a', 'not is', 'defined'), ('b', 'not is', 'defined')]
    assert con.extract_defined_undefined('a is undefined or b is undefined') == [('a', 'is', 'undefined'), ('b', 'is', 'undefined')]
    assert con.extract_defined_undefined('a is defined b is undefined') == [('a', 'is', 'defined'), ('b', 'is', 'undefined')]

# Generated at 2022-06-22 11:41:49.080090
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test case imports
    from ansible.playbook import Playbook
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    # Test fixture imports
    from units.mock.loader import DictDataLoader

    # Test fixture data
    inventory_content = dict(
        all=dict(
            hosts=dict(
                test_host=dict(
                    ansible_connection='local',
                    ansible_host='127.0.0.1',
                    ansible_user='test',
                    var1='Hello'
                )
            )
        )
    )

    # Test object creation
    loader = DictDataLoader(inventory_content)
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    templar = Templar(loader=loader, variables={})

    # Test method

# Generated at 2022-06-22 11:41:58.853646
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    conditional = Conditional()
    conditional._loader = DictDataLoader({
        "test.j2": "{{ 'a' if a == 'undef' }}",
    })
    templar = Templar(conditional._loader, variables={})
    all_vars = dict(hostvars=dict(a='value'))

    res = conditional.evaluate_conditional(templar, all_vars)
    assert res is True, 'Expected "True" but got "%s"' % res

    res = conditional.evaluate_conditional(templar, dict(hostvars=dict(a='undef')))
    assert res is False, 'Expected "False" but got "%s"' % res



# Generated at 2022-06-22 11:42:17.626955
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    playbook = """
    ---
    - hosts: all
      tasks:
        - debug: msg="a={{ a }}"
          when: a is defined and (b is defined or not a) and (b is defined or not b)
    """

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['.'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = Templar(loader=loader, variables=variable_manager.get_vars(playbook_dir='./', playbook_vars=dict(a=1, b=2)))

# Generated at 2022-06-22 11:42:27.339728
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager

    loader = 'dummy'
    play_context = PlayContext()
    variable_manager = VariableManager()

    templar = Templar(loader=loader, variables=variable_manager, play_context=play_context)
    c = Conditional(loader=loader)
    c.when = ['dummy1', 'dummy2 and dummy3']
    assert not c.evaluate_conditional(templar, dict(dummy1='dummy1', dummy2='dummy2', dummy3='dummy3'))



# Generated at 2022-06-22 11:42:39.672942
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import Role
    from ansible.playbook.task.include import IncludeTask

    pb = Playbook()
    pb._entries = []


# Generated at 2022-06-22 11:42:49.452267
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    for c, e in (
        ("boo and not foo.bar is undefined", [("foo.bar", "is", "undefined")]),
        ("boo and not hostvars['foo.bar'] is defined", [("hostvars['foo.bar']", "is", "defined")]),
        ("boo and not foo.bar is defined and hostvars[inventory_hostname] is not undefined", [("foo.bar", "is", "defined"), ("hostvars[inventory_hostname]", "is not", "undefined")]),
    ):
        assert e == Conditional().extract_defined_undefined(c)

# unit tests for method Conditional.evaluate_conditional

# Generated at 2022-06-22 11:43:01.961697
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    module_utils_path = 'ansible/module_utils'
    module_utils_loader = 'ansible.module_utils.basic.AnsibleModule'
    if C.DEFAULT_MODULE_UTILS_PATH is not None:
        module_utils_path = C.DEFAULT_MODULE_UTILS_PATH
        if module_utils_path.startswith('./'):
            # make paths relative to the current directory instead of the source tree
            module_utils_path = module_utils_path[2:]
        if ':' in module_utils_path:
            parts = module_utils_path.split(':')
            base_path = parts[0].strip()
            module_utils_path = parts[1].strip()
            with open(base_path, 'rb') as f:
                mod_data = f

# Generated at 2022-06-22 11:43:13.571400
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional_one    = "a is defined and b is defined and c is defined"
    conditional_two    = "a not is defined or b not is undefined or c not is defined"
    conditional_three  = "a is not defined and b is undefined and c is not defined"
    conditional_four   = "a is defined or b is not undefined or c is defined"
    conditional_five   = "a is not defined and b is not undefined and c is not defined"
    conditional_six    = "a is not defined and b is defined and c is not defined"
    conditional_seven  = "a not is defined and b not is undefined and c not is defined"
    conditional_eight  = "a is defined and b is not defined and c is not defined"
    conditional_nine   = "a is defined and b is defined and c is not defined"
    conditional

# Generated at 2022-06-22 11:43:25.447254
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    Test the method: extract_defined_undefined(self, conditional)
    '''
    display.display(u"Test the method: extract_defined_undefined(self, conditional)")

    conditional = 'defined foo'
    if Conditional().extract_defined_undefined(conditional) != [('foo', 'is', 'defined')]:
        display.display(u"Test failed: %s failed" % conditional)

    conditional = 'defined foo or defined bar'
    if Conditional().extract_defined_undefined(conditional) != [('foo', 'is', 'defined')]:
        display.display(u"Test failed: %s failed" % conditional)

    conditional = 'not defined foo or defined bar'

# Generated at 2022-06-22 11:43:37.477721
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.utils.jinja2_only_toplevel import AnsibleJ2Vars
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    # Set up context
    hostvars = HostVars({})
    templar = Templar(loader=None, variables=AnsibleJ2Vars({}), shared_loader_obj=None, template_path=None)

    # Test simple defined/undefined statements
    c = Conditional(loader=None)
    assert c.extract_defined_undefined("test is defined or other is undefined or other is True") == [
        ('test', 'is', 'defined'),
        ('other', 'is', 'undefined'),
    ]

    # Test basic conditional
    # Test simple defined/undefined statements
   

# Generated at 2022-06-22 11:43:49.464006
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from units.mock.loader import DictDataLoader

    def run_eval_cond(cond_list, expected_result):

        hostvars = {
            'foo': {
                'x': 1,
                'y': 'foo',
                'z': [],
                'w': {'a': 'b'}
            },
            'bar': {
                'x': 1,
                'y': [1, 2, 3],
                'z': True,
                'w': False
            },
            'baz': {
                'x': 1,
                'y': None,
                'z': [],
                'w': 'abc'
            }
        }

        t = MyTemplar(dict(inventory={'hostvars': hostvars}))

# Generated at 2022-06-22 11:44:01.606088
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """Test for method evaluate_conditional of class Conditional.

    This method tests that the evaluate_conditional method of class Conditional
    works as expected in valid cases.
    """

    # Test case 1: conditional with multiple boolean values
    test_item = Conditional()
    test_item.when = [True, True]
    assert(test_item.evaluate_conditional(True, True))

    # Test case 2: conditional with variable variable tests
    test_item = Conditional()
    test_item.when = ["ansible_distribution == 'CentOS'", "ansible_distribution == 'Ubuntu'"]
    assert(test_item.evaluate_conditional(True, True))

    # Test case 3: conditional with variable variable tests and boolean values
    test_item = Conditional()

# Generated at 2022-06-22 11:44:28.798196
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert isinstance(Conditional().extract_defined_undefined(''), list)
    assert isinstance(Conditional().extract_defined_undefined('var is defined'), list)
    assert isinstance(Conditional().extract_defined_undefined('var is not defined'), list)
    assert isinstance(Conditional().extract_defined_undefined('var is undefined'), list)
    results = Conditional().extract_defined_undefined('')
    assert len(results) == 0
    results = Conditional().extract_defined_undefined('var is defined')
    assert len(results) == 1
    assert results[0][0] == 'var'
    assert results[0][1] == 'is'
    assert results[0][2] == 'defined'

# Generated at 2022-06-22 11:44:41.137223
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar

    class MyConditional(Conditional):
        pass

    mc = MyConditional()
    mc.when = ['{{ 1 == 1 }}', '{{ False }}', '{{ missing_var is defined }}',
               '{{ "lookup(" in foo_lookups_var }}', '{{ "lookup(" in foo_in_lookups_var }}',
               '{{ foo_defined_var is defined }}', '{{ foo_undefined_var is defined }}',
               "{{ foo_int_var is defined and foo_int_var > 0 }}",
               "{{ foo_int_var is defined and foo_int_var < 0 }}",
               "{{ foo_int_var > 0 }}", "{{ foo_int_var < 0 }}", "{{ foo_int_var }}", ]
    mc.on_failure

# Generated at 2022-06-22 11:44:47.393800
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Note: function name must start with 'test_' in order to be considered by the testsuite

    # This skeleton test suite is just to give a basic idea and be extended later,
    # it is not intended to pass or fail at the moment

    # import the module we want to test
    from ansible.playbook.task_include import TaskInclude
    # We'll use a few other modules here for convenience
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Create a few test objects
    ti = TaskInclude()
    pc = PlayContext()
    vm = VariableManager()
    templar = Templar(variables=vm)
    # set the play context
    ti.set_play_context(pc)

    # Define

# Generated at 2022-06-22 11:44:54.192045
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory_manager = InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)
    variable_manager.set_inventory(inventory_manager)

    conditional = Conditional(loader=loader)
    assert conditional.evaluate_conditional(variable_manager, {}) is True

# Generated at 2022-06-22 11:45:05.877089
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook import PlayBook

    playbook = PlayBook(loader=None)

    cond = Conditional(loader=playbook._loader)
    cond.when = ['false', 'false1', 'true', 'false2']

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    data_loader = DataLoader()
    inventory = InventoryManager(loader=data_loader, sources=['/dev/null'])
    variable_manager = VariableManager(loader=data_loader, inventory=inventory)


# Generated at 2022-06-22 11:45:17.587655
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
   cond = Conditional()

# Generated at 2022-06-22 11:45:21.280374
# Unit test for constructor of class Conditional
def test_Conditional():
    c = Conditional()
    assert c.when == [], "default when not set to empty list"

# Generated at 2022-06-22 11:45:32.944817
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    module_name = 'test_Conditional_evaluate_conditional'
    originating_method = ('{0}.{1}'.format(module_name, test_Conditional_evaluate_conditional.__name__))

    import copy
    import sys
    import unittest

    sys.path.insert(
        0,
        '/var/lib/awx/projects/ansible-testing/library/modules'
    )    

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    from test_conditional import TestConditional
    from test_hosts_and_groups import TestHostsAndGroups

    #test_vars = VariableManager()
    #test_vars.extra_vars = {
    #    "conditional

# Generated at 2022-06-22 11:45:45.500818
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    import os
    import sys

    # The class Conditional uses global variable 'display' which needs to be initialized in this unit-test class
    # global variable 'display' is initialized in module ansible.utils.display
    # In order to initialize 'display' we need to mock module 'ansible.utils.display'
    class MockAnsibleUtilsDisplay:

        def __init__(self):
            self.deprecate = None

    # The class Conditional uses global variable 'C' which needs to be initialized in this unit-test class
    # global variable 'C' is initialized in module ansible.constants
    # In order to initialize 'C' we need to mock module 'ansible.constants'
    class MockAnsibleConstants:

        def __init__(self):
            self.STRIP_

# Generated at 2022-06-22 11:45:57.796560
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    test_data = [
        ("foo is defined", [('foo', 'is', 'defined')]),
        ("foo is not defined", [('foo', 'is', 'defined')]),
        ("foo is defined and bar not is undefined", [('foo', 'is', 'defined'), ('bar', 'not', 'undefined')]),
        ("foo is defined or bar not is undefined", [('foo', 'is', 'defined'), ('bar', 'not', 'undefined')]),
    ]
    for test in test_data:
        result = conditional.extract_defined_undefined(test[0])
        if result != test[1]:
            raise AssertionError("extract_defined_undefined failed on %s, result %s, wanted %s" % (test[0], result, test[1]))
    return

# Generated at 2022-06-22 11:46:42.844232
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    Test method extract_defined_undefined.
    '''

    conditional = Conditional()

    # assert that an invalid conditional is correctly handled
    res = conditional.extract_defined_undefined('not invalid')
    assert res == []

    # assert that a conditional with both defined and undefined
    # constructs is correctly handled
    res = conditional.extract_defined_undefined('foo is defined and bar is not defined')
    assert res == [('foo', 'is', 'defined'), ('bar', 'is not', 'defined')]

    # assert that a conditional with only undefined constructs
    # is correctly handled
    res = conditional.extract_defined_undefined('bar is not defined')
    assert res == [('bar', 'is not', 'defined')]

    # assert that a conditional with only defined constructs
    # is correctly handled
   

# Generated at 2022-06-22 11:46:51.291843
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    m = Conditional()
    assert m.evaluate_conditional({}, {})

    # Test that boolean conditional statements evaluate correctly
    m = Conditional()
    m._when = [False]
    assert m.evaluate_conditional({}, {}) == False

    m = Conditional()
    m._when = [True]
    assert m.evaluate_conditional({}, {}) == True

    # Test that a dict conditional statement evaluates correctly
    m = Conditional()
    m._when = [dict(a=1, b=2)]
    assert m.evaluate_conditional({}, {}) == False

    # Test that a string conditional statement evaluates correctly
    m = Conditional()
    m._when = ['a == "good"']
    assert m.evaluate_conditional({}, {}) == False

    # Test that a string conditional statement evaluates correctly


# Generated at 2022-06-22 11:46:55.825652
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined("") == []
    assert conditional.extract_defined_undefined("{{a}}") == []
    assert conditional.extract_defined_undefined("hostvars[inventory_hostname] is defined") == [("hostvars[inventory_hostname]", "is", "defined")]
    assert conditional.extract_defined_undefined("{{a}} is defined") == []
    assert conditional.extract_defined_undefined("{{a}} is not defined") == []
    assert conditional.extract_defined_undefined("a is defined") == [("a", "is", "defined")]
    assert conditional.extract_defined_undefined("a is not defined") == [("a", "is", "not", "defined")]
    assert conditional.extract_

# Generated at 2022-06-22 11:47:03.675188
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # This is needed to handle loading of included files from task
    from ansible.playbook.task_include import TaskInclude
    TaskInclude._load_role = lambda x, y, z, build_role_dependencies=False: (None, None)
    TaskInclude._get_role_dependencies = lambda x, y, z: []
    TaskInclude._load_included_file = lambda x, y, z, role_name=None, task_include=None, is_handler=False, validate_filters=False: None

    class MyConditional(Conditional):
        pass


# Generated at 2022-06-22 11:47:12.103730
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Note: the code path that is actually tested by this unit test is quite limited
    # at this point.
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task

    variable_manager = VariableManager()
    loader = DataLoader()

    variable_manager.set_inventory(InventoryManager(loader=loader, sources='localhost,'))
    variable_manager.extra_vars = dict(var='var')

    task = Task()
    task._variable_manager = variable_manager
    task._loader = loader

    # Note: the templar is only one of the dependencies of Conditional.evaluate_conditional.
    # It would be better to initialize

# Generated at 2022-06-22 11:47:20.161497
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    loader = DictDataLoader({'test.yml': 'test'})
    templar = Templar(loader=loader, variables={'test': 'test'}, vault_secrets=vault)
    conditional = Conditional(loader=loader)
    result = conditional.evaluate_conditional(templar, None)
    assert result is True

    # simple test of true/false strings
    conditional = Conditional(loader=loader)
    conditional.when = ['test']
    assert conditional.evaluate_conditional(templar, None) is True
    conditional.when = ['other']
    assert conditional.evaluate_conditional(templar, None) is False

    # simple test of true/false boole

# Generated at 2022-06-22 11:47:31.158067
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext

    c = Conditional()

    # test normal path

    # when set but empty: True
    c.when = []
    assert c.evaluate_conditional(PlayContext(), dict())

    # when set but valid: True
    c.when = [True]
    assert c.evaluate_conditional(PlayContext(), dict())

    # when set but invalid: False
    c.when = [False]
    assert not c.evaluate_conditional(PlayContext(), dict())

    # complex conditional
    c.when = ['1 is 2 or False']
    assert not c.evaluate_conditional(PlayContext(), dict())

    # when set but invalid and multiple conditionals: False
    c.when = ['1 is 2', '10 is not 10', '0 == 0']
    assert not c

# Generated at 2022-06-22 11:47:39.904505
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:47:52.517279
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    expected = {
        'hostvars[inventory_hostname] == inventory_hostname':
            'True'
    }
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from collections import namedtuple
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import wrap_var

# Generated at 2022-06-22 11:48:01.677164
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    case1 = "hostvars['foo'] is not defined"
    result = Conditional().extract_defined_undefined(case1)
    assert result == [('hostvars[\'foo\']', 'is not', 'defined')]

    case2 = """defined(my_var)
    hostvars['foo'] is not defined"""
    result = Conditional().extract_defined_undefined(case2)
    assert result == [('hostvars[\'foo\']', 'is not', 'defined')]

    case3 = """
    not my_var
    hostvars['foo'] is not defined"""
    result = Conditional().extract_defined_undefined(case3)
    assert len(result) == 0


# Generated at 2022-06-22 11:49:20.720490
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from unittest import TestCase
    from ansible.playbook.conditional import Conditional

    class TestConditional(Conditional):
        pass

    test_conditional = TestConditional()


# Generated at 2022-06-22 11:49:27.762934
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    m = Conditional()

# Generated at 2022-06-22 11:49:38.617130
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar


# Generated at 2022-06-22 11:49:50.041468
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestObj(Conditional):
        pass
    # create an object of the class and make Ds attribute to None
    obj = TestObj()
    setattr(obj, '_ds', None)
    obj._loader = None
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    # create a object of the class DataLoader
    dataloader = DataLoader()
    # create a object of the class VariableManager
    variable_manager = VariableManager()
    # create a object of the class Templar
    templar = Templar(loader=dataloader, variables=variable_manager)
    # create a dict of the all_vars

# Generated at 2022-06-22 11:50:01.332662
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.base import Base
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar

    import jinja2

    my_vars = dict(
        foo='foo',
        bar='bar'
    )

    conditional = 'foo == bar'

    b_o = Base()
    b_o.vars = my_vars

    p_o = Play()
    p_o.vars = my_vars

    t_o = Task()
    t_o.vars = my_vars

    t_o.when = conditional
    p_o.when = conditional
    b_o.when = conditional

    t_o._add_parent(p_o)

# Generated at 2022-06-22 11:50:08.747844
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    module = collections.namedtuple('MyModule', ['params'])
    module.params = dict()
