

# Generated at 2022-06-13 05:23:45.953812
# Unit test for function response_closure
def test_response_closure():
    def test_module(module_args, **kwargs):
        result = AnsibleModule(**kwargs).execute_module(**module_args)
        assert not result.get('failed', False)
        return result

    # Test single response
    result = test_module(dict(command=["sleep", "0"],
                              responses={'pattern': 'response'}))
    assert result['stdout'] == 'response\n'
    result = test_module(dict(command=["sleep", "0"],
                              responses={'pattern': 'response'}))
    assert result['stdout'] == 'response\n'

    # Test multi response
    result = test_module(dict(command=["sleep", "0"],
                              responses={'pattern': ['response1', 'response2']}))

# Generated at 2022-06-13 05:23:53.440445
# Unit test for function main
def test_main():
  commands = [
    #(command, echo, chdir, creates, removes, timeout)
    ('echo hello', False, '.', '.', None, 30, 1, "hello\n"),
    ('echo hello', False, '.', '.', '.', 30, 1, "hello\n")
  ]
  for command, echo, chdir, creates, removes, timeout, rc, stdout in commands:
    assert main(command, echo, chdir, creates, removes, timeout) == (rc, stdout)



# Generated at 2022-06-13 05:23:57.719203
# Unit test for function main
def test_main():
    args = dict(
        command='test_command',
        responses=dict(test_key='test_value'),
    )

    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            responses=dict(type='dict', required=True),
        )
    )

    module.params.update(args)
    main()

# Generated at 2022-06-13 05:24:06.959284
# Unit test for function main
def test_main():
    mod = AnsibleModule(argument_spec=dict(
        command=dict(required=True),
        chdir=dict(type='path'),
        creates=dict(type='path'),
        removes=dict(type='path'),
        responses=dict(type='dict', required=True),
        timeout=dict(type='int', default=30),
        ),
        supports_check_mode=False)

    mod.params['command'] = 'ls'
    mod.params['responses'] = dict()

    # Run main to exit with correct parameters when no exceptions occur.
    main()

    # Run main to exit with correct parameters when an exception occurs.
    main()

# Generated at 2022-06-13 05:24:18.519073
# Unit test for function response_closure
def test_response_closure():
    import os
    import sys
    import tempfile
    import unittest
    import ansible.module_utils.basic

    # Make sure the module source is on the path
    # Make sure the module source is on the path
    if os.path.realpath(ansible.__file__).startswith(tempfile.gettempdir()):
        # If the ansible module source is in a temp directory,
        # we are probably running inside a test runner, so use that source
        module_utils_path = os.path.realpath(ansible.module_utils.basic.__file__)
        module_utils_dir = os.path.dirname(module_utils_path)
        if module_utils_dir not in sys.path:
            sys.path.insert(0, module_utils_dir)

# Generated at 2022-06-13 05:24:30.278350
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
        )
    )

    question = "Question"
    responses = ["response1", "response2", "response3"]
    wrapped = response_closure(module, question, responses)
    assert wrapped({"child_result_list": ["child_result1"]}) == b"response1\n"
    assert wrapped({"child_result_list": ["child_result1"]}) == b"response2\n"

# Generated at 2022-06-13 05:24:37.250332
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )
    chdir = module.params['chdir']
    args = module.params['command']
    creates = module.params['creates']
    removes = module.params['removes']
    responses = module.params['responses']
    timeout = module.params['timeout']
    echo = module.params['echo']

    events = dict()

# Generated at 2022-06-13 05:24:44.642541
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={'responses': {'type': 'dict', 'required': True}}
    )

    question = 'Question'
    responses = ['response1', 'response2']

    response = response_closure(module, question, responses)
    assert response(dict(child_result_list=[])) == b'response1\n'
    assert response(dict(child_result_list=[])) == b'response2\n'

# Generated at 2022-06-13 05:24:53.325002
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )
    args = module.params['command']
    responses = module.params['responses']
    timeout = module.params['timeout']
    echo = module.params['echo']
    events = dict()
    for key, value in responses.items():
        if isinstance(value, list):
            response = response_closure(module, key, value)

# Generated at 2022-06-13 05:25:01.537163
# Unit test for function response_closure
def test_response_closure():
    class MockModule:
        def fail_json(self, msg):
            self.error = msg

    responses = ['resp1', 'resp2', 'resp3']
    resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses)
    question = 'Question'
    module = MockModule()
    response_0 = response_closure(module, question, responses)
    response_gen = response_closure(module, question, responses)

    result_0 = response_0(None)
    result_gen = response_gen({'child_result_list': ['Match: resp1\n']})


# Generated at 2022-06-13 05:25:16.642109
# Unit test for function main
def test_main():
    # make sure we can exit with a non-zero status
    try:
        main()
    except SystemExit as e:
        assert e.code == 1


# Generated at 2022-06-13 05:25:18.418861
# Unit test for function main
def test_main():

    args = {"command":"touch /tmp/test_main", "responses":{"abc":"def"}, "removes":None, "echo":False, "chdir":None, "creates":None, "timeout":30}
    ansible_module_main(args)



# Generated at 2022-06-13 05:25:29.411552
# Unit test for function main
def test_main():
    #########################################################################
    # Example usage
    #########################################################################
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )

    # How to set args
    args = "run commands"

    # How to set chdir
    chdir = None

    # How to set creates
    creates = None

    # How to set removes
    removes = None

    # How to set responses
    responses = None

    # How to set timeout
    timeout = 30



# Generated at 2022-06-13 05:25:41.297765
# Unit test for function main
def test_main():
  module = AnsibleModule( argument_spec=dict(
    command=dict(required=True),
    chdir=dict(type='path'),
    creates=dict(type='path'),
    removes=dict(type='path'),
    responses=dict(type='dict', required=True),
    timeout=dict(type='int', default=30),
    echo=dict(type='bool', default=False),
    )
  )

  os.chdir("c:\\Users\\lhagstrom\\Documents\\thermo\\src" )
  chdir = "c:\\Users\\lhagstrom\\Documents\\thermo\\src"
  args = "python example_ansible_input.py"
  creates = "true"
  removes = None
  #responses = { 'Password' : 'password' }

# Generated at 2022-06-13 05:25:42.733657
# Unit test for function main
def test_main():

    print("Test main()")

# Generated at 2022-06-13 05:25:51.870515
# Unit test for function main
def test_main():
    test_args = (
        '''
        - name: Case insensitive password string match
          ansible.builtin.expect:
            command: passwd username
            responses:
              (?i)password: "MySekretPa$$word"
          # you don't want to show passwords in your logs
          no_log: true

        - name: Generic question with multiple different responses
          ansible.builtin.expect:
            command: /path/to/custom/command
            responses:
              Question:
                - response1
                - response2
                - response3
        '''
    )

# Generated at 2022-06-13 05:26:03.628358
# Unit test for function response_closure

# Generated at 2022-06-13 05:26:18.013886
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    from faketime import fake_time
    from io import StringIO
    from datetime import datetime
    import sys

    failed = False
    msg = []

    # Fail the module
    def fail(m):
        failed = True
        msg.append(m)

    # Mock module
    class MModule:
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            fail(msg)

    # Mock module object
    m = MModule()

    # Mock child_result_list
    child_result_list = [
        "Question 1: Question 1\n",
        "Question 2: Question 2\n"
    ]

    # Test next() succeeds
    question = "Question"

# Generated at 2022-06-13 05:26:26.765273
# Unit test for function main
def test_main():
    # pylint: disable=import-error,unused-import,unused-variable,unused-argument
    import sys
    import os
    import pytest
    import contextlib
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six import StringIO
    import ansible.module_utils.basic as basic
    # pylint: enable=import-error,unused-import,unused-variable,unused-argument

    @contextlib.contextmanager
    def nostderr():
        """
        Suppress the stderr.  This is needed to capture the output of the
        main function.
        """
        savestder

# Generated at 2022-06-13 05:26:33.505019
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )

    chdir = module.params['chdir']
    args = module.params['command']
    creates = module.params['creates']
    removes = module.params['removes']
    responses = module.params['responses']
    timeout = module.params['timeout']
    echo = module.params['echo']

    events = dict()

# Generated at 2022-06-13 05:26:55.703676
# Unit test for function response_closure
def test_response_closure():
    import difflib
    import string
    global response_closure
    import ansible.module_utils.basic as mod_utils
    global to_bytes

    def diff_strings(x, y):
        x_lines=x.splitlines(1)
        y_lines=y.splitlines(1)
        diff_generator = difflib.unified_diff(x_lines, y_lines)
        diff = ""
        for line in diff_generator:
            diff += line
        return diff


# Generated at 2022-06-13 05:27:03.459920
# Unit test for function main
def test_main():
    # Test if main is called
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
        )
    )
    module.params['command'] = 'test'
    module.params['chdir'] = ''
    module.params['creates'] = ''
    module.params['removes'] = ''
    module.params['responses'] = ''
    module.params['timeout'] = ''
    rc, out, err = main()

# Generated at 2022-06-13 05:27:13.648306
# Unit test for function response_closure
def test_response_closure():
    # testing 1 response
    responses = [to_text('response1')]
    question = 'question1'
    result_response = response_closure(AnsibleModule, question, responses)
    assert result_response({'child_result_list': [to_text('response_received')]}) == to_bytes('response1\n')
    # testing one response and eventually iterate through the list again
    responses = [to_text('response1'), to_text('response2')]
    question = 'question2'
    result_response = response_closure(AnsibleModule, question, responses)
    assert result_response({'child_result_list': [to_text('response_received')]}) == to_bytes('response1\n')

# Generated at 2022-06-13 05:27:25.267369
# Unit test for function main
def test_main():
    args = {
        'command': 'passwd username',
        'responses': {
            'password': 'MySekretPa$$word'
        },
        'timeout': 30,
        'echo': False,
        '_ansible_check_mode': False,
        '_ansible_diff': False,
        '_ansible_verbosity': 0,
        '_ansible_selinux_special_fs': False
    }


# Generated at 2022-06-13 05:27:39.469742
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule, missing_required_lib
    from ansible.module_utils._text import to_bytes, to_native, to_text
    import pytest

    class FakeModule(AnsibleModule):
        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

    module = FakeModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )

    responses = ["first", "second", "third"]


# Generated at 2022-06-13 05:27:47.990022
# Unit test for function main
def test_main():
    '''
    Unit test case for function main
    '''
    # Further discussion of the unit testing approach is
    # available at
    # https://github.com/ansible/ansible/pull/10391#issuecomment-222768791
    #
    # The unit test is a modified version of the "Quickstart"
    # described in
    # https://docs.pytest.org/en/latest/getting-started.html
    # except that the module is not installed at the site level.
    # Rather it is loaded through a parent directory for testing purposes.
    #
    # The unit test uses the pytest framework with the following plugins
    # installed:
    # * testinfra
    # * pytest-xdist
    # * pytest-html
    #
    # A testinfra fixture is used to return test data


# Generated at 2022-06-13 05:28:00.700587
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )

    if not HAS_PEXPECT:
        module.fail_json(msg=missing_required_lib("pexpect"),
                         exception=PEXPECT_IMP_ERR)

    chdir = module.params['chdir']
    args = module.params['command']
    creates = module.params['creates']
    removes = module.params['removes']

# Generated at 2022-06-13 05:28:09.603345
# Unit test for function response_closure
def test_response_closure():
    import pexpect
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            responses=dict(type='dict', required=True),
        )
    )

    def closure(info):
        return b'yes\n'

    question = 'Are you sure?'
    responses = ['yes', 'no']
    events = {to_bytes(question): closure}
    out = []
    rc = None

    def collect_output(b_out):
        out.append(b_out)


# Generated at 2022-06-13 05:28:19.748514
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )
    question = 'question'
    responses = ['a','b','c']
    rc = response_closure(module, question, responses)
    assert rc({'child_result_list': ['response1']}) == b'a\n'
    assert rc({'child_result_list': ['response1']}) == b'b\n'

# Generated at 2022-06-13 05:28:26.657379
# Unit test for function response_closure
def test_response_closure():
    import sys
    import types
    import pexpect
    module = types.ModuleType('ansible.modules.command.expect')
    module.fail_json = strict_fail_json
    module.params = {'responses': {}}
    module.pexpect = pexpect
    questions = [
        'question 1',
        'question 2',
        'question 3'
    ]
    responses = [
        'response 1',
        'response 2',
        'response 3'
    ]
    response = response_closure(module, questions[0], responses)
    assert isinstance(response, types.FunctionType), \
        "response_closure should return a function"
    assert response.__name__ == 'wrapped'

    if six.PY3:
        import io
        import sys
        out = io.BytesIO

# Generated at 2022-06-13 05:29:08.030768
# Unit test for function response_closure
def test_response_closure():
    import pytest

    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )

    responses = dict()
    responses["Question"] = ["response1", "response2", "response3"]

    response = response_closure(module, "Question", responses["Question"])

    assert (response(dict()) == b'response1\n')
    assert (response(dict()) == b'response2\n')

# Generated at 2022-06-13 05:29:08.996986
# Unit test for function main

# Generated at 2022-06-13 05:29:09.440068
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:29:16.734368
# Unit test for function main
def test_main():
    import sys
    import os
    path = os.path.abspath(__file__)
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(path))))
    print(sys.path)
    print('=======================')

    from ansible.module_utils.basic import *
    from ansible.module_utils._text import to_bytes, to_native, to_text
    from ansible.module_utils.basic import AnsibleModule
    import traceback
    cmd_list = ['/bin/ping', '-c', '5', '8.8.8.8']
    cmd = ' '.join(cmd_list)

# Generated at 2022-06-13 05:29:28.657090
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule as MockAnsibleModule
    from ansible.module_utils._text import to_bytes
    import test.support

    class MockException(Exception):
        pass

    class MockAnsibleFailJson(object):
        def __init__(self):
            self.fail_msg = None
            self.fail_args = None

        def __call__(self, msg, **kwargs):
            self.fail_msg = msg
            self.fail_args = kwargs

    def mock_next():
        raise StopIteration

    def mock_next_response(info):
        responses = [b'response1', b'response2', b'response3']

# Generated at 2022-06-13 05:29:37.830112
# Unit test for function main
def test_main():
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes

    content = 'Hello World!'
    file_path = tempfile.NamedTemporaryFile(dir='.')
    file_path.file.write(to_bytes(content))
    file_path.file.flush()

    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            responses=dict(type='dict', required=True),
            chdir=dict(type='path', required=False),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )
    args = 'cat %s' % file_path.name.decode('utf-8')

    module.params['command'] = args


# Generated at 2022-06-13 05:29:47.738765
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils._text import to_bytes

    fake_pexpect = MockPexpect(b'', 0, None)
    fake_pexpect.run.return_value = (b'', 0)

    module = MockAnsibleModule()
    module.params = dict(command='command', echo=False, responses={'Question': 'answer'})
    module._ansible_version = 2.8

    pexpect_class = MockPexpectClass()
    pexpect_class.run = fake_pexpect.run
    pexpect_class._run = fake_pexpect._run

    setattr(module, 'pexpect', pexpect_class)

    # With pexpect>=4
    with pytest.raises(AnsibleExitJson) as info:
        main

# Generated at 2022-06-13 05:29:56.531286
# Unit test for function main
def test_main():
    read_hosts = '1.1.1.1'
    read_group = 'test_group'
    command = 'nslookup www.sina.com.cn'
    timeout = 30
    result = {'rc': 0, 'delta': '0:00:00.016487', 'start': '2018-05-11 10:08:46.907820', 'cmd': command, 'stdout': 'Server:  10.211.2.213\nAddress:  10.211.2.213#53\n\nNon-authoritative answer:\nName:    www.sina.com.cn\nAddress:  111.13.101.208\n\n', 'changed': True, 'end': '2018-05-11 10:08:46.924307'}

# Generated at 2022-06-13 05:30:07.903607
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(argument_spec={})
    question = 'Question'
    responses = ['response1', 'response2']
    response = response_closure(module, question, responses)
    child_result_list = []
    child_result_list.append(response({'child_result_list': child_result_list}))
    child_result_list.append(response({'child_result_list': child_result_list}))
    try:
        response({'child_result_list': child_result_list})
    except Exception as err:
        assert 'No remaining responses for \'Question\', output was ' \
               '\'response2\'\n' in str(err)

# Generated at 2022-06-13 05:30:11.707478
# Unit test for function main
def test_main():
    return_value = main()
    if return_value is not None:
        raise ValueError('main should return None but returned %s' % return_value)


# Generated at 2022-06-13 05:31:03.598018
# Unit test for function response_closure
def test_response_closure():
    responses = [u'Yes', u'No', u'maybe']
    question = u'Do you like cheese?'
    module = AnsibleModule(argument_spec={})

    wrap = response_closure(module, question, responses)

    info = {u'child_result_list': [u'Do you like cheese?']}
    assert wrap(info) == u'Yes\n'

    info = {u'child_result_list': [u'Do you like cheese?']}
    assert wrap(info) == u'No\n'

    info = {u'child_result_list': [u'Do you like cheese?']}
    assert wrap(info) == u'maybe\n'

    info = {u'child_result_list': [u'Do you like cheese?']}

# Generated at 2022-06-13 05:31:15.443422
# Unit test for function response_closure
def test_response_closure():
    import unittest
    import unittest.mock as mock

    class TestExpectModule(unittest.TestCase):
        def fail_json(self, msg, **kwargs):
            raise Exception(msg, kwargs)
    module = TestExpectModule()
    module.fail_json = mock.MagicMock()

    # Test normal response closure
    assert response_closure(module, "key", ["value1", "value2"])("") == b'value1\n'
    assert response_closure(module, "key", ["value1", "value2"])("") == b'value2\n'
    with self.assertRaises(Exception) as e:
        response_closure(module, "key", ["value1", "value2"])("")

# Generated at 2022-06-13 05:31:27.254207
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )
    child_result_list = ['Last', 'chance', 'for', 'a', 'hint']
    for q in ["Question", "Question1", "Question2"]:
        r = response_closure(module, q, ["response1", "response2"])
        assert r({'child_result_list': child_result_list}) == b'response1\n'

# Generated at 2022-06-13 05:31:38.590952
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )

    args = {'out':'/tmp/test_expect_output.txt', 'echo':False, 'expected_prompt':['password: '], 'timeout':'20', 'command':'/bin/echo "abcd"', 'responses':{'password: ':'abcd'}}
    module.params = args
    main()


# Generated at 2022-06-13 05:31:39.825488
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:31:49.230741
# Unit test for function main
def test_main():
    import sys
    import os
    import pexpect
    import module_utils.basic

    class DummyAnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.failed = False
            self.exit_args = {}

        def fail_json(self, **kwargs):
            self.failed = True
            self.exit_args = kwargs

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

    def mock_pexpect_run(*args, **kwargs):
        events = kwargs.get('events', {})
        responses = []
        for key, value in events.items():
            if callable(value):
                responses.append(value({'child_result_list': []}))
            else:
                responses

# Generated at 2022-06-13 05:31:59.704476
# Unit test for function response_closure
def test_response_closure():
    import mock
    import StringIO
    import sys

    # Mock out pexpect
    pexpect_spawn = mock.Mock()
    pexpect_spawn.__str__ = lambda self: '<pexpect object>'
    pexpect_spawn.isalive.return_value = True

    # Python 2.x expects items in pexpect.spawn.__init__ to be bytestrings
    # Python 3.x expects items in pexpect.spawn.__init__ to be text
    if sys.version_info[0] == 2:
        def to_bytes_or_native(s):
            return to_bytes(s)
    else:
        def to_bytes_or_native(s):
            return to_native(s)


# Generated at 2022-06-13 05:32:06.925819
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )

    if not HAS_PEXPECT:
        module.fail_json(msg=missing_required_lib("pexpect"),
                         exception=PEXPECT_IMP_ERR)

    chdir = './'
    args = 'ls'
    creates = None
    removes = None
    responses = {'Question': 'MyResponse'}
    timeout = module.params['timeout']

# Generated at 2022-06-13 05:32:07.674581
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:32:08.531095
# Unit test for function main
def test_main():
    pass