

# Generated at 2022-06-13 00:34:54.001052
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    pass

# Generated at 2022-06-13 00:34:59.974660
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class MockModule:
        def __init__(self):
            self.run_command_result = 0
            self.run_command_out = b'\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05'
            self.get_bin_path_name = 'sysctl'
            self.get_bin_path_result = '/usr/bin/sysctl'

        def run_command(self, cmd, encoding):
            assert cmd == ['/usr/bin/sysctl', '-b', 'kern.boottime']
            if self.run_command_result == 0:
                return (self.run_command_result, self.run_command_out, '')
            else:
                return (self.run_command_result, '', '')

       

# Generated at 2022-06-13 00:35:09.343841
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    test = DarwinHardware({'module_setup': True})
    test.sysctl = {
        'hw.memsize': '1125899906842624',  # 1TiB
        'hw.physicalcpu': '1',
        'hw.logicalcpu': '2',
    }

    # Test with vm_stat installed
    original_get_bin_path = get_bin_path
    def mock_get_bin_path(name, opt_dirs=[]):
        if name == 'vm_stat':
            return '/path/to/vm_stat'
        else:
            return original_get_bin_path(name, opt_dirs)
    get_bin_path = mock_get_bin_path

    import ansible.module_utils.basic

# Generated at 2022-06-13 00:35:18.569465
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = get_module_mock()
    sysctl_cmd = module.get_bin_path('sysctl')
    darwin_hardware = DarwinHardware(module)
    out = b'{ sec = 123456; usec = 0 }\n'
    darwin_hardware.module.run_command.return_value = (0, out, '')

    result = darwin_hardware.get_uptime_facts()

    darwin_hardware.module.run_command.assert_called_once_with([sysctl_cmd, '-b', 'kern.boottime'], encoding=None)

    assert result['uptime_seconds'] == int(time.time()) - 123456



# Generated at 2022-06-13 00:35:21.213901
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert(DarwinHardwareCollector._platform == 'Darwin')
    assert(issubclass(DarwinHardwareCollector._fact_class, Hardware))


# Generated at 2022-06-13 00:35:30.943556
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec=dict())

    hardware_obj = DarwinHardware()
    hardware_obj.module = module

    # Mock method 'get_mac_facts', method 'get_cpu_facts', method 'get_memory_facts', method 'get_uptime_facts'
    hardware_obj.get_mac_facts = MagicMock(return_value={'osversion': '15.6.0', 'osrevision': '15G1212'})
    hardware_obj.get_cpu_facts = MagicMock(return_value={'processor_vcpus': '4', 'processor': 'Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz', 'processor_cores': '4'})

# Generated at 2022-06-13 00:35:40.504042
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    mac = DarwinHardware()

# Generated at 2022-06-13 00:35:46.842025
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Instantiate a DarwinHardware object
    dh = DarwinHardware(dict())

    # Test on PowerPC platform
    dh.sysctl = {'hw.logicalcpu': 3,
                 'hw.physicalcpu': 2,
                 'hw.cputype': 18,
                 'hw.cpusubtype': 9}
    assert dh.get_cpu_facts() == {'processor_vcpus': '3',
                                  'processor': 'PowerPC G3',
                                  'processor_cores': '2'}

    # Test on Intel platform
    dh.sysctl = {'machdep.cpu.brand_string': 'Core i7',
                 'machdep.cpu.core_count': 4}

# Generated at 2022-06-13 00:35:58.062462
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    def run_command_mock(self, args, encoding=None, errors=None, binary=False):
        return 0, '1334718045', None

    import sys
    import ctypes
    if sys.platform == 'darwin':
        dylib = ctypes.CDLL('libc.dylib')
        dylib.time.restype = ctypes.c_int
        dylib.time.argtypes = [ctypes.POINTER(ctypes.c_int)]

        darwin_time = dylib.time(None)
        assert darwin_time == 1334718045

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    dh = DarwinHardware(None)
    dh.get_uptime_facts = run_command_mock
    result = dh.get_

# Generated at 2022-06-13 00:36:00.090182
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hc = DarwinHardwareCollector(None)
    assert isinstance(hc, DarwinHardwareCollector)

# Generated at 2022-06-13 00:36:15.068572
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector._fact_class is not None
    assert darwin_hardware_collector._platform is not None
    assert darwin_hardware_collector._fact_class.__name__ == 'DarwinHardware'
# end of the unit test

# Generated at 2022-06-13 00:36:21.167353
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from tests.module_utils import AnsibleModule
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    d = DarwinHardware(module)
    sp = d.get_system_profile()
    assert sp['Hardware UUID'] == '3D85E6E0-6D95-5410-9C95-8BFA0F2048D7'

# Generated at 2022-06-13 00:36:24.916567
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    class TestModule:
        def run_command(self, command):
            return (0, "", "")
    module = TestModule()
    fact_class = DarwinHardware(module)
    assert fact_class.get_cpu_facts() == {}


# Generated at 2022-06-13 00:36:29.442185
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    """ Unit test for method get_mac_facts of class DarwinHardware """
    darwin_hardware = DarwinHardware()
    system_profile = darwin_hardware.get_system_profile()
    mac_facts = darwin_hardware.get_mac_facts()
    assert mac_facts['model'] == system_profile['Model Name']

# Generated at 2022-06-13 00:36:31.999800
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = None
    memory_facts = DarwinHardware.get_memory_facts(None)
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts

# Generated at 2022-06-13 00:36:39.427706
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import sys
    import ansible.module_utils.facts.hardware.darwin as test_module
    h = test_module.DarwinHardware()

    system_profile = h.get_system_profile()
    current_python_version = sys.version_info[:2]

    assert (len(system_profile) > 0), \
        "DarwinHardware().get_system_profile() should return a dict with at least one key. Received %s" \
        % system_profile
    assert (("Model Name" in system_profile) or ("Processor Name" in system_profile)), \
        "DarwinHardware().get_system_profile() returned an unexpected result: %s" \
        % system_profile



# Generated at 2022-06-13 00:36:50.323008
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    # Define a test class that overrides the get_raw_uptime function
    class DarwinHardwareTest(DarwinHardware):
        def get_raw_uptime(self):
            # This is an output of sysctl -b kern.boottime on macOS 10.14.6
            return b'\x00\x00\x00\x00\x00\x00\x00\xc3\xd9X\x1b\x00\x00\x00\x00\x00\x00'

    dh = DarwinHardwareTest()

    assert dh.get_uptime_facts() == {'uptime_seconds': 1570466117}

# Generated at 2022-06-13 00:36:59.702527
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    system_profiler_path = get_bin_path('system_profiler')
    if system_profiler_path is None:
        module.fail_json(msg="system_profiler is not available in the system")
    dh = DarwinHardware(module)
    system_profile = dh.get_system_profile()
    if system_profile:
        module.exit_json(ansible_facts=dict(
            system_profile=system_profile
        ))
    else:
        module.fail_json(msg="system_profiler failed to run")



# Generated at 2022-06-13 00:37:01.853785
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hw_collector = DarwinHardwareCollector()
    assert hw_collector.platform == 'Darwin'

# Generated at 2022-06-13 00:37:12.200775
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import time
    import unittest
    import subprocess

    def secs_from_boot(date):
        try:
            return int(time.time() - subprocess.check_output('sysctl -b kern.boottime'.split()).split(',')[0])
        except:
            return 0

    class TestDarwinHardware(DarwinHardware):
        def get_uptime_facts(self):
            return super(TestDarwinHardware, self).get_uptime_facts()

    # On Darwin, the default format is annoying to parse.
    # Use -b to get the raw value and decode it.
    sysctl_cmd = subprocess.check_output('which sysctl'.split()).decode("utf-8")
    cmd = [sysctl_cmd, '-b', 'kern.boottime']

    #

# Generated at 2022-06-13 00:37:38.415457
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule()
    module.run_command = MagicMock(return_value=(0, 'hw.model: iMac15,1', ''))
    module.get_bin_path = MagicMock(return_value='/sbin/sysctl')
    mac_facts = DarwinHardware(module).get_mac_facts()
    assert mac_facts == {'model': 'iMac15,1', 'product_name': 'iMac15,1', 'osversion': '19.6.0', 'osrevision': '17G7024'}


# Generated at 2022-06-13 00:37:46.430013
# Unit test for method populate of class DarwinHardware

# Generated at 2022-06-13 00:37:52.218624
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hardware = DarwinHardware(module)
    hardware.sysctl = {
        'hw.physicalcpu': 2,
        'hw.logicalcpu': 4,
        'hw.ncpu': 4
    }

    system_profile = {
        'System Version': '10.10.5',
        'System Model': 'MacPro6,1',
        'Boot ROM Version': '186.0.0.0.0',
        'Hardware Overview': 'Mac Pro (Late 2013)'
    }

    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_vcpus'] == 4

    hardware.sysctl = {
        'hw.physicalcpu': 4
    }

    cpu_facts = hardware.get_

# Generated at 2022-06-13 00:37:54.548139
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """
    Unit test for constructor of class DarwinHardwareCollector

    Returns:
        None

    """
    collector = DarwinHardwareCollector()
    assert collector
    assert collector.platform == 'Darwin'
    assert collector.fact_class == 'DarwinHardware'


# Generated at 2022-06-13 00:38:00.343341
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.system.base import dummy_module
    from ansible.module_utils.facts.system.base import DummySysctl

    m = dummy_module(sysctl=DummySysctl(kern_boottime=0, hw_memsize=1024*1024*1024))
    osfamily = DarwinHardware(m)
    osfamily.sysctl = dict()
    osfamily.sysctl['hw.memsize'] = b'1048576000'

    total_used = 0
    page_size = 4096
    vm_stat_command = b'/usr/bin/vm_stat'

    rc, out, err = m.run_command(vm_stat_command)

# Generated at 2022-06-13 00:38:05.863546
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    test = DarwinHardware()
    test.sysctl = { 'kern.osversion': '19.6.0', 'kern.osrevision': '15G1004' }
    rc, out, err = test.module.run_command("sysctl hw.model")
    rc, out, err = test.module.run_command("sysctl hw.model")
    test.get_mac_facts()


# Generated at 2022-06-13 00:38:14.492665
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.common import get_platform
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collector import get_collector_instance

    if get_platform().startswith('Darwin'):
        facts = Facts(dict(), dict())

        hwcollector = get_collector_instance(facts)
        hwcollector.collect(facts)
        hw = facts.get('hardware')

        assert isinstance(hw, DarwinHardware)

        system_profile = hw.get_system_profile()

        if system_profile:
            assert 'Processor Name' in system_profile
            assert 'Processor Speed' in system_profile
        else:
            assert False

# Generated at 2022-06-13 00:38:16.651477
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    d = DarwinHardwareCollector()
    assert d is not None

# Generated at 2022-06-13 00:38:22.440325
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Set up some input variables
    test_module = AnsibleModule(argument_spec={'gather_subset': dict(type='list')}, supports_check_mode=False)
    darwin_collector = DarwinHardwareCollector(test_module)


# Generated at 2022-06-13 00:38:34.195972
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "", ""))
    module.get_bin_path = MagicMock(return_value="")
    module.run_command = MagicMock(return_value=(0, "", ""))
    hardware = DarwinHardware(module)


# Generated at 2022-06-13 00:39:15.829343
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = FakeModule()
    hardware = DarwinHardware(module)
    hardware.populate()
    assert hardware.facts['model'] == 'MacBookPro12,1'
    assert hardware.facts['osversion'] == '16.7.0'
    assert hardware.facts['osrevision'] == '16G2073'


# Generated at 2022-06-13 00:39:16.800375
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    rhc = DarwinHardwareCollector()
    assert rhc.collect() != None

# Generated at 2022-06-13 00:39:22.861937
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Create a test module
    class TestModule(object):
        def __init__(self):
            self.run_command_results = [(0, 'test_out', ''), (0, 'test_out', '')]
            self.run_command_calls = []
            self.params = {'gather_subset': 'all'}

        def run_command(self, cmd, encoding=None):
            self.run_command_calls.append(cmd)
            return self.run_command_results.pop(0)

        def get_bin_path(self, arg):
            return 'vm_stat'

    test_module = TestModule()
    test_module_results = {'memtotal_mb': 0, 'memfree_mb': 0}

    # Mock the behavior of vm_stat command
    # In this

# Generated at 2022-06-13 00:39:25.419154
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware_collector = DarwinHardwareCollector()
    assert hardware_collector._fact_class == DarwinHardware
    assert hardware_collector._platform == 'Darwin'

# Generated at 2022-06-13 00:39:35.984049
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import pytest

    memtotal_mb = 8192
    memfree_mb = int(memtotal_mb * .20)
    memory_facts = {
        'memtotal_mb': memtotal_mb,
        'memfree_mb': memfree_mb,
    }

    memfree_out = "Pages free:                    1453.\n".encode('ascii')
    memtotal_out = "Mach Virtual Memory Statistics: (page size of 4096 bytes)\n".encode('ascii')

    mock_device = DarwinHardware()
    mock_device.module = MagicMock()


# Generated at 2022-06-13 00:39:36.724054
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hwc = DarwinHardwareCollector()
    assert hwc is not None

# Generated at 2022-06-13 00:39:44.082773
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    '''Unit test for method populate'''


# Generated at 2022-06-13 00:39:53.251731
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import json
    import sys

    mocked_module = type('module', (object,), {
        'run_command': lambda self, cmd: (0, json.dumps({
            '/usr/sbin/system_profiler SPHardwareDataType': {
                'out': 'Hardware:    Mac Pro\n Model Name:   Mac Pro\n  Processor Name:   Quad-Core Intel Xeon\n  Processor Speed:   2.8 GHz',
                'rc': 0
            }
        })[cmd[0].strip() + ' '.join(cmd[1:])], '')
    })()

    d = DarwinHardware(mocked_module)
    facts = {}
    facts.update(d.populate())

    sys.stdout.write(json.dumps(facts))

if __name__ == '__main__':
    test_

# Generated at 2022-06-13 00:40:03.594827
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware = DarwinHardware()
    hardware.module.run_command = Mock(return_value=(0, 'test output', ''))
    hardware.get_mac_facts = Mock(return_value={'test_mac_fact': 'test'})
    hardware.get_cpu_facts = Mock(return_value={'test_cpu_fact': 'test'})
    hardware.get_memory_facts = Mock(return_value={'test_memory_fact': 'test'})
    hardware.get_uptime_facts = Mock(return_value={'test_uptime_fact': 'test'})
    result = hardware.populate()
    assert 'test_mac_fact' in result
    assert 'test_cpu_fact' in result
    assert 'test_memory_fact' in result
    assert 'test_uptime_fact' in result

# Generated at 2022-06-13 00:40:09.150460
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = TestGetbinpath
    hardware_collection = DarwinHardwareCollector(module=module)
    hardware = hardware_collection.collect()[0]
    hardware_info = hardware.get_cpu_facts()
    assert hardware_info['processor'] == 'Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz'
    assert hardware_info['processor_cores'] == 4
    assert hardware_info['processor_vcpus'] == 8



# Generated at 2022-06-13 00:41:29.457657
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModuleMock()
    hardware = DarwinHardware(module)
    facts = hardware.populate()
    assert 'model' in facts
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'osversion' in facts
    assert 'osrevision' in facts
    assert 'uptime_seconds' in facts


# Generated at 2022-06-13 00:41:30.935528
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    obj = DarwinHardwareCollector()
    assert obj.platform == 'Darwin'

# Generated at 2022-06-13 00:41:39.909675
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import tempfile
    import os

    f, path = tempfile.mkstemp()
    profiledata = """Hardware:

    Hardware Overview:

      Model Name: Mac Pro
      Model Identifier: MacPro1,1
      Processor Name: 2.66 GHz Quad-Core Intel Xeon
      Processor Speed: 2.66 GHz
      Number of Processors: 2
      Total Number of Cores: 8
      L2 Cache (per Processor): 12 MB
      Memory: 8 GB
      Bus Speed: 1.33 GHz
      Boot ROM Version: MP11.005C.B08
      SMC Version (system): 1.7f10
      Serial Number (system): XXXXXXXXXXX
      Hardware UUID: XXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

    [...]

    """


# Generated at 2022-06-13 00:41:42.067507
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    result = DarwinHardwareCollector()
    assert result.__class__.__name__ == 'DarwinHardwareCollector'
    assert result._platform == 'Darwin'
    assert result._fact_class == DarwinHardware


# Generated at 2022-06-13 00:41:52.629094
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    import platform
    import sys
    import unittest

    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.collector.darwin import DarwinHardware

    class FakeModule(object):
        def run_command(self, command, encoding=None):
            if command == ['sysctl', 'hw.model']:
                return (0, b'hw.model: MacBookPro12,1\n', b'')
            elif command == ['sysctl', 'machdep.cpu.brand_string']:
                return (0, b'machdep.cpu.brand_string: Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz\n', b'')
            elif command == ['sysctl', 'machdep.cpu.core_count']:
                return

# Generated at 2022-06-13 00:42:01.150025
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():

    # Init module
    class FakeModule(object):

        def __init__(self):
            self.run_command_calls = 0
            self.run_command_results = [
                # Ok
                (0, "hw.memsize: 12345678\n", ""),
                (0, "kern.osversion: 15A284\n", ""),
                (0, "kern.osrevision: 15A284\n", ""),
                (0, "hw.model: MacBookPro12,1\n", ""),
            ]

        def run_command(self, args, encoding=None):
            result = self.run_command_results[self.run_command_calls]
            self.run_command_calls += 1
            return result

    fake_module = FakeModule()

    # Init hardware


# Generated at 2022-06-13 00:42:09.038746
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Arrange
    DarwinHardware_obj = DarwinHardware()
    DarwinHardware_obj.sysctl = {'hw.memsize': 2**64}
    vm_stat_command = '/usr/bin/vm_stat'

    mock_run_command = MagicMock(return_value=(0, mock_vm_stat_output, ''))
    with patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware.module.run_command', mock_run_command):
        # Act
        memory_facts = DarwinHardware_obj.get_memory_facts()

        # Assert
        expected_memory_facts = {
            'memtotal_mb': 9223372036854775807,
            'memfree_mb': 55769,
        }
        assert memory_facts == expected_memory_facts
       

# Generated at 2022-06-13 00:42:11.404305
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    collector = DarwinHardwareCollector()
    assert collector.platform == 'Darwin'

# Generated at 2022-06-13 00:42:20.760858
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    # Import Ansible Mock
    try:
        from unittest.mock import MagicMock, patch, PropertyMock
    except ImportError:
        from mock import MagicMock, patch, PropertyMock

    # Create a mock module object with run_command
    mock_module = MagicMock()

# Generated at 2022-06-13 00:42:22.646465
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    obj = DarwinHardwareCollector()
    assert obj.platform == 'Darwin'
    obj._collect(None) # make pylint happy