

# Generated at 2022-06-13 13:42:10.574552
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock a LookupModule instance with a mocked _get_file_contents()
    # method that returns the filename as the file content.
    # This is used to skip file reading so we can check existence.
    mock_self = type('', (), {
        '_get_file_contents': lambda self, filename: filename,
        'find_file_in_search_path': lambda self, variables, subdir, filename, ignore_missing=False: filename,
    })()

    # Get the run() from class LookupModule
    lookup_module_run = LookupModule.run

    # Check first_found return value
    assert lookup_module_run(mock_self, ['/path/test.txt'], None) == ['/path/test.txt']

    # Check first_found return value with multiple entries
    assert lookup_module_

# Generated at 2022-06-13 13:42:18.398451
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: change with proper error handling and add extra testing
    item = 'testing'
    variables = {}
    terms = {}
    skip = False
    lookup_plugin = LookupModule()
    lookup_plugin.run(terms, variables, skip)

    try:
        lookup_plugin.run(item, variables, skip)
    except AnsibleLookupError:
        # should throw error
        pass

# Generated at 2022-06-13 13:42:28.097046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit test for method LookupModule.run
    '''
    import mock
    module = mock.Mock()

# Generated at 2022-06-13 13:42:34.639741
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.first_found
    lm = ansible.plugins.lookup.first_found.LookupModule()

# Generated at 2022-06-13 13:42:45.899406
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    class Options(object):
        connection = None
        module_path = None
        forks = 10
        become = None
        become_method = None
        become_user = None
        check = None
        diff = None
        listhosts = None
        listtasks = None
        listtags = None
        syntax = None
        private_key_file = None
        verbosity = None

    # Initialize variables
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader)
    options = Options()
    variable_manager

# Generated at 2022-06-13 13:42:55.945300
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test without paths and without files
    terms = ['/tmp/foo.txt']
    variables = {}
    kwargs = {}
    lookup_obj = LookupModule()
    result = lookup_obj.run(terms, variables, **kwargs)
    assert result == ['/tmp/foo.txt']

    # test with paths and without files
    terms = ['/tmp/foo.txt']
    variables = {}
    kwargs = {'paths': '/tmp/foo.txt'}
    lookup_obj = LookupModule()
    result = lookup_obj.run(terms, variables, **kwargs)
    assert result == ['/tmp/foo.txt']

    # test without paths and with files
    terms = ['/tmp/foo.txt']
    variables = {}

# Generated at 2022-06-13 13:43:07.997545
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # get data to test with
    #import json
    #with open('host_vars/all.yml', 'r') as f:
    #    data = json.load(f)

    # create lookup object
    lm = LookupModule()

    # test with no data, expect no files found
    terms = [ {'files': '/some/file', 'paths': ['/tmp/path']} ]
    retval = lm.run(terms, {}, {})
    assert retval == []

    # test with files, expect file found
    terms = [ {'files': 'README.md', 'paths': ['./']} ]
    retval = lm.run(terms, {}, {})

# Generated at 2022-06-13 13:43:16.148615
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # creates class instance (LookupModule)
    lookup = LookupModule()

    # dictionary to pass for terms argument
    terms = {
        'files': 'foo,bar',
        'paths': 'path/to1,path/to2',
        'skip': True
    }

    # dictionary to pass for variables argument
    variables = {}

    # dictionary to pass for kwargs argument
    kwargs = {}

    # create directory to store files
    import tempfile
    from ansible.module_utils._text import to_bytes
    from shutil import rmtree
    temp_dir = tempfile.mkdtemp()
    path1 = to_bytes(os.path.join(temp_dir, 'path', 'to1'))

# Generated at 2022-06-13 13:43:17.525440
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement a unit test
    pass

# Generated at 2022-06-13 13:43:27.556479
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test complex structure
    test_subject = LookupModule()
    test_subject._load_name = 'first_found'
    test_subject._options = {'files': [], 'paths': [], 'skip': False}

    # setup 0: simple string
    params = ['foo.txt']
    expected_result = ['foo.txt']
    assert expected_result == test_subject.run(params, {})

    # setup 1: simple list
    params = [
        ['foo.txt'],
        ['bar.txt', 'whiz.txt'],
    ]
    expected_result = ['foo.txt', 'bar.txt', 'whiz.txt']
    assert expected_result == test_subject.run(params, {})

    # setup 2: hard list

# Generated at 2022-06-13 13:43:41.065332
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with dictionary as terms

    terms = [{'files': 'foo1', 'paths': ''}]
    modules = LookupModule()
    result = modules.run(terms)
    assert result == ['foo1']

    terms = [{'files': 'foo2', 'paths': ''}]
    modules = LookupModule()
    result = modules.run(terms)
    assert result == ['foo2']

    terms = [{'files': 'foo3', 'paths': ''}]
    modules = LookupModule()
    result = modules.run(terms)
    assert result == ['foo3']

    terms = [{'files': 'foo4', 'paths': ''}]
    modules = LookupModule()
    result = modules.run(terms)
    assert result == ['foo4']


# Generated at 2022-06-13 13:43:48.829149
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    lookup_plugin = LookupModule()

    p = '/path/to/foo'
    f1 = '/path/to/foo.cnf'
    f2 = '/path/to/foo.yml'
    f3 = '/path/to/foo.py'
    f4 = '/path/to/foo.rb'
    f5 = '/path/to/else.cnf'
    f6 = '/path/to/else.yml'
    f7 = '/path/to/else.py'
    f8 = '/path/to/else.rb'

    # Test dict mode
    #   - use only relation mode
    #   - use only absolute mode
    #   - use relation mode and absolute mode
    #  

# Generated at 2022-06-13 13:43:58.919630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    # pylint: disable=too-many-arguments
    def _run(terms, variables):
        # pylint: disable=no-member
        return LookupModule().run(terms, variables)

    # pylint: disable=no-member
    def _strip_paths(paths):
        return ["%s/%s" % (LookupModule._basedir, p) for p in paths]

    terms = {'files': ['foo', 'bar', 'dkjfhskdjfh'], 'paths': ['../test/test_data']}
    assert _run(terms, {}) == _strip_paths(['foo'])


# Generated at 2022-06-13 13:44:09.100479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.module_utils.six import StringIO
    from ansible.utils.path import makedirs_safe

    # used for the test

# Generated at 2022-06-13 13:44:15.083340
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    import tempfile
    import shutil
    import os
    import stat

    class TestLookupModule(LookupModule):
        def __init__(self, module_name=None, templar=None, loader=None, paths=None, shares=None, variables=None,
                     **kwargs):
            self.test_module_name = module_name
            self.test_templar = templar
            self.test_loader = loader
            self.test_paths = paths
            self.test_shares = shares
            self.test_variables = variables
            self.test_kwargs = kwargs
            self.return_value = ["/tmp/foo.txt"]


# Generated at 2022-06-13 13:44:25.770231
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test method run of class LookupModule
    """
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    # if no file found, run raises an exception of type AnsibleLookupError
    try:
        look = LookupModule(templar)
        look.run([{'files': ['foo.txt'], 'paths': ['/tmp', '/root'], 'skip': False}], None, errors='strict')
        assert False
    except AnsibleLookupError as e:
        assert e.__class__.__name__ == 'AnsibleLookupError'

    # if no file found, run returns an empty list which is the expected value
    look = LookupModule(templar)

# Generated at 2022-06-13 13:44:36.486774
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # no files, no paths
    terms = []
    variables = dict()
    kwargs = dict()
    total_search, skip = lookup._process_terms(terms, variables, kwargs)
    output = lookup.run(terms, variables, **kwargs)
    assert output == []

    # one file, no paths
    terms = ["file1"]
    variables = dict()
    kwargs = dict()
    total_search, skip = lookup._process_terms(terms, variables, kwargs)
    output = lookup.run(terms, variables, **kwargs)
    assert output == []

    # one file, one path
    terms = ["file1"]
    variables = dict()
    kwargs = dict()
    kwargs["paths"] = ["path1"]
    total

# Generated at 2022-06-13 13:44:48.094708
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def load_defer(t):
        return {'test': t}

    def load_first(t):
        return t['test']

    partial_test = {
        'test': 'first',
        'skip': False,
    }
    full_test = {
        '__ansible_arguments__': [load_first],
        '__ansible_lookup_plugin__': 'first_found',
        '__ansible_lookup_terms__': [load_defer(partial_test), 'second', partial_test],
    }
    result = LookupModule().run(full_test['__ansible_lookup_terms__'], full_test, defer_results=True)
    # check that it returned a list of 1 item
    assert len(result) == 1

# Generated at 2022-06-13 13:44:59.779911
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.utils.path import unfrackpath
    from ansible.utils import context_objects as co

    rootdir = tempfile.mkdtemp()

    # Setup the first_found test files
    os.mkdir(os.path.join(rootdir, 'a'))
    os.mkdir(os.path.join(rootdir, 'b'))
    os.mkdir(os.path.join(rootdir, 'c'))
    open(os.path.join(rootdir, 'a', 'file1.txt'), 'w').close()
    open(os.path.join(rootdir, 'a', 'file2.txt'), 'w').close()
    open(os.path.join(rootdir, 'b', 'file1.txt'), 'w').close()

   

# Generated at 2022-06-13 13:45:00.978978
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert True

# Generated at 2022-06-13 13:45:18.454169
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # The import of Ansible-2.1 classes fails while running under python2.6
    # and needs to be skipped.
    import sys
    if sys.version_info[:2] == (2, 6):
            return

    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    class DummyHost:
        name = "dummyNinja"
        vars = HostVars(vars={"var1": "item1"})

    class DummyPlay:
        def __init__(self):
            self.vars = VariableManager()

        def get_variable_manager(self):
            return self.vars

        def get_variable_manager(self):
            return self.vars


# Generated at 2022-06-13 13:45:21.470781
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    #TODO: Add unit test cases
    pass


# Generated at 2022-06-13 13:45:32.363364
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    # successfully find file1.txt
    ret = lm.run(
        terms=[{"files": "file1.txt", "paths": "/tmp/, /etc/"}, "files/file2.txt"],
        variables={'inventory_hostname': 'all'}
    )
    assert ret == ['/tmp/file1.txt']

    # raises No file was found when using first_found.
    try:
        ret = lm.run(
            terms=[{"files": "file1.txt", "paths": "/tmp/, /etc/"}, "files/file2.txt", "file3.txt"],
            variables={'inventory_hostname': 'all'}
        )
    except AnsibleLookupError:
        pass

# Generated at 2022-06-13 13:45:40.656703
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The 'terms' and 'variables' parameters of run method are not involved in the test of this method.
    # So, they can be filled with arbitrary values.
    terms = ['foo', 'bar']
    variables = {}

    # create a LookupModule instance to test
    test_instance = LookupModule()

    # override method find_file_in_search_path and make it always return None
    def mock_find_file_in_search_path(var, sub, file, ign):
        return None
    test_instance.find_file_in_search_path = mock_find_file_in_search_path

    # test when skip is False
    skip = False
    result = test_instance.run(terms, variables, skip=skip)
    assert result == []

    # test when skip is True
    skip = True


# Generated at 2022-06-13 13:45:48.735455
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    lookup = LookupModule()
    lookup._templar = NameMapper('AnsibleUndefinedVariable', 'UndefinedError')
    lookup._templar.template = lambda x: x

    # Exercise
    terms = list()
    terms.append({'files': 'foo'})
    terms.append({'files': 'foo', 'paths': 'bar'})
    terms.append({'paths': 'bar'})
    variables = dict()
    result = lookup.run(terms, variables)

    # Verify
    assert result == [], 'Expected empty list'


# Generated at 2022-06-13 13:45:54.718610
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Generate a fake action plugin object
    class FakeActionModule(object):
        def __init__(self):
            self.task_vars = dict()
        def _dump_results(self, result, result_type, task_result=None, add_to_cache=False):
            return result, result_type, task_result

    fake_action_module = FakeActionModule()

    # Create a fake lookup plugin object
    l = LookupModule()
    l.set_loader({})
    l.set_env(fake_action_module)

    # Create a templar
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    templar = Templar(loader=None, variables={})
    templar._available_variables = dict()

   

# Generated at 2022-06-13 13:46:02.771440
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mocks

    class MockTemplar:
        def __init__(self):
            self.templates = []
        def template(self, template):
            self.templates.append(template)
            return template

    class MockVariables:
        def __init__(self):
            pass

    class MockSearchPath:
        def __init__(self):
            self.searches = []
        def search(self, variables, subdir, fn, ignore_missing=True):
            self.searches.append((variables, subdir, fn, ignore_missing))
            return '/path/to/file'

    class MockLookupBase:
        def __init__(self, variables, templar, search_path):
            self._variables = variables
            self._templar = templar
            self._

# Generated at 2022-06-13 13:46:14.328996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given variables
    variables = {}

    # given arguments
    #tests_files = {"files": ["foo", "bar"], "paths": ["/path/1", "/path/2"]}
    #tests_paths = {"files": ["foo", "bar", "baz"], "paths": ["/path/1", "/path/2"]}

    # given additional arguments
    kwargs = {}

    # given object
    lookup_obj = LookupModule()

    #assert lookup_obj.run([tests_paths], variables, **kwargs) == [*, *, *]
    #assert lookup_obj.run([tests_paths], variables, **kwargs) == [*, *, *, *, *, *]

# Generated at 2022-06-13 13:46:21.925930
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.config.manager import ConfigManager
    config = ConfigManager(parser=None, run_once=True, usage='', output_opts=False).get_settings()
    config._next_config_path = lambda x: config

    module = LookupModule(
        loader=None,
        templar=None, # TODO:
        shared_loader_obj=None,
        variables={},
    )
    import os
    module._subdir = 'search/subdir'
    module.set_options(direct=dict(paths=[os.path.dirname(__file__)], files=['file1.txt', 'file2.txt']))
    module.run([], {})


# Generated at 2022-06-13 13:46:31.911948
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestVars:
        def __init__(self):
            self.hostvars = {
                'host1': {
                    'hostvars': {
                        'username': 'pratik',
                        'home': '/home/pratik'
                    }
                },
                'host2': {
                    'hostvars': {
                        'username': 'test',
                        'home': '/home/test'
                    }
                }
            }
            self.basedir = '/home/ansible/test_ansible_playbook'
        def get_vars(self, loader=None, play=None, host=None, task=None):
            return self.hostvars.get(host)['hostvars']
    lookup = LookupModule()

# Generated at 2022-06-13 13:46:52.008472
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(loader=None, templar=None, **{}).run(terms=None, variables=None) == []
    assert LookupModule(loader=None, templar=None, **{}).run(terms=['/path/to/foo.txt'], variables=None) == ['/path/to/foo.txt']
    assert LookupModule(loader=None, templar=None, **{}).run(terms=[{'files': "/path/to/foo.txt"}], variables=None) == ['/path/to/foo.txt']

# Generated at 2022-06-13 13:47:01.876006
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''

    # Patch getattr to avoid AnsibleUndefinedVariable exception
    from ansible.module_utils.six.moves import builtins
    setattr(builtins, 'getattr', lambda *args, **kwargs: '')

    import tempfile
    tmp_file_path = tempfile.mkstemp()[1]

    (isinstance(LookupModule().run([], {}), list))
    (isinstance(LookupModule().run(['foo'], {}), list))
    (isinstance(LookupModule().run([{}], {}), list))
    (isinstance(LookupModule().run(['foo', 'bar'], {}), list))
    (isinstance(LookupModule().run([['foo', 'bar'], {}], {}), list))

# Generated at 2022-06-13 13:47:09.803613
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lookup_module = LookupModule()

    fake_variables = dict()
    # TODO: Fix to use LookupPlugin class to set options
    fake_kwargs = dict()

    # Verify that no file has been found for an invalid path
    with pytest.raises(AnsibleLookupError):
        fake_file_list = list()
        lookup_module.run(fake_file_list, fake_variables, **fake_kwargs)

# Generated at 2022-06-13 13:47:18.452616
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Given:
    l = LookupModule()
    l._templar = None

    # When:
    #  - terms = list of strings, 'path' exists and 'fn' exists
    #  - terms = list of strings, 'path' exists and 'fn' does not exist
    #  - terms = list of strings, 'path' does not exists and 'fn' does not exist
    #  - terms = list of strings, 'path' exists and there is no 'fn'
    #  - terms = list of strings, 'path' does not exists and there is no 'fn'
    #  - terms = list with one item that is a string, 'path' exists and 'fn' exists
    #  - terms = list with one item that is a string, 'path' exists and 'fn' does not exist
    #  - terms = list with

# Generated at 2022-06-13 13:47:29.857761
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['foo.txt']
    plugins_path = ''
    loader = None
    variable_manager = None
    loader_class = None
    class Task(object):
        def __init__(self):
            self.name = 'name'
            self.args = dict()
        def copy(self):
            return Task()
    class PlayContext(object):
        def __init__(self):
            self.default_vars = dict()
            self.vars = dict()
            self.vars_prompt = dict()
            self.prompt = dict()
            self.ask_pass = False
            self.ask_sudo_pass = False
            self.ask_su_pass = False
            self.become = False
            self.become_method = False
            self.become_user = False
            self

# Generated at 2022-06-13 13:47:36.639999
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from jinja2.exceptions import UndefinedError

    with pytest.raises(AnsibleLookupError):
        LookupModule().run(['foo'], dict())

    def _s(s):
        return [s]

    l = LookupModule()

    with pytest.raises(AnsibleLookupError):
        # no file found
        l.run(['/etc/passwd'], dict())

    # NOTE: this is not right, we're testing a different code path
    # should test first_found as part of a task and get the include_role subdir 'files'
    # l = LookupModule(loader=DictDataLoader({'/etc/passwd': ''}),
    #                  variables=dict())
    l = LookupModule()
    l._loader = l.loader

# Generated at 2022-06-13 13:47:48.224153
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import types
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    plugins = (LookupModule,)
    class FakeVarManager(Mapping):
        def __init__(self, data):
            self._data = data
        def __getitem__(self, key):
            return self._data.get(key)
        def __setitem__(self, key, value):
            self._data[key] = value
        def __delitem__(self, key):
            del self._data[key]
        def __iter__(self):
            return iter(self._data)
        def __len__(self):
            return len(self._data)
        def __contains__(self, key):
            return key in self._data

# Generated at 2022-06-13 13:47:58.599299
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # ----------------------------------------

    # verify files in list but no paths specified
    # first _process_terms returns correct data
    lookup_module = LookupModule()
    terms = ['files/file1.txt', 'file2.txt', {'files': ['baz.txt'], 'paths': ['path/to/']}]
    lookup_module.set_options(var_options={}, direct={'skip': False})
    total_search, skip = lookup_module._process_terms(terms, {}, {})
    assert skip == False
    assert len(total_search) == 3
    assert total_search == ['files/file1.txt', 'file2.txt', 'baz.txt']
    # then run returns correct result
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:48:11.680558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    First found lookup look for the first existing file in a list of files
    and return the path to it.
    """

    # TODO: fix this abomination
    # TODO: add correct junit integration to make this a proper test

    test00 = dict(
        files=['/path/to/foo.txt', ],
        paths=[]
    )

    test01 = dict(
        files=['/path/to/foo.txt', '/path/to/bar.txt'],
        paths=[]
    )

    test02 = dict(
        files=['/path/to/foo.txt', 'bar.txt'],
        paths=[]
    )


# Generated at 2022-06-13 13:48:16.923180
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm.set_options({'files': ["/path/to/foo.txt", "bar.txt", "/path/to/biz.txt"], 'paths': [], 'skip': False})
    res = lm.run([], [])
    assert res == ['/path/to/foo.txt']

    lm.set_options({'files': ["/path/to/foo.txt", "bar.txt", "/path/to/biz.txt"], 'paths': [], 'skip': True})
    res = lm.run([], [])
    assert res == []


# Generated at 2022-06-13 13:48:48.046548
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible_collections.ansible.netcommon.plugins.module_utils.netcommon import load_provider
    from ansible.module_utils.facts.network.base import get_network_module
    from ansible.module_utils.facts.network.interfaces import Interfaces
    from ansible.module_utils.facts.network.generic import Generic as GenericNetwork
    from ansible.module_utils.facts.processor.base import get_processor_module
    from ansible.module_utils.facts.processor.cpuinfo import Cpuinfo as CpuinfoProcessor
    from ansible.module_utils.facts.system.base import get_system_module
    from ansible.module_utils.facts.system.distribution import Distribution as SystemDistribution


# Generated at 2022-06-13 13:48:55.803368
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    templar = "_templar"
    setattr(lookup_module, '_templar', templar)
    find_file_in_search_path = "_find_file_in_search_path"
    setattr(lookup_module, '_find_file_in_search_path', find_file_in_search_path)
    _variables = "_variables"

    # test raise AnsibleUndefinedVariable(msg)
    terms = [{'files': 'file1'}, "_variables"]
    setattr(lookup_module, 'run', terms)
    variables = {'variable': 'value'}

# Generated at 2022-06-13 13:49:07.413007
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test_one_of_many_files_in_one_of_many_paths_without_list_of_files_parameter
    lookup_instance = LookupModule()
    lookup_instance._find_file_in_search_path = lambda x, y, z: None

    terms = [{'files': 'file1', 'paths': 'p1,p2'}]
    variables = {}
    kwargs = {}
    result = lookup_instance.run(terms, variables, **kwargs)
    assert result == []

    # test_one_of_many_files_in_one_of_many_paths_without_list_of_files_parameter
    lookup_instance = LookupModule()
    lookup_instance._find_file_in_search_path = lambda x, y, z: None

   

# Generated at 2022-06-13 13:49:16.644935
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    class MockTemplar:
        def template(self, fn):
            return fn

    class MockAnsibleUndefinedVariable(AnsibleUndefinedVariable):
        pass

    class MockAnsibleUndefinedLookupVariable(AnsibleLookupError):
        pass

    class MockLookupBase:
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=True):
            return fn

    class MockLookupModule(MockLookupBase):
        _subdir = None
        _templar = MockTemplar()
        options = None
        path = None

        def set_options(self, var_options, direct):
            self.options = direct

        def get_option(self, option):
            return self.options.get(option)


# Generated at 2022-06-13 13:49:22.620729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: this needs better assertions
    # TODO: this needs better use of host and inventory
    # TODO: need to capture stdout of the subprocess

    try:
        terms = [ {"files": ["a"]}, {"files": ["b"]}]
        lu = LookupModule()
        lu.run(terms=terms, variables=dict())
    except Exception as e:
        assert e.args[0] == "No file was found when using first_found."

# Generated at 2022-06-13 13:49:28.997389
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [{'files': 'foo', 'path': None},
             {'files': 'bar', 'path': None},
             {'files': 'baz', 'path': None}]
    lookup_plugin = LookupModule()
    actual_result = lookup_plugin.run(terms=terms, variables={})
    expected_result = ['foo']
    assert actual_result == expected_result

# Generated at 2022-06-13 13:49:44.841727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    search_path = ['/opt/ansible/plugins/lookup/first_found']
    fp = search_path[0]
    lookup = LookupModule()
    lookup.basedir = os.path.dirname(fp)

    # setup test parameters
    #TODO: consider refactor and use another method
    lookup._templar = None
    lookup._loader = None
    lookup._finder = None

    # NOTE: this the following structure is broken, meaning
    # it does not do what it is expected.
    # it should use 'append' for files and paths.
    # otherwise it clobbers any entry with the last one
    # what is expected to be used as 'global'
    # this is also true for the 'skip' option.
    # perhaps the best way to fix it is to disallow
    # the above form

# Generated at 2022-06-13 13:49:53.338373
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test: no files found
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=dict(), direct={'files': ['foo.txt'], 'paths': ['/tmp']})

    results = lookup_module.run(terms=['foo.txt'], variables=dict())
    assert results == []

    # Test: one file found
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=dict(), direct={'files': ['foo.txt'], 'paths': [os.path.join(os.path.dirname(__file__), 'unit')]})

    results = lookup_module.run(terms=['foo.txt'], variables=dict())

# Generated at 2022-06-13 13:50:07.535422
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This unit test was automatically created from a code snippet
    # created on 2020-08-07 12:02:49 by Gluon Touch IDE on the following platforms:
    #   - Darwin (macOS) 18.7.0, 64-bit Intel Core i5
    #   - Ubuntu 18.04.3 LTS, 64-bit Intel Xeon Silver 4110
    #   - Windows 10.0.18362, 64-bit AMD Ryzen Threadripper 2970WX
    #   - Windows 10.0.10240.16384, 64-bit Intel Celeron N2830

    # Unit test setup (automatically created)
    LookupModule = lookup_plugins['first_found'].__class__

# Generated at 2022-06-13 13:50:19.740203
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # lookups change with ansible version and when using ansible-base,
    # ansible continues to be installed via pip, so we need to mock the correct
    # version to get the correct imports
    #
    # versions later than 2.11.0 have ansible_base installed, so we need to mock
    # 2.11.0 to get the correct import statements
    if 'ansible_base' in sys.modules:
        ansible_version = '2.11.0'
    else:
        ansible_version = '2.9.0'

    sys.modules['ansible'] = MagicMock()
    sys.modules['ansible.module_utils.six'] = MagicMock()
    sys.modules['ansible.module_utils.six.string_types'] = MagicMock()

# Generated at 2022-06-13 13:50:53.534551
# Unit test for method run of class LookupModule
def test_LookupModule_run():

  # Create an instance of class LookupModule
  lookupModule = LookupModule()
  # Create terms - first_found files are relative to the task execution path unless they are prefixed with a path
  terms = [ '/path1/dir1/dir11/dir111/file1.txt',
            'path1/dir1/dir11/dir111/file2.txt',
            'path1/dir1/dir11/dir112/file3.txt']
  # Create variables
  variables = {}
  # Create a kwargs object
  kwargs = {}
  # Call method run of class LookupModule
  lookupModule.run(terms, variables, **kwargs)

# Generated at 2022-06-13 13:51:05.255611
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert(LookupModule('').run([],{},files=[],paths=[]) == [])
    assert(LookupModule('').run([],{},files=['*.com'],paths=['/etc/logs', '/var/logs']) == [])
    assert(LookupModule('').run([],{},files=['*.conf', '*.py'],paths=['/etc/logs', '/var/logs']) == [])
    assert(LookupModule('').run([],{},files=['*.conf', '*.py'],paths=['/etc/logs', '/var/logs']) == [])

# Generated at 2022-06-13 13:51:13.619694
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class OptionsModule(object):
        def get_option(self, *args):
            # Mock of self.get_option().
            # Returned values are not important.

            return None

    class VariablesModule(object):
        def __init__(self, variables):
            self.variables = variables

        def get(self, name, varargs=None, kwargs=None, default=None):
            # Mock of self._variables.get().

            return self.variables.get(name, default)

    class TemplarModule(object):

        def __init__(self, variables):
            self.variables = variables

        class Undefined(object):
            # Mock of class Undefined.

            pass


# Generated at 2022-06-13 13:51:23.913790
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm._subdir = 'files'
    assert lm.run(['notthere.txt'], dict(ANSIBLE_MODULE_UTILS='test'), skip=True) == []
    assert lm.run(['notthere.txt'], dict(ANSIBLE_MODULE_UTILS='test'), skip=False) == None
    assert lm.run(['ANSIBLE_MODULE_UTILS/lookup_plugins/test.txt'], dict(ANSIBLE_MODULE_UTILS='test'), skip=True) == \
        ["test/unit/lookup_plugins/files/first_found/ANSIBLE_MODULE_UTILS/lookup_plugins/test.txt"]

# Generated at 2022-06-13 13:51:24.511387
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:51:29.043360
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:51:38.190982
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    lookup_module = LookupModule()
    variable_manager = ansible.vars.VariableManager()
    variable_manager._extra_vars = {}
    variable_manager._options_vars = {}
    variable_manager._fact_cache = {}
    variable_manager.set_available_variables(
        loader=ansible.parsing.dataloader.DataLoader(),
        variables=variable_manager._fact_cache
    )
    loader = ansible.parsing.dataloader.DataLoader()
    templar = ansible.template.Templar(loader=loader, variable_manager=variable_manager)
    variable_manager._templar = templar
    variable_manager._variables = variable_manager._extra_vars.copy()

# Generated at 2022-06-13 13:51:47.028773
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create dummy variables to use
    variables = {}

    # create instance of class
    l = LookupModule()

    # set search path
    l._searchpath = '/home/richard/tmp/ansible/'

    # used to set subdir for testing
    l._subdir = 'files'

    # ----------------------------------------------------
    # test with valid 'terms'
    # ----------------------------------------------------

    # run with terms that contains 'files' and 'paths' and a valid searchpath
    total_search, skip = l._process_terms([{'files': 'one two,three', 'paths': 'four:five six'}], variables, {})
    # assert that only one path was found in total_search
    assert len(total_search) == 1

    # run with terms that contains 'files' and 'paths' and a valid searchpath


# Generated at 2022-06-13 13:52:00.497653
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # mock _load_plugins method to silence a warning and to make the test run faster (no plugin loading)
    lookup._load_plugins = lambda searchpath: None
    lookup.set_options({'files': ['foo.conf', 'bar.conf'], 'paths': ['.', './files', '/etc']})