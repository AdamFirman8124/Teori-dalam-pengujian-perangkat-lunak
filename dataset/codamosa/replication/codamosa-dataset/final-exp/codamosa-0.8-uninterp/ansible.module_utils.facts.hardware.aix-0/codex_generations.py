

# Generated at 2022-06-13 00:35:02.403076
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    cpu_facts = AIXHardware().get_cpu_facts()
    assert cpu_facts["processor"]
    assert cpu_facts["processor_count"] == 1
    assert cpu_facts["processor_cores"] == 2



# Generated at 2022-06-13 00:35:12.250958
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():

    module = AnsibleModule(argument_spec={})
    module.params = {}
    hardware_collector = AIXHardwareCollector(module=module)
    aix_hardware = hardware_collector.collect(module=module)[0]

    cpu_facts = aix_hardware.get_cpu_facts()

    assert cpu_facts is not None
    assert cpu_facts['processor_count'] is not None
    assert cpu_facts['processor'] is not None
    assert cpu_facts['processor_cores'] is not None

    # Unit test for method get_memory_facts of class AIXHardware
    def test_AIXHardware_get_memory_facts():
        module = AnsibleModule(argument_spec={})
        module.params = {}
        hardware_collector = AIXHardwareCollector(module=module)
        aix_

# Generated at 2022-06-13 00:35:20.593591
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    aix_hardware = AIXHardware()

# Generated at 2022-06-13 00:35:30.482018
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    hardware = AIXHardware({'module_setup': True,
                            'bin_dir': '.',
                            'command_timeout': 60,
                            'remote_tmp': '/tmp'})

    devices = hardware.get_device_facts()
    assert devices['devices']
    assert isinstance(devices['devices'], dict)
    devices_keys = devices['devices'].keys()

    # Fake devices list

# Generated at 2022-06-13 00:35:32.041632
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    aix_hardware_obj = AIXHardware()
    aix_hardware_obj.get_mount_facts()

# Generated at 2022-06-13 00:35:35.750228
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    hw = AIXHardware(module)
    hw.populate()
    module.exit_json(changed=False)


# Generated at 2022-06-13 00:35:43.807428
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    m = AIXHardware() 
    vgs_path = '/usr/bin/vgs.txt'
    try:
        with open(vgs_path) as vgs_file: 
            vgs_facts = m.get_vgs_facts(vgs_file.read())
    except IOError as e:
        print("{0}{1}".format(e.strerror, e.filename))


# Generated at 2022-06-13 00:35:56.637363
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec = dict()
    )

    module.run_command = Mock(return_value=(0, open(get_fixture_path('devices'), 'r').read(), ''))

    hardware = AIXHardware(module)

    devices = hardware.get_device_facts()


# Generated at 2022-06-13 00:36:03.044837
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    mod = type('AnsibleModule', (object,), {})
    setattr(mod, 'run_command', lambda x_: (0, '', ''))
    setattr(mod, 'get_bin_path', lambda x, required=False: 'bin/path')
    hw_collector = AIXHardwareCollector(module=mod)
    assert hw_collector._platform == 'AIX'
    assert hw_collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:36:05.402098
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    facts_collector = AIXHardwareCollector()
    assert facts_collector._platform == 'AIX'
    assert facts_collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:36:31.912031
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})

    hardware_collector = AIXHardwareCollector(module=module)
    hardware = AIXHardware(module)
    hardware_collector.collect(hardware, module)

    assert hardware.memfree_mb == hardware_collector.facts['ansible_memfree_mb']
    assert hardware.memtotal_mb == hardware_collector.facts['ansible_memtotal_mb']
    assert hardware.swapfree_mb == hardware_collector.facts['ansible_swapfree_mb']
    assert hardware.swaptotal_mb == hardware_collector.facts['ansible_swaptotal_mb']
    assert hardware.processor == hardware_collector.facts['ansible_processor']

# Generated at 2022-06-13 00:36:40.150409
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    """Unit test for method get_mount_facts of class AIXHardware"""

    class TestModule:
        def __init__(self, module_name, bin_path):
            self.module_name = module_name
            self.bin_path = bin_path

        def get_bin_path(self, arg, required=False):
            return self.bin_path


# Generated at 2022-06-13 00:36:52.675857
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    ''' Method: get_device_facts of class AIXHardware '''
    # Populate constants from json file

    # Populate test with constants from json file

# Generated at 2022-06-13 00:36:54.357415
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw = AIXHardwareCollector()
    assert hw._platform == "AIX"
    assert isinstance(hw._fact_class, AIXHardware)

# Generated at 2022-06-13 00:37:00.704359
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    collected_facts = {'ansible_mounts': []}
    module = FakeAnsibleModule(
        collected_facts=collected_facts,
    )
    hardware = AIXHardware(module)
    vgs_facts = hardware.get_vgs_facts()
    assert vgs_facts['vgs']['testvg'][0]['pv_name'] == 'hdisk105'
    assert vgs_facts['vgs']['rootvg'][0]['pp_size'] == '4 megabyte(s)'
    assert vgs_facts['vgs']['rootvg'][1]['pv_state'] == 'active'



# Generated at 2022-06-13 00:37:11.415147
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module_args = dict()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # not validating here.  Validation of data being returned is being done with assert statements below

    # create an AIXHardware object with the content
    # (first 20 lines only) from file module_utils/facts/hardware/aix/lsvg.out
    hardware = AIXHardware(module=module)

    # get vg and pv facts
    vgs_facts = hardware.get_vgs_facts()

    #
    # test results to make sure they are correct
    #
    # vgs_facts should be a dict with only one key: vgs
    assert len(vgs_facts) == 1
    assert 'vgs' in vgs_facts

    # key 'vgs' in v

# Generated at 2022-06-13 00:37:20.656669
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list'))
    )

    # Set up a class object.
    hw_obj = AIXHardware(module)

    hw_obj.populate()
    assert hw_obj.facts['processor'] == 'PowerPC_POWER8'
    assert hw_obj.facts['processor_count'] == 2
    assert hw_obj.facts['processor_cores'] == 8
    assert hw_obj.facts['memtotal_mb'] == 262496
    assert hw_obj.facts['swaptotal_mb'] == 314368
    assert hw_obj.facts['firmware_version'] == 'IBM,AXX150A0'

# Generated at 2022-06-13 00:37:29.379090
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(dict(
        ansible_facts=dict(
            devices=dict(
                devices=dict(
                    device_name_1=dict(
                        name='device_name_1',
                        attributes=dict(
                            attribute1='value1',
                            attribute2='value2'
                        ),
                        state='State',
                        type='type'
                    )
                )
            )
        )
    ))

    ah = AIXHardware(module)

    assert ah.get_device_facts() == module.ansible_facts['devices']

# Generated at 2022-06-13 00:37:40.469493
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    """
    Return valid values for AIX-specific dmi facts.
    """
    h = AIXHardware()

    # Test using the /usr/bin/lsconf output from an IBM POWER7 system.
    lsconf_path = '/usr/bin/lsconf'

# Generated at 2022-06-13 00:37:43.392184
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector is not None
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:38:11.964798
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    a = AIXHardware()
    a.module = DummyAnsibleModule()
    cmd = "/usr/sbin/lsattr -El sys0 -a fwversion"
    a.module.run_command.return_value = (0, 'IBM,AIX 7.2', '')
    facts = a.get_dmi_facts()
    a.module.run_command.assert_called_with(cmd)
    assert facts == {'firmware_version': 'AIX 7.2'}


# Generated at 2022-06-13 00:38:23.199560
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True)

    if not HAS_AIX_UTILS:
        module.fail_json(msg=missing_required_lib('aix utilities'))

    hardware_collector = AIXHardwareCollector(module=module)
    hardware_fact = hardware_collector.collect()[0]
    populate = hardware_fact.populate()
    parent_class_populate = hardware_fact.__class__.__base__.populate(hardware_fact)
    populate.pop('devices')
    parent_class_populate.pop('devices')
    assert populate == parent_class_populate



# Generated at 2022-06-13 00:38:34.968861
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module_mock = Mock()

# Generated at 2022-06-13 00:38:43.137957
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    import sys
    # needed for "lsdev" test
    sys.modules['ansible'] = type('mod', (), {'__file__': '/'})


# Generated at 2022-06-13 00:38:49.954048
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    # Create the mock module
    module = AnsibleModule(argument_spec={})
    module.params = {
        'name': 'Test',
        'state': 'present',
        'user': None,
        'password': None,
        'server': None,
        'force': False
    }
    hardware_object = AIXHardware(module=module)
    # Set the mock command outputs
    hardware_object.module.run_command.return_value = (
        0, '', '')
    hardware_object.module.get_bin_path.return_value = '/usr/sbin/mount'

    # Test the method
    result = hardware_object.get_mount_facts()
    # Check the results
    assert result == {'mounts': []}

# Generated at 2022-06-13 00:38:57.751091
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts import hardware as hardware_module
    module = hardware_module.Hardware()
    aix_hardware = AIXHardware(module)

    vgs_facts = aix_hardware.get_vgs_facts()

    assert vgs_facts['vgs']['rootvg'] == [{'pv_name': 'hdisk0', 'pv_state': 'active',
                                           'total_pps': '546', 'free_pps': '0', 'pp_size': '4 megabyte(s)'}]

# Generated at 2022-06-13 00:39:10.683295
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:39:14.415220
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 00:39:20.620658
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    if not HAS_AIX_MODULES:
        module.fail_json(msg=missing_required_lib('aix_modules'))

    result = {'changed': False}  # default
    hardware = AIXHardware(module)

    # run test
    result.update(hardware.get_vgs_facts())

    # exit
    module.exit_json(**result)



# Generated at 2022-06-13 00:39:31.421514
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    import sys
    import tempfile
    try:
        module = sys.modules['ansible.module_utils.facts.hardware.aix']
    except KeyError:
        raise Exception('Cannot find ansible.module_utils.facts.hardware.aix module')
    # Which file to use for lsconf?
    #
    lsconf_file_name = '/tmp/lsconf.out'

    # Make fake lsconf output
    #
    lsconf_out = """
System Model: IBM,9117-570
Machine Serial Number: 00FGE23
LPAR Info: 1 10

System Model: IBM,9117-570
Machine Serial Number: 00FGE23
LPAR Info: 1 10
"""

# Generated at 2022-06-13 00:39:57.762668
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    AIXHardwareCollector()

# Generated at 2022-06-13 00:40:06.537793
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={}
    )
    hardware = AIXHardware(module)


# Generated at 2022-06-13 00:40:07.982396
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)
    hardware_facts = hardware.populate()
    assert hardware_facts is not None


# Generated at 2022-06-13 00:40:13.120811
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module=module)
    hardware_facts = hardware.get_memory_facts()
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['memfree_mb']
    assert hardware_facts['swapfree_mb']
    assert hardware_facts['swaptotal_mb']

# Test case to include the tests framework

# Generated at 2022-06-13 00:40:18.758145
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModuleMock()
    cmds = [['/usr/bin/vmstat', '-v'], ['/usr/sbin/lsps', '-s']]

    hw = AIXHardware(module)
    assert hw.get_memory_facts() == {'swapfree_mb': 858, 'swaptotal_mb': 1048, 'memfree_mb': 1060, 'memtotal_mb': 3204}
    module.run_command.assert_has_calls([call(cmds[0]), call(cmds[1])], any_order=True)


# Generated at 2022-06-13 00:40:29.622841
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    import sys
    import os
    import unittest
    import ansible.module_utils.facts.hardware.aix as aix_hw

    # construct a mock class with the same name as the module we're testing
    # because aix_hw.AIXHardware is imported dynamically by AIXHardwareCollector
    # and if we don't mock the class, unittest.mock.patch won't work.
    class_name = 'ansible.module_utils.facts.hardware.aix.AIXHardware'
    if sys.version_info[0] == 2:
        mock_class = type(str(class_name), (object,), {})
    else:
        mock_class = type(class_name, (object,), {})

    hw = mock_class()

    # Mock the run_command method of the

# Generated at 2022-06-13 00:40:40.717534
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    fact_module = AnsibleModuleFake({})
    fact_module.run_command = run_command_fake
    hardware_fact = AIXHardware(fact_module)

    # Test for no vg
    vgs_facts = hardware_fact.get_vgs_facts()
    assert 'vgs' not in vgs_facts

    # Test for empty vg
    vgs_facts = hardware_fact.get_vgs_facts()
    assert 'vgs' in vgs_facts
    assert 'testvg' in vgs_facts['vgs']
    assert vgs_facts['vgs']['testvg'] == []

    # Test for vg with 1 pv
    vgs_facts = hardware_fact.get_vgs_facts()
    assert 'vgs' in vgs_facts

# Generated at 2022-06-13 00:40:44.924474
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    ah = AIXHardware()
    results = ah.get_cpu_facts()
    assert results['processor_count'] > 0
    assert results['processor_cores'] > 0
    assert results['processor']



# Generated at 2022-06-13 00:40:46.876385
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    assert issubclass(AIXHardwareCollector, HardwareCollector), "AIXHardwareCollector must a subclass of HardwareCollector"

# Generated at 2022-06-13 00:40:55.963808
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    args = ""
    set_module_args(args)

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)


# Generated at 2022-06-13 00:41:26.368270
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """
    Test for method get_cpu_facts of class AIXHardware
    """

# Generated at 2022-06-13 00:41:37.299695
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    uname_path = './tests/data/aix_uname_data'
    lsdev_path = './tests/data/lsdev_test'
    lsattr_path = './tests/data/lsattr_test'
    df_path = './tests/data/aix_df_data'
    mock_module = AnsibleModuleMock(ansible_module_mock=AIXHardwareCollector, uname_path=uname_path,
                                    lsdev_path=lsdev_path, lsattr_path=lsattr_path, df_path=df_path)
    ah = AIXHardware(mock_module)
    mount_facts = ah.get_mount_facts()

# Generated at 2022-06-13 00:41:42.394384
# Unit test for method get_memory_facts of class AIXHardware

# Generated at 2022-06-13 00:41:44.547307
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aix = AIXHardware()
    aix.get_vgs_facts()

# Generated at 2022-06-13 00:41:55.410594
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True)

    gather_subset = module.params['gather_subset']

    run_command = MagicMock(return_value=(0, '', ''))
    module.run_command = run_command

    get_bin_path = MagicMock(return_value=True)
    module.get_bin_path = get_bin_path

    aix_hardware = AIXHardware(module)

    if '!all' in gather_subset and 'all' not in gather_subset:
        gather_subset = aix_hardware.GATHER_SUBSET

    populate_facts = aix_hardware.populate

# Generated at 2022-06-13 00:41:57.199247
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    aix_hw = AIXHardware()
    mount_facts = aix_hw.get_mount_facts()
    mounts = mount_facts['mounts']
    assert mounts[0]['mount'] == '/'



# Generated at 2022-06-13 00:42:00.584525
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # Check that AIXHardwareCollector class is initialized
    aix_collector = AIXHardwareCollector()
    assert aix_collector._platform == 'AIX'
    assert aix_collector._fact_class == AIXHardware
    assert aix_collector._fact_class.platform == 'AIX'

# Generated at 2022-06-13 00:42:06.754594
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    """
    Test for method get_mount_facts of class AIXHardware.
    :return:
    """
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.hardware.aix import AIXHardware
    print("Running Unit test for method get_mount_facts of class AIXHardware")
    test_mount_info = {'mount': '/home',
                       'device': '/dev/hdisk0',
                       'fstype': 'jfs2',
                       'options': 'rw',
                       'time': 'Dec 02 22:36',
                       'size_total': 524288,
                       'size_available': 471816,
                       'size_used': 52472}

# Generated at 2022-06-13 00:42:11.393982
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    hw = AIXHardware()
    fact = hw.get_mount_facts()
    assert fact['mounts'][0]['mount'] == '/'
    assert fact['mounts'][0]['device'] == '/dev/hd4'
    assert fact['mounts'][0]['fstype'] == 'jfs2'
    assert fact['mounts'][0]['options'] == 'rw,log=/dev/hd8'

# Generated at 2022-06-13 00:42:20.761172
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    hw = AIXHardware(module=test_module)

    out = hw.populate()

    assert 'memtotal_mb' in out
    assert 'swaptotal_mb' in out
    assert 'processor_cores' in out
    assert 'processor_count' in out
    assert out['processor'][0] == 'PowerPC_POWER5'
    assert out['firmware_version'] == 'IBM,8233-E8B'
    assert out['product_name'] == '8233-E8B'
    assert out['vgs']['rootvg'][0]['pv_name'] == 'hdisk0'


# Generated at 2022-06-13 00:42:53.185484
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    args = {'ANSIBLE_MODULE_ARGS': {'gather_subset': '!all,!min'},
            'ANSIBLE_MODULE_CONSTANTS': {}}


# Generated at 2022-06-13 00:43:01.017255
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():

    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "proc0 Available 00-00-00-00 IBM,8231-E2B", ""))
    module.run_command = MagicMock(return_value=(0, "type PowerPC_POWER8", ""))
    module.run_command = MagicMock(return_value=(0, "smt_threads Off 8", ""))

    hardware = AIXHardware(module)

    result = hardware.get_cpu_facts()

    assert result['processor_count'] == 1
    assert result['processor_cores'] == 8
    assert result['processor'] == 'PowerPC_POWER8'


# Generated at 2022-06-13 00:43:04.967135
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    aix_hardware = AIXHardware()
    facts = aix_hardware.get_dmi_facts()
    assert 'firmware_version' in facts
    assert 'product_serial' in facts
    assert 'lpar_info' in facts
    assert 'product_name' in facts

# Generated at 2022-06-13 00:43:06.317126
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    obj = AIXHardwareCollector()
    assert obj.platform == 'AIX'
    assert obj.fact_class == AIXHardware

# Generated at 2022-06-13 00:43:11.485568
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = MockAnsibleModule()
    aix_class = AIXHardware()
    aix_class.module = module
    rc, out, err = aix_class.module.run_command("/usr/sbin/lsdev -Cc processor")
    aix_class.module.run_command.assert_called_with("/usr/sbin/lsdev -Cc processor")
    assert aix_class.get_cpu_facts() == {'processor_cores': 4, 'processor': 'POWER9', 'processor_count': 2}



# Generated at 2022-06-13 00:43:22.624882
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from distutils.version import LooseVersion
    import sys
    import ansible.module_utils.facts.hardware.aix

    if sys.version_info[0] == 2 and sys.version_info[1] == 6:
        return (False, 'Unit test for method get_device_facts of class AIXHardware '
                'does not support Python 2.6')

    if LooseVersion(ansible.__version__) < LooseVersion('2.1.0'):
        return (False, 'Unit test for method get_device_facts of class AIXHardware '
                       'works only starting from version 2.1 of Ansible')


# Generated at 2022-06-13 00:43:25.080399
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hc = AIXHardwareCollector()
    assert isinstance(hc, HardwareCollector)
    assert hc.platform == 'AIX'
    assert hc.fact_class == AIXHardware
    assert hc.config == {}
    assert hc.facts == {}


# Generated at 2022-06-13 00:43:35.627846
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    ah = AIXHardware(module)
    vgs_facts = ah.get_vgs_facts()

# Generated at 2022-06-13 00:43:44.439989
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    def run_command_mock(args, **kwargs):
        if args[0].endswith('lsdev'):
            return 0, 'ent0 Available   Network Interface', ''
        if args[0].endswith('lsattr'):
            return 0, 'alias4 ent0    Network Address\n'

# Generated at 2022-06-13 00:43:52.030998
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():

    class FakeModule:
        def run_command(self, cmd):
            out = """proc0 Available 00-00 Processor
proc1 Available 00-00 Processor
proc2 Available 00-00 Processor
proc3 Available 00-00 Processor
proc4 Available 00-00 Processor
proc5 Available 00-00 Processor
proc6 Available 00-00 Processor
proc7 Available 00-00 Processor"""
            return (0, out, '')

    class FakeFactCollector:
        def __init__(self, module):
            self.module = module

    module = FakeModule()
    fact_collector = FakeFactCollector(module)
    hardware_collector = AIXHardwareCollector(module, fact_collector)
    cpu_facts = hardware_collector.collect()

    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts

# Generated at 2022-06-13 00:44:32.501917
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    class ModuleStub(object):
        def __init__(self):
            self.bin_path = {}

        def run_command(self, *args, **kwargs):
            # lsdev -Cc disk output
            if args[0] == ("%s -o" % 'lsdev'):
                return 0, LSDEV_C_C_DISK_OUTPUT, None

            # lsattr -E -l hdisk0 output
            if args[0] == ['lsattr', '-E', '-l', 'hdisk0']:
                return 0, LSATTR_E_L_HDISK0_OUTPUT, None

            # lsattr -E -l hdisk1 output
            if args[0] == ['lsattr', '-E', '-l', 'hdisk1']:
                return 0, LS

# Generated at 2022-06-13 00:44:39.520560
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)
    hardware_facts = hardware.populate()

    assert hardware_facts['firmware_version'] == '10.230.35'
    assert hardware_facts['product_serial'] == '05C3B8B'
    assert hardware_facts['product_name'] == '8286-42A'
    assert hardware_facts['lpar_info'] == '1 CEC'

    assert hardware_facts['processor'] == 'PowerPC_POWER7'
    assert hardware_facts['processor_cores'] == 4
    assert hardware_facts['processor_count'] == 8
    assert hardware_facts['memtotal_mb'] == 16380
    assert hardware_facts['memfree_mb'] == 15180