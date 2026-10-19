

# Generated at 2022-06-22 11:40:27.341732
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    # Pass empty dict so we know it is empty
    all_vars = {}

    # Tests that `when` set to `False` always returns false
    conditional = Conditional()
    conditional.when = False
    res = conditional.evaluate_conditional(play_context.templar, all_vars)
    assert res is False

    # Tests that `when` set to `True` always returns true
    conditional.when = True
    res = conditional.evaluate_conditional(play_context.templar, all_vars)
    assert res is True

    # Tests that `when` set to `None` always returns true
    conditional.when = None

# Generated at 2022-06-22 11:40:37.915912
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """Test if evaluate_conditional returns correct True or False by checking
    conditional statements with different logic operators.
    """
    C.DEFAULT_MODULE_NAME = 'command'
    class TestTask(Conditional):
        def __init__(self):
            self._ds = 'tasks/foo.yaml'
            self._loader = DictDataLoader(dict())
        def get_ds(self):
            return self._ds
    task = TestTask()
    # No variable was defined in the test variable
    local_vars = dict()
    # Set some variables in the fact cache

# Generated at 2022-06-22 11:40:47.933110
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """test_Conditional_evaluate_conditional

    Test the evaluate_conditional method of the Conditional class.

    Note: the test is not structural, but is based on the results.
    """
    from ansible.playbook.play_context import PlayContext
    # set the play context for shared variables
    play_context = PlayContext()
    play_context.CLIARGS = {'tags': [None, []], 'skip_tags': [None, []],
                            'check': False, 'syntax': False}
    templar = C.aliases.get('template')


# Generated at 2022-06-22 11:41:00.455546
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()
    pc.CLIARGS = {}
    pc.CLIARGS['forks'] = 10
    pc.CLIARGS['ask_pass'] = False
    pc.CLIARGS['ask_sudo_pass'] = False
    pc.CLIARGS['ask_su_pass'] = False
    pc.CLIARGS['ask_vault_pass'] = False
    pc.CLIARGS['vault_password_file'] = ''
    pc.CLIARGS['new_vault_password_file'] = ''
    pc.CLIARGS['vault_password'] = None
    pc.CLIARGS['timeout'] = 60
    pc.CLIARGS['remote_port'] = None
    pc.CL

# Generated at 2022-06-22 11:41:14.099682
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    match_list = conditional.extract_defined_undefined("test_testi is defined")
    assert match_list == [('test_testi', 'is', 'defined')]
    match_list = conditional.extract_defined_undefined("test_testi is not defined")
    assert match_list == [('test_testi', 'is not', 'defined')]
    match_list = conditional.extract_defined_undefined("test_testi is undefined")
    assert match_list == [('test_testi', 'is', 'undefined')]
    match_list = conditional.extract_defined_undefined("test_testi is not undefined")
    assert match_list == [('test_testi', 'is not', 'undefined')]
    match_list = conditional.extract_

# Generated at 2022-06-22 11:41:24.486586
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    conditional1 = "some | random | string"
    expected1 = []
    conditional2 = "my_var is defined"
    expected2 = [('my_var', 'is', 'defined')]
    conditional3 = "my_var is undefined or another_var is defined"
    expected3 = [('my_var', 'is', 'undefined'), ('another_var', 'is', 'defined')]
    conditional4 = "hostvars['some_host'] is defined and (hostvars['some_host']|default({})).get('some_var')|d([])" \
                   "|length > 0"
    expected4 = [('hostvars[\'some_host\']', 'is', 'defined')]

# Generated at 2022-06-22 11:41:36.765322
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()
    pc.variable_manager.set_extra_vars({
        'foo': 'bar',
        'baz': True,
        'blippy': False,
        'wibble': 123,
        'empty': '',
        'nope': None,
        'listofstuff': ['foo', 'bar', 'baz'],
    })
    c = Conditional()

    def _assert_cond(expected, conditional):
        actual = c.evaluate_conditional(pc.templar, pc.available_variables)
        assert actual == expected, "%s:  (cond: %s) == %s" % (conditional, expected, actual)


# Generated at 2022-06-22 11:41:49.379833
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Options(object):
        def __init__(self):
            self.force_color = False
            self.host_key_checking = False
            self.syntax = False
            self.connection = 'local'
            self.remote_user = 'remote_user'
            self.private_key_file = 'test/file/path'
            self.ssh_common_args = ''
            self.sftp_extra_args = ''
            self.scp_extra_args = ''
            self.ssh_extra_args = ''
            self.verbosity = 0
            self.check = False
            self.listhosts = False
            self.listtasks = False
            self.listtags = False
            self.module_paths = None
            self.tree = None
            self.playbook_paths = None


# Generated at 2022-06-22 11:41:56.509954
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    """This test does a basic smoke test to ensure the evaluate_conditional method
    returns expected results. The resulting code (or change in the code) may be
    adjusted to the needs of better testing of the method.
    """

    class MyConditional(Conditional):

        def __init__(self):
            super(MyConditional, self).__init__()

        def evaluate_conditional(self, templar, all_vars):
            return super(MyConditional, self).evaluate_conditional(templar, all_vars)

    cond = MyConditional()

    # Test the scenario when the conditional value is None
    cond.when = [None]
    result = cond.evaluate_conditional(None, None)
    assert (result is True)

    # Test the scenario when the conditional value is empty string

# Generated at 2022-06-22 11:42:00.337266
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()

    # _when = FieldAttribute(isa='list', default=list)
    assert conditional._when == []

    # Conditional() default loader is None
    assert conditional._loader is None

# Generated at 2022-06-22 11:42:15.129781
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    results = dict(
        skipped = [],
        failed = [],
        ok = [],
    )


# Generated at 2022-06-22 11:42:26.782703
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:42:35.890768
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()

# Generated at 2022-06-22 11:42:49.541425
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
   c = Conditional()

# Generated at 2022-06-22 11:43:02.081881
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestModule(Conditional):
        pass

    task = TestModule()
    task.when = ['foo', 'bar']
    task_vars = dict(foo='foo', bar='bar', baz='baz')
    templar = DummyVarsTemplate(task_vars)
    assert task.evaluate_conditional(templar, task_vars)

    task = TestModule()
    task.when = ['foo', 'bar', 'baz']
    task_vars = dict(foo='foo', bar='bar')
    templar = DummyVarsTemplate(task_vars)
    assert not task.evaluate_conditional(templar, task_vars)

    task = TestModule()
    task.when = ['foo', 'bar', 'foo and bar']

# Generated at 2022-06-22 11:43:13.614739
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def assert_result(cond, expected):
        c = Conditional()
        actual = c.extract_defined_undefined(cond)
        assert actual == expected, 'cond=%s, actual=%s' % (cond, actual)

    assert_result('a is defined', [('a', 'is', 'defined')])
    assert_result('a is not defined', [('a', 'is not', 'defined')])
    assert_result('a is not defined or a is defined', [('a', 'is not', 'defined'), ('a', 'is', 'defined')])
    assert_result('a is not defined or b is defined', [('a', 'is not', 'defined'), ('b', 'is', 'defined')])

# Generated at 2022-06-22 11:43:25.500196
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()

# Generated at 2022-06-22 11:43:37.565984
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from . import StrategyModule, DataLoader

    loader = DataLoader()
    t = StrategyModule(play=None, new_stdin='some_input_data')
    fake_vars = dict(test_var='test_value')

    # test that evaluate_conditional ignores non-truthy when's'
    assert t.evaluate_conditional(templar=t, all_vars=fake_vars, when=None)
    assert t.evaluate_conditional(templar=t, all_vars=fake_vars, when=False)
    assert t.evaluate_conditional(templar=t, all_vars=fake_vars, when=0)
    assert t.evaluate_conditional(templar=t, all_vars=fake_vars, when='')
    assert t.evaluate_

# Generated at 2022-06-22 11:43:42.136936
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    ''' test cases for method evaluate_condition of class Conditional'''
    display.verbosity = 3
    class DummyTask(Conditional):
        def __init__(self, loader=None):
            self._loader = loader
    all_vars = {'var1': 'string value', 'var2': 1, 'var3': False, 'var4': ['var1', 'var2', 'var3'] }

# Generated at 2022-06-22 11:43:53.909738
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    # simple valid tests
    s = 'hostvars[inventory_hostname] is not defined'
    a = c.extract_defined_undefined(s)
    assert len(a) == 1 and a[0] == ('hostvars[inventory_hostname]', 'is not', 'defined')

    s = 'foo is not defined or bar is defined or hostvars[inventory_hostname] is not defined'
    a = c.extract_defined_undefined(s)
    assert len(a) == 3 and a[0] == ('foo', 'is not', 'defined') and \
        a[1] == ('bar', 'is', 'defined') and a[2] == ('hostvars[inventory_hostname]', 'is not', 'defined')

# Generated at 2022-06-22 11:44:14.283072
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    
    # Test the function with the defined and undefined keywords
    # result doesn't contain "defined" and "undefined"
    result = conditional.extract_defined_undefined("(a is defined or b is undefined)")
    assert len(result) == 2
    contains = ("a" in result[0] and "b" in result[1]) or ("a" in result[1] and "b" in result[0])
    assert contains
    
    # Test the function with the isnot keyword
    result = conditional.extract_defined_undefined("(a isnot defined or b isnot undefined)")
    contains = ("a" in result[0] and "b" in result[1]) or ("a" in result[1] and "b" in result[0])
    assert contains
    
    # Test

# Generated at 2022-06-22 11:44:26.830268
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    dataloader = DataLoader()
    inventory = InventoryManager(loader=dataloader, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=dataloader, inventory=inventory)
    my_vars = variable_manager.get_vars(
        play=dict(
            playbook_basedir='tests',
            roles_path='tests/roles'
        ),
        host=inventory.get_host('all'),
        task=None
    )
    templar = Templar(loader=dataloader, variables=my_vars)

# Generated at 2022-06-22 11:44:37.633055
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # initialize the test class
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    c = Conditional()
    c._loader = True
    pc = PlayContext()
    t = Templar(loader=c._loader, variables=pc.cli_vars)
    all_vars = dict(magicvar='magicval')

    # test case 1
    conditional = 'magicvar == "magicval"'
    res = c.evaluate_conditional(t, all_vars)
    assert res == True

    # test case 2
    conditional = 'magicvar != "magicval"'
    res = c.evaluate_conditional(t, all_vars)
    assert res == False

# Generated at 2022-06-22 11:44:49.742789
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # No variables, nothing to do
    temp = Conditional()
    pc = PlayContext()
    templar = Templar(loader=None, variables=dict())
    res = temp.evaluate_conditional(templar, templar.available_variables)
    assert res

    # Variables, that are not used
    temp = Conditional()
    temp.when = ["2 > 1", "1 < 2"]
    pc = PlayContext()
    templar = Templar(loader=None, variables=dict())
    res = temp.evaluate_conditional(templar, templar.available_variables)
    assert res

    temp.when = ["2 < 1", "1 < 2"]
    res = temp.evaluate_cond

# Generated at 2022-06-22 11:45:01.509760
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class FakeVarsModule:
        def __init__(self, vars=dict()):
            self.vars = vars

        def get_vars(self, play=None, host=None, task=None, include_hostvars=True):
            return self.vars

    class Base:
        pass

    class ConditionalClass(Conditional):
        pass

    conditional_class = ConditionalClass()

    base = Base()
    base._templar = FakeTemplar()
    base._loader = FakeLoader()

    base._variable_manager = FakeVariableManager(FakeVarsModule(dict(a=1, b=2)))
    conditional_class.when = ["a and b"]
    result = conditional_class.evaluate_conditional(base._templar, base._variable_manager.get_vars())
   

# Generated at 2022-06-22 11:45:12.215629
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    import pytest
    x = Conditional()
    assert [('foo', 'is', 'defined')] == x.extract_defined_undefined('foo is defined')
    assert [('foo', 'is', 'defined'), ('a', 'not is', 'undefined')] == x.extract_defined_undefined('foo is defined or a not is undefined')
    assert [('hostvars[inventory_hostname]', 'not is', 'undefined')] == x.extract_defined_undefined('hostvars[inventory_hostname] not is undefined')
    assert [] == x.extract_defined_undefined('hostvars[inventory_hostname] or foo is not defined')
    assert [] == x.extract_defined_undefined('foo')
    assert [] == x.extract_defined_undefined('foo and bar')

# Generated at 2022-06-22 11:45:23.427953
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    data = [
        ('$x is undefined', [('x', 'is', 'undefined')]),
        ('$x is not defined', [('x', 'is not', 'defined')]),
        ('$x is defined', [('x', 'is', 'defined')]),
        ('$x is undefined or $y is defined', [('x', 'is', 'undefined'), ('y', 'is', 'defined')]),
        ('$x == 4 and $y is undefined or $z is defined', [('y', 'is', 'undefined'), ('z', 'is', 'defined')]),
    ]
    for cond, expected in data:
        c = Conditional()
        assert c.extract_defined_undefined(cond) == expected


# Generated at 2022-06-22 11:45:34.495408
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.template import Templar
    #FIXME: Need to write proper unit tests with mocking
    templar = Templar(loader=None)

    # tests fail when not loading constants at top level, so disable that with a stub C
    class C(object):
        jinja2_native_bool = False

    module = Conditional()

    assert module.evaluate_conditional(templar=templar, all_vars={'a': 1}) is True
    assert module.evaluate_conditional(templar=templar, all_vars={'a': 0}) is True
    assert module.evaluate_conditional(templar=templar, all_vars={'a': 1, 'b': 1}) is True

# Generated at 2022-06-22 11:45:46.622538
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader

    C.HOST_VARS      = dict()
    C.GROUP_VARS     = dict()
    C.VARS           = dict()

    my_loader = DataLoader()
    assert Conditional(my_loader).evaluate_conditional(my_loader.get_basedir(),"")

    my_loader = DataLoader()
    assert not Conditional(my_loader).evaluate_conditional(my_loader)

    my_loader = DataLoader()
    assert Conditional(my_loader).evaluate_conditional(my_loader)

    my_loader = DataLoader()
    assert Conditional(my_loader).evaluate_conditional(my_loader)

    my_loader = DataLoader()
    assert Conditional(my_loader).evaluate_conditional(my_loader)

# Generated at 2022-06-22 11:45:58.959102
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.playbook.play_context import PlayContext

    # Test all combinations which should return True

# Generated at 2022-06-22 11:46:22.918380
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    assert conditional.extract_defined_undefined(u'k1 == "v1" and (k2 is not defined or k2 == "v2")') == [(u'k2', u'is not', u'defined')]
    assert conditional.extract_defined_undefined(u'k1 == "v1" and (k2 is defined or k2 == "v2")') == [(u'k2', u'is', u'defined')]
    assert conditional.extract_defined_undefined(u'k1 == "v1" and (k2 is undefined or k2 == "v2")') == [(u'k2', u'is', u'undefined')]

# Generated at 2022-06-22 11:46:31.321553
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    c = Conditional(loader=DataLoader())
    c.when = [ 'foo == bar', 'foo is not bar' ]
    vars = VariableManager()
    assert c.evaluate_conditional(vars, dict(foo='bar'))
    assert not c.evaluate_conditional(vars, dict(foo='baz'))

    c.when = [ 'foo == "bar"', 'foo is not "bar"' ]
    assert c.evaluate_conditional(vars, dict(foo='bar'))
    assert not c.evaluate_conditional(vars, dict(foo='baz'))

    c.when = [ 'foo == "bar"', 'foo is not "baz"' ]
   

# Generated at 2022-06-22 11:46:41.573531
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import jinja2

    display.verbosity = 3
    templar = jinja2.Environment()

    # define a conditional expression, using a string
    expression = "foo > 2"
    # create a Conditional object and add the expression
    cond = Conditional()
    cond.when.append(expression)

    # define a dictionary with variables and values
    all_vars = {
        "foo": 3,
        "bar": 2,
        "baz": "this is text"
    }

    # evaluate the expression
    result = cond.evaluate_conditional(templar, all_vars)

    # Test the result
    assert result == True

    # define other expression with a variable that is not defined in all-vars
    expression = "foo > bar+1"
    # add the new expression
    cond

# Generated at 2022-06-22 11:46:51.132015
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    def test(conditionals, variables, expected_results):
        display.display('==== test_Conditional_evaluate_conditional ====')
        display.display('conditionals = %s' % conditionals)
        display.display('variables = %s' % variables)
        display.display('expected_results = %s' % expected_results)

        loader = DataLoader()
        variable_manager = VariableManager()

        play_context = PlayContext()
        play_context.variable_manager = variable_manager
        templar = Templar(loader, variables, play_context)


# Generated at 2022-06-22 11:46:57.977083
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.compat.tests import unittest

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib

    # For this test we want to be able to test the value of a variable
    # without the var being defined in any of the passed in data. To do
    # this, we will use a VariableManager and provide it a set of variables
    # that we can use to test the value of the var
    test_var = dict()
    test_var[u'foo'] = u'bar'
    vars_loader = dict()
    vars_loader['vars'] = VariableManager(loader=None, variables=test_var)

    # Inject the templar into our local copy of the conditional class
    # so we can call evaluate

# Generated at 2022-06-22 11:47:05.077797
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # create the Conditional object
    cond = Conditional()
    # create the test data
    test_data = {
        "hostvars['foo'] is defined": [
            ('hostvars[\'foo\']', 'is', 'defined')
        ],
        "hostvars['foo'] is not undefined": [
            ('hostvars[\'foo\']', 'is not', 'undefined')
        ],
        "hostvars['foo'] is defined and hostvars['bar'] is not undefined": [
            ('hostvars[\'foo\']', 'is', 'defined'),
            ('hostvars[\'bar\']', 'is not', 'undefined')
        ]
    }

    # run the actual tests
    for test_string in test_data.keys():
        result = cond.extract_defined_undefined

# Generated at 2022-06-22 11:47:17.981254
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def test_extract_defined_undefined(conditional, expected):
        c = Conditional()
        result = c.extract_defined_undefined(conditional)
        assert result == expected, "Result is %s, expected %s" % (result, expected)
    test_extract_defined_undefined('hostvars[inventory_hostname] is defined', [('hostvars[inventory_hostname]', 'is', 'defined')])
    test_extract_defined_undefined('hostvars[inventory_hostname] is defined and hostvars[inventory_hostname] is defined', [('hostvars[inventory_hostname]', 'is', 'defined'), ('hostvars[inventory_hostname]', 'is', 'defined')])

# Generated at 2022-06-22 11:47:19.940829
# Unit test for constructor of class Conditional
def test_Conditional():
    conditional = Conditional()
    assert conditional is not None


# Generated at 2022-06-22 11:47:30.965652
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    try:
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars.manager import VariableManager
        from ansible.inventory.manager import InventoryManager
        from ansible.playbook.play_context import PlayContext
    except ImportError as e:
        print("FATAL: '%s' is missing. Skipping test." % e.name)
        return

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_context = PlayContext()
    t = C.DEFAULT_TEMPLATE_ENGINE
    loader.set_basedir('/tmp/ansible_test')

# Generated at 2022-06-22 11:47:43.447922
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import jinja2

    class PlaybookModule:
        pass

    class PlaybookExecutor:
        def __init__(self):
            self.result = PlaybookModule()
            self.result.contacted = {'x': {'invocation': {'module_args': 'z'}}}
            self.result._host = 'x'
            self.result._task = class_instance
            self.result._task.name = 'n'

        def get_host_results(self, hostname, taskname):
            return self.result

        def get_host_variable(self, hostname, varname):
            return {'x': 'y'}

        def get_task_result(self, hostname, taskname):
            return self.result

    class Class:
        def __init__(self):
            self.loader

# Generated at 2022-06-22 11:48:20.365186
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Conditional(object):
        def __init__(self):
            self.when = ["{{ a }} == 2 or {{ b }} or {{ c.d }}", False]
    class MyVars(dict):
        pass
    class MyTemplar(object):
        def __init__(self):
            self.environment = None
        def is_template(self, content):
            if not isinstance(content, text_type) or content == "":
                return False
            return "{{ " in content or "{%" in content
        def template(self, content, disable_lookups=False):
            if self.is_template(content):
                if disable_lookups:
                    return content
                else:
                    return "template(%s)" % (content)
            else:
                return content

# Generated at 2022-06-22 11:48:33.516647
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
  # Test 1a: Positive case - True when
  #          when 1: True
  #          when 2: False
  conditional = Conditional()
  conditional.when = [True, False]
  res = conditional.evaluate_conditional(None, None)
  assert res == True

  # Test 1b: Negative case - False when
  #          when 1: False
  #          when 2: False
  conditional = Conditional()
  conditional.when = [False, False]
  res = conditional.evaluate_conditional(None, None)
  assert res == False

  # Test 2a: Positive case - True when
  #           when 1: True
  #           when 2: True
  #           when 3: False
  conditional = Conditional()
  conditional.when = [True, True, False]
  res = conditional.evaluate_conditional

# Generated at 2022-06-22 11:48:45.952886
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import ansible.ansible_compat
    # Creating a fake object to test evaluate_conditional
    class TestObject:
        def __init__(self):
            self._ds = {}
            self._loader = ansible.ansible_compat.AnsibleLoader()

    # Creating a fake jinja2 environment to test evaluate_conditional
    class FakeEnvironment:
        def parse(self, cond, filename, name):
            return ast.parse(cond, mode='exec')

        def generate(self, parsed, environment, filename, name):
            gen = generate(parsed, self, filename, name)
            return gen.next()

    # Creating fake jinja2 template to test evaluate_conditional
    class FakeTemplate:
        def __init__(self, txt, lookup=False):
            self.txt = txt


# Generated at 2022-06-22 11:48:56.804960
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined("var is defined") == [("var", "is", "defined")]
    assert Conditional().extract_defined_undefined("var is not defined") == [("var", "is not", "defined")]
    assert Conditional().extract_defined_undefined("var is not defined and var2 is undefined") == [("var", "is not", "defined"), ("var2", "is", "undefined")]
    assert Conditional().extract_defined_undefined("var is not defined and 'var2' is undefined") == [("var", "is not", "defined"), ("'var2'", "is", "undefined")]

# Generated at 2022-06-22 11:49:08.553039
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    variable_names = [ "hostvars['foo']", "hostvars['bar']",
                       "foo", "bar",
                       "hostvars['a']", "a"
                     ]

    conditionals = [ "hostvars['foo'] is defined",
                     "hostvars['bar'] is undefined",
                     "foo is defined",
                     "bar is undefined",
                     "hostvars['a'] is defined and a is undefined",
                     "hostvars['a'] is defined and a is not defined",
                     "hostvars['a'] is not defined and a is not undefined",
                     "hostvars['a'] is not defined and a is defined",
                   ]


# Generated at 2022-06-22 11:49:21.048372
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    class Conditional_evaluate_conditional_instance(Conditional):
        pass

    def _generate_fake_variable_manager(all_vars):
        class FakeVariableManager:
            def get_vars(self, play=None, host=None, task=None):
                return all_vars

            def add_variable(self, host, varname, value):
                pass

            def add_child(self, child):
                pass

            def set_nonpersistent_facts(self, host, facts):
                pass

            @property
            def extra_vars(self):
                return {}

            @extra_vars.setter
            def extra_vars(self, extra_vars):
                pass

            @property
            def hostvars(self):
                return {}


# Generated at 2022-06-22 11:49:32.601485
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # exemple with one statement
    res = Conditional.extract_defined_undefined("var is defined")
    assert(res == [('var', 'is', 'defined')])
    # example with two statements
    res = Conditional.extract_defined_undefined("var_1 is defined or var_2 is not defined")
    assert(res == [('var_1', 'is', 'defined'), ('var_2', 'is not', 'defined')])
    # example with multiple statements
    res = Conditional.extract_defined_undefined("var_1 is defined or var_2 is not defined or var_3 is defined")
    assert(res == [('var_1', 'is', 'defined'), ('var_2', 'is not', 'defined'), ('var_3', 'is', 'defined')])

# Generated at 2022-06-22 11:49:44.423148
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Always():
        def evaluate_conditional(self, templar, all_vars):
            return True
        def when(self):
            return 'not true'
        def name(self):
            return 'test'
    class Never():
        def evaluate_conditional(self, templar, all_vars):
            return False
        def when(self):
            return 'not true'
        def name(self):
            return 'test'

    import ansible.playbook.task_include as task_include
    import ansible.playbook.block as block
    import ansible.playbook.play as play
    import ansible.playbook.playbook as playbook

    fake_loader = DictDataLoader({})

    block1 = block.Block()
    block1.block = [Always()]

# Generated at 2022-06-22 11:49:55.587511
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    assert Conditional(None).extract_defined_undefined("'test' is defined") == [("test", "is", "defined")]
    assert Conditional(None).extract_defined_undefined("'test1' == 'test2' or 'test3' is defined") == [("test3", "is", "defined")]
    assert Conditional(None).extract_defined_undefined("7-9 == 'test' or 'test3' is not defined") == [("test3", "is", "not", "defined")]
    assert Conditional(None).extract_defined_undefined("7-9 == 'test' or foo is not defined") == [('foo', 'is', 'not', 'defined')]

# Generated at 2022-06-22 11:50:07.486042
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    from ansible.template import Templar
    from ansible.utils.display import Display

    testdisplay = Display()

    # initialize templar
    vault_pass = '$ANSIBLE_VAULT;1.1;AES256'
    vault = VaultLib(password=vault_pass)
    vault_editor = VaultEditor(vault_pass)
    templar = Templar(loader=None, variables={}, vault_secrets=vault.secrets)

    # initialize vars
    all_vars = dict()

    # test simple string and int
    cond = Conditional()

    # string: assert true
    cond.when = ['foo is bar']