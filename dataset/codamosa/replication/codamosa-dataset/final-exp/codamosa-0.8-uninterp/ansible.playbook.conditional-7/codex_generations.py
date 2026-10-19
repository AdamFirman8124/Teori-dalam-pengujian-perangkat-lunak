

# Generated at 2022-06-22 11:40:27.481390
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template.template import Templar

    C.ANSIBLE_VAULT_VERSION = 1
    C.ANSIBLE_VAULT_PASSWORD_FILE = 'test/ansible-vault-password-file'

    from ansible.template.vars import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-22 11:40:38.065779
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar

    conditional = Conditional()


# Generated at 2022-06-22 11:40:44.007702
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    class TestConditional(Conditional):
        pass

    tl = TestConditional()


# Generated at 2022-06-22 11:40:49.843882
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    conditional = 'test_var is defined or test_var2 is defined and test_var3 is not defined'
    result = c.extract_defined_undefined(conditional)
    expected = [('test_var', 'is', 'defined'), ('test_var2', 'is', 'defined'), ('test_var3', 'is not', 'defined')]
    assert result == expected, \
        "Result of method extract_defined_undefined of class Conditional should be %s but is %s" % (expected, result)

# Generated at 2022-06-22 11:41:02.414018
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class Object(object):
        def __init__(self, ds):
            self._ds = ds
            self._name = None
            self._loader = None

        def add_when(self, val):
            self._when.append(val)

        def evaluate_conditional(self, templar, all_vars):
            return Conditional.evaluate_conditional(self, templar, all_vars)

        def _validate_when(self, attr, name, value):
            if not isinstance(value, list):
                setattr(self, name, [value])

        _when = FieldAttribute(isa='list', default=list, extend=True, prepend=True)

    import jinja2
    class MockTemplar(object):
        def __init__(self):
            self.environment

# Generated at 2022-06-22 11:41:03.692611
# Unit test for constructor of class Conditional
def test_Conditional():
    assert issubclass(Conditional, object)

# Generated at 2022-06-22 11:41:17.234448
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional().extract_defined_undefined('hostvars[inventory_hostname] is defined') == [('hostvars[inventory_hostname]', 'is', 'defined')]
    assert Conditional().extract_defined_undefined('not hostvars[inventory_hostname] is undefined') == [('hostvars[inventory_hostname]', 'not is', 'undefined')]
    assert Conditional().extract_defined_undefined('(hostvars[inventory_hostname] is not defined) and hostname is defined') == [('hostvars[inventory_hostname]', 'is not', 'defined'), ('hostname', 'is', 'defined')]
    assert Conditional().extract_defined_undefined('hostvars[inventory_hostname] is defined and test_var is not defined and other_var is not defined')

# Generated at 2022-06-22 11:41:27.439500
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class ConditionalTestClass(Conditional):
        pass
    import jinja2
    test_all_vars = dict(
        var1='foo',
        var2='bar',
        var3=3,
        var4=-1,
        var5=1,
        var6=True,
        var7=False,
        var8=['foo', 'bar'],
        var9=dict(foo='bar'),
    )
    test_templar = jinja2.Environment()

    # unit test for empty conditional
    test_obj = ConditionalTestClass()
    test_obj._loader = None
    test_obj._ds = 'test_obj'
    test_obj.when = [None]

    assert test_obj.evaluate_conditional(test_templar, test_all_vars)



# Generated at 2022-06-22 11:41:38.397412
# Unit test for method extract_defined_undefined of class Conditional

# Generated at 2022-06-22 11:41:50.638936
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def _test(test_case, expected):
        x = Conditional()
        assert x.extract_defined_undefined(test_case) == expected

    # Empty string, nothing to find
    for e in ('', '\n', '\r'):
        yield _test, e, []
    # Valid cases

# Generated at 2022-06-22 11:42:07.776879
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    host_vars = {'test_host': {'test_var': 'test_value'}}
    group_vars = {'test_group': {'test_var': 'test_value'}}


# Generated at 2022-06-22 11:42:17.816191
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    import sys

    loader = DataLoader()
    group = 'lay1'
    host = '127.0.0.1'
    inventory = InventoryManager(loader, sources='localhost,')
    inventory.add_host(host)
    inventory.add_group(group)
    inventory.add_child(group, host)

    play_context = PlayContext(remote_addr=host, remote_user='remote_user')
    templar = Templar

# Generated at 2022-06-22 11:42:27.488784
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestConditional(Conditional):
        _name = "test_conditional"
    test_conditional = TestConditional()
    test_conditional._ds = "test_ds"
    test_conditional.when = ["ansible_os_family == 'RedHat'", "test_var == 'ok'"]
    templar = None
    all_vars = dict(test_var="ok")
    assert test_conditional.evaluate_conditional(templar, all_vars) == True
    all_vars = dict(test_var="ko")
    assert test_conditional.evaluate_conditional(templar, all_vars) == False


# Generated at 2022-06-22 11:42:36.329274
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    import ansible.playbook.play
    import ansible.playbook.role
    import ansible.template
    import ansible.vars

    p = ansible.playbook.play.Play()
    r = ansible.playbook.role.Role()
    t = ansible.template.Templar(loader=ansible.vars.VariableManager())
    # Tests the True branch
    p.vars = dict(test_var1=0, test_var2=0)
    assert(Conditional.evaluate_conditional(p, t) == True)
    # Tests the False branch
    p.vars = dict(test_var1="test", test_var2="expected")
    assert(Conditional.evaluate_conditional(p, t) == False)
    # Tests the check of variables

# Generated at 2022-06-22 11:42:49.583988
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class CountingPluginLoader:
        def __init__(self):
            self.count = 0

        def get(self, *args, **kwargs):
            self.count += 1
            return None

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()

# Generated at 2022-06-22 11:43:02.155920
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()

# Generated at 2022-06-22 11:43:13.701985
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    module = Conditional()
    vars = VariableManager()
    res = module.evaluate_conditional(templar=vars, all_vars=vars)
    assert res is True

    res = module.evaluate_conditional(templar=vars, all_vars=vars, conditional=True)
    assert res is True

    res = module.evaluate_conditional(templar=vars, all_vars=vars, conditional=False)
    assert res is False

    res = module.evaluate_conditional(templar=vars, all_vars=vars, conditional='hostvars["foo"] is defined')
    assert res is False


# Generated at 2022-06-22 11:43:25.617515
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def _test(test_str, expected):
        test_results = Conditional().extract_defined_undefined(test_str)
        assert test_results == expected, 'Result: %s, Expected: %s' % (test_results, expected)


# Generated at 2022-06-22 11:43:37.698601
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    pc = PlayContext()
    t = Templar(pc)
    c = Conditional(loader=None)

    result = c.extract_defined_undefined(None)
    assert result == []
    result = c.extract_defined_undefined('')
    assert result == []
    result = c.extract_defined_undefined('anything')
    assert result == []
    result = c.extract_defined_undefined('anything var1 is undefined')
    assert result == [('var1', 'is', 'undefined')]
    result = c.extract_defined_undefined('var1 is defined and (var2 is undefined or var3 is defined)')

# Generated at 2022-06-22 11:43:49.628557
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    assert Conditional.extract_defined_undefined("a is defined") == [("a", "is", "defined")]
    assert Conditional.extract_defined_undefined("a is not undefined") == [("a", "is not", "undefined")]
    assert Conditional.extract_defined_undefined("a is defined or b is defined") == [("a", "is", "defined"), ("b", "is", "defined")]
    assert Conditional.extract_defined_undefined("2.0 > 1.9 and a is defined") == [("a", "is", "defined")]
    assert Conditional.extract_defined_undefined("2.0 > 1.9 and a is not undefined") == [("a", "is not", "undefined")]

# Generated at 2022-06-22 11:44:15.511796
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display = Display()
    display.verbosity = 3
    import jinja2
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    class Play(object):
        def __init__(self):
            self._ds = None
            self._loader = None
            self._variable_manager = None
            self._shared_loader_obj = None
            self._loader_cache = None
            self.vars = {}
            self.extra_vars = {}
            self.set_extra_vars(None)
            self.hosts = None

        def set_extra_vars(self, extra_vars):
            if C.DEFAULT_JINJA2_NATIVE:
                self.extra_vars['ansible_facts'] = {}
            else:
                extra_

# Generated at 2022-06-22 11:44:26.783577
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    class TestConditional(Conditional):
        def __init__(self, loader, templar, all_vars):
            self.when = ['ansible_eth0.mtu == 9000', 'ansible_eth1.mtu == 9000']
            self._templar = templar
            self._all_vars = all_vars
            self._loader = loader

    all_vars = {'ansible_eth0.mtu': 9000, 'ansible_eth1.mtu':1500}
    templar = TestTemplar()
    cond = TestConditional(None, templar, all_vars)

    assert cond.evaluate_conditional(templar, all_vars) == False



# Generated at 2022-06-22 11:44:39.143864
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.template.template

    ctx = ansible.playbook.play_context.PlayContext()
    C.DEFAULT_HANDLER_INCLUDES = True
    C.DEFAULT_PRIVATE_ROLE_VARS = True
    play = ansible.playbook.play.Play()
    play._included_filenames = []
    play.first_file_in_play = "fake"
    play._post_validation_errors = []
    block = ansible.playbook.block.Block()
    task = ansible.playbook.task.Task()
    role = ansible

# Generated at 2022-06-22 11:44:50.370969
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.module_utils.six import StringIO

    import ansible.plugins.loader as plugin_loader

    from ansible.template import Templar

    from ansible.vars.manager import VariableManager

    from ansible.parsing.dataloader import DataLoader

    from ansible.inventory.manager import InventoryManager

    from ansible.playbook.play_context import PlayContext

    class Options:
        connection = 'local'
        module_path = None
        forks = 100
        remote_user = 'username'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = None
        become_user = None
        verbosity = 1


# Generated at 2022-06-22 11:45:01.994359
# Unit test for method evaluate_conditional of class Conditional

# Generated at 2022-06-22 11:45:12.494209
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    display.verbosity = 4
    all_vars = dict(
        hostvars=dict(
            host1=dict(
                foo=dict(
                    bar='val'
                )
            ),
            host2=dict(
                foo=dict(
                    bar='val'
                )
            )
        ),
        groups=dict(
            group1=dict(
                hosts=['host1', 'host2']
            ),
            group2=dict(
                hosts=['host1']
            )
        )
    )
    assert Conditional().evaluate_conditional('groups["group1"]["hosts"] | length > 1', all_vars)
    assert Conditional().evaluate_conditional('groups["group2"]["hosts"] | length == 1', all_vars)
    assert Conditional().evaluate_

# Generated at 2022-06-22 11:45:19.992644
# Unit test for constructor of class Conditional
def test_Conditional():
    from ansible.playbook import PlayBook
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    play_context = PlayContext()
    play = PlayBook.load(dict(name="test", hosts="all", gather_facts="no", tasks=[]),
                         loader=loader, play_context=play_context, variable_manager=play_context.variable_manager)
    assert play.hosts == "all"



# Generated at 2022-06-22 11:45:30.218308
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    assert c.extract_defined_undefined('foo_bar is not defined') == [('foo_bar', 'is not', 'defined')]
    assert c.extract_defined_undefined('foo_bar is undefined') == [('foo_bar', 'is', 'undefined')]
    assert c.extract_defined_undefined('foo_bar not is undefined') == [('foo_bar', 'not is', 'undefined')]
    assert c.extract_defined_undefined('foo_bar not is defined') == [('foo_bar', 'not is', 'defined')]
    assert c.extract_defined_undefined('hostvars["foo"] is not defined') == [('hostvars["foo"]', 'is not', 'defined')]
    assert c.extract_defined_undefined

# Generated at 2022-06-22 11:45:40.607196
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar

    # Check a conditional with a single condition
    t = Templar(play_context=PlayContext())
    c = Conditional()
    c._ds = Task()
    assert c.evaluate_conditional(t, dict(foo="bar")) == False
    c.when = AnsibleUnsafeText("foo == 'bar'", False)
    assert c.evaluate_conditional(t, dict(foo="bar")) == True

    # Check if a list of conditionals works
    t = Templar(play_context=PlayContext())
    c = Conditional()
    c._ds = Task()
    assert c.evaluate_conditional

# Generated at 2022-06-22 11:45:50.421836
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional = Conditional()
    res = conditional.extract_defined_undefined("{{ foo == 'bar' and bar is defined }}")
    assert len(res) == 1 and (res[0][0], res[0][1], res[0][2]) == ('bar', 'is', 'defined')
    res = conditional.extract_defined_undefined("{{ foo == 'bar' and 'bar' is defined }}")
    assert len(res) == 1 and (res[0][0], res[0][1], res[0][2]) == ('bar', 'is', 'defined')
    res = conditional.extract_defined_undefined("{{ foo == 'bar' and hostvars['bar'] is defined }}")

# Generated at 2022-06-22 11:46:25.769907
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    c = Conditional()
    conditional1 = "ansible_os_family is defined and ansible_os_family == 'RedHat'"
    expected1 = [("ansible_os_family", "is", "defined"),
                 ("ansible_os_family", "==", "RedHat")]
    assert(c.extract_defined_undefined(conditional1) == expected1)
    conditional2 = "ansible_os_family not in ['RedHat', 'Debian']"
    assert(c.extract_defined_undefined(conditional2) == [])


# Generated at 2022-06-22 11:46:35.532866
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():

    from ansible.playbook.play import Play

    # struture to test
    conditional = "(var1 == var2  or (var3 is defined and " \
                  "group_names['var4'] is not defined)) and var5 is not defined"
    expected = [('var3', 'is', 'defined'), ('group_names[\'var4\']', 'is not', 'defined'), ('var5', 'is not', 'defined')]
    # initiate test class
    conditional = Conditional()
    result = conditional.extract_defined_undefined(conditional=conditional)
    assert result == expected, 'Conditional.extract_defined_undefined returned %s instead of %s' % (result, expected)

# Generated at 2022-06-22 11:46:47.289032
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.base import Base
    b = Base()

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['localhost,']))

    variable_manager.extra_vars = {'foo': 'bar'}
    templar = Templar(loader=loader, variables=variable_manager)

    def test_conditional(template, expected_value, var_dict=None):
        conditional = Conditional()
        conditional.when = [template]


# Generated at 2022-06-22 11:46:58.828747
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    def test(c, expected_result):
        conditional = Conditional()
        res = conditional.extract_defined_undefined(c)
        if (res != expected_result):
            print ("ERROR: \"%s\" should be understood as \"%s\" not \"%s\"" % (c, expected_result, res))

    test("""something
            not foo is defined""", [('foo', 'not is', 'defined')])
    test("""something
            foo not is defined""", [('foo', 'not is', 'defined')])
    test("""something
            foo is not defined""", [('foo', 'is', 'defined')])
    test("""something
            foo is defined""", [('foo', 'is', 'defined')])

# Generated at 2022-06-22 11:47:05.520899
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    conditional_object = Conditional()
    # Test for combination of is, not, undefined and defined checking
    test_value = "a is not undefined and b is undefined and c is defined"
    result = conditional_object.extract_defined_undefined(test_value)
    assert result == [('a', 'is not', 'undefined'), ('b', 'is', 'undefined'), ('c', 'is', 'defined')]

    # Test for is, undefined and defined checking
    test_value = "a is undefined and b is defined"
    result = conditional_object.extract_defined_undefined(test_value)
    assert result == [('a', 'is', 'undefined'), ('b', 'is', 'defined')]

    # Test for is, undefined checking
    test_value = "a is undefined and b is undefined"
    result

# Generated at 2022-06-22 11:47:18.369898
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():

    from ansible.playbook.base import Base
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.parsing.dataloader import DataLoader

    # Variables used in the conditional tests
    test_host = Host(name="testhost")
    test_host.vars = HostVarsVars(host=test_host, variables=dict(foo='bar', baz='qux'))

    test_group = Group(name="testgroup")
    test_group.hosts.add(test_host)

# Generated at 2022-06-22 11:47:29.579639
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    loader = DictDataLoader({})
    variable_manager = VariableManager()

    conditional = Conditional({})
    conditional._loader = loader
    conditional.when = ["(1) > 0", "(1) < 0", "(1) >= 0", "(1) <= 0", "(1) == 0", "(1) != 0", "(1) == 1", "(0) != 1"]
    assert conditional.evaluate_conditional(Templar(loader=loader, variables=variable_manager), HostVars(loader=loader, variables=variable_manager)) is False
    conditional.when = ["(1) == 0"]

# Generated at 2022-06-22 11:47:41.880499
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    '''
    Test the method extract_defined_undefined of class Conditional
    '''

    # test empty string
    conditional = ''
    c = Conditional()
    result = c.extract_defined_undefined(conditional)
    assert result == []

    # test string without defined/undefined pattern
    conditional = "a_var and b_var"
    result = c.extract_defined_undefined(conditional)
    assert result == []

    conditional = "a_var and b_var and c_var"
    result = c.extract_defined_undefined(conditional)
    assert result == []

    conditional = "a_var"
    result = c.extract_defined_undefined(conditional)
    assert result == []

    # test string with 2 valid defined/undefined pattern

# Generated at 2022-06-22 11:47:54.268122
# Unit test for method extract_defined_undefined of class Conditional
def test_Conditional_extract_defined_undefined():
    # Test method extract_defined_undefined of class Conditional
    # Test 1: is defined
    # Test 2: is not defined
    # Test 3: is defined and is not defined, both in one expression
    # Test 4: random text, without any defined or undefined in it
    # Test 5: is defined and is not defined, both in one expression, and also other random text

    c = Conditional()

    test1 = u'some_var is defined'
    test2 = u'some_other_var is not defined'
    test3 = u'some_var is defined and some_other_var is not defined'
    test4 = u'some random text without definitions'
    test5 = u'some_var is defined and some_other_var is not defined, also some random text'


# Generated at 2022-06-22 11:48:02.652706
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
    to prevent regression on the method Conditional.evaluate_conditional()
    '''
    import ansible.playbook.play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    p = ansible.playbook.play.Play()
    t = Templar(loader=DataLoader())
    v = VariableManager()
    p._variable_manager = v

    p.when = ['inventory_hostname == foo']
    # hostname foo
    assert p.evaluate_conditional(t, v.get_vars(loader=t._loader, play=p))

    p.when = ['inventory_hostname != foo']
    # hostname foo

# Generated at 2022-06-22 11:49:09.675612
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    '''
      Playbook:
        - hosts: all
          gather_facts: no
          tasks:
            - when: 1 < 2
            - when: 2 < 3
            - when: 2 < 1
          handlers:
            - include: test_Conditional_evaluate_conditional.yml
              when: 2 < 3

      # Handler file test_Conditional_evaluate_conditional.yml
      - debug: msg="test"
    '''
    # Prepare inventory and fake connection
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    loader.connection_loader = connection_loader
    loader.lookup_

# Generated at 2022-06-22 11:49:21.598598
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # Mock the templar and the template
    from mock import MagicMock, ANY

    # Mock the templar
    templar = MagicMock()
    # When the templar receives an eval, then it returns an int
    templar.template = MagicMock(return_value=1)
    # Create a Conditional object
    conditional = Conditional()
    # Set the templar
    conditional._templar = templar
    # Set when value and do the evaluation
    conditional.when = True
    res = conditional.evaluate_conditional(templar, "")
    assert res is True
    # The template has been called, then return True
    templar.template.assert_any_call(True)

    # Set when value and do the evaluation, then the value is not True
    conditional.when = 0

# Generated at 2022-06-22 11:49:33.211209
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    import jinja2
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    t = Templar(variables={})
    h = Host(name="randomhost")
    g = Group(name="somerg")
    g.hosts.append(h)
    v = VariableManager()
    v.set_host_variable(h, "omg", 42)
    v.set_host_variable(h, "ansible_ssh_host", "foo.example.com")
    v.set_host_variable(h, "ansible_ssh_port", 42)
    v.set_host_variable(h, "ansible_ssh_user", "joe")
    v.set_host_variable

# Generated at 2022-06-22 11:49:44.813376
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    ''' test_Conditional_evaluate_conditional is a unit test for method evaluate_conditional of class Conditional
    '''
    test_obj = Conditional()
    test_obj.when = ['some_var']
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inventory)

    templar = Templar(loader=None, variables=variable_manager)

    res = test_obj.evaluate_conditional(templar, {'some_var': 'val'})
    assert res

    res = test_obj.evaluate_conditional(templar, {'some_var_not': 'val'})

# Generated at 2022-06-22 11:49:55.863504
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    coll = Conditional()
    coll.when.append('inventory_hostname in groups.webservers')
    coll.when.append('inventory_hostname in groups.dbservers')
    coll.when.append('inventory_hostname in groups.dbservers and groups.webservers')

    # Test variables to be used with templating
    all_vars = dict(
        inventory_hostname = 'server01',
        groups = dict(
            webservers = ['server01', 'server02', 'server03'],
            dbservers = ['server01', 'server02', 'server03'],
        ),
    )

    # Test data

# Generated at 2022-06-22 11:50:07.774125
# Unit test for method evaluate_conditional of class Conditional
def test_Conditional_evaluate_conditional():
    # setup temporary class
    class TestConditional(Conditional):
        pass

    inventory = {
        "all": {
            "children": ["ungrouped"]
        },
        "ungrouped": {}
    }

    # create class instance with variable and custom variable
    tc = TestConditional()
    tc._loader = None
    tc._ds = {
        "test": {
            "test": [1,2,3],
            "test2": "test"
        }
    }