

# Generated at 2022-06-13 01:06:36.344056
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={
        },
        supports_check_mode=True)

    # Mock the run_command method
    module_run_command = module.run_command

    def run_command(cmd, check_rc=True):
        return (0, 'Memory size: 8192 Megabytes', '')

    module.run_command = run_command

    # Mock the get_file_content method
    module_get_file_content = module.get_file_content

    def get_file_content(file_path):
        return 'swapfile\t-\t/var/run\ttmpfs\t-\tswap\t-\tyes\t-\n'

    module.get_file_content = get_file_content

    hardware = SunOSHardware(module)

    #

# Generated at 2022-06-13 01:06:44.488261
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModuleMock()
    kstatMock = AnsibleCmdMock('/usr/bin/kstat -p unix:0:system_misc:boot_time', 0, 'unix:0:system_misc:boot_time    1548249689\n')
    module.run_command = kstatMock.run

    sun_hw = SunOSHardware(module)

    uptime_facts = sun_hw.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 1548249689

# Generated at 2022-06-13 01:06:55.990289
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    sunos_hardware_instance = SunOSHardware()
    # Expected output
    expected_cpu_facts = {
  'processor': ['SUNW,SPARC-Enterprise', 'SUNW,SPARC-Enterprise'],
  'processor_cores': NA,
  'processor_count': 2
}
    # Expected input

# Generated at 2022-06-13 01:06:58.454860
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    m = SunOSHardware()
    uptime_facts = m.get_uptime_facts()
    assert type(uptime_facts['uptime_seconds']) is int

# Generated at 2022-06-13 01:07:02.855705
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    import time
    module = AnsibleModuleMock()
    sunos_hw = SunOSHardware(module=module)
    time.sleep(1)
    uptime_seconds = sunos_hw.get_uptime_facts()['uptime_seconds']
    # get_uptime_facts() is dependent on the duration of time.sleep() to get uptime_seconds for the test assertion
    assert uptime_seconds > 0 and uptime_seconds < 2

# Generated at 2022-06-13 01:07:13.369435
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:07:22.562524
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    p = SunOSHardware()
    test_facts = {
        "ansible_processor": [
            "SUNW,SPARC-Enterprise",
            "SUNW,UltraSPARC-IIe"
        ],
        "product_name": "SUNW,SPARC-Enterprise",
        "system_vendor": "SUNW,SPARC-Enterprise",
    }
    res = p.populate(test_facts)

    assert 'swap_reserved_mb' in res
    assert 'swap_allocated_mb' in res

# Generated at 2022-06-13 01:07:28.957730
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = type('', (), {'run_command': lambda x: (0, ' unix:0:system_misc:boot_time    1548249689', '')})()
    uptime_facts = SunOSHardware(module).get_uptime_facts()

    assert uptime_facts
    assert uptime_facts.get('uptime_seconds', False) is not False

# Generated at 2022-06-13 01:07:33.429583
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModuleMock()

    cpu_facts = SunOSHardware(module).get_cpu_facts()

    expected_cpu_facts = {
        'processor': ['SUNW,SPARC-Enterprise'],
        'processor_count': 1,
        'processor_cores': 8
    }

    assert cpu_facts == expected_cpu_facts


# Generated at 2022-06-13 01:07:44.654943
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class MockModule(object):
        def __init__(self, boot_time):
            self.boot_time = boot_time
            self.run_command_count = 0
            self.run_command_rc = 0

        def run_command(self, cmd, check_rc=True):
            rc = self.run_command_rc
            self.run_command_count += 1
            if cmd == ['/usr/bin/kstat', '-p', 'unix:0:system_misc:boot_time']:
                out = "unix:0:system_misc:boot_time    %d\n" % self.boot_time
                return rc, out, ""
            else:
                raise Exception("unknown command")

    # Case 1, boot_time = 1548220831
    #   uptime_seconds = $

# Generated at 2022-06-13 01:08:09.667372
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """Unit test for method get_cpu_facts of class SunOSHardware.

    NOTE: This test only looks for the processor_count and processor_cores facts
    for simplicity.
    """
    expected = {'processor_count': 1, 'processor_cores': 1}

    hardware = SunOSHardware()
    hardware.module = FakeModule()
    hardware.module.run_command = MagicMock(return_value=(0, '', ''))

    actual = hardware.get_cpu_facts()

    # Compare the two results
    assert (expected['processor_count'] == actual['processor_count']) and \
           (expected['processor_cores'] == actual['processor_cores'])

# Generated at 2022-06-13 01:08:12.314744
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hardware_mock = SunOSHardware(dict())

    # mock the run_command method of the SunOSHardware class

# Generated at 2022-06-13 01:08:14.443138
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = None
    SunOSHardware.get_dmi_facts(module)  # noqa

# Generated at 2022-06-13 01:08:25.724693
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    get_device_facts = SunOSHardware.get_device_facts


# Generated at 2022-06-13 01:08:37.819098
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:08:44.540531
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware_facts = SunOSHardware().populate()
    assert hardware_facts['system_vendor'] == 'VMware, Inc.'
    assert hardware_facts['product_name'] == 'Standard PC'
    assert hardware_facts['processor'] == [u'Genuine Intel(R) CPU @ 2.00GHz']
    assert hardware_facts['processor_cores'] == 2
    assert hardware_facts['processor_count'] == 1
    assert hardware_facts['memtotal_mb'] == 1008
    assert hardware_facts['swapfree_mb'] == 1023
    assert hardware_facts['swap_reserved_mb'] == 0
    assert hardware_facts['swap_allocated_mb'] == 0
    assert hardware_facts['devices']['sda']['product'] == 'VBOX HARDDISK'

# Generated at 2022-06-13 01:08:56.187128
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    """
    Test the get_memory_facts method of SunOSHardware
    :return:
    """

    # used to store the instance of SunOSHardware class
    testObj = SunOSHardware()
    _, out, _ = testObj.module.run_command("echo 'Memory size: 8192 Megabytes\n' \
                                           && echo 'Swap\tresv\tfree\t\talloc\tfree' \
                                           && /usr/sbin/swap -s | /usr/bin/tail -1")
    expected_out = {'memtotal_mb': 8192, 'swapfree_mb': 5801, 'swaptotal_mb': 7440,
                    'swap_allocated_mb': 1638, 'swap_reserved_mb': 1638}

    assert testObj.get_memory_

# Generated at 2022-06-13 01:09:08.418519
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:09:17.139325
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # Setup
    hardware_module_params = {
        'module_utils': 'ansible.module_utils.facts.hardware.sunos',
        'run_command': run_command
    }
    prtconf_output = """Memory size: 16384 Megabytes"""
    swap_output = """swapfile             dev  swaplo blocks   free
/dev/zvol/dsk/rpool/swap        32,2      16  2097148   71628"""
    commands = (prtconf_output, swap_output)

    def run_command(command, module):
        if command == 'prtconf':
            return (0, commands[0], None)
        elif command == 'swap':
            return (0, commands[1], None)

# Generated at 2022-06-13 01:09:23.475510
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware()
    hardware.module = module
    facts = hardware.get_memory_facts()
    assert facts['swaptotal_mb'] is not None
    assert facts['swapfree_mb'] is not None
    assert facts['swap_allocated_mb'] is not None
    assert facts['swap_reserved_mb'] is not None

# Generated at 2022-06-13 01:09:58.794698
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():

    class module():
        def run_command(self, cmd):
            return 0, "System Configuration: Sun Microsystems  sun4u", ""

    class mySunOSHardware(SunOSHardware):
        module = module()

    output = {'system_vendor': 'Sun Microsystems', 'product_name': 'sun4u'}
    obj = mySunOSHardware()
    assert obj.get_dmi_facts() == output

# Generated at 2022-06-13 01:10:07.092497
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'unix:0:system_misc:boot_time    1548249721', ''))
    sunos_hardware = SunOSHardware(module=module)
    result = sunos_hardware.get_uptime_facts()

    module.run_command.assert_called_once_with('/usr/bin/kstat -p unix:0:system_misc:boot_time')
    assert result == {'uptime_seconds': int(time.time() - 1548249721)}

# Generated at 2022-06-13 01:10:12.844932
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    h = SunOSHardware()
    memory_facts = h.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swap_allocated_mb' in memory_facts
    assert 'swap_reserved_mb' in memory_facts

# Generated at 2022-06-13 01:10:16.068085
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)
    memory_facts = hardware.get_memory_facts()
    module.exit_json(ansible_facts={'memory_facts': memory_facts})


# Generated at 2022-06-13 01:10:17.920071
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hardware = SunOSHardware(None)

    facts = hardware.get_cpu_facts()

    assert 'processor' in facts



# Generated at 2022-06-13 01:10:29.387592
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = FakeAnsibleModule()
    hardware = SunOSHardware(module)


# Generated at 2022-06-13 01:10:39.691137
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Create a test class object
    sunos_facts = SunOSHardware(None, 0)

    # Set the out and err output

# Generated at 2022-06-13 01:10:44.834676
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    import sys
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import Mock, patch
    from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.sunos import SunOSHardware

    class TestHardware(SunOSHardware):

        def populate(self, collected_facts=None):
            return collected_facts

    class TestSunOSHardware(unittest.TestCase):
        def setUp(self):
            self.sunosHardware = TestHardware(dict())


# Generated at 2022-06-13 01:10:47.646277
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardware_collector = SunOSHardwareCollector()
    assert hardware_collector._platform == 'SunOS'
    assert hardware_collector._fact_class == SunOSHardware
    assert hardware_collector.required_facts == set(['platform'])

# Generated at 2022-06-13 01:10:54.629124
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()
    hardware.module = object()
    fact_output = {'product_name': 'SUNW,Ultra-4', 'system_vendor': 'Oracle Corporation'}
    hardware.module.run_command = lambda cmd: (0, 'System Configuration:\t\tOracle Corporation SUNW,Ultra-4', '')
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts == fact_output
    return


# Generated at 2022-06-13 01:12:00.314022
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardware_collector = SunOSHardwareCollector()

    assert hardware_collector.required_facts == set(['platform'])
    assert hardware_collector._platform == 'SunOS'



# Generated at 2022-06-13 01:12:07.946695
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()
    out_mock = ('System Configuration: VMware, Inc. All rights reserved. VMware Virtual Platform\nv.vishal123')
    rc_mock = 0
    prtdiag_mock = ['/usr/bin/prtdiag']
    err_mock = ''

    dmi_facts = hardware.get_dmi_facts(out_mock, rc_mock, prtdiag_mock, err_mock)
    assert dmi_facts == {'system_vendor': 'VMware, Inc.', 'product_name': 'v.vishal123'}

    out_mock = ('System Configuration: QEMU Standard PC (i440FX + PIIX, 1996)')

# Generated at 2022-06-13 01:12:11.822971
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    facts = {}

    # create a class instance of SunOSHardware
    sunos_hw = SunOSHardware(facts)
    sunos_hw.module = AnsibleModule(argument_spec={})

    sunos_hw.populate()

# Generated at 2022-06-13 01:12:19.156181
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """Test the get_cpu_facts method of SunOSHardware"""

    # Setup
    module_mock = Mock()
    module_mock.run_command = MagicMock()
    module_mock.run_command.return_value = (0, TEST_CPUINFO, '')
    hardware_instance = SunOSHardware(module_mock)
    expected_facts = {
        'processor': [
            'ARMv7 Processor rev 1 (v7l) @ 1000MHz', 'ARMv7 Processor rev 1 (v7l) @ 1000MHz'],
        'processor_count': 2,
        'processor_cores': 2,
    }

    # Test
    cpu_facts = hardware_instance.get_cpu_facts()

    # Assert
    assert cpu_facts == expected_facts


# Generated at 2022-06-13 01:12:30.868890
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    m = SunOSHardware({})

    # Test Solaris 8
    dmi = ('System Configuration: Sun Microsystems sun4u\n'
           'Memory size: 65536 Megabytes\n'
           '\n'
           '=========================== CPUs =============================\n'
           '         Run Ecache CPU CPU Temperature Temperature\n'
           'CPUs Mb  MHz State   Impl. Mask    Boards       Cpu   Cpu\n'
           '--- -- ----- ------ ------ --- ----------- ------ ------\n'
           '0   16  1200 1      US-III  2,3,4,5      1       37    39\n'
           '1   16  1200 1      US-III  2,3,4,5      1       38    37\n')


# Generated at 2022-06-13 01:12:38.557818
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """ returns cpu facts """

    expected_output = ['Intel(r) Xeon(r) CPU E5-2699 v3 @ 2.30GHz']
    module = MockModule()
    module.run_command = Mock(return_value=(0, kstat_output, ''))
    hw = SunOSHardware(module)
    cpu_facts = hw.get_cpu_facts()

    assert cpu_facts['processor'] == expected_output
    assert cpu_facts['processor_cores'] == 24
    assert cpu_facts['processor_count'] == 2



# Generated at 2022-06-13 01:12:49.756000
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    import mock

    # Mock the module and return an instance of class Hardware
    mock_module = mock.Mock()

# Generated at 2022-06-13 01:12:58.686842
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """ Unit test for method get_device_facts of class SunOSHardware """
    facts = {'system_vendor': None, 'product_name': None, 'uptime_seconds': None, 'swaptotal_mb': 0, 'mounts': [], 'memtotal_mb': 0, 'devices': {}, 'processor_count': 4, 'swapfree_mb': 0, 'swap_reserved_mb': 0, 'processor_cores': 4, 'processor': ['Genuine Intel(R) CPU 0000 @ 2.00GHz'], 'swap_allocated_mb': 0}

    module = MockModule()

    hardware = SunOSHardware(module)
    hardware.populate(facts)
    device_facts = hardware.get_device_facts()

    assert len(device_facts.keys()) == 2
    assert 'devices' in device

# Generated at 2022-06-13 01:13:00.362312
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware_instance = SunOSHardware({})
    facts = hardware_instance.get_dmi_facts()
    assert type(facts) == dict

# Generated at 2022-06-13 01:13:07.832116
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    m = SunOSHardware(dict())

    # platform_sbin = '/usr/platform/' + platform.rstrip() + '/sbin'
    # prtdiag_path = self.module.get_bin_path("prtdiag", opt_dirs=[platform_sbin])

# Generated at 2022-06-13 01:15:36.407916
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardware_collector = SunOSHardwareCollector()
    assert hardware_collector.platform == 'SunOS'

# Generated at 2022-06-13 01:15:39.537575
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    class mock_module:
        @staticmethod
        def run_command(command):
            return 0, "Memory size: 32768 Megabytes\n", ""
    result = SunOSHardware.get_memory_facts(mock_module)
    assert result['memtotal_mb'] == 32768



# Generated at 2022-06-13 01:15:41.375986
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    x=SunOSHardware()
    device_facts = x.get_device_facts()
    assert device_facts['devices']['sd0']['product'] == 'VBOX HARDDISK'

# Generated at 2022-06-13 01:15:49.640904
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts.utils import ansible_facts
    from ansible.module_utils import common

    mock_module = common.AnsibleModule(argument_spec={}, supports_check_mode=False)
    mock_module.run_command = lambda x: (0, 'spam', '')

    mock_module.run_command_environ_update = {
        'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'
    }

    facts_collector = FactsCollector(mock_module)
    facts_collector.collect(['hardware'])

    # Make sure the processor information

# Generated at 2022-06-13 01:15:54.046778
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=False
    )

    mem_facts = SunOSHardware(module).get_memory_facts()
    assert "memtotal_mb" in mem_facts

# Generated at 2022-06-13 01:16:02.380268
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:16:03.451659
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = None
    SunOSHardware.get_dmi_facts(module)

# Generated at 2022-06-13 01:16:11.318725
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """
    Unit test for SunOSHardware.get_device_facts()
    """
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    # Mock data for get_device_facts input