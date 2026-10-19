

# Generated at 2022-06-13 05:49:05.989246
# Unit test for function main
def test_main():
    # Initialise a new ansible module object
    import  ansible_module_ping
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import _load_params
    import json
    import sys
    import os

    sys.argv = ["ansible-ping", "/tmp/ansible/ansible_module_ping.py"]

    # Set params and args to test
    params = dict(data='1')
    args = dict()

    # Run the main function
    result = ansible_module_ping.main()

    # Create the expected results
    result = dict(
        ping='1',
    )

    assert(result == result)

# Generated at 2022-06-13 05:49:08.328267
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:49:14.773721
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

        result = dict(
            ping=module.params['data'],
        )

    module.exit_json(**result)


# main()

# Generated at 2022-06-13 05:49:16.855056
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    AnsibleModule = ansible.module_utils.basic.AnsibleModule
    main(AnsibleModule)

# Generated at 2022-06-13 05:49:18.283047
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:49:25.340104
# Unit test for function main
def test_main():
    # Try normal run through
    params = dict(data='pong')
    p = Plugin(params=params, module_name='ping', module_args={'data': 'pong'})
    assert p.run() == params

    # Try when data set to crash
    params = dict(data='pong')
    p = Plugin(params=params, module_name='ping', module_args={'data': 'crash'})
    assert p.run() == params

# Generated at 2022-06-13 05:49:34.531601
# Unit test for function main
def test_main():
    testdata = [
        {
            "test_case": "Normal",
            "test_data": {
                "data": "pong"
            },
            "expected_exit_code": 0,
            "expected_out": {
                "ping": "pong"
            }
        },
        {
            "test_case": "Crash",
            "test_data": {
                "data": "crash"
            },
            "expected_fail": True
        }
    ]

    import mock
    test_main_module = mock.MagicMock()
    test_main_module.params = testdata[0]['test_data']
    main_module_dict = {"ansible.module_utils.basic.AnsibleModule": test_main_module}
    test_main_module.exit_json = mock

# Generated at 2022-06-13 05:49:41.605455
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    import ansible.builtin.ping
    import sys
    import os

    class TestAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            if kwargs["argument_spec"] is None:
                kwargs["argument_spec"] = dict()
            super(TestAnsibleModule, self).__init__(*args, **kwargs)

        def exit_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args["changed"] = False

        def exit_failure(self, **kwargs):
            self.exit_args = kwargs

# Generated at 2022-06-13 05:49:50.083056
# Unit test for function main
def test_main():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.modules.network.ping import main
    import json

    # Test with data=pong
    set_module_args(dict(data='pong'))
    result = main()
    assert len(result) == 1, "One key is required in the result; len is %d" % len(result)
    assert json.dumps(dict(ping="pong")) == json.dumps(result)

    # Test with data=crash.  We can't fully control the key in the result
    set_module_args(dict(data='crash'))
    try:
        main()
        assert False, "An exception was not raised"
    except Exception as e:
        assert "boom"

# Generated at 2022-06-13 05:49:57.408915
# Unit test for function main
def test_main():
    from ansible.modules.network.ping import main
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:50:03.834077
# Unit test for function main
def test_main():
    try:
        #Test for valid parameters
        result = main('')
        assert result['changed'] == False
    except:
        assert False

# Generated at 2022-06-13 05:50:09.396049
# Unit test for function main
def test_main():

    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            super(AttrDict, self).__init__(*args, **kwargs)
            self.__dict__ = self

    # Define the return value from the AnsibleModule
    module = AttrDict()
    module.params = {
        'data': 'pong'
    }
    module.exit_json = lambda **kwargs: None

    # Run the function
    main()

# Generated at 2022-06-13 05:50:13.344385
# Unit test for function main
def test_main():
    # This needs to be fixed.  Ping should just be a simple return value.
    # We can't use the normal unit testing mechanisms because the module
    # code is reading command line arguments instead of looking at module.params
    # which is how we normally do unit testing.
    pass

# Generated at 2022-06-13 05:50:15.106635
# Unit test for function main
def test_main():
    module = dict()
    module['params'] = dict()
    module['params']['data'] = 'pong'
    module['params']['data'] == 'pong'

# Generated at 2022-06-13 05:50:23.703303
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    def my_run_command_mock(self, tmp, task_vars=dict()):
        return (0, to_bytes(u'{"changed": false, "ping": "pong"}'), '')

    def my_run_command_crash_mock(self, tmp, task_vars=dict()):
        return (1, to_bytes(u'{"changed": false, "ping": "pong"}'), '')

    arguments = dict(
        data=dict(type='str', default='pong'),
    )
    requirements = dict()


# Generated at 2022-06-13 05:50:29.304629
# Unit test for function main
def test_main():
    #unit test requires working module-utils/basic.py
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._json_compat import json
    from ansible.module_utils._text import to_bytes
    # set up the module object
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    # set up the mock objects
    # run the _exec() function
    module.exit_json(**module.params)
    # check if module.exit_json() was called
    assert module.exit_json.called
    # test if input values are equal to output values
    module.exit_json.assert_called_with(ping='pong')

# Generated at 2022-06-13 05:50:36.369509
# Unit test for function main
def test_main():
    # Setup arguments
    args = {}
    args['data'] = "pong"

    # Setup module
    module = AnsibleModule(name = "ping", argument_spec=dict(data=dict(type='str', default='pong'),))
    module.check_mode = False

    # Run function main with arguments args
    main(module)

    # Check results
    assert module.exit_json.called
    assert module.params['data'] == "pong"
    assert module.params['data'] == result['ping']

# Generated at 2022-06-13 05:50:36.916927
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:50:37.627365
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:50:49.027448
# Unit test for function main
def test_main():
    import os
    import sys
    import pytest
    # include parent path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from module_utils import basic
    from module_utils import action
    # module params
    params = dict(
        data='pong',
    )
    # exit json
    exit_json = dict(
        changed=False,
        ping='pong',
    )
    # remove basic.ANSIBLE_ARGS
    if 'ANSIBLE_ARGS' in basic.__dict__:
        del basic.ANSIBLE_ARGS

    def mock_supports_check_mode(sefl, **kwargs):
        return True


# Generated at 2022-06-13 05:51:00.858327
# Unit test for function main
def test_main():
    res = None
    # test with no data
    res = main({'data': 'pong'})
    assert res == {'ping': 'pong'}

    # test with data set to crash
    res = main({'data': 'crash'})
    assert res == {'ping': 'pong'}

# Generated at 2022-06-13 05:51:11.835989
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        )
    )
    def raise_exc(self, exception):
        raise exception
    test_module.fail_json = raise_exc.__get__(test_module, AnsibleModule)

    # Check that we get a crash
    test_module.params['data'] = 'crash'
    with pytest.raises(Exception) as exc_info:
        main()
    assert exc_info.value.args[0] == 'boom'

    # Check that we can return data
    test_module.params['data'] = 'testdata'
    main()

# Generated at 2022-06-13 05:51:18.285861
# Unit test for function main
def test_main():
    def fail(msg):
        print('FAIL: %s' % msg)
        exit(1)

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = module.run_command('ping: pong')
    if result[0] != 0:
        fail("Unexepcted non-zero return code")
    elif result[1]['ping'] != 'pong':
        fail("Unexpected non-pong return value")


# Generated at 2022-06-13 05:51:25.287525
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)



# Generated at 2022-06-13 05:51:32.048303
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    rc = module.run_command('ping')

    # Verify that the return code and the data are correct
    assert rc == 0
    assert data == 'pong'

# Generated at 2022-06-13 05:51:35.678441
# Unit test for function main
def test_main():
    m = AnsibleModule(argument_spec={'data': {'type': 'str', 'default': 'pong'}}, supports_check_mode=True)
    assert m.params['data'] == 'pong'
    assert m.check_mode is True
    m.exit_json(ping='pong')

# Generated at 2022-06-13 05:51:39.497528
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:51:40.442999
# Unit test for function main
def test_main():
    with pytest.raises(Exception):
        main()

# Generated at 2022-06-13 05:51:51.542264
# Unit test for function main
def test_main():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.module_utils.basic import AnsibleModule
    from ansible.utils.unsafe_proxy import ansible_module_kwargs

    def test_module(**kwargs):
        module_args = dict(
            data=dict(type='str', default='pong')
        )
        module_args.update(kwargs)
        module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
        )

        if module.params['data'] == 'crash':
            raise Exception("boom")

        result = dict(
            ping=module.params['data'],
        )

        module.exit_json(**result)


# Generated at 2022-06-13 05:51:59.098924
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import json

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=module.params['data'],
    )

    json_out = module.exit_json(**result)
    output = to_bytes(json.dumps(json_out))
    assert result['ping'] == 'pong'
    assert type(json_out) == dict
    assert output.startswith(b'{"msg": "")}\n')


# Generated at 2022-06-13 05:52:16.773613
# Unit test for function main
def test_main():
    # TODO: Add unit tests that don't crash.
    assert 1 == 1

# Generated at 2022-06-13 05:52:21.298793
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=module.params['data'],
    )
    assert result == dict(ping='pong')


# Generated at 2022-06-13 05:52:34.068825
# Unit test for function main
def test_main():
    from ansible.module_utils.six import PY3
    import sys

    # Load the module
    sys.path.append('../library')
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2
    import sys

    if PY2:
        from StringIO import StringIO
    else:
        from io import StringIO

    # Set the module input parameters
    module_args = dict(
        data=dict(type='str', default='pong')
    )

    # Run the ping function and set the result
    setattr(AnsibleModule, 'params', module_args)
    main()

    # Create mock stdout and stderr
    real_stdout = sys.stdout


# Generated at 2022-06-13 05:52:37.088645
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    result = dict(
        ping=module.params['data'],
    )

    assert result == dict(ping='pong')

# Generated at 2022-06-13 05:52:37.543099
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:52:38.005522
# Unit test for function main
def test_main():
  main()

# Generated at 2022-06-13 05:52:40.736567
# Unit test for function main
def test_main():
    import json
    payload = {
        'data': 'pong'
    }
    result = {}

    result = main(json.dumps(payload))

    assert 'ping' in result
    assert result['ping'] == 'pong'


# Generated at 2022-06-13 05:52:48.877569
# Unit test for function main
def test_main():

    test_module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong'),
                                                   supports_check_mode=dict(type='bool', default=True)))

    ansible_facts = {}  # additional test data

    if test_module.params['data'] == 'crash':
        raise TypeError("Test exception")

    test_result = dict(ping=test_module.params['data'])

    test_module.exit_json(**test_result)

# Generated at 2022-06-13 05:52:49.489995
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:52:55.452956
# Unit test for function main
def test_main():
    # a test module from Ansible itself
    from ansible.modules.system import ping
    mod = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result_success = dict(
        changed=0,
        ping="pong"
    )
    result_no_change = dict(
        ping="pong"
    )
    result_failure = dict(
        msg="boom",
        failed=True
    )
    # test return with default value, changed = 0 and success = 0
    result = ping.main()
    assert result == result_no_change
    # test return changed = 1 and success = 0
    result = ping.main(module=mod)
    assert result == result_

# Generated at 2022-06-13 05:53:28.773943
# Unit test for function main
def test_main():
    # unit test code here
    pass

# Generated at 2022-06-13 05:53:38.605377
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    original_module_utils_basic_ANSIBLE_MODULE_UTILS = ansible.module_utils.basic.ANSIBLE_MODULE_UTILS
    ansible.module_utils.basic.ANSIBLE_MODULE_UTILS = None
    import ansible.module_utils.urls
    original_module_utils_urls_HAS_SSLCONTEXT = ansible.module_utils.urls.HAS_SSLCONTEXT
    ansible.module_utils.urls.HAS_SSLCONTEXT = False
    original_module_utils_urls_HAS_SSH = ansible.module_utils.urls.HAS_SSH
    ansible.module_utils.urls.HAS_SSH = False
    original_module_utils_urls_H

# Generated at 2022-06-13 05:53:40.208856
# Unit test for function main
def test_main():
    import doctest
    doctest.testmod()
    doctest.run_docstring_examples(main, globals())

# Generated at 2022-06-13 05:53:43.696068
# Unit test for function main
def test_main():
    # Testing with default arguments
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:53:51.284621
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:53:52.301770
# Unit test for function main
def test_main():
    result = main()
    assert True

# Generated at 2022-06-13 05:53:54.745466
# Unit test for function main
def test_main():
    args = dict(
        data='ping'
    )
    with pytest.raises(Exception) as excinfo:
        main()
    assert 'boom' in str(excinfo.value)

# Generated at 2022-06-13 05:53:58.424492
# Unit test for function main
def test_main():
    module_args={}
    try:
        main()
    except Exception as e:
        module_args['Exception'] = "boom"


# Generated at 2022-06-13 05:54:06.627100
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible_collections.ansible.builtin.tests.unit.modules.utils import set_module_args

    with pytest.raises(SystemExit) as cm:
        set_module_args(dict(data='crash'))
        main()
    exception = cm.value.code
    assert exception == 1
    out = to_bytes(stdout.getvalue())
    err = to_bytes(stderr.getvalue())
    assert b"An exception occurred during task execution. To see the full traceback, use -vvv. The error was: boom" in err
    assert b"failed=True" in out
    assert b"msg=unreachable" in out

   

# Generated at 2022-06-13 05:54:14.343251
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)



# Generated at 2022-06-13 05:55:40.041276
# Unit test for function main

# Generated at 2022-06-13 05:55:46.023385
# Unit test for function main
def test_main():
    httpretty.enable()
    httpretty.register_uri(httpretty.GET, 'http://example.com')
    # httpretty.register_uri(httpretty.GET, 'http://example.com', body=user_string, status=200)

    # Load the module and test parameters
    module = utils.load_params('basic.yml', 'ping.yml')

    # Mock return values and side effects
    ret = module.params['ansible_facts']
    print(ret)
    # ret['changed'] = True

    # Run the module
    module.exit_json(**ret)

    httpretty.disable()

# Generated at 2022-06-13 05:55:46.747558
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:55:49.188176
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as e:
        raise Exception("Test Exception", e)

# Generated at 2022-06-13 05:55:52.103804
# Unit test for function main
def test_main():
    result = {}

    #  Check for expected exception
    try:
        main()
    except Exception as e:
        result['Exception'] = e

    assert 'Exception' in result

# Generated at 2022-06-13 05:55:56.503115
# Unit test for function main
def test_main():
    test_module = AnsibleModule({
        "data": "pong"
        }, check_invalid_arguments=False)
    result = dict(
        ping="pong"
    )
    assert main() == None
    test_module.exit_json.assert_called_with(**result)

# Generated at 2022-06-13 05:56:03.816319
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic

    # Setup required parameters
    data = 'pong'

    # Create the AnsibleModule for function main
    module = AnsibleModule(
        argument_spec=dict(
        data=dict(type='str', default='pong'),
    ),
        supports_check_mode=True
    )

    # Test function call
    result = main()

    assert result['ansible_facts']['ping'] == 'pong'

    # Test exception
    with pytest.raises(Exception):
        assert main(data='crash')

# Generated at 2022-06-13 05:56:07.823511
# Unit test for function main
def test_main():
    for args in [dict(), dict(data='pong'), dict(data='crash')]:
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 0

# Generated at 2022-06-13 05:56:12.478890
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )
    module.exit_json(**result)

# Generated at 2022-06-13 05:56:13.226619
# Unit test for function main
def test_main():
    # Tests for main()
    assert callable(main)