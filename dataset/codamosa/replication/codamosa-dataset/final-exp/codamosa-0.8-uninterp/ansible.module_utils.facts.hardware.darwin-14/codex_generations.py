

# Generated at 2022-06-13 00:34:59.768026
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Initialize basic module instance and class instance
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda x, encoding=None: (0, '', '')
    hardware = DarwinHardware(module)

    # Create a mock sysctl dictionary
    sysctl_dict = {
        'hw.memsize': '17179869184',
    }

    # Create a mock memory stats dictionary
    memory_stats = {
        'Pages wired down': '7793',
        'Pages active': '965',
        'Pages inactive': '1943',
    }

    # Mock get_sysctl so we don't actually run the command
    hardware.sysctl = sysctl_dict

    # Mock the command we want to unit test on

# Generated at 2022-06-13 00:35:09.193460
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    darwin = DarwinHardware()
    darwin.module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    darwin.module.run_command = MagicMock(return_value=(0, '', ''))
    darwin.sysctl = {
        'hw.memsize': '4297176064',
        'hw.physicalcpu': '1',
        'kern.boottime': 'CompileTime',
        'kern.osrevision': '15503',
        'kern.osversion': '15.6.0',
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-4870HQ CPU @ 2.50GHz'
    }
    darwin.populate()

# Generated at 2022-06-13 00:35:19.278029
# Unit test for method get_cpu_facts of class DarwinHardware

# Generated at 2022-06-13 00:35:29.454012
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():

    import ansible.module_utils.facts.hardware.darwin as darwin
    import time

    test_hardware = darwin.DarwinHardware(None, {})

    # Test with valid system uptime
    test_hardware.sysctl = dict()
    test_hardware.sysctl['kern.boottime'] = '{ sec = 1442089201, usec = 0 } Sun Sep 13 12:00:01 2015'
    test_hardware.sysctl['kern.boottime.tv_sec'] = '1442089201'
    test_hardware.sysctl['kern.boottime.tv_usec'] = '0'

    result = test_hardware.get_uptime_facts()

# Generated at 2022-06-13 00:35:35.856324
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = AnsibleModule({})
    hardware_collector = DarwinHardwareCollector({}, module)
    hardware = DarwinHardware({}, module)
    rc, out, err = module.run_command(["/usr/sbin/system_profiler", "SPHardwareDataType"])
    assert rc == 0
    system_profile = hardware.get_system_profile()
    assert system_profile['Serial Number (system):'] == out.splitlines()[1].split()[2]


# Generated at 2022-06-13 00:35:38.372247
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector._fact_class == DarwinHardware


# Generated at 2022-06-13 00:35:45.935223
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class TestModule(object):
        def __init__(self, retcode=0):
            self.retcode = retcode
            
        def run_command(self, cmd, encoding=None):
            if cmd[-1] == 'kern.boottime':
                data = 'dummy'
            else:
                data = b'\x1e\x7c\x49\x89\xa9\x3c'
            return (self.retcode, data, '')

        def get_bin_path(self, name):
            return 'sysctl'

    m = TestModule()
    h = DarwinHardware(m)

    (retcode, out, err) = m.run_command(['sysctl', '-b', 'kern.boottime'])

    uptime_seconds = h.get_uptime_

# Generated at 2022-06-13 00:35:57.467946
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = DummyModule()
    facts = DarwinHardware(module)
    setattr(facts, 'sysctl', {'hw.memsize': '1048576'})
    mock_rc_command = {0: 'Mach Virtual Memory Statistics: (page size of 4096 bytes)',
                       1: 'Pages free:                              42946.',
                       2: 'Pages active:                             5372.',
                       3: 'Pages inactive:                           10706.',
                       4: 'Pages speculative:                          627.',
                       5: 'Pages throttled:                              0.',
                       6: 'Pages wired down:                          1561.',
                       7: 'Pages purgeable:                              0.',
                       8: '"Translation faults":                  4769708.',
                       9: 'Pages copy-on-write:                    1066462.'}


# Generated at 2022-06-13 00:36:07.095693
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    set_module_args({})

    class TestDarwinHardware(DarwinHardware):

        def __init__(self, module):
            self.sysctl = dict()
            self.module = module
            self.facts = dict()

        def populate(self, collected_facts=None):
            hardware_facts = {}
            cpu_facts = self.get_cpu_facts()

# Generated at 2022-06-13 00:36:12.820273
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # Unit test for method DarwinHardwareCollector.__init__()
    c = DarwinHardwareCollector()

    # Verify that the correct class was instantiated
    assert isinstance(c, DarwinHardwareCollector)
    assert isinstance(c, HardwareCollector)

    # Verify that the _fact_class attribute was set correctly
    assert c._fact_class == DarwinHardware
    assert c._fact_class.platform == 'Darwin'

# Generated at 2022-06-13 00:36:32.922958
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModuleMock()
    hardware = DarwinHardware(module)
    hardware.sysctl = {
        'kern.osversion': '12.2',
        'kern.osrevision': '15C50',
        'hw.memsize': '256',
        'hw.physicalcpu': '1',
        'hw.logicalcpu': '1',
        'hw.ncpu': '1',
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz',
        'machdep.cpu.core_count': '4',
    }
    hardware.get_mac_facts = MagicMock(return_value={'a': 'b'})

# Generated at 2022-06-13 00:36:40.756122
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # A sample output from /usr/bin/vm_stat command
    VM_MEMORY_STATS = """
Mach Virtual Memory Statistics: (page size of 4096 bytes)
Pages free:                               210439.
Pages active:                             106934.
Pages inactive:                           29981.
Pages speculative:                         3610.
Pages wired down:                         13107.
Pages purgeable:                           6090.
Pages occupied by compressor:               901.
Pages used by compressed swap:               11.
Decompressions:                            58606.
Compressions:                            393945.
Pageins:                                 7190352.
Pageouts:                                1518579.
Swapins:                                 1475242.
Swapouts:                                1678553.
"""
    module = AnsibleModuleStub()
    # We can't mock

# Generated at 2022-06-13 00:36:43.133692
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    d = DarwinHardwareCollector()
    assert isinstance(d._fact_class, type(DarwinHardware))

# Generated at 2022-06-13 00:36:55.704221
# Unit test for method get_system_profile of class DarwinHardware

# Generated at 2022-06-13 00:37:02.615545
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = AnsibleModule(dict())
    hardware_fact_module = DarwinHardware(module)

    # Mock the command output
    hardware_fact_module.module.run_command = Mock(return_value=(0, b'\x00\x00\x00\x00\x00\x00\x00\x00', ''))

    result = hardware_fact_module.get_uptime_facts()

    assert result['uptime_seconds'] > 0

# Generated at 2022-06-13 00:37:12.754262
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    class MockModule:
        def run_command(self, cmd):
            if cmd == ['/usr/sbin/system_profiler', 'SPHardwareDataType']:
                return (0, 'Processor Name: Intel(R) Core(TM) i7-4970HQ CPU @ 2.20GHz\nProcessor Speed: 2.2 GHz\n', '')
            elif cmd == ['sysctl', 'hw.model']:
                return (0, 'hw.model: MacBookPro11,4', '')
            elif cmd == ['sysctl', 'machdep.cpu.core_count']:
                return (0, 'machdep.cpu.core_count: 6\n', '')

# Generated at 2022-06-13 00:37:18.588250
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    '''class DarwinHardware.get_uptime_facts'''
    class MockModule(object):
        def get_bin_path(self, binary):
            return binary
        def run_command(self, cmd, encoding=None):
            return (0, struct.pack('@L', 1522775210), None)

    module = MockModule()
    hardware = DarwinHardware(module)
    assert hardware.get_uptime_facts() == {'uptime_seconds': 1522775210}

# Generated at 2022-06-13 00:37:22.350711
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, "", "")

    hardware = DarwinHardware(module_mock)

    # Make sure uptime_seconds is a number
    facts = hardware.get_uptime_facts()
    assert(isinstance(facts['uptime_seconds'], int))

# Generated at 2022-06-13 00:37:32.668640
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Test with an Intel processor
    sysctl = {'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-7920HQ CPU @ 3.10GHz', 'machdep.cpu.core_count': '8'}
    module = create_mock({'run_command': [0, '', ''], 'get_bin_path': ''})
    hardware = DarwinHardware(module)
    hardware.sysctl = sysctl
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-7920HQ CPU @ 3.10GHz'
    assert cpu_facts['processor_cores'] == '8'
    assert 'processor_vcpus' not in cpu_facts

    # Test with a PowerPC processor
    sysctl

# Generated at 2022-06-13 00:37:37.175686
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.facts.hardware import DarwinHardware
    from ansible.module_utils._text import to_bytes

    module = AnsibleModuleMock()
    darwin_hardware = DarwinHardware(module)

    # Empty system_profiler output: no keys in output
    module.run_command.return_value = (0, "", "")
    assert darwin_hardware.get_system_profile() == {}

    # Missing colon in output: keys will not be added to output
    module.run_command.return_value = (0, "       Hardware:\n", "")
    assert darwin_hardware.get_system_profile() == {}

    # One line of output: dictionary contains 1 key
    module.run_command.return_value

# Generated at 2022-06-13 00:37:57.073759
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    import mock
    module = mock.Mock()
    mac_hardware = DarwinHardware(module)
    mac_hardware.sysctl = {
        'hw.physicalcpu': 1,
        'hw.logicalcpu': 1,
        'hw.ncpu': 1,
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-4980HQ CPU @ 2.80GHz',
        'machdep.cpu.core_count': 1
    }
    mac_hardware.get_system_profile = mock.Mock(return_value={})
    result = mac_hardware.get_cpu_facts()

# Generated at 2022-06-13 00:38:07.653843
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.hardware.posix import PosixHardware
    import os
    import tempfile
    import unittest

    class Test(unittest.TestCase):

        def setUp(self):
            self.base = PosixHardware()
            self.base.module = FakeAnsibleModule()
            self.base.module.run_command = run_command_mock
            self.darwin_hardware = DarwinHardware()
            self.darwin_hardware.module = FakeAnsibleModule()
            self.darwin_hardware.module.run_command = run_command_mock
            self.darwin_hardware.sysctl = {}

# Generated at 2022-06-13 00:38:16.421046
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    """Test function for method get_memory_facts in DarwinHardware class."""

    def test_run_command(arg):
        """Helper function to replace module.run_command.
        Takes one argument and returns a list consisting of the desired vm_stat output."""
        test_return = [0, 'Mach Virtual Memory Statistics: (page size of 4096 bytes)\n' + arg, '']
        return test_return

    # Declare a mock class for the ansible module class
    class MockModule(object):
        run_command = test_run_command

        @staticmethod
        def get_bin_path(arg):
            # Mock get_bin_path to return vm_stat
            return 'vm_stat'

    # Define a dictionary of arguments passed to the module

# Generated at 2022-06-13 00:38:27.688445
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    """
    Ensure that the method DarwinHardware.get_uptime_facts return the correct uptime_seconds
    """
    # Time at which to set the system time
    reference_time = 1486439833.0

    # Format of the struct returned by sysctl kern.boottime
    # TODO: Test also on big endian
    struct_format = '@L'  # unsigned long
    struct_size = struct.calcsize(struct_format)

    # Result we expect to get
    expected_uptime_seconds = int(time.time() - reference_time)

    # Create a DarwinHardware object
    h = DarwinHardware()
    h.module = FakeAnsibleModule()

    # Monkey patch the run_command method
    # The sysctl command will return the reference_time

# Generated at 2022-06-13 00:38:30.406661
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    x = DarwinHardwareCollector()
    assert x.platform == 'Darwin'
    assert x._fact_class == DarwinHardware


# Generated at 2022-06-13 00:38:41.352303
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    """
    Unit test to check that the system_profiler command is parsed correctly.
    """

# Generated at 2022-06-13 00:38:43.456448
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """Test constructor of class DarwinHardwareCollector"""
    darwin_hw_collector = DarwinHardwareCollector()
    assert darwin_hw_collector._fact_class == DarwinHardware

# Generated at 2022-06-13 00:38:55.502261
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    # Load system_profiler output to be able to mock the return value of the function
    test_data_file = open('test/system_profiler.txt', 'r')
    test_data = test_data_file.read()
    test_data_file.close()

    # Create a fake module
    module_mock = type('module', (object,), {})()
    module_mock.run_command = lambda cmd: (0, test_data, '')
    module_mock.check_mode = False
    module_mock.debug = False

    # Instanciate the class to test
    hardware = DarwinHardware()
    hardware.module = module_mock

    system_profile = hardware.get_system_profile()

    assert(system_profile['Model Identifier'] == 'Macmini6,2')
   

# Generated at 2022-06-13 00:39:01.452510
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = get_mock_module()
    obj = MacHardware(module)
    rc = 0
    out = 'hw.model: iMac12,1'
    err = ''
    (rc, out, err) = module.run_command.return_value

    result = obj.get_mac_facts()
    assert result['model'] == 'iMac12,1'
    assert result['osversion'] == '15.6.0'
    assert result['osrevision'] == '15G1004'



# Generated at 2022-06-13 00:39:10.757413
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    # Test get_system_profile on a darwin machine
    fake_module_obj = FakeModule()
    hardware_obj = DarwinHardware(fake_module_obj)
    assert hardware_obj.get_system_profile() == {}
    # Test get_system_profile on a non-darwin machine
    fake_module_obj = FakeModule(cmd_results=dict(
        run_command=dict(
            rc=1,
            out='',
            err='',
        ),
    ))
    hardware_obj = DarwinHardware(fake_module_obj)
    assert hardware_obj.get_system_profile() == {}


# Generated at 2022-06-13 00:39:39.821377
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    mac_facts = {'model': 'MacPro5,1', 'osversion': '15.2.0', 'osrevision': '16C67'}
    sysctl = {'hw.physicalcpu': 8, 'hw.logicalcpu': 8, 'hw.ncpu': 8, 'machdep.cpu.brand_string': 'Intel(R) Xeon(R) CPU E5462 @ 2.80GHz', 'machdep.cpu.core_count': 8}
    darwin_hw = DarwinHardware({'module_setup': True, 'bin_path': '/usr/bin/', 'sysctl': sysctl, 'devices': [{'class': 'mac', 'facts': mac_facts}]})
    cpu_facts = darwin_hw.get_cpu_facts()

# Generated at 2022-06-13 00:39:41.177410
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # Checking if object initialization is successful or not.
    obj = DarwinHardwareCollector()
    assert obj

# Generated at 2022-06-13 00:39:43.018890
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    harware = DarwinHardware(module)
    hardware = harware.populate()
    assert hardware is not None
    assert len(hardware) > 0

# Generated at 2022-06-13 00:39:48.007967
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = type("AnsibleModule", (object,), dict(run_command=run_command))
    fact_class = type("DarwinHardware", (object,), dict(module=module))
    fact_method = getattr(fact_class, "get_uptime_facts")

    def run_command(self, args, encoding=None):
        return 0, struct.pack("@L", int(time.time()) - 10), ""

    assert fact_method() == {'uptime_seconds': 10}

# Generated at 2022-06-13 00:39:58.852200
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModuleMock()

    # The 'vm_stat' command returns a different result on different versions
    # of macOS. For example:
    # - 10.13 (High Sierra):
    #     vm_stat
    #     Mach Virtual Memory Statistics: (page size of 4096 bytes)
    #     Pages free:                               177.
    #     Pages active:                             532.
    #     Pages inactive:                           390.
    #     Pages wired down:                         1126.
    #     Pages purgeable:                           13.
    #     "Translation faults":                     706278.
    #     Pages copy-on-write:                     182414.
    #     Pages zero filled:                       246252.
    #     Pages reactivated:                        12772.
    #     Pages purged:                             14675.
    #     File-

# Generated at 2022-06-13 00:40:06.501162
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = MockModule()
    hardware = DarwinHardware(module)

    # test get_mac_facts
    module.run_command.return_value = (0, 'hw.model: MacPro6,1', '')
    # osversion = kern.osversion = "17.4.0"
    hardware.sysctl = {'kern.osversion': '17.4.0', 'kern.osrevision': '1680.22.78', }

    result = hardware.get_mac_facts()
    assert result == {'model': 'MacPro6,1', 'osversion': '17.4.0', 'osrevision': '1680.22.78'}


# Generated at 2022-06-13 00:40:15.658343
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    hardware = DarwinHardware()

    # Create an object with a mocked run_command method

# Generated at 2022-06-13 00:40:18.188205
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware = DarwinHardware()
    hardware_facts = hardware.populate()
    for key, value in hardware_facts.items():
        assert isinstance(key, str)
        assert key in hardware_facts
        assert value

# Generated at 2022-06-13 00:40:21.644735
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    assert DarwinHardware().get_system_profile() is not None

# Generated at 2022-06-13 00:40:30.744111
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Create a dummy module for passing commands
    module = type('', (), {
        'run_command': lambda *args, **kwargs: (0, '', ''),
        'get_bin_path': lambda *args, **kwargs: '',
        '_socket': lambda *args, **kwargs: '',
        'nxos_provider_spec': lambda *args, **kwargs: '',
    })()

    # Create a dummy class for DarwinHardware
    class DarwinHardware():
        def __init__(self):
            self.module = module

# Generated at 2022-06-13 00:41:15.112019
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.hardware.base import Hardware
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    class FakeModule:
        def __init__(self):
            self.params = {}
            self.run_command_values = {}
            self.run_command_results = []
            self.run_command_calls = []

        def get_bin_path(self, arg, opt_dirs=[]):
            return '/usr/bin/' + arg

    class FakeMemory:
        def __init__(self, pages_wired_down, pages_active, pages_inactive):
            self.pages_wired_down = pages

# Generated at 2022-06-13 00:41:23.692523
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import unittest
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(object):
        def run_command(self, command, encoding=None):
            return (0, test_data, '')

    test_data = struct.pack('@L', (time.time() - 100000))
    kern_boottime, = struct.unpack('@L', test_data[:8])
    expected_data = {'uptime_seconds': int(time.time() - kern_boottime)}

    dh = DarwinHardware()
    dh.module = FakeModule()
    data = dh.get_uptime_facts()
    assert data == expected_data



# Generated at 2022-06-13 00:41:35.086265
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    sut = DarwinHardware()

# Generated at 2022-06-13 00:41:42.285541
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = type('', (), dict())()
    module.run_command = run_command
    darwin_hardware = DarwinHardware(module)

    class Object(object):
        pass

    vm_stats = Object()
    vm_stats.Pages = Object()
    vm_stats.Pages.wired_down = 1
    vm_stats.Pages.active = 2
    vm_stats.Pages.inactive = 3
    darwin_hardware.sysctl = {'hw.memsize': "12884901888"}

    def run_command(command, **kwargs):
        return (0, vm_stats, obj)

    real_run_command = darwin_hardware.module.run_command


# Generated at 2022-06-13 00:41:52.941340
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = FakeModule()
    hardware = DarwinHardware(module=module)
    hardware._get_system_profile = lambda: {}

    # Find vm_stat
    vm_stat = '/usr/bin/vm_stat'
    hardware.module.get_bin_path = lambda x: vm_stat

    vm_stat_out_free = '''
    Mach Virtual Memory Statistics: (page size of 4096 bytes)
    Pages free:                            3179.
    '''
    vm_stat_out_notfree = '''
    Mach Virtual Memory Statistics: (page size of 4096 bytes)
    Pages wired down:                      1005.
    Pages active:                          68909.
    Pages inactive:                        3250.
    '''

# Generated at 2022-06-13 00:42:01.378269
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    import builtins
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    darwin_hardware = DarwinHardware(None)

    darwin_hardware.module = builtins.__dict__['__builtins__']['FakeModule']()

    darwin_hardware.module.run_command = lambda x: (
        0,
        """
{
    "kern.osversion": "19.0.0",
    "kern.osrevision": "19.0.0",
}
""",
        "")

    darwin_hardware.sysctl = darwin_hardware.get_sysctl()

    facts = darwin_hardware.get_mac_facts()
    assert facts['model'] == 'MacBookPro'
    assert facts['osversion']

# Generated at 2022-06-13 00:42:03.130664
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import doctest
    failed, tests = doctest.testmod(DarwinHardware)
    assert failed == 0



# Generated at 2022-06-13 00:42:08.710789
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    d = DarwinHardware()
    d.sysctl = {
        'hw.model': "iMac19,1\n",
        'kern.osversion': "19.6.0\n",
        'kern.osrevision': "15G20015\n"
    }
    assert d.get_mac_facts() == {
        'model': "iMac19,1",
        'product_name': "iMac19,1",
        'osversion': "19.6.0",
        'osrevision': "15G20015"
    }


# Generated at 2022-06-13 00:42:14.028393
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    darwin_facts = DarwinHardware()
    # Create an OS object
    darwin_facts.module = {
        'run_command': mock_run_command,
    }
    facts = darwin_facts.get_memory_facts()
    assert facts['memtotal_mb'] == 16
    assert facts['memfree_mb'] == 5



# Generated at 2022-06-13 00:42:23.629614
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class TestClass:
        def get_bin_path(self, value, opt_dirs=[]):
            return 'vm_stat'


# Generated at 2022-06-13 00:44:12.149573
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():

    module = Mock(fail_json=None, run_command=None, get_bin_path=None)

# Generated at 2022-06-13 00:44:17.814465
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModuleMock()
    mac_facts = {
        'osversion': '16.7.0',
        'osrevision': '1510.71.9',
        'model': 'MacBookPro13,1',
        'product_name': 'MacBookPro13,1',
        'uptime_seconds': 18037,
        'memtotal_mb': 16384,
        'memfree_mb': 16334,
        'processor_cores': 4,
        'processor_vcpus': 4,
        'processor': 'Intel(R) Core(TM) i5-8257U CPU @ 1.40GHz'
    }


# Generated at 2022-06-13 00:44:28.623674
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    module = MockModule()
    module.run_command.return_value = 0, "hw.model: x86_64", ""
    module.run_command.return_value = 0, "kern.osversion: 12.3.0", ""
    module.run_command.return_value = 0, "kern.osrevision: 12345", ""
    darwin_hardware = DarwinHardware(module)
    mac_facts = darwin_hardware.get_mac_facts()
    assert mac_facts['model'] == "x86_64"
    assert mac_facts['osversion'] == "12.3.0"
    assert mac_facts['osrevision'] == 12345



# Generated at 2022-06-13 00:44:29.695034
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    DarwinHardware.get_mac_facts(module)

# Generated at 2022-06-13 00:44:37.054298
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware


# Generated at 2022-06-13 00:44:43.942218
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    darwin_hardware = DarwinHardware(module, dict())
    # Test 1
    darwin_hardware.sysctl = \
        {'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-6560U CPU @ 2.20GHz'}
    darwin_hardware.sysctl['machdep.cpu.core_count'] = 2
    cpu_facts = darwin_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-6560U CPU @ 2.20GHz'
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_vcpus'] == ''
    # Test 2
    darwin_hardware.sys