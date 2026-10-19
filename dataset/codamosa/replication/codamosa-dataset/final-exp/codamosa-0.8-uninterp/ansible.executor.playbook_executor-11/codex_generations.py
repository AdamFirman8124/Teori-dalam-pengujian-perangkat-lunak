

# Generated at 2022-06-12 21:41:26.245382
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.executor.module_common import ModuleCommon
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.factory import Factory
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    from ansible.config.manager import ConfigManager

# Generated at 2022-06-12 21:41:38.472888
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    playbooks_path = 'test-data/test_playbooks'
    playbook_path = 'test-data/test_playbooks/playbook.yaml'
    assert os.path.exists(playbook_path) is True, "Playbook path is not accessible"
    assert isinstance(playbook_path, str) is True, "Provide valid playbook path"
    inventory_path = 'test-data/test_inventory'
    assert os.path.exists(inventory_path) is True, "Inventory path is not accessible"
    assert isinstance(inventory_path, str) is True, "Provide valid inventory path"
    variable_manager = VariableManager('inventory')
    loader = DataLoader()
    passwords = dict(vault_pass='secret')

# Generated at 2022-06-12 21:41:39.630058
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbook = PlaybookExecutor([], [], [], [], [])
    assert playbook.run() == 0

# Generated at 2022-06-12 21:41:45.924843
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # create a fake inventory
    inventory = HostInventory()

    inventory.add_host('fake_host', 'all')
    inventory.add_host('fake_host2', 'all')

    # create a fake variable_manager
    variable_manager = VariableManager()

    variable_manager._extra_vars = {}
    variable_manager._options_vars = {}

    variable_manager._extra_vars['fake_key'] = 'fake_var'
    variable_manager._extra_vars['fake_key2'] = 'fake_var2'

    variable_manager._extra_vars['inventory_hostname'] = 'fake_host'
    variable_manager._extra_vars['inventory_hostname2'] = 'fake_host2'


# Generated at 2022-06-12 21:41:48.063387
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    playbooks = []
    inventory = ""
    variable_manager = ""
    loader = ""
    passwords = ""

    PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)


# Generated at 2022-06-12 21:41:48.562627
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:41:58.561818
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.vars.manager import VariableManager
    # Use this code block to create a sample test case
    # ansible-playbook --connection=local --become ./test/integration/targets/test_playbooks/ping.yml -i ./test/integration/inventory -vvvv
    # with 'ansible-playbook --connection=local --become ./test/integration/targets/test_playbooks/ping.yml -i ./test/integration/inventory -vvvv' as cmd:

# Generated at 2022-06-12 21:42:00.359513
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Initialize valid input to test method run
    input = {}
    return_value = ''
    test = PlaybookExecutor(input, None, None, None, None)
    assert test.run() == return_value



# Generated at 2022-06-12 21:42:11.704066
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../..'))
    from ansible import constants as C
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    def mock_init(self, playbooks, inventory, variable_manager, loader, passwords):
        self._playbooks = playbooks
        self._inventory = inventory
        self._variable_manager = variable_manager
        self._loader = loader
        self.passwords = passwords
        self._unreachable_hosts = dict()


# Generated at 2022-06-12 21:42:20.484736
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():

    class TestPlaybookExecutor(PlaybookExecutor):

        def _generate_retry_inventory(self, filename, failed_hosts):
            return True

    # Test if playbooks parameter is provided
    try:
        playbookExecutor = TestPlaybookExecutor(playbooks="playbook.yml",
                                                inventory=None, variable_manager=None,
                                                loader=None, passwords=None)
    except TypeError:
        pass
    else:
        raise AssertionError("Exception not raised")

    # Test if playbooks parameter is list
    try:
        playbookExecutor = TestPlaybookExecutor(playbooks=["playbook.yml"],
                                                inventory=None, variable_manager=None,
                                                loader=None, passwords=None)
    except TypeError:
        pass

# Generated at 2022-06-12 21:42:53.184502
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    plbk_executor = PlaybookExecutor(playbooks=['/home/ansible/playbook1.yml', '/home/ansible/playbook2.yml'],
                                     inventory=Inventory(loader=DataLoader(),
                                                         variable_manager=VariableManager(), host_list='hosts'),
                                     variable_manager=VariableManager(),
                                     loader=DataLoader(), passwords={})
    assert plbk_executor is not None


# Generated at 2022-06-12 21:43:02.302939
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    # initialize
    loader = DataLoader()
    passwords = dict(vault_pass='secret')

    # Parsing results in created objects
    pbex = PlaybookExecutor(
        playbooks=['test_playbook.yaml'],
        inventory=InventoryManager(loader=loader, sources='localhost,'),
        variable_manager=VariableManager(), loader=loader, passwords=passwords)
    # __init__ should set up _tqm
    assert pbex._tqm is not None
    # run() should return integer
    assert pbex.run() == 0

# Generated at 2022-06-12 21:43:12.549357
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Provide test case inputs
    test_playbooks = ['/home/purva/ansible-2.9.6/playbooks/cisco_ios_show.yml']
    test_inventory_file_name = '/home/purva/ansible-2.9.6/playbooks/inventory'
    test_inventory = InventoryManager(loader=None, sources=test_inventory_file_name)
    test_variable_manager = VariableManager()
    test_loader = DataLoader()
    test_passwords = dict()

    # Perform the test
    test_obj = PlaybookExecutor(test_playbooks, test_inventory, test_variable_manager, test_loader, test_passwords)
    test_result = test_obj.run()

    # Return the result and perform any assertion checks
    return test_result

# Generated at 2022-06-12 21:43:18.115958
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    pbex_obj = PlaybookExecutor(["/home/vhuang/ansible/playbooks/mongo_replica_set.yaml"],
                                InventoryManager(loader=DataLoader(), sources=["/home/vhuang/ansible/inventory/hosts"]),
                                "", "", "")
    pbex_obj.run()

if __name__ == '__main__':
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:43:25.678883
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'test_key': 'test_value'}
    path = '../test/test_playbooks/playbook.yml'
    variable_manager.set_inventory(Inventory(loader, '../test/test_playbooks/hosts'))
    playbook_executor = PlaybookExecutor([path], variable_manager, loader, {})
    result = playbook_executor.run()

    #Test for the return code
    assert result == 0

# Generated at 2022-06-12 21:43:33.731291
# Unit test for constructor of class PlaybookExecutor

# Generated at 2022-06-12 21:43:35.072588
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # TODO
    # Change this assertion to more readable one
    pass

# Generated at 2022-06-12 21:43:35.681235
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    return

# Generated at 2022-06-12 21:43:46.936225
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    fake_loader = DictDataLoader({})
    fake_inventory = Inventory(loader=fake_loader, variable_manager=VariableManager())
    fake_variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)

    pbex = PlaybookExecutor(
        playbooks=['test_playbook.yml'],
        inventory=fake_inventory,
        variable_manager=fake_variable_manager,
        loader=fake_loader,
        passwords={}
    )

    assert pbex._playbooks == ['test_playbook.yml']
    assert pbex._inventory == fake_inventory
    assert pbex._variable_manager == fake_variable_manager
    assert pbex._loader == fake_loader

# Generated at 2022-06-12 21:43:47.590109
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:44:26.369783
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbooks = ['play.yml']
    inventory = BaseInventory()
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = {}

    playbook_executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    result = playbook_executor.run()

# Generated at 2022-06-12 21:44:28.179889
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    PlaybookExecutor()



# Generated at 2022-06-12 21:44:41.423313
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    class UtPlaybook:
        pass
    class UtVariableManager:
        pass
    class UtLoader:
        pass
    class UtTaskQueueManager:
        def __init__(self):
            self.send_callback_feedback = None
        def send_callback(self, *args):
            self.send_callback_feedback = args
            return None
        def cleanup(self):
            pass
    class UtInventory:
        def __init__(self):
            self.feedback = None
        def restrict_to_hosts(self, some_iterable):
            self.feedback = some_iterable
        def remove_restriction(self):
            self.feedback = 'remove_restriction'
    class UtPlay:
        def __init__(self):
            self.name = 'ut-play'
            self

# Generated at 2022-06-12 21:44:42.511169
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass


# Generated at 2022-06-12 21:44:50.653320
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Test fail
    test_data = dict(
        playbooks=['test_fixtures/test.yml'],
        inventory=Inventory(['localhost']),
        variable_manager=Inventory(),
        loader=None,
        passwords=Inventory()
    )
    pbe = PlaybookExecutor(**test_data)
    assert pbe is not None
    assert pbe.run() is not None

# Generated at 2022-06-12 21:44:51.339662
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass


# Generated at 2022-06-12 21:44:52.345007
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # FIXME:
    pass

# Generated at 2022-06-12 21:44:56.805202
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from zupport import mock, zupport_playbook_executor
    with mock.patch('zupport.zupport_playbook_executor.PlaybookExecutor.run') as mock_run:
        mock_run.return_value = 'test'
        results = zupport_playbook_executor.run()

# Generated at 2022-06-12 21:45:08.189228
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
	# Create a fake inventory
	inventory = FakeInventory()
	
	# Create a fake variable manager
	variable_manager = FakeVariableManager()
	
	# Create a fake loader
	loader = FakeLoader()
	
	# Create a fake password
	password = FakePassword()
	
	# Create an empty list of playbooks
	playbooks = []
	
	# Create a playbook executor using the created objects
	executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, password)
	
	# Run the playbook executor
	executor.run()
	
	# Check that the inventory was correctly called during the run of the playbook executor
	assert(inventory.called)
	
	# Check that the inventory was correctly called during the run of the playbook executor
	assert(variable_manager.called)
	


# Generated at 2022-06-12 21:45:09.579709
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    print('test_PlaybookExecutor_run')
    pass


# Generated at 2022-06-12 21:45:44.655701
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    # Here we can check if an PlaybookExecutor object is created appropriately
    pass

# Generated at 2022-06-12 21:45:51.621666
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    # Initilization of variables for unit testing class PlaybookExecutor
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources="")
    passwords = {}
    playbooks = ["/home/user/test.yml"]

    # Execution of constructor
    lst = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    # Assertion checks
    assert lst._playbooks == playbooks
    assert lst._inventory == inventory
    assert lst._variable_manager == variable_manager
    assert lst._loader == loader
    assert lst.passwords == passwords
    assert lst._unreachable_hosts == {}
    assert lst._tqm.inventory == inventory
    assert lst._tqm.variable_manager == variable_manager


# Generated at 2022-06-12 21:45:56.002496
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Create a fixture
    fixture = init_fixture(request)
    # Get the fixture data
    data = getattr(fixture, 'subtest_%s' % request.param)
    # return the fixture data
    return data

# Generated at 2022-06-12 21:45:59.395966
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    executor = PlaybookExecutor(
        playbooks=["test"],
        inventory="test",
        variable_manager="test",
        loader="test",
        passwords="test"
    )
    assert executor is not None


# Generated at 2022-06-12 21:46:03.645284
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    loader = DataLoader()
    passwords = dict()
    playbooks = ['/etc/ansible/test.yml']
    x = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    with pytest.raises(AnsibleError):
        x.run()

# Generated at 2022-06-12 21:46:05.370717
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    assert False, "TODO: Write tests for test_PlaybookExecutor_run"



# Generated at 2022-06-12 21:46:06.129027
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:46:10.466158
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    '''
    unit test for method run of class PlaybookExecutor
    '''
    mycls = PlaybookExecutor(
        playbooks=None,
        inventory=None,
        variable_manager=None,
        loader=None,
        passwords=None
    )
    result = mycls.run()
    assert(result == 0)


# Generated at 2022-06-12 21:46:17.877739
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    playpath = '../../examples/ansible_managed.template'
    from ansible.inventory.manager import InventoryManager
    i = InventoryManager('localhost,')
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()
    from ansible.vars.manager import VariableManager
    v = VariableManager()
    pe = PlaybookExecutor([playpath], i, v, dl, None)
    print(pe)

if __name__ == '__main__':
    test_PlaybookExecutor()

# Generated at 2022-06-12 21:46:18.701345
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    assert True

# Generated at 2022-06-12 21:47:02.839961
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import ansible.utils.collection_loader
    import ansible.inventory.manager
    import ansible.playbook.play
    import ansible.parsing.yaml.loader
    import ansible.parsing.yaml.objects

    # Create test object
    sample_inventory = ansible.inventory.manager.InventoryManager(loader=ansible.utils.collection_loader,
                                                                  sources='')
    sample_variable_manager = ansible.vars.manager.VariableManager(loader=ansible.utils.collection_loader,
                                                                   inventory=sample_inventory)
    sample_loader = ansible.parsing.dataloader.DataLoader()
    sample_passwords = {}

# Generated at 2022-06-12 21:47:11.067039
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Arguments for method run of class PlaybookExecutor
    playbooks = ["/home/ansible/projects/ansible/playbooks/project2.yml"]
    inventory = []
    variable_manager = []
    loader = PlaybookExecutor
    passwords = "test_password"

    # possible return values and their description
    possible_return_values = [
        {'playbook': '/home/ansible/projects/ansible/playbooks/project2.yml', 'plays': []},
    ]
    playbooks_valid_values = [
        "/home/ansible/projects/ansible/playbooks/project2.yml"
    ]
    playbooks_wrong_values = [
        "/home/ansible/projects/ansible/playbooks/project_300.yml"
    ]

    # check if method run

# Generated at 2022-06-12 21:47:20.832158
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    args = parser.parse_args()
    setattr(args, 'version', False)
    setattr(args, 'listhosts', True)
    setattr(args, 'listtasks', True)
    setattr(args, 'listtags', True)
    args.inventory = None
    args.connection = 'local'
    args.module_path = None
    args.private_key_file = None
    args.ssh_common_args = None
    args.ssh_extra_args = None
    args.sftp_extra_args = None
    args.scp_extra_args = None
    args.become = False
    args.become_method = 'sudo'
    args.become_user = None
    args.become_ask_pass = False
    args.verbosity = 0

# Generated at 2022-06-12 21:47:21.466392
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:47:23.888616
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbook_executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    result = playbook_executor.run()
    assert result == 0

# Generated at 2022-06-12 21:47:30.542294
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    context.CLIARGS = ImmutableDict(listhosts=False, listtasks=False, listtags=False, syntax=False, connection='ssh',
                                    module_path=None, forks=None, private_key_file=None,
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                    become=False, become_method=None, become_user=None, verbosity=0, check=False,
                                    diff=False, tags=[u'all'], run_once=False, start_at_task=None,
                                    inventory=[u'/Users/lavie/PycharmProjects/ansible/examples/inventory'],
                                    subset='all')


# Generated at 2022-06-12 21:47:34.050353
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

if __name__ == '__main__':
    test_PlaybookExecutor()

# Generated at 2022-06-12 21:47:45.545357
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    playbook_path = "playbooks/show_arp.yaml"
    var_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=["inventory/test_inventory.yaml"])
    passwords = {}

    context.CLIARGS['syntax'] = True

    playbook = PlaybookExecutor(
        playbooks=[playbook_path],
        inventory=inventory,
        variable_manager=var_manager,
        loader=loader,
        passwords=passwords)

    playbook.run()
    assert context.CLIARGS['syntax']


if __name__ == '__main__':
    test

# Generated at 2022-06-12 21:47:53.682391
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
   inventory = ansible.inventory.Inventory("localhost,")
   variable_manager = ansible.vars.VariableManager()
   loader = DataLoader()
   passwords = {}
   playbooks = ["./test/test_playbook.yml"]
   ansible_playbook = ansible.playbook.PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
   ansible_playbook.run()

if __name__ == "__main__":
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:48:01.164118
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Make args for constructor
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = {}
    # Create an instance of PlaybookExecutor
    pb = PlaybookExecutor(['/usr/lib/python2.7/site-packages/ansible/playbooks/test/test_playbook.yml'], None, variable_manager, loader, passwords)
    # Call the method run
    pb.run()
    assert len(pb._playbooks) != 0
    assert pb._inventory != None
    assert pb._variable_manager != None
    assert len(pb.passwords) == 0
    assert pb._unreachable_hosts == {}

# Generated at 2022-06-12 21:48:43.458977
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    print("Test PlaybookExecutor constructor")
    playbooks = "test_playbook"
    inventory = "test_inventory"
    variable_manager = "test_variable_manager"
    loader = "test_loader"
    passwords = "test_passwords"
    playbook_executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    assert playbook_executor is not None
    assert playbook_executor._playbooks == "test_playbook"
    assert playbook_executor._inventory == "test_inventory"
    assert playbook_executor._variable_manager == "test_variable_manager"
    assert playbook_executor._loader == "test_loader"
    assert playbook_executor.passwords == "test_passwords"
    assert playbook_executor._unreachable_hosts == {}

#

# Generated at 2022-06-12 21:48:51.272719
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Create a Mock Inventory with Host
    inventory = Inventory(loader=None, variable_manager=None, host_list=[])
    inventory._hosts_cache= [ Host(name='52.52.52.52')]

    # Mock the Playbook being passed in but don't want to run anything for test
    # so we create an instance where the run method does nothing
    class MockPlaybook_no_run:
        def __init__(self, playbook):
            self._included_path = None
            self.vars_prompt = None
        def post_validate(self, templar):
            pass
        def get_plays(self):
            # Return a list of plays with one empty play
            self.plays = []
            self.plays.append(MockPlay())
            return self.plays


# Generated at 2022-06-12 21:48:59.023668
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # initialize object
    playbooks = ['playbook1.yml','playbook2.yml','playbook3.yml']
    inventory = ['inventory1.yml','inventory2.yml','inventory3.yml']
    variable_manager = None
    loader = None
    passwords = {}

    # execute method
    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    executor.run()

    # assert results
    assert executor.run() == 0

test_PlaybookExecutor_run()



# Generated at 2022-06-12 21:48:59.654124
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:49:02.059721
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # No exception
    playbook_executor = PlaybookExecutor("playbooks", "inventory", "variable_manager", "loader", "passwords")
    playbook_executor.run()

# Generated at 2022-06-12 21:49:02.670074
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:49:07.981306
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    e = mock.Mock()
    with context.captured_stdout() as stdout:
        with context.captured_stdout() as stderr:
            PlaybookExecutor(e,e,e,e,e).run()
            assert 'run_self_tests' not in stdout.getvalue()
            assert 'run_self_tests' not in stderr.getvalue()
            assert 'No issues encountered' in stdout.getvalue()


# Generated at 2022-06-12 21:49:13.767701
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbooks = ['ansible/playbooks/tests/cli/cli_play.yml']
    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager()
    loader = DataLoader()

    obj = PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader)

    assert isinstance(inventory, InventoryManager)
    assert isinstance(variable_manager, VariableManager)
    assert isinstance(loader, DataLoader)

    assert obj.run() == 0

# Generated at 2022-06-12 21:49:25.813189
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    try:
        test_playbooks_list = ['C:\\Ansible\\playbooks\\playbook1.yml', 'C:\\Ansible\\playbooks\\playbook2.yml']
        test_playbooks = [to_text(test_playbooks_list[0]), to_text(test_playbooks_list[1])]
        test_inventory = Inventory("C:\\Ansible\\inventory\\hosts")
        test_variable_manager = None
        test_loader = None
        test_passwords = None
        test_obj = PlaybookExecutor(test_playbooks, test_inventory, test_variable_manager, test_loader, test_passwords)
    except Exception as e:
        return False

    return True

if __name__ == '__main__':
    test_PlaybookExecutor()

# Generated at 2022-06-12 21:49:37.043794
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    class DummyInventory2:
        def __init__(self):
            self.hosts = {
                'all': {
                    'children': [
                        'group1',
                        'group2',
                        'group3',
                        'ungrouped'
                    ]
                },
                'group1': {
                    'hosts': ['host01', 'host02']
                },
                'group2': {
                    'hosts': ['host03']
                },
                'group3': {
                    'children': ['group4', 'group5']
                },
                'group4': {
                    'hosts': ['host04']
                },
                'group5': {
                    'hosts': ['host05']
                }
            }

        def get_hosts(self, pattern, ignore_limits=False):
            return

# Generated at 2022-06-12 21:50:18.521728
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass_args = {}
    fail_args = {}
    # Pass: Try to run the ansible playbook
    arg = {'listhosts':True,'listtasks':True,'listtags':True,'syntax':True}
    p = PlaybookExecutor(playbooks="/home/ansible/playbook.yml",inventory="ip_address",variable_manager="",loader="",passwords="")
    p.run()
    # Fail: Try to run the ansible playbook with empty parameters
    arg = {}
    p1 = PlaybookExecutor(playbooks="",inventory="",variable_manager="",loader="",passwords="")
    p1.run()

# Generated at 2022-06-12 21:50:23.754537
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    '''
    Unit test for method run of class PlaybookExecutor
    '''

    playbook_executor = PlaybookExecutor(None, None, None, None, None)
    print (test_PlaybookExecutor_run.__doc__)
    print (playbook_executor.run.__doc__)
    print (playbook_executor.run())


# Generated at 2022-06-12 21:50:33.714779
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    _loader = DictDataLoader({})
    _inventory = InventoryManager(loader=_loader, sources='')
    _variable_manager = VariableManager(_loader, inventory=_inventory)
    _variable_manager._extra_vars = {}
    _display = Display()
    _options = Options(connection='smart', module_path=None, forks=100, become=None,
                       become_method=None, become_user=None, check=False, diff=False,
                       syntax=False, start_at_task=None)
    passwords = dict(conn_pass=None, become_pass=None)
    _passwords = passwords