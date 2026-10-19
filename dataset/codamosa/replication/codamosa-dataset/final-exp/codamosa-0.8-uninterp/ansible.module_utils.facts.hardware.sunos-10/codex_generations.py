

# Generated at 2022-06-13 01:06:35.254687
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class MockModule(object):
        def run_command(self, cmd, debug=None, check_rc=True, environ_update=None):
            return (0, "unix:0:system_misc:boot_time    1548249689", "")

    class MockFactCollector(object):
        def __init__(self):
            self.get_all = lambda: {'platform': 'SunOS'}

    obj = SunOSHardware(MockFactCollector())
    obj.module = MockModule()

    assert obj.get_uptime_facts() == {'uptime_seconds': int(time.time()) - 1548249689}

# Generated at 2022-06-13 01:06:42.788841
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()

    sdh = SunOSHardware(module)

# Generated at 2022-06-13 01:06:54.213829
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = None

    sunos_hardware = SunOSHardware(module)
    collected_facts = {'ansible_machine': 'i86pc'}
    facts_dict = sunos_hardware.populate(collected_facts)

    assert isinstance(facts_dict, dict) == True
    assert 'memtotal_mb' in facts_dict
    assert 'swapfree_mb' in facts_dict
    assert 'swaptotal_mb' in facts_dict
    assert 'swap_allocated_mb' in facts_dict
    assert 'swap_reserved_mb' in facts_dict
    assert 'processor' in facts_dict
    assert 'processor_count' in facts_dict
    assert 'processor_cores' in facts_dict


# Generated at 2022-06-13 01:06:57.596327
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hardware = SunOSHardware()
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts

# Generated at 2022-06-13 01:07:07.220716
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = MagicMock()
    module.run_command = MagicMock()
    module.run_command.return_value = 0, open('../unittests/files/cpu_info.txt').read(), None
    sh = SunOSHardware(module)

    cpu_facts = sh.get_cpu_facts()

    assert cpu_facts['processor'] == ['sun4u']
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 64
    assert cpu_facts['processor_threads_per_core'] == 1


# Generated at 2022-06-13 01:07:11.260931
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    # create a collector object
    sunoshw_collector_obj = SunOSHardwareCollector()

    # check if the class attribute is initialized or not
    if sunoshw_collector_obj.class_name != 'SunOSHardwareCollector':
        raise Exception('class_name is not initialized')

# Generated at 2022-06-13 01:07:23.798531
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    class CustomModule:
        def run_command(self, args):
            return (0, 'module: SUNW,SPARC-Enterprise-T5220\n'
                               'brand: sparclite\n'
                               'clock_MHz: 1996\n'
                               'chip_id: 0\n'
                               'implementation: SPARC-M6\n'
                               'module: SUNW,SPARC-Enterprise-T5220\n'
                               'brand: sparclite\n'
                               'clock_MHz: 1996\n'
                               'chip_id: 1\n'
                               'implementation: SPARC-M6\n', '')

            return (0, '', '')

    fact_class = SunOSHardware(CustomModule())
    cpu_facts = fact_class.get

# Generated at 2022-06-13 01:07:34.438332
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)


# Generated at 2022-06-13 01:07:44.876087
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    hardware = SunOSHardware()
    hardware_output = hardware.populate()

    assert hardware_output['uptime_seconds']
    assert hardware_output['uptime_seconds'] > 0

    assert hardware_output['memtotal_mb']
    assert hardware_output['memtotal_mb'] > 0

    assert hardware_output['swapfree_mb']
    assert hardware_output['swapfree_mb'] > 0

    assert hardware_output['swaptotal_mb']
    assert hardware_output['swaptotal_mb'] > 0

    assert hardware_output['swap_allocated_mb']
    assert hardware_output['swap_allocated_mb'] > 0

    assert hardware_output['swap_reserved_mb']
    assert hardware_output['swap_reserved_mb'] > 0

# Generated at 2022-06-13 01:07:47.733174
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    sh = SunOSHardware({})
    assert sh.get_dmi_facts() == {'product_name': 'Sun Fire V440', 'system_vendor': 'Sun Microsystems'}

# Generated at 2022-06-13 01:08:13.889121
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    facts = SunOSHardware()

    # When prtdiag is present in /usr/sbin
    m_run_command = m_get_bin_path = m_check_type_string = m_get_file_content = None

    def run_command_mock(self, args, check_rc=True):
        if "/usr/sbin/prtconf" in args:
            out = "Memory size: 16384 Megabytes"
        elif "/usr/sbin/swap -s" in args:
            out = "Total: 2097148k bytes allocated + 4556k reserved = 2097600k used, \
                    4194303616k available"

# Generated at 2022-06-13 01:08:16.329817
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    sunoshardware = SunOSHardware()
    uptime_facts = sunoshardware.get_uptime_facts()
    assert('uptime_seconds' in uptime_facts)


# Generated at 2022-06-13 01:08:24.079141
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()

    # expected returns from /usr/sbin/prtdiag

# Generated at 2022-06-13 01:08:34.597202
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    h = SunOSHardware()
    out = "System Configuration: Sun Microsystems  sun4u\n"
    out += "System clock frequency: 333 MHz\n"
    out += "Memory size: 8192 Megabytes\n"
    out += "System uptime: 10 days 10 hours 16 minutes 22 seconds\n\n"
    out += "System Configuration:  Sun Microsystems  T5240"
    assert h._get_dmi_facts(out) == {"system_vendor": "Sun Microsystems",
                                                 "product_name": "sun4u"}
    assert h._get_dmi_facts("\n") == {}



# Generated at 2022-06-13 01:08:39.451456
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    hardware = SunOSHardware()
    hardware.module = AnsibleModule(argument_spec=dict())
    hardware.module.run_command = MagicMock()
    hardware.module.run_command.return_value = (0, mock_prtconf, '')
    hardware.get_memory_facts()
    expected = {
        "memtotal_mb": 263168,
    }
    assert hardware.facts == expected


# Generated at 2022-06-13 01:08:43.434216
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = MagicMock()
    hardware = SunOSHardware(module)
    result = hardware.get_dmi_facts()
    assert result['system_vendor'] == 'Oracle Corporation'

# Generated at 2022-06-13 01:08:55.307422
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    ''' Unit test for method get_dmi_facts of class SunOSHardware
    '''
    class FakeModule(object):
        def __init__(self):
            self.run_command_sentinel = True

# Generated at 2022-06-13 01:09:07.337266
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    test_BinModule = type('test_BinModule', (object,), {
        'run_command': lambda self, cmd: (0, '''module: cpu_info
instance: 0
chip_id: 0
core_id: 0
clock_MHz: 2900
brand: UltraSPARC-T1 (Niagara)
impl_name: Sun Microsystems, Inc.
implementation: 1
chip_type: sun4v
chip_rev: 1.0
stick_type: 10
stick_rev: 1.0''', None),
        'get_bin_path': lambda self, *args: '/usr/bin/kstat'
    })

# Generated at 2022-06-13 01:09:18.494138
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # We don't care about the module, just the output of the facts.
    # So we mock the module and then call the method.
    module = type('AnsibleModule', (object,), {'run_command': run_command_mock})

    # To test the output, we need the output from prtconf, swap -s and swap -l
    prtconf_out = """Memory size: 32768 Megabytes
"""
    swap_s_out = """total: 34432k bytes allocated + 22876k reserved = 57312k used, 414748k available
"""
    swap_l_out = """"swapfile"   16384   32768   32768  -  "swapfile"
"""


# Generated at 2022-06-13 01:09:30.610212
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:09:53.390252
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():

    # arrange
    m = SunOSHardware()
    m.module.run_command = MagicMock(return_value=(0, 'Physical memory size: 1024 Megabytes', None))
    # act
    response = m.get_memory_facts()

    # assert
    assert 'memtotal_mb' in response
    assert response['memtotal_mb'] == 1024


# Generated at 2022-06-13 01:09:58.016167
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    import datetime

    # Load json facts data
    json_data = {}
    json_data['datetime'] = {'date': datetime.datetime(2018, 1, 12, 19, 45, 37, tzinfo=datetime.timezone.utc), 'timezone': datetime.timezone(datetime.timedelta(0), 'UTC')}
    json_data['cmdline'] = []
    json_data['system'] = 'SunOS'
    json_data['python'] = {}
    json_data['python']['executable'] = '/usr/local/bin/python3'

# Generated at 2022-06-13 01:10:09.241444
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})


# Generated at 2022-06-13 01:10:18.026761
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = FakeAnsibleModule()
    sunos_hardware_obj = SunOSHardware(module=module)

    # Returned correct product name, vendor and revision on SunOS system
    result = sunos_hardware_obj.get_dmi_facts()
    assert result['product_name'] == 'Sun Fire X4470'
    assert result['system_vendor'] == 'Oracle Corporation'

    # Returned blank product name and vendor on Linux system
    module.run_command_output.append('System Configuration:  Supermicro X11SCL/X11SCL-F')
    result = sunos_hardware_obj.get_dmi_facts()
    assert 'product_name' not in result
    assert 'system_vendor' not in result



# Generated at 2022-06-13 01:10:27.251480
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.params = {'fact_path': '/etc/ansible/facts.d'}
    facts_obj = SunOSHardware(module)
    memory_facts_dict = facts_obj.get_memory_facts()
    assert isinstance(memory_facts_dict, dict)
    assert 'memtotal_mb' in memory_facts_dict
    assert 'swapfree_mb' in memory_facts_dict
    assert 'swaptotal_mb' in memory_facts_dict
    assert 'swap_allocated_mb' in memory_facts_dict
    assert 'swap_reserved_mb' in memory_facts_dict

# Generated at 2022-06-13 01:10:36.367958
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware = SunOSHardware()
    hardware_facts = hardware.populate()
    assert 'memtotal_mb' in hardware_facts
    assert 'processor' in hardware_facts
    assert 'processor_count' in hardware_facts
    assert 'processor_cores' in hardware_facts
    assert 'swapfree_mb' in hardware_facts
    assert 'swaptotal_mb'  in hardware_facts
    assert 'swap_allocated_mb' in hardware_facts
    assert 'swap_reserved_mb' in hardware_facts
    assert 'system_vendor' in hardware_facts
    assert 'product_name' in hardware_facts


# Generated at 2022-06-13 01:10:45.415199
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Load the kstat output
    kstat = '''
module:    cpu_info
instance:  0
class:     misc
chip_id:   0
core_id:   0
clock_MHz: 3200
brand:     sun4u
implementation:  SPARC64-VI
chip    :  SUNW,SPARC-Enterprise-T5220

module:    cpu_info
instance:  1
class:     misc
chip_id:   0
core_id:   1
clock_MHz: 3200
brand:     sun4u
implementation:  SPARC64-VI
chip    :  SUNW,SPARC-Enterprise-T5220
'''
    # Create a SunOSHardware object with the cpu_info output
    facter = SunOSHardware()

# Generated at 2022-06-13 01:10:52.424319
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    """
    Test get_dmi_facts method of SunOSHardware class
    """
    collected_facts = dict(ansible_machine='i86pc')
    test_object = SunOSHardware(dict(module=None), collected_facts)

    # Test product name
    dmi_facts_solaris8 = dict(system_vendor='Sun Microsystems', product_name='Sun Fire V210')
    dmi_facts_solaris10 = dict(system_vendor='Oracle Corporation', product_name='Sun Fire X4450')
    dmi_facts_solaris11 = dict(system_vendor='Oracle Corporation', product_name='Sun Fire X4170 M3 Server')
    dmi_facts_virtualbox = dict(system_vendor='Oracle Corporation', product_name='VirtualBox')
    dmi_facts_kvm

# Generated at 2022-06-13 01:11:03.010186
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    facts = SunOSHardware().get_memory_facts()
    assert 'memtotal_mb' in facts, \
        "Failed to retrieve memory_facts, expected key memtotal_mb not found"
    assert 'swap_reserved_mb' in facts, \
        "Failed to retrieve memory_facts, expected key swap_reserved_mb not found"
    assert 'swap_allocated_mb' in facts, \
        "Failed to retrieve memory_facts, expected key swap_allocated_mb not found"
    assert 'swaptotal_mb' in facts, \
        "Failed to retrieve memory_facts, expected key swaptotal_mb not found"
    assert 'swapfree_mb' in facts, \
        "Failed to retrieve memory_facts, expected key swapfree_mb not found"

# Generated at 2022-06-13 01:11:08.001262
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Create an instance of SunOSHardware and call get_cpu_facts
    sun_os_hardware = SunOSHardware()
    cpu_facts = sun_os_hardware.get_cpu_facts()

    assert cpu_facts['processor_count'] > 0
    assert cpu_facts['processor_cores'] > 0

# Generated at 2022-06-13 01:11:34.955272
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    from ansible.module_utils.facts.collector import get_collector_class
    from ansible.module_utils.facts.hardware.sunos import SunOSHardwareCollector
    from ansible.module_utils.facts.hardware.base import Hardware, HardwareCollector

    # Assert class is a subclass of HardwareCollector
    collector_class = get_collector_class("hardware", "SunOS")
    assert issubclass(collector_class, HardwareCollector)

    # Assert class is a subclass of Hardware
    collector_class = get_collector_class("hardware", "SunOS")
    assert issubclass(collector_class.fact_class, Hardware)

    # Assert platform is set correctly
    assert collector_class.platform == "SunOS"

    # Assert required_facts is set correctly

# Generated at 2022-06-13 01:11:45.534683
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware(dict())
    out = """System Configuration: VMware, Inc.              VMware Virtual Platform
        Sun Microsystems  sun4u"""
    facts = hardware.get_dmi_facts(out)
    assert facts['system_vendor'] == 'VMware, Inc.', 'system_vendor'
    assert facts['product_name'] == 'VMware Virtual Platform', 'product_name'

    out = """System Configuration: VMware, Inc.              VMware Virtual Platform"""
    facts = hardware.get_dmi_facts(out)
    assert facts['system_vendor'] == 'VMware, Inc.', 'system_vendor'
    assert facts['product_name'] == 'VMware Virtual Platform', 'product_name'

# Generated at 2022-06-13 01:11:50.836388
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # A list of facts to re-use for every test
    required_facts = {'platform': 'SunOS'}

    # A list of data sets and their respective results

# Generated at 2022-06-13 01:11:58.890884
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # Test get_memory_facts method of class SunOSHardware which
    # calculates swap_allocated_mb, swap_reserved_mb, swaptotal_mb and swapfree_mb
    # swap_reserved_mb = reserved, swap_allocated_mb = allocated, swaptotal_mb = free + used,
    # swapfree_mb = free
    sunos_hardware = SunOSHardware()
    memory_facts = sunos_hardware.get_memory_facts()
    # Make sure the returned facts are integers
    assert memory_facts['swap_allocated_mb'] == 32
    assert memory_facts['swap_reserved_mb'] == 30
    assert memory_facts['swaptotal_mb'] == 48
    assert memory_facts['swapfree_mb'] == 16

# Generated at 2022-06-13 01:12:07.296224
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    out_mock = (
        'Memory size: 16384 Megabytes'
    )
    out_mock2 = '     reserved:   104219488K (  618.67%)\n'\
                '     allocated:   104219488K (  618.67%)\n'\
                '     free:            104K (   0.00%)  1456.12M\n'\
                '     total:       67108864K\n'

    mem_facts = SunOSHardware(module).get_memory_facts(out_mock, out_mock2)

    assert mem_facts['memtotal_mb'] == 16384

# Generated at 2022-06-13 01:12:16.824592
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    setattr(module, 'run_command', global_run_command)
    hardware = SunOSHardware(module)
    device_facts = hardware.get_device_facts()

    # Basic sanity checks for the devices dictionary.
    assert isinstance(device_facts['devices'], dict)
    assert 'sd0' in device_facts['devices']
    assert 'sd1' in device_facts['devices']

    # Device 1 has disk errors, but device 2 does not.
    assert device_facts['devices']['sd1']['hard_errors'] == '23546'
    assert device_facts['devices']['sd1']['soft_errors'] == '16'
    assert device_facts['devices']['sd2']['hard_errors'] == '0'

# Generated at 2022-06-13 01:12:28.025369
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    class TestModule():
        def __init__(self):
            self.run_command_environ_update = {}
            self.run_command_rc = 0
            self.run_command_out = ''
            self.run_command_err = ''

        def run_command(self, command):
            return self.run_command_rc, self.run_command_out, self.run_command_err

    class TestCollector():
        def __init__(self):
            self.module = TestModule()

    # init class to test
    test_obj = SunOSHardware(TestCollector())

    # set test data

# Generated at 2022-06-13 01:12:31.921276
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock
    hw = SunOSHardware()
    hw.module = module

    uptime_facts = hw.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 50000


# Generated at 2022-06-13 01:12:37.811690
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = FakeModule()
    h = SunOSHardware(module)

    memory_facts = h.get_memory_facts(collected_facts=None)

    # Test if the result is a dictionary.
    assert(isinstance(memory_facts, dict))

    # Test if the result looks like this:
    # {'memtotal_mb': 8192, 'swapfree_mb': 1024, 'swaptotal_mb': 2048}
    assert(memory_facts['memtotal_mb'] == 8192)
    assert(memory_facts['swapfree_mb'] == 1024)
    assert(memory_facts['swaptotal_mb'] == 2048)



# Generated at 2022-06-13 01:12:43.306373
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    m = SunOSHardware()
    d = {'devices': {}}

    # Test platform not SunOS
    m.module.params = {'gather_subset': ['hardware'], 'filter': '*'}
    m.module.deprecation('Incorrect test for method get_device_facts!', version='2.11')
    m.module.run_command = mock.Mock(return_value=(0, None, None))
    assert m.get_device_facts() == d

    # Test kstat command not found
    m.module.run_command = mock.Mock(return_value=(1, None, None))
    assert m.get_device_facts() == d

    # Test stderr with no disks

# Generated at 2022-06-13 01:13:06.078872
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class TestUptimeFacts:
        def run_command(self, cmd):
            return (0, "unix:0:system_misc:boot_time    1548249689", "")

    test_uptime = SunOSHardware(TestUptimeFacts())
    uptime_facts = test_uptime.get_uptime_facts()
    assert uptime_facts["uptime_seconds"] > 0

# Generated at 2022-06-13 01:13:10.713490
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()
    hardware.module.run_command = lambda cmd, check_rc=True: (0, 'System Configuration: Oracle Corporation sun4u', None)
    facts = hardware.get_dmi_facts()
    assert facts['system_vendor'] == "Oracle Corporation"
    assert facts['product_name'] == "sun4u"

# Generated at 2022-06-13 01:13:19.349255
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    values = '''
        module:   cpu_info
        module_id:     0
        instance:      0
        class:     misc
        ena:       1
        chip_id:   0
        clock_MHz: 4005
        brand:     sun4u
        cpu_type:  sparcv9
        chip_type: sun4u
        state:     on-line
    '''
    values2 = '''
        module:   cpu_info
        module_id:     0
        instance:      1
        class:     misc
        ena:       1
        chip_id:   0
        clock_MHz: 4005
        brand:     sun4u
        cpu_type:  sparcv9
        chip_type: sun4u
        state:     on-line
    '''


# Generated at 2022-06-13 01:13:30.113740
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    output = """module:       cpu_info
instance:    1
class:       misc
chip_id:     0
clock_MHz:   3200
cpu_type:    AMD Opteron 6274
brand:       AMD Opteron(tm) Processor 6274
module:       cpu_info
instance:    2
class:       misc
chip_id:     0
clock_MHz:   3200
cpu_type:    AMD Opteron 6274
brand:       AMD Opteron(tm) Processor 6274"""

    _mock_module = MockModule()
    hardware = SunOSHardware(_mock_module)

    hardware.get_cpu_facts()

    expected_results = {'processor': ['AMD Opteron(tm) Processor 6274', 'AMD Opteron(tm) Processor 6274']}

# Generated at 2022-06-13 01:13:34.134365
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    test_data = 'System Configuration: VMware, Inc. VMware Virtual Platform'
    ah = SunOSHardware({'module_setup': True}, [test_data], 'SunOS')
    assert ah.get_dmi_facts() == {'system_vendor': 'VMware, Inc.', 'product_name': 'VMware Virtual Platform'}

# Generated at 2022-06-13 01:13:38.413153
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    test_module = type('AnsibleModule', (object,), {'run_command': get_uptime_facts_run_command_mock})
    test_class = type('SunOSHardware', (SunOSHardware,), {'module': test_module})
    test_class.populate()
    uptime_facts = test_class.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 54321


# Generated at 2022-06-13 01:13:51.191959
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    import sys

    if sys.version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO

    module = SunOSHardwareCollector._create_module_mock()
    module.run_command_environ_update = {}
    cpu_facts = {'processor_count': 1, 'processor_cores': 1, 'processor': []}
    memory_facts = {'memtotal_mb': 2000, 'swaptotal_mb': 2000, 'swapfree_mb': 2000, 'swap_reserved_mb': 2000, 'swap_allocated_mb': 2000}
    dmi_facts = {'system_vendor': 'Test', 'product_name': 'Me'}
    device_facts = {'devices': {}}

# Generated at 2022-06-13 01:13:56.089360
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    mock_module = type('MockModule', (), {'run_command': MagicMock()})
    mock_module.run_command.return_value = (0, '', '')
    facts = SunOSHardware(mock_module).populate()
    assert facts['processor'] == ['Fujitsu SPARC Enterprise T5440 @ 1600MHz']
    assert facts['memtotal_mb'] == 147456
    assert facts['swapfree_mb'] == 0
    assert facts['swaptotal_mb'] == 0
    assert facts['swap_allocated_mb'] == 0
    assert facts['swap_reserved_mb'] == 0


# Generated at 2022-06-13 01:14:03.378769
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """SunOSHardware - returns content of solaris specific facts"""
    module = FakeModule({'ansible_system_vendor': 'Oracle Corporation', 'ansible_product_name': 'T5120', 'ansible_machine': 'sparcv9'})
    hardware = SunOSHardware(module)
    facts = hardware.populate()
    assert facts['system_vendor'] == 'Oracle Corporation'
    assert facts['product_name'] == 'T5120'
    assert facts['processor_cores'] == 'NA'
    assert facts['processor_count'] == 1
    assert facts['processor'] == ['SUNW,UltraSPARC-T1 @ 1200MHz']
    assert facts['memtotal_mb'] == 4096
    assert facts['swapfree_mb'] == 0
    assert facts['swaptotal_mb'] == 0
    assert facts

# Generated at 2022-06-13 01:14:12.434820
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    dmi_facts = {
        'system_vendor': 'Oracle Corporation',
        'product_name': 'SUNW,SPARC-Enterprise-T5240'
    }
    raw_prtdiag_output = """
System Configuration:  Oracle Corporation SUNW,SPARC-Enterprise-T5240
System Configuration:  Oracle Corporation Unknown product SunOS 5.11 11.3 sparc
System Configuration:  QEMU Standard PC (i440FX + PIIX, 1996)
System Configuration:  Oracle Corporation Unknown product SunOS 5.11 11.3 sparc
System Configuration:  Oracle Corporation SUNW,SPARC-Enterprise-T5240
System Configuration:  Oracle Corporation Unknown product SunOS 5.11 11.3 sparc"""
    sunoshw = SunOSHardware()
    sunoshw.module = get_mock_object()


# Generated at 2022-06-13 01:15:10.872683
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    s = SunOSHardware()

    disk_stats = {
        'Product': 'product',
        'Revision': 'revision',
        'Serial No': 'serial',
        'Size': 'size',
        'Vendor': 'vendor',
        'Hard Errors': 'hard_errors',
        'Soft Errors': 'soft_errors',
        'Transport Errors': 'transport_errors',
        'Media Error': 'media_errors',
        'Predictive Failure Analysis': 'predictive_failure_analysis',
        'Illegal Request': 'illegal_request',
    }

    s.get_device_facts()



# Generated at 2022-06-13 01:15:14.973739
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():

    hardware_facts = SunOSHardware.get_memory_facts(None)

    assert isinstance(hardware_facts, dict)
    assert ['memtotal_mb', 'swapfree_mb', 'swaptotal_mb', 'swap_allocated_mb', 'swap_reserved_mb'] == list(hardware_facts.keys())



# Generated at 2022-06-13 01:15:21.949532
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = type('test', (object,), {})()
    module.run_command = mock_run_command

    sunos_hardware = SunOSHardware(module)
    result = sunos_hardware.get_device_facts()

    assert result['devices']['sda']['product'] == 'VBOX HARDDISK'
    assert result['devices']['sda']['revision'] == '1.0'
    assert result['devices']['sda']['serial'] == 'VB0ad2ec4d-074a'
    assert result['devices']['sda']['size'] == '50.00 GB'
    assert result['devices']['sda']['vendor'] == 'ATA'

# Generated at 2022-06-13 01:15:25.426383
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    m_class_instance = SunOSHardware()
    m_class_instance.module.run_command = lambda *args, **kwargs: (0, 'Memory size: 4134 Megabytes', '')

    assert m_class_instance.get_memory_facts() == {'memtotal_mb': 4134}

# Generated at 2022-06-13 01:15:36.054801
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:15:43.249034
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    This method unit tests populate method of class SunOSHardware.
    """
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts.collector import TestModule
    from ansible.module_utils.facts.utils import TestInputModule

    test_module = TestModule(TestInputModule())

    # test
    sunos_hw = SunOSHardware(test_module)
    results = sunos_hw.populate()

    assert 'memtotal_mb' in results
    assert 'swapfree_mb' in results
    assert 'swaptotal_mb' in results
    assert 'swap_allocated_mb' in results
    assert 'swap_reserved_mb' in results
    assert 'system_vendor' in results

# Generated at 2022-06-13 01:15:48.488466
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    cpu_facts = SunOSHardware().get_cpu_facts()

    # assert the cpu_facts keys
    assert set(cpu_facts.keys()) == set(['processor_count', 'processor', 'processor_cores'])

    # assert the cpu_facts values
    assert cpu_facts['processor_count'] >= 1
    assert cpu_facts['processor_cores'] >= 1
    assert cpu_facts['processor']
    assert len(cpu_facts['processor']) == cpu_facts['processor_count']

# Generated at 2022-06-13 01:15:57.108899
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class SunOSHardwareMock(SunOSHardware):
        def __init__(self):
            pass

        def run_command(self, args):
            class ProcessResultMock:
                def __init__(self, rc, out, err):
                    self.rc = rc
                    self.stdout = out
                    self.stderr = err
            if args == '/usr/bin/uname -i':
                return(0, 'foosparc', '')
            elif args == '/usr/platform/foosparc/sbin/prtdiag':
                return ProcessResultMock(
                    0, 'System Configuration: \nSun Microsystems sun4u', '')

# Generated at 2022-06-13 01:16:05.184895
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = FakeAnsibleModule()
    hardware = SunOSHardware(module)

    uname_output = """SunOS
5.11
11.4
generic_147147-11
i86pc"""

# Generated at 2022-06-13 01:16:13.178866
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    import sys, os, json
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts.utils import get_file_content
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dmi_facts  = SunOSHardware().get_dmi_facts()
    # get the content of the file /etc/release
    release_content = get_file_content('/etc/release')
    # create a dictionary with the content of the file /etc/release
    release_dict = {}
    release_dict['content']=release_content
    # print to json
    # print json.dumps(release_dict, indent=2)
    # print json.dumps(dmi