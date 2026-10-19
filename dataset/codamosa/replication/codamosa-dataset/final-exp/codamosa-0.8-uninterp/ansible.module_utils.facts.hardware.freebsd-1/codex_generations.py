

# Generated at 2022-06-13 00:45:32.433038
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """Test class FreeBSDHardwareCollector
    """
    hardware_collector = FreeBSDHardwareCollector()
    hardware_collector.collect()

    hardware = hardware_collector.get_facts()

    assert hardware['uptime_seconds'] > 0, 'Fail: uptime_seconds'
    assert hardware['memtotal_mb'] > 0, 'Fail: memtotal_mb'
    assert hardware['memfree_mb'] > 0, 'Fail: memfree_mb'
    assert hardware['swaptotal_mb'] > 0, 'Fail: swaptotal_mb'
    assert hardware['swapfree_mb'] > 0, 'Fail: swapfree_mb'
    assert hardware['processor_cores'] > 0, 'Fail: processor_cores'
    assert hardware['processor_count'] > 0, 'Fail: processor_count'

# Generated at 2022-06-13 00:45:39.241680
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''
    FreeBSDHardware class unit test for method populate.
    '''
    class FreeBSDHardwareFakeModule:
        def __init__(self):
            pass

        def get_bin_path(self, name):
            if name == 'sysctl':
                return '/sbin/sysctl'
            elif name == 'swapinfo':
                return '/sbin/swapinfo'
            elif name == 'dmesg':
                return '/sbin/dmesg'
            else:
                return None

        def run_command(self, args, check_rc=False, encoding=None, data=None):
            if args == '/sbin/sysctl -n hw.ncpu':
                return (0, '8\n', '')

# Generated at 2022-06-13 00:45:44.447509
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert FreeBSDHardwareCollector._platform == 'FreeBSD'
    assert fhc._platform == 'FreeBSD'
    assert fhc.get_platform() == 'FreeBSD'


# Generated at 2022-06-13 00:45:50.498345
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FakeModule(object):
        def get_bin_path(self, path):
            return 'sysctl'

        def run_command(self, cmd, encoding=None, check_rc=True, executable=None, data=None):
            return 0, os.urandom(8), None

    hardware = FreeBSDHardware(FakeModule())
    facts = hardware.get_uptime_facts()

    assert facts['uptime_seconds'] > 0

# Generated at 2022-06-13 00:46:00.559611
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
        )


# Generated at 2022-06-13 00:46:03.775951
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hc = FreeBSDHardwareCollector()
    assert isinstance(hc, HardwareCollector)
    assert isinstance(hc._fact_class, FreeBSDHardware)


# Generated at 2022-06-13 00:46:10.915061
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    test_module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(type='list', default=['all'])
        }
    )
    result = FreeBSDHardware(test_module).populate()
    assert result['ansible_processor_cores'] == '1'
    assert result['ansible_memory_mb']['real']['total'] > 0
    assert result['devices']['da0'] == []
    assert result['ansible_uptime_seconds'] > 0
    assert result['ansible_system_vendor'] == 'NA'

# Generated at 2022-06-13 00:46:21.943240
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = type('module', (object,), {})()
    module.run_command = lambda x: (0, "vm.stats.vm.v_page_size: 8192\nvm.stats.vm.v_page_count: 524288\nvm.stats.vm.v_free_count: 27244", None)
    module.get_bin_path = lambda x: "/sbin/sysctl"
    fb = FreeBSDHardware(module)

    expected_memtotal = 524288 * 8192 // 1024 // 1024
    expected_memfree = 27244 * 8192 // 1024 // 1024

    m = fb.get_memory_facts()
    assert m['memtotal_mb'] == expected_memtotal
    assert m['memfree_mb'] == expected_memfree


# Generated at 2022-06-13 00:46:29.183486
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """
    This unit test is used to check the method get_dmi_facts from class FreeBSDHardware
    """
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    class module(object):
        def __init__(self):
            self.run_command_environ_update = None
            self.run_command_tmpdir = None
        def get_bin_path(self, path, opt_dirs=[]):
            return '/test'
    class TestFreeBSDHardware(FreeBSDHardware):
        def __init__(self, module):
            self.module = module
    import json
    test_module = module()
    test_instance = TestFreeBSDHardware(test_module)

    # Test case value
    test_module.run_command_rc = 0
    test_module.run_

# Generated at 2022-06-13 00:46:38.050318
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    ''' test for get_memory_facts method of class FreeBSDHardware '''
    from ansible.module_utils import facts
    from ansible.module_utils.facts.collector.freebsd import FreeBSDHardware
    import os

    # Initialize the freebsd hardware object
    freebsd_hw_obj = FreeBSDHardware()

    # mock the sysctl command

# Generated at 2022-06-13 00:46:54.824858
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class AnsibleModuleMock():
        def __init__(self):
            self.run_command_args = []
        def get_bin_path(self, name):
            return name
        def run_command(self, cmd, encoding, check_rc=True):
            self.run_command_args.append(cmd)
            return 0, kern_boottime, ''

    kern_boottime = "vm.stats.vm.v_page_size: 0\nvm.stats.vm.v_page_count: 2\nvm.stats.vm.v_free_count: 0\n"
    hw = FreeBSDHardware(AnsibleModuleMock())
    hw._get_mount_facts = lambda: 0
    facts = hw.populate()
    assert facts['memtotal_mb'] == 0

# Generated at 2022-06-13 00:46:58.847713
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    # The FreeBSDHardwareCollector can be instantiated
    hw_collector = FreeBSDHardwareCollector()
    assert isinstance(hw_collector, HardwareCollector)
    assert hw_collector.platform == 'FreeBSD'
    assert hw_collector._fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:47:05.818845
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module_name = 'ansible.module_utils.facts.hardware.freebsd'
    module = __import__(module_name, fromlist=['ansible', 'module_utils', 'facts', 'hardware'])
    inst = module.FreeBSDHardware()
    inst.module = Mock()
    sysdir = '/dev'
    drives = re.compile(r'(ada?\d+|da\d+|a?cd\d+)')
    slices = re.compile(r'(ada?\d+s\d+\w*|da\d+s\d+\w*)')
    if os.path.isdir(sysdir):
        dirlist = sorted(os.listdir(sysdir))
        for device in dirlist:
            d = drives.match(device)

# Generated at 2022-06-13 00:47:11.546902
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module=module)
    result = hardware.get_cpu_facts()

    assert type(result) == dict
    assert result['processor_count'] == 2
    assert result['processor'] == ['Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz', 'Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz']
    assert result['processor_cores'] == 2

# Generated at 2022-06-13 00:47:16.474952
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():

    class FakeModule(object):
        @staticmethod
        def run_command(cmd, check_rc=False, encoding=None):
            if '/sbin/sysctl -n hw.ncpu' in cmd:
                return 0, b'8\n', None

# Generated at 2022-06-13 00:47:19.210090
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    x = FreeBSDHardwareCollector()
    assert x.platform == 'FreeBSD'

# Generated at 2022-06-13 00:47:29.956298
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class MockModule:
        def __init__(self, out, rc):
            self.out = out
            self.rc = rc

        def get_bin_path(self, _):
            return '/bin/false'

        def run_command(self, _, encoding=None):
            return self.rc, self.out, None

    # Check that we return uptime_seconds
    # when sysctl(8) returns a valid boottime value.
    boottime_seconds = 100
    boottime_microseconds = 200000

    out = struct.pack('@LL', boottime_seconds, boottime_microseconds)
    m = MockModule(out, 0)
    fhw = FreeBSDHardware(m)
    right_now = time.time()
    uptime_seconds = int(right_now - boottime_seconds)

# Generated at 2022-06-13 00:47:31.466293
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    x = FreeBSDHardwareCollector()
    assert x.platform == "FreeBSD"
    assert x.fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:47:40.653350
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = MockModule()
    obj = FreeBSDHardware(module)
    obj.populate()
    assert obj.facts['devices'] == {'ada0': ['ada0s1', 'ada0s2', 'ada0s3', 'ada0s4'],
                                    'ada1': ['ada1s1'],
                                    'cd0': []}
    assert obj.facts['system_vendor'] == 'FreeBSD'
    assert obj.facts['uptime_seconds'] > 0
    assert 'mounts' in obj.facts
    # Check that the list of mounts is non-empty.
    assert len(obj.facts['mounts']) > 0
    # We may not have found swapinfo if the system hasn't been booted yet.
    assert 'swaptotal_mb' in obj.facts or 'swapfree_mb' in obj

# Generated at 2022-06-13 00:47:43.163937
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    ''' Return _fact_class instantiated from _platform '''
    return FreeBSDHardwareCollector().collect()[0]

# Generated at 2022-06-13 00:48:03.090756
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys
    module = sys.modules['ansible.module_utils.facts.hardware.freebsd']
    freebsdHardware = module.FreeBSDHardware()
    freebsdHardware.module = sys.modules['ansible.modules.system.setup']
    freebsdHardware.module.get_bin_path = lambda x: '/bin/dmidecode'

    dmi_facts = freebsdHardware.get_dmi_facts()
    assert dmi_facts['board_vendor'] != 'NA'
    assert dmi_facts['board_vendor'] != ''

# Generated at 2022-06-13 00:48:08.799797
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = DummyModule()
    freebsd_hardware = FreeBSDHardware(module)
    freebsd_hardware.module.run_command = run_command_success

    memory_facts = freebsd_hardware.get_memory_facts()

    assert memory_facts == {'memtotal_mb': 2000,
                            'memfree_mb': 1000,
                            'swaptotal_mb': 32768,
                            'swapfree_mb': 16384}



# Generated at 2022-06-13 00:48:18.943577
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Test data
    test_data = {
        'memtotal_mb': 732,
        'memfree_mb': 695,
        'swaptotal_mb': 732,
        'swapfree_mb': 731,
    }

    # Create instance of FreeBSDHardware
    freebsd_hw = FreeBSDHardware()

    # Populate module_utils
    freebsd_hw.module = MockModule()
    freebsd_hw.module.run_command.return_value = (0, '', '')
    freebsd_hw.module.get_bin_path.return_value = 'sysctl'

    # Create expected output

# Generated at 2022-06-13 00:48:27.988614
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

# Generated at 2022-06-13 00:48:37.051257
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

# Generated at 2022-06-13 00:48:46.057185
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class FakeModule:
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = []
            self.params['gather_timeout'] = 10

        def run_command(self, command):
            if command == '/usr/sbin/dmidecode -s bios-release-date':
                return 0, "12/01/2006", ""
            elif command == '/usr/sbin/dmidecode -s bios-vendor':
                return 0, "SEGA", ""
            elif command == '/usr/sbin/dmidecode -s bios-version':
                return 0, "01.00", ""
            elif command == '/usr/sbin/dmidecode -s baseboard-asset-tag':
                return 0, "None", ""

# Generated at 2022-06-13 00:48:58.463185
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Test for the function get_uptime_facts of class FreeBSDHardware
    # Test dmidecode facts
    # Test for constructor of class FreeBSDHardware
    m = FreeBSDHardware({})
    # Test for method get_uptime_facts of class FreeBSDHardware
    (rc, out, err) = m.module.run_command('sysctl -b kern.boottime')
    assert rc == 0
    (kern_boottime, ) = struct.unpack('@L', out[:struct.calcsize('@L')])
    uptime_facts = {'uptime_seconds': int(time.time() - kern_boottime)}
    assert m.get_uptime_facts() == uptime_facts

# Generated at 2022-06-13 00:49:07.908413
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = Mock()
    module.run_command.side_effect = [([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', ''),
                                      ([0], '\n', '')]

# Generated at 2022-06-13 00:49:17.294706
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class MockModule(object):
        def run_command(self, cmd, encoding=None):
            return (
                0,
                b'\x00\x00\x00\x00\x00\x00\x00\xf9\x7f\xd3\x02\x00',
                ''
            )

    class MockSystem(object):
        def __init__(self):
            self.system = 'FreeBSD'

    class MockArgs(object):
        def __init__(self):
            self.gather_subset = 'all'
            self.gather_timeout = 5

    hardware = FreeBSDHardware(MockModule(), MockSystem(), MockArgs())
    uptime_facts = hardware.get_uptime_facts()
    expected_uptime_facts = {'uptime_seconds': 123}

# Generated at 2022-06-13 00:49:22.098543
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = MockModule()
    get_dmi_facts = FreeBSDHardware(module)
    dmi_facts = get_dmi_facts.get_dmi_facts()

    if get_dmi_facts.module.get_bin_path('dmidecode'):
        for (k, v) in dmi_facts.items():
            assert v != "NA"
    else:
        for (k, v) in dmi_facts.items():
            assert v == "NA"



# Generated at 2022-06-13 00:49:57.803849
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    hardware_collector = FreeBSDHardwareCollector()
    hardware_facts = hardware_collector.collect()
    assert hardware_facts['devices'][hardware_facts['devices'].keys()[0]][0].startswith('ada') == True


# Generated at 2022-06-13 00:50:02.412804
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fake_module = MyFakeModule()
    hardware_collector = FreeBSDHardwareCollector(fake_module)
    assert hardware_collector._platform == 'FreeBSD'
    assert hardware_collector._fact_class == FreeBSDHardware
    assert hardware_collector._file_mapping == {}
    assert hardware_collector._excluded_files == []


# Generated at 2022-06-13 00:50:12.704598
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:50:20.214262
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = object()
    fbsd_hardware = FreeBSDHardware(module)

    class MockRunCommand:
        def __init__(self, out, rc):
            self.out = out
            self.rc = rc

        def __call__(self, cmd, encoding):
            assert encoding is None
            return self.rc, self.out, None

    class MockModule:
        def __init__(self, mock_run_command):
            self.run_command = mock_run_command
            self.get_bin_path = lambda x: '/usr/bin/' + x

        def fail_json(self, **args):
            raise RuntimeError(args['msg'])

    # Test: valid output
    expected_value = 123456

# Generated at 2022-06-13 00:50:27.606909
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fixture_data = [
        'hw.ncpu: 4',
        'hw.physmem: 8589934592',
    ]
    mock_cmd = MagicMock(return_value=('success', '\n'.join(fixture_data), ''))
    with patch.dict(HardwareCollector.__dict__, {'run_command': mock_cmd}):
        hw_facts = FreeBSDHardwareCollector(MagicMock())
        assert hasattr(hw_facts, 'get_all')
        assert hasattr(hw_facts, 'get_cpu')
        assert hasattr(hw_facts, 'get_memory')
        assert hw_facts._fact_class == FreeBSDHardware
        assert hw_facts._platform == 'FreeBSD'
        assert hw_facts.collect()

# Generated at 2022-06-13 00:50:36.963768
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    """
    Construct a FreeBSDHardware object and test its method get_cpu_facts()
    """
    # Construct an object
    if os.path.isfile("/var/run/dmesg.boot"):
        dmesg_boot_content = get_file_content("/var/run/dmesg.boot")
    else:
        dmesg_boot_content = get_file_content("/var/run/dmesg.boot.test")

    module = type('', (), {
        'run_command': (lambda self, args, check_rc=False, encoding=None: (0, dmesg_boot_content, '')),
        'get_bin_path': (lambda self, args, check_rc=False, encoding=None: "/sbin/sysctl")
    })
    module = module()

    free

# Generated at 2022-06-13 00:50:44.969593
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    fhw = FreeBSDHardware(dict())

    cpu_facts = fhw.get_cpu_facts()
    memory_facts = fhw.get_memory_facts()
    uptime_facts = fhw.get_uptime_facts()
    dmi_facts = fhw.get_dmi_facts()
    device_facts = fhw.get_device_facts()
    mount_facts = fhw.get_mount_facts()

    print('cpu_facts: {}'.format(cpu_facts))
    print('memory_facts: {}'.format(memory_facts))
    print('uptime_facts: {}'.format(uptime_facts))
    print('dmi_facts: {}'.format(dmi_facts))
    print('device_facts: {}'.format(device_facts))

# Generated at 2022-06-13 00:50:46.467106
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """Unit test for constructor of class FreeBSDHardwareCollector"""
    my_obj = FreeBSDHardwareCollector()
    param = my_obj._platform
    assert param == 'FreeBSD'

# Generated at 2022-06-13 00:50:51.258571
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware_collector = FreeBSDHardwareCollector()
    assert hardware_collector._platform == 'FreeBSD'
    assert hardware_collector._fact_class.platform == 'FreeBSD'


# Generated at 2022-06-13 00:50:58.275528
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    fhw = FreeBSDHardware()
    dmi_dict = fhw.get_dmi_facts()

    assert dmi_dict['system_vendor'] is not None
    assert dmi_dict['product_name'] is not None
    assert dmi_dict['product_serial'] is not None
    assert dmi_dict['product_version'] is not None
    assert dmi_dict['product_uuid'] is not None
    assert dmi_dict['board_vendor'] is not None
    assert dmi_dict['board_name'] is not None
    assert dmi_dict['board_serial'] is not None
    assert dmi_dict['board_asset_tag'] is not None
    assert dmi_dict['board_version'] is not None
    assert dmi_dict['bios_vendor'] is not None
   

# Generated at 2022-06-13 00:52:23.710874
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    """
    Test method get_device_facts of class FreeBSDHardware
    """

# Generated at 2022-06-13 00:52:30.916978
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class ModuleStub():
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, exe, opt_dirs=[], required=False):
            if exe == 'dmidecode':
                return '/usr/sbin/dmidecode'
            else:
                return ''

        def run_command(self, cmd, check_rc=True, encoding=None):
            if cmd[0:2] == '/u':
                rc = 0
            else:
                rc = 1
            return (rc, cmd, '')

    module = ModuleStub({})
    test_obj = FreeBSDHardware(module)
    result = test_obj.get_dmi_facts()
    assert result

# Generated at 2022-06-13 00:52:40.208760
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hw = FreeBSDHardware(module)

    # Test when only name of CPU are available
    module.run_command = MagicMock(return_value=(0, '0', ''))
    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts == {'processor_count': '0', 'processor': []}

    # Test when name and number of CPU are available
    module.run_command = MagicMock(return_value=(0, '2', ''))
    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts == {'processor_count': '2', 'processor': []}

    # Test when only name of CPU are available

# Generated at 2022-06-13 00:52:41.656437
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModuleMock()
    hardware = FreeBSDHardware(module)
    hardware.populate()

# Generated at 2022-06-13 00:52:51.745006
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class Module(object):
        def __init__(self):
            self.params = {}
            self.fail_json = lambda **args: None
            self.run_command = lambda cmd, **kwargs: (0, "vm.stats.vm.v_page_size: 16384\nvm.stats.vm.v_page_count: 383216\nvm.stats.vm.v_free_count: 41098\n", "")
            self.get_bin_path = lambda cmd: cmd

    class AnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.fail_json = lambda **args: None

# Generated at 2022-06-13 00:53:02.347255
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    result = {'failed': False}

    class MockModuleReturnError(object):
        rc = 1

        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            return self.rc, '', ''

    class MockModuleReturnData(object):
        rc = 0

        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            return self.rc, 'hw.ncpu: 2\n', ''

    class MockClass(object):
        module = MockModuleReturnError()

    hardware = FreeBSDHardware(module)
    hardware.module = MockModuleReturn

# Generated at 2022-06-13 00:53:03.822692
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hw = FreeBSDHardwareCollector()
    assert hw is not None

# Generated at 2022-06-13 00:53:08.091461
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hardware = FreeBSDHardware(dict(module=dict()))
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) > 1
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts
    assert int(cpu_facts['processor_count']) >= 1


# Generated at 2022-06-13 00:53:14.985004
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    class TestModule(object):
        def get_bin_path(self, name, required=False):
            if name == 'dmidecode':
                return "dmidecode"
            else:
                return None


# Generated at 2022-06-13 00:53:24.493106
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils._text import to_bytes

    def get_bin_path(name):
        return '/bin/%s' % name

    class FreeBSDFactsModule(object):
        def __init__(self, module):
            self.module = module

        def get_bin_path(self, name):
            return '/bin/%s' % name

        def run_command(self, cmd, encoding=None):
            # To emulate a real sysctl command, we need to build a fake dmesg
            # output based on the current time.
            now = int(time.time())
            struct_format = '=L'
            struct_size = struct.calcsize(struct_format)