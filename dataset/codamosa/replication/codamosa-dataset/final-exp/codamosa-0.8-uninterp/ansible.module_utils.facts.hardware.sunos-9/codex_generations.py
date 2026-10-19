

# Generated at 2022-06-13 01:06:33.375946
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModule(
        argument_spec = dict()
    )
    hardware = SunOSHardware(module=module)
    rc = open('tests/data/uptime_facts')
    out = rc.read()
    rc.close()
    result = hardware.get_uptime_facts(out)
    assert result['uptime_seconds'] == 1548249689

# Generated at 2022-06-13 01:06:40.607599
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # Mock module and class SunOSHardware
    class MockModule():
        def run_command(self, cmd):
            return 0, 'Memory size: 8192 Megabytes', None

    class MockSunOSHardware(SunOSHardware):
        def __init__(self):
            self.module = MockModule()

    # Create instance of class SunOSHardware
    sunos_memory_facts = MockSunOSHardware()
    # Call method get_memory_facts
    result = sunos_memory_facts.get_memory_facts()

    # Assert method get_memory_facts returns correct result
    assert result == dict(memtotal_mb=8192)

# Generated at 2022-06-13 01:06:53.086884
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = DummyModule()
    hardware = SunOSHardware(module)
    device_facts = hardware.get_device_facts()
    assert device_facts == {'devices': {'sda': {'hard_errors': '0',
                                                'illegal_request': '6',
                                                'media_errors': '0',
                                                'predictive_failure_analysis': '0',
                                                'product': 'VBOX HARDDISK',
                                                'revision': '1.0',
                                                'serial': 'VB0ad2ec4d-074a',
                                                'size': '50.00 GB',
                                                'soft_errors': '0',
                                                'transport_errors': '0',
                                                'vendor': 'ATA'}}
                              }

# Generated at 2022-06-13 01:06:54.107201
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    SunOSHardwareCollector()

# Generated at 2022-06-13 01:06:59.567460
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collector import get_collector_instance

    facts_collector = FactCollector()
    SunOSHW = get_collector_instance(SunOSHardwareCollector, facts_collector)

    facts = {}
    SunOSHW.get_cpu_facts(facts)
    assert facts["processor_count"] == 1



# Generated at 2022-06-13 01:07:11.838175
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    '''
    Test the populate method of SunOSHardware
    '''
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # Create a FakeModule with basic attributes normally set by AnsibleModule
    class FakeModule:
        def __init__(self):
            self.run_command_environ_update = None

        def get_bin_path(self, app, **kwargs):
            return app

        def run_command(self, args, **kwargs):
            return 0, '', ''

    # Create Collector
    test_collector = Collector()
    test_collector.collectors = [DistributionFactCollector]
    test_collector.collect()

    #

# Generated at 2022-06-13 01:07:14.499043
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    assert SunOSHardwareCollector.collect() == {'platform': 'SunOS'}


# Generated at 2022-06-13 01:07:19.538290
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardware_collector_class = SunOSHardwareCollector()
    hardware_collector_class.collect()
    for key in hardware_collector_class.facts.keys():
        assert hardware_collector_class.facts[key] is not None

if __name__ == '__main__':
    test_SunOSHardwareCollector()

# Generated at 2022-06-13 01:07:31.839336
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.test.test_module_1 import mock_module

    module = mock_module()
    module.run_command = MagicMock(return_value=(0, '', ''))

    hardware = SunOSHardware(module)

    hardware.get_cpu_facts = MagicMock()
    hardware.get_memory_facts = MagicMock()
    hardware.get_dmi_facts = MagicMock()
    hardware.get_device_facts = MagicMock()
    hardware.get_uptime_facts = MagicMock()

    hardware.populate()

    hardware.get_cpu_facts.assert_called_once_with()
    hardware.get_memory_facts.assert_called_once_with()
    hardware.get_dmi_facts.assert_called_once_with()
    hardware

# Generated at 2022-06-13 01:07:40.129026
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()
    hardware.module.run_command = lambda x, use_unsafe_shell=False: ('', 'System Configuration:\tOracle Corporation\tSUNW,SPARC-Enterprise-T5120\n', '')

    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['system_vendor'] == 'Oracle Corporation'
    assert dmi_facts['product_name'] == 'SUNW,SPARC-Enterprise-T5120'


# Generated at 2022-06-13 01:08:05.741683
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    """
    Given the following uptime data

    kstat unix:0:system_misc:boot_time    1548249689
    """
    temp_module = mock.MagicMock()
    temp_module.run_command.return_value = (0, "unix:0:system_misc:boot_time    1548249689", '')

    hardware = SunOSHardware(temp_module)
    uptime_facts = hardware.get_uptime_facts()


# Generated at 2022-06-13 01:08:15.298265
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:08:23.349481
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = FakeAnsibleModule()
    hardware_facts = SunOSHardware(module).populate()

    assert hardware_facts['processor_cores'] == 'NA'
    assert hardware_facts['processor_count'] == 8
    assert hardware_facts['memtotal_mb'] == 4096
    assert hardware_facts['swapfree_mb'] == 8388608
    assert hardware_facts['swaptotal_mb'] == 8388608
    assert hardware_facts['swap_allocated_mb'] == 0
    assert hardware_facts['swap_reserved_mb'] == 0
    assert hardware_facts['system_vendor'] == 'Oracle Corporation'
    assert hardware_facts['product_name'] == 'VirtualBox'
    assert hardware_facts['devices']['sd0']['product'] == 'VBOX HARDDISK'
    assert hardware

# Generated at 2022-06-13 01:08:25.237576
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.collector.sunos import SunOSHardware
    sunos_hw = SunOSHardware({})
    assert sunos_hw.get_dmi_facts() == {'system_vendor': 'QEMU', 'product_name': 'Standard PC (i440FX + PIIX, 1996)'}

# Generated at 2022-06-13 01:08:35.496767
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, 'unix:0:system_misc:boot_time    1548249689', ''))

    sunos_hardware = SunOSHardware(module=module)
    uptime_facts = sunos_hardware.get_uptime_facts()

    module.run_command.assert_called_with('/usr/bin/kstat -p unix:0:system_misc:boot_time')

    #   time.time() - boot_time
    assert uptime_facts['uptime_seconds'] == time.time() - 1548249689

# Generated at 2022-06-13 01:08:38.926203
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'sderr:::Serial No\tsd0\t99\tsd1\t0', ''))
    H = SunOSHardware(module)
    assert H.get_device_facts() == {'devices': {'sd0': {'serial': '99'}}}


# Generated at 2022-06-13 01:08:49.092114
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():

    class RunCommandMock:
        def __init__(self):
            self.returncode = 0
            self.stdout = """
System Configuration: VMware, Inc. VMware Virtual Platform
"""
        def __call__(self, *args):
            return self

    class ModuleMock:
        def __init__(self):
            self.run_command = RunCommandMock()

    fake_module = ModuleMock()

    sunos_hardware = SunOSHardware(fake_module)
    dmi_facts = sunos_hardware.get_dmi_facts()

    assert type(dmi_facts) is dict
    assert len(dmi_facts.keys()) == 2



# Generated at 2022-06-13 01:08:57.644908
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    hardware_collector = SunOSHardware(module)
    facts = hardware_collector.populate()

    assert 'processor' in facts
    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swap_allocated_mb' in facts
    assert 'swap_reserved_mb' in facts
    assert 'mounts' in facts
    assert 'devices' in facts
    assert 'uptime_seconds' in facts

# Generated at 2022-06-13 01:09:03.432854
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = mock.MagicMock()
    module.run_command = mock.Mock()
    module.run_command.return_value = (0, 'Memory size: 16384 Megabytes', '')

    test_obj = SunOSHardware(module)
    assert test_obj.get_memory_facts() == {'memtotal_mb': 16384}



# Generated at 2022-06-13 01:09:10.867411
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware_facts = SunOSHardware()
    facts = hardware_facts.populate()
    assert facts['ansible_processor'][0].startswith('SPARC M8')
    assert facts['ansible_processor_arch'].startswith('sparc')
    assert 'memtotal_mb' in facts
    assert 'swap_allocated_mb' in facts
    assert 'swap_reserved_mb' in facts
    assert 'processor_count' in facts
    assert 'processor_cores' in facts



# Generated at 2022-06-13 01:09:51.828279
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Create an instance of the class SunOSHardware
    instance = SunOSHardware()

    # Result of the command "/usr/sbin/kstat cpu_info"
    with open("tests/unit/module_utils/facts/hardware/SunOS/kstat_cpu_info.txt") as f:
        kstat_cpu_info_out = f.read()

    # Result of the command "/usr/sbin/prtconf"
    with open("tests/unit/module_utils/facts/hardware/SunOS/prtconf.txt") as f:
        prtconf_out = f.read()

    # Result of the command "/usr/sbin/swap -s"
    with open("tests/unit/module_utils/facts/hardware/SunOS/swap_s.txt") as f:
        swap_s

# Generated at 2022-06-13 01:09:58.146251
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = AnsibleModuleMock({'system_vendor': 'Oracle Corporation',
                                'product_name': 'SUN FIRE X4170 SERVER'})

    d = SunOSHardware(module)
    dmi_facts = d.get_dmi_facts()

    assert dmi_facts['system_vendor'] == 'Oracle Corporation'
    assert dmi_facts['product_name'] == 'SUN FIRE X4170 SERVER'

# Generated at 2022-06-13 01:10:09.381485
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    fake_module = 'fake'


# Generated at 2022-06-13 01:10:18.423013
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # find out about the current boot time
    boot_time = None
    rc, out, err = module.run_command('/usr/bin/kstat -p unix:0:system_misc:boot_time')
    if rc == 0:
        boot_time = int(out.split('\t')[1])

    h = SunOSHardware()

    # the test for rc != 0 above is weak. If it's faulty,
    # we want to avoid this command raising an exception.
    # so we'll explicitly test for that and mock the result
    # if rc != 0
    h.module.run_command = lambda cmd: (boot_time is not None and [rc, out, err] or [0, "", ""])[module.run_command.__code__.co_argcount]

    uptime_facts = h.get

# Generated at 2022-06-13 01:10:29.965410
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():

    mock_module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    mock_module.run_command = MagicMock(side_effect=[(0, "/tmp/prtconf.out", ""), (0, "/tmp/swap_s.out", "")])

    file_handle = open('/tmp/prtconf.out', 'w')
    file_handle.write("Memory size: 2048 Megabytes")
    file_handle.close()

    file_handle = open('/tmp/swap_s.out', 'w')
    file_handle.write("swapfile          dev  swaplo blocks   free")
    file_handle.close()

    h = SunOSHardware(mock_module)
    m = h.get_memory_facts()


# Generated at 2022-06-13 01:10:40.211304
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    module = DummyAnsibleModule()
    hardware = SunOSHardware(module)

    # set up a fake kstat output

# Generated at 2022-06-13 01:10:42.954631
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    facts = {
        'platform': 'SunOS',
    }

    SunOSHWFactCollector = SunOSHardwareCollector(facts=facts)
    assert SunOSHWFactCollector._platform == 'SunOS'
    assert SunOSHWFactCollector._fact_class is SunOSHardware

# Generated at 2022-06-13 01:10:50.838309
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    sun_hw = SunOSHardware(module)


# Generated at 2022-06-13 01:10:54.764567
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    facts = SunOSHardware().get_cpu_facts()
    assert isinstance(facts['processor'], list)
    assert isinstance(facts['processor_cores'], int)
    assert isinstance(facts['processor_count'], int)


# Generated at 2022-06-13 01:11:04.434542
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.facts import Facts
    import ansible.module_utils.facts.hardware.sunos
    import ansible.module_utils.facts.hardware.base
    import ansible.module_utils.facts.timeout

    facts = Facts()
    facts = ansible.module_utils.facts.hardware.sunos.SunOSHardware().populate(facts)
    facts = ansible.module_utils.facts.hardware.base.Hardware().populate(facts)

    assert facts['uptime_seconds'] == 10

    # Verifying that the generate_mount_facts function is called
    # marking this function as a side_effect
    def fake_run_command(command):
        return 0, 'Mounted on /mnt/dummy', ''
    ansible.module_utils.facts.timeout.run

# Generated at 2022-06-13 01:11:51.188218
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware_facts = SunOSHardware()

    # Mock the run_command method to return the output of /usr/sbin/prtconf
    def mock_run_command(module, cmd):
        if cmd == ['/usr/sbin/prtconf']:
            out = """System Configuration: Oracle Corporation  Sun Fire X4270

            Memory size: 16384 Megabytes
            """
            return (0, out, '')
        return (0, '', '')

    hardware_facts.module.run_command = mock_run_command
    hardware_facts.module.get_bin_path = mock_run_command

    # Manually call the method used to set system_vendor and product_name facts
    hardware_facts.get_dmi_facts()

    # Assert the keys are present and valid

# Generated at 2022-06-13 01:11:59.454037
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command_environ_update = {}

        def run_command(self, command, in_data=None, check_rc=True):
            if command[-1] == 'prtconf':
                return (0, """
Memory size: 64 Megabytes
""", '')
            elif command[-1] == 'swap -s':
                return (0, """
total: 20480k bytes allocated + 20480k reserved = 40960k used, 4194176k available
""", '')

        def get_bin_path(self, arg, opt_dirs=[]):
            return arg

    hardware = SunOSHardware(MockModule())
    facts = hardware.populate()

# Generated at 2022-06-13 01:12:07.731227
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:12:08.422251
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    pass

# Generated at 2022-06-13 01:12:15.877071
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = object()
    hardware = SunOSHardware(module)
    result = hardware.populate()
    assert 'processor' in result
    assert 'memtotal_mb' in result
    assert 'swapfree_mb' in result
    assert 'swaptotal_mb' in result
    assert 'swap_allocated_mb' in result
    assert 'swap_reserved_mb' in result
    assert 'system_vendor' in result
    assert 'product_name' in result
    assert 'devices' in result
    assert 'devices' in result['devices']
    assert 'uptime_seconds' in result

# Generated at 2022-06-13 01:12:18.911359
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardware_collector = SunOSHardwareCollector()
    assert hardware_collector
    assert hardware_collector._fact_class == SunOSHardware
    assert hardware_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:12:30.597594
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec=dict())
    test_module.run_command = MagicMock(return_value=(0,'module:     sun4v    implementation:  sun cpu     clock_MHz:  24000    chip_id:   0    cpu_type:  sunw,UltraSPARC-T2\nmodule:     sun4v    implementation:  sun cpu     clock_MHz:  24000    chip_id:   1    cpu_type:  sunw,UltraSPARC-T2\n',''))
    hardware = SunOSHardware(module=test_module)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == ['sunw,UltraSPARC-T2 @ 24000MHz','sunw,UltraSPARC-T2 @ 24000MHz']
    assert cpu_facts

# Generated at 2022-06-13 01:12:37.440855
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    '''
    Testing a normal output of command: prtconf | grep 'Memory size'
    The expected output is:  Memory size: 8192 Megabytes
    '''
    facts = SunOSHardware()
    facts.module = AnsibleModuleMock()
    facts.module.run_command = mock.MagicMock(return_value=["", "Memory size: 8192 Megabytes", ""])
    assert facts.get_memory_facts() == {'memtotal_mb': 8192, 'swapfree_mb': 'NA', 'swaptotal_mb': 'NA',
                                        'swap_allocated_mb': 'NA', 'swap_reserved_mb': 'NA'}


# Generated at 2022-06-13 01:12:48.755257
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    fake_module = object()

# Generated at 2022-06-13 01:12:53.641043
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = type('AnsibleModule', (), {})
    module.run_command = lambda *args, **kwargs: (0, "Memory size: 6116576 KB", "")
    hardware_obj = SunOSHardware(module)
    memory_facts = hardware_obj.get_memory_facts()
    assert memory_facts.get('memtotal_mb') == 5968


# Generated at 2022-06-13 01:13:38.688560
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # a class to receive the collected facts
    class CollectedFacts:
        ansible_processor = 'i86pc'
        ansible_machine = 'i86pc'

    # empty content of /usr/sbin/kstat cpu_info output
    cpu_info_output = ''
    # instance of class SunOSHardware
    sunos = SunOSHardware({'module_setup': True}, collected_facts=CollectedFacts())
    # output of method get_cpu_facts when /usr/sbin/kstat cpu_info output is empty
    output_empty_cpu_info_output = sunos.get_cpu_facts(sunos.collected_facts)
    assert output_empty_cpu_info_output == {'processor': [], 'processor_cores': 'NA', 'processor_count': 0}
    # content of /usr

# Generated at 2022-06-13 01:13:43.684719
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = DummyModule()
    sunos_hw = SunOSHardware(module)
    sunos_hw.populate()
    assert module.exit_args['failed'] is False


# Generated at 2022-06-13 01:13:49.916839
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Create a test instance of the SunOSHardware class.
    sunos_hw = SunOSHardware({})

    # Invoke populate on the test instance and return the result.
    return sunos_hw.populate()

if __name__ == '__main__':
    # If executed as a script, print the result of method populate of
    # class SunOSHardware.
    print(test_SunOSHardware_populate())

# Generated at 2022-06-13 01:13:59.243353
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)


# Generated at 2022-06-13 01:14:10.037507
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = MagicMock()
    module.run_command.return_value = (None, "fake_output", None)

    sunos = SunOSHardware(module)
    result = sunos.populate()


# Generated at 2022-06-13 01:14:13.112329
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    HardwareCollector.collectors['SunOS'] = SunOSHardwareCollector()
    SunOSHardwareCollector.populate(collected_facts={'platform': 'SunOS'}, validate_certs=False)

# Generated at 2022-06-13 01:14:18.207773
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    """Tests for the method get_uptime_facts of the SunOSHardware class."""
    # Initialize the class
    sha = SunOSHardware()
    # Set the uptime_seconds to a dummy value
    uptime_old = sha.facts['uptime_seconds']

    # Call the get_uptime_facts method
    uptime_facts = sha.get_uptime_facts()
    # Check if the returned values
    assert uptime_facts['uptime_seconds'] > uptime_old

# Generated at 2022-06-13 01:14:26.375731
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:14:27.775619
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    facts = {}
    collector = SunOSHardwareCollector(facts)
    assert collector.fact_class == SunOSHardware

# Generated at 2022-06-13 01:14:34.178095
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hardware_facts = SunOSHardware()
    collected_facts = {'ansible_machine': 'asdf'}