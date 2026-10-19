

# Generated at 2022-06-13 05:23:48.918097
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import load_fixture
    from ansible.module_utils.local import LocalAnsibleModule

    yaml_fixture = load_fixture('expect', 'expect_fixture.yml')
    mock_args = yaml_fixture[0]
    mock_args['command'] = load_fixture('expect', mock_args['command'])
    module = LocalAnsibleModule(**mock_args)

    # Set pexpect version manually, for module testing
    module.pexpect_version = '3.3'

    try:
        main()
    except AssertionError as e:
        assert True, '%s' % e

    # Set pexpect version manually, for module testing, to the lowest supported

# Generated at 2022-06-13 05:23:56.983322
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

  # with patch.object(pexpect, "HAS_PEXPECT", True):
  #   with patch.object(pexpect, "_run", return_value=('',0)):
  #       with patch.object(os.path, "exists", return_value=False):
  #           with patch.object(pexpect, "pexpect", Exception):
  #               main()

# Generated at 2022-06-13 05:24:04.617026
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.six import StringIO
    from ansible.module_utils import common

    class FakeModule(object):
        def __init__(self, exit_json=None, fail_json=None):
            self.exit_json = exit_json
            self.fail_json = fail_json


# Generated at 2022-06-13 05:24:12.516447
# Unit test for function main
def test_main():

    # Prepare required module parameters and test arguments
    args = dict(
        command = 'helper',
        responses = dict(
            Question = 'Response'
        )
    )

    # Initialize arguments
    set_module_args(args)

    # Test AnsibleModule initialization and parameters
    m_args = module.params

    assert m_args['command'] == args['command']
    assert m_args['responses'] == args['responses']
    assert m_args['timeout'] == 30
    assert m_args['echo'] == False

    # Test AnsibleModule invocation
    if __name__ == '__main__':
        try:
            main()
        except SystemExit as e:
            raise Exception("Unexpected SystemExit exception: {}".format(e))

# Generated at 2022-06-13 05:24:20.716808
# Unit test for function main
def test_main():
    command = 'echo 123'
    responses = {}
    responses['123?'] = '456\n'
    responses['789?'] = '102938\n'

    module = AnsibleModule(argument_spec=dict(
        command=dict(type='str', required=True),
        echo=dict(type='bool', default=False),
        timeout=dict(type='int', default=30),
        responses=dict(type='dict', required=True),
    ))

    setattr(module, 'params', {
        "command": command,
        "responses": responses,
        "timeout": 3,
        "echo": False
    })

    startd = datetime.datetime.now()
    main()
    endd = datetime.datetime.now()
    delta = endd - startd
    assert to_

# Generated at 2022-06-13 05:24:21.249462
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:24:30.377180
# Unit test for function response_closure
def test_response_closure():
    def test_module(s):
        return AnsibleModule(
            argument_spec=dict()
        )

    module = test_module('test')
    responses = ['one', 'two', 'three']
    response = response_closure(module, 'test', responses)

    assert response({}) == b'one\n'
    assert response({}) == b'two\n'
    assert response({}) == b'three\n'

    with pytest.raises(AnsibleAssertionError) as excinfo:
        response({})
    assert "No remaining responses for 'test'" in str(excinfo.value)

# Generated at 2022-06-13 05:24:36.705550
# Unit test for function main

# Generated at 2022-06-13 05:24:47.107329
# Unit test for function response_closure
def test_response_closure():
    import StringIO
    import sys

    b_out = StringIO.StringIO()
    sys.stdout = b_out

    module = AnsibleModule(argument_spec=dict())

    question = 'Question'
    responses = [
        'response1',
        'response2',
        'response3'
        ]

    response = response_closure(module, question, responses)
    for matched, info in [('Question', dict(child_result_list=[b'First'])),
                          ('Question', dict(child_result_list=[b'Second'])),
                          ('Question', dict(child_result_list=[b'Third'])),
                          ]:
        results = response(info)
        assert results == responses.pop(0) + '\n'

# Generated at 2022-06-13 05:24:54.827051
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleExitJson, AnsibleFailJson, AnsibleModule
    module = AnsibleModule({
        'command' : '/bin/pwd',
        'chdir': '',
        'creates': '',
        'removes': '',
        'responses': {'.*' : 'ok'},
        'timeout' : 30,
        'echo' : True,
    }, check_invalid_arguments=False)
    # Test the import of expected libraries and modules
    # Check that all expected exceptions are raised
    from ansible.module_utils.basic import AnsibleModule
    import pexpect
    try:
        from unittest.mock import patch, MagicMock
    except ImportError:
        from mock import patch, MagicMock

# Generated at 2022-06-13 05:25:18.966790
# Unit test for function response_closure
def test_response_closure():
    class MockAnsibleModule:
        def fail_json(self, *args, **kwargs):
            pass

    module = MockAnsibleModule()
    question = b"Question"
    responses = [b"a", b"b", b"c"]
    gen = response_closure(module, question, responses)
    assert gen(None) == b"a\n"
    assert gen(None) == b"b\n"
    assert gen(None) == b"c\n"

    responses = [b"response1", b"response2", b"response3"]
    gen = response_closure(module, question, responses)
    assert gen(None) == b"response1\n"
    assert gen(None) == b"response2\n"
    assert gen(None) == b"response3\n"

   

# Generated at 2022-06-13 05:25:30.377075
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from io import StringIO
    from unittest.mock import call, patch

    from ansible.module_utils.basic import AnsibleModule, missing_required_lib

    module_args = dict(
        command='true',
        responses=dict(
            question=dict(
                value='response1',
            ),
        ),
    )


# Generated at 2022-06-13 05:25:42.953490
# Unit test for function response_closure
def test_response_closure():
    class ModuleMock:
        def fail_json(self, *args, **kwargs):
            self.output = kwargs

        def __init__(self):
            self.output = None

    class GeneratorMock:
        def __init__(self, items):
            self.items = items
            self.idx = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.idx < len(self.items):
                idx = self.idx
                self.idx += 1
                return to_bytes(self.items[idx])
            else:
                raise StopIteration()

    module = ModuleMock()
    responses = GeneratorMock([b'a', b'b', b'c'])

# Generated at 2022-06-13 05:25:43.643104
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:25:49.239939
# Unit test for function main
def test_main():
    # Mock pexpect
    class mockpexpect:
        @staticmethod
        def run(args, timeout, withexitstatus, events, cwd, echo, encoding):
            return '', 0

    # Mock AnsibleModule
    class mockansiblemodule:
        def __init__(self, argument_spec, bypass_checks=False, no_log=False,
                     check_invalid_arguments=True, mutually_exclusive=None,
                     required_together=None, required_one_of=None,
                     add_file_common_args=False, supports_check_mode=False,
                     required_if=None):
            self.argument_spec = argument_spec
            self.bypass_checks = bypass_checks
            self.no_log = no_log
            self.check_invalid_arguments = check_invalid

# Generated at 2022-06-13 05:25:54.906818
# Unit test for function response_closure
def test_response_closure():
    class FakeModule():
        def __init__(self, responses=None):
            self.responses = responses

        def fail_json(self, msg):
            self.fail_msg = msg

    module = FakeModule({'Question': ['response1', 'response2', 'response3']})
    question = 'Question'
    responses = ['response1', 'response2', 'response3']
    # Create first iterator
    info = dict()
    info['child_result_list'] = list()
    wrapped = response_closure(module, question, responses)
    assert wrapped(info) == b'response1\n'
    assert wrapped(info) == b'response2\n'
    assert wrapped(info) == b'response3\n'
    info['child_result_list'].append('unexpected output')
    wrapped

# Generated at 2022-06-13 05:26:04.913704
# Unit test for function main
def test_main():
    os.environ['ANSIBLE_CONFIG'] = 'test/ansible.cfg'
    from ansible.module_utils.six import PY2

    if not PY2:
        os.environ['LC_ALL'] = 'en_US.UTF-8'

    with open('test/test.command') as f:
        command = f.read()

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


# Generated at 2022-06-13 05:26:15.711244
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(argument_spec=dict())
    # Test that we can return responses in the correct order
    responses = ["one", "two", "three"]
    response = response_closure(module, "Question", responses)
    responses_returned = []
    for i in xrange(len(responses)):
        responses_returned.append(response({}))
    assert responses_returned == responses
    # Test that we can not return more responses than were given
    try:
        response({})
        raise AssertionError("Expected pexpect.ExceptionPexpect")
    except pexpect.ExceptionPexpect:
        pass

# Generated at 2022-06-13 05:26:16.466221
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:26:26.491963
# Unit test for function main
def test_main():
    import pytest
    import getpass
    from ansible.module_utils import basic
    from ansible.module_utils.actions import AnsibleModule
    if getpass.getuser() != 'root':
        pytest.skip("root required")
    AnsibleModule = AnsibleModule(
        argument_spec = dict(
            command = dict(required = True),
            chdir = dict(type = 'str'),
            creates = dict(type = 'str'),
            removes = dict(type = 'str'),
            responses = dict(type = 'dict', required = True),
            timeout = dict(type = 'int', default = 30),
            echo = dict(type = 'bool', default = False),
        )
    )

# Generated at 2022-06-13 05:26:56.738713
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
    # Values used in the arguments of response_closure
    question = 'Question'
    responses = ['response1', 'response2', 'response3']

    # Definition of the expected results
    result1 = response_closure(module, question, responses)
    result2 = response_closure(module, question, responses)
    result3 = response_closure(module, question, responses)
    result4 = response_

# Generated at 2022-06-13 05:27:05.891279
# Unit test for function main
def test_main():
    args = dict(
        command='/tmp/command',
        responses=dict(
            question1=['response1'],
            question2=['response2'],
            question3=['response3'],
        )
    )

    # Test new behavior of list responses
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

    # Test old behavior of string responses

# Generated at 2022-06-13 05:27:17.222220
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import unittest
    from ansible.module_utils._text import to_bytes, to_native

    class TestResponseClosure(unittest.TestCase):
        def setUp(self):
            self.module = AnsibleModule(
                argument_spec=dict()
            )
            self.out = StringIO()
            self.module.exit_json = lambda **kwargs: self.out.write(to_native(self.module.jsonify(kwargs)))

        def test_generator(self):
            question = 'test'
            response = ['1', '2', '3']
            wrapped = response_closure(self.module, question, response)

# Generated at 2022-06-13 05:27:27.699390
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import json
    import os

    def _get_stdout(args):
        startd = datetime.datetime.now()


# Generated at 2022-06-13 05:27:41.698985
# Unit test for function response_closure
def test_response_closure():
    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.failures = list()

        def fail_json(self, msg):
            self.failures.append(msg)

    module = FakeModule()
    question = "question"
    responses = ["a", "b", "c"]
    response = response_closure(module, question, responses)

    # First call returns 'a\n', second call returns 'b\n', and third
    # call returns 'c\n'
    for expected in map(lambda x: to_bytes(x + '\n'), responses):
        result = response(dict())
        assert result == expected

    # The fourth call should fail the module
    response(dict())

# Generated at 2022-06-13 05:27:47.018875
# Unit test for function main
def test_main():
    subprocess.run(["touch /tmp/ansible_test_file_for_expect"], shell=True)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    print(pytest_wrapped_e.type)
    print(pytest_wrapped_e.value)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
    subprocess.run(["rm /tmp/ansible_test_file_for_expect"], shell=True)

# Generated at 2022-06-13 05:27:59.975603
# Unit test for function main
def test_main():
    args = {'command': 'ls /home/test', 'chdir': '', 'creates': '', 'removes': '', 'responses': {'(?i)password:': 'MySekretPa$$word'}, 'timeout': 30, 'echo': False}

# Generated at 2022-06-13 05:28:09.301126
# Unit test for function main
def test_main():
    argument_spec = {
        'command': dict(required=True),
        'chdir': dict(type='path'),
        'creates': dict(type='path'),
        'removes': dict(type='path'),
        'responses': dict(type='dict', required=True),
        'timeout': dict(type='int', default=30),
        'echo': dict(default=False, type="bool"),
    }

    res_data = {"failed": False, "rc": 0, "changed": True, "start": "aaaaa",
                "delta": "aaaa", "end": "aaaaa", "cmd": "ls", "stdout": "aaaa"}
    module = AnsibleModule(argument_spec, supports_check_mode=True)

# Generated at 2022-06-13 05:28:09.956470
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:28:20.064380
# Unit test for function response_closure
def test_response_closure():
    import contextlib

    class Module(object):
        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

    responses = {
        'Question 1': 'Response 1',
        'Question 2': ['Response 2-1', 'Response 2-2'],
        'Question 3': ['Response 3-1', 'Response 3-2']}

    module = Module()
    q = 'Question 2'
    r = responses[q]
    f = response_closure(module, q, r)

    # Return Response 2-1
    with contextlib.ExitStack() as es:
        g = es.enter_context(f({}))
        assert g == 'Response 2-1\n'

    # Return Response 2-2

# Generated at 2022-06-13 05:29:24.376347
# Unit test for function response_closure
def test_response_closure():
    import doctest
    import inspect
    result = doctest.testmod(inspect.getmodule(test_response_closure))
    if result[0] > 0:
        raise RuntimeError('test failures: %s', result[1])

# Generated at 2022-06-13 05:29:35.695639
# Unit test for function main
def test_main():
    import mock
    import os
    import pexpect

    import ansible.module_ansible.expect
    import ansible.module_ansible.expect.argspec
    import ansible.module_ansible.expect.loader

    class AnsibleModuleMock(object):
        class FailJson(object):
            def __init__(self, module, msg='non-zero return code', **kwargs):
                self.kwargs = kwargs
                self.msg = msg
                self.module = module

        def __init__(self, argument_spec):
            self.argument_spec = argument_spec
            self.params = {}
            self.check_mode = False
            self.diff = False

        def fail_json(self, msg='non-zero return code', **kwargs):
            raise self.FailJ

# Generated at 2022-06-13 05:29:49.437809
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
    responses = ['r1', 'r2', 'r3']
    question = 'Question'
    i = 0

    response = response_closure(module, question, responses)
    while i < len(responses):
        next_response = response({'child_result_list': [],
                                  'result_item': ''})
        assert next_response == to_bytes(responses[i])

# Generated at 2022-06-13 05:29:49.812024
# Unit test for function main
def test_main():

    main()

# Generated at 2022-06-13 05:29:57.173081
# Unit test for function main

# Generated at 2022-06-13 05:30:09.377284
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

    question = 'What is your name?'
    responses = ['John', 'Jane']
    rc = response_closure(module, question, responses)
    assert b'John' == rc({'child_result_list': []})
    assert b'Jane' == rc({'child_result_list': []})

    question = 'Another question'

# Generated at 2022-06-13 05:30:21.076334
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import os
    import sys
    import pytest

    # Make sure pexpect is present
    try:
        import pexpect
        HAS_PEXPECT = True
    except ImportError:
        pytest.skip('pexpect is not installed')

    # Make sure pexpect version is at least 3.3
    if not hasattr(pexpect, '_run'):
        pytest.skip('pexpect version is too old')

    # Prepare input args
    args = ['passwd', 'username']
    env = dict(HOME='/root')

    # Prepare test fixtures
    chdir = '.'
    creates = None
    removes = None

# Generated at 2022-06-13 05:30:31.089501
# Unit test for function main
def test_main():
    command = "cat /etc/hosts"
    creates_file = "/etc/hosts"
    creates_file_exist = True
    removes_file = "/etc/hosts"
    removes_file_exist = True
    timeout = 20
    echo = True
    responses = {
        "sss": "sss",
        "aaa": "aaa"
        }
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
    module.params

# Generated at 2022-06-13 05:30:32.186160
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:30:44.617043
# Unit test for function main
def test_main():
    def run_main(args, responses):
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
        module.exit_json(
            cmd=args,
            stdout="skipped, since %s exists" % creates,
            changed=False,
            rc=0
        )
    
    run_main('ls', 'OK')

# Generated at 2022-06-13 05:32:52.047995
# Unit test for function main
def test_main():
    import random
    import string
    # The two parts of the test
    # 1. Test if main() runs correctly to return a json string
    # 2. Test if the json string is correctly formed

    # Use a simple command that runs /bin/echo so that this test is
    # independent of the current environment.
    # That is, if there is no /bin/echo or if /bin/echo does not
    # have the correct output, the test will fail and we
    # will need to adjust the test rather than a user adjusting
    # their system or someone adjusting the test for their system.
    random_str = ''.join(random.choice(string.ascii_uppercase +
                                       string.digits) for _ in range(10))
    command = '/bin/echo ' + random_str

# Generated at 2022-06-13 05:32:56.409435
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

    responses = ["one", "two", "three"]
    question = "What do you get if you multiply six by nine?"
    result = response_closure(module, question, responses)
    assert result({'child_result_list': ['foo']}) == b'one\n'
    assert result({'child_result_list': ['bar']}) == b'two\n'

# Generated at 2022-06-13 05:33:02.450606
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    values = [
        (1, ['one', 'two', 'three'], b'one\n'),
        (2, ['one', 'two', 'three'], b'two\n'),
        (3, ['one', 'two', 'three'], b'three\n'),
        (4, ['one', 'two', 'three'], False),
    ]
    for test, responses, expected in values:
        module = AnsibleModule(argument_spec=dict())
        result = response_closure(module, 'question', responses)
        if isinstance(expected, bool):
            assert result({}) is expected
        else:
            assert result({}) == expected

# Generated at 2022-06-13 05:33:03.210515
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:33:15.082070
# Unit test for function response_closure
def test_response_closure():
    import io
    import unittest

    class ModuleFake:
        def __init__(self, *args, **kwargs):
            pass

        def fail_json(self, *args, **kwargs):
            raise Exception(args, kwargs)

    class MyTestCase(unittest.TestCase):
        def test_response_closure_1(self):
            # Simply test that response_closure returns a function
            # to handle responses
            module = ModuleFake()
            question = 'A question?'
            responses = ['response 1', 'response 2', 'response 3']
            closure = response_closure(module, question, responses)
            self.assertTrue(callable(closure))

        def test_response_closure_2(self):
            # Test that the closure function raises an exception when
            # it runs out of responses
            module

# Generated at 2022-06-13 05:33:22.871223
# Unit test for function main
def test_main():
    #####################################################################
    # Test modules
    import tempfile, re, os

    # Test module imports
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native, to_text
    from ansible.module_utils.basic import missing_required_lib

    # Test modules have the right implementation
    assert to_bytes('hello') == b'hello'
    assert to_native('hello') == 'hello'
    assert to_text('hello') == 'hello'

    assert missing_required_lib('pexpect') == 'python module pexpect required'

    ####################################################################
    # Test Exit Json