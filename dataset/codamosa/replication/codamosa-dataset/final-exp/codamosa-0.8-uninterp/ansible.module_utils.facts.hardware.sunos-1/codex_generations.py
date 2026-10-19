

# Generated at 2022-06-13 01:06:28.028769
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    h = SunOSHardware()
    collected_facts = {'ansible_machine': 'i86pc'}
    h.populate(collected_facts)

# Generated at 2022-06-13 01:06:38.610248
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    my_class = SunOSHardware()
    output = ['System Configuration:  Oracle Corporation sun4v', ' Memory size: 4096 Megabytes', '']
    output = '\n'.join(output)
    my_class.module.run_command = lambda args, check_rc=False: (0, output, '')
    result = my_class.get_dmi_facts()
    assert result.get('system_vendor') == 'Oracle Corporation'
    assert result.get('product_name') == 'sun4v'

    # test for second regexp condition
    output = ['System Configuration:  Fujitsu M10-4S']
    output = '\n'.join(output)
    my_class.module.run_command = lambda args, check_rc=False: (0, output, '')
    result = my_class.get_

# Generated at 2022-06-13 01:06:51.137631
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    import json
    class ModuleMock(object):
        def __init__(self):
            self.run_command_result = []

# Generated at 2022-06-13 01:07:00.831181
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():

    hardware = SunOSHardware({'module_setup': True})

    # Test cpu_facts with real output

# Generated at 2022-06-13 01:07:06.971731
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    test_out = open('tests/resources/SunOS/kstat_p_sderr.txt').read()
    module = {}
    module['run_command'] = lambda cmd: [0, test_out, '']
    test_obj = SunOSHardware(module)
    result = test_obj.get_device_facts()
    assert result
    assert "devices" in result
    assert "sd0" in result['devices']
    assert "vendor" in result['devices']['sd0']
    assert "product" in result['devices']['sd0']
    assert "revision" in result['devices']['sd0']
    assert "serial" in result['devices']['sd0']
    assert "size" in result['devices']['sd0']

# Generated at 2022-06-13 01:07:18.499394
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:07:31.095797
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    import ansible.utils.context_objects as context_objects
    import ansible.module_utils.facts.hardware.sunos as sunos_module
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    test_hardware = SunOSHardware()

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import timeout

    class TestModule(object):
        def __init__(self):
            self.run_command_environ_update = dict()
            self.run_command_rc = 0
            self.run_command_out = to_bytes('')
            self.run_command_err = to_bytes('')
            self.params = dict()
            self.fail_json = dict()

# Generated at 2022-06-13 01:07:37.011459
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    class TestModule:
        def run_command(self, command):
            return 0, '', ''

    class TestSunOSHardware(SunOSHardware):
        def __init__(self):
            self.module = TestModule()

    hw = TestSunOSHardware()
    hw.get_memory_facts()
    assert hw


# Generated at 2022-06-13 01:07:44.985581
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand()
    module.get_bin_path = FakeGetBinPath()
    module.get_file_content = FakeGetFileContent()
    test_facts = {}
    test_hw = SunOSHardware(module)
    results = test_hw.get_cpu_facts(test_facts)

    assert results['processor'] == ['SPARC T4 (chipid 0, clock 1795 MHz)',
                                    'SPARC T4 (chipid 1, clock 1795 MHz)']
    assert results['processor_count'] == 2
    assert results['processor_cores'] == 16


# Generated at 2022-06-13 01:07:51.412752
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():

    class ModuleMock:
        def run_command(self, command):
            if command == ["/usr/sbin/prtconf"]:
                out = 'Memory size: 32 Megabytes'
                return 0, out, ''
            if command == "/usr/sbin/swap -s":
                return 0, 'total: 169504k bytes allocated + 15080k reserved = 185084k used, 159816k available', ''
        get_bin_path = lambda self, name: name

    class FactsMock:
        pass

    facts = FactsMock()
    module = ModuleMock()
    memory_facts = SunOSHardware(module, facts).get_memory_facts()
    assert memory_facts['memtotal_mb'] == 32
    assert memory_facts['swapfree_mb'] == 155

# Generated at 2022-06-13 01:08:16.497818
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    module = DummyModule({}, {}, {}, {}, {})

    collector = SunOSHardwareCollector()
    assert collector._platform == 'SunOS'
    assert collector.required_facts == set(['platform'])

    collector.collect(module=module, collected_facts=None)
    assert module.called_functions[-1] == ('collect_device_facts',)
    assert module.called_functions[-2] == ('collect_uptime_facts',)
    assert module.called_functions[-3] == ('collect_mount_facts',)
    assert module.called_functions[-4] == ('collect_dmi_facts',)
    assert module.called_functions[-5] == ('collect_cpu_facts',)

# Generated at 2022-06-13 01:08:28.012172
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:08:39.611674
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:08:50.143709
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    test_module = type('FakeModule', (object,), {'run_command': get_uptime_facts})
    setattr(test_module, 'get_bin_path', lambda module, path, opt_dirs: path)
    test_facts = SunOSHardwareCollector(module=test_module).collect()['ansible_facts']
    uptime = test_facts.get('ansible_uptime')

    assert uptime['seconds'] > 0
    assert uptime['hours'] == uptime['minutes'] == uptime['days'] == 0



# Generated at 2022-06-13 01:08:58.466394
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    """
    Unit test for method get_memory_facts of class SunOSHardware.
    :return:
    """
    prtconf_out = """Memory size: 8192 Megabytes
    """
    swap_s_out = """swapfile             dev   swaplo blocks   free
/dev/zvol/dsk/rpool/swap 214,1         16  2097136  2097136
"""
    test_obj = SunOSHardware()
    test_obj.module.run_command = MagicMock(return_value=(0, prtconf_out, ''))
    test_obj.module.run_command = MagicMock(return_value=(0, swap_s_out, ''))
    mem_facts = test_obj.get_memory_facts()
    assert mem_facts['memtotal_mb'] == 8192

# Generated at 2022-06-13 01:09:09.785885
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:09:17.913555
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    class test_module():
        def get_bin_path():
            pass
        def run_command(cmd):
            return {
                "/usr/sbin/prtconf": (
                    0,
                    'System Configuration: Sun Microsystems sun4v\nMemory size: 1024 Megabytes',
                    ''
                ),
                "/usr/sbin/swap -s": (
                    0,
                    'total: 16516k bytes allocated + 656k reserved = 17172k used, 41834680k available',
                    ''
                )
            }.get(cmd)
    module = test_module()
    mhw = SunOSHardware(module)
    mhw.get_memory_facts()
    assert mhw.facts['memtotal_mb'] == 1024
    assert mhw.facts['swap_allocated_mb'] == 16


# Generated at 2022-06-13 01:09:29.002140
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # Test setup
    module = MagicMock()
    module.run_command.side_effect = [('', 'System Configuration: Sun Microsystems sun4v SPARC Enterprise T5440', '')]

    # Test execution
    test_obj = SunOSHardware(module)
    facts = test_obj.get_dmi_facts()

    # Test assertions
    module.run_command.assert_called_with('/usr/sbin/prtdiag')
    assert ('system_vendor' in facts)
    assert ('product_name' in facts)
    assert (facts['system_vendor'] == 'Sun Microsystems')
    assert (facts['product_name'] == 'sun4v SPARC Enterprise T5440')

# Generated at 2022-06-13 01:09:33.878424
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # Make sure we don't run in UTC timezone.
    os.environ['TZ'] = 'America/New_York'
    # Make sure time.time() returns epoch time in seconds.
    time._struct_time_time = time.time
    # Make sure time.time() returns epoch time in seconds rather than milliseconds.
    time._struct_time_mtime = time.time
    # Make sure time.time() returns a timestamp without a fractional part.
    time.time = lambda: int(time.time())

    f = SunOSHardware()
    uptime_facts = f.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] > 0
    assert isinstance(uptime_facts['uptime_seconds'], int)

# Generated at 2022-06-13 01:09:39.710686
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    mock_module = MagicMock()
    mock_module.run_command.return_value = (0, 'unix:0:system_misc:boot_time 1548249689', '')
    sunos_hw = SunOSHardware()

    # Because we mock module.run_command, we do not get the uptime_seconds
    # of the current system. So we hardcode its value instead.
    expected_uptime_facts = {
        'uptime_seconds': 1567832992
    }

    uptime_facts = sunos_hw.get_uptime_facts()

    assert uptime_facts == expected_uptime_facts

# Generated at 2022-06-13 01:10:17.836867
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = MockModule()
    facts_collector = SunOSHardware()
    facts = facts_collector.populate()

    assert facts['processor'] == ['SUNW,UltraSPARC-IIi @ 184MHz']
    assert facts['processor_cores'] == 'NA'
    assert facts['processor_count'] == 1
    assert facts['memtotal_mb'] == 1024
    assert facts['swap_reserved_mb'] == 0
    assert facts['swap_allocated_mb'] == 0
    assert facts['swaptotal_mb'] == 0
    assert facts['swapfree_mb'] == 0
    assert facts['swap_used_mb'] == 0
    assert facts['swap_percent_used'] == 0
    assert facts['swap_percent_free'] == 0

# Generated at 2022-06-13 01:10:29.292057
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    # Create a SunOSHardware instance
    sun_hw = SunOSHardware()
    # kstat output

# Generated at 2022-06-13 01:10:36.502112
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = MagicMock()
    module.run_command.return_value = (0, 'unix:0:system_misc:boot_time     1548249689', '')
    # We want to test methods of SunOSHardware, not the entire class.
    # Because of this, we need to create a mock object in order to pass it as a parameter.
    mock_facts = MagicMock()
    facts = SunOSHardware.get_uptime_facts(mock_facts, module)
    assert type(facts) is dict


# Generated at 2022-06-13 01:10:38.996132
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModule({})
    module.run_command = MagicMock(return_value=(0, 'unix:0:system_misc:boot_time\t1548249689', ''))
    fact = SunOSHardware(module)
    collected_facts = {}
    collected_facts['uptime_seconds'] = 0
    collected_facts = fact.get_uptime_facts(collected_facts)

    assert collected_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 01:10:44.237576
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    from ansible.module_utils.facts.hardware import SunOSHardware
    from ansible.module_utils.facts.utils import get_file_content

    sd_facts = get_file_content('./test/unit/module_utils/facts/hardware/sunos_sd_facts')

# Generated at 2022-06-13 01:10:55.082564
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    import os
    import shutil
    import tempfile

    # Setup
    class Module:
        def __init__(self):
            self.run_command = run_command

        def get_bin_path(self, name, opt_dirs=[]):
            return "/usr/bin/kstat"

    class Facts:
        def __init__(self, platform):
            self._data = {
                'platform': platform
            }

    def run_command(command, check_rc=True):
        class Response:
            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err

        # Use current time as a fake boot time
        boot_time = int(time.time())


# Generated at 2022-06-13 01:11:04.640442
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    dmi_facts = {'system_vendor': 'Sun Microsystems',
                 'product_name': 'Sun Fire V240'}
    system_conf = 'System Configuration: Sun Microsystems  Sun Fire V240\n'
    assert(SunOSHardware().get_dmi_facts(system_conf) == dmi_facts)
    system_conf = 'System Configuration: VMware, Inc. VMware Virtual Platform\n'
    assert(SunOSHardware().get_dmi_facts(system_conf) == {'system_vendor': 'VMware, Inc.',
                                                         'product_name': 'VMware Virtual Platform'})
    system_conf = 'System Configuration: Oracle Corporation        SUN FIRE X4300 M2 SERVER'

# Generated at 2022-06-13 01:11:14.908546
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModuleStub(argument_spec=dict())
    hardware = SunOSHardware(module)

    physid = 0
    sockets = {}

    cpu_facts = []

    collected_facts = dict()
    collected_facts['ansible_machine'] = 'i86pc'


# Generated at 2022-06-13 01:11:19.255273
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = SunOSHardware()

# Generated at 2022-06-13 01:11:24.514941
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    import json

    # Test data for class
    # Sample data for SunOS platform

# Generated at 2022-06-13 01:12:35.864235
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """
    SunOSHardware.get_cpu_facts() Test
    """
    test_object = SunOSHardware()


# Generated at 2022-06-13 01:12:47.977530
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    """ Test SunOSHardware.get_uptime_facts for known output of kstat
        command.
    """

    class FakeModule():
        def run_command(self, cmd):
            if cmd == '/usr/bin/kstat -p unix:0:system_misc:boot_time':
                return 0, 'unix:0:system_misc:boot_time\t1554487083', ''
            else:
                return 1, '', 'err'

    # Current time: Thu Feb 7 05:24:06.157336 2019
    fake_module = FakeModule()
    sun_hardware = SunOSHardware(fake_module)
    uptime = sun_hardware.get_uptime_facts()

    boot_time = 1554487083
    # Current time: Fri Feb 15 05:14:48.204764 2019


# Generated at 2022-06-13 01:12:57.357994
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    """
    Test for method SunOSHardware._get_uptime_facts

    Test scenario:
        - Call method with a dummy kstat output
        - Test if the correct uptime is returned
    """

    class TestModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, args, check_rc=True):
            return 0, "unix:0:system_misc:boot_time    1548249689", None

    class TestSunOSHardware(SunOSHardware):
        def __init__(self, module):
            super(TestSunOSHardware, self).__init__(module)

    tsh = TestSunOSHardware(TestModule())

    # current time = 1548269596
    assert tsh._get_uptime_facts()['uptime_seconds'] == 1548269

# Generated at 2022-06-13 01:12:58.664433
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec=dict())
    SunOSHardware().get_device_facts()



# Generated at 2022-06-13 01:13:06.691610
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = MagicMock()
    set_module_args({})

    # Mock sunos_memory and sunos_cpu facts
    module.run_command = MagicMock(return_value=(0, sample_memory_facts, ''))
    memory_facts = SunOSHardware._parse_memory_facts(module)
    module.run_command = MagicMock(return_value=(0, sample_cpu_facts, ''))
    cpu_facts = SunOSHardware._parse_cpu_facts(module)

    # Mock device_facts, dmi_facts and mount_facts
    module.get_file_content = MagicMock(return_value=sample_fstab)
    mount_facts = SunOSHardware._parse_mount_facts(module)

# Generated at 2022-06-13 01:13:09.190544
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardware_collector = SunOSHardwareCollector()
    assert hardware_collector._fact_class is not None
    assert hardware_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:13:18.206332
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():

    test_module = SunOSHardware.platform
    error1 = 'kstat returned status code "1".'
    error2 = 'get_device_facts failed to get dmi facts on SunOS.'

    m = SunOSHardware()
    m.module = FakeModule(test_module)

    d = {}

# Generated at 2022-06-13 01:13:22.465068
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    def mykstat(cmd):
        return(0, 'unix:0:system_misc:boot_time    1548249689', '')

    sh = SunOSHardware({})
    sh.module = MockModule()
    sh.module.run_command = mykstat
    sh.get_uptime_facts()
    assert(sh.facts['uptime_seconds'] == int(time.time() - 1548249689))



# Generated at 2022-06-13 01:13:24.949793
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    SunOSHardware(module).populate()


# Generated at 2022-06-13 01:13:34.644410
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    mock_module = type('MockModule', (), {})()
    mock_module.run_command = type('MockRunCommand', (), {})()