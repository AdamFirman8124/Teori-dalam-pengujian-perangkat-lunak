

# Generated at 2022-06-13 05:23:47.938077
# Unit test for function response_closure
def test_response_closure():
    import tempfile
    import os
    import shutil

    tempdir = tempfile.mkdtemp()
    testfile = os.path.join(tempdir, 'test_file')
    temp_module = AnsibleModule(argument_spec={})
    test_responses = ['response 1', 'response 2', 'response 3']
    test_question = "Question"
    test_closure = response_closure(temp_module, test_question, test_responses)

    # First call to test_closure should return the first response test_responses
    answer = test_closure({'child_result_list': None})
    assert answer == b'response 1\n'

    # Second call to test_closure should return the second response test_responses
    answer = test_closure({'child_result_list': None})
    assert answer == b

# Generated at 2022-06-13 05:23:56.585736
# Unit test for function response_closure
def test_response_closure():
    tests = {
        # list of responses
        'foo': ['bar', 'baz', 'quix'],
        # single string response
        'quux': 'quix',
        # unicode list
        u'quũx': [u'quix', u'quũx', u'quöx'],
        # unicode string
        u'quöx': u'quix',
    }

    # make a test module
    class TestModule:
        def fail_json(self, msg, **kwargs):
            raise RuntimeError(msg, kwargs)

    # run test set

# Generated at 2022-06-13 05:24:08.478111
# Unit test for function main
def test_main():
    # Create an instance of our mock class
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

    module.params['command'] = 'ls -al'
    module.params['responses'] = {'Question':'Response'}

    startd = datetime.datetime.now()

    endd = datetime.datetime.now()
    delta = endd - startd


# Generated at 2022-06-13 05:24:11.399838
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit as e:
        if not e.code == 0:
            raise

# Generated at 2022-06-13 05:24:21.772572
# Unit test for function main
def test_main():
    # Import here, since the above code has not yet run and can modify the
    # path of the module
    import sys
    import subprocess
    import time
    import os
    import tempfile
    import shutil

    # Create a temp dir that we can use for this test
    tmp_dir = tempfile.mkdtemp()

    # Create a temp file that we can use for this test
    tmp_file = tempfile.NamedTemporaryFile(dir=tmp_dir)

    # Make sure the tmp_file is writable
    old_umask = os.umask(0o022)

    # Give it some content
    tmp_file.write(b'Hello\n')

    # Close the tmp_file so we can reopen it with the expect module
    tmp_file.close()

    # Reopen the file so that we can read

# Generated at 2022-06-13 05:24:32.726914
# Unit test for function response_closure
def test_response_closure():
    m = AnsibleModule(argument_spec=dict(
        command=dict(required=True),
        responses=dict(type='dict', required=True),
        timeout=dict(type='int', default=30),
        echo=dict(type='bool', default=False),
    ))
    resp = ['foo', 'bar', 'baz', 'qux']
    resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in resp)
    next(resp_gen)
    next(resp_gen)
    next(resp_gen)
    next(resp_gen)
    try:
        next(resp_gen)
        assert False
    except StopIteration:
        pass

    wrapped = response_closure(m, 'Question', resp)

    child_result_

# Generated at 2022-06-13 05:24:38.825339
# Unit test for function main
def test_main():
  class FakeModule:
    def __init__(self):
      self.params = dict()
      self.params['command'] = 'ls -latr /'
      self.params['chdir'] = None
      self.params['creates'] = None
      self.params['removes'] = None
      self.params['responses'] = None
      self.params['timeout'] = None
      self.params['echo'] = True
  module = FakeModule()
  main()


# Generated at 2022-06-13 05:24:48.770036
# Unit test for function response_closure
def test_response_closure():
    def test_module(**kwargs):
        class TestModule():
            def fail_json(self, msg, **kwargs):
                raise AnsibleModuleFail(msg)

        return TestModule()

    module = test_module()
    question = 'Test Question'
    responses = ['response1', 'response2']

    resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses)
    wrapped = response_closure(module, question, responses)

    try:
        next_resp = wrapped({'child_result_list': []})
    except AnsibleModuleFail:
        next_resp = None

    assert next_resp == next(resp_gen)


# Generated at 2022-06-13 05:24:59.255201
# Unit test for function response_closure
def test_response_closure():
    import pexpect
    import json
    import re
    import textwrap
    import sys
    import signal

    # Catch SIGPIPE in pexpect.py, so
    # we can test the handling of a broken pipe
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    # set up a function to catch stdout/stderr
    # to check what happens when we fake a pipe break
    def catch_output():
        class OutputGrabber(object):
            def __init__(self, fp, old_stdout):
                # fp should be sys.stdout or sys.stderr
                self._fp = fp
                self._copy = old_stdout
                self._data = ''
                self._created = False
                self._override = None


# Generated at 2022-06-13 05:25:05.889732
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

    question = 'Question'
    responses = [ 'response1', 'response2' ]
    response = response_closure(module, question, responses)
    assert(response({'child_result_list': ['child_result_message']}) == b'response1\n')
    assert(response({'child_result_list': ['child_result_message']}) == b'response2\n')

# Generated at 2022-06-13 05:25:35.504995
# Unit test for function response_closure
def test_response_closure():
    import sys
    import argparse
    import doctest
    import textwrap
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Test module', epilog=textwrap.dedent(r'''
        Example:

$ python -c 'from ansible.module_utils.basic import AnsibleModule; m = AnsibleModule(); m.params = dict(respo=[1, 2]); m.fail_json(msg="TEST");'
fatal: [localhost]: FAILED! => {
    "msg": "TEST"
}
'''))

# Generated at 2022-06-13 05:25:47.209992
# Unit test for function main
def test_main():
    class AnsibleModuleMock(object):
        def __init__(self, argspec, module_params=dict()):
            self.params = module_params
            self.argspec = argspec
            self.fail_json = lambda **kwargs: None
            self.exit_json = lambda **kwargs: None

    class DocfragmentMock(object):
        version_added = None

    # create a class mock for pexpect
    class PexpectMock(object):
        def __init__(self, command, timeout=30, logfile=None, **kwargs):
            self.command = command
            self.timeout = timeout
            self.logfile = logfile
            self.prompt_return = False  # set to true to return from the prompt call

# Generated at 2022-06-13 05:26:01.131633
# Unit test for function response_closure
def test_response_closure():
    ''' response_closure creates a closure that cycles through lists of responses.

    We'll just test that the closure works to ensure that successive calls
    produce successive list items. We're not testing the error condition/message,
    since that will be tested in the pexpect module itself.
    '''
    resp1 = ['foo', 'bar']
    resp2 = ['baz', 'qux']
    resp_all = {'resp1': resp1, 'resp2': resp2}
    module = AnsibleModule({}, check_invalid_arguments=False)
    for key, value in resp_all.items():
        resp_gen = response_closure(module, key, value)
        resp1_1 = resp_gen(dict())
        resp1_2 = resp_gen(dict())
        assert resp1_1 == 'foo\n'

# Generated at 2022-06-13 05:26:13.606721
# Unit test for function response_closure
def test_response_closure():
    import pexpect
    import sys

    class FakeModule(object):
        def __init__(self):
            self.changed = False
            self.args = dict(
                command = 'test_command',
                responses = dict(
                    Question = ['A', 'B']
                ),
                timeout = 20
            )

        def fail_json(self, **kwargs):
            print(kwargs)
            sys.exit(1)

    fm = FakeModule()
    args = fm.args
    chdir = None
    creates = None
    removes = None
    timeout = args['timeout']
    echo = False

    def echo_function(resp):
        print(resp)

    events = dict()
    for key, value in args['responses'].items():
        if isinstance(value, list):
            response

# Generated at 2022-06-13 05:26:22.143231
# Unit test for function response_closure
def test_response_closure():
    # Test normal behavior
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
        )
    )
    question = "test question"
    responses = [ "response1", "response2", "response3" ]
    test_closure = response_closure(module, question, responses)
    result = test_closure( { 'child_result_list': [ 'some output' ] } )
    expected = [b"response1\n", b"response2\n", b"response3\n"]
    # print(expected)
    # print(result)
    assert expected == result

    # Test empty list
    question = "test question"
    responses = [ ]
   

# Generated at 2022-06-13 05:26:35.094937
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    # Mock module for testing
    class MockModule(object):
        def fail_json(self, msg, **kwargs):
            raise AssertionError("MockModule fail_json called. msg: %s, kwargs: %s" % (msg, kwargs))
    module = MockModule()
    # Set of tests to run
    responses = [
        (["a"], ["a"], ["b"], ["a", "a", "b"]),
        (["a"], ["a"], ["b", "c"], ["a", "b", "c"]),
        (["a"], ["a", "a"], ["b"], ["a", "a", "b"])
    ]
    # Run tests

# Generated at 2022-06-13 05:26:41.789820
# Unit test for function response_closure
def test_response_closure():
    import types

    class FakeModule(object):
        def __init__(self):
            self.fail_json_called = False

        def fail_json(self, *args, **kwargs):
            self.fail_json_called = True

    module = FakeModule()

    question = 'Question1'
    responses = ['response1', 'response2', 'response3']
    response = response_closure(module, question, responses)
    assert isinstance(response, types.FunctionType)

    # First call has to return first response
    info = {}
    assert response(info) == b'response1\n'

    # Second call has to return second response
    assert response(info) == b'response2\n'

    # Third call has to return third response
    assert response(info) == b'response3\n'

# Generated at 2022-06-13 05:26:47.304900
# Unit test for function main
def test_main():
    err = {'msg': 'file does not exist', 'rc': 1, 'stderr': '', 'stdout': 'skipped, since /path/to/does/not/exist does not exist'}
    assert main(args=['/path/to/does/not/exist', 'removes=/path/to/does/not/exist']) == err


# Generated at 2022-06-13 05:26:56.242282
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
    question = "Hello World"
    responses = ['Hello World']
    info = dict(
        child_result_list = ['Hello World'],
    )
    response = response_closure(module, question, responses)
    result = response(info)
    assert result is not None


# Generated at 2022-06-13 05:27:05.403725
# Unit test for function main
def test_main():
    module_args = dict(
        args="echo hello world",
        responses={
            "hello": "goodbye",
        }
    )
    tmp_test_result = dict()
    tmp_test_result['cmd'] = 'echo hello world'
    tmp_test_result['stdout'] = 'goodbye'
    tmp_test_result['rc'] = 0
    tmp_test_result['start'] = str(datetime.datetime.now())
    tmp_test_result['end'] = str(datetime.datetime.now())
    tmp_test_result['changed'] = True
    tmp_test_result['delta'] = '0:00:00.000000'

    def test_exit_json(obj):
        assert obj['cmd']==tmp_test_result['cmd']

# Generated at 2022-06-13 05:27:34.039248
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.six import StringIO
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
        stdout_lines=StringIO()
    )
    question = 'foo'
    responses = ['bar\n', 'baz\n']
    first_response = response_closure(module, question, responses)
    second_response = response_closure(module, question, responses)
    assert first_response({}) == b'bar\n'
   

# Generated at 2022-06-13 05:27:45.345343
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

    # test for list argument
    responses = ['foo','bar','baz','qux']
    response = response_closure(module, 'question', responses)
    assert response({'child_result_list':['0','1','2','3','4']})=='foo\n'

# Generated at 2022-06-13 05:27:59.293172
# Unit test for function main
def test_main():
    # test for master branch
    expected_intermediate_result = {
        'changed': True,
        'cmd': 'passwd username',
        'end': str(datetime.datetime.now()),
        'rc': 0,
        'start': str(datetime.datetime.now()),
        'stdout': '',
        'delta': str(datetime.datetime.now()-datetime.datetime.now())
    }
    intermediate_result = main()
    assert intermediate_result['changed'] == expected_intermediate_result['changed']
    assert intermediate_result['cmd'] == expected_intermediate_result['cmd']
    assert intermediate_result['stdout'] == expected_intermediate_result['stdout']
    assert intermediate_result['rc'] == expected_intermediate_result['rc']
    assert intermediate_

# Generated at 2022-06-13 05:28:09.237685
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(argument_spec={})

    # Test with a single element list
    responses = response_closure(module, 'question', ['response'])
    assert responses({'child_result_list': []}) == b'response\n'
    assert responses({'child_result_list': []}) == b'response\n'

    # Test with a multi element list
    responses = response_closure(module, 'question', ['response1', 'response2'])
    assert responses({'child_result_list': []}) == b'response1\n'
    assert responses({'child_result_list': []}) == b'response2\n'
    assert responses({'child_result_list': []}) == b'response2\n'

    # Test with a multi element list with too few responses

# Generated at 2022-06-13 05:28:14.830855
# Unit test for function main
def test_main():
    m = AnsibleModule(argument_spec=dict(
        command=dict(required=True),
        chdir=dict(type='path'),
        creates=dict(type='path'),
        removes=dict(type='path'),
        responses=dict(type='dict', required=True),
        timeout=dict(type='int', default=30),
        echo=dict(type='bool', default=False),
    ))
    main()

# Generated at 2022-06-13 05:28:23.842834
# Unit test for function response_closure
def test_response_closure():
    responses = ['yes', 'no', 'maybe']
    resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses)
    resp = response_closure(None, None, responses)
    assert resp(None) == next(resp_gen)
    assert resp(None) == next(resp_gen)
    assert resp(None) == next(resp_gen)

    # Test exception raising
    class TestException(Exception):
        pass
    class TestModule(object):
        def fail_json(self, msg, **kwargs):
            raise TestException(msg)
    module = TestModule()
    error_msg = "No remaining responses for 'pattern', output was 'result'"

# Generated at 2022-06-13 05:28:33.454713
# Unit test for function main

# Generated at 2022-06-13 05:28:46.730736
# Unit test for function main
def test_main():
    output = {
        'msg': 'non-zero return code',
        'cmd': "passwd username",
        'rc': 1,
        'start': '2016-05-01 14:33:04.320632',
        'stdout': 'stderr',
        'end': '2016-05-01 14:33:34.320634',
        'changed': True,
        'delta': '0:00:30',
    }
    responses = {
        "Are you sure you want to continue connecting (yes/no)?" : "yes",
        "password": "MySekretPa$$word",
        "Press RETURN to get started.": "",
    }
    expect_cmd = "passwd username"

# Generated at 2022-06-13 05:28:49.935939
# Unit test for function main
def test_main():
    # Unit test imports
    import shutil
    import tempfile

    # Unit test setup
    tempdir = tempfile.mkdtemp()

    try:
        # Unit test code
        main()
    finally:
        # Unit test teardown
        shutil.rmtree(tempdir)

# Generated at 2022-06-13 05:28:57.830003
# Unit test for function main
def test_main():
    import __main__ as main
    # Mock class for key-value pairs
    class ArgumentSpec():
        def __init__(self):
            self.command = 'print(#test)'
            self.chdir = None
            self.creates = None
            self.removes = None
            self.responses = {}
            self.timeout = None
            self.echo = False

    # Mock class for AnsibleModule, because if it gets imported directly
    # it tries to parse command-line arguments.
    class AnsibleModule():
        def __init__(self):
            self.argument_spec = ArgumentSpec()

        def fail_json(self, **kwargs):
            return kwargs

        def exit_json(self, **kwargs):
            return kwargs

    res = main.main()

# Generated at 2022-06-13 05:29:43.859114
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:29:44.635065
# Unit test for function response_closure
def test_response_closure():
  assert 1 == 1

# Generated at 2022-06-13 05:29:51.808444
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(argument_spec={})
    responses = ['one', 'two', 'three']
    question = 'test'
    rc = response_closure(module, question, responses)
    assert rc('one') == 'one\n'
    assert rc('two') == 'two\n'
    assert rc('three') == 'three\n'
    assert_raises(AnsibleExitJson, rc, ('three'))

# Generated at 2022-06-13 05:29:59.067442
# Unit test for function main
def test_main():
    # Verify that fail_json is called in the case of no command being passed
    from ansible.module_utils.basic import AnsibleModule as _am
    am = _am(argument_spec={'command': dict(required=True)})

    b_out, rc = main(am, '', '', '', '', '', 30, '')
    assert 'no command given' in b_out
    assert rc == 256

    # Verify that fail_json is called when an insufficient version of
    # pexpect is installed
    class FakeVersion(object):
        def __init__(self, version):
            self.version = version

    pexpect = FakeVersion('3.1')
    b_out, rc = main(am, 'echo foo', None, '', '', '', 30, '')

# Generated at 2022-06-13 05:30:05.233823
# Unit test for function main
def test_main():
    args = [
        'ansible-playbook',
        './test_playbook.yml'
    ]
    rc = {'rc': 0}
    sys.exit(test_ansible_playbook(args, rc))

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:30:12.725294
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule, missing_required_lib
    from ansible.module_utils._text import to_bytes, to_native, to_text

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


# Generated at 2022-06-13 05:30:22.970564
# Unit test for function main

# Generated at 2022-06-13 05:30:25.870377
# Unit test for function response_closure
def test_response_closure():
    args = [1, 2, 3]
    def test_function(info):
        assert info == args
    f = response_closure(test_function, args)
    f()

# Generated at 2022-06-13 05:30:34.728712
# Unit test for function main
def test_main():
  # Define args.
  args = dict(
    command='/usr/bin/whoami',
    response={
      r'my-hostname login: ': 'my-username',
      r'Password: ': 'my-password',
      r'Password expired. Change it now? \(y/n\) ': 'n',
      r'$ ': 'whoami',
      r'my-username': 'exit'
    },
    timeout=10)

  # Define module.
  module = AnsibleModule(args)

  # Run main().
  main()

# Generated at 2022-06-13 05:30:45.630912
# Unit test for function response_closure
def test_response_closure():
    import copy
    import random

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

    # Generate a random length list of 10-60 responses
    test_responses = [to_text(random.randint(0, 9)) for i in range(random.randint(10, 60))]
    # Randomly modify a few of the responses to ensure they are being transformed properly

# Generated at 2022-06-13 05:32:40.928220
# Unit test for function main
def test_main():
    cmd_1 = "/usr/bin/sleep 1"
    cmd_2 = "/usr/bin/sleep 1"
    cmd_3 = "ansible_host"
    output_1 = main(cmd_1,2)
    output_2 = main(cmd_2,3)
    assert output_1 == output_2



# Generated at 2022-06-13 05:32:47.876839
# Unit test for function response_closure
def test_response_closure():
    import mock
    import ansible.module_utils.ansible_free_form

    module, command, responses=mock.Mock(spec_set=ansible.module_utils.ansible_free_form.AnsibleModule), "command", {"Question": ["resp1", "resp2", "resp3"]}
    resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses["Question"])
    expected_outputs = [next(resp_gen)]
    recieved_outputs = []
    # Perform first call
    wrapped = response_closure(module, "Question", ["resp1", "resp2", "resp3"])
    recieved_outputs.append(wrapped({'child_result_list' : ["output"]}))
    expected_outputs

# Generated at 2022-06-13 05:32:52.493547
# Unit test for function response_closure
def test_response_closure():
    import mock
    run_command = mock.Mock(return_value=('', 0))
    module = mock.Mock(
        fail_json=mock.Mock(side_effect=SystemExit(1)),
        run_command=run_command
    )
    responses = ['1', '2', '3']
    response_closure(
        module,
        "Question",
        responses
    )()

    # Call it twice to verify we get the second response
    # - 'ansible.builtin.expect' is only used from one file: 'action/network.py'
    # which does not use the 'list' functionality
    # - Python 2 does not have the 'nonlocal' keyword
    #   so we can't access the generator directly from 'response_closure'
    # - For now, just call it twice to make sure

# Generated at 2022-06-13 05:33:01.242097
# Unit test for function response_closure
def test_response_closure():
    import re
    import unittest2

    class _MockModule(object):
        def fail_json(self, msg):
            raise msg

    responses = ['Hello', 'World']
    question = '(?i)enter'
    info = dict(child_result_list=[b'first', b'second'])

    # Successive calls to the closure should return successive values
    closure = response_closure(_MockModule(), question, responses)
    assert closure(info) == b'Hello\n'
    assert closure(info) == b'World\n'

    # If the closure runs out of responses, it should raise an error
    try:
        closure(info)
        assert False
    except RuntimeError as e:
        assert re.match(r'No remaining responses for .*', str(e))



# Generated at 2022-06-13 05:33:13.673893
# Unit test for function response_closure
def test_response_closure():
    class AnsibleModuleMock(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

    module = AnsibleModuleMock(
        command='echo hello',
        responses={
            'hello': [
                'goodbye', 'goodnight', 'see you next time'
            ]
        }
    )

    # Test with call count of 2.
    # Should return 'goodnight'
    resp_gen = response_closure(module, 'hello', ['goodbye', 'goodnight', 'see you next time'])

    try:
        assert resp_gen({"child_result_list":["hello", "hello"]}) == to_bytes('goodnight\n')
    except StopIteration:
        pass

# Generated at 2022-06-13 05:33:14.423102
# Unit test for function main
def test_main():
    # TODO: write unit test
    assert False

# Generated at 2022-06-13 05:33:22.181260
# Unit test for function main
def test_main():
  import pexpect
  class MockModule:
    params = {}
    def fail_json(self,msg, **result):
      raise AssertionError(msg)
    def exit_json(self, **result):
      pass
  class MockPexpectSpawn:
    def __init__(self, cmd, timeout):
      self.cmd = cmd
      self.timeout = timeout
    def expect(self, *args, **kwargs):
      self.expect_args = args
      self.expect_kwargs = kwargs
      return 0
    def sendline(self, line):
      pass
  class MockPexpect:
    def __init__(self, *args, **kwargs):
      self.args = args
      self.kwargs = kwargs