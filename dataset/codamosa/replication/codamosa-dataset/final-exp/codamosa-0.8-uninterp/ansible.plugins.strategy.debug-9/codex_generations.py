

# Generated at 2022-06-13 14:55:39.891162
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug
    from ansible.playbook import Playbook
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager

    tqm = TaskQueueManager(
            inventory=InventoryManager(host_list=['hosts']),
            playbook=Playbook.load('./test/data/err.yml'),
            stdout_callback="default",
            options=None,
            loader=None,
            passwords=None,
        )
    strategy = ansible.plugins.strategy.debug.StrategyModule(tqm)
    print(strategy.debugger_active) # prints True
    tqm.run()


# Generated at 2022-06-13 14:55:50.655756
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.plugins.loader import find_plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

# Generated at 2022-06-13 14:55:51.383500
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()



# Generated at 2022-06-13 14:55:51.868000
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None


# Generated at 2022-06-13 14:55:55.609533
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.constants as C
    import ansible.utils.display as D
    mock_tqm = C.TEST_TASK_QUEUE_MANAGER
    mod = StrategyModule(mock_tqm)
    assert mod.debugger_active == True


# Generated at 2022-06-13 14:56:00.692136
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm={"tasks": [
        {"name": "try_me", "action": {"module": "omg", "args": ["a", "b"]}},
        {"name": "try_me_again", "action": {"module": "lol", "args": {"a": "b"}}}
    ]})



# Generated at 2022-06-13 14:56:08.626305
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.module_utils.common._collections_compat import MutableMapping  # pylint: disable=import-error
    import ansible.constants as C
    import ansible.executor.task_queue_manager as TQM
    import ansible.vars.manager as  VM

    sys.modules['ansible.vars.manager'] = VM # pylint: disable=no-member
    sys.modules['ansible.module_utils.common._collections_compat'] = MutableMapping
    sys.modules['ansible.constants'] = C

    #sys.modules['ansible.executor.task_queue_manager'] = TQM
    sys.modules['ansible.plugins.connection.chroot'] = None
    sys.modules['ansible.plugins.connection.local'] = None
   

# Generated at 2022-06-13 14:56:10.093318
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None


# Generated at 2022-06-13 14:56:18.704838
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Basically setup() of taks_queue_manager.py
    config = [{'host': 'host1', 'port': 'port1'}, {'host': 'host2', 'port': 'port2'}]
    connections = ['paramiko', 'ssh', 'local']
    passwords = dict()
    # Setup the terminal width
    try:
        terminal_width = int(os.environ['COLUMNS'])
    except (KeyError, ValueError):
        try:
            # os.sysconf() is not available on all platforms
            terminal_width = int(os.sysconf('SC_CONSOLE_WIDTH'))
        except (OSError, ValueError):
            terminal_width = 80

    new_stdin = open(os.devnull, 'r')

# Generated at 2022-06-13 14:56:21.513916
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'a'
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm
    assert sm.debugger_active == True

# We use a custom runner for debugging, so we don't use a normal host/job queue
# but implement our own.


# Generated at 2022-06-13 14:56:23.635482
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  sm = StrategyModule()
  assert sm.debugger_active == True


# Generated at 2022-06-13 14:56:27.410294
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:56:28.066326
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 14:56:29.646662
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  print("Test of class StrategyModule")
  StrategyModule()



# Generated at 2022-06-13 14:56:39.385766
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 14:56:49.756851
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Unit test for StrategyModule constructor
    """
    class TQM(object):
        class VarsDict(object):
            class AnsibleHost(object):
                def __init__(self, task, result):
                    self.task = task
                    self.result = result
                def run(self):
                    return (self.task, self.result)

            def __init__(self, result):
                self.result = result

            def __getitem__(self, task):
                return self.AnsibleHost(task, self.result)

        def __init__(self, result):
            self.result = result
        def __getitem__(self, key):
            return self.VarsDict(self.result)
        def cleanup(self):
            return "{} is cleanup"

    tqm = T

# Generated at 2022-06-13 14:56:52.696026
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert tqm.__dict__ == {}
    assert StrategyModule(tqm).debugger_active == True


# Generated at 2022-06-13 14:56:53.958359
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(object)



# Generated at 2022-06-13 14:56:57.657201
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule({'name': 'test', 'enabled': 'yes', 'subset': None, 'subset_count': None, 'start_at_task': None})
    assert strategy_module != None
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:56:58.555831
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:57:03.683064
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TaskQueueManager:
        def __init__(self):
            self.stats = None
        def get_inventory(self):
            return None
        def get_variable_manager(self):
            return None
        def get_loader(self):
            return None
    tqm = TaskQueueManager()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:57:07.823369
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #print('StrategyModule unit test test_StrategyModule()')
    #tqm = StrategyModule(tqm)
    #assert 'tqm = StrategyModule.__init__(tqm)'

    print('StrategyModule unit test test_StrategyModule() not implemented')


# Generated at 2022-06-13 14:57:08.703930
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('tqm')


# Generated at 2022-06-13 14:57:18.801421
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler_task_list import HandlerTaskList
    from ansible.executor.task_queue_manager import TaskQueueManager

    play = Play()
    play_context = PlayContext()
    task = Task()
    task._role = None
    task._block = Block(parent_block=play)
    play.handlers = HandlerTaskList(play=play, block=play._entries)
    play.post_validate()


# Generated at 2022-06-13 14:57:19.742058
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 14:57:30.740480
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# End of Unit test for constructor of class StrategyModule

    def pager(self, lines):
        # this used to use shell for each line, but it's much more
        # efficient to just use shell once, since we're not paging
        # this could be improved further by storing process output
        # and using popen.communicate(output)[0]
        with open('/dev/tty', 'w') as dev_tty:
            dev_tty.write('\n'.join(lines))

    def run(self, iterator, play_context):
        result = super(StrategyModule, self).run(iterator, play_context)
        self.default_pager(iterator)
        return result


# Generated at 2022-06-13 14:57:42.719318
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestClass:
        def __init__(self):
            self.inventory = None
            self.variable_manager = None
            self.loader = None
            self.options = None
            self.passwords = None
            self.callback = None
            self.__callbacks = []
            self._tqm_stdout_handle = None
            self.stdout_callback = None
            self.failed_hosts = {}
            self.stats = {}
            self.run_additional_callbacks = True

    class Play:
        def __init__(self):
            self.roles = []

    class Playbook:
        def __init__(self):
            self.workspace = None

    tqm = TestClass()
    tqm.loader = TestClass()
    tqm.loader.get_basedir

# Generated at 2022-06-13 14:57:43.420965
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:57:44.431754
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:57:48.649050
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test case:
    #    tqm = ...
    #    StrategyModule = StrategyModule(tqm)
    #
    # Test result:
    #    StrategyModule.debugger_active == True
    dummy = None
    strategy_module = StrategyModule(dummy)
    assert(strategy_module.debugger_active)



# Generated at 2022-06-13 14:57:54.660472
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test = StrategyModule(None)
    assert test.debugger_active == True
    return True


# Generated at 2022-06-13 14:58:04.194342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from ansible.module_utils._text import to_text
    except ImportError:
        from ansible.module_utils._text import to_bytes as to_text
    from ansible.errors import AnsibleError, AnsibleConnectionFailure
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude, Include
    from ansible.playbook.task import Task
    from ansible.plugins import strategy_loader
    from ansible.template import Templar

    module_loader, names, paths = strategy_loader.all(class_only=True)
    # Test StrategyModule

# Generated at 2022-06-13 14:58:04.842892
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 14:58:08.379677
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule("test_tqm")
    sm_dict = sm.__dict__
    assert sm_dict["debugger_active"] == True
    assert sm_dict["tqm"] == "test_tqm"



# Generated at 2022-06-13 14:58:11.041216
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestAnsibleTQM(object):
        pass

    strategy = StrategyModule(TestAnsibleTQM())
    assert strategy.debugger_active



# Generated at 2022-06-13 14:58:12.412997
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    StrategyModule(tqm)


# Generated at 2022-06-13 14:58:23.976284
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Test_tqm(object):
        def __init__(self, hosts, inventory, variable_manager, loader, options, passwords, stdout_callback=None, run_additional_callbacks=True, run_tree=False, tags=None, skip_tags=None, one_line=None):
            self.hosts = hosts
            self.inventory = inventory
            self.variable_manager = variable_manager
            self.loader = loader
            self.options = options
            self.passwords = passwords
            self.stdout_callback = stdout_callback
            self.run_additional_callbacks = run_additional_callbacks
            self.run_tree = run_tree
            self.tags = tags
            self.skip_tags = skip_tags
            self.one_line = one_line


# Generated at 2022-06-13 14:58:30.490812
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("# Unit test for constructor of class StrategyModule")
    try:
        cmd.Cmd()
    except NameError:
        try:
            class Cmd2(cmd.Cmd):
                pass
        except:
            pass

    tm = None
    try:
        tm = cmd.Cmd()
    except NameError:
        try:
            tm = Cmd2()
        except:
            pass

    sm = StrategyModule(tm)
    assert(isinstance(sm, LinearStrategyModule))
    assert(isinstance(sm, object))



# Generated at 2022-06-13 14:58:31.652699
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: How to implement unit test for subclass of BaseStrategyModule?
    pass



# Generated at 2022-06-13 14:58:33.797450
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    debug_module = StrategyModule(None)
    assert isinstance(debug_module, LinearStrategyModule) is True
    assert debug_module.debugger_active is True



# Generated at 2022-06-13 14:58:43.185658
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:58:44.377234
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=1)


# Generated at 2022-06-13 14:58:44.779951
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:48.496720
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    if __name__ == '__main__':
        print('in __main__')
    else:
        print('not in __main__')
    class TestClass:
        def __init__(self):
            self.TEST = 'TEST1'
            self.TEST2 = 'TEST2'
    tqm = TestClass()
    sm = StrategyModule(tqm)
    print('sm.debugger_active=>')
    pprint.pprint(sm.debugger_active)



# Generated at 2022-06-13 14:58:51.640994
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import ansible.plugins.strategy.debug as debug_mod
    except ImportError:
        return
    s = debug_mod.StrategyModule(tqm={})
    assert  s.debugger_active == True


# Generated at 2022-06-13 14:58:52.924149
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('tqm')


# Generated at 2022-06-13 14:58:53.689624
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 14:58:57.630311
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = dict()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True
    assert tqm == strategy_module.tqm
    assert tqm == strategy_module.tqm


# Generated at 2022-06-13 14:59:03.366926
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = {'id': 'test_StrategyModule'}

    sm = StrategyModule(test_tqm)
    assert sm._tqm == test_tqm
    assert sm._display == None
    assert sm._fail_hosts == []
    assert sm._unreachable_hosts == []
    assert sm._completed_hosts == []
    assert sm._pending_results == 0
    assert sm._cur_worker == 0
    assert sm._total_workers == 5


# Generated at 2022-06-13 14:59:08.855898
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class test_tqm():
        def __init__(self):
            self.host_list = [
                '192.168.1.1',
                '192.168.1.2',
                ]
    tqm = test_tqm()
    result = StrategyModule(tqm)
    assert result.debugger_active is True


# Generated at 2022-06-13 15:00:02.772282
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # check if the constructor raises an exception
    # you can use the doctest or unittest module
    pass



# Generated at 2022-06-13 15:00:04.447533
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule('Test')
    assert s.debugger_active


# Generated at 2022-06-13 15:00:07.302449
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Constructor of class StrategyModule
    :return:
    """
    tqm = None
    linear = StrategyModule(tqm)

    assert linear



# Generated at 2022-06-13 15:00:15.910536
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug as debug
    import ansible.playbook.play
    import ansible.playbook.task_include

    playbook = ansible.playbook.play.Play().load(dict(
            name = "testing debug mode",
            hosts = 'all',
            gather_facts = 'no',
            tasks = [
                ansible.playbook.task_include.TaskInclude(
                    static  = 'yes',
                    tasks   = [ 'debug_me.yml' ]
                )
            ]
        ), vault_password='password')
    assert playbook.name == "testing debug mode"
    assert playbook.hosts == 'all'
    assert playbook.gather_facts == 'no'
    assert playbook.tasks[0].static == 'yes'
    assert playbook.tasks[0].t

# Generated at 2022-06-13 15:00:17.217636
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm)
    


# Generated at 2022-06-13 15:00:18.089121
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm)


# Generated at 2022-06-13 15:00:22.167045
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # calling constructor method
    StrategyModule()

    # calling member methods
    module.run()

    # calling member variables
    module.debugger_active
    module.tqm

# test for each methods of class StrategyModule

# Generated at 2022-06-13 15:00:25.773907
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_list = 'localhost'
    tqm = 'tqm'
    strategy = StrategyModule(tqm)
    # TODO: Make more test data
    assert strategy.debugger_active == True


# Generated at 2022-06-13 15:00:29.362164
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTqm: pass
    tqm = TestTqm()
    strategymodule = StrategyModule(tqm)
    assert strategymodule.debugger_active == True

# Unit test class cmd.Cmd
# Use to work with unit tests

# Generated at 2022-06-13 15:00:30.857390
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MockTQM()
    StrategyModule(tqm)


# Generated at 2022-06-13 15:04:02.619183
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:04:05.577218
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    context = {'play_context': {'extra_vars': {}}}
    task = {'id': 'id'}
    loader = None
    inventory = None
    play_context = None
    tqm = None
    s = StrategyModule(tqm)
    s.run(loader, inventory, play_context, task)
# end unit test

# Generated at 2022-06-13 15:04:06.297336
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:04:07.533811
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        StrategyModule(None)
    except:
        return True
    return False



# Generated at 2022-06-13 15:04:08.870117
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 15:04:11.889423
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    return (True)


# Generated at 2022-06-13 15:04:14.112091
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:04:15.310106
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:04:17.124357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("using " + StrategyModule.__name__)



# Generated at 2022-06-13 15:04:20.050690
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Execute method
    StrategyModule.__init__('tqm')
    # Test if all attributes was initialized
    try:
        assert StrategyModule.debugger_active == True
    except AssertionError as e: raise(e)
