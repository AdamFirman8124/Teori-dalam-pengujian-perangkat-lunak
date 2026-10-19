

# Generated at 2022-06-13 13:42:10.879841
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for valid input
    lm = LookupModule()

    terms = ['path/tasks.yaml', 'path/other_tasks.yaml']
    variables = {
        'ansible_current_instance': 'test_instance',
        'inventory_hostname': 'localhost'
    }
    kwargs = {
        'skip': True
    }
    path = lm.run(terms, variables, **kwargs)
    assert len(path) == 0

    terms = [{
        'files': 'path/tasks.yaml, path/other_tasks.yaml',
        'paths': 'path',
        'skip': False
    }]
    variables = {
        'ansible_current_instance': 'test_instance',
        'inventory_hostname': 'localhost'
    }


# Generated at 2022-06-13 13:42:25.644922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def f_get_option(self, key):
        return self.options[key]

    class FakeLookupModule(LookupModule):
        def __init__(self, *args, **kwargs):
            super(FakeLookupModule, self).__init__(*args, **kwargs)
            self.options = dict()

        def set_options(self, var_options, direct=None):
            if direct is not None:
                self.options.update(direct)

        def get_option(self, key):
            return self.options[key]


# Generated at 2022-06-13 13:42:28.871244
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([{'files': 'foo'}]) == ['foo']
    # TODO: add more tests

# Generated at 2022-06-13 13:42:37.427742
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ul = LookupModule()
    terms = [
        'a/b/c.cfg',
        {'paths': 'a/b/c'},
        ['a/b/c.cfg', 'a/b/c2.cfg'],
        {'files': ['a/b/c.cfg', 'a/b/c2.cfg'], 'paths': 'a/b/c'},
        'a/b/c.cfg', {'paths': ['a/b/c', 'a/b/c2'], 'skip': True},
        'a/b/c.cfg', {'paths': ['a/b/c', 'a/b/c2'], 'skip': False},
    ]
    variables = {}
    kwargs = {}

# Generated at 2022-06-13 13:42:48.992673
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1 -1
    lookup_module = LookupModule()
    lookup_module._templar = FakeTemplar()
    lookup_module.run(
        terms = [
            { 'files': ['file1', 'file2'] },
            { 'files': ['file3', 'file4'] },
            { 'files': ['file5', 'file6'] },
        ],
        variables = {},
        #kwargs = {}
    )
    result = lookup_module._templar.results
    assert result == [
        '/file1',
        '/file3',
        '/file5',
    ]

    # Test 1 -2
    lookup_module = LookupModule()
    lookup_module._templar = FakeTemplar()

# Generated at 2022-06-13 13:42:51.850282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run

    :return:
    """
    tm = LookupModule()
    tm._templar = None
    tm._loader = None
    tm.run([], {})

# Generated at 2022-06-13 13:43:00.027309
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.module_utils.six import PY3
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    lookup_plugin = LookupModule()

    if PY3:

        # unicode is only supported in Python 3
        # tests for str/unicode are done by using str() on unicode
        # which returns bytes, and bytes/non-unicode are the same type
        # as Python 3 has no separate bytes type
        fake_var = u'unicode_var_value'
    else:
        # Python 2 bytes have to be prefixed with 'b' to differentiate
        # from str, so they are equivalent to Python 3 bytes
        fake_var = 'bytes_var_value'
    fake_path = os.path.real

# Generated at 2022-06-13 13:43:11.261037
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Path to file with content: [path1:dir1, path2:dir2, file1]
    path_to_test_file = "./test_LookupModule_run/first_found_test.txt"

    # Path to file with content: [dir1/file1]
    path_to_file_found = "./test_LookupModule_run/file1"

    # Prepare for test
    # and create test files
    fh = open(path_to_test_file, "w")
    fh.write("path1:dir1\tpath2:dir2\tfile1")
    fh.close()

    fh = open(path_to_file_found, "w")
    fh.write("file1")
    fh.close()

    # Create instance of LookupModule
   

# Generated at 2022-06-13 13:43:23.545426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    filename = 'foobar.txt'
    filename1 = 'foobar1.txt'
    dirname = 'fake_dir'
    dirname1 = 'fake_dir1'
    dirname2 = 'fake_dir2'
    dirname3 = 'fake_dir3'
    dirname4 = 'fake_dir4'

    # 1st case: terms = filename
    lookup_module = LookupModule()
    lookup_module._subdir = dirname
    test_file = os.path.join(dirname, filename)
    assert_result = [test_file]
    assert lookup_module.run(terms=[filename]) == assert_result

    # 2nd case: terms = [filename, filename1]
    lookup_module = LookupModule()
    lookup_module._subdir = dirname

# Generated at 2022-06-13 13:43:25.060423
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Tests not implemented"

# Generated at 2022-06-13 13:43:39.682214
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Tests in this class are not complete. TODO: complete them.
    # TODO: Add tests with files and paths.
    # TODO: Add tests with a mix of types.
    # TODO: Add tests with an actual file in ansible_connection.

    # TODO: Mocking _process_terms could improve tests, as it is called twice
    # for each test case in LookupModule._run()
    class Test_LookupModule(LookupModule):
        def __init__(self):
            self._current_connection = None
            self._subdir = 'files'
            self._loader = None

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
            if fn == 'found':
                return 'bar'
            return None


# Generated at 2022-06-13 13:43:44.038904
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import the class/function to test
    from ansible.plugins.lookup.first_found import LookupModule
    # define needed functions/values that would normally exist outside of testing environment
    def find_file_in_search_path(variables, subdir, filename, ignore_missing=False):
        dir_list = ['/tmp/path/', '/fake/path/']
        fn_list = ['testfile', 'testfile2', 'testfile3']
        path_list = []
        for dir in dir_list:
            for fn in fn_list:
                path_list.append(os.path.join(dir, fn))
        if filename in path_list:
            return filename
        else:
            return None

    # set default values for testing
    terms = [
        'foo'
    ]
    variables = {}

# Generated at 2022-06-13 13:43:56.258567
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # This is integration test as it is testing whole class.
    # mock is used here as it is simple and it can mock instances of objects.
    # https://docs.python.org/3/library/unittest.mock.html
    # noinspection PyUnresolvedReferences
    import mock

    # we will mock 'find_file_in_search_path' method
    # noinspection PyUnresolvedReferences
    from ansible.plugins.lookup.first_found import LookupModule

    # noinspection PyUnusedLocal
    def side_effect(*args, **kwargs):
        if args[0] == "foo":
            return "/path/to/foo"
        elif args[0] == "bar":
            return None
        else:
            return None

    # noinspection PyUnusedLocal

# Generated at 2022-06-13 13:44:07.564662
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module_utils_path = os.path.join(os.path.dirname(__file__), '..', '..')
    if module_utils_path not in sys.path:
        sys.path.insert(0, module_utils_path)
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('first_found')

# Generated at 2022-06-13 13:44:22.281781
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # test no files given
    # assertRaisesRegexp is deprecated, but raises an AttributeError in Python 3
    # noinspection PyDeprecation
    assertRaisesRegexp(AnsibleLookupError,
                       'No file was found when using first_found.',
                       lookup.run, [], {})

    # test file not exists
    # assertRaisesRegexp is deprecated, but raises an AttributeError in Python 3
    # noinspection PyDeprecation
    assertRaisesRegexp(AnsibleLookupError,
                       'No file was found when using first_found.',
                       lookup.run, ['foo'], {}, basedirs=['/tmp/lookup_test'])

    # create test file

# Generated at 2022-06-13 13:44:27.334947
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _terms = ["/path/to/foo.txt", "/path/to/bar.txt"]
    _variables = {}
    _kwargs = {}
    _return = LookupModule().run(_terms, _variables, **_kwargs)
    assert _return == []


# Generated at 2022-06-13 13:44:37.409726
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import os
    import shutil
    from pathlib import Path

    test_dir = Path(tempfile.mkdtemp()).resolve()
    test_file1 = test_dir / 'test1'
    test_file2 = test_dir / 'test2'
    test_file3 = test_dir / 'test_dir' / 'test3'

    test_file1.touch(exist_ok=True)
    test_file2.touch(exist_ok=True)
    (test_file3.parent).mkdir(parents=True, exist_ok=True)
    test_file3.touch(exist_ok=True)


    # test non existing file
    none_file = test_dir / 'none'
    with tempfile.TemporaryDirectory() as module_dir:
        os.ch

# Generated at 2022-06-13 13:44:48.442753
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase

    def _templar_template(s):
        return s

    lookup = LookupModule()
    lookup._templar = MockTemplar()
    lookup._templar.template = _templar_template
    lookup._templar.available_variables = {}
    lookup._templar._fail_on_undefined = False

    assert lookup.run(terms=[], variables={}, files=[], paths=[]) == [], 'Failed to return empty list when no file was found.'

    lookup.find_file_in_search_path = MockFindFileInSearchPath()

    lookup.run(terms=[], variables={}, files=[], paths=[])

# Generated at 2022-06-13 13:44:59.970276
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test empty terms
    terms = []
    variables = {}
    kwargs = {}
    expected_results = []

    result = LookupModule(loader=None, basedir=None, **kwargs).run(terms, variables, **kwargs)
    assert result == expected_results, "Result should be {} but is: {}".format(expected_results, result)
    del result

    # Test empty variables
    terms = ["test_filename"]
    variables = {}
    kwargs = {}
    expected_results = []

    result = LookupModule(loader=None, basedir=None, **kwargs).run(terms, variables, **kwargs)
    assert result == expected_results, "Result should be {} but is: {}".format(expected_results, result)
    del result

    # Test term with skip=False and no filename

# Generated at 2022-06-13 13:45:01.368679
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:45:19.761543
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:45:31.545358
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    arguments = [
        # Terms
        [{'files': 'one.yml', 'paths': '/path/to/one'}],
        [{'files': '/path/to/two/two.yml'}],
        [{'files': 'three.yml', 'paths': '/path/to/three'}],
        [{'files': 'four.yml', 'paths': '/path/to/four/'}],
        # Variables
        {},
        # kwargs
        {}
    ]
    lookup_module = LookupModule()
    lookup_module.set_loader()
    mock_loader_constructor = 'ansible.plugins.loader.lookup.file.'

# Generated at 2022-06-13 13:45:40.189794
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: this is a hacky way of testing as it does not test YAML parsing
    # TODO: rewrite this to test term YAML parsing
    import sys
    import os
    import inspect
    import tempfile

    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    test_dir = os.path.realpath(os.path.join(current_dir, '..', '..', 'test_data'))
    test_file_path = os.path.join(test_dir, 'test_file')
    test_file = open(test_file_path, "w")
    test_file.write('foo\n')
    test_file.close()

    # this is a hack to reload the ansible.module_utils.

# Generated at 2022-06-13 13:45:51.719715
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class LookupModule_object(LookupModule):

        def __init__(self):
            self._subdir = 'files'
            self.list_of_results = []

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
            self.list_of_results.append(fn)
            if fn == '__notfound__':
                return None
            return fn

    # first test without skip option
    lookup_mod = LookupModule_object()


# Generated at 2022-06-13 13:46:02.767337
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_loader({'find_file_in_search_path': lambda variables, subdir, fn, ignore_missing=False: 'abcd'})
    assert(l.run(terms=['test1.yaml'], variables={}) == ['abcd'])
    l.set_loader({'find_file_in_search_path': lambda variables, subdir, fn, ignore_missing=False: False})
    try:
        l.run(terms=['test1.yaml'], variables={})
        assert(False)
    except AnsibleLookupError:
        pass

if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 13:46:15.975396
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test a single term
    assert LookupModule().run('bar.txt', dict()) == ['/etc/ansible/files/bar.txt']

    # Test a list of terms
    assert LookupModule().run(['bar.txt', 'foo.txt'], dict()) == ['/etc/ansible/files/bar.txt']

    # Test a list of terms with skip
    assert LookupModule().run(['bar.txt', 'foo.txt'], dict(), skip=True) == []

    # Test a single dict-term
    assert LookupModule().run(dict(files='bar.txt'), dict()) == ['/etc/ansible/files/bar.txt']

    # Test a single dict-term with path
    assert LookupModule().run(dict(files='bar.txt', paths='.'), dict()) == ['bar.txt']

# Generated at 2022-06-13 13:46:25.776712
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with dict term and dict kwarg
    l = LookupModule()
    l._templar = None
    total_search, skip = l._process_terms([{"files": "test.txt", "paths": ["path1", "path2"]}, {"files": "test2.txt", "paths": ["path3", "path4"]}], {}, {})
    assert len(total_search) == 4
    assert skip is False

    # test with dict term and list term
    total_search, skip = l._process_terms([{"files": "test.txt", "paths": ["path1", "path2"]}, "test2.txt"], {}, {})
    assert len(total_search) == 3
    assert skip is False

    # test with sliced list
    total_search, skip = l._process_terms

# Generated at 2022-06-13 13:46:33.898178
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    obj = LookupModule()

    #test that no files are passed into first_found with empty terms list
    # test that lookup fails when no files are found
    assert obj.run([], {}, files = [], paths = []) == [], "No files were passed into first_found, but it found a file."
    try:
        obj.run([], {}, files = [], paths = [])
        assert False
    except AnsibleLookupError:
        assert True

    # test that lookup fails when no files are found, but skip option is true
    # test that skip option works as a global
    assert obj.run([], {}, files = [], paths = [], skip = True) == [], "No files were passed into first_found, but it found a file."

# Generated at 2022-06-13 13:46:47.895318
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import PY3

    if PY3:
        from unittest import mock
    else:
        import mock

    class TestVariables(object):
        def __init__(self, ansible_virtualization_type, ansible_distribution, ansible_os_family):
            self.ansible_virtualization_type = ansible_virtualization_type
            self.ansible_distribution = ansible_distribution
            self.ansible_os_family = ansible_os_family

    lm = LookupModule()
    lm.set_loader({})
    lm.set_environment(TestVariables('docker', 'Debian', 'Debian'))

    fake_file_to_find = 'fake_file_to_find'
    fake_file_to_find_

# Generated at 2022-06-13 13:46:59.091071
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class AnsibleModuleMock(object):
        class AnsibleModuleMock(object):
            params = {}
        def __init__(self, file_args, params):
            self.params = params
            self.file_args = file_args
            self.fail = False
            self.fail_file = None

        def fail_json(self, msg):
            if self.fail_file in self.file_args:
                self.fail = True

    class TestLookupModule(LookupModule):
        _file_args = []
        _fail_file = []

        def __init__(self):
            pass

        @property
        def _templar(self):
            return self

        def template(self, fn):
            return fn


# Generated at 2022-06-13 13:47:13.024815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: add tests
    pass

# Generated at 2022-06-13 13:47:25.281290
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleLookupError
    from ansible.plugins.lookup import LookupBase

    class AnsibleVar(dict):

        def __getitem__(self, key):
            return dict.get(self, key, None)

    class AnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = AnsibleVar(params=kwargs)
            self.fail_json = lambda **kwargs: kwargs

    class LookupBaseClass(LookupBase):
        def find_file_in_search_path(self, variables, subdir, filename, ignore_missing=False):
            return filename

    class LookupModuleClass(LookupModule):
        def __init__(self, **kwargs):
            self._templar = AnsibleVar()
            self.set

# Generated at 2022-06-13 13:47:34.939357
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock class variables to avoid importing LookupBase and LookupError
    class LookupBase_mock(object):
        def __init__(self, *args, **kwargs):
            self._templar = '_templar'
        class _Templar(object):
            def __init__(self, *args, **kwargs):
                pass
            def template(self, template):
                return template
        class AnsibleLookupError(Exception):
            def __init__(self, err_msg):
                self.message = err_msg
            def __str__(self):
                return self.message
    global LookupBase
    LookupBase = LookupBase_mock

    # Mock class variables to avoid importing AnsibleError and AnsibleUndefinedVariable

# Generated at 2022-06-13 13:47:36.142376
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(None, None) == None

# Generated at 2022-06-13 13:47:48.087194
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create instance of LookupModule
    lookup_plugin = LookupModule()

    # Create test file for testing 'found'
    with open('test_run.txt', 'wb') as f:
        f.write("This is a test file")

    # Create list of files that will be searched
    terms = ["test_run.txt", "test_run_one.txt"]

    # Check that run returns path of file that is specified in list
    value = lookup_plugin.run(terms)
    assert value == ["test_run.txt"]

    # Create another file to test 'not found'
    with open('test_run_none.txt', 'wb') as f:
        f.write("This is another test file")

    # Create list of files that will be searched

# Generated at 2022-06-13 13:47:58.540129
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:48:11.634339
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # import main class
    from ansible.plugins.lookup import LookupModule

    # create main class object
    lookup_module_object = LookupModule()

    # initialize datastructures for the for-loop of the run method
    total_search = []
    skip = False

    # create a subdir object
    lookup_module_object._subdir = 'files'

    # create a find_file_in_search_path function object

    def find_file_in_search_path(variables, terms, ignore_missing):
        # we use a dummy function that just returns the last file
        return terms[-1]

    # set the function object to the find_file_in_search_path attribute of the lookup_module_object
    lookup_module_object.find_file_in_search_path = find

# Generated at 2022-06-13 13:48:12.613703
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.run()

# Generated at 2022-06-13 13:48:21.322839
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert LookupModule().run(['test1.txt', 'test2.txt', 'test3.txt'], {}, paths=['/home/vagrant/test']) == ['/home/vagrant/test/test1.txt']
    assert LookupModule().run(['test1.txt', 'test2.txt', 'test3.txt'], {}, paths=['/home/vagrant/test', '/home/vagrant/test2']) == ['/home/vagrant/test/test1.txt']
    assert LookupModule().run(['test4.txt', 'test5.txt', 'test6.txt'], {}, paths=['/home/vagrant/test', '/home/vagrant/test2']) == []


# Generated at 2022-06-13 13:48:33.913506
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test_run_with_list_and_dict_of_strings
    terms = [{'files': ['foo', 'bar'], 'paths': 'test'}]
    variables = {}
    kwargs = {}
    l = LookupModule()
    total_search, skip = l._process_terms(terms, variables, kwargs)
    assert ['test/foo', 'test/bar'] == total_search
    assert False == skip

    # test_run_with_list_of_dicts_and_strings
    terms = [{'files': ['foo', 'bar'], 'paths': 'test'}, 'foo', 'bar']
    variables = {}
    kwargs = {}
    l = LookupModule()
    total_search, skip = l._process_terms(terms, variables, kwargs)


# Generated at 2022-06-13 13:49:09.259638
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import sys
    import tempfile
    import pytest

    # create if they do not exist
    try:
        os.mkdir('/tmp/test/path/')
    except OSError as e:
        if e.errno != 17:     # 17: file exists
            raise e
    try:
        os.mkdir('/tmp/test/path2/')
    except OSError as e:
        if e.errno != 17:     # 17: file exists
            raise e
    try:
        os.mkdir('/tmp/test/lookup/')
    except OSError as e:
        if e.errno != 17:     # 17: file exists
            raise e


# Generated at 2022-06-13 13:49:19.491541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # Given
    terms = [
        {"files": "1.txt", "paths": "/opt/"},
        {"files": "2.txt", "paths": "/opt/"},
        {"files": ["a.txt", "b.txt", "c.txt"], "paths": ["/opt/"]},
        ["files=d.txt paths=/opt/", "files=e.txt paths=/opt/"],
        "files=f.txt paths=/opt/",
    ]
    variables = {}
    kwargs = {}

    # When
    obj = LookupModule()
    obj.find_file_in_search_path = find_file_in_search_path
    r = obj.run(terms, variables, **kwargs)

    # Then

# Generated at 2022-06-13 13:49:31.000038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Allocate instance of class LookupModule
    var_options = {'path': ['path1', 'path2', 'path3'], 'ext': '.conf'}
    look = LookupModule()

    # create a dict of form of terms
    term_dict = {'files': ['file1', 'file2', 'file3'], 'paths': ['path1', 'path2', 'path3'], 'ext': '.conf'}

    # create relative and none relative paths
    relative_paths = []
    relative_paths.append('test1.conf')
    relative_paths.append('test2.conf')

    non_relative_paths = []
    non_relative_paths.append('/test1.conf')
    non_relative_paths.append('/test2.conf')

    # call run

# Generated at 2022-06-13 13:49:31.598400
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:49:37.224939
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # test0
    # first_found:
    #  - a.yml
    #  - b.yml
    # paths:
    #   - path1
    #   - path2
    #
    # outputs = ['path1/a.yml','path2/a.yml','path1/b.yml','path2/b.yml']
    # return = ['path1/a.yml']
    #
    # test1
    # first_found:
    #  - a.yml
    #  - b.yml
    #
    # paths:
    #   - path1
    #   - path2
    #
    # outputs = ['a.yml','b.yml']
    # return = ['a.yml']
    #
    #

# Generated at 2022-06-13 13:49:48.771401
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    arg_dict = {
        'files': 'foo,bar',
        'paths': 'path1,path2',
        'skip': True
    }
    files = ','.join(arg_dict.keys())

    lookup = LookupModule()
    terms = [arg_dict]
    lookup.set_options(direct={'files': files})

    assert lookup._process_terms(terms, None, None)[0] == ['path1/foo', 'path2/foo', 'path1/bar', 'path2/bar']

    lookup.set_options(direct=None)

    assert lookup._process_terms(terms, None, None)[0] == ['foo', 'bar']


# Generated at 2022-06-13 13:49:55.685704
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import sys
    import unittest

    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_text

    ansible_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
    sys.path.append(ansible_path)
    from ansible import context
    from ansible.plugins.lookup import LookupBase

    # NOTE:
    # - to run this test, simply call ./hacking/test-module -m ./lib/ansible/plugins/lookup/first_found.py
    # - it does not check for errors, but will print out the files found when searching for test_*.txt
    # - on pyhton2 it will print errors, but the test will run


# Generated at 2022-06-13 13:50:08.307354
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.plugins.lookup.first_found import _split_on, LookupModule

    lookup_module = LookupModule()
    lookup_module._subdir = 'files'


# Generated at 2022-06-13 13:50:19.822423
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import shutil
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # Set up some mock data
    dummy_loader = DataLoader()
    dummy_inventory = InventoryManager(loader=dummy_loader, sources='')
    host = Host("test", dummy_inventory)

    # Set up some 'mock' objects for the lookup module

# Generated at 2022-06-13 13:50:32.250867
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO:
    # - use parametrized 'paths' & 'files' in dict term
    # - use 'list' parametrized for 'paths' & 'files' in dict term
    # - use 'var' parametrized for 'paths' & 'files' in dict term
    # - use 'const' parametrized for 'paths' & 'files' in dict term
    # - use 'global' parametrized for 'skip' in dict term
    # - use 'var' parametrized for 'skip' in dict term
    # - use 'const' parametrized for 'skip' in dict term

    lm = LookupModule()
    params = dict(paths=['/tmp/production', '/tmp/staging'], files=['foo', 'bar'], skip=False)


# Generated at 2022-06-13 13:51:35.527602
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._subdir = 'role/files'

    # test no errors raised when file is found
    def test_find_file_in_search_path(self, **kwargs):
        return 'role/files/file1'

    lookup_module.find_file_in_search_path = test_find_file_in_search_path
    assert lookup_module.run(terms=['file1'], variables={}) == ['role/files/file1']

    # test errors raised when file is not found
    def test_find_file_in_search_path(self, **kwargs):
        return None

    lookup_module.find_file_in_search_path = test_find_file_in_search_path

# Generated at 2022-06-13 13:51:45.319203
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = [{'files': 'hoge.txt'}]
    variables = {}
    _result = LookupModule().run(terms, variables)
    assert _result == []

    terms = [{'files': 'hoge.txt', 'paths': './test/test_first_found/test_files'}]
    variables = {}
    _result = LookupModule().run(terms, variables)
    assert _result == ['./test/test_first_found/test_files/hoge.txt']

    terms = [{'files': 'hoge.txt', 'paths': './test/test_first_found/test_files'},
             {'files': 'fuga.txt', 'paths': './test/test_first_found/test_files'}]
    variables = {}
    _result

# Generated at 2022-06-13 13:51:52.161914
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_run_provider = {
        "files": [
            "test_file",
            "test_file1"
        ],
        "paths": [
            "path"
        ],
        "skip": False
    }

    assert LookupModule().run(terms=[LookupModule_run_provider], variables={}) == []