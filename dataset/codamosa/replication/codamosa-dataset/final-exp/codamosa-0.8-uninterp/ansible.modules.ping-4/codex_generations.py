

# Generated at 2022-06-13 05:49:06.835408
# Unit test for function main
def test_main():
    test_module = AnsibleModule({'data': {'type': 'str', 'default': 'pong'}}, "0")

    try:
        main(test_module)
    except Exception as e:
        assert False
        assert "boom" in e.message

    test_module = AnsibleModule({'data': {'type': 'str', 'default': 'crash'}}, "0")

    try:
        main(test_module)
    except Exception as e:
        assert "boom" in e.message

# Generated at 2022-06-13 05:49:07.789466
# Unit test for function main
def test_main():
    from ansible.module_utils.common.removed import removed
    assert removed('ping')

# Generated at 2022-06-13 05:49:11.604513
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert module.ping('data') == 'pong'

# Generated at 2022-06-13 05:49:21.173954
# Unit test for function main
def test_main():
    import collections

    # Mock the AnsibleModule
    mock_AnsibleModule = collections.namedtuple('MockAnsibleModule', ['params'])
    mock_AnsibleModule.params = {'data': 'crash'}

    # Mock the exception
    mock_Exception = collections.namedtuple('MockException', ['args'])
    mock_Exception.args = ((),)

    # Mock the exit_json method
    mock_exit_json = collections.namedtuple('MockExitJson', ['called'])
    mock_exit_json.called = False

    # Mock the fail_json method
    mock_fail_json = collections.namedtuple('MockFailJson', ['called'])
    mock_fail_json.called = False

    # Mock the import_module method

# Generated at 2022-06-13 05:49:21.670571
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:49:26.384504
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
    )
    test_result = dict(
        ping=module.params['data'],
    )
    assert main() == test_result

# Test crash function

# Generated at 2022-06-13 05:49:32.139689
# Unit test for function main
def test_main():
    argument_spec = dict(
        data=dict(type='str', default='pong'),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )
    module.params['data'] = 'crash'
    try:
        main()
    except:
        pass
    else:
        assert False, "Exception was expected"

# Generated at 2022-06-13 05:49:35.309467
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()


# Generated at 2022-06-13 05:49:36.071135
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()


# Generated at 2022-06-13 05:49:36.799927
# Unit test for function main
def test_main():
    try:
        main()
    except:
        print("error")

# Generated at 2022-06-13 05:49:41.932053
# Unit test for function main
def test_main():
    import sys, os


# Generated at 2022-06-13 05:49:43.967072
# Unit test for function main
def test_main():
    from . import ping
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    ping.main()



# Generated at 2022-06-13 05:49:47.292467
# Unit test for function main
def test_main():
    data = 'pong'
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default=data)), supports_check_mode=True)
    result = dict(ping=module.params['data'])
    assert result['ping'] == data

# Generated at 2022-06-13 05:49:48.217572
# Unit test for function main
def test_main():
    assert main() == main()

# Generated at 2022-06-13 05:49:54.476766
# Unit test for function main
def test_main():
    from ansible.module_utils.ping import main
    from ansible.module_utils.common._collections_compat import Mapping

    result = main()
    assert isinstance(result, Mapping)

    result = main(dict(data='crash'))
    assert result == dict(failed=dict(msg='boom'))

# Generated at 2022-06-13 05:49:56.130193
# Unit test for function main
def test_main():
    print("hi")
    # test_module=ansible.builtin.ping
    # test_module.main()

# Generated at 2022-06-13 05:50:04.607081
# Unit test for function main
def test_main():
    """
    Function: test_main()
    Description: unit test for function main()
    """

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params.get('data') == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params.get('data'),
    )

    assert result == dict(
        ping='pong',
    )

# Generated at 2022-06-13 05:50:10.537774
# Unit test for function main
def test_main():
    import copy
    import json

    # Create the test fixture
    data = {'changed': False, 'data': 'pong'}

    # Call the function to be tested
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = module.exit_json(data = data)
    assert result == {'changed': False, 'data': {'changed': False, 'data': 'pong'}, 'failed': False, 'rc': 0}

# Generated at 2022-06-13 05:50:11.591866
# Unit test for function main
def test_main():
    with pytest.raises(Exception):
      main()

# Generated at 2022-06-13 05:50:12.138142
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:50:23.912708
# Unit test for function main
def test_main():
    # Example test case
    module1 = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module1.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module1.params['data'],
    )

    module1.exit_json(**result)

    # Example test case
    module2 = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module2.params['data'] == 'crash':
        raise Exception("boom")


# Generated at 2022-06-13 05:50:27.658281
# Unit test for function main
def test_main():

    # Test with no arguments specified
    module = AnsibleModule(argument_spec=dict())


if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-13 05:50:31.478555
# Unit test for function main
def test_main():
    ping_data = dict(
        data='pong',
    )
    set_module_args(ping_data)
    result = main()
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:50:41.252307
# Unit test for function main
def test_main():
    import json
    import ansible_ping

    self = type('', (), {})()
    self.params = dict()

    # Unit tests with no ping data
    module = type('', (), {})()
    module.params = self.params
    setattr(module, 'exit_json', lambda x, **kwargs: test_main.ping_data)
    ansible_ping.main()
    assert json.loads(test_main.ping_data)['ping'] == 'pong'

    # Unit tests with ping data
    test_data = 'Test Ansible Ping'
    module = type('', (), {})()
    module.params = self.params
    self.params['data'] = test_data
    setattr(module, 'exit_json', lambda x, **kwargs: test_main.ping_data)
    ans

# Generated at 2022-06-13 05:50:41.939148
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:50:47.588417
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=False
    )
    result = module.run_command('ping')
    assert result[0] == 0
    assert result[1] == 'pong'

# Generated at 2022-06-13 05:50:53.811140
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import ImmutableDict
    module_args = ImmutableDict(
        data='pong',
        diff=True,
        ignore_check_mode=False,
        check=False,
        diff_match='strict',
        diff_ignore_lines=None
    )

    assert main(module_args) == None

# Generated at 2022-06-13 05:50:58.215752
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    try:
        main()
    except Exception:
        pass
    else:
        assert False, 'Exception not raised'

# Generated at 2022-06-13 05:51:08.404329
# Unit test for function main
def test_main():
    sample_run_result = None
    sample_exit_json_result = None
    sample_fail_json_result = None
    with mock.patch('ansible.module_utils.basic.AnsibleModule') as m:
        m.return_value.params = {}
        m.return_value.check_mode = True
        sample_run_result = main()
        sample_exit_json_result = exit_json(msg='goodbye', changed=True, foo='bar')
        sample_fail_json_result = fail_json(msg='goodbye', **result)
    assert sample_run_result == sample_exit_json_result
    assert sample_run_result == sample_fail_json_result

# Generated at 2022-06-13 05:51:10.896746
# Unit test for function main
def test_main():
    test_args = ['--data','pong']
    import sys
    sys.argv = ['ansible-test-ping'] + test_args
    main()

# Generated at 2022-06-13 05:51:25.363219
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    
    
    assert module.params['data'] == False

    result = dict(
        ping=module.params['data'],
    )
    assert result['ping'] is not None
    assert result['ping'] == 'pong'

test_main()

# Generated at 2022-06-13 05:51:31.406271
# Unit test for function main
def test_main():
    # test case
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert main() == module.exit_json(ping=module.params['data'])

# Generated at 2022-06-13 05:51:39.130734
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Test module.params['data'] == 'pong'
    module.params['data'] = 'pong'
    result = dict(
        ping=module.params['data'],
    )
    assert result == {
        'ping': 'pong'
    }

    # Test module.params['data'] == 'crash'
    module.params['data'] = 'crash'
    try:
        result = dict(
            ping=module.params['data'],
        )
    except Exception:
        pass

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:51:49.790232
# Unit test for function main
def test_main():
   import imp
   import tempfile
   import os

   fd, my_tmpfile = tempfile.mkstemp()
   os.close(fd)
   os.remove(my_tmpfile)
   my_tmpfile_fh = open(my_tmpfile, 'w')


# Generated at 2022-06-13 05:51:51.585138
# Unit test for function main
def test_main():
    data = dict(data='pong')
    module = AnsibleModule(data)
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:51:59.901858
# Unit test for function main
def test_main():
    from ansible_collections.ibmdec.power_ibmi.tests.unit.compat import unittest
    from ansible_collections.ibmdec.power_ibmi.tests.unit.compat.mock import MagicMock
    from ansible_collections.ibmdec.power_ibmi.tests.unit.modules.utils import set_module_args, AnsibleExitJson

    WORKING_MODULE_PATH = "ansible_collections.ibmdec.power_ibmi.plugins.modules.ping.py"

# Generated at 2022-06-13 05:52:06.819603
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

# Generated at 2022-06-13 05:52:11.620489
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

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:52:15.728301
# Unit test for function main
def test_main():
    module_args = dict(
        data='pong'
    )
    with pytest.raises(Exception) as execinfo:
        main(**module_args)
    assert "boom" in str(execinfo)