

# Generated at 2022-06-13 00:45:33.619666
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import pytest

    class MockModule:
        binary_files = {'sysctl': '/bin/sysctl'}

        class MockRunCommand:
            def __init__(self, stdout, stderr, rc):
                self.stdout = stdout
                self.stderr = stderr
                self.rc = rc

            def __call__(self, cmd, encoding=None):
                return (self.rc, self.stdout, self.stderr)

        def __init__(self):
            self._run_command = self.MockRunCommand('foo', 'bar', 123)

        def get_bin_path(self, name):
            return self.binary_files[name]

        def run_command(self, cmd, encoding=None):
            return self._run_command(cmd, encoding)

   

# Generated at 2022-06-13 00:45:35.023966
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    # Test construction of FreeBSDHardwareCollector
    fhwc = FreeBSDHardwareCollector()
    assert(fhwc)


# Generated at 2022-06-13 00:45:47.464911
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():

    class Module(object):
        def __init__(self):
            self.run_command = MagicMock(
                return_value=(0, 'hw.ncpu: 4\nvm.stats.vm.v_page_size: 4096\nvm.stats.vm.v_page_count: 2273966\nvm.stats.vm.v_free_count: 1418450\n', '')
            )
            self.get_bin_path = MagicMock(return_value='sysctl')


    class TestFreeBSDHardware(FreeBSDHardware):
        def __init__(self, module):
            self.module = module


    hardware = TestFreeBSDHardware(Module())
    facts = hardware.get_memory_facts()

    assert facts['memfree_mb'] == 5512
    assert facts['swaptotal_mb']

# Generated at 2022-06-13 00:45:55.562373
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    sysctl = ModuleFactCollector()
    sysctl.get_bin_path = lambda x: 'echo'
    sysctl.run_command = lambda x: (0, 'hw.ncpu: 1\nhw.physmem: 1\nhw.realmem: 1', None)

    hw = FreeBSDHardware(sysctl)
    facts = hw.get_memory_facts()

    assert(facts['memtotal_mb'] == 1)
    assert(facts['swaptotal_mb'] == 0)
    assert(facts['memfree_mb'] == 0)
    assert(facts['swapfree_mb'] == 0)



# Generated at 2022-06-13 00:46:03.702789
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    factClass = FreeBSDHardware()
    factClass.module = MockModule()

    factClass.module.run_command = Mock(return_value=(0, '8\n', ''))
    cpu_facts = factClass.get_cpu_facts()
    assert cpu_facts['processor_count'] == '8'

    factClass.module.run_command = Mock(return_value=(0, 'RCA 8080', ''))
    cpu_facts = factClass.get_cpu_facts()
    assert cpu_facts['processor'] == ['RCA 8080']

    factClass.module.run_command = Mock(return_value=(0, 'Logical CPUs per core: 4', ''))
    cpu_facts = factClass.get_cpu_facts()
    assert cpu_facts['processor_cores'] == '4'


# Generated at 2022-06-13 00:46:08.347009
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    bsd_handler = FreeBSDHardwareCollector()
    result = bsd_handler.get_memory_facts(module)
    assert 'memtotal_mb' in result and 'memfree_mb' in result and 'swaptotal_mb' in result and 'swapfree_mb' in result


# Generated at 2022-06-13 00:46:10.050222
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    hardware = FreeBSDHardware({})
    assert hardware.get_device_facts() == {'devices': {}}

# Generated at 2022-06-13 00:46:12.524968
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hardware = FreeBSDHardware()

    memory_facts = hardware.get_memory_facts()

    assert memory_facts['memfree_mb'] >= 981
    assert memory_facts['swapfree_mb'] >= 981

# Generated at 2022-06-13 00:46:16.480546
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    # Constructor test of class FreeBSDHardwareCollector
    freebsd_hw_collector = FreeBSDHardwareCollector()
    assert freebsd_hw_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 00:46:26.235076
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    import sys
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.common.collections import ImmutableDict

    FactsCollector = FactCollector(module=None,
                                   collector=FreeBSDHardwareCollector(module=None),
                                   cachedir=None,
                                   collector_classes=[FreeBSDHardwareCollector])
    collected_facts = FactsCollector.collect(module_facts=dict(),
                                             collected_facts=ImmutableDict(ansible_facts=dict(hardware=dict())))

    stdout = sys.stdout
    sys.stdout = open('/dev/tty', 'w')

# Generated at 2022-06-13 00:46:39.277289
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    fake_module = type('fake_module', (), {'run_command': lambda *a, **k: (0, b'\x00\x00\x00\x00\x00\x00\x01\xAA', '')})
    hardware = FreeBSDHardware(fake_module)
    uptime = hardware.get_uptime_facts()['uptime_seconds']
    assert uptime > 0

# Generated at 2022-06-13 00:46:49.586229
# Unit test for method get_cpu_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:46:56.947608
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    if os.uname().sysname != 'FreeBSD':
        return

    # Create a dummy module
    dummy_module = DummyModule()

    # Create a FreeBSDHardware object
    freebsd_hardware = FreeBSDHardware(dummy_module)

    # Test it
    uptime_facts = freebsd_hardware.get_uptime_facts()

    # Check the result
    assert uptime_facts
    assert 'uptime_seconds' in uptime_facts

    uptime_seconds = uptime_facts['uptime_seconds']
    assert uptime_seconds > 0



# Generated at 2022-06-13 00:47:02.658160
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=('', '', 0))
    fbsdhardware = FreeBSDHardware(module)
    memory_facts = fbsdhardware.get_memory_facts()
    assert set(memory_facts.keys()) == set(['memfree_mb', 'memtotal_mb', 'swapfree_mb', 'swaptotal_mb'])

# Generated at 2022-06-13 00:47:05.681059
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware_collector = FreeBSDHardwareCollector()
    assert hardware_collector._fact_class == FreeBSDHardware
    assert hardware_collector._platform == 'FreeBSD'


# Generated at 2022-06-13 00:47:14.007340
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # kern.boottime is the amount of seconds since the epoch when the system
    # was booted. By default, sysctl returns an human readable string, which
    # is not suitable for computations, so we need to pass the option -b to
    # get the raw value.
    #
    # Example:
    #
    # $ sysctl -b kern.boottime
    # Fri Aug 25 11:44:32 2017  9314046715
    #
    # The raw value is a list of 16 bits, with the lower 32 bits of the boottime
    # and the higher 32 bits of the boottime. The whole list needs to be unpacked
    # using the right format, which is '@L' (see the Python documentation of
    # struct).

    fhw = FreeBSDHardware()
    # Mock the method run_command

# Generated at 2022-06-13 00:47:14.924741
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    my_obj = FreeBSDHardwareCollector()
    assert FreeBSDHardwareCollector == type(my_obj)

# Generated at 2022-06-13 00:47:25.822203
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils import basic
    sys = basic.AnsibleModule(argument_spec={})
    f = FreeBSDHardware(sys)

    # mock up a sysinfo structure
    class fake_sysinfo(object):
        def __init__(self, boot_time_seconds, boot_time_microseconds):
            self.boot_time_seconds = boot_time_seconds
            self.boot_time_microseconds = boot_time_microseconds

    # generate a fake time.time()
    time_now = time.time()
    # generate fake boot time: 30 seconds ago
    time_boot = time_now - 30
    # generate and return structure
    sysinfo = fake_sysinfo(int(time_boot), int((time_boot - int(time_boot)) * 1e6))

    # patch time.time and c

# Generated at 2022-06-13 00:47:34.590441
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = MockModule()

# Generated at 2022-06-13 00:47:38.863333
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    m = {'run_command.return_value': ('', '', 0)}
    facts = FreeBSDHardware(m)
    dmi_facts = facts.get_dmi_facts()

    assert isinstance(dmi_facts, dict)

    assert dmi_facts['system_vendor'] == 'NA'



# Generated at 2022-06-13 00:47:54.556762
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    module = FakeAnsibleModule()
    hardware_object = FreeBSDHardware(module)
    hardware_object.module.run_command = FakeRunCommand(output='hw.ncpu: 1')

    cpu_facts = hardware_object.get_cpu_facts()
    assert cpu_facts['processor_count'] == '1'



# Generated at 2022-06-13 00:47:59.564021
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    ''' test method get_memory_facts of class FreeBSDHardware'''
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    freebsd_hw = FreeBSDHardware(module)
    memory = freebsd_hw.get_memory_facts()
    assert memory['memfree_mb'] >= 0
    assert memory['memtotal_mb'] >= 0
    assert memory['swapfree_mb'] >= 0
    assert memory['swaptotal_mb'] >= 0


# Generated at 2022-06-13 00:48:08.799187
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts import ModuleFacts
    module = ModuleFacts()
    module.register_platform_subclass(FreeBSDHardware, 'FreeBSD')
    hw = FreeBSDHardware(module)

    with open('/proc/meminfo', 'r') as f:
        total_mem = int(f.readline().split()[1]) / 1024
        free_mem = int(f.readline().split()[1]) / 1024
    with open('/proc/swaps', 'r') as f:
        total_swap = int(re.split(r'\s+', f.readlines()[1])[2]) / 1024
        free_swap = int(re.split(r'\s+', f.readlines()[1])[3]) / 1024

    memory_facts = hw.get

# Generated at 2022-06-13 00:48:18.943527
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    ''' Test FreeBSDHardware.get_cpu_facts
    '''

    class TestModule(object):
        def __init__(self, rc, out, err, bin_path):
            self.rc = rc
            self.out = out
            self.err = err
            self.bin_path_rcs = {'sysctl': rc}
            self.bin_paths = {'sysctl': bin_path}

        def get_bin_path(self, name, opt_dirs=[]):
            '''fake get_bin_path which returns the pathname of a binary, if
            the binary was found in the expected location.  Otherwise, return
            None.
            '''
            try:
                if self.bin_path_rcs[name] < 0:
                    return None
            except KeyError:
                pass
           

# Generated at 2022-06-13 00:48:24.427284
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    def fake_run_command(module, cmd, encoding=None):
        return (0, struct.pack('@L', 61839), '')

    hardware = FreeBSDHardware(module=MockModule())
    hardware.module.run_command = fake_run_command
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts == {
        'uptime_seconds': int(time.time()) - 61839,
    }



# Generated at 2022-06-13 00:48:35.611531
# Unit test for method get_memory_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:48:45.513656
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:48:59.117251
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    """Unit test"""
    import io

    class ModuleMock(object):
        def __init__(self, *args, **kwargs):
            self.run_command_args = args
            self.run_command_kwargs = kwargs
            self.rc = 0
            self.encoding = None

        def run_command(self, *args, **kwargs):
            self.run_command_args = args
            self.run_command_kwargs = kwargs
            return [self.rc, self.out, self.err]

        def get_bin_path(self, *args, **kwargs):
            return '/bin/true'


# Generated at 2022-06-13 00:49:07.217417
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # create testmodule
    import ansible.module_utils.facts.hardware.freebsd
    testmodule = ansible.module_utils.facts.hardware.freebsd

    # create testclass
    class TestClass():
        def __init__(self, rc=0, out='', err=''):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, arg):
            return 'Path to ' + arg

    # create testobj
    testobj = TestClass()
    testobj.module = TestClass()
    testobj.module.run_command = TestClass

    # set testdata
    testobj.module.run_command.rc = 0
    testobj.module.run_command.out = 'hw.ncpu: 2'

    #

# Generated at 2022-06-13 00:49:15.975811
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """ Tests the method populate of class FreeBSDHardware.

    1. Initially test the return of the method populate with an empty class.
    2. Test the return of the method populate when the class has previously
        collected facts.
    3. Test the return of the method populate with an unknown device.
    """

    # Test case 1: Initially test the return of the method populate with an
    # empty class.
    # Expected results:
    #     {'processor_cores': 4,
    #     'processor_count': 1,
    #     'memtotal_mb': 7959,
    #     'swaptotal_mb': 0,
    #     'swapfree_mb': 0,
    #     'uptime_seconds': 694762,
    #     'memfree_mb': 314,
    #     'system_vendor': 'NA

# Generated at 2022-06-13 00:49:30.467980
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    from ansible.module_utils.facts import Collector
    facts_list = Collector.collect(['hardware'], gather_subset='all', module=None)
    for k, v in facts_list.items():
        assert isinstance(v, dict)
        assert isinstance(v['hardware'], dict)
        assert v['hardware']['platform'] == 'FreeBSD'

# Generated at 2022-06-13 00:49:32.741325
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    facts_collector = FreeBSDHardwareCollector()
    assert facts_collector.__class__.__name__ == 'HardwareCollector'

# Generated at 2022-06-13 00:49:37.481417
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware_collector = FreeBSDHardwareCollector()
    assert isinstance(hardware_collector, HardwareCollector)
    assert hardware_collector.platform == 'FreeBSD'
    assert hardware_collector.fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:49:43.245768
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    test_object = FreeBSDHardware()

    def mock_run_command(args, check_rc=False, encoding=None):
        # We don't really test the value of the timestamp, but at least
        # make sure we are decoding the right number of bytes.
        assert args == ['/sbin/sysctl', '-b', 'kern.boottime']
        assert encoding is None
        return 0, '\x01' * 8, ''

    test_object.module.run_command = mock_run_command

    assert test_object.get_uptime_facts() == {'uptime_seconds': 1}

# Generated at 2022-06-13 00:49:53.764155
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:50:01.223216
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)

    rc, out, err = module.run_command("/sbin/sysctl -n vm.stats.vm.v_page_size")
    pagesize = int(out.strip())
    rc, out, err = module.run_command("/sbin/sysctl -n vm.stats.vm.v_page_count")
    pagecount = int(out.strip())
    rc, out, err = module.run_command("/sbin/sysctl -n vm.stats.vm.v_free_count")
    freecount = int(out.strip())
    rc, out, err = module.run_command("/sbin/swapinfo -k")
    lines = out.splitlines()

# Generated at 2022-06-13 00:50:11.539432
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class MockModule:
        def __init__(self, module):
            self.module = module
        def get_bin_path(self, cmd):
            return cmd
        def run_command(self, cmd, check_rc=None, encoding=None):
            return self.module.run_command(cmd, check_rc, encoding)

    class MockAnsibleModule:
        def __init__(self, module_args, initialize_with_dmesg_boot_out=True):
            self.params = module_args
            self.result = dict(changed=False, dmesg_boot='')

# Generated at 2022-06-13 00:50:14.900745
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    fhw = FreeBSDHardware(None)
    cpu_facts = fhw.get_cpu_facts()

    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts


# Generated at 2022-06-13 00:50:19.923634
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class TestModule(object):
        def get_bin_path(self, arg):
            if arg == 'dmidecode':
                return '/usr/sbin/dmidecode'
            return None

        def run_command(self, arg, encoding=None):
            o = 'Handle 0x0000, DMI type 0, 24 bytes\n'\
                'BIOS Information\n'\
                '\tVendor: Google\n'\
                '\tVersion: Google\n'\
                '\tRelease Date: Fri Jul 24 10:49:55 2015\n'\
                '\tAddress: 0xE0000\n' \
                '\tRuntime Size: 128 kB\n'\
                '\tROM Size: 2560 kB'
            return 0, o, None


# Generated at 2022-06-13 00:50:27.557332
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """get_memory_facts() returns memory statistics"""

    # We definitely need a cls instance to call get_memory_facts()
    from ansible.plugins.module_utils.facts import kernel
    class Foo:
        # Mock some needed attributes
        module = kernel.AnsibleModule(argument_spec={})
        module.get_bin_path = lambda x: '/sbin/sysctl'
        module.run_command = lambda x, encoding=None: (0, 'vm.stats.vm.v_page_size: 4096\nvm.stats.vm.v_page_count: 624448\nvm.stats.vm.v_free_count: 623592', '')

    cls = Foo
    facts = FreeBSDHardware(cls).get_memory_facts()
    assert facts['memtotal_mb'] == 1536
   

# Generated at 2022-06-13 00:50:41.437277
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'data', ''))
    hardware_data = FreeBSDHardware(module)
    hardware_data.get_dmi_facts()
    assert module.run_command.called

# Generated at 2022-06-13 00:50:47.609267
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    current_time = int(time.time())
    boot_time = current_time - 123
    raw_boot_time = struct.pack('@L', boot_time)

    # Read the command output.
    def open_file(filename, mode='r'):
        if mode == 'rb':
            return raw_boot_time
        raise IOError

    hardware_facts = FreeBSDHardware()
    hardware_facts.module.get_bin_path = lambda x: x
    hardware_facts.module.run_command = lambda x, check_rc=True, encoding=None: (0, open_file(x, mode='rb'), None)

    assert hardware_facts.get_uptime_facts() == {
        'uptime_seconds': current_time - boot_time,
    }

# Generated at 2022-06-13 00:50:54.121166
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    class fake_module(object):
        def run_command(self, command):
            if command == "/usr/sbin/sysctl -n hw.physmem":
                return (0, "12345678910\n", None)
        def get_bin_path(self, command):
            if command == "sysctl":
                return "/usr/sbin/sysctl"

    m = fake_module()
    h = FreeBSDHardware(m)
    h.get_memory_facts()
    assert h.facts.get('memtotal_mb') == 116465

# Generated at 2022-06-13 00:50:57.599929
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict(filter=dict(required=False, type='str')))
    fshw = FreeBSDHardware(module)
    facts = fshw.get_memory_facts()
    assert facts['memtotal_mb'] > 0

# Generated at 2022-06-13 00:51:07.958131
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """
    Unit test for method get_memory_facts of class FreeBSDHardware
    """

# Generated at 2022-06-13 00:51:16.482575
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware_obj = FreeBSDHardware(module)
    memory_facts = hardware_obj.get_memory_facts()
    assert (isinstance(memory_facts, dict)) and memory_facts
    assert 'memtotal_mb' in memory_facts
    assert isinstance(memory_facts['memtotal_mb'], int)
    assert 'memfree_mb' in memory_facts
    assert isinstance(memory_facts['memfree_mb'], int)
    assert 'swaptotal_mb' in memory_facts
    assert isinstance(memory_facts['swaptotal_mb'], int)
    assert 'swapfree_mb' in memory_facts
    assert isinstance(memory_facts['swapfree_mb'], int)


# Generated at 2022-06-13 00:51:21.561277
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec={})
    facts = FreeBSDHardware(test_module).populate()
    assert 'processor_count' in facts
    assert 'processors' in facts
    assert 'processor_cores' in facts
    assert isinstance(facts['processors'], list)
    assert isinstance(facts['processor_count'], int)
    assert isinstance(facts['processor_cores'], int)



# Generated at 2022-06-13 00:51:23.294279
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    my_FreeBSDHardware = FreeBSDHardware()
    my_FreeBSDHardware.populate()


if __name__ == '__main__':
    test_FreeBSDHardware_populate()

# Generated at 2022-06-13 00:51:25.145591
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    fhw = FreeBSDHardware()
    dmi = fhw.get_dmi_facts()
    assert isinstance(dmi, dict), "get_dmi_facts returned %s instead of a dict" % dmi

# Generated at 2022-06-13 00:51:28.547595
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    h = FreeBSDHardware(dict(module=dict(run_command=run_command)))
    assert h.get_device_facts() == {'devices': {'ada0': ['ada0s1a', 'ada0s1b', 'ada0s2']}}


# set of facts as returned by FreeBSDHardware.get_device_facts()
devices = {'devices': {'ada0': ['ada0s1a', 'ada0s1b', 'ada0s2']}}

# stub for module.run_command

# Generated at 2022-06-13 00:51:56.493219
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    test_class = FreeBSDHardware()
    test_class._module = None
    test_class.module = None
    test_class._timeout = 1
    chk_cmd = 'sysctl hw.bios.date hw.bios.vendor hw.bios.version hw.machine hw.model hw.ncpu'
    (rc, out, err) = test_class.module.run_command(chk_cmd)

# Generated at 2022-06-13 00:52:01.942021
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = MockModule()
    hardware = FreeBSDHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert len(cpu_facts) == 5
    assert cpu_facts['processor'] == ["AMD64"]
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_count'] == 2



# Generated at 2022-06-13 00:52:06.138370
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """
    Test the constructor of the class FreeBSDHardwareCollector
    """
    module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=['!all'], type='list')
    ))
    result = {}
    try:
        result['ansible_facts'] = FreeBSDHardwareCollector(
            module=module,
            facts={'ansible_system': 'FreeBSD'}
        ).collect()
        result['changed'] = False
    except Exception as e:
        result['msg'] = str(e)
        result['failed'] = True
    return result


# Generated at 2022-06-13 00:52:11.075538
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    import sys
    sys.path.append('../../lib/')
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.system.freebsd import FreeBSDHardware

    module = ModuleFacts(
        dict(ANSIBLE_MODULE_ARGS={'gather_subset': 'all', 'gather_timeout': 10}))
    hardware = FreeBSDHardware(module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts.get('memfree_mb', 'NA') != 'NA'
    assert memory_facts.get('swapfree_mb', 'NA') != 'NA'
    assert memory_facts.get('swaptotal_mb', 'NA') != 'NA'

# Generated at 2022-06-13 00:52:20.095106
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    import platform
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware()
    sysctl = hardware.module.get_bin_path('sysctl')
    hardware.module.run_command = lambda x, check_rc=True: get_test_data(x)
    if platform.system() == 'FreeBSD':
        data = hardware.get_memory_facts()
        assert data['memtotal_mb'] == 1024
        assert data['memfree_mb'] == 512
        assert data['swaptotal_mb'] == 2048
        assert data['swapfree_mb'] == 1024
    elif sysctl:
        data = hardware.get_memory_facts()
        assert data['memtotal_mb'] in [2048, 4096]

# Generated at 2022-06-13 00:52:29.060138
# Unit test for method get_memory_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:52:33.397297
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import pytest
    import sys
    sys.path.append('../plugins/')

    # dmidecode is not available on all Linux distributions
    # Skip this test when the command is not present.
    dmidecode = '/usr/sbin/dmidecode'
    if not os.path.exists(dmidecode):
        pytest.skip('dmidecode not installed')

    x = FreeBSDHardware()
    dmi_facts = x.get_dmi_facts()
    assert dmi_facts == {} or 'system_vendor' in dmi_facts

# Generated at 2022-06-13 00:52:42.521312
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError
    from ansible.module_utils._text import to_bytes

    class FakeModule:
        class FakeRunCommand:
            def __init__(self):
                self.cmd = []
                self.rc = None
                self.out = None
                self.err = None

            def __call__(self, cmd, encoding=None):
                self.cmd = cmd
                return (self.rc, self.out, self.err)

        def __init__(self):
            self.run_command = self.FakeRunCommand()
            self.get_bin_path = lambda x: x

    fake_module = FakeModule()


# Generated at 2022-06-13 00:52:50.426542
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """Unit tests FreeBSDHardware.get_cpu_facts()"""

    module = AnsibleModule(
        argument_spec = dict()
    )

    test_obj = FreeBSDHardware(module)
    test_obj.populate()

    assert test_obj.cpu_facts['processor'][0].startswith('Intel(R)')
    assert 'i386' not in test_obj.cpu_facts['processor'][0]
    assert test_obj.cpu_facts['processor_cores'] == '1'
    assert test_obj.cpu_facts['processor_count'] == '1'


# Generated at 2022-06-13 00:53:00.054609
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import time
    import sys

    sys.modules['ansible.module_utils.facts.timeout'] = __import__('ansible.module_utils.facts.timeout', fromlist=['TimeoutError'])

    fact_class = FreeBSDHardware()

    # FIXME: this test is fragile in face of timezone changes and daylight saving time
    expected_result = {'uptime_seconds': int(time.time() - 1569756870)}
    result = fact_class.get_uptime_facts()
    assert result == expected_result


if __name__ == '__main__':
    test_FreeBSDHardware_get_uptime_facts()

# Generated at 2022-06-13 00:54:30.202538
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import doctest
    module = AnsibleModule(argument_spec={})
    facts = FreeBSDHardwareCollector(module).collect()[0]
    result = facts.get_dmi_facts()
    assert result


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 00:54:36.110348
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class ModuleTest:
        class RunCommand:
            def __init__(self):
                self.out = '4'

        def __init__(self):
            self.run_command = ModuleTest.RunCommand()
            self.get_bin_path = lambda x: x

    hw = FreeBSDHardware()
    hw.module = ModuleTest()

    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts['processor'] == ['CPU:', 'Intel(R) Core(TM) i3-3217U CPU', '  @ 1.80GHz']
    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor_cores'] == '2'


# Generated at 2022-06-13 00:54:43.082253
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # Create a dummy module
    module = type('AnsibleModule', (), dict(
        run_command=lambda *_, **__: (0, "", ""),
        get_bin_path=lambda *_: "",
    ))

    # Instanciate FreeBSDHardware
    facts = FreeBSDHardware(module)

    # Run FreeBSDHardware.populate()
    facts.populate()

    # check that all expected variables are set
    assert facts.data['uptime_seconds']
    assert facts.data['memtotal_mb']
    assert facts.data['memfree_mb']
    assert facts.data['swaptotal_mb']
    assert facts.data['swapfree_mb']
    assert facts.data['processor_cores']
    assert facts.data['processor_count']
    assert facts.data['devices']

# Generated at 2022-06-13 00:54:52.946254
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Create a test instance of AnsibleModule
    from ansible.utils.display import Display
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.processor.freebsd import _get_processor
    from ansible.module_utils.facts.system.freebsd import _get_uname_info
    display = Display()
    ansible_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        display=display,
    )

    # Create a instantiation of the FreeBSDHardware class with all its dependencies
    testinstance = FreeBSDHardware(ansible_module)

    # Set values of required dependencies


# Generated at 2022-06-13 00:54:55.021083
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    '''
    Make sure that instance of FreeBSDHardwareCollector can be created
    '''
    FreeBSDHardwareCollector()

# Generated at 2022-06-13 00:55:01.082414
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FakeModule:
        @staticmethod
        def run_command(cmd, encoding=None):
            if cmd == ['/sbin/sysctl', '-b', 'kern.boottime']:
                time_b = str(int(time.time()))
                return 0, time_b.encode('utf-8'), ''
            return 0, b'', ''

        @staticmethod
        def get_bin_path(name):
            return name

    f = FreeBSDHardware(FakeModule())
    assert 'uptime_seconds' in f.get_uptime_facts()

# Generated at 2022-06-13 00:55:03.282798
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    # Test to see if module properly implements FreeBSDHardwareCollector.
    fact_collector = FreeBSDHardwareCollector()
    assert isinstance(fact_collector, HardwareCollector)


# Generated at 2022-06-13 00:55:07.360320
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    hardware = FreeBSDHardware(module)
    result = dict(changed=False)
    result['ansible_facts'] = dict(hardware=hardware.populate())
    module.exit_json(**result)

