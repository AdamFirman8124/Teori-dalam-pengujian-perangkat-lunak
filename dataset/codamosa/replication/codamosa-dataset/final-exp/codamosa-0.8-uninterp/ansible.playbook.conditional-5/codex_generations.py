

# Generated at 2022-06-22 11:40:25.507846
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    import sys
    import tempfile
    import os
    import json
    import difflib
    import shutil
    #from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play

    sys.stdout = tempfile.TemporaryFile(mode='w+')
    sys.stderr = tempfile.TemporaryFile(mode='w+')
    dummy_play = Play().load({
        'name': 'test',
        'hosts': 'dummy',
        'gather_facts': True,
        'tasks': []
    }, variable_manager=VariableManager(), loader=DataLoader())

    dummy_conditional = Conditional(loader=DataLoader())


# Generated at 2022-06-22 11:40:28.085124
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    run_test = False
    if run_test == True:
        pass


# Generated at 2022-06-22 11:40:32.407305
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined('hostvars["foo"] is not defined') == [('hostvars["foo"]', 'is not', 'defined')]
    assert Conditional().extract_defined_undefined('hostvars[foo] is defined and ansible_version is defined') == [('hostvars[foo]', 'is', 'defined'), ('ansible_version', 'is', 'defined')]
    assert Conditional().extract_defined_undefined('') == []
    assert Conditional().extract_defined_undefined('foo is a not good') == []


# Generated at 2022-06-22 11:40:33.293700
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    pass

# Generated at 2022-06-22 11:40:37.806435
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import jinja2.exceptions


# Generated at 2022-06-22 11:40:46.916263
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VariableManager

    conditional = Conditional()

    # without templar
    assert conditional.evaluate_conditional(None, {}) == True
    assert conditional.evaluate_conditional(None, {'foo': 'bar'}) == True
    assert conditional.evaluate_conditional(None, {'bar': 'foo'}) == True
    assert conditional.evaluate_conditional(None, {'baz': 'foo'}) == True

    # with templar

# Generated at 2022-06-22 11:41:00.045539
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def test_extract_defined_undefined(conditional, expected):
        conditional = Conditional()
        result = conditional.extract_defined_undefined(conditional=conditional)
        assert result == expected

    test_extract_defined_undefined(conditional="foo is defined", expected=[('foo', 'is', 'defined')])
    test_extract_defined_undefined(conditional="foo is not defined", expected=[('foo', 'is', 'not defined')])
    test_extract_defined_undefined(conditional="foo is undefined", expected=[('foo', 'is', 'undefined')])
    test_extract_defined_undefined(conditional="foo is not undefined", expected=[('foo', 'is', 'not undefined')])

# Generated at 2022-06-22 11:41:13.648245
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:41:25.921915
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test the method evaluate_conditional with an empty list
    class TestConditional(Conditional):
        _when = [ ]
    tc = TestConditional()
    assert tc.evaluate_conditional('', '') is True
    assert tc.evaluate_conditional(None, '') is True

    # Test the method evaluate_conditional with None and False literals
    class TestConditional2(Conditional):
        _when = [ None, False ]
    tc = TestConditional2()
    assert tc.evaluate_conditional('', '') is True
    assert tc.evaluate_conditional(True, '') is False
    assert tc.evaluate_conditional(False, '') is False

    # Test the method evaluate_conditional with an string that evaluates to false

# Generated at 2022-06-22 11:41:37.875713
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.base import Base

    def test_playbook():
        return Base()

    #############################################################
    #### Conditional evaluation
    #############################################################
    # setup test playbook
    play_pb = test_playbook()
    play_vars = dict(a=1, b=2)
    play_pb.vars = play_vars
    play_pb._included_files = []

    # setup test task
    task_pb = test_playbook()
    task_pb.action = 'test task'
    task_pb.deprecate_warn = task_pb.deprecate = False
    task_pb._ds = dict(name='test task')
    task_pb._parent = play_pb
    task_pb.set_loader(play_pb._loader)

    #

# Generated at 2022-06-22 11:41:49.839797
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.inventory.manager import InventoryManager

    # Arrange
    cond = Conditional()
    templar = AnsibleMockTemplar()

    # Act/Assert for undefined variable
    try:
        cond.evaluate_conditional(templar, dict())
        assert False #  expected an exception
    except AnsibleUndefinedVariable:
        pass

    # Act/Assert for undefined variable
    try:
        all_vars = dict(hostvars=dict(host1=dict(foo="bar")))
        cond.evaluate_conditional(templar, all_vars)
        assert False #  expected an exception
    except AnsibleUndefinedVariable:
        pass

    # Act/Assert for True
    cond.when = True
    assert cond.evaluate_conditional(templar, dict())

   

# Generated at 2022-06-22 11:41:56.756378
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    # Create a Conditional object
    from ansible.playbook.base import Conditional, Base
    from ansible.parsing.dataloader import DataLoader

    class C(Conditional):
        pass

    obj = C(loader=DataLoader())

    conditional = "foo is defined"
    print(obj.extract_defined_undefined(conditional))

    conditional = "foo is not defined"
    print(obj.extract_defined_undefined(conditional))

    conditional = "foo is defined"
    print(obj.extract_defined_undefined(conditional))

    conditional = "foo is defined and bar is not defined"
    print(obj.extract_defined_undefined(conditional))

    conditional = "foo is defined or bar is not defined"

# Generated at 2022-06-22 11:42:07.748336
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    test_cases = [
        ('foo is defined', [('foo', 'is', 'defined')]),
        ('foo is not defined', [('foo', 'is not', 'defined')]),
        ('foo is undefined', [('foo', 'is', 'undefined')]),
        ('foo is not undefined', [('foo', 'is not', 'undefined')]),
        ('foo is not defined or bar is defined', [('foo', 'is not', 'defined'), ('bar', 'is', 'defined')]),
        ('foo is not defined and bar is defined', [('foo', 'is not', 'defined'), ('bar', 'is', 'defined')]),
    ]

    for test_case in test_cases:
        extractions = Conditional.extract_defined_undefined(Conditional(), test_case[0])

# Generated at 2022-06-22 11:42:16.034560
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    load_from_file = True
    try:
        from ansible.parsing.dataloader import DataLoader

        loader = DataLoader()
        c = Conditional(loader=loader)
        templar = Templar(loader=loader, variables={'o': {'k': 'v'}})
        # one simple test for now
        m = c.evaluate_conditional(templar, {'o': {'k': 'v'}})
        assert m is True
    except ImportError:
        load_from_file = False
        raise


from ansible.template import Templar



# Generated at 2022-06-22 11:42:27.488631
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    import jinja2
    import sys
    import unittest2 as unittest

    class TestConditional(Conditional):

        def __init__(self):

            loader = jinja2.DictLoader({
                'fake_template.j2': '{{ fake_var }}',
            })
            variable_manager = VariableManager()

            #when used directly, this class needs a loader, but we want to
            #make sure we don't trample on the existing one if this class
            #is used as a mix-in with a playbook base class
            self._loader = loader


# Generated at 2022-06-22 11:42:39.828124
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestConditional:
        _ds = None
        _task = None

        def __init__(self, when, templar, all_vars):
            self.when = [when]
            self._loader = None

            self.evaluate_conditional(templar, all_vars)

    # Test possible conditions

# Generated at 2022-06-22 11:42:50.516850
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    pc = PlayContext()
    templar = Templar(loader=None, variables={})

    # initializing when
    when = list()

    # conditional expression
    when.append(True)
    when.append('1')
    when.append('1 == 1')

    task_ds = dict()
    task_ds['when'] = when

    try:
        task = Conditional(loader=None)
        task.load_data(task_ds, loader=None)
        assert task.evaluate_conditional(templar, pc)
    except AnsibleError as e:
        pytest.fail("evaluate_conditional failed with: %s" % to_native(e))


# Generated at 2022-06-22 11:43:02.730846
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    # TODO: move this to a testcase
    assert conditional.extract_defined_undefined('hostvars[inventory_hostname] is defined and hostvars[inventory_hostname]["os_family"] == "RedHat"') == [('hostvars[inventory_hostname]', 'is', 'defined')]
    assert conditional.extract_defined_undefined('hostvars[inventory_hostname] is undefined and hostvars[inventory_hostname]["os_family"] == "RedHat"') == [('hostvars[inventory_hostname]', 'is', 'undefined')]

# Generated at 2022-06-22 11:43:14.164887
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:43:26.101413
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.module_utils.six import BytesIO
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from units.mock.loader import DictDataLoader

    conditional_obj = Conditional()

    # test when conditional is None
    assert conditional_obj.evaluate_conditional(Templar(DictDataLoader(), variable_manager=VariableManager()), variable_manager=VariableManager()) is True

    # test when conditional is boolean True
    assert conditional_obj.evaluate_conditional(Templar(DictDataLoader(), variable_manager=VariableManager()), variable_manager=VariableManager(), conditional=True) is True

    # test when conditional evaluates to True
    conditional_obj.when = "foo.bar"


# Generated at 2022-06-22 11:43:42.938480
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined("foo is defined and bar is not undefined") == [('foo', 'is', 'defined'), ('bar', 'is not', 'undefined')]


# Generated at 2022-06-22 11:43:55.419308
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class ConditionalTest(Conditional):
        def __init__(self, loader=None):
            super(ConditionalTest, self).__init__(loader=loader)

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader_obj = DataLoader()
    variable_manager = VariableManager(loader=loader_obj)

    mock_ds = dict()
    mock_ds['hostvars'] = dict()
    mock_ds['hostvars']['test_host'] = dict()

    mock_ds['hostvars']['test_host']['foo'] = 5
    mock_ds['hostvars']['test_host']['bar'] = False
    mock_ds['hostvars']['test_host']['baz']

# Generated at 2022-06-22 11:44:05.294184
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar

    variables = 2

    class TestClass(Conditional):
        def __init__(self, test_value):
            self._loader = DataLoader()
            self.variable_manager = VariableManager(loader=self._loader, variables=variables)
            self.templar = Templar(loader=self._loader, variables=self.variable_manager)
            self.when = test_value

    # test cases for normal evaluation

# Generated at 2022-06-22 11:44:16.493290
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars import VariableManager, DataLoader

    loader = DataLoader()
    vars_mgr = VariableManager(loader)
    templar = Templar(loader, vars_mgr)

    def assert_equal(conditional, result):
        assert conditional.evaluate_conditional(templar, vars_mgr.get_vars(loader=loader, play=None, host=None, task=None)) == result

    c = Conditional()

    c.when = [True]
    assert_equal(c, True)

    c.when = [False]
    assert_equal(c, False)

    c.when = [True, True]
    assert_equal(c, True)

    c.when = [True, False]

# Generated at 2022-06-22 11:44:28.173762
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = "var1 is defined and var2 not is undefined"
    obj = Conditional()
    results = obj.extract_defined_undefined(conditional)
    assert results[0][0] == 'var1'
    assert results[0][1] == 'is'
    assert results[0][2] == 'defined'
    assert results[1][0] == 'var2'
    assert results[1][1] == 'not is'
    assert results[1][2] == 'undefined'

    conditional = "var1 is defined"
    obj = Conditional()
    results = obj.extract_defined_undefined(conditional)
    assert results[0][0] == 'var1'
    assert results[0][1] == 'is'
    assert results[0][2] == 'defined'


# Generated at 2022-06-22 11:44:31.618840
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()
    conditional = "var1 is not defined or var2 is defined"
    result = cond.extract_defined_undefined(conditional)
    assert result == [('var1', 'is not', 'defined'), ('var2', 'is', 'defined')], result


# Generated at 2022-06-22 11:44:43.649867
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    cond = Conditional()

    assert cond.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert cond.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert cond.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]
    assert cond.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]

    assert cond.extract_defined_undefined('foo not is defined') == [('foo', 'not is', 'defined')]
    assert cond.extract_defined_undefined('foo not is not defined') == [('foo', 'not is not', 'defined')]
    assert cond.extract

# Generated at 2022-06-22 11:44:49.272069
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display.verbosity = 3
    display.debug('verbose: %s %s %s %s' % (
        display.verbose, display.debug, display.deprecated, display.skipped))
    assert Display.verbosity == 3
    assert Display.verbose == 3
    assert Display.debug == 3
    assert Display.deprecated == 0
    assert Display.skipped == 0

    tester = Conditional()
    loader, variable_manager, inventory, data = tester._loader, variable_manager, inventory, data
    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=inventory)

    context = {}
    all_vars = {}
    # Unhandled conditional
    conditional = 10


# Generated at 2022-06-22 11:45:01.069860
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    test case for method extract_defined_undefined of class Conditional
    '''
    conditional = Conditional()
    test_data = [
        ('foo is not undefined', [ ('foo', 'is not', 'undefined') ]),
        ('foo is undefined', [ ('foo', 'is', 'undefined') ]),
        ('not foo', [ ]),
        ('foo is not undefined and bar not defined', [ ('foo', 'is not', 'undefined'), ('bar', 'not', 'defined') ]),
        ('foo is not defined or bar is not undefined', [ ('foo', 'is not', 'defined'), ('bar', 'is not', 'undefined') ]),
    ]
    for test in test_data:
        test_results = conditional.extract_defined_undefined(test[0])

# Generated at 2022-06-22 11:45:12.180060
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

    data = conditional.extract_defined_undefined('foo is defined')
    assert len(data) == 1
    assert data[0][0] == 'foo'
    assert data[0][1] == 'is'
    assert data[0][2] == 'defined'

    data = conditional.extract_defined_undefined('foo is bar is defined')
    assert len(data) == 1
    assert data[0][0] == 'foo is bar'
    assert data[0][1] == 'is'
    assert data[0][2] == 'defined'

    data = conditional.extract_defined_undefined('foo is defined or bar is not defined')
    assert len(data) == 2
    assert data[0][0] == 'foo'

# Generated at 2022-06-22 11:45:51.026438
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader, variables={'hostvars': {'host1': {'a': 1}, 'host2': {'a': 2}, 'host3': {'a': 3}}})

    assert Conditional(loader=loader).evaluate_conditional(templar, [])

    assert Conditional(loader=loader, when=[True]).evaluate_conditional(templar, [])
    assert not Conditional(loader=loader, when=[False]).evaluate_conditional(templar, [])

    assert Conditional(loader=loader, when=['a == 1']).evaluate_conditional(templar, {'a': 1})
    assert not Conditional(loader=loader, when=['a == 1']).evaluate

# Generated at 2022-06-22 11:45:52.299727
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # todo
    pass

# Generated at 2022-06-22 11:46:03.330511
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """
    the method evaluate_conditional returns False if the
    conditional evaluates as such.
    """
    CONDITIONAL_DATA = [
        (['ldap_user.get("cn") == "Foo" or ldap_user.get("givenName") == "Foo"'], True),
        (['ansible_user == "Foo"'], False),
    ]

    display = Display()
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, None)

    for (when, result) in CONDITIONAL_DATA:
        task = MyTask(loader=loader)
        task.when = when
        variable_manager.set_host_variable(inventory.get_host("localhost"), "ansible_user", "Foo")
        variable_manager

# Generated at 2022-06-22 11:46:15.199176
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    inv = dict(
        group1=dict(
            hosts=['localhost'],
            vars=dict(
                foo=1,
                bar=dict(
                    baz=2
                )
            )
        ),
        group2=dict(
            hosts=['localhost'],
            vars=dict(
                baz=3,
                bar=dict(
                    foo=2
                )
            )
        )
    )
    connection = 'local'

# Generated at 2022-06-22 11:46:26.630446
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.template import Templar

    my_host = Host(name='test_host')
    my_group = Group(name="test_group")
    my_group.add_host(my_host)
    my_inventory = Inventory("test_inventory")
    my_inventory.add_group(my_group)
    my_inventory.add_host(my_host)

# Generated at 2022-06-22 11:46:37.481514
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    conditional = Conditional(None)

    test_expression = u"a is defined or b is undefined or c is not defined or d is not undefined"
    expected_result = [(u"a", u"is", u"defined"),
                       (u"b", u"is", u"undefined"),
                       (u"c", u"is not", u"defined"),
                       (u"d", u"is not", u"undefined")]
    result = conditional.extract_defined_undefined(test_expression)
    assert result == expected_result

    test_expression = u""
    expected_result = []
    result = conditional.extract_defined_undefined(test_expression)
    assert result == expected_result

    test_expression = u"a is defined"

# Generated at 2022-06-22 11:46:49.295481
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # test type argument
    conditional = Conditional()
    assert conditional.extract_defined_undefined("") == []
    assert conditional.extract_defined_undefined("a") == []
    assert conditional.extract_defined_undefined("defined") == []
    assert conditional.extract_defined_undefined("undefined") == []
    assert conditional.extract_defined_undefined("a is defined") == []
    assert conditional.extract_defined_undefined("a is defined and b") == []
    assert conditional.extract_defined_undefined("a is not defined and b is defined") == []
    assert conditional.extract_defined_undefined("a is defined or b is undefined") == []
    assert conditional.extract_defined_undefined("(a is not defined) or (b is undefined)") == []
    assert conditional

# Generated at 2022-06-22 11:46:59.631789
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class TestConditional(Conditional):
        def __init__(self, variable_manager, loader, play_context):
            super(TestConditional, self).__init__()
            self._variable_manager = variable_manager
            self._loader = loader
            self._play_context = play_context

    p = PlayContext()
    p.remote_addr = 'testhost'
    i = InventoryManager(loader=DataLoader(), sources=[])
    i.add_host('testhost')
    h = i.get_host('testhost')

# Generated at 2022-06-22 11:47:12.077651
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    Unit test for method extract_defined_undefined of class Conditional.
    '''
    cond = Conditional()

    result = cond.extract_defined_undefined(None)
    assert result == []

    result = cond.extract_defined_undefined(True)
    assert result == []

    result = cond.extract_defined_undefined('non_defined_undefined')
    assert result == []

    result = cond.extract_defined_undefined('hostvars["192.168.99.100"] is undefined')
    assert result == [('hostvars["192.168.99.100"]', 'is', 'undefined')]

    result = cond.extract_defined_undefined('hostvars[\'192.168.99.100\'] is undefined')

# Generated at 2022-06-22 11:47:24.758701
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    class TestConditional(Conditional):
        def __init__(self, ds):
            self._ds = ds
            self._loader = ds._loader
    pb = PlayContext()
    pb.VARIABLES = dict(foo='bar', baz=42, fact_fname='wendy', fact_spam='eggs')
    templar = pb.get_encoder()
    tc = TestConditional(pb)
    all_vars = dict(vars(pb), **pb.VARIABLES)
    assert tc.evaluate_conditional(templar, all_vars) is True
    tc.when = dict(test_conditional='foo == "bar"')

# Generated at 2022-06-22 11:48:27.518712
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:48:34.132121
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # test setup
    loader = DictDataLoader({
        "/playbook": """
        - hosts: all
          tasks:
            - debug:
                msg: "{{ condition }}"
              when: condition
          vars:
            condition: true
        """
    })
    playbook = PlayBook.load(loader, "/playbook")

    # test
    for t in playbook.get_plays()[0].get_tasks():
        assert t.evaluate_conditional(t._templar, t.vars)



# Generated at 2022-06-22 11:48:46.295438
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    c = Conditional()
    # case 1
    assert c.evaluate_conditional(Templar({}), {}) is True
    # case 2
    assert c.evaluate_conditional(Templar({"a": True}), {"a": True}) is True
    # case 3
    assert c.evaluate_conditional(Templar({"a": True}), {"a": False}) is False
    # case 4
    assert c.evaluate_conditional(Templar({"a": True}), {"a": True, "b": True}) is True
    # case 5
    assert c.evaluate_conditional(Templar({"a": True}), {"a": True, "b": False}) is True
    # case 6

# Generated at 2022-06-22 11:48:59.017722
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    hostname_vars = dict(hostname="test-host.test-domain.com")
    metrics_enabled_vars = dict(metrics_enabled=True)
    metrics_disabled_vars = dict(metrics_enabled=False)
    database_port_vars = dict(database_port=1234)
    database_host_vars = dict(database_host="test-host.test-domain.com")
    database_host_other_vars = dict(database_host="other-host.test-domain.com")

    cas_vars = dict(high_availability=True)
    cas_disabled_vars = dict(high_availability=False)
    cas_standalone_vars = dict(standalone=True)
    cassandra_vars = dict(cassandra=True)

    valid_vars

# Generated at 2022-06-22 11:49:10.123848
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    test_data = (
        "foo is a_defined_var and bar is not defined",
        "bar is defined or baz is undefined",
        "biz is 'defined'",
        "qux is not 'undefined'",
        "cow is defined or dog is undefined and fish is defined and bird is undefined"
    )


# Generated at 2022-06-22 11:49:21.732891
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # Dummy ds object
    class DsObj(object):
        def __init__(self):
            self._ds = None

    # Dummy class inheriting from Conditional
    class Conditional_test(Conditional, DsObj):
        def __init__(self):
            Conditional.__init__(self)

    # Dummy play_context object
    play_context = PlayContext()

    # Dummy templar object
    templar = Templar(play_context=play_context)

    conditional = Conditional_test()

    # This is to set hostvars value in all_vars
    all_vars = {}
    all_vars['hostvars'] = {}

# Generated at 2022-06-22 11:49:32.039355
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def _do_test(cond, expected):
        m = Conditional()
        res = m.extract_defined_undefined(cond)
        assert expected == res, "Got %s instead of %s" % (res, expected)

    _do_test(
        "hostvars['remote_addr'] is defined",
        [('hostvars[\'remote_addr\']', 'is', 'defined')]
    )
    _do_test(
        "hostvars[remote_addr] is not undefined",
        [('hostvars[remote_addr]', 'is not', 'undefined')]
    )

# Generated at 2022-06-22 11:49:42.509670
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:49:54.203551
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class TestConditional(Conditional):
        pass

    import jinja2
    from ansible.template import Templar

    env = jinja2.Environment(undefined=jinja2.StrictUndefined)
    templar = Templar(loader=None, variables={})

    my_host = TestConditional()

# Generated at 2022-06-22 11:50:04.513351
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    display.verbosity = 3
    all_vars = VariableManager()