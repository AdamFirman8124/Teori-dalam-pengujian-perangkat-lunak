

# Generated at 2022-06-13 13:42:04.592277
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        'foo.txt'
    ]

    variables = {
        'ansible_search_path': [
            '/path/to/project/files/'
        ]
    }

    lookup_module = LookupModule()

    assert lookup_module.run(terms, variables=variables) == [
        '/path/to/project/files/foo.txt'
    ]

# Generated at 2022-06-13 13:42:15.407012
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import builtins

    # construct a lookup
    lookup = LookupModule()

    # create an empty list of terms
    terms = []

    # create an empty list of variables
    variables = {}

    # Add two items to variables['ansible_search_path']
    variables['ansible_search_path'] = []
    variables['ansible_search_path'].append(os.path.join(os.environ['HOME'], 'ansible_unittest'))
    variables['ansible_search_path'].append('.')
    variables['ansible_search_path'].append(os.path.join(os.environ['HOME'], 'ansible_unittest', 'files'))

    # Construct

# Generated at 2022-06-13 13:42:27.114851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import shutil
    import tempfile


# Generated at 2022-06-13 13:42:36.648043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    cwd = os.getcwd()

# Generated at 2022-06-13 13:42:47.347816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.get_basedir = lambda: '/'
    lookup.find_file_in_search_path = lambda variables, subdir, filepath: filepath

# Generated at 2022-06-13 13:42:50.743376
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module_string = ""
    result_expected = []
    lm = LookupModule()
    result = lm.run(module_string)
    assert result == result_expected


# Generated at 2022-06-13 13:42:57.473092
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ["/my/path/*.txt"]
    variables = None
    # test with empty call
    paths = lookup_module.run(terms, variables)
    #assert paths == ["/Users/cmoulliard/playground/ansible/playbooks/files/fooapp/test.txt", "/Users/cmoulliard/playground/ansible/playbooks/files/fooapp/test1.txt", "/Users/cmoulliard/playground/ansible/playbooks/files/fooapp/test2.txt"]

# Generated at 2022-06-13 13:43:02.411765
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()

    # Unit test 1 with path: /etc/nginx/conf.d/*
    terms = ["/etc/nginx/conf.d/*"]
    results = mod.run(terms)
    assert results is not None


# Generated at 2022-06-13 13:43:12.940697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test run of class LookupModule
    # returns object of type list

    # Fixture data
    test_host_vars = {
        'ansible_search_path':  [
            os.path.join(os.getcwd(),'test_data','fileglob_module_data')
        ]
    }

    # Fixture test cases

# Generated at 2022-06-13 13:43:24.112299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run(["*.txt"], variables={"files": ["files1/file1.txt", "files2/file2.txt", "files1/file1.txt"]}) == [
        "files1/file1.txt", "files2/file2.txt", "files1/file1.txt"
    ]
    assert module.run(["*"], variables={"files": ["file1.txt", "file2.txt", "file1.txt"]}) == [
        "file1.txt", "file2.txt", "file1.txt"
    ]

# Generated at 2022-06-13 13:43:37.416326
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    fake_env = dict(
        ansible_search_path=[
            os.path.join(os.getcwd(), 'files', 'files1'),
            os.path.join(os.getcwd(), 'files', 'files2')
        ]
    )

    # Simple use
    results = module.run([ '*.txt' ], fake_env)
    assert len(results) == 2
    assert results[0] == os.path.join(os.getcwd(), 'files/files1/foo.txt')
    assert results[1] == os.path.join(os.getcwd(), 'files/files2/foo.txt')

    # Simple use - no matching files
    results = module.run([ '*.not' ], fake_env)
    assert len(results) == 0



# Generated at 2022-06-13 13:43:38.391837
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.run(['*'], variables={})

# Generated at 2022-06-13 13:43:46.098828
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    ret = lookup.run(['*.txt'], {'basedir': os.path.dirname(__file__), 'ansible_search_path': []})
    assert 'fileglob/LICENSE' in ret

    ret = lookup.run(['fileglob'], {'basedir': os.path.dirname(__file__), 'ansible_search_path': []})
    assert '.travis.yml' in ret

    ret = lookup.run(['*.txt','*.yml'], {'basedir': os.path.dirname(__file__), 'ansible_search_path': []})
    assert 'fileglob/LICENSE' in ret
    assert '.travis.yml' in ret

# Generated at 2022-06-13 13:43:57.267004
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Return empty list if file-pattern in terms matches no files
    assert lookup_module.run(['*/doesnotexist']) == []
    # Return a list of the file names that match the file-pattern
    assert lookup_module.run(['*c']) == ['a', 'b', 'c']
    # Return a list of the file names that match the file-pattern

# Generated at 2022-06-13 13:44:05.536067
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    terms = [
        os.path.join('..','README.md'),
        os.path.join('..','*.py'),
    ]
    # for the first term glob should not find anything, for the second term matching should be performed globally
    result = module.run(terms, variables={'working_dir': 'tests'})
    assert result[0].endswith(terms[0])
    assert len(result) > 1
    for res in result:
        assert res.endswith(terms[1][2:]) == True

# Generated at 2022-06-13 13:44:13.891218
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = [
        'fileglob_data/file1.txt',
        'fileglob_data/file2.txt',
        'fileglob_data/file3.txt',
    ]
    result = LookupModule().run(test_terms)
    assert result == [
        'fileglob_data/file1.txt',
        'fileglob_data/file2.txt',
    ]

# Generated at 2022-06-13 13:44:19.239769
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    files = ['file1', 'file2', 'file3']

    # empty term
    l = LookupModule()
    assert l.run([''], variables = {'files': files}) == []

    # term not in files
    l = LookupModule()
    assert l.run(['file4'], variables = {'files': files}) == []

    # term in files
    l = LookupModule()
    assert l.run('file1', variables = {'files': files}) == ['file1']

    # term in files
    l = LookupModule()
    assert l.run('file', variables = {'files': files}) == ['file1', 'file2', 'file3']

# Generated at 2022-06-13 13:44:24.371000
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    lookup_mod = LookupModule()

    # Check basic case
    terms = ['/my/path/*.txt']
    result = lookup_mod.run(terms)

    # Check empty case
    terms = []
    result = lookup_mod.run(terms)
    assert result == []

# Generated at 2022-06-13 13:44:35.389606
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Struct:
        pass
    module = Struct()
    setattr(module, 'params', {'wantlist': 'yes'})
    setattr(module, 'basedir', "/etc/ansible/roles")
    facts = ""
    lookup = LookupModule()

    ret = lookup.run(terms=['*.yml'], variables=facts, inject=module)
    assert len(ret) == 2
    assert ret[0] == "/etc/ansible/roles/test/tasks/main.yml"
    assert ret[1] == "/etc/ansible/roles/test/tasks/test.yml"

    module.params['wantlist'] = 'no'
    ret = lookup.run(terms=['*.yml'], variables=facts, inject=module)

# Generated at 2022-06-13 13:44:37.151597
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # We can't test this without throwing an exception
    pass

# Generated at 2022-06-13 13:44:49.174751
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # results from glob.glob and os.path.isfile are mocked to get correct results
    results = {
        'glob': ["/tmp/foo.txt", "/tmp/bar.txt", "/tmp/foo.txt", "/tmp/bar.txt"],
        'isfile': [True, True, False, True]
    }

    def mock_glob(path):
        return results['glob']

    def mock_isfile(path):
        return True in results['isfile']

    modules = {'glob': mock_glob, 'os.path': mock_isfile}
    with mock.patch.dict('sys.modules', modules):
        # the following statements will be the same to original LookupModule.run()
        lookup_module = LookupModule()

# Generated at 2022-06-13 13:44:55.963573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    lookup = LookupModule()
    lookup._loader = None
    lookup._templar = None
    lookup.set_options({})
    assert lookup.run(terms=['foo']) == []
    assert lookup.run(terms=['/foo/bar']) == []
    assert lookup.run(terms=['bar/foo/example.py']) == []
    assert lookup.run(terms=['example.py']) == []

# Generated at 2022-06-13 13:45:04.089177
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['foo', 'test', 'bar']
    test_variables = 'foo/test, bar'
    # Asserting characteristic of the test_variables being passed as a parameter
    assert os.path.basename(test_variables) != test_variables
    L = LookupModule()

    # Asserting that it calls find_file_in_search_path method of the LookupModule class
    assert L.find_file_in_search_path(test_variables, 'files', os.path.dirname(test_variables)) == 'foo/test'

    # Creating a class object of the LookupModule class
    L = LookupModule()

    # Asserting the return value of the method run of the LookupModule class

# Generated at 2022-06-13 13:45:06.055153
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["/my/path/*.txt"]
    obj = LookupModule()
    assert obj.run(terms) == ['/my/path/*.txt']

# Generated at 2022-06-13 13:45:11.957838
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Not testing none cases because AnsibleFileNotFound exceptions are raised
    results = LookupModule().run(['*'], {'ansible_search_path': ['/testdir']})
    assert results == []
    results = LookupModule().run(['*'], {'ansible_search_path': ['/etc']})
    assert results != []
    results = LookupModule().run(['*'], {'ansible_search_path': ['/etc/hosts']})
    assert results == []
    results = LookupModule().run(['/etc/hosts'], {'ansible_search_path': ['/etc']})
    assert results != []
    results = LookupModule().run(['/etc/hosts'], {'ansible_search_path': ['/etc/']})
    assert results != []


# Generated at 2022-06-13 13:45:17.361850
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class Variables(object):
        def __init__(self, dict):
            self.__dict__.update(dict)

    # TODO: Need to add a unit test for when this lookup matches files
    file_glob_lookup = LookupModule()
    files = file_glob_lookup.run(["/path/to/dir/*.txt"], variables=Variables({}))
    assert files == []

# Generated at 2022-06-13 13:45:19.809552
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['*.py'],{}) == ['fileglob.py']

# Generated at 2022-06-13 13:45:31.585255
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    import os
    lookup_module = LookupModule()
    basedir = lookup_module.get_basedir({'ansible_basedir':os.path.abspath(os.path.join(os.path.dirname(__file__),'fixtures/lookup_plugins_fileglob'))})
    test_fixture_dir = os.path.join(basedir, 'files')
    test_terms = 'test_fileglob*.txt'
    results = lookup_module.run(test_terms, {'ansible_search_path':[test_fixture_dir]})
    assert results == ['test_fileglob1.txt', 'test_fileglob2.txt']
    
    # Missing pattern
    with pytest.raises(AnsibleFileNotFound):
        lookup_

# Generated at 2022-06-13 13:45:34.233352
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test environment where all parameters are known
    # Create a test object for class LookupModule
    # Call the method with known values
    # Assert the results
    pass

# Generated at 2022-06-13 13:45:36.960534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # arrange
    terms = ['/my/path/*.txt']
    # act
    module = LookupModule()
    files = module.run(terms, None)

    # assert
    assert len(files) == 0

# Generated at 2022-06-13 13:45:51.408325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test parsing
    assert LookupModule.run(LookupModule(), ['/etc/ansible/hosts']) == ['/etc/ansible/hosts']
    assert LookupModule.run(LookupModule(), ['/etc/ansible/hosts'], wantlist=True) == ['/etc/ansible/hosts']

    # test parsing
    assert LookupModule.run(LookupModule(), ['/etc/ansible/hosts'], wantlist=True) == ['/etc/ansible/hosts']

    # test parsing
    assert LookupModule.run(LookupModule(), ['/etc/ansible/ansible.cfg'], wantlist=True) == ['/etc/ansible/ansible.cfg']

    # test parsing

# Generated at 2022-06-13 13:45:54.555232
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    tm = LookupModule()
    assert tm.run(['/tmp/michael', '/tmp/ryan']) == ['/tmp/michael', '/tmp/ryan']
    assert tm.run([]) == []


# Generated at 2022-06-13 13:46:00.403772
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.run(["*.py"])
    #lookup.run(["*.md"]) # No Markdown file, so this should return empty result set
    #lookup.run(["*.ini"]) # No ini file, so this should return empty result set

# Generated at 2022-06-13 13:46:13.018307
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.utils.path import unfrackpath
    from ansible.parsing.dataloader import DataLoader
    from units.mock.patch import patch, MagicMock

    dl = DataLoader()

    test_lookup = patch.object(LookupModule, 'find_file_in_search_path')
    find_file_in_search_path = test_lookup.start()
    get_basedir = patch.object(LookupModule, 'get_basedir')
    _get_basedir = get_basedir.start()

    test_lookup = patch.object(os.path, 'expanduser')
    os_expanduser = test_lookup.start()

    test_lookup = patch.object(os.path, 'expandvars')
    os_expandvars = test

# Generated at 2022-06-13 13:46:21.857321
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    from collections import namedtuple

    FakeAnsibleModule = namedtuple('FakeAnsibleModule', ['params'])
    FakeModuleUtils = namedtuple('FakeModuleUtils', ['get_search_path'])

    fm = FakeAnsibleModule(params={})
    fmu = FakeModuleUtils(
        get_search_path=lambda: ['/var/tmp/ansible/playbooks/files/fooapp']
    )

    lookup_module = LookupModule(
        basedir='/var/tmp/ansible/playbooks',
        runner_path='/var/tmp/ansible/playbooks/ansible-runner',
        ansible_module=fm,
        module_utils=fmu,
        loader=None
    )

    # Act
    result = lookup_module.run

# Generated at 2022-06-13 13:46:30.926157
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    # Test case where globbing fails
    assert lookup_obj.run(['*.txt']) == []
    # Test case where globbing succeeds
    assert lookup_obj.run(['*_test*.py']) == [u'LookupModule_test.py']
    # Test case where globbing finds nothing
    assert lookup_obj.run(['*.txt']) == []
    # Test case where globbing finds two items
    assert lookup_obj.run(['?_test*.py']) == [u'1_test_1.py', u'1_test_2.py', u'2_test_1.py', u'2_test_2.py']

# Generated at 2022-06-13 13:46:45.232083
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=too-many-locals

    test_data = [
                ('../test/test_data/test_fileglob_run_test_data1.txt', 'test_file1.txt')
                ]

    module_name = 'fileglob'
    basedir = '/home/enis/pyprojects/ansible/test/test_data/test_fileglob_run_test_data1'
    ansible_search_path = ['/home/enis/pyprojects/ansible/test/test_data']
    terms = ['test_file1.txt']
    variables = {'ansible_search_path':ansible_search_path}

    lookup_plugin = LookupModule()

    # Check if method run returns correct data

# Generated at 2022-06-13 13:46:51.003853
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    basedir = os.path.dirname(__file__)
    test_dir = os.path.join(basedir, 'fileglob')
    lookup = LookupModule()
    assert lookup.run(['nosuchfile'], variables={'ansible_search_path': [test_dir]}) == []
    assert lookup.run(['fileglob'], variables={'ansible_search_path': [test_dir]}) == ['fileglob']
    assert lookup.run(['fileglob', '*.txt'], variables={'ansible_search_path': [test_dir]}) == ['fileglob.txt', 'fileglob.txt~']

# Generated at 2022-06-13 13:47:00.648486
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import os
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.plugins.lookup import LookupBase

    # create empty ansible config
    c = {'DEFAULT_MODULE_LANG': 'en_US.UTF-8',
         'DEFAULT_MODULE_SUFFIX': '.py',
         'DEFAULT_MODULE_TEXT': '#!/usr/bin/python'}

    # create empty ansible arguments

# Generated at 2022-06-13 13:47:04.393162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    terms = ['../../../../../etc/passwd']
    file_paths = look.run(terms)
    assert len(file_paths) == 1
    assert file_paths[0] == '../etc/passwd'

# Generated at 2022-06-13 13:47:18.487717
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        import __main__
        __main__.IS_ANSIBLE_TESTING = True
    except Exception:
        pass

    module = LookupModule()
    # Test with single term
    assert module.run(['globbing_test_file.txt'], {'ansible_basedir': './test/integration/data/validate/lookup', 'ansible_search_path': ['../../validate/lookup', '..']}) == ['../../validate/lookup/globbing_test_file.txt']

    # Test with list of terms

# Generated at 2022-06-13 13:47:19.378544
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:47:27.358852
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.config.manager import ConfigManager
    config_manager = ConfigManager(
        os.path.realpath(os.path.join(os.path.dirname(__file__), '../../../../test/ansible.cfg')))
    config_manager._read_config_data(['/etc/ansible/ansible.cfg', './test/ansible.cfg', 'test/ansible.cfg'])
    config_manager.set_config_type('fileglob')
    with config_manager.context() as config:
        lookup_module = LookupModule()
        terms = ['a', 'b', 'c']

# Generated at 2022-06-13 13:47:35.717905
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    testcases = {}

    # Setup testcases
    this = os.path.dirname(os.path.realpath(__file__))
    testcases[0] = {}
    testcases[0]['terms'] = [
        'foo',
        'bar'
    ]
    testcases[0]['result_expected'] = os.path.join(this, 'foo', 'bar')    # This is the file to create

    testcases[1] = {}
    testcases[1]['terms'] = [
        'readme.txt'
    ]
    testcases[1]['result_expected'] = os.path.join(this, 'foo', 'readme.txt')

    # Execute testcases

# Generated at 2022-06-13 13:47:47.789429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils.ansible_modlib.common.collections import ImmutableDict

    # Setup a test LookupModule object
    lookup_module_obj = LookupModule()
    lookup_module_obj.set_options(ImmutableDict({'wantlist': True}))

    # Test run with a single path and no directories (test_simple_glob)
    matches = lookup_module_obj.run([to_bytes('files/test_file_?.txt')],
                                    ImmutableDict({'basedir': '/usr/share/ansible/ansible_test_folder/'}))
    assert len(matches) == 2

# Generated at 2022-06-13 13:47:58.349664
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import shutil
    import tempfile
    import unittest
    
    # Create a test directory and files
    dirpath = tempfile.mkdtemp()
    filenames = ["foo.txt", "bar.txt", "baz.doc", "foo.doc", "qux.txt"]
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "w") as outf:
            outf.write(filepath)

    # Set up an instance of the object under test
    lookup_obj = LookupModule()

    # Set up variables for testing
    variables = dict()
    variables['ansible_search_path'] = [dirpath]

    # Run test cases
    test_results = list()

# Generated at 2022-06-13 13:48:07.445729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import lookup_loader
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    lookup_loader.set_loader(loader)
    results = list(lookup_loader.get('fileglob').run(['test*'], variable_manager))

    assert(results[0].endswith('test_LookupModule_run.py'))

# Generated at 2022-06-13 13:48:17.918889
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # mock class to handle a temp path being created by mkdtemp()
    def mock_mkdtemp(self):
        return 'temp_dir'
    LookupBase.mkdtemp = mock_mkdtemp

    # mock class to handle a temp file being created by tempfile.mkstemp()
    def mock_tempfile_mkstemp(self,suffix='', prefix='tmp', dir=None, text=False):
        return ('filehandle','temp_file')
    LookupBase.tempfile_mkstemp = mock_tempfile_mkstemp

    # create instance of class LookupModule
    lookup_module = LookupModule()

    # test non-recursive run of method
    assert lookup_module.run(['*.txt']) == []

    # test recursive run of method

# Generated at 2022-06-13 13:48:23.900456
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock input
    lookup = LookupModule()
    lookup.find_file_in_search_path = lambda *args: args[1]
    lookup.get_basedir = lambda x, : ""
    lookup.settings = dict(
        jinja2_native=False,
        _terms="file_path"
    )

    # Mock output
    os.path.basename = lambda x: x
    os.path.isfile = lambda x: True
    glob.glob = lambda x: x

    # Test method
    assert lookup.run(["", "", "file_path"]) == ["", "", "file_path"]

# Generated at 2022-06-13 13:48:29.762905
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case 1: The incorrect term should give empty list
    terms = ["badword.txt"]
    ret = LookupModule().run(terms, {})
    assert not ret

    # Test case 2: The correct term should give non-empty list
    terms = ["ansible.cfg"]
    ret = LookupModule().run(terms, {})
    assert ret

# Generated at 2022-06-13 13:49:06.814545
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    :return:
    """
    lookup_module = LookupModule()
    # Test with no dir and file, should use ansible_search_path and 'files'
    terms = ['hosts']
    variables = {'ansible_search_path': ['/Users/mickey/ansible', '/Users/mickey/playbooks']}
    expected_ret = ['/Users/mickey/ansible/files/hosts', '/Users/mickey/playbooks/files/hosts', '/Users/mickey/ansible/hosts', '/Users/mickey/playbooks/hosts']
    ret = lookup_module.run(terms, variables)
    assert expected_ret == ret
    # Test with dir and file
    terms = ['/etc/hosts']

# Generated at 2022-06-13 13:49:08.657930
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ["/test/*", "/test/test1*"]
    assert lookup_module.run(terms) == []

# Generated at 2022-06-13 13:49:12.688933
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test the method run of class LookupModule
    """
    unit = LookupModule()

    term = "/test"
    result = [{'_list': [u'/test']}]

    glob.glob = MagicMock(return_value=True)
    assert unit.run(term) == result

# Generated at 2022-06-13 13:49:22.297364
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a fake LookupModule for testing
    class FakeLookupModule(object):
        def __init__(self, basedir=None):
            self.basedir = basedir
        def get_basedir(self, variables):
            return self.basedir
        def find_file_in_search_path(self, variables, path, dirname):
            return os.path.join(path, dirname)

    # Create the object
    lm = LookupModule(FakeLookupModule(basedir='/tmp/'))

    # Make it think 'files' are present in the search path
    variables = dict(ansible_search_path=['/some/path'])

    # Check the results
    terms = ['somefile.txt']
    results = lm.run(terms, variables=variables)

# Generated at 2022-06-13 13:49:33.224223
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Init the class
    lookup_mod = LookupModule()

    # Test if the function raises error on empty terms
    try:
        lookup_mod.run([], None)
    except AnsibleFileNotFound:
        pass
    except Exception as e:
        raise e
    else:
        raise Exception("AnsibleFileNotFound is not raised when the terms are empty")

    # Test if the function raises error on missing file in terms
    try:
        lookup_mod.run(["files/test_file.txt"], None)
    except AnsibleFileNotFound:
        pass
    except Exception as e:
        raise e
    else:
        raise Exception("AnsibleFileNotFound is not raised when the file is not found")

    # Test if the function raises error on invalid terms
    # terms should be of type list

# Generated at 2022-06-13 13:49:36.130808
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(
        argument_spec = dict(
            _raw_params = dict(type='str', required=True),
        ),
        supports_check_mode=True
    )
    module.exit_json(changed=False, foo='bar')

# Generated at 2022-06-13 13:49:41.231567
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    data = [
        ['/tmp/example.txt', [], {}, {}, []],
        ['/playbooks/files/*', [], {}, {}, []],
        ['/tmp/*.txt', [], {}, {}, []],
        ['/tmp/test.txt', [], {}, {}, []],
        ['/etc/*', [], {}, {}, []],
        ['test.cf', [], {}, {}, []],
        ['/tmp/test*', [], {}, {}, []]
    ]

    mod = LookupModule()
    mod.set_options({'wantlist': False})
    for (term, _, ds, variables, expected) in data:
        result = mod.run(terms=[term], variables=variables)[0]
        assert result == expected, "term='%s'" % term

# Generated at 2022-06-13 13:49:44.500670
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    testlookup = LookupModule()
    assert testlookup is not None
    testlookup.add_fake_dicts()
    results = testlookup.run(["*"])
    assert results is not None

# Generated at 2022-06-13 13:49:53.127682
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test 1: terms = ['*.txt']
    # expected: ret = ['/my/path/file1.txt', '/my/path/file2.txt']
    l = LookupModule()
    ret = l.run(['*.txt'], variables={'myvar': 'myval'})
    assert(len(ret) == 2)
    assert(ret[0] == '/my/path/file1.txt')
    assert(ret[1] == '/my/path/file2.txt')

    # test 2: terms = ['/my/path/*.txt']
    # expected: ret = ['/my/path/file1.txt', '/my/path/file2.txt']
    l = LookupModule()

# Generated at 2022-06-13 13:49:59.183940
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create instance
    lookup = LookupModule()

    # Call run method
    result = lookup.run(["test_LookupModule_run.txt"], variables={"file_root": "/path/to/file/root"})

    # Assert that result is not empty
    assert result