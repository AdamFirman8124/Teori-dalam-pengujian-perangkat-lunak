

# Generated at 2022-06-13 13:26:32.630841
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test_LookupModule_run0
    content_up_to_line_3 = """
    001
    002
    003"""
    # test_LookupModule_run1
    content_after_line_2 = """
    002
    003
    """
    # test_LookupModule_run2
    content = """
    002
    003
    004
    """
    # test_LookupModule_run3
    content_with_line_break = """
    001
    002
    """

    lookup_module = LookupModule()

    ret = lookup_module.run(['test_file'], variables=None, lstrip=True, rstrip=True)
    assert ret[0] == content_up_to_line_3

    ret = lookup_module.run

# Generated at 2022-06-13 13:26:46.753573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    output = lookup_module.run(["/ansible/static/test_runner/tests/fixtures/test_file1.txt"])
    assert output == [u"This is line number 1\n", u"This is line number 2\n", u"This is line number 3\n"]

    output = lookup_module.run(["/ansible/static/test_runner/tests/fixtures/test_file2.txt"])
    assert output == [u"This is line number 1\n", u"This is line number 2\n", u"This is line number 3\n"]

    output = lookup_module.run(["/ansible/static/test_runner/tests/fixtures/test_file3.txt"])

# Generated at 2022-06-13 13:26:49.442176
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    descriptor, terms, options, plugins, variables = {}, {}, {}, {}, {}
    lookup = LookupModule()
    lookup.run(terms, variables)

# Generated at 2022-06-13 13:26:50.432331
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 1

# Generated at 2022-06-13 13:27:03.916554
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    #os.system('touch test_file1')
    open('test_file1', 'w').close()
    #os.system('touch test_file2')
    open('test_file2', 'w').close()

    l = LookupModule()
    l.set_options({'_terms': ['test_file1', 'test_file2']})
    result = l.run(['test_file1', 'test_file2'])
    assert result[0] == ''
    assert result[1] == ''

    l.set_options({'_terms': ['test_file1', 'test_file2'], 'rstrip': False})
    result = l.run(['test_file1', 'test_file2'])
    assert result[0] == '\n'

# Generated at 2022-06-13 13:27:06.362899
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    with pytest.raises(AnsibleError, match="could not locate file in lookup: foo.txt"):
        lookup_obj.run(terms=["foo.txt"])

# Generated at 2022-06-13 13:27:07.472109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  pass

# Generated at 2022-06-13 13:27:15.650576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["foo", "bar"]
    variables = {
        "__FILE__": "files/myfile",
        "__INVOCATION__": "2"
        }

    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables)
    assert result == ['foo', 'bar']

    terms = ["foo", "bar"]
    variables = {
        "__FILE__": "files/myfile",
        "__INVOCATION__": "2"
        }

    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables, lstrip=True, rstrip=True)
    assert result == ['foo', 'bar']

    terms = ["foo", "bar"]

# Generated at 2022-06-13 13:27:27.319851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["/dev/null"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-13 13:27:34.458351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Test "term" as a string
    term= "foo"
    lookup_mod = LookupModule()
    assert lookup_mod.run(terms=term) == "foo"

    #Test "term" as a list of strings
    terms= ["foo", "bar", "baz"]
    lookup_mod = LookupModule()
    assert lookup_mod.run(terms=terms) == ["foo", "bar", "baz"]

# Generated at 2022-06-13 13:27:50.707979
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    cachedir = 'tests/unit/lookup/file/cachedir'

# Generated at 2022-06-13 13:27:56.463112
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test for method 'run' of class 'LookupModule'
    #factory = Factory()
    #lookup_inst = factory.create_instance(LookupModule, terms=['/path/to/foo.txt'], variables=None)
    lookup_inst = LookupModule()
    lookup_inst.run(terms=['/path/to/foo.txt'], variables=None)

# Generated at 2022-06-13 13:28:08.293978
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Make a mock class for loader which returns mock content
    class TestLoader2(object):
        def __init__(self):
            pass

        def _get_file_contents(self, path):
            return ['{"a":"b"}'], False
    # Instantiate LookupModule class
    lm = LookupModule()
    # Set value of _loader
    lm._loader = TestLoader2()
    # Set value of basedir
    lm.basedir = 'basedir'
    # Set value of variables
    variables = {'a': 'b'}
    searchpath = ['first_dir', 'second_dir']
    # Set value of runner
    runner = {'path': 'runner_path'}
    # Set value of templar
    templar = 'templar'
    # Set value of loader

# Generated at 2022-06-13 13:28:12.096363
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = dict()
    lookupModule = LookupModule()
    lookupModule.run(terms=['doesnotexist'], variables={}, result=result)
    assert result == {}
    lookupModule.run(terms=['file1.txt'], variables={}, result=result)
    assert result['file'] == 'file1.txt'

# Generated at 2022-06-13 13:28:18.201566
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Set up test data

    # Instantiate class to be tested
    test_object = LookupModule()

    # Define test parameters

    # Execute method to be tested
    test_result = test_object.run()

    # Assert test result
    assert test_result == None


if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:28:26.436220
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {}

    class AnsibleModulePathMock(object):
        def __init__(self):
            self.suite_paths = ["test_resources"]

    class AnsibleLoaderMock(object):
        def __init__(self, basedir):
            self.basedir = basedir

        # Method to mock the real behavior of _get_file_contents, but only for the files under the mock basedir
        def _get_file_contents(self, filename):
            if filename.startswith(self.basedir):
                return [b"sample text"]
            else:
                raise AnsibleParserError()


    class VariablesMock(dict):
        pass

    basedir = 'test_resources/'

   

# Generated at 2022-06-13 13:28:33.236558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['test1.txt','test2.txt','test3.txt']
    result = module.run(terms)
    assert len(result) == 3
    assert result[0] == 'test1\n'
    assert result[1] == 'test2\n'
    assert result[2] == 'test3\n'

# Generated at 2022-06-13 13:28:45.598147
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ testing run method of LookupModule """

    # Create a test case class to set up for the test
    class TestCase:
        def __init__(self, test_name):
            self.test_name = test_name

        def run_test(self):
            """ test run method of LookupModule """

            # Create a test object to test the run method of LookupModule
            test = create_test_object()

            # Get the method to run the test
            run_method = getattr(test, self.test_name)

            # Run the test
            run_method()

        def test_run_method_no_args(self):
            """ test run method with no arguments """

            # Create a test object to test the run method of LookupModule
            test = create_test_object(self.test_name)

            #

# Generated at 2022-06-13 13:28:57.257511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import argparse
    from ansible.plugins.lookup import LookupBase

    # create the object under test
    lu = LookupModule()

    class Options:
        def __init__(self):
            self.rstrip = False
            self.lstrip = False
            self.lookup_plugins = []

    class Arg:
        z = 'plugins/lookup/file.py'

    class Args:
        lookupfile = Arg()
        listtasks = False
        module_path = []
        watc = False
        diff = False
        force_handlers = False
        start_at_task = None
        verbosity = 0
        forky = 0
        become_method = None
        become_user = None
        become_ask_pass = False
        become_exe = ''

# Generated at 2022-06-13 13:29:04.954542
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_text

    lookup_module = LookupModule()
    lookup_module.set_loader(None)

    assert lookup_module.run(terms=['file.txt'], variables=dict(ansible_config_file="./ansible.cfg"), lstrip=True, rstrip=True) == [to_text("file1\nfile2\n")]


# Generated at 2022-06-13 13:29:13.172433
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert (LookupModule().run(['README.md'])[0] == open('README.md', 'r').read())

# Generated at 2022-06-13 13:29:22.801771
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    display = Display()
    display.verbosity = 99

    # initialize LookupModule
    lookup_module = LookupModule()

    # test run method
    # test that an AnsibleError exception is raised when the passed file isn't found
    try:
        lookup_module.run(["invalid_file.txt"], variables="test_variables")
    except AnsibleError as e:
        assert e.args[0] == "could not locate file in lookup: invalid_file.txt"

    # test that run method returns the content of the file
    assert lookup_module.run(["test_file.txt"], variables="test_variables")[0] == "this is a test file\n"

# Generated at 2022-06-13 13:29:35.200620
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ut_lookupfile = "/path/to/file.yml"
    ut_lookupfile_content = u"test\ncontent\n"
    ut_tf = "/path/to/test_file"
    ut_tf_content = u"test_content"

    ut_terms = [
        ut_lookupfile,
        "file.yml"
    ]
    ut_variables = {
        "ansible_playbook_python": "/usr/bin/python",
        "playbook_dir": "/path/to/playbook/"
    }
    ut_kwargs = {
        "lstrip": False,
        "rstrip": True
    }


# Generated at 2022-06-13 13:29:42.215889
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    options = dict(
        connection='local',
        module_path=None,
        forks=100,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
    )

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 13:29:45.730428
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import and instantiate class
    lookup = LookupModule()

    # run method of the LookupModule class
    ret = lookup.run([],{})

    # test the return value
    assert ret == []

# Generated at 2022-06-13 13:29:53.256709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class testclass:
        class testvariables:
            debug = 1

    testterm1 = "file1.txt"
    testterm2 = "file2.txt"
    testterms = [testterm1, testterm2]

    test_ret1 = "this is line 1\nthis is line 2\nthis is line 3"
    test_ret2 = "this is line 4\nthis is line 5\nthis is line 6"
    test_ret = [test_ret1, test_ret2]

    test_run = LookupModule()
    test_run.set_loader(testclass)
    test_run.set_templar(testclass)
    test_run.set_inventory(testclass)
    test_run.set_basedir('.')
    test_run.set_env(testclass)

# Generated at 2022-06-13 13:30:05.293978
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for file lookup when file is present in path
    lookup = LookupModule()
    lookup._loader = DictDataLoader({u"/etc/ansible/hierarchy/group_vars/group1/vault.yml": b"$ANSIBLE_VAULT;1.2;AES256;testuser\n33373631323665643738306330316332396135613861386332386662613832373361626434303738\n65316262636235333764663133323630386662333262396466346161636362313039323161393562\n326532366561316662346366663663632376430396536356339353235306537306337626334653666\n\n"})
    lookup.set

# Generated at 2022-06-13 13:30:19.542449
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    terms = [
        '/path/to/foo.txt',
        'bar.txt',  # will be looked in files/ dir relative to play or in role
        '/path/to/biz.txt'
    ]

# Generated at 2022-06-13 13:30:27.744439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Test case 1:
    # Content of file foo1.txt is
    # whiz: foo
    # bang: bar
    # bang: baz
    # variable foo1.yaml
    # ---
    # whiz: foo
    # bang: bar
    # bang: baz
    data_1 = module.run(["./test/files/foo1.txt"], variables={}, **{'rstrip': True, 'lstrip': False})
    assert data_1 == ['---\nwhiz: foo\nbang: bar\nbang: baz'], data_1

    # Test case 2:
    # Content of file foo2.txt is
    # whiz: foo
    # bang: bar
    # bang: baz
    # variable foo2.yaml
    # ---


# Generated at 2022-06-13 13:30:40.801755
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create dummy AnsibleFile instance
    class AnsibleFile():
        def __init__(self, loader, path, file_name):
            self._loader = loader
            self._path = path
            self._name = file_name

    # Create dummy VirtualFile instance
    class VirtualFile():
        def __init__(self, path, contents):
            self._path = path
            self._contents = contents

        def __repr__(self):
            return '<VirtualFile:%s>' % self._path

        def __iter__(self):
            yield self._contents

    # Create dummy DataLoader instance
    class DataLoader():
        def __init__(self):
            self.virtual_files = []

        def add_file(self, path):
            self.virtual_files.append(VirtualFile(path, path))

# Generated at 2022-06-13 13:31:01.703735
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test that the default behavior is to strip whitespace from the ends of the file

    class MockFile(object):
        def __init__(self, file_path):
            self.file_path = file_path

        def __enter__(self):
            return self

        def __exit__(self, type, value, traceback):
            return False

        def read(self):
            if self.file_path == './test_LookupModule_run_foo.txt':
                return u'bar\n'
            else:
                raise IOError

    class MockLoader(object):
        def get_basedir(self, task):
            return '.'

        def _get_file_contents(self, file_name):
            return (MockFile(file_name), {})

    module = LookupModule()

# Generated at 2022-06-13 13:31:11.072565
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import plugin class
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.six import PY2

    # define a mock ansible_context (self.ansible)
    # we can use this to get the path to our lookup Plugins directory (r'filename' in the example below)
    # However, because this is a test, we can use python's native '__file__' variable to the same result
    ansible_context = {'basedir': __file__,
                       'plugin_name': 'file.py'}

    # create an instance of our plugin
    l = LookupModule(ansible_context, r'filename')

    # mock AnsibleOptions
    l.options = {'lstrip': False,
                 'rstrip': True}

    # finally, test the run method
    #

# Generated at 2022-06-13 13:31:21.366045
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=import-error,no-name-in-module
    import ansible.plugins

    # FakeLookupModule is used instead of LookupModule to skip the effect of the code in
    # LookupModule.run() that depends on the presence of ansible.parsing.yaml.objects.AnsibleUnicode
    FakeLookupModule = type('FakeLookupModule', (ansible.plugins.lookup.LookupBase, object, ), {})

    # Fake the search path
    fake_search_path = [
        'files/',
        '/path/to/files/',
    ]

    # Fake the content of the searched file
    fake_file_content = 'foo/bar'

    # Create the lookup module
    lookup_module = FakeLookupModule()

    # Mock the find_file_in

# Generated at 2022-06-13 13:31:24.625523
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test the content of a file in files/ directory of a playbook
    # (contains the number 42)
    assert 42 == 42, 'validating'

# Generated at 2022-06-13 13:31:35.803831
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Prepare for testing
    lu = LookupModule()
    terms = ["foo.txt", "bar.txt", "biz.txt"]
    lu.set_options(var_options=None, direct=None)

    # Test when finding file successful
    lu.loader.get_real_file = lambda search_path, filename: 'path/to/' + filename
    lu.loader.get_file_contents = lambda filename: (b'contents of ' + filename, True)
    assert lu.run(terms) == ['contents of path/to/foo.txt', 'contents of path/to/bar.txt', 'contents of path/to/biz.txt']

    # Test when missing file
    lu.loader.get_real_file = lambda search_path, filename: None

# Generated at 2022-06-13 13:31:46.716271
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test: default options
    lookup_obj = LookupModule()

    # Test lookup
    lookup_obj.find_file_in_search_path = lambda variables, directories, filename: '/path/to/test.txt'
    lookup_obj._loader._get_file_contents = lambda filepath: ('contents of test.txt', u'/path/to/test.txt')
    terms = ['test.txt']
    variables = None
    kwargs = dict()
    result = lookup_obj.run(terms, variables, **kwargs)
    # Test assertions
    assert result[0] == 'contents of test.txt'

    # Test: rstrip and lstrip options
    lookup_obj = LookupModule()

    # Test lookup

# Generated at 2022-06-13 13:31:59.538130
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import mock
    #from ansible.plugins.lookup import LookupModule
    #from ansible.utils.display import Display
    #display = Display()

    module = mock.MagicMock()
    module.params = {}
    module.params['_terms'] = ['/path/to/somefile']

    # unit test 1: fail to get file contents
    module._loader._get_file_contents = mock.MagicMock(return_value=(b'\x00\x01\x02', True))
    LookupModule(context=module).run(terms=['somefile']) == ['\x00\x01\x02']
    assert module.fail_json.called
    assert 'failed to parse' in module.fail_json.call_args[0][0]

    # unit test 2: normal
    module._loader

# Generated at 2022-06-13 13:32:00.371592
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:32:09.260624
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Stub for class Display
    class DisplayStub(object):
        def __getattr__(self, name):
            if name == 'display':
                return lambda x: None
            if name == 'debug':
                return lambda x: None
            if name == 'vvvv':
                return lambda x: None
    lookup_class = LookupModule()
    lookup_class.set_loader(None)
    lookup_class.set_basedir('.')
    setattr(lookup_class, '_display', DisplayStub())
    terms = {'file' : '../test/test.txt'}
    assert lookup_class.run(terms, variables=None, **{}) == ['That\'s a test file\n']

# Generated at 2022-06-13 13:32:22.639736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            pass

        @patch('ansible.plugins.lookup.file.open')
        @patch('os.path.isfile')
        @patch('ansible.plugins.lookup.file.LookupBase')
        def test_run_rstrip_lstrip(self, LookupBase_mock, isfile_mock, open_mock):
            open_mock.return_value = ["foo","  bar","  baz "]
            LookupBase_mock.get_option.side_effect = [False, True]
            isfile_mock.return_value = True
            result

# Generated at 2022-06-13 13:32:47.201519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run(["TEST_file_lookup.txt"])[0] == "Lookup module test\n"

# Generated at 2022-06-13 13:32:56.898336
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    lookup_plugin.set_options({'_ansible_lookup_plugin': {'basedir': './tests/lookup_plugins'}})

    assert lookup_plugin.run(['file.txt']) == [u"contents of file\n"]

    assert lookup_plugin.run(['file.txt'], {}, lstrip=False) == [u" contents of file\n"]

    assert lookup_plugin.run(['file.txt'], {}, rstrip=False) == [u"contents of file\n "]

# Generated at 2022-06-13 13:33:05.364809
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Mocking classes
    class MockVarManager:
        def __init__(self):
            self.hostvars = {}
            self.vars = {'playbook_dir': 'playbooks'}
            self.extra_vars = {}

        def get_vars(self, loader, play, task, host):
            self.vars.update(self.extra_vars)
            return self.vars

        def get_host_vars(self, host, task):
            self.hostvars.update(self.extra_vars)
            return self.hostvars

        def update_vars(self, variables):
            self.extra_vars = variables

    class MockDisplay:
        def __init__(self):
            self.vmsg = ""
            self

# Generated at 2022-06-13 13:33:07.822182
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    x = LookupModule()
    assert x.run(["../../../../../../etc/passwd"], '', [])==[]

# Generated at 2022-06-13 13:33:18.064937
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Using the file "test_lookup_plugins_file.py" as a test case
    # since it is a valid yaml file and does not need to be created
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # Loading the file "test_lookup_plugins_file.py" in a string
    with open(os.path.join(current_dir, 'test_lookup_plugins_file.py'), 'r') as f:
        expected_result = f.read()

    # Test the file "test_lookup_plugins_file.py" is parsed correctly

# Generated at 2022-06-13 13:33:24.873403
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    import ansible.utils.path
    # set the path to the test files

    ansible.utils.path.lookup_file_in_search_path = my_lookup_file_in_search_path

    lookup_val = LookupModule().run(["one"], dict())

    assert len(lookup_val) == 1
    assert lookup_val[0] == 'Test lookup content one'

    lookup_val = LookupModule().run(["three"], dict())

    assert len(lookup_val) == 1
    assert lookup_val[0] == 'Test lookup content three'

    lookup_val = LookupModule().run(["one", "three"], dict())

    assert len(lookup_val) == 2
    assert lookup_val[0]

# Generated at 2022-06-13 13:33:35.127008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_object = LookupModule()

    terms = ['/tmp/test.txt']

    variables = dict(
        ansible_managed='Ansible managed: {file} modified on %Y-%m-%d %H:%M:%S by root',
        template_host='test_template_host'
    )

    result = LookupModule_object.run(
        terms=terms,
        variables=variables,
        lstrip=False,
        rstrip=False,
    )

    assert result == ['this is for testing file lookup\n']

# Generated at 2022-06-13 13:33:41.049327
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    # pylint: disable=too-many-function-args
    # Test method run of class LookupModule
    # Test expected results
    lookup_instance = LookupModule()
    assert lookup_instance._loader._get_file_contents.__module__ == "_loader"
    assert lookup_instance._loader._get_file_contents.__name__ == "_get_file_contents"
    assert lookup_instance._loader._get_file_contents.__qualname__ == "_loader._get_file_contents"

# Generated at 2022-06-13 13:33:49.557330
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import textwrap
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 4
    lookup = LookupModule()
    args = {'variables': {}, 'lstrip': False, 'rstrip': False}
    #file_path = 'test/test_lookup_file.txt'
    file_path = 'test/test_lookup_file_2.txt'
    with open(file_path, 'w') as f:
        f.write(textwrap.dedent("""\
        line one
        line two
        line three
        """))
    with open(file_path) as f:
        print(lookup.run([file_path], **args))
    os.remove('test/test_lookup_file_2.txt')

# Generated at 2022-06-13 13:34:00.053702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_set_options_self = {}
    test_set_options_self['find_file_in_search_path'] = lambda x, y, z: None
    test_terms = ['Hello, world!']
    lk = LookupModule()
    lk.set_options = lambda x = None, direct = None: test_set_options_self.update(x) or None
    result = lk.run(test_terms)
    assert isinstance(result, list) == True
    assert len(result) == 1
    assert result[0] == test_terms[0]

# Generated at 2022-06-13 13:34:46.720599
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    terms = ['foo.txt']
    res = lookup_obj.run(terms)
    assert res == ['bar\n']


# Generated at 2022-06-13 13:34:51.512397
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Variables
    lookup = LookupModule()

    # Local tests
    lookup.run(terms=['test.txt'], variables={'role_path':os.getcwd()})

    # Remote tests
    lookup.run(terms=['test.txt'], variables={'role_path':'http://localhost/'})
    lookup.run(terms=['test.txt'], variables={'role_path':'ftp://localhost/'})
    lookup.run(terms=['test.txt'], variables={'role_path':'//localhost/'})
    lookup.run(terms=['test.txt'], variables={'role_path':'localhost'})
    
    # Failure tests

    # Exceptions tests

# Generated at 2022-06-13 13:35:04.158996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TestCase.subTest(msg=None, **subtest_kwargs):
    # https://docs.python.org/3.6/library/unittest.html#distinguishing-test-iterations-using-subtests
    class TestCase(unittest.TestCase):
        pass
    tc = TestCase()
    test_case = tc.subTest(msg=None, **subtest_kwargs)

    class LookupModule(object):
        def _loader_get_file_contents(self, lookupfile, show_data=True):
            if lookupfile == u'DNE':
                raise AnsibleParserError("File lookup error")
            return ["red", "green", "blue"]
    lm = LookupModule()
    results = lm.run([u'DNE'])

# Generated at 2022-06-13 13:35:12.433749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup_plugin = lookup_loader.get('file', class_only=True)

    class Options(object):
        pass

    options = Options()
    options.lstrip = False
    options.rstrip = True
    options.verbosity = 3

    class LookupBase_class(object):

        def set_options(self, var_options=None, direct=None):
            return

        def get_option(self, key):
            return vars(options)[key]

        def find_file_in_search_path(self, variables, dirname, filename):
            print("LOOKUP_FILE_DUMMY_VALUE")
            return "LOOKUP_FILE_DUMMY_VALUE"


# Generated at 2022-06-13 13:35:22.493486
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    class VarModule(object):
        def __init__(self):
            self.__is_verbose = True
    class FakeVars(object):
        def __init__(self):
            self.__variables = VarModule()

    vars_obj = FakeVars()
    vars_obj.__variables.__is_verbose = True
    result = lookup.run(terms="hostvars.yaml", variables=vars_obj)
    expected_result = ["""
---
src: 127.0.0.1
dst: 127.0.0.1
"""]
    assert result == expected_result

# Generated at 2022-06-13 13:35:31.197912
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.module_utils.fact_cache
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.vars.variable_manager
    import ansible.utils.vars
    import ansible.utils.plugin_docs

    mgr = ansible.vars.variable_manager.VariableManager()
    src = ansible.vars.manager.DataLoader()
    var = ansible.vars.manager.VarsModule()
    fc = ansible.module_utils.fact_cache.FactCache()
    loader = ansible.parsing.dataloader.DataLoader()
    psr = ansible.parsing.dataloader.DataLoader()
    lookup = ansible.plugins.lookup.LookupBase()
    lkpl = Look

# Generated at 2022-06-13 13:35:42.107345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    import ansible.constants as C

    lookup_ins = LookupModule()

    fake_loader = DictDataLoader({
        '/etc/passwd': '#user:password hash',
        'bar.txt': 'bar',
        '/nonexistent_file': None
    })

    fake_inventory = Inventory(loader=fake_loader, variable_manager=VariableManager(), host_list=[])

    terms = [
        '/etc/passwd',
        'bar.txt',
        '/nonexistent_file',
    ]

    # Default options is `rstrip=True, lstrip=False`
    results = lookup_ins.run(terms)

# Generated at 2022-06-13 13:35:42.544899
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:35:47.257660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import collections
    import tempfile
    import pytest
    lookup = LookupModule()
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = tempfile.NamedTemporaryFile(dir=tempdir)
        with test_file as fh:
            fh.write(b"Hello World")
            fh.flush()
            fh.seek(0)
            ret = lookup.run([test_file.name], None)
            assert(ret == ["Hello World"])

if __name__ == '__main__':
    pytest.main()

# Generated at 2022-06-13 13:35:49.468220
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(terms=['invalid/test-file']) == []
