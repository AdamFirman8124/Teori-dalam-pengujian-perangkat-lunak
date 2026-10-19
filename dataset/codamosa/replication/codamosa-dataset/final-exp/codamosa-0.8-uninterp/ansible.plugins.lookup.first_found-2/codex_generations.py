

# Generated at 2022-06-13 13:42:11.473385
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar = None
    l._loader = None
    l._find_file_in_search_path = None
    l._subdir = None

    # Test No files
    with pytest.raises(AnsibleLookupError) as context:
        l.run(None, None)
    assert "No file was found when using first_found." in str(context.value)

    # Test file not found
    f = 'missing'
    with pytest.raises(AnsibleLookupError) as context:
        l.run([f], None)
    assert "No file was found when using first_found." in str(context.value)

    # Test file found, no skip
    f = 'modules'
    result = l.run([f], None)

# Generated at 2022-06-13 13:42:25.773958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up an environment with a couple of files which can be found by the
    # first_found lookup.
    import tempfile
    lookup_dir = tempfile.mkdtemp()
    # This path will be relative to the location of this file.
    test_file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'first-found-file.txt')
    # Create a directory to be searched by the first_found lookup.
    dir_to_find = os.path.join(lookup_dir, 'find-me')
    os.mkdir(dir_to_find)
    # Put a copy of the test file inside the directory to be found.

# Generated at 2022-06-13 13:42:35.948363
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # NOTE: dict term has issues.
    #  any file that is found will 'skip' the rest of the list.
    #  any 'skip' in a dict term clobbers the previous one when joining
    
    # test for dict term
    # result = lookup_module.run([{'files': ['foo.txt'], 'paths': ['path1', 'path2']},
    #                             {'files': ['bar.txt'], 'paths': ['path1', 'path2']}],
    #                            dict(role_path=['/a/b']), var_templates=dict(test=42))
    # assert result == ['/a/b/files/path1/foo.txt']

    # test for string term

# Generated at 2022-06-13 13:42:40.997601
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    l = LookupModule()

    # no file passed
    assert l.run(terms=['foo'], variables={}) == []
    assert l.run(terms=['foo'], variables={'skip': True}) == []
    assert l.run(terms=['foo'], variables={'skip': False}) != []

# Generated at 2022-06-13 13:42:50.943296
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._subdir = 'files'
    assert l.run(["test_files/test_file"], dict()) == ["test_files/test_file"]
    assert l.run([dict(files=["test_files/test_file"])], dict()) == ["test_files/test_file"]
    assert l.run([dict(files=["test_files/test_file"], skip=True)], dict()) == ["test_files/test_file"]
    assert l.run([dict(files=["test_files/not_existing"], skip=True)], dict()) == []
    assert l.run([dict(files=["test_files/not_existing"], skip=False)], dict()) == []  # should raise an exception


# Generated at 2022-06-13 13:42:58.613888
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    params = dict(
        files=['tasks.yaml', 'other_tasks.yaml'],
        paths=['/path/to/'],
        skip=False
    )
    lm = LookupModule()
    terms = [params]
    lm._subdir = 'files'

    data_loader = DataLoader()

    # Existing file
    result = lm.run(terms, data_loader, templar=None)
    assert result == ['tasks.yaml']

    # Non-existing file
    result = lm.run(terms, data_loader, templar=None)
    assert result == []

# Generated at 2022-06-13 13:43:09.233447
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    
    variables = {}
    terms = [
        [
            {
                'paths': ['/tmp/test1', '/tmp/test2'],
                'files': ['test1.conf', 'test2.conf']
            },
            {
                'paths': ['/tmp/test1', '/tmp/test2'],
                'files': ['test3.conf', 'test4.conf']
            }
        ]
    ]
    
    result = lookup_module.run(terms, variables)
    assert result == ['/tmp/test1/test3.conf']

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:43:16.778156
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # We expect list ['foo']
    total_search, skip = lookup._process_terms(['foo'], {}, {})
    assert total_search == ['foo']

    # We expect list ['foo']
    total_search, skip = lookup._process_terms(['foo'], {}, {'files': ['foo']})
    assert total_search == ['foo']

    # We expect list []
    total_search, skip = lookup._process_terms([{'files': ['foo']}], {}, {})
    assert total_search == ['foo']

    # We expect list []
    total_search, skip = lookup._process_terms([{'files': ['foo'], 'paths': ['bar']}], {}, {})
    assert total_search == ['bar/foo']

    # We expect list

# Generated at 2022-06-13 13:43:27.083069
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import random
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes, to_text
    if PY2:
        from io import BytesIO
        b_io = BytesIO
    else:
        from io import StringIO

    lookup_module = LookupModule()
    path = os.path.abspath(__file__)
    dirname = os.path.dirname(path)
    files_dirname = os.path.join(dirname, "files")
    if PY2:
        files_path = to_bytes(files_dirname, errors='strict')
    else:
        files_path = to_text(files_dirname, errors='strict')


# Generated at 2022-06-13 13:43:29.017303
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    #TODO: implement unit test 
    assert False

# Generated at 2022-06-13 13:43:42.345382
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initializing a Lookup module and a Jinja2 environment to test the run method
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    class Options(object):
        def __init__(self):
            self.paths = []
            self.files = []
            self.skip = False
    options = Options()
    class VariableManager_mock(object):
        def __init__(self):
            self._fact_cache = dict()
        def get_vars(self, search_paths):
            return {'ansible_virtualization_type': '', 'ansible_os_family': '', 'ansible_distribution': ''}

# Generated at 2022-06-13 13:43:49.685972
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils._text import to_bytes
    from units.mock.lookup_plugin import mock_lookup_loader, MockLookupModule

    terms = [
        '1',
        {'files': 'test_3', 'skip': 'True'},
        ['test_2'],
        {'files': 'test_5', 'paths': 'test_6'}
    ]

    # In order:
    #   files=['1', 'test_3']
    #   paths=[]
    #   skip=False
    #   files=['test_2']
    #   paths=[]
    #   skip=False
    #   files=['test_5']
    #   paths=['test_6']
    #   skip=False

# Generated at 2022-06-13 13:43:59.433890
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:44:14.484441
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test1: test with the input terms as a list of string
    terms = [
        "/etc/ansible/group_vars/mygroup/vars.yaml",
        "/etc/ansible/group_vars/mygroup.yaml",
        "/etc/ansible/host_vars/myhost/vars.yaml",
        "/etc/ansible/host_vars/myhost.yaml"
    ]

    variables = {}

    set_option_terms = [
        {'files': 'some_file', 'paths': '/some/path'},
        'some_term',
        ['some_file', 'some_path']
    ]
    # create object
    obj = LookupModule()

    # test with different input terms

# Generated at 2022-06-13 13:44:25.571249
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Define test function
    def test_function(terms, variables, **kwargs):
        lookup_mod = LookupModule()
        test_subdir = 'test_subdir'
        lookup_mod._subdir = test_subdir
        return lookup_mod.run(terms, variables, **kwargs)

    # Define test data
    test_data = (
        # test_data structure:
        #  terms           variables     kwargs       expected_path
        (
            "test_file_1",
            dict(),
            dict(),
            None
        ),
        (
            "test_file_2",
            dict(),
            dict(),
            None
        ),
    )

    # Create mocks

# Generated at 2022-06-13 13:44:36.361828
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import string_types

    subdir = 'files'
    terms = ['foo/*.conf']
    variables = {'role_path': 'foo'}
    kwargs = {}
    expected_total_search = ['foo/*.conf']
    expected_skip = False

    obj = LookupModule(loader=None, variables=None)

    result_total_search, result_skip = obj._process_terms(terms, variables, kwargs)

    # NOTE: `_process_terms` is an internal method that is not part of the public interface
    #       but this test documents the expected results.
    assert isinstance(result_total_search, list)
    assert len(result_total_search) == 1


# Generated at 2022-06-13 13:44:48.095024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._templar = DictVars()

    # No files found
    assert lookup.run(terms = ['/path/to/foo.txt', '/path/to/bar.txt'], variables = dict()) == []

    # No files found
    assert lookup.run(terms = ['/path/to/foo.txt', '/path/to/bar.txt'], variables = dict()) == []

    # No files found
    assert lookup.run(terms = ['/path/to/foo.txt', '/path/to/bar.txt'], variables = dict()) == []

    # One file found

# Generated at 2022-06-13 13:44:59.777155
# Unit test for method run of class LookupModule
def test_LookupModule_run():

  # __init__(self, loader=None, templar=None, shared_loader_obj=None)
  loader = None
  templar = None
  shared_loader_obj = None
  obj = LookupModule(loader, templar, shared_loader_obj)

  # _process_terms(self, terms, variables, kwargs)
  # obj.set_options(var_options=variables, direct=term)
  obj._options = {'files': ['file1', 'file2'], 'paths': ['path1', 'path2']}
  terms = [{'files': ['file3', 'file4'], 'paths': ['path3', 'path4']}, {'files': ['file5', 'file6'], 'paths': ['path5', 'path6']}]

# Generated at 2022-06-13 13:45:14.022837
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1 - a single term with a file and a path
    lookup_params = {
        'files': 'a_file',
        'paths': '/a/path'
    }
    parser = LookupModule().parse(lookup_params)
    result = LookupModule().run(parser, None)
    assert result == ['/a/path/a_file']

    # Test 2 - a single term with a file and no path
    lookup_params = {
        'files': 'a_file'
    }
    parser = LookupModule().parse(lookup_params)
    result = LookupModule().run(parser, None)
    assert result == ['files/a_file']

    # Test 3 - a single term with a list of files and a path

# Generated at 2022-06-13 13:45:22.063218
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test for method run of class LookupModule
    # FIXME: this is too limited
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    lm = LookupModule(loader)

    files = [{'files': 'foo,bar'}]
    paths = [{'paths': 'baz,biz'}]
    terms = ['foo', 'bar']

    total_search, skip = lm._process_terms(files, {}, {'files': 'foo,bar'})
    assert (total_search == ['foo', 'bar'])
    assert (skip is False)

    total_search, skip = lm._process_terms(paths, {}, {'paths': 'baz,biz'})

# Generated at 2022-06-13 13:45:32.631990
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.run = _LookupModule_run
    assert LookupModule.run(["dummy_file"],{},"") == ['Test Path']

# Mock method to test run method of class LookupModule

# Generated at 2022-06-13 13:45:40.810254
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LOOKUP = LookupModule()

    # get class variables
    #_templar
    #find_file_in_search_path()
    #_subdir = 'files'
    #
    # get class methods
    #run()
    #set_options()
    #get_option()
    #
    # set class functions
    def mock_tmp(src, vars):
        return src

    def mock_find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        if "SUBDIR" in fn:
            return subdir+"/"+fn
        else:
            return fn

    LOOKUP._templar = mock_tmp
    LOOKUP.find_file_in_search_path = mock_find_file_in_search_path
    LOOKUP._sub

# Generated at 2022-06-13 13:45:51.599996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    luc = LookupModule()
    luc._subdir = 'templates'
    lookup_results = luc.run([
        {
            'files': 'foo.conf',
            'paths': '/extra/path'
        },
        {
            'files': 'bar.conf',
            'paths': '/extra/path'
        },
        {
            'files': 'baz.conf',
            'paths': '/extra/path'
        }
    ], dict())
    assert lookup_results == ['/extra/path/foo.conf']

# Generated at 2022-06-13 13:46:03.421029
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TEST: with ERRORS and ignore
    looker = LookupModule()
    looker.set_options({'errors': 'ignore'})
    assert looker.run([], {}, **{'skip': True}) == []
    assert looker.run([], {}, **{'skip': False}) == ''
    # TODO: think about this more, for now we will check the keywords again
    assert looker.run([], {}, **{'term': '', 'skip': True}) == []
    assert looker.run([], {}, **{'term': '', 'skip': False}) == ''
    assert looker.run([], {}, **{'term': 'README', 'files': [], 'paths': ['files', 'files2'], 'skip': True}) == []

# Generated at 2022-06-13 13:46:16.272907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock import modules
    import ansible.plugins.lookup
    import ansible.errors
    
    # Mock ansible.errors.AnsibleLookupError
    class MockAnsibleLookupError():
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
    ansible.errors.AnsibleLookupError = MockAnsibleLookupError

    # Mock ansible.plugins.lookup.LookupBase
    class MockLookupBase():
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing):
            return fn
    ans

# Generated at 2022-06-13 13:46:26.141360
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import inspect
    import os
    import sys
    import tempfile

    # create temporary directory
    tmp_dir = tempfile.mkdtemp(prefix='ansible_test_lookup_')
    local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    # create temporary file in temporary directory and write some text to it
    tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', dir=tmp_dir, delete=False)
    tmp_file.write('foobar')
    tmp_file.close()

    # add the temporary directory to sys.path
    sys.path.append(tmp_dir)

    # create temporary module in temporary directory, write some code to it
    tmp_module = tempfile.NamedTemporary

# Generated at 2022-06-13 13:46:34.590339
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # Create lookup object
    lookup = LookupModule()
    # Define common variables
    variables = {'role_path': '..', 'hostvars': {'somehost': {'inventory_hostname': 'somehost'}}}
    # Define test inputs and expected outputs

# Generated at 2022-06-13 13:46:48.590065
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase
    lookup_base = LookupBase()

    # setup arguments
    terms = []
    variables = {'inventory_hostname': 'hostname'}

    # setup test cases

# Generated at 2022-06-13 13:46:59.235508
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create objets for test
    lookup_module = LookupModule()
    lookup_module._subdir = 'files'
    # Test with no files
    terms = []
    variables = {}
    kwargs = {}
    with pytest.raises(AnsibleLookupError):
        lookup_module.run(terms, variables, **kwargs)
    # Test with one file
    terms = ['file_1', {'files': 'file_2', 'paths': 'path/to/files'}]
    variables = {}
    kwargs = {'files': 'file_1', 'paths': '', 'skip': False}
    lookup_module.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing: None if fn == 'file_1' else 'result'

# Generated at 2022-06-13 13:47:08.540958
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    #####
    # setup
    #####

    # pretend to be a task context
    class LookupModule_run_context:
        def __init__(self):
            self._subdir = 'files'

    class LookupModule_run_templar:
        def template(self, a):
            return 'emplate: ' + a

    class LookupModule_run_loader:
        pass

    # inputs

# Generated at 2022-06-13 13:47:33.741073
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_instance = LookupModule()
    # NOTE: the LookupModule_instance._templar is not set in the dummy test
    #       class, so all templates will be returned as not found (i.e. None)
    #       and any jinja2.exceptions.UndefinedError will be ignored.

    def _find_file_in_search_path(variables, subdir, fn, ignore_missing=False):
        if subdir != 'files':
            raise AnsibleLookupError("sorry, no other subdir supported, this is a mock")
        if fn in ['', 'foo', 'bar']:
            return fn
        # NOTE: any other template will be returned as not found (i.e. None)
        return None

    LookupModule_instance.find_file_in_search_path = _find_

# Generated at 2022-06-13 13:47:46.263470
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mocking params
    import mock

    # Mocking an object of class LookupBase
    # 1. Instantiation
    lookup_base_obj = LookupBase()

    # 2. Calling methods
    lookup_base_obj.set_options(var_options={}, direct={'skip': False, 'paths': [], 'files': []})
    lookup_base_obj.get_option('files')
    lookup_base_obj.get_option('skip')

    # 3. Mocking methods
    lookup_base_obj.get_option = mock.MagicMock(return_value=True)
    assert lookup_base_obj.get_option('skip') == True

    lookup_base_obj.set_options = mock.MagicMock(return_value=0)

# Generated at 2022-06-13 13:47:55.669000
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:47:58.998882
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = {'files': 'somefile.txt'}
    variables = {}
    os.path.exists = lambda a: True
    lookup.find_file_in_search_path = lambda a,b,c,d: 'somepath'
    assert lookup.run(terms, variables) == ['somepath']
    pass

# Generated at 2022-06-13 13:48:11.903230
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    display = Display()
    variable_manager = VariableManager(loader=DataLoader())
    variable_manager.extra_vars = {
        'cheese': 'cheddar',
        'directory':'/foo/bar'
    }

    mylookup = LookupModule(display)
    mylookup._subdir = 'files'

    # check with a file in current directory
    found_files = mylookup.run(terms=['testamatic.txt'], variables=variable_manager)[0]
    assert found_files == './testamatic.txt'

    # check with a list of files

# Generated at 2022-06-13 13:48:21.357031
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    try:
        lookup_module.run(terms = 0, variables = {})
    except AnsibleLookupError as e:
        e_message = str(e)
        # This message has been changed and is not backward compatible.
        # However, this check was never added to the test...
        #assert(e_message == "Invalid term supplied, can handle string, mapping or list of strings but got: <class 'int'> for 0")
        assert(e_message == "Invalid term supplied, can handle string, mapping or list of strings but got: <class 'int'>")

    try:
        lookup_module.run(terms = [0, 1, 2], variables = {})
    except AnsibleLookupError as e:
        e_message = str(e)
        # This message has been changed and is

# Generated at 2022-06-13 13:48:22.550821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 13:48:34.881681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup_instance = lookup_loader.get('first_found')

    # Case 1
    term = ['file_foo.txt']
    kwargs = dict()
    variables = dict()

    try:
        lookup_instance.run(terms=term, variables=variables, **kwargs)
    except AnsibleLookupError as e:
        assert e.message == "No file was found when using first_found."

    # Case 2
    term = ['file_foo.txt', dict(paths=[])]
    kwargs = dict()
    variables = dict()


# Generated at 2022-06-13 13:48:35.468501
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:48:44.810688
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import string_types

    lookup_obj = LookupModule()

    # Test for not string_types input
    result, _ = lookup_obj._process_terms(['a', 1], None, None)
    assert not result

    # Test for string_types input
    result, _ = lookup_obj._process_terms(['a'], None, None)
    assert isinstance(result, list)

    # Test for input format that is not supported explicitely
    result, _ = lookup_obj._process_terms({'a': 'b'}, None, None)
    assert not result

    # Test for a supported input format
    result, _ = lookup_obj._process_terms(['a', {'files': 'b', 'paths': 'src'}], None, None)

# Generated at 2022-06-13 13:49:14.077470
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    # to be finished

    # Act
    result = LookupModule.run()

    # Assert
    # to be finished

# Generated at 2022-06-13 13:49:23.416591
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    terms = ["/some/path/some_file"]
    variables = {}
    kwargs = {}
    res = lookup_module.run(terms, variables, **kwargs)

    assert res == ['/some/path/some_file']

    terms = ["not_existing_file"]
    variables = {}
    kwargs = {}

    try:
        lookup_module.run(terms, variables, **kwargs)
    except AnsibleLookupError:
        pass
    else:
        raise Exception('AnsibleLookupError not raised')

    terms = ["not_existing_file"]
    variables = {}
    kwargs = {'skip': True}
    res = lookup_module.run(terms, variables, **kwargs)

    assert res == []


# Generated at 2022-06-13 13:49:33.756382
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  terms = ['a']
  variables = {}
  kwargs = {}

  lookup_module = LookupModule()
  lookup_module._process_terms = lambda terms, variables, kwargs: (['b'], False)
  lookup_module.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing: 'c'

  assert lookup_module.run(terms, variables, **kwargs) == ['c']

  lookup_module._process_terms = lambda terms, variables, kwargs: (['d'], True)
  lookup_module.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing: None
  assert lookup_module.run(terms, variables, **kwargs) == []

# Generated at 2022-06-13 13:49:39.215271
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a variable to store arguments and expected return values of a call to the method
    test_args_expected_returns = {
        'no_file_found': {
            'args': [
                'foo',
                {'ANSIBLE_FILTER_PLUGINS': '/path/to/ansible/plugins/filter'}
            ],
            'expected_return': []
        },
        'file_found': {
            'args': [
                'ansible_facts',
                {'ANSIBLE_FILTER_PLUGINS': '/path/to/ansible/plugins/filter'}
            ],
            'expected_return': ['/path/to/ansible/plugins/filter/ansible_facts.py']
        },
    }

    # Test the run method of class LookupModule with the arguments and expected return values
    #

# Generated at 2022-06-13 13:49:50.064980
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # get instance of LookupModule with args and kwargs
    lookup = LookupModule(
        loader=None,
        templar=None,
        shared_loader_obj=None)

    # test real path
    lookup.basedir = '/tmp'
    assert lookup.run(['/tmp/mypath'], variables=dict()) == ['/tmp/mypath']

    # test env path
    assert lookup.run(['${HOME}'], variables=dict(HOME='/root')) == ['/root']

    # test file existing
    lookup.basedir = 'tests/lookup_plugins/'
    assert lookup.run(['first_found.py'], variables=dict()) == ['tests/lookup_plugins/first_found.py']

# Generated at 2022-06-13 13:50:00.195890
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    test_terms = [
        {
            'files': 'file1'
        },
        {'files': 'file2', 
            'paths': 'path1'
        },
        {
            'files': 'file3,file4',
            'paths': 'path2:path3;path4'
        }
    ]
    test_variables = {}
    test_kwargs = {}
    module._process_terms = lambda terms, variables, kwargs: (terms, variables, kwargs)
    module.run(test_terms, test_variables, **test_kwargs)
    assert module.run(test_terms, test_variables, **test_kwargs) == (test_terms, test_variables, test_kwargs)


# Generated at 2022-06-13 13:50:07.898919
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # NOTE: from docs
    #   Notes -
    #   This lookup can be used in 'dual mode', either passing a list of file names or a dictionary that has files and paths.
    testobj = LookupModule()

    ###############################################################################################
    # test: passing a list of file names
    ###############################################################################################
    terms = ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt']
    variables = {}
    kwargs = {}

    result = testobj._process_terms(terms, variables, kwargs)
    testobj.run(terms, variables, **kwargs)
    assert result

    ###############################################################################################
    # test: passing a dictionary that has files and paths
    ###############################################################################################

# Generated at 2022-06-13 13:50:14.382596
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    display.verbosity = 4
    lookup_plugin = LookupModule()

    terms = [
        {'files': 'file1', 'paths': 'path1'},
        {'files': 'file2', 'paths': 'path2'},
        {'files': 'file3', 'paths': 'path3'},
        {'files': 'file4', 'paths': 'path4'},
    ]

    fake_vars = dict(
        ansible_play_basedir='/home/test/playbook',
        ansible_inventory_basedir='/home/test/inventory',
    )


# Generated at 2022-06-13 13:50:23.694147
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Running unit test 'test_LookupModule_run'")
    # This test makes sure that the run function returns the first existing file in the specified list.
    # Create a LookupModule object
    lookup = LookupModule()

    # Create a list of files that need to be searched
    files_list = ['/etc/hosts', '/etc/ubuntu/hosts', '/etc/centos/hosts']

    # Create a dictionary with the keyword argument for the run function
    kw_dict = {'files': files_list, 'paths': ['/etc'], 'skip': True}

    # Return value from the run function
    run_result = lookup.run([], kw_dict)

    # Expected return value from the run function
    expected_result = ['/etc/hosts']


# Generated at 2022-06-13 13:50:33.252309
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create the instance of LookupModule class
    lm = LookupModule()

    # call run function with dummy arguments
    result = lm.run([], {})
    assert result == [], "Incorrect results"

    # call run function with dummy arguments
    result = lm.run([0], {})
    assert result == [], "Incorrect results"

    # call run function with dummy arguments
    result = lm.run([["files"]], {})
    assert result == [], "Incorrect results"

    # call run function with dummy arguments
    result = lm.run([["files"], ["paths"]], {})
    assert result == [], "Incorrect results"

    # call run function with dummy arguments
    result = lm.run([{'files': ["file1", "file2"]}], {})

# Generated at 2022-06-13 13:51:30.646718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule().run([{'files': ['foo', 'bar'], 'paths': ['/tmp/path1', '/tmp/path2']}, 'baz'], dict(), skip=True)

# Generated at 2022-06-13 13:51:38.948588
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The lookup file is expected to be found in the same directory as this file
    import os, sys
    lookup_file = os.path.join(os.path.dirname(__file__), "test_lookup_plugins", "test_lookup_first_found.py")
    sys.path.append(os.path.dirname(lookup_file))
    from test_lookup_first_found import LookupModule

    # Test method run of class LookupModule.
    # Requires the test variable "files" to be set to a list of existing files.
    # The test variable "files_not_found" specifies a list of non-existing files.
    # The test variable "paths" can be used to specify a list of directories.
    # Returns the path of the first file found.

# Generated at 2022-06-13 13:51:45.770050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        {
            'files': 'default.yml',
            'paths': 'vars'
        },
        {
            'files': '{{ ansible_os_family }}.yml',
            'paths': 'vars'
        },
        {
            'files': '{{ ansible_distribution }}.yml',
            'paths': 'vars'
        },
    ]
    variables = {}
    lookup = LookupModule()
    lookup.set_loader(None)

    result = lookup.run(terms, variables, skip=True)
    assert result == []

# Generated at 2022-06-13 13:51:59.568504
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.text.converters import to_text

    L = LookupModule()
    L._lookup_plugin_loaded([])

    ##
    # remap/reorder helpers
    import inspect
    def fake_template(string, variables):
        return string, variables

    def helper(name, args):
        args = list(args)

        # check for lookup call in first position
        # this needs to be removed
        try:
            if args[0] in ('lookup', 'query') and args[1] == 'first_found':
                args.pop(0)
                args.pop(0)
        except:
            pass

        func = getattr(L, name)