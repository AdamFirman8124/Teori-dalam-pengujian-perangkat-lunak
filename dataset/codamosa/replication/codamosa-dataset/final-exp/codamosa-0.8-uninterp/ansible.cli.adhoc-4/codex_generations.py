

# Generated at 2022-06-12 20:11:58.284727
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from units.mock.loader import DictDataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Set options for AdHocCLI
    test_adhoc_options = {
        'module_name': 'ping',
        'module_args': '',
        'inventory': './tests/units/inventory',
        'forks': 1,
        'one_line': False,
        'tree': None,
        'ask_vault_pass': False,
        'ask_pass': False,
        'ask_sudo_pass': False,
        'verbosity': 1,
        'ask_su_pass': False,
        'diff': False,
    }

    # Create AdHocCLI
    test_adhoc_cmd = AdHocCLI

# Generated at 2022-06-12 20:12:03.787392
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Deprecated warning for inventory in context.CLIARGS
    # Reset context.CLIARGS to avoid a crash (issue #31480)
    import ansible.context
    ansible.context.CLIARGS = ansible.context.CLIARGS._replace(inventory=None)
    adhoc_obj = AdHocCLI()
    adhoc_obj.run()

# Generated at 2022-06-12 20:12:06.388283
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    if adhoc_cli.parser.description is not None:
        assert True
    else:
        assert False


# Generated at 2022-06-12 20:12:11.801570
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    try:
        adhoc_cli = AdHocCLI(['tmp_dummy_arg', 'tmp/dummy_path'])
        # FIXME
        assert False
    except SystemExit as e:
        assert 0 == e.code
    except Exception as e:
        # TODO: This need to be checked with real error message.
        assert str(e) == 'Connection to host=None timed out: connect() failed (110: Connection timed out)'

# Generated at 2022-06-12 20:12:16.749132
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    # Constructor
    cli = AdHocCLI(['--module-name', 'ping'])

    # init_parser()
    cli.init_parser()

    # post_process_args()
    cli.post_process_args(cli.args)

    # run()

    # class __init__()
    cli.AdHocCLI()

if __name__ == '__main__':
    test_AdHocCLI()

# Generated at 2022-06-12 20:12:19.624558
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert adhoc_cli is not None


# Generated at 2022-06-12 20:12:30.265942
# Unit test for method post_process_args of class AdHocCLI
def test_AdHocCLI_post_process_args():
    import ansible.constants as constants
    import ansible.errors as errors
    import ansible.utils.display as display

    class MockedDisplay(display.Display):
        def __init__(self):
            pass

        def verbosity(self):
            pass

    class MockedError(errors.AnsibleError):
        def __init__(self):
            pass

    class MockedVaultPasswordFile(constants.VaultPasswordFile):
        def __init__(self):
            pass

    class MockedCLIArgs(object):
        def __init__(self):
            pass

    display = MockedDisplay()
    constants.VaultPasswordFile = MockedVaultPasswordFile
    errors.AnsibleError = MockedError

    # set the options pre-set
    options = MockedCLIArgs()
    options

# Generated at 2022-06-12 20:12:32.191472
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adHocCLI = AdHocCLI()
    assert adHocCLI is not None

# Generated at 2022-06-12 20:12:33.712402
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI(args=['localhost', '-m', 'shell', '-a', 'echo "hello"'])
    assert adhoc.run() == 0

# Generated at 2022-06-12 20:12:42.791220
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager


# Generated at 2022-06-12 20:12:57.015901
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ar = {'module_name': 'command', 'module_args': 'ls -l /tmp'}
    cli = AdHocCLI(args=ar)
    cli.run()

# Generated at 2022-06-12 20:12:58.287624
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI(['-h'])

# Generated at 2022-06-12 20:12:59.717141
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert AdHocCLI().run() == 0

# Generated at 2022-06-12 20:13:03.455303
# Unit test for method post_process_args of class AdHocCLI
def test_AdHocCLI_post_process_args():
    if C.ANSIBLE_FORCE_COLOR:
        assert C.ANSIBLE_NOCOLOR is not True
        assert C.ANSIBLE_NOCOLOR is False
    else:
        assert C.ANSIBLE_NOCOLOR is not False
        assert C.ANSIBLE_NOCOLOR is True

# Generated at 2022-06-12 20:13:04.697970
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    c = AdHocCLI()
    c.run()

# Generated at 2022-06-12 20:13:15.555497
# Unit test for method post_process_args of class AdHocCLI
def test_AdHocCLI_post_process_args():
    import sys

    # Test case when forks option is specified
    sys.argv = ["ansible-playbook", "-f", "5", "sample_playbook.yml"]
    adhoc_cli = AdHocCLI()
    adhoc_cli.parse()
    # post_process_args() method calls validate_conflicts()
    # which raises AnsibleOptionsError exception if multiple
    # mutually exclusive arguments are specified
    assert adhoc_cli.post_process_args(adhoc_cli.options)

    # Test case when forks option is not specified
    sys.argv = ["ansible-playbook", "sample_playbook.yml"]
    adhoc_cli = AdHocCLI()
    adhoc_cli.parse()
    # post_process_args() method calls validate_conflicts()


# Generated at 2022-06-12 20:13:16.308070
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:13:18.978821
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # Test basic construction
    ad_hoc = AdHocCLI()
    assert ad_hoc is not None

    # Check CLI member is initialized correctly
    assert ad_hoc.cli is not None

# Generated at 2022-06-12 20:13:22.378611
# Unit test for method post_process_args of class AdHocCLI
def test_AdHocCLI_post_process_args():
    args = ['-f', '20', '-u', 'remote-user', '--ask-pass', 'remote-host']
    namespace = AdHocCLI(args=args).parse()

    assert namespace.forks == 20
    assert namespace.ask_pass
    assert namespace.remote_user == 'remote-user'
    assert namespace.inventory == []

# Generated at 2022-06-12 20:13:23.439555
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO: add some unit tests for AdHocCLI class
    pass

# Generated at 2022-06-12 20:14:06.557935
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    dict_of_options = dict()
    dict_of_options['module_name'] = 'ping'
    dict_of_options['module_args'] = 'data=running unit test'
    dict_of_options['ask_pass'] = False
    dict_of_options['ask_become_pass'] = False
    dict_of_options['ask_sudo_pass'] = False
    dict_of_options['verbosity'] = 3
    dict_of_options['listhosts'] = False
    dict_of_options['pattern'] = 'all'
    dict_of_options['one_line'] = False
    dict_of_options['forks'] = 5
    dict_of_options['seconds'] = 0
    dict_of_options['poll_interval'] = 15
    dict_of_options['tree'] = None

# Generated at 2022-06-12 20:14:14.195590
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    adhoc_cli = AdHocCLI(['test_pattern'])

# Generated at 2022-06-12 20:14:17.823116
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhocobj = AdHocCLI(['ansible', 'all', '--list-hosts'])
    adhocobj.parse()

if __name__ == "__main__":
    test_AdHocCLI()

# Generated at 2022-06-12 20:14:18.657044
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI([])
    assert cli

# Generated at 2022-06-12 20:14:19.982375
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    module = AdHocCLI()
    module.run()

# Generated at 2022-06-12 20:14:27.156533
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # noinspection PyProtectedMember
    a = AdHocCLI()
    # noinspection PyProtectedMember
    assert a._play_ds("pattern", 1234, 1) == {'hosts': 'pattern', 'gather_facts': 'no',
                                            'tasks': [{'action': {'module': 'command',
                                                          'args': {'_raw_params': '*',
                                                                   '_uses_shell': False,
                                                                   'argv': ''}},
                                                       'async_val': 1234,
                                                       'poll': 1,
                                                       'timeout': None}],
                                            'name': 'Ansible Ad-Hoc'}

# Generated at 2022-06-12 20:14:28.510388
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli.parser


# Generated at 2022-06-12 20:14:33.900927
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    # test init_parser
    adhoc.init_parser()
    assert type(adhoc.parser.prog).__name__ == 'str'
    assert type(adhoc.parser.usage).__name__ == 'str'
    assert type(adhoc.parser.description).__name__ == 'str'
    assert type(adhoc.parser.epilog).__name__ == 'str'

# Generated at 2022-06-12 20:14:39.081583
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    my_adhoc = AdHocCLI()
    try:
        my_adhoc.init_parser()
        options, args = my_adhoc.parser.parse_args()
        my_adhoc.post_process_args(options)
        my_adhoc.run()
        assert my_adhoc
    except Exception as e:
        print(e)

if __name__ == '__main__':
    test_AdHocCLI()

# Generated at 2022-06-12 20:14:50.362346
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adHocCLI = AdHocCLI()

    # Expected pattern
    pattern = 'test_pattern'

    # Expected return code
    return_code = 0

    # Mock modules
    class Mock_get_host_list:
        def __init__(self, inventory):
            self.inventory = inventory

        def __call__(self, subset):
            return self.inventory, pattern, subset

    class Mock_ask_passwords:
        def __call__(self):
            return 'sshpass', 'becomepass'

    class Mock_self:
        def __init__(self, inventory):
            self.inventory = inventory

        def _play_prereqs(self):
            return 'loader', self.inventory, 'variable_manager'


# Generated at 2022-06-12 20:15:28.251208
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.run()

# Generated at 2022-06-12 20:15:28.843538
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO: Create unit test
    pass

# Generated at 2022-06-12 20:15:32.621378
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI(['-i', 'localhost,', '-m', 'shell', '-a', 'ls', 'local'])
    adhoc.run()

# Generated at 2022-06-12 20:15:34.313633
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    acli = AdHocCLI()

# Generated at 2022-06-12 20:15:34.928927
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:15:36.687191
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert adhoc_cli.parser is not None
    assert adhoc_cli.run() == 0

# Generated at 2022-06-12 20:15:39.767992
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' unit test for constructor of class AdHocCLI'''
    a = AdHocCLI(['host1', 'host2', 'host3'])
    assert a

# Generated at 2022-06-12 20:15:40.373125
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:15:47.694857
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
        Function to test run() method of class AdHocCLI
    """

# Generated at 2022-06-12 20:15:49.017505
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoccli = AdHocCLI()
    assert adhoccli is not None

# Generated at 2022-06-12 20:17:21.248277
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # test AdHocCLI.run(), we use some of the other methods so that we can call run() with a reasonable
    # set of parameters

    # mock stdin
    class MockStdin(object):
        def __init__(self):
            self.input = ''

        def read(self):
            return self.input
    # end of class MockStdin

    # mock stdout
    class MockStdout(object):
        def __init__(self):
            self.output = ''

        def write(self, string):
            self.output += string
    # end of class MockStdout

    # mock stderr
    class MockStderr(object):
        def __init__(self):
            self.output = ''

        def write(self, string):
            self.output += string
    # end of

# Generated at 2022-06-12 20:17:24.051273
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI([])
    assert adhoc_cli._VERSION == "2.6.0"
    assert adhoc_cli._display_version == "ansible-2.6.0"

# Generated at 2022-06-12 20:17:34.125422
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:17:43.094578
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import __main__
    from ansible.release import __version__
    from ansible.utils.display import Display
    from ansible.utils.sentinel import Sentinel
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.vars import combine_vars
    from ansible.vars import load_extra_vars
    from ansible.vars import load_options_vars
    import ansible.cli.adhoc
    import ansible.constants
    import ansible.errors
    import ansible.release
    import ansible.utils.display
    import ansible.utils.sentinel
    import ansible.utils.vars
    import ansible.v

# Generated at 2022-06-12 20:17:45.681291
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    cli.parse()

# Generated at 2022-06-12 20:17:50.450808
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ad_hoc_cli = AdHocCLI()
    ad_hoc_cli.init_parser()
    options, args = ad_hoc_cli.parser.parse_args([])
    ad_hoc_cli.options = options

    # Run will fail as it is not possible to test CLI in isolation
    assert ad_hoc_cli.run() == 1

# Generated at 2022-06-12 20:17:52.304333
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(args=[])
    cli.post_process_args(args=[])
    cli.run()

# Generated at 2022-06-12 20:17:54.911275
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # set up basic objects
    args = []
    parser = CLI.base_parser(args)
    cli = AdHocCLI(parser)
    assert isinstance(cli,AdHocCLI), "Failed to create AdHocCLI object"

# Generated at 2022-06-12 20:17:55.978218
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()

# Generated at 2022-06-12 20:17:57.222240
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass
