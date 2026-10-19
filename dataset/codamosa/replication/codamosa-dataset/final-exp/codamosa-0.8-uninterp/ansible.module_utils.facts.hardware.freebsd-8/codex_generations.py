

# Generated at 2022-06-13 00:45:35.059982
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """ Tests for FreeBSDHardware.populate() """
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    hardware_facts = hardware.populate()
    assert hardware_facts['devices'] != {}
    assert hardware_facts['devices']['ada0'] != []
    assert hardware_facts['devices']['ada0'][0] == 'ada0s1a'
    assert hardware_facts['devices']['ada1'] != []
    assert hardware_facts['devices']['ada1'][0] == 'ada1s1a'
    assert hardware_facts['devices']['ada2'] != []
    assert hardware_facts['devices']['ada2'][0] == 'ada2s1a'
    assert hardware_facts['processor'] != []

# Generated at 2022-06-13 00:45:38.135030
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """This test case is to test specific facts with FreeBSD"""
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)

    assert hardware.populate() != {}


# Generated at 2022-06-13 00:45:39.818078
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    hw = FreeBSDHardware({})
    hw.populate()



# Generated at 2022-06-13 00:45:52.142381
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Build the result that sysctl -b kern.boottime returns
    result = struct.pack('@L', int(time.time() - 60.0))

    module = FakeAnsibleModule()

    # Initialize a FreeBSDHardware object with the mocked module
    bsd_hw = FreeBSDHardware(module)

    # Patch the method get_bin_path of the FreeBSDHardware module
    # to return an arbitrary command and no error

# Generated at 2022-06-13 00:45:54.985522
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    facts = FreeBSDHardwareCollector(None, None, None)
    assert isinstance(facts, HardwareCollector)
    assert facts.platform == 'FreeBSD'


# Generated at 2022-06-13 00:46:03.372917
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import timeout

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
    )

    hardware = FreeBSDHardware(module)
    # On FreeBSD, the default format is annoying to parse.
    # Use -b to get the raw value and decode it.
    sysctl_cmd = module.get_bin_path('sysctl')
    cmd = [sysctl_cmd, '-b', 'kern.boottime']

    # We need to get raw bytes, not UTF-8.
    rc, out, err = module.run_command(cmd, encoding=None)

    # kern.boottime returns two 64-bit fields, but we are only interested in
    # the first one.
    struct_format

# Generated at 2022-06-13 00:46:12.851065
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():

    # Mocking module instance
    module = type('AnsibleModule', (object,), {
        'run_command': lambda self, cmd, check_rc=False: (0, 'hw.ncpu: 2', ''),
        'get_bin_path': lambda self, name: '/sbin/sysctl'
    })

    # Mocked instance of FreeBSDHardware
    hw = FreeBSDHardware(module)
    hw_facts = hw.get_cpu_facts()

    assert hw_facts['processor_count'] == 2
    assert hw_facts['processor'] == ['Amlogic Meson AML8726-MX rev H (v7l)', 'Amlogic Meson AML8726-MX rev H (v7l)']
    assert hw_facts['processor_cores'] == 4


# Unit test

# Generated at 2022-06-13 00:46:18.067618
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hardware = FreeBSDHardware()

    sysctl = hardware.module.get_bin_path('sysctl')
    rc, out, err = hardware.module.run_command("%s vm.stats" % sysctl, check_rc=False)
    for line in out.splitlines():
        data = line.split()
        if 'vm.stats.vm.v_page_size' in line:
            pagesize = int(data[1])
        if 'vm.stats.vm.v_page_count' in line:
            pagecount = int(data[1])
        if 'vm.stats.vm.v_free_count' in line:
            freecount = int(data[1])

    assert pagesize * pagecount == hardware.get_memory_facts()['memtotal_mb'] * 1024 * 1024
    assert pagesize * freecount

# Generated at 2022-06-13 00:46:27.241634
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """
    unit test for get_memory_facts of class FreeBSDHardware
    """

    # set up

# Generated at 2022-06-13 00:46:31.431899
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()

    assert fhc
    assert fhc._fact_class == FreeBSDHardware
    assert fhc._platform == 'FreeBSD'
    assert fhc._fact_class({}) is not None

# Generated at 2022-06-13 00:46:46.395714
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    allowed_keys = [u'memory_mb', u'memory_mb_available', u'swapfree_mb', u'swaptotal_mb',
                    u'processor', u'processor_cores', u'processor_count', u'devices', u'uptime_seconds',
                    u'memory_mb_used', u'swapfree', u'swapused', u'uptime_hours', u'uptime_days',
                    u'uptime_seconds_raw', u'swapused_mb', u'mounts']
    hw = FreeBSDHardwareCollector()
    actual_keys = set(hw.get_all()[0].keys())

# Generated at 2022-06-13 00:46:57.373041
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    test_module = AnsibleModule({'module_setup': False}, bypass_checks=True)
    test_module.params = {}
    test_facts = FreeBSDHardware.populate()
    assert isinstance(test_facts, dict)
    assert 'uptime_seconds' in test_facts
    assert 'memfree_mb' in test_facts
    assert 'memtotal_mb' in test_facts
    assert 'swapfree_mb' in test_facts
    assert 'swaptotal_mb' in test_facts
    assert 'devices' in test_facts
    assert 'board_serial' in test_facts
    assert 'board_version' in test_facts
    assert 'board_vendor' in test_facts
    assert 'chassis_asset_tag' in test_facts
    assert 'chassis_serial' in test_facts


# Generated at 2022-06-13 00:47:00.282925
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhwc = FreeBSDHardwareCollector()
    assert fhwc._platform == 'FreeBSD'
    assert issubclass(fhwc._fact_class, FreeBSDHardware)
    assert fhwc.collect() is not None

# Generated at 2022-06-13 00:47:07.968602
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware({})
    uptime_facts = hardware.get_uptime_facts()
    assert isinstance(uptime_facts, dict)

    assert 'uptime_seconds' in uptime_facts, 'Could not find uptime_seconds field'
    assert isinstance(uptime_facts['uptime_seconds'], int), \
        'uptime_seconds is not an int'
    assert uptime_facts['uptime_seconds'] >= 0, \
        'uptime_seconds is negative'

# Generated at 2022-06-13 00:47:15.438720
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module_mock = MockModule()
    module_mock.run_command = Mock(return_value=(0, """
vm.stats.vm.v_page_size: 4096
vm.stats.vm.v_page_count: 5588911
vm.stats.vm.v_free_count: 207364""", ''))
    facts = FreeBSDHardware(module_mock)
    expected = {
        'memfree_mb': 8192,
        'memtotal_mb': 22048,
        'swapfree_mb': 2048,
        'swaptotal_mb': 4096
    }
    fact = facts.get_memory_facts()
    assert fact == expected



# Generated at 2022-06-13 00:47:22.426009
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """
    Test case for FreeBSDHardware.get_cpu_facts()
    """
    process = MockModuleProcess()
    module = MockModule(process=process)
    process.set_module(module)
    hardware = FreeBSDHardware(module)
    results = hardware.get_cpu_facts()
    assert results['processor'] == ['Intel(R) Pentium(R) CPU P6100  @ 2.00GHz']
    assert results['processor_cores'] == '2'
    assert results['processor_count'] == '2'


# Generated at 2022-06-13 00:47:32.887071
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collector import get_collector_for_platform
    import time

    f = Facts(module=None)
    fh = FreeBSDHardware(module=None)

    # Fake time to be fixed between calls
    t = time.time()
    time.time = lambda: t

    assert fh.get_uptime_facts() == {'uptime_seconds': 0}

    # Simulate 1 second of uptime
    t += 1
    assert fh.get_uptime_facts() == {'uptime_seconds': 1}

    t += 1

# Generated at 2022-06-13 00:47:41.760097
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:47:54.342154
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import FactsCollector

    # Also test that hardware.dmi returns a dict as expected.
    hardware_facts_dict = {
        'uptime_seconds': 123
    }

    test_module = basic.AnsibleModule(argument_spec={})
    test_module.exit_json = lambda **kwargs: kwargs

    # monkey-patch the module to return our test value
    real_get_mount_size = get_mount_size
    real_get_file_content = get_file_content
    real_run_command = test_module.run_command


# Generated at 2022-06-13 00:47:59.047500
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class C:
        def __init__(self):
            self.module = C()
            self.module.run_command = lambda: ('', 'hw.ncpu: 2', '')
            self.module.get_bin_path = lambda x: x
    c = C()

    facts = FreeBSDHardware(c).get_cpu_facts()
    assert facts['processor_count'] == '2'



# Generated at 2022-06-13 00:48:15.134588
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    module.run_command.return_value = (0, 'hw.ncpu: 4', '')
    freebsd_hw = FreeBSDHardware(module)
    result = freebsd_hw.get_cpu_facts()
    assert result['processor_count'] == '4'
    assert result['processor'] == []

# Generated at 2022-06-13 00:48:24.468618
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hw = FreeBSDHardware()

    hw.module.run_command = lambda cmd, ignore_rc=False: (0, 'vm.stats.vm.v_page_size: 4096', '')
    sysctl_mock = hw.module.get_bin_path('sysctl')
    hw.get_memory_facts()
    hw.get_mount_facts()
    assert sysctl_mock.called
    assert hw.facts['memtotal_mb'] == 8
    assert hw.facts['memfree_mb'] == 2

    hw.module.run_command = lambda cmd, ignore_rc=False: (0, 'vm.stats.vm.v_page_size: 4096', '')
    swapinfo_mock = hw.module.get_bin_path('swapinfo')

# Generated at 2022-06-13 00:48:35.611410
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """
    Unit test for function get_dmi_facts of class FreeBSDHardware.
    """
    # mock dmidecode output
    cmd = 'dmidecode -s'
    rc = 0

# Generated at 2022-06-13 00:48:45.514437
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class Module:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name):
            if name == "sysctl":
                return "sysctl"
            else:
                return None

        def run_command(self, command, check_rc=True, encoding=None):
            if "hw.ncpu" in command:
                rc = 0
                out = "32"
                err = None
            return rc, out, err

    h = FreeBSDHardware(Module())
    cpu_facts = h.get_cpu_facts()
    assert cpu_facts['processor_count'] == '32'
    assert len(cpu_facts['processor']) == 1
    assert cpu_facts['processor'][0] == "Intel(R) Xeon(R) CPU E3-1231 v3"


# Generated at 2022-06-13 00:48:59.116560
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """
    Unit test for get_cpu_facts
    """
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware(BaseFactCollector())
    hardware._get_file_content = lambda x, encoding: to_bytes('CPU:     Intel(R) Core(TM) i7-6600U CPU @ 2.60GHz')
    hardware._binary_files = {
        'sysctl': '/sbin/sysctl',
    }
    hardware._module.run_command = lambda command: (0, to_bytes('hw.ncpu: 2\n'), None)
    hardware.populate()

# Generated at 2022-06-13 00:49:08.445944
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    dmi_facts = {}

    dmi_bin = "/usr/local/sbin/dmidecode"

# Generated at 2022-06-13 00:49:17.035858
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():

    # Case 1: the command 'sysctl -b kern.boottime' returns a valid boottime.
    # sysctl returns a raw string of bytes, not UTF-8.
    module = AnsibleModule(argument_spec={})
    freebsd_hardware = FreeBSDHardware(module=module)
    freebsd_hardware.get_uptime_facts = MagicMock(return_value=b"679443547.1345\x00\x00\x00\x00\x00\x00\x00")
    result = freebsd_hardware.get_uptime_facts()
    assert result == {'uptime_seconds': 679443547}

    # Case 2: the command 'sysctl -b kern.boottime' returns an invalid boottime.
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 00:49:21.350043
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    memory_facts = hardware.get_memory_facts();
    assert type(memory_facts['memtotal_mb']) == int
    assert type(memory_facts['memfree_mb']) == int
    assert type(memory_facts['swaptotal_mb']) == int
    assert type(memory_facts['swapfree_mb']) == int


# Generated at 2022-06-13 00:49:27.622621
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    fake_module = FakeModule()
    fake_module.run_command = lambda cmd: (0, struct.pack('@L', 1510838177), '')

    hardware = FreeBSDHardware()
    hardware.module = fake_module

    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts == {
        'uptime_seconds': 1510851207 - 1510838177,
    }


# FakeModule class used to mock the run_command method

# Generated at 2022-06-13 00:49:38.200234
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """Unit test for method get_memory_facts of class FreeBSDHardware"""
    import tempfile, os
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    fd, fn = tempfile.mkstemp()
    stats = '\n'.join(['hw.ncpu: 1', 'hw.physmem: 4294967296', 'hw.usermem: 4294967296'])
    os.write(fd, stats)
    os.close(fd)
    hw = FreeBSDHardware(module=None, sysctl_file=fn)
    hw.populate()
    assert hw.facts['processor_count'] == '1'
    os.remove(fn)

# Generated at 2022-06-13 00:49:57.660282
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec=dict())

    hardware = FreeBSDHardware(module)
    collected_facts = hardware.populate()

    assert collected_facts['devices']
    assert collected_facts['memtotal_mb'] > 0
    assert collected_facts['swaptotal_mb'] > 0
    assert collected_facts['uptime_seconds'] > 0



# Generated at 2022-06-13 00:50:08.314563
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:50:17.318141
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    out = 'hw.ncpu: 4\n'
    dmesg_boot = '  CPU: AMD Ryzen 9 3900X 12-Core Processor (2394.65-MHz K8-class CPU)\r\n'
    dmesg_boot += '  Logical CPUs per core: 2\r\n'
    fh = open(FreeBSDHardware.DMESG_BOOT, 'w')
    fh.write(dmesg_boot)
    fh.close()
    hw = FreeBSDHardware()
    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts['processor'] == ['AMD Ryzen 9 3900X 12-Core Processor (2394.65-MHz K8-class CPU)']
    assert cpu_facts['processor_count'] == '4'

# Generated at 2022-06-13 00:50:24.510635
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """This is a unit test for method get_memory_facts of class FreeBSDHardware

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    import sys
    import io
    import unittest
    from mock import MagicMock, patch

    class AnsibleModuleMock(MagicMock):
        def __init__(self):
            MagicMock.__init__(self)

    sys.modules['ansible'] = MagicMock()
    sys.modules['ansible.module_utils.facts'] = MagicMock()
    sys.modules['ansible.module_utils.facts.hardware'] = MagicMock()
    sys.modules['ansible.module_utils.facts.hardware.freebsd'] = MagicMock()

# Generated at 2022-06-13 00:50:31.551573
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''Return empty dictionary'''
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    freebsd_hardware_collector = FreeBSDHardwareCollector(module=module)
    freebsd_hardware_collector.collect()
    freebsd_hardware_collector._gather_facts()
    assert 'dmi-information' in freebsd_hardware_collector.facts
    assert len(freebsd_hardware_collector.facts['dmi-information'].keys()) == 16
    # Check all keys are correct
    assert 'bios-release-date' in freebsd_hardware_collector.facts['dmi-information'].keys()

# Generated at 2022-06-13 00:50:41.448721
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True)
    h = FreeBSDHardware(module=module)
    h.populate()

    assert h.cpu() == {
        'processor': ['Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz'],
        'processor_cores': 2,
        'processor_count': '4'}
    assert h.mem() == {
        'memfree_mb': 356,
        'memtotal_mb': 3924,
        'swapfree_mb': 0,
        'swaptotal_mb': 0}

# Generated at 2022-06-13 00:50:52.210371
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''
    unit test for populate method of FreeBSDHardware class
    '''
    h = FreeBSDHardware()
    h.module = FakeModule()
    h.populate()
    assert(h.facts['devices'])
    assert(h.facts['memfree_mb'])
    assert(h.facts['memtotal_mb'])
    assert(h.facts['mounts'])
    assert(h.facts['processor'])
    assert(h.facts['processor_cores'])
    assert(h.facts['processor_count'])
    assert(h.facts['swapfree_mb'])
    assert(h.facts['swaptotal_mb'])
    assert(h.facts['uptime_seconds'])



# Generated at 2022-06-13 00:50:58.124241
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    """Test get_device_facts method of FreeBSDHardware class
    """
    module = AnsibleModule(argument_spec=dict())
    module.params['gather_subset'] = ['']
    module.params['gather_timeout'] = 5
    module.params['gather_cache'] = False
    module.check_mode = False
    result = dict(changed=False, ansible_facts=dict())
    hardware_collector = FreeBSDHardwareCollector(module=module)
    hardware = hardware_collector.collect()
    result['ansible_facts'] = hardware.populate()
    assert 'devices' in result['ansible_facts']


# Generated at 2022-06-13 00:51:02.266515
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    memory_facts = {'memtotal_mb': 6144, 'memfree_mb': 3335, 'swaptotal_mb': 1024, 'swapfree_mb': 1023}
    m = FreeBSDHardware()
    assert memory_facts == m.get_memory_facts()


# Generated at 2022-06-13 00:51:06.293077
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = FakeAnsibleModule()
    hardwarecollection = FreeBSDHardwareCollector(module=module)
    hardwareclass = hardwarecollection.collect()
    hardwareclass.get_dmi_facts()


# Unit test class for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:51:25.618192
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hardware = FreeBSDHardware(module)
    hardware.get_cpu_facts()


# Generated at 2022-06-13 00:51:30.588651
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    bin_path = '/usr/local/bin'
    path_to_dmidecode = 'dmidecode'
    path_to_dmidecode = os.path.join(bin_path, path_to_dmidecode)

    class Module(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, arg, opt_dirs=[]):
            return path_to_dmidecode

        def run_command(self, cmd, encoding=None, check_rc=True, close_fds=True):
            if cmd == path_to_dmidecode + ' -s bios-release-date':
                out = "BIOS\nRelease Date: 10/07/2015\n"
                rc = 0
                err = ''

# Generated at 2022-06-13 00:51:32.893182
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    facts = FreeBSDHardware().get_dmi_facts()
    assert 'system_vendor' in facts


# Generated at 2022-06-13 00:51:40.390258
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    # Check that dmi_facts is a dictionary
    hardware = FreeBSDHardware(dict())
    dmi_facts = hardware.get_dmi_facts()
    assert type(dmi_facts) == dict

    # Check that some of the dmi_facts values are not empty
    dmi_facts_keys = ('bios_date', 'bios_vendor', 'bios_version', 'board_name', 'board_vendor', 'system_vendor', 'product_name')
    for key in dmi_facts_keys:
        assert (key in dmi_facts) and (dmi_facts[key] != 'NA')

# Generated at 2022-06-13 00:51:49.020972
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # Create a dummy AnsibleModule object, and use the module utility to
    # create a fake module object
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.hardware import freebsd
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    test_module = FreeBSDHardware()
    test_module.module = ModuleFacts(freebsd, 'test', {'name': 'test'})

    # Create a fake sysctl output
    fake_sysctl_output = '''hw.ncpu: 2
    hw.physmem: 8589934592
    hw.usermem: 8446935040
    hw.realmem: 8589934592
    hw.ncpu_per_socket: 2'''
    test_module

# Generated at 2022-06-13 00:51:56.373803
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FakeAnsibleModule:
        def __init__(self):
            self.params = {
                'gather_timeout': 1
            }

        def get_bin_path(self, name):
            return name

    class FakePlayContext:
        def __init__(self):
            self.timeout = 100

    class FakeTask:
        def __init__(self):
            self.play_context = FakePlayContext()

    class FakePlay:
        def __init__(self):
            self.task = FakeTask()

    class FakePlaybook:
        def __init__(self):
            self.play = FakePlay()

    class FakeLoader:
        def __init__(self):
            self.plays = FakePlaybook()


# Generated at 2022-06-13 00:52:05.586143
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    hardware = FreeBSDHardware(module=module)
    dmi_facts = hardware.get_dmi_facts()

    assert 'bios_date' in dmi_facts
    assert 'bios_vendor' in dmi_facts
    assert 'bios_version' in dmi_facts
    assert 'board_asset_tag' in dmi_facts
    assert 'board_name' in dmi_facts
    assert 'board_serial' in dmi_facts
    assert 'board_vendor' in dmi_facts
    assert 'board_version' in dmi_facts
    assert 'chassis_asset_tag' in dmi_facts
    assert 'chassis_serial' in dmi_facts
   

# Generated at 2022-06-13 00:52:15.752527
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class ModuleMock():
        def __init__(self, *args, **kwargs):
            self.run_command_expect = (0, '', '')
            self.run_command_args = list()

        def set_run_command_expect(self, exit, out, err):
            self.run_command_expect = (exit, out, err)

        def run_command(self, args, check_rc=True, encoding='utf-8'):
            self.run_command_args.append(args)
            if self.run_command_expect:
                exit = self.run_command_expect[0]
                out = self.run_command_expect[1]
                err = self.run_command_expect[2]
                self.run_command_expect = None
               

# Generated at 2022-06-13 00:52:22.874576
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    f = FreeBSDHardware()
    f.module = MagicMock()
    f.module.run_command.return_value = (0, '', '')
    f.module.get_bin_path.return_value = '/usr/bin/dmidecode'

    # Test execution of method populate
    f.populate()

    # Test if all parameters are present in the result
    assert 'uptime_seconds' in f.facts
    assert 'devices' in f.facts
    assert 'memfree_mb' in f.facts
    assert 'memtotal_mb' in f.facts
    assert 'swapfree_mb' in f.facts
    assert 'swaptotal_mb' in f.facts
    assert 'processor' in f.facts
    assert 'processor_cores' in f.facts
    assert 'processor_count' in f

# Generated at 2022-06-13 00:52:29.580161
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''unit test for FreeBSDHardware class'''
    # create an instance
    fhw = FreeBSDHardware()

    facts = fhw.populate()
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'devices' in facts
    assert 'uptime_seconds' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    # Test if a JSONDict is given by the populate method
    assert json.dumps(facts)

# Generated at 2022-06-13 00:52:55.699449
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    data = """vm.stats.vm.v_page_size:                  4096
vm.stats.vm.v_page_count:                793328
vm.stats.vm.v_free_count:                 473980
vm.stats.vm.v_inactive_count:             119910
vm.stats.vm.v_cache_count:                103791"""
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()
    module.run_command.return_value = (0, data, None)
    fact = FreeBSDHardware(module)
    assert fact.get_memory_facts() == {'memtotal_mb': 3100, 'memfree_mb': 1844}


# Generated at 2022-06-13 00:53:02.974826
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class TestModule(object):
        def get_bin_path(self, path):
            return '/bin/{}'.format(path)

        def run_command(self, cmd, check_rc=True, encoding=None):
            return 0, '\x01\x00\x00\x00\x00\x00\x00\x00', ''

    test_module = TestModule()
    hw = FreeBSDHardware(test_module)
    facts = hw.get_uptime_facts()

    assert 'uptime_seconds' in facts
    assert facts['uptime_seconds'] == 4294967296

# Generated at 2022-06-13 00:53:11.163042
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts import timeout

    import time
    import unittest

    class MockModule(object):
        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, binary):
            return self.bin_path

        def run_command(self, command, encoding=None, check_rc=True):
            return True, command[-1], None

    class MockTimeout(timeout.Timeout):
        def __init__(self, seconds):
            pass

    class TestFreeBSDHardware(unittest.TestCase):
        def setUp(self):
            bin_path = '.'
            self.module = MockModule(bin_path)
            self

# Generated at 2022-06-13 00:53:20.711851
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = MockModule()
    sysctl = module.get_bin_path('sysctl')
    dmi = module.get_bin_path('dmidecode')

    setattr(module, 'run_command', run_command)
    setattr(module, 'run_command_environ_update', run_command_environ_update)
    setattr(module, 'get_bin_path', get_bin_path)
    setattr(module, 'get_file_content', get_file_content)

    hardware_facts = FreeBSDHardware(module)

    dmi_facts = hardware_facts.get_dmi_facts()

    # Assert that all the keys are present in dmi facts
    assert(len(dmi_facts) >= 13)
    assert('bios_date' in dmi_facts)

# Generated at 2022-06-13 00:53:30.646460
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    mock_module = type('', (), {})()
    mock_module.run_command = lambda args: (0, 'hw.ncpu: 4', '')

    facts = FreeBSDHardware(mock_module)

    expected = {'processor': ['Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz',
                              'Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz',
                              'Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz',
                              'Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz'],
                'processor_cores': '4',
                'processor_count': '4',
               }
    assert facts.get_cpu_facts() == expected


# Generated at 2022-06-13 00:53:41.056204
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """Unit test for function get_cpu_facts of class FreeBSDHardware"""

    # Use a mock for the ansible module
    module = MockAnsibleModule()

    # Create the instance of FreeBSDHardware class.  "module" is passed to the init.
    hardware_instance = FreeBSDHardware(module)

    # test 1
    # Get the cpu facts and check them for this specific system
    cpu_facts = hardware_instance.get_cpu_facts()

    # check count
    if cpu_facts['processor_count'] != '2':
        module.fail_json(msg="processor_count is not 2")

    # check each cpu
    if 'GenuineIntel' not in cpu_facts['processor'][0]:
        module.fail_json(msg="GenuineIntel not in cpu0")

# Generated at 2022-06-13 00:53:46.894564
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # TODO: write unit test for FreeBSDHardware.populate
    # This is a stub to make it easier to write this test
    module = AnsibleModule(argument_spec=dict())
    hardware_instance = FreeBSDHardware(module)
    hardware_info = hardware_instance.populate()
    assert hardware_info['memtotal_mb'] > -1
    assert hardware_info['memfree_mb'] > -1
    assert hardware_info['swaptotal_mb'] > -1
    assert hardware_info['swapfree_mb'] > -1
    assert hardware_info['processor_cores'] > -1
    assert hardware_info['processor_count'] > -1
    assert hardware_info['uptime_seconds'] > -1


# Generated at 2022-06-13 00:53:53.441957
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    facts_instance = FreeBSDHardware(module)
    facts = facts_instance.populate()
    assert facts.get('devices') is not None
    assert facts.get('uptime_seconds') is not None
    assert facts.get('memtotal_mb') is not None
    assert facts.get('memfree_mb') is not None
    assert facts.get('processors') is not None



# Generated at 2022-06-13 00:53:57.791084
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:53:59.906647
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware_collector = FreeBSDHardwareCollector()
    assert hardware_collector.platform == 'FreeBSD'
    assert hardware_collector._fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:55:01.476583
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    ''' This unit test mocks method run_command and it is used to test
        get_uptime_facts of class FreeBSDHardware'''

    # Create a FreeBSDHardware object
    hardware_obj = FreeBSDHardware()
    hardware_obj.module = MagicMock()

    # Define value to be returned by run_command
    rc = 0
    out = '12113984767 8781448'.encode()
    err = ''

    # Return value to be used when method run_command is called
    hardware_obj.module.run_command.return_value = (rc, out, err)

    # Call get_uptime_facts of class FreeBSDHardware
    fact = hardware_obj.get_uptime_facts()

    # Assert that method run_command has been called
    hardware_obj.module.run_command.assert_called_with

# Generated at 2022-06-13 00:55:06.121822
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={
        'dmidecode_path': {'type': 'str', 'default': None},
    })
    hardware = FreeBSDHardware(module)
    dmi_facts = hardware.get_dmi_facts()
    assert isinstance(dmi_facts, dict)
    assert 'chassis_vendor' in dmi_facts
    assert 'system_vendor' in dmi_facts
    assert 'form_factor' in dmi_facts


# Generated at 2022-06-13 00:55:13.978114
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    import sys
    import pkg_resources

    class ModuleMock(object):
        def __init__(self):
            self.run_command_results = []
            self.run_command_result_index = -1
        def get_bin_path(self, module_name):
            return '/sbin/' + module_name
        def run_command(self, args, check_rc=False, encoding=None):
            self.run_command_result_index += 1
            if self.run_command_result_index >= len(self.run_command_results):
                raise IndexError('unexpected: module.run_command called with %s' % args)
            expected = self.run_command_results[self.run_command_result_index]
            if isinstance(expected, Exception):
                raise expected