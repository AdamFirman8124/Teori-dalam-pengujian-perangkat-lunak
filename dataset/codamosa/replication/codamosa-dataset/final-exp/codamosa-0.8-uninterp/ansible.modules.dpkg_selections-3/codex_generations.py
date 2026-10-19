

# Generated at 2022-06-13 05:13:02.164163
# Unit test for function main
def test_main():
    print("running unit tests for function main")
    assert True

# Generated at 2022-06-13 05:13:11.064821
# Unit test for function main
def test_main():
    # Test with pre-existing selection
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    setattr(module, 'run_command', lambda *args, **kwargs: (0, 'something install', ''))
    setattr(module, 'check_mode', False)
    setattr(module, '_diff', False)

    main()

    assert module.params['name'] == 'something'
    assert module.params['selection'] == 'install'
    assert module.check_mode == False
    assert module._diff == False

    # Test with non pre-existing selection
    module = AnsibleModule

# Generated at 2022-06-13 05:13:21.997423
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:13:28.300136
# Unit test for function main
def test_main():
  ansible_options = {'name': 'test-package', 'selection': 'deinstall'}
  module = AnsibleModule(
    argument_spec={
      'name': dict(required=True),
      'selection': dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    },
    supports_check_mode=True
  )
  module.params = ansible_options
  main()


# Generated at 2022-06-13 05:13:28.855570
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:13:29.400209
# Unit test for function main
def test_main():
    assert(main())

# Generated at 2022-06-13 05:13:32.766082
# Unit test for function main
def test_main():
    my_file = open('./../tests/dpkg_selections/test_dpkg_selections', "r")
    args = dict(
        selection='hold',
        name='python'
    )
    rc, out, err = main(args)
    assert err == my_file.readline()

# Generated at 2022-06-13 05:13:43.183567
# Unit test for function main
def test_main():
    import os
    import unittest
    import tempfile
    import sys

    # Prepare environment
    os.environ['DPKG_MAINTSCRIPT_PACKAGE'] = 'ansible'
    os.environ['DPKG_MAINTSCRIPT_NAME'] = 'ansible-prerm'

    # Prepare fake module
    module = AnsibleModule(
        argument_spec={
            'name': {'required': True},
        },
        supports_check_mode=True
    )
    module.exit_json = lambda x: None
    module.fail_json = lambda x: None
    module.get_bin_path = lambda x, y: '/bin/' + x
    module.run_command = lambda x, y: [0, '', '']

    # Execute main()
    main()



# Generated at 2022-06-13 05:13:54.644951
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    orig_run_command = AnsibleModule.run_command

    rc = (0, 'install', '')
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            state=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        )
    )
    module.run_command = lambda *args, **kwargs: rc

    module.run_command = lambda *args, **kwargs: (0, 'cc', '')

    rc = (0, 'hold', '')
    module.run_command = lambda *args, **kwargs: rc

    rc = (0, 'cc', '')

# Generated at 2022-06-13 05:14:01.402402
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

# Generated at 2022-06-13 05:14:30.384915
# Unit test for function main
def test_main():
    cmd = ['python', 'apt_key.py']

# Generated at 2022-06-13 05:14:31.212731
# Unit test for function main
def test_main():
    assert main() == True


# Generated at 2022-06-13 05:14:33.609891
# Unit test for function main
def test_main():
    print("Calling main...")
    main()
    print("Finished main")

# Generated at 2022-06-13 05:14:43.917705
# Unit test for function main
def test_main():
    fake_module = SimpleNamespace(params=dict(name='python', selection='hold'))

    # default state of the module is changed == False
    # module.exit_json(changed=changed, before=current, after=selection)
    assert main(fake_module) == dict(changed=False, before='not present', after='hold')

    # Check if module.check_mode or not changed
    fake_module.check_mode = True
    assert main(fake_module) == dict(changed=False, before='not present', after='hold')
    fake_module.check_mode = False
    fake_module.params['selection'] = 'not present'
    assert main(fake_module) == dict(changed=False, before='not present', after='not present')

    # module.run_command([dpkg, '--set-selections

# Generated at 2022-06-13 05:14:58.201437
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)

    run_command_args = {'rc': rc, 'out': out, 'err':err, 'check_rc': True}

    dpkg_set_selections_data = "%s %s" % (name, selection)


# Generated at 2022-06-13 05:15:04.784377
# Unit test for function main
def test_main():
        dpkg = "/usr/bin/dpkg"
        selection = "not present"
        current = "install"
        out = "python not present"
        err = None
        rc = 0

        _mock_run_command = mock.Mock(return_value=(rc,out,err))
        _mock_exit_json = mock.Mock(return_value=None)
        _mock_module = mock.Mock(exit_json=_mock_exit_json,get_bin_path=dpkg,run_command=_mock_run_command)
        _mock_exit_json = mock.Mock(return_value=None)

        with mock.patch.object(main,'module',_mock_module):
             main()

# Generated at 2022-06-13 05:15:17.134646
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:15:24.717269
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'

    def run_command(args, data):
        assert args == ['/usr/bin/dpkg', '--set-selections']
        assert data == "python hold"
        return 0, "", ""

    module = MagicMock(params={'name': name, 'selection': selection})
    module.get_bin_path.return_value = '/usr/bin/dpkg'
    module.run_command.side_effect = run_command
    main()

# Generated at 2022-06-13 05:15:26.102935
# Unit test for function main
def test_main():
    name = 'vim'
    selection = 'hold'

    main(name, selection)

# Generated at 2022-06-13 05:15:32.391868
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    print(module.check_mode)

# Test run
test_main()

# Generated at 2022-06-13 05:16:02.550084
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    main()


# Generated at 2022-06-13 05:16:12.751849
# Unit test for function main
def test_main():
    dpkg = '/usr/bin/dpkg'
    name = 'python'
    selection = 'hold'
    data = "%s %s" % (name, selection)

    current = 'hold'

    class Module(object):
        class RunCommand(object):
            def __new__(cls, *args,**kwargs):
                if args[1][2] == name:
                    return [0, current, '']
                else:
                    return [0, "", ""]
        def __init__(self, *args, **kwargs):
            self.changed = True
            self.params = {'name':name, 'selection':selection}
            self.runner = self.RunCommand()
        def exit_json(self, *args, **kwargs):
            self.args = args
            self.kwargs = kw

# Generated at 2022-06-13 05:16:23.187282
# Unit test for function main
def test_main():
    test = {"name": "python", "selection": "hold" }
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'remove', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]
    changed = current != selection
    if module.check_mode or not changed:
        module.exit_json(changed=changed, before=current, after=selection)


# Generated at 2022-06-13 05:16:28.454376
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    import ansible.module_utils.action_plugins

    m = ansible.module_utils.basic.AnsibleModule(argument_spec={'name': {'required': True}, 'selection': {'required': True, 'choices': ['install', 'hold', 'deinstall', 'purge']}}, supports_check_mode=True)
    
    print(m.params)
    print(m.params['name'])
    print(m.params['selection'])

    #m.run_command([dpkg, '--get-selections', name], check_rc=True)

# Generated at 2022-06-13 05:16:32.753591
# Unit test for function main
def test_main():
    with patch("builtins.open", MagicMock(side_effect=[Exception("Boom!"), MagicMock(read_data='python install\n')])):
        assert main() == 1
    with patch("builtins.open", MagicMock(read_data='python install\n')):
        assert main() == 0

# Generated at 2022-06-13 05:16:43.372446
# Unit test for function main
def test_main():
    import codecs
    import os
    import re
    import tempfile
    test_file = tempfile.NamedTemporaryFile(mode='a', delete=False)
    test_file.write(codecs.BOM_UTF8)
    test_file.write(u'python\tinstall\n')
    test_file.close()
    args = dict(
        name='python',
        selection='hold',
        module_defaults=dict(bin_ansible_callbacks=True),
    )
    result = main(**args)
    assert type(result) == dict
    assert result['changed'] == True
    assert result['before'] == 'install'
    assert result['after'] == 'hold'