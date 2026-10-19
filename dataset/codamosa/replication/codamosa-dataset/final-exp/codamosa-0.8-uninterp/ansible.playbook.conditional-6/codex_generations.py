

# Generated at 2022-06-22 11:40:29.744888
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import jinja2

    class TestClass(Conditional):
        pass

    assert TestClass().evaluate_conditional(jinja2.StrictUndefined(), dict()) == True

    assert TestClass(when="False").evaluate_conditional(jinja2.StrictUndefined(), dict()) == False

    assert TestClass(when=["False", "True"]).evaluate_conditional(jinja2.StrictUndefined(), dict()) == False

    assert TestClass(when=["False", "False"]).evaluate_conditional(jinja2.StrictUndefined(), dict()) == False

    assert TestClass(when=["True", "True"]).evaluate_conditional(jinja2.StrictUndefined(), dict()) == True


# Generated at 2022-06-22 11:40:37.511101
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext

    # SETUP
    conditional_test = Conditional()
    conditional_test._ds = {}
    conditional_test._loader = None
    conditional_test._attributes = []
    conditional_test.when = ["'1' == '1'"]
    play_context = PlayContext()
    templar = None
    all_vars = {}

    # TEST
    result = conditional_test.evaluate_conditional(templar, all_vars)

    # ASSERT
    assert result == True


# Generated at 2022-06-22 11:40:46.726258
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    assert cond.extract_defined_undefined({"when": "foo is defined"}) == [("foo", "is", "defined")]
    assert cond.extract_defined_undefined({"when": "foo is not defined"}) == [("foo", "is not", "defined")]
    assert cond.extract_defined_undefined({"when": "foo is undefined"}) == [("foo", "is", "undefined")]
    assert cond.extract_defined_undefined({"when": "foo is not undefined"}) == [("foo", "is not", "undefined")]
    assert cond.extract_defined_undefined({"when": "hostvars['foo'] is defined"}) == [("hostvars['foo']", "is", "defined")]
    assert cond.extract

# Generated at 2022-06-22 11:41:00.045241
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    play = Play()
    task = Task()
    play.set_loader(task._loader)


# Generated at 2022-06-22 11:41:13.648298
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Import needed for the unit test
    from ansible.parsing import DataLoader

    def _evaluate_conditional(conditional):
        from ansible.template import Templar
        from ansible.vars import VariableManager
        from ansible.playbook.play_context import PlayContext
        from ansible.playbook.task import Task

        test_data = dict(p=dict(a=3, b=4))
        variable_manager = VariableManager()
        variable_manager.set_inventory(DataLoader().load(test_data))
        variable_manager.add_extra_vars({'test_var': 'foo'})

        loader = DataLoader()
        variable_manager.set_loader(loader)

        play_context = PlayContext()
        variable_manager.set_play_context(play_context)

        task = Task()

# Generated at 2022-06-22 11:41:25.922125
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Foo:
        _when = [ 'foo' ]

    # Invalid when type
    obj = Foo()
    obj.when = 12
    try:
        obj.evaluate_conditional(None, None)
        assert False
    except:
        assert True

    # Invalid when value
    obj.when = [12]
    try:
        obj.evaluate_conditional(None, None)
        assert False
    except:
        assert True

    # invalid templar
    obj.when = ['{{foo}}']
    try:
        obj.evaluate_conditional(12, None)
        assert False
    except:
        assert True

    # invalid all_vars
    obj.when = ['{{foo}}']

# Generated at 2022-06-22 11:41:37.875447
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.plugins import filter_loader
    from ansible.parsing.yaml.objects import AnsibleUnicode
    # FIXME: make separate unit test for _check_conditional
    assert Conditional()._check_conditional(True, Templar(None), {})
    assert Conditional()._check_conditional(False, Templar(None), {})
    assert Conditional()._check_conditional('True', Templar(None), {})
    assert Conditional()._check_conditional('False', Templar(None), {})
    assert Conditional()._check_conditional('true', Templar(None), {})
    assert Conditional()._check_conditional('false', Templar(None), {})
    assert Conditional()._check_conditional('TRUE', Templar(None), {})

# Generated at 2022-06-22 11:41:50.638937
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    # Test 1
    if True:
        t = Templar(loader=loader, variables={'foo': 'bar'})
        c = Conditional(loader=loader)
        assert c.evaluate_conditional(t, []) is True
        assert c.evaluate_conditional(t, []) is True

    # Test 2 - conditional evaluates to True
    if True:
        t = Templar(loader=loader, variables={'foo': 'bar'})
        c = Conditional(loader=loader)

# Generated at 2022-06-22 11:42:02.614403
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class TestClass(object):
        def __init__(self, variables=None, loader=None):
            self.hostvars = {'host1': {'var1': 'foo', 'var2': 'foobar'},
                             'host2': {'var3': 'bar'}}
            self.vars = variables or {}
            self.when = ['var1 == "foo"']
            self.tasks = []
            self._loader = loader

        def __repr__(self):
            return "c"

    # Create a fake loader
    class TestLoader(object):
        pass

    loader = TestLoader()

    # Create a fake templar class
    class TestTemplar(object):
        def __init__(self, loader=None, variables=None):
            self.variables = variables or {}

       

# Generated at 2022-06-22 11:42:11.736496
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    print("c.extract_defined_undefined({'foo is undefined and bar is defined'}) = %s" % c.extract_defined_undefined("foo is undefined and bar is defined"))
    print("c.extract_defined_undefined({'foo is undefined'}) = %s" % c.extract_defined_undefined("foo is undefined"))
    print("c.extract_defined_undefined({'foo is not defined'}) = %s" % c.extract_defined_undefined("foo is not defined"))
    print("c.extract_defined_undefined({'foo not is defined'}) = %s" % c.extract_defined_undefined("foo not is defined"))

# Generated at 2022-06-22 11:42:31.344706
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import ansible.inventory.manager
    import jinja2

    loader = DataLoader()
    host_list = ansible.inventory.manager.get_inventory_manager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=host_list)

    task = Task()

    # no when - always true
    task.when = None
    ret = task.evaluate_conditional(task, variable_manager.get_vars())
    assert ret is True

    # empty when - always true
    task.when = []
    ret = task.evaluate_conditional(task, variable_manager.get_vars())
    assert ret

# Generated at 2022-06-22 11:42:37.168045
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar

    task = Task()
    task.when = (
        'foo is defined',
        'bar is not defined',
        'baz is undefined',
    )

    result = task.extract_defined_undefined('foo is defined and bar is not defined and baz is undefined')

    assert result == [('foo', 'is', 'defined'), ('bar', 'is not', 'defined'), ('baz', 'is', 'undefined')]



# Generated at 2022-06-22 11:42:49.920844
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # Setup
    all_vars = dict()
    templar = Templar(loader=None, variables=all_vars)
    base = Conditional(loader=None)

    # Tests
    assert base.evaluate_conditional(templar, all_vars)
    base.when = ['']
    assert base.evaluate_conditional(templar, all_vars)
    base.when = ['True']
    assert base.evaluate_conditional(templar, all_vars)
    base.when = ['False']
    assert not base.evaluate_conditional(templar, all_vars)
    base.when = [True]

# Generated at 2022-06-22 11:43:02.525025
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # None conditional
    conditional = None
    result = Conditional().extract_defined_undefined(conditional)
    assert result == []
    # Empty conditional
    conditional = ""
    result = Conditional().extract_defined_undefined(conditional)
    assert result == []
    # No defined/undefined variable
    conditional = "var1 == 1 and var2 == 2"
    result = Conditional().extract_defined_undefined(conditional)
    assert result == []
    # Single 'defined' variable
    conditional = "var1 is defined"
    result = Conditional().extract_defined_undefined(conditional)
    assert result == [('var1', 'is', 'defined')]
    # Single 'undefined' variable
    conditional = "var1 is undefined"
    result = Conditional().extract_defined_

# Generated at 2022-06-22 11:43:13.991951
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined("") == []
    assert Conditional().extract_defined_undefined("foo is defined") == [('foo', 'is', 'defined')]
    assert Conditional().extract_defined_undefined("'foo' is defined") == [('foo', 'is', 'defined')]
    assert Conditional().extract_defined_undefined('"foo" is defined') == [('foo', 'is', 'defined')]
    assert Conditional().extract_defined_undefined("foo not is defined") == [('foo', 'not is', 'defined')]
    assert Conditional().extract_defined_undefined("foo is not defined") == [('foo', 'is', 'not defined')]

# Generated at 2022-06-22 11:43:25.179512
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    test_conditional = Conditional(loader=loader)

    # These test cases are based on the list at: http://docs.ansible.com/playbooks_conditionals.html#playbook-conditionals

    # Boolean
    test_conditional._ds = 'boolean'
    test_conditional.when = [True]
    res = test_conditional.evaluate_conditional(Templar(loader=loader), variable_manager.get_vars(loader=loader))
    assert res is True

    test_conditional._ds = 'boolean'
    test_conditional.when = [False]
    res

# Generated at 2022-06-22 11:43:37.158304
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test for a when that is True
    t = Conditional()
    t._ds = {}
    t._when = ['True']
    f = t.evaluate_conditional
    assert f('templar', dict(one = '1')) == True

    # Test for a when that is False
    t = Conditional()
    t._ds = {}
    t._when = ['False']
    f = t.evaluate_conditional
    assert f('templar', dict(one = '1')) == False

    # Test for a when that is empty
    t = Conditional()
    t._ds = {}
    t._when = []
    f = t.evaluate_conditional
    assert f('templar', dict(one = '1')) == True

    # Test for a when that is "None"

# Generated at 2022-06-22 11:43:49.133751
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
   # First: Test evaluation with a static (not templated) dictionary
   staticDict = {
      'ok' : True,
      'ok_str' : 'True',
      'nok' : False,
      'nok_str' : 'False',
      'a' : 'a',
      'b' : 'b',
      'c' : 'c'
   }

   # First, test with static conditional that should evaluate to True
   staticConditional = "ok"
   staticResult = True
   staticEvalSucceeded = True

   conditional = Conditional()
   actualResult = conditional.evaluate_conditional(staticConditional, staticDict)

# Generated at 2022-06-22 11:43:58.861669
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    instance = Conditional()

    host_vars = {"foo": "bar"}
    extra_vars = {"foo": "baz"}
    variables = {"ansible_play_hosts": [], "play_hosts": []}

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["/dev/null"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # set variable "foo"
    variable_manager._extra_vars = extra_vars
    variable_manager._host_vars = host_vars
    variable_manager.set_nonpersistent_facts(variables)

   

# Generated at 2022-06-22 11:44:06.549793
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar

    vars = dict(
        foo=dict(bar=dict(baz=1)),
        quux=dict(baz=3),
        something_else=4,
        baz=8,
    )

    assert Conditional(None).evaluate_conditional(Templar(loader=None, variables=vars), vars)

    conditional = 'foo.bar.baz == 1'
    assert Conditional(None).evaluate_conditional(Templar(loader=None, variables=vars), vars)

    conditional = 'foo.bar.baz is not quux.baz'
    assert Conditional(None).evaluate_conditional(Templar(loader=None, variables=vars), vars)

    conditional = 'something_else is not defined'

# Generated at 2022-06-22 11:44:33.799597
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    a = Conditional()
    assert a.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert a.extract_defined_undefined('foo not is defined') == [('foo', 'not is', 'defined')]
    assert a.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]
    assert a.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert a.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]
    assert a.extract_defined_undefined('foo  is  not  undefined') == [('foo', 'is not', 'undefined')]

# Generated at 2022-06-22 11:44:46.058609
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # pylint: disable=too-few-public-methods
    class TestConditional(object):
        # pylint: disable=no-self-use
        def extract_defined_undefined(self, conditional):
            return Conditional.extract_defined_undefined(self, conditional)

    c = TestConditional()


# Generated at 2022-06-22 11:44:58.138319
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook.base import Base
    from ansible.template import Templar
    import jinja2

    class Test(Conditional, Base):
        pass

    t = Test()

    mock_loader = jinja2.DictLoader({})
    mock_vars = jinja2.Environment(loader=mock_loader)
    mock_templar = Templar(loader=mock_loader, variables=mock_vars)

    the_vars = dict(
        core_var=dict(
            hostvars=dict(
                localhost=dict(
                    core_var_localhost=True
                )
            )
        )
    )

    # test when hostvars is used as a variable
    mock_vars.loader.mapping = the_vars
    assert t.evaluate_conditional

# Generated at 2022-06-22 11:45:08.426502
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()


# Generated at 2022-06-22 11:45:19.867145
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined("my_var is defi") == []
    assert isinstance(c.extract_defined_undefined("my_var is defined"), list)
    assert isinstance(c.extract_defined_undefined("my_var is defined")[0], tuple)
    assert c.extract_defined_undefined("my_var is defined") == [("my_var", "is", "defined")]
    assert isinstance(c.extract_defined_undefined("my_var is defined")[0][0], str)
    assert isinstance(c.extract_defined_undefined("my_var is defined")[0][1], str)
    assert isinstance(c.extract_defined_undefined("my_var is defined")[0][2], str)

# Generated at 2022-06-22 11:45:32.163500
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:45:44.584945
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')

    templar = Templar(loader=loader, inventory=inventory, variable_manager=variable_manager)

    conditional = Conditional()

    # Test cases where the conditional is a string

    # Test case where the conditional is empty string
    conditional._when = [""]
    assert conditional.evaluate_conditional(templar, variable_manager.get_vars(loader=loader, play=None, host=None)) == True

    # Test case where the conditional is a string
    conditional._when = ["foo"]

# Generated at 2022-06-22 11:45:54.381018
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Define plugin to get a loader
    class Plugin:
        def __init__(self, *args, **kwargs):
            self.name = kwargs.get('name')
            self.path = kwargs.get('path')
            self.config = dict(foo=42, bar='42')
    plugin = Plugin(name='foo', path='/')

    # Define environment to get a templar
    class Environment:
        class Engine:
            def __init__(self, *args, **kwargs):
                self.environment = dict(foo=42, bar='42')

        def __init__(self, *args, **kwargs):
            self.engine = self.Engine()

    class Templar:
        def __init__(self, *args, **kwargs):
            self.environment = Environment()

   

# Generated at 2022-06-22 11:45:55.168513
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()

# Generated at 2022-06-22 11:46:07.903949
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.parsing.dataloader import DataLoader

    c = Conditional(loader=DataLoader())

    assert c.extract_defined_undefined('a') == []
    assert c.extract_defined_undefined('a is undefined') == [('a', 'is', 'undefined')]
    assert c.extract_defined_undefined('a is defined') == [('a', 'is', 'defined')]
    assert c.extract_defined_undefined('a is not undefined') == [('a', 'is not', 'undefined')]
    assert c.extract_defined_undefined('a is not defined') == [('a', 'is not', 'defined')]


# Generated at 2022-06-22 11:46:50.601298
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert c.extract_defined_undefined('foo is defined and bar is defined') == [('foo', 'is', 'defined'), ('bar', 'is', 'defined')]
    assert c.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert c.extract_defined_undefined('foo is not defined or bar is defined') == [('foo', 'is not', 'defined'), ('bar', 'is', 'defined')]
    assert c.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]

# Generated at 2022-06-22 11:46:57.629688
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:47:09.475870
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # This test exercises the evaluate_conditional function.
    #
    # We have the following cases:
    #
    # 1. Test for placeholder in condition         | Test for
    # 2. Test for valid condition                  | Test for
    # 3. Test for invalid condition                | Test for
    # 4. Test for valid undefined / defined        | Test for

    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    # Mock the unfrackpath_noop function so that the function
    # doesn't throw an error when it encounters a non-

# Generated at 2022-06-22 11:47:13.935291
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined(conditional="foo is undefined and bar is defined") == \
        [('foo', 'is', 'undefined'), ('bar', 'is', 'defined')]



# Generated at 2022-06-22 11:47:26.275704
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    class X(Conditional):
        pass
    x = X(loader=loader)
    templar = loader.load_basedir(basedir='.')

    # test the AND of conditions
    x.when = ['1 < 2 and 2 < 3', '3 < 4']
    assert x.evaluate_conditional(templar, variable_manager.get_vars()) is True

    # test the OR of conditions
    x.when = ['1 > 2 or 2 < 3', '3 > 4']
    assert x.evaluate_conditional(templar, variable_manager.get_vars()) is True

    # test the NOT of conditions
    x

# Generated at 2022-06-22 11:47:36.910785
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # inventory to test with
    i = InventoryManager(loader=DataLoader(), sources=[])
    h = i.add_host('example_host')
    h.set_variable('some_var', 'some_value')
    h.set_variable('var_1', 'var_1_value')
    h.set_variable('var_2', 'var_2_value')
    h.set_variable('dict_in_var', {'foo': 'bar'})
    h.set_variable('dict_in_var.foo', 'baz')

    # variable manager to test with
    v = VariableManager(loader=DataLoader(), inventory=i)



# Generated at 2022-06-22 11:47:41.929270
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    conditional = Conditional()

    # Test empty condition
    result = conditional.evaluate_conditional(None, None)
    assert result is True

    # Test None condition
    result = conditional.evaluate_conditional(None, None, None)
    assert result is True

    # Test True condition
    result = conditional.evaluate_conditional(None, None, True)
    assert result is True

    # Test False condition
    result = conditional.evaluate_conditional(None, None, False)
    assert result is False

    # Test False condition
    result = conditional.evaluate_conditional(None, None, "False")
    assert result is False

    # Test True condition
    result = conditional.evaluate_conditional(None, None, "True")
    assert result is True

    # Test regex match

# Generated at 2022-06-22 11:47:54.319735
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:48:02.651826
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    import ansible.constants as C

    # As we are testing a mix-in, we need to create a test class.
    class ConditionalChecker(Conditional):

        def __init__(self):
            super(ConditionalChecker, self).__init__()
            self._ds = dict()

    class Host():
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    # SETUP our enviroment
    play_context = PlayContext()
    loader = None

# Generated at 2022-06-22 11:48:13.572601
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:49:28.919993
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # basic tests
    assert Conditional.extract_defined_undefined("") == []
    assert Conditional.extract_defined_undefined("a is defined") == [("a", "is", "defined")]
    assert Conditional.extract_defined_undefined("a is defined and b is not defined") == [("a", "is", "defined"), ("b", "is not", "defined")]
    assert Conditional.extract_defined_undefined("a is defined and b is not undefined") == [("a", "is", "defined"), ("b", "is not", "undefined")]
    assert Conditional.extract_defined_undefined("a is defined and b is undefined") == [("a", "is", "defined"), ("b", "is", "undefined")]
    # tests with 'hostvars[x]'


# Generated at 2022-06-22 11:49:42.069940
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional.extract_defined_undefined('a is defined and b is undefined') == [('a', 'is', 'defined'), ('b', 'is', 'undefined')]
    assert Conditional.extract_defined_undefined('not a is defined') == [('a', 'is', 'defined')]
    assert Conditional.extract_defined_undefined('not a is undefined') == [('a', 'is', 'undefined')]
    assert Conditional.extract_defined_undefined('a is not defined') == [('a', 'is not', 'defined')]
    assert Conditional.extract_defined_undefined('a is not undefined') == [('a', 'is not', 'undefined')]

# Generated at 2022-06-22 11:49:49.613882
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = "'foobar' in group_names"
    list = Conditional().extract_defined_undefined(conditional)
    assert len(list) == 1
    assert list[0][0] == 'group_names'
    assert list[0][1] == 'in'
    assert list[0][2] == 'defined'

    conditional = "'foobar' not in group_names"
    list = Conditional().extract_defined_undefined(conditional)
    assert len(list) == 1
    assert list[0][0] == 'group_names'
    assert list[0][1] == 'not in'
    assert list[0][2] == 'defined'

    conditional = "'foobar' is defined"
    list = Conditional().extract_defined_undefined(conditional)
    assert len(list)

# Generated at 2022-06-22 11:50:01.290127
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.role.definition import RoleDefinition

    rd = RoleDefinition()
    rd._ds = {}  # pylint: disable=protected-access
    assert rd.evaluate_conditional(None, {})

    rd._role_path = 'test'
    rd._ds = {'some_var': 'some_value'}
    rd.when = ['some_var is defined']
    assert rd.evaluate_conditional(None, {})

    rd.when = ['some_var is not defined']
    assert not rd.evaluate_conditional(None, {})

    rd.when = ['some_other_var is not defined']
    assert rd.evaluate_conditional(None, {})

    rd.when = ['some_var == some_value']
    assert r

# Generated at 2022-06-22 11:50:08.694708
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_fact("hello", "world")
    variable_manager.set_fact("dict_var", {"a": 1})
    variable_manager.set_fact("myvar", "foo")

    # Basic execution of templating as well as validation of unquoted boolean.
    cond = Conditional(loader=loader)
    assert cond.evaluate_conditional({}, variable_manager) is True
    cond.when = '{{ hello }} == "world"'
    assert cond.evaluate_conditional({}, variable_manager) is True
    cond.when = "dict_var['a'] == 1"