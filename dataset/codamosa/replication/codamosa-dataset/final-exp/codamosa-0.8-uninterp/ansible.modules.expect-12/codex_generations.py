

# Generated at 2022-06-13 05:23:44.867082
# Unit test for function response_closure
def test_response_closure():
    from collections import namedtuple
    module = namedtuple('module', ['fail_json'])(lambda x: x)
    responses = ['one', 'two', 'three']
    global_response = response_closure(module, 'Question', responses)
    # Only test on the first call, since the function will change
    # the value of responses on each invocation. The code itself is
    # thoroughly tested in the unit test for expect
    assert global_response({}) == b'one\n'

# Generated at 2022-06-13 05:23:54.664782
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    rc_values = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
    response_closures = []
    for i in rc_values:
        try:
            rc = response_closure(module, "key", i)
            response_closures.append(rc)
        except Exception as e:
            raise AssertionError("response_closure(%s) failed with exception: %s" % (i, get_exception()))

# Generated at 2022-06-13 05:24:00.583309
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(argument_spec={})
    test_question = 'Test Question'
    test_responses = ['Test Response 1', 'Test Response 2']
    test_closure = response_closure(module, test_question, test_responses)

    assert test_closure(dict()) == b'Test Response 1\n'
    assert test_closure(dict()) == b'Test Response 2\n'
    module.fail_json.assert_called_with(msg="No remaining responses for 'Test Question', output was ''")



# Generated at 2022-06-13 05:24:08.266134
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            responses=dict(type='dict', required=True),
        )
    )

    responses = module.params['responses']
    child_result_list = []
    for key, value in responses.items():
        if isinstance(value, list):
            response = response_closure(module, key, value)
        else:
            response = '%s\n' % value
        child_result_list.append(response)
    for item in child_result_list:
        print(item)

# Generated at 2022-06-13 05:24:19.814345
# Unit test for function response_closure
def test_response_closure():
    class TestModule(object):
        def fail_json(self, msg, child_result_list=None):
            pass
    module = TestModule()
    module.fail_json = lambda msg, child_result_list=None: msg
    responses = ['foo', 'bar']
    question = 'Question'
    expect_fmt = "No remaining responses for '%s', output was 'foo'"
    response_func = response_closure(module, question, responses)
    assert response_func({'child_result_list': ['foo']}) == b'foo\n'
    assert response_func({'child_result_list': ['foo']}) == b'bar\n'
    assert response_func({'child_result_list': ['foo']}) == expect_fmt % question

# Generated at 2022-06-13 05:24:26.607792
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

# Generated at 2022-06-13 05:24:27.777004
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import Ansi

# Generated at 2022-06-13 05:24:40.469328
# Unit test for function main
def test_main():
    import mock, tempfile
    from ansible.module_utils.basic import AnsibleModule

    with mock.patch('ansible.module_utils.basic.AnsibleModule', autospec=True) as am:
        with mock.patch('__builtin__.open', mock.mock_open(), create=True) as m:
            main()
        m.assert_any_call('/dev/null', 'wb')
        m.assert_any_call('/dev/null', 'rb')
        m.assert_any_call('/dev/null', 'wb')
        m.assert_any_call('/dev/null', 'rb')
        m.assert_any_call('/dev/null', 'wb')
        m.assert_any_call('/dev/null', 'rb')
        m.assert_any_call

# Generated at 2022-06-13 05:24:50.315699
# Unit test for function main

# Generated at 2022-06-13 05:25:00.100025
# Unit test for function main
def test_main():
    import doctest
    from ansible.module_utils.six import PY3
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
    args = doctest.sys.argv
    pt_version = None
    try:
        import pkg_resources
        pt_version = pkg_resources.get_distribution("pexpect").version
    except ImportError:
        # `pkg_resources` is an optional dep of pexpect, not
        # installed by default.  Pexpect doesn't support python3
        # < 3.4, but the distro may have patched pexpect to drop
        # the pkg_resources dependency.
        pass

# Generated at 2022-06-13 05:25:21.432014
# Unit test for function main
def test_main():
    import os
    import multiprocessing
    import tempfile
    import shutil
    import pexpect
    import sys
    import time
    import errno
    import io

    _pattern_type = type(pexpect.EOF)

    _PY2 = sys.version_info[0] <= 2
    _PY3 = sys.version_info[0] >= 3

    def _read_file(path):
        f = open(path, 'r')
        out = f.read()
        f.close()
        return out

    def _read_bytes_file(path):
        f = open(path, 'rb')
        out = f.read()
        f.close()
        return out

    def _write_file(path, contents):
        f = open(path, 'w')

# Generated at 2022-06-13 05:25:31.376075
# Unit test for function response_closure
def test_response_closure():
    module = object()
    responses = ['foo', 'bar', 'baz']
    func = response_closure(module, 'Test', responses)
    assert func({'child_result_list': []}) == b'foo\n'
    assert func({'child_result_list': []}) == b'bar\n'
    assert func({'child_result_list': []}) == b'baz\n'
    module.fail_json = lambda msg: msg
    try:
        func({'child_result_list': []})
        assert False, "Should have failed"
    except Exception as e:
        assert str(e) == "No remaining responses for 'Test', output was ''"

# Generated at 2022-06-13 05:25:43.959786
# Unit test for function main
def test_main():
    import __builtin__ as builtins
    from ansible.modules.system import expect as mod

    def test_pexpect_run(self, command, timeout=-1, withexitstatus=False,
            events=None, extra_args=None, logfile=None, cwd=None, env=None, _spawn=None):
        return (to_bytes("test"), 123)
    pexpect.run = test_pexpect_run

    def run_command(args, check_rc=True, close_fds=True, executable=None,
            data=None, binary_data=False, path_prefix=None, cwd=None,
            use_unsafe_shell=False, prompt_regex=None):
        return 0, "OK", ""
    setattr(builtins, 'run_command', run_command)

   

# Generated at 2022-06-13 05:25:52.828126
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.basic import AnsibleModule
    import six

    module = AnsibleModule(argument_spec={})

    # Test with non-list for responses
    question = 'question'
    response = 'response'
    responses = [response]
    resp_gen = response_closure(module, question, responses)

    assert six.next(resp_gen) == b'%s\n' % to_bytes(response).rstrip(b'\n')
    assert resp_gen({'child_result_list': ['output']}) == b'%s\n' % to_bytes(response).rstrip(b'\n')
    try:
        resp_gen({'child_result_list': ['output']})
        raise Exception('expected a failure')
    except:
        pass

    # Test with list for responses


# Generated at 2022-06-13 05:26:04.269999
# Unit test for function response_closure
def test_response_closure():
    import tempfile
    from pexpect.spawnbase import SpawnBase

    import ansible.module_utils.basic

    class MockAnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.check_mode = False
            self.no_log = False

        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

    class MockSpawn(SpawnBase):
        def __init__(self, **kwargs):
            self.exitstatus = 0
            self.before = ''
            self.after = ''
            self.match = MockMatch(self)

        def close(self):
            pass

    class MockMatch(object):
        def __init__(self, spawn):
            self.match = ''

# Generated at 2022-06-13 05:26:16.464537
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.six import PY3
    if PY3:
        byteify = lambda x: x
    else:
        byteify = lambda x: x.encode('utf-8')

    class MockModule():
        def __init__(self):
            self.fail_json = lambda **kwargs: None
            self.fail_args = []

        def fail_json(self, *args, **kwargs):
            self.fail_args.append(dict(changed=False, failed=True, msg=args[0]))

    module_obj = MockModule()
    question = 'Question'
    responses = ['response', 'response2']
    response_func = response_closure(module_obj, question, responses)


# Generated at 2022-06-13 05:26:26.490484
# Unit test for function response_closure
def test_response_closure():
    global response_closure
    import unittest
    import pexpect
    import tempfile

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs
        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

    class FakePexpect(object):
        def __init__(self):
            self.proc = tempfile.TemporaryFile()
            self.proc.write(b"hello\n")
            self.proc.write(b"world\n")
            self.proc.seek(0)
            self.echo = False
            self.searcher = pexpect.searcher_re(self)
            self.timeout = 0.25

        def expect(self, pattern):
            self.se

# Generated at 2022-06-13 05:26:37.678006
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

    responses = ['one', 'two', 'three']
    question = 'Question'
    response = response_closure(module, question, responses)

    info = {
        'child_result_list': [
            'one\r\n',
            'Question\r\n',
            'two\r\n'
        ]
    }


# Generated at 2022-06-13 05:26:51.961896
# Unit test for function main
def test_main():
    import io
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    # from local action plugin
    orig_stdout = sys.stdout
    orig_stderr = sys.stderr

    p = module._ansible_tmpdir
    sys.stdout = open(p + '/stdout', 'w')
    sys.stderr = open(p + '/stderr', 'w')

    # create a mock pexpect object
    pexpect_mock = Mock()
    # run function
    main(module,pexpect_mock)
    # restore
    sys.stdout = orig_stdout
    sys.stderr = orig_stderr

# Generated at 2022-06-13 05:26:59.100441
# Unit test for function main
def test_main():
    argv = ['ansible.builtin.expect',
           '--chdir', '',
           '--creates', '',
           '--removes', '',
           '-a', 'command=foo',
           '-a', 'responses={}']
    import sys
    sys.argv = argv
    try:
        main()
        assert False
    except SystemExit as e:
        if e.code == 0:
            assert True
        else:
            assert False

# Generated at 2022-06-13 05:27:27.495068
# Unit test for function response_closure
def test_response_closure():
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = lambda x: None
    module.fail_json = lambda x: None
    question = "question"
    responses = ("response1", "response2")
    wrapped = response_closure(module, question, responses)
    info = {'child_result_list': ["result"]}
    assert wrapped(info) == b"response1\n"
    assert wrapped(info) == b"response2\n"
    try:
        wrapped(info)
        assert False
    except SystemExit:
        pass

# Generated at 2022-06-13 05:27:41.511778
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    class ModuleFailException(Exception):
        pass

    module = AnsibleModule(argument_spec={})

    # Test that a string response is returned for each invocation
    for i in range(1, 10):
        r = response_closure(module, 'Question', ['string response'])
        result = r({})
        assert result == b"string response\n"

    # Test that a list of string responses are returned, one per invocation
    for i in range(1, 10):
        r = response_closure(module, 'Question', ['response1', 'response2'])
        result = r({})
        assert result in [b"response1\n", b"response2\n"]

    # Test that the error condition

# Generated at 2022-06-13 05:27:49.403131
# Unit test for function response_closure
def test_response_closure():
    args = dict(
        command='passwd username',
        responses={
            'password': ['MySekretPa$$word']
        }
    )
    module = AnsibleModule(argument_spec=dict())

    wrapped = response_closure(module, 'password', args['responses']['password'])
    assert wrapped({'child_result_list': ['']}) == b'MySekretPa$$word\n'
    try:
        wrapped({'child_result_list': ['']})
        assert 'expected StopIteration'
    except StopIteration:
        pass

# Generated at 2022-06-13 05:28:01.201685
# Unit test for function main
def test_main():
    with open('/tmp/test_pexpect', 'w') as myfile:
        myfile.write('$ ')
    with open('/tmp/test_pexpect_responses', 'w') as myfile:
        myfile.write('test')

    with open('/tmp/test_pexpect', 'r') as myfile:
        module_args = dict(
            command='echo "test"')
    result = dict(
        cmd='echo "test"',
        stdout='test',
        rc=0,
    )
    check_args = dict(
        checkmode=False,
        diff=False,
        platform='Linux'
    )
    result['changed'] = True

# Generated at 2022-06-13 05:28:06.065490
# Unit test for function response_closure
def test_response_closure():
    import sys
    sys.path.insert(0, '..')
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3
    def fake_fail_json(msg):
        raise Exception(msg)

    module = AnsibleModule(argument_spec=dict())

    responses = ['a', 'b']
    question = 'dummy question'

    # Test sequence of responses
    response = response_closure(module, question, responses)
    assert response(None) == b'a\n'
    assert response(None) == b'b\n'

    # Test missing responses
    if not PY3:
        # Python 2.7 with pytest-xdist fails to catch the StopIteration
        with pytest.raises(Exception):
            response(None)
   

# Generated at 2022-06-13 05:28:16.157014
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils import basic
    import types
    # build a fake module
    module = basic.AnsibleModule(argument_spec={})
    # test a list of responses
    responses = ['A', 'B', 'C']
    func = response_closure(module, 'Q', responses)
    # the func should be a function
    assert isinstance(func, types.FunctionType)
    # the first call to func should return the first item from responses
    assert func({}) == 'A\n'
    # the second call to func should return the second item from responses
    assert func({}) == 'B\n'
    # the third call to func should return the third item from responses
    assert func({}) == 'C\n'
    # after the third call, there should be no more responses, so calling
    # func should raise

# Generated at 2022-06-13 05:28:25.538802
# Unit test for function main
def test_main():
    import sys
    import __builtin__
    from io import StringIO
    
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils._text import to_native
    from ansible.module_utils.basic import AnsibleModule

    class ExitJson(Exception):
        pass

    class FailJson(Exception):
        pass

    def exit_json(*args, **kwargs):
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise ExitJson(kwargs)

    def fail_json(*args, **kwargs):
        kwargs['failed'] = True
        raise FailJson(kwargs)

    def get_module_path(*args, **kwargs):
        return 'ansible.builtin.expect'



# Generated at 2022-06-13 05:28:34.152989
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.six.moves import StringIO
    class Module(object):
        def fail_json(self, msg, **kwargs):
            raise ValueError(msg, kwargs)

        def exit_json(self, rc=0, **kwargs):
            raise ValueError(rc, kwargs)

    class ChildResult(object):
        pass

        def __init__(self, out, exitstatus):
            self.exitstatus = exitstatus
            self.stdout = out
            self.stderr = b''

    module = Module()
    question = 'test question'
    responses = ['test 1', 'test 2', 'test 3']
    expected_result = [b'test 1\n', b'test 2\n', b'test 3\n']

# Generated at 2022-06-13 05:28:44.730209
# Unit test for function response_closure
def test_response_closure():
    class Module(object):
        def __init__(self):
            self.fail_json = lambda *args,**kwargs: None
    module = Module()

    question = 'Test?'
    responses = [ 'Test' ]
    gen = response_closure(module, question, responses)
    result = gen({'child_result_list':[]})
    assert result == b'Test\n'
    try:
        gen({'child_result_list':[]})
    except Exception as e:
        assert e.args[0] == "No remaining responses for 'Test?', output was ''"
        pass
    else:
        assert 'Should have failed'

# Generated at 2022-06-13 05:28:52.255984
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

    responses = ['Yes', 'No']
    question = 'Are you sure?'
    resp = response_closure(module, question, responses)

    expected = [b'Yes\n', b'No\n']
    actual = []
    for i in range(2):
        actual.append(resp({'child_result_list': [b'']}))


# Generated at 2022-06-13 05:29:52.829392
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes, to_text

    # pexpect.run is introduced in 4.0, our function backports it
    try:
        import pexpect
        pexpect_run = getattr(pexpect, 'run')
    except ImportError:
        pexpect_run = None
    pexpect_run_saved = pexpect.run


# Generated at 2022-06-13 05:29:57.202957
# Unit test for function main
def test_main():
    import contextlib2
    import pexpect

    with contextlib2.ExitStack() as stack:
        mock_module = stack.enter_context(MockAnsibleModule())
        stack.enter_context(MockPexpect(pexpect.spawn, 'spawn'))
        stack.enter_context(MockPexpect(pexpect._run, '_run'))
        stack.enter_context(MockPexpect(pexpect.run, 'run'))
        stack.enter_context(MockPexpect(pexpect.runu, 'runu'))

        # Testing run/runu

# Generated at 2022-06-13 05:30:09.413759
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
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
    module.exit_json = lambda x: x
    args = module.params['command']
    responses = module.params['responses']
    module.params['responses'] = responses
    response = responses['password']

# Generated at 2022-06-13 05:30:21.103390
# Unit test for function response_closure
def test_response_closure():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from ansible.module_utils.six import PY3

    ansible_version_tuple = tuple(map(int, ansible_version.split('.')))

    if not PY3 and ansible_version_tuple >= (2, 4):
        import __builtin__ as builtins
    else:
        import builtins

    class AnsibleModuleFake(object):
        def __init__(self):
            self.params = {'command': '', 'responses': {}}

        def fail_json(*args, **kwargs):
            raise AnsibleFailJson

    class AnsibleFailJson(Exception):
        pass

    def fake_builtin_open(self, filename, mode=None, encoding=None):
        return

# Generated at 2022-06-13 05:30:31.127866
# Unit test for function main
def test_main():
    import time
    import unittest
    import ansible.module_utils.action_plugins.expect as expect

    class Tests(unittest.TestCase):

        def test_main_exception(self):
            from ansible.module_utils.basic import AnsibleModule
            from ansible.module_utils._text import to_bytes
            # We did not implement this function for our unit test
            # but will be implemented in future
            pass

        def test_response_closure(self):
            from ansible.module_utils.basic import AnsibleModule
            from ansible.module_utils._text import to_bytes
            import ansible.module_utils.action_plugins.expect as expect
            module = AnsibleModule(
            )
            question = "hello"
            responses = ["hi", "hello"]
            self.assertE

# Generated at 2022-06-13 05:30:44.129258
# Unit test for function response_closure
def test_response_closure():
    import unittest
    mock = unittest.mock.MagicMock()
    mock.fail_json.side_effect = RuntimeError
    list_of_strings = [b'string1', b'string2', b'string3']
    responses = response_closure(mock, 'Question', list_of_strings)
    assert responses(dict()) == b'string1\n'
    assert responses(dict()) == b'string2\n'
    assert responses(dict()) == b'string3\n'
    mock.fail_json.assert_called_once_with(msg="No remaining responses for 'Question', output was 'b''")
    # Test that state of generated responses is not changed by use
    # of the function
    assert responses(dict()) == b'string1\n'

# Generated at 2022-06-13 05:30:53.118034
# Unit test for function response_closure
def test_response_closure():
    global module
    module = AnsibleModule(argument_spec={})
    assert response_closure(module, 'question', ['response1', 'response2'])('x') == b'response1\n'
    assert response_closure(module, 'question', ['response1', 'response2'])('x') == b'response2\n'

    try:
        response_closure(module, 'question', ['response1', 'response2'])('x')
        assert False, 'should have thrown an exception'
    except SystemExit:
        pass

# Generated at 2022-06-13 05:30:58.927965
# Unit test for function main
def test_main():
    args = dict(
        command='echo',
        chdir=None,
        creates=None,
        removes=None,
        responses=dict(
            hello='hello',
        ),
        timeout=30,
        echo=False,
    )

    with patch.object(AnsibleModule, 'run_command') as run_mock:
        main()
        main(args)

# Generated at 2022-06-13 05:30:59.939058
# Unit test for function main
def test_main():
    # Write unit test here
    pass

# Generated at 2022-06-13 05:31:00.435274
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:33:18.438647
# Unit test for function response_closure
def test_response_closure():
    import sys
    import io

    class fake_module():
        def fail_json(self, msg, **kwargs):
            sys.stderr.write(msg)
            sys.exit(1)

    class fake_pexpect():
        class ExceptionPexpect(Exception):
            pass

    fake_module_obj = fake_module()
    fake_pexpect_obj = fake_pexpect()

    # Valid case
    ques="Q1"
    responses=["A1", "A2"]
    gen_exp = response_closure(fake_module_obj, ques, responses)

    for i in range(0, len(responses)):
        result = gen_exp({})
        expected = "%s\n" % responses[i]

# Generated at 2022-06-13 05:33:24.611438
# Unit test for function main
def test_main():

    import sys
    import os
    import tempfile
    import random
    random.seed(0)

    test_dir = os.path.join(tempfile.gettempdir(), 'ansible_test_dir_%d' % random.randint(10000, 99999))
    test_file1 = os.path.join(test_dir, 'file1')
    test_file2 = os.path.join(test_dir, 'file2')

    os.makedirs(test_dir)
    open(test_file1, 'w+').close()
    open(test_file2, 'w+').close()

    main_dir = os.path.dirname(__file__) # should be /path/to/ansible/lib/ansible/modules/files
    sys.path.insert(0, main_dir)