

# Generated at 2022-06-13 13:42:11.247563
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.six import StringIO
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    class FakeTemplar(Templar):
        def __init__(self):
            self.available_variables = dict()

        def template(self, var):
            try:
                return self.available_variables[var]
            except KeyError:
                raise UndefinedError

    lookup_mod = LookupModule()
    lookup_mod._subdir = None

    # noop test
    lookup_mod._templar = FakeTem

# Generated at 2022-06-13 13:42:25.710322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    lookup._subdir = 'files'
    
    def _find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        ignore_missing_mock = ignore_missing
        if fn == '/etc/foo.conf':
            return '/etc/foo.conf'
        else:
            return None

    lookup.find_file_in_search_path = _find_file_in_search_path

    def _get_option(self, param):
        if param == 'skip':
            return True
        else:
            return None

    lookup.get_option = _get_option

    class _templar:
        @staticmethod
        def template(fn):
            if fn == '/etc/foo.conf':
                return '/etc/foo.conf'

# Generated at 2022-06-13 13:42:35.948368
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    # Importing variables for test
    from ansible.vars.manager import VariableManager

    vars = VariableManager()
    vars.extra_vars = {
        "foo_file_name": "foo.txt",
        "bar_file_name": "bar.txt",
        "biz_file_name": "biz.txt",
        "baz_file_name": "baz.txt",
        "bop_file_name": "bop.txt",
    }
    # Testing with a list
    lm = LookupModule()
    lm._templar = vars
    assert lm.run(['fiz.txt', '{{ qux_file_name }}', '{{ foo_file_name }}'], vars) == []

# Generated at 2022-06-13 13:42:46.884575
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # The lookup does not work with the test data loader
    lu = LookupModule()

    # Empty
    assert lu.run([], variables={}, **{'_terms': [], 'files': [], 'paths': [], 'skip': False}) == []

    # Only paths to search
    assert lu.run([], variables={}, **{'_terms': [], 'files': [], 'paths': ['/tmp/nofile', '/path/to/file'], 'skip': False}) == []

    # Only files

# Generated at 2022-06-13 13:42:56.955351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    module = FakeModule()

    # test list of strings
    assert lookup_module.run([
        'foo.txt',
        'bar.txt',
    ], module, skip=True) == []

    # test list of dicts
    assert lookup_module.run([
        {'files': 'foo.txt'},
        {'files': 'bar.txt'},
    ], module, skip=True) == []

    # test list of list of strings
    assert lookup_module.run([
        ['foo.txt'],
        ['bar.txt'],
    ], module, skip=True) == []

    # test list of list of dicts

# Generated at 2022-06-13 13:43:09.064145
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import pytest
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils._text import to_text
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.contextmanager import chdir

    lookup = LookupModule()
    lookup._subdir = 'lookup_plugins'
    lookup.set_options(var_options=dict())

    with chdir(os.path.dirname(__file__)):
        x = lookup.run([], dict())
        assert x == [], to_text(x)
        with pytest.raises(AnsibleLookupError):
            x = lookup.run(["test_lookup_first_found_nonexistent.txt"], dict())
        assert x == [], to_text(x)

# Generated at 2022-06-13 13:43:14.631217
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six.moves.urllib.parse import quote as urlquote
    from ansible.parsing.ajson import AnsibleJSONEncoder
    import ansible.plugins.lookup.first_found as first_found

    # load a fake module
    module = type('First', (object,), dict(
        run_command=lambda *args: 0,
        exit_json=lambda *args: 0,
        fail_json=lambda *args: 0,
        _ansible_no_log=lambda *args: 0,
    ))()

    # load a fake var manager
   

# Generated at 2022-06-13 13:43:25.443135
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_params = {
        "files": ["file1.txt", "file2.txt"],
        "paths": ["/usr/share", "/usr/share/ansible"]
    }

    # testing: params:
    #       files:
    #         - file1.txt
    #         - file2.txt
    #       paths:
    #         - /usr/share
    #         - /usr/share/ansible
    assert ['/usr/share/file1.txt'] == LookupModule().run(
        terms=[test_params], variables={}, **{}
    )

    # testing: file1.txt
    assert ['/usr/share/file1.txt'] == LookupModule().run(
        terms=[test_params["files"][0]], variables={}, **{}
    )

    # testing

# Generated at 2022-06-13 13:43:37.413140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import pytest
    import ansible.plugins.loader
    import ansible.template
    import ansible.vars
    import ansible.constants

    # initialize
    ansible.constants.DEFAULT_MODULE_PATH = os.path.join(os.path.dirname(__file__), '../../../lib/ansible/modules')
    ansible.plugins.loader.add_directory(os.path.join(os.path.dirname(__file__), '..'), with_subdir=True)
    template = ansible.template

    # create an instance of ansible variables
    #
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/vars/__init__.py
    variables = ansible.vars.VariableManager

# Generated at 2022-06-13 13:43:40.867325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    f = LookupModule()
    t = ['path/file1.txt', 'path/file2.txt', ['path/file3.txt', 'path/file4.txt']]
    v = {}
    k = {}
    f.run(t, v, **k)

# Generated at 2022-06-13 13:43:58.441742
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # file is found in specified search paths
    assert lookup_module.run([{'files': 'foo', 'paths': ['/tmp/production', '/tmp/staging']}], {}) == ['/tmp/production/foo']

    # file is found in specified search paths
    assert lookup_module.run([{'files': 'foo', 'paths': ['test/data/production', 'test/data/staging']}], {}) == ['test/data/production/foo']

    # file is found in specified search paths
    assert lookup_module.run([{'files': 'foo', 'paths': ['test/data/staging', 'test/data/production']}], {}) == ['test/data/staging/foo']

    # file is found in specified search paths
    assert lookup_module

# Generated at 2022-06-13 13:44:08.765558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_runner(dict(basedir='./'))

    # Test missing file
    terms = ['this_is_an_invalid_file']
    variables = {}
    kwargs = {}
    try:
        l.run(terms, variables, **kwargs)
    except AnsibleLookupError as e:
        assert e.message == "No file was found when using first_found."

    # Test valid file
    terms = ['files/valid_file']
    variables = {}
    kwargs = {}
    result = l.run(terms, variables, **kwargs)
    assert result[0] == './files/valid_file'

    # Test missing file with more search paths

# Generated at 2022-06-13 13:44:16.759438
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    uut = LookupModule()
    result = uut.run( terms = [
                    {
                        'files': 'some_file,some_other_file',
                        'paths': 'some_path,some_other_path',
                        'skip': True,
                    },
                    {
                        'files': 'some_file,some_other_file',
                        'paths': 'some_path,some_other_path',
                        'skip': False,
                    },
                    'some_file'],
                variables = {},
                **{}
            )


# Generated at 2022-06-13 13:44:24.087730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    mod.set_options(var_options={}, direct={'files': ['foo.txt','bar.txt'], 'paths':['/tmp/profiles/']})
    mod_lst_dict = [mod]
    assert len(mod_lst_dict) == 1
    assert mod_lst_dict[0]['files'] == ['foo.txt','bar.txt']
    assert mod_lst_dict[0]['paths'] == ['/tmp/profiles/']


# Generated at 2022-06-13 13:44:35.172248
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ll = LookupModule()

    ll._templar = None  # mockup of ansible.parsing.dataloader.DataLoader
    ll._loader = None   # mockup of ansible.parsing.dataloader.DataLoader

    ll._templar.template = lambda s: s

    terms = [
        'single_file.txt'
    ]

    variables = dict()
    kwargs = {
        'files': '',
        'paths': '/path/to/files,/extra/path/,/'
    }
    result = ll.run(terms, variables, **kwargs)
    assert result == ['/path/to/files/single_file.txt']

    terms = [
        'single_file.txt', 'another_file.txt'
    ]

    variables = dict

# Generated at 2022-06-13 13:44:47.430097
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create test files
    fd, test1 = tempfile.mkstemp()
    os.close(fd)
    fd, test2 = tempfile.mkstemp()
    os.close(fd)
    fd, test3 = tempfile.mkstemp()
    os.close(fd)

    # Create test data

# Generated at 2022-06-13 13:44:59.385016
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test arguments and return values
    test_arguments = []
    test_returns = []

    # Options used in many test cases (key, values, default values)
    options_list = [("files", ['foo', 'bar', 'biz'], []), ("paths", ['foo', 'bar', 'biz'], []), ("skip", [True, False], False)]
    options_dicts = []

    # Loop over elements in options_list
    for element in options_list:

        # Generate all possible permutations for the dictionary items
        for values in itertools.product(*element[1]):

            # Create list with all possible dictionaries
            options_dicts.append(dict(zip(element[0], values)))

    # Remove all dictionaries which would give an empty result

# Generated at 2022-06-13 13:45:13.881352
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    task_vars = dict()
    vars = dict()

    # create mock templar
    from ansible.template import Templar
    templar = Templar(loader=None, variables=task_vars)

    # create mock loader
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    # create mock var manager
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()

    # create mock inventory
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager(loader=loader, sources='')
    play_context.set_inventory(inventory)

    # create LookupBase instance
    lookup_instance = LookupModule()
    lookup_instance.set_loader(loader)

# Generated at 2022-06-13 13:45:26.896174
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class FakeVars():
        def __init__(self, hostvars=None):
            self.vars = hostvars

    # test 1 - create a list of files tried
    lookup = LookupModule()
    files = [
        {
            "files": "jinja_file1.txt",
            "paths": "./, ./invalid/",
            "skip": "False"
        },
        {
            "files": "jinja_file2.txt",
            "paths": "./, ./invalid/",
            "skip": "True"
        }
    ]

    for f in files:
        total_search, _ = lookup._process_terms(f, FakeVars(), {})
        assert isinstance(total_search, list)
        assert len(total_search) == 4

    # test

# Generated at 2022-06-13 13:45:28.856281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # lookup_first_found = LookupModule()
    # lookup_first_found.run()
    assert 1 == 1

# Generated at 2022-06-13 13:45:41.773570
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with a string as terms
    terms = 'file.txt'
    lm = LookupModule()
    result = lm.run(terms, {})
    assert result == ['file.txt']

    # Test with a list as terms
    terms = ['file.txt']
    lm = LookupModule()
    result = lm.run(terms, {})
    assert result == ['file.txt']

    # Test with a list of string as terms
    terms = ['file1.txt', 'file2.txt']
    lm = LookupModule()
    result = lm.run(terms, {})
    assert result == ['file1.txt']

    # Test with a list as terms and 'files' as option
    terms = [{'files': ['file1.txt', 'file2.txt']}]
   

# Generated at 2022-06-13 13:45:52.543875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm._process_terms(['foo.yml', 'bar.yml'], {}, {'paths': '/path/to'}) == (['/path/to/foo.yml', '/path/to/bar.yml'], False)
    assert lm._process_terms(['foo.yml', 'bar.yml'], {}, {'paths': '/path/to:other/path'}) == (['/path/to/foo.yml', '/path/to/bar.yml', 'other/path/foo.yml', 'other/path/bar.yml'], False)

# Generated at 2022-06-13 13:46:03.672210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit test for method run of class LookupModule
    '''
    # unit-testing modules bootstrap code
    import os
    import sys
    import unittest
    import warnings

    module_path = os.path.realpath(os.path.dirname(__file__))
    sys.path.insert(0, module_path + "/../..")

    # This is required for the Ansible options to be registered
    from ansible.plugins.loader import lookup_loader

    # AnsibleLookupError exception handler
    from ansible.errors import AnsibleLookupError

    # Mock class from Ansible instead of using the real one
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-13 13:46:16.440997
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create instance
    obj = LookupModule()

    def testmethod(terms, variables, **kwargs):
        return obj.run(terms, variables, **kwargs)

    # define env variables needed to run
    os.environ['ANSIBLE_CONFIG'] = "test/test.cfg"
    os.environ['ANSIBLE_DATA_DIR'] = "test/test.dir"
    os.environ['ANSIBLE_LOCAL_TEMP'] = "test/test.local.temp"
    os.environ['ANSIBLE_REMOTE_TEMP'] = "test/test.remote.temp"

    # define mocks and test data
    fake_env = {'var': 'val'}
    fake_env2 = {'var2': 'val2'}
    fake_path = 'fake/path'
    fake

# Generated at 2022-06-13 13:46:26.776754
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.playbook.task_include import TaskInclude

    def _load_counts(validate_file):
        return TaskInclude._load_counts(validate_file)

    lookup_plugin = LookupModule()

# Generated at 2022-06-13 13:46:34.690760
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test one case of method run of class LookupModule in
    # ansible.plugins.lookup.first_found
    def file_is_present(filename='example.yml'):
        # create a file and write a string to it
        f = open(filename, 'w')
        f.write('Hello World')
        f.close()
        # if file was created successfully return True, otherwise False
        return os.path.isfile(filename)

    # locate current directory
    dir = os.path.dirname(os.path.abspath(__file__))
    # enter into directory 'test_utils'
    dir = os.path.join(dir, 'test_utils')
    # create test directory and enter it
    os.mkdir(dir)
    os.chdir(dir)

    # generate a list of

# Generated at 2022-06-13 13:46:40.942782
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = [
        {
            'files': 'foo',
            'paths': 'bar'
        },
        'foo',
        {
            'files': 'foo',
            'paths': 'bar'
        }
    ]

    variables = {}

    lookup_module.run(terms, variables)

# Generated at 2022-06-13 13:46:41.808756
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:46:51.541429
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    # Create mock environment variables
    mock_variables = dict()

    # Create mock files in mock search path
    mock_file1 = os.path.join('replace_path/','mock_file1')
    mock_file2 = os.path.join('replace_path/', 'mock_file2')
    # Create mock environment variables
    mock_variables['hostvars'] = dict()
    # Create mock functions for lookup
    lookup._process_terms = lambda x,y,z: ([mock_file1, mock_file2], False)
    lookup.find_file_in_search_path = lambda x,y,z,w: z
    # assert that the test will return the mock file

# Generated at 2022-06-13 13:47:01.267010
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myvar = dict(
        ansible_os_family='RedHat',
        ansible_distribution='RedHat',
        ansible_virtualization_type='Docker',
    )

    terms = [
        {'files': 'foo,file1', 'paths': '/tmp/production:/tmp/staging'},
        {'files': 'foo,file2', 'paths': '/tmp1/production:/tmp1/staging'},
        {'files': 'foo,file3', 'paths': '/tmp2/production:/tmp2/staging'},
        {'files': 'foo,file4', 'paths': '/tmp3/production:/tmp3/staging'},
    ]

    lookup_obj = LookupModule()
    lookup_obj._templar = DummyTemplar()
    lookup_obj._

# Generated at 2022-06-13 13:47:21.560222
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ls = LookupModule()
    ls._templar = None
    with open ('/tmp/example_lookup.yml', 'w') as f:
        f.write('example: a\n')
    r = ls.run(['/tmp/example_lookup.yml'], {}, path=[], skip=False)
    assert r == ['/tmp/example_lookup.yml']

# Generated at 2022-06-13 13:47:33.494276
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._subdir = 'files'
    lookup_module._templar.environment.loader = jinja2.DictLoader({})
    lookup_module._templar._available_variables = {}
    lookup_module._options = {}
    assert lookup_module.run(terms=['test.yml']) == ['test.yml']
    assert lookup_module.run(terms=['test.yml', 'test1.yml']) == ['test.yml']
    assert lookup_module.run(terms=['test.yml', 'files/test1.yml', 'files/test2.yml']) == ['test.yml']

# Generated at 2022-06-13 13:47:46.081130
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Parameters
    # terms : [{},{}]
    # variables : []

    terms = [{'files': 'foo', 'paths': 'path/to/file.txt'}]
    variables = []
    kwargs = []

    module = LookupModule()

    # Real Run
    module.run(terms, variables)

    # Mocked Run
    module.get_option = Mock()
    module.find_file_in_search_path = Mock()

    module.run(terms, variables)
    print('mocked')
    print(module.get_option.call_count, module.find_file_in_search_path.call_count)

    path = 'path/to/file.txt'
    file = 'foo'
    var_options = []
    subdir = 'files'
    ignore

# Generated at 2022-06-13 13:47:47.656312
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Test not implemented"


# Generated at 2022-06-13 13:47:58.244645
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subdir = 'files'
    base_paths = [os.path.normpath('/tmp/foo'), os.path.normpath('/tmp/bar')]
    base_files = ['file1', 'file2', 'file3', 'file4']

    # define a few test variables
    vars = dict(
        files1=base_files,
        files2=['file5'],
        files3=['file6', 'file7'],
        paths1=base_paths,
        paths2=['/tmp/baz'],
        paths3=[],
        terms=[],
        term1='terms',
        term2='/tmp/bar/file4',
    )

    # create a LookupModule instance
    lm = LookupModule()
    lm._subdir = subdir

    # create

# Generated at 2022-06-13 13:48:11.451189
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    actual = {
        'found': [],
        'raised': None,
    }

    args = [
        [
            {
                'files': ['first_found_local.yml'],
                'paths': ['test/test_lookup.data/'],
                'skip': True,
            },
            {'skip': False},
            'first_found_local.yml',
        ],
        [
            {
                'files': ['first_found_local.yml'],
                'paths': ['test/test_lookup.data/'],
                'skip': False,
            },
            {'skip': False},
            'first_found_local.yml',
        ],
    ]


# Generated at 2022-06-13 13:48:20.979785
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import unittest

    # NOTE: this is in case we want to add more tests.
    class LookupModuleTest(unittest.TestCase):
        pass

    # generic helpers
    vars_data = dict(
        ansible_env={'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'},
        ansible_distribution='Ubuntu',
        ansible_distribution_version='15.10',
        ansible_os_family='Debian',
        ansible_pkg_mgr='apt',
        ansible_architecture='x86_64',
        ansible_system='Linux',
        ansible_processor_count=4,
    )

# Generated at 2022-06-13 13:48:23.854370
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    print (lookup_module.run(['test'], {}))


# Generated at 2022-06-13 13:48:36.019160
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Import module to be tested
    from ansible.plugins.lookup import first_found

    # Create instance
    lookup_module = first_found.LookupModule()

    # 'terms' is the argument to method run
    # 'variables' is the argument to method run
    # 'kwargs' is the argument to method run

    # Test direct call
    if False:
        # create terms
        terms = [
            {'files': 'bar.txt', 'paths': '/tmp/john,/tmp/doe', 'skip': True},
            {'files': 'foo.txt', 'paths': '/tmp/john,/tmp/doe', 'skip': True},
        ]

        assert lookup_module.run(terms=terms, variables={}, **{'skip': True}) == []

    # Test call via lookup

# Generated at 2022-06-13 13:48:36.621373
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:49:10.547329
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict

    # Test no skip
    lookup = LookupModule()
    lookup.set_options(ImmutableDict({'skip': False}))
    try:
        lookup.run([], None)
        assert False, 'should fail'
    except AnsibleLookupError:
        pass

    # Test skip
    lookup = LookupModule()
    lookup.set_options(ImmutableDict({'skip': True}))
    assert lookup.run([], None) == []

    # Test option override file
    lookup = LookupModule()
    lookup.set_options(ImmutableDict({'skip': True, 'files': 'foo.txt'}))
    assert lookup.run([], None) == []

    # Test option override path
    lookup = LookupModule()

# Generated at 2022-06-13 13:49:20.560104
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_lookup = LookupModule()
    test_lookup._subdir = 'files'
    test_lookup.searchpath = [os.getcwd()]
    assert test_lookup.run(terms=[
        'test_data/test_file_1.conf',
        'test_data/test_file_2.conf',
        'test_data/test_file_3.conf',
    ], variables=dict(
        ansible_virtualization_type='kvm'
    )) == \
           [os.path.join(os.getcwd(), 'test_data/test_file_1.conf')]

    # Test searchpath
    test_lookup = LookupModule()
    test_lookup._subdir = 'files'

# Generated at 2022-06-13 13:49:31.933682
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def __mock_find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
        if fn == 'bar.txt':
            return 'bar.txt'
        else:
            return None

    # create object LookupModule
    lm = LookupModule()

    # get reference to _process_terms method
    pt = lm._process_terms

    def _mock_process_terms(terms, variables, kwargs):
        return pt(terms, variables, kwargs), True

    # assign _mock_process_terms to _process_terms
    lm._process_terms = _mock_process_terms

    # assign __mock_find_file_in_search_path to find_file_in_search_path
    lm.find_file_in_search

# Generated at 2022-06-13 13:49:37.679068
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # term string
    term1 = "file_1.txt"
    # term string with non default paths
    term2 = {'files': "file1.txt,file2.txt;foofile.txt", 'paths': '/home'}
    # term string with non default paths, files and option skip on
    term3 = {'files': "file1.txt,file2.txt;foofile.txt", 'paths': '/home', 'skip': True}
    # term string with non default paths, files and option skip on
    term4 = {'files': "file1.txt,file2.txt;foofile.txt", 'paths': "/home,/tmp", 'skip': True}

    # create lookup object
    lu = LookupModule()

# Generated at 2022-06-13 13:49:48.987984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # https://github.com/ansible/ansible/blob/stable-2.9/test/units/plugins/lookup/test_first_found.py#L15-L24
    lookup_plugin = LookupModule()

    # test without any files
    assert lookup_plugin.run(terms=['a', 'b'], variables=dict(), paths=['y', 'm']) == [], 'Should not return any files when no files are supplied'

    # test with path but no files
    assert lookup_plugin.run(terms=['a', 'b'], variables=dict(), paths=['y', 'm']) == [], 'Should not return any files when path is supplied but no files'

    # test with files but no paths

# Generated at 2022-06-13 13:49:50.450175
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule()


# Generated at 2022-06-13 13:49:52.621273
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    # TODO: write

# Generated at 2022-06-13 13:50:07.318750
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import imp
    import os
    import ansible
    from ansible.module_utils._text import to_text

    if sys.version_info[0] > 2:
        # TODO: this should be done in a better way,
        # there is no reason to disable issue warnings
        # and hide them with this module.
        imp.find_module('markupsafe')
        module_name = 'markupsafe'
    else:
        module_name = 'markupsafe.module_utils'

    # we need markupsafe to test the return value
    # as we cannot pass a dict to template
    # so we need to dig into the the markupsafe module
    # find the lookup module and patch it in
    module_path = imp.find_module(module_name)[1]

# Generated at 2022-06-13 13:50:19.693752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock class to avoid using the real AnsibleLookupError class
    class MockLookupError(Exception): pass

    # Mock ansible_virtualization_type, ansible_distribution and ansible_os_family
    class MockAnsibleVariables:
        def __getitem__(self, key):
            key = key[7:]  # Remove ansible_ prefix
            if key == "virtualization_type":
                return "virtualbox"
            elif key == "distribution":
                return "debian"
            elif key == "os_family":
                return "debian"
            return None

    # This test case covers the block of code starting at line 209
    def test_with_virtualbox_virtualization_type():
        mock_templar = TestAnsibleMockTemplar()


# Generated at 2022-06-13 13:50:27.390983
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    (isinstance(LookupModule('','').run(["foo","bar"], 'var'), list))
    (isinstance(LookupModule('','').run(["foo","bar"], 'var'), list))
    (isinstance(LookupModule('','').run([{"files":["foo","bar"],"paths":["/tmp"]}, "foo"], 'var'), list))

# Generated at 2022-06-13 13:51:15.477927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:51:21.198254
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Test without arguments
    lookup_plugin = LookupModule()
    variables = dict()
    results, skip = lookup_plugin.run([], variables)
    assert results == [], "Expected results to be an empty list"
    assert skip == False, "Expected skip to be False, got {} instead.".format(skip)

# Generated at 2022-06-13 13:51:30.135505
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _get_plugin():
        basedir = os.path.join(os.path.dirname(__file__), '..', 'lookup_plugins')
        return LookupModule.find_plugin(basedir, "first_found", '.', '.')

    # Call the run method without arguments - fail
    plugin = _get_plugin()
    assert(plugin.run([]) is False)

    # Call the run method with arguments
    plugin = _get_plugin()
    assert(type(plugin.run([{'files': 'foo', 'paths': '/tmp'}])) == list)

# Generated at 2022-06-13 13:51:30.801462
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:51:38.877173
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # you may want to test with custom classes and methods in this test
    # because this test is working in the class scope.
    cls = LookupModule()
    print('zzzz',cls.run)
    # e.g.
    #class MockVars:
        #pass
    #cls.set_options = MagicMock(return_value=MockVars)
    #cls.run('foo', 'bar', baz='plonk')

# vim: set expandtab ts=4 sw=4:

# Generated at 2022-06-13 13:51:47.301499
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create object of class LookupModule
    obj = LookupModule()
    # Fake object of class _PluginLoader to avoid exception
    obj._loader = object()

    # List of files
    files = [os.path.join(os.path.sep, 'var', 'tmp', 'file1'),
             os.path.join(os.path.sep, 'var', 'tmp', 'file2')]

    # Check function first
    # simulate file2 existing and file1 existing. Expected result is ['/var/tmp/file2']
    result = obj.run(files, None, paths=[os.path.join(os.path.sep, 'var', 'tmp')])
    assert result == [os.path.join(os.path.sep, 'var', 'tmp', 'file2')]
    # simulate file2

# Generated at 2022-06-13 13:52:00.561749
# Unit test for method run of class LookupModule