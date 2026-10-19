

# Generated at 2022-06-13 06:41:49.420216
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    """
    Unit test for method find_vars_files of class DataLoader
    """
    # test with role
    # test with role and non-existing vars directory
    # test with role and vars directory
    # test with role and vars file
    # test with role and vars file with extension
    # test with role and vars file with 'yaml' extension
    # test with role and vars file with 'yml' extension
    # test with role and vars file with 'json' extension
    # test with role and vars files with 'yaml' and 'yml' extensions
    # test with role and vars files with all extensions
    # test with role, vars directory and vars file
    # test with role, vars directory and vars files with all extensions
    # test with non-existing role and non-existing vars

# Generated at 2022-06-13 06:41:55.348192
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    expected = [
        u'/tmp/ansible/foo',
        u'/tmp/ansible/foo',
        u'/tmp/ansible/foo',
        u'/tmp/ansible/foo',
        u'/tmp/ansible/foo',
        u'/tmp/ansible/foo',
    ]
    basedir = u'/tmp/ansible'
    paths = [
        u'foo'
    ]
    for path in paths:
        if DataLoader().path_dwim_relative(basedir, u'tmp', path) != expected[paths.index(path)]:
            raise AssertionError('unexpected result')

# Generated at 2022-06-13 06:42:03.429991
# Unit test for method load_from_file of class DataLoader

# Generated at 2022-06-13 06:42:16.276310
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    loader = DataLoader()
    file_name = './tests/units/utils/loaders/test.yml'
    with open(file_name, 'r') as f:
        file_contents = f.read()

    # Test with valid file name
    test_contents = "".join(loader.load_from_file(file_name))
    assert test_contents == file_contents

    # Test with invalid file name
    invalid_file_name = './tests/units/utils/loaders/test_invalid.yml'
    with pytest.raises(AnsibleFileNotFound):
        loader.load_from_file(invalid_file_name)

    # Test with directory name
    directory_name = './tests/units/utils/loaders/'

# Generated at 2022-06-13 06:42:28.909145
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    yaml_document = """\
---
- hosts: localhost
  gather_facts: no
  connection: local
  tasks:
    - name: get a test fact
      setup:
      register: test_facts
    - debug:
        var: test_facts
"""
    content = textwrap.dedent(yaml_document).strip()

    ansible_play = ansible_playbook_from_content(content, "/tmp/test.yml")

    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.reserved import Reserved
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

# Generated at 2022-06-13 06:42:33.923734
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    loader = DataLoader()
    fd, tmp_path = tempfile.mkstemp()
    os.close(fd)
    assert os.path.exists(tmp_path)
    loader.tempfiles.add(tmp_path)
    loader.cleanup_tmp_file(tmp_path)
    assert not os.path.exists(tmp_path)

# Generated at 2022-06-13 06:42:46.714450
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():

    dl = DataLoader()
    dir_1 = '/tmp/test_path_dwim_relative/dir_1'
    file_1 = os.path.join(dir_1, 'file_1')
    dir_2 = '/tmp/test_path_dwim_relative/dir_2'
    file_2 = os.path.join(dir_2, 'file_2')

    os.makedirs(dir_1)
    with open(file_1, 'w') as f:
        f.write('file_1')

    os.makedirs(dir_2)
    with open(file_2, 'w') as f:
        f.write('file_2')

    # relative path, file in search_path, expect original path

# Generated at 2022-06-13 06:42:54.126026
# Unit test for method path_dwim_relative_stack of class DataLoader
def test_DataLoader_path_dwim_relative_stack():
    # Arrange
    basedir = "/galaxy/project"
    path = "./roles/role1/tasks/main.yml"
    dirname = "files"
    source = "var.yml"
    loader = DataLoader(None, None, None, None, basedir)
    expected = "/galaxy/project/roles/role1/files/var.yml"

    # Act
    actual = loader.path_dwim_relative_stack([path], dirname, source, True)

    # Assert
    assert actual == expected


# Generated at 2022-06-13 06:42:59.639607
# Unit test for method path_dwim_relative_stack of class DataLoader
def test_DataLoader_path_dwim_relative_stack():
    dl = DataLoader()
    tmp = tempfile.mkdtemp()
    tmp_roles_dir = os.path.join(tmp, 'roles')
    role_dir = os.path.join(tmp_roles_dir, 'role')
    os.makedirs(role_dir)
    tasks_dir = os.path.join(role_dir, 'tasks')
    template_dir = os.path.join(role_dir, 'templates')
    files_dir = os.path.join(role_dir, 'files')
    vars_dir = os.path.join(role_dir, 'vars')
    play_dir = os.path.join(tmp, 'play')
    options = {'roles_path': tmp_roles_dir}
    set_options(options)


# Generated at 2022-06-13 06:43:02.670540
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    assert True == True

# Generated at 2022-06-13 06:43:26.350666
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    with patch('os.unlink') as os_unlink, patch('os.path.exists') as os_path_exists:
        os_path_exists.return_value = True
        l = DataLoader()
        l._tempfiles = set(['/tmp/foo', '/tmp/bar'])
        l.cleanup_tmp_file('/tmp/foo')
        l.cleanup_tmp_file('/tmp/baz')
        assert os_unlink.call_count == 1
        assert '/tmp/bar' in l._tempfiles


# Generated at 2022-06-13 06:43:30.805185
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():

    loader = DataLoader()
    p = patch.object(loader, '_read_file')
    m = p.start()
    m.return_value = 'foo: True'
    p.stop()
    assert loader.load_from_file('file') == {'foo': True}

# Generated at 2022-06-13 06:43:38.141958
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    dl = DataLoader()
    dl.set_basedir(os.path.dirname(os.path.dirname(__file__)) + os.path.sep + 'test/sanity')
    test_dir = os.path.dirname(os.path.dirname(__file__)) + os.path.sep + 'test'
    assert dl.find_vars_files(test_dir, 'testvarfile') == [test_dir + os.path.sep + 'testvarfile' + os.path.sep + 'testvarfile']
    assert dl.find_vars_files(test_dir, 'testvarfile2') == [test_dir + os.path.sep + 'testvarfile2']



# Generated at 2022-06-13 06:43:44.861267
# Unit test for method is_file of class DataLoader
def test_DataLoader_is_file():
    f1 = tempfile.mkstemp(dir=C.DEFAULT_LOCAL_TMP)
    f2 = tempfile.mkdtemp(dir=C.DEFAULT_LOCAL_TMP)

    # Test file existence
    loader = DataLoader()
    assert(loader.is_file(f1[1]))
    assert(not loader.is_file(f2))

    # Test directory existence
    assert(not loader.is_file(f2, follow=False))

# Generated at 2022-06-13 06:43:49.089918
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    loader = DataLoader()
    loader.set_vault_secrets([])
    assert loader.get_real_file("/etc/passwd") == "/etc/passwd"



# Generated at 2022-06-13 06:43:54.225352
# Unit test for method is_file of class DataLoader
def test_DataLoader_is_file():
    loader = DataLoader()
    assert loader.is_file("/bin/echo") == True
    assert loader.is_file("/dev/null") == True
    assert loader.is_file("/etc/passwd") == True
    assert loader.is_file("/etc/foo/bar") == False
    assert loader.is_file("doesnotexist") == False


# Generated at 2022-06-13 06:44:08.127000
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    global args
    args = Mock(spec=['connection'])
    args.connection = 'local'
    loader = DataLoader()
    path = 'tests/testdata/var_dir_file.yml'
    path_correct = 'tests/testdata/var_dir_file.yml'
    path_correct2 = 'tests/testdata/var_dir_file'
    path_correct3 = 'tests/testdata/var_dir_file.yaml'
    path_wrong = 'tests/testdata/test_append_to.yml'
    path_wrong2 = 'tests/testdata/test_append_to'
    assert loader.load_from_file(path_correct) == {'test_var': 'var_value_file'}

# Generated at 2022-06-13 06:44:14.079952
# Unit test for method is_file of class DataLoader
def test_DataLoader_is_file():
    '''test is_file'''
    test_loader = DataLoader()
    mock_file = '/some/path/to/random.file'
    # Mock path_exists to return True for any path it is given
    test_loader.path_exists = MagicMock(return_value=True)
    # Mock is_directory to return False for any path it is given
    test_loader.is_directory = MagicMock(return_value=False)
    # Test that is_file returns True for any path
    assert test_loader.is_file(mock_file) == True
    # Change path_exists to return False for any path it is given
    test_loader.path_exists = MagicMock(return_value=False)
    # Test that is_file returns False for any path

# Generated at 2022-06-13 06:44:26.435082
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    def f(path):
        try:
            return set(os.listdir(path))
        except FileNotFoundError:
            return set()

    d = DataLoader()
    assert(len(f(d.get_basedir())) == 0)
    assert(len(d._tempfiles) == 0)

    assert(d.get_real_file('/etc/hosts').endswith('/etc/hosts'))
    assert(d.get_real_file('/etc/passwd').endswith('/etc/passwd'))

    os.environ['ANSIBLE_VAULT_PASSWORD_FILE'] = '/does/not/exist'
    assert(d.get_real_file('/dev/null').endswith('/dev/null'))


# Generated at 2022-06-13 06:44:33.737181
# Unit test for method path_dwim_relative_stack of class DataLoader
def test_DataLoader_path_dwim_relative_stack():
    loader = DataLoader()
    file_name = 'common.yml'
    dirname = 'plugin_vars'
    paths = ['/var/data/ansible/public/plugins/action', '/var/data/ansible/public/plugins/action/common.yml']
    assert loader.path_dwim_relative_stack(paths, dirname, file_name) == '/var/data/ansible/public/plugins/action/plugin_vars/common.yml'



# Generated at 2022-06-13 06:44:52.803716
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import is_encrypted_file

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    ld = DataLoader()
    ld.set_vault_secrets(['$ANSIBLE_VAULT;1.1;AES256;ansible'])

    m_open = MagicMock()
    with patch('ansible.parsing.vault.open', m_open):
        ## if the file is vault encrypted then a temp decrypted file is returned
        # vaulted file
        b_file_path = to_bytes('/tmp/foo.vaulted')

# Generated at 2022-06-13 06:45:04.098241
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    """ Unit test for method path_dwim_relative of class DataLoader """
    loader = DataLoader()
    # Case 1: path = /etc/ansible, dirname = templates, source = test.yml
    # Expect: /etc/ansible/templates/test.yml
    # Result: /etc/ansible/templates/test.yml
    path1 = '/etc/ansible'; dirname1 = 'templates'; source1 = 'test.yml'
    path1_result = loader.path_dwim_relative(path1, dirname1, source1)
    assert path1_result == '/etc/ansible/templates/test.yml'
    # Case 2: path = /etc/ansible, dirname = templates, source = /tmp/test.yml
    # Expect: /tmp/

# Generated at 2022-06-13 06:45:15.019141
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    '''
    Unit test for path_dwim_relative
    '''
    loader = DataLoader()
    search_paths = [
        u'/a/b/c/d/e',
        u'/foo/bar',
        u'/baz/qux',
    ]
    assert loader.path_dwim_relative(search_paths, u'look', u'here') == u'/a/b/c/d/e/look/here'
    assert loader.path_dwim_relative(search_paths, u'look', u'/here/too') == u'/here/too'
    assert loader.path_dwim_relative(search_paths, u'look', u'../there') == u'/a/b/c/d/there'


# Generated at 2022-06-13 06:45:24.049633
# Unit test for method path_dwim_relative_stack of class DataLoader
def test_DataLoader_path_dwim_relative_stack():
    '''
    DataLoader.path_dwim_relative_stack() Test Method
    '''
    from ansible.errors import AnsibleFileNotFound
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    path_missing = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/does_not_exist')
    assert path_missing
    assert os.path.exists(path_missing) == False

    play_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../playbooks/')
    assert play_path
    assert os.path.exists(play_path)

    # test no paths provided

# Generated at 2022-06-13 06:45:35.788739
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    # 
    # test load_from_file without fail_on_missing
    # 
    loader = DataLoader()
    result = loader.load_from_file('./test/fixtures/test_loader_invalid_yaml.yaml')
    assert result == {}
    assert loader._cache == {}

    # 
    # test load_from_file with fail_on_missing
    # 
    loader = DataLoader()
    try:
        loader.load_from_file('./test/fixtures/test_loader_invalid_yaml.yaml', 'test_fail_on_missing')
        assert False, 'AnsibleFileNotFound was not raised'
    except AnsibleFileNotFound:
        assert loader._cache == {}



# Generated at 2022-06-13 06:45:46.262242
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    data_loader = DataLoader()

    # Example call to cleanup_tmp_file with provided parameters
    # Note: only run the tests if the vault password is supplied with the VAULT_PASSWORD env variable
    vault_password = os.getenv("VAULT_PASSWORD")
    if vault_password:
        # This test case uses a sample vault file which should be able to be decrypted using the supplied password
        # If using an alternate vault password, update the vault file to decrypt using that password
        vault_test_file_name = "test-vault.yml"
        vault_decrypted_test_file_name = "test-vault-decrypted.yml"
        temp_file_path = data_loader.get_real_file(vault_test_file_name, decrypt=True)

        # Check that the file was decrypted

# Generated at 2022-06-13 06:45:48.057888
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    x = DataLoader()
    assert hasattr(x, 'cleanup_all_tmp_files')


# Generated at 2022-06-13 06:45:55.849935
# Unit test for method find_vars_files of class DataLoader
def test_DataLoader_find_vars_files():
    cur_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    temp_file = tempfile.mktemp(dir=cur_dir)
    temp_file1 = tempfile.mktemp(dir=cur_dir)
    temp_dir = tempfile.mkdtemp(dir=cur_dir)
    temp_dir1 = tempfile.mkdtemp(dir=cur_dir)
    extensions = ['.yml', '.yaml']
    for ext in extensions:
        for temp_file_path in [temp_file, temp_file1]:
            with open(temp_file, 'w') as temp_file:
                temp_file.write('')

# Generated at 2022-06-13 06:45:58.904858
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    fake_loader = DataLoader()
    assert fake_loader.get_real_file


# Generated at 2022-06-13 06:46:11.005080
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    '''
    Unit test for method cleanup_all_tmp_files of class DataLoader
    '''
    loader = DataLoader()
    loader.set_basedir('/home/ansible/playbook')
    tempfile_path = loader.path_dwim_relative(loader.get_basedir(), 'files', 'test_file')
    with TempfileManager(loader.get_basedir(), loader.get_vault_secrets(), tempfile_path) as tempfiles:
        assert tempfile_path in tempfiles
        loader.cleanup_all_tmp_files()
        assert tempfile_path not in tempfiles

# Generated at 2022-06-13 06:46:52.326612
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.cli import CLI
    from ansible.utils.display import Display
    from ansible.errors import AnsibleFileNotFound, AnsibleParserError
    
    vault_file = os.path.join(os.getcwd(), "vault.txt")
    temp_file = "temp.txt"
    if os.path.exists(temp_file):
        os.remove(temp_file)

    if not os.path.exists(vault_file):
        display = Display()
        cli = CLI(["ansible-vault", "create", vault_file, "--vault-password-file=pass.txt"])
        cli.parse()

# Generated at 2022-06-13 06:46:57.107973
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    loader = DataLoader()
    assert len(loader._tempfiles) == 0
    tmpfile = loader._create_content_tempfile('test data')
    assert len(loader._tempfiles) == 1
    assert tmpfile in loader._tempfiles
    loader.cleanup_tmp_file(tmpfile)
    assert len(loader._tempfiles) == 0
    assert tmpfile not in loader._tempfiles



# Generated at 2022-06-13 06:47:00.171571
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    data_loader = DataLoader()
    temp_file = data_loader._create_content_tempfile('this is a temp file')
    assert os.path.exists(temp_file)
    data_loader.cleanup_tmp_file(temp_file)
    assert temp_file not in data_loader._tempfiles
    assert not os.path.exists(temp_file)


# Generated at 2022-06-13 06:47:10.347457
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():

    def test_cleanup_tmp_file_1(file_path):
        d = DataLoader()
        assert file_path not in d._tempfiles
        d.cleanup_tmp_file(file_path)

    def test_cleanup_tmp_file_2(file_path):
        d = DataLoader()
        d._tempfiles.add(file_path)
        assert file_path in d._tempfiles
        d.cleanup_tmp_file(file_path)
        assert file_path not in d._tempfiles

    def test_cleanup_tmp_file_3(file_path):
        import os
        d = DataLoader()
        fd, content_tempfile = tempfile.mkstemp(dir=C.DEFAULT_LOCAL_TMP)
        assert content_tempfile not in d._tempfiles

# Generated at 2022-06-13 06:47:20.973063
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    from ansible.parsing.vault import VaultLib
    test_loader = DataLoader()
    # test_loader.get_real_file(file_path, decrypt=True)
    # test_loader.get_real_file(file_path, decrypt=False)
    def test_helper(file_path, decrypt=True):
        # create a temp file
        fd, content_tempfile = tempfile.mkstemp(dir=C.DEFAULT_LOCAL_TMP)
        f = os.fdopen(fd, 'w')
        try:
            f.write("Ansible. DataLoader test")
        except Exception as err:
            os.remove(content_tempfile)
            raise Exception(err)
        finally:
            f.close()
        file_path = content_tempfile
        # get

# Generated at 2022-06-13 06:47:29.260343
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    """
    Test cleanup_tmp_file method of class DataLoader
    """
    # Test DataLoader mocked object
    mock_dl = DataLoader()

    # Test files
    file_name = 'test_file'
    file_name_temp = 'temp_file'

    # Test folder
    folder_name = 'Test_DataLoader_cleanup_tmp_file'

    # Test file_path
    file_path = os.path.join(folder_name, file_name)
    file_path_temp = os.path.join(folder_name, file_name_temp)

    # Create test folder
    try:
        os.mkdir(folder_name)
    except OSError:
        print("Creation of test folder %s failed" % folder_name)

# Generated at 2022-06-13 06:47:40.153184
# Unit test for method load_from_file of class DataLoader
def test_DataLoader_load_from_file():
    loader = DataLoader()
    mock_file = Mock(spec=FileFormat)
    mock_file.load_from_file.return_value = {'loaded': 'from_file'}
    loader._get_file_format.return_value = mock_file
    assert loader.load_from_file('/path/to/file') == {u'loaded': u'from_file'}
    mock_file.load_from_file.assert_called_once_with('/path/to/file')
    loader._get_file_format.assert_called_once_with('/path/to/file')


# Generated at 2022-06-13 06:47:47.127712
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    def Test():
        loader = DataLoader(
            config_data=dict(
                vault_password_files=['./test/fixtures/vault/passwordfile.txt'],
                vars_plugins=['./test/fixtures/plugins'],
                group_vars='./test/fixtures/group_vars',
                host_vars='./test/fixtures/host_vars',
                roles_path='./test/fixtures/roles',
                modules_path='./test/fixtures/modules'
            )
        )
        loader.cleanup_all_tmp_files()
    Test()
    


# Generated at 2022-06-13 06:47:49.005075
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    data_loader = DataLoader()
    data_loader.cleanup_all_tmp_files()

# Generated at 2022-06-13 06:47:58.932332
# Unit test for method path_dwim_relative of class DataLoader
def test_DataLoader_path_dwim_relative():
    
    # setUp variables
    source = 'main.yml'
    
    
    # Create the loader, which has access to the files in the tests/ dir
    loader = DataLoader()
    
    # Create a Mock class first, then override relevant attributes
    m = mock.mock_open()
    with mock.patch('builtins.open', m, create=True):
        # Call the test function
        result = loader.path_dwim(source)
    
    # Evaluate results
    assert source == result
    
    return result


# Generated at 2022-06-13 06:49:03.703400
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    temp_file_path = tempfile.mkdtemp()

# Generated at 2022-06-13 06:49:10.112122
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # make sure we handle the case of not giving a file to get_real_file properly
    dl = DataLoader()
    try:
        dl.get_real_file(None)
    except AnsibleParserError:
        pass
    except Exception as e:
        # We should catch AnsibleParserError, instead of Exception
        raise Exception("AnsibleParserError is expected, instead of %s." % str(type(e)))
    else:
        raise Exception("AnsibleParserError is expected.")



# Generated at 2022-06-13 06:49:17.189827
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    # get_real_file: decryption done because no vault password was specified
    # Create a DataLoader object with the minimal parameters
    dl = DataLoader()
    # Create a temporary file containing encrypted data
    test_file_content='$ANSIBLE_VAULT;1.1;AES256\n616361626263313233343536373839316162636465666768696a6b6c6d6e6f70\n7172737475767778797a30313233343536373839316263646566676869\n'
    test_file = tempfile.NamedTemporaryFile()
    test_file.write(test_file_content)
    test_file.flush()
    test_file_path = test_file.name
    real_path = dl.get_real

# Generated at 2022-06-13 06:49:23.045300
# Unit test for method cleanup_all_tmp_files of class DataLoader
def test_DataLoader_cleanup_all_tmp_files():
    # Test using a real DataLoader
    loader = DataLoader()
    ansible_vault_file = u"ansible/test/data/vault/vaulted_file.yml"
    file_path = loader.get_real_file(ansible_vault_file, decrypt=True)
    loader.cleanup_all_tmp_files()
    assert os.path.exists(file_path) == False


# Generated at 2022-06-13 06:49:31.822088
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    from ansible.parsing.dataloader import DataLoader
    from tempfile import mkstemp
    from os import remove
    
    # Create a temp file
    fd, file_name = mkstemp()
    f = os.fdopen(fd, 'w')
    f.write('Test content')
    f.close()
    loader = DataLoader()
    loader.cleanup_tmp_file(file_name)
    assert not os.path.exists(file_name)
    

# Generated at 2022-06-13 06:49:45.401182
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    loader = DataLoader()
    # Testing with file given by get_real_file which creates a temporary
    # file.
    real_file = loader.get_real_file("./tests/resources/varsfiles/files/file_with_vault_password.yml")
    loader.cleanup_tmp_file(real_file)
    # Cleaning a file that hasn't been created by get_real_file must not do
    # anything.
    another_real_file = loader.get_real_file("./tests/resources/varsfiles/files/file_with_vault_password.yml")
    loader.cleanup_tmp_file("./tests/resources/varsfiles/files/file_with_vault_password.yml")
    # Cleaning a file that has been created by get_real_file

# Generated at 2022-06-13 06:49:46.407337
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    assert True

# Generated at 2022-06-13 06:49:56.689757
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    """
    Test if cleanup_tmp_file returns the file path as a string
    """
    test_file_path = '/tmp/test_loader'

    def Mock_open(self, file, mode):
        tmp_file = open(file, mode)
        tmp_file.write('test')
        tmp_file.close()
        return tmp_file

    def Mock_cleanup_tmp_file(self, file_path):
        os.remove(file_path)

    with patch.multiple(DataLoader, open=Mock_open, cleanup_tmp_file=Mock_cleanup_tmp_file) as mocks:
        dl = DataLoader()
        dl.get_real_file(test_file_path, False)
        assert os.path.isfile(test_file_path) is True

# Generated at 2022-06-13 06:50:06.456755
# Unit test for method cleanup_tmp_file of class DataLoader
def test_DataLoader_cleanup_tmp_file():
    import tempfile
    from ansible.compat.tests import unittest

    class TestDataLoader(unittest.TestCase):

        def setUp(self):
            self.data_loader = DataLoader()

        def tearDown(self):
            self.data_loader.cleanup_all_tmp_files()

        def test_cleanup_tmp_file_removes_file(self):
            '''
            Test that cleanup_tmp_file() deletes a file
            '''
            fd, content_tempfile = tempfile.mkstemp(dir=C.DEFAULT_LOCAL_TMP)
            os.close(fd)
            self.data_loader.get_real_file(content_tempfile)
            self.assertTrue(os.path.exists(content_tempfile))
            self.data_

# Generated at 2022-06-13 06:50:16.144091
# Unit test for method get_real_file of class DataLoader
def test_DataLoader_get_real_file():
    loader = DataLoader()
    datadir = "tests/integration/test_utils/playbooks/test_playbook"
    assert loader.get_real_file(loader.path_dwim(os.path.join(datadir, "encrypted_file.yml")), decrypt=True) is not None
    assert loader.get_real_file(loader.path_dwim(os.path.join(datadir, "encrypted_file.yml")), decrypt=False) is None
    assert loader.get_real_file(loader.path_dwim(os.path.join(datadir, "unencrypted_file.yml"))) is not None
    loader.cleanup_all_tmp_files()

