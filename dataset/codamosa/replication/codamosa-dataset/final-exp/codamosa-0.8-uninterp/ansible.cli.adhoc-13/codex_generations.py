

# Generated at 2022-06-12 20:12:05.378138
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # Test without '-m BASE_MODULE_NAME_HERE'
    context.CLIARGS = dict(module_name='', module_args='', host_pattern=['myhost'])

    adhoc_cli = AdHocCLI()
    adhoc_cli.init_parser()

    parser = adhoc_cli.parser
    parser_options = adhoc_cli.parser._actions[2:]
    assert parser_options[0].dest == 'module_name'
    assert parser_options[0].default == 'command'

    # Test with '-m BASE_MODULE_NAME_HERE'
    context.CLIARGS = dict(module_name='setup', module_args='', host_pattern=['myhost'])

    adhoc_cli = AdHocCLI()
    adh

# Generated at 2022-06-12 20:12:06.558561
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI(['-m', '', '127.0.0.1'])
    assert cli
    assert cli.parser

# Generated at 2022-06-12 20:12:15.373244
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class MockCLIArgs(object):
        def __init__(self):
            self.args = 'test'
            self.module_name = 'ping'
            self.become = False
            self.verbosity = 2
            self.listhosts = False
            self.listtasks = False
            self.listtags = False
            self.connection = 'smart'
            self.timeout = 10
            self.tree = None
            self.ssh_common_args = ''
            self.ssh_extra_args = ''
            self.sftp_extra_args = ''
            self.scp_extra_args = ''
            self.b_ssh_extra_args = ''
            self.b_sftp_extra_args = ''
            self.b_scp_extra_args = ''

# Generated at 2022-06-12 20:12:20.618951
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import os
    import sys
    import StringIO
    import unittest

    from units.mock.loader import DictDataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    display = Display()
    display.verbosity = 1
    display.columns = 132

    sys.stdout = StringIO.StringIO()
    sys.stderr = StringIO.StringIO()

    class TestPbCLI(unittest.TestCase):

        @unittest.skipUnless(sys.version_info >= (2, 7), "requires python2.7 or greater")
        def test_simple_run(self):
            '''
            Test a simple run
            '''

# Generated at 2022-06-12 20:12:23.098069
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''Unit test for method run of class AdHocCLI'''

    adhoc_cli = AdHocCLI()
    adhoc_cli.run()

# Generated at 2022-06-12 20:12:27.155226
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # create and execute the single task playbook which returns the exit code
    test_AdHocCLI = AdHocCLI()

    # post process and validate options for bin/ansible
    test_AdHocCLI.post_process_args()

    assert test_AdHocCLI.run() == 0

# Generated at 2022-06-12 20:12:33.869904
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI(
        args=['webservers'],
        module_name='shell',
        module_args=None,
        check=False,
        inventory='/etc/ansible/hosts',
        verbosity=3
    )

    assert adhoc_cli.positional_args_count == 1
    assert adhoc_cli.positional_args_pattern == 'webservers'
    assert adhoc_cli.module_name == 'shell'
    assert adhoc_cli.module_args is None
    assert adhoc_cli.check is False
    assert adhoc_cli.inventory == '/etc/ansible/hosts'
    assert adhoc_cli.verbosity == 3



# Generated at 2022-06-12 20:12:34.856418
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.run()

# Generated at 2022-06-12 20:12:36.952107
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    adhoc = AdHocCLI()
    assert isinstance(adhoc.parser, CLI.parser)

# Generated at 2022-06-12 20:12:41.350679
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # A valid constructor
    a = AdHocCLI()

    # No hosts are matching
    a.post_process_args(dict(args='nonexistant'))
    a.run()


# Generated at 2022-06-12 20:12:57.945880
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    Test run method of class AdHocCLI
    """
    cli_args = ['-a', 'arg1=val1 arg2=val2', '-m', 'ping', 'localhost']
    cli = AdHocCLI(args=cli_args)
    cli.run()
    assert cli.CLEANUP_CALLBACKS['on_start'] == cli._cleanup_on_start
    assert cli.CLEANUP_CALLBACKS['on_async_ok'] == cli._cleanup_on_async_ok
    assert cli.CLEANUP_CALLBACKS['on_async_failed'] == cli._cleanup_on_async_failed

# Generated at 2022-06-12 20:13:04.851579
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' adhoc_cli = AdHocCLI(args)

    Creates and returns an instance of AdHocCLI.
    '''

    adhoc_cli = AdHocCLI(['-m', 'ping', '-a', 'data=abcde', 'localhost'])
    assert adhoc_cli.parser.description == "Define and run a single task 'playbook' against a set of hosts"
    assert adhoc_cli.parser.usage == "%prog <host-pattern> [options]"
    assert adhoc_cli.parser.epilog == "Some actions do not make sense in Ad-Hoc (include, meta, etc)"
    assert adhoc_cli.parser._option_string_actions['-m'].help == "Name of the action to execute (default=ping)"
    assert ad

# Generated at 2022-06-12 20:13:11.003151
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # Enable automatic module path discovery
    C.DEFAULT_MODULE_PATH = ["fake_modules"]

    ad_hoc = AdHocCLI([])
    assert ad_hoc is not None

# Generated at 2022-06-12 20:13:14.706200
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    args = ['ansible', 'all', '-i', 'localhost,', '-m', 'setup']
    display = Display()
    adhoc = AdHocCLI(args, display)
    adhoc.options, adhoc.args = adhoc.parser.parse_args(args)
    adhoc.post_process_args(adhoc.options)
    adhoc.run()

# Generated at 2022-06-12 20:13:16.817502
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ''' Unit test for method run of class AdHocCLI '''

    # TODO: The test method has to be implemented
    pass

# Generated at 2022-06-12 20:13:26.450032
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.module_utils.basic import AnsibleModule

    class Display:
        pass

    class MockPlay:
        def __repr__(self):
            return 'MockPlay'

        def serialize(self):
            return dict(hosts='hostpattern', gather_facts='no', tasks='tasklist')

    class MockPlaybook:
        def __repr__(self):
            return 'MockPlaybook'

        def __init__(self, entries):
            self._entries = entries

        def __getattr__(self, name):
            return self._entries

        def _get_entries(self):
            pass

        def _set_entries(self):
            pass

        entries = property(_get_entries, _set_entries)


# Generated at 2022-06-12 20:13:27.097202
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()

# Generated at 2022-06-12 20:13:38.085301
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:13:41.427440
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()

    setattr(cli, 'post_process_args', lambda x : x)

    cli.options = {'module_name': 'shell', 'module_args': 'ls -l'}

    cli.run()

# Generated at 2022-06-12 20:13:44.293244
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO
    # Need to mock the class ModuleLoader
    # Need to mock the class VariableManager
    adhoc_cli = AdHocCLI()
    adhoc_cli.init_parser()
    adhoc_cli.run()

# Generated at 2022-06-12 20:14:05.748884
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert adhoc is not None

# Generated at 2022-06-12 20:14:08.156863
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI(args=['localhost', '-v'])
    assert type(cli) == AdHocCLI


# Generated at 2022-06-12 20:14:14.965949
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    mock_inventory = 'sample_inventory_file.yml'
    mock_args = 'sample_arguments_file.yml'

# Generated at 2022-06-12 20:14:17.383285
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI([])


if __name__ == '__main__':
    test_AdHocCLI()

# Generated at 2022-06-12 20:14:19.100592
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI()

# Generated at 2022-06-12 20:14:21.487788
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    args = ['-i', 'localhost,', '-m', 'ping', 'localhost']
    cmd = AdHocCLI(args)
    assert cmd.run() == 0

# Generated at 2022-06-12 20:14:23.773828
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli
    assert cli._tqm is None
    assert cli.parser
    assert cli.args is None

# Generated at 2022-06-12 20:14:34.201876
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import connection_loader

    dl = DataLoader()
    inv_data = """
        localhost ansible_connection=local
        foo ansible_connection=local
        """

    vars_data = {}

    options = opt_help.add_ssh_args(optparse.OptionParser())
    options.connection = 'local'
    options.module_name = 'echo'
    options.module_args = 'foo'
    options.listhosts = 'True'
    options.subset = 'all'
    options.pattern = 'all'
    options.one_line

# Generated at 2022-06-12 20:14:34.823037
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:14:36.806380
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ad_hoc = AdHocCLI(args=[])
    assert isinstance(ad_hoc, AdHocCLI)

# Generated at 2022-06-12 20:15:29.356063
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Unit test for method run of class AdHocCLI when all tests are passed
    context.CLIARGS = {'module_name': 'shell', 'module_args': 'ls', 'args': 'ansible-2.8'}
    adhoccli = AdHocCLI()
    adhoccli.post_process_args(context.CLIARGS)
    assert adhoccli.run() == 0
    context.CLIARGS = {'module_name': 'shell', 'module_args': 'ls', 'args': 'ansible-2.9'}
    adhoccli = AdHocCLI()
    adhoccli.post_process_args(context.CLIARGS)
    assert adhoccli.run() == 0

# Generated at 2022-06-12 20:15:30.896719
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:15:42.340433
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' constructor for class AdHocCLI '''
    adhoc_cli = AdHocCLI(
        ['pattern'], 'bin/ansible',
        '%prog [pattern] [options]', 'Define and run a single task "playbook" against a set of hosts',
        'Some actions do not make sense in Ad-Hoc (include, meta, etc)'
    )


if __name__ == '__main__':
    adhoc_cli = AdHocCLI(
        ['pattern'], 'bin/ansible',
        '%prog [pattern] [options]', 'Define and run a single task "playbook" against a set of hosts',
        'Some actions do not make sense in Ad-Hoc (include, meta, etc)'
    )
    test_AdHocCLI()

# Generated at 2022-06-12 20:15:45.260533
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    a = AdHocCLI()
    a.run()
    return "Unit test for method run of class AdHocCLI passed."

# Generated at 2022-06-12 20:15:54.175199
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test with empty CLI args
    options = {}
    adhoc_cli = AdHocCLI(args=[])
    assert (adhoc_cli.run() == 0)

    # Test with CLI args

# Generated at 2022-06-12 20:15:57.547299
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert False, "\nRun this test with `python -m pytest -rs tests/test_module_utils/test_ansible_module_utils_cli.py` to get test results"

if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:16:01.856348
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    args = [
        'localhost',
        '-c', 'local',
        '--module-name', 'ping',
    ]
    cli = AdHocCLI(args)
    parser = cli.create_parser()
    cli.parse(parser, args)
    cli.post_process_args(context.CLIARGS)
    cli.run()

if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:16:07.891350
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create instance of AdHocCLI and test method run
    # Add your own testcases

    # Construct command args
    sys_argv = ['ansible', '-m', 'setup', 'host1', 'host2']
    # Substitute original argument parser with one returning our args
    adhoc_cli = AdHocCLI(args=sys_argv)
    # Call method
    adhoc_cli.run()

# Generated at 2022-06-12 20:16:08.793094
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI().run()

# Generated at 2022-06-12 20:16:11.684071
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Calling run method
    adhocObj = AdHocCLI(["--hosts","hostPattern"])
    adhocObj.run()
    #No assertion for now


# Generated at 2022-06-12 20:17:50.175606
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ''' test module run '''

    class FakeCLI():

        def __init__(self):
            pass

        def run(self):
            self.done = True

        def post_process_args(self, options):
            return options


    fake_cli = FakeCLI()

    ahc = AdHocCLI(fake_cli)

    class FakeOptions():
        pass

    options = FakeOptions()
    options.ask_pass = False
    options.module_name = 'setup'
    options.module_args = ''
    options.args = 'test-host'

    ahc.post_process_args(options)

    ahc.run()

    assert fake_cli.done

# Generated at 2022-06-12 20:17:51.096334
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    my_adhoc = AdHocCLI()

# Generated at 2022-06-12 20:17:52.240213
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:17:56.323057
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    context.CLIARGS = dict(forks=10,  module_name='ping', module_args='', subset='test', seconds=10,
                           poll_interval=10, listhosts=False, verbosity=1)
    context.CLIARGS = Bunch(context.CLIARGS)
    context.CLIARGS.args = 'test'
    adhoc = AdHocCLI()
    adhoc.run()

# Generated at 2022-06-12 20:17:58.500852
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert isinstance(adhoc._parser, object)


# Generated at 2022-06-12 20:18:06.830700
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # It should fail without required option module_name
    try:
        os.environ['ANSIBLE_RETRY_FILES_ENABLED'] = '0'
        options = ad_helpers.get_options(['command', '-i', 'hosts', 'host1', 'host2'])
        cli = AdHocCLI(args=[], options=options)
        cli.run()
    except Exception as e:
        assert e.args[0] == 'No action detected in task. This often indicates a misspelled module name, or incorrect module path.'

    # It should fail without required option module_args

# Generated at 2022-06-12 20:18:07.826987
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ad = AdHocCLI()
    ad.run()

# Generated at 2022-06-12 20:18:09.153526
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:18:18.235356
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from io import StringIO
    import sys
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 0
    # Get a string format of the object
    def object_to_string(obj):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        print(obj)
        sys.stdout = old_stdout
        result_string = result.getvalue()
        return result_string
    # Test run
    AdHocCLI = AdHocCLI()
    options = None
    AdHocCLI.run(options=options)

# Generated at 2022-06-12 20:18:25.663931
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    command = '''echo "Hello World"'''
    options = {'module_name': 'shell'}
    pattern = 'localhost'

    _, inventory, variable_manager = AdHocCLI()._play_prereqs()
    play_ds = AdHocCLI()._play_ds(pattern, async_val=options['seconds'], poll=options['poll_interval'])
    play = Play().load(play_ds, variable_manager=variable_manager)
    playbook = Playbook(variable_manager)
    playbook._entries.append(play)
    playbook._file_name = '__adhoc_playbook__'
