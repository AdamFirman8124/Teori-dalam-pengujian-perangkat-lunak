

# Generated at 2022-06-13 01:06:34.213384
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )
    hardware = SunOSHardware(module)

    system_vendor = hardware.get_dmi_facts()['system_vendor']

    # FIXME
    status = 0
    if system_vendor == 'Sun Microsystems':
        status = 1

    assert status == 1

# Generated at 2022-06-13 01:06:45.651880
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = FakeAnsibleModule()
    module.get_bin_path.return_value = 'test_real_path'
    # SunOS 8
    module.run_command.return_value = [0,
                                       'System Configuration: Sun Microsystems sun4u\n',
                                       '']
    SunOSHardware(module).populate()
    assert module.fail_json.call_count == 0
    assert module.exit_json.call_count == 1
    assert module.exit_json.call_args[0][0]['ansible_system_vendor'] == 'Sun Microsystems'
    assert module.exit_json.call_args[0][0]['ansible_product_name'] == 'sun4u'
    # SunOS 9

# Generated at 2022-06-13 01:06:51.626111
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    test_inst = SunOSHardware(dict())

    test_inst.module = mock.MagicMock()
    test_inst.module.run_command = MagicMock(return_value=(0, "unix:0:system_misc:boot_time 1548249689", ""))

    assert test_inst.get_uptime_facts() == {'uptime_seconds': 1234567}

# Generated at 2022-06-13 01:07:01.161425
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class module:
        def __init__(self, run_command_side_effect=None, current_time=None):
            self._run_command_side_effect = run_command_side_effect
            self._current_time = current_time

        def run_command(self, args):
            return self._run_command_side_effect(args)

    class fact_collector:
        def __init__(self):
            self.get = dict()

        def __getitem__(self, key):
            return self.get[key]

        def __setitem__(self, key, value):
            self.get[key] = value

    fact_collector = fact_collector()

    # Test return uptime_facts and set uptime_seconds to None

# Generated at 2022-06-13 01:07:07.208700
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class fakeClass(object):
        class module(object):
            verbose_override = 0
            def __init__(self, verbose_override=None):
                self.verbose_override = verbose_override

            def get_option(self, option):
                return self.verbose_override

            def run_command(self, cmd):
                class Return(object):
                    def __init__(self):
                        self.rc = 0
                        self.stdout = """
System Configuration: Sun Microsystems  sun4u
System clock frequency: 120000000 Hz
Memory size: 2097152 Kbytes
"""
                        self.stderr = None
                return Return()
    test = fakeClass()
    test2 = SunOSHardware(test)
    results = test2.get_dmi_facts()
    assert results

# Generated at 2022-06-13 01:07:18.685506
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock()
    hardware_obj = SunOSHardware(module)
    hardware_obj.populate()
    assert hardware_obj.ansible_facts['ansible_devices']['sd0']['size'] == "50G"
    assert hardware_obj.ansible_facts['ansible_devices']['sd0']['revision'] == "1.0"
    assert hardware_obj.ansible_facts['ansible_devices']['sd0']['vendor'] == "ATA"
    assert hardware_obj.ansible_facts['ansible_processor'][0].startswith('SPARC')
    assert hardware_obj.ansible_facts['ansible_processor_count'] == 1
    assert hardware_obj.ansible_facts['ansible_processor_cores'] == 'NA'
   

# Generated at 2022-06-13 01:07:26.535381
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    test_file_path = os.path.join(os.path.dirname(__file__), 'unit', 'test_data', 'SunOSHardware.get_cpu_facts')
    cpu_facts = {'processor_cores': 2,
                 'processor_count': 2,
                 'processor': ['AMD Opteron Processor 4226 @ 1250MHz']}
    check_results(test_file_path, 'get_cpu_facts', cpu_facts)



# Generated at 2022-06-13 01:07:35.857803
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """ Test the SunOSHardware method get_device_facts.  """
    module = None
    test = SunOSHardware(module)
    # load kstat output
    with open('./unit/tests/module_extras/sunos_sderr.txt', 'r') as f:
        sderr = f.read()

    result = test.get_device_facts({'kstat_sderr': sderr})

    # expected output.

# Generated at 2022-06-13 01:07:37.923984
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    # Set up a test object
    hardware_collector = SunOSHardwareCollector()

    # Verify that the test object is properly set up
    assert hardware_collector.required_facts == {'platform'}
    assert hardware_collector._platform == 'SunOS'


# Generated at 2022-06-13 01:07:44.001092
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = type('MockModule', (object,), {'run_command': MagicMock()})()
    mock_module_function = MagicMock(return_value=(0, 'unix:0:system_misc:boot_time    1548249689', ''))
    module.run_command = mock_module_function
    s = SunOSHardware(module)
    results = s.get_uptime_facts()
    assert results['uptime_seconds'] == int(time.time() - 1548249689)

# Generated at 2022-06-13 01:08:12.709413
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    import platform

    h = SunOSHardware(dict())

    def get_bin_path_stub(*args, **kwargs):
        if args[0] == 'prtdiag':
            return "./test/unit/ansible_collections/ansible/community/plugins/modules/facts/hardware/prtdiag_" + platform.uname()[0] + '_' + platform.uname()[4]

    h.module.get_bin_path = get_bin_path_stub

    expected_dmi_facts = {'system_vendor': 'VMware, Inc.',
                          'product_name': 'VMware Virtual Platform',
                          'ansible_product_name': 'VMware Virtual Platform',
                          'ansible_system_vendor': 'VMware, Inc.'}

    assert h

# Generated at 2022-06-13 01:08:15.934073
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    h = SunOSHardware({'run_command': CommandMock})
    out = h.get_dmi_facts()

    assert out['system_vendor'] == 'Fujitsu'
    assert out['product_name'] == 'SPARC Enterprise M3000 Server'



# Generated at 2022-06-13 01:08:23.829960
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # Instanciate the class
    hardware = SunOSHardware(None)

    # set prtconf output when it's OracleVM
    hardware.module.run_command_environ_update = {'LANG': 'C'}
    hardware.module.run_command.return_value = 0, 'System Configuration: Oracle Corporation VirtualBox', ''

    assert hardware.get_dmi_facts() == {
        'system_vendor': 'Oracle Corporation',
        'product_name': 'VirtualBox'
    }

    # set prtconf output when it's not OracleVM
    hardware.module.run_command.return_value = 0, 'System Configuration: Sun Microsystems sunw,Sun-Fire-T200', ''


# Generated at 2022-06-13 01:08:30.835996
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    facts = SunOSHardware.get_dmi_facts()
    assert isinstance(facts, dict)
    assert isinstance(facts['system_vendor'], str)
    assert isinstance(facts['product_name'], str)

if __name__ == '__main__':
    # Unit test for method get_dmi_facts of class SunOSHardware
    test_SunOSHardware_get_dmi_facts()

# Generated at 2022-06-13 01:08:35.663503
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})

    hardware_facts_instance = SunOSHardware(module)
    hardware_facts = hardware_facts_instance.populate()
    assert 'cpu_facts' in hardware_facts.keys()
    assert 'memtotal_mb' in hardware_facts.keys()
    assert 'swapfree_mb' in hardware_facts.keys()
    assert 'swaptotal_mb' in hardware_facts.keys()
    assert 'swap_allocated_mb' in hardware_facts.keys()
    assert 'swap_reserved_mb' in hardware_facts.keys()
    assert 'system_vendor' in hardware_facts.keys()
    assert 'product_name' in hardware_facts.keys()
    assert 'devices' in hardware_facts.keys()
    assert 'mounts' in hardware_facts

# Generated at 2022-06-13 01:08:41.839379
# Unit test for method populate of class SunOSHardware

# Generated at 2022-06-13 01:08:54.368489
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()

    c = SunOSHardware(module=module)

    sample_kstat_cpu_info = """
cpu_info:
module: 0
instance: 0
clock_MHz:	2400.000
cpu_type:	sparc
brand:		SPARC-T4
fpu_type:	sparc_vis3
implementation:	SUNW,SPARC-T4
chip_id:	0
ncpu:		4
chip_type:	SPARC-T4
state:		on-line
board_rev:	0x01
board_serial:	<empty string>
"""

    module.run_command.return_value = (0, sample_kstat_cpu_info, None)
    cpu_facts = c.get_cpu_facts()

# Generated at 2022-06-13 01:09:02.389384
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    fact_module = SunOSHardware(dict())
    out = 'unix:0:system_misc:boot_time	1548249689'
    props = {"run_command.return_value": (0, out, None)}
    fact_module.module = MagicMock(**props)
    uptime_facts = fact_module.get_uptime_facts()
    assert 'uptime_seconds' in uptime_facts
    assert uptime_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 01:09:05.320536
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    h_collector = SunOSHardwareCollector()
    assert h_collector._fact_class == SunOSHardware
    assert h_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:09:07.654802
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    result = get_device_facts()
    assert 'devices' in result
    assert type(result['devices']) == dict
    return

# Generated at 2022-06-13 01:09:32.351095
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    test_module = type('', (), {'run_command': lambda x: ('', 'System Configuration: Sun Microsystems  sun4v', '')})()
    hw = SunOSHardware(test_module)
    assert hw.get_dmi_facts() == {'system_vendor': 'Sun Microsystems', 'product_name': 'sun4v'}


# Generated at 2022-06-13 01:09:34.416158
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    m = SunOSHardware(dict(), dict())
    ut = m.get_uptime_facts()
    assert ut['uptime_seconds'] > 0

# Generated at 2022-06-13 01:09:40.222269
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='/usr/bin/kstat')

    hardware = SunOSHardware(module)
    facts = hardware.get_device_facts()
    assert facts.get('devices'), "Expected devices not found"
    assert facts.get('devices').get('sda'), "Expected sda not found"
    assert facts.get('devices').get('sda').get('size'), "Expected sda size not found"


# Generated at 2022-06-13 01:09:41.551837
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # FIXME: Add tests related to method populate of class SunOSHardware
    assert 1

# Generated at 2022-06-13 01:09:50.374747
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    HAL = SunOSHardware()
    HAL.module = object()

# Generated at 2022-06-13 01:09:57.936909
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    hardware_facts = SunOSHardware()
    dmi_facts = hardware_facts.get_dmi_facts()

    manufacturer = dmi_facts.get('system_vendor')
    productname = dmi_facts.get('product_name')

    assert manufacturer in ['QEMU', 'Oracle Corporation', 'Sun Microsystems', 'Fujitsu', 'VMware, Inc.']
    assert productname in ['VBOX', 'Virtual Machine', 'VirtualBox', 'VirtualBox VM']

# Generated at 2022-06-13 01:10:04.552332
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModuleMock()
    module.run_command = AnsibleModuleMock.run_command

    prtconf_output = """System Configuration: VMware, Inc. VMware Virtual Platform
Memory size: 16384 Megabytes"""
    module.run_command.side_effect = [
        (0, "", ""),
        (0, prtconf_output, ""),
        (0, "", ""),
        (0, "", "")
    ]

    swap_s_output = """total:  8192k bytes allocated + 2580k reserved = 10772k used, 184224k available
"""
    module.run_command.side_effect = [
        (0, swap_s_output, "")
    ]

    hardware = SunOSHardware()

    facts = hardware.populate()


# Generated at 2022-06-13 01:10:09.740719
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    def run_command(module, command, check_rc=True):
        return 0, "", ""

    SunOSHardware.run_command = run_command
    facts = SunOSHardware(module).populate()
    assert facts['memory']['memtotal_mb'] == 'NA'
    assert facts['memory']['swap_reserved_mb'] == 'NA'
    assert facts['memory']['swap_allocated_mb'] == 'NA'
    assert facts['memory']['swaptotal_mb'] == 'NA'
    assert facts['memory']['swapfree_mb'] == 'NA'
    assert facts['processor'] == []
    assert facts['processor_cores'] == 'NA'
   

# Generated at 2022-06-13 01:10:18.656814
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Arrange
    module = AnsibleModuleMock()
    # In case that the value of module.run_command is known,
    # the value of get_cpu_facts can be verified easily

# Generated at 2022-06-13 01:10:30.193028
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = DummyModule()
    hardware = SunOSHardware(module)
    module.run_command.return_value = (0, "", "")
    rc, out, err = module.run_command.return_value

    # prtconf output: Memory size: 131072 Megabytes
    module.run_command.return_value = (rc, "Memory size: 131072 Megabytes", err)
    memory_facts = hardware.get_memory_facts()

    assert memory_facts.get("memtotal_mb") == 131072

    # swap -s output: allocated   348544, reserved     0, used     1844
    module.run_command.return_value = (rc, "allocated   348544, reserved     0, used     1844", err)
    memory_facts = hardware.get_memory_facts()



# Generated at 2022-06-13 01:10:58.728369
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class FakeModule:
        def run_command(self, cmd):
            out = "System Configuration: Sun Microsystems sun4v\n"
            return 0, out, ''

    fact = SunOSHardware()
    fact.module = FakeModule()
    dmi_facts = fact.get_dmi_facts()

    assert 'system_vendor' in dmi_facts
    assert dmi_facts['system_vendor'] == 'Sun Microsystems'
    assert 'product_name' in dmi_facts
    assert dmi_facts['product_name'] == 'sun4v'

# Generated at 2022-06-13 01:11:06.762913
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    hardware = SunOSHardware(module)
    test_input = '''module: intel
clock_MHz: 2400
chip_id: 0
cpu_type: i386
brand: Genuine Intel(R) CPU     T2080  @ 1.73GHz
implementation: x86
module: intel
clock_MHz: 2400
chip_id: 0
cpu_type: i386
brand: Genuine Intel(R) CPU     T2080  @ 1.73GHz
implementation: x86
'''
    module.run_command.return_value = (0, test_input, '')
    result = hardware.get_cpu_facts()
    assert result['processor_cores'] == 2
    assert result['processor_count'] == 2

# Generated at 2022-06-13 01:11:09.647726
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    expected_result = {'processor': ['Intel(R) Xeon(R) CPU X5660 @ 2.80GHz'],
                       'processor_cores': 2,
                       'processor_count': 1}
    module = DummyModule()
    sunos_hardware = SunOSHardware(module)
    result = sunos_hardware.get_cpu_facts()
    assert result == expected_result



# Generated at 2022-06-13 01:11:12.826970
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    collector = SunOSHardwareCollector()
    assert collector._fact_class == SunOSHardware
    assert collector._platform == 'SunOS'
    assert collector.required_facts == set(['platform'])

# vim: set et ts=4 sw=4:

# Generated at 2022-06-13 01:11:16.873429
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():

    module = object()
    module.run_command = lambda cmd: (0, 'unix:0:system_misc:boot_time    1548249689\n', '')
    sun_hardware = SunOSHardware(module)

    uptime_facts = sun_hardware.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 01:11:18.680082
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    hardware = SunOSHardware()
    hardware.module = MockModule()
    uptime_facts = hardware.get_uptime_facts()
    assert len(uptime_facts) != 0


# Generated at 2022-06-13 01:11:19.801030
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    collector = SunOSHardwareCollector(None)
    assert collector.facts == 'hardware'



# Generated at 2022-06-13 01:11:29.208772
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    sunos_facts = SunOSHardware()
    hostvars = {
        'ansible_machine': 'i86pc',
        'ansible_processor': [],
    }
    facts = sunos_facts.populate(hostvars)
    assert facts['processor_count'] == 1
    assert facts['processor_cores'] == 1
    assert facts['swap_allocated_mb'] > 0
    assert facts['swap_reserved_mb'] > 0
    assert facts['swaptotal_mb'] > 0
    assert facts['swapfree_mb'] > 0
    assert facts['system_vendor'] == 'Sun Microsystems'
    assert 'fstype' in facts['mounts'][0]
    assert 'mount' in facts['mounts'][0]

# Generated at 2022-06-13 01:11:40.764197
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Set up the test environment
    mock_module = MagicMock()
    mock_module.run_command.return_value = 0, output, ''
    mock_module.fail_json.return_value = {}
    mock_module.params = {}
    mock_SunOSHardware = SunOSHardware(mock_module)

    # Call the SunOSHardware method
    cpu_facts = mock_SunOSHardware.get_cpu_facts()

    # Test the results
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 32

# Generated at 2022-06-13 01:11:52.194410
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    hardware_obj = SunOSHardware()


# Generated at 2022-06-13 01:12:43.589724
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    current = int(time.time())
    fake_kstat_out = "unix:0:system_misc:boot_time    {}".format(current - 12345678)

    class fake_module(object):
        def run_command(self, cmd):
            return (0, fake_kstat_out, '')

    h = SunOSHardware(module=fake_module())
    uptime_facts = h.get_uptime_facts()
    assert type(uptime_facts) == dict
    assert 'uptime_seconds' in uptime_facts
    assert uptime_facts['uptime_seconds'] == 12345678


# Generated at 2022-06-13 01:12:54.381506
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:13:01.532857
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    content = "System Configuration:      Sun Microsystems  sun4v\nSystem Configuration:      Sun Microsystems  sun4u"
    hw = SunOSHardware('module')
    hw.module.run_command = lambda self, cmd: (0, content, "")
    hw.module.get_bin_path = lambda self, cmd: "/usr/bin/cmd"

    # Positive testcase
    hw.get_dmi_facts()
    assert hw.facts['dmi']['system_vendor'] == "Sun Microsystems"
    assert hw.facts['dmi']['product_name'] == "sun4u"

    # Negative testcase
    content = "System Configuration:      Sun Microsystems  sun4v\nSystem Configuration:      Sun Microsystems  sun4u"

# Generated at 2022-06-13 01:13:11.735208
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from textwrap import dedent
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible_collections.community.general.plugins.module_utils.facts.facts import FactManager

    def mock_run_command(self, args):
        return (0, dedent('''
        System Configuration: Sun Microsystems sun4u
        '''), '')

    SunOSHardware.run_command = mock_run_command

    fact_manager = FactManager()
    fact_manager._collector_classes[SunOSHardware._platform] = SunOSHardware._fact_class
    fact_manager.collect(['hardware'], cached=False)

    assert fact_manager.facts['hardware']['dmi']['system_vendor'] == 'Sun Microsystems'
    assert fact_manager

# Generated at 2022-06-13 01:13:12.705754
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    hardware = SunOSHardware()



# Generated at 2022-06-13 01:13:19.681673
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # Mock output of command prtdiag
    mock_run_command = (0,
       'System Configuration: Oracle Corporation  Generic X86PC\n'
       'System clock frequency: 2792 MHz\n'
       'Memory size: 8192 Megabytes\n',
       '')

    # Instantiate SunOSHardware class
    sunos_hardware = SunOSHardware(dict(module=dict(run_command=mock_run_command)))

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == dict(system_vendor='Oracle Corporation', product_name='Generic X86PC')


# Generated at 2022-06-13 01:13:22.942758
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    obj = SunOSHardware()

    collected_facts = {'platform': "SunOS",
                       'ansible_machine': "i86pc"}
    facts = obj.populate(collected_facts=collected_facts)

    if not facts:
        assert False, 'CPU facts not populated'
    if not facts['processor']:
        assert False, 'Processor is not populated'

# Generated at 2022-06-13 01:13:31.459342
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = MockModule()

    # Mock kstat output
    class Kstat:
        def __init__(self):
            self.stdout = "unix:0:system_misc:boot_time    1548249689"
            self.stderr = ""
            self.rc = 0

    module.run_command = lambda x: Kstat()

    # Create the object that will be tested
    x = SunOSHardware(module=module)

    # Run the actual test
    facts = x.get_uptime_facts()

    assert facts['uptime_seconds'] == int(time.time() - 1548249689)

# Generated at 2022-06-13 01:13:39.223025
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    hw = SunOSHardware()

    # Return empty dict if kstat output is empty
    def mock_run_command_kstat_empty_output(*args, **kwargs):
        return 1, "", "Error"
    hw.module.run_command = mock_run_command_kstat_empty_output
    assert hw.get_uptime_facts() == {}

    # Return uptime_facts if kstat output is correct
    def mock_run_command_kstat_correct_output(*args, **kwargs):
        return 0, "unix:0:system_misc:boot_time    1548249689", ""
    hw.module.run_command = mock_run_command_kstat_correct_output

# Generated at 2022-06-13 01:13:51.886711
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # The contents of test_out is in a format that mimics the output of kstat
    # for unix:0:system_misc:boot_time. This output would be returned when the
    # uptime has been approximately 1 hour and 24 minutes (5100 seconds).
    test_out = "unix:0:system_misc:boot_time\t1548246489"

    # Create an instance of the SunOSHardware class
    sunoshardware = SunOSHardware()
    uptime = sunoshardware.get_uptime_facts()

    # Get the current time
    current_time = int(time.time())

    # Verify the expected values are returned
    assert "uptime_seconds" in uptime
    assert uptime["uptime_seconds"] == (current_time - 1548246489)

# Generated at 2022-06-13 01:15:52.603657
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class GetDMIFactsTester():
        def __init__(self):
            self.stdout = """System Configuration: Sun Microsystems sun4v"""

        def get_bin_path(self, binary):
            return "/usr/bin/" + binary

        def run_command(self, cmd, *args, **kwargs):
            return 0, self.stdout, ""

    test_sunos_collector = SunOSHardwareCollector()
    test_sunos_instance = test_sunos_collector.collect()

    test_sunos_hardware = SunOSHardware()
    test_sunos_hardware.module = GetDMIFactsTester()

    print(test_sunos_instance)
    assert test_sunos_instance['dmi']['system_vendor'] == 'Sun Microsystems'
    assert test

# Generated at 2022-06-13 01:16:01.223066
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Create mock AnisbleModule object
    module = AnsibleModule(
        argument_spec=dict()
    )

    module.run_command = mock.Mock(return_value=(0, 'kstat cpu_info', ''))
    module.run_command_environ_update = {}
    module.get_bin_path = mock.Mock(return_value='/usr/sbin/prtconf')
    module.run_command = mock.Mock(return_value=(0, 'Memory size: 8192 Megabytes', ''))
    hardware_collector = SunOSHardwareCollector(module=module)
    hardware_collector.collect()
    assert hardware_collector.facts['ansible_processor_count'] == 1


# Generated at 2022-06-13 01:16:09.260854
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock()
    module.run_command = run_command
    module.get_file_content = get_file_content
    module.stat = os.stat
    module.get_bin_path = get_bin_path
    module.get_mount_size = get_mount_size

    hw = SunOSHardware(module)
    facts = hw.populate()

    assert "memtotal_mb" in facts
    assert "memfree_mb" in facts
    assert "swaptotal_mb" in facts
    assert "swapfree_mb" in facts
    assert "swap_allocated_mb" in facts
    assert "swap_reserved_mb" in facts
    assert "processor_count" in facts
    assert "system_vendor" in facts