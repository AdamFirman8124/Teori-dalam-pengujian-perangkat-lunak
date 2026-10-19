

# Generated at 2022-06-13 00:45:31.281116
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    cpu_facts = {'processor': ['AMD Athlon(tm) II X2 215 Processor'],
                 'processor_cores': '2',
                 'processor_count': '2'}
    module = FakeModule()
    fhw = FreeBSDHardware()
    facts = fhw.get_cpu_facts()

    for k in cpu_facts:
        assert facts[k] == cpu_facts[k]


# Generated at 2022-06-13 00:45:38.346088
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    test_module = type('AnsibleModule', (object,), dict(params=dict(), fail_json=None))()

    test_module.get_bin_path = lambda arg: arg
    test_hardware = FreeBSDHardware(module=test_module)


# Generated at 2022-06-13 00:45:50.733825
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    from ansible.module_utils.facts.timeout import TimeoutError
    # These are the expected results for this example.
    expected_results = {'processor': ['AMD Athlon(tm) XP 2400+', 'AMD Athlon(tm) XP 2400+'],
                        'processor_cores': '1',
                        'processor_count': '2'}

    # This is a sample of the output of /var/run/dmesg.boot file.

# Generated at 2022-06-13 00:45:56.968513
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    test_object = FreeBSDHardware()
    test_object.module.run_command = run_command

    facts = test_object.get_cpu_facts()

    assert_equals(facts["processor_cores"], "2")
    assert_equals(facts["processor_count"], "1")
    assert_equals(facts["processor"][0], "Core i3-6100 (3.7GHz)")



# Generated at 2022-06-13 00:46:07.820056
# Unit test for method populate of class FreeBSDHardware

# Generated at 2022-06-13 00:46:15.288939
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    '''
    Mock the return code, stdout and stderr of the run_command method of the
    host.
    '''
    mock_run_command = Mock(return_value=(0, 'hw.ncpu: 4', ''))
    with patch.object(answer_module.AnsibleModule, 'run_command') as run_command:
        run_command.side_effect = mock_run_command
        freebsd_hw = FreeBSDHardware({})
        assert freebsd_hw.get_cpu_facts() == {'processor': [], 'processor_cores': 'NA', 'processor_count': '4'}
        assert run_command.call_count == 1
        assert run_command.call_args[0][0] == '/sbin/sysctl -n hw.ncpu'


# Generated at 2022-06-13 00:46:25.367821
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    mod = AnsibleModule(argument_spec={})
    mod.get_bin_path = MagicMock(return_value="/bin/sysctl")

# Generated at 2022-06-13 00:46:35.501513
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(argument_spec=dict(bin_path=dict(type='str')))
    module.params['bin_path'] = dict(dmidecode='/usr/sbin/dmidecode')

# Generated at 2022-06-13 00:46:42.173886
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.hardware import HardwareCollector
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.hardware.linux.distribution import LinuxDistribution
    hardware_obj = FreeBSDHardware()
    hardware_obj.populate()
    assert hardware_obj.get_all()['uptime_seconds'] > 0



# Generated at 2022-06-13 00:46:47.044537
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    from ansible.module_utils.facts.collector.freebsd import FreeBSDHardware
    freebsd = FreeBSDHardware(None)
    cpu_facts = freebsd.get_cpu_facts()
    assert isinstance(cpu_facts, dict) and cpu_facts
    for key in 'processor', 'processor_cores', 'processor_count':
        assert cpu_facts.get(key) is not None


# Generated at 2022-06-13 00:46:59.533488
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    facts = {}
    hardware = FreeBSDHardware(None, facts, None)
    hardware.get_cpu_facts()



# Generated at 2022-06-13 00:47:02.617660
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc._platform == 'FreeBSD'
    assert fhc._fact_class == FreeBSDHardware
    return fhc


# Generated at 2022-06-13 00:47:03.252418
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    pass

# Generated at 2022-06-13 00:47:12.708461
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class AnsibleModuleMock(object):
        def __init__(self):
            self._bin_path = {}

        def get_bin_path(self, command):
            # Paths to dmidecode, dmidecode.8 and dmidecode.old must be fake
            # in order to avoid problems when the unit test is executed in a
            # system which contains dmidecode
            if command.startswith('dmidecode'):
                self._bin_path[command] = os.path.join(os.path.dirname(__file__), command)
            return self._bin_path.get(command)
    class MockModule:
        def __init__(self):
            self.params = { 'timeout' : 0 }
            self.fail_json = self.check_fail_json
            self.run

# Generated at 2022-06-13 00:47:13.761150
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    candidate = FreeBSDHardware()
    data = candidate.get_dmi_facts()
    assert('bios_date' in data)



# Generated at 2022-06-13 00:47:20.358537
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})

    hardware_obj = FreeBSDHardware(module)

    hardware_obj.module.run_command = MagicMock(return_value=(0, '1', ''))
    hardware_obj.get_cpu_facts = MagicMock(return_value={"processor_cores": 2, "processor": ["Intel(R) Core(TM) i3-4370 CPU @ 3.80GHz", "Intel(R) Core(TM) i3-4370 CPU @ 3.80GHz"], "processor_count": 2})
    hardware_obj.get_memory_facts = MagicMock(return_value={"memtotal_mb": 1024, "memfree_mb": 512})
    hardware_obj.get_uptime_facts = MagicMock(return_value={"uptime_seconds": 100})
    hardware_

# Generated at 2022-06-13 00:47:31.154995
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hardware_instance = FreeBSDHardware()

    hardware_instance.module.run_command = fake_run_command

    # Test sysctl command failed
    hardware_instance.module.run_command.side_effect = [[1, '', 'Execution failed']]
    memory_facts = hardware_instance.get_memory_facts()

    assert memory_facts == {}

    # Test a command successful
    hardware_instance.module.run_command.side_effect = [[0, 'vm.stats.vm.v_page_size: 16384\nvm.stats.vm.v_page_count: 1048576\nvm.stats.vm.v_free_count: 524288\n', '']]
    memory_facts = hardware_instance.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 16
    assert memory_

# Generated at 2022-06-13 00:47:40.352464
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 00:47:44.562301
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhcollector = FreeBSDHardwareCollector(None)

    assert isinstance(fhcollector, HardwareCollector), \
        "Object fhcollector is not of type HardwareCollector"
    assert fhcollector.platform == 'FreeBSD'

# Generated at 2022-06-13 00:47:56.474124
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class FakeAnsibleModule:
        def __init__(self):
            self.params = {}
            self.check_mode = False

        def get_bin_path(self, command):
            if command == "sysctl":
                return True
            if command == "swapinfo":
                return True
            return None


# Generated at 2022-06-13 00:48:16.275144
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware()
    hardware.module = module
    hardware.setup()

    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == memory_facts['memtotal_mb']
    assert memory_facts['memfree_mb'] <= memory_facts['memtotal_mb']
    assert memory_facts['swaptotal_mb'] == memory_facts['swaptotal_mb']
    assert memory_facts['swapfree_mb'] <= memory_facts['swaptotal_mb']



# Generated at 2022-06-13 00:48:20.861268
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    memory_facts = hardware.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts

# Generated at 2022-06-13 00:48:28.290051
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = MockModule()
    hardware = FreeBSDHardware(module)

    rc = 0

# Generated at 2022-06-13 00:48:37.186124
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError

    # Given a class FreeBSDHardware
    freebsd_hardware = FreeBSDHardware()

    freebsd_hardware._get_mount_facts = lambda: {}
    freebsd_hardware._get_uptime_facts = lambda: {}
    freebsd_hardware._get_cpu_facts = lambda: {}

    # And the fact sysctl is found
    freebsd_hardware.module.get_bin_path = lambda s: '/bin/sysctl'

    # And I get memory facts from the class
    memory_facts = freebsd_hardware._get_memory_facts()

    # Then I expect the fact memtotal_mb is a number
    assert memory_facts

# Generated at 2022-06-13 00:48:38.972387
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert(fhc.platform == 'FreeBSD')


# Generated at 2022-06-13 00:48:41.909152
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert FreeBSDHardwareCollector.platform == 'FreeBSD'
    assert FreeBSDHardwareCollector.fact_class._platform == 'FreeBSD'
    assert FreeBSDHardwareCollector.fact_class._fact_class is FreeBSDHardware

# Generated at 2022-06-13 00:48:48.717156
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    os_facts = {'distribution': 'FreeBSD'}
    test_module = type('', (object,), {'get_bin_path': lambda self, x: '/bin/%s' % x, 'run_command': run_command})
    test_module.module = test_module()
    fh = FreeBSDHardware(module=test_module)
    fh.populate()

# Generated at 2022-06-13 00:48:52.278680
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector.freebsd_hardware import FreeBSDHardware

    kern_boottime = int(time.time()) - 3 * 3600  # 3h ago
    m = FreeBSDHardware()
    m.module = MagicMock()
    m.module.get_bin_path = MagicMock(return_value='/usr/bin/sysctl')
    m.module.run_command = MagicMock(return_value=(0, to_bytes(struct.pack('@L', kern_boottime)), to_bytes('')))
    assert m.get_uptime_facts()['uptime_seconds'] == 3 * 3600

# Generated at 2022-06-13 00:49:03.452854
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hardware_facts = FreeBSDHardware()
    module = type('module', (), {})()
    hardware_facts.module = module
    module.get_bin_path = lambda x: 'sysctl'

# Generated at 2022-06-13 00:49:12.285545
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Create a fake module.
    module = type('', (), {})()
    # Create a fake AnsiModule object.
    ansible_module = type('', (), {})()
    # Set the fake module as the ansible_module attribute of the AnsiModule object.
    ansible_module.module = module
    # Create a fake object to use as the run_command return.
    fake_result = type('', (), {'stdout': '', 'stderr':''})()
    # Create a fake attribute for the module.
    module.run_command = lambda x, encoding=None: fake_result
    # Create a fake attribute for the module.
    module.get_bin_path = lambda x: ''
    # Create the object that is being tested.

# Generated at 2022-06-13 00:49:54.857715
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hardware = FreeBSDHardware()
    hardware.module = AnsibleModuleMock()
    hardware.module.run_command.return_value = (0, '2', '')
    cpu_facts = hardware.get_cpu_facts()

    hardware.module.run_command.assert_called_once_with('sysctl -n hw.ncpu')
    assert cpu_facts['processor_count'] == '2'
    assert not cpu_facts['processor']
    assert not cpu_facts['processor_cores']


# Generated at 2022-06-13 00:49:58.866366
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    modules = {
        'ansible_facts': {},
        'ansible_module_args': {},
        'ansible_module_class': {},
        'ansible_module_name': '',
        'ansible_module_set': False,
    }

    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True, **modules)
    module.warn = mock.Mock()

    facter = FreeBSDHardware(module)

    result = facter.get_dmi_facts()

    # TODO: add test cases
    # assert result == expected_result

# Generated at 2022-06-13 00:50:09.219076
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # setup module arguments
    module_args = dict()

    # setup mock functions
    def get_bin_path_mock(path):
        return path

    # setup results

# Generated at 2022-06-13 00:50:17.965746
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # Create an instance of class FreeBSDHardware
    hardware = FreeBSDHardware("module")

    # Prepare data used in the test
    cpu_facts = {
        'processor': ['Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz'],
        'processor_cores': '2',
        'processor_count': '2',
    }
    # dmesg_boot stores the data returned by dmesg

# Generated at 2022-06-13 00:50:19.456031
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc.get_fact_class() == FreeBSDHardware
    assert fhc.get_platform() == 'FreeBSD'

# Generated at 2022-06-13 00:50:20.051489
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert FreeBSDHardwareCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 00:50:23.244809
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['form_factor'] == 'NA'



# Generated at 2022-06-13 00:50:26.816403
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.run_command = MagicMock(return_value=[0, TEST_DEVICES, ''])
    test_module.fail_json = MagicMock(return_value=None)
    test_facts = FreeBSDHardware(test_module).get_device_facts()
    assert test_facts['devices'] == JSON_TEST_DEVICES


# Generated at 2022-06-13 00:50:33.797795
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FakeModule:
        def __init__(self):
            self.tmpdir = os.getcwd()
            self.fail_json = self.fail
            self.log = self.logger

        def logger(self, msg):
            print(msg)

        def fail(self, msg):
            self.logger(msg)
            exit(1)

    fm = FakeModule()
    setattr(fm, 'run_command', lambda *_, **__: [0, '1234567890', ''])

    hw = FreeBSDHardware()
    hw.module = fm
    uptime_facts = {}
    uptime_facts['uptime_seconds'] = int(time.time() - 1234567890)
    assert uptime_facts == hw.get_uptime_facts()


# Generated at 2022-06-13 00:50:42.843589
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import platform
    import unittest

    class fake_module:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, tool):
            if tool == 'sysctl':
                return '/sbin/sysctl'
            else:
                return None

        def run_command(self, cmd, encoding=None):
            # We need to get raw bytes, not UTF-8.
            assert encoding is None

# Generated at 2022-06-13 00:52:07.392427
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class FakeFreeBSDHardwareModule:
        _ansible_module = None

        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, cmd, check_rc=True, encoding="utf-8"):
            return (0, FAKE_SYSCTL_HW_NCPU, "")

    hw = FreeBSDHardware(module=FakeFreeBSDHardwareModule(module_name='none'))
    result = hw.get_cpu_facts()

# Generated at 2022-06-13 00:52:10.158210
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    '''
    This function is used to test the constructor of FreeBSDHardwareCollector.
    '''
    collector = FreeBSDHardwareCollector()
    assert collector.platform == "FreeBSD"
    assert collector.fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:52:13.164558
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hw_collector = FreeBSDHardwareCollector()
    assert hw_collector.platform == 'FreeBSD'
    assert hw_collector.fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:52:21.020035
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    mock_module = type('MockModule', (object,), {
        'run_command': lambda self, command: (1, '', ''),
        'get_bin_path': lambda self, command: command,
    })
    mock_module = mock_module()
    hardware = FreeBSDHardware(mock_module)
    rc, out, err = mock_module.run_command("sysctl -n hw.physmem")
    total_physmem = int(out.split()[0])
    rc, out, err = mock_module.run_command("sysctl -n hw.usermem")
    user_physmem = int(out.split()[0])
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == total_physmem // 1024 // 1024
    assert memory

# Generated at 2022-06-13 00:52:24.153039
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModuleMock()
    hardware_collector = FreeBSDHardwareCollector(module)
    hardware = hardware_collector.collect(module, collected_facts=dict())
    assert isinstance(hardware, dict)



# Generated at 2022-06-13 00:52:31.689273
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    import pytest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    # Create a class for unit test
    class MyFreeBSDHardware(FreeBSDHardware):
        def __init__(self):
            self.sysctl = '/tmp/sysctl'    # Use a temporal file instead of real sysctl

        class ModuleMock:
            def __init__(self):
                self.params = {}
                self.check_mode = False
                # self.get_bin_path = lambda x: '/usr/bin/' + x   # No need to test the module
                self.run_command = lambda x, encoding=None: (0, '/tmp/sysctl output', '')


# Generated at 2022-06-13 00:52:36.601930
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = FakeModule()
    facts = FreeBSDHardware(module).get_device_facts()
    assert 'devices' in facts
    assert '/dev/ada0' in facts['devices']
    assert '/dev/ada1' in facts['devices']
    assert 'ada0s1a' in facts['devices']['/dev/ada0']
    assert 'ada1s1a' in facts['devices']['/dev/ada1']



# Generated at 2022-06-13 00:52:45.520713
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class TestModule:

        def get_bin_path(self, path):
            return path

        def run_command(self, cmd):
            return 0, '# dmidecode 2.12', ''

    class TestHardware:

        def __init__(self):
            self.module = TestModule()

        def get_dmi_facts(self):
            return FreeBSDHardware(self.module).get_dmi_facts()

    hd = TestHardware()
    dmi_facts = hd.get_dmi_facts()
    assert dmi_facts['bios_date'] == 'NA'
    assert dmi_facts['bios_vendor'] == 'NA'
    assert dmi_facts['bios_version'] == 'NA'
    assert dmi_facts['board_asset_tag'] == 'NA'


# Generated at 2022-06-13 00:52:53.772212
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Testing FreeBSDHardware.get_dmi_facts()
    # dmidecode output from FreeBSD 12.0-RELEASE-p6
    # dmidecode output from FreeBSD 8.2-RELEASE-p7
    # dmidecode output from FreeBSD 10.4-RELEASE-p8
    module = DummyModule()
    mod_obj = ModuleObj(module)

# Generated at 2022-06-13 00:53:03.253280
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    dmi_facts = hardware.get_dmi_facts()
    assert 'bios_date' in dmi_facts
    assert 'bios_vendor' in dmi_facts
    assert 'bios_version' in dmi_facts
    assert 'board_asset_tag' in dmi_facts
    assert 'board_name' in dmi_facts
    assert 'board_serial' in dmi_facts
    assert 'board_vendor' in dmi_facts
    assert 'board_version' in dmi_facts
    assert 'chassis_asset_tag' in dmi_facts
    assert 'chassis_serial' in dmi_facts
    assert 'chassis_vendor' in dmi_facts