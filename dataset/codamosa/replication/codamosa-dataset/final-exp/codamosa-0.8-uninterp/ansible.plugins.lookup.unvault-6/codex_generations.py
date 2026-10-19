

# Generated at 2022-06-13 14:34:35.095054
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ip = LookupModule()

    # test with invalid file path
    try:
        ip.run(terms='/tmp/sample.yml', variables=None)
        assert False, 'Failed as invalid file path is provided'
    except Exception as e:
        assert 'Unable to find file matching' in str(e)

    # test with valid file path
    with open('/tmp/sample.yml', 'w') as f:
        f.write('Sample content')

    ret = ip.run(terms='/tmp/sample.yml', variables=None)
    assert ret == [u'Sample content']

    # test with invalid lookup dir

# Generated at 2022-06-13 14:34:43.985838
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._loader = None
    lookup_module._templar = None
    lookup_module.run(["test.txt"])
    lookup_module.run(["test.txt", "test2.txt"])
    lookup_module.run(["test.txt", "test2.txt", "test3.txt"])
    lookup_module.run(["test.yaml"])
    lookup_module.run(["test.yaml", "test2.yaml"])
    lookup_module.run(["test.yaml", "test2.yaml", "test3.yaml"])

# Generated at 2022-06-13 14:34:55.880581
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an instance of the LookupModule class
    lm = LookupModule()

    # Create a dictionary of the 'run' method's arguments
    run_kwargs = dict(
      terms=['unvault_test_file.yml'],
      variables={},
      **dict(
        loader=dict(
          get_real_file=dict(
            return_value='/etc/ansible/test/unvault_test_file.yml'
          )
        ),
        find_file_in_search_path=dict(
          return_value=dict(
            path='/etc/ansible/test/unvault_test_file.yml',
            realpath='/etc/ansible/test/unvault_test_file.yml'
          )
        )
      )
    )



# Generated at 2022-06-13 14:35:06.027567
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from collections import namedtuple

    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, wrap_var

    # Mock LookupBase
    class MockLookupBase(LookupBase):
        class MockVars(object):
            pass

        def __init__(self):
            self.name = 'mock_lookup_base'
            self.parent = None
            self.playbook_dir = None
            self.loader = None
            self.basedir = None
            self.curr_file = None
            self.templar = Templar(loader=self.loader, variables={})
            self.vars = self.MockVars()

        def get_basedir(self, task_vars):
            return self.basedir


# Generated at 2022-06-13 14:35:17.431573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # expected data
    expected_config_1 = b"""{"key1": "value1"}"""
    expected_config_2 = b"""{"key2": "value2"}"""

    # create test_file with expected_config_1
    test_file = './tests/test_data/test_vault.yml'
    with open(test_file, 'w') as test_file_handle:
        test_file_handle.write(expected_config_1)

    # create test_file with expected_config_1
    test_file_2 = './tests/test_data/test_vault_2.yml'
    with open(test_file_2, 'w') as test_file_handle:
        test_file_handle.write(expected_config_2)

    unvault_lookup = Lookup

# Generated at 2022-06-13 14:35:26.749269
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    lookup_plugin_class = LookupModule

    my_vars = {'ansible_basedir': os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))}
    my_terms = ["lookup_fixtures.yml"]
    my_kwargs = {'wantlist': False}

    foo_obj = lookup_plugin_class()
    assert foo_obj.run(my_terms, my_vars, **my_kwargs) == [u"# Test fixture for Ansible vault\n#\nfoo: bar"]

# Generated at 2022-06-13 14:35:30.447604
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['lookups/unvault/lookup_file.txt']
    expected = ['lookups/unvault/lookup_file.txt contents']
    result = module.run(terms)

    assert(result == expected)

# Generated at 2022-06-13 14:35:35.524407
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # return value of the method run of class LookupModule
    test_result = ["line1\n", "line2\n"]

    # initialization of the class under test
    l = LookupModule()
    test = l.run(["testfile"], variables = {})
    assert test == test_result

# Generated at 2022-06-13 14:35:36.315973
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:35:47.319821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    from ansible.plugins.loader import lookup_loader
    from ansible.utils.display import Display
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    
    import os
    
    # For purpose of test, we copy a sample file into test directory.
    # But, it is not possible to write a vault file here, since the test will fail
    # with "!vault |$ANSIBLE_VAULT;1.1;AES256 ..."
    # This is because lookup_loader.add_directory() is not executed because the plugin
    # is not in lookup_plugins/ directory.

# Generated at 2022-06-13 14:36:02.203034
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import Sequence

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import copy

    assert isinstance(AnsibleLoader(None).construct_mapping(None, None), Mapping)
    assert isinstance(AnsibleLoader(None).construct_sequence(None, None), Sequence)

    # create an encrypted string with ansible-vault
    clear_text = "some text"
    vault_password = "abc123"

# Generated at 2022-06-13 14:36:04.662346
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_options(direct={'_terms': {'type': 'list', 'elements': 'string', 'required': True}})
    assert lookup.run(['/etc/foo.txt']) == ['bar']

# Generated at 2022-06-13 14:36:14.790426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # test get_real_file successfully return result
    import ansible.utils.path
    from ansible.module_utils._text import to_bytes
    from ansible.vars.hostvars import HostVars

    old_method_name = ansible.utils.path.get_real_file
    ansible.utils.path.get_real_file = lambda x: '/test/testfile'
    test_content = 'test_content'
    with open('/test/testfile', 'wb') as f:
        f.write(to_bytes(test_content))
    test_host_name = 'testhost'
    hostvars = HostVars(variables=dict(), vault_password='vaultpassword')
    hostvars.add_host(test_host_name)



# Generated at 2022-06-13 14:36:24.952289
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Populate data_loader, inventory and variable_manager
    data_loader = DataLoader()
    inventory = InventoryManager(loader=data_loader, sources=['localhost'])
    variable_manager = VariableManager(loader=data_loader, inventory=inventory)

    lookup_plugin = LookupModule()

    test_file_path = '/tmp/test_file_123456'
    test_file_content = 'Something secret\n'
    test_file_unvaulted_content = '$ANSIBLE_VAULT;1.1;AES256;my_local_host_name\n' + test_file_content + '\n'

# Generated at 2022-06-13 14:36:30.614208
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: ansible-test data-driven instead of mock
    uv = LookupModule()
    r = uv.run(['/etc/foo.txt'])
    assert r == [b'text\n']
    r = uv.run(['/etc/foo.txt', '/etc/bar.txt'])
    assert r == [b'text\n', b'bar\n']

# Generated at 2022-06-13 14:36:40.441768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    assert lu.run(terms=[u'test/unvault.yml'], variables={}) == [
        '---\n',
        '- hosts: localhost\n',
        '  tasks:\n',
        '    - debug: msg="the value of foo.txt is {{lookup(\'unvault\', \'/etc/foo.txt\')|to_string }}"\n',
        '    #- debug: msg="the value of foo.txt is {{lookup(\'unvault\', \'/etc/foo.txt\')|to_string }}"\n']

# Generated at 2022-06-13 14:36:40.929984
# Unit test for method run of class LookupModule
def test_LookupModule_run():


    assert True

# Generated at 2022-06-13 14:36:51.055837
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import tempfile
    from ansible.module_utils._text import to_bytes
    fd, path = tempfile.mkstemp(text=True) # make temp file with ansible-vault encrypted content
    with open(fd, 'wb') as f:
        f.write(b'{"username": "user", "password": "pwd"}')

    lookup = LookupModule()
    res = lookup.run([to_bytes(path)], None)
    assert len(res) != 0
    assert json.loads(res[0]) == json.loads('{"username": "user", "password": "pwd"}')

# Generated at 2022-06-13 14:37:03.438546
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    #import shutil
    #from unittest import mock
    #from ansible.module_utils.common.text.converters import to_bytes

    # Create a fake Ansible context to exercise the lookup class.
    fake_loader = FakeAnsibleFileLoader()
    fake_loader.set_basedir('/playbook/path')
    fake_var = {}
    fake_var['ansible_playbook_basedir'] = '/playbook/path'

    my_vars = {
        'ansible_playbook_basedir': '/playbook/path',
        'myfile': '/my/file',
        'myfile2': '/my/file2',
    }

    # Test standard use case
    lookup_plugin = LookupModule()
    lookup_plugin.set_loader(fake_loader)


# Generated at 2022-06-13 14:37:09.780432
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    results_list = LookupModule().run(["/etc/ansible/hosts"], [], ansible_vars=dict())
    assert isinstance(results_list, list)
    assert len(results_list) == 1
    assert results_list[0].startswith(u"\n# Ansible managed\n[local]")
    assert results_list[0].endswith(u"localhost\n")
    with pytest.raises(AnsibleParserError):
        results_list = LookupModule().run(["/etc/foobar"], [], ansible_vars=dict())

# Generated at 2022-06-13 14:37:21.306527
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:37:22.077033
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:37:23.423876
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert 'Hello World' in lookup.run(['./tests/resources/ansible_unvault.yml'], [])

# Generated at 2022-06-13 14:37:32.528055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    assert lookup_obj.run(["/tmp/unvault_test.yml"]) == ["--- a: b\n"]

# Generated at 2022-06-13 14:37:35.248569
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    lookup = LookupModule()
    assert lookup.run(terms=['test_lookup_file.txt']) == ['test_lookup_file\n']

# Generated at 2022-06-13 14:37:40.638559
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import Mapping

    loader_mock = Mock(basic.AnsibleModule)
    lookup_plugin = LookupModule(loader=loader_mock)

    # Case 1. Test without arguments
    with pytest.raises(AnsibleParserError):
        lookup_plugin.run()

    # Case 2. Test with empty terms
    with pytest.raises(AnsibleParserError):
        lookup_plugin.run(terms=[])

    # Case 3. Test with empty terms
    with pytest.raises(AnsibleParserError):
        lookup_plugin.run(terms=[""])

    # Case 4. Test with valid terms

# Generated at 2022-06-13 14:37:45.817242
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.path import unfrackpath
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import lookup_loader

    # Setup fixture
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    vault_lookup = lookup_loader.get('vault')
    unvault_lookup = lookup_loader.get('unvault')

    # Setup test data
    one_vaulted_file = 'unvault_one_vaulted_file.yml'
   

# Generated at 2022-06-13 14:37:46.641453
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:37:56.921057
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    path = '/usr/local/foo'
    term = '/usr/local/foo'
    contents = 'This is foo and doo'

    import os
    import shutil
    import tempfile
    import filecmp
    import base64
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.crypto.basic import encrypt_bytes
    from ansible.module_utils.crypto.basic import decrypt_bytes
    import ansible.module_utils.six as six

    class mock_module_utils_crypto_basic:

        @staticmethod
        def encrypt_bytes(key, iv, plaintext):
            if six.PY3:
                plaintext = plaintext.decode('utf-8')
            return base64.b64encode(plaintext)

       

# Generated at 2022-06-13 14:38:02.786210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    unvault_file = open('test_vault.txt', 'wb')
    unvault_file.write('test vault data')
    unvault_file.close()
    res = lm.run(terms=['test_vault.txt'])
    if 'test vault data' in res:
        assert True
    else:
        assert False

# Generated at 2022-06-13 14:38:13.985185
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    ansible_vars = {}
    terms = ["/etc/ansible/hosts"]
    results = lookup_module.run(terms, ansible_vars)
    assert results
    assert len(results) == 1
    assert results[0]

# Generated at 2022-06-13 14:38:19.972153
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import tempfile

    # Create temporary content file
    (fd, tmp_file) = tempfile.mkstemp()
    os.write(fd, b'foobar')
    os.close(fd)

    # Create temporary copy of LookupBase to avoid side effects
    old_LookupBase = LookupBase
    class DummyLookupBase(LookupBase):
        def __init__(self, variables=None, loader=None):
            pass
        def find_file_in_search_path(self, variables, path, filename):
            return None
        def set_options(self, var_options=None, direct=None):
            pass
    LookupBase = DummyLookupBase

    # Create temporary copy of loader
    old_Loader = LookupBase._loader

# Generated at 2022-06-13 14:38:20.656713
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['foo.txt']) == [b'ansible']

# Generated at 2022-06-13 14:38:32.106735
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    data = []

    def dummy_find_file_in_search_path(path, check_vault_encrypted, term):  # pylint: disable=unused-argument
        return "/foo/bar/" + term
    class DummyLoader:
        @staticmethod
        def get_real_file(file, decrypt=True):  # pylint: disable=unused-argument
            return file
    class DummyDisplay:
        @staticmethod
        def debug(tmp):  # pylint: disable=unused-argument
            data.append(tmp)
        @staticmethod
        def vvvv(tmp):  # pylint: disable=unused-argument
            data.append(tmp)

# Generated at 2022-06-13 14:38:40.262050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    import mock
    import StringIO
    lookup = LookupModule()
    mock_loader = mock.MagicMock()
    mock_loader.find_file_in_search_path = mock.MagicMock(return_value="/tmp/foo")
    mock_loader.get_real_file = mock.MagicMock(return_value="/tmp/foo")
    lookup._loader = mock_loader
    lookup._set_options = mock.MagicMock()
    with mock.patch('ansible.plugins.lookup.unvault.open', mock.mock_open(read_data='bar'), create=True):
        assert lookup.run(terms=["foo"]) == ["bar"]

# Generated at 2022-06-13 14:38:46.486793
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = dict(terms=["/etc/foo.txt"])

    # TODO: Need to mock FileLoader and find_file_in_search_path
    # so this test can be run without files on disk
    # and without relying on environment variables

    # lm = LookupModule()
    # result = lm.run([], [], **args)

    # assert result == []



# Generated at 2022-06-13 14:38:56.017439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def find_file_in_search_path(variables, file_type, file_name):
        return "test"

    variables = {}
    lookup = LookupModule()
    lookup._loader = MockLoader({'files':{'test':"test", "test_unvault": "test_unvault"}})
    lookup.find_file_in_search_path = find_file_in_search_path


    with pytest.raises(AnsibleParserError):
        lookup.run(terms=["invalid_file"], variables=variables, **{'skip_encoding': True})

    assert lookup.run(terms=["test"], variables=variables, **{'skip_encoding': True}) == ["test"]



# Generated at 2022-06-13 14:39:01.332467
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule class
    unvault_lookup = LookupModule()

    # Create a terms list where terms[0] is a vaulted file
    terms = []
    terms.append("$ANSIBLE_CONFIG")

    # Expect the content of terms[0] file to be returned
    assert unvault_lookup.run(terms) == ["[defaults]\nhost_key_checking = False\n"]

# Generated at 2022-06-13 14:39:02.022053
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:39:02.738134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:39:29.171801
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import json
    import sys
    import shutil
    import tempfile
    import pytest

    # Define a temporary folder to hold the test fixtures
    temp_root = tempfile.mkdtemp()

    # Create a temporary vault encrypted file
    temp_dir = os.path.join(temp_root, 'roles', 'test')
    os.makedirs(temp_dir)
    temp_vault_file = os.path.join(temp_dir, 'vars', 'main.yml')

    # Write the contents to the file, encrypt it and delete the original
    with open(temp_vault_file, 'w') as f:
        f.write("""---""")

# Generated at 2022-06-13 14:39:40.094725
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_expected = ["test-contents-1", "test-contents-2"]
    terms = ["test-vaulted-file-1", "test-vaulted-file-2"]
    test_obj = LookupModule()
    test_obj.set_options(direct={})
    test_obj._loader = MockLoader()
    test_obj._loader.vault_secrets = {}
    test_obj._loader.mocked_file_dictionary = {}
    # First test without vaulted file
    test_obj._loader.mocked_file_dictionary["files"] = [None] * len(terms)
    assert test_obj.run(terms) == []
    # Second test with vaulted files
    test_obj._loader.mocked_file_dictionary["files"] = terms
    assert test_obj.run

# Generated at 2022-06-13 14:39:41.258009
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  lookup_module = LookupModule()
  # TODO: Test with term that exists + term that doesnt exist

# Generated at 2022-06-13 14:39:47.325727
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class FakeLoader:
        class FakeFileLoader:
            def get_real_file(self, lookupfile, decrypt=True):
                return lookupfile
        def __init__(self):
            self.file_loader = self.FakeFileLoader()

    lm = LookupModule()
    lm.set_loader(FakeLoader())

    terms = ['/some/file.txt']

    with open('/some/file.txt', 'w') as f:
        f.write('This is a test')

    assert lm.run(terms) == ['This is a test']

# Generated at 2022-06-13 14:39:57.385696
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_loader({'get_real_file': lambda x: 'tests/test_lookup_plugins/lookup_fixtures/lookup_unvault/' + x})
    # Test for simple case with single term
    terms = ['test1']
    ret = l.run(terms)
    assert ret == ['/my/content\n']
    # Test with multiple terms
    terms = ['test1', 'test1']
    ret = l.run(terms)
    assert ret == ['/my/content\n', '/my/content\n']
    # Test with multiple terms, one missing
    terms = ['test3', 'test1']
    try:
        l.run(terms)
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 14:39:59.970841
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['test_file_for_unvault_lookup']
    result = lookup.run(terms)
    assert result == [u'This is unvault lookup test file\n']

# Generated at 2022-06-13 14:40:00.398691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:40:07.726129
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    contents = b'[foobar]\nlocalhost\n'
    import os
    import tempfile
    import shutil
    from ansible.parsing.vault import VaultLib
    module_args = {'vault_password_file': '~/.vault_password.txt'}
    tmp_lookup_path = tempfile.mkdtemp()
    lookup_file = os.path.join(tmp_lookup_path, 'inventory.yml')
    vault_file = os.path.join(tmp_lookup_path, 'vault_inventory.yml')
    with open(lookup_file, 'wb') as f:
        f.write(contents)
    vault = VaultLib(**module_args)
    vault_data = vault.encrypt(contents)

# Generated at 2022-06-13 14:40:19.494270
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib

    utils = {
        "decrypt_text": lambda x, y: x,
        "encrypt": lambda x, y: y,
        "is_encrypted_text": lambda x: False,
        "is_encrypted_bin": lambda x: False
    }

    test_lookup = LookupModule(loader=None, cli=None, inventory=None,
                               vault_secrets_files=None,
                               decrypt_text=utils["decrypt_text"],
                               encrypt_text=utils["encrypt"],
                               is_encrypted_text=utils["is_encrypted_text"],
                               is_encrypted_bin=utils["is_encrypted_bin"])
    from ansible.parsing.vault import VaultSecret

# Generated at 2022-06-13 14:40:21.688253
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run((1, 2, 3)) == [1, 2, 3]

# Generated at 2022-06-13 14:41:00.995917
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["/etc/passwd", "/etc/group"]
    variables = {}
    lookup = LookupModule()
    lookup.run(terms, variables)

# Generated at 2022-06-13 14:41:04.392547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    m = LookupModule()
    result = m.run(['file.txt'], variables={'ansible_vault_password_file': 'some_file'})
    assert result == ['fööbår\n']

# Generated at 2022-06-13 14:41:08.116501
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    try:
        lookup_module.run([], variables={})
    except Exception as e:
        assert type(e) == AnsibleParserError

    assert lookup_module.run(['/home/user/files/inventory.yml'], variables={}) == ["test inventory"]

# Generated at 2022-06-13 14:41:11.406517
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(terms=['./test/fixtures/lookup_plugin/unvault'])
    assert result == [u'decoded: bar']

# Generated at 2022-06-13 14:41:13.457954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    ret = lookup_module.run(terms=["UnvaultTest.yml"])
    assert ret[0] == "foo: bar\n"

# Generated at 2022-06-13 14:41:15.983542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_name = 'test_LookupModule_run'
    lm = LookupModule()
    assert lm is not None, 'Couldn\'t create LookupModule object for test: %s' % test_name
    # Can't create a test for this one
    return

# Generated at 2022-06-13 14:41:18.328498
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["/usr/share/ansible/plugins/lookup_plugins/test/data/unvaulted_file.txt"]
    variables = {}
    result = LookupModule().run(terms, variables)
    assert result == ['unvaulted file content\n']

# Generated at 2022-06-13 14:41:18.734205
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:41:20.638600
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = [
      'terms',
      dict()
    ]
    assert LookupModule(*args).run() == None



# Generated at 2022-06-13 14:41:26.461173
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._loader = DictDataLoader({'a.yml': """---
foo: bar
bar: baz
"""})
    lookup.set_options(var_options={}, direct={})

    terms = ['a.yml']
    result = lookup.run(terms)
    assert result[0] == """---
foo: bar
bar: baz
"""

# Generated at 2022-06-13 14:42:53.411764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    result = lookup_plugin.run(["Invalid file"], dict())
    assert len(result) == 0
    assert isinstance(result, list)

# Generated at 2022-06-13 14:43:01.293096
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(direct={})
    term = 'tests/unittest_data/unvault_test_file.txt'
    with open("/home/kk/.ansible/tmp/ansible-local-5530VsS/tmp_o7wq3e/vault_pass.txt", "r") as f:
        vault_pass = f.read().rstrip("\n")
    #vault_pass = "testpass"
    #_, _, lookup_result = lookup_module.run([term], variables={'ansible_vault_password': vault_pass})
    _, _, lookup_result = lookup_module.run([term], variables={"vault_password": "testpass"})

# Generated at 2022-06-13 14:43:01.809617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:43:10.278370
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize empty plugin
    lookup = LookupModule()
    # Unit test for run() method: vault file
    terms = ["vault_test_file.yml"]
    display = Display()
    ret = lookup.run(terms=terms, variables=None, **{'vault_password': 'password', '_original_file': 'vault_test_file.yml'})
    assert len(ret) > 0
    assert ret == ["value for vault_test_file\n"]

    # Unit test for run() method: not a vault file
    terms = ["test_file.yml"]
    output = display.display(None, 'test_file.yml')
    ret = lookup.run(terms=terms, variables=None, **{'_original_file': 'test_file.yml'})

# Generated at 2022-06-13 14:43:16.792310
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    lookup = LookupModule()
    lookup._loader = DummyLoader()
    lookup.set_options(var_options={'vars': {'inventory_dir': './'}}, direct={'foo': 'bar'})
    lookup.display = Display()
    assert lookup.run(['test.yml']) == [b'foo: "bar"\n']
    assert [isinstance(v, AnsibleUnsafeText) for v in lookup.run(['test.yml'])] == [True]
    assert lookup.run(['test_var.yml']) == [b'foo: "bar"\n']
    assert lookup.run(['test_var.yml']) == [b'foo: "bar"\n']

# Unit

# Generated at 2022-06-13 14:43:24.140671
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import collections
    import sys
    import pdb
    #pdb.set_trace()

    import os
    import shutil
    from ansible_collections.ansible.community.plugins.module_utils._text import to_bytes, to_text
    from ansible.utils.display import Display
    from ansible.plugins.lookup import LookupBase
    from ansible.errors import AnsibleParserError
    from ansible.plugins.loader import LookupModuleLoader
    from ansible.utils.display import Display
    display = Display()

    # create file in some temporary directory, remember those tests
    # should not rely on actual file names, mainly on the file contents.
    # It is safer to actually create files on testing, to avoid mistakes
    # here, in the tests.
    import tempfile
    dir_name = tempfile.mkd

# Generated at 2022-06-13 14:43:28.018855
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import pytest
    test_dir = "./test/unittest/vault/test_data/test_unvault_run/"
    os.chdir(test_dir)
    with open("test_vault.txt", "wb") as f:
        f.write("hello")
    os.environ["ANSIBLE_VAULT_PASSWORD_FILE"] = "test_vault_pass"
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(["test_vault.txt"]) == ["hello"]
    os.chdir("../../../../../")

# Generated at 2022-06-13 14:43:33.588632
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestVariables:
        basedir = './tests/unit/lookup_plugins/files'

    terms = []
    terms.append('unvault_test.txt')

    lookup_plugin = LookupModule()
    result = lookup_plugin.run(terms, variables=TestVariables)

    # result is a list of length 1 and first element is the content of file
    assert len(result) == 1
    assert result[0] == 'unvault_test\n'

# Generated at 2022-06-13 14:43:41.214858
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from io import BytesIO
    import os

    fd, fname = tempfile.mkstemp()
    os.close(fd)


# Generated at 2022-06-13 14:43:43.071630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(None, None).run([], {}) == []
