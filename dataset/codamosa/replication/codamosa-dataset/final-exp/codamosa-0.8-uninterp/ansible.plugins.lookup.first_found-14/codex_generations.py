

# Generated at 2022-06-13 13:42:10.924228
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:42:24.080071
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lm = LookupModule()
    # Unit tests can't use the self.inject method
    lm._templar = DummyTemplar()
    lm._loader = DummyLoader()
    results = lm.run(terms=[{"files": ["a", "b"],
                             "paths": ["/path/to/u/a", '/path/to/b']}],
                     variables={})
    assert results == ['/path/to/u/a/a']

    results = lm.run(terms=[{"files": ["a", "b"],
                             "paths": ["/path/to/u/a", '/path/to/b'],
                             "skip": True}],
                     variables={})
    assert results == []


# Generated at 2022-06-13 13:42:26.958901
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Test start")
    # TBD
    print("Test End")


if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:42:36.536284
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_terms = [
        ['files/testfiles/foo.txt', 'files/testfiles/bar.txt'],
        {'files': 'files/testfiles/foo.txt', 'paths': '/home/ansibull/ansible/test/units/module_utils/testfiles/files'},
        {'files': 'files/testfiles/bar.txt', 'paths': 'files/testfiles'},
        {'files': 'testfiles/foo.txt', 'paths': 'files/testfiles'},
        {'files': 'testfiles/bar.txt', 'paths': 'files/testfiles'}
    ]

    lookup_obj = LookupModule()

# Generated at 2022-06-13 13:42:47.266112
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Parameter files is absent from terms, so method returns empty list
    test_terms = [
        {
            'paths': '/usr/share/ansible',
            'skip': True
        }
    ]
    test_variables = { 'ansible_distribution': 'RHELE', 'ansible_os_family': 'RedHat' }
    test_kwargs = { }
    expected = []
    actual = LookupModule().run(test_terms, test_variables, **test_kwargs)
    assert actual == expected

    # Parameter paths is not absent from terms, but doesn't lead to a file that is found via find_file_in_search_path,
    # so method returns empty list

# Generated at 2022-06-13 13:42:57.247259
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # The following dictionaries are used to test the run method's behavior
    term_dict_1 = {
        "files": "foo.txt",
        "paths": "path/to"
    }
    term_dict_2 = {
        "files": "biz.txt",
        "paths": "path"
    }
    term_dict_3 = {
        "files": "foo",
        "paths": "path"
    }
    term_dict_4 = {
        "files": "foo",
        "paths": "to/path"
    }
    term_dict_5 = {
        "files": "foo.txt",
        "paths": "to/path"
    }

# Generated at 2022-06-13 13:43:09.446282
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: this is a strange and odd test, it tests only 'run'
    # and not the implementation of the templating engine which looks the same
    # and is the same between lookup and plugin.
    # it will be used as a test to refactor templating engine to be shared
    # between lookup & plugins and in the future add tests for 'lookup'
    # it also does not test class methods, even though it uses them

    assert (LookupModule.run.__module__ == 'ansible.plugins.lookup.first_found')

    # TODO: refactor with mock, as several method calls are defined in base

    # create plugin object
    PluginClass = LookupModule

    # create instance of plugin object
    PluginObj = PluginClass()

    # create mocks for templating engine
    TemplatingEngineClassMock = Lookup

# Generated at 2022-06-13 13:43:16.855408
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    t = {}
    t['terms'] = {'files': ['/path/to/foo.txt', 'bar.txt'],
                  'paths': ['/tmp/production', '/tmp/staging']}
    t['variables'] = {}
    t['kwargs'] = {}
    t['self'] = {'_subdir': 'files'}
    t['self']['_templar'] = {'template':(lambda x: str)}
    t['self']['find_file_in_search_path'] = (lambda x,y,z: str)

    # Exercise
    L = LookupModule()
    L._templar = t['self']['_templar']

# Generated at 2022-06-13 13:43:27.122689
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import PY2
    from ansible.lookup.builtin import LookupModule
    import sys

    # NOTE: see '_process_terms' for how a list is processed
    # the 'dict' option is for a single entry and can only be the first.
    # when this is the case, it's internal options can be set globally
    # but then any subsequent entries will reset those options back to default.
    # This is a minor design limitation that is here by default.

    lookup_mod = LookupModule()

    ############################################################################
    #### By passing a list of strings to the terms directly (without a dict) ####
    ############################################################################

    #################################
    #### files only, no paths ####
    #################################

    #### one file, absolute path ###
    assert lookup_mod

# Generated at 2022-06-13 13:43:38.790885
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test class
    class TestClass():

        def __init__(self, args):
            pass

        @classmethod
        def find_file_in_search_path(cls, variables, subdir, fn, ignore_missing):
            return 'filename'

    # Create a instance and set the attribute
    test_class = TestClass({})
    test_class._templar = TestClass({})
    test_class._subdir = 'files'
    test_class._templar.template = lambda x: 'filename'

    # Create a test function for test class
    def test_func():
        # Execute the run function, and assert the result
        result = test_class.run('terms', {}, **{})
        assert result == ['filename']


# Generated at 2022-06-13 13:43:43.957229
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test empty or dummy class
    assert True == True


# Generated at 2022-06-13 13:43:54.086053
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    # NOTE: all existing test use this import as a 'given'
    from ansible.utils.path import unfrackpath
    lookup_plugin = LookupModule()

    # Act and Assert
    # NOTE: use unfrackpath on __file__ as 'given' makes no sense
    result = lookup_plugin.run(terms=['ansible.cfg', 'doesnotexist'], variables=dict(_original_file=unfrackpath(__file__)), inject=dict(
        ANSIBLE_CONFIG=unfrackpath(__file__)
    ))
    assert result == [unfrackpath(__file__)]

# Generated at 2022-06-13 13:44:01.333356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupBase:
        def __init__(self, values):
            self.values = values

        def get_basedir(self, variables):
            return self.values['basedir']

        def find_file_in_search_path(self, variables, subdir, filename, ignore_missing):
            if subdir not in variables['basedir']:
                return None
            if filename not in variables['basedir'][subdir]:
                return None
            return variables['basedir'][subdir][filename]


# Generated at 2022-06-13 13:44:10.690501
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 13:44:15.647304
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO

    class FakeTemplar:
        def __init__(self):
            self._fail_on_undefined_errors = True
            self._available_variables = dict()
            self._fail_on_undefined_errors = True

        def set_available_variables(self, variables):
            self._available_variables = variables

        def template(self, template_str, convert_bare=True, preserve_trailing_newlines=True, escape_backslashes=True, fail_on_undefined=True):
            self._fail_on_undefined_errors = fail_on_undefined

# Generated at 2022-06-13 13:44:25.889674
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # 'files' is the list of file names to look for,
    # 'paths' is the list of paths in which to look for the files
    m = LookupModule().run
    assert m([{'files': 'foo.txt', 'paths': '/path/to'}], {}) == ['/path/to/foo.txt']
    assert m([{'files': 'foo.txt', 'paths': '/path/to'}, {'files': 'bar.txt'}], {}) == ['/path/to/foo.txt']
    assert m([{'files': 'foo.txt', 'paths': '/path/to'}, {'files': 'bar.txt'}, {'files': 'foo'}], {}) == ['/path/to/foo.txt']

# Generated at 2022-06-13 13:44:36.601162
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest
    from ansible.parsing.dataloader import DataLoader

    from units.mock.loader import DictDataLoader

    # This class is needed for the plugin to work
    class MockLookupPlugin(LookupBase):
        def __init__(self, loader):
            self._loader = loader

        def run(self, terms, variables=None, **kwargs):
            pass

    # initialize plugin
    lookup = MockLookupPlugin(DictDataLoader({}))

    # This is needed for the templating to work
    class MockVars(object):
        pass

    # initialize variables
    variables = MockVars()

    # Mock the templating function
    def mock_template(src):
        return src

    lookup._templar = MockVars()
    lookup._templar.template

# Generated at 2022-06-13 13:44:39.283288
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    # Require one parameter, a list of params
    # Return a list
    res = lookup_loader.get('first_found').run(terms=[{'files': 'foo', 'paths': '/path/to/data'}]) 
    assert len(res) == 1
    assert res[0] == '/path/to/data/foo'

# Generated at 2022-06-13 13:44:49.008270
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:45:00.374827
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup
    import ansible.template
    import ansible.vars
    import ansible.utils.path
    from ansible.utils.display import Display
    from ansible.module_utils._text import to_bytes

    display = Display()

    class FakeTemplar(ansible.template.Templar):
        def __init__(self):
            pass
        def template(self, fn):
            if isinstance(fn, string_types):
                return fn
            elif isinstance(fn, Mapping):
                return fn['files']
            return None

    # TODO: more tests of options, errorhandling, etc
    m = LookupModule()
    m._templar = FakeTemplar()
    m._display = display


# Generated at 2022-06-13 13:45:10.775398
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Given
    import os
    import tempfile
    dir0 = tempfile.mkdtemp()
    dir1 = tempfile.mkdtemp()
    dir2 = tempfile.mkdtemp()
    file0 = os.path.basename(tempfile.mkstemp(dir=dir0)[1])
    file1 = os.path.basename(tempfile.mkstemp(dir=dir1)[1])
    file2 = os.path.basename(tempfile.mkstemp(dir=dir2)[1])
    term0 = file0
    term1 = file1
    term2 = file2
    terms = [term0, term1, term2]

    set_options = LookupModule.set_options
    find_file_in_search_path = LookupModule.find_file_in_search_path

# Generated at 2022-06-13 13:45:19.086853
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    _input = ['/some/file/some_file', '/some/file/other_file']

    _subdir = 'files'

    _output = ['/some/file/some_file']

    _find_file_in_search_path = True

    test_object = LookupModule()
    test_object._subdir = _subdir

    test_object.find_file_in_search_path = lambda x1, x2, x3, x4: _find_file_in_search_path
    test_object._templar = {'template': lambda x: x}

    assert test_object.run(_input, {}) == _output



# Generated at 2022-06-13 13:45:30.529877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_params = dict(
        terms=[{'files': 'foo', 'paths': 'bar'},
               ['foobar', {'files': 'foo', 'paths': 'bar'}],
               ],
        variables=dict(
            ansible_playbook_python='python',
            ansible_playbook_python3='python3',
        ),
        **dict(
            ansible_playbook_python='python',
            ansible_playbook_python3='python3',
        ),
    )
    lookup_obj = LookupModule()

    results, skip = lookup_obj._process_terms(**lookup_params)
    assert len(results) == 5
    assert skip is False

    results.clear()

# Generated at 2022-06-13 13:45:39.652333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import pytest
    import tempfile
    from io import StringIO
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import configparser

    def _mktmppath(tmpdir, name, content=None):
        """Create a temporary file in tmpdir with given name,
        content and return the path to it.
        :param tmpdir: temporary directory to create the file
        :param name: file name to be created
        :param content: content for the file
        """

        fpath = os.path.join(str(tmpdir), name)
        fobj = open(fpath, "w")
        if content is not None:
            fobj.write(content)
        fobj.close()
        return fpath

    # Create a configuration file to

# Generated at 2022-06-13 13:45:51.318414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.find_file_in_search_path = lambda self, vars, subdir, fn, ignore_missing: fn

    expected_paths = ['first_list', 'second_list', 'first_other_list', 'second_other_list', 'single_term']

    # test single file
    testmodule = LookupModule()
    testmodule._subdir = 'testdir1'
    path = testmodule.run('single_file', variables={}, files='single_term')
    assert path == expected_paths

    # test list of files
    testmodule = LookupModule()
    testmodule._subdir = 'testdir1'
    path = testmodule.run(['first_file', 'second_file'], variables={}, files='first_list,second_list')
    assert path == expected_paths

   

# Generated at 2022-06-13 13:46:00.541066
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import shutil
    import tempfile
    import unittest

    class TestCase(unittest.TestCase):

        def setUp(self):
            self.tmp_path = tempfile.mkdtemp()

            # create a file tree

# Generated at 2022-06-13 13:46:13.197815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test for LookupModule._run.
    """
    # GIVEN: A LookupModule with a mocked _templar
    from ansible.utils.display import Display
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from jinja2.utils import soft_unicode

    mock_vars = {'total_search': [['']], 'skip': False, 'subdir': '', 'fn': '', 'path': '/path/to/file'}
    mock_stream = ''
    mock_environment_loader = ''

    dummy_env = object()
    dummy_loader = object()
    dummy_templar = object()

    display = Display()

# Generated at 2022-06-13 13:46:21.961956
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    import os
    import tempfile
    import shutil

    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            self.d1 = tempfile.mkdtemp()
            self.d2 = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.d1)
            shutil.rmtree(self.d2)

        def test_lookup_first_found_found_one(self):
            fn1 = os.path.join(self.d1, 'ansible')
            fn2 = os.path.join(self.d2, 'ansible')

            with open(fn1, 'w') as f:
                f.write('test')

# Generated at 2022-06-13 13:46:31.911479
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # File not found
    with pytest.raises(AnsibleLookupError):
        lookupModule = LookupModule()
        lookupModule.run(['./test/files/no_file'], [], [])

    # Existing file without error, without skip
    lookupModule = LookupModule()
    result = lookupModule.run(['./test/files/file1'], [], [])
    assert result[0] == './test/files/file1'

    # Existing file without error, with skip
    lookupModule = LookupModule()
    result = lookupModule.run([{'files': './test/files/file1', 'skip': True}], [], [])
    assert result[0] == './test/files/file1'

    # Existing file with error ignored, with skip
    lookupModule = Look

# Generated at 2022-06-13 13:46:45.183297
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    parser = LookupModule()
    assert parser._process_terms(['1.txt', '2.txt', '3.txt'], None, None) == [['1.txt', '2.txt', '3.txt'], False]
    assert parser._process_terms('a.txt,b.txt', None, None) == [['a.txt', 'b.txt'], False]
    assert parser._process_terms({'paths': '1.txt,2.txt'}, None, None) == [['1.txt', '2.txt'], False]
    assert parser._process_terms({'files': 'a.txt,b.txt'}, None, None) == [['a.txt', 'b.txt'], False]

# Generated at 2022-06-13 13:46:57.050716
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Object initialization
    lookup_plugin = LookupModule()
    # Test the run method

# Generated at 2022-06-13 13:47:07.827536
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:47:17.173532
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # iso_lookup = LookupModule()
    # x = iso_lookup.run('/home/test.txt', {"testing": False})
    # print x
    # assert x == ["/home/test.txt"]
    #
    # x = iso_lookup.run('/home/test.txt', {"testing": True})
    # print x
    # assert x == []

    iso_lookup = LookupModule()
    x = iso_lookup.run(['home/test.txt'], {})
    print(x)

    x = iso_lookup.run(['home/{{ test_var }}'], {"test_var": True})
    print(x)

    x = iso_lookup.run(['home/{{ test_var }}'], {"test_var": False})
    print(x)

# Generated at 2022-06-13 13:47:27.897442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Check first_found returns the first path of the first file inputted.
    terms = '/tmp/some_file'
    variables = dict()
    assert module.run(terms, variables) == ['/tmp/some_file']

    # Check first_found returns the first path of the first file inputted
    # and search for the file in the relative path.
    terms = 'some_file'
    assert module.run(terms, variables) == ['some_file']

    # Check first_found returns the first path of the first file inputted
    # and search for the file in the relative path and the list of paths.
    terms = 'some_file'
    module.set_options(var_options=variables, direct=dict(paths='/etc,/tmp'))

# Generated at 2022-06-13 13:47:35.941213
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._loader = None
    lookup._templar = None
    lookup._available_variables = None
    lookup._fact_cache = None
    lookup._lookup_args = None
    lookup._lookup_parameters = None
    lookup._plugin_data = None
    lookup._plugin_options = None
    lookup._search_path = None
    lookup._var_manager = None
    lookup._verbosity = None
    lookup._roles_path = None
    lookup._role_vars = None
    lookup._role_prefix = None
    lookup._task = None
    lookup._task_vars = None
    lookup._task_path = None
    lookup._tqm = None
    lookup._wrapper = None


# Generated at 2022-06-13 13:47:47.941400
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    class MockTemplar(object):
        def __init__(self, templar):
            self._templar = templar

        def template(self, *args, **kwargs):
            return self._templar.template(*args, **kwargs)

    class MockVars(object):
        def __init__(self, vars_):
            self._vars = vars_

        def get_vars(self, *args, **kwargs):
            return self._vars.get_vars(*args, **kwargs)

    file_mock = pytest.Mock()
    file_mock.exists = pytest.Mock(return_value=True)


# Generated at 2022-06-13 13:47:58.449404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialisation
    tests_dir = os.path.dirname(__file__)
    test_path = os.path.join(tests_dir, 'test_data', 'first_found')
    os.chdir(test_path)
    ansible_vars = {'playbook_dir': None, 'play_hosts': [], 'inventory_hostname': ''}
    lm = LookupModule()
    lm.set_loader(None)

    # Setup test data
    open('file1.txt', 'a').close()
    open('file1.txt', 'a').close()

    # Run tests

# Generated at 2022-06-13 13:48:11.590613
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # FIXME: replace with plugin unit tests
    m = LookupModule()

    # order of params is important here
    res = m.run([
        {'files': ['foo', 'bar'], 'paths': ['', 'a.b']},
        'biz',
        {'files': ['foo'], 'paths': ['a.b', 'a.c']}
    ])
    assert(res == ['foo'])

    res = m.run([
        {'files': ['foo', 'bar']},
        'biz'
    ])
    assert(res == ['foo'])

    # FIXME:
    # this should fail and raise an error, as 'files' and 'paths' are required
    # res = m.run([{}])


# Generated at 2022-06-13 13:48:21.092283
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Setup test
    lu = LookupModule()

    mock_variables = dict()

    # Test - ensure right error is thrown if param is not a list
    with pytest.raises(AnsibleLookupError) as excinfo:
        lu.run("Not a list", mock_variables)
    assert excinfo.value.message == "Invalid term supplied, can handle string, mapping or list of strings but got: <class 'str'> for Not a list"

    # Test - ensure no exception is raised if first item in param is not a list
    assert lu.run(["Not a list"], mock_variables) == []

    # Test - ensure right error is thrown if param list is empty
    with pytest.raises(AnsibleLookupError) as excinfo:
        lu.run([], mock_variables)


# Generated at 2022-06-13 13:48:33.313904
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._templar = None

    # no file inside first path: fail with error
    assert lookup.run(['a', 'b/c'], {}, files='foo.txt,bar.txt', paths='.,b') == []

    # file exists in first path: success
    assert lookup.run(['a', 'b/c'], {}, files='foo.txt,bar.txt', paths='fixtures/files,b')[0] == 'fixtures/files/foo.txt'

    # file exists in second path: success
    assert lookup.run(['a', 'b/c'], {}, files='foo.txt,bar.txt', paths='.,fixtures/files')[0] == 'fixtures/files/bar.txt'

    # file exists in first path, after a failure on

# Generated at 2022-06-13 13:49:00.038627
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # 1. test passing str
    terms = ['a file name', 'another file name']
    expected_result = ['a file name', 'another file name']
    assert expected_result == LookupModule().run(terms, None)[1]

    # 2. test passing dict with 'path'
    terms = [{'paths': 'a file name'}, {'paths': 'another file name'}]
    expected_result = ['a file name', 'another file name']
    assert expected_result == LookupModule().run(terms, None)[1]

    # 3. test passing dict with 'files'
    terms = [{'files': 'a file name'}, {'files': 'another file name'}]
    expected_result = ['a file name', 'another file name']

# Generated at 2022-06-13 13:49:07.044736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  # Test case 1 - valid use case
  variables = {}
  terms = [{'files': 'hosts', 'paths': '/etc/ansible'}]
  lookup = LookupModule()
  lookup._subdir = 'roles/dummy/files'
  lookup._templar = None
  lookup._finder = None
  result = lookup.run(terms, variables)
  assert result == ['/etc/ansible/hosts']

# Generated at 2022-06-13 13:49:08.389214
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: write me
    pass

# Generated at 2022-06-13 13:49:23.879717
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2

    lu = LookupModule()

    assert lu._split_on([u'a,b,c']) == [u'a', u'b', u'c']

    # NOTE: py2/py3 use different unicode names
    if PY2:
        assert lu._split_on([u'\u2019,\u2022,\u2019']) == [u'\u2019', u'\u2022', u'\u2019']
    else:
        assert lu._split_on([u'\u2019,\u2022,\u2019']) == [u'\u2019', u'\u2022', u'\u2019']


# Generated at 2022-06-13 13:49:33.796313
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    # test for case when '_subdir' is assigned and file is found

    lookup_module._subdir = 'files'
    lookup_module.find_file_in_search_path = lambda var: '/path/to/file'

    assert '/path/to/file' == lookup_module.run([{}], {})[0]

    # test for case when '_subdir' is assigned and file is not found

    lookup_module.find_file_in_search_path = lambda var: None

    # this case should rise an exception
    try:
        lookup_module.run([{}], {})
    except AnsibleLookupError:
        pass
    else:
        raise AssertionError

    # test for case when '_subdir' is assigned and 'skip' is set to True

# Generated at 2022-06-13 13:49:39.235209
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager._extra_vars = {'hello': 'world'}

    # construct
    lookup = LookupModule()
    lookup._templar = Templar(loader=None, variables=variable_manager)

    # tests
    assert lookup._process_terms(terms=['{{ hello }}'], variables=variable_manager._extra_vars, kwargs={'skip': True}) == (['world'], True)
    assert lookup._process_terms(terms=['{{ hello }}'], variables=variable_manager._extra_vars, kwargs={}) == (['world'], False)

# Generated at 2022-06-13 13:49:50.069687
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # test case run1
    lookup_module._templar = object()
    lookup_module._templar.template = lambda x: x
    lookup_module.find_file_in_search_path = lambda x, y, z: z
    assert lookup_module.run([{"files": ["foo"]}], {}) == ["foo"]

    # test case run2
    lookup_module._templar = object()
    lookup_module._templar.template = lambda x: 'foo'
    lookup_module.find_file_in_search_path = lambda x, y, z: None
    assert lookup_module.run([{}], {}) == ["foo"]

    # test case run3
    lookup_module.set_options = lambda arg1, arg2: None
    lookup_

# Generated at 2022-06-13 13:50:00.191206
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # ERROR test: no files and no paths
    with pytest.raises(AnsibleLookupError) as e:
       lu = LookupModule()
       lu.run(terms=['a'], variables={'lookup_file_write_perm': '0644'})
    assert 'No file was found when using first_found' in e.value.message

    # ERROR test: no files and paths
    with pytest.raises(AnsibleLookupError) as e:
       lu = LookupModule()
       lu.run(terms=[{'paths': ['/tmp']}], variables={'lookup_file_write_perm': '0644'})
    assert 'No file was found when using first_found' in e.value.message

    # ERROR test: files and no paths

# Generated at 2022-06-13 13:50:07.870347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from pprint import pprint as pp

    # basic test: we have multiple files to lookup
    lookup = LookupModule()
    lookup.set_loader(None)
    lookup.set_environment({'ansible_current_tasks': {'role': {'name': 'rolename'}}})
    files, skip = lookup._process_terms([['files1.txt', 'files2.txt'], {'paths': ['path1', 'path2']}], {}, {})

    assert 'files1.txt' in files
    assert 'files2.txt' in files
    assert 'path1/files1.txt' in files
    assert 'path1/files2.txt' in files
    assert 'path2/files1.txt' in files
    assert 'path2/files2.txt' in files

    # test with file_

# Generated at 2022-06-13 13:50:12.265551
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Test 1: Create object LookupModule when files list is empty
    Lookup_Module_obj =LookupModule()
    
     # get subdir if set by task executor, default to files otherwise
    path = Lookup_Module_obj.find_file_in_search_path(None, 'files', '/etc/passwd')

    # Prepare method arguments
    terms=[{'files':[]}]
    variables = None
    
    # Unittest for LookupModule
    try:
        result = Lookup_Module_obj.run(terms, variables)
        assert False
    except AssertionError:
        pass

# Generated at 2022-06-13 13:50:53.481201
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(direct={"files": ["foo", "ansible_virtualization_type", "bar"], "paths": ["/tmp/production", "/tmp/staging"]})
    lookup_module._templar = type('Templar', (), {'template': lambda self, foo: foo})
    lookup_module.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=False: None if fn == "bar" else fn
    lookup_module._subdir = "files"

    assert lookup_module.run(terms=[], variables={}) == ["foo"]
    assert lookup_module.run(terms=[], variables={'ansible_virtualization_type': 'kvm'}) == ["kvm"]


# Generated at 2022-06-13 13:51:07.837205
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock the lookup plugin
    class MockLookupModule(LookupModule):
        def __init__(self, *args, **kwargs):
            return

        def _process_terms(self, terms, variables, kwargs):
            return (["/file1.txt", "/file2.txt", "/file3.txt"], True)

        # This mock method is used to return a 'dummy' path for each term
        # This is to fake that the 'real' path of file exists.
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=True):
            if fn == "/file1.txt":
                return "file1.txt"
            elif fn == "/file2.txt":
                return "file2.txt"

# Generated at 2022-06-13 13:51:15.979547
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class TestClass(object):
        '''This is a test class'''

        class TestLookupModule(LookupModule):
            def __init__(self, data=None):
                self.data = data

            def run(self, terms, variables=None, **kwargs):
                self.data = super(TestClass.TestLookupModule, self).run(terms, variables, **kwargs)

        test_object = TestLookupModule()

        def __init__(self):
            self.test_object = TestClass.TestLookupModule()

    test_object = TestClass()

    class Params(object):
        '''This is a test class'''

        def __init__(self):
            self.test_data = dict()


# Generated at 2022-06-13 13:51:23.672362
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule().run(['vars/test1.yml', 'vars/test2.yml'], variables={
        'playbook_dir': 'test/playbooks',
        'playbook_parent_dir': 'test',
        'playbook_root': 'test/playbooks',
        'playbook_path': 'test/playbooks/main.yml',
        'ansible_file_name': 'main.yml',
        'ansible_modulename': 'main'
    })



# Generated at 2022-06-13 13:51:24.241718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:51:34.988267
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an object of class LookupModule
    lookup = LookupModule()
    # value of _templar of class LookupModule
    lookup._templar = {'template': 'Value'}
    # value of _subdir of class LookupModule
    lookup._subdir = {'_subdir': 'Value'}
    # value of find_file_in_search_path of class LookupModule
    lookup.find_file_in_search_path = []
    # value of find_file_in_search_path of class LookupModule
    lookup.find_file_in_search_path = ['Value1', 'Value2']
    # value of find_file_in_search_path of class LookupModule
    lookup.find_file_in_search_path = []
    # value of find_file_in_search

# Generated at 2022-06-13 13:51:45.168012
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import mock

    lookup_module = LookupModule()
    assert lookup_module is not None

    # Dummy options passed to templar to mock _load_vars or lookup_loader
    fake_options = mock.Mock()
    fake_options.lookup_loader = mock.Mock()

    # Make _find_file_in_search_path return True to simulate that the file was
    # found.
    lookup_module._find_file_in_search_path = mock.Mock(
        return_value=True)

    # Dummy variable list.
    variable_list = ['variable']

    # Dummy params in which the files do not exist.
    params = {'files': ['/fake/path1'], 'paths': ['/fake/path2']}


# Generated at 2022-06-13 13:51:59.325412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes

    lookup = LookupModule()

    # Set templar to get _subdir
    import jinja2
    from ansible.template import Templar
    lookup._templar = Templar(variables={}, loader=None)
    lookup._subdir = 'files'

    # mock find_file_in_search_path to do nothing.
    def noop(*args, **kwargs):
        return None
    lookup.find_file_in_search_path = noop

    # Create terms