

# Generated at 2022-06-12 21:41:10.682390
# Unit test for method run of class PlaybookExecutor

# Generated at 2022-06-12 21:41:22.625319
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import os
    import sys
    import tempfile

    from ansible import context
    from ansible.plugins import vars_loader

    from ansible.modules.system import ping
    from ansible.utils.display import Display
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    
    curr_path = os.path.dirname(os.path.realpath(__file__))

    # create a temporary directory to test loading files from
    tmpdir = tempfile.mkdtemp()

    # create a directory to hold file loader plugin test data
    vars_path = os.path.join(tmpdir, 'vars')
    os.mkdir(vars_path)

    # create a file loader plugin

# Generated at 2022-06-12 21:41:32.898925
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbook = '/home/centos/Project/ansible-practice/roles/role_a/tasks/main.yml'
    inventory = InventoryManager
    variable_manager = []
    loader = Loader
    passwords = []
    playbooks = []
    playbooks.append(playbook)
    # playbooks = []
    # playbooks_executor = PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
    # playbooks_executor.run()

# test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:41:42.919098
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    ##################################################################################
    #																				#
    #	Simple test to validate the basic functionality of class PlaybookExecutor 	#
    #																				#
    ##################################################################################
    # Make sure we have the required python modules
    module_imports = ["ansible.module_utils.common.parameters","ansible.module_utils.common.collections"]
    module_exists(module_imports)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    #playbooks = ["playbook_listen.yml"]

# Generated at 2022-06-12 21:41:44.186642
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    """
    test method PlaybookExecutor.run()
    """
    pass



# Generated at 2022-06-12 21:41:49.962738
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    command_line = 'ansible-playbook tests/test_playbook_executor.yml'
    context.CLIARGS = context.CLI.parse()
    loader, inventory, variable_manager = CLI.setup_loader_inventory_variable_manager(context.CLIARGS)
    passwords = {}
    collection = loader.load_collections_from_list([collection_dir()])
    pe = PlaybookExecutor(playbooks=['tests/test_playbook_executor.yml'],
                          inventory=inventory,
                          variable_manager=variable_manager,
                          loader=collection,
                          passwords=passwords)
    result = pe.run()
    assert result is not None
    assert len(result) > 1


# Generated at 2022-06-12 21:41:57.256050
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    #instantiation of dummy objects
    playbooks = []
    inventory = {}
    variable_manager = {}
    loader = {}
    passwords = {}
    #instantiation of class to be tested with dummy objects
    objPlaybookExecutor = PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
    #Meaning of the error code returned by method run of class PlaybookExecutor
    result = objPlaybookExecutor.run()
    assert type(result) is int

# Generated at 2022-06-12 21:41:57.721766
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
  pass

# Generated at 2022-06-12 21:42:05.509056
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    from units.mock.loader import DictDataLoader
    from units.compat import mock

    def _tqm_run(play=None):
        return 1


# Generated at 2022-06-12 21:42:15.752244
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    module = sys.modules[__name__]
    setattr(module, 'CLIARGS', {})

    # Test with playbooks containing static and dynamic includes
    playbooks = ['test_cases/test_playbook_executor/dynamic_include_play.yml',
                 'test_cases/test_playbook_executor/static_include_play.yml']
    context.CLIARGS['start_at_task'] = 'Display hostname, date and time'

    # Test with a 'hosts' value that does not match playbook's 'hosts' value
    variable_manager = VariableManager()
    ads = {}
    variable_manager.extra_vars = {u'hosts': u'myhost1', u'group_names': [u'ungrouped']}

    loader = DataLoader()

# Generated at 2022-06-12 21:42:44.273674
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    '''
    unit test for class PlaybookExecutor
    '''
    def _uniq(lst):
        res = []
        for elem in lst:
            if elem not in res:
                res.append(elem)
        return res

    # collect fixture

# Generated at 2022-06-12 21:42:48.264051
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    plugin_dirs=None
    additional_source_dirs=None
    inventory_filename=None
    rtr=PlaybookExecutor(plugin_dirs, additional_source_dirs, inventory_filename)
    assert rtr is not None
    assert type(rtr) == PlaybookExecutor

# Generated at 2022-06-12 21:42:56.584475
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Let there be
    inventory = 'inventory.py'
    variable_manager = 'variable_manager.py'
    loader = 'loader.py'
    passwords = 'passwords.py'
    playbooks = ['a.yml']
    obj = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    #Execute the code
    obj.run()

#Unittest
if __name__ == '__main__':
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:43:08.364859
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    display = Display()
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = dict()
    cmd_connection = ''
    cmd_timeout = 5
    cmd_ssh_common_args = ''
    cmd_sftp_extra_args = ''
    cmd_scp_extra_args = ''
    cmd_ssh_extra_args = ''
    cmd_verbosity = ''
    cmd_syntax = False
    cmd_check = False
    cmd_listhosts = False
    cmd_listtasks = False
    cmd_listtags = False
    cmd_diff = False
    cmd_tags = 'all'
    inventory = Inventory()
    options = Options()
    args = list()
    contexts = list()

# Generated at 2022-06-12 21:43:16.045845
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Inventory file path
    # FIXME: Get proper inventory file path
    inventory_path = ""
    # Play book file path
    # FIXME: Get proper play book file path
    play_book_path = ""

    # Load inventory file
    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list=inventory_path)
    # Set variable_manager
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    # Load play book file
    play_book = Playbook.load(play_book_path, variable_manager=variable_manager, loader=DataLoader())
    
    # Get play book variable
    variable = play_book.get_variable(host="localhost")
    # Assertions

# Generated at 2022-06-12 21:43:25.188952
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Initialize the arguments that would be passed to the PlaybookExecutor constructor
    playbooks = ["../../../tests/test_data/hello_world.yml"]
    inventory = Inventory(loader=DataLoader(), host_list="../../../tests/test_data/hosts")
    passwords = {}
    variable_manager = VariableManager()

    # Specify password as a parameter to the constructor
    loader = DataLoader()

    # Create an instance of PlaybookExecutor
    pe = PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)

    # Execute the method under test
    result = pe.run()
    assert result == 0

# Generated at 2022-06-12 21:43:26.263471
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    if __name__ == '__main__':
        pass

# Generated at 2022-06-12 21:43:34.084509
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Setup
    playbook_filename = "unit_test_playbook.yml"
    rerun_filename = "unit_test_rerun.retry"
    with open(playbook_filename, "w+") as fd:
        fd.write("- name: test\n  hosts: all\n  tasks:\n" +
                 "  - name: test\n    ping: {}")

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader),
                          host_list=["localhost"])
    variable_manager = VariableManager()
    passwords = {"conn_pass": "testpass"}

# Generated at 2022-06-12 21:43:34.697733
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:43:46.650805
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    PlaybookExecutor_obj = PlaybookExecutor()


if __name__ == '__main__':
    from unit.test_loader import TestLoader
    from unit.test_parser import TestParser
    from unit.test_varsmanager import TestVarsManager
    from unit.test_inventory import TestInventory
    from unit.test_password import TestPassword

    loader = TestLoader()
    parser = TestParser(loader=loader)
    inventory = TestInventory(loader=loader, sources=["/etc/ansible/hosts"])
    test_passwords = TestPassword()

    vars_manager = TestVarsManager(loader=loader, inventory=inventory)


# Generated at 2022-06-12 21:44:09.245763
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:44:17.636135
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Testing with a valid variable manager
    variable_manager = VariableManager(loader=None, inventory=None)
    # Testing with a valid loader
    loader = DataLoader()
    # Testing with ansible_playbook_run=False for ansible_playbook_python
    ansible_playbook_python = AnsiblePlaybookPython(ansible_playbook_run=False)
    # Testing with ansible_playbook_run=False for ansible_playbook_python
    ansible_playbook_python = AnsiblePlaybookPython(ansible_playbook_run=False)
    # Testing with a valid options
    options = Options()
    # Testing with a valid passwords
    passwords = None
    # Testing with a valid playbooks
    playbooks = ['playbook.yml']
    # Testing with a valid inventory

# Generated at 2022-06-12 21:44:18.457128
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:44:20.182372
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass


# Generated at 2022-06-12 21:44:31.867725
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import os
    import tempfile
    from ansible_collections.ansible.community.tests.unit.mock.patch import patch

    from ansible.plugins.loader import action_loader, lookup_loader
    from ansible.plugins.connection.smart import Connection
    from ansible.plugins.strategy.linear import Strategy
    from ansible.plugins.callback.default import CallbackModule
    from ansible import context
    import ansible.constants as C
    import ansible.utils.display as display
    import ansible.utils.path as path

    # to prevent the display module from printing to stdout/stderr
    display.Display.verbosity = 0

    root_dir = os.path.join(os.path.dirname(__file__), 'data', 'test_playbook_executor')
    playbook_path = os

# Generated at 2022-06-12 21:44:36.718485
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # assert len(p.required_together) == 0
    pass

if __name__=='__main__':
    p = PlaybookExecutor()
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:44:38.372844
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
  assert False # TODO: implement your test here


# Generated at 2022-06-12 21:44:39.296482
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    i = PlaybookExecutor(playbooks = '')
    i.run() 
        

# Generated at 2022-06-12 21:44:47.994095
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    '''
    Unit test for method run of class PlaybookExecutor
    '''
    # Build the parser
    # FIXME: need to add short option for inventory (-i)

# Generated at 2022-06-12 21:44:51.924496
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    inventory_path = "tests/integration/inventory"
    playbook_path = "tests/integration/playbook.yml"
    loader = DataLoader()
    variable_manager = VariableManager()

    # Get the inventory
    inventory = InventoryManger(loader, variable_manager, inventory_path)
    variable_manager.set_inventory(inventory)

    # Create the playbook executor instance
    pbex = PlaybookExecutor(playbook_path, inventory, variable_manager, loader, "IncorrectPassword")
    assert pbex.run() == 0

# Generated at 2022-06-12 21:45:36.918571
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():

    pass


# Generated at 2022-06-12 21:45:44.416713
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    class Options(object):
        verbosity = 3
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        connection = 'paramiko'
        module_path = None
        forks = 10
        remote_user = None
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = None
        become_method = None
        become_user = None
        become_ask_pass = None
        become_ask_su_pass = True
        check = False
        timeout = None
        start_at_task = None


# Generated at 2022-06-12 21:45:56.362189
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import json
    import os
    import tempfile
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.vars.manager import VariableManager

    class Display():
        def __init__(self): pass

        def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
            print("Display:", msg)

    class Context():
        class CLIARGS():
            def __init__(self):
                self._args = {}

            def get(self, key):
                return self._args.get(key)

            def __setitem__(self, key, value):
                self._args[key] = value


# Generated at 2022-06-12 21:45:57.004020
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:45:59.771086
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    try:
        pe = PlaybookExecutor([], [], [], [], [])
        pe.run()
    except Exception as e:
        assert(0)

# Generated at 2022-06-12 21:46:07.945353
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import tempfile
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    variable_manager._extra_vars = dict(foo='bar', baz='gaz')

    passwords = dict(
        conn_pass=dict(conn_pass='pass'),
        become_pass=dict(become_pass='pass'),
    )

# Generated at 2022-06-12 21:46:16.039950
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    fake_loader = DictDataLoader({
        "test.yml": "",
        "test1.yml": "",
    })
    fake_loader.set_basedir("/")

    # Test passing one playbook
    pe = PlaybookExecutor('test.yml', None, None, fake_loader, None)
    assert pe.run() == 0

    # Test passing a list
    pe = PlaybookExecutor(['test.yml', 'test1.yml'], None, None, fake_loader, None)
    assert pe.run() == 0

# Generated at 2022-06-12 21:46:24.419183
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    '''
        This test is to test the constructor of class PlaybookExecutor.
        It will check if the parameters passed to constructor are as expected by running a playbook.
    '''

    playbook_path = '../../../test/functional/targets/test.yml'
    inventory_path = '../../../test/functional/inventory'
    extra_vars = {"my_var1": "Goodbye", "my_var2": "World"}

    # Test default value for forks

# Generated at 2022-06-12 21:46:27.613677
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    PlayBookExecutor = PlaybookExecutor()
    result = PlayBookExecutor.run()
    assert result == 0


# Generated at 2022-06-12 21:46:36.564905
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    print('\n>>>>>>>>>> Unit test for method run of class PlaybookExecutor')

    # Create a PlaybookExecutor object
    playbooks = ansible.cli.playbook.PlaybookCLI().parse()[0]
    loader = DataLoader()
    passwords = {}
    inventory = ansible.inventory.InventoryManager(loader=loader,
                                                   sources='localhost,')
    variable_manager = ansible.vars.VariableManager(loader=loader, inventory=inventory)

    playbook_executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    playbook_executor.run()

    print('\n>>>>>>>>>> Unit test for method run of class PlaybookExecutor')



# Generated at 2022-06-12 21:47:25.885664
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    inventory= Inventory('inventory.txt')
    variable_manager=VariableManager('/tmp','dummy')
    loader = DataLoader()
    passwords = dict()
    playbooks = 'test_playbook.yml'

    pe = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    result=pe.run()
    print(result)


if __name__ == '__main__':
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:47:33.979574
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    module_args = {'_ansible_syspath': ['/usr/lib/python3.6/site-packages'], '_ansible_module_builtin': True, '_ansible_module_name': 'json_query', '_raw_params': '{"query": "versions[?name==\'docker\']"}', 'module_args': {'_ansible_check_mode': False, '_ansible_debug': False, '_ansible_diff': False, '_ansible_selectattr': None, '_ansible_string_conversion': 'strict', '_ansible_verbosity': 0, 'expand': False, 'index': None, 'make_list': False, 'query': 'versions[?name==\'docker\']'}}

# Generated at 2022-06-12 21:47:38.614379
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    inventory = None
    variable_manager = None
    loader = None
    passwords = None
    playbooks = None
    expected_result = None
    actual_result = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    assert expected_result == actual_result


# Generated at 2022-06-12 21:47:46.501971
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    # Create a PlaybookExecutor object using dummy data
    playbooks = ['test.yml']
    inventory = api.get_host_list(
        'localhost',
        pattern='localhost'
    )
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = {'conn_pass': 'pass', 'become_pass': 'pass'}
    playbook_executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    # Check if test case pass
    assert playbook_executor.run() == 0

# Generated at 2022-06-12 21:47:56.661116
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    #playbooks = ['/home/gongzhaopeng/shangmei/playbooks/sm-deploy.yml']
    playbooks = ['/home/gongzhaopeng/shangmei/playbooks/sm-deploy-dev.yml']
    #inventory = InventoryManager(loader=loader, sources='/home/gongzhaopeng/shangmei/ansible/hosts/test')
    inventory = InventoryManager(loader=loader, sources='/home/gongzhaopeng/shangmei/ansible/hosts/dev')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    loader = DataLoader()
    passwords = dict(vault_pass='secret')

# Generated at 2022-06-12 21:48:04.033185
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import sys

    sys.modules['ansible'] = MagicMock(return_value=None)
    sys.modules['ansible.cli'] = MagicMock(return_value=None)
    sys.modules['ansible.utils'] = MagicMock(return_value=None)
    sys.modules['ansible.utils.color'] = MagicMock(return_value=None)

    from ansible import context
    from ansible.playbook import Playbook

    context.CLIARGS = {}
    context.CLIARGS['syntax'] = False
    context.CLIARGS['tags'] = []
    context.CLIARGS['skip_tags'] = []
    context.CLIARGS['start_at_task'] = None
    context.CLIARGS['listhosts'] = False
    context.CLI

# Generated at 2022-06-12 21:48:09.203175
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbook_executor = PlaybookExecutor(['/home/mahesh/Desktop/final_assignment/ansible_2.7/module_utils/module_common.py', '/home/mahesh/Desktop/final_assignment/ansible_2.7/module_utils/module_common.py'], '', '', '', '')
    playbook_executor.run()



# Generated at 2022-06-12 21:48:18.149848
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    import unittest
    import sys
    # Test with a fresh inventory
    inventory = InventoryManager(loader=None, sources='localhost,', vault_password=None)
    display.verbosity = 4
    context.CLIARGS = {'syntax': False, 'listhosts': False,
                       'listtags': False, 'listtasks': False, 'start_at_task': False}
    passwords = None
    variable_manager = VariableManager(loader=None, inventory=inventory)
    loader = DataLoader()
    # Test with a fresh inventory
    inventory = InventoryManager(loader=loader, sources='localhost,', vault_password=None)
    display.verbosity = 4

# Generated at 2022-06-12 21:48:19.119770
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass


# Generated at 2022-06-12 21:48:24.955107
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    inventory = Inventory(Loader(), variable_manager=VariableManager())
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = dict(vault_pass='secret')
    playbook_executor = PlaybookExecutor(playbooks=None,inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
    return playbook_executor

test_executor = test_PlaybookExecutor()
print(dir(test_executor))

# Generated at 2022-06-12 21:49:28.209588
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbooks = "E:\Ansible-Repository\practice-projects\ansible\ansible-2.9.12\lib\ansible\parsing\dataloader.py"
    passwords = "E:\Ansible-Repository\practice-projects\ansible\ansible-2.9.12\lib\ansible\parsing\dataloader.py"
    loader = "E:\Ansible-Repository\practice-projects\ansible\ansible-2.9.12\lib\ansible\parsing\dataloader.py"
    variable_manager = "E:\Ansible-Repository\practice-projects\ansible\ansible-2.9.12\lib\ansible\parsing\dataloader.py"

# Generated at 2022-06-12 21:49:28.953335
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:49:40.358079
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    class Options:
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        start_at_task = None
        forks = 10
        force_handlers = False
        step = False
        tags = None
        skip_tags = None
        limit = None
        subset = None
        extra_vars = []
        vault_password = None
        new_vault_password = None
        new_vault_password_file = None
        vault_ids = []
        vault_password_files = []
        inventory = './tests/inventory'
        flush_cache = False
        force_flush_cache = False
        become = None
        become_user = None
        become_method = None
        become_ask_pass = False
        become_ask_sudo_pass = False
        become

# Generated at 2022-06-12 21:49:47.051015
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playlist = Playbook('../../../examples/ansible-playbook-nginx-install.yml')
    print(playlist.hosts)
    print(playlist.name)
    print(playlist.gather_facts)
    for pl in playlist.get_plays():
        print(pl.name)
        print(pl.get_tasks())
        print(pl.get_handlers())
        print(pl.vars)

if __name__ == '__main__':
    test_PlaybookExecutor_run()

# Generated at 2022-06-12 21:49:48.023210
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    PlaybookExecutor()

# Generated at 2022-06-12 21:49:58.127704
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    args = {}
    args['listhosts'] = None
    args['listtags'] = None
    args['listtasks'] = None
    args['syntax'] = None
    args['forks'] = 5
    args['ask_pass'] = False
    args['private_key_file'] = None
    args['ssh_common_args'] = None
    args['ssh_extra_args'] = None
    args['sftp_extra_args'] = None
    args['scp_extra_args'] = None
    args['become'] = None
    args['become_method'] = None
    args['become_user'] = None
    args['verbosity'] = 3
    args['start_at_task'] = None
    args['step'] = None
    args['tags'] = None

# Generated at 2022-06-12 21:50:01.166113
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    p = PlaybookExecutor(playbooks = ['data/test_playbook.yml'], inventory = ['data/inventory'], variable_manager = [''], loader = [''], passwords = [''] )
    p.run()
    assert p is not None

# Generated at 2022-06-12 21:50:05.140654
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    playbooks = ['ansible/playbooks/hello.yml']
    inventory = Inventory(loader=None, variable_manager=None, host_list='ansible/inventory.ini')
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = dict(vault_pass='secret')
    pbe = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    pbe.run()

# Generated at 2022-06-12 21:50:05.816909
# Unit test for method run of class PlaybookExecutor
def test_PlaybookExecutor_run():
    pass

# Generated at 2022-06-12 21:50:07.186201
# Unit test for constructor of class PlaybookExecutor
def test_PlaybookExecutor():
    pass