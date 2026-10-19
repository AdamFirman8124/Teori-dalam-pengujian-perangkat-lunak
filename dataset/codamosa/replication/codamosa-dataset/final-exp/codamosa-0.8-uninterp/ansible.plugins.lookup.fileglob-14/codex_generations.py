

# Generated at 2022-06-13 13:42:07.865616
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Fail
    assert lookup.run(["*.md"]) == []

    # Pass
    # Create a directory
    os.system('mkdir -p /tmp/foo/bar')
    # Create a test file
    os.system('touch /tmp/foo/bar/test')
    # Create an empty file
    os.system('touch /tmp/foo/bar/empty')
    # Test file glob
    assert lookup.run(["/tmp/foo/bar/*.md"]) == []
    assert lookup.run(["/tmp/foo/bar/test"]) == ['/tmp/foo/bar/test']
    assert lookup.run(["/*.md"]) == []

    # Cleanup
    os.system('rm -rf /tmp/foo/')

# Generated at 2022-06-13 13:42:16.912639
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    lookup = LookupModule(loader, variable_manager, templar=None)


# Generated at 2022-06-13 13:42:23.392369
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['*.txt'], {}) == []

    test_file=open("test_file1.txt","w")
    test_file1=open("test_file2.txt","w")

    assert LookupModule().run(['*.txt'], {}) == ['test_file1.txt', 'test_file2.txt']

    test_file.close()
    test_file1.close()

# Generated at 2022-06-13 13:42:33.180229
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule = __import__('ansible.plugins.lookup.fileglob').ansible.plugins.lookup.fileglob.LookupModule
    import os
    l = LookupModule()
    test_dir = os.path.dirname(os.path.realpath(__file__))
    result = l.run([os.path.join(test_dir,'test_fileglob.py')],{'ansible_search_path':[os.path.dirname(test_dir)]})
    if not isinstance(result, list):
        raise ValueError
    if os.path.basename(result[0]) != 'test_fileglob.py':
        raise ValueError

# Generated at 2022-06-13 13:42:45.706942
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(terms=['/etc/hosts'], inject={'playbook_dir': '/etc/ansible', 'hostvars': {'host1': {'ansible_search_path': ['~']}}}) == [to_text('/etc/hosts')]
    assert LookupModule().run(terms=['/etc/hosts'], inject={'playbook_dir': '/etc/ansible', 'hostvars': {'host1': {'ansible_search_path': ['~', '/home/me/']}}}) == [to_text('/etc/hosts')]

# Generated at 2022-06-13 13:42:56.315859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests if the function can find files in the search path
    # Args: (self, terms, variables=None, **kwargs)
    # Returns: list of paths

    # Expected results
    expected_results = ['/playbooks/files/fooapp/hosts', '/playbooks/files/fooapp/main.yml']

    # Testing with a list of terms
    # Single file, no directory, hence look in the paths directory, then files directory
    # within the paths directory
    terms = ['/fooapp/main.yml']
    variables = {'ansible_search_path': ['/playbooks']}
    res = LookupModule().run(terms, variables)
    assert res == expected_results, "failed getting a list of files matching a pattern in a search path"

    # Testing with just a file name, hence, iterate

# Generated at 2022-06-13 13:43:08.444799
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock
    from ansible_collections.community.general.tests.unit.compat.mock import patch
    mock_glob = MagicMock(return_value=["/path/to/ansible/tools/docsite/tools/ansible-doc-1.9.4.html"])
    mock_isfile = MagicMock(return_value=True)
    mock_join = MagicMock(return_value="/path/to/ansible/tools/docsite/tools/ansible-doc-1.9.4.html")

# Generated at 2022-06-13 13:43:15.196133
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = '/etc/hosts'
    assert l.run(terms) == ['/etc/hosts']
    assert l.run(['/etc/hosts','/etc/resolv.conf']) == [
        '/etc/hosts','/etc/resolv.conf']
    assert l.run([]) == []
    assert l.run(['/etc/hosts*']) == [
        '/etc/hosts']
    assert l.run(['/etc/hosts*', '/etc/resolv.conf']) == [
        '/etc/hosts','/etc/resolv.conf']

# Generated at 2022-06-13 13:43:25.932533
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test requirement: must be run from the directory ansible/lib/ansible/plugins/lookup/
    import os
    import sys
    import types
    import unittest
    from ansible.errors import AnsibleFileNotFound

    class TestLookupModule(unittest.TestCase):
        def setUp(self):
            self.lookup = LookupModule()
            # Customize ansible.plugins.loader._module_finder to make available
            # ansible.plugins.lookup.fileglob.LookupModule

            import ansible.plugins.loader
            if sys.version_info[0] < 3:
                import imp
                imp.reload(ansible.plugins.loader)
            else:
                # Python 3
                import importlib
                importlib.reload(ansible.plugins.loader)

            import ans

# Generated at 2022-06-13 13:43:38.085911
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:43:42.434687
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['../../test/test_utils.py']
    with open('../../test/test_utils.py', 'r') as file:
        expected = [file.read()]
        actual = lookup_module.run(terms)
    assert actual == expected
    print("Actual Tests Passed")

if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 13:43:53.256881
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_obj = LookupModule()
    terms = [
        '/my/path/*.txt',
        '*.txt',
        '/my/path/*.yml',
        '*.yml'
    ]
    # test for list of files in terms
    result = lookup_module_obj.run(terms)
    assert result == ['/my/path/*.txt', '*.txt', '/my/path/*.yml', '*.yml']
    # test for list of files in terms
    result = lookup_module_obj.run(terms, wantlist=True)
    assert result == ['/my/path/*.txt', '*.txt', '/my/path/*.yml', '*.yml']

# Generated at 2022-06-13 13:44:00.804595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run("*.txt", variables={'ansible_search_path': ['/data/myfiles/files', '/data/myfiles']}) == []

    assert lookup_module.run("*.txt", variables={'ansible_search_path': ['/data/myfiles/files', '/data/myfiles']}) == []
    
    lookup_module = LookupModule()
    assert lookup_module.run("*.txt", variables={'ansible_search_path': ['/data/myfiles/files', '/data/myfiles']}) == []
    assert lookup_module.run("*.txt", variables={'ansible_search_path': ['/data/myfiles/files', '/data/myfiles']}) == []


# Generated at 2022-06-13 13:44:06.706764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run(
        ['/playbooks/files/fooapp/*'],
        {
            "ansible_search_path": [
                "/playbooks"
            ],
            "ansible_basedir": "/tmp",
            "myvar": "foo"
        }
    )
    assert result == ['/playbooks/files/fooapp/test1']

# Generated at 2022-06-13 13:44:17.015282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = [
        'test_file.txt',
        'test_file.ext'
    ]
    variables = {
        'ansible_search_path': [
            '.',
            'test_file.txt'
        ],
        'files': 'test_file.txt'
    }
    expected = [
        'test_file.txt',
    ]
    assert expected == lookup_module.run(terms, variables)

# Generated at 2022-06-13 13:44:18.555441
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    parameters = {'terms': 'something'}

    lookup_obj = LookupModule()

    results = lookup_obj.run(**parameters)

    assert results == []

# Generated at 2022-06-13 13:44:26.649429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.basedir = os.path.join(os.getcwd(), '..', '..')
    assert len(lookup.run(['ansible.cfg'])) == 1
    assert len(lookup.run(['lookup_plugins/fileglob.py'])) == 1
    assert len(lookup.run(['does-not-exist'])) == 0
    assert len(lookup.run(['does-not-exist1', 'does-not-exist2'])) == 0
    assert len(lookup.run(['does-not-exist1', 'ansible.cfg'])) == 1
    assert len(lookup.run(['./does-not-exist'])) == 0
    assert len(lookup.run(['does-not-exist*'])) == 0

# Generated at 2022-06-13 13:44:29.977524
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms_expected = ['/path/to/file']
    variables_expected = {}
    assert lookup_module.run(terms_expected, variables_expected) == []



# Generated at 2022-06-13 13:44:38.738182
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:44:42.430076
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    # check if the result of run method is equal to the expected result
    assert ['/my/path/file1.txt'] == lookup_obj.run(['/my/path/*.txt'], {'role_path': '.'})

# Generated at 2022-06-13 13:44:52.411519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.context import context
    from .test_result import AnsibleResult
    import tempfile
    import os
    import shutil

    md = LookupModule()
    md.basedir = None
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 13:44:59.934710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils.facts import Facts

    lookup = LookupModule()
    lookup.set_options({'args': {}})
    lookup.set_context({'vars': {'ansible_search_path': []}}, {'ansible_facts': Facts({})})  # context and runner

    pytest.raises(AnsibleFileNotFound, 'lookup.run([])')
    pytest.raises(AnsibleFileNotFound, 'lookup.run(["./not-existing"])')
    pytest.raises(AnsibleFileNotFound, 'lookup.run(["./not-existing-too"])')

    import tempfile
    dir_path = tempfile.mkdtemp()

# Generated at 2022-06-13 13:45:14.096214
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    basedir = os.path.dirname(__file__)
    data_dir = os.path.join(basedir, '../../../test/unit/lookup_plugins/data')

    lm = LookupModule()
    lm.set_options({})

    # test that globbing works
    test_terms = ['*']
    test_paths = [data_dir]
    ret = lm.run(test_terms, dict(ansible_search_path=test_paths, _original_file=data_dir))
    assert len(ret) == 2, ret

    # test that globbing works with paths
    test_terms = ['data/*']
    test_paths = [data_dir]

# Generated at 2022-06-13 13:45:17.753309
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = "/etc/*.conf"
    terms = terms.split(',')
    variables = dict(ansible_search_path=['/etc/ansible'])
    str = lookup_module.run(terms, variables)
    assert str != None

# Generated at 2022-06-13 13:45:29.689757
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ast
    class Test_LookupModule(LookupModule):
        def __init__(self, basedir=None, runner=None, **kwargs):
            self.basedir = basedir
        def find_file_in_search_path(self, variables, dirs, path):
            return path
        def get_basedir(self, variables):
            return '/test_basedir'
    test = Test_LookupModule()
    # test glob pattern with single file
    terms = ['/test_basedir/testfile']
    variables = {}
    assert test.run(terms, variables) == ['/test_basedir/testfile']
    # test glob pattern with file and directory
    terms = ['/test_basedir/testfile']

# Generated at 2022-06-13 13:45:36.503147
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    path = os.path.dirname(os.path.realpath(__file__))
    lookup_module = LookupModule()
    lookup_module.get_basedir = lambda x: path

    # Test that the first element of the result matches the expected pattern
    result = lookup_module.run(
        terms=['*'],
        variables={'ansible_search_path': '../lookup_plugins'},
        wantlist=False
    )
    assert 'fileglob.py' in result[0]

# Generated at 2022-06-13 13:45:48.735392
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    sys.modules['__main__'] = sys.modules[__name__]
    from ansible.plugins.lookup import LookupModule

    test_dir = os.path.dirname(__file__)
    test_dir = test_dir if test_dir != '' else '.'

    lookup = LookupModule()
    terms = ['/my/path/*.txt', '*.conf', '/my/path/*.conf']
    _terms = [os.path.join(test_dir, t) for t in terms]
    results = lookup.run(_terms, dict(ansible_search_path=test_dir), wantlist=True, variables=dict(ansible_search_path=test_dir))

    file_name_1 = os.path.join(test_dir, "foo.conf")
    file_name_

# Generated at 2022-06-13 13:45:53.215493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    f = open("/tmp/testfilegloblookup", "w")
    f.write("test")
    f.close()
    lookup_obj = LookupModule()
    test_terms = [ "/tmp/testfilegloblookup" ]
    lookup_obj._basedir = "/tmp"
    lookup_obj.run(test_terms)
    assert lookup_obj.run(test_terms) == [ '/tmp/testfilegloblookup' ]
    os.remove("/tmp/testfilegloblookup")

# Generated at 2022-06-13 13:46:03.001534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test LookupModule object
    test_lookup = LookupModule()

    # Create a valid "terms" list
    test_terms = ['/home/ansible/*.txt']

    # Create a valid "variables" dict
    test_variables = dict()
    test_variables['ansible_search_path'] = ['/home/ansible']

    # Perform the test run
    run_result = test_lookup.run(test_terms, test_variables)

    # Check the result
    assert type(run_result) is list
    assert run_result == ['/home/ansible/foo.txt', '/home/ansible/bar.txt']

# Generated at 2022-06-13 13:46:16.020648
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test method run of class LookupModule"""
    # test LookupModule.run with a simple path
    terms = ['./tests/lookup_plugins/test_fileglob.py']
    files = LookupModule().run(terms)
    assert isinstance(files, list)
    assert len(files) == 1
    assert files[0] == './tests/lookup_plugins/test_fileglob.py'

    # test LookupModule.run with a glob path
    terms = ['./tests/lookup_plugins/test*.py']
    files = LookupModule().run(terms)
    assert isinstance(files, list)
    assert len(files) == 2
    assert files[0] == './tests/lookup_plugins/test_fileglob.py'