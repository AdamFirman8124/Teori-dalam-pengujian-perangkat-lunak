

# Generated at 2022-06-22 11:40:27.958103
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    variable_manager = VariableManager()
    variable_manager.set_inventory(None)

    play_context = PlayContext()

    templar = Templar(loader=None, variables=variable_manager,
                      shared_loader_obj=None, play_context=play_context)

    # Here is a list of conditionals that are expected to be evaluated as
    # True.  Conditionals that should be evaluated as False are listed
    # in test_Conditional_evaluate_conditional_false.

# Generated at 2022-06-22 11:40:38.589695
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager

    results = {
        'ansible_facts': {'foo': 'bar'},
        'changed': False,
        'invocation': {'module_args': {'foo': 'foo'}},
    }

    vars_manager = VariableManager()
    vars_manager.resolve_vars_in_templated_namespace(results)
    context = PlayContext()
    templar = Templar(loader=None, shared_loader_obj=None, variables=vars_manager)

    test_conditional = Conditional()

    test_conditional.when = ['{{ ansible_facts["foo"] == "bar" }}']
    assert test_conditional.evaluate_cond

# Generated at 2022-06-22 11:40:48.051379
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    conditional_result = Conditional()

    templar = AnsibleTemplate()

    # Testing with undefined variable
    test_data = {'a': 'ok', 'b': 'ok', 'c': 'ok'}
    result = conditional_result.evaluate_conditional(templar, test_data)
    assert not result

    # Testing with defined variable
    test_data = {'undefined_var': 'ok'}
    result = conditional_result.evaluate_conditional(templar, test_data)
    assert result == True

    # Testing with defined variable in a list
    test_data = {'undefined_var': ['ok']}
    result = conditional_result.evaluate_conditional(templar, test_data)
    assert result == True

    # Testing with undefined variable in a list

# Generated at 2022-06-22 11:41:00.594022
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Test data
    c = Conditional()
    context = PlayContext()
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'dept': 'sales', 'env': 'production'}
    variable_manager._hostvars = {'localhost': {'ansible_connection': 'local'},}
    templar = Templar(loader=None, variables=variable_manager, play_context=context)

    # Test using evaluate_conditional with undefined variable
    # This should cause an AnsibleUndefinedVariable error.

# Generated at 2022-06-22 11:41:01.683280
# Unit test for constructor of class Conditional
def test_Conditional():
    Conditional()

# Generated at 2022-06-22 11:41:15.672361
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class DummyClass(Conditional):
        pass
    all_vars = dict(
        a=4,
        b=dict(c='c')
    )
    dc = DummyClass()
    templar = DummyTemplar()
    # test empty
    assert dc.evaluate_conditional(templar, all_vars)

    # test list
    dc = DummyClass(when=['a == 4', 'b.c == "c"'])
    assert dc.evaluate_conditional(templar, all_vars)
    dc = DummyClass(when=['a == 6', 'b.c == "c"'])
    assert not dc.evaluate_conditional(templar, all_vars)

    # test bool
    dc = DummyClass(when=True)
    assert dc.evaluate

# Generated at 2022-06-22 11:41:28.308327
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    cond = Conditional()

    class FakeEnv:
        def from_string(self, str):
            return FakeTemplate(str)

        def get_template(self, *args, **kwargs):
            return FakeTemplate('')

    class FakeTemplate:
        def __init__(self, str):
            self.str = str

        def render(self, context):
            return self.str

    import jinja2
    templar = jinja2.Environment(loader=jinja2.DictLoader({}))
    templar.environment = FakeEnv()
    templar.set_available_variables({'var': 'test'})

    assert cond._check_conditional('var == "test"', templar, {}) == True

# Generated at 2022-06-22 11:41:29.937218
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    assert True


# Generated at 2022-06-22 11:41:39.702531
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    # list of tuples with test case and expected result

# Generated at 2022-06-22 11:41:50.839787
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook import Play
    import ansible.playbook.play
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar


# Generated at 2022-06-22 11:42:04.589816
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager

    class TestConditional(Conditional):
        pass

    # Simple play for validating TestConditional
    class TestPlay():
        def __init__(self):
            self.hostvars = HostVars(inventory=None)

            self.variable_manager = VariableManager()
            self.variable_manager.set_host_variable(host=None, varname='foo', value=42)
            self.variable_manager.set_host_variable(host=None, varname='bar', value=42)
            self.variable_manager.set_host_variable(host=None, varname='baz', value=42)

# Generated at 2022-06-22 11:42:14.784429
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class DummyInventory(object):
        pass

    vars_mgr = VariableManager()

    class Dummy(Conditional):
        _loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.set_inventory(DummyInventory())
    variable_manager._extra_vars = {"env": "test"}
    templar = Templar(loader=DataLoader(), variables=variable_manager)

    # foo is not defined, so this should fail
    assert not Dummy().evaluate_conditional(templar, dict())

    # foo is not defined, so this should fail

# Generated at 2022-06-22 11:42:26.587169
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class MyClass(Conditional):
        _when = FieldAttribute(isa='list', default=list, extend=True, prepend=True)

    class FakeTemplar(object):
        def __init__(self, loader, fail_on_undefined=False, environment=None):
            self._loader = loader
            self._fail_on_undefined = fail_on_undefined
            self._environment = environment

        def is_template(self, data, fail_on_undefined=False, escape_backslashes=True):
            self._fail_on_undefined = fail_on_undefined
            return False

        def template(self, data, fail_on_undefined=False, disable_lookups=False, escape_backslashes=True):
            self._fail_on_undefined = fail_on_undefined
           

# Generated at 2022-06-22 11:42:35.793326
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    class DummyUnicode(text_type):
        pass

    # This class is used to test method extract_defined_undefined
    class TestConditional(Conditional):
        def __init__(self):
            pass

    conditional = TestConditional()
    assert conditional.extract_defined_undefined("") == []
    assert conditional.extract_defined_undefined("foo") == []
    assert conditional.extract_defined_undefined("foo.bar") == []
    assert conditional.extract_defined_undefined("foo not is defined") == [('foo', 'not is', 'defined')]
    assert conditional.extract_defined_undefined("foo is not defined") == [('foo', 'is not', 'defined')]

# Generated at 2022-06-22 11:42:47.156992
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Test for extract_defined_undefined with valid expression
    conditional = 'foo is defined and (bar is not defined or baz is defined)'
    result = Conditional().extract_defined_undefined(conditional)
    assert result == [('foo', 'is', 'defined'), ('bar', 'is not', 'defined'), ('baz', 'is', 'defined')]

    # Test for extract_defined_undefined with invalid expression
    conditional = 'foo is defined and test is defined'
    result = Conditional().extract_defined_undefined(conditional)
    assert result == []


# Generated at 2022-06-22 11:42:57.185251
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    _test_writer = Display()
    _test_in = dict(
        foo = 123,
        bar = 456,
        gaz = 789,
        test = 'No Value',
        message = 'Hello',
        a_list = [ 1, 2, 3, 4, 5 ],
        a_dict = dict(
            one = 1,
            two = 2,
            three = 3,
            four = 4,
            five = 5,
        )
    )

# Generated at 2022-06-22 11:43:05.078046
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.template import Templar

    column = PlayContext()
    column.become = False
    column.become_user = 'example_user'
    column.connection = 'local'
    column.network_os = None
    column.remote_addr = '127.0.0.1'
    column.remote_user = 'example_user'
    column.port = 22
    column.become_password = 'example_password'

    class MyConditional(Conditional):

        def evaluate_conditional(self, templar, all_vars):
            return super(MyConditional, self).evaluate_conditional(templar, all_vars)

    conduit = MyConditional()


# Generated at 2022-06-22 11:43:16.810174
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    ''' test the evaluate_conditional method of Conditional'''
    import sys
    import os
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.strategy import StrategyBase

    class MyTaskQueueManager(TaskQueueManager):
        ''' a version of TaskQueueManager that does not call cleanup'''
        def __init__(self, *args, **kwargs):
            super(MyTaskQueueManager, self).__init__(*args, **kwargs)

        def cleanup(self):
            self._cleanup_processes()


# Generated at 2022-06-22 11:43:21.828835
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import pytest
    c = Conditional(loader=None)
    assert c.extract_defined_undefined("var1 is undefined") == [("var1", "is", "undefined")]
    assert c.extract_defined_undefined("var1 is not undefined") == [("var1", "is not", "undefined")]
    assert c.extract_defined_undefined("var1 is defined") == [("var1", "is", "defined")]
    assert c.extract_defined_undefined("var1 is not defined") == [("var1", "is not", "defined")]

# Generated at 2022-06-22 11:43:32.208454
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    test_Conditional_evaluate_conditional is a unit test for the method identify_conditional of the class Conditional
    :return:
    '''
    from ansible.playbook.base import Base
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    base = Base()
    base.when = [
            1,
            0,
            'ansible_facts["distribution"] == "CentOS" or ansible_facts["distribution"] == "RedHat"',
            'ansible_facts["distribution_major_version"] is defined',
            'ansible_facts["distribution_major_version" is not defined'
    ]

    # Create all necessary objects to call the method
    host_vars_

# Generated at 2022-06-22 11:43:58.111609
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook.base import Base

    class MyBase(Base):
        _when = FieldAttribute(isa='list', default=list, extend=True, prepend=True)

    base = MyBase(loader=None)
    assert isinstance(base._when, list)
    assert len(base._when) == 0

    class MyBase2(Base):
        pass

    try:
        base = MyBase2(loader=None)
    except AnsibleError as e:
        assert 'loader' in str(e)

    class MyBase3(Base):
        _loader = object()

    base = MyBase3()
    assert isinstance(base, MyBase3)


# Generated at 2022-06-22 11:44:06.213742
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar

    # test with a simple True condition
    test_obj = Conditional()
    test_obj.when = [True]
    templar = Templar(loader=None)
    display.verbosity = 3
    assert(test_obj.evaluate_conditional(templar, {}) == True)

    # test with a simple False condition
    test_obj = Conditional()
    test_obj.when = [False]
    templar = Templar(loader=None)
    display.verbosity = 3
    assert(test_obj.evaluate_conditional(templar, {}) == False)

    # test with a simple condition that uses a variable
    test_obj = Conditional()
    test_obj.when = ["{{var1}}"]
    templar = Templar(loader=None)
   

# Generated at 2022-06-22 11:44:14.897410
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('') == []
    assert c.extract_defined_undefined('some_var is defined') == [('some_var', 'is', 'defined')]
    assert c.extract_defined_undefined('some_var is defined or another_var not is defined and a_third_var is undefined') == [('some_var', 'is', 'defined'), ('another_var', 'not is', 'defined'), ('a_third_var', 'is', 'undefined')]


# Generated at 2022-06-22 11:44:27.204487
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    class TestConditional:
        pass
    obj = Conditional()
    test_Conditional.__bases__ += (obj,)
    test_obj = test_Conditional()
    # test1
    conditional = 'var_1 is defined and var_2 is defined and var_3 is defined and var_4 is defined'
    res = test_obj.extract_defined_undefined(conditional)
    assert res == [('var_1', 'is', 'defined'), ('var_2', 'is', 'defined'), ('var_3', 'is', 'defined'), ('var_4', 'is', 'defined')]
    # test2
    conditional = 'var_1 is not defined or var_2 is not defined or var_3 is not defined or var_4 is not defined'
    res = test_obj.extract_defined_undefined

# Generated at 2022-06-22 11:44:39.648245
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    
    assert cond.extract_defined_undefined('1==2 and 3==4 or not (hostvars["localhost"] is undefined or hostvars["localhost"].foo is undefined and hostvars["localhost"].bar is undefined)') == \
        [('hostvars["localhost"]', 'is', 'undefined'), ('hostvars["localhost"].foo', 'is', 'undefined'), ('hostvars["localhost"].bar', 'is', 'undefined')]
    

# Generated at 2022-06-22 11:44:50.827185
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:45:02.376288
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    mc = Conditional()
    mc.vars = dict(a=1, b=2, c=3, d=4, e=5)
    mc.when = ['a == 1']
    assert mc.evaluate_conditional('', mc.vars) == True
    mc.when = ['b == 2']
    assert mc.evaluate_conditional('', mc.vars) == True
    mc.when = ['c == 3']
    assert mc.evaluate_conditional('', mc.vars) == True
    mc.when = ['d == 4']
    assert mc.evaluate_conditional('', mc.vars) == True
    mc.when = ['e == 5']
    assert mc.evaluate_conditional('', mc.vars) == True


# Generated at 2022-06-22 11:45:05.655622
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Prepare
    conditional = "a is defined or b is undefined or c is not defined"
    expected = [("a", "is", "defined"), ("b", "is", "undefined"), ("c", "is not", "defined")]

    # Execute
    conditional = Conditional()
    result = conditional.extract_defined_undefined(conditional=conditional)

    # Verify
    assert result == expected

# Generated at 2022-06-22 11:45:11.492538
# Unit test for constructor of class Conditional
def test_Conditional():
    # test_Conditional requires an instance of AnsibleLoader

    # TODO: mock AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    cond = Conditional(loader=loader)
    assert cond



# Generated at 2022-06-22 11:45:16.864616
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Fake it till you make it
    play_context = PlayContext()
    play_context._task = 'fake_task'

    ret = list(Conditional.evaluate_conditional.__code__.co_varnames)
    assert 'self' not in ret



# Generated at 2022-06-22 11:45:54.342840
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # This unit test checks that the method extract_defined_undefined, defined
    # in class Conditional, extracts each conditional from the input string
    # and returns the referenced variable, the conditional logic and the
    # conditional state for each match.
    conditional = Conditional()

    # Test a simple conditional defined
    test_string = 'hostvars[inventory_hostname].some_var is defined'
    expected_result = [('hostvars[inventory_hostname].some_var', 'is', 'defined')]
    assert conditional.extract_defined_undefined(test_string) == expected_result

    # Test a simple conditional undefined
    test_string = 'hostvars[inventory_hostname].some_var is undefined'

# Generated at 2022-06-22 11:46:07.275681
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.base import Base
    from ansible.parsing.yaml.dumper import AnsibleDumper

    class TestCond(Base, Conditional):
        def __init__(self, ds):
            super(TestCond, self).__init__(ds)

    # The class to test, and an instance
    test_class = TestCond({})

    # Some sample conditionals to test

# Generated at 2022-06-22 11:46:19.438218
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    Conditional.when.value = None
    Conditional.when.field = None

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    play_context = PlayContext()
    variable_manager = VariableManager()

    all_vars = dict(
        foo='abcd',
        bar='xyz',
        baz=42,
        answer=43
    )

    play_context.prompt = dict(foo='prompt foo', bar='prompt bar')
    play_context.vault_password = 'pass'

    templar = Templar(loader=None, variables=all_vars)
    test_conditional = Conditional(templar)

    # Use a custom list of conditionals to test this method.
   

# Generated at 2022-06-22 11:46:23.734831
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    example = Conditional(loader=loader)
    assert example.when is not None

# Generated at 2022-06-22 11:46:31.637412
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    import jinja2.environment

    host = Host("foohost")
    variable_manager = VariableManager()
    variable_manager.add_host_vars(host, {"foo":"bar"})
    variable_manager.add_host_vars(host, {"baz":"qux"})
    variable_manager.set_host_variable(host, "barbaz", "quxbaz")
    variable_manager.set_host_variable(host, "oof", "rab")
    variables = variable_manager.get_vars(host=host)

    conditional

# Generated at 2022-06-22 11:46:42.586196
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()

# Generated at 2022-06-22 11:46:54.455565
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:47:02.724166
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    loader = DataLoader()
    play_context = PlayContext()
    templar = Templar(loader=loader, variables={'test': 'value'})

    class TestClass(object):
        _when = []
        def __init__(self):
            self._loader = loader

    t = TestClass()

    # Test the case when one of the conditionals evaluates to False
    # In this case, evaluate_conditional should return False
    t._when = ['false_conditional']
    assert not t.evaluate_conditional(templar, {})

    # Test the case when the conditionals evaluates to True
    # In this case, evaluate_conditional should return True

# Generated at 2022-06-22 11:47:15.239052
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import jinja2
    from ansible.playbook.play_context import PlayContext

    class TestConditional(Conditional):
        def __init__(self):
            self.t = jinja2.Environment(loader=jinja2.DictLoader({'t.j2': '{{ hostvar_a }}'}))

# Generated at 2022-06-22 11:47:27.112998
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import jinja2

    class Empty():
        pass

    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            super(AttrDict, self).__init__(*args, **kwargs)
            self.__dict__ = self

    # test object
    obj = Conditional()
    obj.when = ["foo == 'bar'", "false", "", True]

    # test data
    variables = AttrDict(hostvars=AttrDict(), foo="bar")

# Generated at 2022-06-22 11:48:33.943177
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    playbook = PlayContext()
    templar = Templar(loader=None, variables=VariableManager(), shared_loader_obj=None)
    a = Conditional(loader=templar)

    assert a.extract_defined_undefined(conditional=None) == []
    assert a.extract_defined_undefined(conditional='') == []
    assert a.extract_defined_undefined(conditional='a') == []
    assert a.extract_defined_undefined(conditional='  ') == []
    assert a.extract_defined_undefined(conditional='a and b') == []

# Generated at 2022-06-22 11:48:43.914563
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    tester = Conditional()

    display.display("\n------------- Extract defined and undefined test -------------")
    test_strings = ["not foo is undefined",
                    "foo is defined",
                    "bar is defined and foo is undefined",
                    "foo is not defined and bar is not undefined",
                    "\"foo\" is not defined and bar is not \"undefined\""]
    for test_string in test_strings:
        display.display("Test string: %s" % test_string)
        display.display("Extracted: %s" % tester.extract_defined_undefined(test_string))

    display.display("\n------------- Extract defined and undefined test (not all defined/undefined) -------------")

# Generated at 2022-06-22 11:48:55.947136
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    assert not Conditional().evaluate_conditional(Templar(), dict())
    assert not Conditional().evaluate_conditional(Templar(), dict(a=[1]))
    assert Conditional(when=[]).evaluate_conditional(Templar(), dict())
    assert not Conditional(when=[]).evaluate_conditional(Templar(), dict(a=[1]))
    assert not Conditional(when=[None]).evaluate_conditional(Templar(), dict())
    assert Conditional(when=[{'a': [1]}]).evaluate_conditional(Templar(), dict(a=[1]))
    assert Conditional(when=[True]).evaluate_conditional(Templar(), dict())
    assert Conditional(when=[False]).evaluate_conditional(Templar(), dict(a=[1]))

# Generated at 2022-06-22 11:49:08.121111
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:49:20.565289
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    c = Conditional()

    play_context = PlayContext()
    play_context.remote_port = 22
    play_context.remote_addr = 'localhost'
    play_context.remote_user = 'root'

    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='Hello World')))
            ])

    play = Play().load(play_source, variable_manager=VariableManager(), loader=None)

# Generated at 2022-06-22 11:49:32.275395
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    all_vars = dict(
        dict(
            name="Alice",
            age=1,
            gender="F",
            foo="",
            bar=None,
            baz=["a","b"],
            ansible_ssh_user="foo",
        ),
        dict(
            ansible_ssh_host="bar",
        ),
        dict(
            hostvars=dict(
                nocollapse=dict(
                    ansible_ssh_host="bar",
                ),
            ),
        ),
    )

    # create a new data loader so we don't conflict with other unit tests
    loader = DataLoader()

    # setup context with tem

# Generated at 2022-06-22 11:49:42.765041
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.vars.manager import VariableManager

    class TestConditionalClass(Conditional):
        pass

    test_obj= TestConditionalClass()
    test_obj.when = [
        "ansible_os_family == 'RedHat' and ansible_distribution_version | int >= 7",
        "'foo' in groups and ansible_os_family == 'Debian' and ansible_os_major_version in version_compare('wheezy', '>=')",
        "'bar' in groups and ansible_distribution_major_version in version_compare('trusty', '>=')",
    ]

    variable_manager = VariableManager()

# Generated at 2022-06-22 11:49:54.451584
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    C.HOST_KEY_CHECKING = False

    # Create the base objects
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    # Create a task:
    task = Conditional(loader=loader)

    # With a playlist, the task doesn't need to be a list
    task._ds = dict(name="Test", when=['1 == 1', '1 == 2'])

    # should return True

# Generated at 2022-06-22 11:50:06.302424
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    vm = VariableManager()
    class testConditional(Conditional):
        def __init__(self):
            self._loader = None
            self.when = [ "{{ test_conditional }}", "{{ test_actor }}" ]
    test_conditional = testConditional()
    templar = Templar(loader=None, variables=vm)
    vm.set_facts({"test_conditional":True, "test_actor":True})

    result = test_conditional.evaluate_conditional(templar, vm._fact_cache)
    assert result is True
    vm.set_facts({"test_conditional":False, "test_actor":True})

# Generated at 2022-06-22 11:50:18.233001
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.task_include import TaskInclude

    # Create mocks
    templar = MagicMock()
    all_vars = MagicMock()
    conditional = "conditional"

    # Create class instance
    conditional = Conditional()
    conditional._check_conditional = MagicMock()
    conditional._check_conditional.return_value = True

    result = conditional.evaluate_conditional(templar, all_vars)

    # Check result
    assert result

    # Test with False
    conditional._check_conditional.return_value = False
    result = conditional.evaluate_conditional(templar, all_vars)

    # Check result
    assert result is not True

    # Test with Exception
    conditional._check_conditional.side_effect = Exception
