

# Generated at 2022-06-13 06:41:58.453260
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    sample_file_system = {'test_vars_dir': {'a.yml': '', 'a.yaml': '', 'b': '', 'c.yaml': '',
                                            'd': '', 'e.yaml': '', 'f': '', 'g.yml': ''},
                          'test_vars_dir2': {'a.yml': '', 'g.yaml': '', 'b': '', 'c.yml': '',
                                             'd': '', 'e.yaml': '', 'f': '', 'g.yml': ''}}

    test_path = 'test_vars_dir'
    name = 'a'
    extensions = C.YAML_FILENAME_EXTENSIONS
    allow_dir = True
    test_DataLoader

# Generated at 2022-06-13 06:42:08.969893
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    loader = DataLoader()
    file_path = loader.path_dwim('playbook.yaml')
    loader.get_real_file(file_path)

    if len(loader._tempfiles) == 0:
        raise AssertionError('tmpfile is not created')
    # call the cleanup_tmp_file() method
    loader.cleanup_tmp_file(file_path)
    tmp_len = len(loader._tempfiles)
    if tmp_len != 0:
        raise AssertionError('tmpfile is not deleted')

#---------------------------------------------------------------------------------------------------

# Generated at 2022-06-13 06:42:17.950996
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    # Set up test objects
    basedir = "/path/to/basedir"
    host_basedir = "/path/to/host/basedir"
    cur_basedir = "/path/to/cur/basedir"
    path = "/path/to/tasks"
    source = "test.yml"
    dirname = "role_dir/dirname"
    eval_data = {'dir': host_basedir, 'basedir': basedir, 'role_path': path, 'role_dirname': dirname, 'source': source}

    # Create test object
    loader = DataLoader()
    loader.set_basedir(basedir)

    # test path_dwim_relative
    real_path = loader.path_dwim_relative(path, dirname, source)

# Generated at 2022-06-13 06:42:24.763354
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    data_loader = DataLoader()

    base_path = u'/tmp/test-test-test'
    source = u'file.xyz'
    dirname = u'dir-test-test'

    # Tests with file in the same dir
    path = base_path
    assert data_loader.path_dwim_relative(path, dirname, source) == os.path.join(base_path, source)
    path = os.path.join(base_path, u'tasks')
    assert data_loader.path_dwim_relative(path, dirname, source) == os.path.join(base_path, source)

    # Tests with file in the same dir with dirname
    path = base_path

# Generated at 2022-06-13 06:42:35.525500
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    from ansible.vars import VaultLib
    from ansible.utils import create_bytes_buffer

    test_loader = DataLoader()
    vault_pass = VaultLib()._get_file_vault_secret()
    with tempfile.NamedTemporaryFile(prefix='ansible-vault-', dir=C.DEFAULT_LOCAL_TMP, delete=False) as tmp:
        password_bytes = create_bytes_buffer(vault_pass)

# Generated at 2022-06-13 06:42:45.677749
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    (failure_count, tests_run) = doctest.testmod(
        DataLoader,                                             # the module to test
        optionflags=doctest.NORMALIZE_WHITESPACE | doctest.REPORT_NDIFF | doctest.ELLIPSIS,
        raise_on_error=True,
        verbose=False                                           # set to True to see verbose report
    )
    if failure_count != 0:
        raise Exception("Unit test failure of AnsibleDocModule: %s out of %s passed" %(tests_run - failure_count, tests_run))


# Generated at 2022-06-13 06:42:53.639589
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    import os
    import shutil

    def do_assert(file_pattern, expected):
        actual = loader.find_vars_files(tmpdir, 'foo', extensions=file_pattern)
        assert sort_list(actual) == sort_list(expected)

    tmpdir = os.path.realpath(tempfile.mkdtemp(dir=__file__))

# Generated at 2022-06-13 06:42:59.032273
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    content = 'hello world!'
    tf = tempfile.mktemp()
    with open(tf, 'wb') as f:
        f.write(to_bytes(content))

    loader = DataLoader()
    # check that tempfile is not in list of tempfiles
    assert tf not in loader._tempfiles
    # get real file which should add the tempfile to the list of tempfiles
    real_path = loader.get_real_file(tf, decrypt=False)
    assert real_path in loader._tempfiles
    # check that cleanup temp file removes the temp file from the list of tempfile
    loader.cleanup_tmp_file(real_path)
    assert real_path not in loader._tempfiles
    # cleanup the created tempfile
    os.remove(tf)

# Generated at 2022-06-13 06:43:00.277319
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    dl = DataLoader()
    assert [] == dl.find_vars_files('', '')



# Generated at 2022-06-13 06:43:10.702277
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    # test valid extensions
    extensions = ['.yaml', '.yml', '.json', '.txt']
    # init dataloader
    dl = DataLoader()
    # tmp directory
    tmpdir = tempfile.mkdtemp()
    # tmp file path
    tmp_file = os.path.join(tmpdir, 'test_file')
    # tmp directory path
    tmp_dir = os.path.join(tmpdir, 'test_dir')
    # test file that should be found
    test_file = os.path.join(tmp_dir, 'test_file.yaml')
    # dir to test
    test_dir = os.path.join(tmp_dir, 'test_dir')


# Generated at 2022-06-13 06:44:07.374143
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleParserError
    import os
    import shutil

    # Arg spec CmdlineOptions.parse
    args = []
    args.append('-c')
    args.append('local')
    args.append('test.yml')

    test_dir = 'test/unit/parsing/dataloader'
    test_data_dir = os.path.join(test_dir, 'data')
    test_data_file = os.path.join(test_data_dir, 'test.yml')

    test_data_content = '''
    defaults:
      test_var: 'test_value'
    '''

    b_test_data_content = to_bytes(test_data_content)

   

# Generated at 2022-06-13 06:44:19.266780
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    loader = DataLoader()
    loader._tempfiles = set()
    assert loader.cleanup_all_tmp_files() is None
    loader.cleanup_all_tmp_files()
    loader._tempfiles.add(u'/Users/shivam/.ansible/tmp/ansible-tmp-1498501762.67-211847556051490/aggr_name')
    loader.cleanup_all_tmp_files()
    loader._tempfiles.add(u'/Users/shivam/Hempy/ansible-vish/ansible-tmp-1498501762.67-211847556051490/aggr_name')
    loader._tempfiles.add(u'/Users/shivam/H/ansible-tmp-1498501762.67-211847556051490/aggr_name')
   

# Generated at 2022-06-13 06:44:21.350489
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    dl = DataLoader()
    dl.cleanup_all_tmp_files()

# Generated at 2022-06-13 06:44:26.836801
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():

    # 1. Setup
    dl = DataLoader()
    dl._tempfiles = set(["/tmp/1.txt", "/tmp/2.txt", "/tmp/3.txt", "/tmp/4.txt"])

    # 2. Exercise
    dl.cleanup_all_tmp_files()

    # 3. Verify
    assert dl._tempfiles == set()

# Generated at 2022-06-13 06:44:36.071402
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    loader = DataLoader()
    # Check calling method on instance that is not used.
    assert not loader._tempfiles
    # Check calling method on instance that has tempfiles.
    loader._tempfiles.add("foo")
    assert "foo" in loader._tempfiles
    loader.cleanup_all_tmp_files()
    assert not loader._tempfiles
    # Check calling method on instance that has tempfiles but can't be removed.
    loader._tempfiles.add("foo")
    assert "foo" in loader._tempfiles
    loader.cleanup_tmp_file = lambda x: None
    loader.cleanup_all_tmp_files()
    assert not loader._tempfiles

# Generated at 2022-06-13 06:44:47.243914
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():

    class TestArgs:
        def __init__(self):
            self.config_data = {}
            self.verbosity = 0

    class TestDisplay:
        def __init__(self):
            self.verbosity = 0
            self.warning = display.warning

    global CO_LOAD_FROM_FILE

    test_args = TestArgs()
    display = TestDisplay()

    co_loader = DataLoader()
    co_loader.set_vault_password(None)

    # Default values of args
    args = {
        'path': None,
        'filename': '',
        'convert_data': True,
        'allow_duplicates': False,
        'content': None,
        'cache': True,
    }

    # Prepare args for test

# Generated at 2022-06-13 06:44:53.628859
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    loader = DataLoader()

    h_file = loader.get_real_file('../fixtures/ansible.cfg')
    assert os.path.exists(h_file)

    loader.cleanup_tmp_file(h_file)
    assert h_file not in loader._tempfiles

    # Test cleanup all temp files
    h_file = loader.get_real_file('../fixtures/ansible.cfg')
    loader.cleanup_all_tmp_files()
    assert h_file not in loader._tempfiles

    # Test invalid file cleanup
    loader.cleanup_tmp_file('invalid.file')



# Generated at 2022-06-13 06:44:59.061350
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    '''test_DataLoader_cleanup_all_tmp_files'''
    obj = DataLoader()
    obj.cleanup_all_tmp_files()

    obj = DataLoader(path_lookup={'*': {'module_utils': 'a.b.c'}})
    obj.cleanup_all_tmp_files()



# Generated at 2022-06-13 06:45:02.210291
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    # create an instance of class
    data_loader = DataLoader()
    # call the method of the class
    data_loader.cleanup_tmp_file()


# Generated at 2022-06-13 06:45:13.455550
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    loader = DataLoader()
    module_path = os.path.join(os.path.dirname(__file__), u'data')
    vfiles = loader.find_vars_files(module_path, u'array', extensions=[u'yaml'])
    assert vfiles == [
        to_text(os.path.join(module_path, u'array.yaml')),
        to_text(os.path.join(module_path, u'array', u'basic.yaml')),
    ]
    vfiles = loader.find_vars_files(module_path, u'hash', extensions=[u'yaml'])

# Generated at 2022-06-13 06:46:39.519782
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    temp_dir = tempfile.mkdtemp()
    dir_path = os.path.join(temp_dir, 'dir')
    os.mkdir(dir_path)
    files = [os.path.join(temp_dir, 'file%d' % i) for i in range(3)]
    for f in files:
        open(f, 'a').close()
    loader = DataLoader()
    loader.set_basedir(temp_dir)
    files_to_test = ['file1', 'file2', 'file3', 'dir/file2', 'dir/file1', 'dir/file3']
    for f in files_to_test:
        real_path = loader.get_real_file(f)
        assert os.path.exists(real_path)
    loader.cleanup_all_tmp

# Generated at 2022-06-13 06:46:53.986206
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    from ansible.utils.encrypt import VaultLib
    from ansible.parsing import vault
    from unittest import TestCase
    from tempfile import mkstemp
    from os import fdopen, unlink

    class TestDataLoader(DataLoader):
        def __init__(self):
            pass

        @staticmethod
        def is_file(path):
            o_path = unfrackpath(path)
            return os.path.isfile(o_path)

    class DataLoaderTests(TestCase):
        def setUp(self):
            self.TEST_FILE_CONTENTS = u"this is a test"
            self.TEST_DATA_LOADER = TestDataLoader()
            fd, self.TEST_FILE_PATH = mkstemp()
            f = fdopen(fd, "wb")

# Generated at 2022-06-13 06:46:55.856806
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    dloader = DataLoader()
    file_path = '/tmp/'
    dloader.cleanup_tmp_file(file_path)


# Generated at 2022-06-13 06:46:58.578184
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():

    d = DataLoader()

    # Test for TypeError
    with pytest.raises(TypeError):
        d.cleanup_all_tmp_files(None)

    assert d.cleanup_all_tmp_files() is None

# Generated at 2022-06-13 06:47:04.639448
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    from unit.test_DataLoader import TestDataLoader
    from ansible.parsing.dataloader import DataLoader

    load = DataLoader()

# Generated at 2022-06-13 06:47:09.860609
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    tmp = tempfile.mkdtemp()
    dl = DataLoader()
    try:
        to_clean = dl._create_content_tempfile(b'some text')
        dl._tempfiles.add(to_clean)
        assert os.path.exists(to_clean)
        dl.cleanup_tmp_file(to_clean)
        assert os.path.exists(to_clean) == False
    finally:
        shutil.rmtree(tmp)


# Generated at 2022-06-13 06:47:20.421764
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # Initialize class
    data_loader = DataLoader()
    vault_secrets = {}
    # data_loader._vault = vault(vault_secrets)

    # Get data from files
    file_path = os.path.join(os.path.dirname(__file__), '../../../templates/somefile.j2')
    file_path = os.path.abspath(file_path)
    # print(file_path)
    with open(file_path, 'w') as f:
        f.write('sample data')
    file_path = to_text(file_path)
    # print(file_path)
    # file_path = '~/DummyDir/dummy.txt'
    result = data_loader.get_real_file(file_path, decrypt=False)


# Generated at 2022-06-13 06:47:26.523107
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    loader = DataLoader()
    paths_ = [
        '/Users/jfernan/Documents/ansible_dev/ansible/test/units/module_utils/data/testpath/referenced.yml']
    results = []
    for path_ in paths_:
        results.append(loader.get_real_file(path_))
    return results


if __name__ == '__main__':
    test_res = test_DataLoader_get_real_file()
    print(test_res)

# Generated at 2022-06-13 06:47:34.867815
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    loader = DataLoader()
    mock_file_path = '/tmp/123'
    loader._tempfiles.add(mock_file_path)
    assert mock_file_path in loader._tempfiles
    with patch('os.unlink') as mock_unlink:
        loader.cleanup_tmp_file(mock_file_path)
    assert os.unlink.called
    assert mock_file_path not in loader._tempfiles


# Generated at 2022-06-13 06:47:47.062114
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    from ansible.parsing.vault import VaultLib
    from six import StringIO

    class FakeVault(object):
        secrets = set()

        def decrypt(self, data, filename=None):
            return data
    vault_secrets = [u'decrypt_test']
    myvault = FakeVault()
    myvault.secrets = set(vault_secrets)
    tempfilemodule = TempfileModule()
    tempfilemodule._vault = myvault
    tempfilemodule.set_basedir('/my/basedir')
    mypath = '/my/basedir/foo/bar'
    myvault_path = '/my/basedir/foo/bar_vault'
    myvault_file = StringIO()

# Generated at 2022-06-13 06:48:31.210142
# Unit test for method get_real_file of class DataLoader

# Generated at 2022-06-13 06:48:42.008551
# Unit test for method path_dwim_relative_stack of class DataLoader
def test_DataLoader_path_dwim_relative_stack():
    loader = DataLoader()
    paths = [
        '.',
        '/root/playbooks',
        '/root/playbooks/roles/role/tasks'
    ]
    dirname = 'templates'
    source = 'test.yml'
    is_role = False
    assert loader.path_dwim_relative_stack(paths, dirname, source, is_role) == '/root/playbooks/templates/test.yml'
    source = '../vars/test.yml'
    assert loader.path_dwim_relative_stack(paths, dirname, source, is_role) == '/root/playbooks/vars/test.yml'

# Generated at 2022-06-13 06:48:54.039123
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():

    class TestAnsibleModule(object):
        def __init__(self):
            self.params = dict()
            self.params['_ansible_verbosity'] = 0
            self._ansible_verbosity = 0
            self._task = None
            self._play_context = None
            self._loader = None
            self._templar = None

    class TestAnsiblePlayContext(object):
        def __init__(self):
            self.module_vars = dict()
            self.extra_vars = dict()

    class TestModule(object):
        def __init__(self):
            self._ansible_module = TestAnsibleModule()
            self._play_context = TestAnsiblePlayContext()
            self.ansible_module = self._ansible_module
            self.play_context = self

# Generated at 2022-06-13 06:49:02.115175
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
  from ansible.parsing.vault import VaultLib
  from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
  d = DataLoader()
  v = VaultLib(passwords={})
  d._vault = v
  assert isinstance(d.load_from_file(None), AnsibleMapping)
  assert isinstance(d.load_from_file(b''), AnsibleMapping)
  assert isinstance(d.load_from_file(''), AnsibleMapping)
  assert isinstance(d.load_from_file([]), AnsibleSequence)
  assert isinstance(d.load_from_file(b'---\n- test1\n- test2'), AnsibleSequence)

# Generated at 2022-06-13 06:49:04.574125
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    from ansible.test.test_data_loader import test_DataLoader_cleanup_all_tmp_files
    test_DataLoader_cleanup_all_tmp_files()

# Generated at 2022-06-13 06:49:10.678875
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    myDataLoader = DataLoader()
    FAILED_TESTS = 0
    #FAILED_TESTS += test_DataLoader_cleanup_tmp_file_00()
    if FAILED_TESTS:
        print(ugettext("%d tests failed. Please fix and try again.") % (FAILED_TESTS))
        sys.exit(1)
    else:
        print(ugettext("All tests passed successfully!"))


# Generated at 2022-06-13 06:49:22.516603
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    from units.compat import mock

    ldr = DataLoader()
    ldr.path_exists = mock.Mock(side_effect=[True, False])
    ldr.is_directory = mock.Mock(side_effect=[False])
    ldr.list_directory = mock.Mock(side_effect=[['c.yml']])
    ldr.is_file = mock.Mock(side_effect=[True])

    path = "../data/plugins/vars"
    name = "vars_files"
    extensions = C.YAML_FILENAME_EXTENSIONS

    assert ldr.find_vars_files(path, name, extensions) == [os.path.join(path, name)+'.yml']



# Generated at 2022-06-13 06:49:35.384748
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    filename = 'test_valid_file.yml'
    b_filename = 'test_valid_file.yml'
    filepath = 'tests/test_valid_file.yml'
    b_filepath = 'tests/test_valid_file.yml'
    with open(filepath, 'w') as f:
        f.write('password: test')
    assert os.path.exists(filepath)

    dl = DataLoader()
    # case 1: test file is accessible and exist
    # dl.get_real_file(filename)
    assert dl.get_real_file(filepath) == filepath

    # case 2: test file is accessible and exist
    # dl.get_real_file(b_filename)
    assert dl.get_real_file(b_filepath)

# Generated at 2022-06-13 06:49:43.127489
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    '''
    Unit tests for the function and return values of DataLoader.cleanup_tmp_file

    :return: None
    '''
    obj = DataLoader()
    file_path = '/home/user/example.txt'
    try:
        obj.cleanup_tmp_file(file_path)
        raise AssertionError("Expected Exception not raised")
    except AnsibleFileNotFound:
        pass
    except Exception as e:
        raise e



# Generated at 2022-06-13 06:49:46.031112
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
   loader = DataLoader()
   tmpcontent='Hello World'
   file_path = loader._create_content_tempfile(tmpcontent)
   assert loader.cleanup_tmp_file(file_path) == None
   assert os.path.isfile(file_path) == False



# Generated at 2022-06-13 06:50:48.275940
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    import yaml
    test_file = u'/tmp/ansible_DataLoader_load_from_file.yml'
    with open(test_file, 'w') as f:
        yaml_data = {'foo': 'bar'}
        yaml.dump(yaml_data, f)

    try:
        dl = DataLoader()
        data = dl.load_from_file(test_file)

        assert data == yaml_data

    finally:
        os.unlink(test_file)



# Generated at 2022-06-13 06:50:55.628621
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    loader = None
    try:
        with tempfile.NamedTemporaryFile() as f:
            test_file = f.name
            loader = DataLoader()
            loader.path_exists = lambda x: True
            loader.is_file = lambda x: True
            loader.get_real_file(test_file)
            assert test_file in loader._tempfiles
            assert os.path.exists(test_file)
            loader.cleanup_tmp_file(test_file)
            assert test_file not in loader._tempfiles
            assert not os.path.exists(test_file)
    finally:
        if loader:
            loader.cleanup_all_tmp_files()



# Generated at 2022-06-13 06:50:57.233898
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    """
    Test DataLoader class get_real_file method
    """
    pass


# Generated at 2022-06-13 06:51:06.194916
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    # Test with a non existent file path
    dl = DataLoader()
    with pytest.raises(AnsibleFileNotFound):
        dl.load_from_file("/non/existent/path")

    # Test with a directory path
    dl = DataLoader()
    with pytest.raises(AnsibleParserError):
        dl.load_from_file("/")

    # Test with a valid file path
    dl = DataLoader()
    test_file = tempfile.mkstemp()
    try:
        os.write(test_file[0], b"text")
        parsed_data = dl.load_from_file(test_file[1])
        assert parsed_data == "text"
    finally:
        os.close(test_file[0])

# Generated at 2022-06-13 06:51:17.656237
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    # Configure the arguments that would normally be provided by the ansible command line
    args = Namespace()
    args.module_path = None
    args.roles_path = None
    args.vault_password_files = []
    args.vault_ids = ''
    args.ask_vault_pass = False

    # Initialize the vault secret cache
    vault_secrets = VaultSecretCache()
    vault_secrets.update(args=args)

    # Create a DataLoader object
    loader = DataLoader()

    # Specify an example file to load
    b_file_name = b'/etc/ansible/facts.d/factfile'

    # Call the method under test

# Generated at 2022-06-13 06:51:24.345272
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    test_load_from_file = """
    - hosts: localhost
      tasks:
        - name: test
          debug: var=item
      with_fileglob:
      - "{{ playbook_dir }}/test_data_loader.yml"
    """
    # Load a file that matches the glob
    test_load_from_file_1 = """
    - hosts: localhost
      tasks:
        - name: test
          debug: var=item
      with_fileglob:
      - "{{ playbook_dir }}/test_data_loader_1.yml"
    """
    # Load a file that doesn't match the glob

# Generated at 2022-06-13 06:51:30.433575
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    dl = DataLoader()
    t1 = dl._create_content_tempfile("data")
    # calling twice with the same path is a noop and should not raise an exception
    dl.cleanup_tmp_file(t1)
    dl.cleanup_tmp_file(t1)
