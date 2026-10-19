

# Generated at 2022-06-13 06:41:55.241870
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    loader = DataLoader()
    path = "/home/user/ansible/playbooks"
    dirname = "tasks"
    source = "main.yml"
    is_role = False
    assert loader.path_dwim_relative(path, dirname, source, is_role) == "/home/user/ansible/playbooks/tasks/main.yml"
    dirname = "files"
    assert loader.path_dwim_relative(path, dirname, source, is_role) == "/home/user/ansible/playbooks/files/main.yml"
    dirname = "handlers"
    assert loader.path_dwim_relative(path, dirname, source, is_role) == "/home/user/ansible/playbooks/handlers/main.yml"
    dirname

# Generated at 2022-06-13 06:42:04.605871
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    """Unit test for path_dwim_relative."""
    # path_dwim_relative() should return "do/re/mi.yaml"
    # when dirname is "foobar" and source is "fa/so/la.yaml"
    source = u'fa/so/la.yaml'
    dirname = u'foobar'
    path = u'/my/base/dir/do/re/mi.yaml'
    loader = DataLoader()
    output = loader.path_dwim_relative(path, dirname, source)
    assert output == u'/my/base/dir/do/re/fa/so/la.yaml'
    # path_dwim_relative() should return "/absolute/path"
    # when dirname is "foobar" and source is "/absolute/path"


# Generated at 2022-06-13 06:42:14.638387
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    from ansible.errors import AnsibleFileNotFound
    # Unit test of:
    #     path_dwim_relative
    #     This is an error-throwing wrapper for a class method.
    # Test with and without 'dirname'
    # Test with and without '.yml' filename extension
    for dirname in ['', 'vars']:
        for source in ['a.yml', 'a']:
            # call method
            try:
                ansible.plugins.loader.path_dwim_relative(None, dirname, source)
            except AnsibleFileNotFound:
                # not covered in unit tests
                pass
    return True


# Generated at 2022-06-13 06:42:21.746400
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    assert DataLoader().path_dwim_relative("/home/localadmin/backup/my.yml", "tasks", "my.yml", False) == "/home/localadmin/backup/tasks/my.yml"
    assert DataLoader().path_dwim_relative("/home/localadmin/backup/my.yml", "tasks", "other.yml", False) == "/home/localadmin/backup/tasks/other.yml"
    assert DataLoader().path_dwim_relative("/home/localadmin/backup/my.yml", "meta", "other.yml", False) == "/home/localadmin/backup/meta/other.yml"


# Generated at 2022-06-13 06:42:28.390679
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    # Setup
    result = {}

    # Test
    loader = DataLoader()
    result['before'] = len(loader._tempfiles)
    loader.cleanup_all_tmp_files()
    result['after'] = len(loader._tempfiles)

    # Return results
    return result

# Generated at 2022-06-13 06:42:35.198926
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
  path_dwim_relative_test_cases = [
      ('/var//lib/awx/projects//foo/inventories//bar//test.yml', '/var/lib/awx/projects/foo/inventories/bar/test.yml')
  ]
  for test_case in path_dwim_relative_test_cases:
      # print('testing: {}'.format(test_case))
      assert DataLoader.path_dwim_relative(b'/', b'test', test_case[0]) == test_case[1]


# Generated at 2022-06-13 06:42:46.891015
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    # Create a DataLoader object
    adl = DataLoader()
    # Create a temporary file
    fd, fname = tempfile.mkstemp(dir=C.DEFAULT_LOCAL_TMP)
    os.close(fd)
    # Add the temporary file to the list of temporary files
    adl._tempfiles.add(fname)
    # Delete the temporary file, if created
    if(os.path.isfile(fname)):
        os.remove(fname)
    # Call cleanup_all_tmp_files
    adl.cleanup_all_tmp_files()
    # Check if cleanup_all_tmp_files deleted the temporary file
    assert(not os.path.exists(fname))


# Generated at 2022-06-13 06:42:54.318197
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    dl = DataLoader()
    with open('./test/loader_tests/test_load_from_file.yml') as f:
        read_data = f.read()
    data = AnsibleLoader(read_data).get_single_data()
    loaded_data = dl.load_from_file('./test/loader_tests/test_load_from_file.yml')
    assert loaded_data == data

# Generated at 2022-06-13 06:42:55.209837
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
  DataLoader().find_vars_files()

# Generated at 2022-06-13 06:42:58.485579
# Unit test for method is_file of class DataLoader
def test_DataLoader_is_file():

    # Test with a file path
    from os.path import isfile
    file_path = '/path/to/file'
    result = isfile(file_path)
    assert result == DataLoader.is_file(file_path)

    # Test with a directory path
    dir_path = '/path/to/dir'
    result = False
    assert result == DataLoader.is_file(dir_path)


# Generated at 2022-06-13 06:43:29.922561
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    vcr_kwargs = {}
    if os.environ.get('VCR_RECORD_MODE', 'none') != 'none':
        # VCR can't serialize a lot of the objects passed around, so we have to
        # tell it to let the client socket handle that
        vcr_kwargs['filter_headers'] = ['authorization']

    with vcr.use_cassette('test/fixtures/vcr_cassettes/test_DataLoader_load_from_file.yaml', **vcr_kwargs):

        # create an instance of the Ansible parser
        yaml_file = load_fixture_file('yaml_loader_data/ansible_hosts.yaml')
        parser = AnsibleParser(yaml_file)
        parser.parse()

        # create an instance of DataLoader
       

# Generated at 2022-06-13 06:43:34.399818
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    # init class
    DataLoader_instance = DataLoader()
    # call the method load_from_file
    assert DataLoader_instance.load_from_file(file_name='None', cache=True, unsafe_proxy=False, show_content=False, collection_list=None) is None

# Generated at 2022-06-13 06:43:35.610691
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    assert False, "Not implemented"


# Generated at 2022-06-13 06:43:36.153380
# Unit test for method path_dwim_relative_stack of class DataLoader
def test_DataLoader_path_dwim_relative_stack():
    pass

# Generated at 2022-06-13 06:43:42.053549
# Unit test for method is_file of class DataLoader
def test_DataLoader_is_file():
    # Create a test fixture
    loader_obj = DataLoader()

    # Test a case of when file exists in path.
    path = '/home/user/file'
    os.path.exists = MagicMock(return_value=True)
    os.path.isfile = MagicMock(return_value=True)
    result = loader_obj.is_file(path)
    assert result == True

    # Test a case of when file doesn't exists in path.
    path = '/home/user/file'
    os.path.exists = MagicMock(return_value=False)
    os.path.isfile = MagicMock(return_value=False)
    result = loader_obj.is_file(path)
    assert result == False



# Generated at 2022-06-13 06:43:44.650897
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    test_loader = DataLoader()
    self.assertTrue(test_loader.find_vars_files('./', 'FILE_NAME'))


# Generated at 2022-06-13 06:43:51.958894
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    # Test DataLoader.find_vars_files
    # Test with invalid args
    try:
        DataLoader().find_vars_files(None, 'test')
    except AnsibleParserError as e:
        if 'Invalid root path' not in str(e):
            raise AssertionError("Expected AnsibleParserError, but found: %s" % repr(e))
    else:
        raise AssertionError("Expected AnsibleParserError")



# Generated at 2022-06-13 06:44:05.761178
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    '''
    Test cleanup_tmp_file method of DataLoader.
    '''
    dl = DataLoader()
    # Check if all the local variables are defined in DataLoader class
    assert all(hasattr(dl, attr) for attr in ['_tempfiles'])

    # Test case 1: 
    # Test if get_real_file method throws exception when filename is None
    try:
        with pytest.raises(AnsibleParserError) as e:
            dl.get_real_file(None)
    except Exception as err:
        assert str(err) == "invalid literal for int() with base 10: 'None'"

    # Test case 2: 
    # Test if get_real_file method throws exception when filename is empty string

# Generated at 2022-06-13 06:44:15.255170
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    config_manager = ConfigManager()
    loader = DataLoader()
    # find_vars_files(self, path, name, extensions=None, allow_dir=True)
    name = "meta"
    exten = [''] + C.YAML_FILENAME_EXTENSIONS
    path = config_manager.get_config_basedir() + "/" + name
    # check if the directory exists

# Generated at 2022-06-13 06:44:22.273984
# Unit test for method is_file of class DataLoader
def test_DataLoader_is_file():
  data = 'a: 1'
  loader = DataLoader()
  with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write(data)
    temp_file.close()

  result = loader.is_file(temp_file.name)
  assert result, 'Test for method DataLoader.is_file() failed!'
  os.remove(temp_file.name)

# Generated at 2022-06-13 06:44:39.408030
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    from ansible.compat import StringIO
    fixture = StringIO('yaml')
    display = Display()
    ansible = Ansible(None, None, allow_filesystem_imports=False, display=display)
    dl = DataLoader(fixture, '/tmp/root', None, None, None, lookups=ansible.lookup_loader)
    dl.cleanup_all_tmp_files()

# Generated at 2022-06-13 06:44:49.745626
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    dl = DataLoader()
    # two files in repo
    real_path = dl.get_real_file('playbooks/playbook.yml')
    assert real_path == 'playbooks/playbook.yml', "path should be equal to 'playbooks/playbook.yml', but is {}".format(real_path)

    # one file in repo, one included
    real_path = dl.get_real_file('playbooks/include/tasks.yml')
    assert real_path == 'playbooks/include/tasks.yml', "path should be equal to 'playbooks/include/tasks.yml', but is {}".format(real_path)

    # one file in repo, one included, one in vault

# Generated at 2022-06-13 06:45:00.600684
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    display.display(display.DisplayMessage('<test_DataLoader_get_real_file()>'))

    # Test Data
    filename = u'ansible/test/units/module_utils/test_module_utils_basic.py'
    file_path = os.path.join('ansible', 'test', 'units', 'module_utils', 'test_module_utils_basic.py')
    file_path_with_basedir = os.path.join(u'~', file_path)

    # Test get_real_file
    dl = DataLoader()
    rf = dl.get_real_file(file_path)
    assert os.path.exists(file_path)
    assert os.path.exists(rf) and filename == os.path.basename(rf)

# Generated at 2022-06-13 06:45:11.822650
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # Create an instance of class DataLoader
    ans = DataLoader()

    # Create a temporary file containing a vault encrypted file
    temp_fd, temp_path = tempfile.mkstemp()
    f = os.fdopen(temp_fd, 'wb')
    f.write(b_VAULT_ENCRYPTED)
    f.close()

    # Check decryption of vault file
    vault_file = ans.get_real_file(temp_path, decrypt=True)
    f = open(vault_file)
    acquired = f.read()
    f.close()
    assert acquired == b_VAULT_CONTENT, 'Decryption of vault file failed'

    # Check without decryption of vault file
    vault_file = ans.get_real_file(temp_path, decrypt=False)

# Generated at 2022-06-13 06:45:15.981178
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():

    t1 = to_bytes("tempfile1.txt")
    t2 = to_bytes("tempfile2.txt")
    t3 = to_bytes("tempfile3.txt")

    # add a bunch of files to the tempfiles set
    cur_dl = DataLoader()
    cur_dl._tempfiles = {t1, t2, t3}

    # verify all files were loaded correctly
    assert cur_dl._tempfiles == {t1, t2, t3}

    # create a bunch of files to clean up
    with open(t1, "w") as temp1:
        temp1.write("test1")

    with open(t2, "w") as temp2:
        temp2.write("test2")


# Generated at 2022-06-13 06:45:20.444716
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    l = AnsibleLoader()
    l.set_basedir(u"/root/ansible/lib/ansible/plugins/lookup")
    path = "/root/ansible/lib/ansible/plugins/lookup/file.py"
    result = l.load_from_file(path)
    assert result==None

# Generated at 2022-06-13 06:45:27.139131
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    from ansible.parsing.vault import VaultLib

    def os_path_join(dir, filename):
        return str(dir) + os.sep + str(filename)

    def check_file_path(file_path, file_obj):
        assert(isinstance(file_path, binary_type))
        file_path = to_text(file_path, errors='surrogate_or_strict')
        assert(os.path.exists(file_path))
        assert(os.path.isfile(file_path))
        with open(file_path, 'rb') as f:
            assert(f.read() == file_obj.read())


# Generated at 2022-06-13 06:45:38.774755
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():

    class MockVaultSecretParser(object):
        class Secret(object):
            pass

        def __init__(self):
            self.secrets = [self.Secret(), self.Secret()]

        def get_secrets(self, vault_id):
            return self.secrets

    class MockVaultMgr(object):
        def __init__(self):
            self.secrets = [self.Secret(), self.Secret()]

        class Secret(object):
            pass

        def get_secret(self, vault_id):
            return self.secrets

        def decrypt(self, val, filename, vault_password=None):
            return val

    class MockVaultFile(object):
        def __init__(self, name, block=False):
            self.name = name
            self.block = block


# Generated at 2022-06-13 06:45:48.387592
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.path import unfrackpath

    # Test valid case
    dataLoader = DataLoader()
    vault_password_file = os.path.join(os.path.dirname(__file__), 'vault_password_file')
    vault_succinct_password_file = os.path.join(os.path.dirname(__file__), 'vault_succinct_password_file')
    vault_secret = 'VaultPassword'
    vault_id = 'vault_id'
    vault_alias = 'vault_alias'

    real_path = dataLoader.get_real_file(vault_password_file)

# Generated at 2022-06-13 06:45:56.091030
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    from ansible.errors import AnsibleError
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play_context import PlayContext
    import unittest

    # A reference implementation of the method to test
    class RefDataLoader(DataLoader):
        def find_vars_files(self, path, name, extensions=None, allow_dir=True):
            return super(RefDataLoader, self).find_vars_files(path, name, extensions, allow_dir)

    # Test data

# Generated at 2022-06-13 06:46:32.850353
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    if not os.path.exists(os.path.join(DATA_DIR, 'examples')):
        os.makedirs(os.path.join(DATA_DIR, 'examples'))
    with open(os.path.join(DATA_DIR, 'examples', 'foo.yml'), 'w') as f:
        f.write('foo_var: "foo"')
    loader = DataLoader()
    assert loader.load_from_file(os.path.join(DATA_DIR, 'examples', 'foo.yml')) == {'foo_var': 'foo'}


# Generated at 2022-06-13 06:46:34.433670
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    loader = DataLoader()
    loader.cleanup_all_tmp_files()

# Generated at 2022-06-13 06:46:41.843361
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # Get the class
    DataLoader_class = module_loader.load_module('AnsibleLoader').DataLoader

    # Get an instance of DataLoader
    args = {}
    inst = DataLoader_class(**args)

    # Initialize method with valid arguments
    # Unicode type
    file_path = u'/opt/ansible/test/file.txt'
    decrypt = True
    try:
        # Call the method
        real_path = inst.get_real_file(file_path, decrypt)
    except Exception as e:
        inst.cleanup_all_tmp_files()
        raise Exception(e)
    else:
        inst.cleanup_all_tmp_files()

    print("Successfully executed method get_real_file of class DataLoader")
    return real_path



# Generated at 2022-06-13 06:46:53.253386
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    loader = DataLoader()
    files = [
        tempfile.NamedTemporaryFile(dir=C.DEFAULT_LOCAL_TMP).name,
        tempfile.NamedTemporaryFile(dir=C.DEFAULT_LOCAL_TMP).name,
        tempfile.NamedTemporaryFile(dir=C.DEFAULT_LOCAL_TMP).name,
    ]
    loader._tempfiles = set(files)

    loader.cleanup_all_tmp_files()
    assert len(os.listdir(C.DEFAULT_LOCAL_TMP)) == 0
    assert len(loader._tempfiles) == 0

# Generated at 2022-06-13 06:47:01.046368
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import is_encrypted_file
    import tempfile
    import os
    # Set up test environment
    my_loader = DataLoader()
    my_loader._vault = VaultLib()

# Generated at 2022-06-13 06:47:11.736572
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    import tempfile
    from ansible.parsing.vault import VaultLib

    def get_reader():
        vault_pass = [VaultLib.gen_password()]
        vault_id = ['test']
        return VaultLib(vault_pass), vault_id

    tmpfd1, temppath1 = tempfile.mkstemp()
    os.close(tmpfd1)

    tmpfd2, temppath2 = tempfile.mkstemp()
    os.close(tmpfd2)

    tmpfd3, temppath3 = tempfile.mkstemp()
    os.close(tmpfd3)

    reader, vault_id = get_reader()
    encrypted_data = reader.encrypt(b"foo")


# Generated at 2022-06-13 06:47:20.430958
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    dl = DataLoader()
    assert dl._tempfiles == set()
    tf1 = dl._create_content_tempfile('one')
    assert tf1 in dl._tempfiles
    assert os.path.exists(tf1)
    tf2 = dl._create_content_tempfile('two')
    assert tf2 in dl._tempfiles
    assert os.path.exists(tf2)
    dl.cleanup_all_tmp_files()
    assert dl._tempfiles == set()
    assert not os.path.exists(tf1)
    assert not os.path.exists(tf2)


# Generated at 2022-06-13 06:47:28.710987
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    # Set up mock of AnsibleVault and load
    mock_vault = mock.Mock()
    mock_vault.get_decrypted_text.return_value = 'test_content'
    mock_vault.secrets = [('test_secret', 'test_pass')]
    # Set up mock of TaskExecutor and load
    mock_task = mock.Mock()
    mock_task.get_original_vars.return_value = {'test_var': 'test_val'}
    # Initialize DataLoader object and load
    dl = DataLoader(vault_secrets=mock_vault.secrets)
    test_loader = dl.load_from_file(mock_task, 'test_file')
    # Assert
    assert test_loader == 'test_content'

#

# Generated at 2022-06-13 06:47:42.777677
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    args = {}
    vars = {'ansible_connection': 'local'}
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='setup', args=args), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    ), variable_manager=VariableManager(), loader=DictDataLoader())
    tqm = None

# Generated at 2022-06-13 06:47:49.188192
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    from ansible.parsing.vault import VaultLib
    import tempfile
    # create a vault secret for testing
    vault_password = '111111'
    vault = VaultLib([(vault_password,)])
    test_content = b'$ANSIBLE_VAULT;1.1;AES256'
    content = to_bytes(test_content + vault.encrypt(b'test_content'))
    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    tmpfile.write(content)
    tmpfile.close()
    loader = DataLoader()
    # check if this file is created
    assert os.path.exists(tmpfile.name)
    # check if the decrypted file is created
    assert os.path.exists(loader.get_real_file(tmpfile.name))


# Generated at 2022-06-13 06:48:51.458523
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    # Test setup
    ##########################################################################
    # Mock Variables
    ##########################################################################
    self = {}
    self['_basedir'] = u'/home/ansible/playbook/'
    self['_dflt_basedir'] = u'/home/ansible/playbook/'
    self['_vault_secrets'] = {}

    # Data
    ##########################################################################
    file_name = u'group_vars/all/var'
    variable_manager = {}

    ##########################################################################
    # Expected Results
    ##########################################################################
    path = self['_basedir'] + file_name
    rtn = {u'var1': u'var1', u'var2': u'var2'}
    rtn_t = {}

    # Unit test
    #################################################################

# Generated at 2022-06-13 06:49:00.166629
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # Constructor
    # Return a DataLoader object for the given play context
    #
    # Given:
    #   * A PlayContext object
    #   * A string representing the path to the file
    #   * A string representing the name of the file
    #
    # When:
    #   * A DataLoader object is constructed
    #
    # Then:
    #   * Return a DataLoader object
    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.remote_addr = '127.0.0.1'
    play_context.remote_user = 'root'
    play_context.port = '22'
    play_context.password = None
    play_context.private_key_file = None
    play_context.become = 'yes'
    play_context

# Generated at 2022-06-13 06:49:03.231343
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # test with encrypted file
    # test with plain file
    # test with unexisting file
    pass

# Generated at 2022-06-13 06:49:08.158769
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # create a temp file that will be deleted on exit
    test_filename = tempfile.mkstemp(text=True)[1]
    with open(test_filename, "w") as f:
        f.write("Hello World")
    assert DataLoader().get_real_file(test_filename) == test_filename



# Generated at 2022-06-13 06:49:09.637581
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    fakeLoader = DataLoader()
    assertDataLoader_get_real_file(fakeLoader)


# Generated at 2022-06-13 06:49:15.080616
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    loader = DataLoader()

    # test that load_from_file can handle streams
    # but the editorx plugin needs to copy the contents to a file first, so this test is not really useful
    stream_path = u'/tmp/junk.yaml'
    data = b'''{}'''
    stream = io.StringIO(to_text(data, errors='surrogate_or_strict'))
    with open(to_bytes(stream_path, errors='surrogate_or_strict'), 'wb') as f:
        f.write(data)
    stream_result = loader.load_from_file(stream_path)
    assert stream_result == {}

    # test that load_from_file can handle files
    file_path = u'/tmp/junk2.yaml'

# Generated at 2022-06-13 06:49:20.732945
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    # Prepare for testing
    path = '/path/to/files'
    name = 'foo'
    extensions = []
    allow_dir = True
    # Run method
    DataLoader.find_vars_files(path, name, extensions, allow_dir)
    # No assertation for now, because it's a private method

# --- end of DataLoader --- #



# Generated at 2022-06-13 06:49:24.361034
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # test_file=None

    dl = DataLoader()
    file_path = None
    decrypt = True
    test_file = dl.get_real_file(file_path, decrypt)
    assert isinstance(test_file, six.text_type)
    assert test_file == u''


# Generated at 2022-06-13 06:49:31.068461
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    data_loader = DataLoader()
    b_tmp_file = data_loader._create_content_tempfile(b'content')

    assert b_tmp_file
    assert os.path.exists(b_tmp_file)

    data_loader.cleanup_all_tmp_files()

    assert not os.path.exists(b_tmp_file)


# Generated at 2022-06-13 06:49:42.566223
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    f1 = tempfile.NamedTemporaryFile(delete=False)
    f2 = tempfile.NamedTemporaryFile(delete=False)
    f3 = tempfile.NamedTemporaryFile(delete=False)
    dl = DataLoader()
    dl._tempfiles = set()
    dl._tempfiles.add(f1.name)
    dl._tempfiles.add(f2.name)
    dl._tempfiles.add(f3.name)
    dl.cleanup_tmp_file("%s" % f2.name)
    assert set(dl._tempfiles) == set([f1.name, f3.name])