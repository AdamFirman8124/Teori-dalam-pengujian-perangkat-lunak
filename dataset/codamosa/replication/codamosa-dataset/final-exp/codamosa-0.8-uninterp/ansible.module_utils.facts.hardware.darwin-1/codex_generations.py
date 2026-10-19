

# Generated at 2022-06-13 00:34:54.119243
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    dh = DarwinHardware()
    assert dh.get_system_profile() == dict()

# Generated at 2022-06-13 00:34:58.263000
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, 'machdep.cpu.brand_string: Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz', '')
    hw = DarwinHardware(module_mock)
    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz'

# Generated at 2022-06-13 00:35:08.088195
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    hardware = DarwinHardware({})
    expected_result = {'System Version': 'OS X 10.12.6 (16G29)', 'Hardware Overview': 'Model Name: MacBook Air Model Identifier: MacBookAir5,2 Processor Name: Intel Core i5 Processor Speed: 1,8 GHz Number of Processors: 1 Total Number of Cores: 2 L2 Cache (per Core): 256 KB L3 Cache: 3 MB Memory: 8 GB Boot ROM Version: MBA51.00EF.B03 SMC Version (system): 2.7f0 Serial Number (system): C02MFFY8FV4V Hardware UUID: 5D9F9F1C-3A3F-5E2D-8D66-8F62B0EAD5F5'}
    assert expected_result == hardware.get_system_profile()



# Generated at 2022-06-13 00:35:12.340153
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Our test mock environment.
    class ModuleTest(object):
        @staticmethod
        def get_bin_path(command):
            return command

        @staticmethod
        def run_command(cmd, encoding=None):
            rc = 0
            out = struct.pack('@L', 1386976503)  # Oct 13, 2013 08:01:43 (UTC)
            err = ''
            return rc, out, err

    # Test the DarwinHardware.get_uptime_facts() method.
    dh = DarwinHardware()
    dh.module = ModuleTest
    uptime_facts = dh.get_uptime_facts()
    assert(uptime_facts['uptime_seconds'] == 22379)  # Oct 17, 2013 07:03:59 (UTC)

# Generated at 2022-06-13 00:35:14.837785
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """This creates a darwin hardware collector and checks if it is an instance of HardwareCollector
    and if it has a 'platform' attribute.
    """
    darwin_collector = DarwinHardwareCollector()
    assert isinstance(darwin_collector, HardwareCollector)
    assert hasattr(darwin_collector, 'platform')

# Generated at 2022-06-13 00:35:21.728759
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    """
    This test case asserts that the get_system_profile method of the class DarwinHardware
    will return a dictionary of the form:
    """
    system_profile = DarwinHardware.get_system_profile(None)
    assert isinstance(system_profile, dict)
    expected_keys = ['Model Name', 'Model Identifier', 'Processor Name', 'Processor Speed',
                     'Number of Processors', 'Memory', 'Serial Number (system)']
    for key in expected_keys:
        assert key in system_profile, "Did not find %s in system_profile" % key


# Generated at 2022-06-13 00:35:23.739109
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    facts = DarwinHardware().get_uptime_facts()
    assert 'uptime_seconds' in facts

# Generated at 2022-06-13 00:35:32.471563
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Testcase 1:
    # On Darwin, the default format is annoying to parse.
    # Use -b to get the raw value and decode it.
    # sysctl -b kern.boottime
    # When the above command is executed on a Darwin-based host,
    # the output returned is a string, which is the time
    # when the Darwin-based host booted in seconds.

    # Assigning the command to be executed as a variable.
    vm_stat_command = 'vm_stat'
    # Assigning the string to be returned from the command execution.
    # This value corresponds to the case when the Darwin-based host
    # has booted for 7 seconds.

# Generated at 2022-06-13 00:35:41.023303
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    hardware = DarwinHardware(None)
    hardware.module.run_command = lambda x: (0, to_bytes('0\n1\nhw.model: Model\n'), to_bytes(''))
    hardware.sysctl = {'kern.osversion': 'osversion', 'kern.osrevision': 'osrevision'}
    assert hardware.get_mac_facts() == {'model': 'Model', 'osversion': 'osversion', 'osrevision': 'osrevision'}



# Generated at 2022-06-13 00:35:53.122852
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import ansible.module_utils.facts.hardware.darwin as darwin

    # Expected raw output
    #
    # macOS 10.13
    out_10_13 = b'\x01\xd9\xbd\x0c\x00\x00\x00\x00'

    # macOS 10.14
    out_10_14 = b'\x01\xdb\xd2\x45\x00\x00\x00\x00'

    # macOS 10.15
    out_10_15 = b'\x01\xdd\x18\x48\x00\x00\x00\x00'

    # macOS 10.12 and below
    out_10_12 = b'\xff\xff\xff\xff\x00\x00\x00\x00'

   

# Generated at 2022-06-13 00:36:08.256236
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    mc = DarwinHardware()
    mc.sysctl = {'machdep.cpu.brand_string': 'Intel', 'machdep.cpu.core_count': 2}
    rc = mc.get_cpu_facts()
    assert rc['processor'] == 'Intel'
    assert rc['processor_cores'] == 2


# Generated at 2022-06-13 00:36:18.927713
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import time

    class FakeModule(object):
        def __init__(self, boottime=None):
            self.boottime = boottime

        def get_bin_path(self, *args):
            return '/sbin/sysctl'

        def run_command(self, cmd, encoding=None):
            if self.boottime is None:
                return (0, '', '')

            data = struct.pack('@L', self.boottime)
            return (0, data, '')

    hardware = DarwinHardware(FakeModule())
    uptime_facts = hardware.get_uptime_facts()
    assert len(uptime_facts) == 1

# Generated at 2022-06-13 00:36:28.670599
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    module = FakeAnsibleModule()
    hardware = DarwinHardware(module)
    hardware.sysctl = dict()
    intel_cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in intel_cpu_facts
    assert 'processor_cores' in intel_cpu_facts
    assert 'processor_vcpus' in intel_cpu_facts
    assert intel_cpu_facts['processor_cores'] > 0

    hardware.sysctl = dict()
    hardware.sysctl['hw.physicalcpu'] = '3'
    hardware.sysctl['hw.ncpu'] = '4'
    powerpc_cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in powerpc_cpu_facts

# Generated at 2022-06-13 00:36:30.011796
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware = DarwinHardwareCollector(None)
    assert hardware.platform == 'Darwin'

# Generated at 2022-06-13 00:36:38.582323
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import sys
    import os

# Generated at 2022-06-13 00:36:42.258638
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # create the instance
    hc = DarwinHardwareCollector()

    # check name and platform
    assert hc.name == 'hardware.darwin'
    assert hc.platform == 'Darwin'


# Generated at 2022-06-13 00:36:51.826987
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = type('DummyModule', (object,), dict(run_command=lambda *args, **kwargs: (0, '', '')))
    hardware_instance = DarwinHardware(module)
    hardware_instance.sysctl = dict(
        machdep=dict(cpu_brand_string="TestCPU", cpu_core_count=2)
    )

    cpu_facts = hardware_instance.get_cpu_facts()
    assert cpu_facts['processor'] == "TestCPU"
    assert cpu_facts['processor_cores'] == "2"
    assert cpu_facts['processor_vcpus'] == ""

# Generated at 2022-06-13 00:36:53.206907
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert isinstance(DarwinHardwareCollector(), HardwareCollector)

# Generated at 2022-06-13 00:37:04.102101
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    mem_facts = {}
    call_command = ['/usr/bin/vm_stat']
    status_code = 0

# Generated at 2022-06-13 00:37:13.718353
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    ######################################################################
    # Initialize test environment
    ######################################################################
    # Initializing test class
    hardware = DarwinHardware(module)

    # Retrieving sysctl's mocks
    sysctl_values = {}
    sysctl_values['hw.memsize'] = '4294967296'
    sysctl_values['hw.model'] = 'iMac13,2'
    sysctl_values['hw.ncpu'] = '8'
    sysctl_values['hw.physicalcpu'] = '4'
    sysctl_values['hw.busfrequency_max'] = '120000000'
    sysctl_values['hw.busfrequency_min'] = '10000000'

# Generated at 2022-06-13 00:37:31.431620
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    '''Unit test of the populate method of class DarwinHardware'''
    # Note: the data below are based on a Darwin 16.7.0
    #       This test is fragile because the command output may
    #       change in next releases of Darwin

# Generated at 2022-06-13 00:37:42.218887
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = FakeModule()
    hardware = DarwinHardware(module)

    module.run_command.return_value = 0, '', ''
    module.run_command.return_value[1] = '''
    Hardware:

      Hardware Overview:

        Model Name: MacBook Pro
        Processor Name: Intel Core i7
        Processor Speed: 2.2 GHz
        Number of Processors: 1
        Total Number of Cores: 2
        L2 Cache (per Core): 256 KB
        L3 Cache: 4 MB
        Memory: 16 GB
        Boot ROM Version: MBP55.00AC.B03
        SMC Version (system): 2.4f0
        Serial Number (system): W8xxxxxx0GZ
        Hardware UUID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    '''

    assert hardware.get_system_profile

# Generated at 2022-06-13 00:37:52.053060
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module)
    facts = hardware.populate()

    assert 'processor' in facts
    assert isinstance(facts['processor'], str)
    assert 'processor_cores' in facts
    assert isinstance(facts['processor_cores'], int)
    assert 'memtotal_mb' in facts
    assert isinstance(facts['memtotal_mb'], int)
    assert 'memfree_mb' in facts
    assert isinstance(facts['memfree_mb'], int)
    assert 'model' in facts
    assert isinstance(facts['model'], str)
    assert 'osversion' in facts
    assert isinstance(facts['osversion'], str)
    assert 'osrevision' in facts

# Generated at 2022-06-13 00:37:57.772225
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():

    sysctl_data = {
        'hw.physicalcpu': 2,
        'hw.logicalcpu': 4,
        'hw.cpufrequency': 2500000000,
        'machdep.cpu.core_count': 2,
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz'
    }

    # Create the module mock
    module_mock = AnsibleMock()

    # Create the class
    darwin_hardware = DarwinHardware(module_mock)

    # Run the method
    darwin_hardware.get_cpu_facts()

    # Check the result
    assert darwin_hardware.facts['processor'] == 'Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz'

# Generated at 2022-06-13 00:38:08.437440
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    # Commands
    result = {
        'stdout': 'hw.model: MacBookPro8,2\n',
        'stdout_lines': ['hw.model: MacBookPro8,2']
    }
    run_command_result = result

    # Facts
    sysctl = {
        'kern.osversion': '15.6.0',
        'kern.osrevision': '17G65'
    }

    # Module
    module = type('', (), {
        'run_command': lambda self, cmd: run_command_result,
        'fail_json': lambda self, msg: False,
    })()

    # Hardware
    hardware = DarwinHardware()
    hardware.module = module
    hardware.sysctl = sysctl
    # Test
    hardware_facts = hardware.get_mac_facts()

# Generated at 2022-06-13 00:38:16.746008
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    # Test with an empty output
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    hardware_class = DarwinHardware(dict(module=dict(run_command=lambda *args, **kwargs: (0, StringIO(), StringIO()))))
    assert hardware_class.get_system_profile() == {}

    # Test with an output with correct key:value pairs
    hardware_class = DarwinHardware(dict(module=dict(run_command=lambda *args, **kwargs: (0, StringIO('a: b\n\nx: y'), StringIO()))))
    assert hardware_class.get_system_profile() == {'a': 'b', 'x': 'y'}

# Generated at 2022-06-13 00:38:24.348253
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    d_hardware = DarwinHardware()
    collected_facts = dict()
    mac_facts = d_hardware.get_mac_facts()
    assert mac_facts['osversion'].startswith('15.')
    assert mac_facts['osrevision'].startswith('20160')
    assert mac_facts['model'] == 'MacBookAir6,2'

if __name__ == '__main__':
    test_DarwinHardware_get_mac_facts()

# Generated at 2022-06-13 00:38:28.995299
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware_facts = DarwinHardware(module)
    check_dict = hardware_facts.get_mac_facts()
    assert check_dict['osversion'] == '16.7.0'
    assert check_dict['osrevision'] == ''
    assert check_dict['model'] == 'MacBookPro11,4'

# Generated at 2022-06-13 00:38:40.618768
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # as get_sysctl() requires a module, we create a mock module object
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts.hardware import DarwinHardware
    module = ModuleFactCollector()

    # the mock sysctl data

# Generated at 2022-06-13 00:38:48.479802
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import ansible.module_utils.facts.hardware.darwin
    import sys

    # Create mock object to mock module_utils.common.process.get_bin_path
    mock_module = ansible.module_utils.facts.hardware.darwin
    mock_module.os = sys.modules['ansible.module_utils.facts.hardware.darwin.os']
    mock_module.get_bin_path = lambda x: '/usr/bin/vm_stat'

    # Create mock object to mock module.run_command
    mock_module.module = sys.modules['ansible.module_utils.facts.hardware.darwin.AnsibleModule']

# Generated at 2022-06-13 00:39:15.119048
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    #
    # Create an instance of DarwinHardware with an empty module
    # and check that the result of method get_system_profile is
    # of the correct type (a dictionary) and of the correct length
    #

    mac_hw = DarwinHardware(dict(module=dict()))
    system_profile = mac_hw.get_system_profile()
    assert isinstance(system_profile, dict)
    assert len(system_profile) == 19



# Generated at 2022-06-13 00:39:20.872978
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec = dict()
    )
    hardware = DarwinHardware(module=module)
    result = hardware.populate()
    assert 'processor' in result
    assert 'processor_cores' in result
    assert 'memtotal_mb' in result
    assert 'memfree_mb' in result
    assert 'model' in result
    assert 'osversion' in result
    assert 'osrevision' in result
    assert 'uptime_seconds' in result

# Generated at 2022-06-13 00:39:25.531531
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = AnsibleModuleMock()
    module.run_command = lambda x: (0, struct.pack('@L', int(time.time() - 42)), '')
    hardware_obj = DarwinHardware(module)
    uptime_facts = hardware_obj.get_uptime_facts()
    assert uptime_facts == {'uptime_seconds': 42}

# Generated at 2022-06-13 00:39:36.055864
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    # Init the class
    testdarwinhw = DarwinHardware()

    # Get the facts
    testdarwinhw.module = Mock()
    testdarwinhw.module.run_command.return_value = (0, 'hw.model: x86_64', None)
    testdarwinhw.sysctl = dict(kern=dict(osversion='10.9.1', osrevision='Darwin Kernel Version 10.9.1: Tue Oct  8 15:22:08 PDT 2013; root:xnu-2422.92.1~2/RELEASE_X86_64'))

    mac_facts = testdarwinhw.get_mac_facts()


# Generated at 2022-06-13 00:39:40.582097
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    test = DarwinHardware(None, True)
    # On a Mac, the output of system_profiler
    # is a list of lines of the form 'key: value'; for instance,
    # ['Processor Name: Intel Core i7', 'Processor Speed: 2.8 GHz']
    # The function get_system_profile should return a dictionary with
    # keys 'Processor Name' and 'Processor Speed' and values
    # 'Intel Core i7' and '2.8 GHz', respectively:

# Generated at 2022-06-13 00:39:46.857640
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import pytest

    class MockModule(object):
        def __init__(self):
            self.run_command_result = (0, 42, '')
            self.fake_time_time = 1560284807

        def run_command(self, cmd, encoding=None):
            assert encoding == None
            assert cmd == [sysctl_cmd, '-b', 'kern.boottime']
            return self.run_command_result

        def get_bin_path(self, name):
            return name

    @pytest.fixture(scope='function')
    def module(self):
        return MockModule()

    def test_error(self, module):
        module.run_command_result = (1, '', 'error')
        hardware = DarwinHardware(module)
        uptime_facts = hardware.get_upt

# Generated at 2022-06-13 00:39:57.578875
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    """
    Unit test for method DarwinHardware.get_uptime_facts
    """
    import mock
    import module_utils.facts.hardware.darwin as mock_darwin

    mock_module = mock.Mock()
    mock_module.run_command = mock.Mock()
    mock_module.get_bin_path = mock.Mock()
    mock_module.get_bin_path.return_value = "/usr/bin/sysctl"

    with mock.patch('module_utils.facts.hardware.darwin.time', mock.Mock()) as mock_time:
        mock_time.time.return_value = 1435686509.0  # 1435686509.0 = datetime.utcnow()

# Generated at 2022-06-13 00:40:06.391078
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleFailJson
    from ansible_collections.ansible.community.tests.unit.compat import mock
    from ansible_collections.ansible.community.plugins.module_utils import basic

    # The fixture to return values for run_command
    def run_command(module, command):
        return 0, 'hw.model: MacPro6,1', ''

    darwin_hardware = DarwinHardware()

    # The mac facts we are looking for

# Generated at 2022-06-13 00:40:08.813643
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hardware_collector = DarwinHardwareCollector()
    assert hardware_collector.__class__.__name__ == 'DarwinHardwareCollector'



# Generated at 2022-06-13 00:40:12.585676
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = FakeAnsibleModule({'ATTRIBUTE': 'VALUE'}, 'fixture.cfg')
    hardware_fixture = DarwinHardware(module)
    assert hardware_fixture.get_system_profile() == {'Serial Number': u'verylongstring'}


# Generated at 2022-06-13 00:40:59.962407
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    """
    A method in class DarwinHardware replicates the command vm_stat that returns
    the number of pages of different types. The results are converted to MB.
    """
    # We want to replicate the output of command vm_stat that is:
    #     'Mach Virtual Memory Statistics: (page size of 4096 bytes)
    #      Pages free:                   3099.
    #      Pages active:                 98367.
    #      Pages inactive:               28327.
    #      Pages speculative:            25277.
    #      Pages throttled:              0.
    #      Pages wired down:        212177849.
    #      Pages purgeable:              4579.
    #      "Translation faults":      4868086.
    #      Pages copy-on-write:      16995735.
    #      Pages zero filled:        62784002.

# Generated at 2022-06-13 00:41:02.868203
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hw_ins = DarwinHardwareCollector()
    assert type(darwin_hw_ins) == DarwinHardwareCollector
    assert type(darwin_hw_ins._fact_class) == DarwinHardware

# Generated at 2022-06-13 00:41:10.358496
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = DummyAnsibleModule()
    test_class = DarwinHardware(module)
    test_class.sysctl = {
        'hw.memsize': 16 * 1024 * 1024 * 1024,
        'hw.pagesize': 4096
    }

# Generated at 2022-06-13 00:41:14.691321
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = MockModule()
    darwin_hardware = DarwinHardware(module)
    memory_facts = darwin_hardware.get_memory_facts()
    assert 'memtotal_mb' in memory_facts

# Singleton instance of MockModule's object
MOCK_MODULE_OBJECT = None

# Generated at 2022-06-13 00:41:21.649669
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_module = type('module', (object,), {
        'run_command': lambda self, command: (0, ': hw.model: x86_64\n: hw.cpufrequency_max: 3000000000\n: hw.memsize: 3817678848\n', ''),
    })('test_module')
    test_dwh = DarwinHardware(test_module)
    system_profile = test_dwh.get_system_profile()

    assert system_profile['Processor Name'] == 'x86_64'


# Generated at 2022-06-13 00:41:32.765612
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    h = DarwinHardware()
    h.module = DummyModule()
    h.module.run_command = FakeCommand
    h.module.get_bin_path = get_bin_path

    # Canned output from vm_stat on a Macbook Pro with 4 GB of memory

# Generated at 2022-06-13 00:41:40.882571
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    import sys
    import json
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockModule:
        def __init__(self):
            self.run_command_called = False
            self.run_command_rc = 0
            self.run_command_out = b'sysctl hw.model: cmd not found\n'
            self.run_command_err = b''

        def run_command(self, command):
            self.run_command_called = True
            return self.run_command_rc, self.run_command_out, self.run_command_err

    # first, with no sysctl output
    module = MockModule()

# Generated at 2022-06-13 00:41:50.959708
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware_obj = DarwinHardwareCollector.fetch_facts()
    hardware_obj.populate()

    # Check for keys processor and processor_cores
    assert 'processor' in hardware_obj.populate()
    assert 'processor_cores' in hardware_obj.populate()

    # Check for keys memtotal_mb and memfree_mb
    assert 'memtotal_mb' in hardware_obj.populate()
    assert 'memfree_mb' in hardware_obj.populate()

    # Check for keys model, osversion, osrevision
    assert 'model' in hardware_obj.populate()
    assert 'osversion' in hardware_obj.populate()
    assert 'osrevision' in hardware_obj.populate()

    # Check for key uptime_seconds

# Generated at 2022-06-13 00:41:55.201412
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    hardware = DarwinHardware()
    hardware.sysctl = dict()
    hardware.sysctl['hw.memsize'] = 3958241280
    memory_facts = hardware.get_memory_facts()
    assert memory_facts == {
        'memtotal_mb': 3788,
        'memfree_mb': 3788,
    }

# Generated at 2022-06-13 00:41:56.036130
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    x = DarwinHardwareCollector()
    assert x

# Generated at 2022-06-13 00:43:36.322772
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    class TestModule:
        def __init__(self):
            self.params = dict()
            self.run_command_value = (0, '', '')

        def run_command(self, args, check_rc=True, encoding=None):
            self.called = True
            self.command_args = args
            self.check_rc = check_rc
            return self.run_command_value

    class TestDarwinHardware(DarwinHardware):
        module = TestModule()
        sysctl = {
            'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz',
            'machdep.cpu.core_count': '4',
        }

    hardware = TestDarwinHardware()


# Generated at 2022-06-13 00:43:45.176455
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = MagicMock(return_value='/usr/sbin/system_profiler')

# Generated at 2022-06-13 00:43:52.571531
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    """
    Run unit tests for method get_memory_facts in class DarwinHardware
    """
    sut = DarwinHardware(dict(), dict())

    # vm_stat return value for a not-enough-memory system.

# Generated at 2022-06-13 00:44:00.134951
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # test case 1:
    # command output: { 'kern.boottime' : b'{ sec = 1531798930, usec = 705981 }
    # expected result: { 'uptime_seconds' : 208 }
    command_output = b'{ sec = 1531798930, usec = 705981 }\n'
    expected_result = { 'uptime_seconds' : 208 }
    dw = DarwinHardware()
    result = dw.parse_uptime(command_output)
    assert expected_result == result, \
        "'uptime_seconds' is '%s', should be '%s'." % (result, expected_result)

    # test case 2:
    # command output: { 'kern.boottime' : b'{ sec = 0, usec = 0 }
    # expected result: { '

# Generated at 2022-06-13 00:44:09.139747
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    dh = DarwinHardware(dict())

    sysctl_cmd = '/usr/sbin/sysctl'
    cmd = [sysctl_cmd, '-b', 'kern.boottime']

    def side_effect(a, encoding, errors):
        # kern.boottime returns seconds and microseconds as two 64-bits
        # fields, but we are only interested in the first field.
        # Just return seconds as a string, as we do not care about
        # the second field here
        return 0, '12345678', ''

    dh.module.get_bin_path = lambda x: sysctl_cmd
    dh.module.run_command = lambda x, encoding=None, errors=None: side_effect(x, encoding, errors)

    assert dh

# Generated at 2022-06-13 00:44:16.397080
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import sys
    import platform
    import os
    import tempfile
    import shutil


# Generated at 2022-06-13 00:44:26.908675
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    mock_stdout = """Model: MacBookPro12,1
OS Version: 10.11.6
Kernel Version: Darwin 15.6.0
Kernel UUID: 0EFA9B26-2F34-3E3C-B5E6-F1C406620CA2
System Integrity Protection: enabled
"""
    mock_run_command = MagicMock(
        name='run_command',
        return_value=(0, mock_stdout, ''),
    )
    module.run_command = mock_run_command
    m = DarwinHardware(module)
    results = m.populate()
    assert results['model'] == 'MacBookPro12,1'

# Generated at 2022-06-13 00:44:34.992622
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class TestModule(object):
        def __init__(self, out, rc):
            self.out = out
            self.rc = rc

        def run_command(self, cmd, encoding=None):
            return self.rc, self.out, None

    real_time = int(time.time())