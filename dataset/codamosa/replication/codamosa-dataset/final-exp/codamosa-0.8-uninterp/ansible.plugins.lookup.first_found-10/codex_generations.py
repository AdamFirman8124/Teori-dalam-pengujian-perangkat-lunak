

# Generated at 2022-06-13 13:42:11.284835
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars

    data_loader = DataLoader()
    inventory = InventoryManager(
        loader=data_loader,
    )
    variable_manager = VariableManager(
        loader=data_loader,
        inventory=inventory,
    )
    play_context = PlayContext()

    ### override ansible_playbook_python to use python3 +

# Generated at 2022-06-13 13:42:12.689228
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # FIXME: missing test
    pass

# Generated at 2022-06-13 13:42:20.053633
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run([
        {'paths': 'a/path', 'files': 'foo,bar.txt'},
        {'paths': 'a/path', 'files': 'foo,bar.txt'},
        {'paths': 'a/path', 'files': 'foo,bar.txt'},
    ], {}) == []

# Generated at 2022-06-13 13:42:31.364833
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    assert lu.run(terms=['/tmp/test_LookupModule_run/no_file', '/tmp/test_LookupModule_run/file_ok'],
                  variables={},
                  error_on_undefined_vars=False) == ['/tmp/test_LookupModule_run/file_ok']

    assert lu.run(terms=['/tmp/test_LookupModule_run/no_file', '/tmp/test_LookupModule_run/file_ok'],
                  variables={},
                  skip=True,
                  error_on_undefined_vars=False) == ['/tmp/test_LookupModule_run/file_ok']


# Generated at 2022-06-13 13:42:44.051220
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # NOTE: not using 'importlib' due to ansible constraints for 2.8
    from ansible.plugins.lookup import first_found
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager

    # setup multiple vars
    # TODO: to be expanded when other vars are needed

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variables = VariableManager(loader=loader, inventory=inventory)
    # load inventory and set vars
    inventory.parse_inventory(['host1 ansible_distribution=RedHat ansible_os_family=RedHat'])
    vars = inventory.get_vars_by_

# Generated at 2022-06-13 13:42:54.921456
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create instance of class LookupModule
    lookup_module_instance = LookupModule()

    # Get the parameters from test file and create a list needed for test
    test_file = open("test.txt", "r")
    test_params_list = test_file.readline()

    test_params = ast.literal_eval(test_params_list)
    terms = test_params["terms"]
    variables = test_params["variables"]
    kwargs = test_params["kwargs"]

    # For some reason "paths" key in dict was causing error. The reason was that the
    # value has a comma in it. Dictionary can recognize comma as a separator
    # which is why it was not creating a list out of it
    # the workaround is to replace the string from file by replacing the "," with ";"
    # and

# Generated at 2022-06-13 13:43:06.813800
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()
    file_list = ['test1.txt', 'test2.txt', 'test3.txt']

    # test full path
    module._loader.set_basedir('./')
    assert module.run(file_list) == ['./test1.txt']

    # test relative path
    module._loader.set_basedir('./test')
    assert module.run(file_list) == ['./test/test1.txt']

    # test full path
    module._loader.set_basedir('./test')
    assert module.run(map(lambda y: './' + y, file_list)) == ['./test/test1.txt']

    # test relative path
    module._loader.set_basedir('./t1/t2/t3')

# Generated at 2022-06-13 13:43:15.543817
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # unit tests for lookup module need to be in this dir
    this_dir = os.path.dirname(__file__)

    # generate a fake inventory, with the host containing this file,
    # as the only one defined
    # generate a fake inventory, with the host containing this file,
    # as the only one defined

# Generated at 2022-06-13 13:43:26.521280
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # skipped testing when skip=False as not practical to create a test case with
    # a valid file name.

    # Simple term test
    test_term = ['/path/to/a/valid/file1', 'relative/dir/file2']
    l = LookupModule()
    total_search = l._process_terms(test_term, 'variables', 'kwargs')
    assert len(total_search) == 2

    # Dict style term test
    test_term = [{'files': 'file1,file2', 'paths': '/path/to/a/valid'}, {'files': 'file3', 'paths': '/path/other/valid'}]
    l = LookupModule()
    total_search = l._process_terms(test_term, 'variables', 'kwargs')

# Generated at 2022-06-13 13:43:38.440830
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    files = [
        'A.txt',
        'B.txt',
        'C.txt',
        'D.txt',
        'E.txt',
    ]
    paths = [
        '/tmp/one/',
        '/tmp/two/',
        '/tmp/three/',
        '/tmp/four/',
        '/tmp/five/',
    ]

# Generated at 2022-06-13 13:43:47.852775
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup._process_terms([{'files': ['a', 'b', 'c'], 'paths': ['d', 'e']}, {'files': 'f,g,h', 'paths': 'i,j'}],
        {}, {})
    assert result[0] == ['d/a', 'd/b', 'd/c', 'e/a', 'e/b', 'e/c', 'i/f', 'i/g', 'i/h', 'j/f', 'j/g', 'j/h']
    assert result[1] is False


# Generated at 2022-06-13 13:43:48.726501
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 13:43:58.853192
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test method run of LookupModule class

    This is a generic test for method run of class LookupModule
    It tracks:
     - returned objects
     - raised exceptions
     - stopped execution (if a return/break is missing)
    """
    import pytest
    from ansible.plugins.lookup.first_found import LookupModule
    from ansible.module_utils.six import string_types
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager

    # The class to test
    cls = LookupModule


# Generated at 2022-06-13 13:44:09.034627
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # return the first file found in list of files, by default look in file
    # relative path
    assert ['/path/to/foo.txt'] == LookupModule().run(
        terms=[
            '/path/to/foo.txt',
            '/path/to/bar.txt',
            '/path/to/biz.txt'
        ]
    )

    # look in additional path
    assert ['/path/to/foo.txt'] == LookupModule().run(
        terms=[
            '/path/to/foo.txt',
            '/path/to/bar.txt',
            '/path/to/biz.txt',
        ],
        variables={
            'paths': '/extra/path',
        }
    )

    # find file in dict term

# Generated at 2022-06-13 13:44:10.655087
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:44:18.790282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.utils.path as path_utils
    import ansible.parsing.dataloader as DataLoader

    LookupBase._get_file_name_if_relative = lambda self, x: x # do not try to parse template
    LookupBase.get_basedir = lambda self, variables: '/test_dir'

    def find_file_in_search_path_mock(variables, subdir, filename, ignore_missing):
        return os.path.join('/test_dir', subdir, filename)

    path_utils.path_dwim = lambda x, y: os.path.join('/test_dir', y)


# Generated at 2022-06-13 13:44:26.699824
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.context import CLIContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    context = PlayContext()
    clicontext = CLIContext()

    current_path = os.path.dirname(__file__)
    data_path = os.path.join(current_path, "__data")
    data_files_path1 = os.path.join(data_path, "files1")
    data_files_path2 = os.path.join(data_path, "files2")

    variables = variable_manager.get_vars(loader=loader, context=context)

    # Template tests
   

# Generated at 2022-06-13 13:44:37.062801
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.inventory.manager import InventoryManager
    import pytest
    import os

    display = Display()
    variable_manager = VariableManager(inventory=InventoryManager(loader=None, sources='localhost,'))

    def _init_runner():
        my_vars = variable_manager.get_vars(loader=None, play=None)
        my_vars = combine_vars(my_vars, variable_manager.get_vars(loader=None, play=None))

# Generated at 2022-06-13 13:44:44.532017
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import context
    from ansible.plugins.loader import lookup_loader

    pm = context.CLIARGS['module_path']
    lookup_module = lookup_loader.get('first_found', pm)

    # TODO: write test
    # total_search = ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt']
    #
    # for f in total_search:

# Generated at 2022-06-13 13:44:50.037091
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LookupModule().run(
        [
            'foo.conf',
            {
                'files': 'foo.txt,bar.txt',
                'paths': 'a/b/c,d/e/f',
            },
            'foo2.conf'
        ],
        {},
    )

    LookupModule().run(
        [
            'foo.conf',
            'bar.txt',
            {
                'files': 'foo.txt,bar.txt',
                'paths': 'a/b/c,d/e/f',
            },
            'foo2.conf'
        ],
        {},
    )

# Generated at 2022-06-13 13:44:56.416281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:45:00.046648
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run([{
        'files': "test1",
        'paths': "/tmp/test,/tmp/test2"
    }, {
        'files': "test2",
        'paths': "/tmp/test,/tmp/test2"
    }]) == ['/tmp/test/test1']

# Generated at 2022-06-13 13:45:14.168845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.find_file_in_search_path = lambda variables, subdir, fn, ignore_missing=True: fn + '_path'
    lookup._loader = lambda: None
    lookup._loader.get_basedir = lambda: None
    lookup._loader.get_basedir.return_value = '/x/y'

    assert lookup.run(None, {}, files=['a.txt'], paths=['/tmp/']) == ['/tmp/a.txt_path']
    assert lookup.run(None, {}, files=['a.txt'], paths=['/tmp/'], skip=True) == []
    assert lookup.run([], {}, files=['a.txt'], paths=['/x/y/']) == ['/x/y/a.txt_path']

# Generated at 2022-06-13 13:45:27.278479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    srcFilePath = os.path.dirname(os.path.realpath(__file__))
    unittestPath = os.path.abspath(os.path.join(srcFilePath, '..', 'unittest_data'))

    terms = (
        ['/tmp/fake1', '/tmp/fake2', '/tmp/fake3'],
        [{"paths": "/tmp/", "files": "fake1,fake2,fake3", "skip": True}, "/tmp/fake1", "/tmp/fake2", "/tmp/fake3"],
        [{"paths": "/tmp/", "files": "fake1,fake2,fake3", "skip": False}, "/tmp/fake1", "/tmp/fake2", "/tmp/fake3"])

# Generated at 2022-06-13 13:45:37.735512
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lkup = LookupModule()

    # NOTE: during refactor noticed that
    # 1. 'files' can be from a list of dict, but not in one dict,
    # 2. 'paths' can be from a list, but also in one dict,
    # 3. 'skip' can be from list of dict and one dict, but in the end it does not matter
    # if there are more than one - last value will be used.

    # That is why we have 3 sets of tests for each feature: lists and dicts.

    # test list of strings (no paths)
    total_search, skip = lkup._process_terms(['file1', 'file2'], {}, {})
    assert ['file1', 'file2'] == total_search
    assert False is skip

    # test list of strings + skip
    total_

# Generated at 2022-06-13 13:45:50.253901
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # params
    terms = [
        {'files': ['foo.txt', 'bar.txt'], 'paths': ['/tmp/production', '/tmp/staging']},
        {'files': ['biz.txt', 'baz.txt'], 'paths': ['/tmp/production', '/tmp/staging']},
    ]
    variables = {}
    kwargs = {}

    # instantiate
    _lookup = LookupModule()

    # methods
    _lookup.set_options = lambda var_options=None, direct=None: None
    _lookup.get_option = lambda x: None
    _lookup.find_file_in_search_path = lambda a, b, c, ignore_missing: None
    _lookup._templar = None

    # test

# Generated at 2022-06-13 13:45:59.904868
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        LookupModule().run([], {})
        assert False is True
    except AnsibleLookupError as e:
        assert "No file was found when using first_found." in str(e)

    assert LookupModule().run(['*'], {}) == []
    assert LookupModule().run([{'paths': './test/fixtures/lookups/first_found',
                                'files': 'not_found'}],
                              {'ansible_basedir': os.path.dirname(os.path.abspath(__file__))}) == []

# Generated at 2022-06-13 13:46:12.723777
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import operator
    from ansible.module_utils._text import to_native

    module = LookupModule()
    assert operator.eq(type(module), type(LookupModule()))

    test_list = ['first_found_return.yml', 'first_found_return.sh']
    test_dict = {'files': 'first_found_return.yml,first_found_return.sh', 'paths': './'}
    test_dict2 = {'files': ['first_found_return.sh', 'first_found_return.yml']}
    test_dict3 = {'files': ['return_none_file.yml', 'return_none_file.sh'], 'paths': './'}
    test_dict4 = {'paths': './tests'}

# Generated at 2022-06-13 13:46:21.691967
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModuleTest = type('LookupModuleTest', (object,), dict(LookupModule.__dict__))
    lookup_module = LookupModuleTest()
    lookup_module.__dict__['_choose_colon_file'] = lambda self: """
#
# This file controls the state of network interfaces.
#
# Please see interfaces(5) for more information on 
# the syntax of this configuration file.
#

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet static
        address {{ networks.management.ip }}
        netmask {{ networks.management.netmask }}
"""
    lookup_module.__dict__['_templar'] = object()

# Generated at 2022-06-13 13:46:31.844163
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import shutil
    from ansible.module_utils.six import PY3
    local_basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
    local_files = [
        'first_winning_file',
        'first_winning_file_2',
    ]

    local_files_in_path = [
        'current_play_relative',
        'current_play_relative_2',
        'current_play_extra_relative',
        'current_play_extra_relative_2',
        'role_relative',
        'role_relative_2',
        'role_extra_relative',
        'role_extra_relative_2',
    ]

    for f in local_files:
        shutil

# Generated at 2022-06-13 13:46:51.989999
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils._text import to_text
    results = dict(
        skipped='',
        failed='',
        exception=None,
    )
    module_args = dict(
        _raw_params='',
        _task=None,
        _terms=[],
        _task_vars=dict(),
        _unsafe_proxy_tempdir='',
    )

    # NOTE:  cannot mock 'self' as jinja2 calls it but it is not in 'self'
    def _get_vars(*args, **kwargs):
        return module_args['_task_vars']

    def _templar_template(*args, **kwargs):
        return to_text(args[0])

    # Cannot mock self as jinja2 calls it
    file_name = 'some/filename'


# Generated at 2022-06-13 13:47:01.840614
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.path import makedirs_safe
    from ansible.utils.path import unfrackpath
    import shutil
    tmpdir = unfrackpath("$TMPDIR/ansible_first_found_test")
    shutil.rmtree(tmpdir, True)
    makedirs_safe(tmpdir)

    # write out some files for the test
    test_vars = dict(
        foo_path = '%s/foo' % tmpdir,
        bar_path = '%s/bar' % tmpdir,
        foobar_path = '%s/foo/bar' % tmpdir,
        foobar_file = 'test.txt',
        foobar_file_path = '%s/foo/bar/test.txt' % tmpdir,
    )

# Generated at 2022-06-13 13:47:10.030325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        validate = {'errors': 'ignore'}
        lookup = LookupModule()
        terms = ['/path/to/file1', '/path/to/file2']
        variables = {'inventory_hostname': 'testhost'}
        lookup.run(terms, variables)
        raise AssertionError("AnsibleLookupError not raised")
    except AnsibleLookupError as e:
        assert e.message == 'No file was found when using first_found.'
    assert lookup.run(terms, variables, skip=True, **validate) == []
    terms.append('/path/to/file3')
    assert lookup.run(terms, variables, **validate) == ['/path/to/file1']

# Generated at 2022-06-13 13:47:22.403510
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  l = LookupModule(loader = None, templar = None)
  assert_expect_exception(l.run, [ [] ], AnsibleLookupError, "No file was found when using first_found.")

  prefs = []
  res = l.run([{'paths': [ 'path' ], 'files': [ 'foo' ]}], prefs)
  assert res == ['path/foo'], res

  res = l.run([{'paths': [ 'path' ], 'files': [ 'foo', 'bar' ]}], prefs)
  assert res == ['path/foo'] or res == ['path/bar'], res

  res = l.run([{'paths': [ 'path', 'path2' ], 'files': [ 'foo', 'bar' ]}], prefs)

# Generated at 2022-06-13 13:47:33.810691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        dict(files=['foo.txt'], paths=['/tmp/production', '/tmp/staging']),
        dict(files=['bar.txt'], paths=['/home'])
    ]
    lookup_mod = LookupModule()
    total_search, skip = lookup_mod._process_terms(terms, None, None)
    assert total_search == ['/tmp/production/foo.txt', '/tmp/staging/foo.txt', '/home/bar.txt']
    # error if a file is not found
    try:
        lookup_mod.run(terms, None, None)
        assert False
    except AnsibleLookupError:
        pass

    # no file found

# Generated at 2022-06-13 13:47:46.288857
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for multiple terms and paths
    assert (LookupModule().run(terms=[10, 20, 30, {'files': 'test.txt', 'paths': '.,/a/b,/a/c'}, 50, 60])
            == ['/a/b/test.txt', '/a/c/test.txt', 'test.txt'])
    # Test for multiple terms and multiple paths
    assert (LookupModule().run(terms=[10, 20, 30, {'files': 'test.txt', 'paths': ['/a/b', '/a/c']}, 50, 60])
            == ['/a/b/test.txt', '/a/c/test.txt'])
    # Test for multiple terms and paths with environ variables

# Generated at 2022-06-13 13:47:55.671297
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._subdir = "files"
    lookup._loader = None

    # Test parameters

# Generated at 2022-06-13 13:48:00.681247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def run_lookup_module_run(sut):
        params = ['bar/a.txt', 'foo/b.txt']
        try:
            sut.run(params)
            assert False, "AnsibleLookupError is not raised"
        except AnsibleLookupError as e:
            assert str(e) == 'No file was found when using first_found.'

    LookupModule_instance = LookupModule()
    run_lookup_module_run(LookupModule_instance)

    LookupModule_instance._loader = None
    run_lookup_module_run(LookupModule_instance)

# Generated at 2022-06-13 13:48:13.091634
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        {'files': ['foo.txt'], 'paths': ['baz'], 'skip': True},
        {'files': ['bar.txt', 'baz.txt'], 'skip': True},
        {'files': ['hostname.txt'], 'paths': ['baz', 'foo'], 'skip': False},
    ]
    variables = {
        'ansible_basedir': '/home/ansible',
        'ansible_playbook_python': '/usr/bin/python'
    }
    kwargs = {}

    total_search, skip = lookup._process_terms(terms, variables, kwargs)


# Generated at 2022-06-13 13:48:14.569429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(LookupModule(None, None).run([], None)) is None

# Generated at 2022-06-13 13:48:37.805763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test list of files
    assert LookupModule(None, None).run(["foo.txt"], {}) == []
    assert LookupModule(None, None).run(["/etc/passwd"], {}) == ['/etc/passwd']
    # test dict file
    assert LookupModule(None, None).run([{"files": ["foo.txt"]}], {}) == []
    assert LookupModule(None, None).run([{"files": ["/etc/passwd"]}], {}) == ['/etc/passwd']
    # test dict files and paths
    tmpdir = os.path.dirname(os.path.realpath(__file__)) + "/tmpdir"
    assert LookupModule(None, None).run([{"files": ["foo.txt"]}], {}) == []
    # create a file

# Generated at 2022-06-13 13:48:44.140758
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with 'dict' term
    test_Instance = LookupModule()

    # NOTE: the dict term is designed for a single dict, not a list of dicts or list of strings or a single string.
    # If things are 'mixed then there is no way to know the order of precedence.
    total_search, skip = test_Instance._process_terms([{'files': 'file1,file2', 'paths': 'path1,path2'}], {}, {})
    assert len(total_search) == 4



# Generated at 2022-06-13 13:48:45.631425
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 0



# Generated at 2022-06-13 13:48:54.778485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    f = '/tmp/foo'
    l = LookupModule()
    l._subdir='files'
    l._templar = None #TODO
    assert [f] == l.run(terms=['foo'], variables={'_original_file': f})
    assert [f] == l.run(terms=[{'files': 'foo', 'paths': '/tmp'}], variables={'_original_file': f})
    assert [f] == l.run(terms=[{'files': 'foo', 'paths': ['/tmp'], 'skip': False}], variables={'_original_file': f})
    assert [f] == l.run(terms=[{'files': 'foo', 'paths': ['/tmp'], 'skip': True}], variables={'_original_file': f})

# Generated at 2022-06-13 13:49:06.972416
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup = LookupModule()
    # Test without any files found
    assert test_lookup.run(terms=[
        {"files": "1.txt"},
        {"files": "2.txt"},
    ], variables={}) == []
    # Test with some files found
    assert test_lookup.run(terms=[
        {"files": "1.txt"},
        {"files": "2.txt"},
    ], variables={"_original_file": "test.txt"}) == [os.path.join(os.path.dirname(os.path.realpath("test.txt")), 'files', '2.txt')]
    # Test with skip=True

# Generated at 2022-06-13 13:49:16.138092
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):
        def find_file_in_search_path(self, variables, subdir, fn, ignore_missing):
            return fn

    # Test prepare
    terms = [1, 2, 3]
    variables = {'spam': 'eggs'}

    def test_process_terms_exception(terms):
        lookup_module = TestLookupModule()
        total_search = lookup_module._process_terms(terms, variables)
        return total_search[0]

    def test_process_terms_exception_uses_override(terms):
        lookup_module = TestLookupModule()
        total_search = lookup_module._process_terms(terms, variables)
        return total_search[1]

    # Test exeption from _process_terms

# Generated at 2022-06-13 13:49:24.945926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access

    # Expected conditions
    # - When there is no matching file, an AnsibleLookupError is raised
    # - When there is a matching file, the path to that file is returned

    # test with no matching file
    loop = LookupModule()
    terms = ['doesntexist']
    variables = {}
    kwargs = {}
    with pytest.raises(AnsibleLookupError):
        loop.run(terms, variables, **kwargs)

    # test with a matching file
    test_file = os.path.join(os.path.dirname(__file__), 'test_first_found.txt')
    terms = [test_file]
    variables = {}
    kwargs = {}
    res = loop.run(terms, variables, **kwargs)


# Generated at 2022-06-13 13:49:31.505411
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(terms=['/etc/hosts','/etc/passwd','/dev/null'], variables = {}) == ['/etc/hosts']
    # expected list of paths
    assert lookup.run(terms=[{'files':'hosts,passwd,null', 'paths':'/etc,/dev'}, {'paths':'/dev/shm'}], variables={}) == ['/etc/hosts']
    # expected list of paths with extra comma
    assert lookup.run(terms=[{'files':'hosts,passwd,null', 'paths':'/etc,'}, {'paths':'/dev/shm'}], variables={}) == ['/etc/hosts']
    # expected list of paths with extra comma and semicolon

# Generated at 2022-06-13 13:49:41.693163
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def fake_find_file_in_search_path(vars, subdir, fn, ignore_missing=False):
        if fn == 'bar.txt':
            return '/path/to/bar.txt'
        elif fn == 'foo.txt':
            return '/path/to/foo.txt'
        elif fn == 'biz.txt' and 'paths' in vars:
            return '/path/to/biz.txt'
        return None

    import pytest

    LookupModule._templar = None
    LookupModule._loader = None

    with pytest.raises(AnsibleLookupError):
        # No files found
        assert LookupModule().run(terms=['/path/to/'], variables={}, skip=False)


# Generated at 2022-06-13 13:49:51.524681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import wrap_var


# Generated at 2022-06-13 13:50:09.421463
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    path_files = ['/tmp/files']
    path1 = '/tmp/path1'
    path2 = '/tmp/path2'
    path3 = '/tmp/path3'
    files1 = ['file1.txt', 'file2.txt']
    files2 = ['file3.txt', 'file4.txt']
    files3 = ['file5.txt', 'file6.txt']

    # First, we need to create a couple of files to make sure things works

    # Create path1, path2 and path3
    os.makedirs(path1)
    os.makedirs(path2)
    os.makedirs(path3)

    # Create files1 in path1
    for f in files1:
        open(os.path.join(path1, f), 'a').close()

    # Create

# Generated at 2022-06-13 13:50:10.277601
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 13:50:20.747364
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Case 1:
    # This test case includes the following scenarios:
    # 1. If using 'dual mode' (see description above), either a list of files 'terms' is used or a key 'files' with a list of files is required.
    # 2. If the lookup doesn't find an existing file, it terminates with an error message.
    # 3. In 'dual mode', if using a list of files 'terms', the lookup uses the file names or the list of file names in 'terms'.

    terms = ['/tmp/file1.txt', '/tmp/file2.txt', '/tmp/file3.txt']
    search_paths = ['/tmp']

    vars = { 'terms':terms, 'files':terms, 'paths':search_paths}

# Generated at 2022-06-13 13:50:32.433299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create plugin
    lm = LookupModule()
    lm._Subdir = 'files'

    # parameters
    terms = [
        {
            'files': 'foo, bar',
            'paths': '/path/to/foo.txt, /path/to/bar.txt',
            'skip': False
        },
        {
            'files': 'foo, bar',
            'paths': '/path/to/foo.txt, /path/to/bar.txt',
            'skip': True
        },
        {
            'files': 'foo, bar',
            'paths': '/path/to/foo.txt, /path/to/bar.txt',
            'skip': False
        },
    ]

    variables = dict()
    kwargs = dict()

    # run
    assert lm.run

# Generated at 2022-06-13 13:50:43.219402
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    # no terms
    terms = []
    variables = {}
    assert lm.run(terms, variables) == []
    # no files, no paths, no skip
    terms = [{}]
    variables = {}
    assert lm.run(terms, variables) == []
    # no files, no paths, skip
    terms = [{'skip': True}]
    variables = {}
    assert lm.run(terms, variables) == []
    # files, no paths, no skip
    terms = [{'files': 'bar'}]
    variables = {}
    assert lm.run(terms, variables) == []
    # files, no paths, skip
    terms = [{'files': 'bar', 'skip': True}]
    variables = {}

# Generated at 2022-06-13 13:50:52.736978
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test to test method run of class LookupModule
    # REVIEW: true unit test
    # REVIEW: add all assert statements
    # REVIEW: test all branches
    # REVIEW: each test should be independent
    test_terms = ['test1.txt', 'test2.txt']
    test_variables = {'test': 'test'}
    test_kwargs = {'files': ['test1.txt'], 'paths': ['.'], 'skip': True}
    lookup_instance = LookupModule()
    lookup_instance.run(test_terms, test_variables, **test_kwargs)



# Generated at 2022-06-13 13:50:58.468227
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text

    terms = {'files': 'foo.conf', 'paths': '/tmp/production,/tmp/staging'}
    variables = {'inventory_hostname': 'localhost'}
    kwargs = {'_original_basename': 'first_found'}

    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_name = temp_file.name
    temp_file.close()

    temp_dir = tempfile.mkdtemp()
    temp_file_1 = temp_dir + "/foo.conf"
    temp_file_2 = temp_dir + "/" + variables['inventory_hostname'] + ".conf"
    temp_file_3 = temp_dir + "/bar.conf"

    files

# Generated at 2022-06-13 13:50:59.991851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # done in test_lookup_plugins

    return

# Generated at 2022-06-13 13:51:03.965435
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        LookupModule.run()
    except Exception as e:
        # Return the exception
        return e
    else:
        # No exception was raised
        return None

# Generated at 2022-06-13 13:51:13.626580
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup a fake ansible to test with
    fake_ansible = FakeAnsible()
    fake_lookup = LookupModule(fake_ansible)

    # test a simple term
    terms = ["myfile.txt"]
    results = fake_lookup.run(terms, dict())
    assert results == "path/to/myfile.txt"

    # test a list of terms
    terms = [["myfile.txt", "otherfile.txt"]]
    results = fake_lookup.run(terms, dict())
    assert results == "path/to/myfile.txt"

    # test dict term
    terms = [dict(files="myfile.txt")]
    results = fake_lookup.run(terms, dict())
    assert results == "path/to/myfile.txt"

    # test dict term with

# Generated at 2022-06-13 13:51:45.321445
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a fake ansible structure
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    templar = Templar(loader=loader, variables=variable_manager)

    # create a lookup instance
    lookup = LookupModule()
    lookup._templar = templar

    # create data

# Generated at 2022-06-13 13:51:59.407677
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os.path
    import tempfile
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes

    # Test string variables, exact match
    terms = ['{{ existing_file }}', '{{ unmatching_file }}', '{{ existing_relative_file }}']
    variables = dict(existing_file=__file__)
    kwargs = dict(skip=False)

    total_search, _ = LookupModule()._process_terms(terms, variables, kwargs)
    matches = LookupModule().run(terms, variables, **kwargs)
    assert len(matches) == 1
    assert matches[0] == total_search[0]

    # Test list variable, exact match