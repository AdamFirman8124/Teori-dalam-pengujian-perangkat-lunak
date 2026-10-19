

# Generated at 2022-06-13 05:49:00.798338
# Unit test for function main
def test_main():
    assert callable(main)
    assert isinstance(main(), AnsibleModule)
    assert isinstance(main().params, dict)

# Generated at 2022-06-13 05:49:06.131548
# Unit test for function main
def test_main():
    with patch('ansible_collections.ansible.builtin.plugins.modules.ping.AnsibleModule') as mock_AnsibleModule:
        mock_AnsibleModule.return_value.params = {'data': 'pong'}
        mock_AnsibleModule.return_value.exit_json.return_value = None
        mock_AnsibleModule.return_value.fail_json.return_value = None
        result = main()
        assert result == {"changed": False, "ping": "pong"}

# Generated at 2022-06-13 05:49:11.480693
# Unit test for function main
def test_main():
    # Setup the stubs
    f_module = {}
    f_module['argument_spec'] = {'data': {'type': 'str', 'default': 'pong'}}
    f_module['params'] = {'data': 'pong'}
    f_module['check_mode'] = True

    from ansible.module_utils.basic import AnsibleModule
    f_AnsibleModule = AnsibleModule
    AnsibleModule = MagicMock(return_value=f_module)

    # Execute the function
    main()

    # Check the results
    AnsibleModule.assert_called_with(check_mode=True, argument_spec={'data': {'type': 'str', 'default': 'pong'}})
    f_module['exit_json'].assert_called_with(ping='pong')



# Generated at 2022-06-13 05:49:21.033924
# Unit test for function main
def test_main():
    """
    Unit tests for function main
    """

    # Construct test data
    test_args = []
    test_kwargs = {
        'data': 'pong',
    }

    # Construct actual return data
    actual_return = {
        'ping': 'pong',
        'changed': False,
        'ansible_facts': {},
        'invocation': {
            'module_args': test_kwargs,
        },
        '_ansible_no_log': False,
    }

    # Test function
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    actual_return = main(module, *test_args, **test_kwargs)
    assert actual