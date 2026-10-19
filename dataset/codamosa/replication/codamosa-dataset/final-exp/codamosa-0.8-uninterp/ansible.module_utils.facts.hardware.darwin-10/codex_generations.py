

# Generated at 2022-06-13 00:34:54.818640
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware = {
        'osversion': '17.7.0',
        'model': 'MacBookPro3,1',
        'osrevision': '14F27',
        'processor_cores': 4,
        'memfree_mb': 2453,
        'memtotal_mb': 3072,
        'processor': 'Intel(R) Core(TM)2 Duo CPU     P8600  @ 2.40GHz',
        'uptime_seconds': 351628,
        'processor_vcpus': '',
    }
    hardware_collector = DarwinHardwareCollector()
    facts = hardware_collector.collect()
    assert facts == hardware

# Generated at 2022-06-13 00:35:07.136802
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import datetime
    import time
    import mock

    current_time = int(time.time())

    # mock module class
    class MockModule(object):
        def __init__(self):
            self._ansible_module_initialized = True

        def get_bin_path(self, program):
            return program

        def run_command(self, cmd, encoding=None):
            return 0, struct.pack('@L', current_time - 300), ''

    m = MockModule()
    facts = DarwinHardware(m).get_uptime_facts()
    assert 'uptime_seconds' in facts
    assert facts['uptime_seconds'] == 300


# Generated at 2022-06-13 00:35:17.475859
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path
    import sys

    sys.path.append("/Users/gaby/work/ansible/ansible/lib/ansible/module_utils/facts/hardware/")

    darwin_hardware = DarwinHardware()

    darwin_hardware.sysctl = {'kern.osversion': '15.6.0'}
    darwin_hardware.get_system_profile = lambda: {'Processor Speed': '2.7', 'Processor Name': 'Intel Core i7'}

    mac_facts = darwin_hardware.get_mac_facts()

    assert mac_facts['osversion'] == '15.6.0'

# Generated at 2022-06-13 00:35:25.306842
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    mac = DarwinHardware()
    mac.module = object()
    mac.module.run_command = lambda x: (0, 'Hardware:\n   Hardware Overview:\n      Model Name: MacBook Air\n      Model Identifier: MacBookAir7,2\n      Processor Name: Intel Core i5\n      Processor Speed: 1.3 GHz\n      Number of Processors: 1\n      Total Number of Cores: 2', '')
    assert 'MacBookAir7,2' == mac.get_system_profile()['Model Name']

# Generated at 2022-06-13 00:35:32.173099
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = FakeAnsibleModule()
    hardware = DarwinHardware(module)
    hardware.get_system_profile = MagicMock(return_value=system_profile)
    system_profile_facts = hardware.get_mac_facts()

    assert system_profile_facts['model'] == 'iMac12,1'
    assert system_profile_facts['osversion'] == '19.0.0'
    assert system_profile_facts['osrevision'] == 'Darwin Kernel Version 19.0.0: Thu Oct 17 16:17:15 PDT 2019; root:xnu-6153.41.3~29/RELEASE_X86_64'



# Generated at 2022-06-13 00:35:41.671429
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import os
    import shutil

    # Mock os.path.exists
    class mock_exists:
        def __init__(self):
            self.sysctl = False

        def __call__(self, file):
            if file == '/usr/sbin/system_profiler':
                return True
            return False

    def mock_run_command(module, args, encoding=None):
        if args[0] == '/usr/sbin/system_profiler' and args[1] == 'SPHardwareDataType':
            return 0, cmd5_out, ''

        return 1, '', ''

    # mock module
    import ansible.module_utils.facts.hardware.darwin
    class mock_module:
        def __init__(self):
            self.run_command = mock_run_command


# Generated at 2022-06-13 00:35:51.808693
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    """Unit test to verify that get_uptime_facts() returns the
    number of seconds since boot time.
    """
    # pylint: disable=unused-argument
    def mock_run_command(self, args, encoding=None):
        return 0, struct.pack('@L', 12345), ''

    import ansible.module_utils.facts.hardware.darwin as darwin
    darwin.Hardware.run_command = mock_run_command
    darwin.time = MockTime()
    assert darwin.Hardware().get_uptime_facts() == {'uptime_seconds': 12345}



# Generated at 2022-06-13 00:36:02.561069
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    """
    Provide input values and expected results for method get_memory_facts
    of class DarwinHardware
    """
    my_darwin_hardware = DarwinHardware()
    my_darwin_hardware.sysctl = {'hw.memsize': '4294967296'}
    assert my_darwin_hardware.get_memory_facts() == {'memtotal_mb': 4096, 'memfree_mb': 0}

    my_darwin_hardware = DarwinHardware()
    my_darwin_hardware.sysctl = {'hw.memsize': '4294967296'}

# Generated at 2022-06-13 00:36:09.909729
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # sysctl should return a string
    test_sysctl_output = b'\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03-\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Create an instance of class DarwinHardware
    mock_module = Mock(**{'run_command.return_value': (0, test_sysctl_output, '')})
    dar

# Generated at 2022-06-13 00:36:20.459829
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    darwin_hardware = DarwinHardware(dict(module=None))
    # non-existing file
    assert darwin_hardware.get_system_profile() == {}
    # empty file
    darwin_hardware._system_profile_fname = 'test/unittests/data/empty.txt'
    assert darwin_hardware.get_system_profile() == {}
    # test file
    darwin_hardware._system_profile_fname = 'test/unittests/data/system_profiler_SPHardwareDataType.txt'

# Generated at 2022-06-13 00:36:33.121027
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware_collector_object = DarwinHardwareCollector()
    assert hardware_collector_object._fact_class == DarwinHardware
    assert hardware_collector_object._platform == 'Darwin'


# Generated at 2022-06-13 00:36:35.080983
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = type('Module', (object,), {})
    mem_facts = DarwinHardware().get_memory_facts(module)
    assert 'memtotal_mb' in mem_facts
    assert 'memfree_mb' in mem_facts

# Generated at 2022-06-13 00:36:40.413105
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts import hardware_collectors
    mock_module = type('AnsibleModule', (object, ), {'command': lambda *args, **kw: (0, '0', ''),
                                                     'run_command': lambda *args, **kw: (0, '0', ''),
                                                     'get_bin_path': lambda *args, **kw: '/sbin/sysctl',
                                                     })()
    hardware_collectors.add_collector(DarwinHardwareCollector)
    mock_module.sysctl = get_sysctl(mock_module, ['hw', 'machdep', 'kern'])

# Generated at 2022-06-13 00:36:52.897143
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module)
    # Test with a brand string
    hardware.sysctl = {'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-4260U CPU @ 1.40GHz'}
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i5-4260U CPU @ 1.40GHz'
    assert cpu_facts['processor_cores'] == hardware.sysctl['machdep.cpu.core_count']
    assert cpu_facts['processor_vcpus'] == hardware.sysctl.get('hw.logicalcpu') or hardware.sysctl.get('hw.ncpu')
    # Test without a brand string
    hardware.sys

# Generated at 2022-06-13 00:37:03.700387
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Since DarwinHardware.get_cpu_facts() calls DarwinHardware.get_system_profile(),
    # and get_system_profile() calls macOS command "/usr/sbin/system_profiler",
    # we need to mock these 2 functions in order to do the unit tests.

    # Here is the mock data
    MOCK_SYSTEM_PROFILE = {
        'Processor Name': 'Intel Core i5',
        'Processor Speed': '3.3 GHz'
    }

    # Get a mock object of DarwinHardware, mock object of get_system_profile()
    # and mock object of sysctl
    mock_DarwinHardware = DarwinHardware()
    mock_DarwinHardware.get_system_profile = lambda: MOCK_SYSTEM_PROFILE

# Generated at 2022-06-13 00:37:13.485925
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts import hardware as hardware_module
    # Mock the required module for this unit test
    hardware_module.get_sysctl = lambda self, keys: {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz',
        'machdep.cpu.core_count': 4,
    }
    # Create an instance of DarwinHardware
    hardware = DarwinHardware(module=None)
    # Execute method get_cpu_facts
    cpu_facts = hardware.get_cpu_facts()
    # Assert that the result is correct

# Generated at 2022-06-13 00:37:23.546336
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = FakeAnsibleModule()
    dhw = DarwinHardware(module)

    class FakeVmStat:
        def __init__(self, rc, out):
            self.rc = rc
            self.out = out
            self.err = ''

    # This fake will return an error
    vmstat = FakeVmStat(1, '')
    dhw.module.run_command = lambda c: vmstat
    memory_facts = dhw.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 0
    assert memory_facts['memfree_mb'] == 0

    # This fake will return a valid run

# Generated at 2022-06-13 00:37:33.943603
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Check Intel i7 processor has 26 cores
    sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz',
        'machdep.cpu.core_count': 26,
        'hw.logicalcpu': 52
    }
    hardware = DarwinHardware(dict(module=None), sysctl=sysctl)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz'
    assert cpu_facts['processor_cores'] == 26
    assert cpu_facts['processor_vcpus'] == 52

    # Check PowerPC processor has 2 cores

# Generated at 2022-06-13 00:37:42.338504
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    dh = DarwinHardware(module=None)
    sysctl = get_sysctl(None, ['hw', 'machdep', 'kern'])

    facts = dh.populate()

    assert facts['processor']
    assert facts['processor_cores']
    assert facts['processor_vcpus']
    assert facts['memtotal_mb']
    assert facts['memfree_mb']
    assert facts['model']
    assert facts['osversion']
    assert facts['osrevision']
    assert facts['uptime_seconds']

# Generated at 2022-06-13 00:37:46.523871
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    # mock the system_profiler command
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    DarwinHardware.get_system_profile = lambda self: dict(
            ModelName='iMac9,1',
            ModelIdentifier='iMac9,1',
            ProcessorName='Intel Core 2 Duo',
            ProcessorSpeed='3.06 GHz'
            )

    # run test, then compare results
    output = DarwinHardware().get_cpu_facts()
    assert output['processor'] == 'Intel Core 2 Duo @ 3.06 GHz'

# Generated at 2022-06-13 00:38:15.845119
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, call

    import ansible.module_utils.facts.hardware.darwin as darwin

    sysctl_cmd = '/usr/bin/sysctl'
    struct_format = '@L'
    struct_size = struct.calcsize(struct_format)

    # The likely system uptime value in seconds, to be returned by time.time()
    likely_system_uptime = 1538624918

    class MockResponse():
        def __init__(self, return_code, out, err):
            self.returncode = return_code
            self.stdout = out
            self.stderr = err


# Generated at 2022-06-13 00:38:27.286093
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    fixture = DarwinHardware(dict())
    fixture.sysctl = dict()
    fixture.sysctl['hw.memsize'] = 2097152


# Generated at 2022-06-13 00:38:39.096317
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.system = 'Darwin'

    # Create a test instance of DarwinHardware
    darwinHardware = DarwinHardware(module)

    # Create a vm_stat command output
    vm_stat_output = '''Pages free:                              3159.
Pages active:                             2380.
Pages inactive:                           1582.
Pages wired down:                         2350.
Pages purgeable:                           285.
Pages speculative:                         45.
Pages throttled:                             0.
Pages wired down:                         2350.
Pages wired down transfer:                   0.
Pages purgeable:                           285.
Pages purgeable transfer:                    0.
'''

    # Inject the command output into the instance of DarwinHardware

# Generated at 2022-06-13 00:38:46.740087
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    dh = DarwinHardware(module)

    facts = dh.populate()

    assert facts['processor'] == 'Intel Core i5'
    assert facts['processor_cores'] == 2
    assert facts['processor_vcpus'] == 4
    assert facts['memtotal_mb'] == 8192
    assert facts['memfree_mb'] == 8192
    assert facts['model'] == 'MacBookAir4,2'
    assert facts['osversion'] == '15E65'
    assert facts['osrevision'] == '17'
    assert facts['uptime_seconds'] == 1000



# Generated at 2022-06-13 00:38:53.188917
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Test parameters
    module_args = dict()

    # Test objects
    module = AnsibleModule(
        argument_spec=module_args,
    )

    collected_facts = dict()
    darwin_hardware = DarwinHardware(module)

    # Test
    hardware_facts = darwin_hardware.populate(collected_facts)

    assert hardware_facts

# Generated at 2022-06-13 00:39:01.946095
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import mock
    import os

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils._text import to_bytes

    class MockModule(object):

        def __init__(self):
            self.run_command_results = [
                (0, os.urandom(8), ''),
            ]

        def get_bin_path(self, name):
            return name

        def run_command(self, args, encoding=None):
            return self.run_command_results.pop(0)

    class MockTime(object):

        def time(self):
            return 12345678

    def _run_get_uptime_facts(time_mock=MockTime()):
        module = MockModule()
        facts = DarwinHardware(module)

# Generated at 2022-06-13 00:39:08.725742
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModuleMock()
    hardware = DarwinHardware(module)
    hardware.sysctl = {
        'kern.osversion': '16.7.0',
        'kern.osrevision': '1500000'
    }
    mac_facts_dict = hardware.get_mac_facts()
    assert mac_facts_dict == {'osversion': '16.7.0', 'osrevision': '1500000'}


# Generated at 2022-06-13 00:39:18.343832
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = FakeAnsibleModule(
        dict(run_command=run_command_fake_success)
    )
    hardware = DarwinHardware(module)
    assert hardware.get_system_profile() == {
        'Model Name': 'MacBook Pro',
        'Model Identifier': 'MacBookPro6,2',
        'Processor Name': 'Intel Core i7',
        'Processor Speed': '2.66 GHz',
        'Memory': '8 GB',
        'Bus Speed': '1.07 GHz',
        'Boot ROM Version': 'MBP61.0057.B0F',
        'SMC Version': '1.57f17'
    }



# Generated at 2022-06-13 00:39:19.462291
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    d = DarwinHardware()
    assert 'Model Name' in d.get_system_profile()

# Generated at 2022-06-13 00:39:24.831594
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    hardware = DarwinHardware()
    hardware.sysctl = {'hw.memsize': (1 << 42)}
    hardware.module.run_command = lambda cmd: (0, 'Pages wired down: 0\nPages active: 100\nPages inactive: 200\n', '')
    result = hardware.get_memory_facts()
    assert result == {'memfree_mb': 0, 'memtotal_mb': 4398046511104}

# Generated at 2022-06-13 00:40:12.627258
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    f_class = DarwinHardware(dict())
    rc = 0
    out = "hw.model: iMac12,1"
    err = ""

    f_class.sysctl = dict()
    f_class.sysctl['kern.osversion'] = "1.2.3"
    f_class.sysctl['kern.osrevision'] = "4"

    facts = f_class.get_mac_facts()
    assert len(facts) == 3
    assert facts['model'] == "iMac12,1"
    assert facts['osversion'] == "1.2.3"
    assert facts['osrevision'] == "4"

# Generated at 2022-06-13 00:40:23.165777
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = MagicMock()
    command = ['sysctl', 'machdep.cpu.brand_string']
    module.run_command = Mock(return_value=(0, 'machdep.cpu.brand_string: Intel(R) Core(TM) i7-4578U CPU @ 3.00GHz', ''))
    hw = DarwinHardware(module)
    hw.sysctl = {'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-4578U CPU @ 3.00GHz'}
    assert hw.get_cpu_facts() == {'processor': hw.sysctl['machdep.cpu.brand_string'],
                                  'processor_cores': '',
                                  'processor_vcpus': ''}


# Generated at 2022-06-13 00:40:31.757069
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = MagicMock()
    module.run_command.return_value = (0, '', '')

# Generated at 2022-06-13 00:40:43.384660
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():

    from ansible.module_utils import basic
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    m_args = basic.AnsibleModuleArguments(dict())
    m_facts = basic.AnsibleModule(m_args)

# Generated at 2022-06-13 00:40:52.929829
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    import platform
    import sys
    import unittest

    class MacFactsTestModule(object):
        class ModuleFailException(Exception):
            pass

        def __init__(self, **kwargs):
            self.run_command_calls = 0
            self.params = kwargs

        def fail_json(self, msg, **kwargs):
            self.kwargs = kwargs
            raise MacFactsTestModule.ModuleFailException(msg)

        def run_command(self, cmd, encoding='utf-8'):
            self.run_command_calls += 1


# Generated at 2022-06-13 00:40:59.720551
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModuleMock()
    hardware = DarwinHardware(module)
    fact = 'osversion'

    rc0, out0, err0 = module.run_command("sysctl kern.osversion")
    rc1, out1, err1 = module.run_command("sysctl kern.osrevision")
    if rc0 != 0:
        out0 = ''
    if rc1 != 0:
        out1 = ''

    assert hardware.get_mac_facts()[fact] == out0.splitlines()[-1].split()[1]
    fact = 'osrevision'
    assert hardware.get_mac_facts()[fact] == out1.splitlines()[-1].split()[1]



# Generated at 2022-06-13 00:41:08.873541
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = MockModule()
    hardware = DarwinHardware(module)
    module.run_command.return_value = (0, """Hardware:

    Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro11,1
      Processor Name: Intel Core i7
      Processor Speed: 2.5 GHz
      Number of Processors: 1
      Total Number of Cores: 4
      L2 Cache (per Core): 256 KB
      L3 Cache: 6 MB
      Memory: 16 GB
      Boot ROM Version: MBP111.0138.B16
      SMC Version (system): 2.18f15
      Serial Number (system): 1234567890
      Hardware UUID: 00000000-0000-1000-8000-0026BB765291

""", '')
    facts = hardware.get_system_profile()

# Generated at 2022-06-13 00:41:11.129166
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    h = DarwinHardware()
    profile = h.get_system_profile()

# Generated at 2022-06-13 00:41:15.227753
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    platform = DarwinHardwareCollector._platform
    darwin_hardware_collector = DarwinHardwareCollector(platform, None)
    assert darwin_hardware_collector
    assert DarwinHardwareCollector._fact_class == DarwinHardware

# Generated at 2022-06-13 00:41:18.292154
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    obj = DarwinHardware()
    obj.module = MockModule()
    res = obj.get_system_profile()
    assert res['Processor Speed'] == '2.4 GHz'

# Generated at 2022-06-13 00:42:48.648290
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.hardware.darwin import get_sysctl

    try:
        get_sysctl(None, ['hw','machdep','kern'])
        # valid system
        assert DarwinHardware.get_mac_facts(None)
    except OSError:
        # mock out get_sysctl without running
        def get_sysctl(module, args):
            kern = {
                'osversion': '12.3.0',
                'osrevision': '15D21',
            }
            machdep = {
                'cpu.brand_string': '',
                'cpu.core_count': 2,
            }

# Generated at 2022-06-13 00:42:57.033319
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import tempfile
    import os

    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.write(b"Thu Jan  1 00:02:55 1970\n")
    tmp_file.close()


# Generated at 2022-06-13 00:43:05.115415
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    darwin_facts = DarwinHardware()
    darwin_facts.get_mac_facts = lambda s: {'model': 'MacBook', 'osversion': '10.6.5', 'osrevision': '10H574'}
    darwin_facts.get_cpu_facts = lambda s: {'processor': 'Intel', 'processor_cores': 4, 'processor_vcpus': 4}
    darwin_facts.get_memory_facts = lambda s: {'memtotal_mb': 16384, 'memfree_mb': 10000}
    darwin_facts.get_uptime_facts = lambda s: {'uptime_seconds': 15000}
    mac_facts = darwin_facts.populate()
    assert mac_facts['model'] == 'MacBook'

# Generated at 2022-06-13 00:43:07.665836
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.hardware.darwin import DarwinHardwareCollector
    # Test DarwinHardwareCollector
    fact_collector = FactCollector(DarwinHardwareCollector)

# Generated at 2022-06-13 00:43:09.282654
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    test = DarwinHardware()
    assert test.get_memory_facts() == {'memtotal_mb': 0, 'memfree_mb': 0}

# Generated at 2022-06-13 00:43:15.061779
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.common.text.utils import to_text
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.darwin import get_mac_facts
    from ansible.module_utils.facts import ModuleExecutor
    from ansible.module_utils.facts.hardware.base import get_file_content
    from ansible.module_utils.facts.hardware.base import Hardware, HardwareCollector
    from ansible.module_utils.facts.sysctl import get_sysctl

    class MockModule(object):

        def __init__(self):
            self.check_mode = False
            self.params = {}


# Generated at 2022-06-13 00:43:23.636401
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    hardware = DarwinHardware()
    hardware.module = AnsibleModuleStub()
    hardware.module.run_command = run_command_stub

    # Stub return value of run_command
    hardware.module.run_command.return_value = (0, 'Machine Name:  MacBook Pro\nMachine Model: MacBookPro6,2\n', '')

    # Call the method to be tested
    system_profile = hardware.get_system_profile()

    # Check that the output is a dict with the right values
    assert system_profile == {'Machine Name': 'MacBook Pro', 'Machine Model': 'MacBookPro6,2'}


# Generated at 2022-06-13 00:43:29.328716
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Mock module class
    class MockModule(object):
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, binary, required=False, opt_dirs=[]):
            return binary

        def run_command(self, binary, encoding=None):
            cmd = ' '.join(binary)
            if cmd == '/usr/sbin/system_profiler SPHardwareDataType':
                return (0, 'Processor Name: Intel Core i7\nProcessor Speed: 2.7 GHz\nTotal Number of Cores: 4\n', '')
            elif cmd == 'sysctl hw.model':
                return (0, 'hw.model: MacBookPro11,1\n', '')

# Generated at 2022-06-13 00:43:37.261829
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from io import StringIO
    output_data = """
Hardware:

Hardware Overview:

  Model Name: MacBook Pro
  Model Identifier: MacBookPro14,3
  Processor Name: Intel Core i7
  Processor Speed: 2.9 GHz
  Number of Processors: 1
  Total Number of Cores: 4
  L2 Cache (per Core): 256 KB
  L3 Cache: 8 MB
  Memory: 16 GB
  Boot ROM Version: MP61.0116.B24
  SMC Version (system): 2.45f0
  Serial Number (system): C02QXAQVFFT8
  Hardware UUID: 0BFC0E01-822D-54C2-88F7-C9B47B66B9FC"""

# Generated at 2022-06-13 00:43:46.128840
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    module.exit_json = lambda **kwargs: None
    darwin_hardware = DarwinHardware(module)
    darwin_hardware.sysctl = {
        'hw.memsize': '8589934592',
        'hw.physicalcpu': '4',
        'hw.logicalcpu': '4',
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz',
        'kern.osversion': '16.6.0',
        'kern.osrevision': '',
    }