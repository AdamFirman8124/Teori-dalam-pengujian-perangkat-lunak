

# Generated at 2022-06-13 13:26:29.537597
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Run method of class LookupModule with arguments: terms=['test_file.txt'], variables=None, **kwargs
    # test_file.txt contains string: test_file
    lookupModule = LookupModule()
    assert(['test_file'] == lookupModule.run(terms=['test_file.txt'], variables=None, **kwargs))

# Generated at 2022-06-13 13:26:30.940050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ test_LookupModule_run """



# Generated at 2022-06-13 13:26:38.115444
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = [{"_terms": "{{file_name}}", "rstrip": False}]
    variables = {"file_name": "file_name"}
    kwargs = {"_terms": "{{file_name}}", "rstrip": False}

    test_obj = LookupModule(terms=terms, variables=variables, **kwargs)
    result = test_obj.run(terms, variables, **kwargs)
    print(result)


if __name__ == "__main__":
    # Execute only if run as a script
    test_LookupModule_run()

# Generated at 2022-06-13 13:26:48.807102
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    lookup_module = LookupModule()
    # Test with file that does not exist
    with pytest.raises(AnsibleError) as exc:
        lookup_module.run(["/path/to/nonexist.txt"])
    assert exc.value.message == "could not locate file in lookup: /path/to/nonexist.txt"
    # Test with a single real file
    content = lookup_module.run(["fixme_nonexisting_file.py"])[0]
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           "fixme_nonexisting_file.py")) as f:
        assert content == f.read()
    # Test with multiple

# Generated at 2022-06-13 13:27:02.993930
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.plugins.lookup.file import LookupModule
    from ansible.template import Templar

    lookup_class = LookupModule(play_context=PlayContext())
    lookup_class.set_options(dict(plugins=dict(), environ=dict()))
    lookup_class._templar = Templar()

    test_list = [
        "json_order_test.json",
        "/dev/null"
    ]

    results = lookup_class.run(test_list)

    assert "\n" in results[0]
    assert "\n" in results[1]
    options = read_docstring(LookupModule.__doc__)["options"]
    assert type(options)

# Generated at 2022-06-13 13:27:10.703173
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with a string
    assert LookupModule(None).run(["str"], dict()) == [u'str']
    # test with a byte string
    assert LookupModule(None).run([b"str"], dict()) == [u'str']
    # test with an array
    assert LookupModule(None).run([['a', 'b'], 'c'], dict()) == [u'a,b', u'c']
    # test with a dict
    assert LookupModule(None).run([{'a':'b'}], dict()) == [u'{"a": "b"}']

# Generated at 2022-06-13 13:27:17.172827
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.get_basedir = lambda: "/root"
    assert lookup_module.run(['myfile.txt']) == [u'mycontents']
    assert lookup_module.run(['myfile.txt', 'myfile2.txt']) == [u'mycontents', u'mycontents2']
    lookup_module.get_basedir = lambda: "/root/doesnt_exist"
    assert lookup_module.run(['myfile.txt']) == []
    lookup_module.set_options(direct={'rstrip': False, 'lstrip': True})
    assert lookup_module.run(['myfile.txt']) == [u'\nmycontents\n  ']

# Generated at 2022-06-13 13:27:20.580652
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/etc/passwd']
    lookupModule = LookupModule()
    entries = lookupModule.run(terms)
    assert entries[0].split(':')[0] == 'root'

# Generated at 2022-06-13 13:27:27.016776
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test_data_type; INPUT data is a text string list
    terms = ['/path/to/foo.txt', 'bar.txt', '/path/to/biz.txt']
    rm = LookupModule()

    # test_mode; INPUT option is False
    ret = rm.run(terms, variables=None, **{'lstrip':False, 'rstrip':False})[0]
    assert ret == u'a line of text\na line of text\na line of text\n', \
            'Expected "a line of text\\na line of text\\na line of text\\n" result but got "%s"' % ret

    # test_mode; INPUT option is True
    ret = rm.run(terms, variables=None, **{'lstrip':True, 'rstrip':True})[0]

# Generated at 2022-06-13 13:27:37.769419
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MyLookupModule(LookupModule):
        def __init__(self, loader=None, templar=None, **kwargs):
            self._loader = loader
            self._templar = templar

    ##################################################################
    # mock class `MyLookupModule`
    ##################################################################
    class mock_AnsibleParserError(AnsibleParserError):
        pass

    class mock_AnsibleError(AnsibleError):
        pass

    class mock_AnsibleFileNotFound(AnsibleFileNotFound):
        pass

    class mock_AnsibleFileSystemError(AnsibleFileSystemError):
        pass

    class mock_AnsibleFileExists(AnsibleFileExists):
        pass

    class mock_AnsibleFileSkip(AnsibleFileSkip):
        pass

# Generated at 2022-06-13 13:27:51.732770
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    v = {'foo': 'bar'}

    # Test YAML hash
    terms = ['/etc/ansible/facts.d/foo.fact']
    result = lookup.run(terms, variables=v)
    assert len(result) == 1
    assert result == [u'foo: bar']

    # Test YAML list
    terms = ['/etc/ansible/facts.d/bar.fact']
    result = lookup.run(terms, variables=v)
    assert len(result) == 1
    assert result == [u'- bar']

    # Test plain text
    terms = ['/etc/ansible/facts.d/baz.fact']
    result = lookup.run(terms, variables=v)
    assert len(result) == 1

# Generated at 2022-06-13 13:27:54.552620
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run([]) == []
    assert module.run(['not_exist_file']) == []

# Generated at 2022-06-13 13:28:06.307157
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['inventory/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    lookup_res = LookupModule().run(['defaults.yml'], variable_manager)[0]


# Generated at 2022-06-13 13:28:14.297238
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    testlookup = LookupModule()
    testlookup.set_loader("something")
    setattr(testlookup._loader, '_get_file_contents', lambda self, x: ('Test contents 1','Test contents 2'))
    assert testlookup.run(['testfile.txt']) == ['Test contents 1']

    setattr(testlookup._loader, '_get_file_contents', lambda self, x: ('Test contents 3','Test contents 4'))
    assert testlookup.run(['testfile.txt']) == ['Test contents 3']

    setattr(testlookup._loader, '_get_file_contents', lambda self, x: ('Test contents 5','Test contents 6'))
    assert testlookup.run(['testfile.txt']) == ['Test contents 5']


# Generated at 2022-06-13 13:28:24.371361
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Test the lookup module.
    '''
    import os.path
    import sys
    import yaml
    # Use in-code defined fixture
    lookupBase = LookupModule()
    curr_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    lookupBase.set_loader(curr_dir)

    # Test file reading
    term = "file_test_1.txt"
    file_name = os.path.join('fixtures', term)
    with open(file_name, "rb") as f:
        expected_output = f.read().decode("utf-8").rstrip()
    output = lookupBase.run((term,), {}, lstrip=False, rstrip=False)
    assert(expected_output == output[0])
    output

# Generated at 2022-06-13 13:28:26.551699
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = ['/etc/foo.txt']
    result = l.run(terms, variables=None, **{'lstrip': True, 'rstrip': True})
    assert result == ['foo']

# Generated at 2022-06-13 13:28:38.756351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    from io import StringIO
    import sys
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    import ansible.constants as C

    display = Display()
    display.verbosity = 3
    options = dict()

    variable_manager = VariableManager()
    loader = DataLoader()

    # Create inventory and pass to var manager
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    # create

# Generated at 2022-06-13 13:28:54.163238
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    mock_entries = ["/path/to/foo.txt", "bar.txt", "/path/to/biz.txt"]
    mock_variables = {"role_path" : "/home/user/test/roles/common"}

    def return_test_file_path(*args, **kwargs):
        if kwargs["terms"][0] == "/path/to/foo.txt":
            return "/home/user/test/roles/common/files/foo.txt"
        elif kwargs["terms"][0] == "bar.txt":
            return "/home/user/test/roles/common/bar.txt"

# Generated at 2022-06-13 13:29:06.539151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat import jinja2_native, six

    '''Unit test for class LookupModule method run()'''


# Generated at 2022-06-13 13:29:14.348800
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:29:27.593311
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    for term, contents in [('somefile', 'somecontents'), ('someotherfile', 'someothercontents')]:
        path = lookup._loader.path_dwim(term)
        with open(path, 'w') as f:
            f.write(contents)

    assert lookup.run(['somefile']) == ['somecontents']
    assert lookup.run(['somefile', 'someotherfile']) == ['somecontents', 'someothercontents']

    os.unlink(path)

# Generated at 2022-06-13 13:29:42.099905
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import builtins
    display = BuiltinModuleMock('display')

    l = LookupModule(loader=None, templar=None, shared_loader_obj=None)
    l.display = display

    assert l.run([], variables={}, lstrip=False, rstrip=False) == []
    assert display.display_args[0] == "File lookup term: None"

    display._display.reset_mock()

    l.find_file_in_search_path = MagicMock()
    assert l.run(["/etc/foo.txt"], variables={}, lstrip=False, rstrip=False) is None
    assert display.display_args[0] == "File lookup term: /etc/foo.txt"

    display._display.reset_mock()

   

# Generated at 2022-06-13 13:29:49.983320
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_LookupModule_run.file_exists = True
    test_LookupModule_run.dir_exists = True

    class LookupModuleTester(LookupModule):
        def __init__(self, *args, **kwargs):
            pass

        def _get_file_contents(self, path):
            return "content"

        def _get_path_from_terms(self, terms):
            return terms

        def _loader_get_path_from_terms(self, terms):
            return terms

        def _loader_get_relative_path(self, name):
            return name

        def _loader_path_exists(self, path):
            if test_LookupModule_run.file_exists:
                return True

# Generated at 2022-06-13 13:29:55.031448
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['foo.txt', 'bar.txt', 'biz.txt']
    variables = {'ansible_lsb': None}
    results = module.run(terms, variables)
    assert results == ['foo content', 'bar content', 'biz content']

# Generated at 2022-06-13 13:30:00.434008
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Initialize
    lookup_plugin = LookupModule()

    # When term has a value then the method run should raise an error
    terms = ['test.txt']
    result = lookup_plugin.run(terms)
    assert isinstance(result, list), 'AnsibleError not handled properly'

# Generated at 2022-06-13 13:30:11.218498
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_path = os.path.normpath('test/test.txt')
    module = LookupModule()
    content = module.run([test_path])
    assert(content[0] == 'test')
    module.set_options(**{'lstrip': True})
    module.set_options(**{'rstrip': True})
    content_lstrip = module.run([test_path])
    assert(content_lstrip[0] == 'test')
    content_rstrip = module.run([test_path])
    assert(content_rstrip[0] == 'test')
    content_lstrip_rstrip = module.run([test_path])
    assert(content_lstrip_rstrip[0] == 'test')

# Generated at 2022-06-13 13:30:22.738600
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    # Test find_file_in_search_path for 'files'
    files = [
        ('/etc/foo.txt', 'FOO'),
        ('/etc/bar.txt', 'BAR'),
        ('/etc/baz.txt', 'BAZ'),
        ('/etc/biz.txt', 'BIZ'),
        ('/etc/boz.txt', 'BOZ'),
    ]
    for path, content in files:
        with open(path, 'w') as f:
            f.write(content)


# Generated at 2022-06-13 13:30:33.248843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.loader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    play = Play().load('test_playbook.yml', loader=loader, variable_manager=VariableManager(), loader_type='yaml')
    task1 = play.get_tasks()[0]
    lookup = task1.args['terms']
    assert lookup[0] == '/etc/foo.txt'
    assert lookup[1] == 'bar.txt'
    assert lookup[2] == '/path/to/biz.txt'

# Generated at 2022-06-13 13:30:38.069003
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This unit test was create with pytest-bdd python package
    # GIVEN a lookup module
    # WHEN run method is called
    # THEN check if run method finish without exceptions
    # AND check if returned value is the expected
    pass

# Generated at 2022-06-13 13:30:48.453028
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # FIXME: does not look like ansible module at all
    # should just test for expected results
    # rather than using fake ansible object
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    class FakeOptions:
        verbosity = 0
        connection = 'local'

    class FakeVariableManager:
        def __init__(self):
            self.vars = {
                'playbook_dir': '/playbook',
            }

    class FakeHost:
        name = 'testhost'

    class FakePlay:
        vars = {
            'foo': 'bar',
        }

    class FakeTask:
        vars = {
            'role_path': '/playbook/roles'
        }

    class FakeInventory:
        hosts = {}
       

# Generated at 2022-06-13 13:31:08.901540
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Configure return value for method find_file_in_search_path of class LookupModule
    test_1 = 'test_1'
    test_2 = 'test_2'

    def find_file_in_search_path(variables, directory, term):
        if (term == test_1):
            return test_1
        elif (term == test_2):
            return test_2
        else:
            return

    lookupModule = LookupModule()
    lookupModule.find_file_in_search_path = find_file_in_search_path

    # Configure return value for method _get_file_contents of class DataLoader
    test_3 = 'test_3'
    test_4 = 'test_4'
    test_5 = 'test_5'

# Generated at 2022-06-13 13:31:20.465646
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    from ansible.plugins.loader import lookup_loader
    # _get_file_contents
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    lm = lookup_loader.get('file', loader=loader, basedir='/home/vagrant',
                           variables={'lookup_file': 'lookup_fixtures/file3.txt'})

    assert 'this is file3\n' == lm.run(['{{lookup_file}}'],
                                       variables={'lookup_file': 'lookup_fixtures/file3.txt'},
                                       lstrip=False, rstrip=False)[0]

# Generated at 2022-06-13 13:31:31.860488
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockDisplay:
        def debug(self, msg):
            return

    class MockAnsibleError(Exception):
        pass

    class MockAnsibleParserError(Exception):
        pass

    class MockLoader:
        def __init__(self):
            self.path_results = []
            self.path_results.append('C:\\ansible\\files\\foo.txt')

        def _get_file_contents(self, lookupfile):
            return b'The contents of foo.txt', None

        def _find_file_in_search_path(self, tokens, env_var_name, subdir_name, pathsep=u':'):
            for result in self.path_results:
                if tokens[-1] in result:
                    return result
            return None


# Generated at 2022-06-13 13:31:35.960841
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module._loader.path_dwim('files', 'files/bar.txt') == module._loader.path_dwim('files', 'bar.txt')

# Generated at 2022-06-13 13:31:45.902302
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    lookupModule.set_loader({
        '_get_file_contents': lambda lookupfile: (b' \n', False)
    })
    results = lookupModule.run([], {}, rstrip=False, lstrip=False)
    assert results == [b' \n']
    results = lookupModule.run([], {}, rstrip=False, lstrip=True)
    assert results == [b'\n']
    results = lookupModule.run([], {}, rstrip=True, lstrip=False)
    assert results == [b' \n']
    results = lookupModule.run([], {}, rstrip=True, lstrip=True)
    assert results == [b'']

# Generated at 2022-06-13 13:31:47.303583
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_LookupModule = LookupModule()


# Generated at 2022-06-13 13:32:00.229202
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    # importing os here has the side-effect of adding ansible/plugins/files to sys.path
    # We need this so that lookup_plugins/file.py can be found. It is not on
    # sys.path normally.
    # (No additional side-effects were observed when I tried to import
    # other modules that are not available on python3, so it appears that
    # this approach is safe.)
    #
    # The contents of ansible/plugins/files are copied from the
    # git master branch of Ansible as of commit
    #
    # cb00dcee7b1a94e34d7c4a3d4b7c77b48fdb7dac
    #
    # The following files have been deleted, because they are not relevant
    # for unit testing lookup_plugins/file.py:

# Generated at 2022-06-13 13:32:09.943878
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up
    fd, lookupfile = tempfile.mkstemp(dir='/tmp')
    os.close(fd)
    contents = ["file contents", "line 2", "line 3", "line 4"]
    with open(lookupfile, 'w') as f:
        f.write("\n".join(contents))

    # Test rstrip=True, lstrip=False, terms=lookupfile
    lookup_params = dict(
        _loader=DictDataLoader(dict(files={}))
    )
    lookup = LookupModule(**lookup_params)
    result = lookup.run(terms=[lookupfile], variables={})

    # Check
    assert len(result) == 1
    assert result[0] == "\n".join(contents)
    # Clean up

# Generated at 2022-06-13 13:32:12.391332
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lmodule = LookupModule()
    # TODO [JD] Add unit tests
    assert True == True

# Generated at 2022-06-13 13:32:24.648884
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.path import unfrackpath
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import os
    import pytest
    import tempfile
    test_directory = tempfile.mkdtemp()
    test_file_path = os.path.join(test_directory, 'test_file')
    test_file_content = 'testing'
    f = open(test_file_path, 'w')
    f.write(test_file_content)
    f.close()
    print("test_LookupModule_run test directory: %s" % test_directory)

    # create the lookup module
    lookup_paths = [unfrackpath(test_directory)]
    arg_options = {}
    loader = DictDataLoader()

# Generated at 2022-06-13 13:33:00.375604
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1: single file lookup
    lookup = LookupModule()
    lookup._templar = DummyTemplar(variables={})
    lookup._loader = DummyLoader(path_exists_map={
        'dummy_path': {
            'test.txt': 'hello world',
        }
    }, default_basedir='dummy_path')
    result = lookup.run(['test.txt'])
    assert result == ['hello world']

    # Test 2 with lstrip and rstrip,
    lookup = LookupModule()
    lookup.set_options(var_options={}, direct={'lstrip': True, 'rstrip': True})
    lookup._templar = DummyTemplar(variables={})

# Generated at 2022-06-13 13:33:05.824415
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests import unittest

    display = Display()
    display.verbosity = 0

    lm = LookupModule()

    # Tests the error conditions of the run method
    with unittest.TestCase() as tc:
        tc.assertRaises(AnsibleError, lm.run, terms='')

    display.verbosity = 1

# Generated at 2022-06-13 13:33:16.396414
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def file_loader(self, path, file, templar, **kwargs):
        return (b'contents', path)

    def find_file_in_search_path(self, variables, path, file):
        return path + file

    from unittest import mock
    import os

    test_dir = os.path.dirname(os.path.realpath(__file__))

    test_terms = ['foo.txt', 'bar.txt']
    test_variables = {'my_var': '1'}


# Generated at 2022-06-13 13:33:20.842618
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    display = Display()
    display.debug("Test lookup module file")
    file_content = lookup_module.run(["/etc/hosts"])
    assert(type(file_content) is list)
    assert(type(file_content[0]) is str)
    assert("127.0.0.1" in file_content[0])

# Generated at 2022-06-13 13:33:24.645715
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/etc/resolv.conf']
    result = LookupModule().run(terms, [])
    assert (result == ['nameserver 6.6.6.6\nnameserver 1.2.3.4\nsearch test.example.com foo.example.com bar.example.com'])
    assert(LookupModule().run(['/nonexistantfile'], []) == [])

# Generated at 2022-06-13 13:33:34.364397
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Unit tests of method run of class LookupModule '''
    import os
    test_terms = ['unittest.txt']
    lu = LookupModule()
    # Test that a file is copied to a temp directory and the file is read
    lu._loader = DictDataLoader({'roles/role1/files/unittest.txt': 'UNITTEST contents of unittest.txt file'})
    results = lu.run(test_terms)
    assert results == ['UNITTEST contents of unittest.txt file']

# Generated at 2022-06-13 13:33:36.100436
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: write test
    pass


# Generated at 2022-06-13 13:33:43.894512
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    # Test for invalid file
    try:
        lookup_plugin.run(["/etc/passwd_invalid"], lookup_plugin, **{})
        assert False
    except AnsibleError:
        assert True
    # Test for valid file
    assert lookup_plugin.run(["/etc/passwd"], lookup_plugin, **{}) == [open("/etc/passwd", "r").read()]

# Generated at 2022-06-13 13:33:50.448046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test simple string return
    test_instance = LookupModule()
    test_instance._loader = DummyClass()
    assert test_instance.run(['sample_file']) == ['sample_file\n']

    # Test simple string as file return
    test_instance = LookupModule()
    test_instance._loader = DummyClass()
    assert test_instance.run(['sample_file']) == ['sample_file\n']

    # Test return with lstrip and rstrip turned on
    test_instance = LookupModule()
    test_instance._loader = DummyClass()
    assert test_instance.run(['sample_file'], lstrip=True) == ['sample_file']
    assert test_instance.run(['sample_file'], rstrip=True) == ['sample_file']

# Generated at 2022-06-13 13:33:55.606609
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create the object
    lookup = LookupModule()
    terms = "/etc/ansible/hosts"
    variables = {}
    result = lookup.run(terms, variables)
    assert result == [u'[local]\nlocalhost\n']

# Generated at 2022-06-13 13:34:45.613767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["/etc/os-release", "/etc/issue", "/etc/os-release", "/etc/passwd"]
    ret = lookup.run(terms)
    print(ret)

# Generated at 2022-06-13 13:34:49.026469
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run('/test_lookup_file') == 'foo'
    assert lookup.run(['/test_lookup_file', '/test_lookup_file']) == ['foo', 'foo']

# Generated at 2022-06-13 13:35:02.563615
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term = "testfile"
    file_contents = "this\nis\na\ntest\nfile\n"
    lookup_module = LookupModule()
    #setup fake files folder
    import os
    import tempfile
    lookup_module._loader.searchpath = []
    # dummy searchpath for testing
    lookup_module._loader.searchpath.append(".")
    lookup_module._loader.searchpath.append("{0}/ansible/playbooks/files".format(os.getcwd()))
    test_path = "{0}/ansible/playbooks/files/{1}".format(os.getcwd(), term)
    with open(test_path, "wb") as test_file:
        test_file.write(file_contents)
    lookup_module.run(terms = [term])


# Generated at 2022-06-13 13:35:10.932537
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import os

    p = os.path.dirname(__file__)
    fixture_path = os.path.join(p, '../fixtures')
    test_file_name = 'test_file.txt'
    test_file_content = 'This is test file content.'

    dl = DataLoader()
    v = VariableManager()
    v.set_vault_password('secret')
    i = InventoryManager(loader=dl, sources=[os.path.join(fixture_path, 'hosts')])


# Generated at 2022-06-13 13:35:16.678966
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""
    lookup = LookupModule()
    lookup.set_options({'lstrip': True, 'rstrip': True, '_ansible_lookup_plugin': 'file'})

    # test with no terms given
    assert lookup.run([]) == []

    # test with a non-exisiting file
    assert lookup.run(["foobar.txt"]) == []

    # test with an existing file
    assert lookup.run(["README.md"]) == ["# Ansible plugins\n"]

    # test with an existing file with spaces in the path
    assert lookup.run(["tests/data/with spaces.txt"]) == ["data\n"]

# Generated at 2022-06-13 13:35:27.394367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import tempfile
    import shutil
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import assertRegexpMatches
    from ansible.plugins.lookup.file import LookupModule

    # initialize
    temp_dir = tempfile.mkdtemp(prefix='ansible-lookup-test')
    temp_file_name = 'file'
    temp_file = os.path.join(temp_dir, temp_file_name)
    temp_file_content = 'test-content'
    terms = os.path.join(temp_file_name)
    temp_content_file = open(temp_file, 'w')

# Generated at 2022-06-13 13:35:39.470672
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar

    # Prepare mocked object
    lm = LookupModule()
    lm.set_loader(AnsibleLoader(None, variables={}))
    lm._loader.set_basedir('/path/to/basedir')
    lm._templar = Templar(variables={})

    # Prepare test data
    terms = [
        "foo.txt",
        "/opt/bar.txt",
        "baz.txt"
    ]

    expected_result = [
        "FileFooContent",
        "FileBarContent",
        "FileBazContent"
    ]

    # Setup mocked functions

# Generated at 2022-06-13 13:35:40.348562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # @ToDo: write some tests
    pass

# Generated at 2022-06-13 13:35:53.098002
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    test_terms = [
        {'_terms': ['does_not_exist'], 'msg': "could not locate file in lookup: does_not_exist", 'return': []},
        {'_terms': ['AnsiballZ_command.py'], 'msg': "File lookup using .*AnsiballZ_command.py as file", 'return': ["#!/usr/bin/python"]}
    ]

    for test in test_terms:
        try:
            result = lookup.run(test['_terms'])
            assert result == test['return']
        except AnsibleError as e:
            if not test['msg']:
                print(test)
                raise
            assert test['msg'] in str(e)


# Generated at 2022-06-13 13:36:00.404047
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    from ansible.utils import py3compat

    from ansible.errors import AnsibleError, AnsibleParserError
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.utils.display import Display

    display = Display()

    lookup_module = LookupModule()

    _temp_dir = tempfile.mkdtemp()
