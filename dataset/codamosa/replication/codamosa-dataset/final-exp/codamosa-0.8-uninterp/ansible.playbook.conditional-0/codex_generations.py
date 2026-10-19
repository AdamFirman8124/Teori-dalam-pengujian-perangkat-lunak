

# Generated at 2022-06-22 11:40:25.508064
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    # test the single not is undefined
    test = conditional.extract_defined_undefined("var is not undefined")
    assert test[0][1:] == ('is', 'undefined')
    assert test[0][0] == "var"
    # test the single is not defined
    test = conditional.extract_defined_undefined("var is not defined")
    assert test[0][1:] == ('is', 'defined')
    assert test[0][0] == "var"
    # test the single is defined
    test = conditional.extract_defined_undefined("var is defined")
    assert test[0][1:] == ('is', 'defined')
    assert test[0][0] == "var"
    # test the single is undefined

# Generated at 2022-06-22 11:40:36.810076
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play import Play
    from ansible.template import Templar

    hosts = [
        'testhost',
        'testhost0',
        'testhost1',
        'testhost2',
        'testhost3',
        'testhost4',
        'testhost5'
    ]

    play_source = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='ping', args=''))
        ]
    )

    play = Play().load(play_source, variable_manager={}, loader=None)
    print("Loaded play")

    templar = Templar(loader=None)


# Generated at 2022-06-22 11:40:46.163004
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # the yaml parser & templar cannot be used here because they depend on self.evaluate_conditional
    # see _t_load_yaml_from_file/_t_templar_process in test/unit/loader/test_loader.py
    # and _load_attr_from_yaml in test/unit/utils/test_module_utils.py
    # see _t_templar_process in test/unit/playbook/test_playbook.py
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import os.path
    import sys
    import ansible.module_utils.six

    class FakePlayContext:
        def __init__(self):
            self.prompt

# Generated at 2022-06-22 11:40:52.996798
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    class AuxConditional(Conditional):
        def __init__(self):
            super(AuxConditional,self).__init__()

    aux = AuxConditional()
    loader = DataLoader()
    inventory = InventoryManager(loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-22 11:41:03.720193
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook import Play
    from ansible.template import Templar

    verbose = False

    # create a new play to ensure we have a task instance that is correct
    my_play = Play().load({}, loader=None, variable_manager=None)

    my_vars = {
        'foo': 'bar',
        'baz': 'bat',
        'flibble': 'wibble'
    }

    my_conditional = Conditional()

    # we have a nice templar instance that we can use to test this
    my_templar = Templar(loader=None, variables=my_vars)

    my_conditional.when = [ ]

    assert my_conditional.evaluate_conditional(my_templar, my_vars) is True


# Generated at 2022-06-22 11:41:17.234564
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined("a is defined") == [('a', 'is', 'defined')]
    assert c.extract_defined_undefined("a is not undefined") == [('a', 'is not', 'undefined')]
    assert c.extract_defined_undefined("a is defined and b is defined") == [('a', 'is', 'defined'), ('b', 'is', 'defined')]
    assert c.extract_defined_undefined("a is defined and b is not undefined") == [('a', 'is', 'defined'), ('b', 'is not', 'undefined')]

# Generated at 2022-06-22 11:41:29.686999
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader

    # create a Subclass of class namedtuple
    FakeHostVars = namedtuple('HostVars', ['hostname', 'test_property'])
    # create some hostvars
    hostvars = [FakeHostVars('host1', 'a'), FakeHostVars('host2', 'b')]
    # create a dict of all variables available to the execution of the task
    all_vars = dict([(hostvars[i].hostname, {'test_property': hostvars[i].test_property}) for i in range(len(hostvars))])

    # create a basic task for testing

# Generated at 2022-06-22 11:41:38.040312
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.task_include import TaskInclude

# Generated at 2022-06-22 11:41:50.640323
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined('hostvars[inventory_hostname]') == \
        [('hostvars[inventory_hostname]', 'is', 'defined')]
    assert conditional.extract_defined_undefined('hostvars["inventory_hostname"]') == \
        [('hostvars["inventory_hostname"]', 'is', 'defined')]
    assert conditional.extract_defined_undefined('foo is not defined') == \
        [('foo', 'is not', 'defined')]
    assert conditional.extract_defined_undefined('foo is undefined') == \
        [('foo', 'is', 'undefined')]

# Generated at 2022-06-22 11:42:02.614367
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    This method tests that extract_defined_undefined returns the values
    for defined and undefined tests correctly.
    '''
    from ansible.playbook.base import Base

    class TestConditional(Conditional, Base):
        pass

    test_obj = TestConditional()

    strings_list = [
        "a is defined and b is undefined",
        "a is not defined and b is undefined or c is defined",
        "a.b is not defined and b.c is undefined or c.d is not defined",
        "a.b is not defined and b.c is defined or c.d is undefined",
        "a.b is defined and b.c is undefined or c.d is not defined",
    ]


# Generated at 2022-06-22 11:42:18.799845
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar
    import jinja2
    from jinja2.exceptions import UndefinedError

    j2_env = jinja2.Environment()
    j2_env.filters['quote'] = str
    templar = Templar(loader=None, variables=[], shared_loader_obj=None, environment=j2_env)

    cond = Conditional()
    cond._ds = dict()

    # in this test, the Conditional class is not used as a mix-in, we are testing its
    # evaluate_conditional method directly
    assert cond.evaluate_conditional(templar, dict())

    # here we start testing the various features that affect the result of the conditional
    assert not cond.evaluate_conditional(templar, dict(x=None))

# Generated at 2022-06-22 11:42:23.641919
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display = Display()
    display.verbosity = 0
    args = {'ignore_errors': False,
            'become': False,
            'become_user': '',
            'check_mode': False,
            'diff': False,
            'start_at_task': u''}

    from ansible.parsing.dataloader import DataLoader

    # hack because we are testing without a play context
    def get_basedir(*args, **kwargs):
        return '/'

    from ansible.vars import VariableManager, HostVars

    variable_manager = VariableManager()
    loader = DataLoader()

    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=loader, sources='localhost,')

    variable_manager.set_inventory(inventory)

    variable_manager.extra_v

# Generated at 2022-06-22 11:42:34.428767
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

    assert conditional.extract_defined_undefined(None) == []
    assert conditional.extract_defined_undefined('') == []
    assert conditional.extract_defined_undefined('device.vendor is defined') == []
    assert conditional.extract_defined_undefined('device.vendor is undefined') == []
    assert conditional.extract_defined_undefined('device.vendor isnot defined') == []
    assert conditional.extract_defined_undefined('device.vendor isnot undefined') == []
    assert conditional.extract_defined_undefined('device.vendor not is defined') == []
    assert conditional.extract_defined_undefined('device.vendor not is undefined') == []

# Generated at 2022-06-22 11:42:39.224464
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestClass(Conditional):
        def __init__(self):
            pass
    testClass = TestClass()
    # TODO: unit test for evaluate_conditional
    

# Generated at 2022-06-22 11:42:50.628915
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:43:02.833023
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    p = Conditional()
    s = 'hostvars[inventory_hostname] is not defined'
    assert p.extract_defined_undefined(s) == [('hostvars[inventory_hostname]', 'is not', 'defined')]
    s = 'hostvars[inventory_hostname] is not defined and a is defined or b is undefined'
    assert p.extract_defined_undefined(s) == [('hostvars[inventory_hostname]', 'is not', 'defined'),
                                               ('a', 'is', 'defined'),
                                               ('b', 'is', 'undefined')]
    s = 'hostvars[inventory_hostname] is defined'

# Generated at 2022-06-22 11:43:08.318256
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    result = c.extract_defined_undefined('a is defined and b not is undefined and c is defined')
    assert result == [('a', 'is', 'defined'), ('b', 'not is', 'undefined'), ('c', 'is', 'defined')]



# Generated at 2022-06-22 11:43:20.310852
# Unit test for constructor of class Conditional
def test_Conditional():
    """
    Returns True on Success,
    Returns False on failure,
    """
    from ansible.playbook.base import Base
    from jinja2.exceptions import TemplateSyntaxError, UndefinedError
    from ansible.vars import VariableManager, HostVars
    from ansible.inventory.host import Host
    from ansible.utils.boolean import boolean
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    import yaml
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory('localhost'))

    class Task(Base, Conditional):
        pass

    class Play(Base, Conditional):
        pass

    task = Task()
    play = Play()
    variable_manager.set

# Generated at 2022-06-22 11:43:31.207196
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    assert not Conditional().evaluate_conditional(None, None)

    class MyConditional(Conditional):
        def __init__(self, when=None, ds=None):
            self._when = when
            self._ds = ds

    assert MyConditional(when=[]).evaluate_conditional(None, None)
    assert MyConditional(when=None).evaluate_conditional(None, None)
    assert MyConditional(when=False).evaluate_conditional(None, None)
    assert not MyConditional(when=True).evaluate_conditional(None, None)

    assert MyConditional(when=[None, None]).evaluate_conditional(None, None)
    assert MyConditional(when=[None, False]).evaluate_conditional(None, None)
    assert not MyConditional(when=[None, True]).evaluate_

# Generated at 2022-06-22 11:43:41.657292
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.module_utils.six import PY3
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    class TestHostVars(HostVars):
        def __init__(self):
            self.vars = dict()
        def get(self, item, *args, **kwargs):
            if item.startswith("__"):
                raise LookupError("Invalid access to: %s" % item)
            if item in self.vars:
                return self.vars.get(item)
            else:
                return None

    class TestTemplar(Templar):
        def __init__(self):
            self.environment = None
            self.vars = Test

# Generated at 2022-06-22 11:44:04.261561
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    Test extract_defined_undefined method for cases:
    1) string doesn't contain defined/undefined markers
    2) string contains defined/undefined markers
    '''
    test_conditional = Conditional()

    # test 1 string doesn't contain defined/undefined markers
    conditional = "1 == 1"
    result = test_conditional.extract_defined_undefined(conditional)
    assert result == []

    # test 2 string contain defined/undefined markers
    conditional = "1 == 1 or undefined_var is undefined or defined_var is defined or wrong_var is wrong_state"
    result = test_conditional.extract_defined_undefined(conditional)
    assert result == [('undefined_var', 'is', 'undefined'), ('defined_var', 'is', 'defined')]


# Unit

# Generated at 2022-06-22 11:44:15.945137
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    # Set up a fake display class for testing
    class DisplayTest(Display):
        def __init__(self):
            self.messages = []

        def warning(self, msg):
            self.messages.append(msg)

        def display(self, msg):
            pass
        def vvv(self, msg):
            pass

    display = DisplayTest()

    # Set up a fake templar class for testing
    class TemplarTest(Templar):
        def __init__(self):
            self.available_variables = {}

        def template(self, template, **kwargs):
            return template

    # Set up

# Generated at 2022-06-22 11:44:23.193940
# Unit test for constructor of class Conditional
def test_Conditional():
    # constructor with no loader
    conditional = Conditional()
    assert conditional._loader is None
    # make sure that an error is thrown when the loader is not set
    try:
        conditional.evaluate_conditional(None, None)
        assert 0, "An error was expected"
    except AnsibleError:
        pass

    # constructor with loader
    loader = "loader"
    conditional = Conditional(loader)
    assert conditional._loader == loader

# Generated at 2022-06-22 11:44:32.584685
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    def _fake_all_vars():
        return dict(
            x=dict(y=1),
            z=dict(a=dict(b=dict(c=1)))
        )

    # check that it works with no conditional as well
    assert Conditional().evaluate_conditional(None, _fake_all_vars())


# Generated at 2022-06-22 11:44:44.008900
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

    # Basic checks
    assert conditional.extract_defined_undefined("") == []
    assert conditional.extract_defined_undefined("a_var is defined") == [('a_var', 'is', 'defined')]
    assert conditional.extract_defined_undefined("a_var is not defined") == [('a_var', 'is not', 'defined')]
    assert conditional.extract_defined_undefined("a_var is undefined") == [('a_var', 'is', 'undefined')]
    assert conditional.extract_defined_undefined("a_var is not undefined") == [('a_var', 'is not', 'undefined')]

# Generated at 2022-06-22 11:44:54.654752
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # Create a test Conditional object
    conditional = Conditional()

    # Create a test template to pass in
    class FakeTemplar():
        def __init__(self):
            pass
        def template(self, template, *args, **kwargs):
            return template
        def is_template(self, template):
            return False

    templar = FakeTemplar()

    ansible_vars = dict()

    # Test basic (boolean) evaluation
    assert conditional.evaluate_conditional(templar, ansible_vars)
    conditional.when = [False]
    assert not conditional.evaluate_conditional(templar, ansible_vars)

    # Test basic evaluation with string conditional
    conditional.when = ["THIS_SHOULD_EVALUATE_TO_TRUE"]
    assert conditional.evaluate_

# Generated at 2022-06-22 11:44:58.987217
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = "string1 is defined and string2 is defined and string3"
    result = Conditional().extract_defined_undefined(conditional)
    assert result == [('string1', 'is', 'defined'), ('string2', 'is', 'defined')]



# Generated at 2022-06-22 11:45:09.025070
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    def _test_conditional(conditional, vars, expect):
        self = Conditional()
        self.when = [conditional]

        # a simple templar localization test, nothing fancy
        templar = MagicMock(spec=AnsibleTemplar)
        templar.is_template = MagicMock(return_value=False)
        templar.template = MagicMock(return_value=conditional)

        res = self.evaluate_conditional(templar, vars)
        assert res == expect, 'Failed to evaluate conditional: %s' % conditional

    vars = dict(a=1, b=2, c=3)
    _test_conditional('a == 1 and b == 2 and c == 3', vars, True)

# Generated at 2022-06-22 11:45:20.199835
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # Initialize the Conditional object
    obj = Conditional(loader=None)

    # Define test strings
    str1 = ''
    str2 = 'hostvars[inventory_hostname] == inventory_hostname'
    str3 = 'hostvars["foo_bar"] == inventory_hostname'
    str4 = 'hostvars[inventory_hostname] == "foo_bar"'
    str5 = 'hostvars[inventory_hostname] is not defined'

    # Test evaluate_conditional
    is_conditional_true = obj._check_conditional(str1, "templar", "all_vars")
    assert is_conditional_true == True

    is_conditional_true = obj._check_conditional(str2, "templar", "all_vars")
    assert is_conditional

# Generated at 2022-06-22 11:45:32.246740
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.playbook.base import Base
    from ansible.vars.hostvars import HostVars

    class MyTask(Conditional, Base):
        pass

    # used to generate a hostvars variable structure
    class Host:
        def __init__(self, name):
            self.name = name

# Generated at 2022-06-22 11:46:09.498078
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

    # check if empty list is returned
    assert conditional.extract_defined_undefined('') == []

    # check if only defined variables are returned
    assert conditional.extract_defined_undefined('defined variable') == [('variable', '', 'defined')]
    assert conditional.extract_defined_undefined('variable is defined') == [('variable', 'is', 'defined')]
    assert conditional.extract_defined_undefined('variable is not defined') == [('variable', 'is not', 'defined')]

    # check if only undefined variables are returned
    assert conditional.extract_defined_undefined('undefined variable') == [('variable', '', 'undefined')]
    assert conditional.extract_defined_undefined('variable is undefined') == [('variable', 'is', 'undefined')]


# Generated at 2022-06-22 11:46:21.590872
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Test that extract_defined_undefined returns expected result
    conditional = Conditional()
    result = conditional.extract_defined_undefined("a is defined and b is not undefined")
    assert len(result) == 2
    assert result[0] == ("a", "is", "defined")
    assert result[1] == ("b", "is not", "undefined")

    result = conditional.extract_defined_undefined("hostvars['foo'] is undefined and 'bar' is defined")
    assert len(result) == 2
    assert result[0] == ("hostvars['foo']", "is", "undefined")
    assert result[1] == ("'bar'", "is", "defined")

    result = conditional.extract_defined_undefined("a is defined and b is defined and c is undefined")

# Generated at 2022-06-22 11:46:30.683537
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play().load(dict(
        name="Test Play",
        hosts="all",
        gather_facts="no",
        tasks=[
            dict(
                name="Test Task",
                some_var=dict(
                    foo="bar"
                ),
                another_var="baz",
                some_undef_var="{{ some_undef_var }}"
            )
        ]
    ), loader=loader, variable_manager=variable_manager)


# Generated at 2022-06-22 11:46:42.192877
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.playbook import Playbook

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = {}

    temp = Templar(loader=loader, variables=variable_manager, play_context=play_context)
    conditional = Conditional(loader=loader)

    ######################################################
    # Test evaluate_conditional with valid conditions
    ######################################################

    # Test evaluate_conditional with no conditional
    conditional.when = None
    assert conditional.evaluate_conditional(temp, {})

    # Test evaluate_conditional with empty conditional
    conditional.when = ""
    assert conditional

# Generated at 2022-06-22 11:46:51.196681
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    # This helper function is used by the unit test below to simulate the existence
    # of key-value pairs in Ansible dict 
    def _add_var(var_name, var_value):
        setattr(current_play, '_ds', dict())
        setattr(current_play._ds, '__UNSAFE__', True)
        setattr(current_play._ds, var_name, var_value)

    # Testing of conditionals not templated
    def test_not_templated(cond, exp_res):
        try:
            res = current_play.evaluate_conditional(templar, all_vars)
            assert res == exp_res
        except Exception as e:
            assert False, e

# Generated at 2022-06-22 11:47:00.823702
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    Returns a Conditional object that can be used in tests.
    '''
    from ansible.template import Templar
    from ansible import variables
    from ansible.parsing.yaml.objects import AnsibleUnicode


# Generated at 2022-06-22 11:47:06.824030
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    class TestConditional(Conditional):
        def __init__(self):
            pass
    t = TestConditional()

    r = t.extract_defined_undefined('hostvars[inventory_hostname] is defined')
    assert r == [('hostvars[inventory_hostname]', 'is', 'defined')]
    r = t.extract_defined_undefined('(hostvars[inventory_hostname] is defined)')
    assert r == [('hostvars[inventory_hostname]', 'is', 'defined')]
    r = t.extract_defined_undefined('not ( hostvars[inventory_hostname] is defined )')
    assert r == [('hostvars[inventory_hostname]', 'is', 'defined')]

# Generated at 2022-06-22 11:47:19.940761
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    conditional = Conditional()

    play_context = PlayContext()
    play_context._hostvars = HostVars(play_context)

    templar = Templar(loader=None, variables={}, shared_loader_obj=None,
                      loader_basedir={}, play_context=play_context)

    # define the variables for the conditional check
    all_vars = dict(test1=True, test2=True, test3=True)

    # test the empty condition
    assert conditional.evaluate_conditional(templar, all_vars) is True

    # since all the conditions are evaluated, only the last should be true

# Generated at 2022-06-22 11:47:31.005034
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

# Generated at 2022-06-22 11:47:43.488328
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    variable_str1 = 'a1 is defined'
    variable_str2 = 'a2 is not defined'
    variable_str3 = 'a3 is undefined'
    variable_str4 = 'a4 is not undefined'
    variable_str5 = 'hostvars["hostname"] is defined'
    variable_str6 = 'hostvars["hostname"] is not defined'
    variable_str7 = 'hostvars["hostname"] is undefined'
    variable_str8 = 'hostvars["hostname"] is not undefined'

    conditionals = [variable_str1, variable_str2, variable_str3, variable_str4, variable_str5, variable_str6, variable_str7, variable_str8]

    # create a Conditional class object
    conditional = Conditional()


# Generated at 2022-06-22 11:48:34.832043
# Unit test for constructor of class Conditional
def test_Conditional():
    module = Conditional()
    assert module is not None

# Generated at 2022-06-22 11:48:47.233807
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """
    Test for method evaluate_conditional of class Conditional
    """
    from ansible.template.safe_eval import safe_eval, ERROR_CLASSES

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    display.verbosity = 3

    class SampleClass(object):
        pass

    all_vars = dict(
        a=1,
        b=2,
        c=dict(
            d=dict(
                e=5,
            )
        ),
        f=dict(
            g=8,
        ),
    )

    sc = SampleClass()
    sc.conditional = Conditional()


# Generated at 2022-06-22 11:48:57.263804
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.base import Base

    class ConditionalObject(Conditional, Base):
        def __init__(self, when_str=None, hostvars=None, facts=None):
            self.when = [when_str]
            self._ds = None
            self._loader = None
            self._hostvars = hostvars or dict()
            self._fact_cache = facts or dict()

    # TODO
    # Write unit tests for the evaluate conditional method and add them
    # to this function
    # Method to test
    # - test 1: no conditional (should return True)
    # - test 2: conditional is a string that evaluates to a boolean (should return True)
    # - test 3: conditional is a string that evaluates to True (should return True)
    # - test 4: conditional is a string that evaluates to

# Generated at 2022-06-22 11:49:08.652656
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class DummyClass(Conditional):
        def __init__(self, loader=None):
            super(DummyClass, self).__init__(loader=loader)

    # use private function since we don't have a templar instance to use
    def _evaluate_conditional(conditional='', extra_vars={}, fail_on_undefined=False):
        loader = DummyMockLoader()
        dc = DummyClass(loader=loader)
        dc.when = [conditional]
        return dc._check_conditional(conditional, loader._templar, extra_vars)


# Generated at 2022-06-22 11:49:21.150502
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    module_loader = 'ansible.parsing.dataloader.DataLoader'
    variable_manager = 'ansible.vars.manager.VariableManager'
    loader = 'ansible.playbook.play_context.PlayContext'
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(loader.load_inventory('localhost'))
    variable_manager.set_loader(loader)
    variable_manager._extra_vars = dict(local_var=dict(a=1, b=2))
    play_context = PlayContext()
    play_context.network

# Generated at 2022-06-22 11:49:32.707008
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    m = Conditional()
    assert m.evaluate_conditional(None, {}) is True
    m = Conditional(None)
    assert m.evaluate_conditional(None, {}) is True
    m._ds = {}
    assert m.evaluate_conditional(None, {}) is True
    m._when = 'a'
    assert m.evaluate_conditional(None, {}) is True
    m._when = 'b'
    assert m.evaluate_conditional(None, {'b': 1}) is True
    m._when = 'c'
    assert m.evaluate_conditional(None, {'c': None}) is True
    m._when = 'd'
    assert m.evaluate_conditional(None, {'d': ''}) is True
    m._when = 'e'
    assert m.evaluate_cond

# Generated at 2022-06-22 11:49:43.148289
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Create mock templar
    class MockTemplar:
        def is_template(self, value):
            # This is a very simple implementation, it is called only for tests 1 to 6
            return False

        def template(self, value, **kwargs):
            if value == 'my_hostname':
                return 'host1'
            elif value == 'host1':
                return 'host1'
            elif value == 'my_hostname2':
                return 'host2'
            elif value == 'hostvars[my_hostname]':
                return ''
            elif value == 'hostvars[host1]':
                return ''
            elif value == 'hostvars[my_hostname2]':
                return 'a'
            elif value == 'hostvars[host2]':
                return

# Generated at 2022-06-22 11:49:54.798631
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    class TestRole:
        def __init__(self):
            self.task_vars = {}

    class TestTask:
        def __init__(self):
            self.role = TestRole()
            self.when = []
            self.loader = DataLoader()

    class TestPlayContext:
        def __init__(self):
            self.hostvars = {}

    play_context = TestPlayContext()
    task = TestTask()

    play = Play()
    play._loader = DataLoader()
    play.hosts = 'all'

    templar = play._get_templar(play=play)


# Generated at 2022-06-22 11:50:06.708404
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    def check(input, output):
        c = Conditional()
        assert c.extract_defined_undefined(input) == output

    check("'some_string' not in string_var and int_var > 2 and (other_var is defined or var_2 is undefined)", [('var_2', 'is', 'undefined')])
    check("(some_var is not defined or (some_var == False and another_var is defined))", [('some_var', 'is', 'not defined'), ('another_var', 'is', 'defined')])
    check("(var_1 is defined and var_2 is not defined) and some_string in string_var and int_var > 2", [('var_1', 'is', 'defined'), ('var_2', 'is', 'not defined')])