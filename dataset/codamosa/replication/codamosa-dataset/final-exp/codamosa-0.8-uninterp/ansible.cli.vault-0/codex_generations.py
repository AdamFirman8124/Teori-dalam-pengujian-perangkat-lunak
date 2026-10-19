

# Generated at 2022-06-12 20:43:46.062394
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    # Imports required within this example
    from units.compat import unittest
    from units.compat.mock import MagicMock, patch
    from ansible.module_utils._text import to_bytes

    context.CLIARGS = {'args': ['testfile'], 'c': False, 'create_new_password': True, 'encrypt_vault_id': 'test_vault_id'}


# Generated at 2022-06-12 20:43:49.492060
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()
    pass

# Generated at 2022-06-12 20:43:56.184679
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    from ansible.utils.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    loader, path_dwim, vault_secret = _get_mock_data('vault_data.yml', 'vault.key')
    post_vars = {}
    vault_id = 'P@$$w0rd1'
    vault = VaultLib([(vault_id, vault_secret)])

    plaintext_before = 'This is a secret'
    context.CLIARGS['args'] = ['vault_test_file.yml']
    context.CLIARGS['output_file'] = 'vault_test_file.yml.output'
    context.CLIARGS['func'] = lambda: None
    vault_cli = VaultCL

# Generated at 2022-06-12 20:43:59.897536
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    err = ''
    unittest.TestCase().assertEqual(
        err,
        VaultCLI().execute_decrypt(),
        'Test if err is return by execute_decrypt')

# Generated at 2022-06-12 20:44:04.217815
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
  cliArgs = {'args': [ "encrypted.txt" ], 'output_file': None}
  vaultLib = VaultLib([("id1", "password1")])
  vaultEditor = VaultEditor(vaultLib)
  vaultCLI = VaultCLI("decrypt", cliArgs, vaultEditor)
  vaultCLI.execute_decrypt()


# Generated at 2022-06-12 20:44:15.391401
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    '''
    AnsibleVaultCLI object should init with CLIARGS built from parser
    '''

    # Fixtures to avoid calling 'ansible-vault'
    options = AnsibleVaultCLI._options()
    parser = CLI.base_parser(constants.DEFAULT_MODULE_PATH, options=options)
    CLI.add_vault_options(parser)
    context.CLIARGS = parser.parse_args(['--encrypt', 'foo.yml'])
    context.VAULT_PASSWORDS_FILE = None

    vault = VaultCLI()

    # TODO: make more robust test, not just a post_process_args() no-exception
    vault.post_process_args()
    assert True is True

# Generated at 2022-06-12 20:44:23.977445
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    from ansible.utils.display import Display
    import os
    import sys

    _display = Display()

    # Load a dummy vault secret
    dummy_password = b'pass'
    dummy_secret = VaultLib(None)._encrypt_string(dummy_password, None)

    v = VaultCLI(dummy_secret, _display)
    v._setup_args()
    v.run()

    # Change the prefix, so main can execute the changed context.CLIARGS
    old_prefix = context.CLIARGS_PREFIX
    context.CLIARGS_PREFIX = 'vault_'

# Generated at 2022-06-12 20:44:32.611489
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    """
    Test: encrpyt_string is called on instances of VaultCLI
    Given:
        - A VaultCLI instance with a VaultLib and VaultEditor
        - an encrypt_string_prompt and an encrypt_string_read_string arguments
    When:
        - A VaultCLI instance is called with the execute_encrypt_string method
    Then:
        - The VaultCLI instance calls its VaultEditor's encrypt_bytes() method
        - The returned ciphertext is displayed.
    """

    # TODO: mock this out in the tests?
    def prompt(msg, private=False):
        if private:
            return 'prompted_text'
        return 'prompted_text'

    # TODO: mock this out in the tests?
    def pager(msg):
        return 'pager_text'

    #

# Generated at 2022-06-12 20:44:39.768362
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    test_input = StringIO()
    test_output = StringIO()
    test_args = [
        'ansible-vault', 'encrypt_string', '-v', '-n', 'var_name',
        'var_value', '-n', 'other_var', 'other_value',
        '--encrypt-vault-id', 'enc@foo.com',
    ]
    vault_cli = VaultCLI(args=test_args,
                         stdin=test_input,
                         stdout=test_output,
                         stderr=test_output)
    # We need to mock out the editor's encrypt_bytes
    # method so we don't encrypt when running unit tests
    # pylint: disable=unused-argument
    # The first argument is self, but pylint doesn't
    # handle mock

# Generated at 2022-06-12 20:44:42.880821
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    vaultcli = VaultCLI()
    with pytest.raises(AnsibleOptionsError) as excinfo:
        vaultcli.execute_create()
    assert to_text(excinfo.value) == "ansible-vault create can take only one filename argument"


# Generated at 2022-06-12 20:45:13.177331
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
  CLI = VaultCLI()
  CLI.editor = VaultEditor()
  CLI.encrypt_secret = "abcd"
  CLI.execute_encrypt()



# Generated at 2022-06-12 20:45:18.105380
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # Set up required vars that VaultCLI._format_output_vault_strings needs.
    # This is kind of a cheaty way of testing this method, but it works and
    # lets us leave the actual VaultCLI stuff alone.
    mock_secret = 'mock_secret'
    mock_vault_id = 'mock_vault_id'

    # b_plaintext_list is a list of tuples.  In each tuple, the first element is
    # the actual b_plaintext string to be encrypted.  There are always two more
    # elements to the tuple, a string (either 'prompt' or 'args') representing
    # where the string came from and a string (or None) for the variable name.

# Generated at 2022-06-12 20:45:22.826366
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():

    vault_cli = VaultCLI()
    vault_cli.editor = mock.Mock()
    vault_cli.pager = mock.Mock()
    f = u'file1'

    vault_cli.execute_view(vault_files=[f])

    vault_cli.editor.plaintext.assert_called_with(f)
    vault_cli.pager.assert_called_with(u'plaintext')


# Generated at 2022-06-12 20:45:34.238011
# Unit test for method post_process_args of class VaultCLI

# Generated at 2022-06-12 20:45:46.258166
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()

    default_vault_ids = ['id_rsa']
    def test(args, expected_output, expected_vault_ids):
        # print(args, expected_output, expected_vault_ids)
        context.CLIARGS = cm.parse_args(['ansible-vault', 'encrypt'] + args, vault_ids=default_vault_ids)
        context.CLIARGS['func'] = vault_cli.execute_encrypt_string
        vault_secrets, vault_ids = vault_cli.post_process_args()
        print(vault_secrets)
        print(vault_ids)

        assert vault_ids == expected_vault_ids

        formated_vault_secrets = []

# Generated at 2022-06-12 20:45:50.624148
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    args = get_data('vault/vault-cli-args.yml')
    test = VaultCLI(args)

    result = test.post_process_args()

    assert result is None

# Generated at 2022-06-12 20:45:51.195930
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():

    # Not implemented yet
    assert False



# Generated at 2022-06-12 20:45:54.759279
# Unit test for method execute_view of class VaultCLI

# Generated at 2022-06-12 20:45:55.780267
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    pass



# Generated at 2022-06-12 20:46:02.992652
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    file_name = 'test_file.txt'

    random_str = 'qwertyuiopasdfghjklzxcvbnm'
    plaintext = random_str

    # create vault file
    with open(file_name, 'w') as f:
        f.write(plaintext)
    vault_secrets = {'secret': 'abc'}
    vault_cli = VaultCLI(vault_secrets)
    # open file for edit
    vault_cli.editor.edit_file(file_name)
    # check file content
    with open(file_name) as f:
        ciphertext = f.read()
    assert ciphertext != plaintext

    # Unit test for method execute_view of class VaultCLI
    # open file for view

# Generated at 2022-06-12 20:46:46.109434
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    vault_cli = VaultCLI(args=['ansible-vault', 'edit', '--output-file', 'file_name'])
    assert vault_cli.parser.parse_args(['ansible-vault', 'edit', '--output-file', 'file_name']) == vault_cli.options



# Generated at 2022-06-12 20:46:57.109920
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()

    #args_dict = dict(encrypt=False, decrypt=False, editor=False, create=False, rekey=False, output=False, view=False, args=[])
    args_dict = dict(encrypt=True, decrypt=False, editor=False, create=False, rekey=False, output=False, view=False, args=['/vagrant/ansible-vault/test/unit/hacking/test_data/test.yml'])
    #args_dict = dict(encrypt=False, decrypt=True, editor=False, create=False, rekey=False, output=False, view=False, args=['/vagrant/ansible-vault/test/unit/hacking/test_data/test.yml.enc'])
    #args_dict = dict(

# Generated at 2022-06-12 20:47:05.946460
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    # Implicit setup for test_VaultCLI_execute_decrypt
    # Setup mock_loader
    mock_loader = Mock()
    vault_secrets = []
    mock_loader.get_vault_secrets.return_value = vault_secrets

    # Setup mock_Options
    mock_Options = Mock()
    mock_ask_pass = False
    mock_new_vault_password_file = []
    mock_new_vault_id = []
    mock_new_vault_password = []
    mock_output_file = None
    mock_encrypt_vault_id = []
    mock_encrypt_vault_password_file = []
    mock_encrypt_vault_password = []
    mock_args = []
    mock_Options.ask_vault_pass = mock_ask_pass

# Generated at 2022-06-12 20:47:12.095464
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    print('')
    print('')

    obj = VaultCLI()
    context.CLIARGS = {'verbosity': 0}
    obj.setup_vault_secrets(context.CLIARGS['vault_ids'], context.CLIARGS['vault_password_files'], context.CLIARGS['new_vault_password_file'])
    obj.execute_view()

# Generated at 2022-06-12 20:47:13.659040
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    # Creating an instance of the VaultCLI class
    vault_cli = VaultCLI()
    # Calling the method execute_rekey
    vault_cli.execute_rekey()


# Generated at 2022-06-12 20:47:21.028633
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    vault_id = None
    vault_string = 'this is a test'
    vault_string_binary = b'this is a test'
    text = 'this is a test\n'
    b_text = to_bytes(text)

    assert execute_encrypt_string(vault_string, vault_id) == b_text

    assert execute_encrypt_string(vault_string_binary, vault_id) == b_text

    # test that it still works when given a named variable to return
    assert execute_encrypt_string(vault_string, vault_id, 'foo') == b'this is a test\n'

# Generated at 2022-06-12 20:47:29.803440
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    vaultcli = VaultCLI()

    vaultcli.editor = VaultEditor(None)
    context.CLIARGS = {'args': ['filename'], 'encrypt_vault_id': None }

    vaultcli.execute_create()

    assert vaultcli.editor.create_file.called
    # assert vaultcli.editor.create_file.call_args_list[0][0][0] == 'filename'
    # assert vaultcli.editor.create_file.call_args_list[0][1] == {'encrypt_secret': None, 'vault_id': None}


# Generated at 2022-06-12 20:47:31.917436
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    vault_cli = VaultCLI()
    ret = vault_cli.execute_view()

    assert ret is None


# Generated at 2022-06-12 20:47:36.909274
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    cli = VaultCLI()
    cli.editor = {}
    cli.editor.plaintext = lambda *args, **kwargs: b'foo'
    cli.pager = lambda *args, **kwargs: None
    cli.execute_view()


# Generated at 2022-06-12 20:47:44.723576
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    display = Display()
    vault_password = b'asdfasdf'
    args = ['filename', '--encrypt-vault-id', 'test@test']
    cliargs = {'encrypt_vault_id': 'test@test',
               'ask_vault_pass': False,
               'verbosity': 0,
               'args': ['filename'],
               'output_file': None,
               'encrypt_vault_id_prompt': False}
    enc_secret = to_bytes('asdfasdf')

    class FakeLoader(object):
        def get_vault_ids(self):
            return ['test@test']

    loader = FakeLoader()


# Generated at 2022-06-12 20:48:51.360871
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    # TODO: Add unit tests for things that are not implemented
    pass

# Generated at 2022-06-12 20:49:01.161109
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    # Create a new "parser" object, and return the values provided by it
    # if the args provided to it are valid.
    def _get_parser(args):
        parser = VaultCLI.base_parser(constants.DEFAULT_VAULT_ID, constants.DEFAULT_VAULT_PASSWORD_FILES)
        options, _ = parser.parse_known_args(args)

        return options

    # Call the "post_process_args" method using the values returned by the
    # parser as an argument
    def _test(args):
        args = to_text(args).split()
        options = _get_parser(args)
        cli = VaultCLI(args)
        cli.post_process_args(options)


# Generated at 2022-06-12 20:49:02.642268
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    assert True


# Generated at 2022-06-12 20:49:04.445985
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    vault_cli = VaultCLI()
    vault_cli.execute_decrypt()


# Generated at 2022-06-12 20:49:13.217253
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    """
    Test the execute_create() method of the VaultCLI class
    """
    # Initialize the class structure
    test_context = context.CLIARGS
    test_context['args'] = ['test_file']
    test_context['encrypt_vault_id'] = ""
    test_context['encrypt_secret'] = ""
    test_context['vault_password_file'] = ""
    test_context['vault_ids'] = ""
    test_context['new_vault_password_file'] = ""
    test_context['new_vault_ids'] = ""
    test_context['new_vault_id'] = ""
    test_context['new_encrypt_secret'] = ""
    test_context['new_encrypt_vault_id'] = ""

# Generated at 2022-06-12 20:49:22.861800
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():

    fixture_path, fixture_name = os.path.split(os.path.realpath(__file__))
    vault_password_file = os.path.join(fixture_path, 'fixtures', 'ansible-vault-password-file')

    test_args = ['ansible-vault', 'view', '--vault-password-file', vault_password_file, os.path.join(fixture_path, 'fixtures', 'ansible-vault-test-file')]

    with mock.patch.object(sys, 'argv', test_args):
        VaultCLI = get_file_vault_action_plugin(None)

        with mock.patch('os.path.exists') as exists_mock:
            exists_mock.return_value = False
            VaultCLI.parse()


# Generated at 2022-06-12 20:49:24.805501
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    vcli = VaultCLI()
    # TODO: create a context.CLIARGS dict to avoid a KeyError
    # vcli.execute_edit()

# Generated at 2022-06-12 20:49:30.152010
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    mod = AnsibleModule()
    mod.editor = '/usr/bin/vi'
    vault_secrets = ['donttell']
    mod.vault_password = 'donttell'
    secret = random_password()
    filename = 'donttell'
    cli = VaultCLI(mod)
    cli.encrypt_secret = secret
    cli.pager = lambda x: x
    cli.editor = VaultEditor(VaultLib(vault_secrets))
    cli.editor.decrypt_file = lambda x: secret
    cli.execute_view([filename])
    assert cli.editor.decrypt_file(filename) == secret


# Generated at 2022-06-12 20:49:41.021360
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    arg2 = {}
    arg2['args'] = ['/home/ansible/ansible/test/testdata/sample_vault_file']
    arg2['new_vault_id'] = 'my_second_vault_password'
    arg2['new_vault_password_file'] = '/home/ansible/ansible/test/testdata/vault_password_file'
    arg2['verbosity'] = 0
    arg2['ask_vault_pass'] = False
    context.CLIARGS = arg2
    x = VaultCLI()
    x.encrypt_secret = 'my_vault_password'
    x.encrypt_vault_id = 'my_vault_password'
    x.new_encrypt_vault_id = 'my_second_vault_password'


# Generated at 2022-06-12 20:49:48.334457
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()
    myargs = {'func': 'encrypt_string', 'args': ['abc', 'def', 'ghi'], 'encrypt_string_names': ['foo', 'bar'], 'encrypt_string_read_stdin': True}
    expected_args = {'func': 'encrypt_string', 'args': ['abc', 'def', 'ghi'], 'encrypt_string_names': ['foo', 'bar', None, None], 'encrypt_string_read_stdin': True}
    vault_cli.post_process_args(myargs)
    assert myargs == expected_args


# Generated at 2022-06-12 20:51:53.563731
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
  # Test that 'ansible-vault encrypt' fails when no arguments are provided
  with pytest.raises(AnsibleOptionsError) as exception_info:
    vault_cli = VaultCLI()
    vault_cli.execute_encrypt()
  assert 'Supply one or more filenames' in str(exception_info.value)

  # Test that 'ansible-vault encrypt' successfully encrypts a plain file
  argv_save = sys.argv

# Generated at 2022-06-12 20:51:57.616948
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    # instantiate the class
    vault_cli = VaultCLI()
    # instantiate the attribute
    context.CLIARGS = False
    # call the run method
    vault_cli.run()


# Generated at 2022-06-12 20:52:07.647638
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():

    # FIXME: add test for missing secrets
    # FIXME: should these be in 1 test or each in their own test?

    # run an encryptor/editor test on a file
    def run_vault_editor(tmp, encrypt_secret, vault_id, output_file=None):
        # create a test file
        with open(tmp, 'w') as fh:
            fh.write('bar')

        # encrypt file
        encrypt_argv = ['ansible-vault', 'encrypt', tmp,
                        '--vault-id', vault_id + '@prompt',
                        '--vault-password-file', encrypt_secret]
        if output_file:
            encrypt_argv.extend(['--output', output_file])

# Generated at 2022-06-12 20:52:14.018966
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    vault_secret = b'testvaultsecret\n'
    encrypt_secret = vault_secret
    encrypt_vault_id = 'foo'

    # Setup required mocks.
    class Args(dict):
        @property
        def args(self):
            return ['bar']

    class MockVaultEditor(object):
        def __init__(self, *args, **kwargs):
            pass

        def create_file(self, *args, **kwargs):
            pass

    # Call the method
    with patch.multiple('ansible.parsing.vault', editor_path=None, VaultEditor=MockVaultEditor):
        vault_cli = VaultCLI(encrypt_secret=encrypt_secret, encrypt_vault_id=encrypt_vault_id)
        vault_cli.editor = MockV

# Generated at 2022-06-12 20:52:20.995453
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # execute_encrypt_string() will encrypt a single string using the user-provided vault_secret.
    # The resulting vaulted string will be formatted in YAML suitable for use in a playbook file.
    # If the user has provided a string name, this name will be used as the YAML variable name.
    # If the user has not provided a string name, the output will consist of a YAML scalar with
    # a leading comment explaining that this is the encrypted output of a string.
    # If more than one string is provided, the encrypted output of each string will be separated
    # by comments to allow the user to distinguish them.
    pass

# VaultCLI tests

# Generated at 2022-06-12 20:52:23.862643
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    vault_cli = VaultCLI()
    vault_cli.execute_encrypt()


# Generated at 2022-06-12 20:52:31.556504
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    v = VaultCLI()
    v.setup_vault_secrets = mock.Mock()
    v.editor = mock.Mock()
    v.editor.decrypt_file = mock.Mock()
    v.execute_decrypt(['a', 'b'])
    expected = [mock.call('a'), mock.call('b')]
    assert v.editor.decrypt_file.call_args_list == expected, \
        "execute_decrypt should decrypt all files"


# Generated at 2022-06-12 20:52:39.292489
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    args = {}
    args['encrypt_vault_id']  = None
    args['new_vault_id']  = None
    args['new_vault_password_file']  = None
    args['ask_vault_pass']  = False
    args['output_file']  = None
    args['vault_password_file']  = None
    args['vault_ids']  = None
    args['verbosity']  = 0
    args['ask_vault_pass_vault_id']  = None
    args['args']  = ['hosts']

# Generated at 2022-06-12 20:52:43.433616
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    vault_cli = VaultCLI()
    with patch('sys.argv', ['ansible-vault', 'create', '--output-file', 'test_VaultCLI_execute_create']):
        context.CLIARGS = context.VaultCLI.load_args()
        vault_cli.execute_create()

# Generated at 2022-06-12 20:52:53.526341
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    vault_file_path    = os.path.abspath('./tests/test_data/vault-test3-password.yml')
    vault_password_str = 'ansible'

    # The following file is created by test_VaultLib_create_key
    # It contains a single binary key.
    vault_secret_file  = os.path.abspath('./tests/test_data/vault-test-key')
    vault_secret_key   = open(vault_secret_file, 'r').read()

    b_vault_password_str = to_bytes(vault_password_str, errors='surrogate_or_strict')
    b_vault_secret_key   = to_bytes(vault_secret_key, errors='surrogate_or_strict')

   