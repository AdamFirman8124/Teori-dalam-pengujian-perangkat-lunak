

# Generated at 2022-06-12 20:43:48.335621
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    # Create a Thing
    thing = VaultCLI()
    # Call method execute_create on it
    test_thing.execute_create()
    # Check state of thing
    assert True


# Generated at 2022-06-12 20:43:55.166996
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    vault_secrets = ['password2']

    vault_file = tempfile.NamedTemporaryFile()


    vault_file_path = vault_file.name

    my_vault = VaultLib(vault_secrets)
    my_vault.encrypt_file(vault_file_path, vault_secrets[0])

    cli_args = {'args': [vault_file_path], 'k': False, 'output': None, 'vault_password_file': None, 'ask_vault_pass': False, 'output_file': None, 'new_vault_id': None, 'new_vault_password_file': None}

    vault_editor = VaultEditor(my_vault)
    my_cli = VaultCLI(cli_args, vault_editor)
    my_cli.execute_

# Generated at 2022-06-12 20:44:06.420895
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    # Test for method execute_encrypt(self)
    # of class VaultCLI
    vault_file = NamedTemporaryFile(delete=False)
    

# Generated at 2022-06-12 20:44:18.289066
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    vault_id = 'the_vault_id'
    vault_password_file = '/path/to/file'
    args = ['test1', 'test2']
    context_args = {'new_vault_id': vault_id}

    # Test with no new vault id specified
    context.CLIARGS = {'args': args}
    cli = VaultCLI(args)
    with pytest.raises(AnsibleOptionsError) as err:
        cli.setup_vault_secrets(loader=None)
    assert 'A new vault password is required to use Ansible\'s Vault rekey' in str(err.value)

    # Test with new vault id specified
    context.CLIARGS = {'args': args}
    context.CLIARGS.update(context_args)
    cl

# Generated at 2022-06-12 20:44:29.179292
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    v = VaultCLI()

    class MockCLIARGS:
        def __init__(self):
            self.ask_vault_pass = False
            self.args = ['foo.yml']
            self.output_file = None
 
        def __call__(self):
            pass

    class MockDisplay:
        @staticmethod
        def display(msg, color='blue'):
            pass

    class MockEditor:
        @staticmethod
        def decrypt_file(f, output_file):
            return "foo"

    class MockVaultLib:
        def __init__(self, vault_secrets):
            pass

    class MockVaultSecret:
        def __init__(self, vault_id, vault_pass, new_vault_pass):
            pass

    context.CLIARGS = MockCL

# Generated at 2022-06-12 20:44:34.380330
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    context.CLIARGS = {'args': [], 'ask_vault_pass': False, 'verbosity': False}
    x = VaultCLI()
    assert isinstance(x.execute_decrypt(), None)


# Generated at 2022-06-12 20:44:35.823868
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    obj = VaultCLI()
    obj.execute_rekey()


# Generated at 2022-06-12 20:44:41.489178
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    argv = ['ansible-vault', 'create', '/playbooks/foo.yml']
    with patch.object(sys, 'argv', argv):
        with pytest.raises(AnsibleOptionsError) as excinfo:
            Application('vault', 'vault').run()
        assert excinfo.value.args[0] == 'ansible-vault create can take only one filename argument'


# Generated at 2022-06-12 20:44:53.598710
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    from ansible.cli.vault import VaultCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.utils.vault import VaultLib
    from ansible.utils.vault import VaultEditor


    v = VaultCLI(args=['edit', '.vault_pass.txt'], vault_password_files=None,
                 auto_prompt=False)

    context.CLIARGS = v.parse()
    vault_password_files = context.CLIARGS['vault_password_files']
    loader = DataLoader()
    display = Display()

    vault_secrets = v.setup_vault_secrets(loader, vault_password_files, auto_prompt=False)

# Generated at 2022-06-12 20:45:01.883031
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    with pytest.raises(AnsibleOptionsError, match=r"A vault password must be specified to encrypt data with Ansible Vault"):
        c = VaultCLI()
        c.encrypt_secret = None
        c.execute_encrypt()

    with pytest.raises(AnsibleOptionsError, match=r"No files to encrypt were found on the command line."):
        c = VaultCLI()
        c.encrypt_secret = "password"
        c.execute_encrypt()

    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "test"), "w") as f:
            f.write("test")
        c = VaultCLI()
        c.encrypt_secret = "password"
        c.execute_encrypt()

# Generated at 2022-06-12 20:45:37.023461
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()
    vault_cli.post_process_args(context.CLIARGS)

    # test that the first positional argument ("args") is now a list
    assert isinstance(context.CLIARGS['args'], list)
    
    # test that the resulting list is properly formatted (with the first item being passed as 'my_file.yml')
    try:
        assert context.CLIARGS['args'][0] == 'my_file.yml'
    except:
        return False

    # test that the resulting list is properly formatted (with the second item being passed as 'my_file.yml')
    try:
        assert context.CLIARGS['args'][1] == 'my_file2.yml'
    except:
        return False

    # test that the resulting list

# Generated at 2022-06-12 20:45:49.934023
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    _f = os.path.join(os.path.dirname(os.path.realpath(__file__)), __file__)
    _d = os.path.dirname(_f)
    with open(_f, 'rb') as f:
        b_plaintext = f.read()
    data = dict(
        editor=MagicMock(
            encrypt_bytes=MagicMock(return_value=b'12345'),
            encrypt_file=MagicMock()
        ),
        encrypt_vault_id='test_encrypt_vault_id',
        encrypt_secret='test_encrypt_secret',
    )
    cli = VaultCLI(**data)
    cli.execute_encrypt()

# Generated at 2022-06-12 20:46:00.071187
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():

    v = VaultCLI()

    # create a test file to encrypt

    import tempfile
    test_file = tempfile.NamedTemporaryFile(mode='wt')
    test_file.write('\n'.join(['inline_string', 'string1', 'string2', 'string3', 'string4']))
    test_file.flush()

    cli_args = {'encrypt_vault_id': 'id_rsa'}
    v.setup_vault_secrets(FakeVaultSecretLoader, cli_args=cli_args)

    # Test cli_args={'output_file': None} => encrypted content is written to the original file
    #        cli_args={'output_file': 'encrypted.txt'} => encrypted content is written to 'encrypted.txt' file
    #        cli_args

# Generated at 2022-06-12 20:46:00.730139
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # assert True
    return True



# Generated at 2022-06-12 20:46:06.372483
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    test_vault_file = 'test_vault_file'

    vault_id = '123'
    vault_password = 'secret'

    vault_secrets = {'123': 'secret'}

    loader = DictDataLoader({'vault_passwords': vault_secrets})
    vault = VaultLib(vault_secrets)
    editor = VaultEditor(vault)

    cli = VaultCLI([], loader=loader, editor=editor)
    cli.encrypt_secret = vault_password
    cli.encrypt_vault_id = vault_id
    cli.execute_create()

    assert os.path.exists(test_vault_file)

    os.remove(test_vault_file)



# Generated at 2022-06-12 20:46:07.848775
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    self = VaultCLI()

# Generated at 2022-06-12 20:46:17.556079
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    context.CLIARGS = {
        'action': 'create',
        'args': ['foo'],
        'encrypt_vault_id': 'vault_id_01',
        'output_file': None,
        'new_vault_id': None,
        'new_vault_password_file': None,
    }
    context.VAULT_PASS_FILE = 'vault_pass_file'
    from ansible.errors import AnsibleOptionsError
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.vault import get_file_vault_secret
    from ansible.parsing.vault import match_encrypt_secret

# Generated at 2022-06-12 20:46:20.430282
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    vault_cli = VaultCLI()
    vault_cli.editor()
    with pytest.raises(AnsibleOptionsError):
        vault_cli.execute_create()



# Generated at 2022-06-12 20:46:22.265779
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    from nose import SkipTest
    raise SkipTest("TODO: write your unit test for VaultCLI.run")

# Generated at 2022-06-12 20:46:32.623280
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    from ansible.utils.display import Display
    display = Display()

    mock_context = MagicMock()
    mock_loader = MagicMock()
    mock_options_error = MagicMock()
    mock_display = MagicMock()
    mock_encrypt_secret = MagicMock()

    # Mimic the vault_secrets dict that would normally be returned from self.setup_vault_secrets()
    # mock_loader.get_vault_secrets.return_value.items() = {'foo': 123}

    vault_cli = VaultCLI(mock_context, mock_loader)

    # confirm that encrypt_string_read_stdin is true
    assert vault_cli.encrypt_string_read_stdin is True

    # mock out the stdin sys.stdin.read.return_value = 'string

# Generated at 2022-06-12 20:47:16.626348
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        # FIXME: VaultCLI needs a bunch of init arguments
        # Test with a bad option
        with pytest.raises(AnsibleOptionsError):
            VaultCLI(args=['create', '-i', '/etc/ansible/roles/foo/vars/main.yml'])

    # Test with a valid option
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        # FIXME: VaultCLI needs a bunch of init arguments
        VaultCLI(args=['view',
                       '-i', '/etc/ansible/roles/foo/vars/main.yml',
                       '--vault-password-file', '/etc/ansible/vault_pass.txt'])


# Generated at 2022-06-12 20:47:27.923177
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    target = VaultCLI()
    globals()['display'] = FakeDisplay()

    fake_vault_secrets = [('default', 'VaultSecret1'), ('default', 'VaultSecret2')]
    target.setup_vault_secrets = lambda x, y, z, a, b : fake_vault_secrets

    fake_cmd_args = ('vault_command', '--encrypt', '--encrypt_vault_id', 'default', '--encrypt_string_prompt', 'test')
    cmd_args = fake_cmd_args + ('--encrypt_string_files', '/test/test_file_1, /test/test_file_2')
    target.setup_vault_ids = lambda x, y, z, a : ['default']
    target.encrypt_string_read_stdin

# Generated at 2022-06-12 20:47:35.631583
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader

    from ansible.utils.display import Display
    from ansible.utils.display import Display
    from ansible.utils.vault import VaultEditor

    loader = AnsibleLoader(None, vault_secrets=None)
    vault = VaultLib(vault_secrets=None)
    display = Display()
    editor = VaultEditor(vault)

    v = VaultCLI(loader, display, editor)

    # Check with valid args
    args = dict(
        encrypt_string='secret',
        encrypt_string_prompt=True,
        encrypt_string_stdin=True,
        encrypt_vault_id='mysecret',
        func=v.execute_encrypt
    )
   

# Generated at 2022-06-12 20:47:39.548852
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    vault_cli = VaultCLI()
    cli_args = dict(
        new_vault_password_file=False,
        encrypted_vault_id=False,
        ask_vault_pass=False,
        vault_password_file=False,
        create_new_password=False,
        encrypt_vault_id=False,)
    setattr(context, 'CLIARGS', cli_args)
    assert not vault_cli.post_process_args('')


# Generated at 2022-06-12 20:47:48.928417
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    from ansible.cli.vault import VaultCLI
    from ansible.parsing.vault import VaultLib
    context = Mock()
    vault_cli = VaultCLI(context)
    f = 'test.txt'
    vault_cli.editor = Mock()
    vault_cli.encrypt_secret = u'foo'
    vault_cli.encrypt_vault_id = 'a'
    vault_cli.execute_create()
    assert vault_cli.editor.edit_file.call_count == 1
    assert_has_calls(vault_cli.editor.edit_file, [call(f)])
    # Test create_file
    file_name = 'test.yml'
    data = 'test'
    vault_lib = VaultLib([('a', u'foo')])
    vault_lib

# Generated at 2022-06-12 20:47:54.893641
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    pass
# and restore umask

import os
old_umask = os.umask(0)
# END
# BEGIN
if __name__ == '__main__':
    cli = VaultCLI()
    try:
        cli.run()
    except AnsibleError as e:
        cli.logger.error(to_text(e))
        exitcode = 1
    except SystemExit as e:
        pass
    else:
        exitcode = 0

    # Fixme: exitcode is None if skip_log_init
    if exitcode is not None:
        sys.exit(exitcode)
# END
# -*- coding: utf-8 -*-
#
# Ansible Vault documentation build configuration file, created by
# sphinx-quickstart on Wed Jun 21 10:13:32 2017.

# Generated at 2022-06-12 20:47:57.550488
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    # Testing the case when a file is created
    # Testing the case when more than one file is created
    pass

# Generated at 2022-06-12 20:48:04.950605
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    """Tests method execute_rekey of class VaultCLI"""
    class_ = VaultCLI
    # TODO: construct object for test
    method = 'execute_rekey'

    args = ''
    kwargs = {}

    # TODO: construct call arguments
    # call_args = (, )
    # call_kwargs = {}

    # TODO: run test
#    result = class_(*args, **kwargs).execute_rekey(*call_args, **call_kwargs)
    result = None

    # TODO: assert result
#    assert result == expected

    raise SkipTest # Temporarily skipped


# Generated at 2022-06-12 20:48:16.971930
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
    # Test execute_rekey method
    # Test cli.test_vault rekey example.yml --vault-password-file vault_password.txt --new-vault-password-file new_vault_password.txt
    test_vault = VaultCLI({
        'command': 'rekey',
        'vault_password_file': 'vault_password.txt',
        'new_vault_password_file': 'new_vault_password.txt',
        'args': ['example.yml']
    })
    test_vault.setup()
    test_vault.execute_rekey()

    # Test cli.test_vault rekey example.yml --vault-password-file vault_password.txt --new-vault-password-file new_vault_password.txt --encrypt-

# Generated at 2022-06-12 20:48:24.656949
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.module_utils.six import string_types, binary_type
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.utils.display import Display
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor

    v = VaultCLI()
    assert isinstance(v, VaultCLI)

    # pylint: disable=protected-access
    v._display = Display()
    v._loader = None
    v._vault = VaultLib()
    v.editor = VaultEditor(VaultLib())

    #
    # create test
    #
    # fake create_parser
    # pylint: disable=unused-variable


# Generated at 2022-06-12 20:49:10.936633
# Unit test for method execute_view of class VaultCLI
def test_VaultCLI_execute_view():
    import tempfile
    import pytest
    import os
    import shutil

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create a temporary file to use with VaultCLI.execute_view
    fn = 'test_VaultCLI_execute_view'
    file_path = os.path.join(temp_dir, fn)
    with open(file_path, 'w') as f:
        f.write('test_VaultCLI_execute_view')

    # Verify that the file was created
    assert os.path.isfile(file_path) is True

    # Make a VaultCLI object, encrypt the temporary file and write the
    # resulting ciphertext back to the file
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-12 20:49:21.917577
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    print(u'Start unit test for method run of class VaultCLI.')

    # Pre-check
    before_struct = inspect.getmembers(context)
    before_context_CLIARGS = context.CLIARGS
    assert((context.CLIARGS == {}) or (context.CLIARGS == None))

    # Setup test data
    context.CLIARGS = {}
    context.CLIARGS['name'] = 'ansible-vault'
    context.CLIARGS['func'] = 'fake_function'
    context.CLIARGS['ask_vault_pass'] = True
    context.CLIARGS['output_file'] = None
    context.CLIARGS['args'] = []
    context.CLIARGS['encrypt_string_prompt'] = False

# Generated at 2022-06-12 20:49:28.720993
# Unit test for method execute_create of class VaultCLI

# Generated at 2022-06-12 20:49:29.440983
# Unit test for method execute_view of class VaultCLI

# Generated at 2022-06-12 20:49:39.665298
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    method = 'test_VaultCLI_execute_edit'

    # FIXME: add other inputs for args, encrypt_vault_id, vault_password_file
    args = [os.path.expanduser("~/.ansible/vault_password")]

    # FIXME: we should be mocking the VaultEditor to prevent the actual file from being edited
    # FIXME: add other inputs for args, encrypt_vault_id, vault_password_file
    f = args[0]
    # FIXME: not sure why we need to write the file out again, it was just read in above
    with open(f, 'w') as v_file:
        v_file.write('foo\n')

    context.CLIARGS = {'ask_vault_pass': False, 'output_file': None, 'args': args}

# Generated at 2022-06-12 20:49:41.915450
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    args = {}
    cli = VaultCLI(args)
    cli.run()
# end class VaultCLI


# Generated at 2022-06-12 20:49:43.697196
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    # TODO: create test for VaultCLI.execute_encrypt
    assert True == True

# Generated at 2022-06-12 20:49:48.764790
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
    # create the mock object
    context.CLIARGS = {
        'ask_vault_pass': False,
    }
    # invoke method
    cli = VaultCLI()
    cli.execute_encrypt_string()

if __name__ == '__main__':
    # Unit test for method execute_encrypt_string of class VaultCLI
    test_VaultCLI_execute_encrypt_string()

# Generated at 2022-06-12 20:49:51.591212
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    v = VaultCLI()
    v.editor.decrypt_file = MagicMock()
    v.execute_edit()
    v.editor.decrypt_file.assert_called()


# Generated at 2022-06-12 20:50:02.087670
# Unit test for method execute_decrypt of class VaultCLI
def test_VaultCLI_execute_decrypt():
    """ test_VaultCLI_execute_decrypt() """
    # test case for issue #42410
    runner_args = dict(
        become=False,
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
        extra_vars=(),
        forks=None,
        inventory=None,
        listhosts=None,
        module_path=None,
        pattern=None,
        subset=None,
        tags=[],
        vault_ids=[],
        vault_password_files=[]
    )
    cli = CLI(args=[], runner_args=runner_args)
    cli.get_opt = MagicMock()
    cli.get_opt.__getitem__ = Mock(return_value=None)

# Generated at 2022-06-12 20:51:05.448786
# Unit test for method execute_encrypt_string of class VaultCLI
def test_VaultCLI_execute_encrypt_string():
	# TODO Write unit test
	pass

# Generated at 2022-06-12 20:51:13.697696
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    # Test with MOCK_STDOUT and MOCK_STDERR
    TestCLI.parser = CLI.base_parser(
        usage='%prog [options] encrypt [options] [FILENAME|-]',
        connect_opts=True,
        meta_opts=True,
        runas_opts=True,
        subset_opts=True,
        check_opts=True,
        runtask_opts=True,
        vault_opts=True,
        fork_opts=True,
        module_opts=True,
        json_opts=True
    )
    TestCLI.parser.set_usage('usage: %prog [options] encrypt [options] [FILENAME|-]')

# Generated at 2022-06-12 20:51:14.620836
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    pass # todo


# Generated at 2022-06-12 20:51:17.208932
# Unit test for method execute_edit of class VaultCLI
def test_VaultCLI_execute_edit():
    #
    # Example 1.
    #
    # @TODO: Write your test here.
    #
    pass



# Generated at 2022-06-12 20:51:28.347736
# Unit test for method run of class VaultCLI
def test_VaultCLI_run():
    # Test with --help
    runner = CliRunner()
    result = runner.invoke(main, ['vault', '--help'])
    assert result.exit_code == 0

# Generated at 2022-06-12 20:51:32.975797
# Unit test for method post_process_args of class VaultCLI
def test_VaultCLI_post_process_args():
    '''
    Unit test for method post_process_args of class ansible.cli.VaultCLI
    '''

    # Any initializations go here

    # Run the method under test, passing all required arguments
    test_instance = VaultCLI()
    test_instance.post_process_args()

    # Optionally, you may put some assertions here to verify the results of
    # your module.


# Generated at 2022-06-12 20:51:38.449628
# Unit test for method execute_create of class VaultCLI
def test_VaultCLI_execute_create():
    cli = VaultCLI()
    cli.setup_vault_secrets = Mock(return_value=[('default', 'foo'), ('bar', 'blah')])
    cli.editor = Mock()
    context.CLIARGS = {'args': ['filename'], 'encrypt_vault_id': None}
    cli.execute_create()
    cli.editor.create_file.assert_called_with('filename', 'foo', 'default')



# Generated at 2022-06-12 20:51:39.762102
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    v = VaultCLI()
    v.execute_encrypt()


# Generated at 2022-06-12 20:51:51.418579
# Unit test for method execute_rekey of class VaultCLI
def test_VaultCLI_execute_rekey():
   vault_cli = VaultCLI()
   args = ['args']

# Generated at 2022-06-12 20:51:57.638221
# Unit test for method execute_encrypt of class VaultCLI
def test_VaultCLI_execute_encrypt():
    # test the encrypt CLI command

    vault_text = '''The black prince
He was the fairest of all flowers
On plains of Sheffield he lay
He went to London
With his head held high
And died in the morning
The black prince'''

    vault_file = 'plaintext.vault'

    with open(vault_file, 'w') as f:
        f.write(vault_text)

    results = subprocess.check_output(['ansible-vault', 'encrypt', vault_file],
                                      input='password')

    encrypted_vault_file_name = '%s.%s' % (vault_file, 'vault')
    with open(encrypted_vault_file_name) as f:
        vault_text = f.read()
