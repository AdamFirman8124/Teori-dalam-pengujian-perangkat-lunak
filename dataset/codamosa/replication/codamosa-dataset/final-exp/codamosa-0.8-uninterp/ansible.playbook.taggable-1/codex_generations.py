

# Generated at 2022-06-13 09:13:20.882484
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    import unittest

    class TestTaggable(Taggable):
        pass

    class TestTask(Task):
        pass

    class TestRole(Role):
        pass

    class TestBlock(Block):
        pass

    class TestPlayContext(PlayContext):
        pass

    class TestTaggableEvaluateTags(unittest.TestCase):

        def test_check_condition_invalid(self):
            block = TestBlock()
            result = block.evaluate_tags(only_tags=['not_valid'], skip_tags=['not_valid'], all_vars={})
            self.assertFalse

# Generated at 2022-06-13 09:13:29.280378
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test with only_tags
    t = Taggable()
    t._tags = ['tag1', 'tag2']
    assert t.evaluate_tags(only_tags=['tag1'], skip_tags=[], all_vars={})
    assert not t.evaluate_tags(only_tags=['tag4'], skip_tags=[], all_vars={})

    # Test with skip_tags
    t = Taggable()
    t._tags = ['tag1', 'tag2']
    assert not t.evaluate_tags(only_tags=[], skip_tags=['tag1'], all_vars={})
    assert t.evaluate_tags(only_tags=[], skip_tags=['tag4'], all_vars={})
    # Test with only_tags and skip_tags
    t = Taggable()
   

# Generated at 2022-06-13 09:13:39.215263
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeModule(object):
        def __init__(self):
            self._tags = ['always']
            self._loader = None
    mod = FakeModule()
    assert mod.evaluate_tags(['all', 'never'], ['never'], None) == False
    assert mod.evaluate_tags(['noexist'], ['never'], None) == False
    assert mod.evaluate_tags(['noexist', 'tagged'], ['never'], None) == True
    assert mod.evaluate_tags(['tagged'], ['never'], None) == True
    assert mod.evaluate_tags(['all'], ['never', 'always'], None) == False
    assert mod.evaluate_tags(['all'], ['never'], None) == True
    assert mod.evaluate_tags(['always'], ['never'], None) == True

# Generated at 2022-06-13 09:13:51.630743
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host

  # TODO: create a mock object for self._loader


# Generated at 2022-06-13 09:14:02.929643
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    class Fake_cls(Taggable):
        pass

    taggable = Fake_cls()
    assert taggable.tags == []

    taggable.tags = "tag1,tag2"
    assert taggable.tags == ['tag1','tag2']
    assert taggable.evaluate_tags(['tag1','tag3','tag4'], [], {}) == True
    assert taggable.evaluate_tags(['tag2','tag3','tag4'], [], {}) == True
    assert taggable.evaluate_tags(['tag3', 'tag4'], [], {}) == False
    assert taggable.evaluate_tags([], ['tag3', 'tag4'], {}) == True

# Generated at 2022-06-13 09:14:10.953126
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.yaml.objects import AnsibleSequence

    #############################################################
    # only_tags and skip_tags does not affect
    #############################################################
    # no tags
    obj1 = Taggable()
    result = obj1.evaluate_tags([], [], {})
    assert result == True

    # tags is untagged
    obj2 = Taggable()
    obj2.tags = ['untagged']
    result = obj2.evaluate_tags([], [], {})
    assert result == True

    # tags is empty
    obj3 = Taggable()
    obj3.tags = []
    result = obj3.evaluate_tags([], [], {})
    assert result == True

    # tags is not untagged
    obj4 = Taggable()

# Generated at 2022-06-13 09:14:19.730414
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.module_utils._text import to_bytes

    only_tags = [b'skip']
    skip_tags = [b'always']
    ansible_class = Taggable()
    ansible_class.tags = to_bytes("skip")
    assert not ansible_class.evaluate_tags(only_tags, skip_tags, {})

    only_tags = [b'always']
    skip_tags = [b'skip']
    ansible_class.tags = to_bytes("skip")
    assert not ansible_class.evaluate_tags(only_tags, skip_tags, {})

    only_tags = [b'skip']
    skip_tags = [b'skip']
    ansible_class.tags = to_bytes("skip")

# Generated at 2022-06-13 09:14:28.928061
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task as task
    import ansible.playbook.role as role
    import ansible.playbook.play as play

    # Create valid task instance
    t = task.Task()
    t.tags = ['tag1', 'tag2', 'tag3']

    # Check results for valid instance
    assert t.evaluate_tags(['tag1', 'tag3'], [], {}) == True
    assert t.evaluate_tags([], ['tag1', 'tag3'], {}) == False
    assert t.evaluate_tags(['tag1', 'tag3', 'always'], [], {}) == True
    assert t.evaluate_tags(['tag1', 'tag3', 'always'], ['always'], {}) == False

# Generated at 2022-06-13 09:14:36.584513
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyTaggable(Taggable):
        pass

    _all_vars = dict()
    _only_tags = ['tag1', 'tag2']
    _skip_tags = ['tag3', 'tag4']

    _taggable = DummyTaggable()

    assert not _taggable.evaluate_tags(None, None, _all_vars)

    _taggable.tags = ['tag1']
    assert _taggable.evaluate_tags(_only_tags, None, _all_vars)
    assert _taggable.evaluate_tags(_only_tags, _skip_tags, _all_vars)

    _taggable.tags = ['tag3']
    assert not _taggable.evaluate_tags(_only_tags, _skip_tags, _all_vars)

# Generated at 2022-06-13 09:14:45.346893
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    Result = []
    # Taggable with one tag
    class Taggable_OneTag(Taggable):
        pass
    testobj_onetag = Taggable_OneTag()
    testobj_onetag.tags = ['tag1']
    Result.append( testobj_onetag.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) )
    Result.append( testobj_onetag.evaluate_tags(only_tags=['tag1'], skip_tags=[], all_vars={}) )
    Result.append( testobj_onetag.evaluate_tags(only_tags=[], skip_tags=['tag1'], all_vars={}) )

# Generated at 2022-06-13 09:15:04.911462
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    testClass=Taggable()
    # test 1: no tag specified. Should run
    only_tags=[]
    skip_tags=[]
    assert(testClass.evaluate_tags(only_tags, skip_tags, {}))
    # test 2: tag set to never. Should not run
    only_tags=["test"]
    skip_tags=[]
    testClass.tags=["never"]
    assert(not testClass.evaluate_tags(only_tags, skip_tags, {}))
    # test 3: tag set to always. Should run
    only_tags=["test"]
    skip_tags=[]
    testClass.tags=["always"]
    assert(testClass.evaluate_tags(only_tags, skip_tags, {}))
    # test 4: tag set to test but we skip tag test. Should not run
    only

# Generated at 2022-06-13 09:15:16.242424
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    loader = DataLoader()
    print("Set up inventory\n")
    inventory = InventoryManager(loader=loader, sources=['localhost,', 'otherhost,'])
    host = Host(name='localhost')
    group = Group(name='group1')
    group.add_host(host)
    inventory.add_group(group)

# Generated at 2022-06-13 09:15:25.990426
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    map1 = {
        "tags": ["bar", "foo"],
        "only_tags": ["baz"]
    }
    map2 = {
        "tags": ["bar", "foo"],
        "skip_tags": ["baz"]
    }
    map3 = {
        "tags": ["bar", "foo"],
        "only_tags": ["baz"],
        "skip_tags": []
    }
    map4 = {
        "tags": ["bar", "foo"],
        "only_tags": ["baz"],
        "skip_tags": ["baz"]
    }
    map5 = {
        "tags": ["bar", "foo"],
        "only_tags": ["baz"],
        "skip_tags": ["foo"]
    }

# Generated at 2022-06-13 09:15:36.677509
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """ Method evaluate_tags of class Taggable: tests all possible scenarios

    """
    # Object definition
    class MockTaggable(Taggable):
        def __init__(self):
            super(MockTaggable, self).__init__()
            self._loader = None
            self.tags = None
    obj = MockTaggable()

    # Required for evaluations
    only_tags = []
    skip_tags = []
    all_vars = {}

    # Test 1 - default only_tags / skip_tags, no tags
    obj.tags = None
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars)
    # Test 2 - default only_tags / skip_tags, with tags
    obj.tags = ['a', 'b']

# Generated at 2022-06-13 09:15:52.117018
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    t = Task()

    # test skipping based on task tags
    t.tags = ['tag1']
    assert t.evaluate_tags(None, ['tag2'], None)
    assert t.evaluate_tags(None, ['tag1'], None)
    assert t.evaluate_tags(None, ['tag1', 'tag2'], None)
    assert t.evaluate_tags(None, ['tag2','tag1'], None)
    assert not t.evaluate_tags(None, [], None)

    # test running based on task tags
    t.tags = ['tag1', 'tag2']
    assert t.evaluate_tags(['tag1', 'tag2'], None, None)
    assert t.evaluate_tags(['tag2', 'tag1'], None, None)


# Generated at 2022-06-13 09:15:56.968309
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    def check_tags(item, only_tags, skip_tags, all_vars, expected):
        assert item.evaluate_tags(only_tags, skip_tags, all_vars) == expected

    t = Task.load(dict(name='test task', tags=['a', 'b', 'c']), play=dict(), loader=None, variable_manager=None)

    check_tags(t, only_tags=['a', 'b'], skip_tags=[], all_vars={}, expected=True)

    check_tags(t, only_tags=['a', 'b'], skip_tags=['c', 'd'], all_vars={}, expected=True)


# Generated at 2022-06-13 09:16:06.910537
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """Generates a test case for class Taggable."""
    # Note:
    # * Taggable is a mixin class.  For testing, we use a class MyTaggable
    #   that inherits from Taggable.
    # * Taggable uses the templating engine of Ansible.  For testing, we
    #   replace this engine with the lambda function my_template.
    # * Ansible variables are also templated.  For testing, we define all_vars
    #   as containing the single variable 'role', value 'web'.

    class my_template:
        def __init__(self, *args, **kwargs):
            pass
        def template(self, value, fail_on_undefined=False):
            return value



# Generated at 2022-06-13 09:16:15.167069
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play import Play
    
    all_vars = dict()
    play1 = Play().load(dict(
        hosts='localhost',
        gather_facts='no',
        tags=['hello','spam'],
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='Hello world'))),
        ]
    ), variable_manager=None, loader=None)

    # Test for an empty arg for only_tags, skip_tags
    assert play1.evaluate_tags(only_tags=None, skip_tags=None, all_vars=all_vars)

    # Test for an empty arg for only_tags, skip_tags, when the play has a "tagged" tag

# Generated at 2022-06-13 09:16:25.375724
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self, tags, only_tags, skip_tags):
            self.tags = tags
            self.only_tags = only_tags
            self.skip_tags = skip_tags

    # given: only_tags=A and tags=B
    # then:
    #       A=B -> should_run
    #       A inters B -> should_run
    #       A is not mutally exclusive with B -> should_run
    #       otherwise should not run
    #
    # given: skip_tags=C and tags=D
    # then:
    #       C=D -> should not run
    #       C inters D -> should not run
    #       C is not mutally exclusive with D -> should not run
    #       otherwise should run
    #
    #

# Generated at 2022-06-13 09:16:39.924939
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableObject(Taggable):
        def __init__(self, tags):
            self.tags = tags
            self._loader = None
    assert TaggableObject(tags=None).evaluate_tags(only_tags=None, skip_tags=None, all_vars={})
    assert TaggableObject(tags=None).evaluate_tags(only_tags=[], skip_tags=[], all_vars={})
    assert TaggableObject(tags=None).evaluate_tags(only_tags=[], skip_tags=None, all_vars={})
    assert TaggableObject(tags=None).evaluate_tags(only_tags=None, skip_tags=[], all_vars={})

# Generated at 2022-06-13 09:16:57.935482
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """Unit test for method _evaluate_tags of class Taggable"""
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class TestTask(Task, Taggable):
        def __init__(self, play, ds, all_vars):
            Task.__init__(self, play, ds)
            Taggable.__init__(self, play, ds)
            self.loader = DataLoader()
            self._variable_manager = VariableManager(loader=self.loader, inventory=play.get_inventory())
            self._variable_manager.set_play_context(play._play_context)
            self.vars = all_vars
            self.args = dict()

    # Test with no tags

# Generated at 2022-06-13 09:17:09.196050
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from collections import namedtuple

    Base = namedtuple('Base', ['tags', 'only_tags', 'skip_tags', 'result'])
    Case = namedtuple('Case', ['name', 'only_tags', 'skip_tags', 'result'])

    class T(Base, Taggable):
        pass

    def run(case):
        t = T(tags=case.name, only_tags=case.only_tags, skip_tags=case.skip_tags, result=False)

        assert(t.evaluate_tags(t.only_tags, t.skip_tags, {}) == case.result)

    # case: empty tags
    run(Case('', [], [], True))
    run(Case('', ['foo'], [], False))
    run(Case('', [], ['foo'], True))

   

# Generated at 2022-06-13 09:17:20.842117
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class testclass(Taggable):
        tags = []
    testobj = testclass()
    assert testobj.evaluate_tags(only_tags=['all'], skip_tags=[], all_vars={}) == True
    assert testobj.evaluate_tags(only_tags=['all'], skip_tags=['all'], all_vars={}) == False
    assert testobj.evaluate_tags(only_tags=['all'], skip_tags=['all', 'always'], all_vars={}) == False
    assert testobj.evaluate_tags(only_tags=['all'], skip_tags=['never'], all_vars={}) == True
    assert testobj.evaluate_tags(only_tags=['all'], skip_tags=['never', 'tagged'], all_vars={}) == True

# Generated at 2022-06-13 09:17:26.322554
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.clean import module_response

    class Mock(Taggable):
        pass

    class TestEvaluateTags(unittest.TestCase):
        ''' test evaluate_tags of class Taggable '''

        def test_evaluate_tags(self):
            only_tags = set()
            only_tags.add('webservers')
            skip_tags = set()
            skip_tags.add('databases')
            vars_data = dict()
            vars_data['tag_webservers'] = 'tagged_webservers'
            vars_data['tag_databases'] = 'tagged_databases'

            data = dict()

# Generated at 2022-06-13 09:17:33.459185
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTest(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # Tests for tagged tasks with no skip tags given
    domains = [
        [],  # No tags and no skip tags
        ['example'],
        ['example', 'example2'],
        ['example', 'example2', 'example3'],
    ]

    for d in domains:
        for i in range(0, len(d) + 1):  # Choosing combination (subset) of tags
            t = TaggableTest(d)
            assert t.evaluate_tags(d[:i], [], None)

    # Tests for tagged tasks with skip tags given

# Generated at 2022-06-13 09:17:41.500571
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:17:52.215260
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.template import Templar

    class TestTaggable(Taggable):
        def __init__(self, tags=None):
            self.tags = tags
            self._loader = None

    def load(attr, ds):
        return ds

    # test with simple cases
    t = TestTaggable()
    t._load_tags = load
    t.tags = ['tag2']
    assert t.evaluate_tags(['tag1', 'tag2'], ['tag3'], dict())
    assert t.evaluate_tags(['always'], ['tag3'], dict())
    assert t.evaluate_tags(['tag1', 'tag2'], ['never'], dict())

# Generated at 2022-06-13 09:17:58.083247
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # This test is for role "test_role02",
    # check the test/test_roles/test_role02/tasks/main.yml for more details

    # Init the object of Taggable
    class TaggableObject(Taggable):
        name = "TaggableObject"
        tags = ["xxx", "yyy", "zzz"]

    # OnlyTags:
    only_tags = set(['xxx', 'aaa', 'bbb', 'ccc'])
    to1 = TaggableObject()
    assert to1.evaluate_tags(only_tags, None, None)
    only_tags = set(['aaa', 'bbb', 'ccc'])
    to2 = TaggableObject()
    assert not to2.evaluate_tags(only_tags, None, None)

# Generated at 2022-06-13 09:18:08.014688
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3']
    all_vars = {'var1':'value1'}

    # data loader
    loader = DataLoader()

    # variable manager
    variable_manager = VariableManager()

    # inventory
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

    # create taggable object
    taggable = Taggable()
    taggable._loader = loader

    # test for evaluating tag1 for taggable object
    taggable.tags = ['tag1']

# Generated at 2022-06-13 09:18:08.565499
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert True

# Generated at 2022-06-13 09:18:46.548764
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # pylint: disable=unused-variable
    from ansible.playbook.role.definition import RoleDefinition

    fake_definition = RoleDefinition()

    fake_definition.tags = ['test1', 'test2']
    assert fake_definition.evaluate_tags(['test1'], ['test2'], {}) is True
    assert fake_definition.evaluate_tags(['test1'], ['test1'], {}) is False
    assert fake_definition.evaluate_tags(['test2'], ['test1'], {}) is True
    assert fake_definition.evaluate_tags(['test2'], ['test2'], {}) is False
    assert fake_definition.evaluate_tags(['test4'], ['test4'], {}) is False

# Generated at 2022-06-13 09:18:57.569785
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Init objects
    _item = None
    only_tags = ('tag_1', 'tag_2', 'tag_3', 'tagged', 'all', 'always')
    skip_tags = ('tag_1', 'tag_2', 'tag_3', 'tagged', 'all', 'always')
    all_vars = {'tag_1': 'tag_1', 'tag_2': 'tag_2', 'tag_3': 'tag_3'}

    # Test when item.tags is empty
    _item = Taggable()
    assert _item.evaluate_tags(only_tags, skip_tags, all_vars) == False

    # Test when item.tags is a list of tags with one tag
    _item = Taggable()
    _item.tags = ['tag_1']
    assert _item.evaluate

# Generated at 2022-06-13 09:19:06.091773
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    import os

    class TaggableClass(Taggable):
        _loader = True

        def __init__(self, tags):
            self.tags = tags

    class TestEvaluateTags(unittest.TestCase):

        def test_evaluate_tags(self):
            t = TaggableClass(tags=['first', 'second'])
            self.assertTrue(t.evaluate_tags(only_tags=['first'], skip_tags=['other'], all_vars={}))
            self.assertFalse(t.evaluate_tags(only_tags=['third'], skip_tags=['other'], all_vars={}))
            self.assertFalse(t.evaluate_tags(only_tags=['first'], skip_tags=['second'], all_vars={}))


# Generated at 2022-06-13 09:19:16.375355
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeVars(dict):
        fake_key = 'fake_value'
        list_with_fake_key = [ 'is_a_list', FakeVars.fake_key ]

    # monkey patch isdisjoint method for collections.Set
    import collections
    collections.Set.isdisjoint = lambda self, other: not bool(self & other)

    tags = ['fake_key', 'list_with_fake_key']

    fake_taggable = Taggable()
    fake_taggable._loader = 'fake_loader'
    fake_taggable.tags = tags

    # only_tags=['fake_value']
    assert fake_taggable.evaluate_tags(['fake_value'], [], FakeVars) is True
    # only_tags=['always', 'fake_value']

# Generated at 2022-06-13 09:19:28.293848
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MyTaggable(Taggable):
        pass

    a_task = MyTaggable()
    a_task.tags.append('tag1')
    a_task.tags.append('tag2')
    a_task.tags.append('tag3')

    assert a_task.evaluate_tags(only_tags=['tag4'], skip_tags=['tag5'], all_vars={}) == False
    assert a_task.evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=['tag5'], all_vars={}) == True
    assert a_task.evaluate_tags(only_tags=['tag1', 'tag2', 'tag3'], skip_tags=['tag5'], all_vars={}) == True

# Generated at 2022-06-13 09:19:40.197774
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext

    for obj in (Task(), Block(), Handler(), Role()):
        obj.tags = set()
        obj.tags.add('tagA')
        obj.tags.add('tagB')
        obj.tags.add('tagC')
        obj.tags.add('tagD')
        obj.tags.add('tagE')

        assert obj.evaluate_tags(None, None, {})

        assert obj.evaluate_tags(['tagA'], None, {})

# Generated at 2022-06-13 09:19:41.191696
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    pass

# Generated at 2022-06-13 09:19:52.556148
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' method evaluate_tags of class Taggable'''
    import ansible.plugins.loader
    import ansible.playbook.task_include
    import ansible.playbook.play_context
    import ansible.template
    from ansible.vars import VariableManager

    # only_tags = ['ubuntu', 'x86']
    only_tags = ['ubuntu']
    # skip_tags = ['all', 'always']
    skip_tags = []
    all_vars = VariableManager()

    # Print out Taggable.evaluate_tags for a test
    loaded_tags = False
    for name, obj in ansible.plugins.loader.all(class_only=True):
        if not hasattr(obj, "tags"):
            continue
        if name == "Include":
            tobj = obj()
            tobj._

# Generated at 2022-06-13 09:20:02.994158
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeDS:
        def __init__(self, tags):
            self.tags = tags
    class FakeTask(Taggable):
        def __init__(self, tags):
            self.tags = tags
            self._loader = None
    class FakeOptions:
        def __init__(self, only_tags, skip_tags):
            self.only_tags = only_tags
            self.skip_tags = skip_tags

    for t in ['', 'untagged', 'notag']:
        ds = FakeDS([])
        task = FakeTask([])
        assert(task.evaluate_tags(None, None, []) is True)
        assert(task.evaluate_tags([], None, []) is True)
        assert(task.evaluate_tags(None, [], []) is True)

# Generated at 2022-06-13 09:20:10.432773
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableObject(Taggable):
        def __init__(self, tags):
            self.tags = tags
            super(TaggableObject, self).__init__()
    only_tags = frozenset([])
    skip_tags = frozenset([])
    all_vars = dict()
    assert TaggableObject([]).evaluate_tags(only_tags, skip_tags, all_vars)
    assert not TaggableObject(['never']).evaluate_tags(only_tags, skip_tags, all_vars)
    assert not TaggableObject(['never']).evaluate_tags(only_tags, frozenset(['never']), all_vars)
    assert TaggableObject([]).evaluate_tags(frozenset(['tagged']), skip_tags, all_vars)

# Generated at 2022-06-13 09:21:13.243886
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # create a mock Taggable class, useful for unittesting of
    # non object-specific code
    class MockTaggable(Taggable):
        pass

    mt = MockTaggable()

    # define some tags (and their aliases) for testing purposes
    always_tags = ['always']
    all_tags = ['all']
    never_tags = ['never']
    tagged_tags = ['tagged']

    # define some default tags for testing purposes
    tags = ['tag1', 'tag2']

    # define some alternative tags for testing purposes
    tags_with_always = tags + always_tags
    tags_with_never = tags + never_tags

    # define some arbitrary tags for testing purposes
    tags_arb1 = ['arb1']
    tags_arb2 = ['arb2']
    tags_arb12 = tags_arb

# Generated at 2022-06-13 09:21:24.893239
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    testInst = Taggable()
    testInst.tags = ['tag1','tag2','tag3']
    assert testInst.evaluate_tags(None, None, None) == True
    assert testInst.evaluate_tags(['tag1'], None, None) == True
    assert testInst.evaluate_tags(['all'], None, None) == True
    assert testInst.evaluate_tags(['tag1','tag2'], None, None) == True
    assert testInst.evaluate_tags(['tag3'], None, None) == True
    assert testInst.evaluate_tags(['tag4'], None, None) == False
    assert testInst.evaluate_tags(['tag4','tag5'], None, None) == False
    assert testInst.evaluate_tags(None, ['tag1'], None) == True
    assert test

# Generated at 2022-06-13 09:21:39.334987
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.include import Include
    from ansible.playbook.handler import Handler

    t = Task()
    assert t.evaluate_tags(['a'], [], {}) == False
    assert t.evaluate_tags([], ['a'], {}) == True
    t.tags.append('a')
    assert t.evaluate_tags(['a'], [], {}) == True
    assert t.evaluate_tags(['a'], [], {'tags': ['b']}) == True
    t.tags.remove('a')
    t.tags.append('b')

# Generated at 2022-06-13 09:21:44.752482
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task_tagged_one = Task()
    task_tagged_one._ds = dict(tags=['tagged', 'untagged'])
    task_tagged_one._role_name = "test"

    task_tagged_two = Task()
    task_tagged_two._ds = dict(tags=['tagged', 'untagged'])
    task_tagged_two._role_name = "test"

    task_tagged_three = Task()
    task_tagged_three._ds = dict(tags=['tagged', 'untagged'])
    task_tagged_three._role_name = "test"

    task_untagged = Task()

# Generated at 2022-06-13 09:21:54.648041
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
	taggable = Taggable()
	assert taggable.evaluate_tags(['tag1, tag2'], ['tag3'], {}) == True
	assert taggable.evaluate_tags(['always'], ['tag3'], {}) == True
	assert taggable.evaluate_tags(['never'], ['tag3'], {}) == False
	assert taggable.evaluate_tags(['tag1', 'tag2'], ['tag3'], {}) == True
	assert taggable.evaluate_tags(['tag1', 'tag2'], ['never'], {}) == False

# Generated at 2022-06-13 09:22:05.040489
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    taggable = Taggable()

    # Test untagged object, that is, NON-tagged object
    assert taggable.evaluate_tags(only_tags=[], skip_tags=[])     == True
    assert taggable.evaluate_tags(only_tags=['tag1'], skip_tags=[])== False
    assert taggable.evaluate_tags(only_tags=[], skip_tags=['tag1']) == True
    assert taggable.evaluate_tags(only_tags=['tag1'], skip_tags=['tag1']) == False
    assert taggable.evaluate_tags(only_tags=['tag1'], skip_tags=['tag2']) == False
    assert taggable.evaluate_tags(only_tags=[], skip_tags=['tag2']) == True

# Generated at 2022-06-13 09:22:18.569599
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableClass(Taggable):
        def __init__(self):
            super(TaggableClass, self).__init__()
            self.tags = []

    taggable = TaggableClass()
    assert taggable.evaluate_tags(only_tags = None, skip_tags = None, all_vars = {}) == True

    taggable.tags = ['test']
    assert taggable.evaluate_tags(only_tags = None, skip_tags = None, all_vars = {}) == True

    assert taggable.evaluate_tags(only_tags = ['test'], skip_tags = None, all_vars = {}) == True
    assert taggable.evaluate_tags(only_tags = ['test'], skip_tags = ['test'], all_vars = {}) == False


# Generated at 2022-06-13 09:22:32.399114
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # set up
    class TestTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags
    test_taggable = TestTaggable(["always"])
    # should run
    actual_value1 = test_taggable.evaluate_tags(only_tags = ["always"], skip_tags = ["never"])
    actual_value2 = test_taggable.evaluate_tags(only_tags = ["always", "always_skip"], skip_tags = ["never"])
    actual_value3 = test_taggable.evaluate_tags(only_tags = ["all"], skip_tags = ["never"])
    actual_value4 = test_taggable.evaluate_tags(only_tags = ["tagged"], skip_tags = ["never"])
    # should not run
    actual

# Generated at 2022-06-13 09:22:40.750935
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    class DummyDatastructure:
        def __init__(self, loader, variables=None, task_vars=None):
            self._loader = loader
            if variables is not None:
                self._variables = variables
            if task_vars is not None:
                self._task_vars = task_vars

    class DummyLoader:
        class FakeVarsModule:
            def __init__(self, dict):
                self.dict = dict
            def get_vars(self, loader, play, host, task):
                return self.dict

        def __init__(self, vars_dict):
            self.vars_module = Dummy

# Generated at 2022-06-13 09:22:50.867300
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Create a Taggable instance
    import ansible.playbook.base
    class TaggableMixin(ansible.playbook.base.Base):

        __metaclass__ = ansible.playbook.base.AnsibleBase
        _tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)

    class TaggableClass(TaggableMixin, Taggable):
        pass

    taggable = TaggableClass()

    # Case 1: 'tagged' and 'untagged' in only_tags
    only_tags = ['tagged', 'untagged']
    assert taggable.evaluate_tags(only_tags, [], {}) == True

    # Case 2: 'all' in only_tags
    only_tags = ['all']
    assert tagg