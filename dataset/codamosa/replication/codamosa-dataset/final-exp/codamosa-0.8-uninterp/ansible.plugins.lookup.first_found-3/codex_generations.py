

# Generated at 2022-06-13 13:41:55.518972
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit testing for method run of class LookupModule """
    pass


# Generated at 2022-06-13 13:42:08.139148
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with options.
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(['/tmp/foo.txt'], dict(files=['bar.txt'])) == []

    assert lookup_plugin.run([{"files": ["bar.txt"], "paths": ["/tmp"]}], dict()) == []

    # Test with terms.
    assert lookup_plugin.run([], dict()) == []

    assert lookup_plugin.run(['/tmp/foo.txt', 'bar.txt'], dict(files=['bar.txt'])) == []

    assert lookup_plugin.run([{'files': ['bar.txt'], 'paths': ['/tmp']}, 'foo.txt'], dict()) == []

# Generated at 2022-06-13 13:42:14.992981
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.errors import AnsibleError
    from ansible.plugins.lookup.first_found import LookupModule

    class FakeTemplar:
        """Templar class with templating mocked out."""
        def __init__(self):
            self.template_result = None

        def template(self, templatestring, convert_bare=False, escape_backslashes=True,
                     fail_on_undefined=True, override_vars=None, preserve_trailing_newlines=False,
                     escape_minimum=False, convert_data=False, static_vars=None):
            return self.template_result

    class FakePlayContext:
        """PlayContext class with variables mocked out."""
        def __init__(self):
            self

# Generated at 2022-06-13 13:42:28.521562
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:42:37.171929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # case when some file is found.
    lookup_module._templar = lambda x: x
    lookup_module._templar.template = lambda x: x
    lookup_module.find_file_in_search_path = lambda *x: 'test_path'
    lookup_module._subdir = 'test_subdir'
    assert lookup_module.run([{'files': 'test_file', 'paths': 'test_path'}]) == ['test_path']

    # case when no file is found.
    lookup_module._templar = lambda x: x
    lookup_module._templar.template = lambda x: x
    lookup_module.find_file_in_search_path = lambda *x: None

# Generated at 2022-06-13 13:42:48.774353
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # case 1
    data = dict(terms='/tmp/foo.txt', variables={})
    lookup_mock = create_mock(LookupModule)
    lookup_mock._templar.template.return_value = '/tmp/foo.txt'
    lookup_mock.find_file_in_search_path.side_effect = [None, '/etc/foo.txt']
    ret = lookup_mock.run(*[data['terms'], data['variables']])
    assert(lookup_mock.run.call_count == 1)
    assert(lookup_mock.find_file_in_search_path.call_count == 1)

# Generated at 2022-06-13 13:42:57.879614
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _ = LookupModule({}, templar=None, loader=None)
    # Test relative paths, files (and directories) available
    assert _.run([['test_file_path/test_file_relative2.txt'], ['test_file_path/test_file_relative.txt']]) == ['test_file_path/test_file_relative.txt']
    # Test relative paths, directories available
    assert _.run([['test_file_path/test_file_relative2'], ['test_file_path/test_file_relative']]) == ['test_file_path/test_file_relative']
    # Test absolute paths, files (and directories) available

# Generated at 2022-06-13 13:43:10.003572
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    # Current test values
    current_test_values = {
        'terms': ['test1.txt', 'test2.txt', 'test3.txt'],
        'variables': {},
        'kwargs': {'errors': 'ignore'}
    }

    # Expected result for the current test values
    # Note that the find_file_in_search_path method of ansible.plugins.loader.lookup
    # is mocked to avoid external dependencies
    current_expected_result = ['test1.txt']

    # Call the tested method
    lookup_module = LookupModule()
    result = lookup_module.run(current_test_values['terms'], current_test_values['variables'], **current_test_values['kwargs'])



# Generated at 2022-06-13 13:43:17.150653
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common.collections import ImmutableDict
    import pytest
    lookup_plugin = LookupModule()

    # first call the run method
    # the run method has a variable number of arguments
    # the first argument is mandatory and defines the variable name used to identify the list of files/directories
    # the second argument is also mandatory and defines the list of paths/directories/files to search
    # the values of these two arguments are part of the input object

    # test 1: run method called with no argument
    no_args = ImmutableDict()
    with pytest.raises(AnsibleLookupError) as exec_info:
        lookup_plugin.run(no_args)

# Generated at 2022-06-13 13:43:21.954043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    output_empty = lookup_module.run(terms=[], variables=dict(), skip=True)
    assert output_empty == [], output_empty
    output = lookup_module.run(terms=[], variables=dict(), skip=False)
    assert output == [], output

# Generated at 2022-06-13 13:43:36.912207
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText as unsafe_text

    test_file_names = {
        'foo': 'foo',
        'bar': 'bar_lookup_plugin_test',
        'biz': 'biz'
    }
    test_file_contents = {
        'foo': 'foo contents',
        'bar': 'bar contents',
        'biz': 'biz contents'
    }
    test_paths = [
        'foo_path',
        'bar_path',
        'biz_path'
    ]
    test_files = [
        'foo',
        'bar',
        'biz'
    ]

    variables = {}

    lm = LookupModule()


# Generated at 2022-06-13 13:43:45.613246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.path import unfrackpath

    # current_path = unfrackpath('/home/vagrant/ansible/ansible/modules')
    current_path = unfrackpath('/home/vagrant/ansible/lib/ansible/modules/packaging')
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._loader = DataLoader()
    lookup._loader.set_basedir(current_path)

    # Test term = files = relative path
    terms = [ 'sample_lines.conf' ]
    variables = {}
    result = lookup.run(terms, variables)

# Generated at 2022-06-13 13:43:56.899245
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Test the run() method of the LookupModule class. """
    # Test the case where the path is None i.e. no file found
    lookup_module = LookupModule()
    lookup_module._templar = MagicMock()
    lookup_module._templar.template = MagicMock(return_value='/path/to/file')
    lookup_module.find_file_in_search_path = MagicMock(return_value=None)
    assert lookup_module.run(['/path/to/file'], {}) == [], 'Test failed'
    
    # Test the case where the path is not None i.e. found a file
    lookup_module = LookupModule()
    lookup_module._templar = MagicMock()

# Generated at 2022-06-13 13:44:06.086563
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # arrange
    terms = [
        {
            'files': 'file1, file2',
            'paths': '/path1, /path2',
        },
        {
            'files': 'file2, file3',
            'paths': '/path2, /path3',
        },
        '/foo/bar/file3',
    ]

    variables = None
    kwargs = {}

    # act
    result = LookupModule().run(terms, variables, **kwargs)

    # assert
    assert result == ['/path1/file1', '/path2/file2', '/foo/bar/file3']



# Generated at 2022-06-13 13:44:17.378342
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.listify import listify_lookup_plugin_terms

    class MockTemplar(object):
        def template(self, value, fail_on_undefined=False, convert_bare=False):
            return value

    terms = [
        'foo',
        {'files': 'first,second', 'paths': 'relative_path,/path'},
        ['third', 'fourth'],
        {'files': 'fifth,sixth', 'paths': 'relative_path,/path'},
    ]
    terms = listify_lookup_plugin_terms(terms, [], None, MockTemplar())

    luk = LookupModule()
    luk.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=False: fn

# Generated at 2022-06-13 13:44:26.382653
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # create test objects
    context = PlayContext()
    templar = Templar(loader=None, variables={}, shared_loader_obj=None)
    lookup = LookupModule()
    lookup._templar = templar

    # create mock files and directories
    mock_file0 = 'test_LookupModule_run_test0.txt'
    mock_file1 = 'test_LookupModule_run_test1.txt'
    mock_dir1 = 'test_LookupModule_run_dir1'
    mock_dir2 = 'test_LookupModule_run_dir2'

# Generated at 2022-06-13 13:44:36.930028
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test for method run of class LookupModule
    # This is an example of a simple test function for a class method
    # For more complex tests you may need to set more parameters in the
    # constructor for the object you are testing.

    test_term = [{'files': ['foo', 'bar'], 'paths': ['/tmp/test/path', '/tmp/test/path2']}]
    expected_result = ['/tmp/test/path2/bar']
    variables = {
        'ansible_playbook_dir': '/tmp/test',
        'ansible_role_dir': '/tmp/test/roles',
        'ansible_file_dir': '/tmp/test/files',
    }
    test_object = LookupModule()
    actual_result = test_object.run(test_term, variables)

# Generated at 2022-06-13 13:44:48.201107
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils import six
    import os

    def _force_not_found(self, path):
        if path == "file1" or path == "file2":
            return None
        return path

    if not hasattr(LookupBase, "_find_file_in_search_path"):
        class LookupModule(LookupBase):
            def _get_file_name_if_exists(self, file_name):
                return file_name
        LookupBase._find_file_in_search_path = _force_not_found
        LookupBase.run = LookupModule.run

    loader, inventory, _loader, _inventory, var

# Generated at 2022-06-13 13:44:54.176569
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test for method run
    # Test for method run when no file is found but skip is False
    terms = ['/path1/file1.txt', '/path2/file2.txt', '/path3/file3.txt']
    variables = {}
    parameters = {}
    lookup_module = LookupModule()
    try:
        lookup_module.run(terms, variables, **parameters)
    except AnsibleLookupError as e:
        assert e.message == "No file was found when using first_found."

    # Test for method run when no file is found and skip is True
    terms = ['/path1/file1.txt', '/path2/file2.txt', '/path3/file3.txt']
    variables = {}
    parameters = {'skip': True}
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:45:00.844059
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # init
    mock_self = LookupModule()

    # set test values
    mock_self.set_options(var_options={}, direct={'paths': ['path']})
    mock_self.set_options(var_options={}, direct={'files': ['file']})
    mock_self.set_options(var_options={}, direct={'skip': True})

    # init a test term
    term = {}
    term['files'] = ['file1.txt', 'file2.txt']
    term['paths'] = ['path1', 'path2']

    # build test variables
    variables = {}
    variables['path'] = 'path1'
    variables['files'] = 'file1.txt'

    # create mock method to test

# Generated at 2022-06-13 13:45:18.374390
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with mock
    Check = type('Check', (object,), {})()
    Check.__dict__ = {
        "finder": type('Finder', (object,), {}),
        "_templar": type('Templar', (object,), {}),
        "find_file_in_search_path": lambda *args: "/var/lib"
    }

    Check.finder.__dict__ = {
        "SEARCH_PATH": ['.']
    }

    Check._templar.__dict__ = {
        "template": lambda x: x
    }

    total_search, skip = Check._process_terms(terms=['one', 'two'], variables={}, kwargs={})
    assert total_search == ['one', 'two']
    assert skip == False

    total_search, skip = Check._

# Generated at 2022-06-13 13:45:30.343417
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._templar = DummyTemplar()
    lookup._loader = DummyLoader()
    lookup.set_options(direct={"files":"test_file.json", "paths":"test_path/test_path2"})
    assert lookup.run(terms=None, variables=None) == ['/test_path/test_path2/test_file.json']
    lookup.set_options(direct={"files":"test_file.json"})
    assert lookup.run(terms=None, variables=None) == ['test_file.json']
    lookup.set_options(direct={"files":"test_file.json", "paths":"test_path/test_path2", "skip": True})
    assert lookup.run(terms=None, variables=None) == []
    lookup.set

# Generated at 2022-06-13 13:45:31.179953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass # TODO

# Generated at 2022-06-13 13:45:39.998060
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # patching the function _find_needle_in_haystack:
    # it is called by find_file_in_search_path
    # and it is not compatible with python 3
    from ansible.plugins.lookup.first_found import _find_needle_in_haystack
    from ansible.plugins.lookup.first_found import _split_on

    def _find_needle_in_haystack(needle, haystack):
        if needle in haystack:
            return True
        return False

    # Test for option 'skip = False' and path not found
    # Test for a list of search paths
    # Test for a list of file names
    # Test for a dictionary that has 'files' and 'paths'
    lookup_module = LookupModule()

# Generated at 2022-06-13 13:45:51.547313
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test object
    lookup_module = LookupModule()

    # Test run without a file found
    total_search = [
        "inventory.d",
        "group_vars/all.yaml",
        "host_vars/%s.yaml" % "test_host",
        "/etc/ansible/hosts",
        "roles"
    ]
    skip = True
    # Test the method
    assert lookup_module.run(total_search, {}, **{}) == []

    # Test run for a file found
    total_search = ["group_vars/all.yaml", "host_vars/%s.yaml" % "test_host"]
    result = lookup_module.run(total_search, {}, **{})
    # Test the method

# Generated at 2022-06-13 13:46:03.394234
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    total_search = []
    term = [
        {
            'files': 'foo',
            'paths': ':;'
        },
        {
            'files': 'bar',
            'paths': ':;'
        },
        [
            {
                'files': 'foo2',
                'paths': ':;'
            },
            {
                'files': 'bar2',
                'paths': ':;'
            },
        ],
        'test',
        [
            'test2',
            {
                'files': 'test5',
                'paths': ':;'
            }
        ]
    ]

    total_search, skip = lookup._process_terms(term, None, None)

# Generated at 2022-06-13 13:46:05.313300
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LookupModule('').run(['notfound.file'],{})

# Generated at 2022-06-13 13:46:17.376311
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test class initialization
    l = LookupModule()
    l._templar = None
    # wrong type of terms
    terms = "foo.conf"
    variables = {}
    kwargs = {}
    with pytest.raises(AnsibleLookupError):
        l.run(terms, variables, **kwargs)
    # wrong type of variable
    terms = ["foo.conf"]
    variables = "foo"
    kwargs = {}
    with pytest.raises(AnsibleLookupError):
        l.run(terms, variables, **kwargs)
    # wrong type of kwargs
    terms = ["foo.conf"]
    variables = {}
    kwargs = "foo"

# Generated at 2022-06-13 13:46:27.545869
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # execute method without passing any params
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(None, None) == [], 'No files supplied, expected empty list'

    # execute method passing a string
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(['README.md'], None) == [], 'README.md does not exist, expected empty list'

    # execute method passing a list containing a string
    lookup_plugin = LookupModule()
    assert lookup_plugin.run([['README.md']], None) == [], 'README.md does not exist, expected empty list'

    # execute method passing a list containing a string
    lookup_plugin = LookupModule()

# Generated at 2022-06-13 13:46:35.156051
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 13:46:49.489415
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        {'files': 'foo.txt', 'paths': '/path/to,/other/path'},
        {'files': 'bar.txt,biz.txt', 'paths': '/path/to'},
        'buz.txt',
        {'files': 'bar.txt,biz.txt', 'paths': '/path/to', 'skip': True}
    ]
    terms2 = [{'files': 'a.txt,b.txt'}, {'files': 'c.txt,d.txt'}, {'files': 'e.txt,f.txt'}]

# Generated at 2022-06-13 13:46:59.932047
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        {'files': 'f1,f2', 'paths': '/p1:/p2'},
        {'files': 'f2,f3', 'paths': '/p1:/p2'},
    ]
    variables = {}
    kwargs = {}

    lookup_plugin = LookupModule()
    lookup_plugin._subdir = 'files'

    def side_effect(variables, basedir, fn, ignore_missing):
        if fn.endswith('f3'):
            return os.path.join(basedir, fn)
        return None

    lookup_plugin.find_file_in_search_path = side_effect

    expected = [os.path.join('files', 'f3')]
    actual = lookup_plugin.run(terms, variables, **kwargs)


# Generated at 2022-06-13 13:47:08.921482
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import shutil
    import tempfile
    import ansible.module_utils.six as six

    # Setup test data
    test_temp_dir = tempfile.mkdtemp()
    test_filename = six.text_type(os.urandom(32).encode('hex'))
    test_dir = six.text_type(os.urandom(32).encode('hex'))
    test_dir_path = os.path.join(test_temp_dir, test_dir)
    test_path = os.path.join(test_dir_path, test_filename)
    init_path = os.path.join(test_temp_dir, "__init__.py")
    os.mkdir(test_dir_path, 0o755)
    open(test_path, 'a').close()


# Generated at 2022-06-13 13:47:17.805635
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # set up a environment and 2 files to find
    tmpdir = '/tmp/ansible-test-LookupModule-first_found'
    os.makedirs(os.path.join(tmpdir, 'playbooks', 'files'))
    os.makedirs(os.path.join(tmpdir, 'playbooks', 'folder'))
    os.makedirs(os.path.join(tmpdir, 'playbooks', 'folder', 'files'))
    os.makedirs(os.path.join(tmpdir, 'playbooks', 'folder', 'var'))

# Generated at 2022-06-13 13:47:26.714304
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=import-error,unused-variable,unused-argument
    import ansible.plugins.lookup.first_found
    import ansible.plugins.loader
    import ansible.template

    # pylint: disable=import-error,no-name-in-module,redefined-outer-name
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Host(name='localhost', port=None)
    inventory.vars = {'ansible_connection': "local"}
    variable_manager.set_inventory(inventory)

    # pylint: disable=too-many-function-args,no-member
    first

# Generated at 2022-06-13 13:47:34.409544
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    first_found_lookup = LookupModule()

    terms = [
        {
            'files': 'foo,bar',
            'paths': 'baz,biz'
        },
        {
            'files': 'foo2,bar2',
            'paths': 'baz2,biz2'
        },
        [
            {
                'files': 'foof,barf',
                'paths': 'bazf,bizf'
            },
            {
                'files': 'foof2,barf2',
                'paths': 'bazf2,bizf2'
            }
        ]
    ]


# Generated at 2022-06-13 13:47:37.673321
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run(terms=['/path1/filename1', '/path2/filename2'], variables={}, skip=True)
    assert result == []

# Generated at 2022-06-13 13:47:49.007713
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_obj = LookupModule()

    assert lookup_obj.run(terms=['foo'], variables={}, skip=False) == ['foo']
    assert lookup_obj.run(terms=[{'files': 'foo.txt'}], variables={}, skip=False) == ['foo.txt']
    assert lookup_obj.run(terms=[{'files': 'foo.txt',
                                  'paths': 'db'}], variables={}, skip=False) == ['db/foo.txt']
    assert lookup_obj.run(terms=[{'files': 'foo.txt',
                                  'paths': 'db:exec'}], variables={}, skip=False) == ['db/foo.txt',
                                                                                       'exec/foo.txt']

# Generated at 2022-06-13 13:47:58.909900
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import pytest
    from ansible.plugins.lookup.first_found import LookupModule
    from ansible.parsing.vault import VaultLib

    lookup_plugin = LookupModule()
    lookup_plugin._subdir = 'files'


# Generated at 2022-06-13 13:48:06.149188
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    lookup._templar = type('Templar', (object,), {'template': lambda s, t, fail_on_undefined=True: t})()
    lookup.set_options(var_options={'role_path': 'test'}, direct={'_terms': ['test.txt']})
    assert lookup.run() == ['test.txt']

# Generated at 2022-06-13 13:48:24.575085
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #
    # pylint: disable=unused-variable
    #

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.plugins.lookup.first_found import LookupModule
    from ansible.context import context
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'a': 'X'})

    #
    # Simple list of files
    #
    lookup_instance = LookupModule()

    try:
        res = lookup_instance.run(terms=['one', 'two'], variables=dict())
    except LookupError as e:
        res = None
        msg = str(e)
        assert msg == "No file was found when using first_found.", 'Unexpected error message: "%s"' % msg

# Generated at 2022-06-13 13:48:36.656496
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # No file found
    lookup = LookupModule()
    assert lookup.run(terms=['c:\\temp\\foo.txt'], variables=None) == []

    # File found
    lookup = LookupModule()
    assert lookup.run(terms=['c:\\windows\\system32\\drivers\\etc\\hosts'], variables=None) == ['c:\\windows\\system32\\drivers\\etc\\hosts']

    # No file found
    lookup = LookupModule()
    assert lookup.run(terms=['foo.txt'], variables=None) == []

    # File found
    lookup = LookupModule()
    assert lookup.run(terms=['hosts'], variables=None) == ['c:\\windows\\system32\\drivers\\etc\\hosts']

    # No file found
    lookup = LookupModule()

# Generated at 2022-06-13 13:48:45.649273
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    term_one = {'files': 'a_test', 'paths': 'a_path'}
    with pytest.raises(AnsibleLookupError) as excinfo:
        lookup.run(term_one, {})
    assert 'No file was found when using first_found' in str(excinfo.value)

    term_two = ['a_test', 'a_path']
    with pytest.raises(AnsibleLookupError) as excinfo:
        lookup.run(term_two, {}, files='x_test', paths='x_path')
    assert 'No file was found when using first_found' in str(excinfo.value)

    term_three = {'files': 'a_test', 'paths': 'a_path', 'skip': False}
   

# Generated at 2022-06-13 13:48:46.705088
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # load_fixture_data()
    pass

# Generated at 2022-06-13 13:48:53.020783
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms_list = [
        'term1',
        {
            'files': 'file1,file2',
            'paths': 'path1',
        },
        {
            'files': 'file3',
            'paths': 'path2,path3',
        },
    ]
    self = LookupModule()
    result = self.run(terms_list, variables={}, wantlist=False)
    assert result == 'term1'


# Generated at 2022-06-13 13:49:06.670028
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange

    # Declare vars
    class TestObject():
        def __init__(self, name):
            self.name = name

    class TestLookupModule(LookupModule):
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing):
            return "/path/to/file"

    # Get a list of functions in class LookupModule
    members = inspect.getmembers(LookupModule)
    for name, data in members:
        # If a function, append it
        if inspect.isfunction(data):
            setattr(TestLookupModule, name, data)
    # Get a list of functions in class AnsibleLookupError
    members = inspect.getmembers(AnsibleLookupError)

# Generated at 2022-06-13 13:49:09.697637
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: test this more, get why it is sooooo compl
    # NOTE: why does test_first_found_run not test dictionary term ?
    pass

# Generated at 2022-06-13 13:49:11.159053
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Test not implemented"


# Generated at 2022-06-13 13:49:26.177414
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # for testing use of jinja2
    import jinja2
    from ansible._vars import VariableManager
    from ansible.template import Templar, AnsibleEnvironment
    import os

    # play/role/example_playbook/files/variables.yml

    variables = VariableManager()

    # NOTE: path must exist and be relative, not finding a file is OK
    # NOTE: should catch errors from template
    path = None

    test_templar = Templar(loader=None, variables=variables, environment=AnsibleEnvironment(loader=None))
    variables.update({'ansible_virtualization_type': 'vagrant'})

    # example 1
    # setup
    full_path = 'test_templates/'

# Generated at 2022-06-13 13:49:41.478920
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar

    # setup basic module
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=False)

    # setup real template
    templar = Templar(loader=None, variables={})

    # setup class
    lu = LookupModule(loader=None, templar=templar, variables={})

    # tests
    # first file exists
    files = ['a', 'b', 'c']
    paths = ['tests/unit/lookup_plugins/files']
    lookup_kwargs = {'files': files, 'paths': paths}

# Generated at 2022-06-13 13:50:07.203188
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json

    # fixture: no errors
    terms = [
        {'files': 'foo.txt', 'paths': '/tmp/production:/tmp/staging'},
        {'files': 'bar.txt', 'paths': '/tmp/production:/tmp/staging'},
    ]
    variables = {}
    lookup = LookupModule()
    lookup.set_loader(lambda: json.dumps({'foo.txt': '', 'bar.txt': ''}))
    result = lookup.run(terms, variables)
    assert result == ['/tmp/production/foo.txt', '/tmp/production/bar.txt']

    # fixture: yamlfiles

# Generated at 2022-06-13 13:50:19.645592
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # NOTE: This is incomplete
    #    - variables on first_found are ignored
    #    - this should have 'using a dict' tests and more
    lookup = LookupModule()

    terms = [
        "bar",
        {
            "files": "foo,bar",
            "paths": "/tmp/whatever",
            "errors": "ignore",
            "skip": False,
            "match": "first"
        },
        "qux",
    ]

    # No files found, not skipping
    with pytest.raises(AnsibleLookupError) as exc:
        lookup.run(terms, {})
    assert "No file was found when using first_found." in str(exc.value)

    # Set files to find

# Generated at 2022-06-13 13:50:32.250264
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.module_utils import basic

    loader = DataLoader()
    variables = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='first_found', args=dict(files=dict(files='test_first_found', paths='./'))))
            ]
        )
    play = Play().load(play_source, variable_manager=variables, loader=loader)
   

# Generated at 2022-06-13 13:50:42.871109
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six.moves.urllib.parse import urlsplit
    from ansible.module_utils._text import to_bytes

    def mock_get_config_for_module(self, *args, **kwargs):
        return {
            'paths': [],
            'files': [],
            'extensions': [],
            'skip': False,
        }

    # Return a fake file for the given path
    def mock_find_file_in_search_path(self, *args, **kwargs):
        (path, filename) = args[2:]
        if path != '/path/to':
            return None
        if filename == 'files/bar.txt':
            return 'foo.txt'
        return None

    # Return a fake directory for the given path

# Generated at 2022-06-13 13:50:54.085030
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test for method run of class LookupModule
    # TODO: do more testing

    lm = LookupModule()

    # some tests,
    # one dict, onedict
    r = lm.run([{'files': 'foo', 'paths': 'bar'}], {})
    assert r == ['/etc/ansible/roles/role_under_test/bar/foo']

    # some tests,
    # one dict, nodedict
    r = lm.run([{'files': 'foo', 'paths': 'bar'}, {'files': 'biz', 'paths': 'baz'}], {})
    assert r == ['/etc/ansible/roles/role_under_test/bar/foo']

    # one string, one string

# Generated at 2022-06-13 13:51:05.195434
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test(terms, variables, skip):
        lm = LookupModule()
        lm.set_options({'files': 'test.txt', 'paths': './test', 'skip': skip})
        ret = lm.run(terms, variables)
        return ret
    assert test('test.txt', {}, False) == ['./test/test.txt']
    assert test(['test.txt'], {}, True) == []
    assert test(['test.txt'], {}, '1') == []
    assert test(['test.txt'], {}, None) == ['./test/test.txt']

# Generated at 2022-06-13 13:51:10.836313
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global_options = dict(src_file="ansible/plugins/lookup/first_found.py")
    run_args = dict(terms=["a", "b", "c"], variables=[], **global_options)
    r = LookupModule().run(*run_args)
    return r

if __name__ == '__main__':
    from pprint import pprint
    pprint(test_LookupModule_run())

# Generated at 2022-06-13 13:51:16.137942
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    m = lm.run
    assert m([{'files': ['foo']}], None) == 'foo'
    assert m([{'files': ['foo'], 'paths': ['path']}], None) == 'path/foo'
    assert m([{'files': ['foo']}, {'files': ['bar']}], None) == 'bar'
    assert m([{'files': ['foo1', 'foo2']}, {'files': ['bar']}], None) == 'foo1'



# Generated at 2022-06-13 13:51:27.666234
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import tempfile

    files = (('foo.txt', 'content1'),
             ('bar.txt', 'content2'),
             ('temp/bar.txt', 'content3'),
             ('temp/spam.txt', 'content4'))

    lookup = LookupModule()

    # create test files
    with tempfile.TemporaryDirectory() as tmpdir:
        for fn, content in files:
            os.makedirs(os.path.dirname(os.path.join(tmpdir, fn)), exist_ok=True)
            with open(os.path.join(tmpdir, fn), 'w') as f:
                f.write(content)
        # set base dir for search
        lookup._basedir = tmpdir

        # basic usage

# Generated at 2022-06-13 13:51:37.453617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    lu._templar = DummyTemplar()
    lu._loader = DummyLoader()
    lu.set_options(var_options={}, direct={})

    # The 'terms' parameter
    # 1) dict type
    files = [ 'foo', 'bar' ]
    paths = [ 'baz' ]
    terms = [
        { 'files': files },
        { 'paths': paths },
        { 'files': files, 'paths': paths }
    ]
    for term in terms:
        lu.run(term, {})
    # 2) list type
    terms = [
        files,
        paths,
        files + paths
    ]
    for term in terms:
        lu.run(term, {})
    # 3) string type
