

# Generated at 2022-06-13 01:06:39.563606
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.collector.sunos import SunOSHardwareCollector

    class TestModule():
        def run_command(self, command):
            if command == "/usr/bin/kstat cpu_info":
                return 0, "Clock_MHz\t2000\nbrand\tIntel(r) Xeon(r) CPU E5-2698 v3 @ 2.30GHz\nchip_id\t0\nimplementation\tGenuineIntel\n", ''
            elif command == ['prtconf']:
                return 0, 'System Configuration: Sun Microsystems sun4v\nMemory size: 2048 Megabytes', ''

# Generated at 2022-06-13 01:06:44.258762
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={})
    hardware_obj = SunOSHardware(module)
    uptime_facts = hardware_obj.get_uptime_facts()
    assert('uptime_seconds' in uptime_facts)

# Generated at 2022-06-13 01:06:48.261736
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hc = SunOSHardwareCollector(dict())
    assert hc.required_facts == set(['platform'])
    assert hc.platform == 'SunOS'
    assert hc.fact_class == SunOSHardware


# Generated at 2022-06-13 01:06:58.923317
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hw = SunOSHardware()


# Generated at 2022-06-13 01:07:11.361588
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:07:23.904826
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = MagicMock()
    run_command_result = (0, '', '')
    run_command_side_effect = [
        run_command_result,  # /usr/bin/kstat cpu_info
        run_command_result,  # /usr/sbin/prtconf
        run_command_result,  # /usr/sbin/swap -s
        run_command_result,  # /usr/bin/kstat -p sderr:::#{stat}
    ]

# Generated at 2022-06-13 01:07:28.597585
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    my_obj = SunOSHardwareCollector()
    assert my_obj._platform == 'SunOS'
    assert my_obj.required_facts == set(['platform'])
    assert my_obj._fact_class == SunOSHardware

# Generated at 2022-06-13 01:07:36.483544
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    m_module = MagicMock()
    m_module.run_command.side_effect = [
        # get_cpu_facts
        (0, '', ''),
        # get_memory_facts
        (0, '', ''),
        (0, '', ''),
        # get_dmi_facts
        (0, 'System Configuration: Sun Microsystems  sun4u\n', ''),
        # get_device_facts
        (0, '/usr/bin/kstat -p unix:0:system_misc:boot_time', ''),
        # get_mount_facts
        (0, '', ''),
    ]
    m_module.get_bin_path.side_effect = [
        '/usr/bin/kstat', '/usr/bin/prtdiag'
    ]


# Generated at 2022-06-13 01:07:39.353714
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    def test_required_facts():
        collector = SunOSHardwareCollector(module=None)
        assert collector.required_facts == set(['platform'])

    test_required_facts()

# Generated at 2022-06-13 01:07:47.368054
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:08:14.553760
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    m = SunOSHardware({'module_setup': True})
    rc, out, err = m.module.run_command(["/usr/sbin/prtconf"])
    memory_facts = m.get_memory_facts()
    assert memory_facts['memtotal_mb'] == int(out.splitlines()[3].split()[2])

    rc, out, err = m.module.run_command("/usr/sbin/swap -s")
    allocated = int(out.split()[1][:-1])
    reserved = int(out.split()[5][:-1])
    used = int(out.split()[8][:-1])
    free = int(out.split()[10][:-1])
    memory_facts = m.get_memory_facts()
    # swap_allocated_mb


# Generated at 2022-06-13 01:08:22.822233
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class MockModule(object):
        def run_command(*args, **kwargs):
            self = args[0]
            command = args[1]
            # return boot time
            if command == '/usr/bin/kstat -p unix:0:system_misc:boot_time':
                return 0, 'unix:0:system_misc:boot_time 1548249689', ''
        def get_bin_path(bin_name, opt_dirs):
            return '/usr/bin/kstat'
    class MockFactCollector(object):
        def collect(self):
            return {'platform': 'SunOS'}

    mm = MockModule()
    mfc = MockFactCollector()

    sh = SunOSHardwareCollector(module=mm, fact_collector=mfc)

# Generated at 2022-06-13 01:08:28.398111
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = FakeModule()
    module.run_command = lambda x: ['', 'System Configuration: Sun Microsystems sun4u', '']
    hw = SunOSHardware(module)
    expected = {'system_vendor': 'Sun Microsystems', 'product_name': 'sun4u'}
    assert hw.get_dmi_facts() == expected



# Generated at 2022-06-13 01:08:33.703760
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware(None)
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['system_vendor'] == 'Oracle Corporation'
    assert dmi_facts['product_name'] == 'Sun Fire 2900'

# Generated at 2022-06-13 01:08:38.268330
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class fake_module(object):
        def run_command(self, arg):
            return (0, "unix:0:system_misc:boot_time    1548249689", "")

    class fake_uptime_facts(object):
        def __init__(self):
            self.platform = "SunOS"
            self.module = fake_module()
            self.uptime_facts = {}

    kstat = SunOSHardware(fake_uptime_facts())
    uptime_facts = kstat.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 01:08:43.683723
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    SunOSHardware_dmi = SunOSHardware()
    cmd = "mock -r {0} {1}".format(SunOSHardware_dmi.platform, "prtdiag")
    SunOSHardware_dmi.module.run_command = lambda *args, **kwargs: (0, cmd, None)

    # Test the mock return value
    assert (SunOSHardware_dmi.get_dmi_facts())['system_vendor'] == 'mock'
    assert (SunOSHardware_dmi.get_dmi_facts())['product_name'] == '-r SunOS prtdiag'

    # Test that we get back an empty dictionary when there is no vendor information
    SunOSHardware_dmi.module.run_command = lambda *args, **kwargs: (0, "Hello, world!", None)

# Generated at 2022-06-13 01:08:55.548322
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from io import StringIO
    from ansible.module_utils.facts.sunos.hardware import SunOSHardware
    from ansible.module_utils.facts.sunos.hardware import SunOSHardwareCollector
    from ansible.module_utils.facts.sunos.hardware import SunOSHardwareCheck
    from ansible.module_utils.facts.sunos.sysctl import SunOSSysctlFactCollector
    from ansible.module_utils.facts.facts import Facts
    module = Facts({}, {}, True)
    module.run_command = lambda x, check_rc=True: [0, '', '']
    module.run_command_environ_update = {'LC_ALL': 'C', 'LANG': 'C', 'LC_MESSAGES': 'C'}
    facts_collector = SunOSHardwareCollect

# Generated at 2022-06-13 01:09:07.656244
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Example input
    #   module: Processor
    #   module: SUNW,UltraSPARC-T1
    #   clock_MHz: 1991
    #   cpu_type: sun4v
    #   cpu_implementation: SPARC_T1
    #   chip_id: 0

    vendor_expected = 'Sun Microsystems'
    model_expected = 'SUNW,UltraSPARC-T1 @ 1991MHz'

    # Set up module
    module = AnsibleModule(
        argument_spec = dict()
    )

# Generated at 2022-06-13 01:09:19.049989
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:09:31.079234
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # test data
    # uname -i
    platform = 'i86pc'
    in1 = (0, 'Fujitsu Siemens', None)
    in2 = (0, 'Oracle Corporation IBM', None)
    in3 = (0, 'Fujitsu Siemens', None)
    in4 = (0, 'Oracle Corporation sun4u', None)
    in5 = (0, 'Fujitsu Siemens', None)
    in6 = (0, 'QEMU', None)
    in7 = (0, 'Oracle Corporation', None)
    in8 = (0, 'Sun Microsystems sun4v', None)
    in9 = (0, 'VMware, Inc.', None)
    in10 = (1, '', None)
    in11 = (0, '', 'error')


# Generated at 2022-06-13 01:10:15.419827
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    import pytest
    system_vendor = 'vendor'
    product_name = 'sd510'
    processor = ['SPARC T4-4']
    processor_count = 1  # sockets
    processor_cores = 1  # virtual CPUs
    memtotal_mb = 32768
    swap_allocated_mb = 0  # could be different if oversubscribed
    swap_reserved_mb = 0  # could be different if oversubscribed
    swapfree_mb = 4096
    swaptotal_mb = 4096

# Generated at 2022-06-13 01:10:15.956232
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    pass

# Generated at 2022-06-13 01:10:21.557174
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # run_command() will return a MemoryError in Python 2 and a
    # subprocess.CalledProcessError in Python 3.  This dummy exception handler
    # will catch both and allow the tests to verify the expected values.
    def dummy_run_command(module, command):
        if command == ["/usr/sbin/prtconf"]:
            return 1, "Memory size: 32 GB", ""
        return 1, "", ""

    m_inst = SunOSHardware()
    m_inst.module = type('', (object,), {'run_command': dummy_run_command})
    assert m_inst.get_memory_facts() == {'memtotal_mb': 32 * 1024}

# Generated at 2022-06-13 01:10:32.361492
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """
    Testing SunOSHardware.get_cpu_facts
    """
    sunos_hardware = SunOSHardware({})
    expected_facts = {
        "processor": ["SPARC64-VII (chipid 0, clock 1200 MHz) ",
                      "SPARC64-VII (chipid 1, clock 1200 MHz) "],
        "processor_count": 2,
        "processor_cores": 8
    }

    # For mock_run_command
    PRTDIAG_PATH = "/usr/sbin/prtdiag"

    # pylint: disable=unused-argument
    def mock_run_command(module, cmd, *args, **kwargs):
        """
        mock_run_command
        """
        if cmd == PRTDIAG_PATH:
            output = TEST_PRTDIAG_OUTPUT

# Generated at 2022-06-13 01:10:40.850682
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # Create a class SunOSHardware object
    obj = SunOSHardware()
    # Create a function object
    func_obj = getattr(obj, "get_memory_facts")
    # Run prtconf command and get memory facts
    memory_facts = func_obj()
    # Check if the values in the dictionary are not None
    assert (memory_facts['memtotal_mb'] is not None and memory_facts['swapfree_mb'] is not None and
            memory_facts['swaptotal_mb'] is not None and memory_facts['swap_allocated_mb'] is not None and
            memory_facts['swap_reserved_mb'] is not None)



# Generated at 2022-06-13 01:10:47.501707
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, CPU_KSTAT_OUTPUT, ""))
    sunos_hw = SunOSHardware(module)
    result = sunos_hw.get_cpu_facts()
    assert result["ansible_processor"] == ["SPARC64-VII (chipid 0, clock 2400 MHz) @ 2400 MHz", "SPARC64-VII (chipid 0, clock 2400 MHz) @ 2400 MHz"]
    assert result["ansible_processor_cores"] == "2"
    assert result["ansible_processor_count"] == "2"


# Generated at 2022-06-13 01:10:55.927157
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    import pytest

    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    with pytest.raises(KeyError):

        class MockSunOSHardware:
            """ Mock class for SunOSHardware """
            def __init__(self):
                self.module = MockModule()

            def get_uptime_facts(self):
                return self.module.run_command('/usr/bin/kstat -p unix:0:system_misc:boot_time')

        sunos_hw = MockSunOSHardware()
        sunos_hw.get_uptime_facts()


# Generated at 2022-06-13 01:11:01.005982
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    hardware = SunOSHardware()
    hardware.module = MagicMock()
    hardware.module.run_command = MagicMock()
    hardware.module.run_command.return_value = ('0', 'Memory size: 256 Megabytes', '')
    hardware.collect_device_facts = False
    hardware.populate()
    assert hardware.facts['memtotal_mb'] == 256

# Generated at 2022-06-13 01:11:06.101927
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:11:15.613644
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class Module(object):
        def run_command(self, cmd, *args, **kwargs):
            class SderrOutput(object):
                def __init__(self):
                    self.out = dict()

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc_value, traceback):
                    pass

                def __getitem__(self, item):
                    return self.out[item]

                def __setitem__(self, item, value):
                    self.out[item] = value


# Generated at 2022-06-13 01:12:31.003949
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    data = SunOSHardware({}, {'platform': 'SunOS'})
    data.module.run_command = Mock(return_value=(0,
                                                 'System Configuration: Sun Microsystems sun4u',
                                                 ''))
    assert data.get_dmi_facts() == {'system_vendor': 'Sun Microsystems',
                                    'product_name': 'sun4u'}



# Generated at 2022-06-13 01:12:42.082892
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = FakeAnsibleModule()

    system_facts = {}
    hardware_collector = SunOSHardwareCollector(module, system_facts)
    facts = hardware_collector.collect(None, None)
    hardware = SunOSHardware(facts)

    hardware.populate()

    assert hardware.facts['memtotal_mb'] == 2000
    assert hardware.facts['swapfree_mb'] == 1004
    assert hardware.facts['swaptotal_mb'] == 2024
    assert hardware.facts['swap_allocated_mb'] == 2020
    assert hardware.facts['swap_reserved_mb'] == 2020

    assert len(hardware.facts['processor']) == 2
    assert hardware.facts['processor'][0] == 'Genuine Intel(R) CPU @ 2.40GHz'

# Generated at 2022-06-13 01:12:53.084698
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    '''
    This method is used to test get_cpu_facts method of SunOSHardware class,
    defined in facts/hardware/sunos.py
    '''

    # Creating an instance of SunOSHardware
    hardware_instance = SunOSHardware()

    # Set the attributes of hardware_instance
    hardware_instance.module = MockModule()
    hardware_instance.module.run_command.return_value = (0, 'module: \
        cpu_info\nbrand\nclock_MHz\nchip_id\nchiprev\nclog\ncore_id\n\
        implementation\npg\nstatus', '')

    # Create a Mock instance of collected_facts
    collected_facts = {}
    collected_facts['ansible_machine'] = 'i86pc'

    # Assert that get_cpu_facts returns the expected

# Generated at 2022-06-13 01:13:00.690360
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    out = """module: sun4v
module_reset2: 0x1
module_reset3: 0x1
clock_MHz: 1197
cpu_type: AMD64
chip_id: 0
state: on-line
chip_id: 1
state: on-line
chip_id: 2
state: on-line
chip_id: 3
state: on-line
implementation: AMD
brand: AMD Opteron(tm) Processor 6172"""

    hw = SunOSHardware()
    facts = hw.get_cpu_facts(collected_facts={'ansible_machine': 'i86pc'})
    for i in range(4):
        assert facts['processor'][i] == 'AMD Opteron(tm) Processor 6172 @ 1197MHz'

    assert facts['processor_count'] == 4

# Generated at 2022-06-13 01:13:10.802415
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    """
    This test function checks the method get_memory_facts
    """
    result = {}

    result['swap_reserved_mb'] = 0
    result['swap_allocated_mb'] = 0
    result['swapfree_mb'] = 0
    result['swaptotal_mb'] = 0
    result['memtotal_mb'] = 0

    # Use C locale for hardware collection helpers to avoid locale specific number formatting (#24542)
    locale = 'C'
    module = AnsibleModule(argument_spec={})
    module.run_command_environ_update = {'LANG': locale, 'LC_ALL': locale, 'LC_NUMERIC': locale}

    hardware = SunOSHardware(module)

    module.exit_json(changed=False, ansible_facts=hardware.populate())


# Unit

# Generated at 2022-06-13 01:13:14.660387
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module_args = {'module_name': 'test', 'module_args': {}}
    uptime_facts = SunOSHardware(module_args).get_uptime_facts()
    assert 'uptime_seconds' in uptime_facts
    assert uptime_facts['uptime_seconds'] >= 0

# Generated at 2022-06-13 01:13:22.464700
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModuleMock({})

    # Create an instance of class SunOSHardware assuming the system
    # has prtconf and swap -s.
    hardware = SunOSHardware(module)

    # Create a test fixture by creating a mock of the commands
    # and the expected results from the hardware.
    # prtconf
    out_prtconf = StringIO()
    out_prtconf.write("Memory size: 64 Megabytes")
    out_prtconf.seek(0)
    # swap -s
    out_swap_s = StringIO()
    out_swap_s.write("total: 8096k bytes allocated + 4k reserved = 8100k used, 473716k available")
    out_swap_s.seek(0)

    # mock the commands and the results
    module.run_command

# Generated at 2022-06-13 01:13:31.062928
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.facts.collector.sunos import SunOSHardware
    class MockModule(object):
        def run_command(self, command):
            return 0, 'unix:0:system_misc:boot_time    1548249689', ''

    module = MockModule()
    hardware = SunOSHardware(module)
    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == int(time.time() - 1548249689)
    assert len(uptime_facts) == 1

# Generated at 2022-06-13 01:13:38.943528
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    #
    # Create the object.
    hardware = SunOSHardware()
    expected = [
        "SPARC T5 (chipid 0, clock 1800 MHz)",
        "SPARC T5 (chipid 0, clock 1800 MHz)",
        "SPARC T5 (chipid 0, clock 1800 MHz)",
        "SPARC T5 (chipid 0, clock 1800 MHz)",
        "SPARC T5 (chipid 1, clock 1800 MHz)",
        "SPARC T5 (chipid 1, clock 1800 MHz)",
        "SPARC T5 (chipid 1, clock 1800 MHz)",
        "SPARC T5 (chipid 1, clock 1800 MHz)"
    ]
    #
    # Test the functionality.
    result = hardware.get_cpu_facts({'ansible_machine': 'sun4u'})
    assert str(result['processor']) == str

# Generated at 2022-06-13 01:13:44.600568
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardwareCollector = SunOSHardwareCollector(module=module)
    hardware = SunOSHardware(module)
    facts = hardware.populate()
    assert 'processor_count' in facts
    assert 'processor' in facts
    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swap_allocated_mb' in facts
    assert 'swap_reserved_mb' in facts
    assert 'system_vendor' in facts
    assert 'product_name' in facts
    assert 'devices' in facts
