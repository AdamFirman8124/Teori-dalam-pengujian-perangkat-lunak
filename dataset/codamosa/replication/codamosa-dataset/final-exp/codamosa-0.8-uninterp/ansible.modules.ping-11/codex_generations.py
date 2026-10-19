

# Generated at 2022-06-13 05:49:08.015787
# Unit test for function main
def test_main():
    # The following are some test cases to exercise the code.
    # ansible-test units --python bin/ping.py
    # ansible-test units --python bin/ping.py --tox

    # These tests use the mock library. See examples here:
    # https://docs.python.org/3/library/unittest.mock.html
    # https://docs.ansible.com/ansible/latest/dev_guide/testing_unit_testing.html

    with patch('ansible.module_utils.basic.AnsibleModule'):
        mymod = AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )
        assert mymod.params['data'] == 'pong'

        mymod.params

# Generated at 2022-06-13 05:49:09.167419
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:49:16.026326
# Unit test for function main
def test_main():
    # Set up mock object
    m = Mock()
    
    # Set up mock objects
    m.module.params = {
        'data': 'pong'
    }
    
    # Set up expected results
    expected_results = dict(
        ping='pong'
    )
    
    # Run main function
    main()
    
    # Check if function exit_json was called with expected results
    m.module.exit_json.assert_called_once_with(**expected_results)

# Generated at 2022-06-13 05:49:25.028606
# Unit test for function main
def test_main():
    import sys
    import json
    import pytest

    if sys.version_info[:2] < (2, 7):
        pytest.skip(msg="Requires python version 2.7 or higher.")

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    stdin = sys.stdin

    # Encoding of the test may vary depending on whether the test is being run
    # inside or outside of the Python interpreter:
    # Inside python:
    #   sys.stdin.encoding
    # Outside python:
    #   sys.stdin.encoding = None
    #   sys.stdin = open('/dev/stdin', 'rb')
    # so check for both.
    if sys.stdin.encoding is not None:
        encoding = sys

# Generated at 2022-06-13 05:49:29.224987
# Unit test for function main
def test_main():
    m = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert m.params['data'] == 'pong'
    assert m.supports_check_mode

# Generated at 2022-06-13 05:49:36.208887
# Unit test for function main
def test_main():
    import ansible.module_utils.basic as utils
    import ansible.module_utils.basic.AnsibleModule as ans
    class TestException(Exception):
        pass
    testmod = utils.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    with pytest.raises(TestException):
        testmod.params['data'] = 'crash'
        main()

    testmod.params['data'] = 'pong'
    main()

# Generated at 2022-06-13 05:49:40.332481
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


# Generated at 2022-06-13 05:49:49.384049
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    m = ansible.module_utils.basic.AnsibleModule(argument_spec={'data': {'type': 'str', 'default': 'pong'}}, supports_check_mode=True)
    m.params = {'data': 'some_data', '_ansible_check_mode': True}
    setattr(m, 'exit_json', lambda d: None)
    setattr(m, 'exit_json', lambda d: None)
    assert m.check_mode is True
    import ansible.module_utils.basic
    assert m.params['data'] == 'some_data'
    with pytest.raises(Exception) as excinfo:
        main()
    assert 'boom' in str(excinfo.value)

# Generated at 2022-06-13 05:49:51.933111
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:49:52.478635
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:50:04.232072
# Unit test for function main
def test_main():
    print ("testing")
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    print (module.params['data'])
    result = {u'changed': False, u'ping': u'pong'}
    assert result == main(module)
    result = {u'changed': False, u'ping': u'not pong'}
    assert result != main(module)

# Generated at 2022-06-13 05:50:08.853424
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import json

    params = dict(
        data='pong',
    )
    obj = AnsibleModule(argument_spec=params, check_invalid_arguments=False)
    obj.params['ANSIBLE_MODULE_ARGS'] = params
    main()


# Generated at 2022-06-13 05:50:14.746294
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main == 'pong'
    main()

# Generated at 2022-06-13 05:50:17.246972
# Unit test for function main
def test_main():
    import sys
    sys.argv = ['ansible-ping.py', ""]
    result = main()
    print(result)
    assert result

# Generated at 2022-06-13 05:50:26.599125
# Unit test for function main
def test_main():
    from ansible_collections.misc.not_a_real_collection.plugins.modules import ansible_ping
    from ansible.module_utils import basic
    import tempfile
    import os

    (fd, test_path) = tempfile.mkstemp()
    os.close(fd)

# Generated at 2022-06-13 05:50:31.077230
# Unit test for function main
def test_main():
    # Test
    # m = DummyModule(params={'data': 'crash'})
    # result = main(m)
    # assert result['failed']
    # assert result['msg'] == 'boom'
    pass

# Generated at 2022-06-13 05:50:39.357838
# Unit test for function main
def test_main():
  data = {
    'data': 'abc',
  }
  
  #mock AnsibleModule
  class MockAnsibleModule:
    def __init__(self, data):
      self.params = data

    def exit_json(self, **args):
      return args

    def fail_json(self, **args):
      return args
      
  mock_module = MockAnsibleModule(data)
  
  #run
  result = main()

  #assert
  assert result['ping'] == data['data']
  
  # mock exception
  data = {
    'data': 'crash',
  }
  mock_module = MockAnsibleModule(data)
  success_result = main()

# Generated at 2022-06-13 05:50:45.130642
# Unit test for function main
def test_main():
    ansible_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert ansible_module.params['data'] == 'pong'
    # assert ansible_module.exit_json(**result) == {'ping': 'pong'}

# Generated at 2022-06-13 05:50:47.825900
# Unit test for function main
def test_main():

    import doctest
    import ansible.modules.system.ping as ping
    doctest.testmod(ping)

# Generated at 2022-06-13 05:50:52.740338
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
    return result

# Generated at 2022-06-13 05:51:01.089054
# Unit test for function main
def test_main():
    assert main() == True

# Generated at 2022-06-13 05:51:09.603194
# Unit test for function main
def test_main():
  try:
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    assert PY3, 'This module does not work with Python2'

    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    assert 'ping' not in module.params, "no ping by default"
    assert main(), "main() should return something truthy"
  except ImportError:
    pass

# Generated at 2022-06-13 05:51:17.453901
# Unit test for function main
def test_main():
    from ansible.modules.ping import main
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.dict_transformations import deep_diff
    from ansible.module_utils.arguments import ModuleArgsParser
    import json

    # Test with no differences
    req_args = dict(
        data=dict(type='str', default='pong'),
    )
    m = AnsibleModule(argument_spec=req_args, supports_check_mode=True)
    m.exit_json = lambda **kwargs: kwargs.update(changed=True) or kwargs
    main()

    assert m.exit_json.called
    assert len(m.exit_json.call_args) == 1

# Generated at 2022-06-13 05:51:25.089295
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    try:
        if module.params['data'] == 'crash':
            raise Exception("boom")

        result = dict(
            ping=module.params['data'],
        )

        module.exit_json(**result)
    except Exception as e:
        assert e == 'boom'

# Generated at 2022-06-13 05:51:31.821395
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        )
    )
    result = main()
    print (result)
    assert module.params['data'] == 'pong'
    assert result.get('ping') == 'pong'
    assert result.get('changed') == False

# Generated at 2022-06-13 05:51:37.876939
# Unit test for function main
def test_main():
    content = dict(
        data=dict(default='pong', type='str')
    )
    result = dict(
        ping='pong'
    )

    test = AnsibleModule(
        argument_spec=content,
        supports_check_mode=True
    )

    assert test.exit_json(**result) == dict(
        ansible_facts=dict(ping='pong'),
        changed=False,
        skipped=False,
        verbose_override=False,
        blackout=None,
        ignored_errno=[],
        rc=0
    )

# Generated at 2022-06-13 05:51:38.778261
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:51:41.145274
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))

    try:
        main()
        assert True == False
    except SystemExit as e:
        assert e.code == 0
    except:
        assert True == False


# Generated at 2022-06-13 05:51:51.504081
# Unit test for function main
def test_main():
    def test_module():
        test_params = {
            'data': 'pong'
        }
        ansible_args = dict(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )
        test_module = AnsibleModule(**ansible_args)
        test_module.params = test_params
        return test_module

    def test_result():
        return dict(
            ping='pong'
        )

    test_module = test_module()


# Generated at 2022-06-13 05:51:59.586009
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils.basic import AnsibleModule, AnsibleExitJson, AnsibleFailJson, set_module_args
    set_module_args(dict(data='pong'))
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    try:
        main()
    except SystemExit as e:
        sys.exit(e)
    except Exception as e:
        module.fail_json(msg=repr(e))
    assert module.exit_json.call_count == 1
    assert module.exit_json.call_args[0][0]['ping'] == 'pong'


# Generated at 2022-06-13 05:52:20.601291
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # set module args
    module.params['data'] = 'crash'

    # execute the main function
    main()


# Generated at 2022-06-13 05:52:27.815795
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

test_main()

# Generated at 2022-06-13 05:52:38.409486
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    import ansible.module_utils.argspec
    import ansible.module_utils.netcommon
    from ansible.compat.tests.mock import patch,MagicMock
    import ansible.utils
    from ansible.utils.collection_loader.yaml_collection_loader import get_collection_loader
    import tempfile
    import json
    import sys
    import os

    # Get a filename of an existing file (created by py.test) so we can extract the directory it is in
    existing_file = os.path.realpath(__file__)
    temp_dir = os.path.dirname(existing_file)

    # Create a tmp python file
    (tmp_fd, tmp_path) = tempfile.mkstemp(dir=temp_dir, suffix=".py")

# Generated at 2022-06-13 05:52:41.389087
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
            debug=dict(type='bool', default=False),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:52:45.521581
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.exit_json = basic.FakeAnsibleExitJson()
    main()
    res = module.exit_json
    assert res.get('ping') == 'pong'

# Unit test 2 for function main

# Generated at 2022-06-13 05:52:46.061262
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:52:50.955426
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import ImmutableDict
    argument_spec = dict(data=dict(type='str', default='pong'))
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )
    # Check that check_mode is True
    assert module.check_mode is True

    # Check that diff_mode is False
    assert module.diff_mode is False

    # Check that fail_json is a function
    assert callable(module.fail_json)

    # Check that exit_json is a function
    assert callable(module.exit_json)

    # Check that all module_args fields are correct
    assert module.module_args == argument_spec
    assert module.params == dict(data='pong')

    # Check that

# Generated at 2022-06-13 05:52:51.338139
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:52:58.237129
# Unit test for function main
def test_main():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=module.params['data'],
    )

    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:53:02.761997
# Unit test for function main
def test_main():
    # Test return value is correct
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == dict(
        ping=module.params['data'],
    )

# Generated at 2022-06-13 05:53:36.044437
# Unit test for function main
def test_main():
    with pytest.raises(Exception) as excinfo:
        main()
        print(excinfo)
    assert excinfo.type == Exception
    assert str(excinfo.value) == "boom"

# Generated at 2022-06-13 05:53:41.254001
# Unit test for function main
def test_main():
    # Construct the module object
    argument_spec = { 'data': { 'type': 'str', 'default': 'pong' } }
    metadata = { 'check_mode': True }
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True, metadata=metadata)

    # Mock the function function that runs during invokation which will be called during AnsibleModule.exit_json()
    # In this file this function is named 'main()'
    def mock_exit_json(self, **kwargs):
        pass
    AnsibleModule.exit_json = mock_exit_json

    # Call the function that needs to be unit tested, function named 'main()'
    main()

# Generated at 2022-06-13 05:53:47.937363
# Unit test for function main
def test_main():
    args = dict(
        data='pong',
    )

    result = dict(
        ping='pong',
        changed=False
    )

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    module.params = args

    assert module.params == args
    assert result == main()

# Generated at 2022-06-13 05:53:50.286417
# Unit test for function main
def test_main():
    with pytest.raises(Exception) as e_info:
        main()
    assert "boom" == e_info.value.args[0]

# Generated at 2022-06-13 05:53:51.199603
# Unit test for function main
def test_main():
    assert main().get('ping') == 'pong'

# Generated at 2022-06-13 05:53:53.907092
# Unit test for function main
def test_main():
    test_argv = ['--check']
    test_argv.extend('-a "data=testdata"')
    result = main().params
    assert result['ping'] == 'testdata'

# Generated at 2022-06-13 05:54:00.462836
# Unit test for function main
def test_main():
    # This test uses the built-in ping module to get data to test the
    # _make_invocation_command function.
    import os
    import sys
    import json
    import subprocess
    from ansible.module_utils.basic import AnsibleModule

    # Setup the data we need to run the module.
    data = 'crash'
    expected_results = None
    expected_return_code = 1
    test_result = {}
    # args = "ansible/modules/system/ping.py"
    args = ["ansible/modules/system/ping.py", "data=" + data]
    os_environ = os.environ.copy()
    # Execute the module code and capture its output.

# Generated at 2022-06-13 05:54:03.200476
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

    result = {
        'ping': module.params['data'],
    }

    module.exit_json(**result)


# Generated at 2022-06-13 05:54:08.883912
# Unit test for function main
def test_main():
    import os
    import sys
    try:
        import json
    except ImportError:
        import simplejson as json
    import sys
    import argparse

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
    test_main()

# Generated at 2022-06-13 05:54:16.368423
# Unit test for function main
def test_main():
    # Test with no argument
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'
    # Test with crash argument
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='crash'),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'crash'
    # Test with foo argument
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='foo'),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'foo'

# Generated at 2022-06-13 05:55:36.143885
# Unit test for function main
def test_main():
    assert main() == None


# Generated at 2022-06-13 05:55:37.717776
# Unit test for function main
def test_main():
    response = main()
    # Test response
    assert response == None

# Generated at 2022-06-13 05:55:45.934219
# Unit test for function main
def test_main():
    ansible_options = {}
    # Extra arguments to pass to ansible-playbook
    ansible_options['extra_vars'] = []
    # If you have a custom ansible.cfg file, specify it here
    ansible_options['ansible_config'] = None
    # If you want to run as a different user, specify it here
    ansible_options['remote_user'] = None
    # A list of hosts to run on
    ansible_options['hosts'] = []
    # The path to a playbook
    ansible_options['playbook'] = None
    # curl or socks proxy to use
    ansible_options['curl_proxy'] = None
    # The path to a private key file
    ansible_options['private'] = None
    # A list of arguments to pass directly to ansible
    ansible_options

# Generated at 2022-06-13 05:55:46.686836
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:55:50.071467
# Unit test for function main
def test_main():
    attrs = {}
    args = {'data': 'pong'}
    result = main(attrs, args)
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:55:58.284571
# Unit test for function main
def test_main():
    # Execute the following with: 'nosetests test_ping.py -s' so you can see the output
    print('--- Running main()')
    connection_args = dict()
    module_args = dict(data=dict(type='str', default='pong'))
    m = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    result = dict(
        ping=m.params['data'],
    )
    print('--- Result:', result)
    assert result == dict(ping='pong')

# Generated at 2022-06-13 05:56:09.770568
# Unit test for function main
def test_main():
    import random
    import string

    # We don't have pytest for this module so we have to implement our own unit tests
    # In order to not have to have a ton of boilerplate, we just make sure the function
    # calls we care about actually happen.  There's not a lot of logic here so this will do.
    class FakeModule:
        check_mode = None
        params = None
        exit_json = None
        fail_json = None

        def __init__(self):
            self.params = dict()

        def exit_json(self, **kwargs):
            if self.exit_json:
                self.exit_json(kwargs)

        def fail_json(self, **kwargs):
            if self.fail_json:
                self.fail_json(kwargs)


# Generated at 2022-06-13 05:56:21.800887
# Unit test for function main
def test_main():
    # Case 1
    with patch.object(ansible.module_utils.basic, 'AnsibleModule') as mock_module, patch.object(main, 'Exception') as mock_exception, patch.object(ansible.module_utils.basic, 'exit_json') as mock_exit_json, patch.object(ansible.module_utils.basic, 'fail_json') as mock_fail_json, patch.object(ansible.module_utils.basic, 'run_command') as mock_run_command:
        mock_module.return_value = MainTestClass()
        mock_MainTestClass = mock_module.return_value
        mock_MainTestClass.params.return_value = {'data': 'crash'}

# Generated at 2022-06-13 05:56:30.494135
# Unit test for function main
def test_main():
    import tempfile, os
    from ansible.module_utils.basic import AnsibleModule
    from sys import version_info

    # AnsibleModule is defined in ansible.module_utils.basic and we
    # can't mock it's import in our test environment so we work
    # around it here.
    if version_info[0] < 3:
        import __builtin__ as builtins  # pylint: disable=import-error
        builtins.__dict__['AnsibleModule'] = AnsibleModule

        # StringIO is also defined in module_utils so we have to do a similar
        # workaround.
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO
    else:
        import builtins
        builtins.__dict__['AnsibleModule'] = Ansible

# Generated at 2022-06-13 05:56:33.479793
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    with pytest.raises(Exception) as e:
        main()
    assert e.match("boom")