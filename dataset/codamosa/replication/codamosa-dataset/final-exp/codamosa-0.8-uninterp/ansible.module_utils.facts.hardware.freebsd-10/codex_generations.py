

# Generated at 2022-06-13 00:45:32.981545
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hw = FreeBSDHardware()

    # Set test values for get_cpu_facts method
    hw.module = object()
    hw.module.get_bin_path = lambda x: '/usr/bin/sysctl'

    import os
    os.environ['PATH'] += ':/usr/bin'
    hw.module.run_command = lambda x: ("", 'hw.ncpu: 8\n', '')

    cpu_facts = {'processor_count': '8', 'processor': ['Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz']}
    hw._populate_from_files = lambda: True

    result_cpu_facts = hw.get_cpu_facts()

    assert result_cpu_facts['processor_count'] == cpu_facts['processor_count']
   

# Generated at 2022-06-13 00:45:39.457514
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Prepare a module mock object
    module = type("AnsibleModule", (object,), dict(check_mode=False, params={}))()
    module.run_command = lambda *_args, **_kwargs: ([0, '', ''], 'out', 'err')
    module.get_bin_path = lambda *_args, **_kwargs: 'sysctl'

    # Run the tested code
    hw = FreeBSDHardware(module)
    hw.get_memory_facts()

    # Test that AnsibleModule.run_command was called
    assert module.run_command.called



# Generated at 2022-06-13 00:45:46.034675
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModuleMock()
    bsdhw = FreeBSDHardware(module=module)
    result = bsdhw.populate()
    for k in ('system_vendor', 'bios_version', 'product_serial'):
        assert result.get(k) is not None
        assert result.get(k) == 'NA'



# Generated at 2022-06-13 00:45:56.660697
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class MockModule():
        def __init__(self):
            pass

        def run_command(self, args, encoding=None):
            cmd = ['/usr/sbin/sysctl', '-b', 'kern.boottime']
            if args != cmd:
                raise Exception("wrong command: %s vs %s" % (args, cmd))
            if encoding is not None:
                raise Exception("bad encoding: %s" % encoding)
            return (0, struct.pack('@L', 1000), '')

        def get_bin_path(self, bin_name):
            return '/usr/local/bin/%s' % bin_name

    mockModule = MockModule()
    uptime_facts = FreeBSDHardware(mockModule).get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == int

# Generated at 2022-06-13 00:46:00.064268
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    x = FreeBSDHardwareCollector()
    # test for class name
    assert 'FreeBSDHardwareCollector' in str(x.__class__)
    # test for class parent name
    assert 'HardwareCollector' in str(x.__class__.__bases__)

# Generated at 2022-06-13 00:46:10.709253
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    '''
    Fake fstatvfs function to simulate TimeoutError
    '''
    class fake_statvfs():
        f_bsize = 512
        f_frsize = 512
        f_blocks = 97664256
        f_bfree = 0
        f_bavail = 0
        f_files = 192512
        f_ffree = 0
        f_favail = 0
        f_flag = 4096
        f_namemax = 255
        def __init__(self):
            pass

    class fake_time():
        def __init__(self):
            pass
        def time(self):
            return 1234567890

    fake_os = {
        'statvfs': fake_statvfs,
    }

    fake_statvfs_object = fake_statvfs()


# Generated at 2022-06-13 00:46:22.269731
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import pytest

    class ModuleStub:
        def get_bin_path(self, name):
            return 'sysctl'

        def run_command(self, cmd, encoding=None, errors=None, check_rc=False):
            return 0, 'kern.boottime: Thu Apr  5 18:58:32 2018', ''

    class FactCacheStub:
        def __init__(self):
            self.cmd_cache = {}

        def get_cmd_output(self, cmd):
            return self.cmd_cache[cmd]

        def set_cmd_output(self, cmd, out):
            self.cmd_cache[cmd] = out

    module = ModuleStub()
    fact_cache = FactCacheStub()

    fact_module = FreeBSDHardware(module=module, fact_cache=fact_cache)

   

# Generated at 2022-06-13 00:46:27.010112
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = get_module()

    # Example from Debian

# Generated at 2022-06-13 00:46:36.496642
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    freebsd_hardware = FreeBSDHardware(module)

    assert type(freebsd_hardware.get_uptime_facts()) is dict


# If run as a script, instantiate test object
if __name__ == '__main__':
    from ansible.module_utils.basic import AnsibleModule
    import json
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    hw = FreeBSDHardware(module=module, timeout=60)
    facts = hw.populate()

    # Print the collected facts in JSON format
    print(json.dumps(facts))

# Generated at 2022-06-13 00:46:47.086074
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''Unit tests for method get_dmi_facts of class FreeBSDHardware'''
    module = AnsibleModule(argument_spec={})

    # Mock method get_bin_path of module
    dmi_bin = '/tmp/dmidecode'
    def mock_get_bin_path(cmd):
        return dmi_bin
    module.get_bin_path = mock_get_bin_path

    # Mock method run_command of module
    def mock_run_command(cmd, check_rc=None):
        output = []
        output.append('# dmidecode 3.0')
        output.append('Getting SMBIOS data from sysfs.')
        output.append('SMBIOS 2.7 present.')

# Generated at 2022-06-13 00:47:12.972547
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())

    fhw = FreeBSDHardware()
    fhw.get_memory_facts()

# Generated at 2022-06-13 00:47:15.886316
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    hardware_collector = FreeBSDHardwareCollector(module=module,
                                                  share=module.shared_loader_obj)
    hardware_facts = hardware_collector.collect()['ansible_facts']
    assert hardware_facts['ansible_processor_count'] is not None
    assert hardware_facts['ansible_devices'] is not None
    assert hardware_facts['ansible_mounts'] is not None

# Generated at 2022-06-13 00:47:20.273497
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    fact_collector = FreeBSDHardwareCollector(module, {})
    assert fact_collector.platform == "FreeBSD"
    assert fact_collector._fact_class.platform == "FreeBSD"

# Generated at 2022-06-13 00:47:28.356021
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = MockModule()

    # Mock the sysctl command for unit testing
    sysctl_mock_path = os.path.join(os.path.dirname(__file__), 'fixtures/sysctl_mock')
    module.run_command = Mock(return_value=(0, open(sysctl_mock_path).read(), ''))

    hardware = FreeBSDHardware(module)

    # Tests
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] == 60



# Generated at 2022-06-13 00:47:33.551555
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # We do not mock the command, but we pass the test anyway since
    # the only method called by get_uptime_facts returns a hard-coded
    # dictionary.
    module = MockModule()
    fact_class = FreeBSDHardware(module=module)
    assert fact_class.get_uptime_facts() == {'uptime_seconds': 0}
    module.exit_json.assert_not_called()
    module.fail_json.assert_not_called()



# Generated at 2022-06-13 00:47:36.485970
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class args:
        module = None
        timeout = 10
    h = FreeBSDHardware(args)
    h.populate()
    assert 'processor_count' in h.facts

# Generated at 2022-06-13 00:47:41.912401
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hardware = FreeBSDHardware({'module': False})

    hardware.module.run_command = run_mock

    f = open('tests/data/FreeBSD/dmesg.boot')
    dmesg_boot = f.read()

    results = hardware.get_cpu_facts()

    assert results['processor'] == ['Intel(R) Core(TM) i5-6600K CPU @ 3.50GHz']
    assert results['processor_cores'] == '4'
    assert results['processor_count'] == '4'



# Generated at 2022-06-13 00:47:54.428509
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    mem = 0
    swap = 0
    free = 0
    sysctl = 'sysctl'
    rc, out, err = os.system("%s -n hw.physmem && %s -n vm.stats.vm.v_page_size && %s -n vm.stats.vm.v_free_count && %s -n vm.stats.vm.v_page_count && %s -n vm.stats.vm.v_swappgsin && %s -n vm.stats.vm.v_swappgsout && %s -n vm.stats.vm.v_swappginuse && %s -n vm.stats.vm.v_swapoutuse" % (sysctl, sysctl, sysctl, sysctl, sysctl, sysctl, sysctl, sysctl))
    if rc == 0:
        mem = int

# Generated at 2022-06-13 00:48:00.413802
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    obj = FreeBSDHardware()
    obj.module.run_command = lambda *args, **kwargs: (0, '2', '')
    assert isinstance(obj.get_cpu_facts(), dict)
    with open(__file__) as f:
        [line for line in f if 'CPU:' in line]
        obj.module.run_command = lambda *args, **kwargs: (0, [line for line in f if 'CPU:' in line][0], '')
        assert isinstance(obj.get_cpu_facts(), dict)


# Generated at 2022-06-13 00:48:06.517693
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():

    class FakeModule(object):
        def __init__(self, bin_path=None):
            self.bin_path=bin_path
        def get_bin_path(self, name, required=False):
            return self.bin_path

    # Mocking module
    module_mock = FakeModule(bin_path=None)

    assert FreeBSDHardware(module=module_mock).get_uptime_facts() == {}

    # Mocking module
    module_mock = FakeModule(bin_path='/bin')

# Generated at 2022-06-13 00:48:57.603342
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts import collector
    import time
    import os

    class OSModuleFake:
        def get_bin_path(self, _):
            return 'true'

        def run_command(self, cmd, check_rc=False, encoding=None):
            return 0, os.urandom(struct.calcsize('L')), ""

    hardware = FreeBSDHardware(OSModuleFake())
    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == int(time.time() - struct.unpack('>L', os.urandom(struct.calcsize('L')))[0])

collector.add_collector(FreeBSDHardwareCollector)

# Return a list of collecters required for this platform
# to work properly.  For FreeBSD,

# Generated at 2022-06-13 00:49:07.225994
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    facts = FreeBSDHardware(module).populate()

# Generated at 2022-06-13 00:49:15.974484
# Unit test for method populate of class FreeBSDHardware

# Generated at 2022-06-13 00:49:17.676580
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    # Create the object
    hardware_c = FreeBSDHardwareCollector()
    #
    # TODO: Add assert statements
    #

# Generated at 2022-06-13 00:49:21.680832
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    freebsd_hw_module = FreeBSDHardware({})
    freebsd_hw_facts = freebsd_hw_module.populate()

    assert 'memfree_mb' in freebsd_hw_facts
    assert 'memtotal_mb' in freebsd_hw_facts
    assert 'processor' in freebsd_hw_facts
    assert 'devices' in freebsd_hw_facts

# Generated at 2022-06-13 00:49:29.294144
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hostname = u'localhost'
    port = 22
    username = u'root'
    password = u''
    tmpdir = u'test/integration/tmp'
    become = False
    become_method = u'local1'

    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    obj = FreeBSDHardware(module=None)
    obj.module.get_bin_path = lambda *args, **kwargs: None
    facts = obj.populate()
    import pprint
    pprint.pprint(facts)



# Generated at 2022-06-13 00:49:41.359470
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class FakeModule():
        def __init__(self, exit_code):
            self.exit_code = exit_code
            self.executed = []

        def get_bin_path(self, exe):
            return '/path/to/dmidecode'

        def run_command(self, cmd):
            self.executed.append(cmd)

# Generated at 2022-06-13 00:49:52.474118
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import get_collector_facts

    my_module = AnsibleModule()
    fhw = FreeBSDHardware(my_module)

    pfacts = get_collector_facts(my_module)

    facts = fhw.populate()

    assert facts is not None

    assert 'uptime_seconds' in facts

    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts

    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts

    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts


# Generated at 2022-06-13 00:49:57.978399
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    freebsd_hardware = FreeBSDHardware()
    # Get the current time
    curr_time = time.time()
    # Get the uptime facts
    uptime_facts = freebsd_hardware.get_uptime_facts()
    # Check if the uptime facts are not empty
    assert (uptime_facts)
    # Check if uptime_seconds is not negative
    assert (int(curr_time - uptime_facts['uptime_seconds']) > 0)

# Generated at 2022-06-13 00:50:08.362740
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """ This unit test case checks if the method populate()
    of class FreeBSDHardware return the right values on FreeBSD.
    """
    class Module(object):
        def __init__(self, run_command_ans):
            self.run_command_ans = run_command_ans

        def run_command(self, cmd, encoding=None, check_rc=False):
            return self.run_command_ans[cmd]

        def get_bin_path(self, name, opt_dirs=[]):
            return name


# Generated at 2022-06-13 00:51:24.333352
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():

    class MockModule(object):
        def __init__(self):
            self.params = {
                'run_command_check_rc': True,
                'run_command_encoding': None,
            }

        def get_bin_path(self, arg):
            if arg == 'sysctl':
                return 'sysctl'
            return None

        def run_command(self, command, check_rc=None, encoding=None):
            if command == 'sysctl -b kern.boottime':
                # Dummy output from sysctl.
                return 0, bytes([0, 0, 0, 0, 0, 0, 0, 4]), list()

            raise Exception('Unexpected command %s' % command)

    # Create a module and a FreeBSDHardware object
    module = MockModule()
    hardware = FreeBSDHardware(module)

   

# Generated at 2022-06-13 00:51:25.766887
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhwc = FreeBSDHardwareCollector()
    # Test for class attributes
    assert fhwc.platform == 'FreeBSD'
    assert fhwc.fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:51:32.794582
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    if module._name == 'freebsd_hardware':
        # Create empty object and populate it with data
        hardware = FreeBSDHardware(module)
        dmi_facts = hardware.get_dmi_facts()

        # Check if dmi_facts has some data containing
        if len(dmi_facts.keys()) < 1:
            module.fail_json(msg="Empty output of dmidecode command")



# Generated at 2022-06-13 00:51:42.342035
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class MockModule:
        def __init__(self):
            self.params = { 'timeout': 1 }
            self.run_command_dict = { 'swapinfo -k': ("Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%", "", "") }

        def run_command(self, cmd, check_rc=True, encoding=None):
            return self.run_command_dict[cmd]

    class MockFreeBSDHardware:
        def __init__(self, module):
            self.module = module

        def get_memory_facts(self):
            return super(MockFreeBSDHardware, self).get_memory_facts()

    class MockHardware:
        @staticmethod
        def get_file_content(filename):
            return None

# Generated at 2022-06-13 00:51:43.550664
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    facts = FreeBSDHardwareCollector()
    assert facts.platform == 'FreeBSD'
    assert isinstance(facts, HardwareCollector)


# Generated at 2022-06-13 00:51:49.889396
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hardware = FreeBSDHardware(dict())

    def test(cmd_out, expected):
        hardware.module.run_command = lambda cmd: (0, cmd_out, '')
        assert hardware.get_memory_facts() == expected

    test('''
vm.stats.vm.v_page_size: 4096
vm.stats.vm.v_page_count: 15538944
vm.stats.vm.v_free_count: 12677422
''', {
        'memtotal_mb': 60916,
        'memfree_mb': 49822,
    })

# Generated at 2022-06-13 00:51:51.322975
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    facts = FreeBSDHardware().get_cpu_facts()
    assert facts['processor_count'] > 0


# Generated at 2022-06-13 00:51:53.376224
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """This will test the constructor of FreeBSDHardwareCollector class"""
    collector = FreeBSDHardwareCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class._platform == 'FreeBSD'

# Generated at 2022-06-13 00:52:04.721837
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts import FallbackModuleUtils
    from ansible.module_utils.facts.utils import get_file_content, get_mount_size

    class SomeRandomClass:
        pass

    module = SomeRandomClass()
    module.run_command = FallbackModuleUtils.run_command
    module.exit_json = FallbackModuleUtils.exit_json
    module.exit_json.__code__ = FallbackModuleUtils.exit_json.__code__
    module.fail_json = FallbackModuleUtils.fail_json
    module.fail_json.__code__ = FallbackModuleUtils.fail_json.__code__

    # dmidecode
    module.get_bin_path = Fall

# Generated at 2022-06-13 00:52:12.914209
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module_mock = type('', (), {})()
    module_mock.run_command = lambda cmd: ([0, 0, ''], 'Chassis Type: Rack Mount Chassis')
    module_mock.get_bin_path = lambda cmd: ''
    hw = FreeBSDHardware({})
    hw.module = module_mock
    dmi_facts = hw.get_dmi_facts()
    assert 'form_factor' in dmi_facts
    assert 'Rack Mount Chassis' == dmi_facts['form_factor']