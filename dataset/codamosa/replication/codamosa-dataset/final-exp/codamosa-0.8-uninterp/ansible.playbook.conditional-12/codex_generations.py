

# Generated at 2022-06-22 11:40:26.878980
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.utils.vars import combine_vars

    # Simulate basic inventory
    loader = DictDataLoader({})
    inventory = InventoryManager(loader=loader)
    vault_password = VaultLib(['hideme'])

    # Simulate facts
    my_vars = {'foo': 'bar', 'bar': 'baz'}
    my_host = inventory.get_host('localhost')
    my_host.v

# Generated at 2022-06-22 11:40:32.661151
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    p = Conditional()
    assert p.extract_defined_undefined("hostvars['foo'] is defined") == [("hostvars['foo']", "is", "defined")]
    assert p.extract_defined_undefined("foo not is defined") == [("foo", "not is", "defined")]
    assert p.extract_defined_undefined("foo is not defined and bar is undefined") == [("foo", "is not", "defined"), ("bar", "is", "undefined")]

# Generated at 2022-06-22 11:40:37.558961
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.base import Base
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    class TestClass(Base):
        pass
    test_class = TestClass()
    test_class._loader = DataLoader()
    test_class._variable_manager = VariableManager(loader=test_class._loader)

    templar = Templar(loader=test_class._loader, variables=test_class._variable_manager.get_vars(play=test_class))

    # Boolean value
    test_class.when = True
    assert(test_class.evaluate_conditional(templar, {}) == True)

    test_class.when = False

# Generated at 2022-06-22 11:40:43.963954
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    test_Conditional_extract_defined_undefined
    :return:
    '''
    cond = Conditional()
    cond_expr = "vn_interfaces.interface[0].name is defined and vn_interfaces.interface[0].name == 'lo'"

    assert(len(cond.extract_defined_undefined(cond_expr)) == 2)
    assert(len(cond.extract_defined_undefined(cond_expr)[0]) == 3)
    assert(cond.extract_defined_undefined(cond_expr)[0][0] == 'vn_interfaces.interface[0].name')
    assert(cond.extract_defined_undefined(cond_expr)[0][1] == 'is')

# Generated at 2022-06-22 11:40:51.305009
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    # regular use cases
    assert [('hostvars[inventory_hostname]', 'is', 'defined')] == c.extract_defined_undefined("hostvars[inventory_hostname] is defined")
    assert [('foo', 'not is', 'undefined')] == c.extract_defined_undefined("foo not is undefined")
    assert [('foo', 'is', 'undefined')] == c.extract_defined_undefined("foo is undefined")
    assert [('foo', 'is not', 'defined')] == c.extract_defined_undefined("foo is not defined")
    assert [('foo', 'is', 'defined')] == c.extract_defined_undefined("foo is defined")
    # not matching

# Generated at 2022-06-22 11:40:56.738336
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    when = "string and hostvars[inventory_hostname] == 'localhost' and not hostvars['localhost']['working'] and hostvars['localhost']['failed'] is defined"

    def_undef = c.extract_defined_undefined(when)
    assert def_undef[0] == ('hostvars[inventory_hostname]', '==', 'localhost')
    assert def_undef[1] == ('hostvars[\'localhost\'][\'working\']', 'not', 'defined')
    assert def_undef[2] == ('hostvars[\'localhost\'][\'failed\']', 'is', 'defined')



# Generated at 2022-06-22 11:41:05.745041
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:41:18.470880
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined("hostvars['hostname'] is not defined") == [('hostvars[\'hostname\']', 'is not', 'defined')]
    assert Conditional().extract_defined_undefined("foo is defined") == [('foo', 'is', 'defined')]
    assert Conditional().extract_defined_undefined("foo is not defined") == [('foo', 'is not', 'defined')]
    assert Conditional().extract_defined_undefined("foo is defined or bar is defined") == [('foo', 'is', 'defined'), ('bar', 'is', 'defined')]
    assert Conditional().extract_defined_undefined("foo is undefined") == [('foo', 'is', 'undefined')]

# Generated at 2022-06-22 11:41:30.775671
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # test with when as boolean
    obj = Conditional()
    obj.when = False
    assert not obj.evaluate_conditional(None, None)

    obj.when = True
    assert obj.evaluate_conditional(None, None)

    # test with when as string
    obj.when = "some_non_empty_string"
    assert obj.evaluate_conditional(None, None)

    obj.when = ""
    assert not obj.evaluate_conditional(None, None)

    # test with when as {list, of, values}
    obj.when = [True, False, "some_non_empty_string", ""]
    assert obj.evaluate_conditional(None, None)
    assert not obj.when[1]

    obj.when = [False, True, "", "some_non_empty_string"]


# Generated at 2022-06-22 11:41:40.158907
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
        This function tests the method evaluate_conditional of class Conditional.
        More specifically:
            1. Tests whether evaluate_conditional returns False if any of the
               conditionals in self.when evaluates as such.
            2. Tests whether evaluate_conditional raises an AnsibleError exception
               if the attempt to evaluate a conditional fails.
    '''

    # Define test values for conditionals
    CONDITIONALS_TRUE = ['1 == 1', '1 == 1 or 1 == 2', '1 == 1 and 1 == 2']
    CONDITIONALS_FALSE = ['1 == 2', '1 == 2 or 1 == 3', '1 == 2 and 1 == 3']

    # Test whether evaluate_conditional returns False if any of the conditionals in self.when evaluates as such.

# Generated at 2022-06-22 11:41:57.290241
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test evaluating jinja2 conditional
    assert Conditional().evaluate_conditional(template(), {'var': True}, None, None)
    assert Conditional().evaluate_conditional(template(), {'var': False}, None, None)

    # Test evaluating non-jinja2 conditional
    assert Conditional().evaluate_conditional(template(), {'var': True}, None, None)
    assert Conditional().evaluate_conditional(template(), {'var': False}, None, None)


# Generated at 2022-06-22 11:42:07.713503
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import get_all_plugin_loaders

    class TestConditional(Conditional):
        def __init__(self, loader=None):
            self._loader = None
            self._name = 'test'
            self._connection = 'local'
            self._when = [None]
            self._ds = {'localhost': { 'ansible_connection': 'local' }}

    ds = { 'localhost': { 'ansible_connection': 'local' } }
    context = PlayContext()
    context.vars = VariableManager()

# Generated at 2022-06-22 11:42:14.095385
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    host_vars = {
        'foo': {
            'bar': 'test',
        },
    }
    module_vars = {}
    all_vars = {'hostvars': host_vars, 'vars': module_vars}
    conditional = Conditional()
    templar = AnsibleTemplar()
    condition = conditional.evaluate_conditional(templar, all_vars)
    assert condition is True


# Generated at 2022-06-22 11:42:26.323145
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.template import Templar

    data = {'a': 1, 'b': 2, 'c': 3}
    t = Templar(None, variables=data)


# Generated at 2022-06-22 11:42:35.623105
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar

    play = Play.load(dict(
        name="test play",
        hosts="all",
        tasks=[
            dict(
                name="test task",
                action=dict(
                    module="shell",
                    args="ls",
                ),
            ),
        ],
    ), loader=None)
    task = play.get_tasks()[0]
    templar = Templar(loader=None, variables=dict(
        hostvars=dict(
            localhost=dict(
                var1=100,
            ),
        ),
    ))

    # Test removing defined/undefined tests from conditional in the method evaluate_conditional

# Generated at 2022-06-22 11:42:49.362464
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    available_variables = dict(
        ansible_check_mode='yep',
        minion='foo',
        master='bar',
        minion2='foo',
        master2='bar',
        foo='bar',
        bar='foo',
        hostvars=dict(
            foo=dict(bar='foo'),
            bar=dict(foo='bar'),
        ),
        groups=dict(
            foo=['minion', 'minion2'],
            bar=['master', 'master2'],
        ),
        a_dict=dict(
            b='c',
        ),
    )
    play_context = PlayContext()

# Generated at 2022-06-22 11:43:01.797412
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    display = Display()

    my_vars = dict(
        foo='foo',
        bar='bar',
        baz='baz',
        file='/etc/passwd',
    )

    play_context = PlayContext()
    templar = Templar(loader=None, variables=my_vars)

    # test conditional with no jinja-style variables in string
    conditional = "foo != bar"
    assert Conditional().evaluate_conditional(templar, my_vars) is True

    # test conditional with jinja-style variables in string
    conditional = "{{ foo }} != {{ bar }}"
    assert Conditional().evaluate_conditional(templar, my_vars) is True

    # test conditional

# Generated at 2022-06-22 11:43:13.441446
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    def test_conditional(conditional, all_vars, expected):
        if isinstance(all_vars, dict):
            for k, v in list(all_vars.items()):
                if isinstance(v, dict) or isinstance(v, list):
                    display.debug("        %s: %s" % (k, v))
                else:
                    display.debug("        %s: '%s'" % (k, v))
        else:
            display.debug("        %s" % (all_vars))
        conditional = Conditional()
        templar = conditional.loader.templar
        templar._available_variables = all_vars
        result = conditional.evaluate_conditional(templar, all_vars)
        if not (result == expected):
            raise Assertion

# Generated at 2022-06-22 11:43:25.345329
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    a = Conditional()
    b = a.extract_defined_undefined("foo is defined and bar is not defined")
    assert b == [('foo', 'is', 'defined'), ('bar', 'is not', 'defined')]
    c = a.extract_defined_undefined("foo is defined and 'bar' is not defined")
    assert c == [('foo', 'is', 'defined'), ('bar', 'is not', 'defined')]
    d = a.extract_defined_undefined("'foo' is defined and 'bar' is not defined")
    assert d == [('foo', 'is', 'defined'), ('bar', 'is not', 'defined')]
    e = a.extract_defined_undefined("foo is defined and bar")
    assert e == [('foo', 'is', 'defined')]

# Generated at 2022-06-22 11:43:37.340752
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook import Play

    # test data

# Generated at 2022-06-22 11:43:56.194464
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    tests = {
        'foo is defined': [('foo', 'is', 'defined')],
        'foo is not defined': [('foo', 'is', 'not'), ('defined', '', '')],
        'foo not is defined': [('foo', 'not', ''), ('is', '', ''), ('defined', '', '')],
        'foo and bar is defined': [('bar', 'is', 'defined')],
        'foo is defined or bar is not defined':
            [('foo', 'is', 'defined'), ('bar', 'is', 'not'), ('defined', '', '')],
    }
    for test, result in tests.items():
        assert conditional.extract_defined_undefined(test) == result


# Generated at 2022-06-22 11:43:59.751459
# Unit test for constructor of class Conditional
def test_Conditional():
    display.columns = 80
    display.verbosity = 1
    conditional = Conditional()
    assert conditional._validate_when('', '', None) is None



# Generated at 2022-06-22 11:44:12.959752
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    def _test(test_strings, expected_list):
        actual = Conditional().extract_defined_undefined(test_strings)
        if actual == expected_list:
            return 'OK'
        else:
            return 'Expected %s, Actual %s' % (expected_list, actual)

    # test case for single defined_undefined pattern in string
    test_strings1 = 'a is defined and b is undefined'
    expected_list1 = [('a', 'is', 'defined')]
    assert _test(test_strings1, expected_list1) == 'OK'

    # test case for multiple defined_undefined patterns in string
    test_strings2 = 'a is not defined and b not is undefined and c is defined'

# Generated at 2022-06-22 11:44:26.270022
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    # pylint: disable=import-error
    from ansible.playbook.helpers import load_list_of_blocks


# Generated at 2022-06-22 11:44:34.661174
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    loader = DataLoader()
    invm = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=invm)
    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-22 11:44:46.774019
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    myCond = Conditional()


# Generated at 2022-06-22 11:44:57.926346
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    variable_manager = VariableManager()
    templar = Templar(loader=None, variables=variable_manager)

    # Test case:
    #    - when: test_var == "test_value"
    # Check if result of evaluation is "test_value"

    conditional = 'test_var == "test_value"'
    all_vars = {'test_var': 'test_value'}

    conditional_obj = Conditional()

    result = conditional_obj.evaluate_conditional(templar, all_vars)

    assert result



# Generated at 2022-06-22 11:45:05.842112
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestConditional(Conditional):
        def __init__(self, loader=None):
            super(TestConditional, self).__init__(loader=loader)

# Generated at 2022-06-22 11:45:17.536764
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Test the method evaluate_conditional of class Conditional
    '''
    from ansible.playbook import Play, Playbook, PlayContext, PlaybookExecutor
    from ansible.template import Templar

    pb = PlaybookExecutor(playbooks=[Playbook.load('/tmp/playbook.yml', variable_manager=None, loader=None)])
    pc = pb._tqm._inventory.get_variable_manager()
    play = Play().load(dict(
        name = "Conditional test",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='foo'))),
        ]
    ), variable_manager=pc, loader=pb._loader)

# Generated at 2022-06-22 11:45:19.030278
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # TODO: Add test cases
    pass


# Generated at 2022-06-22 11:45:50.514655
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    Conditional._validate_when = Conditional.__dict__['_validate_when']
    Conditional.extract_defined_undefined = Conditional.__dict__['extract_defined_undefined']
    Conditional._check_conditio

# Generated at 2022-06-22 11:46:01.349742
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class TestConditional(Conditional):
        def __init__(self, loader, when):
            self._loader = loader
            self.when = when

    # run tests per playbook

# Generated at 2022-06-22 11:46:04.821091
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    test_class = Conditional()
    test_class._loader = None
    assert test_class.evaluate_conditional('cond') == False
    assert test_class.evaluate_conditional(True) == True



# Generated at 2022-06-22 11:46:17.743416
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar

    # Patch the constants for the test
    C.DEFAULT_HASH_BEHAVIOUR = "merge"
    C.DEFAULT_HASH_DELIMITER = ":"

    fake_loader = DictDataLoader({})
    c = Conditional(loader=fake_loader)

    # Patch the templar for the test
    c._templar = Templar(loader=fake_loader)
    c._templar._available_variables = dict()

    # Is the variable 'a' defined?
    assert c.evaluate_conditional(c._templar, dict(a=1)) == True
    assert c.evaluate_conditional(c._templar, dict(a=0)) == True

# Generated at 2022-06-22 11:46:21.487324
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    assert True == Conditional.evaluate_conditional(True)
    assert True == Conditional.evaluate_conditional(False, True)
    assert False == Conditional.evaluate_conditional(False)


# Generated at 2022-06-22 11:46:34.173115
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # test_data_00

    try:
        import __main__
        setattr(__main__, '__file__', '/test/ansible_modlib.conditional.Conditional/evaluate_conditional/__init__.py')
    except (ImportError, AttributeError):
        pass

    import ansible.module_utils.basic
    import ansible.module_utils.urls
    import ansible.module_utils.six
    import ansible.module_utils.json
    import ansible.module_utils.six.moves
    import ansible.module_utils.six.moves.urllib.parse
    import ansible.module_utils.six.moves.urllib.request
    import ansible.module_utils.six.moves.urllib.error
    import ansible.module_utils

# Generated at 2022-06-22 11:46:42.054097
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=None, sources=None)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play_context = PlayContext()
    t = Templar(loader=None, variables=variable_manager, playcontext=play_context)

    conditional = Conditional()
    conditional._when = ["1", "2", "0", "", "5", None, "0"]
    result = conditional.evaluate_conditional(t, {})

    assert result == False

# Generated at 2022-06-22 11:46:49.174169
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class TestModule:
        class Base(Conditional):
            pass

    # Create an instance of the class

    # Set up some fake variable context for evaluation
    templar = TestModule.Base()
    templar._loader = DictDataLoader({})
    fake_all_vars = dict(
        foo=dict(
            bar=dict(
                baz=True
            )
        )
    )

    # Evaluate the conditional
    true = templar.evaluate_conditional(templar, fake_all_vars)



# Generated at 2022-06-22 11:46:59.513742
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class DummyAnsibleModule(object):
        def __init__(self, kwargs):
            self.params = kwargs

    class DummyCommand(object):
        def __init__(self):
            self.connection = "local"

    def my_filter(*args, **kwargs):
        return True

    class DummyTemplar(object):
        def __init__(self):
            self.available_variables = {}
            self.environment = Jinja2Environment(extensions=set(['jinja2.ext.do']))
            self.environment.filters['booltest'] = my_filter
            #self.environment.loader = self._loader
            self.final_context = {}
            self.noop_vars = {}


# Generated at 2022-06-22 11:47:11.905910
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible import constants as C
    from ansible.vars import VariableManager

    conditional = Conditional()


# Generated at 2022-06-22 11:47:53.866935
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    templar = Templar(loader=None)
    host = Host()

    # Test True conditional
    conditional = 'hostvars[inventory_hostname] == inventory_hostname'
    host.vars = {'inventory_hostname': 'localhost'}
    assert Conditional().evaluate_conditional(templar, host.vars) is True
    # Test Undefined conditional
    conditional = 'hostvars[inventory_hostname] == foo'
    host.vars = {'inventory_hostname': 'localhost'}
    assert Conditional().evaluate_conditional(templar, host.vars) is False
    # Test False conditional
    conditional = 'hostvars[inventory_hostname] == foo'

# Generated at 2022-06-22 11:48:02.558610
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    if not C.DEFAULT_LOAD_CALLBACK_PLUGINS:
        raise ValueError("This test requires the callback plugins to be loaded")
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.loader import connection_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    variable_manager.set_inventory(inventory)

    # Can't use variable_manager.get_vars() directly as this method returns a new dict each time
    # see: https://github.com/ansible/ansible/blob/devel/lib

# Generated at 2022-06-22 11:48:13.466144
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class MyObj(Base, Conditional):
        def __init__(self, loader=None):
            self._ds = {}
            super(MyObj, self).__init__()


# Generated at 2022-06-22 11:48:21.063865
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # simple true/false tests
    assert Conditional()._check_conditional('foo', object(), dict(foo=True)) is True
    assert Conditional()._check_conditional('foo', object(), dict(foo=False)) is False
    assert Conditional()._check_conditional('foo', object(), dict(foo=0)) is False
    assert Conditional()._check_conditional('foo', object(), dict(foo=1)) is True
    assert Conditional()._check_conditional('foo', object(), dict(foo='0')) is True
    assert Conditional()._check_conditional('foo', object(), dict(foo='1')) is True
    assert Conditional()._check_conditional('foo', object(), dict(foo='')) is False
    assert Conditional()._check_conditional('foo', object(), dict(foo=' '))

# Generated at 2022-06-22 11:48:26.534774
# Unit test for constructor of class Conditional
def test_Conditional():
    class TestConditional(Conditional):
        def __init__(self):
            super(Conditional, self).__init__()

    # If we get here without error, success!
    return True

# Generated at 2022-06-22 11:48:35.513669
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.playbook.task import Task
    import pytest

    OPTIONS = {}

    @pytest.fixture
    def task_setup(request):
        loader = DataLoader()
        inv = InventoryManager(loader=loader, sources=None)
        var_manager = VariableManager(loader=loader, inventory=inv)
        task = Task()
        task.set_loader(loader=loader)
        task.set_inventory(inventory=inv)
        task.set_variable_manager(var_manager=var_manager)

# Generated at 2022-06-22 11:48:47.952764
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.base import Base

    class TestConditional(Base, Conditional):
        pass

    class FakeVarsModule:
        def __init__(self, a=None, b=None, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None, k=None):
            self.test_a = a
            self.test_b = b
            self.test_c = c
            self.test_d = d
            self.test_e = e
            self.test_f = f
            self.test_g = g
            self.test_h = h
            self.test_i = i
            self.test_j = j
            self.test_k = k


# Generated at 2022-06-22 11:49:01.016390
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """ Unit test for method evaluate_conditional of class Conditional """
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # initialize test variables
    variable_manager = VariableManager()
    variable_manager._extra_vars = {}
    variable_manager.set_nonpersistent_facts(dict())

    # initialize test conditionals

# Generated at 2022-06-22 11:49:12.747524
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestConditional(Conditional):
        def __init__(self, when, result, vars):
            self._ds = "test_cond"
            self._when = when
            self._expected_result = result
            self._vars = vars

        def run(self, tmp=None, task_vars=dict()):
            return self.evaluate_conditional(self.get_loader(), self._vars)

    c = TestConditional(['inventory_hostname in groups["foo"]'], True,
                        dict(inventory_hostname="foo.example.com", groups=dict(foo=["foo.example.com"])))
    t = c.get_loader()
    res = c.run()
    assert res == c._expected_result

# Generated at 2022-06-22 11:49:23.561806
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class test_Conditional(Conditional):
        '''
        This is a test class for testing the Conditional class.
        '''
        _when = FieldAttribute(isa='list', default=list)

    class FakeVarsModule:

        _ds = None

        def __init__(self, ds):
            self._ds = ds

    def get_vars(self, play=None, host=None, task=None, include_variables=True):
        return dict()

    test_Condition = test_Conditional()

    # Set up conditions for testing
    test_Condition.when = dict()