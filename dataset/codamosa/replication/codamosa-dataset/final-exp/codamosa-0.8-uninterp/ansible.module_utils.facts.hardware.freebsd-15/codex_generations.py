

# Generated at 2022-06-13 00:45:35.331817
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # create an instance of FreeBSDHardware.
    # FreeBSDHardware defines sysctl method.
    # Initialize the arguments of sysctl method
    args = dict(rc=0, out='vm.stats.vm.v_page_count: 8388608\nvm.stats.vm.v_page_size: 4096\nvm.stats.vm.v_page_free: 541070\nvm.stats.vm.v_page_zero_count: 23388\nvm.stats.vm.v_page_active_count: 484498\nvm.stats.vm.v_page_inactive_count: 1533580\n', err='')
    # mock the sysctl method of FreeBSDHardware class
    def sysctl(self):
        return args['rc'], args['out'], args['err']
    # create an instance of Facts class

# Generated at 2022-06-13 00:45:47.979679
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """
    Unit test for method get_dmi_facts of class FreeBSDHardware
    """
    module = AnsibleModule(argument_spec={})


# Generated at 2022-06-13 00:45:50.132580
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    m = FreeBSDHardware({})
    assert isinstance(m.get_memory_facts(), dict)



# Generated at 2022-06-13 00:45:55.456163
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    facts = hardware.populate()
    assert isinstance(facts['dev'], list)
    assert isinstance(facts['devices'], dict)
    assert isinstance(facts['uptime_seconds'], int)
    assert isinstance(facts['uptime_hours'], int)

# Generated at 2022-06-13 00:45:58.027924
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = None
    collector = FreeBSDHardwareCollector(module)
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDHardware



# Generated at 2022-06-13 00:45:59.049087
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    FreeBSDHardwareCollector()

# Generated at 2022-06-13 00:46:05.623459
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = AnsibleModuleMock(params=dict())
    device_facts = {}
    expected_device_facts = {'devices': {'da0': ['da0s1a']}}

    def isdir_mock(x):
        if x == '/dev':
            return True
        return False

    def listdir_mock(x):
        return ['da0', 'da0s1a']

    def match_mock(x, y):
        if y == r'(ada?\d+|da\d+|a?cd\d+)':
            return True
        return False

    module.get_bin_path = get_bin_path_mock
    module.run_command = run_command_mock
    module.register_ansible_module_argument = register_ansible_module_argument_mock

# Generated at 2022-06-13 00:46:13.434014
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Set up a test module and a FreeBSDHardware class instance to be tested
    module = type('', (), {})
    module.get_bin_path = lambda s, x: '/usr/bin/sysctl'
    module.run_command = lambda s, x: (0, 'hw.pagesize = 4096\nhw.physmem = 6333441536\nvm.stats.vm.v_free_count = 30207', '')
    freebsd_hw = FreeBSDHardware(module)

    # Get memory facts
    facts = freebsd_hw.get_memory_facts()

    assert facts['memtotal_mb'] == 6072
    assert facts['memfree_mb'] == 1177


# Generated at 2022-06-13 00:46:17.202994
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # Initialize FreeBSDHardware class instance
    freebsd_hardware = FreeBSDHardware(None)
    # Get cpu facts for FreeBSD system
    # cpu_facts is a dictionary
    cpu_facts = freebsd_hardware.get_cpu_facts()

    # Required keys for cpu facts dictionary
    keys = ['processor_cores', 'processor_count']

    # If cpu facts is a dictionary and it contains all the required keys,
    # the method get_cpu_facts is working as expected.
    assert isinstance(cpu_facts, dict)
    assert set(keys).issubset(cpu_facts)



# Generated at 2022-06-13 00:46:25.529327
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    m = FreeBSDHardware(module=None)
    dmi_facts = m.get_dmi_facts()
    assert(dmi_facts['system_vendor'])
    assert(dmi_facts['product_name'])
    assert(dmi_facts['product_serial'])
    assert(dmi_facts['product_uuid'])
    assert(dmi_facts['product_version'])
    assert(dmi_facts['bios_vendor'])
    assert(dmi_facts['bios_version'])
    assert(dmi_facts['board_vendor'])
    assert(dmi_facts['board_name'])



# Generated at 2022-06-13 00:46:39.091470
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc._fact_class == FreeBSDHardware
    assert fhc._platform == 'FreeBSD'

# Generated at 2022-06-13 00:46:42.847978
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert FreeBSDHardwareCollector._platform == 'FreeBSD'
    assert FreeBSDHardwareCollector._fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:46:47.849427
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    class FakeModule:
        def __init__(self):
            self.run_command = lambda *args, **kwargs: (0, 'sysctl: unknown oid \'vm.stats.vm.v_page_size\'', '')
            self.get_bin_path = lambda *args, **kwargs: '/sbin/sysctl',

    module = FakeModule()
    hardware = FreeBSDHardware(module)
    hardware.populate()

# Generated at 2022-06-13 00:46:50.071475
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    bhc = FreeBSDHardwareCollector()
    assert bhc._fact_class == FreeBSDHardware
    assert bhc._platform == 'FreeBSD'

# Generated at 2022-06-13 00:47:00.140127
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = collections.namedtuple("Module", "run_command get_bin_path")
    run_cmd = collections.namedtuple("run_command", "stdout")

# Generated at 2022-06-13 00:47:07.475323
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec=dict())
    module.params = dict()

    module.get_bin_path = MagicMock(return_value='/usr/sbin/dmidecode')

    fbsd_hw = FreeBSDHardware(module)
    dmi_facts = fbsd_hw.get_dmi_facts()

    assert 'bios_date' in dmi_facts
    assert 'bios_vendor' in dmi_facts
    assert 'system_vendor' in dmi_facts


# Generated at 2022-06-13 00:47:16.143539
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # Test environment:
    # - test cpu: Intel(R) Core(TM) i5-5250U CPU @ 1.60GHz
    # - dmesg.boot
    # CPU: Intel(R) Core(TM) i5-5250U CPU @ 1.60GHz (1594.97-MHz K8-class CPU)
    #   Origin="GenuineIntel"  Id=0x406c3  Family=0x6  Model=0x3c  Stepping=3
    #   Features=0xbfebfbff  Features2=0x7fbae3ff
    #   AMD Features=0x2c100000  AMD Features2=0x21<SYSCALL,NX,Page1GB>

    # Create an instance of class FreeBSDHardware
    hardware = FreeBSDHardware()
    hardware.module = MagicMock()



# Generated at 2022-06-13 00:47:28.228804
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Create a FreeBSDHardware object
    hardware = FreeBSDHardware()

    # Mock the module, the module run_command function and struct.unpack function
    import ansible.module_utils.facts.hardware.freebsd
    ansible.module_utils.facts.hardware.freebsd.struct = type("", (object,), {"unpack": lambda x, y: (42,)})
    hardware.module = type("", (object,), {"run_command": lambda x, check_rc=None, encoding=None: (0, struct.pack("@L", 1337), "")})

    # Assert the returned values
    facts = hardware.get_uptime_facts()
    assert "uptime_seconds" in facts
    assert isinstance(facts["uptime_seconds"], int)
    assert facts["uptime_seconds"] == 42

# Generated at 2022-06-13 00:47:33.764942
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.facts.collector import TestModuleCollector

    def run_module():
        module_args = dict(gather_subset='all')
        collected_facts = TestModuleCollector.run_module(module_args)
        return collected_facts.get('ansible_facts')

    facts = run_module()
    # Test that processor_count has been populated
    assert facts['ansible_processor_count'] == facts['ansible_processor_vcpus']

# Generated at 2022-06-13 00:47:35.328200
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    obj = FreeBSDHardwareCollector()
    assert obj is not None

# Generated at 2022-06-13 00:47:54.385807
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    kwargs = {
        'module': DummyModule,
    }
    freebsd_hardware = FreeBSDHardware(**kwargs)
    freebsd_hardware.populate()



# Generated at 2022-06-13 00:48:01.308289
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''
    Unit test for method populate of class FreeBSDHardware
    '''
    from ansible.utils import context_objects as co
    from ansible.plugins.module_utils.facts.collector.freebsd import FreeBSDHardware

    # Create a module
    fake_module = co.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    # Create a FreeBSDHardware object
    freebsd_hardware_obj = FreeBSDHardware(fake_module)
    # Populate method of FreeBSDHardware object must return a dict
    assert isinstance(freebsd_hardware_obj.populate(), dict)

# Generated at 2022-06-13 00:48:07.850204
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Test for issue #28653
    # Memory facts are empty for FreeBSD with 512 MB memory
    # Free memory is 524288 kB
    m = FreeBSDHardware({}, {'PATH': '',
                             'ansible_memfree_mb': '512',
                             'ansible_memtotal_mb': '1024'})
    mem = m.get_memory_facts()

    assert 'memtotal_mb' in mem
    assert 'memfree_mb' in mem
    assert 'swaptotal_mb' in mem
    assert 'swapfree_mb' in mem

# Generated at 2022-06-13 00:48:14.567941
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """Test FreeBSDHardware.get_cpu_facts() method"""
    module = FakeAnsibleModule()
    hardware = FreeBSDHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert "processor_count" in cpu_facts
    assert cpu_facts['processor_count'] == "1"
    assert "processor" in cpu_facts
    assert len(cpu_facts['processor']) > 0
    assert "processor_cores" in cpu_facts
    assert "1" == cpu_facts['processor_cores']



# Generated at 2022-06-13 00:48:24.018476
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import platform

    # Create a dummy class to test the method.
    class MockModule(object):
        def __init__(self):
            self.PATH = '/p/a/t/h'
            self.run_command = run_command

        def get_bin_path(self, prog):
            return '/usr/bin/%s' % prog

    # Create a dummy function to get the command output
    def run_command(cmd, encoding=None, errors=None, check_rc=True):
        # Assert the command is what we expect
        if not cmd[0] == '/usr/bin/sysctl' or not cmd[1] == '-b' or not cmd[2] == 'kern.boottime':
            raise AssertionError("Unexpected command %r" % cmd)

        # Return a tuple of the raw bytes

# Generated at 2022-06-13 00:48:31.907948
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class Bunch:
        pass

    module = Bunch()
    module.run_command = run_command_test
    module.get_bin_path = get_bin_path_test

    hardware_facts = FreeBSDHardware(module)
    res = hardware_facts.get_cpu_facts()
    assert res['processor_count'] == '1'
    assert res['processor'] == ['Quad-Core AMD Opteron(tm) Processor 1389']



# Generated at 2022-06-13 00:48:32.404413
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    FreeBSDHardwareCollector()

# Generated at 2022-06-13 00:48:38.403821
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    test_module = get_test_module()
    hw = FreeBSDHardware(test_module)
    cpu_facts = hw.get_cpu_facts()

    assert isinstance(cpu_facts, dict)
    assert 'processor_count' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor' in cpu_facts
    assert isinstance(cpu_facts['processor'], list)


# Generated at 2022-06-13 00:48:46.857958
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """Test method get_dmi_facts of class FreeBSDHardware"""
    # pylint: disable=protected-access
    module = AnsibleModule(argument_spec={})
    module.params = {}
    hardware = FreeBSDHardware(module)

    # Redefine dmidecode callable
    from ansible.module_utils.facts.hardware.freebsd import dmidecode
    def fake_dmidecode(cmd):
        """Return fake output for dmidecode command"""
        val = FakeDmidecodeOutput.get(cmd)
        if val is not None:
            return 0, val, ''
        return 1, '', ''
    hardware.dmidecode = fake_dmidecode

    # Define fake dmidecode output

# Generated at 2022-06-13 00:49:00.049121
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """This will test the FreeBSDHardwareCollector class"""

    # Specify some constants that we know to exist on FreeBSD
    platform = 'FreeBSD'
    fact_class = 'FreeBSDHardware'
    # Now create an instance of FreeBSDHardwareCollector
    collector = FreeBSDHardwareCollector()
    # Assert that the instance is not None
    assert collector is not None
    # Assert that we got the right platform
    assert collector._platform == platform
    # Assert that we got the right class
    assert collector._fact_class == fact_class

if __name__ == '__main__':
    # Create an instance of FreeBSDHardwareCollector and get facts from it
    collector = FreeBSDHardwareCollector()
    facts_dict = collector.collect()
    # Print the resulting facts

# Generated at 2022-06-13 00:49:48.845539
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = MockModule()
    freebsd_hw = FreeBSDHardware(module)
    freebsd_hw.get_cpu_facts()
    assert freebsd_hw.module.run_command.call_args_list[0] == call([mock_bin_path, '-n', 'hw.ncpu'], check_rc=False)
    for line in mock_dmesg_boot.splitlines():
        if 'CPU:' in line:
            assert freebsd_hw.facts['processor'][0] == 'amd64'
        if 'Logical CPUs per core' in line:
            assert freebsd_hw.facts['processor_cores'] == '1'
    assert freebsd_hw.facts['processor_count'] == '2'


# Generated at 2022-06-13 00:49:58.370825
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """Check FreeBSDHardware.get_memory_facts()
    """
    import sys
    import os
    from ansible.module_utils.facts import Facts

    memtotal = 'MemTotal:        3899848 kB\n'
    memfree = 'MemFree:          638684 kB\n'
    swapfree = 'SwapFree:               0 kB\n'
    swapcached = 'SwapCached:            0 kB\n'

    # First we create a new Facts module with custom methods and
    # inject it into system path.
    # sys.modules dict is used by python to look up modules on import,
    # so we will insert our test module in there.

    def testrun_command(cmd, check_rc=False):
        if 'proc/meminfo' in cmd:
            return 0, memtotal + mem

# Generated at 2022-06-13 00:50:08.734809
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    import sys
    import tempfile
    import shutil

    sysdir = '/dev'
    if 'FREEBSD_HARDWARE_FAKE_DEVICE_DIR' in os.environ:
        sysdir = os.environ['FREEBSD_HARDWARE_FAKE_DEVICE_DIR']

    # test data is in $CWD/freebsd_hardware_test_data relative to this file
    this_file_path = os.path.abspath(__file__)
    test_data_path = os.path.join(os.path.dirname(this_file_path), 'freebsd_hardware_test_data')
    # read data from test data file
    test_data_file_name = 'test_FreeBSDHardware_get_device_facts.txt'
    devices = []

# Generated at 2022-06-13 00:50:10.863733
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    collector = FreeBSDHardwareCollector()
    assert FreeBSDHardwareCollector._fact_class == collector._fact_class
    assert FreeBSDHardwareCollector._platform == collector._platform

# Generated at 2022-06-13 00:50:11.770103
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    freebsd_hw = FreeBSDHardware({})
    return freebsd_hw.get_dmi_facts()

# Generated at 2022-06-13 00:50:19.160868
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    # set up module object to call methods from
    module.get_bin_path = lambda module: '/usr/bin/sysctl'
    module.run_command = lambda cmd: (0, 
        "hw.ncpu: 2\nhw.model: AMD Opteron(tm) Processor 4376\nhw.machine: amd64\nhw.cputype: 131072\n", 
        '')
    hardware = FreeBSDHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] is not None
    assert cpu_facts['processor_count'] == "2"
    assert cpu_facts['processor_cores'] is not None


# Generated at 2022-06-13 00:50:24.519807
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    dmidecode = '/bin/dmidecode'
    # Mock dmidecode binary detection
    module.get_bin_path = MagicMock(return_value=dmidecode)
    module.run_command = run_command_mock
    freebsdHardware = FreeBSDHardware()
    freebsdHardware.module = module
    fact_subset = dict((k, freebsdHardware.facts[k]) for k in [
        'devices',
        'processor',
        'processor_cores',
        'processor_count',
        'system_vendor',
    ])

# Generated at 2022-06-13 00:50:31.948046
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    kern_boottime = b'\x00\x00\x00\x00\x00\x00\x00\x00'

    struct_format = '@L'
    struct_size = struct.calcsize(struct_format)
    if len(kern_boottime) < struct_size:
        return

    (kern_boottime, ) = struct.unpack(struct_format, kern_boottime[:struct_size])

    fact_obj = FreeBSDHardware()
    uptime_facts = fact_obj.get_uptime_facts()
    assert 'uptime_seconds' in uptime_facts, 'uptime_seconds is not exist in uptime_facts'
    assert uptime_facts['uptime_seconds'] == int(time.time() - kern_boottime)

# Generated at 2022-06-13 00:50:34.017118
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware_collector = FreeBSDHardwareCollector()
    assert hardware_collector.platform == 'FreeBSD'

# Generated at 2022-06-13 00:50:43.003997
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """Tests FreeBSDHardware.get_cpu_facts()."""
    # Simulate the output of sysctl -n hw.ncpu
    mock_out = "8"
    def mock_run_command_one(*args, **kwargs):
        return (1, mock_out, "")
    # Simulate the output of dmesg

# Generated at 2022-06-13 00:52:15.394850
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    test_cases = [
        {
            'kern.boottime': b'\x00\x00\x00\xb4\x00\x00\x00\x00',
            'result': 176,
        },
        {
            'kern.boottime': b'\x00\x00\x03\x2f\x00\x00\x00\x00',
            'result': 1279,
        },
        {
            'kern.boottime': b'\x01\xd5\x71\x9d\x8e\x03\x00\x00',
            'result': 168433671,
        },
    ]
    for entry in test_cases:
        result = FreeBSDHardware(None).get_uptime_facts(entry['kern.boottime'])
       

# Generated at 2022-06-13 00:52:22.619012
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    custom_module_utils_path = os.path.join(module_utils_path, 'FreeBSD/hardware')
    for name in os.listdir(custom_module_utils_path):
        path = os.path.join(custom_module_utils_path, name)
        if os.path.isfile(path):
            module_name, ext = os.path.splitext(name)
            if ext == '.py' and module_name != "__init__":
                module = __import__('ansible.module_utils.facts.hardware.FreeBSD.hardware.' + module_name, fromlist=[''])
                load_class = getattr(module, module_name, None)
                if load_class is not None:
                    load_class()

    collector = FreeBSDHardwareCollector()
    assert collector._fact_

# Generated at 2022-06-13 00:52:27.916414
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    set_module_args(dict(gather_subset='!all,!min,!network'))
    FreeBSDHardwareCollector(module)
    f = FreeBSDHardware(module)

    dmi_facts = f.get_dmi_facts()
    for (k, v) in dmi_facts.items():
        assert len(v) > 0 and v != 'NA'

# Generated at 2022-06-13 00:52:33.991887
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Create a FreeBSDHardware object
    freebsd_hardware = FreeBSDHardware()

    # Create a fake dmidecode binary
    def fake_dmidecode(k):
        if k == 'system-product-name':
            return 'VirtualBox'
        if k == 'system-serial-number':
            return '0'
        if k == 'system-uuid':
            return 'foo'
        if k == 'system-version':
            return 'bar'
        if k == 'system-manufacturer':
            return 'innotek GmbH'
        if k == 'bios-release-date':
            return '01/01/2007'
        if k == 'bios-vendor':
            return 'innotek GmbH'
        if k == 'bios-version':
            return 'VirtualBox'
       

# Generated at 2022-06-13 00:52:42.451609
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import tempfile
    import shutil

    test_dir = tempfile.mkdtemp()
    f = open(os.path.join(test_dir, 'dmidecode'), 'w', 0o700)
    f.write('#!/bin/sh\necho \'system-manufacturer: To be filled by O.E.M.\nexit 0\'')
    f.close()

    module = FakeAnsibleModule({'ansible_system_vendor': 'NA'})
    hardware = FreeBSDHardware(module)
    dmi_facts = hardware.get_dmi_facts()

    shutil.rmtree(test_dir)

    assert dmi_facts['system_vendor'] == 'To be filled by O.E.M.'



# Generated at 2022-06-13 00:52:47.100692
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModuleMock()
    module.params = {}
    module.run_command = AnsibleModuleMock.run_command
    fb = FreeBSDHardware()
    fb.module = module
    result = fb.get_dmi_facts()
    assert isinstance(result, dict)



# Generated at 2022-06-13 00:52:52.361684
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module=module)
    hardware.populate()
    assert hardware.data['uptime_seconds']
    assert hardware.data['devices']
    assert hardware.data['devices']['ada0']
    assert hardware.data['devices']['ada0'][0] == 'ada0s1'
    assert hardware.data['devices']['ada0'][1] == 'ada0s2'


# Generated at 2022-06-13 00:52:55.169050
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = MagicMock()
    hardware = FreeBSDHardware(module=module)
    hardware.get_device_facts()
    assert module.run_command.called
    assert hardware.devices

# Generated at 2022-06-13 00:53:04.307855
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import stat
    import mock
    import platform
    import sys

    # Define some dummy methods
    def dummy_run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=True, path_prefix=None, cwd=None, raise_err=True, environ_update=None, umask=None, encoding=None):
        return 0, '', ''

    def dummy_get_bin_path(self, arg, opt_dirs=[]):
        return '/usr/local/bin/dmidecode'

    def dummy_read_file(path, default=None):
        if path == '/usr/local/bin/dmidecode':
            return True
        return False

    # Mock the module.run_command, module.get_bin_path and os

# Generated at 2022-06-13 00:53:12.206540
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModuleMock()
    hw = FreeBSDHardware(module)
    hw.module.run_command.return_value = (0, 'kern.boottime: { sec = 1600696036, usec = 756028 }\n', '')
    assert hw.get_uptime_facts() == {'uptime_seconds': 1600696036}

    hw.module.run_command.return_value = (0, 'kern.boottime: { sec = 1600696036, usec = 756028 }', '')
    assert hw.get_uptime_facts() == {'uptime_seconds': 1600696036}

    # Now check for a proper error
    hw.module.run_command.return_value = (0, '/dev/ada0p3', None)