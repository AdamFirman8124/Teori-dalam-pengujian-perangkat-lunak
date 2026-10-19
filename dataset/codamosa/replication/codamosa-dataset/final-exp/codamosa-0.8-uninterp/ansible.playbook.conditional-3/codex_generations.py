

# Generated at 2022-06-22 11:40:28.696904
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    # Test extract_defined_undefined of class Conditional
    #
    # This method extracts all the defined/undefined variables
    # from a given conditional statement and return a list in the
    # form [(var_name, logis, state)]
    #
    # Returns:
    #   list: list of extracted variables in the form [(var_name, logis, state)]

    from ansible.playbook.conditional import Conditional

    # conditional statement with a space after the word 'is'
    conditional = "hostvars[inventory_hostname] is not defined and hostvars[inventory_hostname].some_var is   defined"

    # expected result

# Generated at 2022-06-22 11:40:30.074250
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()
    assert conditional.evaluate_conditional(None, None) is True

# Generated at 2022-06-22 11:40:40.579208
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class TestConditional(Conditional):
        _when = FieldAttribute(isa='list', default=list)

    when_list = TestConditional()
    when_list._when.append('foo and bar')
    when_list._when.append(True)
    when_list._when.append(False)
    when_list._when.append('baz')
    when_list._when.append('not qux')

    all_vars = dict(foo='bar', bar='baz', baz=True, qux=False)
    templar = None
    expected = False
    actual = when_list.evaluate_conditional(templar, all_vars)
    assert actual == expected

    all_vars = dict(foo=None, bar=None, baz=None, qux=True)
    templ

# Generated at 2022-06-22 11:40:43.388890
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.template.safe_eval import test_cond_test

    cond = Conditional()

    for (c, expected) in test_cond_test:
        got = cond.extract_defined_undefined(c)
        assert got == expected, "Test failed for conditional %s, got %s, expected %s" % (c, got, expected)


# Generated at 2022-06-22 11:40:51.082373
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    """
    Test for method extract_defined_undefined of class Conditional
    """

    display.vvvv('')
    display.vvvv('Unit test for method extract_defined_undefined of class Conditional')

    # Test cases
    test_cases = [
        """{{ foobar is defined }}""",
        """{{ foobar is not defined or foobar is defined }}""",
        """{{ foobar is undefined or foobar is defined }}""",
        """{{ foo is defined and foobar is undefined or foobar is defined }}""",
        """{{ foo is defined and (foobar is undefined or foobar is defined) }}""",
        """{{ (foo is defined and foobar is defined) and foobar is undefined }}""",
        """{{ foobar.stdout == 'foooooo' and foobar.rc == 8 }}""",
    ]

# Generated at 2022-06-22 11:40:52.527555
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()

# Generated at 2022-06-22 11:41:03.352242
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    class TestData_Conditional(object):

        @property
        def _name(self):
            return None

        @property
        def _ds(self):
            return None

        def __init__(self, when):
            self.when = when

    class TestModule(object):
        pass

    loader = DataLoader()

    tmp = Templar(loader=loader, shared_loader_obj=loader, variables={'ansible_distribution': 'AmigaDOS'})

    tmp.set_available_variables(VariableManager().get_vars(loader=loader, play=PlayContext(TestModule())))
   

# Generated at 2022-06-22 11:41:16.929555
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    from ansible.template import Templar

    t = Templar(loader=loader, variables={'testvar': "testvalue"})
    c = Conditional(loader=loader)
    assert c.evaluate_conditional(t, {})

    c.when = ["testvar"]
    assert c.evaluate_conditional(t, {})

    c.when = ["testvar == 'testvalue'"]
    assert c.evaluate_conditional(t, {})

    c.when = ["testvar == 'nottestvalue'"]
    assert not c.evaluate_conditional(t, {})

    c.when = ['"testvalue"' == "testvar"]
    assert c.evaluate_conditional(t, {})


# Generated at 2022-06-22 11:41:29.223366
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.utils.unicode import to_unicode
    import os

    loader = DataLoader()
    fake_vid = plugin_loader.get_vars_loader(loader)
    inventory = InventoryManager(loader, sources='localhost,')
    variable_manager = VariableManager(loader=fake_vid, inventory=inventory)

# Generated at 2022-06-22 11:41:39.382899
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    loader = DummyLoader()
    host = DummyHost()
    task = Conditional(loader=loader)
    templar = Templar(loader=loader, variables=dict(x=True, y=False))
    host.vars = dict(z=True)
    # single when var
    task.when = ['x']
    assert task.evaluate_conditional(templar, host.get_vars())
    task.when = ['y']
    assert not task.evaluate_conditional(templar, host.get_vars())
    task.when = ['z']
    assert task.evaluate_conditional(templar, host.get_vars())
    task.when = ['z and x']
    assert task.evaluate_conditional(templar, host.get_vars())

# Generated at 2022-06-22 11:41:48.742664
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Todo: add test
    pass


# Generated at 2022-06-22 11:41:59.792229
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional_obj = Conditional()
    conditional_list = [ 'not (somevar is defined) and (othervar is defined)', 'not somevar|default("not defined")|int == 123', 'somevar|default("not defined") == "foo"', 'somevar is defined', 'somevar is not defined' ]
    for condition in conditional_list:
        result = conditional_obj.extract_defined_undefined(condition)
        assert isinstance(result, list)
        for item in result:
            assert len(item) == 3
            assert(item[1] == 'is' or item[1] == 'is not' or item[1] == 'not is')
            assert(item[2] == 'defined' or item[2] == 'undefined')
            assert VALID_VAR_REGEX.match(item[0])

# Generated at 2022-06-22 11:42:10.251133
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display = Display()
    # First test without error
    conditional_test_class = Conditional()
    conditional_test_class._ds = None
    conditional_test_class.when = [u'ansible_eth0', u'ansible_eth1']
    all_vars = dict(ansible_eth0=dict(device=u'eth0', speed=u'10'), ansible_eth1=None)

    display.debug(u'ConditionalTestClass properties:')
    for k, v in conditional_test_class.__dict__.items():
        display.debug(u'%s %s' % (k, v))

    display.debug(u'When expression:')
    for item in conditional_test_class.when:
        display.debug(u'%s' % item)


# Generated at 2022-06-22 11:42:19.607881
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert set(Conditional().extract_defined_undefined('1 == 3 or (not foo is defined and True)')) == set([('foo', 'not is', 'defined')])
    assert set(Conditional().extract_defined_undefined('1 == 3 or (foo is undefined or True)')) == set([('foo', 'is', 'undefined')])
    assert set(Conditional().extract_defined_undefined('1 == 3 or (bar is not defined or True)')) == set([('bar', 'is not', 'defined')])
    assert set(Conditional().extract_defined_undefined('1 == 3 or ("bar" is not defined or True)')) == set([('bar', 'is not', 'defined')])

# Generated at 2022-06-22 11:42:31.108304
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-22 11:42:38.266584
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    ''' unit test for method extract_defined_undefined of class Conditional '''
    conditional = Conditional()

    assert conditional.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert conditional.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert conditional.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]
    assert conditional.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]
    assert conditional.extract_defined_undefined('foo and bar is defined') == [('bar', 'is', 'defined')]
    assert conditional.extract_defined_undefined('foo and bar is not defined')

# Generated at 2022-06-22 11:42:50.081756
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert DEFINED_REGEX.search("foo is not defined")
    assert DEFINED_REGEX.search("foo is not defined and bar is not defined")
    assert DEFINED_REGEX.search("bar is undefined")
    assert DEFINED_REGEX.search("bar not is defined")
    assert DEFINED_REGEX.search("bar is undefined and foo is not defined")
    assert DEFINED_REGEX.search("bar is undefined and hostvars['foo'] is not defined")
    assert DEFINED_REGEX.search("hostvars['foo']is undefined")
    assert DEFINED_REGEX.search("hostvars['foo']isnot defined")
    assert DEFINED_REGEX.search("hostvars['foo']\tis defined")


# Generated at 2022-06-22 11:43:02.595546
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Make a Conditional object available
    module = _get_module_mock()
    cond = Conditional()
    cond._loader=module._loader

    # Test some defined/undefined conditions

# Generated at 2022-06-22 11:43:14.032954
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    c = Conditional()

    assert c.extract_defined_undefined('') == []
    assert c.extract_defined_undefined('foo') == []
    assert c.extract_defined_undefined('foo not is undefined') == [('foo', 'not', 'undefined')]
    assert c.extract_defined_undefined('foo not is undefined and bar') == [('foo', 'not', 'undefined')]
    assert c.extract_defined_undefined('foo and bar not is undefined') == [('bar', 'not', 'undefined')]
    assert c.extract_defined_undefined('foo not is undefined and bar not is undefined') == [('foo', 'not', 'undefined'), ('bar', 'not', 'undefined')]

# Generated at 2022-06-22 11:43:25.222349
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert (Conditional.extract_defined_undefined("x is defined") == [('x', 'is', 'defined')])
    assert (Conditional.extract_defined_undefined("x is defined and y is defined") == [('x', 'is', 'defined'), ('y', 'is', 'defined')])
    assert (Conditional.extract_defined_undefined("x is defined and y is undefined") == [('x', 'is', 'defined'), ('y', 'is', 'undefined')])
    assert (Conditional.extract_defined_undefined("x is not defined and y is not defined") == [('x', 'is not', 'defined'), ('y', 'is not', 'defined')])

# Generated at 2022-06-22 11:43:42.683571
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inv)
    templar = Templar(loader=loader, variables=variable_manager)

    conditional = Conditional(loader=loader)

    # test with a valid conditional string
    assert conditional.evaluate_conditional(templar, {})

    conditional.when = ['False']
    assert not conditional.evaluate_conditional(templar, {})

    conditional.when = ['False', 'False']
    assert not conditional.evaluate_conditional(templar, {})


# Generated at 2022-06-22 11:43:55.060625
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    variable_manager = VariableManager(loader=None)

# Generated at 2022-06-22 11:44:00.720882
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # given
    cond_str = "foo is defined and bar is undefined"
    item = Conditional()
    # when
    result = item.extract_defined_undefined(cond_str)
    # then
    assert result == [('foo', 'is', 'defined'), ('bar', 'is', 'undefined')]



# Generated at 2022-06-22 11:44:13.746960
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # setup test objects
    variable_manager = VariableManager()
    loader = DictDataLoader({})

    play_context = dict(
        become_method='sudo',
        become_user='testuser',
        check_mode=True,
        diff=False,
        error_on_undefined_vars=True,
        listtags=False,
        listtasks=False,
        listhosts=False,
        roles_path=C.DEFAULT_ROLES_PATH,
    )

    templar = Templar(loader=loader, variables=variable_manager, play_context=play_context)

    conditional = Conditional(loader=loader)
    conditional.when = ["a > b"]

    variable_manager.set_host

# Generated at 2022-06-22 11:44:26.580126
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    play_context = Dummy()
    play_context.vault_password = None
    play_context.become = True
    play_context.become_user = 'root'
    all_vars = VariableManager()
    all_vars.extra_vars = dict(a=True, b=3)
    templar = Templar(loader=None, variables=all_vars, vault_secrets=VaultLib(None), context=play_context, shared_loader_obj=play_context)
    conditional = Conditional(loader=None)
    assert conditional.evaluate_conditional(templar, all_vars)
    conditional.when = ['a']

# Generated at 2022-06-22 11:44:34.888496
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:44:46.828726
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    # project root path
    from os.path import dirname, abspath, join
    root = abspath(dirname(dirname(dirname(dirname(__file__)))))

    # test playbook context
    play_context = PlayContext()
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 22
    play_context.remote_user = 'vagrant'
    play_context.connection = 'ssh'
    play_context.become = False
    play_context.become_method = 'sudo'

# Generated at 2022-06-22 11:44:56.003485
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:45:05.108133
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Test(Conditional):
        def __init__(self):
            super(Test, self).__init__()
            self._ds = None
            self.when = list()

    test = Test()
    test.when = list()
    
    from ansible.template import Templar
    t = Templar(loader=None, shared_loader_obj=None, variables={'a':1})

    #test of case when condition is True
    test.when = [True]
    result = test.evaluate_conditional(t, None)
    assert result, "evaluate_conditional returned wrong result: " + str(result) + \
            " with condition: " + str(test.when)

    #test of case when condition is False
    test.when = [False]
    result = test.evaluate_conditional(t, None)
   

# Generated at 2022-06-22 11:45:16.805350
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined("my_var is not defined") == [("my_var", "is not", "defined")]
    assert conditional.extract_defined_undefined("my_var is not defined and my_var2 is defined") == [("my_var", "is not", "defined"), ("my_var2", "is", "defined")]
    assert conditional.extract_defined_undefined("my_var is not defined or my_var2 is defined") == [("my_var", "is not", "defined"), ("my_var2", "is", "defined")]

# Generated at 2022-06-22 11:45:45.235754
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Test that invalid statements always return an empty array
    assert Conditional().extract_defined_undefined("foo is undefined") == []
    assert Conditional().extract_defined_undefined("foo is defined") == []
    assert Conditional().extract_defined_undefined("foo is") == []
    assert Conditional().extract_defined_undefined("is foo") == []
    assert Conditional().extract_defined_undefined("foo not is undefined") == []
    assert Conditional().extract_defined_undefined("foo not is defined") == []

    # Test that valid statements always return the right tuple
    assert Conditional().extract_defined_undefined("foo is undefined") == [('foo', 'is', 'undefined')]

# Generated at 2022-06-22 11:45:55.202502
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()

    assert c.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]

    assert c.extract_defined_undefined('foo not is defined') == [('foo', 'not is', 'defined')]

    assert c.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]

    assert c.extract_defined_undefined('foo not is undefined') == [('foo', 'not is', 'undefined')]

    assert c.extract_defined_undefined('foo is defined or foo is undefined') == [('foo', 'is', 'defined'), ('foo', 'is', 'undefined')]


# Generated at 2022-06-22 11:46:07.943447
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.module_utils.six import StringIO
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    class SampleConditional(Conditional):
        pass

    # empty when:
    data = dict(
        when=list(),
        )

    obj = SampleConditional()
    obj.vars = data

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    result = obj.evaluate_conditional(templar, {})
    assert result

    # single when:

# Generated at 2022-06-22 11:46:08.685671
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()

# Generated at 2022-06-22 11:46:20.932741
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined('hostvars[inventory_hostname] is defined') == [('hostvars[inventory_hostname]', 'is', 'defined')]
    assert conditional.extract_defined_undefined('hostvars[inventory_hostname] is defined and hostvars[inventory_hostname] is defined') == [('hostvars[inventory_hostname]', 'is', 'defined'), ('hostvars[inventory_hostname]', 'is', 'defined')]

# Generated at 2022-06-22 11:46:33.809240
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    cond = Conditional()

    test_cases = [
        # input, expected output
        ('', []),
        ('foo is defined', [('foo', 'is', 'defined')]),
        ('foo not is undefined', [('foo', 'not is', 'undefined')]),
        ('foo is undefined', [('foo', 'is', 'undefined')]),
        ('foo is bar', []),
        (r'foo is defined and hostvars["bar"] is undefined', [('foo', 'is', 'defined'), (r'hostvars["bar"]', 'is', 'undefined')]),
    ]

    for test_case in test_cases:
        actual_output = cond.extract_defined_undefined(test_case[0])

# Generated at 2022-06-22 11:46:42.733470
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host

    task = Task()
    host = Host()
    host.name = 'foobar'

    # test keys and values

    # normal
    task.set_loader(None)
    task.when = ["{{ foo }} == 'bar'"]
    assert task.evaluate_conditional({'foo': 'bar'}, host) is True
    assert task.evaluate_conditional({'foo': 'bar123'}, host) is False

    # case insensitive
    task.set_loader(None)
    task.when = ["{{ foo }} == 'BAR'"]
    assert task.evaluate_conditional({'foo': 'bar'}, host) is True
    task.when = ["{{ foo }} == 'bar'"]

    # value as integer
    task

# Generated at 2022-06-22 11:46:51.260000
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    mock_ds = type('MockDS', (object,), {})()

    class TestConditional(Conditional):
        def __init__(self):
            self.when = [None, '', True, False, 'foo','"bar"']
            self.when[0] = "foo | bool"
            self.when[1] = "not foo"
            self.when[2] = "bar.baz is defined"
            self.when[3] = "baz.foo is undefined"
            self.when[4] = "lookup('foo', 'bar')"
            self.when[5] = "lookup('foo', 'bar')"
            self._ds = mock_ds


# Generated at 2022-06-22 11:47:00.823340
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:47:12.754711
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined("hostvars['hostname'] is defined") == [('hostvars[\'hostname\']', 'is', 'defined')]
    assert conditional.extract_defined_undefined("hostvars['hostname'] is not defined") == [('hostvars[\'hostname\']', 'is not', 'defined')]
    assert conditional.extract_defined_undefined("hostvars['hostname'] is undefined") == [('hostvars[\'hostname\']', 'is', 'undefined')]
    assert conditional.extract_defined_undefined("hostvars['hostname'] is not undefined") == [('hostvars[\'hostname\']', 'is not', 'undefined')]

# Generated at 2022-06-22 11:47:55.378697
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from jinja2 import Environment, DictLoader

    # Load fake inventory
    inventory = {}

    class MyTask(Conditional):
        def __init__(self, loader):
            self._loader = loader
            # add fake inventory
            self._inventory = inventory

    # Setup jinja2 Environment
    environment = Environment(loader=DictLoader({
        'f1': u'{{ a }}',
        'f2': u'{{ b }}',
        'f3': u'{{ c }}',
        'f4': u'{{ d }}',
        'f5': u'{{ e }}',
    }))


# Generated at 2022-06-22 11:48:01.331611
# Unit test for constructor of class Conditional
def test_Conditional():
    temp = Conditional()

    assert (temp._when == [])
    assert (hasattr(temp, "_loader") == False)
    assert (hasattr(temp, "_ds") == False)



# Generated at 2022-06-22 11:48:08.379710
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    t = Conditional()
    assert t.extract_defined_undefined("hostvars['x'] not is defined") == [('hostvars[\'x\']', 'not is', 'defined')]
    assert t.extract_defined_undefined("hostvars['x'] is not defined") == [('hostvars[\'x\']', 'is not', 'defined')]
    assert t.extract_defined_undefined("hostvars['x'] is undefined") == [('hostvars[\'x\']', 'is', 'undefined')]
    assert t.extract_defined_undefined("hostvars['x'] not is undefined") == [('hostvars[\'x\']', 'not is', 'undefined')]

# Generated at 2022-06-22 11:48:18.837566
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import merge_hash
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.vars import VariableManager
    from ansible.parsing.dataloader import Data

# Generated at 2022-06-22 11:48:24.782203
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Prepare
    test_conditional = Conditional()
    # Actual Call
    conditional_list = test_conditional.extract_defined_undefined("hostvars['foo'] is defined")
    # Assert
    assert conditional_list == [('hostvars[\'foo\']', 'is', 'defined')]

# Generated at 2022-06-22 11:48:34.957662
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory("localhost"))

    cond = Conditional(loader=loader)
    cond._ds = dict(name="foo")
    assert cond.evaluate_conditional(variable_manager.extra_vars_loader, {})

    cond = Conditional(loader=loader)
    cond._when = [ False ]
    assert not cond.evaluate_conditional(variable_manager.extra_vars_loader, {})

    cond = Conditional(loader=loader)
    cond._when = [ '"a" in hostvars[inventory_hostname]' ]

# Generated at 2022-06-22 11:48:44.414554
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    this function tests the method evaluate_conditional of class Conditional

    :return:
    '''
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # define test cases
    TestCase = collections.namedtuple('test_tuple', [
        'description',
        'conditional',
        'all_vars',
        'assert_result',
    ])

# Generated at 2022-06-22 11:48:55.663718
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """Test evaluate_conditional() of class Conditional

    This is a unit test for the method evaluate_conditional() of class Conditional.
    """

    ############################################################
    # Test setup

    # Define a MockTemplar class
    class MockTemplar:
        def __init__(self):
            self.available_variables = None

        def is_template(self, data):
            """A mock method to replace Templar.is_template"""
            return True

        def template(self, template, disable_lookups=False):
            """A mock method to replace Templar.template"""
            return template

    # Define a MockConditional class
    class MockConditional(Conditional):
        def __init__(self):
            self.when = None
            self._loader = None

    # Define various testing data

# Generated at 2022-06-22 11:49:07.846318
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test basic functionality of evaluate_conditional
    class Test(Conditional):
        pass
    test = Test()
    all_vars = dict()
    templar = MagicMock()
    templar.template.return_value = True
    result = test.evaluate_conditional(templar, all_vars)
    assert result

    # Test works with a mock object
    test = Test(MagicMock())
    result = test.evaluate_conditional(templar, all_vars)
    assert result

    # Test works with a mock object and undefined vars
    templar.template.return_value = None
    result = test.evaluate_conditional(templar, all_vars)
    assert not result

    # Test works with a missing item in all_vars

# Generated at 2022-06-22 11:49:20.244999
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play import Play
    from ansible.template import Templar

    play_obj = Play.load(dict(
        name = 'test play',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='this should display')))
        ]
    ), loader=None)

    # test with no when specified
    task_obj = play_obj.tasks[0]
    assert task_obj.evaluate_conditional(Templar({}), {})
    assert task_obj.evaluate_conditional(Templar({}), dict(foo='bar'))

    # test with when specified with a "True" value
    task_obj = play_obj.tasks[0]