

# Generated at 2022-06-13 13:42:07.949678
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mod = LookupModule()
    lookup_mod._loader = DictDataLoader({"/dev/null": "content"})
    lookup_mod._templar = DummyTemplar()

    # Test call with minimum params and no files found
    terms = ['/f1', '/f2', '/f3']
    variables = {'inventory_hostname': 'example.com'}
    with pytest.raises(AnsibleLookupError) as exec_info:
        lookup_mod.run(terms, variables)
    assert 'No file was found when using first_found.' in str(exec_info.value)

    # Test call with minimum params and one file found
    terms = ['/dev/null', '/f2', '/f3']
    variables = {'inventory_hostname': 'example.com'}
   

# Generated at 2022-06-13 13:42:14.252765
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # This is not a real test, just a quick way to check if the results are ok.
    # Expected result for example case is:
    # [u'/etc/ansible/hosts']
    #
    # The reason for this, is that the method run will change depending on the system
    return lookup.run([
        [u'/etc/ansible/hosts', u'/etc/hosts'],
        [u'/home/user/fake-hosts'],
        {
            u'files': u'dummy-hosts,hosts',
            u'paths': u'/etc/ansible,/etc,/tmp'
        }
    ])

# Generated at 2022-06-13 13:42:28.079480
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize a basic LookupModule object
    lookup_module = LookupModule()
    lookup_module._templar = None
    lookup_module._loader = None

    # mock call to find_file_in_search_path
    def find_file_in_search_path(vars, subdir, filename, ignore_missing):
        if filename.endswith('.txt'):
            return 'file.txt'
        if filename.endswith('.png'):
            return 'file.png'
        return None

    # mock call to _templar.template
    def templar_template(fn):
        return fn

    # no files or paths
    msg = "No file was found when using first_found."

# Generated at 2022-06-13 13:42:36.876341
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm._templar = lm._loader.load_basedir(os.path.dirname(__file__))
    # test that _process_terms is called
    with pytest.raises(AnsibleLookupError):
        lm.run([''])
    # test that no file is found
    with pytest.raises(AnsibleLookupError):
        lm.run([{'files': 'foo.yml', 'paths': './bar'}], variables=dict())
    # test that file found is returned
    assert lm.run([{'files': 'lookup_plugins.py', 'paths': './library'}], variables=dict()) == ['./library/lookup_plugins.py']
    # test that file found is returned
    assert l

# Generated at 2022-06-13 13:42:39.877429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Only for coverage purpose
    result = LookupModule().run(['test', dict(files='test_1')])
    assert result == []

# Generated at 2022-06-13 13:42:50.479965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestTemplar:
        def __init__(self):
            self.__data = dict()

        def template(self, path):
            return self.__data[path]

    class TestVariables:
        def get_vars(self, play=None, task=None, hostvars=None):
            return {'role_path': '/path/to/role'}

    class TestLookupBase:
        def __init__(self):
            self.__data = dict()

        def find_file_in_search_path(self, variables, subdir, path, ignore_missing):
            return self.__data[path]

    p = LookupModule(loader=None)

    tt = TestTemplar()
    p._templar = tt

# Generated at 2022-06-13 13:42:59.016227
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def assert_raises_lookup_plugin_error(*args, **kwargs):
        try:
            LookupModule.run(*args, **kwargs)
        except AnsibleLookupError:
            pass
        except Exception:
            print("AnsibleLookupError is not raised")

    def assert_raises_lookup_error(*args, **kwargs):
        try:
            LookupModule.run(*args, **kwargs)
        except AnsibleLookupError:
            print("AnsibleLookupError is raised")
        except Exception:
            pass

    lookup_module = LookupModule()
    terms = [{'files': 'foo.txt', 'paths': './relative/path'}]
    variables = {'inventory_hostname': 'localhost'}

    # test invalid term type
    assert_ra

# Generated at 2022-06-13 13:43:10.697586
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create files for testing
    import tempfile
    import shutil
    from os import mkdir
    from os.path import join
    import os
    import stat

    testdir = tempfile.mkdtemp()

    paths_dict = {}


# Generated at 2022-06-13 13:43:23.500358
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: these are set to run with 'test_basic'
    # adding this to test its behaviour
    from ansible.plugins.lookup.basic import LookupModule as lm

    # Tests for class LookupModule
    # Unit tests for method run of class LookupModule
    class Args(object):
        def __init__(self, params):
            for k, v in params.items():
                setattr(self, k, v)

    class Variables(object):
        def __init__(self):
            self._data = {}

        def get(self, key, default=None):
            return self._data.get(key, default)

        def set(self, key, value):
            self._data[key] = value

    class Templar(object):
        def template(self, string):
            return string



# Generated at 2022-06-13 13:43:36.087510
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  #pylint: disable=missing-docstring
  #pylint: disable=protected-access
  #pylint: disable=redefined-variable-type
  #pylint: disable=too-many-locals
  #pylint: disable=too-many-statements
  #pylint: disable=unused-variable

  lookup_mock = LookupModule()

  option_kwargs = dict(
      files=['foo', 'bar'],
      paths=['/var/tmp', '/etc'],
      skip=False
  )
  lookup_mock.set_options(**option_kwargs)

  # test with sequences
  files = ['a', 'b']
  paths = ['c', 'd', 'e']
  terms = ['f', 'g']
  result = lookup_mock

# Generated at 2022-06-13 13:43:47.334710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._subdir = 'files'
    # create an empty 'self.find_file_in_search_path' method to avoid 'not implemented' error
    lookup_module.find_file_in_search_path = lambda *a: None
    # create an empty 'self.set_options' method to avoid 'no _templar variable' error
    lookup_module.set_options = lambda *a: None
    # create an empty 'self._templar.template' method to avoid 'no _templar variable' error
    lookup_module._templar = type('', (), {})()
    lookup_module._templar.template = lambda *a: None


# Generated at 2022-06-13 13:43:57.965830
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:44:08.332445
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Test_LookupBase:
        def __init__(self, subdir):
            self._subdir = subdir

        def find_file_in_search_path(self, variables, subdir, filename, ignore_missing=False):
            return subdir + '/' + filename

    class Test_Templar:
        def template(variable):
            return "template/" + variable

    test_instance = LookupModule(None, Test_Templar(), None)
    test_instance.__class__.set_options = LookupModule.set_options

    # Test without any parameters
    result = test_instance.run(None, None)
    assert result == []

    # Test with empty file list
    result = test_instance.run([{}], None)
    assert result == []


# Generated at 2022-06-13 13:44:18.208717
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test run method of class LookupModule
    '''

    # Test with terms as dict
    terms = {'files': 'foo', 'paths': 'bar'}
    variables = 'baz'

    # create an instance of LookupModule
    l = LookupModule()
    l.get_basedir = lambda **kwargs: 'test'
    l._find_file_in_path = lambda **kwargs: 'test'

    # mock find_file_in_search_path method
    def find_file(variables, subdir, fn, ignore_missing):
        '''
        Test find_file_in_search_path method
        '''
        return fn

    l.find_file_in_search_path = find_file

    # mock templar.template method
    l._templar

# Generated at 2022-06-13 13:44:27.834005
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    # call run method with empty terms
    result = lookup.run(terms=[], variables=dict())
    assert result == [], "Call run method with empty terms returned %s is not valid" % result

    # call run method with terms as a list
    result = lookup.run(terms=['foo', 'bar'], variables=dict())
    assert result == [], "Call run method with terms as a list returned %s is not valid" % result

    # call run method with terms as a dict containing files and paths
    result = lookup.run(terms=[{'files': 'foo', 'paths': 'bar'}], variables=dict())
    assert result == [], "Call run method with terms as a dict containing files and paths returned %s is not valid" % result

    # call run method with terms as a dict containing files and

# Generated at 2022-06-13 13:44:37.681183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO

    lookup = LookupModule()
    lookup.set_loader()

    def test_lookup(subdir, ext):
        path = subdir + ext
        lookup._subdir = subdir
        ret = lookup.run(terms=path, variables=None, **{})
        assert ret[0] == path

    fn = 'unit_test/foo.txt'
    base_dir = os.path.dirname(__file__)
    test_lookup(subdir='files', ext=fn)

    lookup._subdir = 'files'
    terms = ['unit_test/a.txt']
    ret = lookup.run(terms=terms, variables=None, **{})

    lookup = LookupModule()
    lookup.set_loader()
    lookup.set_basedir

# Generated at 2022-06-13 13:44:48.475504
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    from ansible import context
    from ansible.context import CLIContext
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # Need to setup a context for this
    context._init_global_context(CLIContext())
    context._set_global_context(context.CLIContext())

    templar = Templar(loader=None, variables=VariableManager())

    # This is a special case of the run method.
    # The lookup_plugin object is empty.
    # The result is []
    lookup_plugin = LookupModule()
    lookup_plugin._templar = templar
    terms = "foo"

# Generated at 2022-06-13 13:45:00.015529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    import shutil
    lookup = LookupModule()

    # setup files and paths to search
    files_list = [os.path.basename(tempfile.NamedTemporaryFile(prefix='lookup_first_found').name),
                  os.path.basename(tempfile.NamedTemporaryFile(prefix='lookup_first_found').name),
                  os.path.basename(tempfile.NamedTemporaryFile(prefix='lookup_first_found').name)]

    tests_dir = tempfile.mkdtemp(prefix='lookup_first_found')
    lookup.set_options(var_options={}, direct={'_filesdir': tests_dir})

    paths = []

# Generated at 2022-06-13 13:45:09.420424
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run(
        ['foo.txt', 'bar.txt', 'baz.txt'],
        dict(ansible_env=dict(ANSIBLE_LOOKUP_PLUGINS='/tmp/ansible/plugins/lookup:/etc/ansible/plugins/lookup'))
    )
    assert result == []

# Generated at 2022-06-13 13:45:18.803958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest.mock as mock
    kwargs = {}
    kwargs['files'] = ['file', 'file1']
    def mock_lookup_file_in_search_path_path(arg1, arg2, arg3, arg4):
        if arg3 == 'file':
            return '/file'
        return None
    with mock.patch.object(LookupModule,"lookup_file_in_search_path") as mock_method:
        mock_method.side_effect = mock_lookup_file_in_search_path_path
        lookup = LookupModule()
        ret = lookup.run('unused', 'unused', **kwargs)
        assert ret == ['/file']


# Generated at 2022-06-13 13:45:34.353404
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import tempfile
    from ansible.utils.path import unfrackpath

    # variables used in unit tests only and defined by test framework
    # t_module_utils_path  # path to dir containing module_utils, can be overridden by test framework
    # t_files_path   # path to dir containing files dir to read vars, can be overridden by test framework
    # t_vars_path  # path to dir containing vars dir to read vars, can be overridden by test framework

    test_dir = os.path.dirname(os.path.abspath(__file__))
    # make full paths relative to this test dir, since getting called via load_module
    # so all paths should be relative to this test, otherwise they will be relative to
    # lib/ansible/module_utils/
    t_

# Generated at 2022-06-13 13:45:41.597286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    path = lookup_module.run(terms=['missing_file.txt'], variables={})[0]
    assert path is None

    lookup_module = LookupModule()
    path = lookup_module.run(terms=['missing_file.txt'], variables={}, skip=True)[0]
    assert path is None

    lookup_module = LookupModule()
    path = lookup_module.run(terms=['missing_file.txt'], variables={}, skip=False)[0]
    assert path is None

    lookup_module = LookupModule()
    path = lookup_module.run(terms=['FIRST_FOUND_LOOKUP.rst'], variables={})[0]
    assert path == 'FIRST_FOUND_LOOKUP.rst'


# Generated at 2022-06-13 13:45:52.430538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {}
    lookup = LookupModule()

    # Test 1: No file is found, raise an error
    kwargs = {'terms':
              [
                  {'files': 'foo.txt', 'paths': 'path1'},
                  {'files': 'foo.txt', 'paths': 'path2'}
              ]
              }
    try:
        lookup.run(**kwargs)
    except Exception as e:
        assert('No file was found when using first_found.' in str(e))

    # Test 2: Found a single file
    lookup.find_file_in_search_path = lambda variables, subdir, filename, ignore_missing: 'path1/foo.txt' if filename == 'path1/foo.txt' else None

# Generated at 2022-06-13 13:46:03.651175
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _module_runner(module, *args, **kwargs):
        """helper to create a LookupModule object and run the run() method"""
        obj = module(*args, **kwargs)
        ret = obj.run(args[1:], kwargs)
        return ret

    # double check that _process_terms has been refactored correctly i.e.
    # as expected the global settings will be clobbered when passed inline.
    # This is tested as that is the behaviour before and was unintentional.
    # This may be a feature, but it should be documented otherwise is a general source of confusion
    global_settings = {
        'skip': False,
        'files': ['/tmp/foo'],
        'paths': ['/tmp/foo/path', '/tmp/bar'],
    }


# Generated at 2022-06-13 13:46:14.421166
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Instantiation of LookupModule
    class LookupModuleDummy(LookupModule):
        def __init__(self, role_params):
            self.role_params = role_params
            self._subdir = 'files'
    lookuper = LookupModuleDummy(role_params=None)
    total_search, skip = lookuper._process_terms(['role_params'], variables={}, kwargs={'role_params': {'files': ['file1', 'file2'], 'skip': False}})
    assert total_search == [
        'file1', 'file2'
    ]
    assert skip == False
    # test_LookupModule_run()

# Generated at 2022-06-13 13:46:21.038967
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Parameters
    terms=[{'files': ['foo', 'bar', 'biz'], 'paths': ['/tmp/production', '/tmp/staging']},
            '/path/to/foo.txt',
            '/path/to/biz.txt',
            'bar.txt'
           ]
    variables={}
    # Expected results
    expected_run_results=[None]
    # Using lookup module
    results=LookupModule().run(terms, variables)
    # Printing results
    print(results)
    # Asserting results
    assert results == expected_run_results


# Generated at 2022-06-13 13:46:31.523364
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test single string term
    lookup = LookupModule()
    result = lookup.run(terms = ['test.txt'])
    assert result == ['/path/to/test.txt']
    # Test multiple string terms
    result = lookup.run(terms = ['test.txt', 'other.txt'])
    assert result == ['/path/to/test.txt']
    # Test string term with dict
    result = lookup.run(terms = ['test.txt', {'files': 'other.txt'}])
    assert result == ['/path/to/test.txt']
    # Test string term with dict
    result = lookup.run(terms = ['notagoodfile.txt', {'files': 'other.txt'}])
    assert result == ['/path/to/other.txt']

# Generated at 2022-06-13 13:46:45.753210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing method run of class LookupModule
    # Since we are unit testing, we must first create an instance of PathLookup to set up some of the variables in class LookupBase
    # Imports
    import ansible.plugins.lookup.first_found
    reload(ansible.plugins.lookup.first_found)
    from ansible.plugins.lookup.first_found import LookupModule
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.six import string_types
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # Create an instance of VariableManager (vm)
    vm = VariableManager()

    # Create an instance of Templar (templar)
    templar = Templar(loader=None, variables=vm)

    # Create an instance of Ansible

# Generated at 2022-06-13 13:46:55.477841
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    terms = [
        {
            'files': 'foo.txt',
            'paths': 'vars',
            'skip': False
        },
        {
            'files': 'bar.txt',
            'paths': 'vars',
            'skip': False
        },
        {
            'files': 'biz.txt',
            'paths': 'vars',
            'skip': False
        }
    ]
    result = lookup.run(terms, dict())

    assert result == ['vars/foo.txt']

# Generated at 2022-06-13 13:47:05.946850
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils._text import to_bytes

    # Create a valid object for the LookupModule object
    obj = LookupModule()

    # Data for file './tests/unit/lib/ansible/modules/test_file.txt'
    obj._DICT_1 = {'files': ['test_file.txt'], 'paths': ['./tests/unit/lib/ansible/modules/']}
    # Data for file './tests/unit/lib/ansible/modules/test_file1.txt'
    obj._DICT_2 = {'files': ['test_file1.txt'], 'paths': ['./tests/unit/lib/ansible/modules/']}
    # Data for file './tests

# Generated at 2022-06-13 13:47:18.839590
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(LookupModule().run([], {}))

# Generated at 2022-06-13 13:47:27.203347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize test parameters
    terms = [
        {'files': 'foo', 'paths': 'DirA;DirB'},
        'file2',
        {'files': 'foo2', 'paths': 'DirC'},
    ]
    variables = 'var'
    find_file_in_search_path_return = './DirA/foo'

    # Mock only the methods of class LookupModule that use external resources
    lookup_mock = LookupModule()
    lookup_mock.find_file_in_search_path = Mock(return_value=find_file_in_search_path_return)

    # Call the tested method and assert its result
    actual_result = lookup_mock.run(terms, variables)
    expected_result = ['./DirA/foo']

# Generated at 2022-06-13 13:47:35.652953
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup a class to test with
    class LookupModule_RUN(LookupModule):
        """
        LookupModule used for testing
        """

        def _find_file_in_search_path(self, _1, _2, fn, _3=False):
            if fn in ['notfound.txt']:
                return None
            if fn in ['found.txt']:
                return 'found.txt'
            return 'invalid-val'

    lookup_plugin = LookupModule_RUN()
    lookup_plugin._subdir = 'files'

    # test a single value
    with pytest.raises(AnsibleLookupError):
        lookup_plugin.run(terms='notfound.txt')

    # test a list
    assert lookup_plugin.run(terms=['notfound.txt']) == []


# Generated at 2022-06-13 13:47:47.750746
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import tempfile
    import os
    from ansible.module_utils.six import PY3
    from ansible.plugins.loader import lookup_loader
    from ansible.module_utils.six.moves import builtins

    # Create two files for test purposes
    temp_dir = tempfile.gettempdir()
    fd, f1p = tempfile.mkstemp(dir=temp_dir)
    fd, f2p = tempfile.mkstemp(dir=temp_dir)

    f1p = os.path.join(temp_dir, f1p).replace('\\', '/')
    f2p = os.path.join(temp_dir, f2p).replace('\\', '/')

    f1p = os.path.normpath(os.path.abspath(f1p))
    f

# Generated at 2022-06-13 13:47:58.315728
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test method run of class LookupModule
    :return: None
    """
    import tempfile
    import os

    terms = []
    variables = {}
    kwargs = {}

    file1 = tempfile.NamedTemporaryFile(delete=False)
    file1.close()
    terms.append({'files': file1.name, 'paths': ''})

    file2 = tempfile.NamedTemporaryFile(delete=False)
    file2.close()
    terms.append({'files': file2.name, 'paths': ''})

    lookup = LookupModule()
    result = lookup.run(terms, variables, **kwargs)

    os.unlink(file1.name)
    os.unlink(file2.name)

    assert result == [file1.name]

# Generated at 2022-06-13 13:48:11.497192
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test 1
    from ansible.parsing.dataloader import DataLoader

    lu = LookupModule()
    lu._loader = DataLoader()
    lu._templar = lu._loader.load_from_file('/etc/hosts')
    lu._basedir = os.getcwd()
    lu._subdir = 'files'

    files = []
    files.append(os.path.join(os.getcwd(), "test-trafaret.yaml"))
    files.append("/etc/hosts")

    terms = []
    terms.append(files)

    total_search, skip = lu._process_terms(terms, None, None)
    print("total_search: %s" % total_search)
    print("skip: %s" % skip)


# Generated at 2022-06-13 13:48:21.016728
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['first_file.txt', 'second_file.txt', {'files': ['file.txt'], 'paths': ['.'], 'skip': True}]
    variables = {'ansible_virtualization_type': 'docker'}

    lookup_plugin = LookupModule()
    lookup_plugin._subdir = 'files'
    lookup_plugin._loader = None
    lookup_plugin._templar = None

    assert lookup_plugin.run(terms, variables) == ['first_file.txt']

    terms = ['first_file.txt', 'second_file.txt', {'files': ['file.txt', 'files/file.txt'], 'paths': ['.']}]

    lookup_plugin = LookupModule()
    lookup_plugin._subdir = 'files'
    lookup_plugin._loader = None
    lookup_

# Generated at 2022-06-13 13:48:33.228612
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test for method run of class LookupModule"""
    import os
    import sys
    import shutil
    test_dir = os.path.join(os.path.dirname(__file__), '../../')
    test_dir = os.path.abspath(test_dir)
    os.chdir(test_dir)
    sys.path.insert(0, test_dir)
    test_directory_name = 'LookupModuleTest-Run'
    test_directory_path = os.path.join(os.path.sep, *test_directory_name.split('/'))
    test_path = os.path.join(test_dir, test_directory_path)
    # Create test directory
    if not os.path.exists(test_path):
        os.makedirs(test_path)

# Generated at 2022-06-13 13:48:43.600022
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with no skip and no values
    terms = []
    variables = {}
    lookup = LookupModule()

    with pytest.raises(AnsibleLookupError):
        lookup.run(terms, variables)

    # Test with no skip and empty values
    terms = [{'files': [], 'paths': []}]
    variables = {}
    lookup = LookupModule()

    with pytest.raises(AnsibleLookupError):
        lookup.run(terms, variables)

    # Test with no skip
    terms = [{'files': ['value'], 'paths': ['value']}]
    variables = {}
    lookup = LookupModule()
    assert lookup.run(terms, variables) == ['value']

    # Test with skip

# Generated at 2022-06-13 13:48:54.083910
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
    lm = LookupModule()

    #
    # method _process_terms
    #
    # first test only passing kwargs
    params = {'paths': '/tmp/',
              'files': 'foo.txt,bar.txt',
              'skip': True}
    args = []
    total_search, skip = lm._process_terms(args, {}, params)
    assert isinstance(total_search, list)
    assert len(total_search) == 2
    assert total_search[0] == '/tmp/foo.txt'
    assert total_search[1] == '/tmp/bar.txt'
    assert skip is True

    # test passing a list in args, should append to total_search
    total_search, skip = l

# Generated at 2022-06-13 13:49:14.775616
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)
    variable_manager._hostvars = {'localhost': {'role': 'test', 'role_path': 'test/files'}}

    templar = Templar(loader=loader, variable_manager=variable_manager, lookups=C.DEFAULT_LOAD_CALLBACK_PLUGINS)

    # Test `run` without arguments, the expected result is a
    # AnsibleLookupError exception


# Generated at 2022-06-13 13:49:23.928849
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock objects
    mock_variables = {}
    mock_kwargs = {}
    mock_kwargs['files'] = ['foo', 'bar', 'biz']
    mock_kwargs['paths'] = ['/tmp/production', '/tmp/staging']
    mock_kwargs['skip'] = False

    # Create the first object, expecting 3 items: ['a', 'b', 'c']
    terms = ['a', 'b', 'c']
    lookup_module = LookupModule()
    result = lookup_module.run(terms, mock_variables, **mock_kwargs)
    assert result == ['a', 'b', 'c']

    # Create the second object, expecting 6 items: ['foo', 'foo', 'bar', 'bar', 'biz', 'biz']

# Generated at 2022-06-13 13:49:24.628879
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Tests not implemented"

# Generated at 2022-06-13 13:49:34.194070
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Ensure no file is found if no file is passed
    lookup = LookupModule()

    class TestModule(object):
        def __init__(self):
            self.params = []

    class TestVarManager(object):
        def get_vars(self, load_any_vars=False):
            return dict()

    # Test simulate params
    test_module = TestModule()
    test_var_manager = TestVarManager()
    test_terms = [dict(files=[], paths=[])]

    # Assert error
    try:
        lookup.run(test_terms, test_var_manager, test_module)
    except AnsibleLookupError as e:
        assert str(e) == 'No file was found when using first_found.'

    # Ensure no file is found if wrong file is passed
    # Test simulate params

# Generated at 2022-06-13 13:49:47.689811
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Unit testing for the run method of LookupModule '''

    # Create an instance of LookupModule
    lookup_module = LookupModule()

    # Create a dictionary that represents argspec for the run method
    argspec = {
        'terms': [{
            'files': ['foo'],
            'paths': ['bar'],
            'skip': True
        }]
    }

    # Set args for the run method
    args = ['', argspec, None]

    # Execute the run method
    result = lookup_module.run(*args)

    # Assert the result is what you expect
    assert result == [], \
    'Result "%s" is not what was expected: %s' % (result, [])

    # Reset the args
    args = ['/path/to/foo', {}, None]

   

# Generated at 2022-06-13 13:50:03.835251
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    lookup_module._templar = None

    lookup_module.set_options(var_options={}, direct={})
    assert lookup_module.get_option('files') == []
    assert lookup_module.get_option('paths') == []
    assert lookup_module.get_option('skip') == False

    lookup_module.set_options(var_options={}, direct={'files': 'foo.txt', 'paths': "myfiles", 'skip': True})
    assert lookup_module.get_option('files') == 'foo.txt'
    assert lookup_module.get_option('paths') == "myfiles"
    assert lookup_module.get_option('skip') == True

    # The dict option is saying 'here is some configuration' but:
    # - it will not be

# Generated at 2022-06-13 13:50:05.446711
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: add real tests for this as it is currently not tested
    pass

# Generated at 2022-06-13 13:50:07.717412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(
        terms = [
            'example_without_path'
        ],
        variables = {},
        **{}
    )
    assert result == [ 'example_without_path' ]


# Generated at 2022-06-13 13:50:19.781269
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # config to use in all tests
    kwargs = dict(files=(('file1', 'file2'), 'file3'), paths='/some/path')

    # test when no path
    terms = ['some_file']
    test_run = LookupModule().run(terms, {}, **kwargs)
    assert test_run == ['/some/path/some_file'], 'Could not get file with no path'

    # test when empty path
    terms = ['/some_file']
    test_run = LookupModule().run(terms, {}, **kwargs)
    assert test_run == ['/some_file'], 'Could not get file without'

    # test when no path and a file with a coma
    terms = ['data,some_file']

# Generated at 2022-06-13 13:50:32.256116
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # Test all the conditions with different types of term
    terms = [{"files": ["file1","file2"], "paths": ["path1","path2"]}, {"files": "file3", "paths": "path3"}, ["file4"], "file5"]
    path = module.find_file_in_search_path({"_original_file": "abc.yml", "_original_dir": "tmp"}, "files", "file1")
    assert path == "/tmp/path1/file1"
    path = module.find_file_in_search_path({"_original_file": "abc.yml", "_original_dir": "tmp"}, "files", "file2")
    assert path == "/tmp/path2/file2"

# Generated at 2022-06-13 13:51:08.685593
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader

    # Test using a dict as parameter
    param = {'files': ['/path/to/foo.txt', '/path/to/bar.txt'],
             'paths':['/etc/pam.d'],
             #'skip': True
            }
    lookup_module = plugin_loader.get('first_found')
    result = lookup_module.run([param])
    assert isinstance(result, list)

    # Test using a list as parameter
    param = ['/path/to/foo.txt', '/path/to/bar.txt',
             param] # using the same dict as before
    lookup_module = plugin_loader.get('first_found')
    result = lookup_module.run([param])
    assert isinstance(result, list)

    # Test using

# Generated at 2022-06-13 13:51:16.557253
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import shutil
    import tempfile
    import unittest

    class First_Found_TestCase(unittest.TestCase):
        def setUp(self):
            super(First_Found_TestCase, self).setUp()
            self.test_dir = tempfile.mkdtemp()

        def tearDown(self):
            super(First_Found_TestCase, self).tearDown()
            shutil.rmtree(self.test_dir)

        def test_basic_files(self):
            l = LookupModule()
            l._templar = DummyTemplar()

            path = os.path.join(self.test_dir, 'foo')
            os.mkdir(path)

# Generated at 2022-06-13 13:51:28.172348
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import re
    import os
    import sys

    # mock
    class MockTempalte(object):
        def __init__(self):
            self.answers = {}
        def template(self, value):
            # return vars.get(value, value)
            return self.answers[value]

    # This test is a bit contrived as the Jinja templating is not tested
    # but it was designed to get the basic functionality correct that is
    # used in all first_found lookup plugins.
    LookupModule.get_basedir = lambda self, variables: variables['basedir']


# Generated at 2022-06-13 13:51:36.770925
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    class OptionsModule(object):
        def __init__(self, var_options, direct):
            self.var_options = var_options
            self.direct = direct

    class TemplarModule(object):
        def template(self, fn):
            return fn

    options = { 
        "files": ["A", "B", "C"],
        "paths": ["P1", "P2"]
    }
    terms = [OptionsModule(0, options)]
    variables = []

    l = LookupModule()
    l._templar = TemplarModule()
    l.check_for_collections = False

    # Test
    assert l.run(terms, variables) == []

    # Teardown

# Generated at 2022-06-13 13:51:46.177784
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeVars
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get("first_found")

    # path to this file
    file_path = os.path.realpath(__file__)
    file_dir = os.path.dirname(file_path)

    # path to test files
    test_dir = os.path.join(file_dir, "test_first_found")
    test_file1 = os.path.join(test_dir, "hello.txt")
    test_file2 = os.path.join(test_dir, "hello2.txt")

# Generated at 2022-06-13 13:51:59.721635
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockLookupModule(LookupModule):

        def _split_on(terms, spliters=','):

            # TODO: fix as it does not allow spaces in names
            termlist = []
            if isinstance(terms, string_types):
                for spliter in spliters:
                    terms = terms.replace(spliter, ' ')
                termlist = terms.split(' ')
            else:
                # added since options will already listify
                for t in terms:
                    termlist.extend(_split_on(t, spliters))

            return termlist

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):

            return fn
