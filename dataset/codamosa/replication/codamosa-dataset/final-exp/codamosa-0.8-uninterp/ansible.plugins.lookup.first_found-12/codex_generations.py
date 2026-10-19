

# Generated at 2022-06-13 13:42:12.288176
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run([["file1", "file2", "file3"]], {})
    assert result == [("file1", "file2", "file3")]

    result = lookup.run([{"files": ["file1", "file2", "file3"], "paths": ["path1", "path2", "path3"]}], {})
    assert result == [("file1", "file2", "file3")]

    result = lookup.run(["file"], {})
    assert result == ["file"]

    result = lookup.run([{"files": "file1,file2,file3", "paths": "path1:path2:path3"}], {})
    assert result == [("file1", "file2", "file3")]


# Generated at 2022-06-13 13:42:26.572273
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    templar = Templar(loader=None)
    lookup._templar = templar

    # Test exception with empty list
    try:
        lookup.run([], {})
    except AnsibleLookupError as exception:
        assert str(exception) == "No file was found when using first_found."

    # Test exception with invalid term
    try:
        lookup.run([{}, 2], {})
    except AnsibleLookupError as exception:
        assert str(exception) == 'Invalid term supplied, can handle string, mapping or list of strings but got: <type \'int\'> for 2'

    # Test exception with empty dictionary

# Generated at 2022-06-13 13:42:29.369620
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule.
    """
    # TODO: This is a stub, implement properly.
    assert True

# Generated at 2022-06-13 13:42:39.406413
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run([], {}) == [], "Empty path list must return empty list"
    assert lookup.run("dummy", {}) == [], "Empty path list must return empty list"
    assert lookup.run("dummy", {}, skip=True) == [], "Empty path list must return empty list"
    assert lookup.run("dummy", {}, files="dummy", skip=True) == [], "Empty path list must return empty list"
    assert lookup.run("dummy", {}, files="dummy", paths='file:dummy', skip=True) == [], "Empty path list must return empty list"

# Generated at 2022-06-13 13:42:50.137605
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Test the plugin lookup get_contents() method '''
    # Test the run() on a file that exists
    test_terms = '''
    - files:
        - file1
        - file2
    - files:
        - file2
        - file3
        - file4
    - files:
        - file1
        - file2
    - files:
        - file1
        - file2
        - file3
      paths:
        - test1
        - test2
    - files:
        - file2
        - file3
        - file4
      paths:
        - test2
        - test3
    - files:
        - file1
        - file2
      paths:
        - test1
        - test2
        skip: true
      '''


# Generated at 2022-06-13 13:42:54.564868
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import _LookupModuleProcessor
    args = [["files/foo.txt"], {"_ansible_no_log": True}]
    processor = _LookupModuleProcessor(args, loader=None)
    assert LookupModule(processor).run(args[0], args[1]) == ["files/foo.txt"]

# Generated at 2022-06-13 13:43:06.129320
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupTypes = {
        'first_found': LookupModule,
    }
    l = LookupModule()
    import ansible.plugins.loader as plugin_loader
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', 'lookup_plugins'))
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', 'vars_plugins'))


# Generated at 2022-06-13 13:43:15.421481
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    files_dir = os.path.join(os.path.dirname(__file__), 'files')
    lookup_module = LookupModule()

    # test regular usage
    assert lookup_module.run(['{{ lookup_file_name }}'], dict(lookup_file_name='test_lookup_file.txt'), wantlist=True) == ['%s/%s' % (files_dir, 'test_lookup_file.txt')]
    assert lookup_module.run(['%s/%s' % (files_dir, 'test_lookup_file.txt')], dict(), wantlist=True) == ['%s/%s' % (files_dir, 'test_lookup_file.txt')]

    # test compound usage

# Generated at 2022-06-13 13:43:26.398168
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Options:
        def __init__(self, variables, direct=None):
            self.var_options = variables
            if direct:
                self.direct = direct

    class Variables:
        def __init__(self, variables):
            self.var = variables

    class SearchPath:
        def __init__(self, search_path):
            self.search = search_path

    class FindFile:
        def __init__(self, found_file=None):
            self.found = found_file

    variables = {
        'ansible_virtualization_type': 'test_system',
        'ansible_distribution': 'test_distro',
        'ansible_os_family': 'test_family',
        'inventory_hostname': 'test_host',
    }

# Generated at 2022-06-13 13:43:38.391606
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _test_run(params_in, searchpath=None):
        class MockTemplar(object):
            def __init__(self):
                self.template_data = {
                    'ansible_virtualization_type': 'kvm',
                    'ansible_distribution': 'ubuntu',
                    'ansible_os_family': 'debian',
                    'inventory_hostname': 'local'
                }
                self.environment = None

            def template(self, param):
                return self.template_data.get(param, param)

        class MockLoader(object):
            def __init__(self):
                self.path_segment_to_paths = {
                    'files': searchpath
                }

        lookup_plugin = LookupModule()
        lookup_plugin._templar = MockTemplar()
        lookup

# Generated at 2022-06-13 13:43:49.573059
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader

    # create special instance with fake 'files' subdir
    loader = DataLoader()
    lookup = lookup_loader._create_lookup_plugin('first_found', loader=loader)
    lookup._subdir = 'files'

    # 'first_found' plugin can be called in many ways, this tests the 'classic' call
    # passing a list of _terms

# Generated at 2022-06-13 13:43:59.383522
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock class module_utils.lookup_plugins.LookupBase
    class MockLookupBase(LookupBase):
        def __init__(self, loader, path, data=None):
            return None
        def find_file_in_search_path(self, variables, subdir, filename, ignore_missing=False):
            return True

    # Mock class ansible.template.Template
    class MockTemplate(object):
        def __init__(self, *args, **kwargs):
            return None
        def template(self, *args, **kwargs):
            return files

    # Mock class ansible.parsing.dataloader.DataLoader
    class MockDataLoader(object):
        def __init__(self, *args, **kwargs):
            return None

    # Mock class ansible.vars.manager.

# Generated at 2022-06-13 13:44:14.407930
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test that when no files are found, the correct error is raised
    templar = DummyTemplar()
    lookup_module = LookupModule(templar=templar)
    try:
        lookup_module.run([], {})
    except AnsibleLookupError:
        pass
    else:
        raise Exception("Error not raised")

    # test that a single file is found
    templar = DummyTemplar()
    lookup_module = LookupModule(templar=templar)
    filenames = ["/a/b/foo.txt"]
    templar.template_results = {
        "/a/b/foo.txt": "/a/b/foo.txt"
    }

# Generated at 2022-06-13 13:44:25.537831
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.loader import lookup_loader
    lookup = lookup_loader.get('first_found')

    test_data_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_data',
    )
    test_data_paths = [
        '',
        test_data_path,
        os.path.join(test_data_path, 'search_path'),
        os.path.join(test_data_path, 'files'),
    ]

    # Test without searchpath without error, only file is found

# Generated at 2022-06-13 13:44:29.716023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # no file is found
    terms = ['file1', 'file2']
    files = ['file1']
    paths = ['path1', 'path2']
    variables = dict()
    assert lookup.run(terms, variables) == list()

# Generated at 2022-06-13 13:44:38.654066
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyVars(object):
        def __init__(self, values):
            self.values = values

        def get(self, key, default=None):
            return self.values.get(key, default)

    class DummyTempalte(object):
        def __init__(self):
            self.template_data = None

        def template(self, data):
            self.template_data = data
            return data

    class DummyLookupBase(object):
        def __init__(self):
            self.options = {}
            self.var_options = None

        def set_options(self, var_options=None, direct=None):
            self.var_options = var_options
            self.options = direct


# Generated at 2022-06-13 13:44:48.805531
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # define file for test
    testfile1 = '/tmp/test1.txt'
    testfile2 = '/tmp/test2.txt'
    testfile3 = '/tmp/test3.txt'

    # create test file
    with open(testfile1, 'w') as f:
        f.write('test')
    with open(testfile2, 'w') as f:
        f.write('test')
    with open(testfile3, 'w') as f:
        f.write('test')

    #
    # test find first existing file using list of files
    #
    l = LookupModule()

    # test basic call without any paths
    files = [testfile1, testfile2]
    result = l.run(files, {})
    assert result == [testfile1]

    # test call with

# Generated at 2022-06-13 13:45:00.219499
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os

    # imports for test
    from ansible.errors import AnsibleLookupError

    from units.mock.loader import DictDataLoader

    from ansible.parsing.dataloader import DataLoader

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # test cases, expected result, input parm values
    test_cases = dict()

    # test case 1
    test_cases[1] = {'test_results': [],
                     'test_input': {'terms': [],
                                    'variables': {}, 'kwargs': {},
                                    'files': [], 'paths': [], 'skip': False}}

    # test case 2

# Generated at 2022-06-13 13:45:14.237263
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # FIXME: ouch, this is ugly and a huge hack, maybe a loop?
    files = [
        'foo',
        'bar',
        {
            'files': 'foo,bar',
            'paths': 'bar,foo',
            'skip': True
        },
        {
            'files': 'foo,bar',
            'paths': 'bar,foo'
        },
        {
            'files': 'foo,bar',
            'paths': 'bar,foo',
            'skip': True
        }
    ]

    paths = [
        '.',
        './files'
    ]

    # this is kind of a weird case, is it undefined or empty?
    undefined = './files/foo'

    search_paths = []

# Generated at 2022-06-13 13:45:22.135918
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    mock_path = "/path/to/file"
    mock_ids = ["12","34"]

    for mock_id in mock_ids:

        # Mock class instantiation
        lookup = LookupModule()
        lookup._loader = mock.MagicMock()
        lookup._templar = mock.MagicMock()

        # Mock find file in search path
        lookup._loader.path_dwim = mock.MagicMock(return_value=mock_path)

        # Test run method
        path = lookup.run([mock_id],None,None)

        assert path
        assert path[0] == mock_path
        assert lookup._loader.path_dwim.call_count == 1

    # Test exception
    lookup = LookupModule()
    lookup._loader = mock.MagicMock()
    lookup._templar

# Generated at 2022-06-13 13:45:34.824537
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_native

    import io
    import pytest

    class TemporaryDirectory():
        """
        Create and return a temporary directory.  This has the same
        behavior as mkdtemp but can be used as a context manager.  For
        example:

            with TemporaryDirectory() as tmpdir:
                ...

        Upon exiting the context, the directory and everything contained
        in it are removed.
        """

        def __init__(self, suffix="", prefix="tmp", dir=None):
            import tempfile
            self.name = tempfile.mktemp(suffix, prefix, dir)
            self._closed = False

        def __repr__(self):
            return "<{} {!r}>".format(self.__class__.__name__, self.name)


# Generated at 2022-06-13 13:45:35.982795
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO
    pass


# Generated at 2022-06-13 13:45:42.313650
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.errors import AnsibleError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 13:45:52.876964
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    files = ["bar", "baz", "foo"]
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.errors import AnsibleLookupError
    from ansible.plugins.loader import lookup_loader

    lookup_first_found = lookup_loader.get('first_found')

    # Test inputs
    # Test case 1: terms, variables are None
    terms = None
    variables = None
    result, skip = lookup_first_found._process_terms(terms, variables, {})
    assert result == [] and skip == False

    # Test case 2: terms is a dictionary, variables is None

# Generated at 2022-06-13 13:46:02.236726
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader(get_loader(dict(hostvars=dict(
        host1=dict(ansible_distribution='Debian'), host2=dict(ansible_distribution='CentOS')))))
    assert lookup_module.run([dict(files=dict(
        files=['{{ ansible_distribution }}', '{{ ansible_os_family }}', 'default'],
        paths=['vars']))]) == ['vars/Debian', 'vars/CentOS', 'vars/default']

# Generated at 2022-06-13 13:46:13.096979
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subdir_old = LookupModule._subdir
    try:
        LookupModule._subdir = 'files'
        assert LookupModule.run(terms=['/tmp/file', {'files': 'file2', 'paths': '/tmp'}, '/tmp/file3']) == ['/tmp/file']

        LookupModule._subdir = 'paths'
        assert LookupModule.run(terms=['/tmp/file', {'files': 'file2', 'paths': '/tmp'}, '/tmp/file3']) == ['/tmp/file3']
    finally:
        LookupModule._subdir = subdir_old

# Generated at 2022-06-13 13:46:21.910315
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    # NOTE: this is 'dummy' code and plenty more cases can be added

    # if 'search' structure is not a list, raise as this is code error
    l.run(42, {}) # raises AnsibleLookupError

    # any dicts in the search will be set as options
    assert l.run([{'files':'bar'}, {'files': 'foo'}], {}) == ['bar'] # first entry wins

    # lists of strings will be concatinated
    assert l.run([['foo'], ['bar']], {}) == ['bar']

    # strings are not checked for templates
    assert l.run(['foo'], {}) == ['foo']

    # this also requires working 'find_file_in_search_path'

# Generated at 2022-06-13 13:46:31.872422
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given
    lm = LookupModule()

# Generated at 2022-06-13 13:46:44.441443
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import hashlib
    test_paths = ['/path/to/testing', '/path/to/files', '/path/to/directory']
    test_files = ['testfile.txt', 'testing.conf', 'testfile', 'test.txt', hashlib.md5(b'bacon').hexdigest()]

    parameters = {'files': test_files, 'paths': test_paths}

    lookup = LookupModule()
    result = lookup.run(parameters)
    assert result == ['/path/to/testing/testfile.txt', '/path/to/files/testing.conf', '/path/to/directory/testfile', '/path/to/directory/test.txt', '/path/to/directory/' + hashlib.md5(b'bacon').hexdigest()]

# Generated at 2022-06-13 13:46:50.423219
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    lookup.set_loader(dict(path=""))

    # _split_on
    assert _split_on('list1,list2', ',') == ['list1', 'list2']
    assert _split_on('list1;list2', ';') == ['list1', 'list2']
    assert _split_on('list1:list2', ':') == ['list1', 'list2']
    # only use first spliter in list
    assert _split_on('list1;list2', ';,') == ['list1', 'list2']

    # general test
    assert len(lookup.run([''], dict())) < 1

    # skipping files
    kwargs = dict(skip=True)

# Generated at 2022-06-13 13:47:03.964996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    fake_variables = dict()
    fake_term = { 'files': 'foo', 'paths': 'bar' }
    fake_term_expanded = [ 'bar/foo' ]

    lookup_plugin = LookupModule()
    lookup_plugin._subdir = 'files'
    result = lookup_plugin.run([ fake_term ], fake_variables)
    assert result == fake_term_expanded


# Generated at 2022-06-13 13:47:15.149822
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock class LookupBase
    class LookupBaseMock:

        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing=False):
            return "test"

        def set_options(self, var_options, direct):
            return

        def get_option(self, key):
            return True

        def _templar(self):
            return True
            # Mock class Templar
            class TemplarMock:

                def template(self, fn):
                    return fn
            return TemplarMock()

    # Mock class LookupBase returning 'test' when calling find_file_in_search_path with 'test'

# Generated at 2022-06-13 13:47:25.745526
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    data = {'files': ['foo', 'bar'], 'paths': ['/tmp/production', '/tmp/staging']}
    terms = [{'files': ['foo', 'bar'], 'paths': ['/tmp/production', '/tmp/staging']},
             {'files': ['foo', 'bar'], 'paths': ['/tmp/production', '/tmp/staging']},
             [{'files': ['foo', 'bar'], 'paths': ['/tmp/production', '/tmp/staging']},
              {'files': ['foo', 'bar'], 'paths': ['/tmp/production', '/tmp/staging']}]
             ]

    # TODO: find a way to be able to create and load a config to use as options/vars

    l = LookupModule()
    l.set_options

# Generated at 2022-06-13 13:47:35.202220
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    lookup_module = LookupModule()
    lookup_module._templar = Templar()
    lookup_module._templar.available_variables = {}
    terms = ["something.yml", "somethingelse.yml"]
    result = lookup_module.run(terms, {})
    assert result is not None
    assert result == []
    terms = [{'files': 'something.yml'}]
    result = lookup_module.run(terms, {})
    assert result is not None
    assert result == []
    terms = [
        {'files': 'something.yml', 'paths': '/etc/ansible/something/roles'},
        {'files': 'something.yml', 'paths': '/etc/ansible/something/playbooks'},
    ]


# Generated at 2022-06-13 13:47:47.471524
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _run(terms, variables, **kwargs):
        lookup_instance = LookupModule()
        return lookup_instance.run(terms, variables, **kwargs)

    # no files
    assert [] == _run(terms=[], variables={})

    # empty string file and no paths
    assert [] == _run(terms=['', ''], variables={})

    # one string file and no paths
    assert [] == _run(terms=['test'], variables={})

    # one string file and empty string path
    assert [] == _run(terms=['test'], variables={}, paths='')

    # one string file and empty list path
    assert [] == _run(terms=['test'], variables={}, paths=[])

    # one string file and empty tuple path

# Generated at 2022-06-13 13:47:58.138800
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import os
    import shutil
    import tempfile
    import unittest
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup.first_found import LookupModule

    class TestFirstFoundModule(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()
            self.workdir = os.path.join(self.tmpdir, 'workdir')
            os.mkdir(self.workdir)


# Generated at 2022-06-13 13:48:11.349593
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase

    lookup_mod = LookupModule()
    lookup_base = LookupBase()

    fn_dict = {"files": "/path/to/file", "paths": "/path/to/path1,/path/to/path2"}
    terms = [fn_dict] # list of dictionaries

    # test with empty search paths
    lookup_base = LookupBase()
    lookup_base._loader = MockLoader(["test_1", "test_2", "test_3"])
    assert lookup_base.find_file_in_search_path({"my_vars": "my_value", "_ansible_tmp_dir_name": "test_1"}, "files", "test_2", ignore_missing=True) == "test_2"

    # test with two search paths

# Generated at 2022-06-13 13:48:20.860322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._subdir = 'files'

    # Mockup for find_file_in_search_path method
    def mockup_find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        if fn == 'first_ok':
            return fn
        elif fn == 'not_found':
            return None
        else:
            raise AnsibleLookupError("test_LookupModule_run error")

    lookup_module.find_file_in_search_path = mockup_find_file_in_search_path

    # Test without options
    lookup_terms = ['first_ok', 'not_found']
    result = lookup_module.run(lookup_terms, {})
    assert result == ['first_ok']

    # Test

# Generated at 2022-06-13 13:48:32.989702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins.loader import lookup_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.display import Display
    import ansible.constants as C
    import os

    # Define display variables and Display class
    display = Display()
    display.verbosity = 3

    # Define

# Generated at 2022-06-13 13:48:43.400366
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """The file ``/tmp/somefile`` is used in the test as a file that exists, as well as ``/tmp`` as a directory that exists.
    These files and directories are changed to a new temporary file or directory that is deleted at the end of the test.
    """
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes

    tempdir = tempfile.mkdtemp()
    tempfile1 = tempfile.NamedTemporaryFile(dir=tempdir, delete=False)
    tempfile1.close()
    tempfile2 = tempfile.NamedTemporaryFile(dir=tempdir, delete=False)
    tempfile2.close()

    temp = tempfile1.name

    tempfile1_name = os.path.basename(tempfile1.name)
    tempfile2_

# Generated at 2022-06-13 13:49:01.848384
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    subdir = 'test'
    setattr(lm, '_subdir', subdir)
    def find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        if subdir == 'test':
            return fn + '-found'
        else:
            return None
    setattr(lm, 'find_file_in_search_path', find_file_in_search_path)
    terms = ['file1', 'file2']
    result = lm.run(terms, None)
    assert result == ['file1-found']

# Generated at 2022-06-13 13:49:09.761282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt'], {}) == '/path/to/foo.txt'
    assert LookupModule.run([{'files':['/path/to/foo.txt', '/path/to/bar.txt'], 'paths':['/extra/path'], 'skip':True}], {}) == ['']
    assert LookupModule.run([{'files':['/path/to/foo.txt', '/path/to/bar.txt'], 'paths':['/extra/path']}], {}) == '/path/to/foo.txt'

# Generated at 2022-06-13 13:49:11.837042
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Unit test for method of class LookupModule not implemented"

# Generated at 2022-06-13 13:49:26.414785
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def __generic_test(terms, **kwargs):
        l = LookupModule()
        l._loader_mock = MagicMock()
        l._loader_mock.path_dwim.return_value = '/some/path'
        l._templar_mock.template.return_value = terms
        return l.run(terms, {}, **kwargs)

    terms = "some_file"
    assert __generic_test(terms) == ['/some/path/some_file']

    terms = "some_file.conf"
    assert __generic_test(terms) == ['/some/path/some_file.conf']

    terms = "some_file,some_other_file.conf"

# Generated at 2022-06-13 13:49:41.774215
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    NOTE: purpose of this test is to keep track of all 'possible' parameter
    terms. At the time of writing, the 'mapping style' was not documented,
    but seemed to do something.

    NOTE: in order to pass the test, the following variables
    must be set in the environment:
    ANSIBLE_TEST_DATA_ROOT
    ANSIBLE_TEST_DATA_ROOT_WRITEABLE
    '''

    import os

    import pytest

    from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup import LookupBase

# Generated at 2022-06-13 13:49:51.593721
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with string terms
    lookup = LookupModule()
    lookup._subdir = 'files'
    files = ['/path/to/file1.txt', 'file2.txt', '/path/to/file3.txt']
    paths = ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt']
    result, skip = lookup._process_terms(terms=files, variables={}, kwargs={})
    assert result == ['/path/to/file1.txt', 'file2.txt', '/path/to/file3.txt']
    assert skip is False
    result, skip = lookup._process_terms(terms=paths, variables={}, kwargs={})
    assert result == ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt']

# Generated at 2022-06-13 13:50:02.157823
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:50:09.096645
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt']

    lookup_plugin = LookupModule()
    lookup_plugin._loader = None
    lookup_plugin._templar = None
    lookup_plugin._find_file_in_search_path = \
        lambda v, subdir, fn, ignore_missing: subdir + '/' + fn
    result = lookup_plugin.run(terms, {})
    assert result == ['/files/foo.txt']

    lookup_plugin.set_options(direct={'paths': '/more/path', 'files': terms})
    result = lookup_plugin.run(terms, {})
    assert result == ['/more/path/foo.txt']


# Generated at 2022-06-13 13:50:10.532358
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement
    pass

# Generated at 2022-06-13 13:50:12.344798
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # TODO: Implement unit tests for method run of class LookupModule
    raise NotImplementedError

# Generated at 2022-06-13 13:50:35.995211
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, [])
    empty_play = Play.empty(variable_manager=variable_manager, loader=loader)

    # test single file as string
    lm = LookupModule()
    lm.set_loader(loader)
    lm.set_inventory(inventory)
    ret = lm.run(terms='foo.txt', variables=empty_play.get_variable_manager().vars, task=empty_play)
    assert ret[0] == 'foo.txt'

    # test single file in list
    l

# Generated at 2022-06-13 13:50:41.077314
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    lookup_plugin = LookupModule()

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])

    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 13:50:42.526981
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True


# Generated at 2022-06-13 13:50:53.942160
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._load_name = "foo.bar.py"
    l._templar = DummyTemplar()
    l._finder = DummyFinder()

    # single string
    terms = "something"
    assert l.run(terms) == ['something']

    # list
    l._templar = DummyTemplar()
    l._finder = DummyFinder()
    terms = ['one', 'two']
    assert l.run(terms) == ['one', 'two']

    # dict, no paths
    l._templar = DummyTemplar()
    l._finder = DummyFinder()
    terms = [{'files': 'something'}]
    assert l.run(terms) == ['something']

    # dict, with paths
    l._templ

# Generated at 2022-06-13 13:51:08.207104
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a class MockTemplar that can be used to mock jinja2.Template
    class MockTemplar:
        # initialize with a name
        def __init__(self):
            self.name = 'mock_templar'

        # function to return name of class
        def get_name(self):
            return self.name

        # function to return the same arguments that were passed
        def template(self, template_string):
            return template_string

    # create a class MockVars that can be used to mock ansible.vars.VariableManager
    class MockVars:
        def __init__(self):
            self.name = 'mock_variables'

        def get_name(self):
            return self.name


# Generated at 2022-06-13 13:51:16.264333
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    # Dummy values for `variables`, `subdir` and `path`
    variables = {"_original_file": "./test_lookup_plugin.py"}
    lookup._subdir = "files"
    path = ["test_lookup_plugin.py"]

    # Dummy values for `terms`, `var_options` and `kwargs`
    # `terms` is a dict with a list of dicts as values.
    terms = [
        {
            "files": "test_lookup_plugin.py",
            "paths": "files",
            "skip": False
        }
    ]

    var_options = {}
    kwargs = {}

    lookup.run(terms, var_options, **kwargs)

# Generated at 2022-06-13 13:51:27.702375
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a class to test with
    class FakeLookupModule(LookupModule):
        def _templar(self, x):
            return x
        def find_file_in_search_path(self, vars, subdir, fn, ignore_missing=True):
            return fn
    # Create an instance of the class
    test_lookup = FakeLookupModule()
    # Set options in a dict
    options = {'files': ['foo.conf', 'bar.conf'], 'paths': ['', '/etc']}
    # Make a list with the options dict as its only item
    test_terms = [options, options]
    # Test if the files are looked up correctly

# Generated at 2022-06-13 13:51:37.493372
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import mock
    import pytest
    from pathlib import Path
    from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup.first_found import LookupModule
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from units.module_utils._text import to_bytes, to_text


# Generated at 2022-06-13 13:51:46.582439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    src = '/etc/ansible/test_LookupModule_run/'
    dest = '/tmp/test_LookupModule_run'
    files = (
        'main.yaml',
        'main.yml',
        'roles/common/main.yaml',
        'roles/common/main.yml',
        'roles/common/tasks/main.yaml',
        'roles/common/tasks/main.yml',
    )

# Generated at 2022-06-13 13:51:57.530293
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # For coverage test
    l = LookupModule()
    l.get_option=lambda x: None
    l.find_file_in_search_path=lambda x,y,z, **kwargs: None
    l.set_options=lambda x, **kwargs: None
    l._load_name=lambda x: None
    l._fail_lookup=lambda x: None
    # For unit test
    l.find_file_in_search_path=lambda x,y,z, **kwargs: z
    l.run(terms=['test'], variables={'test': 't'})