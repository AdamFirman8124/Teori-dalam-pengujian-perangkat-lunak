

# Generated at 2022-06-13 00:45:33.579020
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = sys.modules['__main__']
    if not hasattr(module, 'get_bin_path'):
        module.get_bin_path = lambda x: 'sysctl'

# Generated at 2022-06-13 00:45:40.635822
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import module_utils.facts.hardware.freebsd

    # Test case 1
    boottime_out = b'\x00\x00\x00\x00\x00\x00\x00.\x99\x00\x00\x00'
    module_utils.facts.hardware.freebsd.struct.unpack = lambda format, inp: (int(time.time()),)

    hardware = FreeBSDHardware(None)
    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts == {'uptime_seconds': int(time.time())}

# Generated at 2022-06-13 00:45:52.948752
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = MockModule()
    x = FreeBSDHardware(module=module)
    BIOS_DATE1 = '06/08/2015'
    BIOS_VENDOR1 = 'VBox'
    BIOS_VERSION1 = 'VirtualBox'
    BOARD_SERIAL1 = '0x00000000'
    CHASSIS_ASSET1 = 'Default string or unicode string'
    CHASSIS_SERIAL1 = '0x00000000'
    CHASSIS_VERSION1 = 'Default string or unicode string'

# Generated at 2022-06-13 00:45:58.155290
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    hardware = FreeBSDHardware(module=module)
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor_count' in cpu_facts
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts


# Generated at 2022-06-13 00:46:08.538404
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """
    Method to test get_dmi_facts() of class FreeBSDHardware.
    """

    class MockModule:
        def __init__(self, dmidecode_bin):
            self.dmidecode_bin = dmidecode_bin

        def get_bin_path(self, executable, required=False):
            return self.dmidecode_bin

        def run_command(self, command, check_rc=True, encoding=None):
            # response for dmidecode -s baseboard-serial-number
            out = "Base Board Serial Number\n" \
                  "MSF7360700B\n"
            return (0, out, "")

    # Test case when dmidecode is available
    m = MockModule("/usr/sbin/dmidecode")
    fhw = FreeBSDHardware()
   

# Generated at 2022-06-13 00:46:11.723009
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """
    Test case for the get_cpu_facts method of FreeBSDHardware
    """
    # setup test environment
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    test_obj = FreeBSDHardware(module)
    cpu_facts = test_obj.get_cpu_facts()

    assert cpu_facts['processor_count'] == '2'
    assert len(cpu_facts['processor']) == 2
    assert cpu_facts['processor_cores'] == '2'



# Generated at 2022-06-13 00:46:15.913185
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    dmi_facts = FreeBSDHardware().get_dmi_facts()

    # Check for the existence of some well known keys
    for key in ('system_vendor', 'product_name'):
        assert key in dmi_facts



# Generated at 2022-06-13 00:46:25.845815
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    cpu_facts = {'processor': ['Intel(R) Core(TM) i5-2500K CPU @ 3.30GHz'],
                 'processor_count': '2',
                 'processor_cores': '2',
                 'processor_threads_per_core': '1'}

    module = AnsibleModule(dict(ansible_facts={'hardware': {}}))

    hardware = FreeBSDHardware(module)
    hardware.get_cpu_facts()
    facts = hardware.populate()
    assert facts['processor'] == cpu_facts['processor']
    assert facts['processor_cores'] == cpu_facts['processor_cores']
    assert facts['processor_count'] == cpu_facts['processor_count']
    assert facts['processor_threads_per_core'] == cpu_facts['processor_threads_per_core']


# Generated at 2022-06-13 00:46:28.511582
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    facts = FreeBSDHardwareCollector()
    assert isinstance(facts, dict)
    assert 'hardware' in facts
    assert isinstance(facts['hardware'], FreeBSDHardware)

# Generated at 2022-06-13 00:46:37.896411
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError

    class FreeBSDHardwareModule:
        def get_bin_path(self, bin_path):
            return '/bin/echo'

        def run_command(self, cmd):
            if cmd.startswith('/bin/echo'):
                return 0, '', ''


# Generated at 2022-06-13 00:46:59.576529
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """ This method unit test the get_memory_facts method of class FreeBSDHardware
        using the examples from https://www.freebsd.org/cgi/man.cgi?query=meminfo&sektion=2

        :return: True if test passes otherwise False
        :rtype: bool
    """

# Generated at 2022-06-13 00:47:09.853077
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():

    # Create a FreeBSDHardware object for testing
    h = FreeBSDHardware()

    # Create an AnsibleModule object for testing
    module = FakeModule()
    h.module = module

    # Test 1:
    # Setup the module.run_command mock to return rc=0, out='', err=''
    module.run_command.return_value = (0, '', '')

    # Test the method
    out = h.populate()

    # Check the expected results
    assert out == {'processor_count': '',
                   'processor': [],
                   'devices': {},
                   'memtotal_mb': 0,
                   'memfree_mb': 0,
                   'swaptotal_mb': 0,
                   'swapfree_mb': 0}

    # Test 2
    # Setup the module.run_command mock to return a

# Generated at 2022-06-13 00:47:13.260201
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    facts = hardware.get_memory_facts()
    assert isinstance(facts['memtotal_mb'], (int, type(None)))
    assert isinstance(facts['memfree_mb'], (int, type(None)))
    assert isinstance(facts['swaptotal_mb'], (int, type(None)))
    assert isinstance(facts['swapfree_mb'], (int, type(None)))

# Generated at 2022-06-13 00:47:19.204384
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import pytest
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware


# Generated at 2022-06-13 00:47:29.956956
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    class mock_module():
        def get_bin_path(self, arg):
            return "/usr/sbin/dmidecode"

        def run_command(self, arg):
            return (0, get_file_content(os.path.join(os.path.dirname(__file__), 'fixtures', 'dmi_output')), '')

    collected_facts = FreeBSDHardware(mock_module()).populate()

# Generated at 2022-06-13 00:47:33.802887
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    m = FreeBSDHardware()
    # Mocking the module run_command method
    m.module.run_command = lambda arg: ('0', struct.pack('@L', 1527168811), '')

    assert m.get_uptime_facts() == {'uptime_seconds': 1527177595 - 1527168811}

# Generated at 2022-06-13 00:47:42.399984
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # test for get_memory_facts with data from sysctl vm.stats
    data_in = {'v_page_size': '4096',
               'v_page_count': '7801299',
               'v_free_count': '7641517'}
    expected_data_out = {'memfree_mb': '30216',
                         'memtotal_mb': '30743'}
    out = FreeBSDHardware.get_memory_facts(data_in)
    assert out == expected_data_out

    # test for get_memory_facts with data from swapinfo
    data_in = {'swaptotal': '314368',
               'swapfree': '314368'}
    expected_data_out = {'swapfree_mb': '307',
                         'swaptotal_mb': '307'}

# Generated at 2022-06-13 00:47:54.721159
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    test_hardware = FreeBSDHardware()
    key_used = 'vm.stats.vm.v_page_count'
    key_avail = 'vm.stats.vm.v_free_count'
    key_bufspace = 'vfs.bufspace'
    key_pagesize = 'vm.stats.vm.v_page_size'

    # Prevent sysctl to answer
    test_hardware.module.run_command = success_false
    memory_facts = test_hardware.get_memory_facts()
    assert 'swaptotal_mb' not in memory_facts
    assert 'swapfree_mb' not in memory_facts
    assert 'memtotal_mb' not in memory_facts
    assert 'memfree_mb' not in memory_facts

    # Successful sysctl mock
    test_hardware.module.run

# Generated at 2022-06-13 00:48:03.031784
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():

    mock_module = type('AnsibleModule', (object,), {
        'params': {
            'gather_timeout': 25
        },
        'run_command': lambda self, cmd, check_rc=True: (0, '', ''),
        'get_bin_path': lambda self, executable, opt_dirs=[] : '/usr/bin/sysctl',
        'USER_BASE_PATH': '/home/me/',
    })
    mock_module_instance = mock_module()

    fhw = FreeBSDHardware(mock_module_instance)

    fhw.get_cpu_facts = lambda : {
        'processor': ['AMD Ryzen 5 2600X Six-Core Processor'],
        'processor_count': 6,
        'processor_cores': 12,
    }


# Generated at 2022-06-13 00:48:06.125686
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = HardwareCollector._get_platform_module('FreeBSD')
    collector = module.get_collector()
    assert(collector.__class__.__name__ == 'FreeBSDHardwareCollector')

# Generated at 2022-06-13 00:48:33.519758
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec=dict())
    bsdhw = FreeBSDHardware(module)

    try:
        facts = bsdhw.get_uptime_facts()
    except TimeoutError:
        pass
    else:
        assert isinstance(facts['uptime_seconds'], int)

# Generated at 2022-06-13 00:48:43.674721
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    hardware = FreeBSDHardware()


# Generated at 2022-06-13 00:48:53.217311
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hardware = FreeBSDHardware()
    hardware.module = MockModule()
    hardware.module.run_command = Mock(return_value=[0, '', ''])
    hardware.module.get_bin_path = Mock(return_value='/usr/bin/sysctl')
    hardware.DMESG_BOOT = 'test/ansible/module_utils/facts/hardware/dmesg.boot'
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts


# Generated at 2022-06-13 00:48:59.300792
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    freebsdHardware = FreeBSDHardware(module)
    memory_facts = freebsdHardware.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts



# Generated at 2022-06-13 00:49:03.270444
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = None
    fb = FreeBSDHardware(module=module)

    # Test with a non-existing file
    try:
        fb.get_uptime_facts()
        raise Exception('Unexpected success')
    except IOError:
        pass

    # Test with a file with invalid contents
    with open('/tmp/dmesg.boot', 'w') as f:
        f.write('Some invalid content')
    try:
        fb.get_uptime_facts()
        raise Exception('Unexpected success')
    except ValueError:
        pass

    # Test with a valid file
    with open('/tmp/dmesg.boot', 'w') as f:
        f.write('kern.boottime={ sec = 1598304518, usec = 0 }')
    boot_time = fb.get_

# Generated at 2022-06-13 00:49:05.868710
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    harware = FreeBSDHardware(module)

    assert harware.populate()

# Generated at 2022-06-13 00:49:07.492099
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():

    import doctest
    doctest.testmod(FreeBSDHardware, verbose=False, optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-13 00:49:16.293197
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    hw = FreeBSDHardware()

    # Run successfully, no comments in dmidecode output
    dmi_facts = hw.get_dmi_facts()

    assert dmi_facts['bios_date'] == '2015-12-02'
    assert dmi_facts['bios_vendor'] == 'SeaBIOS'
    assert dmi_facts['bios_version'] == '1.10.2-1.el6'
    assert dmi_facts['board_asset_tag'] == 'NA'
    assert dmi_facts['board_name'] == 'NA'
    assert dmi_facts['board_serial'] == 'NA'
    assert dmi_facts['board_vendor'] == 'NA'
    assert dmi_facts['board_version'] == 'NA'

# Generated at 2022-06-13 00:49:23.417051
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    import re
    import unittest
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    class ImportedModule(object):
        def __init__(self):
            self.run_command = lambda x: (0, to_bytes("hw.ncpu: 1\nvm.stats.vm.v_page_size: 4096\nvm.stats.vm.v_page_count: 870912\nvm.stats.vm.v_free_count: 838560\n"), '')
            self.get_bin_path = get_bin_path

    fbsd_hw = FreeBSDHardware(ImportedModule())
    procs = re.compile

# Generated at 2022-06-13 00:49:28.815887
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    hardware = FreeBSDHardware(module)

    hardware.get_cpu_facts()
    assert hardware.facts['processor'] == ['Intel(R) Core(TM) i7-3667U CPU @ 2.00GHz']
    assert hardware.facts['processor_cores'] == '1'
    assert hardware.facts['processor_count'] == '2'



# Generated at 2022-06-13 00:50:21.152529
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Create a test class
    class TestAnsibleModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, binary_name):
            if self.params['dmi_bin_path']:
                return self.params['dmi_bin_path']
            else:
                return None

        def run_command(self, cmd, encoding=None, errors=None):
            if cmd == '/fake/dmidecode -s bios-release-date':
                return 0, '2012-01-01', None
            if cmd == '/fake/dmidecode -s bios-vendor':
                return 0, 'FOO', None
            if cmd == '/fake/dmidecode -s bios-version':
                return 0, '1.1', None

# Generated at 2022-06-13 00:50:22.787935
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    obj = FreeBSDHardwareCollector()
    assert obj._platform == "FreeBSD"
    assert obj._fact_class == FreeBSDHardware



# Generated at 2022-06-13 00:50:29.347550
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    """
    Unit test for get_uptime_facts of class FreeBSDHardware
    """
    fake_module = FakeAnsibleModule(
        dict(
            dict(
                ansible_module_instance='fake_module_instance',
                module_args=dict(
                    gather_subset=[
                        'all',
                    ],
                ),
            )
        )
    )
    fake_ansible_module_get_bin_path = fake_module.get_bin_path
    fake_module.get_bin_path = lambda x: '/dev/null'

    Hardware = FreeBSDHardware(fake_module)
    Hardware.module = fake_module
    fake_module.run_command = lambda x: (0, '', '')


# Generated at 2022-06-13 00:50:36.086805
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    FreeBSD_module = AnsibleModuleMock()
    FreeBSD_module.run_command = run_command
    FreeBSD_module.get_bin_path = get_bin_path
    FreeBSD = FreeBSDHardware(FreeBSD_module)
    facts = FreeBSD.populate()
    assert 'processor_cores' in facts
    assert 'memtotal_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'devices' in facts
    assert 'uptime_seconds' in facts



# Generated at 2022-06-13 00:50:40.556370
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = FakeModule({})
    hardware = FreeBSDHardware(module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 1
    assert memory_facts['memfree_mb'] == 1
    assert memory_facts['swaptotal_mb'] == 1
    assert memory_facts['swapfree_mb'] == 1



# Generated at 2022-06-13 00:50:52.593463
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    m = FreeBSDHardware(dict())
    dmi_facts = m.get_dmi_facts()
    assert dmi_facts['board_asset_tag'] == 'NA'
    assert dmi_facts['board_name'] == 'NA'
    assert dmi_facts['board_serial'] == 'NA'
    assert dmi_facts['board_vendor'] == 'NA'
    assert dmi_facts['board_version'] == 'NA'
    assert dmi_facts['chassis_asset_tag'] == 'NA'
    assert dmi_facts['chassis_serial'] == 'NA'
    assert dmi_facts['chassis_vendor'] == 'NA'

# Generated at 2022-06-13 00:50:55.437300
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    fhw = FreeBSDHardware()
    devices = fhw.get_device_facts()
    assert type(devices) is dict
    assert "devices" in devices
    assert type(devices["devices"]) is dict
    assert len(devices["devices"]) > 0



# Generated at 2022-06-13 00:51:05.709914
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(
        argument_spec={}
    )

    # We can't run sysctl(8) which is required in FreeBSDHardware.get_memory_facts()
    # to test this method. So let's parse the result of sysctl(8) instead.
    rc, out, err = module.run_command(module.get_bin_path('sysctl') + ' vm.stats', check_rc=False)
    assert rc == 0
    out = to_bytes(out)
    memory_facts = FreeBSDHardware(module, out=out).get_memory_facts()
    assert len(memory_facts) == 4
    assert memory_facts['memtotal_mb'] == 524288
    assert memory_

# Generated at 2022-06-13 00:51:16.391303
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import get_collector

    m = get_collector('FreeBSDHardwareCollector')
    # Add a test to check if running system is FreeBSD
    if not m.collect()['ansible_facts']['ansible_system'] == 'FreeBSD':
        raise Exception('Current OS is not FreeBSD')

    filename_for_test = 'tests/unittests/dmidecode_output'

    fake_DMESG_BOOT = "CPU:\n"
    fake_DMESG_BOOT += "Logical CPUs per core: 1\n"
    fake_DMESG_BOOT += "Physical CPUs per socket: 1\n"
    fake_DMESG_BOOT += "Processors: 2\n"

    fake_

# Generated at 2022-06-13 00:51:24.689608
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # kern.boottime returns seconds and microseconds as two 64-bits
    # fields, but we are only interested in the first field.
    test_cases = (
        # Current time (when the test is run) is
        # Tue, 07 Jan 2020 23:48:47 GMT
        # Time when I rebooted the system and recorded the dmesg was
        # Tue Jan  7 23:33:38 GMT 2020 UTC
        # So I should get a result of 795 seconds
        (b'\x00\x00\x00\x00\x01\x5E\xE3\xD3\x00\x00\x00\x00\x00\x00\x00\x00', 795),
        # Test for a broken sysctl output
        (b'', {}),
    )


# Generated at 2022-06-13 00:52:34.824583
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = MockModule()
    hw = FreeBSDHardware(module)
    cpu_facts = hw.get_cpu_facts()

    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 2
    assert 'amd64-assist' in cpu_facts['processor']
    assert 'FreeBSD' in cpu_facts['processor']

    assert 'processor_count' in cpu_facts
    assert cpu_facts['processor_count'] == 2

    assert 'processor_cores' in cpu_facts
    assert cpu_facts['processor_cores'] == 2


# Generated at 2022-06-13 00:52:38.103610
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    fh = FreeBSDHardware(dict())
    mem_facts = fh.get_memory_facts()
    assert 'memtotal_mb' in mem_facts
    assert 'swaptotal_mb' in mem_facts

# Generated at 2022-06-13 00:52:40.368621
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    my_obj = FreeBSDHardwareCollector()
    assert isinstance(my_obj._fact_class, Hardware)
    assert my_obj._platform == 'FreeBSD'

# Generated at 2022-06-13 00:52:48.703822
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FakeModule(object):
        def __init__(self):
            self.boottime = 0

        def get_bin_path(self, name, required=False):
            if name == 'sysctl':
                return name

        def run_command(self, cmd, encoding=None, check_rc=True):
            if cmd[0] == 'sysctl':
                return 0, struct.pack('@L', self.boottime), ''

    module = FakeModule()
    hardware = FreeBSDHardware(module)

    now = 1462789351.7667484
    module.boottime = now - 10.0
    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 10.0

    module.boottime = now - 10.1

# Generated at 2022-06-13 00:52:53.926187
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # Works only on FreeBSD
    if 'FreeBSD' not in platform.system():
        print('Skipping test_FreeBSDHardware_populate')
        return
    from ansible_collections.ansible.misc.tests.unit.compat.sys_platform import freebsd_10_4_x86_64_hardware_mock as freebsd_hardware
    hardware = FreeBSDHardware(module=None)
    facts = hardware.populate(freebsd_hardware.Facts({}))
    assert len(facts) > 0

# Generated at 2022-06-13 00:53:01.194779
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    fact_module = 'ansible_facts'
    fact_class = 'hardware'
    fact_subclass = 'FreeBSD'
    fact_method = 'populate'
    expected_facts = ['devices', 'memfree_mb', 'memtotal_mb', 'mounts', 'processor', 'processor_cores', 'processor_count',
                      'swapfree_mb', 'swaptotal_mb', 'uptime_seconds']
    mod = AnsibleModule(argument_spec={})
    obj = FreeBSDHardware(mod)

    assert_equal(obj.populate(), {})

# Generated at 2022-06-13 00:53:05.593676
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})

    freebsd_hardware = FreeBSDHardware(module)
    freebsd_hardware.get_device_facts()
    result = freebsd_hardware.get_device_facts()

    assert result['devices']

    module.exit_json(changed=False, ansible_facts=result)

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 00:53:13.269845
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''Unit test for method populate of class FreeBSDHardware'''
    from ansible.module_utils.facts.test.test_hardware.test_FreeBSDHardware import (
        FAKE_DMESG_BOOT,
        FAKE_FREEBSD_FACTS,
        MockModule)
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    # setup
    fake = MockModule(
        params={'gather_subset': '!all,!min'},
        ansible_facts=FAKE_FREEBSD_FACTS)
    with open(FreeBSDHardware.DMESG_BOOT, 'w') as f:
        f.write(FAKE_DMESG_BOOT)

    # test
    FreeBSDHardware(fake).populate()

    # assert

# Generated at 2022-06-13 00:53:21.273060
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_timeout'] = 10
            self.params['timeout'] = 10

        @staticmethod
        def get_bin_path(path):
            cmd = '/sbin/sysctl -n hw.ncpu'
            return cmd

    class MockRunCommand(object):
        def __init__(self):
            self.rc = 0
            self.out = 'hw.ncpu: 4'
            self.err = ''

    mock_module = MockModule()
    mock_run_command = MockRunCommand()

    old_run_command = HardwareCollector.run_command

    HardwareCollector.run_command = lambda self, *args, **kwargs: mock_run_command


# Generated at 2022-06-13 00:53:26.309962
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    facts = FreeBSDHardwareCollector
    epoch = int(time.time())
    boottime_raw = struct.pack('@L', epoch)
    boottime_str = boottime_raw.decode('utf-8')
    assert {'uptime_seconds': 1} == facts._fact_class().get_uptime_facts(boottime_str)