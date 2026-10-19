

# Generated at 2022-06-13 09:13:24.279526
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    # [1] setup
    play_context = PlayContext()
    play_context.only_tags = ['tagged']
    play_context.skip_tags = ['never', 'nope']
    play_context._task_tags = frozenset(['tagged'])
    play_context._role_tags = frozenset(['tagged'])
    play_context._play_tags = frozenset(['tagged'])
    play_context._all_tags = play_context._task_tags | play_context._role_tags | play_context._play_tags

    # [2] Test tagged

# Generated at 2022-06-13 09:13:28.269249
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ta = Taggable()
    assert ta.evaluate_tags(["a"], [], {}) == True, "Assertions are working"
    assert ta.evaluate_tags([], ["a"], {}) == True, "Assertions are working"

# Generated at 2022-06-13 09:13:38.423467
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Default test
    test_object = Taggable()

    test_only_tags = []
    test_skip_tags = []
    test_all_vars = {}

    should_run_default = test_object.evaluate_tags(test_only_tags, test_skip_tags, test_all_vars)
    assert should_run_default

    # Test with only tags
    test_only_tags = ['only_1', 'only_2']
    test_skip_tags = []
    test_all_vars = {}

    # Only_1 and only_2 in self.tags should return True
    test_object._tags = ['only_1', 'only_2', 'only_3']

# Generated at 2022-06-13 09:13:53.650006
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    import ansible.playbook.task
    task = ansible.playbook.task.Task()

    # Check the default return value
    assert task.evaluate_tags([], []) == True
    assert task.evaluate_tags(None, None) == True
    assert task.evaluate_tags([], None) == True

    # Check the tag 'always'
    task._tags = ['always']
    assert task.evaluate_tags([], ['never']) == True

    # Check the tag 'never'
    task._tags = ['never']
    assert task.evaluate_tags(['always'], []) == False
    assert task.evaluate_tags([], ['never', 'all']) == False
    assert task.evaluate_tags(['all'], ['never']) == False

# Generated at 2022-06-13 09:14:05.213439
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task

    def my_test_task():
        print('test_task')

    def my_test_always_task():
        print('test_always_task')

    def my_test_never_task():
        print('test_never_task')

    task = ansible.playbook.task.Task()
    task.action = my_test_task
    task.tags = ['tagged']

    always_task = ansible.playbook.task.Task()
    always_task.action = my_test_always_task
    always_task.tags = ['always']

    never_task = ansible.playbook.task.Task()
    never_task.action = my_test_never_task
    never_task.tags = ['never']

    # test that tasks with skip_tags do not

# Generated at 2022-06-13 09:14:09.343624
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.template import Templar


# Generated at 2022-06-13 09:14:14.684007
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass(Taggable):
        pass

    item = TestClass()
    item.tags = ['a', 'b']

    only_tags = ['c', 'd', 'e']
    skip_tags = ['f', 'g', 'h']
    assert item.evaluate_tags(only_tags, skip_tags, {'test_variable': True}) == False

    only_tags = ['a', 'c', 'd', 'e']
    skip_tags = ['f', 'g', 'h']
    assert item.evaluate_tags(only_tags, skip_tags, {'test_variable': True}) == True

    only_tags = ['a', 'c', 'd', 'e']
    skip_tags = ['a', 'f', 'g', 'h']

# Generated at 2022-06-13 09:14:24.122200
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import IncludeTask
    from ansible.playbook.taggable import Taggable
    from ansible.template import Templar

    loader = 'fake loader'
    variables = dict()

    class MyTaggable(Taggable):
        _loader = FieldAttribute(isa='loader', default=dict)

    class MyIncludeTask(IncludeTask, MyTaggable):
        pass

    class MyIncludeRole(IncludeRole, MyTaggable):
        pass

    #####################################################################
    # Test 1: include_role and include_task - No tags specified
    #####################################################################

    # Parameters

    # include_role
    filename = 'filename for include_role'

# Generated at 2022-06-13 09:14:32.527586
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.six import iteritems
    from ansible.template import Templar

    loader = DataLoader()

    # PlayContext for tests
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    # Data for testing
    play_context._set_only_tags('tag_a')
    play_context._set_skip_tags(['tag_c', 'tag_d'])

    # Set

# Generated at 2022-06-13 09:14:39.372509
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    # Test that when untagged is the only tag, we evaluate True when 'tagged' is in only_tags
    tagged_only = Playbook()
    tagged_only = tagged_only.load(dict(
        name = "Tagged Only",
        hosts = ['localhost'],
        gather_facts = 'no',
        roles = ['test-role'],
        tasks = [
            dict(
                action = dict(module='debug', args=dict(msg='Test Msg'))
            )
        ]
    ), loader=None, variable_manager=None)
    tagged_

# Generated at 2022-06-13 09:14:55.084002
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeRole(Taggable):
        pass

    only_tags = ['foo']
    skip_tags = ['bar']

    role = FakeRole()

    # Test no tags
    role.tags = []
    assert(role.evaluate_tags(only_tags, skip_tags, dict()) == True)

    # Test only_tags
    role.tags = ['foo', 'bar']
    assert role.evaluate_tags(only_tags, skip_tags, dict()) == True

    role.tags = ['foos']
    assert role.evaluate_tags(only_tags, skip_tags, dict()) == False

    # Test skip_tags
    role.tags = ['bar', 'foos']
    assert role.evaluate_tags(only_tags, skip_tags, dict()) == False

    # Test both only_tags and skip_tags
   

# Generated at 2022-06-13 09:15:07.483150
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    Taggable._tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)

    only_tags = set(['all', 'tagged'])
    skip_tags = set(['never', 'tagged'])

    my_taggable = Taggable()
    my_taggable.tags = "big,bigger"

    # check for a tagged item that shouldn't be run
    assert my_taggable.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars={}) == False

    # check for a tagged item that should be run
    my_taggable.tags = "big,bigger"

# Generated at 2022-06-13 09:15:19.290709
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    only_tags = ['tagA']
    skip_tags = []
    all_vars = dict(foo='foo', bar='bar')

    play_context = PlayContext()
    play_context.only_tags = only_tags
    play_context.skip_tags = skip_tags
    play_context.tags = ['tagA','tagB','tagC']

    task = Task()
    task._play_context = play_context
    task.tags = set(['tagB','tagC','never'])
    assert task.evaluate_tags(only_tags, skip_tags, all_vars) == False

    task.tags = set(['tagA','tagB','always'])

# Generated at 2022-06-13 09:15:29.725528
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    # Action plugin needs to get the group vars from the inventory
    from ansible.plugins.action import ActionBase
    class ActionModule(ActionBase):
        def run(self, tmp=None, task_vars=dict()):
            raise NotImplementedError()

    # Fake task
    task = Task()
    task.action = 'debug'
    task.args = {'msg': 'hello world'}

    # Fake block
    block = Block()

# Generated at 2022-06-13 09:15:39.426009
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Scenario 1: no tags
    evaluation = Taggable.evaluate_tags(None, None, None)
    assert evaluation

    # Scenario 2: no tags, only_tags = always
    only_tags = ['always']
    evaluation = Taggable.evaluate_tags(only_tags, None, None)
    assert evaluation

    # Scenario 3: all tags, no skip_tags
    tags = ['all', 'a', 'b']
    skip_tags = None
    only_tags = dict()  # dict is used to emulate an empty list
    evaluation = Taggable.evaluate_tags(tags, skip_tags, only_tags)
    assert evaluation

    # Scenario 4: all tags, with skip_tags
    tags = ['all', 'a', 'b']
    skip_tags = ['never', 'c', 'd']


# Generated at 2022-06-13 09:15:47.768689
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # import needed to allow class to be resolved
    import ansible.playbook.role_include

    class MyTaggable(Taggable):
        # needed to make the class resolvable outside the class definition
        pass
    # create taggableinstance
    taggable = MyTaggable()
    # set tags property
    taggable.tags = ['always', 'foo']
    # test different selection scenarios
    all_vars = dict()
    only_tags = ['tagged', 'bar']
    skip_tags = ['tagged', 'bar']
    assert taggable.evaluate_tags(only_tags, skip_tags, all_vars) == False
    only_tags = ['tagged', 'bar']
    skip_tags = ['tagged', 'notfoo']

# Generated at 2022-06-13 09:15:58.243792
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task

    t = Task()
    only_tags=['tagged']
    skip_tags=['tagged']

    # test untagged
    assert t.evaluate_tags(only_tags, skip_tags, {}) == False

#    # test when tags specified but with no value
#    t.tags=[]
#    assert t.evaluate_tags(only_tags, skip_tags, {}) == False
#
#    # test when tags specified
#    t.tags = ['tagged']
#    assert t.evaluate_tags(only_tags, skip_tags, {}) == False
#
#    # test when skip_tags specified but with no value
#    t.tags = []
#    assert t.evaluate_tags(only_tags, [], {}) == False
#
#   

# Generated at 2022-06-13 09:16:07.805844
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        pass

    t = MyTaggable()

    # test case 1
    t.tags = [u'w1', u'a', u'1', u'b']
    assert t.evaluate_tags(only_tags=[u'w1'], skip_tags=['not1'], all_vars={})
    assert not t.evaluate_tags(only_tags=[u'w2'], skip_tags=[], all_vars={})
    assert not t.evaluate_tags(only_tags=[u'w1'], skip_tags=[u'a'], all_vars={})
    assert not t.evaluate_tags(only_tags=[u'w1'], skip_tags=[u'1'], all_vars={})

# Generated at 2022-06-13 09:16:16.035799
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    from ansible.template import Templar

    from ansible.vars.manager import VariableManager

    class TaggableDummyClass(Taggable):
        _allow_duplicates = FieldAttribute(isa='bool', default=True)
        _name             = FieldAttribute(isa='string')

        def __init__(self, name=None, loader=None, vault_pass=None):
            self._name = name
            self._loader = loader
            self._templar = Templar(loader=loader, shared_loader_obj=loader, vault_pass=vault_pass)
            self._ds = None
            self._metadata = None
            self.all_vars = VariableManager()


# Generated at 2022-06-13 09:16:22.640949
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Create a Taggable instance to test
    taggable = Taggable()

    # Set the tags attribute value
    taggable.tags = ['tag1', 'tag2']

    # Create all_vars variable
    all_vars = {}

    # Check that evaluate_tags returns True if the only_tags is set to 'all'
    only_tags = ['all']
    should_run = taggable.evaluate_tags(only_tags, [], all_vars)
    assert should_run

    # Check that evaluate_tags returns True if only_tags has a tag present in taggable
    only_tags = ['tag1']
    should_run = taggable.evaluate_tags(only_tags, [], all_vars)
    assert should_run

    # Check that evaluate_tags returns False if only_tags

# Generated at 2022-06-13 09:16:47.143027
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """ Test the method Taggable._evaluate_tags() """
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    class TestObj():
        tags = None
        _loader = None
        def _load_tags(self, attr, ds):
            return ds

    p = Play().load({'name': 'foobar', 'hosts': 'all'}, loader=None, variable_manager=None)
    r = Role().load({'name': 'foobar', 'hosts': 'all'}, loader=None, variable_manager=None)
    b = Block().load({'name': 'foobar', 'hosts': 'all'}, loader=None, variable_manager=None, play=p)


# Generated at 2022-06-13 09:16:56.712065
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    m = Taggable()
    d = dict(only_tags=[], skip_tags=[])
    assert m.evaluate_tags(d['only_tags'], d['skip_tags'], dict(tags=[]))
    assert m.evaluate_tags(d['only_tags'], d['skip_tags'], dict(tags=['1']))
    assert m.evaluate_tags(d['only_tags'], d['skip_tags'], dict(tags=['always']))
    assert m.evaluate_tags(d['only_tags'], d['skip_tags'], dict(tags=['always', 'never']))

    assert m.evaluate_tags(d['only_tags'], d['skip_tags'], dict(tags=['always', '1']))

# Generated at 2022-06-13 09:17:08.044851
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self, tags=None):
            self._tags = tags if tags else []
            self._loader = None
        def __eq__(self, other):
            return self._tags == other._tags

# Generated at 2022-06-13 09:17:20.414224
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.vars import VariableManager

    class TestItem(Taggable):
        pass

    test_item = TestItem()
    test_item._loader = None
    test_item.tags = ['foo', 'bar']

    only_tags = ['foo', 'bar']
    skip_tags = None
    all_vars = dict()
    variable_manager = VariableManager(loader=None, inventory=None)
    variable_manager._extra_vars = dict()
    variable_manager.set_nonpersistent_facts(all_vars)
    assert test_item.evaluate_tags(only_tags, skip_tags, variable_manager.get_vars(play=None))

    skip_tags = ['bar']

# Generated at 2022-06-13 09:17:30.436630
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    fake_loader = None
    fake_tags = set([ 'always', 'testing' ])
    fake_items = [ "fake_item1", "fake_item2"]
    fake_vars = dict()

    """ Tests Taggable.evaluate_tags() - always and not skipped """
    config = Taggable()
    config._loader = fake_loader
    config.tags = fake_tags
    assert config.evaluate_tags(only_tags=[], skip_tags=[], all_vars=fake_vars)

    """ Tests Taggable.evaluate_tags() - always and not skipped """
    config = Taggable()
    config._loader = fake_loader
    config.tags = []
    assert config.evaluate_tags(only_tags=[], skip_tags=[], all_vars=fake_vars)


# Generated at 2022-06-13 09:17:34.792767
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MyTaggable(Taggable):
        def __init__(self):
            pass

    myTaggable = MyTaggable()

    # with no tags
    myTaggable.tags = None
    assert myTaggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars=None) == True
    assert myTaggable.evaluate_tags(only_tags=set(), skip_tags=set(), all_vars=None) == True
    assert myTaggable.evaluate_tags(only_tags=None, skip_tags=set(), all_vars=None) == True
    assert myTaggable.evaluate_tags(only_tags=set(['foo', 'bar']), skip_tags=set(['foobar']), all_vars=None) == True
    assert my

# Generated at 2022-06-13 09:17:41.135822
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert Taggable() == Taggable()
    assert Taggable(tags=['my_tag']) != Taggable()
    assert Taggable(tags=['my_tag']) != Taggable(tags=['your_tag'])
    assert Taggable(tags=['my_tag']) == Taggable(tags=['my_tag'])
    assert Taggable(tags=['my_tag']) != Taggable(tags=['my_tag', 'your_tag'])
    assert Taggable(tags=['my_tag', 'your_tag']) == Taggable(tags=['my_tag', 'your_tag'])

# Generated at 2022-06-13 09:17:46.853981
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Create a t in order to test the method evaluate_tags
    t = Taggable()

    # Create the result of evaluate_tags
    res = t.evaluate_tags([], [], {})

    # Create the expected result
    exp_res = True

    # Compare the result with the expected result
    assert res == exp_res

# Generated at 2022-06-13 09:17:54.973111
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_instance = Taggable()
    test_instance.tags = []

    assert test_instance.evaluate_tags(None, None, dict()) == True
    assert test_instance.evaluate_tags(['all'], None, dict()) == True
    assert test_instance.evaluate_tags(['tagged'], None, dict()) == False
    assert test_instance.evaluate_tags(['test'], None, dict()) == False
    assert test_instance.evaluate_tags(['all'], ['never'], dict()) == True
    assert test_instance.evaluate_tags(['all'], ['always'], dict()) == False
    assert test_instance.evaluate_tags(['tagged'], ['never'], dict()) == False
    assert test_instance.evaluate_tags(['tagged'], ['always'], dict()) == False

    test_

# Generated at 2022-06-13 09:17:56.338070
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # TODO
    pass

# Generated at 2022-06-13 09:18:31.553206
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    myplay1 = Play().load(dict(
        name = "myplay",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='/bin/false'))
        ]
    ), loader=DataLoader())

# Generated at 2022-06-13 09:18:43.428469
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.base import Base
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.lookup_plugin import LookupBase
    from ansible.playbook.role.task import Task as RoleTask
    from ansible.playbook.role.defaults import Defaults
    from ansible.playbook.role.meta import RoleMeta
    from ansible.playbook.role.include import RoleInclude

# Generated at 2022-06-13 09:18:53.081696
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    class MockTaggable:
        def __init__(self):
            self.tags = None
            self._loader = None
            self.untagged = frozenset(['untagged'])

    class TaggableTest(unittest.TestCase):
        def test_evaluate_tags(self):
            def _test(tags, opts, expect):
                t = MockTaggable()
                t.tags = tags
                actual = t.evaluate_tags(opts['only_tags'], opts['skip_tags'], {})
                self.assertEqual(actual, expect)
            only_tags = ['only1', 'only2']
            skip_tags = ['skip1', 'skip2']

# Generated at 2022-06-13 09:19:02.749470
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Taggable object used to test evaluate_tags
    class FakeTaggable(Taggable):
        def __init__(self):
            self._tags = None
            self.tags = None
    
        # Dummy method to make this class look like a valid Ansible class
        def get_name(self):
            return self
    
    # Create the Taggable instance
    tag = FakeTaggable()
    
    # Create a dummy vars dict to be used
    vars = {"test1": True, "test2": "hello"}
    
    # Create list of different scenarios to test

# Generated at 2022-06-13 09:19:13.371389
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_class = Taggable()
    test_obj = {
        "one": 1,
        "two": "{{ two }}",
    }
    test_only_tags = {
        "cylinder",
        "rectangle"
    }
    test_skip_tags = {
        "circle"
    }

    # Setup object
    test_class._loader = "test"
    test_class.tags = [
        "cylinder",
        "{{ cylinder_or_rectangle }}",
        "{{ one }}",
        [
            "cylinder",
            "circle"
        ],
        "{{ two }}",
        [
            "{{ one }}"
        ]
    ]
    # Setup Templar
    templar = Templar(loader=test_class._loader, variables=test_obj)
    test_class

# Generated at 2022-06-13 09:19:27.292518
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    def test(only_tags, skip_tags, tags):
        # The class definition of Taggable is spread out over several
        # different classes (and could change). So let's just use a
        # minimal definition for this unit test
        class Taggable:
            _tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)
            def __init__(self, tags):
                self.tags = tags
            def evaluate_tags(self, only_tags, skip_tags, all_vars):
                if self.tags:
                    templar = Templar(loader=None, variables=None)
                    tags = templar.template(self.tags)
                    _temp_tags = set()
                    for tag in tags:
                        if isinstance(tag, list):
                            _temp_

# Generated at 2022-06-13 09:19:39.294491
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    inventory = Inventory('localhost,')
    vars_mgr = VariableManager(loader=None, inventory=inventory)

    task_obj = Taggable()
    task_obj._loader = None
    task_obj._role = None
    task_obj.name = 'task_name'

    # Test case 1: tags as a string
    tags = 'tag1, tag2'

    # Test case 1.1: only_tags, skip_tags are not specified
    only_tags = None
    skip_tags = None
    should_run = task_obj.evaluate_tags(only_tags, skip_tags, vars_mgr._vars)
    assert(should_run == True)

    # Test case 1.2: only_tags is specified


# Generated at 2022-06-13 09:19:47.094675
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Create a Taggable object
    class DummyTaggable(Taggable):
        _valid_tags = (set(string_types))
    obj = DummyTaggable()

    # Create tag variables
    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3', 'tag4']
    all_vars = {'tag_var': ['tag1', 'tag2', 'tag3', 'tag4']}

    # Create tags
    obj.tags = ['tag1', 'tag2']
    # Evaluate tags
    should_run = obj.evaluate_tags(only_tags, skip_tags, all_vars)
    assert should_run == True, "Tagged items should run."

    # Create tags
    obj.tags = ['tag3', 'tag4']
    # Evaluate

# Generated at 2022-06-13 09:19:56.517858
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    # init the obj
    block    = Block()
    task     = Task()
    task._parent = block
    block._parent = block
    only_tags = set()
    skip_tags = set()
    all_vars  = dict()
    block_tags  = None
    task_tags  = None

    # test when both block and task are 'untagged'
    result = task.evaluate_tags(only_tags, skip_tags, all_vars)
    assert(result is True)

    # test when block is 'untagged' and task is 'tagged'
    task_tags = set(['test_tag'])
    result = task.evaluate_tags(only_tags, skip_tags, all_vars)

# Generated at 2022-06-13 09:20:06.103312
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # all_vars should not be empty
    all_vars = {}

    # try a play
    play = Play()
    play._tags = ['test1','test2','test3','test4','test5']
    only_tags = ['test1','test3','test4']
    skip_tags = ['test2','test5']
    try:
        is_to_run = play.evaluate_tags(only_tags, skip_tags, all_vars)
        assert is_to_run == True
    except AnsibleError as e:
        print('failed to run %s' % play._name)

    # try a task
    task = Task()
    task._tags = ['test1','test2','test3','test4','test5']
    only_tags = ['test1','test3','test4']
    skip

# Generated at 2022-06-13 09:21:07.194582
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    import sys
    import unittest
    import tempfile
    import textwrap

    sandbox_path = tempfile.mkdtemp()
    if not os.path.isdir(sandbox_path):
        os.makedirs(sandbox_path)

    sys.path.insert(0, sandbox_path)

    from ansible.errors import AnsibleError
    from ansible.template import Templar

    class MyTaggable(Taggable):

        def __init__(self, loader):
            self._loader = loader

    def test_evaluate_tags(self, only_tags, skip_tags, current_tags, expected_result):

        my_taggable = MyTaggable(self.loader)
        my_taggable.tags = current_tags


# Generated at 2022-06-13 09:21:15.048461
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import PlayBook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.inventory import Inventory
    import os

    class FakeVarsModule():
        def __init__(self,vars_ansible_content):
            self.content = vars_ansible_content

        def get_vars(self,loader,path,templar,strict):
            content = loader.load_from_file(path)
            self.content.update(content)
            return content

    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 09:21:26.544840
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MyTaggable(Taggable):

        _tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)

    # run all
    only_tags = []
    skip_tags = []
    should_run = MyTaggable(tags=[]).evaluate_tags(only_tags, skip_tags, {})
    assert should_run is True

    should_run = MyTaggable(tags=["tag1"]).evaluate_tags(only_tags, skip_tags, {})
    assert should_run is True

    # run tagged (tag1)
    only_tags = ["tagged"]
    skip_tags = []
    should_run = MyTaggable(tags=[]).evaluate_tags(only_tags, skip_tags, {})
    assert should_run is False

# Generated at 2022-06-13 09:21:40.786702
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    class TestTaggable(Taggable):
        def __init__(self,**kwargs):
            super(TestTaggable,self).__init__(**kwargs)

    '''
    test_Taggable_evaluate_tags:
    '''
    tt = TestTaggable(tags=[u'foo','bar','baz','qux','quux','corge','grault','garply','waldo','fred','plugh','xyzzy'])
    assert tt.evaluate_tags(only_tags=set(['foo','bar','baz']), skip_tags=set(['foo','bar','baz']), all_vars={}) == False  # tasks that match both "only_tags" and "skip_tags" are skipped

# Generated at 2022-06-13 09:21:49.227037
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = []
    skip_tags = []
    all_vars = {}
    tags = []

    taggable = Taggable()
    taggable.tags = tags

    assert taggable.evaluate_tags(only_tags, skip_tags, all_vars) is True

    tags = ['tags1', 'tags2']
    taggable.tags = tags
    only_tags = ['tagged']
    assert taggable.evaluate_tags(only_tags, skip_tags, all_vars) is True

    skip_tags = ['tagged']
    assert taggable.evaluate_tags(only_tags, skip_tags, all_vars) is False

    skip_tags = []
    only_tags = []

# Generated at 2022-06-13 09:21:55.440899
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    t = Task()
    assert t.evaluate_tags(['tagged'],'', {})
    assert t.evaluate_tags(['tagged'],['tagged'], {})
    assert t.evaluate_tags(['tagged'],['always', 'tagged'], {})
    assert t.evaluate_tags([],['always'], {})
    assert t.evaluate_tags(['tagged'],['always'], {})
    assert t.evaluate_tags(['tagged'],['always', 'tagged'], {}) == False
    assert t.evaluate_tags(['tagged'],['always', 'tagged'], {}) == False
    assert t.evaluate_tags(['tagged'],['never', 'tagged'], {}) == False
    assert t.evaluate

# Generated at 2022-06-13 09:22:05.116147
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Instanciate the object to test
    obj = Taggable()

    # Set the object's tags attribute
    tags = {'test1', 'test2'}
    obj.tags = tags

    # Set the object's untagged attribute
    untagged = {'untagged'}
    obj.untagged = untagged

    # Check that the method evaluate_tags returns True
    # if the "only_tags" parameter is empty and
    # the "skip_tags" parameter is empty ("only_tags" and "skip_tags" are the parameters of the method)
    only_tags = []
    skip_tags = []
    all_vars = {}
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars)

    # Check that the method evaluate_tags returns False
    # if the "only_tags

# Generated at 2022-06-13 09:22:18.595381
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''unit test for method evaluate_tags of class Taggable
    '''

    # initialization
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

    # instantiate objects
    block = Block()
    task = Task()
    handler = Handler()
    role = Role()
    play = Play()
    all_vars = dict()
    only_tags = list()
    skip_tags = list()


    # test case 1:
    # set tags of block
    block.tags = ["1", 2, 3]
    # set tags of task
    task.tags = ["4", 5, 6]
    # evaluate tags
   

# Generated at 2022-06-13 09:22:29.663246
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import PlayBase

    task1 = PlayBase()
    task1.tags = ['never', 'skip']
    
    task2 = PlayBase()
    task2.tags = ['skip']

    task3 = PlayBase()
    task3.tags = ['a', 'b']

    task4 = PlayBase()
    task4.tags = ['always', '1', '2']

    task5 = PlayBase()

    print(task1.evaluate_tags(only_tags=['a', 'b', 'c'], skip_tags=['skip', 'a']))
    print(task2.evaluate_tags(only_tags=['a', 'b', 'c'], skip_tags=['skip', 'a']))

# Generated at 2022-06-13 09:22:39.321161
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Testing with hosts
    hosts = [
        '127.0.0.1',
        '127.0.0.2',
        '127.0.0.3',
    ]
    host_objects=[]

    import ansible.inventory
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    for host in hosts:
        host_objects.append(Host(name=host))

    local_group = Group(name='local')
    local_group.add_host(host_objects[0])
    local_group.add_host(host_objects[1])

    internet_group = Group(name='internet')