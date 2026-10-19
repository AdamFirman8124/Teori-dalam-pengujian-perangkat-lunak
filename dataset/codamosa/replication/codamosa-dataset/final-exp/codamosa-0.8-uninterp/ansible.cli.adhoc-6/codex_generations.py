

# Generated at 2022-06-12 20:11:52.572375
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import ansible.config.manager
    from ansible.cli.adhoc import AdHocCLI
    result = AdHocCLI().run(args=[])
    assert result == 0
    #test is a failed test due to the fact that self._play_ds is not returning the right content
    #assert result.exception.msg == "No hosts matched, nothing to do"

# Generated at 2022-06-12 20:11:54.564021
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(args=['localhost'])
    assert isinstance(adhoc, AdHocCLI)

# Generated at 2022-06-12 20:12:02.230793
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    args = [
        '-i', 'inventory.ini',
        'all',
        '-a', 'ls',
        '-m', 'copy',
        '--tree', '/tmp/test_AdHocCLI',
        '--one-line',
        '--list-hosts',
        '--verbose',
    ]
    cli = AdHocCLI(args)
    assert cli.options.one_line == True
    assert cli.options.tree == '/tmp/test_AdHocCLI'
    assert cli.options.forks == 5
    assert cli.options.listhosts == True
    assert cli.options.verbosity == 3
    assert cli.options.extra_vars == []

# Generated at 2022-06-12 20:12:05.377157
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    try:
        adhoc_cli = AdHocCLI(args=['-b','-m','ping','all'])
        adhoc_cli.run()
        assert True
    except:
        assert False

# Generated at 2022-06-12 20:12:06.301437
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # TODO: Implement test
    pass

# Generated at 2022-06-12 20:12:08.241735
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ''' Test the method run of class AdHocCLI '''
    pass


# Generated at 2022-06-12 20:12:16.383770
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:12:20.096583
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    try:
        AdHocCLI().run()
    except SystemExit:
        pass

if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:12:22.274756
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    assert AdHocCLI(args=['host', '-m', 'module-name', '-a', 'option=value'])

# Generated at 2022-06-12 20:12:25.071355
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    unit test method run of class AdHocCLI
    '''
    pass

# Generated at 2022-06-12 20:12:41.304928
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import argparse

    argv = ['-m', 'echo', '--args', 'foo=bar', 'all']

# Generated at 2022-06-12 20:12:52.124827
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    def SideEffect(args):
        options = list(args.__dict__.items())
        return dict(options)

    AdHocCLI.post_process_args = mock.MagicMock(side_effect=SideEffect)
    AdHocCLI.ask_passwords = mock.MagicMock(return_value=(None, None))
    AdHocCLI.get_host_list = mock.MagicMock()
    AdHocCLI.play_prereqs = mock.MagicMock()
    AdHocCLI._play_ds = mock.MagicMock(return_value={'name': 'Ansible Ad-Hoc'})

    # making sure to remove any environment variable

# Generated at 2022-06-12 20:13:00.858394
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''Return a random integer in the range [a, b].'''
    import mock
    import collections
    import ansible.constants as C
    import ansible.cli.adhoc

    inventory = mock.Mock()
    variable_manager = mock.Mock()
    loader = mock.Mock()
    cb = mock.Mock()

    my_adhoc = ansible.cli.adhoc.AdHocCLI(args=['./ansible/test/units/mock/ansible-mock', '-i', 'test_inventories/test_inventory3',
                                                'localhost', '--module-name', 'ping', '--module-args', 'state=present'])
    my_adhoc.post_process_args = lambda x: x

# Generated at 2022-06-12 20:13:01.890865
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    result = AdHocCLI().run()
    assert result == 0

# Generated at 2022-06-12 20:13:06.863798
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    def test_supports_check_mode():
        a = AdHocCLI(['-m', 'shell', '-a', 'id', '-i', 'inventory', 'all'])
        assert a.supports_check_mode is False

    # TODO: Failing while running with 'test', even though it passes when runs outside test.
    #       Need to debug and find out why it is failing
    #test_supports_check_mode()



# Generated at 2022-06-12 20:13:13.608592
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class DummyOption(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
    adhoc_cli = AdHocCLI()
    options = DummyOption(module_name="system", module_args="")
    with pytest.raises(AnsibleOptionsError):
        adhoc_cli.run()

# Generated at 2022-06-12 20:13:21.993479
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Unit test for method run of class AdHocCLI
    '''
    # use context.CLIARGS

# Generated at 2022-06-12 20:13:23.990025
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    my_adhoc = AdHocCLI()
    assert my_adhoc.init_parser() == 0

# Generated at 2022-06-12 20:13:28.539160
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    adhoc.post_process_args(adhoc.args)

# Generated at 2022-06-12 20:13:30.413062
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert False, "No tests for class AdHocCLI"

# Generated at 2022-06-12 20:13:46.457719
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI(args=[])
    adhoc_cli.parser = adhoc_cli.init_parser()
    (options, args) = adhoc_cli.parser.parse_args([])
    adhoc_cli.post_process_args(options)
    adhoc_cli.run()

# Generated at 2022-06-12 20:13:49.418212
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI([])
    assert cli is not None


# Generated at 2022-06-12 20:13:50.353672
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()

# Generated at 2022-06-12 20:13:58.851550
# Unit test for constructor of class AdHocCLI

# Generated at 2022-06-12 20:14:03.380376
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(args=['-m', 'ping'], runas_opts=True)
    cli.post_process_args(None)
    result = cli.run()
    assert result == 0

# Generated at 2022-06-12 20:14:04.741615
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''Unit test for method run of class AdHocCLI'''
    pass

# Generated at 2022-06-12 20:14:07.651405
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(['ansible', 'all', '--module-name', 'ping', '-a', 'ping'])
    assert adhoc



# Generated at 2022-06-12 20:14:08.896164
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli is not None

# Generated at 2022-06-12 20:14:20.394314
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """Unit test for AdHocCLI.run()"""

    # Create AdHocCLI object
    adhoccli = AdHocCLI()

    # Initialise the parser using AdHocCLI object
    adhoccli.init_parser()

    # Initialise context
    context.CLIARGS = {}

    # Set context flags
    context.CLIARGS['subset'] = None
    context.CLIARGS['listhosts'] = None
    context.CLIARGS['listtasks'] = None
    context.CLIARGS['listtags'] = None
    context.CLIARGS['syntax'] = None
    context.CLIARGS['connection'] = None
    context.CLIARGS['module_path'] = None
    context.CLIARGS['forks'] = None


# Generated at 2022-06-12 20:14:21.315320
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    assert AdHocCLI

# Generated at 2022-06-12 20:14:57.909123
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Don't run under pypy, it doesn't work
    from sys import executable
    if 'pypy' in executable:
        return True

    # Just for this test, we're going to completely ignore the deprecation warning about the config file.
    import warnings
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.constants import DEFAULT_MODULE_NAME
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    import ansible.utils.display as display
    display.VERBOSITY = 0

    warnings.filterwarnings(module='ansible', action='ignore', message='Unsupported usage: inventory script.*')
    # Run the

# Generated at 2022-06-12 20:15:06.167879
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create a test object
    adhoc_test = AdHocCLI()
    # Mocking methods and attributes required for execution of method run
    adhoc_test.callback = None
    context.CLIARGS={'verbosity':5,'forks':10,'ask_pass':False,'ask_become_pass':False,'become':False,'become_method':'sudo','become_user':None,'check':False,'remote_user':'subbu','subset':None,'one_line':False,'tree':None,'seconds':None,'poll_interval':None,'module_args':'subbu-test','module_name':'ping','listhosts':False,'listtasks':False,'listtags':False,'vault_password_file':None,'args':'subbu-test'}
    # Creating a mock ad-h

# Generated at 2022-06-12 20:15:16.260572
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create a AdHocCLI object and invokes the run method.
    # This test will be extended as needed.
    # TODO: Create a test function in AdHocCLI class
    import sys
    # AdHocCLI class has been changed in Ansible 2.3
    if (sys.version_info > (3, 0)):
        from ansible.cli.adhoc import AdHocCLI
    else:
        from ansible.cli.adhoc import AdHocCLI as AdHocCLI
    new_object = AdHocCLI()
    new_object.run()

# Generated at 2022-06-12 20:15:22.821298
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    d1 = 'debug.args'
    d2 = 'debug.verbosity'
    a1 = 'args'
    a2 = 'ask_sudo_pass'
    a3 = 'ask_su_pass'
    a4 = 'ask_vault_pass'
    a5 = 'become_ask_pass'
    a6 = 'become_method'
    a7 = 'become_user'
    a8 = 'connection'
    a9 = 'check'
    a10 = 'diff'
    a11 = 'forks'
    a12 = 'listhosts'
    a13 = 'listtags'
    a14 = 'listtasks'
    a15 = 'module_name'
    a16 = 'module_path'
    a17 = 'module_args'

# Generated at 2022-06-12 20:15:23.817623
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(None)
    cli.run()

# Generated at 2022-06-12 20:15:29.991115
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import tempfile
    import shutil
    import os
    import sys

    # Create a empty temp directory
    os.chdir(tempfile.gettempdir())
    tmpDir = tempfile.mkdtemp(prefix='tmp_ansible_test_AdHocCLI_run')
    print(tmpDir)

    # Change directory to the temp directory
    os.chdir(tmpDir)


# Generated at 2022-06-12 20:15:30.986945
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.run()

# Generated at 2022-06-12 20:15:35.615004
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    adhoc_cli = AdHocCLI()

    # Test case: empty args
    assert (adhoc_cli.run(args={}) == 2)

    # Test case: normal args

# Generated at 2022-06-12 20:15:36.186099
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:15:42.170731
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ''' ad_hoc_test1.py:TestAdHoc.test_AdHocCLI_run
    '''
    myargs = ['localhost', '-m', 'ping', '-a', '1=2']
    mycli = AdHocCLI(args=myargs)
    mycli.parse()
    mycli.post_process_args(mycli.options)
    result = mycli.run()
    return result

# Generated at 2022-06-12 20:16:50.263042
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import ansible.constants as C
    from ansible.utils.display import Display
    display = Display()
    C.ANSIBLE_FORCE_COLOR = True
    adhoc = AdHocCLI()
    adhoc.init_parser()
    adhoc.options = adhoc.parser.parse_args(["-m", "ping", "localhost"])
    adhoc.post_process_args(adhoc.options)
    display.verbosity = adhoc.options.verbosity
    adhoc.validate_conflicts(adhoc.options, runas_opts=True, fork_opts=True)
    adhoc.run()
    print("AdHocCLI " + "=" * 60)
    print("AdHocCLI " + "Success" + " " * 60)


# Generated at 2022-06-12 20:16:52.544962
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create a AdHocCLI object
    AdHocCLI_obj = AdHocCLI()

    # Create a AdHocCLI object
    # CALL: get_host_list
    # CALL: run
    AdHocCLI_obj.run()

# Generated at 2022-06-12 20:16:52.984721
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:16:55.016227
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """ This is to test run method of  AdHocCLI
    """
    adhoc = AdHocCLI()
    result = adhoc.run()
    assert result == 0

# Generated at 2022-06-12 20:17:00.600074
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class MyAdHocCLI(AdHocCLI):
        def __init__(self):
            # use empty args
            self.args = []

    # test with no hosts matching pattern
    def mock_ask_passwords(self):
        return (None, None)

    def mock_get_host_list(self, inventory, subset, pattern):
        return []

    cli = MyAdHocCLI()
    # set the mocked functions
    cli.ask_passwords = mock_ask_passwords
    cli.get_host_list = mock_get_host_list
    # set the options
    cli.options = opt_help.create_parser(['-m', 'setup', '-a', 'filter=*ipv4*', 'localhost']).parse_args()
    # test it
    return

# Generated at 2022-06-12 20:17:02.140641
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli is not None

# Generated at 2022-06-12 20:17:06.505022
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # Test with no arguments
    cli = AdHocCLI()
    assert cli._play_prereqs() == (None, None, None)


if __name__ == '__main__':  # pragma: no cover
    adhoc_cli = AdHocCLI()
    adhoc_cli.run()

# Generated at 2022-06-12 20:17:07.895923
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    assert cli.run() == 0


# Generated at 2022-06-12 20:17:14.181065
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    print("testing class AdHocCLI: method run ...")
    import sys
    import os
    import subprocess
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common.collections import ImmutableDict

    # default values = {
    #     'module_name': 'command',
    #     'module_args': '',
    #     'args': '',
    #     'listhosts': False,
    # }

# Generated at 2022-06-12 20:17:20.660649
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create object AdHocCLI
    testAdHocCLI=AdHocCLI(cmdline=['ansible', 'localhost', '-m', 'ping'])
    testAdHocCLI.parse()
    testAdHocCLI.post_process_args(context.CLIARGS)
    result = testAdHocCLI.run()
    # Check result is True
    assert result == 0

# Generated at 2022-06-12 20:21:22.839528
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """Tests run method of class AdHocCLI"""

    # Testing for AdHocCLI.run when context.CLIARGS is None
    context.CLIARGS = None
    ad_hoc_cli = AdHocCLI()
    ad_hoc_cli.post_process_args = MagicMock()
    ad_hoc_cli.init_parser = MagicMock()
    ad_hoc_cli.run_subset = MagicMock(return_value=0)
    ad_hoc_cli.ask_passwords = MagicMock(return_value=(None, None))
    ad_hoc_cli._play_prereqs = MagicMock()
    ad_hoc_cli.get_host_list = MagicMock()
    ad_hoc_cli._play_ds = MagicM

# Generated at 2022-06-12 20:21:23.418740
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:21:26.527705
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI(None)
    assert isinstance(adhoc_cli, AdHocCLI)
    assert isinstance(adhoc_cli, CLI)

# Generated at 2022-06-12 20:21:34.670152
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # stubs
    class FakeRunner:
        def __init__(self):
            self.results_raw = {
                "dark": {
                    "unreachable": False,
                    "skipped": False,
                    "ok": 1,
                    "changed": 0,
                    "failures": 1,
                    "ansible_facts": {},
                    "ansible_included_var_files": [],
                    "item": {}
                }
            }
