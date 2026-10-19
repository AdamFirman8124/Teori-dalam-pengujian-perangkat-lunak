

# Generated at 2022-06-13 13:42:04.655924
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule() 
    terms = [{"files": "test1.txt", "paths": "test_file"}]
    variables = dict()
    kwargs = dict()
    lookup_module._subdir = 'files'
    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ["test_file/test1.txt"]

# Generated at 2022-06-13 13:42:13.808034
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = [
        # terms, variables, **kwargs
        ([], {}, {}),
        ([{'files': 'file2'}], {'file1': 'file1_content'}, {}),
        ([{'files': 'file1'}], {'file1': 'file1_content'}, {}),
        ([{'files': 'file1', 'paths': 'path1'}], {'file1': 'file1_content'}, {}),
        ([{'files': 'file1', 'paths': 'path1', 'skip': True}], {'file1': 'file1_content'}, {}),
        ([{'files': 'file1', 'skip': True}], {'file1': 'file1_content'}, {}),
    ]


# Generated at 2022-06-13 13:42:27.711289
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:42:36.812323
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='../test/test_inventory.yml')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    variable_manager.extra_vars['ansible_distribution'] = 'CentOS'
    variable_manager.extra_vars['ansible_os_family'] = 'RedHat'
    variable_manager.extra_vars['ansible_virtualization_type'] = 'container'


# Generated at 2022-06-13 13:42:47.744424
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mock terms, variables
    terms = [{
        'files': ['firstfile', 'secondfile'],
        'paths': ['apath']
    }, {
        'files': ['thirdfile', 'fourthfile'],
    }]

    variables = {'ansible_foo': 'bar'}

    # mock file_lookup_result
    file_lookup_result = ['/apath/firstfile']

    # mock file_load_result
    file_load_result = ['firstcontent']

    l = LookupModule()
    l.set_loader(None)

    # mock find_file_in_search_path function
    l.find_file_in_search_path = Mock(return_value=file_lookup_result)

    # mock file_load function

# Generated at 2022-06-13 13:42:57.323130
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible_collections.community.general.plugins.modules.lookup.first_found import LookupModule
    terms = [{'files': 'bar.txt', 'paths':'/tmp/production', 'skip': False
              }, {'files': 'quux.txt', 'paths':'/tmp/production', 'skip': False
              }, {'files': 'foo.txt', 'paths':'/tmp/production', 'skip': True
             }]
    variables = {}
    lookup_module = LookupModule()
    path = lookup_module.run(terms, variables)
    assert path == ['/tmp/production/bar.txt']


# Generated at 2022-06-13 13:43:09.498140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test LookupModule.run without kwargs
    path = "/ansible/foo.txt"

    # FIXME: refactor lookup code so mocks are actually useful
    terms = [
        {'paths': '/ansible', 'files': 'foo.txt'},
        {'paths': '', 'files': 'foo.txt'},
        {'paths': '', 'files': ''}
    ]

    variables = {
        'src': "{{ lookup('first_found', findme) }}"
    }

    subdir = 'file'

    # Mock function LookupModule.find_file_in_search_path for path not None
    def mocked_find_file_in_search_path(variables, subdir, filename):
        if filename == 'foo.txt':
            return path

    # test with one

# Generated at 2022-06-13 13:43:15.037632
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    #
    # unit test includes simple data checking as this part is already tested
    # via integration tests.
    #

    with open('test_file', 'w') as f:
        f.write('test content')

    # valid tests for a valid term
    try:
        lookup = LookupModule()

        # simple test, this should work
        assert(lookup.run('test_file', {}) == ['test_file'])

        # testing wit an extra path
        assert(lookup.run([['test_file'], {'paths':[os.getcwd()]}], {}) == ['test_file'])

    finally:
        os.remove('test_file')

    # invalid tests for a invalid term

# Generated at 2022-06-13 13:43:25.822560
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with none value of term
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(None, None, None) == ([]), "Test with None term failed."

    # Test with invalid type of term
    lookup_plugin.run([ 1, 2 ], None, None) == ([]), "Test with invalid type term failed."

    # Test with invalid type of paths
    lookup_plugin.run(['path1', 'path2'], None, paths=1) == ([]), "Test with invalid path failed."

    # Test with valid type of paths
    lookup_plugin.run(['path1', 'path2'], None, paths=['path3']) == ([]), "Test with valid path failed."

    # Test with invalid paths value

# Generated at 2022-06-13 13:43:38.045978
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with a valid string that exists in the search path
    valid_string_obj = LookupModule()
    valid_string_obj._templar = None
    valid_string_obj._loader = None
    valid_string_obj._find_needle = None
    valid_string_obj.run_terms = None
    valid_string_obj._subdir = "files"

    terms = [
        {
            "files": "hello.txt",
            "paths": ["tests/integration/files/hello"],
        },
    ]


# Generated at 2022-06-13 13:43:49.281084
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.template import Templar
    import pytest

    lookup = LookupModule()
    lookup._templar = Templar(None, variables={})

    # Test with invalid terms, missing and invalid files, valid and invalid paths
    with pytest.raises(AnsibleLookupError) as err:
        lookup._process_terms([{}], {}, {})

    with pytest.raises(AnsibleLookupError) as err:
        lookup._process_terms([[]], {}, {})


# Generated at 2022-06-13 13:43:59.194152
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleLookupError
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.plugins.lookup import LookupBase
    import os

    # set up
    basic._ANSIBLE_ARGS = to_text(os.environ['ANSIBLE_ARGS'])
    lookup_paths = LookupBase().get_search_paths()

    # set up module (because run is static method)
    module = LookupModule()

    # test run (with simple path and env)
    os.environ['ANSIBLE_LOOKUP_PLUGIN_SEARCH_PATHS'] = lookup_paths

    # test on this module file!
    result = module.run(terms=['first_found.py'])
    assert result

# Generated at 2022-06-13 13:44:13.536834
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = UnitTest()
    lookup_module = LookupModule()

    terms = [
        'file',
        {'files': 'file1,file2', 'paths': 'path1,path2', 'skip': 'False'}
    ]
    variables = {'test': 'test_var'}
    kwargs = {'test_kwarg': 'test_kwarg_var'}

    assert lookup_module.run(terms, variables, **kwargs) == ['file1']
    assert lookup_module.run(terms, variables, **kwargs) == ['path1/file1', 'path2/file1', 'path1/file2', 'path2/file2']
    assert lookup_module.run(terms, variables, **kwargs) == ['file']



# Generated at 2022-06-13 13:44:25.156868
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup
    c = LookupModule()

    assert isinstance(c, LookupBase)

    # test
    assert c.run(terms=["test_data/test1", "test_data/test2"], variables={})[0] == "test_data/test1"
    assert c.run(terms=["test_data/test1", "test_data/test2"], variables={})[0] == "test_data/test1"

    with pytest.raises(AnsibleLookupError):
        c.run(terms=["test_data/test3", "test_data/test4"], variables={})[0] == "test_data/test1"

    c = LookupModule()

# Generated at 2022-06-13 13:44:36.068554
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(argument_spec={'terms': dict(required=True, type='list', elements='dict')})

    files = ['file_in_play', 'file_in_role', 'file_in_playbook', 'file_in_playbook_extra']
    paths = ['/tmp/foo', '/tmp/bar']
    total_search = [f for f in paths for fn in files] + files

    terms = [{'files': files}, {'paths': paths}, {'files': files}, {'files': files}]
    lm = LookupModule()

    # Create a fake result for lookup
    class Fake_Templar:
        def template(self, fn):
            return fn


# Generated at 2022-06-13 13:44:47.942761
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TESTING: running the test to pass, but since this is string i can not
    # add tests as i would like.
    # First create a lookup object
    lookup = LookupModule()

    # Mock the ansible variables
    variables = {}

    # List of valid items to search for files
    terms = ['file1.txt',
             'vars/file2.txt',
             'files/file3.txt',
             {'files': 'file5.txt'},
             {'files': ['file6.txt', 'file7.txt']},
             {'files': 'file8.txt', 'paths': 'vars'}]

    # Start testing
    # 1: test with a list of valid items and expected results
    results = lookup.run(terms, variables)

# Generated at 2022-06-13 13:44:59.776845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Check for osfamily / rolespecifc / default in ../roles/role_name/files
    # Use default

    # Check for path in ../playbooks/play-name/files
    # Use first

    # Check for path in ../playbooks/play-name/../group_vars/group_name
    # Use second

    # Check for path in ../playbooks/play-name/../group_vars/all
    # Use third

    # Check for path in ../playbooks/play-name/../host_vars
    # Use fourth

    # Check for path in ../playbooks/play-name/../host_vars/host_name
    # Use fifth

    # Check for path in ../group_vars/group_name
    # Use sixth

    # Check

# Generated at 2022-06-13 13:45:14.060125
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    """ Unit tests for LookupModule class method run """

    lookup = LookupModule()

    args = (
        # NOTE: '_terms' must be a list but all other keys are optional
        '_terms',

        # optional keys to test
        'files',
        'paths',
        'skip',

        # set 'skippable' to True
        'skippable'
    )

    # NOTE: kwargs cannot be empty or caller will fail
    # NOTE: must use 'skippable' as the key as it changes the error code
    #       it will be removed in the lookup class
    kwargs = {'skippable': True}

    # Set search paths to a known set

# Generated at 2022-06-13 13:45:24.015794
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Minimal call to class LookupModule
    l = LookupModule()

    # Call the method run()
    result = l.run(terms="test")
    assert result is None, "Return is not None : %s" % result

    result = l.run(terms="test", variables="test")
    assert result is None, "Return is not None : %s" % result

    result = l.run(terms="test", variables={"var" : "value"}, some_kwarg="testkwarg")
    assert result is None, "Return is not None : %s" % result

# Generated at 2022-06-13 13:45:33.842906
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test single param with one file's path
    param = ['/etc/ansible/facts.d/']
    variables = {}
    total_search, skip = LookupModule()._process_terms(param, variables, '')

    assert total_search == ['/etc/ansible/facts.d/']
    assert skip is False

    # test single param with list of file's paths
    param = ['/etc/ansible/facts.d/', '/etc/ansible/host_vars/']
    variables = {}
    total_search, skip = LookupModule()._process_terms(param, variables, '')

    assert total_search == ['/etc/ansible/facts.d/', '/etc/ansible/host_vars/']
    assert skip is False

    # test single param with list of file's paths and one file

# Generated at 2022-06-13 13:45:50.254319
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    EXPECTED_RESULT = ["/tmp/production/foo.txt", "/tmp/production/bar.txt", "/tmp/staging/foo.txt", "/tmp/staging/bar.txt",
                       "/dev/null/foo.txt", "/dev/null/bar.txt", "foo.txt", "bar.txt"]

    lookup_module = LookupModule()
    assert lookup_module.run([{'files': 'foo.txt,bar.txt', 'paths': '/tmp/production, /tmp/staging', 'skip': False},
                              {'files': 'foo.txt,bar.txt', 'paths': '/dev/null',
                               'skip': False}], {'_original_file': 'test', '_original_module': 'test'}) == EXPECTED_RESULT



# Generated at 2022-06-13 13:45:59.905354
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO - this test will be discussed with @zjw
    import pytest
    from ansible.utils.path import unfrackpath
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    # TODO - add failsafe check for existence of files before adding to dirs.

# Generated at 2022-06-13 13:46:10.533308
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test data
    terms = [
        {'files': 'hello.txt', 'paths': 'test/data/first_found'},
        'hello.txt',
        'hello.txt',
        'hello.txt',
        'hello.txt'
    ]
    variables = {}
    kwargs = {}

    # Instantiate LookupModule
    lm = LookupModule()

    # Execute run() of LookupModule with given test data
    res = lm.run(terms, variables, **kwargs)

    # Assert that the result is as expected
    assert res == ['test/data/first_found/hello.txt']

# Generated at 2022-06-13 13:46:16.838176
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    terms = {'files': 'a', 'paths': 'b'}
    variables = {}

    module.set_options(var_options=variables, direct=terms)

    module.get_option('files') == 'a'
    module.get_option('paths') == 'b'

    module.run(terms, variables=variables) # Cannot test as method find_file_in_search_path is static

# Generated at 2022-06-13 13:46:27.306316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a dummy class for ansible where the templar is always an empty object
    class Dummy(object):
        class Templar(object):
            def __getattr__(self, attr):
                return self

            def template(self, var):
                return var

        def __init__(self):
            self._templar = Dummy.Templar()

    # create a dummy class for ansible.vars with a static vars attribute
    class DummyVars(object):
        vars = {
            'ansible_virtualization_type': 'dummy_virtualization_type',
            'ansible_distribution': 'dummy_distribution',
            'ansible_os_family': 'dummy_os_family',
            'inventory_hostname': 'dummy_inventory_hostname',
        }
   

# Generated at 2022-06-13 13:46:34.852837
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l_m = LookupModule()

    # Making sure we get an AnsibleLookupError when running it with no operation to 'run'.
    try:
        l_m.run()
        assert False
    except AnsibleLookupError:
        assert True

    # Making sure we get an AnsibleLookupError when running it with no operation to 'run'.
    try:
        l_m.run([], {})
        assert False
    except AnsibleLookupError:
        assert True

    # Making sure we get an 'empty list back' when running it with a file that does not exist
    # in the first path specified.
    var_term = [{'files': 'file1', 'paths': '/path/to/file/that/does/not/exist'}]

# Generated at 2022-06-13 13:46:38.405717
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    lookup_plugin._templar = None
    assert lookup_plugin.run(['testfile1.txt'], {}, skip=True) == []

# Generated at 2022-06-13 13:46:50.238107
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    lookup._loader = None
    lookup._templar = None
    lookup._loader_plugins = None

    with pytest.raises(AnsibleLookupError):
        lookup.run([], {}, skip=False)

    def _find_file_in_search_path(variables, subdir, fn, ignore_missing=False):
        return fn

    file_name = "foo.yml"
    lookup._find_file_in_search_path = _find_file_in_search_path

    # missing file, skip=False
    with pytest.raises(AnsibleLookupError):
        files = ["bar.yml" , "foo.yml"]
        lookup.run(files, {}, skip=False)

    # delete file_name before next test

# Generated at 2022-06-13 13:47:00.537719
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:47:01.215847
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:47:15.508808
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from collections import namedtuple
    FakeHost = namedtuple('FakeHost', ('get_vars', 'get_name'))
    FakeHost_inst = FakeHost(lambda: {'inventory_hostname': 'paddle-opentracing-cassandra-1'}, lambda: 'localhost')
    FakeTask = namedtuple('FakeTask', ('_ds', '_role'))
    FakeTask_inst = FakeTask(dict(foo='bar'), dict(path='.'))
    FakePlayContext = namedtuple('FakePlayContext', ('variable_manager', 'task'))
    FakePlayContext_inst = FakePlayContext(namedtuple('FakeVariableManager', ('get_vars'))(lambda: {}), FakeTask_inst)

# Generated at 2022-06-13 13:47:25.910229
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar = Template()

    assert_equal(l.run(
        terms=['fn_from_option'],
        variables={
            'first_found': {
                'files': 'fn_from_option',
            }
        }),
        ['fn_from_option'])

    assert_equal(l.run(
        terms=[
            'fn_from_term',
            {
                'files': 'fn_from_dict',
            }
        ],
        variables={
            'first_found': {
                'files': 'fn_from_term',
                'paths': ['/path_from_term'],
            }
        }),
        ['fn_from_option', 'fn_from_dict'])


# Generated at 2022-06-13 13:47:35.290491
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LookupModule_instance = LookupModule()

    # run method test
    assert LookupModule_instance.run(terms=[{'files': 'foo', 'paths': 'path/to', 'skip': True}], variables={'foo': 'foo_var', 'bar': 'bar_var'}, lookup_plugin=None) == []
    assert LookupModule_instance.run(terms=[{'files': 'foo', 'paths': 'path/to'}], variables={'foo': 'foo_var', 'bar': 'bar_var'}, lookup_plugin=None) == ['path/to/foo']

# Generated at 2022-06-13 13:47:44.151320
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    _mock_terms = [
        {"files": "/etc/hosts", "paths": "/tmp/production:/tmp/staging"}
    ]
    _mock_variables = {}
    _mock_kwargs = {}
    _mock_self = LookupModule()

    # Act
    _result = _mock_self.run(_mock_terms, _mock_variables, **_mock_kwargs)

    # Assert
    assert _result == ["/etc/hosts"]

# Generated at 2022-06-13 13:47:45.611843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: provide a unit test for the 'run' method of the LookupModule
    pass

# Generated at 2022-06-13 13:47:57.138473
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu1 = LookupModule()
    assert lu1.run([], {}) == []

    lu2 = LookupModule()
    assert lu2.run([1], {}) == []

    lu3 = LookupModule()
    assert lu3.run([1], {}, files='foo', paths='path') == []

    lu4 = LookupModule()
    assert lu4.run([{'files': 'foo', 'paths': 'path'}], {}) == []

    lu5 = LookupModule()
    assert lu5.run([{'files': 'foo', 'paths': 'path'}], {}, files='foo', paths='path') == []

    lu6 = LookupModule()

# Generated at 2022-06-13 13:48:01.202843
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    try:
        lookup_module.run(['NOT_TERM'])
    except AnsibleLookupError:
        pass  # OK to not find a file
    else:
        assert False, "ERROR: No file found but expected AnsibleLookupError."

    try:
        lookup_module.run(terms=[{'not_files': True}])
    except AnsibleLookupError:
        pass  # OK to not find a file
    else:
        assert False, "ERROR: No file found but expected AnsibleLookupError."

# Generated at 2022-06-13 13:48:13.635464
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test without files and without paths
    # expected term value = ['./files']
    terms = ['./files']
    variables = {'a': 2}
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._loader = None
    assert lookup.run(terms, variables) == ['./files']

    # test with files and without paths
    # expected term value = ['./files/term1', 'file2.txt']
    terms = [{'files': 'term1, file2.txt'}]
    variables = {'a': 2}
    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._loader = None
    assert lookup.run(terms, variables) == ['./files/term1', 'file2.txt']

    # test with paths and

# Generated at 2022-06-13 13:48:19.296547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # define list of files and paths
    files = ['a', 'b']
    paths = ['c', 'd']

    # create params
    params = {
        'files': files,
        'paths': paths,
        'skip': True
    }

    # create partial function
    def _partial_func(self, terms, variables, **kwargs):
        # define list of files and paths
        files = ['a', 'b']
        paths = ['c', 'd']
        # create params
        params = {
            'files': files,
            'paths': paths,
            'skip': True
        }
        # set options
        self.set_options(var_options=variables, direct=params)
        # split
        files = self.get_option('files')

# Generated at 2022-06-13 13:48:31.078184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run([], {}) == []
    assert lookup.run(['notfound.txt'], {}) == []
    assert lookup.run([{'files': 'notfound.txt', 'skip': True}], {}) == []
    assert lookup.run([{'files': 'notfound.txt', 'paths': 'search_path'}], {}) == []
    assert lookup.run([{'files': 'notfound.txt', 'paths': 'search_path', 'skip': True}], {}) == []
    assert lookup.run(['notfound.txt'], {'files': 'notfound.txt'}) == []
    assert lookup.run(['notfound.txt'], {'files': 'notfound.txt', 'skip': True}) == []

# Generated at 2022-06-13 13:48:41.608696
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    f = LookupModule()
    terms = [ '../some_fake_file.txt' ]
    res = f.run(terms, {}, skip=True)
    assert res == []

    # TODO: write more tests

# Generated at 2022-06-13 13:48:51.620783
# Unit test for method run of class LookupModule
def test_LookupModule_run(): # FIXME: Test fail (wrong error message)

    from ansible.plugins.lookup.first_found import LookupModule # FIXME: Use mock objects instead of real Ansibles
    lookup = LookupModule()

    with pytest.raises(AnsibleLookupError) as exc:
        lookup.run([], [], skip=True)
    assert exc.value.message == "No file was found when using first_found."

    with pytest.raises(AnsibleLookupError) as exc:
        lookup.run([], [])
    assert exc.value.message == "No file was found when using first_found."

# Generated at 2022-06-13 13:49:04.835125
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a LookupModule object
    lu = LookupModule()

    # patch the templar object
    lu._templar = None

    # patch the find_file_in_search_path to return a value (path)
    lu.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing: "/path/to/file1"

    # no search paths and no files, skip True
    terms = []
    variables = {}
    kwargs = {
        'skip': True
    }
    result = lu.run(terms, variables, **kwargs)
    assert result == []

    # no search paths and no files, skip False
    terms = []
    variables = {}
    kwargs = {
        'skip': False
    }

# Generated at 2022-06-13 13:49:13.993272
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init class
    lookup_module = LookupModule()
    # set some vars
    variables = dict()
    variables['ansible_distribution'] = 'fake_distro'
    variables['ansible_os_family'] = 'fake_os_family'
    kwargs = dict()

    total_search = []
    skip = False

    # call method
    total_search, skip = lookup_module._process_terms(terms=['foo', 'bar', 'baz'],
                                                      variables=variables,
                                                      kwargs=kwargs)
    # assert result
    assert total_search == ['foo', 'bar', 'baz']
    assert skip == False

    # call method

# Generated at 2022-06-13 13:49:15.263517
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:49:26.268970
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        '/test_files/test_file_1.txt',
        {
            'files': [
                '/test_files/test_file_1.txt',
                '/test_files/test_file_2.txt'
            ],
            'paths': [
                'test_files'
            ],
            'skip': False
        },
        {
            'files': [
                '/test_files/test_file_1.txt',
                '/test_files/test_file_2.txt'
            ],
            'paths': [
                'test_files'
            ],
            'skip': True
        }
    ]
    variables = {}

    lookupmodule = LookupModule()
    result_list = lookupmodule.run(terms, variables, validate_certs=False)

    assert result_

# Generated at 2022-06-13 13:49:41.555777
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import stat
    import tempfile
    import shutil

    testdir = tempfile.mkdtemp()

# Generated at 2022-06-13 13:49:51.409290
# Unit test for method run of class LookupModule
def test_LookupModule_run():  #TODO: check if this test is ok
    lookup_mock = LookupModule()
    lookup_mock._process_terms = lambda terms, variables, kwargs: (terms, kwargs.get('skip', False))
    lookup_mock.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=False: 'True'

    #TODO: create unit tests with all possibilities
    assert lookup_mock.run(terms=['/path/to/foo.txt', 'bar.txt'], variables={}, skip=False) == ['/path/to/foo.txt']
    assert lookup_mock.run(terms=['/path/to/foo.txt', 'bar.txt'], variables={}, skip=True) == []

# Generated at 2022-06-13 13:50:02.119692
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # set up mock
    #######################################################################################
    # NOTE: it's not clear why this inherits from AnsibleLoader, this is tested elsewhere
    class MockTemplar():
        def template(self, value):
            return value
    term = 'bar'
    variables = [1, 2, 3]
    searchpath = ['/etc', '/usr/local/etc']
    files = ['foo.conf', 'foo.txt']
    paths = ':'.join(searchpath)
    kwargs = {
        'files': files,
        'paths': paths,
    }
    finderpath = {
        'files': [ 'files', 'files' ],
        'paths': searchpath
    }

# Generated at 2022-06-13 13:50:05.054924
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # See:
    #
    # - ansible/test/test_runner.py
    # - ansible/test/test_plugins/test_lookup/test_first_found.py
    # - ansible/test/units/lookup/test_file.py
    pass

# Generated at 2022-06-13 13:50:32.249874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.module_utils.six import string_types
    from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
    from ansible.plugins.lookup import LookupBase
    from ansible.parsing.yaml.objects import AnsibleUnicode
    import ansible
    import os

    ansible_path = ansible.__path__[0]
    playbooks_path = os.path.join(ansible_path, 'playbooks')
    playbooks_file = os.path.join(playbooks_path, 'lookup_plugins', 'library', 'test_first_found_file.yml')

# Generated at 2022-06-13 13:50:42.455363
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:50:53.929781
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Good scenario
    # /test_files/config_file_1.txt exists, /test_files/config_file_2.txt does not
    config_files = ["config_file_1.txt", "config_file_2.txt"]
    lookup_file = LookupModule()
    lookup_file_path = lookup_file.run(config_files, [], paths=[], files=config_files)
    assert len(lookup_file_path) == 1

    # Missing the file parameter
    try:
        lookup_file = LookupModule()
        lookup_file_path = lookup_file.run([], [], paths=[], files=[])
    except Exception as err:
        assert isinstance(err, AnsibleLookupError)
        assert str(err) == "Missing required terms, files"

    # Missing the file parameter

# Generated at 2022-06-13 13:51:08.208261
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(direct={'skip': 'True'})
    assert [] == l.run(['empty_list'])

    l.set_options(direct={'skip': 'False'})

    # param skip=False
    l.set_options(direct={'skip': 'False'})
    assert [] == l.run(['empty_list'])

    l.set_options(direct={'skip': 'True'})
    assert [] == l.run(['empty_list'])

    l.set_options(direct={'skip': ''})
    assert [] == l.run(['empty_list'])

    # param skip=True
    l.set_options(direct={'skip': 'True'})
    assert [] == l.run(['empty_list'])

    l

# Generated at 2022-06-13 13:51:19.621252
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:51:31.493395
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    lookup = LookupModule()
    lookup._subdir = 'files'
    lookup._loader = 'unused'
    lookup._templar = 'unused'

    # If a simple string is passed as terms, it should be returned
    terms = 'test.conf'
    variables = 'unused'
    kwargs = {'errors': 'strict'}
    result = lookup.run(terms, variables, **kwargs)
    assert result == terms

    # files must be a list
    terms = ['a.conf', 'b.conf', 'c.conf']
    variables = 'unused'
    kwargs = {'files': 'test.conf'}
    with pytest.raises(AnsibleLookupError) as err:
        lookup.run(terms, variables, **kwargs)


# Generated at 2022-06-13 13:51:35.833121
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Following are the test cases to test the source code
    lookup_module = LookupModule()
    assert lookup_module._process_terms is not None, "Method test_LookupModule_run failed"
    assert lookup_module.run is not None, "Method test_LookupModule_run failed"
    # TODO: Add test cases for the method run of class LookupModule

# Generated at 2022-06-13 13:51:43.117170
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Input param (variables):
    variables = dict()

    # Input param (terms):
    terms = [['/etc/hosts.allow'], ['hosts_allow.tmp', 'paths=[/etc/]', 'skip=True']]

    # Test object initialization
    obj = LookupModule()

    # Expected result:
    # 1. ['/etc/hosts.allow']
    # 2. []

    # Test run
    assert obj.run(terms, variables) in [['/etc/hosts.allow'], []]

# Generated at 2022-06-13 13:51:55.980112
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # term is not a string, not a list and not a mapping
    obj = LookupModule()
    fake_variables = {}
    term = 2
    results = obj.run(term, fake_variables)
    assert False, results

    # term is a string
    term = "test"
    results = obj.run(term, fake_variables)
    assert results == []

    # term is a mapping
    term = {'files': 'test, tes2', 'paths': '/test, /test2'}
    results = obj.run(term, fake_variables)
    assert results == []

    # term is a list
    term = ['test1', {'files': 'test, tes2', 'paths': '/test, /test2'}, 'test3']