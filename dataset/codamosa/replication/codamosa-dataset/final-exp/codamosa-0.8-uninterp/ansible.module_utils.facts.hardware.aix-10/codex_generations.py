

# Generated at 2022-06-13 00:35:10.564306
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    if not HAS_AIX_MODULES:
        module.fail_json(msg='aix modules required for this test')

    base_facts = {}
    if module._name == 'aix_hardware_facts':
        base_facts = AIXHardware(module).populate()
    elif module._name == 'aix_lsdev_facts':
        base_facts = AIXHardware(module).get_device_facts()
    else:
        module.fail_json(msg='Unknown module name')

    module.exit_json(ansible_facts=base_facts)


# Generated at 2022-06-13 00:35:13.542221
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    assert AIXHardwareCollector._platform == 'AIX'
    assert AIXHardwareCollector._fact_class == AIXHardware


# Generated at 2022-06-13 00:35:21.350025
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Prepare testable AIXHardware class
    setattr(AIXHardware, 'module', BaseFactCollector())
    setattr(AIXHardware.module, 'get_bin_path', lambda x, required=False: x)

    # Prepare test data

# Generated at 2022-06-13 00:35:25.454377
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():

    # Create an instance of AIXHardwareCollector via constructor
    aix_collector = AIXHardwareCollector()

    # Test attributes of the class
    assert aix_collector._platform == 'AIX'
    assert aix_collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:35:32.047231
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    # Arrange
    module = AnsibleModuleMock()
    path = module.get_bin_path('vmstat')
    module.run_command.return_value = (0, '2048 memory pages\n123 free pages', '')
    hardware = AIXHardware(module)

    # Act
    memory_facts = hardware.get_memory_facts()

    # Assert
    module.run_command.assert_called_once_with(path + ' -v')
    assert memory_facts['memtotal_mb'] ==  8
    assert memory_facts['memfree_mb'] == 0



# Generated at 2022-06-13 00:35:41.596761
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():

    # Create AIXHardware
    ah = AIXHardware()

    # Mock methods
    ah.module.run_command = ah.run_command
    
    # Test first use case
    rc = 0
    out = '''
              memory pages   =        131072
              total  data   =        61658
              total  stack  =        16384
              total  text   =        53248
              pin  data    =        60871
              pin  stack   =        16384
              pin  text    =        53248
              data             =        5047
              stack            =        655
              text             =        0
              free pages       =        96311
              long-term average free pages =       73114
              free list         =        96311 
    '''

    err = ''

# Generated at 2022-06-13 00:35:54.034531
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardware_module = AIXHardware(module)


# Generated at 2022-06-13 00:35:56.726709
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:36:02.744399
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    # returns AIXHardware
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=[], type='list')})
    hardware_facts = AIXHardware(module).populate()

    assert 'firmware_version' in hardware_facts
    assert 'product_serial' in hardware_facts
    assert 'product_name' in hardware_facts
    assert 'lpar_info' in hardware_facts



# Generated at 2022-06-13 00:36:09.979172
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    test_obj = AIXHardware()


# Generated at 2022-06-13 00:36:33.764534
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    hardware = AIXHardware('module')
    hardware.module.run_command = lambda *args, **kwargs: (0, '', '')
    facts = hardware.populate()

    assert facts['memfree_mb']
    assert facts['memtotal_mb']
    assert facts['swapfree_mb']
    assert facts['swaptotal_mb']
    assert facts['processor']
    assert facts['processor_cores']
    assert facts['processor_count']
    assert facts['firmware_version']
    assert facts['product_serial']
    assert facts['lpar_info']
    assert facts['product_name']



# Generated at 2022-06-13 00:36:35.282928
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw = AIXHardwareCollector()
    print(hw._platform)


# Generated at 2022-06-13 00:36:42.285209
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)

    dmi_facts = {
        'firmware_version': 'IBM,BLA24123',
        'product_serial': '2F234567H',
        'lpar_info': 'partition1 22 24',
        'product_name': 'IBM,8347-L23-MHB'
    }

    # Test case 1: successful completion
    module.run_command = MagicMock(return_value=(0, '  IBM,BLA24123', ''))
    module.get_bin_path = MagicMock(return_value=True)

# Generated at 2022-06-13 00:36:43.972607
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    f = AIXHardware()
    mount_result = f.get_mount_facts()
    assert mount_result is not None

# Generated at 2022-06-13 00:36:50.323362
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)
    hardware_facts = hardware.get_memory_facts()
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['swaptotal_mb'] >= 0
    assert hardware_facts['swapfree_mb'] >= 0



# Generated at 2022-06-13 00:36:59.702108
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    test_module = type('', (), {'run_command': get_mount_facts_command_data})
    test_instance = AIXHardware(test_module)
    test_result = test_instance.get_mount_facts()

# Generated at 2022-06-13 00:37:10.845852
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    # The test expects a "module" to be an object that contains a "run_command"
    # function that behaves like a run_command function saved in a
    # "module_utils/basic.py" file and a "get_bin_path" function that behaves
    # like a function saved in "ansible/module_utils/facts/utils/get_module",
    # therefore the test creates a fake module that contains two functions that
    # behave like they were in the "ansible/module_utils/facts/hardware/aix.py"
    # file.
    _module = FakeModule()

    _module.run_command = FakeRunCommand()
    _module.run_command.set_response(0, '12345 memory pages\n'
                                         '54321 free pages\n')


# Generated at 2022-06-13 00:37:12.645846
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    x = AIXHardwareCollector()
    assert isinstance(x, HardwareCollector)


# Generated at 2022-06-13 00:37:16.640995
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # mock os
    _platform = 'AIX'
    _fact_class = AIXHardware
    aix_hw_col = AIXHardwareCollector(_platform, _fact_class)
    assert aix_hw_col._platform == _platform
    assert aix_hw_col._fact_class == _fact_class

# Generated at 2022-06-13 00:37:24.132589
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """Test method get_cpu_facts of class AIXHardware."""

    import os
    import shutil
    import tempfile

    test_file = os.path.join(tempfile.mkdtemp(), 'test_AIXHardware_get_cpu_facts.lsdev')

    # stub lsdev command
    cmd_stub = "lsdev -Cc processor > %s" % test_file
    try:
        os.system(cmd_stub)
    finally:
        pass

    # call get_cpu_facts which will return empty dictionary
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    obj = AIXHardware()
    cpu_facts = obj.get_cpu_facts()
    if not cpu_facts:
        assert 1 == 1

    # stub lsdev command
    cmd_st

# Generated at 2022-06-13 00:38:03.468661
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hardwareCollector = AIXHardwareCollector(module)



# Generated at 2022-06-13 00:38:06.629329
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """ Test the constructor of class AIXHardwareCollector """
    aix_hardware = AIXHardwareCollector()
    assert aix_hardware.platform == 'AIX'
    assert aix_hardware.fact_class == AIXHardware

# Generated at 2022-06-13 00:38:08.006496
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    assert isinstance(AIXHardwareCollector().hardware, AIXHardware)

# Generated at 2022-06-13 00:38:12.824713
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware_collector = AIXHardwareCollector(module=module, params={})
    hardware = hardware_collector.collect()[0]
    assert hardware.platform == 'AIX'
    assert hardware.processor_count == 4
    assert hardware.processor == 'PowerPC_POWER8'
    assert hardware.processor_cores == 4

# Generated at 2022-06-13 00:38:24.210239
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    dummy_module = DummyModule()
    dummy_module.get_bin_path('lsattr', True)
    dummy_module.lsattr = MagicMock(return_value = 'FWVERSION IBM,8233-E8B\n')
    dummy_module.get_bin_path('lsconf', True)
    dummy_module.lsconf = MagicMock(return_value = 'Machine Serial Number: 03M1234\n ... \nLPAR Info:\n1 ENT 1\nSystem Model: IBM,8233-E8B')
    obj = AIXHardware(dummy_module)
    dmi_facts = obj.get_dmi_facts()
    assert dmi_facts['product_serial'] == '03M1234'
    assert dmi_facts['lpar_info'] == '1 ENT 1'
    assert dmi

# Generated at 2022-06-13 00:38:36.037831
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Unit test for method get_vgs_facts of class AIXHardware
    """
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    import os

    if os.path.exists('/usr/sbin/lsvg'):
        lsvg_path = '/usr/sbin/lsvg'
    elif os.path.exists('/usr/bin/lsvg'):
        lsvg_path = '/usr/bin/lsvg'
    elif os.path.exists('/sbin/lsvg'):
        lsvg_path = '/sbin/lsvg'
    elif os.path.exists('/bin/lspkg'):
        lsvg_path = '/bin/lsvg'


# Generated at 2022-06-13 00:38:41.190063
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module_mock = AnsibleModuleMock()
    module_mock.run_command.return_value = (
        0,
        """
        firmware_version: IBM,8205-E6C
        """
    )
    hardware = AIXHardware(module_mock)
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['firmware_version'] == 'IBM,8205-E6C'



# Generated at 2022-06-13 00:38:52.617553
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:39:01.564407
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    aix_hw = AIXHardware({})
    def mock_run_command(command, **kwargs):
        class MockData():
            def __init__(self, stdout, stdin, stderr, rc):
                self.stdout = stdout
                self.stdin = stdin
                self.stderr = stderr
                self.rc = rc

# Generated at 2022-06-13 00:39:07.058338
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    if not module.check_mode:
        hardware = AIXHardware(module=module)
        facts = hardware.populate()
        assert 'memtotal_mb' in facts
        assert 'memfree_mb' in facts
    else:
        module.exit_json(changed=False, ansible_facts={})



# Generated at 2022-06-13 00:40:29.660884
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    devices = hardware.get_device_facts()['devices']
    assert '/dev/hdisk0' in devices
    assert '/dev/hdisk1' in devices
    assert devices['/dev/hdisk1']['state'] == "Available"
    assert devices['/dev/hdisk1']['type'] == "FC Adapter"
    assert 'size' in devices['/dev/hdisk1']['attributes']
    assert 'devno' in devices['/dev/hdisk1']['attributes']
    assert 'dev_type' in devices['/dev/hdisk1']['attributes']

# Generated at 2022-06-13 00:40:39.645344
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = mock.Mock()
    module.run_command.return_value = (0, None, None)
    module.get_bin_path.return_value = True
    module.get_mount_size.return_value = {'size_total': 1,
                                          'size_available': 1,
                                          'size_used': 1,
                                          'inode_total': 1,
                                          'inode_available': 1,
                                          'inode_used': 1}
    ah = AIXHardware(module)
    print(ah.populate())

    assert ah.populate()['firmware_version'] == 'IBM,8233-E8B'

# Generated at 2022-06-13 00:40:48.240235
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec = dict())
    hardware = AIXHardware(module=module)
    hardware.module.run_command = MagicMock(return_value=(0,
                                                          'proc0 Available 00-00 Processor 0 00-00-00-00-00-00-00-00',
                                                          'stdout'))
    expected_result = {'processor': '00-00', 'processor_count': 1, 'processor_cores': 1}
    result = hardware.get_cpu_facts()

    # Verify that the method returns the expected values
    assert result == expected_result

    return


# Generated at 2022-06-13 00:40:51.288028
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    testAIXHardwareCollector = AIXHardwareCollector()
    assert testAIXHardwareCollector._platform == 'AIX'
    assert testAIXHardwareCollector._fact_class == AIXHardware

# Generated at 2022-06-13 00:40:59.320572
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    cpu_info = """
proc0 Available 00-00
proc1 Available 00-01
proc2 Available 00-02
proc3 Available 00-03
proc4 Available 00-04
proc5 Available 00-05
proc6 Available 00-06
proc7 Available 00-07
proc8 Available 00-08
proc9 Available 00-09
proc10 Available 00-0A
proc11 Available 00-0B
proc12 Available 00-0C
proc13 Available 00-0D
proc14 Available 00-0E
proc15 Available 00-0F
proc16 Available 00-10
proc17 Available 00-11
proc18 Available 00-12
proc19 Available 00-13
""".strip()
    cpu_facts = AIXHardware().get_cpu_facts(cpu_info)
    assert cpu_facts['processor_count'] == 20

# Generated at 2022-06-13 00:41:08.143266
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    hardware = AIXHardware(None)
    memory_facts = hardware.get_memory_facts()
    assert isinstance(memory_facts['memtotal_mb'], int) and memory_facts['memtotal_mb'] >= 0, 'MemTotal is not a valid integer value'
    assert isinstance(memory_facts['memfree_mb'], int) and memory_facts['memfree_mb'] >= 0, 'MemFree is not a valid integer value'
    assert isinstance(memory_facts['swaptotal_mb'], int) and memory_facts['swaptotal_mb'] >= 0, 'SwapTotal is not a valid integer value'
    assert isinstance(memory_facts['swapfree_mb'], int) and memory_facts['swapfree_mb'] >= 0, 'SwapFree is not a valid integer value'

# Generated at 2022-06-13 00:41:14.794339
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = MockModule()
    hw = AIXHardware
    hw.module = module
    hw.mount_path = module.get_bin_path("mount")
    rc, out, err = module.run_command("".join([hw.mount_path, " > /tmp/mount"]))
    hw.mount_path = "/tmp/mount"
    rc, out, err = module.run_command("".join([hw.mount_path, " > /tmp/mount"]))
    hw.module.run_command = Mock(return_value=(0, out, err))
    facts = hw.get_mount_facts()

# Generated at 2022-06-13 00:41:24.049073
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:41:29.764076
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # setup test parameters
    module = {}
    command_runner = {}

    # instantiate the AIXHardwareCollector object
    obj = AIXHardwareCollector(module, command_runner)

    # check if object is instance of class AIXHardwareCollector
    assert isinstance(obj, AIXHardwareCollector)


# Generated at 2022-06-13 00:41:39.145434
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:44:37.626088
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    hardware_obj = AIXHardware(module)
    result = hardware_obj.get_mount_facts()
    assert result is not None