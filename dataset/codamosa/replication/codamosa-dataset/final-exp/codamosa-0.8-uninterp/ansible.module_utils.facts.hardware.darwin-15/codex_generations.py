

# Generated at 2022-06-13 00:34:58.291488
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    mock_module = Mock()
    mock_module.run_command.return_value = (0, '1565783179', '')
    mock_module.get_bin_path.return_value = '/usr/sbin/sysctl'

    # Test normalized output
    d = DarwinHardware(mock_module)
    d.module = mock_module
    uptime_facts = d.get_uptime_facts()
    assert uptime_facts == {'uptime_seconds': 1565783207}

# Generated at 2022-06-13 00:35:08.080039
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system import System
    from ansible.module_utils.facts.collector import BaseCollector
    from ansible.module_utils.facts import fact_cache
    import os


# Generated at 2022-06-13 00:35:12.387179
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import unittest
    import mock

    module = mock.Mock()
    module.run_command.return_value = (0, b'{ sec = 1501402313, usec = 727101 }', '')
    module.get_bin_path.return_value = 'sysctl'

    hardware = DarwinHardware(module=module)

    uptime_facts = hardware.get_uptime_facts()
    assert 'uptime_seconds' in uptime_facts
    assert uptime_facts['uptime_seconds'] == int((time.time() - 1501402313))



# Generated at 2022-06-13 00:35:19.753269
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import json
    from ansible.module_utils._text import to_bytes

    # The output of `/usr/sbin/system_profiler SPHardwareDataType`

# Generated at 2022-06-13 00:35:29.902361
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import re
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    source_string = """
    Hardware:

    Hardware Overview:

      Model Name: Mac Pro
      Model Identifier: MacPro5,1
      Processor Name: Quad-Core Intel Xeon
      Processor Speed: 2.93 GHz
      Number of Processors: 1
      Total Number of Cores: 4
      L2 Cache (per Core): 256 KB
      L3 Cache: 8 MB
      Memory: 12 GB
      Processor Interconnect Speed: 4.8 GT/s
      Boot ROM Version: MP51.0089.B00
      SMC Version (system): 1.39f5
      Serial Number (system): XXXXXXXXXX
      Hardware UUID: XXXXXXXXXX
      Sudden Motion Sensor:
      State: Enabled

    """

    source_string

# Generated at 2022-06-13 00:35:39.989946
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import os
    import tempfile

    # This would need to get moved to test/unit/plugins/modules/test_facts.py
    # but for now it's easier to keep the 2 tests together for the time being.
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.facts import AnsibleFactCollector


# Generated at 2022-06-13 00:35:50.733180
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Create a test module and set the return values of the module_utils.common.process.get_bin_path function
    module = AnsibleModule(argument_spec=dict())
    module.get_bin_path = Mock(return_value=sysctl_cmd)

    # Create a mock sysctl command that returns the correct initial time
    sysctl_cmd = '/usr/sbin/sysctl'
    sysctl_return = struct.pack('@L', initial_time)

    # Create a DarwinHardware object
    hardware_facts = DarwinHardware(module)

    # Call the get_uptime_facts function to get the uptime facts
    uptime_facts = hardware_facts.get_uptime_facts()

    # Check that the uptime_seconds is set correctly, depending on the
    # initial_time variable

# Generated at 2022-06-13 00:35:58.198599
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Run test without gathered facts
    module = MagicMock(run_command=MagicMock(return_value=(0, '', '')))
    hw = DarwinHardware(module)
    # The following will fail if populate() fails to return a dictionary
    x = hw.populate()

    # Run test with gathered facts
    m1 = MagicMock(return_value=dict())
    module = MagicMock(run_command=m1)
    hw = DarwinHardware(module)
    x = hw.populate(dict())



# Generated at 2022-06-13 00:36:07.621449
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    start_time = int(time.time()) - 100
    # Create a file with fake data
    (sysctl_fd, sysctl_out) = tempfile.mkstemp()
    os.write(sysctl_fd, struct.pack('@L', start_time))
    os.close(sysctl_fd)

    # Create a MockModule for the get_uptime_facts method
    m = MockModule()
    m.run_command = Mock(return_value=(0, sysctl_out, ''))
    m.get_bin_path = Mock(return_value='sysctl')
    dhw = DarwinHardware()
    uptime_facts = dhw.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] >= 100

    # Clean up
    os.remove(sysctl_out)

# Generated at 2022-06-13 00:36:12.989233
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    darwin_hardware = DarwinHardware(module)
    output = darwin_hardware.populate()

    module.exit_json(
        changed=False,
        ansible_facts={
            'ansible_hardware': output
        }
    )

# Generated at 2022-06-13 00:36:24.916321
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hw = DarwinHardwareCollector()
    assert darwin_hw._fact_class == DarwinHardware
    assert darwin_hw._platform == 'Darwin'

# Generated at 2022-06-13 00:36:33.724155
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    facts_dict = dict()

    # Make sure to return empty dicts for all fact groups
    darwin_hardware = DarwinHardware()
    facts_dict = darwin_hardware.populate()

    assert facts_dict['processor'] is not None
    assert facts_dict['processor_cores'] is not None
    assert facts_dict['processor_vcpus'] is not None
    assert facts_dict['memtotal_mb'] is not None
    assert facts_dict['memfree_mb'] is not None
    assert facts_dict['model'] is not None
    assert facts_dict['osversion'] is not None
    assert facts_dict['osrevision'] is not None
    assert facts_dict['uptime_seconds'] is not None

# Generated at 2022-06-13 00:36:43.415179
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware import DarwinHardware
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import get_collector
    from ansible.module_utils.six import BytesIO

    # Create the module
    module = AnsibleModule(
        argument_spec=dict()
    )

    # Create a mock uptime file
    kern_boottime = int(time.time()) - 5000
    uptime_file_content = BytesIO()
    uptime_file_content.write(to_bytes(struct.pack('@L', kern_boottime)))

    # Create a mock Collector
    # Mock

# Generated at 2022-06-13 00:36:55.950487
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class MockVmstatModule:
        def __init__(self, output='', rc=0):
            self.output = output
            self.rc = rc

        def run_command(self, command):
            return self.rc, self.output, ''

    module = MockVmstatModule('Cache:         4')

    mac_facts = DarwinHardware()
    mac_facts.module = module
    memory_facts = mac_facts.get_memory_facts()
    assert memory_facts == {'memfree_mb': 0,
                            'memtotal_mb': 0}


# Generated at 2022-06-13 00:37:08.276174
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_module = lambda: None
    test_module.run_command = lambda x: (0, 'Serial Number (system): W81496RE0N\nMemory: 16 GB\nProcessor Name: Intel Core i5\nProcessor Speed: 3.2 GHz\nProcessor Number: 2', '')
    test_module.params = {}

    darwin_hw = DarwinHardware(test_module)
    system_profile = darwin_hw.get_system_profile()
    assert system_profile['Serial Number (system)'] == 'W81496RE0N'
    assert system_profile['Memory'] == '16 GB'
    assert system_profile['Processor Name'] == 'Intel Core i5'
    assert system_profile['Processor Speed'] == '3.2 GHz'
    assert system_profile['Processor Number']

# Generated at 2022-06-13 00:37:18.546216
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    '''
    Test module facts.
    '''
    mac = '''hw.model: MacBookAir6,2
kern.osversion: 15D21
kern.osrevision:    15D21
kern.boottime: { sec = 1459009875, usec = 0 }
    '''
    mac_facts = '''hw.model: MacBookAir6,2
kern.osversion: 15D21
kern.osrevision:    15D21
'''
    expected_mac_facts = {
        'model': 'MacBookAir6,2',
        'osversion': '15D21',
        'osrevision': '15D21'
    }

    mac_test = DarwinHardware(dict(), mac)
    assert mac_test.get_mac_facts() == expected_mac_facts



# Generated at 2022-06-13 00:37:23.757364
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts import ansible_runner

    runner = ansible_runner.AnsibleRunner(callback='datastore', object_database_update=False)
    runner.run(pattern='ansible.module_utils.facts.hardware.darwin', module='setup')

    assert runner.datastore is not None
    assert 'ansible_uptime_seconds' in runner.datastore
    assert isinstance(runner.datastore['ansible_uptime_seconds'], int)

# Generated at 2022-06-13 00:37:34.145833
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import module_utils.facts.hardware.darwin as darwin
    darwin_hardware = darwin.DarwinHardware({})
    darwin_hardware.module = MagicMock()

# Generated at 2022-06-13 00:37:39.685755
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():

    # Create a mock module, just for the purpose of testing
    # this constructor
    class MockModule:
        def __init__(self):
            self.params = {}

    module = MockModule()

    # Check the constructor, without fail_on_errors
    hwc = DarwinHardwareCollector(module)
    assert hwc is not None

# Generated at 2022-06-13 00:37:41.298542
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware_collector = DarwinHardwareCollector()
    assert hardware_collector.collect()

# Generated at 2022-06-13 00:38:12.092269
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    content = """Hardware:

    Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro9,2
      Processor Name: Intel Core i7
      Processor Speed: 2.3 GHz
      Number of Processors: 1
      Total Number of Cores: 4
      L2 Cache (per Core): 256 KB
      L3 Cache: 6 MB
      Memory: 8 GB
      Boot ROM Version: MBP91.00D3.B0C
      SMC Version (system): 2.3f36
      Serial Number (system): C02KQ0WUDVH5
      Hardware UUID: FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF

    """

    hardware = DarwinHardware()
    hardware.module.run_command = lambda _: (0, content, '')
    profile = hardware.get_system_profile()



# Generated at 2022-06-13 00:38:16.001309
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector.platform == 'Darwin'
    assert darwin_hardware_collector._fact_class.platform == 'Darwin'
    assert darwin_hardware_collector._fact_class is DarwinHardware

# Generated at 2022-06-13 00:38:27.459726
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})

    def test_run_command(self, command_line, check_rc=True, close_fds=True, executable=None, use_unsafe_shell=False, encoding=None,
                         errors='surrogate_then_replace', env_strings=None, data=None, binary_data=True,
                         path_prefix=None, cwd=None, prompt_regex=None, remove_tmp_files=True, tmp_path=None,
                         log_files=True, copy_path=None, process_ids=None, binary_output=False):
        test_processor_cores = '4'
        test_memtotal_mb = '2'
        test_model = 'MEOW'
        test_osversion = 'CAT'

# Generated at 2022-06-13 00:38:28.767559
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware_collector = DarwinHardwareCollector()
    assert hardware_collector is not None

# Generated at 2022-06-13 00:38:40.429129
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    """
    Test for method get_cpu_facts of class DarwinHardware
    """
    module = 'ansible.module_utils.facts.hardware.darwin'
    m = __import__(module)
    class_ = getattr(getattr(m, 'hardware'), 'DarwinHardware')
    method = getattr(class_, 'get_cpu_facts')
    sysctl_intel = {'machdep.cpu.brand_string': 'Intel', 'machdep.cpu.core_count': '4'}
    sysctl_ppc = {'hw.physicalcpu': '2'}
    system_profile = {'Processor Name': 'PowerPC', 'Processor Speed': '1GHz'}

# Generated at 2022-06-13 00:38:48.336086
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    # This test is not part of the CI workflow.
    import unittest

    class MyTestCase(unittest.TestCase):
        def test_DarwinHardware_get_system_profile(self):
            darwin = DarwinHardware()
            self.assertEqual(darwin.get_system_profile(), {
                'Model Identifier': 'MacBookPro6,2',
                'Processor Name': 'Intel Core 2 Duo',
                'Processor Speed': '2.4 GHz',
                'Number of Processors': '1',
                'Total Number of Cores': '2',
                'L2 Cache (per Core)': '256 KB',
                'L3 Cache': '3 MB',
                'Memory': '8 GB'
            })


# Generated at 2022-06-13 00:38:59.110229
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware = DarwinHardware()


# Generated at 2022-06-13 00:39:08.634215
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = get_mock_module()

    run_command_expectations = [
        (('sysctl hw.model',), {'rc': 0, 'stdout': 'hw.model: MacBookPro6,2\n'}),
    ]

    module.run_command = get_mock_command(run_command_expectations)

    result = DarwinHardware._get_mac_facts(module)

    assert result['model'] == 'MacBookPro6,2'
    assert result['osversion'] == '15.6.0'
    assert result['osrevision'] == '199506'



# Generated at 2022-06-13 00:39:09.635197
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    obj = DarwinHardwareCollector()
    assert obj.collect() is not None

# Generated at 2022-06-13 00:39:16.935883
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=[], type='list'),
        }
    )
    # Test DarwinHardware class fetching
    d = DarwinHardware(module)
    facts = d.populate()
    # Test DarwinHardwareCollector class fetching
    c = DarwinHardwareCollector(module)
    facts = c.collect()
    assert len(facts) != 0



# Generated at 2022-06-13 00:40:05.827976
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    darwin_hw = DarwinHardware(dict())
    darwin_hw.sysctl = {'kern.osversion':'10.12.3', 'kern.osrevision':'16D32'}
    darwin_hw._run_command = lambda cmd, encoding: (0, 'hw.model: MacBookPro11,4\n', '')
    assert darwin_hw.get_mac_facts() == {'osversion': '10.12.3',
                                         'osrevision': '16D32',
                                         'model': 'MacBookPro11,4',
                                         'product_name': 'MacBookPro11,4'}


# Generated at 2022-06-13 00:40:11.758660
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    darwin_hardware = DarwinHardware(module)

    system_profile = darwin_hardware.get_system_profile()

    assert system_profile != dict()
    assert 'Serial Number (system)' in system_profile
    assert 'Model Name' in system_profile
    assert 'Hardware UUID' in system_profile

    module.exit_json(changed=False)



# Generated at 2022-06-13 00:40:19.206595
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Create a mock module
    mock_module = type('AnsibleModule', (object,), dict(params={}))()
    # Create an instance of DarwinHardware
    dhw = DarwinHardware(mock_module)
    dhw.sysctl = get_sysctl(mock_module, ['hw', 'machdep', 'kern'])
    dhw.get_system_profile = lambda: {}
    # Mock method get_mac_facts to return empty dictionary
    dhw.get_mac_facts = lambda: {}
    # Mock method get_cpu_facts to return empty dictionary
    dhw.get_cpu_facts = lambda: {}
    # Mock method get_memory_facts to return empty dictionary
    dhw.get_memory_facts = lambda: {}
    # Mock method get_uptime_facts to return empty dictionary
    d

# Generated at 2022-06-13 00:40:30.062878
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class TestModule:
        def get_bin_path(self, filename, opts=None):
            return 'echo'

        def run_command(self, cmd, encoding=None):
            return (0, 'kern.boottime = {sec=1585204019, usec=110496}', '')

    class TestFacts:
        def __init__(self):
            pass

        def __getitem__(self, key):
            return None

        def get(self, key, default=None):
            return None

    testModule = TestModule()
    testFacts = TestFacts()
    testFacts.module = testModule
    testFacts._platform = 'Darwin'

    assert testFacts.get_uptime_facts() == {'uptime_seconds': 1585204019}

# Generated at 2022-06-13 00:40:42.127551
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    # Force the platform to Darwin for testing
    module.params['ansible_facts']['ansible_system'] = 'Darwin'
    Collector.set_module(module)
    obj = DarwinHardwareCollector(module)
    cpu_facts = obj.collect()['cpu']
    # Test the simplest case, with the sysctl value 'machdep.cpu.brand_string'
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i5-5287U CPU @ 2.90GHz'
    assert cpu_facts['processor_cores'] == '4'

    # Test the

# Generated at 2022-06-13 00:40:44.527396
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    result = DarwinHardwareCollector.get_uptime_facts(False)
    assert result['uptime_seconds'] >= 0

# Generated at 2022-06-13 00:40:45.216701
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert DarwinHardwareCollector._platform == 'Darwin'

# Generated at 2022-06-13 00:40:47.390872
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hc = DarwinHardwareCollector()
    assert hc._platform == 'Darwin'
    assert hc._fact_class == DarwinHardware


# Generated at 2022-06-13 00:40:49.179860
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    Facts = DarwinHardwareCollector()
    assert Facts._fact_class == DarwinHardware
    assert Facts._platform == 'Darwin'

# Generated at 2022-06-13 00:40:57.888565
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    h = DarwinHardware()
    h._get_sysctl = lambda: {"hw.model": "Pentium II",
                             "hw.physicalcpu": 1,
                             "hw.ncpu": 2}
    assert h.get_cpu_facts() == {"processor": "Pentium II",
                                 "processor_cores": 1,
                                 "processor_vcpus": 2}

    h = DarwinHardware()
    h._get_sysctl = lambda: {"machdep.cpu.brand_string": "Intel(R) Core(TM) i5-5287U CPU @ 2.90GHz",
                             "machdep.cpu.core_count": 2,
                             "hw.physicalcpu": 2,
                             "hw.ncpu": 4}

# Generated at 2022-06-13 00:42:17.927527
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    system_profile = DarwinHardware.get_system_profile()

    assert system_profile.__class__ == dict

    if "Model Identifier" not in system_profile:
        raise AssertionError("System profile missing 'Model Identifier'.")


# Generated at 2022-06-13 00:42:26.257202
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    mac = DarwinHardware(module)

    # Create a test fixture using a string from vm_stat output and the expected result
    test = dict()
    test['name'] = 'Darwin 14.3.0 Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64'

# Generated at 2022-06-13 00:42:33.210036
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # This test is to assert or reject the output of the method
    # get_cpu_facts of class DarwinHardware when given below input
    # This test is valid only on Darwin Hardware
    import sys
    facts = dict()
    facts['distribution'] = sys.platform
    input_sysctl = dict()
    # Case 1
    input_sysctl['machdep.cpu.brand_string'] = 'Intel(R) Core(TM) i5 CPU 2.4GHz'
    input_sysctl['machdep.cpu.core_count'] = 4
    input_sysctl['machdep.cpu.thread_count'] = 4
    input_sysctl['hw.memsize'] = 32212254720
    input_sysctl['kern.osversion'] = '17.3.0'

# Generated at 2022-06-13 00:42:34.286267
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    dHCollector = DarwinHardwareCollector()
    assert(dHCollector._platform == 'Darwin')

# Generated at 2022-06-13 00:42:44.618089
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    """
    Unit test for method get_cpu_facts of class DarwinHardware

    :return:
    """
    sysctl_values = {
        'hw.logicalcpu': '2',
        'hw.physicalcpu': '1',
        'hw.ncpu': '2',
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-3230M CPU @ 2.60GHz',
        'machdep.cpu.core_count': '2'
    }
    sysctl_values_ppc = {
        'hw.logicalcpu': '2',
        'hw.physicalcpu': '1',
        'hw.ncpu': '2',
        'hw.memsize': '4294967296',
    }
    # Simulate the get_system_profile function

# Generated at 2022-06-13 00:42:53.675370
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_module = FakeModule()
    h = DarwinHardware(module=test_module)

    # simulate the command output
    test_module.run_command = lambda *args, **kwargs: (0, """
    0
    1
    2
    hello
    3: hola
    4: bye
    5
    """, '')

    system_profile = h.get_system_profile()

    # check that it produces a dict
    assert isinstance(system_profile, dict) == True

    # check that the first line (0) and the last line (5) are excluded
    assert '0' not in system_profile
    assert '5' not in system_profile

    # check that multiple spaces are reduced to one
    assert system_profile['3'] == 'hola'
    assert system_profile['4'] == 'bye'

# Generated at 2022-06-13 00:42:57.683188
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    darwin_hardware = DarwinHardware()

    # Regression test for issue #25182
    darwin_hardware.sysctl = {'hw.memsize': '4294967296'}

    memory_facts = darwin_hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4096
    assert memory_facts['memfree_mb'] == 0

# Generated at 2022-06-13 00:43:04.673585
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    """
    Test that method get_system_profile of class DarwinHardware
    returns a non-empty dict
    """

    # Create a dummy AnsibleModule object
    from ansible.module_utils.facts import Facts
    import ansible.module_utils.facts.hardware.darwin as darwin_facts

    module = Facts(
        fakeargs = dict(
            gather_subset = ['all'],
        ),
        # True because we want the module to exit after execution
        exit_json = True,
        # True because we do not want to invoke the module
        check_mode = True,
    )

    # Create a DarwinHardware object
    dh = darwin_facts.DarwinHardware(module)
    assert dh.get_system_profile()

# Generated at 2022-06-13 00:43:11.930343
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = AnsibleModule(argument_spec=dict())


# Generated at 2022-06-13 00:43:23.103001
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Initial: no collected facts
    collected_facts = dict()

    # Initialize collector
    darwin_hardware = DarwinHardware(collected_facts)

    # Avoid calling sysctl_get, since it has dependencies that require system
    darwin_hardware.sysctl_get = lambda x: {}
    darwin_hardware.sysctl_all = lambda x: {}

    # Fake output from /usr/sbin/system_profiler SPHardwareDataType
    darwin_hardware.get_system_profile = lambda: {'Processor Name': 'Foo', 'Processor Speed': 'Bar'}

    # Fake output from vm_stat
    darwin_hardware.module.run_command = lambda x: (0, 'Foo', '')

    hardware_facts_1 = darwin_hardware.pop