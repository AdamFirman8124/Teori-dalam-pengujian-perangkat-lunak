

# Generated at 2022-06-13 05:23:45.915442
# Unit test for function response_closure
def test_response_closure():
    class FakeModule(object):
        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

    module = FakeModule()
    responses = [ 'foo', 'bar' ]
    question = 'Question'
    reassigned_response_closure = response_closure(module, question, responses)
    assert reassigned_response_closure([question]) == b'foo\n'
    assert reassigned_response_closure([question]) == b'bar\n'
    try:
        reassigned_response_closure([question])
        raise Exception('should not get here')
    except Exception as e:
        assert e.args[0] == "No remaining responses for 'Question', output was ''"

# Generated at 2022-06-13 05:23:50.787053
# Unit test for function main
def test_main():
    args = {
        'command': '/bin/echo',
        'responses': {
            '.*': 'foo',
        },
    }
    rc = 0
    out = 'foo'
    assert main(args, rc, out) == 0


# Generated at 2022-06-13 05:23:58.135952
# Unit test for function response_closure
def test_response_closure():
    import pexpect
    module_args = {
        'command': 'echo "Hey"',
        'chdir': None,
        'creates': None,
        'removes': None,
        'responses': {
            'Hey': ['Hello', 'Goodbye']
        },
        'timeout': 1,
        'echo': False
    }
    module = AnsibleModule(argument_spec=dict(
        command=dict(required=True),
        chdir=dict(type='path'),
        creates=dict(type='path'),
        removes=dict(type='path'),
        responses=dict(type='dict', required=True),
        timeout=dict(type='int', default=30),
        echo=dict(type='bool', default=False)
    ))

# Generated at 2022-06-13 05:24:08.719517
# Unit test for function main
def test_main():

    # Test against empty arguments
    with pytest.raises(SystemExit):
        main(['action_plugins/expect.py'])

    # Test against non-array inputs
    with pytest.raises(SystemExit):
        main(['action_plugins/expect.py', '--argument', '"value"'])

    # Test against non-key-value input
    with pytest.raises(SystemExit):
        main(['action_plugins/expect.py',
              '--argument', 'value',
              '--argument2', 'value2'])

    # Test against missing required arguments
    with pytest.raises(SystemExit):
        main(['action_plugins/expect.py',
              '--argument', 'value'])

    # Test against only required arguments

# Generated at 2022-06-13 05:24:11.359110
# Unit test for function main
def test_main():
    from ansible.modules.system.expect import main


# Generated at 2022-06-13 05:24:11.917717
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:24:20.390652
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    sys.modules['ansible'] = type('module', (), {})
    sys.modules['ansible.module_utils'] = type('module', (), {})
    sys.modules['ansible.module_utils.basic'] = type('module', (), {})
    sys.modules['ansible.module_utils.basic'].AnsibleModule = AnsibleModule
    import expect

    def run(create_response_func):
        module = expect.AnsibleModule(argument_spec={
            'command': dict(required=True),
            'responses': dict(type='dict', required=True)
        })
        responses = [
            {"key": ["value1", "value2", "value3"]},
        ]

# Generated at 2022-06-13 05:24:32.143574
# Unit test for function response_closure
def test_response_closure():
    import os
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            responses=dict(type='dict', required=True),
        )
    )
    os.chdir('/')

    responses = {'Question': ['response1', 'response2', 'response3']}
    closures = {question: response_closure(module, question, responses[question])
                for question, responses in responses.items()}
    questions = list(responses.keys())

    closure = closures[questions[0]]
    response = closure({'child_result_list': []})
    assert response == b'response1\n', \
        "Expect response1 got '%s'" % response


# Generated at 2022-06-13 05:24:33.820008
# Unit test for function response_closure
def test_response_closure():
    import doctest
    result = doctest.testmod(expect)
    if result.failed > 0:
        exit(1)

# Generated at 2022-06-13 05:24:39.758461
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import action_plugins

    real_main = main
    def fake_main(args, **kwargs):
        # Ensure we never spawn a child process; that causes issues
        pexpect.spawn = lambda *args, **kwargs: None
        real_main(args, **kwargs)

    # Monkeypatch pexpect.runu, which is the run() variant used when
    # encoding=None
    real_pexpect_runu = pexpect.runu
    def fake_pexpect_runu(*args, **kwargs):
        kwargs['encoding'] = None
        return real_pexpect_runu(*args, **kwargs)
    pexpect.runu = fake_pexpect_runu


# Generated at 2022-06-13 05:24:58.976752
# Unit test for function main

# Generated at 2022-06-13 05:25:05.638453
# Unit test for function main
def test_main():
    from unittest import TestCase, mock
    from unittest.mock import patch

    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import ImmutableDict

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught
        by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught
        by the test case"""
        pass

    def exit_json(*args, **kwargs):
        """function to patch over exit_json; package return
        data into an exception"""
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)


# Generated at 2022-06-13 05:25:11.269325
# Unit test for function response_closure
def test_response_closure():
    def module_fail_json(msg):
        print(('FAIL %s' % msg))

    def module_exit_json(**kwargs):
        print(('EXIT %s' % str(kwargs)))

    module = type('', (object,), dict(fail_json=module_fail_json,
                                      exit_json=module_exit_json))

    rc = []
    for i in range(1, 4):
        rc.append(response_closure(module, 'Question', ['response%s' % i]))

    for _ in range(3):
        try:
            res = rc[0]({})
            print(res)
        except SystemExit:
            pass


# Generated at 2022-06-13 05:25:21.433204
# Unit test for function main
def test_main():
    import pexpect
    import os
    import sys
    import getpass
    import time

    the_user = getpass.getuser()
    tmp_file = None
    try:
        tmp_file = open("/tmp/%s.txt" % the_user, "w")
        print("Printing a message")
        tmp_file.write("Printing a message")
        tmp_file.close()

        command_string = "/usr/bin/cat /tmp/%s.txt" % the_user
        print(command_string)
        print(type(command_string))
        responses = {
            r"Printing a message": "Got the message"
        }
        print(type(responses))
        main()

    finally:
        if tmp_file is not None:
            tmp_file.close()


# Generated at 2022-06-13 05:25:32.472110
# Unit test for function response_closure
def test_response_closure():

    args = 'test'
    responses = {
        'abc': 'abc\n',
        'cde': [ 'cde1\n', 'cde2\n', 'cde3\n' ]
    }
    expected = {
        'abc': [ 'abc\n' ],
        'cde': [ 'cde1\n', 'cde2\n', 'cde3\n' ]
    }
    actual = {}

    class MyModule(object):
        def fail_json(self, *args, **kwargs):
            raise Exception()

    for key in responses:
        actual[key] = []
        for i in range(4):
            actual[key].append(response_closure(MyModule(), key, responses[key])({}))

    assert expected == actual

# Generated at 2022-06-13 05:25:35.834333
# Unit test for function response_closure
def test_response_closure():
    responses = ['1', '2', '3']
    responses_gen = response_closure(module=None, question='Q1', responses=responses)
    assert responses_gen(None) == b'1\n'
    assert responses_gen(None) == b'2\n'
    assert responses_gen(None) == b'3\n'

# Generated at 2022-06-13 05:25:47.462768
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(type='str'),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        ),
        supports_check_mode=False
    )

    if not HAS_PEXPECT:
        module.fail_json(msg=missing_required_lib("pexpect"),
                         exception=PEXPECT_IMP_ERR)

    chdir = module.params['chdir']
    args = module.params['command']
    creates = module.params['creates']

# Generated at 2022-06-13 05:26:01.242153
# Unit test for function response_closure
def test_response_closure():
    import sys
    import unittest
    class Main(object):
        def __init__(self):
            self.params = {}
            for k, v in params.items():
                self.params[k] = v

        def fail_json(self, **kwargs):
            print(kwargs)
    params = {'responses': {'Question': ['foo', 'bar', 'baz']},
              'command': 'foo',
              }

    class TestResponseClosure(unittest.TestCase):
        def test_return(self):
            self.assertEquals(response_closure(sys.modules['__main__'].Main(),
                                               params['responses'].keys()[0],
                                               params['responses'].values()[0])
                                               (None), 'foo\n')


# Generated at 2022-06-13 05:26:01.812440
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:26:02.622501
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:26:35.538839
# Unit test for function main
def test_main():
    pexpect.spawn = PeekSpawn(responses=[
        ('.*\[sudo\] password for foobar:', 'BAR'),
    ])
    module = AnsibleModule(dict(
        command="sudo ls /root",
        chdir="root",
        creates="root",
        removes="/root/ansible_test",
        responses={"[sudo] password for foobar:": 'BAR'},
        timeout=30,
        echo=False,
    ))


# Generated at 2022-06-13 05:26:42.108943
# Unit test for function response_closure
def test_response_closure():
    class FakeModule(object):
        def __init__(self):
            self.fail_json_called = False

    def fail_json(*args, **kwargs):
        self.fail_json_called = True

    module = FakeModule()
    module.fail_json = fail_json

    question = 'question'
    responses = ['foo', 'bar', 'baz']
    resp = response_closure(module, question, responses)

    assert resp({'child_result_list': []}) == 'foo\n'
    assert resp({'child_result_list': []}) == 'bar\n'
    assert resp({'child_result_list': []}) == 'baz\n'
    assert resp({'child_result_list': []}) == 'foo\n'
    assert resp({'child_result_list': []})

# Generated at 2022-06-13 05:26:49.232548
# Unit test for function main
def test_main():
    args = dict(
        command="echo '1'",
        responses=dict(
            echo="1",
        )
    )

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    # Ensure that we have the proper exit code
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

# Generated at 2022-06-13 05:26:50.118057
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:26:50.628643
# Unit test for function main
def test_main():
  print(main())

# Generated at 2022-06-13 05:26:59.581692
# Unit test for function response_closure
def test_response_closure():
    responses = ['response1', 'response2', 'response3']
    response = response_closure(AnsibleModule(argument_spec={}), 'MyQuestion', responses)
    full_out = b''

    for i in range(len(responses)):
        full_out, result = response({'child_result_list': [full_out]})
        assert result == b'response%d\n' % (i + 1)

    try:
        response({'child_result_list': [full_out]})
    except SystemExit as e:
        assert e.code == 1
    else:
        # make pyflakes happy
        assert False

# Generated at 2022-06-13 05:27:07.741443
# Unit test for function main
def test_main():
    my_input = '''
    ---
    # delete the database with certain name
    - name: Test case for main()
      hosts: localhost
      tasks:
        - name: input
          assert:
            that:
              - 3 == 3
          expect:
            echo: true
            command: passwd mattmartz
            responses:
              test: passwd
              password: test
              Re-enter: test
    '''
    m_args = AnsibleModule(argument_spec=dict())
    m_args.check_mode = False
    m_args.no_log = False

# Generated at 2022-06-13 05:27:09.085952
# Unit test for function main
def test_main():
    print("Test1: Ansible expect module")
    main()

# Generated at 2022-06-13 05:27:20.337399
# Unit test for function main
def test_main():
    mock_module = Mock(**dict(
        argument_spec=dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        ),
        params = dict(
            chdir=None,
            creates=None,
            removes=None,
            timeout=30,
            echo=False,
            responses=[],
            command=[]
        ),
        fail_json = Mock(),
        exit_json = Mock(),
    ))
    mock_pexpect = Mock()
    mock_pexpect.__version__ = "3.3"


# Generated at 2022-06-13 05:27:29.985490
# Unit test for function main
def test_main():
    import json
    import mock
    from ansible.module_utils.common._text import to_text
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    result = dict(
        cmd='command',
        stdout='some stdout',
        stderr='some stderr',
        rc=1,
        start='start',
        end='end',
        delta='delta',
        changed=True,
    )
    result_success = result.copy()
    result_success.update(dict(
        stdout='no stdout',
        stderr='no stderr',
        rc=0,
    ))

    # We need to provide pexpect.run without any side-effects in the global
    # namespace for this to work.
    # For this to work,

# Generated at 2022-06-13 05:28:18.115667
# Unit test for function response_closure
def test_response_closure():
    import ansible_module_expect as ame
    import itertools

    module = AnsibleModule(
        argument_spec=dict(
            responses=dict(type='dict', required=True),
        )
    )
    responses = ['first', 'second', 'third']
    response = ame.response_closure(module, 'Question', responses)
    for expected, actual in itertools.zip_longest(
            responses, [response({}), response({}), response({})]):
        assert to_text(expected) == to_text(actual)

# Generated at 2022-06-13 05:28:27.656265
# Unit test for function response_closure
def test_response_closure():
    # test that the closure returns the right responses
    module = AnsibleModule(argument_spec={})
    responses = ['response1','response2','response3','response4']
    responses_closure = response_closure(module, 'Question', responses)
    assert responses_closure({'child_result_list':[]}) == b'response1\n'
    assert responses_closure({'child_result_list':[]}) == b'response2\n'
    assert responses_closure({'child_result_list':[]}) == b'response3\n'
    assert responses_closure({'child_result_list':[]}) == b'response4\n'
    # Check the closure fails correctly when out of responses
    run_raised = False

# Generated at 2022-06-13 05:28:34.289115
# Unit test for function response_closure
def test_response_closure():
    import mock
    import os

    # Change to the expected pwd
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    module = mock.Mock()
    question = 'Question?'
    responses = ['response1\n', 'response2\n', 'response3\n']

    func = response_closure(module, question, responses)

    func({'child_result_list': ['response1\n']})
    func({'child_result_list': ['response1\n']})
    func({'child_result_list': ['response1\n']})

# Generated at 2022-06-13 05:28:47.241952
# Unit test for function main
def test_main():

    # Create a Mock module
    module = type('module', (object,), {'exit_json': exit_json, 'fail_json': fail_json})

    # Create a Mock class
    class Mockpexpect:
        @staticmethod
        def run(command, events, timeout, echo, cwd):
            return ('Mock Output', 0)

        @staticmethod
        def __version__():
            return '3.3'

    # Define the class and staticmethods
    pexpect = type('pexpect', (object,), {'run': Mockpexpect.run, '__version__': Mockpexpect.__version__})

    # Define the arguments

# Generated at 2022-06-13 05:28:53.186542
# Unit test for function response_closure
def test_response_closure():
    import tempfile
    import subprocess
    import os

    _, script_path = tempfile.mkstemp(text=True)

# Generated at 2022-06-13 05:28:59.594327
# Unit test for function main
def test_main():
    test_module = {
        "command": "command",
        "chdir": "chdir",
        "creates": "creates",
        "removes": "removes",
        "responses": {},
        "timeout": 0,
        "echo": False
    }


# Generated at 2022-06-13 05:29:00.235626
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:29:09.348459
# Unit test for function main
def test_main():
    print("Hello world")
    args = "echo Hello world"
    with patch.object(AnsibleModule, 'fail_json') as mocked_fail_json:
        mocked_fail_json.return_value = None
        with patch.object(pexpect, 'run') as mocked_pexpect_run:
            print("\tTesting result code 0")
            mocked_pexpect_run.return_value = "Hello world\n".encode("utf-8"), 0
            main()
            print("\tTesting result code None")
            mocked_pexpect_run.return_value = None, None
            main()
            print("\tTesting result code 1")
            mocked_pexpect_run.return_value = "Hello world\n".encode("utf-8"), 1
            main()
            print("Finished")

# Generated at 2022-06-13 05:29:16.641852
# Unit test for function response_closure
def test_response_closure():
    def _response_closure(responses):
        # Fake AnsibleModule instance
        class FakeAnsibleModule(object):
            def fail_json(self, msg, **kwargs):
                raise AssertionError(msg)

        module = FakeAnsibleModule()

        question = 'An important question'
        actual = response_closure(module, question, responses)

        # Keep track of expected responses
        expected_iter = iter(responses)

        # Keep track of actual responses generated
        actual_responses = []

        # Keep track of child_result_list for fail_json()
        child_result_list = []

        # Call actual() enough times to exhaust the responses

# Generated at 2022-06-13 05:29:28.293990
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils._text import to_text

    module = AnsibleModule(
        argument_spec=dict(
            responses=dict(type='dict', required=True),
        )
    )

    def test_response_closure_generic(q, r, should_error=False):
        questions = {to_text(q): r}
        r = response_closure(module, q, r)
        responses = []
        child_result_list = []

# Generated at 2022-06-13 05:30:56.818144
# Unit test for function main
def test_main():
    import pytest
    import json
    import os
    import os.path

    import ansible.module_utils.basic
    import ansible.module_utils._text

    #
    # Stub results from remote
    #
    from ansible.modules.remote_management.windows import win_command
    from ansible.modules.remote_management.windows import win_wmic
    from ansible.modules.remote_management.windows import win_uri

    def stub_execute_command(cmd, args):
        if 'wmic' in cmd and len(args) == 2 and 'process' in cmd \
                and args[0] == 'call' and args[1] == 'create':
            return (0, '', '')


# Generated at 2022-06-13 05:31:04.310973
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.common.collections import ImmutableDict
    module = ImmutableDict(
        fail_json=lambda msg, **kwargs: msg,
    )
    responses = ['response1', 'response2', 'response3']
    question = 'Question'
    response = response_closure(module, question, responses)
    for i in range(len(responses)):
        assert(response({}).decode() == responses[i])
    with pytest.raises(ValueError) as excinfo:
        response({'child_result_list':[]})
    assert('No remaining responses for \'Question\', output was '
        in str(excinfo.value))

# Generated at 2022-06-13 05:31:15.688085
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
        )
    )

    responses = {
        'Does this work' : [ 'Yes it does', 'No it does not' ],
        'Do this' : 'Done',
        'Do that' : 'Also done'
    }

    response_function = response_closure(
        module, 'Does this work', responses['Does this work']
    )
    assert response_function({'child_result_list': []}) == 'Yes it does\n'
    assert response_function({'child_result_list': []}) == 'No it does not\n'

# Generated at 2022-06-13 05:31:22.610035
# Unit test for function main
def test_main():
    assert fire_command(command='echo 1', response='1')
    assert fire_command(command='echo 0', response='0')
    assert fire_command(command=None, response='0')
    assert fire_command(command='echo 1', response='2')
    assert fire_command(command='echo 1', response='1')
    assert fire_command(command='echo 0', response='1')
    assert fire_command(command='echo 0', response='0')

import unittest

# Generated at 2022-06-13 05:31:34.472988
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(argument_spec={})
    m.fail_json = lambda **kwargs: kwargs

    # test_gen
    r = response_closure(m, 'question', ['response1', 'response2', 'response3'])
    assert r({}) == b'response1\n'
    assert r({}) == b'response2\n'
    assert r({}) == b'response3\n'

    # test_recursion
    try:
        r({})
    except Exception as e:
        msg = to_text(e)
    assert msg == "No remaining responses for 'question', " \
                  "output was ''"

    # test_literal
    r = response_closure(m, 'question', 'response')


# Generated at 2022-06-13 05:31:41.929705
# Unit test for function response_closure
def test_response_closure():
    import mock
    import pexpect
    from pprint import pprint
    from subprocess import Popen, PIPE
    from .basic import to_bytes
    from .expect import response_closure

    test_script = """#!/bin/bash
echo "foo bar"
echo "baz bang"
read -p "Question: " -ra answer
echo $answer
read -p "Question: " -ra answer
echo $answer
read -p "Question: " -ra answer
echo $answer
read -p "Question: " -ra answer
echo $answer
"""

    with open('test_script', 'wb') as f:
        f.write(to_bytes(test_script))

    os.chmod('test_script', 0o755)

# Generated at 2022-06-13 05:31:50.126805
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
    global PEXPECT_IMP_ERR
    PEXPECT_IMP_ERR = 0

    global HAS_PEXPECT
    HAS_PEXPECT = True

    print("Test Expect Module")
    print("==================")
    print("PEXPECT_IMP_ERR: " + str(PEXPECT_IMP_ERR))

# Generated at 2022-06-13 05:31:58.876356
# Unit test for function response_closure
def test_response_closure():
    from types import MethodType

    class FakeModule(object):
        def __init__(self):
            pass
        def fail_json(self, msg):
            print(msg)

    aFakeModule = FakeModule()

    result = response_closure(aFakeModule, "hi", ["a", "b"])

    assert isinstance(result, MethodType)

    assert result(dict()) == b'a\n'
    assert result(dict()) == b'b\n'

    caught = False
    try:
        result(dict())
    except SystemExit as e:
        caught = True
        assert e.code == 1

    assert caught == True

# Generated at 2022-06-13 05:32:06.524271
# Unit test for function main
def test_main():
    # Test pexpect with an exception
    pexpect = 'test_pexpect'
    test_main.mock_pexpect = False
    def pexpect_side_effect(*args, **kwargs):
        if not test_main.mock_pexpect:
            raise pexpect.ExceptionPexpect('An error occurred')
        else:
            return (b'test\n', 0)
    pexpect.run = pexpect_side_effect
    ansible_module = AnsibleModule(dict(command='/bin/ls', creates=None, removes=None, responses={}, timeout=5, echo=False))
    with pytest.raises(SystemExit):
        main()
    # Test pexpect with a TimeoutExpired exception

# Generated at 2022-06-13 05:32:07.256310
# Unit test for function main
def test_main():
    main()