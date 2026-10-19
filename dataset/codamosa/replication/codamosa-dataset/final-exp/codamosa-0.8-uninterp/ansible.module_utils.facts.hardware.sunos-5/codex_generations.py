

# Generated at 2022-06-13 01:06:36.067598
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    set_module_args(dict())

    class UptimeFakeModule(object):
        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/kstat'

        def run_command(self, *args, **kwargs):
            return (0, "unix:0:system_misc:boot_time    1548249689", "")

    sunos = SunOSHardware(UptimeFakeModule())
    uptime_facts = sunos.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] == int(time.time() - 1548249689)

# Generated at 2022-06-13 01:06:47.889457
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hw = SunOSHardwareCollector()
    collected_facts = {'ansible_machine': 'i86pc'}
    hw_facts = hw.populate(collected_facts)

    assert hw_facts['processor_cores'] != 'NA'
    assert hw_facts['system_vendor']
    assert hw_facts['product_name']
    assert hw_facts['devices']
    assert hw_facts['devices']['sd0']['product']
    assert hw_facts['devices']['sd0']['size']
    assert hw_facts['devices']['sd0']['vendor']
    assert hw_facts['devices']['sd0']['revision']
    assert hw_facts['devices']['sd0']['serial']

# Generated at 2022-06-13 01:06:56.037242
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # Instantiate a mock module
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # Instantiate a SunOSHardware object
    s = SunOSHardware(module)

    rc = 0
    out = 'unix:0:system_misc:boot_time    1548249689'
    err = ''

    # Get dict of uptime facts
    facts = s.get_uptime_facts(rc, out, err)

    # Assert that the dict of uptime facts is not empty
    assert not len(facts) == 0

# Generated at 2022-06-13 01:07:07.919106
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:07:19.593588
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = MockModule()

    # Test for Oracle VM
    module.run_command = Mock(return_value=(0, 'QEMU Virtual CPU version 2.5+', ''))
    hardware = SunOSHardware(module)
    assert hardware.get_dmi_facts() == {'system_vendor': 'QEMU', 'product_name': 'Virtual CPU version 2.5+'}

    # Test for Solaris KVM
    module.run_command = Mock(return_value=(0, 'Oracle Corporation sun4v', ''))
    hardware = SunOSHardware(module)
    assert hardware.get_dmi_facts() == {'system_vendor': 'Oracle Corporation', 'product_name': 'sun4v'}

    # Test for Solaris LDOM

# Generated at 2022-06-13 01:07:24.426495
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['system_vendor'] == "Sun Microsystems"
    assert dmi_facts['product_name'] == "SUNW,Sun-Fire-V440"

# Generated at 2022-06-13 01:07:34.870713
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    This test verifies if the SunOSHardware.populate method works.
    For this test to  work properly, the file /etc/mnttab should be mocked.
    """
    module = MockModule()
    hardware = SunOSHardware(module)
    module.run_command = MockRunCommand()
    hardware.get_cpu_facts = MockGetCpuFacts()
    hardware.get_mount_facts = MockGetMountFacts()
    hardware.get_dmi_facts = MockGetDmiFacts()
    hardware.get_device_facts = MockGetDeviceFacts()
    hardware.get_uptime_facts = MockGetUptimeFacts()

    # mocking wire call
    hardware.collect_wireless_facts = MockCollectWirelessFacts()

    facts = hardware.populate()


# Generated at 2022-06-13 01:07:45.268226
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # mock module
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    module = basic.AnsibleModule(argument_spec={})
    module.run_command = lambda *args, **kwargs: (0, to_bytes('Fujitsu T5120\n'), None)
    module.run_command_environ_update = {}

    # set platform to SunOS
    module.facts = {'platform': 'SunOS'}

    # create SunOSHardware instance and get cpu facts
    sunos_facts = SunOSHardware(module).get_cpu_facts()

    # assert cpu facts
    assert sunos_facts['processor'] == ['Fujitsu T5120']
    assert sunos_facts['processor_cores'] == 1

# Generated at 2022-06-13 01:07:51.639350
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # Test for get_memory_facts() method of SunOSHardware
    # Test for normal input
    module = AnsibleModule(argument_spec={'gather_subset': {'type': 'list'}})
    module.params['gather_subset'] = ['!all', 'min']
    hw_obj = SunOSHardware(module)
    facts_dict = hw_obj.populate()
    assert facts_dict is not None
    if 'memtotal_mb' in facts_dict:
        assert facts_dict['memtotal_mb'] >= 0
    else:
        assert 'memtotal_mb' in facts_dict
    if 'swapfree_mb' in facts_dict:
        assert facts_dict['swapfree_mb'] >= 0
    else:
        assert 'swapfree_mb' in facts_dict

# Generated at 2022-06-13 01:07:57.910927
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():

    mock_an_module = type('AnsibleModule', (object,), {
        'run_command': lambda self, args: (0, 'unix:0:system_misc:boot_time 1548249689', ''),
        })()
    fact = SunOSHardware()

    fact.module = mock_an_module
    uptime = fact.get_uptime_facts()
    assert uptime['uptime_seconds'] == 1548249689

# Generated at 2022-06-13 01:08:19.877048
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    uptime_facts = {}
    expected_uptime_facts = {'uptime_seconds': 1}

    try:
        s = SunOSHardware()
        setattr(s, 'module', MockDiskModule('kstat', 'unix:0:system_misc:boot_time', rc=0, out='1548249688'))
        uptime_facts = s.get_uptime_facts()
    except Exception:
        pass

    assert uptime_facts == expected_uptime_facts


import unittest

# Generated at 2022-06-13 01:08:23.829381
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    data = {
        'ansible_architecture': 'sparc64',
        'ansible_machine': 'sun4u',
    }

    result = {
        'processor': ['SPARC32plus @ 200MHz'],
        'processor_cores': 'NA',
        'processor_count': 1,
    }

    h = SunOSHardware(data)
    assert result == h.get_cpu_facts()

# Generated at 2022-06-13 01:08:28.026821
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware = SunOSHardware({})
    hardware.module.run_command = lambda args: (0, '', '')

    hardware.populate()

    expected = {
        'devices': {},
        'memtotal_mb': 0,
        'processor': [],
        'processor_cores': 'NA',
        'processor_count': 0,
        'swap_allocated_mb': 0,
        'swap_reserved_mb': 0,
        'swaptotal_mb': 0,
        'swapfree_mb': 0,
        'uptime_seconds': None,
    }

    assert hardware.facts == expected, "'test_SunOSHardware_populate' failed"

# Generated at 2022-06-13 01:08:39.612806
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:08:45.585659
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class KstatMock:
        def __init__(self):
            self.cmd = None
            self.cmd_results = []

        def run_command(self, cmd):
            self.cmd = cmd
            return self.cmd_results.pop(0)

    # Create object to be tested
    sun_hw = SunOSHardware()
    # Mock the run_command method
    sun_hw.module = KstatMock()

    # Assume we get the following output from kstat

# Generated at 2022-06-13 01:08:48.900363
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    f = SunOSHardware()
    uptime_facts = f.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] >= 0

# Generated at 2022-06-13 01:08:57.786742
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    module.run_command = Mock()
    module.run_command.side_effect = [
        (0, 'Memory size: 8192 Megabytes', ''), # prtconf -v
        (0, 'Total swap space:  4095 Megabytes', ''), # swap -s
    ]

    hw = SunOSHardware()
    facts = hw.populate()

    assert facts['memtotal_mb'] == 8192
    assert facts['swaptotal_mb'] == 4095
    assert facts['swapfree_mb'] == 4095
    assert facts['swap_allocated_mb'] == 0
    assert facts['swap_reserved_mb'] == 0



# Generated at 2022-06-13 01:09:09.135081
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    """
    This is the unittest function for SunOSHardware method get_memory_facts.
    The test is invoked by invoking the method "test_SunOSHardware_get_memory_facts"
    :return:
    """
    class moduleMock(object):
        """
        This class is used to mock the module object that is passed to the remove_facts
        method.
        """
        class __specific__:
            """
            This class is used to mock the module object's ansible_facts
            attribute.
            """
            @staticmethod
            def get(param=None):
                """
                This is the mock implementation of the get method for ansible_facts dictionay
                :param param: This attribute is ignored for the mock implementation
                :return: None
                """
                return None

        ansible_facts = __specific__()

       

# Generated at 2022-06-13 01:09:14.839405
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    import sys
    if sys.version_info[0] >= 3:
        from io import StringIO
    else:
        from StringIO import StringIO

    bot = SunOSHardware()
    rc = 0
    out = """Memory size: 8192 Megabytes
"""
    err = ''

    bot.module.run_command = lambda x: (rc, out, err)

    facts = bot.get_memory_facts()
    assert facts['memtotal_mb'] == 8192

# Generated at 2022-06-13 01:09:28.054645
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    # Utility code for unit testing of populate
    # Without this every unit test must reimplement this
    import sys

    class MockModule(object):
        def __init__(self):
            self.run_command_called = False
            self.run_command_rc = 0
            self.run_command_out = ''
            self.run_command_err = ''
            self.run_command_environ_update = {}
            self.run_command_kwargs = {}

        def get_bin_path(self, arg, opt_dirs=[]):
            if arg == "prtdiag":
                return "/usr/sbin/prtdiag"


# Generated at 2022-06-13 01:09:53.135363
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    sunos_hardware = SunOSHardware()
    collected_facts = {}
    fact_data = sunos_hardware.populate(collected_facts)

    assert 'processor' in fact_data
    assert fact_data['processor'] != []
    assert 'memtotal_mb' in fact_data
    assert fact_data['memtotal_mb'] >= 0
    assert 'swapfree_mb' in fact_data
    assert fact_data['swapfree_mb'] >= 0
    assert 'swaptotal_mb' in fact_data
    assert fact_data['swaptotal_mb'] >= 0
    assert 'swap_allocated_mb' in fact_data
    assert fact_data['swap_allocated_mb'] >= 0
    assert 'swap_reserved_mb' in fact_data
    assert fact_data

# Generated at 2022-06-13 01:09:58.311040
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():

    m = SunOSHardware()
    r = m.get_memory_facts()

    assert r['memtotal_mb'] == 131072
    assert r['swaptotal_mb'] == 0
    assert r['swapfree_mb'] == 0
    assert r['swap_reserved_mb'] == 0
    assert r['swap_allocated_mb'] == 0

# Generated at 2022-06-13 01:10:03.448666
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)

    cmd = ['/usr/bin/kstat', '-p']
    for ds in hardware.get_device_facts()['devices'].values()[0].keys():
        cmd.append('sderr:::%s' % ds)

    rc, out, err = module.run_command(cmd)
    assert rc == 0
    assert out != ''

# Generated at 2022-06-13 01:10:13.940934
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = FakeAnsibleModule()
    module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}

    hw = SunOSHardware(module)
    memory_facts = hw.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4294967296
    assert memory_facts['swapfree_mb'] == 0
    assert memory_facts['swaptotal_mb'] == 0
    assert memory_facts['swap_allocated_mb'] == 1024
    assert memory_facts['swap_reserved_mb'] == 2048


# Generated at 2022-06-13 01:10:18.941497
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware(None)
    dmi_facts = hardware.get_dmi_facts()

    # Product name and vendor of an example system, should be matched
    # by get_dmi_facts.
    dmi_facts_test = {
        'system_vendor': 'Oracle Corporation',
        'product_name': 'Sun Fire X4170'
    }
    assert dmi_facts == dmi_facts_test

# Generated at 2022-06-13 01:10:30.459417
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    hardware = SunOSHardware(module)
    hardware.populate()

# Generated at 2022-06-13 01:10:40.635206
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:10:48.664914
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    class MockModule():
        class MockResults():
            def __init__(self, out, rc):
                self.rc = rc
                self.stdout = out
        def __init__(self):
            self.run_command_results = []
            self.run_command_called = []
        def run_command(self, args, check_rc=True):
            self.run_command_called.append(args)
            return self.run_command_results.pop(0)

    module = MockModule()
    module.run_command_results = [
        MockModule.MockResults(
'''Memory size: 8192 Megabytes

''', 0)
    ]

    hardware = SunOSHardware(module)

    facts_results = hardware.populate()

    assert facts_results['memtotal_mb'] == 8192


# Generated at 2022-06-13 01:11:00.117242
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    """ Validates that memory facts are correctly parsed.

        Unit tests are run with '-v' so ensure the
        output is formatted correctly.
    """
    # expected output from /usr/sbin/prtconf
    prtconf_out = """System Configuration:  Sun Microsystems  sun4u
Memory size: 16384 Megabytes
"""
    # expected output from /usr/sbin/swap -s
    swap_out = """total: 16779760k bytes allocated + 122252k reserved = 16892016k used, 33370820k available
"""
    module = type('', (), {})()
    setattr(module, '_run_command', lambda cmd: (0, prtconf_out, ''))
    setattr(module, 'run_command', lambda cmd: (0, swap_out, ''))


# Generated at 2022-06-13 01:11:02.545616
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock()
    cls = SunOSHardware(module)
    out = cls.populate()
    assert len(out) > 0

# Generated at 2022-06-13 01:11:46.804278
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    collector = SunOSHardwareCollector()
    assert collector.required_facts == set(['platform'])
    assert collector.platform == 'SunOS'
    assert collector.fact_class == SunOSHardware

if __name__ == '__main__':
    # Unit testing.
    test_SunOSHardwareCollector()

# Generated at 2022-06-13 01:11:48.834072
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    uptime_facts = {}
    uptime_facts['uptime_seconds'] = int(time.time())
    return uptime_facts

# Generated at 2022-06-13 01:11:53.489205
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    hardware = SunOSHardware()
    out = "unix:0:system_misc:boot_time    1548249689"
    uptime_seconds = int(time.time() - int(out.split('\t')[1]))
    result = hardware.get_uptime_facts()
    assert result['uptime_seconds'] == uptime_seconds

# Generated at 2022-06-13 01:12:01.188081
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModuleMock()
    module.run_command = MagicMock()

    mock_device_cmd_out = '''sderr:0:sd0,err:Product VBOX HARDDISK   9
sderr:0:sd0,err:Revision        1.0
sderr:0:sd0,err:Serial No       VB0ad2ec4d-074a
sderr:0:sd0,err:Size    53687091200
sderr:0:sd0,err:Vendor  ATA'''

    module.run_command.return_value = (0, mock_device_cmd_out, '')

    result = SunOSHardware(module).get_device_facts()

# Generated at 2022-06-13 01:12:05.550651
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    hardware = SunOSHardware()
    hardware.module = MagicMock()
    hardware.module.run_command = MagicMock()
    hardware.module.run_command.return_value = (1, "Memory size: 8192 Megabytes", "")

    # test the size of memtotal_mb
    assert hardware.get_memory_facts()['memtotal_mb'] == 8192


# Generated at 2022-06-13 01:12:09.415166
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardware_collector = SunOSHardwareCollector()
    assert hardware_collector.required_facts == set(['platform'])
    assert hardware_collector._platform == 'SunOS'
    assert hardware_collector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:12:14.911342
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware = SunOSHardware({})
    hardware_facts = hardware.populate()

    # This test is not comprehensive, just makes sure the
    # hardware facts that are added as part of this module work
    # as expected.

    assert hardware_facts['system_vendor'].startswith('Oracle Corporation')
    assert hardware_facts['product_name'] == 'SUNW,SPARC-Enterprise'

# Generated at 2022-06-13 01:12:18.037069
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)
    facts = hardware.get_memory_facts()
    assert 'memtotal_mb' in facts


# Generated at 2022-06-13 01:12:29.538824
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    facts = SunOSHardware({})

# Generated at 2022-06-13 01:12:31.920731
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    m = SunOSHardware({'ansible_facts': {'platform': 'SunOS'}})
    assert m.platform == 'SunOS'



# Generated at 2022-06-13 01:13:53.357895
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # Create a module object
    module = AnsibleModule(argument_spec={})
    # Create a SunOSHardware object
    obj = SunOSHardware()
    # Set get_memory_facts on module object
    obj.module = module

    # Create two variables to test the method
    prtconf_response = "Memory size: 20480 Megabytes"
    swap_s_response = "             total:        12288    used:             0\
     available:        12288"

    # Create a module return value object
    class Return:
        rc = 0
        stdout = ''
        stderr = ''

    return_value1 = Return()
    return_value1.stdout = prtconf_response
    return_value2 = Return()
    return_value2.stdout = swap_s_response

    # Set module run_command

# Generated at 2022-06-13 01:14:02.163140
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    """
    Tests method get_dmi_facts.
    This test requires that the Solaris machine being tested has a vendor
    and a product name in the output of /usr/sbin/prtdiag.
    """
    sunos_hardware = SunOSHardware()
    out = """System Configuration: Sun Microsystems  sun4u
Sun Fire V210/V240, No Keyboard
OpenBoot 4.30.0, 4096 MB memory installed, Serial #52112194.
Ethernet address 0:3:ba:26:d4:8f, Host ID: 8326d48f."""
    sunos_hardware.module.run_command.return_value = (0, out, '')

# Generated at 2022-06-13 01:14:11.403213
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = None
    fact = SunOSHardware(module)
    # Reference variables
    out = 'System Configuration: Sun Microsystems sun4u'
    vendor = 'Sun Microsystems'
    product = 'sun4u'

    # If you know of any other manufacturers whose names appear in
    # the first line of prtdiag's output, please add them here:
    vendors = [
        "Fujitsu",
        "Oracle Corporation",
        "QEMU",
        "Sun Microsystems",
        "VMware, Inc.",
    ]
    vendor_regexp = "|".join(map(re.escape, vendors))

# Generated at 2022-06-13 01:14:19.267821
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class MockModule():
        def __init__(self):
            self.run_command = MagicMock(return_value=(0, """
System Configuration: Sun Microsystems sun4u Sun Fire V440
Memory size: 4194304 Megabytes
System Peripherals (Software Nodes):
SUNW,UltraSPARC-IV+
System clock frequency: 1000 MHz
--------------------------------------------------------------------------
""", ''))
            self.get_bin_path = MagicMock()
            self.params = {'timeout': 10}
            self.module_args = {'timeout': 10}
            self.name = 'mock'

    class MockHardware(SunOSHardware):
        def __init__(self):
            self.module = MockModule()

    hw = MockHardware()
    dmi_facts = hw.get_dmi_facts()

# Generated at 2022-06-13 01:14:20.902795
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    sh = SunOSHardware()
    uptime_facts = sh.get_uptime_facts()
    assert 'uptime_seconds' in uptime_facts

# Generated at 2022-06-13 01:14:29.389623
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.check_mode = False
            self.run_command_results = [0, '', '']
            self.run_command_calls = []
            self.get_bin_path_results = [0, '/usr/bin/kstat', '']
            self.get_bin_path_calls = []

        def run_command(self, args, check_rc=True, environ_update=None):
            self.run_command_calls.append(args)
            return self.run_command_results

        def get_bin_path(self, arg, opt_dirs=None):
            self.get_bin_path_calls.append((arg, opt_dirs))
            return self.get_bin

# Generated at 2022-06-13 01:14:38.724682
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    # Create mock module
    class MockModule(object):
        def __init__(self):
            self.run_command_results = {}
            self.run_command_environ_update = None

        def run_command(self, args, check_rc=True):
            return self.run_command_results[args]

    # Create mock module obj
    obj = MockModule()

    # Create instance of SunOSHardware
    fact_class_inst = SunOSHardware()

    # Set module used by SunOSHardware to mock module
    fact_class_inst.module = obj

    # Expected results
    results = 15600

    # Set rc/out/err of mocked run_command to current time - boot time

# Generated at 2022-06-13 01:14:44.103107
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    SunOSHardware_fake = SunOSHardware()
    SunOSHardware_fake.module = FakeModule()
    SunOSHardware_fake.module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}
    SunOSHardware_fake.get_cpu_facts()
    assert SunOSHardware_fake.facts['processor'] == ['SPARC64-X']
    assert SunOSHardware_fake.facts['processor_cores'] == 2
    assert SunOSHardware_fake.facts['processor_count'] == 2


# Generated at 2022-06-13 01:14:48.057049
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hardware = SunOSHardware()
    collected_facts = hardware.populate()
    cpu_facts = hardware.get_cpu_facts(collected_facts)
    facts = {
        'processor': [
            'SPARC T4-1 @ 1665MHz',
            'SPARC T4-1 @ 1665MHz',
            'SPARC T4-1 @ 1665MHz',
            'SPARC T4-1 @ 1665MHz'
        ],
        'processor_cores': 8,
        'processor_count': 4
    }
    assert cpu_facts == facts

# Generated at 2022-06-13 01:14:58.350225
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Create class object
    hardware_obj = SunOSHardware()

    # Create input data
    facts_str = """
        module: cpu_info
        class: misc
        instance: 0
        brand: Intel(r) Xeon(r) CPU E5-2670 v2 @ 2.50GHz
        clock_MHz: 2501
        cpu_fru: PSB1
        cpu_type: x86
        implementation: x64
        chip_id: 0
        module: cpu_info
        class: misc
        instance: 1
        brand: Intel(r) Xeon(r) CPU E5-2670 v2 @ 2.50GHz
        clock_MHz: 2501
        cpu_fru: PSB1
        cpu_type: x86
        implementation: x64
        chip_id: 0
    """

    # Initialize class