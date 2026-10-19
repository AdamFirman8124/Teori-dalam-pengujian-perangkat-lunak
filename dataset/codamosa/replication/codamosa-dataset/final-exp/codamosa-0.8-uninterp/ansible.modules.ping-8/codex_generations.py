

# Generated at 2022-06-13 05:49:00.339394
# Unit test for function main
def test_main():
    print('Testing module:', __file__)
    from ansible.modules.network.ping import *
    from ansible.module_utils.network.ping import *
    import pytest

# Generated at 2022-06-13 05:49:04.071036
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

# Generated at 2022-06-13 05:49:06.700344
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:49:07.175529
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:49:14.721969
# Unit test for function main
def test_main():
    """
    Test function main()
    """

    # Generate AnsibleModule object
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Result should be true
    assert main()

    # Test except of main()
    try:
        main()
    except Exception as e:
        assert str(e) == 'boom'

    # Test extra variables
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:49:15.306170
# Unit test for function main
def test_main():
  assert main() != None

# Generated at 2022-06-13 05:49:18.708844
# Unit test for function main
def test_main():
  ansible_module_ping = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
  assert ansible_module_ping


# Generated at 2022-06-13 05:49:20.493156
# Unit test for function main
def test_main():
    data = None
    assert main(data) == {'ping': 'pong'}

# Generated at 2022-06-13 05:49:21.159533
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:49:25.461080
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    set_module_args(data='crash')
    result = dict(ping='crash')
    main()

# Generated at 2022-06-13 05:49:36.243389
# Unit test for function main
def test_main():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    builtins.__dict__['__salt__'] = {}
    builtins.__dict__['__opts__'] = {}
    m = AnsibleModule(
        argument_spec={
            "data": {"type": "str", "default": "pong"}
        },
        supports_check_mode=True
    )
    return_value = main()
    assert return_value['changed'] == False
    assert return_value['ping'] == "pong"

# Generated at 2022-06-13 05:49:38.702769
# Unit test for function main
def test_main():
    # Dict input for function main and expected result.
    input_main = {'data': 'crash'}

    result_main = Exception("boom")

    # Calling main function and asserting expected result.
    assert main(input_main) == result_main

# Generated at 2022-06-13 05:49:48.666717
# Unit test for function main
def test_main():
    import json

    # Test check_mode and diff mode
    module = AnsibleModule(argument_spec={'data': {'type': 'str', 'default': 'pong'}},
                           supports_check_mode=True,
                           )
    result = module.exit_json(**dict(ping='test_main'))
    assert json.loads(result['_ansible_diff'])['after']['ping'] == 'test_main'
    assert result['_ansible_check_mode']

    # Test normal mode
    with open('/tmp/ansible_ping_payload', 'w') as payload:
        payload.write('{"ANSIBLE_MODULE_ARGS": {"data": "pong"}}')


# Generated at 2022-06-13 05:49:52.439428
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

# Generated at 2022-06-13 05:50:01.051742
# Unit test for function main
def test_main():
    # 
    # ping:
    #     description: Value provided with the data parameter.
    #     returned: success
    #     type: str
    #     sample: pong
    #   # Test we can logon to 'webservers' and execute python with json lib.
    #   # ansible webservers -m ping
    
    #   - name: Example from an Ansible Playbook
    #     ansible.builtin.ping:
    
    #   - name: Induce an exception to see what happens
    #     ansible.builtin.ping:
    #       data: crash
    # module = get_module_instance('ansible.builtin.ping')

    import ansible.builtin.ping
    data = {'data':'pong'}
    result = ansible.builtin.ping.main

# Generated at 2022-06-13 05:50:10.049322
# Unit test for function main
def test_main():
    f = open('/tmp/test_ansible_lib_ping', 'w')
    g = open('/tmp/test_ansible_lib_ping_stdout', 'w')
    h = open('/tmp/test_ansible_lib_ping_stderr', 'w')

    save_stdout = sys.stdout
    save_stderr = sys.stderr
    sys.stdout = g
    sys.stderr = h


# Generated at 2022-06-13 05:50:14.034760
# Unit test for function main
def test_main():
     args = dict(
             data="hello world")
     result = dict(
             ping="hello world")
     module = AnsibleModule(argument_spec=args)
     main()
     assert module.exit_json.call_args[0][0] == result

# Generated at 2022-06-13 05:50:16.559116
# Unit test for function main
def test_main():
    with pytest.raises(Exception) as excinfo:
        main()
    assert "boom" in str(excinfo.value)

# Generated at 2022-06-13 05:50:21.816785
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong')
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    assert result == {
        'ping': 'pong'
    }

# Generated at 2022-06-13 05:50:23.898949
# Unit test for function main
def test_main():
    # In this test, just make sure we don't crash.
    #
    # This is kind of a lame unit test but it's better than nothing.
    main()

# Generated at 2022-06-13 05:50:36.753133
# Unit test for function main
def test_main():
    args = dict(
        data='pong'
    )
    test_module = AnsibleModule(argument_spec=args)

    def mock_exit_json(self, **kwargs):
        self.exit_args = kwargs

    test_module.exit_json = mock_exit_json
    main()
    res_args = test_module.exit_args
    assert res_args['ping'] == 'pong'


# Generated at 2022-06-13 05:50:37.450031
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:50:40.980570
# Unit test for function main
def test_main():
    test_input = {"data": "ping", "check_mode": True} #input
    test_result = {"ping": "ping"} #output
    assert main(test_input) == test_result

# Generated at 2022-06-13 05:50:50.042632
# Unit test for function main
def test_main():
    testargs = ["ping", "data=blah"]
    with patch.object(sys, 'argv', testargs):
        with patch('ansible.module_utils.basic.AnsibleModule') as ansible_module_mock:
            ansible_module_mock.return_value.params['data'].return_value = 'blah'
            with pytest.raises(SystemExit):
                main()
            ansible_module_mock.return_value.fail_json.assert_called_once_with(msg='invalid data specified')

    testargs = ["ping", "data=crash"]
    with patch.object(sys, 'argv', testargs):
        with patch('ansible.module_utils.basic.AnsibleModule') as ansible_module_mock:
            ansible_module_m

# Generated at 2022-06-13 05:50:50.635039
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:51:01.370148
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert module.params == dict(
        data='pong',
    )
    # The _ansible_*_interpreter are deprecated, but we set them here so that test_utils.unit
    # can detect that this module works with Python 2 & 3.
    module._ansible_no_log_values['_ansible_python_interpreter'] = "/path/to/python"

# Generated at 2022-06-13 05:51:05.380579
# Unit test for function main
def test_main():
    a = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')),
                      supports_check_mode=True)
    main(a)

# Generated at 2022-06-13 05:51:10.335513
# Unit test for function main
def test_main():
    # Construct a dummy “module”.
    module = type('', (), dict(params={
        'data': 'whatever',
        'diff': False,
        'check_mode': False,
        },
        exit_json=lambda x: None,
        fail_json=lambda x: None,
        check_mode=lambda: False))

    # Call main() with the dummy module.
    main()
    main.argument_spec = {}

    # Check that calling main() with a crash parameter raises an exception.
    module.params['data'] = 'crash'
    with pytest.raises(Exception):
        main()

# Generated at 2022-06-13 05:51:14.840821
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec = dict(
            data = dict(type = 'str', default = 'pong'),
        ),
        supports_check_mode = True
    )
    module.exit_json(ping = module.params['data'])

from ansible.module_utils.basic import *
main()

# Generated at 2022-06-13 05:51:24.314402
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import Mapping
    class FakeModule(object):
        def __init__(self):
            self.params = {'data': 'pong'}
    import ansible.builtin
    try:
        ansible.builtin.ping.main()
        assert False, "Expected an exception"
    except Exception:
        pass
    try:
        ansible.builtin.ping.main(FakeModule())
        assert False, "Expected an exception"
    except Exception:
        pass
    ansible.builtin.ping.main(FakeModule())

# Generated at 2022-06-13 05:51:44.404947
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    result = dict(
        ping='test',
    )

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert main() == module.exit_json(**result)


# Generated at 2022-06-13 05:51:51.169992
# Unit test for function main
def test_main():
    with pytest.raises(Exception, match='boom'):
        module = AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )

        result = dict(
            ping=module.params['data'],
        )

        if module.params['data'] == 'crash':
            raise Exception("boom")

        module.exit_json(**result)

# Generated at 2022-06-13 05:51:56.402626
# Unit test for function main
def test_main():
    args = {
            'data': 'pong'
    }
    rc = None
    out = None
    err = None
    result = None

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

# Generated at 2022-06-13 05:52:02.319504
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


# Generated at 2022-06-13 05:52:03.664812
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:52:06.860787
# Unit test for function main
def test_main():
    data = dict(
        data='pong',
    )
    module = AnsibleModule(data)
    result = dict(
        ping=module.params['data'],
    )
    assert result == main()

# Generated at 2022-06-13 05:52:11.661784
# Unit test for function main
def test_main():
    import sys
    import os

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    import ansible.builtin.ping as mymodule

    #Unit test expected output
    testResult = dict(
        ping="pong",
    )

    testParams = dict(
        data="pong",
    )

    assert mymodule.main(testParams) == testResult

# Generated at 2022-06-13 05:52:15.737367
# Unit test for function main
def test_main():
    args = dict(
        data='crash',
    )
    with pytest.raises(Exception) as excinfo:
        main(args)
    assert 'boom' in str(excinfo)

# Generated at 2022-06-13 05:52:19.113770
# Unit test for function main
def test_main():
  module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
  )
  assert main(module) == None

# Generated at 2022-06-13 05:52:21.876282
# Unit test for function main
def test_main():
    class Options:
        data = 'pong'
    module = AnsibleModule(argument_spec=Options(), supports_check_mode=True)
    result = dict(ping='pong')
    assert main() == module.exit_json(**result)

# Generated at 2022-06-13 05:52:57.412661
# Unit test for function main
def test_main():
    import sys
    module_args = dict(
        data="pong",
    )
    obj = AnsibleModule(**module_args)
    obj.exit_json = lambda **kwargs: sys.exit(0)
    main()

# Generated at 2022-06-13 05:52:58.038271
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:53:03.522347
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

# Generated at 2022-06-13 05:53:09.297799
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
    
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:53:11.459397
# Unit test for function main
def test_main():
    data1 = dict(
        data=dict(type='str', default='pong')
    )
    module = AnsibleModule(**data1)
    try:
        main()
    except Exception as e:
        print("Exception thrown: '{}'".format(e))
    else:
        print("No exceptions thrown!")


# Generated at 2022-06-13 05:53:15.177114
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    import pytest
    with pytest.raises(Exception):
        module.params['data'] = 'crash'
        main()

# Generated at 2022-06-13 05:53:21.539327
# Unit test for function main
def test_main():
    import pytest
    import os
    import collections
    import copy

    class MockModule:
        def __init__(self, params):
            self.params = params

        def fail_json(self, fail_msg):
            raise Exception(fail_msg)

    class MockException(Exception):
        pass

    # When data == "crash" we should see an exception
    params = {'data': 'crash'}
    module = MockModule(params)
    with pytest.raises(MockException, match='boom'):
        main()

    # pong by default
    params = {}
    module = MockModule(params)
    try:
        main()
    except Exception as err:
        assert False, "Unexpected exception: {}".format(err)

    # params['data'] value set to what we specify.

# Generated at 2022-06-13 05:53:28.609454
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import get_exception
    # Project mock_module from Ansible
    from ansible.module_utils.ping import AnsibleModule

    ANSIBLE_MODULE_INSTANCE = AnsibleModule(
        "ansible", "test arg"
    )
    
    ANSIBLE_MODULE_INSTANCE.params["data"] = "test data"
    result = dict(
        ping=ANSIBLE_MODULE_INSTANCE.params['data'],
    )
    assert main() == result

# Generated at 2022-06-13 05:53:35.526143
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

import unittest
import sys

# Generated at 2022-06-13 05:53:36.157396
# Unit test for function main
def test_main():
    with pytest.raises(Exception):
        main()

# Generated at 2022-06-13 05:54:54.604198
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Test if module crash
    try:
        main()
    except Exception as e:
        print(e)
        assert False

    # Test if module works as expected
    result = main()
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:54:55.077753
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-13 05:54:58.590097
# Unit test for function main
def test_main():
    fake_module_args = {
        'data': 'pong',
    }
    fake_module = AnsibleModule(fake_module_args)
    # Fake ansible_module.exit_json() calls exit()
    fake_module.exit_json = lambda *args, **kwargs: exit()

    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:55:02.098249
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
    )
    assert main() == "fooasdf"

# Generated at 2022-06-13 05:55:07.468921
# Unit test for function main
def test_main():
    # mock function call for function main
    with patch('ansible_collections.ansible.builtin.plugins.module_utils.basic.AnsibleModule.exit_json', side_effect=Mock(return_value=None)):
        cur_argv = list(sys.argv)
        sys.argv = cur_argv[:1] + ['data=crash', 'foo=bar']
        main()
        sys.argv = cur_argv


# Generated at 2022-06-13 05:55:12.448055
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.basic import AnsibleModule

    def fake_exit_json(**kwargs):
        sys.modules[__name__].exit_json = fake_exit_json
        return

    # Expected result
    result = {
        'ping': 'pong'
    }

    # Can't test the module directly as it uses ansible.utils.module_docs_fragments
    # Will just test the main function
    with pytest.raises(Exception) as exc:
        main()
    assert get_exception() == "boom"

    # Test with a good data
    sys.modules[__name__].exit_json = fake_exit_json
    main()

# Generated at 2022-06-13 05:55:24.398507
# Unit test for function main

# Generated at 2022-06-13 05:55:34.356278
# Unit test for function main
def test_main():
    import sys
    module_name = sys.modules[__name__].__file__

    # When the module is imported, the test_main() function could not be called
    # directly because it is not defined yet.
    # Just a workaround to import the module again
    import imp
    m = imp.load_source(module_name[0:module_name.rfind(".py")], module_name)

    # m is the loaded module
    assert isinstance(m, object)

    # module is a global variable which holds the module object
    global module
    module = m

    # Call main()
    assert module.main() == None

# Generated at 2022-06-13 05:55:40.529533
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

# Generated at 2022-06-13 05:55:44.967220
# Unit test for function main
def test_main():
    class AnsibleModuleDummy:
        def __init__(self):
            self.params = {'data': 'pong'}
    my_ansible_module = AnsibleModuleDummy()
    assert main(my_ansible_module) == {'ping': 'pong'}
    assert my_ansible_module.exit_json.called

# Generated at 2022-06-13 05:58:24.590431
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()


# Generated at 2022-06-13 05:58:34.609845
# Unit test for function main
def test_main():
    import mock
    import ansible.module_utils.basic as basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.errors import AnsibleAction, AnsibleActionFail

    m = mock.Mock()
    m.get_bin_path.return_value = "/usr/bin/python"
    basic._SUDO_BINARY = "/usr/bin/sudo"
    basic.ANSIBLE_MODULE_ARGS = {}
    basic.ANSIBLE_PYTHON_INTERPRETER = "/usr/bin/python"
    basic.HAS_BOTO = False

    params = {
        'data': 'pong',
        'ANSIBLE_MODULE_ARGS': {},
    }

# Generated at 2022-06-13 05:58:35.063684
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:58:37.520468
# Unit test for function main
def test_main():
    m = AnsibleModule(
        argument_spec=dict(
            data=dict(required=True, type='str'),
        ),
        supports_check_mode=True
    )
    assert 'pong' in main(m)

# Generated at 2022-06-13 05:58:40.558456
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

# Generated at 2022-06-13 05:58:41.992763
# Unit test for function main
def test_main():
    mock_module = Mock(params=dict(data='pong'))
    assert main() == (dict(ping='pong'), None)

# Generated at 2022-06-13 05:58:44.635933
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:58:49.326817
# Unit test for function main
def test_main():
    testargs = { 'data': 'pong' }
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        # Call main() as tried in the code
        main()
        # Assert we get a SystemExit exception
        assert pytest_wrapped_e.type == SystemExit
        # and that it's error code is 1
        assert pytest_wrapped_e.value.code == 1