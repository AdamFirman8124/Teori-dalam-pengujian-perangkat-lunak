

# Generated at 2022-06-22 11:40:26.215012
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook.play_context import PlayContext

    conditional = Conditional(loader=None)
    assert conditional._when == []
    context = PlayContext()
    context.network_os = 'ios'
    conditional.on_network_os(context, 'ios')
    assert conditional._when[0] == 'ansible_network_os == "ios"'
    assert conditional._when[0] == 'ansible_network_os == "ios"'



# Generated at 2022-06-22 11:40:28.224973
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()
    assert conditional.when is not None
    assert conditional.when == []


# Generated at 2022-06-22 11:40:38.836987
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined("myvar is defined") == [("myvar", "is", "defined")]
    assert c.extract_defined_undefined("myvar is not defined") == [("myvar", "is not", "defined")]
    assert c.extract_defined_undefined("myvar is undefined") == [("myvar", "is", "undefined")]
    assert c.extract_defined_undefined("myvar is not undefined") == [("myvar", "is not", "undefined")]

# Generated at 2022-06-22 11:40:44.263381
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    text = "myvar is defined and hostvars['myvar'] is not defined and myvar is not 'myvalue' and myvar is 'myvalue'"
    expected = [('myvar', 'is', 'defined'), ('hostvars[\'myvar\']', 'is not', 'defined'), ('myvar', 'is not', '\'myvalue\'')]
    assert Conditional().extract_defined_undefined(text) == expected


# Generated at 2022-06-22 11:40:51.417984
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import jinja2
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import sys

    class TestConditional(Conditional):
        def __init__(self, loader):
            self._ds = dict()
            self._loader = loader
            self._name = "TestConditional"
            super(TestConditional, self).__init__(loader)

    # construct a fake loader for jinja
    class DummyLoader(object):
        def get_basedir(self, *args, **kwargs):
            pass

    tmpenv = jinja2.Environment(loader=DummyLoader())
    tmpenv.filters.update(C.DEFAULT_JINJA2_FILTERS)

    t = Templar(tmpenv)
    v = VariableManager()


# Generated at 2022-06-22 11:40:57.808772
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:41:11.094253
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    Test method extract_defined_undefined of class Conditional.
    :return:
    '''
    cond = Conditional()

    # Test 1
    conditional = "ansible_distribution == 'RedHat'"
    results = cond.extract_defined_undefined(conditional)
    assert not results

    # Test 2
    conditional = "ansible_distribution == 'RedHat' and 'foo' is undefined"
    results = cond.extract_defined_undefined(conditional)
    assert results == [('foo', 'is', 'undefined')]

    # Test 3
    conditional = "ansible_distribution == 'RedHat' and 'foo' is not defined"
    results = cond.extract_defined_undefined(conditional)
    assert results == [('foo', 'is', 'not defined')]

# Generated at 2022-06-22 11:41:21.966380
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import sys
    import tempfile
    import unittest

    from collections import namedtuple
    from jinja2 import Environment, FileSystemLoader
    from ansible.parsing.dataloader import DataLoader

    from ansible import context
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.constants import DEFAULT_VAULT_ID_MATCH

    # Conditional class does not get direct access to plugin_loader.
    # Thus we need to make sure that the plugin loader is properly initialized
    # with the current environment.
    context.CLIARGS = namedtuple('CLIArgs', ['vault_ids'])
    context.CLIARGS.vault_ids = [DEFAULT_VAULT_ID_MATCH]

# Generated at 2022-06-22 11:41:31.843097
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cases = [
        ('hostvars["foo"] not is undefined', [('hostvars["foo"]', 'not is', 'undefined')]),
        ('hostvars["foo"] not is undefined or hostvars["bar"] is defined', [('hostvars["foo"]', 'not is', 'undefined'), ('hostvars["bar"]', 'is', 'defined')]),
        ('foo not is defined or bar not is defined', [('foo', 'not is', 'defined'), ('bar', 'not is', 'defined')]),
        ('foo not is defined or bar not is defined or baz is undefined', [('foo', 'not is', 'defined'), ('bar', 'not is', 'defined'), ('baz', 'is', 'undefined')]),
    ]
    for case in cases:
        c = Conditional()
        assert c.extract

# Generated at 2022-06-22 11:41:43.858206
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template.template import Templar

    class DataStructure(object):
        pass

    class Task(Conditional):
        pass

    # init task object
    task_ds = DataStructure()
    task = Task(loader=None)
    task._ds = task_ds

    # init play_context object
    play_context = PlayContext()
    templar = Templar(loader=None, variables=play_context.accelerate_variables)


# Generated at 2022-06-22 11:42:04.380113
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    Cond = Conditional()

    # Test basic regexes
    assert Cond.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert Cond.extract_defined_undefined('foo not is defined') == [('foo', 'not is', 'defined')]
    assert Cond.extract_defined_undefined('foo not is undefined') == [('foo', 'not is', 'undefined')]
    assert Cond.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert Cond.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]
    # Test basic regexes (with hostvars)

# Generated at 2022-06-22 11:42:13.089382
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    fake_loader = DataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources='')
    fake_variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    fake_t = Templar(loader=fake_loader, variables=fake_variable_manager)

    # no when
    c = Conditional(loader=fake_loader)
    assert c.evaluate_conditional(fake_t, dict())

    # when is True
    c = Conditional(loader=fake_loader)
    c.when = True
    assert c.evaluate_conditional(fake_t, dict())

# Generated at 2022-06-22 11:42:25.471725
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    This unit tests the following conditional statements in method
    evaluate_conditional of class Conditional:
     - when: foo in bar
     - when: foo not in bar
     - when: foo == 1
     - when: foo != 1
     - when: foo is defined
     - when: foo is not defined
    '''

    import jinja2
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # all variables
    all_vars = dict(
        foo="bar",
        bar="bar",
        baz="12",
        aa=1,
        bb=2,
        cc=3,
    )

    # create template environment
    env = jinja2.Environment(undefined=jinja2.StrictUndefined)

# Generated at 2022-06-22 11:42:35.323467
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    pc = PlayContext()
    templar = Templar(pc, None)

    # hostvars is read-only, so we use a custom implementation here
    class FakeHostVars: pass
    hv = FakeHostVars()

    # some variables for the test playbook

# Generated at 2022-06-22 11:42:41.290441
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # Create a test playbook
    test_playbook = type('TestPlaybook', (object,), {})
    test_playbook.name = 'playbook_name'
    test_playbook.host_file = 'hosts'

    # Create templar with a variable path set to "host_vars"
    variable_manager = VariableManager()
    variable_manager.extra_vars = { 'host_vars': 'host_vars_value' }
    templar = Templar(loader=None, variables=variable_manager,
                      shared_loader_obj=test_playbook)

    # Create a test conditional

# Generated at 2022-06-22 11:42:51.786716
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    templar = Templar(play_context=play_context, loader=None, shared_loader_obj=None)
    conditional = Conditional()
    conditional.when = ['{{ 1 + 2 > 1 }}', '{{ 1 + 3 > 2 }}']
    assert conditional.evaluate_conditional(templar, dict())

    play_context.CLIARGS = {'vault_password': ''}
    conditional.when = ['{{ "vault" in playbook_dir.split("/") }}']
    assert conditional.evaluate_conditional(templar, dict())

    conditional.when = ['{{ "vault" in playbook_dir.split("/") }}', 'myvar is defined']
    assert conditional

# Generated at 2022-06-22 11:43:03.445189
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()


# Generated at 2022-06-22 11:43:14.727436
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional_object = Conditional()
    conditional_string = "hostvars['hostname'] is defined and (hostvars['hostname'].ansible_facts.os_family == 'RedHat' or hostvars['hostname'].ansible_facts.os_family == 'Debian') and hostvars['hostname'].ansible_facts.os_family is not undefined"
    result = conditional_object.extract_defined_undefined(conditional_string)

# Generated at 2022-06-22 11:43:19.836898
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader

    class MyYAMLObject(AnsibleBaseYAMLObject):
        def __init__(self, loader, node):
            super(MyYAMLObject, self).__init__(loader, node)
            self._ds = AnsibleMapping(loader=loader, node=node)

    class MyYAMLLoader(AnsibleLoader):
        def __init__(self, data):
            super(MyYAMLLoader, self).__init__()
            self._root = self.load_data(data)
            self._curr_doc = 0

    # Verify that all variables are available

# Generated at 2022-06-22 11:43:30.317888
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import sys
    import sys
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    if sys.version_info >= (2, 7):
        import unittest
        from ansible.parsing.yaml.objects import AnsibleUnicode
        from ansible.template import Templar

        class TestConditional(unittest.TestCase):

            class FakeDS:
                pass

            class FakeSelf(Conditional):
                def __init__(self, ds):
                    self.ds = ds
                    self._ds = ds
                    self.when = []
                    self._loader = None

            def setUp(self):
                self.ds = self.FakeDS()

            def tearDown(self):
                pass

# Generated at 2022-06-22 11:43:51.186389
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    try:
        import yaml
        from ansible.vars.manager import VariableManager
        from ansible.playbook.play_context import PlayContext
        from ansible.template import Templar
        has_yaml = True
    except:
        has_yaml = False
    import unittest

    if not has_yaml:
        raise unittest.SkipTest("No YAML module installed, cannot execute this test")

    fake_loader = None

    class TestConditional(Conditional):
        pass

    test_block = TestConditional(loader=fake_loader)
    test_block.when = ["ansible_os_family == 'Debian'"]


# Generated at 2022-06-22 11:44:00.468818
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    conditional = Conditional()
    conditional.when = '{{ hostvars[inventory_hostname + "_instance"] is undefined }} and \
                        (not (ansible_os_family == "RedHat" and not ansible_pkg_mgr in "yum") and \
                        ansible_os_family == "RedHat" and ansible_pkg_mgr == "yum" and group_names == "all_linux")'

    # All variables are defined in YAML in the following classes:
    # class AnsiblePlaybook(Base):
    #   class AnsiblePlay(Base):
    #     class AnsibleTask(Base):
    #       class ModuleArgs(Base):
    #       class Conditional(Conditional):
   

# Generated at 2022-06-22 11:44:13.578637
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'a': True, 'b': False}
    loader = DataLoader()
    templar = Templar(loader=loader, variable_manager=variable_manager)

    # Test with conditional as string
    temp_conditional = Conditional()

# Generated at 2022-06-22 11:44:22.155513
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    # 1st test, valid use
    defined_undefined = cond.extract_defined_undefined('hostvar is defined and hostvar is not undefined and hostvar is defined')
    assert defined_undefined == [('hostvar', 'is', 'defined'), ('hostvar', 'is', 'defined')]
    # 2nd test, invalid use
    defined_undefined = cond.extract_defined_undefined('hostvar')
    assert defined_undefined == []


# Generated at 2022-06-22 11:44:32.583931
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    # we need a host to work with
    mock_loader = DictDataLoader({
        "hostvars.yml": """
            foo:
                foo: 1
                bar: 2
                bam: 3
                bat: 4
                baz: 5
        """,
        "bar/vars.yml": """
            foo:
                bar: 6
        """,
    })

    inventory = InventoryManager(loader=mock_loader, sources=["hostvars.yml", "bar/vars.yml"])
    variable_manager = inventory.get_variable_manager()
    templar = Templar(loader=mock_loader, variables=variable_manager)

    # test hostvars
    res = Conditional()._

# Generated at 2022-06-22 11:44:41.137517
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c1 = Conditional()
    assert len(c1.extract_defined_undefined("foo is defined")) == 1
    assert len(c1.extract_defined_undefined("foo is not defined")) == 1
    assert len(c1.extract_defined_undefined("foo is not defined and bar is defined")) == 2
    assert len(c1.extract_defined_undefined("foo is not defined and bar is defined or baz is undefined")) == 3
    assert len(c1.extract_defined_undefined("not foo")) == 0



# Generated at 2022-06-22 11:44:51.504904
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined("") == []
    assert c.extract_defined_undefined("{{a}}") == []
    assert c.extract_defined_undefined("result|default(a) is defined") == [("a", "is", "defined")]
    assert c.extract_defined_undefined("hostvars['foo'] is not defined") == [("hostvars['foo']", "is not", "defined")]
    assert c.extract_defined_undefined("hostvars['foo'] is defined and hostvars['bar'] is not defined") == [("hostvars['foo']", "is", "defined"), ("hostvars['bar']", "is not", "defined")]

# Generated at 2022-06-22 11:45:03.024250
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook.play import Play
    from ansible.utils.color import stringc

    pb = Play()

    if not isinstance(pb, Conditional):
        raise AssertionError("Failed to instantiate playbook from Conditional")
    if pb.when != []:
        raise AssertionError("Failed to instantiate playbook 'when' from Conditional")
    if pb._validate_when("_validate_when", "when", []):
        raise AssertionError("Failed to set list of 'when'")
    if not isinstance(pb.when, list):
        raise AssertionError("Failed to set list of 'when'")

# Generated at 2022-06-22 11:45:15.113438
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('hostname is defined') == [('hostname', 'is', 'defined')]
    assert c.extract_defined_undefined('hostname is not defined') == [('hostname', 'is not', 'defined')]
    assert c.extract_defined_undefined('hostname is not defined or foobar is undefined') == [('hostname', 'is not', 'defined'), ('foobar', 'is', 'undefined')]
    assert c.extract_defined_undefined('hostname is not defined or foobar is not undefined') == [('hostname', 'is not', 'defined'), ('foobar', 'is not', 'undefined')]

# Generated at 2022-06-22 11:45:19.278123
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook.task_include import TaskInclude
    conditional = Conditional()
    assert isinstance(conditional, Conditional)
    assert conditional._validate_when.callable
    my_task_include = TaskInclude()
    assert isinstance(my_task_include, TaskInclude)
    assert my_task_include._validate_when.callable

# Generated at 2022-06-22 11:45:43.816686
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    mycond = 'a is defined or b is defined and c is undefined'
    assert cond.extract_defined_undefined(mycond) == [('a', 'is', 'defined'), ('b', 'is', 'defined'), ('c', 'is', 'undefined')]
    mycond = 'a.b.c.d is defined'
    assert cond.extract_defined_undefined(mycond) == [('a.b.c.d', 'is', 'defined')]



# Generated at 2022-06-22 11:45:56.478386
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    loader = DictDataLoader({})
    templar = Templar(loader=loader)
    conditional_obj = Conditional(loader)
    # test case 1 (True)
    conditional_obj._when = ['True']
    assert conditional_obj.evaluate_conditional(templar, {})
    # test case 2 (False)
    conditional_obj._when = ['False']
    assert not conditional_obj.evaluate_conditional(templar, {})
    # test case 3 (when as a list)
    conditional_obj._when = [True, True]
    assert conditional_obj.evaluate_conditional(templar, {})
    # test case 4 (when as a list)
    conditional_obj._when = [True, False]
    assert not conditional_obj.evaluate_conditional(templar, {})
    #

# Generated at 2022-06-22 11:46:08.841450
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    class TestConditional(Conditional): pass

    conditional = TestConditional()
    result = conditional.extract_defined_undefined('hostvars[inventory_hostname] is defined')
    assert [(u'hostvars[inventory_hostname]', u'is', u'defined')] == result

    result = conditional.extract_defined_undefined(u'hostvars["inventory_hostname"] is undefined')
    assert [(u'hostvars[inventory_hostname]', u'is', u'undefined')] == result

    result = conditional.extract_defined_undefined('hostvars[inventory_hostname] not is defined')
    assert [(u'hostvars[inventory_hostname]', u'not is', u'defined')] == result


# Generated at 2022-06-22 11:46:20.989952
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.playbook.play_context import PlayContext
    from ansible.template.safe_eval import safe_eval
    import jinja2
    cond = Conditional()

    # This first test evaluates a string for comparison against a variable.
    # It should ignore errors from the template engine and return True
    template_fail_conditional = "{{ foo is defined }}"
    templar = Templar(loader=None, variables={"foo": 1})
    assert cond.evaluate_conditional(templar, templar._available_variables)

    # This conditional will fail to evaluate, but since it's a boolean,
    # it should return True
    template_fail_conditional = True

# Generated at 2022-06-22 11:46:33.855050
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:46:42.760351
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    class DummyContext(PlayContext):
        def __init__(self):
            self.hostvars = dict()

    play_context = DummyContext()
    templar = Templar(loader=None, shared_loader_obj=None, variables=dict())
    templar._templates = dict()
    templar.set_available_variables(variables=dict())

    conditional = Conditional(loader=templar.loader)

    # Test that empty conditionals evaluate as True
    assert conditional.evaluate_conditional(templar, play_context.variable_manager.get_vars(loader=templar._loader, play=play_context)) is True

    conditional.when = None
    assert conditional.evaluate_cond

# Generated at 2022-06-22 11:46:46.770943
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    ''' test evaluate_conditional method '''
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()
    class TestConditional(Conditional):
        def __init__(self, *args, **kwargs):
            super(TestConditional, self).__init__(*args, **kwargs)
            self._loader = DataLoader()
            self._templar = Templar(loader=self._loader, variables={})
            self._ds = DataLoader()

    c = TestConditional()

# Generated at 2022-06-22 11:46:47.576302
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # TODO: fix test
    pass

# Generated at 2022-06-22 11:46:58.871185
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    c = Conditional()
    templar = Templar(loader=DataLoader())
    all_vars = dict()

    assert c.evaluate_conditional(templar, all_vars) is True

    c.when = ['']
    assert c.evaluate_conditional(templar, all_vars) is True

    c.when = ['abcde']
    assert c.evaluate_conditional(templar, all_vars) is False

    c.when = ['a is defined']
    assert c.evaluate_conditional(templar, all_vars) is False

    c.when = ['b is defined']

# Generated at 2022-06-22 11:47:10.978152
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:47:55.993695
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # Setup the test
    from ansible.playbook.null_loader import (
        AnsibleNullLoader,
        AnsibleNullVariableManager
    )


# Generated at 2022-06-22 11:48:07.177345
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def _extract_defined_undefined(*args):
        c = Conditional()
        return c.extract_defined_undefined(*args)

    assert _extract_defined_undefined('hostvars["foo"] is defined and hostvars["bar"] is defined') == [
        ('hostvars["foo"]', 'is', 'defined'),
        ('hostvars["bar"]', 'is', 'defined')
    ]
    assert _extract_defined_undefined('hostvars["foo"] is defined and hostvars["bar"] is not defined') == [
        ('hostvars["foo"]', 'is', 'defined'),
        ('hostvars["bar"]', 'is', 'not defined')
    ]

# Generated at 2022-06-22 11:48:18.221688
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Basic usage
    conditional = ConditionUnitTestTasks(when=['foo is defined'])
    assert conditional.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]

    # Basic usage with invalid negation
    conditional = ConditionUnitTestTasks(when=['foo is not defined'])
    assert conditional.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]

    # No defined condition
    conditional = ConditionUnitTestTasks(when=['foo'])
    assert conditional.extract_defined_undefined('foo') == []

    # Multiple defined conditions
    conditional = ConditionUnitTestTasks(when=['foo is not defined', 'bar is undefined'])

# Generated at 2022-06-22 11:48:26.836547
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.plugins import loader as plugin_loader
    from ansible.template import Templar

    all_vars = dict(foo=1, bar=dict(baz=2))
    templar = Templar(loader=plugin_loader.PluginLoader())
    c = Conditional()
    c.when = [
        'foo > 0 and bar.baz > 0',
        'foo > 0 or bar.baz > 5',
        'foo > 3',
        'bar.baz > 3',
        'foo > 5 or bar.baz > 5',
    ]
    assert c.evaluate_conditional(templar, all_vars)



# Generated at 2022-06-22 11:48:35.645546
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    class MyConditional(Conditional):
        def __init__(self, loader=None):
            super(Conditional, self).__init__()

    conditional = MyConditional()
    # Test all combinations of logic, state and variable
    for logic, state in (('is', 'defined'), ('is', 'undefined'), ('not', 'defined'), ('not', 'defined')):
        for var in ('hostvars[inventory_hostname]', 'a', 'a1', '_a', '_a1', 'hostvars[\'inventory_hostname\']', 'hostvars[\'a\']', 'hostvars[\'a1\']'):
            result=[(var, logic, state)]
            extracted = conditional.extract_defined_undefined('%s %s %s' % (var, logic, state))

# Generated at 2022-06-22 11:48:48.064837
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    loader = DataLoader()
    variables = VariableManager()
    inventory = InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)
    play_context = PlayContext()
    templar = Templar(loader=loader, variables=variables)

    all_vars = dict()
    all_vars['ansible_os_family'] = 'Linux'
    all_vars['linux_facts'] = {
        'distribution': 'Ubuntu',
        'distribution_version': '18.04'
    }

# Generated at 2022-06-22 11:48:57.644222
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeProxy

    loader = AnsibleLoader(None, variable_manager=None)
    templar = Templar(loader=loader, variables={})

    assert Conditional(loader=loader).evaluate_conditional(templar, {}) is True
    assert Conditional(loader=loader).evaluate_conditional(templar, {'a': True}) is True

    # test that variables are passed to jinja2
    assert Conditional(loader=loader).evaluate_conditional(templar, {'a': '1'}) == AnsibleUnsafeText('1') == '1'
   

# Generated at 2022-06-22 11:49:08.800143
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    ''' test_Conditional_extract_defined_undefined '''
    ansible_vars = {}
    ansible_vars['foo'] = 213
    ansible_vars['bar'] = 'a string'
    cond = Conditional()
    assert cond.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert cond.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]
    assert cond.extract_defined_undefined('foo is not defined and bar is defined') == [('foo', 'is not', 'defined'), ('bar', 'is', 'defined')]

# Generated at 2022-06-22 11:49:21.198528
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
   class foo(Conditional):
       def __init__(self):
           self._loader = None
           self._ds = None
           super(foo, self).__init__(self)


   # Testcase 1
   obj = foo()
   obj.when = list()
   obj.when.append(u'not (ansible_architecture == "i386" AND ansible_os_family == "Windows")')
   obj.when.append(u'not (ansible_architecture == "armv7l"  and ansible_distribution == "Raspbian GNU/Linux")')
   obj.when.append(u'ansible_architecture == "x86_64"')
   obj.when.append(u'ansible_distribution == "Ubuntu" or ansible_distribution == "Debian"')


# Generated at 2022-06-22 11:49:32.759627
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """
    Unit tests for method evaluate_conditional of class Conditional
    """

    # Test case 1:
        # when is empty
        # expect true
    test_hostvars = {}
    test_conditional = Conditional(loader=None)
    test_conditional.when = []
    test_templar = MockTemplar(variable_manager=MockVariableManager(test_hostvars))
    expect_result1 = True
    result1 = test_conditional.evaluate_conditional(test_templar, test_hostvars)
    assert result1 == expect_result1

    # Test case 2:
        # when is None
        # expect true
    test_hostvars = {}
    test_conditional = Conditional(loader=None)
    test_conditional.when = None
    test_tem