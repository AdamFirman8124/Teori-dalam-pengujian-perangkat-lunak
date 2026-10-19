

# Generated at 2022-06-13 13:42:10.928294
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    # Correct Values

# Generated at 2022-06-13 13:42:24.081326
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    exc = AnsibleLookupError('file not found exception')
    def run(self, terms, variables=None, **kwargs):
        return terms

    def find_file_in_search_path(self, variables, paths, file_name, ignore_missing=False):
        for p in paths:
            for f in file_name:
                if os.path.isabs(f):
                    return f

    def _templar_template(self, fn):
        return fn

    def _templar_template_result(self, fn):
        return fn

    def get_option(self, key):
        if key == 'skip':
            return True
        return None

    LookupModule._templar.template = _templar_template
    LookupModule._templar.template_result = _templar_template

# Generated at 2022-06-13 13:42:33.042334
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create test class and instance
    lm = LookupModule()
    lm._templar = LookupBase._create_template_class('LookupModule_run')

    # create sequence and mapping to test from
    seq = [
        'test.txt',
        {
            'files': 'test1.txt,test2.txt',
            'paths': 'path/to/'
        },
        ['test3.txt', 'test4.txt']
    ]

    mapping = {
        'mapping': {
            'files': 'test1.txt,test2.txt',
            'paths': 'path/to/'
        },
        'list': ['test3.txt', 'test4.txt']
    }

    # create base test
    test = lm.run(seq, None)

    #

# Generated at 2022-06-13 13:42:45.707795
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # prepare environment
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.common._collections_compat import Mapping
    import pytest

    # create inventory
    loader = DataLoader()
    inv_data = """
    [all]
    localhost ansible_connection=local
    """
    inv = InventoryManager(loader=loader, sources=inv_data)

    # create variable manager
    vars_manager = VariableManager(loader=loader, inventory=inv)
    vars_manager.set_inventory(inv)


# Generated at 2022-06-13 13:42:56.317199
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert LookupModule().run(['/file1', '/file2', {'files': '/file3'}], {}) == ['/file1']
    assert LookupModule().run(['/file1', '/file2', {'files': '/file3'}, '/file4'], {}) == ['/file1']
    assert LookupModule().run(['/file1', '/file2', {'files': '/file3'}, '/file4', {'files': '/file5'}], {}) == ['/file1']
    assert LookupModule().run(['/file1', '/file2', {'files': '/file3'}, {'files': '/file4'}, {'files': '/file5'}], {}) == ['/file1']

# Generated at 2022-06-13 13:43:03.915602
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    host = MagicMock()
    basedir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'hacking')
    lookup_mm = LookupModule(loader=MagicMock(), templar=MagicMock(), basedir=basedir)

    # Act
    result = lookup_mm.run([
        'x'
    ], dict())

    # Assert
    assert result == []

# Generated at 2022-06-13 13:43:10.157903
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    # Load base class
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from ansible.plugins.lookup import LookupBase

    # Mock class for run tests
    class LookupModule(LookupBase):
        def __init__(self, loader=None, templar=None, **kwargs):
            super(LookupModule, self).__init__(loader=loader, templar=templar, **kwargs)
            self.searchpath = 'search/path'
            self.files = []
            self.path = None


# Generated at 2022-06-13 13:43:17.217272
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # define default values and return values
    # these values are used to mock functions which should not be called
    # in context of this test
    def_returns = {
        'find_file_in_search_path': None
    }

    # define mocked functions
    mock_functions = {
        # '_search_path': LookupModule._search_path,
        '_templar.template':
            lambda self, text: text,
    }

    # define expected results

# Generated at 2022-06-13 13:43:18.323541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement
    pass

# Generated at 2022-06-13 13:43:28.097922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global LookupModule

    # import only after hitting usage to speed up loading for other tasks
    from ansible.plugins.loader import lookup_loader

    LookupModule = lookup_loader.get('first_found', class_only=True)

    from ansible.utils.display import Display
    display = Display()

    display.verbosity = 6

    # this used to be global
    # TODO: remove
    def _split_on(terms, spliters=','):

        # TODO: fix as it does not allow spaces in names
        termlist = []
        if isinstance(terms, string_types):
            for spliter in spliters:
                terms = terms.replace(spliter, ' ')
            termlist = terms.split(' ')

# Generated at 2022-06-13 13:43:41.398818
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Uses any simple 'mapping' type
    class IdentityMapping(Mapping):
        def __init__(self, *args, **kwargs):
            self.store = dict()
            self.update(dict(*args, **kwargs))

        def __getitem__(self, key):
            return self.store[key]

        def __setitem__(self, key, value):
            self.store[key] = value

        def __iter__(self):
            return iter(self.store)

        def __len__(self):
            return len(self.store)

        def copy(self):
            # Return a shallow copy of the mapping
            return IdentityMapping(self.store.copy())

        def __repr__(self):
            return '{0!r}'.format(self.store)

    # Uses

# Generated at 2022-06-13 13:43:42.342814
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: how to test this?
    pass

# Generated at 2022-06-13 13:43:43.167105
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: write
    pass


# Generated at 2022-06-13 13:43:50.203237
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit tests for method run of class LookupModule
    '''
    # Construct an instance of LookupModule
    lookup_mod = LookupModule()

    # Test with default options
    input_params = {}
    expected_result = []

    # TODO: unit test is not running  because the error is:
    # '_AssertRaisesContext' object has no attribute '_raiseFailure'
    # and the test processing is rstricted to:
    # try:
    #     with self.assertRaises(exception) as context:
    #         return test_method()
    #     self._raiseFailure(str(context.exception))
    # except AssertionError as e:
    #     # save the current exception
    #     self._raiseFailure(e)
    # except Exception:
    #     #

# Generated at 2022-06-13 13:43:52.638078
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    result = lu.run('any', dict())
    assert result == ['any']



# Generated at 2022-06-13 13:44:00.729274
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:44:10.341996
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Some basic fixtures
    subdir = 'files'
    terms = ['foo', 'bar', 'baz']
    paths = ['path/to/files', 'path/two']
    files = ['foo.txt', 'bar.txt', 'baz.txt']

    # Create the object and stub out the 'find_file_in_search_path'
    lm = LookupModule()
    lm._subdir = subdir
    lm.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing: fn

    # Make sure we can search by files
    kwargs = {'files': files, 'paths': None}
    total_search, skip = lm._process_terms(terms, None, kwargs)
    assert total_search == files
    assert skip is False

    #

# Generated at 2022-06-13 13:44:15.304965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    path = os.path.join(os.path.dirname(__file__), '..', '..', 'lookup_plugins', 'first_found.py')
    path = os.path.abspath(path)
    # mock.patch()'s __file__ will be relative from the directory
    # containing the python source, hence the need for realpath.
    mock_path = '{0}.mock'.format(path)
    sys.modules['j2_plugin_vars'] = MagicMock(__file__=mock_path)
    mock_path = '{0}.mock'.format(path)
    sys.modules['j2_filter_plugins'] = MagicMock(__file__=mock_path)

    # Variables
    task = MagicMock()
    variables = MagicMock()
    task

# Generated at 2022-06-13 13:44:25.801689
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import builtins
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import lookup_loader

    # check if we have the lookup plugin finder loaded
    assert 'first_found' in lookup_loader._lookup_plugins

    builtins.open = lambda path, mode: 'filecontent'
    os = pytest.importorskip('os')
    os.path = pytest.importorskip('os.path')
    os.path.isfile = lambda _: True
    os.path.isdir = lambda _: False

    variables = VariableManager()
    loader = DataLoader()
   

# Generated at 2022-06-13 13:44:34.467151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile, shutil

    test_dir = tempfile.mkdtemp()
    test_file = os.path.join(test_dir, 'test_file.txt')
    with open(test_file, 'w') as f:
        f.write('TEST')
    d = {
        'lookup_plugin_name': 'first_found',
        '_terms': [test_file],
    }
    l = LookupModule()
    r = l.run([d], None)
    assert r == [test_file]
    shutil.rmtree(test_dir)

# Generated at 2022-06-13 13:44:48.500488
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleLookupError
    from ansible.plugins.lookup import LookupBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}

    play_context = dict(
        loader=loader,
        variable_manager=variable_manager,
        all_vars=dict()
    )

    path = '.'
    for d in [u'files', u'default']:
        p = os.path.join(path, d)

# Generated at 2022-06-13 13:45:00.057562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # For more information on how to unit test ansible plugins, please refer to:
    # https://docs.ansible.com/ansible/devel/dev_guide/developing_plugins.html#testing-plugins
    # Basic parameters
    terms = ['file_exists_1', 'file_exists_2', {
        'files': 'file_exists_3,file_exists_4',
        'paths': 'tests/test_data',
    }]
    variables = {}
    options = {}
    # Setup the object we want to unit test
    LookupModule_object = LookupModule()
    # Unit test the LookupModule.run() method

# Generated at 2022-06-13 13:45:14.170401
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mock 'os' module for LookupModule
    class FakeOs(object):
        def __init__(self, *args, **kwargs):
            pass

        def path_exists(self, path):
            if path == '/some/path/first_found_in_path.txt':
                return True
            else:
                return False

    real_os = LookupModule.os

# Generated at 2022-06-13 13:45:22.113761
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class OptionsModule():
        def __init__(self, var_options=None, direct=None):
            self.var_options = var_options
            self.direct = direct

    class LookupBase_TEST(LookupBase):
        def __init__(self, loader, templar, **kwargs):
            self._loader = loader
            self._templar = templar

        def find_file_in_search_path(self, variables, subdir, file, ignore_missing=False):
            if file == 'found.txt':
                return file
            else:
                return None

    # From test_run, args=(files=None, paths=None, skip=False):
    terms = ['nofile.txt']
    options = OptionsModule(var_options=None, direct=None)
    lookup = Lookup

# Generated at 2022-06-13 13:45:32.758091
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six.moves import builtins

    builtins.__ansible_module_builtin__ = True

    import ansible.plugins.lookup.first_found
    import ansible.template
    import ansible.vars
    import os

    lookup_module = LookupModule()

    def _read_var_file(file_name):
        return ""

    def _match_and_list(self, path, pattern):
        # simulate files in 'files/' dir relative to play, tasks and current dir
        if 'files' in path:
            path = os.path.join(path, 'files')
        if pattern in ('test1.txt', 'test2.txt', 'test3.txt'):
            if path in ('/tmp/files', 'files', 'files/files'):
                return

# Generated at 2022-06-13 13:45:40.833799
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for lookup for type Sequence
    params = [{'files': ['foo', 'bar'], 'paths': ['path/to']}, {'files': ['foo', 'bar'], 'paths': ['path/to']}]
    expected_result = ['/path/to/foo']
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    mock_find_file_in_search_path = lambda self, variables, subdir, fn: os.path.join(fixtures_path, subdir, 'foo') if subdir == 'files' else None
    LookupModule.find_file_in_search_path = mock_find_file_in_search_path

    lookup_obj = LookupModule()

# Generated at 2022-06-13 13:45:46.254386
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Runs a simple test for LookupModule.run."""
    test_terms = ["test1.txt", "test2.txt"]
    test_variables = ""
    test_kwargs = ""

    lookup_module = LookupModule()
    result = lookup_module.run(test_terms, test_variables, test_kwargs)
    assert result

# Generated at 2022-06-13 13:46:01.126476
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class LookupModuleMock(LookupModule):

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=True):
            # FIXME: should mock vars not hardcoding important variable.
            if 'omit_a.yml' in fn:
                raise AnsibleLookupError("something went wrong.")
            return fn

    subdir = 'files'
    findme = [
        '/path/to/foo.txt',
        'bar.txt',  # will be looked in _subdir subdir relative to role and/or play
        {'files': 'biz.txt', 'paths': "/path/to"},
        'omit_a.yml',
        {'files': 'omit_b.yml', 'paths': "/path/to"},
    ]
   

# Generated at 2022-06-13 13:46:13.686082
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    lu._templar.available_variables = dict(a="A", b="B")
    try:
        lu._templar.template(1)
        assert False, "Should have failed"
    except Exception:
        pass

    lu.find_file_in_search_path = lambda m, v, k: "to_%s_%s_%s_but_not_found" % (v, m, k)
    lu.run([], dict(a="foo", b="bar"))
    assert False, "Should have failed"

    lu.run([], dict(a="foo", b="bar"), files="A", paths="B")
    assert False, "Should have failed"


# Generated at 2022-06-13 13:46:20.855515
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup.get_basedir = lambda: os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test/test_lookup_plugins')

    # file is found
    assert(lookup.run(terms=['xxxx.cfg'], variables={})[0] == os.path.join(lookup.get_basedir(), 'files/xxxx.cfg'))

    # file is not found
    assert(lookup.run(terms=['xxxx.cfg'], variables={}) == [])

# Generated at 2022-06-13 13:46:42.736583
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar = None
    lookup_module._subdir = None
    terms = ["{{ foo }}", {"files": "spam.txt", "paths": "{{ bar }},baz:quux", "skip": True}, "{{ baz }}"]
    variables = {"foo": "spam.txt", "bar": "quux", "baz": "eggs.txt"}
    kwargs = {}
    result = lookup_module.run(terms, variables, **kwargs)
    assert result == []

# Generated at 2022-06-13 13:46:51.850536
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    with open('test_lookup_plugin_first_found') as f:
        TEST_CASES = json.load(f)

    lookup_first_found = LookupModule()

    def _run(case, i):

        ret = lookup_first_found.run(case['terms'], case['variables'])

        if case.get('exception'):
            assert case.get('exception') in str(ret[1])
        else:
            assert ret == case['result'], 'test #{0}: {1}'.format(i, case.get('comment', ''))


# Generated at 2022-06-13 13:47:01.724884
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: this is a helper method to avoid idenitical code
    # during tests.
    # will convert the dict of paths and files to a list
    # to ensure that format is acceptable
    def get_terms_list(terms):
        paths = terms['paths']
        files = terms['files']

        terms_list = []
        for path in paths:
            for file in files:
                terms_list.append(path + os.sep + file)

        return terms_list

    # NOTE: the point of below tests is to ensure that after the
    # the dictionary 'terms' has been created that it is in fact
    # converted to a list in the _process_terms method.

    # all of the below tests have a combination of dict options,
    # list options and paths and files that do and don't exist.

    # NOTE

# Generated at 2022-06-13 13:47:08.858326
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    terms = [
        {
            'files': 'file1',
            'paths': 'path1'
        },
        {
            'files': 'file2:file3',
            'paths': 'path2:path3'
        },
        {
            'files': 'file4,file5',
            'paths': 'path4,path5'
        }
    ]

    variables = {}
    kwargs = {}

    results = module.run(terms, variables, **kwargs)
    assert len(results) == 1
    assert results[0] == 'path4/file4'


# Generated at 2022-06-13 13:47:21.057903
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.errors import AnsibleLookupError

    # Setup module parameters
    tl = LookupModule()
    tl._subdir = 'files'
    tl.set_options(var_options={}, direct={
        'files': ['vars/dummy.yml'],
        'paths': [os.path.join(os.path.dirname(__file__), 'files')],
        'skip': False,
    })

    # Execute run method
    result = tl.run(terms=['vars/dummy.yml'], variables={}, )

    # Assert expected results
    assert (len(result) == 1)

# Generated at 2022-06-13 13:47:25.408357
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test that LookupModule object is correctly populated in ansible-playbook
    """
    # TODO: think how to test it
    return
    assert False

# Generated at 2022-06-13 13:47:34.990353
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.common._collections_compat import OrderedDict

    assert LookupModule._split_on(["foo,bar,baz"],[","]) == ["foo","bar","baz"]

    # pass some test options
    args = OrderedDict()
    args['_ansible_version'] = '2.9.9'
    args['_ansible_module_name'] = 'command'
    args['_ansible_module_setup'] = True
    args['_ansible_system'] = 'Linux'
    args['_ansible_debug'] = False
    args['_ansible_no_log'] = False
    args['_ansible_check_mode'] = False

# Generated at 2022-06-13 13:47:45.993562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()


    terms = [
      # testing: list of strings
      ['/tmp/foo.txt', '/tmp/bar.txt'],
      # testing: dictionary
      {'files': ['/tmp/foo.txt', '/tmp/bar.txt']}
    ]

    # testing: file does not exist
    results = lookup.run(terms, {})
    assert results == []

    # testing: file does not exist
    results = lookup.run(terms, {}, skip=True)
    assert results == []

    # testing: file does not exist
    lookup = LookupModule()
    results = lookup.run(terms, {}, skip=False)
    assert results == []

# Generated at 2022-06-13 13:47:57.478379
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test run of LookupModule
    module = LookupModule()

    # Test run for terms as a list
    terms = ['test1.txt', {'files': ['test2.txt']}]
    variables = {}
    result = module.run(terms, variables)
    assert result == [], "test_LookupModule_run: Expected: [], Found: %s" % result

    # Test run for terms as a list
    terms = [{'files': ['test1.txt'], 'paths': ['']}]
    variables = {}
    result = module.run(terms, variables)
    assert result == [], "test_LookupModule_run: Expected: [], Found: %s" % result

    # Test run for terms as a list
    terms = []
    variables = {}
    result = module.run

# Generated at 2022-06-13 13:48:10.847937
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a MockTemplar
    templar = Templar(loader=None, variables={})

    # create a LookupModule object
    lookupModule = LookupModule()

    # create an empty parameters dictionary
    params = {}

    # create an empty results dictionary
    results = {}

    # create an empty ansible_file_size dictionary (needed for method find_file_in_search_path)
    ansible_file_size = {}

    # define a list of files to be searched for
    files = ["file1", "file2"]

    # add file1 to the list of files to be searched for
    results["file1"] = "file1"

    # define a dictionary of kwargs
    kwargs = {}

    # get the output of method run()
    results = lookupModule.run(files, params, kwargs)

# Generated at 2022-06-13 13:48:35.415766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _fixture = [
        {'files': 'foo,bar,baz', 'paths': '/path/to/file,/other/path'},
        {'files': 'foo,bar,baz', 'paths': '/path/to/file,/other/path'},
        {'files': 'foo,bar,baz', 'paths': '/path/to/file,/other/path'},
    ]


# Generated at 2022-06-13 13:48:43.239461
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test corner cases
    assert lookup_module.run(terms=None, variables=None) is None
    assert lookup_module.run(terms="", variables=None) is None
    assert lookup_module.run(terms=[], variables=None) is None
    assert lookup_module.run(terms="fake_not_existing_file", variables=None) is None

    # Test all file types
    assert lookup_module.run(terms="testfile", variables=None) == ['/home/ubuntu/testfile']
    assert lookup_module.run(terms="testfile", variables=None, skip=True) == []

# Generated at 2022-06-13 13:48:53.876581
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:49:01.301303
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_loader()
    path = lookup.run(["/usr/share/ansible/"])
    assert path is not None
    assert len(path) == 3
    assert path[0] == "/usr/share/ansible/"
    assert path[1] == "HACKING.rst"
    assert path[2] == "README.md"

# Generated at 2022-06-13 13:49:09.586810
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 'skip' option with list of terms
    terms = ['foo.txt', 'bar.txt']
    kwargs = dict(skip=True)
    lookup = LookupModule()
    total_search, skip = lookup._process_terms(terms, dict(), kwargs)
    assert total_search == ['foo.txt', 'bar.txt']
    assert skip is True

    # Test 'skip' option with dict term
    terms = [dict(files=['foo.txt', 'bar.txt'], skip=True)]
    kwargs = dict()
    lookup = LookupModule()
    total_search, skip = lookup._process_terms(terms, dict(), kwargs)
    assert total_search == ['foo.txt', 'bar.txt']
    assert skip is True

    # Test 'skip' option overwriting 'skip

# Generated at 2022-06-13 13:49:25.256988
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Try to open files in the following order:
    #   1) 'default.yml' in the 'vars' subdir
    #   2) '{{ ansible_os_family }}.yml' in the 'vars' subdir
    #   3) '{{ ansible_distribution }}.yml' in the 'vars' subdir
    test_case_1 = [dict(files=['{{ ansible_distribution }}.yml', '{{ ansible_os_family }}.yml'],
                        paths=['vars']),
                   'default.yml']

    # Try to open file in the following order:
    #   1) '{{ ansible_virtualization_type }}_foo.conf' in the current directory
    #   2) 'default_foo.conf' in the current directory
    test_case

# Generated at 2022-06-13 13:49:34.425585
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    search_paths = []
    expected_result = []
    real_result = []

    # test_case1: terms = None
    lookup_plugin = LookupModule()
    terms = None
    variables = {}
    with pytest.raises(AnsibleLookupError) as exec_info:
        lookup_plugin.run(terms, variables)
    assert exec_info.value.args[0] == "No file was found when using first_found."
    assert real_result == expected_result

    # test_case2: terms is a str, not in search_path
    lookup_plugin = LookupModule()
    terms = "dummy.txt"
    variables = {}
    with pytest.raises(AnsibleLookupError) as exec_info:
        lookup_plugin.run(terms, variables)

# Generated at 2022-06-13 13:49:36.683584
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins
    lookup = ansible.plugins.lookup.first_found.LookupModule()
    assert lookup.run(['/tmp/foo', {'paths': '/tmp/'}],{}) == ['/tmp/foo']


# Generated at 2022-06-13 13:49:48.372025
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize a LookupModule object
    look = LookupModule()
    # Use a list as terms, a dict as variables, and a bool as an argument of param 'skip'
    terms = ['/path/file.txt']
    variables = {'hostvars': {'host1': {'ansible_os_family': 'RedHat'}}}
    skip = True
    # Run the method run

# Generated at 2022-06-13 13:49:55.448181
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First test, error if terms is None
    lookup = LookupModule()
    try:
        lookup.run(None)
        assert False, "Should have thrown an AnsibleLookupError"
    except AnsibleLookupError:
        pass

    # Second test, error if terms is an empty list
    try:
        lookup.run([])
        assert False, "Should have thrown an AnsibleLookupError"
    except AnsibleLookupError:
        pass

    # Test multiple file names, with no paths
    (files, path) = lookup.run(['foo', 'bar'], None)
    assert files == [], "Should not have found any files"
    assert path is None

    # Test multiple file names, with paths

# Generated at 2022-06-13 13:50:26.072461
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookupModule = LookupModule()

    # test without any parameters
    assert len(lookupModule.run(["testfile"])) == 0

    lookupModule._loader = "THIS IS A LOADER"
    assert lookupModule._loader is not None

    # test with terms and kwargs
    assert len(lookupModule.run(["testfile"], dict(files=["somefile"]))) == 0

    # test with terms, kwargs and variables
    assert len(lookupModule.run(["testfile"], dict(files=["somefile"]), dict(variable=None))) == 0

    # test with multiple terms and kwargs
    assert len(lookupModule.run(["testfile", "anotherTestFile"], dict(files=["somefile"]))) == 0

# Generated at 2022-06-13 13:50:35.362694
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    terms = ['foo.txt', 'bar.txt']
    variables = {}
    lookup_module = LookupModule()

    with pytest.raises(AnsibleLookupError) as execinfo:
        lookup_module.run(terms, variables)
    exception_msg = "No file was found when using first_found."
    assert execinfo.value.args[0] == exception_msg

    terms = [{'files': 'foo.txt', 'paths': '/path1'}, {'files': 'bar.txt', 'paths': '/path2'}]
    lookup_module = LookupModule()

    with pytest.raises(AnsibleLookupError) as execinfo:
        lookup_module.run(terms, variables)
    assert execinfo.value.args[0] == exception_msg



# Generated at 2022-06-13 13:50:43.960605
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import binary_type
    from ansible.module_utils._text import to_text
    from units.compat.mock import MagicMock, patch
    _mock_module_data = MagicMock()
    _mock_loader_data = MagicMock()
    _mock_module_data.params = {}
    _mock_loader_data.get_basedir.return_value = '/tmp'
    _mock_module_data.get_loader.return_value = _mock_loader_data
    _mock_module_data.fail_json.side_effect = AnsibleLookupError
    _mock_module_data._diff = False
    _mock_module_data._ansible_no_log = False
    # _mock_module_data.params

# Generated at 2022-06-13 13:50:54.445984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _get_lookup_instance():
        return LookupModule()

    lookup_instance = _get_lookup_instance()

    terms = [
        { 'files': 'foo.txt', 'paths': '~' },
        'bar.txt',
        [ 'foo.txt', 'bar.txt' ],
        { 'files': 'foo.txt', 'paths': '~' },
    ]
    variables = {}
    expected_result = [
        ['/home/user/foo.txt'],
        ['/home/user/bar.txt'],
        ['/home/user/foo.txt'],
        ['/home/user/foo.txt'],
    ]
    for i, term in enumerate(terms):
        result = lookup_instance.run(term, variables)

# Generated at 2022-06-13 13:51:08.443364
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    lookup_module = LookupModule()

    # no files and no paths
    with pytest.raises(AnsibleLookupError) as lookup_module_error:
        lookup_module.run([], {}, files=[], paths=[])
    assert "At least one file or path is required" in str(lookup_module_error.value)

    # no files, but with paths
    with pytest.raises(AnsibleLookupError) as lookup_module_error:
        lookup_module.run([], {}, files=[], paths=['/path1', '/path2'])
    assert "At least one file or path is required" in str(lookup_module_error.value)

    # with files and paths

# Generated at 2022-06-13 13:51:12.896529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    instance = LookupModule()
    assert instance.run(terms=['bar.txt','foo.txt'], variables={}) == ['bar.txt']
    assert instance.run(terms=[{'files':['bar.txt','foo.txt']}], variables={}) == []

# Generated at 2022-06-13 13:51:19.254259
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: this is a starting point for unit testing this module.
    # it is not complete/comprehensive and is not in the test/ subdir so it is not part of the test suite.

    # TODO: refactor to use test_runner.py
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar

    import os
    import shutil
    import sys

    # setup for testing
    test_dir = 'test_first_found'
    test_file = 'foo'
    test_data = 'contents'

    # setup temp dir/files
    sv_cwd = os.getcwd()
    # create our test dir
    os.mkdir(test_dir)


# Generated at 2022-06-13 13:51:30.356016
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test empty result
    lookups = LookupModule()

    # Test wrong file
    result = lookups.run(terms=["not_found"], variables=[])
    assert result == []

    # Test user file
    result = lookups.run(terms=["./files/test.txt"], variables=[])
    assert result == ["files/test.txt"]

    # Test wrong file and user file
    result = lookups.run(terms=["not_found", "./files/test.txt"], variables=[])
    assert result == ["files/test.txt"]

    # Test skip True
    result = lookups.run(terms=["./files/test.txt", "not_found"], variables=[], skip=True)
    assert result == ["files/test.txt"]

# Generated at 2022-06-13 13:51:38.772904
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from unittest import TestCase, TestLoader, TextTestRunner, TestSuite

    class LookupModuleTest(TestCase):

        def setUp(self):
            self.vault_password = 'secret'
            self.vault_password_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_vault_password_file')
            f = open(self.vault_password_file, 'w')
            f.write(self.vault_password)
            f.close()


# Generated at 2022-06-13 13:51:47.241304
# Unit test for method run of class LookupModule