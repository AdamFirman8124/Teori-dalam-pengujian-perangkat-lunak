

# Generated at 2022-06-13 05:23:37.595922
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:23:43.311095
# Unit test for function response_closure
def test_response_closure():
    test_module = object()
    test_question = 'test_question'
    test_responses = ['response1', 'response2']
    expected = ['response1', 'response1\n', 'response2', 'response2\n']
    test_closure = response_closure(test_module, test_question, test_responses)
    actual = []

    for x in range(0, 4):
        actual.append(test_closure(object()))

    assert actual == expected

# Generated at 2022-06-13 05:23:53.292314
# Unit test for function main
def test_main():
    # Import re, which has been removed as a dependency in 2.5,
    # but we still need it to test `pattern.search`
    import re
    #import random
    #import pprint

    # Create a test class for the AnsibleModule class
    # pylint: disable=invalid-name
    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args['failed'] = True
            raise Exception(kwargs['msg'])

        def exit_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args['failed'] = False

    # Create a test class for the IsADirectory

# Generated at 2022-06-13 05:24:00.505253
# Unit test for function main
def test_main():
    assert_raises(AnsibleFailJson, main, {}, {
        'command': '',
        'responses': {
            'Question': "Answer"
        },
        'timeout': None
    })

    try:
        main({}, {
            'command': 'ls',
            'responses': {
                'Question': "Answer"
            },
            'timeout': None
        })
    except Exception as e:
        assert False, "Unexpected Exception: " + str(e)

    main({}, {
        'command': 'ls',
        'responses': {
            'Question': ["Answer", "Answer"]
        },
        'timeout': None
    })

# Generated at 2022-06-13 05:24:01.674707
# Unit test for function main
def test_main():
    out = main()
    assert out is not None

# Generated at 2022-06-13 05:24:03.622123
# Unit test for function main
def test_main():
    print ("Start test_main")
    assert True is not False
    print ("End test_main")

# Generated at 2022-06-13 05:24:12.162897
# Unit test for function main
def test_main():
  import pexpect
  import tempfile
  import os

  def run_expect(cmd, responses, timeout=60, chdir=None):
    # suppress output
    t = tempfile.TemporaryFile()
    events = {}
    for key, value in responses.items():
      events[to_bytes(key)] = to_bytes(value)
    try:
      b_out = pexpect.run(cmd, timeout=timeout, events=events, cwd=chdir,
                          withexitstatus=True, echo=False, encoding=None,
                          outfile=t, logfile=t)
    except pexpect.ExceptionPexpect as e:
      print('run_expect failed: %s' % e)
      return
    t.seek(0)
    return b_out

  # Test echo

# Generated at 2022-06-13 05:24:22.138860
# Unit test for function response_closure
def test_response_closure():
    # Using fixtures from main()
    test_module = AnsibleModule(
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

    test_args = 'ls -l'
    test_chdir = None
    test_creates = None
    test_removes = None

    test_responses = {
        'question1': ['yes', 'no'],
        'question2': ['yes', 'no'],
    }


# Generated at 2022-06-13 05:24:31.896217
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict()
    )

    question = 'Question'
    response_strings = [
        'response1',
        'response2',
        'response3']
    closure = response_closure(module, question, response_strings)

    assert closure(dict()) == b'response1\n'
    assert closure(dict()) == b'response2\n'
    assert closure(dict()) == b'response3\n'
    module.fail_json.called_once_with(msg="No remaining responses for '%s', "
                                          "output was ''" %
                                          question)

# Generated at 2022-06-13 05:24:43.080203
# Unit test for function main
def test_main():

    import json
    import sys
    import shlex
    from ansible.module_utils import basic
    from ansible.compat.tests.mock import patch, Mock
    from ansible.module_utils.six.moves import builtins

    class FakeStream:

        def __init__(self):
            self.contents = ''

        def write(self, data):
            self.contents += data

        def flush(self):
            pass

    fake_stdin = FakeStream()
    fake_stdout = FakeStream()


# Generated at 2022-06-13 05:25:01.786765
# Unit test for function response_closure
def test_response_closure():
    import pexpect
    import StringIO
    import sys

    class ModuleFailException(Exception):
        pass

    class MockModule(object):
        def __init__(self):
            self.fail_json_args = []

        def fail_json(self, *args, **kwargs):
            self.fail_json_args.append((args, kwargs))
            raise ModuleFailException()

    class MockPexpect(object):
        def __init__(self, *args, **kwargs):
            self._spawn_args = (args, kwargs)
            self._child_result_list = []
            self.child_result_list = self._child_result_list.append


# Generated at 2022-06-13 05:25:06.714454
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

# Generated at 2022-06-13 05:25:12.432440
# Unit test for function main
def test_main():
    args = [__file__, '-m', 'test_action_plugin.expect',
            '-a', "command=ls -l / | grep passwd"]
    from ansible.cli import CLI
    cli = CLI(args)
    cli.parse()
    cli.run()

# Generated at 2022-06-13 05:25:21.944371
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as result:
        main()
    assert not result.value.args[0]['changed']
    assert result.value.args[0]['rc'] == 0
    assert result.value.args[0]['start'] == '2019-04-02 18:08:40.692243'
    assert result.value.args[0]['end'] == '2019-04-02 18:08:40.692243'
    assert result.value.args[0]['delta'] == '0:00:00.000053'
    assert result.value.args[0]['cmd'] == 'echo hello'
    assert result.value.args[0]['stdout'] == 'hello'



# Generated at 2022-06-13 05:25:33.116873
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    import io
    import sys

    class TestModule(AnsibleModule):
        pass

    # Set up test inputs, including mock module
    test_responses_list = [
        ['response1', 'response2', 'response3'],
        ['response4', 'response5'],
    ]

    test_question = 'Question'

    # Set up mock module
    sys.stdout = io.StringIO()
    test_module = TestModule()

    # Set up mock response closure
    response_closure_result = response_closure(test_module,
                                               test_question,
                                               test_responses_list[0])

    # Test expected results
    # - First question returns first response

# Generated at 2022-06-13 05:25:45.508559
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.command_question import CommandQuestion
    from ansible.module_utils.common.command_question import _ANSI_COLORS_PATTERN
    from ansible.module_utils.common.command_question import _ANSIBLE_COLORS_PATTERN
    import ansible.module_utils.basic
    import ansible.module_utils.action_plugins.command
    import pexpect
    import os

    argv = [
        'ansible-test',
        'expect',
        '--command=/bin/bash',
        '--responses',
        '{"Prompt": {"text": "Response", "error": "Error"}}',
    ]

# Generated at 2022-06-13 05:25:59.431900
# Unit test for function response_closure
def test_response_closure():
    # Simple function test
    from ansible.module_utils import basic  # pylint: disable=import-error
    basic.ANSIBLE_MODULE_ARGS = {'command': '/path/to/command', 'responses': {'foo': ['bar', 'baz']}}
    basic.ANSIBLE_MODULE_RETVALS = {}

    response_closure(basic.AnsibleModule(argument_spec={}), 'foo', ['bar', 'baz'])

    # Test function call with error
    basic.ANSIBLE_MODULE_RETVALS['fail_json'] = None

    try:
        response_closure(basic.AnsibleModule(argument_spec={}), 'foo', []).__call__({})
    except SystemExit:
        pass


# Generated at 2022-06-13 05:26:06.800398
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import MutableMapping

    def mocked_module(*args):
        print("mocked_module args: %s" % args)
        import sys
        sys.modules['ansible'] = MockAnsibleModule()
        from ansible.module_utils.common.collections import ImmutableDict
        return MockAnsibleModule(argument_spec = ImmutableDict(type='dict', required=True))

    class MockAnsibleModule():
        def __init__(self, argument_spec=None):
            self.fail_json_called = False
            self.fail_json_args = {}
            self.fail_json_kwargs = {}


# Generated at 2022-06-13 05:26:19.552775
# Unit test for function main
def test_main():
    import datetime
    # for unit tests, it's necessary to clear this out of the namespace
    global main
    main()

    # Define a rule to catch the output and check that it is what we expect.
    # This will be called once for each call to
    # AnsibleModule.fail_json(*args, **kwargs)
    # during each test run.

    # This is necessary to be able to test error conditions
    # without having to resort to mocking and stubbing.
    def fail_json(*args, **kwargs):
        """Fail with supplied arguments
        This is a wrapper around AnsibleModule.fail_json, that stores information about
        calls to AnsibleModule.fail_json for test validation.
        """
        # keep track of the args to AnsibleModule.fail_json
        # to check in the test cases
        FailJson

# Generated at 2022-06-13 05:26:30.149412
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import action

    import pexpect
    import unittest

    #  cmd, chdir, creates, removes, responses, timeout, echo,
    args_dict = dict(
        command='passwd username',
        chdir=None,
        creates=None,
        removes=None,
        responses=dict(),
        timeout=30,
        echo=False,
        _ansible_check_mode=False,
        _ansible_debug=False,
        _ansible_diff=False,
        _ansible_verbosity=0,
    )

    # Create an instance of the module class
    test_module = action.ActionModule(argument_spec=args_dict)

    #  class pexpect.spawn(command, args=[], timeout=30

# Generated at 2022-06-13 05:27:01.380481
# Unit test for function main
def test_main():
    import pexpect
    import pexpect.exceptions
    from ansible.module_utils.basic import AnsibleModule

    # run the module
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

# Generated at 2022-06-13 05:27:02.721478
# Unit test for function main
def test_main():
    unit_test.main()

# Generated at 2022-06-13 05:27:12.897059
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
                ),
            )
    module.check_mode = False
    command = module.params['command']
    chdir = module.params['chdir']
    creates = module.params['creates']
    removes = module.params['removes']
    responses = module.params['responses']
    timeout = module.params['timeout']
    echo = module.params['echo']
    
    main()

# Generated at 2022-06-13 05:27:21.155913
# Unit test for function response_closure
def test_response_closure():
    m = AnsibleModule(argument_spec={'responses': {'type': 'dict', 'required': True}})
    question = 'Foo'
    responses = ['foo', 'bar']
    func = response_closure(m, question, responses)
    assert func({'child_result_list': ['baz']}) == b'foo\n'
    assert func({'child_result_list': ['baz']}) == b'bar\n'
    assert b'No remaining responses for' in m.fail_json.call_args[0][0]

# Generated at 2022-06-13 05:27:22.310408
# Unit test for function main
def test_main():
    result = None
    pass

# Generated at 2022-06-13 05:27:31.170043
# Unit test for function response_closure
def test_response_closure():
    class FakeModule:
        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

    module = FakeModule()

    qa_pair = [
        ('my question', 'answer1'),
        ('my question', ['answer1', 'answer2']),
        ('my question', ['answer1', 'answer2', 'answer3']),
        ('question2', ['answer1', 'answer2'])
    ]

    for key, value in qa_pair:
        response = response_closure(module, key, value)
        assert response(None) == b'answer1\n'
        if isinstance(value, list):
            for i in value:
                assert response(None) == b'%s\n' % to_bytes(i)

# Generated at 2022-06-13 05:27:43.808065
# Unit test for function main
def test_main():
    args = command, chdir, creates, removes, responses, timeout, echo = 'command', 'chdir', 'creates', 'removes', 'responses', 300, True
    pexpect.__version__ = '1'
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value == 1

##
# Test response_closure
#
# 1. Test that all elements of the list are yielded and the StopIteration exception is raised.
#    The info['child_result_list'][-1] element is the last line of pexpect output.
#    This will be the last expected response and the line that raised the StopIteration exception.
#    This will be the last line of the output.

# 2. Test that the response is repeated if the responses argument is a string.


# Generated at 2022-06-13 05:27:47.753611
# Unit test for function main
def test_main():
    a = to_text(pexpect.__version__)
    print('Current pexpect version is %s' %(a))

# Generated at 2022-06-13 05:27:58.605225
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import pexpect
    import os
    import sys

    mod_globals = dict(
        __file__=os.path.join(sys.prefix, 'ansible', 'modules', 'commands', 'expect.py'),
        __name__='ansible.modules.commands.expect',
        __doc__=__doc__,
    )
    mod_globals.update(globals())
    module = AnsibleModule(
        argument_spec=dict(
            responses=dict(type='dict', required=True),
        )
    )


# Generated at 2022-06-13 05:28:07.714580
# Unit test for function response_closure
def test_response_closure():
    # Import required python libraries
    import ansible.module_utils.basic

    test_responses = {'question': ['response1', 'response2', 'response3']}
    test_closure = response_closure(None, 'question', test_responses['question'])

    info = {'child_result_list': ['array should be empty', 'array should be empty']}
    for expected_response, actual_response in zip(test_responses['question'],
            [test_closure(info), test_closure(info), test_closure(info)]):
        assert to_bytes(expected_response).rstrip(b'\n') == actual_response

    # Now test the fail
    test_closure(info)

# Generated at 2022-06-13 05:29:08.574548
# Unit test for function main
def test_main():
    """ Unit test for function main
    """
    import subprocess
    import os
    import tempfile
    import shutil
    import time

    module_path = os.path.dirname(os.path.abspath(__file__))

    test_dir = tempfile.mkdtemp()

    proc = subprocess.Popen(
        [os.path.join(module_path, __file__), '-vvvv'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=test_dir,
        universal_newlines=True
    )

    # This is a valid command.  We are going to run this through the
    # module and get back the json results.

# Generated at 2022-06-13 05:29:15.966484
# Unit test for function response_closure
def test_response_closure():
    test_filename = os.path.abspath(__file__)
    module = AnsibleModule(
        argument_spec={'command': {'required': True}},
        supports_check_mode=False,
        check_invalid_arguments=False,
        bypass_checks=True
    )
    responses = ["test", "test2", "test3", "test4", "test5"]
    response_next_mock = "test4"
    response = response_closure(module, test_filename, responses)
    assert response({"child_result_list":[]}) == "test\n"
    assert response({"child_result_list":[]}) == "test2\n"
    assert response({"child_result_list":[]}) == "test3\n"

# Generated at 2022-06-13 05:29:24.067167
# Unit test for function main
def test_main():
    Test = namedtuple("Test", "arguments expected")

# Generated at 2022-06-13 05:29:35.460415
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule.exit_json') as m_exit_json:
        p_expect = __import__('pexpect')

        # test no command given
        p_expect.run.reset_mock()
        args = {
            'command': '',
            'chdir': '',
            'creates': '',
            'removes': '',
            'responses': {
                '?': 'thank you',
                'badkey': ''
                },
            'timeout': 10,
            'echo': False
        }
        p_expect.run = MagicMock(return_value = ('skipped', 0))
        main(argv=[], add_finalizer=False, verbosity=0)
        mock_call_exit_json = m_exit_

# Generated at 2022-06-13 05:29:45.533552
# Unit test for function response_closure
def test_response_closure():
    m = AnsibleModule(argument_spec=dict(responses=dict(type='dict', required=True)))
    r = [ "response1", "response2", "response3" ]
    q = "Question"
    r_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in r)
    closure = response_closure(m, q, r)

    child_result_list = []
    assert r_gen.next() == closure({ "child_result_list": child_result_list })
    assert r_gen.next() == closure({ "child_result_list": child_result_list })
    assert r_gen.next() == closure({ "child_result_list": child_result_list })

# Generated at 2022-06-13 05:29:50.880554
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    import copy

    module = AnsibleModule(argument_spec={})
    question = 'foo'
    responses = [ "bar", "baz" ]
    expected_responses = copy.deepcopy(responses)

    closure = response_closure(module, question, responses)

    first_response = closure({})
    assert first_response == b"bar\n"

    second_response = closure({})
    assert second_response == b"baz\n"

    third_response = closure({})
    assert third_response == b"bar\n"

    assert responses == expected_responses

# Generated at 2022-06-13 05:29:52.124587
# Unit test for function main
def test_main():
    input = 'ansible.builtin.expect'
    main(input)

# Generated at 2022-06-13 05:29:57.950343
# Unit test for function response_closure
def test_response_closure():
    """Test response_closure function."""
    import ansible.modules.system.expect as expect

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

    question = u'Are you sure you want to continue connecting'
    responses = [u'yes', u'no']

    response_closure(module, question, responses)

    module.exit_json(changed=True)

# Generated at 2022-06-13 05:30:09.855084
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.common._collections_compat import Mapping
    import pytest

    def response_closure_fixture(module, question, responses):
        return response_closure(module, question, responses)

    class TestModule:
        def fail_json(self, *args, **kwargs):
            raise AssertionError(args[0])

    module = TestModule()
    question = 'question'
    responses = ['response']

    def test_fixture_type():
        assert callable(response_closure_fixture)

    def test_return_type():
        assert callable(response_closure_fixture(module, question, responses))

    def test_return_type_closure_correct_response():
        closure = response_closure_fixture(module, question, responses)

# Generated at 2022-06-13 05:30:21.075618
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(
        argument_spec = dict()
    )
    responses = []
    responses.append("first response")
    responses.append("second response")
    responses.append("third response")

    closure = response_closure(module, "my question", responses)
    info = dict()
    info['child_result_list'] = ["no match"]
    assert closure(info) == b'first response\n'
    assert closure(info) == b'second response\n'
    assert closure(info) == b'third response\n'
    try:
        closure(info)
        assert False
    except AnsibleModuleError as e:
        assert e.args[0] == "No remaining responses for 'my question', output was 'no match'"

# Generated at 2022-06-13 05:32:06.178396
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:32:18.777083
# Unit test for function main
def test_main():
    import sys
    import tempfile
    import time
    import os
    import shutil

    import ansible.module_utils.basic
    import ansible.module_utils._text

    #  Get the current working directory
    #  Setup a temporary directory to emulate the chdir call
    cwd = os.getcwd()
    tempdir = tempfile.mkdtemp()

    #  Configure a basic test scenario
    argv = [
        'ansible-test',
        'expect',
        '--verbosity', 'debug',
        '--command', 'sleep 1'
    ]
    argv.extend(['--chdir', tempdir])
    argv.extend(['--creates', 'expect.txt'])
    argv.extend(['--removes', 'expect.txt'])


# Generated at 2022-06-13 05:32:26.962675
# Unit test for function main
def test_main():
    import mock
    import sys
    import unittest

    try:
        # python3
        from io import StringIO
    except ImportError:
        # python2
        from StringIO import StringIO

    mock_pexpect = mock.MagicMock()
    mock_pexpect.ExceptionPexpect = Exception
    mock_pexpect.__version__ = '0.0'
    mock_pexpect._run.side_effect = AttributeError

    mock_pexpect_run = mock.MagicMock()
    mock_pexpect_run.side_effect = TypeError

    with mock.patch.object(sys, 'modules', {
        'pexpect': mock_pexpect,
        'pexpect.run': mock_pexpect_run,
    }):
        from ansible.modules.system.expect import main

# Generated at 2022-06-13 05:32:32.791007
# Unit test for function main
def test_main():
    import os
    import time
    import datetime

# Generated at 2022-06-13 05:32:43.257420
# Unit test for function response_closure
def test_response_closure():
    class MockModule(object):
        def fail_json(self, msg, **kwargs):
            self.msg = msg

    module = MockModule()
    responses = ['resp0', 'resp1', 'resp2']

    the_closure = response_closure(module, 'question', responses)
    i = 0
    for resp in responses:
        result = the_closure({})
        assert result == to_bytes(resp + '\n')
        i += 1

    # Check that failure occurs on no-more-responses
    the_closure({'child_result_list': ['last child output']})
    assert 'No remaining responses for \'question\', output was \'last child output\'' in module.msg

# Generated at 2022-06-13 05:32:49.440338
# Unit test for function response_closure
def test_response_closure():
    import collections
    argb = "abc"
    argl = ["abc", "def"]
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

    # test single value
    res = response_closure(module, "test", argb)
    resl = list(res)
    assert isinstance(resl[0], bytes)
    assert resl[0] == b'abc\n'

    # test list

# Generated at 2022-06-13 05:32:54.177080
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    def run_module(responses, command=None):
        my_args = dict(
            responses=responses,
        )
        if command is not None:
            my_args['command'] = command
        return basic.AnsibleModule(argument_spec=dict(**my_args))

    def my_fail_json(*args, **kwargs):
        pass

    module = run_module(responses={'Question': 'response'})
    module.fail_json = my_fail_json

    wrapped = response_closure(module, 'Question', ['response1', 'response2'])

    assert wrapped({'child_result_list': [None]}) == b"response1\n"

# Generated at 2022-06-13 05:33:00.768547
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
    module.params['command'] = 'ls'
    module.params['responses'] = {'(?i)ls:': 'yes'}
    main()

# Generated at 2022-06-13 05:33:10.420573
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    responses = ['foo', 'bar', 'baz']
    answer = response_closure(module, 'Question', responses)

    assert answer({}) == 'foo\n'
    assert answer({}) == 'bar\n'
    assert answer({}) == 'baz\n'
    try:
        answer({})
        assert False
    except Exception as e:
        assert to_text(e).endswith('output was \'baz\'')

# Generated at 2022-06-13 05:33:19.685654
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.action.pexpect import pexpect
    import datetime

    def _pexpect_run(*args, **kwargs):
        if kwargs.pop('withexitstatus', None):
            return (to_bytes('ls'), 0)
        return (to_bytes('ls'),)

    pexpect.run = _pexpect_run

    setattr(basic.AnsibleModule, 'exit_json', exit_json)
    setattr(basic.AnsibleModule, 'fail_json', fail_json)
