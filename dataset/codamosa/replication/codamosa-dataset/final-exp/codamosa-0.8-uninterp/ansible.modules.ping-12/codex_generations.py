

# Generated at 2022-06-13 05:49:08.205834
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


    # Mock AnsibleModule
    class MockAnsibleModule(object):
        """
        fake AnsibleModule class
        """
        def __init__(self, argument_spec, **kwargs):
            self.params = {}
            self.argument_spec = argument_spec

        def exit_json(self, **kwargs):
            return kwargs

        def fail_json(self, **kwargs):
            return kwargs

    # Mock AnsibleModule
    class MockAnsibleModule2(object):
        """
        fake AnsibleModule class
        """
        def __init__(self, argument_spec, **kwargs):
            self.params = {"data": "crash"}
            self.argument_spec = argument_spec


# Generated at 2022-06-13 05:49:14.283063
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

# Generated at 2022-06-13 05:49:20.343568
# Unit test for function main
def test_main():
    # make sure that we can ping
    res_args = dict(
        ANSIBLE_MODULE_ARGS=dict(data='pong')
    )
    result = AnsibleModule(**res_args).ping()
    assert result['ping'] == 'pong'

    # make sure that we can crash
    res_args = dict(
        ANSIBLE_MODULE_ARGS=dict(data='crash')
    )
    result = AnsibleModule(**res_args).ping()
    assert result['ping'] == 'crash'

# Generated at 2022-06-13 05:49:24.973594
# Unit test for function main
def test_main():
    # Test with crash
    result = main()
    assert result['ping'] == 'pong'
    assert result == 'pong'
    
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:49:30.024654
# Unit test for function main
def test_main():
    field, data, kwargs = "data", {}, {}
    kwargs[field] = {"default": "pong", "type": "str"}
    args = dict2namedtuple(kwargs)
    module = AnsibleModule(argument_spec=args)
    result = main()
    assert result["ping"] == "pong"

# Generated at 2022-06-13 05:49:36.237676
# Unit test for function main
def test_main():
    # If a particular function is tested, add the @patch decorator to patch the output of that function
    # For example - use @patch('ansible.module_utils.network.common.edit_config')
    # or @patch('ansible.builtin.win_ping.AnsibleModule')
    # To run the unit tests, run following command from the root dir:
    # python -m pytest --cov-report= --cov=lib/ansible/modules/windows/win_ping -v -s
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        )
    )
    result = dict(
        ping=module.params['data'],
    )
    module.exit_json(**result)


# Generated at 2022-06-13 05:49:42.558921
# Unit test for function main
def test_main():
    """ Implements unit test for main function """

    from ansible.module_utils.basic import AnsibleModule

    # Set up the class object for this module with the module_args parameter
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )


    # Make the results dictionary
    result = dict(
        ping=module.params['data'],
    )

    # Print the results
    print(str(result))

    # Exit with an error when the data parameter is crash
    if module.params['data'] == 'crash':
        raise Exception("boom")

    # Exit with success
    module.exit_json(**result)

# Demonstrate success
test_main()

# Demonstrate

# Generated at 2022-06-13 05:49:50.949062
# Unit test for function main
def test_main():
    import sys
    import os

    # For the test to work, we must:
    # * Not have the environment variable ANSIBLE_MODULE_ARGS set.  If this gets
    #   set, code within AnsibleModule will read its values for the parameters
    #   and we can't easily override those values.
    # * Have the environment variable ANSIBLE_MODULE_ARGS set to valid json
    #   that represents the parameters to the module.
    # * Monkey patch the AnsibleModule.__init__ method so that it will save the
    #   module_args and json_args that it was passed.
    # * Monkey patch the exit_json and fail_json methods so that they won't exit
    #   but will instead save their parameters to their respective names.

    # Save the values of these so we can restore them after the test.
   

# Generated at 2022-06-13 05:49:55.783125
# Unit test for function main
def test_main():
    test_main.__name__ = 'test_' + main.__name__
    if hasattr(module, 'exit_json'):
        module.exit_json = AnsibleModule.exit_json
    if hasattr(module, 'fail_json'):
        module.fail_json = AnsibleModule.fail_json
    main()

# Generated at 2022-06-13 05:50:06.077128
# Unit test for function main
def test_main():
    print("""
Uncomment the tests below and run:
    python -m ansible.modules.ping.test_ping
""")
    # from ansible.module_utils.basic import AnsibleModule

    # run the module without fail_json() calls for now
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    # module.fail_json(msg="FAILED")
    # module.exit_json(msg="OK")
    module.exit_json(**dict(
        ping=module.params['data'],
    ))

# Generated at 2022-06-13 05:50:11.132428
# Unit test for function main
def test_main():
    result = main()
    assert result == {'msg': 'Hello'}

# Generated at 2022-06-13 05:50:20.501933
# Unit test for function main
def test_main():
    import pytest
    import json
    from ansible.module_utils.common._collections_compat import Mapping
    with pytest.raises(Exception) as excinfo:
        main()
    assert excinfo.value.message == "boom"

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        test_main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
    pytest_wrapped_e.traceback = pytest.PytestWarning
    assert isinstance(json.loads(json.dumps(dict(ping='pong'), indent=4)), Mapping)

# Generated at 2022-06-13 05:50:22.389396
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit as e:
        assert e.args[0] == 0
        # Successful exit


# Generated at 2022-06-13 05:50:23.514016
# Unit test for function main
def test_main():
    # Verify function returns "pong"
    assert main() == "pong"

# Generated at 2022-06-13 05:50:25.970740
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:50:36.957057
# Unit test for function main
def test_main():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    import sys

    # Encoding module test
    mb_data = b'{"invocation": {"module_name": "ping", "module_args": {"data": "pong"}}, "changed": false, "ping": "pong"}'
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    func_result = dict(
        ping='pong',
    )
    result = module.exit_json(**func_result)
    assert result == mb_data
    # Crash module test

# Generated at 2022-06-13 05:50:40.529185
# Unit test for function main
def test_main():
    module = AnsibleModule()
    module.params['data'] = 'pong'
    result = dict(ping="pong")
    module.exit_json(**result)


# Generated at 2022-06-13 05:50:47.431255
# Unit test for function main
def test_main():
    # make the argument names more intuitive
    args = dict(
        data='pong'
    )

    # make a dummy AnsibleModule object
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(**args)

    # run the function to test with the arguments above
    result = main()

    # assert that the resulting object has all the right keys
    assert result.keys() == ['ping']
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:50:53.356111
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert main() == module.exit_json(**dict(
        ping=module.params['data'],
    ))


# Generated at 2022-06-13 05:50:59.412925
# Unit test for function main
def test_main():
    # Test case 1: no options include
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



# Generated at 2022-06-13 05:51:12.492437
# Unit test for function main
def test_main():

    testarg_data = "pong"
    testarg_data_optional = None
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    # To replace module
    module.params['data'] = testarg_data
    # Run the actual function
    main()

# Generated at 2022-06-13 05:51:16.517398
# Unit test for function main
def test_main():
    # verify main function returns without error
    assert main()



# Generated at 2022-06-13 05:51:23.211276
# Unit test for function main
def test_main():
    mod_args = dict(
        data='pong',
    )

    results = dict(
        ping='pong',
    )

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.exit_json(**results)

# Generated at 2022-06-13 05:51:26.415685
# Unit test for function main
def test_main():
  # test empty argument
  # assert that result is as epected with empty argument
  # assert that result is as epected with empty argument
  # assert that result is as epected with empty argument
  # assert that result is as epected with empty argument
  assert True == False

# Generated at 2022-06-13 05:51:36.056972
# Unit test for function main
def test_main():
    # set up test environment
    import sys

    if 'ansible.builtin.ping' not in sys.modules:
        # Workaround to give the test class access to the test class's name
        # Use this instead of the module name to be sure that other directories
        # with the same name as the module don't cause problems
        # (https://github.com/ansible/ansible/commit/d5d5db139f5b6d04c1f5d6c49e639fae8e0a1572)
        sys.modules['ansible.builtin.ping'] = sys.modules[__name__]

    import ansible.modules.ping as ping

    # place objects in test environment of module
    ping.main()

# Generated at 2022-06-13 05:51:48.185755
# Unit test for function main
def test_main():
    def test_ansible_module(result):
        if result['invocation']['module_name'] == 'ping':
            assert result['ping'] == 'pong'
        else:
            raise Exception('Unexpected module: {}'.format(result['invocation']['module_name']))

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert module.params['data'] == 'pong'

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

    if module.params['data'] == 'crash':
        raise Exception("boom")


# Generated at 2022-06-13 05:51:48.726994
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:51:55.639474
# Unit test for function main
def test_main():
    # Test a successful ping
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
    )
    result = dict(
        ping=module.params['data'],
    )
    module.exit_json(**result)
    assert module.params['data'] == 'pong'

    # Test a crashing ping
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='crash'),
        ),
    )
    result = dict(
        ping=module.params['data'],
    )
    with pytest.raises(Exception, match='boom'):
        module.exit_json(**result)

# Generated at 2022-06-13 05:52:07.376107
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Mock module.exit_json to make sure we're getting the right one
    exit_json_mock = MagicMock()
    module.exit_json = exit_json_mock

    args = {'data': 'pong'}
    main()

    expected_result = dict(
        ping=module.params['data'],
    )

    assert exit_json_mock.call_args[0][0] == expected_result

    # Now test with the data=crash
    args = {'data': 'crash'}
    exit_json_mock.reset_mock()

# Generated at 2022-06-13 05:52:09.028651
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as ex:
        assert False, "An exception occured: "+ex.message

# Generated at 2022-06-13 05:52:36.149328
# Unit test for function main
def test_main():
    from ansible.modules.network.nxos import nxos_ping
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network_common import to_list

    _mock_module = lambda *args, **kwargs: _mock_module_helper(
                                              module_file='/usr/lib/python2.7/dist-packages/ansible/modules/network/nxos/nxos_ping.py',
                                              *args, **kwargs)

    def _ansible_module_helper(module_file, *args, **kwargs):
        args = to_list(args)


# Generated at 2022-06-13 05:52:39.892053
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

# Generated at 2022-06-13 05:52:41.000476
# Unit test for function main
def test_main():
    result = {}
    result['ping'] = 'pong'
    assert main() == result

# Generated at 2022-06-13 05:52:42.493420
# Unit test for function main
def test_main():
    args = dict(
        data='pong',
    )
    module = AnsibleModule(argument_spec=args)
    main()

# Generated at 2022-06-13 05:52:46.657755
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
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

# Generated at 2022-06-13 05:52:48.507424
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong')
        ),
        supports_check_mode=True
    )

    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:52:51.213134
# Unit test for function main
def test_main():
    # A) Setup Test
    import ansible.module_utils.basic
    testmodule = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # B) Test Execution
    result = main()

    # C) Test Assertions
    assert result == {'changed': False, 'ping': 'pong'}

# Generated at 2022-06-13 05:52:53.401921
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

# Generated at 2022-06-13 05:53:00.124096
# Unit test for function main
def test_main():
    # Set up mock arguments and custom return value for function 'main'
    module_mock = {'params': {'data': 'pong'}}
    result_mock = {'changed': False}
    module = AnsibleModule(**module_mock)
    result = main(module)

    # Assert that the mock return value matches the return value of the function
    assert result == result_mock

# Generated at 2022-06-13 05:53:10.882201
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, BasicException
    from ansible.module_utils import common_err, errors
    import ansible.module_utils.ping as ping
    import errno
    import json
    import os
    import shutil
    import sys
    from tempfile import mkdtemp
    from ansible.utils.display import Display
    from ansible import constants as C
    import traceback
    display = Display()
    display.verbosity = 3

    # Set default dir to use for tmp files
    tempdir = mkdtemp()

    # Encode dummy data in the same format as a real argument file
    data = json.dumps({"ANSIBLE_MODULE_ARGS": {"data": 'pong'}})
    data = data.replace(' ', '')

# Generated at 2022-06-13 05:53:41.938255
# Unit test for function main
def test_main():
  main()

# Generated at 2022-06-13 05:53:53.115053
# Unit test for function main
def test_main():

    # We should be able to use the module object here, but it does not seem
    # to be auto-imported for us.  We will just import it manually.
    import ansible.modules.builtin.ping

    # We will not use the AnsibleModule class here as that is now being tested.
    # We will simply create our own dict with the parameters we expect to
    # pass the function.
    test_args = dict(
        data='pong',
    )

    # Unit test main() using a fake AnsibleModule object
    result = ansible.modules.builtin.ping.main()

    # We should get a dict as a result
    assert type(result) == dict

    # Check the contents of the dict to make sure it matches what
    # we expected.
    if result['ping'] != 'pong':
        raise Assert

# Generated at 2022-06-13 05:53:56.841124
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
  
  print(module.params['data'])
  
test_main()

# Generated at 2022-06-13 05:54:05.011830
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.ansible_ping import main
    import json
    
    attrs = {
        'test': {
            'data': 'pong'
        }
    }
    # This is the way to pass params to a function under test
    # using the AnsibleModule object's params dictionary.
    # Since AnsibleModule is a dictionary subclass it's easy to set
    # the params using a dict object's syntax.
    module = AnsibleModule(params=attrs['test'])
    
    main()
    
    assert module.exit_json.called
    assert module.exit_json.call_args[0][0] == {'ping': "pong"}

# Generated at 2022-06-13 05:54:08.909797
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec = dict(
            data = dict(type = 'str', default = 'pong'),
        ),
        supports_check_mode = True
    )

    if test_module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping = test_module.params['data'],
    )

    test_module.exit_json(**result)

# Generated at 2022-06-13 05:54:13.555457
# Unit test for function main
def test_main():
    test_result = {'ping': 'pong'}
    test_module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)
    test_module.exit_json(**test_result)
    assert test_module.params['data'] == 'ping'

# Generated at 2022-06-13 05:54:22.820107
# Unit test for function main
def test_main():
    # Patch the AnsibleModule for testing
    module_mock = MagicMock(spec=AnsibleModule)
    module_mock._debug = False
    module_mock.params = {'data': 'pong'}
    module_mock.exit_json = MagicMock(return_value=0)
    module_mock.fail_json = MagicMock(return_value=0)

    # Run the function under test
    main()

    # Make sure we called exit_json with the correct result
    # module_mock.exit_json.assert_called_once_with(changed=False, msg='pong')

# Generated at 2022-06-13 05:54:28.595271
# Unit test for function main
def test_main():
    argv = [
        'ping',
        '-a', 'data=pong'
    ]
    fake_args = dict(
        data='pong'
    )
    ansible_args = [
        'ansible-playbook',
        'ansible.builtin.ping'
    ]
    AnsibleModule.main(ansible_args, argv, fake_args)

# Generated at 2022-06-13 05:54:32.152247
# Unit test for function main
def test_main():
    argv = [
        'ping',
        '-a', 'data=crash',
    ]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(argv)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

# Generated at 2022-06-13 05:54:38.709020
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import sys
    import os
    import json

    tmpdir = os.path.dirname(sys.argv[0])
    module_path = os.path.join(tmpdir, 'ansible_test.py')


# Generated at 2022-06-13 05:55:53.788593
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:56:04.036140
# Unit test for function main
def test_main():
    content = "---\n"
    content += "module: ping\n"
    content += "version_added: historical\n"
    content += "short_description: Try to connect to host, verify a usable python and return C(pong) on success\n"
    content += "description:\n"
    content += "  - A trivial test module, this module always returns C(pong) on successful\n"
    content += "    contact. It does not make sense in playbooks, but it is useful from\n"
    content += "    C(/usr/bin/ansible) to verify the ability to login and that a usable Python is configured.\n"
    content += "  - This is NOT ICMP ping, this is just a trivial test module that requires Python on the remote-node.\n"

# Generated at 2022-06-13 05:56:04.663356
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:56:11.265440
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={'data': {'default': 'pong', 'type': 'str'}}, supports_check_mode=True)
    module.params = {'data': 'pong'}
    result = dict(ping='pong')
    assert result == main(module)

# Generated at 2022-06-13 05:56:11.979384
# Unit test for function main
def test_main():
    print("no")

# Generated at 2022-06-13 05:56:22.888491
# Unit test for function main
def test_main():
  # Unit test for function main
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')),
                           supports_check_mode=True)

    if module.params['data'] == 'crash':
        raise Exception('boom')

    result = {'ping': module.params['data']}
    module.exit_json(**result)

#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2012, Mickael Hoarau <mhoarau@makina-corpus.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either

# Generated at 2022-06-13 05:56:25.077790
# Unit test for function main
def test_main():
    ping_args = dict(
        data='pong',
    )
    with pytest.raises(SystemExit):
        main(ping_args)

# Generated at 2022-06-13 05:56:28.810071
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    module.exit_json(ping=module.params['data'])

# Generated at 2022-06-13 05:56:29.594248
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-13 05:56:31.654814
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    assert module.params['data'] == 'pong'
    assert module.check_mode is False