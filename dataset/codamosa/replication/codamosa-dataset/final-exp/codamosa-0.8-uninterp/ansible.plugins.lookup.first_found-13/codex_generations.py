

# Generated at 2022-06-13 13:42:10.279896
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    source = [
        {
            'files': [
                'file1'
            ],
            'paths': [
                '/extra/path/'
            ]
        },
        'file2',
        'file3',
        'file4',
        {
            'files': [
                '/extra/file5'
            ],
            'paths': [
                '/path/'
            ]
        },
        '/extra/file6',
        '/extra/file7'
    ]
    lookup = LookupModule()
    assert lookup.run(source=source, variables={}, **{}) == ['/extra/path/file1', 'file2', 'file3', 'file4', '/extra/file5', '/extra/file6', '/extra/file7']


# Generated at 2022-06-13 13:42:17.710050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    import os

    lookup = LookupModule()
    lookup._merged_params = {
        'files': ['test.csv', 'test.yml'],
        'paths': [os.path.join(os.getcwd(), 'files')]
    }
    assert lookup.run(None, None) == ['test.csv']

# Generated at 2022-06-13 13:42:27.893295
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import tempfile
    from ansible.parsing.yaml.objects import AnsibleUnicode

    from ansible.module_utils.six import b
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import common as module_common

    from ansible.plugins.loader import lookup_loader

    loader = lookup_loader

    lookup = loader.get('first_found', class_only=True)()

    # create test files
    fd, test_file = tempfile.mkstemp()
    os.close(fd)
    with open(test_file, "wb") as f:
        f.write(b("Hello, World!"))

    fd, another_file = tempfile.mkstemp()
    os.close(fd)

# Generated at 2022-06-13 13:42:34.572267
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # checking for exact order of results is too rigid,
    # this test tries to only check for the results to be correct

    # our test
    terms = [
        {
            'files': 'file1,file2',
            'paths': '/path1:/path2'
        },
        {
            'files': 'file3,file4',
            'paths': '/path3:/path4'
        },
        {
            'files': '',
            'paths': 'path5:path6'
        },
        {
            'files': '',
            'paths': ''
        }
    ]
    variables = {
        'ansible_env': {
            'ANSIBLE_CONFIG': '',
            'ANSIBLE_ROLES_PATH': ''
        }
    }

# Generated at 2022-06-13 13:42:45.857248
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._subdir = 'files'

    # NOTE: the _templar is not initialized and does not work (a lot of stuff missing)
    #       so the result is not what the run method returns in a real environment
    def fake_finder(variables, subdir, fn, ignore_missing):
        if fn == 'foo':
            return '/path/to/foo'
        elif fn == 'bar':
            return None
        else:
            return 'test'
    lookup.find_file_in_search_path = fake_finder

    assert lookup.run([], {}) == []
    assert lookup.run(['foo'], {}) == []
    assert lookup.run(['foo', 'bar'], {}) == []
    assert lookup.run(['bar', 'foo'], {}) == []

# Generated at 2022-06-13 13:42:52.462645
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        ["foo", "bar", "baz"],
        ["bar", "baz", "foo"],
        ["baz", "foo", "bar"],
    ]
    variables = []

    lookup = LookupModule()

    # Terms is a string
    try:
        lookup.run(terms="", variables=variables)
    except AnsibleLookupError:
        pass
    else:
        raise AssertionError("Fail to check terms is a string")

    # Terms is not a string
    lookup.run(terms=terms, variables=variables)
    return

# Generated at 2022-06-13 13:42:59.206992
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    tl = LookupModule()
    tl.set_loader(AnsibleLoaderMock())
    f = FirstFoundTest()
    results = []
    for term in f.terms:
        results.append(tl.run(term, f.variables, **f.options))
    assert results == f.expected, 'lookup module results are not as expected: %s' % results


# Generated at 2022-06-13 13:43:10.828878
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # initialization
    lookup_ins = LookupModule()

    # set up variables
    terms = []
    terms_1 = {'files': 'search_file', 'paths': 'search_path'}
    terms_2 = ['search_file2', 'search_path2']
    terms.append(terms_1)
    terms.append(terms_2)
    kwargs = {'files': 'search_file3', 'paths': 'search_path3'}
    variables = {}
    variables['ansible_playbook_python'] = "/usr/bin/python"
    variables['ansible_playbook_python'] = variables['ansible_playbook_python'] + "/test_LookupModule_run"
    variables['group_names'] = ['test_host']

# Generated at 2022-06-13 13:43:23.499950
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module_obj = LookupModule()
    lookup_module_obj._templar = None
    lookup_module_obj.basedir = '.'
    lookup_module_obj._loader = '.'

    terms = [{'skip': False, 'files': '', 'paths': '/etc/ansible/'}]
    assert lookup_module_obj.run(terms) == []

    terms = [{'skip': False, 'files': 'foo', 'paths': '/etc/ansible/'}]
    assert lookup_module_obj.run(terms) == []

    terms = [{'skip': False, 'files': 'hosts', 'paths': ''}]
    assert lookup_module_obj.run(terms) == []


# Generated at 2022-06-13 13:43:36.084191
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.module_utils.six import PY3

    lookup_module = LookupModule()

    # Test with a single term
    term_single = '/path/to/single_file.conf'
    search_list, _ = lookup_module._process_terms(term_single, {}, {})
    assert search_list == [term_single]

    # Test with a list of terms
    term_list = ['/path/to/file1.conf', '/path/to/file2.conf']
    search_list, _ = lookup_module._process_terms(term_list, {}, {})
    assert search_list == term_list

    # Test with list of terms and dictionary with files

# Generated at 2022-06-13 13:43:51.355287
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("\n Unit test for method run of class LookupModule ")

    # TEST 1
    print("\n TEST 1: Check lookup method with invalid term")
    # Initialize lookup module
    lookupObject = LookupModule()
    # call lookup method with invalid term
    try:
        lookupObject.run(terms=0, variables=None, **{})
    except AnsibleLookupError as e:
        print(str(e))

    # TEST 2
    print("\n TEST 2: Check lookup method with string type of term")
    # Initialize lookup module
    lookupObject = LookupModule()
    # call lookup method with invalid term
    try:
        lookupObject.run(terms='foo', variables=None, **{})
    except AnsibleLookupError as e:
        print(str(e))

    # TEST 3


# Generated at 2022-06-13 13:44:00.061473
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.constants as C
    # Setup the module
    m = LookupModule()
    m.get_option = lambda key: {
        'omit': C.DEFAULT_OMIT_INTERNAL_KEYS,
        'allow_duplicates': True,
        'errors': 'strict',
        'skip': False,
        'variables': {},
        'paths': [],
        'files': [],
    }[key]

    # Setup the templar
    class MockTemplar:
        def template(self, term):
            return term

    m._templar = MockTemplar()

    # Setup the find_file_in_search_path mock

# Generated at 2022-06-13 13:44:09.947103
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # initialize
    lookup_module = LookupModule()

    # only terms, use default parameters
    terms = ['file1.txt', '/path/to/file2.txt', '/path/to/file3.txt']
    result = lookup_module.run(terms, {})
    assert(result == ['/path/to/file2.txt'])
    #
    # use a list inside a list
    result = lookup_module.run([terms], {})
    assert(result == ['/path/to/file2.txt'])
    #
    # set 'skip' to True
    result = lookup_module.run([terms], {}, skip=True)
    assert(result == [])
    #
    # set 'paths'
    result = lookup_module.run([terms], {}, paths='/path/to')


# Generated at 2022-06-13 13:44:15.144345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # set up mock class
    test_inst = LookupModule()

    # set up mocks
    test_inst._templar = mock.Mock()

    # invoke run
    test_inst.run('foo', 'bar')

    # assert
    assert test_inst._templar.template.assert_called_once_with('foo')

# Generated at 2022-06-13 13:44:19.472973
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup test
    module = LookupModule()

    # Test call
    module.run(terms=None, variables=dict())



# Generated at 2022-06-13 13:44:27.070129
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = LookupModule()

    test_terms = [
        {'files': 'foo, bar.txt', 'paths': '/path:/path2', 'skip': False},
        {'files': 'foo', 'paths': '/path:/path2', 'skip': False},
        {'files': 'foo, bar.txt', 'paths': '/path:/path2'},
        [
            {'files': 'foo, bar.txt'},
            {'paths': '/path:/path2'},
        ]
    ]


# Generated at 2022-06-13 13:44:37.253681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    import pytest

    def FakeTemplar():
        return

    def FakeDataLoader():
        return

    def FakeInventoryManager():
        return

    def FakeVariableManager():
        return

    def FakeFindFileInSearchPath():
        return

    path = '/tmp/fake/path.txt'

    #
    # case 1: term is a string and it is not a valid path, skip=True
    #
    fake_terms = 'fake.txt'
    fake_variables = FakeVariableManager()
    fake_kwargs = {'skip': True}
    fake_filelist = ['fake.txt']
   

# Generated at 2022-06-13 13:44:48.411911
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _find_file_in_search_path(variables, subdir, fn, ignore_missing=False):
        return fn

    # setup a dummy class
    class TestClass(LookupModule):

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
            return _find_file_in_search_path(variables, subdir, fn, ignore_missing=ignore_missing)

    terms = [
        '/path/to/foo',
        {'files': 'foo,bar', 'paths': '/path/to,/path/from'},
        '/path/from/bar',
        {'files': 'baz'},
    ]

    variables = {}
    kwargs = {}

    # call the function
    lookup = TestClass()
    lookup.run

# Generated at 2022-06-13 13:44:55.134844
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run([{'files':['foo','bar','baz'], 'paths': ['roles/1','roles/2','roles/3']}], dict(
        ansible_play_basedir = '/path/to/play/basedir',
        ansible_role_basedir = '/path/to/role/basedir'
    )) == ['roles/3/baz']

# Generated at 2022-06-13 13:45:02.274556
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # Test if the list of search terms is correctly built with the given arguments
    # simple cases
    terms = module._process_terms(terms=['/etc/my_first_file.conf'], variables={}, kwargs={})
    assert module._flatten(terms[0]) == ['/etc/my_first_file.conf']
    terms = module._process_terms(terms=['/etc/my_first_file.conf', '/etc/my_second_file.conf'], variables={}, kwargs={})
    assert module._flatten(terms[0]) == ['/etc/my_first_file.conf', '/etc/my_second_file.conf']
    # then, with inline config

# Generated at 2022-06-13 13:45:18.611857
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import os
    import pytest
    import ansible.constants as C
    ##################################################
    # Fixtures
    ##################################################

    @pytest.fixture
    def variable_manager():
        ##################################################
        # Variable manager
        ##################################################
        variable_manager = VariableManager()
        variable_manager.extra_vars = {'inventory_dir': 'tests/inventory', 'inventory_file': 'tests/inventory/hosts'}
        return variable

# Generated at 2022-06-13 13:45:30.418490
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping

    class LookupModuleMock(LookupModule):
        def set_options(self, var_options, direct):
            self.var_options = var_options
            self.direct = direct

        def get_option(self, name):
            return self.direct.get(name)

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
            if fn == 'bar.txt':
                return fn
            else:
                return None

        def _templar(self, term):
            assert isinstance(term, string_types)
            return term

        def _templar_template(self, term, convert_bare=False, fail_on_undefined=False):
            assert isinstance

# Generated at 2022-06-13 13:45:39.596483
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    from ansible.inventory.manager import InventoryManager

    # Lets use a temporary plugin to get an object of LookupModule
    class TestLookup(LookupBase):
        def __init__(self):
            super().__init__()

        def run(self, terms, variables, **kwargs):
            return terms

    # Default args of LookupModule
    my_plugin = TestLookup()
    my_plugin._display = Display()
    my_plugin._subdir = 'files'


    # Create variable manager with variable a
    variable_manager = VariableManager()

# Generated at 2022-06-13 13:45:51.275359
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'inventory_hostname': 'test'}
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 13:46:00.509463
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._templar = None
    lookup.find_file_in_search_path = lambda variables, subdir, filename, ignore_missing=False: filename
    # test_terms
    #  - string
    #  - mapping
    #  - list of strings
    #  - unhandled value

# Generated at 2022-06-13 13:46:13.149434
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_unicode

    sample_file = b'\x4B\x4B\x4B\x4B\x4B\x4B'

    class LookupModuleMock(LookupModule):

        def __init__(self, loader=None, templar=None, **kwargs):
            self.set_loader(loader)
            self.set_templar(templar)

        def find_file_in_search_path(self, variables, subdir, file_name, ignore_missing=False):
            self.assertEqual(subdir, 'files')
            return '/path/to/' + file_name


# Generated at 2022-06-13 13:46:24.059301
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_term = [
        {
            'files': ('/etc/group,/etc/groop'),
            'paths': ('/etc/group,/etc/groop'),
            'skip': False,
        },
        {
            'files': ('/etc/group,/etc/groop'),
            'paths': ('/etc/group,/etc/groop'),
            'skip': False,
        },
        {
            'files': ('/etc/group,/etc/groop'),
            'paths': ('/etc/group,/etc/groop'),
            'skip': False,
        },
    ]

    test_variables = dict()

    test_kwargs = dict()

    LookupModule().run(test_term, test_variables, **test_kwargs)


test_Look

# Generated at 2022-06-13 13:46:32.842437
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test for the LookupModule method run. """
    # Test verifies that no file was found
    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    lookup_module._templar = None
    lookup_module._loader = None
    lookup_module._find_needle = None

    file_path = lookup_module.run(['fake1', 'fake2'], variables=dict())
    assert file_path == [], "Should have returned an empty list."

    # Test verifies that no file was found but skip error=True
    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    lookup_module._templar = None
    lookup_module._loader = None
    lookup_module._find_needle = None

    file_path = lookup_module

# Generated at 2022-06-13 13:46:45.309248
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['first_found_file.yml', 'other_first_found_file.yml', {'files': 'second_first_found_file.yml', 'paths': 'where/to/look'}]
    # To test this method, we need to bypass _process_terms and use search directly
    # since it's not possible to test with a file system
    variables = {'files': ['first_found_file.yml', 'second_first_found_file.yml'], 'paths': 'where/to/look'}
    obj = LookupModule()
    assert obj.run(terms, variables) == ['where/to/look/second_first_found_file.yml'], "run() doesn't return the correct value"

# Generated at 2022-06-13 13:46:57.651093
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create mock templar
    def template(data):
        return data

    # create mock find_file_in_search_path
    # _templar.template(fn) is equal to fn
    def find_file_in_search_path(variables, subdir, filename, ignore_missing=True):
        # return the first file in the list of files to find
        return filename if filename in ['file1', 'file2'] else None

    # create mock and init lookup
    lookup_mock = LookupModule(loader=None, templar=template)
    lookup_mock.find_file_in_search_path = find_file_in_search_path
    lookup_mock.set_options(var_options=None, direct=None)
    lookup_mock._subdir = 'files'

    # execute

# Generated at 2022-06-13 13:47:03.787057
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    res = lookup_module.run(["test_file"], {})
    assert res == ['/etc/ansible/test_file']


# Generated at 2022-06-13 13:47:04.709310
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO:
    pass

# Generated at 2022-06-13 13:47:15.396503
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['tests/inventory/test_hosts.yml'])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    play_context = PlayContext()
    play_context.remote_user = 'test_user'
    play_context.connection = 'local'
    play_context.module_name = 'copy'
    play_context.executor = 'by_value'
    play_context.subdir = ''
    lookup_module = LookupModule()
    lookup_module._

# Generated at 2022-06-13 13:47:25.844804
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: update tests after _split_on is fixed
    assert False

# Generated at 2022-06-13 13:47:35.263136
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar = DummyTemplar()
    assert l.run([], {}, files='file1', paths='/tmp/path1') == ['/tmp/path1/file1']
    assert l.run([], {}, files='file1', paths='/tmp/path1:/tmp/path2') == ['/tmp/path1/file1', '/tmp/path2/file1']
    assert l.run([], {}, files='file1,file2', paths='/tmp/path1:/tmp/path2') == ['/tmp/path1/file1', '/tmp/path2/file1', '/tmp/path1/file2', '/tmp/path2/file2']

# Generated at 2022-06-13 13:47:47.510155
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def run_test(class_instance, terms, variables, expected_files_list, skip=False):
        assert class_instance.run(terms, variables, skip=skip) == expected_files_list

    os.environ['ANSIBLE_GET_URL_TIMEOUT'] = '1'

    lu = LookupModule()

    # simple filename
    files_list = ['file1.txt', 'file2.txt', 'file3.txt']
    run_test(lu, files_list, {}, files_list)

    # use first found file
    run_test(lu, ['file1.txt', 'file2.txt', 'file3.txt'], {}, ['file1.txt'])

# Generated at 2022-06-13 13:47:52.072515
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_obj = LookupModule()

    # test return value of case 1
    terms = ["/path/to/foo.txt"]
    variables = []
    LookupModule_ret1 = LookupModule_obj.run(terms, variables, **{})


# Generated at 2022-06-13 13:47:54.784299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module_lookup = LookupModule()
    assert module_lookup.run([{'files': '/tmp', 'paths': 'var'}]) == []


# Generated at 2022-06-13 13:48:01.237230
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os

    # Build fake lookup class
    class FakeClass:
        def __init__(self, path):
            self._basedir = path
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=True):

            path = os.path.join(self._basedir, os.path.dirname(fn))
            fn = os.path.join(path, os.path.basename(fn))

            return fn if os.path.exists(fn) else None

    # Build fake templar class
    class FakeTemplarClass:
        def template(self, fn):
            return fn

    # If a file is found, return path to the file (as string)
    templar = FakeTemplarClass()

# Generated at 2022-06-13 13:48:13.687453
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # based on a combination of tests
    #   - test/units/plugins/lookup/test_first_found.py
    #   - test/units/plugins/lookup/test_find.py
    class Tester:
        def __init__(self, value=None, template=None, search_path=[], found=True):
            self._value = value
            self._template = template
            self._search_path = search_path
            self._found = found

        def template(self, value):
            return self._template

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing):
            if self._found:
                return self._value

        def get_option(self, option_name):
            if 'files' == option_name:
                return self._value

    t

# Generated at 2022-06-13 13:48:28.769355
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.first_found import LookupModule
    l = LookupModule()
    l.get_option = lambda x: []
    l.find_file_in_search_path = lambda x,y,z,**kwargs: z
    fn = l.run([['f1', 'f2'], ['f3', 'f4']], {}, skip=True)
    assert fn == [u'f1', u'f2', u'f3', u'f4']

    # TODO: add more tests

# Generated at 2022-06-13 13:48:39.685693
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    mLm = LookupModule()

    # create the structure needed for this test,  the default search path is './',
    #  so we need to set it to the test directory
    options = {}
    options['_basedir'] = os.path.join(os.path.dirname(__file__))
    options['_ansible_vault_password'] = None

    dataloader = DataLoader()
    variables = VariableManager()
    ret = mLm.run(terms=[], variables=variables, **options)
    assert ret == []

    ret = mLm.run(terms=['test.txt'], variables=variables, **options)

# Generated at 2022-06-13 13:48:47.546675
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __main__
    import os
    tmp = os.path.join(os.path.dirname(__main__.__file__), 'test_test_first_found', 'tmp')
    files = os.path.join(os.path.dirname(__main__.__file__), 'test_test_first_found', 'files')
    os.chdir(tmp)
    assert(os.getcwd() == tmp)
    assert(os.path.exists(files))
    os.chdir(tmp)
    lookup_plugin = LookupModule()
    # test 'dual mode', passing a list for files and paths

# Generated at 2022-06-13 13:48:55.660059
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('first_found', class_only=True)
    # Tests for parameter 'terms'
    with pytest.raises(AnsibleLookupError, message="Invalid term supplied, can handle string, mapping or list of strings but got: <class 'int'> for 1"):
        lookup.run(1, {})
    # Tests for parameter 'variables'
    with pytest.raises(AssertionError, message="Expected type <class 'dict'> for variable: variables"):
        lookup.run([], 1)
    # Tests for return type
    lookup.run([], {}).__class__ is list
    # Test with all needed parameters

# Generated at 2022-06-13 13:49:07.852762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # no files and no paths
    terms = ['foo1.txt']
    variables = {}
    result = lookup.run(terms=terms, variables=variables)
    assert result == [
        'foo1.txt']

    # only files
    terms = ['foo2.txt', 'foo3.txt']
    variables = {}
    result = lookup.run(terms=terms, variables=variables)
    assert result == [
        'foo2.txt']

    # only paths
    terms = [{'files': [], 'paths': ['path1', 'path2']}]
    variables = {}
    result = lookup.run(terms=terms, variables=variables)
    assert result == [
        'path1/foo1.txt']

    # both files and paths

# Generated at 2022-06-13 13:49:18.009369
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  ## PREPARE TEST
  # Vars
  import os
  import shutil
  ALL_DIR = os.getcwd()
  FILES_DIR = os.path.join(ALL_DIR, 'files/')
  PATHS_DIR = os.path.join(ALL_DIR, 'paths/')
  TASKS_DIR = os.path.join(ALL_DIR, 'roles/my-role/tasks/')
  with open(os.path.join(FILES_DIR, 'first_found.txt'),'w') as file:
    file.close()
  with open(os.path.join(PATHS_DIR, 'first_found.txt'),'w') as file:
    file.close()

# Generated at 2022-06-13 13:49:25.601158
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import pytest
    from ansible.errors import AnsibleLookupError
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    sys.modules['ansible.module_utils.six'] = __import__('ansible.module_utils.six')
    sys.modules['ansible.module_utils.common._collections_compat'] = __import__('ansible.module_utils.common._collections_compat')
    sys.modules['ansible.module_utils.six.moves'] = __import__('ansible.module_utils.six.moves')
    sys.modules['ansible.module_utils.parsing.convert_bool'] = __import__('ansible.module_utils.parsing.convert_bool')

# Generated at 2022-06-13 13:49:34.713147
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with two files
    lookup_obj = LookupModule()
    terms = ['/path/to/first_file',
             '/path/to/second_file']
    variables = {}
    assert lookup_obj.run(terms, variables) == \
        ['/path/to/first_file']

    # Test with three files
    lookup_obj = LookupModule()
    terms = ['/path/to/first_file',
             '/path/to/second_file',
             '/path/to/third_file']
    variables = {}
    assert lookup_obj.run(terms, variables) == \
        ['/path/to/first_file']

    # Test with zero files
    lookup_obj = LookupModule()
    terms = []
    variables = {}

# Generated at 2022-06-13 13:49:39.828081
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock some module internals
    def _templar_template(self, fn):
        expected_template = 'test/test.yml'
        if expected_template.find(fn) < 0:
          raise AnsibleUndefinedVariable
        return expected_template

    LookupModule._templar = None
    LookupModule._templar.template = _templar_template
    LookupModule.find_file_in_search_path = lambda *args: 'test/test.yml'

    lookup_module = LookupModule()


# Generated at 2022-06-13 13:49:50.188471
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:50:05.856238
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # print("in test_LookupModule_run()")

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variables = VariableManager()


# Generated at 2022-06-13 13:50:08.232559
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = [{'files': 'foo.txt', 'paths': ':', 'skip': True}]
    variables = {'file': 'somefile.yaml'}
    kwargs = {}
    LookupModule.run(terms, variables, **kwargs)

# Generated at 2022-06-13 13:50:19.821584
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    LookupModule_obj = LookupModule()
    LookupModule_obj._subdir = 'files'

    # Test case #1
    # term = 'string', Mapping, list of strings
    
    ff_obj1 = LookupModule()
    ff_obj1.set_options(var_options=None, direct={u'files': u'file1,file2', u'paths': u'path1,path2'})
    ff_obj1._subdir = 'files'

    total_search_list_list = total_search_list = ["path1/file1", "path1/file2", "path2/file1", "path2/file2"]
    skip = False


# Generated at 2022-06-13 13:50:31.050886
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Successful run, first_found search path
    """

    # arrange
    terms = ['foo', 'bar']
    variables = {'hostvars': {'hostgroup': {'baz': 'bing'}},
                 'inventory_hostname': 'hostgroup'}
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._templar = None # TODO: mock this
    lookup.set_loader({'_basedir': '.'})
    lookup.set_environment({'FOO': 'bar'})

    # act
    result = lookup.run(terms, variables)

    # assert
    assert result == ['bar']

# Generated at 2022-06-13 13:50:41.763042
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock variabels
    variables = {}

    # Mock arguments
    basedir = "/tmp/ansible_lookup_first_found_test"
    terms = ['foo', 'bar', 'baz']
    kwargs = {
        '_subdir': 'files',
        'errors': 'strict',
    }

    # Setup mock environment
    os.makedirs(basedir + "/files")
    open(basedir + "/files/foo", 'a').close()
    open(basedir + "/files/bar", 'a').close()

    lookup = LookupModule()
    lookup.basedir = basedir

    assert lookup.run(terms, variables, **kwargs) == [basedir + "/files/foo"]

    os.remove(basedir + "/files/foo")

# Generated at 2022-06-13 13:50:53.661132
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with skip set True
    lookup_instance = LookupModule()
    results = lookup_instance.run([{
        'files': 'first.txt',
        'paths': '/path/to/first.txt',
        'skip': True
    }], None)
    assert results == []

    # test when file exists
    lookup_instance.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing: '/path/to/first.txt'
    results = lookup_instance.run([{
        'files': 'first.txt',
        'paths': '/path/to/first.txt',
        'skip': False
    }], None)
    assert results == ['/path/to/first.txt']

    # test 'when not found' with skip set to False
    lookup_instance.find

# Generated at 2022-06-13 13:51:07.906860
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import io
    import pytest
    from textwrap import dedent
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.plugins.loader import lookup_loader
    from ansible.template.safe_eval import assert_bytes_or_unicode
    from ansible.template.safe_eval import assert_type_str

    LOADER = lookup_loader
    LOOKUP = LOADER.get("first_found")

    def add_search_paths(lookup, paths):
        search_paths = set(lookup.get_option('paths'))
       

# Generated at 2022-06-13 13:51:16.043771
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test for parameter terms
    class Mock_AnsibleTemplate():

        def __init__(self, obj):
            self._obj = obj

        def template(self, term):
            return '.'.join([self._obj, term])

    # Test for parameter variables
    class Mock_AnsibleVariables():

        def __init__(self, obj):
            self._obj = obj

        def __getitem__(self, key):
            return self._obj.lower()

    # Test for parameter kwargs
    class Mock_AnsibleKwargs():

        def __init__(self, obj):
            self._obj = obj

        def __getitem__(self, key):
            return self._obj[key]

    # Test for parameter subdir

# Generated at 2022-06-13 13:51:27.604692
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:51:33.788006
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    terms = [
        'one.txt',
        'two.txt',
        'three.txt'
    ]
    variables = 'placeholder'

    lookup = LookupModule()
    lookup.find_file_in_search_path = lambda v, s, f, i: 'path_to_' + f

    # Test
    assert lookup.run(terms, variables) == ['path_to_one.txt']

# Generated at 2022-06-13 13:51:59.645955
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os.path
    import shutil
    import tempfile
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    # create test dir
    tmpdir = tempfile.mkdtemp()
    # create test dir structure
    subdir = tempfile.mkdtemp(dir=tmpdir)
    subsubdir = tempfile.mkdtemp(dir=subdir)
    subsubsubdir = tempfile.mkdtemp(dir=subsubdir)
    # create files
    (fd1, testfile1) = tempfile.mkstemp(dir=subsubsubdir)
    (fd2, testfile2) = tempfile.mkstemp(dir=subsubsubdir)
    #