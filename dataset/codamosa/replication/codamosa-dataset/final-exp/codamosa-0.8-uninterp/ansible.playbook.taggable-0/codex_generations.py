

# Generated at 2022-06-13 09:13:20.914166
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Task(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # all values are none
    t, only_tags, skip_tags, all_vars = Task([]) , None, None, None
    assert t.evaluate_tags(only_tags, skip_tags, all_vars) == True

    # only_tags is specified
    only_tags, skip_tags, all_vars = ['tag1', 'tag2'], None, None
    t, only_tags, skip_tags, all_vars = Task(['tag1']), only_tags, skip_tags, all_vars
    assert t.evaluate_tags(only_tags, skip_tags, all_vars) == True

    # skip_tags is specified
    only_tags, skip_tags, all_v

# Generated at 2022-06-13 09:13:29.303746
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = None
    skip_tags = None
    all_vars = None
    temp_Taggable = Taggable()
    temp_Taggable.tags = ['all', 'test']
    assert( True == temp_Taggable.evaluate_tags(only_tags, skip_tags, all_vars) )

    skip_tags = ['all']
    assert( True == temp_Taggable.evaluate_tags(only_tags, skip_tags, all_vars) )

    skip_tags = ['test']
    assert( False == temp_Taggable.evaluate_tags(only_tags, skip_tags, all_vars) )

    skip_tags = None
    only_tags = ['all']

# Generated at 2022-06-13 09:13:39.256762
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ta = Taggable()
    # Test case 1: no tag options
    assert ta.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) == True
    # Test case 2: only only_tags is specified and matches a tag
    assert ta.evaluate_tags(only_tags=['a'], skip_tags=[], all_vars={'tags':['a']}) == True
    # Test case 3: only only_tags is specified and does not match a tag
    assert ta.evaluate_tags(only_tags=['a'], skip_tags=[], all_vars={'tags':['b']}) == False
    # Test case 4: only skip_tags is specified and matches a tag

# Generated at 2022-06-13 09:13:51.690154
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    # Block: skip with tags
    block = Block()
    block.only_tags = ['nonexistent']
    block.skipped_tags = ['never']
    # Task: has tags
    task1 = Task()
    task1.tags = ['never']
    task1.only_tags = ['nonexistent']
    task1.skipped_tags = ['never']
    # Task: untagged
    task2 = Task()
    task2.only_tags = ['never']
    task2.skipped_tags = ['never']
    # Task: has tags that don't match
    task3 = Task()
    task3.tags = ['maybenexttime']
    task3.only_tags = ['never']
    task

# Generated at 2022-06-13 09:14:03.032923
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # define a new class inheriting from Taggable
    class MyTaggable(Taggable):
        pass

    myobj = MyTaggable()

    myobj.tags = ['r1', 'r2']
    assert myobj.evaluate_tags([], [], {})

    myobj.tags = ['never', 'r1', 'r2']
    assert not myobj.evaluate_tags([], [], {})

    myobj.tags = ['r1', 'r2']
    assert myobj.evaluate_tags(['r2'], [], {})

    myobj.tags = ['r1', 'r2']
    assert myobj.evaluate_tags(['r1'], [], {})

    myobj.tags = ['r1', 'r2']

# Generated at 2022-06-13 09:14:11.014982
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags  = ['tag1', 'tag2', 'tag3', 'tag4']
    skip_tags  = ['tag5', 'tag6', 'tag7', 'tag11', 'tag12', 'tag13']
    all_vars   = {'tag_prefix': 'tag'}
    taggable   = Taggable()
    tags       = set()

    # Should run, empty tags
    taggable._tags = list()
    assert(taggable.evaluate_tags(only_tags, skip_tags, all_vars))

    # Should run, match all tags
    taggable._tags = ['all']
    assert(taggable.evaluate_tags(only_tags, skip_tags, all_vars))

    # Should run, match always
    taggable._tags = ['always']

# Generated at 2022-06-13 09:14:20.187426
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' this is the unit test for class Taggable evaluate_tags method '''

    # Export to work inside Ansible, import to work outside Ansible
    import sys
    modpath = sys.modules[__name__].__file__
    moddir = os.path.dirname(modpath)
    sys.path.insert(0, moddir)
    from ansible.plugins.loader import get_all_plugin_loaders

    # Get module_loader for testing
    for loader_name in get_all_plugin_loaders():
        mod_path = __name__.split('.')
        mod_path[-1] = loader_name
        try:
            module_loader = import_module('.'.join(mod_path))
        except ImportError:
            continue


# Generated at 2022-06-13 09:14:32.745481
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    #  create instances for testing
    class Test(Taggable):

        def __init__(self, tags=None):
            self.tags = tags

    # only_tags = {'all', 'always'}
    def test1():
        this = Test()
        # must_be_true
        res = this.evaluate_tags(set(['all', 'always']), set(), dict())
        if not res:
            raise AssertionError

    # only_tags = {'all', 'always'}, skip_tags = {'all', 'never'}
    def test2():
        this = Test(tags=['always'])
        # must_be_true
        res = this.evaluate_tags(set(['all', 'always']), set(['all', 'never']), dict())
        if not res:
            raise

# Generated at 2022-06-13 09:14:36.497152
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self):
            pass
        def _load_tags(self, attr, ds):
            return ds

    test_taggable = TestTaggable()

    # Test tags which contain only tags
    test_taggable.tags = ['tag1', 'tag2', 'tag3']
    only_tags = ['tag1', 'tag2', 'tag3']
    skip_tags = []
    all_vars = []

    assert test_taggable.evaluate_tags(only_tags, skip_tags, all_vars) is True

    only_tags = ['tag1', 'tag2', 'tag3', 'tag4']
    skip_tags = []
    all_vars = []


# Generated at 2022-06-13 09:14:45.293332
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # create test objects
    class TestObject(Taggable): 
        def __init__(self, tags=None, only_tags=None, skip_tags=None, all_vars=None):
            self.tags = tags
            self.only_tags = only_tags
            self.skip_tags = skip_tags
            self.all_vars = all_vars 

    # create test objects
    # (tags, only_tags, skip_tags, all_vars, expected result)

# Generated at 2022-06-13 09:15:04.867006
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.play_context import PlayContext
    from ansible.utils import context_objects as co

    base = Base()
    co.set(base, 'vars', dict())
    p = PlayContext()
    # Test case 1
    # Tags is not specified, and skip_tags is empty list. should_run should return True
    base.tags = None
    base.evaluate_tags(None, [], {})
    assert (base.evaluate_tags(None, [], {}) == True)
    # Test case 2
    # Tags is not specified, only_tags is empty list. should_run should return True
    base.tags = None
    base.evaluate_tags([], None, {})
    assert (base.evaluate_tags([], None, {}) == True)

# Generated at 2022-06-13 09:15:16.190113
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.attribute import Attribute

    # Create a mock attribute dict
    attribute_dict = dict(
        _only_tags    = set(),
        _skip_tags    = set(),
        _tags         = list(),
        _loader       = None,
        _all_vars     = dict()
    )
    # Create a mock Taggable class with the dict we just created
    my_tag = Taggable(**attribute_dict)

    # Define the test cases of the method

# Generated at 2022-06-13 09:15:25.922862
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class foo(Taggable):
        pass
    test = foo()
    assert test.evaluate_tags(only_tags=[], skip_tags=[], all_vars={ 1 : "bar", 2 : "baz"})
    assert not test.evaluate_tags(only_tags=['something'], skip_tags=[], all_vars={ 1 : "bar", 2 : "baz"})
    assert not test.evaluate_tags(only_tags=['something', 'something_else'], skip_tags=[], all_vars={ 1 : "bar", 2 : "baz"})
    assert test.evaluate_tags(only_tags=[], skip_tags=['something'], all_vars={ 1 : "bar", 2 : "baz"})

# Generated at 2022-06-13 09:15:36.589820
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude

    ti = TaskInclude()
    ti._attributes = dict()
    ti._parent = dict()
    ti.tags = ['tag1']

    only_tags = ['tag1']
    skip_tags = []
    assert(ti.evaluate_tags(only_tags, skip_tags, dict()))

    only_tags = ['tag1', 'tag2']
    skip_tags = []
    assert(ti.evaluate_tags(only_tags, skip_tags, dict()))

    only_tags = ['tag2']
    skip_tags = []
    assert(not ti.evaluate_tags(only_tags, skip_tags, dict()))

    only_tags = []
    skip_tags = ['tag1']

# Generated at 2022-06-13 09:15:52.045543
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    loader = object()
    all_vars = dict()

    tags = ['a', 'b']
    only_tags = ['b', 'tagged']
    skip_tags = ['never', 'always']
    test_case_1 = Taggable()
    test_case_1._loader = loader
    test_case_1.tags = tags
    assert test_case_1.evaluate_tags(only_tags, skip_tags, all_vars)

    tags = ['never', 'a']
    only_tags = ['b', 'tagged']
    skip_tags = ['a', 'always']
    test_case_2 = Taggable()
    test_case_2._loader = loader
    test_case_2.tags = tags

# Generated at 2022-06-13 09:15:56.909133
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' this method will be used as unit test for method evaluate_tags of class Taggable '''
    from ansible.playbook.play import Play
    myplay = Play()
    myplay.tags = ['test3','test4','test5']
    # Test case when only_tags not None and skip_tags None
    only_tags = ['test1','test2','test3','test4','test5','test6']
    skip_tags = None
    all_vars = dict()
    myplay.evaluate_tags(only_tags, skip_tags, all_vars)
    assert myplay.tags == ['test3','test4','test5']
    # Test case when only_tags None and skip_tags not None
    only_tags = None

# Generated at 2022-06-13 09:16:00.114466
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    assert t.evaluate_tags(['a','b'],'always',{}) == True
    assert t.evaluate_tags('never',['never'],{}) == False

# Generated at 2022-06-13 09:16:08.274350
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert Taggable.evaluate_tags(None, None, None) == True
    assert Taggable.evaluate_tags(None, ['all'], None) == False
    assert Taggable.evaluate_tags(None, ['tagged'], None) == False
    assert Taggable.evaluate_tags(None, [], None) == True
    assert Taggable.evaluate_tags(None, ['all'], None) == False
    assert Taggable.evaluate_tags(None, ['always'], None) == True
    assert Taggable.evaluate_tags(None, ['never'], None) == False
    assert Taggable.evaluate_tags(['tagged'], ['tagged'], None) == False

# Generated at 2022-06-13 09:16:16.361084
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # importing is being done due to import cycle of module and class Taggable
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C

    # Test only_tags
    assert TaskInclude.evaluate_tags(['only_tag_task'], [], [], 'only_tag_task', DataLoader(), VariableManager(), [])
    assert not TaskInclude.evaluate_tags(['only_tag_task'], [], [], 'other_tag_task', DataLoader(), VariableManager(), [])
    assert not TaskInclude.evaluate_tags(['only_tag_task'], [], [], '', DataLoader(), VariableManager(), [])


# Generated at 2022-06-13 09:16:26.114082
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
  import unittest

  class TestTaggable(Taggable):
    pass

  """Verify if a task is marked as tagged, it will run with tags=[]"""
  test_taggable = TestTaggable(tags=[])
  # We are not running with any tag options, so the task should be run
  assert(test_taggable.evaluate_tags([],[],{}) == True)

  """Verify if a task is marked with a tag, it will run with only_tags=['that_tag']"""
  test_taggable = TestTaggable(tags=['that_tag'])
  # We are only running tasks tagged with 'that_tag', so the task should be run
  assert(test_taggable.evaluate_tags(['that_tag'], [], {}) == True)


# Generated at 2022-06-13 09:16:49.721516
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTaggable(Taggable):
        def __init__(self):
            self.tags = []

    test_object = MockTaggable()
    test_object.tags = []
    # test_object.skip_tags = None
    # test_object.only_tags = None
    # test_object.all_vars = []

    # test_object.only_tags = None
    # test_object.skip_tags = []
    # assert test_object.evaluate_tags(None, [], []) == True

    # test_object.only_tags = None
    # test_object.skip_tags = None
    # assert test_object.evaluate_tags(None, None, []) == True

    test_object.tags = ['all']
    test_object.only_tags = ['all']
    test

# Generated at 2022-06-13 09:16:58.020708
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class testTaggable(Taggable):
        def __init__(self):
            self._loader = "loader"
            self.tags = []
            self.name = "test"

    test_obj1 = testTaggable()
    test_obj2 = testTaggable()
    test_obj3 = testTaggable()
    test_obj4 = testTaggable()
    test_obj5 = testTaggable()
    test_obj6 = testTaggable()
    test_obj7 = testTaggable()
    test_obj8 = testTaggable()
    test_obj9 = testTaggable()

    test_obj1.tags = []
    test_obj2.tags = ['tag1', 'tag2']
    test_obj3.tags = ['tag1', 'tag2']
   

# Generated at 2022-06-13 09:17:09.260396
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    dataloader = DataLoader()
    templar = Templar(loader=dataloader)


# Generated at 2022-06-13 09:17:21.297328
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    loader = None
    all_vars = {}
    class MockLoader():
        pass
    class MockChild():
        ''' Mocks a child class of Taggable '''
        _loader = MockLoader()
        tags = []
        def evaluate_tags(self, only_tags, skip_tags, all_vars):
            return super(MockChild, self).evaluate_tags(only_tags, skip_tags, all_vars)
    tags = []
    result = MockChild().evaluate_tags(tags, tags, all_vars)
    assert result == True
    tags = ['a', 'b']
    result = MockChild().evaluate_tags(tags, tags, all_vars)
    assert result == True
    result = MockChild().evaluate_tags(tags, None, all_vars)
    assert result == True


# Generated at 2022-06-13 09:17:30.820908
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    import sys

    class TestTaggable(Taggable):
        def __init__(self):
            self._loader = None

    task = TestTaggable()
    # _tags is a list
    task.tags = ['tag1', 'tag2', 'tag3', 'tag4']
    only_tags = None
    skip_tags = None

    # Test case 1: ensure a task without any tags always runs
    assert task.evaluate_tags(only_tags, skip_tags, None)

    # Test case 2: ensure a task with all tags always runs
    task.tags = ['all', 'tag1', 'tag2', 'tag3', 'tag4']
    assert task.evaluate_tags(only_tags, skip_tags, None)

    # Test case 3: ensure a task with the always tag always runs

# Generated at 2022-06-13 09:17:40.343597
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    import sys
    libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, libpath)
    from ansible.playbook.task import Task

    task = Task()

    only_tags = ['test_tag', 'test_tag2']
    skip_tags = ['skip_tag', 'skip_tag2']

    # test that the task is executed
    task.tags = ['test_tag']
    task_run = task.evaluate_tags(only_tags, skip_tags, all_vars={})
    assert task_run

    task.tags = ['test_tag2']
    task_run = task.evaluate_tags(only_tags, skip_tags, all_vars={})

# Generated at 2022-06-13 09:17:51.529257
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' This is a unit test for method Taggable::evaluate_tags '''
    from ansible.playbooks import PlaybookInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    import ansible.constants as C

    # first, a Task without any tags
    task = Task()
    # we should run it when all tags are explicitely skipped
    assert task.evaluate_tags({}, ['all'], {}) == True
    # we should run it when all tags are explicitely skipped, except always
    assert task.evaluate_tags({}, ['all', 'always'], {}) == True
    # we should run it when all tags are explicitely skipped, except always

# Generated at 2022-06-13 09:18:06.246647
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test default, return True
    task = Taggable()
    assert task.evaluate_tags([], [], None) == True

    # Test if 'only_tags' argument is a non empty list and 'skip_tags' is
    # an empty list, return True
    task.tags = {'test'}
    assert task.evaluate_tags({'test'}, [], None) == True

    # Test if 'only_tags' argument is an empty list and 'skip_tags' is
    # a non empty list, return False
    task.tags = {'test'}
    assert task.evaluate_tags([], {'test'}, None) == False

    # Test if 'only_tags' argument is a non empty list with always tag
    # and 'skip_tags' is an empty list, return True

# Generated at 2022-06-13 09:18:14.213738
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    task = Taggable()
    task.tags = ["always"]
    assert task.evaluate_tags(["always"],[],{}) == True

    task.tags = ["never"]
    assert task.evaluate_tags(["all"],[],{}) == True

    task.tags = ["never"]
    assert task.evaluate_tags(["all"],[],{}) == True


    task.tags = ["never"]
    assert task.evaluate_tags(["all"],["never"],{}) == False


    task.tags = ["tag1"]
    assert task.evaluate_tags(["tag1"],[],{}) == True


    task.tags = ["tag1"]
    assert task.evaluate_tags(["tagged"],[],{}) == True


    task.tags = ["tag1"]

# Generated at 2022-06-13 09:18:25.647614
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Playbook
    from ansible.playbook.task import Task

    pb = Playbook()
    t1 = Task()
    t2 = Task()
    t3 = Task()
    t4 = Task()
    t5 = Task()

    t1._loader.set_basedir('./')
    t1.name = "Task1"
    play = pb.get_deps_for_host("all")[0]
    t1._parent = play
    t1.tags = ["tag1", "tag2"]
    t1_should_run = t1.evaluate_tags(['tag1'], ['tag2'], pb._basedir)
    assert t1_should_run is True

    t2.name = "Task2"
    play = pb.get_dep

# Generated at 2022-06-13 09:18:55.145534
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyTaggableObject(Taggable):
        pass

    obj_no_tags = DummyTaggableObject()

    assert obj_no_tags.evaluate_tags(only_tags=['tag1'], skip_tags=[], all_vars={}) == False
    assert obj_no_tags.evaluate_tags(only_tags=[], skip_tags=['tag1'], all_vars={}) == False
    assert obj_no_tags.evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=[], all_vars={}) == False
    assert obj_no_tags.evaluate_tags(only_tags=['tag2'], skip_tags=['tag1'], all_vars={}) == False

# Generated at 2022-06-13 09:19:04.477669
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableClass():
        def __init__(self, tags):
            self.tags = tags

    # task without tags
    task = TaggableClass(tags=[])

    # only_tags = ['all']
    only_tags = ['all', 'mock_tag']
    skip_tags = []
    all_vars = []

    # test case 1: only_tags = ['all']
    assert(True == Taggable.evaluate_tags(task, only_tags, skip_tags, all_vars))

    # test case 2: only_tags = ['all', 'mock_tag']
    assert(True == Taggable.evaluate_tags(task, only_tags, skip_tags, all_vars))

    # test case 3: only_tags = ['mock_tag']

# Generated at 2022-06-13 09:19:15.200483
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    r = Taggable()
    # это просто примеры из теста
    r._tags = ['always']
    assert r.evaluate_tags(None, ['never'], {}) == True

    r._tags = ['never']
    assert r.evaluate_tags(['always'], None, {}) == False

    r._tags = ['always']
    assert r.evaluate_tags(['never'], None, {}) == False

    r._tags = ['never']
    assert r.evaluate_tags(None, ['always'], {}) == True

    r._tags = ['never']
    assert r.evaluate_tags(None, ['always'], {}) == True

    r._tags = ['never']

# Generated at 2022-06-13 09:19:24.970520
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # test with only_tags
    t = Taggable()
    t._tags = 'test'
    assert t.evaluate_tags(['test'], '', {})
    assert not t.evaluate_tags(['not_test'], '', {})
    assert t.evaluate_tags(['true'], '', {})
    assert not t.evaluate_tags(['false'], '', {})
    assert t.evaluate_tags(['always'], '', {})
    assert t.evaluate_tags(['all'], '', {})
    assert not t.evaluate_tags(['all'], ['never'], {})
    # test should_run is False and then True
    assert not t.evaluate_tags(['false'], ['test'], {})

# Generated at 2022-06-13 09:19:36.745812
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    for class_type in [Task, RoleDefinition]:
        t = class_type()
        t.tags = []
        t.only_tags = []
        t.skip_tags = []
        assert t.evaluate_tags(t.only_tags, t.skip_tags, PlayContext())

        t.tags = dict(name='a')
        t.only_tags = []
        assert not t.evaluate_tags(t.only_tags, t.skip_tags, PlayContext())

        t.only_tags = dict(name='a')
        assert t.evaluate_tags(t.only_tags, t.skip_tags, PlayContext())


# Generated at 2022-06-13 09:19:45.602965
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    loader = DataLoader()
    var_manager = VariableManager()
    host = Host(name="foo")
    group = Group(name="bar")
    host.set_variable("ansible_python_interpreter","/usr/bin/python2.6")
    host.add_group(group)
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    inventory.add_host(host)

# Generated at 2022-06-13 09:19:55.624468
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Object to test
    taggable = Taggable()

    # Test that it is tagged
    taggable.tags = ['tag1']
    only_tags = ['tag1']
    skip_tags = []
    assert taggable.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars={}) == True

    # Test that it is tagged
    taggable.tags = ['tag1']
    only_tags = ['tag1', 'tag2']
    skip_tags = []
    assert taggable.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars={}) == True

    # Test that it is tagged
    taggable.tags = ['tag1']
    only_tags = ['tag2', 'tag1']
   

# Generated at 2022-06-13 09:20:05.441202
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTest(Taggable):
        pass

    testee = MyTest()

    testee._loader = None
    testee._ds = None

    testee.tags = []
    assert testee.evaluate_tags(None, None, {}) == True
    assert testee.evaluate_tags(None, [], {}) == True
    assert testee.evaluate_tags([], None, {}) == False
    assert testee.evaluate_tags([], [], {}) == True
    assert testee.evaluate_tags(['skipme'], ['skipme'], {}) == False
    assert testee.evaluate_tags(['skipme'], [], {}) == False
    assert testee.evaluate_tags([], ['skipme'], {}) == True

# Generated at 2022-06-13 09:20:13.493397
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # test data
    only_tag = ['tag1', 'tag2']
    skip_tag = ['tag3', 'tag4']
    all_vars = {'test':'test'}
    
    # test evaluate_tags where tags is defined
    tags = ['tag1', 'tag2']
    taggable_obj = Taggable()
    taggable_obj.tags = tags
    taggable_obj.all_vars = all_vars
    
    result = taggable_obj.evaluate_tags(only_tag, skip_tag, all_vars)
    assert result == True

    tags = ['tag3', 'tag4', 'tag5']
    taggable_obj.tags = tags

# Generated at 2022-06-13 09:20:24.652387
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os

    base_dir = os.path.dirname(os.path.dirname(__file__))
    dataloader = DataLoader()
    all_vars = VariableManager(loader=dataloader)
    all_vars._fact_cache = HostVars(
        _variable_manager=all_vars,
        _loader=dataloader
    )

    # test 'always' tag - always run
    #      'never' tag -

# Generated at 2022-06-13 09:21:30.902240
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest

    class Dummy:
        pass

    d = Dummy()
    d.tags = []
    d.evaluate_tags(only_tags=['all'], skip_tags=[], all_vars={})
    d.evaluate_tags(only_tags=[], skip_tags=['all'], all_vars={})
    d.evaluate_tags(only_tags=['never'], skip_tags=['always'], all_vars={})
    d.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars={})
    d.evaluate_tags(only_tags=['always'], skip_tags=['never'], all_vars={})
    d.evaluate_tags(only_tags=[], skip_tags=['never'], all_vars={})
    d

# Generated at 2022-06-13 09:21:43.517360
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    result = Base()._load_tags('', 'tag')
    assert result == ['tag']

    result = Base()._load_tags('', ['tag'])
    assert result == ['tag']

    result = Base()._load_tags('', 'tag1, tag2, tag3')
    assert result == ['tag1', 'tag2', 'tag3']

    result = Base()._load_tags('', [1, 2, 3])
    assert result == [1, 2, 3]

    result = Base()._load_tags('', True)

# Generated at 2022-06-13 09:21:57.062993
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    scriptlet = '''
- hosts: all
  gather_facts: no
  tasks:

  - name: Ensure iptables is running
    service: name=iptables state=running
    tags:
      - tagged
      - iptables

  - name: Ensure sshd is running
    service: name=sshd state=running
    tags:
      - tagged
      - sshd

  - name: Ensure ntp is installed
    yum: name=ntp state=installed
    tags:
      - ntp

  - name: Ensure ntp is running
    service: name=ntp state=running
    tags:
      - ntp
      - tagged
    '''

    import ansible.playbook
    from ansible.inventory.manager import InventoryManager

# Generated at 2022-06-13 09:22:04.772760
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class ClassTest(Taggable):
        def __init__(self):
            self.tags = []

    for i in range(10):
        test = ClassTest()

        test.tags.append("test1")
        test.tags.append("test2")

        only_tags = []
        skip_tags = []

        only_tags.append("test3")
        skip_tags.append("test1")

        if not test.evaluate_tags(only_tags, skip_tags, {}):
            print("test_Taggable_evaluate_tags: success")
            return

    print("test_Taggable_evaluate_tags: failed")


# Generated at 2022-06-13 09:22:18.462437
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MyTaggable(Taggable):

        # This is only here because the Taggable class needs to be instantiated
        # The test_Taggable_evaluate_tags function is called in the Taggable class above
        # The Taggable class is instantiated in the load function in the Play class
        # Therefore, the Play class needs to be instantiated.
        # The Play class needs a _loader and loader.path_dwim needs to be a string
        def __init__(self):
            self._loader = None

    only_tags = set()
    skip_tags = set()

    tags = set(['t1', 't2'])

    myTaggable = MyTaggable()
    myTaggable.tags = tags

# Generated at 2022-06-13 09:22:32.262003
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class DummyTaggable(Taggable):
        _tags = FieldAttribute(isa='list', default=[], listof=(string_types, int), extend=True)

        def __init__(self, tags=None, only_tags=None, skip_tags=None, all_vars=None):
            self._tags = tags
            self.only_tags = only_tags
            self.skip_tags = skip_tags
            self.all_vars = all_vars

    tags = ['always']
    only_tags = ['always']
    skip_tags = []
    all_vars = {}

    obj = DummyTaggable(tags, only_tags, skip_tags, all_vars)
    assert(obj.evaluate_tags(only_tags, skip_tags, all_vars))


# Generated at 2022-06-13 09:22:40.700187
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.block
    import ansible.utils.unsafe_proxy
    import yaml

    class MyClass(object):
        tags = ['first', 'second']

        def load_tags(self, value):
            return value

    obj = MyClass()
    # get access to protected class method
    obj.evaluate_tags = Taggable.evaluate_tags.__get__(obj)
    assert obj.evaluate_tags(['first'], [], []) == True
    assert obj.evaluate_tags(['first', 'second'], [], []) == True
    assert obj.evaluate_tags([], ['first'], []) == False
    assert obj.evaluate_tags([], ['second'], []) == False
    assert obj.evaluate_tags([], ['first', 'second'], []) == False
    assert obj

# Generated at 2022-06-13 09:22:50.865218
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible import constants as C

    class DummyTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # Empty tag
    obj = DummyTaggable(tags=[])
    assert obj.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) == True
    assert obj.evaluate_tags(only_tags=C.TAG_UNTAGGED, skip_tags=[], all_vars={}) == True
    assert obj.evaluate_tags(only_tags=[], skip_tags=C.TAG_UNTAGGED, all_vars={}) == False
    assert obj.evaluate_tags(only_tags=[], skip_tags=['no-such-tag'], all_vars={}) == True

    # Always tag
    obj = Dummy

# Generated at 2022-06-13 09:22:58.139361
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.included_file import IncludedFile

    # Tags used in tests
    tagA = 'tagA'
    tagB = 'tagB'

    # Set of tasks - to build play and test evaluate_tags()
    tasks = [
        Task(),
        Task(),
        Task(),
        Task(tags=[tagA]),
        Task(),
        Task(),
        Task(tags=[tagA, tagB]),
        Task(),
        Task(),
        Task(),
    ]

    # Set of tags to test evaluate_tags()

# Generated at 2022-06-13 09:23:05.863690
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    ansible_options = {
        'connection': 'local',
        'module_path': '/usr/share/ansible',
        'fork': 50,
        'remote_user': 'ansible',
        'private_key_file': '~/.ssh/id_rsa',
        'ssh_common_args': '',
        'ssh_extra_args': '',
        'sftp_extra_args': '',
        'scp_extra_args': '',
        'become': False,
        'become_method': 'sudo',
        'become_user': 'root',
        'verbosity': 5,
        'check': False,
    }