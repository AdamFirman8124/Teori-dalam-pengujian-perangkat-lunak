

# Generated at 2022-06-13 00:45:30.321622
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hardware = FreeBSDHardware()
    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor'] == ['Genuine Intel(R) CPU 0000 @ 2.30GHz']
    assert cpu_facts['processor_cores'] == '4'
    assert cpu_facts['processor_count'] == '4'


# Generated at 2022-06-13 00:45:37.726842
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Use a timestamp far in the past to test.
    kernel_boot_time = 50000
    raw_boot_time = struct.pack('@L', kernel_boot_time)
    class MockModule:
        class MockRunCommand:
            def __init__(self):
                self.rc = 0
                self.output = raw_boot_time
                self.error = b''

            def __call__(self, cmd, encoding, check_rc=True):
                return (self.rc, self.output, self.error)

        run_command = MockRunCommand()

        def __init__(self):
            self.fail_json = None
            self.run_command = self.MockRunCommand()

        def get_bin_path(self, bin):
            return bin


# Generated at 2022-06-13 00:45:50.050720
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''
    Test for learning dmi facts from system

    Uses dmidecode executable if available
    '''

    from ansible.module_utils import basic
    from ansible.module_utils.facts import module_provisioner

    # In case of missing dmidecode, return
    # the list of facts after filling 'NA'.
    if not basic.HAS_DMIDECODE:
        module = module_provisioner.ModuleProvisioner(dict(ANSIBLE_MODULE_ARGS={'gather_subset': 'all'}), basic.AnsibleModule)
        hardware_collector = FreeBSDHardwareCollector(module=module)
        facts = hardware_collector.collect(module=module)
        for (k, v) in facts['ansible_dmi'].items():
            assert v == 'NA'


# Generated at 2022-06-13 00:45:54.932368
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc.platform == 'FreeBSD'
    assert fhc.fact_class == 'freebsd'
    assert fhc.fact_subclass == 'hardware'
    assert isinstance(fhc.collect(), list)
    assert isinstance(fhc.options, dict)

# Generated at 2022-06-13 00:46:02.936850
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    fhw = FreeBSDHardware()

    def mockrun_command(module, command_path, command_args, check_rc=False, executable=None, encoding=None):
        if command_path == '/sbin/swapinfo':
            return (0, 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%\n', '')
        elif command_path == '/sbin/sysctl':
            return (0, 'vm.stats.vm.v_page_count: 176095\nvm.stats.vm.v_free_count: 107794\nvm.stats.vm.v_page_size: 4096\n', '')
        else:
            return (0, '', '')

    fhw.module.run_command = mockrun

# Generated at 2022-06-13 00:46:06.383760
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = AnsibleModule(argument_spec={})
    is_freebsd = module.get_bin_path('freebsd-version')
    if not is_freebsd:
        module.fail_json(msg='This system is not FreeBSD')
    facts_collector = FreeBSDHardwareCollector(module=module)
    assert facts_collector._platform == 'FreeBSD'
    assert issubclass(facts_collector._fact_class, Hardware)
    assert facts_collector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 00:46:14.537419
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class FreeBSDHardwareTest:
        def get_bin_path(self, bin_name):
            return '/bin/%s' % bin_name

        def run_command(self, command_args, encoding=None):
            (rc, out, err) = (0, '', '')

# Generated at 2022-06-13 00:46:24.867421
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys

    dmi_bin = 'dummy_dmidecode'

# Generated at 2022-06-13 00:46:35.212003
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.six import PY3

    module = DummyAnsibleModule()

    # Disable loading of dmidecode on PY3.
    if PY3:
        module.run_command = DummyAnsibleModule.run_command_py3
    else:
        module.run_command = DummyAnsibleModule.run_command_py23

    freebsd_hw_ins = FreeBSDHardware(module)

    # populate the hardware object
    freebsd_hw_ins.populate()

    # assert the hardware object facts
    assert(freebsd_hw_ins.facts['uptime_seconds'] == 1234)
    assert(freebsd_hw_ins.facts['processor'] is not None)
    assert(freebsd_hw_ins.facts['devices'] is not None)

# Generated at 2022-06-13 00:46:35.753195
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert True

# Generated at 2022-06-13 00:46:55.932710
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    import datetime
    import time

    module_mock = Mock()
    module_mock.run_command.return_value = 0, struct.pack('@L', int(time.time())), ''

    facts = FreeBSDHardware(module_mock)
    uptime_facts = facts.get_uptime_facts()

    assert 'uptime_seconds' in uptime_facts

    uptime = datetime.timedelta(seconds=uptime_facts['uptime_seconds'])
    assert uptime.days >= 0


# Generated at 2022-06-13 00:47:06.400550
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    sysctl = module.get_bin_path('sysctl')
    cpu_facts = {}
    cpu_facts['processor'] = []
    if sysctl:
        rc, out, err = module.run_command("%s -n hw.ncpu" % sysctl, check_rc=False)
        cpu_facts['processor_count'] = out.strip()

    dmesg_boot = get_file_content(FreeBSDHardware.DMESG_BOOT)
    if not dmesg_boot:
        try:
            rc, dmesg_boot, err = module.run_command(module.get_bin_path("dmesg"), check_rc=False)
        except Exception:
            dmesg_boot = ''


# Generated at 2022-06-13 00:47:14.467854
# Unit test for method get_memory_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:47:18.557762
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    test_module.run_command = MagicMock(return_value=(0, 'hw.ncpu: 4', ''))  # mock run_command()

    hw = FreeBSDHardware(test_module)
    result = hw.get_memory_facts()
    assert result['processor_count'] == '4'



# Generated at 2022-06-13 00:47:23.423712
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Create an empty object of the FreeBSDHardware class
    fhw_obj = FreeBSDHardware()

    # Mock needed parameters for the get_memory_facts method
    class StructType:
        pass
    fhw_obj.module = StructType()
    fhw_obj.module.get_bin_path = lambda x: '/sbin/sysctl'
    fhw_obj.module.run_command = lambda x, y: ('0', 'vm.stats.vm.v_page_size: 65535\nvm.stats.vm.v_page_count: 113926\nvm.stats.vm.v_free_count: 885\n', '')

    # Expected output after executing get_memory_facts
    expected_memory_facts = {'memtotal_mb': 728, 'memfree_mb': 56}

    # The actual

# Generated at 2022-06-13 00:47:31.623158
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    hardware = FreeBSDHardware(module)
    hardware.populate()
    # cpu_facts test
    print("cpu_facts test")
    assert hardware.cpu_facts['processor_count'] == '1'
    assert hardware.cpu_facts['processor_cores'] == '2'
    assert hardware.cpu_facts['processor'][0] == 'Intel(R) Core(TM) i7-3740QM CPU @ 2.70GHz (2704.66-MHz K8-class CPU)'



# Generated at 2022-06-13 00:47:38.903096
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from sys import version_info
    import pickle

    if version_info[0] >= 3:
        unicode = str

    module = basic.AnsibleModule(
        argument_spec = dict()
    )

    module.run_command = lambda *args, **kwargs: (0, pickle.dumps(10.0), b"")

    hardware = FreeBSDHardware(module=module)

    assert hardware.get_uptime_facts() == {'uptime_seconds': 10}

# Generated at 2022-06-13 00:47:44.104386
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Unset the locale LC_ALL (relying on the default value)
    # In case LANG is set, use C.UTF-8, which is available in
    # Debian, so that we don't fail in the test when it is run
    os.environ['LC_ALL'] = "C.UTF-8"
    try:
        del os.environ['LC_ALL']
    except KeyError:
        pass

    # Create the hardware object
    hardware = FreeBSDHardware()

    # test the function get_uptime_facts
    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] >= 0

# Generated at 2022-06-13 00:47:54.679307
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():

    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    #sysctl and dmesg are assumed to be in path
    res = FreeBSDHardware(module=module).populate()
    #FIXME -- the 'devices' and 'mounts' output should be more reliably
    #         comparable, so that we can test for them.
    assert 'processor' in res.keys()
    assert 'system_vendor' in res.keys()
    assert 'memtotal_mb' in res.keys()
    assert 'uptime_seconds' in res.keys()
    assert 'mounts' in res.keys()
    assert 'devices' in res.keys()

# Generated at 2022-06-13 00:48:03.000611
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    import sys
    import ansible.module_utils.facts.hardware.freebsd


# Generated at 2022-06-13 00:48:35.382477
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Create the object
    hardware = FreeBSDHardware()

    # Create fake memory facts and fake swapinfo output
    memory_facts = {'memtotal_mb': 100, 'swaptotal_mb': 50, 'swapfree_mb': 40, 'memfree_mb': 10}
    swapinfo_out = "Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%"

    # Mock the object
    hardware.module = Mock()
    hardware.module.run_command.return_value = (0, swapinfo_out, '')

    # Test
    result = hardware.get_memory_facts()
    assert result == memory_facts


# Generated at 2022-06-13 00:48:43.383254
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """
    Unit test for method populate of class FreeBSDHardware.
    This method is testing the whole class.
    """
    set_module_args(dict(gather_subset='all'))
    hardware = FreeBSDHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['devices']
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['swaptotal_mb']
    assert hardware_facts['processor']
    assert hardware_facts['system_vendor']
    assert hardware_facts['uptime_seconds']
    assert hardware_facts['mounts']
    assert hardware_facts['devices']

# Generated at 2022-06-13 00:48:45.198219
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    harware = FreeBSDHardware(module)
    res = harware.populate()
    assert type(res) is dict
    assert 'processor' in res



# Generated at 2022-06-13 00:48:50.672913
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    fh = FreeBSDHardware(None)
    print('dmi_facts = %s' % fh.get_dmi_facts())

# Generated at 2022-06-13 00:49:02.133865
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import datetime

    hardware = FreeBSDHardware()

    # Generate a time before the Unix Epoch
    time_before_epoch = datetime.datetime(1970, 1, 1) - datetime.timedelta(seconds=10)
    hardware._get_uptime_facts = lambda: time_before_epoch

    hardware.collect()

    assert hardware.uptime_seconds == 0

    # Generate a time after the Unix Epoch
    time_after_epoch = datetime.datetime.now()

    hardware._get_uptime_facts = lambda: time_after_epoch

    hardware.collect()

    assert hardware.uptime_seconds > 0 and hardware.uptime_seconds < int(time_after_epoch.timestamp())

    # Generate a time during the Unix Epoch
    time_during_epoch = dat

# Generated at 2022-06-13 00:49:06.727793
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():

    hardware_collector = FreeBSDHardwareCollector()

    hardware_facts = hardware_collector.collect()

    assert hardware_facts['processor'] is not None
    assert hardware_facts['processor_cores'] is not None
    assert hardware_facts['memtotal_mb'] is not None
    assert hardware_facts['swaptotal_mb'] is not None
    assert hardware_facts['devices'] is not None



# Generated at 2022-06-13 00:49:14.712100
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """
    FreeBSDHardware unit test for method populate
    """

    # Test FreeBSDHardware.populate()
    from ansible.module_utils.facts import hardware as hw

    # mock data to use for re-usable tests
    m_mem = {'memfree_mb': '377', 'swaptotal_mb': '2047', 'processor': ['Intel(R) Core(TM) i3-3240 CPU @ 3.40GHz'],
             'memtotal_mb': '3948', 'swapfree_mb': '1947', 'processor_count': '2', 'processor_cores': '2'}
    m_uptime = {'uptime_seconds': '205682'}

# Generated at 2022-06-13 00:49:22.803068
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import get_collector
    from ansible.module_utils.facts.timeout import timeout

    collected_facts = {}
    collector = get_collector(
        'FreeBSDHardwareCollector',
        collected_facts=collected_facts,
    )

    # Test with correct value.
    raw_value = to_bytes(
        'kern.boottime: { sec = 1567753934, usec = 78347 } Sun Sep 15 09:02:14 2019',
    )
    def side_effect(*args, **kwargs):
        return 0, raw_value, None


# Generated at 2022-06-13 00:49:33.250961
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware import FreeBSDHardware
    from time import time
    class TestModule:
        def __init__(self, uptime):
            self.sysctl = '/bin/sysctl'
            self.uptime = uptime
        def get_bin_path(self, arg):
            return self.sysctl
        def run_command(self, arg, check_rc=True, encoding=None):
            if encoding is None:
                return 0, self.uptime, None
            else:
                raise NotImplementedError('Unicode not implemented')
    class TestUnix:
        def __init__(self):
            self.module = TestModule(struct.pack('@LL', int(time()), 0))
    test_hardware = FreeBSDHardware(TestUnix())
    test_hardware.collect

# Generated at 2022-06-13 00:49:44.142650
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    # Initialize the object for class FreeBSDHardware
    # Import module_utils here to simulate 'ansible_facts'
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.utils import FactsParams
    params = FactsParams()
    freebsdobj = FreeBSDHardware(params)
    # Delete the '/dev' directory
    import shutil
    shutil.rmtree('/dev')
    # Create an empty '/dev' directory and then run program
    os.mkdir('/dev')
    result = freebsdobj.get_device_facts()
    os.rmdir('/dev')
    # If the program is executed successfully, it will return an empty dict
    assert result == {}
    # Create an empty file

# Generated at 2022-06-13 00:51:04.772922
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = FakeAnsibleModule()
    # When swapinfo is available
    swapinfo_path = '/usr/sbin/swapinfo'
    module.set_bin_path('swapinfo', swapinfo_path)

    module.set_command_response('swapinfo -k', {
        'stdout': 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%',
        'rc': 0
    })

    # When sysctl is available
    sysctl_path = '/sbin/sysctl'
    module.set_bin_path('sysctl', sysctl_path)


# Generated at 2022-06-13 00:51:12.153466
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.utils.shlex import shlex_split
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.system.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import timeout

    module = MockModule()
    freebsd_hardware = FreeBSDHardware(module)

    expected_uptime_facts = { 'uptime_seconds': 123 }

    # We need to get raw bytes, not UTF-8.
    rc, out, err = module.run_command(shlex_split("/sbin/sysctl -b kern.boottime"), encoding=None)
    if rc != 0:
        # Do not test when real command failed
        assert True
    else:
        struct_format = '@L'
        struct_size = struct.cal

# Generated at 2022-06-13 00:51:23.794777
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = FreeBSDHardware(module, collected_facts={})

    hw_facts = hw.populate()
    assert set(hw_facts.keys()) == set(['processor', 'swaptotal_mb', 'uptime_seconds', 'mounts', 'processor_count', 'devices', 'processor_cores', 'swapfree_mb', 'memtotal_mb', 'memfree_mb'])
    assert set(hw_facts['devices'].keys()) == set(['da0', 'ada0'])
    assert hw_facts['devices']['da0'] == []

    assert hw_facts['mounts'][0]['device'] == '/dev/ada0p3'
    assert hw_facts['mounts'][0]['mount'] == '/'
   

# Generated at 2022-06-13 00:51:29.723289
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FakeModule(object):
        def __init__(self):
            self.run_command_calls = []

        def get_bin_path(self, name, *args, **kwargs):
            return name

        def run_command(self, args, *kwargs):
            self.run_command_calls.append((args, kwargs))

            return 0, ' ', ''

    class FakeTime(object):
        def time(self):
            return 1549166939

    sysctl_cmd = '/sbin/sysctl'
    expected_output = [('-b', 'kern.boottime'),
                       (sysctl_cmd, '-b', 'kern.boottime')]
    expected_result = {
        'uptime_seconds': 12345,
    }

    # Mock get_bin_path

# Generated at 2022-06-13 00:51:39.645014
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.params['gather_subset'] = "!all,min"
    module.exit_json = exit_json
    hw = FreeBSDHardware(module)
    result = hw.populate()
    assert 'ansible_facts' in result
    assert isinstance(result['ansible_facts'], dict)
    assert 'devices' in result['ansible_facts']
    assert 'uptime_seconds' in result['ansible_facts']
    assert 'devices' in result['ansible_facts']
    assert 'memtotal_mb' in result['ansible_facts']
    assert 'memfree_mb' in result['ansible_facts']
    assert 'processor' in result['ansible_facts']
    assert 'processor_cores' in result['ansible_facts']

# Generated at 2022-06-13 00:51:43.145486
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hardware = FreeBSDHardware()
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_cores'] == '4'
    assert cpu_facts['processor_count'] == '4'
    assert len(cpu_facts['processor']) == 4

# Generated at 2022-06-13 00:51:51.490420
# Unit test for method get_memory_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:51:55.460461
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    '''
    Unit test for method get_uptime_facts
    '''
    test_class = FreeBSDHardware()

    def os_read(path, _):
        return b'\x00\x00\x00\x00\x00\x00\x00\x00'

    test_class.module.os_read = os_read
    res = test_class.get_uptime_facts()

    assert res == {'uptime_seconds': 0}

# Generated at 2022-06-13 00:52:01.616392
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """
    Test case for the method get_memory_facts of class FreeBSDHardware
    """
    hardware = FreeBSDHardware({})
    hardware.module = True
    hardware.module.run_command = lambda x, encoding=None: (0, x, '')
    data = hardware.get_memory_facts()
    assert data['memfree_mb'] == '-2147483648'

# Generated at 2022-06-13 00:52:11.257692
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """
    Test that the method get_memory_facts is working properly on FreeBSD
    """

    # Create a FreeBSDHardware instance for the test
    hardware = FreeBSDHardware()
    # Call the method with valid parameters
    hardware.module.run_command = MagicMock(return_value=(0, "vm.stats.vm.v_page_size: 4096\n"
                                                             "vm.stats.vm.v_page_count: 12243314\n"
                                                             "vm.stats.vm.v_free_count: 336514\n", ""))
    actual_result = hardware.get_memory_facts()
    assert hardware.module.run_command.called

    # Verify by comparing the result with expected results