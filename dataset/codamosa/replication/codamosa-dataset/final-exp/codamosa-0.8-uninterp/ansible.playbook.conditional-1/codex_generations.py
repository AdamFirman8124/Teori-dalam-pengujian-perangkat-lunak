

# Generated at 2022-06-22 11:40:25.590697
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    def replace_host_var_in_str(str):
        """ replace host_var in str with a real value """
        return str.replace('host_var', 'foo')

    class TestModule(object):
        pass

    class TestPlay(object):
        def __init__(self, loader=None):
            self.hostvars = {'localhost': {'foo': 42}}
            self.vars = self.hostvars['localhost']

    class TestTask(Conditional):
        def __init__(self, loader=None):
            self.name = 'TestTask'
            self.callbacks = TestModule()
            self.callbacks.warn = lambda x: None
            self.callbacks.set_fact = lambda x: None
            self.callbacks.set_stats = lambda x: None


# Generated at 2022-06-22 11:40:28.905302
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar

    # Just need to make sure the templar object will exist
    assert Conditional().evaluate_conditional(Templar(loader=None), None)

# Generated at 2022-06-22 11:40:39.469173
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play_context import PlayContext

    c = Conditional()
    assert c.extract_defined_undefined('foobar') == []
    assert c.extract_defined_undefined('hostvars["foo"] is defined') == [('hostvars["foo"]', 'is', 'defined')]

    # Ensure we can use yaml-style and json-style quoting in tests.  Make sure we don't pick up
    # unquoted variable names here
    assert c.extract_defined_undefined('hostvars[\'foo\'] is defined') == [('hostvars[\'foo\']', 'is', 'defined')]
    assert c.extract_defined_undefined('hostvars["foo"] is defined') == [('hostvars["foo"]', 'is', 'defined')]

# Generated at 2022-06-22 11:40:48.737350
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import ansible.template
    import ansible.vars
    import ansible.utils


# Generated at 2022-06-22 11:41:01.386384
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import imp
    import os
    import sys

    # import module snippets
    f, filename, desc = imp.find_module('_text', [os.path.join(os.path.dirname(__file__), '..', 'module_utils')])
    _text = imp.load_module('_text', f, filename, desc)
    f, filename, desc = imp.find_module('common', [os.path.join(os.path.dirname(__file__), '..', 'plugins', 'action')])
    common = imp.load_module('common', f, filename, desc)
    f, filename, desc = imp.find_module('basic', [os.path.join(os.path.dirname(__file__), '..', 'plugins', 'action')])

# Generated at 2022-06-22 11:41:15.323006
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.base import Base

    class Test(Base, Conditional):
        pass

    test = Test()
    a = test.extract_defined_undefined("hostvars['foo']['bar'] is defined")
    assert a == [('hostvars[foo][bar]', 'is', 'defined')]
    b = test.extract_defined_undefined("hostvars['foo']['bar'] is not defined")
    assert b == [('hostvars[foo][bar]', 'is not', 'defined')]
    c = test.extract_defined_undefined("defined(foo)")
    assert c == [('foo', 'is', 'defined')]
    d = test.extract_defined_undefined("not defined(foo)")

# Generated at 2022-06-22 11:41:25.449313
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # -----
    # Setup
    # -----

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()

    # normal_vars contains all the variables associated with a task,
    # such as host, ansible_ssh_host, ansible_ssh_port, etc.
    normal_vars = dict()
    normal_vars['omit'] = 'omit'
    normal_vars['host_specific_var'] = 'host specific value'
    all_vars = {'ansible_all_vars': normal_vars}

    templar = Templar(loader=loader, variables=variable_manager)
    conditional_test = Conditional(loader=loader)

# Generated at 2022-06-22 11:41:37.432346
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:41:49.936141
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    c = Conditional()
    class test_templar:
        def __init__(self):
            self.environment = None
            self.available_variables = None
        def is_template(self, conditional):
            return False
        def template(self, conditional, disable_lookups = None):
            return conditional

    templar = test_templar()
    all_vars = {'x': 1, 'y': '', 'z': False}

# Generated at 2022-06-22 11:41:50.809513
# Unit test for constructor of class Conditional
def test_Conditional():
    pass

# Generated at 2022-06-22 11:42:04.455231
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Test 1: undefined variable
    conditional = 'some_var is undefined'
    c = Conditional()
    assert c.extract_defined_undefined(conditional) == [('some_var', 'is', 'undefined')]

    # Test 2: defined variable
    conditional = 'some_var is defined'
    assert c.extract_defined_undefined(conditional) == [('some_var', 'is', 'defined')]

    # Test 3: not undefined variable
    conditional = 'some_var is not undefined'
    assert c.extract_defined_undefined(conditional) == [('some_var', 'is', 'undefined')]

    # Test 4: not defined variable
    conditional = 'some_var is not defined'

# Generated at 2022-06-22 11:42:11.889034
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.utils.vars import combine_vars

    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    import ansible.constants as C

    # Preparing enviroment
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    play_context = PlayContext(variable_manager=variable_manager, loader=loader)
    variable_manager.set_inventory(inventory)
    task = Task()

    test_main = Conditional()
    test_

# Generated at 2022-06-22 11:42:13.328247
# Unit test for constructor of class Conditional
def test_Conditional():
    assert Conditional() is not None


# Generated at 2022-06-22 11:42:25.743160
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:42:35.425625
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # -- Setup
    class TestClass(Conditional):
        def __init__(self):
            self._ds = dict()
            self._ds['name'] = 'test.yml'

    conditional_obj = TestClass()

# Generated at 2022-06-22 11:42:48.981554
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import PlayBook

    loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-22 11:42:58.633518
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Simple variable tests, no 'not is', no 'is not'
    c = Conditional()
    for c in ['a is defined',
              'bar is defined',
              'baz is undefined',
              'bar is defined and bar is defined',
              'baz is undefined and foo is undefined',
              'bar is defined and (baz is undefined or foo is undefined)',
              'bar is defined or baz is undefined and foo is undefined',
              'not (f is defined and g is defined) and x is defined',
              'not f is defined and g is defined and x is defined',
              'not (f is defined) and g is defined and x is defined',
              'not (f is defined and g is defined and x is defined)']:
        print(c)
        (variable, logic, state) = c.extract_defined_und

# Generated at 2022-06-22 11:43:05.648912
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Create an instance of class Conditional
    conditional_test = Conditional()
    # Create a dict to test with
    all_vars = dict()
    all_vars['test_var_test'] = ['test_test']
    all_vars['my_var'] = ['my_value']
    # Call method evaluate_conditional with test data
    result = conditional_test._check_conditional("test_var_test is defined", None, all_vars)
    if not result:
        raise AssertionError("Evaluation of conditional should be True but is False")
    result = conditional_test._check_conditional("test_var_test is undefined", None, all_vars)
    if result:
        raise AssertionError("Evaluation of conditional should be False but is True")
    result = conditional_test._

# Generated at 2022-06-22 11:43:09.908673
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()

    # Test single conditional
    cond = 'foo is defined'
    result = c.extract_defined_undefined(cond)
    assert result == [('foo', 'is', 'defined')]

    # Test multiple conditionals
    cond = 'foo is defined and bar is defined'
    result = c.extract_defined_undefined(cond)
    assert result == [('foo', 'is', 'defined'), ('bar', 'is', 'defined')]
    cond = 'foo is defined or bar is defined'
    result = c.extract_defined_undefined(cond)
    assert result == [('foo', 'is', 'defined'), ('bar', 'is', 'defined')]
    cond = 'foo is defined and not bar is defined'
    result = c.extract_defined_undefined(cond)


# Generated at 2022-06-22 11:43:21.661362
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    def mock_get_option(*args, **kwargs):
        if args[0] == 'always_run':
            return True

    def mock_get_vars(*args, **kwargs):
        if args[0] == 'hostvars':
            return dict(HOSTNAME='localhost')

    p = Playbook.load(dict(hosts='localhost', tasks=[dict(action=dict(module='command', args='ls'))]), loader=None, variable_manager=None)

    play = p.get_plays()[0]
    templar = Templar(loader=None, variables=dict(a='b', c=dict(d='e')))


# Generated at 2022-06-22 11:43:47.488736
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    a = Conditional()
    assert a.extract_defined_undefined("1") == []
    assert a.extract_defined_undefined("a is defined") == [("a", " is ", "defined")]
    assert a.extract_defined_undefined("a is defined and b is defined") == [("a", " is ", "defined"), ("b", " is ", "defined")]
    assert a.extract_defined_undefined("a is not defined and b is defined") == [("a", " is not ", "defined"), ("b", " is ", "defined")]
    assert a.extract_defined_undefined("a is not defined and b is not defined") == [("a", " is not ", "defined"), ("b", " is not ", "defined")]

# Generated at 2022-06-22 11:43:59.941700
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    testcond_no_result = 'foobar foobar'
    testcond_one_result = 'foobar not is defined'
    testcond_two_results = 'foobar not is defined foobar is undefined'
    testcond_multi_results = 'foobar not is defined and foobar is undefined and hostvars[inventory_hostname] is defined and inventory_hostname not is undefined'

    a = Conditional()

    assert a.extract_defined_undefined(testcond_no_result) == []
    assert a.extract_defined_undefined(testcond_one_result) == [('foobar', 'not is', 'defined')]
    assert a.extract_defined_undefined(testcond_two_results) == [('foobar', 'not is', 'defined'), ('foobar', 'is', 'undefined')]

# Generated at 2022-06-22 11:44:13.095850
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''Test conditional evaluation'''
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class MyConditional(Conditional):
        _when = FieldAttribute(isa='list', default=list, extend=True, prepend=True)

    my_conditions = ['sys_a == "val_a"', 'sys_b == "val_b"']

    # variables
    variables = dict(
        sys_a='val_a',
        sys_b='val_b',
        sys_c='val_c',
        sys_d='val_d',
    )

    my_conditional = MyConditional()
    my_conditional.when = my_conditions

    play_context = PlayContext()
    templ

# Generated at 2022-06-22 11:44:26.270227
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    extracted_bool_undefined = conditional.extract_defined_undefined('foo is undefined or bar is undefined or baz is true')
    assert extracted_bool_undefined == [('foo', 'is', 'undefined'), ('bar', 'is', 'undefined')]
    extracted_bool_defined = conditional.extract_defined_undefined('foo is undefined or bar is defined or baz is true')
    assert extracted_bool_defined == [('foo', 'is', 'undefined'), ('bar', 'is', 'defined')]
    extracted_bool_not_defined = conditional.extract_defined_undefined('foo is undefined or bar is not defined or baz is true')
    assert extracted_bool_not_defined == [('foo', 'is', 'undefined'), ('bar', 'is not', 'defined')]


# Generated at 2022-06-22 11:44:38.455669
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    assert not cond.extract_defined_undefined('cond and cond')
    assert not cond.extract_defined_undefined('cond or cond')
    assert not cond.extract_defined_undefined('bla')
    assert cond.extract_defined_undefined('var is defined') == [('var', 'is', 'defined')]
    assert cond.extract_defined_undefined('var is defined or cond') == [('var', 'is', 'defined')]
    assert cond.extract_defined_undefined('cond or var is defined') == [('var', 'is', 'defined')]
    assert cond.extract_defined_undefined('cond or var is defined or var is undefined') == [('var', 'is', 'defined'), ('var', 'is', 'undefined')]
    assert cond

# Generated at 2022-06-22 11:44:50.158022
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.plugins.loader import action_loader

    fake_play = dict(
        post_validate=dict(
            all_vars=dict(
                hostvars=dict(
                    localhost=dict(
                        ansible_connection='local'
                    )
                ),
                test=False,
                test_boolean=True,
                test_integer=5,
                test_string= "test_string",
                test_yaml="""
                    ---
                    key: value
                """,
                test_list=[ "value1", "value2" ]
            )
        )
    )

# Generated at 2022-06-22 11:45:01.759724
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    ''' Parametrized unit tests to validate the output of Conditional.evaluate
    /// !IMPORTANT! This test is parametrized but will only be used when the unit test
    code is executed standalone '''

    # parametrized unit tests for Conditional class, method evaluate_conditional
    # this test is structured as a list of lists, each inner list containing:
    #   [0] = (optional) the expected result of evaluate_conditional
    #   [1] = (mandatory) the conditional string to test
    #   [2] = (optional)  the values with which to populate hostvars


# Generated at 2022-06-22 11:45:12.359304
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import unittest2 as unittest
    import ansible.parsing.yaml.objects

    class TestTemplar():

        class DummyEnvironment():

            class DummyTemplate():

                def render(self, environment):
                    return "test"

                def generate(self, environment):
                    return "test"

            def parse(self, text, name, filename):
                return self.DummyTemplate()

        def __init__(self, loader):
            self.loader = loader
            self.environment = TestTemplar.DummyEnvironment()

        def is_template(self, text):
            return False

        def template(self, data, preserve_trailing_newlines=False, escape_backslashes=True, fail_on_undefined=True):
            return data


# Generated at 2022-06-22 11:45:24.147056
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()


# Generated at 2022-06-22 11:45:35.578019
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.conditional import Conditional
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VariableManager

    def test_case(cond, variables, test_cases, is_template=False, disable_lookups=False, expected=False):
        if isinstance(cond, AnsibleUnsafeText):
            disable_lookups = True
        pb = PlayContext()
        pb.terminal_stdout_lines = 10

        vars_manager = VariableManager()
        vars_manager._fact_cache = variables
        pb.vars_manager = vars_manager


# Generated at 2022-06-22 11:46:04.119179
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    pass


# Generated at 2022-06-22 11:46:12.330239
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    ConditionalObj = Conditional()

    assert ConditionalObj.evaluate_conditional('1', {'1':1}) == True
    assert ConditionalObj.evaluate_conditional('foo', {'foo':1}) == True
    assert ConditionalObj.evaluate_conditional('foo', {'foo':0}) == False
    assert ConditionalObj.evaluate_conditional('foo', {}) == False
    assert ConditionalObj.evaluate_conditional('foo.bar', {'foo': {'bar': 1}}) == True
    assert ConditionalObj.evaluate_conditional('foo.bar', {'foo': {'bar': 0}}) == False
    assert ConditionalObj.evaluate_conditional('foo.bar', {'foo': []}) == False
    assert ConditionalObj.evaluate_conditional('foo.bar', {'foo': ""}) == False


# Generated at 2022-06-22 11:46:22.918609
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    cond = Conditional(loader=loader)


# Generated at 2022-06-22 11:46:35.173876
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.templar import MockTemplar

    loader = DictDataLoader({})
    collection = [
        '# empty comment',
        '#',
        '# comments',
        '#',
        '- debug: msg="This task should run"'
    ]

    templar = MockTemplar(collection=collection, loader=loader)

    cond = Conditional()

# Generated at 2022-06-22 11:46:46.913442
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    test_cases = [
        ('', []),
        ('foo == "bar" and baz == "qux"', []),
        ('bar is defined and baz is not defined', [('bar', 'is', 'defined'), ('baz', 'is not', 'defined')]),
        ('baz is not defined', [('baz', 'is not', 'defined')]),
        ('foo is defined', [('foo', 'is', 'defined')]),
        ('foo not is defined', [('foo', 'not is', 'defined')]),
        ('bar not is undefined', [('bar', 'not is', 'undefined')]),
        ('bar is not undefined', [('bar', 'is not', 'undefined')]),
    ]
    for conditional, result in test_cases:
        assert Conditional().extract_defined_undefined(conditional)

# Generated at 2022-06-22 11:46:58.604829
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # For the test cases, we will use a fake AnsibleModule.
    class FakeAnsibleModule:
        def __init__(self, **kwargs):
            self.params = dict()
            for k,v in kwargs.items():
                self.params[k] = v
    # First test case
    m = FakeAnsibleModule(debug=True)
    conditional = Conditional()
    conditional._when = ['existing_param|int == 23']
    templar = Templar(loader=None, variables=m.params)
    all_vars = dict()
    assert conditional.evaluate_conditional(templar, all_vars)
    # Second test case
    m = FakeAnsibleModule(debug=True)
    conditional = Conditional()
    conditional._when = ['existing_param|int == 23']

# Generated at 2022-06-22 11:47:03.739502
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestConditional(Conditional):
        pass

    import jinja2
    from ansible.template import Templar

    template_data_from_file = """
    # contains some jinja2
    [targets]
    localhost ansible_connection=local
    {%- if not foo %}
    foo
    {%- endif %}
    """

    myvars = dict(
        ansible_ssh_host='localhost',
        ansible_ssh_pass='vagrant',
        ansible_ssh_port='22',
        foo=True,
    )
    templar = Templar(loader=None, shared_loader_obj=None, variables=myvars)
    cond = TestConditional(loader=None)

    # from a file
    cond.when = []

# Generated at 2022-06-22 11:47:10.187554
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    foo = Conditional()
    test_str = text_type(
        'foo is defined and (bar is defined or not baz is defined) and '
        'boo is not defined and (not xxx is defined or yyy is defined)')
    expected = [
        ('foo', 'is', 'defined'),
        ('bar', 'is', 'defined'),
        ('baz', 'is', 'undefined'),
        ('boo', 'is', 'undefined'),
        ('xxx', 'is', 'undefined'),
    ]
    assert foo.extract_defined_undefined(test_str) == expected


# Generated at 2022-06-22 11:47:23.362978
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # 1. Normal conditional
    assert Conditional().evaluate_conditional(Conditional(), {"a": "2"})
    assert Conditional().evaluate_conditional(Conditional(), {"a": 0})
    assert Conditional().evaluate_conditional(Conditional(), {"a": True})
    assert Conditional().evaluate_conditional(Conditional(), {"a": False})

    # 2. Not equal
    assert Conditional().evaluate_conditional(Conditional(), {"a": "1", "b": "2"})
    assert Conditional().evaluate_conditional(Conditional(), {"a": "1", "b": 0})

    assert not Conditional().evaluate_conditional(Conditional(), {"a": "2", "b": "2"})
    assert not Conditional().evaluate_conditional(Conditional(), {"a": "1", "b": "1"})

# Generated at 2022-06-22 11:47:35.598381
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Unit test for method evaluate_conditional of class Conditional

    Test the behaviour of evaluate_conditional method for different
    values of conditional with different scenarios
    '''

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # set up required objects
    play_context = PlayContext()
    templar = Templar(loader=None, variables={})

    # set up test data

# Generated at 2022-06-22 11:48:41.476621
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    import unittest
    fromj2vars = dict(
        bar = 'dummy',
        hostvars = dict(
            foo = 'dummy',
            bar = 'dummy',
        ),
    )
    fromj2vars['group_names'] = fromj2vars['groups'] = ['a', 'b']

    class TestConditional(Conditional):
        pass

    testobj = TestConditional()

    class TestExtractDefinedUndefined(unittest.TestCase):
        def test_empty(self):
            self.assertEqual([], testobj.extract_defined_undefined(""))

        def test_no_match(self):
            self.assertEqual([], testobj.extract_defined_undefined("foofoofoo"))

        def test_match(self):
            self

# Generated at 2022-06-22 11:48:53.498506
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    hvars = dict(ansible_connection='local')
    hvars['test_var_one'] = 'test_val_one'
    hvars['test_var_two'] = 'test_val_two'
    hvars['test_var_three'] = 'test_val_three'
    hvars['test_var_four'] = 'test_val_four'
    hvars['test_var_five'] = 'test_val_five'
    hvars['test_var_six'] = 'test_val_six'
    hvars['test_var_seven'] = 'test_val_seven'
    hvars['test_var_eight'] = 'test_val_eight'
    hvars['test_var_nine'] = 'test_val_nine'
    hvars

# Generated at 2022-06-22 11:48:58.892376
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    assert cond.extract_defined_undefined('(a is defined and b is defined)') == [('a', 'is', 'defined'), ('b', 'is', 'defined')]

# unit test for method evaluate_conditional of class Conditional
# FIXME remove in 2.5

# Generated at 2022-06-22 11:49:09.353794
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    try:
        import jinja2
    except ImportError:
        jinja2 = None

    if jinja2 is None:
        raise AnsibleError("error while importing jinja2")

    from ansible.template import Templar

    # Setup test variables
    all_vars = {}
    templar = Templar(loader=None, variables=all_vars)

    # Test variables
    when_list = ["FOO is not defined or FOO.startswith('r')",
                 "TRUE",
                 "FALSE",
                 "foo is defined"]
    when_list_results = [False, True, False, False]

    # Setup variables used in tests
    conditional = Conditional()
    conditional.when = when_list

    # Test evaluate_conditional() method

# Generated at 2022-06-22 11:49:21.548757
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test when conditional is a string
    import jinja2
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.strategy import StrategyBase
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.plugins.connection import ConnectionBase

    # TODO: define 'random' host and group variables
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory

# Generated at 2022-06-22 11:49:33.116752
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    module_utils_path = ansible.module_utils.__path__[0]
    if module_utils_path not in sys.path:
        sys.path.append(module_utils_path)
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.plugins.loader import module_loader, fragment_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    # We need to simulate a host for the fact module.
    loader = DataLoader()
    context = PlayContext()
    context.connection = 'local'
    context.become = False
    context.become_method = 'sudo'
    context.become_user = 'root'

# Generated at 2022-06-22 11:49:35.912600
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test for a simple string
    conditional = 'a simple string'
    object = Conditional()
    assert object.evaluate_conditional(None, None) == conditional

# Generated at 2022-06-22 11:49:42.376939
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('hostvars["foo"] is defined') == [('hostvars["foo"]', 'is', 'defined')]
    assert c.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]
    assert c.extract_defined_undefined('foo is defined or bar is defined') == [('foo', 'is', 'defined'), ('bar', 'is', 'defined')]

# Generated at 2022-06-22 11:49:51.230607
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    # Extract variables and logic states from strings which include defined/undefined checks
    assert conditional.extract_defined_undefined('hostvars[\'foo\'] is defined or hostvars[\'bar\'] is undefined') == [['hostvars[\'foo\']', 'is', 'defined'], ['hostvars[\'bar\']', 'is', 'undefined']]
    # Don't extract variables and logic states from strings which don't include defined/undefined checks
    assert conditional.extract_defined_undefined('empty') == []


# Generated at 2022-06-22 11:50:02.162459
# Unit test for constructor of class Conditional
def test_Conditional():
    yaml_data = '''
- hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - debug:
        msg: 'blah'
      when: {{var}}
'''
    data = {'var': True}
    play, handler = Base.load_from_file('testyaml', yaml_data, variable_manager=VariableManager(loader=DataLoader()), variable_manager_args=dict(all_vars=data))
    play[0]._task_cache = play[0]._compile_roles_tasks()

    # task level conditionals should work
    play[0]._task_cache[0].evaluate_conditional(play[0]._variable_manager.template, play[0]._variable_manager.get_vars(play=play[0]))

