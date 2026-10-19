

# Generated at 2022-06-22 11:40:26.404384
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar

    block = Block()
    task = Task()
    task.name = "TASK"
    block.block = [ task ]

    # set_fact module expects a value of type 'dict'

# Generated at 2022-06-22 11:40:32.359766
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    import jinja2
    import sys

    class MyBase(Conditional):
        def __init__(self, loader=None):
            # since this is a mix-in, it may not have an underlying datastructure
            # associated with it, so we pull it out now in case we need it for
            # error reporting below
            if loader is None:
                raise AnsibleError("a loader must be specified when using Conditional() directly")
            else:
                self._loader = loader
            super(MyBase, self).__init__()


# Generated at 2022-06-22 11:40:42.772746
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar

    # This is the module_utils/basic.py from Ansible 2.1.1.0

# Generated at 2022-06-22 11:40:45.075195
# Unit test for constructor of class Conditional
def test_Conditional():

    # Set up
    b = Conditional()

    # Test
    assert b is not None
    assert hasattr(b, '_validate_when')


# Generated at 2022-06-22 11:40:52.281071
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    t = Templar(loader=None, variables={})
    condition = Conditional()
    condition.when = ['condition1']
    assert not condition.evaluate_conditional(t, play_context.variable_manager.extra_vars)
    condition.when = ['condition1', 'condition2']
    assert not condition.evaluate_conditional(t, play_context.variable_manager.extra_vars)
    condition.when = ['condition1', 'condition2', 'condition3']
    assert not condition.evaluate_conditional(t, play_context.variable_manager.extra_vars)
    condition.when = ['condition1', 'condition2', 'condition3', 'condition4']

# Generated at 2022-06-22 11:41:03.185020
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    host_list = ['localhost']

# Generated at 2022-06-22 11:41:16.840146
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    display.verbosity = 3


# Generated at 2022-06-22 11:41:28.952156
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:41:39.193616
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('hostvars[hostvars[hostvars[hostvars[foo is undefined or not hostvars[bar is undefined]]]]]') == [('hostvars[foo', 'is', 'undefined'), ('hostvars[bar', 'is', 'undefined')]
    assert c.extract_defined_undefined('hostvars[foo is undefined or not hostvars[bar is undefined]]]') == [('hostvars[foo', 'is', 'undefined'), ('hostvars[bar', 'is', 'undefined')]

# Generated at 2022-06-22 11:41:48.564448
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import ansible.playbook
    import ansible.template

    class Host:
        def __init__(self, name='127.0.0.1'):
            self.name = name

    class VariableManager:
        def __init__(self):
            self.extra_vars = dict()

    # Load the needed objects
    class Inventory:
        def __init__(self):
            self.loader = None
    inventory = Inventory()
    inventory.hosts = {'127.0.0.1': Host()}

    # Load the needed objects
    task1 = ansible.playbook.Task()
    task1.name = 'task1'

    # Load the needed objects
    templar = ansible.template.Templar(loader=None, variables=dict(), shared_loader_obj=None)

    # Create

# Generated at 2022-06-22 11:42:07.432799
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

    assert conditional.extract_defined_undefined(None) == []
    assert conditional.extract_defined_undefined('') == []
    assert conditional.extract_defined_undefined('true') == []
    assert conditional.extract_defined_undefined('somevar') == []
    assert conditional.extract_defined_undefined('somevar == "foo"') == []
    assert conditional.extract_defined_undefined('somevar == "foo" and somevar2 is defined') == [('somevar2', 'is', 'defined')]
    assert conditional.extract_defined_undefined('somevar == "foo" and somevar2 is not defined') == [('somevar2', 'is not', 'defined')]

# Generated at 2022-06-22 11:42:17.626720
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext

    conditional = '''
    ( inventory_hostname == 'myhost.localdomain' and (1 == 1) ) or ( test_var | failed )
    '''

    fake_loader = DictDataLoader({
        "file:///test_var": b"3",
    })

    play_context = PlayContext()
    play_context.variable_manager.set_inventory(Inventory(loader=fake_loader))
    play_context.variable_manager.extra_vars = {
        "inventory_hostname": "myhost.localdomain",
        "substring_test": "substring",
        "substring_test_two": "substring_test",
        "list_test": [1, 2, 3],
    }

    conditional_result

# Generated at 2022-06-22 11:42:23.331057
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.clean import module_response_deepcopy

    class TestTask(Task, Conditional):
        pass

    t = TestTask(loader=None)
    assert t.extract_defined_undefined("'foo.bar' in groups") == []

    conditional = "'foo.bar' in groups and hostvars['localhost']['ansible_os_family'] == 'RedHat'"
    assert t.extract_defined_undefined(conditional) == [('hostvars[\'localhost\']', 'is', 'defined')]


# Generated at 2022-06-22 11:42:35.612385
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    variable_manager = VariableManager()
    loader = DataLoader()

    my_vars = {"var1": "value1", "var2": "value2"}
    variable_manager.set_inventory(loader.load_inventory(host_list=['localhost']))
    variable_manager.set_extra_vars(my_vars)
    templar = Templar(loader=loader, variables=variable_manager)

    value1 = templar.template("{{var1}}")
    if value1 != "value1":
        raise AssertionError("Templar don't work!")

    value2 = templar.template("{{var2}}")

# Generated at 2022-06-22 11:42:44.500815
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    conditional.when = [ "baz is undefined" ]
    results = conditional.extract_defined_undefined(conditional.when[0])
    assert len(results) == 1
    assert results[0][0] == "baz"
    assert results[0][1] == "is"
    assert results[0][2] == "undefined"
    conditional.when = [ "foo is defined" ]
    results = conditional.extract_defined_undefined(conditional.when[0])
    assert len(results) == 1
    assert results[0][0] == "foo"
    assert results[0][1] == "is"
    assert results[0][2] == "defined"
    conditional.when = [ "bar not is not defined" ]
    results = conditional.extract_defined_

# Generated at 2022-06-22 11:42:55.548266
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar


# Generated at 2022-06-22 11:43:06.804073
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # FIXME: Using a fake class just to be able to instantiate the Conditional mixin class
    class FakeConditional(Conditional):
        def __init__(self):
            super(FakeConditional, self).__init__()


# Generated at 2022-06-22 11:43:18.306678
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import jinja2

    # test that an empty condition is interpreted as True
    conditional = Conditional()
    conditional._when = ['']
    assert conditional.evaluate_conditional(jinja2.Environment(), {})

    # test that no condition is given is interpreted as True
    conditional._when = []
    assert conditional.evaluate_conditional(jinja2.Environment(), {})

    # test that a literal True value is interpreted as True
    conditional._when = [True]
    assert conditional.evaluate_conditional(jinja2.Environment(), {})

    # test that a literal False is interpreted as False
    conditional._when = [False]
    assert not conditional.evaluate_conditional(jinja2.Environment(), {})

    # test that a variable in hostvars with a value of True is interpreted as True

# Generated at 2022-06-22 11:43:30.298137
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    assert cond.extract_defined_undefined("hostvars['foo'] is defined") == [('hostvars[\'foo\']', 'is', 'defined')]
    assert cond.extract_defined_undefined("hostvars['foo']  is  defined") == [('hostvars[\'foo\']', 'is', 'defined')]
    assert cond.extract_defined_undefined("hostvars['foo'] is undefined") == [('hostvars[\'foo\']', 'is', 'undefined')]
    assert cond.extract_defined_undefined("hostvars['foo'] is not undefined") == [('hostvars[\'foo\']', 'is not', 'undefined')]

# Generated at 2022-06-22 11:43:41.295320
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.splitter import parse_kv
    from ansible.vars.manager import VariableManager
    from ansible.playbook import Play
    import jinja2


# Generated at 2022-06-22 11:43:57.892460
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Conditional.evaluate_conditional is only a wrapper around Conditional._check_conditional
    # and there is a mock of Conditional._check_conditional in test_Conditional__check_conditional.
    # If the function Conditional.evaluate_conditional is changed, its unit test will also
    # need to be changed in test_Conditional__check_conditional.

    if C.DEFAULT_MODULE_LANG == 'C':
        # The unit test has already been covered in test_Conditional__check_conditional.
        pass
    else:
        # Make sure the unit test will be run only if the default module language is not C.
        raise Exception("Unit test for method Conditional.evaluate_conditional is not implemented.")



# Generated at 2022-06-22 11:44:10.400460
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from collections import namedtuple

    class TestObj(Conditional):
        pass

    class TestTemplar(object):

        unsafe_eval_regex = re.compile(r'^(safe_eval|regex_replace)\(')
        env = namedtuple('MockEnv', ['parse', 'compile'])
        environment = env(parse=lambda t, s, f: ast.parse(s, mode='exec'), compile=lambda t, s: s)
        _locals_cache = {}
        jinja2_vars = {}
        jinja2_builtins = {}
        available_variables = {}


# Generated at 2022-06-22 11:44:19.743145
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """Test evaluate_conditional method of Conditional class"""
    class MyTask(object):
        name = 'test_name'
        when = 'test_conditional'
        class _ds(object):
            pass
    class MyTemplar(object):
        class environment(object):
            class parse(object):
                pass
            class generate(object):
                pass
        class _available_variables(object):
            pass
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import generate_ansible_template_vars
    import sys

    # Save the original sys.stdout
    old_stdout = sys.stdout

    # Create StringIO object
    fp = StringIO.StringIO

# Generated at 2022-06-22 11:44:30.407140
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Mock class Conditional
    class ConditionalTest:

        # Mock class Host
        class Host:
            def __init__(self, hostname):
                self.name = hostname
            def __repr__(self):
                return self.name

        # Mock class Play
        class Play:
            def __init__(self, host):
                self.hosts = [host]

        # Mock class PlayContext
        class PlayContext:
            def __init__(self):
                self.play = None
                self.port = 22
                self.remote_addr = None

        # Mock class VariableManager
        class VariableManager:
            def __init__(self, vars):
                self._vars = vars
                self._hostvars = dict([(host, self._vars) for host in ["host1"]])

           

# Generated at 2022-06-22 11:44:42.495993
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # We don't want to create an actual Playbook/Task to run this test as it would
    # require setting up variables in a very specific way. Instead, we create a
    # "templar" to handle templating.

    # This is a very basic jinja2 environment. We don't need anything more
    # complicated to run the test.
    from ansible.template import Templar

    class DummyModule:
        def __init__(self, args, from_task=False):
            self.args = args

        def _load_params(self):
            return dict((k, v) for k, v in iteritems(self.args) if v is not None)

    class DummyTask(Conditional):
        pass

    class DummyPlaybook:
        def __init__(self):
            self.extra_vars = dict

# Generated at 2022-06-22 11:44:43.994468
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # FIXME: write unit tests for this method
    pass


# Generated at 2022-06-22 11:44:54.627532
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    vars_file = "./test/unit/playbook/conditional_vars_file.yml"
    loader = DataLoader()
    vars_manager = [loader.load_from_file(vars_file)]
    templar = Templar(loader=loader, variables=vars_manager)


# Generated at 2022-06-22 11:45:04.518081
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    def check_evaluation(when, expected_result, vars):
        c = Conditional()
        c._when = when
        assert c.evaluate_conditional(Templar(loader=None, variables=vars), vars) == expected_result

    # A minimum set of variables to cover a lot of possible conditions
    base_vars = dict(
        a=False, b=True, c=False,
        d=dict(e=True, f=False), i=dict(j=dict(k=dict())),
        l=None, m='', n='0', o='foo', r=0, s=2,
        t=False, u=True, v='foo', w='bar', z=False,
    )

# Generated at 2022-06-22 11:45:16.479401
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Fixture data
    conditional = '{{ host_name }} == "localhost" or host_name == "localhost"'
    all_vars = {u'host_name': 'localhost'}
    templar = DummyTemplar()

    # Test Case 1
    # Expected result: True
    # Data: conditional is OK
    # Action: initialize a test Conditional object, call evaluate_conditional()
    # Verify: result is True
    conditional_obj = Conditional()
    result = conditional_obj.evaluate_conditional(templar, all_vars)
    assert result

    # Test Case 2
    # Expected result: error
    # Data: conditional is bad
    # Action: initialize a test Conditional object, call evaluate_conditional()
    # Verify: error occur
    conditional_obj = Conditional()
    conditional

# Generated at 2022-06-22 11:45:17.080574
# Unit test for constructor of class Conditional
def test_Conditional():
    c = Conditional()
    assert c is not None

# Generated at 2022-06-22 11:45:37.910915
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    display = Display()
    result = Conditional().extract_defined_undefined('setup_clean is defined or ansible_host is "localhost"')
    expected = [('setup_clean', 'is', 'defined'), ('ansible_host', 'is', 'defined')]
    assert result == expected
    result = Conditional().extract_defined_undefined('ansible_distribution == "Debian" and ansible_distribution_version >= "8"')
    assert result == [('ansible_distribution', 'is', 'defined'), ('ansible_distribution_version', 'is', 'defined')]

# Generated at 2022-06-22 11:45:50.456817
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestClass():
        pass

    loader = TestClass()
    loader.template_class = TestClass
    loader.template_class.environment = TestClass
    loader.template_class.environment.lexer = TestClass
    loader.template_class.environment.lexer.tokenize = tokenize
    loader.template_class.environment.compile = compile
    loader.template_class.environment.generate = generate

    test_conditional = 'foo'
    test_vars = dict()
    test_vars['foo'] = 0
    test_templar = TestClass()
    test_templar.template = evaluate_template
    test_templar.environment = TestClass()
    test_templar.environment.parse = parse
    test_cond = Conditional(loader)
    result = test_cond._check_

# Generated at 2022-06-22 11:46:01.307889
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:46:13.701056
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins import vars_loader

    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'foo': 'bar',
        'baz': True,
        'bam': False,
        'nested': {
            'a': 'b'
        },
        'quotes': 'this string contains "double" quotes'
    }
    loader = DataLoader()
    play_context = PlayContext()

# Generated at 2022-06-22 11:46:23.871239
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class FakeTemplar(object):
        def is_template(self, conditional):
            return False
        def template(self, data, disable_lookups=True):
            return data

    class FakeClass(Conditional):
        pass

    templar = FakeTemplar()
    test_class = FakeClass(loader=None)

    all_vars = dict(fact1=1, fact2=2, fact3=3, fact4=4)
    assert test_class.evaluate_conditional(templar, all_vars)

    all_vars = dict(fact1=1, fact2=2, fact3=3, fact4=4, fact5=5, fact6=6, fact7="string")

# Generated at 2022-06-22 11:46:37.066070
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    scope = {}

    module = ""
    module_args = ""

    class MockTemplar:
        def __init__(self):
            pass

        def is_template(self, text):
            return False

        def template(self, text, **kwargs):
            return text

    class MockModule(Conditional):
        def __init__(self):
            pass
        def __getattribute__(self, attr):
            return scope[attr]

    m = MockModule()
    m._templar = MockTemplar()
    scope['when'] = []
    scope['_templar'] = MockTemplar()
    scope['module'] = module
    scope['module_args'] = module_args
    scope['_ds'] = {}

    assert m.evaluate_conditional(m._templar, {})

# Generated at 2022-06-22 11:46:45.105634
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    import pytest

    class TestConditional(Conditional):
        def __init__(self):
            self._ds = dict()
            self._loader = DataLoader()

    c = TestConditional()

# Generated at 2022-06-22 11:46:53.058267
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.template.template import AnsibleTemplate

    # set continue_if_error=True to allow execution of code after a failed step

# Generated at 2022-06-22 11:47:01.577115
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined(u"foo is defined") == [(u'foo', u'is', u'defined')]
    assert c.extract_defined_undefined(u"foo is not defined") == [(u'foo', u'is not', u'defined')]
    assert c.extract_defined_undefined(u"foo is undefined") == [(u'foo', u'is', u'undefined')]
    assert c.extract_defined_undefined(u"foo is not undefined") == [(u'foo', u'is not', u'undefined')]

# Generated at 2022-06-22 11:47:11.207659
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    """This is a unit test for method extract_defined_undefined of class Conditional"""

# Generated at 2022-06-22 11:47:43.648428
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Conditional_Test(object):
        '''
        This is a test class that extends Conditional to allow testing
        of Conditional.evaluate_conditional
        '''
        def __init__(self):
            pass

    ct = Conditional_Test()
    ct.evaluate_conditional({})

# Generated at 2022-06-22 11:47:55.640416
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-22 11:48:07.155483
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.task import Task

    task = Task()
    task._ds = dict()
    task.when = [
        'ansible_os_family == "RedHat"',
        'ansible_os_family == "Debian"',
    ]

    task_vars = dict(
        ansible_os_family = 'RedHat',
    )

    res = task.evaluate_conditional(None, task_vars)
    assert(res)

    task_vars = dict(
        ansible_os_family = 'Debian',
    )

    res = task.evaluate_conditional(None, task_vars)
    assert(res)

    task_vars = dict(
        ansible_os_family = 'Solaris',
    )


# Generated at 2022-06-22 11:48:18.186326
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:48:28.017124
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    """Unit test Conditional.extract_defined_undefined"""

    conditional = Conditional()

    tests = []
    tests.append([
        'a is defined',
        [('a', 'is', 'defined')]])
    tests.append([
        'a is defined and b is defined',
        [('a', 'is', 'defined'), ('b', 'is', 'defined')]])
    tests.append([
        'a is defined and b is undefined',
        [('a', 'is', 'defined'), ('b', 'is', 'undefined')]])
    tests.append([
        'a is defined or b is defined',
        [('a', 'is', 'defined'), ('b', 'is', 'defined')]])

# Generated at 2022-06-22 11:48:39.684248
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible import context
    from ansible.module_utils.six import PY3
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    assert Conditional().evaluate_conditional(Templar(VariableManager(), loader=None), context.CLIARGS) is True
    assert Conditional(loader=None).evaluate_conditional(Templar(VariableManager(), loader=None), context.CLIARGS) is True
    assert Conditional().evaluate_conditional(Templar(VariableManager(), loader=None), dict(one=1, two=2, three=3)) is True
    assert Conditional().evaluate_conditional(Templar(VariableManager(), loader=None), dict(one=1, two=2, three=3, ansible_python_interpreter=False)) is True

# Generated at 2022-06-22 11:48:52.070212
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    a_dict = {'a':'b'}
    b_dict = {'c':'d'}
    a_dict_with_results = {'a':'b', '_ansible_no_log':False, '_ansible_verbose_always':True, '_ansible_version':10, '_ansible_diff':True}

    conditional = Conditional()

    # Test with True:
    conditional._when = [True]
    assert True == conditional.evaluate_conditional(None, None)

    # Test with False:
    conditional._when = [False]
    assert False == conditional.evaluate_conditional(None, None)

    # Test with expected:
    conditional._when = ['a == b']
    assert True == conditional.evaluate_conditional(None, a_dict)

# Generated at 2022-06-22 11:49:04.427228
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    c = Conditional()
    def testextract(attr, expected):
        result = c.extract_defined_undefined(attr)
        assert result == expected, "testextract(%s,%s) returned %s" % (attr, expected, result)

    # No defined/undefined
    testextract("", [])
    testextract("0", [])
    testextract("True", [])
    testextract("False", [])

    # not is undefined
    testextract("'not' is undefined", [])
    testextract("'not' is not undefined", [])

    # Syntactically invalid
    testextract("hostvars['foo_hostname'] is not defined foo", [])

    # Simple defined/und

# Generated at 2022-06-22 11:49:16.805544
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({})

    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    def test(self, cond, vars=None, expect=False):
        if vars is None:
            vars = dict()
        # Create a fake PlayContext and assign it to the Conditional
        setattr(self, '_play_context', PlayContext())
        res = self.evaluate_conditional(templar, vars)
        assert res == expect, 'Expected %s for "%s" but got %s' % (expect, cond, res)

   

# Generated at 2022-06-22 11:49:27.779560
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display.verbosity = 3
    display.color = None

    # This is a minimal example of Base object and templar (jinja2) object
    class TestClass1(object):
        def __init__(self, ds):
            self._ds = ds
    class TestTemplar1(object):
        def __init__(self):
            self.available_variables = dict()
        def template(self, data=None, **kargs):
            if data is None:
                return None
            try:
                return str(eval(data, {}, self.available_variables))
            except Exception as e:
                if dict(self.available_variables).has_key(data):
                    return dict(self.available_variables)[data]
                else:
                    raise e