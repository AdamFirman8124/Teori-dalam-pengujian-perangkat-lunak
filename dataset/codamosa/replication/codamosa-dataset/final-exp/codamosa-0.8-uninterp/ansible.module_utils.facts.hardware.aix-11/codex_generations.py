

# Generated at 2022-06-13 00:35:08.806356
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={
        'filter': {'type': 'list', 'elements': 'str', 'default': ['*']},
        'gather_subset': {'type': 'list', 'elements': 'str', 'default': ['all']},
        'gather_timeout': {'type': 'int', 'default': 10},
    })

    class MockAIXHardware(AIXHardware):
        def __init__(self, module):
            self.module = module

    ah = MockAIXHardware(module)
    mounts_facts = ah.get_mount_facts()
    mount_path = ah.module.get_bin_path('mount')
    rc, mount_out, err = ah.module.run_command(mount_path)

# Generated at 2022-06-13 00:35:18.113014
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class MockModule:
        def run_command(self, command):
            out = """
                  memory pages
                  4194304
                  free pages
                  2103890
                  """
            return 0, out, None

    # Setup a mock module for testing
    module = MockModule()

    # Setup a mock object for testing
    fact_obj = AIXHardware(module)

    # Invoke the get_memory_facts function on the mock object
    result = fact_obj.get_memory_facts()

    # Check the result
    assert result == {'swapfree_mb': 0, 'memfree_mb': 1660, 'swaptotal_mb': 0, 'memtotal_mb': 16384}


# Generated at 2022-06-13 00:35:21.990150
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aix_hardware = AIXHardware()

    result = aix_hardware.get_dmi_facts()

    assert result['firmware_version'] is not None

# Generated at 2022-06-13 00:35:23.161187
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector.platform == 'AIX'


# Generated at 2022-06-13 00:35:32.142846
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})

    hw = AIXHardware(module)
    facts = hw.populate()

    assert facts.get('firmware_version') is not None, \
    "firmware_version is not None but %r" % facts.get('firmware_version')

    assert facts.get('product_name') is not None, \
    "product_name is not None but %r" % facts.get('product_name')

    assert facts.get('product_serial') is not None, \
    "product_serial is not None but %r" % facts.get('product_serial')

    assert facts.get('lpar_info') is not None, \
    "lpar_info is not None but %r" % facts.get('lpar_info')


# Generated at 2022-06-13 00:35:41.670694
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 00:35:54.034909
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    hw = AIXHardware(None)

    # mocked facts from AIX 6.1 TL7
    hw.module = Mock()
    hw.module.run_command = Mock()
    hw.module.run_command.return_value = (0,
"""proc0 Available 00-00 Processor
proc1 Available 00-01 Processor
proc2 Available 00-02 Processor
proc3 Available 00-03 Processor
""",
    "")
    hw.module.run_command.side_effect = [("",
"""type PowerPC_POWER7
smt_threads 8
""", "")]

    hw.populate()

# Generated at 2022-06-13 00:35:57.827208
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    module.check_mode = False
    aix = AIXHardware(module)
    out = aix.get_mount_facts()
    assert type(out['mounts']) == list

# Generated at 2022-06-13 00:36:04.947878
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class DummyModule:
        def run_command(module, cmd, use_unsafe_shell=False):
            return 0, "memory pages: 4380000\nfree pages: 4379898\n", ""
    dummy_module = DummyModule()
    aix_hardware = AIXHardware(dummy_module)
    result = aix_hardware.get_memory_facts()
    assert (result['memtotal_mb'] == 17015)
    assert (result['memfree_mb'] == 17013)


# Generated at 2022-06-13 00:36:15.967966
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    class FakeModule(object):
        def get_bin_path(self, exe, required=False):
            if 'lsdev' in exe:
                return exe
            else:
                return '/usr/sbin/lsattr'

        def run_command(self, cmd, use_unsafe_shell=True):
            if '/usr/sbin/lsattr' in cmd:
                out = ("attr_name attr_parameter",
                       "attr_name attr_parameter",
                       "attr_name attr_parameter")

# Generated at 2022-06-13 00:36:37.107834
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = type('Module', (object, ), {'run_command': run_command_mock})
    aix_hardware = AIXHardware(module)
    all_facts = dict()
    all_facts['ansible_system'] = 'AIX'
    cpu_facts = aix_hardware.get_cpu_facts(all_facts)

    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 8



# Generated at 2022-06-13 00:36:48.999080
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    from ansible.module_utils.facts.hardware.aix import AIXHardware

# Generated at 2022-06-13 00:36:52.662298
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    h_collector = AIXHardwareCollector()
    assert h_collector._platform == 'AIX'
    assert h_collector._fact_class == AIXHardware
    assert h_collector._fact_class.platform == 'AIX'

# Generated at 2022-06-13 00:36:55.049724
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    ah = AIXHardware()
    ah.module = module
    ah.populate()


# Generated at 2022-06-13 00:37:07.441542
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_facts = AIXHardware(module).populate()

    assert hardware_facts['firmware_version'] == '1'
    assert hardware_facts['product_name'] == 'IBM,9117-570'
    assert hardware_facts['product_serial'] == '06A57182'
    assert hardware_facts['processor_cores'] == 1
    assert hardware_facts['processor_count'] == 2
    assert hardware_facts['processor'] == 'PowerPC_POWER7'
    assert hardware_facts['memfree_mb'] == 257
    assert hardware_facts['memtotal_mb'] == 1088
    assert hardware_facts['swaptotal_mb'] == 2048
    assert hardware_facts['swapfree_mb'] == 2048
    assert hardware_facts['lpar_info']

# Generated at 2022-06-13 00:37:17.798436
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:37:25.508128
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    import sys
    import os
    import tempfile
    import shutil
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils._text import to_bytes

    devnull = open(os.devnull, 'w')

    # Redirect stdout and stderr
    sys.stdout = devnull
    sys.stderr = devnull

    # Create fake directory
    tempdir = tempfile.mkdtemp()

    # Create fake AIX commands
    commands = {
        'vmstat': os.path.join(tempdir, 'vmstat'),
        'lsps': os.path.join(tempdir, 'lsps')
    }

    # Create fake vmstat command

# Generated at 2022-06-13 00:37:27.266344
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    AIXHardwareObject = AIXHardware()
    mount_facts = AIXHardwareObject.get_mount_facts()
    assert mount_facts['mounts']

# Generated at 2022-06-13 00:37:31.029278
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix_collector = AIXHardwareCollector()
    assert aix_collector._fact_class == AIXHardware
    assert aix_collector._platform == 'AIX'


# Generated at 2022-06-13 00:37:34.767893
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hardware_facts = AIXHardwareCollector(module).collect()
    assert hardware_facts.pop('system') == AIXHardwareCollector.get_platform()
    assert hardware_facts.pop('module_hw') == True



# Generated at 2022-06-13 00:38:10.882598
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_system = AIXHardware()
    result = test_system.get_cpu_facts()
    assert 'processor_cores' in result


# Generated at 2022-06-13 00:38:18.376610
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec=dict())
    module.params['gather_subset'] = ['!all', 'devices']
    module.params['filter'] = '*'

    facts = AIXHardware(module=module)

    # Get facts
    facts.populate()

    # Basic test
    devices = facts.get_devices()
    assert devices
    assert isinstance(devices, dict)

    # device
    assert 'hdisk0' in devices
    assert 'hdisk1' in devices
    assert 'cd0' in devices
    assert 'nvidia' in devices
    assert 'scsi0' in devices
    assert 'scsi2' in devices
    assert 'loop0' in devices
    assert 'usbhc0' in devices

    # state

# Generated at 2022-06-13 00:38:22.778264
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts


# Generated at 2022-06-13 00:38:34.593752
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.aix.hardware.aix_hardware import AIXHardware

    module = AnsibleModule(
        argument_spec = dict(
            filter = dict(default='*', required=False)
        )
    )


# Generated at 2022-06-13 00:38:42.097885
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module=module)
    facts = hardware.populate()
    assert facts['processor']
    assert facts['processor_cores']
    assert facts['processor_count']
    assert facts['memtotal_mb']
    assert facts['memfree_mb']
    assert facts['swaptotal_mb']
    assert facts['swapfree_mb']
    assert facts['firmware_version']
    assert facts['product_serial']
    assert facts['product_name']
    assert facts['lpar_info']
    assert facts['vgs']
    assert facts['mounts']
    assert facts['devices']

# Generated at 2022-06-13 00:38:43.745076
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class == 'AIXHardware'

# Generated at 2022-06-13 00:38:55.861185
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    """
    Test the method get_dmi_facts of class AIXHardware.
    """
    import mock
    import sys

    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    aixhw = AIXHardware()
    aixhw.module = mock.Mock()
    aixhw.module.run_command = mock.Mock()

    # Set the aixhw.module.run_command side effect to return test results.

# Generated at 2022-06-13 00:39:04.249316
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = FakeAnsibleModule()
    hardware = AIXHardware(module)

    vmstat_path = module.get_bin_path("vmstat")
    if vmstat_path:
        vmstat_output="""memory pages
        53496
        free pages
        53496
        """
        module.run_command.return_value = 0, vmstat_output, ''
        memory_facts = hardware.get_memory_facts()
        assert memory_facts == {'memfree_mb': 20972, 'memtotal_mb': 20983}



# Generated at 2022-06-13 00:39:16.202215
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.collector.aix.mounts import AIXMountDevice
    class DummyModule:
        def __init__(self):
            self.run_command_environ_update = dict(LANG='C', LC_ALL='C', LC_MESSAGES='C', LC_CTYPE='C')

        def get_bin_path(self, path, required=False):
            if path == 'mount':
                return '/usr/sbin/mount'
            elif path == 'lsvg':
                return '/usr/sbin/lsvg'
            elif path == 'xargs':
                return '/usr/bin/xargs'
            else:
                return path


# Generated at 2022-06-13 00:39:20.166824
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module=module)
    vgs_facts = hardware.get_vgs_facts()

    assert vgs_facts['vgs']
    for e in vgs_facts['vgs']:
        assert vgs_facts['vgs'][e]
        for f in vgs_facts['vgs'][e]:
            assert vgs_facts['vgs'][e][f]


# Generated at 2022-06-13 00:40:33.499688
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:40:38.362256
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """
    Unit test for method get_cpu_facts of class AIXHardware
    """
    module = AnsibleModule(argument_spec=dict())
    hardware_obj = AIXHardware(module)
    hardware_obj.populate()
    assert isinstance(hardware_obj.populate(), dict)


# Generated at 2022-06-13 00:40:49.116817
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    # Test without Available processor entries
    fake_module = get_fake_module('lsdev -Cc processor', rc=0, out='')
    hardware = AIXHardware(fake_module)
    facts = hardware.get_cpu_facts()
    assert 'processor' in facts
    assert facts['processor'] == []
    assert 'processor_count' in facts
    assert facts['processor_count'] == 0
    assert 'processor_cores' not in facts

    # Test with Available processor entries
    fake_module = get_fake_module('lsdev -Cc processor', rc=0, out='proc0 Available 00-00')
    fake_module.run_command = get_run_command_method('lsdev -Cc processor')
    hardware = AIXHardware(fake_module)
    facts = hardware.get_cpu_facts()
   

# Generated at 2022-06-13 00:40:57.823169
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    hardware = AIXHardware(test_module)

    out = """Manufacture Date: 05/13/2009
    Machine Serial Number: 12345678
    Model: IBM,9437-11G
    Model Type: 7942
    Part Number: 6232
    ROM Level: IBM,1.28 (09/28/2011)
    System Type: B91
    TCPA Support: Yes
    Type: Power
    UUID: 12345678-123-123-1234-123456789012
    """

    rc = 0
    err = ''


# Generated at 2022-06-13 00:41:04.550516
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():

    class MockModule:
        def __init__(self):
            self.params = {}
            self.exit_json = None

        def run_command(self, cmd, **kwargs):
            return 0, "", ""

        def get_bin_path(self, name, none_on_missing=False):
            return "path to %s" % name

    class MockAIXHardware(AIXHardware):
        def __init__(self, module):
            self.module = module

    class FactModule(object):
        def __init__(self):
            self.exit_json = None
            self.params = {}

        def exit_json(self, **kwargs):
            pass

    aixhw = MockAIXHardware(MockModule())
    res = aixhw.get_device_facts()

# Generated at 2022-06-13 00:41:11.014028
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    mock_run_command = MagicMock()
    module.run_command = mock_run_command
    mock_run_command.return_value = (0, 'processor   Available  00-00\nprocessor   Available  00-01\n', '')
    ahw = AIXHardware(module)
    facts = ahw.get_cpu_facts()
    assert facts['processor_count'] == 2
    assert facts['processor_cores'] == 1
    assert facts['processor'] == 'proc0'
    mock_run_command.assert_has_calls([call('/usr/sbin/lsdev -Cc processor')])


# Generated at 2022-06-13 00:41:17.010116
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    hardware = AIXHardware()
    hardware.module = AnsibleModule(argument_spec={})
    hardware.module.run_command = MagicMock()
    hardware.module.run_command.return_value = (0, 'memory pages:                                                           \
    354756                                                                          \
    free pages:                                                                     \
    23850                                                                           \
    filesystem pages:                                                               \
    240                                                                             \
    pin pages:                                                                      \
    1709                                                                            \
    paging space pages:                                                             \
    16777215                                                                        \
    total ram pages:                                                                \
    3275706', '')
    result = hardware.get_memory_facts()

# Generated at 2022-06-13 00:41:21.299587
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    class ModuleFake:
        def get_bin_path(self, binary, required=False):
            lsdev_path = '/usr/sbin/lsdev'
            lsattr_path = '/usr/sbin/lsattr'
            if binary == 'lsdev':
                return lsdev_path
            elif binary == 'lsattr':
                return lsattr_path


# Generated at 2022-06-13 00:41:24.833327
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    module = AIXHardware()
    facts = {'processor': ['PowerPC_POWER8'], 'processor_cores': 4, 'processor_count': 4}
    assert module.get_cpu_facts() == facts



# Generated at 2022-06-13 00:41:36.204903
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:44:08.117072
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    testHardware = AIXHardware(dict())
    data = testHardware.get_cpu_facts()
    assert data['processor_cores']
    assert data['processor']
    assert data['processor_count']

# Generated at 2022-06-13 00:44:15.721668
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command_calls = []

        def get_bin_path(self, name):
            return '/usr/sbin/' + name

        def run_command(self, cmd, use_unsafe_shell=False):
            self.run_command_calls.append(cmd)
            if 'lsvg' in cmd and 'xargs' in cmd:
                return 0, (lsvg_output + lsvg_xargs_output), ''
            elif 'lsvg' in cmd:
                return 0, lsvg_output, ''

    # Non rootvg

# Generated at 2022-06-13 00:44:17.601274
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # Test for constructor of class AIXHardwareCollector
    hd = AIXHardwareCollector()
    assert hd._platform == 'AIX'
    assert hd._fact_class == AIXHardware


# Generated at 2022-06-13 00:44:25.340039
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    ahw = AIXHardware(module)
    cpu_facts = ahw._get_cpu_facts()
    assert True is isinstance(cpu_facts, dict)
    assert True is isinstance(cpu_facts['processor'], list)
    assert True is isinstance(cpu_facts['processor_cores'], int)
    assert True is isinstance(cpu_facts['processor_count'], int)


# Generated at 2022-06-13 00:44:33.757345
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    # A:
    settings = dict(
        mounts = [
            {'device': 'node',
             'fstype': 'dev',
             'mount': 'Mounted',
             'options': 'on',
             'time': 'Tue',
             'total_size_kb': 'Sep',
             'used_size_kb': '01'}
        ]
    )
    # D:
    expected_mounts = [
        {'device': 'node',
         'fstype': 'dev',
         'mount': 'Mounted',
         'options': 'on',
         'time': 'Tue',
         'total_size_kb': 'Sep',
         'used_size_kb': '01'}
    ]
    # E:
    assert settings['mounts'] == expected_mounts


# Generated at 2022-06-13 00:44:41.213952
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list')
        ),
        supports_check_mode=False,
    )

    runner = ModuleRunner(module)

    # Passing
    runner.set_fact_file(os.path.join(fixture_path, 'ansible_local.fact'))
    facts = runner.run(module, 'populate')
    assert facts['ansible_facts']['processor_count'] == 8
    assert facts['ansible_facts']['processor_cores'] == 2
    assert facts['ansible_facts']['processor'] == 'PowerPC_POWER8'
    assert facts['ansible_facts']['memtotal_mb'] == 61632