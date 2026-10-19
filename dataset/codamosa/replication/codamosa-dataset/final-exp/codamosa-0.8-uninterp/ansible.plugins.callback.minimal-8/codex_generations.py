

# Generated at 2022-06-13 11:51:37.759828
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import unittest
    import tempfile
    import shutil
    import textwrap
    from ansible.plugins.callback import CallbackBase

    class TestCallbackModule(CallbackBase):
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'bin'

        def __init__(self):
            self.captured = []

        def v2_on_file_diff(self, result):
            self.captured.append(result._result['diff'])


    base = tempfile.mkdtemp()
    orig = tempfile.NamedTemporaryFile(suffix=".orig", dir=base)
    new = tempfile.NamedTemporaryFile(suffix=".new", dir=base)


# Generated at 2022-06-13 11:51:43.984363
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    module = CallbackModule()
    import json
    data = {
        "after": "", 
        "before": "", 
        "diff": [
            "--- /Users/befaird/test_path/test.template\t2019-09-18 14:27:17.000000000 +0800\n", 
            "+++ /Users/befaird/.ansible_module_generated/tmpv1BDCF#Fri Sep 20 11:01:38 CST 2019\n", 
            "@@ -1 +1 @@\n", 
            "-{{ name }}\n", 
            "+test\n"
        ]
    }
    result = lambda : None
    result._result = data

    assert module.v2_on_file_diff(result) == None



# Generated at 2022-06-13 11:51:44.784181
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = Callb

# Generated at 2022-06-13 11:51:55.780110
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import json
    import unittest
    import warnings
    from datetime import datetime

    from ansible.utils.color import stringc
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    from ansible.plugins.loader import callback_loader

    loader = DataLoader()
    group = Group('g1')
    group.set_variable_manager(VariableManager(loader=loader))

    args = {}
    args['connection'] = 'ssh'
    args['tid'] = 1
    args['subset'] = None

# Generated at 2022-06-13 11:52:08.297307
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = {'_ansible_parsed': True, '_ansible_verbose_always': True, '_ansible_no_log': False, '_ansible_item_label': 'item_name', 'changed': True, 'invocation': {'module_args': {'name': 'my_name'}, 'module_name': 'my_module'}, 'item': {'key': 'value'}, 'module_name': 'my_module', 'task': 'tasks/main.yml:13', 'tasks': [{'action': {'__ansible_arguments__': ['test.py', 'arg1'], '__ansible_module__': 'test.py'}, 'async': 12345, 'async_val': 10}], 'stdout': 'my_module'}

# Generated at 2022-06-13 11:52:13.228755
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Instantiate class of CallbackModule
    c = CallbackModule()

    # test_display_ok
    pin = {'changed': True}
    result = {'_result': pin}
    assert c.v2_runner_on_ok(result)
    pout = {'changed': False}
    result = {'_result': pout}
    assert c.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:52:23.588492
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # arrange
    cmd_result = dict()
    cmd_result['stdout'] = '''
    diff --git a/testfile b/testfile
    index 30f39cd..7a9b43c 100644
    --- a/testfile.txt
    +++ b/testfile.txt
    @@ -1,7 +1,5 @@
    -
    -abcdefghijklmnopqrstuvwxyz
    -1234567890
    -abcdefghijklmnopqrstuvwxyz
    -1234567890
    -abcdefghijklmnopqrstuvwxyz
    -1234567890
    +1234567890
    '''
    result = dict()

# Generated at 2022-06-13 11:52:25.049738
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cbm = CallbackModule()
    assert isinstance(cbm, CallbackModule)

# Generated at 2022-06-13 11:52:28.859373
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    result = {'diff': '[{"encoding": "string", "src": "file1.txt", "diff": "+ file1.txt", "dst": "file1.txt"}]'}
    diff = CallbackModule()._get_diff(result['diff'])
    print('%s' % diff)
    assert(diff == '--- before\n+++ after\n@@ -1 +1,2 @@\n+ file1.txt')

# Generated at 2022-06-13 11:52:36.542966
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback_module = CallbackModule()
    callback_module._display = DummyDisplay()
    result = DummyResult()
    result._result = dict(changed=True)
    callback_module.v2_runner_on_ok(result)
    assert callback_module._display.out == "SUCCESS! => {'changed': True}"
    result._result = dict(changed=False)
    callback_module.v2_runner_on_ok(result)
    assert callback_module._display.out == "SUCCESS! => {'changed': False}"


# Generated at 2022-06-13 11:52:50.149830
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    class TestCallbackModule(CallbackModule):
        def __init__(self):
            self._display = display = Display()
            super(TestCallbackModule, self).__init__(display)

    c = TestCallbackModule()
    c.v2_on_file_diff({'diff':'fake diff'})
    assert c._display.data[0] == 'fake diff'


    c = TestCallbackModule()
    c.v2_on_file_diff({'diff':''})
    assert c._display.data[0] == ''




# Generated at 2022-06-13 11:53:00.774879
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    ''' Unit test for method v2_runner_on_ok '''

    import unittest
    import Display
    import RunnerResults
    import Result

    class TestClass(unittest.TestCase):
        def test_set_vars(self, display=Display.Display(), results=Result.Result(RunnerResults.RunnerResults(), 'ok')):
            from Callbacks import CallbackModule
            cb = CallbackModule(display)

        def test_display(self, display=Display.Display(), results=Result.Result(RunnerResults.RunnerResults(), 'ok')):
            from Callbacks import CallbackModule
            cb = CallbackModule(display)
            cb.v2_runner_on_ok(results)

    unittest.main(verbosity=2)

if __name__ == '__main__':
    test_

# Generated at 2022-06-13 11:53:11.544377
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # get Ansible callback object
    callback_obj = CallbackModule()

    # object of class host used as parameter
    class host:

        def get_name(self):
            return "host"
    
    # object of class event used as parameter
    class event:

        def __init__(self):
            self.action = "validate"

    # object of class TaskResult used as parameter
    class TaskResult:

        def __init__(self):
            self.task = event()
            self.host = host()
            self.result = {}

        # '_result' parameter is used for result dictionary
        def _result(self):
            self.result = {
                "rc": -1,
                "stdout": "",
                "stderr": "",
                "msg": ""
            }


# Generated at 2022-06-13 11:53:12.702695
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule()

# Generated at 2022-06-13 11:53:22.259223
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    #Input data
    test_data = [{
                    u'stdout': u'',
                    u'stdout_lines': [],
                    u'changed': True,
                    "invocation": {
                        "module_args": {
                            "_raw_params": "",
                            "_uses_shell": False,
                            "chdir": None,
                            "creates": None,
                            "executable": None,
                            "removes": None,
                            "warn": True
                        }
                    },
                    "item": "",
                    "rc": 0
                }]

    #Expected output
    expected_result = [u'local1 | CHANGED => \n{}\n']

    #Code to be tested
    callback = CallbackModule()
    for item in test_data:
        result = callback

# Generated at 2022-06-13 11:53:25.653004
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    '''
    Test Case for class CallbackModule
    '''
    from ansible.plugins.callback import CallbackModule

    # Test Case for constructor
    cm = CallbackModule()
    assert isinstance(cm, CallbackModule)

# Generated at 2022-06-13 11:53:36.756414
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from collections import namedtuple
    setattr(C, "COLOR_OK", '\033[32m')

    class Display():
        def __init__(self):
            self.output = []
        def display(self, msg, color=None):
            self.output.append(msg)

    class Result():
        def __init__(self):
            self._result = {'changed': True}
            self._host = namedtuple('Host', ['get_name'])('hostname')
            self._task = namedtuple('Task', ['action'])(action='action')

    d = Display()
    r = Result()
    cb = CallbackModule()
    cb._display = d
    cb.v2_runner_on_ok(r)

# Generated at 2022-06-13 11:53:46.843203
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    """This is a unit test for the constructor of the class CallbackModule. """
    # pylint: disable=protected-access
    assert CallbackModule.__dict__['__module__'] == __name__
    assert CallbackModule.__dict__['__doc__'] == """\
    This is the default callback interface, which simply prints messages
    to stdout when new callback events are received.
    """
    assert CallbackModule.__init__.__doc__ == """Constructor"""
    assert "CallbackBase" in CallbackModule.__bases__

    assert CallbackModule.CALLBACK_VERSION == 2.0
    assert CallbackModule.CALLBACK_TYPE == 'stdout'
    assert CallbackModule.CALLBACK_NAME == 'minimal'

    assert CallbackModule._display == None

    assert CallbackModule.v2

# Generated at 2022-06-13 11:53:56.853081
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from mock import Mock
    cb = CallbackModule()
    cb._handle_exception = Mock()
    cb._handle_warnings = Mock()
    cb._display = Mock()
    cb._command_generic_msg = Mock()
    cb._dump_results = Mock()
    import ansible.constants as C
    C.MODULE_NO_JSON = ['shell']
    result = Mock()
    result._task = Mock()
    result._task.action = 'shell'
    result._result = {
        'rc': 1,
        'stdout': '',
        'stderr': '',
        'msg': ''
    }
    result._host = Mock()
    result._host.get_name.return_value = 'foo'

# Generated at 2022-06-13 11:53:57.612358
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass

# Generated at 2022-06-13 11:54:15.547493
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    plugin = CallbackModule()
    fake_host = {'hostname': 'fakehost'}
    result = {'stdout': 'output', 'stderr': 'error', 'msg': 'msg'}
    expected_output = fake_host['hostname'] + " | " + "SUCCESS => " + '\n' + \
        "    " + "stdout: " + '\n' + \
        "    " + "  " + result['stdout'] + '\n' + \
        "    " + "stderr: " + '\n' + \
        "    " + "  " + result['stderr'] + '\n' + \
        "    " + "msg: " + '\n' + \
        "    " + "  " + result['msg'] + '\n'

# Generated at 2022-06-13 11:54:22.353574
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Given
    class FakeDisplay:
        def __init__(self):
            self.result = None

        def display(self, result, color):
            self.result = result

    fake_result = FakeResult(True)
    display = FakeDisplay()

    # When
    callback_module = CallbackModule()
    callback_module._display = display
    callback_module.v2_runner_on_ok(fake_result)

    # Then
    assert display.result == "127.0.0.1 | SUCCESS => {'changed': True}"


# Generated at 2022-06-13 11:54:29.823934
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    an = "an"

# Generated at 2022-06-13 11:54:42.750300
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Create a mock object, with some attributes set
    mock = CallbackModule()
    mock._handle_exception = lambda x: None
    mock._handle_warnings = lambda x: None
    mock._clean_results = lambda x, y: None
    mock._display = "mocked_display"
    mock._dump_results = lambda x, y: "mocked_dump_results"
    mock._command_generic_msg = lambda x, y, z: "mocked_command_generic_msg"

    # Create a class instance, which would be passed to v2_runner_on_failed
    class RunnerOnFailedResultMock():
        def __init__(self):
            self._result = {
                "changed": False
            }
            self._task = RunnerOnFailedTaskMock()
            self._host = RunnerOnF

# Generated at 2022-06-13 11:54:43.475564
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass

# Generated at 2022-06-13 11:54:52.000194
# Unit test for method v2_runner_on_failed of class CallbackModule

# Generated at 2022-06-13 11:55:00.331370
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Arrange
    from ansible.plugins.callback import CallbackBase

    class FakeResult(object):
        _host = "hostname"
        _task = "task"
        _result = "result"

    fake_result = FakeResult()

    class FakeDisplay():
        def display(self, msg, color=None):
            self.msg = msg

    fake_display = FakeDisplay()

    class FakeClass(CallbackBase):
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'minimal'

        def __init__(self):
            self._display = fake_display

    sut = FakeClass()

    # Act
    sut.v2_runner_on_failed(fake_result)

    # Assert
    assert sut.CALLBACK_VERSION

# Generated at 2022-06-13 11:55:01.505052
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    assert False



# Generated at 2022-06-13 11:55:11.268928
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    """Unit test for method v2_on_file_diff of class CallbackModule"""
    from ansible.utils.display import Display
    import sys
    display = Display()
    callback = CallbackModule()
    callback.set_options(display=display, options={'verbosity': 0, 'diff': False, 'tree': None})
    callback.set_runner(runner=None)
    diff = {
       'after': '',
       'before': '',
       'before_header': 'test_file',
       'after_header': 'test_file'}
    result = {'diff': diff}

    callback.v2_on_file_diff(result=result)

# Generated at 2022-06-13 11:55:13.028665
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pytest.fail("No test for this method")


# Generated at 2022-06-13 11:55:31.844102
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    '''Test modules.callback.CallbackModule.test_CallbackModule_v2_on_file_diff()'''

    # Create a CallbackModule
    callback_module = CallbackModule()

    # Provide a result
    result = {'diff': {
                    'after': 'foo\nbar',
                    'before': 'bar\nfoo',
                    'before_header': 'before.txt',
                    'after_header': 'after.txt'
                  }}

    # Assert that the result is displayed
    callback_module._display.display = mock.Mock()
    callback_module.v2_on_file_diff(result)
    assert callback_module._display.display.called is True


# Generated at 2022-06-13 11:55:41.210552
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.parsing.ajson import AnsibleJSONEncoder, AnsibleJSONDecoder

    class Result:
        def __init__(self, result=None):
            self._result = result
        
        def __getattr__(self, attr):
            return self._result[attr]

    def get_result_from_file(filename):
        with open(filename) as f:
            return AnsibleJSONDecoder(from_text=to_text).decode(f.read())
        return None

    def create_result_from_file_diff(from_file, to_file):
        result = get_result_from_file(from_file)
        result['diff'] = get_result_from_file(to_file)


# Generated at 2022-06-13 11:55:49.400799
# Unit test for method v2_runner_on_ok of class CallbackModule

# Generated at 2022-06-13 11:55:51.960313
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():

    def _get_diff(diff):
        return 1

    cb = CallbackModule()
    cb._get_diff = _get_diff

    class DiffResult:
        _result = {'diff': 1}

    cb.v2_on_file_diff(DiffResult)

# Generated at 2022-06-13 11:56:01.292463
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    display = C.Display()
    display.display = lambda msg, color: (msg)
    dummy_call = CallbackModule(display, 'minimal')

    result = {'foo': 'bar'}
    result._result = {'ansible_job_id': '12345'}
    result._host = {'get_name': lambda : 'hostname'}
    result._task = {'action': 'setup'}

    dummy_call._clean_results(result._result, result._task.action)

    dummy_call._handle_warnings(result._result)

    assert dummy_call.v2_runner_on_ok(result) == "hostname | SUCCESS => {\n    \"foo\": \"bar\"\n}"

# Generated at 2022-06-13 11:56:10.274708
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    c = CallbackModule()
    c.C = C
    c.show_custom_stats = False
    c.display = DummyDisplay()
    result = DummyResult()
    result._result = dict()
    result._result['diff'] = """
--- before
+++ after
@@ -1,2 +1,1 @@
-1
-2
+3
        """
    c.v2_on_file_diff(result)
    print(c.C.COLOR_DIFF_ADD, c.C.COLOR_DIFF_REMOVE, c.C.COLOR_DIFF_LINES)

# Generated at 2022-06-13 11:56:11.635435
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    output = ""
    module = CallbackModule()

# Generated at 2022-06-13 11:56:21.466567
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    #Testing a basic test-case for the given function
    #Input data
    #Output data

    test_class = CallbackModule()

    #Testing a basic test-case for the given function
    result = dict()
    result['stdout'] = 'conftest.py'
    result['stderr'] = 'conftest.py'
    result['msg'] = 'conftest.py'
    result['rc'] = 0

    result['changed'] = False
    result['_ansible_no_log'] = False


# Generated at 2022-06-13 11:56:31.761229
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Testing a successful command, with color enabled
    cb = CallbackModule()
    result = {
            u'ansible_facts': {},
            u'changed': False,
            u'invocation': {},
            u'rc': 0,
            u'stdout': u'',
            u'stdout_lines': []
        }
    cb._display.display(
        'hostname | SUCCESS => {\n    "ansible_facts": {}, \n    "changed": false, \n    "invocation": {}, \n    "rc": 0, \n    "stdout": "", \n    "stdout_lines": []\n}\n', 'ok'
    )
    cb.display = lambda x, y: (x, y)
    assert cb.v2_runner_on_ok

# Generated at 2022-06-13 11:56:32.367038
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:57:04.636462
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # CallbackModule_v2_on_file_diff() uses self._display.display(),
    # which is an instance of Display() class defined in plugins/callback/__init__.py.
    # Display() has a wrapper around it and we have a test file for that,
    # we will not test this method in detail.

    # Initialization
    stdout = []
    cb = CallbackModule(stdout)
    cb._display = Display(verbosity=0)
    # Call the method
    cb.v2_on_file_diff({})
    # Verify
    assert not stdout

# Generated at 2022-06-13 11:57:10.633737
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    # Testing constructor of CallbackModule
    module = CallbackModule()
    assert len(module.CALLBACK_VERSION) > 0
    # Callback version must be a float
    assert isinstance(module.CALLBACK_VERSION, float)
    assert len(module.CALLBACK_TYPE) > 0
    # Callback type must be a string
    assert isinstance(module.CALLBACK_TYPE, str)
    assert len(module.CALLBACK_NAME) > 0
    # Callback name must be a string
    assert isinstance(module.CALLBACK_NAME, str)
    assert len(module.CALLBACK_DEPRECATED_WARNING) >= 1
    # Callback deprecated warning must be a boolean
    assert isinstance(module.CALLBACK_DEPRECATED_WARNING, bool)

# Generated at 2022-06-13 11:57:13.254600
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert obj.CALLBACK_VERSION == 2.0
    assert obj.CALLBACK_TYPE == 'stdout'
    assert obj.CALLBACK_NAME == 'minimal'


# Generated at 2022-06-13 11:57:23.566817
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    """ Test the v2_on_file_diff method of class CallbackModule """

    # ansible.module_utils.six.moves.StringIO <- used by the function
    # to get the diff
    # file_name <- will be used to search for the file 
    import six.moves.StringIO
    import tempfile
    file_name = tempfile.mktemp()
    with open(file_name, 'w') as f:
        f.write('Diff lines\n')
    result = {'diff': {file_name: six.moves.StringIO()}}

    # We want the Console.display to be called
    display_called = False


# Generated at 2022-06-13 11:57:30.716758
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    result = {}

    result['diff'] = {}
    result['diff']['after'] = 'After'
    result['diff']['before'] = 'Before'
    result['diff']['before_header'] = 'Before Header'
    result['diff']['after_header'] = 'After Header'

    mock_display = type('mock_display', (object,), {'display': lambda a: a})
    cb = CallbackModule(mock_display())

    assert cb._get_diff(result['diff']) == "\nBefore Header\n\nBefore\n\nAfter Header\n\nAfter\n\n"

# Generated at 2022-06-13 11:57:39.787309
# Unit test for method v2_runner_on_failed of class CallbackModule

# Generated at 2022-06-13 11:57:47.364264
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    """Unit test for method v2_runner_on_ok of class CallbackModule"""

    result = object()
    result._host = object()
    result._host.get_name = lambda: 'myhost'
    result._result = {
        'changed': True,
        'ansible_job_id': '2222147925.30697'
    }
    result._task = object()
    result._task.action = 'setup'
    result._task.vars = {}
    callback = CallbackModule()
    callback.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:57:50.641117
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    ''' Constructor test '''
    x = CallbackModule()
    assert x is not None

# Generated at 2022-06-13 11:57:52.112511
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert isinstance(obj, CallbackModule)


# Generated at 2022-06-13 11:58:01.090201
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.callback.minimal import CallbackModule
    from ansible import constants as C

    c = CallbackModule()

    # Test changed = false
    result = {'ansible_facts': {}, '_ansible_no_log': False, '_ansible_verbose_always': False, 'changed': False, 'invocation': {'module_args': {'state': 'absent', 'name': 'mytest'}}, 'ansible_module_name': 'service', 'diff': {'before': {}, 'after': {}}}
    c._handle_warnings = lambda x: None

# Generated at 2022-06-13 11:59:16.680929
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert(callable(CallbackModule) == True)

# Generated at 2022-06-13 11:59:23.236894
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    class MockDisplay(object):
        def __init__(self):
            self.data = []
        def display(self, data, color=None):
            self.data.append(data)

    cb = CallbackModule()
    cb._display = MockDisplay()

    # diff from regular file
    result = {
        'diff': {
            '/tmp/test1.txt': '---\n+++\n@@ -1,1 +1,1 @@\n-old\n+new'
        },
        'changed': True
    }
    cb.v2_on_file_diff(result)
    assert cb._display.data[0] == '---\n+++\n@@ -1,1 +1,1 @@\n-old\n+new'

    del cb._display.data[:]
    

# Generated at 2022-06-13 11:59:28.026443
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    c = CallbackModule()
    c._dump_results = lambda x, y: x
    c._get_diff = lambda x: x
    # Test diff with changes
    result = {'changed': True, 'diff': ['+a', '-a']}
    assert c.v2_on_file_diff(result) == ['+a', '-a']
    # Test diff without changes
    result = {'changed': False, 'diff': ['+a', '-a']}
    assert c.v2_on_file_diff(result) is None

# Generated at 2022-06-13 11:59:37.321270
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Test 1
    result_dict = {'failed': True, 'parsed': False, 'invocation': {'module_name': ''}, 'stdout': '', 'stdout_lines': [], 'msg': '', 'stderr_lines': [], 'warnings': [], 'stderr': '', 'rc': 0, 'start': '2019-04-18 11:44:29.325392', 'end': '2019-04-18 11:44:29.325839', 'delta': '0:00:00.000447'}
    result_hostname = '192.168.1.1'
    result_ignore_errors = True
    result_display = result_hostname + ' | FAILED! => ' + str(result_dict)

# Generated at 2022-06-13 11:59:42.338310
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = MockTaskResult()
    result._task = MockTask()
    result._host = MockHost()
    result._result = {'failed': ''}
    result._task.action = 'setup'

    callback = CallbackModule()
    callback.v2_runner_on_failed(result)
    assert(callback._dump_results(result._result, indent=4) == "")


# Generated at 2022-06-13 11:59:51.334006
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    def _handle_exception(result):
        pass

    def _handle_warnings(result):
        pass

    def _display_display(results, color=None):
        pass

    class CallbackModuleTestClass:
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'minimal'
        _handle_exception = _handle_exception
        _handle_warnings = _handle_warnings
        _display = {"display": _display_display}

    test_class = CallbackModuleTestClass()

    result = {"_host": {"_name": "name"}, "_task": {"action": "action"}, "_result": {"changed": False}}
    test_class.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:59:52.530894
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    global cb
    cb = CallbackModule()

# Generated at 2022-06-13 11:59:53.781627
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()

# Generated at 2022-06-13 12:00:02.652337
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import six
    import json
    # Test 1
    print("Test 1 ===========================================================")
    mock_result = MockResult()
    mock_result._result = {
        'stdout': 'some message',
        'rc': 0
    }
    
    callback = CallbackModule()
    
    callback.v2_runner_on_failed(mock_result)
    assert six.callable(callback._display.display)
    assert callback._display.display.capture == "some message | FAILED | rc=0 >>\n\n"
    
    # Test 2
    print("Test 2 ===========================================================")
    
    mock_result = MockResult()

# Generated at 2022-06-13 12:00:05.618165
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule().CALLBACK_TYPE == 'stdout'
    assert CallbackModule().CALLBACK_NAME == 'minimal'
    assert CallbackModule().CALLBACK_VERSION == 2.0
    assert CallbackModule()._display is not None
    assert CallbackModule()._plugin_options is not None