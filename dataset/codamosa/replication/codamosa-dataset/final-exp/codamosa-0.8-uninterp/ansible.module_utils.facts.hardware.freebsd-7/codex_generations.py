

# Generated at 2022-06-13 00:45:32.201215
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hardware = FreeBSDHardware()
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == [u'Intel(R) Core(TM)2 Quad CPU    Q9300  @ 2.50GHz', u'Intel(R) Core(TM)2 Quad CPU    Q9300  @ 2.50GHz', u'Intel(R) Core(TM)2 Quad CPU    Q9300  @ 2.50GHz', u'Intel(R) Core(TM)2 Quad CPU    Q9300  @ 2.50GHz']
    assert cpu_facts['processor_cores'] == u'4'
    assert cpu_facts['processor_count'] == u'4'


# Generated at 2022-06-13 00:45:38.628851
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # Populate FreeBSDHardware class
    module = AnsibleModule(argument_spec={
    })

    # Test for populated values for the class after method populate is called
    free_hw_facts = FreeBSDHardware()
    free_hw_facts.populate()
    assert free_hw_facts.memfree_mb
    assert free_hw_facts.memtotal_mb
    assert free_hw_facts.swapfree_mb
    assert free_hw_facts.swaptotal_mb
    assert free_hw_facts.processor
    assert free_hw_facts.processor_cores
    assert free_hw_facts.processor_count
    assert free_hw_facts.devices
    assert free_hw_facts.uptime_seconds



# Generated at 2022-06-13 00:45:40.826922
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    """
    Unit tests for method get_device_facts of class FreeBSDHardware
    """

    hardware = FreeBSDHardware()
    hardware.get_device_facts()

# Generated at 2022-06-13 00:45:53.052206
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    m = FreeBSDHardware(dict(module=None))
    facts = m.get_dmi_facts()

# Generated at 2022-06-13 00:45:57.160893
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    result = hardware.get_dmi_facts()
    # not empty
    assert result != {}
    # not all 'NA'
    assert 'NA' in result.values()


# Generated at 2022-06-13 00:46:00.476562
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = FreeBSDHardware(module=module)
    hardware_facts = hardware.populate()
    assert hardware_facts is not None
    assert hardware_facts['uptime_seconds'] >= 0


# Generated at 2022-06-13 00:46:04.970228
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    gather_subset = list()
    gather_network = 'yes'
    gather_timeout = 5
    module = None

    facts_obj = FreeBSDHardware()
    facts_obj.populate(gather_subset, gather_network, gather_timeout, module)

# Generated at 2022-06-13 00:46:13.798704
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = MockModule()
    dmesg_boot = get_file_content(FreeBSDHardware.DMESG_BOOT)
    if not dmesg_boot:
        try:
            rc, dmesg_boot, err = module.run_command(module.get_bin_path("dmesg"), check_rc=False)
        except Exception:
            dmesg_boot = ''
    hardware = FreeBSDHardware(module)
    hardware.populate()

    # test processor fact
    line_cpu = [line for line in dmesg_boot.splitlines() if 'CPU:' in line]
    cpu_facts = hardware.get_cpu_facts()
    assert len(line_cpu) == len(cpu_facts['processor'])

# Generated at 2022-06-13 00:46:15.764311
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    collector = FreeBSDHardwareCollector()
    assert collector._fact_class == FreeBSDHardware
    assert collector._platform == 'FreeBSD'

# Generated at 2022-06-13 00:46:25.767050
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    h = FreeBSDHardware()

    # kern.boottime returns seconds and microseconds as two 64-bits
    # fields, but we are only interested in the first field.
    struct_format = '@L'
    struct_size = struct.calcsize(struct_format)
    if len(h.boottime) < struct_size:
        raise AssertionError('boottime is too short: %r', h.boottime)

    (kern_boottime, ) = struct.unpack(struct_format, h.boottime[:struct_size])

    uptime_facts = h.get_uptime_facts()

    assert (kern_boottime == uptime_facts['uptime_seconds'] + h.now)

# Generated at 2022-06-13 00:46:47.004875
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')

        def get_bin_path(self, *args, **kwargs):
            if args[0] == 'dmidecode':
                return '/usr/sbin/dmidecode'
            else:
                return None


# Generated at 2022-06-13 00:46:57.461383
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # Create test modules object
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    test_module = object()
    test_module.run_command = lambda *args, **kwargs: (0, '', '')
    test_module.get_bin_path = lambda *args, **kwargs: '/bin/path'

    # Instantiate FreeBSDHardware class to populate
    fhw = FreeBSDHardware(module=test_module)
    collected_facts = fhw.populate()

    assert collected_facts.get('devicememory') is None
    assert collected_facts.get('boardmanufacturer') is None
    assert collected_facts.get('dnsdomain') is None
    assert collected_facts.get('manufacturer') is None
    assert collected_facts.get('productname') is None

# Generated at 2022-06-13 00:47:01.626700
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule({})
    hardwareCollector = FreeBSDHardwareCollector(module=module)

    # Collect facts
    hardware = hardwareCollector.collect()

    # If the collect method returns None, it means that
    # the plugin couldn't be collected
    assert hardware


# Unit test of the class FreeBSDHardware

# Generated at 2022-06-13 00:47:11.462601
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    fake_module = FakeAnsibleModule()
    hardware = FreeBSDHardware(fake_module)
    sysctl = ''
    hardware.module.get_bin_path = lambda x: sysctl
    hardware.module.run_command = lambda x: (0, '', '')
    facts = hardware.get_memory_facts()
    assert facts['memtotal_mb'] == 0
    assert facts['memfree_mb'] == 0

    sysctl = '/sbin/sysctl'
    hardware.module.get_bin_path = lambda x: sysctl
    out = '''hw.physmem: 4864169984
hw.pagesize: 4096
vm.stats.vm.v_page_count: 8111680
vm.stats.vm.v_free_count: 4036460
'''

# Generated at 2022-06-13 00:47:16.742027
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    x = {'vm.stats.vm.v_page_size': '4096', 'vm.stats.vm.v_page_count': '7358899', 'vm.stats.vm.v_free_count': '4516208'}
    y = {'swaptotal_mb': 314368, 'swapfree_mb': 314368, 'memtotal_mb': 29461, 'memfree_mb': 17480}
    f = FreeBSDHardware()
    assert f.get_memory_facts() == y

# Generated at 2022-06-13 00:47:28.865128
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # test value returned by sysctl is not valid (cannot be decoded)
    m = FreeBSDHardware(dict(module=dict()))
    m.module.run_command = lambda cmd, encoding=None: (
        0, 'not a valid struct', ''
    )
    assert m.get_uptime_facts() == {}

    # test when uptime is zero
    m = FreeBSDHardware(dict(module=dict()))
    m.module.run_command = lambda cmd, encoding=None: (
        0, b'\x00\x00\x00\x00\x00\x00\x00\x00', ''
    )
    assert m.get_uptime_facts() == {'uptime_seconds': 0}

    # test when uptime is greater than zero

# Generated at 2022-06-13 00:47:38.127378
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Create a dummy module and exit_json.
    module = type('', (object, ), {'exit_json': lambda x, y: None})()
    fb = FreeBSDHardware(module)

    # Create fake content of file /proc/meminfo

# Generated at 2022-06-13 00:47:44.611849
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    # create an object of the class FreeBSDHardware
    test_obj = FreeBSDHardware(dict())
    # use the object itself to mock the methods used in get_dmi_facts
    test_obj.get_bin_path = lambda x: x + '_bin'
    test_obj.run_command = lambda x, encoding=None: (0, x[0] + ' ' + x[1], None)
    # call the method get_dmi_facts
    dmi_facts = test_obj.get_dmi_facts()
    # compare the output with the expected output
    dmi_expect = dict()
    dmi_expect['bios_date'] = 'dmidecode_bin -s bios-release-date'
    dmi_

# Generated at 2022-06-13 00:47:53.652948
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)

    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts["processor_cores"] == "1", "The number of cores is wrong"
    assert cpu_facts["processor_count"] == "1", "The number of processor is wrong"
    assert cpu_facts["processor"] == ["Intel(R) Core(TM)2 Duo CPU     E8400  @ 3.00GHz"], "The processor data is wrong"



# Generated at 2022-06-13 00:48:02.329979
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class ModuleMock(object):
        def __init__(self, out):
            self.out = out
            self.run_command_calls = []
            self.bin_path_calls = []

        def get_bin_path(self, binary, required=True):
            self.bin_path_calls.append((binary, required))
            if self.out:
                return '/usr/bin/dmidecode'
            else:
                return None

        def run_command(self, binary):
            self.run_command_calls.append(binary)
            return 0, '# comment\nSuccess\n', ''

    fh = FreeBSDHardware()
    fh.module = ModuleMock(True)


# Generated at 2022-06-13 00:48:18.629388
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # Create the class object
    m = FreeBSDHardware(dict())
    rc, out, err = m.module.run_command('sysctl -n hw.ncpu')
    num_cpus = out.strip()
    rc, out, err = m.module.run_command('dmesg')  # using unicode
    cpu_facts = m.get_cpu_facts()
    assert cpu_facts['processor_count'] == num_cpus



# Generated at 2022-06-13 00:48:26.696842
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hw = FreeBSDHardware()

    rc, out, err = hw.module.run_command("echo 'machine amd64'")
    hw.module._sysctl_machine_arch = out.splitlines()[0].split()[1]
    rc, out, err = hw.module.run_command("echo 'hw.ncpu: 2'")
    hw.module.run_command = lambda x, **kwargs: (0, out, '')
    out = hw.get_cpu_facts()

    assert out['processor'] == [u'Intel(R) Xeon(R) CPU E5-2407 0 @ 2.20GHz']
    assert out['processor_count'] == u'2'
    assert out['processor_cores'] == u'1'



# Generated at 2022-06-13 00:48:29.870771
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc.platform == 'FreeBSD'
    assert fhc.fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:48:40.504276
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''Test FreeBSDHardware.get_dmi_facts with mocked dmidecode command output'''

    import copy
    import sys
    import unittest

    from ansible.module_utils import basic
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware as freebsd_hw
    from ansible.module_utils.facts.utils import get_file_content

    # Mock class AnsibleModule to allow returning hardcoded data
    class MockedAnsibleModule(basic.AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(MockedAnsibleModule, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 00:48:41.927536
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''Unit test for method get_dmi_facts of class FreeBSDHardware'''
    freebsd_hardware = FreeBSDHardware(None, None)
    result = freebsd_hardware.get_dmi_facts()
    assert result

# Generated at 2022-06-13 00:48:48.544062
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.collector.freebsd import FreeBSDHardware
    import sys

    # Stubbing x86_64-freebsd11.2-RELEASE-p7
    sys.modules['_struct'].calcsize = lambda x: 8

    test_kern_boottime = 1546300800.0  # Thu, 01 Jan 1970 00:00:00 GMT
    test_out = bytes(struct.pack('@L', test_kern_boottime))

    hardware = FreeBSDHardware()
    hardware._exec_module = lambda cmd, encoding: (0, test_out, '')

    uptime_facts = hardware.get_uptime_facts()
    assert(uptime_facts)
    assert(uptime_facts['uptime_seconds'] > 0)

# Generated at 2022-06-13 00:49:01.213893
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """
    Return the class to test and its expected output
    """

# Generated at 2022-06-13 00:49:09.514814
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = DummyModule()
    # DummyModule defines module.get_bin_path to return '/usr/bin/dmidecode'
    freebsd_hardware = FreeBSDHardware(module)
    dmi_facts = freebsd_hardware.get_dmi_facts()

# Generated at 2022-06-13 00:49:15.203221
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = FakeAnsibleModule()

    # Set dmidecode executable path
    module.get_bin_path = lambda v: "/usr/sbin/dmidecode"

    # Create instance of FreeBSDHardware class
    facts = module.collect_facts(FreeBSDHardware)

    # Check that all dmi facts are present
    for k in facts.keys():
        if "dmi" in k:
            assert(k in facts)



# Generated at 2022-06-13 00:49:22.891209
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class FakeModule:
        def __init__(self):
            self.fail_json = None
            self.run_command = None

    # Data from real output of dmidecode.

# Generated at 2022-06-13 00:49:50.361911
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hwc = FreeBSDHardwareCollector()
    assert(hwc.platform == 'FreeBSD')

# Generated at 2022-06-13 00:49:55.299107
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    hardware = FreeBSDHardware(module)

    facts = hardware.get_cpu_facts()
    assert 'Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz' in facts['processor']
    assert facts['processor_cores'] == '4'
    assert facts['processor_count'] == '1'


# Generated at 2022-06-13 00:50:01.946033
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Create a fake module to have access to get_bin_path
    fake_module = FakeModule()

    # Mock the sysctl command with a fixed output
    sysctl_cmd = '/sbin/sysctl -b kern.boottime'
    sysctl_output = b'\xdc\xd4\x0b\x00\x00\x00\x00\x00\x00\xc4\x00\x00\x00\x00\x00\x00'
    fake_module.run_command(sysctl_cmd, encoding=None).return_value = (0, sysctl_output, '')

    # Create a FreeBSDHardware instance and mock methods
    freebsd_hardware = FreeBSDHardware(fake_module)
    freebsd_hardware.module.get_bin_path = fake_module.get_

# Generated at 2022-06-13 00:50:12.248349
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class Module:
        def __init__(self):
            self.run_command_results = {'sysctl vm.stats -n hw.physmem': ('', '67108864', ''),
                                        'swapinfo -k': ('', 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%\n', '')}
            self.run_command_exceptions = set()

        def get_bin_path(self, arg, required=False):
            if arg == 'sysctl':
                return '/sbin/sysctl'
            if arg == 'swapinfo':
                return '/sbin/swapinfo'


# Generated at 2022-06-13 00:50:19.930541
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    """
    This method tests the get_uptime_facts method of class FreeBSDHardware.
    The method calls the get_uptime_facts method.

    """

    # Import classes required to test this method
    import sys, os
    import json
    import struct
    import time
    from ansible.module_utils.facts.hardware.base import Hardware
    from ansible.module_utils.facts.timeout import TimeoutError, timeout
    from io import StringIO
    from contextlib import contextmanager

    # For mocking
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError, timeout
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_file_content, get_

# Generated at 2022-06-13 00:50:22.864865
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    freebsd_hw = FreeBSDHardware(dict())
    result = freebsd_hw.populate()
    assert result.get('devices') is not None
    assert result.get('uptime_seconds') is not None

# Generated at 2022-06-13 00:50:24.816881
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    m = FreeBSDHardware({})
    out = m.get_uptime_facts()
    assert 'uptime_seconds' in out
    assert out['uptime_seconds'] > 0

# Generated at 2022-06-13 00:50:33.157890
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():

    module = MockAnsibleModule()

    # Dummy values for kern.boottime.
    # We need to make sure that time.time() returns an integer, so that we can
    # predict the result of the calculation.
    module.run_command.return_value = (0, struct.pack('@L', 100000), '')

    # Pretend that 100 seconds have elapsed since the system booted.
    time.time.return_value = 100

    hw = FreeBSDHardware(module)
    facts = hw.get_uptime_facts()

    # The result of the calculation is a float. Sometimes the fact contains
    # the float value, sometimes it's the integer value.
    assert facts['uptime_seconds'] in (89000, 89000.0)

# We need a mock for time.time(), and it must be a method of

# Generated at 2022-06-13 00:50:34.053957
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    pass

# Generated at 2022-06-13 00:50:43.038877
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''Test method get_dmi_facts'''
    module = AnsibleModuleMock()
    module.run_command = AnsibleModule_run_command


# Generated at 2022-06-13 00:51:27.156288
# Unit test for method populate of class FreeBSDHardware

# Generated at 2022-06-13 00:51:30.945819
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """This is to test whether the constructor of FreeBSDHardwareCollector is working or not"""

    hw_collector = FreeBSDHardwareCollector()
    assert hw_collector.platform == "FreeBSD"
    assert hw_collector.fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:51:40.730394
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat import unittest

    HardwareCollector._platform = 'FreeBSD'
    FreeBSDHardware.platform = 'FreeBSD'
    with unittest.mock.patch('ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware.get_cpu_facts'):
        FreeBSDHardware().populate()
    with unittest.mock.patch('ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware.get_memory_facts'):
        FreeBSDHardware().populate()
    with unittest.mock.patch('ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware.get_uptime_facts'):
        FreeBSDHardware().populate()

# Generated at 2022-06-13 00:51:49.344842
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class TestModule(object):
        def __init__(self):
            self.run_command_called = False
            self.run_command_rc = 0
            self.run_command_out = """
hw.ncpu: 1
"""
            self.run_command_err = ""

# Generated at 2022-06-13 00:51:53.866747
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    maclass = FreeBSDHardware()
    maclass.module = MockModule()
    maplatform = maclass.platform
    maclass.module.run_command = Mock(return_value=(0, 'hw.ncpu: 2', ''))
    maclass.module.run_command = Mock(return_value=(0, 'vm.stats.vm.v_page_size: 4096', ''))
    maclass.module.run_command = Mock(return_value=(0, 'vm.stats.vm.v_page_count: 447976', ''))
    maclass.module.run_command = Mock(return_value=(0, 'vm.stats.vm.v_free_count: 175176', ''))

# Generated at 2022-06-13 00:52:02.830481
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    test_obj = FreeBSDHardwareCollector()
    assert test_obj.platform == "FreeBSD"
    assert test_obj.not_a_virtual_machine() == None
    assert test_obj.virtual_machine() == None
    assert test_obj.ignore_virtual_facts() == None
    assert test_obj.collect()
    try:
        from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    except:
        assert test_obj._fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:52:06.902733
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    test_object = FreeBSDHardwareCollector()
    assert test_object.platform == 'FreeBSD'
    assert test_object.fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:52:12.489958
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = type('', (), {})()
    module.get_bin_path = lambda x: '/sbin/' + x
    module.run_command = lambda x: (0, '', '')
    module.exit_json = lambda **kwargs: None
    fs = FreeBSDHardwareCollector(module=module)
    facts = fs.collect()
    assert facts['devices']['da0'] == ['da0s1', 'da0s2']

# Generated at 2022-06-13 00:52:20.583920
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():

    from ansible.module_utils.facts.hardware.freebsd import get_memory_facts

    # Create a instance of FreeBSDHardware
    freebsd_hardware = FreeBSDHardware()

    # Mock the module
    freebsd_hardware.module = MagicMock()

    # Mock the method get_bin_path
    type(freebsd_hardware.module).get_bin_path = MagicMock(return_value="/bin/sysctl")

    # Mock the method run_command

# Generated at 2022-06-13 00:52:23.662789
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert isinstance(FreeBSDHardwareCollector._platform, str)
    assert isinstance(FreeBSDHardwareCollector._fact_class, type)
    assert issubclass(FreeBSDHardwareCollector._fact_class, Hardware)

# Generated at 2022-06-13 00:54:02.724199
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Set up
    module = MockModule()
    module.run_command.return_value = (0, B'\x00\x00\x00\x00\x00\x00\x1eU', None)
    freebsd_hardware = FreeBSDHardware(module)

    # Test
    expected = {
        'uptime_seconds': 123456789,
    }
    actual = freebsd_hardware.get_uptime_facts()

    # Verify
    assert actual == expected


# We need a mock for the module, but AnsibleModule does not allow
# a subclass to redefine a class member.
# So we define a new class that looks like AnsibleModule, but which
# allows us to redefine run_command.
# Note that we cannot use mock_module.run_command, as AnsibleModule
#

# Generated at 2022-06-13 00:54:12.985896
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class TestModule(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, name):
            return '/usr/sbin/dmidecode'

        def run_command(self, cmd, encoding=None):
            return self.rc, self.out, self.err

    # No dmidecode output
    rc, out, err = 0, '', ''
    test_module = TestModule(rc, out, err)
    facts = FreeBSDHardware(test_module).get_dmi_facts()
    assert not facts

    # Test dmidecode output

# Generated at 2022-06-13 00:54:21.890063
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys
    import pytest

    # Only run these tests if dmidecode is available.
    dmidecode_bin = 'dmidecode'
    if dmidecode_bin not in sys.modules.get("{}.utils.module_finder".format(__name__)).get_all_commands():
        pytest.skip("dmidecode is not installed")

    module = AnsibleModule(argument_spec={})
    if not sys.modules.get("{}.facts.hardware".format(__name__)).FreeBSDHardware.DMESG_BOOT:
        sys.modules.get("{}.facts.hardware".format(__name__)).FreeBSDHardware.DMESG_BOOT = "/dev/null"

    k = sys.modules.get("{}.facts.hardware".format(__name__)).FreeBSDHardware

# Generated at 2022-06-13 00:54:23.273948
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware_facts = FreeBSDHardwareCollector()
    assert hardware_facts.collect() == hardware_facts.facts


# Generated at 2022-06-13 00:54:30.760650
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    test_out = """
hw.ncpu: 4
hw.ncpuonline: 4
hw.model: Intel(R) Xeon(R) CPU E7-4870 v2 @ 2.30GHz
hw.machine: amd64
hw.usermem: 422646272
hw.physmem: 11019902976
hw.realmem: 11019902976
hw.ncpufound: 4
"""
    module = FakeModule()
    module.run_command = FakeRunCommand(out=test_out)

    obj = FreeBSDHardware(module)
    assert obj.get_cpu_facts() == {'processor': [], 'processor_count': '4', 'processor_cores': '1'}

    # Test with dmesg.boot file
    module = FakeModule()
    module.get_bin_path = lambda x: None


# Generated at 2022-06-13 00:54:35.489348
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # Mock a module
    module_mock = AnsibleModule(argument_spec={})
    module_mock.run_command = MagicMock(return_value=(0, '', ''))

    # Populate facts
    facts = FreeBSDHardware(module_mock).populate()

    # Assert method run_command is called with the right parameters
    module_mock.run_command.assert_called_with('sysctl vm.stats', check_rc=False)

    # Assert facts is not empty
    assert facts != {}



# Generated at 2022-06-13 00:54:39.301727
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """Test FreeBSDHardware.get_cpu_facts()
    """
    module = AnsibleModule(argument_spec={})
    harwd = FreeBSDHardware(module)
    cpu_facts = harwd.get_cpu_facts()
    assert cpu_facts['processor']
    assert cpu_facts['processor_cores']
    assert cpu_facts['processor_count']

# Generated at 2022-06-13 00:54:43.357819
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = FreeBSDHardware(module)
    facts = {}
    facts = hw.populate()

    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'devices' in facts

# Generated at 2022-06-13 00:54:52.947020
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """
    FreeBSDHardware.

    :returns: ``True`` if everything passed, ``False`` if something failed
    :rtype: ``bool``
    """
    class FreeModule:
        def __init__(self, output):
            self.output = output

        def run_command(self):
            return (0, self.output, '')

        def get_bin_path(self, _):
            return '/usr/sbin/dmidecode'


# Generated at 2022-06-13 00:55:01.788221
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class ModuleMock(object):
        def __init__(self):
            self.run_command_results = {}
            self._run_command_calls = []
        def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, encoding=None):
            self._run_command_calls.append({"args": args, "cwd": cwd})
            if args not in self.run_command_results:
                raise Exception("Unsupported call to run_command: %s" % args)
            else:
                return self.run_command_results[args]