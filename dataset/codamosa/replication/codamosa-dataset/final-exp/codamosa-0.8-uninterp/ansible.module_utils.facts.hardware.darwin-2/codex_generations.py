

# Generated at 2022-06-13 00:34:59.175982
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    hardware = DarwinHardware()
    hardware.module = MockModule()
    hardware.module.run_command.return_value = 0, SP_HARDWARE_DATA_TYPE, None
    result = hardware.get_system_profile()
    assert result['Model Identifier'] == 'MacBookPro11,4'
    assert result['Processor Name'] == 'Intel Core i7'
    assert result['Processor Speed'] == '2.8 GHz'
    assert result['Number of Processors'] == 1
    assert result['Total Number of Cores'] == 4
    assert result['L2 Cache'] == '256 KB'
    assert result['L3 Cache'] == '6 MB'
    assert result['Memory'] == '16 GB'
    assert result['Boot ROM Version'] == 'MBP114.0172.B00'

# Generated at 2022-06-13 00:35:08.788595
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():

    my_vars = dict(
        ansible_processor_cores=4,
        ansible_processor_vcpus=4,
        ansible_processor="Intel(R) Core(TM) i7-3610QM CPU @ 2.30GHz"
    )

    class ModuleMock(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, *_args, **_kwargs):
            return 0, "", ""

    module = ModuleMock()
    module.params = my_vars

    dh = DarwinHardware(module)

    cpu_count = dh.get_cpu_facts()
    assert cpu_count['processor'] == my_vars['ansible_processor']

# Generated at 2022-06-13 00:35:18.959094
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    '''
    Unit test method populate of class DarwinHardware
    '''
    class ModuleStub:
        run_command_counter = 0

        def run_command(self, command, encoding=None):
            '''
            Stub for method run_command of module AnsibleModule
            '''
            self.run_command_counter += 1

            if self.run_command_counter == 1:
                return (0, 'hw.model: Macmini8,1', '')
            elif self.run_command_counter == 2:
                return (0, 'hw.model: Macmini8,1', '')
            elif self.run_command_counter == 3:
                return (0, 'hw.logicalcpu: 8', '')

# Generated at 2022-06-13 00:35:29.211667
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    test_module = AnsibleModule(argument_spec={})

    up_days = 3
    up_hours = 17
    up_mins = 33
    up_secs = 12
    up_time_secs = (up_days * 24 * 3600 + up_hours * 3600 +
                    up_mins * 60 + up_secs)

    # Create a fake sysctl binary.
    mock_sysctl_path = MockSystemPath('sysctl')
    mock_sysctl_binary = MockSystemBinary(mock_sysctl_path)
    mock_sysctl_binary.set_returncode(0)
    mock_sysctl_binary.set_stdout(struct.pack('@L', up_time_secs))

    # Create a test module object.
    test_module.run_command = mock_sysctl_binary

# Generated at 2022-06-13 00:35:39.328022
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = type('_module', (object, ), {})()
    module.run_command = lambda params: (0, 'fake output', '')
    module.get_bin_path = lambda a: ''

    hardware_facts = DarwinHardware(module)

    facts = hardware_facts.populate()

    assert (facts['processor'] != ''), "Processor fact is empty"
    assert (facts['processor_cores'] >= 1), "Processor cores fact is less than 1"
    assert (facts['memtotal_mb'] >= 1), "Memory total fact is less than 1 MB"
    assert (facts['memfree_mb'] >= 1), "Memory free fact is less than 1 MB"
    assert (facts['model'] != ''), "Model fact is empty"
    assert (facts['osversion'] != ''), "OS Version fact is empty"
   

# Generated at 2022-06-13 00:35:48.692140
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    import pytest
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    sysctl_hw_model = dict()
    sysctl_hw_model['hw.model'] = 'Macmini4,1'
    sysctl_kern_osversion = dict()
    sysctl_kern_osversion['kern.osversion'] = '15.6.0'
    sysctl_kern_osrevision = dict()
    sysctl_kern_osrevision['kern.osrevision'] = '0'
    sysctl_facts = dict()
    sysctl_facts.update(sysctl_hw_model)
    sysctl_facts.update(sysctl_kern_osversion)
    sysctl_facts.update(sysctl_kern_osrevision)

# Generated at 2022-06-13 00:35:59.682743
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    platform = 'Darwin'
    class FakeHardware(object):
        # Fake supported_platform
        @property
        def supported_platform(self):
            platform = 'Darwin'
            return platform

        # Fake sysctl
        sysctl = {
            'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz',
            'machdep.cpu.core_count': '4',
            'hw.physicalcpu': '4',
            'hw.logicalcpu': '4',
        }
    hardware_obj = FakeHardware()
    darwin_hardware_obj = DarwinHardware(module=FakeHardware())
    cpu_facts = darwin_hardware_obj.get_cpu_facts(hardware_obj)
    assert cpu_facts['processor']

# Generated at 2022-06-13 00:36:04.730279
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = FakeAnsibleModule()
    hardware = DarwinHardware(module)
    hardware.sysctl = {
        'hw.memsize': '1073741824',
    }
    memory_facts = hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 1024
    assert memory_facts['memfree_mb'] == 0



# Generated at 2022-06-13 00:36:09.189705
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """This function is used to test the constructor of class DarwinHardwareCollector."""
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector.platform == 'Darwin'
    assert darwin_hardware_collector.fact_class == DarwinHardware

# Generated at 2022-06-13 00:36:18.424295
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Mock the module
    module = Mock()

    # Mock the output of sysctl kern.boottime
    kern_boottime = Mock(bytes_result=struct.pack('@L', 1503222210))

    # Mock the manager's run_command
    module.run_command.return_value = (0, kern_boottime, None)

    # Instanciate the class to test
    dhw = DarwinHardware()
    dhw.module = module

    # Run the method to test
    result = dhw.get_uptime_facts()

    # Check the results
    assert result == {'uptime_seconds': int(time.time() - 1503222210)}

# Generated at 2022-06-13 00:36:43.504166
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = MockModule()
    hardware = DarwinHardware(module)
    sysctl_mock = {'machdep.cpu.brand_string': 'Intel(R) Xeon(R) CPU E5-2699 v4 @ 2.20GHz',
                   'hw.physicalcpu': 16,
                   'hw.logicalcpu': 32}
    hardware.sysctl = sysctl_mock
    expected_result = {'processor': 'Intel(R) Xeon(R) CPU E5-2699 v4 @ 2.20GHz', 'processor_cores': 16, 'processor_vcpus': 32}
    assert hardware.get_cpu_facts() == expected_result


# Generated at 2022-06-13 00:36:49.368951
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    darwin_hardware = DarwinHardware()
    profile = darwin_hardware.get_system_profile()
    assert profile['Model Identifier'] == 'MacBookPro11,3'
    assert profile['Processor Name'] == 'Intel Core i7'
    assert profile['Processor Speed'] == '2.2 GHz'

# Generated at 2022-06-13 00:36:59.152516
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    test_module = FakeModule(params={})
    test_module.run_command = FakeCommand
    fact_class = DarwinHardware('Darwin', test_module)
    # Test with Intel
    fact_class.sysctl = {'machdep.cpu.brand_string': 'Intel', 'machdep.cpu.core_count': 8}
    cpu_facts = fact_class.get_cpu_facts()
    assert cpu_facts['processor_cores'] == 8
    assert cpu_facts['processor'] == 'Intel'
    # Test with PowerPC
    fact_class.sysctl = {'hwp.physicalcpu': 8}
    fact_class.get_system_profile = lambda: {'Processor Name': 'PowerPC', 'Processor Speed': '1.6 GHz'}
    cpu_facts = fact_class.get_

# Generated at 2022-06-13 00:37:02.177646
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    module = AnsibleModuleMock()
    hardware_collector = DarwinHardwareCollector(module)
    assert hardware_collector._platform == 'Darwin'


# Generated at 2022-06-13 00:37:10.239201
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    module.run_command = MagicMock(return_value=(0, 'hw.model: MacBookAir5,2\n', ''))
    hardware_facts = DarwinHardware(module, dict())
    facts = hardware_facts.get_mac_facts()
    assert(facts['model'] == 'MacBookAir5,2')
    assert(facts['osversion'] == '16.7.0')
    assert(facts['osrevision'] == '1')


# Generated at 2022-06-13 00:37:19.785088
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.sysctl import Sysctl
    from ansible.module_utils.facts import FactManager
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import string_types

    hardware = Hardware()
    facts = hardware.populate()

    assert 'uptime_seconds' in facts
    assert 'processor_description' in facts
    assert 'processor_sockets' in facts
    assert 'processor_count' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts

    # Test the uptime fact
    assert isinstance(facts['uptime_seconds'], int)
    assert facts['uptime_seconds'] > 0

    # Test the processor count

# Generated at 2022-06-13 00:37:28.908668
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import unittest.mock
    import struct
    mock = unittest.mock
    mock_module = mock.MagicMock()
    mock_module.get_bin_path.return_value = '/usr/sbin/sysctl'
    mock_module.run_command.return_value = 0, struct.pack('@L', int(time.time() - (60*60*24))), None
    darwin_hw = DarwinHardware()
    darwin_hw.module = mock_module
    facts = darwin_hw.get_uptime_facts()

    assert(facts['uptime_seconds'] == 60*60*24)

# Generated at 2022-06-13 00:37:40.079826
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    """Test the get_cpu_facts of DarwinHardware
    """
    # Test a case that sysctl hw.model cannot be determined
    class FakeModule:
        def run_command(self, args):
            return 1, "", "Command execution failed"

    class FakeDarwinHardware:
        def __init__(self):
            self.module = FakeModule()

        def get_system_profile(self):
            return {'Processor Name': 'Intel', 'Processor Speed': '3.3 GHz'}

        def sysctl(self, _):
            return {'hw.physicalcpu': '4', 'hw.logicalcpu': '2'}

    d = FakeDarwinHardware()
    cpu_facts = d.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel @ 3.3 GHz'

# Generated at 2022-06-13 00:37:47.099812
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.sysctl = dict(machdep={'cpu':
                                  dict(
                                      brand_string=u'Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz',
                                      core_count=4,
                                  )
                                  },
                         hw={'physicalcpu': 4,
                             'logicalcpu': 8})

    engine = DarwinHardware(module=module)
    assert engine.get_cpu_facts() == dict(
        processor=u'Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz',
        processor_cores=u'4',
        processor_vcpus=u'8')



# Generated at 2022-06-13 00:37:57.235219
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class ModuleStub:
        name = 'memory_facts'
        version = '1.2.3'

        # Mocked methods
        def run_command(self, cmd, **kwargs):
            out = 'fake_out'
            return (0, out, '')

        def get_bin_path(self, bin_name):
            return '/usr/bin/vm_stat'

    def mocked_get_sysctl(self, keys):
        return {'hw.memsize': '123456789'}

    module = ModuleStub()
    module.get_sysctl = mocked_get_sysctl

    mem_facts = DarwinHardware(module)
    result = mem_facts.populate()
    assert result['memtotal_mb'] == 1163
    assert result['memfree_mb'] == 0


# Unit

# Generated at 2022-06-13 00:38:19.966996
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    collector = DarwinHardwareCollector()
    assert isinstance(collector, DarwinHardwareCollector)
    assert isinstance(collector.platform, str)
    assert collector.platform == 'Darwin'
    assert collector._fact_class == DarwinHardware

# Generated at 2022-06-13 00:38:23.740511
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = MockModule()
    facts = DarwinHardware(module).populate()
    assert facts['uptime_seconds'] >= 0

# Unit test class MockModule

# Generated at 2022-06-13 00:38:35.521083
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = Mock()
    module.run_command = mock_get_bin_path('vm_stat')

# Generated at 2022-06-13 00:38:43.413180
# Unit test for method get_memory_facts of class DarwinHardware

# Generated at 2022-06-13 00:38:44.889261
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # See https://github.com/ansible/ansible/issues/50347
    DarwinHardwareCollector()

# Generated at 2022-06-13 00:38:56.995035
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    fact_functions = dict(
        get_system_profile=lambda: dict(),
        get_mac_facts=lambda: dict(),
        get_cpu_facts=lambda: dict(),
        get_uptime_facts=lambda: dict(),
    )
    hardware = DarwinHardware(dict(), fact_functions)
    total_used = 0
    page_size = 4096

# Generated at 2022-06-13 00:39:01.451889
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_obj = DarwinHardware(module)
    facts = hardware_obj.populate()

    assert isinstance(facts, dict)
    assert 'model' in facts.keys()
    assert 'osrevision' in facts.keys()
    assert 'processor_cores' in facts.keys()
    assert 'memory_mb' in facts.keys()



# Generated at 2022-06-13 00:39:14.170303
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    """
    Method get_system_profile of class DarwinHardware should return a
    dictionary with the information of the system.
    """
    m = MagicMock()

# Generated at 2022-06-13 00:39:22.980466
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    """Test DarwinHardware.populate()."""
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.sysctl import get_sysctl

    # The following class is used only for mocking
    class FakeModule(object):
        def run_command(self, cmd, encoding=None):
            # Return command output as a string
            command = " ".join(cmd)

# Generated at 2022-06-13 00:39:33.888628
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import time

    class FakeModule:
        def __init__(self, output):
            self.output = output

        def run_command(self, cmd, encoding=None):
            cmd_len = len(cmd)
            if cmd_len == 3 and cmd[0] == '/sbin/sysctl' and cmd[1] == '-b':
                return 0, self.output, ''
            return None, None, None

        def get_bin_path(self, cmd, required=False):
            return cmd

    def test_get_uptime_facts(self, output_value, expected_value):
        (osversion, osrevision) = output_value.split()

# Generated at 2022-06-13 00:40:03.844418
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = MagicMock()

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    hardware_facts = DarwinHardware(module)

    kwargs = dict(
        facts=dict(),
        module=module,
        collected_facts=None,
        hardware_facts=dict(),
    )

    from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.darwin import get_memory_facts
    hardware_facts['get_memory_facts'] = get_memory_facts
    # Test with None sysctl_output
    args = [module]
    kwargs['module'].run_command.return_value = (0, None, None)
    kwargs['facts'] = hardware_facts['get_memory_facts'](*args, **kwargs)

# Generated at 2022-06-13 00:40:07.905698
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware = DarwinHardware(dict())
    facts = hardware.populate()
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'model' in facts
    assert 'osversion' in facts
    assert 'osrevision' in facts
    assert 'uptime_seconds' in facts

# Generated at 2022-06-13 00:40:16.816461
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Intel
    test_values = dict()
    test_values['machdep.cpu.core_count'] = 4
    test_values['machdep.cpu.brand_string'] = 'Intel Core i7-7700HQ'
    hardware = DarwinHardware({}, sysctl=test_values)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel Core i7-7700HQ'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_vcpus'] == 0

    # PowerPC
    test_values = dict()
    test_values['hw.physicalcpu'] = 4
    test_values['hw.logicalcpu'] = 2
    test_values['hw.ncpu'] = 1

# Generated at 2022-06-13 00:40:27.612708
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import DarwinSystemPlatformCollector

    module = FakeAnsibleModule()
    facts_collector = ModuleFactCollector(module)
    hardware = DarwinHardware(module)

    hardware._facts['uname'] = {'kernel': 'Darwin'}
    hardware._facts['distribution'] = {}
    hardware._facts['distribution']['system'] = FakeDistribution()
    hardware._facts['system'] = {'platform': 'Darwin'}


# Generated at 2022-06-13 00:40:30.010812
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = MockModule()
    sysctl = {'hw.model': 'iMac11,1'}
    hardware = DarwinHardware(module=module, sysctl=sysctl)
    mac_facts = hardware.get_mac_facts()
    assert mac_facts.get('model') == 'iMac11,1'


# Generated at 2022-06-13 00:40:36.447204
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = FakeModule({
        'hw.memsize': "8589934592",
        'kern.boottime': "1521647274",
    })

    hardware = DarwinHardware(module)

    memory_facts = hardware.get_memory_facts()
    assert(memory_facts['memtotal_mb'] == 8192)
    assert(memory_facts['memfree_mb'] == 8191)



# Generated at 2022-06-13 00:40:46.720798
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    """Validate the DarwinHardware.get_uptime_facts() method.
    """
    test_cases = [
        (None, 0),
        ("", 0),
        ("-1\n", 0),
        ("1514362339\n", 1514362339),
        ("1514362339.99\n", 1514362339),
    ]

    for test_case in test_cases:
        # Test the method
        darwin_hardware = DarwinHardware()
        darwin_hardware.run_command = lambda cmd: (0, test_case[0], None)
        result = darwin_hardware.get_uptime_facts()

        assert result['uptime_seconds'] == test_case[1]

# Generated at 2022-06-13 00:40:55.854606
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from io import BytesIO
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    # Adapted from kern.boottime output on an actual macOS system.
    kern_boottime = (
        b'{ sec = 1479356529, usec = 965107 } Thu Nov 17 22:28:49 2016'
    )
    output = BytesIO(kern_boottime)
    darwin_hardware = DarwinHardware({}, {}, BytesIO(), BytesIO(), output)
    uptime_facts = darwin_hardware.get_uptime_facts()
    assert 'uptime_seconds' in uptime_facts
    uptime_seconds = uptime_facts['uptime_seconds']
    assert isinstance(uptime_seconds, int)
    # The run_command method

# Generated at 2022-06-13 00:41:02.935976
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    class MockModule(object):
        def __init__(self):
            self.run_command_values = [
                (0, 'hw.model: PowerMac11,2', ''),
                (0, 'Model Name: Intel(R) Core(TM)2 Duo CPU     T7300  @ 2.00GHz', ''),
                (0, 'hw.memsize: 4294967296', ''),
                (0, 'kern.boottime: { sec = 1434253388, usec = 0 } Thu Jun 11 18:03:08 2015', ''),
            ]
            self.run_command_calls = []
            self.get_bin_path_values = [None, '/bin/vm_stat']
            self.get_bin_path_calls = []
            self.params = dict()


# Generated at 2022-06-13 00:41:10.427324
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    import sys
    import pytest
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware


    if sys.version_info[0] == 2:
        input_string = '3\nIntel'
    else:
        input_string = '3\nIntel\n'

    cpu_facts = {}
    dh = DarwinHardware({})
    dh.sysctl = {'machdep.cpu.brand_string': 'Intel', 'machdep.cpu.core_count': '6'}
    cpu_facts = dh.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel'
    assert cpu_facts['processor_vcpus'] is None
    dh.sysctl = {}
    cpu_facts = dh.get_cpu_facts()

# Generated at 2022-06-13 00:41:42.973462
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class MockModule(object):
        def __init__(self):
            self.run_command_return_value = 0
            self.run_command_return_string = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
        def get_bin_path(self, path):
            return path
        def run_command(self, cmd, encoding=None):
            return (self.run_command_return_value, self.run_command_return_string, "")
    module = MockModule()
    darwin = DarwinHardware()
    darwin.module = module
    uptime_facts = darwin.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 184467440737095516

# Generated at 2022-06-13 00:41:46.208895
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_collector = DarwinHardwareCollector()
    assert darwin_collector._platform == 'Darwin'
    assert darwin_collector._fact_class == DarwinHardware


# Generated at 2022-06-13 00:41:52.858614
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    """
    Check right facts are collected on Darwin
    """
    facts = DarwinHardware().populate()
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_vcpus' in facts
    assert not facts['processor'].startswith('unknown')
    assert facts['processor_cores'] > 0
    assert facts['processor_vcpus'] == '' or facts['processor_vcpus'] >= facts['processor_cores']

# Generated at 2022-06-13 00:42:01.311596
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import datetime
    now = datetime.datetime.now()
    boot_time = float(now.strftime("%s"))
    boot_time_bytes = struct.pack('@L', int(boot_time))

    module = AnsibleModule(
        argument_spec=dict()
    )
    darwin_hardware = DarwinHardware(module)

    def sysctl_side_effect(*args, **kwargs):
        if args[0][2] == 'kern.boottime':
            return 0, boot_time_bytes, None
        return 0, None, None

    darwin_hardware.module.run_command.side_effect = sysctl_side_effect
    uptime_facts = darwin_hardware.get_uptime_facts()


# Generated at 2022-06-13 00:42:09.110015
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    """Test the method get_cpu_facts of class DarwinHardware."""
    module = AnsibleModuleMock()
    system = DarwinHardware(module)
    system.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Xeon(R) CPU E5-2630L v2 @ 2.40GHz',
        'machdep.cpu.core_count': 2,
        'hw.physicalcpu': 4,
        'hw.logicalcpu': 8
    }

    result = system.get_cpu_facts()

    assert result['processor'] == "Intel(R) Xeon(R) CPU E5-2630L v2 @ 2.40GHz"
    assert result['processor_cores'] == 2
    assert result['processor_vcpus'] == 8



# Generated at 2022-06-13 00:42:11.976756
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    mac_facts = DarwinHardwareCollector()
    assert mac_facts.get_mac_facts()['osversion'] is not None


# Generated at 2022-06-13 00:42:21.400161
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import sys
    if sys.version_info[:2] < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    from mock import MagicMock, patch
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    # Mocked system_profiler output

# Generated at 2022-06-13 00:42:26.774460
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = FakeModule()
    harware = DarwinHardware(module)
    harware.sysctl = {
        'hw.memsize': '134217728'
    }
    harware.module.run_command = lambda a: (0, 'Pages free: 105.  \nPages wired down: 17.  \nPages active: 18.  \n', '')
    assert harware.get_memory_facts() == {
        'memtotal_mb': 128,
        'memfree_mb': 105
    }



# Generated at 2022-06-13 00:42:32.218341
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Perform some setup work for the unit test
    # All of this should be removed when running against target
    import sys
    import ansible.module_utils.facts.hardware.darwin
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import unittest
    import tempfile
    import os
    import shutil
    import json

    class TestDarwinHardware(unittest.TestCase):
        def setUp(self):
            self.module_path = os.path.dirname(ansible.module_utils.facts.hardware.darwin.__file__)
            self.factory = self._get_module_factory()
            self.tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 00:42:39.970256
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils._text import to_bytes
    module = AnsibleModule(argument_spec=dict())
    with patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware.run_command') as run_command:
        run_command.return_value = (0, to_bytes(dedent('''\
            Hardware Overview:

              Model Name: MacBook Pro
              Model Identifier: MacBookPro14,1
              Processor Name: Intel Core i7
              Processor Speed: 2,8 GHz
              Number of Processors: 1
              Total Number of Cores: 4
              L2 Cache (per Core): 256 KB
              L3 Cache: 8 MB
              Memory: 16 GB
            ''')), to_bytes(''))
        obj = DarwinHardware

# Generated at 2022-06-13 00:43:44.547048
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    test = DarwinHardware({})
    test_method = test._get_system_profile()
    assert isinstance(test_method, dict)
    assert test_method.get('Processor Name') == 'Intel Core i7'

# Generated at 2022-06-13 00:43:45.075887
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hwc = DarwinHardwareCollector()

# Generated at 2022-06-13 00:43:52.509288
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = get_module()

    # Create instance of DarwinHardware
    fact_gathering = DarwinHardware(module)

    # Set required system information
    fact_gathering.sysctl = {
        'kern.osversion': '15D21',
        'kern.osrevision': '',
    }

    # Set required system commands
    module.run_command = MagicMock()
    module.run_command.return_value = (0, 'hw.model: PowerMac7,3', '')

    # Get facts
    facts = fact_gathering.get_mac_facts()

    # Check facts
    assert 'model' in facts
    assert facts['model'] == 'PowerMac7,3'
    assert 'product_name' in facts
    assert facts['product_name'] == 'PowerMac7,3'

# Generated at 2022-06-13 00:44:00.050201
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    class TestModule:
        def run_command(self, args):
            return (0, '', '')
    hardware_instance = DarwinHardware(TestModule())
    hardware_instance.sysctl = {'machdep.cpu.brand_string': 'Intel',
                                'machdep.cpu.core_count': 2,
                                'hw.memsize': 8000000000,
                                'hw.ncpu': 2,
                                'kern.osversion': '10.12.6',
                                'kern.osrevision': '16G1212'}
    hardware_instance.sysctl.update(get_sysctl(TestModule(), ['hw', 'machdep', 'kern']))
    hardware_instance.populate()


# Generated at 2022-06-13 00:44:02.297978
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hw = DarwinHardwareCollector()
    assert isinstance(hw, HardwareCollector)
    assert getattr(hw, "_fact_class", None) == DarwinHardware
    assert getattr(hw, "_platform", None) == "Darwin"



# Generated at 2022-06-13 00:44:12.042562
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    """Test the get_system_profile method of class DarwinHardware"""

# Generated at 2022-06-13 00:44:13.526067
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware_collector_facts = DarwinHardwareCollector()
    assert hardware_collector_facts._fact_class == DarwinHardware
    assert hardware_collector_facts._platform == 'Darwin'

# Generated at 2022-06-13 00:44:18.303302
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    module_mock = Mock()
    module_mock.run_command.return_value = (0, '\x86\xED\xD4\x00\x00\x00\x00\x00')
    module_mock.get_bin_path.return_value = '/usr/sbin/sysctl'

    darwin_hardware = DarwinHardware(module_mock)
    uptime_facts = darwin_hardware.get_uptime_facts()

    assert uptime_facts == {'uptime_seconds': 38014929}

# Generated at 2022-06-13 00:44:27.128547
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    testobj = DarwinHardware()

    testobj.module.run_command = Mock(return_value=(
        0, 'hw.model: MacPro6,1\n', ''))
    testobj.sysctl = {
        'kern.osversion': '16.7.0',
        'kern.osrevision': '201602141527',
    }
    result = testobj.get_mac_facts()
    assert result['model'] == 'MacPro6,1'
    assert result['osversion'] == '16.7.0'
    assert result['osrevision'] == '201602141527'


# Generated at 2022-06-13 00:44:29.001406
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """ Test constructor of class DarwinHardwareCollector"""
    facts = DarwinHardwareCollector()
    assert type(facts) == DarwinHardwareCollector
    assert facts._platform == 'Darwin'
    assert facts._fact_class == DarwinHardware