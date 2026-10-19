

# Generated at 2022-06-22 11:40:25.466080
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    module = AnsibleModule()

    mock_loader = DictDataLoader({
        'defaults/main.yml': '''
        variable1: 123
        variable2: 456

        variable3: 789

        variable4: 101112
        variable5: 131415

        variable6: 161718
        variable7: 192021
        variable8: 222324
        variable9: 252627

        variable10: 282930
        variable11: 313233
        variable12: 343536
        variable13: 373839
        variable14: 404142

        variable15: 434445
        '''
    })

    mock_connection = Connection(module._socket_path)

    mock_play_context = PlayContext()
    mock_play_context.connection = mock_connection
    mock_play_context.remote_addr

# Generated at 2022-06-22 11:40:26.775499
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    assert True

# Generated at 2022-06-22 11:40:37.310219
# Unit test for constructor of class Conditional
def test_Conditional():
    class TestClass(Conditional):
        def __init__(self, when=None):
            self.when = when
            self.__super.__init__(self)
        def evaluate_conditional(self):
            return True

    # Test case: check when is valid
    assert TestClass(when=[]).when == []
    assert TestClass(when=None).when == []
    assert TestClass(when=['']).when == ['']
    assert TestClass(when=True).when == [True]
    assert TestClass(when='foo').when == ['foo']
    assert TestClass(when=['foo']).when == ['foo']
    assert TestClass(when=['foo', 'bar']).when == ['foo', 'bar']
    assert TestClass(when='bar').when == ['bar']

    # Test case: check if

# Generated at 2022-06-22 11:40:46.565439
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    test_conditional1 = "var1 is defined and var2 is not defined"
    test_conditional2 = "var1 is undefined and var2 is defined"
    test_conditional3 = "var1 is defined or var2 is unknown"
    test_conditional4 = "var1 is not defined or var2 is unknown"
    test_conditional5 = "var1 not is undefined or var2 is not defined"
    test_conditional6 = "var1 is undefined or var2 is not defined"
    test_conditional7 = "var1 is undefined"
    test_conditional8 = "var1 is defined"
    test_conditional9 = "var1 is not defined"
    test_conditional10 = "hostvars['var1'] is defined"
    test_conditional11 = "hostvars['var1'] is undefined"

# Generated at 2022-06-22 11:40:58.273785
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

    assert conditional.extract_defined_undefined("hostvars['foo'] is not defined") == [('hostvars[\'foo\']', 'is not', 'defined')]
    assert conditional.extract_defined_undefined("hostvars['foo'] is defined") == [('hostvars[\'foo\']', 'is', 'defined')]
    assert conditional.extract_defined_undefined("hostvars['foo'] is defined and hostvars['bar'] is not defined") == [('hostvars[\'foo\']', 'is', 'defined'), ('hostvars[\'bar\']', 'is not', 'defined')]


# Generated at 2022-06-22 11:41:11.715062
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()

    # valid tests
    r = cond.extract_defined_undefined(u"foo is defined")
    assert r == [(u"foo", u"is", u"defined")], "should match defined test: %s" % r

    r = cond.extract_defined_undefined(u"foo is not defined")
    assert r == [(u"foo", u"is", u"not")], "should match defined test: %s" % r

    r = cond.extract_defined_undefined(u"foo is undefined")
    assert r == [(u"foo", u"is", u"undefined")], "should match defined test: %s" % r

    r = cond.extract_defined_undefined(u"foo not is undefined")

# Generated at 2022-06-22 11:41:22.039410
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestPlaybook:
        # make playbook.Base the superclass, so we can use its loader and datastructure
        # properties without having to redefine them
        __metaclass__ = type

# Generated at 2022-06-22 11:41:35.449367
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.unsafe_proxy import wrap_var

    setup_loader = DataLoader()
    setup_inventory = InventoryManager(loader=setup_loader, sources=["tests/units/modules/test_variables/hosts"])
    setup_variable_manager = VariableManager(loader=setup_loader, inventory=setup_inventory)

    # setup test object
    class TestConditional(object, Conditional):
        def __init__(self, loader, variable_manager):
            self._loader = loader
            self._variable_manager = variable_manager

# Generated at 2022-06-22 11:41:48.318331
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:41:59.290553
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # Regression test for: https://github.com/ansible/ansible/issues/11350
    # ansible-playbook -i hosts -e my_var="{ 'a': 'b' }" test.yml --list-hosts

    import unittest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    class TestConditional(unittest.TestCase):
        def setUp(self):
            self.loader = DataLoader()
            self.variable_manager = VariableManager()
            self.variable_manager.set_inventory(self.loader.load_from_file("tests/vars/inventory_var_type"))


# Generated at 2022-06-22 11:42:13.130469
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.base import Base

    class TestConditional(Base):
        pass

    assert TestConditional().extract_defined_undefined("foo is defined") == [("foo", "is", "defined")]
    assert TestConditional().extract_defined_undefined("foo is not defined") == [("foo", "is not", "defined")]
    assert TestConditional().extract_defined_undefined("foo is undefined") == [("foo", "is", "undefined")]
    assert TestConditional().extract_defined_undefined("foo is not undefined") == [("foo", "is not", "undefined")]
    assert TestConditional().extract_defined_undefined("foo not is undefined") == [("foo", "not is", "undefined")]
    assert TestConditional().extract_defined_

# Generated at 2022-06-22 11:42:25.524689
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display = Display()
    display.verbosity = False

    # self.evaluate_conditional(self, templar, variables)

    print("\n  testing Conditional.evaluate_conditional()...")
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {"foo": "xyz", "abc": "123", "def": "456", "xyz":"123"}
    templar = Templar(loader=dataloader, variables=variable_manager)

    c = Conditional(loader=dataloader)
    c.when = "foo == 'xyz'"

    #print("    simple test: %

# Generated at 2022-06-22 11:42:35.357533
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # pylint: disable=import-error,unused-variable
    from ansible.utils.display import Display
    display = Display()
    display.columns = 80
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    jinja_templar = Templar(loader=loader)

    cond2 = dict()
    cond2['vars2'] = False
    cond2['vars3'] = { 'arr': [ 'a', 'b' ] }
    cond2['vars4'] = 5
    cond2['vars5'] = 'string'
    cond2['vars6'] = 5
    cond2['bar'] = 'foo'
    cond2['vars7'] = 'PRD'

    cond = Conditional()


# Generated at 2022-06-22 11:42:41.315488
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    temp_task = Conditional()
    # test with empty string
    assert temp_task.extract_defined_undefined("") == []
    # test with defined/undefined variable
    assert temp_task.extract_defined_undefined("var is defined") == [("var", "is", "defined")]
    assert temp_task.extract_defined_undefined("var is undefined") == [("var", "is", "undefined")]
    assert temp_task.extract_defined_undefined("var is not defined") == [("var", "is not", "defined")]
    assert temp_task.extract_defined_undefined("var is not undefined") == [("var", "is not", "undefined")]
    # test with undefined/defined variable

# Generated at 2022-06-22 11:42:51.830796
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.templating import Templar


# Generated at 2022-06-22 11:43:03.444831
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import os
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # define vars
    os.environ["ansible_ssh_pass"] = "pass"
    os.environ["ansible_ssh_port"] = "2"
    inventory = InventoryManager(loader=loader, sources=["/etc/ansible/hosts"])

    templar = Templar(loader=loader, variables=inventory)
    test = Conditional()

# Generated at 2022-06-22 11:43:15.153300
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    my_conditional = """\
    ( (1 == 1) or (2 == 2) ) and ( \
    ( 1 == 1 and 2 == 2 ) and  \
    (not (1 == 0)) and  \
    (not (12 == 12 and 2 == 3)) and \
    (not (2 == 2 and 3 == 4)) and \
    ('foo' not in 'bar') and \
    ('foo' not in 'baz') and \
    ('foo' in 'foobar') and \
    ('foo' in 'foo') \
    )"""

    cond = Conditional()
    vars_manager = VariableManager()
    context = PlayContext()
    templar

# Generated at 2022-06-22 11:43:27.153705
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
    import ansible.plugins.loader as plugin_loader
    plugin_loader.add_directory(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

# Generated at 2022-06-22 11:43:38.743668
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:43:50.809388
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # test conditions:
    # 1. test when using not
    # 2. test when using "is"
    # 3. test when using "is not"
    # 4. test when using "is defined"
    # 5. test when using "is not defined"

    task = Conditional()

    result = task.extract_defined_undefined('a is not b')
    assert result[0][0] == 'a'
    assert result[0][1] == 'is not'
    assert result[0][2] == 'b'
    assert len(result) == 1

    result = task.extract_defined_undefined('a is b')
    assert result[0][0] == 'a'
    assert result[0][1] == 'is'
    assert result[0][2] == 'b'

# Generated at 2022-06-22 11:44:16.206169
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    d = DataLoader()
    pb = Playbook()
    t = Task()
    # Test if evaluate_conditional return False when any condition is False
    t._ds = Ds()
    t._ds = Ds()
    t._when = [False]
    t._loader = d
    t._play = Play()
    t._play.playbook = pb
    assert t.evaluate_conditional(t._loader.get_basedir(), {}) == False

    # Test if evaluate_conditional return False when a condition with
    # undefined variable
    t._when = [True, "{{ undefined_variable }}"]
    assert t.evaluate_conditional(t._loader.get_basedir(), {}) == False

    # Test if evaluate_conditional return False when a condition with
    # undefined variable in play vars
    t._

# Generated at 2022-06-22 11:44:28.043617
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Test for method Conditional._check_conditional of class Conditional
    '''
    conditional = Conditional()
    def _variable_manager_mock():
        variable_manager = Mock()
        variable_manager.get_vars = Mock()
        variable_manager.get_vars.return_value = {}
        variable_manager.set_host_variable = Mock()
        return variable_manager

    variable_manager = _variable_manager_mock()
    templar = Templar(loader=None, variables=variable_manager)

    # Test with one or multiple valid test str
    test_cond1 = "hostvars[inventory_hostname]|d({})|length > 0 and not (play_hosts|d([]))|length > 0"

# Generated at 2022-06-22 11:44:40.219237
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''Unit test for method evaluate_conditional of class Conditional'''
    from ansible.playbook.base import Base
    from ansible.template import Templar
    from ansible.variables import VariableManager
    class DerivedClass(Base, Conditional):
        pass
    dc = DerivedClass()

    play_context = dict(basedir='/playbook/dir')
    templar = Templar(loader=None, variables=VariableManager(), play_context=play_context)

    # Test for when is None
    dc._when = None
    assert dc.evaluate_conditional(templar, dict())
    dc._when = None
    assert dc.evaluate_conditional(templar, dict(a=1))

    # Test for when is True
    dc._when = True

# Generated at 2022-06-22 11:44:51.451433
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import jinja2
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Note: Requires ansible.cfg
    C.CONFIG_FILE = "./ansible.cfg"

    # Simple test
    c = Conditional()
    c.when = ["foo"]
    templar = Templar(loader=None, variables={})
    assert c.evaluate_conditional(templar, {}) == True

    # Simple test
    c = Conditional()
    c.when = ["foo is not True"]
    templar = Templar(loader=None, variables={'foo': True})
    assert c.evaluate_conditional(templar, {}) == False

    # Simple test
    c = Conditional()
    c.when = ["foo is not True"]


# Generated at 2022-06-22 11:45:02.976567
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    playbook_vars = dict(
        test_cond1="test_cond1",
        test_var1="test_var1",
        test_var2="test_var2",
        test_var3="test_var3",
        test_var4="test_var4",
        test_var5={
            "test_var5_1": list(range(10))
        },
        test_var6={
            "test_var6_1": list(range(10)),
            "test_var6_2": list(range(10))
        },
    )
    play_context = PlayContext()
    play_context.prompt = lambda x, y, z, a=None: None

# Generated at 2022-06-22 11:45:12.905275
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    conditional = Conditional()

    assert conditional.extract_defined_undefined('a is defined') == [('a', 'is', 'defined')]
    assert conditional.extract_defined_undefined('a is not defined') == [('a', 'is not', 'defined')]
    assert conditional.extract_defined_undefined('a is undefined') == [('a', 'is', 'undefined')]
    assert conditional.extract_defined_undefined('a is not undefined') == [('a', 'is not', 'undefined')]

    assert conditional.extract_defined_undefined('a is not defined and b is defined') == [('a', 'is not', 'defined'), ('b', 'is', 'defined')]

# Generated at 2022-06-22 11:45:20.429894
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    assert cond.extract_defined_undefined("foo bar") == []
    # Correctly identify not is defined
    assert cond.extract_defined_undefined("foo not is defined") == [('foo', 'not is', 'defined')]
    # Correctly identify not is undefined
    assert cond.extract_defined_undefined("foo not is undefined") == [('foo', 'not is', 'undefined')]
    # Correctly identify multiple test
    assert cond.extract_defined_undefined("foo is undefined or bar not is defined") == [('foo', 'is', 'undefined'), ('bar', 'not is', 'defined')]
    # Correctly identify undefined
    assert cond.extract_defined_undefined("foo is undefined") == [('foo', 'is', 'undefined')]
    # Correct

# Generated at 2022-06-22 11:45:32.453101
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:45:45.235302
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    """Check if Conditional class extracts undefined variables correctly"""
    c = Conditional()
    assert c.extract_defined_undefined("hostvars") == []
    assert c.extract_defined_undefined("hostvars[foo]") == []
    assert c.extract_defined_undefined("hostvars[foo] is undefined") == [("hostvars[foo]", "is", "undefined")]
    assert c.extract_defined_undefined("hostvars[foo] is not defined") == [("hostvars[foo]", "is not", "defined")]
    assert c.extract_defined_undefined("hostvars[foo] not is undefined") == [("hostvars[foo]", "not is", "undefined")]

# Generated at 2022-06-22 11:45:57.538598
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
  e = Conditional()
  # test _check_conditional
  assert e._check_conditional("1") == True
  assert e._check_conditional("True") == True
  assert e._check_conditional("0") == False
  assert e._check_conditional("False") == False
  assert e._check_conditional("''") == False
  # test extract_defined_undefined
  assert e.extract_defined_undefined("1") == []
  assert e.extract_defined_undefined("2 + 3") == []
  assert e.extract_defined_undefined("1 is defined") == [ ('1', 'is', 'defined') ]
  assert e.extract_defined_undefined("1 is not defined") == [ ('1', 'is not', 'defined') ]
  assert e.extract_

# Generated at 2022-06-22 11:46:27.847217
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()
    assert isinstance(conditional, Conditional)

# Generated at 2022-06-22 11:46:39.072826
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # check that conditional string with no defined/undefined is handled
    # properly (no match found, empty list returned)
    assert Conditional().extract_defined_undefined("foo == bar") == []
    assert Conditional().extract_defined_undefined("foo is bar") == []
    assert Conditional().extract_defined_undefined("foo == 'bar'") == []
    assert Conditional().extract_defined_undefined("foo is 'bar'") == []

    # check that conditional string with one defined/undefined is handled
    # properly (single match found, list containing single match returned)
    assert Conditional().extract_defined_undefined("foo.bar.baz is undefined") == [('foo.bar.baz', 'is', 'undefined')]

# Generated at 2022-06-22 11:46:50.227382
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    ''' test_Conditional.extract_defined_undefined '''
    cond = Conditional()

# Generated at 2022-06-22 11:47:00.076828
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    #pylint: disable=no-member
    # this member is not created at compile time
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    ###########################################################################
    # evaluate_conditional tests for TaskInclude

    # Case 1:
    # Input:
    #   - Conditional: False
    #   - Evaluated conditional (0): False
    #   - Result: False
    #   - Templated condition: False
    # Expectation:
    #   - Return False
    task_include_False = TaskInclude()
    task_include_False._ds = dict()
    task_include_False._ds["name"] = 'include_false'
    task_include_False.when = False

# Generated at 2022-06-22 11:47:12.304480
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined("") == []

    assert Conditional().extract_defined_undefined("a b  or c") == []
    assert Conditional().extract_defined_undefined("a or b and c") == []

    assert Conditional().extract_defined_undefined("a is defined") == [("a", "is", "defined")]
    assert Conditional().extract_defined_undefined("a not is defined") == [("a", "not is", "defined")]
    assert Conditional().extract_defined_undefined("a not is not defined") == [("a", "not is not", "defined")]
    assert Conditional().extract_defined_undefined("a is undefined") == [("a", "is", "undefined")]
    assert Conditional().extract_defined_und

# Generated at 2022-06-22 11:47:24.967855
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    import os
    import sys
    import unittest

    # Define a class that inherits Conditional
    class SomeClass(Conditional):
        pass

    # Build some variables
    fake_loader = dict(
        path_exists=os.path.exists,
        stat = lambda x: os.stat(x),
        is_executable = os.access,
        contains = lambda x,y: y in x,
        to_text = to_text,
        to_nice_yaml = to_text,
    )


# Generated at 2022-06-22 11:47:36.535489
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.playbook.task import Task

    # Setup a basic task
    loader = DataLoader()
    inv_mgr = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inv_mgr)
    task = Task()
    task._role = None
    task.variable_manager = variable_manager
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=None))

    # test: no conditional

    result = task.evaluate_conditional(templar, variable_manager.get_vars(play=None))

# Generated at 2022-06-22 11:47:49.132117
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-22 11:47:55.439234
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class X:
        def __init__(self):
            self._loader = False
            self._ds = None
            self._when = ["a is defined"]

    def test_evaluate_conditional(x, y):
        return x.evaluate_conditional(y, {"a": True})

    assert test_evaluate_conditional(X(), "1")
    assert not test_evaluate_conditional(X(), None)

# Generated at 2022-06-22 11:48:07.128049
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook import PlayBook
    from ansible.playbook.play import Play, PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.vars import VariableManager

    # Playbook
    # optional loaders.
    play = Play()
    play_context = PlayContext()
    loader = None

    # Need a fake inventory
    variable_manager = VariableManager()
    fake_inventory = dict()
    variable_manager.set_inventory(fake_inventory)

    # Make a fake task.
    fake_task = Task()
    fake_task.action = 'fake'
    fake_task.args = dict()
    fake_task.register = 'result'


# Generated at 2022-06-22 11:49:15.440469
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    module_loader = 'test_module_loader'
    connection = 'local'
    play_context = 'test_play_context'
    loader = 'test_loader'
    variable_manager = 'test_variable_manager'
    loader = 'test_loader'
    passwords = 'test_passwords'
    data_structure = {'hosts': 'localhost', 'vars': {}}
    templar = 'test_templar'
    all_vars = 'test_all_vars'

    setattr(connection, '_play_context', play_context)
    setattr(play_context, 'connection', connection)

# Generated at 2022-06-22 11:49:25.317398
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    templar = variable_manager.get_loader()
    fail_vars = dict(
        one="foo",
        two="{{two}}",
        three="{{one}}",
        four="bar",
        five="baz",
        six="{{six}}",
        seven="{{ six }}"
    )

    passed_vars = dict(
        one="passed",
        two="passed",
        three="passed",
        four="passed",
        five="passed",
        six="passed",
        seven="passed"
    )

    # pass the variables to evaluate
   

# Generated at 2022-06-22 11:49:37.498317
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    display.verbosity = 4

    class DummyClass():
        def __init__(self, conditional):
            self.when = conditional

    # test with simple single conditional
    data = "{{ foo is defined }}"
    conditional = Conditional()
    result = conditional.extract_defined_undefined(data)
    assert result == [('foo', 'is', 'defined')]

    # test with simple single conditional with new lines.
    # (this ensures the regex is working properly)
    data = """
    {{ foo is
    defined }}
    """
    result = conditional.extract_defined_undefined(data)
    assert result == [('foo', 'is', 'defined')]

    # test with multiple conditionals on one line
    data = "{{ foo is defined }} and {{ bar is defined }}"
    result = conditional.extract

# Generated at 2022-06-22 11:49:47.245289
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    vars_manager = VariableManager()

    inventory = InventoryManager(loader=loader, sources='')
    hostobj = inventory.add_host("127.0.0.1")
    hostobj.vars = {'ansible_connection': 'local', 'local_vars': "some value"}

    display.verbosity = 4
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    def test_it(conditional, all_vars, expected):
        obj = Conditional(loader=loader)
        obj._ds = {"result": False, "changed": False}
        obj.when = conditional
        result

# Generated at 2022-06-22 11:49:55.366500
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    obj = Conditional(loader='something')
    obj._ds = 'somedata'

    obj.when = [
        {'cond1': 1},
        {'cond2': 2},
        '3',
        ['4', '5'],
        {'cond6': 6},
        7
    ]

    obj._check_conditional = lambda x, y, z: x == y

    assert obj.evaluate_conditional('something', 'something') == True

    obj._check_conditional = lambda x, y, z: x != y

    assert obj.evaluate_conditional('something', 'something') == False



# Generated at 2022-06-22 11:50:07.276016
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from units.mock.loader import DictDataLoader
    from units.mock.path import MockPath
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()

    path = MockPath()
    basedir = path.getcwd()
    loader.set_basedir(basedir)

    # the following are valid python identifiers, so they are valid Jinja2 variables
    # the regex in VALID_VAR_REGEX is separate from val_vars below since a string will
    # be considered valid if it starts with a valid identifier
    val_vars = ['foo', 'foo_bar', '_bar_foo']
    # the following are invalid python identifiers and so they are not valid Jinja2
    # variables