

# Generated at 2022-06-12 20:32:49.376109
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:32:49.933782
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:53.845315
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os

    test_playbook_file_path = os.path.join(os.path.dirname(__file__), 'test_playbook.yml')

    args = [test_playbook_file_path]

    cli = PlaybookCLI(args=args)

    cli.parse()

    cli.run()

# Generated at 2022-06-12 20:33:00.809806
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    PlaybookCLI.display = Display()

    test_args = ['ansible-playbook', 'test_playbook.yaml', '--list-hosts']

    # missing connection and fork options (needed for password prompts)
    # this should blow up
    cli = PlaybookCLI(args=test_args)
    cli.parse()
    try:
        cli.run()
        assert False
    except AnsibleError:
        pass

    # missing connection options (needed for password prompts)
    # this should blow up
    test_args.append('--forks=1')
    cli = PlaybookCLI(args=test_args)
    cli.parse()
    try:
        cli.run()
        assert False
    except AnsibleError:
        pass

    # missing fork options (needed for password

# Generated at 2022-06-12 20:33:08.723610
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    playbookcli=PlaybookCLI()

# Generated at 2022-06-12 20:33:10.312809
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:19.721713
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """ Testcase for PlaybookCLI.run

    post_process_args() and run() are tested, according to public method run() of class PlaybookCLI
    """

    # global consts for monkeypatch
    _CONST_ARGS = 'args'
    _CONST_PATHS = 'private_data_dir, callback_whitelist, module_path,' \
                   ' force_handlers, flush_cache, listtags, listtasks, syntax, ' \
                   ' start_at_task, verbosity, step'
    _CONST_PLAYBOOKS = 'playbooks'
    _CONST_PRIVATE_DATA_DIR = 'private_data_dir'
    _CONST_VERBOSITY = 'verbosity'


# Generated at 2022-06-12 20:33:26.006359
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    mock_options = {
        'verbosity': 1,
        'flush_cache': True,
        'listhosts': False,
        'subset': False,
        'syntax': False,
        'listtasks': False,
        'listtags': False,
        'step': False,
        'start_at_task': False,
        'args': []
    }


# Generated at 2022-06-12 20:33:26.757151
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:29.986894
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    uut = PlaybookCLI(["-i", "tests/unittests/inventory/test.ini", "tests/unittests/playbook_tests/ping.yml"])
    uut.parse()
    assert uut.run() == 0

# Generated at 2022-06-12 20:33:41.569643
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    raise AnsibleError('Test not implemented yet')

# Generated at 2022-06-12 20:33:48.646660
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Calling PlaybookCLI.run() with different combinations of arguments
    """

    C.config.initialize_settings()
    context.CLIARGS = {}

    # Calling run() without any arguments
    # Arguments passed:
    #   None
    # Expected result:
    #   exit_without_ignore() should be called once;
    #   Program should be aborted and empty line should be displayed
    pbcli = PlaybookCLI(None)
    pbcli.run()

# Generated at 2022-06-12 20:33:49.262348
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass  # TODO

# Generated at 2022-06-12 20:33:57.020048
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Verify that playbook runs with no playbook filenames given
    assert PlaybookCLI().run() == 3
    assert PlaybookCLI().run(args=[]) == 3

    # Verify that playbook runs when playbook file exists
    # Note not using a real playbook as that causes other side effects
    assert PlaybookCLI().run(args=['/dev/random']) == 3

    # Verify that playbook runs with single file argument
    # Note not using a real playbook as that causes other side effects
    assert PlaybookCLI().run(args=['/dev/random', 'test1']) == 3

    # Verify that playbook runs with multiple file arguments
    # Note not using a real playbook as that causes other side effects
    assert PlaybookCLI().run(args=['/dev/random', 'test1', 'test2']) == 3


# Generated at 2022-06-12 20:34:05.976116
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    import argparse
    from ansible.parsing.dataloader import DataLoader

    # Create a dummy loader and inventory
    loader = DataLoader()
    inventory = None

    # Create a dummy parser and add default arguments
    parser = argparse.ArgumentParser()
    opt_help.add_connect_options(parser)
    opt_help.add_meta_options(parser)
    opt_help.add_runas_options(parser)
    opt_help.add_subset_options(parser)
    opt_help.add_check_options(parser)
    opt_help.add_inventory_options(parser)
    opt_help.add_runtask_options(parser)
    opt_help.add_vault_options(parser)
    opt_help.add_fork_options(parser)

# Generated at 2022-06-12 20:34:15.567554
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Test for method run of class PlaybookCLI"""
    runner_obj = PlaybookCLI()

    # run ansible-playbook --list-hosts command
    args = ['ansible-playbook', '--list-hosts', "invalid.yml"]
    runner_obj.parse()
    runner_obj.options = runner_obj.parser.parse_args(args[1:])
    runner_obj.post_process_args(runner_obj.options)
    runner_obj.run()

    # run ansible-playbook --version command
    args = ['ansible-playbook', '--version']
    runner_obj.parse()
    runner_obj.options = runner_obj.parser.parse_args(args[1:])
    runner_obj.post_process_args(runner_obj.options)
   

# Generated at 2022-06-12 20:34:18.203763
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    sys.argv = ['ansible-playbook']
    cli = PlaybookCLI(args=sys.argv[1:])
    cli.run()

# Generated at 2022-06-12 20:34:20.438327
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI().run()

# Generated at 2022-06-12 20:34:21.097836
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
  pass

# Generated at 2022-06-12 20:34:31.992251
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    play = CLI.play_prereqs(b_playbook_path, b_inventory, b_variable_manager, b_loader, play)

    pbex = PlaybookExecutor(playbooks=[b_playbook_path], inventory=b_inventory,
                            variable_manager=b_variable_manager, loader=b_loader,
                            passwords=b_passwords)

    results = pbex.run()
    for p in results:
        for idx, play in enumerate(p['plays']):
            if play._included_path is not None:
                loader.set_basedir(play._included_path)
            else:
                pb_dir = os.path.realpath(os.path.dirname(p['playbook']))
                loader.set_basedir(pb_dir)

            #

# Generated at 2022-06-12 20:35:04.326995
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    fake_options = ['ansible-playbook', '-i', 'hosts', 'site.yml']
    cli = PlaybookCLI(args=fake_options)
    cli.options = cli.parse()
    cli.post_process_args(cli.options)
    cli.run()

# Generated at 2022-06-12 20:35:13.802942
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    if not os.path.exists("testdata/inventory"):
        os.mkdir("testdata/inventory")
    inv = InventoryManager(loader=DataLoader(), sources=os.path.abspath("testdata/inventory/hosts"))
    vars_manager = VariableManager(loader=DataLoader(), inventory=inv)

    # Set a fake playbook
    context.CLIARGS = {'args': ["testdata/playbook/playbook.yml"]}
    pb = PlaybookCLI()
    assert pb.run() == 0

# Generated at 2022-06-12 20:35:24.314655
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    playbook_cli = PlaybookCLI()
    playbook_dir = os.path.dirname(os.path.dirname(__file__))
    playbook = os.path.join(playbook_dir, 'playbook.yml')

# Generated at 2022-06-12 20:35:24.720324
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:25.125663
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:31.997075
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    Unit test for method run of class PlaybookCLI
    '''
    from datetime import datetime


# Generated at 2022-06-12 20:35:39.868549
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
    from ansible.utils.collection_loader import AnsibleCollectionConfig as ACC
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path, _get_collection_playbook_path
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    pb = PlaybookCLI()
    # set inventory as localhost
    context.CLIARGS['inventory'] = 'localhost,'
    # add playbooks path to list

# Generated at 2022-06-12 20:35:50.636359
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:35:58.373095
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import tempfile
    import sys

    fd, path = tempfile.mkstemp()
    os.write(fd, b"---\n- hosts: all\n  tasks:\n    - name: test play\n      ping:")
    os.close(fd)

    context_obj = context.CLIARGS

    context_obj['module_path'] = None
    context_obj['module_lang'] = 'C'
    context_obj['force_handlers'] = False
    context_obj['flush_cache'] = None
    context_obj['listhosts'] = False
    context_obj['listtags'] = False
    context_obj['listtasks'] = False
    context_obj['syntax'] = False
    context_obj['step'] = False
    context_obj['start_at_task'] = None


# Generated at 2022-06-12 20:35:58.937064
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:10.105501
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    variables = {'inventory_dir': './test/unit/cli/inventory'}

# Generated at 2022-06-12 20:37:12.638174
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    sys.argv = ['./ansible', '--version']
    assert PlaybookCLI().run() == 0

# Generated at 2022-06-12 20:37:13.200474
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:21.776816
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI

    class Bunch:
        def __init__(self, **kwds):
            self.__dict__.update(kwds)

    p = PlaybookCLI(args=['test.yml'])
    p.parser = Bunch()
    p.options = Bunch()
    p.options.listhosts = True
    p.options.listtasks = True
    p.options.listtags = True
    p.options.list_hosts = True
    p.options.list_tasks = True
    p.options.list_tags = True
    # run with these args, it should not crash
    p.run()

# Generated at 2022-06-12 20:37:25.173642
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible_collections.ansible.community.tests.unit.plugins.cli.fixtures.test_playbook_cli import test_PlaybookCLI_run as base_test
    return base_test()

# Generated at 2022-06-12 20:37:25.944424
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:36.137790
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class PlaybookCLI_run_PBE(PlaybookExecutor):
        def __init__(self, playbooks, inventory, variable_manager, loader, passwords):
            super(PlaybookCLI_run_PBE, self).__init__(playbooks=playbooks, inventory=inventory,
                                variable_manager=variable_manager, loader=loader,
                                passwords=passwords)
        def run(self):
            return 0

    class PlaybookCLI_run_CLI(PlaybookCLI):
        def __init__(self):
            super(PlaybookCLI_run_CLI, self).__init__()

        def _play_prereqs(self):
            return [0, 0, 0]

        def _flush_cache(self):
            pass


# Generated at 2022-06-12 20:37:44.775497
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class TestPlaybookCLI(PlaybookCLI):
        def parse(self):
            pass
        def ask_passwords(self):
            return "abc", "abc"
        def _play_prereqs(self):
            return None, None, None
        def _flush_cache(self, inventory, variable_manager):
            pass

    PlaybookCLI.setup = lambda self: None  # To avoid setup

    class TestRunner(object):
        def __init__(self):
            self.processes = []

    TestRunner.run = lambda self, play, inventory, variable_manager, loader, options, passwords=None: []

    class TestInventory(object):
        def list_hosts(self):
            return [1,2,3]
        def get_hosts(self, pattern):
            return pattern


# Generated at 2022-06-12 20:37:46.876383
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    ps = PlaybookCLI()

# Generated at 2022-06-12 20:37:56.983943
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create mock objects
    # pylint: disable=E1101
    mock_inventory = InventoryManager(loader=DataLoader(), sources='')
    mock_variable = VariableManager()

    # Create mock class
    options = {'listtags': False,
               'listtasks': False,
               'syntax': False,
               'inventory': mock_inventory,
               'variable_manager': mock_variable,
               'loader': DataLoader(),
               'passwords': {}}

    expected_result = 0

    #

# Generated at 2022-06-12 20:39:14.183773
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO implement unit test
    assert False

# Generated at 2022-06-12 20:39:22.242764
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class Options:
        version = C.DEFAULT_DEBUG
        verbosity = 0

        listtags = False
        listtasks = False
        syntax = False
        step = False

        subset = None
        inventory = None
        extra_vars = None
        tree = None
        force_handlers = False
        flush_cache = False

        forks = 5
        ask_vault_pass = False
        vault_password_files = None
        new_vault_password_file = None
        output_file = None
        tags = None
        skip_tags = None
        one_line = None
        start_at_task = None
        role_names = None
        skip_roles = None
        check = False
        diff = False
        diff_unified = False
        diff_using = None
        diff_context = False

# Generated at 2022-06-12 20:39:25.648710
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    This tests the PlaybookCLI method. It will return True when the method
    is completed successfully.
    '''
    pass

# Generated at 2022-06-12 20:39:27.168778
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Unit test for method run of class PlaybookCLI
    """
    pass

# Generated at 2022-06-12 20:39:27.690721
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:39.663001
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # testing that PlaybookCLI.run() validates adjacency
    # when playbook is next to collection
    collection_path_simple = '/usr/share/ansible/test_collection_simple'
    b_test_path = os.path.join(collection_path_simple, b'test.yaml')
    collection_name_simple = 'test.collection_simple'
    b_collection_name_simple = collection_name_simple.encode('utf-8')
    args = [b_test_path]
    context.CLIARGS = {'args': args}
    pbex = PlaybookCLI()
    loader = pbex.loader
    # inventory has not been initialized yet
    assert loader.collection_playbooks == {}
    # verify that collection has been found
    pbex.run()
    assert b

# Generated at 2022-06-12 20:39:43.897668
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test with no input
    def test_no_input():
        cli = PlaybookCLI(['test.yml'])
        cli.run()
        assert False

    # Test with input
    def test_with_input():
        cli = PlaybookCLI(['test.yml'])
        cli.run()
        assert False

# Generated at 2022-06-12 20:39:46.380940
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(['playbook.yml'])
    cli.run()

# Generated at 2022-06-12 20:39:56.406801
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    import tempfile
    import os
    import shutil

    # This is what the command line option parser does before calling
    # run.
    args = [
        'ansible-playbook',
        os.path.join('/etc', 'ansible', 'roles', 'a_role', 'meta', 'main.yml'),
    ]

    # Create the option parser and try to parse the command line
    # arguments.
    cli = PlaybookCLI(args)
    options = cli.parse()

    # Create a temporary directory to hold inventory and fact caches
    # for the test.
    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-12 20:39:59.195550
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI([])
    args = ["/path/to/playbook.yml"]
    ret = cli.run(args)
    assert ret == 0