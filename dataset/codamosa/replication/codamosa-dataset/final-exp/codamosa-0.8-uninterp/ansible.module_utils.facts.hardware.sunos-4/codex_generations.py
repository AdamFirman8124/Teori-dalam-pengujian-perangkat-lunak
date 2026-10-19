

# Generated at 2022-06-13 01:06:41.182013
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})

    p = subprocess.Popen(["/usr/bin/kstat", "-p"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    module.run_command = Mock(return_value=(0, out, err))

    hardware = SunOSHardware(module)
    result = hardware.get_device_facts()


# Generated at 2022-06-13 01:06:53.580295
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts.hardware.sunos import SunOSHardwareCollector

    # Mock the run_command method in order to provide faked data
    SunOSHardware.run_command = staticmethod(lambda self, cmd: (0, to_bytes('1548249689'), ''))

    # The 'platform' fact is required in order to initialize a SunOSHardware object
    collected_facts = {'platform': 'SunOS'}
    sunos_hw = SunOSHardwareCollector.fetch_facts(SunOSHardware, collected_facts)
    uptime_seconds = sunos_hw.get('uptime_seconds')

# Generated at 2022-06-13 01:07:02.497895
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """
    Unit test for method get_device_facts of class SunOSHardware
    """
    device_facts = {}
    device_facts['devices'] = {}

    disk_stats = {
        'Product'              : 'product',
        'Revision'             : 'revision',
        'Serial No'            : 'serial',
        'Size'                 : 'size',
        'Vendor'               : 'vendor',
        'Hard Errors'          : 'hard_errors',
        'Soft Errors'          : 'soft_errors',
        'Transport Errors'     : 'transport_errors',
        'Media Error'          : 'media_errors',
        'Predictive Failure Analysis' : 'predictive_failure_analysis',
        'Illegal Request'      : 'illegal_request',
    }


# Generated at 2022-06-13 01:07:08.111995
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():

    device_facts_cmd = '''/usr/bin/kstat -p sderr:::'Size' sderr:::'Product' sderr:::'Revision' sderr:::'Serial No' sderr:::'Vendor' sderr:::'Hard Errors' sderr:::'Soft Errors' sderr:::'Transport Errors' sderr:::'Media Error' sderr:::'Predictive Failure Analysis' sderr:::'Illegal Request' '''

    # Test the function with Size, Product, Serial No, Vendor, Revision, Hard Errors, Soft Errors, Transport Errors, Media Errors, Predictive Failure Analysis, Illegal Request
    # Return value of the kstat in a dictionary


# Generated at 2022-06-13 01:07:19.374681
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = FakeModule()
    sunos_hardware = SunOSHardware(module)
    collected_facts = {'ansible_lsb': {'distcodename': 'x86', 'distdescription': 'Oracle Solaris 11.4', 'distid': 'Solaris', 'distrelease': '11.4', 'distrib_codename': 'x86', 'distrib_description': 'Oracle Solaris 11.4', 'distrib_id': 'Solaris', 'distrib_release': '11.4', 'majdistrelease': '11', 'release': '11.4'}}

    assert sunos_hardware.get_cpu_facts(collected_facts) == {'processor': ['SPARC-T3 (chipid 0, clock 1200 MHz) @ 1200MHz']}


# Generated at 2022-06-13 01:07:31.710910
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.test_hardware_collector import MockModule
    from ansible.module_utils.facts import hardware as hw_mod

    module = MockModule()

    # Mock output of command /usr/bin/uname -i
    module.run_command.return_value = (0, 'i86pc', '')

    # Mock of prtdiag
    module.get_bin_path.return_value = './test/unit/module_utils/facts/hardware/test_files/prtdiag_output'

    # Actual prtdiag(1m) command is not run
    hw = hw_mod.SunOSHardware(module)
    dmi_facts = hw.get_dmi_facts()


# Generated at 2022-06-13 01:07:38.251194
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    with open('/usr/sbin/prtconf') as f:
        # prtconf -pv | head -1
        mem_size = f.read().splitlines()[0]

    # /usr/sbin/swap -s
    swap_size = 'total: 170860k bytes allocated + 160660k reserved = 331520k used, 7170880k available'


# Generated at 2022-06-13 01:07:46.751897
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    m = SunOSHardware(None)
    cpu_facts = m.get_cpu_facts()

    # The dictionary returned by get_cpu_facts should have the following keys
    assert len(cpu_facts.keys()) == 4
    assert 'processor' in cpu_facts
    assert 'processor_count' in cpu_facts
    assert 'processor_cores' in cpu_facts

    # The processor key should contain a list of strings
    assert isinstance(cpu_facts['processor'], list)
    for string in cpu_facts['processor']:
        assert isinstance(string, str)

    # The keys processor_count and processor_cores should contain integers
    assert isinstance(cpu_facts['processor_count'], int)
    assert isinstance(cpu_facts['processor_cores'], int)



# Generated at 2022-06-13 01:07:52.767073
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.timeout import Timeout

    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, args, environ_update=None, check_rc=False, close_fds=True, binary_data=False, cwd=None):
            if args == ['/usr/sbin/prtconf']:
                return (0, get_file_content('tests/unit/module_utils/facts/hardware/sunos/prtconf.out'), '')

# Generated at 2022-06-13 01:08:01.691783
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, executable, opt_dirs=[]):
            return "/usr/bin/%s" % executable

        def run_command(self, executable, run_command_environ_update=None):
            return 0, '', ''

    def mock_time():
        return 42

    test_module = MockModule()
    test_sunos_hardware = SunOSHardware(test_module)

    test_sunos_hardware.run_command = test_module.run_command
    test_sunos_hardware.get_bin_path = test_module.get_bin_path
    test_sunos_hard

# Generated at 2022-06-13 01:08:25.201324
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec=dict())
    sunos_hardware = SunOSHardware(module)
    result = sunos_hardware.get_device_facts()
    assert isinstance(result, dict)
    # output varies between different VMs, only testing the data type
    assert 'devices' in result
    assert isinstance(result['devices'], dict)
    assert len(result['devices']) > 0

# Generated at 2022-06-13 01:08:27.433507
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)
    status = hardware.populate()

# Generated at 2022-06-13 01:08:31.991287
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    facts = SunOSHardware()
    # Method is not implemented or used, just check that it doesn't fail
    facts.get_cpu_facts({'ansible_machine': 'i86pc'})



# Generated at 2022-06-13 01:08:39.945870
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module_params = dict(
        (k, v) for (k, v) in dict(
            run_command=lambda *args, **kwargs:
            (0, 'System Configuration: VMware, Inc. VMware Virtual Platform\n', '')
        ).items() if k in SunOSHardware.get_dmi_facts.__code__.co_varnames
    )

    h = SunOSHardware(module_params)

    dmi_facts = h.get_dmi_facts()
    assert dmi_facts['system_vendor'] == "VMware, Inc."
    assert dmi_facts['product_name'] == "VMware Virtual Platform"

# Generated at 2022-06-13 01:08:53.249850
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    m = SunOSHardware({'RESPONSE_CALLBACK': None, '_ansible_check_mode': False, '_ansible_verbosity': 0, 'ANSIBLE_MODULE_ARGS': {}, 'ANSIBLE_MODULE_NAME': 'setup', 'ANSIBLE_MODULE_CONSTANTS': {}, 'CHECKMODE': False, 'command': '/usr/bin/kstat -p unix:0:system_misc:boot_time', 'command_args': {}, 'chdir': None, 'creates': None, 'executable': None, 'removes': None, 'stdin': None, 'stdin_add_newline': True, 'strip_empty_ends': True, 'warn': True})

# Generated at 2022-06-13 01:09:00.280456
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    m = SunOSHardware()
    dmi_facts = m.get_dmi_facts()
    assert isinstance(dmi_facts, dict)
    assert dmi_facts['system_vendor'] == 'Oracle Corporation'
    assert dmi_facts['product_name'] == 'Oracle VM VirtualBox'


# Generated at 2022-06-13 01:09:10.917823
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # Create instance of class SunOSHardware
    sunos_hw = SunOSHardware(dict())

    # Mock module, So we can determine the output of run_command
    fake_module = type('', (), {'run_command': mock_run_command})

    # Set module to SunOSHardware
    sunos_hw.module = fake_module

    # Call get_memory_facts method and get the result
    # result is a dict
    result = sunos_hw.get_memory_facts()

    # Expected and corresponding result
    expected = {'memtotal_mb': 4095, 'swap_reserved_mb': 0, 'swap_allocated_mb': 0, 'swaptotal_mb': 0, 'swapfree_mb': 0}

    # Assert items in result are the same as items in expected

# Generated at 2022-06-13 01:09:16.147902
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class sunos_hrd:
        def run_command(self, cmd):
            return 0, "unix:0:system_misc:boot_time\t1548249689", ""

    hrd = SunOSHardware()
    hrd.module = sunos_hrd()
    uptime = hrd.get_uptime_facts()
    assert uptime['uptime_seconds'] == int(time.time() - 1548249689)


# Generated at 2022-06-13 01:09:28.778035
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    import os
    import sys
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.timeout import TimeoutError

    # Set up the mock class objects

# Generated at 2022-06-13 01:09:30.821618
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    facts = dict(platform='SunOS')
    hardware_collector = SunOSHardwareCollector(facts, None)
    assert hardware_collector

# Generated at 2022-06-13 01:10:13.589301
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    hardware = SunOSHardware(module)

    """
    For SPARC machine (SunOS)
    """
    # Output of Solaris 10

# Generated at 2022-06-13 01:10:23.642300
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    from ansible.module_utils.basic import AnsibleModule
    sys_argv_original = AnsibleModule.sys_argv

    # Mocking the module args for get_device_facts

# Generated at 2022-06-13 01:10:34.358312
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Create the class
    hardware_object = SunOSHardware(None)

    out = hardware_object.get_cpu_facts()
    assert out['processor_count'] is not None

    out = hardware_object.get_memory_facts()
    assert out['memtotal_mb'] is not None
    assert out['swapfree_mb'] is not None
    assert out['swaptotal_mb'] is not None
    assert out['swap_allocated_mb'] is not None
    assert out['swap_reserved_mb'] is not None

    out = hardware_object.get_dmi_facts()
    assert out['system_vendor'] is not None
    assert out['product_name'] is not None

    out = hardware_object.get_device_facts()
    assert out['devices'] is not None

    out = hardware

# Generated at 2022-06-13 01:10:44.085316
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    test_module = type('AnsibleModule', (object,), {'run_command': run_command_mock})
    test_SunOSHardware = SunOSHardware(test_module)
    cpu_facts = test_SunOSHardware.get_cpu_facts()

    assert cpu_facts['processor'][0] == 'N/A'

    test_module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}
    cpu_facts = test_SunOSHardware.get_cpu_facts()

    assert cpu_facts['processor'][0] == 'SPARC-Enterprise'
    assert cpu_facts['processor'][1] == 'SPARC-Enterprise'
    assert cpu_facts['processor_count'] == 2
    assert cpu_

# Generated at 2022-06-13 01:10:50.993457
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    memory_str = 'Memory size: 8192 Megabytes'
    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand
    prtconf_out = memory_str
    module.run_command.side_effect = [(0, prtconf_out, ''), (0, '', '')]
    sunoshardware_instance = SunOSHardware(module)
    result = sunoshardware_instance.get_memory_facts()
    assert result['memtotal_mb'] == 8192



# Generated at 2022-06-13 01:10:53.951300
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    m = SunOSHardware(module=None)
    facts = m.get_dmi_facts()

    assert 'system_vendor' in facts
    assert 'product_name' in facts

# Generated at 2022-06-13 01:11:02.197507
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    def run_command(self, args, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False):
        if args[0] == '/usr/bin/kstat' and args[2] == 'unix:0:system_misc:boot_time':
            return (0, 'unix:0:system_misc:boot_time\t1548249689\n', '')

    setattr(SunOSHardware, 'run_command', run_command)
    assert SunOSHardware(None).get_uptime_facts() == {'uptime_seconds': int(time.time() - 1548249689)}

# Generated at 2022-06-13 01:11:05.819043
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    cpu_facts = SunOSHardware().get_cpu_facts()
    for fact in ['processor_count', 'processor_cores', 'processor']:
        assert fact in cpu_facts


# Generated at 2022-06-13 01:11:12.258628
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # Mock a class for testing
    class MockModule:
        def __init__(self):
            pass

        @staticmethod
        def run_command(cmd):
            return 0, 'unix:0:system_misc:boot_time    1548249689', None

    # Create instance of mocked class
    uptime_facts = SunOSHardware(MockModule())

    # Test the result
    assert uptime_facts.get_uptime_facts() == {'uptime_seconds': 1548250211}

# Generated at 2022-06-13 01:11:19.825848
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = SunOSHardware(module)
    hardware_facts = hardware.populate()

    assert hardware_facts.get('processor')
    assert hardware_facts.get('memtotal_mb')
    assert hardware_facts.get('swapfree_mb')
    assert hardware_facts.get('swaptotal_mb')
    assert hardware_facts.get('swap_allocated_mb')
    assert hardware_facts.get('swap_reserved_mb')
    assert hardware_facts.get('system_vendor')
    assert hardware_facts.get('product_name')
    assert hardware_facts.get('devices')
    assert hardware_facts.get('uptime_seconds')


# Generated at 2022-06-13 01:12:34.338658
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:12:45.187315
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:12:56.029922
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:13:04.603232
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hw = SunOSHardware(None)

    # test case 1
    rc1 = 0
    out1 = """
module:    0          cpu_info
instance:  0
class:     misc
chip_id:   0
core_id:   0
clock_MHz: 1700.000
implementation: sun4v
brand:     SPARC-T4
architecture: SPARC (littlenum)
ncpu_per_chip: 1
ncpu_per_board: 8
ncore_per_chip: 4
ncore_per_board: 32
"""
    err1 = ""
    hw.module.run_command = Mock(return_value=(rc1, out1, err1))

    # test case 2
    rc2 = 0

# Generated at 2022-06-13 01:13:15.387384
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:13:17.869525
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    hardware = SunOSHardware(module=module)
    hardware.populate()


# Generated at 2022-06-13 01:13:24.476395
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock()
    module.run_command_environ_update = {}

    # SunOSHardware.populate will call SunOSHardware.get_cpu_facts,
    # SunOSHardware.get_memory_facts, SunOSHardware.get_dmi_facts,
    # SunOSHardware.get_device_facts, SunOSHardware.get_uptime_facts and
    # SunOSHardware.get_mount_facts
    sysctl_path = get_file_content("fixtures/units/ansible_fact/hardware/sunos/sysctl.txt")
    prtconf_path = get_file_content("fixtures/units/ansible_fact/hardware/sunos/prtconf.txt")

# Generated at 2022-06-13 01:13:32.630437
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    ''' Testing get_memory_facts() of SunOSHardware class '''
    test_obj = SunOSHardware()
    test_obj.module = AnsibleModuleMock(dict(command_timeout=10, run_command="/usr/sbin/prtconf"))
    test_obj.module.run_command.return_value = (0, 'Memory size: 16384 Megabytes', '')
    output = test_obj.get_memory_facts()
    assert output['memtotal_mb'] == 16384
    test_obj.module.run_command.assert_called_with("/usr/sbin/prtconf")


# Generated at 2022-06-13 01:13:37.988394
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    ansible_module = AnsibleModuleMock
    hardware = SunOSHardware(ansible_module)
    dmi_facts = hardware.get_dmi_facts()
    assert isinstance(dmi_facts, dict)
    assert dmi_facts['system_vendor'] == 'Sun Microsystems'
    assert isinstance(dmi_facts['system_vendor'], str)
    assert dmi_facts['product_name'] == 'Netra X1'
    assert isinstance(dmi_facts['product_name'], str)


# Generated at 2022-06-13 01:13:39.016319
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    hp = SunOSHardware()
    facts = hp.get_uptime_facts()
    assert facts['uptime_seconds'] > 0