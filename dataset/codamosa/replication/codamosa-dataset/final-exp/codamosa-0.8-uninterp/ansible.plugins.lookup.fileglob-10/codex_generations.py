

# Generated at 2022-06-13 13:41:59.069897
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["term1", "term2"]
    variables = {"ansible_search_path": ["/etc/ansible/hosts"]}
    lookup_module = LookupModule()
    actual_results = lookup_module.run(terms, variables)
    assert actual_results == []

# Generated at 2022-06-13 13:42:11.652373
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule({})

    terms = ['.do*']
    globbed = lookup.run(terms)
    print(globbed)
    print(len(globbed))
    print(globbed[0])
    print(lookup.run(terms))
    print(len(lookup.run(terms)))
    print(lookup.run(terms)[0])
    assert len(lookup.run(terms)) == 1
    assert lookup.run(terms)[0] == 'do_stuff.py'

    terms = ['.do*', '*.txt']
    globbed = lookup.run(terms)
    print(globbed)
    print(len(globbed))
    print(globbed[0])
    print(globbed[1])
    print(lookup.run(terms))

# Generated at 2022-06-13 13:42:24.248207
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.loader import lookup_loader
    l = lookup_loader.get('fileglob')

    Usage = l.run((), dict(ansible_search_path=['./files']))
    assert Usage == []

    Usage = l.run(('README.md',), dict(ansible_search_path=['./files']))
    assert Usage == ['./files/README.md']

    Usage = l.run(('*.md',), dict(ansible_search_path=['./files']))
    assert Usage == ['./files/README.md', './files/YAML_STYLE_GUIDE.md']

    Usage = l.run(('*.md',), dict(ansible_search_path=['./files', './files2']))

# Generated at 2022-06-13 13:42:34.875276
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    path = "/foo/bar"
    term = "grep"
    search_path = "ansible_search_path"
    ansible_variable = {"ansible_search_path": "/foo/bar"}

    with patch.object(LookupModule, 'find_file_in_search_path') as mock_find_file_in_search_path:
        with patch.object(LookupModule, 'get_basedir') as mock_get_basedir:
            with patch.object(os.path, 'isdir', return_value=True):
                with patch.object(glob, 'glob', return_value=["/foo/bar/grep"]):
                    with patch.object(os.path, 'isfile', return_value=True):
                        lookup_module = LookupModule()
                        result = lookup_module.run

# Generated at 2022-06-13 13:42:40.046803
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Setup
    ansibleVariable = {'ansible_search_path' : [['/', '/usr']]}
    test = LookupModule()

    # Test
    actual = test.run(['test.txt'], ansibleVariable)

    # Assert
    assert('test.txt' in actual)

# Generated at 2022-06-13 13:42:44.005725
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(["static_lookup_plugin.py"]) == []      # This file should not be found by this method
    assert LookupModule.run(["*.py"]) != [] # Files with extension .py should be found by this method

# Generated at 2022-06-13 13:42:49.626120
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Setup
    lookup = LookupModule()
    lookup.basedir = '/home/fred/town'

    # Assume
    terms = ['gaga.*']

    # Action
    result = lookup.run(terms)

    # Assert
    assert result == [], "Invalid result {}".format(result)

    return



# Generated at 2022-06-13 13:42:58.465617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import tempfile
    from ansible.parsing.vault import VaultLib
    from ansible import context
    from .lookup_plugins.fileglob import LookupModule

    lookup_module = LookupModule()
    # use a sample dir
    basedir_old = context.CLIARGS['basedir']
    context.CLIARGS['basedir'] = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    # create a sample vault password file
    vault_password_file_fd, vault_password_file = tempfile.mkstemp()
    os.write(vault_password_file_fd, b"my secret")
    os.close(vault_password_file_fd)
    context

# Generated at 2022-06-13 13:43:10.473271
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:43:15.375838
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    terms = ["/my/path/*.txt"]
    variables = {"ansible_search_path": ["/plays/", "/playbooks/"]}

    assert module.run(terms, variables) is not None


# Generated at 2022-06-13 13:43:24.533952
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assert lookup.run(['/my/path/*.txt'], variables={}) == []
    assert lookup.run(['/my/path/*.txt'], variables={'files': '/my/path'}) == []

    # return value
    path = '/Users/test/test.txt'
    with open(path, 'w+') as f:
        f.write('test')
    variables = {'files': '/Users/test'}
    assert lookup.run(['*.txt'], variables) == [path]
    os.remove(path)

# Generated at 2022-06-13 13:43:26.304683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    # Test with file that exist
    mod.run(['mox*.py'])
    # Test with file that doesn't exist
    mod.run(['mox.py'])
    # Test with file that doesn't exist
    mod.run(['mox.*.py'])

# Generated at 2022-06-13 13:43:28.097088
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    lookupModule.run(["dir/file*.ext"])
    lookupModule.run(['file*.ext'])

# Generated at 2022-06-13 13:43:39.338923
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import PY3
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import AnsibleMapping

    os = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    if PY3:
        builtins = 'builtins'
    else:
        builtins = '__builtin__'

    # Patch methods which would access actual filesystem.
    # Also captures calls to these methods.
    orig_open = getattr(builtins, 'open')
    orig_glob = glob.glob
    orig_isfile = os.path.isfile


# Generated at 2022-06-13 13:43:43.533030
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup an instance of LookupModule
    lookup_module = LookupModule()

    # Setup parameters to be passed to lookup syntax as a list of strings
    terms = ["/my/path/*.txt"]

    # Run the lookup syntax with defined parameters
    result = lookup_module.run(terms)

    # Verify the results
    assert isinstance(result, list)

# Generated at 2022-06-13 13:43:46.483367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    terms = ['/home/test/*.txt']
    found_paths = ['/home/test/testfile.txt', '/home/test/testfile1.txt']
    assert lu.run(terms) == found_paths

# Generated at 2022-06-13 13:43:55.637101
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("")
    lookupModule = LookupModule()
    print("Test 1: ")
    test1 = ['/Users/eswar/Ansible/ansible-modules-core/lib/ansible/plugins/lookup/fileglob.py']
    print("The output is: ", (lookupModule.run(terms=test1)))

    print("Test 2: ")
    test2 = ['/Users/eswar/Ansible/ansible-modules-core/lib/ansible/plugins/lookup/fileglob.yml']
    print("The output is: ", (lookupModule.run(terms=test2)))

# Generated at 2022-06-13 13:44:06.884246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=W0212
    terms = ["*.txt"]
    variables = {'ansible_search_path': ('/Users/avimelnik/Documents/sandbox/ansible-glob-lookup/'
                                         'tests/unit/data/roles/test_role/files/')}
    lkup_obj = LookupModule()
    lkup_obj.set_loader(None)
    result = lkup_obj.run(terms, variables)  # pylint: disable=W0212
    assert result == ['/Users/avimelnik/Documents/sandbox/ansible-glob-lookup/'
                      'tests/unit/data/roles/test_role/files/test_file.txt']

# Generated at 2022-06-13 13:44:16.482554
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    (is_fail, exception_message, traceback) = LookupModule(None).run_unit_test(dict(
        terms=["/root/**/*.yml", "/etc/ansible/foobar"],
        ansible_search_path = ["/root", "/etc/ansible/roles", "/etc/ansible/playbook"],
    ))

    if is_fail:
        # We need to fail the test
        assert False, exception_message

# Generated at 2022-06-13 13:44:21.705014
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    lookup_plugin.set_options({})
    lookup_plugin.run(['/my/path/*.txt'], variables={})
    lookup_plugin.set_options(wantlist=True)
    lookup_plugin.run(['*.txt'], variables={})

# Generated at 2022-06-13 13:44:26.075167
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=no-member
    assert LookupModule().run(terms=['dummy']) == []

# Generated at 2022-06-13 13:44:36.712494
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_object = LookupModule()
    assert lookup_object.run(['*.txt'], variables={'ansible_search_path': ['/test_path/test_child_path']}) == ['/test_path/test_child_path/test.txt']

    # Invalid file:
    assert not lookup_object.run(['*.txt'], variables={'ansible_search_path': ['/invalid-path']})
    assert not lookup_object.run(['*.txt'], variables={'ansible_search_path': ['/test_path/invalid']})

    assert lookup_object.run(['*.txt'], variables={'ansible_search_path': ['/test_path']}) == [
        '/test_path/test.txt', '/test_path/test_child_path/test.txt']

    #

# Generated at 2022-06-13 13:44:45.085212
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['a.txt']
    return_value = lookup.run(terms)
    assert return_value == []

    lookup2 = LookupModule()
    terms = ['readme.md']
    variables = {'role_path': '/home/vivek/ansible-role-test'}
    return_value = lookup2.run(terms, variables)
    assert return_value == ['/home/vivek/ansible-role-test/files/readme.md']

# Generated at 2022-06-13 13:44:46.664532
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    results = LookupModule().run(terms=['/path/to/files', '*'], variables={})
    assert(len(results) > 0)

# Generated at 2022-06-13 13:44:50.900351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    fpath = "/tmp/test"
    fname = "test"

    with open(fpath + "/" + fname, 'a'):
        os.utime(fpath + "/" + fname, None)

    assert lookup.run(terms=[fname], variables={"ansible_search_path": [fpath]}) == [fpath + "/" + fname]
    os.remove(fpath + "/" + fname)
    os.rmdir(fpath)

# Generated at 2022-06-13 13:44:54.407762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_result = LookupModule.run.__func__(LookupModule(), ['*.txt'], variables={'ansible_search_path': ['.']})
    print(lookup_result)


if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 13:44:59.817432
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # LookupModule.run must take 3 parameters
    l = LookupModule(None)

    terms = ['/home/usr/file1', '/home/usr/file2']

    variables = {'ansible_search_path':['/home/usr/files']}

    res = l.run(terms, variables)
    assert len(res) == 2, "Wrong length returned"

    variables = {'ansible_search_path':['/tmp']}
    res = l.run(terms, variables)
    assert len(res) == 0, "Wrong length returned"
# END OF UNIT TEST

# Generated at 2022-06-13 13:45:14.060416
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:45:14.545392
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:45:22.110121
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    os.environ['ANSIBLE_SEARCH_PATH'] = os.path.dirname(__file__) + '/search_path'
    basedir = lookup.get_basedir({})
    assert lookup.find_file_in_search_path({}, 'files', 'search_path/test_LookupModule_run.txt') == os.path.abspath(basedir + '/search_path/files/search_path/test_LookupModule_run.txt')
    assert lookup.run(["search_path/test_LookupModule_run.txt"], None, wantlist=True) == [os.path.abspath(basedir + '/search_path/files/search_path/test_LookupModule_run.txt')]

# Generated at 2022-06-13 13:45:34.295665
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    # Test for finding single file in the search path
    assert lu.run(['/playbooks/files/fooapp/bar.txt'], variables={'ansible_search_path': ['/playbooks/files', '/']}) == ['/playbooks/files/fooapp/bar.txt']
    # Test for finding multiple file in the search path
    assert lu.run(['/playbooks/files/fooapp/*'], variables={'ansible_search_path': ['/playbooks/files', '/']}) == ['/playbooks/files/fooapp/bar.txt', '/playbooks/files/fooapp/baz.txt']
    # Test for finding multiple file in the search path with file globs

# Generated at 2022-06-13 13:45:41.556700
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    variables = VariableManager()
    # Create inventory and add group 'ungrouped' with host localhost to it
    inventory = InventoryManager(loader=DataLoader(), sources='')
    host = Host(name="localhost")
    group = Group(name="ungrouped")
    group.add_host(host)
    inventory.add_group(group)
    inventory.add_host(host)
    variables.set_inventory(inventory)

    lookup_module = LookupModule()
    lookup_module.set_loader(DataLoader())
    lookup_module.set_inventory

# Generated at 2022-06-13 13:45:46.070858
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/my/path/*.txt']
    variables = ''
    test_lookup = LookupModule()
    ret = test_lookup.run(terms, variables)
    print(ret)

#if __name__ == '__main__':
#    test_LookupModule_run()

# Generated at 2022-06-13 13:46:01.025479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("test_LookupModule_run")
    lookup = LookupModule()
    lookup.get_basedir = lambda: "/base/dir"
    lookup.get_basedir_from_loader = lambda: "/base/dir"
    lookup.get_loader = lambda: "./"
    lookup.find_file_in_search_path = lambda v, d, f: "/base/dir/files"

    os.path.isfile = lambda f: True
    os.path.exists = lambda f: True
    os.path.join = lambda *f: "/base/dir/".join(f)

    assert lookup.run(["*.txt"], variables={}) == ['/base/dir/files/*.txt']

# Generated at 2022-06-13 13:46:11.959052
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockLookupModule(LookupModule):
        def __init__(self, *args, **kwargs):
            self.test_args = args
            self.test_kwargs = kwargs

        def get_basedir(self, var):
            return "/tmp"

        def find_file_in_search_path(self, var, dir_name, path):
            return "/mnt/files/" + path

    m = MockLookupModule()
    expected_arguments = (([u"/playbooks/files/fooapp/*",], {}),)
    m.run(["/playbooks/files/fooapp/*"])
    assert m.test_args == expected_arguments

# Generated at 2022-06-13 13:46:17.781660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO

    temp_file = StringIO()
    try:
        temp_file.write('abc')
        temp_file.write('def')
        temp_file.seek(0,0)

        assert(LookupModule().run([temp_file.name]) == [temp_file.name])
    finally:
        temp_file.close()
        os.remove(temp_file.name)

# Generated at 2022-06-13 13:46:27.774692
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup = LookupModule()

    # Testing with file path as term
    assert test_lookup.run(['/home/user/sub_dir/file1.txt']) == ['/home/user/sub_dir/file1.txt']

    # Testing with * as term
    assert test_lookup.run(['/home/user/sub_dir/*']) == []

    # Testing with ** as term
    assert test_lookup.run(['/home/user/sub_dir/**']) == []

    # Testing with * at the beginning of term
    assert test_lookup.run(['*home/user/sub_dir/file1.txt']) == []

    # Testing with * at the ending of term

# Generated at 2022-06-13 13:46:35.326911
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a mock class object
    class MyClass():

        def __init__(self, filename, *args, **kwargs):
            self.filename = filename
            self.path = os.path.dirname(filename)

        def find_file_in_search_path(self, variables, paths, filename):
            return os.path.join(self.path, filename)


    # Create a mock variable dictionary
    mock_variables = {'ansible_search_path':["/playbooks/files/fooapp/"]}

    lookup_instance = MyClass("/playbooks/files/fooapp/test.yml")

    # Test 'find_file_in_search_path' method

# Generated at 2022-06-13 13:46:48.902503
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    # file in /etc/ansible/roles/foo/files/
    assert l.run(["/etc/ansible/roles/foo/files/file1.txt"], variables={'_terms':["/etc/ansible/roles/foo/files/file1.txt"]}) == ['/etc/ansible/roles/foo/files/file1.txt']
    # file in /etc/ansible/roles/foo/files/bar
    assert l.run(["/etc/ansible/roles/foo/files/bar/file1.txt"], variables={'_terms':["/etc/ansible/roles/foo/files/bar/file1.txt"]}) == ['/etc/ansible/roles/foo/files/bar/file1.txt']
    # file in

# Generated at 2022-06-13 13:46:56.814683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    # when the file exists in a directory
    if test.run(['testfiles/test1.txt'])[0] == 'testfiles/test1.txt':
        print("test1: passed")
    else:
        print("test1: failed")
    #when the file doesn't exists in a directory
    if test.run(['testfiles/test.txt'])[0] == 'testfiles/test.txt':
        print("test2: failed")
    else:
        print("test2: passed")

# Generated at 2022-06-13 13:47:22.772827
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    obj = LookupModule()
    # Testing when file is inside the directory given
    assert obj.run(["./test-data/fileglob_data/test1/*.txt"], variables={}) == [u'./test-data/fileglob_data/test1/file1.txt']

    # Testing when dir is a relative path
    assert obj.run(["./test-data/fileglob_data/test1/file1.txt"], variables={}) == [u'./test-data/fileglob_data/test1/file1.txt']


# Generated at 2022-06-13 13:47:31.431261
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The test is only for the method run of class LookupModule,
    # The rest is the same as what existed before.
    # The test should be updated when the behavior of the class changes.
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    # Get the current directory
    current_directory = os.getcwd()

    # Create a host object
    host = Host(name="dummy")

    # Create a variable manager of the host

# Generated at 2022-06-13 13:47:37.672961
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_test = LookupModule()
    terms = ["/playbooks/files/fooapp/*"]
    variables = {'inventory_dir': "/playbooks/",
                 'playbook_dir': "/playbooks/",
                 }
    LookupModule_test.run(terms, variables)

# Generated at 2022-06-13 13:47:47.384197
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    a = LookupModule()
    assert ['/etc/hosts'] == a.run(["hosts"], variables={})
    assert ["/etc/hosts"] == a.run(["hosts"], variables={})
    assert ["/etc/hosts"] == a.run(["hosts"], variables={})
    assert ["/etc/hosts"] == a.run(["hosts"], variables={})
    assert ["/etc/hosts"] == a.run(["hosts"], variables={})
    assert ["/etc/hostname", "/etc/services", "/etc/shadow", "/etc/passwd"] == a.run(["sh*"], variables={})

# Generated at 2022-06-13 13:47:51.818014
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    
    lookup.variables = {
        'ansible_search_path' : []
    }

    term = [
        '/my/path/*.txt'
    ]
    
    result = lookup.run(term)
    assert result == []

# Generated at 2022-06-13 13:48:00.058370
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case 1: Returns nothing on a path that does not exist
    test_case_1 = {
        'terms': [
            '/doesnotexist/test.yaml'
        ],
        'want': None
    }

    lm = LookupModule()
    result_1 = lm.run(test_case_1['terms'])
    assert result_1 is None

    # Test case 2: Returns nothing on a glob that matches nothing
    test_case_2 = {
        'terms': [
            '/tmp/*.yaml'
        ],
        'want': None
    }

    lm = LookupModule()
    result_2 = lm.run(test_case_2['terms'])
    assert result_2 is None

    # Test case 3: Returns the globbed path that matches something
    test_case

# Generated at 2022-06-13 13:48:12.842689
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import load_extra_vars
    from ansible.module_utils import basic

    # Create instance of class LookupModule
    # with parameters:
    #   name = 'fileglob'
    #   path = 'ansible.plugins.lookup.fileglob'
    #   basedir = '.'
    #   loader = None
    #   templar = None
    #   shared_loader_obj = None
    #   variable_manager = None

    loader=DataLoader()
    variable_manager=VariableManager()

# Generated at 2022-06-13 13:48:21.982293
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    lookup_module = LookupModule()
    # First test of method run
    # This test will run only if the .directory_test file exists in /etc/ansible/
    # The content of .directory_test will be :
    # /home/username/Ansible-tests/directory_test
    #
    # The directory_test directory must contain the following files or the test will fail:
    # - file1_test.txt
    # - file2_test.txt
    # - file3_test.txt
    # - file4_test.txt
    # - directory_test_a
    #
    # Inside the directory directory_test_a there must be the following files or the test will fail:
    # - file1_test_a.txt
   

# Generated at 2022-06-13 13:48:29.053845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = [
        "fooapp/*"
    ]
    variables = {
        "ansible_search_path": [
            "/playbooks"
        ]
    }
    results = lookup_module.run(terms, variables)
    assert results == [
        "/playbooks/files/fooapp/default",
        "/playbooks/files/fooapp/production.ini"
    ], results

# Generated at 2022-06-13 13:48:39.907700
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        "tests.yml",
        "tests/test.yml",
        "tests/tests.yml",
        "tests/some/other/path.yml",
        "tests/*.yml",
        "tests/other/*.yml",
        "tests/*.yaml",
        "tests/other/*.yaml",
        "tests/*.json",
        "tests/other/*.json",
    ]

# Generated at 2022-06-13 13:48:58.603035
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LookupModule().run(['./lookup_plugins/README.md'])
    LookupModule().run(['docs/docsite.yml'])
    LookupModule().run(['./filter_plugins/tests/test_defaultdict.py'])
    LookupModule().run(['./filter_plugins/ansible/plugins/lookup/password.py'])

# Generated at 2022-06-13 13:49:09.381463
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.path import unfrackpath
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    import pytest

    loader = DataLoader()
    variable_manager = VariableManager()
    file_glob_plug = LookupModule()

    # Test with a valid path
    test_path = '/path/to/file'
    terms = [test_path]
    results = file_glob_plug.run(terms, variables=variable_manager)
    assert results == [unfrackpath(test_path)]

    # Test with invalid path. An empty list is expected
    test_path = '/path/to/file/xyz'
    terms = [test_path]
    results = file_glob_plug.run(terms, variables=variable_manager)

# Generated at 2022-06-13 13:49:25.001843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from units.compat import unittest
    from units.compat.mock import patch, Mock
    import os

    class TestLookupModule(unittest.TestCase):
        def setUp(self):
            self.terms = ['a', 'b']
            self.variables = {
                'ansible_search_path': ['/etc', '/playbooks/files', '/playbooks']
            }
            self.mock_results = ['/playbooks/files/a', '/playbooks/files/b']
            self.mock_dwimmed_path = [
                '/playbooks/files', '/playbooks'
            ]

        def test_LookupModule_run(self):
            # mocks
            glob_mock = Mock()

# Generated at 2022-06-13 13:49:31.203505
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['test.txt']
    variables = {'hostvars': {'testhost': {'ansible_search_path': ['../test/', './test/']}}}

    # mock class
    class MockLookupModule(object):
        def find_file_in_search_path(self, variables, dir, file):
            return "../test/"

    result = LookupModule.run(MockLookupModule(), terms, variables)
    assert result[0] == "../test/test.txt"

# Generated at 2022-06-13 13:49:36.162432
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['/home/vagrant/ansible/library/fileglob/this_file_exists.py']
    variables = {
        'ansible_search_path': [
            '/home/vagrant/ansible/library/fileglob'
        ]
    }

    lu = LookupModule()

    assert lu.run(terms, variables) == ['/home/vagrant/ansible/library/fileglob/this_file_exists.py']

# Generated at 2022-06-13 13:49:41.254900
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def run(terms, variables=None, **kwargs):
        lookup = LookupModule()
        return lookup.run(terms, variables, **kwargs)

    basedir = '/home/couchbase/ansible/'
    terms = ['/dev/sda']
    variables = {'ansible_search_path': [basedir]}

    result = run(terms, variables)
    assert result == ['/dev/sda']

    terms = ['/dev/sda', '/dev/sdb']
    variables = {'ansible_search_path': [basedir]}

    result = run(terms, variables)
    assert result == ['/dev/sda', '/dev/sdb']

    terms = ['*.txt']
    variables = {'ansible_search_path': [basedir]}


# Generated at 2022-06-13 13:49:51.148655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_lookup = LookupModule()
    my_lookup.set_options({'_basedir': 'C:\\tmp\\my_ansible\\my_ansible_repo\\roles\\my_role\\'})
    import ansible.utils.vars
    import ansible.parsing.yaml.objects
    import ansible.context
    import ansible.plugins.loader as plugin_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), os.path.join(os.path.pardir, os.path.pardir)))

# Generated at 2022-06-13 13:50:06.761738
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleFileNotFound
    from ansible.module_utils._text import to_bytes, to_text
    import os
    import yaml
    import glob

    # Constructing a mock class instead of using mock_module due to the fact that
    # mock_module does not mock class methods
    class MockLookupModule(LookupModule):
        def get_basedir(self, variables):
            return os.path.join(
                os.path.dirname(__file__),
                'test/unit/lookup_plugins/files')
    mock_module = MockLookupModule()

    # Case 1: Path has directory and a file
    term = os.path.join('test', 'fileglob.py')
    # Since mock class doesn't have self.get_basedir, we need to
    # call

# Generated at 2022-06-13 13:50:19.095260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Only test in Python 2.6+


    # Read values from config file
    from ansible.config import load_config_file
    c = load_config_file('ansible.cfg')

    # Create variables object
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    h = Host('localhost')
    m = VariableManager(loader=None, hostvars=dict())
    m._extra_vars = dict(ansible_config=c)
    m.set_host_variable(h, 'ansible_search_path', 'roles')
    m.set_host_variable(h, 'ansible_connection', 'local')

    # Create lookup object
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 13:50:26.225000
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['/etc/hosts','/tmp/hosts']) == ['/etc/hosts', '/tmp/hosts']
    assert LookupModule().run(['/etc/hosts','/tmp/hosts'],wantlist=True) == ['/etc/hosts', '/tmp/hosts']
    assert LookupModule().run(['/tmp/hosts','/etc/hosts'],wantlist=True) == ['/tmp/hosts']
    assert LookupModule().run(['/tmp/hosts','/etc/hosts']) == ['/tmp/hosts']
    assert LookupModule().run(['*','/tmp/hosts']) == []
    assert LookupModule().run(['*','/tmp/hosts'],wantlist=True) == []