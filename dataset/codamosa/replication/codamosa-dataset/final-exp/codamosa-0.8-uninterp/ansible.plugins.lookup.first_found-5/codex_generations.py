

# Generated at 2022-06-13 13:42:09.030016
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm._subdir = 'files'
    # file is found
    terms = [
        {'files': 'foo', 'paths': ['/tmp']},
        {'files': 'foo', 'paths': []},
        {'files': 'foo'},
        'foo'
    ]
    for term in terms:
        os.system("touch /tmp/foo")
        assert lm.run(term, dict()) == ['/tmp/foo']
        os.system("rm /tmp/foo")

    # file is not found
    terms = [
        {'files': 'foo', 'paths': ['/tmp']},
        {'files': 'foo', 'paths': []},
        {'files': 'foo'},
        'foo'
    ]

# Generated at 2022-06-13 13:42:15.254943
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # initial setup
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    class Options(object):
        def __init__(self, task_vars=None, **kwargs):
            self.__dict__.update(kwargs)
            self.task_vars = task_vars
    class Connection(object):
        def __init__(self, play_context=None):
            self.play_context = play_context
    mock_loader = basic.AnsibleModule(
        argument_spec=dict(),
    )._loader

    # mocks

# Generated at 2022-06-13 13:42:28.659872
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.errors import AnsibleLookupError
    from .lookup_plugins.first_found import LookupModule
    from ansible.module_utils.six import PY3, PY2
    if PY2:
        from ansible.utils.unicode import to_bytes, to_unicode
    l_mod = LookupModule()
    terms = ['bar', {'files': 'foo'}]
    path = l_mod.run(terms, None)
    assert path == ['bar']
    l_mod.get_option('files')
    l_mod.get_option('paths')
    l_mod.set_options(var_options=None, direct='files=foo')
    l_mod.set_options(var_options=None, direct='files=foo')
    files = l

# Generated at 2022-06-13 13:42:37.268816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test using the setup for task-included tests for the with_first_found lookup
    import os
    import pytest
    from ansible.utils.path import makedirs_safe
    from ansible.errors import AnsibleLookupError
    import ansible.plugins.lookup

    lookup = ansible.plugins.lookup.LookupModule()
    lookup._subdir = "test_with_first_found"
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data', 'lookup_with_first_found')
    makedirs_safe(path)
    os.chdir(path)
    path = os.getcwd()

    # Data to make it easy to test various scenarios
    # Expected values from tests

# Generated at 2022-06-13 13:42:48.843450
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [{'paths': '/path/foo', 'files': 'filename'}, '/path/bar']
    variables = {}
    kwargs = {}
    lm = LookupModule()
    lm._subdir = 'files'
    lm._loader = {}
    lm._templar = {}
    setattr(lm._templar, 'template', lambda x: x)
    setattr(lm, 'find_file_in_search_path', lambda variables, subdir, fn, ignore_missing: fn)
    total_search, skip = lm._process_terms(terms, variables, kwargs)
    found_files = lm.run(terms, variables, **kwargs)

# Generated at 2022-06-13 13:42:57.912412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.plugins.lookup.first_found import LookupModule

    def myfind_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        return "/tmp/dir/fn"

    lookup = LookupModule()
    lookup._templar = None
    lookup.find_file_in_search_path = myfind_file_in_search_path
    lookup._subdir = 'files'

    # Test with string
    terms = ["test"]
    variables = None
    kwargs = {"files": "file1", "paths": "path1:path2"}

    ret = lookup.run(terms=terms, variables=variables, **kwargs)

# Generated at 2022-06-13 13:43:10.003244
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # case: no option, 1 file
    result = LookupModule().run(['myfile.yaml'], dict())
    assert result == ['myfile.yaml']

    # case: ok, 1 file, 1 path, skip=True
    result = LookupModule().run([{'files': ['myfile.yaml'], 'paths': ['.'], 'skip': True,}], dict())
    assert result == []

    # case: ok, 1 file, 1 path, skip=False
    result = LookupModule().run([{'files': ['myfile.yaml'], 'paths': ['.'], 'skip': False,}], dict())
    assert result == ['myfile.yaml']

    # case: ok, 1 file, 1 path, skip=True

# Generated at 2022-06-13 13:43:15.466542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_options(var_options={"a": "b"}, direct={"a": "ignored", "b": "c", "d": "e"})
    assert lookup.get_option('a') == 'b'
    assert lookup.get_option('b') == 'c'
    assert lookup.get_option('d') == 'e'
    with pytest.raises(AnsibleLookupError):
        lookup.get_option('not_defined')
    lookup.set_options(var_options={"a": "b"}, direct={"a": "c"})
    assert lookup.get_option('a') == 'c'
    assert lookup.get_option('b') == 'c'
    assert lookup.get_option('d') == 'e'


# Generated at 2022-06-13 13:43:26.437224
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test 'files' in terms
    assert LookupModule().run(terms=['a.txt', 'b.txt', 'c.txt'], variables={}) == ['a.txt']

    # test 'files' in kwargs
    assert LookupModule().run(terms=['a.txt', 'b.txt', 'c.txt'], variables={}, files=['a.txt', 'b.txt', 'c.txt']) == ['a.txt']

    # test 'filelist' in terms dict
    assert LookupModule().run(terms=[{'files': ['a.txt', 'b.txt', 'c.txt']}, {'files': ['d.txt', 'e.txt', 'f.txt']}], variables={}) == ['a.txt']

    # test 'paths' in terms dict

# Generated at 2022-06-13 13:43:35.481551
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given name of file to search, 
    # when the file was found, 
    # the the correct message is returned
    file_found = "test-file"
    obj = LookupModule()
    obj.set_options({'files': file_found})
    with patch('ansible.plugins.lookup.first_found.LookupModule.find_file_in_search_path', return_value=file_found):
        result = obj.run(['test-file'], {})
        assert result == [file_found]


# Generated at 2022-06-13 13:43:49.899131
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:43:56.680071
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    filename = 'file1'
    paths = ['play/roles/role1/files', 'play/files']

    kwargs = {
        'files': filename,
        'paths': paths,
    }

    lm = LookupModule()
    total_search, skip = lm._process_terms(kwargs, None, kwargs)

    for term in total_search:
        assert term.startswith('play/')
    assert skip == False


# Generated at 2022-06-13 13:44:07.759901
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # See also https://www.python-course.eu/python3_properties.php
    class Search_Path:
        _searchpath = {}

    # Set search path for unit testing
    search_path = Search_Path()
    search_path._searchpath = {
        'files': [
            {'path': './files', 'user': None, 'when': True, 'name': 'files', 'conf_token': None},
            {'path': 'files', 'user': None, 'when': True, 'name': 'files', 'conf_token': None}
        ]
    }

    lookup = LookupModule()
    lookup._loader = None
    lookup._templar = None
    lookup._searchpath = search_path._searchpath
    lookup._file_find_can_use_sudo = False

    # Test 1
   

# Generated at 2022-06-13 13:44:12.175128
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subdir = getattr(LookupModule, '_subdir', 'files')
    assert subdir == 'files'
    # test: to be completed
    pass



# Generated at 2022-06-13 13:44:19.262974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    def test(result, msg):
        # test function to raise error if test fails.
        if not result:
            raise AssertionError(msg)
    # unit test for first_found lookup
    class MockParser(object):
        def __init__(self):
            self.cur_basedir = '/etc'
            self.basedirs = ['/etc', '/var/lib/ansible']
        def expand_path(self, path):
            """Return the absolute path name expanded to remove symbolic links and relative path references."""
            return path
        def get_basedir(self):
            return self.cur_basedir
    class MockTemplar(object):
        def template(self, template):
            return template
    # test using inline configuration

# Generated at 2022-06-13 13:44:26.890499
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup
    import os
    import tempfile
    tmpdir = tempfile.mkdtemp()
    file1 = os.path.join(tmpdir, 'file1')
    file2 = os.path.join(tmpdir, 'file2')
    os.mkdir(os.path.dirname(file1))
    os.mkdir(os.path.dirname(file2))
    open(file1, 'w').close()
    open(file2, 'w').close()
    test1 = [file1, file2]
    test2 = [file2, file1]
    test3 = [file1, 'no_such_file']
    test4 = ['no_such_file', file1]
    all_tests = [test1, test2, test3, test4]


# Generated at 2022-06-13 13:44:29.715934
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    l = LookupModule()
    l.set_options({'skip': True})
    assert l.run(['files'], {}, skip=True) == []

# Generated at 2022-06-13 13:44:38.654010
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # mock the loader
    mock_loader = """
    {
        "_loader_obj": "",
        "_entries": [],
        "_basedir": "",
        "_all_files": {
            "one.yml": [],
            "two.yml": [],
            "three.yml": []
        },
        "path_sep": ":",
        "searchpath": [],
        "basedir": ""
    }
    """

    # mock templar
    mock_templar_result = "result"
    class MockTemplar(object):
        def template(self, data):
            return mock_templar_result

    # mock variable
    mock_var = {
        "_results": []
    }

    # init LookupModule
    lm = LookupModule()



# Generated at 2022-06-13 13:44:48.766331
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create instance of LookupModule with all default parameters
    lookup_module = LookupModule()

    # set value of private property _subdir
    lookup_module._subdir = 'files'

    try:
        # call method run of class LookupModule
        lookup_module.run([{'skip': True, 'paths': ['files'], 'files': []}])
    except AnsibleLookupError as e:
        assert "No file was found when using first_found" in str(e)

    # create test files
    from tempfile import mkstemp
    from os.path import join
    import os

    # create absolute path to temporary directory
    tmp_dir = os.path.dirname(__file__)

    # create absolute path to test files
    tmp_dir = join(tmp_dir, 'files')

    # create

# Generated at 2022-06-13 13:45:00.179746
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        'foo',
        {'files': 'foo.yml', 'paths': 'this_path'},
        {'files': 'foo.yml', 'paths': 'that_path'},
        'bar',
        {'files': 'bar.yml', 'paths': 'another_path'},
        {'files': 'bar.yml'},
    ]
    variables = {}
    lm = LookupModule()
    lm._subdir = 'test_subdir'

    # NOTE: these mock_returns are not quite right because they do not
    # reflect if the 'file' has been found in any of the other locations

# Generated at 2022-06-13 13:45:16.118826
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager


# Generated at 2022-06-13 13:45:16.932935
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:45:29.119609
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockTemplar:
        def __init__(self, result):
            self.result = result

        def template(self, fn):
            return self.result

    class MockModule:
        def __init__(self, params, kwargs):
            self.params = params
            self.kwargs = kwargs

    mock_templar = MockTemplar("test_file")
    lm = LookupModule(loader=None, templar=mock_templar, basedir=None)
    lm._subdir = "test_subdir"
    lm.find_file_in_search_path = lambda x, y, z, **kwargs: "test_file"

    # When string is provided, kwargs must be used to pass options
    terms = "test_term"

# Generated at 2022-06-13 13:45:38.969593
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Construct a LookupModule instance to test with
    lookup_module = LookupModule()
    lookup_module._templar = lookup_module.loader.load_basedir(os.path.dirname(__file__))

    # The find_file_in_search_path method uses _loader_for_path.
    # Patch the _loader_for_path method to always return the same object for a given path
    # NOTE: This may no longer be required as of Ansible 2.6
    from ansible.plugins.loader import _loader_for_path

    def _fake_loader_for_path(path):
        return lookup_module

    lookup_module._loader_for_path = _fake_loader_for_path

    # Construct the test inputs
    terms = ["test_LookupModule_run", "no such file"]
    search

# Generated at 2022-06-13 13:45:50.842165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader

    lookup = LookupModule()
    loader = DataLoader()
    terms = [
        {
            'files': "a,c",
            'paths': "/tmp",
        },
        {
            'files': "b",
            'paths': "/tmp",
            'skip': True
        },
        {
            'files': "a",
            'paths': "/tmp",
        },
        {
            'files': "c",
            'paths': "/tmp",
        }
    ]
    # TODO: test this with a fake file system

# Generated at 2022-06-13 13:46:00.160534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.module_utils._text import to_bytes
    from units.mock.loader import DictDataLoader

    fake_loader = DictDataLoader({
        'myfile.txt': '',
        'testing': '',
        'home/testuser/somefile.txt': '',
        'home/testuser/testdir/': '',
        'home2/testuser/otherfile.txt': '',
    })

    fake_inventory = InventoryManager(loader=fake_loader, sources='localhost,')
    fake_vars = VariableManager()


# Generated at 2022-06-13 13:46:12.872646
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    t = {"params": {"files": ["foo"], "paths": []}, "cache": None, "cacheable": False, "playbook": None, "play": None, "task": {"name": "first_found_run"}, "file_name": "/usr/share/ansible_plugins/lookup_plugins/first_found.py", "var_name": "path", "all_vars": {}, "lookup_type": "first_found", "language": "python", "all_results": {}, "all_items": []}

    terms = [t, t]


# Generated at 2022-06-13 13:46:21.775183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    sut = LookupModule()

    terms = [
        {
            'files': 'foo,bar',
            'paths': '.'
        }
    ]
    variables = {}
    kwargs = {}
    sut._find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=True: fn
    ret = sut.run(terms, variables, **kwargs)
    assert ret == ['foo', 'bar']

    terms = [
        {
            'files': 'foo,bar',
            'paths': '.',
            'skip': True
        }
    ]
    variables = {}
    kwargs = {}
    sut._find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=True: None
    ret = sut.run

# Generated at 2022-06-13 13:46:29.254840
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # No files found
    terms = [
        'path/does/not/exist/file.txt',
        'file.txt'
    ]

    with pytest.raises(AnsibleLookupError):
        lookup.run(terms)

    # File found
    terms = [
        'lookup_plugins/__init__.py',
        'lookup_plugins/__init__.py'
    ]
    assert lookup.run(terms) == ['lookup_plugins/__init__.py']

# Generated at 2022-06-13 13:46:36.280766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Constructor
    lookup_module = LookupModule()

    # Mocking
    # Mock class LookupBase
    lookup_base_class = lookup_module.get_base_class('LookupBase')
    lookup_base_class.find_file_in_search_path = lambda x, y, z, **kw: '/path/to/file'

    # Mock class Templar
    templar_class = lookup_module.get_base_class('Templar')
    templar_class.template = lambda x: x

    # Testing
    # file in files directory
    result = lookup_module.run(['foo', 'bar'], {}, files=['file.conf'])
    assert result == ['/path/to/file'], "Fail: file found in files directory"

    # file in given path
    result = lookup

# Generated at 2022-06-13 13:46:43.017989
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:46:44.329317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: add tests
    pass

# Generated at 2022-06-13 13:46:50.575715
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test: Total search list is populated with file names
    lookup_module.run(
        terms=["a",
               {"files": ["a", "b"], "paths": ["/path/to"]},
               {"files": "a, x, y, z"},
               {"paths": "/path/to:/path/to/other"},
               {"files": "a, x, y, z", "paths": "/path/to:/path/to/other"},
               {"files": "a, x, y, z", "paths": ["/path/to", "/path/to/other"]},
               ["a"]],
        variables={})
    assert len(lookup_module._terms) == 4

# Generated at 2022-06-13 13:46:54.656802
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    filenames, skip = LookupModule._process_terms([], {}, {'skip': False})
    assert filenames == [], 'Expected empty list as first parameter'
    assert skip == False, 'Expected False as second parameter'

# Generated at 2022-06-13 13:47:05.163830
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._loader = None
    lookup_module._templar = None
    lookup_module._subdir = None
    variables = {}

    paths = ['file1.txt', 'file2.txt']
    terms = ['file1.txt', 'file2.txt']
    total_search, skip = lookup_module._process_terms(terms, variables, {})
    assert total_search == paths

    # test dict terminology
    terms = [{'files': 'file1.txt', 'paths': '/path1', 'skip': True}, {'files': 'file2.txt', 'paths': '/path2'}, 'file3.txt']

# Generated at 2022-06-13 13:47:15.721587
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    For some reason the dictionary key 'files' does not seem to have the effect
    that one would have expected. The key 'paths' however does not have any
    apparent issues.
    """
    lookup_module = LookupModule()
    settings = {}
    lookup_module.set_options(direct=settings)
    terms = ['one', {'files': 'two', 'paths': 'three'}, ['four', 'five']]

    total_search, skip = lookup_module._process_terms(terms, settings, settings)

    assert skip is False
    assert total_search == ['one', 'four', 'five']

    # The key 'files' is not added to total_search
    assert 'two' not in total_search
    # The key 'paths' is added to total_search
    assert 'three' in total_

# Generated at 2022-06-13 13:47:26.005281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar

    from ansible.playbook.play_context import PlayContext
    # create the basic test objects ansible uses
    templar = Templar(loader=None, variables={})
    play_context = PlayContext()

    # create an instance of the lookup plugin
    lookup_plugin = LookupModule()
    # inject the resulting template class for tests
    lookup_plugin._templar = templar

    # prepare mock data
    terms = [u'read me!', u'configuration file', AnsibleUnicode(u'hello_world')]

# Generated at 2022-06-13 13:47:35.345666
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        {'files': 'somefile', 'paths': '/some/path'},
        'somefile',
        {'files': 'somefile', 'paths': '/some/other/path'},
        ['somefile', 'someotherfile', 'athirdfile'],
    ]

    expected = [
        '/some/path/somefile',
        'somefile',
        '/some/other/path/somefile',
        'somefile',
    ]

    # same as LookupModule._process_terms() but return values instead
    total_search = []
    skip = False
    for term in terms:
        if isinstance(term, str):
            filelist = [term]
            pathlist = []
        else:
            files = term.get('files', [])

# Generated at 2022-06-13 13:47:45.553206
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lkp = LookupModule()
    # test empty input for case where no files found
    assert [] == lkp.run([], {})
    # test empty input for case where no files found
    assert [] == lkp.run([], {}, skip=True)
    # test non-existent file
    assert [] == lkp.run(['not_exist.txt'], {})
    # test non-existent file
    assert [] == lkp.run(['not_exist.txt'], {}, skip=True)
    # test existing file
    assert [] != lkp.run(['/etc/passwd'], {})

# Generated at 2022-06-13 13:47:50.600971
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given a lookup object
    lookup = LookupModule()
    # When I run the method run with valid inputs
    result = lookup.run(['test_file.txt'])
    # Then I should get a valid result
    assert result == 'test_file.txt'

# Generated at 2022-06-13 13:48:05.266576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    # run method of class LookupModule
    assert(LookupModule.run)

# Generated at 2022-06-13 13:48:16.131199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # A few test files
    test_files = {
        'findme.file': 'findme.file',
        'findme.alternative': 'findme.alternative',
        os.path.join('path', 'findme.file'): 'findme.file',
        os.path.join('path', 'findme.alternative'): 'findme.alternative',
        os.path.join('path', 'to', 'findme.file'): 'findme.file',
        os.path.join('path', 'to', 'findme.alternative'): 'findme.alternative',
    }

# Generated at 2022-06-13 13:48:23.931432
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # simple unit test for testing lookup
    import ansible.plugins.lookup.first_found as lookup_plugin
    class LookupModule(lookup_plugin.LookupModule):
        def __init__(self, basedir=None, **kwargs):
            self.basedir = basedir
            self._templar = Templar(variables={})

        def find_file_in_search_path(self, variables, path, file):
            if file == 'file1' and path == ['/tmp/cache/some/path']:
                return '/tmp/cache/some/path/file1'
            return None

    # Test1: search /tmp/cache/some/path/file1
    lu = LookupModule(basedir={})
    files = ['/tmp/cache/some/path/file1']
    result = l

# Generated at 2022-06-13 13:48:36.065189
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: For more details look at ./tests/unit/plugins/lookup/test_first_found.py

    lookup = LookupModule()

    # Test with empty list of terms
    terms = []
    variables = {}
    assert lookup.run(terms, variables) == [], "Empty list of terms source should be equal []"

    # Test with list of file names that do not exist
    terms = ['fake_file.txt']
    variables = {}
    assert lookup.run(terms, variables) == [], "Terms source should be equal []"

    # Test with valid list of file names
    terms = ['file1.txt']
    variables = {}
    assert lookup.run(terms, variables) == ['file1.txt'], "Terms source should be equal ['file1.txt']"

    # Test with list of valid and invalid file

# Generated at 2022-06-13 13:48:43.794326
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    l = LookupModule()

    l._subdir = 'files'
    # search a directory not existing in ansible modules search path.
    path = l.run([{'files': 'abc.yaml', 'paths': '/var/tmp'}], variable_manager)
    assert len(path) == 0

# Generated at 2022-06-13 13:48:52.041440
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    # TODO: add test case for missing skip variable
    assert l.run(['/path/to/file.yml'], {}, skip=True) == []
    assert l.run(['/path/to/file.yml', '/path/to/file2.yml'], {}, skip=True) == []
    assert l.run(['/path/to/file.yml', '/path/to/file2.yml', '/path/to/file3.yml'], {}, skip=True) == []

# Generated at 2022-06-13 13:49:02.961874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    fn = "./" + os.path.join(os.path.dirname(__file__), '..', '..', 'lookup_plugins', 'first_found.py')
    lm._templar = DummyMock()
    DummyMock.template = lambda self, x: x
    terms = ['../../lookup_plugins/first_found.py', 'files/test.yml', {'files': 'test.yml', 'paths': './'}]
    results = lm.run(terms=terms, variables=dict())
    assert results == [fn] 

# Dummy class for unit testing templar

# Generated at 2022-06-13 13:49:10.071543
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variable_manager = {
        # variable manager: values per host
        "hostvars": {
            "host1": {
                "variable1": "value1",
                "variable2": "value2",
            },
            "host2": {
                "variable2": "value2_2"
            }
        },
    }
    hostname = 'host1'
    variables = variable_manager["hostvars"][hostname]
    terms = ["variable1", "variable2"]
    kwargs = {
        "paths": "a/path",
        "files": "a/file",
        "skip": False,
    }
    instance = LookupModule()
    result = instance.run(terms, variables, **kwargs)
    assert len(result) == 1

# Generated at 2022-06-13 13:49:25.732857
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils._text import to_bytes
    import pytest
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves.builtins import range

    LookupModule.run_annotated = run_annotated

    # 2nd branch of 'if' in run()
    # 1st branch of 'elif' in run()
    # test with a dict
    terms = dict(files='file1')
    vars = dict(files=['/file0'])
    ret = LookupModule.run_annotated(terms, vars)
    assert ret.return_value == ['/file0']

    # 1st branch of 'if' in run()
    # test with a str

# Generated at 2022-06-13 13:49:34.791766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    from ansible.plugins.lookup.first_found import LookupModule
    terms = [{'files': 'fileA,fileB', 'paths': 'pathA,pathB', 'skip': True}, {'files': 'fileC,fileD', 'paths': 'pathC,pathD', 'skip': False}]
    variables = {}
    lookup_module = LookupModule()
    lookup_module.set_loader = 'loader'
    lookup_module.set_basedir = './tests/unit/outputs/lookup_plugins/test_first_found'

    # Act
    total_search, skip = lookup_module._process_terms(terms, variables, {})
    result = lookup_module.run(terms, variables)

    # Assert

# Generated at 2022-06-13 13:49:59.029054
# Unit test for method run of class LookupModule
def test_LookupModule_run():

  # TODO: implement tests
  assert False

# Generated at 2022-06-13 13:50:09.334201
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    arg_specs = {
        'terms': {
            'args': (
                'term1',
                'term2',
                'term3',
            ),
            'kwargs': {},
        },
        'variables': {},
        'kwargs': {},
    }


# Generated at 2022-06-13 13:50:20.255471
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: this works but tests too much, need to rewrite
    terms = [{'files': '/path/to/foo.txt', 'paths': '/path/to/rem/dir'}, 'bar.txt']
    variables = {}
    kwargs = {}
    module = LookupModule()
    total_search, skip = module._process_terms(terms, variables, kwargs)

    assert terms == [{'files': '/path/to/foo.txt', 'paths': '/path/to/rem/dir'}, 'bar.txt']
    assert variables == {}
    assert kwargs == {}
    assert total_search == ['/path/to/rem/dir/foo.txt', 'bar.txt']
    assert skip is False


# Generated at 2022-06-13 13:50:32.397436
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    from ansible.utils.listify import listify_lookup_plugin_terms

    # Create class for unit testing
    class Options:
        def __init__(self, verbosity=0, connection=None, remote_user=None,
                     private_key_file=None, ssh_common_args=None, ssh_extra_args=None,
                     sftp_extra_args=None, scp_extra_args=None, become=None,
                     become_method=None, become_user=None, verbosity=None, check=False,
                     diff=False):
            self.verbosity = verbosity
            self.connection = connection
            self.remote_user = remote_user
            self.private_key_file = private_key_file

# Generated at 2022-06-13 13:50:43.161593
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Declare test variables
    terms1 = 'foo'
    terms2 = 'bar'
    terms3 = 'foo,bar'
    terms4 = 'foo:bar'
    terms5 = ['foo', 'bar']
    terms6 = { 'foo': 'bar', 'x': 'y' }

    # Define test class
    class TestLookupModule(LookupModule):
        def _process_terms(self, terms, variables, kwargs):
            return terms, False


    # Instantiate test class
    class1 = TestLookupModule()

    # Test run method for string input
    results1 = class1.run(terms1)
    assert results1 == ['foo']
    results2 = class1.run(terms2)
    assert results2 == ['bar']

    # Test run method for string input with comma
   

# Generated at 2022-06-13 13:50:50.719006
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._find_file = lambda variables, dirs, f, ignore_missing: f
    lookup._templar = None
    lookup._templar.template = lambda s: s
    lookup._subdir = 'files'
    result = lookup.run(['fake.yml'])
    assert result == ['fake.yml']
    result = lookup.run(['fake.yml'], skip=True)
    assert result == []

# Generated at 2022-06-13 13:50:57.653688
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # params for #run:  terms, variables, **kwargs
    test_module = LookupModule()

    # no return / error
    params = [('not_found', {'skvidal': 'skvidal'}, {})]
    assert [] == test_module.run(*params)

    # found one file
    params = [('skvidal', {'skvidal': 'skvidal'}, {})]
    assert ['skvidal'] == test_module.run(*params)

    # overide default
    params = [('skvidal', {'skvidal': 'skvidal'}, {'skip': True})]
    assert ['skvidal'] == test_module.run(*params)

    # not found / error

# Generated at 2022-06-13 13:51:10.844031
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ LookupModule: test methods run """
    l = LookupModule()
    l._subdir = 'files'

    # Create dict with some files in the paths
    files = {
        '/tmp/file0.txt': 'file0.txt',
        '/tmp/file1.txt': 'file1.txt',
        '/tmp/file2.txt': 'file2.txt',
        '/tmp/file3.txt': 'file3.txt',
        '/tmp/file4.txt': 'file4.txt',
    }
    for file_name, content in files.items():
        with open(file_name, 'w') as fd:
            fd.write(content)

    #
    # Test without arguments.
    #

# Generated at 2022-06-13 13:51:22.402330
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize a LookupModule instance.
    lookup_plugin = LookupModule()

    # Create an iterator, which will return a mock inventory for all hosts.
    def inventory_iterator(host_list):
        inventory = dict(all=dict(children=dict()), _meta=dict(hostvars=dict()))
        for host in host_list:
            inventory['all']['children'][host] = dict(hosts=dict())
            inventory['_meta']['hostvars'][host] = dict()
        return inventory.items()

    # Mock the templar object, it won't be used during this test.
    lookup_plugin._loader = type('', (object,), dict(get_basedir=lambda self: '.'))()

# Generated at 2022-06-13 13:51:33.093629
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # import module
    import ansible.plugins.lookup.first_found

    # create lookup module
    module = ansible.plugins.lookup.first_found.LookupModule()

    # create valid options
    options = dict()
    options['skip'] = False
    options['paths'] = ['.']

    # create valid terms
    terms = ['test.txt']

    # create fake variables
    variables = dict()
    variables['playbook_dir'] = 'data/playbooks'
    variables['play_dir'] = 'data/playbooks/play1'

    # run test
    result = module.run(terms=terms, variables=variables, **options)

    # test result, should be an empty list
    assert result == ['data/playbooks/play1/test.txt']