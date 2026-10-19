

# Generated at 2022-06-13 13:41:59.914311
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # given
    lookup_module = LookupModule()

    # when
    result = lookup_module.run([{'files': '', 'paths': ''}])

    # then
    assert result == []

# Generated at 2022-06-13 13:42:12.025738
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test _process_terms
    terms = [
        'foo',
        {'files': 'bar.py', 'paths': 'path1:path2:/path'},
        ['file1', 'file2']
    ]
    variables = {'ansible_foo': 'bar'}
    kwargs = {}
    test_obj = LookupModule()
    return_value, skip = test_obj._process_terms(terms, variables, kwargs)
    assert return_value == ['foo', 'bar.py', 'path1/bar.py', 'path2/bar.py', '/path/bar.py', 'file1', 'file2']
    assert skip is False

    # Test _process_terms --> with skip

# Generated at 2022-06-13 13:42:26.261392
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init the class and run the module
    # test cases TODO:
    # - no options
    # - no files, no patterns
    # - files but no paths
    # - paths but no files
    # - files and paths
    # - extra basic options (only skip)
    # - test with given relative dir
    # - have a test with search pathes in both lists and dict
    # - have a test with files in both lists and dict
    # - have a test with dict, dict and list, and list, all given in options
    # - using a dict for options and setting same option many times
    # - all the things above with 'errors' set to 'ignore'

    # init with one pattern
    lm = LookupModule()
    # test with one pattern
    #raise Exception("TODO: missing test case")
    # init

# Generated at 2022-06-13 13:42:36.023710
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock module
    module = AnsibleModule(argument_spec={
        'terms': {'type': 'list', 'elements': 'str'},
        'variables': {'type': 'dict'},
    })

    lookup_obj = LookupModule()

    # Mock require_one_of as it is not necessary to test in this unit
    lookup_obj.require_one_of = Mock()

    # Run the code to be tested
    terms = [
        "first_file.txt",
        {'files': "second_file.txt"},
        ["third_file.txt", "fourth_file.txt"],
        {'paths': '/var', 'files': ['fifth_file.txt', 'sixth_file.txt']}
    ]
    variables = {'ansible_facts': {}}
    result = lookup_

# Generated at 2022-06-13 13:42:46.935926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock the lookup module
    o_instance = LookupModule()
    o_instance.run = LookupModule.run

    # Mock the Templar class
    o_templar = object()

    # Mock the find_file_in_search_path() function
    o_export = object()

    o_export.files = ['files/file1.txt', 'files/file2.txt']
    o_export.file = None
    o_export.paths = None
    o_export.path = None
    o_export.skip = None

    # Mock the env export object name
    o_module_utils_module_name = 'ansible.module_utils.module_name'

    # Mock the ansible_module_utils.module_name env
    import sys

# Generated at 2022-06-13 13:42:56.991185
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: this only tests a few basic cases and will be improved in the future

    l = LookupModule()
    l._templar = DummyTemplar()

    # use kwargs
    result = l.run(['abc', '123'], {}, files=['foo', 'bar', 'baz'], paths=['/tmp/1', '/tmp/2', '/tmp/3'])
    assert result == ['/tmp/1/foo']

    # use dict term
    result = l.run([{'files': ['foo', 'bar', 'baz'], 'paths': ['/tmp/a', '/tmp/b', '/tmp/c']}], {})
    assert result == ['/tmp/a/foo']

    # use nested dict and list term

# Generated at 2022-06-13 13:43:01.434664
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = LookupModule.run(terms=terms, variables=variables, task_vars=task_vars, **self.options)
    assert len(terms) == 1
    assert terms[0] == '/path/to/foo.txt'

# Generated at 2022-06-13 13:43:12.217643
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a mock jinja environment
    from jinja2 import Environment
    import jinja2

    templates = {
        'file1.conf': ' first file',
        'file2.conf': ' second file',
        'file3.conf': ' third file',
    }

    def mock_get_template(name):
        class DummyTemplate:
            def render(self, *args, **kwargs):
                return templates[name]
        return DummyTemplate()

    def mock_list_templates():
        return sorted(templates.keys())

    env = Environment(loader=None)
    env.get_template = mock_get_template
    env.list_templates = mock_list_templates

    # create a mock templar
    from ansible.template import Templar

# Generated at 2022-06-13 13:43:23.637401
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # prepare templar
    class FakeTemplar:
        def __init__(self):
            return

        def template(self, filename):
            return filename

    # prepare variables
    class FakeVariables:
        def __init__(self):
            def get(self):
                return 'files'

    variables = FakeVariables()

    lookup = LookupModule()
    lookup._templar = FakeTemplar()

    # no files no paths
    results, _ = lookup._process_terms([], variables, {})
    assert results == []

    # files
    results, _ = lookup._process_terms(['file1', 'file2'], variables, {})
    assert results == ['file1', 'file2']

    # files, in a dictionary
    # for now this is supported.
    results, _ = lookup._

# Generated at 2022-06-13 13:43:36.218116
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # NOTE: needs to be set for the templar to use
    lookup._templar = None
    # NOTE: needs to be set for the templar to use
    lookup._loader = None

    # test proper usage
    total_search, skip = lookup._process_terms(
        ['first', 'second', dict(files=['three']), dict(files=['five'], paths=['foo'])],
        dict(first='first', second='second'),
        dict(files=['first', 'second'], skip=True))
    assert (total_search) == ['first', 'second', 'three', 'foo/five']
    assert (skip) is True

    # test no files give

# Generated at 2022-06-13 13:43:47.920090
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    os.environ['HOME'] = "/tmp"
    lookup = LookupModule()
    # Stub _templar class -> template() returns the input
    lookup._templar = lambda: None
    lookup._templar.template = lambda a: a
    # Stub find_file_in_search_path -> returns a file in a search path
    lookup.find_file_in_search_path = lambda a,b,c,d: "/etc/resolv.conf"
    # Stub get_option -> returns an option
    lookup.get_option = lambda a: None
    lookup.get_option.get = lambda a,b: None
    # Stub set_options to set _options for a lookup.
    lookup._options = None

# Generated at 2022-06-13 13:43:58.440889
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    lu = LookupModule()

    # Prepare test data
    os.makedirs('/tmp/ansible_test/search_path/sub')
    os.makedirs('/tmp/ansible_test/search_path/sub1')
    os.makedirs('/tmp/ansible_test/search_path2')
    with open('/tmp/ansible_test/search_path/foo', 'w+') as fo:
        fo.write('foo')
    with open('/tmp/ansible_test/search_path/sub/foo', 'w+') as fo:
        fo.write('foo')
    with open('/tmp/ansible_test/search_path/sub1/foo', 'w+') as fo:
        fo.write('foo')

# Generated at 2022-06-13 13:44:08.765605
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a mock class for an AnsibleModule that has the needed base class
    # attributes for the run method of the LookupModule class
    class AnsibleModuleMock(object):
        class ModuleFailException(Exception):
            pass

        class Parameters(object):
            def __init__(self, path):
                self._path = path

            def __contains__(self, path):
                return path in self._path

            def get(self, path):
                return self._path[path] if path in self._path else None

        class BaseFileSearch(object):
            def __init__(self, templar, file_name, paths, *args):
                self._templar = templar
                self._file_name = file_name
                self._paths = paths


# Generated at 2022-06-13 13:44:20.209989
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: during refactor noticed that the 'using a dict' as term
    # is designed to only work with 'one' otherwise inconsistencies will appear.
    # E.g.
    #  - skip: True
    #    files: file1.txt
    #  - files: file2.txt
    #    skip: False
    # will only look in files/ for file2.txt and will not skip if not found.
    # This is because the skip here is ignored as it is at first option/entry.

    # ALSO is the only method used but not tested

    pass

# Generated at 2022-06-13 13:44:32.400640
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    def _force_run(args, vars):
        options = LookupModule.run_setup(**args)
        lookup = LookupModule()
        return lookup.run_with_options(options, vars)

    base = os.path.dirname(__file__)

    # Basic test to check function is working
    assert _force_run({'files': 'files/file', 'paths': '.'}, {}) == [os.path.join(base, 'files/file')]

    # Test list of files and non-existent file
    assert _force_run({'files': ['files/file', 'file'], 'paths': ['.', '..']}, {}) == []

    # Test list of paths and non-existent file

# Generated at 2022-06-13 13:44:37.768836
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test LookupModule._split_on()
    # Test 1:
    terms = []
    spliters = [',', ';']
    LookupModule._split_on(terms, spliters)
    # Test 2:
    terms = ['foo', 'bar']
    terms = LookupModule._split_on(terms, spliters)
    assert(terms == ['foo', 'bar'])
    # Test 3:
    terms = 'baz'
    terms = LookupModule._split_on(terms, spliters)
    assert(terms == ['baz'])
    # Test 4:
    terms = {'files': 'foo', 'paths': 'bar'}
    terms = LookupModule._split_on(terms, spliters)
    assert(terms == ['foo', 'bar'])
    # Test 5:
   

# Generated at 2022-06-13 13:44:48.505151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup for test
    lookup = LookupModule()
    lookup._templar = None
    lookup._subdir = 'files'
    variables = {}


# Generated at 2022-06-13 13:45:00.057290
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Patch AnsibleLookupError exception
    def test_exception(parameter):
        raise AnsibleLookupError(parameter)

    LookupModule.AnsibleLookupError = test_exception

    # This will fail on first_found lookup, and give a message that should be processed
    # by test_exception function
    lookup = LookupModule()

    # When the first parameter is invalid, an AnsibleLookupError (programmed by us) is raised
    with pytest.raises(AnsibleLookupError) as exception_info:
        lookup.run(1, 2)

    # Check that the correct error message is raised
    assert str(exception_info.value) == "Invalid term supplied, can handle string, mapping or list of strings but got: <class 'int'> for 1"

    # When the first parameter is a

# Generated at 2022-06-13 13:45:14.186139
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    m = LookupModule()

    # call a method which sets internal attr _subdir
    m.find_file_in_search_path({}, 'files', None)  # set _subdir to 'files'

    # test_basic
    r = m.run([{
        'paths': '/etc/',
        'files': 'hosts'
    }])
    assert r == ['/etc/hosts']

    # test_no_paths
    r = m.run([{
        'files': 'hosts'
    }])
    assert r == ['hosts']

    # test_single_file
    r = m.run(['hosts'])
    assert r == ['hosts']

    # test_simple_list

# Generated at 2022-06-13 13:45:16.025795
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: start writing unit tests for this
    raise Exception("Not implemented")

# Generated at 2022-06-13 13:45:31.496159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.utils.pycompat
    assert ansible.utils.pycompat.PY3

    mylookup = LookupModule()
    terms = [
        ['vars/redhat.yml'],
        {'files': ['some/path/some.file', 'other/path/other.file']},
        {'files': 'some/path/some.file', 'paths': ['other/path']},
        {'files': ['some/path/some.file'], 'paths': ['other/path', 'yet/another/path']},
        {'files': ['some/path/some.file'], 'paths': ['other/path'], 'skip': True},
    ]


# Generated at 2022-06-13 13:45:40.161002
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # first no path or file list
    lookup = LookupModule()
    lookup._subdir = 'files'
    result = lookup.run(terms=['foo', 'bar'], variables={})
    assert result == [u'foo', u'bar']

    # what if none of the paths exist
    lookup = LookupModule()
    lookup._subdir = 'files'
    result = lookup.run(terms=[{'files': 'foo,bar', 'paths': 'baz,doo'}], variables={})
    assert result == ['baz/foo', 'doo/foo', 'baz/bar', 'doo/bar']

    # what if no path
    lookup = LookupModule()
    lookup._subdir = 'files'

# Generated at 2022-06-13 13:45:51.674171
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mod = LookupModule()

    terms = [
        {'files': 'test_file_1.txt,test_file_2.txt', 'paths': 'tmp/test/1,tmp/test/2'},
        {'files': 'test_file_3.txt', 'paths': 'tmp/test/3'},
        {'files': 'test_file_4.txt'}
    ]
    variables = {"inventory_hostname": "hostname"}

    # Mock method for find_file_in_search_path
    class MockFindFileInSearchPath:
        def __init__(self, return_value):
            self.return_value = return_value
            self.call_count = 0


# Generated at 2022-06-13 13:46:03.443442
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:46:07.736855
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.loader import lookup_loader

    terms = [
        {'files': 'file1,file2,file3',
         'paths': '/tmp/path'},
        {'files': 'file4',
         'paths': '/tmp/path1:/tmp/path2'},
        '/tmp/path3/foo.txt',
        {'files': 'file1,file2,file3',
         'paths': '/tmp/path4'},
        {'files': 'file5,file6'},
        '/tmp/path5/bar.foo'
    ]

    # Loop over all found search paths for 'files' and
    # raise an error if a file was found
    for path in lookup_loader.get('first_found').run(terms):
        raise Exception('no file should be found')



# Generated at 2022-06-13 13:46:18.863517
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.common.collections import ImmutableDict

    # mock args for basic function
    options = {
        'paths': '',
        'skip': False,
    }
    terms = []

    # terms can be a string, which is converted into a list
    terms = 'foo'
    # or a list of strings
    terms = ['foo']
    # or a list of string and/or dict
    terms = ['foo', {'files': 'bar'}]
    # only last dict will be used, as this is 'global' info
    terms = [{'files': 'f1'}, {'files': 'f2'}]

    # see 'toplevel' tests for other usage of the lookup

    # Test 1: no files if no terms
    expected = []

# Generated at 2022-06-13 13:46:28.524735
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    kwargs = {
        'files': ['foo', 'bar'],
        'paths': ['/foo', '/bar'],
        'skip': False
    }

    # Test empty terms
    lookup_module = LookupModule()
    result = lookup_module.run([], None)

    # Test one item list terms
    lookup_module = LookupModule()
    result = lookup_module.run(['/baz'], None)

    # Test list terms
    terms = [
        '/foo/foo',
        '/bar/bar',
        {'files': ['foo', 'bar'], 'paths': ['/foo', '/foo/bar']}
    ]
    lookup_module = LookupModule()
    result = lookup_module.run(terms, None)

    # Test 'skip'

# Generated at 2022-06-13 13:46:35.366011
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import shutil

    from ansible.utils.path import unfrackpath

    from units.mock.loader import Loader

    module_loader = Loader()
    lookup_plugin = module_loader.load_plugin('first_found')
    assert isinstance(lookup_plugin, LookupModule)

    # create a temporary directory to avoid breaking other tests
    tmpdir = 'test_lookup_first_found'
    if not os.path.isdir(tmpdir):
        os.mkdir(tmpdir)

    lookup_dir = os.path.join(tmpdir, 'lookup')
    os.mkdir(lookup_dir)

    # create a test directory structure

# Generated at 2022-06-13 13:46:47.418395
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    l._templar = __file__
    l._display = __file__
    l._loader = __file__

    terms = [{"files": ['a', 'b'], "paths": [], "skip": False}, {'files': ['a', 'b'], "paths": [], "skip": True}]
    variables = {}

    path = l.run(terms, variables)

    assert path == [__file__]

    terms = [{"files": ['a', 'b'], "paths": [], "skip": False}, {"files": ['a', 'b'], "paths": [], "skip": True}]
    variables = {}
    path = l.run(terms, variables)

    assert path == []


# Generated at 2022-06-13 13:46:58.695613
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    # pylint: disable=no-member

    class FakeLookupModule(LookupModule):

        def __init__(self, files=['1.txt'], paths=['.']):
            self._files = files
            self._paths = paths

        def get_option(self, key):
            if key == 'files':
                return self._files
            if key == 'paths':
                return self._paths
            return super(FakeLookupModule, self).get_option(key)

        def find_file_in_search_path(self, _, __, fn, ___):
            if fn in self._files:
                return fn
            return None

    class FakeTemplar:
        def __init__(self, *_):
            pass


# Generated at 2022-06-13 13:47:09.786845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test that the first file listed is returned when it exists
    assert LookupModule.run(['foo', 'bar'], {}) == 'foo'
    # Test that the first existing file is returned when they are listed in multiple paths
    assert LookupModule.run(['/tmp/foo', '/tmp/bar'], {}) == '/tmp/foo'
    # Test that no file found raise exception when skip is False
    try:
        LookupModule.run(['/does/not/exist'], {}, skip=False)
    except AnsibleLookupError:
        pass
    # Test that no file found return empty list when skip is True
    assert LookupModule.run(['/does/not/exist'], {}, skip=True) == []

# Generated at 2022-06-13 13:47:18.451017
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create an instanciate of LookupModule
    lookup_plugin = LookupModule()
    # test for different 'terms'
    test_terms = [42, {}, "name1", "name2, name3", ["name4", "name5"], ["name6", ["name7", "name8"]]]
    # test for different outputs
    test_return = [
        [],
        [],
        ['/path/to/name1'],
        ['/path/to/name2', '/path/to/name3'],
        ['/path/to/name4', '/path/to/name5'],
        ['/path/to/name6', '/path/to/name7', '/path/to/name8']
    ]

    # define a mock class for LookupBase.find_file_in_search_path

# Generated at 2022-06-13 13:47:27.013156
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # mock class LookupBase
    class LookupBase():
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing):
            pass

    # create instance of LookupModule
    l = LookupModule()
    l._templar = None
    l._subdir = 'files'

    # mock a list of files
    files = ['file1', 'file2']

    # mock a list of paths
    paths = ['path1', 'path2']

    # mock variable skip
    skip_true = True
    skip_false = False

    # mock variable variables
    variables = {'foo': 'bar'}

    # mock variable terms
    terms = [files, paths]
    terms_dict = {'files': files, 'paths': paths}

    # mock instance of LookupBase

# Generated at 2022-06-13 13:47:35.605030
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    lookup_test_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'test', 'unit', 'lookup_plugins')

    # test_LookupModule_run: test without skip option
    terms = LookupBase._lookup_args_from_terms(['a'], dict(), None)
    lookup = LookupModule()
    with open("./test_first_found1.txt", 'w') as f:
        f.write("test")
    os.chdir(lookup_test_dir)
    try:
        lookup.run(terms, dict(), files='./test_first_found1.txt')
    except AnsibleLookupError:
        assert True
    os.remove("./test_first_found1.txt")

# Generated at 2022-06-13 13:47:47.710801
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def side_effect(args, **kw):
        total_search = args[1]
        fn = kw['fn']
        for f in total_search:
            if f.endswith(fn):
                return f
        return None
    lookupModule = LookupModule()
    lookupModule._templar = object()
    lookupModule._templar.available_variables = {}
    lookupModule.find_file_in_search_path = object()
    lookupModule.find_file_in_search_path.side_effect = side_effect
    term = [
        {
            'files': '/file1',
            'paths': '/path1'
        },
        {
            'files': '/file2',
            'paths': '/path2'
        }
    ]
    # testing first file
    total

# Generated at 2022-06-13 13:47:58.279631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._fail = lambda s: s
    lookup.warn = lambda s, d: s
    lookup._templar = None
    lookup._loader = None

    # find
    assert lookup.run(['test_lookup_first_found.py'], dict()) == ['test_lookup_first_found.py']
    assert lookup.run([{ 'files': 'test_lookup_first_found.py' }], dict()) == ['test_lookup_first_found.py']
    assert lookup.run([{ 'files': 'test_lookup_first_found.py', 'paths': '.' }], dict()) == ['test_lookup_first_found.py']

    # find by vars

# Generated at 2022-06-13 13:48:11.450902
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing import vault
    from ansible.module_utils.six import StringIO

    # is really a 'mapping' but MutableMapping is a parent class
    # of dict but not a dict so we need this to test.
    class dict(MutableMapping):
        pass


# Generated at 2022-06-13 13:48:20.979977
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # FIXME: make this an integration test
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader

    lookup_module = LookupModule()
    assert isinstance(lookup_module, LookupBase)

    # test with first found
    vars = dict(
        files=['file1', 'file2', 'file3'],
        paths=['/path1', '/path2', '/tmp'],
        skip=True,
    )
    terms = ['file1', 'file2', 'file3']
    expected_result = ['/tmp/file1']
    result = lookup_module.run(terms, vars)
    assert result == expected_result

    # test with first found but skip not set

# Generated at 2022-06-13 13:48:33.181914
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleError
    from ansible_collections.ansible.misc.tests.unit.compat.mock import MagicMock

    lookup_obj = LookupModule()

    # Test with required option files is missing
    with pytest.raises(AnsibleLookupError) as exec_info:
        lookup_obj.run([{}], MagicMock())
    assert "One of the following is required" in str(exec_info.value)

    # Test with option skip is missing from args
    with pytest.raises(AnsibleLookupError) as exec_info:
        lookup_obj.run([{"files": "test_file"}], MagicMock())
    assert "skip" in str(exec_info.value)

    # Test with option skip is true, first file is valid, second file is

# Generated at 2022-06-13 13:48:38.072633
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create the lookup
    lookup = LookupModule()

    # create the options
    files = "bar, foo"
    paths = "foo:bar:baz"
    options = dict(files = files, paths = paths)

    # run the lookup
    lookup._process_terms(['foo'], dict(), options)

# Generated at 2022-06-13 13:48:54.614226
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    terms = [{'files': 'a,b', 'paths': 'path1:path2'}, 'c', ['d,e'], {'files': 'f,g'}, 'h']
    variables = {'ansible_lookup_paths': ['/a', '/b']}
    kwargs = {}

    # There is no file in the search path

# Generated at 2022-06-13 13:49:07.481660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Dummy(object):
        pass

    lookup = LookupModule()
    lookup.get_option = Dummy()
    lookup.set_options = Dummy()
    lookup._templar = Dummy()
    lookup._templar.template = Dummy()
    lookup._templar.template.side_effect = lambda x: x
    lookup.find_file_in_search_path = Dummy()
    lookup.find_file_in_search_path.side_effect = lambda variables, subdir, filename, ignore_missing=False: filename
    lookup._subdir = 'files'

    assert lookup.run(terms=[], variables={}) == [], 'it returns an empty list when no files are given'


# Generated at 2022-06-13 13:49:16.868149
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    # initialize
    lookup_plugin = LookupModule()

    # setup test data
    total_search = ['file1', 'file2']
    # mock constants
    lookup_plugin._subdir = 'subdir'

    # test with valid file found
    lookup_plugin.find_file_in_search_path = lambda x, y, z, ignore_missing=True: 'test_file'
    ret = lookup_plugin.run(total_search, variable_manager)

    assert ret == ['test_file']

    # test with valid no file

# Generated at 2022-06-13 13:49:25.340996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # no term
    result = lookup_module.run("", dict())
    assert isinstance(result, list) and len(result) == 0

    # no term passed in dict
    result = lookup_module.run([{}], dict())
    assert isinstance(result, list) and len(result) == 0

    # one term in dict
    result = lookup_module.run([{"files": ["foo.txt"]}], dict())
    assert isinstance(result, list) and len(result) == 0

    # one real term in dict
    result = lookup_module.run([{"files": ["vars.yml"]}], dict())
    assert isinstance(result, list) and len(result) == 1

# Generated at 2022-06-13 13:49:26.014859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 1

# Generated at 2022-06-13 13:49:30.600726
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()
    terms = ['/path/to/foo.txt']
    variables = {}
    # Using empty dict for kwargs since only 'files' and 'paths' keys are needed
    kwargs = {}

    res = module._process_terms(terms, variables, kwargs)
    assert res == ([terms[0]], False)


# Generated at 2022-06-13 13:49:31.909953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: fix this unit test?
    pass

# Generated at 2022-06-13 13:49:37.653389
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import binary_type
    from ansible.module_utils._text import to_bytes
    from ansible.utils.path import unfrackpath

    lookup = LookupModule()
    # BEGIN TEST: return files in current directory
    # set lookup._loader to a dummy object so we don't get an error
    # complaining about a missing loader
    lookup._loader = object()
    terms = [u'README.rst', u'NOT_THERE']
    variables = {}
    kwargs = {}
    result = lookup.run(terms, variables, **kwargs)
    assert os.path.basename(result[0]) == u'README.rst'
    # END TEST: return files in current directory

    # BEGIN TEST: return files in current directory using searchpath
    # set lookup._

# Generated at 2022-06-13 13:49:42.334439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._subdir = 'files'
    lookup_module._templar.template('test')
    lookup_module.find_file_in_search_path()
    lookup_module.run()

# Generated at 2022-06-13 13:49:51.793986
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:50:07.278113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host

    varmgr = VariableManager()
    host = Host(vars={'test_var': 'test_val'})
    varmgr.add_host(host)

    # Test used when lookup is called with: {{ lookup('first_found', ...) }}
    # FIXME: test_found and test_not_found are not handled by the LookupModule class
    test_found = {'terms': [['/does/not/exist', './does/not/exist', '/etc/']], 'skip':False}
    test_not_found = {'terms': [['/does/not/exist', './does/not/exist', '/does/not/exist']], 'skip':False}
   

# Generated at 2022-06-13 13:50:19.694462
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class OptionsModule(object):
        def __init__(self, var_options, direct=None):
            self._values = {}
            if isinstance(var_options, Mapping):
                self._values = var_options
            else:
                raise AnsibleLookupError("Invalid options supplied, must be a mapping")

            if isinstance(direct, Mapping):
                self._values.update(direct)

        def get(self, key, defval=None):
            if self._values.get(key):
                return self._values.get(key)
            return defval

        def __contains__(self, name):
            return name in self._values

        def __getitem__(self, name):
            return self._values[name]


# Generated at 2022-06-13 13:50:22.004374
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:50:28.434588
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._filename = 'test.yml'
    lookup._basedir = '/etc/ansible/roles/role_under_test/tasks'

    # test term is a dict
    result = lookup.run(terms=[{'files': 'file1.yml', 'paths': '/tmp'}], variables={})
    assert result == ['/tmp/file1.yml']

    # test term is a string without variable
    result = lookup.run(terms=['file2.yml'], variables={})
    assert result == ['/etc/ansible/roles/role_under_test/tasks/file2.yml']

    # test term is a string with variable
    variables = {'file': 'file3.yml'}
   

# Generated at 2022-06-13 13:50:37.352949
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils import basic
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256
    from __main__ import *
    lookup_module = LookupModule()
    options = ImmutableDict({u'paths': u'/tmp/files'})
    terms = [u'startnow.yml', u'otherfile.yml']

# Generated at 2022-06-13 13:50:51.190054
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: setup as class with methods to call self.assert*

    # example 1: set _found_file to empty list since skip=True, no file is found
    # if no value is given for `files` or `paths`
    params = [{'skip': True}]
    total_search, skip = LookupModule()._process_terms(params, {}, {'skip': True})
    assert skip
    assert isinstance(total_search, list)
    assert len(total_search) == 0
    assert len(LookupModule().run(params, {})) == 0

    # example 2: looking for /path/to/bar.txt
    params = [{'files': 'bar.txt', 'paths': '/path/to,/path/to/more'}]

# Generated at 2022-06-13 13:50:57.868260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import string_types

    class variables(dict):
        def get(self, key, default=None):
            return self[key] if key in self else default

    variables = variables()
    lookup_base = LookupBase()
    setattr(lookup_base, '_subdir', 'files')
    setattr(lookup_base, '_templar', 'files')
    lookup_module = LookupModule()
    lookup_module.set_loader(lookup_base._loader)

    def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
        file_list = files.get(subdir, [])

# Generated at 2022-06-13 13:51:10.061621
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test 1, invalid term
    lookup_module = LookupModule()
    lookup_module._templar = None
    with pytest.raises(AnsibleLookupError):
        lookup_module.run({"foo": "bar"})

    # test 2, invalid term
    lookup_module = LookupModule()
    lookup_module._templar = None
    with pytest.raises(AnsibleLookupError):
        lookup_module.run(1)

    # test 3, no file found
    lookup_module = LookupModule()
    lookup_module._templar = None
    with pytest.raises(AnsibleLookupError):
        lookup_module.run(["foo", "bar", "baz"])

# Generated at 2022-06-13 13:51:17.326815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    def find_file_in_search_path(*args, **kwargs):
        if args[2] == 'file1':
            return 'file1'
        else:
            return None

    lu.find_file_in_search_path = find_file_in_search_path


# Generated at 2022-06-13 13:51:29.043864
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Simple unit test of method run of class LookupModule

    test_LookupModule_run()
    """
    from ansible.context import context
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import lookup_loader

    context.CLIARGS = {}

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='localhost')

    variable_manager.set_inventory(inventory)

    lookup_module = lookup_loader.get('first_found', basedir='/tmp')
    # result = lookup_module._process_terms([{}, term2])
    result = lookup_

# Generated at 2022-06-13 13:51:41.400848
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test if the run method works correctly
    # Arrange
    lookup = LookupModule()
    lookup.set_options(var_options = {}, direct = {'paths': [], 'files': ['file1','file2','file3']})

    # Act
    result = lookup.run([])

    # Assert
    assert result is not None

# Generated at 2022-06-13 13:51:54.404659
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Case 1: invalid params
    # - Case 1.1: invalid terms
    terms_1 = [1]
    with pytest.raises(AnsibleLookupError):
        lookup.run(terms_1, {})
    # - Case 1.2: invalid var_options
    terms_2 = ["/path/to/file"]
    var_options_2 = {"not_recognized_option": "any value"}
    with pytest.raises(AnsibleLookupError):
        lookup.run(terms_2, var_options_2)
    # Case 2: no file found
    # - Case 2.1: no files
    terms_3 = [{}]