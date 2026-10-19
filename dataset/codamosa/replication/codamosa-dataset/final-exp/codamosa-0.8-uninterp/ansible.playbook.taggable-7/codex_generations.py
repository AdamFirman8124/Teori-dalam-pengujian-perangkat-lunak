

# Generated at 2022-06-13 09:13:18.248311
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.attribute import Attribute
    t = Attribute()
    t.tags._load_tags('tags', ['unit', 'test'])
    assert t.evaluate_tags(['unit'], [], {}) == True


# Generated at 2022-06-13 09:13:25.727558
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.constants import DEFAULT_VAULTPASS

    kwargs = dict(tags=['always', 'always'], task_vars = dict(foo='foo_value', bar='bar_value'), _hostvars=HostVars(dict(
        ansible_ssh_host="127.0.0.1", ansible_ssh_pass="swordfish", ansible_ssh_port=22, ansible_connection="ssh",
        vault_password="vault", default_vault_password=DEFAULT_VAULTPASS), "127.0.0.1"))
    _test_instance = Taggable()

    # test case 1, tags=always and only

# Generated at 2022-06-13 09:13:32.149027
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import AnsibleVars
    pg = PlayContext()
    pg.only_tags = ['tag1','tag2','tag3']
    pg.skip_tags = ['tag_skipped','tag3','tag5']
    pg.tags = ['tag_skipped']
    all_vars = AnsibleVars()
    all_vars.update(pg.as_dict())

    t = Taggable()
    t._loader = None
    t._tags = ['tag2']
    assert t.evaluate_tags(only_tags=pg.only_tags, skip_tags=pg.skip_tags, all_vars=all_vars) == False
    t._tags = ['tag1']

# Generated at 2022-06-13 09:13:41.119566
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
  # Test passing 
  t = Taggable()

  t.tags = ['tag1']
  assert True == t.evaluate_tags(set(['tag1']), set(['tag2']), None)

  t.tags = ['tag1', 'tag2']
  assert True == t.evaluate_tags(set(['tag1', 'tag2']), set(['tag3']), None)

  t.tags = ['tag2', 'tag1']
  assert True == t.evaluate_tags(set(['tag1', 'tag2']), set(['tag3']), None)

  t.tags = ['tag1']
  assert True == t.evaluate_tags(set([]), set(['tag2']), None)

  t.tags = set(['tag1'])

# Generated at 2022-06-13 09:13:52.833277
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    all_vars = dict()
    only_tags = ['tag1', 'tag2', 'tag3']
    skip_tags = ['tag3']
    tag = ['tag1']
    all_vars['tag'] = tag

    task = Taggable()
    task.tags = tag
    should_run = task.evaluate_tags(only_tags, skip_tags, all_vars)
    assert should_run == True

    all_vars['tag'] = ['tag4']
    should_run = task.evaluate_tags(only_tags, skip_tags, all_vars)
    assert should_run == False

    all_vars['tag'] = ['tag1']
    skip_tags = ['tag1']
    should_run = task.evaluate_tags(only_tags, skip_tags, all_vars)

# Generated at 2022-06-13 09:14:04.299685
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    output = []
    class MockAnsibleModule():
        def __init__(self):
            pass

    class MockTaggable(Taggable):
        def __init__(self, data, loader):
            self._loader = loader
            self._load_tags('tags', data.get('tags', []))

    class MockTempler():
        def __init__(self, loader, variables):
            pass
        def template(self, arg):
            return arg
    class MockLoader():
        pass
    loader = MockLoader()
    templer = MockTempler(loader, {})

    # test empty tags
    ds = dict(tags=[])
    t = MockTaggable(ds, loader)
    t.evaluate_tags(['tag1'], [], {})

# Generated at 2022-06-13 09:14:10.202382
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.utils.plugin_docs import get_docstring
    load_docs = get_docstring(Taggable)
    tag1 = load_docs(method='tags')
    tag2 = load_docs(method='evaluate_tags')
    print(tag1)
    print(tag2)

# Generated at 2022-06-13 09:14:19.417631
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.plugins import task_loader, callback_loader

    ds = dict(
        name='template_foo',
        src='/templates/foo.j2',
        dest='/etc/file.conf',
        state='absent',
        force=True,
    )
    task_include = TaskInclude()
    task_include._load_name(attr="name", ds=ds)
    task = Task()
    task.task_include = task

# Generated at 2022-06-13 09:14:31.933036
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockTaggable(Taggable):
        def __init__(self):
            self._loader = None

    mock_only_tags = frozenset(['only_tag'])
    mock_skip_tags = frozenset(['skip_tag'])
    mock_all_vars = {}

    test_taggable = MockTaggable()
    test_taggable._load_tags(None, ['only_tag'])
    assert(test_taggable.evaluate_tags(mock_only_tags, mock_skip_tags, mock_all_vars) == True)
    assert(test_taggable.evaluate_tags(mock_skip_tags, mock_only_tags, mock_all_vars) == False)

# Generated at 2022-06-13 09:14:41.860379
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import pytest
    from ansible.playbooks.play import Play
    from ansible.playbooks.blocks import Block

    ###########################################
    # case 1 : Play is configured with 'never'
    #          tag and with no only_tags or
    #          skip_tags configured
    # Expectation : The play should not run
    ###########################################
    play = Play().load({'name': 'test_play',
                        'connection': 'local',
                        'hosts': 'localhost',
                        'roles': [],
                        'tasks': [{'action': {'module': 'debug', 'msg': 'Executed'},
                                   'tags': ['never'],
                                   'name': 'debug'}],
                        'tags': ['never']})

# Generated at 2022-06-13 09:15:08.225240
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    results = {}

    class TestClass(Taggable):
        pass

    test_obj = TestClass()

    # Check that evaluate_tags return True when there are no tags provided
    # and no tag options have been specified
    test_obj.tags = set()
    actual_result = test_obj.evaluate_tags(set(),set(),{})
    if actual_result != True:
        results['test_Taggable_evaluate_tags_case0'] = 'fail'
    else:
        results['test_Taggable_evaluate_tags_case0'] = 'pass'

    # Check that evaluate_tags return True when the only tag option is --tags=all
    test_obj.tags = set()
    actual_result = test_obj.evaluate_tags({'all'},set(),{})

# Generated at 2022-06-13 09:15:15.874733
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.parsing.yaml.objects import AnsibleSequence

    class MockTaggable(Taggable):
        pass

    only_tags = ['bar', 'foo']
    skip_tags = []
    all_vars = {}

    obj = MockTaggable()

    obj.tags = ['foo']
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars)

    obj.tags = ['foo', 'bar']
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars)

    obj.tags = ['baz']
    assert not obj.evaluate_tags(only_tags, skip_tags, all_vars)

    obj.tags = ['baz', 'foo']

# Generated at 2022-06-13 09:15:25.748229
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    t = TaskInclude()
    tags_to_be_checked = ['__not_existing_tag__', 'another_not_existing_tag']
    t.tags = tags_to_be_checked

    #default values of only_tags and skip_tags are []
    should_run = t.evaluate_tags(only_tags=[], skip_tags=[])
    assert not should_run, "should be False because no tags were specified"

    #default values of only_tags and skip_tags are []
    should_run = t.evaluate_tags(only_tags=['all'], skip_tags=[])
    assert not should_run, "should be False because default of tags is []"

    #default values of only_tags and skip_tags are []

# Generated at 2022-06-13 09:15:36.404249
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t.tags = ['green', 'blue']
    assert t.evaluate_tags(only_tags=['green'], skip_tags=[], all_vars={}) == True
    t.tags = 'green,blue'
    assert t.evaluate_tags(only_tags=['green'], skip_tags=[], all_vars={}) == True
    t.tags = 'green, blue'
    assert t.evaluate_tags(only_tags=['green'], skip_tags=[], all_vars={}) == True
    t.tags = ['green', 'blue', 'sky-blue']
    assert t.evaluate_tags(only_tags=['green', 'sky-blue'], skip_tags=[], all_vars={}) == True

# Generated at 2022-06-13 09:15:51.827480
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # initialize Taggable object
    taggable = Taggable()

    # initialize fields to be used with tags
    taggable.tags = None
    only_tags = None
    skip_tags = None

    # no tags in tags, only_tags and skip_tags
    assert taggable.evaluate_tags(only_tags, skip_tags, []) == True

    # one tag in tags, only_tags and skip_tags
    taggable.tags = 'tag1'
    only_tags = ['tag1']
    skip_tags = ['tag1']
    assert taggable.evaluate_tags(only_tags, skip_tags, []) == True

    # tags in tags, only_tags and skip_tags
    taggable.tags = 'tag1, tag2'

# Generated at 2022-06-13 09:16:02.061137
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestTaggable(Taggable):
        __slots__ = ('_tags', 'mytags')

        def __init__(self):
            self.mytags = None
            self._tags = None

        def load_tags(self, attr, ds):
            return self._load_tags(attr, ds)

    tt = TestTaggable()

    tt.mytags = ['test_one', 'test_two']
    tt.tags = tt.mytags

    # only_tags = ['all'], skip_tags = [], should_run = True
    assert tt.evaluate_tags(only_tags=['all'], skip_tags=[], all_vars=dict()) == True

    # only_tags = ['all', 'never'], skip_tags = [], should_run = True


# Generated at 2022-06-13 09:16:11.153318
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test setup
    class TestClass(Taggable):
        pass

    # Create test object with tags: tag1, tag2 and tag3
    object_tags = TestClass()
    object_tags['tags'] = ['tag1', 'tag2', 'tag3']
    # object_tags.tags is a list
    assert isinstance(object_tags['tags'], list)
    # object_tags.tags has the expected tags
    assert object_tags['tags'] == ['tag1', 'tag2', 'tag3']

    # Test 1.1: always should run
    assert object_tags.evaluate_tags(only_tags=['all', 'tag1'], skip_tags=[], all_vars={})

# Generated at 2022-06-13 09:16:18.067298
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import sys
    import unittest

    # Helper function to build a mock of Taggable
    def build_mock_Taggable(tags):
        class MockTaggable(Taggable):
            def __init__(self, tags):
                self.tags = tags
            def __repr__(self):
                return '<Taggable tags=%s>' % self.tags

        return MockTaggable(tags)

    # Helper function to build a test case

# Generated at 2022-06-13 09:16:24.153629
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    item = Taggable()
    # Default values
    assert item.evaluate_tags(only_tags=[], skip_tags=[], all_vars={})
    assert item.evaluate_tags(only_tags=None, skip_tags=None, all_vars={})

    # Even thee value True is incorrect, it is not possible to use
    # any_tags as a parameter, because it is not defined.
    assert not item.evaluate_tags(only_tags='any_tags', skip_tags=[], all_vars={})
    assert not item.evaluate_tags(only_tags=[''], skip_tags=[], all_vars={})
    assert not item.evaluate_tags(only_tags=['fake_tag'], skip_tags=[], all_vars={})

    # This test is the inverse of the previous one.

# Generated at 2022-06-13 09:16:28.797210
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' test_Taggable_evaluate_tags()
        Make sure method evaluate_tags of class Taggable works as expected.
    '''
    class MyClass(Taggable):
        def __init__(self):
            self._loader = None
            self.tags = []
            self.only_tags = set()
            self.skip_tags = set()

    obj = MyClass()
    all_vars = dict()
    obj.tags = ['tag1', 'tag2']
    assert obj.evaluate_tags(obj.only_tags, obj.skip_tags, all_vars) is True

    # only_tags = set(['tag1', 'tag2'])
    obj.only_tags = set(['tag1', 'tag2'])

# Generated at 2022-06-13 09:16:50.332175
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
 
    class dummy_class(Taggable):
        pass
    
    only_tags = ['tag1','tag2','tag3','tag4','tg5','tg6']
    skip_tags = ['tag1','tag2','tag3','tag4','tg5','tg6']
    all_vars = {}    

    a = dummy_class()
    a.tags = ['tag1','tag2','tag3','tag4','tg5','tg6']
    assert a.evaluate_tags(only_tags,skip_tags,all_vars) == True

    a.tags = ['tag1']
    assert a.evaluate_tags(only_tags,skip_tags,all_vars) == True

    a.tags = ['tag7']
    assert a.evaluate_tags(only_tags,skip_tags,all_vars)

# Generated at 2022-06-13 09:16:58.228009
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()

    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['hosts'])
    variable_manager.set_inventory(inventory)

    t = Base.load(None, variable_manager, loader, play_context=PlayContext())
    instance = Taggable()

    # Test 1:
    # No tags
    # Only_tags = [all]
    # Skip_tags = null
    instance.tags = None

    only_tags = ['all']
    skip_tags = []

    assert instance

# Generated at 2022-06-13 09:17:09.380554
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.attribute import Attribute, FieldAttribute
    from ansible.playbook.play_context import PlayContext

    # class for testing purpose
    class Task(Taggable):
        _tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)
        my_tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)
        tags = FieldAttribute(isa='list', default=None, listof=(string_types, int), extend=True)
        def __init__(self, my_tags=None, tags=None, play_context=None):
            if not play_context:
                play_context = PlayContext()
            self._play_context = play_context
            self.my_tags = my_tags
           

# Generated at 2022-06-13 09:17:21.475331
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_taggable = Taggable()
    assert test_taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars={})
    test_taggable.tags = ['ping', 'always']
    assert test_taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars={})
    assert test_taggable.evaluate_tags(only_tags={'ping'}, skip_tags=None, all_vars={})
    assert test_taggable.evaluate_tags(only_tags={'never'}, skip_tags=None, all_vars={})
    assert test_taggable.evaluate_tags(only_tags={'always'}, skip_tags=None, all_vars={})
    assert test_taggable.evaluate_

# Generated at 2022-06-13 09:17:30.925903
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import PlayBase
    from ansible.playbook.task import Task
    from ansible import constants as C

    # Test without tags
    t = Task()
    assert t.evaluate_tags([], [], dict())

    # Test with only_tags
    t = Task()
    assert t.evaluate_tags([], ['never'], dict())
    assert not t.evaluate_tags([], ['all'], dict())
    assert not t.evaluate_tags([], ['tagged'], dict())
    assert not t.evaluate_tags([], ['test_tag'], dict())

    # Test with skip_tags
    t = Task(tags=['test_tag'])
    assert t.evaluate_tags([], [], dict())
    assert not t.evaluate_tags([], ['never'], dict())

# Generated at 2022-06-13 09:17:39.682884
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Thing(Taggable):
        def __init__(self):
            self.tags = []

    assert Thing().evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=['tag3'], all_vars={})

    # When tags is empty then tags will be ['untagged']
    # 'untagged' is disjoint to ['tag1', 'tag2'] so the task should run
    # 'untagged' is disjoint to ['tag3'] so the task should not be skipped
    assert Thing().evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=['tag3'], all_vars={})
    assert Thing().evaluate_tags(only_tags=['tag3'], skip_tags=['tag2'], all_vars={})

    # When tags

# Generated at 2022-06-13 09:17:51.028636
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import os
    import sys
    import inspect
    import unittest
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    from ansible.playbook import Play

    # First, we test the case without tags.
    # A play should be executed if neither only_tags nor skip_tags are specified.
    # A play should be executed if skip_tags is specified but not only_tags.
    # A play should not be executed if only_tags is specified but not skip_tags.
    p = Play()
    all_vars = {}
    only_tags = ['tag1', 'tag2']
    only_tags = None
    skip

# Generated at 2022-06-13 09:18:05.622482
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display

    class ActionModule(object):
        ''' mock action module '''
        def __init__(self):
            pass

    class Play(object):
        def __init__(self, name):
            self.name = name
            self.hosts = []
            self.tags = []
            self.tasks = []

    class Task(object):
        def __init__(self, name, tags=[]):
            self.name = name
            self.tags = tags
            self.action = None

    class Role(object):
        def __init__(self, name):
            self.name = name
           

# Generated at 2022-06-13 09:18:13.722485
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_obj = Taggable()
    test_obj.tags = []
    test_obj.tags = ['test']

    only_tags = ['never']
    skip_tags = []

    # Test case when tags is not None and only_tags is not None and skip_tags is None
    result = test_obj.evaluate_tags(only_tags, skip_tags, {})
    assert result == False

    # Test case when tags is not None and only_tags is None and skip_tags is not None
    result = test_obj.evaluate_tags(None, ['test'], {})
    assert result == False

    # Test case when tags is not None and only_tags is None and skip_tags is None
    result = test_obj.evaluate_tags(None, None, {})
    assert result == True

    # Test case when tags is

# Generated at 2022-06-13 09:18:20.643362
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockLoad:
        pass

    class MockPlaybooks:
        pass

    class MockOnlyPlay:
        pass

    class MockPlay:
        pass

    class MockTask:
        pass

    class MockPlaybook:
        pass

    class MockData:
        pass

    test_data = MockData()

    test_playbook = MockPlaybook()
    test_playbook._loader = MockLoad()
    test_playbook._variable_manager = MockLoad()
    test_playbook.all_vars = dict(
        {
            'foo': 'bar',
            'wat': ['something', 'something else', 'that other thing', 'animal'],
            'z': 'zoo',
        }
    )
    test_play = MockPlay()
    test_play.tags = ['something', 'something else']
    test

# Generated at 2022-06-13 09:18:59.276263
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    print("Testing class Taggable evaluate_tags method...")
    task = Taggable()

    # Check for invalid type of only_tags and skip_tags arguments
    should_fail = False
    try:
        task.evaluate_tags(1, 2, 3)
    except:
        should_fail = True
    assert(should_fail)

    # Check for regular case
    assert(task.evaluate_tags(set(['tag1', 'tag3']), set(['tag2']), {}) == True)
    assert(task.evaluate_tags(set(['tag1', 'tag2']), set(['tag2']), {}) == False)
    assert(task.evaluate_tags(set(['tag2', 'tag4']), set(['tag1']), {}) == True)

# Generated at 2022-06-13 09:19:07.208835
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    import pytest

    # data to be used in tests
    class test_cls(Taggable):
        def __init__(self):
            self.tags = []
            self.vars = {}

    data = test_cls()
    data.tags = ['test1', 'test2', 'test3']

    # execute the method with empty 'tags' and 'skipped_tags' and expect True as result
    assert data.evaluate_tags([], [], data.vars) is True

    # execute the method with 'tags' containing values that are not present in 'data.tags' list

# Generated at 2022-06-13 09:19:17.349546
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = ['t1', 't2']
    skip_tags = ['t2', 't3']
    all_vars = {"tags": set(['t1', 't2'])}

    t = Taggable()
    assert t.evaluate_tags(only_tags, skip_tags, all_vars) == True
    assert t.tags == ['t1', 't2']

    only_tags = ['t1', 't2']
    skip_tags = ['t2', 't3']
    all_vars = {"tags": set(['t3', 't4'])}

    t = Taggable()
    assert t.evaluate_tags(only_tags, skip_tags, all_vars) == False
    assert t.tags == ['t3', 't4']


# Generated at 2022-06-13 09:19:23.724163
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    ###########
    # fixtures
    ###########
    class MockTaggable(Taggable):
        pass

    class MockAnsibleModule:

        class MockLoader:
            pass

        class MockVariableManager:
            def __init__(self):
                self.vars = {'a': 'b'}

        def __init__(self):
            self.loader = MockAnsibleModule.MockLoader()
            self.variable_manager = MockAnsibleModule.MockVariableManager()

    class MockTask:
        @staticmethod
        def get_name():
            return 'mock_task'

    ansible_module = MockAnsibleModule()
    playbook_context = {
        'a': 'A',
        'b': 'B',
    }
    taggable = MockTaggable()



# Generated at 2022-06-13 09:19:30.261435
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        pass

    # Test that tagged item is not skipped when only_tags is 'tagged' and skip_tags is empty
    t = TestTaggable()
    t._tags = ["bar"]
    t.tags = ["foo", "bar"]
    only_tags = ['tagged']
    skip_tags = []
    assert t.evaluate_tags(only_tags, skip_tags)

    # Test that tagged item is skipped when only_tags is empty and skip_tags is 'tagged'
    t = TestTaggable()
    t._tags = ["bar"]
    t.tags = ["foo", "bar"]
    only_tags = []
    skip_tags = ['tagged']
    assert not t.evaluate_tags(only_tags, skip_tags)

    # Test that tagged item

# Generated at 2022-06-13 09:19:41.308428
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task

    yaml_task_no_tags = """
    - name: test_task
      action: ping
    """

    yaml_task_main_tags = """
    - name: test_task
      action: ping
      tags:
          - test_main
    """

    yaml_task_other_tags = """
    - name: test_task
      action: ping
      tags:
          - test_other
    """

    yaml_task_main_and_other_tags = """
    - name: task_test
      action: ping
      tags:
          - test_main
          - test_other
    """


# Generated at 2022-06-13 09:19:52.642072
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:20:03.076169
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class dummy_block():
        loader = None

    class dummy_task(Taggable):
        _loader = None

    task_1 = dummy_task()
    block_1 = dummy_block()
    block_1.tasks = [task_1]
    play_1 = Play()
    play_1.block = block_1
    play_1._tqm = None
    only_tags = []
    skip_tags = []
    all_vars = {}
    play_1.only_tags = only_tags
    play_1.skip_tags = skip_tags

    task_1.tags = []
    assert task_1.evaluate_tags(play_1.only_tags, play_1.skip_tags, all_vars), "'untagged' task should run if no tag option passed"

    task_1

# Generated at 2022-06-13 09:20:10.488028
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableObject(Taggable):
        _tags = ['tagged', 'ansible']

    class TaggableObjectWithManyTags(Taggable):
        _tags = ['tagged', 'ansible', 'many', 'tags']

    class TaggableObjectWithNeverTag(Taggable):
        _tags = ['tagged', 'ansible', 'never']

    class TaggableObjectWithAllTag(Taggable):
        _tags = ['tagged', 'ansible', 'all']

    class TaggableObjectWithAlwaysTag(Taggable):
        _tags = ['tagged', 'ansible', 'always']

    # Test with no tags
    assert TaggableObject().evaluate_tags([], [], {})
    assert TaggableObjectWithManyTags().evaluate_tags([], [], {})
    assert T

# Generated at 2022-06-13 09:20:20.261573
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task

    # Initialize basic objects

    class Play(Base, Taggable): pass
    class Playbook(Base): pass

    playbook = Playbook()
    play = Play(playbook=playbook)
    task = Task()
    task._parent = play
    task._play = play
    play._loader = {'_basedir': 'some_dir'}
    task._loader = {'_basedir': 'some_dir'}
    task._role = None

    # Unit test for evaluate_tags of class Task
    task.tags = []
    assert task.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) == True
    task.tags = ['always']

# Generated at 2022-06-13 09:21:27.957390
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:21:41.763619
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Ansible requires Python 2.6+
    try:
        from unittest2 import TestCase
    except ImportError:
        from unittest import TestCase

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    for klass in (TaskInclude, Block, Play):
        assert hasattr(klass, 'evaluate_tags')
        assert callable(getattr(klass, 'evaluate_tags'))

    class DummyData():
        def __init__(self, ds):
            self.ds = ds

    class DummyVariables():
        pass


# Generated at 2022-06-13 09:21:55.550547
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Play
    import pytest

    # Make sure that the method evaluates tags as expected.
    # Test cases are constructed with tuples of the form
    # (tags,only_tags,skip_tags,all_vars,should_run)

# Generated at 2022-06-13 09:22:05.184832
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeRunnerForTagsTests(object):
        class connection(object):
            class transport(object):
                def __init__(self):
                    self.transport = 'local'

    r = FakeRunnerForTagsTests()

    class FakeModuleForTagsTests(object):
        def __init__(self):
            self.runner = r
            self.no_log = False

        def v2_runner_on_failed(self, result):
            raise Exception('failed')

        def v2_runner_on_ok(self, result):
            raise Exception('ok')

    class FakeModuleLoaderForTagsTests(object):
        def get_basedir(self, path):
            return path

    class FakePlaybookForTagsTests(Taggable):
        _loader = FakeModuleLoaderForTagsTests()


# Generated at 2022-06-13 09:22:18.628085
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.base import PlayBase

    playbook = PlayBase()
    playbook.vars.update({ "var2": "a" })
    playbook.vars.update({ "var3": [ "a", "b", "c" ] })

    class FakeTask:
        def __init__(self, _name, _tags, _loader, _parent):
            self._parent = _parent
            self.name = _name
            self.tags = _tags
            Taggable.__init__(self, _loader)

    task = FakeTask('Test Task', ['tag2', 'tag3'], playbook._loader, playbook)
    assert task.evaluate_tags(['tag2'], [], {})
    assert task.evaluate_tags(['tag3'], [], {})

# Generated at 2022-06-13 09:22:32.466739
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude

    ti = TaskInclude()

    ti.tags = ['role1']

    assert(ti.evaluate_tags(set(['all']), set(), {}))
    assert(ti.evaluate_tags(set(['role1']), set(), {}))
    assert(ti.evaluate_tags(set(['tagged']), set(), {}))
    assert(not ti.evaluate_tags(set(['role2']), set(), {}))

    ti.tags = set(['role2'])

    assert(ti.evaluate_tags(set(['all']), set(), {}))
    assert(ti.evaluate_tags(set(['tagged']), set(), {}))
    assert(ti.evaluate_tags(set(['role2']), set(), {}))

# Generated at 2022-06-13 09:22:40.800152
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Base(Taggable):
        tags = []
        def __init__(self):
            self._play = None
            self._loader = None

    # Test only_tags when tags are not empty
    base = Base()
    base.tags = ['tag1', 'tag2']
    only_tags = ['tag1']
    skip_tags = []
    all_vars = {
        'always': False
    }
    assert base.evaluate_tags(only_tags, skip_tags, all_vars)

    # Test only_tags when 'tagged' is in only_tags
    base = Base()
    base.tags = ['tag1', 'tag2']
    only_tags = ['tagged']
    skip_tags = []
    all_vars = {
        'always': False
    }
    assert base

# Generated at 2022-06-13 09:22:50.865160
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Create an instance of class Taggable
    t = Taggable()
    # Initialize the tags in different ways
    t.tags = ['a', 'b' ,'c']
    #  print t.tags
    # Check for correctness of method evaluate_tags for different list.
    print (t.evaluate_tags(['a'], [], {}))
    print (t.evaluate_tags(['a', 'c'], [], {}))
    print (t.evaluate_tags(['a', 'b'], [], {}))
    print (t.evaluate_tags([], ['a'], {}))
    print (t.evaluate_tags([], ['a', 'b'], {}))
    print (t.evaluate_tags([], ['k', 'e', 'l'], {}))

# Generated at 2022-06-13 09:22:58.161997
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    t1 = Task()
    t1._loader = None
    t2 = Task()
    t2._loader = None
    t3 = Task()
    t3._loader = None

    # Basic check
    t1.tags = ['always', 'tag1']
    only_tags = ['tag1']
    skip_tags = []
    assert t1.evaluate_tags(only_tags, skip_tags, {}) is True
    skip_tags = ['tag1']
    assert t1.evaluate_tags(only_tags, skip_tags, {}) is False

    # 'all' in only_tags
    only_tags = ['all']
    skip_tags = []
    assert t1.evaluate_tags(only_tags, skip_tags, {}) is True
    assert t2

# Generated at 2022-06-13 09:23:05.891932
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task

    # Basic tests
    # No tags
    t = Task()
    assert t.evaluate_tags(['all'], [], dict())

    # Has tags
    t = Task()
    t.tags.append('my_tag')
    assert t.evaluate_tags(['my_tag'], [], dict())

    # Has tags
    t = Task()
    t.tags.append('my_tag')
    assert t.evaluate_tags([], ['my_tag'], dict())

    # Has tags
    t = Task()
    t.tags.append('my_tag')
    assert not t.evaluate_tags(['other_tag'], ['my_tag'], dict())

    # Has tags
    t = Task()
    t.tags.append('my_tag')
   