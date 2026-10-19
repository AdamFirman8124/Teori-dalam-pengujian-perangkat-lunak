

# Generated at 2022-06-13 05:23:46.920154
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

# Generated at 2022-06-13 05:23:56.460843
# Unit test for function main
def test_main():
    args = dict(
        command=dict(required=True),
        chdir=dict(type='path'),
        creates=dict(type='path'),
        removes=dict(type='path'),
        responses=dict(type='dict', required=True),
        timeout=dict(type='int', default=30),
        echo=dict(type='bool', default=False),
    )

    module = AnsibleModule(
        argument_spec=args
    )

    chdir = module.params['chdir']
    args = module.params['command']
    creates = module.params['creates']
    removes = module.params['removes']
    responses = module.params['responses']
    timeout = module.params['timeout']
    echo = module.params['echo']

    events = dict()

# Generated at 2022-06-13 05:24:04.300768
# Unit test for function main
def test_main():
    import textwrap
    import pexpect

    # patch pexpect.runu
    def runu(self, command, events=None, extra_args=None,
             logfile=None, cwd=None, env=None, _spawn=None, echo=None):
        return ''.encode('utf-8'), 0

    pexpect.runu = runu

    # patch pexpect.run
    def run(self, command, events=None, extra_args=None,
            logfile=None, cwd=None, env=None, _spawn=None, echo=None):
        return ''.encode('utf-8'), 0

    pexpect.run = run

    # patch pexpect._run

# Generated at 2022-06-13 05:24:15.213063
# Unit test for function response_closure
def test_response_closure():
    """Validate expected behaviour for response_closure()"""

    # required imports
    from ansible.module_utils.basic import AnsibleModule
    import os

    # create an AnsibleModule with some parameters
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

    # create a question and some responses for the response_closure
    question = "Asking a question"
    responses = [ "Answer 1","Answer 2","Answer 3" ]
    test_responses = { question: responses }

    # create a list from the responses

# Generated at 2022-06-13 05:24:24.030462
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

# Generated at 2022-06-13 05:24:28.032734
# Unit test for function main
def test_main():
    args = {
        "command": "echo 'Hello World'",
        "responses": {
            "Key": "Value"
        },
        "timeout": 50
    }
    module = AnsibleModule(argument_spec=args)
    main()

# Generated at 2022-06-13 05:24:41.231040
# Unit test for function main
def test_main():
    args = dict(command='ls -l /', responses={'(?i)Is this okay': 'yes'})
    res1 = dict(
        cmd=args['command'],
        stdout="-rw-r--r--  1 root root  148 May  3 15:03 /etc/ansible/ansible.cfg",
        rc=0,
        start='2016-05-03 15:03:28.619427',
        end='2016-05-03 15:03:28.631711',
        delta='0:00:00.012284',
        changed=True)

# Generated at 2022-06-13 05:24:49.032241
# Unit test for function main
def test_main():
    m = AnsibleModule(
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
    m.params = {'command': "/bin/echo ''", 'responses': {'Question': 'response'}, 'timeout': 3}
    main()



# Generated at 2022-06-13 05:24:55.583096
# Unit test for function main
def test_main():
    args = dict(command="/bin/echo hello")
    p = Mock(return_value=(b'', 0))
    module = AnsibleModule(argument_spec=dict(command=dict(required=True)))
    with patch('pexpect.run', p):
        main()
    assert p.called
    assert p.call_args[0][0] == "\"/bin/echo hello\""


# Generated at 2022-06-13 05:25:02.809299
# Unit test for function response_closure
def test_response_closure():
    import ansible.module_utils.basic as basic
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import BytesIO

    # Python 2.6 doesn't have the StringIO module
    # TODO: Remove this when we no longer support Python 2.6
    if PY2:
        StringIO = StringIO.StringIO

    stdout = StringIO()
    # This module has been refactored to handle bytes and text on python 3.
    # To maintain backwards compatibility we'll make sure we're using bytes on py3.
    stdout = BytesIO()


    def gen_ansible_module(*args, **kwargs):
        am = basic.AnsibleModule(*args, **kwargs)
        am

# Generated at 2022-06-13 05:25:34.312048
# Unit test for function main
def test_main():
    # Function used to run the actual command when pexpect.run() is not available.
    # Used to test how the module calls pexpect.run().
    def fake_pexpect_run(args, **kwargs):
        kwargs['args'] = args
        return kwargs

    # Function used to run the actual command when pexpect.run() is not available.
    # Used to test how the module calls pexpect._run().
    def fake_pexpect__run(args, **kwargs):
        kwargs['args'] = args
        # We don't care about output, just what pexpect is doing.
        return '', 0

    # Fake version of pexpect, used to test how the module handles pexpect.

# Generated at 2022-06-13 05:25:46.250596
# Unit test for function main

# Generated at 2022-06-13 05:25:58.180168
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={'responses': dict(required=True, type='dict')})

    responses = ['response1', 'response2', 'response3']
    question = 'question'
    response = response_closure(module, question, responses)

    assert response('key') == b'response1\n'
    assert response('key') == b'response2\n'
    assert response('key') == b'response3\n'
    # This should fail because we have no more responses
    try:
        response('key')
        assert False
    except:
        assert True

# Generated at 2022-06-13 05:26:04.739018
# Unit test for function response_closure
def test_response_closure():
    response = response_closure(None, "Question", ["response1", "response2", "response3"])
    assert response({"child_result_list": ["child_result1"]}) == b'response1\n'
    assert response({"child_result_list": ["child_result2"]}) == b'response2\n'
    assert response({"child_result_list": ["child_result3"]}) == b'response3\n'
    module.fail_json(msg="No remaining responses for '%s', output was '%s'")

# Generated at 2022-06-13 05:26:17.664952
# Unit test for function response_closure
def test_response_closure():
    def test_module(a, b, c):
        return dict(failed=False, changed=False, stdout='')

    module = type('FakeAnsibleModule', (), dict(
        fail_json=lambda self, a: None,
        exit_json=lambda self, a: None,
    ))(test_module)

    responses = ['a', 'b', 'c', 'd']
    gen = response_closure(module, 'question', responses)


    for idx, r in enumerate(responses):
        assert gen(dict()) == b"%s\n" % to_bytes(r)

    try:
        gen(dict())
        assert False, "Should've raised exception"
    except SystemExit as e:
        assert e.code == 1

# Generated at 2022-06-13 05:26:26.736849
# Unit test for function main
def test_main():
    arg_spec = dict(
        command=dict(required=True),
        chdir=dict(type='path'),
        creates=dict(type='path'),
        removes=dict(type='path'),
        responses=dict(type='dict', required=True),
        timeout=dict(type='int', default=30),
        echo=dict(type='bool', default=False),
    )

    class TestModule(AnsibleModule):
        pass

    # Create the module object
    module = TestModule(
        argument_spec=arg_spec,
        check_invalid_arguments=False
    )

    m_os_path_exists = getattr(os.path, 'exists')
    m_os_chdir = getattr(os, 'chdir')
    m_os_path_abspath = getattr

# Generated at 2022-06-13 05:26:33.479287
# Unit test for function response_closure
def test_response_closure():
    created_module = AnsibleModule(
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

    # Clone a dictionary
    example_responses = dict()
    for key, value in created_module.params['responses'].items():
        if isinstance(value, list):
            example_responses[key] = list(value)
        else:
            example_responses[key] = value

    responses = []

# Generated at 2022-06-13 05:26:40.627024
# Unit test for function main
def test_main():
    import unittest
    import cStringIO
    import shutil
    import time
    class Test_Main(unittest.TestCase):
        def setUp(self):
            self.module = None
            self.responses = None
            self.patched_stdout = None
            self.patched_stderr = None
            self.patched_module = None
        def tearDown(self):
            if self.module:
                self.module.exit_json = self.patched_module
            if self.responses:
                self.responses = self.patched_responses
            if self.patched_stderr:
                sys.stderr = self.patched_stderr
            if self.patched_stdout:
                sys.stdout = self.patched_stdout


# Generated at 2022-06-13 05:26:53.861913
# Unit test for function main
def test_main():
    args = dict(
        command='echo hello',
        responses={
            'hello': ''
        },
        timeout=30,
        echo=False,
    )
    with patch('ansible.module_utils.basic.AnsibleModule') as ansibleModuleMock:
        ansibleModuleMock.return_value = ansibleModuleMock
        ansibleModuleMock.params = MagicMock(side_effect = lambda x:[args[x]])
        ansibleModuleMock.fail_json = MagicMock()

        with patch('ansible.module_utils._text.to_bytes') as toBytesMock:
            toBytesMock.return_value = 'MockedBinaryText'

# Generated at 2022-06-13 05:27:03.838484
# Unit test for function response_closure
def test_response_closure():
    class Module(object):
        def __init__(self):
            self.fail_json = lambda **kv: ModuleException(kv)

    class ModuleException(Exception):
        def __init__(self, kv):
            self.kv = kv

    def test(question, responses, expected_responses):
        try:
            f = response_closure(Module(), question, responses)
            for i, r in enumerate(expected_responses):
                resp = f({'child_result_list': ['a']})
                assert(resp == r)
        except ModuleException as e:
            assert(False)
        except Exception as e:
            assert(False)


# Generated at 2022-06-13 05:27:33.375799
# Unit test for function response_closure
def test_response_closure():
    class MockModule(object):
        def __init__(self):
            self.failure = False
        def fail_json(self, msg, **kwargs):
            self.failure = True
            self.failure_msg = msg

    responses = ['a', 'b', 'c', 'd']
    command = 'command'
    question = 'question'
    module = MockModule()
    response = response_closure(module, question, responses)

    result = dict(child_result_list=[])
    value = response(result)
    assert value == b'a\n'
    assert module.failure is False
    assert result['child_result_list'] == []

    result = dict(child_result_list=[command])
    value = response(result)
    assert value == b'b\n'
    assert module

# Generated at 2022-06-13 05:27:42.497156
# Unit test for function main
def test_main():
    args = {"_ansible_check_mode": False, "_ansible_diff": False, "ansible_check_mode": False, "ansible_module_args": {}, "ansible_version": {"full": "2.9.7", "major": 2, "minor": 9, "revision": 7, "string": "2.9.7"}, "changed": False, "invocation": {"module_args": {}}, "module_args": {}}
    args['ansible_module_args'] = dict(command='ls')
    main()
    assert True

# Generated at 2022-06-13 05:27:48.809298
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

# Generated at 2022-06-13 05:27:55.199228
# Unit test for function response_closure
def test_response_closure():
    import ansible.module_utils.basic
    sc = response_closure(ansible.module_utils.basic.AnsibleModule(argument_spec={}), "A", ["B", "C"])
    assert sc({}) == b"B\n"
    assert sc({}) == b"C\n"
    try:
        sc({})
        assert False
    except SystemExit:
        pass
    else:
        assert False

# Generated at 2022-06-13 05:28:05.822756
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from ansible.module_utils.six import b
    if not ansible_version.startswith('2.1'):
        pytest.skip("pexpect module new in Ansible 2.1")
    sys.modules['pexpect'] = MagicMock(__version__='3.2')

    with pytest.raises(SystemExit):
        main()

    sys.modules['pexpect'] = MagicMock(__version__='3.3')
    with patch('ansible.module_utils.basic.AnsibleModule') as am:
        am.return_value = MagicMock(params=dict(
                command='echo foo',
                responses=dict(Question='answer'),
        ))

# Generated at 2022-06-13 05:28:15.894616
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

    def mock_pexpect_run(a, b, c, d, e, f):
        return b'', 0

    args = 'foo'
    responses = {'questions': 'responses'}
    timeout = 60
    echo = True

    global HAS_PEXPECT
    HAS_PEXPECT = True


# Generated at 2022-06-13 05:28:22.781823
# Unit test for function main

# Generated at 2022-06-13 05:28:32.574435
# Unit test for function response_closure
def test_response_closure():
    import pexpect.expect
    class Module(object):
        class FailJson(Exception):
            """Exception raised by module.fail_json."""
            def __init__(self, msg=None, **kwargs):
                self.kwargs = kwargs
                self.msg = msg
                super(Module.FailJson, self).__init__()

        def __init__(self):
            self.fail_json = Module.FailJson

    module = Module()

    per_question = [["first response", "second response", "third response"]]
    responses = {question[0]: question for question in per_question}
    child = pexpect.spawn("/bin/true")
    child.expect(b"")


# Generated at 2022-06-13 05:28:45.774690
# Unit test for function main
def test_main():
    # Save some globals
    _ANSIBLE_ARGS = ['-vvv', __file__,
        'command=/bin/sleep 1 creates=test.log']
    _ANSIBLE_ARGS_ORIG = os.environ['ANSIBLE_ARGS']
    os.environ['ANSIBLE_ARGS'] = ' '.join(_ANSIBLE_ARGS)

    # Init module
    global module

# Generated at 2022-06-13 05:28:52.735371
# Unit test for function main
def test_main():
    # Mock of AnsibleModule object from ansible.module_utils.basic.
    class AnsibleModule(object):
        pass
    ansible_module = AnsibleModule()
    ansible_module.params = {
        'command': 'ls',
        'chdir': None,
        'creates': None,
        'removes': None,
        'responses': {},
        'timeout': 30,
        'echo': False
    }
    # Mock of pexpect.
    class Pexpect():
        @staticmethod
        def run(cmd, timeout, cwd, echo):
            return cmd, 0
    pexpect = Pexpect()
    pexpect.run = Pexpect.run
    # Mock of datetime.datetime.now().

# Generated at 2022-06-13 05:29:52.746601
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
    responses = ["resp", "test", "ansible"]
    question = "What is the question?"
    response = response_closure(module, question, responses)
    new_result = "new data"
    child_result_list = ["old data"]
    info = {'child_result_list': child_result_list}
    child_result_list.append(new_result)

# Generated at 2022-06-13 05:29:58.744407
# Unit test for function main
def test_main():
    def test_response(info):
        responses = ['', '', '', 'yes' if 'yes' in info['child_result_list'][-1] else 'no']
        try:
            return next(resp_gen)
        except StopIteration:
            raise Exception("No remaining responses for '%s', output was '%s'" % (question, info['child_result_list'][-1]))
            # return b'no\n'

    # For the temporary testing purpose, do not use AnsibleModule
    class DummyModule(object):
        def __init__(self):
            self.params = {}
            self.params['command'] = 'certbot renew --force-renewal --agree-tos -m sergy.olshevskiy@gmail.com --expand'
            self.params['chdir']

# Generated at 2022-06-13 05:30:10.258983
# Unit test for function response_closure
def test_response_closure():
    import ansible.module_utils.ansible_modlib.expect._util as _util
    import ansible.module_utils.ansible_modlib as _ansible_modlib
    class Module(object):
        class FailJson(object):
            def __init__(self, msg):
                self.msg = msg

        def __init__(self):
            self.fail_json = self.FailJson

    class ResponseInfo(object):
        def __init__(self, child_result_list):
            self.child_result_list = child_result_list

    responses = ["Foo", "Bar", "Baz"]
    question = "My Question"
    # Create a closure from our test data
    response = _util.response_closure(Module(), question, responses)
    # Run through it twice, should return 2

# Generated at 2022-06-13 05:30:21.644242
# Unit test for function main
def test_main():
    args = dict(
        command='/usr/bin/whoami',
        responses=dict(
            username='root',
            password='hunter2'
        ),
        timeout=30,
        echo=False
    )

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
    module.params = args

    rc = None
    b_out = to_bytes('')

    chdir = module.params['chdir']
    args = module

# Generated at 2022-06-13 05:30:31.268900
# Unit test for function main
def test_main():
    import json
    import subprocess

    # Test arguments with timeout failure
    args = [
        'ansible-playbook',
        '-i', 'localhost,',
        '-e', 'ansible_python_interpreter=/usr/bin/python',
        '-e', 'ansible_connection=local',
        'examples/pexpect.yml',
    ]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, _ = process.communicate()
    assert process.returncode == 2
    json_output = json.loads(output)
    assert json_output['msg'] == 'command exceeded timeout'

    # Test arguments with regex match failure

# Generated at 2022-06-13 05:30:39.601676
# Unit test for function main
def test_main():
    args = dict(
        command='echo "foo"',
        responses=dict()
    )
    # Test that run was called with default echo=False
    # This test is hard to follow, but I'm just trying to exercise the
    # pexpect._run code path, which could only be exercised in python 2
    # without echo=False, which would fail with:
    #
    # pexpect.exceptions.EOF: End Of File (EOF) in read_nonblocking().
    #
    # This is because pexpect._read() was called with echo=False, and
    # stdout.read() would hang, as echo=False is not supported.
    #
    # The test is to ensure that no output is printed, hence the empty
    # b'' to sys.stdout and the empty echo_resp

# Generated at 2022-06-13 05:30:54.740369
# Unit test for function main
def test_main():
    sys.path.append('/usr/local/lib/python2.7/dist-packages/ansible/modules/')
    import json

    # Simulate AnsibleModule
    class AnsibleModule():
        def __init__(self, argument_spec):
            self.params = argument_spec
            self.check_mode = None
            self.diff_mode = None
            self.platform = 'posix'

        def fail_json(self, msg="", rc=None, changed=True, cmd=None, stdout=None, start=None, end=None, delta=None):
            print("FAILED: ", msg)
            print("\tArguments:")
            print("\t\tcheck_mode:", self.check_mode)
            print("\t\tdiff_mode:", self.diff_mode)


# Generated at 2022-06-13 05:30:57.009252
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:31:03.074143
# Unit test for function response_closure
def test_response_closure():
    import types
    responses = ["MySekretPa$$word", "response1", "r2", "r3"]
    r = response_closure(None, None, responses)
    assert isinstance(r, types.FunctionType)

    assert r(None) == b"MySekretPa$$word\n"
    assert r(None) == b"response1\n"
    assert r(None) == b"r2\n"
    assert r(None) == b"r3\n"

# Generated at 2022-06-13 05:31:08.483851
# Unit test for function response_closure
def test_response_closure():

    # Create an ansible module to test the closure
    command = 'uname -r'
    responses = dict(
        question1 = "response1",
        question2 = "response2"
    )
    m = AnsibleModule(
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

    # Test response_closure with a single response
    wrapped = response_closure(m, 'question1', ['response1'])
    assert wrapped(dict()) == b'response1\n'

# Generated at 2022-06-13 05:33:22.481175
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, missing_required_lib

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