

# Generated at 2022-06-13 00:34:58.505415
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.six.moves import StringIO

    module = FakeModule()

    dh = DarwinHardware(module)

    module.run_command.return_value = (0,
                                       "Hardware:\n"
                                       "    Hardware Overview:\n"
                                       "      Model Name: Mac Pro\n"
                                       "      Processor Name: Quad-Core Intel Xeon\n"
                                       "      Processor Speed: 2.66 GHz\n"
                                       "      Number of Processors: 1\n"
                                       "      Total Number of Cores: 4\n",
                                       '')
    system_profile = dh.get_system_profile()


# Generated at 2022-06-13 00:35:04.776144
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    # Crash test only, unless someone finds a way to setup a vm on Travis-ci.
    module = type('AnsibleModule', (object, ),
                  (dict(run_command=None, get_bin_path=None, params={})))()
    module.run_command = lambda *args, **kwargs: (1, '', '')

    DarwinHardware(module).populate(None)

# Generated at 2022-06-13 00:35:16.067984
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    """ This function runs a unit test for the populate function of DarwinHardware class """

    module = type('', (object,), {
        'run_command': run_command_mock,
        'get_bin_path': get_bin_path_mock
    })();

    darwin_hardware_instance=DarwinHardware(module)
    darwin_hardware_instance.sysctl=sysctl_mock

    assert darwin_hardware_instance.populate() == populated_mock



# Generated at 2022-06-13 00:35:25.254102
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.side_effect = lambda x: x
    hardware = DarwinHardware(module)
    hardware.sysctl['machdep.cpu.brand_string'] = 'Intel'
    hardware.sysctl['machdep.cpu.core_count'] = 2
    hardware.sysctl['hw.ncpu'] = 2
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == "Intel"
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_vcpus'] == 2


# Generated at 2022-06-13 00:35:33.264907
# Unit test for method get_uptime_facts of class DarwinHardware

# Generated at 2022-06-13 00:35:42.469745
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import datetime
    from time import time

    # Set mocked time
    timestamp = time()
    # Subtract one year from the current time
    delay = 365*24*60*60
    kern_boottime = int(timestamp) - delay
    darwin_hardware = DarwinHardware({}, {})

    # Mocking struct.unpack()
    def my_unpack(format, out):
        return (kern_boottime, )

    darwin_hardware.struct.unpack = my_unpack
    # End of mocking

    uptime_facts = darwin_hardware.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == int(timestamp) - kern_boottime
    assert uptime_facts['uptime_years'] == 1
    assert uptime_

# Generated at 2022-06-13 00:35:55.266210
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = MockModule()
    darwin_hw = DarwinHardware(module=module)

    darwin_hw.sysctl = {
        'hw.memsize': 4294967296,
        'kern.osversion': '15.0.0',
        'kern.osrevision': '14A389',
        'hw.processor_count': 2,
        'hw.physicalcpu': 4,
    }


# Generated at 2022-06-13 00:36:05.321798
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    _mock_module = BaseFactCollector._mock_module


# Generated at 2022-06-13 00:36:15.996171
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module_mock = AnsibleModuleMock()
    module_mock.run_command = Mock()
    module_mock.run_command.return_value = (0, vm_stat_mock, '')
    memory_facts = DarwinHardware(module_mock).get_memory_facts()
    assert memory_facts['memtotal_mb'] == 4091
    assert memory_facts['memfree_mb'] == 148

    module_mock.run_command.return_value = (0, vm_stat_cpu_usage_mock, '')
    # In this mock, CPU is not idle. So, memfree_mb should be less than in example above.
    memory_facts = DarwinHardware(module_mock).get_memory_facts()
    assert memory_facts['memtotal_mb'] == 4091
    assert memory_facts

# Generated at 2022-06-13 00:36:18.843326
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    my_obj = DarwinHardwareCollector()
    assert my_obj.platform == 'Darwin'
    assert my_obj._platform == 'Darwin'
    assert my_obj._fact_class == DarwinHardware

# Generated at 2022-06-13 00:36:49.263453
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.cache import Cache
    from ansible.module_utils.facts.collector.darwin import DarwinHardwareCollector

    fake_module = FakeModule()
    fake_module.params = {}
    cache = Cache(fake_module)

    facts = ansible_facts.AnsibleFacts(fake_module)
    hw = DarwinHardwareCollector(fake_module)

    hw.populate(facts, cache)

    assert isinstance(facts['ansible_processor'], str)
    assert isinstance(facts['ansible_processor_cores'], int)
    assert isinstance(facts['ansible_processor_vcpus'], int)
    assert isinstance(facts['ansible_memtotal_mb'], int)

# Generated at 2022-06-13 00:36:59.082980
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    test_host = DarwinHardware()
    sysctl_result = {'hw.logicalcpu': 4, 'hw.physicalcpu': 4}
    system_profile_result = {'Processor Speed': '2.3 GHz (2.3 GHz)', 'Processor Name': 'Intel Core i7'}
    sysctl_result_keys = list(sysctl_result.keys())
    test_host.sysctl = sysctl_result
    test_host.get_system_profile = lambda: system_profile_result
    cpu_facts = test_host.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel Core i7 @ 2.3 GHz (2.3 GHz)'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_vcpus'] == 4

# Generated at 2022-06-13 00:37:10.363626
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = FakeAnsibleModule()
    hardware = DarwinHardware(module)
    _, out, _ = module.run_command(['/usr/sbin/system_profiler', 'SPHardwareDataType'])
    _, sysctl_out, _ = module.run_command(['sysctl', 'hw', 'machdep.cpu.brand_string'])
    module.run_command.side_effect = [(0, out, ''), (0, sysctl_out, '')]
    module.get_bin_path.return_value = '/usr/bin/vm_stat'
    _, vmstat_out, _ = module.run_command(['/usr/bin/vm_stat'])

# Generated at 2022-06-13 00:37:19.905213
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    class ModuleStub():
        def __init__(self):
            self.run_command_count = 0

        def run_command(self, args, check_rc=False):
            if self.run_command_count == 0:  # SPHardwareDataType
                self.run_command_count += 1

# Generated at 2022-06-13 00:37:31.030212
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    """Unit test for DarwinHardware.get_mac_facts"""
    test_facts = {
        'osrevision': '15.3.0', 'osversion': 'Darwin Kernel Version 15.3.0: Thu Dec 10 18:40:58 PST 2015; root:xnu-3248.30.4~1/RELEASE_X86_64', 'model': 'Macmini7,1'
    }
    darwin_hardware = DarwinHardware()
    module = AnsibleModuleMock()
    darwin_hardware.module = module
    darwin_hardware.get_mac_facts()
    for key in test_facts.keys():
        module.fail_json.assert_called_with(msg='Failed to retrieve hardware facts for Darwin. Missing %s' % (key))



# Generated at 2022-06-13 00:37:35.977121
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = DarwinHardware(module)
    facts = hardware.populate()

    assert facts['uptime_seconds'] > 0
    assert facts['memfree_mb'] <= facts['memtotal_mb']
    assert facts['processor']
    assert facts['processor_cores']
    assert facts['processor_vcpus']



# Generated at 2022-06-13 00:37:45.517815
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class Module:
        def __init__(self):
            self.run_command_rc = 0

# Generated at 2022-06-13 00:37:47.196305
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware_collector = DarwinHardwareCollector()
    assert hardware_collector.fact_class == DarwinHardware
    assert hardware_collector.platform == 'Darwin'

# Generated at 2022-06-13 00:37:55.358907
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = object()
    module.run_command = lambda cmd: (0, 'test', None)

    hardware = DarwinHardware(module)
    facts = hardware.populate()

    assert 'model' in facts
    assert 'osversion' in facts
    assert 'osrevision' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'uptime_seconds' in facts
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_vcpus' in facts



# Generated at 2022-06-13 00:38:00.588382
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    mock_module = Mock()
    mock_module.run_command.return_value = (0, '''
Mach Virtual Memory Statistics: (page size of 4096 bytes)
Pages free:                              16288.
Pages active:                            61291.
Pages inactive:                          87718.
Pages speculative:                        4319.
Pages throttled:                              0.
Pages wired down:                        23027.
Pages purgeable:                          2674.
"Translation faults":                  1286457.
Pages copy-on-write:                     21821.
Pages zero filled:                     1656010.
Pages reactivated:                        3358.
Pageins:                                  1677.
Pageouts:                                   23.
Object cache: 4 hits of 8575 lookups (0% hit rate)
''', '')

# Generated at 2022-06-13 00:38:30.305212
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    mac_module = MagicMock()

    mac_module.run_command.return_value = (0, '''\
Mach Virtual Memory Statistics: (page size of 4096 bytes)
Pages free:                               1068.
Pages active:                            48120.
Pages inactive:                          48028.
Pages speculative:                        8232.
Pages throttled:                              0.
Pages wired down:                        27226.
Pages purgeable:                          9228.
"Translation faults":                 44705984.
Pages copy-on-write:                   12847231.
Pages zero filled:                    15305409.
Pages reactivated:                     14945711.
Pageins:                              12098817.
Pageouts:                                  725.
Object cache: 9 hits of 1153 lookups (0% hit rate)
''', '')
    dh = DarwinHardware()


# Generated at 2022-06-13 00:38:41.260814
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class ModuleMock():
        def __init__(self):
            self.run_command_result = (0, "Mach Virtual Memory Statistics: (page size of 16384 bytes)", "")

        def run_command(self, command):
            return self.run_command_result

    class DarwinHardwareMock(DarwinHardware):
        def __init__(self, module):
            self.sysctl = {
                "machdep.cpu.brand_string": 'Intel(R) Xeon(R) CPU E5-2699 v3 @ 2.30GHz',
                "machdep.cpu.core_count": 1,
                "hw.physicalcpu": 1,
                "hw.memsize": 4294967296,
            }
            self.module = module

# Generated at 2022-06-13 00:38:44.650493
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    mac_darwin = DarwinHardware()
    mac_darwin.sysctl = dict()
    mac_darwin.sysctl['hw.memsize'] = 8589934592
    assert mac_darwin.get_memory_facts()['memtotal_mb'] == 8192


# Generated at 2022-06-13 00:38:46.431498
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    obj = DarwinHardwareCollector()
    assert obj.platform == 'Darwin'
    assert issubclass(obj.fact_class, DarwinHardware)

# Generated at 2022-06-13 00:38:57.708732
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = MockAnsibleModule()
    hardware = DarwinHardware(module=module)
    hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-4258U CPU @ 2.40GHz',
        'machdep.cpu.core_count': 2
    }
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i5-4258U CPU @ 2.40GHz'
    assert cpu_facts['processor_cores'] == 2

    hardware.sysctl = {
        'hw.logicalcpu': 2,
        'hw.physicalcpu': 2
    }
    cpu_facts = hardware.get_cpu_facts()

# Generated at 2022-06-13 00:39:10.034681
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule({}, {})
    hardware = DarwinHardware(module)
    module.run_command = MagicMock(
        return_value = (0, 'Intel(R) Xeon(R) CPU E5-2699 v3 @ 2.30GHz\n', ''))
    module.get_bin_path = MagicMock(return_value='/usr/sbin/system_profiler')
    rc, out, err = module.run_command(["/usr/sbin/system_profiler", "SPHardwareDataType"])

    hardware.sysctl = {'machdep.cpu.brand_string': 'Intel'}
    facts = hardware.get_cpu_facts()
    assert 'Intel' in facts['processor']


# Generated at 2022-06-13 00:39:21.301151
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.facts import AnsibleFacts

    # mock the module
    module = AnsibleFacts.mock_module

    # mock the hardware
    hardware = DarwinHardware()
    hardware.module = module

    # facts to be tested - replace with actual values
    osversion = '19.0.0'
    osrevision = '19A583'
    model = 'MacBook Pro (Retina, 13-inch, Mid 2014)'
    expected_facts = {
        'osversion': osversion,
        'osrevision': osrevision,
        'model': model
    }

    # mock the sysctl dictionary

# Generated at 2022-06-13 00:39:32.102253
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = FakeModule()

    file_content = {
        '/usr/sbin/system_profiler': '',
        '/sbin/sysctl': '',
    }

    # test for intel platform

    def set_side_effect_sysctl_intel(*args, **kwargs):
        if args[0] == 'hw.model':
            return ('', '', 0), 'hw.model: Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz', ''
        elif args[0] == 'machdep.cpu.brand_string':
            return ('', '', 0), 'machdep.cpu.brand_string: Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz', ''

# Generated at 2022-06-13 00:39:40.715495
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    DarwinHardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-2720QM CPU @ 2.20GHz',
        'machdep.cpu.core_count': 4,
        'hw.memsize': 17179869184,
        'kern.osversion': '16.7.0',
        'kern.osrevision': '15000',
        'hw.physicalcpu': 2,
        'hw.logicalcpu': 4,
        }
    DarwinHardware.get_system_profile = lambda self: {
        'Processor Name': 'Intel Core i7',
        'Processor Speed': '2.2 GHz',
        }

# Generated at 2022-06-13 00:39:46.955053
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.sysctl import get_sysctl
    class MockModule:
        def __init__(self):
            self.run_command_args_list = []
            self.run_command_response_list = [
                (0, "Pages wired down:         65164\nPages active:            4161806\nPages inactive:          4166355\nPages free:              256410\n", "")
            ]
        def run_command(self, cmd, encoding=None):
            self.run_command_args_list.append(cmd)
            return self.run_command_response_list.pop()
        def get_bin_path(self, cmd):
            return cmd

    module_obj = MockModule()


# Generated at 2022-06-13 00:40:31.469826
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware = DarwinHardware()
    mac_facts = hardware.get_mac_facts()
    cpu_facts = hardware.get_cpu_facts()
    memory_facts = hardware.get_memory_facts()
    uptime_facts = hardware.get_uptime_facts()
    hardware_facts = hardware.populate()

    assert hardware_facts['model'] == mac_facts['model'] == mac_facts['product_name']
    assert hardware_facts['osversion'] == mac_facts['osversion']
    assert hardware_facts['osrevision'] == mac_facts['osrevision']
    assert hardware_facts['processor'] == cpu_facts['processor']
    assert hardware_facts['processor_cores'] == cpu_facts['processor_cores'] == hardware_facts['processor_vcpus']
    assert hardware_facts['memtotal_mb']

# Generated at 2022-06-13 00:40:42.758296
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule({})

    darwin_hardware = DarwinHardware(module)
    darwin_hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz',
        'machdep.cpu.core_count': '4',
        'hw.memsize': '17179869184',
        'kern.osversion': '16.7.0',
        'kern.osrevision': '1510',
        'hw.physicalcpu': '4',
    }
    hardware_facts = darwin_hardware.populate()

    assert hardware_facts['model'] == 'MacBookPro11,2'

# Generated at 2022-06-13 00:40:52.637140
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(argument_spec=dict())
    module.run_command = MagicMock(return_value=[0, 'hw.model: MacBookAir7,1', ''])
    module.get_bin_path = MagicMock(return_value='/usr/sbin/system_profiler')

    dh = DarwinHardware(module)
    module.run_command = MagicMock(return_value=[0, 'kern.osversion: 15.6.0', ''])
    module.get_bin_path = MagicMock(return_value='/usr/sbin/system_profiler')
    mac_facts = dh.get_mac_facts()
    assert mac_facts['model'] == 'MacBookAir7,1'
    assert mac_facts['osversion'] == '15.6.0'
    assert mac_

# Generated at 2022-06-13 00:40:57.349098
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = Mock(return_value=(0, "hw.model: x86_64", ""))
    hardware = DarwinHardware(module)
    facts = hardware.get_mac_facts()
    assert 'model' in facts
    assert facts['model'] == 'x86_64'
    assert 'osversion' in facts
    assert 'osrevision' in facts


# Generated at 2022-06-13 00:41:01.909417
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, 'hw.model: xv\n', None)

    h = DarwinHardware(module)
    facts = h.get_mac_facts()
    assert facts['model'] == 'xv'
    assert facts['osversion'] == h.sysctl['kern.osversion']
    assert facts['osrevision'] == h.sysctl['kern.osrevision']

# Generated at 2022-06-13 00:41:04.781607
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils._text import to_bytes

    dh = DarwinHardware({})
    res = dh.get_uptime_facts()
    assert res['uptime_seconds'] == int(time.time())


# Generated at 2022-06-13 00:41:12.235730
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.hardware.darwin import get_memory_facts
    class TestModule(object):
        def run_command(self, command, encoding=None):
            return 0, 'Pages wired down: 2. Pages active: 3. Pages inactive: 4.', ''
    test_module = TestModule()
    test_hardware = DarwinHardware(test_module)
    test_hardware.sysctl = {'hw.memsize': 1610612736}
    test_hardware._fact_class = DarwinHardware
    test_hardware.get_memory_facts()
    assert test_hardware.facts['memtotal_mb'] == 1536
    assert test_hardware

# Generated at 2022-06-13 00:41:22.017157
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import unittest
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    class test_DarwinHardware_get_uptime_facts(unittest.TestCase):
        def setUp(self):
            self.hardware = DarwinHardware()
            self.hardware.module = MockModule()

        def test_get_uptime_facts(self):
            expected_result = {
                'uptime_seconds': 1500
            }
            # The value of kern.boottime is simulated by test_command_run_command
            result_uptime_facts = self.hardware.get_uptime_facts()
            self.assertEqual(result_uptime_facts, expected_result)

    # Mock class for module

# Generated at 2022-06-13 00:41:26.227581
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    module_mock = type('module_mock', (object,),
                       {'run_command': lambda x: (0, 'output', 'error')})
    instance = DarwinHardwareCollector(module_mock)
    assert instance.platform == 'Darwin'
    assert instance._fact_class == DarwinHardware


# Generated at 2022-06-13 00:41:32.212781
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    mac_hw = DarwinHardware(module)
    rc, out, err = module.run_command("sw_vers -productName", encoding=None)
    mac_hw.sysctl = {'kern.osversion': out}

    mac_hw.populate()

# Generated at 2022-06-13 00:42:57.304219
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    """
    Unit test for method get_uptime_facts of class DarwinHardware
    :return:
    """
    output_dict_expected = {
        'uptime_seconds': -1,
    }

    mock_module = Mock()
    type(mock_module).run_command = Mock(return_value=(0, b'', ''))

    darwin = DarwinHardware(mock_module)
    mock_module.get_bin_path = Mock(return_value='/usr/sbin/sysctl')
    darwin.module = mock_module
    uptime_output = darwin.get_uptime_facts()

    assert uptime_output == output_dict_expected

    mock_module = Mock()

# Generated at 2022-06-13 00:43:05.114878
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import sys
    import os
    import unittest
    import tempfile
    from ansible.module_utils._text import to_bytes
    module = None

    class MyDarwinHardware(DarwinHardware):
        def __init__(self, module):
            self.module = module

    class TestModule(object):
        def __init__(self):
            self.run_command_stub_out = None

        def run_command(self, args, encoding=None):
            assert args == ["/usr/sbin/system_profiler", "SPHardwareDataType"]
            return (0, self.run_command_stub_out, None)


# Generated at 2022-06-13 00:43:08.201114
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = fake_ansible_module()
    facts_d = DarwinHardware(module).get_cpu_facts()
    assert facts_d is not None
    assert 'processor_cores' in facts_d
    assert 'processor' in facts_d
    assert 'processor_vcpus' in facts_d


# Generated at 2022-06-13 00:43:11.639754
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    collector = DarwinHardwareCollector({'ansible_facts': {}})
    hardware = DarwinHardware(collector)
    mac_facts = hardware.get_mac_facts({'module': None})
    assert mac_facts['osversion'] != ''
    assert mac_facts['osrevision'] != ''

# Generated at 2022-06-13 00:43:15.227390
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module)
    memory_facts = hardware.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts

# Generated at 2022-06-13 00:43:24.868821
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    data = dict()

    data['sysctl'] = dict(hw=dict(model='MacPro6,1', memsize='800000000', physicalcpu='2', logicalcpu='2'),
                          machdep=dict(cpu=dict(brand_string='Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz')),
                          kern=dict(osversion='15.5.0', osrevision='Darwin Kernel Version 15.5.0: Thu Apr 28 21:41:34 PDT 2016; root:xnu-3248.50.21~8/RELEASE_X86_64'))

    data['run_command'] = dict(
        __getitem__=lambda self, x: dict(
            rc=0,
            out='',
            err=''
        )
    )

    obj = DarwinHardware

# Generated at 2022-06-13 00:43:34.226418
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    hardware = DarwinHardware()
    hardware.module = AnsibleModuleMock()
    hardware.module.run_command.return_value = (0, "hw.model: MacBookPro6,2\n", '')
    hardware.sysctl = {
        'kern.osversion': '15.6.0',
        'kern.osrevision': '1418',
    }
    assert hardware.get_mac_facts() == {
        'model': 'MacBookPro6,2',
        'product_name': 'MacBookPro6,2',
        'osversion': '15.6.0',
        'osrevision': '1418',
    }



# Generated at 2022-06-13 00:43:36.395183
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    dh = DarwinHardware()
    system_profile = dh.get_system_profile()
    assert system_profile.get('Model Name') == 'iMac'

# Generated at 2022-06-13 00:43:45.241491
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = AnsibleModuleMock()
    cmd_run = module.run_command
    sysctl_cmd = module.get_bin_path('sysctl')

    # Define a default boot time that is one day ago
    boottime = int(time.time() - (24 * 60 * 60))

    def mock_cmd_run(*args, **kwargs):
        cmd = args[0]
        assert kwargs.get('encoding') is None
        assert cmd is not None and len(cmd) == 3
        assert cmd[0] == sysctl_cmd
        assert cmd[1] == '-b'
        assert cmd[2] == 'kern.boottime'
        return 0, struct.pack('@L', boottime), ''


# Generated at 2022-06-13 00:43:52.602557
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import sys
    import StringIO
    import unittest
    import mock
    import ansible.module_utils.common.process

    # Mock module
    module = mock.Mock()
    module.run_command = ansible.module_utils.common.process.run_command
    module.get_bin_path = lambda x: 'vm_stat'

    # Mock module_utils.common.process.run_command
    vm_stat_output = ''
    with open('test/runner/facts/vm_stat') as vm_stat_file:
        for line in vm_stat_file:
            vm_stat_output += line
        sys.modules['ansible.module_utils.common.process'].run_command.return_value = (0, vm_stat_output, '')

    # Mock sysctl
    sysctl_