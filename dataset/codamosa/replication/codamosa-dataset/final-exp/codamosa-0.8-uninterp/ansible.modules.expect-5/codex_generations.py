

# Generated at 2022-06-13 05:23:45.798678
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    t_module = AnsibleModule(argument_spec={})
    f_responses = response_closure(t_module, 't_question', ['t_response1', 't_response2', 't_response3'])
    f_responses({'child_result_list': ['']}) == 't_response1\n'
    f_responses({'child_result_list': ['']}) == 't_response2\n'
    f_responses({'child_result_list': ['']}) == 't_response3\n'
    with pytest.raises(Exception, match=r"No remaining responses for 't_question', output was ''"):
        f_responses({'child_result_list': ['']})

# Generated at 2022-06-13 05:23:49.884163
# Unit test for function main
def test_main():
    with patch('ansible_collections.ansible.builtin.plugins.modules.expect.pexpect') as mock:
        mock.run.return_value = (to_bytes('stdout'), 0)
        main()

# Generated at 2022-06-13 05:23:57.609693
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
    responses = [ 'response1', 'response2' ]
    wrapped_response_closure = response_closure(module, question, responses)

    responses_iterator = iter(responses)
    info = {'child_result_list' : [ 'test_response_closure' ] }

# Generated at 2022-06-13 05:24:04.961501
# Unit test for function response_closure
def test_response_closure():
    class FakeModule(object):
        def __init__(self, name):
            self.name = name

        def fail_json(self, **kwargs):
            raise Exception("Fail JSON: %s" % self.name)

    def test_func(name, responses, expected):
        module = FakeModule("test_func(%s,%s,%s)" % (name, responses, expected))
        result = response_closure(module, name, responses)
        if expected:
            # Test answer provided
            try:
                assert result(None) == expected, 'Response is not %r' % expected
            except:
                raise AssertionError("Expected answer %r" % expected)
        else:
            try:
                result(None)
            except:
                pass

# Generated at 2022-06-13 05:24:08.796747
# Unit test for function main
def test_main():
    args = dict(
        command='command',
        chdir='.',
        creates=None,
        removes=None,
        responses=[dict(key=r'(?i)password', value='MySekretPa$$word')],
        timeout=30,
        echo=True,
    )
    main(args)

# Generated at 2022-06-13 05:24:10.759677
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:24:21.199520
# Unit test for function main
def test_main():
    argument_spec = dict(
        command=dict(required=True),
        chdir=dict(type='path'),
        creates=dict(type='path'),
        removes=dict(type='path'),
        responses=dict(type='dict', required=True),
        timeout=dict(type='int', default=30),
        echo=dict(type='bool', default=False),
    )
    test_args = dict(
        command="foo",
        responses=dict(
            Question=dict(
                -response1,
                -response2,
                -response3,
                )
            )
        )
    # Test the pexpect exception
    test_pexpect_imp_err = "test_pexpect_imp_error"
    test_pexpect_exception = "test_pexpect_exception"
    test_

# Generated at 2022-06-13 05:24:26.488726
# Unit test for function main
def test_main():
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
    # test for exceptions
    with pytest.raises(AnsibleFailJson) as excinfo:
        main()
    assert 'command exceeded timeout' in str(excinfo.value)

# Generated at 2022-06-13 05:24:35.329591
# Unit test for function response_closure
def test_response_closure():
    class Arguments(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = Arguments(**kwargs)

        def fail_json(self, *args, **kwargs):
            raise Exception(args[0])

    class MockChild(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    module = MockModule(responses=dict(question=['a', 'b', 'c']))
    child = MockChild(child_result_list=[''])


# Generated at 2022-06-13 05:24:45.234551
# Unit test for function main
def test_main():
    args = dict(
        command='command',
        chdir=None,
        creates=None,
        removes=None,
        responses={
            'Question': 'Answer'
        },
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

    chdir = args['chdir']
    command = args['command']
    creates = args['creates']

# Generated at 2022-06-13 05:24:55.893453
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:25:02.333429
# Unit test for function main
def test_main():
    #import jk_testing
    import os
    #import pexpect

    b_out, rc = pexpect.run(
        "dir", timeout="2", withexitstatus="True",
        events={"(?i)y/n": "y\n"}, encoding="None"
    )
    print("b_out = " + str(b_out))
    print("rc = " + str(rc))

    b_out, rc = pexpect._run(
        "dir", timeout="2", withexitstatus="True",
        events={"(?i)y/n": "y\n"}, echo="False"
    )
    print("b_out = " + str(b_out))
    print("rc = " + str(rc))

    #print("HAS_PEXPECT = " + str

# Generated at 2022-06-13 05:25:07.143079
# Unit test for function response_closure
def test_response_closure():

    class FakeModule:
        def fail_json(self, msg, **kwargs):
            raise AssertionError(msg)

    module = FakeModule()

    responses = [
        "a",
        "b",
        "c",
    ]

    question = "generic question"

    f = response_closure(module, question, responses)

    responses_copy = responses[:]  # make a copy of the responses for later comparison

    for response in responses_copy:
        # Make sure that each response is generated in order
        assert f(None) == to_bytes(response + "\n")

    # Make sure that once all responses have been consumed, it throws an exception
    try:
        f(None)
        assert False
    except AssertionError as e:
        # Make sure the exception message is what we expect
        assert e.message

# Generated at 2022-06-13 05:25:18.683378
# Unit test for function response_closure
def test_response_closure():
    class FakeModule:
        def __init__(self):
            self.failure = False

        def fail_json(self, msg):
            self.failure = True
            self.msg = msg

    module = FakeModule()

    question = "A question"
    responses = ["foo", "bar"]

    resp = response_closure(module, question, responses)

    assert resp({"child_result_list": []}) == b"foo\n"
    assert resp({"child_result_list": [b"foo\n"]}) == b"bar\n"
    assert resp({"child_result_list": [b"foo\n", b"bar\n"]}) is None
    assert module.failure and module.msg == "No remaining responses for 'A question', output was ''"

# Generated at 2022-06-13 05:25:25.275156
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
    main()

# Generated at 2022-06-13 05:25:25.922381
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:25:35.383486
# Unit test for function response_closure

# Generated at 2022-06-13 05:25:40.838765
# Unit test for function main
def test_main():
    import tempfile

    import pexpect
    import pexpect.fdpexpect
    original_spawn = pexpect.spawn
    original_fdspawn = pexpect.fdpexpect.fdspawn
    pexpect.spawn = lambda *args, **kwargs: PrintWrapper(pexpect.spawn(*args, **kwargs))
    pexpect.fdpexpect.fdspawn = lambda *args, **kwargs: PrintWrapper(pexpect.fdpexpect.fdspawn(*args, **kwargs))

    command = 'echo'

# Generated at 2022-06-13 05:25:49.395468
# Unit test for function main
def test_main():
    import sys
    import os
    import argparse
    import json

    import pexpect
    import ansible.module_utils.basic
    import ansible.module_utils.action
    import ansible.module_utils._text
    import ansible.module_utils.action

    for path in [os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))]:
        sys.path.insert(0, path)

    class MockModule(ansible.module_utils.basic.AnsibleModule):
        def __init__(self, **kwargs):
            super(MockModule, self).__init__(**kwargs)

# Generated at 2022-06-13 05:26:00.738282
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

    question = "Question"
    responses = ["response1", "response2", "response3", "response4"]

    resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses)

    def wrapped(out):
        try:
            return next(resp_gen)
        except StopIteration:
            module.fail_json

# Generated at 2022-06-13 05:26:27.027345
# Unit test for function main
def test_main():
    args = {}
    args['chdir'] = '/root'
    args['command'] = 'ls -l'
    args['creates'] = '/root/test.txt'
    args['removes'] = '/root/test.txt'
    args['responses'] = {'password?: ': 'test123'}
    args['timeout'] = 30
    args['echo'] = False
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

   

# Generated at 2022-06-13 05:26:37.225686
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(
        argument_spec=dict()
    )
    responses = [
        "the response 1",
        "the response 2",
        "the response 3"
    ]

    question = "The Question"
    response = response_closure(module, question, responses)
    info = {
        'child_result_list': [
            'Question',
            'Question',
            'Question',
            'Question',
            'Question',
            'Question',
            'Question'
        ]
    }

    assert response(info) == b'the response 1\n'
    assert response(info) == b'the response 2\n'
    assert response(info) == b'the response 3\n'

# Generated at 2022-06-13 05:26:37.897492
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:26:40.399789
# Unit test for function main
def test_main():
    global __file__
    __file__ = 'test_main.py'
    main()

# Generated at 2022-06-13 05:26:53.697696
# Unit test for function main
def test_main():
    """ Test module """

    module = AnsibleModule(
        argument_spec={
            "command": {"required": True, "type": "str"},
            "chdir": {"type": "path"},
            "creates": {"type": "path"},
            "removes": {"type": "path"},
            "responses": {"type": "dict", "required": True},
            "timeout": {"type": "int", "default": 30},
            "echo": {"type": "bool", "default": False},
        }
    )

    import pexpect

    args = module.params["command"]
    chdir = module.params["chdir"]
    creates = module.params["creates"]
    removes = module.params["removes"]
    responses = module.params["responses"]
    timeout = module.params["timeout"]
   

# Generated at 2022-06-13 05:27:03.807152
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.pexpect import HAS_PEXPECT
    import pexpect

    if not HAS_PEXPECT:
        # print(traceback.format_exc())
        pass

# Generated at 2022-06-13 05:27:14.006743
# Unit test for function response_closure
def test_response_closure():
    import sys
    import inspect
    import six

    mod = inspect.getmodule(inspect.currentframe())
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    def assert_eq(a, b):
        if a != b:
            print("assertion failed: %s != %s" % (a, b))
            sys.exit(1)

    assert_eq(response_closure(module, "question", ["a", "b"])({"child_result_list" : [""]}), b"a\n")
    assert_eq(response_closure(module, "question", ["a", "b"])({"child_result_list" : [""]}), b"b\n")

# Generated at 2022-06-13 05:27:23.220429
# Unit test for function main
def test_main():

    # Mock data for function main
    expected_result = {
        "cmd": "",
        "stdout": "skipped, since /tmp/file exists",
        "rc": 0,
        "start": "2005-11-02T11:28:35.682774",
        "end": "2005-11-02T11:28:35.682774",
        "delta": "0:00:00.000000",
        "changed": False
    }

    # Perform function call for main
    actual_result = main()

    # Assert
    assert(expected_result == actual_result)

# Generated at 2022-06-13 05:27:31.771089
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

# Generated at 2022-06-13 05:27:34.410254
# Unit test for function main
def test_main():
    import json
    import sys

    # Override the default sys.argv to test with
    sys.argv = [sys.argv[0], '{"command": "echo hello", "responses": {}}']

    result = main()

    # Test the result is what we expected
    assert 'hello' in result['stdout']

# Generated at 2022-06-13 05:28:21.365993
# Unit test for function response_closure
def test_response_closure():
    # Imports should be at the module level, but the import statement
    # depends on the AnsibleModule class, which is not defined until
    # this point. For this function to be testable with py.test, the
    # imports need to be here.
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text

    result = {'foo': 'bar'}
    my_module = AnsibleModule(**result)

    # This is a repeat of the code from the end of main(), but this
    # test is solely for response_closure.
    responses = {
        'question 1': ['answer 1', 'answer 2'],
        'question 2': ['answer 3', 'answer 4'],
    }
    events = dict()

# Generated at 2022-06-13 05:28:23.827034
# Unit test for function main
def test_main():
  res=main()
  if (res['rc'] != 0):
    raise AssertionError("return code zero expected")

# Generated at 2022-06-13 05:28:33.420133
# Unit test for function main
def test_main():
    # Test for failure when pexpect is too old
    test1_args = dict(
        command='echo',
        responses={},
    )
    test1_expect = dict(
        msg='Insufficient version of pexpect installed (%s), this module requires pexpect>=3.3. '
            'Error was object has no attribute \'run\'' % pexpect.__version__,
        rc=1,
    )
    def test1_run(module):
        # Mock pexpect.__version__ to be too old
        pexpect.__version__ = '3.2'
        return main()
    _run_result = _test_module.run_command_to_dict(test1_run, dict(ANSIBLE_MODULE_ARGS=test1_args))
    _test_module.exit_

# Generated at 2022-06-13 05:28:46.730685
# Unit test for function response_closure
def test_response_closure():
    import types
    import pexpect
    module_01 = AnsibleModule(
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
    question_01 = "Question_01"
    responses_01 = ["response1", "response2", "response3"]
    response_01 = response_closure(module_01, question_01, responses_01)

    p = pexpect.spawn("/bin/bash")
    p.expect("$ ")

# Generated at 2022-06-13 05:28:54.972702
# Unit test for function main
def test_main():
    """Unit test for function main"""
    import tempfile
    import textwrap
    import subprocess

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)

        # Create a temporary shell script
        script_path = os.path.join(tmpdir, 'script.sh')
        with open(script_path, 'w') as f:
            f.write(textwrap.dedent(
                """\
                #!/bin/bash
                read -p "Enter your name: " name
                read -p "Enter your age: " age
                echo "Your name is $name and your age is $age."
                """))
        os.chmod(script_path, 0o755)


        # Run the shell script with pexpect
        args = script_path


# Generated at 2022-06-13 05:29:00.873838
# Unit test for function response_closure
def test_response_closure():
    # Some basic testing of response_closure.
    # Not exhaustive.
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
    assert response_closure(module, "key", ["one"])({}) == b"one\n"
    assert response_closure(module, "key", ["one", "two"])({}) == b"one\n"

# Generated at 2022-06-13 05:29:09.662732
# Unit test for function response_closure
def test_response_closure():
    import io
    from ansible.module_utils._text import to_text

    # Test without trailing newline on all strings
    module = AnsibleModule(argument_spec=dict(responses=dict(type='dict', required=True)))
    question = 'Whatever?'
    responses = ['Some', 'Not all', 'Yes']
    gen = response_closure(module, question, responses)
    r1 = gen({})
    assert isinstance(r1, to_text)
    assert r1 == 'Some\n'
    r2 = gen({})
    assert isinstance(r2, to_text)
    assert r2 == 'Not all\n'
    r3 = gen({})
    assert isinstance(r3, to_text)
    assert r3 == 'Yes\n'

# Generated at 2022-06-13 05:29:15.862709
# Unit test for function main
def test_main():
    cmd = 'cat /etc/hosts'


# Generated at 2022-06-13 05:29:24.019376
# Unit test for function main
def test_main():
    import tempfile
    import os
    import re

    # Unit test for function main
    def test_main():
        import tempfile
        import os
        import re

        fd, path = tempfile.mkstemp()
        os.close(fd)
        os.remove(path)

        initial_cwd = os.getcwd()
        tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 05:29:27.859501
# Unit test for function main
def test_main():
    # Test with no event handlers
    response = main(args=["ls"])
    print("\nsucceeded: " + str(response))

# Run the test for doctype parsing
test_main()

# Generated at 2022-06-13 05:30:54.623955
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec = dict(
            command = dict(required = True),
            creates = dict(type = 'path'),
            removes = dict(type = 'path'),
            responses = dict(type = 'dict', required = True),
            timeout = dict(type = 'int', default = 30),
            echo = dict(type = 'bool', default = False)
        )
    )
    # Test case where creates is set, and the file exists, module should not execute command
    cmd = 'command'
    creates = 'creates.txt'
    removes = ''
    responses = {'questions':'response'}
    timeout = 30
    echo = False
    module.params['command'] = cmd
    module.params['creates'] = creates
    module.params['removes'] = removes

# Generated at 2022-06-13 05:31:04.903125
# Unit test for function main
def test_main():
    import pexpect
    import os
    import sys

    class TestModule(AnsibleModule):
        @staticmethod
        def fail_json(msg, *args, **kwargs):
            raise AssertionError(msg)

    def test_run(args, responses=None, timeout=30, echo=False):
        if responses is None:
            responses = dict()
        module = TestModule({
            'command': args,
            'responses': responses,
            'timeout': timeout,
            'echo': echo
        })
        main()

    def test_exception(args, responses=None, timeout=30, echo=False):
        if responses is None:
            responses = dict()

# Generated at 2022-06-13 05:31:15.965825
# Unit test for function response_closure
def test_response_closure():
    class ModuleMock(object):
        def __init__(self):
            self.fail_json = lambda msg: msg

    module = ModuleMock()
    question = 'question'
    responses = [ 'response1', 'response2', 'response3' ]
    wrapped = response_closure(module, question, responses)

    # First call returns the first response
    class ChildResultListMock(object):
        def __init__(self):
            self.append = lambda x: x

    child_result_list = ChildResultListMock()
    info = { 'child_result_list': child_result_list }
    expected = b'response1\n'
    actual = wrapped(info)
    assert(actual == expected)

    # Second call retuns the second response
    expected = b'response2\n'
   

# Generated at 2022-06-13 05:31:27.704257
# Unit test for function main
def test_main():

    # ansible_module_expect_basic_rs
    # DESCRIPTION: Initialize ansible module argument spec and initialize module object as variable m
    # RETURNS: AnsibleModule object m
    def ansible_module_expect_basic_rs():
        import copy
        argument_spec = dict(
            command=dict(required=True),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )

        return AnsibleModule(argument_spec=argument_spec)

    # ansible_module_expect_basic_ex
    # DESCRIPTION: Execute main() function and

# Generated at 2022-06-13 05:31:39.067446
# Unit test for function main
def test_main():
    # Test that main function has no side effects, fails gracefully
    import random
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.text.converters import to_text, to_native
    from ansible.module_utils.common._collections_compat import Mapping
    random.seed(42)

    # Pick some random parameters for the main function

# Generated at 2022-06-13 05:31:49.057141
# Unit test for function response_closure
def test_response_closure():
    import responses

    module = responses.ExpectModule()
    module.params['command'] = 'ping'
    question = 'Question'
    responses = ['response1', 'response2', 'response3']
    module.params['responses'] = {question: responses}
    result = response_closure(module, question, responses)
    assert result.__name__ == 'wrapped'
    assert result.__closure__[0].cell_contents == module
    assert result.__closure__[1].cell_contents == question
    assert result.__closure__[2].cell_contents == responses
    assert result.__closure__[3].cell_contents == (b'response1\n',
                                                   b'response2\n',
                                                   b'response3\n')

# Generated at 2022-06-13 05:31:59.458747
# Unit test for function main
def test_main():
    """ Test module execution
    """
    from ansible.modules.control import expect
    import sys

    # Test function call
    errmsg = "[Errno 2] No such file or directory"
    argv = ["expect", "test_args"]
    sys.argv = argv
    if len(sys.argv) != len(argv):
        raise ValueError("Command line arguments mismatch, sys.argv: '%s' argv: '%s'" % (sys.argv, argv))
    assert expect.main() is None, "Return value of main function is not None: '%s'" % expect.main()
    sys.argv = []
    assert expect.main() is None, "Return value of main function is not None: '%s'" % expect.main()

# Generated at 2022-06-13 05:32:00.340424
# Unit test for function main
def test_main():
    assert main() is None


# Generated at 2022-06-13 05:32:14.282433
# Unit test for function main
def test_main():
    # Test empty command
    module = AnsibleModule({'command': '', 'responses': {r'(?i)password': 'password'}})
    assert main() == module.fail_json(rc=256, msg='no command given')

    # Test invalid version of pexpect
    module = AnsibleModule({'command': 'ls', 'responses': {r'(?i)password': 'password'}})
    pexpect.__version__ = '0.0'
    assert main() == module.fail_json(
        msg='Insufficient version of pexpect installed (0.0), '
            'this module requires pexpect>=3.3. '
        )

    # Test not using pexpect.run (pexpect>=4)

# Generated at 2022-06-13 05:32:19.327341
# Unit test for function main
def test_main():
    (rc, out, err) = module_run('main()', args=dict(command="ls /",
        responses = dict(
            (r'\? ', ' ')
        )))
    assert rc == 0
    assert '__init__.py' in out