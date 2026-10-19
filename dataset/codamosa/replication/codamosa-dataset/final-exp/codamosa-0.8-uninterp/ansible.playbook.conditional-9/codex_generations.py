

# Generated at 2022-06-22 11:40:28.580247
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import os
    import tempfile

    local_tmp = tempfile.mkdtemp()
    local_vars = dict(
        host_one=dict(foo='1', bar='2', special_chars='@*&'),
        host_two=dict(foo='3', bar='4', special_chars='@*&'),
    )

# Generated at 2022-06-22 11:40:39.131490
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:40:48.477395
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import sys
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.strategy.linear import StrategyModule

    class Base(object):
        """ fake Base class for module class """
        def __init__(self):
            self._options = None
            self._connection = None
            self._play_context = PlayContext()
            self._loader = None
            self._variable_manager = None
            self.aliases = []

        @property
        def options(self):
            return self._options

        @options.setter
        def options(self, option):
            self._options = option


# Generated at 2022-06-22 11:41:01.082751
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    cond = Conditional()
    templar = DummyTemplar()
    all_vars = {}

    # Test no condition
    assert cond.evaluate_conditional(templar, all_vars) == True

    # Test with True condition
    cond = Conditional()
    cond.when.append(True)
    assert cond.evaluate_conditional(templar, all_vars) == True

    # Test with False condition
    cond = Conditional()
    cond.when.append(False)
    assert cond.evaluate_conditional(templar, all_vars) == False

    # Test with empty string condition
    cond = Conditional()
    cond.when.append("")
    assert cond.evaluate_conditional(templar, all_vars) == True

    # Test with real condition

# Generated at 2022-06-22 11:41:14.841438
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Update these variables before running the test
    all_vars = {}

# Generated at 2022-06-22 11:41:25.085184
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined("foo is defined") == [("foo", "is", "defined")]
    assert Conditional().extract_defined_undefined("foo is not defined") == [("foo", "is not", "defined")]
    assert Conditional().extract_defined_undefined("foo is undefined") == [("foo", "is", "undefined")]
    assert Conditional().extract_defined_undefined("foo is not undefined") == [("foo", "is not", "undefined")]
    assert Conditional().extract_defined_undefined("foo is defined and bar is defined") == [("foo", "is", "defined"), ("bar", "is", "defined")]

# Generated at 2022-06-22 11:41:27.731386
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()
    assert conditional._when == [], "incorrect default value for _when"


# Generated at 2022-06-22 11:41:38.613916
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import ansible.callbacks
    import ansible.inventory
    import ansible.playbook
    from ansible.template import Templar
    import tempfile

    #############################################################
    # Initialization
    #############################################################
    # Init ansible options
    ansible.constants.HOST_KEY_CHECKING = False

    # Init ansible callback
    callback = ansible.callbacks.AggregateStats()
    callback = ansible.callbacks.DefaultRunnerCallbacks()

    # Init ansible inventory
    group = ansible.inventory.Group('unittest')
    host = ansible.inventory.Host('localhost')
    group.add_host(host)
    inventory = ansible.inventory.Inventory(host_list=[])
    inventory.add_group(group)

    # Init ansible variable manager
    variable_

# Generated at 2022-06-22 11:41:50.681969
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    import ansible.constants as C

    display.verbosity = 3

    fake_loader = DictDataLoader({
        "some_var": '{ "omg": "lol" }',
        "some_omg": '{ "a": "b" }',
        "other_file": '{ "c": "d" }'
    })

    templar = Templar(loader=fake_loader, vault_secrets=[])
    templar._available_variables = dict()

    pc = PlayContext()

    cond = Conditional(loader=fake_loader)

    # set the play_context
    cond._play_context = pc

# Generated at 2022-06-22 11:42:02.662551
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert [('foo', 'is', 'defined')] == conditional.extract_defined_undefined('foo is defined')
    assert [('foo', 'is', 'not'), ('bar', 'is', 'defined')] == conditional.extract_defined_undefined('foo is not defined and bar is defined')
    assert [('hostvars["foo"]["bar"]["baz"]', 'is', 'not'), ('bar', 'is', 'defined')] == conditional.extract_defined_undefined('hostvars["foo"]["bar"]["baz"] is not defined and bar is defined')
    assert [('foo', 'not is', 'defined')] == conditional.extract_defined_undefined('foo not is defined')

# Generated at 2022-06-22 11:42:20.019550
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    t = Templar(loader=None, variables=VariableManager())

    c = Conditional()
    c._loader = None

    # A simple conditional should return the expected result
    assert(c.evaluate_conditional(t, dict(a=1)) == True)
    assert(c.evaluate_conditional(t, dict(a=0)) == False)

    # A conditional with an undefined variable should raise an exception
    try:
        c.evaluate_conditional(t, dict(a=0))
    except AnsibleUndefinedVariable:
        pass
    else:
        assert(False) # The exception should have been raised

    # A conditional with an undefined variable should return True if the missing variable is checked to not exist

# Generated at 2022-06-22 11:42:31.623989
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    test_value = [('hostvars["discovered_interpreter_python"]', 'is', 'defined'),
                  ('hostvars[inventory_hostname_short]', 'is', 'defined'),
                  ('ansible_python_interpreter', 'is', 'defined'),
                  ('ansible_python_interpreter', 'not', 'defined'),
                  ('foo', 'is', 'defined'),
                  ('bar', 'is', 'defined')]
    test = Conditional()
    assert test_value == test.extract_defined_undefined(
        'hostvars["discovered_interpreter_python"] is defined and hostvars[inventory_hostname_short] is defined and (ansible_python_interpreter is defined or ansible_python_interpreter is not defined) and foo is defined and bar is defined')

# Generated at 2022-06-22 11:42:32.466676
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    assert False

# Generated at 2022-06-22 11:42:43.202556
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # example strings that should pass
    yes = [
        "A is defined and B is defined",
        "A is not defined or B is defined",
        "A is undefined or (B is defined and C is not defined)",
        "A is defined or B is undefined and C is not defined or D is not defined",
    ]
    for a in yes:
        if len(Conditional.extract_defined_undefined(None, a)) == 0:
            print("FAIL: %s should have matched" % a)
        else:
            print("OK: %s matched" % a)

    # example strings that should not pass

# Generated at 2022-06-22 11:42:54.536496
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    result = conditional.extract_defined_undefined(u'foobar is defined')
    assert result == [(u'foobar', u'is', u'defined')]

    result = conditional.extract_defined_undefined(u'foobar is not defined')
    assert result == [(u'foobar', u'is not', u'defined')]

    result = conditional.extract_defined_undefined(u'foobar is undefined')
    assert result == [(u'foobar', u'is', u'undefined')]

    result = conditional.extract_defined_undefined(u'foobar is not undefined')
    assert result == [(u'foobar', u'is not', u'undefined')]


# Generated at 2022-06-22 11:43:04.212660
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:43:16.153402
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    assert ConditionalTest.evaluate_conditional(None, {"a" : "foo", "b" : 2, "c" : 3})
    assert ConditionalTest.evaluate_conditional(None, {"b" : 2, "c" : 3})
    assert not ConditionalTest.evaluate_conditional(None, {"b" : 2})
    assert ConditionalTest.evaluate_conditional(None, {"b" : 2, "d" : ["a","b"]})
    assert not ConditionalTest.evaluate_conditional(None, {"b" : 2, "d" : []})
    assert ConditionalTest.evaluate_conditional(None, {"b" : 2, "d" : "ab"})
    assert not ConditionalTest.evaluate_conditional(None, {"b" : 2, "d" : ""})
    assert ConditionalTest.evaluate

# Generated at 2022-06-22 11:43:26.469153
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert conditional.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert conditional.extract_defined_undefined('foo is defined and bar is not defined') == [
        ('foo', 'is', 'defined'),
        ('bar', 'is not', 'defined')
    ]
    assert conditional.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]
    assert conditional.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]

# Generated at 2022-06-22 11:43:38.378180
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Foo(Conditional):
        def __init__(self, conditionals):
            self._when = conditionals

    class VarManager(object):

        def __init__(self, keys, var_manager=None):
            self._keys = keys
            self._vars = keys
            self._var_manager = var_manager

        def get_vars(self, play=None, host=None, task=None, include_hostvars=True, include_delegate_to=True, use_cache=True):
            if self._var_manager:
                return self._var_manager.get_vars(play=play, host=host, task=task, include_hostvars=include_hostvars,
                                                  include_delegate_to=include_delegate_to, use_cache=use_cache)
            return

# Generated at 2022-06-22 11:43:44.094479
# Unit test for constructor of class Conditional
def test_Conditional():
    class TestConditional(Conditional):
        def __init__(self):
            super(TestConditional, self).__init__()
            self._ds = None
            self._when = [None, True, False, "a == b", "a == 'b'", "a.split() and b|int > c",
                          "a.split() and b|int > c or d and e",
                          "a.split() and b|int > c or d and e or f or g and h or i", 'i']

    testConditional = TestConditional()
    assert testConditional is not None


# Generated at 2022-06-22 11:44:04.069164
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    try:
        from ansible.compat.tests import unittest
    except ImportError:
        import unittest

    class TestConditional(Conditional):
        pass

    # Simple test for positive cases

# Generated at 2022-06-22 11:44:15.841137
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.host import Host

    p = PlayContext()
    t = Templar(loader=None, variables={})
    h = Host(name="foobar")

    c = Conditional()

    assert c.evaluate_conditional(t, {'my_var': 'my_value', 'my_var2': 'my_value2'}) is True

    c._when = ['my_var is my_value']
    assert c.evaluate_conditional(t, {'my_var': 'my_value'}) is True

    c._when = ['my_var is not my_value']
    assert c.evaluate_conditional(t, {'my_var': 'my_value'}) is False


# Generated at 2022-06-22 11:44:27.909339
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestClass(object):
        _ds = 'fake_ds'
        _loader = 'fake_loader'

        def __init__(self, criterion, all_vars):
            self.when = criterion
            self.all_vars = all_vars

        def _check_conditional(self, conditional, templar, all_vars):
            self.cond = conditional
            self.templar = templar
            self.all_vars = all_vars

            return True

    all_vars = dict(a=1, b=2, c=3, d=4)


# Generated at 2022-06-22 11:44:40.219354
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional_obj = Conditional()
    assert conditional_obj.extract_defined_undefined("hostvars[inventory_hostname] is not defined") == [('hostvars[inventory_hostname]', 'is not', 'defined')]
    assert conditional_obj.extract_defined_undefined("a is not undefined") == [('a', 'is not', 'undefined')]
    assert conditional_obj.extract_defined_undefined("a is defined") == [('a', 'is', 'defined')]
    assert conditional_obj.extract_defined_undefined("a is undefined") == [('a', 'is', 'undefined')]
    assert conditional_obj.extract_defined_undefined("a is b") == []

# Generated at 2022-06-22 11:44:51.653640
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    my_object = Conditional()

    conditional = 'hostvars["host1"] is defined and hostvars["host2"] is not defined'
    my_object.when = [conditional]

    result = my_object.extract_defined_undefined(conditional)

    assert result == [('hostvars["host1"]', 'is', 'defined'), ('hostvars["host2"]', 'is not', 'defined')]

    conditional = 'hostvars["host1"] is defined and hostvars["host2"] is not defined or hostvars["host3"] is undefined'
    my_object.when = [conditional]

    result = my_object.extract_defined_undefined(conditional)


# Generated at 2022-06-22 11:45:03.199285
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    ############################################################################
    # Tests for if
    ############################################################################

    # Test empty conditional
    cond = Conditional()
    cond.when = [""]
    templar = Templar(loader=None, variables={})
    result = cond.evaluate_conditional(templar, dict())
    assert result == True, result

    # Test single condition
    cond = Conditional()
    cond.when = [ "ansible_os_family == 'Debian'" ]
    templar = Templar(loader=None, variables=dict(ansible_os_family='Debian'))
    result = cond.evaluate_conditional(templar, dict())
    assert result == True, result

    # Test single failing condition
    cond

# Generated at 2022-06-22 11:45:15.169926
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:45:21.909493
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # We create a dummy object
    class obj: pass
    o = obj()
    o._loader = None
    o._ds = None
    o._templar = None

    # Now it has the method evaluate_conditional
    for attr in Conditional.__dict__:
        if not callable(attr):
            setattr(o, attr, Conditional.__dict__[attr])
    for attr in Conditional.__dict__['__init__'].__func__.__code__.co_varnames:
        if attr != 'self':
            setattr(o, attr, None)

    # We initialize the instance
    o.__init__()

    # We create a dummy templar
    class templar:
        def template(self, data, disable_lookups=False):
            return

# Generated at 2022-06-22 11:45:22.995769
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    #TODO: not yet implemented
    return 0

# Generated at 2022-06-22 11:45:34.168200
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional1 = "var is defined and hostvars['foo'] is defined or hostvars[inventory_hostname] is undefined or (myvar == 'foo' or myvar is not defined) and myvar2 is undefined"
    conditional2 = "not (var is defined and hostvars['foo'] is defined or hostvars[inventory_hostname] is undefined or (myvar == 'foo' or myvar is not defined) and myvar2 is undefined)"
    conditional3 = "myvar is defined and hostvars['foo'] is not defined or hostvars[inventory_hostname] is undefined or (myvar == 'foo' or myvar2 is not defined)"

    obj = Conditional()
    assert len(obj.extract_defined_undefined(conditional1)) == 10

# Generated at 2022-06-22 11:46:01.210725
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    class DummyConditional(Conditional):
        def __init__(self):
            pass

    dummyConditional = DummyConditional()

    # Test 1. Conditional string that pure Python can evaluate.
    conditional = 'foo is defined'
    assert dummyConditional.extract_defined_undefined(conditional) == [('foo', 'is', 'defined')]

    # Test 2. Conditional string that contains jinja2 expressions
    conditional = u"""{{ foo is defined and
                            {{ 'foo' in [1, 2, 3] }} is defined
                            and {{ bar }} is defined
                        }}"""
    assert dummyConditional.extract_defined_undefined(conditional) == [
        ('foo', 'is', 'defined'),
        ('bar', 'is', 'defined'),
    ]

    # Test 3. Conditional string

# Generated at 2022-06-22 11:46:13.597128
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # create a fake loader
    class DummyLoader(object):
        def __init__(self):
            pass

        def get_basedir(self):
            return '/home/ansible'

    class DummyValidator(object):
        def __init__(self):
            pass

        def __call__(self, value):
            return True

    # create a Conditional object with a fake loader
    cond = Conditional(loader=DummyLoader())

    # create a templar for use with the Conditional object
    class DummyVars(object):
        def get(self, value, default=None):
            return "OK"

    class DummyTemplar(object):
        def __init__(self):
            self.environment = DummyEnvironment()
            self.available_variables = DummyVars()


# Generated at 2022-06-22 11:46:23.869594
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
        class MyClass(Conditional):
            def __init__(self, loader=None, templar=None, all_vars=None):
                self.when = [None, '', True, 'a==b', 'a==1', 'a is defined', '(a == 1) or (b is defined)']
                self._loader = loader
                self._templar = templar
                self._all_vars = all_vars
                super(MyClass, self).__init__(loader)

        result = []
        obj = MyClass(templar=None, all_vars={'a': '1', 'b': '2'})

        result.append(obj.evaluate_conditional(templar=None, all_vars={'a': '1', 'b': '2'}))
        result.append

# Generated at 2022-06-22 11:46:37.008908
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    ''' test_Conditional_evaluate_conditional
    Test the normal evaluation of the conditional statement.
    '''

# Generated at 2022-06-22 11:46:48.889755
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('foo or bar is defined') == [('bar', 'is', 'defined')]
    assert c.extract_defined_undefined('foo and bar is defined') == [('bar', 'is', 'defined')]
    assert c.extract_defined_undefined('bar and foo is not defined') == [('foo', 'is not', 'defined')]
    assert c.extract_defined_undefined('foo and bar is defined') == [('bar', 'is', 'defined')]
    assert c.extract_defined_undefined('foo and bar is not defined') == [('bar', 'is not', 'defined')]

# Generated at 2022-06-22 11:46:59.257037
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display.verbosity = 3

# Generated at 2022-06-22 11:47:09.928378
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook.base import Base
    Base.__bases__ = (Conditional,)

    class FakeDS:
        def __init__(self):
            self.path = 'xyz'

    fake_ds = FakeDS()
    fake_ds.path = 'xyz'

    fake_loader = 'xyz'

    obj1 = Base(fake_loader)
    obj2 = Base(fake_loader, fake_ds)

    assert obj1._ds == None
    assert obj1._loader == fake_loader
    assert obj1.when == []

    assert obj2._ds == fake_ds
    assert obj2._loader == fake_loader
    assert obj2.when == []


# Generated at 2022-06-22 11:47:23.090260
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # test evaluate_condition with unsafe variables
    class MyTask(Conditional):
        pass
    t = MyTask()
    templar = None
    all_vars = dict(var1='foo')
    result = t.evaluate_conditional(templar, all_vars)
    assert result == True
    # test evaluate_condition with safe variables
    all_vars = {
        'test_var': 'foo',
        'test_var2': 'bar',
        'test_dict': {
            'key': 'val'
        },
        'test_dict2': {
            'key': 'val'
        }
    }

    # test a case that should fail
    conditional = "test_var == 'foo' and test_var2 == 'foo'"

# Generated at 2022-06-22 11:47:29.893267
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.conditional import Conditional
    assert Conditional().extract_defined_undefined('test_variable is defined') == [('test_variable', 'is', 'defined')]
    assert Conditional().extract_defined_undefined('''test_variable is defined and
        somevar is defined or
        anothervar is undefined''') == [('test_variable', 'is', 'defined'), ('somevar', 'is', 'defined'), ('anothervar', 'is', 'undefined')]


# Generated at 2022-06-22 11:47:42.101683
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    c = Conditional()

    conditional = 'var1 is defined and var2 is defined and var3 is defined and var4 is undefined and var5 is undefined'
    # On the re.search, when looking for hostvars[.+], for the following:
    #  - the square braquets must be escaped, so [ becomes \[
    #  - the .+ is not greedy, we need to replace it with .+? to make it
    #    'non-greedy' and avoid matches like var2 is defined and var3 is defined
    #    to match var2 is defined and var3 is defined and var4 is undefined
    conditional = conditional.replace('hostvars[.+]', 'hostvars[.+?]')

# Generated at 2022-06-22 11:48:04.221443
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = 'hostvars[inventory_hostname] is defined and (hostvars[inventory_hostname].first_name is defined or hostvars[inventory_hostname].last_name is defined) and not hostvars[inventory_hostname].ignore_me is defined'
    expected_result = [['hostvars[inventory_hostname]', 'is', 'defined'], ['hostvars[inventory_hostname].first_name', 'is', 'defined'], ['hostvars[inventory_hostname].last_name', 'is', 'defined'], ['hostvars[inventory_hostname].ignore_me', 'is', 'defined']]

    cond = Conditional()

    result = cond.extract_defined_undefined(conditional)

    assert result == expected_result


# Generated at 2022-06-22 11:48:14.883065
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    fake_loader = DataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources=[])
    play_context = PlayContext()
    variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    templar = Templar(loader=fake_loader, variables=variable_manager)

    conditional = Conditional()

    # boolean values
    all_vars = dict()

    conditional.when.append('"{{ hello }}" == "goodbye"')

# Generated at 2022-06-22 11:48:26.354344
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()

# Generated at 2022-06-22 11:48:30.094437
# Unit test for constructor of class Conditional
def test_Conditional():
    '''
    Make sure that constructor of Conditional is adding
    conditional value
    '''
    class TestTask(Conditional):
        pass

    assert hasattr(TestTask, 'when')



# Generated at 2022-06-22 11:48:41.202835
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

    result = conditional.extract_defined_undefined("a is defined or b is undefined and c is defined")
    assert result == [("a", "is", "defined"), ("b", "is", "undefined"), ("c", "is", "defined")]

    result = conditional.extract_defined_undefined("a is not defined or b is undefined")
    assert result == [("a", "is not", "defined"), ("b", "is", "undefined")]

    result = conditional.extract_defined_undefined("a is not defined or b is not defined")
    assert result == [("a", "is not", "defined"), ("b", "is not", "defined")]

    result = conditional.extract_defined_undefined("a is defined or b is defined")

# Generated at 2022-06-22 11:48:53.284288
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar
    from ansible.template.vars import AnsibleVariable
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({})
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list=[])
    templar = Templar(loader=loader, variables=inventory.get_vars())
    c = Conditional(loader=loader)

    # set the when conditions conditionally
    c.when = []
    assert c.evaluate_conditional(templar, inventory.get_vars())

    c.when = [True]
    assert c.evaluate_conditional(templar, inventory.get_vars())

    c.when = [False]

# Generated at 2022-06-22 11:49:06.035469
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # This test is testing a method which is meant to be overriden in Base
    # It is in here because it is needed by TaskInclude and Task
    # If another class is meant to be tested create a new file with the
    # appropriate name.
    class TestConditional(Conditional):
        # Simulate an object that has a _ds set by a Base child object
        def __init__(self, *args, **kwargs):
            super(TestConditional, self).__init__(*args, **kwargs)
            self._ds = 'fake_ds'

    test_class = TestConditional()

    # Needed for testing and not present because this class is a mixin
    test_class._loader = None
    test_class.when = ['is_linux', '2 > 3']

    # Create a templar to be used by

# Generated at 2022-06-22 11:49:18.353205
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestConditional(Conditional):
        # when used directly, this class needs a loader, but we want to
        # make sure we don't trample on the existing one if this class
        # is used as a mix-in with a playbook base class
        def __init__(self, loader=None):
            # when used directly, this class needs a loader, but we want to
            # make sure we don't trample on the existing one if this class
            # is used as a mix-in with a playbook base class
            if not hasattr(self, '_loader'):
                if loader is None:
                    raise AnsibleError("a loader must be specified when using Conditional() directly")
                else:
                    self._loader = loader
            super(Conditional, self).__init__()

    # variables structure

# Generated at 2022-06-22 11:49:19.266881
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # TODO

    pass


# Generated at 2022-06-22 11:49:31.344040
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # Load the actual module and get a class reference
    from ansible.playbook.task import Task
    C_ref = Conditional
    T_ref = Task

    # Define input and expected output for tests
    _vars = dict(
        a="foobar",
        b=42,
    )

    tests = [
        # (  condition, output )
        (  "True",         True ),
        (  "'foo' in a",   True ),
        (  "'bar' in a",   False),
        (  "b == 42",      True ),
        (  "False",        False),
    ]


# Generated at 2022-06-22 11:50:16.619045
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar, TemplarError
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    all_vars = dict(
        hostvars=dict(
            remote_host=(
                dict(
                    jinja2_safe=True,
                    jinja2_unsafe_str=AnsibleUnsafeText("unsafe"),
                )
            )
        ),
        jinja2_safe=True,
        jinja2_unsafe_str=AnsibleUnsafeText("unsafe"),
    )

    conditional = Conditional()
    templar = Templar(loader=None, shared_loader_obj=None)

    assert conditional._check_conditional("jinja2_safe", templar, all_vars) is True