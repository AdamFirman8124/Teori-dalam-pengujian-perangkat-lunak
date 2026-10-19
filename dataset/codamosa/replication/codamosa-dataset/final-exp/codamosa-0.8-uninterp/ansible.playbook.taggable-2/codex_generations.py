

# Generated at 2022-06-13 09:13:24.089268
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task
    import ansible.module_utils.six as six

    # Tests
    t = ansible.playbook.task.Task()
    # Example item:
    # - hosts: localhost
    #   tasks:
    #     - name: TAGGED
    #       command: do something
    #       tags: [tagged]
    #     - name: UNTAGGED
    #       command: do something
    #     - name: TAGGED AND UNTAGGED
    #       command: do something
    #       tags: [tagged, untagged]
    #     - name: TAGGED BUT NEVER
    #       command: do something
    #       tags: [tagged, never]
    #     - name: NEVER
    #       command: do something
    #       tags: [never

# Generated at 2022-06-13 09:13:31.060641
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Imports required for object creation
    from ansible.playbook.base import Base
    class TestTaggable(Base, Taggable):
        pass

    # Creation of the object to be tested
    base = Base(loader=None)
    test_obj = TestTaggable(base, loader=None, tags=['tagged', 'tagged2', 'untagged'])

    # Testing tags, only_tags and skip_tags with no elements
    only_tags = []
    skip_tags = []
    assert test_obj.evaluate_tags(only_tags, skip_tags, {}) == True

    # Testing tags, only_tags and skip_tags with an element
    # Should be True
    only_tags = ['tagged']
    skip_tags = []

# Generated at 2022-06-13 09:13:39.663809
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.role.include import RoleInclude
    import copy
    import pytest

    options = {'__role_name': 'test', '_role_path': ['/']}
    myRoleInclude = RoleInclude('/', 'roles/myrole', options=options)
    myRoleInclude._load_role_data()
    myRoleInclude._parent = RoleInclude

    assert (myRoleInclude.evaluate_tags(['role_tags'], [], {}) == True)
    assert (myRoleInclude.evaluate_tags(['role_untagged'], [], {}) == False)
    assert (myRoleInclude.evaluate_tags([], ['role_tags'], {}) == False)

# Generated at 2022-06-13 09:13:51.862721
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.vars import VariableManager

    var_manager = VariableManager()
    fake_ds = dict(
        tags   = ['tag1', 'tag2', 'tag3'],
        _loader = dict(),
    )

    FakeTaggable = type('FakeTaggable', (Taggable, ), fake_ds)
    fake_obj = FakeTaggable()

    assert not fake_obj.evaluate_tags(['tag1'], [], var_manager)
    assert fake_obj.evaluate_tags(['tag1'], [], var_manager, True)
    assert fake_obj.evaluate_tags(['tag1', 'tag2', 'tag3'], [], var_manager)

# Generated at 2022-06-13 09:14:03.179443
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()
    obj.tags = ['a']

    assert obj.evaluate_tags(['a', 'b'], [], {})
    assert not obj.evaluate_tags(['c'], [], {})
    assert not obj.evaluate_tags(['c'], ['a'], {})
    assert obj.evaluate_tags(['all'], [], {})
    assert not obj.evaluate_tags(['all'], ['a'], {})
    assert obj.evaluate_tags(['all'], ['never'], {})
    assert not obj.evaluate_tags(['all'], ['always'], {})
    assert obj.evaluate_tags(['always'], [], {})
    assert not obj.evaluate_tags(['always'], ['a'], {})

# Generated at 2022-06-13 09:14:11.104680
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars import VariableManager

    root_ds = AnsibleLoader(None).load_from_file('../../test/units/module_utils/loader_fixtures/tags.yml')

    var_mgr = VariableManager()

    child_ds = root_ds[0]
    child_ds.post_validate(templar=Templar(loader=None, variables=var_mgr))
    assert child_ds.evaluate_tags(['foo', 'buz'], None, None) is True
    assert child_ds.evaluate_tags(['foo', 'buz'], [], None) is True
    assert child_ds.evaluate_tags(['foo', 'buz'], ['bar'], None) is True
    assert child

# Generated at 2022-06-13 09:14:20.441431
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''Define set of test cases to check the behaviour of Taggable.evaluate_tags()'''


# Generated at 2022-06-13 09:14:34.524109
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import os
    import sys

    class FakeLoader(object):
        def __init__(self, basedir='/foo/bar'):
            self._basedir = basedir

        def path_dwim(self, basedir, given):
            if basedir is None:
                basedir = self._basedir
            if not os.path.isabs(given):
                given = os.path.join(basedir, given)
            return given

    class FakePlaybook(object):
        def __init__(self):
            self.loader = FakeLoader()

        def _ds_from_entry(self, entry, template=False):
            return entry

    class FakeTask(object):
        def __init__(self):
            self.play = FakePlaybook()
            self.tags = []

    parent = FakeTask()

   

# Generated at 2022-06-13 09:14:44.126878
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTest:
        def __init__(self):
            self.tags_attrib = []
        def __getattribute__(self,attr):
            val = object.__getattribute__(self,attr)
            if attr == "tags":
                return self.tags_attrib
            return val
        def __setattr__(self,attr,val):
            if attr == "tags":
                self.tags_attrib = val
            return object.__setattr__(self,attr,val)
        def set_tags(self,tags):
            self.tags_attrib = tags
    # End of Dummy class definition

    t = TaggableTest()

    def reset_tags():
        t.set_tags([])

    print ("Empty tags")

# Generated at 2022-06-13 09:14:54.229443
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    hosts = [Host(name="myhost")]
    variable_manager.set_hosts(hosts)


# Generated at 2022-06-13 09:15:12.345941
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Create a PlaybookInclude object with no hosts set and no roles
    hosts = []
    t = Taggable()
    t.tags = []
    assert (t.evaluate_tags([], ['all'], {}) == False)
    assert (t.evaluate_tags(['foo'], ['all'], {}) == False)
    assert (t.evaluate_tags(['all', 'never'], [], {}) == True)
    assert (t.evaluate_tags(['all', 'always'], [], {}) == True)
    assert (t.evaluate_tags([], ['all', 'never'], {}) == False)
    assert (t.evaluate_tags([], ['all', 'always'], {}) == True)
    assert (t.evaluate_tags([], ['never', 'always'], {}) == False)

# Generated at 2022-06-13 09:15:23.858170
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    task = TaskInclude()
    task._load_name = lambda x, y: 'task include foo'
    task._parent = Block()
    task._parent._parent = PlayContext()

    # Test that when only_tags is set to 'always' and tags is unset,
    # then task is run
    task.only_tags = ['always']
    task.tags = None
    assert task.evaluate_tags([], [], {}) == True

    task.only_tags = ['always']
    task.tags = AnsibleUnsafeText(u'foo')

# Generated at 2022-06-13 09:15:34.404962
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTest(Taggable):
        tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)
    # Create instance of class TaggableTest
    taggable_test = TaggableTest()
    taggable_test.tags = ['always']
    # Test with only_tags=['always'] and skip_tags=['never']
    assert taggable_test.evaluate_tags(['always'], ['never'],{})
    # Test with only_tags=['never'] and skip_tags=['always']
    assert not taggable_test.evaluate_tags(['never'], ['always'],{})
    # Test with only_tags=['never'] and skip_tags=['never']

# Generated at 2022-06-13 09:15:43.710851
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    # Create play for testing
    play_context = PlayContext()
    play = Play().load({}, play_context, None)
    assert play._loader is not None
    assert play._variable_manager is not None

    # Create task object
    task_ds = {
        'name': 'test task',
        'tags': []
    }
    task = play.load_task(task_ds, play_context)

    # Test basic result
    result = task.evaluate_tags([], [], {})
    assert result is True

    # Test result with only_tags
    result = task.evaluate_tags(['foo'], [], {})
    assert result is False
    task.tags = ['foo']

# Generated at 2022-06-13 09:15:55.059977
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    test_task = TaskInclude()
    test_task._lazy_load = False
    test_task._name = "test"
    test_task._ds = dict(tags=["A", "B"], always_run=True)
    test_task.post_validate(loader=None, templar=None) # populates the tags attribute
    assert test_task.evaluate_tags("", "", {}) == True
    assert test_task.evaluate_tags("A", "", {}) == True
    assert test_task.evaluate_tags("A,B", "", {}) == True
    assert test_task.evaluate_tags("A,C", "", {}) == True
    assert test_task.evaluate_tags("", "B", {}) == True
   

# Generated at 2022-06-13 09:16:05.340922
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task_include as task_include
    task_include.TaskInclude._load_tags = Taggable._load_tags
    task_include.TaskInclude.evaluate_tags = Taggable.evaluate_tags

    all_vars = dict()
    task_include_obj = task_include.TaskInclude(
        task=dict(),
        role=dict(),
        block=dict(),
        play=dict(
            tags=[
                ['tag1','tag2','tag3'],
            ],
        ),
    )
    assert task_include_obj.evaluate_tags(only_tags=['tag1'], skip_tags=[], all_vars=all_vars) == True

# Generated at 2022-06-13 09:16:14.803014
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # create a fake HostVars for variable substitution
    class HostVars(object):
        pass

    host_vars = HostVars()
    host_vars.var = "test"  # a fake variable

    # construct the object to be tested
    class TaggableTester(Taggable):
        pass

    taggable = TaggableTester()

    # check that the item is runnable (default behavior) if there
    # are no tags, no only_tags and no skip_tags
    assert taggable.evaluate_tags(None, None, host_vars.__dict__)

    # check that the item is runnable if tags match only_tags
    taggable.tags = ["test"]
    assert taggable.evaluate_tags(["test"], None, host_vars.__dict__)



# Generated at 2022-06-13 09:16:25.218381
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.helpers import load_list_of_blocks

    data = [
        {'name': 'first',
         'tags': ['always']},
        {'name': 'second',
         'tags': ['maybe']},
        {'name': 'third',
         'tags': ['never']},
    ]

    blocks = load_list_of_blocks(
        data,
        play=None,
        parent_block=None,
        task_include=TaskInclude,
        role=None,
        use_handlers=False,
    )
    blocks = [block for block in blocks if isinstance(block, TaskInclude)]
    results = [block.evaluate_tags(['all'], [], {}) for block in blocks]


# Generated at 2022-06-13 09:16:39.735278
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    
    from ansible.playbook.base import Base
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    import pytest
    
    obj = Task.load(dict(
        name="Task Name",
        tags="TestTest",
        role=Role.load(dict(
            name="Role Name",
            tags="TestTest"
        ))
    ))
    assert obj.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars={}) == True
    

# Generated at 2022-06-13 09:16:49.203891
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeTaggable:
        def __init__(self, tags=None, _loader=None):
            self.tags = tags
            self._loader = _loader

    # General case
    tags=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    only_tags=['a','c','e','g','i','k','m','o','q','s','u','w','y']
    skip_tags=['b','d','f','h','j','l','n','p','r','t','v','x','z']

    fake_taggable = FakeTaggable(tags=tags)
    assert fake_taggable.tags == tags
   

# Generated at 2022-06-13 09:17:16.672754
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TempTaggable(Taggable):
        ''' A class where the Taggable class can be tested '''
        pass

    temp_tagable = TempTaggable()

    temp_tagable.tags = ['some_tag']
    assert temp_tagable.evaluate_tags(None, None, None) == True

    temp_tagable.tags = ['never']
    assert temp_tagable.evaluate_tags(None, None, None) == False

    temp_tagable.tags = ['always']
    assert temp_tagable.evaluate_tags(None, None, None) == True

    temp_tagable.tags = None
    assert temp_tagable.evaluate_tags(None, None, None) == True

    temp_tagable.tags = ['some_tag']

# Generated at 2022-06-13 09:17:27.415067
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestTaggable(Taggable):
        _tags = FieldAttribute(isa='list', default=list, listof=string_types, extend=True)

    tt = TestTaggable()
    tt._actual_task = None
    tt._loader = None

    # Test run with no tags
    tt.tags = []
    assert tt.evaluate_tags([], [], {}) == True

    # Test run with only_tags set
    tt.tags = []
    assert tt.evaluate_tags(['a'], [], {}) == False

    tt.tags = ['a']
    assert tt.evaluate_tags(['a'], [], {}) == True

    tt.tags = ['untagged']
    assert tt.evaluate_tags(['a'], [], {}) == False



# Generated at 2022-06-13 09:17:38.219689
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyObject(Taggable):
        def __init__(self, tags=None):
            super(DummyObject, self).__init__()
            self.tags = tags

    # only_tags=[], skip_tags=[]
    my_tags = ['tagA']
    obj = DummyObject(tags = my_tags)
    assert obj.evaluate_tags([], [], {}) == True

    # only_tags=['tagA', 'tagB'], skip_tags=[]
    my_tags = ['tagA']
    obj = DummyObject(tags = my_tags)
    assert obj.evaluate_tags(['tagA', 'tagB'], [], {}) == True

    # only_tags=['tagA', 'tagB'], skip_tags=['tagB', 'tagC']
    my_tags

# Generated at 2022-06-13 09:17:50.099755
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task
    import ansible.template.template

# Generated at 2022-06-13 09:18:04.946283
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockLoader(object):
        def __init__(self):
            self.path_cache = {}

        def path_dwim(self, filename):
            return self.path_cache[filename]

    class MockTask(Taggable):
        def __init__(self, tags):
            self._loader = MockLoader()
            self.tags = tags

    tags1 = ['test1']
    tags2 = ['test2']
    tags3 = ['test3']
    tags4 = ['test4']
    tags1_and_2 = set(tags1)
    tags1_and_2.update(tags2)
    tags1_and_2 = list(tags1_and_2)
    tags3_and_4 = set(tags3)
    tags3_and_4.update(tags4)
    tags

# Generated at 2022-06-13 09:18:16.612736
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = []
    skip_tags = []

    # test for include plays
    play = dict(
        tags = ['untagged'],
    )
    assert Taggable(play).evaluate_tags(only_tags, skip_tags, {})

    play = dict(
        tags = ['tag1'],
    )
    assert not Taggable(play).evaluate_tags(only_tags, skip_tags, {})

    play = dict(
        tags = ['tag1', 'tag2'],
    )
    assert not Taggable(play).evaluate_tags(only_tags, skip_tags, {})

    only_tags = ['tag1']
    play = dict(
        tags = ['tag1', 'tag2'],
    )

# Generated at 2022-06-13 09:18:28.470114
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t.tags = ['always', 'atag']
    assert t.evaluate_tags(['always', 'all'], [], {})
    assert t.evaluate_tags(['atag', 'all'], [], {})
    assert t.evaluate_tags(['all', 'tagged'], [], {})
    assert t.evaluate_tags(['atag'], [], {})
    assert not t.evaluate_tags([], [], {})
    assert not t.evaluate_tags([], ['all', 'tagged'], {})
    assert not t.evaluate_tags([], ['always', 'all'], {})
    assert not t.evaluate_tags([], ['atag', 'all'], {})
    assert not t.evaluate_tags([], ['atag'], {})

# Generated at 2022-06-13 09:18:33.850609
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTaggable(Taggable):
        pass

    # Create empty object
    mt = MockTaggable()

    # Run the test
    mt.tags = ['tag1', 'tag2']
    print(mt.evaluate_tags(only_tags=['tag1'], skip_tags=[], all_vars=dict()))
    print(mt.evaluate_tags(only_tags=['tag1'], skip_tags=[], all_vars=dict()))


# Run the unit test
test_Taggable_evaluate_tags()



# Generated at 2022-06-13 09:18:46.116616
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        def __init__(self, tags, only_tags, skip_tags, all_vars):
            self.tags = tags
            self.only_tags = only_tags
            self.skip_tags = skip_tags
            self.all_vars = all_vars


    class MyLoader:
        pass


    # Tests
    my_loader = MyLoader()
    my_taggable = MyTaggable(tags = ['role:kubernetes'], only_tags = ['kubernetes'], skip_tags = ['docker'], all_vars = {'role': 'kubernetes'})
    my_taggable._loader = my_loader


# Generated at 2022-06-13 09:18:53.621678
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.base import Base

    loader = DataLoader()

    only_tags = set([u'tag1', u'tag2', u'tagged'])
    skip_tags = set([u'tag3', u'tag4', u'tagged'])
    all_vars = dict(test_var = u'test_value')
    test_tags = [u'tag1', u'tag2', u'tag3']
    untagged = frozenset(['untagged'])

    base = Base()
    base._loader = loader

    assert base.evaluate_tags(only_tags, skip_tags, all_vars) == True
    base.tags = test_tags

# Generated at 2022-06-13 09:19:17.847441
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    # empty tags should run
    variables = VariableManager()
    play_context = PlayContext(variable_manager=variables)
    play_context.only_tags = ['pizza']
    play_context.skip_tags = ['cheese']
    task = Task.load(dict(name='test task', action={'module': 'echo', 'args': {'msg': 'ok'}}, tags=['pizza']), play_context=play_context)
    assert task.evaluate_tags(play_context.only_tags, play_context.skip_tags, variables) is True

    # tags with only_tags
    variables = VariableManager()
    play_context = PlayContext

# Generated at 2022-06-13 09:19:24.037268
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # set up test
    class TaggableTest(Taggable):
        def __init__(self, loader=None, only_tags=None, skip_tags=None, tags=None):
            self._loader = loader
            self.only_tags = only_tags
            self.skip_tags = skip_tags
            self.tags = tags
    def _loader(self):
        return False
    record_loader = _loader
    only_tags = ['test_only_tag']
    skip_tags = ['test_skip_tag']
    all_vars = {}


# Generated at 2022-06-13 09:19:36.437439
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Instantiate a mock object
    class MockTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # Set the tag parameters of the method
    tags = ['a', 'b']
    only_tags = ['all', 'c']
    skip_tags = ['all']
    all_vars = {}

    # Instantiate an object of Taggable and call its method
    obj = MockTaggable(tags)
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars) == False

    # Set the tag parameters of the method
    tags = ['a', 'b']
    only_tags = ['all', 'c']
    skip_tags = ['all', 'd']
    all_vars = {}

    # Instantiate an object of Taggable

# Generated at 2022-06-13 09:19:45.349872
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import os
    import sys
    import tempfile
    import shutil
    import io
    import copy

    all_vars = dict()
    all_vars['test_tags'] = "test_pass"

    all_vars['test_tags2'] = [ "test_pass", "test_fail" ]

    check_only_tags = set(['test_pass', 'all'])
    check_skip_tags = set(['test_fail', 'all'])

    # Test a Taggable class (Role) with a single tag
    role = Role()
    role._load_name('role')
    role._role_path

# Generated at 2022-06-13 09:19:49.942657
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import sys

    if sys.version_info >= (3,0):
        string_types = (str,)
    else:
        string_types = (str, unicode)  # noqa

    class TestModule:
        def __init__(self):
            self._tags = None
        def __init__(self, _tags):
            self._tags = _tags

    import pytest

    test_modules = [ TestModule(),
                     TestModule(['for_all']), TestModule(['for_all', 'additional_tag']), TestModule(['never']),
                     TestModule(['for_all']), TestModule(['for_all_and_more']), TestModule(['additional_tag']), TestModule(['never'])]

    only_tags = None
    skip_tags = None

# Generated at 2022-06-13 09:19:57.930009
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    #First test case
    t = Taggable()
    t.tags = ['tag1', 'tag2', 'tag3']
    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3', 'tag4']
    assert t.evaluate_tags(only_tags,skip_tags, {}) == True
    #Second test case
    t = Taggable()
    t.tags = ['tag1', 'tag2', 'tag3']
    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3', 'tag4']
    assert t.evaluate_tags(only_tags,skip_tags, {}) == True
    #Third test case
    t = Taggable()
    t.tags = ['tag1', 'tag2', 'tag3']

# Generated at 2022-06-13 09:20:12.515212
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Simple test of evaluate_tags
    class Dummy(Taggable):
        _tags = ['a', 'b']
    d = Dummy()
    assert(d.evaluate_tags(['a', 'b'], [], {}) is True)
    assert(d.evaluate_tags(['a'], [], {}) is True)
    assert(d.evaluate_tags([], [], {}) is True)
    assert(d.evaluate_tags(['c'], [], {}) is False)

    # Test evaluation of 'all' tag
    assert(d.evaluate_tags(['all'], [], {}) is True)
    assert(d.evaluate_tags([], ['all'], {}) is False)
    # If tags are specified, don't include those tagged 'never'

# Generated at 2022-06-13 09:20:23.347938
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # create a fake instance of PlaybookInventory
    class FakeInventory:
        def __init__(self):
            self.hosts= { 'localhost': {} }

    # create a fake instance of PlayContext
    class FakePlayContext:
        def __init__(self):
            self.only_tags = []
            self.skip_tags = []
            self.tags = []
            self.inventory = FakeInventory()

    # create a fake instance of Task
    class FakeTask(Taggable):
        def __init__(self):
            self.tags = []
            self.vars = {}

    # create an instance of Taggable, since it is an abstract class we need to fake it
    taggable = FakeTask()

    # create an instance of PlayContext
    play_context = FakePlayContext()

    # first test

# Generated at 2022-06-13 09:20:36.083678
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import PlayBook
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    import os

    # Test 1: play with only_tags on tasks and handlers, default self.tags
    # Expected result: only tasks and handlers tagged with t1, t2, t3 are run (6 tasks + 1 handler)
    loader = DataLoader()

# Generated at 2022-06-13 09:20:49.935441
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block

    block = Block(play=None)

    # default, should run
    assert block.evaluate_tags(only_tags=[], skip_tags=[]) == True
    assert block.evaluate_tags(only_tags=[], skip_tags=['skipme']) == True
    assert block.evaluate_tags(only_tags=['runme'], skip_tags=[]) == True
    assert block.evaluate_tags(only_tags=['runme'], skip_tags=['skipme']) == True

    # if only_tags are specified, should not run
    block.tags = ['runme']
    assert block.evaluate_tags(only_tags=['runme'], skip_tags=['skipme']) == True

# Generated at 2022-06-13 09:21:29.335273
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableTest(Taggable):
        """ Testing the method Taggable.evaluate_tags(). """

        def __init__(self, tags):
            super(TaggableTest, self).__init__(tags)

    #____________ Positive tests, the items should run ____________________
    # Any task, without tags, it should run
    t = TaggableTest([])
    assert(t.evaluate_tags( [], [], []) == True)
    assert(t.evaluate_tags( ['all'], [], []) == True)
    assert(t.evaluate_tags( [], ['all'], []) == True)
    assert(t.evaluate_tags( ['all'], ['all'], []) == True)

    # Any task, tagged, the tag 'all' matches, it should run
    t = Tagg

# Generated at 2022-06-13 09:21:40.886440
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' Unit test for evaluating tags (does not require a playbook file) '''

    from ansible.playbook import Play
    from ansible.playbook.play import Play as PlayObject

    pb = Play()
    play_context = pb.set_play_context({})
    play_context.load_vars_prompt = lambda x, y: None
    play_context.check_password_prompt = lambda x: True

    # create a playbook task
    play_source =  dict(
        name = "test_task",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='command', args="echo 'TASK'")),
        ]
    )

    # create a play

# Generated at 2022-06-13 09:21:49.226143
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggableClass(Taggable):
        pass

    test_class = TestTaggableClass()
    # test_class.tags = {'test_tag'}
    test_class.tags = ['test_tag']

    # Test tag not in only_tags but also not in skip_tags
    only_tags = ['only1', 'only2']
    skip_tags = ['skip1', 'skip2']
    assert test_class.evaluate_tags(only_tags, skip_tags, {}) == False
    # Test tag in only_tags but not in skip_tags
    only_tags = ['only1', 'only2', 'test_tag']
    skip_tags = ['skip1', 'skip2']
    assert test_class.evaluate_tags(only_tags, skip_tags, {}) == True
    # Test

# Generated at 2022-06-13 09:21:55.437473
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.helpers import load_list_of_tasks
    from ansible.playbook.block import Block
    from ansible.utils.vars import combine_vars
    from ansible.vars.hostvars import HostVars

    test_host = HostVars(dict(ansible_all_ipv4_addresses=['192.168.1.1'],
                              ansible_default_ipv4=dict(address='192.168.1.1',
                                                        alias='eth0:0',
                                                        interface='eth0',
                                                        type='ether')))
    include_task = TaskInclude()
    include_task._load_name("task with 'foo' tag")
    include_task._load

# Generated at 2022-06-13 09:22:05.115491
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task

    task = Task()
    task._loader = None
    assert task.evaluate_tags(only_tags=[], skip_tags=[])
    assert not task.evaluate_tags(only_tags=['something'], skip_tags=[])

    task._tags = ['something']
    assert task.evaluate_tags(only_tags=['something'], skip_tags=[])
    assert not task.evaluate_tags(only_tags=['something_else'], skip_tags=[])
    assert not task.evaluate_tags(only_tags=['something', 'something_else'], skip_tags=[])
    assert task.evaluate_tags(only_tags=['something'], skip_tags=['something_else'])

# Generated at 2022-06-13 09:22:15.810482
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    taggable = Taggable()
    assert taggable.evaluate_tags(['all'], [], {}) is True
    assert taggable.evaluate_tags(['all'], ['never'], {}) is False
    assert taggable.evaluate_tags(['all'], ['always'], {}) is True
    assert taggable.evaluate_tags([], ['never'], {}) is True
    assert taggable.evaluate_tags([], ['always'], {}) is True
    assert taggable.evaluate_tags(['all'], ['tagged'], {}) is True
    assert taggable.evaluate_tags(['all'], ['tagged'], {'tags': ['never']}) is False

# Generated at 2022-06-13 09:22:27.284945
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableSubClass(Taggable):
        def __init__(self):
            self.tags = list()

    taggable = TaggableSubClass()

    # Default case
    taggable.tags = list()
    assert taggable.evaluate_tags([], [], {})

    # Run all tagged tasks
    taggable.tags = list()
    assert taggable.evaluate_tags(['tagged'], [], {})
    taggable.tags = ['tagged']
    assert taggable.evaluate_tags(['tagged'], [], {})

    # Run all tasks
    taggable.tags = list()
    assert taggable.evaluate_tags(['all'], [], {})
    taggable.tags = ['tagged']

# Generated at 2022-06-13 09:22:36.024022
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    templar = Templar(loader=DataLoader(), variables=VariableManager())
    inventory = InventoryManager(loader=DataLoader(), sources=['hosts'])

# Generated at 2022-06-13 09:22:41.920665
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class DummyTaggable(Taggable):
        def __init__(self):
            self.tags = []

    taggable = DummyTaggable()

    # Test default run (no tags on task and no tags on execution)
    assert taggable.evaluate_tags(only_tags=[], skip_tags=[]) == True

    # Test run tagged task (no tags on execution)
    taggable.tags = ['test_tag']
    assert taggable.evaluate_tags(only_tags=[], skip_tags=[]) == True

    # Test run not tagged task (no tags on execution)
    taggable.tags = []
    assert taggable.evaluate_tags(only_tags=[], skip_tags=[]) == True

    # Test run task matching only_tags of execution

# Generated at 2022-06-13 09:22:51.336548
# Unit test for method evaluate_tags of class Taggable