

# Generated at 2022-06-13 13:42:11.998552
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create instance of class LookupModule to test
    lm = LookupModule()

    # There is no run method in LookupBase, so redefine it
    def run(self, terms, variables, **kwargs):
        return self._process_terms(terms, variables, kwargs)

    lm.run = run

    # Set default values for instance attributes
    lm._loader = None
    lm._templar = None
    lm._basedir = None

    # Get result of method run
    result = lm.run(['/path/to/file'], None, skip=False)
    # Check result
    assert result == (['/path/to/file'], False)


# Generated at 2022-06-13 13:42:26.259435
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule

    It is not possible to make a complete test.
    To run this test you must create an empty directory
    and place a shell script inside named test.sh
    """
    # Create an instance of LookupModule and set _subdir
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._loader = None
    lookup._templar = None

    # Create the first param - variables
    variables = dict()
    # the following will raise an exception if the file doesn't exists
    variables['ansible_managed'] = 'Ansible managed'
    functions = None

    # Create the second param - terms
    terms = None

    # Call the method run and it returns a list with a path
    result = lookup.run(terms, variables, functions)
    assert isinstance

# Generated at 2022-06-13 13:42:36.024502
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test run method of LookupModule class"""
    results = LookupModule().run("/bar/foo.txt", dict())
    assert results == ['/bar/foo.txt']

    results = LookupModule().run("/ba/foo.txt", dict())
    assert results == ['/ba/foo.txt']

    results = LookupModule().run("/bar/foo.txt", dict(ansible_env=dict(HOME='/home')))
    assert results == ['/bar/foo.txt']

    results = LookupModule().run("~/foo.txt", dict(ansible_env=dict(HOME='/home')))
    assert results == ['/home/foo.txt']

    results = LookupModule().run("$HOME/foo.txt", dict(ansible_env=dict(HOME='/home')))

# Generated at 2022-06-13 13:42:41.631947
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import sys
    import pytest
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.common._collections_compat import Sequence

    files = ['foo', 'bar']
    paths = ['/tmp/production', '/tmp/staging']
    searchlist = ['/tmp/production/foo', '/tmp/production/bar', '/tmp/staging/foo', '/tmp/staging/bar']

    # ensure LookupModule is called with args and kwargs
    if sys.version_info < (3, ):
        def f(args, kwargs):
            if 'LookupModule' in args[0]:
                return True
            return False
    else:
        def f():
            return True


# Generated at 2022-06-13 13:42:53.801243
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    params = {"files": ['foo', 'bar', 'baz'], 'paths': ['path1', 'path2', 'path3']}
    terms = [params]
    variables = {}

    # Act
    lookup_module = LookupModule()
    lookup_module._find_file_in_search_path = MagicMock(return_value=None)
    lookup_module.run(terms=terms, variables=variables)

    # Assert
    assert lookup_module._find_file_in_search_path.call_count == 9

# Generated at 2022-06-13 13:43:01.342900
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = (
        'default_foo.conf',
        {"files": '{{ ansible_virtualization_type }}_foo.conf', "paths": '.', "skip": True})
    variables = {'ansible_virtualization_type': 'kvm'}
    expected = '/home/alice/ansible/roles/role_under_test/default_foo.conf'
    subdir = 'templates'
    lookup_module._subdir = subdir
    lookup_module.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=False: expected if (subdir == 'templates' and fn == 'kvm_foo.conf') else None
    result = lookup_module.run(terms, variables)
    assert result == [expected]

# Generated at 2022-06-13 13:43:12.139718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mock_loader = unittest.mock.Mock()
    mock_loader.get_basedir.return_value = os.getcwd()
    mock_loader.path_dwim.side_effect = lambda x: x

    mock_templar = unittest.mock.Mock()
    mock_templar.template.side_effect = lambda x: x

    # Test regular run
    lookup_plugin = LookupModule(loader=mock_loader, templar=mock_templar)
    assert lookup_plugin.run([__file__, 'foo'], variables={}) == [__file__]

    # Test error handling
    with pytest.raises(AnsibleLookupError):
        lookup_plugin.run(['bar'], variables={})


# Generated at 2022-06-13 13:43:23.591191
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_loader(None)
    l.set_environment(None)

    class MockTemplar():
        def template(self, s):
            return s

    l._templar = MockTemplar()

    class MockVarManager():
        def __init__(self):
            self.vars = dict(
                ansible_virtualization_type='kvm',
                ansible_os_family='RedHat',
                ansible_distribution='Fedora',
                inventory_hostname='localhost'
            )

        def get_vars(self, loader, path=None, play=None, task=None, include_params=True):
            return self.vars

    l._var_manager = MockVarManager()

    l.set_basedir('.')

    # no terms

# Generated at 2022-06-13 13:43:34.137594
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a lookupModule object
    lookup_module = LookupModule()

    # Setup a term list that has a filter and a path
    term_list = list()
    term_list.append('logs')
    term_list.append('logs/')
    term_list.append('logs/audit.log')

    # Setup a var list that has a filter and a path
    var_list = list()
    var_list.append('logs/')
    var_list.append('logs')

    # Call the run method and check the results match
    assert lookup_module.run(term_list, var_list) == ['logs/']

# Generated at 2022-06-13 13:43:35.207351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: test for run, but for now it is easier to rely on functional tests
    pass

# Generated at 2022-06-13 13:43:42.617055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Temporary variables
    terms = ['file.txt', 'path']
    variables = {}
    kwargs = {}

    #Class instantiation
    test = LookupModule()

    # Method run results in a list
    result = test.run(terms, variables, **kwargs)
    assert isinstance(result, list)

# Generated at 2022-06-13 13:43:49.870464
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.path import unfrackpath
    import os

    lookup = LookupModule()
    lookup._connection = None
    lookup._loader = None
    lookup._templar = None

    # try undefined variable error in template
    total_search, skip = lookup._process_terms([{'files': "{{ var_in_template }}", 'paths': './tests/lookup/first_found/'}], {}, {'skip': False})
    assert total_search == [], "Variable template error not handled"

    # try valid template
    total_search, skip = lookup._process_terms([{'files': "{{ 'file1' }}", 'paths': './tests/lookup/first_found/'}], {}, {'skip': False})

# Generated at 2022-06-13 13:43:59.692535
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_cases = {
        'test_1': {
            'terms': [
                [
                    'foo',
                    'bar',
                    'biz'
                ],
                'world',
                {'files': 'hello'}
            ],
            'variables': dict(),
            'kwargs': dict(),
            'returns': {}  # TODO
        },
        'test_2': {
            'terms': [
                'foo',
                'bar',
                'biz'
            ],
            'variables': dict(),
            'kwargs': dict(files='hello'),
            'returns': {}  # TODO
        },
    }
    test_ansible_module = LookupModule()

    for case, test in test_cases.items():
        print(case)

# Generated at 2022-06-13 13:44:00.777793
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: add unit testing
    assert True

# Generated at 2022-06-13 13:44:10.342312
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Check normal operation
    terms = [
        {'files': 'foo', 'paths': 'path/to'},
        {'files': 'bar', 'paths': 'path/to'},
        'baz',
        {'files': 'foo,bar', 'paths': 'path/to'},
    ]
    lookup.set_options({
        'files': [],
        'paths': ['path/to']
    })
    assert lookup._process_terms(terms, None, None) == \
        ([
            'path/to/foo',
            'path/to/bar',
            'path/to/foo',
            'path/to/bar',
        ], False)

    # Check with skip

# Generated at 2022-06-13 13:44:18.637403
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a templar
    config = dict(DEFAULT_HASH_BEHAVIOUR='replace')
    templar = Templar(loader=DataLoader(), variables={},
                      shared_loader_obj=None, collection_list=[], **config)

    # create a LookupModule
    lu = LookupModule(loader=DataLoader(), templar=templar, **config)

    # create a ansible var
    ansible_var = dict(ansible_distribution='debian', ansible_os_family='Debian')

    # test first case
    terms = ['{{ ansible_distribution }}_foo.conf', 'default_foo.conf']
    search_results = lu.run(terms, ansible_var)
    assert search_results == ['debian_foo.conf']

    # test second case
    terms

# Generated at 2022-06-13 13:44:26.679135
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    lookup.set_options(var_options=dict(files=['/path/to/foo.txt', 'bar.txt'],
                                        paths=['/path/to', '/tmp/production'],
                                        skip=True))
    assert lookup.get_option('files') == ['foo.txt', 'bar.txt']
    assert lookup.get_option('paths') == ['/path/to', '/tmp/production']
    assert lookup.get_option('skip')

    lookup.set_options(var_options=dict(files=['/path/to/foo.txt', 'bar.txt'],
                                        paths=['/path/to', '/tmp/production'],
                                        skip=False))
    assert lookup.get_option('files') == ['foo.txt', 'bar.txt']


# Generated at 2022-06-13 13:44:28.253013
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "No tests for LookupModule"


# Generated at 2022-06-13 13:44:37.911077
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_module_name = sys.modules[__name__]
    my_module = importlib.import_module(
        my_module_name.__name__,
        package=my_module_name.__package__)
    my_class = LookupModule()
    my_class._templar = MyTemplar()
    result = my_class.run([['foo/bar']], 'var')
    assert result == []
    result = my_class.run([{'files': 'foo/bar'}], 'var')
    assert result == []
    result = my_class.run([{'files': 'baz.txt'}], 'var')
    assert result == ['/tmp/baz.txt']

# Generated at 2022-06-13 13:44:48.592752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    templar = Templar(loader=DictDataLoader())
    templar._available_variables = dict()
    lookup_module._templar = templar

    lookup_module.find_file_in_search_path = lambda *args: 'var.tmp'
    lookup_module.set_options = lambda *args: None

    lookup_module._subdir = 'files'

    try:
        total_search, skip = lookup_module._process_terms(['some.txt'], {}, {})
    except Exception as e:
        assert False, "Failed to process terms with exception {}".format(e)

    # no files exist in search path
    lookup_module.find_file_in_search_path = lambda *args: None


# Generated at 2022-06-13 13:45:02.153698
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    fqpn = os.path.dirname(os.path.abspath(__file__))
    assert lookup_plugin.run(terms=['{{ ansible_distribution }}_foo.conf', 'default_foo.conf'], variables={'ansible_distribution': 'Foo'}, inject={'lookup_file': os.path.join(fqpn, 'foo.conf')})[0] == '%s/foo.conf' % fqpn

# Generated at 2022-06-13 13:45:15.217113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MyLookupModule(LookupModule):
        def __init__(self):
            self._templar = None
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing):
            return fn
        def _process_terms(self):
            raise Exception('not implemented')
    lookup = MyLookupModule()
    assert lookup.run(
        [ 'term' ],
        {},
        files = 'file1,file2',
        paths = 'path1,path2',
    ) == ['path1/file1', 'path1/file2', 'path2/file1', 'path2/file2']

# Generated at 2022-06-13 13:45:28.089754
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    dataloader = DataLoader()

    lookup_module = LookupModule()
    test_value = [
        {
            'files': ['"{{ test_file }}"'],
            'paths': [
                '/home/user/path',
                '/etc/path',
            ],
        },
        {
            'paths': [
                '/home/user/path',
                '/etc/path',
            ],
        },
        {
            'files': ['"{{ test_file }}"'],
        },
        {
            'paths': [
                'etc',
                '/etc/path',
            ],
        },
    ]

    class ExecutionContext:
        pass

    execution_context = ExecutionContext()
    execution_context._templar

# Generated at 2022-06-13 13:45:38.318618
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._loader = DummyVarsModule()
    lookup_module._templar = DummyVarsModule()
    lookup_module._find_needle = DummyVarsModule()
    lookup_module._find_needle['found'] = True
    lookup_module._find_needle['path'] = './some_file'
    lookup_module.set_options(var_options={})
    terms = [
        './some_file',
    ]
    for term in terms:
        lookup_module.set_options(var_options={}, direct={})
        result = lookup_module.run(terms=[term], variables={})
        assert result == ['./some_file']

    lookup_module = LookupModule()
    lookup_module._loader = DummyVarsModule

# Generated at 2022-06-13 13:45:50.425431
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def get_templar(vars=None):
        return DummyTemplar
    def set_loader(loader):
        return True
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 13:45:55.461397
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with no files, no skip
    lookup_module = LookupModule()
    lookup_module._subdir = 'files'
    lookup_module._templar = None
    lookup_module.set_options({'files': [], 'skip': False})
    terms = ['foo', {'files': ['bar', 'baz'], 'paths': ['apath'], 'skip': False}]
    lookup_module._process_terms = lambda t, v, k: ([], False)
    with pytest.raises(AnsibleLookupError, match='No file was found when using first_found.'):
        lookup_module.run(terms, {})
    # Test with no files, skip
    lookup_module = LookupModule()
    lookup_module._subdir = 'files'

# Generated at 2022-06-13 13:46:03.159754
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    import sys
    if PY3:
        from io import StringIO
    else:
        from StringIO import StringIO

    # capture output
    # create a "real" object here so pylint doesn't complain
    instance = LookupModule()
    real_stdout = sys.stdout
    fake_stdout = sys.stdout = StringIO()

    # set some arbitrary values
    kwargs = {'bar': 'foo'}

# Generated at 2022-06-13 13:46:16.062394
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import tempfile

    from ansible.module_utils.common._collections_compat import Mapping, Sequence

    # Arrange
    temp_dir = tempfile.mkdtemp()

    # Act
    lookup_module = LookupModule()
    lookup_module._subdir = 'test_templates'
    lookup_module._basedir = temp_dir
    lookup_module._templar = None
    lookup_module._loader = None
    lookup_module._options = dict(skip=False)

    # Create test_templates/test1.j2
    test_templates = os.path.join(temp_dir, lookup_module._subdir)
    os.makedirs(test_templates)
    test1_j2 = os.path.join(test_templates, 'test1.j2')

# Generated at 2022-06-13 13:46:25.851617
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class TestTemplar(object):

        @staticmethod
        def template(template):
            return template

    class TestSearchPath(object):

        @staticmethod
        def search(subdir, filename, ignore_missing=False):
            return [os.path.join(subdir, filename), os.path.join(subdir, 'first.yml')][filename != 'first.yml']

    # Test first found
    total_search = ['/etc/foo.conf', '/etc/bar.conf']
    subdir = 'files'
    templar = TestTemplar()
    searchpath = TestSearchPath()

# Generated at 2022-06-13 13:46:34.488722
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: want to test patterns?

    import pytest

    # no file found
    with pytest.raises(AnsibleLookupError) as err:
        LookupModule().run([None], {})
    assert "No file was found" in str(err)

    # only one file found
    assert LookupModule().run(["file"], {}) == ["file"]

    # several files found (no path)
    assert LookupModule().run(["file", "file2"], {}) == ["file"]

    # several files but with paths
    assert LookupModule().run([{"files": "file,file2", "paths": "/tmp/path,/path/to/files"}], {}) == ["/tmp/path/file"]

    # more complex path

# Generated at 2022-06-13 13:46:51.587778
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.first_found
    # test with no item
    lookup = ansible.plugins.lookup.first_found.LookupModule()
    assert lookup.run(terms=[], variables=None) == []
    # test when no file matches
    lookup = ansible.plugins.lookup.first_found.LookupModule()
    assert lookup.run(terms=[("file1","file2")], variables=None) == []
    assert lookup.run(terms=["file1","file2"], variables=None) == []
    assert lookup.run(terms=[{"files":["file1","file2"]}], variables=None) == []
    # test when one file matches
    lookup = ansible.plugins.lookup.first_found.LookupModule()

# Generated at 2022-06-13 13:46:55.201725
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check that the method runs without throwing any exception
    import ansible.plugins.lookup.first_found
    lookup = ansible.plugins.lookup.first_found.LookupModule()
    lookup.run([], dict())

# Generated at 2022-06-13 13:47:05.600039
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # prepare test data
    class DummyTemplar:
        def template(self, s):
            return s

    class DummyVars:
        ansible_distribution = 'RedHat'
        ansible_os_family = 'Linux'

    class DummyVars2:
        ansible_distribution = 'Ubuntu'
        ansible_os_family = 'Debian'

    class DummyAnsibleModule:
        def __init__(self):
            self.params = {
                "files": ["/etc/network/interfaces"],
                "paths": ["/etc/network/interfaces"],
            }
        def fail_json(self, msg, **kwargs):
            print("Ansible Module Fail: %s" % msg)
            assert False


# Generated at 2022-06-13 13:47:16.045016
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a mock templar for the test
    from ansible.template import Templar
    mock_variables = dict(
        foo='some value',
        bar='other value',
    )
    templar = Templar(loader=None, variables=mock_variables)

    # create a mock templar for test _process_terms
    class MockLookup(LookupBase):
        def __init__(self):
            self._templar = templar
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
            return None

    lookup = MockLookup()

    # verify default config
    assert lookup._get_local_vars() == dict(
        files=[],
        paths=[],
        skip=False,
    )

    # test term as lookup

# Generated at 2022-06-13 13:47:23.857379
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for method run of class 'LookupModule'
    lookup_module = LookupModule()
    total_search, skip = lookup_module._process_terms(terms=['t1', 't2'],
                                                      variables={'files': 'f1', 'paths': 'p1', 'skip': True},
                                                      kwargs={'files': 'f2', 'paths': 'p2', 'skip': True})
    assert total_search == ['f1', 'f2', 't2']
    assert skip == True

# Generated at 2022-06-13 13:47:28.239327
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ This unit test checks for method run of class LookupModule """

    lookup_instance = LookupModule()
    # TODO: test with files, paths and dicts as params
    assert lookup_instance.run([], {}) == []

# Generated at 2022-06-13 13:47:36.070862
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a fake Ansible task
    class FakeTask:
        def __init__(self):
            self.args = dict()
            self.args['_raw_params'] = "a"
            self.env = ["a"]
            self.basedir = '.'
    class FakeVars():
        def __init__(self):
            self._task = FakeTask()
            self._fact_cache = dict()
            self._vars = dict()
            self._role_params = dict()
    class FakeExecutor:
        def get_basedir(self):
            return "."
    class FakeLoader:
        def get_basedir(self):
            return "."
    class FakeTemplar:
        def template(self, fn):
            return fn

    # Actual test case
    lookup = LookupModule()
    lookup

# Generated at 2022-06-13 13:47:48.062056
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit tests for the method run ansible.plugins.lookup.first_found LookupModule.
    """
    import tempfile
    import os
    import shutil
    import pytest

    fh, abs_path = tempfile.mkstemp()
    with open(abs_path, 'w') as tmp_file:
        tmp_file.write('test_LookupModule_run')

    # Create a new temp folder, and creates a file foo in it.
    tmp_dir_path = tempfile.mkdtemp()
    tmp_file_path = os.path.join(tmp_dir_path, 'foo')
    with open(tmp_file_path, 'w') as tmp_file:
        tmp_file.write('test_LookupModule_run')

    # Setup the module and method to test.
   

# Generated at 2022-06-13 13:47:58.509835
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    test_dir = os.path.dirname(__file__)
    test_vars = VariableManager()
    test_vars.set_variable('inventory_dir', test_dir)
    test_vars.set_variable('inventory_file', 'lookup_plugins_empty.yaml')
    test_loader = DataLoader()

    test_context = PlayContext()
    test_context.variable_manager = test_vars
    test_context._loader = test_loader

    test_lookup_plugin_test1 = LookupModule()
    test_lookup_plugin_test1._connection = None
    test_lookup_plugin_

# Generated at 2022-06-13 13:48:11.592777
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test run() from LookupModule
    """
    # test files
    paths = [
        'path',
        'path/to',
        'path/to/foo',
        'path/to/foo.txt',
        'path/to/file',
        'path/to/file.txt',
        'path2',
        'path2/file.txt',
        'path2/file',
        'path2/file.txt',
        'path3/file.txt',
        'path3/file',
        'path3/file.txt',
    ]
    # test files

# Generated at 2022-06-13 13:48:30.621143
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        {'files': ['bar.txt'], 'paths': ['/tmp/production', '/tmp/staging']},
        {'files': ['foo.txt', 'bar.txt'], 'paths': ['/tmp/production', '/tmp/staging']},
    ]
    variables = {}
    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables)
    assert result == ['/tmp/production/foo.txt']

    terms = [
        {'files': 'foo.txt', 'paths': ['/tmp/production', '/tmp/staging']},
        {'files': ['foo.txt', 'bar.txt'], 'paths': ['/tmp/production', '/tmp/staging']},
    ]
    variables = {}
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:48:41.442100
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # will be renamed to 'TestLookupModule' in Ansible 2.10
    class TestLookupBase(LookupBase):

        def run(self, terms, variables, **kwargs):
            total_search, skip = self._process_terms(terms, variables, kwargs)
            return total_search, skip

        def find_file_in_search_path(self, variables, subdir, filename, ignore_missing=False):
            try:
                return self._loader.path_dwim(filename)
            except AnsibleFileNotFound as e:
                if not ignore_missing:
                    raise AnsibleLookupError(e)

    lookup_ins = TestLookupBase()

    # test invalid term causes error

# Generated at 2022-06-13 13:48:53.185306
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    import ansible.constants as C
    import os
    import pytest
    from ansible.plugins.lookup import LookupBase


    class TestLookupBase(LookupBase):

        def run(self, terms, variables=None, **kwargs):
            return terms


    class TestLookupModule(LookupModule):
        def run(self, terms, variables=None, **kwargs):
            return terms

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 13:49:06.110847
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  terms_params_files_paths = [{"files": ["file1", "file2"], "paths": ["path1", "path2"]}, "other_file"]

  from ansible.module_utils._text import to_bytes
  from ansible.parsing.dataloader import DataLoader

  loader = DataLoader()
  mock_templar = _MockTemplar(loader=loader)
  mock_variables  ={"var1": "value1", "var2": "value2"}

  mock_LookupBase = _MockLookupBase()

# Generated at 2022-06-13 13:49:15.218150
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    import unittest

    from ansible.errors import AnsibleError
    from ansible.module_utils.six import PY3

    class LookupModuleTest(unittest.TestCase):
        def setUp(self):
            self.temp_files = []
            self.temp_dirs = []

        def tearDown(self):
            for d in self.temp_dirs:
                if os.path.exists(d):
                    os.rmdir(d)
            for f in self.temp_files:
                if os.path.exists(f):
                    os.remove(f)

        def test_no_file_or_path(self):
            """
            Test if file not found when neither file nor path is passed
            """


# Generated at 2022-06-13 13:49:16.592516
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Tests for the method run of the LookupModule class.
    """
    mock_plugin = LookupModule()
    mock_plugin.run(['lookup'])

# Generated at 2022-06-13 13:49:25.216708
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: break this up into smaller tests
    import os
    import tempfile
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('first_found')

    class TestLookupModule(LookupModule):
        pass
    lookup._lookup_plugin_class = TestLookupModule

    dirname = tempfile.mkdtemp(prefix='ansible_first_found')
    dirname = os.path.realpath(dirname)
    dirname2 = tempfile.mkdtemp(prefix='ansible_first_found')
    dirname2 = os.path.realpath(dirname2)
    dirname3 = os.path.join(dirname, 'dir3', 'dir4')
    dirname3 = os.path.realpath(dirname3)

# Generated at 2022-06-13 13:49:34.386685
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()

    # TODO: test can fail if CWD is not test/files
    # TODO: is it a problem?!?
    # TODO: how to test different CWDs?
    # TODO: how to test different paths?!?
    fname = './test/files/subdir/test.txt'

    # simple file
    term = [fname]
    assert module.run(term, dict()) == [fname]

    # template expansion
    term = dict(files=["./test/files/subdir/{{ 'subdir/test.txt' }}"], paths=[])
    assert module.run([term], dict()) == [fname]

    # empy list
    term = []
    assert module.run(term, dict()) == []

    # empty dict
    term = dict()
   

# Generated at 2022-06-13 13:49:47.790502
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from __main__ import LookupModule as mod
    from __main__ import lookup_loader as loader
    from ansible.template import Templar
    from ansible.parsing.vault import VaultSecret
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.vars import combine_vars
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['localhost']))
    loader.set_inventory(InventoryManager(loader=loader, sources=['localhost']))
    vault_secrets = {}
    loader

# Generated at 2022-06-13 13:49:55.090390
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    file = LookupModule()
    assert file.run(terms={'files':'test.txt','paths':'test'}, variables={}) == ['test/test.txt']
    assert file.run(terms=[{'files':'test.txt','paths':'test'}], variables={}) == ['test/test.txt']
    assert file.run(terms=[{'files':'list.txt,list2.txt','paths':'test,test2'}], variables={}) == ['test/list.txt', 'test2/list2.txt']
    assert file.run(terms=[{'files':'list.txt,list2.txt','paths':'test,test2'}], variables={}) == ['test/list.txt', 'test2/list2.txt']

# Generated at 2022-06-13 13:50:13.709085
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init the lookup module
    result = LookupModule()
    # run find file
    path = result.run(terms=["/tmp/somefile.yml"], variables={}, **{})
    # check if it found the file
    assert path[0] == "/tmp/somefile.yml"
# end unit test

# Generated at 2022-06-13 13:50:23.211165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.utils.unsafe_proxy
    import ansible.vars.unsafe_proxy
    # create vars object
    vars_proxy = ansible.utils.unsafe_proxy.AnsibleUnsafeText('{"path1": "bar", "path2": "foo", "file1": "aaa", "file2": "bbb"}')
    # create an template object
    template_proxy = ansible.vars.unsafe_proxy.AnsibleVarsUnsafeProxy(vars_proxy)
    # create a empty module_vars object
    module_vars = {}

    # create first_found object
    lookup_module = LookupModule(loader=None, templar=template_proxy, **module_vars)
    # set a term value

# Generated at 2022-06-13 13:50:33.054070
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule({}, {})
    f = 'first_line'

    # All valid terms
    terms = ['first_line', {}, []]
    lu._loader = FakeLoader(f)
    assert lu.run(terms, {}) == [f]

    # Invalid term in list
    terms = ['first_line', 1, {}]
    with pytest.raises(AnsibleLookupError):
        lu.run(terms, {})

    # Invalid term in dictionary (defined, but not string)
    terms = [{'files': 1}]
    lu._loader = FakeLoader(f)
    with pytest.raises(AnsibleLookupError):
        lu.run(terms, {})

    # Invalid term (not string, list, or dictionary)

# Generated at 2022-06-13 13:50:42.709292
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ With a valid term, a valid path to file is returned """
    l = LookupModule()
    l.set_loader([])
    results = l.run(['foo'], dict(),
                    files=['foo'],
                    paths='/tmp')
    assert results == [u'/tmp/foo']

    """ With a valid term, a valid path to file is returned when path is list of paths """
    l = LookupModule()
    l.set_loader([])
    results = l.run(['foo'], dict(),
                    files=['foo'],
                    paths='/tmp:/usr/bin:/usr/share')
    assert results == [u'/tmp/foo']

    """ With a valid term, a valid path to file is returned if path has ':' """
    l = LookupModule()
    l.set_loader([])

# Generated at 2022-06-13 13:50:43.436321
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:50:54.282122
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    terms = ["file1.txt", "file2.txt", "file3.txt"]

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_from_source('[test_hosts]\nlocalhost'))
    templar = Templar(loader=loader, variables=variable_manager)

    lookup_plugin = LookupModule()
    lookup_plugin._templar = templar
    lookup_plugin._loader = loader
    lookup_plugin._find_file_in_search_path = lambda x, y, z: to_bytes(terms[0])

# Generated at 2022-06-13 13:51:08.325639
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        {'files': '{{ lookup("env", "HOME") }}/foo.txt', 'paths': '~, /tmp/, /etc/', 'skip': False},
        {'files': 'foo1.txt', 'paths': '~, /tmp/, /etc/', 'skip': True},
        {'files': 'foo2.txt', 'paths': '~, /tmp/, /etc/', 'skip': False},
        {'files': 'foo3.txt', 'paths': '~, /tmp/, /etc/', 'skip': True},
        {'files': 'foo4.txt', 'paths': '~, /tmp/, /etc/', 'skip': False},
    ]

# Generated at 2022-06-13 13:51:16.325372
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Parameters
    params = {
        'files': ['foo'],
        'paths': ['/tmp/production']
    }

    # Mocked return values
    find_file_in_search_path = ['/tmp/production/foo']

    # Mocked AnsibleModule
    mocked_module = MagicMock()
    mocked_templar = MagicMock()
    mocked_var_options = MagicMock()

    # Mocked object
    mocked_lookup_module = LookupModule(mocked_templar, mocked_var_options, mocked_module)
    mocked_lookup_module._templar.template = MagicMock(return_value='foo')
    mocked_lookup_module.find_file_in_search_path = MagicMock(return_value=find_file_in_search_path)

# Generated at 2022-06-13 13:51:27.747325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # test that first file found will be returned
    first_file = '/tmp/test_ansible_lookup_first_found/file1'
    assert module.run([first_file, 'file2'], {}) == [first_file]

    second_file = '/tmp/test_ansible_lookup_first_found/file2'
    assert module.run([first_file, second_file], {}) == [first_file]
    assert module.run([second_file, first_file], {}) == [second_file]

    # test that no file returned if no file found
    with pytest.raises(AnsibleLookupError):
        module.run(['file1', 'file2'], {})

    # test that no file returned if no file found using var options

# Generated at 2022-06-13 13:51:33.536163
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    try:
        lookup.run([
            'file1',
            'file2',
            {'files': 'file3', 'paths': '/path/to/file3'}
        ], {})
    except AnsibleLookupError as e:
        assert isinstance(e, AnsibleLookupError)
    except:
        assert False

