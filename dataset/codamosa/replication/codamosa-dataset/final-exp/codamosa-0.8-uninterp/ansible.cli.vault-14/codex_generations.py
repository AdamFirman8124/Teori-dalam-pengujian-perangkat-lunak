

# Generated at 2022-06-12 20:43:30.730207
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
  c = VaultCLI()
  c.execute_encrypt_string()

# Generated at 2022-06-12 20:43:34.948517
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    target = VaultCLI()
    context.CLIARGS = dict(args=['foo'])
    with mock.patch.object(target.editor, 'create_file', return_value=None) as mock_create_file:
        target.execute_create()
        mock_create_file.assert_called_once_with('foo', None, vault_id=None)


# Generated at 2022-06-12 20:43:46.063108
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():

  test_VaultCLI = VaultCLI()

  # unit test 1
  test_args = dict(
    args = [],
    output_file = None
  )
  test_VaultCLI.context.CLIARGS = test_args

  test_VaultCLI.execute_decrypt()

  # unit test 2
  test_args = dict(
    args = ["-"],
    output_file = None
  )
  test_VaultCLI.context.CLIARGS = test_args

  test_VaultCLI.execute_decrypt()

  # unit test 3
  test_args = dict(
    args = ["-"],
    output_file = "~/.ansible/tmp/ansible-tmp-1552377159.35-272901610628285/encrypted"
  )


# Generated at 2022-06-12 20:43:49.796146
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    # Test method "execute_view" of class "VaultCLI"
    pass



# Generated at 2022-06-12 20:43:56.425071
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    # Set up
    context.CLIARGS = dict(args=['test_file.yml'], output_file=None,
                           keep_template=False, vault_password_file=None,
                           plaintext_vault_password_file=None,
                           no_log=False, vault_ids=None,
                           new_vault_password_file=None,
                           new_vault_ids=None, key=None, config=None,
                           vault_password=None,
                           encrypt_vault_id=None,
                           new_vault_id=None)
    context.settings = settings = C()
    context.become_pass = None
    context.become_method = None
    settings.__dict__.update(C.config.__dict__)
    loader = D

# Generated at 2022-06-12 20:43:57.742621
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    pass



# Generated at 2022-06-12 20:44:08.339122
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    secret = 'secret'
    vault_id = 'ansible-vault'
    empty_args = []
    cliargs = {
        'vault_password_file': '',
        'args': empty_args,
        'output_file': '',
        'encrypt_vault_id': 'ansible-vault',
        'encrypt_string_prompt': '',
        'encrypt_string_stdin_name': '',
        'decrypt_vault_id': '',
        'encrypt_string_names': ''
    }

    vault_secrets = [{'vault_id': vault_id, 'password': secret}]

    # Setup mocks
    run_command_mock = MagicMock(return_value=None)

# Generated at 2022-06-12 20:44:09.385099
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    pass


# Generated at 2022-06-12 20:44:13.152992
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    v = VaultCLI()
    m = MagicMock()
    v.setup_vault_secrets = m
    v.run()
    m.assert_called()


# Generated at 2022-06-12 20:44:16.518365
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    v = VaultCLI()
    # test args are empty
    # Call the method (it doesn't have Returns, so just test no failure.)
    v.execute_edit()



# Generated at 2022-06-12 20:44:49.281438
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    from ansible.cli.vault import VaultCLI

    import ansible.module_utils.basic
    from ansible.parsing.vault import VaultSecret

    # create a test vault CLI and Editor
    cli = VaultCLI([''], '')
    cli.editor = MockVaultEditor()

    cli.execute_edit()

    # the editor will have encrypted and decrypted
    assert cli.editor.encrypted and cli.editor.decrypted



# Generated at 2022-06-12 20:44:59.011783
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    v = VaultCLI()
    # from unittest.mock import Mock
    # test_vault_secrets = Mock()
    # test_encrypt_secret = Mock()
    # test_encrypt_secret.splitlines = test_encrypt_secret
    # test_vault_secrets.splitlines = test_vault_secrets
    # test_vault_secrets.splitlines.return_value = ['vault_id: ****************', 'vault_password: ****************']
    # test_encrypt_secret.splitlines.return_value = ['vault_id: ****************', 'vault_password: ****************']
    # v.setup_vault_secrets = Mock()
    # v.setup_vault_secrets.return_value = test_vault_secrets
    # test_

# Generated at 2022-06-12 20:45:08.790483
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    ansible_module_mock = AnsibleModuleMock()
    context.CLIARGS = {'ask_vault_pass': False,
    'args': ['file1', 'file2'],
    'encrypt_vault_id': '',
    'encrypt_new_vault_id': '',
    'encrypt_new_vault_id_prompt': False,
    'encrypt_vault_id_prompt': False,
    'encrypt_vault_id_string': False,
    'new_vault_id': '',
    'new_vault_password_file': None,
    'output_file': None,
    'prompt': None,
    'vault_password_file': '',
    'vault_id': '',
    'verbosity': False}

# Generated at 2022-06-12 20:45:11.672610
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    module = AnsibleModule(
        argument_spec = dict(
            args = dict(type='list'),
            pager = dict(type='list'),
            editor = dict(type='list'),
            ),
        )
    cli = VaultCLI(module)
    cli.execute()



# Generated at 2022-06-12 20:45:19.092533
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    mycli = VaultCLI()
    context.CLIARGS = {
        'args' : [
            'foo.yml',
            'bar.yml'
        ],
        'ask_vault_pass' : True,
        'new_vault_password_file' : None,
        'new_vault_id' : None,
        'encrypt_string_names': None,
        'func' : 'execute_view',
        'pager': 'less',
        'output_file': None,
        'vault_password_file': None
    }
    assert mycli.editor.vault.secrets is None
    mycli.run()
    assert type(mycli.editor.vault.secrets) == list

# Generated at 2022-06-12 20:45:25.995068
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # Fixture - used by all testcases
    vault_cli = VaultCLI()
    vault_cli.setup_vault_secrets = MagicMock(return_value=['test_vault_password'])
    # Method under test is called once
    vault_cli.editor.encrypt_bytes = MagicMock(return_value=b'Q2lwaGVyVGV4dA==')
    vault_cli.pager = MagicMock()
    VaultCLI_execute_encrypt_string_args = {'encrypt_string_prompt':True, 'ask_vault_pass': False, 'encrypt_string': 'test string'}
    context.CLIARGS = VaultCLI_execute_encrypt_string_args
    vault_cli.execute_encrypt_string()
    assert 1 == vault_cli

# Generated at 2022-06-12 20:45:36.209724
# Unit test for method post_process_args of class VaultCLI

# Generated at 2022-06-12 20:45:43.136090
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    test_vault_opts = {'encrypt_vault_id': 'vault1'}
    # test_vault_opts['encrypt_vault_id'] = 'vault1'
    test_vault_secrets = {'vault1': 'vault1secret'}
    test_new_vault_secrets = {'vault2': 'vault2secret', 'vault1': 'vault1secret'}
    # test_vault_secrets['vault1'] = 'vault1secret'
    test_new_encrypt_secret = ['vault2', 'vault2secret']
    # test_new_encrypt_secret[0] = 'vault2'
    # test_new_encrypt_secret[1] = 'vault2secret'
    test_editor

# Generated at 2022-06-12 20:45:48.097969
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    if not os.path.exists(os.devnull):
        raise AssertionError('os.devnull does not exist')

    saved_stdin = sys.stdin
    saved_stdout = sys.stdout
    saved_stderr = sys.stderr


# Generated at 2022-06-12 20:45:59.366939
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    args = ['-v', 'test_execute_decrypt.yml']

# Generated at 2022-06-12 20:47:04.515909
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    from ansible.cli.vault import VaultCLI
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    import os
    import sys

    # Make a temporary file to build our test data
    (fd, vault_file) = tempfile.mkstemp()
    os.close(fd)

    # Create a VaultSecret to store the vault password we will use in tests
    vault_secret = VaultSecret(b'ansible')
    vault_secret.set_vault_id('testvault')

    # Create a VaultLib to encrypt the test data
    vault_manager = VaultLib([vault_secret])

    # Encrypt

# Generated at 2022-06-12 20:47:11.595833
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    # vault_CLI = VaultCLI()
    # TODO: this is a terrible place for this, but oh well for now
    global display
    display = Display()

    # TODO: make test_VaultCLI_run testable
    # vault_CLI.run(action='encrypt', encrypt_secret='secrettest')
    # TODO: make test_VaultCLI_run testable
    # vault_CLI.run(action='decrypt')
    pass

# Generated at 2022-06-12 20:47:16.396450
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    import ansible.utils
    # Needed for mocking
    import __main__
    import os.path
    from ansible.parsing import loaders
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.context_objects import CLI
    import ansible.plugins
    from ansible.plugins.loader import action_loader, connection_loader, cache_loader, vars_loader, lookup_loader, filter_loader, test_loader, strategy_loader, terminal_loader, strategy_loader
    from ansible.errors import AnsibleOptionsError, AnsibleError
    # The arguments that would normally be passed to the Ansible module
    args = None
    # The exit_json method returns the key-value results
    exit_json = None
    # The fail_json method returns the key-value results

# Generated at 2022-06-12 20:47:23.053037
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    # create a VaultCLI with predetermined options
    # create a fake command line options
    args = "ansible-vault encrypt foo.yml --vault-password-file=~/.vault_pass.txt".split()
    parser = VaultCLI.base_parser(constants.DOCUMENTATION, constants.EPILOG, '2.7')
    cliargs = parser.parse_args(args)

    vault_cli = VaultCLI(cliargs)

    vault_cli.execute_encrypt()

# Generated at 2022-06-12 20:47:25.044808
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    """
    Unit test for method run of class VaultCLI
    """
    # FIXME: vault secret?
    runner = Runner()
    vaultcli = VaultCLI(runner)
    assert False



# Generated at 2022-06-12 20:47:36.908864
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    from ansible.parsing.vault import VaultLib
    from ansible.cli.vault import VaultCLI
    v = VaultLib({"test": "test"})
    vaultcli = VaultCLI(v)
    display = Display()
    src=to_bytes("test_data")
    filename="test_decrypt_file.txt"
    with open(filename, 'wb') as f:
        f.write(vaultcli.editor._encrypt_bytes(src, vault_id="test"))
    vaultcli.execute_decrypt(["test_decrypt_file.txt"])
    with open('test_decrypt_file.txt', 'rb') as f:
        assert f.read() == b'test_data\n'
    os.remove(filename)

# Generated at 2022-06-12 20:47:44.308391
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    vault_cli = VaultCLI()
    vault_cli.encrypt_secret = 'abc123'
    vault_cli.editor = FakeEditor()
    context.CLIARGS = {'encrypt_string': True, 'encrypt_string_prompt': True, 'encrypt_string_read_stdin': False, 'encrypt_string_stdin_name': None, 'show_string_input': False, 'encrypt_string_names': [], 'ask_vault_pass': False, 'vault_password_file': None, 'new_vault_password_file': None, 'output_file': None, 'args': [], 'encrypt_vault_id': 'cipher1'}
    vault_cli.execute()


# Generated at 2022-06-12 20:47:48.400673
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    cliargs = dict(encrypt='foo.txt,bar.txt', foo='bar')
    args = dict(args=cliargs)
    cli = VaultCLI(args)
    assert cli.post_process_args(cliargs['encrypt']) == ['foo.txt', 'bar.txt']



# Generated at 2022-06-12 20:47:54.596534
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    argv = ["ansible-vault", "edit", "foo"]

    with patch.object(VaultCLI, "_setup_vault_secrets") as mock_VaultCLI__setup_vault_secrets:
        with patch.object(VaultCLI, "_load_plugins") as mock_VaultCLI__load_plugins:
            with patch.object(sys, "exit") as mock_sys_exit:
                # Call method
                cli = VaultCLI(args=argv)
                cli.parse()
                cli.run()

                # Ensure methods were called
                assert mock_VaultCLI__setup_vault_secrets.called
                assert mock_VaultCLI__load_plugins.called
                # Ensure we exited with a call to sys.exit
                assert mock_sys_exit.called

# Generated at 2022-06-12 20:48:04.864955
# Unit test for method execute_encrypt_string of class VaultCLI

# Generated at 2022-06-12 20:49:22.861332
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        # fixture
        cli = VaultCLI()
        cli.execute_rekey()

    assert pytest_wrapped_e.type == SystemExit


# Generated at 2022-06-12 20:49:27.601690
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    argv = ['-k', 'my_secret', 'create' 'my_file.yml']
    options = cli.parse(argv, output_opts=False)
    cli.setup_vault_secrets(options, vault_ids=['my_secret'], ask_vault_pass=False)
    vault_cli = VaultCLI()
    vault_cli.run()

    assert os.path.isfile('my_file.yml')

    os.remove('my_file.yml')



# Generated at 2022-06-12 20:49:36.078182
# Unit test for method run of class VaultCLI

# Generated at 2022-06-12 20:49:38.690670
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():


    vault_cli = VaultCLI()

    # Test if method can be called
    vars = {}
    vault_cli.execute_create()



# Generated at 2022-06-12 20:49:46.481572
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    my_vault = VaultCLI()
    with pytest.raises(AnsibleOptionsError) as e:
        my_vault.execute_encrypt()
    assert 'Vault password must be specified' in to_native(str(e))

    my_vault.vault_password = 'ansible'
    with pytest.raises(AnsibleOptionsError) as e:
        my_vault.execute_encrypt()
    assert 'Must specify files to encrypt' in to_native(str(e))

    my_vault.args = ['test/test_vault.py']
    my_vault.execute_encrypt()


# Generated at 2022-06-12 20:49:55.389071
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # vault_secret is bytes
    vault_secret = b"vault_secret"

    # create an instance of the VaultCLI class with vault_secret
    # use it to encrypt "encrypt_this_string"
    # store the result in b_encrypted_string
    vault_cli = VaultCLI([], vault_secret=vault_secret)

    b_plaintext_list = [(b"encrypt_this_string", "", "")]

    # list of dicts {'out': '', 'err': ''}
    outputs = vault_cli._format_output_vault_strings(b_plaintext_list)

    for output in outputs:
        out = output.get('out', '')

    # expected_out is the expected ansible-vault output for encrypting "encrypt_this_string"
    expected_out

# Generated at 2022-06-12 20:49:57.589584
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    vault_cli = VaultCLI()
    vault_cli.execute_rekey()

# Generated at 2022-06-12 20:50:03.118329
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    assert False
# end class VaultCLI

COMMAND_LOADERS = {
    'connection': loader.connection_loader,
    'shell': loader.shell_loader,
    'module': loader.module_loader,
    'module_utils': loader.module_utils_loader,
    'lookup': loader.lookup_loader,
    'filter': loader.filter_loader,
    'callback': loader.callback_loader,

    # things that used to be commands but are now aliases
    # we need to keep these to not break backwards compat
    'become': loader.become_loader,
    'cliconfig': loader.config_loader,
}


# Generated at 2022-06-12 20:50:06.433924
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    expected_result = None
    actual_result = None
    try:
        obj = VaultCLI()
        obj.execute_view()
    except Exception as e:
        actual_result = (type(e), e.args)
    assert expected_result == actual_result



# Generated at 2022-06-12 20:50:13.669832
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    args = [ 'ansible-playbook', '--vault-id testvault_id@prompt --vault-password-file testvault_password_file', 'testplaybook' ]
    parsed_args = CLI.parser.parse_args(args)
    context.CLIARGS = vars(parsed_args)
    cli = VaultCLI(args)
    cli.execute_encrypt()

# Generated at 2022-06-12 20:50:48.726502
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    from ansible.utils import context_objects as co
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.plugins.callback import CallbackBase
    from ansible.inventory.manager import InventoryManager
    from ansible.cli import CLI
    import os
    import json
    import sys
    import pytest
    import ansible.inventory
    import ansible_mock

    # Fixture function that provides the arguments, and initializes
    # the context to run the run() method
    @pytest.fixture
    def run_fixture(request):
        # Initialize context, an instance of AnsibleCLI()
        context

# Generated at 2022-06-12 20:51:00.723930
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    tmp_path = tempfile.mkdtemp()
    test_file_path = os.path.join(tmp_path, 'foo')

# Generated at 2022-06-12 20:51:02.345109
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    cli = VaultCLI(args=[])
    cli.post_process_args()


# Generated at 2022-06-12 20:51:12.692459
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    cli = VaultCLI()
    context.CLIARGS = dict()
    context.CLIARGS['args'] = [ 'ansible.cfg' ]
    context.CLIARGS['output_file'] = 'ansible.cfg.enc'
    context.CLIARGS['vault_password_file'] = './test/test_vault_pass.txt'
    with open('test/test_vault_pass.txt', 'w') as f:
        f.write('ansible')

    cli.execute_encrypt()
    assert os.path.exists('ansible.cfg.enc')

    b_plaintext = to_bytes(u'I like cheese')
    b_ciphertext = cli.editor.encrypt_bytes(b_plaintext)
    cli.editor.decrypt_

# Generated at 2022-06-12 20:51:14.115407
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    vaultcli = VaultCLI()
    vaultcli.execute_encrypt()

# Generated at 2022-06-12 20:51:15.085379
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    pass



# Generated at 2022-06-12 20:51:18.870025
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    # test with sample_argv
    command = VaultCLI(args=sample_argv)
    command.post_process_args(sample_parser)


# Generated at 2022-06-12 20:51:29.138030
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    playbook_dir = tempfile.mkdtemp(prefix='ansible_test_vault_cli')

# Generated at 2022-06-12 20:51:38.160080
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    test_cli = VaultCLI()

    test_cli.setup_vault_secrets = MagicMock()

    test_cli.editor = MagicMock()

    test_cli.editor.encrypt_file = MagicMock()
    test_cli.editor.encrypt_bytes = MagicMock()

    test_cli.editor.decrypt_file = MagicMock()

    test_cli.editor.create_file = MagicMock()

    test_cli.editor.edit_file = MagicMock()

    test_cli.editor.plaintext = MagicMock()

    test_cli.pager = MagicMock()

    test_cli.editor.rekey_file = MagicMock()

    class test_context():
        class test_CLIARGS():
            func = MagicMock()
            show_string_input

# Generated at 2022-06-12 20:51:49.048778
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    # Probably best to not use the file system as we might read unexpected files or write
    # where we don't want to
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-12 20:52:34.209755
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    from ansible.cli.vault import VaultCLI

    import os
    import tempfile
    import sys

    class Options:
        def __init__(self, filename, encrypt_string_prompt=False, encrypt_string_stdin=False,
                     encrypt_string_stdin_name="", show_string_input=False):
            self.filename = filename
            self.encrypt_string_prompt = encrypt_string_prompt
            self.encrypt_string_stdin = encrypt_string_stdin
            self.encrypt_string_stdin_name = encrypt_string_stdin_name
            self.show_string_input = show_string_input

        def __getitem__(self, key):
            return getattr(self, key, None)


# Generated at 2022-06-12 20:52:41.302070
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    # FIXME: this fixture does not get called twice, so the fixture always has
    # setup_vault_secrets = True, even after _get_setup_vault_secrets() returns False
    # on the 2nd run.  This is ok to do because the 2nd fixture arg is not used, just
    # needs to exist.
    setup_vault_secrets = True
    test_args = ['--extra-vars', '@test']
    fake_loader = unittest.mock.MagicMock()
    fake_editor = unittest.mock.MagicMock()
    expected_args = ['--extra-vars']
    expected_searched_vars = ['@test']
    fake_context = unittest.mock.MagicMock()

# Generated at 2022-06-12 20:52:52.280950
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    # Tests for VaultCLI.execute_decrypt
    # Test with basic case, where input is a file with plain text and output is
    # a file with encrypted text.
    #

    @patch('sys.stdout')
    @patch('ansible.parsing.vault.VaultLib')
    @patch('ansible.parsing.vault.VaultLib.decrypt_file', return_value='decrypted_text')
    def create_vault(mock_decrypt_file, mock_vault_lib, mock_stdout):
        vault_cli = VaultCLI()
        vault_cli.editor = vault_cli.create_vault_editor('password')
        return vault_cli


# Generated at 2022-06-12 20:52:55.333789
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # execute_encrypt_string()  # TODO: how to test this? we can't use the display.prompt() 
    # 
    # TODO: mock out tty, stdin
    # TODO: mock out output
    pass

