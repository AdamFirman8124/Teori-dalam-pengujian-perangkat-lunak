

# Generated at 2022-06-13 05:48:59.666781
# Unit test for function main
def test_main():
    print("Starting unit test for function main")
    main()

# Generated at 2022-06-13 05:49:04.298686
# Unit test for function main
def test_main():
    import json

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
        )

    # Test with no arguments provided
    res_args = dict(
       ping='pong',
    )

    res = module.from_json(main())
    assert res.to_dict() == res_args

# Generated at 2022-06-13 05:49:06.902923
# Unit test for function main
def test_main():
    # Test case
    contents = dict(
        data = 'pong'
    )

    # Results of the function
    results = main(contents)
    
    # Test that the results are correct
    assert results['ping'] == 'pong'

# Generated at 2022-06-13 05:49:10.854441
# Unit test for function main
def test_main():
    args = {'data': 'foo'}
    with patch.object(AnsibleModule, 'exit_json') as exit_mock:
        main()
        exit_mock.assert_called_once_with(
            changed=False,
            ping='foo'
        )

# Generated at 2022-06-13 05:49:13.821350
# Unit test for function main
def test_main():
    # Can't just use sys.argv because of windows
    args = [
        '',
        '{"data": "pong"}'
        ]
    assert main(args) == {'ping': 'pong'}

# Generated at 2022-06-13 05:49:19.624048
# Unit test for function main
def test_main():
    # load the module and the function
    from ansible.modules.cloud.amazon.ec2_scaling_policy import apply
    from ansible.modules.cloud.amazon.ec2_scaling_policy import refresh

    # create a namespace for the test data
    module_args = {}

    # call the function with the module_args and the regular fixtures
    result = main(module_args)

    # test the result ...
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:49:22.974916
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        )
    )
    test_module.exit_json(ping="pong")

# Generated at 2022-06-13 05:49:26.769314
# Unit test for function main
def test_main():
    args = dict(data="data_value")
    result = main(args)

    assert result["changed"] is False, "Didn't expect a change"
    assert result["ping"] == "data_value"


# Generated at 2022-06-13 05:49:27.440139
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:49:28.948069
# Unit test for function main
def test_main():
    assert callable(main)

# Unit tests for module ping.py

# Generated at 2022-06-13 05:49:37.974741
# Unit test for function main
def test_main():
    # Create save
    save = dict(
        ANSIBLE_MODULE_ARGS = dict(
            data='pong'
        ),
        ANSIBLE_CHECK_MODE = True
    )

    # Mocks
    class AnsibleModule_mock(object):
        def __init__(self):
            self.params = dict()

        def exit_json(self, **kwargs):
            save.update(kwargs)

    class ModuleExitException(Exception):
        pass

    setattr(AnsibleModule_mock, 'fail_json',
        lambda self, **kwargs: None)

# Generated at 2022-06-13 05:49:43.423364
# Unit test for function main
def test_main():
    # Make the module class we're using
    dummy_module = type('DummyModule', (object,), {
        'exit_json': lambda self, result: result,
        'fail_json': lambda self, msg: msg,
        'params': {'data': 'pong'},
        'check_mode': False
    })
    assert main() == {'ping': 'pong'}

# Generated at 2022-06-13 05:49:47.955764
# Unit test for function main
def test_main():
    args = [ ]
    # args = [ 'arg1', 'arg2' ]
    kwargs = { }
    # kwargs = { '_ansible_debug': True, '_ansible_verbose_always': True }
    ansible_main(args, kwargs)

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 05:49:49.608462
# Unit test for function main
def test_main():
    try:
        main()
    except:
        print("Some errors occurred")
        assert False
    assert True

# Generated at 2022-06-13 05:49:50.916531
# Unit test for function main
def test_main():
    a = {'changed': False, 'ping': 'pong'}
    assert a == main()

# Generated at 2022-06-13 05:49:55.495874
# Unit test for function main
def test_main():
    import os
    import sys
    import unittest

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    sys.modules['ansible'] = type('FakeAnsibleModule', (object,), {'AnsibleModule': module})
    
    import ansible.builtin.ping
    ansible.builtin.ping.main()
    result = dict(ping='pong')
    module.exit_json(**result)

test_main()

# Generated at 2022-06-13 05:50:03.742844
# Unit test for function main
def test_main():

    module_args = {}

    set_module_args(module_args)

    from ansible.modules.network.ping import main
    result = main()

    assert result
    assert result['ansible_facts']['ping'] == 'pong'

    set_module_args(dict(data='crash'))
    try:
        result = main()
    except Exception:
        pass
    else:
        assert False, "Expected Exception, but no exception was thrown"

# Generated at 2022-06-13 05:50:07.185085
# Unit test for function main
def test_main():
    assert main() is None

import os
import sys
import pytest
import tempfile

from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    import nose
    nose.runmodule()


# Generated at 2022-06-13 05:50:14.650613
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

# Generated at 2022-06-13 05:50:19.659293
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

    module.exit_json(**result)

# Generated at 2022-06-13 05:50:37.520995
# Unit test for function main
def test_main():
    import os, tempfile, shutil
    from ansible.module_utils.basic import AnsibleModule

    test_data = {
        'ping': 'pong'
    }

    test_dir = tempfile.mkdtemp()
    test_file = os.path.join(test_dir, 'test')

# Generated at 2022-06-13 05:50:48.988174
# Unit test for function main
def test_main():
    module = AnsibleModule({},{})
    module.exit_json = lambda a: sys.exit(a)
    mgr = module._manager
    endpoint = mgr._endpoint
    endpoint.safe = True
    endpoint.value = (0, {}, {}, [])

    with pytest.raises(SystemExit) as cm:
        main()
    assert cm.value.args == (0,)

    endpoint.value = (1, {}, {}, [])
    with pytest.raises(SystemExit) as cm:
        main()
    assert cm.value.args == (1,)

    endpoint.value = (1, {}, {}, [])
    module.params['data'] = 'crash'
    with pytest.raises(SystemExit) as cm:
        main()

# Generated at 2022-06-13 05:50:49.663111
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:50:55.675018
# Unit test for function main
def test_main():
    with patch.object(AnsibleModule, 'exit_json') as mock_exit_json:
        with patch.object(AnsibleModule, 'params', {'data': 'pong'}): 
            main()
    assert mock_exit_json.called_once
    assert mock_exit_json.call_args[0][0]['ping'] == 'pong'

# Generated at 2022-06-13 05:51:04.645047
# Unit test for function main
def test_main():
    import sys
    # Change the commandline args to only see the parameters we expect to see
    # Don't use the "data" parameter
    sys.argv = ['ansible-test', 'ping']

    from ansible.module_utils.basic import AnsibleModule
    from ansible_test._unittest.loader import ModuleLoader
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes

    # Create an empty module_loader to replace the one that is normally created
    # when calling AnsibleModule
    module_loader = ModuleLoader(None)

    # Create a module with the right import path
    # We use a StringIO object to make the module look like a file on disk
    # so we can create an AnsibleModule
    module_name = 'ansible.builtin.ping'

# Generated at 2022-06-13 05:51:08.419399
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    # Dummy arguments
    args = dict (
        data='pong'
    )

    # Dummy module
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # run test
    main()

# Generated at 2022-06-13 05:51:09.497736
# Unit test for function main
def test_main():
    main()


# Generated at 2022-06-13 05:51:17.035673
# Unit test for function main
def test_main():

    # Setup
    import ansible.module_utils.basic as basic
    m_basic = basic.AnsibleModule
    basic.AnsibleModule = mock_basic_AnsibleModule
    m_exit_json = basic.exit_json
    m_fail_json = basic.fail_json
    basic.exit_json = mock_exit_json
    basic.fail_json = mock_fail_json
    ansible_ping = __import__('ansible.modules.system.ping')
    #ansible_ping.main()
    basic.AnsibleModule = m_basic
    basic.exit_json = m_exit_json
    basic.fail_json = m_fail_json
    #assert False


# Generated at 2022-06-13 05:51:17.790259
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:51:21.863795
# Unit test for function main
def test_main():
    """
    Unit tests for main function
    """
    dict_args = dict(
        data={"default":"pong"}
    )
    main(dict_args)

# Generated at 2022-06-13 05:51:48.322049
# Unit test for function main
def test_main():
    with patch('ansible_collections.misc.not_a_real_collection.plugins.modules.ping.AnsibleModule') as mock_AnsibleModule, patch('ansible_collections.misc.not_a_real_collection.plugins.modules.ping.main') as mock_main:
        assert not mock_main.called
        assert not mock_AnsibleModule.called

        # Ensure we handle the exception
        with pytest.raises(Exception):
            with patch('ansible_collections.misc.not_a_real_collection.plugins.modules.ping.module.exit_json') as mock_exit_json:
                test_module_params = {'data': 'crash'}
                test_result = {'ping': 'crash'}
                mock_main.return_value = test_result
                mock_

# Generated at 2022-06-13 05:51:53.607935
# Unit test for function main
def test_main():
    import json
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    data = to_bytes(json.dumps({
        'ansible_facts': {'data': module.params['data']},
        'changed': False,
        'invocation': {
            'module_args': module.params
        }
    }))

    assert data == main()

# Generated at 2022-06-13 05:52:04.298725
# Unit test for function main
def test_main():
    # Mock module
    class MyModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, **kwargs):
            self.exit_args = kwargs
            return self.exit_args

        def exit_json(self, **kwargs):
            self.exit_args = kwargs
            return self.exit_args

    module = MyModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Success - Crash
    module.params['data'] = 'crash'
    try:
        main()
    except Exception:
        pass
    assert 'changed' in module.exit_args

# Generated at 2022-06-13 05:52:12.544900
# Unit test for function main
def test_main():
    import tempfile
    from ansible.module_utils.six import PY3

    if not PY3:
        module_path = tempfile.mkdtemp()
        module_args = dict(data='crash')
        raw_inp = dict(ANSIBLE_MODULE_ARGS=module_args)
        raw_inp.update(ANSIBLE_MODULE_CONSTANTS=dict())
        exec('import ansible.modules.ping as ping', raw_inp)
        exec('ansible.modules.ping.main()', raw_inp)
        assert 'msg' in raw_inp['ansible_module_results']
        assert 'Exception: boom' in raw_inp['ansible_module_results']['msg']

        module_args = dict(data='pong')

# Generated at 2022-06-13 05:52:17.998784
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong')
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'
    assert module.params['check_mode'] == True

# Generated at 2022-06-13 05:52:22.357446
# Unit test for function main
def test_main():
    # unit tests should be located in the same directory as the code they are testing
    # and be named as ...Test.py
    # there is a test skeleton class called AnsibleModuleTF that can be used as a base
    # for unit testing, see the comments in that class.
    pass

# Generated at 2022-06-13 05:52:24.218135
# Unit test for function main
def test_main():
    # Unit test for function main
    pass

# Generated at 2022-06-13 05:52:31.164216
# Unit test for function main
def test_main():
    print('Testing basic usage of main()')
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=False
    )
    result = dict(
        ping=module.params['data'],
    )
    assert result == dict(ping='pong')
    print('PASS')

# Generated at 2022-06-13 05:52:38.404403
# Unit test for function main
def test_main():
    """ Test module main """
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
    args = dict(
        data='crash',
    )
    import io
    from io import StringIO
    output = StringIO()
    module.fail_json_to_stdout(msg='This is expected to fail', **result)


# Generated at 2022-06-13 05:52:41.683353
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    
    assert module.params['data'] == 'pong'
    

# Generated at 2022-06-13 05:53:17.711261
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

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

    basic.exit_json(**result)

# Generated at 2022-06-13 05:53:19.898970
# Unit test for function main
def test_main():
    args = {}
    args['data'] = 'pong'
    result = main(args)
    assert (result == 'pong')

test_main()

# Generated at 2022-06-13 05:53:24.171710
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    module.check_mode = False
    result = main()
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:53:26.838365
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

# Generated at 2022-06-13 05:53:34.719268
# Unit test for function main
def test_main():
    module = AnsibleModule(
      argument_spec = dict(
        data = dict(type='str', default='pong')
      ),
      supports_check_mode=True
    )
    if module.check_mode:
        pass
    else:
        if module.params['data'] == 'crash':
          module.fail_json(msg="boom")
        module.exit_json(changed=False, ansible_facts=dict(ping=module.params['data']))


# Generated at 2022-06-13 05:53:35.525928
# Unit test for function main
def test_main():
    assert main()


# Generated at 2022-06-13 05:53:38.890293
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        )
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:53:49.474525
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        )
    )
    # Case 1: data = pong
    result = main()
    assert result['ping'] == "pong"
    # Case 2: data = crash
    module.params['data'] = 'crash'
    try:
      result = main()
    except:
      assert True
    # Case 3: data = ping
    module.params['data'] = 'ping'
    result = main()
    assert result['ping'] == "ping"
    # Case 4:
    assert result['msg'] == "pong"
    # Case 5:
    assert result['status'] == "success"

# Generated at 2022-06-13 05:53:51.472055
# Unit test for function main
def test_main():
    o = {
        'changed': False,
        'ping': 'pong'
    }
    assert main() == o


# Generated at 2022-06-13 05:53:56.438609
# Unit test for function main
def test_main():
    ping_data = {
        'ping': 'pong',
    }

    def fake_exit_json(**kwargs):
        # return args
        return kwargs

    # Overriding exit_json to test the function
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.exit_json = fake_exit_json

    # Invoking the function
    result = main()

    assert result == ping_data

# Test crash scenario

# Generated at 2022-06-13 05:55:25.131474
# Unit test for function main
def test_main():
    import collections
    import unittest

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught by the test case"""
        pass
    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught by the test case"""
        pass

    # This class contains the common code needed to interact with Ansible
    # modules. It is instantiated by the TestAnsibleModule class.
    class AnsibleModuleCoordinator(object):
        """Encapsulates common code needed to interact with ansible modules. This class is instantiated by the TestAnsibleModule class"""
        def __init__(self, module_name, module_args, module_kwargs):
            self.result = collections.defaultdict(lambda: 'unknown')
            self.exit_json

# Generated at 2022-06-13 05:55:29.834330
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type="str", default='pong')
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'


# Generated at 2022-06-13 05:55:30.690999
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:55:31.660971
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:55:37.611263
# Unit test for function main
def test_main():
    import json
    from ansible.module_utils.basic import AnsibleModule

    args = dict(
        data="test"
    )
    AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    ).exit_json(**args)
    assert True == True

# Generated at 2022-06-13 05:55:39.551883
# Unit test for function main
def test_main():
    module = AnsibleModule({}, {})
    result = main()
    assert result.data['ping'] == 'pong'

# Generated at 2022-06-13 05:55:41.328584
# Unit test for function main
def test_main():
    test_args = {
        'data': 'foo',
    }

    main()

# Generated at 2022-06-13 05:55:53.891278
# Unit test for function main
def test_main():
    import os
    import pytest
    import sys

    if sys.version_info < (2, 7):
        pytest.skip("This ansible module requires Python 2.7 or higher")

    # This is the mock ansible module

# Generated at 2022-06-13 05:56:00.953643
# Unit test for function main
def test_main():
    import ansible.module_utils.basic as basic_module

    module = basic_module.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # test when argument is set to crash
    module.params['data'] = 'crash'
    with basic_module.AssertionError:
        main()

    # test when argument is set to pong
    module.params['data'] = 'pong'
    main()

# Generated at 2022-06-13 05:56:02.804610
# Unit test for function main
def test_main():
    '''
    unit test for the function main()
    '''
    assert(main() == 0)

# Generated at 2022-06-13 05:58:49.327843
# Unit test for function main
def test_main():
    # Validate args
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:58:55.562480
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleFail, AnsibleExitJson, AnsibleExitSkipped
    import pytest
    assert AnsibleFail
    assert AnsibleExitJson
    assert AnsibleExitSkipped

    import ansible.module_utils.ping as ping
    from ansible.module_utils.ansible_release import __version__

    args = dict(
        data='ping',
        ansible_version='2.7.10',
    )

    module = ping.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert AnsibleFail is ping.AnsibleFail
    assert AnsibleExitJson is ping.AnsibleExitJson
    assert AnsibleExitSkipped