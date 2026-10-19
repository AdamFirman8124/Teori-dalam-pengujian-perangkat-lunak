

# Generated at 2022-06-13 05:23:49.755091
# Unit test for function main
def test_main():
    # Test acceptable version of pexpect
    try:
        import pexpect
        pexpect.test = "Testing pexpect version"
        del pexpect.test
        del pexpect
    except (AttributeError, ImportError):
        return
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True, type='str'),
            chdir=dict(type='path'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            responses=dict(type='dict', required=True),
            timeout=dict(type='int', default=30),
            echo=dict(type='bool', default=False),
        )
    )
    if module.check_mode:
        return
    main()


# Generated at 2022-06-13 05:23:56.830316
# Unit test for function response_closure
def test_response_closure():
    class FakeModule(object):

        def __init__(self):
            self.fail_json_called = False

        def fail_json(self, msg):
            self.fail_json_called = True

    fake_module = FakeModule()

    responses = ['response1', 'response2', 'response3']

    response = response_closure(fake_module, 'question', responses)

    assert response({}) == to_bytes('response1\n')
    assert response({}) == to_bytes('response2\n')
    assert response({}) == to_bytes('response3\n')
    assert response({}) == to_bytes('response1\n')
    assert not fake_module.fail_json_called

# Generated at 2022-06-13 05:24:04.513317
# Unit test for function response_closure
def test_response_closure():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.connection import Connection
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    p = PlayContext()
    p.prompt = ('password')
    dl = DataLoader()
    vm = VariableManager()

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

    response_match

# Generated at 2022-06-13 05:24:13.309889
# Unit test for function response_closure
def test_response_closure():
    import pytest
    from pexpect.expect import TIMEOUT
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    start_time = datetime.datetime.now()
    rc = 0
    response_list = ['response1', 'response2']
    cmd_output = b'test1\ntest2'
    test_generator = response_closure(AnsibleModule(argument_spec={}), 'test_question', response_list)

# Generated at 2022-06-13 05:24:21.353942
# Unit test for function response_closure
def test_response_closure():
    import mock

    module = mock.Mock()
    question = 'Question'
    responses = ['response1', 'response2', 'response3']
    resp_gen = [b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses]

    response = response_closure(module, question, responses)

    assert response({}) == resp_gen[0]
    assert response({}) == resp_gen[1]
    assert response({}) == resp_gen[2]
    module.fail_json.assert_called_with(
        msg="No remaining responses for 'Question', output was ''")

# Generated at 2022-06-13 05:24:32.498931
# Unit test for function main
def test_main():
    args = dict(
        command='echo hello',
        chdir=None,
        creates=None,
        removes=None,
        responses={},
        timeout=30,
        echo=False,
    )
    expected = dict(
        ansible_facts=dict(),
        changed=True,
        cmd=args['command'],
        delta='0:00:00.000015',
        end='2016-08-20 18:42:19.975763',
        rc=0,
        start='2016-08-20 18:42:19.975748',
        stdout='hello'
    )

    with patch.object(pexpect, 'run') as mock_run:
        mock_run.return_value = ("hello", 0)


# Generated at 2022-06-13 05:24:38.287223
# Unit test for function main
def test_main():
    test_main.__test__ = False
    import mock
    import tempfile
    from ansible.module_utils.basic import AnsibleModule, missing_required_lib
    from ansible.module_utils._text import to_bytes, to_native, to_text

    def response_closure(module, question, responses):
        resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses)

        def wrapped(info):
            try:
                return next(resp_gen)
            except StopIteration:
                module.fail_json(msg="No remaining responses for '%s', "
                                     "output was '%s'" %
                                     (question,
                                      info['child_result_list'][-1]))

        return wrapped


# Generated at 2022-06-13 05:24:45.719842
# Unit test for function response_closure
def test_response_closure():
    m = AnsibleModule(argument_spec={})
    func = response_closure(m, "Question", ["response1", "response2", "response3"])
    resp_1 = func({})
    resp_2 = func({})
    resp_3 = func({})
    m.fail_json.assert_called_with(msg="No remaining responses for 'Question', output was ''")
    assert resp_1 == b'response1\n'
    assert resp_2 == b'response2\n'
    assert resp_3 == b'response3\n'

# Generated at 2022-06-13 05:24:53.997617
# Unit test for function response_closure
def test_response_closure():
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

    first_resp = 'First Response'
    second_resp = 'Second Response'
    responses = [first_resp, second_resp]

    question = 'Question'
    response = response_closure(m, question, responses)

    # First call
    output = response({'child_result_list' : ['Out1']})
    assert output == first_resp + '\n'

    # Second

# Generated at 2022-06-13 05:25:01.898348
# Unit test for function main
def test_main():
    # If the module is invoked with `--check`, then we don't do anything.
    # The module is not idempotent in that case, we will always report
    # `changed` (will execute the command).
    module = AnsibleModule(argument_spec={'_ansible_check_mode': {'type': 'bool', 'default': False}})
    if module.params['_ansible_check_mode']:
        module.exit_json(changed=True, msg='Ansible check mode')

    # If the module is invoked with `--diff`, then we don't do anything.
    # The module has no way of knowing the difference between the command
    # execution and the original state.
    module = AnsibleModule(argument_spec={'_ansible_diff': {'type': 'bool', 'default': False}})

# Generated at 2022-06-13 05:25:25.805407
# Unit test for function main
def test_main():
    """
    Test function main
    :return:
    """
    """
    Test function response_closure
    :return:
    """



# Generated at 2022-06-13 05:25:35.288674
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
        )
    )

    args = module.params['command']
    responses = module.params['responses']

    # Capture module failure and output
    fake_stdin = StringIO()
    module.fail_json = lambda *args, **kwargs: fake_stdin.write(str(kwargs))

# Generated at 2022-06-13 05:25:47.061730
# Unit test for function response_closure
def test_response_closure():
    import copy
    import inspect
    import pickle

    def test_module(*args, **kwargs):
        def fail_json(msg, **kwargs_):
            assert False, msg

        mod = type('CustomModule', (object,), {'fail_json': fail_json})()
        mod.params = kwargs

        return mod
    module = test_module(**{
        'command': 'command',
        'responses': {'a': ['1', '2', '3']},
        'timeout': 0,
        'echo': False,
    })

    question = 'a'
    responses = ['1', '2', '3']
    wrapped = response_closure(module, question, responses)

# Generated at 2022-06-13 05:26:01.023181
# Unit test for function main
def test_main():
    print("Test execution")
    args = {
        'command': 'ls -l',
        'chdir': '/tmp',
        'creates': None,
        'removes': None,
        'responses': {'Q1': 'Test'},
        'timeout': 30,
        'echo': True,
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
    if not HAS_PEXPECT:
        module.fail_

# Generated at 2022-06-13 05:26:13.606895
# Unit test for function main
def test_main():
    import tempfile
    import shutil

    dirpath = tempfile.mkdtemp()
    path = os.path.join(dirpath, 'test.txt')
    with open(path, 'w') as f:
        f.write('test')


# Generated at 2022-06-13 05:26:18.237523
# Unit test for function main
def test_main():
    arguments = {'removes': '/path/to/removes', 'command': '/path/to/command', 'creates': '/path/to/creates', 'responses': {'key': 'value'}, 'chdir': '/path/to/chdir'}
    set_module_args(arguments)

    my_expect_mock = MagicMock(return_value=('stdout', 0))
    with patch.dict(expect.__dict__, {'expect': my_expect_mock}):
        main()

    expected_args = [
        '/path/to/command',
        '/path/to/chdir'
    ]
    my_expect_mock.assert_called_once_with(*expected_args, **arguments)

# Generated at 2022-06-13 05:26:26.792003
# Unit test for function main
def test_main():
    # test if arguments are parsed properly
    correct_args = {"chdir": "/",
                    "command": "cat",
                    "creates": "/etc/passwd"}
    test_args = ['-a',
                 'chdir=/',
                 'command=cat',
                 'creates=/etc/passwd']
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

# Generated at 2022-06-13 05:26:33.547328
# Unit test for function main
def test_main():
    test_result = {
        "changed": True,
        "cmd": "echo Hello",
        "delta": "0:00:00.002000",
        "end": "2019-04-01 19:57:54.988000",
        "rc": 0,
        "start": "2019-04-01 19:57:54.986000",
        "stdout": "Hello",
    }

    test_args = {
        "changed": True,
        "cmd": "echo Hello",
        "delta": "0:00:00.002000",
        "end": "2019-04-01 19:57:54.988000",
        "rc": 0,
        "start": "2019-04-01 19:57:54.986000",
        "stdout": "Hello",
    }

   

# Generated at 2022-06-13 05:26:34.669898
# Unit test for function main
def test_main():
    # This will complete because we don't run the command
    assert main() == None

# Generated at 2022-06-13 05:26:41.500422
# Unit test for function response_closure
def test_response_closure():
    import pexpect
    module = type('', (), {})()

    question = 'What is your name?'
    responses = ['siva', 'koki', 'vijay']

    wrapped = response_closure(module, question, responses)

    def test(index):
        g = pexpect.spawn('echo What is your name?')
        wrapped(dict(g=g, child_result_list=[], child_result_str=''))
        child_result_str = g.readline()
        child = chr(g.readbyte())
        g.close()
        assert child_result_str == responses[index] + '\n'
        assert child == '\n'

    test(0)
    test(1)
    test(2)
    test(0)
    test(1)

# Generated at 2022-06-13 05:27:30.449016
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

    # Test simple case: return a single response string
    responses = ['simple string']
    response = response_closure(module, 'simple string', responses)
    assert response({}) == b'simple string\n'

    # Test simple case: return a single response string with \n removed
    responses = ['simple string\n']

# Generated at 2022-06-13 05:27:43.332777
# Unit test for function response_closure
def test_response_closure():
    import sys
    import unittest
    from unittest.mock import patch

    from ansible.module_utils.basic import AnsibleModule

    class TestResponseClosure(unittest.TestCase):
        # Note: If a question is encountered multiple times, its string response
        # will be repeated. If you need different responses for successive
        # question matches, instead of a string response, use a list of strings
        # as the response. The list functionality is new in 2.1.

        def setUp(self):
            self.module = AnsibleModule(
                argument_spec=dict(
                    responses=dict(type='dict', required=True),
                )
            )


# Generated at 2022-06-13 05:27:57.659910
# Unit test for function response_closure
def test_response_closure():
    global module
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

    res = response_closure(module, 'blah', ['foo', 'bar', 'baz'])
    assert res({'child_result_list': ['1', '2', '3']}) == b'foo\n'
    assert res({'child_result_list': ['1', '2', '3']}) == b'bar\n'

# Generated at 2022-06-13 05:28:06.301676
# Unit test for function main
def test_main():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule

    tmpdir = tempfile.gettempdir()

    def make_command_file(name, contents):
        path = os.path.join(tmpdir, name)
        with open(path, 'w') as outfile:
            outfile.write(contents)
        return path

    # Test a simple echo command
    command_file = make_command_file('command_file', 'echo "I am a test"')
    test_module = AnsibleModule({
        'command': command_file,
        'responses': {'I am a test': ''},
    }, check_invalid_arguments=False)
    response = main()
    assert not response.get('failed')

    # Test a simple echo command that runs for a

# Generated at 2022-06-13 05:28:17.023506
# Unit test for function response_closure
def test_response_closure():
    import types
    module = type("a", (object,), {"fail_json": lambda self, a: None})()

    def test_iter():
        for n in [1, 2, 3]:
            yield n

    test_iter_static = (n for n in [1, 2, 3])

    assert isinstance(response_closure(module, "key", "value"), types.FunctionType)
    assert isinstance(response_closure(module, "key", ["a", "b", "c"]), types.FunctionType)
    assert isinstance(response_closure(module, "key", test_iter), types.FunctionType)
    assert isinstance(response_closure(module, "key", test_iter_static), types.FunctionType)

# Generated at 2022-06-13 05:28:24.927252
# Unit test for function main
def test_main():
    args = dict(
        command="echo Hello World"
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

    rc, out, err = module.run_command(args['command'])
    result = dict(
        cmd=args['command'],
        stdout=out
    )
    assert rc == 0
    assert result['cmd'] == 'echo Hello World'
    assert result['stdout'] == 'Hello World\n'

# Generated at 2022-06-13 05:28:30.142460
# Unit test for function main
def test_main():
    command = 'echo Hello World'
    chdir = '/tmp'
    creates = ''
    removes = ''
    responses = {'Hello World': "Hello World"}
    timeout = '30'
    echo = 'False'

    os.chdir(chdir)
    startd = datetime.datetime.now()
    b_out, rc = pexpect.run(command, timeout=timeout, withexitstatus=True,
                            events=responses, cwd=chdir, echo=echo,
                            encoding=None)
    endd = datetime.datetime.now()
    delta = endd - startd

# Generated at 2022-06-13 05:28:30.694450
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:28:34.152990
# Unit test for function main
def test_main():
    import os
    import sys
    sys.path.append(os.path.dirname(__file__))
    import test
    import shutil
    test.get_unit_test('expect')
    main()
    shutil.rmtree(test.UNIT_TEST_PATH+'expect')

# Generated at 2022-06-13 05:28:37.951638
# Unit test for function main
def test_main():
    '''
    Return:
    '''
    print("Start testing")
    args = [
    ]
    res = main(args)
    print("Finish testing")
    return res

# Generated at 2022-06-13 05:29:44.444178
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
            _ansible_check_mode=dict(default=False, type='bool'),
            _ansible_verbosity=dict(default=0, type='int'),
            _ansible_debug=dict(default=False, type='bool'),
            _ansible_diff=dict(default=True, type='bool'),
            _ansible_syslog_facility=dict(type='str'),
        )
    )

   

# Generated at 2022-06-13 05:29:51.253347
# Unit test for function response_closure
def test_response_closure():
  import ansible.module_utils.basic
  from ansible.module_utils._text import to_native, to_text
  from ansible.module_utils.basic import AnsibleModule

  args = [ 1, 2, 3, 4, 5 ]
  responses = [ 7, 8, 9 ]

  test_module = AnsibleModule(
    argument_spec=dict(
      responses=dict(
        type='list',
      )
    )
  )
  test_module.params['responses'] = responses

  num_iterations = -1
  ite_closure = response_closure( test_module, 'testing', responses )
  while True:
    num_iterations += 1
    try:
      result = ite_closure( { 'child_result_list': args } )
    except:
      break

# Generated at 2022-06-13 05:29:57.853331
# Unit test for function main
def test_main():
    _test_args = {
        'command': 'echo test',
        'responses': {
            'test': 'response'
        },
        'echo': False,
    }

    m = AnsibleModule(**_test_args)

    with patch.dict(os.environ, {'LANG': 'C'}):
        with patch('ansible.module_utils.basic.AnsibleModule') as mock:
            mock.return_value = m

# Generated at 2022-06-13 05:30:09.804642
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils._text import to_bytes, to_native

    def wrapped_fn(info):
        return info['child_result_list'][-1]

    module = dict(
        params=dict(
            responses={'test response': ['test response', 'test response2']},
            command='test'
        ),
        fail_json=lambda msg: msg
    )

    response = response_closure(module, 'test response', ['test response','test response2'])

    assert response(dict(child_result_list=[to_bytes('test response')])) == to_bytes('test response2\n')


# Generated at 2022-06-13 05:30:13.101062
# Unit test for function main
def test_main():
    args = "ansible.builtin.expect -a"
    assert main() != 1
    args = "-version-added:"
    assert main() != 1


# Generated at 2022-06-13 05:30:23.237961
# Unit test for function response_closure
def test_response_closure():
    class _Module(object):
        def __init__(self):
            self.fail_json_called = False

        def fail_json(self, *args, **kwargs):
            self.fail_json_called = True

    def _test(mod, question, responses, out_resp, fail_json=False):
        resp_func = response_closure(mod, question, responses)

        responses = [x.rstrip(b'\n') for x in responses]
        # test that the response function returns the responses in sequence
        for i, resp in enumerate(responses):
            assert(resp_func(dict(child_result_list=[])) == responses[i])
        # test that one more call fails
        resp = resp_func(dict(child_result_list=[]))
        assert(resp == out_resp)


# Generated at 2022-06-13 05:30:32.002679
# Unit test for function main
def test_main():
    import random
    import string
    import sys
    import time
    import unittest

    if sys.version_info[0] < 3:
        import mock
    else:
        from unittest import mock

    class TestMain(unittest.TestCase):

        def setUp(self):
            self.module = mock.Mock()

        def tearDown(self):
            pass

        def test_main_pexpect_needed(self):
            with mock.patch('ansible.module_utils.basic.AnsibleModule') as basic:
                basic.side_effect = Exception('AnsibleModule Exception')
                sys.modules['pexpect'] = None

                self.assertRaisesRegex(
                    Exception,
                    'AnsibleModule Exception',
                    main
                )


# Generated at 2022-06-13 05:30:43.444927
# Unit test for function main
def test_main():
    assert to_bytes(main()) == """{
    "changed": true, 
    "cmd": "ls", 
    "delta": "0:00:00.253985", 
    "end": "2015-05-21 22:58:03.396566", 
    "rc": 0, 
    "start": "2015-05-21 22:58:03.142581", 
    "stdout": "execute.py  execute_tests.py  __init__.py  libraries  module_utils  module_utils.basic  module_utils.common  module_utils.network  module_utils.shell  module_utils.urls  modules  plugins  test  tests"
}"""


# Generated at 2022-06-13 05:30:53.150099
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(argument_spec={})

    question = 'foo'

    responses = ['bar', 'baz']

    call_responses = []

    def fake_response_func(info):
        call_responses.append(info)

    response_closure(module, question, responses)({'child_result_list': [42]})

    fake_response_func({'child_result_list': [42]})

    assert call_responses == [{'child_result_list': [42]}]

# Generated at 2022-06-13 05:31:03.358630
# Unit test for function main
def test_main():
    import sys,os,tempfile
    fd, path = tempfile.mkstemp(suffix='.py')
    old_path = sys.path[0]
    sys.path[0] = os.path.dirname(path)

# Generated at 2022-06-13 05:33:21.112522
# Unit test for function main
def test_main():
    #print("In test for function main")

    set_module_args(dict(
        command='date',
        responses=dict(
            YEAR=lambda x: x['event_count'],
            MONTH=lambda x: x['event_count'],
            DAY=lambda x: x['event_count'],
        )
    ))

    import datetime

    res = main()
    now = datetime.datetime.now()

# Generated at 2022-06-13 05:33:21.802398
# Unit test for function main
def test_main():
    command = 'main'
    main()

# Generated at 2022-06-13 05:33:26.370838
# Unit test for function main
def test_main():
    rc, err, out = module.run_command('ansible testhost -m expect -a "command=/bin/false"')
    assert rc==1
    rc, err, out = module.run_command('ansible testhost -m expect -a "command=/bin/echo foo"')
    assert rc==0