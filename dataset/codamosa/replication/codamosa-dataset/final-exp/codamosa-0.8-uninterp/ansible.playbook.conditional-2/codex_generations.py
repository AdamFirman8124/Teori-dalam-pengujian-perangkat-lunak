

# Generated at 2022-06-22 11:40:25.709544
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def _test_extract_defined_undefined(test_case):
        conditional = Conditional()
        result = conditional.extract_defined_undefined(test_case['inputconditional'])
        assert result == test_case['expectedresult'], "For conditional input '{}' expected result '{}', received '{}'".format(test_case['inputconditional'], test_case['expectedresult'], result)


# Generated at 2022-06-22 11:40:31.904024
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory=inventory)

    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='Hello World')))
        ]
    ), variable_manager=variable_manager, loader=loader)

   

# Generated at 2022-06-22 11:40:33.594567
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    assert Conditional().evaluate_conditional(None, None)



# Generated at 2022-06-22 11:40:41.114046
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    conditional_object = Conditional(loader = None)

    # TODO: make this a mock
    play_context = PlayContext()
    templar = Templar(loader=None, variables={'foo': 'bar'},
                      shared_loader_obj=None, disable_lookups=False, play_context=play_context)

    # Test to make sure that regular expressions are working
    assert conditional_object.extract_defined_undefined("myvar is defined") == [('myvar', 'is', 'defined')]
    assert conditional_object.extract_defined_undefined("myvar not is undefined") == [('myvar', 'not is', 'undefined')]

# Generated at 2022-06-22 11:40:47.661934
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Test validate function of class Conditional
    '''
    import os
    import sys
    import copy
    import types

    import pytest

    # Test environment made available to tested method(s)
    module_path = os.path.realpath(os.path.join(__file__, '..', '..', '..', '..', '..', 'lib'))
    if module_path not in sys.path:
        sys.path.insert(0, module_path)

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins import loader

    inventory = InventoryManager

# Generated at 2022-06-22 11:40:54.907190
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional.extract_defined_undefined('{{ foo is not defined }} and {{ bar is defined }}') == [('foo', 'is not', 'defined'), ('bar', 'is', 'defined')]
    assert Conditional.extract_defined_undefined('{{ foo is defined }} or {{ bar is undefined }}') == [('foo', 'is', 'defined'), ('bar', 'is', 'undefined')]


# Generated at 2022-06-22 11:41:04.710439
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VersionedDict

    # Test for conditionals of type True, False, and of type string
    for test_conditional in [True, False, 'dummy_conditional']:
        conditional = Conditional()
        conditional._ds = None
        conditional.when = test_conditional
        templar = Templar(loader=None, variables={'foo': 'FOO'})
        assert conditional.evaluate_conditional(templar, VersionedDict()) == test_conditional

    # Test for conditionals of type list
    test_

# Generated at 2022-06-22 11:41:18.014125
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()


# Generated at 2022-06-22 11:41:30.364604
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    r = Conditional()

    # test 1:
    s = "hostvars['localhost'].var_one is defined and var_two.attr_one is defined"
    assert len(r.extract_defined_undefined(s)) == 2
    assert "hostvars['localhost'].var_one" in r.extract_defined_undefined(s)[0]
    assert "var_two.attr_one" in r.extract_defined_undefined(s)[1]

    # test 2:
    s = "var_one is defined or var_two.attr_one is defined"
    assert len(r.extract_defined_undefined(s)) == 2
    assert "var_one" in r.extract_defined_undefined(s)[0]
    assert "var_two.attr_one" in r

# Generated at 2022-06-22 11:41:39.968237
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # creating a dummy Conditional class for testing
    class Conditional_test(Conditional):
        def __init__(self):
            pass

    c = Conditional_test()

    assert c.extract_defined_undefined("") == []
    assert c.extract_defined_undefined("test_var is defined") == [("test_var", "is", "defined")]
    assert c.extract_defined_undefined("test_var is not defined") == [("test_var", "is not", "defined")]
    assert c.extract_defined_undefined("test_var is undefined") == [("test_var", "is", "undefined")]
    assert c.extract_defined_undefined("test_var is not undefined") == [("test_var", "is not", "undefined")]

# Generated at 2022-06-22 11:41:54.303938
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    res = c.extract_defined_undefined("[ 's1' == 's1' or 's2' == 's2' and foo is defined ]")
    assert res == [('foo', 'is', 'defined')]
    res = c.extract_defined_undefined("[ 's1' == 's1' or 's2' == 's2' ]")
    assert len(res) == 0


# Generated at 2022-06-22 11:42:05.853480
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # define some test data

# Generated at 2022-06-22 11:42:08.958514
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test the method evaluate_conditional of the class Conditional
    
    # Construct the class object
    conditional = Conditional()
    
    # 
    templar   = None
    all_vars  = None
    conditional.evaluate_conditional(templar, all_vars)



# Generated at 2022-06-22 11:42:13.016519
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Create a new instance of Conditional class
    c = Conditional()
    # Test evaluate_conditional method with no parameter
    assert c.evaluate_conditional() is not None



# Generated at 2022-06-22 11:42:15.259256
# Unit test for constructor of class Conditional
def test_Conditional():

    condition = Conditional()
    assert(condition is not None)


# Generated at 2022-06-22 11:42:23.083504
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.six import StringIO
    from ansible.template import Templar

    play_context = PlayContext()
    play_context.update_vars({'foo': 'bar'})

    templar = Templar(loader=None, variables=play_context.given_vars)

    all_vars = play_context.given_vars.copy()

    # Basic test
    assert Conditional().evaluate_conditional(templar, all_vars) is True

    # When with condition
    assert Conditional(when=[]).evaluate_conditional(templar, all_vars) is False

    # When with a string that is True

# Generated at 2022-06-22 11:42:34.392763
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.module_utils.six import StringIO
    from ansible.plugins import module_loader

    class WhenTest(object):
        def __init__(self, when, expected_result):
            self.when = when
            self.expected_result = expected_result

    def do_test(when_tests):
        m = module_loader.get_manager()
        cond = Conditional(m._loader)
        old_stderr = sys.stderr
        stderr = StringIO()
        sys.stderr = stderr
        for when_test in when_tests:
            result = cond.evaluate_conditional(m._loader.variable_manager, when_test.when)

# Generated at 2022-06-22 11:42:44.007817
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from jinja2 import Environment, DictLoader

    loader = DictLoader({'test_template': '{{ test_var }}'})
    j2_env = Environment(loader=loader, trim_blocks=True)
    j2_template = j2_env.get_template('test_template')

    class TestConditional(Conditional):
        pass

    test_conditional = TestConditional(loader=j2_template.new_context)

    # Test "when" param is a list
    test_conditional._when = ['test_var == "test_value"']
    with pytest.raises(AnsibleUndefinedVariable):
        test_conditional.evaluate_conditional(j2_template.new_context, dict(test_var='test_value'))

    test_conditional._when = [False]


# Generated at 2022-06-22 11:42:55.074993
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Initialize a Conditional object
    conditional = Conditional()

    # Initialize a Templar object
    templar = Templar(loader=DictDataLoader())

    # Check when is a list
    when = ['falsy', 'a == 1', True]
    when_evaluated = conditional.evaluate_conditional(templar, dict(a=1), when=when)
    assert when_evaluated is True

    # Check when is a string
    when = 'falsy'
    when_evaluated = conditional.evaluate_conditional(templar, dict(a=1), when=when)
    assert when_evaluated is False

    # Check when is not defined
    when = None
    when_evaluated = conditional.evaluate_conditional(templar, dict(a=1), when=when)
    assert when

# Generated at 2022-06-22 11:43:03.753226
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(dict(a=dict(b=dict(c='abc'))))

    conditional_class = type('ConditionalMixIn', (Conditional,), dict())
    c = conditional_class()

    c.when = ["a is not a", "a.b.c == 'abc'"]
    assert c.evaluate_conditional(variable_manager, variable_manager.get_vars())

    c.when = ["a is not a", "a.b.d == 'abc'"]
    assert not c.evaluate_conditional(variable_manager, variable_manager.get_vars())

# Generated at 2022-06-22 11:43:20.607543
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.template import Templar

    c = Conditional()
    assert c is not None
    assert isinstance(c, Conditional)
    assert isinstance(c, Templar)


# Generated at 2022-06-22 11:43:31.448905
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Test string containing valid conditional statement
    conditional_valid = '{{ ansible_distribution }} == "CentOS"'

    # Test string containing valid conditional statement
    conditional_valid_not = '{{ ansible_distribution }} != "CentOS"'

    # Test string containing invalid conditional statement
    conditional_invalid = '{{ ansible_distribution }} == CS'

    # Test string containing invalid expression in conditional statement
    conditional_invalid_expr = '{{ ansible_distribution }} == 1.0'

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-22 11:43:41.690848
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    class ConditionalTest(Conditional):
        def __init__(self, ds):
            self._ds = ds
            self.when = self._ds.get('when', [])

    ds = dict(
        when='1 > 0'
    )

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(
        foo='bar'
    )
    play_context = PlayContext()

    conditional = ConditionalTest(ds)
    templar = Templar(loader=None, variables=variable_manager, play_context=play_context)


# Generated at 2022-06-22 11:43:46.440967
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.conditional import Conditional
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    my_conditional = Conditional()
    data_loader = DataLoader()

    # First, set the vars of this conditional with methods extend, prepend and set
    my_conditional.set_when(["inventory_hostname == 'example1'", "inventory_hostname == 'example2'"])
    my_conditional.extend_when(["some_var is defined", "not some_var"])
    my_conditional.prepend_when("some_var is defined")

    # Create a VariableManager object
    variable_manager = VariableManager(loader=data_loader)

    # Set the inventory of this variable_manager
    variable_manager

# Generated at 2022-06-22 11:43:59.017072
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vault import VaultLib

    host_vars = HostVars(dict(foo='foovalue', bar='barvalue', baz='bazvalue'))
    play_context = PlayContext(vault_password=VaultLib()._create_vault_password())
    templar = Templar(loader=None, variables=dict(), host_vars=host_vars, play_context=play_context)
    c = Conditional(loader=None)


# Generated at 2022-06-22 11:44:01.101730
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    #TODO
    return None

# Generated at 2022-06-22 11:44:14.120371
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """
    Loader.
    """
    from ansible.plugins.loader import load_plugin_filters
    load_plugin_filters({'load_plugin_filters': []})

    from ansible.template import Templar

    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-22 11:44:24.817892
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.base import Base
    class Test(Base, Conditional):
        pass

    o = Test.load({'when': '1 == 1'})
    assert o.evaluate_conditional(o._templar, o._variable_manager.get_vars(loader=o._loader, play=o._play, host=o._host, task=o._task)) is True

    o = Test.load({'when': '2 == 3'})
    assert o.evaluate_conditional(o._templar, o._variable_manager.get_vars(loader=o._loader, play=o._play, host=o._host, task=o._task)) is False

# Generated at 2022-06-22 11:44:33.469835
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:44:39.362088
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    loader = None
    cond = Conditional(loader=loader)
    cond. when = [ 
        'True',
        '1 == 1',
        '2 == 2 and 3 == 3',
        '4 == 4 and 5 == 6'
    ]
    data = dict()
    templar = None

    # Test normal behavior
    assert cond.evaluate_conditional(templar, data) is False



# Generated at 2022-06-22 11:45:11.437195
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    conditional = 'ansible_os_family == "RedHat" or (ansible_facts.os_family == "RedHat" and ansible_distribution_major_version == "7")'
    expected_result = [('ansible_facts.os_family', '==', 'RedHat')]

    c = Conditional()
    assert c.extract_defined_undefined(conditional) == expected_result

# Generated at 2022-06-22 11:45:23.551046
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.six import StringIO
    from ansible.plugins.doc_fragments import DOCUMENTABLE_CONSTANTS

    from ansible.modules import EXAMPLES

    class FakeDS(object):
        def __init__(self):
            self._ds = None

        @property
        def ds(self):
            return self._ds

        @ds.setter
        def ds(self, value):
            self._ds = value

    class FakeConditional(Conditional, FakeDS):
        pass

    vars_manager = VariableManager()
    s_io = StringIO()

# Generated at 2022-06-22 11:45:34.526927
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    context = PlayContext()
    context.remote_addr = '127.0.0.1'
    context.accelerate = False
    context.network_os = None
    context.remote_user = 'root'
    context.connection = 'local'
    context.port = 22
    context.private_key_file = None
    context.verbosity = 1
    context.become

# Generated at 2022-06-22 11:45:45.123895
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Test evaluate_conditional method of class Conditional
    '''
    # Test not authorized lookups with (pre)defined variables
    # Allowed lookup : lookup('pipe', '/usr/bin/whoami')
    c = Conditional()

# Generated at 2022-06-22 11:45:46.220235
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()
    assert conditional

# Generated at 2022-06-22 11:45:57.336432
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Create dummy Conditional object
    class DummyConditional:
        def __init__(self, conditional):
            self.when = [conditional]
    conditional = DummyConditional('foo is not defined and (bar is defined or not baz) and (qux is something and bla is missing)')

    # Assert on result
    assert conditional.extract_defined_undefined(conditional.when[0]) == [
        ('foo', 'is not', 'defined'),
        ('bar', 'is', 'defined'),
        ('baz', 'is', 'undefined'),
        ('qux', 'is', 'something'),
        ('bla', 'is', 'missing'),
    ]


# Generated at 2022-06-22 11:46:09.703260
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import pytest

    vars_mgr = VariableManager()
    templar = Templar(vars_mgr)

    all_vars = dict(
        hostvars=dict(
            host0=dict(
                a_var = "a",
                a_dict = dict(
                    a_key0 = "a0",
                    a_key1 = "a1"
                ),
                a_list = [ "list_a", "list_b"]

            ),
            host1=dict(
                b_var = "b",
            )
        )
    )

    conditional_obj = Conditional(loader=None)

    ####################################################################################################################
    # Numeric comparisons
    ####################################################################################################################

   

# Generated at 2022-06-22 11:46:21.794952
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:46:27.299101
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.parsing.dataloader import DataLoader
    c = Conditional(loader=DataLoader())
    assert c._when == [], "_when is not empty"
    assert c._loader, "loader is not set"


# Generated at 2022-06-22 11:46:38.631049
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    host = inventory.get_host('localhost')
    variable_manager.set_host_variable(host, 'ansible_user', 'vagrant')
    variable_manager.set_host_variable(host, 'ansible_password', 'vagrant')
    variable_manager.set_host_variable(host, 'ansible_port', '22')
    variable_manager.set_host_variable(host, 'ansible_connection', 'ssh')

# Generated at 2022-06-22 11:47:42.050862
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    """
    The method extract_defined_undefined(self, conditional) of class Conditional
         extracts the defined/undefined conditions of the given conditional string.
    """
    # In the following test case, we have five parts:
    # 1. the given conditional string
    # 2. the expected result (list of tuples)
    # 3. the setup code
    # 4. the call to extract_defined_undefined()
    # 5. the asserts (the expected result is compared with the returned result)

    # given: a conditional string containing one defined/undefined condition
    #        (conditional and the expected result is copied from github.com/ansible/ansible/blob/devel/test/units/modules/test_ansible_module.py)
    cond = 'foo is defined and (bar is defined or not baz is defined)'
   

# Generated at 2022-06-22 11:47:47.413183
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager

    vars_manager = VariableManager()
    from ansible.template import Templar

    templar = Templar(vars_manager, loader=None)

    cond = Conditional()
    cond._ds = 'dummy'
    cond.when = ['1 == 1']

    print(cond.evaluate_conditional(templar, {}))

# Generated at 2022-06-22 11:47:55.949083
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class MyPlaybook:
        when = ["a and b or c"]

    m = MyPlaybook()
    assert(m.evaluate_conditional({"a": True, "b": True, "c": True}) == True)
    assert(m.evaluate_conditional({"a": True, "b": True, "c": False}) == True)
    assert(m.evaluate_conditional({"a": True, "b": False, "c": False}) == False)
    assert(m.evaluate_conditional({"a": False, "b": False, "c": False}) == False)

# Generated at 2022-06-22 11:48:07.177626
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert 'def_undef' in globals()
    assert def_undef.extract_defined_undefined('foo is defined') == [('foo', 'is', 'defined')]
    assert def_undef.extract_defined_undefined('foo is not defined') == [('foo', 'is not', 'defined')]
    assert def_undef.extract_defined_undefined('foo is undefined') == [('foo', 'is', 'undefined')]
    assert def_undef.extract_defined_undefined('foo is not undefined') == [('foo', 'is not', 'undefined')]
    assert def_undef.extract_defined_undefined('hostvars["foo"] is defined') == [('hostvars["foo"]', 'is', 'defined')]
    assert def_undef.extract_

# Generated at 2022-06-22 11:48:18.223702
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    """
    Ensure that defined/undefined variables are correctly extracted
    from a conditional
    """

    mock_cond = Conditional()

# Generated at 2022-06-22 11:48:30.817049
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def assert_extract_defined_undefined(conditional, expected_result):
        actual_result = Conditional.extract_defined_undefined(Conditional(), conditional)
        assert actual_result == expected_result, "Expected result of extract_defined_undefined to be %s but was %s" % (expected_result, actual_result)

    assert_extract_defined_undefined(conditional="a.b.c is defined", expected_result=[("a.b.c", "is", "defined")])
    assert_extract_defined_undefined(conditional="a.b.c is not defined", expected_result=[("a.b.c", "is not", "defined")])

# Generated at 2022-06-22 11:48:41.736965
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    test_data = [
        ('1 < 2', True),
        ('1 == 2', False),
        ('false | bool', False),
        ('true | bool', True),
        ('1 < 2 and 1 == 2', False),
        ('(1 < 2 and 1 == 2) or 1 == 1', True),
    ]

    test_obj = Conditional(loader=None)
    for (test_cond, test_result) in test_data:
        test_obj._when = [test_cond]

        result = test_obj.evaluate_conditional(templar=None, all_vars={})

# Generated at 2022-06-22 11:48:53.455913
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Unit test for Conditional.evaluate_conditional
    '''

    class MockTemplar:
        def __init__(self):
            pass

        def is_template(self, data):
            return False

        def template(self, data, disable_lookups=False):
            return data

        def environment(self):
            return None

    class MockModule:
        def __init__(self, args={}):
            args = dict(args)
            for (k, v) in args.items():
                setattr(self, k, v)

    t = MockTemplar()

# Generated at 2022-06-22 11:49:06.166422
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:49:18.096131
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Define test variables
    dict1 = dict(a='a')
    dict2 = dict(b='b')
    dict_all_vars = dict(dict1, **dict2)
    valid_vars = [name for name in dict_all_vars.keys() if VALID_VAR_REGEX.match(name)]
    dict_all_vars['valid_vars'] = valid_vars
    dict_all_vars['hostvars'] = dict(dict1=dict1, dict2=dict2)
    dict_all_vars['valid_keys'] = ['a', 'b']
    dict_all_vars['valid_conditional_list'] = [
        'a', 'b', 'valid_vars', 'valid_keys', 'hostvars'
    ]
    dict_all_