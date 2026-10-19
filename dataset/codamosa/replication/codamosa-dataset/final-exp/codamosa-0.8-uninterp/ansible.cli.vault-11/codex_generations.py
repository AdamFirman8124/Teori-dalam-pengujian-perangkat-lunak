

# Generated at 2022-06-12 20:43:42.830905
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    args = ['ansible-vault create test']
    context.CLIARGS = {'subcommand': 'create',
                       'args': ['a']}
    context.vault = VaultCLI()



# Generated at 2022-06-12 20:43:50.205067
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    with tempfile.NamedTemporaryFile() as tfile:
        tfile.write(b"key: !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n3137333336653336643731373332396332633338313466646330663332323865343237626164613631323461613731363064\n66666436663364386635643964333138393865656263613431386231383665383038373839656439306638636334666432\n33333735366436613037666362336433663162663639306439663165316665623632653634383365\n")
        tfile.flush()
        loader = DataLoader()

# Generated at 2022-06-12 20:43:56.712466
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # create an instance
    # args = command line args to pass to main function
    ldict = locals()
    args = ["ansible-vault", "encrypt_string", "/Users/Christopher/Documents/ansible/tests/sanity/test_vault_copy_plaintext/test_vault/main.yml", "--name", "foo", "bar", "--name", "baz", "foo", "--encrypt-vault-id", "@prompt"]

# Generated at 2022-06-12 20:44:03.671337
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    import random
    import string
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.vault.playbook import PlaybookVaultSecret
    from units.compat.mock import MagicMock
    from units.compat.mock import patch
    from ansible.cli.vault import VaultCLI
    vault_password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(10))
    vault_password_file = '/home/foo_user/vault-password-file'
    secret = VaultSecret(vault_password, vault_password_file)
    context = dict(CLIARGS=dict(unused_arg='unused_arg'))

# Generated at 2022-06-12 20:44:11.078249
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    vaultcli = VaultCLI()
    args = context.CLIARGS
    args['encrypt_vault_id'] = None
    args['vault_password_file'] = None
    args['vault_ids'] = None
    args['action'] = 'encrypt'
    args['ask_vault_pass'] = False
    argv = ['']
    with pytest.raises(AnsibleOptionsError) as excinfo:
        vaultcli.parse(args=argv)
    assert 'A vault password is required' in str(excinfo.value)


# Generated at 2022-06-12 20:44:21.764825
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    from units.compat.unittest import TestCase
    test_case = TestCase()

    class CLIMock(object):
        class AnsibleVaultCLI(object):
            def __init__(self):
                pass

            def cli(self):
                pass

    with patch('ansible.cli.VaultCLI', new=CLIMock.AnsibleVaultCLI):
        cli = VaultCLI(args=[])
        test_case.assertIsInstance(cli, CLIMock.AnsibleVaultCLI)
        test_case.assertIsNotNone(cli)

    cli = VaultCLI(args=[])

    assert cli.in_data is None
    assert cli.out_data is None
    cli.in_data = to_bytes('Hello world!')

    # TOD

# Generated at 2022-06-12 20:44:31.604582
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    tmpdir = tempfile.mkdtemp()
    print('TMP_DIR: %s' % tmpdir)

    # Example call:
    # python3 -m unittest tests/test_vault_cli.py VaultCLI.test_VaultCLI_execute_encrypt

    # FIXME: this is ugly.  Do we really want to write to a file here?
    # write vault password to file
    vault_secret = b'vault_secret'
    vault_password_file = os.path.join(tmpdir, 'vault_password')
    with open(vault_password_file, 'w') as f:
        f.write(to_native(vault_secret))

    # write the vault file to encrypt
    vault_file = os.path.join(tmpdir, 'vault')

# Generated at 2022-06-12 20:44:34.654610
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    pass


# Generated at 2022-06-12 20:44:43.560713
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    vault_secret = 'vault_secret'
    filename = 'filename'
    output_file = 'output_file'
    args = []
    encrypt_vault_id = 'encrypt_vault_id'
    new_vault_ids = []
    new_vault_password_files = []
    vault_secrets = {'vault_id': vault_secret}
    ask_vault_pass = False
    create_new_password = False

    class TestClass(Exception):
        def __init__(self):
            self.editor = VaultCLI.TestEditor()

    class TestEditor(Exception):
        def __init__(self):
            pass

        def encrypt_file(self, filename, vault_secret, output_file=None, **kwargs):
            pass


# Generated at 2022-06-12 20:44:44.625070
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    pass


# Generated at 2022-06-12 20:45:17.627468
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    '''
    Unit test for method post_process_args of class VaultCLI
    '''

    # Invoke method
    cli = VaultCLI()
    try:
        cli.post_process_args()
    except Exception as e:
        if str(e) == 'Post-processing for VaultCLI.post_process_args not implemented':
            pass
        else:
            raise e

    # Output processing
    # Test for an exception
    if (Exception):
        raise Exception('Caught exception during output processing for VaultCLI.post_process_args')


# Generated at 2022-06-12 20:45:25.115973
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultEditor
    from ansible.utils._text import to_bytes
    from ansible.utils.path import unfrackpath
    from ansible.errors import AnsibleOptionsError
    from ansible.cli.vault import match_encrypt_secret
    from ansible.module_utils._text import to_text
    import pytest
    import yaml
    import os
    import textwrap
    import tempfile

    def test_match_encrypt_secret():
        assert match_encrypt_secret([(1, 3)]) == (1, 3)

        # use first secret
        assert match_encrypt_secret([(1, 3), (2, 3)])

# Generated at 2022-06-12 20:45:30.859048
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    vault_secret = u"foo"
    vault_password_file = u"bar"
    args = [u"baz"]
    cliargs = {
        u"encrypt_vault_id": u"foo",
        u"ask_vault_pass": False,
        u"new_vault_password_file": vault_password_file,
        u"new_vault_id": u"bar",
        u"ask_new_vault_pass": True,
        u"output_file": None,
        u"args": args
    }
    environment = {
        u"vault_password_file": vault_password_file,
        u"ANSIBLE_VAULT_PASSWORD_FILE": vault_password_file
    }

# Generated at 2022-06-12 20:45:40.128730
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()
    context.CLIARGS = dict(identities=['foo'], identity_vault_ids=['bar'],
                           identity_vault_password_file=['baz'])
    vault_cli.post_process_args()
    assert context.CLIARGS == dict(identities=['foo'], identities_vault_ids=['bar'],
                                   identity_vault_password_files=['baz'],
                                   identities_vault_passwords=[])


# Generated at 2022-06-12 20:45:53.362473
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    from ansible_collections.ansible.community.tests.unit.plugins.modules import vault_cli
    vault_cli.CLIARGS['args'] = ['/tmp/test_vaultj2xrf8.yml']

# Generated at 2022-06-12 20:45:54.636189
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    argv = ['ansible-vault', 'encrypt']
    cli = VaultCLI(argv)
    cli.setup()
    cli.run()


# Generated at 2022-06-12 20:45:56.010940
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    '''test_VaultCLI_post_process_args'''

# Generated at 2022-06-12 20:46:02.714120
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    context.CLIARGS = dict(args=['--encrypt-string-prompt'])
    context.CLIARGS['encrypt_string_prompt'] = True
    context.CLIARGS['encrypt_string_read_stdin'] = False
    context.CLIARGS['encrypt_string_stdin_name'] = None
    context.CLIARGS['vault_ids'] = ['default']
    old_umask = os.umask(0o077)
    try:
        vault = VaultCLI()
    finally:
        os.umask(old_umask)
    # This function is pure, so it will not depend on any state
    assert vault.execute_encrypt_string() is None

# Generated at 2022-06-12 20:46:08.504373
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    args = context.CLIARGS

    # context.CLIARGS = {'help': False, 'force': True, 'ask_pass': False, 'ask_su_pass': False, 'ask_sudo_pass': False, 'ask_vault_pass': False, 'become': False, 'become_ask_pass': False, 'become_method': 'sudo', 'become_user': 'root', 'check': False, 'connection': 'smart', 'diff': False, 'flush_cache': False, 'force_handlers': False, 'inventory': None, 'listhosts': None, 'listtags': None, 'listtasks': None, 'module_path': None, 'new_vault_password_file': None, 'output_file': None, 'poll_interval': 15, 'private_key_file': None, '

# Generated at 2022-06-12 20:46:18.164908
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    # Workaround: ensure ArgvIndexError is defined and imported
    from ansible.utils.vault import VaultCLI
    # FIXME: this test can't be run with unit test as it is, because
    # exceptions defined in the same file as a function requiring them
    # are not yet visible at the time the decorator is evaluated.  Thus the
    # decorator never sees the exception and the exception is never
    # returned.
    with pytest.raises(AnsibleOptionsError) as exc:
        VaultCLI(args=['foo'])
    assert str(exc.value) == 'ansible-vault create can take only one filename argument'
    with pytest.raises(AnsibleOptionsError) as exc:
        VaultCLI(args=['create', 'foo', 'bar'])
    assert str(exc.value)

# Generated at 2022-06-12 20:46:54.230429
# Unit test for method run of class VaultCLI

# Generated at 2022-06-12 20:47:04.483119
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    def doit():
        for d in [ '/home/vagrant', '/home/vagrant/ansible' ]:
            if os.path.exists(d):
                break
        else:
            d = ''
        os.chdir(d)
        v = VaultCLI()
        # FIXME: make this readable:
        setattr(v, 'encrypt_string_prompt', False)
        setattr(v, 'encrypt_string_read_stdin', True)
        setattr(v, 'show_string_input', False)
        setattr(v, 'encrypt_vault_id', C.DEFAULT_VAULT_IDENTITY)
        # setattr(v, 'encrypt_secret', 'foo')

# Generated at 2022-06-12 20:47:06.106125
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()
    # TODO
    pass

# Generated at 2022-06-12 20:47:16.543802
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    """Test VaultCLI test_VaultCLI_run() function

    :return
    """
    class FakeContext():
        CLIARGS = {}

    class FakeVaultLib():
        class FakeVault():
            def __init__(self, vault_secrets):
                pass

        def __init__(self, vault_secrets):
            pass

    class FakeVaultEditor():
        def __init__(self, vault):
            pass

        def create_file(self, f, vault_secret, vault_id):
            pass

        def edit_file(self, f):
            pass

        def plaintext(self, f):
            return 'plaintext'

        def rekey_file(self, f, new_secret):
            pass


# Generated at 2022-06-12 20:47:17.964496
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    vault_cli = VaultCLI()
    vault_cli.execute_decrypt()



# Generated at 2022-06-12 20:47:26.281777
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    entity = VaultCLI()

    # Test with an invalid arg passed
    argv = ['-l']
    context.CLIARGS = {'action': 'create', 'ask_pass': False, 'ask_vault_pass': False, 'create_new_password': False}
    with pytest.raises(AnsibleError) as excinfo:
        print(entity.post_process_args(argv))
    assert '  -l\n\nVault\n' in str(excinfo.value)

    # Test with a valid arg passed
    argv = ['-l', 'a']
    context.CLIARGS = {'action': 'create', 'ask_pass': False, 'ask_vault_pass': False, 'create_new_password': False}

# Generated at 2022-06-12 20:47:37.843239
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    mock_args = {
        'func': 'execute_decrypt',
        'ask_vault_pass': True,
        'encrypt_vault_id': 'test_encrypt_id',
        'new_vault_id': 'test_new_id',
        'output_file': 'test_output_file',
        'vault_password_file': 'test_password_file',
        'version': False,
    }
    inventory = MagicMock(spec=Inventory)
    loader = MagicMock(spec=DataLoader)
    display = MagicMock(spec=Display)
    context_cliargs = MagicMock()
    context_display = MagicMock()
    context_display.columns = 80
    context.CLIARGS = context_cliargs
    context_cliargs.__getitem__

# Generated at 2022-06-12 20:47:41.347533
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt(): 
    with patch.object(sys, "argv", ["ansible-vault", "decrypt", "/tmp/ansible_test/test_VaultCLI"]):
        cli = VaultCLI(args=dict())
        cli.run()
    assert to_text(cli.editor.vault.password) == "password"


# Generated at 2022-06-12 20:47:41.933407
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    pass

# Generated at 2022-06-12 20:47:44.828076
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():

    # Encrypt the plaintext, and format it into a yaml block that can be pasted into a playbook.
    # For more than one input, show some differentiating info in the stderr output so we can tell them
    # apart. If we have a var name, we include that in the yaml
    # ok
    pass



# Generated at 2022-06-12 20:48:12.714228
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    # Test the case where the action is 'encrypt'
    vault_id = 'vaultid'
    vault_password = 'somepassword'
    new_vault_id = 'new_vault_id'
    new_vault_password = 'new_vault_password'
    loader = mock.Mock(spec=DataLoader)
    vault_secrets = [
        (vault_id, vault_password),
        (new_vault_id, new_vault_password)
    ]


# Generated at 2022-06-12 20:48:22.268953
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vault import VaultEditor
    from ansible.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode
    from ansible.errors import AnsibleOptionsError
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.context import AnsibleContextDeprecated as context
    import ansible.utils.display as display
    import ansible.constants as C
    import ansible.utils.unsafe_proxy as unsafe_proxy
    import os
    import sys
    import six
    import collections
    import ansible.plugins.loader as plugin_loader


# Generated at 2022-06-12 20:48:27.594407
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # note that we are not using a tempdir here, so if something
    # creates a file called "vault_ids" in the current directory
    # it will get picked up and used

    # test password file
    vpf_path = 'test_vault_pw1'
    vpf_file = open(vpf_path, 'w')
    vpf_file.write(b'ansible')
    vpf_file.close()


# Generated at 2022-06-12 20:48:33.756026
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    #
    # Test: call execute_view(self)
    #
    # Create a test instance
    test_instance = VaultCLI()
    # Test the method with an invalid argument
    test_args = []
    test_kwargs = {}
    with pytest.raises(AnsibleOptionsError):
        test_instance.execute_view(*test_args, **test_kwargs)


# Generated at 2022-06-12 20:48:39.791819
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    args = ['-', '-o', '-', '-n', '-n', '-n', '-n', '-n', '-n', '-n', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-v', '-f', '-f', '-h']
    context.CLIARGS = AnsibleOptions(args)
    context.CLIARGS['func'] = Mock()
    context.CLIARGS['ask_vault_pass'] = False

    # This is the setup for the real vault password mechanism
    context.CLIARGS['vault_password_file'] = []

# Generated at 2022-06-12 20:48:46.227738
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # Create a mock host and context
    host = Mock()
    context = Mock()
    context.CLIARGS = {'encrypt_string_prompt': False,
                       'encrypt_string_stdin': False}

    # Run execute_encrypt_string
    vault_cli = VaultCLI()
    vault_cli.execute_encrypt_string()



# Generated at 2022-06-12 20:48:47.108822
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
	pass


# Generated at 2022-06-12 20:48:50.124271
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_loader = DictDataLoader({})
    vc = VaultCLI(vault_loader)
    #post_process_args() missing 1 required positional argument: 'args'
    args = [None, "create"]
    vc.post_process_args(None, args)
    assert True


# Generated at 2022-06-12 20:48:51.090587
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    vault = VaultCLI()
    vault.execute_encrypt_string()

# Generated at 2022-06-12 20:48:52.681327
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    from ansible.cli import CLI
    cli = CLI(args=[])
    vault = VaultCLI(cli)
    vault.run(args=[])
    assert True


# Generated at 2022-06-12 20:49:34.460712
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    pass

# Generated at 2022-06-12 20:49:44.626406
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    context = Connection('testhost')
    context.CLIARGS = dict(encrypt_vault_id='test', encrypt_string_prompt=True)

    loader = DataLoader()
    vault_secrets = [('test', 'testsecret')]

    def mock_display(*args, **kwargs):
       display.display(*args, **kwargs)

    def mock_pager(text):
        pass

    context._loader = loader
    context._set_log_output(False)
    v = VaultCLI(context)
    v.display = mock_display
    v.pager = mock_pager
    v._format_output_vault_strings = lambda x, y: "Test"
    v.run()

# Generated at 2022-06-12 20:49:53.517291
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    test_file = os.path.join(os.getcwd(), 'test.txt')
    vault_id = 'test'
    secret = 'testsecret'
    vault = {vault_id: secret}
    with open(test_file, 'w') as f:
        f.write('test')

    cli = VaultCLI(['ansible-vault', 'edit', test_file])
    cli.encrypt_vault_id = vault_id
    cli.editor.vault = VaultLib(vault)
    cli.editor.encrypt_file = lambda *args: None
    cli.editor.decrypt_file = lambda *args: None
    cli.execute_edit()
    os.remove(test_file)



# Generated at 2022-06-12 20:50:04.054630
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    args = [
            {
               'encrypt_string_prompt': True,
               'encrypt_string_stdin': False,
               'encrypt_string_stdin_name': None,
               'encrypt_string_names': None,
               'new_vault_id': None,
               'encrypt_vault_id': None,
               'new_vault_password_file': None,
               'output_file': None,
               'ask_vault_pass': False,
               'encrypt_string_newline': False,
               'func': 'EDIT',
               'stdin_args': [],
               'args': [],
               'vault_password_file': [],
               'vault_ids': [''],
               'show_string_input': False
            }
    ]

   

# Generated at 2022-06-12 20:50:11.617321
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    from units.mock.path import mock_unfrackpath_noop
    test_old_encrypt_secret = 'foo'
    test_new_encrypt_secret = 'bar'
    test_new_encrypt_vault_id = 43
    test_file = '/tmp/test_file'

    test_vault_cli = VaultCLI()
    test_vault_cli.new_encrypt_secret = test_new_encrypt_secret
    test_vault_cli.new_encrypt_vault_id = test_new_encrypt_vault_id

    ###########################################################################
    # method test
    ###########################################################################
    test_editor = MagicMock()
    test_vault_cli.editor = test_editor
    test_vault_cli.execute_rekey()



# Generated at 2022-06-12 20:50:12.555374
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    v = VaultCLI()
    v.run()


# Generated at 2022-06-12 20:50:18.093820
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vault import match_encrypt_secret
    from ansible.utils.vault import VaultSecret

    vault_secrets = [VaultSecret('vault_password', 's3cr3t', 'default')]

    vault = VaultLib(vault_secrets)
    editor = VaultEditor(vault)
    method_args = {
        'action': 'encrypt',
        'encrypt_secret': match_encrypt_secret(vault_secrets)[1],
        'encrypt_vault_id': 'default'
    }

    # Verify we're testing what we think we're testing.

# Generated at 2022-06-12 20:50:29.294840
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    # set up arguments
    args = mock.MagicMock()
    args.action = 'create'
    args.ask_vault_pass = False
    args.encrypt_vault_id = None
    args.encrypt_string_read_stdin = False
    args.encrypt_string_names = False
    args.encrypt_string_stdin_name = None
    args.encrypt_string_prompt = None
    args.file = None
    args.new_vault_password_file = None
    args.new_vault_id = None
    args.output_file = None
    args.vault_password_file = None
    args.vault_id = ['Default']
    # run test
    testobj = VaultCLI(args)
    testobj.execute_create()
    # assert

# Generated at 2022-06-12 20:50:34.313336
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    from ansible.parsing.dataloader import DataLoader
    from ansible.cli.adhoc import AdHocCLI

    fixture_path = os.path.join(fixtures_path, 'adhoc/')

    def _mock_ask_vault_pass(prompt=None, confirm=False, auto_prompt=True, reprompt=False, relogin=False):
        return 'secret'

    monkeypatch = mock.patch('ansible.parsing.vault.VaultLib.ask_vault_pass', _mock_ask_vault_pass)
    monkeypatch.start()

    dataloader = DataLoader()


# Generated at 2022-06-12 20:50:36.990081
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # ''' encrypt the supplied string using the provided vault secret '''
    with pytest.raises(AnsibleOptionsError):
        VaultCLI().execute_encrypt_string()



# Generated at 2022-06-12 20:51:22.094363
# Unit test for method execute_create of class VaultCLI

# Generated at 2022-06-12 20:51:23.565736
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    pass # TODO: implement your test here


# Generated at 2022-06-12 20:51:24.171424
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    pass

# Generated at 2022-06-12 20:51:34.217011
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    vault_cli = VaultCLI()
    vault_cli.pager = lambda x: print(x)
    vault_cli.editor = VaultEditor(VaultLib([]))

    # getcwd() can return a unicode string on systems with a unicode default
    # encoding.  We want to try to just use bytes here, so turn cwd into
    # bytes.
    if isinstance(os.getcwd(), text_type):
        cwd = to_bytes(os.getcwd())
    else:
        cwd = os.getcwd()

    # Test filepath handling
    # Test relative path
    vault_cli.editor.plaintext = lambda x: x
    vault_cli.execute_view(['test/test.yml'])

    # Test absolute path

# Generated at 2022-06-12 20:51:41.441779
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    conn_info = None

    if context.CLIARGS.get('version'):
        print(C.DEFAULT_BANNER)
        sys.exit(0)

    if context.CLIARGS.get('help_cmd'):
        parser.print_help()
        sys.exit(0)

    if not context.CLIARGS.get('action'):
        raise AnsibleOptionsError("Incorrect number of arguments passed")

    # this is somewhat redundant as the parser only allows one of these options to be specified
    if context.CLIARGS['action'] not in ['create', 'decrypt', 'edit', 'encrypt', 'encrypt_string', 'rekey', 'view']:
        raise AnsibleOptionsError("Invalid command passed, please specify create, edit, decrypt, encrypt, encrypt_string, rekey or view")



# Generated at 2022-06-12 20:51:44.528941
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    vault_cli = VaultCLI()

    vault_cli.execute_create()

test_VaultCLI_execute_create()

# Generated at 2022-06-12 20:51:46.781151
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    # TODO: test run method
    # TODO: test methods called when executing actions
    pass


# Generated at 2022-06-12 20:51:47.761369
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    pass


# Generated at 2022-06-12 20:51:53.861280
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    args = []
    context.CLIARGS = {}
    context.CLIARGS = {'args': args}
    context.CLIARGS['func'] = VaultCLI.execute_encrypt_string
    context.CLIARGS['args'] = args
    context.CLIARGS['encrypt_string_prompt'] = False
    expected = None
    actual = VaultCLI.execute_encrypt_string()
    assert actual == expected

# Generated at 2022-06-12 20:52:05.295410
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultEditor
    from ansible.cli.vault import VaultCLI
    from ansible.cli.vault import VaultEditorCLI
    import contextlib
    import mock
    import sys

    class FakeLoader(object):
        def __init__(self, vault_password_files=[], vault_ids=[]):
            self.vault_password_files = vault_password_files

        def set_vault_secrets(self, vault_secrets):
            self.secrets = vault_secrets

        def get_basedir(self):
            return None


# Generated at 2022-06-12 20:52:46.511794
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    args = 'ansible-vault view test_vault_passed'.split()
    runner = CliRunner()
    context.CLIARGS = {'ask_vault_pass': False}

    # enc: !vault |
    #       $ANSIBLE_VAULT;1.1;AES256
    #       38363739303331636432353766323731663730353466313963386665353132363637623133346235
    #       65386262656338636432623266333466373332643437333065376368620a61333562373938336638
    #       6233316435623065373132326265646162336535363361333132313362356636346466333362316
    #       2626435

# Generated at 2022-06-12 20:52:48.589719
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    vault_cli = VaultCLI()
    with pytest.raises(AnsibleOptionsError):
        vault_cli.run()


# Generated at 2022-06-12 20:52:57.537296
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    args = "data/foo.yml"
    context.CLIARGS['func'] = Mock()
    vault_id = "vault_id"
    encrypt_secret = "encrypt_secret"
    new_encrypt_secret = "new_encrypt_secret"
    new_encrypt_vault_id = "new_encrypt_vault_id"
    vault_editor = VaultLib(encrypt_secret)
    vault_editor.rekey_file = Mock()
    loader = Mock()
    loader.set_vault_secrets = Mock()
    vault = VaultLib(encrypt_secret)
    editor = VaultEditor(vault)