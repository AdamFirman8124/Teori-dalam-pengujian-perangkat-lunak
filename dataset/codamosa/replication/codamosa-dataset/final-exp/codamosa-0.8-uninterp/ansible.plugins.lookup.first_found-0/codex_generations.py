

# Generated at 2022-06-13 13:42:11.088387
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # class
    p = LookupModule()

    # Tests for the function run of class LookupModule
    # test with a empty dictionary
    terms = {}
    variables = [{}]
    with pytest.raises(AnsibleLookupError) as e_info:
        p.run(terms, variables)
    # test with a simple dictionary with path and file list
    terms = [{'files': ['foo', 'bar'], 'paths': ['path1', 'path2']}]
    variables = [{}]
    assert p.run(terms, variables) == []
    # test with a dictionary with path and file list
    terms = [{'files': ['foo', 'bar'], 'paths': ['path1', 'path2']}]

# Generated at 2022-06-13 13:42:22.577665
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    lookup_plugin.basedir = os.path.join(os.path.dirname(__file__), '../fixtures/lookup_plugins')
    lookup_plugin.set_options(direct={'paths': 'lookup_plugins'})

    assert lookup_plugin.run(['with_list'], {}) == ['lookup_plugins/with_list.txt']

    lookup_plugin.set_options(direct={'paths': 'lookup_plugins', 'test': 'not_found'})

    assert lookup_plugin.run('not_found', {}) == []

# Generated at 2022-06-13 13:42:26.942345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with empty input
    lookup1 = LookupModule()
    assert lookup1.run([''], ['']) is None
    # test with valid input
    lookup2 = LookupModule()
    assert lookup2.run


# test class instantiation

# Generated at 2022-06-13 13:42:28.212869
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:42:36.973125
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [{'files': '*.txt,foo.c',
              'paths': 'ansible/test/,ansible/test/test_lookup/'},
             {'files': 'bar.c,*.py',
              'paths': 'test'}]

    # Fake input variables
    variables = {
        u'lookup_file_test': [u'/etc/ansible/hosts'],
        u'lookup_file_one': [u'test'],
        u'lookup_file_two': [u'test_lookup'],
    }

    # Fake Ansible options
    options = {}

    # Create fake LookupBase instance
    lookup = LookupModule()

    lookup._loader = lambda x: None  # Dummy _loader

# Generated at 2022-06-13 13:42:48.614772
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Args:
        def __init__(self,
                     connection='smart', sudo=None, sudo_user=None, ask_sudo_pass=None,
                     verbosity=None, module_path=None, forks=None, become=None, become_method=None, become_user=None,
                     check=None, listhosts=None, listtasks=None, listtags=None, syntax=None):
            self.connection = connection
            self.sudo = sudo
            self.sudo_user = sudo_user

# Generated at 2022-06-13 13:42:49.182528
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:42:58.161617
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_obj = LookupModule()
    lookup_obj._templar = FakeTemplar()
    lookup_obj._loader = FakeLoader()
    lookup_obj._finder = FakeFinder()
    total_search, skip = lookup_obj._process_terms(
        ['dict.txt', 'dict2.txt'], {}, {'paths': 'path1:path2'})
    assert total_search == ['/path1/dict.txt', '/path2/dict.txt', 'default.txt', '/data1/dict2.txt', '/data2/dict2.txt'], \
        '_process_terms is broken'
    assert skip is False, \
        '_process_terms is broken'

# Generated at 2022-06-13 13:43:05.665093
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    lookup_plugin._subdir = 'test/path/'
    lookup_plugin._loader = MockLoader()
    lookup_plugin._loader._data['test/path/test1.yaml'] = 'test_data'
    assert lookup_plugin.run(["test1.yaml"],{},errors='ignore') == ['test_data']
    assert lookup_plugin.run(["test2.yaml"],{},errors='ignore') == []


# Generated at 2022-06-13 13:43:15.060677
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Stub for dummy class
    class MockAnsibleUndefinedVariable(AnsibleUndefinedVariable):
        pass

    class MockAnsibleLookupError(AnsibleLookupError):
        pass

    class MockLookupBase(LookupBase):
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=True):
            return None

    class MockTemplar(object):
        def template(self, fn):
            return fn

    class MockVariables(object):
        pass

    # Case lookup_file is not found
    lookup_module = LookupModule()
    lookup_module._templar = MockTemplar()
    lookup_module._templar.template = MockTemplar().template
    lookup_module._variables = MockVariables()
    lookup_module._

# Generated at 2022-06-13 13:43:28.161715
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # set the lookup parameters
    lookup_params = {}

    # set options
    options = {'files': 'firstfile','paths': ['firstpath','secondpath']}
    lookup_params.update(options)

    # set terms
    terms = ['firstfile','secondfile']
    lookup_params.update(dict(terms=terms))

    # set variables
    variables = {}

    # set the Ansible term_record
    term_record = dict(vars=variables,task_vars=variables,params=lookup_params)

    # initialise the lookup module
    ll = LookupModule()
    ll.set_loader(object)

    # set the term record
    ll.set_options(term_record)

    # call method run of class LookupModule

# Generated at 2022-06-13 13:43:39.381455
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        {'files': ['foo', 'bar'], 'paths': ['/tmp/production', '/tmp/staging']},
        {'files': ['foo', 'bar'], 'paths': '/tmp'},
        {'files': 'foo,bar', 'paths': '/tmp'},
        {'files': 'foo bar', 'paths': '/tmp'},
        {'files': 'foo,bar', 'paths': '/tmp'},
        'foo',
        ['foo', 'bar', {'files': 'biz, baz', 'paths': '/tmp'}],
    ]
    variables = {}
    subdir = 'files'
    lookup._subdir = subdir


# Generated at 2022-06-13 13:43:51.119201
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm._templar = DummyTemplar()
    lm._find_file_in_search_path = lambda variables, subdir, fn, ignore_missing: fn
    lm.set_options()
    terms = [{'files': 'foo.txt', 'paths': '/path'}]
    result = lm.run(terms, variables={}, skip=False)
    assert result == ['/path/foo.txt']

    terms = [{'files': 'foo.txt', 'paths': '/path'}, 'bar.txt', {'files': 'baz.txt', 'paths': '/other'}]
    result = lm.run(terms, variables={}, skip=False)
    assert result == ['/path/foo.txt']


# Generated at 2022-06-13 13:43:52.926331
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement unit test for LookupModule._process_terms
    assert True


# Generated at 2022-06-13 13:43:56.078144
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.run([[{'files': "/usr/share/foo.txt", 'paths': "/etc", 'skip': True}]], {}, skip=True)

# Generated at 2022-06-13 13:44:07.441789
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    _lookup_module = LookupModule()
    _lookup_module._subdir = 'files'
    _lookup_module.set_options({'paths': '.'})
    _templar = DummyTemplar()

    # Test 'single' value
    result = _lookup_module.run('test', None, _templar=_templar)
    assert result == ['test']

    # Test list of values
    result = _lookup_module.run(['test'], None, _templar=_templar)
    assert result == ['test']

    # Test dict
    result = _lookup_module.run([{'files': 'test'}], None, _templar=_templar)
    assert result == ['test']


# Generated at 2022-06-13 13:44:17.756283
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:44:26.409830
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_term = ["a.txt", "b.txt", {"files": "c.txt,d.txt"}, "e.txt", {"files": "f.txt,g.txt"}, {"files": "h.txt", "paths": "i.txt,j.txt"}, "k.txt"]
    expected_total_search = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt', 'g.txt', 'h.txt', 'i.txt', 'j.txt', 'k.txt']
    expected_skip = False
    lm = LookupModule()
    total_search, skip = lm._process_terms(test_term, {}, {})
    assert (total_search == expected_total_search)
    assert (skip == expected_skip)

    test

# Generated at 2022-06-13 13:44:36.935823
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    # test first two cases without defined paths and without files in default paths
    def create_file(path, name):
        with open(os.path.join(path, name), 'w+') as fd:
            fd.write("{}")

    # paths we search by default
    DEFAULT_PATHS = [
        os.path.join(os.getcwd(), 'files'),
        os.path.join(os.path.expanduser("~"), ".ansible", "tmp", "ansible-tmp-*", "files"),
    ]

    with tempfile.TemporaryDirectory() as tmpdir:
        # we need to create files in tmpdir and in the directories of DEFAULT_PATHS
        # create files we need
        create_file(tmpdir, 'file1')


# Generated at 2022-06-13 13:44:48.251343
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # SETUP
    # create a list of terms (files to look for)
    terms = ['test.txt', 'test2.txt', 'other.txt']

    # create a mock object for the Ansible templating engine
    class MockTemplar:
        @staticmethod
        def template(fn):
            # called for each term, for example:
            #   fn = 'test.txt'
            #   return 'test.txt'
            #   fn = 'test2.txt'
            #   return 'test2.txt'
            return fn

    # create a mock object for the Ansible class containing the variables for the task

# Generated at 2022-06-13 13:45:01.943097
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    from ansible import context
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    templar = Templar(None, [], [], None, None)
    terms = [
        'foo.j2',
        {'files': 'bar.j2', 'paths': './template', 'skip': True},
        {'files': ['foo2.j2', 'bar2.j2'], 'paths': ['', './template'], 'skip': True}
    ]
   
    variables = {}
   
    with context.push(VariableManager()):
        lm = LookupModule()
        lm._templar = templar

    # Act and Assert
    assert lm.run(terms, variables) == ["foo.j2"]

# Generated at 2022-06-13 13:45:14.910109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    # Create a fixture consisting of a LookupModule instance and its arguments
    @pytest.fixture()
    def lookup(monkeypatch, mocker):
        # Create a LookupModule instance
        l = LookupModule()

        # Define the method find_file_in_search_path
        def find_file_in_search_path(variables, subdir, filename, ignore_missing):
            return '%s:%s:%s' % (variables, subdir, filename)
        l.find_file_in_search_path = find_file_in_search_path

        # Define the subdir attribute of the LookupModule instance
        l._subdir = 'files'

        # Define the method _templar.template
        def template(filename):
            return filename

        # Patch the class

# Generated at 2022-06-13 13:45:27.868155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._subdir = 'files'
    # Test find file in paths
    assert l.run(['a.txt'], {}, paths=['a', 'b'], skip=True) == []
    # Test find first file in files
    assert l.run(['a.txt', 'b.txt'], {}, paths=['a', 'b'], skip=True) == []
    # Test find file in files/subdir
    assert l.run(['subdir/file.txt'], {}, paths=['a', 'b'], skip=True) == []
    # Test find file in files/subdir/subsubdir
    assert l.run(['subdir/subsubdir/file.txt'], {}, paths=['a', 'b'], skip=True) == []
    # Test

# Generated at 2022-06-13 13:45:38.165075
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    my_run = LookupModule()
    # the following is the list of files that exist in the filesystem.
    # If a file is added to /etc/ansible/facts.d, it should be added here as well.
    # This list is used in the test case called test_paths_defined_and_none_exist.

# Generated at 2022-06-13 13:45:50.296815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    fd, args_path = tempfile.mkstemp()
    with open(args_path, 'w') as f:
        yaml.dump({'ansible_env': {'HOME': '/home/jdoe'}}, f)
    os.close(fd)
    test_lookup = LookupModule()

    lookup_context = { '_terms': [{'files': 'group_vars/*', 'paths': '{{ playbook_dir }}'}] }
    test_lookup.set_options(var_options=lookup_context, direct=None)
    result = test_lookup._run(None, '/home/jdoe/ansible', False)
    test_lookup.set_options(var_options=lookup_context, direct=None)

# Generated at 2022-06-13 13:45:52.765738
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(terms=['/etc/passwd']).run() == ['/etc/passwd']
    assert LookupModule(terms=['doesnotexist']).run() == []

# Generated at 2022-06-13 13:46:03.731923
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with dict as term
    t = LookupModule()
    t.set_options(var_options=[], direct={'files': 'foo', 'paths': 'bar'})
    expected = ['bar/foo']
    assert t.run([]) == expected

    # test with path/file as term
    t.set_options(var_options=[], direct={'files': 'bar', 'paths': 'foo'})
    expected = ['foo/bar']
    assert t.run([]) == expected

    # test with multiple file/path as term
    t.set_options(var_options=[], direct={'files': 'foo,bar', 'paths': 'bar,foo'})
    expected = ['bar/foo', 'bar/bar', 'foo/foo', 'foo/bar']
    assert t.run([]) == expected

# Generated at 2022-06-13 13:46:16.480316
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from collections import namedtuple
    from ansible.plugins.loader import lookup_loader

    Mock_module_utils_common_collections_compat = namedtuple('Mapping', 'Mapping')
    Mock_module_utils_six = namedtuple('string_types', 'string_types')
    Mock_ansible_plugins_lookup_LookupBase = namedtuple('LookupBase', 'LookupBase')
    Mock_ansible_errors_AnsibleLookupError = namedtuple('AnsibleLookupError', 'AnsibleLookupError')
    Mock_ansible_errors_AnsibleUndefinedVariable = namedtuple('AnsibleUndefinedVariable', 'AnsibleUndefinedVariable')
    Mock_ansible_module_utils_common_collections_compat = namedtuple('Mapping', 'Mapping')

# Generated at 2022-06-13 13:46:26.777364
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
      Test cases for run method of lookup plugin
    """

    # Test case with file exist
    module = LookupModule()
    data = module.run(['/etc/hosts'], dict(ansible_hostname='host1', ansible_user='root'))
    assert data == ['/etc/hosts']

    # Test case with file not exist
    module = LookupModule()
    data = module.run(['/not/exist/file'], dict(ansible_hostname='host1', ansible_user='root'))
    assert data == []

    # Test case with file not exist but skip config is passed as false
    module = LookupModule()

# Generated at 2022-06-13 13:46:34.629109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for "run()" method of class LookupModule."""

    # Setup the situation to be tested

    # Imports
    import shutil
    import tempfile

    # TODO: refactor as it is wrong
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # Auxiliary function for creating a file for testing
    def _mkfile(content, directory, name):
        """Creates a file at "directory/" + name, with content
        "content". The result is the path of the file.
        """
        file_path = os.path.join(directory, name)
        with open(file_path, "w") as file_object:
            file_object.write(content)
        return file_path

    # Auxiliary function for creating a directory for testing

# Generated at 2022-06-13 13:46:49.037932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:46:59.609880
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup test objects
    l = LookupModule()
    l._subdir = 'files'
    # Create fake variables
    variables = {"hostvars":  {
                        'foo': {'ansible_distribution': 'redhat'},
                        'bar': {'ansible_os_family': 'redhat'}
                    },
                    "inventory_hostname": "foo"}
    # Create fake file
    # NOTE: this should always be 'files' and not '../files'
    # TODO: move this somewhere else
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    files_dir = os.path.join(basedir, 'files')

# Generated at 2022-06-13 13:47:04.434246
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()

    # test for #45862: should not raise exception on 'default' in list
    assert module.run([{'files': 'default'}], {}) == []

    # test for #50787: should be able to take a list as well
    assert module.run([['default']], {}) == []

# Generated at 2022-06-13 13:47:14.895518
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a LookupModule with a key value data structure to simulate results from reading a config
    params = {'files': ['test_file.txt', 'test_file2.txt'], 'paths': '/test/path1,/test/path2', 'skip': True}
    terms = ['foo', {'files': ['test_file1.txt', 'test_file2.txt'], 'paths': '/test/path3,/test/path4', 'skip': False},
             'bar', params]

    # Call run method of class LookupModule
    lookup_module_object = LookupModule()
    try:
        result = lookup_module_object.run(terms, None, **params)
    except AnsibleLookupError:
        result = []
    assert result == []

# Generated at 2022-06-13 13:47:25.672097
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    templar = Templar(loader=DataLoader())

    play_context = PlayContext()
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 22

    # test 1
    lookup_module_instance = LookupModule()
    lookup_module_instance.set_loader(DataLoader())
    lookup_module_instance._templar = templar

    # case 1: normal usage

# Generated at 2022-06-13 13:47:28.143584
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Unit test for method run of class LookupModule not implemented"


# Generated at 2022-06-13 13:47:29.088751
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: rewrite unit tests

    assert True

# Generated at 2022-06-13 13:47:36.481867
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test_1
    args = {'lookup_plugin_version': '', 'terms': ['file1.yml'], '_terms': ['file1.yml'], '_id': 'inventory', '_attributes': {}, 'vars': {}}
    args['_variable_manager'] = VariableManager()
    args['_loader'] = DataLoader()
    args['_templar'] = Templar()
    terms = args['terms']
    variables = args['vars']
    obj = LookupModule(**args)
    total_search, skip = obj._process_terms(terms, variables, {})
    path = obj.run(terms, variables, {})
    assert len(total_search) == 1 and type(total_search[0]) == str and total_search[0] == 'file1.yml'


# Generated at 2022-06-13 13:47:43.411727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an object
    LookupModule_Test = LookupModule()
    # Define args
    terms = ['/tmp/foo/bar.txt']
    variables = {}
    kwargs = {}
    # Return value
    return_value = LookupModule_Test.run(terms, variables, **kwargs)
    expected_value = ['/tmp/foo/bar.txt']
    assert return_value == expected_value

# Generated at 2022-06-13 13:47:53.272010
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.first_found as ff
    from ansible.utils.path import unfrackpath
    import os.path

    # Setup the LookupModule
    ff_module = ff.LookupModule()
    ff_module._templar = DummyTemplar()
    lookupfile = unfrackpath("/foo/bar/baz.txt")
    lookupdir = os.path.dirname(lookupfile)

    #####################################################################
    # Case 1: A file is found
    #####################################################################
    # Setup the LookupModule
    ff_module._loader.path_searched = set()
    ff_module.find_file_in_search_path = ff_module.find_file_in_search_path_original
    ff_module.find_file_in_search_path.ex

# Generated at 2022-06-13 13:48:18.896224
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    from ansible.plugins.lookup.first_found import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import os

    current_path = os.path.dirname(os.path.realpath(__file__))
    file_name_1 = 'tests/test_lookup_plugins/first_found/'
    file_name_2 = 'tests/test_lookup_plugins/first_found/test_files/'
    file_name_3 = 'test_files/'
    file_name_4 = 'test_files/test_files/'
    file_name_5 = 'test_files/test_files/'

    # create new lookup

# Generated at 2022-06-13 13:48:30.559675
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.basedir = os.path.dirname(os.path.dirname(__file__))
    l.get_basedir = lambda x: l.basedir

# Generated at 2022-06-13 13:48:41.355302
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Necessary module imports
    import ansible.utils.unsafe_proxy
    module = ansible.utils.unsafe_proxy.UnsafeProxy(
        {'subdir': 'files',
         't': 'templar',
         'vars': {'role_path': 'foo/bar/roles/something'},
         'variables': {'role_path': 'something/roles',
                       'inventory_dir': 'something/inventories',
                       'playbook_dir': 'something/'},
         '_basedir': '.',
         'task_path': '/something/tasks/main.yaml'})
    lookup_module = LookupModule(loader=module)

    # set up the inventory
    hostvars = {}
    inventory = ansible.utils.unsafe_proxy.UnsafeProxy

# Generated at 2022-06-13 13:48:53.089660
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:49:06.039553
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import os

    current_dir = os.path.dirname(os.path.realpath(__file__))

    dummy_loader = DataLoader()
    dummy_inventory = VariableManager()

    # Simple test
    test_path = os.path.join(current_dir, '../_data/lookup_plugins/findme1.txt')
    test_terms = [test_path]
    test_var_manager = VariableManager()
    test_loader = os.path.join(current_dir, '../_data/test_templates/')
    test_loader = DataLoader()
    test_lookup = LookupModule()
    test_lookup._loader = test_loader
    test_lookup

# Generated at 2022-06-13 13:49:15.124332
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __main__

    setattr(__main__, '__file__', '/some/path/some_file.py')

    lookup = LookupModule()
    lookup.set_loader()

    fake_variables={'var': 'foo', 'var1': 'bar'}


    # a list of strings (files)
    test_terms = ['/mnt/foo', '/mnt/bar']
    assert lookup.run(terms=test_terms, variables=fake_variables) == ['/mnt/foo']

    # a list of strings (files) and a dict (options)
    test_terms = ['/mnt/bar', {'files': '/mnt/foo'}]
    assert lookup.run(terms=test_terms, variables=fake_variables) == ['/mnt/bar']

    # a list

# Generated at 2022-06-13 13:49:16.868562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    return None


# Unit tests for method _split_on of module ansible.plugins.lookup.first_found

# Generated at 2022-06-13 13:49:22.481309
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # test when file not found
    with pytest.raises(AnsibleLookupError):
        lookup.run('wrong_file_name', {})
    # test when file found
    file_name = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'README.md')
    assert lookup.run(file_name, {})[0] == file_name

# Generated at 2022-06-13 13:49:23.808168
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:49:33.794984
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_dict=dict(
        _terms=[
            {'files': ['/etc/file1.txt', '/etc/file2.txt'], 'paths': ['/path1', '/path2'], 'skip': False},
            {'files': ['/etc/file3.txt', '/etc/file4.txt'], 'paths': ['/path1', '/path2'], 'skip': True}
        ],
        variables=dict()
    )

    test_class = LookupModule()
    test_class._templar = dict()
    test_class._templar.template = lambda x: x

    test_class.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=False: fn


# Generated at 2022-06-13 13:50:10.679058
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term = [{'files': 'myfile', 'skip': True},{'paths': 'mypath'},{'files': 'myfile2'}]
    lu = LookupModule()
    # method run is expected to return a list of 1 element
    assert(list == type(lu.run(terms=term, variables={})))
    assert(1 == len(lu.run(terms=term, variables={})))

# Generated at 2022-06-13 13:50:21.079092
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # test with a list of file names
    terms = ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt', '/path/to/baz.txt']
    variables = {}
    kwargs = {}
    with patch.object(LookupModule, "find_file_in_search_path") as mock_LookupModule_find_file_in_search_path:
        mock_LookupModule_find_file_in_search_path.return_value = '/path/to/biz.txt'
        assert lookup_module.run(terms, variables, **kwargs) == ['/path/to/biz.txt']

    # test with a dictionary containing keys files and paths

# Generated at 2022-06-13 13:50:32.465620
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with a YAML file as input
    lookup_module = LookupModule()
    result = lookup_module.run(terms=['bar.txt'], variables={"play_dir": "/play/dir", "relative_dir": "/play/dir/other/vars"})
    assert result == ['/play/dir/other/vars/bar.txt'], 'Expected result: /play/dir/other/vars/bar.txt, Actual Result: {0}'.format(result)

    # Test with a list of files as input
    lookup_module = LookupModule()
    result = lookup_module.run(terms=[['/path1/foo.txt', '/path2/bar.txt']], variables={})

# Generated at 2022-06-13 13:50:43.218626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Basic setup for this test, mock needed objects
    def _mock_get_basedir():
        return os.path.abspath("../../")

    lookup_base_mock = LookupBase()
    lookup_base_mock._templar = None
    lookup_base_mock._get_basedir = _mock_get_basedir
    lookup_base_mock._loader = None

    lookup_module = LookupModule()
    lookup_module._templar = lookup_base_mock._templar
    lookup_module._get_basedir = lookup_base_mock._get_basedir
    lookup_module._loader = lookup_base_mock._loader

    #Test that function runs without errors:
    #Create a temporary files to use for test

# Generated at 2022-06-13 13:50:54.104931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    variables = {'ansible_virtualization_type': 'docker',
                 'ansible_os_family': 'unix',
                 'ansible_distribution': 'alpine'}

    # Test 1: test basic usage with string format
    terms = ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt']
    paths, skip = lookup._process_terms(terms, variables, {})
    assert len(paths) == 3
    assert skip == False

    # Test 2: test usage of dict
    terms = [{"files": ["foo.txt", "bar.txt"]},
             {"paths": ["/path/to/file"]},
             {"files": ["biz.txt"], "paths": ["/path/to"]}]

    paths, skip = lookup

# Generated at 2022-06-13 13:51:08.267048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_loader(None)
    assert l.run([]) == [], "run with no param should return empty list"
    assert l.run([], [], files=[], paths=[]) == [], "run with empty params should return empty list"
    terms = [{'files': ['foo'], 'paths': ['@mock']}, {'files': ['bar'], 'paths': ['@mock']}]
    l.run(terms, [], files=[], paths=[]) == ['/mock/path/file/foo']
    terms = [{'files': ['zoo'], 'paths': ['@mock']}, {'files': ['zar'], 'paths': ['@mock']}]

# Generated at 2022-06-13 13:51:19.662896
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:51:20.617416
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:51:32.118774
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # simple test
    terms = [
        "/path/to/foo.txt",
        "bar.txt",
        "/path/to/biz.txt",
    ]
    test_object = LookupModule()
    (total_search, skip) = test_object._process_terms(terms, None, None)
    assert skip is False
    assert total_search == [
        "/path/to/foo.txt",
        "bar.txt",
        "biz.txt",
    ]

    # skip, using a list of strings
    terms = [
        "/path/to/foo.txt",
        "bar.txt",
        "/path/to/biz.txt",
    ]
    kwargs = {
        "skip": True,
    }
    test_object = LookupModule()

# Generated at 2022-06-13 13:51:43.281557
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # in case this is called from a different place than its tests
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import test_utils
    import ansible.plugins.loader

    # load the lookup modules to get its LookupBase class definition
    # so we can override the find_file_in_search_path method for testing
    module_loader = ansible.plugins.loader.LookupModule()

    # mock vars
    class MockVars(dict):
        def get(self, name, default=None):
            return self[name] if name in self else default
    variables = MockVars({'foo': 'fooval'})

    # mock find file