

# Generated at 2022-06-13 11:11:59.545830
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def _get_task():
        class _Task(object):
            def __init__(self):
                self.args = dict()
        return _Task()

    def _get_play_context():
        class _PlayContext(object):
            def __init__(self):
                self.check_mode = False
        return _PlayContext()

    class _Connection(object):
        def __init__(self):
            self._shell = _get_shell()

    class _Shell(object):
        def __init__(self):
            self.tmpdir = '/my/tmpdir'

    def _get_shell():
        return _Shell()

    class _ActionBase(object):
        def __init__(self):
            self._task = _get_task()
            self._connection = _Connection()
            self._play_context

# Generated at 2022-06-13 11:12:04.077560
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {}
    result['_ansible_verbose_override'] = True
    actionmod = ActionModule(None, {}, result=result)
    actionmod.DEFAULT_SLEEP = 1
    actionmod.DEFAULT_TIMEOUT = 10

    # test timeout
    with pytest.raises(TimedOutException):
        actionmod.do_until_success_or_timeout(lambda: True, 1, 1, "timeout")

# Generated at 2022-06-13 11:12:10.883973
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # Success case - test should run 6 times before success
    def success_test(timeout):
        ''' Test function which succeeds after 6 attempts '''
        success_test.call_count += 1
        if success_test.call_count == 6:
            return
        raise Exception('success test failure')

    success_test.call_count = 0
    try:
        am = ActionModule()
        am.do_until_success_or_timeout(success_test, 10, 2, "success_test", sleep=1)
        assert(success_test.call_count == 6)
    except TimedOutException as e:
        assert(False)

    # Failure case - test should run 3 times before timeout
    def failure_test(timeout):
        ''' Test function which fails '''
        raise Exception('failure test failure')


# Generated at 2022-06-13 11:12:13.723095
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(conn=None, tmp=None, task=None, task_vars=None)

    assert action_module.TRANSFERS_FILES == False
    assert action_module._VALID_ARGS == frozenset(('connect_timeout', 'delay', 'sleep', 'timeout'))

# Generated at 2022-06-13 11:12:23.553583
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of class ActionModule with the passed arguments
    act = ActionModule(dict(
      connection='ansible.connection.ssh',
      job_id=0,
      play=dict(hosts=dict('hostname'),
                name='play name',
                roles=list()),
      play_context=dict(
        check_mode=False,
        become=False,
        become_method='sudo',
      ),
      role_name=None,
      task=dict(action=dict(), args=dict(), delegated_vars=dict()),
      task_vars=dict(),
    ))
    # Create a test variable to test method run of class ActionModule
    test_task_vars = dict()

    # Test method run of class ActionModule
    act.run(None, test_task_vars)

# Generated at 2022-06-13 11:12:29.819537
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # In the future, when methods like the following:
    #    class ActionModule(object):
    #        def xxx(self, yyy):
    #            return yyy
    # are converted to properties like this:
    #    class ActionModule(object):
    #        @property
    #        def xxx(self):
    #            return self._xxx
    #        @xxx
    #        def xxx(self, yyy):
    #            self._xxx = yyy
    # these unit tests will fail, so convert the unit tests.
    # For now, method calls like 'xxx(yyy)' can be used until these methods become properties.
    import pytest
    from ansible.plugins.action.wait_for_connection import ActionModule
    m = ActionModule()
    # Module methods, no need to initialize
    m.run

# Generated at 2022-06-13 11:12:30.221162
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 11:12:36.056369
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModule_run_UnitTest(ActionModule):
        from ansible.module_utils.basic import AnsibleModule

        def __init__(self, *args):
            super(ActionModule_run_UnitTest, self).__init__(*args)
            self._execute_module_args_orig = self._execute_module_args

        def _execute_module_args(self, *args, **kwargs):
            if args[0] == 'ansible.legacy.ping':
                # Do not execute real ping module
                return dict(ping='pong')
            else:
                # Call original _execute_module_args
                return self._execute_module_args_orig(*args, **kwargs)

        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task

# Generated at 2022-06-13 11:12:45.637233
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # mock task to avoid setting up a task object
    task_mock = mock.Mock()
    task_mock.args.copy.return_value = {}
    task_mock.args.update.return_value = {}
    task_mock.get_data.return_value = {}

    # instantiate a mocked connection
    connection_mock = mock.Mock()
    connection_mock.reset.return_value = True
    connection_mock.transport_test.return_value = True

    # mock play_context
    play_context = mock.Mock()
    play_context.check_mode = False

    # use a real Display() instance to get better test coverage
    display_instance = Display()

    # instantiate our class

# Generated at 2022-06-13 11:12:55.107354
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(ansible_ssh_host='127.0.0.1',
                     ansible_ssh_port=22,
                     ansible_ssh_user='root',
                     ansible_ssh_private_key_file='/root/.ssh/id_rsa')
    def _execute_module():
        return dict(ping='pong')

    action_module_instance = ActionModule(task=dict(action=dict(args=dict())),
                                          connection=dict(module_implementation_preferences=[]),
                                          task_vars=task_vars,
                                          loader=None,
                                          templar=None,
                                          shared_loader_obj=None)

    action_module_instance._execute_module = _execute_module
    assert action_module_instance.run