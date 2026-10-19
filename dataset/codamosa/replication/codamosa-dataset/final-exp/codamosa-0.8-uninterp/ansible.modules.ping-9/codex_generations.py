

# Generated at 2022-06-13 05:49:05.384618
# Unit test for function main
def test_main():

    # import module snippets
    from ansible.module_utils.basic import AnsibleModule

    # Set up arguments
    argument_spec = dict (
        data = dict(default = 'pong', type = str)
    )

    # Set up test result
    result = dict(
        changed = False,
        ping = 'pong'
    )

    # Instantiate module
    m = AnsibleModule(argument_spec, supports_check_mode = True)

    # Execute function
    main()

    # Run tests
    module.exit_json(**result)

# Generated at 2022-06-13 05:49:06.489488
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as e:
        print(e)

# Generated at 2022-06-13 05:49:10.891186
# Unit test for function main
def test_main():
    # Test arguments
    args = dict(
        data='pong',
    )
    args['checkmode'] = False
    args['_ansible_diff'] = False

    # Return value
    retval = dict(
        ping='pong',
    )

    # Test case for the main function
    # Copy the arguments to a dict to prevent modifying the args dict
    args_copy = dict(args)
    retval_copy = dict(retval)
    test_args = args_copy
    test_retval = retval_copy
    result = main(**test_args)
    assert result == test_retval
