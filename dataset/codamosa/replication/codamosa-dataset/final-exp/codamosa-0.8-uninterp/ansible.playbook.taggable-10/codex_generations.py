

# Generated at 2022-06-13 09:13:24.280456
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars

    play = Play().load({'hosts': 'all', 'roles': [{'role': 'common'}], 'tasks': [{'localhost': {'action': {'module': 'shell', 'args': 'ls'}}}], 'vars': {'test_tag': 'tagged'}}, variable_manager=combine_vars(None, {}), loader=None)

    assert play.tasks[0].evaluate_tags(only_tags=[], skip_tags=[], all_vars=play.get_vars())

# Generated at 2022-06-13 09:13:35.330696
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    import os

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    basedir = 'test/units/playbook/taggable'
    playbook = '%s/playbook.yml' % basedir
    play = Play.load(playbook, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:13:43.137859
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import random
    import sys
    import unittest

    from ansible.errors import AnsibleError
    from ansible.playbook.attribute import FieldAttribute


    class MyObjectTaggable(Taggable):
        _tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)


# Generated at 2022-06-13 09:13:57.499598
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableImpl(Taggable):
        pass

    task = TaggableImpl()
    task.tags = ['tag1', 'tag2']

    # Default values of always_run and tags are set to False and None
    should_run = task.evaluate_tags(only_tags='tag3', skip_tags='tag4', all_vars=None)
    assert (should_run == False)

    # Default values of always_run and tags are set to False and None
    should_run = task.evaluate_tags(only_tags='tag1', skip_tags='tag2', all_vars=None)
    assert (should_run == True)

    # Default values of always_run and tags are set to False and None

# Generated at 2022-06-13 09:14:12.106306
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_class = Taggable()
    # Test if the method evaluate_tags works as expected
    def test_isdisjoint(tags, only_tags, skip_tags, isdisjoint):
        test_class.tags = tags
        return test_class.evaluate_tags(only_tags, skip_tags, {}) == isdisjoint
    assert test_isdisjoint([], ['untagged'], [], True)
    assert test_isdisjoint([], [], ['untagged'], True)
    assert test_isdisjoint(['untagged'], [], [], True)
    assert test_isdisjoint([], ['never'], [], True)
    assert test_isdisjoint([], [], ['never'], True)

# Generated at 2022-06-13 09:14:25.277165
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Add the file to the module path
    import sys, os
    sys.path.append( os.path.abspath(os.path.dirname(__file__)) + '/../' )

    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude

    # Create a Taggable instance and call evaluate_tags()
    task = Task()
    task.tags = ['mytag']

    # Test the case when the task should run
    all_vars = {}
    only_tags = None
    skip_tags = None

# Generated at 2022-06-13 09:14:36.929990
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    templar = Templar(loader=dataloader, variables={})

    # untagged
    t = Taggable()
    t.tags = []
    assert t.evaluate_tags(['tagged'], [], {}) == True
    assert t.evaluate_tags(['tagged'], [], {}) == True
    assert t.evaluate_tags(['untagged'], [], {}) == True
    assert t.evaluate_tags(['always'], [], {}) == False
    assert t.evaluate_tags(['never'], [], {}) == True
    assert t.evaluate_tags([], [], {}) == True
    assert t.evaluate_tags([], ['tagged'], {}) == False
   

# Generated at 2022-06-13 09:14:41.357611
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTest(Taggable):
        def __init__(self, loader):
            self._loader = loader

    class FakeLoader():
        class FakeVarsManager():
            def __init__(self, variables):
                self.variables = variables

            def get_vars(self, play, task, host):
                return self.variables

        def __init__(self, variables):
            self.vars_manager = TaggableTest.FakeLoader.FakeVarsManager(variables)

    class FakeTask():
        def __init__(self, tags):
            self.tags = tags

    class FakePlay():
        def __init__(self, tags):
            self.tags = tags

    class FakePlaybook():
        def __init__(self, play_tags, task_tags):
            self.playbook

# Generated at 2022-06-13 09:14:53.002428
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task
    t = ansible.playbook.task.Task()
    t._loader = 'dummy'
    t.tags = ['foo', 'bar']
    assert t.evaluate_tags(only_tags=['foo'], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['foo', 'bar'], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['foo', 'bar'], skip_tags=['foo'], all_vars={}) == False
    assert t.evaluate_tags(only_tags=[], skip_tags=['foo'], all_vars={}) == True

# Generated at 2022-06-13 09:15:05.418324
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_input_only_tags = dict()
    test_input_only_tags['all'] = ['tag1', 'tag2']

    test_input_skip_tags = dict()
    test_input_skip_tags['all'] = ['tag3', 'tag4']

    test_all_vars = dict()

    test_instance = Taggable()

    test_instance.tags = [1]
    assert test_instance.evaluate_tags(test_input_only_tags, test_input_skip_tags, test_all_vars) == False

    test_instance.tags = ['tag1']
    assert test_instance.evaluate_tags(test_input_only_tags, test_input_skip_tags, test_all_vars) == True

    test_instance.tags = ['tag3']
    assert test_instance

# Generated at 2022-06-13 09:15:23.567765
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''
    taggable = Taggable()
    only_tags = ['tag1', 'tag2', 'tag3']
    skip_tags = ['tag4', 'tag5', 'tag6']
    all_vars = dict()
    taggable.tags = ['tag1', 'tag3', 'tag5']

    # Test with one tag in only_tags
    tag_in_only_tags = only_tags[0]
    taggable.tags.append(tag_in_only_tags)
    only_tags_single = [tag_in_only_tags]

    assert taggable.evaluate_tags(only_tags_single, skip_tags, all_vars) == True

    # Test with one tag in skip_tags
    tag_in_skip_tags = skip_tags[0]
    taggable

# Generated at 2022-06-13 09:15:28.915869
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    play_context = dict(tags={})
    all_vars = dict(tags={})
    only_tags = ['all']
    skip_tags = []
    task_include = TaskInclude(play_context=play_context, loader=None)
    assert task_include.evaluate_tags(only_tags, skip_tags, all_vars) is True

    play_context = dict(tags=['all'])
    all_vars = dict(tags=['all'])
    only_tags = ['all']
    skip_tags = []
    task_include = TaskInclude(play_context=play_context, loader=None)
    assert task_include.evaluate_tags(only_tags, skip_tags, all_vars) is True

    play_

# Generated at 2022-06-13 09:15:38.851615
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import copy

    class FakeTaggable(Taggable):
        pass

    obj = FakeTaggable()

    # first we test with a simple tag set
    all_vars = {}
    obj.tags = ['tag_case_1']
    only_tags = ['tag_case_1']
    skip_tags = []
    assert(obj.evaluate_tags(only_tags, skip_tags, all_vars))

    # now try with a tag set including an 'all'
    only_tags = ['all']
    assert(obj.evaluate_tags(only_tags, skip_tags, all_vars))

    # now try with a tag set including a 'never:true'
    obj.tags = ['never']
    assert(not obj.evaluate_tags(only_tags, skip_tags, all_vars))

   

# Generated at 2022-06-13 09:15:54.205618
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    tags1 = Taggable()
    tags1.tags = ['untagged']
    only_tags = ['all']
    skip_tags = ['never']
    all_vars = {}
    expected_to_run = True
    assert tags1.evaluate_tags(only_tags, skip_tags, all_vars) == expected_to_run

    tags2 = Taggable()
    tags2.tags = ['test_tag']
    expected_to_run = False
    assert tags2.evaluate_tags(only_tags, skip_tags, all_vars) == expected_to_run

    tags3 = Taggable()
    tags3.tags = ['test_tag']
    only_tags = ['tagged']
    expected_to_run = True

# Generated at 2022-06-13 09:16:04.449906
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.vars.manager import VariableManager

    class AnsibleModule:

        def __init__(self):
            pass

        def fail_json(self):
            pass

        def exit_json(self):
            pass

    class PlaybookExecutor:

        def __init__(self):
            self.playbook_dir = os.path.normpath('../../lib/ansible/playbooks')

    class Base:

        def __init__(self, config):
            self.loader = DataLoader()
            self.module_vars = dict()
            self.variable_manager = VariableManager(loader=self.loader,
                                                    use_task_vars=False,
                                                    inventory=None)

    class BaseRes:
        def __init__(self, base):
            self.hosts = dict()


# Generated at 2022-06-13 09:16:14.225440
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestTaggable(Taggable):
        def __init__(self):
            self._loader = None
            self._tags = list()

    # Default test values
    only_tags = list()
    skip_tags = list()
    all_vars = dict()

    test_obj = TestTaggable()

    # If we have no tags to run, we should not run this task
    assert test_obj.evaluate_tags(only_tags, skip_tags, all_vars) == False

    # Add tag which will not be found in any set of tags
    test_obj._tags = ['unique-tag']

    # If we run only tagged tasks and this isn't tagged, we should not run
    only_tags = ['tagged']

# Generated at 2022-06-13 09:16:24.782475
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTester(Taggable):
        tags = []
        def __init__(self, tags):
            self.tags = tags

    t = TaggableTester([])
    assert t.evaluate_tags(['all'])

    t = TaggableTester(['all'])
    assert t.evaluate_tags(['all'])

    t = TaggableTester(['tagged'])
    assert not t.evaluate_tags(['all'])

    t = TaggableTester(['tagged'])
    assert t.evaluate_tags(['tagged'])

    t = TaggableTester(['untagged'])
    assert not t.evaluate_tags(['tagged'])

    t = TaggableTester(['untagged'])

# Generated at 2022-06-13 09:16:27.433913
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    if __name__ == '__main__':
        import doctest
        doctest.testmod()

# Generated at 2022-06-13 09:16:41.227048
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import unittest
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    import ansible.constants as C

    class TestTaggableEvaluateTags(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_task_evaluate_tags(self):

            # a task without tags
            task_no_tags = Task()
            self.assertEqual(True, task_no_tags.evaluate_tags(None, None, None))

            # a task with tags
            task_tags = Task()
            task_tags.tags = ['tag1', 'tag2']

# Generated at 2022-06-13 09:16:49.426259
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.play_context import PlayContext
    context = PlayContext()

    class TestTask(Taggable):

        def __init__(self, tags):
            self.tags = tags

    class TestPlay:
        def __init__(self, tags):
            self.tags = tags

    class TestInclude:
        def __init__(self, tags):
            self.tags = tags

    tags = ['one', 'two', 'three']
    no_tags = []

    # Test PlayContext methods
    assert TestTask(tags).evaluate_tags(context.only_tags, context.skip_tags, {}) == True
    assert TestTask(tags).evaluate_tags(['one', 'two'], context.skip_tags, {}) == True

# Generated at 2022-06-13 09:17:16.607367
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    c1 = Taggable()
    c1._tags = ['tag_a', 'tag_b']
    c2 = Taggable()
    c2._tags = ['tag_c', 'tag_d']
    c3 = Taggable()
    c3._tags = ['tag_e', 'tag_f']
    c4 = Taggable()
    c4._tags = ['tag_g', 'tag_h']
    
    # "tags" is empty
    assert c1.evaluate_tags(['tag_a'], [], None)
    assert not c1.evaluate_tags(['tag_z'], [], None)

    # "only_tags" is empty
    assert c1.evaluate_tags([], ['tag_a'], None)

# Generated at 2022-06-13 09:17:27.325889
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    play = dict(all_vars=dict())
    t = Taggable()
    t._load_tags = Taggable._load_tags
    t.tags = ['A', 'B', 'C']
    assert t.evaluate_tags(only_tags=['A'], skip_tags=['B'], all_vars=play)
    assert t.evaluate_tags(only_tags=['B'], skip_tags=['A'], all_vars=play)
    assert t.evaluate_tags(only_tags=[], skip_tags=['A'], all_vars=play)
    assert t.evaluate_tags(only_tags=['A'], skip_tags=[], all_vars=play)
    assert t.evaluate_tags(only_tags=[], skip_tags=[], all_vars=play)


# Generated at 2022-06-13 09:17:34.049150
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import six

    class MockItem(Taggable):
        def __init__(self, tags=None):
            self._tags = tags

    # MockItem with no tags
    item = MockItem()
    assert not item.tags
    assert item.evaluate_tags([], None, None)
    assert item.evaluate_tags(['untagged'], None, None)
    assert item.evaluate_tags(['all'], None, None)
    assert item.evaluate_tags(['tagged'], None, None)
    assert item.evaluate_tags(['always'], None, None)
    assert item.evaluate_tags(['always', 'always'], None, None)
    assert item.evaluate_tags(['always', 'all'], None, None)

# Generated at 2022-06-13 09:17:41.722101
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    from collections import namedtuple
    from ansible.playbook.task import Task

    MockTask = namedtuple('MockTask', ['tags', '_loader'])
    mock = MockTask(['tag1', 'tag2'], None)
    playbook_task = Task(play=None, block=None, role=None, task_include=None, use_block=None,
                          implicit='implicit', default_vars=False, any_vars=False,
                          is_meta=False, is_role=False)

    # Test with no only_tags and skip_tags
    assert playbook_task.evaluate_tags(only_tags=None, skip_tags=None, all_vars=None) is True

    # Test with only_tags and skip_tags
    assert playbook_task.evaluate_tags

# Generated at 2022-06-13 09:17:52.289843
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task

    only_tags = set(['foo', 'bar', 'baz'])
    skip_tags = set(['nope'])
    all_vars = dict(foo=True, superman=False)

    # Tags explicitly set and should run
    task = Task()
    task.tags = ['foo']
    assert task.evaluate_tags(only_tags, skip_tags, all_vars)

    # Tags explicitly set and should not run
    task = Task()
    task.tags = ['nope']
    assert not task.evaluate_tags(only_tags, skip_tags, all_vars)

    # Tags set by variable and should run
    task = Task()
    task.tags = ['{{foo}}']

# Generated at 2022-06-13 09:17:58.123086
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.compat.tests import unittest

    class TestTaggable(Taggable):
        tags = ['a', 'b']

    @unittest.skipIf(Taggable is None, 'Taggable is not defined')
    class TestTaggableMethods(unittest.TestCase):
        def test_evaluate_tags(self):
            test_taggable = TestTaggable()
            self.assertTrue(test_taggable.evaluate_tags(only_tags=['a'], skip_tags=None, all_vars={}))
            self.assertTrue(test_taggable.evaluate_tags(only_tags=['b'], skip_tags=None, all_vars={}))

# Generated at 2022-06-13 09:18:08.041950
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Role(Taggable):
        pass

    r = Role()
    r._loader = None
    r.tags = ['my-tag', 'test-tag']
    assert r.evaluate_tags(None, None, dict())
    assert r.evaluate_tags(['my-tag', 'test-tag'], None, dict())
    assert r.evaluate_tags(['my-tag'], None, dict())
    assert r.evaluate_tags(['test-tag'], None, dict())
    assert r.evaluate_tags(['tagged'], None, dict())
    assert r.evaluate_tags(['always'], None, dict())
    assert r.evaluate_tags(['all'], None, dict())

# Generated at 2022-06-13 09:18:19.040872
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.task import Task as RoleTask
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.include import Include
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    import pytest

    # Set ansible data used
    block = Block(parent_block=None)
    task = Task(block=block)
    play = Play().load({'hosts': ['localhost'], 'roles': []})
    role = Role(name='test_role')

# Generated at 2022-06-13 09:18:30.264016
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    class DummyLoader:
        def load(self):
            pass

    only_tags = set(['flavour', 'tastes'])
    skip_tags = set(['red'])

    task = Task()
    task.tags = ['flavour', 'red']
    assert not task.evaluate_tags(only_tags, skip_tags, {})

    task = Task()
    task.tags = ['flavour', 'green']
    assert task.evaluate_tags(only_tags, skip_tags, {})

    task = Task()
    task.tags = ['flavour', 'red']
    assert not task.evaluate_tags(only_tags, only_tags, {})

    task = Task()

# Generated at 2022-06-13 09:18:36.121955
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.executor.task_result import TaskResult
    task_result = TaskResult(host=None, task=None)

    # test with tags=None, only_tags=None, skip_tags=None
    task_result.tags = None
    only_tags = None
    skip_tags = None
    all_vars = {}
    assert task_result.evaluate_tags(only_tags, skip_tags, all_vars) == True

    # test with tags=None, only_tags=list, skip_tags=None
    task_result.tags = None
    only_tags = ['tag1', 'tag2']
    skip_tags = None
    all_vars = {}
    assert task_result.evaluate_tags(only_tags, skip_tags, all_vars) == True

    # test with tags=

# Generated at 2022-06-13 09:19:12.332452
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockObj(Taggable):
        def __init__(self, tags):
            self.tags = tags

        def __repr__(self):
            return "MockObj(tags=%s)" % self.tags

    class MockVars():
        def __init__(self, vars):
            self.vars = vars
        def __getitem__(self, key):
            return self.vars[key]
        def __setitem__(self, key, value):
            self.vars[key] = value


# Generated at 2022-06-13 09:19:26.462791
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from collections import namedtuple
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    TagTask = namedtuple('TagTask', ['tags'])

    # Tests for the 'all' tag pattern
    assert not TagTask([u'no-all']).evaluate_tags(only_tags=[u'all'], skip_tags=[], all_vars={})
    assert TagTask([]).evaluate_tags(only_tags=[u'all'], skip_tags=[], all_vars={})
    assert TagTask([u'always']).evaluate_tags(only_tags=[u'all'], skip_tags=[], all_vars={})

    # Tests for the 'all' skip pattern

# Generated at 2022-06-13 09:19:38.386027
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    parent = Play()
    parent.vars = dict(
        foo="foo",
        bar="bar",
    )
    test_tags = dict(
        foo=True,
        bar=True,
    )
    test_task = Task()
    test_task._parent = parent
    test_task.tags = [ "foo", "bar" ]
    test_task.run_tags = dict(
        only_tags    = [ "tagged" ],
        skip_tags    = [ ],
    )

    result = test_task.evaluate_tags(test_task.run_tags.get('only_tags'), test_task.run_tags.get('skip_tags'), parent.vars)
    assert result is True

   

# Generated at 2022-06-13 09:19:48.742435
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # test when items have 'when' attribute
    assert Taggable.evaluate_tags(None, [], ['tag1'], ['tag1', 'tag2'], {}) is True
    assert Taggable.evaluate_tags(None, ['tag1'], ['tag1', 'tag2'], ['tag1', 'tag2'], {}) is False
    assert Taggable.evaluate_tags(None, ['tag1', 'tag2'], ['tag1', 'tag3'], ['tag1', 'tag2'], {}) is False
    assert Taggable.evaluate_tags(None, ['tag1', 'tag3'], ['tag1', 'tag2'], ['tag1', 'tag2'], {}) is True

# Generated at 2022-06-13 09:19:57.304762
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class Playbook(Taggable):
        pass

    playbook_always = Playbook()
    playbook_always.tags = ['always']

    playbook_tagged = Playbook()
    playbook_tagged.tags = ['tagged']
    playbook_untagged = Playbook()
    playbook_untagged.tags = []

    playbook_never = Playbook()
    playbook_never.tags = ['never']

    playbook_all = Playbook()
    playbook_all.tags = ['all']
    playbook_not_all = Playbook()
    playbook_not_all.tags = ['not_all']

    # Case 1: should_run must be True
    # 1.1: if only_tags contains 'always' tag
    only_tags = set(['always'])
    skip_tags = set()
    assert playbook_always.evaluate_tags

# Generated at 2022-06-13 09:20:06.590685
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class Object:
        tags = ['always']

    assert Taggable.evaluate_tags(Object, ['all'], []) == True
    assert Taggable.evaluate_tags(Object, ['all'], ['never']) == True
    assert Taggable.evaluate_tags(Object, ['all'], ['always']) == False
    assert Taggable.evaluate_tags(Object, ['all'], ['always', 'test']) == False
    assert Taggable.evaluate_tags(Object, ['always'], ['always']) == False
    assert Taggable.evaluate_tags(Object, ['always'], ['never']) == True
    assert Taggable.evaluate_tags(Object, ['always'], []) == True
    assert Taggable.evaluate_tags(Object, [], []) == True
    assert Taggable.evaluate_

# Generated at 2022-06-13 09:20:09.058664
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert 1 == 1
    # TODO: write unit tests for Taggable.evaluate_tags()

# Generated at 2022-06-13 09:20:19.563552
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeTask(Taggable):
        _only_tags = FieldAttribute(isa='string')
        _skip_tags = FieldAttribute(isa='string')

        def __init__(self, only_tags, skip_tags):

            self._only_tags = only_tags
            self._skip_tags = skip_tags

            self._tags = ['tag1', 'tag2', 'tag3']

    # test with 'tagged' in only_tags
    ft = FakeTask('tagged', '')
    tags = set(ft.tags)
    assert 'tag1' in tags
    assert 'tag2' in tags
    assert 'tag3' in tags

    # test with 'tagged' in skip_tags
    ft = FakeTask('', 'tagged')
    tags = set(ft.tags)

# Generated at 2022-06-13 09:20:30.619471
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert Taggable.evaluate_tags(['all'], [], [''])
    assert Taggable.evaluate_tags(['all'], ['never'], [''])
    assert Taggable.evaluate_tags(['all'], ['never'], ['always'])
    assert Taggable.evaluate_tags(['all'], [], ['never'])

    assert Taggable.evaluate_tags(['never'], ['never'], [''])
    assert Taggable.evaluate_tags(['never'], ['never'], ['always'])
    assert Taggable.evaluate_tags(['never'], ['never'], ['never'])
    assert not Taggable.evaluate_tags(['never'], [], [''])
    assert not Taggable.evaluate_tags(['never'], [], ['never'])


# Generated at 2022-06-13 09:20:42.244588
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    import pytest
    t = Task()
    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3', 'tag4']

    # test for tags, return True
    t.tags = ['tag1', 'tag2']
    assert t.evaluate_tags(only_tags, skip_tags, dict())

    # test for tags and 'all' in only_tags, return True
    t.tags = ['tag1', 'tag2']
    only_tags = ['all']
    assert t.evaluate_tags(only_tags, skip_tags, dict())

    # test for tags and 'never' in tags, return False
    t.tags = ['tag1', 'tag2', 'never']

# Generated at 2022-06-13 09:21:46.393026
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible import utils
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    ds = dict()

    only_tags = ["all"]
    skip_tags = ["never"]

    # Test case1 - tag is empty
    t = Taggable()
    t.load(ds, play_context)
    assert t.evaluate_tags(only_tags, skip_tags, dict()) == True

    #Test case2 - only_tags is empty
    t.load(ds, play_context)
    assert t.evaluate_tags([], skip_tags, dict()) == True

    #Test case3 - skip_tags is empty
    t.load(ds, play_context)
    assert t.evaluate_tags(only_tags, [], dict()) == True

    #Test case4 -

# Generated at 2022-06-13 09:21:57.492949
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.include import Include
    from ansible.playbook.taggable import Taggable
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # set some basic data structures to hold for the test
    tags = ['test_tag']
    only_tags = ['all']
    skip_tags = ['never']
    only_tags1 = ['test_tag']
    skip_tags1 = ['test_tag']
    only_tags2 = ['tagged']
    skip_tags2 = ['tagged']
    all_vars = {}
    all_vars['test_var'] = 'test_var'

    # Create a set of objects that we need to test this
    all_vars = Variable

# Generated at 2022-06-13 09:22:05.987628
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTaggable(Taggable):
        field = FieldAttribute(isa='list', listof=dict)

    # load a MockTaggable and set the tags attribute to certain tags
    m = MockTaggable()
    m.tags = ['dummy1']

    # set only_tags and skip_tags to None
    only_tags = None
    skip_tags = None
    all_vars = dict()

    # Case 1: default tags
    # case for tags: ['dummy1']
    # case for only_tags: None
    # case for skip_tags: None
    # expected result: True
    result = m.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result == True

    # Case 2: if only_tags has 'dummy3'
    # case for tags:

# Generated at 2022-06-13 09:22:18.964703
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import string_types

    class FakeDS(dict):

        def __init__(self):
            self.tags = None
            return

        def load_tags(self, attr, ds):
            if isinstance(ds, list):
                return ds
            elif isinstance(ds, string_types):
                value = ds.split(',')
                if isinstance(value, list):
                    return [x.strip() for x in value]
                else:
                    return [ds]
            else:
                raise AnsibleError('tags must be specified as a list', obj=ds)

    only_tags=None
    skip_tags=None
    all_vars=None

    # Create a FakeDS Object
   

# Generated at 2022-06-13 09:22:30.032900
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook
    import ansible.utils
    import ansible.vars
    import collections
    import os

    test_data = collections.namedtuple('test_data', 'only_tags skip_tags tags data expect')

# Generated at 2022-06-13 09:22:39.509299
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """The method evaluate_tags() of class `Taggable` takes a dictionary
    which maps the tags to a boolean value indicating whether the task
    should or should not be run.  The method behaves as expected when
    the task has the appropriate tags.

    However, it was returning True even when the task did not have the
    required tags.

    See https://github.com/ansible/ansible/issues/23017

    """

    # Create a fake taggable and call evaluate_tags() on it.
    class FakeTaggable(Taggable):
        def __init__(self, all_vars):
            self._loader = None
            self.tags = None

    # Test for issue 23017 (see the related link).
    taggable = FakeTaggable({})

    # The following call always returned True due to the bug, but

# Generated at 2022-06-13 09:22:50.150128
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block

    class TestTaggable(Taggable):
        def __init__(self, ds, only_tags, skip_tags):
            self._ds = ds
            self._only_tags = only_tags
            self._skip_tags = skip_tags

        def _evaluate_tags(self):
            return self.evaluate_tags(self._only_tags, self._skip_tags, self._ds)

        @property
        def tags(self):
            return self._ds.get('tags', [])

    # Validating the 'only_tags' argument of evaluate_tags

# Generated at 2022-06-13 09:22:57.736204
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass(Taggable):
        def __init__(self):
            self._loader = None

    obj = TestClass()
    obj.tags = ['tag1', 'tag2']
    assert obj.evaluate_tags(['tag1'], [], {}) == True
    assert obj.evaluate_tags(['tag3'], [], {}) == False
    assert obj.evaluate_tags([], ['tag1'], {}) == False
    assert obj.evaluate_tags([], [], {}) == True
    assert obj.evaluate_tags(['tag1'], ['tag1'], {}) == False

    obj.tags = ['tag1']
    assert obj.evaluate_tags(['all'], [], {}) == True
    assert obj.evaluate_tags(['tagged'], [], {}) == True
    assert obj.evaluate

# Generated at 2022-06-13 09:23:05.554594
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    import pytest

    taggable_instance = Taggable()

    [context, all_vars] = _setup_context_and_vars()

    def _test_evaluate_tags(only_tags, skip_tags, expected):
        assert taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars) == expected

    # run task where all tags match
    taggable_instance.tags = ['tag1', 'tag2']
    _test_evaluate_tags(['tag1', 'tag3'], None, True)
    _test_evaluate_tags(['tag1'], None, True)
    _test_evaluate_tags(['tag2'], None, True)