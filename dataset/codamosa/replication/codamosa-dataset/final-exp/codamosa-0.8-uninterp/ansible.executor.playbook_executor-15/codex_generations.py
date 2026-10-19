

# Generated at 2022-06-12 21:41:12.447361
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    vars = VariableManager()
    Playbook.vars = vars

    play = Play()
    play.vars = vars
    play.playbook = Playbook()

    inventory = InventoryManager()
    PlaybookExecutor(playbook=[play], inventory=inventory, variable_manager=vars, loader=None, passwords=None).run()
    
    
    pass

# Generated at 2022-06-12 21:41:24.198939
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Setup
    playbooks = ['../ansible-plugins-collection-playbooks/collection-playbooks//cloud/azure/azure_rm_networkinterface.yml']
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=['../ansible-plugins-collection-playbooks/collection-playbooks/cloud/azure/azure_rm.yml'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-12 21:41:37.343873
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    pb1 = PlaybookExecutor('/tmp/playbook.yml', None, None, None, None)
    assert(pb1._playbooks==['/tmp/playbook.yml'])
    assert(pb1._inventory==None)
    assert(pb1._variable_manager==None)
    assert(pb1._loader==None)
    assert(pb1.passwords==None)
    assert(pb1._unreachable_hosts==dict())

    assert(pb1._tqm is None)

    pb2 = PlaybookExecutor(None, None, None, None, None)
    assert(pb2._playbooks==None)
    assert(pb2._inventory==None)
    assert(pb2._variable_manager==None)
    assert(pb2._loader==None)

# Generated at 2022-06-12 21:41:42.060061
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    parser = PlaybookParser(loader=DataLoader(), variable_manager=VariableManager(), inventory=InventoryManager())
    playbook_executor = PlaybookExecutor(playbooks = ['../ansible-2.8.5/lib/ansible/playbooks/test.yml'], inventory = parser.inventory,
    variable_manager = parser.variable_manager, loader = parser.loader, passwords = {})


# main function starts here
if __name__ == "__main__":
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:41:48.419460
# Unit test for method run of class PlaybookExecutor

# Generated at 2022-06-12 21:41:58.349312
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from unittest import TestCase, mock as mock
    from ansible.playbook import Playbook
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import become_loader
    from ansible.plugins.loader import shell_loader
    class PlaybookExecutor_run_TestCase(TestCase):
        # testcase for the PlaybookExecutor class method run
        # program execution goes here
        def test_PlaybookExecutor(self):
            playbooks = mock.Mock(spec=Playbook)
            inventory = mock.Mock(spec=Inventory)
            variable_manager = mock.Mock(spec=VariableManager)
            loader = mock.Mock(spec=DataLoader)
            passwords = mock.Mock()


# Generated at 2022-06-12 21:42:00.255443
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # TODO: Test for different scenarios in which the run method of PlaybookExecutor class is used
    print('PlaybookExecutor class is tested')
    pass

# Generated at 2022-06-12 21:42:00.804749
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:42:12.605237
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    '''
    Unit test of PlaybookExecutor constructor
    '''

    context.CLIARGS = {'syntax': True}
    loader = DataLoader()
    passwords = {}

    inventory = Inventory(loader, variable_manager=vars.VariableManager())
    playbooks = ['./test.yml']

    playbook_executor = PlaybookExecutor(playbooks, inventory, vars.VariableManager(), loader, passwords)
    assert playbook_executor is not None
    from ansible.executor.task_queue_manager import TaskQueueManager
    assert playbook_executor._tqm is None

    # test without syntax
    context.CLIARGS = {}
    playbook_executor = PlaybookExecutor(playbooks, inventory, vars.VariableManager(), loader, passwords)
    assert playbook_executor is not None
   

# Generated at 2022-06-12 21:42:21.152396
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    '''
    Unit test for method run of class PlaybookExecutor
    '''
    # Inventory is a collection of compiled hosts, groups and vars
    inventory = Inventory(loader=Loader(), variable_manager=VariableManager(), host_list='localhost')
    # Set variables
    variable_manager = VariableManager(loader=Loader(), inventory=inventory)
    # Set loader will read playbooks from corresponding path
    loader = DataLoader()
    # Set passwords
    passwords = dict(vault_pass='secret')
    # Create a play

# Generated at 2022-06-12 21:42:50.791986
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pb = PlaybookExecutor("playbook_for_unit_test", "inventory_for_unit_test", "variable_manager_for_unit_test", "loader_for_unit_test", "passwords_for_unit_test")
    pb.run()

# Generated at 2022-06-12 21:42:53.958236
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    """
    Verifies that the PlaybookExecutor() can be initialized.
    """
    PlaybookExecutor([], {}, {}, {}, {})



# Generated at 2022-06-12 21:43:01.374502
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # A playbooks executor is needed for running ansible
    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    # run the playbook
    exit_code = executor.run()
    # If the execution failed, fail the task
    if exit_code != 0:
        raise AnsibleError('Error while executing a playbook.')
    display.display(u'Playbook had been executed successfully.')

# Generated at 2022-06-12 21:43:11.885882
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Configuramos el contexto de pruebas
    context._init_global_context(['ansible-playbook', '-i', 'localhost,'])
    # Creamos un objeto y lo inicializamos
    pbe = PlaybookExecutor([], InventoryManager(loader=None, sources=['localhost,']), VariableManager(), '', '')
    # Creamos una maquina virtual y la inicializamos
    vm = BaseVM()
    vm.ip = 'localhost'
    vm.plataform = 'linux'
    vm.connection = 'local'
    vm.user = 'root'
    vm.password = 'toor'
    # Ejecutamos PlaybookExecutor.run() con una máquina virtual incorrecta y la comprobamos

# Generated at 2022-06-12 21:43:16.996483
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    # Call class constructor
    pe = PlaybookExecutor(playbooks="", inventory ="", variable_manager ="", loader ="", passwords ="")
    assert pe is not None
    assert pe._playbooks is not None
    assert pe._inventory is not None
    assert pe._variable_manager is not None
    assert pe._loader is not None
    assert pe.passwords is not None
    assert pe._unreachable_hosts is not None


# Generated at 2022-06-12 21:43:21.339807
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Create a PlaybookExecutor object
    pbe = PlaybookExecutor(playbooks="test_playbooks/playbook_test.yaml", inventory=None, variable_manager=None, loader=None, passwords=None)
    # Check it works without raising any exceptions
    assert pbe.run() == 0

# Generated at 2022-06-12 21:43:31.064974
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    print("class PlaybookExecutor - method run")

    from ansible.playbook import Playbook
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import ImmutableDict

    # Ansible.playbook.Playbook
    pb = Playbook()
    # Ansible.vars.VariableManager
    variable_manager = VariableManager()
    # Ansible.inventory.InventoryManager

# Generated at 2022-06-12 21:43:31.698660
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:43:34.424495
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    wf = PlaybookExecutor([], _inventory, _variable_manager, _loader, [])
    assert wf.run() == 0

# Generated at 2022-06-12 21:43:35.084482
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:44:07.601562
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:44:08.684188
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass


# Generated at 2022-06-12 21:44:11.210187
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    '''playbook executor test case'''
    playbook = PlaybookExecutor([], None, None, None, None)
    result = playbook.run()
    assert result is None

# Generated at 2022-06-12 21:44:23.968167
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    '''
    Unit test for method run of class PlaybookExecutor
    '''
    # Test with valid entry
    variable_manager = VariableManager()
    variable_manager._options = {'syntax': True}
    variable_manager._extra_vars = {}
    variable_manager._options['inventory'] = './inventory'
    variable_manager._options['verbosity'] = 2
    variable_manager._options['listhosts'] = True
    variable_manager._options['listtasks'] = True
    variable_manager._options['listtags'] = True
    passwords = dict()
    loader = DataLoader()
    inventory = Inventory(loader, variable_manager._options['inventory'], variable_manager._options['plugin_filters'])
    inventory.parse_inventory(inventory.host_list)

# Generated at 2022-06-12 21:44:27.973115
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():

    playbooks = ['/Users/mayuresh/Git/ansible/test/integration/targets/default/playbook.yml']
    inventory = InventoryManager(loader=DataLoader(), sources='/Users/mayuresh/Git/ansible/test/integration/targets/default/inventory')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    passwords = dict()
    
    pbe = PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
    pbe.run()
    # TODO: Also test for warnings and errors 



# Generated at 2022-06-12 21:44:30.685760
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    p = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    p.run()


# Generated at 2022-06-12 21:44:43.478044
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.playbook
    import ansible.plugins.loader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    #from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import module_loader
    from ansible.plugins.callback import CallbackBase
    from ansible.constants import DEFAULT_MODULE_PATH
    from ansible.module_utils._text import to_bytes, to_native
    import shutil
    import os



# Generated at 2022-06-12 21:44:55.671986
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Set up objects and mocks.
    playbooks = "filepath to playbook"
    inventory = "inventory"
    variable_manager = "variable manager"
    loader = "loader"
    passwords = "passwords"

    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    # Test1: if self._unreachable_hosts is not empty, send callback
    # v2_playbook_on_stats and clean up.
    executor._unreachable_hosts = {'1.1.1.1': '1.1.1.1'}
    executor._tqm = Mock()
    executor._tqm.cleanup = Mock()
    executor._tqm.send_callback = Mock()

    executor.run()
    executor._tqm

# Generated at 2022-06-12 21:45:02.154552
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Test object init 
    playbooks = None
    inventory = {'loader': FakeOptions()}
    variable_manager = FakeOptions()
    loader = FakeOptions()
    passwords = FakeOptions()
    pbe = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    # Test actual functionality
    assert pbe.run() == None


# Unit test helper class to provide dummy
# objects for the PlaybookExecutor unit test

# Generated at 2022-06-12 21:45:09.825164
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    #playbooks = ['c:\\Users\\Administrator\\Desktop\\playbook-test.yaml']
    playbooks = ['playbook.yaml']
    inventory = InventoryManager(loader=None, sources=["/Users/michael/work/ansible_test_hosts"])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    loader = DataLoader()
    passwords = dict()
    pb = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    pb.run()



# Generated at 2022-06-12 21:45:45.518741
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    P = PlaybookExecutor(
        inventory=None,
        variable_manager=None,
        loader=None,
        passwords=None
    )
    assert P is not None


# Generated at 2022-06-12 21:45:54.596407
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Set up parameters for unit tests
    class DummyModule:
        def __init__(self, name, *args, **kwargs):
            self.name = name
        def __call__(self, *args, **kwargs):
            return self.name
    # Can not initiate a PlaybookExecutor directly, so we have to initiate an AnsibleRunner class first
    ar = AnsibleRunner(module_name=DummyModule)
    ar.module_name.run_once=True
    ar.run()

if __name__ == "__main__":
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:46:05.111230
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    """
    This method is responsible for testing the method 'run' of class PlaybookExecutor
    """
    def __init__(self, playbooks, inventory, variable_manager, loader, passwords):
        self._playbooks = playbooks
        self._inventory = inventory
        self._variable_manager = variable_manager
        self._loader = loader
        self.passwords = passwords
        self._unreachable_hosts = dict()

        if context.CLIARGS.get('listhosts') or context.CLIARGS.get('listtasks') or \
                context.CLIARGS.get('listtags') or context.CLIARGS.get('syntax'):
            self._tqm = None

# Generated at 2022-06-12 21:46:12.809236
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbook_executor = PlaybookExecutor(None, None, None, None, None)
    result = playbook_executor.run()
    assert result == 0
    # Test case with single playbook
    test_playbooks = ['~/playbooks/test.yaml']
    playbook_executor = PlaybookExecutor(test_playbooks, None, None, None, None)
    result = playbook_executor.run()
    assert result == 0
    # Test case with multiple playbooks
    test_playbooks = ['~/playbooks/test.yaml', '~/playbooks/test1.yaml']
    playbook_executor = PlaybookExecutor(test_playbooks, None, None, None, None)
    result = playbook_executor.run()
    assert result == 0

# Generated at 2022-06-12 21:46:22.788284
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    '''
    Unit test for constructor of class PlaybookExecutor
    '''
    import ansible.utils.collection_loader
    import ansible.inventory.manager


# Generated at 2022-06-12 21:46:23.450614
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:46:34.539496
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():

    parser = cmdline.CLI.base_parser(constants.DEFAULT_MODULE_PATH)
    cmdline.add_ansible_module_args(parser)
    args = parser.parse_args()

    options = cmdline.cmdline_to_dict(args)


# Generated at 2022-06-12 21:46:36.055443
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    executor = PlaybookExecutor
    executor.run()

# Generated at 2022-06-12 21:46:39.060748
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbooks = ['ansible-playbook', 'playbook1', 'playbook2']
    # The inventory is a class object defined in the ansible.inventory module
    inventory = inventory()
    variable_manager = variable_manager()
    loader = loader()
    passwords = {'conn_pass': 'test_password', 'become_pass': 'test_password1'}
    playbookexecutor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    playbookexecutor.run()

# Generated at 2022-06-12 21:46:44.907370
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    inventory_dict = {'all': {'hosts': {'host1': {}, 'host2': {}}}}
    fake_inventory = create_inventory(inventory_dict)
    fake_variable_manager = FakeVariableManager(fake_inventory)
    fake_loader = create_loader(fake_inventory)

    playbook_path = os.path.join(
        data_context().content.plugin_loader.package_root,
        '../../../../lib/ansible/plugins/action/ansible.cfg')

    args = dict(inventory=fake_inventory, variable_manager=fake_variable_manager, loader=fake_loader, passwords={})
    args.update(context.CLIARGS)
    args.pop('one_line')
    args.pop('tree')
    args.pop('listtags')

# Generated at 2022-06-12 21:47:20.450065
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    """
    [Usage:playbook-executor]
    :param CLIAGRS:         A dict of parameters specified on the command line
    """
    cliargs = {'syntax':False, 'listhosts':False, 'listtasks':False, 'listtags':False, 'start_at_task':None,
               'verbosity':0, 'extra_vars':{}}
    cliargs = type('cliargs', (object,), cliargs)
    context.CLIARGS = cliargs()

    context.CLIARGS.extra_vars = dict(host='40.40.40.40')

    loader = DataLoader()
    variable_manager = VariableManager()
    passwords = dict()

    display.verbosity = 3


# Generated at 2022-06-12 21:47:29.157506
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():


    # Test case 1:
    # Test variables
    playbooks = ["../test/test_playbooks/one_play_playbook.yml"]

    # Test case 1 : 
    # Test variables

# Generated at 2022-06-12 21:47:35.675418
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    loader = None
    variable_manager = variable_manager_base.VariableManager()
    passwords = None
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager._options = {'syntax': False}
    variable_manager._extra_vars = {}

# Generated at 2022-06-12 21:47:47.029739
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():

    play_source = dict(
        name="myplay",
        hosts='localhost',  # by default, localhost
        gather_facts='no',  # by default, on
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

    # since the API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
    options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options.connection = 'local'
    options.module_path = ''

# Generated at 2022-06-12 21:47:48.498606
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    playbook_executor = PlaybookExecutor([], [], [], [], [])
    assert playbook_executor

# Generated at 2022-06-12 21:47:58.904627
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
  obj = PlaybookExecutor([], inventory, variable_manager, loader, passwords)
  obj.run()
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# runner.py:
# ----------------------------------------------------------------------------------------------------------------------

#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA

# Generated at 2022-06-12 21:48:04.989598
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    pbex = PlaybookExecutor(['./test/ansible1.yml'], inventory, variable_manager, loader, None)
    assert isinstance(pbex, PlaybookExecutor)
    assert pbex.run() == 0

# Generated at 2022-06-12 21:48:14.379452
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    hosts = [
        dict(
            hostname = 'hostname1',
            ansible_host = "1.1.1.1",
        ),
        dict(
            hostname = 'hostname2',
            ansible_host = "2.2.2.2",
        ),
    ]

    # Create a dummy playbook.
    playbook_location = "/tmp/test_PlaybookExecutor_run.yaml"
    with open(playbook_location, "w") as playbooks:
        playbooks.write(
            textwrap.dedent(
                """
                ---
                - hosts: all
                - hosts: hostname1
                  tasks:
                    - command: echo "hello world"
                """
            )
        )
 
    # Create a dummy ansible.cfg file.

# Generated at 2022-06-12 21:48:20.913784
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    fake_loader = DictDataLoader({})
    fake_inventory = InventoryManager(loader=fake_loader, sources=[])
    fake_passwords = DictDataLoader({})
    fake_variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    playbook_executor = PlaybookExecutor(
        playbooks=[],
        inventory=fake_inventory,
        variable_manager=fake_variable_manager,
        loader=fake_loader,
        passwords=fake_passwords
    )
    result = playbook_executor.run()
    assert result == 0
    result = playbook_executor.run()
    assert result == 0

# Generated at 2022-06-12 21:48:28.606835
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import copy
    import platform

    check_args = copy.copy(context.CLIARGS)
    check_args['inventory'] = '/home/anthony/Documents/ansible-toolkit/ansible/inventory/hosts'
    check_args['listhosts'] = ''
    check_args['listtasks'] = ''
    check_args['listtags'] = ''
    check_args['syntax'] = ''
    check_args['connection'] = 'local'
    check_args['module-path'] = ''
    check_args['forks'] = 5
    check_args['remote-user'] = 'user'
    check_args['private-key'] = ''
    check_args['ssh-common-args'] = ''
    check_args['ssh-extra-args'] = ''

# Generated at 2022-06-12 21:49:09.586683
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # - test_PlaybookExecutor_run
    ################################################################################
    # PlaybookExecutor.run
    ################################################################################

    # Test with simple playbook and check_mode
    ###########################################

    p = PlaybookExecutor(playbooks=['test_playbook1.yml'], inventory=InventoryManager(None, 'localhost,'), variable_manager=VariableManager(), loader=DataLoader(), passwords={})
    result = p.run()
    assert result == 2

    # Test simple playbook with check_mode and diff
    ################################################

    p = PlaybookExecutor(playbooks=['test_playbook1.yml'], inventory=InventoryManager(None, 'localhost,'), variable_manager=VariableManager(), loader=DataLoader(), passwords={})
    context.CLIARGS['check'] = True

# Generated at 2022-06-12 21:49:10.143428
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    pass

# Generated at 2022-06-12 21:49:11.636859
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pl = PlaybookExecutor()
    assert pl.run == 0

# Generated at 2022-06-12 21:49:23.630712
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    global display
    args = argparse.Namespace()
    args.syntax = True
    args.listhosts = True
    args.listtasks = True
    args.listtags = True
    args.connection = u'local'
    args.module_path = None
    args.forks = 100
    args.remote_user = None
    args.private_key_file = None
    args.ssh_common_args = None
    args.ssh_extra_args = None
    args.sftp_extra_args = None
    args.scp_extra_args = None
    args.become = False
    args.become_method = u'sudo'
    args.become_user = None
    args.verbosity = 1
    args.check = False
    args.diff = False
    args.inventory

# Generated at 2022-06-12 21:49:34.719085
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = dict(vault_pass='secret')

    results = []
    callback_results = []
    options = {}
    options['playbook_path'] = 'playbook.yml'
    options['listhosts'] = None
    options['listtasks'] = None
    options['listtags'] = None
    options['syntax'] = None
    options['connection'] = 'smart'
    options['module_path'] = None
    options['forks'] = 5
    options['private_key_file'] = None
    options['ssh_common_args'] = None
    options['ssh_extra_args'] = None
    options['sftp_extra_args'] = None
    options['scp_extra_args'] = None
    options['become']

# Generated at 2022-06-12 21:49:44.770946
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    """
    Test utility functions of class PlaybookExecutor
    """

    # For testing purpose
    class MockCLI:
        verbosity = 0
        inventory = None
        subset = None
        module_paths = None
        extra_vars = None
        connection = None
        forks = None
        timeout = None
        poll_interval = None
        become = None
        become_method = None
        become_user = None
        check = None
        diff = None
        syntax = None
        start_at_task = None
        step = None
        start_at_play = None


# Generated at 2022-06-12 21:49:50.522220
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    options = context.CLIARGS
    print("test_PlaybookExecutor_run")
    pb_ex = PlaybookExecutor(playbooks=['playbook/playbook.yml'],
                             inventory=InventoryManager(loader=DataLoader(), sources=['inventory/hosts']),
                             variable_manager=VariableManager(), loader=DataLoader(), passwords={})
    options['listtags'] = True
    pb_ex.run()

# Generated at 2022-06-12 21:49:55.724529
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # test case 1:
    try:
        import ansible.utils.args as args
        import ansible.utils.password as password
        args_manager1 = args.Args()
    except Exception as e:
         print("Exception: " + str(e))
    # test case 2:
    try:
        import ansible.utils.args as args
        import ansible.utils.password as password
        password_manager2 = password.Password()
    except Exception as e:
         print("Exception: " + str(e))

# Generated at 2022-06-12 21:49:57.838138
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbook = PlaybookExecutor()
    assert playbook.run() == 0

# Generated at 2022-06-12 21:50:08.341914
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    # Tests constructor without an inventory
    mock_loader = MagicMock()
    mock_variable_manager = MagicMock()
    mock_variable_manager._extra_vars.return_value = {}
    pbexec = PlaybookExecutor(playbooks=['test/ansible/test_utils/test_playbook.yml'],
                              inventory=None,
                              variable_manager=mock_variable_manager,
                              loader=mock_loader,
                              passwords={})

    # Tests constructor with an inventory
    mock_inventory = MagicMock()
    mock_variable_manager._extra_vars.return_value = {}